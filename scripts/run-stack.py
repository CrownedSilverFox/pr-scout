#!/usr/bin/env python3
"""Пересобрать контейнер на свежем образе, прогнать стадию стека и собрать отчёт."""
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


log("пересоздаю контейнер на свежем образе")
for cmd in (["down"], ["create"], ["start"]):
    r = subprocess.run(["sudo", "docker", "compose", *cmd], cwd=ROOT, capture_output=True, text=True)
    log(f"  {cmd[0]}: {(r.stdout or r.stderr).strip().splitlines()[-1][:70]}")
time.sleep(8)

f = (api(f"/api/p/{SLUG}/summary").get("forks") or {})
log(f"кластеры форков после перезагрузки: уникальных кандидатов {len(f.get('ranked') or [])} в топ-20, "
    f"клонов {f.get('duplicates')}, групп {f.get('clusters')}")

log("настраиваю стадию стека: берём take+consider, окно горячих файлов 400 коммитов")
api(f"/api/p/{SLUG}/config", "PUT", {"stack": {"verdicts": ["take", "consider"], "limit": 0, "hot_commits": 400}})
log("запускаю стадию stack")
api(f"/api/p/{SLUG}/jobs/stack", "POST", {})
t0 = time.time()
while True:
    time.sleep(20)
    j = api(f"/api/p/{SLUG}/summary").get("job") or {}
    log(f"  [{time.time() - t0:5.0f}s] {j.get('running')} {j.get('done')}/{j.get('total')}")
    if not j.get("running") and j.get("done"):
        break
    if time.time() - t0 > 3600:
        log("таймаут"); break

s = api(f"/api/p/{SLUG}/summary")
st = s.get("stack") or {}
hot = st.get("hot") or {}
log(f"СТЕК: рассмотрено {st.get('considered')}, влилось {st.get('merged')}, конфликтов {st.get('conflicted')} "
    f"({st.get('merge_cost')}%), патч {st.get('patch', {}).get('files')} файлов {st.get('patch', {}).get('shortstat')}")
log(f"ПОВЕРХНОСТЬ БУДУЩИХ КОНФЛИКТОВ: {hot.get('churn_share')}% правок upstream за {hot.get('commits_scanned')} коммитов "
    f"в наших файлах ({hot.get('hot_in_stack')} из {hot.get('files_in_stack')})")
for h in (hot.get("hot_top") or [])[:10]:
    log(f"  горячий файл {h['file']} — {h['edits']} правок")
log("сохраняю артефакты и собираю отчёт")
print(subprocess.run(["python3", str(ROOT / "scripts/save-artifacts.py")], capture_output=True, text=True).stdout)
