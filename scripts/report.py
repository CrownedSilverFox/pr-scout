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
# Артефакты прогона лежат в data/ для одного проекта; для нескольких — свой каталог:
#   python3 scripts/report.py <slug> [--dir data/runs/<slug>]
argv = sys.argv[1:]
DIR = ROOT / "data"
if "--dir" in argv:
    DIR = pathlib.Path(argv[argv.index("--dir") + 1])
    argv = [a for i, a in enumerate(argv) if not (a == "--dir" or i == argv.index("--dir") + 1)]
SLUG = argv[0] if argv else "paperclipai__paperclip"
REPO = SLUG.replace("__", "/")

rows = json.loads((DIR / "last-run-prs.json").read_text())
if isinstance(rows, dict):
    rows = rows.get("rows") or []
summary = json.loads((DIR / "last-run-summary.json").read_text())
issues = json.loads((DIR / "last-run-issues.json").read_text()) if (DIR / "last-run-issues.json").exists() else []
forks = json.loads((DIR / "last-run-forks.json").read_text()) if (DIR / "last-run-forks.json").exists() else []
rivals = json.loads((DIR / "last-run-rivals.json").read_text()) if (DIR / "last-run-rivals.json").exists() else {}
runs = summary.get("runs") or []
cfg = summary.get("config") or {}
# P["runs"] накапливает все прогоны за всё время: берём только последний цикл (от последнего fetch).
cycle = []
for r in reversed(runs):
    if r.get("stage") == "fetch" and cycle:
        break
    cycle.append(r)
cycle.reverse()
cost = sum(r.get("cost_usd") or 0 for r in cycle)
tokens = sum(r.get("input_tokens") or 0 for r in cycle)

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
for stage in cycle:
    out.append(f"- `{stage.get('stage')}`: {stage.get('items')} шт · {stage.get('seconds')} с · ${stage.get('cost_usd')} · ошибок {stage.get('errors')}")
comp = summary.get("comparison")
if comp:
    mi = comp["input_tokens"]
    stages = ("stage1", "stage2", "issues", "forks", "rivals")
    out += ["", f"Последний цикл: {tokens} входных токенов, ${cost:.4f}. Все прогоны в истории: "
                f"{mi} токенов, ${sum(r.get('cost_usd') or 0 for r in runs):.4f}.",
            "", "| вариант | цена |", "|---|---:|"]
    out.append(f"| Jev (факт, последний цикл) | ${cost:.4f} |")
    inp = sum(r.get("input_tokens", 0) for r in cycle if r.get("stage") in stages)
    outp = sum(r.get("output_tokens") or 0 for r in cycle) or sum((1000 if r.get("stage") == "stage1" else 1500) * r.get("items", 0) for r in cycle if r.get("stage") in stages)
    for name, (pi, po) in {"Claude Opus 5.5": (4.0, 20.0), "Claude Sonnet 5": (2.0, 10.0), "Claude Haiku 4.5": (1.0, 5.0)}.items():
        c = inp * pi / 1e6 + outp * po / 1e6
        out.append(f"| {name} (оценка на тех же токенах) | ${c:.2f} |")
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
    uniq = [f for f in forks if f.get("classified") and not f.get("duplicate_of")]
    dups = [f for f in forks if f.get("duplicate_of")]
    clusters = {}
    for f in dups:
        clusters.setdefault(f["duplicate_of"], []).append(f["fork"])
    out += ["", f"# Форки: проверено {len(forks)}, с коммитами впереди upstream — {len(ahead)}",
            f"После схлопывания клонов уникальных кандидатов — **{len(uniq)}** "
            f"(клонов одной и той же линии работы: {len(dups)} в {len(clusters)} группах)", "",
            "## Форки, которые стоит разобрать (в них есть работа, не отправленная в upstream)", ""]
    for f in sorted(uniq, key=lambda r: -(r.get("score") or 0))[:40]:
        out.append(f"**[{f['fork']}](https://github.com/{f['fork']})** — балл **{f.get('score')}**, "
                   f"`{f.get('kind_label')}`, впереди {f.get('ahead')} коммитов, позади {f.get('behind')}, "
                   f"±{f.get('lines')} строк, ★{f.get('stars')}, пуш {str(f.get('pushed'))[:10]}, "
                   f"ценность {f.get('value')}/4, дубль {f.get('duplicate')}, секреты {f.get('secrets')}")
        for c in (f.get("commits") or [])[:5]:
            out.append(f"  - `{c.get('sha')}` {c.get('date')} {c.get('message')}")
        out.append("")
    if clusters:
        out += ["## Клоны (та же линия работы, что у представителя)", ""]
        for rep, members in list(clusters.items())[:15]:
            out.append(f"- {rep}: ещё {len(members)} — " + ", ".join(members[:8]))
        out.append("")

stack = json.loads((DIR / "last-run-stack.json").read_text()) if (DIR / "last-run-stack.json").exists() else {}
if stack:
    hot = stack.get("hot") or {}
    out += ["", "# Стек: цена поддержки при мёрдже апстрима", "",
            f"Собрали {stack.get('considered')} выбранных PR ({', '.join(stack.get('verdicts') or [])}) "
            f"последовательно в основную ветку:", "",
            f"- влились чисто: **{stack.get('merged')}**",
            f"- конфликтов при сборке: **{stack.get('conflicted')}** ({stack.get('merge_cost')}%)",
            f"- объём патча: {stack.get('patch', {}).get('files')} файлов, {stack.get('patch', {}).get('shortstat')}",
            f"- поверхность будущих конфликтов: **{hot.get('churn_share')}%** правок upstream за последние "
            f"{hot.get('commits_scanned')} коммитов приходятся на файлы, которые патчит наш стек "
            f"({hot.get('hot_in_stack')} из {hot.get('files_in_stack')} наших файлов)", ""]
    if stack.get("conflicts"):
        out += ["## Что конфликтует", ""]
        for c in stack["conflicts"]:
            out.append(f"- #{c['number']}: " + ", ".join(c.get("files") or [])[:160])
        out.append("")
    if hot.get("hot_top"):
        out += ["## Самые горячие файлы, которые мы патчим (правок upstream за окно)", ""]
        for h in hot["hot_top"][:15]:
            out.append(f"- `{h['file']}` — {h['edits']}")
        out.append("")

if rivals:
    out += ["", f"# Один issue — несколько PR: кого брать ({len(rivals)} групп)", ""]
    for issue_no, r in sorted(rivals.items(), key=lambda kv: -(kv[1].get("confidence") or 0)):
        cands = ", ".join(f"#{n}" for n in (r.get("candidates") or [])[:8])
        verdict = f"[#{r['chosen_pr']}](https://github.com/{REPO}/pull/{r['chosen_pr']})" if r.get("chosen_pr") else "ни один"
        out.append(f"- issue #{issue_no} ({r.get('issue_title') or '—'}): кандидаты {cands} → **берём {verdict}** "
                   f"(уверенность {r.get('confidence')}, proper_fix {r.get('proper_fix')})\n")

mapping = json.loads((DIR / "last-run-map.json").read_text()) if (DIR / "last-run-map.json").exists() else {}
if mapping:
    plans = mapping.get("plans") or {}
    names = {"safe": "Безопасный — максимум по баллу без конфликтов внутри",
             "all_in": "Всё в одно — конфликты разбираем руками",
             "top_score": "Топ по баллу — цена поддержки не важна",
             "low_churn": "Минимум поверхности — что реже ломается апстримом",
             "by_area": "По одному на подсистему — шире, а не глубже"}
    out += ["", "# Карта мёрджей: попарный анализ и расклады", "",
            f"Кандидатов {len(mapping.get('candidates') or mapping.get('candidate_list') or [])} (выжившие PR + лучшие форки), "
            f"пар {mapping.get('pairs')}, живьём мержили пересекающиеся по файлам: {mapping.get('pairs_merged')}, "
            f"смысловое сравнение через Jev: {mapping.get('pairs_semantic')}.", "",
            "| расклад | берём | сумма баллов | конфликтов внутри | файлов | горячих правок |",
            "|---|---:|---:|---:|---:|---:|"]
    for key, title in names.items():
        p = plans.get(key) or {}
        if not p:
            continue
        out.append(f"| **{title}** | {p.get('count')} | {p.get('score_sum')} | {p.get('conflicts')} | "
                   f"{p.get('files')} | {p.get('hot_share')}% |")
    for key, title in names.items():
        p = plans.get(key) or {}
        if not p:
            continue
        out += ["", f"## Расклад: {title}", "",
                f"Берём {p.get('count')} ({p.get('kinds', {}).get('pr', 0)} PR + {p.get('kinds', {}).get('fork', 0)} форков), "
                f"сумма баллов {p.get('score_sum')}, конфликтов внутри {p.get('conflicts')}, "
                f"файлов {p.get('files')}, доля горячих правок {p.get('hot_share')}%.", ""]
        for m in (p.get("members") or [])[:40]:
            out.append(f"- `{m['id']}` [{m['title']}](https://github.com/{REPO}/{'pull' if m['kind'] == 'pr' else ''}"
                       f"{str(m['id']).split('-', 1)[1] if m['kind'] == 'pr' else ''}) — балл {m.get('score')}, "
                       f"{m.get('files')} файлов, {m.get('lines')} строк")
        if p.get("conflict_pairs"):
            out += ["", "  Конфликтные пары внутри расклада: "
                        + ", ".join(f"{x[0]}×{x[1]}" for x in p["conflict_pairs"][:10])]
    if mapping.get("duplicates"):
        out += ["", "## Пары, которые Jev считает одной и той же работой", ""]
        for d in mapping["duplicates"][:20]:
            out.append(f"- {d['pair']} — дубль {d.get('duplicate')}, лучше: {d.get('better')}")
    if mapping.get("conflicts"):
        out += ["", "## Пары, которые не мержатся вместе", ""]
        for c in mapping["conflicts"][:20]:
            out.append(f"- {c['pair']} — пересечение {c.get('overlap')} файлов"
                       + (f", конфликт в: {', '.join(c.get('merge_files') or c.get('merge_rev_files') or [])}" if (c.get('merge_files') or c.get('merge_rev_files')) else ""))

d = time.strftime("%Y-%m-%d")
path = ROOT / "reports" / f"{d}-{SLUG.replace('__', '-')}.md"
path.parent.mkdir(exist_ok=True)
path.write_text("\n".join(out))
print(f"отчёт: {path}")
print(f"берём {len(by['take'])}, рассмотреть {len(by['consider'])}, пропускаем {len(by['skip'])}, "
      f"стоимость ${cost:.4f}, токенов {tokens}")
for r in by["take"][:10]:
    print(f"  #{r['number']:<6} {r.get('score'):5} {r['title'][:70]}")
