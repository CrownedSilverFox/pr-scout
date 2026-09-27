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
})
show("конфиг: описания через NordRouter, stack_prs/stack_prs_url очищены")

cfg = api(f"/api/p/{SLUG}/summary").get("config", {})
show(f"частей системы: {len(cfg.get('areas') or {})}, финалистов: {cfg.get('finalists')}, "
     f"исключены авторы: {cfg.get('exclude_authors')}")

api(f"/api/p/{SLUG}/jobs/full", "POST", {})
show("полный прогон запущен: fetch -> describe -> stage1 -> stage2")

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
pathlib.Path("/home/crnsfx/Work/pr-scout/data/last-run-summary.json").write_text(
    json.dumps(s, ensure_ascii=False, indent=2))
pathlib.Path("/home/crnsfx/Work/pr-scout/data/last-run-prs.json").write_text(
    json.dumps(rows, ensure_ascii=False, indent=2))
top = sorted([r for r in (rows if isinstance(rows, list) else rows.get("rows", []))
              if r.get("verdict") in ("take", "consider")], key=lambda r: -r.get("score", 0))
show(f"взято/рассмотреть: {len(top)}; файлы: data/last-run-summary.json, data/last-run-prs.json")
for r in top[:15]:
    show(f"  #{r['number']:<6} {r.get('verdict'):8} score={r.get('score'):5} {r['title'][:70]}")
