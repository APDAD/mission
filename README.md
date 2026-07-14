# Mission Control

Asher's private life dashboard: one page, four tabs (To-Do, NutriDyn, Money, SPC),
usable from phone or Mac.

- `index.html` — the whole app. Served by GitHub Pages. Contains no data.
- All data lives behind a PIN-gated Supabase Edge Function (`mission`, project
  `nutridyn-combined`). Tables: `mission_todos`, `mission_pages`, `mission_config`
  (RLS on, service-role only). Wrong-PIN lockout: 10 fails = 15 minutes.
- The NutriDyn tab renders the latest `COMMAND.html` pushed up by the daily
  `nutridyn-command-refresh` loop (`POST /api/page/nutridyn`, `x-pin` header).
- Loops may add machine to-dos: `POST /api/todos` with `{"text","area","source":"loop"}`.
  Keep at most 3 open machine items at once.
