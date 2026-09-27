#!/usr/bin/env python3
"""Прогон внутри образа: импорт модулей и живые проверки новых стадий (issues/forks/rivals).

Запуск в одноразовом контейнере:
  sudo docker compose run --rm --no-deps --entrypoint python scout /srv/smoke.py
"""
import json
import os
import sys

sys.path.insert(0, "/srv/app")
import main  # noqa: E402
import triage  # noqa: E402

print("импорт ок; задач:", len([k for k in ("full", "everything", "issues", "forks", "rivals") if k]), "| data:", main.DATA)
print("workers: stage1", main.STAGE1_WORKERS, "stage2", main.STAGE2_WORKERS, "merge", main.MERGE_WORKERS, "fork-rest", main.FORK_REST_WORKERS)
assert main.JEV_KEY, "нет ключа Jev"
assert main.GH_TOKEN, "нет GITHUB_TOKEN"

cfg = {"repo": "paperclipai/paperclip", "name": "Paperclip",
       "profile": "Self-hosted Paperclip in Docker Compose, ~10 Claude agents on a subscription, Codex, private Gitea, Dokploy MCP."}

print("\n--- 1. fork compare живьём (REST)")
res = main.gh_rest("/repos/paperclipai/paperclip/compare/master...penclipai:master")
print("статус", res.get("status"), "ahead", res.get("ahead_by"), "behind", res.get("behind_by"),
      "commits", len(res.get("commits") or []), "files", len(res.get("files") or []))
assert "ahead_by" in res, res

print("\n--- 2. Jev по дельте форка")
fork = {"fork": "penclipai/paperclip-cn", "behind": res.get("behind_by"), "lines": 300,
        "commits": [{"sha": c["sha"][:8], "date": (c.get("commit", {}).get("author") or {}).get("date", "")[:10],
                     "message": (c["commit"]["message"] or "").split("\n")[0][:200]} for c in (res.get("commits") or [])[-30:]]}
ans = main.jev(fork, triage.fork_questions(cfg))
if "answers" in ans:
    sc = triage.score_fork(fork, ans["answers"])
    print("балл форка:", sc["score"], "| вид", sc["kind"], "ценность", sc["value"], "дубль", sc["duplicate"], "секреты", sc["secrets"])
else:
    print("ошибка:", ans)

print("\n--- 3. Jev по issue")
issue_state = {"repo": cfg["repo"], "number": 4242, "title": "Heartbeat runs hang when the adapter exits without a result",
               "labels": ["bug"], "comments": 7,
               "description": "With claude_local, when the agent process dies mid-run, the run stays in progress forever, no retry and no wake. Reproduced 5 times today on v0.x."}
ans = main.jev(issue_state, triage.issue_questions(cfg))
if "answers" in ans:
    sc = triage.score_issue({"number": 4242, "title": issue_state["title"]}, ans["answers"], has_pr=False)
    print("балл issue:", sc["score"], "| вид", sc["kind"], "серьёзность", sc["severity"], "частота", sc["common_case"], "есть PR:", sc["has_pr"])
else:
    print("ошибка:", ans)

print("\n--- 4. Jev: какой из конкурентов лучше")
cands = [{"number": 1, "title": "fix(heartbeat): mark run failed when adapter exits", "author": "a", "additions": 40, "deletions": 2, "files": 3,
          "score": 80, "updated": "2026-09-01T00:00:00Z"},
         {"number": 2, "title": "fix: also handle the same case in the codex adapter", "author": "b", "additions": 300, "deletions": 90, "files": 12,
          "score": 62, "updated": "2026-08-01T00:00:00Z"}]
q, body = triage.rival_question(cfg, {"number": 4242, "title": issue_state["title"], "body": issue_state["description"]}, cands)
ans = main.jev({"repo": cfg["repo"], "issue": {"number": 4242}, "candidates": [c["title"] for c in cands]}, q)
if "answers" in ans:
    print("решение:", json.dumps(triage.apply_rival(ans["answers"], {"number": 4242}), ensure_ascii=False))
else:
    print("ошибка:", ans)
print("\nSMOKE OK")
