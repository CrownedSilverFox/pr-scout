# PR Scout: siteboon/claudecodeui

Прогон: 77 PR с баллами, финалистов 47, Jev потратил $0.0822 (1644326 входных токенов).

- `describe`: 0 шт · 0 с · $0 · ошибок 0
- `stage1`: 77 шт · 18 с · $0.01 · ошибок 0
- `stage2`: 47 шт · 292 с · $0.022 · ошибок 0
- `issues-list`: 135 шт · 11 с · $0 · ошибок 0
- `issues`: 135 шт · 31 с · $0.0125 · ошибок 0
- `rivals`: 0 шт · 0 с · $0.0 · ошибок 0
- `forks-list`: 1983 шт · 34 с · $0 · ошибок 0
- `forks`: 323 шт · 62 с · $0.0321 · ошибок 0
- `stack`: 27 шт · 127 с · $0 · ошибок 7
- `map`: 47 шт · 314 с · $0.0056 · ошибок 0

Последний цикл: 1644326 входных токенов, $0.0822. Все прогоны в истории: 639469 токенов, $0.0822.

| вариант | цена |
|---|---:|
| Jev (факт, последний цикл) | $0.0822 |
| Claude Opus 5.5 (оценка на тех же токенах) | $22.82 |
| Claude Sonnet 5 (оценка на тех же токенах) | $11.41 |
| Claude Haiku 4.5 (оценка на тех же токенах) | $5.71 |

## Берём (8)

**#1426** [fix(opencode): read live run events nested under part](https://github.com/siteboon/claudecodeui/pull/1426)
`фикс` · Провайдеры и CLI · автор @jjscarafia · балл **83.8** · 183+7 строк · — дн. · CI: no_ci
  - + серьёзный баг в обычной работе (вред 0.8, частота 0.83)
  - + прямо про ваше использование (2.83/3)

**#1247** [fix(auth): ignore refreshed tokens that are not newer than the stored one](https://github.com/siteboon/claudecodeui/pull/1247)
`фикс` · Доступ и права · автор @mattsm · балл **74.7** · 142+2 строк · — дн. · CI: no_ci
  - + серьёзный баг в обычной работе (вред 0.91, частота 0.74)

**#1446** [fix(claude): keep history after background task notifications](https://github.com/siteboon/claudecodeui/pull/1446)
`фикс` · Провайдеры и CLI · автор @marin-o · балл **73.2** · 87+2 строк · — дн. · CI: no_ci
  - + серьёзный баг в обычной работе (вред 0.44, частота 0.75)
  - + прямо про ваше использование (2.62/3)

**#1444** [fix(claude): wait for a superseded run to exit before resuming its session](https://github.com/siteboon/claudecodeui/pull/1444)
`фикс` · Провайдеры и CLI · автор @marin-o · балл **70.9** · 225+3 строк · — дн. · CI: no_ci
  - + серьёзный баг в обычной работе (вред 0.32, частота 0.77)
  - + прямо про ваше использование (2.66/3)

**#1439** [feat(providers): add selectable runtime profiles](https://github.com/siteboon/claudecodeui/pull/1439)
`фича` · Провайдеры и CLI · автор @dongwook-chan · балл **70.6** · 674+20 строк · — дн. · CI: no_ci
  - + сильная фича (ценность 3.25/4, новизна 0.8)

**#1007** [fix(shell): paste through terminal.paste() and stop swallowing native paste](https://github.com/siteboon/claudecodeui/pull/1007)
`фикс` · Интерфейс · автор @mayankdebnath · балл **69.4** · 26+13 строк · — дн. · CI: no_ci
  - + серьёзный баг в обычной работе (вред 0.58, частота 0.83)
  - + прямо про ваше использование (2.76/3)

**#1000** [fix(browser): install Playwright runtime in package dir, not cwd](https://github.com/siteboon/claudecodeui/pull/1000)
`фикс` · Прочее · автор @LonestoneBot · балл **60.4** · 33+2 строк · — дн. · CI: no_ci
  - + серьёзный баг в обычной работе (вред 0.83, частота 0.79)

**#1213** [fix(claude): normalize queue-operation remove records as user-role text](https://github.com/siteboon/claudecodeui/pull/1213)
`фикс` · Провайдеры и CLI · автор @fedecia · балл **59.8** · 116+0 строк · — дн. · CI: no_ci
  - + серьёзный баг в обычной работе (вред 0.26, частота 0.62)


## Рассмотреть (19)

**#1390** [fix(sessions): keep transcript rows that contain U+2028 or U+2029](https://github.com/siteboon/claudecodeui/pull/1390)
`фикс` · Сессии и стрим · автор @SulimanAbdulrazzaq · балл **72.2** · 475+58 строк · — дн. · CI: no_ci
  - ! баг не критичный или редкий
  - + прямо про ваше использование (2.57/3)

**#1431** [fix(claude): preserve background work across user turns](https://github.com/siteboon/claudecodeui/pull/1431)
`фича` · Провайдеры и CLI · автор @Dredok · балл **71.5** · 756+267 строк · — дн. · CI: no_ci
  - ! фича меняет поведение по умолчанию
  - + сильная фича (ценность 3.35/4, новизна 0.76)
  - + прямо про ваше использование (2.57/3)

**#1440** [fix(chat): drop repeat send presses while a submit is in flight](https://github.com/siteboon/claudecodeui/pull/1440)
`фикс` · Интерфейс · автор @coocon · балл **69.6** · 149+2 строк · — дн. · CI: no_ci
  - ! баг не критичный или редкий
  - + прямо про ваше использование (2.78/3)

**#1453** [🚨 fix(chat): require server receipt before clearing the first prompt](https://github.com/siteboon/claudecodeui/pull/1453)
`фикс` · Сессии и стрим · автор @dongwook-chan · балл **67.6** · 619+183 строк · — дн. · CI: no_ci
  - ! баг не критичный или редкий
  - ! рискованная область (0.57)
  - + прямо про ваше использование (2.84/3)

**#1202** [feat: add CLOUDCLI_DISABLE_UPDATE_CHECK to disable update checks](https://github.com/siteboon/claudecodeui/pull/1202)
`фича` · Деплой и десктоп · автор @coder8080 · балл **64.2** · 367+7 строк · — дн. · CI: no_ci
  - ! фича полезная, но не ключевая

**#1356** [fix(server): drain active chats on shutdown](https://github.com/siteboon/claudecodeui/pull/1356)
`фикс` · Сессии и стрим · автор @dongwook-chan · балл **62.2** · 222+24 строк · — дн. · CI: no_ci
  - ! баг не критичный или редкий

**#1365** [fix(chat): discard stale selection responses after session navigation](https://github.com/siteboon/claudecodeui/pull/1365)
`фикс` · Сессии и стрим · автор @materemias · балл **61.7** · 156+2 строк · — дн. · CI: no_ci
  - ! баг не критичный или редкий

**#1449** [feat(chat): three send modes while a turn is running — after turn, after next tool call, now](https://github.com/siteboon/claudecodeui/pull/1449)
`фича` · Провайдеры и CLI · автор @marin-o · балл **61.3** · 2991+93 строк · — дн. · CI: no_ci
  - ! большой PR (3084 строк)
  - + сильная фича (ценность 3.57/4, новизна 0.86)

**#1364** [fix(chat): guard tool lookups against inherited properties](https://github.com/siteboon/claudecodeui/pull/1364)
`фикс` · Интерфейс · автор @materemias · балл **61.3** · 59+5 строк · — дн. · CI: no_ci
  - ! баг не критичный или редкий

**#995** [fix: install browser runtime outside process cwd](https://github.com/siteboon/claudecodeui/pull/995)
`фикс` · Провайдеры и CLI · автор @CoderLuii · балл **60.6** · 365+11 строк · — дн. · CI: no_ci
  - ! баг не критичный или редкий

**#1436** [fix(windows): resolve the claude CLI by walking PATH instead of where.exe](https://github.com/siteboon/claudecodeui/pull/1436)
`фикс` · Провайдеры и CLI · автор @xingcheng1061 · балл **58.9** · 236+57 строк · — дн. · CI: no_ci
  - ! баг не критичный или редкий

**#1457** [fix(workspace): don't strand the composer mid-screen after the keyboard hides](https://github.com/siteboon/claudecodeui/pull/1457)
`фикс` · Интерфейс · автор @davidboulay · балл **58.0** · 47+4 строк · — дн. · CI: no_ci
  - ! баг не критичный или редкий
  - + прямо про ваше использование (2.55/3)

**#1445** [fix(plugins): include devDependencies when installing plugins](https://github.com/siteboon/claudecodeui/pull/1445)
`фикс` · MCP и плагины · автор @wjc2821296948 · балл **57.1** · 129+6 строк · — дн. · CI: no_ci
  - ! баг не критичный или редкий

**#959** [fix: add Codex provider complete fields](https://github.com/siteboon/claudecodeui/pull/959)
`фикс` · Провайдеры и CLI · автор @CoderLuii · балл **55.7** · 21+0 строк · — дн. · CI: no_ci
  - ! баг не критичный или редкий

**#1061** [fix(codex): show provider thread titles in the sidebar](https://github.com/siteboon/claudecodeui/pull/1061)
`фикс` · Провайдеры и CLI · автор @apple-ouyang · балл **55.6** · 799+33 строк · — дн. · CI: no_ci
  - ! баг не критичный или редкий
  - ! рискованная область (0.61)

**#1310** [fix(auth): verify the session once per mount, not once per token refresh](https://github.com/siteboon/claudecodeui/pull/1310)
`фикс` · Доступ и права · автор @TadMSTR · балл **52.6** · 171+3 строк · — дн. · CI: no_ci
  - ! баг не критичный или редкий

**#1111** [fix: correct workspace root containment check for root paths](https://github.com/siteboon/claudecodeui/pull/1111)
`фикс` · MCP и плагины · автор @MacLeod92 · балл **52.3** · 59+8 строк · — дн. · CI: no_ci
  - ! баг не критичный или редкий

**#1178** [perf(sessions): resolve the session title without holding the transcript](https://github.com/siteboon/claudecodeui/pull/1178)
`перф` · Провайдеры и CLI · автор @TadMSTR · балл **43.0** · 412+15 строк · — дн. · CI: no_ci
  - ! баг не критичный или редкий

**#1278** [Log Claude run lifecycle transitions](https://github.com/siteboon/claudecodeui/pull/1278)
`фича` · Провайдеры и CLI · автор @Wasabi81-code · балл **40.6** · 263+3 строк · — дн. · CI: no_ci
  - ! фича полезная, но не ключевая


## Пропускаем (20)

**#1245** [fix(claude): background agents were reported completed at launch](https://github.com/siteboon/claudecodeui/pull/1245)
`фикс` · Провайдеры и CLI · автор @maslyankov · балл **76.3** · 31+10 строк · — дн. · CI: no_ci
  - ✗ конфликт с основной веткой и взятыми PR: claude-sessions.provider.ts, claude-sessions.test.ts
  - + серьёзный баг в обычной работе (вред 0.63, частота 0.7)
  - + прямо про ваше использование (2.73/3)

**#1443** [feat(opencode): show task calls as subagents](https://github.com/siteboon/claudecodeui/pull/1443)
`фича` · Провайдеры и CLI · автор @jjscarafia · балл **72.4** · 577+10 строк · — дн. · CI: no_ci
  - ✗ код не совпадает с описанием (0.42)
  - ! фича полезная, но не ключевая
  - ! фича меняет поведение по умолчанию
  - + прямо про ваше использование (2.65/3)

**#1233** [Optionally keep one Claude process for a whole conversation](https://github.com/siteboon/claudecodeui/pull/1233)
`фича` · Провайдеры и CLI · автор @edgar965 · балл **69.1** · 819+23 строк · — дн. · CI: no_ci
  - ✗ конфликт с основной веткой и взятыми PR: claude-runtime.provider.js
  - ! фича полезная, но не ключевая

**#1441** [feat(commands): list each CLI's native slash commands, scoped per provider](https://github.com/siteboon/claudecodeui/pull/1441)
`фича` · Провайдеры и CLI · автор @xingcheng1061 · балл **67.3** · 1028+35 строк · — дн. · CI: no_ci
  - ✗ код не совпадает с описанием (0.35)
  - ! фича полезная, но не ключевая
  - ! фича меняет поведение по умолчанию

**#984** [Support Codex custom provider authentication](https://github.com/siteboon/claudecodeui/pull/984)
`фича` · Провайдеры и CLI · автор @Rio-Allen · балл **62.6** · 354+66 строк · — дн. · CI: green
  - ✗ конфликт с основной веткой и взятыми PR: codex-runtime.provider.ts
  - ! фича полезная, но не ключевая

**#1129** [feat(mobile): open the session list when back is pressed](https://github.com/siteboon/claudecodeui/pull/1129)
`фича` · Интерфейс · автор @materemias · балл **61.3** · 459+0 строк · — дн. · CI: no_ci
  - ✗ конфликт с основной веткой и взятыми PR: ProjectWorkspaceShell.tsx
  - ! фича полезная, но не ключевая

**#1324** [feat: add pi as fifth agent provider](https://github.com/siteboon/claudecodeui/pull/1324)
`фича` · Провайдеры и CLI · автор @realjustinwu · балл **60.5** · 5155+100 строк · — дн. · CI: no_ci
  - ✗ конфликт с основной веткой и взятыми PR: .gitignore, agent.routes.ts
  - ✗ код не совпадает с описанием (0.49)
  - ! рискованная область (0.77)
  - ! большой PR (5255 строк)
  - + сильная фича (ценность 3.58/4, новизна 0.86)
  - + прямо про ваше использование (2.55/3)

**#1451** [fix(chat): remove an unsent new session after socket refusal](https://github.com/siteboon/claudecodeui/pull/1451)
`фикс` · Сессии и стрим · автор @dongwook-chan · балл **58.3** · 80+24 строк · — дн. · CI: no_ci
  - ✗ код не совпадает с описанием (0.38)
  - ! баг не критичный или редкий

**#1252** [feat(providers): add Command Code as a coding-agent provider](https://github.com/siteboon/claudecodeui/pull/1252)
`фича` · Провайдеры и CLI · автор @asiqur-rahman · балл **57.1** · 2051+19 строк · — дн. · CI: no_ci
  - ✗ конфликт с основной веткой и взятыми PR: agent.routes.ts, SidebarSessionItem.tsx
  - ✗ продвигает сторонний сервис (0.66)
  - ! фича полезная, но не ключевая
  - ! рискованная область (0.74)
  - ! большой PR (2070 строк)

**#1149** [Add searchable GitHub repo picker and fix mobile Enter-to-send](https://github.com/siteboon/claudecodeui/pull/1149)
`фича` · Интерфейс · автор @Tourniercy · балл **55.9** · 1485+23 строк · — дн. · CI: no_ci
  - ✗ конфликт с основной веткой и взятыми PR: types.ts, types.ts, apiError.ts
  - ! фича полезная, но не ключевая
  - ! фича меняет поведение по умолчанию
  - ! большой PR (1508 строк)

**#1035** [fix: resolve Claude auth status via `claude auth status` instead of a credentials file](https://github.com/siteboon/claudecodeui/pull/1035)
`фикс` · Провайдеры и CLI · автор @zscgeek · балл **54.5** · 92+24 строк · — дн. · CI: no_ci
  - ✗ конфликт с основной веткой и взятыми PR: claude-auth.provider.ts
  - ! баг не критичный или редкий
  - + прямо про ваше использование (2.5/3)

**#1352** [Add Antigravity provider support](https://github.com/siteboon/claudecodeui/pull/1352)
`фича` · Провайдеры и CLI · автор @dongwook-chan · балл **54.1** · 2623+122 строк · — дн. · CI: no_ci
  - ✗ конфликт с основной веткой и взятыми PR: agent.routes.ts, useChatRealtimeHandlers.ts
  - ! фича полезная, но не ключевая
  - ! рискованная область (0.84)
  - ! большой PR (2745 строк)
  - + прямо про ваше использование (2.82/3)

**#1279** [Forward the Claude CLI's stderr to the service log](https://github.com/siteboon/claudecodeui/pull/1279)
`фича` · Провайдеры и CLI · автор @Wasabi81-code · балл **53.9** · 998+3 строк · — дн. · CI: no_ci
  - ✗ код не совпадает с описанием (0.27)
  - ! фича полезная, но не ключевая
  - ! фича меняет поведение по умолчанию

**#917** [Fix Windows browser-runtime install and Claude Code SDK spawn failures](https://github.com/siteboon/claudecodeui/pull/917)
`фикс` · Провайдеры и CLI · автор @benjaminberes-bp · балл **52.3** · 78+9 строк · — дн. · CI: no_ci
  - ✗ конфликт с основной веткой и взятыми PR: claude-sdk.js
  - ! баг не критичный или редкий

**#1034** [fix: honor CLAUDE_CONFIG_DIR for all Claude Code data (projects, sessions, settings, MCP config)](https://github.com/siteboon/claudecodeui/pull/1034)
`фикс` · Провайдеры и CLI · автор @zscgeek · балл **52.3** · 54+28 строк · — дн. · CI: no_ci
  - ✗ конфликт с основной веткой и взятыми PR: eslint.config.js, claude-sdk.js, cli.js
  - ! баг не критичный или редкий

**#1160** [fix(claude): stop dropping an explicitly requested permission mode](https://github.com/siteboon/claudecodeui/pull/1160)
`фикс` · Провайдеры и CLI · автор @fedecia · балл **51.2** · 63+6 строк · — дн. · CI: no_ci
  - ✗ конфликт с основной веткой и взятыми PR: claude-runtime.provider.js
  - ! баг не критичный или редкий

**#1033** [fix(claude): detect macOS Keychain authentication](https://github.com/siteboon/claudecodeui/pull/1033)
`фикс` · Провайдеры и CLI · автор @sudo-eugene · балл **50.7** · 148+2 строк · — дн. · CI: no_ci
  - ✗ конфликт с основной веткой и взятыми PR: claude-auth.provider.ts, claude-auth.test.ts
  - ! баг не критичный или редкий

**#760** [feat: add Kiro CLI provider via ACP](https://github.com/siteboon/claudecodeui/pull/760)
`фича` · Провайдеры и CLI · автор @dgallitelli · балл **46.2** · 3428+62 строк · — дн. · CI: no_ci
  - ✗ продвигает сторонний сервис (0.87)
  - ✗ код не совпадает с описанием (0.33)
  - ! фича полезная, но не ключевая
  - ! рискованная область (0.76)
  - ! большой PR (3490 строк)

**#975** [feat(claude): source model list from cc-switch, gated by env](https://github.com/siteboon/claudecodeui/pull/975)
`фича` · Провайдеры и CLI · автор @8liang · балл **40.8** · 286+1 строк · — дн. · CI: no_ci
  - ✗ конфликт с основной веткой и взятыми PR: claude-models.provider.ts, claude-models.test.ts
  - ! фича полезная, но не ключевая

**#1042** [feat(auth): add opt-in local login bypass](https://github.com/siteboon/claudecodeui/pull/1042)
`фича` · Доступ и права · автор @dongwook-chan · балл **37.1** · 180+33 строк · — дн. · CI: no_ci
  - ✗ конфликт с основной веткой и взятыми PR: cli.js, config.js, index.js
  - ! фича полезная, но не ключевая
  - ! рискованная область (0.77)


## Не дошли до этапа 2 — только балл этапа 1, вердикта нет (30)

**#1447** [feat(file-tree): add a folder search to the directory picker](https://github.com/siteboon/claudecodeui/pull/1447)
`фича` · Файлы и git · автор @xingcheng1061 · балл **59.3** · 783+32 строк · — дн. · CI: —

**#1241** [Tell the desktop app the address the server is actually on](https://github.com/siteboon/claudecodeui/pull/1241)
`фикс` · Деплой и десктоп · автор @edgar965 · балл **57.8** · 94+4 строк · — дн. · CI: —

**#1174** [fix(auth): stop a cached API response from restoring an expired token](https://github.com/siteboon/claudecodeui/pull/1174)
`фикс` · Доступ и права · автор @materemias · балл **57.1** · 116+2 строк · — дн. · CI: —

**#1260** [fix(plugins): install dev dependencies so plugin builds succeed](https://github.com/siteboon/claudecodeui/pull/1260)
`фикс` · MCP и плагины · автор @asiqur-rahman · балл **55.5** · 8+3 строк · — дн. · CI: —

**#978** [Add local account management controls](https://github.com/siteboon/claudecodeui/pull/978)
`фича` · Доступ и права · автор @CoderLuii · балл **55.1** · 584+25 строк · — дн. · CI: —

**#1309** [fix(auth): stop browser HTTP cache from replaying a stale X-Refreshed-Token](https://github.com/siteboon/claudecodeui/pull/1309)
`фикс` · Доступ и права · автор @Sergio-LPA · балл **53.2** · 124+4 строк · — дн. · CI: —

**#1118** [fix(projects): redact GitHub tokens from clone progress stream (P1)](https://github.com/siteboon/claudecodeui/pull/1118)
`безопасность` · MCP и плагины · автор @wjc2821296948 · балл **51.0** · 329+9 строк · — дн. · CI: —

**#1191** [feat: give plugins an authenticated way to reach the host API](https://github.com/siteboon/claudecodeui/pull/1191)
`фича` · MCP и плагины · автор @bvn13 · балл **50.0** · 386+12 строк · — дн. · CI: —

**#1154** [feat(chat): show README summary on the new-conversation empty state](https://github.com/siteboon/claudecodeui/pull/1154)
`фича` · Интерфейс · автор @JerryWestrick · балл **50.0** · 221+2 строк · — дн. · CI: —

**#1215** [fix: install dev deps and rebuild during git-mode self-update](https://github.com/siteboon/claudecodeui/pull/1215)
`фикс` · Деплой и десктоп · автор @StyrIlya · балл **49.0** · 10+2 строк · — дн. · CI: —

**#1240** [Only sign out over a token the request actually sent](https://github.com/siteboon/claudecodeui/pull/1240)
`фикс` · Доступ и права · автор @edgar965 · балл **46.4** · 76+5 строк · — дн. · CI: —

**#928** [feat: add password reset settings tab / 新增密码修改设置页](https://github.com/siteboon/claudecodeui/pull/928)
`фича` · Интерфейс · автор @WenhuaXia · балл **46.4** · 233+5 строк · — дн. · CI: —

**#1038** [feat(appearance): add system font preference](https://github.com/siteboon/claudecodeui/pull/1038)
`фича` · Интерфейс · автор @sudo-eugene · балл **46.3** · 102+15 строк · — дн. · CI: —

**#1257** [fix(cursor): resolve the cursor agent binary as \`agent\` or \`cursor-agent\`](https://github.com/siteboon/claudecodeui/pull/1257)
`фикс` · Провайдеры и CLI · автор @asiqur-rahman · балл **46.0** · 68+6 строк · — дн. · CI: —

**#1070** [fix: update upload and websocket dependencies](https://github.com/siteboon/claudecodeui/pull/1070)
`фикс` · Артефакты · автор @CoderLuii · балл **45.5** · 296+443 строк · — дн. · CI: —

**#1299** [feat(chat): read assistant replies aloud per session](https://github.com/siteboon/claudecodeui/pull/1299)
`фича` · Сессии и стрим · автор @andriilh-amzn · балл **44.9** · 1382+22 строк · — дн. · CI: —

**#1072** [feat(sidebar): optional grouping of project cards by folder name](https://github.com/siteboon/claudecodeui/pull/1072)
`фича` · Интерфейс · автор @Sergio-LPA · балл **44.5** · 356+66 строк · — дн. · CI: —

**#1176** [fix(database): never rotate persisted secrets on a failed read](https://github.com/siteboon/claudecodeui/pull/1176)
`фикс` · Доступ и права · автор @materemias · балл **43.9** · 378+35 строк · — дн. · CI: —

**#1135** [feat(sidebar): add logout action](https://github.com/siteboon/claudecodeui/pull/1135)
`фича` · Интерфейс · автор @mxx1111 · балл **41.6** · 53+4 строк · — дн. · CI: —

**#1221** [fix: pass USER/LOGNAME to plugin subprocess env for macOS Keychain access](https://github.com/siteboon/claudecodeui/pull/1221)
`фикс` · MCP и плагины · автор @nateQQ · балл **41.0** · 6+0 строк · — дн. · CI: —

**#1227** [Let a launcher name a desktop window and open Local CloudCLI at startup](https://github.com/siteboon/claudecodeui/pull/1227)
`фича` · Деплой и десктоп · автор @edgar965 · балл **40.7** · 111+3 строк · — дн. · CI: —

**#1119** [fix(server): restrict CORS to same host:port as the server (P1)](https://github.com/siteboon/claudecodeui/pull/1119)
`безопасность` · Деплой и десктоп · автор @wjc2821296948 · балл **40.6** · 58+6 строк · — дн. · CI: —

**#1226** [Fix two Windows path bugs: drive letter case, and a drive as the workspace root](https://github.com/siteboon/claudecodeui/pull/1226)
`фикс` · MCP и плагины · автор @edgar965 · балл **38.8** · 464+3 строк · — дн. · CI: —

**#1248** [feat(themes): user-selectable colour themes, imported from VS Code](https://github.com/siteboon/claudecodeui/pull/1248)
`фича` · Интерфейс · автор @carsso · балл **35.8** · 2758+131 строк · — дн. · CI: —

**#1175** [fix(auth): keep the session when auth cannot be verified](https://github.com/siteboon/claudecodeui/pull/1175)
`фикс` · Доступ и права · автор @materemias · балл **35.5** · 574+44 строк · — дн. · CI: —

**#1094** [feat: add opt-in bandwidth monitoring behind BANDWIDTH_MONITOR_ENABLED](https://github.com/siteboon/claudecodeui/pull/1094)
`фича` · Сессии и стрим · автор @centerionware · балл **29.4** · 255+13 строк · — дн. · CI: —

**#871** [fix: detect TaskMaster CLI installation on Windows](https://github.com/siteboon/claudecodeui/pull/871)
`фикс` · Задачи и доска · автор @pipipigu · балл **21.7** · 8+5 строк · — дн. · CI: —

**#1360** [refactor(sidebar): collapse footer links into an icon row](https://github.com/siteboon/claudecodeui/pull/1360)
`рефакторинг` · Интерфейс · автор @vruzin · балл **2.3** · 28+70 строк · — дн. · CI: —

**#1372** [docs(types): put the subagent comment back on the type it describes](https://github.com/siteboon/claudecodeui/pull/1372)
`доки` · Документация · автор @liran-funaro · балл **0.2** · 1+1 строк · — дн. · CI: —

**#1361** [test: make backend fixtures portable on Windows](https://github.com/siteboon/claudecodeui/pull/1361)
`тесты/CI` · Прочее · автор @materemias · балл **-0.1** · 8+4 строк · — дн. · CI: —


# Issues: 135 открытых, 116 без единого PR

## Важное, на что PR нет

**#1270** [[BUG] Outgoing chat messages are silently discarded when the WebSocket is closed (no error, no queue)](https://github.com/siteboon/claudecodeui/issues/1270) — балл **92.2**, `Баг`, серьёзность 3.95/4, частота 0.93, релевантность 2.91/3, 0 комм. · @trped · обновлено 2026-09-07

**#1022** [Resumed Claude Code sessions: message history silently truncated at resume boundaries — getSessionMessages filters JSONL by a single sessionId](https://github.com/siteboon/claudecodeui/issues/1022) — балл **86.6**, `Баг`, серьёзность 3.77/4, частота 0.72, релевантность 2.83/3, 1 комм. · @m11a-dev · обновлено 2026-07-14

**#1350** [Permission denials neither carry a reason nor stop the agent — `message` is always the generic fallback, and `interrupt` is never set](https://github.com/siteboon/claudecodeui/issues/1350) — балл **84.1**, `Баг`, серьёзность 3.85/4, частота 0.85, релевантность 2.39/3, 0 комм. · @lyq326 · обновлено 2026-09-18

**#1004** [Shell: PTY keying collapses all new-session shells to one key — cross-tab hijack, duplicate resumed processes, and orphaned Claude sessions burning tokens](https://github.com/siteboon/claudecodeui/issues/1004) — балл **84.1**, `Баг`, серьёзность 3.88/4, частота 0.85, релевантность 2.41/3, 1 комм. · @mayankdebnath · обновлено 2026-07-12

**#1128** [# Title Black blank screen after successful login, occurs in both Electron desktop and local browser version](https://github.com/siteboon/claudecodeui/issues/1128) — балл **84.0**, `Баг`, серьёзность 3.94/4, частота 0.73, релевантность 2.89/3, 1 комм. · @Sulflower314 · обновлено 2026-08-11

**#1297** [Claude history: dropSupersededPromptBranches deletes the live branch when injected user rows share a parentUuid (495 of 890 rows dropped, hasMore: false)](https://github.com/siteboon/claudecodeui/issues/1297) — балл **83.0**, `Баг`, серьёзность 3.92/4, частота 0.62, релевантность 2.72/3, 0 комм. · @andriilh-amzn · обновлено 2026-09-08

**#953** [Shell terminal silently freezes on mobile while Chat keeps updating — stale WebSocket close detaches the live PTY socket; half-open sockets never reaped](https://github.com/siteboon/claudecodeui/issues/953) — балл **81.9**, `Баг`, серьёзность 3.74/4, частота 0.53, релевантность 2.82/3, 1 комм. · @wideplain · обновлено 2026-07-02

**#1136** [Streaming buffer has no message boundary: assistant messages in one turn are merged into a single row](https://github.com/siteboon/claudecodeui/issues/1136) — балл **81.0**, `Баг`, серьёзность 2.98/4, частота 0.76, релевантность 2.94/3, 3 комм. · @materemias · обновлено 2026-08-11

**#1050** [Chat message-pane scrolling is choppy during streaming and while idle](https://github.com/siteboon/claudecodeui/issues/1050) — балл **80.4**, `Производительность`, серьёзность 2.78/4, частота 0.89, релевантность 2.74/3, 1 комм. · @danish-circuit · обновлено 2026-07-21

**#1137** [Older history is unreachable when the first page does not fill the pane](https://github.com/siteboon/claudecodeui/issues/1137) — балл **79.1**, `Баг`, серьёзность 3.26/4, частота 0.64, релевантность 2.72/3, 1 комм. · @materemias · обновлено 2026-08-11

**#1455** [Chat doesn't show what a Bash command changed: the CLI's bashEditDiff is never rendered](https://github.com/siteboon/claudecodeui/issues/1455) — балл **78.7**, `Баг`, серьёзность 2.99/4, частота 0.88, релевантность 2.56/3, 0 комм. · @liran-funaro · обновлено 2026-09-27

**#1368** [Session appears permanently "stuck" past the point where an interrupted background Agent task was resumed (mismatched tool_use_id breaks async-agent completion detection)](https://github.com/siteboon/claudecodeui/issues/1368) — балл **78.7**, `Баг`, серьёзность 3.94/4, частота 0.4, релевантность 2.82/3, 0 комм. · @wolfiko88 · обновлено 2026-09-22

**#1377** [Settings CLI Login dialogs send a hardcoded /workspace path and fail with "Invalid project path"](https://github.com/siteboon/claudecodeui/issues/1377) — балл **78.1**, `Баг`, серьёзность 3.7/4, частота 0.45, релевантность 2.77/3, 0 комм. · @tobolik · обновлено 2026-09-22

**#1402** [Session renamed with `/rename` in terminal TUI is not reflected in the sidebar (follow-up to #747: the custom-title fix is shadowed by two higher-priority name sources)](https://github.com/siteboon/claudecodeui/issues/1402) — балл **77.2**, `Баг`, серьёзность 2.53/4, частота 0.9, релевантность 2.69/3, 0 комм. · @index7559 · обновлено 2026-09-23

**#1366** [Codex history drops user prompts stored as `response_item/user` messages](https://github.com/siteboon/claudecodeui/issues/1366) — балл **76.5**, `Баг`, серьёзность 3.38/4, частота 0.66, релевантность 2.82/3, 0 комм. · @caiwd · обновлено 2026-09-22

**#1148** [Claude Chat and native CLI can silently fork one session: UI shows history that the model did not resume](https://github.com/siteboon/claudecodeui/issues/1148) — балл **76.2**, `Баг`, серьёзность 3.48/4, частота 0.51, релевантность 2.8/3, 1 комм. · @paceaitian · обновлено 2026-08-14

**#1073** [UI stuck on "Setting up your workspace" after update — cannot use sessions](https://github.com/siteboon/claudecodeui/issues/1073) — балл **76.2**, `Баг`, серьёзность 3.97/4, частота 0.46, релевантность 2.94/3, 4 комм. · @caiwd · обновлено 2026-08-14

**#1170** [One session, two transcripts: jsonl_path is decided by scan order, so Chat can render a stale copy indefinitely (looks like a hang)](https://github.com/siteboon/claudecodeui/issues/1170) — балл **75.7**, `Баг`, серьёзность 3.91/4, частота 0.38, релевантность 2.6/3, 1 комм. · @gcdevuk · обновлено 2026-08-18

**#1103** [CloudCLI 1.37.0 enters an infinite loading/reconnect loop in Microsoft Edge, while Chrome works](https://github.com/siteboon/claudecodeui/issues/1103) — балл **75.6**, `Баг`, серьёзность 3.78/4, частота 0.4, релевантность 2.84/3, 3 комм. · @caiwd · обновлено 2026-08-22

**#1099** [Codex session becomes unresponsive when view_image results contain large base64 image data](https://github.com/siteboon/claudecodeui/issues/1099) — балл **75.0**, `Баг`, серьёзность 3.97/4, частота 0.39, релевантность 2.58/3, 1 комм. · @caiwd · обновлено 2026-08-04

**#884** [Interrupt+Continue may spawn parallel `claude --resume` of own sid](https://github.com/siteboon/claudecodeui/issues/884) — балл **75.0**, `Баг`, серьёзность 3.24/4, частота 0.55, релевантность 2.74/3, 1 комм. · @dennisgregory-lab · обновлено 2026-06-15

**#1335** [Shell terminal ignores the light/dark theme setting](https://github.com/siteboon/claudecodeui/issues/1335) — балл **74.7**, `Баг`, серьёзность 2.94/4, частота 0.89, релевантность 2.23/3, 0 комм. · @corva32 · обновлено 2026-09-16

**#1325** [Background shells are killed on the next user message, and PowerShell background commands at end of turn (startsBackgroundWork / superseded run)](https://github.com/siteboon/claudecodeui/issues/1325) — балл **74.7**, `Баг`, серьёзность 3.43/4, частота 0.72, релевантность 2.24/3, 0 комм. · @unisyntax-dev · обновлено 2026-09-14

**#1156** [Session watcher: `ignored` globs are inert under chokidar v4, so all five provider roots are fully walked and polled](https://github.com/siteboon/claudecodeui/issues/1156) — балл **74.7**, `Баг`, серьёзность 3.05/4, частота 0.86, релевантность 2.18/3, 1 комм. · @beemusicco · обновлено 2026-08-16

**#1109** [[Bug] UI crashes to a black screen when plugin install fails; server error detail is not surfaced](https://github.com/siteboon/claudecodeui/issues/1109) — балл **73.6**, `Баг`, серьёзность 3.99/4, частота 0.39, релевантность 2.34/3, 3 комм. · @e-yavuz-1 · обновлено 2026-08-10

**#1069** [Sessions running under the Claude CLI show no running/processing state in the UI](https://github.com/siteboon/claudecodeui/issues/1069) — балл **73.1**, `Запрос фичи`, серьёзность 2.53/4, частота 0.84, релевантность 2.77/3, 1 комм. · @thevinchi · обновлено 2026-07-30

**#1021** [Sessions in project dirs created after server startup are never indexed: watcher emits no events for new dirs, then scan_state checkpoint permanently excludes their files](https://github.com/siteboon/claudecodeui/issues/1021) — балл **72.3**, `Баг`, серьёзность 3.4/4, частота 0.44, релевантность 2.48/3, 2 комм. · @m11a-dev · обновлено 2026-08-17

**#1263** [Codex permission default from Settings is ignored by chat composer](https://github.com/siteboon/claudecodeui/issues/1263) — балл **72.2**, `Баг`, серьёзность 3.08/4, частота 0.83, релевантность 2.03/3, 0 комм. · @ByteEnchanter · обновлено 2026-09-05

**#1306** [New Chat creates two backend sessions and delivers the first message to both (v1.37.3, macOS, npm)](https://github.com/siteboon/claudecodeui/issues/1306) — балл **72.0**, `Баг`, серьёзность 3.07/4, частота 0.37, релевантность 2.78/3, 0 комм. · @margotlym-hash · обновлено 2026-09-10

**#1197** [File tree downloads fail intermittently: blob URL revoked in the same tick and click issued after await](https://github.com/siteboon/claudecodeui/issues/1197) — балл **71.9**, `Баг`, серьёзность 3.37/4, частота 0.84, релевантность 1.82/3, 0 комм. · @coder8080 · обновлено 2026-08-22

**#1181** [create-project unusable on root-user deployments: default WORKSPACES_ROOT (= /root) is entirely inside FORBIDDEN_WORKSPACE_PATHS](https://github.com/siteboon/claudecodeui/issues/1181) — балл **71.7**, `Баг`, серьёзность 3.91/4, частота 0.55, релевантность 2.05/3, 2 комм. · @vachowsky · обновлено 2026-09-02

**#1011** [Codex chats silently produce empty turns when the configured model needs a newer CLI — vendored @openai/codex-sdk 0.141 gets HTTP 400 (e.g. `gpt-5.6-sol`)](https://github.com/siteboon/claudecodeui/issues/1011) — балл **71.7**, `Баг`, серьёзность 3.75/4, частота 0.32, релевантность 2.5/3, 1 комм. · @pfedotovsky · обновлено 2026-08-09

**#641** [**Bug: Web UI permission settings ineffective + workspace path conflict (/root vs ~)**](https://github.com/siteboon/claudecodeui/issues/641) — балл **71.7**, `Баг`, серьёзность 3.94/4, частота 0.41, релевантность 2.59/3, 1 комм. · @w1739902251 · обновлено 2026-08-09

**#1330** [Agent API with `stream: false` always returns `messages: []` and zero tokens — ResponseCollector only matches the legacy string `claude-response` shape](https://github.com/siteboon/claudecodeui/issues/1330) — балл **71.6**, `Баг`, серьёзность 3.61/4, частота 0.79, релевантность 1.73/3, 0 комм. · @sebzz07 · обновлено 2026-09-15

**#1018** [bin.js entrypoint imports uncompiled source (`server/cli.js`) instead of built output (`dist-server/server/cli.js`) — crashes with "Cannot find package '@/shared'"](https://github.com/siteboon/claudecodeui/issues/1018) — балл **71.4**, `Баг`, серьёзность 3.9/4, частота 0.79, релевантность 1.45/3, 1 комм. · @vntai · обновлено 2026-08-09

**#1165** [Bug: Chats break after renaming a project folder](https://github.com/siteboon/claudecodeui/issues/1165) — балл **70.7**, `Баг`, серьёзность 3.21/4, частота 0.74, релевантность 2.25/3, 1 комм. · @benzjeremy · обновлено 2026-08-18

**#1294** [Custom models added through Model Library cannot configure reasoning effort](https://github.com/siteboon/claudecodeui/issues/1294) — балл **70.5**, `Баг`, серьёзность 2.96/4, частота 0.76, релевантность 2.18/3, 0 комм. · @libra0037 · обновлено 2026-09-08

**#883** [No collision detection when resuming the same session id in a second pane](https://github.com/siteboon/claudecodeui/issues/883) — балл **70.5**, `Баг`, серьёзность 3.98/4, частота 0.5, релевантность 2.11/3, 0 комм. · @dennisgregory-lab · обновлено 2026-06-15

**#1367** [Newly uploaded workspace files do not appear immediately in the `@` file picker](https://github.com/siteboon/claudecodeui/issues/1367) — балл **70.3**, `Баг`, серьёзность 2.74/4, частота 0.74, релевантность 2.52/3, 0 комм. · @caiwd · обновлено 2026-09-22

**#1331** [Queued messages wait up to 30s to start — the dispatcher only polls, nothing fires on run completion](https://github.com/siteboon/claudecodeui/issues/1331) — балл **70.1**, `Баг`, серьёзность 2.81/4, частота 0.82, релевантность 2.12/3, 1 комм. · @happy-proger · обновлено 2026-09-16


## Issues, которые уже кто-то закрывает открытым PR (19)

**#1006** Shell: multi-line pastes execute line-by-line (bracketed paste bypassed) and Cmd+V/Ctrl+Shift+V paste nothing on plain-HTTP deployments — балл 73.1, PR: [#1007](https://github.com/siteboon/claudecodeui/pull/1007)

**#1452** 🚨 Chat can silently lose the first prompt despite an open WebSocket — балл 70.2, PR: [#1453](https://github.com/siteboon/claudecodeui/pull/1453)

**#1002** Session permanently lost from UI (untitled, empty transcript) when a message contains U+2028 — readline-based JSONL indexer aborts the whole file — балл 63.8, PR: [#1390](https://github.com/siteboon/claudecodeui/pull/1390)

**#1456** Mobile: composer stranded mid-screen after sending — --keyboard-height goes stale because visualViewport resize is its only writer — балл 54.8, PR: [#1457](https://github.com/siteboon/claudecodeui/pull/1457)

**#556** claude code login issue in OSX — балл 52.7, PR: [#1033](https://github.com/siteboon/claudecodeui/pull/1033)

**#1060** Codex sidebar ignores generated thread titles and keeps transcript fallbacks — балл 48.5, PR: [#1061](https://github.com/siteboon/claudecodeui/pull/1061)

**#1355** [Feature] Gracefully drain active chat runs during server shutdown — балл 48.3, PR: [#1356](https://github.com/siteboon/claudecodeui/pull/1356)

**#1108** [Bug] Plugin install fails with "tsc: not found" (exit 127) when server runs with NODE_ENV=production — балл 47.2, PR: [#1445](https://github.com/siteboon/claudecodeui/pull/1445)

**#1308** Stale X-Refreshed-Token replayed from browser HTTP cache (304 on /api/*) logs the user out right after login ("Your session expired") — балл 47.0, PR: [#1309](https://github.com/siteboon/claudecodeui/pull/1309)

**#1163** Claude runs leave no lifecycle record in the server log — балл 45.2, PR: [#1278](https://github.com/siteboon/claudecodeui/pull/1278)

**#797** Missing Logout Button in UI — балл 44.5, PR: [#978](https://github.com/siteboon/claudecodeui/pull/978)

**#1438** feat: support selectable CLI runtime profiles — балл 37.9, PR: [#1439](https://github.com/siteboon/claudecodeui/pull/1439)

**#1190** [Feature] Plugins have no sanctioned way to read host data or trigger navigation (+PR) — балл 29.9, PR: [#1191](https://github.com/siteboon/claudecodeui/pull/1191)

**#1187** [Feature] Environment variable for disabling update checking — балл 28.5, PR: [#1202](https://github.com/siteboon/claudecodeui/pull/1202)

**#1105** feat: user-selectable color themes (theme registry) — балл 20.4, PR: [#1248](https://github.com/siteboon/claudecodeui/pull/1248)

**#574** [Feature] Add Kiro (AWS Agentic IDE) support — балл 19.9, PR: [#760](https://github.com/siteboon/claudecodeui/pull/760)

**#1071** Feature request: group project cards by project name when ~/.claude is synced across machines — балл 15.4, PR: [#1072](https://github.com/siteboon/claudecodeui/pull/1072)

**#1298** [Feature] Read assistant replies aloud automatically, per session — балл 14.3, PR: [#1299](https://github.com/siteboon/claudecodeui/pull/1299)

**#345** Antigravity support — балл -10.4, PR: [#1352](https://github.com/siteboon/claudecodeui/pull/1352)


# Форки: проверено 1980, с коммитами впереди upstream — 320
После схлопывания клонов уникальных кандидатов — **317** (клонов одной и той же линии работы: 3 в 3 группах)

## Форки, которые стоит разобрать (в них есть работа, не отправленная в upstream)

**[z2512690268/claudecodeui](https://github.com/z2512690268/claudecodeui)** — балл **74.8**, `Фича`, впереди 1 коммитов, позади 209, ±486 строк, ★0, пуш 2026-05-05, ценность 3.18/4, дубль 0.44, секреты 0.12
  - `2e648a0f` 2026-05-05 feat: add DeepSeek models, fix Shell tab switching, add image/PDF preview

**[linchengming/claudecodeui](https://github.com/linchengming/claudecodeui)** — балл **73.3**, `Фича`, впереди 26 коммитов, позади 4, ±2390 строк, ★0, пуш 2026-09-27, ценность 3.19/4, дубль 0.39, секреты 0.14
  - `1fe6d2a1` 2026-09-24 feat(auth): add HTTPS, login rate limiting and optional TOTP 2FA
  - `b6bb2d61` 2026-09-25 docs: add Chinese Windows deployment guide
  - `2cf76e3a` 2026-09-26 feat(claude): keep runs waiting through quota and rate-limit errors until capacity recovers
  - `1d542c7b` 2026-09-26 feat(chat): default new sessions to Codex with GPT-5.6 Sol
  - `1d4303b2` 2026-09-26 docs: add Windows scheduled-task (S4U) auto-start deployment guide

**[vowers/claudecodeui](https://github.com/vowers/claudecodeui)** — балл **70.9**, `Фича`, впереди 3 коммитов, позади 206, ±1639 строк, ★0, пуш 2026-05-14, ценность 2.99/4, дубль 0.41, секреты 0.13
  - `16d454ac` 2026-05-14 feat: add SSE realtime fallback for chat and shell websockets
  - `66369181` 2026-05-14 fix(chat): reflect Skip Permissions override in mode pill
  - `4e6100bb` 2026-05-14 fix(chat): use SDK-reported context window for Claude token budget

**[visionquest-ai/claudecodeui](https://github.com/visionquest-ai/claudecodeui)** — балл **70.8**, `Фича`, впереди 4 коммитов, позади 22, ±556 строк, ★0, пуш 2026-09-14, ценность 2.92/4, дубль 0.42, секреты 0.13
  - `2c0752c7` 2026-09-11 feat(claude): enable token streaming, behind GRAPHTECT_STREAM_DELTAS
  - `ef4e2411` 2026-09-11 feat: stream transcript appends so terminal sessions reach clients live
  - `388c6143` 2026-09-11 feat: carry the provider's message blocks in the transcript append frame
  - `00773e8f` 2026-09-12 feat: one activity signal covering both terminal and daemon-driven sessions

**[coder8080/claudecodeui](https://github.com/coder8080/claudecodeui)** — балл **70.7**, `Фикс`, впереди 13 коммитов, позади 6, ±2402 строк, ★0, пуш 2026-09-25, ценность 2.43/4, дубль 0.53, секреты 0.13
  - `a7cb62a2` 2026-08-20 fix(chat): stop a fresh session slot from clobbering the live token budget
  - `212265e3` 2026-08-22 fix(chat): stamp client-created chat rows on the server clock
  - `0a4b066d` 2026-08-22 fix(file-tree): download files natively instead of buffering a blob URL
  - `2fc672f3` 2026-08-22 refactor: share one blob-download helper across chat, editor and PRD exports
  - `2f8028fb` 2026-08-22 test: run client .test.js suites and read import.meta.env behind a guard

**[bourgois/claudecodeui](https://github.com/bourgois/claudecodeui)** — балл **70.7**, `Фикс`, впереди 30 коммитов, позади 69, ±1063 строк, ★0, пуш 2026-07-10, ценность 2.78/4, дубль 0.54, секреты 0.14
  - `0a1ea62f` 2026-05-04 fix(claude-sync): skip subagent JSONL files to prevent main session corruption
  - `2fcf392d` 2026-05-28 feat: add Codex permission env fallback
  - `59c8b871` 2026-05-28 fix: address Codex permission review feedback
  - `907cbf71` 2026-05-30 fix: prevent system context injection from rendering as user messages
  - `6a8a5e97` 2026-05-30 fix: address CodeRabbit review findings

**[n0rthwood/claudecodeui](https://github.com/n0rthwood/claudecodeui)** — балл **70.4**, `Фича`, впереди 14 коммитов, позади 193, ±2376 строк, ★0, пуш 2026-06-06, ценность 3.62/4, дубль 0.42, секреты 0.13
  - `3dc675fa` 2026-06-04 fix(opencode): resolve session directory on deep-link resume; add AGENTS.md/CLAUDE.md
  - `6855dc76` 2026-06-04 chore: track CLAUDE.md symlink -> AGENTS.md across deployments
  - `ef8887ca` 2026-06-04 fix(chat): default permission mode falls back to global Settings for new conversations
  - `8e9adbe1` 2026-06-05 docs: design for tool-switch + fork session feature (incl. Bug1 model-resume fix)
  - `bcd991ca` 2026-06-05 docs: lock in fork-design decisions (model-switch on resume across providers)

**[ymolic/claudecodeui](https://github.com/ymolic/claudecodeui)** — балл **70.1**, `Фича`, впереди 4 коммитов, позади 43, ±2383 строк, ★0, пуш 2026-09-02, ценность 3.82/4, дубль 0.4, секреты 0.26
  - `c9c8366b` 2026-08-26 feat: integrate Google Antigravity CLI as a first-class provider
  - `df8ba63d` 2026-08-26 build(docker): optimize image build with host bundle and selective native rebuild
  - `51e9a81c` 2026-08-27 fix(antigravity): stop session indexing from corrupting the shared sidebar
  - `2e1b97d9` 2026-09-02 chore(systemd): add host deployment and Docker rollback

**[vaibhav541/claudecodeui](https://github.com/vaibhav541/claudecodeui)** — балл **70.0**, `Фича`, впереди 2 коммитов, позади 275, ±548 строк, ★0, пуш 2026-04-02, ценность 2.8/4, дубль 0.46, секреты 0.14
  - `31836252` 2026-04-02 fix: resolve processing stuck, message ordering, and startup config
  - `bfec0e06` 2026-04-02 feat: session tab bar and hide projects in sidebar

**[xiaohan815/claudecodeui](https://github.com/xiaohan815/claudecodeui)** — балл **69.7**, `Фикс`, впереди 9 коммитов, позади 276, ±183 строк, ★0, пуш 2026-05-14, ценность 2.59/4, дубль 0.52, секреты 0.11
  - `9b8ef404` 2026-03-10 style: 移除 CSS @layer 并内联移动端样式以提高兼容性
  - `ac32a6b3` 2026-03-10 feat(chat): 60秒无流事件兜底探测\nfix(websocket): 重连与消息补发更健壮\nfix(css): 移动端样式等价迁移，清除 esbuild minify 告警\n\n中文说明：\n- 新增 60 秒无流事件看门狗，自动校正 Processing 卡住\n- WebSocket 断线重连与队列补发，避免消息丢失\n- index.css 改为原生属性以兼容压缩器（功能不变
  - `64fc61ba` 2026-03-10 fix(websocket): 优化WebSocket连接处理并移除无用代码
  - `062efbf9` 2026-03-10 Merge branch 'siteboon:main' into main
  - `4e6f3244` 2026-03-11 Merge branch 'siteboon:main' into main

**[sermakov/claudecodeui](https://github.com/sermakov/claudecodeui)** — балл **68.9**, `Фикс`, впереди 3 коммитов, позади 266, ±126 строк, ★0, пуш 2026-04-14, ценность 2.41/4, дубль 0.4, секреты 0.12
  - `d29fe456` 2026-04-14 fix: allow running server inside Claude Code session
  - `1a50b464` 2026-04-14 feat: add file download button for remote/mobile access
  - `ff5f5c72` 2026-04-14 fix: add WebSocket ping heartbeat every 25s for mobile stability

**[huangyunhua-neolix/claudecodeui](https://github.com/huangyunhua-neolix/claudecodeui)** — балл **68.9**, `Фича`, впереди 5 коммитов, позади 273, ±1295 строк, ★0, пуш 2026-04-05, ценность 3.27/4, дубль 0.46, секреты 0.15
  - `bbc455a1` 2026-04-05 feat: refactor chat to raw terminal output with CLI subprocess (#19)
  - `5b62cae2` 2026-04-05 feat: add model selection in Claude settings page (#20)
  - `feec98d4` 2026-04-05 fix: deduplicate user messages and stabilize message keys (#21)
  - `92c37a3d` 2026-04-05 feat: add anthropic proxy for GPT model compatibility (#22)
  - `2725e276` 2026-04-05 fix: resolve claude binary path and decode project names with hyphens/underscores (#23)

**[xingcheng1061/claudecodeui](https://github.com/xingcheng1061/claudecodeui)** — балл **68.7**, `Фича`, впереди 18 коммитов, позади 4, ±6601 строк, ★0, пуш 2026-09-26, ценность 3.27/4, дубль 0.42, секреты 0.14
  - `41034a59` 2026-09-19 fix(claude): resolve the CLI path by walking PATH in-process
  - `39dae270` 2026-09-19 feat(chat): stream reasoning live, collapse thinking by default, independent subagent panel
  - `6417075a` 2026-09-20 feat(claude): learn context windows from results, forward subagent text, surface CLI commands
  - `a21b1d02` 2026-09-20 feat(claude): inject queued turns into a live run, settle tasks on teardown, close the CLI on abort
  - `98defc28` 2026-09-20 fix(chat): bucket stream deltas per session and calm the subagent panel

**[Mwhite84/cloudcli](https://github.com/Mwhite84/cloudcli)** — балл **68.6**, `Фича`, впереди 6 коммитов, позади 63, ±591 строк, ★0, пуш 2026-07-26, ценность 2.62/4, дубль 0.42, секреты 0.15
  - `3e733e36` 2026-07-21 Guard session resume against live external writers; badge and cap sidebar sessions
  - `354eba08` 2026-07-21 Badge MC-booted sessions distinctly via a launch-origin registry
  - `f87b616c` 2026-07-22 Attach to a live session's tmux instead of refusing to open it
  - `b67e43c5` 2026-07-23 feat(sessions): make chat the sole owner of cloudcli sessions + add chat heartbeat
  - `2b308df7` 2026-07-23 Retain Google models in OpenCode catalog

**[jothamgoh/cloudcli-patched](https://github.com/jothamgoh/cloudcli-patched)** — балл **68.4**, `Фича`, впереди 5 коммитов, позади 23, ±493 строк, ★0, пуш 2026-09-27, ценность 2.36/4, дубль 0.38, секреты 0.21
  - `873a2c89` 2026-09-27 chore: allow native install scripts needed to run from source
  - `2eb67f14` 2026-09-27 fix(notifications): use a VAPID subject Apple accepts
  - `b88f49a6` 2026-09-27 feat(chat): fold every run of tool calls into one quiet row
  - `98fe0d67` 2026-09-27 feat(workspace): show only the Chat tab
  - `4d093e76` 2026-09-27 feat(chat): steer a running Claude reply instead of queueing

**[digitalXperiments/claudecodeui](https://github.com/digitalXperiments/claudecodeui)** — балл **67.0**, `Фича`, впереди 201 коммитов, позади 63, ±21769 строк, ★0, пуш 2026-09-23, ценность 3.82/4, дубль 0.34, секреты 0.15
  - `e8c9b552` 2026-07-18 feat: add Grok Build and Kimi as CLI vendor providers
  - `a6545eef` 2026-07-18 docs: describe Grok Build and Kimi additions in the README
  - `755766ab` 2026-07-18 feat: add project categories to the sidebar
  - `e1862320` 2026-07-19 feat: add agy CLI provider and agent visibility controls
  - `eed348a8` 2026-07-19 feat(kanban): phase 0 — module skeleton + tab registration

**[newrootedgit/claudecodeui](https://github.com/newrootedgit/claudecodeui)** — балл **66.8**, `Фикс`, впереди 12 коммитов, позади 296, ±1451 строк, ★0, пуш 2026-05-17, ценность 3.37/4, дубль 0.4, секреты 0.15
  - `0553df82` 2026-03-14 Add persistent tmux-backed terminal sessions
  - `f6d96f7b` 2026-03-14 Fix terminal selection to switch to Shell tab
  - `bf90f6ef` 2026-03-14 fix: reconnect shell when switching between terminal sessions
  - `93f412fc` 2026-03-14 fix: prevent duplicate tmux attach causing double keystrokes
  - `4545caad` 2026-03-16 fix: guard tmux onData/onExit handlers with connectionId

**[facdbe-kt/claudecodeui](https://github.com/facdbe-kt/claudecodeui)** — балл **66.5**, `Фича`, впереди 19 коммитов, позади 126, ±8123 строк, ★0, пуш 2026-06-17, ценность 3.87/4, дубль 0.31, секреты 0.15
  - `16db5ec1` 2026-06-16 fix: pass skipPermissions to shell terminal and SDK bypass mode
  - `1c4cc570` 2026-06-16 feat: project grouping — DB, API, and sidebar UI for organizing projects into collapsible groups
  - `639ffc08` 2026-06-16 feat(sidebar): drag-and-drop + menu to move projects into groups, fix live refresh
  - `b828bb68` 2026-06-16 feat(sidebar): group color picker + restyled group headers
  - `08409544` 2026-06-16 fix(shell): restore vertical swipe-scroll in terminal on mobile

**[CyberBrown/claudecodeui](https://github.com/CyberBrown/claudecodeui)** — балл **66.3**, `Фича`, впереди 2 коммитов, позади 43, ±495 строк, ★0, пуш 2026-08-26, ценность 2.09/4, дубль 0.33, секреты 0.12
  - `8ca4d234` 2026-08-26 feat(guard): two-writer resume policy for live workers (WP #1018)
  - `fdaecdd4` 2026-08-26 Merge pull request #1 from CyberBrown/wp1018-two-writer-guard

**[Xandert6/claudecodeuiforcodex](https://github.com/Xandert6/claudecodeuiforcodex)** — балл **66.0**, `Фича`, впереди 18 коммитов, позади 55, ±680 строк, ★0, пуш 2026-08-03, ценность 2.77/4, дубль 0.53, секреты 0.16
  - `a49e496d` 2026-05-28 feat: add codex image support and sanitize session history
  - `a2b4d901` 2026-05-28 docs: add fork install and upstream sync guide
  - `02d607a6` 2026-05-29 feat: support codex file attachments
  - `6bcb014d` 2026-05-28 feat: add codex image support and sanitize session history
  - `f9e9bff8` 2026-05-28 docs: add fork install and upstream sync guide

**[dione/claudecodeui](https://github.com/dione/claudecodeui)** — балл **65.8**, `Фича`, впереди 2 коммитов, позади 206, ±1380 строк, ★0, пуш 2026-05-13, ценность 2.57/4, дубль 0.44, секреты 0.14
  - `c6f50f71` 2026-04-22 feat: add long-lived Claude CLI process per session (CLAUDE_STREAM_MODE)
  - `315c6ca8` 2026-05-13 fix(claude-sdk): use unique temp dir per handleImages call

**[cdxty/claudecodeui](https://github.com/cdxty/claudecodeui)** — балл **64.7**, `Фикс`, впереди 12 коммитов, позади 191, ±1216 строк, ★0, пуш 2026-06-04, ценность 2.51/4, дубль 0.57, секреты 0.11
  - `ebf75659` 2026-05-23 fix: prevent subagent messages from polluting main chat
  - `0c665c5f` 2026-05-23 fix: tag subagent messages from history with parentToolUseId
  - `a2eb4ebc` 2026-05-23 fix: never index subagent JSONL files as standalone sessions
  - `c8c422a7` 2026-05-23 fix(chat): render new Agent tool as a subagent container
  - `6701b493` 2026-05-23 fix(chat): stop remounting MessageComponent on every store update

**[CaineWind/claudecodeui](https://github.com/CaineWind/claudecodeui)** — балл **64.6**, `Фикс`, впереди 20 коммитов, позади 43, ±4922 строк, ★2, пуш 2026-09-02, ценность 3/4, дубль 0.44, секреты 0.12
  - `5aa81992` 2026-08-29 feat(codex): support native slash commands
  - `13bff986` 2026-08-29 fix(shell): avoid PowerShell codex shim policy errors
  - `062ed913` 2026-08-29 feat(herdr): add direct workspace mode
  - `d0384e0b` 2026-08-29 chore(dev): use port 5200
  - `eeb467a1` 2026-08-29 fix(auth): render structured login errors

**[agogo233/claudecodeui](https://github.com/agogo233/claudecodeui)** — балл **64.6**, `Фикс`, впереди 106 коммитов, позади 22, ±4750 строк, ★0, пуш 2026-09-09, ценность 3.41/4, дубль 0.45, секреты 0.13
  - `ddd37727` 2026-04-29 up
  - `fff66908` 2026-04-29 fix
  - `eb367034` 2026-05-14 gx
  - `349f7035` 2026-05-14 Merge branch 'siteboon:main' into main
  - `86c18e5d` 2026-05-14 fix

**[centerionware/claudecodeui](https://github.com/centerionware/claudecodeui)** — балл **64.3**, `Фикс`, впереди 5 коммитов, позади 52, ±164 строк, ★0, пуш 2026-08-04, ценность 2.05/4, дубль 0.5, секреты 0.08
  - `c16eda4c` 2026-08-02 fix: stop unbounded full-transcript refetch while chat tab is hidden
  - `ddc7855d` 2026-08-02 fix: dedupe concurrent refreshFromServer calls for the same session
  - `f6c0b0c2` 2026-08-02 fix: bound refreshFromServer to a tail refetch instead of full history
  - `147a522d` 2026-08-02 fix: use shared MESSAGES_PER_PAGE constant in fetchMore's default limit
  - `777b88e8` 2026-08-04 Merge branch 'main' into main

**[Huijie-Qin/claudecodeui](https://github.com/Huijie-Qin/claudecodeui)** — балл **63.9**, `Фикс`, впереди 1 коммитов, позади 229, ±285 строк, ★1, пуш 2026-09-24, ценность 2.19/4, дубль 0.47, секреты 0.16
  - `99848239` 2026-04-26 fix: stabilize claude session handling

**[openwengo/claudecodeui](https://github.com/openwengo/claudecodeui)** — балл **63.9**, `Фича`, впереди 3 коммитов, позади 254, ±212 строк, ★0, пуш 2026-04-15, ценность 3.56/4, дубль 0.42, секреты 0.28
  - `7d18e3bf` 2026-03-26 feat: claude and codex login with ANTHROPIC_AUTH_TOKEN and CODEX_API_KEY
  - `bb88c145` 2026-03-30 feat: auto provisionning from env variables
  - `c61a6f3b` 2026-03-30 feat: terminal access

**[dingxiaobo/claudecodeui](https://github.com/dingxiaobo/claudecodeui)** — балл **63.8**, `Фикс`, впереди 8 коммитов, позади 63, ±854 строк, ★0, пуш 2026-07-17, ценность 2.16/4, дубль 0.51, секреты 0.14
  - `981c577d` 2026-07-13 feat: remove width constraints, custom fonts, sidebar community buttons; fix copy underscore loss
  - `2c7577a4` 2026-07-15 Merge remote-tracking branch 'origin/main'
  - `070a2f48` 2026-07-15 Merge branch 'siteboon:main' into main
  - `bebcf0d0` 2026-07-16 Merge branch 'siteboon:main' into main
  - `ffe76b78` 2026-07-16 fix(opencode): exclude opencode built-in provider models from model list

**[asef18766/claudecodeui](https://github.com/asef18766/claudecodeui)** — балл **63.7**, `Фича`, впереди 9 коммитов, позади 18, ±4497 строк, ★0, пуш 2026-09-17, ценность 3.69/4, дубль 0.44, секреты 0.13
  - `11bfed38` 2026-09-15 feat(sandbox): run agent turns inside a Docker sandbox
  - `db96b28a` 2026-09-15 feat(project-tracking): pin sessions to a cross-project run board
  - `ff4b8dd9` 2026-09-16 Merge pull request #1 from asef18766/feat/docker-sandbox-and-project-tracking
  - `891e95d4` 2026-09-17 feat(chat): report session activity from the CLI instead of inferring it
  - `c478d464` 2026-09-17 feat(file-tree): hide gitignored paths by default, with a toggle to reveal them

**[t-huggy/claudecodeui](https://github.com/t-huggy/claudecodeui)** — балл **63.6**, `Фикс`, впереди 4 коммитов, позади 94, ±684 строк, ★0, пуш 2026-08-21, ценность 2.88/4, дубль 0.41, секреты 0.12
  - `164b8cd0` 2026-07-17 fix(chat): keep the SDK permission channel open for the whole turn; read office-doc attachments
  - `416855d3` 2026-07-17 feat(projects): auto-select the AI-OS project when VITE_DEFAULT_PROJECT_PATH is set
  - `ee2d9ffb` 2026-07-17 fix(permissions): wait indefinitely for tool approval instead of auto-denying after 55s
  - `58d1ef12` 2026-08-21 fix(auth): stop a failed re-check from tearing down a fresh login

**[WangJie-cn/claudecodeui](https://github.com/WangJie-cn/claudecodeui)** — балл **63.0**, `Фича`, впереди 13 коммитов, позади 273, ±537 строк, ★0, пуш 2026-04-07, ценность 3.05/4, дубль 0.41, секреты 0.1
  - `6a70862b` 2026-04-07 feat: integrate tmux session selector into Shell tab
  - `95d720d9` 2026-04-07 feat: add Terminal button to provider selection
  - `a6e1d2c5` 2026-04-07 fix: prevent auto-connect when opening Shell via Terminal button
  - `65282935` 2026-04-07 feat: auto-hide shell chrome for fullscreen terminal
  - `f070134d` 2026-04-07 feat: hide parent header and FAB in shell fullscreen

**[kanazawahere/claudecodeui](https://github.com/kanazawahere/claudecodeui)** — балл **62.9**, `Фича`, впереди 3 коммитов, позади 63, ±179 строк, ★0, пуш 2026-08-02, ценность 3.13/4, дубль 0.49, секреты 0.21
  - `a237350e` 2026-07-19 feat(atp): add trusted self-host mode and OpenCode DB override
  - `729a310a` 2026-07-19 fix(atp): expose exact corresponding source in trusted UI
  - `8bf4568f` 2026-08-02 fix(atp): abort prior queryInstance before writer-swap overwrite (#885)

**[tyx3211/claudecodeui](https://github.com/tyx3211/claudecodeui)** — балл **62.9**, `Фича`, впереди 6 коммитов, позади 126, ±1065 строк, ★1, пуш 2026-06-16, ценность 3.19/4, дубль 0.4, секреты 0.17
  - `cc8dcc51` 2026-06-16 feat: add shared-host subagent support
  - `c9e6d703` 2026-06-16 fix: filter claude subagent output
  - `a16093b5` 2026-06-16 feat: mirror subagent stdout to file
  - `13e1d020` 2026-06-16 fix: surface claude subagent errors
  - `f6fa59ce` 2026-06-16 feat: inspect subagent session project

**[Dominicushuy/cloudcli-vps](https://github.com/Dominicushuy/cloudcli-vps)** — балл **62.9**, `Фича`, впереди 4 коммитов, позади 209, ±70 строк, ★0, пуш 2026-05-08, ценность 2.48/4, дубль 0.32, секреты 0.2
  - `9a17f8b2` 2026-05-08 fork-patch: enable WebSocket perMessageDeflate (PF-13)
  - `9ca760e2` 2026-05-08 fork-patch: add WebSocket heartbeat 25s (PF-12)
  - `09774f7e` 2026-05-08 fork-patch: env-based bypassPermissions for headless deploy (D10)
  - `ee34489f` 2026-05-08 fork-patch: env-driven default UI permission mode (D11)

**[jefferyb/claudecodeui](https://github.com/jefferyb/claudecodeui)** — балл **62.9**, `Фича`, впереди 1 коммитов, позади 349, ±527 строк, ★0, пуш 2026-03-01, ценность 3.45/4, дубль 0.29, секреты 0.16
  - `d79a97b9` 2026-03-01 feat(cursor): full Cursor session management and UX improvements

**[wxhn1225/codecliui](https://github.com/wxhn1225/codecliui)** — балл **62.8**, `Фича`, впереди 1 коммитов, позади 687, ±436 строк, ★0, пуш 2025-08-25, ценность 3.52/4, дубль 0.4, секреты 0.15
  - `fcf593e6` 2025-08-25 feat: 支持qwen-code

**[wyt990/claudecodeui](https://github.com/wyt990/claudecodeui)** — балл **62.6**, `Фикс`, впереди 22 коммитов, позади 266, ±16324 строк, ★0, пуш 2026-05-05, ценность 3.66/4, дубль 0.42, секреты 0.18
  - `6ca7c118` 2026-04-14 feat: 增加对claudecode的支持
  - `aad7c967` 2026-04-14 feat: 增加项目目录树功能
  - `9feecfe0` 2026-04-14 fix: 修复项目目录树无法滚动的问题
  - `9c7ff22a` 2026-04-26 feat: 增加纯SSH多服务器远程环境与CLI探测方案
  - `0773cd2b` 2026-04-26 fix: 修复远程项目无法获取目录树的问题

**[Share-With-GPT/claudecodeui](https://github.com/Share-With-GPT/claudecodeui)** — балл **62.3**, `Фича`, впереди 4 коммитов, позади 687, ±654 строк, ★0, пуш 2025-08-27, ценность 3.59/4, дубль 0.47, секреты 0.18
  - `bc8cc1fe` 2025-08-27 add test_node_ssh.js
  - `dfe6bc11` 2025-08-27 add test_argv.py
  - `d724a651` 2025-08-27 feat: add SSH support for remote Claude sessions
  - `adfde2a4` 2025-08-27 Merge pull request #1 from Share-With-GPT/codex/add-ssh-remote-execution-support

**[dannyking94/claudecodeui](https://github.com/dannyking94/claudecodeui)** — балл **61.9**, `Фича`, впереди 19 коммитов, позади 52, ±10571 строк, ★0, пуш 2026-09-21, ценность 3.19/4, дубль 0.49, секреты 0.14
  - `1d77f609` 2026-08-05 fix(shell): keep plain-shell tab alive when no command is given
  - `869ead01` 2026-08-05 fix(chat): keep reading position stable when messages arrive
  - `5457ba8b` 2026-08-05 fix(claude): stamp CLAUDE_CODE_ENTRYPOINT so sessions stay visible
  - `f0da0705` 2026-08-05 fix(chat): stop fighting the scroll gesture while it is in flight
  - `7c257d2d` 2026-08-06 feat(system): add live GPU and CPU status panel

**[TheWebEng/claudecodeui](https://github.com/TheWebEng/claudecodeui)** — балл **61.6**, `Фича`, впереди 12 коммитов, позади 63, ±1713 строк, ★0, пуш 2026-08-10, ценность 2.12/4, дубль 0.57, секреты 0.13
  - `672d15c4` 2026-07-18 fix(claude): detect macOS Keychain authentication
  - `d2b32b65` 2026-07-18 fix(claude): validate CLI installation check
  - `3f0a7fee` 2026-07-18 feat(appearance): add system font preference
  - `6c170b82` 2026-07-18 feat: add provider session ID copy actions
  - `a3a6d335` 2026-07-18 feat(sidebar): add recent conversation feed

## Клоны (та же линия работы, что у представителя)

- AgentDevOS/Incomify: ещё 1 — AgentDevOS/claudecodeui
- stud20/claudecodeui: ещё 1 — PieceMaker-Legal/piecemaker-droit-francais
- carljohnvillavito/claude-code-ui: ещё 1 — 5hojib/claudecodeui


# Стек: цена поддержки при мёрдже апстрима

Собрали 27 выбранных PR (consider, take) последовательно в основную ветку:

- влились чисто: **20**
- конфликтов при сборке: **7** (25.9%)
- объём патча: 57 файлов, 57 files changed, 4755 insertions(+), 502 deletions(-)
- поверхность будущих конфликтов: **6.65%** правок upstream за последние 400 коммитов приходятся на файлы, которые патчит наш стек (57 из 57 наших файлов)

## Что конфликтует

- #1444: server/modules/providers/list/claude/claude-runtime.provider.ts, server/modules/providers/tests/claude-runtime-hold.test.ts
- #1439: server/modules/providers/list/claude/claude-runtime.provider.ts
- #1453: src/modules/chat/hooks/useChatComposerState.ts
- #1356: .env.example
- #1449: server/modules/providers/list/claude/claude-runtime.provider.ts, server/modules/providers/tests/claude-sessions.test.ts, src/modules/chat/hooks/useChatComposerS
- #1000: server/modules/browser-use/browser-use.service.ts
- #1278: server/modules/providers/list/claude/claude-runtime.provider.ts

## Самые горячие файлы, которые мы патчим (правок upstream за окно)

- `server/shared/utils.ts` — 21
- `server/shared/types.ts` — 19
- `server/modules/database/repositories/sessions.db.ts` — 13
- `server/modules/providers/list/claude/claude-sessions.provider.ts` — 13
- `server/modules/providers/list/codex/codex-sessions.provider.ts` — 11
- `server/shared/interfaces.ts` — 11
- `server/modules/providers/tests/codex-sessions.test.ts` — 10
- `server/modules/database/migrations.ts` — 9
- `server/modules/providers/list/codex/codex-session-synchronizer.provider.ts` — 9
- `server/modules/providers/services/sessions-watcher.service.ts` — 8
- `server/modules/database/schema.ts` — 8
- `server/modules/providers/tests/claude-sessions.test.ts` — 8
- `server/modules/providers/list/claude/claude-session-synchronizer.provider.ts` — 8
- `server/modules/providers/services/session-conversations-search.service.ts` — 7
- `server/modules/providers/tests/opencode-sessions.test.ts` — 7


# Карта мёрджей: попарный анализ и расклады

Кандидатов 47 (выжившие PR + лучшие форки), пар 1081, живьём мержили пересекающиеся по файлам: 280, смысловое сравнение через Jev: 150.

| расклад | берём | сумма баллов | конфликтов внутри | файлов | горячих правок |
|---|---:|---:|---:|---:|---:|
| **Безопасный — максимум по баллу без конфликтов внутри** | 24 | 1531.2 | 0 | 87 | 15.06% |
| **Всё в одно — конфликты разбираем руками** | 47 | 3076.3 | 241 | 1386 | 160.5% |
| **Топ по баллу — цена поддержки не важна** | 20 | 1436.2 | 48 | 241 | 57.88% |
| **Минимум поверхности — что реже ломается апстримом** | 24 | 1530.6 | 0 | 83 | 14.69% |
| **По одному на подсистему — шире, а не глубже** | 24 | 1543.9 | 4 | 110 | 15.7% |

## Расклад: Безопасный — максимум по баллу без конфликтов внутри

Берём 24 (19 PR + 5 форков), сумма баллов 1531.2, конфликтов внутри 0, файлов 87, доля горячих правок 15.06%.

- `pr-1426` [fix(opencode): read live run events nested under part](https://github.com/siteboon/claudecodeui/pull1426) — балл 83.8, 2 файлов, 183 строк
- `fork-z2512690268/claudecodeui` [z2512690268/claudecodeui](https://github.com/siteboon/claudecodeui/) — балл 74.8, 11 файлов, 427 строк
- `pr-1247` [fix(auth): ignore refreshed tokens that are not newer than the stored one](https://github.com/siteboon/claudecodeui/pull1247) — балл 74.7, 2 файлов, 142 строк
- `pr-1446` [fix(claude): keep history after background task notifications](https://github.com/siteboon/claudecodeui/pull1446) — балл 73.2, 2 файлов, 87 строк
- `pr-1390` [fix(sessions): keep transcript rows that contain U+2028 or U+2029](https://github.com/siteboon/claudecodeui/pull1390) — балл 72.2, 7 файлов, 475 строк
- `pr-1431` [fix(claude): preserve background work across user turns](https://github.com/siteboon/claudecodeui/pull1431) — балл 71.5, 7 файлов, 756 строк
- `fork-visionquest-ai/claudecodeui` [visionquest-ai/claudecodeui](https://github.com/siteboon/claudecodeui/) — балл 70.8, 5 файлов, 555 строк
- `fork-vaibhav541/claudecodeui` [vaibhav541/claudecodeui](https://github.com/siteboon/claudecodeui/) — балл 70.0, 13 файлов, 524 строк
- `pr-1440` [fix(chat): drop repeat send presses while a submit is in flight](https://github.com/siteboon/claudecodeui/pull1440) — балл 69.6, 2 файлов, 149 строк
- `pr-1007` [fix(shell): paste through terminal.paste() and stop swallowing native paste](https://github.com/siteboon/claudecodeui/pull1007) — балл 69.4, 2 файлов, 26 строк
- `fork-sermakov/claudecodeui` [sermakov/claudecodeui](https://github.com/siteboon/claudecodeui/) — балл 68.9, 6 файлов, 124 строк
- `fork-CyberBrown/claudecodeui` [CyberBrown/claudecodeui](https://github.com/siteboon/claudecodeui/) — балл 66.3, 5 файлов, 495 строк
- `pr-1202` [feat: add CLOUDCLI_DISABLE_UPDATE_CHECK to disable update checks](https://github.com/siteboon/claudecodeui/pull1202) — балл 64.2, 8 файлов, 367 строк
- `pr-1365` [fix(chat): discard stale selection responses after session navigation](https://github.com/siteboon/claudecodeui/pull1365) — балл 61.7, 2 файлов, 156 строк
- `pr-1364` [fix(chat): guard tool lookups against inherited properties](https://github.com/siteboon/claudecodeui/pull1364) — балл 61.3, 4 файлов, 59 строк
- `pr-995` [fix: install browser runtime outside process cwd](https://github.com/siteboon/claudecodeui/pull995) — балл 60.6, 2 файлов, 365 строк
- `pr-1436` [fix(windows): resolve the claude CLI by walking PATH instead of where.exe](https://github.com/siteboon/claudecodeui/pull1436) — балл 58.9, 2 файлов, 236 строк
- `pr-1457` [fix(workspace): don't strand the composer mid-screen after the keyboard hides](https://github.com/siteboon/claudecodeui/pull1457) — балл 58.0, 1 файлов, 47 строк
- `pr-1445` [fix(plugins): include devDependencies when installing plugins](https://github.com/siteboon/claudecodeui/pull1445) — балл 57.1, 2 файлов, 129 строк
- `pr-959` [fix: add Codex provider complete fields](https://github.com/siteboon/claudecodeui/pull959) — балл 55.7, 2 файлов, 21 строк
- `pr-1310` [fix(auth): verify the session once per mount, not once per token refresh](https://github.com/siteboon/claudecodeui/pull1310) — балл 52.6, 2 файлов, 171 строк
- `pr-1111` [fix: correct workspace root containment check for root paths](https://github.com/siteboon/claudecodeui/pull1111) — балл 52.3, 2 файлов, 59 строк
- `pr-1178` [perf(sessions): resolve the session title without holding the transcript](https://github.com/siteboon/claudecodeui/pull1178) — балл 43.0, 3 файлов, 412 строк
- `pr-1278` [Log Claude run lifecycle transitions](https://github.com/siteboon/claudecodeui/pull1278) — балл 40.6, 2 файлов, 263 строк

## Расклад: Всё в одно — конфликты разбираем руками

Берём 47 (27 PR + 20 форков), сумма баллов 3076.3, конфликтов внутри 241, файлов 1386, доля горячих правок 160.5%.

- `pr-1426` [fix(opencode): read live run events nested under part](https://github.com/siteboon/claudecodeui/pull1426) — балл 83.8, 2 файлов, 183 строк
- `fork-z2512690268/claudecodeui` [z2512690268/claudecodeui](https://github.com/siteboon/claudecodeui/) — балл 74.8, 11 файлов, 427 строк
- `pr-1247` [fix(auth): ignore refreshed tokens that are not newer than the stored one](https://github.com/siteboon/claudecodeui/pull1247) — балл 74.7, 2 файлов, 142 строк
- `fork-linchengming/claudecodeui` [linchengming/claudecodeui](https://github.com/siteboon/claudecodeui/) — балл 73.3, 40 файлов, 2029 строк
- `pr-1446` [fix(claude): keep history after background task notifications](https://github.com/siteboon/claudecodeui/pull1446) — балл 73.2, 2 файлов, 87 строк
- `pr-1390` [fix(sessions): keep transcript rows that contain U+2028 or U+2029](https://github.com/siteboon/claudecodeui/pull1390) — балл 72.2, 7 файлов, 475 строк
- `pr-1431` [fix(claude): preserve background work across user turns](https://github.com/siteboon/claudecodeui/pull1431) — балл 71.5, 7 файлов, 756 строк
- `pr-1444` [fix(claude): wait for a superseded run to exit before resuming its session](https://github.com/siteboon/claudecodeui/pull1444) — балл 70.9, 3 файлов, 225 строк
- `fork-vowers/claudecodeui` [vowers/claudecodeui](https://github.com/siteboon/claudecodeui/) — балл 70.9, 27 файлов, 1191 строк
- `fork-visionquest-ai/claudecodeui` [visionquest-ai/claudecodeui](https://github.com/siteboon/claudecodeui/) — балл 70.8, 5 файлов, 555 строк
- `fork-coder8080/claudecodeui` [coder8080/claudecodeui](https://github.com/siteboon/claudecodeui/) — балл 70.7, 46 файлов, 2287 строк
- `fork-bourgois/claudecodeui` [bourgois/claudecodeui](https://github.com/siteboon/claudecodeui/) — балл 70.7, 31 файлов, 894 строк
- `pr-1439` [feat(providers): add selectable runtime profiles](https://github.com/siteboon/claudecodeui/pull1439) — балл 70.6, 25 файлов, 674 строк
- `fork-n0rthwood/claudecodeui` [n0rthwood/claudecodeui](https://github.com/siteboon/claudecodeui/) — балл 70.4, 35 файлов, 2320 строк
- `fork-ymolic/claudecodeui` [ymolic/claudecodeui](https://github.com/siteboon/claudecodeui/) — балл 70.1, 51 файлов, 2362 строк
- `fork-vaibhav541/claudecodeui` [vaibhav541/claudecodeui](https://github.com/siteboon/claudecodeui/) — балл 70.0, 13 файлов, 524 строк
- `fork-xiaohan815/claudecodeui` [xiaohan815/claudecodeui](https://github.com/siteboon/claudecodeui/) — балл 69.7, 8 файлов, 162 строк
- `pr-1440` [fix(chat): drop repeat send presses while a submit is in flight](https://github.com/siteboon/claudecodeui/pull1440) — балл 69.6, 2 файлов, 149 строк
- `pr-1007` [fix(shell): paste through terminal.paste() and stop swallowing native paste](https://github.com/siteboon/claudecodeui/pull1007) — балл 69.4, 2 файлов, 26 строк
- `fork-sermakov/claudecodeui` [sermakov/claudecodeui](https://github.com/siteboon/claudecodeui/) — балл 68.9, 6 файлов, 124 строк
- `fork-huangyunhua-neolix/claudecodeui` [huangyunhua-neolix/claudecodeui](https://github.com/siteboon/claudecodeui/) — балл 68.9, 10 файлов, 1187 строк
- `fork-xingcheng1061/claudecodeui` [xingcheng1061/claudecodeui](https://github.com/siteboon/claudecodeui/) — балл 68.7, 80 файлов, 6234 строк
- `fork-Mwhite84/cloudcli` [Mwhite84/cloudcli](https://github.com/siteboon/claudecodeui/) — балл 68.6, 27 файлов, 559 строк
- `fork-jothamgoh/cloudcli-patched` [jothamgoh/cloudcli-patched](https://github.com/siteboon/claudecodeui/) — балл 68.4, 15 файлов, 397 строк
- `pr-1453` [🚨 fix(chat): require server receipt before clearing the first prompt](https://github.com/siteboon/claudecodeui/pull1453) — балл 67.6, 17 файлов, 619 строк
- `fork-digitalXperiments/claudecodeui` [digitalXperiments/claudecodeui](https://github.com/siteboon/claudecodeui/) — балл 67.0, 1121 файлов, 196963 строк
- `fork-newrootedgit/claudecodeui` [newrootedgit/claudecodeui](https://github.com/siteboon/claudecodeui/) — балл 66.8, 26 файлов, 1312 строк
- `fork-facdbe-kt/claudecodeui` [facdbe-kt/claudecodeui](https://github.com/siteboon/claudecodeui/) — балл 66.5, 75 файлов, 7811 строк
- `fork-CyberBrown/claudecodeui` [CyberBrown/claudecodeui](https://github.com/siteboon/claudecodeui/) — балл 66.3, 5 файлов, 495 строк
- `fork-Xandert6/claudecodeuiforcodex` [Xandert6/claudecodeuiforcodex](https://github.com/siteboon/claudecodeui/) — балл 66.0, 10 файлов, 673 строк
- `pr-1202` [feat: add CLOUDCLI_DISABLE_UPDATE_CHECK to disable update checks](https://github.com/siteboon/claudecodeui/pull1202) — балл 64.2, 8 файлов, 367 строк
- `pr-1356` [fix(server): drain active chats on shutdown](https://github.com/siteboon/claudecodeui/pull1356) — балл 62.2, 6 файлов, 222 строк
- `pr-1365` [fix(chat): discard stale selection responses after session navigation](https://github.com/siteboon/claudecodeui/pull1365) — балл 61.7, 2 файлов, 156 строк
- `pr-1449` [feat(chat): three send modes while a turn is running — after turn, after next tool call, now](https://github.com/siteboon/claudecodeui/pull1449) — балл 61.3, 23 файлов, 2991 строк
- `pr-1364` [fix(chat): guard tool lookups against inherited properties](https://github.com/siteboon/claudecodeui/pull1364) — балл 61.3, 4 файлов, 59 строк
- `pr-995` [fix: install browser runtime outside process cwd](https://github.com/siteboon/claudecodeui/pull995) — балл 60.6, 2 файлов, 365 строк
- `pr-1000` [fix(browser): install Playwright runtime in package dir, not cwd](https://github.com/siteboon/claudecodeui/pull1000) — балл 60.4, 1 файлов, 33 строк
- `pr-1213` [fix(claude): normalize queue-operation remove records as user-role text](https://github.com/siteboon/claudecodeui/pull1213) — балл 59.8, 2 файлов, 116 строк
- `pr-1436` [fix(windows): resolve the claude CLI by walking PATH instead of where.exe](https://github.com/siteboon/claudecodeui/pull1436) — балл 58.9, 2 файлов, 236 строк
- `pr-1457` [fix(workspace): don't strand the composer mid-screen after the keyboard hides](https://github.com/siteboon/claudecodeui/pull1457) — балл 58.0, 1 файлов, 47 строк

  Конфликтные пары внутри расклада: pr-1426×fork-linchengming/claudecodeui, pr-1426×fork-n0rthwood/claudecodeui, pr-1426×fork-digitalXperiments/claudecodeui, fork-z2512690268/claudecodeui×fork-vowers/claudecodeui, fork-z2512690268/claudecodeui×fork-xiaohan815/claudecodeui, fork-z2512690268/claudecodeui×fork-Mwhite84/cloudcli, fork-z2512690268/claudecodeui×fork-digitalXperiments/claudecodeui, fork-z2512690268/claudecodeui×fork-newrootedgit/claudecodeui, fork-z2512690268/claudecodeui×fork-facdbe-kt/claudecodeui, fork-z2512690268/claudecodeui×fork-Xandert6/claudecodeuiforcodex

## Расклад: Топ по баллу — цена поддержки не важна

Берём 20 (9 PR + 11 форков), сумма баллов 1436.2, конфликтов внутри 48, файлов 241, доля горячих правок 57.88%.

- `pr-1426` [fix(opencode): read live run events nested under part](https://github.com/siteboon/claudecodeui/pull1426) — балл 83.8, 2 файлов, 183 строк
- `fork-z2512690268/claudecodeui` [z2512690268/claudecodeui](https://github.com/siteboon/claudecodeui/) — балл 74.8, 11 файлов, 427 строк
- `pr-1247` [fix(auth): ignore refreshed tokens that are not newer than the stored one](https://github.com/siteboon/claudecodeui/pull1247) — балл 74.7, 2 файлов, 142 строк
- `fork-linchengming/claudecodeui` [linchengming/claudecodeui](https://github.com/siteboon/claudecodeui/) — балл 73.3, 40 файлов, 2029 строк
- `pr-1446` [fix(claude): keep history after background task notifications](https://github.com/siteboon/claudecodeui/pull1446) — балл 73.2, 2 файлов, 87 строк
- `pr-1390` [fix(sessions): keep transcript rows that contain U+2028 or U+2029](https://github.com/siteboon/claudecodeui/pull1390) — балл 72.2, 7 файлов, 475 строк
- `pr-1431` [fix(claude): preserve background work across user turns](https://github.com/siteboon/claudecodeui/pull1431) — балл 71.5, 7 файлов, 756 строк
- `pr-1444` [fix(claude): wait for a superseded run to exit before resuming its session](https://github.com/siteboon/claudecodeui/pull1444) — балл 70.9, 3 файлов, 225 строк
- `fork-vowers/claudecodeui` [vowers/claudecodeui](https://github.com/siteboon/claudecodeui/) — балл 70.9, 27 файлов, 1191 строк
- `fork-visionquest-ai/claudecodeui` [visionquest-ai/claudecodeui](https://github.com/siteboon/claudecodeui/) — балл 70.8, 5 файлов, 555 строк
- `fork-coder8080/claudecodeui` [coder8080/claudecodeui](https://github.com/siteboon/claudecodeui/) — балл 70.7, 46 файлов, 2287 строк
- `fork-bourgois/claudecodeui` [bourgois/claudecodeui](https://github.com/siteboon/claudecodeui/) — балл 70.7, 31 файлов, 894 строк
- `pr-1439` [feat(providers): add selectable runtime profiles](https://github.com/siteboon/claudecodeui/pull1439) — балл 70.6, 25 файлов, 674 строк
- `fork-n0rthwood/claudecodeui` [n0rthwood/claudecodeui](https://github.com/siteboon/claudecodeui/) — балл 70.4, 35 файлов, 2320 строк
- `fork-ymolic/claudecodeui` [ymolic/claudecodeui](https://github.com/siteboon/claudecodeui/) — балл 70.1, 51 файлов, 2362 строк
- `fork-vaibhav541/claudecodeui` [vaibhav541/claudecodeui](https://github.com/siteboon/claudecodeui/) — балл 70.0, 13 файлов, 524 строк
- `fork-xiaohan815/claudecodeui` [xiaohan815/claudecodeui](https://github.com/siteboon/claudecodeui/) — балл 69.7, 8 файлов, 162 строк
- `pr-1440` [fix(chat): drop repeat send presses while a submit is in flight](https://github.com/siteboon/claudecodeui/pull1440) — балл 69.6, 2 файлов, 149 строк
- `pr-1007` [fix(shell): paste through terminal.paste() and stop swallowing native paste](https://github.com/siteboon/claudecodeui/pull1007) — балл 69.4, 2 файлов, 26 строк
- `fork-sermakov/claudecodeui` [sermakov/claudecodeui](https://github.com/siteboon/claudecodeui/) — балл 68.9, 6 файлов, 124 строк

  Конфликтные пары внутри расклада: pr-1426×fork-linchengming/claudecodeui, pr-1426×fork-n0rthwood/claudecodeui, fork-z2512690268/claudecodeui×fork-vowers/claudecodeui, fork-z2512690268/claudecodeui×fork-xiaohan815/claudecodeui, fork-linchengming/claudecodeui×pr-1431, fork-linchengming/claudecodeui×pr-1444, fork-linchengming/claudecodeui×fork-vowers/claudecodeui, fork-linchengming/claudecodeui×fork-coder8080/claudecodeui, fork-linchengming/claudecodeui×pr-1439, fork-linchengming/claudecodeui×fork-n0rthwood/claudecodeui

## Расклад: Минимум поверхности — что реже ломается апстримом

Берём 24 (19 PR + 5 форков), сумма баллов 1530.6, конфликтов внутри 0, файлов 83, доля горячих правок 14.69%.

- `pr-1426` [fix(opencode): read live run events nested under part](https://github.com/siteboon/claudecodeui/pull1426) — балл 83.8, 2 файлов, 183 строк
- `pr-1247` [fix(auth): ignore refreshed tokens that are not newer than the stored one](https://github.com/siteboon/claudecodeui/pull1247) — балл 74.7, 2 файлов, 142 строк
- `pr-1446` [fix(claude): keep history after background task notifications](https://github.com/siteboon/claudecodeui/pull1446) — балл 73.2, 2 файлов, 87 строк
- `pr-1444` [fix(claude): wait for a superseded run to exit before resuming its session](https://github.com/siteboon/claudecodeui/pull1444) — балл 70.9, 3 файлов, 225 строк
- `pr-1440` [fix(chat): drop repeat send presses while a submit is in flight](https://github.com/siteboon/claudecodeui/pull1440) — балл 69.6, 2 файлов, 149 строк
- `fork-visionquest-ai/claudecodeui` [visionquest-ai/claudecodeui](https://github.com/siteboon/claudecodeui/) — балл 70.8, 5 файлов, 555 строк
- `pr-1007` [fix(shell): paste through terminal.paste() and stop swallowing native paste](https://github.com/siteboon/claudecodeui/pull1007) — балл 69.4, 2 файлов, 26 строк
- `fork-CyberBrown/claudecodeui` [CyberBrown/claudecodeui](https://github.com/siteboon/claudecodeui/) — балл 66.3, 5 файлов, 495 строк
- `pr-1390` [fix(sessions): keep transcript rows that contain U+2028 or U+2029](https://github.com/siteboon/claudecodeui/pull1390) — балл 72.2, 7 файлов, 475 строк
- `fork-z2512690268/claudecodeui` [z2512690268/claudecodeui](https://github.com/siteboon/claudecodeui/) — балл 74.8, 11 файлов, 427 строк
- `pr-1365` [fix(chat): discard stale selection responses after session navigation](https://github.com/siteboon/claudecodeui/pull1365) — балл 61.7, 2 файлов, 156 строк
- `pr-1364` [fix(chat): guard tool lookups against inherited properties](https://github.com/siteboon/claudecodeui/pull1364) — балл 61.3, 4 файлов, 59 строк
- `pr-995` [fix: install browser runtime outside process cwd](https://github.com/siteboon/claudecodeui/pull995) — балл 60.6, 2 файлов, 365 строк
- `pr-1202` [feat: add CLOUDCLI_DISABLE_UPDATE_CHECK to disable update checks](https://github.com/siteboon/claudecodeui/pull1202) — балл 64.2, 8 файлов, 367 строк
- `pr-1436` [fix(windows): resolve the claude CLI by walking PATH instead of where.exe](https://github.com/siteboon/claudecodeui/pull1436) — балл 58.9, 2 файлов, 236 строк
- `pr-1457` [fix(workspace): don't strand the composer mid-screen after the keyboard hides](https://github.com/siteboon/claudecodeui/pull1457) — балл 58.0, 1 файлов, 47 строк
- `fork-sermakov/claudecodeui` [sermakov/claudecodeui](https://github.com/siteboon/claudecodeui/) — балл 68.9, 6 файлов, 124 строк
- `pr-1445` [fix(plugins): include devDependencies when installing plugins](https://github.com/siteboon/claudecodeui/pull1445) — балл 57.1, 2 файлов, 129 строк
- `pr-959` [fix: add Codex provider complete fields](https://github.com/siteboon/claudecodeui/pull959) — балл 55.7, 2 файлов, 21 строк
- `pr-1310` [fix(auth): verify the session once per mount, not once per token refresh](https://github.com/siteboon/claudecodeui/pull1310) — балл 52.6, 2 файлов, 171 строк
- `pr-1111` [fix: correct workspace root containment check for root paths](https://github.com/siteboon/claudecodeui/pull1111) — балл 52.3, 2 файлов, 59 строк
- `pr-1178` [perf(sessions): resolve the session title without holding the transcript](https://github.com/siteboon/claudecodeui/pull1178) — балл 43.0, 3 файлов, 412 строк
- `pr-1278` [Log Claude run lifecycle transitions](https://github.com/siteboon/claudecodeui/pull1278) — балл 40.6, 2 файлов, 263 строк
- `fork-vaibhav541/claudecodeui` [vaibhav541/claudecodeui](https://github.com/siteboon/claudecodeui/) — балл 70.0, 13 файлов, 524 строк

## Расклад: По одному на подсистему — шире, а не глубже

Берём 24 (20 PR + 4 форков), сумма баллов 1543.9, конфликтов внутри 4, файлов 110, доля горячих правок 15.7%.

- `pr-1426` [fix(opencode): read live run events nested under part](https://github.com/siteboon/claudecodeui/pull1426) — балл 83.8, 2 файлов, 183 строк
- `pr-1247` [fix(auth): ignore refreshed tokens that are not newer than the stored one](https://github.com/siteboon/claudecodeui/pull1247) — балл 74.7, 2 файлов, 142 строк
- `pr-1390` [fix(sessions): keep transcript rows that contain U+2028 or U+2029](https://github.com/siteboon/claudecodeui/pull1390) — балл 72.2, 7 файлов, 475 строк
- `pr-1440` [fix(chat): drop repeat send presses while a submit is in flight](https://github.com/siteboon/claudecodeui/pull1440) — балл 69.6, 2 файлов, 149 строк
- `pr-1202` [feat: add CLOUDCLI_DISABLE_UPDATE_CHECK to disable update checks](https://github.com/siteboon/claudecodeui/pull1202) — балл 64.2, 8 файлов, 367 строк
- `pr-1000` [fix(browser): install Playwright runtime in package dir, not cwd](https://github.com/siteboon/claudecodeui/pull1000) — балл 60.4, 1 файлов, 33 строк
- `pr-1445` [fix(plugins): include devDependencies when installing plugins](https://github.com/siteboon/claudecodeui/pull1445) — балл 57.1, 2 файлов, 129 строк
- `fork-z2512690268/claudecodeui` [z2512690268/claudecodeui](https://github.com/siteboon/claudecodeui/) — балл 74.8, 11 файлов, 427 строк
- `fork-linchengming/claudecodeui` [linchengming/claudecodeui](https://github.com/siteboon/claudecodeui/) — балл 73.3, 40 файлов, 2029 строк
- `pr-1446` [fix(claude): keep history after background task notifications](https://github.com/siteboon/claudecodeui/pull1446) — балл 73.2, 2 файлов, 87 строк
- `fork-visionquest-ai/claudecodeui` [visionquest-ai/claudecodeui](https://github.com/siteboon/claudecodeui/) — балл 70.8, 5 файлов, 555 строк
- `pr-1007` [fix(shell): paste through terminal.paste() and stop swallowing native paste](https://github.com/siteboon/claudecodeui/pull1007) — балл 69.4, 2 файлов, 26 строк
- `fork-sermakov/claudecodeui` [sermakov/claudecodeui](https://github.com/siteboon/claudecodeui/) — балл 68.9, 6 файлов, 124 строк
- `pr-1453` [🚨 fix(chat): require server receipt before clearing the first prompt](https://github.com/siteboon/claudecodeui/pull1453) — балл 67.6, 17 файлов, 619 строк
- `pr-1365` [fix(chat): discard stale selection responses after session navigation](https://github.com/siteboon/claudecodeui/pull1365) — балл 61.7, 2 файлов, 156 строк
- `pr-1364` [fix(chat): guard tool lookups against inherited properties](https://github.com/siteboon/claudecodeui/pull1364) — балл 61.3, 4 файлов, 59 строк
- `pr-995` [fix: install browser runtime outside process cwd](https://github.com/siteboon/claudecodeui/pull995) — балл 60.6, 2 файлов, 365 строк
- `pr-1213` [fix(claude): normalize queue-operation remove records as user-role text](https://github.com/siteboon/claudecodeui/pull1213) — балл 59.8, 2 файлов, 116 строк
- `pr-1436` [fix(windows): resolve the claude CLI by walking PATH instead of where.exe](https://github.com/siteboon/claudecodeui/pull1436) — балл 58.9, 2 файлов, 236 строк
- `pr-1457` [fix(workspace): don't strand the composer mid-screen after the keyboard hides](https://github.com/siteboon/claudecodeui/pull1457) — балл 58.0, 1 файлов, 47 строк
- `pr-959` [fix: add Codex provider complete fields](https://github.com/siteboon/claudecodeui/pull959) — балл 55.7, 2 файлов, 21 строк
- `pr-1310` [fix(auth): verify the session once per mount, not once per token refresh](https://github.com/siteboon/claudecodeui/pull1310) — балл 52.6, 2 файлов, 171 строк
- `pr-1111` [fix: correct workspace root containment check for root paths](https://github.com/siteboon/claudecodeui/pull1111) — балл 52.3, 2 файлов, 59 строк
- `pr-1178` [perf(sessions): resolve the session title without holding the transcript](https://github.com/siteboon/claudecodeui/pull1178) — балл 43.0, 3 файлов, 412 строк

  Конфликтные пары внутри расклада: pr-1426×fork-linchengming/claudecodeui, pr-1390×pr-1213, pr-1202×fork-linchengming/claudecodeui, pr-1000×pr-995

## Пары, которые не мержатся вместе

- fork-digitalXperiments/claudecodeui|fork-facdbe-kt/claudecodeui — пересечение 48 файлов, конфликт в: .gitignore, docs/architecture/01-websocket-transport.md, eslint.config.js, package-lock.json, package.json, server/claude-sdk.js, server/cli.js, server/index.js
- fork-digitalXperiments/claudecodeui|fork-ymolic/claudecodeui — пересечение 35 файлов, конфликт в: server/modules/providers/services/session-synchronizer.service.ts, src/components/chat/constants/providerEffort.ts, src/components/mcp/constants.ts, src/components/provider-auth/types.ts, src/components/settings/constants/constants.ts, src/components/settings/view/tabs/agents-settings/AgentListItem.tsx, src/modules/chat/ChatInterface.tsx, src/modules/chat/hooks/useChatComposerState.ts
- fork-bourgois/claudecodeui|fork-digitalXperiments/claudecodeui — пересечение 30 файлов, конфликт в: server/claude-sdk.js, server/index.js, server/modules/database/repositories/sessions.db.ts, server/modules/providers/list/claude/claude-sessions.provider.ts, server/modules/providers/list/codex/codex-runtime.provider.ts, server/modules/providers/services/sessions-watcher.service.ts, server/routes/taskmaster.js, src/components/chat/view/ChatInterface.tsx
- fork-digitalXperiments/claudecodeui|fork-n0rthwood/claudecodeui — пересечение 27 файлов, конфликт в: AGENTS.md, server/claude-sdk.js, server/gemini-cli.js, server/index.js, server/modules/database/repositories/sessions.db.ts, server/modules/providers/list/claude/claude-models.provider.ts, server/modules/providers/list/codex/codex-models.provider.ts, server/modules/providers/list/codex/codex-runtime.provider.ts
- fork-Mwhite84/cloudcli|fork-digitalXperiments/claudecodeui — пересечение 24 файлов, конфликт в: eslint.config.js, server/index.js, server/modules/providers/list/opencode/opencode-models.provider.ts, server/modules/providers/services/sessions.service.ts, server/modules/providers/tests/opencode-models.test.ts, server/modules/websocket/services/chat-websocket.service.ts, server/modules/websocket/services/shell-websocket.service.ts, src/components/app/AppContent.tsx
- fork-digitalXperiments/claudecodeui|fork-vowers/claudecodeui — пересечение 23 файлов, конфликт в: .gitignore, server/claude-sdk.js, server/index.js, server/modules/websocket/index.ts, server/modules/websocket/services/chat-websocket.service.ts, server/modules/websocket/services/shell-websocket.service.ts, src/components/app/AppContent.tsx, src/components/chat/hooks/useChatProviderState.ts
- fork-digitalXperiments/claudecodeui|fork-newrootedgit/claudecodeui — пересечение 21 файлов, конфликт в: .gitignore, docs/architecture/01-websocket-transport.md, eslint.config.js, package-lock.json, package.json, server/claude-sdk.js, server/cli.js, server/index.js
- fork-digitalXperiments/claudecodeui|fork-xingcheng1061/claudecodeui — пересечение 16 файлов, конфликт в: src/modules/chat/hooks/useSlashCommands.ts
- fork-xingcheng1061/claudecodeui|pr-1449 — пересечение 14 файлов, конфликт в: server/modules/providers/list/claude/claude-runtime.provider.js, server/modules/providers/list/claude/claude-sessions.provider.ts, server/modules/websocket/services/chat-websocket.service.ts, server/shared/interfaces.ts, src/modules/chat/ChatInterface.tsx, src/modules/chat/composer/ChatComposer.tsx, src/modules/chat/composer/QueuedMessageCard.tsx, src/modules/chat/hooks/useChatRealtimeHandlers.ts
- fork-xingcheng1061/claudecodeui|pr-1439 — пересечение 10 файлов, конфликт в: src/modules/chat/hooks/useSlashCommands.ts
- fork-digitalXperiments/claudecodeui|pr-1061 — пересечение 10 файлов, конфликт в: .gitignore, docs/architecture/01-websocket-transport.md, eslint.config.js, package-lock.json, package.json, server/claude-sdk.js, server/cli.js, server/index.js
- fork-bourgois/claudecodeui|fork-n0rthwood/claudecodeui — пересечение 10 файлов, конфликт в: server/claude-sdk.js, server/index.js, server/modules/database/repositories/sessions.db.ts, server/modules/providers/list/claude/claude-sessions.provider.ts, server/modules/providers/list/codex/codex-runtime.provider.ts, server/modules/providers/services/sessions-watcher.service.ts, server/routes/taskmaster.js, src/components/chat/view/ChatInterface.tsx
- fork-facdbe-kt/claudecodeui|fork-n0rthwood/claudecodeui — пересечение 10 файлов, конфликт в: AGENTS.md, server/claude-sdk.js, server/gemini-cli.js, server/index.js, server/modules/database/repositories/sessions.db.ts, server/modules/providers/list/claude/claude-models.provider.ts, server/modules/providers/list/codex/codex-models.provider.ts, server/modules/providers/list/codex/codex-runtime.provider.ts
- fork-digitalXperiments/claudecodeui|fork-vaibhav541/claudecodeui — пересечение 10 файлов, конфликт в: package-lock.json, package.json, server/claude-sdk.js, src/components/app/AppContent.tsx, src/components/sidebar/hooks/useSidebarController.ts, src/components/sidebar/utils/utils.ts, src/components/sidebar/view/Sidebar.tsx, src/components/sidebar/view/subcomponents/SidebarProjectList.tsx
- fork-facdbe-kt/claudecodeui|fork-newrootedgit/claudecodeui — пересечение 10 файлов, конфликт в: package-lock.json, package.json, server/database/db.js, server/database/init.sql, server/index.js, server/modules/git/terminal.js, server/routes/auth.js, src/components/app/AppContent.tsx
- fork-Mwhite84/cloudcli|fork-vowers/claudecodeui — пересечение 9 файлов, конфликт в: .gitignore, server/claude-sdk.js, server/index.js, server/modules/websocket/index.ts, server/modules/websocket/services/chat-websocket.service.ts, server/modules/websocket/services/shell-websocket.service.ts, src/components/app/AppContent.tsx, src/components/chat/hooks/useChatProviderState.ts
- fork-newrootedgit/claudecodeui|fork-vowers/claudecodeui — пересечение 9 файлов, конфликт в: .gitignore, server/claude-sdk.js, server/index.js, server/modules/websocket/index.ts, server/modules/websocket/services/chat-websocket.service.ts, server/modules/websocket/services/shell-websocket.service.ts, src/components/app/AppContent.tsx, src/components/chat/hooks/useChatProviderState.ts
- fork-coder8080/claudecodeui|fork-xingcheng1061/claudecodeui — пересечение 9 файлов, конфликт в: server/modules/file-tree/tests/file-tree.service.test.ts
- fork-jothamgoh/cloudcli-patched|fork-xingcheng1061/claudecodeui — пересечение 9 файлов, конфликт в: src/modules/chat/hooks/useSlashCommands.ts
- fork-Mwhite84/cloudcli|fork-facdbe-kt/claudecodeui — пересечение 9 файлов, конфликт в: eslint.config.js, server/index.js, server/modules/providers/list/opencode/opencode-models.provider.ts, server/modules/providers/services/sessions.service.ts, server/modules/providers/tests/opencode-models.test.ts, server/modules/websocket/services/chat-websocket.service.ts, server/modules/websocket/services/shell-websocket.service.ts, src/components/app/AppContent.tsx