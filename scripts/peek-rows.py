#!/usr/bin/env python3
"""Показать поля одной строки PR из API (для проверки формы отчёта)."""
import json
import pathlib
import re
import sys
import urllib.request

ENV = pathlib.Path("/home/crnsfx/Work/pr-scout/.env").read_text()
import base64

pw = re.search(r"(?m)^APP_PASSWORD=(.*)$", ENV).group(1).strip()
port = re.search(r"(?m)^SCOUT_PORT=(.*)$", ENV)
BASE = f"http://127.0.0.1:{port.group(1).strip() if port else '8000'}"
AUTH = "Basic " + base64.b64encode(f"scout:{pw}".encode()).decode()
slug = sys.argv[1] if len(sys.argv) > 1 else "paperclipai__paperclip"
req = urllib.request.Request(f"{BASE}/api/p/{slug}/prs", headers={"Authorization": AUTH})
rows = json.loads(urllib.request.urlopen(req, timeout=120).read().decode())
if isinstance(rows, dict):
    rows = rows.get("rows") or []
print("строк:", len(rows))
verdicts = {}
for r in rows:
    verdicts[r.get("verdict")] = verdicts.get(r.get("verdict"), 0) + 1
print("вердикты:", verdicts)
sample = next((r for r in rows if r.get("verdict") in ("take", "consider")), rows[0])
print(json.dumps(sample, ensure_ascii=False, indent=2)[:2500])
