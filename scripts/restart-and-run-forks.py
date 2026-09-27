#!/usr/bin/env python3
"""Перезапустить контейнер на свежем образе и прогнать стадию форков, следя за прогрессом."""
import base64
import json
import pathlib
import re
import subprocess
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
STAGE = "forks"


def api(path, method="GET", body=None, timeout=60):
    req = urllib.request.Request(BASE + path, method=method,
                                 data=json.dumps(body).encode() if body is not None else None,
                                 headers={"Authorization": AUTH, "Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        raw = r.read().decode()
    return json.loads(raw) if raw.strip() else {}


def log(msg):
    print(f"[{time.strftime('%H:%M:%S')}] {msg}", flush=True)


log("пересоздаю контейнер на свежем образе")
for cmd in (["down"], ["create"], ["start"]):
    r = subprocess.run(["sudo", "docker", "compose", *cmd], cwd=ROOT, capture_output=True, text=True)
    log(f"  {cmd[0]}: {(r.stdout or r.stderr).strip().splitlines()[-1][:70]}")
time.sleep(8)
api(f"/api/p/{SLUG}/config", "PUT", {"forks": {"limit": 0, "min_stars": 0, "max_commits": 30, "prefilter": True, "save_every": 25}})
log(f"запускаю стадию {STAGE}")
api(f"/api/p/{SLUG}/jobs/{STAGE}", "POST", {})

t0 = time.time()
while True:
    time.sleep(30)
    s = api(f"/api/p/{SLUG}/summary")
    j, f = s.get("job") or {}, s.get("forks") or {}
    log(f"  [{time.time() - t0:6.0f}s] {j.get('running')} {j.get('done')}/{j.get('total')} | "
        f"список {f.get('total')}, проверено {f.get('scanned')}, впереди {f.get('ahead')}, разобрано {f.get('classified')}")
    if not j.get("running") and j.get("done"):
        break
    if time.time() - t0 > 7200:
        log("таймаут наблюдения"); break

s = api(f"/api/p/{SLUG}/summary")
f = s.get("forks") or {}
log(f"ИТОГ: в списке {f.get('total')}, проверено {f.get('scanned')}, с работой впереди {f.get('ahead')}, разобрано Jev {f.get('classified')}")
for r in (f.get("ranked") or [])[:15]:
    log(f"  {r['fork']:<40} балл {r.get('score')} ahead={r.get('ahead')} {r.get('kind_label')}")
for r in (s.get("runs") or [])[-3:]:
    log(f"  прогон {r.get('stage')}: items={r.get('items')} sec={r.get('seconds')} ${r.get('cost_usd')} "
        f"отсеяно={r.get('up_to_date')} удалённых={r.get('gone')}")
