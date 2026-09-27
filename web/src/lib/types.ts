export type Verdict = "take" | "consider" | "skip"
export type Track = "fix" | "feature" | "other"
export type CiClass = "green" | "flaky_only" | "e2e_only" | "red" | "no_ci"
export type StageKey = "fetch" | "describe" | "stage1" | "stage2"

export interface Project {
  slug: string
  repo: string
  name: string
  prs: number
  classified: number
  take: number
  last_run: string | null
}

export interface Reasons {
  skip: string[]
  consider: string[]
  take: string[]
}

/** One row of the PR list: the fields the server exposes in LIST_FIELDS. */
export interface PrRow {
  number: number
  title: string
  author: string
  updated: string
  additions: number
  deletions: number
  files: number
  included: boolean
  classified: boolean
  kind?: string
  area?: string
  track?: Track
  relevance?: number
  bug_severity?: number
  feature_value?: number
  harm?: number
  common_case?: number
  new_capability?: number
  risky?: number
  score?: number
  rank?: number
  duplicate_of?: number | null
  finalist?: boolean
  verdict?: Verdict
  ci_class?: CiClass
  ai_description: boolean
  reasons?: Reasons
  breakdown?: Record<string, number>
}

export interface Run {
  stage: StageKey | "refresh"
  started: string
  seconds: number
  items: number
  errors?: number
  input_tokens?: number
  output_tokens?: number
  cost_usd?: number
  model?: string
}

export interface Job {
  running: string | null
  project: string | null
  done: number
  total: number
  started: number | null
}

export interface OllamaConfig {
  enabled: boolean
  model: string
  min_body: number
}

export interface ProjectConfig {
  repo: string
  name: string
  profile: string
  community_only: boolean
  exclude_authors: string[]
  stack_prs: number[]
  stack_prs_url: string
  finalists: number
  ollama: OllamaConfig
}

export interface Comparison {
  input_tokens: number
  output_estimate: number
  rows: { name: string; cost: number; batch?: number; seconds?: number; actual?: boolean }[]
}

export interface Summary {
  total: number
  classified: number
  finalists: number
  included: number[]
  runs: Run[]
  job: Job
  config: ProjectConfig
  jev_ready: boolean
  github_ready: boolean
  comparison: Comparison | null
}

export interface Question {
  type: "choice" | "score" | "noul"
  instructions: string | { question: string }
  criteria?: string[] | Record<string, string>
}

export interface Criteria {
  setup: string
  stage1: Record<string, Question>
  stage2: Record<string, Question>
  labels: Record<string, string>
  areas: Record<string, string>
  kinds: Record<string, string>
  finalists: number
  negative: string[]
}

export interface Answer {
  type: "choice" | "score" | "noul"
  choice?: string
  score?: number
  noul?: number
  confidence?: number
  probabilities?: Record<string, number>
  legend?: Record<string, string>
}

export interface PrDetail {
  pr: {
    number: number
    title: string
    author: string
    body: string | null
    ai_description?: string
    updated: string
    additions: number
    deletions: number
    files: string[]
  }
  row: PrRow | null
  stage1: { answers: Record<string, Answer> } | null
  stage2: {
    merge: { merge: "clean" | string; conflicts?: string[] }
    ci?: { failing?: string[] } | null
    review: { answers: Record<string, Answer> }
  } | null
}

export interface Status {
  job: Job
  jev_ready: boolean
  github_ready: boolean
  ollama_models: string[]
}

export type ServerEvent =
  | { type: "hello"; job: Job }
  | { type: "start"; job: string; project: string }
  | { type: "step"; job: string; project: string }
  | { type: "log"; message: string }
  | { type: "done"; job: string; project: string }
  | { type: "error"; job: string; project: string; message: string }
  | ({ type: "progress"; project: string; done: number; total: number; number?: number | null } & ProgressExtra)

export interface ProgressExtra {
  phase?: "list" | "describe" | "stage1" | "git" | "merge" | "review"
  page?: number
  seconds?: number
  tokens?: number
  cost?: number
  preview?: string
  title?: string
  merge?: string
  row?: PrRow
  error?: string
}
