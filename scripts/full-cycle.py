#!/usr/bin/env python3
"""Полный цикл PR Scout по репозиторию: сбор → описания → Jev → мерж → issues → форки →
соперники → стек → карта мёрджей → отчёт.

    python3 scripts/full-cycle.py <owner/repo> [job]

Проект создаётся из presets/<owner__repo>.json (профиль и части системы — оттуда).
Артефакты пишутся в data/runs/<slug>/, поэтому прогоны по разным репозиториям не затирают друг друга.
"""
import base64
import json
import pathlib
import re
import subprocess
import sys
import time
import urllib.error
import urllib.request

ROOT = pathlib.Path("/home/crnsfx/Work/pr-scout")
ENV = (ROOT / ".env").read_text()


def env(name, default=""):
    m = re.search(rf"(?m)^{name}=(\S+)", ENV)
    return m.group(1).strip() if m else default


BASE = f"http://127.0.0.1:{env('SCOUT_PORT', '8000')}"
AUTH = "Basic " + base64.b64encode(f"scout:{env('APP_PASSWORD')}".encode()).decode()
REPO = sys.argv[1] if len(sys.argv) > 1 else "siteboon/claudecodeui"
JOB = sys.argv[2] if len(sys.argv) > 2 else "everything"
SLUG = REPO.replace("/", "__")
OUTDIR = ROOT / "data" / "runs" / SLUG
T0 = time.time()


def api(path, method="GET", body=None, timeout=120):
    req = urllib.request.Request(BASE + path, method=method,
                                 data=json.dumps(body).encode() if body is not None else None,
                                 headers={"Authorization": AUTH, "Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        raw = r.read().decode()
    return json.loads(raw) if raw.strip() else {}


def log(msg):
    print(f"[{int(time.time() - T0) // 60:02d}:{int(time.time() - T0) % 60:02d}] {msg}", flush=True)


def wait_job(label, timeout=5400):
    """Ждём завершения задачи по /api/status, печатаем этапы."""
    last, t0 = "", time.time()
    while True:
        time.sleep(10)
        st = api("/api/status", timeout=60)["job"]
        line = (f"{label}: {st.get('running')} {st.get('done')}/{st.get('total')} "
                f"(этап «{st.get('phase') or '—'}»)")
        if line != last:
            log(line)
            last = line
        if not st.get("running"):
            if st.get("error"):
                log(f"  ЗАДАЧА УПАЛА: {st['error']}")
            return st
        if time.time() - t0 > timeout:
            log(f"  таймаут {label}")
            return st


def save_artifacts():
    OUTDIR.mkdir(parents=True, exist_ok=True)
    paths = {"last-run-summary": "summary", "last-run-prs": "prs", "last-run-issues": "issues",
             "last-run-forks": "forks", "last-run-rivals": "rivals", "last-run-stack": "stack",
             "last-run-map": "map"}
    for name, ep in paths.items():
        try:
            data = api(f"/api/p/{SLUG}/{ep}", timeout=600)
        except Exception as e:  # noqa: BLE001
            log(f"  не сохранил {name}: {e}")
            continue
        (OUTDIR / f"{name}.json").write_text(json.dumps(data, ensure_ascii=False, indent=2))
    log(f"артефакты: {OUTDIR}")


projects = api("/api/projects")
if SLUG not in [p.get("slug") for p in projects]:
    log(f"создаю проект {REPO} из пресета")
    api("/api/projects", "POST", {"url": f"https://github.com/{REPO}", "run": False})
else:
    log(f"проект {SLUG} уже есть")

api(f"/api/p/{SLUG}/config", "PUT", {
    "ollama": {"enabled": True, "provider": "nordrouter",
               "model": env("DESCRIBER_MODEL", "google/gemini-3.1-flash-lite"),
               "min_body": 200, "max_tokens": 400, "max_diff": 24000},
    "stack_prs_url": "", "stack_prs": "",
    "forks": {"limit": 0, "min_stars": 0, "max_commits": 30},
    "triage": {"verdicts": ["take", "consider"], "limit": 0, "hot_commits": 400},
})
cfg = api(f"/api/p/{SLUG}/summary").get("config", {})
log(f"конфиг: частей системы {len(cfg.get('areas') or {})}, финалистов {cfg.get('finalists')}, "
    f"профиль {len(cfg.get('profile') or '')} симв.")

log(f"запускаю задачи «{JOB}»")
api(f"/api/p/{SLUG}/jobs/{JOB}", "POST", {})
wait_job(JOB)
save_artifacts()
s = api(f"/api/p/{SLUG}/summary")
log(f"PR {s.get('total')} (классифицировано {s.get('classified')}), финалистов {s.get('finalists')}")

for stage in ("stack", "map"):
    log(f"запускаю стадию {stage}")
    api(f"/api/p/{SLUG}/jobs/{stage}", "POST", {})
    wait_job(stage)
    save_artifacts()

log("собираю отчёт")
r = subprocess.run(["python3", str(ROOT / "scripts/report.py"), SLUG, "--dir", str(OUTDIR)],
                   capture_output=True, text=True)
print(r.stdout or r.stderr)
s = api(f"/api/p/{SLUG}/summary")
log(f"ИТОГ: PR {s.get('total')}, финалистов {s.get('finalists')}, всего прогонов {len(s.get('runs') or [])}")
