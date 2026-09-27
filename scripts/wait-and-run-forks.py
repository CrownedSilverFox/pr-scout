#!/usr/bin/env python3
"""Дождаться, пока issues/rivals отработают, пересобрать контейнер и прогнать форки с отсевом.

Зачем: прогон №3 стартовал на образе БЕЗ отсева форков (compare на каждый из 15.6к, часы).
PR/issues/rivals уже посчитаны и лежат в volume scout_data, поэтому после перезапуска
контейнера запускаем только стадию форков — она теперь минуты.

Стадии "issues-list" уже в списке прогона; ждём, пока job.running не станет "forks",
после чего перезапускаем контейнер (это убивает старый форк-прогон) и запускаем forks заново.
"""
import base64
import json
import pathlib
import re
import subprocess
import sys
import time
import urllib.request

ROOT = pathlib.Path("/home/crnsfx/Work/pr-scout")
ENV = (ROOT / ".env").read_text()


def env(name):
    m = re.search(rf"(?m)^{name}=(.*)$", ENV)
    return m.group(1).strip() if m else ""


BASE = f"http://127.0.0.1:{env('SCOUT_PORT') or '8000'}"
AUTH = "Basic " + base64.b64encode(f"scout:{env('APP_PASSWORD')}".encode()).decode()
SLUG = "paperclipai__paperclip"


def api(path, method="GET", body=None, timeout=60):
    req = urllib.request.Request(BASE + path, method=method,
                                 data=json.dumps(body).encode() if body is not None else None,
                                 headers={"Authorization": AUTH, "Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        raw = r.read().decode()
    return json.loads(raw) if raw.strip() else {}


def log(msg):
    print(f"[{time.strftime('%H:%M:%S')}] {msg}", flush=True)


log("ждём, пока конвейер дойдёт до стадии форков")
while True:
    time.sleep(20)
    j = api(f"/api/p/{SLUG}/summary").get("job") or {}
    run = j.get("running")
    if run == "forks" or run is None:
        log(f"стадия: {run} — можно перезапускать контейнер на образе с отсевом")
        break
    log(f"  сейчас: {run} {j.get('done')}/{j.get('total')}")

log("пересоздаю контейнер")
for cmd in (["down"], ["create"], ["start"]):
    r = subprocess.run(["sudo", "docker", "compose", *cmd], cwd=ROOT, capture_output=True, text=True)
    log(f"  docker compose {cmd[0]}: rc={r.returncode} {(r.stdout or r.stderr).strip().splitlines()[-1][:80] if (r.stdout or r.stderr).strip() else ''}")
time.sleep(8)

log("конфиг: отсев включён, лимита нет")
api(f"/api/p/{SLUG}/config", "PUT", {"forks": {"limit": 0, "min_stars": 0, "max_commits": 30, "prefilter": True, "save_every": 25}})
log("запускаю стадию форков")
api(f"/api/p/{SLUG}/jobs/forks", "POST", {})

t0 = time.time()
while True:
    time.sleep(30)
    s = api(f"/api/p/{SLUG}/summary")
    j, f = s.get("job") or {}, s.get("forks") or {}
    log(f"  [{time.time() - t0:6.0f}s] этап={j.get('running')} {j.get('done')}/{j.get('total')} | "
        f"в списке {f.get('total')}, проверено {f.get('scanned')}, впереди {f.get('ahead')}, разобрано {f.get('classified')}")
    if not j.get("running") and j.get("done"):
        break
    if time.time() - t0 > 7200:
        log("таймаут наблюдения"); break

s = api(f"/api/p/{SLUG}/summary")
f = s.get("forks") or {}
log(f"ГОТОВО: в списке {f.get('total')}, проверено {f.get('scanned')}, с коммитами впереди {f.get('ahead')}, "
    f"разобрано Jev {f.get('classified')}")
for r in (f.get("ranked") or [])[:15]:
    log(f"  {r['fork']:<40} балл {r.get('score')} ahead={r.get('ahead')} {r.get('kind_label')}")
for r in (s.get("runs") or [])[-4:]:
    log(f"  прогон {r.get('stage'):12} items={r.get('items')} sec={r.get('seconds')} ${r.get('cost_usd')} {r.get('up_to_date', '')}")
