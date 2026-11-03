"""High Blood Pressure (ND-CM-202), Metabolic Health Series.

Self-contained sheet module: the front art, the front copy and the back data all live
here (no legacy sheets.py / art.py imports).  Front, top to bottom:
  intro -> nitric-oxide pathway (4 numbered steps) beside a tight-vs-relaxed artery
  with its KEY -> risk-factor icons -> "reading your numbers" + "measure it right"
  beside the AHA/ACC category table.
Back: unchanged from the first draft (the back-page pass revises the products, the
Provider/Pharmacist check and the lifestyle band).

Every number stated on the front carries a source comment next to it.
Edition wording: "{who}" / "{Who}" become "your provider" or "your pharmacist" (build.ed_text).
"""
import re

from svgkit import T, svg
from kit import ICONS, icon

SLUG = "high-blood-pressure"

# ------------------------------------------------------------------ vessel colours (all named in the KEY)
OUTER = "#EDD3AE"      # outer layer of the artery wall (connective tissue): warm tan, CIE76 dE 16.6 from LUMEN
OUTER_LN = "#D2B286"   # its outline
TIGHT = "#9A2924"      # tight (contracted) muscle wall
TIGHT_LN = "#741A16"   # muscle-fibre lines, tight wall
RELAX = "#D27A6C"      # relaxed muscle wall
RELAX_LN = "#B85A4D"   # muscle-fibre lines, relaxed wall
LUMEN = "#F9E1DA"      # blood inside the vessel (shown in the "Blood flow" swatch)
LUMEN_LN = "#E3B4A8"   # outline of the pale "Blood flow" swatch, so it shows on the white KEY
PUSH = "#3A1411"       # arrows: blood pushing on the vessel wall (pressure)
INK = "#2B3236"

# ------------------------------------------------------------------ this sheet's icons (64 x 64 grid, stroke style)
# Open mouth with the tongue out: upper lip, mouth line, a lower lip the tongue hangs over (so the mouth
# reads as open), and four tiny rod-shaped bacteria on the tongue in green (friendly bacteria), each
# 5.2 x 2.4 units, scattered at four angles.  No outline on the rods; placed by a clearance search
# (tools/rods.py in the agent scratch folder): every rod sits 2.6+ units clear of the others and of the
# tongue's and mouth line's inner stroke edge, so they stay separate rods at print size.
BUG = "#2E7D5B"        # the friendly tongue bacteria
_RODS = [(28.2, 39.1, 32), (35.8, 39.8, 16), (32.5, 34.6, -10), (32.2, 45.0, -26)]
IC_TONGUE = ('<path d="M7 25c5-6 11-9 16-8 3 .6 6 2.4 9 2.4s6-1.8 9-2.4c5-1 11 2 16 8"/>'      # upper lip
             '<path d="M7 25c14 4 36 4 50 0"/>'                                                 # mouth line
             '<path d="M7 25c4 11 13 17 25 17s21-6 25-17"/>'                                    # lower lip
             '<path d="M20 28v9c0 9 5.5 15 12 15s12-6 12-15v-9" fill="#F6C9C1"/>'               # tongue, over the lip
             f'<g fill="{BUG}" stroke="none">'
             + "".join(f'<rect x="-2.6" y="-1.2" width="5.2" height="2.4" rx="1.2" transform="translate({x} {y}) rotate({a})"/>'
                       for x, y, a in _RODS) + '</g>')
IC_VESSEL = ('<path d="M5 25c14 0 22-8 54-11"/><path d="M5 39c14 0 22 8 54 11"/>'
             '<path d="M13 32h30"/><path d="M37 25.5l7 6.5-7 6.5"/>')
IC_SOFA = ('<path d="M14 31v-7a6 6 0 0 1 6-6h24a6 6 0 0 1 6 6v7"/>'
           '<path d="M8 36a5 5 0 0 1 10 0v4h28v-4a5 5 0 0 1 10 0v11H8z"/><path d="M12 47v6M52 47v6"/>')
# Cigarette: a long body with a filter band, two curls of smoke rising 21+ units from the lit end, so the
# glyph fills about 38 of the 64 units in height like the scale, sofa and kidneys (the kit's flat bar
# filled only 19 and read as a battery).
IC_SMOKE = ('<rect x="6" y="40" width="46" height="10" rx="2.5"/><path d="M18 40v10"/>'
            '<path d="M45.5 36c-4-4-4-8 0-12s4-8 0-12"/>'                 # smooth smoke waves, 24 and 20 units tall
            '<path d="M54 34c-3.5-3.5-3.5-6.5 0-10s3.5-6.5 0-10"/>')
# Birth control pills: a blister card with a 2 x 3 grid of pills.
IC_PILLS = ('<rect x="13" y="9" width="38" height="46" rx="6"/>'
            + "".join(f'<circle cx="{x}" cy="{y}" r="4.3"/>' for y in (21, 32, 43) for x in (25, 39)))


def _noslash(name):
    """A kit icon without its coral 'avoid' slash: on a list of RISKS the slash would read as 'no salt'."""
    return re.sub(r'<path class="x"[^>]*/>', "", ICONS[name])


def _kidneys():
    """The kit's two kidney beans, each 10% smaller about its own centre and moved 2.8 units outward,
    so a clear 3.6-unit gap shows between them (touching beans read as a walnut).  The group stroke is
    scaled up to match, so the line weight stays 2.8 like every other risk icon."""
    left, right = re.findall(r'<path d="[^"]+"/>', ICONS["kidney"])
    return (f'<g transform="translate(-2.8 0) translate(21.4 32) scale(.9) translate(-21.4 -32)" stroke-width="3.111">{left}</g>'
            f'<g transform="translate(2.8 0) translate(42.6 32) scale(.9) translate(-42.6 -32)" stroke-width="3.111">{right}</g>')


def _ic(body, size, color="currentColor", sw=2.8):
    """Same markup as kit.icon, for this sheet's own icon bodies."""
    return (f'<svg class="ic" viewBox="0 0 64 64" style="width:{size};height:{size};color:{color}" fill="none" '
            f'stroke="currentColor" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round" '
            f'aria-hidden="true">{body}</svg>')


def _no_molecule(c1, c2):
    """Ball-and-stick nitric oxide (N=O) in the 64 grid.  The atoms are plain discs (no outline), r 11.5,
    with a 12-unit gap between them, so the double bond (the two bars) reads at print size instead of the
    pair fusing into one 'N-O' pill; letters 19.5 units = 7.3 pt, still inside the discs.  The two bond
    bars are 3.8 units thick (a touch lighter than the 4.8 outline) with a 6.2-unit white gap, measured
    at 0.8 mm on the 1200 dpi proof, so the '=' reads at arm's length."""
    return (f'<path d="M26 27h12M26 37h12" stroke="{c1}" stroke-width="3.8"/>'
            f'<circle cx="14.5" cy="32" r="11.5" fill="{c1}" stroke="none"/>'
            f'<circle cx="49.5" cy="32" r="11.5" fill="{c2}" stroke="none"/>'
            '<g stroke="none">' + T(14.5, 39.1, "N", 19.5, 800, "#fff", "middle")
            + T(49.5, 39.1, "O", 19.5, 800, "#fff", "middle") + "</g>")


# ------------------------------------------------------------------ small drawing helpers
def _varrow(x, tail, tip, stem, hw, hh, color=PUSH):
    """Vertical arrow from tail to tip (tip may be above or below the tail)."""
    d = 1 if tip > tail else -1
    base = tip - d * hh
    return (f'<path d="M{x},{tail} V{base + d * 0.5:.1f}" stroke="{color}" stroke-width="{stem}" stroke-linecap="round"/>'
            f'<path d="M{x - hw / 2:.1f},{base:.1f} L{x},{tip} L{x + hw / 2:.1f},{base:.1f} Z" fill="{color}"/>')


def _cell(x, y, s=1.0, rot=0):
    """Red blood cell: a biconcave disc seen at a slant (rim, dimple, highlight)."""
    return (f'<g transform="translate({x},{y}) rotate({rot}) scale({s})">'
            '<ellipse rx="15" ry="8.6" fill="#C9323B" stroke="#8E1C24" stroke-width="1.1"/>'
            '<ellipse rx="8.2" ry="3.9" fill="#A6242C"/>'
            '<path d="M-10,-4.6 Q0,-8.6 10,-4.6" fill="none" stroke="#fff" stroke-width="1.5" stroke-linecap="round" opacity=".42"/>'
            '</g>')


def _tag(x, y, w, h, text, size=12):
    """White flow arrow (rounded tail, pointed head) carrying its own label."""
    r, tip = h / 2, h * 0.62
    d = (f"M{x + r:.1f},{y - r:.1f} H{x + w - tip:.1f} L{x + w:.1f},{y:.1f} L{x + w - tip:.1f},{y + r:.1f} "
         f"H{x + r:.1f} A{r:.1f},{r:.1f} 0 0 1 {x + r:.1f},{y - r:.1f} Z")
    return (f'<path d="{d}" fill="#000" opacity=".10" transform="translate(0,1.6)"/>'
            f'<path d="{d}" fill="#fff"/>'
            + T(x + (w - tip) / 2 + r * 0.35, y + size * 0.36, text, size, 800, "#2B1412", "middle"))


def _seg_path(x0, x1, y0, y1, r, left_round):
    """Vessel segment outline: one end rounded (the vessel's end), the other cut square."""
    if left_round:
        return (f"M{x0 + r},{y0} H{x1} V{y1} H{x0 + r} A{r},{r} 0 0 1 {x0},{y1 - r} "
                f"V{y0 + r} A{r},{r} 0 0 1 {x0 + r},{y0} Z")
    return (f"M{x0},{y0} H{x1 - r} A{r},{r} 0 0 1 {x1},{y0 + r} V{y1 - r} "
            f"A{r},{r} 0 0 1 {x1 - r},{y1} H{x0} Z")


def _fibres(x0, x1, y_out, y_in, gap, slant, color, sw):
    """Muscle-fibre lines across one wall band (rings of muscle wrapping the vessel)."""
    out, x = [], x0 - abs(slant) - gap
    while x < x1 + gap:
        out.append(f'M{x:.1f},{y_out:.1f} L{x + slant:.1f},{y_in:.1f}')
        x += gap
    return f'<path d="{" ".join(out)}" stroke="{color}" stroke-width="{sw}" stroke-linecap="round" opacity=".6"/>'


def _segment(uid, x0, x1, top, bot, wall, left_round, fill, ln, gap, sw):
    """Outer layer + muscle wall (top and bottom bands) + lumen, clipped to the outline."""
    po = _seg_path(x0, x1, top, bot, 22, left_round)
    o_in = top + 10                    # outer layer is 10 units thick
    l_top, l_bot = o_in + wall, bot - 10 - wall
    slant = wall * 0.13
    return (f'<clipPath id="{uid}"><path d="{po}"/></clipPath>'
            f'<path d="{po}" fill="{OUTER}" stroke="{OUTER_LN}" stroke-width="1"/>'
            f'<g clip-path="url(#{uid})">'
            f'<rect x="{x0 - 2}" y="{o_in}" width="{x1 - x0 + 4}" height="{bot - 10 - o_in}" fill="{fill}"/>'
            + _fibres(x0, x1, o_in + 1.5, l_top - 1.5, gap, slant, ln, sw)
            + _fibres(x0, x1, bot - 11.5, l_bot + 1.5, gap, slant, ln, sw)
            + f'<rect x="{x0 - 2}" y="{l_top}" width="{x1 - x0 + 4}" height="{l_bot - l_top}" fill="{LUMEN}"/>'
            f'<path d="M{x0 - 2},{l_top} H{x1 + 2} M{x0 - 2},{l_bot} H{x1 + 2}" stroke="{ln}" stroke-width="1.2" opacity=".55"/>'
            '</g>'), l_top, l_bot


# ------------------------------------------------------------------ the picture
W, H = 760, 296


def art_bp(t):
    c1, c2, soft, deep = t["c1"], t["c2"], t["soft"], t["deep"]
    out = []

    # ---- left: the nitric-oxide pathway, four numbered steps.
    # Dietary nitrate -> oral bacteria (mostly on the tongue) reduce it to nitrite -> nitrite is reduced to NO
    # in the stomach, blood and tissues -> NO relaxes vascular smooth muscle (Lundberg, Weitzberg & Gladwin,
    # Nat Rev Drug Discov 2008;7:156-67; NIH Office of Dietary Supplements on dietary nitrate).  The vessel
    # lining also makes NO from L-arginine (eNOS); dietary nitrate is a second route, hence "a building block".
    steps = [
        ("beet", "Eat greens and beets", ["They are rich in nitrate,", "a building block for NO."]),
        ("tongue", "Mouth bacteria help", ["Friendly tongue bacteria", "turn nitrate into nitrite."]),
        ("no", "Your body makes NO", ["Nitrite becomes nitric oxide", "in your blood and tissues."]),
        ("vessel", "NO relaxes vessel walls", ["Vessels widen and blood", "flows with less pressure."]),
    ]
    CX, CW, CH, GAP, Y0 = 6, 236, 58, 18, 6
    bodies = {"beet": ICONS["beet"], "tongue": IC_TONGUE.replace("currentColor", c1), "vessel": IC_VESSEL,
              "no": _no_molecule(c1, c2)}
    for i, (ic, title, lines) in enumerate(steps):
        y = Y0 + i * (CH + GAP)
        out.append(f'<rect x="{CX}" y="{y}" width="{CW}" height="{CH}" rx="11" fill="{soft}" stroke="{c2}" stroke-width="1.5"/>')
        cx, cy = CX + 35, y + CH / 2
        out.append(f'<circle cx="{cx}" cy="{cy}" r="22" fill="#fff" stroke="{c1}" stroke-width="2"/>')
        out.append(f'<g transform="translate({cx - 16.5},{cy - 16.5}) scale(.515625)" fill="none" stroke="{c1}" '
                   f'stroke-width="4.8" stroke-linecap="round" stroke-linejoin="round">{bodies[ic]}</g>')
        # step number, badged on the icon ring: r 7 with a white halo (r 7 + 1); the halo stops 3.75 units
        # below the card border's lower edge (y + 0.75) and 4.4 units clear of the step-3 N disc;
        # the number is 10 units = 7.3 pt
        bx, by = cx - 17, y + 12.5
        out.append(f'<circle cx="{bx}" cy="{by}" r="7" fill="{c1}" stroke="#fff" stroke-width="2"/>'
                   + T(bx, by + 3.6, str(i + 1), 10, 800, "#fff", "middle"))
        tx = CX + 66
        out.append(T(tx, y + 17.5, title, 12.5, 800, deep))
        out.append(T(tx, y + 33.5, lines, 11, 500, "#33404A", lh=1.24))
        if i < 3:
            ay, mx = y + CH, CX + CW / 2
            out.append(f'<path d="M{mx},{ay + 1.5} V{ay + 8}" stroke="{c1}" stroke-width="3" stroke-linecap="round"/>'
                       f'<path d="M{mx - 6.5},{ay + 7.5} L{mx},{ay + 15.5} L{mx + 6.5},{ay + 7.5} Z" fill="{c1}"/>')

    # ---- right: one artery, tightened (left) vs relaxed (right)
    X0, X1 = 262, 756
    XM = (X0 + X1) / 2
    TOP, BOT = 46, 234
    vy = (TOP + BOT) / 2
    lx1, rx0 = XM - 5, XM + 5
    # A tightened artery narrows as a whole: the left tube is 8 units slimmer top and bottom (outer
    # diameter 172 vs 188) and its thick muscle wall (44 vs 24) squeezes the channel down.
    SQ = 8
    seg_l, lt, lb = _segment("hbp-cl", X0, lx1, TOP + SQ, BOT - SQ, 44, True, TIGHT, TIGHT_LN, 7.5, 1.7)
    seg_r, rt, rb = _segment("hbp-cr", rx0, X1, TOP, BOT, 24, False, RELAX, RELAX_LN, 15, 1.6)
    out += [seg_l, seg_r]
    out.append(f'<path d="M{XM},{TOP - 3} V{BOT + 3}" stroke="#AEB5BA" stroke-width="2" stroke-dasharray="5 4"/>')

    # headings, with the nitric-oxide bridge between them
    lc, rc = (X0 + lx1) / 2, (rx0 + X1) / 2
    out.append(T(lc, 20, "UNHEALTHY", 12, 800, INK, "middle", ls=0.8))
    out.append(T(lc, 35.5, "vessel tightened", 10.5, 600, "#5A646B", "middle", italic=True))
    out.append(T(rc, 20, "HEALTHY", 12, 800, INK, "middle", ls=0.8))
    out.append(T(rc, 35.5, "vessel relaxed", 10.5, 600, "#5A646B", "middle", italic=True))
    out.append(T(XM, 20.5, "nitric oxide", 11, 800, c1, "middle"))
    out.append(f'<path d="M{XM - 46},30.5 H{XM + 40}" stroke="{c1}" stroke-width="2.4" stroke-linecap="round"/>'
               f'<path d="M{XM + 38},25 L{XM + 48},30.5 L{XM + 38},36 Z" fill="{c1}"/>')

    # pressure arrows: blood pushing out on the wall; bigger where pressure is high
    # six denser columns at x 302 to 462, so both red cells (x 284 and 483) sit between columns and the
    # arrows never seem to sprout from a cell
    for k in range(6):
        x = 302 + k * 32
        out.append(_varrow(x, vy - 15.5, lt, 3.2, 11, 9))
        out.append(_varrow(x, vy + 15.5, lb, 3.2, 11, 9))
    for k in range(5):
        x = rx0 + 27 + k * 47
        out.append(_varrow(x, rt + 13, rt, 2.2, 8, 6.5))
        out.append(_varrow(x, rb - 13, rb, 2.2, 8, 6.5))

    # red blood cells: squeezed into the narrow vessel, roomy in the relaxed one
    for (x, dy, r) in [(X0 + 22, 1, 8), (lx1 - 21, -1, -10)]:
        out.append(_cell(x, vy + dy, 0.9, r))
    for (x, dy, r) in [(rx0 + 40, -27, 12), (rx0 + 128, -32, -8), (rx0 + 206, -25, 16),
                       (rx0 + 70, 28, -14), (rx0 + 158, 33, 6), (rx0 + 222, 26, -6)]:
        out.append(_cell(x, vy + dy, 0.9, r))

    # flow arrows, labelled as flow (the KEY's "Blood flow"); only the dark arrows stand for pressure
    out.append(_tag(lc - 75, vy, 150, 21, "Flow: high pressure", 11))
    out.append(_tag(rc - 80.5, vy, 161, 21, "Flow: normal pressure", 11))

    # ---- KEY: names every symbol and colour in the vessel
    KY, KH = 244, 48
    out.append(f'<rect x="{X0}" y="{KY}" width="{X1 - X0}" height="{KH}" rx="8" fill="#fff" stroke="#CFD6DA" stroke-width="1.4"/>')
    out.append(T(X0 + 14, KY + KH / 2 + 3.8, "KEY", 10.5, 800, INK, ls=1.2))
    out.append(f'<path d="M{X0 + 50},{KY + 9} V{KY + KH - 9}" stroke="#DDE2E5" stroke-width="1.2"/>')
    r1, r2 = KY + 15, KY + 33

    def item(x, y, sw, label):
        return f'<g transform="translate({x + 12},{y})">{sw}</g>' + T(x + 30, y + 3.9, label, 11, 600, INK)

    def band(fill, ln, n):
        lines = "".join(f'<path d="M{-8 + j * (16 / max(n - 1, 1)):.1f},-5 l1.4,10" stroke="{ln}" stroke-width="1.5" opacity=".7"/>'
                        for j in range(n))
        return f'<rect x="-12" y="-6.5" width="24" height="13" rx="2" fill="{fill}"/>{lines}'

    flow_sw = (f'<rect x="-13" y="-7.5" width="26" height="15" rx="3" fill="{LUMEN}" stroke="{LUMEN_LN}" stroke-width="1"/>'
               '<path d="M-8,-3 H3 L8,0 L3,3 H-8 Z" fill="#fff" stroke="#C9B3AD" stroke-width=".8"/>')
    # gaps label -> next swatch and the right padding measured even (about 27 units each, 400 dpi proof)
    c_1, c_2, c_3 = X0 + 62, X0 + 211, X0 + 379
    out.append(item(c_1, r1, _cell(0, 0, 0.72), "Red blood cell"))
    out.append(item(c_1, r2, band(TIGHT, TIGHT_LN, 4), "Tight muscle wall"))
    # big + small arrow; the label says what the size means (big arrow = high pressure on the wall)
    out.append(item(c_2, r1, _varrow(-5, 7.5, -7.5, 2.8, 9, 7.5) + _varrow(7, 7.5, -2.5, 2, 6.5, 5.5), "Pressure (big = high)"))
    out.append(item(c_2, r2, band(RELAX, RELAX_LN, 2), "Relaxed muscle wall"))
    out.append(item(c_3, r1, flow_sw, "Blood flow"))
    out.append(item(c_3, r2, f'<rect x="-12" y="-6.5" width="24" height="13" rx="2" fill="{OUTER}" stroke="{OUTER_LN}" stroke-width="1"/>',
                    "Outer layer"))
    return svg(W, H, "".join(out), "How nitric oxide relaxes a blood vessel: a tight vessel under high pressure beside a relaxed one")


# ------------------------------------------------------------------ front page
# Risk factors: AHA "Know Your Risk Factors for High Blood Pressure" (family history, age, chronic kidney
# disease; inactivity, high-sodium diet, overweight, too much alcohol, sleep apnea, diabetes, smoking, stress)
# and CDC "High Blood Pressure Risk Factors".  "High BP in pregnancy, birth control pills": pregnancy itself
# is not the risk; high blood pressure during pregnancy (gestational hypertension, preeclampsia, which also
# raises later risk) and estrogen birth control pills, which can raise blood pressure, are: 2017 ACC/AHA
# guideline (Hypertension 2018;71:e13-e115, Table 13, oral contraceptives) and the 2025 AHA/ACC guideline
# (Hypertension 2025;82:e212-e316, hypertension in pregnancy); AHA "Know Your Risk Factors" (preeclampsia).
RISKS = [
    ("scale", "Extra weight"), ("salt", "High-sodium,<br>processed food"), ("sofa", "Sitting most<br>of the day"),
    ("glass", "Too much<br>alcohol"), ("smoke", "Smoking"), ("headache", "Chronic stress"),
    ("moon", "Poor sleep or<br>sleep apnea"), ("bloodsugar", "Diabetes"), ("kidney", "Kidney<br>disease"),
    ("pills", "High BP in pregnancy,<br>birth control pills"), ("dna", "Family<br>history"), ("age", "Increasing age")]
# Icons drawn here rather than straight from the kit: no "avoid" slash on the salt and glass (this row
# lists risks, not rules), a full cigarette with smoke, separated kidney beans, a birth control blister
# card.  The slashed kit versions stay on the back's lifestyle band.
RISK_ICONS = {"sofa": IC_SOFA, "salt": _noslash("salt"), "glass": _noslash("glass"), "smoke": IC_SMOKE,
              "kidney": _kidneys(), "pills": IC_PILLS}

# Blood pressure categories, mm Hg: 2025 AHA/ACC high blood pressure guideline (same cutoffs as the 2017 guideline).
BP_ROWS = [("#3E8E5B", "Normal", "under 120", "and", "under 80"),
           ("#E3B23C", "Elevated", "120 to 129", "and", "under 80"),
           ("#E27A2F", "Stage 1 high", "130 to 139", "or", "80 to 89"),
           ("#C2392E", "Stage 2 high", "140 or more", "or", "90 or more"),
           ("#6E1016", "<b>Severe</b>", "over 180", "and/or", "over 120")]


def front(t, ed):
    risk = "".join(f'<div class="hbp-rf">{_ic(RISK_ICONS[ic], "0.36in") if ic in RISK_ICONS else icon(ic, "0.36in", sw=2.8)}'
                   f'<span>{lab}</span></div>' for ic, lab in RISKS)
    rows = "".join(f'<tr><td><i style="background:{c}"></i>{cat}</td><td class="n">{a}</td><td class="c">{j}</td>'
                   f'<td class="n">{b}</td></tr>' for c, cat, a, j, b in BP_ROWS)
    table = ('<div class="hbp-sh">What the numbers mean</div>'
             '<table class="hbp-bp"><tr><th>Category</th><th>Top number</th><th></th>'
             f'<th>Bottom number</th></tr>{rows}</table>'
             # AHA: over 180/120, wait a few minutes and test again; still high, contact your doctor right away;
             # with chest or back pain, shortness of breath, numbness, weakness, vision change or trouble
             # speaking, call 911 (do not wait for it to come down).
             '<div class="hbp-alarm"><b>Over 180/120?</b> Rest a few minutes and check again. Still that high: call your '
             'doctor right away. With chest or back pain, shortness of breath, numbness, weakness, or trouble seeing or '
             'speaking, <b>call 911</b>.</div>'
             # 2017 ACC/AHA guideline, Table 13 (carried into 2025): decongestants and NSAIDs can raise blood pressure.
             '<div class="hbp-note"><b>Some medicines raise blood pressure,</b> like decongestants in cold remedies and pain relievers '
             'such as ibuprofen and naproxen. Ask {who} first.</div>'
             '<p class="hbp-fn">Categories in mm Hg: 2025 AHA/ACC high blood pressure guideline (same cutoffs as 2017).</p>')
    # 118 over 76: an example reading, "Normal" by the AHA/ACC table beside it (under 120 and under 80).
    nums = ('<div class="hbp-sh">Reading your numbers</div>'
            '<div class="hbp-frac"><div class="n top">118</div>'
            '<div class="d"><b>Systolic</b> (top number): the push on artery walls when your heart beats.</div>'
            '<div class="n">76</div>'
            '<div class="d"><b>Diastolic</b> (bottom number): the push between beats, while your heart rests.</div></div>'
            '<div class="hbp-sh hbp-sh2">Measure it right</div>'
            # AHA / AMA home blood pressure checklist
            '<ul class="hbp-ok"><li>No caffeine, smoking or exercise for 30 minutes. Rest 5 minutes first.</li>'
            '<li>Sit back supported, feet flat, legs uncrossed, arm at heart level.</li>'
            '<li>Cuff on bare skin. Take 2 readings, 1 minute apart. Write them down.</li>'
            '<li>Ask {who} to check your cuff size.</li></ul>'
            # write-in row, styled like the Patient name / Date fields in the page header; each box is
            # 0.42 in wide, room for a handwritten 3-digit number such as 142
            '<div class="hbp-log"><b>Reading</b><i></i><em>/</em><i></i><b class="g">Goal</b><i></i><em>/</em><i></i></div>')
    return ('<div class="hbp">'
            f'<div class="art hbp-art">{art_bp(t)}</div>'
            f'<div class="hbp-h">RISK FACTORS</div><div class="hbp-risk">{risk}</div>'
            f'<div class="hbp-low"><div class="hbp-nums">{nums}</div><div>{table}</div></div>'
            '</div>')


CSS = r"""
.hbp .hbp-h{font:900 12pt Merriweather,Georgia,serif;color:var(--c1);text-align:center;margin:0.09in 0 0.04in;letter-spacing:.02em}
.hbp .hbp-risk{display:grid;grid-template-columns:repeat(6,1fr);gap:0.05in 0.04in}
.hbp .hbp-rf{display:flex;flex-direction:column;align-items:center;text-align:center}
.hbp .hbp-rf .ic{color:#5F676E}
.hbp .hbp-rf span{font-size:8.2pt;line-height:1.18;color:#2F373C;margin-top:2px}
.hbp .hbp-low{display:grid;grid-template-columns:2.85in 1fr;gap:0.2in;margin-top:0.1in;align-items:start}
.hbp .hbp-sh{font:800 7.4pt Inter,sans-serif;letter-spacing:.14em;text-transform:uppercase;color:var(--c1);margin:0 0 3px}
.hbp .hbp-sh2{margin-top:0.07in}
.hbp .hbp-frac{display:grid;grid-template-columns:0.58in 1fr;column-gap:0.1in;align-items:center}
.hbp .hbp-frac .n{font:900 18pt/1.05 Merriweather,Georgia,serif;color:var(--c1);text-align:center;padding:1px 0 2px}
.hbp .hbp-frac .n.top{border-bottom:2.5px solid var(--c1)}
.hbp .hbp-frac .d{font-size:8.1pt;line-height:1.28;color:#2B3236}
.hbp .hbp-frac .d b{font-family:Merriweather,Georgia,serif;color:var(--deep);font-size:9pt}
.hbp .hbp-ok{list-style:none;margin:0;padding:0}
.hbp .hbp-ok li{position:relative;padding-left:15px;font-size:8.1pt;line-height:1.28;margin:0 0 2px;color:#2B3236}
.hbp .hbp-ok li::before{content:"";position:absolute;left:1px;top:3px;width:8px;height:4px;border-left:2px solid var(--c1);
  border-bottom:2px solid var(--c1);transform:rotate(-45deg)}
.hbp .hbp-log{display:flex;align-items:center;gap:4px;margin-top:0.07in;font-size:8pt;color:#2B3236}
.hbp .hbp-log b{font-weight:700;white-space:nowrap}
.hbp .hbp-log b.g{margin-left:6px}
.hbp .hbp-log i{display:block;width:0.42in;height:0.24in;border-radius:5px;background:#E9ECEE;border:1px solid #D6DBDF}
.hbp .hbp-log em{font-style:normal;color:#69737A;font-weight:600}
.hbp .hbp-bp{width:100%;border-collapse:collapse;font-size:8.4pt}
.hbp .hbp-bp th{background:var(--c1);color:#fff;padding:4px 8px;font-size:7.8pt;line-height:1.15;text-align:center}
.hbp .hbp-bp th:first-child{text-align:left}
.hbp .hbp-bp td{padding:2px 8px;border-bottom:1px solid #EEE3E1}
.hbp .hbp-bp tr:nth-child(even) td{background:var(--tint)}
.hbp .hbp-bp td.n{text-align:center;font-variant-numeric:tabular-nums;font-weight:700}
.hbp .hbp-bp td.c{text-align:center;color:#69737A;font-size:7.4pt}
.hbp .hbp-bp td i{display:inline-block;width:9px;height:9px;border-radius:50%;margin-right:7px;vertical-align:-1px}
.hbp .hbp-alarm{border:1.5px solid #C0392B;background:#FDF1EF;border-radius:7px;padding:2px 9px;margin-top:4px;
  font-size:8pt;line-height:1.3;color:#2B3236}
.hbp .hbp-alarm b{color:#A5281E}
.hbp .hbp-note{border-left:4px solid var(--c2);background:var(--tint);border-radius:0 6px 6px 0;padding:2px 9px;margin-top:4px;
  font-size:8pt;line-height:1.3;color:#2B3236}
.hbp .hbp-note b{color:var(--deep)}
.hbp .hbp-fn{font-size:7pt;color:#5E686F;line-height:1.3;margin:3px 0 0}
/* back page, scoped: only this sheet's back carries the .hbp-back marker */
.sheet.back:has(.hbp-back) .col .need{min-height:0.56in}
.sheet.back:has(.hbp-back) .slot li em{display:block}
"""

# ------------------------------------------------------------------ the sheet
SHEET = {
    "slug": SLUG, "code": "ND-CM-202", "order": 7, "theme": "metab", "series": "Metabolic Health Series",
    "title": "High Blood Pressure", "sub": "No symptoms, real risk",
    # 47.7% of U.S. adults have hypertension and 59.2% of them are aware of it (so about 4 in 10 are not):
    # CDC NCHS Data Brief No. 511 (Oct 2024), NHANES Aug 2021 to Aug 2023.
    "intro": ("Nearly <b>half of U.S. adults</b> have high blood pressure, and about <b>4 in 10</b> of them do not know it, "
              "because it rarely causes symptoms. Over the years, the extra force strains the heart, kidneys, brain and eyes "
              "and raises the risk of heart attack and stroke. One signal you can influence is <b>nitric oxide (NO)</b>, which "
              "tells blood-vessel walls to relax. What you eat, how you move, how you sleep and how you handle stress all "
              "change how much of it your body makes."),
    "front": front,
    "css": CSS,
    "back": {
        # the span marks this sheet's back page for the scoped CSS (.sheet.back:has(.hbp-back))
        "life_title": 'Lifestyle Recommendations<span class="hbp-back"></span>',
        "style": "circle",
        # Six tiles, titles 17 characters or fewer so every title sits on one line at 9.6 pt and all six
        # bodies start on the same line.  The lifestyle band is not run through the edition tokens, so it
        # names "your doctor", which is right in both editions.
        "life": [
            # Oler GLC 2025 HBP slide 12: nitrate-rich foods daily (beets, lettuce, spinach); avoid antiseptic
            # mouthwash (it blunts the nitrate-to-NO pathway).  Kapil V et al., Free Radic Biol Med 2013;55:93-100:
            # 7 days of antiseptic (chlorhexidine) mouthwash cut oral nitrite and raised systolic pressure 2 to 3.5
            # mm Hg.  The front's steps 1 and 2 (Lundberg, Weitzberg & Gladwin 2008).
            ("beet", "Boost your NO", "Eat leafy greens and beets daily. Skip antiseptic mouthwash: it kills the "
                                       "bacteria that help make NO."),
            # AHA "How much sodium should I eat per day?": no more than 2,300 mg a day, an ideal limit of 1,500 mg
            # for most adults, especially with high blood pressure; more than 70% comes from packaged, prepared and
            # restaurant food.  2025 AHA/ACC guideline (Hypertension 2025;82:e212-e316): under 1,500 mg optimal.
            ("salt", "Cut the sodium", "Stay under 2,300 mg a day; under 1,500 is even better. Most hides in "
                                       "packaged and restaurant food."),
            # AHA "Managing Weight to Control High Blood Pressure": losing even 5 to 10 pounds can help lower blood
            # pressure.  2017 ACC/AHA guideline Table 15: about 1 mm Hg lower for every 1 kg lost.
            ("scale", "Trim extra weight", "Losing even 5 to 10 pounds can help lower your numbers."),
            # AHA physical activity advice: 150 minutes a week of moderate activity (30 minutes, 5 days).
            # 2017 ACC/AHA Table 15: isometric resistance (hand grip, 4 x 2 minutes) 3 sessions a week.
            # Edwards JJ et al., Br J Sports Med 2023;57:1317-26: isometric work (wall squats, hand grips) gave the
            # largest resting blood pressure drop of any exercise type.  Oler GLC 2025: 20 to 30 minutes, 5 times a
            # week, plus resistance training; Johnson GLC 2026: 30 minutes 5 times a week plus resistance 2-3 times.
            ("dumbbell", "Move, then hold", "Walk briskly 30 minutes, 5 days a week. Add wall sits or hand grips "
                                            "3 times a week."),
            # AHA Life's Essential 8: 7 to 9 hours of sleep a night for adults; AHA: sleep apnea raises blood
            # pressure.  Oler GLC 2025: daily stress care with slow nasal breathing, humming, meditation, yoga.
            ("moon", "Sleep and breathe", "Sleep 7 to 9 hours. Slow breathing calms stress. Loud snoring? Ask your "
                                          "doctor about a sleep test."),
            # AHA: each cigarette raises blood pressure for a while and smoking damages the vessel lining.
            # 2025 AHA/ACC guideline: drink less alcohol, and none is best; Oler GLC 2019: under 1 drink a day.
            ("smoke", "Quit and cut back", "Quit smoking: it tightens your vessels. Cut back on alcohol; none "
                                           "is best."),
        ],
        # Products: Asher's High Blood Pressure Protocol (Gmail 17822c0dfc689947, 2021-03-11: Cardio Essentials
        # BP Support is "the formula"), Chad Oler's HBP slide (GLC 2025 slide 12, GLC 2019: Cardio Flow or Nitric
        # Boost for nitric oxide, CoQ10 100 mg, Omega Pure, magnesium glycinate) and the Johnson GLC 2026 list.
        # Five columns, the competitor's count; their categories map as: BP botanicals (hibiscus, lemon verbena,
        # green coffee) -> BP Support; L-citrulline for nitric oxide -> Nitric Boost; magnesium -> Magnesium
        # Glycinate; omega-3 -> Omega Pure; fucoidan (no NutriDyn equivalent) -> CoQ10, from the protocols.
        # Label facts, sizes, URLs and photo status for every product: products.d/high-blood-pressure.json.
        # Daily rhythm: morning Nitric Boost 3 + CoQ10 1; evening meal BP Support 3 + Omega 2; bedtime
        # Magnesium 1 = 10 pills.  Supplemental magnesium: Nitric Boost 120 mg + 1 Magnesium Glycinate 130 mg =
        # 250 mg a day, under the NIH ODS upper limit of 350 mg a day from supplements.
        "cols": [
            # Start here: Asher's named HBP formula and his rule "BP Support if looking purely for blood pressure
            # support"; ND681 compliance line and its nitric oxide mechanism (Benolea, MegaNatural-BP)
            {"p": "hbp_bp_support", "need": "Healthy pressure", "needsub": "olive leaf, black garlic, celery and grape seed",
             "start": True, "dose": "dose_from_db",
             "bullets": ["Supports healthy blood pressure already in the normal range",
                         "Olive leaf and grape seed support nitric oxide production"]},
            # ND1255: beet root nitrates convert to nitric oxide; "supports healthy nitric oxide production and
            # optimal blood flow"
            {"p": "hbp_nitric_boost", "need": "Boost nitric oxide", "needsub": "beet root and potassium nitrate",
             "dose": "dose_from_db",
             "bullets": ["The nitrate of step 1 on the front, in a capsule",
                         "Supports healthy nitric oxide and blood flow"]},
            # Asher's magnesium blast (2026-10-12, Hypertension 2025 meta-analysis of 38 RCTs): the benefit
            # tracked the starting state, so test first
            {"p": "hbp_mag_glycinate", "need": "Relax vessel walls", "needsub": "magnesium", "dose": "dose_from_db",
             "bullets": ["Supports relaxed, healthy vessel walls",
                         "Helps most when magnesium is low; ask your doctor to check"]},
            {"p": "hbp_omega_1000", "need": "Flexible vessels", "needsub": "omega-3s EPA and DHA", "dose": "dose_from_db",
             "bullets": ["Supports heart and blood vessel health", "Supports healthy triglyceride levels"]},
            # Statins lower CoQ10 (NIH NCCIH, Coenzyme Q10); ND270: "Supports blood flow and nitric oxide
            # production", "Supports energy production"
            {"p": "hbp_coq10", "need": "Power the heart", "needsub": "coenzyme Q10", "dose": "dose_from_db",
             "bullets": ["Statins can lower your CoQ10", "Supports heart energy and healthy blood flow"]},
        ],
        # Three medicine-and-nutrient notes per edition, worded for who checks them: pharmacists check
        # interactions and depletions; providers (MDs, DCs, NDs) order labs and adjust doses.
        # Sources: NIH ODS Magnesium fact sheet (loop and thiazide diuretics raise urinary magnesium loss;
        # spironolactone lowers it; impaired kidneys raise the risk of too much magnesium); NIH ODS Potassium
        # fact sheet (ACE inhibitors, ARBs and potassium-sparing diuretics can raise potassium); 2025 AHA/ACC
        # guideline (potassium-enriched salt substitutes except with CKD or potassium-raising drugs); NIH NCCIH
        # Coenzyme Q10 (statins lower CoQ10; the beta-blocker link rests on old in-vitro data, so it is left
        # out); NIH NCCIH Garlic and NIH ODS Omega-3 and Vitamin E fact sheets (may add to bleeding with blood
        # thinners); nitrate and nitric-oxide formulas can add to the blood-pressure drop from nitroglycerin and
        # PDE5 inhibitors (sildenafil, tadalafil).  Nitric Boost: 150 mg potassium per 3 capsules (ND1255).
        "rx": {
            "pharmacy": [
                "<b>Water pills</b> (HCTZ, chlorthalidone, furosemide) can drain magnesium and potassium, and "
                "<b>statins</b> lower CoQ10. Ask your doctor to check your levels.",
                "<b>Kidney disease, an ACE inhibitor, ARB or spironolactone?</b> Potassium can build up: no potassium "
                "pills or salt substitutes unless prescribed. Ask {who} before magnesium or Nitric Boost "
                "(150 mg potassium).",
                "<b>Blood thinners?</b> Garlic, fish oil and vitamin E may add to bleeding. <b>Nitroglycerin or ED "
                "pills</b> (sildenafil, tadalafil)? Nitric Boost may add to the pressure drop. Bring this sheet to "
                "your next doctor visit.",
            ],
            "practitioner": [
                "<b>Water pills</b> (HCTZ, chlorthalidone, furosemide) can drain magnesium and potassium, and "
                "<b>statins</b> lower CoQ10. Ask {who} to check your levels and kidney function.",
                "<b>Kidney disease, an ACE inhibitor, ARB or spironolactone?</b> Potassium can build up: no potassium "
                "pills or salt substitutes unless prescribed. Ask {who} before magnesium or Nitric Boost "
                "(150 mg potassium).",
                "<b>Keep a home log.</b> These formulas may add to blood pressure pills, nitroglycerin, ED pills and "
                "blood thinners, so {who} may adjust your doses. Never stop a medicine on your own. Bring this sheet "
                "to your pharmacist.",
            ],
        },
    },
}
