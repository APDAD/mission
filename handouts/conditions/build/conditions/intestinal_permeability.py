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

Back page: NutriDyn's 5R GI Restoration Program (ND584).  The Gut Overgrowth sheet owns Remove; this
back covers Replace (Digestive Complete), Repair (GI Integrity, the start pick, and GI Defend),
Reinoculate (UltraBiotic Daily Multi-Strain) and Retain (GI Restore, days 11 to 24).  Label facts and
sources: build/products.d/intestinal-permeability.json.  Back-page CSS is scoped with
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
HX = [4 + i * 50 for i in range(7)]            # healthy cell walls; cell 0 sits inside the frame
# The green arrows cross the cytoplasm of cells 0-2 beside the nucleus (recheck 2026-11-03: an arrow down the
# middle sliced every nucleus in half).  Arrow 5 units left of the cell centre, nucleus 11 units right of it
# (all six healthy cells, so they stay uniform): 2.2 units of clear cytoplasm between the arrow's white halo and
# the nucleus, 4.3 between the nucleus and the cell wall.
NUT_X = [HX[i] + 20 for i in range(3)]
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


# ---- the leak: ONE continuous arrow per gap (recheck 2026-11-03: the old faint band left five detached red
# triangles hanging on the vessel wall like yield signs).  A stream fills the middle of the gap from its mouth,
# deepens as it falls, narrows into a solid neck that crosses the basement membrane and the tissue, and flows
# straight into a bold arrowhead in the blood.  It starts at the gap mouth, below the lanes, so nothing in the
# Medications or Stress lanes ever looks like it leaks.
VESSEL = [((0, BLT + 5), (150, BLT - 5), (300, BLT + 7), (450, BLT)),
          ((450, BLT), (600, BLT - 7), (650, BLT - 4), (W, BLT + 4))]   # the vessel's top edge (S reflected)
NECK_HW = 4.6        # solid neck, 9.2 units wide
HEAD_HW, HEAD_H = 12.5, 26.0


def vessel_y(x):
    """y of the vessel's top edge at x."""
    pts = [p for seg in VESSEL for p in _bez(*seg, n=40)]
    for (x0, y0), (x1, y1) in zip(pts, pts[1:]):
        if x0 <= x <= x1:
            return y0 + (y1 - y0) * (x - x0) / max(1e-6, x1 - x0)
    return BLT


def leak_stream(wl, wr, ybot, gid):
    """The stream down one gap and its neck.  It floods the gap from wall to wall (its edges tuck 1.5 units under
    the cells, which are drawn on top), fades in at the mouth so it has no lid, deepens as it falls and narrows
    into the solid neck.  Returns (markup, x of the neck, y where the head starts)."""
    y0, n = ybot - 2, 16
    ys = [y0 + i * (CB - y0) / n for i in range(n + 1)]
    left = [(x_on(wl, y) - 1.5, y) for y in ys]
    right = [(x_on(wr, y) + 1.5, y) for y in ys[::-1]]
    gx = (x_on(wl, CB - 3) + x_on(wr, CB - 3)) / 2                 # the neck leaves from the middle of the gap floor
    hy0 = vessel_y(gx) + 0.5                                       # the head's base sits on the vessel's top edge
    xl, xr = left[-1][0], right[0][0]
    d = ("M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in left)
         + f" C{xl:.1f},{CB + 4} {gx - NECK_HW:.1f},{CB + 2} {gx - NECK_HW:.1f},{CB + 9}"
         + f" L{gx - NECK_HW:.1f},{hy0 + 2.5:.1f} L{gx + NECK_HW:.1f},{hy0 + 2.5:.1f} L{gx + NECK_HW:.1f},{CB + 9}"
         + f" C{gx + NECK_HW:.1f},{CB + 2} {xr:.1f},{CB + 4} {xr:.1f},{CB:.1f} L"
         + " L".join(f"{x:.1f},{y:.1f}" for x, y in right) + " Z")
    span = hy0 + 2.5 - y0

    def off(y):
        return f"{min(1.0, max(0.0, (y - y0) / span)):.3f}"
    # opacities raised per the recheck (about .3 / .45 / .7), then solid from the gap floor down
    grad = (f'<defs><linearGradient id="{gid}" gradientUnits="userSpaceOnUse" x1="0" y1="{y0:.1f}" x2="0" '
            f'y2="{hy0 + 2.5:.1f}"><stop offset="0" stop-color="{LEAK}" stop-opacity="0"/>'
            f'<stop offset="{off(y0 + 12)}" stop-color="{LEAK}" stop-opacity=".3"/>'
            f'<stop offset="{off(CB - 36)}" stop-color="{LEAK}" stop-opacity=".45"/>'
            f'<stop offset="{off(CB - 3)}" stop-color="{LEAK}" stop-opacity=".7"/>'
            f'<stop offset="{off(CB + 6)}" stop-color="{LEAK}" stop-opacity="1"/>'
            f'<stop offset="1" stop-color="{LEAK}" stop-opacity="1"/></linearGradient></defs>')
    _shape("stream", left + right, 0)
    return grad + f'<path d="{d}" fill="url(#{gid})"/>', gx, hy0


def chevron(x, y, hw):
    """A small flow mark pointing down the stream, drawn behind the items: white on the deeper stream, with a
    dark red edge so it also holds on the pale top of the stream."""
    h = hw * 0.62
    d = f"M{x - hw:.1f},{y - h:.1f} L{x:.1f},{y:.1f} L{x + hw:.1f},{y - h:.1f}"
    return (f'<path d="{d}" fill="none" stroke="#B42A18" stroke-width="3.6" stroke-linecap="round" stroke-linejoin="round" '
            'stroke-opacity=".55"/>'
            f'<path d="{d}" fill="none" stroke="#FFFFFF" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/>')


def leak_head(gx, y0):
    """The bold arrowhead at the end of each stream.  Its base meets the neck with no white seam (the halo runs
    down the two slanted sides only), so the stream and the head read as one arrow."""
    y1, hw = y0 + HEAD_H, HEAD_HW
    _shape("head", [(gx - hw - 1.8, y0), (gx + hw + 1.8, y0), (gx, y1 + 3.0)], 0)
    return (f'<path d="M{gx - hw - 2.2:.1f},{y0 + 1.2:.1f} L{gx + hw + 2.2:.1f},{y0 + 1.2:.1f} L{gx:.1f},{y1 + 3.2:.1f} Z" '
            'fill="#FFFFFF" stroke="#FFFFFF" stroke-width="1" stroke-linejoin="round"/>'
            f'<path d="M{gx - hw:.1f},{y0:.1f} L{gx + hw:.1f},{y0:.1f} L{gx:.1f},{y1:.1f} Z" fill="{LEAK}" '
            f'stroke="{LEAK}" stroke-width="1.2" stroke-linejoin="round"/>')


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
        f'<linearGradient id="{U}-lc" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#D35A47"/>'
        '<stop offset=".28" stop-color="#EC8670"/><stop offset=".6" stop-color="#F29B84"/>'
        '<stop offset="1" stop-color="#D0553F"/></linearGradient>'
        f'<linearGradient id="{U}-lcs" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#C24A39"/>'
        '<stop offset=".3" stop-color="#DD735E"/><stop offset=".62" stop-color="#E5836C"/>'
        '<stop offset="1" stop-color="#BB4634"/></linearGradient>'
        f'<linearGradient id="{U}-lcv" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#B8261A" stop-opacity=".28"/>'
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
        f'<linearGradient id="{U}-klk" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{LEAK}" stop-opacity=".3"/>'
        f'<stop offset=".55" stop-color="{LEAK}" stop-opacity=".55"/><stop offset=".85" stop-color="{LEAK}"/></linearGradient>'
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


def h_cell(x0, x1):
    """A healthy columnar cell; the nucleus sits low (basal) and a little to the right, the same in every
    cell, so the absorbed-nutrient arrow crosses clear cytoplasm beside it."""
    r = 8
    d = f"M{x0},{CB} V{CT + r} Q{x0},{CT} {x0 + r},{CT} H{x1 - r} Q{x1},{CT} {x1},{CT + r} V{CB} Z"
    cx, cy = (x0 + x1) / 2 + NUC_DX, CT + (CB - CT) * 0.74
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
    dict(xc=729, hw=(18, 23, 25, 25, 24), top=5, tilt=-1.5, bites=(0.25, 0.75), crack=1, spark=(11, 25, 7.0), nuc=(-2, 4, 11, 15.5),
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
    right = [(xc + hw[k] + (rnd.uniform(-1.2, 1.2) if 0 < k < 4 else 0), ys[k]) for k in range(5)]
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
    body = (f'<g fill="#E58B76" stroke="#B5473A" stroke-width=".6">{"".join(vil)}</g>'
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
TABS = [("Nutrients", "should pass"), ("Food particles", "should stay out"), ("Microbes", "should stay out"),
        ("Medications", "like ibuprofen"), ("Stress", "of body or mind")]

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
}


def _place(kind, x, y, rnd, rot=None, s=None, narrow=False, tail=True, tag=""):
    """Draw one stream item and register it; microbes in a narrow gap swim nose-down."""
    if kind == M:
        s = s or 0.62
        rot = rot if rot is not None else (rnd.uniform(250, 290) if narrow else rnd.uniform(-60, 240))
    elif kind == F:
        s = s or (0.6 if narrow else 0.66)
        rot = rot if rot is not None else rnd.uniform(-40, 40)
        v = rnd.randrange(3)
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
        r = 5.8 if narrow else 6.2
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


def art_barrier(t):
    del _REG[:]
    del _SHAPES[:]
    rnd = random.Random(23)
    tabcol = [TAB_GREEN] + [t["c1"]] * 4
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
        stream, gxn, hy0 = leak_stream(wl, wr, ybot, f"{U}-band{k}")
        gaps.append((wl, wr, (ytop, ybot), gx, gxn, hy0))
        o.append(stream)

    # ---- blood cells (behind the arrows, the delivered nutrients and the leaked items)
    for (x, y, r) in RBCS:
        o.append(rbc(x, y, r))
        _reg("rbc", x, y, 14, 9)
        _reg_rbc(x, y, r)

    # ---- healthy half: six columnar cells, seams sealed by tight junctions
    for i in range(6):
        o.append(h_villi(HX[i], HX[i + 1], rnd))
    for i in range(6):
        o.append(h_cell(HX[i], HX[i + 1]))
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
    for k, (wl, wr, mouth, gx, gxn, hy0) in enumerate(gaps):
        for side, wall, ctop, dirn in ((0, wl, cells[k][3], 1), (1, wr, cells[k + 1][3], -1)):
            for j in range(3):
                y = ctop + 9 + j * 6
                x = x_on(wall, y) - dirn * 0.6
                ang = hang[k][2] if (side, j) == hang[k][:2] else 0
                if k in (1, 3) and side == 0 and j == 2:     # a second hanging bar on two of the gaps
                    ang = 48
                o.append(stub(x, y, rnd.uniform(5.2, 7.4), dirn, ang, reg=True))
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

    # ---- the leak streams: a crowd at each gap mouth, thinning out as it pours into the blood
    for k, (wl, wr, (ytop, ybot), gx, gxn, hy0) in enumerate(gaps):
        g = random.Random(100 + k)
        kinds = STREAM[k]
        flip = -1 if k % 2 else 1
        aim = (gx, ybot + 12)
        n0, items = len(_REG), []
        # 4 crowding the mouth from the clear band above it (below the lanes, never in one);
        # microbes swim head-first towards the gap
        for i, (cx, cy) in enumerate(CROWD):
            x, y = gx + flip * cx + g.uniform(-2.5, 2.5), ytop + cy + g.uniform(-2.5, 2.5)
            rot = math.degrees(math.atan2(aim[1] - y, aim[0] - x)) + 180 + g.uniform(-15, 15)
            items.append(_place(kinds[i], x, y, g, rot=rot if kinds[i] == M else None, s=0.64, tail="short", tag=f"g{k}c{i}"))
        # 2 squeezing into the mouth, centred in the space between the snapped junction bars
        for i, yy in enumerate([ybot + 5 + g.uniform(-1.5, 1.5), ybot + 24 + g.uniform(-2, 2)]):
            items.append(_in_gap(kinds[4 + i], wl, wr, yy, 9.5, flip * (1 - 2 * i), g, tag=f"g{k}m{i}"))
        # 2 further down the gap, thinning out
        for i, yy in enumerate([CT + 70 + g.uniform(-6, 6), CT + 111 + g.uniform(-6, 6)]):
            items.append(_in_gap(kinds[6 + i], wl, wr, yy, 3.0, g.choice((-1, 1)), g, tag=f"g{k}d{i}"))
        # 1 squeezing through the neck, across the basement membrane
        items.append(_place(kinds[8], gxn + g.uniform(-2, 2), CB + 7, g, narrow=True, s=0.56, tail="short", tag=f"g{k}b"))
        # the bold arrowhead, then a small fan of leaked items just under it
        items.append(leak_head(gxn, hy0))
        fan = [(-18, BLT + 38), (17, BLT + 43), (-1, BLT + 62)][:len(kinds) - 9]
        for i, (fx, fy) in enumerate(fan):
            items.append(_place(kinds[9 + i], gxn + flip * fx + g.uniform(-2, 2), fy + g.uniform(-2, 2), g, s=0.66,
                                tag=f"g{k}f{i}"))
        # flow marks in the open stretches of the stream between the items (drawn first, so the items ride over them)
        spans = sorted((y - hh, y + hh) for _, _, y, _, hh in _REG[n0:] if ybot - 4 < y < CB + 14)
        for (_, b0), (t1, _) in zip(spans, spans[1:]):
            if t1 - b0 >= 13 and b0 < CB - 8:
                yc = min((b0 + t1) / 2, CB - 10)
                hw = min(4.6, (x_on(wr, yc) - x_on(wl, yc)) / 2 - 4.0)
                if hw >= 3:
                    xc = (x_on(wl, yc) + x_on(wr, yc)) / 2
                    o.append(chevron(xc, yc + hw * 0.31, hw))
                    _shape("chev", [(xc - hw - 1.8, yc - hw * 0.31 - 1.8), (xc + hw + 1.8, yc - hw * 0.31 - 1.8),
                                    (xc, yc + hw * 0.31 + 1.8)], 0)
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

    # ---- the five tabs, on top: white type on dark fills (6.2:1 teal, 5.8:1 green)
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
    # the leak as the art draws it: a stream that deepens into a solid neck and one bold head, with a flow mark
    lk = (f'<path d="M-8.5,-14 H8.5 C8.5,-6 2.6,-4.5 2.6,-0.5 V3.4 H-2.6 V-0.5 C-2.6,-4.5 -8.5,-6 -8.5,-14 Z" '
          f'fill="url(#{U}-klk)"/>'
          f'<path d="M-10.2,3.6 H10.2 L0,15.4 Z" fill="#FFFFFF"/>'
          f'<path d="M-8.4,2.6 H8.4 L0,13.2 Z" fill="{LEAK}" stroke="{LEAK}" stroke-width="1" stroke-linejoin="round"/>'
          + chevron(0, -6.2, 3.4))
    mx, mx1, my, my1 = microbe_extent(-34, 0.66)     # centre the key's microbe on its rotated extent
    items = [
        (food(0, 0, 0.95), "Food particle", "not fully digested"),
        (microbe(-(mx + mx1) / 2, -(my + my1) / 2, -34, 0.66), "Microbe", "germs like bacteria"),
        (toxin(0, 0, 9), "Toxin", "made by microbes"),
        (pill(0, 0, -30, 0.85), "Medication", "like ibuprofen"),
        (bolt(0, 0, 0.85, 8), "Stress signal", "stress hormones"),
        (rbc(0, 0, -20, 0.95), "Red blood cell", "carries oxygen"),
        (mv, "Microvilli", "tiny fingers that soak up food"),
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
    return (f'<div class="{U}-key"><span class="{U}-kt">Key<em>Top: inside your gut &middot; Bottom: your blood</em></span>'
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
    # is a common cause of tiredness (NIH ODS iron fact sheet: iron deficiency anemia brings fatigue).
    (icon("battery", "0.34in", "#fff", 3), "Poor absorption", "Low iron, zinc or vitamin D, which can leave you tired"),
]


def front(t, ed):
    caps = (f'<div class="{U}-cap"><div class="{U}-ok"><b>Healthy barrier</b>'
            '<span>Seams sealed. Nutrients pass through the cells.</span></div>'
            f'<div class="{U}-bad"><b>Leaky barrier</b>'
            '<span>Inflammation: seams loosen, gaps open. Food, microbes and toxins leak in.</span></div></div>')
    outs = "".join(f'<div>{ic}<p><b>{a}</b>{b}</p></div>' for ic, a, b in OUTCOMES)
    return (f'<div class="art {U}-art">{art_barrier(t)}</div>{caps}{key_html()}'
            f'<div class="{U}-oh">When the barrier leaks, you may notice</div><div class="{U}-out">{outs}</div>'
            f'<p class="{U}-after">Researchers are also studying how a leaky barrier connects to <b>autoimmune conditions</b> '
            "such as Hashimoto's thyroiditis, rheumatoid arthritis and lupus. If you live with one, ask {who} whether gut "
            'support belongs in your plan.</p>')


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
/* the daily rhythm gets the wider half: morning and evening hold four products each, bedtime one */
.sheet.back:has(.ipx-back) .duo{grid-template-columns:1.5fr 1fr}
.sheet.back:has(.ipx-back) .rhythm{grid-template-columns:1.25fr 1.25fr .72fr}
/* every header keeps a little band for the START HERE badge, so it never touches the title under it */
.sheet.back:has(.ipx-back) .col .need{padding-top:10px}
/* slightly tighter gaps between the back page's blocks, so the footer and the FDA line keep their room */
.sheet.back:has(.ipx-back) .band{padding-top:0.24in!important;padding-bottom:0.14in}
.sheet.back:has(.ipx-back) .ns-title{margin-top:0.1in}
.sheet.back:has(.ipx-back) .cols{margin-top:0.07in}
.sheet.back:has(.ipx-back) .duo{margin-top:0.08in}
.sheet.back:has(.ipx-back) .notes{margin-top:0.08in}
"""


# ----------------------------------------------------------------------------- the sheet
SHEET = {
    "slug": "intestinal-permeability", "code": "ND-GI-101", "theme": "gut", "series": "Gut Health Series",
    "order": 1,
    "title": "Intestinal Permeability", "sub": "Your gut barrier, and why it leaks",
    # Sources for every fact in this paragraph: see the module docstring (Camilleri 2019; Vanuytsel 2014;
    # Bjarnason 1993 and 1984; "every few days" = about 4 to 5 days, van der Flier and Clevers 2009).
    "intro": ("Your gut lining is a wall just one cell thick, sealed at the seams by <b>tight junctions</b>. A healthy lining "
              "lets nutrients through and keeps out undigested food, microbes and the toxins they make. Poor diet, infections, "
              "alcohol, some medications and stress can loosen those seams. Researchers call this "
              "<b>increased intestinal permeability</b>; you may know it as leaky gut. The good news: the lining renews itself "
              "every few days, so the right food, habits and nutrients help it rebuild."),
    "front": front,
    "css": CSS,
    # ------------------------------------------------------------------------- back page
    # Built on NutriDyn's 5R GI Restoration Program [ND584] (ND584 Rev. 1/22, Dropbox id:xHepYs_Ou4AAAAAAAA5smw;
    # verbatim extract scratchpad protocols/raw/ND584_5R_2022_supplement_section.txt).  NutriDyn's fifth R is
    # Retain ("RESTORE & RETAIN"), not "Rebalance".  The Gut Overgrowth sheet (ND-GI-104) owns step 1, Remove
    # (the antimicrobials), so this back covers the other four, said in one line under the band title.
    # The span marks this sheet's back page for the scoped CSS (.sheet.back:has(.ipx-back)).
    "back": {
        "life_title": f'Lifestyle Modifications<span class="{U}-back"></span>',
        "life_sub": ("From NutriDyn&rsquo;s 5R gut plan: this sheet covers Replace, Repair, Reinoculate and Retain. "
                     "Remove is on the Gut Overgrowth sheet."),
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
            {"p": "ip_gi_integrity", "need": "Repair the lining", "start": True,
             "needsub": f'<span class="{U}-r">Repair</span> L-glutamine, zinc carnosine, DGL, aloe',
             "bullets": ["Nourishes the cells that line your gut", "Soothes and coats the lining"],
             "dose": "dose_from_db"},
            {"p": "ip_gi_defend", "need": "Bind and calm",
             "needsub": f'<span class="{U}-r">Repair</span> serum-derived bovine immunoglobulins',
             "bullets": ["Helps bind microbial toxins in the gut", "Supports gut barrier and immune balance"],
             "dose": "dose_from_db"},
            {"p": "ip_ultrabiotic_dms", "need": "Add friendly bacteria",
             "needsub": f'<span class="{U}-r">Reinoculate</span> 7 strains with S.&nbsp;boulardii',
             "bullets": ["Supports a balanced gut microbiome", "S.&nbsp;boulardii is a yeast: antibiotics spare it"],
             "dose": "dose_from_db"},
            {"p": "ip_gi_restore", "need": "Keep the gains",
             "needsub": f'<span class="{U}-r">Retain</span> gut-support shake for days 11 to 24',
             "bullets": ["Supports the gut barrier and its mucus layer", "Feeds your friendly bacteria"],
             "dose": "dose_from_db"},
        ],
        # Three medicine-and-nutrient notes per edition: the pharmacist checks interactions and depletions, the
        # provider orders labs, refers and adjusts.
        "rx": {
            "pharmacy": [
                # Betaine HCl raises gastric acidity; not with peptic ulcer or gastritis (Asher's GERD protocol, Gmail
                # 16d01aaf2b11528e) and a standard caution beside NSAIDs, corticosteroids and acid suppressants.
                "<b>Betaine HCl</b> (Digestive Complete) adds acid: not with an ulcer or gastritis, and ask {who} "
                "before using it with an acid blocker, a daily NSAID or a steroid.",
                # NIH ODS Zinc fact sheet: adult UL 40 mg/day; quinolones and tetracyclines: take the antibiotic at
                # least 2 h before or 4-6 h after zinc.  Two scoops: GI Integrity 2 x 16.1 = 32.2 mg; GI Restore
                # 2 x 18.75 = 37.5 mg (products.d).
                "<b>Zinc</b> from two scoops (32 to 38&nbsp;mg a day, near the 40&nbsp;mg limit) binds quinolone and "
                "tetracycline antibiotics: take them 2 hours before or 4 to 6 after.",
                # Probiotic 2 h from antibiotics; S. boulardii is a yeast that antifungals inactivate; fungemia risk
                # with central venous catheters or weak immunity (Enache-Angoulvant A, Hennequin C. Clin Infect Dis
                # 2005;41:1559-68, PMID 16267727).  Pregnancy: the NutriDyn practice kit's GI Integrity handout,
                # "Check first. Do not use if pregnant or nursing." (repo handouts/nutridyn-practice-kit.pdf).
                "<b>Probiotic:</b> 2 hours from antibiotics; antifungals stop its S.&nbsp;boulardii; not with a central "
                "IV line or weak immunity. <b>Pregnant or nursing?</b> Skip GI Integrity.",
            ],
            "practitioner": [
                # Celiac serology (tTG-IgA) must be done on a gluten-containing diet (Rubio-Tapia A et al. ACG
                # guideline, Am J Gastroenterol 2023;118:59-76, PMID 36602836).  Retest at 12 weeks: Asher's case
                # study MB (Drive 1g_uogbiWY-iw_pLygYDg-mqCGecVSvzsB8tBY6ZVRKs).
                "<b>Test first.</b> {Who} may order a celiac blood test (tTG-IgA) while gluten is still in your diet, "
                "and a stool test now and at 12 weeks.",
                # Same betaine HCl caution as the pharmacy edition, worded as the provider's adjustment.
                "<b>Ulcer or gastritis, or on an acid blocker, a steroid or a daily NSAID?</b> {Who} may leave out "
                "Digestive Complete: its betaine HCl adds acid.",
                # Pregnancy: the NutriDyn practice kit's GI Integrity handout, "Check first. Do not use if pregnant or
                # nursing."  [ND584] "If the patient exhibits significant GI inflammation, replace the Dynamic GI
                # Integrity with Dynamic Inflam-Eze for improving inflammatory markers."
                "<b>Pregnant or nursing?</b> Skip GI Integrity unless {who} says so. With marked gut inflammation, "
                "the 5R swaps it for Inflam-Eze.",
            ],
        },
    },
}
