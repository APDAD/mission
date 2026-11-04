#!/usr/bin/env python3
"""Build the NutriDyn condition-sheet shelf in two editions.

  python3 build.py                         # all sheets, HTML only
  python3 build.py --pdf                   # + PDFs, previews, thumbnails, bundles
  python3 build.py --only gerd,ibd --pdf   # just those sheets (previews for checking)

Editions: practitioner (Provider check, for MDs, DCs, NDs) and pharmacy
(Pharmacist check, for compounding pharmacies).  Output:
  handouts/conditions/<edition>/<slug>.html|.pdf, <edition>/all-condition-sheets.pdf
  handouts/conditions/img/ (shared product photos + thumbnails), index.html
Previews for checking go to $SHEETS_TMP/preview/<edition>/<slug>-<page>.png.
Never hand-edit generated HTML: edit build/conditions/<slug>.py and rebuild.
"""
import json
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
OUT = os.path.dirname(HERE)

import kit  # noqa: E402
from kit import E, icon, logo, theme_vars  # noqa: E402
import products  # noqa: E402
import sheets as legacy_sheets  # noqa: E402
import conditions  # noqa: E402

EDITIONS = {
    "practitioner": {"label": "Practitioner edition", "short": "Practitioners", "rx_title": "Provider check",
                     "who": "your provider", "Who": "Your provider", "for": "MDs, DCs, NDs and their teams"},
    "pharmacy": {"label": "Pharmacy edition", "short": "Pharmacies", "rx_title": "Pharmacist check",
                 "who": "your pharmacist", "Who": "Your pharmacist", "for": "compounding and retail pharmacies"},
}

# 21 CFR 101.93: the exact notice (plural form allowed), in bold type, set off in a hairline box, linked to
# every structure/function statement by the same symbol. The "works alongside your care" line moved out:
# extra words inside the box are not part of the notice, and each check panel already says it.
DISCLAIMER = (f"<span class='mark'>{kit.DIAMOND}</span> These statements have not been evaluated by the Food and Drug "
              "Administration. These products are not intended to diagnose, treat, cure, or prevent any disease.")

BACK_CSS = r"""
.col{position:relative}
.panel.rx h3{display:flex;justify-content:space-between;align-items:baseline;gap:8px;flex-wrap:nowrap;white-space:nowrap}
.panel.rx h3 .rxkeep{font:700 7pt Inter,sans-serif;letter-spacing:0;text-transform:none;color:var(--deep);white-space:nowrap}
.col.st{border-color:#F15F3F;box-shadow:0 0 0 1px #F15F3F,0 2px 6px rgba(20,30,40,.10)}
.startb{position:absolute;top:-8px;right:6px;z-index:3;background:#F15F3F;color:#fff;font:800 7pt/1 Inter,sans-serif;
  letter-spacing:.08em;padding:3px 6px 2px;border-radius:3px;text-transform:uppercase;box-shadow:0 0 0 1.5px #fff;white-space:nowrap}
.lifes.c3{grid-template-columns:repeat(3,1fr);gap:0.18in}
.lifes.c4{grid-template-columns:repeat(4,1fr)}
.lifes.c5{grid-template-columns:repeat(5,1fr)}
.lifes.c6{grid-template-columns:repeat(6,1fr)}
.life.l3{align-items:stretch;text-align:left;flex-direction:row;gap:10px}
.life.l3 .disc2{flex:none;width:0.8in;height:0.8in}
.life.l3 ul{margin:2px 0 0;padding-left:13px;font-size:7.8pt;line-height:1.32;color:#F5F7F8}
.life.l3 b{margin-top:0}
.icons5 .life .disc2{background:transparent;box-shadow:none;color:#FFD9BF}
.icons5 .life .disc2 svg{width:0.6in!important;height:0.6in!important}
a.plink{color:inherit;text-decoration:none;display:flex;flex-direction:column;align-items:center}
a.plink:hover .nm{text-decoration:underline}
.keyrow{display:flex;flex-wrap:wrap;gap:4px 14px;align-items:center;font-size:7.8pt;color:#2B3236;margin:4px 0 0}
.keyrow b{font:800 7pt Inter,sans-serif;letter-spacing:.12em;color:var(--deep)}
.keyrow span{display:inline-flex;align-items:center;gap:5px}
.keyrow i{display:inline-block;width:11px;height:11px;border-radius:50%}
"""


def ed_text(x, ed):
    return x.replace("{who}", ed["who"]).replace("{Who}", ed["Who"]) if isinstance(x, str) else x


def life_block(b):
    style, items = b["style"], b["life"]
    if style == "checks":
        cells = "".join(
            f'<div class="chk"><span class="bx"></span><div><b>{a}</b><ul>{"".join(f"<li>{x}</li>" for x in xs)}</ul></div></div>'
            for a, xs in items)
        return f'<div class="checks">{cells}</div>'
    if style == "circle3":
        cells = "".join(
            f'<div class="life l3"><div class="disc2">{icon(ic, "0.5in")}</div><div><b>{a}</b><ul>{"".join(f"<li>{x}</li>" for x in xs)}</ul></div></div>'
            for ic, a, xs in items)
        return f'<div class="lifes c3">{cells}</div>'
    cls = "hex" if style == "hex" else ""
    cells = "".join(f'<div class="life {cls}"><div class="disc2">{icon(ic, "0.5in")}</div><b>{a}</b><p>{p}</p></div>'
                    for ic, a, p in items)
    extra = " icons5" if style == "icons" else ""
    return f'<div class="lifes c{len(items)}{extra}">{cells}</div>'


SF_VERB = re.compile(r"(supports?|helps?|promotes?|maintains?|aids?|encourages?|nourishes?|contributes?|provides?|"
                     r"fuels?|feeds?|protects?|balances?|calms?|soothes?|builds?|strengthens?)\b", re.I)


def col_block(c):
    p = products.get(c["p"])
    dose, dosesub = c.get("dose"), c.get("dosesub")
    if dose in (None, "dose_from_db"):
        dose, dosesub = p["dose"], p.get("dosesub", "")
    bullets = list(c["bullets"])
    # Tie the column's structure/function statements to the FDA disclaimer in the footer with the
    # same drawn diamond, unless the sheet already marks them itself. The mark goes on each bullet
    # that makes a claim (starts with an S/F verb); if none does, on the first bullet.
    if bullets and not any(m in "".join(bullets) for m in ('class="mark"', "class='mark'", "-dia", kit.DIAMOND)):
        mark = f'&nbsp;<span class="mark">{kit.DIAMOND}</span>'
        claim = [i for i, b in enumerate(bullets) if SF_VERB.match(re.sub(r"<[^>]+>", "", b).strip())]
        for i in claim or [0]:
            bullets[i] = bullets[i] + mark
    lis = "".join(f"<li>{x}</li>" for x in bullets)
    # The badge straddles the column's top edge (half above it), so it never covers the title or the photo.
    start = '<span class="startb">Start here</span>' if c.get("start") else ""
    href = E(p["href"])
    return (f'<div class="col{" st" if c.get("start") else ""}">{start}<div class="need"><b>{c["need"]}</b><i>{c["needsub"]}</i></div>'
            f'<div class="pick"><a class="plink" href="{href}"><img src="{p["img"]}" alt="NutriDyn {E(p["name"])} bottle">'
            f'<div class="nm">{p["name"]}</div></a><div class="sz">{p["size"]}</div></div>'
            f'<div class="what"><ul>{lis}</ul><div class="key"><b>In each serving</b><br>{p["key"]}</div></div>'
            f'<div class="dose">{dose}<small>{dosesub or ""}</small></div></div>')


SLOTS = [("am", "Morning", "sun"), ("pm", "Evening meal", "plate"), ("bed", "Bedtime", "moon")]


def rhythm_block(cols, note=None, ed=None):
    """The three-slot daily schedule plus one plan line. A sheet whose products are alternatives (swap, never
    stack) can replace the default plan line with back["rhythm_note"]; "{plan}" becomes the pill/scoop total
    and the {who}/{Who} tokens are filled per edition."""
    by = {"am": [], "pm": [], "bed": []}
    pills = scoops = droppers = 0
    for c in cols:
        p = products.get(c["p"])
        for slot, n, unit in c.get("sched", p["sched"]):
            by[slot].append(f'{p["name"]} <em>{n}&nbsp;{unit}</em>')
            if unit.startswith("scoop"):
                scoops += n
            elif unit.startswith("dropper"):
                droppers += n
            elif not unit.startswith("serving"):
                pills += n
    cells = ""
    for key, label, ic in SLOTS:
        lis = "".join(f"<li>{x}</li>" for x in by[key]) or "<li><em>nothing to take</em></li>"
        cells += f'<div class="slot"><div class="when">{icon(ic, "13px", sw=4)}{label}</div><ul>{lis}</ul></div>'
    parts = []
    if pills:
        parts.append(f"{pills} pill{'s' if pills != 1 else ''}")
    if scoops:
        parts.append(f"{scoops} scoop{'s' if scoops != 1 else ''}")
    if droppers:
        parts.append(f"{droppers} dropper{'s' if droppers != 1 else ''}")
    joined = ", ".join(parts[:-1]) + (" and " if len(parts) > 1 else "") + parts[-1] if parts else "nothing"
    if note:
        text = note.replace("{plan}", joined)
        total = f'<div class="total">{ed_text(text, ed) if ed else text}</div>'
    else:
        total = (f'<div class="total">The full plan is <b>{joined} a day</b>. Overwhelmed? Start with the '
                 f'<b>Start here</b> pick, then add one product a week.</div>')
    return f'<div class="rhythm">{cells}</div>{total}'


def front_page(s, ed):
    t = kit.THEMES[s["theme"]]
    sub = f'<br><small>{s["sub"]}</small>' if s.get("sub") else ""
    intro = f'<p class="intro">{ed_text(s["intro"], ed)}</p>' if s.get("intro") else ""
    try:
        body = s["front"](t, ed)
    except TypeError:
        body = s["front"](t)
    return (f'<section class="sheet front" style="{theme_vars(s["theme"])}"><div class="rule-top"></div><div class="inner">'
            f'<div class="headrow">{logo("0.27in")}<span class="series">{s["series"]}</span></div>'
            '<div class="fields"><span>Patient name</span><span class="box"></span><span>Date</span><span class="box"></span></div>'
            f'<h1 class="title">{s["title"]}{sub}</h1>{intro}{ed_text(body, ed)}'
            f'<div class="foot"><span>NutriDyn &middot; Practitioner Exclusive &middot; nutridyn.com</span>'
            f'<span class="code">{s["code"]} &middot; Page 1 of 2</span></div></div><div class="rule-bot"></div></section>')


def back_page(s, ed, edkey):
    b = s["back"]
    sub = f'<small>{b["life_sub"]}</small>' if b.get("life_sub") else ""
    cols = "".join(col_block(c) for c in b["cols"])
    rx = b["rx"].get(edkey, b["rx"].get("all", [])) if isinstance(b["rx"], dict) else b["rx"]
    rx = "".join(f"<li>{ed_text(x, ed)}</li>" for x in rx)
    lines = '<div class="ln"></div>' * 3
    return (f'<section class="sheet back" style="{theme_vars(s["theme"])}"><div class="inner" style="top:0">'
            f'<div class="band" style="padding-top:0.3in"><h2>{b["life_title"]}{sub}</h2>{life_block(b)}</div>'
            '<div class="ns-title">Nutrient Solutions<span>What your body needs, and the NutriDyn formula that delivers it</span></div>'
            f'<div class="cols" style="grid-template-columns:repeat({len(b["cols"])},1fr)">{cols}</div>'
            f'<div class="duo"><div class="panel"><h3>Your daily rhythm</h3>{rhythm_block(b["cols"], b.get("rhythm_note"), ed)}</div>'
            f'<div class="panel rx"><h3>{ed["rx_title"]}<span class="rxkeep">Keep taking your medicines.</span></h3><ul>{rx}</ul></div></div>'
            f'<div class="notes"><b>Special considerations for you:</b>{lines}</div>'
            '<div class="recby"><span>Recommended by</span><span class="ln2" data-for></span><span>Phone</span>'
            '<span class="ln2" style="flex:0 0 1.5in"></span></div>'
            f'<div class="foot"><div class="disc">{DISCLAIMER}</div><div style="display:flex;flex-direction:column;align-items:flex-end;gap:4px">'
            f'{logo("0.22in")}<span class="code">{s["code"]} &middot; Page 2 of 2 &middot; {ed["label"]} &middot; 11/2026</span></div></div>'
            '</div><div class="rule-bot"></div></section>')


def sheet_body(s, edkey):
    ed = EDITIONS[edkey]
    return front_page(s, ed) + back_page(s, ed, edkey)


def css_all(sheets):
    return legacy_sheets.EXTRA_CSS + BACK_CSS + "".join(s.get("css", "") for s in sheets)


def sheet_html(s, edkey, sheets):
    ed = EDITIONS[edkey]
    tb = kit.toolbar(f'{s["title"]} · {ed["label"]}', f'{s["slug"]}.pdf', "../index.html")
    return kit.page_shell(f'{s["title"]} · NutriDyn', tb + f'<div class="stack">{sheet_body(s, edkey)}</div>',
                          s["theme"], css_all(sheets))


INDEX_CSS = r"""
body{background:#F1EFE8}
.wrap{max-width:1180px;margin:0 auto;padding:22px 16px 60px}
.hero{background:#14664D;color:#fff;border-radius:14px;padding:22px 22px 20px;display:grid;gap:10px}
.hero .k{font:800 12px Inter;letter-spacing:.18em;text-transform:uppercase;color:#BFE3D4}
.hero h1{font:900 clamp(26px,5vw,40px)/1.1 Merriweather,Georgia,serif;margin:0}
.hero p{margin:0;font-size:15px;line-height:1.5;color:#E5F2EC;max-width:70ch}
.seg{display:inline-flex;background:#0F5440;border-radius:99px;padding:4px;gap:4px;flex-wrap:wrap;justify-self:start}
.seg button{min-height:44px;padding:0 18px;border-radius:99px;border:0;background:transparent;color:#DDEFE7;font:700 14px Inter;cursor:pointer}
.seg button[aria-pressed=true]{background:#fff;color:#14664D}
.bar{display:flex;flex-wrap:wrap;gap:10px;align-items:center;background:#FBFAF6;border-radius:10px;padding:12px 14px;margin:16px 0}
.bar label{font:700 13px Inter;color:#2C2C2A}
.bar input{flex:1 1 220px;min-width:0;min-height:44px;border:1px solid #CFC9BC;border-radius:8px;padding:0 12px;font:15px Inter}
.btn{display:inline-flex;align-items:center;justify-content:center;min-height:44px;padding:0 16px;border-radius:99px;background:#14664D;
  color:#fff;text-decoration:none;font:700 14px Inter;white-space:nowrap}
.btn.g{background:transparent;color:#14664D;border:1.5px solid #14664D}
.btn.c{background:#F15F3F}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(250px,1fr));gap:16px}
.card{background:#FBFAF6;border-radius:12px;overflow:hidden;display:flex;flex-direction:column;box-shadow:0 1px 0 #E2DED4;transition:transform .15s ease}
.card:hover{transform:translateY(-3px)}
.card .th{display:grid;grid-template-columns:1fr 1fr;gap:2px;background:#E2DED4}
.card .th img{width:100%;height:auto;display:block}
.card .bd{padding:12px 14px 14px;display:flex;flex-direction:column;gap:8px;flex:1}
.card h2{font:900 18px/1.2 Merriweather,Georgia,serif;margin:0;color:#2C2C2A}
.card .fam{font:800 11px Inter;letter-spacing:.14em;text-transform:uppercase}
.card .pp{font-size:13px;color:#5B5B55;line-height:1.4;margin:0}
.card .row{display:flex;gap:8px;flex-wrap:wrap;margin-top:auto}
.how{background:#FBFAF6;border-radius:12px;padding:16px 18px;margin-top:18px}
.how h3{font:900 18px Merriweather,Georgia,serif;margin:0 0 6px;color:#14664D}
.how ol{margin:0;padding-left:20px;font-size:14px;line-height:1.55}
.src{font-size:12px;color:#6B6B66;margin-top:18px;line-height:1.5}
.stats{display:grid;grid-template-columns:repeat(auto-fit,minmax(130px,1fr));gap:10px;margin-top:4px}
.st{background:#F1EFE8;color:#2C2C2A;border-radius:10px;padding:10px 12px;display:flex;flex-direction:column;gap:2px}
.st b{font:900 30px/1 Merriweather,Georgia,serif;color:#14664D}
.st span{font:700 11px Inter;letter-spacing:.12em;text-transform:uppercase;color:#5B5B55}
.chips{display:flex;flex-wrap:wrap;gap:8px;margin:4px 0 0}
.chip{display:inline-flex;align-items:center;gap:6px;min-height:44px;padding:0 14px;border-radius:99px;background:#FBFAF6;color:#2C2C2A;
  text-decoration:none;font:700 13px Inter;box-shadow:0 1px 0 #E2DED4}
.chip i{font-style:normal;background:#14664D;color:#fff;border-radius:99px;padding:1px 7px;font-size:12px}
.edbar{justify-content:space-between}
.edbar div{display:flex;flex-direction:column;gap:2px}
.edbar b{font:800 14px Inter;color:#2C2C2A}
.edbar span{font-size:13px;color:#5B5B55}
.grp{margin:22px 0 0}
.grp h2{display:flex;align-items:center;gap:10px;font:900 22px/1.2 Merriweather,Georgia,serif;color:#2C2C2A;margin:0 0 10px}
.grp h2 small{font:700 12px Inter;letter-spacing:.1em;text-transform:uppercase;color:#6B6B66}
.grp .dot{width:14px;height:14px;border-radius:50%;background:var(--fc);flex:none}
.card{border-top:4px solid var(--fc)}
.card h3{font:900 18px/1.2 Merriweather,Georgia,serif;margin:0;color:#2C2C2A}
.card .fam{color:var(--fc)}
.steps{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:12px;margin-top:8px}
.step{background:#fff;border-radius:10px;border-left:5px solid #1D9E75;padding:12px 14px;display:grid;grid-template-columns:auto 1fr;gap:10px;align-items:start}
.step .n{font:900 24px/1 Merriweather,Georgia,serif;color:#1D9E75}
.step b{display:block;font:800 14px Inter;color:#2C2C2A;margin-bottom:2px}
.step p{margin:0;font-size:13.5px;line-height:1.45;color:#4A4A45}
@media (max-width:600px){.chips{flex-wrap:nowrap;overflow-x:auto;scrollbar-width:none;-webkit-overflow-scrolling:touch;padding-bottom:2px}.chips::-webkit-scrollbar{display:none}.chip{flex:none}}
@media (max-width:420px){.st b{font-size:24px}.grp h2{font-size:19px}.seg{display:grid;grid-template-columns:1fr 1fr;justify-self:stretch}.seg button{padding:0 8px}.seg .xl{display:none}.edbar .btn{width:100%}}
"""

SERIES_ORDER = ["Gut Health Series", "Metabolic Health Series", "Immune Health Series", "Hormone Health Series",
                "Pain and Movement Series", "Brain and Nerve Series", "Energy and Stress Series"]


def index_html(sheets):
    by_series = {}
    for s in sheets:
        by_series.setdefault(s.get("series") or "More sheets", []).append(s)
    order = [x for x in SERIES_ORDER if x in by_series] + [x for x in by_series if x not in SERIES_ORDER]
    n_products = len({products.get(c["p"])["name"] for s in sheets for c in s["back"]["cols"]})
    stats = "".join(f'<div class="st"><b>{v}</b><span>{k}</span></div>' for v, k in (
        (len(sheets), "two-sided sheets"), (len(order), "series"), (n_products, "NutriDyn products"), (2, "editions")))
    jump = "".join(f'<a class="chip" href="#practitioner-{i}" data-i="{i}">{E(name.replace(" Series", ""))} <i>{len(by_series[name])}</i></a>'
                   for i, name in enumerate(order))
    secs = ""
    for edkey, ed in EDITIONS.items():
        groups = ""
        for i, name in enumerate(order):
            cards = ""
            for s in by_series[name]:
                c1 = kit.THEMES.get(s["theme"], kit.THEMES["gut"])["c1"]
                names = ", ".join(products.get(x["p"])["name"] for x in s["back"]["cols"])
                cards += (f'<article class="card" style="--fc:{c1}"><a class="th" href="{edkey}/{s["slug"]}.html">'
                          f'<img src="img/thumb-{edkey}-{s["slug"]}-1.jpg" alt="Front of the {E(s["title"])} sheet" loading="lazy">'
                          f'<img src="img/thumb-{edkey}-{s["slug"]}-2.jpg" alt="Back of the {E(s["title"])} sheet" loading="lazy"></a>'
                          f'<div class="bd"><span class="fam">{s["code"]}</span><h3>{s["title"]}</h3>'
                          f'<p class="pp"><b>{len(s["back"]["cols"])} NutriDyn picks:</b> {E(names)}.</p>'
                          f'<div class="row"><a class="btn" data-k href="{edkey}/{s["slug"]}.html">Open</a>'
                          f'<a class="btn g" href="{edkey}/{s["slug"]}.pdf">PDF</a></div></div></article>')
            c1 = kit.THEMES.get(by_series[name][0]["theme"], kit.THEMES["gut"])["c1"]
            groups += (f'<div class="grp" id="{edkey}-{i}" style="--fc:{c1}"><h2><span class="dot"></span>{E(name)}'
                       f'<small>{len(by_series[name])} sheet{"s" if len(by_series[name]) != 1 else ""}</small></h2>'
                       f'<div class="grid">{cards}</div></div>')
        secs += (f'<section data-ed="{edkey}"{" hidden" if edkey != "practitioner" else ""}><div class="bar edbar">'
                 f'<div><b>{ed["label"]}</b><span>for {ed["for"]}. The back page says &ldquo;{ed["rx_title"]}&rdquo;.</span></div>'
                 f'<a class="btn c" href="{edkey}/all-condition-sheets.pdf">All {len(sheets)} sheets, one PDF</a></div>{groups}</section>')
    steps = [("Pick the sheet", "Match it to the conversation. Write the patient's name and the date at the top."),
             ("Tick and circle", "On the back, tick the lifestyle steps that apply and circle the products you recommend."),
             ("Make it theirs", "Write the dose and anything specific under <i>Special considerations</i>. The <b>Start here</b> pick is the one to begin with."),
             ("Send them to the bottle", "Product photos and names link to the product page in the web and PDF versions.")]
    how = "".join(f'<div class="step"><span class="n">{i + 1}</span><div><b>{a}</b><p>{b}</p></div></div>' for i, (a, b) in enumerate(steps))
    body = f"""<div class="wrap">
<div class="hero"><span class="k">NutriDyn &middot; Patient education &middot; November 2026</span>
<h1>Condition sheets</h1>
<p>Front: the condition as a picture, with a key. Back: lifestyle steps, the NutriDyn products for each nutrient, a daily
schedule and a medicine check. Print double-sided, flip on the long edge.</p>
<div class="stats">{stats}</div>
<div class="seg" role="group" aria-label="Edition"><button id="ed-practitioner" aria-pressed="true" data-ed="practitioner">Practitioner<span class="xl"> edition</span></button>
<button id="ed-pharmacy" aria-pressed="false" data-ed="pharmacy">Pharmacy<span class="xl"> edition</span></button></div></div>
<div class="chips" aria-label="Jump to a series">{jump}</div>
<div class="bar"><label for="pr">Practice name for the "Recommended by" line</label>
<input id="pr" placeholder="e.g. your clinic or pharmacy name" autocomplete="organization">
<a class="btn g" href="warehouse-bottle-counter-card.html">Warehouse-bottle counter card</a></div>
{secs}
<div class="how"><h3>How to use them</h3><div class="steps">{how}</div></div>
<p class="src">Built from NutriDyn label facts and NutriDyn protocols. Condition facts from the CDC, WHO, FDA, AASLD, ACG and
AHA/ACC. Every product statement is structure/function and carries the FDA disclaimer. Generated by
handouts/conditions/build/build.py; do not hand-edit.</p></div>
<script>(function(){{var k='mc_sheet_practice',e='mc_sheet_edition',i=document.getElementById('pr');
function show(ed){{document.querySelectorAll('section[data-ed]').forEach(function(s){{s.hidden=s.getAttribute('data-ed')!==ed;}});
document.querySelectorAll('.seg button').forEach(function(b){{b.setAttribute('aria-pressed',b.getAttribute('data-ed')===ed);}});
document.querySelectorAll('.chip[data-i]').forEach(function(c){{c.setAttribute('href','#'+ed+'-'+c.getAttribute('data-i'));}});
try{{localStorage.setItem(e,ed)}}catch(x){{}}}}
document.querySelectorAll('.seg button').forEach(function(b){{b.addEventListener('click',function(){{show(b.getAttribute('data-ed'));}});}});
function upd(){{var v=i.value.trim();document.querySelectorAll('a[data-k]').forEach(function(a){{var b=a.getAttribute('href').split('?')[0];
a.setAttribute('href',v?b+'?for='+encodeURIComponent(v):b);}});try{{localStorage.setItem(k,v)}}catch(x){{}}}}
try{{i.value=localStorage.getItem(k)||'';show(localStorage.getItem(e)||'practitioner')}}catch(x){{}}i.addEventListener('input',upd);upd();}})();</script>"""
    return kit.page_shell("Condition Sheets · NutriDyn", body, "gut", INDEX_CSS, font_base="fonts/")


def main():
    args = sys.argv[1:]
    pdf = "--pdf" in args
    only = None
    if "--only" in args:
        only = set(args[args.index("--only") + 1].split(","))
    tmp = os.environ.get("SHEETS_TMP", os.path.join(HERE, "_tmp"))
    os.makedirs(os.path.join(OUT, "img"), exist_ok=True)
    report = {}
    products.stage_images(os.path.join(OUT, "img"), report)
    strict = {x.replace("-", "_") for x in only} if only else ()
    sheets = conditions.load(strict=strict)
    todo = [s for s in sheets if not only or s["slug"] in only]
    if only and not todo:
        sys.exit(f"no sheet matches {sorted(only)}")
    used = sorted({c["p"] for s in todo for c in s["back"]["cols"]})
    missing = products.check_complete(used)
    if missing:
        print("PLACEHOLDER PRODUCTS STILL IN USE:", missing)
    low = [(k, report.get(k, (0, None))[0]) for k in used if report.get(k, (0, None))[0] < products.MIN_PRINT_PX]
    if low:
        print("LOW-RES PRODUCT PHOTOS (<%dpx tall, under 300 ppi at the 0.98 in print size):" % products.MIN_PRINT_PX, ", ".join(f"{k} {h}px" for k, h in low))
    soft = [k for k in used if products.P.get(k, {}).get("img_soft")]
    if soft:
        print("SOFT PRODUCT PHOTOS (enlarged from 160px thumbnails; need the print master):", ", ".join(soft))
    job = {"items": [], "bundles": []}
    for edkey in EDITIONS:
        d = os.path.join(OUT, edkey)
        os.makedirs(d, exist_ok=True)
        for s in todo:
            f = os.path.join(d, f'{s["slug"]}.html')
            open(f, "w").write(sheet_html(s, edkey, sheets))
            job["items"].append({"html": f, "pdf": os.path.join(d, f'{s["slug"]}.pdf'),
                                 "preview": os.path.join(tmp, "preview", edkey, s["slug"]),
                                 "thumb": os.path.join(OUT, "img", f'thumb-{edkey}-{s["slug"]}')})
        if not only:
            body = "".join(sheet_body(s, edkey) for s in sheets)
            bf = os.path.join(d, "_bundle.html")
            open(bf, "w").write(kit.page_shell("All condition sheets", f'<div class="stack">{body}</div>', "gut", css_all(sheets)))
            job["bundles"].append({"html": bf, "pdf": os.path.join(d, "all-condition-sheets.pdf")})
    if not only:
        open(os.path.join(OUT, "index.html"), "w").write(index_html(sheets))
        # A full build knows every sheet, so it can drop product photos no sheet uses any more.
        keep = {os.path.basename(products.get(c["p"])["img"]) for s in sheets for c in s["back"]["cols"]}
        keep.add("nd-missing.png")
        for f in sorted(os.listdir(os.path.join(OUT, "img"))):
            if f.startswith("nd-") and f.endswith(".png") and f not in keep:
                os.remove(os.path.join(OUT, "img", f))
                print("removed unused photo", f)
    if pdf:
        os.makedirs(tmp, exist_ok=True)
        jf = os.path.join(tmp, f"render-job-{os.getpid()}.json")
        json.dump(job, open(jf, "w"))
        subprocess.run(["node", os.path.join(HERE, "render.js"), jf], check=True)
        type3 = []
        for it in job["items"] + job["bundles"]:
            try:
                fonts = subprocess.run(["pdffonts", it["pdf"]], capture_output=True, text=True, timeout=60).stdout
            except (OSError, subprocess.SubprocessError):
                break
            if "Type 3" in fonts:
                type3.append(os.path.relpath(it["pdf"], OUT))
        if type3:
            print("TYPE 3 FONTS (a character outside the Latin set fell back to a glyph print shops reject; "
                  "draw symbols as inline SVG, e.g. kit.DIAMOND):", ", ".join(type3))
    for b in job["bundles"]:
        if os.path.exists(b["html"]):
            os.remove(b["html"])
    print("built", len(todo), "sheets x", len(EDITIONS), "editions")


if __name__ == "__main__":
    main()
