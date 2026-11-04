"""High Blood Pressure (ND-CM-202), Metabolic Health Series.

Self-contained sheet module: the front art, the front copy and the back data all live
here (no legacy sheets.py / art.py imports).  Front, top to bottom:
  intro -> nitric-oxide pathway (4 numbered steps) beside a tight-vs-relaxed artery (cut ends,
  inner lining that makes NO, NO molecules in the relaxed wall) with its KEY -> risk-factor
  icons -> "reading your numbers" + "measure it right" beside the AHA/ACC category table.
Back (2026-11-03 back-page pass, polish round 1 the same day, polish round 2 on 2026-11-04): six
lifestyle tiles aligned with the NutriDyn protocols (nitrate foods, fruit and no antiseptic mouthwash
from the NutriDyn GLC 2025 endothelial-dysfunction protocol, sodium, weight, walking with isometric
holds below a blood-pressure limit, sleep with daily slow breathing, smoking and alcohol); five
NutriDyn formulas from Asher's Hypertension protocol email and the NutriDyn GLC 2019 / 2025 / 2026
protocols (Cardio Essentials BP Support = Start here, Nitric Boost, Magnesium Glycinate, Omega Pure
EPA-DHA 1000, CoQ10 100 mg; label facts and sources in products.d/high-blood-pressure.json); a
10-pill daily rhythm; six medicine-and-nutrient notes, one list for both editions via {who}.  The
back never uses the abbreviation NO: nitric oxide is spelled out there, since NO is defined only on
the front.

Every number stated on the sheet carries a source comment next to it.
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
LINING = "#FFF3DA"     # inner lining (endothelium), the layer that makes NO: cream, dE 11.8 from LUMEN and OUTER
LINING_LN = "#D7B98E"  # its edge on the blood side
NUC = "#9A6B86"        # the lining cells' nuclei: small mauve dashes, as on a stained slide
LUMEN = "#F9E1DA"      # blood inside the vessel (shown in the "Blood flow" swatch)
LUMEN_LN = "#E3B4A8"   # outline of the pale "Blood flow" swatch, so it shows on the white KEY
HOLE = "#EDBFB4"       # the channel seen end-on in a cut face: a shade darker than LUMEN, so it reads as an opening
                       # (named in the KEY as "Cut end", with a mini cut face)
PUSH = "#3A1411"       # arrows: blood pushing on the vessel wall (pressure)
INK = "#2B3236"
LIN = 3.6              # lining thickness in units: the inner edge of each muscle band is drawn as lining
FR = 10                # half-width of the elliptical cut face at each outer end of the artery

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
# Back-page tile 6 ("Quit, cut back"): the same cigarette with an avoid slash, a no-smoking sign.  The kit's
# "smoke" (a flat bar, two straight bars and a slash) read as a crossed-out battery at print size.  The
# slash runs top left to bottom right, clear of the smoke curls (x 41.5 to 57.5, y 12 to 36); the kit's
# own slash (M10 56 54 10) would cut through them.  The lifestyle discs take kit icon names only, so the
# glyph is registered under a key no other sheet uses (fatty_liver.py and ibd.py register theirs the
# same way).
ICONS["hbp-smoke-x"] = IC_SMOKE + '<path class="x" d="M10 10 54 54"/>'
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


def _fibres(x0, x1, y_out, y_in, gap, slant, color, sw):
    """Muscle-fibre lines across one wall band (rings of muscle wrapping the vessel)."""
    out, x = [], x0 - abs(slant) - gap
    while x < x1 + gap:
        out.append(f'M{x:.1f},{y_out:.1f} L{x + slant:.1f},{y_in:.1f}')
        x += gap
    return f'<path d="{" ".join(out)}" stroke="{color}" stroke-width="{sw}" stroke-linecap="round" opacity=".6"/>'


def _nuclei(x0, x1, y, step=13.0, dx=0.0):
    """The lining cells' nuclei: one small flat mauve dash per cell along a lining band."""
    out, x = [], x0 + step / 2 + dx
    while x < x1 - 2:
        out.append(f'<ellipse cx="{x:.1f}" cy="{y:.2f}" rx="2.5" ry="1" fill="{NUC}"/>')
        x += step
    return "".join(out)


def _segment(uid, x0, x1, top, bot, wall, fill, ln, gap, sw, face):
    """One straight artery segment in long section, cut square at the divider: outer layer (10 units),
    muscle wall (its inner LIN units drawn as the cream lining, with nuclei) and the channel.
    face = "left" or "right" adds the cut face at that outer end: an ellipse FR wide with the same rings
    (outer layer, muscle, lining) round the channel opening, so the artery reads as a cut tube, not a
    capped one.  Returns (markup, channel top, channel bottom)."""
    o_in = top + 10
    l_top, l_bot = o_in + wall, bot - 10 - wall          # channel (blood) edges
    m_top, m_bot = l_top - LIN, l_bot + LIN              # muscle / lining boundaries
    slant = wall * 0.13
    w = x1 - x0
    out = [f'<clipPath id="{uid}"><rect x="{x0}" y="{top}" width="{w}" height="{bot - top}"/></clipPath>',
           f'<rect x="{x0}" y="{top}" width="{w}" height="{bot - top}" fill="{OUTER}" stroke="{OUTER_LN}" stroke-width="1"/>',
           f'<g clip-path="url(#{uid})">',
           f'<rect x="{x0 - 2}" y="{o_in}" width="{w + 4}" height="{bot - 10 - o_in}" fill="{fill}"/>',
           _fibres(x0, x1, o_in + 1.5, m_top - 1.2, gap, slant, ln, sw),
           _fibres(x0, x1, bot - 11.5, m_bot + 1.2, gap, slant, ln, sw),
           f'<rect x="{x0 - 2}" y="{m_top}" width="{w + 4}" height="{LIN}" fill="{LINING}"/>',
           f'<rect x="{x0 - 2}" y="{l_bot}" width="{w + 4}" height="{LIN}" fill="{LINING}"/>',
           _nuclei(x0, x1, m_top + LIN / 2 + 0.2), _nuclei(x0, x1, l_bot + LIN / 2 - 0.2, dx=6.5),
           f'<rect x="{x0 - 2}" y="{l_top}" width="{w + 4}" height="{l_bot - l_top}" fill="{LUMEN}"/>',
           f'<path d="M{x0 - 2},{m_top} H{x1 + 2} M{x0 - 2},{m_bot} H{x1 + 2}" stroke="{ln}" stroke-width="1" opacity=".55"/>',
           f'<path d="M{x0 - 2},{l_top} H{x1 + 2} M{x0 - 2},{l_bot} H{x1 + 2}" stroke="{LINING_LN}" stroke-width=".9"/>',
           '</g>']
    if face:
        xf, cy, r0 = (x0 if face == "left" else x1), (top + bot) / 2, (bot - top) / 2
        r_m, r_l, r_c = r0 - 10, r0 - 10 - wall + LIN, r0 - 10 - wall   # muscle, lining, channel radii

        def ell(ry, fill_, stroke="none", sw_=0, op=1):
            o = f' opacity="{op}"' if op != 1 else ""
            return (f'<ellipse cx="{xf}" cy="{cy}" rx="{FR * ry / r0:.2f}" ry="{ry:.2f}" fill="{fill_}" '
                    f'stroke="{stroke}" stroke-width="{sw_}"{o}/>')
        rings = [r_l + (r_m - r_l) * f for f in ((1 / 3, 2 / 3) if wall > 30 else (0.5,))]
        out += [ell(r0, OUTER, OUTER_LN, 1), ell(r_m, fill), *[ell(r, "none", ln, 0.9, 0.5) for r in rings],
                ell(r_l, LINING), ell(r_c, HOLE, LINING_LN, 0.9)]
    return "".join(out), l_top, l_bot


def _no_dot(x, y, rot, c1, c2):
    """A small nitric oxide molecule for the vessel and its KEY: the N and O discs of step 3, side by side,
    on a white halo so they read on the red muscle wall."""
    return (f'<g transform="translate({x},{y}) rotate({rot})">'
            '<circle cx="-3.6" r="4.4" fill="#fff"/><circle cx="3.6" r="4.4" fill="#fff"/>'
            f'<circle cx="-3.6" r="3.2" fill="{c1}"/><circle cx="3.6" r="3.2" fill="{c2}"/></g>')


# ------------------------------------------------------------------ the picture
W, H = 760, 300


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
    # four cards and three 18-unit gaps fill the 298-unit column, level with the KEY's bottom edge
    CX, CW, CH, GAP, Y0 = 6, 236, 59.5, 18, 6
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
        out.append(T(tx, y + 18, title, 12.5, 800, deep))
        out.append(T(tx, y + 34, lines, 11, 500, "#33404A", lh=1.24))
        if i < 3:
            ay, mx = y + CH, CX + CW / 2
            out.append(f'<path d="M{mx},{ay + 1.5} V{ay + 8}" stroke="{c1}" stroke-width="3" stroke-linecap="round"/>'
                       f'<path d="M{mx - 6.5},{ay + 7.5} L{mx},{ay + 15.5} L{mx + 6.5},{ay + 7.5} Z" fill="{c1}"/>')

    # ---- right: one artery, tightened (left half) vs relaxed (right half).  Layers, outside in: outer layer,
    # muscle, the thin inner lining (endothelium, which makes NO: Lundberg 2008 above; NIH NHLBI "What is
    # the endothelium"), then the blood channel.  Each outer end is a cut face showing the same rings.
    X0, X1 = 262, 756                  # outer extent, faces included (the KEY box spans the same width)
    XM = (X0 + X1) / 2
    TOP, BOT = 46, 230
    vy = (TOP + BOT) / 2
    lx1, rx0 = XM - 5, XM + 5
    XL, XR = X0 + FR, X1 - FR          # face centres
    # A tightened artery narrows as a whole: the left tube is 8 units slimmer top and bottom (outer
    # diameter 168 vs 184) and its thick muscle wall (44 vs 24, lining included) squeezes the channel down.
    SQ = 8
    seg_l, lt, lb = _segment("hbp-cl", XL, lx1, TOP + SQ, BOT - SQ, 44, TIGHT, TIGHT_LN, 7.5, 1.7, "left")
    seg_r, rt, rb = _segment("hbp-cr", rx0, XR, TOP, BOT, 24, RELAX, RELAX_LN, 15, 1.6, "right")
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

    # pressure arrows: blood pushing out on the wall; bigger where pressure is high.  Tips touch the lining.
    # Six columns at x 318 to 468, so the two red cells (x 297 and 487) sit outside them and the arrows
    # never seem to sprout from a cell.
    for k in range(6):
        x = 318 + k * 30
        out.append(_varrow(x, vy - 15.5, lt, 3.2, 11, 9))
        out.append(_varrow(x, vy + 15.5, lb, 3.2, 11, 9))
    acols = [rx0 + 25 + k * 45 for k in range(5)]
    for x in acols:
        out.append(_varrow(x, rt + 13, rt, 2.2, 8, 6.5))
        out.append(_varrow(x, rb - 13, rb, 2.2, 8, 6.5))

    # nitric oxide on the healthy side only: made by the lining, moving out into the muscle it relaxes.
    # One molecule between each pair of arrow columns, alternately just off the lining and further out.
    for j, x in enumerate((a + 22.5 for a in acols[:-1])):
        near = j % 2 == 0
        out.append(_no_dot(x, rt - LIN - (5.2 if near else 12.4), (-18, 14, -9, 22)[j], c1, c2))
        out.append(_no_dot(x + 1.5, rb + LIN + (12.4 if near else 5.2), (16, -12, 9, -20)[j], c1, c2))

    # red blood cells: squeezed into the narrow vessel, roomy in the relaxed one
    for (x, dy, r) in [(XL + FR + 15, 1, 8), (lx1 - 17, -1, -10)]:
        out.append(_cell(x, vy + dy, 0.9, r))
    for (x, dy, r) in [(rx0 + 36, -27, 12), (rx0 + 122, -32, -8), (rx0 + 200, -25, 16),
                       (rx0 + 70, 28, -14), (rx0 + 156, 33, 6), (rx0 + 204, 26, -6)]:
        out.append(_cell(x, vy + dy, 0.9, r))

    # flow arrows, labelled as flow (the KEY's "Blood flow"); only the dark arrows stand for pressure
    out.append(_tag((XL + FR + lx1) / 2 - 75, vy, 150, 21, "Flow: high pressure", 11))
    out.append(_tag(rc - 80.5, vy, 161, 21, "Flow: normal pressure", 11))

    # ---- KEY: names every symbol and colour in the vessel.  Three rows, three columns: what is in the
    # blood | the wall from the inside out | nitric oxide, the outer layer and the cut end (the darker
    # HOLE pink inside the end faces).  Column starts give a 15-unit gap after each column's longest label
    # (Inter 600, 11 units: "Pressure (big = high)" 111.1, "Inner lining (makes NO)" 124.6, measured in
    # the browser) and a 15-unit right pad.
    KY, KH = 240, 58
    out.append(f'<rect x="{X0}" y="{KY}" width="{X1 - X0}" height="{KH}" rx="8" fill="#fff" stroke="#CFD6DA" stroke-width="1.4"/>')
    out.append(T(X0 + 14, KY + KH / 2 + 3.8, "KEY", 10.5, 800, INK, ls=1.2))
    out.append(f'<path d="M{X0 + 50},{KY + 9} V{KY + KH - 9}" stroke="#DDE2E5" stroke-width="1.2"/>')
    r1, r2, r3 = KY + 13, KY + 29, KY + 45

    def item(x, y, sw, label):
        return f'<g transform="translate({x + 12},{y})">{sw}</g>' + T(x + 30, y + 3.9, label, 11, 600, INK)

    def band(fill, ln, n):
        lines = "".join(f'<path d="M{-8 + j * (16 / max(n - 1, 1)):.1f},-5 l1.4,10" stroke="{ln}" stroke-width="1.5" opacity=".7"/>'
                        for j in range(n))
        return f'<rect x="-12" y="-6.5" width="24" height="13" rx="2" fill="{fill}"/>{lines}'

    flow_sw = (f'<rect x="-13" y="-6.5" width="26" height="13" rx="3" fill="{LUMEN}" stroke="{LUMEN_LN}" stroke-width="1"/>'
               '<path d="M-8,-3 H3 L8,0 L3,3 H-8 Z" fill="#fff" stroke="#C9B3AD" stroke-width=".8"/>')
    lining_sw = (f'<rect x="-12" y="-4.5" width="24" height="9" rx="2" fill="{LINING}" stroke="{LINING_LN}" stroke-width="1"/>'
                 + "".join(f'<ellipse cx="{x}" cy="0" rx="2.5" ry="1" fill="{NUC}"/>' for x in (-6.5, 0, 6.5)))
    c_1, c_2, c_3 = X0 + 62, X0 + 218, X0 + 388
    out.append(item(c_1, r1, _cell(0, 0, 0.72), "Red blood cell"))
    out.append(item(c_1, r2, flow_sw, "Blood flow"))
    # big + small arrow; the label says what the size means (big arrow = high pressure on the wall)
    out.append(item(c_1, r3, _varrow(-5, 7, -7, 2.8, 9, 7.5) + _varrow(7, 7, -2.5, 2, 6.5, 5.5), "Pressure (big = high)"))
    out.append(item(c_2, r1, lining_sw, "Inner lining (makes NO)"))
    out.append(item(c_2, r2, band(TIGHT, TIGHT_LN, 4), "Tight muscle wall"))
    out.append(item(c_2, r3, band(RELAX, RELAX_LN, 2), "Relaxed muscle wall"))
    out.append(item(c_3, r1, _no_dot(0, 0, 0, c1, c2), "Nitric oxide"))
    out.append(item(c_3, r2, f'<rect x="-12" y="-6.5" width="24" height="13" rx="2" fill="{OUTER}" stroke="{OUTER_LN}" stroke-width="1"/>',
                    "Outer layer"))
    # a mini cut face, the same rings as the art's end faces (outer layer, relaxed muscle, lining, then
    # the darker HOLE channel), 7.8 x 14 units: wider than the art's 0.11 aspect so the rings read at
    # swatch size, and 2.5 units clear of the row-2 swatch above it
    def ring(rx, ry, fill, stroke="none", sw_=0):
        return f'<ellipse rx="{rx}" ry="{ry}" fill="{fill}" stroke="{stroke}" stroke-width="{sw_}"/>'
    face_sw = (ring(3.9, 7, OUTER, OUTER_LN, 0.9) + ring(3.15, 5.65, RELAX)
               + ring(2.75, 4.9, "none", RELAX_LN, 0.6) + ring(2.3, 4.1, LINING) + ring(1.85, 3.3, HOLE, LINING_LN, 0.7))
    out.append(item(c_3, r3, face_sw, "Cut end"))
    return svg(W, H, "".join(out), "How nitric oxide relaxes a blood vessel: a tight artery under high pressure beside a "
                                   "relaxed one, whose inner lining makes nitric oxide")


# ------------------------------------------------------------------ front page
# Risk factors: AHA "Know Your Risk Factors for High Blood Pressure" (family history, age, chronic kidney
# disease; inactivity, high-sodium diet, overweight, too much alcohol, sleep apnea, diabetes, smoking, stress)
# and CDC "High Blood Pressure Risk Factors".  Tile 10 names two separate risks, joined by "or" so it never
# reads as one causing the other: estrogen birth control pills, which can raise blood pressure (2017 ACC/AHA
# guideline, Hypertension 2018;71:e13-e115, Table 13, oral contraceptives), and high blood pressure during an
# earlier pregnancy (gestational hypertension, preeclampsia), which raises later risk (2025 AHA/ACC guideline,
# Hypertension 2025;82:e212-e316, hypertension in pregnancy; AHA "Know Your Risk Factors", preeclampsia).
# Pregnancy itself is not the risk.  The breaks are set by hand: every clear wording needs 3 lines in a
# 1.24 in tile at 8.2 pt (measured: "Birth control pills," 90 px, "or high BP in a" 83, "past pregnancy" 75).
# Diabetes uses the kit's glucose meter, as the fatty-liver and neuropathy sheets do: the kit's "bloodsugar"
# glyph (a drop with a pulse trace) is the usual sign for blood pressure or a blood test, which confuses on
# a blood-pressure sheet.
RISKS = [
    ("scale", "Extra weight"), ("salt", "High-sodium,<br>processed food"), ("sofa", "Sitting most<br>of the day"),
    ("glass", "Too much<br>alcohol"), ("smoke", "Smoking"), ("headache", "Chronic stress"),
    ("moon", "Poor sleep or<br>sleep apnea"), ("meter", "Diabetes"), ("kidney", "Kidney<br>disease"),
    ("pills", "Birth control pills,<br>or high BP in a<br>past pregnancy"), ("dna", "Family<br>history"),
    ("age", "Increasing age")]
# Icons drawn here rather than straight from the kit: no "avoid" slash on the salt and glass (this row
# lists risks, not rules), a full cigarette with smoke, separated kidney beans, a birth control blister
# card.  The back's lifestyle band keeps the slashed kit salt; its tile 6 uses this cigarette with a slash
# (hbp-smoke-x).
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
             # AHA "When to call 911 about high blood pressure": over 180/120 with chest pain, shortness of
             # breath, back pain, numbness or weakness, change in vision or difficulty speaking, do not wait to see
             # if it comes down: call 911.  No symptoms: wait five minutes and test again; still unusually high,
             # contact your doctor immediately.  The 911 case leads, so nobody re-checks first with symptoms.
             '<div class="hbp-alarm"><b>Over 180/120</b> with chest or back pain, shortness of breath, numbness, weakness, '
             'or trouble seeing or speaking? <b>Call 911 now.</b> No symptoms? Wait 5 minutes and check again. '
             'Still that high: call your doctor right away.</div>'
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
/* back page, scoped: only this sheet's back carries the .hbp-back marker.
   The two formula columns carry the longest label facts, so they get the extra width (Nitric Boost most:
   its serving line names all twelve label ingredients); one header height for all five columns lines the
   photos up, and every product name gets a two-line box, so the sizes share one line and all five bullet
   lists start on one line (a flex box would split the no-break "EPA-DHA" span onto a line of its own).
   In the daily rhythm each count is a small grey pill after the product name, so a name that ends in a
   number never runs into it ("EPA-DHA 1000" then "1 softgel") and a count never splits from its unit; the
   slot widths fit the longest names (measured, Inter 7 pt: "Omega Pure EPA-DHA 1000" 123 px, "Cardio
   Essentials BP Support" 128 px) so each slot stays at five lines or fewer. */
.sheet.back:has(.hbp-back) .cols{grid-template-columns:1.09fr 1.27fr .86fr .86fr .92fr!important}
/* "In each serving" starts on one line in four columns: every bullet list but Nitric Boost's gets the height of
   four bullet lines (4 x 1.28em, plus the one 2 px gap between two bullets; the last bullet's margin collapses).
   The CoQ10 column is 0.92fr (1.35 in) so its serving line fits four lines under the taller list; BP Support at
   1.09fr keeps its line counts (measured).  Nitric Boost is left out on purpose: its serving line names all
   twelve label ingredients in six lines, so under a four-line list it would add two lines to the row and push
   the footer off the page. */
.sheet.back:has(.hbp-back) .col:not(:nth-child(2)) .what ul{min-height:calc(4 * 1.28em + 2px)}
/* one header height for all five columns: the three-line header (column 4, Omega Pure) measures 0.521 in; column 1's
   sub-line is one line since polish round 2, so its centred title sits clear of the START HERE badge */
.sheet.back:has(.hbp-back) .col .need{min-height:0.525in}
.sheet.back:has(.hbp-back) .col .pick .nm{min-height:2.3em}
/* The check panel gets the wider share (1.3 to 1): its six notes then take 12 lines (2+3+2+1+2+2) in both
   editions, where the old 1.1 to 1 split needed 15 for five.  The rhythm keeps its five-line Evening slot: Morning
   and Bedtime sit at their narrowest (65 and 55 px, measured), so Evening gets 116 px, just enough for
   "BP Support 3 capsules" and "EPA-DHA 1000 1 softgel" on one line each (at 1 to 1.35 it drops to 109 px
   and wraps to six lines).  The rhythm panel is a column, so its slot boxes stretch to the check panel's
   height instead of leaving a blank strip under the plan line. */
.sheet.back:has(.hbp-back) .duo{grid-template-columns:1fr 1.3fr;margin-top:0.06in}
.sheet.back:has(.hbp-back) .duo .panel:not(.rx){display:flex;flex-direction:column}
.sheet.back:has(.hbp-back) .rhythm{grid-template-columns:.66fr 1.3fr .58fr;flex:1}
/* The 11-line panel is 1.86 in tall, 0.15 in more than the old four-note panel.  It is paid back from block
   spacing only, never from type size or line spacing: band top padding 0.25 to 0.22 in and bottom 0.18 to
   0.16 in, the band title gap 0.1 to 0.08 in, the gap above Nutrient Solutions 0.1 to 0.08 in, and the
   column header box 0.56 to 0.525 in.  Polish round 2 adds a one-line sixth note (diabetes medicine), 14.3 px
   with its gap, paid back the same way: note gap 2 to 1 px, panel padding 0.08 to 0.06 in, the gap above the
   panels 0.08 to 0.06 in and the notes box padding 0.07 / 0.09 to 0.06 / 0.08 in (measured in print media:
   1.4 px to spare above the footer in both editions). */
.sheet.back:has(.hbp-back) .band{padding-top:0.22in!important;padding-bottom:0.16in}
.sheet.back:has(.hbp-back) .band h2{margin-bottom:0.08in}
.sheet.back:has(.hbp-back) .ns-title{margin-top:0.08in}
.sheet.back:has(.hbp-back) .notes{margin-top:0.08in;padding:0.06in 0.14in 0.08in}
.sheet.back:has(.hbp-back) .duo .panel{padding-top:0.06in;padding-bottom:0.06in}
.sheet.back:has(.hbp-back) .rx li{margin-bottom:1px}
.sheet.back:has(.hbp-back) .slot li{margin:1px 0 3px}
.sheet.back:has(.hbp-back) .slot li em{display:inline-block;white-space:nowrap;background:#EEF1F3;color:#4A555B;
  border-radius:3px;padding:0 3px;line-height:1.3}
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
        # Six tiles, titles short enough that every title sits on one line at 9.6 pt, all six bodies start on
        # the same line, and the gutter between neighbouring titles is 0.2 in or more (Merriweather 700 measured
        # in the browser; the tightest pair, "Lighten the load" / "Move, then hold", is 0.204 in).  The lifestyle
        # band is not run through the edition tokens, so it never uses {who}; "your dentist" in tile 1 is right
        # in both editions.
        "life": [
            # NutriDyn GLC 2025 endothelial-dysfunction protocol, slide 12 (HBP Supplement Recommendations):
            # nitrate-rich foods daily (beets, lettuce, spinach); avoid antiseptic mouthwash (it blunts the
            # nitrate-to-NO pathway).  Kapil V et al., Free Radic Biol Med 2013;55:93-100 (PMID 23183324): 7 days of
            # antiseptic (chlorhexidine) mouthwash cut oral nitrite and raised systolic pressure 2 to 3.5 mm Hg.
            # The exception matters: dentists prescribe chlorhexidine rinse after gum and periodontal treatment,
            # and a patient should not drop it on this sheet's word.  The front's steps 1 and 2 give the why.
            # Title spelled out (NO is defined only on the front); "Make nitric oxide" keeps a 0.204 in gutter
            # to "Cut the sodium" ("Boost nitric oxide" measured 0.195 in).
            # Fruit (polish round 2): potassium-rich, DASH-style eating goes with cutting sodium.  2017 ACC/AHA
            # guideline (Hypertension 2018;71:e13-e115), Table 15: a DASH diet rich in fruits and vegetables, and
            # more dietary potassium (3,500 to 5,000 mg a day, preferably from food, unless kidney disease or a
            # potassium-raising drug rules it out); the 2025 AHA/ACC guideline keeps the heart-healthy, DASH-style
            # pattern.  The NutriDyn GLC 2025 protocol's eating plan names deep-coloured vegetables and fruit
            # (berries, pomegranates) beside the nitrate foods.  The tile prints no potassium number; the check
            # panel's kidney and potassium note covers who must hold back.  Measured: four lines in both editions
            # ("Eat greens, beets and fruit daily." takes five and pushes the footer down).
            ("beet", "Make nitric oxide", "Greens, beets and fruit daily. Skip antiseptic mouthwash unless your "
                                           "dentist prescribed it."),
            # AHA "How much sodium should I eat per day?": no more than 2,300 mg a day, an ideal limit of 1,500 mg
            # for most adults, especially with high blood pressure; more than 70% comes from packaged, prepared and
            # restaurant food.  2025 AHA/ACC guideline (Hypertension 2025;82:e212-e316): under 1,500 mg optimal.
            # (measured at 7.5 pt: four lines, "Under 2,300 mg a day;" 109 px of the 114 px column)
            ("salt", "Cut the sodium", "Under 2,300 mg a day; 1,500 is better. Most comes from packaged and "
                                       "restaurant food."),
            # AHA "Managing Weight to Control High Blood Pressure": losing even 5 to 10 pounds can help lower blood
            # pressure.  2017 ACC/AHA guideline Table 15: about 1 mm Hg lower for every 1 kg lost.
            # ("Trim extra weight" measured two lines at 9.6 pt; this title fits one.)
            ("scale", "Lighten the load", "Losing even 5 to 10 pounds can help lower your numbers."),
            # AHA physical activity advice: 150 minutes a week of moderate activity (30 minutes on most days, 5 a
            # week).  2017 ACC/AHA Table 15: isometric resistance (hand grip, 4 x 2 minutes) 3 sessions a week.
            # Edwards JJ et al., Br J Sports Med 2023;57:1317-26 (PMID 37491419): isometric work (wall squats, hand grips) gave the
            # largest resting blood pressure drop of any exercise type.  NutriDyn GLC 2025 endothelial-dysfunction
            # protocol: 20 to 30 minutes, 5 times a week, plus resistance training; NutriDyn GLC 2026 cardiovascular
            # protocol: 30 minutes 5 times a week plus resistance 2 to 3 times.
            # Safety: an isometric hold raises blood pressure while it lasts, and holding the breath while straining
            # (the Valsalva manoeuvre) raises it further, so the tile says to breathe normally: AHA scientific
            # statement on resistance exercise, Williams MA et al., Circulation 2007;116:572-84 (PMID 17638929,
            # doi 10.1161/CIRCULATIONAHA.107.185214): avoid breath-holding and straining.  Its contraindication
            # table (polish round 2): uncontrolled hypertension above 160/100 mm Hg is a relative contraindication
            # to resistance training (see a physician first), above 180/110 mm Hg an absolute one.  The front's own
            # table puts many readers in Stage 2 or Severe, so the holds come after "Under 160/100?".  The
            # thresholds are as the round-2 review cited them; the statement's full text is outside this build
            # session's network.  "3 times a week" left the tile to keep it at four lines (with it the tile takes
            # five and the footer drops 0.115 in).
            ("dumbbell", "Move, then hold", "Walk 30 minutes most days. Under 160/100? Add wall sits or hand grips; "
                                            "breathe normally."),
            # AHA Life's Essential 8: 7 to 9 hours of sleep a night for adults; AHA: obstructive sleep apnea
            # raises blood pressure, and loud snoring is a common sign (the tile asks about any snoring, a wider
            # net, to stay at four lines).
            # Slow breathing (polish round 2, the stress step: the front's intro names stress and its risk row has
            # "Chronic stress"): NutriDyn GLC 2025 endothelial-dysfunction protocol, daily stress management (deep
            # nasal breathing, humming, meditation, yoga); AHA scientific statement, Brook RD et al., Hypertension
            # 2013;61:1360-83 (PMID 23608661): device-guided slow breathing is Class IIa, Level of Evidence B, the
            # best supported of the stress approaches it graded (other relaxation therapies Class III).  Neither
            # source gives a number of minutes this sheet could print, so the tile says "a few minutes".  The title
            # names both steps in the band's comma style ("Move, then hold", "Quit, cut back"); "Sleep and relax"
            # would point at the relaxation therapies that statement did not support.  Measured: four lines; title
            # gutters 0.278 and 0.366 in.  Keeping "Loud" before "Snoring" as well takes five lines and pushes the
            # footer down.
            ("moon", "Sleep, breathe", "Sleep 7 to 9 hours; breathe slowly a few minutes a day. Snoring? Ask about "
                                       "a&nbsp;sleep&nbsp;test."),
            # AHA: each cigarette raises blood pressure for a while and smoking damages the vessel lining.
            # 2025 AHA/ACC guideline: drink less alcohol, and none is best; NutriDyn GLC 2019 HBP protocol
            # (Taming the Silent Killer): under 1 drink a day.
            # (three lines; the last reads "alcohol; none is best.", no word left alone on a line)
            # Icon: the front's cigarette with an avoid slash (hbp-smoke-x, registered above).
            ("hbp-smoke-x", "Quit, cut back", "Quit smoking: it tightens vessels. Drink less alcohol; "
                                              "none&nbsp;is&nbsp;best."),
        ],
        # Products: Asher's Hypertension protocol email, 2021-03-11 (Cardio Essentials BP Support is "the
        # formula"); the NutriDyn GLC 2025 endothelial-dysfunction protocol, slide 12 (HBP Supplement
        # Recommendations) and the NutriDyn GLC 2019 HBP protocol (Taming the Silent Killer): Cardio Flow or Nitric
        # Boost for nitric oxide, CoQ10 100 mg, Omega Pure, magnesium glycinate; the NutriDyn GLC 2026
        # cardiovascular protocol list.  Five columns, the competitor's count; their categories map as: BP
        # botanicals (hibiscus, lemon verbena, green coffee) -> BP Support; L-citrulline for nitric oxide ->
        # Nitric Boost; magnesium -> Magnesium Glycinate; omega-3 -> Omega Pure; fucoidan (no NutriDyn
        # equivalent) -> CoQ10, from the protocols.  Label facts, sizes, URLs and photo status for every
        # product: products.d/high-blood-pressure.json.
        # Daily rhythm: morning Nitric Boost 3 + Omega 1; evening meal BP Support 3 + Omega 1 + CoQ10 1;
        # bedtime Magnesium 1 = 10 pills.  Supplemental magnesium: Nitric Boost 120 mg + 1 Magnesium Glycinate
        # 130 mg = 250 mg a day, under the NIH ODS upper limit of 350 mg a day from supplements.
        # Every bullet below was measured in its column so no bullet list or serving line grows the row.  The
        # "In each serving" blocks start on one line in four columns (CSS: a four-line bullet-list height, CoQ10
        # widened so its serving line fits four lines).  Nitric Boost's starts higher: its two bullets take two
        # lines and its serving line six (twelve label ingredients), so aligning it would grow the row by two
        # lines (about 0.25 in) and push the footer off the page; measured 2026-11-03.
        "cols": [
            # Start here: Asher's named HBP formula and his rule "BP Support if looking purely for blood pressure
            # support"; ND681 compliance line and its nitric oxide mechanism (Benolea, MegaNatural-BP promote
            # nitric oxide production).  "Helps make nitric oxide" fits one line ("Helps vessels make nitric
            # oxide" took two and grew the row).
            # The sub-line names the four extracts on one line (polish round 2): on two lines ("olive leaf, black
            # garlic, celery and grape seed") the centred three-line header pushed the title up under the START
            # HERE badge, 1 px of clear space at 300 dpi.  One line lowers the title about 5.6 px (measured in the
            # DOM, halo to title box: -1.9 to +3.7 px); the serving line still names each extract in full.  The
            # header box keeps its 0.525 in for column 4's three lines, so the photos stay level.
            {"p": "hbp_bp_support", "need": "Healthy pressure", "needsub": "olive leaf, garlic, celery, grape",
             "start": True, "dose": "dose_from_db",
             "bullets": ["Supports healthy blood pressure already in the normal range",
                         "Helps make nitric oxide"]},
            # ND1255 Rev. 6/25, its own structure/function wording: "supports healthy nitric oxide production and
            # optimal blood flow", "supports healthy blood flow".  Both bullets say the function in the label's
            # sense; neither points back to the front's pressure steps, so nothing reads as "this capsule lowers
            # high blood pressure".  Spelled out (the abbreviation could read as "no production").  Polish round 2:
            # "Supports nitric oxide" named the molecule but not the function; "Helps make nitric oxide" says it
            # in one line ("Supports nitric oxide production" wraps to two lines and grows the row by 11 px).
            {"p": "hbp_nitric_boost", "need": "Boost nitric oxide", "needsub": "beet root and potassium nitrate",
             "dose": "dose_from_db",
             "bullets": ["Helps make nitric oxide", "Supports healthy blood flow"]},
            # Structure/function only, in plain words (polish round 2: "healthy vascular tone" was jargon with no
            # gloss): magnesium is a cofactor in the enzyme systems behind muscle and nerve function and blood
            # pressure regulation (NIH ODS Magnesium fact sheet for health professionals), hence "Supports healthy
            # blood vessels", not "relax vessel walls", which echoed front step 4 and read as "this capsule lowers
            # blood pressure".  The second bullet is an instruction, not a claim, so it carries no diamond: Asher's
            # magnesium blast (2026-10-12, Hypertension 2025 meta-analysis of 38 RCTs) found the benefit tracked
            # the starting state.  It asks about the level instead of sending everyone for a blood test: the
            # routine serum test correlates poorly with the body's magnesium stores (NIH ODS: less than 1% of body
            # magnesium is in serum), so a normal result does not rule magnesium out.  Bullets are not run through
            # {who}, so the token is not used here.  The serving line says why the plan uses less than the label
            # (products.d hbp_mag_glycinate).  Measured: header and bullets keep their line counts.
            {"p": "hbp_mag_glycinate", "need": "Healthy vessels", "needsub": "magnesium", "dose": "dose_from_db",
             "bullets": ["Supports healthy blood vessels", "Ask about your magnesium level"]},
            # the no-break hyphen keeps "omega-3s" whole, so the header wraps "EPA and DHA / omega-3s"
            # Claims from NutriDyn sell sheet ND416 Rev. 4/25 (Omega Pure EPA-DHA 1000): 'Healthy cardiovascular
            # function'; EPA and DHA are 'integral components of membrane phospholipids'. No triglyceride claim.
            {"p": "hbp_omega_1000", "need": "Heart-healthy fats", "needsub": "EPA and DHA omega&#8209;3s", "dose": "dose_from_db",
             "bullets": ["Supports heart and vessel health", "Supports healthy cell membranes"]},
            # Statins lower CoQ10 (NIH NCCIH, Coenzyme Q10); ND270: "Supports blood flow and nitric oxide
            # production", "Supports energy production".  Dose: the label's 1 softgel daily (products.d hbp_coq10).
            {"p": "hbp_coq10", "need": "Power the heart", "needsub": "coenzyme Q10", "dose": "dose_from_db",
             "bullets": ["Statins can lower your CoQ10", "Fuel for heart cells"]},
        ],
        # Six medicine-and-nutrient notes, one list for both editions via {who} ("your pharmacist" or "your
        # provider"), so the pharmacy edition carries every caution the provider edition does: depletions and the
        # fish allergen, potassium, blood pressure medicines (with the never-stop rule and the prescriber, who is
        # the one who can change a dose: a DC or ND handing out the sheet often cannot), diabetes medicines, blood
        # thinners, mineral spacing and pregnancy.  None says a formula lowers blood pressure; they say "show this
        # sheet, doses may need a check".  Drug classes carry a drug name patients know (lisinopril, losartan),
        # and INR is glossed.
        # Fish allergy (polish round 2): Omega Pure EPA-DHA 1000 is fish oil; NutriDyn sell sheet ND416 Rev. 4/25
        # prints "Contains: Fish (Anchovy, Sardine, and Mackerel)." (products.d hbp_omega_1000).
        # Diabetes medicine (polish round 2; diabetes is on the front's risk row): BP Support gives 750 mg olive
        # leaf extract a day (ND681); 500 mg a day lowered HbA1c and fasting insulin against placebo in adults
        # with type 2 diabetes (Wainstein J et al., J Med Food 2012;15:605-10, PMID 22512698, doi
        # 10.1089/jmf.2011.0243), so with insulin or diabetes pills sugar can run lower: the note asks for more
        # checks and leaves any dose change to the prescriber (note 3 already says to show the sheet).
        # Sources: NIH ODS Magnesium fact sheet (loop and thiazide diuretics raise urinary magnesium loss;
        # spironolactone lowers it; impaired kidneys raise the risk of too much magnesium); NIH ODS Potassium
        # fact sheet (ACE inhibitors, ARBs and potassium-sparing diuretics can raise potassium); 2025 AHA/ACC
        # guideline (potassium-enriched salt substitutes except with CKD or potassium-raising drugs); NIH NCCIH
        # Coenzyme Q10 (statins lower CoQ10; the beta-blocker link rests on old in-vitro data, so it is left
        # out); nitrate and nitric-oxide formulas can add to the blood-pressure drop from blood pressure
        # medicines, nitroglycerin and PDE5 inhibitors (sildenafil, tadalafil), as can magnesium, fish oil and
        # the BP Support botanicals.  Blood thinners: NIH NCCIH Garlic and NIH ODS Omega-3 and Vitamin E fact
        # sheets (may add to bleeding); grape seed (200 mg in BP Support, ND681; 50 mg in Nitric Boost, ND1255)
        # and French maritime pine bark (Pycnogenol 50 mg, ND1255) may slow blood clotting, so taking them with
        # anticoagulant or antiplatelet drugs may raise bruising and bleeding risk (Natural Medicines monographs
        # Grape and Pycnogenol, as carried by MedlinePlus Herbs and Supplements; platelet-aggregation data).
        # Pomegranate (polish round 2): Nitric Boost has 200 mg Pomanox pomegranate extract (ND1255 Rev. 6/25),
        # and pomegranate has a case report of a changed INR on warfarin: the INR fell below
        # range when the patient stopped pomegranate juice and the warfarin dose had to rise (Komperda KE,
        # Pharmacotherapy 2009;29:1002-6, PMID 19637955, doi 10.1592/phco.29.8.1002).
        # The note says "ask {who}" for every thinner, because only warfarin has an INR to check: apixaban,
        # rivaroxaban, dabigatran, clopidogrel and aspirin do not.  INR is glossed as a clotting test.
        # CoQ10 and warfarin point both ways, so the note asks for an INR check
        # rather than naming a direction: reduced warfarin effect (Spigset O, Lancet 1994;344:1372-3, PMID
        # 7968059, doi 10.1016/s0140-6736(94)90736-6), more self-reported bleeding on warfarin, OR 3.69
        # (Shalansky S et al., Pharmacotherapy 2007;27:1237-47, PMID 17723077, doi 10.1592/phco.27.9.1237),
        # and no INR change at 100 mg a day in a small crossover RCT (Engelsen J et al., Thromb Haemost
        # 2002;87:1075-6, PMID 12083489).  Pregnancy and nursing: the ND681, ND1255 and ND270 labels all say
        # "If you are pregnant, nursing, or taking medication, consult your healthcare practitioner", and
        # celery seed is traditionally avoided in pregnancy.  Nitric Boost: 150 mg potassium per 3 capsules
        # (ND1255).
        # Mineral spacing: magnesium (Magnesium Glycinate; 120 mg in Nitric Boost) and zinc (7 mg in Nitric Boost,
        # ND1255) bind some medicines in the gut.  NIH ODS Magnesium fact sheet: oral bisphosphonates such as
        # alendronate at least 2 hours apart; tetracycline and quinolone antibiotics at least 2 hours before or
        # 4 to 6 hours after a magnesium supplement.  NIH ODS Zinc fact sheet: the same antibiotics 2 hours before
        # or 4 to 6 hours after zinc.  Levothyroxine prescribing information (Synthroid, sections 2.1 and 7.1): at
        # least 4 hours from products that cut its absorption, magnesium-containing antacids among them.
        # "4 hours apart" covers the thyroid and bone pills only.  It is too short for some antibiotics:
        # ciprofloxacin goes at least 2 hours before or 6 hours after magnesium antacids and zinc-containing
        # products (Cipro prescribing information), moxifloxacin 4 hours before or 8 hours after products with
        # magnesium or zinc (Avelox prescribing information), and NIH ODS gives 4 to 6 hours after.  So the note
        # says "antibiotics: ask {who}" and leaves the gap to the pharmacist for the drug in hand (polish round 2;
        # round 1 wrongly said 4 hours met all three).  The spacing matters here because Nitric Boost is a
        # breakfast dose and levothyroxine is usually a morning dose.  "Bone (alendronate)" glosses the drug for
        # a patient.
        # Measured in the rendered panel at 7.2 pt with the 1 to 1.3 split: 2 + 3 + 2 + 1 + 2 + 2 = 12 lines in
        # both editions (CSS above pays for the twelfth); "BP pills" is the only head short enough to keep note 3
        # on two lines ("High BP" is already on the front).  The fish, pomegranate and antibiotic wording keeps
        # notes 1, 5 and 6 at two lines each; the diabetes note takes one.  A no-break space keeps "Nitric Boost"
        # whole in note 6 (it split across the line break).
        "rx": [
            "<b>Water pills</b> (HCTZ, furosemide) can drain magnesium and potassium; <b>statins</b> lower CoQ10. "
            "Ask about a blood test. <b>Fish allergy?</b> Skip Omega Pure.",
            "<b>Kidney disease, an ACE inhibitor (like lisinopril), ARB (like losartan) or spironolactone?</b> "
            "Potassium can build up: skip salt substitutes, and ask {who} before magnesium or Nitric Boost "
            "(150&nbsp;mg potassium).",
            "<b>BP pills, nitroglycerin or ED pills?</b> Show {who} and your prescriber this sheet first: doses may "
            "need a check. Never stop a medicine on your own.",
            "<b>Diabetes medicine?</b> Olive leaf can lower blood sugar; check it more often.",
            "<b>Blood thinner?</b> Garlic, fish oil, grape seed, pine bark, pomegranate, vitamin E and CoQ10 can "
            "change it: ask {who} (on warfarin, get an INR clotting test).",
            "<b>Thyroid or bone (alendronate) pills?</b> 4 hours apart from magnesium and Nitric&nbsp;Boost; "
            "<b>antibiotics:</b> ask {who}. <b>Pregnant or nursing?</b> Ask first.",
        ],
    },
}
