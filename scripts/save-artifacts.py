#!/usr/bin/env python3
"""Сохранить артефакты последнего прогона и собрать markdown-отчёт."""
import base64
import json
import pathlib
import re
import subprocess
import urllib.request

ROOT = pathlib.Path("/home/crnsfx/Work/pr-scout")
ENV = (ROOT / ".env").read_text()
pw = re.search(r"(?m)^APP_PASSWORD=(.*)$", ENV).group(1).strip()
port = re.search(r"(?m)^SCOUT_PORT=(.*)$", ENV)
BASE = f"http://127.0.0.1:{port.group(1).strip() if port else '8000'}"
AUTH = "Basic " + base64.b64encode(f"scout:{pw}".encode()).decode()
SLUG = "paperclipai__paperclip"


def api(path, timeout=300):
    req = urllib.request.Request(BASE + path, headers={"Authorization": AUTH})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.loads(r.read().decode())


out = ROOT / "data"
for name, path in (("last-run-summary", "/api/p/%s/summary"), ("last-run-prs", "/api/p/%s/prs"),
                   ("last-run-issues", "/api/p/%s/issues"), ("last-run-forks", "/api/p/%s/forks"),
                   ("last-run-rivals", "/api/p/%s/rivals")):
    (out / f"{name}.json").write_text(json.dumps(api(path % SLUG), ensure_ascii=False, indent=2))
    print("сохранил", name)

s = api(f"/api/p/{SLUG}/summary")
print(f"\nPR: {s['total']} (классифицировано {s['classified']}), финалистов {s['finalists']}")
i, f, r = s["issues"], s["forks"], s["rivals"]
print(f"issues: {i['total']} всего, разобрано {i['classified']}, без PR {i['without_pr']}")
print(f"форки: {f['total']} в списке, проверено {f['scanned']}, с работой впереди {f['ahead']}, разобрано {f['classified']}")
print(f"конкурирующие PR: {r['groups']} групп, выбрано {r['picked']}")
print("\nпрогоны этого цикла:")
for run in s["runs"][-6:]:
    print(f"  {run.get('stage'):12} items={run.get('items'):6} sec={run.get('seconds'):6} ${run.get('cost_usd')} "
          f"ошибок={run.get('errors')} отсеяно={run.get('up_to_date')}")

print("\n" + subprocess.run(["python3", str(ROOT / "scripts/report.py"), SLUG], capture_output=True, text=True).stdout)
