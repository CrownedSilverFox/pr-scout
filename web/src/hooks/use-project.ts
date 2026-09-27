import { useMutation, useQuery, useQueryClient } from "@tanstack/react-query"
import { toast } from "sonner"
import { api, keys } from "@/lib/api"
import type { PrRow, Run, StageKey } from "@/lib/types"
import { useApp } from "@/store/app"

export function useProjectData(slug: string) {
  const summary = useQuery({ queryKey: keys.summary(slug), queryFn: () => api.summary(slug) })
  const prs = useQuery({ queryKey: keys.prs(slug), queryFn: () => api.prs(slug) })
  const criteria = useQuery({ queryKey: keys.criteria(slug), queryFn: () => api.criteria(slug) })
  return { summary: summary.data, prs: prs.data, criteria: criteria.data, loading: summary.isPending || prs.isPending || criteria.isPending }
}

export const lastRun = (runs: Run[] | undefined, stage: StageKey) => [...(runs ?? [])].reverse().find((r) => r.stage === stage)

export const classifiedRows = (prs: PrRow[] | undefined) => (prs ?? []).filter((r) => r.classified)

export function useStartJob(slug: string) {
  const qc = useQueryClient()
  const { resetLive, setTab, setJob } = useApp()
  return useMutation({
    mutationFn: (job: "full" | StageKey) => api.startJob(slug, job),
    onSuccess: (_, job) => {
      resetLive()
      setJob({ running: job === "full" ? "fetch" : job, project: slug })
      setTab("run")
      qc.invalidateQueries({ queryKey: keys.summary(slug) })
    },
    onError: (e: Error) => toast.error(e.message),
  })
}

/** Area/kind labels with a readable fallback. */
export const labelOf = (map: Record<string, string> | undefined, key: string | undefined) => (key ? map?.[key] ?? key : "—")
