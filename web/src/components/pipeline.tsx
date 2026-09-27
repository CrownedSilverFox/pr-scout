import { Card } from "@/components/ui/card"
import { lastRun } from "@/hooks/use-project"
import { ago, fmt, money, secs } from "@/lib/format"
import { STEPS } from "@/lib/labels"
import type { PrRow, Summary } from "@/lib/types"
import { cn } from "@/lib/utils"
import { useApp } from "@/store/app"

export function Pipeline({ slug, summary, prs }: { slug: string; summary: Summary; prs: PrRow[] }) {
  const job = useApp((s) => s.job)
  const live = useApp((s) => s.live)
  const running = job?.project === slug ? job.running : null

  return (
    <div className="grid grid-cols-2 gap-3.5 lg:grid-cols-4">
      {STEPS.map((step, i) => {
        const run = lastRun(summary.runs, step.key)
        const active = running === step.key
        let meta = run ? `${fmt(run.items)} · ${secs(run.seconds)} · ${ago(run.started)}` : "ещё не запускался"
        if (!run && step.key === "fetch" && prs.length) meta = `${fmt(prs.length)} PR · импортировано`
        if (!run && step.key === "describe") {
          const described = prs.filter((r) => r.ai_description).length
          if (described) meta = `${fmt(described)} описаний`
        }
        if (run && step.key === "describe") meta = `${fmt(run.items)} описаний · ${secs(run.seconds)} · ${ago(run.started)}`
        if (run && (step.key === "stage1" || step.key === "stage2")) meta += ` · ${money(run.cost_usd)}`
        if (active) meta = live.total ? `${fmt(live.done)} / ${fmt(live.total)}${live.seconds ? ` · ${secs(live.seconds)}` : ""}` : "запускается…"
        const pct = active && live.total ? (live.done / live.total) * 100 : 0

        return (
          <Card key={step.key} className={cn("relative gap-0 overflow-hidden rounded-2xl p-5 shadow-card ring-foreground/[0.07]", active && "ring-2 ring-brand/60")}>
            <span className="absolute top-4 right-4 font-mono text-[11px] text-muted-foreground/60">0{i + 1}</span>
            <div className="flex min-w-0 items-center gap-3">
              <span className={cn("hidden size-8 shrink-0 place-items-center rounded-lg bg-muted sm:grid", active && "bg-brand-soft text-brand", run && !active && "text-take")}>
                <step.icon className={cn("size-4", active && "animate-spin [animation-duration:2.4s]")} />
              </span>
              <span className="min-w-0">
                <span className="block truncate text-[14.5px] font-semibold tracking-tight">{step.title}</span>
                <span className="block truncate text-xs text-muted-foreground">{step.by}</span>
              </span>
            </div>
            <p className="mt-4 flex min-h-5 items-center gap-2 text-[13px] text-foreground/75 tabular">
              {active && <span className="size-1.5 shrink-0 animate-pulse rounded-full bg-brand" />}
              {meta}
            </p>
            <span className="absolute bottom-0 left-0 h-0.5 bg-brand transition-[width] duration-300" style={{ width: `${pct}%` }} />
          </Card>
        )
      })}
    </div>
  )
}
