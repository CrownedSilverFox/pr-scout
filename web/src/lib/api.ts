import type { Criteria, PrDetail, PrRow, Project, ProjectConfig, Status, Summary } from "./types"

async function request<T>(path: string, init?: RequestInit): Promise<T> {
  const res = await fetch(path, init)
  if (!res.ok) {
    const body = await res.json().catch(() => ({}))
    throw new Error(body.detail || res.statusText)
  }
  return res.json()
}

const send = <T>(path: string, body: unknown, method = "POST") =>
  request<T>(path, { method, headers: { "Content-Type": "application/json" }, body: JSON.stringify(body ?? {}) })

const p = (slug: string, path = "") => `/api/p/${slug}${path}`

export const api = {
  status: () => request<Status>("/api/status"),
  projects: () => request<Project[]>("/api/projects"),
  createProject: (body: { url: string; profile: string; community_only: boolean; ollama: boolean; ollama_model: string; run: boolean }) =>
    send<{ slug: string }>("/api/projects", body),
  deleteProject: (slug: string) => request<{ ok: boolean }>(p(slug), { method: "DELETE" }),
  summary: (slug: string) => request<Summary>(p(slug, "/summary")),
  prs: (slug: string) => request<PrRow[]>(p(slug, "/prs")),
  pr: (slug: string, n: number) => request<PrDetail>(p(slug, `/prs/${n}`)),
  criteria: (slug: string) => request<Criteria>(p(slug, "/criteria")),
  saveConfig: (slug: string, body: Partial<Omit<ProjectConfig, "exclude_authors" | "stack_prs" | "ollama">> & {
    exclude_authors?: string
    stack_prs?: string
    ollama?: Partial<ProjectConfig["ollama"]>
  }) => send<ProjectConfig>(p(slug, "/config"), body, "PUT"),
  startJob: (slug: string, job: string) => send<{ ok: boolean }>(p(slug, `/jobs/${job}`), {}),
}

export const keys = {
  status: ["status"] as const,
  projects: ["projects"] as const,
  summary: (slug: string) => ["summary", slug] as const,
  prs: (slug: string) => ["prs", slug] as const,
  pr: (slug: string, n: number) => ["pr", slug, n] as const,
  criteria: (slug: string) => ["criteria", slug] as const,
}
