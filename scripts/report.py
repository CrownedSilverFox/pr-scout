#!/usr/bin/env python3
"""Собрать markdown-отчёт из завершённого прогона PR Scout.

Читает data/last-run-prs.json (строки PR с баллами и вердиктами) и
data/last-run-summary.json, пишет reports/<дата>-<repo>.md.

Использование: python3 scripts/report.py [repo-slug]
"""
import json
import pathlib
import re
import sys
import time

ROOT = pathlib.Path("/home/crnsfx/Work/pr-scout")
SLUG = sys.argv[1] if len(sys.argv) > 1 else "paperclipai__paperclip"
REPO = SLUG.replace("__", "/")

rows = json.loads((ROOT / "data/last-run-prs.json").read_text())
if isinstance(rows, dict):
    rows = rows.get("rows") or []
summary = json.loads((ROOT / "data/last-run-summary.json").read_text())
issues = json.loads((ROOT / "data/last-run-issues.json").read_text()) if (ROOT / "data/last-run-issues.json").exists() else []
forks = json.loads((ROOT / "data/last-run-forks.json").read_text()) if (ROOT / "data/last-run-forks.json").exists() else []
rivals = json.loads((ROOT / "data/last-run-rivals.json").read_text()) if (ROOT / "data/last-run-rivals.json").exists() else {}
runs = summary.get("runs") or []
cfg = summary.get("config") or {}
cost = sum(r.get("cost_usd") or 0 for r in runs)
tokens = sum(r.get("input_tokens") or 0 for r in runs)

KIND = {"bugfix": "фикс", "feature": "фича", "performance": "перф", "security": "безопасность", "refactor": "рефакторинг",
        "docs": "доки", "tests_ci": "тесты/CI", "chore_deps": "обслуживание", "experimental": "эксперимент"}
AREA = (cfg.get("area_labels") or {})


def link(n):
    return f"https://github.com/{REPO}/pull/{n}"


def reasons(r):
    why = (r.get("reasons") or {})
    out = []
    for key, mark in (("skip", "✗"), ("consider", "!"), ("take", "+")):
        for item in why.get(key) or []:
            out.append(f"{mark} {item}")
    return out


def line(r):
    bits = [f"**#{r['number']}** [{r['title']}]({link(r['number'])})",
            f"`{KIND.get(r.get('kind'), r.get('kind'))}` · {AREA.get(r.get('area'), r.get('area'))} · "
            f"автор @{r.get('author')} · балл **{r.get('score')}** · {r.get('additions', 0)}+{r.get('deletions', 0)} строк · "
            f"{r.get('age_days', '—')} дн. · CI: {r.get('ci_class') or '—'}"]
    rev = (r.get("review") or {})
    if rev:
        bits.append("ревью этапа 2: " + ", ".join(f"{k}={v}" for k, v in rev.items()))
    for w in reasons(r):
        bits.append("  - " + w)
    return "\n".join(bits)


by = {"take": [], "consider": [], "skip": [], "nofinal": []}
for r in rows:
    v = r.get("verdict")
    by[v if v in ("take", "consider", "skip") else "nofinal"].append(r)
for v in by:
    by[v].sort(key=lambda r: -(r.get("score") or 0))

out = [f"# PR Scout: {REPO}", "",
       f"Прогон: {len(rows)} PR с баллами, финалистов {summary.get('finalists')}, "
       f"Jev потратил ${cost:.4f} ({tokens} входных токенов).", ""]
for stage in runs:
    out.append(f"- `{stage.get('stage')}`: {stage.get('items')} шт · {stage.get('seconds')} с · ${stage.get('cost_usd')} · ошибок {stage.get('errors')}")
comp = summary.get("comparison")
if comp:
    out += ["", "| вариант | цена |", "|---|---:|"]
    for row in comp["rows"]:
        out.append(f"| {row['name']} | ${row['cost']} |")
out += ["", f"## Берём ({len(by['take'])})", ""]
out += [line(r) + "\n" for r in by["take"]] or ["—"]
out += ["", f"## Рассмотреть ({len(by['consider'])})", ""]
out += [line(r) + "\n" for r in by["consider"][:60]] or ["—"]
out += ["", f"## Пропускаем ({len(by['skip'])})", ""]
out += [line(r) + "\n" for r in by["skip"]] or ["—"]
out += ["", f"## Не дошли до этапа 2 — только балл этапа 1, вердикта нет ({len(by['nofinal'])})", ""]
out += [line(r) + "\n" for r in by["nofinal"][:30]] or ["—"]

if issues:
    open_issues = [i for i in issues if i.get("classified") and not i.get("open_pr")]
    covered = [i for i in issues if i.get("classified") and i.get("open_pr")]
    out += ["", f"# Issues: {len(issues)} открытых, {len(open_issues)} без единого PR", "",
            "## Важное, на что PR нет", ""]
    for i in open_issues[:40]:
        out.append(f"**#{i['number']}** [{i['title']}](https://github.com/{REPO}/issues/{i['number']}) — "
                   f"балл **{i.get('score')}**, `{i.get('kind_label')}`, серьёзность {i.get('severity')}/4, "
                   f"частота {i.get('common_case')}, релевантность {i.get('relevance')}/3, "
                   f"{i.get('comments')} комм. · @{i.get('author')} · обновлено {str(i.get('updated'))[:10]}\n")
    out += ["", f"## Issues, которые уже кто-то закрывает открытым PR ({len(covered)})", ""]
    for i in covered[:25]:
        out.append(f"**#{i['number']}** {i['title']} — балл {i.get('score')}, PR: "
                   + ", ".join(f"[#{n}](https://github.com/{REPO}/pull/{n})" for n in (i.get("open_pr") or [])[:6]) + "\n")

if forks:
    ahead = [f for f in forks if (f.get("ahead") or 0) > 0]
    out += ["", f"# Форки: проверено {len(forks)}, с коммитами впереди upstream — {len(ahead)}", "",
            "## Форки, которые стоит разобрать (в них есть работа, не отправленная в upstream)", ""]
    for f in sorted([f for f in forks if f.get("classified")], key=lambda r: -(r.get("score") or 0))[:40]:
        out.append(f"**[{f['fork']}](https://github.com/{f['fork']})** — балл **{f.get('score')}**, "
                   f"`{f.get('kind_label')}`, впереди {f.get('ahead')} коммитов, позади {f.get('behind')}, "
                   f"±{f.get('lines')} строк, ★{f.get('stars')}, пуш {str(f.get('pushed'))[:10]}, "
                   f"ценность {f.get('value')}/4, дубль {f.get('duplicate')}, секреты {f.get('secrets')}")
        for c in (f.get("commits") or [])[:5]:
            out.append(f"  - `{c.get('sha')}` {c.get('date')} {c.get('message')}")
        out.append("")

if rivals:
    out += ["", f"# Один issue — несколько PR: кого брать ({len(rivals)} групп)", ""]
    for issue_no, r in sorted(rivals.items(), key=lambda kv: -(kv[1].get("confidence") or 0)):
        cands = ", ".join(f"#{n}" for n in (r.get("candidates") or [])[:8])
        verdict = f"[#{r['chosen_pr']}](https://github.com/{REPO}/pull/{r['chosen_pr']})" if r.get("chosen_pr") else "ни один"
        out.append(f"- issue #{issue_no} ({r.get('issue_title') or '—'}): кандидаты {cands} → **берём {verdict}** "
                   f"(уверенность {r.get('confidence')}, proper_fix {r.get('proper_fix')})\n")

d = time.strftime("%Y-%m-%d")
path = ROOT / "reports" / f"{d}-{SLUG.replace('__', '-')}.md"
path.parent.mkdir(exist_ok=True)
path.write_text("\n".join(out))
print(f"отчёт: {path}")
print(f"берём {len(by['take'])}, рассмотреть {len(by['consider'])}, пропускаем {len(by['skip'])}, "
      f"стоимость ${cost:.4f}, токенов {tokens}")
for r in by["take"][:10]:
    print(f"  #{r['number']:<6} {r.get('score'):5} {r['title'][:70]}")
