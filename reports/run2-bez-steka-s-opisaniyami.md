# PR Scout: paperclipai/paperclip

Прогон: 2989 PR с баллами, финалистов 120, Jev потратил $0.3954 (7907624 входных токенов).

- `describe`: 24 шт · 98 с · $0 · ошибок 0
- `stage1`: 2989 шт · 292 с · $0.351 · ошибок 0
- `stage2`: 120 шт · 909 с · $0.0444 · ошибок 0

Последний цикл: 7907624 входных токенов, $0.3954. Все прогоны в истории: 15809553 токенов, $0.7905.

| вариант | цена |
|---|---:|
| Jev (факт, последний цикл) | $0.3954 |
| Claude Opus 5.5 (оценка на тех же токенах) | $31.69 |
| Claude Sonnet 5 (оценка на тех же токенах) | $15.85 |
| Claude Haiku 4.5 (оценка на тех же токенах) | $7.92 |

## Берём (21)

**#12842** [fix(agents): merge runtimeConfig on PATCH instead of replacing the column](https://github.com/paperclipai/paperclip/pull/12842)
`фикс` · CLI и API · автор @vveliev · балл **85.3** · 199+5 строк · — дн. · CI: green
  - + серьёзный баг в обычной работе (вред 0.94, частота 0.72)
  - + прямо про ваше использование (2.75/3)

**#11479** [fix(server): keep comment after-cursor exclusive at microsecond precision](https://github.com/paperclipai/paperclip/pull/11479)
`фикс` · Задачи и согласования · автор @iamasuperuser · балл **84.6** · 147+34 строк · — дн. · CI: green
  - + серьёзный баг в обычной работе (вред 0.84, частота 0.82)
  - + прямо про ваше использование (2.77/3)

**#13936** [fix(server): redact credential-bearing git remotes in run logs](https://github.com/paperclipai/paperclip/pull/13936)
`безопасность` · Запуски и heartbeat · автор @mrkhan91 · балл **84.5** · 606+33 строк · — дн. · CI: green
  - + серьёзный баг в обычной работе (вред 0.93, частота 0.59)
  - + прямо про ваше использование (2.87/3)

**#11311** [fix(adapter-utils): redact env dumps and DSN passwords in transcripts](https://github.com/paperclipai/paperclip/pull/11311)
`безопасность` · Прочее · автор @notandrewblejde · балл **84.0** · 209+5 строк · — дн. · CI: flaky_only
  - + серьёзный баг в обычной работе (вред 0.9, частота 0.62)
  - + прямо про ваше использование (2.78/3)

**#13978** [fix(claude-local): let npm installs run Opus 5.5 with Claude ACP bridge 0.81.2](https://github.com/paperclipai/paperclip/pull/13978)
`фикс` · Claude-адаптер · автор @itsjeremyjohnson · балл **83.6** · 155+84 строк · — дн. · CI: flaky_only
  - + серьёзный баг в обычной работе (вред 0.83, частота 0.65)
  - + прямо про ваше использование (2.96/3)

**#11107** [fix(recovery): stop agent output from bypassing the run-liveness safety gate](https://github.com/paperclipai/paperclip/pull/11107)
`безопасность` · Запуски и heartbeat · автор @trelmitt · балл **83.3** · 96+3 строк · — дн. · CI: flaky_only
  - + серьёзный баг в обычной работе (вред 0.91, частота 0.54)
  - + прямо про ваше использование (2.92/3)

**#11052** [fix(claude-local): classify failures from the run's error surface, not its whole stdout](https://github.com/paperclipai/paperclip/pull/11052)
`фикс` · Claude-адаптер · автор @juancarlosrial76-code · балл **83.0** · 136+1 строк · — дн. · CI: green
  - + серьёзный баг в обычной работе (вред 0.71, частота 0.8)
  - + прямо про ваше использование (2.9/3)

**#13726** [fix(ai-connections): rotate Claude subscription credentials from a file](https://github.com/paperclipai/paperclip/pull/13726)
`фикс` · AI-подключения и доступ · автор @vobornik · балл **82.3** · 153+19 строк · — дн. · CI: green
  - + серьёзный баг в обычной работе (вред 0.83, частота 0.78)
  - + прямо про ваше использование (2.99/3)

**#11462** [fix(security): redact sensitive fields in config-read API responses (extracted from #10284)](https://github.com/paperclipai/paperclip/pull/11462)
`безопасность` · Коннекторы и MCP · автор @JackReis · балл **82.2** · 95+1 строк · — дн. · CI: flaky_only
  - + серьёзный баг в обычной работе (вред 0.85, частота 0.71)
  - + прямо про ваше использование (2.6/3)

**#12870** [fix(adapter-utils): strip DATABASE_URL and BETTER_AUTH_SECRET from inherited agent env](https://github.com/paperclipai/paperclip/pull/12870)
`безопасность` · Другие адаптеры · автор @charlieotis · балл **81.6** · 17+0 строк · — дн. · CI: flaky_only
  - + серьёзный баг в обычной работе (вред 0.93, частота 0.64)
  - + прямо про ваше использование (2.57/3)

**#10735** [fix(issues): re-arm issue monitors on dispatch so a failed run cannot strand the issue](https://github.com/paperclipai/paperclip/pull/10735)
`фикс` · Запуски и heartbeat · автор @juancarlosrial76-code · балл **81.5** · 460+32 строк · — дн. · CI: green
  - + серьёзный баг в обычной работе (вред 0.83, частота 0.58)
  - + прямо про ваше использование (2.86/3)

**#13833** [fix(server): bind run context to the checked-out issue so taskless runs can write](https://github.com/paperclipai/paperclip/pull/13833)
`фикс` · Задачи и согласования · автор @Pdesengrini · балл **81.0** · 848+9 строк · — дн. · CI: green
  - + серьёзный баг в обычной работе (вред 0.88, частота 0.6)
  - + прямо про ваше использование (2.77/3)

**#7432** [fix(issues): resolve identifier to UUID for parentId/descendantOf filters](https://github.com/paperclipai/paperclip/pull/7432)
`фикс` · Задачи и согласования · автор @Sergio-LPA · балл **80.8** · 398+10 строк · — дн. · CI: green
  - + серьёзный баг в обычной работе (вред 0.78, частота 0.77)
  - + прямо про ваше использование (2.55/3)

**#13653** [Deterministic shipped-gate: verify claimed commits before an issue can reach done](https://github.com/paperclipai/paperclip/pull/13653)
`безопасность` · Задачи и согласования · автор @ajinkyabhanudas · балл **80.0** · 558+17 строк · — дн. · CI: green
  - + серьёзный баг в обычной работе (вред 0.79, частота 0.68)
  - + прямо про ваше использование (2.88/3)

**#13769** [fix(heartbeat): re-admit a wake parked by a gate that has gone away](https://github.com/paperclipai/paperclip/pull/13769)
`фикс` · Запуски и heartbeat · автор @MrBlackTongue · балл **79.7** · 341+0 строк · — дн. · CI: green
  - + серьёзный баг в обычной работе (вред 0.92, частота 0.52)
  - + прямо про ваше использование (2.78/3)

**#9219** [fix(claude-local, heartbeat): recover from silent session_lost caused by cwd switches](https://github.com/paperclipai/paperclip/pull/9219)
`фикс` · Запуски и heartbeat · автор @Sergio-LPA · балл **79.0** · 258+2 строк · — дн. · CI: green
  - + серьёзный баг в обычной работе (вред 0.67, частота 0.73)
  - + прямо про ваше использование (2.89/3)

**#3856** [fix(agents): preserve sibling keys of runtimeConfig on partial PATCH](https://github.com/paperclipai/paperclip/pull/3856)
`фикс` · CLI и API · автор @sparkeros · балл **77.8** · 12+0 строк · — дн. · CI: green
  - + серьёзный баг в обычной работе (вред 0.88, частота 0.79)
  - + прямо про ваше использование (2.58/3)

**#5784** [Fix DB backup rotation ENOSPC (per-day daily-tier coalesce + free-space guard)](https://github.com/paperclipai/paperclip/pull/5784)
`фикс` · Деплой и self-host · автор @imvimm · балл **77.3** · 305+25 строк · — дн. · CI: flaky_only
  - + серьёзный баг в обычной работе (вред 0.75, частота 0.6)
  - + прямо про ваше использование (2.55/3)

**#11500** [fix(server): count instead of refuse a run with no recorded source issue](https://github.com/paperclipai/paperclip/pull/11500)
`фикс` · Задачи и согласования · автор @dzianisv · балл **76.9** · 248+8 строк · — дн. · CI: green
  - + серьёзный баг в обычной работе (вред 0.86, частота 0.78)
  - + прямо про ваше использование (2.86/3)

**#4807** [fix(recovery): dispatch in_progress sub-issues with no execution history as fresh assignment (PAP-4766)](https://github.com/paperclipai/paperclip/pull/4807)
`фикс` · Запуски и heartbeat · автор @aimonk2025 · балл **76.7** · 111+1 строк · — дн. · CI: green
  - + серьёзный баг в обычной работе (вред 0.64, частота 0.68)
  - + прямо про ваше использование (2.71/3)

**#11336** [fix(server): share one pluginLifecycleManager between routes and dispatcher](https://github.com/paperclipai/paperclip/pull/11336)
`фикс` · Коннекторы и MCP · автор @c-barlow · балл **76.4** · 173+5 строк · — дн. · CI: green
  - + серьёзный баг в обычной работе (вред 0.57, частота 0.79)
  - + прямо про ваше использование (2.72/3)


## Рассмотреть (22)

**#13622** [fix(claude-local): use the `auth login` subcommand for agent login](https://github.com/paperclipai/paperclip/pull/13622)
`фикс` · Claude-адаптер · автор @croakingtoad · балл **86.0** · 53+1 строк · — дн. · CI: red
  - ! падают тесты CI: ci / verify, ci / Build, ci / Canary Dry Run
  - + серьёзный баг в обычной работе (вред 0.85, частота 0.79)
  - + прямо про ваше использование (2.88/3)

**#6808** [feat(heartbeat): ADR-0044 session lifecycle T1/T2/T3/T4 for claude_local](https://github.com/paperclipai/paperclip/pull/6808)
`фича` · Запуски и heartbeat · автор @yackovleff-solved · балл **83.8** · 680+23 строк · — дн. · CI: green
  - ! фича меняет поведение по умолчанию
  - + сильная фича (ценность 3.02/4, новизна 0.63)
  - + прямо про ваше использование (2.98/3)

**#14039** [fix(claude-local): map thinking effort to the selected model](https://github.com/paperclipai/paperclip/pull/14039)
`фикс` · Claude-адаптер · автор @nctiggy · балл **81.3** · 323+42 строк · — дн. · CI: green
  - ! баг не критичный или редкий
  - + прямо про ваше использование (2.96/3)

**#13802** [fix(server): default and cap the heartbeat-runs list limit](https://github.com/paperclipai/paperclip/pull/13802)
`фикс` · Запуски и heartbeat · автор @hsluiscampingcomfort · балл **80.5** · 89+13 строк · — дн. · CI: red
  - ! падают тесты CI: ci / verify, ci / Verify Paperclip Runner (vitest 1/2)
  - + серьёзный баг в обычной работе (вред 0.87, частота 0.7)

**#13478** [feat(claude-local): retry transient upstream errors with exponential backoff](https://github.com/paperclipai/paperclip/pull/13478)
`фича` · Claude-адаптер · автор @daniel-mariani · балл **80.3** · 300+1 строк · — дн. · CI: red
  - ! фича полезная, но не ключевая
  - ! падают тесты CI: ci / verify, ci / General tests (server (1/5))
  - ! фича меняет поведение по умолчанию
  - + прямо про ваше использование (2.92/3)

**#13148** [fix(claude-local): classify ACP session-limit turn failures as provider quota with the parsed reset time](https://github.com/paperclipai/paperclip/pull/13148)
`фикс` · Claude-адаптер · автор @Sasshigo · балл **80.3** · 139+1 строк · — дн. · CI: red
  - ! падают тесты CI: ci / verify, ci / General tests (server (1/5))
  - + серьёзный баг в обычной работе (вред 0.71, частота 0.8)
  - + прямо про ваше использование (2.77/3)

**#8800** [Add task thread sort order option](https://github.com/paperclipai/paperclip/pull/8800)
`фича` · Задачи и согласования · автор @saphid · балл **80.0** · 512+55 строк · — дн. · CI: green
  - ! фича полезная, но не ключевая
  - + прямо про ваше использование (2.59/3)

**#10862** [Make agent role editable after creation](https://github.com/paperclipai/paperclip/pull/10862)
`фича` · Интерфейс · автор @lucktastic · балл **79.9** · 127+3 строк · — дн. · CI: green
  - ! фича полезная, но не ключевая

**#11466** [fix(server): atomically set checkout run contextSnapshot with issue lock](https://github.com/paperclipai/paperclip/pull/11466)
`фикс` · Задачи и согласования · автор @santhiprakash · балл **79.1** · 281+58 строк · — дн. · CI: red
  - ! баг не критичный или редкий
  - ! падают тесты CI: ci / verify, ci / General tests (server (3/5))
  - + прямо про ваше использование (2.91/3)

**#13447** [fix: preserve OAuth refresh access and contain managed MCP config](https://github.com/paperclipai/paperclip/pull/13447)
`фикс` · Codex-адаптер · автор @joeviezner · балл **78.9** · 303+21 строк · — дн. · CI: green
  - ! баг не критичный или редкий
  - + прямо про ваше использование (2.92/3)

**#13069** [feat(plugins): add per-tool timeouts with structured timeout results](https://github.com/paperclipai/paperclip/pull/13069)
`фича` · Коннекторы и MCP · автор @tejasghalsasi · балл **78.7** · 424+23 строк · — дн. · CI: flaky_only
  - ! фича меняет поведение по умолчанию
  - + сильная фича (ценность 3.06/4, новизна 0.81)

**#14248** [fix(server): keep a policy's other fields when a monitor is stripped](https://github.com/paperclipai/paperclip/pull/14248)
`фикс` · Задачи и согласования · автор @stefanriegel · балл **78.6** · 125+8 строк · — дн. · CI: red
  - ! падают тесты CI: ci / Verify serialized server suites (1/9)
  - + серьёзный баг в обычной работе (вред 0.84, частота 0.63)
  - + прямо про ваше использование (2.5/3)

**#8063** [feat(claude-local): resolve @ file references in agent instructions](https://github.com/paperclipai/paperclip/pull/8063)
`фича` · Claude-адаптер · автор @burnlife001 · балл **78.5** · 150+1 строк · — дн. · CI: red
  - ! падают тесты CI: verify, General tests (server)
  - + сильная фича (ценность 3.22/4, новизна 0.87)
  - + прямо про ваше использование (2.72/3)

**#11980** [feat(approvals): add POST /approvals/:id/cancel for requester withdrawal [INUA-5995]](https://github.com/paperclipai/paperclip/pull/11980)
`фича` · Задачи и согласования · автор @rotem-zecharia · балл **78.4** · 386+1 строк · — дн. · CI: flaky_only
  - ! фича меняет поведение по умолчанию
  - + сильная фича (ценность 3.13/4, новизна 0.9)
  - + прямо про ваше использование (2.52/3)

**#14192** [feat(chat): add a Delete chat action to the agent conversation header](https://github.com/paperclipai/paperclip/pull/14192)
`фича` · Интерфейс · автор @MatrixCODEBreak · балл **78.2** · 293+2 строк · — дн. · CI: flaky_only
  - ! фича полезная, но не ключевая

**#13892** [fix(issues): let the assignee supersede critically-silent run bindings](https://github.com/paperclipai/paperclip/pull/13892)
`фикс` · Запуски и heartbeat · автор @iamasuperuser · балл **78.2** · 788+48 строк · — дн. · CI: green
  - ! баг не критичный или редкий
  - + прямо про ваше использование (2.88/3)

**#13927** [fix(claude-local): fail Opus 5.5 ACP runs early when the bundled Claude Code is too old](https://github.com/paperclipai/paperclip/pull/13927)
`фикс` · Claude-адаптер · автор @kimnamu · балл **78.0** · 164+7 строк · — дн. · CI: red
  - ! падают тесты CI: ci / verify, ci / General tests (chat (1/3))
  - + серьёзный баг в обычной работе (вред 0.67, частота 0.72)
  - + прямо про ваше использование (2.8/3)

**#10871** [feat(dashboard): report token usage where subscription billing zeroes spend](https://github.com/paperclipai/paperclip/pull/10871)
`фича` · Интерфейс · автор @Nissimmiracles · балл **77.7** · 651+38 строк · — дн. · CI: flaky_only
  - ! фича полезная, но не ключевая
  - ! фича меняет поведение по умолчанию

**#4764** [fix: add goal owner editing in goals UI](https://github.com/paperclipai/paperclip/pull/4764)
`фича` · Интерфейс · автор @dumi-bogdan · балл **77.5** · 496+3 строк · — дн. · CI: flaky_only
  - ! фича полезная, но не ключевая
  - ! фича меняет поведение по умолчанию

**#12786** [fix(adapter-utils): redact header-style secrets in command text](https://github.com/paperclipai/paperclip/pull/12786)
`безопасность` · Прочее · автор @superbiche · балл **77.5** · 1925+4 строк · — дн. · CI: green
  - ! большой PR (1929 строк)
  - + серьёзный баг в обычной работе (вред 0.92, частота 0.84)
  - + прямо про ваше использование (2.51/3)

**#13134** [feat(codex-models): read the Codex CLI models cache for ChatGPT-auth installs](https://github.com/paperclipai/paperclip/pull/13134)
`фича` · Codex-адаптер · автор @MindSyncHub · балл **77.0** · 206+1 строк · — дн. · CI: green
  - ! фича полезная, но не ключевая
  - ! фича меняет поведение по умолчанию
  - + прямо про ваше использование (2.52/3)

**#11747** [feat(issues): add staleHours filter to issue list route](https://github.com/paperclipai/paperclip/pull/11747)
`фича` · Задачи и согласования · автор @dzianisv · балл **76.7** · 318+1 строк · — дн. · CI: green
  - ! фича полезная, но не ключевая


## Пропускаем (77)

**#8841** [fix(server): sanitize credential-shaped values before persistence](https://github.com/paperclipai/paperclip/pull/8841)
`безопасность` · Запуски и heartbeat · автор @robertdevore · балл **85.3** · 373+12 строк · — дн. · CI: green
  - ✗ конфликт с основной веткой и взятыми PR: redaction.ts, activity.ts, activity-log.ts
  - + серьёзный баг в обычной работе (вред 0.87, частота 0.86)
  - + прямо про ваше использование (2.94/3)

**#6692** [feat: implement server-side secret value redaction](https://github.com/paperclipai/paperclip/pull/6692)
`безопасность` · Запуски и heartbeat · автор @gorkemhacioglu · балл **84.5** · 307+33 строк · — дн. · CI: flaky_only
  - ✗ конфликт с основной веткой и взятыми PR: redaction.test.ts, heartbeat.ts
  - + серьёзный баг в обычной работе (вред 0.91, частота 0.81)
  - + прямо про ваше использование (2.88/3)

**#12539** [fix(server): redact heartbeat adapter output before persistence](https://github.com/paperclipai/paperclip/pull/12539)
`безопасность` · Запуски и heartbeat · автор @Dfskid · балл **84.2** · 672+50 строк · — дн. · CI: red
  - ✗ конфликт с основной веткой и взятыми PR: heartbeat-process-recovery.test.ts, redaction.test.ts, redaction.ts
  - ! падают тесты CI: ci / verify, ci / General tests (server (4/5)), ci / Build
  - + серьёзный баг в обычной работе (вред 0.82, частота 0.79)
  - + прямо про ваше использование (2.75/3)

**#4294** [Feature/4281 configurable claude local session lifecycle](https://github.com/paperclipai/paperclip/pull/4294)
`фича` · Запуски и heartbeat · автор @thomascolden585-svg · балл **83.9** · 519+11 строк · — дн. · CI: red
  - ✗ конфликт с основной веткой и взятыми PR: heartbeat.ts, Layout.tsx, PropertiesPanel.tsx
  - ✗ код не совпадает с описанием (0.09)
  - ! падают тесты CI: verify
  - + сильная фича (ценность 3.46/4, новизна 0.83)
  - + прямо про ваше использование (2.92/3)

**#9750** [fix(tool-access,tool-gateway): perform MCP initialize handshake for remote HTTP servers, and retry through session churn](https://github.com/paperclipai/paperclip/pull/9750)
`фикс` · Коннекторы и MCP · автор @Quentin-M · балл **83.6** · 521+63 строк · — дн. · CI: flaky_only
  - ✗ конфликт с основной веткой и взятыми PR: mcp-http.test.ts, tool-access-service.test.ts, tool-gateway.test.ts
  - ✗ код не совпадает с описанием (0.44)
  - + серьёзный баг в обычной работе (вред 0.91, частота 0.55)
  - + прямо про ваше использование (2.94/3)

**#4004** [feat(adapter-utils): idle + wall watchdogs for runChildProcess](https://github.com/paperclipai/paperclip/pull/4004)
`фича` · Другие адаптеры · автор @ericnicolaides · балл **83.6** · 489+44 строк · — дн. · CI: green
  - ✗ конфликт с основной веткой и взятыми PR: server-utils.test.ts, server-utils.ts, execute.ts
  - + сильная фича (ценность 3.4/4, новизна 0.78)
  - + прямо про ваше использование (2.99/3)

**#3337** [feat(ui,adapter): add MCP server configuration for claude_local agents](https://github.com/paperclipai/paperclip/pull/3337)
`фича` · Claude-адаптер · автор @gbrancaglione · балл **83.2** · 849+6 строк · — дн. · CI: green
  - ✗ конфликт с основной веткой и взятыми PR: execute.ts, AgentDetail.tsx, vitest.config.ts
  - + сильная фича (ценность 3.14/4, новизна 0.89)
  - + прямо про ваше использование (2.91/3)

**#11387** [feat(pipelines): issue-driven stage gates (autoAdvanceOnIssue) + pipeline-managed disposition exemption](https://github.com/paperclipai/paperclip/pull/11387)
`фича` · Задачи и согласования · автор @adamteale · балл **83.0** · 618+1 строк · — дн. · CI: red
  - ✗ конфликт с основной веткой и взятыми PR: successful-run-handoff.ts
  - ! падают тесты CI: ci / verify, ci / General tests (server (3/5))
  - + сильная фича (ценность 3.3/4, новизна 0.84)
  - + прямо про ваше использование (2.6/3)

**#13950** [feat(budgets): add native calendar_day_utc budget window](https://github.com/paperclipai/paperclip/pull/13950)
`фича` · Задачи и согласования · автор @biokub-agent · балл **82.4** · 297+39 строк · — дн. · CI: flaky_only
  - ✗ код не совпадает с описанием (0.46)
  - + сильная фича (ценность 3.59/4, новизна 0.91)

**#5663** [feat(active-memory): inject always-check memories into agent system prompt on every wake (VOG-5736)](https://github.com/paperclipai/paperclip/pull/5663)
`фича` · Claude-адаптер · автор @vg-jerry · балл **82.4** · 678+1 строк · — дн. · CI: no_ci
  - ✗ конфликт с основной веткой и взятыми PR: execute.ts
  - + сильная фича (ценность 3.44/4, новизна 0.71)
  - + прямо про ваше использование (2.93/3)

**#12031** [fix(issues): arm a default wait monitor when an interaction parks the issue](https://github.com/paperclipai/paperclip/pull/12031)
`фикс` · Задачи и согласования · автор @juancarlosrial76-code · балл **82.3** · 534+1 строк · — дн. · CI: green
  - ✗ конфликт с основной веткой и взятыми PR: issues.ts
  - + серьёзный баг в обычной работе (вред 0.7, частота 0.89)
  - + прямо про ваше использование (2.77/3)

**#12930** [fix(claude-local): keep mcpServerIdentity and remoteExecution in the session codec](https://github.com/paperclipai/paperclip/pull/12930)
`фикс` · Claude-адаптер · автор @qwlong · балл **82.3** · 94+0 строк · — дн. · CI: red
  - ✗ конфликт с основной веткой и взятыми PR: adapter-session-codecs.test.ts
  - ! падают тесты CI: ci / Verify serialized server suites (5/5)
  - + серьёзный баг в обычной работе (вред 0.62, частота 0.86)
  - + прямо про ваше использование (2.98/3)

**#11096** [fix(interactions): accept intuitive ask_user_questions payload shape](https://github.com/paperclipai/paperclip/pull/11096)
`фикс` · Задачи и согласования · автор @sagiw · балл **82.3** · 96+3 строк · — дн. · CI: green
  - ✗ конфликт с основной веткой и взятыми PR: issue.test.ts, issue.ts
  - + серьёзный баг в обычной работе (вред 0.92, частота 0.86)
  - + прямо про ваше использование (2.69/3)

**#5674** [fix: deep-merge runtimeConfig on PATCH instead of full column replace](https://github.com/paperclipai/paperclip/pull/5674)
`фикс` · CLI и API · автор @notandrewblejde · балл **82.2** · 355+16 строк · — дн. · CI: green
  - ✗ конфликт с основной веткой и взятыми PR: agents.ts, queryKeys.ts, Agents.tsx
  - ✗ код не совпадает с описанием (0.12)
  - + серьёзный баг в обычной работе (вред 0.91, частота 0.82)
  - + прямо про ваше использование (2.75/3)

**#3497** [[codex] Add agent model failover chains](https://github.com/paperclipai/paperclip/pull/3497)
`фича` · Запуски и heartbeat · автор @akshitnanda · балл **82.1** · 531+48 строк · — дн. · CI: green
  - ✗ конфликт с основной веткой и взятыми PR: index.ts, build-config.ts, build-config.test.ts
  - + сильная фича (ценность 3.4/4, новизна 0.84)
  - + прямо про ваше использование (2.86/3)

**#7541** [feat(llm): OpenAI-compatible baseUrl + runtime API URL/CLI robustness fixes](https://github.com/paperclipai/paperclip/pull/7541)
`фича` · CLI и API · автор @oups75 · балл **82.0** · 196+35 строк · — дн. · CI: flaky_only
  - ✗ конфликт с основной веткой и взятыми PR: package.json, index.ts, config-schema.test.ts
  - ! фича меняет поведение по умолчанию
  - + сильная фича (ценность 3.32/4, новизна 0.84)
  - + прямо про ваше использование (2.79/3)

**#2779** [  **`security: mitigate cross-agent prompt injection via session handoff content (#2755)`**](https://github.com/paperclipai/paperclip/pull/2779)
`безопасность` · Запуски и heartbeat · автор @utk2602 · балл **81.8** · 408+21 строк · — дн. · CI: green
  - ✗ конфликт с основной веткой и взятыми PR: server-utils.test.ts, execute.ts, execute.ts
  - ✗ код не совпадает с описанием (0.44)
  - + серьёзный баг в обычной работе (вред 0.88, частота 0.71)
  - + прямо про ваше использование (2.97/3)

**#11367** [feat(adapter-utils): opt-in allowlist for agent env inheritance](https://github.com/paperclipai/paperclip/pull/11367)
`безопасность` · Другие адаптеры · автор @marijnp7 · балл **81.7** · 436+25 строк · — дн. · CI: green
  - ✗ конфликт с основной веткой и взятыми PR: execute.ts, test.ts, execute.ts
  - + серьёзный баг в обычной работе (вред 0.88, частота 0.78)
  - + прямо про ваше использование (2.93/3)

**#13995** [fix(sandbox-kubernetes): stop pointing built-in adapter defaults at a never-published :v1 tag](https://github.com/paperclipai/paperclip/pull/13995)
`фикс` · Деплой и self-host · автор @BluePhi09 · балл **81.6** · 269+14 строк · — дн. · CI: green
  - ✗ код не совпадает с описанием (0.19)
  - + серьёзный баг в обычной работе (вред 0.8, частота 0.63)
  - + прямо про ваше использование (2.95/3)

**#13056** [fix(cross-issue-limit): allow heartbeat_timer runs to write to checked-out issues (INUA-6799)](https://github.com/paperclipai/paperclip/pull/13056)
`фикс` · Задачи и согласования · автор @rotem-zecharia · балл **81.6** · 99+6 строк · — дн. · CI: green
  - ✗ конфликт с основной веткой и взятыми PR: heartbeat-issue-liveness-escalation.test.ts
  - ✗ код не совпадает с описанием (0.49)
  - ! рискованная область (0.65)
  - + серьёзный баг в обычной работе (вред 0.9, частота 0.82)
  - + прямо про ваше использование (2.96/3)

**#12649** [fix(server): redact agent profile configuration by default](https://github.com/paperclipai/paperclip/pull/12649)
`безопасность` · CLI и API · автор @samikujakanto · балл **81.6** · 942+51 строк · — дн. · CI: red
  - ✗ конфликт с основной веткой и взятыми PR: low-trust-red-team-routes.test.ts, redaction.test.ts, agents.ts
  - ✗ код не совпадает с описанием (0.22)
  - ! падают тесты CI: ci / Verify serialized server suites (2/5)
  - + серьёзный баг в обычной работе (вред 0.92, частота 0.66)
  - + прямо про ваше использование (2.65/3)

**#11923** [fix(acpx): keep projected secrets off the persisted session env](https://github.com/paperclipai/paperclip/pull/11923)
`безопасность` · Claude-адаптер · автор @alaimster · балл **81.5** · 156+24 строк · — дн. · CI: green
  - ✗ конфликт с основной веткой и взятыми PR: execute.ts, acpx@0.12.0.patch
  - + серьёзный баг в обычной работе (вред 0.93, частота 0.84)
  - + прямо про ваше использование (2.7/3)

**#13138** [fix(server): add durable zombie-session reaper for claude_local runs](https://github.com/paperclipai/paperclip/pull/13138)
`фикс` · Запуски и heartbeat · автор @daniel-mariani · балл **81.4** · 818+5 строк · — дн. · CI: green
  - ✗ конфликт с основной веткой и взятыми PR: native-session-resumption.test.ts
  - + серьёзный баг в обычной работе (вред 0.87, частота 0.54)
  - + прямо про ваше использование (2.95/3)

**#6373** [fix: redact runtime secret values in run logs](https://github.com/paperclipai/paperclip/pull/6373)
`безопасность` · Запуски и heartbeat · автор @jasondbramley · балл **81.2** · 124+7 строк · — дн. · CI: green
  - ✗ конфликт с основной веткой и взятыми PR: command-redaction.test.ts, command-redaction.ts, redaction.test.ts
  - + серьёзный баг в обычной работе (вред 0.9, частота 0.74)
  - + прямо про ваше использование (2.78/3)

**#12002** [fix(approvals): auto-transition in_review issues and wake agents on card rejection](https://github.com/paperclipai/paperclip/pull/12002)
`фикс` · Задачи и согласования · автор @rotem-zecharia · балл **81.1** · 580+3 строк · — дн. · CI: flaky_only
  - ✗ код не совпадает с описанием (0.17)
  - + серьёзный баг в обычной работе (вред 0.81, частота 0.82)
  - + прямо про ваше использование (2.61/3)

**#11558** [fix(adapter-utils): strip server secrets from agent env](https://github.com/paperclipai/paperclip/pull/11558)
`безопасность` · Claude-адаптер · автор @Doom121212 · балл **81.1** · 91+4 строк · — дн. · CI: red
  - ✗ конфликт с основной веткой и взятыми PR: execute.ts, spawn-smoke.test.ts, acpx@0.12.0.patch
  - ! падают тесты CI: verify, General tests (workspaces-b)
  - + серьёзный баг в обычной работе (вред 0.91, частота 0.82)
  - + прямо про ваше использование (2.72/3)

**#9588** [fix: prevent project environment values from leaking through API responses](https://github.com/paperclipai/paperclip/pull/9588)
`безопасность` · Задачи и согласования · автор @cablackmon · балл **81.1** · 578+26 строк · — дн. · CI: green
  - ✗ конфликт с основной веткой и взятыми PR: index.ts, project.ts, issues.ts
  - + серьёзный баг в обычной работе (вред 0.91, частота 0.79)
  - + прямо про ваше использование (2.78/3)

**#3885** [Company run toggle](https://github.com/paperclipai/paperclip/pull/3885)
`фича` · Запуски и heartbeat · автор @Micsi · балл **81.1** · 685+10 строк · — дн. · CI: green
  - ✗ конфликт с основной веткой и взятыми PR: heartbeat-process-recovery.test.ts, companies.ts, heartbeat.ts
  - ! фича меняет поведение по умолчанию
  - + сильная фича (ценность 3.54/4, новизна 0.82)
  - + прямо про ваше использование (2.66/3)

**#13223** [fix(api): reject unknown keys in issue mutation bodies](https://github.com/paperclipai/paperclip/pull/13223)
`фикс` · Задачи и согласования · автор @trixy-the-ai-bot · балл **80.7** · 269+14 строк · — дн. · CI: green
  - ✗ конфликт с основной веткой и взятыми PR: issue.ts
  - + серьёзный баг в обычной работе (вред 0.8, частота 0.67)
  - + прямо про ваше использование (2.65/3)

**#13197** [fix(ui): submit stage decisions with required comments](https://github.com/paperclipai/paperclip/pull/13197)
`фича` · Интерфейс · автор @JamesSparkMojo · балл **80.7** · 288+4 строк · — дн. · CI: flaky_only
  - ✗ конфликт с основной веткой и взятыми PR: IssueProperties.tsx
  - + сильная фича (ценность 3.32/4, новизна 0.91)

**#4597** [fix: bump drizzle-orm to ^0.41.0 to satisfy better-auth peer dep](https://github.com/paperclipai/paperclip/pull/4597)
`фикс` · Прочее · автор @mbradaschia · балл **80.7** · 18+23 строк · — дн. · CI: red
  - ✗ конфликт с основной веткой и взятыми PR: package.json, package.json, pnpm-lock.yaml
  - ! падают тесты CI: policy
  - + серьёзный баг в обычной работе (вред 0.93, частота 0.82)
  - + прямо про ваше использование (2.88/3)

**#8472** [feat(claude-local): --fallback-model so transient 529/overload bumps model instead of failing the run](https://github.com/paperclipai/paperclip/pull/8472)
`фича` · Claude-адаптер · автор @joegalbert-ai · балл **80.4** · 180+0 строк · — дн. · CI: flaky_only
  - ✗ конфликт с основной веткой и взятыми PR: index.ts, execute.ts
  - ! фича меняет поведение по умолчанию
  - + сильная фича (ценность 3.05/4, новизна 0.75)
  - + прямо про ваше использование (2.87/3)

**#2642** [fix: redact Paperclip secrets from logs and Codex artifacts](https://github.com/paperclipai/paperclip/pull/2642)
`безопасность` · Codex-адаптер · автор @halfwitgaslit · балл **79.9** · 376+13 строк · — дн. · CI: green
  - ✗ конфликт с основной веткой и взятыми PR: codex-home.ts, execute.ts, codex-local-execute.test.ts
  - + серьёзный баг в обычной работе (вред 0.88, частота 0.72)
  - + прямо про ваше использование (2.92/3)

**#6042** [feat: auto-inject text attachment content in heartbeat-context + bridge allowlist](https://github.com/paperclipai/paperclip/pull/6042)
`фича` · Задачи и согласования · автор @firepol-ai · балл **79.8** · 310+12 строк · — дн. · CI: green
  - ✗ конфликт с основной веткой и взятыми PR: attachment-types.test.ts, attachment-types.ts, issues.ts
  - ✗ код не совпадает с описанием (0.42)
  - ! фича меняет поведение по умолчанию
  - + сильная фича (ценность 3.4/4, новизна 0.73)
  - + прямо про ваше использование (2.73/3)

**#13117** [fix(issues): read the checkout lock's premise instead of inferring it from status](https://github.com/paperclipai/paperclip/pull/13117)
`фикс` · Задачи и согласования · автор @jayproulx · балл **79.6** · 219+5 строк · — дн. · CI: flaky_only
  - ✗ конфликт с основной веткой и взятыми PR: issues.ts
  - + серьёзный баг в обычной работе (вред 0.86, частота 0.58)
  - + прямо про ваше использование (2.85/3)

**#12581** [fix(server): fail closed on secret-shaped issue comments](https://github.com/paperclipai/paperclip/pull/12581)
`безопасность` · Задачи и согласования · автор @apex-skyner · балл **79.3** · 246+7 строк · — дн. · CI: red
  - ✗ конфликт с основной веткой и взятыми PR: issues-service.test.ts, redaction.test.ts, redaction.ts
  - ! падают тесты CI: ci / verify, ci / General tests (server (3/5)), ci / General tests (server (4/5)), ci / Verify serialized server suites 
  - + серьёзный баг в обычной работе (вред 0.91, частота 0.62)
  - + прямо про ваше использование (2.57/3)

**#13966** [feat(ui): move and delete tasks from context menus](https://github.com/paperclipai/paperclip/pull/13966)
`фича` · Задачи и согласования · автор @luizvb · балл **79.2** · 603+12 строк · — дн. · CI: green
  - ✗ код не совпадает с описанием (0.4)
  - ! фича полезная, но не ключевая
  - ! фича меняет поведение по умолчанию

**#11073** [fix(claude-local): classify an unrefreshable OAuth session as auth required](https://github.com/paperclipai/paperclip/pull/11073)
`фикс` · Claude-адаптер · автор @juancarlosrial76-code · балл **79.1** · 36+1 строк · — дн. · CI: green
  - ✗ конфликт с основной веткой и взятыми PR: parse.test.ts, parse.ts
  - + серьёзный баг в обычной работе (вред 0.9, частота 0.68)
  - + прямо про ваше использование (2.92/3)

**#10104** [fix(server/approvals): wake requester on reject and request-revision](https://github.com/paperclipai/paperclip/pull/10104)
`фикс` · Задачи и согласования · автор @nydamon · балл **79.0** · 264+72 строк · — дн. · CI: flaky_only
  - ✗ конфликт с основной веткой и взятыми PR: approvals.ts
  - + серьёзный баг в обычной работе (вред 0.72, частота 0.87)
  - + прямо про ваше использование (2.9/3)

**#5631** [fix(api): prevent update wiping secret bindings](https://github.com/paperclipai/paperclip/pull/5631)
`фикс` · AI-подключения и доступ · автор @freddiecoleman · балл **79.0** · 68+5 строк · — дн. · CI: green
  - ✗ конфликт с основной веткой и взятыми PR: agents.ts
  - + серьёзный баг в обычной работе (вред 0.93, частота 0.56)
  - + прямо про ваше использование (2.93/3)

**#13630** [fix(ui): present choice questions a stored question set leaves out](https://github.com/paperclipai/paperclip/pull/13630)
`фикс` · Интерфейс · автор @GustavoLarcoDev · балл **78.9** · 253+46 строк · — дн. · CI: green
  - ✗ конфликт с основной веткой и взятыми PR: issue-thread-interactions.test.ts
  - + серьёзный баг в обычной работе (вред 0.86, частота 0.65)
  - + прямо про ваше использование (2.66/3)

**#7757** [fix: handle EPIPE on adapter stdin.write after pipe close](https://github.com/paperclipai/paperclip/pull/7757)
`фикс` · Прочее · автор @exocode · балл **78.9** · 36+1 строк · — дн. · CI: green
  - ✗ конфликт с основной веткой и взятыми PR: server-utils.test.ts
  - + серьёзный баг в обычной работе (вред 0.77, частота 0.65)
  - + прямо про ваше использование (2.66/3)

**#1788** [fix(server): restore issue comment cursor pagination](https://github.com/paperclipai/paperclip/pull/1788)
`фикс` · Задачи и согласования · автор @yoyooyooo · балл **78.9** · 87+9 строк · — дн. · CI: green
  - ✗ конфликт с основной веткой и взятыми PR: issues.ts
  - + серьёзный баг в обычной работе (вред 0.81, частота 0.64)
  - + прямо про ваше использование (2.94/3)

**#8972** [feat(approvals): require a reason or explicit force when rejecting](https://github.com/paperclipai/paperclip/pull/8972)
`фича` · Задачи и согласования · автор @souravsachin · балл **78.8** · 402+10 строк · — дн. · CI: green
  - ✗ конфликт с основной веткой и взятыми PR: Approvals.tsx
  - ! фича меняет поведение по умолчанию
  - + сильная фича (ценность 3.07/4, новизна 0.86)
  - + прямо про ваше использование (2.62/3)

**#11945** [[INUA-6044] fix(approvals): wake linked-issue assignees on card approval](https://github.com/paperclipai/paperclip/pull/11945)
`фикс` · Задачи и согласования · автор @rotem-zecharia · балл **78.7** · 179+0 строк · — дн. · CI: flaky_only
  - ✗ конфликт с основной веткой и взятыми PR: approval-routes-idempotency.test.ts
  - + серьёзный баг в обычной работе (вред 0.8, частота 0.57)
  - + прямо про ваше использование (2.72/3)

**#5262** [Sync: Update from paperclipai/master](https://github.com/paperclipai/paperclip/pull/5262)
`фикс` · Деплой и self-host · автор @deancorserv · балл **78.5** · 457+3 строк · — дн. · CI: flaky_only
  - ✗ конфликт с основной веткой и взятыми PR: docker.yml, heartbeat-workspace-session.test.ts, heartbeat.ts
  - ✗ код не совпадает с описанием (0.28)
  - ! баг не критичный или редкий
  - + прямо про ваше использование (2.96/3)

**#8205** [fix(shared): store multiline text verbatim, stop eating \r/\n escapes (RENA-14562)](https://github.com/paperclipai/paperclip/pull/8205)
`фикс` · Задачи и согласования · автор @rendedennis6-byte · балл **78.4** · 53+25 строк · — дн. · CI: red
  - ✗ конфликт с основной веткой и взятыми PR: issue.test.ts
  - ! падают тесты CI: verify, General tests (server)
  - + серьёзный баг в обычной работе (вред 0.9, частота 0.58)
  - + прямо про ваше использование (2.84/3)

**#6162** [Fix skill mention UUID/slug dispatch resolution](https://github.com/paperclipai/paperclip/pull/6162)
`фикс` · Запуски и heartbeat · автор @ryanclark2 · балл **78.4** · 143+4 строк · — дн. · CI: green
  - ✗ конфликт с основной веткой и взятыми PR: heartbeat-project-env.test.ts, issues-service.test.ts, issues.ts
  - + серьёзный баг в обычной работе (вред 0.88, частота 0.71)
  - + прямо про ваше использование (2.65/3)

**#5833** [feat(harness): runtime orphan reaper + pre-spawn process guard](https://github.com/paperclipai/paperclip/pull/5833)
`фича` · Запуски и heartbeat · автор @ddemid · балл **78.4** · 428+8 строк · — дн. · CI: green
  - ✗ конфликт с основной веткой и взятыми PR: heartbeat-stale-queue-invalidation.test.ts, index.ts, heartbeat.ts
  - ✗ код не совпадает с описанием (0.44)
  - ! фича полезная, но не ключевая
  - ! фича меняет поведение по умолчанию
  - + прямо про ваше использование (2.98/3)

**#2388** [feat(ui): add user management UI to company settings](https://github.com/paperclipai/paperclip/pull/2388)
`фича` · Интерфейс · автор @vbalko-claimate · балл **78.4** · 693+5 строк · — дн. · CI: green
  - ✗ конфликт с основной веткой и взятыми PR: app.ts, access.ts, Layout.tsx
  - ! фича меняет поведение по умолчанию
  - + сильная фича (ценность 3.94/4, новизна 0.91)
  - + прямо про ваше использование (2.72/3)

**#1862** [feat: add raigo governance skill for AI policy enforcement](https://github.com/paperclipai/paperclip/pull/1862)
`фича` · Коннекторы и MCP · автор @musharsec · балл **78.3** · 170+0 строк · — дн. · CI: flaky_only
  - ✗ продвигает сторонний сервис (0.71)
  - + сильная фича (ценность 3.79/4, новизна 0.86)

**#13992** [feat(ui): add project status picker to the project detail page](https://github.com/paperclipai/paperclip/pull/13992)
`фича` · Интерфейс · автор @b3nnb · балл **78.2** · 372+15 строк · — дн. · CI: red
  - ✗ конфликт с основной веткой и взятыми PR: ProjectDetail.test.tsx
  - ! фича полезная, но не ключевая
  - ! падают тесты CI: ci / verify, ci / General tests (chat (1/3)), ci / Verify Paperclip Runner (vitest 1/2)

**#13926** [fix: allow taskless runs to update their assigned issues](https://github.com/paperclipai/paperclip/pull/13926)
`фикс` · Задачи и согласования · автор @wyi184246-creator · балл **78.2** · 415+25 строк · — дн. · CI: green
  - ✗ код не совпадает с описанием (0.39)
  - ! рискованная область (0.51)
  - + серьёзный баг в обычной работе (вред 0.84, частота 0.73)
  - + прямо про ваше использование (2.82/3)

**#7002** [feat(claude-local): load per-agent .env on spawn (JDD-133)](https://github.com/paperclipai/paperclip/pull/7002)
`фича` · Claude-адаптер · автор @gabi-JD · балл **78.2** · 502+12 строк · — дн. · CI: red
  - ✗ конфликт с основной веткой и взятыми PR: package.json, execute.ts, index.ts
  - ! падают тесты CI: verify, policy
  - + сильная фича (ценность 3.01/4, новизна 0.75)
  - + прямо про ваше использование (2.94/3)

**#13052** [feat(audit): add run-recall search over runs and activity](https://github.com/paperclipai/paperclip/pull/13052)
`фича` · Запуски и heartbeat · автор @tejasghalsasi · балл **78.0** · 980+15 строк · — дн. · CI: flaky_only
  - ✗ конфликт с основной веткой и взятыми PR: heartbeats.ts
  - + сильная фича (ценность 3.22/4, новизна 0.88)

**#8447** [feat(inbox): surface pending agent→human asks as "Waiting on you"](https://github.com/paperclipai/paperclip/pull/8447)
`фича` · Интерфейс · автор @Tr1ckyMag1ca1 · балл **78.0** · 567+11 строк · — дн. · CI: red
  - ✗ конфликт с основной веткой и взятыми PR: constants.ts, index.ts, inbox-dismissals.ts
  - ! падают тесты CI: Verify serialized server suites (2/4)
  - ! фича меняет поведение по умолчанию
  - + сильная фича (ценность 3.11/4, новизна 0.84)
  - + прямо про ваше использование (2.61/3)

**#6663** [fix(redaction): redact value-based secret patterns in compactRunLogChunk](https://github.com/paperclipai/paperclip/pull/6663)
`безопасность` · Запуски и heartbeat · автор @PAT-Main · балл **77.9** · 93+1 строк · — дн. · CI: green
  - ✗ конфликт с основной веткой и взятыми PR: heartbeat.ts
  - + серьёзный баг в обычной работе (вред 0.89, частота 0.76)
  - + прямо про ваше использование (2.54/3)

**#10532** [fix(task-watchdogs): stop re-waking valid human-blocked leaves / self-inflicted fingerprint churn (JAC-3989)](https://github.com/paperclipai/paperclip/pull/10532)
`фикс` · Запуски и heartbeat · автор @JackReis · балл **77.5** · 205+712 строк · — дн. · CI: green
  - ✗ код не совпадает с описанием (0.22)
  - ! лишние изменения в дифе
  - + серьёзный баг в обычной работе (вред 0.81, частота 0.7)
  - + прямо про ваше использование (2.62/3)

**#11413** [fix(recovery): retry transient adapter failures on a monitor instead of blocking](https://github.com/paperclipai/paperclip/pull/11413)
`фикс` · Запуски и heartbeat · автор @dzianisv · балл **77.5** · 496+39 строк · — дн. · CI: green
  - ✗ конфликт с основной веткой и взятыми PR: heartbeat.ts, service.ts
  - + серьёзный баг в обычной работе (вред 0.9, частота 0.72)
  - + прямо про ваше использование (2.75/3)

**#4386** [feat(plugin-events): enrich agent.run.* payload with issue context + result](https://github.com/paperclipai/paperclip/pull/4386)
`фича` · Запуски и heartbeat · автор @Bricol1982 · балл **77.5** · 76+24 строк · — дн. · CI: green
  - ✗ конфликт с основной веткой и взятыми PR: heartbeat.ts
  - ! фича меняет поведение по умолчанию
  - + сильная фича (ценность 3.47/4, новизна 0.8)
  - + прямо про ваше использование (2.71/3)

**#13321** [fix(codex): pass MCP bearer tokens through env](https://github.com/paperclipai/paperclip/pull/13321)
`фикс` · Codex-адаптер · автор @iceFusion101 · балл **77.4** · 28+9 строк · — дн. · CI: green
  - ✗ конфликт с основной веткой и взятыми PR: codex-home.test.ts, codex-home.ts
  - + серьёзный баг в обычной работе (вред 0.84, частота 0.54)
  - + прямо про ваше использование (2.74/3)

**#4473** [fix(db): add ON DELETE rules to issue-related foreign keys](https://github.com/paperclipai/paperclip/pull/4473)
`фикс` · Задачи и согласования · автор @alexlomt · балл **77.4** · 191+6 строк · — дн. · CI: green
  - ✗ конфликт с основной веткой и взятыми PR: client.test.ts, _journal.json
  - ! рискованная область (0.57)
  - + серьёзный баг в обычной работе (вред 0.91, частота 0.86)
  - + прямо про ваше использование (2.8/3)

**#10616** [fix(recovery): recognize provider quota exhaustion on the ACP path](https://github.com/paperclipai/paperclip/pull/10616)
`фикс` · Запуски и heartbeat · автор @MrBlackTongue · балл **77.2** · 716+232 строк · — дн. · CI: green
  - ✗ конфликт с основной веткой и взятыми PR: execute.ts, parse.ts, provider-failure-classification.test.ts
  - ! баг не критичный или редкий
  - + прямо про ваше использование (2.91/3)

**#12534** [fix(acpx-engine): materialize Claude runtime skills into project cwd](https://github.com/paperclipai/paperclip/pull/12534)
`фикс` · Claude-адаптер · автор @Danne-J · балл **77.1** · 206+37 строк · — дн. · CI: flaky_only
  - ✗ конфликт с основной веткой и взятыми PR: execute.ts, server-utils.ts
  - + серьёзный баг в обычной работе (вред 0.8, частота 0.61)
  - + прямо про ваше использование (2.78/3)

**#6426** [feat: estimateSubscriptionSpendCents for claude-local (RFC #5066)](https://github.com/paperclipai/paperclip/pull/6426)
`фича` · Claude-адаптер · автор @Jolley71717 · балл **77.1** · 314+5 строк · — дн. · CI: green
  - ✗ конфликт с основной веткой и взятыми PR: index.ts, execute.ts, heartbeat.ts
  - ! фича полезная, но не ключевая
  - + прямо про ваше использование (2.86/3)

**#3917** [Add waiting_on_human_gate state and Human Gate behavior to lead agent prompts](https://github.com/paperclipai/paperclip/pull/3917)
`фича` · Задачи и согласования · автор @zjoh5253 · балл **77.1** · 55+3 строк · — дн. · CI: green
  - ✗ конфликт с основной веткой и взятыми PR: AGENTS.md, StatusIcon.tsx, issue-filters.ts
  - + сильная фича (ценность 3.69/4, новизна 0.71)
  - + прямо про ваше использование (2.66/3)

**#13897** [fix(claude-local): enforce deny-first tools by agent role (SOL-3188 Step 1)](https://github.com/paperclipai/paperclip/pull/13897)
`безопасность` · Claude-адаптер · автор @yackovleff-solved · балл **77.0** · 66+4 строк · — дн. · CI: flaky_only
  - ✗ конфликт с основной веткой и взятыми PR: index.ts, permissions.test.ts, permissions.ts
  - ! рискованная область (0.68)
  - + серьёзный баг в обычной работе (вред 0.93, частота 0.69)
  - + прямо про ваше использование (2.96/3)

**#13467** [fix(claude-local): use --append-system-prompt instead of unsupported -file flag](https://github.com/paperclipai/paperclip/pull/13467)
`фикс` · Claude-адаптер · автор @arnaud-gp · балл **77.0** · 36+37 строк · — дн. · CI: flaky_only
  - ✗ конфликт с основной веткой и взятыми PR: execute.remote.test.ts
  - ! баг не критичный или редкий
  - + прямо про ваше использование (2.76/3)

**#10547** [fix(shared,server): treat error as non-invokable across agent lifecycle](https://github.com/paperclipai/paperclip/pull/10547)
`фикс` · Запуски и heartbeat · автор @santhiprakash · балл **76.9** · 42+8 строк · — дн. · CI: green
  - ✗ конфликт с основной веткой и взятыми PR: issues.ts
  - ✗ код не совпадает с описанием (0.32)
  - ! баг не критичный или редкий
  - + прямо про ваше использование (2.8/3)

**#3481** [fix(server): alias assigneeId to assigneeAgentId in POST /issues](https://github.com/paperclipai/paperclip/pull/3481)
`фикс` · Задачи и согласования · автор @outlawmold · балл **76.9** · 180+17 строк · — дн. · CI: red
  - ✗ конфликт с основной веткой и взятыми PR: package.json, execute.ts, test.ts
  - ✗ код не совпадает с описанием (0.05)
  - ! падают тесты CI: policy
  - + серьёзный баг в обычной работе (вред 0.63, частота 0.87)
  - + прямо про ваше использование (2.85/3)

**#11623** [fix(recovery): stop terminal-run recovery from stranding, flapping, and destroying live monitors](https://github.com/paperclipai/paperclip/pull/11623)
`фикс` · Запуски и heartbeat · автор @dzianisv · балл **76.7** · 593+3 строк · — дн. · CI: flaky_only
  - ✗ конфликт с основной веткой и взятыми PR: service.ts
  - + серьёзный баг в обычной работе (вред 0.86, частота 0.62)
  - + прямо про ваше использование (2.85/3)

**#3910** [fix(issues): slug-mention resolver + UUID validation for @agent wakes](https://github.com/paperclipai/paperclip/pull/3910)
`фикс` · Задачи и согласования · автор @kbecking · балл **76.7** · 677+13 строк · — дн. · CI: green
  - ✗ конфликт с основной веткой и взятыми PR: events.ts, index.ts, types.ts
  - + серьёзный баг в обычной работе (вред 0.6, частота 0.76)
  - + прямо про ваше использование (2.96/3)

**#13812** [feat(apps): add Glasser as a self-serve MCP connection](https://github.com/paperclipai/paperclip/pull/13812)
`фича` · Коннекторы и MCP · автор @glasserai · балл **76.6** · 171+19 строк · — дн. · CI: green
  - ✗ конфликт с основной веткой и взятыми PR: app-definitions.generated.ts, app-definitions.test.ts, ingest-app-definitions.mjs
  - ✗ продвигает сторонний сервис (0.9)
  - + сильная фича (ценность 3.37/4, новизна 0.76)

**#5468** [feat: multi-select issues with batch actions in list view (LAC-459)](https://github.com/paperclipai/paperclip/pull/5468)
`фича` · Задачи и согласования · автор @lacymorrow · балл **76.6** · 844+4 строк · — дн. · CI: green
  - ✗ конфликт с основной веткой и взятыми PR: issues.ts, issues.ts, IssuesList.tsx
  - + сильная фича (ценность 3.42/4, новизна 0.89)

**#11506** [fix: wake requesting agent when approval card is rejected](https://github.com/paperclipai/paperclip/pull/11506)
`фикс` · Задачи и согласования · автор @rotem-zecharia · балл **76.5** · 403+22 строк · — дн. · CI: red
  - ✗ конфликт с основной веткой и взятыми PR: _journal.json, approval.ts, approval-routes-idempotency.test.ts
  - ✗ код не совпадает с описанием (0.11)
  - ! падают тесты CI: Verify serialized server suites (1/5)
  - + серьёзный баг в обычной работе (вред 0.87, частота 0.75)
  - + прямо про ваше использование (2.59/3)

**#12611** [fix(tool-gateway): stop mapping application-level tools/call errors to raw HTTP 404/400 on the named MCP gateway](https://github.com/paperclipai/paperclip/pull/12611)
`фикс` · Коннекторы и MCP · автор @Quentin-M · балл **76.4** · 94+1 строк · — дн. · CI: flaky_only
  - ✗ конфликт с основной веткой и взятыми PR: tool-gateway.ts
  - ! баг не критичный или редкий
  - + прямо про ваше использование (2.85/3)

**#7724** [fix(security): redact transcript artifacts before persistence](https://github.com/paperclipai/paperclip/pull/7724)
`безопасность` · Codex-адаптер · автор @misterbusiness1 · балл **76.4** · 425+4 строк · — дн. · CI: green
  - ✗ конфликт с основной веткой и взятыми PR: execute.ts, run-log-store.ts
  - + серьёзный баг в обычной работе (вред 0.89, частота 0.75)
  - + прямо про ваше использование (2.73/3)


## Не дошли до этапа 2 — только балл этапа 1, вердикта нет (2869)

**#13924** [fix(ai-connections): rotate Claude subscription credentials from a file](https://github.com/paperclipai/paperclip/pull/13924)
`фича` · AI-подключения и доступ · автор @danmoc-88 · балл **79.7** · 153+19 строк · — дн. · CI: —

**#13782** [fix: keep the requesting run alive when an agent hands off its own issue](https://github.com/paperclipai/paperclip/pull/13782)
`фикс` · Задачи и согласования · автор @Waseemilyas · балл **76.3** · 94+1 строк · — дн. · CI: —

**#13060** [feat(runs): add session-log ZIP export for heartbeat runs](https://github.com/paperclipai/paperclip/pull/13060)
`фича` · Запуски и heartbeat · автор @tejasghalsasi · балл **76.3** · 606+0 строк · — дн. · CI: —

**#12287** [fix(codex-local): write http_headers so codex sends the MCP gateway bearer token](https://github.com/paperclipai/paperclip/pull/12287)
`фикс` · Codex-адаптер · автор @zannis · балл **76.3** · 6+2 строк · — дн. · CI: —

**#4003** [fix(adapter-utils): non-blocking onLog in runChildProcess](https://github.com/paperclipai/paperclip/pull/4003)
`фикс` · Другие адаптеры · автор @ericnicolaides · балл **76.3** · 56+8 строк · — дн. · CI: —

**#3823** [fix: include server port in derived auth trusted origins](https://github.com/paperclipai/paperclip/pull/3823)
`фикс` · AI-подключения и доступ · автор @Helmi · балл **76.3** · 147+2 строк · — дн. · CI: —

**#13028** [fix(claude-local): do not treat a background-task notification as a finished turn](https://github.com/paperclipai/paperclip/pull/13028)
`фикс` · Claude-адаптер · автор @MrBlackTongue · балл **76.2** · 85+1 строк · — дн. · CI: —

**#7415** [Enforce heartbeat cooldown on automatic agent wakeups](https://github.com/paperclipai/paperclip/pull/7415)
`фича` · Запуски и heartbeat · автор @alejandroiglesias · балл **76.2** · 777+31 строк · — дн. · CI: —

**#3937** [feat(claude-local): add xhigh and max thinking effort options](https://github.com/paperclipai/paperclip/pull/3937)
`фича` · Claude-адаптер · автор @GodsBoy · балл **76.1** · 85+1 строк · — дн. · CI: —

**#9073** [fix(issues): reject unknown monitor policy fields instead of silently dropping them](https://github.com/paperclipai/paperclip/pull/9073)
`фикс` · Задачи и согласования · автор @dosthcpp · балл **76.1** · 133+1 строк · — дн. · CI: —

**#3131** [fix(adapters/process): inject PAPERCLIP_RUN_ID + PAPERCLIP_API_KEY into spawned env](https://github.com/paperclipai/paperclip/pull/3131)
`фикс` · Другие адаптеры · автор @iws17 · балл **76.1** · 163+1 строк · — дн. · CI: —

**#9810** [feat(mcp): add paperclipListIssueInteractions so agents can read decision-card replies](https://github.com/paperclipai/paperclip/pull/9810)
`фича` · Коннекторы и MCP · автор @greegorij · балл **76.0** · 9+2 строк · — дн. · CI: —

**#9293** [feat(issues): add trigger date to defer agent work until a scheduled time](https://github.com/paperclipai/paperclip/pull/9293)
`фича` · Задачи и согласования · автор @lacymorrow · балл **75.9** · 291+3 строк · — дн. · CI: —

**#8919** [fix(issues): same-agent stale checkout release/adopt across run boundary](https://github.com/paperclipai/paperclip/pull/8919)
`фикс` · Задачи и согласования · автор @florianpollstaetter-dot · балл **75.9** · 224+32 строк · — дн. · CI: —

**#11121** [fix(adapter-utils): authenticate the wake payload so agents can trust it](https://github.com/paperclipai/paperclip/pull/11121)
`безопасность` · Запуски и heartbeat · автор @Nissimmiracles · балл **75.8** · 186+9 строк · — дн. · CI: —

**#10081** [feat(server): include scoped project and milestone intake in wake payload](https://github.com/paperclipai/paperclip/pull/10081)
`фича` · Запуски и heartbeat · автор @Joshtt23 · балл **75.7** · 887+15 строк · — дн. · CI: —

**#11609** [Allow intentional recovery deferral to backlog](https://github.com/paperclipai/paperclip/pull/11609)
`фича` · Задачи и согласования · автор @goldinbidsheets-rgb · балл **75.6** · 203+13 строк · — дн. · CI: —

**#13650** [fix(server): let a heartbeat run write to the issue it checked out](https://github.com/paperclipai/paperclip/pull/13650)
`фикс` · Задачи и согласования · автор @Abel-Salah · балл **75.6** · 549+28 строк · — дн. · CI: —

**#11797** [fix(adapter-utils): block server-only credentials at all agent spawns](https://github.com/paperclipai/paperclip/pull/11797)
`безопасность` · Другие адаптеры · автор @nearfolk · балл **75.6** · 267+27 строк · — дн. · CI: —

**#13685** [fix(heartbeat): stop electing a sibling workspace's cwd for a run that named another](https://github.com/paperclipai/paperclip/pull/13685)
`фикс` · Воркспейсы и git · автор @simberthon · балл **75.5** · 818+39 строк · — дн. · CI: —

**#13659** [fix(issues): auto-assign issue to creating agent when assigneeAgentId missing (INUA-7276)](https://github.com/paperclipai/paperclip/pull/13659)
`фикс` · Задачи и согласования · автор @rotem-zecharia · балл **75.5** · 194+1 строк · — дн. · CI: —

**#10800** [fix(approvals): bind agent secrets on hire approval (COD-362)](https://github.com/paperclipai/paperclip/pull/10800)
`фикс` · Задачи и согласования · автор @codecollie-br · балл **75.5** · 117+2 строк · — дн. · CI: —

**#13550** [fix(server): bind run attribution after verified checkout](https://github.com/paperclipai/paperclip/pull/13550)
`фикс` · Задачи и согласования · автор @kallehiitola · балл **75.4** · 337+5 строк · — дн. · CI: —

**#13883** [fix(recovery): give fresh runs a grace period before the issue-terminal sweep](https://github.com/paperclipai/paperclip/pull/13883)
`фикс` · Запуски и heartbeat · автор @Sergio-LPA · балл **75.3** · 175+7 строк · — дн. · CI: —

**#14005** [fix(server): allow a same-write blocker clear past the blocked-status guard](https://github.com/paperclipai/paperclip/pull/14005)
`фикс` · Задачи и согласования · автор @msoukhomlinov · балл **75.3** · 235+25 строк · — дн. · CI: —

**#13566** [fix(server): restore top-level redacted adapter secrets on agent update](https://github.com/paperclipai/paperclip/pull/13566)
`фикс` · AI-подключения и доступ · автор @alfirus · балл **75.3** · 33+10 строк · — дн. · CI: —

**#10817** [feat(projects): add permanent deletion with managed cleanup](https://github.com/paperclipai/paperclip/pull/10817)
`фича` · Интерфейс · автор @tiangao88 · балл **75.3** · 507+29 строк · — дн. · CI: —

**#13644** [fix(acpx-engine): classify a provider quota wall as a quota wait](https://github.com/paperclipai/paperclip/pull/13644)
`фикс` · Claude-адаптер · автор @Siber704 · балл **75.2** · 62+3 строк · — дн. · CI: —

**#12212** [feat(agents): REST route to grant/revoke scoped permissionKeys on agent principals](https://github.com/paperclipai/paperclip/pull/12212)
`фича` · CLI и API · автор @dzianisv · балл **75.2** · 418+1 строк · — дн. · CI: —

**#9212** [feat(server): return childIssues array from GET /api/issues/{id}](https://github.com/paperclipai/paperclip/pull/9212)
`фича` · Задачи и согласования · автор @calebsimon-CRAFT · балл **75.2** · 114+8 строк · — дн. · CI: —
