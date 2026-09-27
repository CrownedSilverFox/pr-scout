#!/usr/bin/env python3
"""Проверка листинга форков: параллельные REST-страницы (тот же путь, что и в fetch_forks_job)."""
import sys
import time
from concurrent.futures import ThreadPoolExecutor

sys.path.insert(0, "/srv/app")
import main  # noqa: E402

owner, name = "paperclipai", "paperclip"
WORKERS = main.FORK_LIST_WORKERS
forks, page, t0, empty = {}, 1, time.time(), 0
while not empty:
    batch = list(range(page, page + WORKERS))
    with ThreadPoolExecutor(len(batch)) as ex:
        answers = list(ex.map(lambda pg: main.gh_rest(f"/repos/{owner}/{name}/forks?per_page=100&page={pg}&sort=newest"), batch))
    got = 0
    for chunk in answers:
        if isinstance(chunk, list):
            got += len(chunk)
            for f in chunk:
                forks[f["full_name"]] = (f.get("stargazers_count"), (f.get("pushed_at") or "")[:10], f.get("default_branch"))
    empty = 1 if got == 0 else 0
    print(f"страниц по {len(batch)}: всего {len(forks)} форков, {time.time() - t0:.1f}s")
    if len(forks) > 2000:
        break
    page += len(batch)

rate = len(forks) / max(0.1, time.time() - t0)
print(f"\nсобрано {len(forks)} за {time.time() - t0:.1f}s → {rate:.0f} форков/с")
print(f"прогноз на 15.5к: {15463 / rate:.0f} с")
print("без ветки:", sum(1 for v in forks.values() if not v[2]))
for k, v in list(forks.items())[:5]:
    print(f"  {k:<40} ★{v[0]:<4} {v[1]} ветка {v[2] or '—'}")
