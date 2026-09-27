#!/usr/bin/env python3
"""Проверка стримингового этапа форков: конфиг с лимитом, листинг, compare с Jev по ходу.

Использование: python3 scripts/test-fork-stream.py [лимит] [--config-only]
"""
import base64
import json
import pathlib
import re
import sys
import threading
import time
import urllib.request

ENV = pathlib.Path("/home/crnsfx/Work/pr-scout/.env").read_text()


def env(name):
    m = re.search(rf"(?m)^{name}=(.*)$", ENV)
    return m.group(1).strip() if m else ""


BASE = f"http://127.0.0.1:{env('SCOUT_PORT') or '8000'}"
AUTH = "Basic " + base64.b64encode(f"scout:{env('APP_PASSWORD')}".encode()).decode()
SLUG = "paperclipai__paperclip"
LIMIT = int(sys.argv[1]) if len(sys.argv) > 1 and sys.argv[1].isdigit() else 40


def api(path, method="GET", body=None, timeout=120):
    req = urllib.request.Request(BASE + path, method=method,
                                 data=json.dumps(body).encode() if body is not None else None,
                                 headers={"Authorization": AUTH, "Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        raw = r.read().decode()
    return json.loads(raw) if raw.strip() else {}


def listen(stop, seen):
    req = urllib.request.Request(BASE + "/api/events", headers={"Authorization": AUTH, "Accept": "text/event-stream"})
    with urllib.request.urlopen(req, timeout=600) as r:
        for raw in r:
            if stop.is_set():
                return
            line = raw.decode(errors="replace").strip()
            if not line.startswith("data: "):
                continue
            ev = json.loads(line[6:])
            if ev.get("type") == "fork":
                seen.append(ev)
                print(f"  [fork] {ev['fork']:<40} ahead={ev.get('ahead'):<5} балл={ev.get('score')} "
                      f"{ev.get('kind')} | {ev.get('commits')}"[:200], flush=True)
            elif ev.get("type") == "log":
                print("  [log]", ev.get("message", "")[:160], flush=True)


print(f"1. конфиг: лимит {LIMIT} форков")
print(" ", json.dumps(api(f"/api/p/{SLUG}/config", "PUT", {"forks": {"limit": LIMIT, "min_stars": 0, "max_commits": 30, "save_every": 10}}).get("forks"), ensure_ascii=False))

print("2. листинг форков (ничего не сканировалось ранее?)")
api(f"/api/p/{SLUG}/jobs/forks_meta", "POST", {})
t0 = time.time()
while True:
    time.sleep(5)
    j = api(f"/api/p/{SLUG}/summary").get("job") or {}
    if not j.get("running"):
        break
    if time.time() - t0 > 420:
        print("  таймаут листинга"); break
f = (api(f"/api/p/{SLUG}/summary").get("forks") or {})
print(f"  в списке {f.get('total')} форков за {time.time() - t0:.0f}s")

print(f"3. compare+Jev по {LIMIT} форкам, смотрим события в реальном времени")
stop, seen = threading.Event(), []
th = threading.Thread(target=listen, args=(stop, seen), daemon=True)
th.start()
time.sleep(1)
api(f"/api/p/{SLUG}/jobs/forks_compare", "POST", {})
t0 = time.time()
while True:
    time.sleep(10)
    j = api(f"/api/p/{SLUG}/summary").get("job") or {}
    s = api(f"/api/p/{SLUG}/summary").get("forks") or {}
    print(f"  [{time.time() - t0:5.0f}s] этап={j.get('running')} {j.get('done')}/{j.get('total')} | "
          f"проверено {s.get('scanned')}, впереди {s.get('ahead')}, разобрано {s.get('classified')}", flush=True)
    if not j.get("running") and j.get("done"):
        break
    if time.time() - t0 > 600:
        print("  таймаут"); break
stop.set()
f = (api(f"/api/p/{SLUG}/summary").get("forks") or {})
print(f"\nитог: проверено {f.get('scanned')}, с коммитами впереди {f.get('ahead')}, разобрано Jev {f.get('classified')}")
print(f"событий «fork» пришло в SSE: {len(seen)} (стриминг {'работает' if seen else 'НЕ работает'})")
for r in (f.get("ranked") or [])[:8]:
    print(f"  {r['fork']:<40} балл {r.get('score')} ahead={r.get('ahead')} {r.get('kind_label')}")
