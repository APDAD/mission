"""insulin-resistance sheet module (self-contained: no legacy / sheets.py / art.py drawing code).

FRONT: how insulin moves sugar into a cell, drawn at the cell wall.  Two panels, NORMAL and
INSULIN RESISTANCE, share one picture grammar:
  blood vessel (glucose = purple hexagons, insulin = gold dots, red blood cells)
  -> fluid outside the cell
  -> cell membrane: a phospholipid bilayer (two rows of round heads, paired tails)
     with the insulin receptor (Y-shaped: two alpha subunits outside the cell form the
     insulin pocket, two beta subunits cross the membrane and end in signalling domains)
     and the GLUT4 glucose door (a channel; open at the surface when insulin works,
     left packed inside the cell when it does not)
  -> inside the cell.
The step text sits in its own strip under each panel; the art carries only numbered markers and a
few zone names in clear space ("Blood vessel" on a white backdrop).  One KEY names every symbol.
Below the art: what drives it / clues / where it leads, the CDC stat (only "1 in 3" is big) and a
"Know your numbers" panel (ADA glucose and A1c ranges, NHLBI/AHA metabolic syndrome check).

BACK: unchanged from the first draft (a later pass revises the products).
"""
import math
import random

from kit import icon
from svgkit import T, defs, svg, label_bg

# ------------------------------------------------------------------ palette (every one is in the KEY)
GLU, GLU_EDGE = "#6B6FC2", "#45499A"       # glucose (sugar): purple hexagon (same purple as svgkit.GLUCOSE)
INS_EDGE = "#A8740C"                       # insulin: gold dot (svgkit.INSULIN gold, radial gradient irIn)
REC_A, REC_B, REC_EDGE = "#4A8FD0", "#265E96", "#163E66"   # receptor: alpha subunits light blue, beta dark blue
G4_EDGE = "#15683F"                        # GLUT4 glucose door: green helices
HEAD_EDGE, TAIL = "#B65A40", "#C9AC8B"     # cell membrane: phospholipid heads (coral) and tails (tan)
OUTSIDE, INSIDE, CORE = "#EAF2F6", "#FCECE4", "#FFF7EC"
GREEN, RED, INK = "#2F7D59", "#8A1B22", "#2B3236"

# one panel, in viewBox units (two panels + a 16 gap = 760 wide).  Bands from the top:
HDR = 26                   # header
V0, V1 = 30, 72            # blood vessel (wall 5, lumen between)
CY = 176                   # membrane centre line (bilayer spans CY-20 .. CY+20)
IN1 = 268                  # bottom of "inside the cell"; the numbered step strip sits below
PW, PH = 372, 326
REC_X, G4_X = 130, 268     # receptor and GLUT4 positions (panel coordinates)
INS_R, GLU_R = 6.4, 5.2
VM = (V0 + V1) / 2         # vessel mid line
M1, M2 = (176, CY - 74), (205, CY + 80)        # step markers 1 and 2 (both panels)
M3N, M3R = (292, CY + 44), (190, VM)           # step 3: inside the cell (normal) / on the vessel (resistance)


def ir_defs():
    mk = lambda i, c: (f'<marker id="{i}" viewBox="0 0 10 10" refX="6.5" refY="5" markerWidth="4.2" markerHeight="4.2" '
                       f'orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="{c}"/></marker>')
    return defs(
        '<linearGradient id="irG4" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#74D7A7"/><stop offset="1" stop-color="#1F8B57"/></linearGradient>',
        '<radialGradient id="irHd" cx=".38" cy=".34" r=".72"><stop offset="0" stop-color="#FDD6C5"/><stop offset="1" stop-color="#E27B5F"/></radialGradient>',
        '<radialGradient id="irIn" cx=".36" cy=".32" r=".78"><stop offset="0" stop-color="#FFE9A8"/><stop offset=".55" stop-color="#F2B632"/><stop offset="1" stop-color="#DE9A14"/></radialGradient>',
        '<linearGradient id="irVw" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#CF4C55"/><stop offset="1" stop-color="#9A2831"/></linearGradient>',
        '<linearGradient id="irLu" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FCE4E0"/><stop offset="1" stop-color="#F6CBC5"/></linearGradient>',
        '<radialGradient id="irRc" cx=".42" cy=".36" r=".75"><stop offset="0" stop-color="#E8656A"/><stop offset="1" stop-color="#B0242D"/></radialGradient>',
        mk("irAp", GLU_EDGE), mk("irAg", GREEN), mk("irAy", INS_EDGE))


# ------------------------------------------------------------------ molecules and parts
def glucose(x, y, r=GLU_R):
    pts = " ".join(f"{x + r * c:.1f},{y + r * s:.1f}" for c, s in
                   ((1, 0), (.5, .866), (-.5, .866), (-1, 0), (-.5, -.866), (.5, -.866)))
    return f'<polygon points="{pts}" fill="{GLU}" stroke="{GLU_EDGE}" stroke-width="1" stroke-linejoin="round"/>'


def insulin(x, y, r=INS_R):
    return f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="url(#irIn)" stroke="{INS_EDGE}" stroke-width="1"/>'


def red_cell(x, y, rot=0, s=1.0):
    return (f'<g transform="translate({x},{y}) rotate({rot}) scale({s})"><ellipse rx="12.5" ry="7" fill="url(#irRc)" stroke="#8E1D25" stroke-width=".8"/>'
            '<ellipse rx="6.2" ry="2.8" fill="none" stroke="#97202A" stroke-width="1.5" opacity=".75"/></g>')


def lipid(x, yh, down):
    """One phospholipid: round head at (x, yh), two wavy tails pointing into the membrane."""
    s = 1 if down else -1
    y0 = yh + s * 3.9
    L = 11.0
    tails = "".join(f'<path d="M{x + dx:.1f},{y0:.1f} q-1.3,{s * L / 4:.2f} 0,{s * L / 2:.2f} t0,{s * L / 2:.2f}"/>'
                    for dx in (-1.75, 1.75))
    return (f'<g fill="none" stroke="{TAIL}" stroke-width="1.45" stroke-linecap="round">{tails}</g>'
            f'<circle cx="{x:.1f}" cy="{yh}" r="4.3" fill="url(#irHd)" stroke="{HEAD_EDGE}" stroke-width=".6"/>')


def membrane(x0, x1, cy, skips):
    """Phospholipid bilayer from x0 to x1, centre line cy.  skips = [(x, half_width)] where proteins sit."""
    out = [f'<rect x="{x0}" y="{cy - 16}" width="{x1 - x0}" height="32" fill="{CORE}"/>']
    x = x0 + 4.6
    while x < x1:
        if not any(abs(x - c) < hw for c, hw in skips):
            out.append(lipid(x, cy - 16, True) + lipid(x, cy + 16, False))
        x += 9.1
    return "".join(out)


def receptor(cx, cy, bound=True, s=1.0):
    """Insulin receptor with its membrane centre at (cx, cy).  Outline-then-body layering gives one
    clean silhouette: alpha arms and lobes (light blue, outside the cell) form the insulin pocket;
    the two beta subunits (dark blue) cross the bilayer and end in signalling domains inside."""
    arms = [f"M{g * 5},-30 C{g * 6},-46 {g * 11},-58 {g * 18},-69" for g in (-1, 1)]
    lobes = [(-20, -75), (20, -75)]
    rods = [(-9.5, -37, 6.6, 64), (2.9, -37, 6.6, 64)]          # beta: y -37 (outside) to +27 (inside)
    kin = [(-25, 21, 21, 27), (4, 21, 21, 27)]                    # beta signalling (kinase) domains
    o = [f'<g transform="translate({cx},{cy}) scale({s})">']
    for d in arms:
        o.append(f'<path d="{d}" stroke="{REC_EDGE}" stroke-width="16.2" fill="none" stroke-linecap="round"/>')
    for x, y in lobes:
        o.append(f'<circle cx="{x}" cy="{y}" r="11.3" fill="{REC_EDGE}"/>')
    for x, y, w, h in rods:
        o.append(f'<rect x="{x - 1.2}" y="{y - 1.2}" width="{w + 2.4}" height="{h + 2.4}" rx="{(w + 2.4) / 2}" fill="{REC_EDGE}"/>')
    for x, y, w, h in kin:
        o.append(f'<rect x="{x - 1.2}" y="{y - 1.2}" width="{w + 2.4}" height="{h + 2.4}" rx="9.6" fill="{REC_EDGE}"/>')
    o.append(f'<rect x="-8" y="-45.2" width="16" height="8.4" rx="4" fill="{REC_EDGE}"/>')     # alpha-alpha link
    for d in arms:
        o.append(f'<path d="{d}" stroke="{REC_A}" stroke-width="13.8" fill="none" stroke-linecap="round"/>')
    for x, y in lobes:
        o.append(f'<circle cx="{x}" cy="{y}" r="10.1" fill="{REC_A}"/>')
    for x, y, w, h in rods:
        o.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{w / 2}" fill="{REC_B}"/>')
    for x, y, w, h in kin:
        o.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8.4" fill="{REC_B}"/>')
    o.append(f'<rect x="-6.8" y="-44" width="13.6" height="6" rx="3" fill="{REC_A}"/>')
    # soft highlights (light from the upper left)
    for g in (-1, 1):
        o.append(f'<path d="M{g * 5 - 3},-34 C{g * 6 - 3},-48 {g * 11 - 3},-58 {g * 18 - 3},-68" stroke="#9CCBF2" '
                 'stroke-width="2.6" fill="none" stroke-linecap="round" opacity=".75"/>')
        o.append(f'<circle cx="{g * 20 - 3.6}" cy="-78.6" r="3.6" fill="#BFE0FA" opacity=".8"/>')
    for x, y, w, h in kin:
        o.append(f'<rect x="{x + 3}" y="{y + 3}" width="4" height="{h - 8}" rx="2" fill="#5E95CB" opacity=".8"/>')
    if bound:
        o.append(insulin(0, -71))
    o.append("</g>")
    return "".join(o)


def glut4(cx, cy, open_=True, s=1.0):
    """GLUT4 glucose door: two halves of three helices around a water-filled pore."""
    gap, w, step, h = (13.0 if open_ else 3.0), 6.6, 5.8, 54
    o = [f'<g transform="translate({cx},{cy}) scale({s})">']
    if open_:
        o.append(f'<rect x="{-gap / 2 - 1:.1f}" y="{-h / 2 + 2}" width="{gap + 2:.1f}" height="{h - 4}" fill="#D6E8F0"/>')
    for k in (2, 1, 0):                      # outer helices first so the inner ones sit in front
        hh = h - (6 if k == 2 else 0)
        for g in (-1, 1):
            xc = g * (gap / 2 + w / 2 + k * step)
            o.append(f'<rect x="{xc - w / 2:.1f}" y="{-hh / 2:.1f}" width="{w}" height="{hh}" rx="{w / 2}" '
                     f'fill="url(#irG4)" stroke="{G4_EDGE}" stroke-width=".9"/>')
    o.append("</g>")
    return "".join(o)


def vesicle(cx, cy, r, doors):
    """Storage bubble inside the cell: its own little bilayer (two rings of heads) holding GLUT4 doors."""
    o = [f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#FFF9F4"/>']
    n = int(2 * math.pi * r / 6.2)
    for ring, rr in ((0, r), (1, r - 5.4)):
        m = n if ring == 0 else int(n * (r - 5.4) / r)
        for i in range(m):
            a = 2 * math.pi * i / m
            if any(abs((math.degrees(a) - d + 180) % 360 - 180) < 19 for d in doors):
                continue
            o.append(f'<circle cx="{cx + rr * math.cos(a):.1f}" cy="{cy + rr * math.sin(a):.1f}" r="2.1" '
                     f'fill="url(#irHd)" stroke="{HEAD_EDGE}" stroke-width=".4"/>')
    for d in doors:
        a = math.radians(d)
        rm = r - 2.7
        o.append(f'<g transform="translate({cx + rm * math.cos(a):.1f},{cy + rm * math.sin(a):.1f}) rotate({d + 90})">'
                 f'{glut4(0, 0, False, 0.36)}</g>')
    return "".join(o)


def marker(x, y, n):
    return (f'<circle cx="{x}" cy="{y}" r="8.6" fill="#FFFFFF" stroke="{INK}" stroke-width="1.6"/>'
            + T(x, y + 3.9, str(n), 11, 800, INK, "middle"))


def place(rng, radii, box, avoid, pad=1.6, tries=8000):
    """Place one round thing per radius inside box (x0, y0, x1, y1) with its whole body inside, at least
    `pad` clear of every other placed thing and of every avoid ellipse (x, y, rx, ry).  Returns (x, y, r)."""
    out = []
    for r in radii:
        for _ in range(tries):
            x, y = rng.uniform(box[0] + r, box[2] - r), rng.uniform(box[1] + r + pad, box[3] - r - pad)
            if any(((x - ax) / (arx + r + pad)) ** 2 + ((y - ay) / (ary + r + pad)) ** 2 < 1 for ax, ay, arx, ary in avoid):
                continue
            if any((x - px) ** 2 + (y - py) ** 2 < (r + pr + pad) ** 2 for px, py, pr in out):
                continue
            out.append((x, y, r))
            break
    return out


# ------------------------------------------------------------------ one panel
def panel(x0, normal):
    rng = random.Random(11 if normal else 23)
    cid = "irClipN" if normal else "irClipR"
    o = [f'<g transform="translate({x0},0)">',
         f'<clipPath id="{cid}"><rect width="{PW}" height="{PH}" rx="12"/></clipPath>',
         f'<g clip-path="url(#{cid})">',
         f'<rect width="{PW}" height="{PH}" fill="#FFFFFF"/>',
         f'<rect y="{HDR}" width="{PW}" height="{CY - 20 - HDR}" fill="{OUTSIDE}"/>',
         f'<rect y="{CY + 20}" width="{PW}" height="{IN1 - CY - 20}" fill="{INSIDE}"/>']
    # header
    o.append(f'<rect width="{PW}" height="{HDR}" fill="{GREEN if normal else RED}"/>')
    o.append(T(14, 18, "NORMAL" if normal else "INSULIN RESISTANCE", 13, 900, "#FFFFFF", ls=0.8))
    o.append(T(PW - 14, 17.6, "cells answer insulin" if normal else "cells barely answer", 10.5, 600, "#FFFFFF",
               "end", italic=True))

    # blood vessel: wall, lumen, endothelial nuclei, red blood cells, glucose and insulin
    o.append(f'<rect y="{V0}" width="{PW}" height="{V1 - V0}" fill="url(#irVw)"/>')
    o.append(f'<rect y="{V0 + 5}" width="{PW}" height="{V1 - V0 - 10}" fill="url(#irLu)"/>')
    o.append(f'<path d="M0,{V0 + 1.2} H{PW}" stroke="#E98A8F" stroke-width="1" opacity=".7"/>')
    for k in range(6):
        o.append(f'<ellipse cx="{40 + k * 64}" cy="{V0 + 2.6}" rx="8" ry="1.5" fill="#7A1820" opacity=".5"/>'
                 f'<ellipse cx="{72 + k * 64}" cy="{V1 - 2.6}" rx="8" ry="1.5" fill="#7A1820" opacity=".5"/>')
    cells = [(158, VM - 2, 7), (252, VM + 3, -8), (344, VM - 3, 4)]
    for x, y, r in cells:
        o.append(red_cell(x, y, r))
    avoid = [(x, y, 13.5, 8) for x, y, _ in cells]          # red cell size, a little extra for the tilt
    if not normal:
        avoid.append((M3R[0], M3R[1], 8.6, 8.6))           # keep step 3's marker clear
    n_ins, n_glu = (4, 6) if normal else (8, 13)            # resistance: more sugar AND more insulin in the blood
    for x, y, r in place(rng, [INS_R] * n_ins + [GLU_R] * n_glu, (100, V0 + 5, 370, V1 - 5), avoid):
        o.append(insulin(x, y) if r == INS_R else glucose(x, y))
    o.append(label_bg(8, VM - 9, 81, 18, "#FFFFFF", 0.92, 5) + T(48.5, VM + 3.8, "Blood vessel", 10.5, 800, "#8E1F28", "middle"))

    # zone names
    o.append(T(10, V1 + 19, "Outside the cell", 10, 600, "#4C6070", italic=True))
    o.append(T(10, IN1 - 8, "Inside the cell", 10, 600, "#7A4A3C", italic=True))

    # insulin leaves the blood and lands in the receptor pocket (both panels: insulin still binds)
    o.append(f'<path d="M{REC_X},{V1 + 1} V{CY - 86}" stroke="{INS_EDGE}" stroke-width="1.8" stroke-dasharray="3 3" '
             f'marker-end="url(#irAy)" fill="none"/>')

    # membrane, then the proteins in it
    skips = [(REC_X, 14)] + ([(G4_X, 27)] if normal else [])
    o.append(membrane(0, PW, CY, skips))
    o.append(receptor(REC_X, CY, bound=True))

    if normal:
        # glucose travels to the open door, through it, and into the cell
        o.append(f'<path d="M{G4_X},{V1 + 1} V{CY - 31}" stroke="{GLU_EDGE}" stroke-width="1.8" stroke-dasharray="3 3" '
                 'marker-end="url(#irAp)" fill="none"/>')
        o.append(glucose(G4_X, V1 + 22) + glucose(G4_X, V1 + 50))
        o.append(glut4(G4_X, CY, True))
        o.append(glucose(G4_X, CY - 2))
        o.append(f'<path d="M{G4_X},{CY + 30} V{CY + 54}" stroke="{GLU_EDGE}" stroke-width="2.4" marker-end="url(#irAp)" fill="none"/>')
        for dx, dy in [(-24, 66), (28, 70), (54, 46), (82, 64), (2, 82), (56, 80)]:
            o.append(glucose(G4_X + dx, CY + dy))
        # the signal: from the receptor's inside end to the door
        o.append(f'<path d="M156,{CY + 44} C186,{CY + 72} 222,{CY + 70} 242,{CY + 33}" stroke="{GREEN}" stroke-width="2.8" '
                 'fill="none" marker-end="url(#irAg)" stroke-linecap="round"/>')
        o.append(marker(*M1, 1) + marker(*M2, 2) + marker(*M3N, 3))
    else:
        # no door at the surface: glucose piles up outside the cell
        pile = place(rng, [GLU_R] * 13, (166, CY - 38.5, 370, CY - 22), [], pad=1.8)
        drift = place(rng, [GLU_R] * 6, (196, V1 + 8, 368, CY - 42), [(M1[0], M1[1], 8.6, 8.6)]
                      + [(x, y, r + 4, r + 4) for x, y, r in pile], pad=5)
        for x, y, _ in pile + drift:
            o.append(glucose(x, y))
        # weak signal: fades out before it reaches the doors
        o.append(f'<path d="M156,{CY + 44} C178,{CY + 66} 200,{CY + 70} 218,{CY + 64}" stroke="#9AA3A9" stroke-width="2.6" '
                 'fill="none" stroke-dasharray="4 4" stroke-linecap="round"/>')
        xx, xy = 230, CY + 61
        o.append(f'<path d="M{xx - 6},{xy - 6} l12,12 M{xx + 6},{xy - 6} l-12,12" stroke="#C0392B" stroke-width="3" stroke-linecap="round"/>')
        o.append(vesicle(282, CY + 66, 16, [-90]) + vesicle(334, CY + 70, 15, [-90]))
        o.append(T(294, CY + 42, "Glucose doors stuck inside", 10, 700, "#7A4A3C", "middle", italic=True))
        o.append(glucose(64, CY + 46))                    # a trickle still gets in (other transporters)
        o.append(marker(*M1, 1) + marker(*M2, 2) + marker(*M3R, 3))

    # step strip
    steps = (["Insulin from the blood fits into its receptor.", "The signal opens the glucose door.",
              "Glucose moves into the cell for fuel."] if normal else
             ["Insulin still fits its receptor, but the cell barely listens.", "The signal is weak, so the glucose doors stay inside.",
              "Glucose stays in the blood, so blood sugar rises."])
    o.append(f'<path d="M0,{IN1} H{PW}" stroke="#E4E0DA" stroke-width="1"/>')
    for i, s in enumerate(steps):
        y = IN1 + 18 + i * 17
        o.append(f'<circle cx="18" cy="{y - 3.9}" r="7.6" fill="{GREEN if normal else RED}"/>'
                 + T(18, y, str(i + 1), 10.5, 800, "#FFFFFF", "middle") + T(32, y, s, 11, 600, INK))
    o.append("</g>")
    o.append(f'<rect x=".6" y=".6" width="{PW - 1.2}" height="{PH - 1.2}" rx="12" fill="none" stroke="#D3D9DE" stroke-width="1.2"/>')
    o.append("</g>")
    return "".join(o)


# ------------------------------------------------------------------ key strip
KEY_ITEMS = [  # (swatch, label, measured label width at 11 px Inter SemiBold)
    (lambda: glucose(0, 0), "Glucose (sugar)", 84.8),
    (lambda: insulin(0, 0), "Insulin", 35.0),
    (lambda: receptor(0, 3.6, bound=False, s=0.2), "Insulin receptor", 83.1),
    (lambda: glut4(0, 0, True, 0.42), "GLUT4 glucose door", 108.7),
    (lambda: (f'<g transform="scale(.6)"><rect x="-14" y="-16" width="28" height="32" fill="{CORE}"/>'
              + "".join(lipid(x, -16, True) + lipid(x, 16, False) for x in (-9.1, 0, 9.1)) + "</g>"),
     "Cell membrane", 80.1),
    (lambda: red_cell(0, 0, 0, 0.82), "Red blood cell", 74.6),
]


def key_strip(y, w=760, h=32):
    o = [f'<rect x=".6" y="{y}" width="{w - 1.2}" height="{h}" rx="8" fill="#FFFFFF" stroke="#CFD6DA" stroke-width="1.2"/>',
         T(14, y + h / 2 + 3.6, "KEY", 10.5, 800, INK, ls=1.4)]
    sw_w, gap = 24, 8
    total = sum(sw_w + gap + lw for _, _, lw in KEY_ITEMS)
    space = (w - 52 - 14 - total) / (len(KEY_ITEMS) - 1)
    x = 52
    for sw, lab, lw in KEY_ITEMS:
        o.append(f'<g transform="translate({x + sw_w / 2:.1f},{y + h / 2:.1f})">{sw()}</g>')
        o.append(T(round(x + sw_w + gap, 1), y + h / 2 + 3.9, lab, 11, 600, INK))
        x += sw_w + gap + lw + space
    return "".join(o)


def art_insulin():
    body = [ir_defs(), panel(0, True), panel(PW + 16, False), key_strip(PH + 8)]
    return svg(760, PH + 42, "".join(body),
               "Two panels. Normal: insulin from the blood binds its receptor in the cell membrane, the signal opens "
               "the GLUT4 glucose door and glucose moves into the cell. Insulin resistance: insulin binds but the signal "
               "is weak, the glucose doors stay inside the cell and glucose stays in the blood.")


# ------------------------------------------------------------------ front page
def chevrons():
    cols = [("#7D7A86", "What drives it",
             # NIDDK, Insulin Resistance & Prediabetes: excess weight/belly fat, inactivity, age 45+, family
             # history, some medicines (steroids), poor sleep; diet and stress per ADA lifestyle guidance.
             ["Sugary drinks and processed food", "Sitting most of the day", "Short sleep, long-term stress",
              "Extra fat around the belly", "Family history, age 45 or older", "Some medicines, such as steroids"]),
            ("#C2392E", "Clues to watch for",
             # NIDDK: insulin resistance and prediabetes usually have no symptoms; acanthosis nigricans and
             # skin tags can appear; high triglycerides and low HDL travel with it.
             ["Often no signs at all", "Weight gain at the waist", "Tired or foggy after meals",
              "Cravings, hungry soon after eating", "Dark velvety skin patches, skin tags", "High triglycerides, low HDL"]),
            ("#62121A", "Where it can lead",
             ["Prediabetes, then type 2 diabetes", "Heart disease and stroke", "High blood pressure",
              "Fatty liver (MASLD)", "PCOS and hormone shifts", "Memory decline"])]
    cells = "".join(f'<div style="background:{bg}"><h4>{h}</h4><ul>{"".join(f"<li>{x}</li>" for x in xs)}</ul></div>'
                    for bg, h, xs in cols)
    return f'<div class="ir-chev">{cells}</div>'


def stat():
    # CDC (Prediabetes: Your Chance to Prevent Type 2 Diabetes; National Diabetes Statistics Report):
    # 98 million U.S. adults, more than 1 in 3, have prediabetes; more than 8 in 10 of them do not know it.
    # Insulin rising years before glucose: Tabak et al., Lancet 2009 (Whitehall II trajectories).
    return ('<div class="ir-stat"><div class="n"><small>More than</small><b>1 in 3</b></div>'
            '<p>U.S. adults have prediabetes, and <b>more than 8 in 10</b> of them do not know it (CDC). Insulin often '
            'climbs years before blood sugar does, so ask {who} about a <b>fasting insulin</b> test along with the '
            'numbers below.</p></div>')


def numbers():
    def scale(title, unit, tiles):
        t = "".join(f'<div class="ir-t {c}"><i>{a}</i><b>{b}</b></div>' for c, a, b in tiles)
        return (f'<div class="ir-sc"><h4>{title} <span>{unit}</span></h4>'
                f'<div class="ir-tl">{t}<div class="ir-mine"><span>My result</span></div></div></div>')
    # American Diabetes Association, Standards of Care in Diabetes 2026, Tables 2.1 and 2.2:
    # FPG <100 normal, 100-125 prediabetes (IFG), >=126 diabetes; A1C <5.7%, 5.7-6.4%, >=6.5%.
    # Diabetes needs a confirming repeat test unless blood sugar is unmistakably high.
    scales = (scale("Fasting blood sugar", "glucose, mg/dL, after 8 hours with no food",
                    [("ok", "Normal", "under 100"), ("pre", "Prediabetes", "100 to 125"), ("dm", "Diabetes", "126 or more")])
              + scale("A1c", "average blood sugar over about 3 months",
                      [("ok", "Normal", "under 5.7%"), ("pre", "Prediabetes", "5.7 to 6.4%"), ("dm", "Diabetes", "6.5% or more")]))
    # NHLBI "Metabolic Syndrome: Diagnosis" and the AHA/NHLBI scientific statement (Grundy 2005; harmonized
    # 2009): any 3 of 5. Waist 40+ in men / 35+ in women; triglycerides 150+ mg/dL; HDL under 40 men /
    # under 50 women; blood pressure 130/85 or higher (either number counts); fasting glucose 100+ mg/dL.
    # Taking medicine for triglycerides, HDL, blood pressure or blood sugar counts as having that sign.
    signs = [("waist", "Waist", "40 in or more (men)<br>35 in or more (women)"),
             ("drop", "Triglycerides", "150 mg/dL or more"),
             ("heart", "HDL (good) cholesterol", "under 40 (men)<br>under 50 (women)"),
             ("heartpulse", "Blood pressure", "130/85 or higher<br>(either number)"),
             ("bloodsugar", "Fasting blood sugar", "100 mg/dL or more")]
    tiles = "".join(f'<div class="ir-m"><div class="ir-mtop">{icon(ic, "0.24in", sw=3.4)}<span class="ir-bx"></span></div>'
                    f'<b>{a}</b><span>{b}</span></div>' for ic, a, b in signs)
    return ('<div class="ir-nums"><div class="ir-nh"><b>Know your numbers</b><span>Write your results in the boxes, '
            'then go over them with {who}.</span></div>'
            f'<div class="ir-scales">{scales}</div>'
            '<div class="ir-msh"><b>Metabolic syndrome check</b><span>Tick each sign you have. <em>Any 3 of these 5</em> '
            'means metabolic syndrome. Taking medicine for one counts as a yes.</span></div>'
            f'<div class="ir-ms">{tiles}</div>'
            '<p class="ir-src">Sources: American Diabetes Association (a diabetes result is confirmed with a repeat test); '
            'NHLBI and American Heart Association.</p></div>')


def front(t, ed):
    return (f'<div class="irf"><div class="ir-art">{art_insulin()}</div>{chevrons()}{stat()}{numbers()}</div>')


CSS = r"""
.irf .ir-art svg{display:block;width:100%;height:auto}
.irf .ir-chev{display:grid;grid-template-columns:1fr 1fr 1fr;margin:0.07in 0 0}
.irf .ir-chev>div{padding:0.06in 0.2in 0.07in 0.3in;color:#fff;clip-path:polygon(0 0,91% 0,100% 50%,91% 100%,0 100%,7% 50%)}
.irf .ir-chev>div:first-child{clip-path:polygon(0 0,91% 0,100% 50%,91% 100%,0 100%);padding-left:0.14in}
.irf .ir-chev>div:last-child{clip-path:polygon(0 0,100% 0,100% 100%,0 100%,7% 50%)}
.irf .ir-chev h4{margin:0 0 2px;font:800 8.2pt Inter,sans-serif;letter-spacing:.08em;text-transform:uppercase}
.irf .ir-chev ul{margin:0;padding:0;list-style:none;font-size:8.1pt;line-height:1.27}
.irf .ir-stat{display:flex;gap:0.16in;align-items:center;background:var(--soft);border-radius:8px;padding:0.05in 0.16in;margin-top:0.07in}
.irf .ir-stat .n{display:flex;flex-direction:column;align-items:center;flex:none}
.irf .ir-stat .n small{font:800 7pt Inter,sans-serif;letter-spacing:.14em;text-transform:uppercase;color:var(--deep)}
.irf .ir-stat .n b{font:900 23pt/1 Merriweather,Georgia,serif;color:var(--c1);white-space:nowrap}
.irf .ir-stat p{margin:0;font-size:8.6pt;line-height:1.36;color:#2B3236}
.irf .ir-stat p b{font-weight:700;color:var(--deep)}
.irf .ir-nums{margin-top:0.07in;border:1px solid #E6D5D1;border-radius:10px;padding:0.07in 0.14in 0.07in;background:#FFFFFF}
.irf .ir-nh{display:flex;align-items:baseline;gap:10px;margin:0 0 5px}
.irf .ir-nh b{font:900 12.5pt Merriweather,Georgia,serif;color:var(--c1)}
.irf .ir-nh span{font-size:7.8pt;color:#56626A}
.irf .ir-scales{display:grid;grid-template-columns:1fr 1fr;gap:0.18in}
.irf .ir-sc h4{margin:0 0 3px;font:800 8.4pt Inter,sans-serif;color:#2B3236;white-space:nowrap}
.irf .ir-sc h4 span{font-weight:500;font-size:7.3pt;color:#5E686F}
.irf .ir-tl{display:grid;grid-template-columns:1fr 1fr 1fr 0.56in;gap:4px}
.irf .ir-t{border-radius:5px;padding:2px 3px 4px;text-align:center;border-top:3px solid}
.irf .ir-t i{display:block;font:800 7pt Inter,sans-serif;letter-spacing:.07em;text-transform:uppercase;font-style:normal}
.irf .ir-t b{display:block;font:800 10pt/1.15 Inter,sans-serif;margin-top:1px;white-space:nowrap}
.irf .ir-t.ok{background:#E4F2EA;color:#1F6B47;border-color:#2F8A5E}
.irf .ir-t.pre{background:#FCEFD4;color:#7E5300;border-color:#D99A1E}
.irf .ir-t.dm{background:#F8E1DD;color:#9A2620;border-color:#C2392E}
.irf .ir-mine{border:1.3px dashed #9AA5AC;border-radius:5px;display:flex;align-items:flex-start;justify-content:center}
.irf .ir-mine span{font:700 7pt Inter,sans-serif;color:#6A747B;margin-top:2px}
.irf .ir-msh{display:flex;align-items:baseline;gap:8px;margin:7px 0 3px;border-top:1px solid #EFE4E1;padding-top:5px}
.irf .ir-msh b{font:800 8.4pt Inter,sans-serif;color:#2B3236;white-space:nowrap}
.irf .ir-msh span{font-size:7.6pt;color:#4A555C}
.irf .ir-msh em{font-style:normal;font-weight:800;color:var(--c1)}
.irf .ir-ms{display:grid;grid-template-columns:repeat(5,1fr);gap:5px}
.irf .ir-m{display:flex;flex-direction:column;background:var(--tint);border:1px solid #EEDDD9;border-radius:6px;padding:3px 6px 4px}
.irf .ir-mtop{display:flex;justify-content:space-between;align-items:center}
.irf .ir-m .ic{flex:none;color:var(--c1)}
.irf .ir-bx{flex:none;width:0.13in;height:0.13in;border:1.6px solid var(--deep);border-radius:2px;background:#fff}
.irf .ir-m b{font-size:7.6pt;line-height:1.2;color:#2B3236;margin-top:1px}
.irf .ir-m>span{font-size:7.2pt;line-height:1.22;color:#4A555C}
.irf .ir-src{margin:4px 0 0;font-size:7pt;color:#5E686F;line-height:1.3}
"""

SHEET = {
    "slug": "insulin-resistance", "code": "ND-CM-203", "theme": "metab", "series": "Metabolic Health Series",
    "order": 5,
    "title": "Understanding Insulin Resistance", "sub": None,
    "intro": ("Insulin is a hormone your pancreas releases, especially after you eat. It is a messenger: it tells your "
              "cells to open their <b>glucose doors</b>, so sugar (glucose) can leave your blood and go into the cells "
              "for fuel. With <b>insulin resistance</b>, the cells stop listening well. Sugar backs up in the blood, so "
              "the pancreas makes more and more insulin to keep up. This can go on quietly for years before blood sugar "
              "rises high enough to be called prediabetes or type 2 diabetes."),
    "front": front,
    "css": CSS,
    # ---- back: kept exactly as the first draft (sheets.py) until the product pass
    "back": {
        "life_title": "Lifestyle-Based Medicine", "style": "circle3",
        "life": [("plate", "Low-glycemic Mediterranean plate", ["Protein first at every meal", "Half the plate vegetables", "Whole-food carbs, paired with protein or fat", "Three to five balanced meals", "Limit sugar and sweet drinks"]),
                 ("breath", "Lower stress, better sleep", ["Commit to a simple plan", "Deep breathing, 5 minutes a day", "7 to 9 hours of sleep, same times daily", "One 10-minute mindful walk a day"]),
                 ("walk", "Move your muscles", ["Walk 10 minutes after meals", "Strength training 2 to 3 times a week", "Stand up every 30 to 60 minutes", "Moderate to hard exercise 3 to 5 days a week"])],
        "cols": [
            {"p": "gluco_ir", "need": "All-in-one glucose support", "needsub": "dihydroberberine, chromium, ALA, cinnamon", "start": True,
             "bullets": ["Supports healthy glucose metabolism", "Supports insulin sensitivity"], "dose": "dose_from_db"},
            {"p": "berberine", "need": "Metabolic signaling", "needsub": "berberine",
             "bullets": ["Supports healthy glucose levels already in a normal range", "Supports healthy lipid levels"], "dose": "dose_from_db"},
            {"p": "mag_glycinate", "need": "Insulin's helper mineral", "needsub": "magnesium",
             "bullets": ["Needed for normal insulin signaling", "Low magnesium is common with high blood sugar"], "dose": "dose_from_db"},
            {"p": "omega_1000", "need": "Balance fats", "needsub": "omega-3 fatty acids",
             "bullets": ["Supports healthy triglyceride levels", "Supports a healthy inflammatory response"], "dose": "dose_from_db"},
        ],
        "rx": ["<b>Metformin</b> lowers B12 over time. Ask for a B12 check every year.",
               "<b>On diabetes medicine?</b> Berberine adds to sugar-lowering effects: check your glucose and tell your prescriber.",
               "<b>Berberine interacts</b> with some medicines (for example cyclosporine). Let your pharmacist review your list."],
    },
}
