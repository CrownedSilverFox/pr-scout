import { ArrowUpRight, ChevronDown, Play } from "lucide-react"
import { Avatar, AvatarFallback, AvatarImage } from "@/components/ui/avatar"
import { Button } from "@/components/ui/button"
import {
  DropdownMenu, DropdownMenuContent, DropdownMenuItem, DropdownMenuLabel, DropdownMenuSeparator, DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu"
import { Tooltip, TooltipContent, TooltipTrigger } from "@/components/ui/tooltip"
import { useStartJob } from "@/hooks/use-project"
import { avatarUrl, fmt } from "@/lib/format"
import { STEPS } from "@/lib/labels"
import type { Summary } from "@/lib/types"
import { useApp } from "@/store/app"

export function ProjectHeader({ slug, summary }: { slug: string; summary: Summary }) {
  const c = summary.config
  const busy = !!useApp((s) => s.job)
  const start = useStartJob(slug)

  return (
    <header className="flex flex-wrap items-start gap-6">
      <Avatar className="size-16 rounded-2xl shadow-float">
        <AvatarImage src={avatarUrl(c.repo, 128)} alt="" />
        <AvatarFallback className="rounded-2xl">{c.name.slice(0, 2)}</AvatarFallback>
      </Avatar>
      <div className="min-w-64 flex-1">
        <h1 className="text-4xl leading-tight font-semibold tracking-[-0.035em]">{c.name}</h1>
        <div className="mt-1.5 flex flex-wrap items-center gap-x-2.5 gap-y-1 text-[13.5px] text-muted-foreground">
          <a href={`https://github.com/${c.repo}`} target="_blank" rel="noreferrer" className="inline-flex items-center gap-0.5 font-mono text-[12.5px] hover:text-foreground">
            {c.repo}<ArrowUpRight className="size-3.5" />
          </a>
          <span>·</span>
          <a href={`https://github.com/${c.repo}/pulls`} target="_blank" rel="noreferrer" className="hover:text-foreground">
            {fmt(summary.total)} открытых PR{c.community_only ? " сообщества" : ""}
          </a>
        </div>
        {c.profile && (
          <Tooltip>
            <TooltipTrigger asChild>
              <p className="mt-2.5 line-clamp-2 max-w-3xl text-[14.5px] text-foreground/70">{c.profile}</p>
            </TooltipTrigger>
            <TooltipContent side="bottom" className="max-w-lg text-[13px] leading-relaxed">{c.profile}</TooltipContent>
          </Tooltip>
        )}
      </div>
      <div className="flex items-center gap-2 pt-2">
        <Button size="lg" className="h-10 rounded-full px-5 text-[14px]" disabled={busy || start.isPending} onClick={() => start.mutate("full")}>
          <Play className="fill-current" /> Полный прогон
        </Button>
        <DropdownMenu>
          <DropdownMenuTrigger asChild>
            <Button variant="outline" size="icon-lg" className="size-10 rounded-full shadow-card" disabled={busy} aria-label="Отдельные шаги">
              <ChevronDown />
            </Button>
          </DropdownMenuTrigger>
          <DropdownMenuContent align="end" className="w-72">
            <DropdownMenuLabel>Запустить один шаг</DropdownMenuLabel>
            <DropdownMenuSeparator />
            {STEPS.map((s) => (
              <DropdownMenuItem key={s.key} className="gap-3 py-2" onSelect={() => start.mutate(s.key)}>
                <s.icon className="text-muted-foreground" />
                <span className="flex flex-col">
                  <span className="font-medium">{s.title}</span>
                  <span className="text-xs text-muted-foreground">{s.by}</span>
                </span>
              </DropdownMenuItem>
            ))}
          </DropdownMenuContent>
        </DropdownMenu>
      </div>
    </header>
  )
}
