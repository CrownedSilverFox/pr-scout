#!/usr/bin/env python3
"""Пересобрать контейнер, прогнать стадию карты мёрджей и собрать отчёт."""
import base64
import json
import pathlib
import re
import subprocess
import time
import urllib.request

ROOT = pathlib.Path("/home/crnsfx/Work/pr-scout")
ENV = (ROOT / ".env").read_text()
pw = re.search(r"(?m)^APP_PASSWORD=(.*)$", ENV).group(1).strip()
port = re.search(r"(?m)^SCOUT_PORT=(.*)$", ENV)
BASE = f"http://127.0.0.1:{port.group(1).strip() if port else '8000'}"
AUTH = "Basic " + base64.b64encode(f"scout:{pw}".encode()).decode()
SLUG = "paperclipai__paperclip"


def api(path, method="GET", body=None, timeout=120):
    req = urllib.request.Request(BASE + path, method=method,
                                 data=json.dumps(body).encode() if body is not None else None,
                                 headers={"Authorization": AUTH, "Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        raw = r.read().decode()
    return json.loads(raw) if raw.strip() else {}


def log(msg):
    print(f"[{time.strftime('%H:%M:%S')}] {msg}", flush=True)


log("пересоздаю контейнер")
for cmd in (["down"], ["create"], ["start"]):
    r = subprocess.run(["sudo", "docker", "compose", *cmd], cwd=ROOT, capture_output=True, text=True)
    log(f"  {cmd[0]}: {(r.stdout or r.stderr).strip().splitlines()[-1][:70]}")
time.sleep(8)

log("конфиг карты: take+consider + топ-20 форков, смысловых пар до 150")
api(f"/api/p/{SLUG}/config", "PUT", {"map": {"verdicts": ["take", "consider"], "forks_top": 20,
                                             "semantic_pairs": 150, "hot_commits": 400, "top_n": 20}})
log("запускаю стадию map")
api(f"/api/p/{SLUG}/jobs/map", "POST", {})
t0 = time.time()
while True:
    time.sleep(20)
    j = api(f"/api/p/{SLUG}/summary").get("job") or {}
    log(f"  [{time.time() - t0:5.0f}s] {j.get('running')} {j.get('done')}/{j.get('total')}")
    if not j.get("running") and j.get("done"):
        break
    if time.time() - t0 > 5400:
        log("таймаут"); break

m = api(f"/api/p/{SLUG}/map")
log(f"кандидатов {len(m.get('candidate_list') or [])}, пар {m.get('pairs')}, мержили {m.get('pairs_merged')}, "
    f"смысловых пар {m.get('pairs_semantic')}")
log(f"конфликтных пар: {len(m.get('conflicts') or [])}, дублей по смыслу: {len(m.get('duplicates') or [])}")
for name, p in (m.get("plans") or {}).items():
    log(f"  расклад {name:10}: берём {p['count']:3} (PR {p['kinds']['pr']} + форков {p['kinds']['fork']}), "
        f"баллов {p['score_sum']}, конфликтов внутри {p['conflicts']}, файлов {p['files']}, горячих {p['hot_share']}%")
log("сохраняю артефакты и собираю отчёт")
print(subprocess.run(["python3", str(ROOT / "scripts/save-artifacts.py")], capture_output=True, text=True).stdout)
