"""Intestinal Permeability ("leaky gut"), sheet ND-GI-101.

Self-contained: the front-page art, the front builder, the copy and the back-page data all live
here.  Shared drawing helpers come from svgkit (T, svg, TOXIN) and kit (icon).  Every SVG id and CSS
class carries the "ipx" prefix because all sheets share one document in the bundle PDFs.

Front art, per Asher's notes (2026-11-03) and the art director's review of the first redraw:
  - five tabs (Nutrients, Food particles, Microbes, Medications, Stress).  Each tinted lane holds
    only its own tab's items, and nothing that leaks starts inside a lane: the leak streams begin
    at the gap mouths, in the clear band between the lanes and the cells;
  - healthy half: C, D and Zn leave the Nutrients lane, ride a green arrow through the CENTRE of a
    cell body and arrive in the blood (the same three letters all the way); the seams stay sealed
    by three-bar tight junctions;
  - leaky half: six swollen, inflamed cells that differ in size, height and tilt (one is shrunken),
    with notched, ragged walls, bitten tops, broken microvilli, cracks and sparks.  The three-bar
    junctions are snapped in half across every gap, jagged ends, some hanging.  Food particles,
    microbes and toxins crowd each gap mouth, thin out as they pour down a translucent leak stream,
    cross the membrane and fan out under one bold arrowhead in the blood;
  - medications and stress are drawn as causes of damage (a pill resting on an injured cell, bolts
    striking cell tops), never as things that leak: oral medicines are meant to be absorbed;
  - toxins use the series symbol (svgkit.TOXIN red hexagon, white rim), as on the mold sheet;
  - no caption floats on the art; the key names every symbol and every nutrient letter.

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
NUT_X = [HX[i] + 25 for i in range(3)]         # green arrows through the centres of cells 0-2
TRAVEL = [("C", "#B85A16"), ("D", "#2F6DB5"), ("Zn", "#264D8C")]   # lane -> cell -> blood; every token colour
# gives its white letter at least 4.5:1 contrast
LANE_TOKENS = [("Mg", "#8A5A3C"), ("Fe", "#6B3A87"), ("B", "#2E7D4C"), ("Ca", "#187580")]
NUTRIENT_NAMES = [("C", "#B85A16", "vitamin C"), ("D", "#2F6DB5", "vitamin D"), ("Zn", "#264D8C", "zinc"),
                  ("Mg", "#8A5A3C", "magnesium"), ("Fe", "#6B3A87", "iron"), ("B", "#2E7D4C", "B vitamins"),
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


def leak_band(wl, wr, gx, top, gid, neck=BLT + 3):
    """The leak stream: it fills the gap between the two walls (fading in from nothing, so it has no
    edge of its own), then tapers to a slim neck that carries it across the tissue into the blood."""
    ys = [top + i * (CB - top) / 16 for i in range(17)]
    left = [(x_on(wl, y) - 1.5, y) for y in ys]
    right = [(x_on(wr, y) + 1.5, y) for y in ys[::-1]]
    xl, xr = left[-1][0], right[0][0]
    d = ("M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in left)
         + f" C{(xl + gx - 7) / 2:.1f},{CB + 3} {gx - 7:.1f},{CB + 6} {gx - 7:.1f},{CB + 11} L{gx - 7:.1f},{neck} "
         + f"L{gx + 7:.1f},{neck} L{gx + 7:.1f},{CB + 11} C{gx + 7:.1f},{CB + 6} {(xr + gx + 7) / 2:.1f},{CB + 3} {xr:.1f},{CB} L"
         + " L".join(f"{x:.1f},{y:.1f}" for x, y in right) + " Z")
    grad = (f'<defs><linearGradient id="{gid}" gradientUnits="userSpaceOnUse" x1="0" y1="{top:.1f}" x2="0" y2="{neck}">'
            f'<stop offset="0" stop-color="{LEAK}" stop-opacity="0"/><stop offset=".2" stop-color="{LEAK}" stop-opacity=".15"/>'
            f'<stop offset=".84" stop-color="{LEAK}" stop-opacity=".27"/><stop offset="1" stop-color="{LEAK}" stop-opacity=".52"/>'
            '</linearGradient></defs>')
    return grad + f'<path d="{d}" fill="url(#{gid})"/>'


def leak_head(gx, y0=BLT + 2, y1=BLT + 27, hw=13.0):
    """The one bold arrowhead at the end of each leak stream."""
    return (f'<path d="M{gx - hw - 2.4:.1f},{y0 - 1.5:.1f} L{gx + hw + 2.4:.1f},{y0 - 1.5:.1f} L{gx:.1f},{y1 + 3.2:.1f} Z" '
            'fill="#FFFFFF" stroke="#FFFFFF" stroke-width="1.4" stroke-linejoin="round"/>'
            f'<path d="M{gx - hw:.1f},{y0:.1f} L{gx + hw:.1f},{y0:.1f} L{gx:.1f},{y1:.1f} Z" fill="{LEAK}" '
            f'stroke="{LEAK}" stroke-width="1.2" stroke-linejoin="round"/>')


def stitches(x, y, n=3, gap=6.0, half=4.8, col=JUNCTION, sw=2.5):
    return "".join(f'<path d="M{x - half:.1f},{y + j * gap:.1f} H{x + half:.1f}" stroke="{col}" stroke-width="{sw}" '
                   'stroke-linecap="round"/>' for j in range(n))


def stub(x, y, ln, direction, hang=0.0):
    """Half of a snapped tight-junction bar: it sticks out of a cell wall and ends in a jagged break.
    direction +1 points right (out of a gap's left wall), -1 points left; hang tips it down (deg)."""
    pts = [(-1.4, -1.25), (ln - 1.0, -1.25), (ln + 0.8, -0.45), (ln - 0.5, 0.15), (ln + 0.6, 0.75), (ln - 0.8, 1.25),
           (-1.4, 1.25)]
    a = math.radians(hang)
    out = []
    for px, py in pts:
        rx, ry = px * math.cos(a) - py * math.sin(a), px * math.sin(a) + py * math.cos(a)
        out.append(f"{x + direction * rx:.2f},{y + ry:.2f}")
    return f'<polygon points="{" ".join(out)}" fill="{JUNCTION}" stroke="{JUNCTION}" stroke-width=".5" stroke-linejoin="round"/>'


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
    """A healthy columnar cell; the nucleus sits low (basal), centred, the same in every cell."""
    r = 8
    d = f"M{x0},{CB} V{CT + r} Q{x0},{CT} {x0 + r},{CT} H{x1 - r} Q{x1},{CT} {x1},{CT + r} V{CB} Z"
    cx, cy = (x0 + x1) / 2, CT + (CB - CT) * 0.74
    return (f'<path d="{d}" fill="url(#{U}-hc)" stroke="#D2937E" stroke-width="1.2"/>'
            f'<path d="{d}" fill="url(#{U}-hcv)"/>'
            f'<ellipse cx="{cx:.1f}" cy="{cy:.1f}" rx="9" ry="14.5" fill="url(#{U}-hn)" stroke="#B35E57" stroke-width=".9"/>'
            f'<circle cx="{cx + 2:.1f}" cy="{cy - 4:.1f}" r="2.6" fill="#9C423C"/>')


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


def _ext(kind, s=1.0, rot=0.0, r=6.0):
    """(half-width, half-height) of an item, for spacing and gap checks."""
    if kind == M:
        x0, x1, y0, y1 = microbe_extent(rot, s)
        return (x1 - x0) / 2, (y1 - y0) / 2
    if kind == X:
        return r + 1.8, r + 1.8
    return 13 * s, 13 * s


def _place(kind, x, y, rnd, rot=None, s=None, narrow=False, tail=True):
    """Draw one stream item and register it; microbes in a narrow gap swim nose-down."""
    if kind == M:
        s = s or 0.62
        rot = rot if rot is not None else (rnd.uniform(250, 290) if narrow else rnd.uniform(-60, 240))
        x0, x1, y0, y1 = microbe_extent(rot, s, tail)
        _reg(M, x + (x0 + x1) / 2, y + (y0 + y1) / 2, (x1 - x0) / 2, (y1 - y0) / 2)
        return microbe(x, y, rot, s, tail)
    if kind == X:
        r = 5.8 if narrow else 6.2
        _reg(X, x, y, r + 1.8, r + 1.8)
        return toxin(x, y, r)
    s = s or (0.6 if narrow else 0.66)
    _reg(F, x, y, 13 * s, 13 * s)
    return food(x, y, s, rot if rot is not None else rnd.uniform(-40, 40), rnd.randrange(3))


def _in_gap(kind, wl, wr, y, inset, side, rnd):
    """Place an item in a gap at height y, inside the walls less `inset`, nudged to one side."""
    lo, hi = x_on(wl, y) + inset, x_on(wr, y) - inset
    rot = rnd.uniform(250, 290) if kind == M else None
    ew = (microbe_extent(rot, 0.62, "short")[1] - microbe_extent(rot, 0.62, "short")[0]) / 2 if kind == M else \
        (_ext(X, r=5.8)[0] if kind == X else _ext(F, 0.6)[0])
    slack = max(0.0, (hi - lo) / 2 - ew)
    return _place(kind, (lo + hi) / 2 + side * min(slack, rnd.uniform(1.5, 4.0)), y, rnd, rot=rot, narrow=True, tail="short")


def art_barrier(t):
    del _REG[:]
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
    vessel = f"M0,{BLT + 5} C150,{BLT - 5} 300,{BLT + 7} 450,{BLT} S650,{BLT - 4} {W},{BLT + 4}"
    o.append(f'<path d="{vessel} V{FB + 2} H0 Z" fill="url(#{U}-blood)"/>')
    o.append(f'<path d="{vessel}" fill="none" stroke="#E9A09C" stroke-width="3"/>')
    o.append(f'<path d="M0,{CB + 2} H{W}" stroke="#D9A898" stroke-width="2"/>')

    # ---- leaky half geometry first (the streams sit behind the cells)
    cells = [l_cell(c, rnd) for c in LCELLS]
    gaps = []
    for k in range(5):
        wl, wr = cells[k][2], cells[k + 1][1]           # right wall of cell k, left wall of cell k+1
        ytop, ybot = sorted((cells[k][3], cells[k + 1][3]))
        gx = (x_on(wl, ybot + 14) + x_on(wr, ybot + 14)) / 2
        gaps.append((wl, wr, (ytop, ybot), gx))
        o.append(leak_band(wl, wr, gx, ybot + 2, f"{U}-band{k}"))

    # ---- blood cells (behind the arrows, the delivered nutrients and the leaked items)
    for (x, y, r) in [(176, 352, 10), (236, 366, -12), (300, 350, 8), (196, 404, -8), (262, 414, 14), (326, 398, -10),
                      (411, 352, 6), (491, 354, -8), (571, 350, 10), (651, 352, -6), (730, 352, 8),
                      (411, 421, 12), (491, 417, -6), (568, 421, 10), (648, 418, -12), (732, 416, 8), (176, 425, -4)]:
        o.append(rbc(x, y, r))
        _reg("rbc", x, y, 14, 9)

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
    o.append(stitches(SPLIT, CT + 15, n=2))   # the healthy | leaky seam: still holding, but only just
    hang = [(1, 0, 58), (0, 2, 64), (1, 1, 52), (0, 1, 66), (1, 2, 60)]   # per gap: (side, bar, angle)
    for k, (wl, wr, mouth, gx) in enumerate(gaps):
        for side, wall, ctop, dirn in ((0, wl, cells[k][3], 1), (1, wr, cells[k + 1][3], -1)):
            for j in range(3):
                y = ctop + 9 + j * 6
                x = x_on(wall, y) - dirn * 0.6
                ang = hang[k][2] if (side, j) == hang[k][:2] else 0
                if k in (1, 3) and side == 0 and j == 2:     # a second hanging bar on two of the gaps
                    ang = 48
                o.append(stub(x, y, rnd.uniform(5.2, 7.4), dirn, ang))
                _reg("stub", x + dirn * 4, y + (3 if ang else 0), 4.5, 3 if not ang else 5)

    # ---- nutrients through the healthy cell bodies (lane -> cell -> blood: the same three letters)
    for x, (s, c) in zip(NUT_X, TRAVEL):
        o.append(arrow(x, R2 + 19, BLT + 40, GREEN, 5.2, 15))
        o.append(token(x, CT + 40, s, c, 11))
        o.append(token(x + 15, BLT + 57, s, c, 11))
        _reg("tok", x + 15, BLT + 57, 12.5, 12.5)

    # ---- the leak streams: a crowd at each gap mouth, thinning out as it pours into the blood
    for k, (wl, wr, (ytop, ybot), gx) in enumerate(gaps):
        g = random.Random(100 + k)
        kinds = STREAM[k]
        flip = -1 if k % 2 else 1
        aim = (gx, ybot + 12)
        # 4 crowding the mouth from the clear band above it (below the lanes, never in one);
        # microbes swim head-first towards the gap
        for i, (cx, cy) in enumerate(CROWD):
            x, y = gx + flip * cx + g.uniform(-2.5, 2.5), ytop + cy + g.uniform(-2.5, 2.5)
            rot = math.degrees(math.atan2(aim[1] - y, aim[0] - x)) + 180 + g.uniform(-15, 15)
            o.append(_place(kinds[i], x, y, g, rot=rot if kinds[i] == M else None, s=0.64, tail="short"))
        # 2 squeezing into the mouth, centred in the space between the snapped junction bars
        for i, yy in enumerate([ybot + 5 + g.uniform(-1.5, 1.5), ybot + 24 + g.uniform(-2, 2)]):
            o.append(_in_gap(kinds[4 + i], wl, wr, yy, 9.5, flip * (1 - 2 * i), g))
        # 2 further down the gap, thinning out
        for i, yy in enumerate([CT + 70 + g.uniform(-6, 6), CT + 111 + g.uniform(-6, 6)]):
            o.append(_in_gap(kinds[6 + i], wl, wr, yy, 3.0, g.choice((-1, 1)), g))
        # 1 crossing the basement membrane into the tissue
        o.append(_place(kinds[8], gx + g.uniform(-2, 2), CB + 7, g, narrow=True, s=0.56, tail="short"))
        # the bold arrowhead, then a small fan of leaked items just under it
        o.append(leak_head(gx))
        fan = [(-18, BLT + 38), (17, BLT + 43), (-1, BLT + 62)][:len(kinds) - 9]
        for i, (fx, fy) in enumerate(fan):
            o.append(_place(kinds[9 + i], gx + flip * fx + g.uniform(-2, 2), fy + g.uniform(-2, 2), g, s=0.66))

    # ---- causes of damage, on the cells: a pill resting on the shrunken cell, bolts striking tops
    px_, py_ = LCELLS[2]["xc"] + 1, cells[2][3] - 7.5
    o.append(pill(px_, py_, -4, 0.82))
    _reg("pill", px_, py_, 12.5, 6.5)
    for ci, (bx, rot) in [(4, (650, 10)), (5, (731, -8))]:
        ctop = cells[ci][3]
        a = math.radians(rot)
        tx = 0.82 * (BOLT_TIP[0] * math.cos(a) - BOLT_TIP[1] * math.sin(a))
        ty = 0.82 * (BOLT_TIP[0] * math.sin(a) + BOLT_TIP[1] * math.cos(a))
        cx_, cy_ = bx - tx, ctop - 1 - ty
        o.append(bolt(cx_, cy_, 0.82, rot))
        _reg("bolt", cx_, cy_, 9, 13)
        hx, hy = bx, ctop - 1
        o.append("".join(f'<path d="M{hx + 3.2 * math.cos(math.radians(an)):.1f},{hy + 3.2 * math.sin(math.radians(an)):.1f} '
                         f'L{hx + 6.6 * math.cos(math.radians(an)):.1f},{hy + 6.6 * math.sin(math.radians(an)):.1f}" '
                         f'stroke="{STRESS}" stroke-width="1.5" stroke-linecap="round"/>' for an in (-160, -128, -52, -20)))

    # ---- lane items, tidy under each tab (nothing here leaks)
    for x, (s, c) in zip(NUT_X, TRAVEL):        # the three that travel, each right above its arrow
        o.append(token(x, R2 + 1, s, c))
        _reg("lane:tok", x, R2 + 1, 13.6, 13.6)
    for i, (s, c) in enumerate(LANE_TOKENS):
        o.append(token(29 + i * 100 / 3, R1 - 2, s, c))
        _reg("lane:tok", 29 + i * 100 / 3, R1 - 2, 13.6, 13.6)
    for (x, y, s, r, v) in [(184, R1 + 2, 1.0, 10, 0), (227, R1, 0.92, -20, 1), (270, R1 + 3, 1.0, 30, 2),
                            (205, R2 + 1, 0.9, 50, 2), (250, R2, 0.95, -40, 0)]:
        o.append(food(x, y, s, r, v))
        _reg("lane:food", x, y, 13 * s, 13 * s)
    for (x, y, s, r, v) in [(179, BT - 11, 0.9, 0, 1), (229, BT - 11, 0.88, 20, 0), (279, BT - 11, 0.9, -15, 2)]:
        o.append(food(x, y, s, r, v))   # kept out: resting on the sealed lining
        _reg("rest:food", x, y, 13 * s, 13 * s)
    for (x, y, r) in [(336, R1, 18), (378, R1 - 4, -14), (424, R1 + 4, 158), (346, R2 + 2, -26), (402, R2 + 4, 10)]:
        o.append(microbe(x, y, r, 0.92))
        x0, x1, y0, y1 = microbe_extent(r, 0.92)
        _reg("lane:mic", x + (x0 + x1) / 2, y + (y0 + y1) / 2, (x1 - x0) / 2, (y1 - y0) / 2)
    for (x, y, r) in [(484, R1, -22), (528, R1 - 3, 14), (572, R1 + 1, -8), (503, R2 + 2, 30), (556, R2 + 4, -24)]:
        o.append(pill(x, y, r, 0.96))
        _reg("lane:pill", x, y, 15, 12)
    for (x, y, r) in [(635, R1 + 1, -8), (678, R1 + 5, 10), (721, R1 + 1, -6), (656, R2 + 3, 8), (700, R2 + 3, -10)]:
        o.append(bolt(x, y, 0.9, r))
        _reg("lane:bolt", x, y, 10, 14)

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
    lk = (f'<path d="M-8,-14 H8 L4,2 H-4 Z" fill="{_mix(LEAK, .3, "#FFFFFF")}"/>'
          f'<path d="M-9,1 H9 L0,13 Z" fill="{LEAK}" stroke="#FFFFFF" stroke-width="1"/>'
          + toxin(0, -7, 3.6))
    items = [
        (food(0, 0, 0.95), "Food particle", "not fully digested"),
        (microbe(-8, 6, -34, 0.66), "Microbe", "germs like bacteria"),
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
    return (f'<div class="{U}-key"><span class="{U}-kt">Key</span>'
            f'<div class="{U}-kn"><b>Each letter is a nutrient:</b>{nut}</div>'
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
    (line_icon(SHIELD, "0.34in"), "Immune overload", "Allergies and flare-ups of eczema (itchy, red skin)"),
    # Damaged lining cells absorb less, as in celiac disease: Rubio-Tapia A et al. ACG guideline, Am J
    # Gastroenterol 2023;118:59-76 (PMID 36602836); Wierdsma NJ et al. Nutrients 2013;5:3975-92
    # (PMID 24084055): low zinc in 67 % and low iron stores in 46 % of newly diagnosed celiac patients.
    (icon("battery", "0.34in", "#fff", 3), "Poor absorption", "Damaged cells take in less iron, zinc and vitamin D"),
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
    # Back page: unchanged from the first draft (a later pass revises the products).
    "back": {
        "life_title": "Lifestyle Modifications", "style": "checks",
        "life": [("Find and remove food triggers", ["Gluten", "Dairy", "Soy", "Ask about a 3-week elimination trial"]),
                 ("Protect your gut flora", ["Use antibiotics only when truly needed", "Add one fermented food a day (kefir, yogurt, sauerkraut)"]),
                 ("Eat whole, unprocessed foods", ["Cut added sugar and ultra-processed snacks", "Fill half the plate with vegetables and fruit", "Work up to 25 to 30 g of fiber a day"]),
                 ("Ease the load on the lining", ["Keep alcohol low", "Ask before regular ibuprofen or naproxen", "Sleep 7 to 9 hours, manage stress"])],
        "cols": [
            {"p": "gi_integrity", "need": "Rebuild the lining", "needsub": "L-glutamine, zinc carnosine, DGL, aloe", "start": True,
             "bullets": ["Fuel for the cells that line your gut", "Soothing botanicals coat and calm"],
             "dose": "1 scoop daily", "dosesub": "in 6 to 8 oz water"},
            {"p": "ultrabiotic_dms", "need": "Rebalance gut flora", "needsub": "multi-strain probiotic + S. boulardii",
             "bullets": ["Seven friendly strains", "S. boulardii keeps working alongside antibiotics"],
             "dose": "1 capsule daily", "dosesub": "at bedtime"},
            {"p": "gi_defend", "need": "Bind and calm", "needsub": "serum-derived bovine immunoglobulins",
             "bullets": ["Immunoglobulins bind microbial toxins in the gut", "Supports barrier function and immune balance"],
             "dose": "dose_from_db"},
            {"p": "curcumin_bcm95", "need": "Cool the fire", "needsub": "curcumin, the active compound in turmeric",
             "bullets": ["Supports a healthy inflammatory response", "Enhanced-absorption curcumin"],
             "dose": "dose_from_db"},
            {"p": "enzymes", "need": "Digest it fully", "needsub": "digestive enzymes",
             "bullets": ["Breaks food down so fewer large particles reach the lining", "Take with your largest meals"],
             "dose": "dose_from_db"},
        ],
        "rx": ["<b>NSAIDs</b> (ibuprofen, naproxen) used regularly can irritate the gut lining. Ask about alternatives.",
               "<b>Antibiotics:</b> take the probiotic 2 hours apart from each dose and keep going 2 weeks after the course.",
               "<b>Acid blockers</b> long term can lower magnesium and B12. Ask about a check."],
    },
}
