import { Bar, BarChart, Cell, Pie, PieChart, XAxis } from "recharts"
import { ChartContainer, ChartTooltip, ChartTooltipContent, type ChartConfig } from "@/components/ui/chart"
import { fmt } from "@/lib/format"

/** Score histogram in 5-point bins; bins from 65 up are drawn in ink, the rest muted. */
export function ScoreHistogram({ scores, className }: { scores: number[]; className?: string }) {
  const bins = Array.from({ length: 20 }, (_, i) => ({ bin: i * 5, label: `${i * 5}–${i * 5 + 5}`, count: 0 }))
  for (const s of scores) bins[Math.min(19, Math.max(0, Math.floor(s / 5)))].count++
  const config = { count: { label: "PR" } } satisfies ChartConfig
  return (
    <ChartContainer config={config} className={className ?? "aspect-auto h-40 w-full"}>
      <BarChart data={bins} margin={{ top: 4, right: 0, bottom: 0, left: 0 }} barCategoryGap={2}>
        <XAxis dataKey="bin" tickLine={false} axisLine={false} interval={3} tickMargin={6} fontSize={11} />
        <ChartTooltip cursor={false} content={<ChartTooltipContent hideIndicator labelFormatter={(_, p) => `Балл ${p?.[0]?.payload?.label}`} />} />
        <Bar dataKey="count" radius={[4, 4, 2, 2]} isAnimationActive={false}>
          {bins.map((b) => <Cell key={b.bin} className={b.bin >= 65 ? "fill-foreground" : "fill-subtle"} />)}
        </Bar>
      </BarChart>
    </ChartContainer>
  )
}

const DONUT_COLORS = ["var(--brand)", "var(--chart-1)", "var(--chart-2)", "var(--chart-3)", "var(--chart-4)", "var(--chart-5)"]

export function KindDonut({ counts, label }: { counts: Record<string, number>; label: (k: string) => string }) {
  const data = Object.entries(counts).sort((a, b) => b[1] - a[1]).map(([k, v], i) => ({ key: k, name: label(k), value: v, fill: DONUT_COLORS[Math.min(i, DONUT_COLORS.length - 1)] }))
  const config = Object.fromEntries(data.map((d) => [d.key, { label: d.name, color: d.fill }])) satisfies ChartConfig
  return (
    <div className="flex flex-wrap items-center gap-5">
      <ChartContainer config={config} className="aspect-square h-32 shrink-0">
        <PieChart>
          <ChartTooltip content={<ChartTooltipContent nameKey="key" hideLabel />} />
          <Pie data={data} dataKey="value" nameKey="key" innerRadius={36} outerRadius={60} paddingAngle={2} strokeWidth={0} isAnimationActive={false} />
        </PieChart>
      </ChartContainer>
      <ul className="flex min-w-36 flex-1 flex-col gap-1.5 text-[13px] text-foreground/80">
        {data.map((d) => (
          <li key={d.key} className="flex min-w-0 items-center gap-2">
            <span className="size-2 shrink-0 rounded-full" style={{ background: d.fill }} />
            <span className="truncate">{d.name}</span>
            <span className="ml-auto pl-2 text-muted-foreground tabular">{fmt(d.value)}</span>
          </li>
        ))}
      </ul>
    </div>
  )
}
