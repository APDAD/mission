"""Mold Illness sheet (ND-IM-302).  Self-contained: front art, copy and back data.

Front rebuilt 2026-11-03 from Asher's notes on draft 1 ("Great job... mycotoxins is
the red stop sign, and then the crescent looking thing is a binder.  Great job.  We
need that for everything."):
  * the symbol language stays: red hexagon = mycotoxin, blue crescent = binder;
  * every key swatch is measured, so no label touches its swatch (draft 1's legend
    text ran into the crescent);
  * the house is redrawn as a cutaway and carries a KEY (mold growth, moisture or leak);
  * the binder diagram is drawn 1:1 across the full text width and sized so the page
    runs to the footer with no dead space;
  * every label prints at 7 pt or more, nothing is clipped.
Back: kept exactly as draft 1 (sheets.py); a later pass revises the products.

Fix round 2026-11-03 (art director's review):
  * "Cough, wheeze" uses an in-module LUNGS icon (windpipe, two bronchi, two separate
    lobes); the kit "lungs" fused its lobes and read as a peach;
  * step 4 says "Ask a clinician" in both editions (a pharmacist does not examine sinuses);
  * binder diagram: the gut is an open tube that fades out at both ends, the exit arrow
    leaves its open end and is labelled "To stool"; every free toxin now sits downstream of
    the bile duct; the binder capsule opens INSIDE the lumen (cap popped off, binder
    spilling down the gut) instead of pouring through the wall, labelled from clear space;
    the Bile swatch is drawn like the duct (dark rim, light core, square ends) with clear
    space to its words; "Gallbladder" is 10 px and further from the organ, "Gut" sits lower;
    KEY titles are 10 px;
  * house: leaders carry a white underlay (the AC leader no longer vanishes over the roof
    band), the attic has one keyed drop over its puddle (the two merged drops are gone),
    every puddle sits under a keyed drop, and the window's condensation dots are replaced by
    fogged glass with keyed drops, so the key's two symbols are the only ones used;
  * the draft-1 back overflowed its frame (disclaimer cut, page/edition line not printed).
    SHEET["back"] stayed frozen for the back-page pass, so scoped back-only CSS fitted it
    without changing a word (superseded by the back-page pass below).

Back-page pass 2026-11-03 (the front's design is approved and unchanged; only the final
front review's small fixes are applied):
  * front fixes: the binder KEY rows are 22 px apart and the box is narrowed flush right; the
    house KEY swatch is a drop over a puddle ("Moisture, leak or puddle"), so the cutaway's
    puddles are keyed too, with measured label widths; the red return arrow ends at the
    liver's left-lobe tip; the two free binders are drawn the size of the caught ones;
    "Joint aches" uses an in-module JOINT icon (the kit bone is not a joint);
  * products follow NutriDyn's own mold protocols: KBMO Mycotoxin Protocol ND1610 (Binder Pro,
    GI Defend) and a NutriDyn educator's mold plans for Asher's 2025 Georgia seminar
    (Lipo-Flow, glutathione, Mito Recharge).  Binder Pro is the Start-here pick, the binder
    the front's diagram shows.  Five columns, the competitor's count.  Facts and sources:
    products.d/mold.json (mold-owned keys, each label re-opened this pass);
  * binder spacing rule: Binder Pro goes mid-morning and mid-evening (the educator's grids), 2 hours
    from food, other supplements and medicine, and every other product sits at a meal, so the check
    panel's rule, the dose bar and the daily rhythm agree;
  * lifestyle band: protocol advice added where it is real ("Test home & work" from the educator's
    "Preparation Plan (While Waiting on Labs and Home/Work Samples)"; "Stay regular" from
    ND1610's "elimination through the stool" and her optional magnesium citrate); "Fix fast"
    (the front's step 1, word for word) and "Sweat" (no source) are out;
  * the check panel is written per edition: pharmacists check interactions and nutrient
    losses, providers order labs, refer and adjust.

Every SVG is drawn at 1:1 with its printed CSS size (viewBox width = rendered width
in CSS px), so an SVG font-size of 9.4 prints at 7.05 pt.

Sources (a short comment sits next to each fact below):
  Fisk, Lei-Gomez and Mendell, Indoor Air 2007;17:284-96 (meta-analysis: damp, moldy
    homes, about 30 to 50 percent more respiratory and asthma outcomes)
  Mudarri and Fisk, Indoor Air 2007;17:226-35 (21 percent of U.S. current asthma,
    4.6 million cases, attributable to dampness and mold at home)
  CDC, Mold: Basic Facts (stuffy nose, wheezing, red or itchy eyes or skin)
  Institute of Medicine, Damp Indoor Spaces and Health, 2004 (cough, wheeze, upper
    airway symptoms; asthma symptoms in people with asthma)
  EPA, A Brief Guide to Mold, Moisture, and Your Home (dry leaks within 24 to 48 hours;
    more than about 10 square feet: use EPA's remediation guide / a professional)
  Kerkadi et al., J Toxicol Environ Health A 1998;53:231-50 (a bile-acid binder raised
    fecal excretion of the mycotoxin ochratoxin A and cut its enterohepatic recirculation)
  Back page:
  WHO, Mycotoxins fact sheet (aflatoxins in maize, groundnuts, tree nuts, spices; ochratoxin A
    in cereals, coffee, dried vine fruit, wine and grape juice, spices; patulin in apples)
  EPA, A Brief Guide to Mold, Moisture, and Your Home (indoor humidity ideally 30 to 50 percent);
    EPA, Guide to Air Cleaners in the Home (HEPA filters capture mold spores)
  Dietary Guidelines for Americans 2020-2025 (fiber 14 g per 1,000 kcal: 22 to 34 g a day for
    adults, so "about 30 g")
  Ohkawa et al., Rinsho Shinkeigaku 1995;35:806-7 (PMID 8777808: chlorella, a vitamin K-rich
    food, blunted warfarin); Rohde et al., Curr Opin Clin Nutr Metab Care 2007;10:1-5
    (doi:10.1097/MCO.0b013e328011c46c: vitamin K intake over 250 mcg a day lowers warfarin
    sensitivity; supplements can carry enough K1 to move the INR); Sconce et al., Blood
    2007;109:2419-23 (doi:10.1182/blood-2006-09-049262: steady daily vitamin K steadies the INR)
  FDA labels for the azole antifungals (itraconazole, voriconazole, posaconazole: strong CYP3A4
    inhibitors with long interaction lists)
"""
import math
import random

from kit import icon
from svgkit import T, svg

INK = "#2B3236"
SOFT_INK = "#4A555C"
LEAD = "#59636A"
TOXIN = "#C8343B"        # red hexagon: mycotoxin ("the red stop sign")
TOXIN_TXT = "#A3262D"
BINDER = "#2C6FB7"       # blue crescent: binder
BINDER_TXT = "#1D4F87"
WATER = "#3B8BD4"        # blue drop: moisture or leak
BILE = "#5E9E3C"
BILE_TXT = "#3D7424"
MOLD = ("#263719", "#3B5428", "#566F3C")   # mold speck colours, dark to light

HOUSE_W = 400            # CSS px: the house column is exactly this wide
FRONT_W = 735.36         # CSS px: 8.5in page minus two 0.42in margins


def _f(v):
    return f"{v:.2f}".rstrip("0").rstrip(".")


# ============================================================ symbols
def hexagon(x, y, r, fill=TOXIN, edge="#FFFFFF", ew=1.3):
    """Mycotoxin: a red hexagon with a white rim, point up (reads as a stop sign)."""
    pts = " ".join(f"{_f(x + r * math.cos(math.radians(a)))},{_f(y + r * math.sin(math.radians(a)))}"
                   for a in range(-90, 270, 60))
    return f'<polygon points="{pts}" fill="{fill}" stroke="{edge}" stroke-width="{ew}" stroke-linejoin="round"/>'


# Crescent = outer circle R minus a bite circle (radius .85R, centre .45R to the left).
# Its horns sit at x = -0.533R, so its true width runs from -0.533R to +R.
CRES_D, CRES_RI = 0.45, 0.85
CRES_U = -(1 - CRES_RI ** 2 + CRES_D ** 2) / (2 * CRES_D)
CRES_V = math.sqrt(1 - CRES_U ** 2)


def crescent(cx, cy, R, fill=BINDER, rot=0.0):
    """Binder: a crescent centred on its outer circle, bite opening to the left
    (rotated by rot degrees)."""
    u, v, ri = CRES_U * R, CRES_V * R, CRES_RI * R
    d = (f"M{_f(u)},{_f(-v)} A{_f(R)},{_f(R)} 0 1 1 {_f(u)},{_f(v)} "
         f"A{_f(ri)},{_f(ri)} 0 1 0 {_f(u)},{_f(-v)}Z")
    return f'<path transform="translate({_f(cx)},{_f(cy)}) rotate({_f(rot)})" d="{d}" fill="{fill}"/>'


def caught(x, y, r=7.2, R=11.5, rot=0.0):
    """A toxin held in a binder's bite: the hexagon sits on the bite circle's centre."""
    a = math.radians(rot)
    return hexagon(x, y, r) + crescent(x + CRES_D * R * math.cos(a), y + CRES_D * R * math.sin(a), R, rot=rot)


def colony(x, y, r, seed):
    """Mold growth: a soft olive stain with dark specks."""
    rnd = random.Random(seed)
    out = [f'<circle cx="{_f(x)}" cy="{_f(y)}" r="{_f(r)}" fill="url(#moHalo)"/>']
    for _ in range(max(6, int(r * 1.3))):
        ang = rnd.uniform(0, 2 * math.pi)
        dist = r * 0.6 * math.sqrt(rnd.random())
        rr = r * rnd.uniform(0.13, 0.27)
        out.append(f'<circle cx="{_f(x + dist * math.cos(ang))}" cy="{_f(y + dist * math.sin(ang))}" '
                   f'r="{_f(rr)}" fill="{MOLD[rnd.randrange(3)]}"/>')
    return "".join(out)


def drop(x, y, s=1.0):
    """Moisture or leak: a blue drop, tip up, about 10 x 15 at s=1, centred on (x, y)."""
    return (f'<g transform="translate({_f(x)},{_f(y)}) scale({s})">'
            f'<path d="M0,-7.8 C2.5,-4.6 5.2,-1.6 5.2,2 A5.2,5.2 0 0 1 -5.2,2 C-5.2,-1.6 -2.5,-4.6 0,-7.8Z" fill="{WATER}"/>'
            '<path d="M-2.5,2.4 A2.6,2.6 0 0 0 -0.6,4.9" stroke="#FFFFFF" stroke-width="1.1" fill="none" '
            'stroke-linecap="round" opacity=".85"/></g>')


def puddle_drop():
    """Key swatch for water as the cutaway draws it: a keyed drop over a small puddle (every
    puddle in the house sits under a drop), centred on (0, 0) and 15 px wide."""
    return '<ellipse cx="0" cy="6.3" rx="7.5" ry="1.9" fill="#86B1D8"/>' + drop(0, -2.4, 0.8)


def badge(x, y, n, fill):
    return (f'<circle cx="{_f(x)}" cy="{_f(y)}" r="8.5" fill="{fill}"/>'
            + T(x, y + 3.6, str(n), 10, 800, "#FFFFFF", "middle"))


def key_box(x, y, items, w, title="KEY", row_h=19, pad=9, size=10, cols=1):
    """Boxed legend.  items = [(swatch, label)], each swatch drawn centred on (0, 0) and
    at most 18 px wide; its label starts 15 px right of the swatch centre, so there is
    always clear space between a swatch and its words."""
    rows = -(-len(items) // cols)
    col_w = (w - 2 * pad) / cols
    h = pad * 2 + 15 + rows * row_h
    out = [f'<g transform="translate({_f(x)},{_f(y)})">',
           f'<rect width="{_f(w)}" height="{_f(h)}" rx="8" fill="#FFFFFF" stroke="#CFD6DA" stroke-width="1.3"/>',
           T(pad, pad + 9.3, title, 10, 800, INK, ls=1.2)]   # 7.5 pt, off the 7 pt floor
    for i, (sw, lab) in enumerate(items):
        c, r = divmod(i, rows)
        cx = pad + c * col_w + 10
        cy = pad + 15 + r * row_h + row_h / 2
        out.append(f'<g transform="translate({_f(cx)},{_f(cy)})" data-sw="swatch">{sw}</g>')
        out.append(T(cx + 15, cy + size * 0.36, lab, size, 600, INK))
    out.append("</g>")
    return "".join(out), h


def key_row(cx, y, items, title="KEY", pad=9, size=10, gap=16, widths=None):
    """One-line legend centred on cx.  widths = text widths of each label (CSS px)."""
    title_w = 26
    item_ws = [24 + w for w in widths]
    w = pad * 2 + title_w + sum(item_ws) + gap * (len(items) - 1)
    h = 26
    x = cx - w / 2
    out = [f'<g transform="translate({_f(x)},{_f(y)})">',
           f'<rect width="{_f(w)}" height="{h}" rx="8" fill="#FFFFFF" stroke="#CFD6DA" stroke-width="1.3"/>',
           T(pad, h / 2 + 3.6, title, 10, 800, INK, ls=1.2)]
    px = pad + title_w
    for (sw, lab), iw in zip(items, item_ws):
        out.append(f'<g transform="translate({_f(px + 10)},{_f(h / 2)})" data-sw="swatch">{sw}</g>')
        out.append(T(px + 25, h / 2 + size * 0.36, lab, size, 600, INK))
        px += iw + gap
    out.append("</g>")
    return "".join(out)


def leader(x1, y1, x2, y2):
    """Dashed leader with a white underlay, so it stays visible where it crosses dark art
    (the AC leader runs over the slate roof band)."""
    ends = f'x1="{_f(x1)}" y1="{_f(y1)}" x2="{_f(x2)}" y2="{_f(y2)}"'
    return (f'<line {ends} stroke="#FFFFFF" stroke-width="2.6" stroke-linecap="round" opacity=".92"/>'
            f'<line {ends} stroke="{LEAD}" stroke-width=".9" stroke-dasharray="2.6 2"/>'
            f'<circle cx="{_f(x2)}" cy="{_f(y2)}" r="2.6" fill="#FFFFFF" opacity=".92"/>'
            f'<circle cx="{_f(x2)}" cy="{_f(y2)}" r="1.8" fill="{LEAD}"/>')


# ============================================================ house cutaway

# right roof slope: outer line from the apex (200, 14) to the eave (304, 88)
SLOPE = math.atan2(74, 104)


def roof_gap(x):
    """A leak through the right roof slope at x: a dark slot through the roof band and the
    shingle just above it lifted off the roof."""
    dx, dy = math.cos(SLOPE), math.sin(SLOPE)          # down the slope
    nx, ny = -dy, dx                                   # into the roof band
    px, py = x, 14 + 74 * (x - 200) / 104
    thick = 12.3 * math.cos(SLOPE)
    gap = [(px - 2.6 * dx, py - 2.6 * dy), (px + 2.6 * dx, py + 2.6 * dy),
           (px + 2.6 * dx + thick * nx, py + 2.6 * dy + thick * ny), (px - 2.6 * dx + thick * nx, py - 2.6 * dy + thick * ny)]
    hx, hy = px - 11 * dx, py - 11 * dy                # hinge of the lifted shingle
    lift = math.radians(30)
    ex, ey = math.cos(SLOPE - lift), math.sin(SLOPE - lift)
    tx, ty = hx + 13 * ex, hy + 13 * ey                # its lifted lower edge
    flap = [(hx, hy), (tx, ty), (tx - 3.6 * ey, ty + 3.6 * ex), (hx + 3.6 * nx, hy + 3.6 * ny)]
    pts = lambda P: " ".join(f"{_f(a)},{_f(b)}" for a, b in P)
    return (f'<polygon points="{pts(gap)}" fill="#2A3138"/>'
            f'<polygon points="{pts(flap)}" fill="#7A8591" stroke="#3E4751" stroke-width=".7" stroke-linejoin="round"/>')


def art_house(t):
    W, H = HOUSE_W, 284
    out = ['<defs>'
           '<radialGradient id="moHalo"><stop offset="0" stop-color="#4C6634" stop-opacity=".78"/>'
           '<stop offset=".62" stop-color="#5D7843" stop-opacity=".42"/><stop offset="1" stop-color="#6F8A52" stop-opacity="0"/></radialGradient>'
           '<linearGradient id="moGlass" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#E6F2FA"/>'
           '<stop offset="1" stop-color="#B5D3E7"/></linearGradient>'
           '<linearGradient id="moFog" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FFFFFF" stop-opacity=".2"/>'
           '<stop offset="1" stop-color="#FFFFFF" stop-opacity=".62"/></linearGradient>'
           '<linearGradient id="moRoof" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#6A7581"/>'
           '<stop offset="1" stop-color="#4B5561"/></linearGradient>'
           '<clipPath id="moAtticClip"><polygon points="118.9,84 200,26.3 281.1,84"/></clipPath>'
           '<clipPath id="moCutClip"><polygon points="117,166 124,163.5 132,166 142,164 144.5,175 141.5,189 144.5,203 142.5,217 117,217"/></clipPath>'
           '</defs><g transform="translate(0,-6)">']
    # ground outside
    out.append('<rect x="94" y="236" width="212" height="22" rx="3" fill="#BFA283"/>'
               '<rect x="94" y="234.5" width="212" height="4.5" rx="2.2" fill="#8DB56B"/>')
    # wall section and floors
    out.append('<rect x="106" y="84" width="188" height="142" fill="#D9CDB7" stroke="#A8977C" stroke-width="1"/>')
    for (x, y) in [(111, 90), (202, 90), (111, 158), (202, 158)]:
        out.append(f'<rect x="{x}" y="{y}" width="87" height="62" fill="#FBF8F1"/>')
    for y in (84, 152, 220):
        out.append(f'<rect x="106" y="{y}" width="188" height="6" fill="#BFA587" stroke="#9E8565" stroke-width=".7"/>')
    # crawl space: interior, foundation, piers, soil
    out.append('<rect x="114" y="226" width="172" height="24" fill="#E6DDCC"/>'
               '<rect x="114" y="250" width="172" height="8" fill="#9F8467"/>')
    for x in (106, 286):
        out.append(f'<rect x="{x}" y="226" width="8" height="32" fill="#B6AFA5" stroke="#948C82" stroke-width=".7"/>'
                   f'<path d="M{x},234 h8 M{x},242 h8 M{x},250 h8 M{x + 4},226 v8 M{x + 4},242 v8" stroke="#948C82" stroke-width=".6"/>')
    for x in (152, 240):
        out.append(f'<rect x="{x}" y="226" width="8" height="23" fill="#C1BAB0" stroke="#968E84" stroke-width=".6"/>'
                   f'<rect x="{x - 2}" y="248" width="12" height="3" fill="#A9A298"/>')
    out.append('<ellipse cx="205" cy="251.5" rx="16" ry="2.2" fill="#7FA8CE"/>')
    out.append(drop(205, 240.5, 0.8))
    out.append(colony(134, 229.5, 6.5, 11) + colony(266, 229.5, 6, 12))

    # attic interior, collar tie, insulation, AC unit, leak
    out.append('<polygon points="118.9,84 200,26.3 281.1,84" fill="#F4ECDD"/>')
    out.append('<rect x="160" y="50" width="80" height="4" fill="#C49A6C"/>')
    ins = "M110,84 V77 " + " ".join(f"q4,-4.5 8,0" for _ in range(22)) + " V84 Z"
    out.append(f'<g clip-path="url(#moAtticClip)"><path d="{ins}" fill="#F1C3B2" stroke="#DFA690" stroke-width=".7"/></g>')
    out.append('<ellipse cx="252" cy="80.5" rx="9" ry="2.3" fill="#8DB6DA" opacity=".8"/>')
    out.append('<rect x="149" y="80" width="36" height="3.2" rx="1" fill="#8C949B"/>'
               '<rect x="152" y="63" width="30" height="17" rx="2" fill="#CDD2D7" stroke="#8C949B" stroke-width="1"/>'
               '<circle cx="163" cy="71.5" r="5.2" fill="none" stroke="#8C949B" stroke-width="1"/>'
               '<path d="M163,66.3 V76.7 M157.8,71.5 H168.2" stroke="#8C949B" stroke-width=".7"/>'
               '<path d="M172,66 v11 M175,66 v11 M178,66 v11" stroke="#9EA6AD" stroke-width=".8"/>')
    out.append(drop(189.5, 79.5, 0.72))
    out.append(colony(241, 59, 6.5, 13))
    out.append(drop(251, 70, 0.8))            # one keyed drop falling from the roof leak onto the attic puddle
    # roof deck line inside the attic, roof band, soffits
    out.append('<polyline points="118.9,84 200,26.3 281.1,84" fill="none" stroke="#C49A6C" stroke-width="3"/>')
    out.append('<polygon points="96,88 200,14 304,88 304,100.3 200,26.3 96,100.3" fill="url(#moRoof)"/>')
    out.append('<path d="M100,91.2 L200,20 L300,91.2 M100,96.2 L200,25 L300,96.2" stroke="#FFFFFF" stroke-opacity=".14" stroke-width=".8" fill="none"/>')
    out.append('<polygon points="96,100.3 106,100.3 106,93.2" fill="#E3DDD1"/><polygon points="304,100.3 294,100.3 294,93.2" fill="#E3DDD1"/>')
    # roof leak: a gap through the right slope with the shingle above it lifted
    out.append(roof_gap(250))

    # upstairs left: bedroom with a fogged window and a damp ceiling under the AC pan
    out.append('<rect x="124" y="101" width="36" height="32" fill="#FFFFFF" stroke="#9AAFBD" stroke-width="1.2"/>'
               '<rect x="127" y="104" width="30" height="26" fill="url(#moGlass)"/>'
               '<rect x="127" y="104" width="30" height="26" fill="url(#moFog)"/>'
               '<path d="M142,104 V130 M127,117 H157" stroke="#FFFFFF" stroke-width="1.6"/>'
               '<rect x="121" y="133" width="42" height="3" fill="#E6DFD2" stroke="#B8AE9E" stroke-width=".6"/>')
    # fogged glass with the keyed drop running down it (no separate condensation symbol)
    out.append(drop(134.5, 123.6, 0.55) + drop(149.5, 110.8, 0.5))
    out.append(colony(126.5, 132, 5.8, 21) + colony(158, 132.5, 4.8, 22))
    out.append('<rect x="190" y="124" width="5" height="28" rx="1" fill="#A88B6B"/>'
               '<rect x="162" y="137" width="30" height="8" rx="2" fill="#F4F6F9" stroke="#C9D1DA" stroke-width=".7"/>'
               '<rect x="162" y="139.5" width="22" height="7.5" rx="2" fill="#A7B9D2"/>'
               '<ellipse cx="186" cy="135.6" rx="4.6" ry="2.4" fill="#FFFFFF" stroke="#C9D1DA" stroke-width=".7"/>'
               '<rect x="162" y="145" width="30" height="3" fill="#A88B6B"/>'
               '<rect x="163" y="148" width="2" height="4" fill="#8A6F52"/><rect x="189" y="148" width="2" height="4" fill="#8A6F52"/>')
    out.append(colony(170, 94.5, 6.2, 23))

    # upstairs right: bathroom with tile, tub and shower
    out.append('<rect x="202" y="116" width="87" height="36" fill="#E3EBF0"/>')
    out.append("".join(f'<path d="M{x},116 V152" stroke="#CAD6DE" stroke-width=".6"/>' for x in range(210, 289, 8)))
    out.append("".join(f'<path d="M202,{y} H289" stroke="#CAD6DE" stroke-width=".6"/>' for y in range(124, 152, 8)))
    out.append('<rect x="207" y="122" width="8" height="14" rx="1.5" fill="#FFFFFF" stroke="#A9B4BC" stroke-width=".8"/>'
               '<rect x="206" y="136" width="16" height="6" rx="3" fill="#FFFFFF" stroke="#A9B4BC" stroke-width=".8"/>'
               '<rect x="210" y="142" width="7" height="10" fill="#FFFFFF" stroke="#A9B4BC" stroke-width=".8"/>')
    out.append('<rect x="228" y="132" width="61" height="4" rx="2" fill="#FFFFFF" stroke="#A9B4BC" stroke-width=".8"/>'
               '<path d="M230,136 H287 V146 C287,149.5 284.5,152 281,152 H236 C232.5,152 230,149.5 230,146 Z" '
               'fill="#FFFFFF" stroke="#A9B4BC" stroke-width=".8"/>')
    out.append('<path d="M289,103 H279.5" stroke="#98A3AC" stroke-width="2.2"/>'
               '<polygon points="275.5,103.5 283,103.5 285,108.5 273.5,108.5" fill="#A9B4BC"/>')
    out.append(drop(276, 119.5, 0.7))
    out.append(colony(281.5, 95, 6.2, 31) + colony(246, 131.5, 4.8, 32))

    # downstairs left: living room with an opened wall showing a leaking pipe
    out.append('<polygon points="117,166 124,163.5 132,166 142,164 144.5,175 141.5,189 144.5,203 142.5,217 117,217" '
               'fill="#D5C5A8" stroke="#B29C7C" stroke-width=".8"/>')
    out.append('<g clip-path="url(#moCutClip)"><rect x="117" y="160" width="4" height="60" fill="#C9A87F"/>'
               '<rect x="139" y="160" width="4" height="60" fill="#C9A87F"/>'
               '<rect x="127.5" y="160" width="4" height="60" fill="#C47D47"/>'
               '<rect x="128.4" y="160" width="1.1" height="60" fill="#E2A97A"/>'
               '<rect x="126" y="183.5" width="7" height="3.6" rx=".8" fill="#9E5C34"/></g>')
    out.append(drop(136, 192.5, 0.6))
    out.append(colony(130, 209.5, 7.2, 41) + colony(147.5, 213, 4.4, 42))
    out.append('<rect x="160" y="169" width="23" height="15" fill="#F2E8D6" stroke="#B49F80" stroke-width="1.4"/>'
               '<path d="M162,182 L168,175 L172,179 L176,173.5 L181,182 Z" fill="#B9CBB0"/>')
    out.append('<rect x="152" y="196" width="40" height="12" rx="4" fill="#8F9EB3"/>'
               '<rect x="150" y="205" width="44" height="9" rx="3" fill="#A6B3C4"/>'
               '<rect x="147" y="201" width="7" height="14" rx="3" fill="#8F9EB3"/><rect x="190" y="201" width="7" height="14" rx="3" fill="#8F9EB3"/>'
               '<rect x="152" y="215" width="2" height="5" fill="#6B5B4A"/><rect x="189" y="215" width="2" height="5" fill="#6B5B4A"/>')

    # downstairs right: kitchen, sink cabinet open on a leaking trap
    out.append('<rect x="216" y="163" width="68" height="14" fill="#D6C3A2" stroke="#B39C7C" stroke-width=".8"/>'
               '<path d="M238.7,163 V177 M261.3,163 V177" stroke="#B39C7C" stroke-width=".8"/>'
               '<circle cx="235.5" cy="174" r=".9" fill="#8A7456"/><circle cx="241.9" cy="174" r=".9" fill="#8A7456"/>'
               '<circle cx="258.1" cy="174" r=".9" fill="#8A7456"/><circle cx="264.5" cy="174" r=".9" fill="#8A7456"/>')
    out.append('<path d="M248,186 V180.5 C248,176.5 255,176.5 255,180.5 V182.5" stroke="#9AA5AE" stroke-width="2" fill="none" stroke-linecap="round"/>')
    out.append('<rect x="208" y="190" width="81" height="30" fill="#D6C3A2" stroke="#B39C7C" stroke-width=".8"/>'
               '<rect x="208" y="186" width="81" height="4.2" fill="#7C8992"/>')
    out.append('<path d="M238,190 H262 V195.5 C262,197.2 260.8,198.4 259,198.4 H241 C239.2,198.4 238,197.2 238,195.5 Z" '
               'fill="#C8D0D6" stroke="#9AA5AE" stroke-width=".8"/>')
    out.append('<rect x="228" y="200" width="44" height="19" fill="#8F7B60"/>'
               '<polygon points="228,200 222.5,198.5 222.5,219 228,219" fill="#E3D3B6" stroke="#B39C7C" stroke-width=".6"/>'
               '<polygon points="272,200 277.5,198.5 277.5,219 272,219" fill="#E3D3B6" stroke="#B39C7C" stroke-width=".6"/>')
    out.append('<path d="M250,198.4 V205 C250,210.6 258,210.6 258,205 V203.2 H271.5" stroke="#C3CBD1" stroke-width="2.6" '
               'fill="none" stroke-linecap="round"/>')
    out.append('<ellipse cx="257" cy="218.2" rx="7" ry="1.3" fill="#86B1D8"/>')
    out.append(drop(254.5, 213.5, 0.55))
    out.append(colony(237.5, 214, 6, 51))

    # labels and leaders: left column ends at x=86, right column starts at x=314
    lab = lambda x, y, lines, anchor: T(x, y, lines, 10, 700, INK, anchor, lh=1.24)
    out.append(lab(86, 57, ["AC units and", "drip pans"], "end") + leader(89, 61, 150.5, 80.5))
    out.append(lab(86, 112, ["Foggy, wet", "windows"], "end") + leader(89, 116, 125.5, 118.5))
    out.append(lab(86, 182, ["Inside walls", "(hidden leaks)"], "end") + leader(89, 186, 126, 185.3))
    out.append(lab(86, 236, ["Crawl spaces", "and basements"], "end") + leader(89, 240, 129, 231))
    out.append(lab(314, 42, "Roof leaks", "start") + leader(311, 38.5, 256, 46.5))
    out.append(lab(314, 96, ["Showers", "and tubs"], "start") + leader(311, 100, 287, 96))
    out.append(lab(314, 207, "Under sinks", "start") + leader(311, 203.5, 261.8, 211.5))
    out.append("</g>")
    # key: the water swatch is a drop over a puddle, so the cutaway's puddles are keyed too.
    # widths = the labels' measured text widths (CSS px, Inter 600 at 10 px)
    out.append(key_row(200, 256, [(colony(0, 0, 8, 7), "Mold growth"), (puddle_drop(), "Moisture, leak or puddle")],
                       widths=[61, 117]))
    return svg(W, H, "".join(out), "Where mold hides in a home: attic, windows, walls, bathroom, kitchen sink and crawl space")


# ============================================================ binder diagram
def _bez(p0, p1, p2, p3, t):
    u = 1 - t
    return (u ** 3 * p0[0] + 3 * u * u * t * p1[0] + 3 * u * t * t * p2[0] + t ** 3 * p3[0],
            u ** 3 * p0[1] + 3 * u * u * t * p1[1] + 3 * u * t * t * p2[1] + t ** 3 * p3[1])


GY = 210   # gut centre-line baseline
# The first and last segments are short straight runs that carry the tube on past both of
# its faded ends, so its round stroke caps sit wholly in the transparent part of the fade
# mask and the tube reads as open at both ends (not a sealed sac).
GUT = [((38.5, GY + 9.45), (49, GY + 6.3), (59.5, GY + 3.15), (70, GY)),
       ((70, GY), (150, GY - 24), (230, GY + 24), (330, GY)),
       ((330, GY), (420, GY - 22), (480, GY + 22), (560, GY)),
       ((560, GY), (588, GY - 9), (610, GY - 4), (630, GY - 4)),
       ((630, GY - 4), (643, GY - 4), (656, GY - 4), (669, GY - 4))]
GUT_D = "M{},{} ".format(*GUT[0][0]) + " ".join(
    "C{},{} {},{} {},{}".format(*seg[1], *seg[2], *seg[3]) for seg in GUT)
LUMEN = 46.0     # lumen width; the wall band is LUMEN + 22, its outline LUMEN + 25


def gut_y(x):
    """Centre-line height of the gut tube at x (bisection on the matching segment)."""
    for seg in GUT:
        if seg[0][0] <= x <= seg[3][0]:
            lo, hi = 0.0, 1.0
            for _ in range(40):
                mid = (lo + hi) / 2
                if _bez(*seg, mid)[0] < x:
                    lo = mid
                else:
                    hi = mid
            return _bez(*seg, lo)[1]
    raise ValueError(x)


def villi(spacing=7.0, r=2.9, skip=16):
    """Small folds of the gut lining along both edges of the lumen."""
    pts = []
    for seg in GUT:
        pts += [_bez(*seg, i / 240) for i in range(240)]
    pts.append(GUT[-1][3])
    run, nxt, out = 0.0, skip, []
    total = sum(math.dist(pts[i], pts[i + 1]) for i in range(len(pts) - 1))
    for i in range(1, len(pts) - 1):
        run += math.dist(pts[i - 1], pts[i])
        if run < nxt or run > total - skip:
            continue
        nxt += spacing
        tx, ty = pts[i + 1][0] - pts[i - 1][0], pts[i + 1][1] - pts[i - 1][1]
        n = math.hypot(tx, ty)
        nx, ny = -ty / n, tx / n
        for sgn in (1, -1):
            o = sgn * LUMEN / 2
            out.append(f'<circle cx="{_f(pts[i][0] + nx * o)}" cy="{_f(pts[i][1] + ny * o)}" r="{r}"/>')
    return f'<g fill="#EEC6B2" stroke="#DDA48E" stroke-width=".7">{"".join(out)}</g>'


def gut_angle(x):
    """Direction of the gut centre-line at x, in degrees."""
    return math.degrees(math.atan2(gut_y(x + 1) - gut_y(x - 1), 2))


def capsule_open(x, y, rot=0.0):
    """The binder you take, opening inside the gut: a two-tone capsule (white body, blue cap,
    about 34 x 15) whose cap has popped off downstream, so the binder spills out along the
    lumen.  Drawn along the gut's direction (rot)."""
    return (f'<g transform="translate({_f(x)},{_f(y)}) rotate({_f(rot)})">'
            '<path d="M1,-7.3 H-9.7 A7.3,7.3 0 0 0 -9.7,7.3 H1 Z" fill="#FFFFFF" stroke="#2C6FB7" stroke-width="1.6" '
            'stroke-linejoin="round"/>'
            '<path d="M-13.6,-3.2 H-7" stroke="#C9DBEF" stroke-width="1.6" stroke-linecap="round"/>'
            '<g transform="translate(6.5,-2.2) rotate(-24)"><path d="M0,-7.3 H8.2 A7.3,7.3 0 0 1 8.2,7.3 H0 Z" '
            'fill="#2C6FB7"/></g></g>')


LIVER_D = ("M28,78 C24,54 48,33 92,31 C124,30 156,34 182,41 C198,45 212,50 214,57 C215,62 208,66 198,70 "
           "C176,79 150,89 130,99 C122,103 116,107 112,111 C104,121 90,133 72,134 C46,135 30,113 28,93 "
           "C27,87 27,83 28,78 Z")


def art_binder(t, H=288):
    W = FRONT_W
    c1 = t["c1"]
    out = ['<defs>'
           '<radialGradient id="moLiv" cx="34%" cy="28%" r="80%"><stop offset="0" stop-color="#CC6150"/>'
           '<stop offset=".55" stop-color="#A93D30"/><stop offset="1" stop-color="#7C271F"/></radialGradient>'
           '<linearGradient id="moGb" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#B2D67F"/>'
           '<stop offset="1" stop-color="#6A9C42"/></linearGradient>'
           f'<mask id="moRing" maskUnits="userSpaceOnUse" x="0" y="0" width="{_f(W)}" height="{H}">'
           f'<path d="{GUT_D}" stroke="#FFFFFF" stroke-width="{LUMEN + 26}" fill="none" stroke-linecap="round"/>'
           f'<path d="{GUT_D}" stroke="#000000" stroke-width="{LUMEN}" fill="none" stroke-linecap="round"/></mask>'
           # both ends of the gut fade out: this is a stretch of an open tube, not a sealed sac
           f'<linearGradient id="moFadeG" gradientUnits="userSpaceOnUse" x1="0" y1="0" x2="{_f(W)}" y2="0">'
           f'<stop offset="{42 / W:.4f}" stop-color="#000000"/><stop offset="{82 / W:.4f}" stop-color="#FFFFFF"/>'
           f'<stop offset="{614 / W:.4f}" stop-color="#FFFFFF"/><stop offset="{655 / W:.4f}" stop-color="#000000"/></linearGradient>'
           f'<mask id="moFade" maskUnits="userSpaceOnUse" x="0" y="0" width="{_f(W)}" height="{H}">'
           f'<rect width="{_f(W)}" height="{H}" fill="url(#moFadeG)"/></mask>'
           '<marker id="moArR" viewBox="0 0 10 10" refX="6.5" refY="5" markerWidth="4.4" markerHeight="4.4" orient="auto-start-reverse">'
           '<path d="M0,0 L10,5 L0,10 z" fill="#C0392B"/></marker>'
           '<marker id="moArK" viewBox="0 0 10 10" refX="6.5" refY="5" markerWidth="3.6" markerHeight="3.6" orient="auto-start-reverse">'
           '<path d="M0,0 L10,5 L0,10 z" fill="#2B3236"/></marker>'
           '</defs>']
    # gallbladder (tucked under the liver), bile duct to the gut, liver
    out.append('<path d="M83,112 C75,130 79,156 96,157 C113,158 117,133 107,110 Z" fill="url(#moGb)" stroke="#4E7F2E" stroke-width="1"/>')
    duct_end = (152, gut_y(152) - 22)
    duct = f"M106,118 C114,142 136,152 {_f(duct_end[0])},{_f(duct_end[1])}"
    out.append(f'<path d="{duct}" stroke="#4E8A33" stroke-width="9" fill="none" stroke-linecap="round"/>'
               f'<path d="{duct}" stroke="#86C25E" stroke-width="5" fill="none" stroke-linecap="round"/>')
    out.append(f'<path d="{LIVER_D}" fill="url(#moLiv)" stroke="#6E231B" stroke-width="1.2"/>'
               '<path d="M128,32 C126,58 120,86 112,110" stroke="#FFFFFF" stroke-opacity=".38" stroke-width="1.6" fill="none"/>'
               '<path d="M44,52 C58,40 80,35 104,35" stroke="#FFFFFF" stroke-opacity=".42" stroke-width="3.2" fill="none" stroke-linecap="round"/>')
    out.append(T(70, 100, "Liver", 10.5, 700, "#FFFFFF", "middle", italic=True))
    out.append(hexagon(93, 140, 4.8) + hexagon(98, 150.5, 4.8))     # toxins riding in the bile
    out.append(T(71, 152, "Gallbladder", 10, 700, BILE_TXT, "end", italic=True))
    # gut tube with its lining: folds are drawn, then the wall band is laid back over their
    # outer halves so only the part that bulges into the lumen shows.  The whole tube fades
    # out at both ends (moFade).
    out.append('<g mask="url(#moFade)">'
               f'<path d="{GUT_D}" stroke="#CF9984" stroke-width="{LUMEN + 25}" fill="none" stroke-linecap="round"/>'
               f'<path d="{GUT_D}" stroke="#EEC6B2" stroke-width="{LUMEN + 22}" fill="none" stroke-linecap="round"/>'
               f'<path d="{GUT_D}" stroke="#FCEBE2" stroke-width="{LUMEN}" fill="none" stroke-linecap="round"/>')
    out.append(villi())
    out.append(f'<path d="{GUT_D}" stroke="#EEC6B2" stroke-width="{LUMEN + 22}" fill="none" stroke-linecap="round" mask="url(#moRing)"/>'
               f'<path d="{GUT_D}" stroke="#DDA48E" stroke-width="{LUMEN + 1.6}" fill="none" stroke-linecap="round" mask="url(#moRing)"/>'
               f'<path d="{GUT_D}" transform="translate(0,{-(LUMEN / 2 + 5.5)})" stroke="#FFFFFF" stroke-opacity=".38" stroke-width="2.6" fill="none" stroke-linecap="round"/>'
               '</g>')
    out.append(T(88, gut_y(88) + LUMEN / 2 + 29, "Gut", 10.5, 700, "#9A5A45", "middle", italic=True))
    # unbound toxins: they enter with the bile (the duct meets the gut at x = 152), so they all
    # sit downstream of it; one escapes through the wall
    for (x, dy) in [(172, -6), (222, 6), (272, -5)]:
        out.append(hexagon(x, gut_y(x) + dy, 8.6))
    esc_x = 322
    esc_y = gut_y(esc_x) - LUMEN / 2 - 3
    out.append(hexagon(esc_x, esc_y, 8.6))
    # recirculation loop back to the liver
    # it ends where its arrowhead tip just meets the liver's left-lobe tip (edge near x = 212 at y = 63)
    p0, p1, p2, p3 = (esc_x + 2, esc_y - 12.5), (esc_x + 6, 120), (300, 66), (214, 63)
    out.append(f'<path d="M{_f(p0[0])},{_f(p0[1])} C{_f(p1[0])},{_f(p1[1])} {_f(p2[0])},{_f(p2[1])} {_f(p3[0])},{_f(p3[1])}" '
               'stroke="#C0392B" stroke-width="3" fill="none" stroke-dasharray="6 4.5" marker-end="url(#moArR)"/>')
    mx, my = _bez(p0, p1, p2, p3, 0.55)
    out.append(hexagon(mx, my, 6.2))
    # the binder you take: swallowed, it opens inside the gut and the binder spills out down the lumen
    cap_x = 364
    cap_y = gut_y(cap_x) + 1
    out.append(capsule_open(cap_x, cap_y, gut_angle(cap_x)))
    # the free binders are the size of the caught ones (R 12 against 13.6): a binder does not grow
    # when it catches a toxin
    for (x, dy, R, rot) in [(396, 7, 12, 12), (424, -7, 12, -14)]:
        out.append(crescent(x, gut_y(x) + dy, R, rot=rot))
    # its label sits in clear space above the gut; a leader points into the lumen
    out.append(leader(385, 154.5, cap_x - 2, cap_y - 10.8) + T(388, 152, "A binder you take", 10.5, 700, BINDER_TXT))
    # bound toxins in the second stretch
    for (x, dy, rot) in [(450, 4, 6), (500, -4, -4), (550, 4, 8), (598, -2, 0)]:
        out.append(caught(x, gut_y(x) + dy, r=8.6, R=13.6, rot=rot))
    # exit: the arrow leaves the open end of the gut, labelled where it points
    ey = gut_y(628)
    out.append(f'<path d="M624,{_f(ey)} H714" stroke="#2B3236" stroke-width="3.4" marker-end="url(#moArK)"/>')
    out.append(T(694, ey - 9, "To stool", 10.5, 700, INK, "middle"))
    # captions, numbered in reading order.  Kerkadi et al. 1998: mycotoxins leave the liver in bile, are
    # partly reabsorbed (enterohepatic recirculation), and a bile-acid binder raised their fecal excretion.
    out.append(badge(236, 30, 1, c1) + T(250, 34, "Your liver packs toxins into bile.", 10.5, 700, INK))
    out.append(badge(176, 114, 2, c1) + T(190, 110, ["Bile carries them", "into the gut."], 10.5, 700, BILE_TXT))
    out.append(badge(352, 104, 3, c1) + T(366, 100, ["No binder? Some toxins soak", "back in and return to the liver."], 10.5, 700, TOXIN_TXT))
    cy4 = H - 13
    out.append(badge(408, cy4, 4, c1) + T(422, cy4 + 3.8, "Binders hold on, so the toxins leave with stool.", 10.5, 700, BINDER_TXT))
    # key
    # rows 22 px apart, so the two crescent swatches keep a 4 px gap; the box ends flush with the
    # column's right edge (731) and carries the same side padding left and right of its labels
    kb, _ = key_box(568, 10, [(hexagon(0, 0, 7), "Mycotoxin"), (crescent(-2.6, 0, 9.5), "Binder"),
                              (caught(-3.4, 0, r=5.2, R=8.2), "Toxin caught by a binder"),
                              # drawn like the duct: dark rim under the light core, square ends
                              ('<path d="M-8,0 H7" stroke="#4E8A33" stroke-width="9"/>'
                               '<path d="M-8,0 H7" stroke="#86C25E" stroke-width="5"/>', "Bile"),
                              ('<path d="M-9,0 H5" stroke="#C0392B" stroke-width="2.6" stroke-dasharray="4 3"/>'
                               '<path d="M3,-4.5 L9.5,0 L3,4.5 Z" fill="#C0392B"/>', "Soaks back in")],
                    163, row_h=22)
    out.append(kb)
    return svg(_f(W), H, "".join(out), "How a binder helps carry mycotoxins out of the body")


# ============================================================ front page
EYE = ('<path d="M6 34c7-11 16-16 26-16s19 5 26 16c-7 11-16 16-26 16S13 45 6 34z"/><circle cx="32" cy="34" r="8"/>'
       '<path d="M19 9l3 5M32 6v6M45 9l-3 5"/>')
# Lungs: a windpipe that forks into two bronchi, each entering its own tapered lobe.  (The kit
# icon fused the lobes under one stem and read as a peach at 0.36 in.)
LUNGS = ('<path d="M32 7v17M32 24l-6 6M32 24l6 6"/>'
         '<path d="M26 22c-8-1-15 9-16 22-1 7 2 11 7 11 6 0 9-4 9-11V22z"/>'
         '<path d="M38 22c8-1 15 9 16 22 1 7-2 11-7 11-6 0-9-4-9-11V22z"/>')
INHALER = ('<path d="M31 25V10a4 4 0 0 1 4-4h4a4 4 0 0 1 4 4v15"/>'
           '<path d="M27 25h20v25a4 4 0 0 1-4 4H14a4 4 0 0 1-4-4v-6a4 4 0 0 1 4-4h13z"/><path d="M27 40v14"/><path d="M4 41h.5M2.5 47h.5M4 53h.5"/>')
# Joint (a knee, front view): the upper bone ends in two rounded knobs, the lower bone in a flat
# top, a clear gap between them, and three short ache rays on each side of the gap.  (The kit
# "bone" is a whole bone, not a joint, and was the one symptom icon that did not show its symptom.)
JOINT = ('<path d="M26 4v14c0 2-6 3-6 8 0 3 2 5 5 5 3 0 5-2 7-2s4 2 7 2c3 0 5-2 5-5 0-5-6-6-6-8V4"/>'
         '<path d="M21 40c0-1.2 1-2 2-2h18c1 0 2 .8 2 2 0 3-5 4-5 7v13M26 60V47c0-3-5-4-5-7"/>'
         '<path d="M13 29.5l-6-3M12 34.5H5M13 39.5l-6 3M51 29.5l6-3M52 34.5h7M51 39.5l6 3"/>')


def own_icon(body, size, sw):
    return (f'<svg class="ic" viewBox="0 0 64 64" style="width:{size};height:{size}" fill="none" stroke="currentColor" '
            f'stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{body}</svg>')


CSS = r"""
.mo-front{display:flex;flex-direction:column}
.mo-front .mo-h{font:900 12pt Merriweather,Georgia,serif;color:var(--c1);letter-spacing:.02em;margin:0 0 0.04in}
.mo-front .mo-art svg{display:block;width:100%;height:auto}
.mo-front .mo-signs{display:grid;grid-template-columns:1fr 1fr;gap:0.12in;margin:0 0 0.08in}
.mo-front .mo-grp{background:var(--tint);border:1px solid #E4DCEF;border-radius:8px;padding:4px 6px 5px}
.mo-front .mo-grp h4{margin:0 0 3px;text-align:center;font:800 7.4pt Inter,sans-serif;letter-spacing:.12em;
  text-transform:uppercase;color:var(--c1)}
.mo-front .mo-ics{display:grid;grid-template-columns:repeat(4,1fr)}
.mo-front .mo-ics div{display:flex;flex-direction:column;align-items:center;text-align:center;color:var(--c1)}
.mo-front .mo-ics span{font-size:8pt;color:#3A4247;line-height:1.15;margin-top:2px}
.mo-front .mo-two{display:grid;grid-template-columns:1fr 400px;gap:15px;align-items:stretch;margin-bottom:0.08in}
.mo-front .mo-col{display:flex;flex-direction:column}
.mo-front .mo-steps{display:flex;flex-direction:column;gap:6px}
.mo-front .mo-step{display:flex;gap:8px;align-items:flex-start}
.mo-front .mo-step .n{flex:none;width:0.26in;height:0.26in;border-radius:50%;background:var(--c1);color:#fff;
  font:800 9pt Inter,sans-serif;display:flex;align-items:center;justify-content:center}
.mo-front .mo-step b{font:800 9.4pt Inter,sans-serif;color:var(--deep);display:block}
.mo-front .mo-step span{display:block;font-size:8.3pt;color:#3A4247;line-height:1.3}
.mo-front .mo-stat{display:flex;gap:10px;align-items:center;background:var(--soft);border-radius:8px;padding:6px 10px;margin-top:auto}
.mo-front .mo-steps{margin-bottom:8px}
.mo-front .mo-stat b{font:900 19pt Merriweather,Georgia,serif;color:var(--c1);line-height:1;white-space:nowrap}
.mo-front .mo-stat span{font-size:8.3pt;line-height:1.3;color:#2B3236}
/* BACK PAGE (back-page pass 2026-11-03).  Reached through the marker span in the lifestyle title,
   so the rules touch only this sheet's back, in its own file and in the all-sheets bundle.
     - lifestyle cells keep the kit's 0.1in gap (closer, the long lines of two cells read across as
       one) and the grid reaches 0.1in into the band's side padding, so every title sets on one line;
     - each "In each serving" block sits on its dose bar (the .what box is a column with the
       facts pushed to its foot), so the five facts blocks end on one line;
     - every dose bar is one height with its text centred, so the bars form one row;
     - the Morning box takes its natural width (its longest line, "Binder Pro 2 capsules,
       mid-morning", is 159 px), so its five lines never wrap; the other two share the rest. */
.sheet.back:has(.mo-back) .lifes{gap:0.1in;margin:0 -0.1in}
.sheet.back:has(.mo-back) .col .what{display:flex;flex-direction:column}
.sheet.back:has(.mo-back) .col .what .key{margin-top:auto}
.sheet.back:has(.mo-back) .col .dose{min-height:0.35in;display:flex;flex-direction:column;justify-content:center}
.sheet.back:has(.mo-back) .col .pick{padding-left:0.05in;padding-right:0.05in}
.sheet.back:has(.mo-back) .duo{grid-template-columns:1.55fr 1fr}
.sheet.back:has(.mo-back) .rhythm{grid-template-columns:max-content 1fr 1fr}
"""


def front(t, ed):
    s = lambda body: own_icon(body, "0.36in", 2.9)
    k = lambda name: icon(name, "0.36in", sw=2.9)
    grp_a = [(k("nose"), "Stuffy nose"), (s(LUNGS), "Cough, wheeze"), (s(EYE), "Itchy, red eyes"),
             (s(INHALER), "Asthma flares")]
    grp_b = [(k("battery"), "Fatigue"), (k("brain"), "Brain fog"), (k("headache"), "Headaches"), (s(JOINT), "Joint aches")]
    cells = lambda items: "".join(f"<div>{ic}<span>{lab}</span></div>" for ic, lab in items)
    # CDC Mold: Basic Facts + IOM 2004 for group A; group B is what patients commonly report
    signs = ('<div class="mo-signs">'
             f'<div class="mo-grp"><h4>Breathing and allergy</h4><div class="mo-ics">{cells(grp_a)}</div></div>'
             f'<div class="mo-grp"><h4>Many people also report</h4><div class="mo-ics">{cells(grp_b)}</div></div></div>')
    steps = [
        # EPA: dry within 24-48 hours; more than about 10 sq ft, follow EPA's remediation guide (a pro)
        ("Remove the exposure", "Find and fix the water first. Dry any leak within 24 to 48 hours. "
                                "Mold over 10 square feet? Hire a pro."),
        ("Keep bile flowing", "Your liver packs toxins into bile. Bile carries them into the gut on their way out."),
        ("Bind toxins in the gut", "Fiber and binders hold on to toxins so they leave with stool. "
                                   "Aim for an easy bowel movement every day."),
        # sinus care is a clinician's call in both editions (a pharmacist does not examine sinuses)
        ("Check the sinuses", "Stuffy long after you leave the building? Ask a clinician whether your sinuses need care too."),
        ("Treat fungal overgrowth only if found", "Antifungal care is for when a clinician confirms it."),
    ]
    st = "".join(f'<div class="mo-step"><div class="n">{i + 1}</div><div><b>{a}</b><span>{b}</span></div></div>'
                 for i, (a, b) in enumerate(steps))
    # Mudarri and Fisk 2007: 21% (4.6 million) of U.S. current asthma cases attributable to home dampness and mold
    stat = ('<div class="mo-stat"><b>1 in 5</b><span>U.S. asthma cases is tied to dampness and mold at home, '
            'researchers estimate.</span></div>')
    return ('<div class="mo-front">' + signs
            + '<div class="mo-two">'
            f'<div class="mo-col"><h3 class="mo-h">YOUR RECOVERY, IN ORDER</h3><div class="mo-steps">{st}</div>{stat}</div>'
            f'<div class="mo-col"><h3 class="mo-h">WHERE MOLD HIDES AT HOME</h3><div class="mo-art">{art_house(t)}</div></div>'
            '</div>'
            '<h3 class="mo-h">WHY BINDERS MATTER</h3>'
            f'<div class="mo-art">{art_binder(t)}</div></div>')


SHEET = {
    "slug": "mold", "code": "ND-IM-302", "order": 9, "theme": "immune", "series": "Immune Health Series",
    "title": "Mold Illness", "sub": "Mycotoxin exposure and recovery",
    # Fisk et al. 2007 meta-analysis: damp, moldy homes, about 30-50% increases in
    # respiratory and asthma-related outcomes.  CDC/WHO: some molds make mycotoxins.
    "intro": ("Mold grows wherever water lingers: a slow roof leak, a damp crawl space, an overflowing AC drip pan. "
              "Some molds make <b>mycotoxins</b>, natural toxins carried on spores and dust. Damp, moldy homes raise the "
              "chances of coughing, wheezing and asthma symptoms by about <b>30 to 50 percent</b>, and many people also "
              "report tiredness, headaches and brain fog. The signs are broad, so mold is easy to miss. Recovery starts "
              "with removing the exposure."),
    "front": front,
    "css": CSS,
    "back": {
        # the empty span marks this sheet's back page for the scoped CSS (.sheet.back:has(.mo-back))
        "life_title": 'Lifestyle Recommendations<span class="mo-back"></span>', "style": "circle",
        "life": [
            # NutriDyn educator: "Mold Care ~ Preparation Plan (While Waiting on Labs and Home/Work
            # Samples)": support starts while the home and the workplace are checked
            ("house", "Test home &amp; work", "Start the plan while home and work are checked for mold."),
            # EPA, A Brief Guide to Mold, Moisture, and Your Home: indoor humidity ideally 30 to 50 percent
            ("meter", "Dry the air", "Keep indoor humidity at 30 to 50 percent. A dehumidifier helps."),
            # EPA, Guide to Air Cleaners in the Home: HEPA filters capture mold spores; HEPA vacuums in cleanup
            ("filter", "Filter it", "HEPA air purifiers and HEPA vacuums trap mold spores."),
            # WHO, Mycotoxins fact sheet: maize and groundnuts (aflatoxins), cereals in storage and dried
            # vine fruit (ochratoxin A) are the main sources; spices, coffee and wine are smaller ones
            ("jar", "Limit risky foods", "Peanuts, corn, stored grains and dried fruit can carry mycotoxins."),
            # Dietary Guidelines 2020-2025: 22 to 34 g fiber a day for adults; front step 3: fiber binds
            ("wheat", "More fiber", "Fiber holds on to toxins in bile. Aim for about 30&nbsp;g a day."),
            # ND1610: binders work by "elimination through the stool"; the educator's preparation plan:
            # "OPTIONAL Cape Aloe/Mag Citrate 1-4 before sleep"
            ("gut", "Stay regular", "Binders leave with stool. Constipated? Ask about magnesium citrate."),
        ],
        # NutriDyn's own mold protocols first: KBMO Mycotoxin Protocol ND1610 (Binder Pro, GI Defend) and
        # a NutriDyn educator's mold plans (Lipo-Flow, "Glutathione/NAC", Mito Recharge).  They also cover
        # the competitor's categories: binders (Binder Pro), bitter herbs and bile (Lipo-Flow: artichoke,
        # dandelion, gentian), mitochondrial support (Mito Recharge); NutriDyn has no phosphatidylcholine
        # product, and the protocol's glutathione takes that place.  Timing: Binder Pro goes mid-morning and
        # mid-evening (the educator's grids), 2 hours from food, other supplements and medicine; every other
        # product sits at a meal, GI Defend in the morning.  Claim bullets start with their verb, so the kit
        # ends each one with the diamond tied to the FDA line.  Facts, doses, sources: products.d/mold.json.
        "cols": [
            # ND1610's lead product; ND1141 Rev. 12/25 "Supports healthy detoxification"; Asher's email to a
            # practice, 2026-10-29: "Binder Pro has no charcoal or clay"
            {"p": "mo_binder_pro", "need": "Bind toxins in the gut", "needsub": "pectin, Humiplex, chlorella",
             "start": True, "dose": "dose_from_db",
             "bullets": ["Helps carry toxins out with stool", "No charcoal or clay"]},
            # ND850 Rev. 12/24: "Supports healthy gut barrier function"; "binding, neutralizing, and removing
            # toxins from the gut".  Not called a binder here: the 2-hour rule is Binder Pro's alone
            {"p": "mo_gi_defend", "need": "Guard the gut lining", "needsub": "bovine immunoglobulins",
             "dose": "dose_from_db",
             "bullets": ["Supports a healthy gut barrier", "Helps neutralize toxins in the gut"]},
            # ND606 Rev. 4/26: "Promote healthy bile processes", "Promote healthy liver function"
            {"p": "mo_lipo_flow", "need": "Keep bile flowing", "needsub": "artichoke, gentian bitters",
             "dose": "dose_from_db",
             "bullets": ["Promotes healthy bile flow", "Supports healthy liver function"]},
            # ND971 Rev. 8/24: "Supports healthy glutathione levels", "Detox Support"; glutathione is the
            # liver's packing step (conjugation) before toxins leave in bile (front caption 1)
            {"p": "mo_glutathione", "need": "Top up glutathione", "needsub": "the detox antioxidant",
             "dose": "dose_from_db",
             "bullets": ["Helps the liver pack toxins into bile", "Supports healthy glutathione levels"]},
            # ND812 Rev. 2/25: "Promote healthy mitochondria", "Support healthy detoxification capacity"
            {"p": "mo_mito", "need": "Fuel your cells", "needsub": "mitochondrial support",
             "dose": "dose_from_db",
             "bullets": ["Promotes healthy mitochondria", "Supports healthy detox capacity"]},
        ],
        "rx": {
            # Both editions go to patients, worded for who checks them: a pharmacist checks interactions and
            # nutrient losses, a provider orders labs, refers and adjusts.
            "pharmacy": [
                # Binder spacing rule: the educator's grids keep the binder between meals, away from the meal-time
                # supplements; humic-fulvic acids and chlorella are chelators (ND1141), pectin a soluble fiber
                "<b>Binders can catch medicines and nutrients too.</b> Keep Binder Pro 2 hours from food, "
                "other supplements and every medicine. {Who} can help you time it.",
                # ND812: 250 mcg vitamin K1 per 3 capsules; Ohkawa 1995 (chlorella blunted warfarin);
                # Rohde 2007 (over 250 mcg a day lowers warfarin sensitivity)
                "<b>On warfarin?</b> Vitamin K can weaken it: Mito Recharge has 250&nbsp;mcg vitamin K1, and "
                "Binder Pro&rsquo;s chlorella adds some. Ask {who} first.",
                # FDA labels: azole antifungals are strong CYP3A4 inhibitors with long interaction lists
                "<b>Prescribed an antifungal?</b> Many interact with other medicines. Show {who} your full list, "
                "supplements included.",
            ],
            "practitioner": [
                "<b>Binders can catch medicines and nutrients too.</b> Keep Binder Pro 2 hours from food, "
                "other supplements and every medicine.",
                # the educator's "Areas to Further Assess": Mycotoxin Urine Assessment, Mold Antibody Assessment,
                # Organic Acid Testing (NutriDyn sells the KBMO kits; ND1610 is the KBMO follow-up sheet);
                # Asher refers CIRS-level cases to CIRS-trained clinicians (Gmail 18a44129ee7139f6)
                "<b>Testing guides the plan.</b> {Who} may order a urine mycotoxin, mold antibody or organic "
                "acids test, then adjust your plan or refer you to a specialist.",
                # ND812 K1; Ohkawa 1995; Rohde 2007; Sconce 2007 (a steady daily intake steadies the INR)
                "<b>On warfarin?</b> Vitamin K can weaken it: Mito Recharge has 250&nbsp;mcg vitamin K1, and "
                "Binder Pro&rsquo;s chlorella adds some. {Who} may check your INR sooner.",
            ],
        },
    },
}
