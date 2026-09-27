# PR Scout: paperclipai/paperclip

Прогон: 2988 PR с баллами, финалистов 120, Jev потратил $0.3951 (7901929 входных токенов).

- `fetch`: 2988 шт · 545 с · $0 · ошибок 0
- `stage1`: 2988 шт · 424 с · $0.3507 · ошибок 0
- `stage2`: 120 шт · 1947 с · $0.0444 · ошибок 0

| вариант | цена |
|---|---:|
| Jev (факт) | $0.3951 |
| Claude Opus 5.5 | $94.97 |
| Claude Sonnet 5 | $47.48 |
| Claude Haiku 4.5 | $23.74 |

## Берём (15)

**#11311** [fix(adapter-utils): redact env dumps and DSN passwords in transcripts](https://github.com/paperclipai/paperclip/pull/11311)
`безопасность` · Прочее · автор @notandrewblejde · балл **84.5** · 209+5 строк · None дн. · CI: flaky_only
  - + серьёзный баг в обычной работе (вред 0.91, частота 0.62)
  - + прямо про ваше использование (2.81/3)

**#11479** [fix(server): keep comment after-cursor exclusive at microsecond precision](https://github.com/paperclipai/paperclip/pull/11479)
`фикс` · Задачи и согласования · автор @iamasuperuser · балл **84.4** · 147+34 строк · None дн. · CI: green
  - + серьёзный баг в обычной работе (вред 0.83, частота 0.83)
  - + прямо про ваше использование (2.78/3)

**#13936** [fix(server): redact credential-bearing git remotes in run logs](https://github.com/paperclipai/paperclip/pull/13936)
`безопасность` · Запуски и heartbeat · автор @mrkhan91 · балл **84.3** · 606+33 строк · None дн. · CI: green
  - + серьёзный баг в обычной работе (вред 0.93, частота 0.57)
  - + прямо про ваше использование (2.88/3)

**#11107** [fix(recovery): stop agent output from bypassing the run-liveness safety gate](https://github.com/paperclipai/paperclip/pull/11107)
`безопасность` · Запуски и heartbeat · автор @trelmitt · балл **83.0** · 96+3 строк · None дн. · CI: flaky_only
  - + серьёзный баг в обычной работе (вред 0.91, частота 0.54)
  - + прямо про ваше использование (2.89/3)

**#11052** [fix(claude-local): classify failures from the run's error surface, not its whole stdout](https://github.com/paperclipai/paperclip/pull/11052)
`фикс` · Claude-адаптер · автор @juancarlosrial76-code · балл **82.8** · 136+1 строк · None дн. · CI: green
  - + серьёзный баг в обычной работе (вред 0.73, частота 0.79)
  - + прямо про ваше использование (2.88/3)

**#11462** [fix(security): redact sensitive fields in config-read API responses (extracted from #10284)](https://github.com/paperclipai/paperclip/pull/11462)
`безопасность` · Коннекторы и MCP · автор @JackReis · балл **82.7** · 95+1 строк · None дн. · CI: flaky_only
  - + серьёзный баг в обычной работе (вред 0.86, частота 0.72)
  - + прямо про ваше использование (2.61/3)

**#10735** [fix(issues): re-arm issue monitors on dispatch so a failed run cannot strand the issue](https://github.com/paperclipai/paperclip/pull/10735)
`фикс` · Запуски и heartbeat · автор @juancarlosrial76-code · балл **81.6** · 460+32 строк · None дн. · CI: green
  - + серьёзный баг в обычной работе (вред 0.84, частота 0.59)
  - + прямо про ваше использование (2.86/3)

**#13653** [Deterministic shipped-gate: verify claimed commits before an issue can reach done](https://github.com/paperclipai/paperclip/pull/13653)
`фикс` · Задачи и согласования · автор @ajinkyabhanudas · балл **80.7** · 558+17 строк · None дн. · CI: green
  - + серьёзный баг в обычной работе (вред 0.78, частота 0.69)
  - + прямо про ваше использование (2.92/3)

**#13978** [fix(claude-local): let npm installs run Opus 5.5 with Claude ACP bridge 0.81.2](https://github.com/paperclipai/paperclip/pull/13978)
`фикс` · Claude-адаптер · автор @itsjeremyjohnson · балл **80.0** · 155+84 строк · None дн. · CI: flaky_only
  - + серьёзный баг в обычной работе (вред 0.84, частота 0.65)
  - + прямо про ваше использование (2.69/3)

**#13769** [fix(heartbeat): re-admit a wake parked by a gate that has gone away](https://github.com/paperclipai/paperclip/pull/13769)
`фикс` · Запуски и heartbeat · автор @MrBlackTongue · балл **79.5** · 341+0 строк · None дн. · CI: green
  - + серьёзный баг в обычной работе (вред 0.92, частота 0.5)
  - + прямо про ваше использование (2.82/3)

**#9219** [fix(claude-local, heartbeat): recover from silent session_lost caused by cwd switches](https://github.com/paperclipai/paperclip/pull/9219)
`фикс` · Запуски и heartbeat · автор @Sergio-LPA · балл **79.3** · 258+2 строк · None дн. · CI: green
  - + серьёзный баг в обычной работе (вред 0.69, частота 0.74)
  - + прямо про ваше использование (2.88/3)

**#11500** [fix(server): count instead of refuse a run with no recorded source issue](https://github.com/paperclipai/paperclip/pull/11500)
`фикс` · Задачи и согласования · автор @dzianisv · балл **76.5** · 248+8 строк · None дн. · CI: green
  - + серьёзный баг в обычной работе (вред 0.86, частота 0.79)
  - + прямо про ваше использование (2.82/3)

**#4807** [fix(recovery): dispatch in_progress sub-issues with no execution history as fresh assignment (PAP-4766)](https://github.com/paperclipai/paperclip/pull/4807)
`фикс` · Запуски и heartbeat · автор @aimonk2025 · балл **76.2** · 111+1 строк · None дн. · CI: green
  - + серьёзный баг в обычной работе (вред 0.65, частота 0.67)
  - + прямо про ваше использование (2.67/3)

**#9810** [feat(mcp): add paperclipListIssueInteractions so agents can read decision-card replies](https://github.com/paperclipai/paperclip/pull/9810)
`фича` · Коннекторы и MCP · автор @greegorij · балл **76.2** · 9+2 строк · None дн. · CI: flaky_only
  - + сильная фича (ценность 3.33/4, новизна 0.88)
  - + прямо про ваше использование (2.52/3)

**#11336** [fix(server): share one pluginLifecycleManager between routes and dispatcher](https://github.com/paperclipai/paperclip/pull/11336)
`фикс` · Коннекторы и MCP · автор @c-barlow · балл **75.9** · 173+5 строк · None дн. · CI: green
  - + серьёзный баг в обычной работе (вред 0.56, частота 0.79)
  - + прямо про ваше использование (2.69/3)


## Рассмотреть (19)

**#13622** [fix(claude-local): use the `auth login` subcommand for agent login](https://github.com/paperclipai/paperclip/pull/13622)
`фикс` · Claude-адаптер · автор @croakingtoad · балл **85.0** · 53+1 строк · None дн. · CI: red
  - ! падают тесты CI: ci / verify, ci / Build, ci / Canary Dry Run
  - + серьёзный баг в обычной работе (вред 0.86, частота 0.8)
  - + прямо про ваше использование (2.8/3)

**#6808** [feat(heartbeat): ADR-0044 session lifecycle T1/T2/T3/T4 for claude_local](https://github.com/paperclipai/paperclip/pull/6808)
`фича` · Запуски и heartbeat · автор @yackovleff-solved · балл **83.9** · 680+23 строк · None дн. · CI: green
  - ! фича меняет поведение по умолчанию
  - + сильная фича (ценность 3.03/4, новизна 0.64)
  - + прямо про ваше использование (2.97/3)

**#13148** [fix(claude-local): classify ACP session-limit turn failures as provider quota with the parsed reset time](https://github.com/paperclipai/paperclip/pull/13148)
`фикс` · Claude-адаптер · автор @Sasshigo · балл **80.7** · 139+1 строк · None дн. · CI: red
  - ! падают тесты CI: ci / verify, ci / General tests (server (1/5))
  - + серьёзный баг в обычной работе (вред 0.69, частота 0.82)
  - + прямо про ваше использование (2.78/3)

**#13802** [fix(server): default and cap the heartbeat-runs list limit](https://github.com/paperclipai/paperclip/pull/13802)
`фикс` · Запуски и heartbeat · автор @hsluiscampingcomfort · балл **79.8** · 89+13 строк · None дн. · CI: red
  - ! падают тесты CI: ci / verify, ci / Verify Paperclip Runner (vitest 1/2)
  - + серьёзный баг в обычной работе (вред 0.87, частота 0.67)

**#11466** [fix(server): atomically set checkout run contextSnapshot with issue lock](https://github.com/paperclipai/paperclip/pull/11466)
`фикс` · Задачи и согласования · автор @santhiprakash · балл **79.8** · 281+58 строк · None дн. · CI: red
  - ! падают тесты CI: ci / verify, ci / General tests (server (3/5))
  - + серьёзный баг в обычной работе (вред 0.78, частота 0.58)
  - + прямо про ваше использование (2.91/3)

**#13478** [feat(claude-local): retry transient upstream errors with exponential backoff](https://github.com/paperclipai/paperclip/pull/13478)
`фича` · Claude-адаптер · автор @daniel-mariani · балл **79.8** · 300+1 строк · None дн. · CI: red
  - ! фича полезная, но не ключевая
  - ! падают тесты CI: ci / verify, ci / General tests (server (1/5))
  - ! фича меняет поведение по умолчанию
  - + прямо про ваше использование (2.9/3)

**#14248** [fix(server): keep a policy's other fields when a monitor is stripped](https://github.com/paperclipai/paperclip/pull/14248)
`фикс` · Задачи и согласования · автор @stefanriegel · балл **79.6** · 125+8 строк · None дн. · CI: red
  - ! падают тесты CI: ci / Verify serialized server suites (1/9)
  - + серьёзный баг в обычной работе (вред 0.85, частота 0.65)
  - + прямо про ваше использование (2.51/3)

**#14192** [feat(chat): add a Delete chat action to the agent conversation header](https://github.com/paperclipai/paperclip/pull/14192)
`фича` · Интерфейс · автор @MatrixCODEBreak · балл **78.7** · 293+2 строк · None дн. · CI: flaky_only
  - ! фича полезная, но не ключевая

**#8063** [feat(claude-local): resolve @ file references in agent instructions](https://github.com/paperclipai/paperclip/pull/8063)
`фича` · Claude-адаптер · автор @burnlife001 · балл **78.7** · 150+1 строк · None дн. · CI: red
  - ! падают тесты CI: verify, General tests (server)
  - + сильная фича (ценность 3.18/4, новизна 0.87)
  - + прямо про ваше использование (2.73/3)

**#10871** [feat(dashboard): report token usage where subscription billing zeroes spend](https://github.com/paperclipai/paperclip/pull/10871)
`фича` · Интерфейс · автор @Nissimmiracles · балл **78.5** · 651+38 строк · None дн. · CI: flaky_only
  - ! фича полезная, но не ключевая
  - ! фича меняет поведение по умолчанию
  - + прямо про ваше использование (2.56/3)

**#11980** [feat(approvals): add POST /approvals/:id/cancel for requester withdrawal [INUA-5995]](https://github.com/paperclipai/paperclip/pull/11980)
`фича` · Задачи и согласования · автор @rotem-zecharia · балл **78.3** · 386+1 строк · None дн. · CI: flaky_only
  - ! фича меняет поведение по умолчанию
  - + сильная фича (ценность 3.13/4, новизна 0.89)
  - + прямо про ваше использование (2.53/3)

**#4764** [fix: add goal owner editing in goals UI](https://github.com/paperclipai/paperclip/pull/4764)
`фича` · Интерфейс · автор @dumi-bogdan · балл **77.9** · 496+3 строк · None дн. · CI: flaky_only
  - ! фича полезная, но не ключевая
  - ! фича меняет поведение по умолчанию

**#13892** [fix(issues): let the assignee supersede critically-silent run bindings](https://github.com/paperclipai/paperclip/pull/13892)
`фикс` · Запуски и heartbeat · автор @iamasuperuser · балл **77.7** · 788+48 строк · None дн. · CI: green
  - ! баг не критичный или редкий
  - + прямо про ваше использование (2.88/3)

**#8800** [Add task thread sort order option](https://github.com/paperclipai/paperclip/pull/8800)
`фича` · Интерфейс · автор @saphid · балл **77.5** · 512+55 строк · None дн. · CI: green
  - ! фича полезная, но не ключевая

**#12786** [fix(adapter-utils): redact header-style secrets in command text](https://github.com/paperclipai/paperclip/pull/12786)
`безопасность` · Прочее · автор @superbiche · балл **77.5** · 1925+4 строк · None дн. · CI: green
  - ! большой PR (1929 строк)
  - + серьёзный баг в обычной работе (вред 0.92, частота 0.83)
  - + прямо про ваше использование (2.52/3)

**#13134** [feat(codex-models): read the Codex CLI models cache for ChatGPT-auth installs](https://github.com/paperclipai/paperclip/pull/13134)
`фича` · Codex-адаптер · автор @MindSyncHub · балл **76.7** · 206+1 строк · None дн. · CI: green
  - ! фича полезная, но не ключевая
  - ! фича меняет поведение по умолчанию
  - + прямо про ваше использование (2.53/3)

**#13883** [fix(recovery): give fresh runs a grace period before the issue-terminal sweep](https://github.com/paperclipai/paperclip/pull/13883)
`фикс` · Запуски и heartbeat · автор @Sergio-LPA · балл **76.6** · 175+7 строк · None дн. · CI: green
  - ! баг не критичный или редкий
  - + прямо про ваше использование (2.74/3)

**#13028** [fix(claude-local): do not treat a background-task notification as a finished turn](https://github.com/paperclipai/paperclip/pull/13028)
`фикс` · Claude-адаптер · автор @MrBlackTongue · балл **76.3** · 85+1 строк · None дн. · CI: green
  - ! баг не критичный или редкий
  - + прямо про ваше использование (2.82/3)

**#11747** [feat(issues): add staleHours filter to issue list route](https://github.com/paperclipai/paperclip/pull/11747)
`фича` · Задачи и согласования · автор @dzianisv · балл **76.0** · 318+1 строк · None дн. · CI: green
  - ! фича полезная, но не ключевая


## Пропускаем (86)

**#6692** [feat: implement server-side secret value redaction](https://github.com/paperclipai/paperclip/pull/6692)
`безопасность` · Запуски и heartbeat · автор @gorkemhacioglu · балл **84.9** · 307+33 строк · None дн. · CI: flaky_only
  - ✗ конфликт с основной веткой и взятыми PR: redaction.test.ts, heartbeat.ts
  - + серьёзный баг в обычной работе (вред 0.92, частота 0.81)
  - + прямо про ваше использование (2.9/3)

**#8841** [fix(server): sanitize credential-shaped values before persistence](https://github.com/paperclipai/paperclip/pull/8841)
`безопасность` · Запуски и heartbeat · автор @robertdevore · балл **84.8** · 373+12 строк · None дн. · CI: green
  - ✗ конфликт с основной веткой и взятыми PR: redaction.ts, activity.ts, activity-log.ts
  - + серьёзный баг в обычной работе (вред 0.87, частота 0.85)
  - + прямо про ваше использование (2.94/3)

**#4294** [Feature/4281 configurable claude local session lifecycle](https://github.com/paperclipai/paperclip/pull/4294)
`фича` · Запуски и heartbeat · автор @thomascolden585-svg · балл **84.2** · 519+11 строк · None дн. · CI: red
  - ✗ конфликт с основной веткой и взятыми PR: heartbeat.ts, Layout.tsx, PropertiesPanel.tsx
  - ✗ код не совпадает с описанием (0.09)
  - ! падают тесты CI: verify
  - + сильная фича (ценность 3.49/4, новизна 0.84)
  - + прямо про ваше использование (2.92/3)

**#11387** [feat(pipelines): issue-driven stage gates (autoAdvanceOnIssue) + pipeline-managed disposition exemption](https://github.com/paperclipai/paperclip/pull/11387)
`фича` · Задачи и согласования · автор @adamteale · балл **83.4** · 618+1 строк · None дн. · CI: red
  - ✗ конфликт с основной веткой и взятыми PR: successful-run-handoff.ts
  - ! падают тесты CI: ci / verify, ci / General tests (server (3/5))
  - + сильная фича (ценность 3.38/4, новизна 0.85)
  - + прямо про ваше использование (2.57/3)

**#3337** [feat(ui,adapter): add MCP server configuration for claude_local agents](https://github.com/paperclipai/paperclip/pull/3337)
`фича` · Claude-адаптер · автор @gbrancaglione · балл **83.4** · 849+6 строк · None дн. · CI: green
  - ✗ конфликт с основной веткой и взятыми PR: execute.ts, AgentDetail.tsx, vitest.config.ts
  - + сильная фича (ценность 3.16/4, новизна 0.89)
  - + прямо про ваше использование (2.92/3)

**#12539** [fix(server): redact heartbeat adapter output before persistence](https://github.com/paperclipai/paperclip/pull/12539)
`безопасность` · Запуски и heartbeat · автор @Dfskid · балл **83.3** · 672+50 строк · None дн. · CI: red
  - ✗ конфликт с основной веткой и взятыми PR: heartbeat-process-recovery.test.ts, redaction.test.ts, redaction.ts
  - ! падают тесты CI: ci / verify, ci / General tests (server (4/5)), ci / Build
  - + серьёзный баг в обычной работе (вред 0.82, частота 0.78)
  - + прямо про ваше использование (2.69/3)

**#4004** [feat(adapter-utils): idle + wall watchdogs for runChildProcess](https://github.com/paperclipai/paperclip/pull/4004)
`фича` · Другие адаптеры · автор @ericnicolaides · балл **83.1** · 489+44 строк · None дн. · CI: green
  - ✗ конфликт с основной веткой и взятыми PR: server-utils.test.ts, server-utils.ts, execute.ts
  - + сильная фича (ценность 3.37/4, новизна 0.77)
  - + прямо про ваше использование (2.99/3)

**#9750** [fix(tool-access,tool-gateway): perform MCP initialize handshake for remote HTTP servers, and retry through session churn](https://github.com/paperclipai/paperclip/pull/9750)
`фикс` · Коннекторы и MCP · автор @Quentin-M · балл **83.0** · 521+63 строк · None дн. · CI: flaky_only
  - ✗ конфликт с основной веткой и взятыми PR: mcp-http.test.ts, tool-access-service.test.ts, tool-gateway.test.ts
  - ✗ код не совпадает с описанием (0.47)
  - + серьёзный баг в обычной работе (вред 0.9, частота 0.53)
  - + прямо про ваше использование (2.95/3)

**#2779** [  **`security: mitigate cross-agent prompt injection via session handoff content (#2755)`**](https://github.com/paperclipai/paperclip/pull/2779)
`безопасность` · Запуски и heartbeat · автор @utk2602 · балл **82.7** · 408+21 строк · None дн. · CI: green
  - ✗ конфликт с основной веткой и взятыми PR: server-utils.test.ts, execute.ts, execute.ts
  - ✗ код не совпадает с описанием (0.4)
  - + серьёзный баг в обычной работе (вред 0.88, частота 0.74)
  - + прямо про ваше использование (2.98/3)

**#11096** [fix(interactions): accept intuitive ask_user_questions payload shape](https://github.com/paperclipai/paperclip/pull/11096)
`фикс` · Задачи и согласования · автор @sagiw · балл **82.6** · 96+3 строк · None дн. · CI: green
  - ✗ конфликт с основной веткой и взятыми PR: issue.test.ts, issue.ts
  - + серьёзный баг в обычной работе (вред 0.92, частота 0.85)
  - + прямо про ваше использование (2.73/3)

**#5663** [feat(active-memory): inject always-check memories into agent system prompt on every wake (VOG-5736)](https://github.com/paperclipai/paperclip/pull/5663)
`фича` · Claude-адаптер · автор @vg-jerry · балл **82.5** · 678+1 строк · None дн. · CI: no_ci
  - ✗ конфликт с основной веткой и взятыми PR: execute.ts
  - + сильная фича (ценность 3.45/4, новизна 0.69)
  - + прямо про ваше использование (2.94/3)

**#5674** [fix: deep-merge runtimeConfig on PATCH instead of full column replace](https://github.com/paperclipai/paperclip/pull/5674)
`фикс` · CLI и API · автор @notandrewblejde · балл **82.1** · 355+16 строк · None дн. · CI: green
  - ✗ конфликт с основной веткой и взятыми PR: agents.ts, queryKeys.ts, Agents.tsx
  - ✗ код не совпадает с описанием (0.11)
  - + серьёзный баг в обычной работе (вред 0.91, частота 0.81)
  - + прямо про ваше использование (2.76/3)

**#12031** [fix(issues): arm a default wait monitor when an interaction parks the issue](https://github.com/paperclipai/paperclip/pull/12031)
`фикс` · Задачи и согласования · автор @juancarlosrial76-code · балл **82.0** · 534+1 строк · None дн. · CI: green
  - ✗ конфликт с основной веткой и взятыми PR: issues.ts
  - + серьёзный баг в обычной работе (вред 0.73, частота 0.89)
  - + прямо про ваше использование (2.73/3)

**#12930** [fix(claude-local): keep mcpServerIdentity and remoteExecution in the session codec](https://github.com/paperclipai/paperclip/pull/12930)
`фикс` · Claude-адаптер · автор @qwlong · балл **82.0** · 94+0 строк · None дн. · CI: red
  - ✗ конфликт с основной веткой и взятыми PR: adapter-session-codecs.test.ts
  - ! падают тесты CI: ci / Verify serialized server suites (5/5)
  - + серьёзный баг в обычной работе (вред 0.61, частота 0.87)
  - + прямо про ваше использование (2.98/3)

**#3497** [[codex] Add agent model failover chains](https://github.com/paperclipai/paperclip/pull/3497)
`фича` · Запуски и heartbeat · автор @akshitnanda · балл **81.8** · 531+48 строк · None дн. · CI: green
  - ✗ конфликт с основной веткой и взятыми PR: index.ts, build-config.ts, build-config.test.ts
  - + сильная фича (ценность 3.38/4, новизна 0.84)
  - + прямо про ваше использование (2.84/3)

**#13223** [fix(api): reject unknown keys in issue mutation bodies](https://github.com/paperclipai/paperclip/pull/13223)
`фикс` · Задачи и согласования · автор @trixy-the-ai-bot · балл **81.7** · 269+14 строк · None дн. · CI: green
  - ✗ конфликт с основной веткой и взятыми PR: issue.ts
  - + серьёзный баг в обычной работе (вред 0.81, частота 0.68)
  - + прямо про ваше использование (2.7/3)

**#13056** [fix(cross-issue-limit): allow heartbeat_timer runs to write to checked-out issues (INUA-6799)](https://github.com/paperclipai/paperclip/pull/13056)
`фикс` · Задачи и согласования · автор @rotem-zecharia · балл **81.7** · 99+6 строк · None дн. · CI: green
  - ✗ конфликт с основной веткой и взятыми PR: heartbeat-issue-liveness-escalation.test.ts
  - ! рискованная область (0.65)
  - + серьёзный баг в обычной работе (вред 0.9, частота 0.82)
  - + прямо про ваше использование (2.96/3)

**#13950** [feat(budgets): add native calendar_day_utc budget window](https://github.com/paperclipai/paperclip/pull/13950)
`фича` · Задачи и согласования · автор @biokub-agent · балл **81.4** · 297+39 строк · None дн. · CI: flaky_only
  - ✗ код не совпадает с описанием (0.49)
  - + сильная фича (ценность 3.56/4, новизна 0.91)

**#11558** [fix(adapter-utils): strip server secrets from agent env](https://github.com/paperclipai/paperclip/pull/11558)
`безопасность` · Claude-адаптер · автор @Doom121212 · балл **81.4** · 91+4 строк · None дн. · CI: red
  - ✗ конфликт с основной веткой и взятыми PR: execute.ts, spawn-smoke.test.ts, acpx@0.12.0.patch
  - ! падают тесты CI: verify, General tests (workspaces-b)
  - + серьёзный баг в обычной работе (вред 0.9, частота 0.84)
  - + прямо про ваше использование (2.74/3)

**#11923** [fix(acpx): keep projected secrets off the persisted session env](https://github.com/paperclipai/paperclip/pull/11923)
`безопасность` · Прочее · автор @alaimster · балл **81.4** · 156+24 строк · None дн. · CI: green
  - ✗ конфликт с основной веткой и взятыми PR: execute.ts, acpx@0.12.0.patch
  - + серьёзный баг в обычной работе (вред 0.93, частота 0.8)
  - + прямо про ваше использование (2.76/3)

**#11367** [feat(adapter-utils): opt-in allowlist for agent env inheritance](https://github.com/paperclipai/paperclip/pull/11367)
`безопасность` · Другие адаптеры · автор @marijnp7 · балл **81.4** · 436+25 строк · None дн. · CI: green
  - ✗ конфликт с основной веткой и взятыми PR: execute.ts, test.ts, execute.ts
  - + серьёзный баг в обычной работе (вред 0.88, частота 0.76)
  - + прямо про ваше использование (2.94/3)

**#12002** [fix(approvals): auto-transition in_review issues and wake agents on card rejection](https://github.com/paperclipai/paperclip/pull/12002)
`фикс` · Задачи и согласования · автор @rotem-zecharia · балл **81.3** · 580+3 строк · None дн. · CI: flaky_only
  - ✗ код не совпадает с описанием (0.16)
  - + серьёзный баг в обычной работе (вред 0.82, частота 0.82)
  - + прямо про ваше использование (2.61/3)

**#13197** [fix(ui): submit stage decisions with required comments](https://github.com/paperclipai/paperclip/pull/13197)
`фича` · Интерфейс · автор @JamesSparkMojo · балл **81.3** · 288+4 строк · None дн. · CI: flaky_only
  - ✗ конфликт с основной веткой и взятыми PR: IssueProperties.tsx
  - + сильная фича (ценность 3.32/4, новизна 0.91)

**#6162** [Fix skill mention UUID/slug dispatch resolution](https://github.com/paperclipai/paperclip/pull/6162)
`фикс` · Запуски и heartbeat · автор @ryanclark2 · балл **81.2** · 143+4 строк · None дн. · CI: green
  - ✗ конфликт с основной веткой и взятыми PR: heartbeat-project-env.test.ts, issues-service.test.ts, issues.ts
  - + серьёзный баг в обычной работе (вред 0.89, частота 0.75)
  - + прямо про ваше использование (2.77/3)

**#13138** [fix(server): add durable zombie-session reaper for claude_local runs](https://github.com/paperclipai/paperclip/pull/13138)
`фикс` · Запуски и heartbeat · автор @daniel-mariani · балл **81.1** · 818+5 строк · None дн. · CI: green
  - ✗ конфликт с основной веткой и взятыми PR: native-session-resumption.test.ts
  - ! баг не критичный или редкий
  - + прямо про ваше использование (2.96/3)

**#7541** [feat(llm): OpenAI-compatible baseUrl + runtime API URL/CLI robustness fixes](https://github.com/paperclipai/paperclip/pull/7541)
`фича` · CLI и API · автор @oups75 · балл **81.1** · 196+35 строк · None дн. · CI: flaky_only
  - ✗ конфликт с основной веткой и взятыми PR: package.json, index.ts, config-schema.test.ts
  - ! фича меняет поведение по умолчанию
  - + сильная фича (ценность 3.32/4, новизна 0.83)
  - + прямо про ваше использование (2.75/3)

**#13995** [fix(sandbox-kubernetes): stop pointing built-in adapter defaults at a never-published :v1 tag](https://github.com/paperclipai/paperclip/pull/13995)
`фикс` · Деплой и self-host · автор @BluePhi09 · балл **81.0** · 269+14 строк · None дн. · CI: green
  - ✗ код не совпадает с описанием (0.16)
  - + серьёзный баг в обычной работе (вред 0.8, частота 0.66)
  - + прямо про ваше использование (2.88/3)

**#9588** [fix: prevent project environment values from leaking through API responses](https://github.com/paperclipai/paperclip/pull/9588)
`безопасность` · Задачи и согласования · автор @cablackmon · балл **81.0** · 578+26 строк · None дн. · CI: green
  - ✗ конфликт с основной веткой и взятыми PR: index.ts, project.ts, issues.ts
  - + серьёзный баг в обычной работе (вред 0.92, частота 0.78)
  - + прямо про ваше использование (2.77/3)

**#8472** [feat(claude-local): --fallback-model so transient 529/overload bumps model instead of failing the run](https://github.com/paperclipai/paperclip/pull/8472)
`фича` · Claude-адаптер · автор @joegalbert-ai · балл **80.3** · 180+0 строк · None дн. · CI: flaky_only
  - ✗ конфликт с основной веткой и взятыми PR: index.ts, execute.ts
  - ! фича меняет поведение по умолчанию
  - + сильная фича (ценность 3.05/4, новизна 0.76)
  - + прямо про ваше использование (2.84/3)

**#6042** [feat: auto-inject text attachment content in heartbeat-context + bridge allowlist](https://github.com/paperclipai/paperclip/pull/6042)
`фича` · Задачи и согласования · автор @firepol-ai · балл **80.2** · 310+12 строк · None дн. · CI: green
  - ✗ конфликт с основной веткой и взятыми PR: attachment-types.test.ts, attachment-types.ts, issues.ts
  - ✗ код не совпадает с описанием (0.41)
  - ! фича меняет поведение по умолчанию
  - + сильная фича (ценность 3.45/4, новизна 0.75)
  - + прямо про ваше использование (2.71/3)

**#4597** [fix: bump drizzle-orm to ^0.41.0 to satisfy better-auth peer dep](https://github.com/paperclipai/paperclip/pull/4597)
`фикс` · Прочее · автор @mbradaschia · балл **80.2** · 18+23 строк · None дн. · CI: red
  - ✗ конфликт с основной веткой и взятыми PR: package.json, package.json, pnpm-lock.yaml
  - ! падают тесты CI: policy
  - + серьёзный баг в обычной работе (вред 0.94, частота 0.81)
  - + прямо про ваше использование (2.84/3)

**#12649** [fix(server): redact agent profile configuration by default](https://github.com/paperclipai/paperclip/pull/12649)
`безопасность` · CLI и API · автор @samikujakanto · балл **80.1** · 942+51 строк · None дн. · CI: red
  - ✗ конфликт с основной веткой и взятыми PR: low-trust-red-team-routes.test.ts, redaction.test.ts, agents.ts
  - ✗ код не совпадает с описанием (0.22)
  - ! падают тесты CI: ci / Verify serialized server suites (2/5)
  - + серьёзный баг в обычной работе (вред 0.93, частота 0.65)
  - + прямо про ваше использование (2.54/3)

**#13966** [feat(ui): move and delete tasks from context menus](https://github.com/paperclipai/paperclip/pull/13966)
`фича` · Задачи и согласования · автор @luizvb · балл **79.8** · 603+12 строк · None дн. · CI: green
  - ✗ код не совпадает с описанием (0.41)
  - ! фича полезная, но не ключевая
  - ! фича меняет поведение по умолчанию

**#3885** [Company run toggle](https://github.com/paperclipai/paperclip/pull/3885)
`фича` · Запуски и heartbeat · автор @Micsi · балл **79.7** · 685+10 строк · None дн. · CI: green
  - ✗ конфликт с основной веткой и взятыми PR: heartbeat-process-recovery.test.ts, companies.ts, heartbeat.ts
  - + сильная фича (ценность 3.54/4, новизна 0.81)
  - + прямо про ваше использование (2.56/3)

**#2642** [fix: redact Paperclip secrets from logs and Codex artifacts](https://github.com/paperclipai/paperclip/pull/2642)
`безопасность` · Codex-адаптер · автор @halfwitgaslit · балл **79.6** · 376+13 строк · None дн. · CI: green
  - ✗ конфликт с основной веткой и взятыми PR: codex-home.ts, execute.ts, codex-local-execute.test.ts
  - + серьёзный баг в обычной работе (вред 0.89, частота 0.7)
  - + прямо про ваше использование (2.9/3)

**#11073** [fix(claude-local): classify an unrefreshable OAuth session as auth required](https://github.com/paperclipai/paperclip/pull/11073)
`фикс` · Claude-адаптер · автор @juancarlosrial76-code · балл **79.5** · 36+1 строк · None дн. · CI: green
  - ✗ конфликт с основной веткой и взятыми PR: parse.test.ts, parse.ts
  - + серьёзный баг в обычной работе (вред 0.9, частота 0.69)
  - + прямо про ваше использование (2.91/3)

**#10104** [fix(server/approvals): wake requester on reject and request-revision](https://github.com/paperclipai/paperclip/pull/10104)
`фикс` · Задачи и согласования · автор @nydamon · балл **79.5** · 264+72 строк · None дн. · CI: flaky_only
  - ✗ конфликт с основной веткой и взятыми PR: approvals.ts
  - + серьёзный баг в обычной работе (вред 0.72, частота 0.86)
  - + прямо про ваше использование (2.92/3)

**#5631** [fix(api): prevent update wiping secret bindings](https://github.com/paperclipai/paperclip/pull/5631)
`фикс` · AI-подключения и доступ · автор @freddiecoleman · балл **79.4** · 68+5 строк · None дн. · CI: green
  - ✗ конфликт с основной веткой и взятыми PR: agents.ts
  - + серьёзный баг в обычной работе (вред 0.93, частота 0.58)
  - + прямо про ваше использование (2.93/3)

**#13630** [fix(ui): present choice questions a stored question set leaves out](https://github.com/paperclipai/paperclip/pull/13630)
`фикс` · Интерфейс · автор @GustavoLarcoDev · балл **79.3** · 253+46 строк · None дн. · CI: green
  - ✗ конфликт с основной веткой и взятыми PR: issue-thread-interactions.test.ts
  - + серьёзный баг в обычной работе (вред 0.87, частота 0.66)
  - + прямо про ваше использование (2.65/3)

**#13117** [fix(issues): read the checkout lock's premise instead of inferring it from status](https://github.com/paperclipai/paperclip/pull/13117)
`фикс` · Задачи и согласования · автор @jayproulx · балл **79.3** · 219+5 строк · None дн. · CI: flaky_only
  - ✗ конфликт с основной веткой и взятыми PR: issues.ts
  - + серьёзный баг в обычной работе (вред 0.86, частота 0.58)
  - + прямо про ваше использование (2.83/3)

**#6373** [fix: redact runtime secret values in run logs](https://github.com/paperclipai/paperclip/pull/6373)
`безопасность` · Запуски и heartbeat · автор @jasondbramley · балл **79.2** · 124+7 строк · None дн. · CI: green
  - ✗ конфликт с основной веткой и взятыми PR: command-redaction.test.ts, command-redaction.ts, redaction.test.ts
  - + серьёзный баг в обычной работе (вред 0.9, частота 0.74)
  - + прямо про ваше использование (2.65/3)

**#1788** [fix(server): restore issue comment cursor pagination](https://github.com/paperclipai/paperclip/pull/1788)
`фикс` · Задачи и согласования · автор @yoyooyooo · балл **79.0** · 87+9 строк · None дн. · CI: green
  - ✗ конфликт с основной веткой и взятыми PR: issues.ts
  - + серьёзный баг в обычной работе (вред 0.81, частота 0.65)
  - + прямо про ваше использование (2.94/3)

**#8205** [fix(shared): store multiline text verbatim, stop eating \r/\n escapes (RENA-14562)](https://github.com/paperclipai/paperclip/pull/8205)
`фикс` · Задачи и согласования · автор @rendedennis6-byte · балл **78.8** · 53+25 строк · None дн. · CI: red
  - ✗ конфликт с основной веткой и взятыми PR: issue.test.ts
  - ! падают тесты CI: verify, General tests (server)
  - + серьёзный баг в обычной работе (вред 0.9, частота 0.59)
  - + прямо про ваше использование (2.85/3)

**#12581** [fix(server): fail closed on secret-shaped issue comments](https://github.com/paperclipai/paperclip/pull/12581)
`безопасность` · Задачи и согласования · автор @apex-skyner · балл **78.7** · 246+7 строк · None дн. · CI: red
  - ✗ конфликт с основной веткой и взятыми PR: issues-service.test.ts, redaction.test.ts, redaction.ts
  - ! падают тесты CI: ci / verify, ci / General tests (server (3/5)), ci / General tests (server (4/5)), ci / Verify serialized server suites 
  - + серьёзный баг в обычной работе (вред 0.91, частота 0.64)

**#7002** [feat(claude-local): load per-agent .env on spawn (JDD-133)](https://github.com/paperclipai/paperclip/pull/7002)
`фича` · Claude-адаптер · автор @gabi-JD · балл **78.7** · 502+12 строк · None дн. · CI: red
  - ✗ конфликт с основной веткой и взятыми PR: package.json, execute.ts, index.ts
  - ! падают тесты CI: verify, policy
  - + сильная фича (ценность 3.01/4, новизна 0.77)
  - + прямо про ваше использование (2.94/3)

**#8447** [feat(inbox): surface pending agent→human asks as "Waiting on you"](https://github.com/paperclipai/paperclip/pull/8447)
`фича` · Интерфейс · автор @Tr1ckyMag1ca1 · балл **78.6** · 567+11 строк · None дн. · CI: red
  - ✗ конфликт с основной веткой и взятыми PR: constants.ts, index.ts, inbox-dismissals.ts
  - ! падают тесты CI: Verify serialized server suites (2/4)
  - ! фича меняет поведение по умолчанию
  - + сильная фича (ценность 3.12/4, новизна 0.84)
  - + прямо про ваше использование (2.64/3)

**#2388** [feat(ui): add user management UI to company settings](https://github.com/paperclipai/paperclip/pull/2388)
`фича` · Интерфейс · автор @vbalko-claimate · балл **78.6** · 693+5 строк · None дн. · CI: green
  - ✗ конфликт с основной веткой и взятыми PR: app.ts, access.ts, Layout.tsx
  - ! фича меняет поведение по умолчанию
  - + сильная фича (ценность 3.93/4, новизна 0.91)
  - + прямо про ваше использование (2.71/3)

**#7757** [fix: handle EPIPE on adapter stdin.write after pipe close](https://github.com/paperclipai/paperclip/pull/7757)
`фикс` · Прочее · автор @exocode · балл **78.4** · 36+1 строк · None дн. · CI: green
  - ✗ конфликт с основной веткой и взятыми PR: server-utils.test.ts
  - + серьёзный баг в обычной работе (вред 0.76, частота 0.64)
  - + прямо про ваше использование (2.64/3)

**#5833** [feat(harness): runtime orphan reaper + pre-spawn process guard](https://github.com/paperclipai/paperclip/pull/5833)
`фича` · Запуски и heartbeat · автор @ddemid · балл **78.4** · 428+8 строк · None дн. · CI: green
  - ✗ конфликт с основной веткой и взятыми PR: heartbeat-stale-queue-invalidation.test.ts, index.ts, heartbeat.ts
  - ✗ код не совпадает с описанием (0.41)
  - ! фича полезная, но не ключевая
  - ! фича меняет поведение по умолчанию
  - + прямо про ваше использование (2.97/3)

**#11945** [[INUA-6044] fix(approvals): wake linked-issue assignees on card approval](https://github.com/paperclipai/paperclip/pull/11945)
`фикс` · Задачи и согласования · автор @rotem-zecharia · балл **78.3** · 179+0 строк · None дн. · CI: flaky_only
  - ✗ конфликт с основной веткой и взятыми PR: approval-routes-idempotency.test.ts
  - ! баг не критичный или редкий
  - + прямо про ваше использование (2.74/3)

**#1862** [feat: add raigo governance skill for AI policy enforcement](https://github.com/paperclipai/paperclip/pull/1862)
`фича` · Коннекторы и MCP · автор @musharsec · балл **78.2** · 170+0 строк · None дн. · CI: flaky_only
  - ✗ продвигает сторонний сервис (0.72)
  - + сильная фича (ценность 3.7/4, новизна 0.86)

**#8972** [feat(approvals): require a reason or explicit force when rejecting](https://github.com/paperclipai/paperclip/pull/8972)
`фича` · Задачи и согласования · автор @souravsachin · балл **78.0** · 402+10 строк · None дн. · CI: green
  - ✗ конфликт с основной веткой и взятыми PR: Approvals.tsx
  - ! фича меняет поведение по умолчанию
  - + сильная фича (ценность 3.06/4, новизна 0.87)
  - + прямо про ваше использование (2.56/3)

**#13992** [feat(ui): add project status picker to the project detail page](https://github.com/paperclipai/paperclip/pull/13992)
`фича` · Интерфейс · автор @b3nnb · балл **77.9** · 372+15 строк · None дн. · CI: red
  - ✗ конфликт с основной веткой и взятыми PR: ProjectDetail.test.tsx
  - ! падают тесты CI: ci / verify, ci / General tests (chat (1/3)), ci / Verify Paperclip Runner (vitest 1/2)
  - + сильная фича (ценность 3.03/4, новизна 0.9)

**#13926** [fix: allow taskless runs to update their assigned issues](https://github.com/paperclipai/paperclip/pull/13926)
`фикс` · Задачи и согласования · автор @wyi184246-creator · балл **77.8** · 415+25 строк · None дн. · CI: green
  - ✗ конфликт с основной веткой и взятыми PR: cross-issue-influence-limit.ts
  - ✗ код не совпадает с описанием (0.38)
  - ! рискованная область (0.52)
  - + серьёзный баг в обычной работе (вред 0.84, частота 0.71)
  - + прямо про ваше использование (2.83/3)

**#13927** [fix(claude-local): fail Opus 5.5 ACP runs early when the bundled Claude Code is too old](https://github.com/paperclipai/paperclip/pull/13927)
`фикс` · Claude-адаптер · автор @kimnamu · балл **77.8** · 164+7 строк · None дн. · CI: red
  - ✗ конфликт с основной веткой и взятыми PR: acp.ts
  - ! падают тесты CI: ci / verify, ci / General tests (chat (1/3))
  - + серьёзный баг в обычной работе (вред 0.67, частота 0.71)
  - + прямо про ваше использование (2.8/3)

**#10532** [fix(task-watchdogs): stop re-waking valid human-blocked leaves / self-inflicted fingerprint churn (JAC-3989)](https://github.com/paperclipai/paperclip/pull/10532)
`фикс` · Запуски и heartbeat · автор @JackReis · балл **77.8** · 205+712 строк · None дн. · CI: green
  - ✗ код не совпадает с описанием (0.18)
  - ! лишние изменения в дифе
  - + серьёзный баг в обычной работе (вред 0.83, частота 0.7)
  - + прямо про ваше использование (2.63/3)

**#12738** [fix(interactions): raise custom target key limit and tolerate unparseable stored payloads in scans](https://github.com/paperclipai/paperclip/pull/12738)
`фикс` · Задачи и согласования · автор @EbrahimProgrammer · балл **77.7** · 66+5 строк · None дн. · CI: red
  - ✗ конфликт с основной веткой и взятыми PR: issue.ts, issue-thread-interactions.ts
  - ! падают тесты CI: ci / verify, ci / General tests (server (3/5))
  - + серьёзный баг в обычной работе (вред 0.92, частота 0.49)
  - + прямо про ваше использование (2.7/3)

**#13052** [feat(audit): add run-recall search over runs and activity](https://github.com/paperclipai/paperclip/pull/13052)
`фича` · Запуски и heartbeat · автор @tejasghalsasi · балл **77.6** · 980+15 строк · None дн. · CI: flaky_only
  - ✗ конфликт с основной веткой и взятыми PR: heartbeats.ts
  - + сильная фича (ценность 3.24/4, новизна 0.88)

**#4386** [feat(plugin-events): enrich agent.run.* payload with issue context + result](https://github.com/paperclipai/paperclip/pull/4386)
`фича` · Запуски и heartbeat · автор @Bricol1982 · балл **77.6** · 76+24 строк · None дн. · CI: green
  - ✗ конфликт с основной веткой и взятыми PR: heartbeat.ts
  - ! фича меняет поведение по умолчанию
  - + сильная фича (ценность 3.49/4, новизна 0.79)
  - + прямо про ваше использование (2.72/3)

**#13897** [fix(claude-local): enforce deny-first tools by agent role (SOL-3188 Step 1)](https://github.com/paperclipai/paperclip/pull/13897)
`безопасность` · Claude-адаптер · автор @yackovleff-solved · балл **77.1** · 66+4 строк · None дн. · CI: flaky_only
  - ✗ конфликт с основной веткой и взятыми PR: index.ts, permissions.test.ts, permissions.ts
  - ! рискованная область (0.75)
  - + серьёзный баг в обычной работе (вред 0.94, частота 0.71)
  - + прямо про ваше использование (2.97/3)

**#12534** [fix(acpx-engine): materialize Claude runtime skills into project cwd](https://github.com/paperclipai/paperclip/pull/12534)
`фикс` · Claude-адаптер · автор @Danne-J · балл **77.1** · 206+37 строк · None дн. · CI: flaky_only
  - ✗ конфликт с основной веткой и взятыми PR: execute.ts, server-utils.ts
  - + серьёзный баг в обычной работе (вред 0.8, частота 0.61)
  - + прямо про ваше использование (2.78/3)

**#12287** [fix(codex-local): write http_headers so codex sends the MCP gateway bearer token](https://github.com/paperclipai/paperclip/pull/12287)
`фикс` · Codex-адаптер · автор @zannis · балл **77.1** · 6+2 строк · None дн. · CI: green
  - ✗ конфликт с основной веткой и взятыми PR: codex-home.test.ts
  - + серьёзный баг в обычной работе (вред 0.75, частота 0.78)
  - + прямо про ваше использование (2.81/3)

**#11413** [fix(recovery): retry transient adapter failures on a monitor instead of blocking](https://github.com/paperclipai/paperclip/pull/11413)
`фикс` · Запуски и heartbeat · автор @dzianisv · балл **77.1** · 496+39 строк · None дн. · CI: green
  - ✗ конфликт с основной веткой и взятыми PR: heartbeat.ts, service.ts
  - + серьёзный баг в обычной работе (вред 0.89, частота 0.72)
  - + прямо про ваше использование (2.73/3)

**#5468** [feat: multi-select issues with batch actions in list view (LAC-459)](https://github.com/paperclipai/paperclip/pull/5468)
`фича` · Задачи и согласования · автор @lacymorrow · балл **77.1** · 844+4 строк · None дн. · CI: green
  - ✗ конфликт с основной веткой и взятыми PR: issues.ts, issues.ts, IssuesList.tsx
  - + сильная фича (ценность 3.4/4, новизна 0.89)

**#10616** [fix(recovery): recognize provider quota exhaustion on the ACP path](https://github.com/paperclipai/paperclip/pull/10616)
`фикс` · Запуски и heartbeat · автор @MrBlackTongue · балл **77.0** · 716+232 строк · None дн. · CI: green
  - ✗ конфликт с основной веткой и взятыми PR: execute.ts, parse.ts, provider-failure-classification.test.ts
  - ! баг не критичный или редкий
  - + прямо про ваше использование (2.89/3)

**#9073** [fix(issues): reject unknown monitor policy fields instead of silently dropping them](https://github.com/paperclipai/paperclip/pull/9073)
`фикс` · Задачи и согласования · автор @dosthcpp · балл **77.0** · 133+1 строк · None дн. · CI: green
  - ✗ конфликт с основной веткой и взятыми PR: issue.test.ts, issue.ts
  - + серьёзный баг в обычной работе (вред 0.72, частота 0.8)
  - + прямо про ваше использование (2.7/3)

**#13812** [feat(apps): add Glasser as a self-serve MCP connection](https://github.com/paperclipai/paperclip/pull/13812)
`фича` · Коннекторы и MCP · автор @glasserai · балл **76.9** · 171+19 строк · None дн. · CI: green
  - ✗ конфликт с основной веткой и взятыми PR: app-definitions.generated.ts, app-definitions.test.ts, ingest-app-definitions.mjs
  - ✗ продвигает сторонний сервис (0.9)
  - + сильная фича (ценность 3.34/4, новизна 0.78)

**#13321** [fix(codex): pass MCP bearer tokens through env](https://github.com/paperclipai/paperclip/pull/13321)
`фикс` · Codex-адаптер · автор @iceFusion101 · балл **76.9** · 28+9 строк · None дн. · CI: green
  - ✗ конфликт с основной веткой и взятыми PR: codex-home.test.ts, codex-home.ts
  - + серьёзный баг в обычной работе (вред 0.83, частота 0.55)
  - + прямо про ваше использование (2.69/3)

**#7415** [Enforce heartbeat cooldown on automatic agent wakeups](https://github.com/paperclipai/paperclip/pull/7415)
`фича` · Запуски и heartbeat · автор @alejandroiglesias · балл **76.9** · 777+31 строк · None дн. · CI: flaky_only
  - ✗ конфликт с основной веткой и взятыми PR: index.ts, agent.ts, index.ts
  - + сильная фича (ценность 3.04/4, новизна 0.74)
  - + прямо про ваше использование (2.7/3)

**#11623** [fix(recovery): stop terminal-run recovery from stranding, flapping, and destroying live monitors](https://github.com/paperclipai/paperclip/pull/11623)
`фикс` · Запуски и heartbeat · автор @dzianisv · балл **76.8** · 593+3 строк · None дн. · CI: flaky_only
  - ✗ конфликт с основной веткой и взятыми PR: service.ts
  - + серьёзный баг в обычной работе (вред 0.86, частота 0.62)
  - + прямо про ваше использование (2.86/3)

**#7724** [fix(security): redact transcript artifacts before persistence](https://github.com/paperclipai/paperclip/pull/7724)
`безопасность` · Codex-адаптер · автор @misterbusiness1 · балл **76.8** · 425+4 строк · None дн. · CI: green
  - ✗ конфликт с основной веткой и взятыми PR: execute.ts, run-log-store.ts
  - + серьёзный баг в обычной работе (вред 0.89, частота 0.76)
  - + прямо про ваше использование (2.71/3)

**#3481** [fix(server): alias assigneeId to assigneeAgentId in POST /issues](https://github.com/paperclipai/paperclip/pull/3481)
`фикс` · Задачи и согласования · автор @outlawmold · балл **76.8** · 180+17 строк · None дн. · CI: red
  - ✗ конфликт с основной веткой и взятыми PR: package.json, execute.ts, test.ts
  - ✗ код не совпадает с описанием (0.03)
  - ! падают тесты CI: policy
  - ! лишние изменения в дифе
  - + серьёзный баг в обычной работе (вред 0.62, частота 0.87)
  - + прямо про ваше использование (2.86/3)

**#4473** [fix(db): add ON DELETE rules to issue-related foreign keys](https://github.com/paperclipai/paperclip/pull/4473)
`фикс` · Задачи и согласования · автор @alexlomt · балл **76.7** · 191+6 строк · None дн. · CI: green
  - ✗ конфликт с основной веткой и взятыми PR: client.test.ts, _journal.json
  - ! рискованная область (0.54)
  - + серьёзный баг в обычной работе (вред 0.91, частота 0.86)
  - + прямо про ваше использование (2.71/3)

**#8919** [fix(issues): same-agent stale checkout release/adopt across run boundary](https://github.com/paperclipai/paperclip/pull/8919)
`фикс` · Задачи и согласования · автор @florianpollstaetter-dot · балл **76.6** · 224+32 строк · None дн. · CI: green
  - ✗ конфликт с основной веткой и взятыми PR: issues.ts
  - + серьёзный баг в обычной работе (вред 0.88, частота 0.75)
  - + прямо про ваше использование (2.93/3)

**#13467** [fix(claude-local): use --append-system-prompt instead of unsupported -file flag](https://github.com/paperclipai/paperclip/pull/13467)
`фикс` · Claude-адаптер · автор @arnaud-gp · балл **76.5** · 36+37 строк · None дн. · CI: flaky_only
  - ✗ конфликт с основной веткой и взятыми PR: execute.remote.test.ts
  - ! баг не критичный или редкий
  - + прямо про ваше использование (2.72/3)

**#11121** [fix(adapter-utils): authenticate the wake payload so agents can trust it](https://github.com/paperclipai/paperclip/pull/11121)
`безопасность` · Запуски и heartbeat · автор @Nissimmiracles · балл **76.3** · 186+9 строк · None дн. · CI: green
  - ✗ конфликт с основной веткой и взятыми PR: server-utils.test.ts, server-utils.ts, execute.ts
  - ! рискованная область (0.59)
  - + серьёзный баг в обычной работе (вред 0.86, частота 0.82)
  - + прямо про ваше использование (2.95/3)

**#6426** [feat: estimateSubscriptionSpendCents for claude-local (RFC #5066)](https://github.com/paperclipai/paperclip/pull/6426)
`фича` · Claude-адаптер · автор @Jolley71717 · балл **76.3** · 314+5 строк · None дн. · CI: green
  - ✗ конфликт с основной веткой и взятыми PR: index.ts, execute.ts, heartbeat.ts
  - ! фича полезная, но не ключевая
  - + прямо про ваше использование (2.82/3)

**#11797** [fix(adapter-utils): block server-only credentials at all agent spawns](https://github.com/paperclipai/paperclip/pull/11797)
`безопасность` · Другие адаптеры · автор @nearfolk · балл **76.2** · 267+27 строк · None дн. · CI: red
  - ✗ конфликт с основной веткой и взятыми PR: execute.ts, spawn-smoke.test.ts, server-utils.test.ts
  - ✗ код не совпадает с описанием (0.42)
  - ! падают тесты CI: Verify serialized server suites (3/5)
  - + серьёзный баг в обычной работе (вред 0.94, частота 0.58)
  - + прямо про ваше использование (2.72/3)

**#12611** [fix(tool-gateway): stop mapping application-level tools/call errors to raw HTTP 404/400 on the named MCP gateway](https://github.com/paperclipai/paperclip/pull/12611)
`фикс` · Коннекторы и MCP · автор @Quentin-M · балл **76.1** · 94+1 строк · None дн. · CI: flaky_only
  - ✗ конфликт с основной веткой и взятыми PR: tool-gateway.ts
  - ! баг не критичный или редкий
  - + прямо про ваше использование (2.85/3)

**#3131** [fix(adapters/process): inject PAPERCLIP_RUN_ID + PAPERCLIP_API_KEY into spawned env](https://github.com/paperclipai/paperclip/pull/3131)
`фикс` · Другие адаптеры · автор @iws17 · балл **76.0** · 163+1 строк · None дн. · CI: green
  - ✗ конфликт с основной веткой и взятыми PR: execute.ts
  - + серьёзный баг в обычной работе (вред 0.72, частота 0.74)
  - + прямо про ваше использование (2.91/3)

**#3910** [fix(issues): slug-mention resolver + UUID validation for @agent wakes](https://github.com/paperclipai/paperclip/pull/3910)
`фикс` · Задачи и согласования · автор @kbecking · балл **76.0** · 677+13 строк · None дн. · CI: green
  - ✗ конфликт с основной веткой и взятыми PR: events.ts, index.ts, types.ts
  - + серьёзный баг в обычной работе (вред 0.57, частота 0.74)
  - + прямо про ваше использование (2.95/3)

**#13550** [fix(server): bind run attribution after verified checkout](https://github.com/paperclipai/paperclip/pull/13550)
`фикс` · Задачи и согласования · автор @kallehiitola · балл **75.9** · 337+5 строк · None дн. · CI: flaky_only
  - ✗ конфликт с основной веткой и взятыми PR: cross-issue-influence-limit-postgres.test.ts, issues.ts
  - ! баг не критичный или редкий
  - + прямо про ваше использование (2.79/3)

**#13644** [fix(acpx-engine): classify a provider quota wall as a quota wait](https://github.com/paperclipai/paperclip/pull/13644)
`фикс` · Claude-адаптер · автор @Siber704 · балл **75.8** · 62+3 строк · None дн. · CI: flaky_only
  - ✗ конфликт с основной веткой и взятыми PR: execute.ts
  - ! баг не критичный или редкий
  - + прямо про ваше использование (2.69/3)

**#10468** [feat(claude-local): OpenRouter fallback on Anthropic 529 Overloaded](https://github.com/paperclipai/paperclip/pull/10468)
`фича` · Claude-адаптер · автор @ericdfields · балл **75.8** · 424+2 строк · None дн. · CI: flaky_only
  - ✗ конфликт с основной веткой и взятыми PR: execute.ts, parse.ts
  - ✗ продвигает сторонний сервис (0.51)
  - ! фича полезная, но не ключевая
  - + прямо про ваше использование (2.73/3)

**#10081** [feat(server): include scoped project and milestone intake in wake payload](https://github.com/paperclipai/paperclip/pull/10081)
`фича` · Запуски и heartbeat · автор @Joshtt23 · балл **75.8** · 887+15 строк · None дн. · CI: green
  - ✗ конфликт с основной веткой и взятыми PR: SPEC-implementation.md, server-utils.test.ts, server-utils.ts
  - ! фича меняет поведение по умолчанию
  - + сильная фича (ценность 3.05/4, новизна 0.72)
  - + прямо про ваше использование (2.68/3)

**#3823** [fix: include server port in derived auth trusted origins](https://github.com/paperclipai/paperclip/pull/3823)
`фикс` · AI-подключения и доступ · автор @Helmi · балл **75.8** · 147+2 строк · None дн. · CI: green
  - ✗ конфликт с основной веткой и взятыми PR: better-auth.ts
  - + серьёзный баг в обычной работе (вред 0.83, частота 0.7)
  - + прямо про ваше использование (2.95/3)


## Не дошли до этапа 2 — только балл этапа 1, вердикта нет (2868)

**#12842** [fix(agents): merge runtimeConfig on PATCH instead of replacing the column](https://github.com/paperclipai/paperclip/pull/12842)
`фикс` · CLI и API · автор @vveliev · балл **85.0** · 199+5 строк · None дн. · CI: —

**#13726** [fix(ai-connections): rotate Claude subscription credentials from a file](https://github.com/paperclipai/paperclip/pull/13726)
`фикс` · AI-подключения и доступ · автор @vobornik · балл **82.6** · 153+19 строк · None дн. · CI: —

**#14039** [fix(claude-local): map thinking effort to the selected model](https://github.com/paperclipai/paperclip/pull/14039)
`фикс` · Claude-адаптер · автор @nctiggy · балл **82.0** · 323+42 строк · None дн. · CI: —

**#10862** [Make agent role editable after creation](https://github.com/paperclipai/paperclip/pull/10862)
`фича` · Интерфейс · автор @lucktastic · балл **81.6** · 127+3 строк · None дн. · CI: —

**#12870** [fix(adapter-utils): strip DATABASE_URL and BETTER_AUTH_SECRET from inherited agent env](https://github.com/paperclipai/paperclip/pull/12870)
`безопасность` · Другие адаптеры · автор @charlieotis · балл **81.5** · 17+0 строк · None дн. · CI: —

**#13833** [fix(server): bind run context to the checked-out issue so taskless runs can write](https://github.com/paperclipai/paperclip/pull/13833)
`фикс` · Задачи и согласования · автор @Pdesengrini · балл **80.4** · 848+9 строк · None дн. · CI: —

**#7432** [fix(issues): resolve identifier to UUID for parentId/descendantOf filters](https://github.com/paperclipai/paperclip/pull/7432)
`фикс` · Задачи и согласования · автор @Sergio-LPA · балл **80.1** · 398+10 строк · None дн. · CI: —

**#3937** [feat(claude-local): add xhigh and max thinking effort options](https://github.com/paperclipai/paperclip/pull/3937)
`фича` · Claude-адаптер · автор @GodsBoy · балл **77.3** · 85+1 строк · None дн. · CI: —

**#14012** [fix(heartbeat): bind run-scoped runtime gateways to their agent](https://github.com/paperclipai/paperclip/pull/14012)
`безопасность` · Запуски и heartbeat · автор @busla · балл **75.9** · 134+0 строк · None дн. · CI: —

**#13924** [fix(ai-connections): rotate Claude subscription credentials from a file](https://github.com/paperclipai/paperclip/pull/13924)
`фикс` · AI-подключения и доступ · автор @danmoc-88 · балл **75.9** · 153+19 строк · None дн. · CI: —

**#13659** [fix(issues): auto-assign issue to creating agent when assigneeAgentId missing (INUA-7276)](https://github.com/paperclipai/paperclip/pull/13659)
`фикс` · Задачи и согласования · автор @rotem-zecharia · балл **75.7** · 194+1 строк · None дн. · CI: —

**#13566** [fix(server): restore top-level redacted adapter secrets on agent update](https://github.com/paperclipai/paperclip/pull/13566)
`фикс` · AI-подключения и доступ · автор @alfirus · балл **75.7** · 33+10 строк · None дн. · CI: —

**#9293** [feat(issues): add trigger date to defer agent work until a scheduled time](https://github.com/paperclipai/paperclip/pull/9293)
`фича` · Задачи и согласования · автор @lacymorrow · балл **75.7** · 291+3 строк · None дн. · CI: —

**#9212** [feat(server): return childIssues array from GET /api/issues/{id}](https://github.com/paperclipai/paperclip/pull/9212)
`фича` · Задачи и согласования · автор @calebsimon-CRAFT · балл **75.7** · 114+8 строк · None дн. · CI: —

**#13650** [fix(server): let a heartbeat run write to the issue it checked out](https://github.com/paperclipai/paperclip/pull/13650)
`фикс` · Задачи и согласования · автор @Abel-Salah · балл **75.6** · 549+28 строк · None дн. · CI: —

**#5784** [Fix DB backup rotation ENOSPC (per-day daily-tier coalesce + free-space guard)](https://github.com/paperclipai/paperclip/pull/5784)
`фикс` · Деплой и self-host · автор @imvimm · балл **75.6** · 305+25 строк · None дн. · CI: —

**#9280** [perf(server): cut auth middleware DB round-trips and make db pool size configurable](https://github.com/paperclipai/paperclip/pull/9280)
`перф` · AI-подключения и доступ · автор @lacymorrow · балл **75.6** · 286+48 строк · None дн. · CI: —

**#6663** [fix(redaction): redact value-based secret patterns in compactRunLogChunk](https://github.com/paperclipai/paperclip/pull/6663)
`безопасность` · Запуски и heartbeat · автор @PAT-Main · балл **75.6** · 93+1 строк · None дн. · CI: —

**#2097** [fix(server): complete FK dependency cleanup in company delete](https://github.com/paperclipai/paperclip/pull/2097)
`фикс` · Прочее · автор @iam-dev · балл **75.6** · 168+8 строк · None дн. · CI: —

**#13060** [feat(runs): add session-log ZIP export for heartbeat runs](https://github.com/paperclipai/paperclip/pull/13060)
`фича` · Запуски и heartbeat · автор @tejasghalsasi · балл **75.5** · 606+0 строк · None дн. · CI: —

**#3856** [fix(agents): preserve sibling keys of runtimeConfig on partial PATCH](https://github.com/paperclipai/paperclip/pull/3856)
`фикс` · CLI и API · автор @sparkeros · балл **75.5** · 12+0 строк · None дн. · CI: —

**#4003** [fix(adapter-utils): non-blocking onLog in runChildProcess](https://github.com/paperclipai/paperclip/pull/4003)
`фикс` · Другие адаптеры · автор @ericnicolaides · балл **75.5** · 56+8 строк · None дн. · CI: —

**#3284** [fix(issues): use resolved UUID instead of identifier in wakeup payloads](https://github.com/paperclipai/paperclip/pull/3284)
`фикс` · Задачи и согласования · автор @kbecking · балл **75.5** · 9+9 строк · None дн. · CI: —

**#13685** [fix(heartbeat): stop electing a sibling workspace's cwd for a run that named another](https://github.com/paperclipai/paperclip/pull/13685)
`фикс` · Воркспейсы и git · автор @simberthon · балл **75.4** · 818+39 строк · None дн. · CI: —

**#10547** [fix(shared,server): treat error as non-invokable across agent lifecycle](https://github.com/paperclipai/paperclip/pull/10547)
`фикс` · Запуски и heartbeat · автор @santhiprakash · балл **75.4** · 42+8 строк · None дн. · CI: —

**#13447** [fix: preserve OAuth refresh access and contain managed MCP config](https://github.com/paperclipai/paperclip/pull/13447)
`фикс` · Codex-адаптер · автор @joeviezner · балл **75.3** · 303+21 строк · None дн. · CI: —

**#13469** [perf(workspaces): stop paying for unused Git scans in the terminal reaper](https://github.com/paperclipai/paperclip/pull/13469)
`перф` · Воркспейсы и git · автор @fayonation · балл **75.2** · 320+17 строк · None дн. · CI: —

**#9675** [feat(mcp): add document-annotation tools and includeAnnotationComments](https://github.com/paperclipai/paperclip/pull/9675)
`фича` · Коннекторы и MCP · автор @greegorij · балл **75.2** · 153+4 строк · None дн. · CI: —

**#6273** [heartbeat: kill detached child after 5-min grace (RED-1279)](https://github.com/paperclipai/paperclip/pull/6273)
`фикс` · Запуски и heartbeat · автор @redmutex · балл **75.2** · 89+2 строк · None дн. · CI: —

**#14027** [fix(agents): let bound agents be edited and unbound from AI connections](https://github.com/paperclipai/paperclip/pull/14027)
`фикс` · AI-подключения и доступ · автор @VishvakR · балл **75.1** · 34+4 строк · None дн. · CI: —
