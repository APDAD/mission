"""Intestinal Permeability ("leaky gut"), sheet ND-GI-101.

Self-contained: the front-page art, the front builder, the copy and the back-page data all live
here.  Shared drawing helpers come from svgkit (T, svg, TOXIN) and kit (icon).  Every SVG id and CSS
class carries the "ipx" prefix because all sheets share one document in the bundle PDFs.

Front art, per Asher's notes (2026-11-03), the art director's review of the first redraw and the final
front recheck (2026-11-03, scratchpad wf/front_rechecks_A.json):
  - five tabs (Nutrients, Food particles, Microbes, Medications, Stress).  Each tinted lane holds
    only its own tab's items, and nothing that leaks starts inside a lane: the leak streams begin
    at the gap mouths, in the clear band between the lanes and the cells;
  - healthy half: C, Fe and Zn (water-soluble, so they really go straight into the blood; vitamin D
    stays in the lane) leave the Nutrients lane, ride a green arrow through the cytoplasm beside the
    nucleus and arrive in the blood (the same three letters all the way); the seams, the healthy |
    leaky seam included, stay sealed by the key's three-bar tight junction;
  - leaky half: six swollen, inflamed cells that differ in size, height and tilt (one is shrunken),
    with notched, ragged walls, bitten tops, broken microvilli, cracks and sparks.  The three-bar
    junctions are snapped in half across every gap, jagged ends, some hanging.  Each leak is ONE
    continuous arrow: a stream that floods the gap from its mouth, deepens as it falls, narrows into
    a solid neck across the membrane and flows into a bold arrowhead in the blood, with small flow
    chevrons between the items.  Food particles, microbes and toxins crowd each gap mouth, ride the
    stream down and fan out under the head;
  - medications and stress are drawn as causes of damage (a pill resting on an injured cell, bolts
    striking cell tops), never as things that leak: oral medicines are meant to be absorbed;
  - toxins use the series symbol (svgkit.TOXIN red hexagon, white rim), as on the mold sheet;
  - every object registers its true outline in _SHAPES; a clearance check (2 units between any two
    objects, 1 unit past a damaged wall) found the tangencies the NUDGE table clears;
  - no caption floats on the art; the key names the two regions (top: inside the gut, bottom: the
    blood), every symbol and every nutrient letter.

Back page: NutriDyn's 5R GI Restoration Program (ND584).  The Gut Overgrowth sheet carries Remove's herbs
(the antimicrobials); this back keeps the Remove-step diet as its first checklist box and covers Replace
(Digestive Complete), Repair (GI Integrity, the start pick, and GI Defend), Reinoculate (UltraBiotic Daily
Multi-Strain) and Retain (GI Restore, days 11 to 24).  The plan line under the daily rhythm (rhythm_note)
says days 1 to 10 run the first four products together and GI Restore takes over on days 11 to 24.  Label
facts and sources: build/products.d/intestinal-permeability.json.  Back-page CSS is scoped with
.sheet.back:has(.ipx-back) (a marker span in the lifestyle title).

Condition facts (sources; every citation resolved on PubMed 2026-11-03):
  - One cell layer sealed by tight junctions; NSAIDs, endurance exercise and dietary emulsifiers
    raise permeability: Camilleri M. Gut 2019;68:1516-26 (PMID 31076401).
  - Psychological stress and the stress hormone CRH raise small-intestine permeability in people:
    Vanuytsel T et al. Gut 2014;63:1293-9 (PMID 24153250).  Physical stress does too (4-day
    military ski march): Karl JP et al. Am J Physiol GI Liver Physiol 2017;312:G559-71
    (PMID 28336545).  Hence the Stress tab: "of body or mind".
  - NSAIDs (ibuprofen-type pain pills) damage and inflame the small intestine: Bjarnason I et al.
    Gastroenterology 1993;104:1832-47 (PMID 8500743).  Hence the Medications tab: "like ibuprofen".
  - Alcohol raises gut permeability: Bjarnason I, Peters TJ, Wise RJ. Lancet 1984;1:179-82
    (PMID 6141332).
  - The lining renews itself every 4 to 5 days ("every few days"): van der Flier LG, Clevers H.
    Annu Rev Physiol 2009;71:241-60 (PMID 18808327).
  - Gluten (gliadin) releases zonulin, which opens tight junctions; barrier and autoimmunity:
    Fasano A. Physiol Rev 2011;91:151-75 (PMID 21248165); Mu Q et al. Front Immunol 2017;8:598
    (PMID 28588585).
  - Deliberately NOT claimed on the front: antibiotics and poor sleep as direct causes.  Human
    evidence is thin (metronidazole even prevented NSAID-induced permeability: Davies GR et al.
    Dig Dis Sci 1993;38:417-25, PMID 8444070; sleep data are mostly mouse studies and sleep-apnoea
    associations: Mashaqi S et al. Sleep Med Rev 2023;69:101774, PMID 37028145).  The back page's
    antibiotic advice is about protecting gut flora, which is well supported.
"""
import math
import random
import re

from kit import icon
from svgkit import T, svg, TOXIN

U = "ipx"

# ----------------------------------------------------------------------------- geometry
# The art prints 7.66 in wide, so 1 unit = 0.726 pt (7 pt = 9.6 units, 8 pt = 11 units).
W = 760
FT, FB = 1, 436           # frame top / bottom
TY, TH, PTR = 7, 44, 8    # tab top / height / pointer
LANE_T, LANE_B = TY + 22, 126   # lanes start behind the tabs and end here
R1, R2 = 77, 105          # the two rows of items in each lane
BT = 158                  # tips of the healthy microvilli
CT = 172                  # apical membrane (top of the cell bodies)
CB = 310                  # basal edge: the tissue starts here, so every gap stays an open channel
BLT = 330                 # top of the blood vessel
SPLIT = 304               # healthy | leaky

GREEN = "#23894F"         # absorbed-through-a-cell arrow
TAB_GREEN = "#1B7444"     # Nutrients tab (5.8:1 with white)
LEAK = "#E0412A"          # the leak stream
JUNCTION = "#5E2F22"      # tight-junction stitches
STRESS = "#8150B8"

LANE_X = [6 + i * 150 for i in range(5)]       # lane and tab left edges
LANE_W = 142
# Healthy cell walls.  Cell 0 starts under the frame's left edge (round 3: a 3-unit strip of lumen showed beside it,
# down to the tissue), so the lining reads as running on past the picture; its nucleus keeps the 50-unit cell's place.
HX = [-12] + [4 + i * 50 for i in range(1, 7)]
# The green arrows cross the cytoplasm of cells 0-2 beside the nucleus (recheck 2026-11-03: an arrow down the
# middle sliced every nucleus in half).  Arrow 5 units left of the cell centre, nucleus 11 units right of it
# (all six healthy cells, so they stay uniform): 2.2 units of clear cytoplasm between the arrow's white halo and
# the nucleus, 4.3 between the nucleus and the cell wall.
NUT_X = [4 + i * 50 + 20 for i in range(3)]
NUC_DX = 11
LANE_TOK_X = [29 + i * 100 / 3 for i in range(4)]   # top row of the Nutrients lane
# The three that travel lane -> cell -> blood leave the cell straight into the blood (standard physiology:
# vitamin C via its transporter, iron via ferroportin, zinc via ZnT1, all into the portal blood).  Vitamin D is
# fat-soluble: it is absorbed with dietary fat and leaves the cell in chylomicrons through the lymph, so it stays
# in the lane rather than being drawn going straight into the blood (Silva MC, Furlanetto TW. Nutr Rev
# 2018;76:60-76, PMID 29025082; recheck 2026-11-03).
# Every token colour gives its white letter at least 4.5:1 contrast; none is green, so none blends into an arrow.
TRAVEL = [("C", "#B85A16"), ("Fe", "#6B3A87"), ("Zn", "#264D8C")]
LANE_TOKENS = [("Mg", "#8A5A3C"), ("D", "#2F6DB5"), ("B", "#2E7D4C"), ("Ca", "#187580")]
NUTRIENT_NAMES = [("C", "#B85A16", "vitamin C"), ("Fe", "#6B3A87", "iron"), ("Zn", "#264D8C", "zinc"),
                  ("Mg", "#8A5A3C", "magnesium"), ("D", "#2F6DB5", "vitamin D"), ("B", "#2E7D4C", "B vitamins"),
                  ("Ca", "#187580", "calcium")]

_REG = []   # every placed item as (kind, x, y, half-width, half-height): read by the layout check


def _mix(col, a, bg="#F1F7F8"):
    """Opaque colour = col at alpha a over bg.  Lanes use this instead of fill/stroke-opacity: in the
    Chromium PDF a stroke-opacity on the lanes leaked into the fills drawn after them (tissue, blood)."""
    c = [int(col[i:i + 2], 16) for i in (1, 3, 5)]
    b = [int(bg[i:i + 2], 16) for i in (1, 3, 5)]
    return "#" + "".join(f"{round(b[i] + (c[i] - b[i]) * a):02X}" for i in range(3))


def _reg(kind, x, y, hw, hh):
    _REG.append((kind, x, y, hw, hh))


# Every drawn object also records its real outline (rotated, scaled) as (kind, points, stroke radius), so a
# clearance check can measure true gaps between shapes instead of loose axis-aligned boxes (recheck 2026-11-03:
# the box pass hid tangencies such as a flagellum ending on a food particle).
_SHAPES = []   # (kind, points, stroke radius, closed, group): pieces of one object share a group


def _shape(kind, pts, rad=0.0, closed=True, group=None):
    if group is None:
        group = len(_SHAPES) + 1
    _SHAPES.append((kind, [(float(px), float(py)) for px, py in pts], float(rad), closed, group))
    return group


def _xf(pts, x, y, rot=0.0, s=1.0):
    a = math.radians(rot)
    ca, sa = math.cos(a), math.sin(a)
    return [(x + s * (px * ca - py * sa), y + s * (px * sa + py * ca)) for px, py in pts]


def _bez(p0, p1, p2, p3, n=8):
    return [tuple((1 - t) ** 3 * a + 3 * (1 - t) ** 2 * t * b + 3 * (1 - t) * t * t * c + t ** 3 * d
                  for a, b, c, d in zip(p0, p1, p2, p3)) for t in (i / n for i in range(n + 1))]


def _ell(rx, ry, n=24):
    return [(rx * math.cos(2 * math.pi * i / n), ry * math.sin(2 * math.pi * i / n)) for i in range(n)]


def _rrect(w, h, r, n=6):
    """Outline of a w x h rounded rectangle centred on 0,0."""
    pts = []
    for cx, cy, a0 in ((w / 2 - r, -h / 2 + r, -90), (w / 2 - r, h / 2 - r, 0), (-w / 2 + r, h / 2 - r, 90),
                       (-w / 2 + r, -h / 2 + r, 180)):
        pts += [(cx + r * math.cos(math.radians(a0 + 90 * i / n)), cy + r * math.sin(math.radians(a0 + 90 * i / n)))
                for i in range(n + 1)]
    return pts


# ----------------------------------------------------------------------------- symbols
# Every symbol is drawn centred on (x, y) so the key can reuse it at (0, 0).
def token(x, y, sym, col, r=12.5):
    fs = 12.5 if len(sym) == 1 else 10.4
    if r < 12:
        fs *= r / 12.5 + 0.06
    return (f'<g transform="translate({x:.1f},{y:.1f})"><circle r="{r}" fill="{col}" stroke="#fff" stroke-width="2.2"/>'
            f'<circle r="{r - 1.6:.1f}" fill="url(#{U}-shine)"/>'
            + T(0, fs * 0.36, sym, round(fs, 1), 800, "#fff", "middle") + "</g>")


FOOD = ["M-11,-3 C-12,-11 -2,-14 5,-11 C13,-8 14,1 9,7 C4,12 -6,12 -10,6 C-12,3 -11,0 -11,-3Z",
        "M-12,1 C-13,-6 -6,-11 1,-11 C8,-11 13,-6 12,1 C11,8 5,11 -1,11 C-7,11 -11,7 -12,1Z",
        "M-10,-7 C-4,-12 7,-11 11,-5 C14,1 10,9 3,10 C-2,11 -6,8 -9,9 C-13,9 -14,2 -12,-2 C-12,-4 -11,-6 -10,-7Z"]


def food(x, y, s=1.0, rot=0, v=0):
    return (f'<g transform="translate({x:.1f},{y:.1f}) rotate({rot:.0f}) scale({s})">'
            f'<path d="{FOOD[v % 3]}" fill="url(#{U}-food)" stroke="#6E4A2C" stroke-width="1.3"/>'
            '<path d="M-6,-6.5 C-3,-9 2,-9 5,-7" fill="none" stroke="#F6E2C6" stroke-width="1.8" stroke-linecap="round"/>'
            '<circle cx="-3" cy="2" r="1.5" fill="#86593A"/><circle cx="4" cy="-1" r="1.2" fill="#86593A"/>'
            '<circle cx="1" cy="5.5" r="1.1" fill="#86593A"/></g>')


# local outline points of a microbe (body, hair tips, flagellum), for its rotated extent
_MIC_PTS = [(-15, -6.6), (15, -6.6), (15, 6.6), (-15, 6.6), (-10.3, -10.2), (8.7, -10.2), (-10.3, 10.2),
            (8.7, 10.2), (23.6, -3.6), (32.6, 0), (27.6, 3.6)]


def microbe_extent(rot, s, tail=True):
    a = math.radians(rot)
    pts = _MIC_PTS if tail is True else _MIC_PTS[:8] + ([(23.6, 0), (20, -3.6)] if tail == "short" else [])
    xs = [s * (px * math.cos(a) - py * math.sin(a)) for px, py in pts]
    ys = [s * (px * math.sin(a) + py * math.cos(a)) for px, py in pts]
    return min(xs), max(xs), min(ys), max(ys)


def microbe(x, y, rot=0, s=1.0, tail=True):
    hairs = "".join(f"M{-9 + i * 4.5:.1f},-6.4 l-1.3,-3.8 M{-9 + i * 4.5:.1f},6.4 l-1.3,3.8 " for i in range(5))
    flag = {True: "M14.6,0 c3,-3.6 6,3.6 9,0 s6,3.6 9,0", "short": "M14.6,0 c3,-3.6 6,3.6 9,0"}.get(tail, "")
    return (f'<g transform="translate({x:.1f},{y:.1f}) rotate({rot:.0f}) scale({s})">'
            f'<path d="{hairs}{flag}" fill="none" stroke="#4C7224" stroke-width="1.3" stroke-linecap="round"/>'
            f'<rect x="-15" y="-6.6" width="30" height="13.2" rx="6.6" fill="url(#{U}-mic)" stroke="#4C7224" stroke-width="1.3"/>'
            '<path d="M-10,-3.2 H7" stroke="#EAF6D2" stroke-width="2" stroke-linecap="round"/>'
            '<circle cx="-5" cy="1.9" r="1.7" fill="#4C7224"/><circle cx="3.6" cy="1.3" r="1.5" fill="#4C7224"/></g>')


def toxin(x, y, r=6.0):
    """Toxin: the series' red hexagon (svgkit.TOXIN, the mold sheet's 'red stop sign'), point up,
    with a white rim for contrast on red and a dark hairline so it also holds on the pale lumen."""
    pts = " ".join(f"{x + r * math.cos(math.radians(a)):.2f},{y + r * math.sin(math.radians(a)):.2f}"
                   for a in range(-90, 270, 60))
    return (f'<polygon points="{pts}" fill="none" stroke="#5E1014" stroke-width="3.6" stroke-linejoin="round"/>'
            f'<polygon points="{pts}" fill="url(#{U}-tox)" stroke="#FFFFFF" stroke-width="1.6" stroke-linejoin="round"/>')


def pill(x, y, rot=0, s=1.0):
    return (f'<g transform="translate({x:.1f},{y:.1f}) rotate({rot:.0f}) scale({s})">'
            '<rect x="-14.5" y="-6.8" width="29" height="13.6" rx="6.8" fill="#FFFFFF" stroke="#244F93" stroke-width="1.5"/>'
            '<path d="M0,-6.8 H7.7 A6.8,6.8 0 0 1 7.7,6.8 H0 Z" fill="#2B5DA8"/>'
            '<path d="M-10,-3.1 H-3" stroke="#D3DCE9" stroke-width="2" stroke-linecap="round"/>'
            '<path d="M3,-3.1 H9" stroke="#86A8DC" stroke-width="2" stroke-linecap="round"/></g>')


BOLT_TIP = (-4.6, 15)


def bolt(x, y, s=1.0, rot=0):
    return (f'<g transform="translate({x:.1f},{y:.1f}) rotate({rot:.0f}) scale({s})">'
            f'<path d="M2.5,-15 L-8.5,1.8 L-1.6,1.8 L-4.6,15 L8.8,-3.6 L2.1,-3.6 L6.2,-15 Z" fill="{STRESS}" '
            'stroke="#4B2778" stroke-width="1.2" stroke-linejoin="round"/>'
            '<path d="M3,-11.5 L-4.6,-0.2" stroke="#D2B6F0" stroke-width="1.4" stroke-linecap="round"/></g>')


def spark(x, y, r=7.0):
    pts = []
    for k in range(16):
        a = math.radians(k * 22.5 - 90)
        rr = r if k % 2 == 0 else r * 0.42
        pts.append(f"{x + rr * math.cos(a):.2f},{y + rr * math.sin(a):.2f}")
    return (f'<polygon points="{" ".join(pts)}" fill="#FF8B3D" stroke="#C2321C" stroke-width="1" stroke-linejoin="round"/>'
            f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r * 0.3:.2f}" fill="#FFE27D"/>')


def rbc(x, y, rot=0, s=1.0):
    return (f'<g transform="translate({x:.1f},{y:.1f}) rotate({rot:.0f}) scale({s})">'
            '<ellipse rx="13.5" ry="7.8" fill="#E5484F" stroke="#7E141B" stroke-width="1"/>'
            '<ellipse rx="7" ry="3.3" fill="#B3242C"/>'
            '<path d="M-9.5,-4.6 Q0,-8.2 9.5,-4.6" fill="none" stroke="#F8A8AA" stroke-width="1.4" stroke-linecap="round"/></g>')


def arrow(x, y0, y1, col, w=5.5, head=16.0, halo="#FFFFFF"):
    """Vertical arrow pointing down, with a white halo so it reads on cells and on blood."""
    hw = head * 0.62
    return (f'<path d="M{x:.1f},{y0} V{y1 - head + 1}" stroke="{halo}" stroke-width="{w + 4.2}" stroke-linecap="round"/>'
            f'<path d="M{x - hw - 2.4:.1f},{y1 - head - 1.5:.1f} L{x + hw + 2.4:.1f},{y1 - head - 1.5:.1f} L{x:.1f},{y1 + 3:.1f} Z" '
            f'fill="{halo}" stroke="{halo}" stroke-width="1.6" stroke-linejoin="round"/>'
            f'<path d="M{x:.1f},{y0} V{y1 - head + 1}" stroke="{col}" stroke-width="{w}" stroke-linecap="round"/>'
            f'<path d="M{x - hw:.1f},{y1 - head:.1f} L{x + hw:.1f},{y1 - head:.1f} L{x:.1f},{y1} Z" fill="{col}" '
            f'stroke="{col}" stroke-width="1.2" stroke-linejoin="round"/>')


# ---- the leak: ONE continuous stream per gap.  Art review round 3 (2026-11-03): the old stream flooded each gap
# from wall to wall in the inflamed cells' own salmon, so every gap read as empty, cell-coloured background (1.2:1
# against the cells at the gap floor) and the items as beads on a dotted line.  Now the stream is its own object:
#   - a red ribbon NARROWER than the gap, so a strip of pale gap shows on each side of it (2.5 units at the mouth,
#     more lower down, where it has narrowed as it falls and the swollen cells bulge apart again);
#   - LEAK at .65 at the mouth, solid by mid-gap; a darker edge (EDGE, 1.2 units) down both sides and a light
#     gloss streak down its left side, so it reads as liquid;
#   - unbroken: the ribbon tapers into a neck across the basement membrane and the tissue, and the neck flows into
#     a bold arrowhead in the blood (one outline, one fill, one edge);
#   - no flow chevrons: the items ride the stream at varied offsets and angles, crossing its edges.
# It starts at the gap mouth, below the lanes, so nothing in the Medications or Stress lanes ever looks like it leaks.
VESSEL = [((0, BLT + 5), (150, BLT - 5), (300, BLT + 7), (450, BLT)),
          ((450, BLT), (600, BLT - 7), (650, BLT - 4), (W, BLT + 4))]   # the vessel's top edge (S reflected)
RIB_M0, RIB_M1 = 3.2, 3.6    # ribbon edge to wall: at the mouth, and from 30 units down (2.2+ units of pale show)
RIB_MAX = 26.0               # the widest ribbon: the wide mouths become a funnel no wider than this
NECK_HW = 6.3                # the neck, 12.6 units wide
HEAD_HW, HEAD_H = 13.5, 26.0
DEEP = "#C9311D"             # the stream deepens to this by mid-gap (2:1 or more against the inflamed cells)
EDGE = "#A8281A"             # the stream's darker edge
GLOSS = "#FFC0AE"            # the light streak down its left side
GAP_TOP, GAP_BOT = "#F3F8F9", "#F9EAE4"   # the open gap behind the stream: lumen-pale at the mouth, tissue-pale below


def vessel_y(x):
    """y of the vessel's top edge at x."""
    pts = [p for seg in VESSEL for p in _bez(*seg, n=40)]
    for (x0, y0), (x1, y1) in zip(pts, pts[1:]):
        if x0 <= x <= x1:
            return y0 + (y1 - y0) * (x - x0) / max(1e-6, x1 - x0)
    return BLT


def _smooth(v, r):
    return [sum(v[max(0, i - r):i + r + 1]) / len(v[max(0, i - r):i + r + 1]) for i in range(len(v))]


def _inner(wall, y, side):
    """The wall's innermost x within 3 units of y: the torn notches only ever widen a gap, so the ribbon ignores them."""
    xs = [x_on(wall, y + d) for d in (-3, -1.5, 0, 1.5, 3)]
    return max(xs) if side < 0 else min(xs)


def ribbon(wl, wr, ybot):
    """The stream's two edges down one gap, sampled every 2 units from the mouth to the gap floor: (ys, lefts, rights).
    The ribbon keeps RIB_M0..RIB_M1 of pale gap on each side, narrows as it falls (it never widens again), and its
    edges are smoothed so it reads as poured liquid, not as a copy of the ragged walls."""
    y0 = ybot - 1.0
    n = int(round((CB - y0) / 2)) + 1
    ys = [y0 + i * (CB - y0) / (n - 1) for i in range(n)]
    al = [_inner(wl, y, -1) for y in ys]
    ar = [_inner(wr, y, 1) for y in ys]
    marg = [RIB_M0 + (RIB_M1 - RIB_M0) * min(1.0, (y - y0) / 30) for y in ys]
    cen, wid, run = [], [], RIB_MAX
    for a, b, m in zip(al, ar, marg):
        run = min(run, b - a - 2 * m)
        cen.append((a + b) / 2)
        wid.append(run)
    cen, wid = _smooth(cen, 6), _smooth(wid, 3)
    lefts = [max(c - w / 2, a + m) for c, w, a, m in zip(cen, wid, al, marg)]
    rights = [min(c + w / 2, b - m) for c, w, b, m in zip(cen, wid, ar, marg)]
    return ys, lefts, rights


def _lerp_at(ys, vs, y):
    for (ya, va), (yb, vb) in zip(zip(ys, vs), zip(ys[1:], vs[1:])):
        if ya <= y <= yb:
            return va + (vb - va) * (y - ya) / max(1e-6, yb - ya)
    return vs[0] if y < ys[0] else vs[-1]


def leak_stream(wl, wr, ybot, gid):
    """One gap's open channel (pale, wall to wall, its edges tucked under the cells drawn later) and the stream in it:
    ribbon, neck and arrowhead as ONE outline.  Returns (markup, ribbon edges as (ys, lefts, rights), neck x, y of the
    head's base)."""
    ys, lefts, rights = ribbon(wl, wr, ybot)
    y0 = ys[0]
    gx = (x_on(wl, CB - 3) + x_on(wr, CB - 3)) / 2                 # the neck leaves from the middle of the gap floor
    hy0 = vessel_y(gx) + 0.5                                       # the head's base sits on the vessel's top edge
    # the ribbon flows into the neck between 20 units above the gap floor and 8 below it (smoothstep, no pinch)
    t0, t1 = CB - 20, CB + 8
    lt, rt = _lerp_at(ys, lefts, t0), _lerp_at(ys, rights, t0)
    left = [(l, y) for y, l in zip(ys, lefts) if y < t0]
    right = [(r, y) for y, r in zip(ys, rights) if y < t0]
    for i in range(15):
        f = i / 14
        s = f * f * (3 - 2 * f)
        y = t0 + (t1 - t0) * f
        left.append((lt + (gx - NECK_HW - lt) * s, y))
        right.append((rt + (gx + NECK_HW - rt) * s, y))
    left.append((gx - NECK_HW, hy0))
    right.append((gx + NECK_HW, hy0))
    tip = (gx, hy0 + HEAD_H)
    head_l, head_r = (gx - HEAD_HW, hy0), (gx + HEAD_HW, hy0)
    outline = left + [head_l, tip, head_r] + right[::-1]

    def pts(p):
        return " L".join(f"{x:.2f},{y:.2f}" for x, y in p)
    # the open gap, wall to wall (tucked 1.5 units under the cells, which are drawn on top), then the stream
    gy = [y0 - 1 + i * (CB + 2 - y0) / 24 for i in range(25)]
    chan = [(x_on(wl, y) - 1.5, y) for y in gy] + [(x_on(wr, y) + 1.5, y) for y in gy[::-1]]
    span = tip[1] - y0

    def off(y):
        return f"{min(1.0, max(0.0, (y - y0) / span)):.3f}"
    mid = (y0 + CB) / 2
    # both fade in over their first 8 units, so neither has a flat lid at the mouth
    defs = (f'<defs><linearGradient id="{gid}c" gradientUnits="userSpaceOnUse" x1="0" y1="{y0 - 1:.1f}" x2="0" y2="{CB:.1f}">'
            f'<stop offset="0" stop-color="{GAP_TOP}" stop-opacity="0"/>'
            f'<stop offset="{9 / (CB - y0 + 1):.3f}" stop-color="{GAP_TOP}"/><stop offset="1" stop-color="{GAP_BOT}"/></linearGradient>'
            f'<linearGradient id="{gid}" gradientUnits="userSpaceOnUse" x1="0" y1="{y0:.1f}" x2="0" y2="{tip[1]:.1f}">'
            f'<stop offset="0" stop-color="{LEAK}" stop-opacity="0"/>'
            f'<stop offset="{off(y0 + 8)}" stop-color="{LEAK}" stop-opacity=".65"/>'
            f'<stop offset="{off(y0 + 26)}" stop-color="{LEAK}"/>'
            f'<stop offset="{off(mid)}" stop-color="{DEEP}"/>'
            f'<stop offset="1" stop-color="{DEEP}"/></linearGradient>'
            f'<linearGradient id="{gid}e" gradientUnits="userSpaceOnUse" x1="0" y1="{y0:.1f}" x2="0" y2="{y0 + 12:.1f}">'
            f'<stop offset="0" stop-color="{EDGE}" stop-opacity="0"/><stop offset="1" stop-color="{EDGE}"/></linearGradient>'
            '</defs>')
    # the gloss streak: down the left third of the ribbon and the neck, in two runs, stopping short of the head
    gl = [(l + (r - l) * 0.27, y) for (l, y), (r, _) in zip(left[:-1], right[:-1]) if y0 + 6 <= y <= hy0 - 3]
    cut = int(len(gl) * 0.55)
    gloss = "".join(f'<path d="M{pts(run)}" fill="none" stroke="{GLOSS}" stroke-width="{w}" stroke-linecap="round" '
                    'stroke-linejoin="round" stroke-opacity=".9"/>' for run, w in ((gl[:cut], 1.7), (gl[cut + 3:], 1.4)) if len(run) > 1)
    hx0, hx1 = gx - HEAD_HW * 0.62, gx - HEAD_HW * 0.2                       # a short gloss on the head's left flank
    gloss += (f'<path d="M{hx0:.2f},{hy0 + 3.2:.2f} L{hx1 + 1.2:.2f},{hy0 + HEAD_H * 0.62:.2f}" stroke="{GLOSS}" '
              'stroke-width="1.3" stroke-linecap="round" stroke-opacity=".8"/>')
    halo = (f'<path d="M{gx - HEAD_HW - 2.6:.2f},{hy0 + 1.2:.2f} L{gx + HEAD_HW + 2.6:.2f},{hy0 + 1.2:.2f} '
            f'L{gx:.2f},{tip[1] + 3.4:.2f} Z" fill="#FFFFFF" stroke="#FFFFFF" stroke-width="1" stroke-linejoin="round"/>')
    edge = "".join(f'<path d="M{pts(side + [tip])}" fill="none" stroke="url(#{gid}e)" stroke-width="1.2" '
                   'stroke-linejoin="round" stroke-linecap="round"/>' for side in (left + [head_l], right + [head_r]))
    _shape("stream", outline, 0)
    _shape("head", [(gx - HEAD_HW - 2.6, hy0 + 1.2), (gx + HEAD_HW + 2.6, hy0 + 1.2), (gx, tip[1] + 3.4)], 0)
    markup = (defs + f'<path d="M{pts(chan)} Z" fill="url(#{gid}c)"/>' + halo
              + f'<path d="M{pts(outline)} Z" fill="url(#{gid})"/>' + gloss + edge)
    return markup, (ys, lefts, rights), gx, hy0


def stitches(x, y, n=3, gap=6.0, half=4.8, col=JUNCTION, sw=2.5):
    return "".join(f'<path d="M{x - half:.1f},{y + j * gap:.1f} H{x + half:.1f}" stroke="{col}" stroke-width="{sw}" '
                   'stroke-linecap="round"/>' for j in range(n))


def stub(x, y, ln, direction, hang=0.0, reg=False):
    """Half of a snapped tight-junction bar: it sticks out of a cell wall and ends in a jagged break.
    direction +1 points right (out of a gap's left wall), -1 points left; hang tips it down (deg)."""
    pts = [(-1.4, -1.25), (ln - 1.0, -1.25), (ln + 0.8, -0.45), (ln - 0.5, 0.15), (ln + 0.6, 0.75), (ln - 0.8, 1.25),
           (-1.4, 1.25)]
    a = math.radians(hang)
    out = []
    for px, py in pts:
        rx, ry = px * math.cos(a) - py * math.sin(a), px * math.sin(a) + py * math.cos(a)
        out.append(f"{x + direction * rx:.2f},{y + ry:.2f}")
    if reg:
        _shape("stub", [tuple(map(float, p.split(","))) for p in out], 0.25)
    return f'<polygon points="{" ".join(out)}" fill="{JUNCTION}" stroke="{JUNCTION}" stroke-width=".5" stroke-linejoin="round"/>'


# ----------------------------------------------------------------------------- true outlines for the clearance check
def _path_pts(d):
    """Sample an absolute 'M x,y C x,y x,y x,y ... Z' outline (the food shapes) into points."""
    xy = [tuple(map(float, p.split(","))) for p in re.findall(r"-?[\d.]+,-?[\d.]+", d)]
    pts = [xy[0]]
    for j in range(1, len(xy) - 2, 3):
        pts += _bez(pts[-1], xy[j], xy[j + 1], xy[j + 2])[1:]
    return pts


_FOOD_PTS = [_path_pts(d) for d in FOOD]
_BOLT_PTS = [(2.5, -15), (-8.5, 1.8), (-1.6, 1.8), (-4.6, 15), (8.8, -3.6), (2.1, -3.6), (6.2, -15)]


def _reg_food(kind, x, y, s, rot, v):
    _shape(kind, _xf(_FOOD_PTS[v % 3], x, y, rot, s), 0.65 * s)


def _reg_mic(kind, x, y, rot, s, tail=True):
    g = _shape(kind, _xf(_rrect(30, 13.2, 6.6), x, y, rot, s), 0.65 * s)
    for i in range(5):
        for sg in (-1, 1):
            _shape(kind, _xf([(-9 + 4.5 * i, sg * 6.4), (-10.3 + 4.5 * i, sg * 10.2)], x, y, rot, s), 0.65 * s, False, g)
    if tail:
        t = _bez((14.6, 0), (17.6, -3.6), (20.6, 3.6), (23.6, 0))
        if tail is True:
            t += _bez((23.6, 0), (26.6, -3.6), (29.6, 3.6), (32.6, 0))[1:]
        _shape(kind, _xf(t, x, y, rot, s), 0.65 * s, False, g)


def _reg_tox(kind, x, y, r):
    _shape(kind, [(x + r * math.cos(math.radians(a)), y + r * math.sin(math.radians(a))) for a in range(-90, 270, 60)], 1.8)


def _reg_pill(kind, x, y, rot, s):
    _shape(kind, _xf(_rrect(29, 13.6, 6.8), x, y, rot, s), 0.75 * s)


def _reg_bolt(kind, x, y, s, rot):
    _shape(kind, _xf(_BOLT_PTS, x, y, rot, s), 0.6 * s)


def _reg_rbc(x, y, rot, s=1.0):
    _shape("rbc", _xf(_ell(13.5, 7.8), x, y, rot, s), 0.5 * s)


def _reg_tok(kind, x, y, r):
    _shape(kind, [(x + px, y + py) for px, py in _ell(r, r)], 1.1)


# ----------------------------------------------------------------------------- defs
def defs_svg():
    return (
        "<defs>"
        f'<clipPath id="{U}-clip"><rect x="1" y="{FT}" width="{W - 2}" height="{FB - FT}" rx="14"/></clipPath>'
        f'<linearGradient id="{U}-lumen" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#F6FAFB"/>'
        '<stop offset="1" stop-color="#E4F0F3"/></linearGradient>'
        f'<linearGradient id="{U}-tissue" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#F6DFD6"/>'
        '<stop offset="1" stop-color="#EFCBBF"/></linearGradient>'
        f'<linearGradient id="{U}-blood" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#B2323A"/>'
        '<stop offset=".55" stop-color="#94222A"/><stop offset="1" stop-color="#6E141B"/></linearGradient>'
        f'<linearGradient id="{U}-hc" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#EDB8A1"/>'
        '<stop offset=".22" stop-color="#F8D6C6"/><stop offset=".55" stop-color="#FCE3D7"/>'
        '<stop offset=".85" stop-color="#F5CAB7"/><stop offset="1" stop-color="#EAB099"/></linearGradient>'
        f'<linearGradient id="{U}-hcv" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FFFFFF" stop-opacity=".35"/>'
        '<stop offset=".25" stop-color="#FFFFFF" stop-opacity="0"/><stop offset=".85" stop-color="#C98A75" stop-opacity="0"/>'
        '<stop offset="1" stop-color="#C98A75" stop-opacity=".22"/></linearGradient>'
        f'<linearGradient id="{U}-lc" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#D88072"/>'
        '<stop offset=".28" stop-color="#EEAA9A"/><stop offset=".6" stop-color="#F4BEAF"/>'
        '<stop offset="1" stop-color="#D57B6A"/></linearGradient>'
        f'<linearGradient id="{U}-lcs" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#CB6E60"/>'
        '<stop offset=".3" stop-color="#E09686"/><stop offset=".62" stop-color="#E8A595"/>'
        '<stop offset="1" stop-color="#C96556"/></linearGradient>'
        f'<linearGradient id="{U}-lcv" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#B8261A" stop-opacity=".22"/>'
        '<stop offset=".3" stop-color="#B8261A" stop-opacity="0"/><stop offset=".85" stop-color="#7A1D14" stop-opacity="0"/>'
        '<stop offset="1" stop-color="#7A1D14" stop-opacity=".22"/></linearGradient>'
        f'<linearGradient id="{U}-mv" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#F9DDD0"/>'
        '<stop offset="1" stop-color="#EDB29B"/></linearGradient>'
        f'<radialGradient id="{U}-hn" cx=".38" cy=".32" r=".75"><stop offset="0" stop-color="#F3ABA2"/>'
        '<stop offset=".6" stop-color="#DE8077"/><stop offset="1" stop-color="#C86A62"/></radialGradient>'
        f'<radialGradient id="{U}-ln" cx=".38" cy=".32" r=".75"><stop offset="0" stop-color="#D45A50"/>'
        '<stop offset="1" stop-color="#9C2F29"/></radialGradient>'
        f'<radialGradient id="{U}-glow" cx=".5" cy=".5" r=".5"><stop offset="0" stop-color="#FF5A36" stop-opacity=".42"/>'
        '<stop offset=".7" stop-color="#FF6A3D" stop-opacity=".15"/><stop offset="1" stop-color="#FF6A3D" stop-opacity="0"/></radialGradient>'
        f'<radialGradient id="{U}-shine" cx=".35" cy=".28" r=".7"><stop offset="0" stop-color="#FFFFFF" stop-opacity=".5"/>'
        '<stop offset=".6" stop-color="#FFFFFF" stop-opacity="0"/></radialGradient>'
        f'<radialGradient id="{U}-food" cx=".38" cy=".3" r=".8"><stop offset="0" stop-color="#DDB68A"/>'
        '<stop offset="1" stop-color="#A97849"/></radialGradient>'
        f'<radialGradient id="{U}-tox" cx=".36" cy=".3" r=".8"><stop offset="0" stop-color="#E8656B"/>'
        f'<stop offset=".55" stop-color="{TOXIN}"/><stop offset="1" stop-color="#A4232A"/></radialGradient>'
        f'<linearGradient id="{U}-mic" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#C2DE8E"/>'
        '<stop offset="1" stop-color="#86B24C"/></linearGradient>'
        f'<linearGradient id="{U}-klk" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{LEAK}" stop-opacity=".65"/>'
        f'<stop offset=".3" stop-color="{LEAK}"/><stop offset=".62" stop-color="{DEEP}"/></linearGradient>'
        "</defs>")


# ----------------------------------------------------------------------------- cells
def _cr(pts, step=2.4):
    """Sample a Catmull-Rom spline through pts.  Returns [(x, y, segment index)]."""
    out = []
    n = len(pts)
    for i in range(n - 1):
        p0 = pts[i - 1] if i else pts[i]
        p1, p2 = pts[i], pts[i + 1]
        p3 = pts[i + 2] if i + 2 < n else p2
        k = max(2, int(math.hypot(p2[0] - p1[0], p2[1] - p1[1]) / step))
        for j in range(k):
            t = j / k
            t2, t3 = t * t, t * t * t
            xy = [0.5 * (2 * b + (-a + c) * t + (2 * a - 5 * b + 4 * c - d) * t2 + (-a + 3 * b - 3 * c + d) * t3)
                  for a, b, c, d in zip(p0, p1, p2, p3)]
            out.append((xy[0], xy[1], i))
    out.append((pts[-1][0], pts[-1][1], n - 2))
    return out


def x_on(wall, y):
    """x of a wall polyline (monotonic in y) at height y; clamps beyond its ends."""
    for (x0, y0), (x1, y1) in zip(wall, wall[1:]):
        if min(y0, y1) <= y <= max(y0, y1) and y1 != y0:
            return x0 + (x1 - x0) * (y - y0) / (y1 - y0)
    return wall[0][0] if abs(y - wall[0][1]) < abs(y - wall[-1][1]) else wall[-1][0]


def h_villi(x0, x1, rnd):
    """Brush border: dense, even, round-tipped microvilli (drawn before the body hides their bases)."""
    pitch, fw = 4.25, 3.0
    n = int((x1 - x0 - 10) / pitch)
    start = (x0 + x1) / 2 - (n - 1) * pitch / 2
    fingers = "".join(f'<rect x="{start + k * pitch - fw / 2:.2f}" y="{BT + rnd.uniform(-0.6, 0.9):.2f}" width="{fw}" '
                      f'height="{CT - BT + 6}" rx="{fw / 2:.2f}"/>' for k in range(n))
    return f'<g fill="url(#{U}-mv)" stroke="#C98670" stroke-width=".65">{fingers}</g>'


def h_cell(x0, x1, mid=None):
    """A healthy columnar cell; the nucleus sits low (basal) and a little to the right, the same in every
    cell, so the absorbed-nutrient arrow crosses clear cytoplasm beside it.  `mid` overrides the cell's centre for
    the nucleus (cell 0 runs on under the frame)."""
    r = 8
    d = f"M{x0},{CB} V{CT + r} Q{x0},{CT} {x0 + r},{CT} H{x1 - r} Q{x1},{CT} {x1},{CT + r} V{CB} Z"
    cx, cy = (mid if mid is not None else (x0 + x1) / 2) + NUC_DX, CT + (CB - CT) * 0.74
    _shape("cell", [(x0, CB), (x0, CT), (x1, CT), (x1, CB)], 0.6)
    _shape("nucleus", [(cx + 8.6 * math.cos(a * math.pi / 12), cy + 14.5 * math.sin(a * math.pi / 12)) for a in range(24)], 0.45)
    return (f'<path d="{d}" fill="url(#{U}-hc)" stroke="#D2937E" stroke-width="1.2"/>'
            f'<path d="{d}" fill="url(#{U}-hcv)"/>'
            f'<ellipse cx="{cx:.1f}" cy="{cy:.1f}" rx="8.6" ry="14.5" fill="url(#{U}-hn)" stroke="#B35E57" stroke-width=".9"/>'
            f'<circle cx="{cx + 2:.1f}" cy="{cy - 4:.1f}" r="2.5" fill="#9C423C"/>')


# The six damaged cells.  hw = half-widths at 7, 25, 52, 78 and 100 % of the cell's height;
# top = how far the eroded top sits below CT; tilt in degrees (the base stays put);
# notches = (side, fraction of height, depth, half-height) tears in the walls.
LCELLS = [
    dict(xc=331, hw=(19, 25, 27, 26, 25), top=4, tilt=0.0, bites=(0.62,), crack=-6, spark=(12, 24, 7.0), nuc=(-1, 2, 11.5, 15.5),
         lean=True, notches=[("R", .30, 3.2, 3.0), ("R", .52, 2.6, 2.6), ("R", .74, 3.8, 3.2), ("R", .9, 2.8, 2.4)]),
    dict(xc=411, hw=(18, 24, 28, 27, 25), top=7, tilt=-2.0, bites=(0.3,), crack=8, spark=(-9, 31, 6.0), nuc=(2, -3, 11, 15),
         notches=[("L", .34, 3.6, 3.0), ("L", .6, 2.6, 2.5), ("L", .82, 3.2, 3.0), ("R", .28, 2.8, 2.6), ("R", .47, 3.8, 3.4),
                  ("R", .69, 2.6, 2.4), ("R", .88, 3.0, 2.8)]),
    dict(xc=491, hw=(13, 18, 21, 20, 19), top=22, tilt=3.0, bites=(0.45,), crack=4, spark=(-5, 22, 5.0), nuc=(1, 6, 9.5, 12.5),
         shrunken=True,
         notches=[("L", .38, 3.0, 2.6), ("L", .7, 3.8, 3.2), ("L", .9, 2.6, 2.2), ("R", .32, 3.4, 3.0), ("R", .58, 2.6, 2.4),
                  ("R", .8, 3.6, 3.0)]),
    dict(xc=571, hw=(20, 26, 29, 27, 26), top=3, tilt=-1.0, bites=(), crack=-10, spark=(12, 27, 7.5), nuc=(-3, 0, 12, 16),
         notches=[("L", .27, 2.8, 2.6), ("L", .5, 3.8, 3.4), ("L", .66, 2.5, 2.2), ("L", .86, 3.2, 2.8), ("R", .36, 3.0, 2.8),
                  ("R", .62, 3.8, 3.2), ("R", .84, 2.6, 2.4)]),
    dict(xc=651, hw=(17, 23, 26, 25, 24), top=9, tilt=2.0, bites=(0.7,), crack=-1, spark=(-11, 31, 6.5), nuc=(3, -2, 10.5, 15),
         notches=[("L", .3, 3.4, 3.0), ("L", .55, 2.6, 2.4), ("L", .8, 3.8, 3.2), ("R", .26, 2.6, 2.4), ("R", .45, 3.2, 3.0),
                  ("R", .68, 3.8, 3.2), ("R", .9, 2.8, 2.4)]),
    # the last cell runs on under the frame's right edge (hwr: its right half-widths; round 3: a 6-unit strip of lumen
    # beside it read as a sixth, empty gap)
    dict(xc=729, hw=(18, 23, 25, 25, 24), hwr=(45, 47, 49, 49, 48), top=5, tilt=-1.5, bites=(0.25, 0.75), crack=1,
         spark=(11, 25, 7.0), nuc=(-2, 4, 11, 15.5),
         notches=[("L", .33, 3.6, 3.2), ("L", .58, 2.6, 2.4), ("L", .78, 3.2, 2.8), ("R", .3, 3.2, 2.8), ("R", .48, 2.8, 2.6),
                  ("R", .7, 3.4, 3.0), ("R", .88, 2.6, 2.2)]),
]


def l_cell(c, rnd):
    """A swollen, inflamed, damaged cell.  Returns (svg, left wall, right wall, top y), the walls as
    (x, y) polylines from top to bottom after the tears and the tilt are applied."""
    xc, hw, top = c["xc"], c["hw"], CT + c["top"]
    h = CB - top
    ys = [top + h * f for f in (0.07, 0.25, 0.52, 0.78, 1.0)]
    left = [(xc - hw[k] + (rnd.uniform(-1.2, 1.2) if 0 < k < 4 else 0), ys[k]) for k in range(5)]
    hwr = c.get("hwr", hw)
    right = [(xc + hwr[k] + (rnd.uniform(-1.2, 1.2) if 0 < k < 4 else 0), ys[k]) for k in range(5)]
    if c.get("lean"):                      # the first leaky cell still leans on the healthy side
        left = [(SPLIT + d, ys[k]) for k, d in enumerate((5, 1.5, 1, 1, 1))]
    xl, xr = left[0][0], right[0][0]
    m = 8
    tops = []
    for k in range(m + 1):
        f = k / m
        y = top + 1.5 + rnd.uniform(-1.0, 2.6) - (3.5 * math.sin(math.pi * f) if c.get("shrunken") else 0)
        for b in c["bites"]:
            if abs(f - b) < 0.07:
                y += 4.5
        tops.append((xl + 5 + (xr - xl - 10) * f, y))
    chain = left[::-1] + tops + right
    sm = _cr(chain)
    wall_l = [(x, y) for x, y, s in sm if s <= 3]          # bottom -> top
    head = [(x, y) for x, y, s in sm if 4 <= s <= 13]
    wall_r = [(x, y) for x, y, s in sm if s >= 14]         # top -> bottom

    def tear(wall, side):
        inward = 1 if side == "L" else -1
        pts = list(wall)
        for sd, f, depth, hh in c["notches"]:
            if sd != side:
                continue
            yc = top + h * f
            v = [(x_on(wall, yc - hh), yc - hh), (x_on(wall, yc) + inward * depth, yc), (x_on(wall, yc + hh), yc + hh)]
            pts = [p for p in pts if abs(p[1] - yc) > hh] + v
        return sorted(pts, key=lambda p: p[1], reverse=(side == "L"))

    wall_l, wall_r = tear(wall_l, "L"), tear(wall_r, "R")
    k = math.tan(math.radians(c["tilt"]))

    def sh(x, y):                       # tilt: shear about the base
        return x + (CB - y) * k, y

    outline = [sh(x, y) for x, y in wall_l + head + wall_r]
    _shape("lcell", outline, 0.7)
    d = "M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in outline) + " Z"
    vil = []
    for i, (x, y) in enumerate(tops[1:-1]):
        for dx in (-2.4, 2.4):
            hgt = rnd.choice([0, 0, 2, 3, 0, 4] if c.get("shrunken") else [0, 0, 3, 4, 6, 8])
            if hgt:
                bx, by = sh(x + dx, y)
                rot = rnd.uniform(-26, 26)
                vil.append(f'<rect x="{bx - 1.5:.1f}" y="{by - hgt:.1f}" width="3" height="{hgt + 6}" rx="1.5" '
                           f'transform="rotate({rot:.0f} {bx:.1f} {by + 2:.1f})"/>')
    ndx, ndy, nrx, nry = c["nuc"]
    ncx, ncy = sh(xc + ndx, CT + (CB - CT) * 0.66 + 3 + ndy)
    nrot = rnd.uniform(-14, 14)
    ccx, ccy = sh(xc + c["crack"], top + 3)
    zig = [(2.6, 5.5), (-3.2, 4.5), (3.6, 5.5), (-2.2, 4.5)] if not c.get("shrunken") else [(2.2, 4.5), (-2.8, 4.0), (2.6, 4.5)]
    crack = f"M{ccx:.1f},{ccy:.1f} " + " ".join(f"l{a * rnd.uniform(.85, 1.2):.1f},{b * rnd.uniform(.9, 1.15):.1f}" for a, b in zig)
    sx, sy = sh(xc + c["spark"][0], top + c["spark"][1])
    fill = f"{U}-lcs" if c.get("shrunken") else f"{U}-lc"
    body = (f'<g fill="#E7A798" stroke="#B95A4C" stroke-width=".6">{"".join(vil)}</g>'
            f'<path d="{d}" fill="url(#{fill})" stroke="#AE3D31" stroke-width="1.4" stroke-linejoin="round"/>'
            f'<path d="{d}" fill="url(#{U}-lcv)"/>'
            f'<ellipse cx="{ncx:.1f}" cy="{ncy:.1f}" rx="{nrx}" ry="{nry}" transform="rotate({nrot:.0f} {ncx:.1f} {ncy:.1f})" '
            f'fill="url(#{U}-ln)" stroke="#7E231E" stroke-width=".9"/>'
            f'<circle cx="{ncx + 2:.1f}" cy="{ncy - 4:.1f}" r="{nrx * 0.26:.1f}" fill="#6E1C17"/>'
            f'<path d="{crack}" fill="none" stroke="#7A2219" stroke-width="1.3" stroke-linecap="round" stroke-linejoin="round"/>'
            + spark(sx, sy, c["spark"][2]))
    wl = [sh(x, y) for x, y in wall_l][::-1]            # top -> bottom
    wr = [sh(x, y) for x, y in wall_r]
    top_y = sum(y for _, y in tops) / len(tops)
    return body, wl, wr, top_y


# ----------------------------------------------------------------------------- the art
# The two causes say what they do and wear their own colour (round 3: in the "should stay out" teal, with "like
# ibuprofen" / "of body or mind" under them, a child could read them as two more things that leak in).  NSAIDs and
# stress loosen the seams: Bjarnason 1993, Vanuytsel 2014, Karl 2017 (module docstring).  "Some can": NSAIDs do,
# most medicines do not, and a patient must never read the tab as a reason to stop an essential medicine (the intro
# says "some medications", the key "like ibuprofen").
TABS = [("Nutrients", "should pass"), ("Food particles", "should stay out"), ("Microbes", "should stay out"),
        ("Medications", "some can loosen seams"), ("Stress", "can loosen seams")]
CAUSE = "#5B4A8E"         # the two cause tabs (7.4:1 with white)

# What pours through each gap, from the crowd at the mouth down to the fan in the blood:
# 4 crowding above the mouth, 2 squeezing into it, 2 further down, 1 crossing the membrane,
# then 2 or 3 fanning out under the arrowhead.  Five gaps, five different mixes.
F, M, X = "food", "mic", "tox"
STREAM = [[M, X, F, M, X, M, M, X, F, M, X, F],
          [F, M, X, F, M, F, F, X, M, F, M],
          [X, F, M, M, F, X, M, F, X, F, X, M],
          [F, M, X, F, M, X, X, F, M, M, F],
          [M, F, X, F, M, X, F, M, X, X, F, M]]
CROWD = [(-15, -26), (12, -28), (-2, -13), (19, -8)]   # (dx, dy) above the higher cell top; mirrored on odd gaps
RBCS = [(176, 352, 10), (236, 366, -12), (300, 350, 8), (196, 404, -8), (262, 414, 14), (326, 398, -10),
        (411, 352, 6), (491, 354, -8), (571, 350, 10), (651, 352, -6), (730, 352, 8),
        (411, 421, 12), (491, 417, -6), (568, 421, 10), (648, 418, -12), (732, 416, 8), (176, 425, -4)]


def _ext(kind, s=1.0, rot=0.0, r=6.0):
    """(half-width, half-height) of an item, for spacing and gap checks."""
    if kind == M:
        x0, x1, y0, y1 = microbe_extent(rot, s)
        return (x1 - x0) / 2, (y1 - y0) / 2
    if kind == X:
        return r + 1.8, r + 1.8
    return 13 * s, 13 * s


# Hand nudges for single stream items, keyed by tag (g<gap> + c crowd / m mouth / d down the gap / b membrane /
# f fan in the blood + index): (dx, dy, extra rotation[, absolute rotation[, scale]]).  They clear the
# tangencies the true-outline clearance check found (2 units between any two objects, 1 unit past a cell wall).
NUDGE = {
    "g0c1": (-1, -3, 0),
    "g0c3": (-2, 0, 0),             # off cell 1's top corner
    "g0m1": (0, 4, 0),              # its tail kissed the toxin above it
    "g1m1": (0, 2, 0),
    "g2c1": (0, -5, 0),
    "g2c2": (-2, 0, 0),
    "g2c3": (-5, -2, 0),            # it sat on cell 3's top corner
    "g2m1": (2, 0, 0),              # its white rim touched a snapped junction tip
    "g3c1": (-2, -3, 0),
    "g3b": (0, -1, 0),
    "g4c0": (-4, -4, 0),            # gap 4's crowd was a three-way pile-up
    "g4c1": (0, -6, 0),
    "g4c2": (-3, 0, 0),
    "g4c3": (-2, -9, 0),
    "g4m0": (-1, 0, 0, 270, 0.57),  # nose straight down, a little smaller, to squeeze between the snapped bars
    "g4m1": (2, 2.5, 0),
    "g4f2": (0, 0, 180),            # its tail ended on a food particle: turn it around
    "g0f0": (-3, 3, 0),             # round 3: the bigger arrowhead's halo touched its tail
}


def _place(kind, x, y, rnd, rot=None, s=None, narrow=False, tail=True, tag="", v=None, r=None):
    """Draw one stream item and register it; microbes in a narrow gap swim nose-down."""
    if kind == M:
        s = s or 0.62
        rot = rot if rot is not None else (rnd.uniform(250, 290) if narrow else rnd.uniform(-60, 240))
    elif kind == F:
        s = s or (0.6 if narrow else 0.66)
        rot = rot if rot is not None else rnd.uniform(-40, 40)
        v = rnd.randrange(3) if v is None else v
    dx, dy, dr, *fix = NUDGE.get(tag, (0, 0, 0))
    x, y = x + dx, y + dy
    if fix and fix[0] is not None:
        rot = fix[0]
    if len(fix) > 1:
        s = fix[1]
    if kind == M:
        rot += dr
        x0, x1, y0, y1 = microbe_extent(rot, s, tail)
        _reg(M, x + (x0 + x1) / 2, y + (y0 + y1) / 2, (x1 - x0) / 2, (y1 - y0) / 2)
        _reg_mic(f"{M}:{tag}", x, y, rot, s, tail)
        return microbe(x, y, rot, s, tail)
    if kind == X:
        r = r or (5.8 if narrow else 6.2)
        _reg(X, x, y, r + 1.8, r + 1.8)
        _reg_tox(f"{X}:{tag}", x, y, r)
        return toxin(x, y, r)
    rot += dr
    _reg(F, x, y, 13 * s, 13 * s)
    _reg_food(f"{F}:{tag}", x, y, s, rot, v)
    return food(x, y, s, rot, v)


def _in_gap(kind, wl, wr, y, inset, side, rnd, tag=""):
    """Place an item in a gap at height y, inside the walls less `inset`, nudged to one side."""
    lo, hi = x_on(wl, y) + inset, x_on(wr, y) - inset
    rot = rnd.uniform(250, 290) if kind == M else None
    ew = (microbe_extent(rot, 0.62, "short")[1] - microbe_extent(rot, 0.62, "short")[0]) / 2 if kind == M else \
        (_ext(X, r=5.8)[0] if kind == X else _ext(F, 0.6)[0])
    slack = max(0.0, (hi - lo) / 2 - ew)
    return _place(kind, (lo + hi) / 2 + side * min(slack, rnd.uniform(1.5, 4.0)), y, rnd, rot=rot, narrow=True,
                  tail="short", tag=tag)


def _outline(kind, rot, s, v=0, r=6.0):
    """An item's outline points around (0, 0) and its stroke radius, for placing it against the walls."""
    if kind == M:
        body = _xf(_rrect(30, 13.2, 6.6), 0, 0, rot, s)
        return body + _xf(_MIC_PTS[4:8] + [(23.6, 0), (20, -3.6)], 0, 0, rot, s), 0.65 * s
    if kind == F:
        return _xf(_FOOD_PTS[v % 3], 0, 0, rot, s), 0.65 * s
    return [(r * math.cos(math.radians(a)), r * math.sin(math.radians(a))) for a in range(-90, 270, 60)], 1.8


def _ride(kind, side_l, side_r, rib, y, side, rnd, tag, poke=2.2):
    """One leaked item riding the stream at height y.  On `side` (-1 left, +1 right) it straddles the ribbon's edge,
    poking up to `poke` units past it into the pale gap, at a varied angle, but it keeps clear of the cell walls
    (1 unit past their stroke, plus 0.5) and of the snapped junction bars (2 units, plus 0.5).  side_l / side_r are
    (wall, [bar outlines]) for the gap's two sides."""
    s = v = r = None
    if kind == M:
        s, rot = rnd.uniform(0.58, 0.63), 270 + side * rnd.uniform(10, 30)    # nose-down, leaning to its edge
    elif kind == F:
        s, rot, v = rnd.uniform(0.56, 0.63), rnd.uniform(-55, 55), rnd.randrange(3)
    else:
        rot, r = 0, rnd.uniform(5.5, 6.1)
    pts, rad = _outline(kind, rot, s or 1.0, v or 0, r or 6.0)
    (wl, bars_l), (wr, bars_r) = side_l, side_r
    lo = max(x_on(wl, y + py) - px + 0.7 + rad + 1.5 for px, py in pts)
    hi = min(x_on(wr, y + py) - px - 0.7 - rad - 1.5 for px, py in pts)
    for bars, sg in ((bars_l, -1), (bars_r, 1)):
        for bar in bars:
            for bx, by in bar:
                for px, py in pts:
                    if abs(y + py - by) < 2.8 + rad:
                        if sg < 0:
                            lo = max(lo, bx - px + 0.25 + rad + 2.5)
                        else:
                            hi = min(hi, bx - px - 0.25 - rad - 2.5)
    ys, lefts, rights = rib
    ex0, ex1 = min(px for px, _ in pts), max(px for px, _ in pts)
    tx = _lerp_at(ys, lefts, y) - poke - ex0 if side < 0 else _lerp_at(ys, rights, y) + poke - ex1
    x = min(max(tx, lo), hi) if lo <= hi else (lo + hi) / 2
    return _place(kind, x, y, rnd, rot=rot, s=s, narrow=True, tail="short", tag=tag, v=v, r=r)


def art_barrier(t):
    del _REG[:]
    del _SHAPES[:]
    rnd = random.Random(23)
    tabcol = [TAB_GREEN] + [t["c1"]] * 2 + [CAUSE] * 2
    o = [defs_svg(),
         f'<rect x="1" y="{FT}" width="{W - 2}" height="{FB - FT}" rx="14" fill="url(#{U}-lumen)"/>',
         f'<g clip-path="url(#{U}-clip)">']
    # lanes: each tab's column, outlined so the clear band below reads as "outside every lane"
    for x, col in zip(LANE_X, tabcol):
        o.append(f'<path d="M{x},{LANE_T} V{LANE_B - 12} Q{x},{LANE_B} {x + 12},{LANE_B} H{x + LANE_W - 12} '
                 f'Q{x + LANE_W},{LANE_B} {x + LANE_W},{LANE_B - 12} V{LANE_T} Z" fill="{_mix(col, .085)}" '
                 f'stroke="{_mix(col, .22)}" stroke-width="1"/>')
    # tissue from the basal edge down, inflammation glow (below the lanes), vessel, basement membrane
    o.append(f'<rect x="0" y="{CB}" width="{W}" height="{BLT - CB + 14}" fill="url(#{U}-tissue)"/>')
    o.append(f'<ellipse cx="531" cy="{CT + 96}" rx="224" ry="92" fill="url(#{U}-glow)"/>')
    (a0, a1, a2, a3), (_, b1, b2, b3) = VESSEL
    vessel = (f"M{a0[0]},{a0[1]} C{a1[0]},{a1[1]} {a2[0]},{a2[1]} {a3[0]},{a3[1]} "
              f"C{b1[0]},{b1[1]} {b2[0]},{b2[1]} {b3[0]},{b3[1]}")
    o.append(f'<path d="{vessel} V{FB + 2} H0 Z" fill="url(#{U}-blood)"/>')
    o.append(f'<path d="{vessel}" fill="none" stroke="#E9A09C" stroke-width="3"/>')
    o.append(f'<path d="M0,{CB + 2} H{W}" stroke="#D9A898" stroke-width="2"/>')

    # ---- leaky half geometry first (the streams sit behind the cells)
    cells = [l_cell(c, rnd) for c in LCELLS]
    outlines = [pts for kind, pts, *_ in _SHAPES if kind == "lcell"]
    gaps = []
    for k in range(5):
        wl, wr = cells[k][2], cells[k + 1][1]           # right wall of cell k, left wall of cell k+1
        ytop, ybot = sorted((cells[k][3], cells[k + 1][3]))
        gx = (x_on(wl, ybot + 14) + x_on(wr, ybot + 14)) / 2
        stream, rib, gxn, hy0 = leak_stream(wl, wr, ybot, f"{U}-band{k}")
        gaps.append((wl, wr, (ytop, ybot), gx, gxn, hy0, rib))
        o.append(stream)

    # ---- blood cells (behind the arrows, the delivered nutrients and the leaked items)
    for (x, y, r) in RBCS:
        o.append(rbc(x, y, r))
        _reg("rbc", x, y, 14, 9)
        _reg_rbc(x, y, r)

    # ---- healthy half: six columnar cells, seams sealed by tight junctions
    for i in range(6):
        o.append(h_villi(4 if i == 0 else HX[i], HX[i + 1], rnd))
    # cell 0 runs on under the frame: 4 more microvilli to the left of its first, at the same pitch, from their own
    # random source so every other random draw in the art (bar lengths, jitter) stays as the clearance check tuned it
    lr = random.Random(5)
    o.append(f'<g fill="url(#{U}-mv)" stroke="#C98670" stroke-width=".65">' + "".join(
        f'<rect x="{12 - 4.25 * k - 1.5:.2f}" y="{BT + lr.uniform(-0.6, 0.9):.2f}" width="3" height="{CT - BT + 6}" '
        'rx="1.5"/>' for k in range(1, 5)) + "</g>")
    for i in range(6):
        o.append(h_cell(HX[i], HX[i + 1], 29 if i == 0 else None))
    for x in HX[1:6]:
        o.append(stitches(x, CT + 6))

    # ---- leaky half: the damaged cells, then the snapped junctions across every gap
    for body, *_ in cells:
        o.append(body)
    # The healthy | leaky seam is still sealed: the key's three-bar tight junction, each bar centred on the seam and
    # reaching 3.5 units into both cells, where both walls are present (recheck 2026-11-03: the old two-bar mark
    # was not in the key and ran 5 units into the leaky cell's wall).
    for j in range(3):
        y = CT + 10 + j * 6
        xs = [x0 + (x1 - x0) * (y - y0) / (y1 - y0) for (x0, y0), (x1, y1) in zip(outlines[0], outlines[0][1:] + outlines[0][:1])
              if min(y0, y1) <= y <= max(y0, y1) and y1 != y0]
        xr_ = min(xs)
        xm, half = (SPLIT + xr_) / 2, (xr_ - SPLIT) / 2 + 3.5
        o.append(f'<path d="M{xm - half:.1f},{y:.1f} H{xm + half:.1f}" stroke="{JUNCTION}" stroke-width="2.5" '
                 'stroke-linecap="round"/>')
    hang = [(1, 0, 58), (0, 2, 64), (1, 1, 52), (0, 1, 66), (1, 2, 60)]   # per gap: (side, bar, angle)
    bars = [([], []) for _ in gaps]                                         # per gap: the bar outlines on each side
    for k, (wl, wr, mouth, gx, gxn, hy0, rib) in enumerate(gaps):
        for side, wall, ctop, dirn in ((0, wl, cells[k][3], 1), (1, wr, cells[k + 1][3], -1)):
            for j in range(3):
                y = ctop + 9 + j * 6
                x = x_on(wall, y) - dirn * 0.6
                ang = hang[k][2] if (side, j) == hang[k][:2] else 0
                if k in (1, 3) and side == 0 and j == 2:     # a second hanging bar on two of the gaps
                    ang = 48
                o.append(stub(x, y, rnd.uniform(5.2, 7.4), dirn, ang, reg=True))
                bars[k][side].append(_SHAPES[-1][1])
                _reg("stub", x + dirn * 4, y + (3 if ang else 0), 4.5, 3 if not ang else 5)

    # ---- nutrients through the healthy cells, beside the nucleus (lane -> cell -> blood: the same three letters)
    for x, (s, c) in zip(NUT_X, TRAVEL):
        o.append(arrow(x, R2 + 19, BLT + 40, GREEN, 5.2, 15))
        ga = _shape("arrow", [(x, R2 + 19), (x, BLT + 40 - 15 + 1)], 4.7, False)
        _shape("arrow", [(x - 11.7, BLT + 40 - 16.5), (x + 11.7, BLT + 40 - 16.5), (x, BLT + 43)], 0.8, True, ga)
        o.append(token(x, CT + 40, s, c, 11))
        _reg_tok("tok:cell", x, CT + 40, 11)
        o.append(token(x + 15, BLT + 57, s, c, 11))
        _reg("tok", x + 15, BLT + 57, 12.5, 12.5)
        _reg_tok("tok:blood", x + 15, BLT + 57, 11)

    # ---- the leak streams: a crowd at each gap mouth; then the items ride the stream down, zig-zagging across its
    # edges at varied angles (never single file down the middle), squeeze through the neck and fan out in the blood
    for k, (wl, wr, (ytop, ybot), gx, gxn, hy0, rib) in enumerate(gaps):
        g = random.Random(100 + k)
        kinds = STREAM[k]
        flip = -1 if k % 2 else 1
        aim = (gx, ybot + 12)
        items = []
        # 4 crowding the mouth from the clear band above it (below the lanes, never in one);
        # microbes swim head-first towards the gap
        for i, (cx, cy) in enumerate(CROWD):
            x, y = gx + flip * cx + g.uniform(-2.5, 2.5), ytop + cy + g.uniform(-2.5, 2.5)
            rot = math.degrees(math.atan2(aim[1] - y, aim[0] - x)) + 180 + g.uniform(-15, 15)
            items.append(_place(kinds[i], x, y, g, rot=rot if kinds[i] == M else None, s=0.64, tail="short", tag=f"g{k}c{i}"))
        # 1 squeezing into the mouth, between the snapped junction bars (two draws, as when the mouth held two items,
        # so this one keeps the place the clearance check tuned)
        ym = [ybot + 5 + g.uniform(-1.5, 1.5), g.uniform(-2, 2)][0]
        items.append(_in_gap(kinds[4], wl, wr, ym, 9.5, flip, g, tag=f"g{k}m0"))
        # 3 riding the stream down the gap, each crossing the ribbon's edge on alternate sides
        sides = ((wl, bars[k][0]), (wr, bars[k][1]))
        ride = [ybot + 27 + j * (CB - 56 - ybot) / 2 + g.uniform(-2, 2) for j in range(3)]   # below the bars, to CB - 29
        for i, yy in enumerate(ride):
            items.append(_ride(kinds[5 + i], *sides, rib, yy, -flip if i % 2 == 0 else flip, g, tag=f"g{k}r{i}"))
        # 1 squeezing through the neck, across the basement membrane
        items.append(_place(kinds[8], gxn + flip * 1.5 + g.uniform(-1, 1), CB + 7, g, narrow=True, s=0.56, tail="short",
                            tag=f"g{k}b"))
        # a small fan of leaked items just under the arrowhead
        fan = [(-18, BLT + 38), (17, BLT + 43), (-1, BLT + 62)][:len(kinds) - 9]
        for i, (fx, fy) in enumerate(fan):
            items.append(_place(kinds[9 + i], gxn + flip * fx + g.uniform(-2, 2), fy + g.uniform(-2, 2), g, s=0.66,
                                tag=f"g{k}f{i}"))
        o.extend(items)

    # ---- causes of damage, on the cells: a pill resting on the shrunken cell, bolts striking tops
    px_, py_ = LCELLS[2]["xc"] + 1, cells[2][3] - 7.5
    o.append(pill(px_, py_, -4, 0.82))
    _reg("pill", px_, py_, 12.5, 6.5)
    _reg_pill("pill", px_, py_, -4, 0.82)
    for ci, (bx, rot) in [(4, (650, 10)), (5, (731, -8))]:
        ctop = cells[ci][3]
        a = math.radians(rot)
        tx = 0.82 * (BOLT_TIP[0] * math.cos(a) - BOLT_TIP[1] * math.sin(a))
        ty = 0.82 * (BOLT_TIP[0] * math.sin(a) + BOLT_TIP[1] * math.cos(a))
        cx_, cy_ = bx - tx, ctop - 1 - ty
        o.append(bolt(cx_, cy_, 0.82, rot))
        _reg("bolt", cx_, cy_, 9, 13)
        _reg_bolt("bolt", cx_, cy_, 0.82, rot)
        hx, hy = bx, ctop - 1
        o.append("".join(f'<path d="M{hx + 3.2 * math.cos(math.radians(an)):.1f},{hy + 3.2 * math.sin(math.radians(an)):.1f} '
                         f'L{hx + 6.6 * math.cos(math.radians(an)):.1f},{hy + 6.6 * math.sin(math.radians(an)):.1f}" '
                         f'stroke="{STRESS}" stroke-width="1.5" stroke-linecap="round"/>' for an in (-160, -128, -52, -20)))

    # ---- lane items, tidy under each tab (nothing here leaks)
    for x, (s, c) in zip(NUT_X, TRAVEL):        # the three that travel, each right above its arrow
        o.append(token(x, R2 + 1, s, c))
        _reg("lane:tok", x, R2 + 1, 13.6, 13.6)
        _reg_tok("lane:tok", x, R2 + 1, 12.5)
    for i, (s, c) in enumerate(LANE_TOKENS):
        o.append(token(LANE_TOK_X[i], R1 - 2, s, c))
        _reg("lane:tok", LANE_TOK_X[i], R1 - 2, 13.6, 13.6)
        _reg_tok("lane:tok", LANE_TOK_X[i], R1 - 2, 12.5)
    for (x, y, s, r, v) in [(184, R1 + 2, 1.0, 10, 0), (227, R1, 0.92, -20, 1), (270, R1 + 3, 1.0, 30, 2),
                            (205, R2 + 1, 0.9, 50, 2), (250, R2, 0.95, -40, 0)]:
        o.append(food(x, y, s, r, v))
        _reg("lane:food", x, y, 13 * s, 13 * s)
        _reg_food("lane:food", x, y, s, r, v)
    for (x, y, s, r, v) in [(179, BT - 11, 0.9, 0, 1), (229, BT - 11, 0.88, 20, 0), (279, BT - 11, 0.9, -15, 2)]:
        o.append(food(x, y, s, r, v))   # kept out: resting on the sealed lining
        _reg("rest:food", x, y, 13 * s, 13 * s)
        _reg_food("rest:food", x, y, s, r, v)
    for (x, y, r) in [(336, R1, 18), (378, R1 - 4, -14), (424, R1 + 4, 158), (346, R2 + 2, -26), (402, R2 + 4, 10)]:
        o.append(microbe(x, y, r, 0.92))
        x0, x1, y0, y1 = microbe_extent(r, 0.92)
        _reg("lane:mic", x + (x0 + x1) / 2, y + (y0 + y1) / 2, (x1 - x0) / 2, (y1 - y0) / 2)
        _reg_mic("lane:mic", x, y, r, 0.92)
    for (x, y, r) in [(484, R1, -22), (528, R1 - 3, 14), (572, R1 + 1, -8), (503, R2 + 2, 30), (556, R2 + 4, -24)]:
        o.append(pill(x, y, r, 0.96))
        _reg("lane:pill", x, y, 15, 12)
        _reg_pill("lane:pill", x, y, r, 0.96)
    for (x, y, r) in [(635, R1 + 1, -8), (678, R1 + 5, 10), (721, R1 + 1, -6), (656, R2 + 3, 8), (700, R2 + 3, -10)]:
        o.append(bolt(x, y, 0.9, r))
        _reg("lane:bolt", x, y, 10, 14)
        _reg_bolt("lane:bolt", x, y, 0.9, r)

    o.append(T(16, FB - 12, "BLOODSTREAM", 13, 800, "#FFFFFF", ls=2))
    o.append("</g>")
    o.append(f'<rect x="1" y="{FT}" width="{W - 2}" height="{FB - FT}" rx="14" fill="none" stroke="#C3D5DA" stroke-width="1.4"/>')

    # ---- the five tabs, on top: white type on dark fills (6.2:1 teal, 5.8:1 green, 7.4:1 cause purple)
    for (lab, sub), x, col in zip(TABS, LANE_X, tabcol):
        o.append(f'<rect x="{x}" y="{TY}" width="{LANE_W}" height="{TH}" rx="7" fill="{col}"/>')
        o.append(f'<path d="M{x + 59},{TY + TH - 1} h24 l-12,{PTR} z" fill="{col}"/>')
        o.append(T(x + 71, TY + 18.5, lab, 13.5, 800, "#FFFFFF", "middle"))
        o.append(T(x + 71, TY + 34.5, sub, 11, 600, "#FFFFFF", "middle"))
    return svg(W, FB + 2, "".join(o), "A healthy gut lining with sealed seams beside a leaky one with gaps that let food, "
               "microbes and toxins pour into the bloodstream")


# ----------------------------------------------------------------------------- key
def swatch(markup, vb=30):
    h = vb / 2
    return f'<svg viewBox="{-h} {-h} {vb} {vb}" aria-hidden="true">{markup}</svg>'


def key_html():
    tj = (f'<rect x="-13" y="-11" width="12" height="22" rx="3" fill="url(#{U}-hc)" stroke="#D2937E"/>'
          f'<rect x="1" y="-11" width="12" height="22" rx="3" fill="url(#{U}-hc)" stroke="#D2937E"/>'
          + stitches(0, -6, 3, 5.5, 4.6))
    tr = (f'<rect x="-15" y="-11" width="9" height="22" rx="3" fill="url(#{U}-lc)" stroke="#AE3D31"/>'
          f'<rect x="6" y="-11" width="9" height="22" rx="3" fill="url(#{U}-lc)" stroke="#AE3D31"/>'
          + "".join(stub(-6.2, -6 + j * 5.5, 3.4, 1, 0) + stub(6.2, -6 + j * 5.5, 3.4, -1, 55 if j == 1 else 0)
                    for j in range(3)))
    infl = (f'<circle r="15" fill="url(#{U}-glow)"/><rect x="-9" y="-12.5" width="18" height="25" rx="7" '
            f'fill="url(#{U}-lc)" stroke="#AE3D31"/>' + spark(-2.6, 1.5, 5.6)
            + '<path d="M4.4,-12.5 l2,4.2 l-2.4,3.4 l2.6,4.2" fill="none" stroke="#7A2219" stroke-width="1.2" '
            'stroke-linecap="round" stroke-linejoin="round"/>')   # a damaged cell: red, glowing, sparked, cracked
    mv = (f'<g fill="url(#{U}-mv)" stroke="#C98670" stroke-width=".6">'
          + "".join(f'<rect x="{-11.6 + k * 4.6:.1f}" y="-12" width="3" height="14" rx="1.5"/>' for k in range(6)) + "</g>"
          f'<rect x="-14" y="-1" width="28" height="13" rx="4" fill="url(#{U}-hc)" stroke="#D2937E"/>')
    # the leak as the art draws it: a red ribbon with a dark edge and a gloss streak, tapering into a neck and one
    # bold head (white halo), all one shape
    side = "C{a}6.5,-7 {a}2.8,-4.5 {a}2.8,-0.5 L{a}2.8,2.6 L{a}8.2,2.6 L0,13.6"
    lk = (f'<path d="M-10.6,3.3 L10.6,3.3 L0,16.6 Z" fill="#FFFFFF" stroke="#FFFFFF" stroke-linejoin="round"/>'
          f'<path d="M-6.5,-14 {side.format(a="-")} L8.2,2.6 L2.8,2.6 L2.8,-0.5 C2.8,-4.5 6.5,-7 6.5,-14 Z" '
          f'fill="url(#{U}-klk)"/>'
          f'<path d="M-4.4,-11.5 C-4.4,-7.5 -1.5,-5 -1.5,-1.6" fill="none" stroke="{GLOSS}" stroke-width="1.3" '
          'stroke-linecap="round"/>'
          + "".join(f'<path d="M{a}6.5,-14 {side.format(a=a)}" fill="none" stroke="{EDGE}" stroke-width="1.1" '
                    'stroke-linejoin="round" stroke-linecap="round"/>' for a in ("-", "")))
    mx, mx1, my, my1 = microbe_extent(-34, 0.66)     # centre the key's microbe on its rotated extent
    items = [
        (food(0, 0, 0.95), "Food particle", "not fully digested"),
        (microbe(-(mx + mx1) / 2, -(my + my1) / 2, -34, 0.66), "Microbe", "germs like bacteria"),
        (toxin(0, 0, 9), "Toxin", "made by microbes"),
        (pill(0, 0, -30, 0.85), "Medication", "like ibuprofen"),
        (bolt(0, 0, 0.85, 8), "Stress signal", "stress hormones"),
        (rbc(0, 0, -20, 0.95), "Red blood cell", "carries oxygen"),
        # "food" clashed with the art's "Food particles should stay out".  Not "tiny fingers that soak up nutrients":
        # in this six-column key it ran 6 px into the Absorbed arrow (measured 2026-11-03); this keeps a 7.5 px gap.
        (mv, "Microvilli", "tiny fingers soak up nutrients"),
        (arrow(0, -13, 13, GREEN, 4.2, 11), "Absorbed", "through a cell"),
        (lk, "Leak", "through a gap"),
        (tj, "Tight junction", "seals the seam"),
        (tr, "Torn junction", "seam torn open"),
        (infl, "Inflammation", "red, swollen cells"),
    ]
    cells = "".join(f'<div>{swatch(sw)}<p><b>{a}</b>{b}</p></div>' for sw, a, b in items)
    # key tokens: the art's token, with letters big enough to print at 7 pt or more at 0.22 in
    def ktok(sym, col):
        fs = 13 if len(sym) == 1 else 11.6
        return (f'<circle r="12" fill="{col}" stroke="#fff" stroke-width="2"/><circle r="10.4" fill="url(#{U}-shine)"/>'
                + T(0, fs * 0.36, sym, fs, 800, "#fff", "middle"))
    nut = "".join(f'<span>{swatch(ktok(s, c), 26)}{name}</span>' for s, c, name in NUTRIENT_NAMES)
    # The key names the two regions first (recheck 2026-11-03: only the bottom was labelled, so a child had to
    # guess that the top is the inside of the gut), and says every letter is absorbed, the still ones included.
    # Round 3: the middle band (the lining, and the pale tissue under it) is named too, on the same line.
    return (f'<div class="{U}-key"><span class="{U}-kt">Key<em>Top: inside your gut &middot; Middle: the lining and the '
            f'tissue under it &middot; Bottom: your blood</em></span>'
            f'<div class="{U}-kn"><b>Each letter is a nutrient your gut absorbs:</b>{nut}</div>'
            f'<div class="{U}-kg">{cells}</div></div>')


# ----------------------------------------------------------------------------- front page
# An immune "alert" shield, drawn in kit.icon's 64x64 line style (kit has no shield icon).
SHIELD = '<path d="M32 6 52 13v17c0 13-8.5 22.5-20 27C20.5 52.5 12 43 12 30V13z"/><path d="M32 21v14M32 43v1"/>'


def line_icon(body, size, color="#fff", sw=3.0):
    return (f'<svg class="ic" viewBox="0 0 64 64" style="width:{size};height:{size};color:{color}" fill="none" '
            f'stroke="currentColor" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round" '
            f'aria-hidden="true">{body}</svg>')


OUTCOMES = [
    # Ventura MT et al. Dig Liver Dis 2006;38:732-6 (PMID 16880015): permeability is higher in people with
    # adverse reactions to food and rises with symptom severity.  Gluten and zonulin: Fasano 2011 (docstring).
    (icon("plate", "0.34in", "#fff", 3), "Food reactions",
     "Bloating or other symptoms after foods such as gluten, dairy or soy"),
    # Akdis CA. Nat Rev Immunol 2021;21:739-51 (PMID 33846604): epithelial barrier defects in allergy and
    # atopic dermatitis.  Pike MG et al. J Invest Dermatol 1986;86:101-4 (PMID 3745938): higher gut
    # permeability in children with eczema.
    (line_icon(SHIELD, "0.34in"), "Immune reactions", "Allergies and flare-ups of eczema (itchy, red skin)"),
    # Damaged lining cells absorb less, as in celiac disease: Rubio-Tapia A et al. ACG guideline, Am J
    # Gastroenterol 2023;118:59-76 (PMID 36602836); Wierdsma NJ et al. Nutrients 2013;5:3975-92
    # (PMID 24084055): low zinc in 67 % and low iron stores in 46 % of newly diagnosed celiac patients.  Low iron
    # is a common cause of tiredness (NIH ODS iron fact sheet: iron deficiency anemia brings fatigue).  Round 3: worded
    # as damaged CELLS absorbing less (the celiac evidence), since looser seams alone do not cause malabsorption.
    (icon("battery", "0.34in", "#fff", 3), "Poor absorption",
     "Damaged cells absorb less iron, zinc or vitamin D, so you may tire"),
]


def front(t, ed):
    caps = (f'<div class="{U}-cap"><div class="{U}-ok"><b>Healthy barrier</b>'
            '<span>Seams sealed. Nutrients pass through the cells.</span></div>'
            f'<div class="{U}-bad"><b>Leaky barrier</b>'
            '<span>Inflammation: seams loosen, gaps open. Food, microbes and toxins leak in.</span></div></div>')
    outs = "".join(f'<div>{ic}<p><b>{a}</b>{b}</p></div>' for ic, a, b in OUTCOMES)
    # Gut symptoms with an autoimmune disease belong with the treating clinician too, so the pharmacy edition names
    # the doctor as well; the practitioner edition's "your provider" already is that clinician.
    tell = "{who} and your doctor" if ed.get("rx_title", "").startswith("Pharmacist") else "{who}"
    return (f'<div class="art {U}-art">{art_barrier(t)}</div>{caps}{key_html()}'
            f'<div class="{U}-oh">When the barrier leaks, you may notice</div><div class="{U}-out">{outs}</div>'
            f'<p class="{U}-after">Researchers are also studying how a leaky barrier connects to <b>autoimmune conditions</b> '
            f"such as Hashimoto's thyroiditis, rheumatoid arthritis and lupus. If you live with one, tell {tell} about any "
            'gut symptoms.</p>')


CSS = r"""
.ipx-cap{display:grid;grid-template-columns:40fr 60fr;margin-top:5px;text-align:center}
.ipx-cap>div{padding:0 0.06in;display:flex;flex-direction:column;align-items:center;gap:2px}
.ipx-cap b{display:inline-block;font:800 8.2pt Inter,sans-serif;letter-spacing:.06em;text-transform:uppercase;color:#fff;
  border-radius:99px;padding:1.5px 12px}
.ipx-cap .ipx-ok b{background:var(--deep)}
.ipx-cap .ipx-bad b{background:#B93A2B}
.ipx-cap span{font-size:8.4pt;line-height:1.3;color:#2B3236}
.ipx-key{position:relative;border:1.2px solid #CBD7DB;border-radius:8px;padding:7px 8px 4px;margin-top:14px}
.ipx-kt{position:absolute;top:-7px;left:12px;background:#fff;padding:0 6px;font:800 7.2pt Inter,sans-serif;
  letter-spacing:.16em;text-transform:uppercase;color:var(--deep)}
.ipx-kt em{font:700 7.2pt Inter,sans-serif;font-style:normal;letter-spacing:0;text-transform:none;color:#3D474D;
  margin-left:9px}
.ipx-kn{display:flex;align-items:center;justify-content:space-between;gap:2px 6px;padding:0 4px 2px;margin:0 0 4px;
  border-bottom:1px dashed #D3DCE0;font-size:7pt;line-height:1.2;color:#3D474D}
.ipx-kn b{font-size:7.6pt;color:#1F2A2E;white-space:nowrap}
.ipx-kn span{display:inline-flex;align-items:center;gap:3px;white-space:nowrap}
.ipx-kn svg{flex:none;width:0.22in;height:0.22in;overflow:visible}
.ipx-kg{display:grid;grid-template-columns:repeat(6,auto);justify-content:space-between;gap:4px 6px}
.ipx-kg>div{display:flex;align-items:center;gap:4px;min-width:0}
.ipx-kg svg{flex:none;width:0.25in;height:0.25in;overflow:visible}
.ipx-kg p{margin:0;font-size:7pt;line-height:1.2;color:#3D474D;white-space:nowrap}
.ipx-kg b{display:block;font-size:7.6pt;color:#1F2A2E}
.ipx-oh{font:900 11pt Merriweather,Georgia,serif;color:var(--c1);text-align:center;margin:0.09in 0 0.05in}
.ipx-out{display:grid;grid-template-columns:repeat(3,1fr);gap:0.1in}
.ipx-out>div{display:flex;align-items:center;gap:8px;background:var(--c1);color:#fff;border-radius:7px;padding:0.07in 0.1in}
.ipx-out .ic{flex:none}
.ipx-out p{margin:0;font-size:8.4pt;line-height:1.3}
.ipx-out b{display:block;font-family:Merriweather,Georgia,serif;font-size:10.6pt;margin-bottom:1px}
.ipx-after{margin:0.09in 0 0;text-align:center;font-size:8.6pt;line-height:1.38;color:#2B3236;
  background:var(--soft);border-radius:6px;padding:0.06in 0.16in}
.ipx-after b{color:var(--deep)}
/* ---- this sheet's back page only (the page holding the .ipx-back marker in the lifestyle title) */
/* the 5R step tag at the start of each column's sub-line: a white chip on the teal header */
.ipx-r{display:inline-block;font:800 7pt/1.25 Inter,sans-serif;letter-spacing:.05em;text-transform:uppercase;
  background:#fff;color:var(--deep);border-radius:3px;padding:0 4px;margin-right:2px}
/* the one-line scope statement under the band title */
.sheet.back:has(.ipx-back) .band h2 small{font:600 8.6pt Inter,sans-serif;letter-spacing:0;color:#FFE6D4;margin-top:3px}
/* the duo keeps the kit's 1.35fr | 1fr split; inside the rhythm, morning and evening hold four products each and
   bedtime one, so bedtime gets the narrow slot (its one line wraps to four, still no taller than morning's five) */
.sheet.back:has(.ipx-back) .rhythm{grid-template-columns:1.3fr 1.3fr .6fr}
/* every header keeps a little band for the START HERE badge, so it never touches the title under it: the kit's
   .startb straddles the column's top edge, and at the kit's 0.07in padding its white rim touches the cap height of
   "Nourish the lining" (checked at 4x, 2026-11-03); 10px leaves about 3px clear.  Not a .startt override. */
.sheet.back:has(.ipx-back) .col .need{padding-top:10px}
/* slightly tighter gaps between the back page's blocks, so the footer and the FDA line keep their room */
.sheet.back:has(.ipx-back) .band{padding-top:0.24in!important;padding-bottom:0.14in}
.sheet.back:has(.ipx-back) .ns-title{margin-top:0.1in}
.sheet.back:has(.ipx-back) .cols{margin-top:0.07in}
.sheet.back:has(.ipx-back) .duo{margin-top:0.08in}
.sheet.back:has(.ipx-back) .notes{margin-top:0.08in}
/* three write-in rules at 0.2 in (kit 0.24 in) give the footer and the full FDA notice their room */
.sheet.back:has(.ipx-back) .notes .ln{height:0.2in}
"""


# ----------------------------------------------------------------------------- the sheet
SHEET = {
    "slug": "intestinal-permeability", "code": "ND-GI-101", "theme": "gut", "series": "Gut Health Series",
    "order": 1,
    "title": "Intestinal Permeability", "sub": "Your gut barrier, and why it leaks",
    # Sources for every fact in this paragraph: see the module docstring (Camilleri 2019; Vanuytsel 2014;
    # Bjarnason 1993 and 1984; "every few days" = about 4 to 5 days, van der Flier and Clevers 2009).  Round 3: the
    # last sentence no longer says nutrients help the lining "rebuild": Camilleri 2019 says repair of a leaky barrier by
    # supplements still needs confirmation, so the sheet claims only what food and habits do for a renewing lining.
    "intro": ("Your gut lining is a wall just one cell thick, sealed at the seams by <b>tight junctions</b>. A healthy lining "
              "lets nutrients through and keeps out undigested food, microbes and the toxins they make. Poor diet, infections, "
              "alcohol, some medications and stress can loosen those seams. Researchers call this "
              "<b>increased intestinal permeability</b>; you may know it as leaky gut. The good news: the lining renews itself "
              "every few days, and food and daily habits help it stay strong."),
    "front": front,
    "css": CSS,
    # ------------------------------------------------------------------------- back page
    # Built on NutriDyn's 5R GI Restoration Program [ND584] (ND584 Rev. 1/22;
    # verbatim extract scratchpad protocols/raw/ND584_5R_2022_supplement_section.txt).  NutriDyn's fifth R is
    # Retain ("RESTORE & RETAIN"), not "Rebalance".  The Gut Overgrowth sheet (ND-GI-104) owns step 1, Remove
    # (the antimicrobials), so this back covers the other four, said in one line under the band title.
    # The span marks this sheet's back page for the scoped CSS (.sheet.back:has(.ipx-back)).
    "back": {
        "life_title": f'Lifestyle Modifications<span class="{U}-back"></span>',
        # The first checklist box is ND584's Remove-step diet, so the line says that only Remove's HERBS (the
        # antimicrobials: Spectrum BR, Nutricidin, Paradex) live on the Gut Overgrowth sheet.  One line, no wrap.
        "life_sub": ("From NutriDyn&rsquo;s 5R gut plan: Replace, Repair, Reinoculate and Retain here; "
                     "Remove&rsquo;s herbs are on the Gut Overgrowth sheet."),
        "style": "checks",
        "life": [
            # [ND584] step 1 (days 1-10): "REMOVE all dietary triggers such as gluten, dairy, sugar, artificial
            # sweeteners, soy, and alcohol.  All processed foods and beverages should be eliminated"
            ("Days 1 to 10: take a break from triggers",
             ["Gluten, dairy and soy", "Sugar, artificial sweeteners and alcohol", "Ultra-processed food and drinks"]),
            # [ND584] step 2: "REPLACE eliminated foods with fresh fruits and vegetables, high-quality protein, and
            # healthy fats.  Add fermented foods (sauerkraut, kimchi, kombucha)"; Step 1 list: "at least 5 servings of
            # fruits and vegetables per day, including at least 1 dark green leafy vegetable".  Dairy-free ferments
            # only (recheck 2026-11-03: kefir and yogurt sat beside "take out dairy").
            ("Eat to rebuild the lining",
             ["5 or more fruits and vegetables a day, 1 leafy green", "Good-quality protein and healthy fats",
              "1 fermented food a day: sauerkraut, kimchi or kombucha"]),
            # [ND584] Step 2 (days 11-24): "Begin reintroducing 1 serving daily of a single food category for 3 days.
            # Do this for each food category (wheat/gluten, dairy, sugar).  If you have a reaction, stop consuming
            # this food category immediately and notify your healthcare practitioner."
            ("Days 11 to 24: bring foods back one at a time",
             ["One group at a time: gluten, dairy, sugar", "1 serving a day for 3 days",
              "A reaction? Stop that food and tell your care team"]),
            # NSAIDs raise permeability (Bjarnason 1993; Camilleri 2019, module docstring).  [ND584] Clean Eating Tips:
            # "Avoid eating under stress ... within 2 hours of bedtime.  Eat slowly"; "30 minutes of cardiovascular
            # exercise 5 days per week"; "Block out just 10 minutes daily to focus on relaxation techniques."
            ("Ease the load on the lining",
             ["Ask before regular ibuprofen or naproxen", "Eat slowly and calmly; nothing 2 hours before bed",
              "Move 30 minutes, 5 days a week; 10 calm minutes daily"]),
        ],
        # Products: the 5R's own picks, left to right in the order the line above names the steps.  Label facts,
        # sources and photo notes: build/products.d/intestinal-permeability.json.  Doses follow the protocol where
        # the label allows it (GI Integrity and GI Defend: the labels give no frequency, the 5R and the GI-MAP
        # protocol say twice daily) and the label otherwise (Digestive Complete 2 per meal, not the 5R's 3;
        # UltraBiotic 1 a day).  Days 1 to 10 run Replace, Repair and Reinoculate together; GI Restore takes over
        # from the two shakes on days 11 to 24 [ND584].
        "cols": [
            {"p": "ip_digestive_complete", "need": "Digest food fully",
             "needsub": f'<span class="{U}-r">Replace</span> betaine HCl, pepsin, ox bile, enzymes',
             "bullets": ["Supports protein, fat and starch digestion",
                         "Take with meals, never on an empty stomach"], "dose": "dose_from_db"},
            # Headers 2 and 3 say what the product does for the lining in structure/function words ("Repair the
            # lining" read as a tissue-repair claim under a front page that shows the lining damaged); the REPAIR chip
            # keeps NutriDyn's step name.
            {"p": "ip_gi_integrity", "need": "Nourish the lining", "start": True,
             "needsub": f'<span class="{U}-r">Repair</span> L-glutamine, zinc carnosine, DGL, aloe',
             "bullets": ["Nourishes the cells that line your gut", "Soothes and coats the lining"],
             "dose": "dose_from_db"},
            {"p": "ip_gi_defend", "need": "Bind and protect",
             "needsub": f'<span class="{U}-r">Repair</span> serum-derived bovine immunoglobulins',
             "bullets": ["Helps bind microbial toxins in the gut", "Supports gut barrier and immune balance"],
             "dose": "dose_from_db"},
            # "microbes", not "bacteria": one of the seven strains, S. boulardii, is a yeast.
            {"p": "ip_ultrabiotic_dms", "need": "Add friendly microbes",
             "needsub": f'<span class="{U}-r">Reinoculate</span> 7 strains with S.&nbsp;boulardii',
             "bullets": ["Supports a balanced gut microbiome", "S.&nbsp;boulardii is a yeast: antibiotics spare it"],
             "dose": "dose_from_db"},
            {"p": "ip_gi_restore", "need": "Keep the gains",
             "needsub": f'<span class="{U}-r">Retain</span> gut-support shake for days 11 to 24',
             "bullets": ["Supports the gut barrier and its mucus layer", "Feeds your friendly bacteria"],
             "dose": "dose_from_db"},
        ],
        # The plan line replaces the kit's "add one product a week", which ND584 rules out: "The first 4 R's last
        # 10 days and all four steps should be done at the same time.  The final R is from day 11 to day 24."
        # "The first four products", not ND584's "all four steps": the band names four steps here, Retain included.
        # {plan} = the kit's pill and scoop total (GI Restore's "serving" lines are left out of it, so it is the
        # days 1 to 10 peak: 7 pills and 4 scoops).
        "rhythm_note": ("Days 1 to 10: <b>{plan} a day</b>, the first four products together. "
                        "Days 11 to 24: switch to GI Restore, 1 scoop twice a day."),
        # Four medicine-and-nutrient notes per edition, nine printed lines each (the most the panel holds without
        # pushing the footer off the page): the pharmacist checks interactions and depletions, the provider orders
        # labs, refers and adjusts.  Both editions now carry the probiotic's central-line / weak-immunity caution,
        # the pregnancy line and the test-before-gluten-free point.  The animal sources (pork enzymes and ox bile in
        # Digestive Complete, beef serum in GI Defend) are named on the two serving lines; a separate allergy line
        # would need two more lines than either panel has.
        "rx": {
            "pharmacy": [
                # Betaine HCl raises gastric acidity; not with peptic ulcer or gastritis (Asher's ulcer and HCl email,
                # 2019-09-05) and a standard caution beside NSAIDs, corticosteroids and acid suppressants.
                "<b>Betaine HCl</b> (Digestive Complete) adds acid: not with ulcers or gastritis; ask first with acid "
                "blockers, NSAIDs or steroids.",
                # NIH ODS Zinc fact sheet: UL 40 mg/day from age 19 (34 mg at 14-18, 12 and 23 mg at 4-8 and 9-13),
                # hence "adult limit"; quinolones and tetracyclines: take the antibiotic at least 2 h before or
                # 4-6 h after zinc.  Two scoops: GI Integrity 2 x 16.1 = 32.2 mg; GI Restore
                # 2 x 18.75 = 37.5 mg (products.d).
                "<b>Zinc</b> from two scoops (32 to 38&nbsp;mg a day, near the 40&nbsp;mg adult limit) binds quinolone and "
                "tetracycline antibiotics: take them 2 hours before or 4 to 6 after.",
                # Probiotic 2 h from antibiotics; S. boulardii is a yeast that antifungals inactivate; fungemia risk
                # with central venous catheters or weak immunity (Enache-Angoulvant A, Hennequin C. Clin Infect Dis
                # 2005;41:1559-68, PMID 16267727).
                "<b>Probiotic:</b> 2 hours from antibiotics; antifungals stop its S.&nbsp;boulardii; not with a central "
                "IV line or weak immunity.",
                # Pregnancy: the NutriDyn practice kit's GI Integrity handout, "Check first. Do not use if pregnant or
                # nursing." (repo handouts/nutridyn-practice-kit.pdf); "ask before the others": the UltraBiotic
                # (ND460) and GI Restore (ND529) sell sheets, "If you are pregnant, nursing, or taking medication,
                # consult your healthcare practitioner before use" (products.d).  Celiac serology (tTG-IgA) needs a
                # gluten-containing diet (Rubio-Tapia A et al. ACG guideline, Am J Gastroenterol 2023;118:59-76,
                # PMID 36602836), and the checklist's first box takes gluten out on day 1.
                "<b>Pregnant or nursing?</b> Skip GI Integrity; ask before the others. <b>Celiac test?</b> Do it before "
                "you stop gluten.",
            ],
            "practitioner": [
                # Celiac serology (tTG-IgA) must be done on a gluten-containing diet (Rubio-Tapia 2023, above).  Stool
                # tests before and after the plan: Asher's zonulin case study, 2026-04-24 (stool and zonulin retested
                # after the plan).  No NutriDyn protocol document gives a retest interval (ND584's step 3 is "Day 24
                # & Beyond: meet with practitioner; continue monitoring"), so the sheet names none.
                "<b>Tests:</b> {Who} may order a celiac blood test (tTG-IgA) before you stop gluten, and stool tests "
                "before and after.",
                # Same betaine HCl caution as the pharmacy edition, worded as the provider's adjustment.
                "<b>Ulcer or gastritis, or on an acid blocker, a steroid or a daily NSAID?</b> {Who} may leave out "
                "Digestive Complete: its betaine HCl adds acid.",
                # Pregnancy: the practice kit's GI Integrity handout and the two sell sheets (pharmacy edition, above).
                # [ND584] "If the patient exhibits significant GI inflammation, replace the Dynamic GI Integrity with
                # Dynamic Inflam-Eze for improving inflammatory markers."  The swap has its own lead-in, so it never
                # reads as the pregnancy alternative (Inflam-Eze, products DB R266: turmeric root extract 400 mg,
                # quercetin 500 mg, ginger extract 200 mg, green tea extract 100 mg, none established as safe in
                # pregnancy).
                "<b>Pregnant or nursing?</b> Skip GI Integrity unless {who} says so, and ask before the others. "
                "<b>Marked gut inflammation?</b> The 5R swaps GI Integrity for Inflam-Eze.",
                # S. boulardii fungemia with central venous catheters or weak immunity (Enache-Angoulvant 2005, above).
                "<b>Central IV line or weak immunity?</b> Skip UltraBiotic.",
            ],
        },
    },
}
