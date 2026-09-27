import { Card } from "@/components/ui/card"
import { Pill } from "@/components/pr-bits"
import { Panel } from "@/components/views/overview"
import type { Criteria, Question } from "@/lib/types"

export function CriteriaView({ criteria }: { criteria: Criteria }) {
  return (
    <div className="flex flex-col gap-14">
      <div className="grid gap-4 lg:grid-cols-2">
        <Panel title="Как работает Jev">
          <p className="text-[14px] leading-relaxed text-muted-foreground">
            Jev (TypeSafe) — не чат-модель. Он получает «состояние» (здесь — PR) и набор типизированных вопросов и возвращает по каждому вероятности:
            <b className="text-foreground"> choice</b> — выбор варианта, <b className="text-foreground">score</b> — оценка по шкале,
            <b className="text-foreground"> noul</b> — вероятность «да». Баллы и вердикты собираются из этих ответов обычным кодом, поэтому правила прозрачны и их легко поменять.
          </p>
        </Panel>
        <Panel title="Относительно чего оценивается релевантность">
          <p className="text-[14px] leading-relaxed text-foreground/80">
            {criteria.setup || "Описание использования не задано — укажите его в настройках, чтобы Jev оценивал релевантность под вас."}
          </p>
        </Panel>
      </div>

      <Section title="Этап 1 · все PR — заголовок, описание, файлы">
        {Object.entries(criteria.stage1).map(([k, q]) => <QuestionCard key={k} label={criteria.labels[k] ?? k} q={q} />)}
      </Section>
      <Section title="Этап 2 · финалисты — сам код">
        {Object.entries(criteria.stage2).map(([k, q]) => <QuestionCard key={k} label={criteria.labels[k] ?? k} q={q} />)}
      </Section>

      <div className="flex flex-col gap-5">
        <h2 className="text-lg font-semibold tracking-[-0.025em]">Балл</h2>
        <Card className="gap-4 rounded-2xl px-7 py-7 shadow-card ring-foreground/[0.07]">
          <Formula name="Фикс" terms={[["40", "релевантность"], ["25", "вред × частота"], ["15", "серьёзность"], ["10", "полезно всем"], ["5", "тесты"], ["5", "описание"]]} />
          <Formula name="Фича" terms={[["40", "релевантность"], ["30", "ценность"], ["15", "новизна"], ["10", "полезно всем"], ["5", "тесты"]]} />
          <div className="flex flex-wrap items-center gap-1.5 text-[13.5px]">
            <span className="mr-1 font-medium">Штрафы</span>
            {["−12 · риск", "−8 если > 1000 строк", "−10 если > 2500", "−5 если не обновлялся 30 дней"].map((t) => <Pill key={t} tone="danger">{t}</Pill>)}
          </div>
          <p className="text-[13px] text-muted-foreground">
            Вред = максимум из «ломается основное», «теряются данные», «падает приложение», «дыра в безопасности». Дубли (одно issue или одинаковый заголовок) схлопываются.
            Топ-{criteria.finalists} фиксов и фич с релевантностью ≥ 1.5 идут на этап 2.
          </p>
        </Card>
      </div>

      <div className="flex flex-col gap-5">
        <h2 className="text-lg font-semibold tracking-[-0.025em]">Вердикт</h2>
        <div className="grid gap-4 lg:grid-cols-3">
          <Rule title="Пропускаем" className="text-danger">если хоть одно: конфликт с основной веткой и взятыми PR · подозрительный код &gt; 0.3 · продвигает сторонний сервис &gt; 0.5 · качество &lt; 1.5 из 3 · код не совпадает с описанием</Rule>
          <Rule title="Берём" className="text-take">нет причин пропустить и нет оговорок, и PR сильный: фикс — вред×частота ≥ 0.45 или серьёзность ≥ 3 при частоте ≥ 0.6; фича — ценность ≥ 3 и новизна ≥ 0.5</Rule>
          <Rule title="Рассмотреть" className="text-consider">остальное. Оговорки: падают тесты CI (боты ревью и флаки e2e не считаются) · риск ≥ 0.5 · посторонние изменения · фича меняет поведение по умолчанию · больше 1500 строк</Rule>
        </div>
      </div>
    </div>
  )
}

function Section({ title, children }: { title: string; children: React.ReactNode }) {
  return (
    <div className="flex flex-col gap-5">
      <h2 className="text-lg font-semibold tracking-[-0.025em]">{title}</h2>
      <div className="grid gap-4 [grid-template-columns:repeat(auto-fill,minmax(min(360px,100%),1fr))]">{children}</div>
    </div>
  )
}

function QuestionCard({ label, q }: { label: string; q: Question }) {
  const text = typeof q.instructions === "string" ? q.instructions : q.instructions.question
  return (
    <Card className="gap-3 rounded-2xl px-6 py-6 shadow-card ring-foreground/[0.07]">
      <div className="flex items-baseline justify-between gap-3">
        <h3 className="text-[15px] font-semibold tracking-[-0.015em]">{label}</h3>
        <Pill tone="outline" className="font-mono">{q.type}</Pill>
      </div>
      <p className="font-mono text-[12.5px] leading-relaxed text-muted-foreground">{text}</p>
      {Array.isArray(q.criteria) && (
        <ol start={0} className="list-decimal pl-5 text-[13.5px] text-foreground/80 marker:text-muted-foreground">
          {q.criteria.map((c) => <li key={c} className="my-0.5">{c}</li>)}
        </ol>
      )}
      {q.criteria && !Array.isArray(q.criteria) && (
        <ul className="flex flex-col gap-1 text-[13.5px] text-foreground/80">
          {Object.entries(q.criteria).slice(0, 16).map(([k, v]) => <li key={k}><span className="font-mono text-[12.5px]">{k}</span> — {v}</li>)}
        </ul>
      )}
    </Card>
  )
}

function Formula({ name, terms }: { name: string; terms: [string, string][] }) {
  return (
    <div className="flex flex-wrap items-center gap-1.5 text-[13.5px]">
      <span className="mr-1 font-medium">{name} =</span>
      {terms.map(([w, t], i) => (
        <span key={t} className="flex items-center gap-1.5">
          {i > 0 && <span className="text-muted-foreground">+</span>}
          <Pill><b className="font-semibold tabular">{w}</b>· {t}</Pill>
        </span>
      ))}
    </div>
  )
}

function Rule({ title, className, children }: { title: string; className: string; children: React.ReactNode }) {
  return (
    <Card className="gap-2 rounded-2xl px-6 py-6 shadow-card ring-foreground/[0.07]">
      <h3 className={`text-base font-semibold tracking-[-0.02em] ${className}`}>{title}</h3>
      <p className="text-[14px] leading-relaxed text-foreground/75">{children}</p>
    </Card>
  )
}
