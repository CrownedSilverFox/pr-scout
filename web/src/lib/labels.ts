import { Cpu, GitMerge, GitPullRequest, Sparkles, type LucideIcon } from "lucide-react"
import type { CiClass, StageKey, Track, Verdict } from "./types"

export const STEPS: { key: StageKey; title: string; by: string; icon: LucideIcon }[] = [
  { key: "fetch", title: "Сбор PR", by: "GitHub GraphQL", icon: GitPullRequest },
  { key: "describe", title: "Описания", by: "локальная модель · Ollama", icon: Cpu },
  { key: "stage1", title: "Классификация", by: "Jev · все PR", icon: Sparkles },
  { key: "stage2", title: "Код и мерж", by: "git + Jev · финалисты", icon: GitMerge },
]

export const VERDICT: Record<Verdict, string> = { take: "Берём", consider: "Рассмотреть", skip: "Пропускаем" }

export const VERDICT_HINT: Record<Verdict, string> = {
  take: "Серьёзный фикс или сильная фича, ложится на основную ветку, код чистый",
  consider: "Полезно, но есть оговорки: CI, риск, размер или ценность",
  skip: "Конфликт, слабый или подозрительный код",
}

export const TRACK: Record<Track, string> = { fix: "Фикс", feature: "Фича", other: "Прочее" }

export const CI: Record<CiClass, { tone: Tone; label: string }> = {
  green: { tone: "take", label: "CI зелёный" },
  flaky_only: { tone: "consider", label: "CI: только флаки" },
  e2e_only: { tone: "consider", label: "CI: только флаки" },
  red: { tone: "danger", label: "CI красный" },
  no_ci: { tone: "outline", label: "без CI" },
}

export type Tone = "take" | "consider" | "skip" | "danger" | "brand" | "ink" | "outline" | "neutral"

/** Score breakdown keys → human labels (negative keys are penalties). */
export const BREAKDOWN: Record<string, string> = {
  relevance: "релевантность",
  harm_common: "вред × частота",
  severity: "серьёзность",
  general: "полезно всем",
  tests: "тесты",
  clear: "описание",
  value: "ценность фичи",
  new_capability: "новизна",
  "-risky": "штраф: риск",
  "-size": "штраф: размер",
  "-stale": "штраф: давно не обновлялся",
}

export const RUN_NAMES: Record<string, string> = {
  fetch: "Сбор PR",
  describe: "Описания · Ollama",
  stage1: "Этап 1 · Jev",
  stage2: "Этап 2 · Jev + git",
  refresh: "Обновление",
}
