import { create } from "zustand"
import type { Job, PrRow, ProgressExtra } from "@/lib/types"

export type Tab = "overview" | "all" | "run" | "criteria" | "cost" | "settings"

export type FeedItem =
  | { kind: "row"; key: string; row: PrRow }
  | { kind: "describe"; key: string; number: number; title: string; preview: string }
  | { kind: "merge"; key: string; number: number; clean: boolean }

export interface Live {
  done: number
  total: number
  seconds: number
  tokens: number
  cost: number
  message: string
  scores: number[]
  areas: Record<string, number>
  feed: FeedItem[]
}

const emptyLive = (): Live => ({ done: 0, total: 0, seconds: 0, tokens: 0, cost: 0, message: "", scores: [], areas: {}, feed: [] })

interface AppState {
  slug: string | null
  tab: Tab
  openPr: number | null
  addOpen: boolean
  job: Pick<Job, "running" | "project"> | null
  live: Live
  setSlug: (slug: string | null) => void
  setTab: (tab: Tab) => void
  setOpenPr: (n: number | null) => void
  setAddOpen: (open: boolean) => void
  setJob: (job: AppState["job"]) => void
  resetLive: () => void
  stepStarted: () => void
  progress: (ev: { done: number; total: number; number?: number | null } & ProgressExtra) => void
  log: (message: string) => void
}

const FEED_LIMIT = 250

export const useApp = create<AppState>((set) => ({
  slug: decodeURIComponent(location.hash.slice(1)) || null,
  tab: "overview",
  openPr: null,
  addOpen: false,
  job: null,
  live: emptyLive(),
  setSlug: (slug) => {
    if (slug) history.replaceState(null, "", `#${slug}`)
    set({ slug, openPr: null, live: emptyLive() })
  },
  setTab: (tab) => set({ tab }),
  setOpenPr: (openPr) => set({ openPr }),
  setAddOpen: (addOpen) => set({ addOpen }),
  setJob: (job) => set({ job }),
  resetLive: () => set({ live: emptyLive() }),
  stepStarted: () => set((s) => ({ live: { ...s.live, done: 0, total: 0, seconds: 0 } })),
  log: (message) => set((s) => ({ live: { ...s.live, message } })),
  progress: (ev) =>
    set((s) => {
      const live: Live = { ...s.live, done: ev.done, total: ev.total }
      if (ev.seconds != null) live.seconds = ev.seconds
      if (ev.tokens != null) live.tokens = ev.tokens
      if (ev.cost != null) live.cost = ev.cost
      if (ev.phase === "list") live.message = `страница ${ev.page}`
      let item: FeedItem | null = null
      if (ev.row) {
        const r = ev.row
        live.scores = [...s.live.scores, r.score ?? 0]
        if (r.area) live.areas = { ...s.live.areas, [r.area]: (s.live.areas[r.area] ?? 0) + 1 }
        item = { kind: "row", key: `row-${r.number}-${ev.done}`, row: r }
      } else if (ev.phase === "describe" && ev.preview && ev.number) {
        item = { kind: "describe", key: `d-${ev.number}`, number: ev.number, title: ev.title ?? "", preview: ev.preview }
      } else if (ev.phase === "merge" && ev.number) {
        const clean = ev.merge === "clean"
        live.message = `#${ev.number}: ${clean ? "ложится" : "конфликт"}`
        item = { kind: "merge", key: `m-${ev.number}`, number: ev.number, clean }
      }
      if (item) live.feed = [item, ...s.live.feed].slice(0, FEED_LIMIT)
      return { live }
    }),
}))
