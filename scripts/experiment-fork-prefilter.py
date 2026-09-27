"""Эксперимент: можно ли отсеять форки без compare-запроса?

Идея: compare стоит 1 запрос REST на форк (15 613 запросов ≈ 3.1 ч при 5000/ч).
Если head-коммит форка уже есть в истории upstream master, у форка нет своей работы
(ahead_by = 0) — compare не нужен. OID-ы можно тянуть батчами через GraphQL (алиасы,
50 форков на запрос), а историю master — один раз.

Проверяем: (1) доля форков, которую так можно отсеять; (2) точность правила на выборке
(сверяем с настоящим compare).
"""
import json
import os
import random
import sys
import time
import urllib.request

sys.path.insert(0, "/srv/app")
import main  # noqa: E402

UP = "paperclipai/paperclip"
BASE = "master"
random.seed(7)

t0 = time.time()
print("1. история upstream master (OID-ы), страницы по 100")
oids, cursor, pages = set(), None, 0
while pages < 60:
    q = ('query($c:String){repository(owner:"paperclipai",name:"paperclip"){'
         'defaultBranchRef{target{... on Commit{history(first:100,after:$c){pageInfo{hasNextPage endCursor} nodes{oid}}}}}}}')
    res = main.http_json_retry("https://api.github.com/graphql", {"query": q, "variables": {"c": cursor}},
                               main.gh_headers({"Content-Type": "application/json"}), 120)
    h = res["data"]["repository"]["defaultBranchRef"]["target"]["history"]
    oids |= {n["oid"] for n in h["nodes"]}
    pages += 1
    if not h["pageInfo"]["hasNextPage"]:
        break
    cursor = h["pageInfo"]["endCursor"]
print(f"   master OID-ов: {len(oids)} за {pages} страниц, {time.time() - t0:.1f}s")

print("2. список форков (первые 1200 по свежести), потом их head OID батчами")
forks, page = [], 1
while len(forks) < 1200:
    chunk = main.gh_rest(f"/repos/{UP}/forks?per_page=100&page={page}&sort=newest")
    if not isinstance(chunk, list) or not chunk:
        break
    forks += [{"fork": f["full_name"], "branch": f.get("default_branch")} for f in chunk]
    page += 1
print(f"   форков: {len(forks)}")

BATCH = 50
heads = {}
t1 = time.time()
for i in range(0, len(forks), BATCH):
    group = [f for f in forks[i:i + BATCH] if f["branch"]]
    parts = []
    for j, f in enumerate(group):
        owner, name = f["fork"].split("/")
        parts.append(f'r{j}: repository(owner:"{owner}",name:"{name}"){{object(expression:"{f["branch"]}"){{... on Commit{{oid}}}}}}')
    query = "query{" + " ".join(parts) + "}"
    res = main.http_json_retry("https://api.github.com/graphql", {"query": query}, main.gh_headers({"Content-Type": "application/json"}), 120)
    if res.get("errors"):
        print("   GraphQL ошибка:", str(res["errors"])[:200]); break
    data = res.get("data") or {}
    for j, f in enumerate(group):
        obj = (data.get(f"r{j}") or {}).get("object") or {}
        heads[f["fork"]] = obj.get("oid")
print(f"   head OID собраны за {time.time() - t1:.1f}s ({len(heads) // BATCH + 1} запросов вместо {len(forks)})")

known = sum(1 for oid in heads.values() if oid in oids)
unknown = [k for k, v in heads.items() if v and v not in oids]
print(f"\n3. предварительный отсев без compare: head в истории master — {known} из {len(heads)} "
      f"({100 * known / max(1, len(heads)):.0f}%), требуют проверки — {len(unknown)}")

print("\n4. проверка точности правила на выборке (настоящий compare)")
sample = random.sample([k for k, v in heads.items() if v in oids], min(8, known)) + random.sample(unknown, min(8, len(unknown)))
ok = bad = 0
for k in sample:
    r = main.gh_rest(f"/repos/{UP}/compare/{BASE}...{k.split('/')[0]}:{heads[k] and 'master'}?per_page=1")
    ahead = r.get("ahead_by") if isinstance(r, dict) else None
    expect_skip = heads[k] in oids
    verdict = "ок" if (expect_skip and ahead == 0) or (not expect_skip and ahead and ahead > 0) else "РАСХОЖДЕНИЕ"
    ok += verdict == "ок"; bad += verdict != "ок"
    print(f"   {k:<40} head={'в upstream' if expect_skip else 'не в upstream'} ahead_by={ahead} → {verdict}")
print(f"\nитог: совпало {ok}, расхождений {bad}; отсев экономит ~{100 * known / max(1, len(heads)):.0f}% compare-запросов")
