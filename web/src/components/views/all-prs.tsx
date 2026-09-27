import { useEffect, useMemo, useRef, useState } from "react"
import {
  createColumnHelper, createSortedRowModel, rowSortingFeature, sortFns, tableFeatures, useTable, type SortingState,
} from "@tanstack/react-table"
import { ArrowDown, ArrowUp, Search } from "lucide-react"
import { Button } from "@/components/ui/button"
import { Card } from "@/components/ui/card"
import { Input } from "@/components/ui/input"
import { Kbd } from "@/components/ui/kbd"
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from "@/components/ui/select"
import { Switch } from "@/components/ui/switch"
import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow } from "@/components/ui/table"
import { ToggleGroup, ToggleGroupItem } from "@/components/ui/toggle-group"
import { AiMark, Meter, Pill } from "@/components/pr-bits"
import { classifiedRows, labelOf } from "@/hooks/use-project"
import { fmt } from "@/lib/format"
import { VERDICT } from "@/lib/labels"
import type { Criteria, PrRow } from "@/lib/types"
import { cn } from "@/lib/utils"
import { useApp } from "@/store/app"

const PAGE = 120
const features = tableFeatures({ rowSortingFeature, sortedRowModel: createSortedRowModel(), sortFns })
const col = createColumnHelper<typeof features, PrRow>()

type VerdictFilter = "any" | "take" | "consider" | "skip" | "finalist" | "included"

export function AllPrs({ prs, criteria }: { prs: PrRow[]; criteria: Criteria }) {
  const setOpenPr = useApp((s) => s.setOpenPr)
  const searchRef = useRef<HTMLInputElement>(null)
  const [query, setQuery] = useState("")
  const [track, setTrack] = useState("all")
  const [area, setArea] = useState("all")
  const [verdict, setVerdict] = useState<VerdictFilter>("any")
  const [relevantOnly, setRelevantOnly] = useState(false)
  const [hideDupes, setHideDupes] = useState(true)
  const [shown, setShown] = useState(PAGE)
  const [sorting, setSorting] = useState<SortingState>([{ id: "score", desc: true }])

  useEffect(() => {
    const onKey = (e: KeyboardEvent) => {
      if (e.key === "/" && !/INPUT|TEXTAREA/.test((e.target as HTMLElement).tagName)) {
        e.preventDefault()
        searchRef.current?.focus()
      }
    }
    addEventListener("keydown", onKey)
    return () => removeEventListener("keydown", onKey)
  }, [])

  const data = useMemo(() => {
    const q = query.trim().toLowerCase()
    return classifiedRows(prs).filter((r) =>
      (!q || String(r.number).includes(q) || r.title.toLowerCase().includes(q) || r.author.toLowerCase().includes(q))
      && (track === "all" || r.track === track)
      && (area === "all" || r.area === area)
      && (verdict === "any" || (verdict === "finalist" ? r.finalist : verdict === "included" ? r.included : r.verdict === verdict))
      && (!relevantOnly || (r.relevance ?? 0) >= 2.5)
      && (!hideDupes || !r.duplicate_of))
  }, [prs, query, track, area, verdict, relevantOnly, hideDupes])

  const columns = useMemo(() => col.columns([
    col.accessor("rank", { header: "#", cell: (c) => <span className="font-mono text-xs text-muted-foreground">{c.getValue() ?? ""}</span>, sortDescFirst: false }),
    col.accessor("title", {
      header: "Pull request",
      sortDescFirst: false,
      cell: ({ row: { original: r } }) => (
        <div className="min-w-64 whitespace-normal">
          <p className="leading-snug font-medium tracking-[-0.01em]">{r.title}</p>
          <p className="mt-1 flex flex-wrap items-center gap-2 text-xs text-muted-foreground">
            <span className="font-mono">#{r.number}</span><span>@{r.author}</span>
            {r.included && <Pill tone="ink">уже взят</Pill>}
            {r.duplicate_of && <Pill tone="outline">дубль #{r.duplicate_of}</Pill>}
            {r.ai_description && <AiMark />}
          </p>
        </div>
      ),
    }),
    col.accessor("kind", { header: "Тип", cell: (c) => <Pill>{labelOf(criteria.kinds, c.getValue())}</Pill> }),
    col.accessor("area", { header: "Часть", cell: (c) => <span className="text-muted-foreground">{labelOf(criteria.areas, c.getValue())}</span> }),
    col.accessor("relevance", { header: "Релевант.", cell: (c) => <Meter value={c.getValue()} max={3} /> }),
    col.accessor("harm", { header: "Вред", cell: ({ row: { original: r } }) => <Meter value={r.track === "fix" ? r.harm : undefined} max={1} /> }),
    col.accessor("feature_value", { header: "Ценность", cell: ({ row: { original: r } }) => <Meter value={r.track === "feature" ? r.feature_value : undefined} max={4} /> }),
    col.accessor("score", { header: "Балл", cell: (c) => <span className="font-semibold tracking-tight tabular">{fmt(c.getValue(), 1)}</span> }),
    col.accessor("verdict", {
      header: "Вердикт",
      enableSorting: false,
      cell: (c) => { const v = c.getValue(); return v ? <Pill tone={v}>{VERDICT[v]}</Pill> : null },
    }),
  ]), [criteria])

  const table = useTable({ features, columns, data, state: { sorting }, onSortingChange: setSorting })
  const rows = table.getRowModel().rows

  return (
    <div className="flex flex-col gap-6">
      <div className="flex flex-wrap items-center gap-3">
        <div className="relative min-w-64 flex-1">
          <Search className="pointer-events-none absolute top-1/2 left-3.5 size-4 -translate-y-1/2 text-muted-foreground" />
          <Input ref={searchRef} value={query} onChange={(e) => { setQuery(e.target.value); setShown(PAGE) }}
            placeholder="Номер, заголовок или автор" className="h-10 rounded-full bg-card pr-12 pl-10 shadow-card" />
          <Kbd className="absolute top-1/2 right-3 -translate-y-1/2">/</Kbd>
        </div>
        <ToggleGroup type="single" value={track} onValueChange={(v) => v && setTrack(v)} variant="outline" className="h-10 rounded-full bg-card p-1 shadow-card">
          {[["all", "Все"], ["fix", "Фиксы"], ["feature", "Фичи"], ["other", "Прочее"]].map(([v, l]) => (
            <ToggleGroupItem key={v} value={v} className="h-8 rounded-full border-0 px-3.5 data-[state=on]:bg-primary data-[state=on]:text-primary-foreground">{l}</ToggleGroupItem>
          ))}
        </ToggleGroup>
        <Select value={area} onValueChange={setArea}>
          <SelectTrigger className="h-10! min-w-52 rounded-full bg-card px-4 shadow-card"><SelectValue /></SelectTrigger>
          <SelectContent position="popper" sideOffset={6}>
            <SelectItem value="all">Все части системы</SelectItem>
            {Object.entries(criteria.areas).map(([k, v]) => <SelectItem key={k} value={k}>{v}</SelectItem>)}
          </SelectContent>
        </Select>
        <Select value={verdict} onValueChange={(v) => setVerdict(v as VerdictFilter)}>
          <SelectTrigger className="h-10! min-w-44 rounded-full bg-card px-4 shadow-card"><SelectValue /></SelectTrigger>
          <SelectContent position="popper" sideOffset={6}>
            <SelectItem value="any">Любой вердикт</SelectItem>
            <SelectItem value="take">Берём</SelectItem>
            <SelectItem value="consider">Рассмотреть</SelectItem>
            <SelectItem value="skip">Пропускаем</SelectItem>
            <SelectItem value="finalist">Все финалисты</SelectItem>
            <SelectItem value="included">Уже взяты</SelectItem>
          </SelectContent>
        </Select>
        <label className="flex cursor-pointer items-center gap-2.5 text-sm text-foreground/80">
          <Switch checked={relevantOnly} onCheckedChange={setRelevantOnly} /> Только релевантные
        </label>
        <label className="flex cursor-pointer items-center gap-2.5 text-sm text-foreground/80">
          <Switch checked={hideDupes} onCheckedChange={setHideDupes} /> Без дублей
        </label>
      </div>

      <Card className="gap-0 overflow-hidden rounded-2xl p-0 shadow-card ring-foreground/[0.07]">
        <Table>
          <TableHeader>
            {table.getHeaderGroups().map((g) => (
              <TableRow key={g.id} className="hover:bg-transparent">
                {g.headers.map((h) => {
                  const sorted = h.column.getIsSorted()
                  return (
                    <TableHead key={h.id} className={cn("h-12 px-3 text-[12.5px] font-medium text-muted-foreground first:pl-6 last:pr-6", h.column.getCanSort() && "cursor-pointer select-none hover:text-foreground", sorted && "text-foreground")}
                      onClick={h.column.getToggleSortingHandler()}>
                      <span className="inline-flex items-center gap-1">
                        <table.FlexRender header={h} />
                        {sorted === "asc" && <ArrowUp className="size-3.5" />}
                        {sorted === "desc" && <ArrowDown className="size-3.5" />}
                      </span>
                    </TableHead>
                  )
                })}
              </TableRow>
            ))}
          </TableHeader>
          <TableBody>
            {rows.slice(0, shown).map((row) => (
              <TableRow key={row.id} className="cursor-pointer" onClick={() => setOpenPr(row.original.number)}>
                {row.getAllCells().map((cell) => (
                  <TableCell key={cell.id} className="px-3 py-4 first:pl-6 last:pr-6"><table.FlexRender cell={cell} /></TableCell>
                ))}
              </TableRow>
            ))}
            {!rows.length && (
              <TableRow><TableCell colSpan={columns.length} className="py-16 text-center text-muted-foreground">Ничего не нашлось</TableCell></TableRow>
            )}
          </TableBody>
        </Table>
      </Card>
      <div className="flex items-center justify-center gap-4 text-sm text-muted-foreground">
        {rows.length > shown && <Button variant="outline" className="rounded-full" onClick={() => setShown((n) => n + PAGE)}>Показать ещё</Button>}
        <span className="tabular">{fmt(Math.min(shown, rows.length))} из {fmt(rows.length)}</span>
      </div>
    </div>
  )
}
