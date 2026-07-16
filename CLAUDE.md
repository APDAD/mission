# Mission Control — THE CONSTITUTION
The dashboard for Asher Allen's entire life. Any agent editing this repo obeys this file.

## WHAT THIS IS
One self-contained index.html, PUBLIC repo (APDAD/mission), served at
https://apdad.github.io/mission/. All data lives behind a PIN-gated Supabase Edge Function
("mission" on project nutridyn-combined); the page itself contains ZERO data. NEVER commit
data, balances, doctor names, or money.html (gitignored) to this repo. Verify git status
before every commit. Commit + push after every change; Pages redeploys in ~60s.

## THE API (function v3; code retrievable via Supabase get_edge_function)
Base: $MISSION_API from ~/nutridyn-territory/dashboard-feed/mission.env, header x-pin.
- /api/todos GET/POST/PATCH/:id/DELETE/:id (POST {text, area: nutridyn|spc|money|life,
  source: asher|loop}); DELETE /api/todos clears done
- /api/page/<key> GET/POST (text/html body) - keys: nutridyn, map, money, tomorrow
- /api/dump(s) - legacy brain dumps (UI box removed; API kept)
- PIN auth: SHA-256 in mission_config, 10 fails = 15-min lockout. Never weaken.

## DESIGN LAWS (Asher's explicit words; violating these gets rebuilt)
- Atelier brand only: paper #F1EFE8, card #FBFAF6, ink #2C2C2A, green #1D9E75, gold #EF9F27,
  Cormorant Garamond + Inter. Never dark/generic SaaS. Fun and alive: hover lifts, the
  animated hero gradient, CONFETTI on todo completion (inline canvas, no libraries).
- TODAY tab is the default and the heart: 3 big count tiles, then THE SERPENTINE SNAKE:
  numbered tiles, 3/2/1 columns by viewport, direction alternates per row with gold arrows,
  turn arrow under each row's last tile, numbers always true order. Tiles starting
  "FRIDAY ONLY."/"LATER." render muted.
- ONE ACTION PER TILE, ten-year-old wording, URLs render as green Open buttons. Email tiles
  carry exact draft links in the ACCOUNT-PINNED form
  https://mail.google.com/mail/?authuser=asher@nutri-dyn.com#drafts/<threadId> — never
  /mail/u/0/ (u/0 is his PERSONAL Gmail in Chrome, so u/0 links dump him on the wrong
  account's drafts folder; learned 2026-07-15), never folder links.
- BOARD ORDER: the API returns tiles NEWEST-FIRST and the page renders in API order. To put
  a tile at the END of the snake, create it FIRST; the last tile posted shows first.
- Tab panels fill the viewport (iframes calc(100vh - 150px)). Mobile 375px must stack clean
  with zero horizontal scroll. SPC cannot be iframed (their login blocks it); honest button.
- The page must keep working inside nothing (it IS the top page) and its child iframes get
  <base target="_blank"> injected by loadPage.

## VERIFICATION LAW
No change ships without loading the LIVE site (PIN 116584) in a browser, exercising the
changed behavior (desktop AND 375px mobile), and leaving ZERO test residue (undo any test
todo state via the API). A broken page push blanks his whole dashboard; validate before push.

## WHO FEEDS IT
Loops in ~/.claude/scheduled-tasks/ push pages and tiles (see ~/nutridyn-territory/CLAUDE.md
for the Board Law, Heartbeat Law, and truth hierarchy). The Board Truth Sweep deletes tiles
whose Gmail action provably happened. Day-close (1:45pm) stages tomorrow.
