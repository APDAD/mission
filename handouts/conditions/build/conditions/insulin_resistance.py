"""insulin-resistance sheet module (self-contained: no legacy / sheets.py / art.py drawing code).

FRONT: how insulin moves sugar into a cell, drawn at the cell wall.  Two panels, NORMAL and
INSULIN RESISTANCE, share one picture grammar:
  blood vessel (glucose = purple hexagons, insulin = gold dots, red blood cells)
  -> fluid outside the cell
  -> cell membrane: a phospholipid bilayer (two rows of round heads, paired tails), laid out
     segment by segment so every protein sits in an even, symmetric notch, holding
     the insulin receptor (Y-shaped: two alpha subunits outside the cell form the insulin
     pocket, two beta subunits cross the membrane and end in signalling domains) and
     the GLUT4 glucose door (a channel).  Spare doors wait inside the cell in STORAGE BUBBLES:
     small closed bilayers built from the same lipid unit, doors seated in the wall.
     NORMAL: the signal brings a bubble up to the surface and the door opens there.
     RESISTANCE: the signal dies out and the bubbles stay inside, so glucose piles up outside.
  -> inside the cell.
The step text sits in its own strip under each panel; the art carries only numbered markers (same
style as the strip bullets) and a few names in clear space.  One KEY names every symbol, the storage
bubble included (seven pairs), each pair fenced by hairlines so no swatch can be read with its
neighbour's label.  Below the art: what drives it / clues / where it leads, the CDC stat (only "1 in 3"
is big) and a "Know your numbers" panel (ADA glucose and A1c ranges, a fasting-insulin write-in,
NHLBI/AHA metabolic syndrome check).

BACK (product pass, 2026-11-03; reviewer fixes the same day): lifestyle band from Asher's blood-sugar
handout (10-hour eating window, slow-sugar plate) plus ADA movement and sleep; four NutriDyn protocol
products, each "In each serving" line copied from its NutriDyn sell sheet (sources in
products.d/insulin-resistance.json): Gluco IR (Start here), Berberine Pro, UltraBiotic Akkermansia Plus,
Omega Pure EPA-DHA 1000; a daily rhythm that keeps Berberine Pro's three before-meal doses; four notes per
edition (pharmacy: interactions, pregnancy, depletions, live bacteria; practitioner: labs, the prescriber
for blood-sugar medicine, the dihydroberberine overlap with pregnancy, live bacteria).  The back-page CSS
is scoped with .sheet.back:has(.ir-back), a marker span in the lifestyle title, so it cannot leak into
other sheets in the all-sheets bundle.
"""
import math
import random

from kit import ICONS
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
CY = 176                   # membrane centre line (head rows at CY -/+ 16, so the bilayer spans CY-20.6 .. CY+20.6)
IN1 = 268                  # bottom of "inside the cell"; the numbered step strip sits below
PW, PH = 372, 326
REC_X, G4_X = 130, 264.5   # receptor and GLUT4 positions (G4_X puts every membrane segment at ~9 spacing)
INS_R, GLU_R = 6.4, 5.2
VM = (V0 + V1) / 2         # vessel mid line
HEAD_R, HEAD_DY, LIPID_STEP = 4.3, 16, 9.1   # phospholipid head radius, head-row offset from CY, target spacing
REC_HW = 10.7              # receptor beta rods (with outline) half width where they cross the membrane
G4_HW = 25.15              # open GLUT4 door half width: outer helix edge + half stroke
G4_SHUT_HW, G4_HH = 20.15, 27.45   # closed door (pore shut) half width, door half height (with stroke)
M1 = (176, CY - 74)                          # step 1: next to the insulin pocket (both panels)
M2 = (152, CY + 75)                          # step 2: under the receptor, where the signal starts (both panels)
# step 3: glucose entering (normal) / left in the blood (resistance).  The resistance marker sits in clear space
# just right of the "Blood vessel" pill (pill ends at x 89), not among the molecules, which start at x 118.
M3N, M3R = (G4_X + 24, CY + 44), (102, VM)
VBOX_N, VBOX_R = (100, V0 + 5, 362, V1 - 5), (118, V0 + 5, 362, V1 - 5)   # vessel molecule boxes (8+ clear of the frame)
# Storage bubble: outer head ring radius.  With bubble()'s lipid scale 0.5 the heads reach 23.3 and the closed
# doors 25.1.  Sized up from 18.5 (2026-11-03 review) so the doors could grow to the same protein as the
# membrane door (see bubble()).  21 keeps every gap below at 4.7 or more; the suggested 22 would leave only about
# 3.7 above and below the resistance bubbles, between the caption and the step strip.
BUB_R = 21
BUB_OUT = BUB_R + (HEAD_R + 0.3) * 0.5       # outer edge of the head ring
# normal: a storage bubble arriving under the membrane, 0.8 below it, tucked against the open door's lower-left
# corner (its upper-right door 5.2 from the door's outer helix where the door ends), so the open door reads as
# the one it delivered; that bubble door already points at the corner
NB, NB_DOORS = (216, 220.7), (-30, 210)
# resistance: two bubbles stuck inside, in the band between the caption and the step strip.  Measured gaps (viewBox
# units, outlines incl. doors): 4.7 to the caption and to the strip rule, 6.3 to the X, 9.4 between the bubbles.
# Doors stay within 50 degrees of level, so no door tip sticks up into the caption or down into the strip.
RB = [((243, 240), (-35, 160)), ((299, 240), (-10, 135))]
# Resistance caption: 5.3 below the membrane's heads.  Centred at 267, 4 left of the bubbles' midpoint, because
# the 193-wide line must keep 8 clear of the frame on the right and the bubbles 6 clear of the X on the left.
CAP_X, CAP_Y = 267, CY + 33.5


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


def lipid(x, yh, down, L=11.0):
    """One phospholipid: round head at (x, yh), two wavy tails of length L pointing into the membrane."""
    s = 1 if down else -1
    y0 = yh + s * 3.9
    tails = "".join(f'<path d="M{x + dx:.2f},{y0:.2f} q-1.3,{s * L / 4:.2f} 0,{s * L / 2:.2f} t0,{s * L / 2:.2f}"/>'
                    for dx in (-1.75, 1.75))
    return (f'<g fill="none" stroke="{TAIL}" stroke-width="1.45" stroke-linecap="round">{tails}</g>'
            f'<circle cx="{x:.2f}" cy="{yh}" r="{HEAD_R}" fill="url(#irHd)" stroke="{HEAD_EDGE}" stroke-width=".6"/>')


def lipid_xs(lo, hi, blocks, clear=0.5):
    """Head centres for the bilayer between x=lo and x=hi (the frame's inner edges), laid out segment
    by segment between protein blocks [(left, right)]: even spacing inside each segment, and the end
    heads of every segment exactly `clear` from the block or frame edge, so each protein sits in a
    symmetric notch and both panel edges are cut the same way."""
    edges = [lo] + [e for b in sorted(blocks) for e in b] + [hi]
    xs = []
    for a, b in zip(edges[0::2], edges[1::2]):
        a, b = a + clear + HEAD_R + 0.3, b - clear - HEAD_R - 0.3     # 0.3 = half the head stroke
        n = max(1, round((b - a) / LIPID_STEP))
        xs += [a + i * (b - a) / n for i in range(n + 1)]
    return xs


def membrane(xs, cy):
    """Phospholipid bilayer across the panel: cream core between the head rows, one lipid pair per x."""
    return (f'<rect x="0" y="{cy - HEAD_DY}" width="{PW}" height="{2 * HEAD_DY}" fill="{CORE}"/>'
            + "".join(lipid(x, cy - HEAD_DY, True) + lipid(x, cy + HEAD_DY, False) for x in xs))


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


def bubble(cx, cy, doors, R=BUB_R, s=0.5, L=3.2, ds=0.3):
    """GLUT4 storage bubble: a closed bilayer built from the same lipid() unit as the cell membrane
    (scaled by s, with short tails), drawn the way the membrane is: a cream wall with a row of heads
    on each face and the tails meeting inside it.  Proportions (2026-11-03 review): the wall is 12.8
    units thick, 0.31 of the cell membrane's 41.2, and the doors are drawn at ds = 0.3, so a door spans
    its wall the way the big door spans the membrane (door height / wall 1.28 here, 1.33 there) and
    reads as the same protein; at the old 0.21 the doors were 1.06 walls tall and looked like tabs.  A
    real vesicle wall is as thick as the cell membrane; that one compromise is what "Cell drawing not to
    scale" under the panel covers.  Outer and inner heads share ONE list of angles, so
    every pair lines up radially.  The angles are laid out segment by segment between the doors (like
    lipid_xs): the outer heads nearly touch and stop 0.5 from each door, so every door sits in an even
    notch.  The inner face keeps a head at every one of those angles, right up to each door, and the doors
    are drawn last, on top, the way proteins sit in a bilayer (the nearest inner heads tuck half under a
    door's edge), so both leaflets run unbroken and the ring reads as one even bilayer all the way round.
    doors = angles in degrees (SVG: 0 is right, 90 is down) of the closed GLUT4 doors seated through
    the wall."""
    hr = (HEAD_R + 0.3) * s                     # head radius with stroke
    reach = (3.9 + L) * s + 0.73 * s            # head centre to tail tip (round cap included)
    ri = R - 2 * reach - 0.4                    # inner-face head centres (0.4 between tail tips)
    rc = (R + ri) / 2                           # wall centre line: the doors sit here
    dhw, dhh = G4_SHUT_HW * ds, G4_HH * ds

    def clear(a, d, rr):                        # a head at angle a on ring rr stays 0.5 clear of the door at d?
        ux, uy = rr * math.cos(a) - rc * math.cos(d), rr * math.sin(a) - rc * math.sin(d)
        v = ux * math.cos(d) + uy * math.sin(d)
        u = -ux * math.sin(d) + uy * math.cos(d)
        return math.hypot(max(abs(u) - dhw, 0), max(abs(v) - dhh, 0)) >= hr + 0.5

    dr = sorted(math.radians(d) % (2 * math.pi) for d in doors)
    half = []
    for d in dr:                                # smallest angular offset that clears each door (outer face)
        lo, hi = 0.0, math.pi / 2
        for _ in range(40):
            m = (lo + hi) / 2
            lo, hi = (lo, m) if clear(d + m, d, R) else (m, hi)
        half.append(hi)
    step = (2 * hr + 0.7) / R                   # outer heads nearly touch (as in the membrane); inner ones share the angles
    angles = []
    for i, d in enumerate(dr):
        j = (i + 1) % len(dr)
        a0, a1 = d + half[i], dr[j] + (2 * math.pi if j == 0 else 0) - half[j]
        n = max(1, round((a1 - a0) / step))
        angles += [a0 + k * (a1 - a0) / n for k in range(n + 1)]
    o = [f'<circle cx="{cx}" cy="{cy}" r="{R}" fill="{CORE}"/>',
         f'<circle cx="{cx}" cy="{cy}" r="{ri:.2f}" fill="{OUTSIDE}"/>']
    inner, outer = [], []
    for a in angles:
        for rr, rot, lst in ((R, 90, outer), (ri, -90, inner)):   # outer tails point in, inner tails point out
            lst.append(f'<g transform="translate({cx + rr * math.cos(a):.2f},{cy + rr * math.sin(a):.2f}) '
                       f'rotate({math.degrees(a) + rot:.1f}) scale({s})">{lipid(0, 0, True, L)}</g>')
    o += inner + outer
    for d in doors:
        a = math.radians(d)
        o.append(f'<g transform="translate({cx + rc * math.cos(a):.2f},{cy + rc * math.sin(a):.2f}) rotate({d + 90})">'
                 f'{glut4(0, 0, False, ds)}</g>')
    return "".join(o)


def marker(x, y, n, col):
    """Step number in the art: drawn like the step-strip bullets (panel colour, white numeral), with a
    white outline so it stands clear of busy art."""
    return (f'<circle cx="{x}" cy="{y}" r="8.6" fill="{col}" stroke="#FFFFFF" stroke-width="1.5"/>'
            + T(x, y + 3.9, str(n), 11, 800, "#FFFFFF", "middle"))


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


def settle(rng, n, x0, x1, floor, r=GLU_R, gap=1.0, slide=4.0, rows=2):
    """Drop n glucose hexagons at random x in [x0, x1] onto the membrane (lowest centre y = floor) and
    onto each other, the way sugar would pile up: each falls straight down until a face meets the
    floor or a hexagon already there, then slides up to `slide` units sideways into the lowest spot it
    can reach (so it tips off a peak into a groove instead of towering).  All hexagons share one
    orientation, so three axes (the flat faces) decide contact exactly; gap 1.0 lets the 1-unit strokes
    just touch.  At most `rows` rows.  Gives a loose, natural pile with a few touching."""
    D = 2 * 0.866 * r + gap
    out = []

    def rest(x):
        y = floor
        for px, py, _ in out:
            dx = x - px
            lo = max(-D, (-D - 0.866 * dx) / 0.5, (-D + 0.866 * dx) / 0.5)
            hi = min(D, (D - 0.866 * dx) / 0.5, (D + 0.866 * dx) / 0.5)
            if lo < hi:
                y = min(y, py + lo)
        return y

    for _ in range(5000):
        if len(out) == n:
            break
        x = rng.uniform(x0 + r, x1 - r)
        cand = [x + k * 0.25 for k in range(int(-slide * 4), int(slide * 4) + 1)]
        y, _, x = max((rest(c), -abs(c - x), c) for c in cand if x0 + r <= c <= x1 - r)
        if y >= floor - D * (rows - 1) - 0.5:
            out.append((x, y, r))
    return out


# ------------------------------------------------------------------ one panel
def placed_all(things, want, what):
    if len(things) < want:      # never drop molecules silently: the counts carry the message
        print(f"WARNING insulin-resistance art: placed {len(things)} of {want} {what}")
    return things


def panel(x0, normal):
    rng = random.Random(11 if normal else 35)     # seeds checked to place every vessel molecule
    col = GREEN if normal else RED
    cid = "irClipN" if normal else "irClipR"
    o = [f'<g transform="translate({x0},0)">',
         f'<clipPath id="{cid}"><rect width="{PW}" height="{PH}" rx="12"/></clipPath>',
         f'<g clip-path="url(#{cid})">',
         f'<rect width="{PW}" height="{PH}" fill="#FFFFFF"/>',
         # outside / inside colours run under the head rows, so no white seam shows at the bilayer edges
         f'<rect y="{HDR}" width="{PW}" height="{CY - HEAD_DY - HDR}" fill="{OUTSIDE}"/>',
         f'<rect y="{CY + HEAD_DY}" width="{PW}" height="{IN1 - CY - HEAD_DY}" fill="{INSIDE}"/>']
    # header
    o.append(f'<rect width="{PW}" height="{HDR}" fill="{col}"/>')
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
        avoid.append((M3R[0], M3R[1], 8.6 + 5, 8.6 + 5))   # step 3's marker stands well clear of the molecules
    n_ins, n_glu = (4, 6) if normal else (8, 13)            # resistance: more sugar AND more insulin in the blood
    for x, y, r in placed_all(place(rng, [INS_R] * n_ins + [GLU_R] * n_glu, VBOX_N if normal else VBOX_R, avoid),
                              n_ins + n_glu, "vessel molecules"):
        o.append(insulin(x, y) if r == INS_R else glucose(x, y))
    o.append(label_bg(8, VM - 9, 81, 18, "#FFFFFF", 0.92, 5) + T(48.5, VM + 3.8, "Blood vessel", 10.5, 800, "#8E1F28", "middle"))

    # zone names
    o.append(T(10, V1 + 19, "Outside the cell", 10, 600, "#4C6070", italic=True))
    o.append(T(10, IN1 - 8, "Inside the cell", 10, 600, "#7A4A3C", italic=True))

    # insulin leaves the blood and lands in the receptor pocket (both panels: insulin still binds)
    o.append(f'<path d="M{REC_X},{V1 + 1} V{CY - 86}" stroke="{INS_EDGE}" stroke-width="1.8" stroke-dasharray="3 3" '
             f'marker-end="url(#irAy)" fill="none"/>')

    # membrane, then the proteins in it
    blocks = [(REC_X - REC_HW, REC_X + REC_HW)] + ([(G4_X - G4_HW, G4_X + G4_HW)] if normal else [])
    o.append(membrane(lipid_xs(1.2, PW - 1.2, blocks), CY))
    o.append(receptor(REC_X, CY, bound=True))

    if normal:
        # glucose travels to the open door, through it, and into the cell.  The dashed path breaks 2 units
        # short of each travelling hexagon, so the molecules ride the path instead of being skewered by it.
        stops = [V1 + 1, V1 + 22, V1 + 50, CY - 31]
        for k, (a, b) in enumerate(zip(stops, stops[1:])):
            a, b = (a if k == 0 else a + GLU_R + 2), (b if k == len(stops) - 2 else b - GLU_R - 2)
            o.append(f'<path d="M{G4_X},{a} V{b}" stroke="{GLU_EDGE}" stroke-width="1.8" stroke-dasharray="3 3" fill="none"'
                     + (' marker-end="url(#irAp)"/>' if k == len(stops) - 2 else '/>'))
        o.append(glucose(G4_X, V1 + 22) + glucose(G4_X, V1 + 50))
        o.append(glut4(G4_X, CY, True))
        o.append(glucose(G4_X, CY - 2))
        o.append(f'<path d="M{G4_X},{CY + 30} V{CY + 54}" stroke="{GLU_EDGE}" stroke-width="2.4" marker-end="url(#irAp)" fill="none"/>')
        for dx, dy in [(-14, 70), (28, 70), (54, 46), (82, 64), (2, 82), (56, 80)]:   # first one clear of the green arrowhead
            o.append(glucose(G4_X + dx, CY + dy))
        # the signal brings a storage bubble, doors and all, up to the surface: the arrow sweeps from the
        # receptor's inside end and turns up into the bubble, which is arriving at the membrane by the door
        o.append(bubble(*NB, NB_DOORS))
        # the arrowhead tip stops 1.2 under the bubble; the irAg marker reaches 4.1 past the path end at stroke 2.8
        end = NB[1] + BUB_OUT + 1.2 + 4.1
        o.append(f'<path d="M157.5,{CY + 35} C172,{CY + 74} {NB[0]},{end + 18.5:.1f} {NB[0]},{end:.1f}" stroke="{GREEN}" '
                 'stroke-width="2.8" fill="none" marker-end="url(#irAg)" stroke-linecap="round"/>')
        o.append(marker(*M1, 1, col) + marker(*M2, 2, col) + marker(*M3N, 3, col))
    else:
        # no door at the surface: glucose piles up on the membrane (2 loose rows), more drifts above it
        floor = CY - HEAD_DY - HEAD_R - 0.3 - 0.866 * GLU_R - 0.5 - 0.3
        pile = placed_all(settle(random.Random(PILE_SEED), 13, 166, 368, floor), 13, "pile glucose")
        top = min(y for _, y, _ in pile) - 0.866 * GLU_R
        drift = placed_all(place(rng, [GLU_R] * 6, (196, V1 + 8, 366, top - 6), [(M1[0], M1[1], 8.6 + 4, 8.6 + 4)]
                                 + [(x, y, r + 4, r + 4) for x, y, r in pile], pad=5), 6, "drifting glucose")
        for x, y, _ in pile + drift:
            o.append(glucose(x, y))
        # weak signal: fades out before it reaches the doors
        o.append(f'<path d="M157.5,{CY + 35} C170,{CY + 60} 182,{CY + 70} 196,{CY + 69}" stroke="#9AA3A9" stroke-width="2.6" '
                 'fill="none" stroke-dasharray="4 4" stroke-linecap="round"/>')
        xx, xy = 204, CY + 68
        o.append(f'<path d="M{xx - 5.5},{xy - 5.5} l11,11 M{xx + 5.5},{xy - 5.5} l-11,11" stroke="#C0392B" stroke-width="3" stroke-linecap="round"/>')
        for c, doors in RB:
            o.append(bubble(*c, doors))
        o.append(T(CAP_X, CAP_Y, "Glucose doors stuck in storage bubbles", 10, 700, "#7A4A3C", "middle", italic=True))
        o.append(marker(*M1, 1, col) + marker(*M2, 2, col) + marker(*M3R, 3, col))

    # step strip: the art's symbols are named here too (green arrow, grey dashes and the X, the storage bubbles),
    # and resistance step 3 says why that vessel holds twice the insulin (NIDDK: the pancreas makes more insulin
    # to keep blood glucose in a healthy range).  Every line measured at 11 Inter SemiBold: 324 to 328 units
    # against the 330 between x 32 and the frame margin.
    steps = (["Insulin from the blood fits into its receptor.",
              "The signal (green arrow) raises a bubble of doors. One opens.",
              "Glucose moves into the cell for fuel."] if normal else
             ["Insulin still fits its receptor, but the cell barely listens.",
              "The signal (grey dashes) dies at the X. Doors stay in bubbles.",
              "Glucose stays in the blood. The pancreas makes more insulin."])
    o.append(f'<path d="M0,{IN1} H{PW}" stroke="#E4E0DA" stroke-width="1"/>')
    for i, s in enumerate(steps):
        y = IN1 + 18 + i * 17
        o.append(f'<circle cx="18" cy="{y - 3.9}" r="7.6" fill="{col}"/>'
                 + T(18, y, str(i + 1), 10.5, 800, "#FFFFFF", "middle") + T(32, y, s, 11, 600, INK))
    o.append("</g>")
    o.append(f'<rect x=".6" y=".6" width="{PW - 1.2}" height="{PH - 1.2}" rx="12" fill="none" stroke="#D3D9DE" stroke-width="1.2"/>')
    o.append("</g>")
    return "".join(o)


PILE_SEED = 7          # picked by eye from seeds 1-8: two loose rows, a few touching, no towers


# ------------------------------------------------------------------ key strip
def _membrane_swatch():
    return (f'<g transform="scale(.6)"><rect x="-14" y="-16" width="28" height="32" fill="{CORE}"/>'
            + "".join(lipid(x, -16, True) + lipid(x, 16, False) for x in (-9.1, 0, 9.1)) + "</g>")


KEY_ITEMS = [  # (swatch drawn at 0,0, swatch half width incl. stroke, label, label advance at 10 px Inter 600)
    # advances measured with getComputedTextLength in the rendered sheet (same @font-face Inter as the art)
    (lambda: glucose(0, 0), 5.7, "Glucose (sugar)", 76.96),
    (lambda: insulin(0, 0), 6.9, "Insulin", 31.8),
    (lambda: receptor(0, 3.5, bound=False, s=0.19), 6.0, "Insulin receptor", 75.37),
    (lambda: glut4(0, 0, True, 0.42), 10.6, "GLUT4 glucose door", 98.64),
    # the storage bubble, a scaled copy of the normal panel's bubble (doors and all): 2026-11-03 review, the one
    # symbol a patient could not guess, unlabelled in the NORMAL panel
    (lambda: f'<g transform="scale(.55)">{bubble(0, 0, NB_DOORS)}</g>', 13.7, "Storage bubble", 73.57),
    (_membrane_swatch, 8.4, "Cell membrane", 72.7),
    (lambda: red_cell(0, 0, 0, 0.82), 10.6, "Red blood cell", 67.71),
]
KEY_H, KEY_TITLE_W, KEY_PAIR_GAP, KEY_MARGIN, KEY_SIZE = 34, 26.3, 4, 10, 10


def key_strip(y, w=760, h=KEY_H):
    """One row: KEY, then swatch + label pairs.  Each pair is sized from its real swatch width, 4 units
    from swatch to label, and the leftover width is spread evenly between pairs (about 9 units) with a
    hairline divider in the middle of each gap, so no swatch reads with its neighbour's label.  Seven
    pairs fit one row with labels at 10 units, which prints at 7.3 pt (the viewBox is 760 units across
    the 7.66 in column)."""
    o = [f'<rect x=".6" y="{y}" width="{w - 1.2}" height="{h}" rx="8" fill="#FFFFFF" stroke="#CFD6DA" stroke-width="1.2"/>',
         T(KEY_MARGIN, y + h / 2 + 3.7, "KEY", 10.5, 800, INK, ls=1.4)]
    used = sum(2 * hw + KEY_PAIR_GAP + lw for _, hw, _, lw in KEY_ITEMS)
    x = KEY_MARGIN + KEY_TITLE_W
    gap = (w - KEY_MARGIN - x - used) / len(KEY_ITEMS)
    for sw, hw, lab, lw in KEY_ITEMS:
        o.append(f'<path d="M{x + gap / 2:.2f},{y + 8} V{y + h - 8}" stroke="#DCE2E6" stroke-width="1"/>')
        x += gap
        o.append(f'<g transform="translate({x + hw:.2f},{y + h / 2:.2f})">{sw()}</g>')
        o.append(T(round(x + 2 * hw + KEY_PAIR_GAP, 2), y + h / 2 + 3.6, lab, KEY_SIZE, 600, INK))
        x += 2 * hw + KEY_PAIR_GAP + lw
    return "".join(o)


def art_insulin():
    body = [ir_defs(), panel(0, True), panel(PW + 16, False), key_strip(PH + 8)]
    return svg(760, PH + 10 + KEY_H, "".join(body),
               "Two panels. Normal: insulin from the blood binds its receptor in the cell membrane, the signal brings a "
               "storage bubble of GLUT4 glucose doors up to the surface, the door opens and glucose moves into the cell. "
               "Insulin resistance: insulin binds but the signal is weak, the glucose doors stay inside the cell in "
               "storage bubbles and glucose piles up outside and stays in the blood.")


# ------------------------------------------------------------------ front page
IR_ICONS = {  # same 64x64 line-icon contract as kit.ICONS
    "tape": ('<circle cx="23" cy="26" r="16"/><circle cx="23" cy="26" r="4.5"/>'
             '<path d="M23 42h35v10H23z"/><path d="M33 42v5M41 42v7M49 42v5"/>'),          # tape measure: waist
    "tube": ('<path d="M25 7v38a7 7 0 0 0 14 0V7"/><path d="M20 7h24"/><path d="M25 27h14"/>'
             '<path d="M30 35v1M34 40v1"/>'),                                                   # test tube: triglycerides
    "gauge": ('<circle cx="32" cy="35" r="22"/><path d="M32 35 44 22"/><path d="M15 35h5M44 35h5M32 18v5M20 23l3.5 3.5"/>'
              '<circle cx="32" cy="35" r="3" fill="currentColor" stroke="none"/>'),            # pressure dial: blood pressure
}


def ir_icon(name, size, sw=3.4):
    body = IR_ICONS.get(name) or ICONS[name]
    return (f'<svg class="ic" viewBox="0 0 64 64" style="width:{size};height:{size}" fill="none" stroke="currentColor" '
            f'stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{body}</svg>')


def chevrons():
    cols = [("#67646F", "What drives it",      # white text on #67646F is 5.8:1 (the old #7D7A86 was 4.2:1)
             # NIDDK, Insulin Resistance & Prediabetes: excess weight/belly fat, inactivity, age 45+, family
             # history, some medicines (steroids), poor sleep; diet and stress per ADA lifestyle guidance.
             ["Sugary drinks and processed food", "Sitting most of the day", "Short sleep, long-term stress",
              "Extra fat around the belly", "Family history, age 45 or older", "Some medicines, such as steroids"]),
            # "good HDL" glosses HDL in one line (168 px of the 197 px column at 8.1 pt)
            ("#C2392E", "Clues to watch for",
             # NIDDK, Insulin Resistance & Prediabetes: insulin resistance and prediabetes usually have no
             # symptoms and are found with blood tests (fasting glucose, A1c); some people have darkened skin
             # in the armpit or on the back and sides of the neck (acanthosis nigricans), and many small skin
             # tags often appear in these same areas.  High fasting insulin: the pancreas over-produces insulin
             # to keep glucose normal (NIDDK), and fasting insulin climbs years before glucose does (Tabak et
             # al., Lancet 2009).  High triglycerides and low HDL travel with it (NHLBI metabolic syndrome).
             ["Often no signs at all", "Blood sugar creeping up on labs", "High fasting insulin on a lab test",
              "Dark skin at the neck or armpits", "Skin tags in those same spots", "High triglycerides, low good HDL"]),
            # NIDDK: insulin resistance raises the risk of type 2 diabetes, heart disease and stroke, high blood
            # pressure, fatty liver disease (MASLD, named here in plain words) and is linked to PCOS; AHA/NHLBI.
            # Memory and thinking: higher HOMA-IR and fasting insulin predicted a steeper 11-year decline in verbal
            # fluency in 3,695 adults (Ekblad LL et al., Diabetes Care 2017;40:751-758, PMID 28381479; it did not
            # predict word-list recall, hence "memory and thinking", not "memory"), and diabetes is one of the 14
            # modifiable dementia risks (Livingston G et al., Lancet Commission 2024, Lancet 2024;404:572-628,
            # PMID 39096926).  Both read on PubMed 2026-11-03.
            ("#62121A", "Where it can lead",
             ["Prediabetes, then type 2 diabetes", "Heart disease and stroke", "High blood pressure",
              "Fatty liver disease", "PCOS and hormone shifts", "Memory and thinking problems"])]
    cells = "".join(f'<div style="background:{bg}"><h4>{h}</h4><ul>{"".join(f"<li>{x}</li>" for x in xs)}</ul></div>'
                    for bg, h, xs in cols)
    return f'<div class="ir-chev">{cells}</div>'


def stat(ed):
    # CDC (Prediabetes: Your Chance to Prevent Type 2 Diabetes; National Diabetes Statistics Report):
    # 98 million U.S. adults, more than 1 in 3, have prediabetes; more than 8 in 10 of them do not know it.
    # Insulin rising years before glucose: Tabak et al., Lancet 2009 (Whitehall II trajectories).
    # Who orders the test: in the practitioner edition the provider handing over the sheet orders it, so the
    # sentence names the same person as Know your numbers ({who} = your provider).  In the pharmacy edition
    # it stays "your doctor": fasting insulin is a blood test a prescriber orders, which most pharmacists
    # cannot do, while the pharmacist is the one Know your numbers sends the results to.
    asker = ed["who"] if ed.get("rx_title") == "Provider check" else "your doctor"
    return ('<div class="ir-stat"><div class="n"><small>More than</small><b>1 in 3</b></div>'
            '<p>U.S. adults have prediabetes, and <b>more than 8 in 10</b> of them do not know it (CDC). Insulin often '
            f'climbs years before blood sugar does, so ask {asker} about a <b>fasting insulin</b> test along with the '
            'numbers below.</p></div>')


def numbers():
    def scale(title, unit, tiles):
        t = "".join(f'<div class="ir-t {c}"><i>{a}</i><b>{b}</b></div>' for c, a, b in tiles)
        return (f'<div class="ir-sc"><h4>{title} <span>{unit}</span></h4>'
                f'<div class="ir-tl">{t}<div class="ir-mine"><span>My result</span></div></div></div>')
    # American Diabetes Association, Standards of Care in Diabetes (Section 2, Diagnosis and Classification):
    # FPG <100 normal, 100-125 prediabetes (IFG), >=126 diabetes; A1C <5.7%, 5.7-6.4%, >=6.5%.
    # Diabetes needs a confirming repeat test unless blood sugar is unmistakably high.
    scales = (scale("Fasting blood sugar", "mg/dL, after 8 hours with no food",
                    [("ok", "Normal", "under 100"), ("pre", "Prediabetes", "100 to 125"), ("dm", "Diabetes", "126 or more")])
              + scale("A1c", "average blood sugar over about 3 months",
                      [("ok", "Normal", "under 5.7%"), ("pre", "Prediabetes", "5.7 to 6.4%"), ("dm", "Diabetes", "6.5% or more")]))
    # NHLBI "Metabolic Syndrome: Diagnosis" and the AHA/NHLBI scientific statement (Grundy 2005; harmonized
    # 2009): any 3 of 5. Waist 40+ in men / 35+ in women; triglycerides 150+ mg/dL; HDL under 40 men /
    # under 50 women; blood pressure 130/85 or higher (either number counts); fasting glucose 100+ mg/dL.
    # Taking medicine for triglycerides, HDL, blood pressure or blood sugar counts as having that sign.
    signs = [("tape", "Waist", "40 inches or more (men)<br>35 inches or more (women)"),
             ("tube", "Triglycerides", "150 mg/dL or more"),
             ("heart", "HDL (good) cholesterol", "under 40 mg/dL (men)<br>under 50 mg/dL (women)"),
             ("gauge", "Blood pressure", "130/85 or higher<br>(either number)"),
             ("bloodsugar", "Fasting blood sugar", "100 mg/dL or more")]
    tiles = "".join(f'<div class="ir-m"><div class="ir-mtop">{ir_icon(ic, "0.24in")}<span class="ir-bx"></span></div>'
                    f'<b>{a}</b><span>{b}</span></div>' for ic, a, b in signs)
    # Fasting insulin write-in: no cutoff is printed because none is set.  The ADA Standards of Care do not
    # use insulin to diagnose anything and insulin assays are not standardized between labs, so the patient
    # copies the lab's own reference range next to the result.  Both write-ins are dashed boxes like every
    # other write-in on the page; "Fill in" is said by the boxes themselves ("My result"), so the sub-line
    # keeps only who to review them with, which leaves each box about 0.75 in wide.
    return ('<div class="ir-nums"><div class="ir-nh"><b>Know your numbers</b><span class="ir-sub">Review your results '
            'with {who}.</span>'
            '<span class="ir-fi"><b>Fasting insulin</b><i></i>&micro;IU/mL<em>Lab range</em><i></i></span></div>'
            f'<div class="ir-scales">{scales}</div>'
            '<div class="ir-msh"><b>Metabolic syndrome check</b><span>Tick each sign you have. If you take medicine for '
            'one, tick it. <em>Any 3 of these 5</em> means metabolic syndrome.</span></div>'
            f'<div class="ir-ms">{tiles}</div>'
            '<p class="ir-src">Sources: American Diabetes Association (a diabetes result is confirmed with a repeat test); '
            'NHLBI and American Heart Association. Cell drawing not to scale.</p></div>')


def front(t, ed):
    return (f'<div class="irf"><div class="ir-art">{art_insulin()}</div>{chevrons()}{stat(ed)}{numbers()}</div>')


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
.irf .ir-nh{display:flex;align-items:baseline;gap:8px;margin:0 0 5px}
.irf .ir-nh>b{flex:none;font:900 12.5pt Merriweather,Georgia,serif;color:var(--c1);white-space:nowrap}
.irf .ir-nh .ir-sub{flex:none;font-size:7.8pt;color:#56626A;white-space:nowrap}
.irf .ir-nh .ir-fi{flex:1 1 auto;min-width:0;display:flex;justify-content:flex-end;align-items:baseline;gap:3px;
  white-space:nowrap;font-size:7.8pt;color:#2B3236}
.irf .ir-fi b,.irf .ir-fi em{flex:none;font:800 7.8pt Inter,sans-serif;font-style:normal;color:#2B3236}
.irf .ir-fi em{margin-left:7px}
.irf .ir-fi i{flex:0 1 0.78in;min-width:0.62in;height:0.16in;align-self:center;border:1.3px dashed #9AA5AC;
  border-radius:4px;background:#fff}
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
.irf .ir-ms{display:grid;grid-template-columns:1.22fr .9fr 1.1fr .88fr .9fr;gap:5px}
.irf .ir-m{display:flex;flex-direction:column;background:var(--tint);border:1px solid #EEDDD9;border-radius:6px;padding:3px 6px 4px}
.irf .ir-mtop{display:flex;justify-content:space-between;align-items:center}
.irf .ir-m .ic{flex:none;color:var(--c1)}
.irf .ir-bx{flex:none;width:0.13in;height:0.13in;border:1.6px solid var(--deep);border-radius:2px;background:#fff}
.irf .ir-m b{font-size:7.6pt;line-height:1.2;color:#2B3236;margin-top:1px}
.irf .ir-m>span{font-size:7.2pt;line-height:1.22;color:#4A555C}
.irf .ir-src{margin:4px 0 0;font-size:7pt;color:#5E686F;line-height:1.3}
"""

# Back page: the shared back layout has no sheet class, so every rule is scoped with :has() to the marker
# span in this sheet's lifestyle title and cannot leak into the other sheets of the all-sheets bundle.
BACK_CSS = r"""
/* Gluco IR's label line (eleven ingredients) is the longest */
.sheet.back:has(.ir-back) .cols{grid-template-columns:1.34fr 1fr 1fr 1fr!important}
/* a little less red above and below the lifestyle cards (shared 0.3 in / 0.18 in) so the footer stays on the page */
.sheet.back:has(.ir-back) .band{padding-top:0.22in!important;padding-bottom:0.14in}
.sheet.back:has(.ir-back) .band h2{margin-bottom:0.07in}
/* the morning list is the longest, bedtime holds one capsule */
.sheet.back:has(.ir-back) .rhythm{grid-template-columns:1.4fr 1.1fr .8fr}
/* the rx panel (four notes, 12 lines) sets the row's height: the rhythm slots grow to match it instead of
   leaving a gap under the pill total */
.sheet.back:has(.ir-back) .duo>.panel:first-child{display:flex;flex-direction:column}
.sheet.back:has(.ir-back) .duo>.panel:first-child .rhythm{flex:1}
/* lifestyle discs a little smaller so each bullet line holds about 28 characters */
.sheet.back:has(.ir-back) .life.l3 .disc2{width:0.68in;height:0.68in}
"""

SHEET = {
    "slug": "insulin-resistance", "code": "ND-CM-203", "theme": "metab", "series": "Metabolic Health Series",
    "order": 5,
    "title": "Understanding Insulin Resistance", "sub": None,
    # NIDDK, Insulin Resistance & Prediabetes: the pancreas makes more insulin to keep blood glucose in a healthy
    # range; over time it cannot keep up and glucose rises into prediabetes and type 2 diabetes.
    "intro": ("Insulin is a hormone your pancreas releases, especially after you eat. It is a messenger: it tells your "
              "cells to open their <b>glucose doors</b>, so sugar (glucose) can leave your blood and go into the cells "
              "for fuel. With <b>insulin resistance</b>, the cells stop listening well. Sugar starts to back up, so the "
              "pancreas pushes out more and more insulin to keep blood sugar normal. This can go on quietly for years "
              "before blood sugar climbs high enough to be called prediabetes or type 2 diabetes."),
    "front": front,
    "css": CSS + BACK_CSS,
    "back": {
        # the span marks this sheet's back page for the scoped CSS (.sheet.back:has(.ir-back))
        "life_title": 'Lifestyle-Based Medicine<span class="ir-back"></span>',
        # Asher's blood-sugar handout: "Three levers, one plan" (when you eat, what you eat; his third lever is
        # Gluco IR, which sits in the products below).  NIDDK: physical activity and weight loss help the body
        # respond better to insulin.  No disease words: the line sits over the product page.
        "life_sub": "When you eat, what you eat and how you move: three levers that help your cells answer insulin",
        "style": "circle3",
        "life": [
            # Asher's blood-sugar patient handout (repo handouts/blood-sugar-patient-handout.pdf), from the Viple
            # 2026 meta-analysis of time-restricted eating (10 RCTs, 599 adults, windows 4 to 10 hours, about 4
            # months): "A common starting point: 10 hrs"; "Keep the same hours: most days" and do not stretch the
            # window "later and later on weekends"; water, sparkling water, herbal tea, black coffee "are fine
            # during your fasting hours. Nothing with sugar in it."; "Talk to your provider first if: you already
            # take anything for blood sugar".  8 AM to 6 PM: the protocol research's worked example.
            # "Plain tea" (2026-11-03 review): the handout's "herbal tea" and "Nothing with sugar in it" in two
            # words, since in Atlanta "tea" alone often means sweet tea.  The title drops its "A" so it fits one
            # line: this card set the band's height, and the line it frees pays for the fourth rx note below.
            ("clock", "10-hour eating window",
             ["Example: 8 AM to 6 PM", "Same hours, weekends too",
              "Outside it: water, plain tea or black coffee", "On blood sugar medicine? Ask your doctor first"]),
            # Same handout, page 2 (Sun 2026 meta-analysis of low-glycemic-index eating, 25 RCTs, 1,973 people):
            # "Low glycemic index simply means foods that raise blood sugar slowly" -> "slow-sugar plate" (no
            # jargon); half the plate non-starchy vegetables; "vegetables and protein first, slow carbohydrate
            # last"; slow carbs "about a fist"; "Whole fruit only. Juice delivers the sugar without the fiber".
            ("plate", "A slow-sugar plate",
             ["Non-starchy veggies: half the plate", "Veggies and protein first",
              "Slow carbs last, about a fist", "Whole fruit, not juice"]),
            # ADA Standards of Care in Diabetes 2025, Section 5: resistance exercise 2 to 3 sessions a week on
            # nonconsecutive days; interrupt prolonged sitting every 30 minutes.  Walking after meals: Reynolds AN
            # et al., Diabetologia 2016 (10 minutes after each meal beat one 30-minute walk for after-meal glucose).
            # The NutriDyn GLC 2026 insulin-resistance protocol PDF adds resistance training.  Sleep: National Sleep
            # Foundation, 7 to 9 hours for adults (the front lists short sleep as a driver).
            ("walk", "Move often, sleep well",
             ["Walk 10 minutes after meals", "Strength training 2 to 3 days a week",
              "Stand up every 30 minutes", "Sleep 7 to 9 hours a night"]),
        ],
        # Products (4, the competitor sheet's count), all from NutriDyn protocols: Asher's blood-sugar handout and
        # "Own Every Protocol" HbA1c path (Gluco IR + Berberine Pro), the NutriDyn GLC 2026 insulin-resistance
        # protocol PDF (Dropbox id:xHepYs_Ou4AAAAAAAA7hTA: Berberine Pro, Alpha-Lipoic Acid 200 mg, Omega Pure
        # EPA-DHA 1000 where triglycerides are raised) and the NutriDyn GLC 2024 metabolic-syndrome protocol PDF
        # (Dropbox id:xHepYs_Ou4AAAAAAAArn2A: UltraBiotic Akkermansia Plus).
        # Competitor categories: chromium AND alpha lipoic acid -> Gluco IR (600 mcg chromium picolinate, 300 mg
        # alpha lipoic acid), berberine -> Berberine Pro; vanadyl sulfate has no NutriDyn equivalent (scratchpad
        # products/needs.md).
        # OPEN ITEM, ALPHA-LIPOIC ACID (2026-11-03 review): the protocol brief's lineup is Gluco IR, Berberine Pro,
        # Alpha-Lipoic Acid R270 and Omega OR Akkermansia.  R270 (200 mg, label facts in products.d as ir_ala) is
        # held back only for its photo: the one staged R270 image is another brand's bottle (Progressive
        # Professional P872, 60 capsules) and must not be used.  The R196 Akkermansia photo is a 160 px thumbnail
        # too, so the swap waits on a print master for either bottle.  Dropbox /NutriDyn/Product Images/Product
        # Images (1)/ holds R270R.png (id:xHepYs_Ou4AAAAAAAA5I7g, 99,335 bytes) and R196.png
        # (id:xHepYs_Ou4AAAAAAAA5Ipw, 86,496 bytes), but both sit in the byte range of that folder's 420 px web
        # renders (its _Web files match the repo's 420 px bottles byte for byte), so they are probably web size,
        # not 600 px print masters; their pixel size is unverified (content host blocked, metadata has none).
        # When a real R270 master is staged as build/img-src/ir_ala.png: replace the ir_akk column with
        #   {"p": "ir_ala", "need": "Antioxidant energy support", "needsub": "alpha-lipoic acid 200 mg",
        #    "dose": "dose_from_db", "bullets": ["Supports healthy blood sugar balance", "Supports energy production"]}
        # (ND283's own claims), keep Omega as column 4, add "Gluco IR already gives 300 mg alpha-lipoic acid, so
        # 500 mg a day in total" to the overlap note, drop the live-bacteria note, narrow the now-empty Bedtime slot
        # in BACK_CSS, and re-render: the Morning box grows by one line.
        # Label facts, doses and sources: products.d/insulin-resistance.json.  Card claims are the NutriDyn sell
        # sheets' own structure/function wording (ND506, ND1130, ND1194, ND416), all read 2026-11-03; ND1130, ND1194
        # and ND416 re-opened for the review.
        # Start here: Gluco IR, Asher's lead insulin-resistance formula ("IR = Insulin Resistance"), which carries
        # the chromium, alpha-lipoic acid and dihydroberberine in one bottle.
        "cols": [
            # needsub spells out alpha-lipoic acid (203 px of the 206 px line); cinnamon is in the label line
            {"p": "ir_gluco_ir", "need": "All-in-one glucose support",
             "needsub": "dihydroberberine, chromium, alpha-lipoic acid", "start": True, "dose": "dose_from_db",
             # both bullets open with the claim verb, so build.py ties each to the FDA disclaimer diamond
             "bullets": ["Promotes healthy blood glucose levels already in the normal range",
                         "Supports the normal action of insulin (chromium)"]},
            # ND1130: dihydroberberine "works primarily through the activation of AMPK, a central regulator of
            # cellular energy balance" -> "Cell energy switch"
            {"p": "ir_berberine", "need": "Cell energy switch", "needsub": "dihydroberberine + cinnamon",
             "dose": "dose_from_db",
             "bullets": ["Promotes healthy glucose metabolism", "Supports heart health and healthy lipid balance"]},
            # ND1194: "Support healthy glucose metabolism", "Promote effective weight management", "Promote
            # healthy gut barrier function"
            {"p": "ir_akk", "need": "Friendly gut bacteria", "needsub": "Akkermansia + 4 probiotic strains",
             "dose": "dose_from_db",
             "bullets": ["Supports healthy glucose metabolism", "Supports healthy weight and a healthy gut lining"]},
            # The GLC 2026 protocol uses it "where triglycerides are raised", but ND416 (Rev. 4/25, re-opened) makes no
            # triglyceride claim, so neither does the card: bullet 1 is ND416's "Healthy cardiovascular function";
            # bullet 2 is ND416's EPA and DHA as "integral components of membrane phospholipids", found "especially
            # in cell membranes" (the membrane the front page draws).  The need names the nutrient (ND416: omega-3s
            # are "essential" because the body does not make them) instead of the old "Healthy blood fats", which
            # implied the triglyceride claim.  "in the body" keeps "membranes" off a line of its own.
            {"p": "ir_omega", "need": "Essential omega-3 fats", "needsub": "EPA + DHA from fish oil",
             "dose": "dose_from_db",
             "bullets": ["Supports healthy cardiovascular function",
                         "Supports healthy cell membranes in the body"]},
        ],
        # Four notes per edition (2026-11-03 review).  Pharmacists check interactions, pregnancy and depletions;
        # providers order labs, and a change to a blood-sugar medicine goes to the doctor who prescribes it (most
        # DCs and NDs cannot adjust insulin or a sulfonylurea).  The medicine notes are cautions, never "adds to
        # the drug's effect": wording that a product augments a drug action reads as an implied disease claim
        # (21 CFR 101.93(g)(2)).  Product names carry no-break spaces so "Gluco / IR" cannot split.
        # Sources: dihydroberberine 100 mg per 5 Gluco IR capsules (ND506) + 100 mg per Berberine Pro capsule x 3
        # (ND1130) = 400 mg a day.  Guo Y et al., Eur J Clin Pharmacol 2012;68:213-217, PMID 21870106,
        # doi:10.1007/s00228-011-1108-2 (berberine 300 mg three times daily for 2 weeks lowered CYP2D6, 2C9 and 3A4
        # activity: a plain-berberine result, so the sheet says "can slow" / "can change"); Wu X et al., Eur J Clin
        # Pharmacol 2005;61:567-572, PMID 16133554, doi:10.1007/s00228-005-0952-3 (berberine 0.2 g three times daily
        # raised cyclosporine levels in kidney-transplant patients).  Low-sugar risk on insulin and sulfonylureas:
        # ADA Standards of Care 2025, Sections 6 and 9; NIH ODS chromium fact sheet; MedlinePlus alpha-lipoic acid,
        # gymnema and berberine monographs (all in Gluco IR; berberine also in Berberine Pro).
        # Pregnancy and breastfeeding: berberine displaces bilirubin from albumin about tenfold more than
        # phenylbutazone and is "best avoided in jaundiced neonates and pregnant women" (Chan E, Biol Neonate
        # 1993;63:201-208, PMID 8513024, doi:10.1159/000243932, read on PubMed 2026-11-03); MedlinePlus Berberine
        # (Natural Medicines) rates it likely unsafe in pregnancy and breastfeeding (newborn kernicterus), per the
        # 2026-11-03 review (medlineplus.gov is outside this session's network, not re-opened).  The ND506 and
        # ND1130 labels say only "If you are pregnant, nursing ... consult".  Same caution as gut_overgrowth's
        # "Pregnant or nursing?" line for its berberine products.
        # Live bacteria: Akkermansia Plus is 80% pasteurized and 20% live A. muciniphila (100 million CFU live) plus
        # live B. animalis HN019 and B420, L. rhamnosus GG and C. butyricum (ND1194, re-opened 2026-11-03).
        # Probiotics carry more risk with a weak immune system (NCCIH, "Probiotics: What You Need To Know", per the
        # review, not re-opened; Doron S, Snydman DR, Clin Infect Dis 2015;60 Suppl 2:S129-34, PMID 25922398,
        # systemic infections in susceptible people; Yelin I et al., Nat Med 2019;25:1728-1732, PMID 31700189,
        # bacteremia traced to the capsule's strain in ICU patients).  Cyclosporine users are immune-suppressed.
        # Metformin and B12: ADA Standards of Care 2025, Section 9 ("consider periodic measurement of vitamin B12").
        # Biotin: FDA Safety Communication 2017, updated 2019 (biotin can cause incorrect results in some lab
        # tests); Gluco IR has 2,000 mcg (ND506).  Recheck at about 3 months: A1c reflects about 3 months (front).
        # Fit, measured in the rendered PDF: 12 lines per edition (was 11), no one-word last line; the free line
        # comes from the lifestyle title above.
        "rx": {
            "practitioner": [
                "<b>Labs now and in about 3 months:</b> fasting glucose, A1c, fasting insulin and lipids, plus B12 "
                "if you take metformin. Gluco&nbsp;IR&rsquo;s biotin can throw off some tests: tell the lab.",
                "<b>On medicine for blood sugar?</b> Before you start, tell the doctor who prescribes it: the dose "
                "may need a change. Check your sugar more often at first.",
                "<b>Two products, one ingredient.</b> Gluco&nbsp;IR and Berberine&nbsp;Pro both have "
                "dihydroberberine, 400&nbsp;mg a day together. Avoid both if pregnant or breastfeeding. It can "
                "change how drugs like cyclosporine clear: ask {who} if you need both.",
                "<b>Weak immune system</b> or on cyclosporine? Ask {who} before Akkermansia&nbsp;Plus: it has "
                "live bacteria.",
            ],
            "pharmacy": [
                "<b>Two products, one ingredient.</b> Gluco&nbsp;IR and Berberine&nbsp;Pro both contain "
                "dihydroberberine, 400&nbsp;mg a day together. Avoid both if pregnant or breastfeeding. It can "
                "slow the liver enzymes (CYP3A4, 2D6, 2C9) that clear drugs such as cyclosporine: bring your "
                "full list.",
                "<b>Insulin or a sulfonylurea</b> (such as glipizide)? Ask your prescriber before you start, and "
                "watch for low blood sugar.",
                "<b>Metformin</b> can lower B12 over time: ask about a regular check. Gluco&nbsp;IR has "
                "2,000&nbsp;mcg biotin, which can throw off some lab tests: tell the lab.",
                "<b>Weak immune system</b> or on cyclosporine? Ask {who} before Akkermansia&nbsp;Plus: it has "
                "live bacteria.",
            ],
        },
    },
}
