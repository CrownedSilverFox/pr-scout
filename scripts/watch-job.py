#!/usr/bin/env python3
"""Открыть SSE PR Scout, дёрнуть задачу и напечатать события (включая ошибки).

Использование: python3 scripts/watch-job.py <job> [slug] [секунд]
  job: fetch | describe | stage1 | stage2 | full
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
    return (m.group(1).strip() if m else "")


BASE = f"http://127.0.0.1:{env('SCOUT_PORT') or '8000'}"
AUTH = "Basic " + base64.b64encode(f"scout:{env('APP_PASSWORD')}".encode()).decode()
JOB = sys.argv[1] if len(sys.argv) > 1 else "fetch"
SLUG = sys.argv[2] if len(sys.argv) > 2 else "paperclipai__paperclip"
LIMIT = int(sys.argv[3]) if len(sys.argv) > 3 else 600
stop = threading.Event()


def sse():
    req = urllib.request.Request(BASE + "/api/events", headers={"Authorization": AUTH, "Accept": "text/event-stream"})
    with urllib.request.urlopen(req, timeout=LIMIT + 30) as r:
        for raw in r:
            if stop.is_set():
                break
            line = raw.decode(errors="replace").strip()
            if not line.startswith("data: "):
                continue
            try:
                ev = json.loads(line[6:])
            except json.JSONDecodeError:
                continue
            t = time.strftime("%H:%M:%S")
            if ev.get("type") == "progress":
                print(f"{t} прогресс {ev.get('phase')} {ev.get('done')}/{ev.get('total')} "
                      f"#{ev.get('number')} {ev.get('error') or ev.get('title') or ''}"[:200], flush=True)
            else:
                print(f"{t} {json.dumps(ev, ensure_ascii=False)[:400]}", flush=True)
            if ev.get("type") == "done" and ev.get("job") == JOB:
                stop.set()
                return


th = threading.Thread(target=sse, daemon=True)
th.start()
time.sleep(1.5)
req = urllib.request.Request(f"{BASE}/api/p/{SLUG}/jobs/{JOB}", method="POST",
                             data=b"{}", headers={"Authorization": AUTH, "Content-Type": "application/json"})
try:
    with urllib.request.urlopen(req, timeout=60) as r:
        print("задача запущена:", r.read().decode()[:200], flush=True)
except Exception as e:
    print("не удалось запустить:", e, flush=True)
th.join(LIMIT)
print("наблюдение завершено")
