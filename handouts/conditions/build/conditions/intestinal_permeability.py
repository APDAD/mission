"""Intestinal Permeability ("leaky gut"), sheet ND-GI-101.

Self-contained: the front-page art, the front builder, the copy and the back-page data all live
here.  Shared drawing helpers come from svgkit (T, svg) and kit (icon).  Every SVG id and CSS class
carries the "ipx" prefix because all sheets share one document in the bundle PDFs.

Front art, per Asher's notes (2026-11-03):
  - five tabs (Nutrients, Food particles, Microbes, Medications, Stress), each tab's items in its
    own tinted lane directly under it;
  - healthy half: nutrients pass THROUGH the cell bodies (green arrows), the seams stay sealed;
  - leaky half: wide, ragged gaps, torn tight junctions, swollen, damaged and inflamed cells, and a
    stream of food particles, microbes and toxins pouring through the gaps into a clearly
    labelled bloodstream (bold red arrows);
  - no caption floats on the art: the two half captions sit in clear space under it;
  - a key names every symbol.
Medications are drawn as a cause of damage (pills resting on injured cells), not as something that
leaks into the blood: oral medicines are meant to be absorbed, so drawing them as "should have
stayed out" would be wrong.  The stream carries the microbes' toxins instead.

Condition facts (sources):
  - One layer of cells sealed by tight junctions; diet, infection, alcohol, NSAIDs and stress can
    raise permeability: Camilleri M. Leaky gut: mechanisms, measurement and clinical implications
    in humans. Gut 2019;68:1516-26.
  - Psychological stress raises permeability in people: Vanuytsel T et al. Gut 2014;63:1293-9.
  - NSAIDs raise small-intestine permeability: Bjarnason I et al. Gastroenterology 1993;104:1832-47.
  - The lining renews itself every few days (about 4 to 5): van der Flier LG, Clevers H.
    Annu Rev Physiol 2009;71:241-60.
  - Barrier and autoimmunity research: Fasano A. Physiol Rev 2011;91:151-75; Mu Q et al.
    Front Immunol 2017;8:598.
"""
import math
import random

from kit import icon
from svgkit import T, svg

U = "ipx"

# ----------------------------------------------------------------------------- geometry
W = 760                 # art width in SVG units; prints 7.66 in wide, so 1 unit = 0.725 pt (7 pt = 9.7 units)
FT, FB = 1, 460         # frame top / bottom
TY, TH = 8, 46          # tab top / height
LANE_B = 160            # lanes end here
BT = 170                # tips of the healthy microvilli
CT = 184                # apical membrane (top of the cell bodies)
CB = 328                # basal edge of the cells
BLT = 348               # top of the blood vessel
SPLIT = 304             # healthy | leaky

GREEN = "#23894F"       # nutrients tab and the absorbed-through-a-cell arrow
LEAK = "#E0412A"        # the leak path through a gap
JUNCTION = "#5E2F22"    # tight-junction stitches
STRESS = "#8150B8"

HX = [-2 + i * 51 for i in range(7)]           # healthy cell walls
NUT_X = [HX[i] + 16 for i in range(3)]          # nutrient arrows, through the cell bodies
LX = [343, 427, 506, 586, 665, 744]             # leaky cell centres
GX = [(a + b) / 2 for a, b in zip(LX, LX[1:])]  # gap centres: the leak arrows


# ----------------------------------------------------------------------------- symbols
# Every symbol is drawn centred on (x, y) so the key can reuse it at (0, 0).
def token(x, y, sym, col, r=12.5):
    fs = 12.5 if len(sym) == 1 else 10.4
    return (f'<g transform="translate({x:.1f},{y:.1f})"><circle r="{r}" fill="{col}" stroke="#fff" stroke-width="2.2"/>'
            f'<circle r="{r - 1.6:.1f}" fill="url(#{U}-shine)"/>'
            + T(0, fs * 0.36, sym, fs, 800, "#fff", "middle") + "</g>")


FOOD = ["M-11,-3 C-12,-11 -2,-14 5,-11 C13,-8 14,1 9,7 C4,12 -6,12 -10,6 C-12,3 -11,0 -11,-3Z",
        "M-12,1 C-13,-6 -6,-11 1,-11 C8,-11 13,-6 12,1 C11,8 5,11 -1,11 C-7,11 -11,7 -12,1Z",
        "M-10,-7 C-4,-12 7,-11 11,-5 C14,1 10,9 3,10 C-2,11 -6,8 -9,9 C-13,9 -14,2 -12,-2 C-12,-4 -11,-6 -10,-7Z"]


def food(x, y, s=1.0, rot=0, v=0):
    return (f'<g transform="translate({x:.1f},{y:.1f}) rotate({rot:.0f}) scale({s})">'
            f'<path d="{FOOD[v % 3]}" fill="url(#{U}-food)" stroke="#6E4A2C" stroke-width="1.3"/>'
            '<path d="M-6,-6.5 C-3,-9 2,-9 5,-7" fill="none" stroke="#F6E2C6" stroke-width="1.8" stroke-linecap="round"/>'
            '<circle cx="-3" cy="2" r="1.5" fill="#86593A"/><circle cx="4" cy="-1" r="1.2" fill="#86593A"/>'
            '<circle cx="1" cy="5.5" r="1.1" fill="#86593A"/></g>')


def microbe(x, y, rot=0, s=1.0, tail=True):
    hairs = "".join(f"M{-9 + i * 4.5:.1f},-6.4 l-1.3,-3.8 M{-9 + i * 4.5:.1f},6.4 l-1.3,3.8 " for i in range(5))
    flag = "M14.6,0 c3,-3.6 6,3.6 9,0 s6,3.6 9,0" if tail else ""
    return (f'<g transform="translate({x:.1f},{y:.1f}) rotate({rot:.0f}) scale({s})">'
            f'<path d="{hairs}{flag}" fill="none" stroke="#4C7224" stroke-width="1.3" stroke-linecap="round"/>'
            f'<rect x="-15" y="-6.6" width="30" height="13.2" rx="6.6" fill="url(#{U}-mic)" stroke="#4C7224" stroke-width="1.3"/>'
            '<path d="M-10,-3.2 H7" stroke="#EAF6D2" stroke-width="2" stroke-linecap="round"/>'
            '<circle cx="-5" cy="1.9" r="1.7" fill="#4C7224"/><circle cx="3.6" cy="1.3" r="1.5" fill="#4C7224"/></g>')


def toxin(x, y, r=7.0, rot=0):
    pts = " ".join(f"{r * math.cos(math.radians(a + rot)):.2f},{r * math.sin(math.radians(a + rot)):.2f}"
                   for a in range(30, 390, 60))
    return (f'<g transform="translate({x:.1f},{y:.1f})"><polygon points="{pts}" fill="#F6C332" stroke="#4A3600" '
            f'stroke-width="1.6" stroke-linejoin="round"/><circle r="{r * 0.3:.2f}" fill="#4A3600"/></g>')


def pill(x, y, rot=0, s=1.0):
    return (f'<g transform="translate({x:.1f},{y:.1f}) rotate({rot:.0f}) scale({s})">'
            '<rect x="-14.5" y="-6.8" width="29" height="13.6" rx="6.8" fill="#FFFFFF" stroke="#244F93" stroke-width="1.5"/>'
            '<path d="M0,-6.8 H7.7 A6.8,6.8 0 0 1 7.7,6.8 H0 Z" fill="#2B5DA8"/>'
            '<path d="M-10,-3.1 H-3" stroke="#D3DCE9" stroke-width="2" stroke-linecap="round"/>'
            '<path d="M3,-3.1 H9" stroke="#86A8DC" stroke-width="2" stroke-linecap="round"/></g>')


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


def stitches(x, y, n=3, gap=6.0, half=4.8, col=JUNCTION, sw=2.5):
    return "".join(f'<path d="M{x - half:.1f},{y + j * gap:.1f} H{x + half:.1f}" stroke="{col}" stroke-width="{sw}" '
                   'stroke-linecap="round"/>' for j in range(n))


def torn(xl, xr, y, ln=6.5):
    """Torn tight junction across a gap: stubs hang off both walls, the middle is missing."""
    out = []
    for j, dy in enumerate((0, 8)):
        yy = y + dy
        out.append(f'<path d="M{xl - 1:.1f},{yy:.1f} l{ln:.1f},{ln * 0.55 + j:.1f}" stroke="{JUNCTION}" stroke-width="2.5" stroke-linecap="round"/>')
        out.append(f'<path d="M{xr + 1:.1f},{yy + 1:.1f} l{-ln:.1f},{ln * 0.6 + j:.1f}" stroke="{JUNCTION}" stroke-width="2.5" stroke-linecap="round"/>')
    return "".join(out)


# ----------------------------------------------------------------------------- defs
def defs_svg():
    return (
        "<defs>"
        f'<clipPath id="{U}-clip"><rect x="1" y="{FT}" width="{W - 2}" height="{FB - FT}" rx="14"/></clipPath>'
        f'<linearGradient id="{U}-lumen" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#F6FAFB"/>'
        '<stop offset="1" stop-color="#E7F2F5"/></linearGradient>'
        f'<linearGradient id="{U}-tissue" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FBEDE8"/>'
        '<stop offset="1" stop-color="#F3D6CC"/></linearGradient>'
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
        f'<linearGradient id="{U}-lcv" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#B8261A" stop-opacity=".28"/>'
        '<stop offset=".3" stop-color="#B8261A" stop-opacity="0"/><stop offset=".85" stop-color="#7A1D14" stop-opacity="0"/>'
        '<stop offset="1" stop-color="#7A1D14" stop-opacity=".22"/></linearGradient>'
        f'<linearGradient id="{U}-mv" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#F9DDD0"/>'
        '<stop offset="1" stop-color="#EDB29B"/></linearGradient>'
        f'<radialGradient id="{U}-hn" cx=".38" cy=".32" r=".75"><stop offset="0" stop-color="#F3ABA2"/>'
        '<stop offset=".6" stop-color="#DE8077"/><stop offset="1" stop-color="#C86A62"/></radialGradient>'
        f'<radialGradient id="{U}-ln" cx=".38" cy=".32" r=".75"><stop offset="0" stop-color="#D45A50"/>'
        '<stop offset="1" stop-color="#9C2F29"/></radialGradient>'
        f'<radialGradient id="{U}-glow" cx=".5" cy=".5" r=".5"><stop offset="0" stop-color="#FF5A36" stop-opacity=".45"/>'
        '<stop offset=".7" stop-color="#FF6A3D" stop-opacity=".17"/><stop offset="1" stop-color="#FF6A3D" stop-opacity="0"/></radialGradient>'
        f'<radialGradient id="{U}-shine" cx=".35" cy=".28" r=".7"><stop offset="0" stop-color="#FFFFFF" stop-opacity=".5"/>'
        '<stop offset=".6" stop-color="#FFFFFF" stop-opacity="0"/></radialGradient>'
        f'<radialGradient id="{U}-food" cx=".38" cy=".3" r=".8"><stop offset="0" stop-color="#DDB68A"/>'
        '<stop offset="1" stop-color="#A97849"/></radialGradient>'
        f'<linearGradient id="{U}-mic" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#C2DE8E"/>'
        '<stop offset="1" stop-color="#86B24C"/></linearGradient>'
        "</defs>")


# ----------------------------------------------------------------------------- cells
def _smooth(pts):
    """Catmull-Rom spline through pts as cubic Bezier commands (the path is already at pts[0])."""
    d = []
    n = len(pts)
    for i in range(n - 1):
        p0 = pts[i - 1] if i else pts[i]
        p1, p2 = pts[i], pts[i + 1]
        p3 = pts[i + 2] if i + 2 < n else p2
        c1 = (p1[0] + (p2[0] - p0[0]) / 6, p1[1] + (p2[1] - p0[1]) / 6)
        c2 = (p2[0] - (p3[0] - p1[0]) / 6, p2[1] - (p3[1] - p1[1]) / 6)
        d.append(f"C{c1[0]:.1f},{c1[1]:.1f} {c2[0]:.1f},{c2[1]:.1f} {p2[0]:.1f},{p2[1]:.1f}")
    return " ".join(d)


def h_villi(x0, x1, rnd):
    """Brush border: dense, even, round-tipped microvilli (drawn before the body hides their bases)."""
    pitch, fw = 4.25, 3.0
    n = int((x1 - x0 - 10) / pitch)
    start = (x0 + x1) / 2 - (n - 1) * pitch / 2
    fingers = "".join(f'<rect x="{start + k * pitch - fw / 2:.2f}" y="{BT + rnd.uniform(-0.6, 0.9):.2f}" width="{fw}" '
                      f'height="{CT - BT + 6}" rx="{fw / 2:.2f}"/>' for k in range(n))
    return f'<g fill="url(#{U}-mv)" stroke="#C98670" stroke-width=".65">{fingers}</g>'


def h_cell(x0, x1, nuc_dx=0.0):
    r = 8
    d = f"M{x0},{CB} V{CT + r} Q{x0},{CT} {x0 + r},{CT} H{x1 - r} Q{x1},{CT} {x1},{CT + r} V{CB} Z"
    cx, cy = (x0 + x1) / 2 + nuc_dx, CT + (CB - CT) * 0.67
    return (f'<path d="{d}" fill="url(#{U}-hc)" stroke="#D2937E" stroke-width="1.2"/>'
            f'<path d="{d}" fill="url(#{U}-hcv)"/>'
            f'<ellipse cx="{cx:.1f}" cy="{cy:.1f}" rx="9.5" ry="15.5" fill="url(#{U}-hn)" stroke="#B35E57" stroke-width=".9"/>'
            f'<circle cx="{cx + 2:.1f}" cy="{cy - 4:.1f}" r="2.8" fill="#9C423C"/>')


LEVELS = [10, 36, 76, 114]   # offsets below the cell top / CT where a leaky cell's half-width is set


def l_cell(xc, top, rnd, hw=(19, 24, 28, 27, 26), left_wall=None, bites=(), crack_dx=8.0, nuc_dx=0.0):
    """A swollen, inflamed, damaged cell: bulging walls, an eroded and bitten top, broken
    microvilli, a crack and a dark, swollen nucleus.  Returns (svg, left wall x at the top,
    right wall x at the top)."""
    ys = [top + LEVELS[0], CT + LEVELS[1], CT + LEVELS[2], CT + LEVELS[3], CB]
    left = [(xc - hw[k] + (rnd.uniform(-1.6, 1.6) if 0 < k < 4 else 0), ys[k]) for k in range(5)]
    right = [(xc + hw[k] + (rnd.uniform(-1.6, 1.6) if 0 < k < 4 else 0), ys[k]) for k in range(5)]
    if left_wall is not None:            # the first leaky cell still leans on the healthy side
        left = [(left_wall[k], ys[k]) for k in range(5)]
    xl, xr = left[0][0], right[0][0]
    m = 8
    tops = []
    for k in range(m + 1):
        f = k / m
        y = top + 1.5 + rnd.uniform(-1.0, 2.6)
        for b in bites:
            if abs(f - b) < 0.07:
                y += 4.5
        tops.append((_lerp(xl + 5, xr - 5, f), y))
    chain = left[::-1] + tops + right
    d = f"M{chain[0][0]:.1f},{chain[0][1]:.1f} " + _smooth(chain) + " Z"
    vil = []
    for x, y in tops[1:-1]:
        for dx in (-2.4, 2.4):
            h = rnd.choice([0, 0, 3, 4, 6, 8])
            if h:
                rot = rnd.uniform(-24, 24)
                vil.append(f'<rect x="{x + dx - 1.5:.1f}" y="{y - h:.1f}" width="3" height="{h + 6}" rx="1.5" '
                           f'transform="rotate({rot:.0f} {x + dx:.1f} {y + 2:.1f})"/>')
    cx = xc + nuc_dx
    cy = CT + (CB - CT) * 0.66 + 3
    rot = rnd.uniform(-12, 12)
    cx0, cy0 = xc + crack_dx, top + 4
    crack = f"M{cx0:.1f},{cy0:.1f} l2.6,5.5 l-3.2,4.5 l3.6,5.5 l-2.2,4.5"
    body = (f'<g fill="#E58B76" stroke="#B5473A" stroke-width=".6">{"".join(vil)}</g>'
            f'<path d="{d}" fill="url(#{U}-lc)" stroke="#AE3D31" stroke-width="1.4" stroke-linejoin="round"/>'
            f'<path d="{d}" fill="url(#{U}-lcv)"/>'
            f'<ellipse cx="{cx:.1f}" cy="{cy:.1f}" rx="11.5" ry="15.5" transform="rotate({rot:.0f} {cx:.1f} {cy:.1f})" '
            f'fill="url(#{U}-ln)" stroke="#7E231E" stroke-width=".9"/>'
            f'<circle cx="{cx + 2:.1f}" cy="{cy - 4:.1f}" r="3" fill="#6E1C17"/>'
            f'<path d="{crack}" fill="none" stroke="#7A2219" stroke-width="1.3" stroke-linecap="round" stroke-linejoin="round"/>')
    return body, xl, xr


def _lerp(a, b, f):
    return a + (b - a) * f


# ----------------------------------------------------------------------------- the art
TABS = [("Nutrients", "should pass", GREEN), ("Food particles", "should stay out", None),
        ("Microbes", "should stay out", None), ("Medications", "NSAIDs, antibiotics", None),
        ("Stress", "and poor sleep", None)]

# what pours through each gap, top to bottom: (kind, variant)
STREAM = [[("mic", 0), ("food", 0), ("tox", 0), ("mic", 0)],
          [("food", 1), ("mic", 0), ("tox", 0), ("food", 2)],
          [("tox", 0), ("food", 2), ("mic", 0), ("tox", 0)],
          [("food", 0), ("tox", 0), ("mic", 0), ("food", 1)],
          [("mic", 0), ("food", 1), ("tox", 0), ("mic", 0)]]
STREAM_Y = [BT - 13, CT + 30, CT + 74, CT + 116]


def art_barrier(t):
    rnd = random.Random(23)
    tabcol = [c or t["c2"] for _, _, c in TABS]
    o = [defs_svg(),
         f'<rect x="1" y="{FT}" width="{W - 2}" height="{FB - FT}" rx="14" fill="url(#{U}-lumen)"/>',
         f'<g clip-path="url(#{U}-clip)">']
    # lanes: each tab's column, so its items sit clearly under it
    for i, col in enumerate(tabcol):
        x = 6 + i * 150
        o.append(f'<path d="M{x},{TY + 24} V{LANE_B - 12} Q{x},{LANE_B} {x + 12},{LANE_B} H{x + 130} '
                 f'Q{x + 142},{LANE_B} {x + 142},{LANE_B - 12} V{TY + 24} Z" fill="{col}" opacity=".09"/>')
    # tissue under the lining, inflammation glow, blood vessel, basement membrane
    o.append(f'<rect x="0" y="{CT + 12}" width="{W}" height="{BLT - CT}" fill="url(#{U}-tissue)"/>')
    o.append(f'<ellipse cx="540" cy="{(CT + CB) / 2 - 8:.0f}" rx="270" ry="132" fill="url(#{U}-glow)"/>')
    vessel = f"M0,{BLT + 5} C150,{BLT - 5} 300,{BLT + 7} 450,{BLT} S650,{BLT - 4} {W},{BLT + 4}"
    o.append(f'<path d="{vessel} V{FB + 4} H0 Z" fill="url(#{U}-blood)"/>')
    o.append(f'<path d="{vessel}" fill="none" stroke="#E9A09C" stroke-width="3"/>')
    o.append(f'<path d="M0,{CB + 3} H{W}" stroke="#D9A898" stroke-width="2"/>')

    # ---- healthy half: six columnar cells, seams sealed by tight junctions
    for i in range(6):
        o.append(h_villi(HX[i], HX[i + 1], rnd))
    for i in range(6):
        o.append(h_cell(HX[i], HX[i + 1], 7 if i < 3 else (-3 if i % 2 else 3)))
    for x in HX[1:6]:
        o.append(stitches(x, CT + 6))

    # ---- leaky half: swollen, inflamed cells pulled apart into wide, ragged gaps
    tops = [CT + 4, CT + 7, CT + 3, CT + 8, CT + 5, CT + 6]
    bites = [(0.62,), (0.3,), (), (0.7,), (0.25, 0.75), (0.45,)]
    cdx = [-6, 8, 9, -8, 6, 7]
    walls = []
    for k, (xc, top) in enumerate(zip(LX, tops)):
        lw = [SPLIT + 5, SPLIT + 1.5, SPLIT + 1, SPLIT + 1, SPLIT + 1] if k == 0 else None
        body, xl, xr = l_cell(xc, top, rnd, left_wall=lw, bites=bites[k], crack_dx=cdx[k], nuc_dx=rnd.uniform(-3, 3))
        o.append(body)
        walls.append((xl, xr, top))
    o.append(stitches(SPLIT, CT + 15, n=2))   # the healthy | leaky seam: still holding, but only just
    for k in range(5):
        xl = walls[k][1]
        xr = walls[k + 1][0]
        o.append(torn(xl + 1.5, xr - 1.5, max(walls[k][2], walls[k + 1][2]) + 13))

    # inflammation sparks on the damaged tops (on the cell bodies, clear of the gap arrows)
    for x, y, r in [(353, CT + 26, 7), (418, CT + 32, 6.5), (496, CT + 32, 7.5), (596, CT + 26, 7),
                    (655, CT + 34, 6.5), (735, CT + 28, 7)]:
        o.append(spark(x, y, r))

    # ---- arrows: nutrients through the healthy cell bodies, leaks through the gaps
    for x in NUT_X:
        o.append(arrow(x, 128, BLT + 48, GREEN, 5.2, 15))
    for gx in GX:
        o.append(arrow(gx, 136, BLT + 50, LEAK, 6.2, 17))
    for x, (s, c) in zip(NUT_X, [("C", "#E07B24"), ("D", "#2F6DB5"), ("A", "#C2477A")]):
        o.append(token(x, CT + 42, s, c, 11))

    # the stream: what pours through each gap
    for gx, items in zip(GX, STREAM):
        for (kind, v), y in zip(items, STREAM_Y):
            if kind == "mic":
                o.append(microbe(gx, y, 90 + rnd.uniform(-6, 6), 0.8))
            elif kind == "food":
                o.append(food(gx, y, 0.74, rnd.uniform(-30, 30), v))
            else:
                o.append(toxin(gx, y, 6.8, rnd.uniform(0, 30)))

    # ---- lane items, tidy under each tab
    for (x, y, s, c) in [(29, 84, "C", "#E07B24"), (61, 84, "Mg", "#B4652E"), (93, 84, "D", "#2F6DB5"),
                         (125, 84, "Zn", "#264D8C"), (45, 112, "Fe", "#6B3A87"), (77, 112, "B", "#3C9A5F"),
                         (109, 112, "Ca", "#1F8E9A")]:
        o.append(token(x, y, s, c))
    for (x, y, s, r, v) in [(184, 84, 1.0, 10, 0), (227, 82, 0.92, -20, 1), (270, 86, 1.0, 30, 2),
                            (205, 114, 0.9, 50, 2), (250, 114, 0.95, -40, 0)]:
        o.append(food(x, y, s, r, v))
    for (x, y, s, r, v) in [(176, BT - 10, 0.92, 0, 1), (228, BT - 10, 0.88, 20, 0), (279, BT - 10, 0.9, -15, 2)]:
        o.append(food(x, y, s, r, v))   # kept out: resting on the sealed lining
    for (x, y, r) in [(334, 84, 18), (380, 80, -14), (424, 86, 22), (346, 114, -30), (414, 116, 12)]:
        o.append(microbe(x, y, r, 0.95))
    for (x, y, r) in [(482, 84, -22), (528, 80, 14), (573, 86, -8), (503, 114, 32), (566, 116, -26)]:
        o.append(pill(x, y, r, 0.98))
    o.append(pill(509, BT + 5, 6, 0.95))    # a pill resting on an injured cell
    for (x, y, r) in [(634, 82, -8), (678, 80, 10), (722, 84, -6), (656, 112, 8), (700, 114, -10)]:
        o.append(bolt(x, y, 1.0, r))
    o.append(bolt(664, BT - 10, 0.85, 16))   # stress signals striking the seams
    o.append(bolt(744, BT - 10, 0.85, -12))

    # ---- bloodstream: nutrients delivered on the left, leaked items on the right
    dy = BLT - 338   # positions below were laid out for a vessel top at 338
    for (x, y, r) in [(46, 400, 10), (92, 410, -12), (90, 356, -8), (182, 424, 8), (262, 418, -10), (226, 364, 14),
                      (340, 416, 12), (468, 422, 6), (506, 368, -8), (590, 412, -14), (548, 430, -6), (742, 404, -10)]:
        o.append(rbc(x, y + dy, r))
    for (x, y, s, c) in [(148, 392, "D", "#2F6DB5"), (222, 398, "Zn", "#264D8C"), (282, 378, "C", "#E07B24")]:
        o.append(token(x, y + dy, s, c, 11.5))
    for x, y, s, r, v in [(334, 376, 0.75, 20, 1), (384, 428, 0.68, -10, 0), (504, 404, 0.72, -30, 2), (664, 370, 0.7, 40, 0)]:
        o.append(food(x, y + dy, s, r, v))
    for x, y, r in [(428, 410, 25), (662, 414, -20), (706, 430, 8)]:
        o.append(microbe(x, y + dy, r, 0.75))
    for x, y, r in [(414, 370, 0), (574, 374, 10), (626, 428, 20), (734, 366, 5)]:
        o.append(toxin(x, y + dy, 6.5, r))
    o.append(T(16, FB - 13, "BLOODSTREAM", 13, 800, "#FFFFFF", ls=2))
    o.append("</g>")
    o.append(f'<rect x="1" y="{FT}" width="{W - 2}" height="{FB - FT}" rx="14" fill="none" stroke="#C3D5DA" stroke-width="1.4"/>')

    # ---- the five tabs, on top
    for i, ((lab, sub, _), col) in enumerate(zip(TABS, tabcol)):
        x = 6 + i * 150
        o.append(f'<rect x="{x}" y="{TY}" width="142" height="{TH}" rx="7" fill="{col}"/>')
        o.append(f'<path d="M{x + 59},{TY + TH - 1} h24 l-12,11 z" fill="{col}"/>')
        o.append(T(x + 71, TY + 21, lab, 13.5, 800, "#fff", "middle"))
        o.append(T(x + 71, TY + 37, sub, 10.2, 500, "#EAF4F7", "middle"))
    return svg(W, FB + 2, "".join(o), "A healthy gut lining with sealed seams beside a leaky one with gaps that let food, "
               "microbes and toxins into the bloodstream")


# ----------------------------------------------------------------------------- key
def swatch(markup, vb=30):
    h = vb / 2
    return f'<svg viewBox="{-h} {-h} {vb} {vb}" aria-hidden="true">{markup}</svg>'


def key_html():
    tj = (f'<rect x="-13" y="-11" width="12" height="22" rx="3" fill="url(#{U}-hc)" stroke="#D2937E"/>'
          f'<rect x="1" y="-11" width="12" height="22" rx="3" fill="url(#{U}-hc)" stroke="#D2937E"/>'
          + stitches(0, -6, 3, 5.5, 4.6))
    tr = (f'<rect x="-14.5" y="-11" width="9" height="22" rx="3" fill="url(#{U}-lc)" stroke="#AE3D31"/>'
          f'<rect x="5.5" y="-11" width="9" height="22" rx="3" fill="url(#{U}-lc)" stroke="#AE3D31"/>'
          + torn(-5, 5, -6, 3.4))
    infl = (f'<circle r="15" fill="url(#{U}-glow)"/><rect x="-9" y="-12.5" width="18" height="25" rx="7" '
            f'fill="url(#{U}-lc)" stroke="#AE3D31"/>' + spark(-2.6, 1.5, 5.6)
            + '<path d="M4.4,-12.5 l2,4.2 l-2.4,3.4 l2.6,4.2" fill="none" stroke="#7A2219" stroke-width="1.2" '
            'stroke-linecap="round" stroke-linejoin="round"/>')   # a damaged cell: red, glowing, sparked, cracked
    items = [
        (token(0, 0, "C", "#E07B24", 12), "Vitamin, mineral", "C, D, Zn, Mg..."),
        (food(0, 0, 0.95), "Food particle", "not fully digested"),
        (microbe(-8, 6, -34, 0.66), "Microbe", "germs like bacteria"),
        (toxin(0, 0, 9), "Toxin", "made by microbes"),
        (pill(0, 0, -30, 0.85), "Medication", "NSAIDs, antibiotics"),
        (bolt(0, 0, 0.85, 8), "Stress signal", "stress hormones"),
        (arrow(0, -13, 13, GREEN, 4.2, 11), "Absorbed", "through a cell"),
        (arrow(0, -13, 13, LEAK, 4.6, 12), "Leak", "through a gap"),
        (tj, "Tight junction", "seals the seam"),
        (tr, "Torn junction", "seam torn open"),
        (infl, "Inflammation", "red, swollen cells"),
        (rbc(0, 0, -20, 0.95), "Red blood cell", "carries oxygen"),
    ]
    cells = "".join(f'<div>{swatch(sw)}<p><b>{a}</b>{b}</p></div>' for sw, a, b in items)
    return f'<div class="{U}-key"><span class="{U}-kt">Key</span><div class="{U}-kg">{cells}</div></div>'


# ----------------------------------------------------------------------------- front page
# An immune "alert" shield, drawn in kit.icon's 64x64 line style (kit has no shield icon).
SHIELD = '<path d="M32 6 52 13v17c0 13-8.5 22.5-20 27C20.5 52.5 12 43 12 30V13z"/><path d="M32 21v14M32 43v1"/>'


def line_icon(body, size, color="#fff", sw=3.0):
    return (f'<svg class="ic" viewBox="0 0 64 64" style="width:{size};height:{size};color:{color}" fill="none" '
            f'stroke="currentColor" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round" '
            f'aria-hidden="true">{body}</svg>')


OUTCOMES = [(icon("plate", "0.34in", "#fff", 3), "Food reactions",
             "Bloating or other symptoms after foods such as gluten, dairy or soy"),
            (line_icon(SHIELD, "0.34in"), "Immune overload", "Seasonal allergies, skin flare-ups, catching every cold"),
            (icon("battery", "0.34in", "#fff", 3), "Poor absorption", "Running low on vitamin D, B12, iron, magnesium or zinc")]


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
.ipx-key{position:relative;border:1.2px solid #CBD7DB;border-radius:8px;padding:9px 8px 6px;margin-top:9px}
.ipx-kt{position:absolute;top:-7px;left:12px;background:#fff;padding:0 6px;font:800 7.2pt Inter,sans-serif;
  letter-spacing:.16em;text-transform:uppercase;color:var(--deep)}
.ipx-kg{display:grid;grid-template-columns:repeat(6,1fr);gap:6px 4px}
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
    # Bjarnason 1993; "every few days" = about 4 to 5 days, van der Flier and Clevers 2009).
    "intro": ("Your gut lining is a wall just one cell thick, sealed at the seams by <b>tight junctions</b>. A healthy lining "
              "lets nutrients through and keeps out undigested food, microbes and the toxins they make. Poor diet, infections, "
              "alcohol, some medications and long-term stress can loosen those seams. Researchers call this "
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
