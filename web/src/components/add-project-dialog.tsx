import { useEffect } from "react"
import { Controller, useForm } from "react-hook-form"
import { zodResolver } from "@hookform/resolvers/zod"
import { z } from "zod"
import { useMutation, useQuery, useQueryClient } from "@tanstack/react-query"
import { toast } from "sonner"
import { Button } from "@/components/ui/button"
import { Dialog, DialogContent, DialogDescription, DialogFooter, DialogHeader, DialogTitle } from "@/components/ui/dialog"
import { Field, FieldDescription, FieldError, FieldGroup, FieldLabel } from "@/components/ui/field"
import { Input } from "@/components/ui/input"
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from "@/components/ui/select"
import { Switch } from "@/components/ui/switch"
import { Textarea } from "@/components/ui/textarea"
import { api, keys } from "@/lib/api"
import { useApp } from "@/store/app"

const schema = z.object({
  url: z.string().trim().regex(/^(https?:\/\/github\.com\/)?[\w.-]+\/[\w.-]+\/?$/, "Нужна ссылка вида https://github.com/owner/repo"),
  profile: z.string(),
  community_only: z.boolean(),
  ollama: z.boolean(),
  ollama_model: z.string(),
})
type Values = z.infer<typeof schema>

export function AddProjectDialog() {
  const open = useApp((s) => s.addOpen)
  const { setAddOpen, setSlug, setTab, resetLive } = useApp()
  const qc = useQueryClient()
  const status = useQuery({ queryKey: keys.status, queryFn: api.status, enabled: open })
  const models = status.data?.ollama_models.length ? status.data.ollama_models : ["qwen3.5:9b"]
  const form = useForm<Values>({
    resolver: zodResolver(schema),
    defaultValues: { url: "", profile: "", community_only: true, ollama: true, ollama_model: "qwen3.5:9b" },
  })
  useEffect(() => {
    const preferred = models.find((m) => m.startsWith("qwen3.5:9b")) ?? models[0]
    if (!models.includes(form.getValues("ollama_model"))) form.setValue("ollama_model", preferred)
  }, [models, form])

  const create = useMutation({
    mutationFn: (v: Values) => api.createProject({ ...v, run: true }),
    onSuccess: async ({ slug }) => {
      await qc.invalidateQueries({ queryKey: keys.projects })
      setAddOpen(false)
      form.reset()
      setSlug(slug)
      resetLive()
      setTab("run")
      toast.success("Проект добавлен — пошёл полный прогон")
    },
    onError: (e: Error) => form.setError("url", { message: e.message }),
  })

  const err = form.formState.errors
  return (
    <Dialog open={open} onOpenChange={setAddOpen}>
      <DialogContent className="gap-6 rounded-3xl p-9 sm:max-w-xl">
        <DialogHeader>
          <DialogTitle className="text-2xl font-semibold tracking-[-0.035em]">Новый проект</DialogTitle>
          <DialogDescription>Scout соберёт открытые PR, допишет пустые описания локальной моделью и прогонит всё через Jev.</DialogDescription>
        </DialogHeader>
        <form id="add-project" onSubmit={form.handleSubmit((v) => create.mutate(v))}>
          <FieldGroup className="gap-6">
            <Field data-invalid={!!err.url}>
              <FieldLabel htmlFor="url">Репозиторий на GitHub</FieldLabel>
              <Input id="url" autoFocus placeholder="https://github.com/owner/repo" {...form.register("url")} />
              <FieldError errors={[err.url]} />
            </Field>
            <Field>
              <FieldLabel htmlFor="profile">Как вы используете проект</FieldLabel>
              <FieldDescription>Jev оценит, насколько каждый PR важен именно для этого</FieldDescription>
              <Textarea id="profile" rows={4} placeholder="Например: self-hosted в Docker на одном сервере, используем модули X и Y, для нас важнее всего стабильность и безопасность." {...form.register("profile")} />
            </Field>
            <Controller control={form.control} name="community_only" render={({ field }) => (
              <Field orientation="horizontal">
                <Switch id="community_only_new" checked={field.value} onCheckedChange={field.onChange} />
                <FieldLabel htmlFor="community_only_new" className="font-normal">Только PR сообщества — без владельцев, мейнтейнеров и коллабораторов</FieldLabel>
              </Field>
            )} />
            <Controller control={form.control} name="ollama" render={({ field }) => (
              <Field orientation="horizontal">
                <Switch id="ollama_new" checked={field.value} onCheckedChange={field.onChange} />
                <FieldLabel htmlFor="ollama_new" className="font-normal">Дописывать пустые описания локальной моделью</FieldLabel>
              </Field>
            )} />
            <Controller control={form.control} name="ollama_model" render={({ field }) => (
              <Field>
                <FieldLabel>Модель Ollama</FieldLabel>
                <Select value={field.value} onValueChange={field.onChange} disabled={!form.watch("ollama")}>
                  <SelectTrigger className="h-10! w-full rounded-xl bg-card px-3.5"><SelectValue /></SelectTrigger>
                  <SelectContent position="popper" sideOffset={6}>
                    {models.map((m) => <SelectItem key={m} value={m}>{m}</SelectItem>)}
                  </SelectContent>
                </Select>
              </Field>
            )} />
            {status.data && !status.data.github_ready && (
              <p className="rounded-xl bg-consider-soft px-4 py-3 text-[13px] text-consider">На сервере не задан GITHUB_TOKEN — без него GitHub не отдаст список PR.</p>
            )}
          </FieldGroup>
        </form>
        <DialogFooter className="m-0 gap-2 border-0 bg-transparent p-0">
          <Button variant="outline" className="h-10 rounded-full px-5" onClick={() => setAddOpen(false)}>Отмена</Button>
          <Button type="submit" form="add-project" className="h-10 rounded-full px-5" disabled={create.isPending}>Добавить и запустить</Button>
        </DialogFooter>
      </DialogContent>
    </Dialog>
  )
}
