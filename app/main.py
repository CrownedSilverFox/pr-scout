"""PR Scout: classify open pull requests of any GitHub repository with Jev and show the results."""
import asyncio
import base64
import concurrent.futures as cf
import datetime as dt
import json
import os
import re
import secrets
import shutil
import subprocess
import threading
import time
import urllib.error
import urllib.request
from pathlib import Path
from queue import Queue

from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import FileResponse, Response, StreamingResponse
from fastapi.staticfiles import StaticFiles

from scoring import (KIND_LABELS, NEGATIVE, QUESTION_LABELS, STAGE2_QUESTIONS, auto_areas, cost_comparison,
                     mark_duplicates, score_pr, stage1_questions, stage1_state, verdict)
from triage import (FORK_KIND_LABELS, ISSUE_KIND_LABELS, RIVAL_LABELS, apply_rival, fork_questions,
                    issue_questions, rival_question, score_fork, score_issue)

APP_DIR = Path(__file__).parent
DATA = Path(os.environ.get("DATA_DIR", "/data"))
PRESETS = APP_DIR.parent / "presets"
# Jev endpoint. Two interchangeable providers:
#   TypeSafe   https://api.typesafe.ai/v1/systemone   (types: noul / choice / score)
#   NordRouter https://nordrouter.com/v1/evaluate     (types: boolean / choice / score)
# NordRouter rejects `noul` with 400 upstream_error, so jev() translates it both ways.
JEV_URL = os.environ.get("JEV_API_URL", "https://api.typesafe.ai/v1/systemone")
JEV_MODEL = os.environ.get("JEV_MODEL", "jev-latest")
JEV_KEY = os.environ.get("TYPESAFE_API_KEY") or os.environ.get("NORDROUTER_API_KEY", "")
GH_TOKEN = os.environ.get("GITHUB_TOKEN", "")
PASSWORD = os.environ.get("APP_PASSWORD", "")
OLLAMA_URL = os.environ.get("OLLAMA_URL", "http://host.docker.internal:11434").rstrip("/")
# USD per 1M input tokens: TypeSafe 0.042, NordRouter 0.05 (measured from X-Charged-USD).
PRICE_PER_MTOK = float(os.environ.get("JEV_PRICE_PER_MTOK", "0.042"))
# NordRouter allows 15 rps; stage 1 is ~1.1 s per PR, so 16 workers sit right at the limit.
STAGE1_WORKERS = int(os.environ.get("JEV_STAGE1_WORKERS", "14"))
STAGE2_WORKERS = int(os.environ.get("JEV_STAGE2_WORKERS", "10"))
# Descriptions of PRs whose author wrote nothing: a local Ollama model, or NordRouter's
# OpenAI-compatible chat endpoint (no GPU needed). gemini-3.1-flash-lite ~8 s per diff;
# deepseek-v4-flash is 10x cheaper but took 85 s on the same input, so it is too slow here.
NORDROUTER_URL = os.environ.get("NORDROUTER_URL", "https://nordrouter.com").rstrip("/")
DESCRIBER_MODEL = os.environ.get("DESCRIBER_MODEL", "google/gemini-3.1-flash-lite")
DESCRIBER_WORKERS = int(os.environ.get("DESCRIBER_WORKERS", "6"))
# Stage 2 git work (fetch branch, test merge, diff) runs in parallel worktrees: upstream did it
# one PR at a time, which cost 32 of 48 minutes on a 3000-PR run while Jev answered in 21 s.
MERGE_WORKERS = int(os.environ.get("JEV_MERGE_WORKERS", "6"))
# Fork mining walks every fork with the compare API and asks Jev about the deltas.
FORK_REST_WORKERS = int(os.environ.get("FORK_REST_WORKERS", "10"))

app = FastAPI(title="PR Scout")
lock = threading.RLock()
projects: dict[str, dict] = {}  # slug -> {"config", "prs", "stage1", "stage2", "runs", "rows", "finalists", "included"}
job = {"running": None, "project": None, "done": 0, "total": 0, "started": None}
listeners: list[asyncio.Queue] = []
loop: asyncio.AbstractEventLoop | None = None


# ---------- storage ----------
def slug_of(repo):
    return repo.replace("/", "__")


def pdir(slug):
    return DATA / "projects" / slug


def read_json(path, default):
    return json.loads(path.read_text()) if path.exists() else default


def write_json(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(".tmp")
    tmp.write_text(json.dumps(value, ensure_ascii=False))
    tmp.replace(path)


def save(slug, name):
    write_json(pdir(slug) / f"{name}.json", projects[slug][name])


def preset_for(repo):
    return read_json(PRESETS / f"{slug_of(repo)}.json", {})


def migrate_legacy():
    """v0 kept a single project's files at the data root. Move them into projects/ using its preset."""
    root_files = [DATA / f"{n}.json" for n in ("prs", "stage1", "stage2", "runs")]
    if not (DATA / "prs.json").exists() or (DATA / "projects").exists():
        return
    repo = os.environ.get("LEGACY_REPO", "paperclipai/paperclip")
    target = pdir(slug_of(repo))
    target.mkdir(parents=True, exist_ok=True)
    for f in root_files:
        if f.exists():
            shutil.move(str(f), str(target / f.name))
    if (DATA / "repo").exists():
        shutil.move(str(DATA / "repo"), str(target / "repo"))
    cfg = {"repo": repo, "name": repo.split("/")[1], "profile": "", "community_only": True, "exclude_authors": [], "stack_prs": [],
           "stack_prs_url": "", "finalists": 120, "ollama": {"enabled": True, "model": "qwen3.5:9b", "min_body": 200}}
    cfg.update(preset_for(repo))
    write_json(target / "config.json", cfg)


def load_project(slug):
    d = pdir(slug)
    p = {"config": read_json(d / "config.json", None)}
    if not p["config"]:
        return
    for name, default in (("prs", []), ("stage1", {}), ("stage2", {}), ("runs", []), ("issues", {}), ("forks", {}), ("rivals", {})):
        p[name] = read_json(d / f"{name}.json", default)
    p["prs"] = {x["number"]: x for x in p["prs"]} if isinstance(p["prs"], list) else {int(k): v for k, v in p["prs"].items()}
    projects[slug] = p
    p["included"] = load_included(p["config"])
    recompute(slug)


def load_included(cfg):
    nums = set(cfg.get("stack_prs") or [])
    if cfg.get("stack_prs_url"):
        try:
            with urllib.request.urlopen(cfg["stack_prs_url"], timeout=15) as r:
                text = r.read().decode()
            nums |= {int(m) for m in re.findall(r"^\s*(\d+)", re.sub(r"#.*", "", text), re.M)}
        except Exception:
            pass
    return nums


def recompute(slug):
    with lock:
        P = projects[slug]
        cfg, now, rows = P["config"], dt.datetime.now(dt.timezone.utc), {}
        for n, pr in P["prs"].items():
            res = P["stage1"].get(str(n))
            base = {k: pr.get(k) for k in ("number", "title", "author", "updated", "additions", "deletions", "issues")}
            base.update(files=len(pr["files"]), included=n in P["included"], classified=bool(res), ai_description=bool(pr.get("ai_description")))
            if res:
                base.update(score_pr(pr, res["answers"], now))
            rows[n] = base
        classified = [r for r in rows.values() if r["classified"]]
        mark_duplicates(classified, P["included"])
        ranked = sorted(classified, key=lambda r: -r["score"])
        for i, r in enumerate(ranked, 1):
            r["rank"] = i
        finalists = [r["number"] for r in ranked if r["track"] in ("fix", "feature") and not r["duplicate_of"]
                     and not r["included"] and r["relevance"] >= 1.5][: cfg.get("finalists", 120)]
        for n in finalists:
            rows[n]["finalist"] = True
            s2 = P["stage2"].get(str(n))
            if s2:
                rows[n].update(verdict(rows[n], s2))
        P["rows"], P["finalists"] = rows, finalists
        P["issue_rows"] = issue_rows(P)
        P["fork_rows"] = fork_rows(P)


def issue_rows(P):
    """Rows for the open issues: who is already fixing them, and what Jev thinks of them."""
    covered, mentioned = {}, {}
    for n, pr in P["prs"].items():
        for i in pr.get("issues") or []:
            covered.setdefault(i, []).append(n)
        for i in {int(x) for x in re.findall(r"#(\d+)", pr.get("body") or "")}:
            mentioned.setdefault(i, []).append(n)
    rows = {}
    for k, v in (P.get("issues") or {}).items():
        meta, res = v.get("meta"), v.get("answers")
        if not meta:
            continue
        row = {kk: meta.get(kk) for kk in ("number", "title", "author", "created", "updated", "comments", "labels")}
        row.update(classified=bool(res), open_pr=sorted(covered.get(meta["number"]) or []), kind_label=None)
        if res:
            row.update(score_issue(meta, res, has_pr=bool(covered.get(meta["number"])), mentioned_by=mentioned.get(meta["number"]) or ()))
            row["kind_label"] = ISSUE_KIND_LABELS.get(row.get("kind"), row.get("kind"))
        rows[meta["number"]] = row
    ranked = sorted([r for r in rows.values() if r["classified"]], key=lambda r: -r["score"])
    for i, r in enumerate(ranked, 1):
        r["rank"] = i
    return rows


def fork_rows(P):
    """Rows for the forks that carry commits upstream does not have."""
    rows = {}
    for k, v in (P.get("forks") or {}).items():
        if not v.get("scanned"):
            continue
        row = {kk: v.get(kk) for kk in ("fork", "owner", "branch", "pushed", "stars", "ahead", "behind", "lines", "status", "truncated", "commits", "files")}
        row["classified"] = bool(v.get("answers"))
        if v.get("answers"):
            row.update(score_fork(v, v["answers"]))
            row["kind_label"] = FORK_KIND_LABELS.get(row.get("kind"), row.get("kind"))
        rows[k] = row
    ranked = sorted([r for r in rows.values() if r["classified"]], key=lambda r: -r["score"])
    for i, r in enumerate(ranked, 1):
        r["rank"] = i
    return rows


def get_project(slug):
    if slug not in projects:
        raise HTTPException(404, "Проект не найден")
    return projects[slug]


@app.on_event("startup")
async def startup():
    global loop
    loop = asyncio.get_running_loop()
    migrate_legacy()
    for d in sorted((DATA / "projects").glob("*")):
        load_project(d.name)


# ---------- auth ----------
@app.middleware("http")
async def basic_auth(request: Request, call_next):
    if PASSWORD and request.url.path != "/healthz":
        header, ok = request.headers.get("authorization", ""), False
        if header.startswith("Basic "):
            try:
                ok = secrets.compare_digest(base64.b64decode(header[6:]).decode().split(":", 1)[1], PASSWORD)
            except Exception:
                ok = False
        if not ok:
            return Response(status_code=401, headers={"WWW-Authenticate": 'Basic realm="PR Scout"'})
    return await call_next(request)


# ---------- events / jobs ----------
def emit(event):
    if loop is not None:
        for q in list(listeners):
            loop.call_soon_threadsafe(q.put_nowait, event)


def progress(done, total, number=None, **extra):
    with lock:
        job["done"], job["total"] = done, total
    emit({"type": "progress", "project": job["project"], "done": done, "total": total, "number": number, **extra})


def run_job(name, slug, steps):
    with lock:
        if job["running"]:
            raise HTTPException(409, f"Уже идёт задача: {job['running']}")
        job.update(running=name, project=slug, done=0, total=0, started=time.time())
    emit({"type": "start", "job": name, "project": slug})

    def wrapper():
        try:
            for step in steps:
                with lock:
                    job["running"] = step.__name__.replace("_job", "")
                emit({"type": "step", "job": job["running"], "project": slug})
                stats = step(slug)
                if stats:
                    with lock:
                        projects[slug]["runs"].append(stats)
                        save(slug, "runs")
            emit({"type": "done", "job": name, "project": slug, "stats": stats})
        except Exception as e:
            emit({"type": "error", "job": name, "project": slug, "message": str(e)[:500]})
        finally:
            with lock:
                job.update(running=None, project=None)
    threading.Thread(target=wrapper, daemon=True).start()


def now_iso():
    return dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds")


# ---------- external calls ----------
def http_json(url, data=None, headers=None, timeout=120):
    req = urllib.request.Request(url, data=json.dumps(data).encode() if data is not None else None, headers=headers or {})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.load(r)


def http_json_retry(url, data=None, headers=None, timeout=120, tries=5):
    """Same as http_json but survives transient resolver/network blips.

    Docker's embedded DNS occasionally answers `No address associated with hostname`
    for a second or two (a systemd-resolved stub upstream); a paging query losing a
    page used to abort the whole fetch job.
    """
    for attempt in range(tries):
        try:
            return http_json(url, data, headers, timeout)
        except urllib.error.HTTPError:
            raise
        except Exception:
            if attempt == tries - 1:
                raise
            time.sleep(1.5 * (attempt + 1))


def jev(state_value, questions):
    """Ask Jev typed questions about one PR.

    TypeSafe names a yes/no question `noul` and answers with `noul`; NordRouter's
    /v1/evaluate only knows `boolean` and answers with `probability`. Translate in
    both directions so scoring.py keeps working against either provider.
    """
    payload = {"model": JEV_MODEL, "state": state_value, "questions": to_provider(questions)}
    for attempt in range(6):
        try:
            res = http_json(JEV_URL, payload, {"Authorization": f"Bearer {JEV_KEY}", "Content-Type": "application/json"}, 180)
            if res.get("answers"):
                res["answers"] = from_provider(res["answers"])
            return res
        except urllib.error.HTTPError as e:
            if e.code in (429, 500, 502, 503, 529):
                time.sleep(min(30, 2 ** attempt))
                continue
            return {"error": f"HTTP {e.code}"}
        except Exception:
            time.sleep(min(30, 2 ** attempt))
    return {"error": "retries exhausted"}


def to_provider(questions):
    """`noul` (TypeSafe) -> `boolean` (NordRouter); everything else goes as is."""
    out = {}
    for name, q in questions.items():
        q = dict(q)
        if q.get("type") == "noul":
            q["type"] = "boolean"
        out[name] = q
    return out


def from_provider(answers):
    out = {}
    for name, a in answers.items():
        a = dict(a)
        if a.get("type") == "boolean" and "probability" in a:
            a["noul"] = a["probability"]
        out[name] = a
    return out


def gh_rest(path, timeout=60, tries=6):
    """GitHub REST GET that respects the rate limit instead of dying on it.

    Reads X-RateLimit-Remaining/Reset on every answer and sleeps until the window
    rolls over when the budget is nearly gone — a fork walk over 15k repos needs
    several hourly windows and must survive them.
    """
    for attempt in range(tries):
        try:
            req = urllib.request.Request(f"https://api.github.com{path}", headers=gh_headers())
            with urllib.request.urlopen(req, timeout=timeout) as r:
                data = json.loads(r.read().decode())
                remaining, reset = r.headers.get("X-RateLimit-Remaining"), r.headers.get("X-RateLimit-Reset")
            if remaining is not None and reset and int(remaining) < 100:
                wait = max(5, int(reset) - int(time.time()) + 5)
                emit({"type": "log", "message": f"GitHub REST: осталось {remaining} запросов, пауза {wait} с до сброса окна"})
                time.sleep(wait)
            return data
        except urllib.error.HTTPError as e:
            reset, remaining = (e.headers.get("X-RateLimit-Reset") if e.headers else None), (e.headers.get("X-RateLimit-Remaining") if e.headers else None)
            if e.code in (403, 429) and (remaining == "0" or e.code == 429):
                wait = max(5, int(reset) - int(time.time()) + 5) if reset else 60
                emit({"type": "log", "message": f"лимит GitHub исчерпан (HTTP {e.code}), пауза {wait} с"})
                time.sleep(wait)
                continue
            if e.code in (404, 451):
                return {"error": f"HTTP {e.code}"}
            if attempt == tries - 1:
                raise
            time.sleep(2 * (attempt + 1))
        except Exception:
            if attempt == tries - 1:
                raise
            time.sleep(2 * (attempt + 1))


def gh_headers(extra=None):
    h = {"Accept": "application/vnd.github+json", **(extra or {})}
    if GH_TOKEN:
        h["Authorization"] = f"Bearer {GH_TOKEN}"
    return h


GQL = """query($owner:String!,$name:String!,$cursor:String){repository(owner:$owner,name:$name){
 defaultBranchRef{name}
 pullRequests(states:OPEN,first:40,after:$cursor,orderBy:{field:UPDATED_AT,direction:DESC}){
  pageInfo{hasNextPage endCursor}
  nodes{number title body isDraft createdAt updatedAt additions deletions authorAssociation author{login}
   files(first:100){nodes{path}} closingIssuesReferences(first:10){nodes{number}}}}}}"""


def clean_body(body):
    body = re.sub(r"<!--.*?-->|- \[[ x]\] .*|## Checklist.*|## Model Used.*?(?=\n## |\Z)", "", body or "", flags=re.S | re.I)
    return re.sub(r"\n{3,}", "\n\n", body).strip()[:3500]


# ---------- jobs ----------
def fetch_job(slug):
    if not GH_TOKEN:
        raise RuntimeError("Нужен GITHUB_TOKEN (токен GitHub без прав, только чтение публичных репозиториев)")
    P, t0, started = projects[slug], time.time(), now_iso()
    cfg = P["config"]
    owner, name = cfg["repo"].split("/")
    prs, cursor, page = {}, None, 0
    while True:
        res = http_json_retry("https://api.github.com/graphql", {"query": GQL, "variables": {"owner": owner, "name": name, "cursor": cursor}},
                              gh_headers({"Content-Type": "application/json"}), 120)
        if res.get("errors"):
            raise RuntimeError("GitHub: " + "; ".join(e.get("message", "") for e in res["errors"])[:300])
        repo = res["data"]["repository"]
        if not repo:
            raise RuntimeError("Репозиторий не найден или приватный")
        cfg["default_branch"] = (repo.get("defaultBranchRef") or {}).get("name") or "main"
        conn = repo["pullRequests"]
        for p in conn["nodes"]:
            author = (p.get("author") or {}).get("login") or "ghost"
            if p["isDraft"] and not cfg.get("include_drafts"):
                continue
            if author in cfg.get("exclude_authors", []):
                continue
            if cfg.get("community_only") and p["authorAssociation"] in ("OWNER", "MEMBER", "COLLABORATOR"):
                continue
            old = P["prs"].get(p["number"], {})
            prs[p["number"]] = {"number": p["number"], "title": p["title"], "author": author, "created": p["createdAt"], "updated": p["updatedAt"],
                                "additions": p["additions"], "deletions": p["deletions"], "files": [f["path"] for f in p["files"]["nodes"]],
                                "issues": [i["number"] for i in p["closingIssuesReferences"]["nodes"]], "body": clean_body(p["body"]),
                                "association": p["authorAssociation"],
                                **({"ai_description": old["ai_description"]} if old.get("ai_description") and old.get("updated") == p["updatedAt"] else {})}
        page += 1
        progress(len(prs), len(prs), phase="list", page=page)
        if not conn["pageInfo"]["hasNextPage"]:
            break
        cursor = conn["pageInfo"]["endCursor"]
    with lock:
        P["prs"] = prs
        if not cfg.get("custom_areas"):
            cfg["areas"], cfg["area_labels"] = auto_areas(prs.values())
        write_json(pdir(slug) / "config.json", cfg)
        save_prs(slug)
        P["included"] = load_included(cfg)
    recompute(slug)
    return {"stage": "fetch", "started": started, "seconds": round(time.time() - t0), "items": len(prs), "errors": 0, "input_tokens": 0, "cost_usd": 0, "model": "GitHub GraphQL"}


def save_prs(slug):
    write_json(pdir(slug) / "prs.json", list(projects[slug]["prs"].values()))


def ollama_models():
    try:
        return [m["name"] for m in http_json(f"{OLLAMA_URL}/api/tags", timeout=10)["models"] if "embed" not in m["name"]]
    except Exception:
        return []


def describe_job(slug):
    """Write a description from the diff when the author wrote little or nothing.

    Two providers: a local Ollama model (upstream default) or any OpenAI-compatible
    chat endpoint — here NordRouter, which needs no local GPU.
    """
    P, t0, started = projects[slug], time.time(), now_iso()
    cfg = P["config"]
    oc = cfg.get("ollama") or {}
    if not oc.get("enabled"):
        return None
    provider = oc.get("provider") or "ollama"
    describer_key = os.environ.get("NORDROUTER_API_KEY") or JEV_KEY
    if provider == "nordrouter" and not describer_key:
        raise RuntimeError("Для описаний через NordRouter нужен NORDROUTER_API_KEY")
    if not GH_TOKEN:
        raise RuntimeError("Для описаний нужен GITHUB_TOKEN (скачиваю дифы)")
    todo = [p for p in P["prs"].values() if len(p.get("body") or "") < oc.get("min_body", 200) and not p.get("ai_description")]
    out_tokens = 0
    progress(0, len(todo), phase="describe")

    def one(pr):
        req = urllib.request.Request(f"https://api.github.com/repos/{cfg['repo']}/pulls/{pr['number']}", headers=gh_headers({"Accept": "application/vnd.github.diff"}))
        with urllib.request.urlopen(req, timeout=60) as r:
            diff = r.read().decode(errors="ignore")[: oc.get("max_diff", 24000)]
        prompt = ("You review a GitHub pull request whose author wrote little or no description. From the title and the diff, "
                  "write a plain English description in 3-5 sentences: what problem it fixes or what it adds, and what the change does. "
                  f"No headings, no bullet points.\n\nTitle: {pr['title']}\n\nAuthor's text: {pr.get('body') or '(none)'}\n\nDiff:\n{diff}")
        if provider == "nordrouter":
            res = http_json_retry(f"{NORDROUTER_URL}/v1/chat/completions",
                                  {"model": oc.get("model") or DESCRIBER_MODEL, "messages": [{"role": "user", "content": prompt}],
                                   "max_tokens": oc.get("max_tokens", 400), "temperature": 0.2},
                                  {"Authorization": f"Bearer {describer_key}", "Content-Type": "application/json"}, 180)
            usage = res.get("usage") or {}
            text = (res["choices"][0]["message"].get("content") or "").strip()
            return pr["number"], text, usage.get("completion_tokens", 0)
        res = http_json(f"{OLLAMA_URL}/api/generate", {"model": oc.get("model", "qwen3.5:9b"), "prompt": prompt, "stream": False, "think": False,
                                                      "options": {"num_ctx": 16384, "temperature": 0.2}}, {"Content-Type": "application/json"}, 300)
        return pr["number"], res.get("response", "").strip(), res.get("eval_count", 0)

    done = 0
    with cf.ThreadPoolExecutor(DESCRIBER_WORKERS if provider == "nordrouter" else 2) as ex:
        for fut in cf.as_completed([ex.submit(one, p) for p in todo]):
            done += 1
            try:
                n, text, toks = fut.result()
                out_tokens += toks
                with lock:
                    P["prs"][n]["ai_description"] = text
                progress(done, len(todo), n, phase="describe", seconds=round(time.time() - t0, 1), preview=text[:160], title=P["prs"][n]["title"])
            except Exception as e:
                progress(done, len(todo), phase="describe", error=str(e)[:120])
            if done % 20 == 0:
                with lock:
                    save_prs(slug)
    with lock:
        save_prs(slug)
    recompute(slug)
    return {"stage": "describe", "started": started, "seconds": round(time.time() - t0), "items": len(todo), "errors": 0,
            "input_tokens": 0, "output_tokens": out_tokens, "cost_usd": 0, "model": f"ollama/{oc.get('model')}"}


def stage1_job(slug, limit=None):
    P, t0, started = projects[slug], time.time(), now_iso()
    questions = stage1_questions(P["config"])
    prs = list(P["prs"].values())[: limit or None]
    tokens, done, errors = 0, 0, 0
    progress(0, len(prs), phase="stage1")
    with cf.ThreadPoolExecutor(STAGE1_WORKERS) as ex:
        futures = {ex.submit(jev, stage1_state(p), questions): p["number"] for p in prs}
        for fut in cf.as_completed(futures):
            n, res = futures[fut], fut.result()
            done += 1
            row = None
            if "answers" in res:
                tokens += res["usage"]["input_tokens"]
                with lock:
                    P["stage1"][str(n)] = {"answers": res["answers"], "usage": res["usage"]}
                    row = {**P["rows"].get(n, {}), **score_pr(P["prs"][n], res["answers"])}
            else:
                errors += 1
            progress(done, len(prs), n, phase="stage1", row=row, tokens=tokens, cost=round(tokens * PRICE_PER_MTOK / 1e6, 4), seconds=round(time.time() - t0, 1))
    with lock:
        save(slug, "stage1")
    recompute(slug)
    return {"stage": "stage1", "started": started, "seconds": round(time.time() - t0), "items": len(prs), "errors": errors,
            "input_tokens": tokens, "cost_usd": round(tokens * PRICE_PER_MTOK / 1e6, 4), "model": "jev-latest"}


SKIP_FILE = re.compile(r"(pnpm-lock\.yaml|package-lock\.json|yarn\.lock|\.snap$|\.svg$|\.png$|\.lock$|/dist/|generated)")


def stage2_job(slug):
    P, t0, started = projects[slug], time.time(), now_iso()
    cfg = P["config"]
    repo = pdir(slug) / "repo"

    def git(*args, check=False):
        r = subprocess.run(["git", "-C", str(repo), *args], capture_output=True, text=True)
        if check and r.returncode:
            raise RuntimeError(f"git {' '.join(args)}: {r.stderr[-300:]}")
        return r

    recompute(slug)
    finalists, base = list(P["finalists"]), cfg.get("default_branch", "main")
    progress(0, len(finalists), phase="git")
    if not (repo / ".git").exists():
        emit({"type": "log", "message": "Клонирую репозиторий (один раз, пару минут)…"})
        subprocess.run(["git", "clone", "--filter=blob:none", "--no-tags", f"https://github.com/{cfg['repo']}.git", str(repo)], check=True, capture_output=True)
    git("config", "user.email", "scout@localhost"); git("config", "user.name", "PR Scout")
    git("merge", "--abort"); git("reset", "-q", "--hard"); git("clean", "-fdq")
    git("fetch", "-q", "--no-tags", "origin", base, check=True)
    git("checkout", "-q", "-B", "stack", f"origin/{base}", check=True)
    for n in sorted(P["included"]):
        git("fetch", "-q", "origin", f"pull/{n}/head:pr-{n}")
        if git("merge", "-q", "--no-ff", "--no-edit", f"pr-{n}").returncode:
            git("merge", "--abort")
            emit({"type": "log", "message": f"#{n} из «уже взятых» не вливается в свежую {base}"})
    merges, diffs = {}, {}
    # Ветки PR качаем параллельно: 120 последовательных fetch — это минуты ожидания сети.
    with cf.ThreadPoolExecutor(MERGE_WORKERS) as ex:
        for n, failed in ex.map(lambda n: (n, git("fetch", "-q", "origin", f"pull/{n}/head:pr-{n}").returncode != 0), finalists):
            if failed:
                merges[n] = {"merge": "fetch_failed", "conflicts": []}

    # Тестовый мерж каждого финалиста идёт в своей рабочей копии: параллельные merge в одном
    # дереве топчут друг друга (upstream делал это последовательно — 32 минуты из 48 на 3000 PR).
    stack_sha = git("rev-parse", "stack").stdout.strip()
    git("worktree", "prune")
    pool = Queue()
    worktrees = []
    for i in range(max(1, MERGE_WORKERS)):
        wt = repo.parent / f"merge-{i}"
        if wt.exists():
            subprocess.run(["git", "-C", str(repo), "worktree", "remove", "--force", str(wt)], capture_output=True, text=True)
        r = subprocess.run(["git", "-C", str(repo), "worktree", "add", "--detach", "--force", str(wt), stack_sha], capture_output=True, text=True)
        if r.returncode:
            emit({"type": "log", "message": f"worktree {wt.name} не создался: {r.stderr[-200:]}"})
            continue
        worktrees.append(wt)
        pool.put(wt)

    def wgit(wt, *args):
        return subprocess.run(["git", "-C", str(wt), *args], capture_output=True, text=True)

    def test_merge(args):
        i, n = args
        if n in merges:  # ветка не скачалась
            progress(i, len(finalists), n, phase="merge", merge=merges[n]["merge"])
            return n, merges[n], diff_of(n)
        wt = pool.get()
        try:
            wgit(wt, "reset", "-q", "--hard", stack_sha)
            wgit(wt, "clean", "-fdq")
            m = wgit(wt, "merge", "--no-commit", "--no-ff", f"pr-{n}")
            conflicts = wgit(wt, "diff", "--name-only", "--diff-filter=U").stdout.split() if m.returncode else []
            wgit(wt, "merge", "--abort")
            wgit(wt, "reset", "-q", "--hard", stack_sha)
            wgit(wt, "clean", "-fdq")
            res = {"merge": "clean" if m.returncode == 0 else ("conflict" if conflicts else "error"), "conflicts": conflicts[:10],
                   **({"message": (m.stderr or m.stdout)[-240:]} if m.returncode and not conflicts else {})}
        finally:
            pool.put(wt)
        progress(i, len(finalists), n, phase="merge", merge=res["merge"])
        return n, res, diff_of(n)

    def diff_of(n):
        """Diff of the PR against its merge base. Read-only: safe to run in parallel."""
        mb = git("merge-base", "stack", f"pr-{n}").stdout.strip()
        chunks = [c for c in re.split(r"(?=^diff --git )", git("diff", mb, f"pr-{n}").stdout if mb else "", flags=re.M)
                  if c.strip() and not SKIP_FILE.search(c.split("\n", 1)[0])]
        chunks.sort(key=lambda c: ("test" in c.split("\n", 1)[0].lower(), len(c)))
        text = ""
        for c in chunks:
            if len(text) + len(c) <= 90_000:
                text += c
        return text or "(empty diff)"

    try:
        with cf.ThreadPoolExecutor(max(1, len(worktrees))) as ex:
            for n, res, text in ex.map(test_merge, [(i, n) for i, n in enumerate(finalists, 1)]):
                merges[n], diffs[n] = res, text
    finally:
        for wt in worktrees:
            subprocess.run(["git", "-C", str(repo), "worktree", "remove", "--force", str(wt)], capture_output=True, text=True)
        git("worktree", "prune")

    def ci_status(n, previous):
        if not GH_TOKEN:
            return previous
        try:
            runs = http_json(f"https://api.github.com/repos/{cfg['repo']}/commits/{git('rev-parse', f'pr-{n}').stdout.strip()}/check-runs?per_page=100", headers=gh_headers(), timeout=30)["check_runs"]
        except Exception:
            return previous
        failing = [c["name"] for c in runs if c.get("conclusion") in ("failure", "timed_out")]
        return {"pass": sum(c.get("conclusion") == "success" for c in runs), "fail": len(failing),
                "pending": sum(c.get("status") != "completed" for c in runs), "failing": failing[:12], "none": not runs}

    tokens, done = 0, 0
    def review(n):
        pr = P["prs"][n]
        return n, jev({"title": pr["title"], "description": (pr.get("body") or pr.get("ai_description") or "")[:1500], "diff": diffs.get(n, "(no diff)")}, STAGE2_QUESTIONS)
    with cf.ThreadPoolExecutor(STAGE2_WORKERS) as ex:
        for n, res in ex.map(review, finalists):
            done += 1
            if "answers" in res:
                tokens += res["usage"]["input_tokens"]
                with lock:
                    prev = P["stage2"].get(str(n), {})
                    P["stage2"][str(n)] = {"merge": merges[n], "ci": ci_status(n, prev.get("ci")), "review": {"answers": res["answers"], "usage": res["usage"]}}
            progress(done, len(finalists), n, phase="review", tokens=tokens, seconds=round(time.time() - t0, 1))
    with lock:
        save(slug, "stage2")
    recompute(slug)
    return {"stage": "stage2", "started": started, "seconds": round(time.time() - t0), "items": len(finalists), "errors": 0,
            "input_tokens": tokens, "cost_usd": round(tokens * PRICE_PER_MTOK / 1e6, 4), "model": "jev-latest"}


# ---------- issues, forks, rivals: the same Jev, three more questions ----------
GQL_ISSUES = """query($owner:String!,$name:String!,$cursor:String){repository(owner:$owner,name:$name){
 issues(states:OPEN,first:50,after:$cursor,orderBy:{field:UPDATED_AT,direction:DESC}){
  pageInfo{hasNextPage endCursor}
  nodes{number title body createdAt updatedAt comments{totalCount} authorAssociation author{login}
   labels(first:10){nodes{name}}}}}}"""

GQL_FORKS = """query($owner:String!,$name:String!,$cursor:String){repository(owner:$owner,name:$name){
 forks(first:100,after:$cursor,orderBy:{field:PUSHED_AT,direction:DESC}){
  pageInfo{hasNextPage endCursor}
  nodes{nameWithOwner name pushedAt stargazerCount isFork owner{login}
   defaultBranchRef{name target{... on Commit{oid}}}}}}}"""


def fetch_issues_job(slug):
    """All open issues of the upstream repository (metadata only, no Jev yet)."""
    P, t0, started = projects[slug], time.time(), now_iso()
    cfg, owner, name = P["config"], *P["config"]["repo"].split("/")
    excluded = set(cfg.get("exclude_authors") or [])
    issues, cursor, page = {}, None, 0
    while True:
        res = http_json_retry("https://api.github.com/graphql", {"query": GQL_ISSUES, "variables": {"owner": owner, "name": name, "cursor": cursor}},
                              gh_headers({"Content-Type": "application/json"}), 120)
        if res.get("errors"):
            raise RuntimeError("GitHub: " + "; ".join(e.get("message", "") for e in res["errors"])[:300])
        conn = (res.get("data") or {}).get("repository", {}).get("issues")
        if not conn:
            raise RuntimeError("Репозиторий не найден или приватный")
        for i in conn["nodes"]:
            author = (i.get("author") or {}).get("login") or "ghost"
            if author in excluded:
                continue
            issues[i["number"]] = {"number": i["number"], "title": i["title"], "body": clean_body(i["body"]), "author": author,
                                   "association": i["authorAssociation"], "created": i["createdAt"], "updated": i["updatedAt"],
                                   "comments": i["comments"]["totalCount"], "labels": [x["name"] for x in i["labels"]["nodes"]]}
        page += 1
        progress(len(issues), len(issues), phase="issues-list", page=page)
        if not conn["pageInfo"]["hasNextPage"]:
            break
        cursor = conn["pageInfo"]["endCursor"]
    with lock:
        old = P.get("issues") or {}
        P["issues"] = {str(n): {**old.get(str(n), {}), "meta": m} for n, m in issues.items()}
        save(slug, "issues")
    recompute(slug)
    return {"stage": "issues-list", "started": started, "seconds": round(time.time() - t0), "items": len(issues), "errors": 0,
            "input_tokens": 0, "cost_usd": 0, "model": "GitHub GraphQL"}


def issues_job(slug):
    """Ask Jev what every open issue is and how much it hurts — including issues no PR touches."""
    P, t0, started = projects[slug], time.time(), now_iso()
    questions = issue_questions(P["config"])
    todo = [n for n, v in P["issues"].items() if v.get("meta")]
    tokens, done, errors = 0, 0, 0
    progress(0, len(todo), phase="issues")
    with cf.ThreadPoolExecutor(STAGE1_WORKERS) as ex:
        futures = {ex.submit(jev, {"repo": P["config"]["repo"], "number": v["meta"]["number"], "title": v["meta"]["title"],
                                   "labels": v["meta"]["labels"], "created": v["meta"]["created"], "comments": v["meta"]["comments"],
                                   "description": (v["meta"]["body"] or "(no description)")[:2500]}, questions): int(n)
                   for n, v in ((n, v) for n, v in P["issues"].items() if v.get("meta"))}
        for fut in cf.as_completed(futures):
            n, res = futures[fut], fut.result()
            done += 1
            if "answers" in res:
                tokens += res["usage"]["input_tokens"]
                with lock:
                    P["issues"][str(n)]["answers"] = res["answers"]
                    P["issues"][str(n)]["usage"] = res["usage"]
            else:
                errors += 1
            progress(done, len(todo), n, phase="issues", tokens=tokens, seconds=round(time.time() - t0, 1))
    with lock:
        save(slug, "issues")
    recompute(slug)
    return {"stage": "issues", "started": started, "seconds": round(time.time() - t0), "items": len(todo), "errors": errors,
            "input_tokens": tokens, "cost_usd": round(tokens * PRICE_PER_MTOK / 1e6, 4), "model": "Jev"}


def fetch_forks_job(slug):
    """The fork list of the upstream repository: who forked, when they last pushed, their head commit."""
    P, t0, started = projects[slug], time.time(), now_iso()
    owner, name = P["config"]["repo"].split("/")
    forks, cursor, page = {}, None, 0
    while True:
        res = http_json_retry("https://api.github.com/graphql", {"query": GQL_FORKS, "variables": {"owner": owner, "name": name, "cursor": cursor}},
                              gh_headers({"Content-Type": "application/json"}), 120)
        if res.get("errors"):
            raise RuntimeError("GitHub: " + "; ".join(e.get("message", "") for e in res["errors"])[:300])
        conn = (res.get("data") or {}).get("repository", {}).get("forks")
        if not conn:
            raise RuntimeError("Репозиторий не найден или приватный")
        for f in conn["nodes"]:
            branch = (f.get("defaultBranchRef") or {})
            forks[f["nameWithOwner"]] = {"fork": f["nameWithOwner"], "owner": (f.get("owner") or {}).get("login"),
                                         "pushed": f["pushedAt"], "stars": f["stargazerCount"],
                                         "branch": branch.get("name"), "oid": ((branch.get("target") or {}) or {}).get("oid")}
        page += 1
        progress(len(forks), len(forks), phase="forks-list", page=page)
        if not conn["pageInfo"]["hasNextPage"]:
            break
        cursor = conn["pageInfo"]["endCursor"]
    with lock:
        old = P.get("forks") or {}
        P["forks"] = {k: {**old.get(k, {}), **v} for k, v in forks.items()}
        save(slug, "forks")
    recompute(slug)
    return {"stage": "forks-list", "started": started, "seconds": round(time.time() - t0), "items": len(forks), "errors": 0,
            "input_tokens": 0, "cost_usd": 0, "model": "GitHub GraphQL"}


def forks_job(slug):
    """Compare every fork with upstream and ask Jev about the commits it has ahead.

    One compare request per fork; the REST budget is 5000/h, so the walk spans several
    hourly windows by design (gh_rest sleeps to the reset instead of failing).
    """
    P, t0, started = projects[slug], time.time(), now_iso()
    cfg = P["config"]
    fcfg = cfg.get("forks") or {}
    owner, name = cfg["repo"].split("/")
    base = cfg.get("default_branch") or "main"
    forks = [f for f in P["forks"].values() if f.get("branch")]
    forks.sort(key=lambda f: f.get("pushed") or "", reverse=True)
    if fcfg.get("limit"):
        forks = forks[: int(fcfg["limit"])]
    if fcfg.get("min_stars"):
        forks = [f for f in forks if (f.get("stars") or 0) >= int(fcfg["min_stars"])]
    todo = [f for f in forks if not f.get("scanned")]
    progress(0, len(todo), phase="forks-compare")
    errs = 0
    t0 = time.time()

    def compare(f):
        fork_owner, fork_repo = f["fork"].split("/")
        path = f"/repos/{owner}/{name}/compare/{base}...{fork_owner}:{f['branch']}"
        res = gh_rest(path)
        if res.get("error"):
            return f, {"status": res["error"], "ahead": 0, "behind": 0, "commits": [], "files": [], "lines": 0}
        commits = [{"sha": c["sha"][:8], "date": (c.get("commit", {}).get("author") or {}).get("date", "")[:10],
                    "message": (c.get("commit", {}).get("message") or "").split("\n")[0][:200]} for c in (res.get("commits") or [])]
        lines = sum((x.get("additions") or 0) + (x.get("deletions") or 0) for x in (res.get("files") or []))
        return f, {"status": res.get("status"), "ahead": res.get("ahead_by", 0), "behind": res.get("behind_by", 0),
                   "truncated": bool(res.get("total_commits", 0) > len(commits)),
                   "commits": commits[-int(fcfg.get("max_commits", 30)):], "files": [x["filename"] for x in (res.get("files") or [])][:20],
                   "lines": lines, "scanned": now_iso()}

    done = 0
    with cf.ThreadPoolExecutor(FORK_REST_WORKERS) as ex:
        for fut in cf.as_completed([ex.submit(compare, f) for f in todo]):
            f, res = fut.result()
            done += 1
            with lock:
                P["forks"][f["fork"]].update(res)
                if done % 25 == 0:
                    save(slug, "forks")
            progress(done, len(todo), phase="forks-compare", ahead=sum(1 for v in P["forks"].values() if (v.get("ahead") or 0) > 0),
                     seconds=round(time.time() - t0, 1))
    ahead = [f for f in P["forks"].values() if (f.get("ahead") or 0) > 0 and f.get("commits")]
    questions = fork_questions(cfg)
    tokens, errs = 0, 0
    progress(0, len(ahead), phase="forks")
    t0 = time.time()
    with cf.ThreadPoolExecutor(STAGE1_WORKERS) as ex:
        futures = {ex.submit(jev, {"repo": cfg["repo"], "fork": f["fork"], "behind_upstream_by": f.get("behind"),
                                   "commits": f["commits"], "files": f.get("files")}, questions): f["fork"] for f in ahead}
        for fut in cf.as_completed(futures):
            key, res = futures[fut], fut.result()
            done += 1
            if "answers" in res:
                tokens += res["usage"]["input_tokens"]
                with lock:
                    P["forks"][key]["answers"] = res["answers"]
                    P["forks"][key]["usage"] = res["usage"]
            else:
                errs += 1
            progress(done, len(ahead), phase="forks", tokens=tokens, seconds=round(time.time() - t0, 1))
    with lock:
        save(slug, "forks")
    recompute(slug)
    return {"stage": "forks", "started": started, "seconds": round(time.time() - t0), "items": len(todo), "errors": errs,
            "input_tokens": tokens, "cost_usd": round(tokens * PRICE_PER_MTOK / 1e6, 4), "model": "GitHub compare + Jev"}


def rivals_job(slug):
    """One issue, several pull requests: ask Jev which one to take."""
    P, t0, started = projects[slug], time.time(), now_iso()
    cfg = P["config"]
    groups = {}
    for n, pr in P["prs"].items():
        for i in (pr.get("issues") or []):
            groups.setdefault(i, []).append(n)
    todo = {i: sorted(v, key=lambda n: -(P["rows"].get(n, {}).get("score") or 0)) for i, v in groups.items() if len(v) > 1}
    rivals, tokens, errors, done = {}, 0, 0, 0
    progress(0, len(todo), phase="rivals")
    questions = None

    def ask(item):
        issue_no, nums = item
        meta = (P["issues"].get(str(issue_no)) or {}).get("meta") or {"number": issue_no, "title": f"issue #{issue_no}", "body": ""}
        cands = []
        for n in nums[:8]:
            row = {**P["rows"].get(n, {}), "number": n, "auto": is_bot(P["prs"][n].get("author"))}
            s2 = P["stage2"].get(str(n)) or {}
            if s2.get("review"):
                row["review"] = {k: round(v, 2) for k, v in _review_numbers(s2["review"]["answers"]).items()}
                row["merge_status"] = (s2.get("merge") or {}).get("merge")
            cands.append(row)
        q, body = rival_question(cfg, {**meta, "body": (meta.get("body") or "")[:1200]}, cands)
        return issue_no, meta, cands, q

    prepared = [ask(item) for item in todo.items()]
    with cf.ThreadPoolExecutor(STAGE1_WORKERS) as ex:
        futures = {}
        for issue_no, meta, cands, q in prepared:
            futures[ex.submit(jev, {"repo": cfg["repo"], "issue": {"number": meta["number"], "title": meta["title"],
                                                                   "description": (meta.get("body") or "")[:1200]},
                                    "candidates": [c["title"] for c in cands]}, q)] = (issue_no, meta)
        for fut in cf.as_completed(futures):
            (issue_no, meta), res = futures[fut], fut.result()
            done += 1
            if "answers" in res:
                tokens += res["usage"]["input_tokens"]
                with lock:
                    rivals[str(issue_no)] = {**apply_rival(res["answers"], meta), "candidates": todo[issue_no], "usage": res["usage"]}
            else:
                errors += 1
            progress(done, len(todo), issue_no, phase="rivals", tokens=tokens, seconds=round(time.time() - t0, 1))
    with lock:
        P["rivals"] = rivals
        save(slug, "rivals")
    recompute(slug)
    return {"stage": "rivals", "started": started, "seconds": round(time.time() - t0), "items": len(todo), "errors": errors,
            "input_tokens": tokens, "cost_usd": round(tokens * PRICE_PER_MTOK / 1e6, 4), "model": "Jev"}


BOT_AUTHORS = re.compile(r"(\[bot\]$|-bot$|^dependabot|^renovate|^github-actions)", re.I)


def is_bot(author):
    return bool(BOT_AUTHORS.search(author or ""))


def _review_numbers(answers):
    return {k: v.get("score", v.get("noul", 0)) for k, v in answers.items()}


# ---------- API ----------
LIST_FIELDS = ("number", "title", "author", "updated", "additions", "deletions", "files", "included", "classified", "kind", "area", "track",
               "relevance", "bug_severity", "feature_value", "harm", "common_case", "new_capability", "risky", "score", "rank",
               "duplicate_of", "finalist", "verdict", "ci_class", "ai_description", "reasons")


@app.get("/api/projects")
def list_projects():
    with lock:
        out = []
        for slug, P in projects.items():
            rows = P["rows"].values()
            out.append({"slug": slug, "repo": P["config"]["repo"], "name": P["config"].get("name") or P["config"]["repo"],
                        "prs": len(P["prs"]), "classified": sum(r["classified"] for r in rows),
                        "take": sum(r.get("verdict") == "take" for r in rows), "last_run": P["runs"][-1]["started"] if P["runs"] else None})
        return out


def parse_repo(text):
    m = re.search(r"(?:github\.com[/:])?([\w.-]+)/([\w.-]+?)(?:\.git)?/?$", text.strip())
    if not m:
        raise HTTPException(400, "Не понял ссылку. Нужна вида https://github.com/owner/repo")
    return f"{m.group(1)}/{m.group(2)}"


@app.post("/api/projects")
async def create_project(request: Request):
    body = await request.json()
    repo = parse_repo(body.get("url", ""))
    slug = slug_of(repo)
    if slug in projects:
        raise HTTPException(409, "Такой проект уже есть")
    preset = preset_for(repo)
    cfg = {"repo": repo, "name": body.get("name") or preset.get("name") or repo.split("/")[1], "profile": body.get("profile", "").strip() or preset.get("profile", ""),
           "community_only": body.get("community_only", True), "include_drafts": False, "exclude_authors": [],
           "stack_prs": [], "stack_prs_url": "", "finalists": int(body.get("finalists") or 120),
           "ollama": {"enabled": bool(body.get("ollama", True)), "model": body.get("ollama_model") or "qwen3.5:9b", "min_body": 200},
           "areas": {"other": "Anything else"}, "area_labels": {"other": "Прочее"}}
    for k in ("areas", "area_labels", "exclude_authors", "stack_prs_url", "default_branch"):
        if k in preset:
            cfg[k] = preset[k]
    cfg["custom_areas"] = "areas" in preset
    write_json(pdir(slug) / "config.json", cfg)
    load_project(slug)
    if body.get("run", True):
        run_job("full", slug, [fetch_job, describe_job, stage1_job, stage2_job])
    return {"slug": slug}


@app.put("/api/p/{slug}/config")
async def update_config(slug: str, request: Request):
    P, body = get_project(slug), await request.json()
    with lock:
        cfg = P["config"]
        for k in ("name", "profile", "community_only", "include_drafts", "finalists", "stack_prs_url"):
            if k in body:
                cfg[k] = body[k]
        for k in ("forks", "triage"):
            if k in body:
                cfg[k] = {**cfg.get(k, {}), **body[k]}
        if "exclude_authors" in body:
            cfg["exclude_authors"] = [a.strip() for a in re.split(r"[,\s]+", body["exclude_authors"]) if a.strip()] if isinstance(body["exclude_authors"], str) else body["exclude_authors"]
        if "stack_prs" in body:
            cfg["stack_prs"] = [int(x) for x in re.findall(r"\d+", str(body["stack_prs"]))]
        if "ollama" in body:
            cfg["ollama"] = {**cfg.get("ollama", {}), **body["ollama"]}
        write_json(pdir(slug) / "config.json", cfg)
        P["included"] = load_included(cfg)
    recompute(slug)
    return cfg


@app.delete("/api/p/{slug}")
def delete_project(slug: str):
    get_project(slug)
    if job["project"] == slug:
        raise HTTPException(409, "По проекту идёт задача")
    with lock:
        projects.pop(slug)
    shutil.rmtree(pdir(slug), ignore_errors=True)
    return {"ok": True}


@app.get("/api/p/{slug}/prs")
def list_prs(slug: str):
    P = get_project(slug)
    with lock:
        return [{k: r.get(k) for k in LIST_FIELDS} for r in P["rows"].values()]


@app.get("/api/p/{slug}/prs/{n}")
def pr_detail(slug: str, n: int):
    P = get_project(slug)
    with lock:
        pr = P["prs"].get(n)
        if not pr:
            raise HTTPException(404)
        return {"pr": pr, "row": P["rows"].get(n), "stage1": P["stage1"].get(str(n)), "stage2": P["stage2"].get(str(n))}


@app.get("/api/p/{slug}/summary")
def summary(slug: str):
    P = get_project(slug)
    with lock:
        rows = list(P["rows"].values())
        issues = list((P.get("issue_rows") or {}).values())
        forks = list((P.get("fork_rows") or {}).values())
        return {"total": len(rows), "classified": sum(r["classified"] for r in rows), "finalists": len(P["finalists"]),
                "included": sorted(P["included"]), "runs": P["runs"], "job": dict(job), "config": P["config"],
                "issues": {"total": len(issues), "classified": sum(r["classified"] for r in issues),
                           "without_pr": sum(1 for r in issues if r["classified"] and not r.get("open_pr")),
                           "ranked": sorted([r for r in issues if r["classified"]], key=lambda r: -(r.get("score") or 0))[:20]},
                "forks": {"scanned": len(forks), "ahead": sum(1 for r in forks if (r.get("ahead") or 0) > 0),
                          "classified": sum(r["classified"] for r in forks),
                          "total": len(P.get("forks") or {}),
                          "ranked": sorted([r for r in forks if r["classified"]], key=lambda r: -(r.get("score") or 0))[:20]},
                "rivals": {"groups": len(P.get("rivals") or {}),
                           "picked": sum(1 for r in (P.get("rivals") or {}).values() if r.get("chosen_pr")),
                           "list": list((P.get("rivals") or {}).values())},
                "jev_ready": bool(JEV_KEY), "github_ready": bool(GH_TOKEN), "comparison": cost_comparison(P["runs"])}


@app.get("/api/p/{slug}/issues")
def list_issues(slug: str):
    P = get_project(slug)
    with lock:
        return sorted((P.get("issue_rows") or {}).values(), key=lambda r: -(r.get("score") or 0))


@app.get("/api/p/{slug}/forks")
def list_forks(slug: str):
    P = get_project(slug)
    with lock:
        return sorted((P.get("fork_rows") or {}).values(), key=lambda r: -(r.get("score") or 0))


@app.get("/api/p/{slug}/rivals")
def list_rivals(slug: str):
    P = get_project(slug)
    with lock:
        return (P.get("rivals") or {})


@app.get("/api/p/{slug}/criteria")
def criteria(slug: str):
    cfg = get_project(slug)["config"]
    return {"setup": cfg.get("profile"), "stage1": stage1_questions(cfg), "stage2": STAGE2_QUESTIONS, "labels": QUESTION_LABELS,
            "areas": cfg.get("area_labels") or {}, "kinds": KIND_LABELS, "finalists": cfg.get("finalists", 120), "negative": NEGATIVE}


@app.get("/api/ollama/models")
def get_ollama_models():
    return ollama_models()


@app.post("/api/p/{slug}/jobs/{name}")
async def start_job(slug: str, name: str, request: Request):
    get_project(slug)
    if name not in ("fetch", "describe") and not JEV_KEY:
        raise HTTPException(400, "Не задан ключ Jev (TYPESAFE_API_KEY или NORDROUTER_API_KEY)")
    body = await request.json() if request.headers.get("content-length") not in (None, "0") else {}
    pipelines = {
        "full": [fetch_job, describe_job, stage1_job, stage2_job],
        "everything": [fetch_job, describe_job, stage1_job, stage2_job, fetch_issues_job, issues_job, rivals_job, fetch_forks_job, forks_job],
        "fetch": [fetch_job], "describe": [describe_job], "stage2": [stage2_job],
        "stage1": [(lambda s: stage1_job(s, body.get("limit")))],
        "issues": [fetch_issues_job, issues_job], "issues_meta": [fetch_issues_job], "issues_jev": [issues_job],
        "forks": [fetch_forks_job, forks_job], "forks_meta": [fetch_forks_job], "forks_compare": [forks_job],
        "rivals": [rivals_job],
    }
    if name not in pipelines:
        raise HTTPException(404)
    if name == "stage1":
        pipelines["stage1"][0].__name__ = "stage1_job"
    run_job(name, slug, pipelines[name])
    return {"ok": True}


@app.get("/api/status")
def status():
    return {"job": dict(job), "jev_ready": bool(JEV_KEY), "github_ready": bool(GH_TOKEN), "ollama_models": ollama_models()}


@app.get("/api/events")
async def events(request: Request):
    q: asyncio.Queue = asyncio.Queue()
    listeners.append(q)

    async def stream():
        try:
            yield f"data: {json.dumps({'type': 'hello', 'job': dict(job)})}\n\n"
            while not await request.is_disconnected():
                try:
                    yield f"data: {json.dumps(await asyncio.wait_for(q.get(), timeout=15), ensure_ascii=False)}\n\n"
                except asyncio.TimeoutError:
                    yield ": ping\n\n"
        finally:
            listeners.remove(q)
    return StreamingResponse(stream(), media_type="text/event-stream", headers={"Cache-Control": "no-cache", "X-Accel-Buffering": "no"})


@app.get("/healthz")
def healthz():
    return {"ok": True}


@app.get("/")
def index():
    return FileResponse(APP_DIR / "static" / "index.html")


app.mount("/static", StaticFiles(directory=APP_DIR / "static"), name="static")
