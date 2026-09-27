#!/usr/bin/env python3
"""Создать проект в PR Scout и запустить полный прогон, потом следить за прогрессом.

Читает APP_PASSWORD из ~/Work/pr-scout/.env, сам берёт URL и порт оттуда же.
Печатает строки вида `[мм:сс] этап/прогресс`, в конце — сводку.
"""
import base64
import json
import pathlib
import re
import sys
import time
import urllib.error
import urllib.request

ENV = pathlib.Path("/home/crnsfx/Work/pr-scout/.env").read_text()


def env(name):
    m = re.search(rf"(?m)^{name}=(.*)$", ENV)
    return (m.group(1).strip() if m else "")


BASE = f"http://127.0.0.1:{env('SCOUT_PORT') or '8000'}"
AUTH = "Basic " + base64.b64encode(f"scout:{env('APP_PASSWORD')}".encode()).decode()
REPO = sys.argv[1] if len(sys.argv) > 1 else "paperclipai/paperclip"
JOB = sys.argv[2] if len(sys.argv) > 2 else "everything"
SLUG = REPO.replace("/", "__")
T0 = time.time()


def api(path, method="GET", body=None, timeout=120):
    req = urllib.request.Request(BASE + path, method=method,
                                 data=json.dumps(body).encode() if body is not None else None,
                                 headers={"Authorization": AUTH, "Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        raw = r.read().decode()
    return json.loads(raw) if raw.strip() else {}


def show(msg):
    print(f"[{int(time.time() - T0) // 60:02d}:{int(time.time() - T0) % 60:02d}] {msg}", flush=True)


try:
    projects = [p for p in api("/api/projects")]
except urllib.error.HTTPError as e:
    raise SystemExit(f"API не отвечает: HTTP {e.code} {e.read().decode()[:200]}")

if SLUG not in [p.get("slug") or p.get("repo", "").replace("/", "__") for p in projects]:
    created = api("/api/projects", "POST", {"url": f"https://github.com/{REPO}", "run": False})
    show(f"проект создан: {json.dumps(created, ensure_ascii=False)[:300]}")
else:
    show(f"проект {SLUG} уже есть")

# Описания без GPU: NordRouter-чат вместо Ollama. stack_prs* очищаем — в эксперименте
# не хотим наследовать список «уже взятых» PR из форка коллеги.
api(f"/api/p/{SLUG}/config", "PUT", {
    "ollama": {"enabled": True, "provider": "nordrouter", "model": env("DESCRIBER_MODEL") or "google/gemini-3.1-flash-lite",
               "min_body": 200, "max_tokens": 400, "max_diff": 24000},
    "stack_prs_url": "", "stack_prs": "",
    # Форки: 0 = обойти все (лимит REST 5000/ч, проход растягивается на несколько окон)
    "forks": {"limit": 0, "min_stars": 0, "max_commits": 30},
})
show("конфиг: описания через NordRouter, stack_prs очищены, форки — все")

cfg = api(f"/api/p/{SLUG}/summary").get("config", {})
show(f"частей системы: {len(cfg.get('areas') or {})}, финалистов: {cfg.get('finalists')}, "
     f"исключены авторы: {cfg.get('exclude_authors')}")

api(f"/api/p/{SLUG}/jobs/{JOB}", "POST", {})
show(f"прогон {JOB} запущен")

last = ""
while True:
    time.sleep(10)
    s = api(f"/api/p/{SLUG}/summary", timeout=60)
    job = s.get("job") or {}
    if job.get("running"):
        line = (f"{job['running']}: {job.get('done')}/{job.get('total')} "
                f"(этап «{job.get('phase') or '—'}»)")
    else:
        line = "job не выполняется"
    runs = s.get("runs") or []
    extra = ""
    if runs:
        r = runs[-1]
        extra = (f" | последний прогон {r.get('stage')}: {r.get('items')} шт, {r.get('seconds')}s, "
                 f"${r.get('cost_usd')}, ошибок {r.get('errors')}")
    if line + extra != last:
        show(line + extra)
        last = line + extra
    if not job.get("running") and runs:
        break

s = api(f"/api/p/{SLUG}/summary")
show(f"ГОТОВО: всего {s.get('total')} PR, классифицировано {s.get('classified')}, "
     f"финалистов {s.get('finalists')}, уже взято {len(s.get('included') or [])}")
for r in s.get("runs") or []:
    show(f"  {r.get('stage'):8} items={r.get('items'):5} sec={r.get('seconds'):6} "
         f"cost=${r.get('cost_usd')} errors={r.get('errors')}")
comp = s.get("comparison")
if comp:
    for row in comp["rows"]:
        show(f"  стоимость: {row['name']:22} ${row['cost']}" + (f" (batch ${row['batch']})" if "batch" in row else " (факт)"))

rows = api(f"/api/p/{SLUG}/prs", timeout=180)
outdir = pathlib.Path("/home/crnsfx/Work/pr-scout/data")
outdir.mkdir(parents=True, exist_ok=True)
for name, path in (("last-run-summary", "/api/p/%s/summary"), ("last-run-prs", "/api/p/%s/prs"),
                   ("last-run-issues", "/api/p/%s/issues"), ("last-run-forks", "/api/p/%s/forks"), ("last-run-rivals", "/api/p/%s/rivals")):
    try:
        (outdir / f"{name}.json").write_text(json.dumps(api(path % SLUG, timeout=300), ensure_ascii=False, indent=2))
    except Exception as e:
        show(f"не сохранил {name}: {e}")

s = api(f"/api/p/{SLUG}/summary")
show(f"итог: PR {s.get('total')} (классифицировано {s.get('classified')}), финалистов {s.get('finalists')}")
iss, fk, rv = s.get("issues") or {}, s.get("forks") or {}, s.get("rivals") or {}
show(f"issues: {iss.get('total')} всего, {iss.get('classified')} разобрано, {iss.get('without_pr')} без PR")
show(f"форки: {fk.get('total')} в списке, {fk.get('scanned')} проверено, {fk.get('ahead')} с коммитами впереди, {fk.get('classified')} разобрано Jev")
show(f"конкурирующие PR: {rv.get('groups')} групп, выбрано {rv.get('picked')}")
for r in (iss.get("ranked") or [])[:10]:
    show(f"  issue #{r['number']:<6} {r.get('score'):5} {r.get('kind_label') or r.get('kind')} | PR: {r.get('open_pr') or '—'} | {r['title'][:60]}")
for r in (fk.get("ranked") or [])[:10]:
    show(f"  форк {r['fork']:<38} {r.get('score'):5} ahead={r.get('ahead')} {str(r.get('commits') or [{}])[0].get('message', '')[:50]}")

top = sorted([r for r in (rows if isinstance(rows, list) else rows.get("rows", []))
              if r.get("verdict") in ("take", "consider")], key=lambda r: -r.get("score", 0))
show(f"взято/рассмотреть: {len(top)}; файлы: data/last-run-*.json")
for r in top[:15]:
    show(f"  #{r['number']:<6} {r.get('verdict'):8} score={r.get('score'):5} {r['title'][:70]}")
