# Mission Control — THE CONSTITUTION
The dashboard for Asher Allen's entire life. Any agent editing this repo obeys this file.

## WHAT THIS IS
One self-contained index.html, PUBLIC repo (APDAD/mission), served at
https://apdad.github.io/mission/. All data lives behind a PIN-gated Supabase Edge Function
("mission" on project nutridyn-combined); the page itself contains ZERO data. NEVER commit
data, balances, doctor names, or money.html (gitignored) to this repo. Verify git status
before every commit. Commit + push after every change; Pages redeploys in ~60s.

## THE ONE-SURFACE LAW (Asher's direct order, 2026-07-22 — the day he found a second to-do
## list hiding on the NutriDyn tab, including a room request that had been blocking his
## August 12 dinner since July 9)
TODAY IS THE ONLY PLACE A TO-DO MAY LIVE. It holds his ENTIRE life: NutriDyn, money, SPC,
family, everything. If he has to do it, it is a tile on TODAY, full stop.
EVERY OTHER TAB IS INSIGHT ONLY. NutriDyn (with the Map folded in as a sub-view), Money, and
SPC exist to show him the picture: numbers, accounts, trends, geography. They may NOT carry
action cards, "moves", "needs", asks, or anything phrased as something for him to do. A loop
that renders an action anywhere but TODAY has hidden it from him, which is worse than not
writing it at all.
BINDING ON EVERY LOOP: if you compute something he must act on, POST IT TO /api/todos. You may
ALSO show its context on a tab, but the tab version is a read-only echo, never the only copy.
nutridyn-command-refresh in particular: its "moves" and "needs" arrays must mirror board tiles,
never replace them, and every move it renders must already exist on TODAY.
NO TILE CAP while this law stands. The old 15-tile ceiling pushed real work onto other
surfaces, which is exactly the failure this law exists to kill. Order does the work the cap
used to do: most urgent and most time-bound at the top of the snake. Overflow to backlog.md
only for things that are genuinely NOT his to do yet.
MAP: not a tab. It lives inside NUTRIDYN as a Territory/Map sub-toggle (shipped 2026-07-22).

## THE DELIVERY LAW (Asher's direct order, 2026-07-22)
"I will rarely look at folders. That's not my flow. I will look at HTML pages, my Mission
Control, and what's on Claude Code. Mission Control is my base and source of truth. That's
where I work from."
A FILE PATH IS NOT A DELIVERABLE. If he has to open Finder, a folder, or a text editor to see
your work, you have not delivered it — you have hidden it. This is the same failure as the
hidden second to-do list, one layer up: the work exists, he just never sees it.
THREE SURFACES, AND ONLY THREE:
  1. MISSION CONTROL — every action lives here as a TODAY tile (see THE ONE-SURFACE LAW).
  2. A LIVE HTML PAGE — anything he needs to LOOK at gets published to the mission repo and
     served from https://apdad.github.io/mission/... , then linked from a tile. Existing
     shelves: /study/ (annotated papers), /blasts/ (email previews), /handouts/ (patient PDFs),
     /sig/ (signature assets). Add a shelf rather than leaving an artifact on disk only.
  3. THE CLAUDE CODE CONVERSATION — what you say to him directly.
WRITE SUMMARIES IN URLS, NOT PATHS. Never end a turn by telling him a thing is "at
blasts/2026-07-22-foo.html". Publish it, then give him the link. Local files under
~/nutridyn-territory are the machine's workspace and the machine's business.
KEEP THE PUBLISHED COPY HONEST. When a page mirrors something that lives elsewhere (a Direct
Mail message, a Gmail draft), generate it FROM that source, not from a parallel file that can
drift, and say on the page which source it came from. A preview that silently disagrees with
what will actually send is worse than no preview.
The public-repo rule still binds absolutely: NO data, balances, doctor names, PHI, or money.
Marketing copy and patient education are fine — he mass-mails them anyway. Check before adding.

## THE ASK LAW (Asher's direct order, 2026-08-04: "every tile and every action item I should
## be able to ask a question... that's where I want to interact")
THE BOARD IS A TWO-WAY SURFACE. Two mechanisms, both riding the existing answers pipeline —
no new API, no new reader:
1. EVERY TILE HAS AN ANSWER BOX, machine tiles and his own alike. Machine tiles say "Answer
   the machine"; his tiles say "Ask the machine about this". Both POST /api/todos/:id/answer,
   the answer-reader loop claims and executes, and the claimed state glows green on ANY tile.
2. THE ASK ROW (gold, under the add row on TODAY): free-form questions. A question becomes a
   ❓-prefixed tile (source asher, area life) whose ANSWER FIELD carries the question verbatim,
   which drops it straight into /api/answers. THE ANSWER FIELD IS AUTHORITATIVE: tile text
   truncates at 500 server-side, the answer does not; the reader reads the answer, never the
   tile text. The reader replies WITH A TILE ON THE BOARD (pre-decided, per THE PRE-DECIDED
   LAW in the territory constitution) and deletes the ❓ tile. Question-tile copy is
   question-shaped ("Your question" label, "Change my question").
NO MODEL PICKER, deliberately: one "machine" identity on the board; model routing stays
machine-side per the tiering laws. Do not add a Fable/Opus dropdown without a new order.
Latency honesty: the board promises "within the half hour"; the reader runs every ~5 minutes
inside the awake window. Never promise chat-speed on the board.

## THE CHAT-EVAPORATES LAW (Asher's direct order 2026-08-18: "there is a lot on my claude
## code and chat... I may leave for days and come back not knowing anything we talked about...
## my source of truth is mission control")
CHAT IS A WORKING SURFACE, NOT A RECORD. He forgets every conversation; the board must not.
Before any substantive session ends its turn:
1. EVERY OPEN QUESTION the machine asked him in chat becomes a machine tile (its "?" puts it
   in the need-your-word strip). An unanswered chat question is a dropped ball by definition.
2. EVERY DECISION-IN-WAITING, promise, or "when you say X I'll do Y" becomes a tile.
3. WHAT CHANGED goes to /api/page/sinceyouleft — a short, newest-first digest in plain
   ten-year-old words. TODAY renders it as "Since you were gone" (hidden when >7 days
   stale). Day-close refreshes it; any session that ships something substantial rewrites it
   the same turn. It is a digest, never a second to-do list: actions still live as tiles.
4. If the full picture lives on another tab or page, TODAY carries a tile or digest line
   POINTING there (his words: "todays page should have a tile telling me to go there").
The test: if he vanished for a week right now and read only TODAY, would he know everything
he needs? If no, the turn is not finished.

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
- TODAY tab is the default and the heart (COUNCIL REBUILD 2026-08-11, 9-agent review, 31/32
  proposals survived adversarial verification): hero (greeting + progress + THE REFRESH),
  3 HONEST counts (in today's run / crushed / need your word — never a scare-count), add+ask
  rows, search, the NEED-YOUR-WORD chip strip, then TODAY'S RUN: the top ~7 tiles by
  client-side score (deadline words, action verbs, NutriDyn revenue weighting per his
  "blowing this out the water" order, legal/deadline overrides) rendered as THE SERPENTINE
  SNAKE (numbered, gold arrows, send-class tiles wear a gold left edge), with RUN IT v2
  (Asher 2026-08-19): the button asks the machine for THE VITAL THREE — it must exhaust
  every machine route over the whole board first, survive an adversarial gauntlet (agent A
  claims "the machine can still do this", agent B attacks A, final conclusion — the law
  lives in mission-answer-reader's SKILL), then post VITAL 1/2/3 tiles: the only gestures
  truly his. VITAL scores +100, the button becomes "Run the vital 3" and walks exactly
  those, one card at a time (Done/Skip). Latency honesty: the pick takes ~15 min via the
  answers pipeline; the button says so and never pretends to be instant. Below the run: THE REST OF THE BOARD, a
  counted, sorted, searchable fold ("N held safe — nothing lost", the NOTHING-IS-THROWN-AWAY
  law in UI form) and the LATER drawer whose tiles auto-wake when a date in their text
  arrives. Long tiles collapse to their first sentence with "the whole story" one tap away —
  loops write headlines that stand alone. THE RUN IS DEALT, NOT REFILLED
  (Asher 2026-08-12: "seven in today's run... it doesn't change... make me feel good"):
  the run is dealt ONCE per day (localStorage, date-keyed ids) and COUNTS DOWN as he kills
  it; the hero bar measures the run, not the ocean, so it can reach full; only a score>=65
  emergency deals itself in late. The countdown talks back ("N down, M to go") with a praise
  ladder that celebrates and never guilts (Rolling / You are cooking / Unstoppable). CRUSHED TODAY IS A NUMBER, NOT A LIST (Asher
  2026-08-19: "I don't need this section"): the strikethrough done-list is gone; the count
  tile, countdown and praise carry the wins, day-close sweeps done rows server-side. THE
  WINS SPARKLINE: 7-day kill history as inline-SVG bars in the hero right rail (real local
  data only, gold = today) — the template for THE VISUAL MANDATE (same day: "graphs and
  charts where you see fit, don't do it just to do it"): pages render inline-SVG Atelier
  charts ONLY over number series their loops already compute; one good chart beats five.
  When
  the DEAL empties: DAY WON end-state ("You crushed all N dealt today"), one confetti per
  day, honest held-safe count — winning the day never requires emptying the ocean.
  THE BRIEF RENDERER (same day, "all that mumble jumbo"): any long tile body renders as
  gold-dot bullets — loops can mark real bullets with "•" or " | "; otherwise sentences
  group into bullets and a CAPS lead-in ("STRICKLAND:") becomes the bullet's bold head.
  URLs are shielded (\x01-fenced) from the sentence splitter so Open buttons never split at
  their dots — caught live 2026-08-12 when com#drafts fragments leaked as text. Note the
  shell caches: a JS change reaches his phone on next app relaunch, not on data refresh. Tiles starting "FRIDAY ONLY."/"LATER."
  render muted inside their drawer. Below the
  snake: THE EMPIRE STRIP (2026-08-03, Asher: "whatever is in SPC, financial, card benefits,
  NutriDyn, the map, radar — it needs to be on TODAY in some way or form; that's my source
  of truth") — six cards (NutriDyn/Radar/Map/Finances/Card benefits/SPC) showing live digest
  lines pulled from each domain's pushed page plus an updated-ago stamp; one tap opens the
  deep view. LOOPS: mark the 2-3 lines worth surfacing with data-digest="..." attributes on
  any element in your pushed page; without them the strip falls back to the page's first
  h1-h3 headings. The strip also exposes feed staleness (an "Updated 20d ago" card is a
  loop bug on display) — never suppress the stamp.
- THE REFRESH SYSTEM (2026-08-03; he saved the site to his iPhone home screen and the only
  way to freshen it was Safari-refresh-and-return): the hero's ↻ button refreshes EVERYTHING
  (todos, tomorrow, empire digests, any open tab iframes) from one tap; the app also
  auto-refreshes when it returns to the foreground (visibilitychange + pageshow, >60s since
  last) and re-pulls todos every ~5 minutes while visible. The "Fresh as of h:mm" stamp under
  the button is the proof. Never remove the auto-refresh paths; they are why the home-screen
  app can be trusted.
- TAB NAMES: the money tab is labeled FINANCES (his rename, 2026-08-03); its internal key,
  area value, and /api/page/money stay 'money' for API compatibility. Sub-tab label
  "Overview". The add-chip reads "Finances".
- ONE ACTION PER TILE, ten-year-old wording, URLs render as green Open buttons. Email tiles
  carry exact draft links in the ACCOUNT-PINNED form
  https://mail.google.com/mail/?authuser=asher@nutri-dyn.com#drafts/<threadId> — never
  /mail/u/0/ (u/0 is his PERSONAL Gmail in Chrome, so u/0 links dump him on the wrong
  account's drafts folder; learned 2026-07-15), never folder links.
- BOARD ORDER: the API returns tiles NEWEST-FIRST and the page renders in API order. To put
  a tile at the END of the snake, create it FIRST; the last tile posted shows first.
- PATCH DOES NOT EDIT TILE TEXT. PATCH /api/todos/<id> with {"text":...} returns HTTP 200 and
  echoes back the row, but the text is UNCHANGED on the server. Only {"done":true|false}
  actually applies. To change wording you MUST DELETE and re-POST (which moves the tile to the
  front of the snake, so re-post the whole affected run in order). This burned twice on
  2026-07-15: once on the Amex tiles, then AGAIN an hour later when three "HOLD, do not send"
  warnings were PATCHed onto bad-citation tiles, returned 200, and never appeared on his board,
  while he was told they had. NEVER report a board change you have not re-read back from
  GET /api/todos. A 200 from this API is not proof.
- TILE LENGTH: the API truncates todo text at 2000 chars (raised from 500 on 2026-08-06,
  Edge Function v5, after the 500 cap chopped a bill-watch tile mid-word on Asher's screen
  and a sweep found four more victims — silently, at exactly 500, no error). Discipline
  unchanged: a tile is ONE ACTION AND A LINK; long detail belongs in a draft or page. After
  posting, re-read and check len(text) — the cap is still silent, just far away now.
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

## KEEP THE PUBLISHED INSTRUCTIONS HONEST TOO (2026-08-10, mission-answer-reader)
A page here does not only MIRROR things, it INSTRUCTS him, and nothing audits those sentences.
peptide-seminar/campaign.html told him to count the room by searching his inbox for "SEAT
REQUEST" — twice, once as a gate on a doctor-facing blast. The register form POSTs to the
Supabase registration list and emails him NOTHING; that subject exists only on the page's mailto
fallback, which no real registrant has ever used. The instruction returned ZERO while two people
were registered. RULE: every imperative sentence on a page here (count / search / check / reply
to) is a detector, and it must be tested against the instrument before it ships and whenever the
page is touched. Naming a channel is a claim. Also: `grep` over raw HTML counterfeits absence
(`&nbsp;` inside a tag hides the phrase) — strip tags and unescape before searching a page.

## A FOLD IS A FILTER, AND A BUTTON BEHIND ONE IS NOT A BUTTON (2026-08-11, mission-answer-reader)
The collapse-to-headline fold shipped the same day it was measured, and on its first audit
**75 of 121 open tiles had their ONLY button inside `.stepmore`, which is `display:none`** until
he taps "the whole story". Every one of those tiles read as compliant with THE PRE-DECIDED LAW —
the link was in the text, the deep link was live, the sweeps that regex tile text all passed —
and the gesture he actually has to make was one tap out of sight. A renderer silently bounds what
a tile can ASK FOR, and no check that reads tile TEXT can see that boundary.
FIXED: `stepCard` hoists the first link of any scheme (`https?:`, `sms:`, `tel:`) up into the
headline. THE RULE: any change to how a tile renders must be re-checked against the question "can
he still reach the one gesture without opening anything", measured on the live board, not reasoned
about. Count buttons that have a non-zero bounding box, never buttons that exist in the DOM.
SMS AND TEL ARE FIRST-CLASS (his order, 2026-08-11: "cant you add this to his text and just have
it there for me to press send?"). An `sms:+1NUMBER&body=<urlencoded>` link opens Messages with the
whole message already typed, so the only gesture left is Send — which is the press-send button he
asked for WITHOUT the machine ever typing into a text thread. Render it with NO `target=_blank`
(iOS needs the same-tab hand-off) and label it Text; `tel:` labels Call.

- A PROXY REPRODUCES THE MEASUREMENT AND DELETES THE QUESTION — AND THE SECOND BROWSER SURFACE WAS
  NEVER TESTED (added 2026-08-11 by mission-answer-reader, empty queue, finishing the check the
  15:45 fire honestly said it could not finish). That fire shipped the button hoist, found that
  claude-in-chrome's `resize_window` REPORTS SUCCESS AND DOES NOT MOVE THE VIEWPORT (innerWidth
  stayed 1501 at two widths, a real control), correctly refused to claim a phone pass, and fell back
  to a labelled proxy: 390px CARD WIDTH on a desktop viewport. It reported 4 buttons, none zero-box,
  0px overflow. All true, and it missed the defect entirely.
  THIS SESSION HAS A SECOND BROWSER. `mcp__Claude_Browser__resize_window preset:mobile` really
  emulates: verified 375x812, Android UA, maxTouchPoints 5, `(pointer:coarse)` TRUE and
  `(pointer:fine)` FALSE. One tool was blind and the other was not, and no run had enumerated the
  surfaces before pleading the limit. FOUR NEGATIVE READERS IS NOT AN EXHAUSTED INVENTORY, applied
  to TOOL SURFACES rather than to mail channels or python packages — third shape, same law.
  WHAT THE PROXY COULD NOT SEE, and this is the part that generalizes. At 375px real, every hoisted
  headline button measured 45x21 and the .hint links 16px tall, against a 44px minimum. The proxy
  measured THE SAME PIXELS — 45x21 is 45x21 at any window size — so it was not that the proxy got a
  wrong number. IT GOT THE RIGHT NUMBER AND NOBODY ASKED WHETHER IT WAS A THUMB TARGET, because on a
  desktop viewport a mouse hits 21px perfectly and the question never forms. A PROXY DOES NOT WEAKEN
  A CHECK, IT NARROWS THE QUESTION SET, silently, and the checks that survive all pass — which is
  why the proxy run reported clean. Sibling of A DETECTOR THAT CANNOT FIRE (there the sensor is dead,
  here the sensor is fine and the QUESTION is missing) and of A LIVE BUTTON IS NOT A CORRECT BUTTON
  (liveness, aim, and now ERGONOMICS are three different properties of one anchor).
  THE COST WAS THE WHOLE POINT OF THE FEATURE: the hoist put a button on 76 tiles that morning
  precisely so THE PRE-DECIDED LAW's one irreducible gesture would always be reachable, and that
  gesture was 21px tall on the phone he reads the board from. The machine did everything on both
  sides of the click and then made the click hard.
  THE RULE: (1) before pleading that a viewport, a device or a rendering cannot be checked, enumerate
  the browser surfaces this session actually has and try each — name them out loud, per "any inbox I
  can read" is an inventory claim; (2) a proxy measurement may never close a check whose subject is
  the real device — say what the proxy cannot ask, not just what it could not measure; (3) verify any
  responsive fix with a control that MUST disagree (here 1280px/pointer:fine still renders 45x21 and
  16px, proving the rule is scoped and his Mac is untouched — a mobile-only pass would have proven
  only that CSS loaded).
  MECHANIC, verified live: an inline `cssText` beats every stylesheet rule, so the phone fix was
  literally unreachable while linkBtn styled itself inline; moving it to a `.gobtn` class was the
  precondition for the media query. `display:inline-flex;align-items:center;min-height:44px` gives a
  full 44px target while staying in the text flow, which padding alone cannot do at 12px.
