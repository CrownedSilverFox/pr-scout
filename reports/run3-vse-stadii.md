# PR Scout: paperclipai/paperclip

Прогон: 2989 PR с баллами, финалистов 120, Jev потратил $0.7286 (14569284 входных токенов).

- `describe`: 0 шт · 1 с · $0 · ошибок 0
- `stage1`: 2989 шт · 365 с · $0.351 · ошибок 0
- `stage2`: 120 шт · 577 с · $0.0443 · ошибок 0
- `issues-list`: 2467 шт · 128 с · $0 · ошибок 0
- `issues`: 2467 шт · 360 с · $0.1883 · ошибок 0
- `rivals`: 34 шт · 12 с · $0.0015 · ошибок 0
- `forks-list`: 15624 шт · 156 с · $0 · ошибок 0
- `forks-list`: 15624 шт · 154 с · $0 · ошибок 0
- `forks-list`: 15627 шт · 144 с · $0 · ошибок 0
- `forks`: 1844 шт · 295 с · $0.1435 · ошибок 0

Последний цикл: 14569284 входных токенов, $0.7286. Все прогоны в истории: 23713640 токенов, $1.5211.

| вариант | цена |
|---|---:|
| Jev (факт, последний цикл) | $0.7286 |
| Claude Opus 5.5 (оценка на тех же токенах) | $252.01 |
| Claude Sonnet 5 (оценка на тех же токенах) | $126.00 |
| Claude Haiku 4.5 (оценка на тех же токенах) | $63.00 |

## Берём (22)

**#12842** [fix(agents): merge runtimeConfig on PATCH instead of replacing the column](https://github.com/paperclipai/paperclip/pull/12842)
`фикс` · CLI и API · автор @vveliev · балл **85.3** · 199+5 строк · — дн. · CI: green
  - + серьёзный баг в обычной работе (вред 0.93, частота 0.73)
  - + прямо про ваше использование (2.75/3)

**#11479** [fix(server): keep comment after-cursor exclusive at microsecond precision](https://github.com/paperclipai/paperclip/pull/11479)
`фикс` · Задачи и согласования · автор @iamasuperuser · балл **85.2** · 147+34 строк · — дн. · CI: green
  - + серьёзный баг в обычной работе (вред 0.85, частота 0.84)
  - + прямо про ваше использование (2.77/3)

**#13936** [fix(server): redact credential-bearing git remotes in run logs](https://github.com/paperclipai/paperclip/pull/13936)
`безопасность` · Запуски и heartbeat · автор @mrkhan91 · балл **84.0** · 606+33 строк · — дн. · CI: green
  - + серьёзный баг в обычной работе (вред 0.93, частота 0.56)
  - + прямо про ваше использование (2.88/3)

**#13978** [fix(claude-local): let npm installs run Opus 5.5 with Claude ACP bridge 0.81.2](https://github.com/paperclipai/paperclip/pull/13978)
`фикс` · Claude-адаптер · автор @itsjeremyjohnson · балл **83.5** · 155+84 строк · — дн. · CI: flaky_only
  - + серьёзный баг в обычной работе (вред 0.83, частота 0.65)
  - + прямо про ваше использование (2.93/3)

**#11107** [fix(recovery): stop agent output from bypassing the run-liveness safety gate](https://github.com/paperclipai/paperclip/pull/11107)
`безопасность` · Запуски и heartbeat · автор @trelmitt · балл **83.5** · 96+3 строк · — дн. · CI: flaky_only
  - + серьёзный баг в обычной работе (вред 0.9, частота 0.55)
  - + прямо про ваше использование (2.91/3)

**#11311** [fix(adapter-utils): redact env dumps and DSN passwords in transcripts](https://github.com/paperclipai/paperclip/pull/11311)
`безопасность` · Прочее · автор @notandrewblejde · балл **83.4** · 209+5 строк · — дн. · CI: flaky_only
  - + серьёзный баг в обычной работе (вред 0.9, частота 0.6)
  - + прямо про ваше использование (2.77/3)

**#11052** [fix(claude-local): classify failures from the run's error surface, not its whole stdout](https://github.com/paperclipai/paperclip/pull/11052)
`фикс` · Claude-адаптер · автор @juancarlosrial76-code · балл **83.0** · 136+1 строк · — дн. · CI: green
  - + серьёзный баг в обычной работе (вред 0.7, частота 0.81)
  - + прямо про ваше использование (2.9/3)

**#13726** [fix(ai-connections): rotate Claude subscription credentials from a file](https://github.com/paperclipai/paperclip/pull/13726)
`фикс` · AI-подключения и доступ · автор @vobornik · балл **81.7** · 153+19 строк · — дн. · CI: green
  - + серьёзный баг в обычной работе (вред 0.82, частота 0.77)
  - + прямо про ваше использование (2.99/3)

**#10735** [fix(issues): re-arm issue monitors on dispatch so a failed run cannot strand the issue](https://github.com/paperclipai/paperclip/pull/10735)
`фикс` · Запуски и heartbeat · автор @juancarlosrial76-code · балл **81.1** · 460+32 строк · — дн. · CI: green
  - + серьёзный баг в обычной работе (вред 0.84, частота 0.58)
  - + прямо про ваше использование (2.84/3)

**#13833** [fix(server): bind run context to the checked-out issue so taskless runs can write](https://github.com/paperclipai/paperclip/pull/13833)
`фикс` · Задачи и согласования · автор @Pdesengrini · балл **80.9** · 848+9 строк · — дн. · CI: green
  - + серьёзный баг в обычной работе (вред 0.88, частота 0.62)
  - + прямо про ваше использование (2.74/3)

**#9219** [fix(claude-local, heartbeat): recover from silent session_lost caused by cwd switches](https://github.com/paperclipai/paperclip/pull/9219)
`фикс` · Claude-адаптер · автор @Sergio-LPA · балл **80.6** · 258+2 строк · — дн. · CI: green
  - + серьёзный баг в обычной работе (вред 0.73, частота 0.73)
  - + прямо про ваше использование (2.91/3)

**#12870** [fix(adapter-utils): strip DATABASE_URL and BETTER_AUTH_SECRET from inherited agent env](https://github.com/paperclipai/paperclip/pull/12870)
`безопасность` · Другие адаптеры · автор @charlieotis · балл **80.6** · 17+0 строк · — дн. · CI: flaky_only
  - + серьёзный баг в обычной работе (вред 0.93, частота 0.62)
  - + прямо про ваше использование (2.54/3)

**#13769** [fix(heartbeat): re-admit a wake parked by a gate that has gone away](https://github.com/paperclipai/paperclip/pull/13769)
`фикс` · Запуски и heartbeat · автор @MrBlackTongue · балл **80.3** · 341+0 строк · — дн. · CI: green
  - + серьёзный баг в обычной работе (вред 0.92, частота 0.55)
  - + прямо про ваше использование (2.76/3)

**#13653** [Deterministic shipped-gate: verify claimed commits before an issue can reach done](https://github.com/paperclipai/paperclip/pull/13653)
`фикс` · Задачи и согласования · автор @ajinkyabhanudas · балл **80.2** · 558+17 строк · — дн. · CI: green
  - + серьёзный баг в обычной работе (вред 0.78, частота 0.69)
  - + прямо про ваше использование (2.89/3)

**#7432** [fix(issues): resolve identifier to UUID for parentId/descendantOf filters](https://github.com/paperclipai/paperclip/pull/7432)
`фикс` · Задачи и согласования · автор @Sergio-LPA · балл **80.1** · 398+10 строк · — дн. · CI: green
  - + серьёзный баг в обычной работе (вред 0.76, частота 0.77)
  - + прямо про ваше использование (2.54/3)

**#11462** [fix(security): redact sensitive fields in config-read API responses (extracted from #10284)](https://github.com/paperclipai/paperclip/pull/11462)
`безопасность` · Коннекторы и MCP · автор @JackReis · балл **78.1** · 95+1 строк · — дн. · CI: flaky_only
  - + серьёзный баг в обычной работе (вред 0.87, частота 0.75)

**#9810** [feat(mcp): add paperclipListIssueInteractions so agents can read decision-card replies](https://github.com/paperclipai/paperclip/pull/9810)
`фича` · Коннекторы и MCP · автор @greegorij · балл **77.2** · 9+2 строк · — дн. · CI: flaky_only
  - + сильная фича (ценность 3.36/4, новизна 0.88)
  - + прямо про ваше использование (2.57/3)

**#3856** [fix(agents): preserve sibling keys of runtimeConfig on partial PATCH](https://github.com/paperclipai/paperclip/pull/3856)
`фикс` · CLI и API · автор @sparkeros · балл **76.6** · 12+0 строк · — дн. · CI: green
  - + серьёзный баг в обычной работе (вред 0.88, частота 0.78)
  - + прямо про ваше использование (2.52/3)

**#13782** [fix: keep the requesting run alive when an agent hands off its own issue](https://github.com/paperclipai/paperclip/pull/13782)
`фикс` · Задачи и согласования · автор @Waseemilyas · балл **76.4** · 94+1 строк · — дн. · CI: green
  - + серьёзный баг в обычной работе (вред 0.52, частота 0.82)
  - + прямо про ваше использование (2.85/3)

**#4807** [fix(recovery): dispatch in_progress sub-issues with no execution history as fresh assignment (PAP-4766)](https://github.com/paperclipai/paperclip/pull/4807)
`фикс` · Запуски и heartbeat · автор @aimonk2025 · балл **76.3** · 111+1 строк · — дн. · CI: green
  - + серьёзный баг в обычной работе (вред 0.63, частота 0.67)
  - + прямо про ваше использование (2.69/3)

**#13060** [feat(runs): add session-log ZIP export for heartbeat runs](https://github.com/paperclipai/paperclip/pull/13060)
`фича` · Запуски и heartbeat · автор @tejasghalsasi · балл **76.3** · 606+0 строк · — дн. · CI: flaky_only
  - + сильная фича (ценность 3.21/4, новизна 0.9)

**#11336** [fix(server): share one pluginLifecycleManager between routes and dispatcher](https://github.com/paperclipai/paperclip/pull/11336)
`фикс` · Коннекторы и MCP · автор @c-barlow · балл **76.2** · 173+5 строк · — дн. · CI: green
  - + серьёзный баг в обычной работе (вред 0.57, частота 0.79)
  - + прямо про ваше использование (2.71/3)


## Рассмотреть (20)

**#13622** [fix(claude-local): use the `auth login` subcommand for agent login](https://github.com/paperclipai/paperclip/pull/13622)
`фикс` · Claude-адаптер · автор @croakingtoad · балл **84.5** · 53+1 строк · — дн. · CI: red
  - ! падают тесты CI: ci / verify, ci / Build, ci / Canary Dry Run
  - + серьёзный баг в обычной работе (вред 0.87, частота 0.79)
  - + прямо про ваше использование (2.75/3)

**#6808** [feat(heartbeat): ADR-0044 session lifecycle T1/T2/T3/T4 for claude_local](https://github.com/paperclipai/paperclip/pull/6808)
`фича` · Запуски и heartbeat · автор @yackovleff-solved · балл **84.0** · 680+23 строк · — дн. · CI: green
  - ! фича меняет поведение по умолчанию
  - + сильная фича (ценность 3.03/4, новизна 0.64)
  - + прямо про ваше использование (2.98/3)

**#14039** [fix(claude-local): map thinking effort to the selected model](https://github.com/paperclipai/paperclip/pull/14039)
`фикс` · Claude-адаптер · автор @nctiggy · балл **81.2** · 323+42 строк · — дн. · CI: green
  - ! баг не критичный или редкий
  - + прямо про ваше использование (2.96/3)

**#13802** [fix(server): default and cap the heartbeat-runs list limit](https://github.com/paperclipai/paperclip/pull/13802)
`фикс` · Запуски и heartbeat · автор @hsluiscampingcomfort · балл **81.0** · 89+13 строк · — дн. · CI: red
  - ! падают тесты CI: ci / verify, ci / Verify Paperclip Runner (vitest 1/2)
  - + серьёзный баг в обычной работе (вред 0.88, частота 0.7)
  - + прямо про ваше использование (2.53/3)

**#13148** [fix(claude-local): classify ACP session-limit turn failures as provider quota with the parsed reset time](https://github.com/paperclipai/paperclip/pull/13148)
`фикс` · Claude-адаптер · автор @Sasshigo · балл **80.3** · 139+1 строк · — дн. · CI: red
  - ! падают тесты CI: ci / verify, ci / General tests (server (1/5))
  - + серьёзный баг в обычной работе (вред 0.7, частота 0.8)
  - + прямо про ваше использование (2.77/3)

**#10862** [Make agent role editable after creation](https://github.com/paperclipai/paperclip/pull/10862)
`фича` · Интерфейс · автор @lucktastic · балл **79.9** · 127+3 строк · — дн. · CI: green
  - ! фича полезная, но не ключевая

**#11466** [fix(server): atomically set checkout run contextSnapshot with issue lock](https://github.com/paperclipai/paperclip/pull/11466)
`фикс` · Задачи и согласования · автор @santhiprakash · балл **79.9** · 281+58 строк · — дн. · CI: red
  - ! падают тесты CI: ci / verify, ci / General tests (server (3/5))
  - + серьёзный баг в обычной работе (вред 0.79, частота 0.59)
  - + прямо про ваше использование (2.9/3)

**#13478** [feat(claude-local): retry transient upstream errors with exponential backoff](https://github.com/paperclipai/paperclip/pull/13478)
`фича` · Claude-адаптер · автор @daniel-mariani · балл **79.6** · 300+1 строк · — дн. · CI: red
  - ! фича полезная, но не ключевая
  - ! падают тесты CI: ci / verify, ci / General tests (server (1/5))
  - ! фича меняет поведение по умолчанию
  - + прямо про ваше использование (2.81/3)

**#10871** [feat(dashboard): report token usage where subscription billing zeroes spend](https://github.com/paperclipai/paperclip/pull/10871)
`фича` · Интерфейс · автор @Nissimmiracles · балл **78.7** · 651+38 строк · — дн. · CI: flaky_only
  - ! фича полезная, но не ключевая
  - ! фича меняет поведение по умолчанию
  - + прямо про ваше использование (2.59/3)

**#14248** [fix(server): keep a policy's other fields when a monitor is stripped](https://github.com/paperclipai/paperclip/pull/14248)
`фикс` · Задачи и согласования · автор @stefanriegel · балл **78.4** · 125+8 строк · — дн. · CI: red
  - ! падают тесты CI: ci / Verify serialized server suites (1/9)
  - + серьёзный баг в обычной работе (вред 0.83, частота 0.63)

**#13447** [fix: preserve OAuth refresh access and contain managed MCP config](https://github.com/paperclipai/paperclip/pull/13447)
`фикс` · Коннекторы и MCP · автор @joeviezner · балл **78.2** · 303+21 строк · — дн. · CI: green
  - ! баг не критичный или редкий
  - + прямо про ваше использование (2.9/3)

**#12786** [fix(adapter-utils): redact header-style secrets in command text](https://github.com/paperclipai/paperclip/pull/12786)
`безопасность` · Прочее · автор @superbiche · балл **78.1** · 1925+4 строк · — дн. · CI: green
  - ! большой PR (1929 строк)
  - + серьёзный баг в обычной работе (вред 0.93, частота 0.83)
  - + прямо про ваше использование (2.56/3)

**#13892** [fix(issues): let the assignee supersede critically-silent run bindings](https://github.com/paperclipai/paperclip/pull/13892)
`фикс` · Запуски и heartbeat · автор @iamasuperuser · балл **78.0** · 788+48 строк · — дн. · CI: green
  - ! баг не критичный или редкий
  - + прямо про ваше использование (2.88/3)

**#14192** [feat(chat): add a Delete chat action to the agent conversation header](https://github.com/paperclipai/paperclip/pull/14192)
`фича` · Интерфейс · автор @MatrixCODEBreak · балл **77.9** · 293+2 строк · — дн. · CI: flaky_only
  - ! фича полезная, но не ключевая

**#11980** [feat(approvals): add POST /approvals/:id/cancel for requester withdrawal [INUA-5995]](https://github.com/paperclipai/paperclip/pull/11980)
`фича` · Задачи и согласования · автор @rotem-zecharia · балл **77.8** · 386+1 строк · — дн. · CI: flaky_only
  - ! фича меняет поведение по умолчанию
  - + сильная фича (ценность 3.14/4, новизна 0.9)

**#13134** [feat(codex-models): read the Codex CLI models cache for ChatGPT-auth installs](https://github.com/paperclipai/paperclip/pull/13134)
`фича` · Codex-адаптер · автор @MindSyncHub · балл **77.5** · 206+1 строк · — дн. · CI: green
  - ! фича полезная, но не ключевая
  - ! фича меняет поведение по умолчанию
  - + прямо про ваше использование (2.53/3)

**#8063** [feat(claude-local): resolve @ file references in agent instructions](https://github.com/paperclipai/paperclip/pull/8063)
`фича` · Claude-адаптер · автор @burnlife001 · балл **77.4** · 150+1 строк · — дн. · CI: red
  - ! падают тесты CI: verify, General tests (server)
  - + сильная фича (ценность 3.22/4, новизна 0.87)
  - + прямо про ваше использование (2.63/3)

**#4764** [fix: add goal owner editing in goals UI](https://github.com/paperclipai/paperclip/pull/4764)
`фича` · Интерфейс · автор @dumi-bogdan · балл **77.2** · 496+3 строк · — дн. · CI: flaky_only
  - ! фича полезная, но не ключевая
  - ! фича меняет поведение по умолчанию

**#8800** [Add task thread sort order option](https://github.com/paperclipai/paperclip/pull/8800)
`фича` · Интерфейс · автор @saphid · балл **77.1** · 512+55 строк · — дн. · CI: green
  - ! фича полезная, но не ключевая

**#13069** [feat(plugins): add per-tool timeouts with structured timeout results](https://github.com/paperclipai/paperclip/pull/13069)
`фича` · Коннекторы и MCP · автор @tejasghalsasi · балл **76.9** · 424+23 строк · — дн. · CI: flaky_only
  - ! фича меняет поведение по умолчанию
  - + сильная фича (ценность 3.03/4, новизна 0.8)


## Пропускаем (78)

**#8841** [fix(server): sanitize credential-shaped values before persistence](https://github.com/paperclipai/paperclip/pull/8841)
`безопасность` · Запуски и heartbeat · автор @robertdevore · балл **84.9** · 373+12 строк · — дн. · CI: green
  - ✗ конфликт с основной веткой и взятыми PR: redaction.ts, activity.ts, activity-log.ts
  - + серьёзный баг в обычной работе (вред 0.86, частота 0.85)
  - + прямо про ваше использование (2.95/3)

**#6692** [feat: implement server-side secret value redaction](https://github.com/paperclipai/paperclip/pull/6692)
`безопасность` · Запуски и heartbeat · автор @gorkemhacioglu · балл **84.6** · 307+33 строк · — дн. · CI: flaky_only
  - ✗ конфликт с основной веткой и взятыми PR: redaction.test.ts, heartbeat.ts
  - + серьёзный баг в обычной работе (вред 0.91, частота 0.82)
  - + прямо про ваше использование (2.89/3)

**#4294** [Feature/4281 configurable claude local session lifecycle](https://github.com/paperclipai/paperclip/pull/4294)
`фича` · Запуски и heartbeat · автор @thomascolden585-svg · балл **84.3** · 519+11 строк · — дн. · CI: red
  - ✗ конфликт с основной веткой и взятыми PR: heartbeat.ts, Layout.tsx, PropertiesPanel.tsx
  - ✗ код не совпадает с описанием (0.1)
  - ! падают тесты CI: verify
  - + сильная фича (ценность 3.49/4, новизна 0.84)
  - + прямо про ваше использование (2.93/3)

**#9750** [fix(tool-access,tool-gateway): perform MCP initialize handshake for remote HTTP servers, and retry through session churn](https://github.com/paperclipai/paperclip/pull/9750)
`фикс` · Коннекторы и MCP · автор @Quentin-M · балл **84.1** · 521+63 строк · — дн. · CI: flaky_only
  - ✗ конфликт с основной веткой и взятыми PR: mcp-http.test.ts, tool-access-service.test.ts, tool-gateway.test.ts
  - ✗ код не совпадает с описанием (0.45)
  - + серьёзный баг в обычной работе (вред 0.92, частота 0.55)
  - + прямо про ваше использование (2.96/3)

**#4004** [feat(adapter-utils): idle + wall watchdogs for runChildProcess](https://github.com/paperclipai/paperclip/pull/4004)
`фича` · Другие адаптеры · автор @ericnicolaides · балл **83.7** · 489+44 строк · — дн. · CI: green
  - ✗ конфликт с основной веткой и взятыми PR: server-utils.test.ts, server-utils.ts, execute.ts
  - + сильная фича (ценность 3.44/4, новизна 0.78)
  - + прямо про ваше использование (2.99/3)

**#11387** [feat(pipelines): issue-driven stage gates (autoAdvanceOnIssue) + pipeline-managed disposition exemption](https://github.com/paperclipai/paperclip/pull/11387)
`фича` · Задачи и согласования · автор @adamteale · балл **83.5** · 618+1 строк · — дн. · CI: red
  - ✗ конфликт с основной веткой и взятыми PR: successful-run-handoff.ts
  - ! падают тесты CI: ci / verify, ci / General tests (server (3/5))
  - + сильная фича (ценность 3.34/4, новизна 0.85)
  - + прямо про ваше использование (2.59/3)

**#3337** [feat(ui,adapter): add MCP server configuration for claude_local agents](https://github.com/paperclipai/paperclip/pull/3337)
`фича` · Claude-адаптер · автор @gbrancaglione · балл **83.4** · 849+6 строк · — дн. · CI: green
  - ✗ конфликт с основной веткой и взятыми PR: execute.ts, AgentDetail.tsx, vitest.config.ts
  - + сильная фича (ценность 3.16/4, новизна 0.89)
  - + прямо про ваше использование (2.92/3)

**#12539** [fix(server): redact heartbeat adapter output before persistence](https://github.com/paperclipai/paperclip/pull/12539)
`безопасность` · Запуски и heartbeat · автор @Dfskid · балл **83.0** · 672+50 строк · — дн. · CI: red
  - ✗ конфликт с основной веткой и взятыми PR: heartbeat-process-recovery.test.ts, redaction.test.ts, redaction.ts
  - ! падают тесты CI: ci / verify, ci / General tests (server (4/5)), ci / Build
  - + серьёзный баг в обычной работе (вред 0.82, частота 0.77)
  - + прямо про ваше использование (2.69/3)

**#12930** [fix(claude-local): keep mcpServerIdentity and remoteExecution in the session codec](https://github.com/paperclipai/paperclip/pull/12930)
`фикс` · Claude-адаптер · автор @qwlong · балл **82.9** · 94+0 строк · — дн. · CI: red
  - ✗ конфликт с основной веткой и взятыми PR: adapter-session-codecs.test.ts
  - ! падают тесты CI: ci / Verify serialized server suites (5/5)
  - + серьёзный баг в обычной работе (вред 0.65, частота 0.87)
  - + прямо про ваше использование (2.98/3)

**#11923** [fix(acpx): keep projected secrets off the persisted session env](https://github.com/paperclipai/paperclip/pull/11923)
`безопасность` · AI-подключения и доступ · автор @alaimster · балл **82.8** · 156+24 строк · — дн. · CI: green
  - ✗ конфликт с основной веткой и взятыми PR: execute.ts, acpx@0.12.0.patch
  - + серьёзный баг в обычной работе (вред 0.94, частота 0.84)
  - + прямо про ваше использование (2.76/3)

**#12002** [fix(approvals): auto-transition in_review issues and wake agents on card rejection](https://github.com/paperclipai/paperclip/pull/12002)
`фикс` · Задачи и согласования · автор @rotem-zecharia · балл **82.7** · 580+3 строк · — дн. · CI: flaky_only
  - ✗ код не совпадает с описанием (0.15)
  - + серьёзный баг в обычной работе (вред 0.86, частота 0.83)
  - + прямо про ваше использование (2.62/3)

**#5663** [feat(active-memory): inject always-check memories into agent system prompt on every wake (VOG-5736)](https://github.com/paperclipai/paperclip/pull/5663)
`фича` · Claude-адаптер · автор @vg-jerry · балл **82.5** · 678+1 строк · — дн. · CI: no_ci
  - ✗ конфликт с основной веткой и взятыми PR: execute.ts
  - + сильная фича (ценность 3.47/4, новизна 0.71)
  - + прямо про ваше использование (2.92/3)

**#12031** [fix(issues): arm a default wait monitor when an interaction parks the issue](https://github.com/paperclipai/paperclip/pull/12031)
`фикс` · Задачи и согласования · автор @juancarlosrial76-code · балл **82.4** · 534+1 строк · — дн. · CI: green
  - ✗ конфликт с основной веткой и взятыми PR: issues.ts
  - + серьёзный баг в обычной работе (вред 0.73, частота 0.88)
  - + прямо про ваше использование (2.77/3)

**#7541** [feat(llm): OpenAI-compatible baseUrl + runtime API URL/CLI robustness fixes](https://github.com/paperclipai/paperclip/pull/7541)
`фича` · CLI и API · автор @oups75 · балл **82.4** · 196+35 строк · — дн. · CI: flaky_only
  - ✗ конфликт с основной веткой и взятыми PR: package.json, index.ts, config-schema.test.ts
  - ! фича меняет поведение по умолчанию
  - + сильная фича (ценность 3.36/4, новизна 0.84)
  - + прямо про ваше использование (2.81/3)

**#13950** [feat(budgets): add native calendar_day_utc budget window](https://github.com/paperclipai/paperclip/pull/13950)
`фича` · Задачи и согласования · автор @biokub-agent · балл **82.1** · 297+39 строк · — дн. · CI: flaky_only
  - ✗ код не совпадает с описанием (0.45)
  - + сильная фича (ценность 3.57/4, новизна 0.91)

**#11096** [fix(interactions): accept intuitive ask_user_questions payload shape](https://github.com/paperclipai/paperclip/pull/11096)
`фикс` · Задачи и согласования · автор @sagiw · балл **82.1** · 96+3 строк · — дн. · CI: green
  - ✗ конфликт с основной веткой и взятыми PR: issue.test.ts, issue.ts
  - + серьёзный баг в обычной работе (вред 0.91, частота 0.84)
  - + прямо про ваше использование (2.73/3)

**#5674** [fix: deep-merge runtimeConfig on PATCH instead of full column replace](https://github.com/paperclipai/paperclip/pull/5674)
`фикс` · CLI и API · автор @notandrewblejde · балл **81.9** · 355+16 строк · — дн. · CI: green
  - ✗ конфликт с основной веткой и взятыми PR: agents.ts, queryKeys.ts, Agents.tsx
  - ✗ код не совпадает с описанием (0.1)
  - + серьёзный баг в обычной работе (вред 0.9, частота 0.82)
  - + прямо про ваше использование (2.74/3)

**#13197** [fix(ui): submit stage decisions with required comments](https://github.com/paperclipai/paperclip/pull/13197)
`фича` · Интерфейс · автор @JamesSparkMojo · балл **81.8** · 288+4 строк · — дн. · CI: flaky_only
  - ✗ конфликт с основной веткой и взятыми PR: IssueProperties.tsx
  - + сильная фича (ценность 3.32/4, новизна 0.92)

**#3497** [[codex] Add agent model failover chains](https://github.com/paperclipai/paperclip/pull/3497)
`фича` · Запуски и heartbeat · автор @akshitnanda · балл **81.8** · 531+48 строк · — дн. · CI: green
  - ✗ конфликт с основной веткой и взятыми PR: index.ts, build-config.ts, build-config.test.ts
  - + сильная фича (ценность 3.38/4, новизна 0.84)
  - + прямо про ваше использование (2.85/3)

**#13138** [fix(server): add durable zombie-session reaper for claude_local runs](https://github.com/paperclipai/paperclip/pull/13138)
`фикс` · Запуски и heartbeat · автор @daniel-mariani · балл **81.7** · 818+5 строк · — дн. · CI: green
  - ✗ конфликт с основной веткой и взятыми PR: native-session-resumption.test.ts
  - + серьёзный баг в обычной работе (вред 0.87, частота 0.53)
  - + прямо про ваше использование (2.96/3)

**#2779** [  **`security: mitigate cross-agent prompt injection via session handoff content (#2755)`**](https://github.com/paperclipai/paperclip/pull/2779)
`безопасность` · Запуски и heartbeat · автор @utk2602 · балл **81.7** · 408+21 строк · — дн. · CI: green
  - ✗ конфликт с основной веткой и взятыми PR: server-utils.test.ts, execute.ts, execute.ts
  - ✗ код не совпадает с описанием (0.43)
  - + серьёзный баг в обычной работе (вред 0.88, частота 0.7)
  - + прямо про ваше использование (2.98/3)

**#13223** [fix(api): reject unknown keys in issue mutation bodies](https://github.com/paperclipai/paperclip/pull/13223)
`фикс` · Задачи и согласования · автор @trixy-the-ai-bot · балл **81.5** · 269+14 строк · — дн. · CI: green
  - ✗ конфликт с основной веткой и взятыми PR: issue.ts
  - + серьёзный баг в обычной работе (вред 0.82, частота 0.67)
  - + прямо про ваше использование (2.68/3)

**#13995** [fix(sandbox-kubernetes): stop pointing built-in adapter defaults at a never-published :v1 tag](https://github.com/paperclipai/paperclip/pull/13995)
`фикс` · Деплой и self-host · автор @BluePhi09 · балл **81.4** · 269+14 строк · — дн. · CI: green
  - ✗ код не совпадает с описанием (0.18)
  - + серьёзный баг в обычной работе (вред 0.8, частота 0.65)
  - + прямо про ваше использование (2.91/3)

**#13056** [fix(cross-issue-limit): allow heartbeat_timer runs to write to checked-out issues (INUA-6799)](https://github.com/paperclipai/paperclip/pull/13056)
`фикс` · Задачи и согласования · автор @rotem-zecharia · балл **81.4** · 99+6 строк · — дн. · CI: green
  - ✗ конфликт с основной веткой и взятыми PR: heartbeat-issue-liveness-escalation.test.ts
  - ! рискованная область (0.65)
  - + серьёзный баг в обычной работе (вред 0.9, частота 0.82)
  - + прямо про ваше использование (2.95/3)

**#11367** [feat(adapter-utils): opt-in allowlist for agent env inheritance](https://github.com/paperclipai/paperclip/pull/11367)
`безопасность` · Другие адаптеры · автор @marijnp7 · балл **81.4** · 436+25 строк · — дн. · CI: green
  - ✗ конфликт с основной веткой и взятыми PR: execute.ts, test.ts, execute.ts
  - + серьёзный баг в обычной работе (вред 0.87, частота 0.77)
  - + прямо про ваше использование (2.93/3)

**#12649** [fix(server): redact agent profile configuration by default](https://github.com/paperclipai/paperclip/pull/12649)
`безопасность` · CLI и API · автор @samikujakanto · балл **81.3** · 942+51 строк · — дн. · CI: red
  - ✗ конфликт с основной веткой и взятыми PR: low-trust-red-team-routes.test.ts, redaction.test.ts, agents.ts
  - ✗ код не совпадает с описанием (0.19)
  - ! падают тесты CI: ci / Verify serialized server suites (2/5)
  - + серьёзный баг в обычной работе (вред 0.92, частота 0.67)
  - + прямо про ваше использование (2.61/3)

**#3885** [Company run toggle](https://github.com/paperclipai/paperclip/pull/3885)
`фича` · Запуски и heartbeat · автор @Micsi · балл **81.1** · 685+10 строк · — дн. · CI: green
  - ✗ конфликт с основной веткой и взятыми PR: heartbeat-process-recovery.test.ts, companies.ts, heartbeat.ts
  - ! фича меняет поведение по умолчанию
  - + сильная фича (ценность 3.56/4, новизна 0.81)
  - + прямо про ваше использование (2.66/3)

**#11558** [fix(adapter-utils): strip server secrets from agent env](https://github.com/paperclipai/paperclip/pull/11558)
`безопасность` · Claude-адаптер · автор @Doom121212 · балл **80.9** · 91+4 строк · — дн. · CI: red
  - ✗ конфликт с основной веткой и взятыми PR: execute.ts, spawn-smoke.test.ts, acpx@0.12.0.patch
  - ! падают тесты CI: verify, General tests (workspaces-b)
  - + серьёзный баг в обычной работе (вред 0.91, частота 0.81)
  - + прямо про ваше использование (2.74/3)

**#9588** [fix: prevent project environment values from leaking through API responses](https://github.com/paperclipai/paperclip/pull/9588)
`безопасность` · Задачи и согласования · автор @cablackmon · балл **80.7** · 578+26 строк · — дн. · CI: green
  - ✗ конфликт с основной веткой и взятыми PR: index.ts, project.ts, issues.ts
  - + серьёзный баг в обычной работе (вред 0.91, частота 0.76)
  - + прямо про ваше использование (2.77/3)

**#13966** [feat(ui): move and delete tasks from context menus](https://github.com/paperclipai/paperclip/pull/13966)
`фича` · Задачи и согласования · автор @luizvb · балл **79.7** · 603+12 строк · — дн. · CI: green
  - ✗ код не совпадает с описанием (0.37)
  - ! фича полезная, но не ключевая
  - ! фича меняет поведение по умолчанию

**#12581** [fix(server): fail closed on secret-shaped issue comments](https://github.com/paperclipai/paperclip/pull/12581)
`безопасность` · Задачи и согласования · автор @apex-skyner · балл **79.6** · 246+7 строк · — дн. · CI: red
  - ✗ конфликт с основной веткой и взятыми PR: issues-service.test.ts, redaction.test.ts, redaction.ts
  - ! падают тесты CI: ci / verify, ci / General tests (server (3/5)), ci / General tests (server (4/5)), ci / Verify serialized server suites 
  - + серьёзный баг в обычной работе (вред 0.91, частота 0.62)
  - + прямо про ваше использование (2.54/3)

**#6042** [feat: auto-inject text attachment content in heartbeat-context + bridge allowlist](https://github.com/paperclipai/paperclip/pull/6042)
`фича` · Задачи и согласования · автор @firepol-ai · балл **79.6** · 310+12 строк · — дн. · CI: green
  - ✗ конфликт с основной веткой и взятыми PR: attachment-types.test.ts, attachment-types.ts, issues.ts
  - ✗ код не совпадает с описанием (0.38)
  - ! фича меняет поведение по умолчанию
  - + сильная фича (ценность 3.45/4, новизна 0.74)
  - + прямо про ваше использование (2.67/3)

**#2642** [fix: redact Paperclip secrets from logs and Codex artifacts](https://github.com/paperclipai/paperclip/pull/2642)
`безопасность` · Codex-адаптер · автор @halfwitgaslit · балл **79.6** · 376+13 строк · — дн. · CI: green
  - ✗ конфликт с основной веткой и взятыми PR: codex-home.ts, execute.ts, codex-local-execute.test.ts
  - + серьёзный баг в обычной работе (вред 0.88, частота 0.72)
  - + прямо про ваше использование (2.89/3)

**#6373** [fix: redact runtime secret values in run logs](https://github.com/paperclipai/paperclip/pull/6373)
`безопасность` · Запуски и heartbeat · автор @jasondbramley · балл **79.5** · 124+7 строк · — дн. · CI: green
  - ✗ конфликт с основной веткой и взятыми PR: command-redaction.test.ts, command-redaction.ts, redaction.test.ts
  - + серьёзный баг в обычной работе (вред 0.9, частота 0.72)
  - + прямо про ваше использование (2.69/3)

**#5631** [fix(api): prevent update wiping secret bindings](https://github.com/paperclipai/paperclip/pull/5631)
`фикс` · AI-подключения и доступ · автор @freddiecoleman · балл **79.5** · 68+5 строк · — дн. · CI: green
  - ✗ конфликт с основной веткой и взятыми PR: agents.ts
  - + серьёзный баг в обычной работе (вред 0.93, частота 0.6)
  - + прямо про ваше использование (2.92/3)

**#7757** [fix: handle EPIPE on adapter stdin.write after pipe close](https://github.com/paperclipai/paperclip/pull/7757)
`фикс` · Прочее · автор @exocode · балл **79.4** · 36+1 строк · — дн. · CI: green
  - ✗ конфликт с основной веткой и взятыми PR: server-utils.test.ts
  - + серьёзный баг в обычной работе (вред 0.79, частота 0.64)
  - + прямо про ваше использование (2.7/3)

**#6162** [Fix skill mention UUID/slug dispatch resolution](https://github.com/paperclipai/paperclip/pull/6162)
`фикс` · Запуски и heartbeat · автор @ryanclark2 · балл **79.4** · 143+4 строк · — дн. · CI: green
  - ✗ конфликт с основной веткой и взятыми PR: heartbeat-project-env.test.ts, issues-service.test.ts, issues.ts
  - + серьёзный баг в обычной работе (вред 0.87, частота 0.73)
  - + прямо про ваше использование (2.7/3)

**#11073** [fix(claude-local): classify an unrefreshable OAuth session as auth required](https://github.com/paperclipai/paperclip/pull/11073)
`фикс` · Claude-адаптер · автор @juancarlosrial76-code · балл **79.0** · 36+1 строк · — дн. · CI: green
  - ✗ конфликт с основной веткой и взятыми PR: parse.test.ts, parse.ts
  - + серьёзный баг в обычной работе (вред 0.9, частота 0.68)
  - + прямо про ваше использование (2.91/3)

**#1862** [feat: add raigo governance skill for AI policy enforcement](https://github.com/paperclipai/paperclip/pull/1862)
`фича` · Коннекторы и MCP · автор @musharsec · балл **78.9** · 170+0 строк · — дн. · CI: flaky_only
  - ✗ продвигает сторонний сервис (0.74)
  - + сильная фича (ценность 3.74/4, новизна 0.86)

**#13992** [feat(ui): add project status picker to the project detail page](https://github.com/paperclipai/paperclip/pull/13992)
`фича` · Интерфейс · автор @b3nnb · балл **78.8** · 372+15 строк · — дн. · CI: red
  - ✗ конфликт с основной веткой и взятыми PR: ProjectDetail.test.tsx
  - ! фича полезная, но не ключевая
  - ! падают тесты CI: ci / verify, ci / General tests (chat (1/3)), ci / Verify Paperclip Runner (vitest 1/2)
  - ! фича меняет поведение по умолчанию

**#10532** [fix(task-watchdogs): stop re-waking valid human-blocked leaves / self-inflicted fingerprint churn (JAC-3989)](https://github.com/paperclipai/paperclip/pull/10532)
`фикс` · Запуски и heartbeat · автор @JackReis · балл **78.8** · 205+712 строк · — дн. · CI: green
  - ✗ код не совпадает с описанием (0.21)
  - ! лишние изменения в дифе
  - + серьёзный баг в обычной работе (вред 0.84, частота 0.71)
  - + прямо про ваше использование (2.67/3)

**#13630** [fix(ui): present choice questions a stored question set leaves out](https://github.com/paperclipai/paperclip/pull/13630)
`фикс` · Интерфейс · автор @GustavoLarcoDev · балл **78.7** · 253+46 строк · — дн. · CI: green
  - ✗ конфликт с основной веткой и взятыми PR: issue-thread-interactions.test.ts
  - + серьёзный баг в обычной работе (вред 0.86, частота 0.67)
  - + прямо про ваше использование (2.61/3)

**#10104** [fix(server/approvals): wake requester on reject and request-revision](https://github.com/paperclipai/paperclip/pull/10104)
`фикс` · Задачи и согласования · автор @nydamon · балл **78.5** · 264+72 строк · — дн. · CI: flaky_only
  - ✗ конфликт с основной веткой и взятыми PR: approvals.ts
  - + серьёзный баг в обычной работе (вред 0.71, частота 0.85)
  - + прямо про ваше использование (2.89/3)

**#1788** [fix(server): restore issue comment cursor pagination](https://github.com/paperclipai/paperclip/pull/1788)
`фикс` · Задачи и согласования · автор @yoyooyooo · балл **78.5** · 87+9 строк · — дн. · CI: green
  - ✗ конфликт с основной веткой и взятыми PR: issues.ts
  - + серьёзный баг в обычной работе (вред 0.81, частота 0.63)
  - + прямо про ваше использование (2.93/3)

**#5262** [Sync: Update from paperclipai/master](https://github.com/paperclipai/paperclip/pull/5262)
`фикс` · Деплой и self-host · автор @deancorserv · балл **78.4** · 457+3 строк · — дн. · CI: flaky_only
  - ✗ конфликт с основной веткой и взятыми PR: docker.yml, heartbeat-workspace-session.test.ts, heartbeat.ts
  - ✗ код не совпадает с описанием (0.28)
  - ! баг не критичный или редкий
  - + прямо про ваше использование (2.96/3)

**#8205** [fix(shared): store multiline text verbatim, stop eating \r/\n escapes (RENA-14562)](https://github.com/paperclipai/paperclip/pull/8205)
`фикс` · Задачи и согласования · автор @rendedennis6-byte · балл **78.4** · 53+25 строк · — дн. · CI: red
  - ✗ конфликт с основной веткой и взятыми PR: issue.test.ts
  - ! падают тесты CI: verify, General tests (server)
  - + серьёзный баг в обычной работе (вред 0.9, частота 0.57)
  - + прямо про ваше использование (2.84/3)

**#4386** [feat(plugin-events): enrich agent.run.* payload with issue context + result](https://github.com/paperclipai/paperclip/pull/4386)
`фича` · Запуски и heartbeat · автор @Bricol1982 · балл **78.3** · 76+24 строк · — дн. · CI: green
  - ✗ конфликт с основной веткой и взятыми PR: heartbeat.ts
  - ! фича меняет поведение по умолчанию
  - + сильная фича (ценность 3.5/4, новизна 0.81)
  - + прямо про ваше использование (2.74/3)

**#2388** [feat(ui): add user management UI to company settings](https://github.com/paperclipai/paperclip/pull/2388)
`фича` · Интерфейс · автор @vbalko-claimate · балл **78.3** · 693+5 строк · — дн. · CI: green
  - ✗ конфликт с основной веткой и взятыми PR: app.ts, access.ts, Layout.tsx
  - ! фича меняет поведение по умолчанию
  - + сильная фича (ценность 3.94/4, новизна 0.9)
  - + прямо про ваше использование (2.71/3)

**#13117** [fix(issues): read the checkout lock's premise instead of inferring it from status](https://github.com/paperclipai/paperclip/pull/13117)
`фикс` · Задачи и согласования · автор @jayproulx · балл **78.2** · 219+5 строк · — дн. · CI: flaky_only
  - ✗ конфликт с основной веткой и взятыми PR: issues.ts
  - + серьёзный баг в обычной работе (вред 0.86, частота 0.54)
  - + прямо про ваше использование (2.83/3)

**#13321** [fix(codex): pass MCP bearer tokens through env](https://github.com/paperclipai/paperclip/pull/13321)
`фикс` · Codex-адаптер · автор @iceFusion101 · балл **78.1** · 28+9 строк · — дн. · CI: green
  - ✗ конфликт с основной веткой и взятыми PR: codex-home.test.ts, codex-home.ts
  - + серьёзный баг в обычной работе (вред 0.85, частота 0.54)
  - + прямо про ваше использование (2.75/3)

**#11945** [[INUA-6044] fix(approvals): wake linked-issue assignees on card approval](https://github.com/paperclipai/paperclip/pull/11945)
`фикс` · Задачи и согласования · автор @rotem-zecharia · балл **78.1** · 179+0 строк · — дн. · CI: flaky_only
  - ✗ конфликт с основной веткой и взятыми PR: approval-routes-idempotency.test.ts
  - ! баг не критичный или редкий
  - + прямо про ваше использование (2.71/3)

**#5833** [feat(harness): runtime orphan reaper + pre-spawn process guard](https://github.com/paperclipai/paperclip/pull/5833)
`фича` · Запуски и heartbeat · автор @ddemid · балл **78.0** · 428+8 строк · — дн. · CI: green
  - ✗ конфликт с основной веткой и взятыми PR: heartbeat-stale-queue-invalidation.test.ts, index.ts, heartbeat.ts
  - ✗ код не совпадает с описанием (0.46)
  - ! фича полезная, но не ключевая
  - ! фича меняет поведение по умолчанию
  - + прямо про ваше использование (2.94/3)

**#3481** [fix(server): alias assigneeId to assigneeAgentId in POST /issues](https://github.com/paperclipai/paperclip/pull/3481)
`фикс` · Задачи и согласования · автор @outlawmold · балл **78.0** · 180+17 строк · — дн. · CI: red
  - ✗ конфликт с основной веткой и взятыми PR: package.json, execute.ts, test.ts
  - ✗ код не совпадает с описанием (0.03)
  - ! падают тесты CI: policy
  - ! лишние изменения в дифе
  - + серьёзный баг в обычной работе (вред 0.67, частота 0.87)
  - + прямо про ваше использование (2.81/3)

**#8447** [feat(inbox): surface pending agent→human asks as "Waiting on you"](https://github.com/paperclipai/paperclip/pull/8447)
`фича` · Интерфейс · автор @Tr1ckyMag1ca1 · балл **77.9** · 567+11 строк · — дн. · CI: red
  - ✗ конфликт с основной веткой и взятыми PR: constants.ts, index.ts, inbox-dismissals.ts
  - ! падают тесты CI: Verify serialized server suites (2/4)
  - ! фича меняет поведение по умолчанию
  - + сильная фича (ценность 3.1/4, новизна 0.85)
  - + прямо про ваше использование (2.6/3)

**#7002** [feat(claude-local): load per-agent .env on spawn (JDD-133)](https://github.com/paperclipai/paperclip/pull/7002)
`фича` · Claude-адаптер · автор @gabi-JD · балл **77.9** · 502+12 строк · — дн. · CI: red
  - ✗ конфликт с основной веткой и взятыми PR: package.json, execute.ts, index.ts
  - ! фича полезная, но не ключевая
  - ! падают тесты CI: verify, policy
  - + прямо про ваше использование (2.93/3)

**#12738** [fix(interactions): raise custom target key limit and tolerate unparseable stored payloads in scans](https://github.com/paperclipai/paperclip/pull/12738)
`фикс` · Задачи и согласования · автор @EbrahimProgrammer · балл **77.7** · 66+5 строк · — дн. · CI: red
  - ✗ конфликт с основной веткой и взятыми PR: issue.ts, issue-thread-interactions.ts
  - ! баг не критичный или редкий
  - ! падают тесты CI: ci / verify, ci / General tests (server (3/5))
  - + прямо про ваше использование (2.72/3)

**#8972** [feat(approvals): require a reason or explicit force when rejecting](https://github.com/paperclipai/paperclip/pull/8972)
`фича` · Задачи и согласования · автор @souravsachin · балл **77.6** · 402+10 строк · — дн. · CI: green
  - ✗ конфликт с основной веткой и взятыми PR: Approvals.tsx
  - ! фича меняет поведение по умолчанию
  - + сильная фича (ценность 3.07/4, новизна 0.85)
  - + прямо про ваше использование (2.56/3)

**#6426** [feat: estimateSubscriptionSpendCents for claude-local (RFC #5066)](https://github.com/paperclipai/paperclip/pull/6426)
`фича` · Claude-адаптер · автор @Jolley71717 · балл **77.6** · 314+5 строк · — дн. · CI: green
  - ✗ конфликт с основной веткой и взятыми PR: index.ts, execute.ts, heartbeat.ts
  - ! фича полезная, но не ключевая
  - + прямо про ваше использование (2.85/3)

**#13926** [fix: allow taskless runs to update their assigned issues](https://github.com/paperclipai/paperclip/pull/13926)
`фикс` · Задачи и согласования · автор @wyi184246-creator · балл **77.5** · 415+25 строк · — дн. · CI: green
  - ✗ код не совпадает с описанием (0.43)
  - ! рискованная область (0.51)
  - + серьёзный баг в обычной работе (вред 0.84, частота 0.71)
  - + прямо про ваше использование (2.8/3)

**#6663** [fix(redaction): redact value-based secret patterns in compactRunLogChunk](https://github.com/paperclipai/paperclip/pull/6663)
`безопасность` · Запуски и heartbeat · автор @PAT-Main · балл **77.3** · 93+1 строк · — дн. · CI: green
  - ✗ конфликт с основной веткой и взятыми PR: heartbeat.ts
  - + серьёзный баг в обычной работе (вред 0.88, частота 0.74)
  - + прямо про ваше использование (2.56/3)

**#8472** [feat(claude-local): --fallback-model so transient 529/overload bumps model instead of failing the run](https://github.com/paperclipai/paperclip/pull/8472)
`фича` · Claude-адаптер · автор @joegalbert-ai · балл **77.3** · 180+0 строк · — дн. · CI: flaky_only
  - ✗ конфликт с основной веткой и взятыми PR: index.ts, execute.ts
  - ! фича меняет поведение по умолчанию
  - + сильная фича (ценность 3.01/4, новизна 0.77)
  - + прямо про ваше использование (2.63/3)

**#12534** [fix(acpx-engine): materialize Claude runtime skills into project cwd](https://github.com/paperclipai/paperclip/pull/12534)
`фикс` · Claude-адаптер · автор @Danne-J · балл **77.2** · 206+37 строк · — дн. · CI: flaky_only
  - ✗ конфликт с основной веткой и взятыми PR: execute.ts, server-utils.ts
  - + серьёзный баг в обычной работе (вред 0.8, частота 0.63)
  - + прямо про ваше использование (2.75/3)

**#12287** [fix(codex-local): write http_headers so codex sends the MCP gateway bearer token](https://github.com/paperclipai/paperclip/pull/12287)
`фикс` · Codex-адаптер · автор @zannis · балл **77.0** · 6+2 строк · — дн. · CI: green
  - ✗ конфликт с основной веткой и взятыми PR: codex-home.test.ts
  - + серьёзный баг в обычной работе (вред 0.75, частота 0.79)
  - + прямо про ваше использование (2.8/3)

**#13052** [feat(audit): add run-recall search over runs and activity](https://github.com/paperclipai/paperclip/pull/13052)
`фича` · Запуски и heartbeat · автор @tejasghalsasi · балл **76.9** · 980+15 строк · — дн. · CI: flaky_only
  - ✗ конфликт с основной веткой и взятыми PR: heartbeats.ts
  - + сильная фича (ценность 3.17/4, новизна 0.88)

**#10547** [fix(shared,server): treat error as non-invokable across agent lifecycle](https://github.com/paperclipai/paperclip/pull/10547)
`фикс` · Запуски и heartbeat · автор @santhiprakash · балл **76.9** · 42+8 строк · — дн. · CI: green
  - ✗ конфликт с основной веткой и взятыми PR: issues.ts
  - ✗ код не совпадает с описанием (0.29)
  - ! баг не критичный или редкий
  - + прямо про ваше использование (2.75/3)

**#11413** [fix(recovery): retry transient adapter failures on a monitor instead of blocking](https://github.com/paperclipai/paperclip/pull/11413)
`фикс` · Запуски и heartbeat · автор @dzianisv · балл **76.9** · 496+39 строк · — дн. · CI: green
  - ✗ конфликт с основной веткой и взятыми PR: heartbeat.ts, service.ts
  - + серьёзный баг в обычной работе (вред 0.88, частота 0.72)
  - + прямо про ваше использование (2.72/3)

**#4473** [fix(db): add ON DELETE rules to issue-related foreign keys](https://github.com/paperclipai/paperclip/pull/4473)
`фикс` · Задачи и согласования · автор @alexlomt · балл **76.9** · 191+6 строк · — дн. · CI: green
  - ✗ конфликт с основной веткой и взятыми PR: client.test.ts, _journal.json
  - ! рискованная область (0.58)
  - + серьёзный баг в обычной работе (вред 0.91, частота 0.85)
  - + прямо про ваше использование (2.77/3)

**#3917** [Add waiting_on_human_gate state and Human Gate behavior to lead agent prompts](https://github.com/paperclipai/paperclip/pull/3917)
`фича` · Задачи и согласования · автор @zjoh5253 · балл **76.9** · 55+3 строк · — дн. · CI: green
  - ✗ конфликт с основной веткой и взятыми PR: AGENTS.md, StatusIcon.tsx, issue-filters.ts
  - + сильная фича (ценность 3.7/4, новизна 0.72)
  - + прямо про ваше использование (2.63/3)

**#12611** [fix(tool-gateway): stop mapping application-level tools/call errors to raw HTTP 404/400 on the named MCP gateway](https://github.com/paperclipai/paperclip/pull/12611)
`фикс` · Коннекторы и MCP · автор @Quentin-M · балл **76.8** · 94+1 строк · — дн. · CI: flaky_only
  - ✗ конфликт с основной веткой и взятыми PR: tool-gateway.ts
  - ! баг не критичный или редкий
  - + прямо про ваше использование (2.86/3)

**#13897** [fix(claude-local): enforce deny-first tools by agent role (SOL-3188 Step 1)](https://github.com/paperclipai/paperclip/pull/13897)
`безопасность` · Claude-адаптер · автор @yackovleff-solved · балл **76.7** · 66+4 строк · — дн. · CI: flaky_only
  - ✗ конфликт с основной веткой и взятыми PR: index.ts, permissions.test.ts, permissions.ts
  - ! рискованная область (0.74)
  - + серьёзный баг в обычной работе (вред 0.94, частота 0.71)
  - + прямо про ваше использование (2.96/3)

**#5468** [feat: multi-select issues with batch actions in list view (LAC-459)](https://github.com/paperclipai/paperclip/pull/5468)
`фича` · Задачи и согласования · автор @lacymorrow · балл **76.7** · 844+4 строк · — дн. · CI: green
  - ✗ конфликт с основной веткой и взятыми PR: issues.ts, issues.ts, IssuesList.tsx
  - + сильная фича (ценность 3.46/4, новизна 0.89)

**#3823** [fix: include server port in derived auth trusted origins](https://github.com/paperclipai/paperclip/pull/3823)
`фикс` · AI-подключения и доступ · автор @Helmi · балл **76.7** · 147+2 строк · — дн. · CI: green
  - ✗ конфликт с основной веткой и взятыми PR: better-auth.ts
  - + серьёзный баг в обычной работе (вред 0.84, частота 0.72)
  - + прямо про ваше использование (2.95/3)

**#13467** [fix(claude-local): use --append-system-prompt instead of unsupported -file flag](https://github.com/paperclipai/paperclip/pull/13467)
`фикс` · Claude-адаптер · автор @arnaud-gp · балл **76.6** · 36+37 строк · — дн. · CI: flaky_only
  - ✗ конфликт с основной веткой и взятыми PR: execute.remote.test.ts
  - ! баг не критичный или редкий
  - + прямо про ваше использование (2.74/3)

**#10616** [fix(recovery): recognize provider quota exhaustion on the ACP path](https://github.com/paperclipai/paperclip/pull/10616)
`фикс` · Запуски и heartbeat · автор @MrBlackTongue · балл **76.5** · 716+232 строк · — дн. · CI: green
  - ✗ конфликт с основной веткой и взятыми PR: execute.ts, parse.ts, provider-failure-classification.test.ts
  - ! баг не критичный или редкий
  - + прямо про ваше использование (2.88/3)

**#11623** [fix(recovery): stop terminal-run recovery from stranding, flapping, and destroying live monitors](https://github.com/paperclipai/paperclip/pull/11623)
`фикс` · Запуски и heartbeat · автор @dzianisv · балл **76.5** · 593+3 строк · — дн. · CI: flaky_only
  - ✗ конфликт с основной веткой и взятыми PR: service.ts
  - + серьёзный баг в обычной работе (вред 0.85, частота 0.6)
  - + прямо про ваше использование (2.88/3)

**#11121** [fix(adapter-utils): authenticate the wake payload so agents can trust it](https://github.com/paperclipai/paperclip/pull/11121)
`безопасность` · Запуски и heartbeat · автор @Nissimmiracles · балл **76.4** · 186+9 строк · — дн. · CI: green
  - ✗ конфликт с основной веткой и взятыми PR: server-utils.test.ts, server-utils.ts, execute.ts
  - ! рискованная область (0.61)
  - + серьёзный баг в обычной работе (вред 0.85, частота 0.83)
  - + прямо про ваше использование (2.96/3)

**#7415** [Enforce heartbeat cooldown on automatic agent wakeups](https://github.com/paperclipai/paperclip/pull/7415)
`фича` · Запуски и heartbeat · автор @alejandroiglesias · балл **76.4** · 777+31 строк · — дн. · CI: flaky_only
  - ✗ конфликт с основной веткой и взятыми PR: index.ts, agent.ts, index.ts
  - + сильная фича (ценность 3.04/4, новизна 0.71)
  - + прямо про ваше использование (2.7/3)

**#13812** [feat(apps): add Glasser as a self-serve MCP connection](https://github.com/paperclipai/paperclip/pull/13812)
`фича` · Коннекторы и MCP · автор @glasserai · балл **76.3** · 171+19 строк · — дн. · CI: green
  - ✗ конфликт с основной веткой и взятыми PR: app-definitions.generated.ts, app-definitions.test.ts, ingest-app-definitions.mjs
  - ✗ продвигает сторонний сервис (0.91)
  - + сильная фича (ценность 3.35/4, новизна 0.76)


## Не дошли до этапа 2 — только балл этапа 1, вердикта нет (2869)

**#11506** [fix: wake requesting agent when approval card is rejected](https://github.com/paperclipai/paperclip/pull/11506)
`фикс` · Задачи и согласования · автор @rotem-zecharia · балл **76.2** · 403+22 строк · — дн. · CI: —

**#9293** [feat(issues): add trigger date to defer agent work until a scheduled time](https://github.com/paperclipai/paperclip/pull/9293)
`фича` · Задачи и согласования · автор @lacymorrow · балл **76.2** · 291+3 строк · — дн. · CI: —

**#5784** [Fix DB backup rotation ENOSPC (per-day daily-tier coalesce + free-space guard)](https://github.com/paperclipai/paperclip/pull/5784)
`фикс` · Деплой и self-host · автор @imvimm · балл **76.1** · 305+25 строк · — дн. · CI: —

**#8919** [fix(issues): same-agent stale checkout release/adopt across run boundary](https://github.com/paperclipai/paperclip/pull/8919)
`фикс` · Задачи и согласования · автор @florianpollstaetter-dot · балл **76.1** · 224+32 строк · — дн. · CI: —

**#3910** [fix(issues): slug-mention resolver + UUID validation for @agent wakes](https://github.com/paperclipai/paperclip/pull/3910)
`фикс` · Задачи и согласования · автор @kbecking · балл **76.1** · 677+13 строк · — дн. · CI: —

**#13028** [fix(claude-local): do not treat a background-task notification as a finished turn](https://github.com/paperclipai/paperclip/pull/13028)
`фикс` · Claude-адаптер · автор @MrBlackTongue · балл **76.0** · 85+1 строк · — дн. · CI: —

**#9306** [feat(config): attribution.commit/pr opt-out for the Paperclip co-author trailer](https://github.com/paperclipai/paperclip/pull/9306)
`фича` · Коннекторы и MCP · автор @lacymorrow · балл **76.0** · 640+30 строк · — дн. · CI: —

**#9073** [fix(issues): reject unknown monitor policy fields instead of silently dropping them](https://github.com/paperclipai/paperclip/pull/9073)
`фикс` · Задачи и согласования · автор @dosthcpp · балл **76.0** · 133+1 строк · — дн. · CI: —

**#13924** [fix(ai-connections): rotate Claude subscription credentials from a file](https://github.com/paperclipai/paperclip/pull/13924)
`фикс` · AI-подключения и доступ · автор @danmoc-88 · балл **75.9** · 153+19 строк · — дн. · CI: —

**#13685** [fix(heartbeat): stop electing a sibling workspace's cwd for a run that named another](https://github.com/paperclipai/paperclip/pull/13685)
`фикс` · Воркспейсы и git · автор @simberthon · балл **75.9** · 818+39 строк · — дн. · CI: —

**#13659** [fix(issues): auto-assign issue to creating agent when assigneeAgentId missing (INUA-7276)](https://github.com/paperclipai/paperclip/pull/13659)
`фикс` · Задачи и согласования · автор @rotem-zecharia · балл **75.9** · 194+1 строк · — дн. · CI: —

**#9212** [feat(server): return childIssues array from GET /api/issues/{id}](https://github.com/paperclipai/paperclip/pull/9212)
`фича` · Задачи и согласования · автор @calebsimon-CRAFT · балл **75.9** · 114+8 строк · — дн. · CI: —

**#13650** [fix(server): let a heartbeat run write to the issue it checked out](https://github.com/paperclipai/paperclip/pull/13650)
`фикс` · Задачи и согласования · автор @Abel-Salah · балл **75.8** · 549+28 строк · — дн. · CI: —

**#13644** [fix(acpx-engine): classify a provider quota wall as a quota wait](https://github.com/paperclipai/paperclip/pull/13644)
`фикс` · Claude-адаптер · автор @Siber704 · балл **75.8** · 62+3 строк · — дн. · CI: —

**#9280** [perf(server): cut auth middleware DB round-trips and make db pool size configurable](https://github.com/paperclipai/paperclip/pull/9280)
`перф` · AI-подключения и доступ · автор @lacymorrow · балл **75.8** · 286+48 строк · — дн. · CI: —

**#3131** [fix(adapters/process): inject PAPERCLIP_RUN_ID + PAPERCLIP_API_KEY into spawned env](https://github.com/paperclipai/paperclip/pull/3131)
`фикс` · Другие адаптеры · автор @iws17 · балл **75.8** · 163+1 строк · — дн. · CI: —

**#3937** [feat(claude-local): add xhigh and max thinking effort options](https://github.com/paperclipai/paperclip/pull/3937)
`фича` · Claude-адаптер · автор @GodsBoy · балл **75.7** · 85+1 строк · — дн. · CI: —

**#9871** [feat: inject GITHUB_TOKEN auth header in ghFetch](https://github.com/paperclipai/paperclip/pull/9871)
`фича` · Деплой и self-host · автор @uw-ssec-bot · балл **75.7** · 130+1 строк · — дн. · CI: —

**#14012** [fix(heartbeat): bind run-scoped runtime gateways to their agent](https://github.com/paperclipai/paperclip/pull/14012)
`безопасность` · Запуски и heartbeat · автор @busla · балл **75.6** · 134+0 строк · — дн. · CI: —

**#13700** [fix: preserve shell arguments in native SSH execution](https://github.com/paperclipai/paperclip/pull/13700)
`фикс` · Codex-адаптер · автор @Jp121987 · балл **75.6** · 83+10 строк · — дн. · CI: —

**#11747** [feat(issues): add staleHours filter to issue list route](https://github.com/paperclipai/paperclip/pull/11747)
`фича` · Задачи и согласования · автор @dzianisv · балл **75.6** · 318+1 строк · — дн. · CI: —

**#10081** [feat(server): include scoped project and milestone intake in wake payload](https://github.com/paperclipai/paperclip/pull/10081)
`фича` · Запуски и heartbeat · автор @Joshtt23 · балл **75.6** · 887+15 строк · — дн. · CI: —

**#7724** [fix(security): redact transcript artifacts before persistence](https://github.com/paperclipai/paperclip/pull/7724)
`безопасность` · Codex-адаптер · автор @misterbusiness1 · балл **75.6** · 425+4 строк · — дн. · CI: —

**#11797** [fix(adapter-utils): block server-only credentials at all agent spawns](https://github.com/paperclipai/paperclip/pull/11797)
`безопасность` · Другие адаптеры · автор @nearfolk · балл **75.5** · 267+27 строк · — дн. · CI: —

**#13883** [fix(recovery): give fresh runs a grace period before the issue-terminal sweep](https://github.com/paperclipai/paperclip/pull/13883)
`фикс` · Запуски и heartbeat · автор @Sergio-LPA · балл **75.4** · 175+7 строк · — дн. · CI: —

**#14005** [fix(server): allow a same-write blocker clear past the blocked-status guard](https://github.com/paperclipai/paperclip/pull/14005)
`фикс` · Задачи и согласования · автор @msoukhomlinov · балл **75.2** · 235+25 строк · — дн. · CI: —

**#13469** [perf(workspaces): stop paying for unused Git scans in the terminal reaper](https://github.com/paperclipai/paperclip/pull/13469)
`перф` · Воркспейсы и git · автор @fayonation · балл **75.2** · 320+17 строк · — дн. · CI: —

**#13271** [fix: preserve active runs through terminal issue writes](https://github.com/paperclipai/paperclip/pull/13271)
`фикс` · Задачи и согласования · автор @briscocom · балл **75.2** · 446+118 строк · — дн. · CI: —

**#4003** [fix(adapter-utils): non-blocking onLog in runChildProcess](https://github.com/paperclipai/paperclip/pull/4003)
`фикс` · Другие адаптеры · автор @ericnicolaides · балл **75.2** · 56+8 строк · — дн. · CI: —

**#3284** [fix(issues): use resolved UUID instead of identifier in wakeup payloads](https://github.com/paperclipai/paperclip/pull/3284)
`фикс` · Задачи и согласования · автор @kbecking · балл **75.1** · 9+9 строк · — дн. · CI: —


# Issues: 2467 открытых, 2070 без единого PR

## Важное, на что PR нет

**#12334** [Email/password sign-in broken: better-auth 1.7.0 bump requires account.issuer column that schema/migrations never added](https://github.com/paperclipai/paperclip/issues/12334) — балл **96.2**, `Баг`, серьёзность 3.99/4, частота 0.94, релевантность 2.97/3, 1 комм. · @lsimpsonsfdc · обновлено 2026-08-27

**#10056** [shouldWakeAssigneeOnCheckout re-arms on its own completion comment, causing an unbounded self-sustaining wake loop](https://github.com/paperclipai/paperclip/issues/10056) — балл **92.9**, `Баг`, серьёзность 3.88/4, частота 0.9, релевантность 2.86/3, 0 комм. · @gracejudy · обновлено 2026-07-23

**#8047** [Run transcripts persist raw secret values to run logs, heartbeat_runs, and backups — redact bound secret values at the transcript writer](https://github.com/paperclipai/paperclip/issues/8047) — балл **92.3**, `Безопасность`, серьёзность 4/4, частота 0.9, релевантность 2.94/3, 8 комм. · @belousov-petr · обновлено 2026-09-27

**#5423** [buildRunOutputSilence called on heartbeatService but only exported from recoveryService — /live-runs returns 500](https://github.com/paperclipai/paperclip/issues/5423) — балл **91.5**, `Баг`, серьёзность 3.85/4, частота 0.91, релевантность 2.73/3, 0 комм. · @kimparrot · обновлено 2026-05-07

**#1825** [Memory leak: pino-pretty file transport ThreadStream buffer grows unbounded, OOMs every ~60min](https://github.com/paperclipai/paperclip/issues/1825) — балл **91.4**, `Падение/данные`, серьёзность 4/4, частота 0.8, релевантность 2.93/3, 4 комм. · @atd93 · обновлено 2026-07-10

**#3517** [mcp-server: tool names have double prefix mcp_paperclip_paperclipXxx](https://github.com/paperclipai/paperclip/issues/3517) — балл **91.4**, `Баг`, серьёзность 3.66/4, частота 0.93, релевантность 2.94/3, 2 комм. · @Daradaal · обновлено 2026-04-18

**#2554** [Security: Multiple Critical Vulnerabilities in Default Configuration (Hardcoded Secret, Disabled Sandbox, JWT Replay, SSRF)](https://github.com/paperclipai/paperclip/issues/2554) — балл **90.9**, `Безопасность`, серьёзность 3.99/4, частота 0.86, релевантность 2.94/3, 0 комм. · @joergmichno · обновлено 2026-04-02

**#6128** [Agents with secret_ref env entries break after v2026.512.0 — migration 0082_dry_vision doesn't backfill company_secret_bindings](https://github.com/paperclipai/paperclip/issues/6128) — балл **90.5**, `Баг`, серьёзность 3.98/4, частота 0.75, релевантность 2.96/3, 3 комм. · @belousov-petr · обновлено 2026-08-30

**#2684** [Frontend stuck on 'Loading...' when session expires or WebSocket disconnects — no redirect to /login](https://github.com/paperclipai/paperclip/issues/2684) — балл **90.4**, `Баг`, серьёзность 3.88/4, частота 0.82, релевантность 2.9/3, 1 комм. · @goodcomex · обновлено 2026-04-04

**#10499** [New Project dialog never collects repoRef, causing WorkspaceValidationFailure on every isolated_workspace/git_worktree run](https://github.com/paperclipai/paperclip/issues/10499) — балл **90.2**, `Баг`, серьёзность 3.95/4, частота 0.81, релевантность 2.89/3, 0 комм. · @iamdavidmichaelmoore · обновлено 2026-07-30

**#13805** [Anthropic subscription connections die within hours: capture keeps only the short-lived access token, and the refresh write-back never runs for Anthropic](https://github.com/paperclipai/paperclip/issues/13805) — балл **89.9**, `Баг`, серьёзность 3.88/4, частота 0.75, релевантность 2.99/3, 2 комм. · @AutomatonHub · обновлено 2026-09-27

**#6728** [bug: cost_events.cost_cents = 0 for billing_type = subscription_included — budget gates not firing](https://github.com/paperclipai/paperclip/issues/6728) — балл **89.8**, `Баг`, серьёзность 3.88/4, частота 0.91, релевантность 2.89/3, 1 комм. · @troykelly · обновлено 2026-09-11

**#13081** [Bare wakeCommentId bypasses the terminal-status gate: a closeout comment can revive a done/cancelled issue (policy.ts:546)](https://github.com/paperclipai/paperclip/issues/13081) — балл **89.7**, `Баг`, серьёзность 3.91/4, частота 0.84, релевантность 2.83/3, 0 комм. · @dvt-tnf · обновлено 2026-09-09

**#8163** [GET /api/issues/{id}/comments → 500: enrichCommentsWithDerivedAgentAttribution binds Date objects to postgres-js](https://github.com/paperclipai/paperclip/issues/8163) — балл **89.6**, `Баг`, серьёзность 3.83/4, частота 0.83, релевантность 2.75/3, 0 комм. · @MINECUMN · обновлено 2026-06-15

**#4050** [LatestRunCard violates rules-of-hooks → React #310 on agent detail page](https://github.com/paperclipai/paperclip/issues/4050) — балл **89.5**, `Баг`, серьёзность 3.78/4, частота 0.89, релевантность 2.7/3, 1 комм. · @SergeK76 · обновлено 2026-04-19

**#2730** [Issue routing is permanently locked at creation — tickets cannot be reassigned or handed off](https://github.com/paperclipai/paperclip/issues/2730) — балл **89.5**, `Баг`, серьёзность 3.98/4, частота 0.92, релевантность 2.96/3, 1 комм. · @ttomiczek · обновлено 2026-04-04

**#13371** [Runtime gateway tokens (pcgw_) fail verification on the gateway MCP route, so installed apps never reach claude_local runs (2026.831.1)](https://github.com/paperclipai/paperclip/issues/13371) — балл **89.4**, `Баг`, серьёзность 3.94/4, частота 0.83, релевантность 2.96/3, 0 комм. · @Octember · обновлено 2026-09-13

**#4019** [Sub-issues don't inherit parent's projectId — breaks agent execution](https://github.com/paperclipai/paperclip/issues/4019) — балл **89.2**, `Баг`, серьёзность 3.92/4, частота 0.82, релевантность 2.84/3, 1 комм. · @ming0627 · обновлено 2026-04-19

**#13431** [hire_agent approval reads payload fields at wrong nesting level — creates blank, budget-uncapped agent instead of applying the proposed hire](https://github.com/paperclipai/paperclip/issues/13431) — балл **88.9**, `Баг`, серьёзность 3.9/4, частота 0.73, релевантность 2.9/3, 0 комм. · @gauravkhapekar · обновлено 2026-09-14

**#8765** [git-workspace-sync: 'dubious ownership' abort in sandbox pods when /tmp uid != process uid](https://github.com/paperclipai/paperclip/issues/8765) — балл **88.9**, `Баг`, серьёзность 3.95/4, частота 0.83, релевантность 2.72/3, 1 комм. · @Aurelian-Shuttleworth · обновлено 2026-06-29

**#9893** [[bug] codex_local adapter passes --dangerously-bypass-approvals-and-sandbox twice, all codex_local runs abort](https://github.com/paperclipai/paperclip/issues/9893) — балл **88.8**, `Баг`, серьёзность 3.91/4, частота 0.91, релевантность 2.65/3, 1 комм. · @jonguttman · обновлено 2026-08-05

**#13956** [Task comment composer never sends: no request reaches the server (open and closed tasks), board user, v2026.916.1](https://github.com/paperclipai/paperclip/issues/13956) — балл **88.5**, `Баг`, серьёзность 3.84/4, частота 0.83, релевантность 2.91/3, 0 комм. · @mha33 · обновлено 2026-09-24

**#12731** [Issue creation silently binds new issues to the creating run's execution workspace, overriding the project's `isolated_workspace` policy](https://github.com/paperclipai/paperclip/issues/12731) — балл **88.4**, `Баг`, серьёзность 3.9/4, частота 0.88, релевантность 2.79/3, 1 комм. · @Waseemilyas · обновлено 2026-09-10

**#5042** [claude_local adapter uses CLI flags + model IDs that don't exist in public Claude Code 2.0.30](https://github.com/paperclipai/paperclip/issues/5042) — балл **88.2**, `Баг`, серьёзность 3.8/4, частота 0.71, релевантность 2.97/3, 2 комм. · @ajantoniou · обновлено 2026-06-23

**#5810** [500 on GET /api/issues/:id/comments — Date passed to postgres driver as string in heartbeat_runs query (2026.512.0)](https://github.com/paperclipai/paperclip/issues/5810) — балл **88.1**, `Баг`, серьёзность 3.67/4, частота 0.83, релевантность 2.76/3, 2 комм. · @aduduman031084 · обновлено 2026-05-13

**#14144** [adapterConfig (model selection) set at hire time or via PATCH is not persisted / not returned by GET](https://github.com/paperclipai/paperclip/issues/14144) — балл **88.0**, `Баг`, серьёзность 3.65/4, частота 0.85, релевантность 2.94/3, 1 комм. · @peachiia · обновлено 2026-09-26

**#12686** [Agent's own terminal-status PATCH returns 403, stranding issues as blocked](https://github.com/paperclipai/paperclip/issues/12686) — балл **88.0**, `Баг`, серьёзность 3.86/4, частота 0.73, релевантность 2.92/3, 1 комм. · @matt-palmetto · обновлено 2026-09-02

**#13808** [0.3.1: runs not de-duplicated per issue, and terminalized runs leak active environment_leases that permanently block issue wakes](https://github.com/paperclipai/paperclip/issues/13808) — балл **87.9**, `Баг`, серьёзность 3.96/4, частота 0.68, релевантность 2.92/3, 4 комм. · @msoukhomlinov · обновлено 2026-09-27

**#3409** [Secrets master key path mismatch causes secrets to become undecryptable on Docker container recreation](https://github.com/paperclipai/paperclip/issues/3409) — балл **87.7**, `Баг`, серьёзность 3.93/4, частота 0.67, релевантность 2.97/3, 3 комм. · @AndersLundDK · обновлено 2026-07-20

**#13661** [valuesForIssue Seq Scans all of heartbeat_runs on every issue read: unindexed second branch of the OR costs 5.3 s per call (5306 ms -> 0.19 ms with the missing index)](https://github.com/paperclipai/paperclip/issues/13661) — балл **87.6**, `Производительность`, серьёзность 3.73/4, частота 0.78, релевантность 2.81/3, 1 комм. · @simberthon · обновлено 2026-09-22

**#4697** [[Bug] executionRunId Zombie Lock — Cannot Be Cleared via Any API, Requires Manual DB Intervention](https://github.com/paperclipai/paperclip/issues/4697) — балл **87.4**, `Баг`, серьёзность 3.97/4, частота 0.82, релевантность 2.95/3, 1 комм. · @almadigitalsystems · обновлено 2026-06-10

**#437** [Agent runs fail due to server restarts, missing claude PATH, and stale JWTs](https://github.com/paperclipai/paperclip/issues/437) — балл **87.2**, `Баг`, серьёзность 3.98/4, частота 0.69, релевантность 2.89/3, 3 комм. · @vlad-tsoy · обновлено 2026-03-16

**#5568** [npm audit advisories in stable/canary Paperclip packages](https://github.com/paperclipai/paperclip/issues/5568) — балл **87.1**, `Безопасность`, серьёзность 3.95/4, частота 0.71, релевантность 2.97/3, 0 комм. · @AnobleSCM · обновлено 2026-05-09

**#10714** [Change-consent gate binds an accepted `request_confirmation` to a target key, not to the approved content](https://github.com/paperclipai/paperclip/issues/10714) — балл **87.0**, `Безопасность`, серьёзность 3.99/4, частота 0.78, релевантность 2.72/3, 0 комм. · @antiautomation · обновлено 2026-08-02

**#6483** [Adapter should pass --setting-sources=user so ~/.claude/settings.json hooks load under claude_local](https://github.com/paperclipai/paperclip/issues/6483) — балл **87.0**, `Баг`, серьёзность 3.7/4, частота 0.79, релевантность 2.9/3, 0 комм. · @zenfire-paperclip-bot · обновлено 2026-05-21

**#3552** [Agent instructions editor does not save input (AGENTS.md)](https://github.com/paperclipai/paperclip/issues/3552) — балл **87.0**, `Баг`, серьёзность 3.92/4, частота 0.83, релевантность 2.88/3, 4 комм. · @MHoener69 · обновлено 2026-04-18

**#13616** [Workspace lifecycle: completion-time worktree teardown fails the finishing run; isolated_workspace shared across issues; two board-interaction defects (self-hosted 0.3.1)](https://github.com/paperclipai/paperclip/issues/13616) — балл **86.8**, `Баг`, серьёзность 3.88/4, частота 0.84, релевантность 2.98/3, 0 комм. · @jayesh291 · обновлено 2026-09-18

**#14164** [`serialize` does not protect a reused isolated worktree — the holder gate is skipped for every issue whose resolved mode is `isolated_workspace`](https://github.com/paperclipai/paperclip/issues/14164) — балл **86.7**, `Баг`, серьёзность 3.85/4, частота 0.82, релевантность 2.69/3, 0 комм. · @Xkonti · обновлено 2026-09-26

**#2912** [Stale execution locks not released on cancelled/failed/timed-out runs](https://github.com/paperclipai/paperclip/issues/2912) — балл **86.3**, `Баг`, серьёзность 3.44/4, частота 0.81, релевантность 2.91/3, 1 комм. · @cryptulien · обновлено 2026-05-07

**#12029** [2026.817.0 sandbox callback bridge allowlist omits hiring routes documented by bundled paperclip-create-agent skill](https://github.com/paperclipai/paperclip/issues/12029) — балл **86.2**, `Баг`, серьёзность 3.64/4, частота 0.76, релевантность 2.88/3, 0 комм. · @dam-sec-paperclip · обновлено 2026-08-23


## Issues, которые уже кто-то закрывает открытым PR (397)

**#13960** ensureManagedProjectWorkspace compares repo URLs without normalizing `.git`, so it clones a phantom checkout and fails every git_worktree run — балл 77.8, PR: [#14015](https://github.com/paperclipai/paperclip/pull/14015)

**#4759** Security: HTTP logger leaks plaintext passwords (and other secrets) in reqBody on 4xx responses — балл 77.0, PR: [#10467](https://github.com/paperclipai/paperclip/pull/10467)

**#9976** heartbeat: session config fingerprint invalidated by issue/project updatedAt churn, and misses trust-preset/workspace-identity drift — балл 74.7, PR: [#9977](https://github.com/paperclipai/paperclip/pull/9977)

**#13725** Claude subscription connections stop working about 8 hours after sign-in and cannot refresh — балл 73.8, PR: [#13726](https://github.com/paperclipai/paperclip/pull/13726)

**#2755** Security: Cross-agent prompt injection via session handoff content — балл 73.4, PR: [#2779](https://github.com/paperclipai/paperclip/pull/2779)

**#13822** contextSnapshot.issueId is never updated after wake, so POST /issues/:id/checkout cannot grant an agent write access to the issue it just checked out — балл 72.9, PR: [#14229](https://github.com/paperclipai/paperclip/pull/14229)

**#14023** Agent bound to a Claude subscription AI connection can never be unbound: env CLAUDE_CODE_OAUTH_TOKEN is stripped and edits 422 once the token expires (wizard's first agent is stuck) — балл 72.4, PR: [#14027](https://github.com/paperclipai/paperclip/pull/14027)

**#12118** Timer-heartbeat runs get 403 cross_issue_influence_run_context_required on every issue write, including their own issue — stated remedy is unachievable — балл 72.3, PR: [#12532](https://github.com/paperclipai/paperclip/pull/12532), [#13650](https://github.com/paperclipai/paperclip/pull/13650), [#13833](https://github.com/paperclipai/paperclip/pull/13833)

**#10195** Deferred stage-handoff wakes starve behind stale deferred wakes: review handoffs never fire until unrelated issue activity — балл 71.9, PR: [#10199](https://github.com/paperclipai/paperclip/pull/10199)

**#11037** Command redaction produces invalid JSON in run logs (consumes the escaping backslash) — балл 71.6, PR: [#12530](https://github.com/paperclipai/paperclip/pull/12530)

**#12413** serialize is silently not applied when an issue has no projectWorkspaceId: concurrent runs enter the shared git checkout with no deferral and no warning — балл 71.0, PR: [#12554](https://github.com/paperclipai/paperclip/pull/12554)

**#7040** opencode-local adapter drops plugin and other fields from opencode.jsonc when creating runtime config — балл 70.9, PR: [#7354](https://github.com/paperclipai/paperclip/pull/7354)

**#13730** PATCH /api/issues/{id} cancels the caller's own run when an agent reassigns its own issue (2026.916.0) — балл 70.7, PR: [#13782](https://github.com/paperclipai/paperclip/pull/13782)

**#12633** Composio broker connections never leave draft status — every child toolkit's tools are invisible to the tool gateway — балл 70.4, PR: [#12634](https://github.com/paperclipai/paperclip/pull/12634)

**#8690** fix(server): checkout flips in_review → in_progress when expectedStatuses includes in_review — балл 70.2, PR: [#8712](https://github.com/paperclipai/paperclip/pull/8712)

**#2925** [Bug] agents.api_key column should be UNIQUE — shared keys cause identity collision — балл 70.0, PR: [#3240](https://github.com/paperclipai/paperclip/pull/3240)

**#7755** [Bug] EPIPE crash in adapter-utils server-utils.js:1687 — unhandled Socket error on stdin.write after pipe close — балл 69.8, PR: [#7757](https://github.com/paperclipai/paperclip/pull/7757), [#12324](https://github.com/paperclipai/paperclip/pull/12324), [#14057](https://github.com/paperclipai/paperclip/pull/14057)

**#1063** Bug: startNextQueuedRunForAgent executes queued runs for paused agents — no pause guard on queue drain — балл 69.6, PR: [#1067](https://github.com/paperclipai/paperclip/pull/1067)

**#10344** Recovery misclassifies Claude session/weekly-limit failures as stuck work, minting permanent `blocked` issues instead of using the existing provider-quota wait — балл 69.5, PR: [#13148](https://github.com/paperclipai/paperclip/pull/13148)

**#958** Slow UI - Critical memory leak and UI freeze from unpaginated heartbeat runs — балл 69.3, PR: [#7311](https://github.com/paperclipai/paperclip/pull/7311), [#13560](https://github.com/paperclipai/paperclip/pull/13560)

**#12112** work-product create silently discards unknown keys (z.object strip), so agents report success on lost work — балл 69.3, PR: [#12152](https://github.com/paperclipai/paperclip/pull/12152)

**#9874** clearExecutionRunIfTerminal never reaps a queued-but-never-started heartbeat-run, leaving an unbreakable executionRunId exec-lock on the issue — балл 68.5, PR: [#10449](https://github.com/paperclipai/paperclip/pull/10449), [#10794](https://github.com/paperclipai/paperclip/pull/10794)

**#4543** First-run heartbeat fails: "Agent authentication required" — no agent keys after UI onboarding — балл 68.5, PR: [#4562](https://github.com/paperclipai/paperclip/pull/4562)

**#2671** claude_local adapter does not disable Claude Code auto-memory when para-memory-files skill is active — балл 68.5, PR: [#2722](https://github.com/paperclipai/paperclip/pull/2722)

**#3459** Sub-issues inherit projectWorkspaceId from parent but not projectId — workspace resolution falls back to agent_home — балл 68.2, PR: [#3992](https://github.com/paperclipai/paperclip/pull/3992)


# Форки: проверено 15614, с коммитами впереди upstream — 1851

## Форки, которые стоит разобрать (в них есть работа, не отправленная в upstream)

**[axelweichert/paperclip](https://github.com/axelweichert/paperclip)** — балл **79.4**, `Фича`, впереди 4 коммитов, позади 2041, ±758 строк, ★0, пуш 2026-06-03, ценность 3.39/4, дубль 0.3, секреты 0.14
  - `c2fb522c` 2026-06-03 feat(run-caps): deterministic run-rate/no-progress cap evaluator + constants (WEI-210)
  - `af3dae53` 2026-06-03 feat(heartbeat): pre-run gate enforcing run-caps with board notification (WEI-210)
  - `19ca45b3` 2026-06-03 feat(dashboard): per-agent run-rate + auto-pause panel (WEI-210)
  - `2c9f3289` 2026-06-03 feat(hire): bound maxTurnsPerRun hire-default + document run-caps (WEI-210)

**[SEONGMINY/paperclip](https://github.com/SEONGMINY/paperclip)** — балл **79.0**, `Фича`, впереди 1 коммитов, позади 2841, ±334 строк, ★0, пуш 2026-04-01, ценность 3.72/4, дубль 0.35, секреты 0.15
  - `2cc0a18a` 2026-04-01 feat: codex 세션 전략 추가

**[azibetti/paperclip](https://github.com/azibetti/paperclip)** — балл **76.8**, `Фича`, впереди 6 коммитов, позади 2340, ±1498 строк, ★0, пуш 2026-04-17, ценность 3.85/4, дубль 0.34, секреты 0.14
  - `7ab78736` 2026-04-17 feat: add knowledge management functionality to project details
  - `199b079b` 2026-04-17 feat: enhance issue comment logic to handle automated agent processes
  - `db50acc8` 2026-04-17 fix(e2e): use backlog status for test issue to prevent spurious agent wakeup
  - `360a7313` 2026-04-17 feat: integrate DEFAULT_CLAUDE_LOCAL_MODEL into agent creation and update issue dialog model label
  - `46b42b93` 2026-04-17 feat: add OpenAI API adapter with CLI and UI support

**[siddharthramputty/paperclip](https://github.com/siddharthramputty/paperclip)** — балл **76.4**, `Фича`, впереди 3 коммитов, позади 2408, ±839 строк, ★0, пуш 2026-04-11, ценность 3.32/4, дубль 0.42, секреты 0.1
  - `d947f57b` 2026-04-11 windows: copy instead of symlink in claude-local and codex-local adapters
  - `2c5934bc` 2026-04-11 feat(adapters): add ollama_local in-server adapter
  - `a0910f73` 2026-04-11 Fix gemini_local adapter on Windows and clean up sandbox flag

**[qwlong/paperclip](https://github.com/qwlong/paperclip)** — балл **76.1**, `Фикс`, впереди 16 коммитов, позади 181, ±1595 строк, ★0, пуш 2026-09-15, ценность 2.59/4, дубль 0.51, секреты 0.11
  - `96a883fc` 2026-09-06 fix(claude-local): keep mcpServerIdentity and remoteExecution in the session codec
  - `8577cd96` 2026-09-06 feat(claude-local): gate session resume behind adapterConfig.resumeSessions
  - `42073cde` 2026-09-06 feat(ui): Enter sends in the composer, Shift+Enter is the newline
  - `cf81a633` 2026-09-07 fix(agents): stop non-ASCII names from colliding on a stripped url key
  - `943709ea` 2026-09-07 Merge pull request #1 from qwlong/fix/agent-url-key-non-ascii

**[tim80411/paperclip](https://github.com/tim80411/paperclip)** — балл **76.0**, `Фикс`, впереди 6 коммитов, позади 165, ±917 строк, ★0, пуш 2026-09-16, ценность 2.88/4, дубль 0.67, секреты 0.14
  - `7bab10ab` 2026-07-22 fix(pipelines): return 404 for non-UUID pipeline/case identifiers
  - `4b81bc7d` 2026-07-28 fix(companies): remove() 因外鍵而永遠刪不掉有資料的公司
  - `f1d42009` 2026-07-28 fix(agents): remove() 沒有脫鉤 routine assignee，導致刪 agent 回 500
  - `949c1142` 2026-08-05 fix(quota): Codex 週視窗被貼成「5h limit」——標籤改用回傳的視窗時長
  - `2980d6bf` 2026-08-05 server: honor preset PAPERCLIP_RUNTIME_API_URL during startup

**[NaCl5alt/paperclip](https://github.com/NaCl5alt/paperclip)** — балл **76.0**, `Фича`, впереди 2 коммитов, позади 2079, ±1114 строк, ★0, пуш 2026-09-20, ценность 3.22/4, дубль 0.32, секреты 0.11
  - `98578606` 2026-06-08 [platform/core] adapter-aware failover + context-handoff bridge (#2)
  - `aa86b9f9` 2026-06-08 claude_local の Advanced 設定に Recovery fallback agent 項目を追加し hire/PATCH 双方で recoveryFallbackAgentId を保存できるようにする (#4)

**[alcylu/paperclip](https://github.com/alcylu/paperclip)** — балл **75.8**, `Фича`, впереди 4 коммитов, позади 2673, ±805 строк, ★0, пуш 2026-06-12, ценность 3.43/4, дубль 0.33, секреты 0.23
  - `40ab200b` 2026-04-07 feat: add Claude subscription rotation for multi-account support
  - `b8d596f1` 2026-04-07 fix: read Claude OAuth tokens from macOS keychain
  - `7ff2851f` 2026-04-09 fix: detect rate_limit_event so subscription rotation actually triggers
  - `815962c0` 2026-04-10 fix: inbox badge counts all issues instead of only unread ones

**[keegoid/paperclip](https://github.com/keegoid/paperclip)** — балл **75.7**, `Фикс`, впереди 16 коммитов, позади 2208, ±2092 строк, ★0, пуш 2026-05-31, ценность 2.64/4, дубль 0.43, секреты 0.12
  - `c10d0e50` 2026-05-06 fix: bound silent timer watchdogs
  - `c684c015` 2026-05-06 Merge pull request #6 from keegoid/fig/dev-223-silent-timer-watchdog
  - `28046531` 2026-05-06 test: cover timer no-work negative cases
  - `5b38ee79` 2026-05-06 Merge pull request #7 from keegoid/fig/dev-268-timer-no-work-negative-tests
  - `3ea6e561` 2026-05-06 fix: harden codex-local heartbeat liveness (#8)

**[simberthon/paperclip](https://github.com/simberthon/paperclip)** — балл **75.2**, `Фикс`, впереди 2 коммитов, позади 1884, ±329 строк, ★0, пуш 2026-09-26, ценность 2.73/4, дубль 0.51, секреты 0.1
  - `237843c5` 2026-06-28 fix(heartbeat): stop stranding agents in error after spurious transient failure (LUN-2682)
  - `1d1a50a5` 2026-06-28 Merge pull request #1 from simberthon/LUN-2682-spurious-failure-strand-fix

**[paulmerz/paperclip](https://github.com/paulmerz/paperclip)** — балл **74.9**, `Фича`, впереди 1 коммитов, позади 2258, ±1347 строк, ★0, пуш 2026-04-28, ценность 2.78/4, дубль 0.41, секреты 0.13
  - `3e359616` 2026-04-28 Add continuation loop guard & token budgets

**[Southeastern-Renovation/paperclip](https://github.com/Southeastern-Renovation/paperclip)** — балл **74.6**, `Фикс`, впереди 8 коммитов, позади 929, ±1028 строк, ★0, пуш 2026-09-08, ценность 2.61/4, дубль 0.42, секреты 0.15
  - `0939e03d` 2026-08-17 feat(costs): price token usage when the adapter reports nothing, so budgets bind
  - `6a629cdd` 2026-08-17 fix(costs): a redirected base URL is a bill, not a subscription
  - `43ec44f4` 2026-08-18 Merge pull request #2 from Southeastern-Renovation/fix/base-url-is-not-a-subscription
  - `016b55dd` 2026-08-18 Merge pull request #1 from Southeastern-Renovation/feat/model-price-fallback
  - `716a9b98` 2026-08-18 fix(costs): price by who invoices, not by what the model calls itself

**[zackjyo39-alt/paperclip](https://github.com/zackjyo39-alt/paperclip)** — балл **74.6**, `Деплой`, впереди 3 коммитов, позади 2841, ±806 строк, ★0, пуш 2026-08-13, ценность 3.54/4, дубль 0.41, секреты 0.18
  - `93455d4a` 2026-03-29 Add self-hosted Paperclip wrapper
  - `d2062edc` 2026-03-29 Merge branch 'codex/self-hosted-wrapper'
  - `7d0b3ee4` 2026-04-01 Merge branch 'paperclipai:master' into master

**[RiyDomingo/paperclip-master](https://github.com/RiyDomingo/paperclip-master)** — балл **74.5**, `Фича`, впереди 2 коммитов, позади 2416, ±3503 строк, ★0, пуш 2026-04-13, ценность 3.88/4, дубль 0.34, секреты 0.14
  - `cbf72def` 2026-04-10 Add Codex OSS/local support & Claude parse fixes
  - `27adde2c` 2026-04-13 Add document index & issue outstanding summaries

**[RajdevShivam/paperclip](https://github.com/RajdevShivam/paperclip)** — балл **74.1**, `Фикс`, впереди 4 коммитов, позади 3680, ±896 строк, ★0, пуш 2026-03-17, ценность 2.95/4, дубль 0.39, секреты 0.12
  - `ff7dac11` 2026-03-17 fix(issues): clear all execution lock fields on release and PATCH
  - `cb1b6317` 2026-03-17 fix: execution locks, silent success, process-lost retry, injection, env vars, perf
  - `b75b575c` 2026-03-17 fix(heartbeat): inject live issue state into system prompt on comment wake
  - `89926ce8` 2026-03-17 fix(adapter): clear session and set distinct errorCode on Anthropic API 5xx

**[YukiCrisp/paperclip](https://github.com/YukiCrisp/paperclip)** — балл **74.0**, `Фича`, впереди 8 коммитов, позади 1805, ±2103 строк, ★0, пуш 2026-09-16, ценность 2.82/4, дубль 0.4, секреты 0.15
  - `888e108e` 2026-06-19 fix(heartbeat): detect PID reuse before treating an orphaned run as alive
  - `13b794de` 2026-06-19 fix(heartbeat): guard against double-launching an agent with a live detached survivor (#2)
  - `258cfe8a` 2026-06-20 feat(heartbeat): sanctioned reap-run verb + remove raw-SQL run termination (ENGA-520)
  - `5813cd13` 2026-06-21 Merge remote-tracking branch 'origin/master' into tmp-fork-master
  - `2a271599` 2026-06-21 feat(claude-local): no-token inactivity watchdog + run-level wall-clock cap (ENGA-578 pt2) (#5)

**[utk2602/paperclip](https://github.com/utk2602/paperclip)** — балл **73.7**, `Безопасность`, впереди 18 коммитов, позади 2724, ±429 строк, ★0, пуш 2026-04-06, ценность 2.37/4, дубль 0.37, секреты 0.12
  - `9c4436b6` 2026-04-04 security: tighten session handoff summary truncation to 200 chars
  - `294b3a7b` 2026-04-04 security: wrap session handoff in XML trust boundary delimiters
  - `97912445` 2026-04-04 security: add wrapUntrustedHandoff() defense-in-depth utility
  - `eb232daf` 2026-04-04 security: use wrapUntrustedHandoff in all adapter execute files
  - `1f23e313` 2026-04-04 security: add system-prompt preamble to wrapUntrustedHandoff

**[Aitor1111/paperclip](https://github.com/Aitor1111/paperclip)** — балл **73.6**, `Фича`, впереди 22 коммитов, позади 2364, ±2318 строк, ★0, пуш 2026-04-29, ценность 3.7/4, дубль 0.45, секреты 0.13
  - `0c0aa2b9` 2026-04-14 feat: add terminal launcher utility for interactive Claude Code sessions
  - `2ca9ae3b` 2026-04-14 fix: harden terminal-launcher path quoting, detection, and tests
  - `2a2881d3` 2026-04-14 feat: add POST /api/agents/:id/meet endpoint for interactive sessions
  - `3529b68c` 2026-04-14 feat: intercept heartbeat runs with "meet" label to open interactive terminal
  - `b64fa109` 2026-04-14 feat: add Meet button to agent detail page

**[uthapjhojho/paperclip](https://github.com/uthapjhojho/paperclip)** — балл **73.6**, `Фича`, впереди 2 коммитов, позади 2671, ±53 строк, ★0, пуш 2026-08-29, ценность 2.75/4, дубль 0.41, секреты 0.13
  - `e85b78c0` 2026-04-07 fix(docker): add locale support and set default data dir
  - `126a83df` 2026-08-29 feat: add hermes_local adapter type and isHeartbeatTriggeredRun helper

**[thejoyfulist/paperclip](https://github.com/thejoyfulist/paperclip)** — балл **73.5**, `Фикс`, впереди 4 коммитов, позади 1217, ±291 строк, ★0, пуш 2026-08-06, ценность 2.62/4, дубль 0.5, секреты 0.1
  - `82193514` 2026-08-02 fix(server): prevent active run self-comment wake loop
  - `66fcf6a7` 2026-08-02 fix(server): guard top-level run comments from self-wake
  - `9eec8ffc` 2026-08-04 [verified] fix: suppress self-comment wake loops
  - `8107f3f1` 2026-08-06 Merge pull request #1 from thejoyfulist/fix/self-comment-run-wake-loop

**[Jeon1691/paperclip](https://github.com/Jeon1691/paperclip)** — балл **73.4**, `Деплой`, впереди 3 коммитов, позади 2208, ±854 строк, ★0, пуш 2026-05-05, ценность 3.3/4, дубль 0.42, секреты 0.13
  - `9f267f17` 2026-03-31 Add Proxmox deployment workflow
  - `c835d63b` 2026-05-05 Migrate claude-local to `claude auth login` subcommand
  - `5eb02289` 2026-05-05 Merge feat/proxmox-deploy into master

**[ryanclark2/paperclip](https://github.com/ryanclark2/paperclip)** — балл **73.3**, `Фикс`, впереди 2 коммитов, позади 427, ±1403 строк, ★0, пуш 2026-09-26, ценность 2.4/4, дубль 0.37, секреты 0.11
  - `de30a985` 2026-09-05 adapters: make the configured agent cwd an unconditional pin, with a test
  - `4a766f08` 2026-09-10 heartbeat: give a queued run that blocks open work a 24h dispatch head start (ALM-7932) (#2)

**[haydonbunting-source/paperclip](https://github.com/haydonbunting-source/paperclip)** — балл **73.0**, `Безопасность`, впереди 1 коммитов, позади 1697, ±1929 строк, ★0, пуш 2026-07-03, ценность 2.35/4, дубль 0.33, секреты 0.14
  - `1730690d` 2026-07-03 [verified] Harden defaults against backdoor-like behavior (#1)

**[ilyanemchenko/paperclip](https://github.com/ilyanemchenko/paperclip)** — балл **72.9**, `Фикс`, впереди 2 коммитов, позади 1641, ±134 строк, ★0, пуш 2026-07-08, ценность 2.53/4, дубль 0.49, секреты 0.11
  - `435348de` 2026-07-07 fix(server): reuse shared execution workspaces safely
  - `54c68e6a` 2026-07-08 fix(workspaces): archive shared primary sessions cleanly

**[Flopsstuff/paperclip](https://github.com/Flopsstuff/paperclip)** — балл **72.9**, `Фикс`, впереди 4 коммитов, позади 170, ±432 строк, ★0, пуш 2026-09-26, ценность 2.31/4, дубль 0.5, секреты 0.1
  - `d554c478` 2026-09-17 fix(ui): keep task composer available while pause state loads (#13562)
  - `38e5b317` 2026-09-05 fix(environments): remote-only adapterConfig.cwd
  - `d511d290` 2026-06-27 fix(skill): commit co-author trailers name the agent and its model
  - `3587eb02` 2026-09-26 fix(hermes): omit -m when the model resolves to auto

**[jotavgomes/paperclip](https://github.com/jotavgomes/paperclip)** — балл **72.8**, `Фикс`, впереди 17 коммитов, позади 793, ±1834 строк, ★0, пуш 2026-08-25, ценность 3.14/4, дубль 0.44, секреты 0.19
  - `7e3c6df3` 2026-08-24 fix(docker): restart policy and migration flag on compose (#11989)
  - `f941dd0c` 2026-08-24 fix(adapter-utils): seed Codex ACP auth.json from a configured OPENAI_API_KEY (#11999)
  - `2282703d` 2026-08-24 fix: atomic runtime skill materialization + full optional-chaining guard in FileViewerSheet (#11991)
  - `ab978401` 2026-08-24 feat(plugins): add Telegram Bot Control plugin (#12004)
  - `f22e6fe2` 2026-08-24 fix(adapters): unblock a fresh gemini_local agent's first heartbeat (#12018)

**[daniel-mariani/paperclip](https://github.com/daniel-mariani/paperclip)** — балл **72.7**, `Фикс`, впереди 8 коммитов, позади 166, ±823 строк, ★0, пуш 2026-09-21, ценность 2.21/4, дубль 0.42, секреты 0.09
  - `2ff5dd8c` 2026-09-10 fix(server): add durable zombie-session reaper for claude_local runs
  - `9091b940` 2026-09-16 fix(server): address Greptile review findings on zombie-reaper PR
  - `abe14626` 2026-09-10 fix(server): retain in-memory handle when zombie kill throws; add kill-failure test
  - `5b47e4d2` 2026-09-15 fix(server): guard against PID recycling in reapSilentZombieRuns retry path
  - `80fde3c6` 2026-09-16 fix(test): add reapSilentZombieRuns mock to startup wiring test

**[SXITS/paperclip](https://github.com/SXITS/paperclip)** — балл **72.7**, `Фича`, впереди 4 коммитов, позади 2145, ±799 строк, ★0, пуш 2026-09-15, ценность 2.7/4, дубль 0.45, секреты 0.1
  - `84425bd4` 2026-05-13 feat(done-gate): write-time PATCH gate for status=done transitions (STAA-4122)
  - `5304c5c2` 2026-05-13 fix(done-gate): scope gate to agent actors; bypass for board/user and execution-policy decisions
  - `34ee4499` 2026-05-13 Merge feat/done-gate-staa-4122: write-time PATCH gate for status=done (STAA-4122/STAA-4128)
  - `ac8b4f55` 2026-05-14 fix(claude-local): treat subtype=success as succeeded even with non-zero exit code (STAA-4174)

**[GODEXTREME/paperclip](https://github.com/GODEXTREME/paperclip)** — балл **72.5**, `Фича`, впереди 4 коммитов, позади 1513, ±1228 строк, ★0, пуш 2026-07-14, ценность 3.2/4, дубль 0.38, секреты 0.26
  - `d2c54965` 2026-06-14 feat(agents): persist per-adapter config and add usage-limit fallback adapter (#1)
  - `25a3c0e6` 2026-06-14 chore: self-host GHCR/Portainer compose + on-demand image publish + token plan (#2)
  - `0478eee4` 2026-06-14 fix(ui): stop previous adapter config bleeding into the form on adapter switch (#3)
  - `2e8be507` 2026-06-14 fix(ui): reset cheap model profile on adapter switch + keep disable sticky (#4)

**[vaibhav0806/paperclip](https://github.com/vaibhav0806/paperclip)** — балл **72.3**, `Фикс`, впереди 2 коммитов, позади 1464, ±348 строк, ★0, пуш 2026-07-19, ценность 2.46/4, дубль 0.42, секреты 0.12
  - `1785a942` 2026-07-19 fix(codex): surface provider errors emitted as text
  - `5339014f` 2026-07-19 fix(server): preserve scoped recovery issue state

**[contactmurphy/paperclip](https://github.com/contactmurphy/paperclip)** — балл **72.3**, `Деплой`, впереди 23 коммитов, позади 953, ±460 строк, ★0, пуш 2026-09-05, ценность 2.75/4, дубль 0.84, секреты 0.1
  - `661edf1b` 2026-04-06 fix: add USER node to Dockerfile to fix Claude Code root user error
  - `2645e811` 2026-04-06 fix: handle non-root execution in entrypoint script
  - `e74362b0` 2026-04-06 fix: remove VOLUME keyword banned by Railway
  - `b3467894` 2026-04-06 fix: restore missing backslash on line 10 breaking Dockerfile build
  - `63f4d727` 2026-04-06 chore: trigger redeploy after clearing healthcheck path

**[antoine97419/paperclip](https://github.com/antoine97419/paperclip)** — балл **72.2**, `Фикс`, впереди 2 коммитов, позади 76, ±778 строк, ★0, пуш 2026-09-23, ценность 2.36/4, дубль 0.42, секреты 0.11
  - `08dbd2d5` 2026-09-23 fix(recovery): bound self-originated continuation recovery
  - `f59b668d` 2026-09-23 fix(heartbeat): suppress same-run blocked self-wake

**[OvictorVieira/paperclip](https://github.com/OvictorVieira/paperclip)** — балл **72.1**, `Фича`, впереди 40 коммитов, позади 2138, ±2475 строк, ★0, пуш 2026-05-14, ценность 2.86/4, дубль 0.55, секреты 0.18
  - `1bbbbe9b` 2026-05-04 feat: add sessionPolicy summarized for Ralph Loop style agents
  - `42b60884` 2026-05-05 fix(adapters): persist summarized handoff on failures
  - `eee34d83` 2026-05-05 fix(codex): isolate home for fresh session policies
  - `effd1546` 2026-05-04 Fix Cloud tenant issue identifier routes (#5196)
  - `1beb6b7d` 2026-05-05 Expand plugin host surface (#5205)

**[scaleupventures01/paperclip](https://github.com/scaleupventures01/paperclip)** — балл **72.0**, `Фича`, впереди 14 коммитов, позади 26, ±1513 строк, ★0, пуш 2026-09-27, ценность 3.64/4, дубль 0.41, секреты 0.18
  - `f63a3c6a` 2026-09-25 feat: add delivery and operations agent roles (#1)
  - `422ea77d` 2026-09-25 feat: add complete ScaleUp role taxonomy (#2)
  - `bce64072` 2026-09-25 feat: allow scoped autonomous pod hiring (#3)
  - `f29626d0` 2026-09-25 feat: scope manager lifecycle actions (#4)
  - `bf265c26` 2026-09-25 fix: use scoped validator package export (#5)

**[VincentShipsIt/paperclip](https://github.com/VincentShipsIt/paperclip)** — балл **71.6**, `Фикс`, впереди 21 коммитов, позади 2377, ±2237 строк, ★0, пуш 2026-04-12, ценность 2.79/4, дубль 0.69, секреты 0.15
  - `72daffb6` 2026-04-02 fix: clear stale executionRunId on release, reassignment, and checkout (#2482)
  - `cc7a17a2` 2026-04-02 fix: harden orphan-process reap startup behavior (DLD-1636) (#2501)
  - `fa76631f` 2026-04-02 fix(adapters/claude-local): classify quota exhaustion as recoverable failure (#2505)
  - `d57bc6c2` 2026-04-02 fix: cache materialised GitHub skills to avoid re-fetch on every heartbeat run (#2508)
  - `b72eaa3c` 2026-04-02 feat: fatal stderr detection, zombie run hardening, and UI improvements

**[lnsflive/paperclip](https://github.com/lnsflive/paperclip)** — балл **71.5**, `Фикс`, впереди 4 коммитов, позади 1391, ±1236 строк, ★0, пуш 2026-09-11, ценность 2.8/4, дубль 0.44, секреты 0.1
  - `1283cd3f` 2026-09-11 ci: run the PR workflow on main and runtime bases
  - `10985edf` 2026-09-11 fix(execution-policy): preserve eligible next-stage reviewers (#1)
  - `5d69f0f9` 2026-09-11 Fix atomic changes-requested routing reconciliation (#3)
  - `f289be92` 2026-09-11 Fix recovery mutation transaction deadlock (#4)

**[abernerus/paperclip](https://github.com/abernerus/paperclip)** — балл **71.5**, `Фикс`, впереди 22 коммитов, позади 1884, ±1657 строк, ★0, пуш 2026-08-06, ценность 2.73/4, дубль 0.4, секреты 0.09
  - `93788c8b` 2026-06-17 fix(server): allow recovery action owner to resolve as false_positive without board [CAS-6623]
  - `d9bb807f` 2026-06-17 Merge pull request #1 from abernerus/cas-6623-recovery-action-owner-false-positive
  - `9694095b` 2026-06-19 Move design guide skill under agents
  - `cdb26d4e` 2026-06-19 Tighten Paperclip skill descriptions
  - `c99cf534` 2026-06-24 fix(recovery): keep delegated assignee durable across stranded recovery retries [CAS-6342]

**[Nootencorp/paperclip](https://github.com/Nootencorp/paperclip)** — балл **71.5**, `Фикс`, впереди 3 коммитов, позади 2129, ±839 строк, ★0, пуш 2026-05-21, ценность 2.76/4, дубль 0.44, секреты 0.12
  - `96fa3a47` 2026-05-16 fix: tolerate stale activity log run ids
  - `291e3c87` 2026-05-16 fix(server): validate request run ids before attribution
  - `344c75bf` 2026-05-17 Fix Hermes resume session recovery

**[oldboydev/paperclip](https://github.com/oldboydev/paperclip)** — балл **71.5**, `Фикс`, впереди 25 коммитов, позади 2199, ±371 строк, ★0, пуш 2026-05-05, ценность 2.51/4, дубль 0.46, секреты 0.15
  - `a3a4a67a` 2026-05-04 fix(claude-adapter): skip unknown system events in probe stream to support SessionStart hooks
  - `10f6121f` 2026-05-04 Merge pull request #1 from oldboydev/fix/claude-probe-hooks
  - `a1e1815d` 2026-05-03 [codex] Add issue monitor liveness controls (#4988)
  - `aaec1809` 2026-05-03 [codex] Retry max-turn exhausted heartbeats (#5096)
  - `1b94054d` 2026-05-03 Let sandbox providers declare shell defaults (#5114)

**[bhushan-patil-official/paperclip](https://github.com/bhushan-patil-official/paperclip)** — балл **71.4**, `Фича`, впереди 11 коммитов, позади 2092, ±2157 строк, ★0, пуш 2026-05-26, ценность 3.15/4, дубль 0.49, секреты 0.27
  - `756f2a93` 2026-05-18 Add CTO agent instruction template for hiring and onboarding.
  - `ba0eebea` 2026-05-18 Merge branch 'paperclipai:master' into master
  - `6ccb263f` 2026-05-21 Merge branch 'paperclipai:master' into master
  - `03d764bd` 2026-05-22 Add model fallback chains and priority-based model tiers.
  - `e84d3533` 2026-05-23 Merge branch 'paperclipai:master' into master


# Один issue — несколько PR: кого брать (34 групп)

- issue #958 (Slow UI - Critical memory leak and UI freeze from unpaginated heartbeat runs): кандидаты #13560, #7311 → **берём [#7311](https://github.com/paperclipai/paperclip/pull/7311)** (уверенность 0.99, proper_fix 0.82)

- issue #7781 (Company deletion 500s on companies with data — child tables deleted before parents / FKs not cascaded): кандидаты #10322, #9684 → **берём [#10322](https://github.com/paperclipai/paperclip/pull/10322)** (уверенность 0.98, proper_fix 0.7)

- issue #10182 ([TEC-7237] Implement adapterConfig user-lock and narrow skill-sync): кандидаты #10193, #10200, #10198 → **берём [#10193](https://github.com/paperclipai/paperclip/pull/10193)** (уверенность 0.98, proper_fix 0.7)

- issue #7290 ([opencode] env variable can not be overriden): кандидаты #7352, #7292 → **берём [#7352](https://github.com/paperclipai/paperclip/pull/7352)** (уверенность 0.98, proper_fix 0.71)

- issue #693 (Validation matrix: board auth, agent auth, bootstrap invite, onboarding): кандидаты #3543, #2998 → **берём [#3543](https://github.com/paperclipai/paperclip/pull/3543)** (уверенность 0.97, proper_fix 0.64)

- issue #4143 (User-participant approval stages have no UI action buttons): кандидаты #13986, #9596, #5487 → **берём [#13986](https://github.com/paperclipai/paperclip/pull/13986)** (уверенность 0.96, proper_fix 0.7)

- issue #3936 (Add xHigh and Max thinking effort options to claude_local adapter): кандидаты #14039, #3937 → **берём [#3937](https://github.com/paperclipai/paperclip/pull/3937)** (уверенность 0.96, proper_fix 0.83)

- issue #7755 ([Bug] EPIPE crash in adapter-utils server-utils.js:1687 — unhandled Socket error on stdin.write after pipe close): кандидаты #7757, #14057, #12324 → **берём [#7757](https://github.com/paperclipai/paperclip/pull/7757)** (уверенность 0.95, proper_fix 0.57)

- issue #3108 (catchUpPolicy: skip_missed not respected — overdue routines fire on first scheduler tick after startup): кандидаты #3133, #11368 → **берём [#3133](https://github.com/paperclipai/paperclip/pull/3133)** (уверенность 0.95, proper_fix 0.56)

- issue #8617 (request_confirmation reject on a user-assigned issue never wakes the creator agent (silent stall)): кандидаты #8516, #10278 → **берём [#8516](https://github.com/paperclipai/paperclip/pull/8516)** (уверенность 0.92, proper_fix 0.74)

- issue #8931 (Plugin page URL gets company slug tripled when switching teams via top-left dropdown): кандидаты #9176, #9084 → **берём [#9084](https://github.com/paperclipai/paperclip/pull/9084)** (уверенность 0.92, proper_fix 0.66)

- issue #9874 (clearExecutionRunIfTerminal never reaps a queued-but-never-started heartbeat-run, leaving an unbreakable executionRunId exec-lock on the issue): кандидаты #10794, #10449 → **берём [#10794](https://github.com/paperclipai/paperclip/pull/10794)** (уверенность 0.91, proper_fix 0.57)

- issue #7479 (UTF-8 encoding corruption on Windows in adapter-utils stream handlers): кандидаты #13225, #7440 → **берём [#7440](https://github.com/paperclipai/paperclip/pull/7440)** (уверенность 0.9, proper_fix 0.84)

- issue #3195 (issue #3195): кандидаты #5098, #4282 → **берём [#5098](https://github.com/paperclipai/paperclip/pull/5098)** (уверенность 0.89, proper_fix 0.48)

- issue #4625 (periodic heartbeat recovery failed): кандидаты #9454, #4805 → **берём [#4805](https://github.com/paperclipai/paperclip/pull/4805)** (уверенность 0.84, proper_fix 0.58)

- issue #11857 (GET /companies/:companyId/issues?createdByAgentId= is silently ignored (returns full unfiltered set)): кандидаты #11858, #12742 → **берём [#11858](https://github.com/paperclipai/paperclip/pull/11858)** (уверенность 0.82, proper_fix 0.59)

- issue #10406 (Creating a blocked issue does not wake its unblock owner): кандидаты #12734, #12556, #10418 → **берём [#12734](https://github.com/paperclipai/paperclip/pull/12734)** (уверенность 0.78, proper_fix 0.67)

- issue #11932 (Agent-addressed interaction wake is cancelled as issue_assignee_changed when addressee is not issue assignee): кандидаты #13211, #11939 → **берём [#13211](https://github.com/paperclipai/paperclip/pull/13211)** (уверенность 0.74, proper_fix 0.58)

- issue #7245 (company import --target new strands imported agents in pending_approval with no approval record (no UI button, no CLI verb -> unactivatable)): кандидаты #10246, #7337 → **берём [#7337](https://github.com/paperclipai/paperclip/pull/7337)** (уверенность 0.74, proper_fix 0.63)

- issue #13935 (Slack gallery app ("Use this connection as an agent tool") fails with "Invalid permissions requested": bot OAuth endpoints + search:read scope don't match mcp.slack.com): кандидаты #14037, #13954 → **берём [#14037](https://github.com/paperclipai/paperclip/pull/14037)** (уверенность 0.68, proper_fix 0.61)

- issue #5893 (GET /api/companies/{companyId}/activity ignores ?since= query param (returns full history every call)): кандидаты #11552, #5907 → **берём [#5907](https://github.com/paperclipai/paperclip/pull/5907)** (уверенность 0.63, proper_fix 0.68)

- issue #13806 (Agent cannot comment on or close its own assigned issue: assigneeAgentId set at creation doesn't satisfy the cross-issue-influence guard): кандидаты #13926, #14087 → **берём [#14087](https://github.com/paperclipai/paperclip/pull/14087)** (уверенность 0.63, proper_fix 0.55)

- issue #6805 (claude_local adapter fails on Windows when user profile path contains a space): кандидаты #6891, #6897 → **берём [#6891](https://github.com/paperclipai/paperclip/pull/6891)** (уверенность 0.61, proper_fix 0.57)

- issue #14034 (hermes_gateway final-output runs can be misclassified as "no concrete action evidence" before final comment is persisted): кандидаты #14085, #14041 → **берём [#14041](https://github.com/paperclipai/paperclip/pull/14041)** (уверенность 0.6, proper_fix 0.56)

- issue #12118 (Timer-heartbeat runs get 403 cross_issue_influence_run_context_required on every issue write, including their own issue — stated remedy is unachievable): кандидаты #13833, #13650, #12532 → **берём [#13833](https://github.com/paperclipai/paperclip/pull/13833)** (уверенность 0.57, proper_fix 0.59)

- issue #14149 (openclaw_gateway: streamed assistant deltas are trimmed, so words run together in comments): кандидаты #14217, #14150 → **берём [#14217](https://github.com/paperclipai/paperclip/pull/14217)** (уверенность 0.56, proper_fix 0.54)

- issue #63 (Symlink creation fails on Windows (EPERM) in adapter-claude-local and adapter-codex-local): кандидаты #872, #5234 → **берём [#5234](https://github.com/paperclipai/paperclip/pull/5234)** (уверенность 0.55, proper_fix 0.7)

- issue #13126 (codex_local: model discovery ignores the Codex CLI's own models_cache.json, so ChatGPT-auth installs never see new models): кандидаты #13134, #13127 → **берём [#13134](https://github.com/paperclipai/paperclip/pull/13134)** (уверенность 0.46, proper_fix 0.63)

- issue #13078 (Runs with no source issue in contextSnapshot cannot write to ANY issue, including their own): кандидаты #13833, #13650 → **берём [#13833](https://github.com/paperclipai/paperclip/pull/13833)** (уверенность 0.42, proper_fix 0.54)

- issue #637 (Bug: sidebar-badges 500 — dashboard.summary() crashes on missing count property): кандидаты #733, #677 → **берём [#733](https://github.com/paperclipai/paperclip/pull/733)** (уверенность 0.4, proper_fix 0.29)

- issue #7594 (BUG: successful-run handoff aborts with schema too_big error on long issue titles (and run/agent names)): кандидаты #5369, #12516 → **берём [#5369](https://github.com/paperclipai/paperclip/pull/5369)** (уверенность 0.4, proper_fix 0.75)

- issue #7411 (fix(service): add OOMPolicy=continue to paperclip.service — agent OOM kill cascades to server crash): кандидаты #7219, #7376 → **берём ни один** (уверенность 0.28, proper_fix 0.47)

- issue #4996 (issue #4996): кандидаты #5060, #10519 → **берём [#5060](https://github.com/paperclipai/paperclip/pull/5060)** (уверенность 0.24, proper_fix 0.41)

- issue #1317 (Proposition: Add all codex models (2min work)): кандидаты #5087, #9382 → **берём [#5087](https://github.com/paperclipai/paperclip/pull/5087)** (уверенность 0.21, proper_fix 0.57)
