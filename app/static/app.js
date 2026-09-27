/* PR Scout front end: no build step, no framework. */
const $ = (s, el = document) => el.querySelector(s);
const $$ = (s, el = document) => [...el.querySelectorAll(s)];
const esc = (s) => String(s ?? "").replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
const fmt = (n, d = 0) => (n ?? 0).toLocaleString("ru-RU", { maximumFractionDigits: d, minimumFractionDigits: d });
const money = (n) => (!n ? "$0" : n < 1 ? "$" + fmt(n, n < 0.01 ? 4 : n < 0.1 ? 3 : 2) : "$" + fmt(n, n < 10 ? 2 : 0));
const secs = (s) => (s < 90 ? `${fmt(s)} с` : s < 5400 ? `${fmt(s / 60, 1)} мин` : `${fmt(s / 3600, 1)} ч`);
const ago = (iso) => {
  if (!iso) return "";
  const m = (Date.now() - new Date(iso)) / 60000;
  return m < 1 ? "только что" : m < 60 ? `${Math.round(m)} мин назад` : m < 1440 ? `${Math.round(m / 60)} ч назад` : `${Math.round(m / 1440)} дн назад`;
};

const I = {
  github: '<svg viewBox="0 0 24 24"><path d="M9 19c-4 1.5-4-2-6-2m12 4v-3.5c0-1 .1-1.4-.5-2 2.8-.3 5.5-1.4 5.5-6a4.6 4.6 0 0 0-1.3-3.2 4.2 4.2 0 0 0-.1-3.2s-1.1-.3-3.5 1.3a12 12 0 0 0-6.2 0C6.5 2.8 5.4 3.1 5.4 3.1a4.2 4.2 0 0 0-.1 3.2A4.6 4.6 0 0 0 4 9.5c0 4.6 2.7 5.7 5.5 6-.6.6-.6 1.2-.5 2V21"/></svg>',
  chip: '<svg viewBox="0 0 24 24"><rect x="6" y="6" width="12" height="12" rx="2"/><path d="M9 2v4M15 2v4M9 18v4M15 18v4M2 9h4M2 15h4M18 9h4M18 15h4"/></svg>',
  spark: '<svg viewBox="0 0 24 24"><path d="M12 3l1.9 5.8L20 11l-6.1 2.2L12 19l-1.9-5.8L4 11l6.1-2.2z"/></svg>',
  branch: '<svg viewBox="0 0 24 24"><circle cx="6" cy="5" r="2.5"/><circle cx="6" cy="19" r="2.5"/><circle cx="18" cy="8" r="2.5"/><path d="M6 7.5v9M18 10.5c0 4-6 3-10.8 6.5"/></svg>',
  play: '<svg viewBox="0 0 24 24"><path d="M7 4.5v15l12-7.5z" fill="currentColor" stroke="none"/></svg>',
  down: '<svg viewBox="0 0 24 24"><path d="m6 9 6 6 6-6"/></svg>',
  sun: '<svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg>',
  moon: '<svg viewBox="0 0 24 24"><path d="M21 12.8A9 9 0 1 1 11.2 3a7 7 0 0 0 9.8 9.8z"/></svg>',
  x: '<svg viewBox="0 0 24 24"><path d="M18 6 6 18M6 6l12 12"/></svg>',
};
const STEPS = [
  { key: "fetch", t: "Сбор PR", by: "GitHub GraphQL", ico: "github" },
  { key: "describe", t: "Описания", by: "локальная модель · Ollama", ico: "chip" },
  { key: "stage1", t: "Классификация", by: "Jev · все PR", ico: "spark" },
  { key: "stage2", t: "Код и мерж", by: "git + Jev · финалисты", ico: "branch" },
];
const VERDICT = { take: "Берём", consider: "Рассмотреть", skip: "Пропускаем" };
const TRACK = { fix: "Фикс", feature: "Фича", other: "Прочее" };
const CI = { green: ["ok", "CI зелёный"], flaky_only: ["warn", "CI: только флаки"], e2e_only: ["warn", "CI: только флаки"], red: ["bad", "CI красный"], no_ci: ["line", "без CI"] };
const KIND_COLORS = ["var(--k8)", "var(--k0)", "var(--k1)", "var(--k2)", "var(--k3)", "var(--k4)", "var(--k5)", "var(--k6)", "var(--k7)"];

const S = { slug: null, projects: [], status: {}, summary: null, prs: [], criteria: null, sort: { key: "score", dir: -1 }, shown: 120,
  track: "", live: null, job: null };

async function api(path, opts) {
  const r = await fetch(path, opts);
  if (!r.ok) throw new Error((await r.json().catch(() => ({}))).detail || r.statusText);
  return r.json();
}
const P = (path) => `/api/p/${S.slug}${path}`;
const post = (url, body, method = "POST") => api(url, { method, headers: { "Content-Type": "application/json" }, body: JSON.stringify(body || {}) });
const areaLabel = (a) => (S.criteria?.areas || {})[a] || a || "—";
const kindLabel = (k) => (S.criteria?.kinds || {})[k] || k || "—";

function toast(text, kind = "") {
  const el = document.createElement("div");
  el.className = `toast ${kind}`;
  el.innerHTML = `<div>${text}</div>`;
  $("#toasts").append(el);
  setTimeout(() => { el.style.transition = "opacity .3s"; el.style.opacity = "0"; setTimeout(() => el.remove(), 300); }, 4200);
}

function ring(score, size = 44) {
  const sw = size > 60 ? 4 : 3, r = (size - sw) / 2 - 1, c = 2 * Math.PI * r, v = Math.max(0, Math.min(100, score || 0)), m = size / 2;
  return `<div class="ring ${size > 60 ? "lg" : ""}" style="width:${size}px;height:${size}px"><svg width="${size}" height="${size}" viewBox="0 0 ${size} ${size}"><circle cx="${m}" cy="${m}" r="${r}" fill="none" stroke="var(--surface-3)" stroke-width="${sw}"/>
    <circle cx="${m}" cy="${m}" r="${r}" fill="none" stroke="var(--ink)" stroke-width="${sw}" stroke-linecap="round" stroke-dasharray="${(c * v) / 100} ${c}"/></svg><span class="v">${fmt(v)}</span></div>`;
}
const meter = (v, max) => `<span class="meter"><i><b style="width:${Math.max(0, Math.min(100, (v / max) * 100))}%"></b></i>${fmt(v, 1)}</span>`;

// ---------- theme & services ----------
function applyTheme() {
  const t = document.documentElement.dataset.theme || (matchMedia("(prefers-color-scheme: light)").matches ? "light" : "dark");
  $("#theme").innerHTML = t === "light" ? I.moon : I.sun;
}
$("#theme").addEventListener("click", () => {
  const cur = document.documentElement.dataset.theme || (matchMedia("(prefers-color-scheme: light)").matches ? "light" : "dark");
  const next = cur === "light" ? "dark" : "light";
  document.documentElement.dataset.theme = next;
  try { localStorage.setItem("scout-theme", next); } catch (e) {}
  applyTheme();
});

async function loadStatus() {
  S.status = await api("/api/status").catch(() => ({}));
  const m = S.status.ollama_models || [];
  $("#services").innerHTML = `<span class="${S.status.jev_ready ? "ok" : "off"}">Jev ${S.status.jev_ready ? "подключён" : "нет ключа"}</span>
    <span class="${S.status.github_ready ? "ok" : "off"}">GitHub ${S.status.github_ready ? "токен есть" : "нет токена"}</span>
    <span class="${m.length ? "ok" : "off"}">Ollama ${m.length ? `· ${m.length} мод.` : "недоступна"}</span>`;
}

// ---------- projects ----------
async function loadProjects(keep) {
  S.projects = await api("/api/projects");
  const want = decodeURIComponent(location.hash.slice(1));
  S.slug = keep && S.projects.find((p) => p.slug === S.slug) ? S.slug : S.projects.find((p) => p.slug === want)?.slug || S.projects[0]?.slug || null;
  renderSidebar();
  if (!S.slug) return renderWelcome();
  await loadAll();
}
function renderSidebar() {
  $("#projects").innerHTML = S.projects.map((p) => {
    const owner = p.repo.split("/")[0];
    const live = S.job?.project === p.slug ? '<span class="live"></span>' : "";
    return `<div class="proj ${p.slug === S.slug ? "on" : ""}" data-slug="${p.slug}">
      <img src="https://github.com/${esc(owner)}.png?size=64" alt="" loading="lazy">
      <div><div class="n">${esc(p.name)} ${live}</div><div class="s"><span>${fmt(p.prs)} PR</span>${p.take ? `<b>${p.take} берём</b>` : ""}</div></div></div>`;
  }).join("");
}
function renderWelcome() {
  $(".main").innerHTML = `<div class="welcome"><img src="/static/logo.svg" alt=""><h1>Какие PR стоит взять?</h1>
    <p>PR Scout собирает все открытые pull request репозитория, дописывает пустые описания локальной моделью и за пару минут раскладывает их через Jev: что берём, что рассмотреть, что пропустить — с причинами.</p>
    <p><button class="btn primary" onclick="openAdd()">${I.play} Добавить репозиторий</button></p></div>`;
}

async function loadAll() {
  location.hash = S.slug;
  [S.summary, S.prs, S.criteria] = await Promise.all([api(P("/summary")), api(P("/prs")), api(P("/criteria"))]);
  S.job = S.summary.job.running ? S.summary.job : null;
  renderSidebar(); renderHeader(); renderPipeline(); renderKpis(); renderBoard(); renderInsights();
  fillAreaFilter(); renderGrid(); renderCriteria(); renderCost(); renderSettings(); renderRunHero();
}

// ---------- header & pipeline ----------
function renderHeader() {
  const c = S.summary.config, owner = c.repo.split("/")[0];
  $("#phead").innerHTML = `<img class="avatar" src="https://github.com/${esc(owner)}.png?size=104" alt="">
    <div class="grow"><h1>${esc(c.name)}</h1>
      <div class="repo"><a href="https://github.com/${esc(c.repo)}" target="_blank" class="mono">${esc(c.repo)} ↗</a>
        <span>·</span><a href="https://github.com/${esc(c.repo)}/pulls" target="_blank">${fmt(S.summary.total)} открытых PR${c.community_only ? " сообщества" : ""}</a></div>
      ${c.profile ? `<div class="profile" title="${esc(c.profile)}">${esc(c.profile)}</div>` : ""}</div>
    <div class="run-actions">
      <button class="btn primary" id="btn-full">${I.play} Полный прогон</button>
      <button class="btn" id="btn-menu" aria-label="Отдельные шаги">${I.down}</button>
      <div class="menu" id="menu">
        ${STEPS.map((s, i) => `<button data-job="${s.key}"><span class="mono muted">${i + 1}</span><span>${s.t}<small>${s.by}</small></span></button>`).join("")}
      </div></div>`;
  $("#btn-full").onclick = () => startJob("full");
  $("#btn-menu").onclick = (e) => { e.stopPropagation(); $("#menu").classList.toggle("open"); };
  $$("#menu [data-job]").forEach((b) => (b.onclick = () => { $("#menu").classList.remove("open"); startJob(b.dataset.job); }));
  syncButtons();
}
function lastRun(stage) { return [...(S.summary?.runs || [])].reverse().find((r) => r.stage === stage); }
function renderPipeline(live) {
  const running = S.job?.project === S.slug ? S.job.running : null;
  $("#pipeline").innerHTML = STEPS.map((s, i) => {
    const r = lastRun(s.key), active = running === s.key;
    let meta = r ? `${fmt(r.items)} · ${secs(r.seconds)} · ${ago(r.started)}` : "ещё не запускался";
    if (!r && s.key === "fetch" && S.prs?.length) meta = `${fmt(S.prs.length)} PR · импортировано`;
    const described = !r && s.key === "describe" ? (S.prs || []).filter((x) => x.ai_description).length : 0;
    if (described) meta = `${fmt(described)} описаний`;
    if (s.key === "describe" && r) meta = `${fmt(r.items)} описаний · ${secs(r.seconds)} · ${ago(r.started)}`;
    if ((s.key === "stage1" || s.key === "stage2") && r) meta += ` · ${money(r.cost_usd)}`;
    if (active && live) meta = `${fmt(live.done)} / ${fmt(live.total)}${live.seconds ? ` · ${secs(live.seconds)}` : ""}`;
    const pct = active && live?.total ? (live.done / live.total) * 100 : 0;
    return `<div class="step ${active ? "active" : r ? "done" : ""}"><span class="idx">0${i + 1}</span>
      <div class="top"><div class="ico">${I[s.ico]}</div><div><div class="t">${s.t}</div><div class="by">${s.by}</div></div></div>
      <div class="meta">${active ? '<i class="live-dot"></i>' : ""}${meta}</div><div class="bar" style="width:${pct}%"></div></div>`;
  }).join("");
}

// ---------- overview ----------
function renderKpis() {
  const s = S.summary, rows = S.prs, by = (v) => rows.filter((r) => r.verdict === v).length;
  const jev = s.runs.filter((r) => r.stage === "stage1" || r.stage === "stage2");
  const cost = jev.reduce((a, r) => a + (r.cost_usd || 0), 0), t = jev.reduce((a, r) => a + (r.seconds || 0), 0);
  const k = (l, v, sub, cls = "") => `<div class="kpi ${cls}"><div class="l">${l}</div><div class="v">${v}</div><div class="sub">${sub}</div></div>`;
  $("#kpis").innerHTML = k("Открытых PR", fmt(s.total), `${fmt(s.finalists)} дошли до ревью кода`)
    + k("Берём", fmt(by("take")), "сильные и чистые", "take") + k("Рассмотреть", fmt(by("consider")), `есть оговорки · ${fmt(by("skip"))} пропускаем`, "consider")
    + k("Jev обошёлся в", money(cost), `за ${secs(t)} работы`, "accent");
  $("#count-all").textContent = fmt(s.classified);
}
function reasonsHtml(r, limit = 3) {
  if (!r.reasons) return "";
  const items = [...(r.reasons.skip || []).map((x) => ["no", x]), ...(r.reasons.take || []).map((x) => ["pro", x]), ...(r.reasons.consider || []).map((x) => ["con", x])];
  return `<div class="why">${items.slice(0, limit).map(([c, x]) => `<span class="${c}">${esc(x)}</span>`).join("")}${items.length > limit ? `<span class="muted">+ ещё ${items.length - limit}</span>` : ""}</div>`;
}
function tags(r) {
  const ci = CI[r.ci_class];
  return `<div class="tags"><span class="chip">${TRACK[r.track] || ""}</span><span class="chip line">${esc(areaLabel(r.area))}</span>${ci ? `<span class="chip ${ci[0]}">${ci[1]}</span>` : ""}${r.ai_description ? '<span class="chip brand" title="Описание дописала локальная модель">✎ ИИ</span>' : ""}</div>`;
}
function renderBoard() {
  const fin = S.prs.filter((r) => r.verdict).sort((a, b) => b.score - a.score);
  const desc = { take: "Серьёзный фикс или сильная фича, ложится на основную ветку, код чистый", consider: "Полезно, но есть оговорки: CI, риск, размер или ценность", skip: "Конфликт, слабый или подозрительный код" };
  if (!fin.length) { $("#board").innerHTML = `<div class="panel" style="grid-column:1/-1"><div class="empty-s">Этап 2 ещё не запускался — вердиктов пока нет. Запустите «Полный прогон».</div></div>`; return; }
  $("#board").innerHTML = ["take", "consider", "skip"].map((v) => {
    const list = fin.filter((r) => r.verdict === v), shown = list.slice(0, v === "skip" ? 12 : 40);
    return `<div class="col ${v}"><div class="col-h"><h2>${VERDICT[v]}</h2><span class="pill">${list.length}</span></div><div class="col-desc">${desc[v]}</div>
      <div class="cards">${shown.map((r) => `<div class="card" data-n="${r.number}"><div><div class="num">#${r.number} · @${esc(r.author)}</div><div class="t">${esc(r.title)}</div>${tags(r)}${reasonsHtml(r, v === "skip" ? 1 : 2)}</div>${ring(r.score)}</div>`).join("")}
      ${list.length > shown.length ? `<div class="more-link">…и ещё ${list.length - shown.length} во вкладке «Все PR»</div>` : ""}</div></div>`;
  }).join("");
}
function hbars(counts, labelFn, max) {
  const entries = Object.entries(counts).sort((a, b) => b[1] - a[1]);
  const m = max || Math.max(1, ...entries.map((e) => e[1]));
  return entries.map(([k, v]) => `<div class="hbar"><span title="${esc(labelFn(k))}">${esc(labelFn(k))}</span><div class="track"><div class="fill" style="width:${(v / m) * 100}%"></div></div><span class="n">${fmt(v)}</span></div>`).join("");
}
function donut(counts) {
  const entries = Object.entries(counts).sort((a, b) => b[1] - a[1]), total = entries.reduce((a, e) => a + e[1], 0) || 1;
  let acc = 0;
  const r = 44, c = 2 * Math.PI * r;
  const arcs = entries.map(([k, v], i) => { const len = (v / total) * c, seg = `<circle cx="60" cy="60" r="${r}" fill="none" stroke="${KIND_COLORS[i % 9]}" stroke-width="16" stroke-dasharray="${Math.max(0, len - 2)} ${c}" stroke-dashoffset="${-acc}"/>`; acc += len; return seg; }).join("");
  return `<div class="donut-wrap"><svg width="120" height="120" viewBox="0 0 120 120" style="transform:rotate(-90deg)">${arcs}</svg>
    <div class="legend">${entries.map(([k, v], i) => `<span><i style="background:${KIND_COLORS[i % 9]}"></i>${esc(kindLabel(k))} · ${fmt(v)}</span>`).join("")}</div></div>`;
}
function hist(values, bins = 20) {
  const h = new Array(bins).fill(0);
  values.forEach((v) => h[Math.min(bins - 1, Math.max(0, Math.floor((v / 100) * bins)))]++);
  const m = Math.max(1, ...h);
  return h.map((c, i) => `<div class="b" style="height:${(c / m) * 100}%" title="${i * 5}–${i * 5 + 5}: ${c} PR">${i % 4 === 0 ? `<em>${i * 5}</em>` : ""}</div>`).join("");
}
function renderInsights() {
  const rows = S.prs.filter((r) => r.classified);
  const count = (key) => rows.reduce((a, r) => ((a[r[key]] = (a[r[key]] || 0) + 1), a), {});
  $("#insights").innerHTML = `<div class="panel"><div class="panel-h"><h3>По частям системы</h3><span class="muted">${fmt(rows.length)} PR</span></div>${hbars(count("area"), areaLabel)}</div>
    <div class="panel"><div class="panel-h"><h3>По типу изменения</h3></div>${donut(count("kind"))}</div>
    <div class="panel"><div class="panel-h"><h3>Распределение балла</h3><span class="muted">0–100</span></div><div class="hist">${hist(rows.map((r) => r.score))}</div></div>`;
}

// ---------- all PRs ----------
function fillAreaFilter() {
  $("#f-area").innerHTML = `<option value="">Все части системы</option>` + Object.entries(S.criteria.areas || {}).map(([k, v]) => `<option value="${k}">${esc(v)}</option>`).join("");
}
function filtered() {
  const q = $("#f-search").value.trim().toLowerCase(), area = $("#f-area").value, ver = $("#f-verdict").value;
  return S.prs.filter((r) => r.classified
    && (!q || String(r.number).includes(q) || r.title.toLowerCase().includes(q) || r.author.toLowerCase().includes(q))
    && (!S.track || r.track === S.track) && (!area || r.area === area)
    && (!ver || (ver === "finalist" ? r.finalist : ver === "included" ? r.included : r.verdict === ver))
    && (!$("#f-rel").checked || r.relevance >= 2.5) && (!$("#f-dup").checked || !r.duplicate_of));
}
function renderGrid() {
  const { key: k, dir: d } = S.sort;
  const rows = filtered().sort((a, b) => (a[k] > b[k] ? 1 : a[k] < b[k] ? -1 : 0) * d);
  $$(".grid th").forEach((th) => th.classList.toggle("sorted", th.dataset.sort === k));
  $("#grid-body").innerHTML = rows.slice(0, S.shown).map((r) => `<tr data-n="${r.number}">
    <td class="n muted mono">${r.rank ?? ""}</td>
    <td><div class="ttl">${esc(r.title)}</div><div class="sub"><span class="mono">#${r.number}</span><span>@${esc(r.author)}</span>
      ${r.included ? '<span class="chip ink">уже взят</span>' : ""}${r.duplicate_of ? `<span class="chip line">дубль #${r.duplicate_of}</span>` : ""}${r.ai_description ? '<span class="chip brand">✎ ИИ</span>' : ""}</div></td>
    <td><span class="chip">${esc(kindLabel(r.kind))}</span></td><td class="muted">${esc(areaLabel(r.area))}</td>
    <td>${meter(r.relevance, 3)}</td><td>${r.track === "fix" ? meter(r.harm, 1) : '<span class="muted">—</span>'}</td><td>${r.track === "feature" ? meter(r.feature_value, 4) : '<span class="muted">—</span>'}</td>
    <td class="n score">${fmt(r.score, 1)}</td><td>${r.verdict ? `<span class="chip ${r.verdict}">${VERDICT[r.verdict]}</span>` : ""}</td></tr>`).join("")
    || `<tr><td colspan="9"><div class="empty-s">Ничего не нашлось</div></td></tr>`;
  $("#grid-count").textContent = `${fmt(Math.min(S.shown, rows.length))} из ${fmt(rows.length)}`;
  $("#btn-more").style.display = rows.length > S.shown ? "" : "none";
}

// ---------- drawer ----------
function probRows(probs, selected, legend) {
  return `<div class="probs">${Object.entries(probs).sort((a, b) => b[1] - a[1]).slice(0, 6).map(([k, p]) =>
    `<div class="prob ${k === String(selected) ? "sel" : ""}"><span>${esc(legend ? legend[k] ?? k : k)}</span><span class="track"><b style="width:${p * 100}%"></b></span><span class="p">${fmt(p * 100)}%</span></div>`).join("")}</div>`;
}
function answerHtml(key, a) {
  const neg = (S.criteria.negative || []).includes(key);
  let v;
  if (a.type === "noul") {
    const col = neg && a.noul >= 0.5 ? "var(--danger)" : a.noul >= 0.34 ? "var(--ink)" : "var(--faint)";
    v = `<div class="noul"><span class="track"><b style="width:${a.noul * 100}%;background:${col}"></b></span><b>${fmt(a.noul, 2)}</b></div>`;
  } else if (a.type === "choice") {
    const lbl = key === "area" ? S.criteria.areas : key === "kind" ? S.criteria.kinds : null;
    v = `<div><b>${esc(lbl ? lbl[a.choice] ?? a.choice : a.choice)}</b> <span class="chip line">уверенность ${fmt(a.confidence * 100)}%</span>${probRows(a.probabilities, a.choice, lbl)}</div>`;
  } else {
    v = `<div><b>${fmt(a.score, 2)}</b> <span class="muted">из ${Object.keys(a.legend).length - 1}</span> <span class="chip line">уверенность ${fmt(a.confidence * 100)}%</span>${probRows(a.probabilities, null, a.legend)}</div>`;
  }
  return `<div class="ans"><div class="k">${esc(S.criteria.labels[key] || key)}</div>${v}</div>`;
}
const BD = { relevance: "релевантность", harm_common: "вред × частота", severity: "серьёзность", general: "полезно всем", tests: "тесты", clear: "описание",
  value: "ценность фичи", new_capability: "новизна", "-risky": "штраф: риск", "-size": "штраф: размер", "-stale": "штраф: давно не обновлялся" };
async function openPr(n) {
  const d = await api(P(`/prs/${n}`)), pr = d.pr, row = d.row || {}, repo = S.summary.config.repo, s2 = d.stage2;
  const bd = row.breakdown || {}, bmax = Math.max(1, ...Object.values(bd).map(Math.abs));
  $("#drawer-body").innerHTML = `
    <div class="d-top">${ring(row.score, 76)}<div style="flex:1;min-width:0">
      <div class="d-meta"><a href="https://github.com/${esc(repo)}/pull/${n}" target="_blank" class="mono">#${n} на GitHub ↗</a><span>@${esc(pr.author)}</span><span>обновлён ${ago(pr.updated)}</span><span>+${fmt(pr.additions)} / −${fmt(pr.deletions)}</span><span>${pr.files.length} файлов</span></div>
      <h1>${esc(pr.title)}</h1>${tags(row)}</div><button class="icon-btn d-close" onclick="closeDrawer()" aria-label="Закрыть">${I.x}</button></div>
    ${row.verdict ? `<div class="verdict-banner ${row.verdict}"><h3>${VERDICT[row.verdict]}</h3>${reasonsHtml(row, 10)}</div>` : row.included ? `<div class="verdict-banner take"><h3>Уже взят в сборку</h3></div>` : ""}
    <div class="d-sec"><h3>Из чего сложился балл · место ${row.rank ?? "—"}</h3>${Object.entries(bd).map(([k, v]) => `<div class="hbar"><span>${esc(BD[k] || k)}</span><div class="track"><div class="fill ${k.startsWith("-") ? "neg" : ""}" style="width:${(Math.abs(v) / bmax) * 100}%"></div></div><span class="n">${k.startsWith("-") ? "−" : "+"}${fmt(Math.abs(v), 1)}</span></div>`).join("")}</div>
    ${s2 ? `<div class="d-sec"><h3>Этап 2 · код и совместимость</h3><div class="tags" style="margin-bottom:6px"><span class="chip ${s2.merge.merge === "clean" ? "ok" : "bad"}">${s2.merge.merge === "clean" ? "ложится на основную ветку" : "конфликт" + (s2.merge.conflicts?.length ? ": " + esc(s2.merge.conflicts.map((f) => f.split("/").pop()).join(", ")) : "")}</span>${(s2.ci?.failing || []).map((f) => `<span class="chip line">${esc(f)}</span>`).join("")}</div>
      ${Object.entries(s2.review.answers).map(([k, a]) => answerHtml(k, a)).join("")}</div>` : ""}
    ${d.stage1 ? `<div class="d-sec"><h3>Этап 1 · ответы Jev</h3>${Object.entries(d.stage1.answers).map(([k, a]) => answerHtml(k, a)).join("")}</div>` : ""}
    <div class="d-sec"><h3>Описание автора</h3><div class="body-text">${esc(pr.body || "Автор ничего не написал.")}</div></div>
    ${pr.ai_description ? `<div class="d-sec"><h3>Описание по дифу · локальная модель</h3><div class="body-text ai">${esc(pr.ai_description)}</div></div>` : ""}
    <div class="d-sec"><h3>Файлы</h3><div class="files mono">${pr.files.map(esc).join("<br>")}</div></div>`;
  $("#drawer").classList.add("open"); $("#scrim").classList.add("open"); $("#drawer").scrollTop = 0;
}
function closeDrawer() { $("#drawer").classList.remove("open"); $("#scrim").classList.remove("open"); }
window.closeDrawer = closeDrawer;

// ---------- criteria ----------
function renderCriteria() {
  const c = S.criteria, L = c.labels;
  const q = (key, x) => {
    const ins = typeof x.instructions === "string" ? x.instructions : x.instructions.question;
    const crit = Array.isArray(x.criteria) ? `<ol start="0">${x.criteria.map((y) => `<li>${esc(y)}</li>`).join("")}</ol>`
      : x.criteria ? `<ul>${Object.entries(x.criteria).slice(0, 16).map(([k, v]) => `<li><span class="mono">${esc(k)}</span> — ${esc(v)}</li>`).join("")}</ul>` : "";
    return `<div class="q"><div class="h"><span>${esc(L[key] || key)}</span><span class="chip mono">${x.type}</span></div><div class="ins">${esc(ins)}</div>${crit}</div>`;
  };
  $("#criteria").innerHTML = `<div class="crit-head">
      <div class="panel"><div class="panel-h"><h3>Как работает Jev</h3></div><div class="muted" style="font-size:13px;line-height:1.6">Jev (TypeSafe) — не чат-модель. Он получает «состояние» (здесь — PR) и набор типизированных вопросов и возвращает по каждому вероятности:
        <b>Choice</b> — выбор варианта, <b>Score</b> — оценка по шкале, <b>Noul</b> — вероятность «да». Все баллы и вердикты собираются из этих ответов обычным кодом, поэтому правила прозрачны и их легко поменять.</div></div>
      <div class="panel"><div class="panel-h"><h3>Относительно чего оценивается релевантность</h3></div><div style="font-size:13px;color:var(--text-2);line-height:1.6">${esc(c.setup || "Описание использования не задано — укажите его в настройках, чтобы Jev оценивал релевантность под вас.")}</div></div></div>
    <div class="sec-title">Этап 1 · все PR — заголовок, описание, файлы</div><div class="q-grid">${Object.entries(c.stage1).map(([k, x]) => q(k, x)).join("")}</div>
    <div class="sec-title">Этап 2 · финалисты — сам код</div><div class="q-grid">${Object.entries(c.stage2).map(([k, x]) => q(k, x)).join("")}</div>
    <div class="sec-title">Балл</div>
    <div class="panel"><div class="formula"><b>Фикс</b> =<span class="term"><b>40</b>·релевантность</span>+<span class="term"><b>25</b>·вред×частота</span>+<span class="term"><b>15</b>·серьёзность</span>+<span class="term"><b>10</b>·полезно всем</span>+<span class="term"><b>5</b>·тесты</span>+<span class="term"><b>5</b>·описание</span></div>
      <div class="formula"><b>Фича</b> =<span class="term"><b>40</b>·релевантность</span>+<span class="term"><b>30</b>·ценность</span>+<span class="term"><b>15</b>·новизна</span>+<span class="term"><b>10</b>·полезно всем</span>+<span class="term"><b>5</b>·тесты</span></div>
      <div class="formula">Штрафы:<span class="term neg">−12·риск</span><span class="term neg">−8 если &gt;1000 строк</span><span class="term neg">−10 если &gt;2500</span><span class="term neg">−5 если не обновлялся 30 дней</span></div>
      <div class="muted" style="font-size:12.5px">Вред = максимум из «ломается основное», «теряются данные», «падает приложение», «дыра в безопасности». Дубли (одно issue или одинаковый заголовок) схлопываются. Топ-${c.finalists} фиксов и фич с релевантностью ≥ 1.5 идут на этап 2.</div></div>
    <div class="sec-title" style="margin-top:22px">Вердикт</div>
    <div class="rules"><div class="rule skip"><h4>Пропускаем</h4>если хоть одно: конфликт с основной веткой и взятыми PR · подозрительный код &gt; 0.3 · продвигает сторонний сервис &gt; 0.5 · качество &lt; 1.5 из 3 · код не совпадает с описанием</div>
      <div class="rule take"><h4>Берём</h4>нет причин пропустить и нет оговорок, и PR сильный: фикс — вред×частота ≥ 0.45 или серьёзность ≥ 3 при частоте ≥ 0.6; фича — ценность ≥ 3 и новизна ≥ 0.5</div>
      <div class="rule consider"><h4>Рассмотреть</h4>остальное. Оговорки: падают тесты CI (боты ревью и флаки e2e не считаются) · риск ≥ 0.5 · посторонние изменения · фича меняет поведение по умолчанию · больше 1500 строк</div></div>`;
}

// ---------- cost ----------
function renderCost() {
  const runs = S.summary.runs, cmp = S.summary.comparison;
  const name = { fetch: "Сбор PR", describe: "Описания · Ollama", stage1: "Этап 1 · Jev", stage2: "Этап 2 · Jev + git", refresh: "Обновление" };
  let bars = `<div class="empty-s">Сравнение появится после первого прогона Jev.</div>`, headline = "";
  if (cmp) {
    const max = Math.max(...cmp.rows.map((r) => r.cost)), min = Math.max(0.001, Math.min(...cmp.rows.map((r) => r.cost)));
    const w = (v) => 4 + (Math.log(v / min) / Math.log(max / min || 10)) * 96;
    const jev = cmp.rows[0].cost, haiku = cmp.rows.find((r) => r.name.includes("Haiku"));
    headline = `<div class="big-number">в ${fmt(haiku.batch / jev)} раз</div><div class="muted">дешевле, чем та же работа на Claude Haiku 4.5 даже через Batch API, и в ${fmt(cmp.rows[1].cost / jev)} раз дешевле Opus 5.5</div>`;
    bars = `<div class="cmp">${cmp.rows.map((r) => `<div class="r ${r.actual ? "actual" : ""}"><span>${esc(r.name)}</span><div class="track"><b style="width:${w(r.cost)}%"></b></div>
      <span class="v">${money(r.cost)}${r.batch ? `<small>batch ${money(r.batch)}</small>` : `<small>${secs(r.seconds)}</small>`}</span></div>`).join("")}</div>
      <div class="muted" style="font-size:12px;margin-top:14px">Логарифмическая шкала. Для Claude — те же ${fmt(cmp.input_tokens)} входных токенов плюс ~${fmt(cmp.output_estimate)} выходных (JSON и короткое обоснование). Цены Anthropic за 1M токенов: Opus 5.5 $4/$20, Sonnet 5 $2/$10, Haiku 4.5 $1/$5; Batch −50%.
      Цена скорости и дешевизны: Jev не пишет обоснований, и описание PR может его увлечь — поэтому решения собираются из атомарных вопросов и проверяются кодом (git, CI) на этапе 2.</div>`;
  }
  $("#cost").innerHTML = `<div class="cost-grid"><div class="panel"><div class="panel-h"><h3>Jev против генеративной модели на тех же данных</h3></div>${headline}${bars}</div>
    <div class="panel"><div class="panel-h"><h3>История прогонов</h3></div><table class="runs">${[...runs].reverse().slice(0, 30).map((r) => `<tr><td>${name[r.stage] || r.stage}<div class="muted" style="font-size:12px">${ago(r.started)} · ${esc(r.model || "")}</div></td>
      <td>${fmt(r.items)} · ${secs(r.seconds)}<br>${r.cost_usd ? money(r.cost_usd) : r.output_tokens ? fmt(r.output_tokens) + " ток. локально" : "бесплатно"}</td></tr>`).join("") || '<tr><td class="muted">Пока пусто</td></tr>'}</table></div></div>`;
}

// ---------- settings ----------
function renderSettings() {
  const c = S.summary.config, o = c.ollama || {};
  $("#settings").innerHTML = `
    <label class="field"><span>Название</span><input name="name" value="${esc(c.name || "")}"></label>
    <label class="field"><span>Как вы используете проект <em>Относительно этого Jev оценивает релевантность. После изменения перезапустите «Классификацию».</em></span><textarea name="profile" rows="6">${esc(c.profile || "")}</textarea></label>
    <label class="switch"><input type="checkbox" name="community_only" ${c.community_only ? "checked" : ""}><i></i>Только PR сообщества — без владельцев, мейнтейнеров и коллабораторов</label>
    <label class="field"><span>Исключить авторов <em>логины через запятую</em></span><input name="exclude_authors" value="${esc((c.exclude_authors || []).join(", "))}"></label>
    <label class="field"><span>Уже взятые PR <em>номера через запятую — их не предлагаем, а финалистов проверяем на мерж поверх них</em></span><input name="stack_prs" value="${esc((c.stack_prs || []).join(", "))}"></label>
    <label class="field"><span>…или ссылка на их список <em>текстовый файл, номер PR в начале строки</em></span><input name="stack_prs_url" value="${esc(c.stack_prs_url || "")}" placeholder="https://raw.githubusercontent.com/…/prs.txt"></label>
    <label class="field"><span>Финалистов на этап 2</span><input name="finalists" type="number" min="10" max="500" value="${c.finalists || 120}"></label>
    <label class="switch"><input type="checkbox" name="ollama_enabled" ${o.enabled ? "checked" : ""}><i></i>Дописывать описания локальной моделью (${esc(o.model || "qwen3.5:9b")}), если текст автора короче ${o.min_body || 200} символов</label>
    <div class="modal-actions"><button class="btn primary">Сохранить</button></div>
    <div class="danger-zone"><span class="muted" style="font-size:13px">Уже взято: ${S.summary.included.length ? S.summary.included.map((n) => "#" + n).join(", ") : "ничего"}</span><button type="button" class="btn danger" id="btn-delete">Удалить проект</button></div>`;
  $("#btn-delete").onclick = async () => {
    if (!confirm(`Удалить ${c.repo} со всеми результатами?`)) return;
    await api(P(""), { method: "DELETE" }); toast(`Проект ${esc(c.repo)} удалён`); location.hash = ""; S.slug = null; loadProjects();
  };
}
$("#settings").addEventListener("submit", async (e) => {
  e.preventDefault();
  const f = new FormData(e.target);
  await post(P("/config"), { name: f.get("name"), profile: f.get("profile"), community_only: !!f.get("community_only"), exclude_authors: f.get("exclude_authors"),
    stack_prs: f.get("stack_prs"), stack_prs_url: f.get("stack_prs_url"), finalists: +f.get("finalists"), ollama: { enabled: !!f.get("ollama_enabled") } }, "PUT");
  toast("Настройки сохранены", "ok"); loadAll();
});

// ---------- run ----------
function renderRunHero(ev) {
  const running = S.job?.project === S.slug ? S.job.running : null;
  const step = STEPS.find((s) => s.key === running);
  const L = S.live || {};
  if (!running && !L.total) return renderRunIdle();
  $("#run-hero").innerHTML = `<div class="row"><div><h2>${running ? `Идёт: ${step ? step.t : "прогон"}` : "Готов к прогону"}</h2>
      <div class="muted" style="font-size:13px">${running ? (L.msg || step?.by || "") : "Полный прогон: сбор PR → описания → классификация Jev → мерж и ревью кода финалистов."}</div></div>
      <div style="margin-left:auto"><button class="btn primary" ${running ? "disabled" : ""} onclick="startJob('full')">${I.play} Полный прогон</button></div></div>
    <div class="stats"><div><b>${fmt(L.done || 0)} / ${fmt(L.total || 0)}</b>готово</div><div><b>${secs(L.seconds || 0)}</b>прошло</div><div><b>${fmt(L.seconds ? (L.done || 0) / L.seconds : 0, 1)}</b>PR в секунду</div><div><b>${fmt(L.tokens || 0)}</b>токенов Jev</div><div><b>${money(L.cost || 0)}</b>стоимость</div></div>
    <div class="progress"><b style="width:${L.total ? (L.done / L.total) * 100 : 0}%"></b></div>`;
}
function renderRunIdle() {
  const runs = S.summary?.runs || [], rows = S.prs.filter((r) => r.classified);
  const jev = [lastRun("stage1"), lastRun("stage2")].filter(Boolean);
  const sum = (k) => jev.reduce((a, r) => a + (r[k] || 0), 0);
  const last = runs[runs.length - 1];
  $("#run-hero").innerHTML = `<div class="row"><div><h2>Готов к прогону</h2>
      <div class="muted" style="font-size:13px">${last ? `Последний прогон ${ago(last.started)}. ` : ""}Полный прогон: сбор PR → описания → классификация Jev → мерж и ревью кода финалистов.</div></div>
      <div style="margin-left:auto"><button class="btn primary" onclick="startJob('full')">${I.play} Полный прогон</button></div></div>
    <div class="stats"><div><b>${fmt(rows.length)}</b>оценено Jev</div><div><b>${secs(sum("seconds"))}</b>время Jev</div><div><b>${fmt(sum("seconds") ? sum("items") / sum("seconds") : 0, 1)}</b>PR в секунду</div><div><b>${fmt(sum("input_tokens"))}</b>токенов Jev</div><div><b>${money(sum("cost_usd"))}</b>стоимость</div></div>`;
  $("#live-hist").innerHTML = rows.length ? hist(rows.map((r) => r.score)) : "";
  const areas = rows.reduce((a, r) => ((a[r.area] = (a[r.area] || 0) + 1), a), {});
  $("#live-area").innerHTML = rows.length ? hbars(areas, areaLabel) : "";
}
function resetLive() { S.live = { done: 0, total: 0, hist: [], areas: {}, n: 0 }; $("#feed").innerHTML = ""; $("#live-hist").innerHTML = ""; $("#live-area").innerHTML = ""; }

async function startJob(name) {
  try {
    await post(P(`/jobs/${name}`));
    resetLive(); switchTab("run");
  } catch (e) { toast(esc(e.message), "err"); }
}
window.startJob = startJob;
function syncButtons() {
  const busy = !!S.job;
  ["#btn-full", "#btn-menu"].forEach((id) => { if ($(id)) $(id).disabled = busy; });
}

function onEvent(ev) {
  if (ev.type === "hello") { S.job = ev.job.running ? ev.job : null; syncButtons(); return; }
  if (ev.type === "start") { S.job = { running: ev.job, project: ev.project }; syncButtons(); renderSidebar(); if (ev.project === S.slug) { resetLive(); renderPipeline(); } return; }
  if (ev.type === "step") {
    S.job = { running: ev.job, project: ev.project };
    if (ev.project === S.slug) {
      S.live = { ...S.live, done: 0, total: 0, seconds: 0 }; renderPipeline(S.live); renderRunHero();
      // the previous step has just finished and written its run: pick it up so it stops saying "not run yet"
      api(P("/summary")).then((sum) => { if (ev.project !== S.slug) return; S.summary = sum; renderPipeline(S.live); }).catch(() => {});
    }
    return;
  }
  if (ev.type === "log") { if (S.live) S.live.msg = ev.message; renderRunHero(); return; }
  if (ev.type === "done" || ev.type === "error") {
    S.job = null; syncButtons(); renderSidebar();
    const p = S.projects.find((x) => x.slug === ev.project)?.name || ev.project;
    toast(ev.type === "done" ? `<b>${esc(p)}</b>: прогон завершён` : `<b>${esc(p)}</b>: ${esc(ev.message)}`, ev.type === "done" ? "ok" : "err");
    loadProjects(true); return;
  }
  if (ev.type !== "progress" || ev.project !== S.slug) return;
  S.live = { ...S.live, ...ev, msg: ev.phase === "merge" ? `#${ev.number}: ${ev.merge === "clean" ? "ложится" : "конфликт"}` : ev.phase === "list" ? `страница ${ev.page}` : S.live?.msg };
  renderPipeline(S.live); renderRunHero();
  const feed = $("#feed");
  if (ev.row) {
    const r = ev.row;
    S.live.hist = [...(S.live.hist || []), r.score]; S.live.areas[r.area] = (S.live.areas[r.area] || 0) + 1;
    feed.insertAdjacentHTML("afterbegin", `<div class="it" data-n="${r.number}"><span class="mono muted">#${r.number}</span><div><div class="t">${esc(r.title)}</div><div class="d"><span class="chip">${TRACK[r.track]}</span> <span class="chip line">${esc(areaLabel(r.area))}</span></div></div>${ring(r.score, 40)}</div>`);
    if (S.live.hist.length < 40 || S.live.hist.length % 8 === 0 || ev.done === ev.total) { $("#live-hist").innerHTML = hist(S.live.hist); $("#live-area").innerHTML = hbars(S.live.areas, areaLabel); }
  } else if (ev.phase === "describe" && ev.preview) {
    feed.insertAdjacentHTML("afterbegin", `<div class="it" data-n="${ev.number}"><span class="mono muted">#${ev.number}</span><div><div class="t">${esc(ev.title || "")}</div><div class="d">✎ ${esc(ev.preview)}…</div></div><span class="chip brand">Ollama</span></div>`);
  } else if (ev.phase === "merge") {
    feed.insertAdjacentHTML("afterbegin", `<div class="it" data-n="${ev.number}"><span class="mono muted">#${ev.number}</span><div><div class="t">${esc(S.prs.find((x) => x.number === ev.number)?.title || "")}</div></div><span class="chip ${ev.merge === "clean" ? "ok" : "bad"}">${ev.merge === "clean" ? "ложится" : "конфликт"}</span></div>`);
  }
  while (feed.children.length > 250) feed.lastChild.remove();
  $("#feed-count").textContent = S.live.total ? `${fmt(S.live.done)} / ${fmt(S.live.total)}` : "";
}
function connectEvents() {
  const es = new EventSource("/api/events");
  es.onmessage = (m) => onEvent(JSON.parse(m.data));
  es.onerror = () => { es.close(); setTimeout(connectEvents, 3000); };
}

// ---------- add project ----------
async function openAdd() {
  $("#modal").classList.add("open");
  await loadStatus();
  const models = S.status.ollama_models?.length ? S.status.ollama_models : ["qwen3.5:9b"];
  $("#ollama-models").innerHTML = models.map((m) => `<option ${m.startsWith("qwen3.5:9b") ? "selected" : ""}>${esc(m)}</option>`).join("");
  $("#add-hint").textContent = S.status.github_ready ? "" : "На сервере не задан GITHUB_TOKEN — без него GitHub не отдаст список PR.";
  setTimeout(() => $("#add-form [name=url]").focus(), 50);
}
window.openAdd = openAdd;
$("#btn-add").addEventListener("click", openAdd);
$("#add-cancel").addEventListener("click", () => $("#modal").classList.remove("open"));
$("#add-form").addEventListener("submit", async (e) => {
  e.preventDefault();
  const f = new FormData(e.target);
  try {
    const r = await post("/api/projects", { url: f.get("url"), profile: f.get("profile"), community_only: !!f.get("community_only"), ollama: !!f.get("ollama"), ollama_model: f.get("ollama_model"), run: true });
    $("#modal").classList.remove("open"); e.target.reset();
    S.slug = r.slug; location.hash = r.slug; await loadProjects(true); resetLive(); switchTab("run");
    toast("Проект добавлен — пошёл полный прогон", "ok");
  } catch (err) { $("#add-hint").textContent = err.message; }
});

// ---------- wiring ----------
function switchTab(t) {
  $$("#tabs button").forEach((b) => b.classList.toggle("active", b.dataset.tab === t));
  $$(".tab").forEach((s) => s.classList.toggle("active", s.id === "tab-" + t));
}
document.addEventListener("click", (e) => {
  const tab = e.target.closest("#tabs button"); if (tab) return switchTab(tab.dataset.tab);
  const proj = e.target.closest(".proj"); if (proj) { S.slug = proj.dataset.slug; S.shown = 120; return loadAll(); }
  if (!e.target.closest(".run-actions")) $("#menu")?.classList.remove("open");
  const seg = e.target.closest("#f-track button");
  if (seg) { $$("#f-track button").forEach((b) => b.classList.toggle("on", b === seg)); S.track = seg.dataset.v; S.shown = 120; return renderGrid(); }
  const th = e.target.closest("th[data-sort]");
  if (th) { const k = th.dataset.sort; S.sort = { key: k, dir: S.sort.key === k ? -S.sort.dir : k === "rank" || k === "title" ? 1 : -1 }; return renderGrid(); }
  const item = e.target.closest("[data-n]"); if (item && !e.target.closest("a")) openPr(+item.dataset.n);
});
$("#scrim").addEventListener("click", closeDrawer);
document.addEventListener("keydown", (e) => {
  if (e.key === "Escape") { closeDrawer(); $("#modal").classList.remove("open"); }
  if (e.key === "/" && !/INPUT|TEXTAREA|SELECT/.test(document.activeElement.tagName)) { e.preventDefault(); switchTab("all"); $("#f-search").focus(); }
});
["#f-search", "#f-area", "#f-verdict", "#f-rel", "#f-dup"].forEach((id) => $(id).addEventListener("input", () => { S.shown = 120; renderGrid(); }));
$("#btn-more").addEventListener("click", () => { S.shown += 120; renderGrid(); });
window.addEventListener("hashchange", () => { const h = decodeURIComponent(location.hash.slice(1)); if (h && h !== S.slug && S.projects.some((p) => p.slug === h)) { S.slug = h; loadAll(); } });

applyTheme();
loadStatus();
$("#pipeline").innerHTML = STEPS.map(() => '<div class="step skeleton" style="height:92px"></div>').join("");
$("#kpis").innerHTML = new Array(6).fill('<div class="kpi skeleton" style="height:96px"></div>').join("");
loadProjects().then(connectEvents).catch((e) => toast("Ошибка загрузки: " + esc(e.message), "err"));

// the tab bar gets a hairline only once it sticks to the top
new IntersectionObserver(([e]) => $("#tabbar").classList.toggle("stuck", !e.isIntersecting)).observe($("#tab-sentinel"));
