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

d = time.strftime("%Y-%m-%d")
path = ROOT / "reports" / f"{d}-{SLUG.replace('__', '-')}.md"
path.parent.mkdir(exist_ok=True)
path.write_text("\n".join(out))
print(f"отчёт: {path}")
print(f"берём {len(by['take'])}, рассмотреть {len(by['consider'])}, пропускаем {len(by['skip'])}, "
      f"стоимость ${cost:.4f}, токенов {tokens}")
for r in by["take"][:10]:
    print(f"  #{r['number']:<6} {r.get('score'):5} {r['title'][:70]}")
