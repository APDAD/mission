#!/usr/bin/env python3
"""Build the NutriDyn condition-sheet shelf.

  python3 handouts/conditions/build/build.py          # HTML only
  python3 handouts/conditions/build/build.py --pdf    # + PDFs, previews (Playwright)

Writes handouts/conditions/<slug>.html, <slug>.pdf, all-condition-sheets.pdf,
index.html and img/thumb-*.jpg.  Never hand-edit the generated HTML.
"""
import html
import json
import os
import re
import shutil
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
OUT = os.path.dirname(HERE)
REPO = os.path.dirname(os.path.dirname(OUT))

import kit  # noqa: E402
from kit import E, icon, logo, theme_vars  # noqa: E402
import products  # noqa: E402
import sheets  # noqa: E402

DISCLAIMER = ("<span class='mark'>&#9670;</span> These statements have not been evaluated by the Food and Drug "
              "Administration. These products are not intended to diagnose, treat, cure, or prevent any disease. "
              "Nutrient support works alongside, never instead of, the care and medicines your practitioner prescribes.")

BACK_CSS = r"""
.col{position:relative}
.startt{position:absolute;top:0.5in;right:-1px;background:#F15F3F;color:#fff;font:800 6.2pt Inter,sans-serif;letter-spacing:.1em;
  padding:3px 6px 3px 8px;border-radius:3px 0 0 3px;text-transform:uppercase;z-index:2}
.lifes.c4{grid-template-columns:repeat(4,1fr)}
.lifes.c5{grid-template-columns:repeat(5,1fr)}
.lifes.c6{grid-template-columns:repeat(6,1fr)}
.lifes.c3{grid-template-columns:repeat(3,1fr);gap:0.18in}
.life.l3{align-items:stretch;text-align:left;flex-direction:row;gap:10px}
.life.l3 .disc2{flex:none;width:0.8in;height:0.8in}
.life.l3 ul{margin:2px 0 0;padding-left:13px;font-size:7.8pt;line-height:1.32;color:#F5F7F8}
.life.l3 b{margin-top:0}
.hexrow{display:flex;flex-wrap:wrap;justify-content:center;gap:0.06in 0.12in}
.hexrow .life{width:1.12in}
.icons5 .life .disc2{background:transparent;box-shadow:none;color:#FFD9BF}
.icons5 .life .disc2 svg{width:0.6in!important;height:0.6in!important}
"""


def life_block(b):
    style = b["style"]
    items = b["life"]
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
    cells = "".join(
        f'<div class="life {cls}"><div class="disc2">{icon(ic, "0.5in")}</div><b>{a}</b><p>{p}</p></div>'
        for ic, a, p in items)
    n = len(items)
    extra = " icons5" if style == "icons" else ""
    return f'<div class="lifes c{n}{extra}">{cells}</div>'


def col_block(c):
    p = products.get(c["p"])
    dose = c.get("dose")
    dosesub = c.get("dosesub")
    if dose in (None, "dose_from_db"):
        dose, dosesub = p["dose"], p.get("dosesub", "")
    lis = "".join(f"<li>{x}</li>" for x in c["bullets"])
    start = '<span class="startt">Start here</span>' if c.get("start") else ""
    return (f'<div class="col">{start}<div class="need"><b>{c["need"]}</b><i>{c["needsub"]}</i></div>'
            f'<div class="pick"><img src="{p["img"]}" alt="NutriDyn {E(p["name"])} bottle"><div class="nm">{p["name"]}</div>'
            f'<div class="sz">{p["size"]}</div></div>'
            f'<div class="what"><ul>{lis}</ul><div class="key"><b>In each serving</b><br>{p["key"]}</div></div>'
            f'<div class="dose">{dose}<small>{dosesub or ""}</small></div></div>')


SLOTS = [("am", "Morning", "sun"), ("pm", "Evening meal", "plate"), ("bed", "Bedtime", "moon")]


def rhythm_block(cols):
    by = {"am": [], "pm": [], "bed": []}
    caps = scoops = 0
    for c in cols:
        p = products.get(c["p"])
        for slot, n, unit in p["sched"]:
            by[slot].append(f'{p["name"]} <em>{n} {unit}</em>')
            if unit.startswith("scoop"):
                scoops += n
            elif unit.startswith(("dropper", "serving")):
                pass
            else:
                caps += n
    cells = ""
    for key, label, ic in SLOTS:
        lis = "".join(f"<li>{x}</li>" for x in by[key]) or "<li><em>nothing</em></li>"
        cells += f'<div class="slot"><div class="when">{icon(ic, "13px", sw=4)}{label}</div><ul>{lis}</ul></div>'
    parts = []
    if caps:
        parts.append(f"{caps} pill{'s' if caps != 1 else ''}")
    if scoops:
        parts.append(f"{scoops} scoop{'s' if scoops != 1 else ''}")
    total = (f'<div class="total">The full plan is <b>{" and ".join(parts)} a day</b>. Overwhelmed? Start with the '
             f'<b>Start here</b> pick, then add one product a week.</div>')
    return f'<div class="rhythm">{cells}</div>{total}'


def front_page(s):
    t = kit.THEMES[s["theme"]]
    sub = f'<br><small>{s["sub"]}</small>' if s.get("sub") else ""
    intro = f'<p class="intro">{s["intro"]}</p>' if s.get("intro") else ""
    return (f'<section class="sheet front" style="{theme_vars(s["theme"])}"><div class="rule-top"></div><div class="inner">'
            f'<div class="headrow">{logo("0.27in")}<span class="series">{s["series"]}</span></div>'
            '<div class="fields"><span>Patient name</span><span class="box"></span><span>Date</span><span class="box"></span></div>'
            f'<h1 class="title">{s["title"]}{sub}</h1>{intro}{s["front"](t)}'
            f'<div class="foot"><span>NutriDyn &middot; Practitioner Exclusive &middot; nutridyn.com</span>'
            f'<span class="code">{s["code"]} &middot; Page 1 of 2</span></div></div><div class="rule-bot"></div></section>')


def back_page(s):
    b = s["back"]
    sub = f'<small>{b["life_sub"]}</small>' if b.get("life_sub") else ""
    ncol = len(b["cols"])
    cols = "".join(col_block(c) for c in b["cols"])
    rx = "".join(f"<li>{x}</li>" for x in b["rx"])
    lines = '<div class="ln"></div>' * 3
    return (f'<section class="sheet back" style="{theme_vars(s["theme"])}"><div class="rule-top" style="display:none"></div><div class="inner" style="top:0">'
            f'<div class="band" style="padding-top:0.3in"><h2>{b["life_title"]}{sub}</h2>{life_block(b)}</div>'
            '<div class="ns-title">Nutrient Solutions<span>What your body needs, and the NutriDyn formula that delivers it</span></div>'
            f'<div class="cols" style="grid-template-columns:repeat({ncol},1fr)">{cols}</div>'
            f'<div class="duo"><div class="panel"><h3>Your daily rhythm</h3>{rhythm_block(b["cols"])}</div>'
            f'<div class="panel rx"><h3>Pharmacist check</h3><ul>{rx}</ul></div></div>'
            f'<div class="notes"><b>Special considerations for you:</b>{lines}</div>'
            '<div class="recby"><span>Recommended by</span><span class="ln2" data-for></span><span>Phone</span>'
            '<span class="ln2" style="flex:0 0 1.5in"></span></div>'
            f'<div class="foot"><div class="disc">{DISCLAIMER}</div><div style="display:flex;flex-direction:column;align-items:flex-end;gap:4px">'
            f'{logo("0.22in")}<span class="code">{s["code"]} &middot; Page 2 of 2 &middot; 11/2026</span></div></div>'
            '</div><div class="rule-bot"></div></section>')


def sheet_html(s, standalone=True):
    body = front_page(s) + back_page(s)
    if not standalone:
        return body
    tb = kit.toolbar(f'{s["title"]} · two-sided sheet', f'{s["slug"]}.pdf')
    return kit.page_shell(f'{s["title"]} · NutriDyn sheet', tb + f'<div class="stack">{body}</div>', s["theme"],
                          sheets.EXTRA_CSS + BACK_CSS)


INDEX_CSS = r"""
body{background:#F1EFE8}
.wrap{max-width:1180px;margin:0 auto;padding:22px 16px 60px}
.hero{background:#14664D;color:#fff;border-radius:14px;padding:22px 22px 20px;display:grid;gap:10px}
.hero .k{font:800 12px Inter;letter-spacing:.18em;text-transform:uppercase;color:#BFE3D4}
.hero h1{font:900 clamp(26px,5vw,40px)/1.1 Merriweather,Georgia,serif;margin:0}
.hero p{margin:0;font-size:15px;line-height:1.5;color:#E5F2EC;max-width:70ch}
.stats{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:10px;margin:16px 0}
.stt{background:#FBFAF6;border-radius:10px;padding:12px 14px}
.stt b{display:block;font:900 30px Merriweather,Georgia,serif;color:#14664D;line-height:1}
.stt span{font:700 11px Inter;letter-spacing:.12em;text-transform:uppercase;color:#6B6B66}
.bar{display:flex;flex-wrap:wrap;gap:10px;align-items:center;background:#FBFAF6;border-radius:10px;padding:12px 14px;margin-bottom:16px}
.bar label{font:700 13px Inter;color:#2C2C2A}
.bar input{flex:1 1 220px;min-width:0;min-height:44px;border:1px solid #CFC9BC;border-radius:8px;padding:0 12px;font:15px Inter}
.btn{display:inline-flex;align-items:center;justify-content:center;min-height:44px;padding:0 16px;border-radius:99px;background:#14664D;
  color:#fff;text-decoration:none;font:700 14px Inter;white-space:nowrap}
.btn.g{background:transparent;color:#14664D;border:1.5px solid #14664D}
.btn.c{background:#F15F3F}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(250px,1fr));gap:16px}
.card{background:#FBFAF6;border-radius:12px;overflow:hidden;display:flex;flex-direction:column;box-shadow:0 1px 0 #E2DED4;
  transition:transform .15s ease,box-shadow .15s ease}
.card:hover{transform:translateY(-3px);box-shadow:0 8px 20px rgba(0,0,0,.08)}
.card .th{display:grid;grid-template-columns:1fr 1fr;gap:2px;background:#E2DED4}
.card .th img{width:100%;height:auto;display:block}
.card .bd{padding:12px 14px 14px;display:flex;flex-direction:column;gap:8px;flex:1}
.card h2{font:900 18px/1.2 Merriweather,Georgia,serif;margin:0;color:#2C2C2A}
.card .fam{font:800 11px Inter;letter-spacing:.14em;text-transform:uppercase}
.card .pp{font-size:13px;color:#5B5B55;line-height:1.4;margin:0}
.card .row{display:flex;gap:8px;flex-wrap:wrap;margin-top:auto}
.how{background:#FBFAF6;border-radius:12px;padding:16px 18px;margin-top:18px;display:grid;gap:8px}
.how h3{font:900 18px Merriweather,Georgia,serif;margin:0;color:#14664D}
.how ol{margin:0;padding-left:20px;font-size:14px;line-height:1.55}
.src{font-size:12px;color:#6B6B66;margin-top:18px;line-height:1.5}
"""


def index_html(all_sheets):
    fam = {"gut": ("#0E6A7A", "Gut"), "teal": ("#13827C", "Gut"), "gerd": ("#CF4A1C", "Gut"),
           "metab": ("#8A1B22", "Metabolic"), "immune": ("#4A2B80", "Immune")}
    cards = ""
    for s in all_sheets:
        c, f = fam[s["theme"]]
        n = len(s["back"]["cols"])
        names = ", ".join(products.get(x["p"])["name"] for x in s["back"]["cols"])
        cards += (f'<article class="card"><a class="th" href="{s["slug"]}.html"><img src="img/thumb-{s["slug"]}-1.jpg" alt="Front of the {E(s["title"])} sheet" loading="lazy">'
                  f'<img src="img/thumb-{s["slug"]}-2.jpg" alt="Back of the {E(s["title"])} sheet" loading="lazy"></a>'
                  f'<div class="bd"><span class="fam" style="color:{c}">{f} &middot; {s["code"]}</span><h2>{s["title"]}</h2>'
                  f'<p class="pp">{n} NutriDyn picks: {E(names)}.</p>'
                  f'<div class="row"><a class="btn" data-k href="{s["slug"]}.html">Open and print</a><a class="btn g" href="{s["slug"]}.pdf">PDF</a></div></div></article>')
    body = f"""<div class="wrap">
<div class="hero"><span class="k">NutriDyn &middot; Patient education &middot; November 2026</span>
<h1>Condition sheets</h1>
<p>Nine two-sided handouts. The front explains the condition. The back has the lifestyle steps, the NutriDyn products that
deliver each nutrient (with photos, what's in them and how to take them), a daily schedule and pharmacist notes on medicine
and nutrient interactions. Print double-sided, flip on the long edge.</p></div>
<div class="stats"><div class="stt"><b>9</b><span>conditions</span></div><div class="stt"><b>18</b><span>printed pages</span></div>
<div class="stt"><b>{len({x["p"] for s in all_sheets for x in s["back"]["cols"]})}</b><span>NutriDyn products shown</span></div>
<div class="stt"><b>1</b><span>start-here pick per sheet</span></div></div>
<div class="bar"><label for="pr">Practice name to print on every sheet</label>
<input id="pr" placeholder="e.g. your pharmacy or clinic name" autocomplete="organization">
<a class="btn c" href="all-condition-sheets.pdf">All 9 sheets, one PDF</a>
<a class="btn g" href="warehouse-bottle-counter-card.html">Warehouse-bottle counter card</a></div>
<div class="grid">{cards}</div>
<div class="how"><h3>How to use them</h3><ol>
<li>Pick the sheet, write the patient's name and date at the top.</li>
<li>On the back, tick the lifestyle steps that apply and circle the products you recommend.</li>
<li>Write the dose and anything specific in <i>Special considerations</i>. The "Start here" pick is the one to begin with.</li>
<li>Typing a practice name above fills the "Recommended by" line when you print from the page (the PDFs leave it blank to hand-write).</li>
</ol></div>
<p class="src">Built from NutriDyn label facts and practitioner protocols. Condition facts from the CDC, WHO, FDA, AASLD,
ACG and AHA/ACC. Every product statement is structure/function and carries the FDA disclaimer. Generated by
handouts/conditions/build/build.py; do not hand-edit.</p>
</div>
<script>(function(){{var i=document.getElementById('pr');var k='mc_sheet_practice';
function upd(){{var v=i.value.trim();document.querySelectorAll('a[data-k]').forEach(function(a){{var b=a.getAttribute('href').split('?')[0];
a.setAttribute('href',v?b+'?for='+encodeURIComponent(v):b);}});try{{localStorage.setItem(k,v)}}catch(e){{}}}}
try{{i.value=localStorage.getItem(k)||''}}catch(e){{}}i.addEventListener('input',upd);upd();}})();</script>"""
    return kit.page_shell("Condition Sheets · NutriDyn", body, "gut", INDEX_CSS)


def main():
    pdf = "--pdf" in sys.argv
    os.makedirs(os.path.join(OUT, "img"), exist_ok=True)
    products.stage_images(os.path.join(OUT, "img"))
    missing = products.check_complete([c["p"] for s in sheets.SHEETS for c in s["back"]["cols"]])
    if missing:
        print("PLACEHOLDER PRODUCTS STILL IN USE:", missing)
    for s in sheets.SHEETS:
        with open(os.path.join(OUT, f'{s["slug"]}.html'), "w") as f:
            f.write(sheet_html(s))
    allbody = "".join(sheet_html(s, False) for s in sheets.SHEETS)
    tmp = os.environ.get("SHEETS_TMP", HERE)
    os.makedirs(tmp, exist_ok=True)
    with open(os.path.join(tmp, "_all.html"), "w") as f:
        f.write(kit.page_shell("All condition sheets", f'<div class="stack">{allbody}</div>', "gut", sheets.EXTRA_CSS + BACK_CSS)
                .replace('src="img/', f'src="{OUT}/img/'))
    with open(os.path.join(OUT, "index.html"), "w") as f:
        f.write(index_html(sheets.SHEETS))
    if pdf:
        subprocess.run(["node", os.path.join(HERE, "render.js"), OUT, tmp], check=True)
    print("built", len(sheets.SHEETS), "sheets")


if __name__ == "__main__":
    main()
