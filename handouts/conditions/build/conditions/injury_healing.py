"""Healing After Injury (ND-MS-601), Pain and Movement Series.  slug "injury-healing".

Self-contained sheet module (no legacy sheets.py / art.py drawing code): the front art, the
front copy and the back data all live here.  Shared helpers come only from svgkit / kit.
Every SVG id starts with "ih-" and every CSS class with "ihl-", so nothing collides with the
other sheets in the all-sheets bundle.

FRONT, top to bottom
  intro -> THE THREE PHASES OF HEALING: a whiplash inset (head and neck in profile with the
  cervical spine, the back-then-forward motion, a lens on the overstretched front of the neck)
  zooms into one magnified ligament drawn three times on a time ribbon:
    1 INFLAMMATION  torn fibres, clot, swelling, immune cells leaving a small blood vessel
    2 REPAIR        fibroblasts laying new collagen in a loose criss-cross, new vessel sprouts
    3 REMODEL       new fibres lined up along the pull of movement
  each with "what is happening" and "your part", then a KEY naming every symbol ->
  "What can slow healing" icon row -> "Get care right away" (911 now / call today).
BACK
  lifestyle band (circle style) -> 5 NutriDyn products (Start here: Inflam-Eze Plus) ->
  rhythm -> Provider / Pharmacist check.  Product facts live in products.d/injury-healing.json.

SOURCES (each number on the page carries one of these tags in a comment)
  [LEONG20]   Leong NL et al. Tendon and ligament healing and current approaches to tendon and
              ligament regeneration. J Orthop Res 2020;38(1):7-12. PMID 31529731,
              doi:10.1002/jor.24475 (full text read, PMC7307866): three overlapping stages;
              clot + neutrophils + macrophages first; fibroblasts recruited from about day 2;
              remodelling from about 2 weeks, fibres "aligned in the direction of stress",
              type III -> type I collagen, "continues for months and years"; healed tissue
              "lacks the native biomechanical ... properties"; sprains and strains form scar
              "which can take years to remodel"; collagen synthesis is oxygen dependent.
  [THOMO15]   Thomopoulos S et al. Mechanisms of tendon injury and repair. J Orthop Res
              2015;33(6):832-839. PMID 25641114, doi:10.1002/jor.22806 (inflammatory, then
              proliferative and remodelling phases).
  [KHAN09]    Khan KM, Scott A. Mechanotherapy: how physical therapists' prescription of exercise
              promotes tissue repair. Br J Sports Med 2009;43(4):247-252. PMID 19244270,
              doi:10.1136/bjsm.2008.054239 (load drives repair and remodelling).
  [PEACE20]   Dubois B, Esculier JF. Soft-tissue injuries simply need PEACE and LOVE. Br J Sports
              Med 2020;54(2):72-73. PMID 31377722, doi:10.1136/bjsports-2019-101253 (protect early,
              then load and exercise).
  [GUO10]     Guo S, DiPietro LA. Factors affecting wound healing. J Dent Res 2010;89(3):219-229.
              PMID 20139336, doi:10.1177/0022034509359125 (oxygenation, age, stress, diabetes,
              obesity, medications, alcohol, smoking, nutrition).
  [SMITH18]   Smith TJ et al. Impact of sleep restriction on local immune response and skin
              barrier restoration with and without "multinutrient" nutrition intervention.
              J Appl Physiol 2018;124(1):190-200. PMID 28912361 (sleep restriction slowed repair).
  [NINDS]     NIH NINDS, Whiplash information page: a soft-tissue neck injury from a sudden
              backward and/or forward jerk of the head, most often in rear-end car crashes.
  [CDC-TBI]   CDC HEADS UP, concussion danger signs (worsening headache, repeated vomiting,
              slurred speech, confusion, unusual drowsiness: call 911 / emergency department).
  [CDC-VTE]   CDC, Venous thromboembolism (blood clots) signs: leg swelling or pain (call your
              provider as soon as possible); chest pain or trouble breathing (get help now).
  [CDC-SSI]   CDC, Surgical site infection FAQ: redness and pain around the cut, cloudy
              drainage, fever.
  [AAOS]      AAOS OrthoInfo, cauda equina / spinal cord warning signs: new weakness or numbness
              with loss of bladder or bowel control is an emergency.
"""
import math
import os
import random

from kit import icon
from svgkit import T, svg

# ============================================================== text measuring (layout only)
_FACES = {}
_WEIGHTS = {400: "Regular", 500: "Medium", 600: "SemiBold", 700: "Bold", 800: "ExtraBold", 900: "Black"}
_FONT_DIRS = ("/usr/share/fonts/opentype/inter", "/usr/share/fonts/truetype/inter",
              os.path.expanduser("~/Library/Fonts"), "/Library/Fonts")


def _face(name):
    if name not in _FACES:
        from PIL import ImageFont
        for d in _FONT_DIRS:
            for ext in ("otf", "ttf"):
                f = os.path.join(d, f"Inter-{name}.{ext}")
                if os.path.exists(f):
                    _FACES[name] = ImageFont.truetype(f, 100)
                    return _FACES[name]
        raise FileNotFoundError(name)
    return _FACES[name]


def tw(text, size, weight=600, ls=0.0):
    """Advance width of `text` in Inter at `size` px (falls back to a generous guess)."""
    try:
        w = _face(_WEIGHTS[weight]).getlength(text) * size / 100
    except Exception:
        w = len(text) * size * (0.68 if text.isupper() else 0.6)
    return w + ls * len(text)


# ============================================================== palette (every one is in the KEY)
INK = "#23292D"
P1, P1_TX = "#C8343B", "#A8262D"            # phase 1, inflammation (red)
P2, P2_TX = "#D99A1C", "#8C5F05"            # phase 2, repair (gold)
P3, P3_TX = "#2F8F5B", "#1E6B42"            # phase 3, remodel (green)
FIB, FIB_EDGE = "#EBDDC6", "#B49C78"     # healthy collagen fibres (ivory)
NEW, NEW_EDGE = "#E2A82E", "#B57C0A"        # new collagen (gold criss-cross)
GRN, GRN_EDGE = "#3E9B66", "#1E6B42"     # remodelled fibres (green)
FB, FB_EDGE, FB_NUC = "#F2C14E", "#A8740C", "#7E5304"       # fibroblast (gold spindle cell)
IMM, IMM_EDGE = "#7A4FB8", "#4A2C80"     # immune cell (purple dot)
RBC, RBC_EDGE = "#C9343C", "#8E1D25"        # red blood cell
VES, VES_EDGE, VES_LUM = "#F1B9B4", "#D07C78", "#FBE6E2"    # small blood vessel
SWELL = "#E44E58"                           # swelling / inflammation haze
PULL = "#1F5E8C"                            # pull of movement (theme blue)
BG = "#FFF9F3"                              # loose tissue around the ligament
SKIN, SKIN_EDGE, SKIN_SH = "#F6DCCB", "#C99782", "#EFC9B4"
BONE, BONE_EDGE, DISC = "#FBF4E4", "#A8936F", "#9CC3DA"

# ============================================================== geometry
W, H = 760, 410
IX0, IX1 = 0, 160                 # whiplash inset column
PX0, PW, PG = 172, 190, 9         # first panel x, panel width, gap between panels
PXS = [PX0 + i * (PW + PG) for i in range(3)]
HY = 30                           # phase heading baseline row (badges centred at HY - 4)
RY = 50                           # time ribbon centre line
VY0, VH = 64, 176                 # tissue view: top, height
CAP_Y = VY0 + VH + 15             # first caption baseline
PART_Y = CAP_Y + 37               # "your part" pill top
KEY_Y, KEY_H = PART_Y + 44, 72    # key box (3 rows)
BAND0, NF, FH, FGAP = 56, 8, 9.4, 1.4       # ligament band top (view coords), fibres, fibre height, gap
BAND1 = BAND0 + NF * FH + (NF - 1) * FGAP
GAPX = PW / 2                     # tear centre (view coords)
SC = (BAND1 - BAND0) / 72.4        # detail offsets below were laid out on a 72.4-unit band


def ih_defs():
    g = [
        '<linearGradient id="ih-fib" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FCF8F0"/>'
        f'<stop offset=".55" stop-color="{FIB}"/><stop offset="1" stop-color="#DCC8A8"/></linearGradient>',
        '<linearGradient id="ih-grn" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#A9DEBE"/>'
        f'<stop offset=".5" stop-color="{GRN}"/><stop offset="1" stop-color="#2A7E50"/></linearGradient>',
        '<radialGradient id="ih-imm" cx=".36" cy=".32" r=".75"><stop offset="0" stop-color="#D9C9F5"/>'
        f'<stop offset=".5" stop-color="{IMM}"/><stop offset="1" stop-color="#55339A"/></radialGradient>',
        '<linearGradient id="ih-fb" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FCE3A2"/>'
        f'<stop offset="1" stop-color="{FB}"/></linearGradient>',
        f'<radialGradient id="ih-swell" cx=".5" cy=".5" r=".5"><stop offset="0" stop-color="{SWELL}" stop-opacity=".5"/>'
        f'<stop offset=".6" stop-color="{SWELL}" stop-opacity=".22"/><stop offset="1" stop-color="{SWELL}" stop-opacity="0"/></radialGradient>',
        '<radialGradient id="ih-rbc" cx=".4" cy=".35" r=".75"><stop offset="0" stop-color="#E66A70"/>'
        f'<stop offset="1" stop-color="{RBC}"/></radialGradient>',
        f'<linearGradient id="ih-rib" x1="{PXS[0]}" y1="0" x2="{PXS[2] + PW}" y2="0" gradientUnits="userSpaceOnUse">'
        f'<stop offset="0" stop-color="{P1}"/><stop offset=".26" stop-color="{P1}"/><stop offset=".40" stop-color="{P2}"/>'
        f'<stop offset=".60" stop-color="{P2}"/><stop offset=".74" stop-color="{P3}"/><stop offset="1" stop-color="{P3}"/></linearGradient>',
        f'<linearGradient id="ih-skin" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#FBE8DC"/>'
        f'<stop offset="1" stop-color="{SKIN}"/></linearGradient>',
        f'<marker id="ih-ar" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="4.4" markerHeight="4.4" orient="auto-start-reverse">'
        f'<path d="M0,0 L10,5 L0,10 z" fill="{INK}"/></marker>',
        f'<marker id="ih-ap" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="4" markerHeight="4" orient="auto-start-reverse">'
        f'<path d="M0,0 L10,5 L0,10 z" fill="{IMM_EDGE}"/></marker>',
    ]
    return "<defs>" + "".join(g) + "</defs>"


# ============================================================== little parts (also the KEY swatches)
def immune(x, y, r=4.3):
    return (f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="url(#ih-imm)" stroke="{IMM_EDGE}" stroke-width=".8"/>')


def red_cell(x, y, rot=0, s=1.0):
    return (f'<g transform="translate({x:.1f},{y:.1f}) rotate({rot:.0f}) scale({s})">'
            f'<ellipse rx="5" ry="3.4" fill="url(#ih-rbc)" stroke="{RBC_EDGE}" stroke-width=".6"/>'
            f'<ellipse rx="2.3" ry="1.3" fill="none" stroke="{RBC_EDGE}" stroke-width=".9" opacity=".7"/></g>')


def fibroblast(x, y, rot=0, s=1.0):
    """Gold spindle-shaped repair cell with a dark nucleus and thin tapering ends."""
    return (f'<g transform="translate({x:.1f},{y:.1f}) rotate({rot:.0f}) scale({s})">'
            f'<path d="M-13,0 C-9,-.6 -7,-3.6 0,-3.8 C7,-3.6 9,-.6 13,0 C9,.6 7,3.6 0,3.8 C-7,3.6 -9,.6 -13,0 Z" '
            f'fill="url(#ih-fb)" stroke="{FB_EDGE}" stroke-width=".8" stroke-linejoin="round"/>'
            f'<ellipse rx="3.6" ry="2" fill="{FB_NUC}"/><ellipse cx="-1" cy="-.6" rx="1.2" ry=".6" fill="#B8862A"/></g>')


def new_collagen(x0, y0, x1, y1, w=1.7):
    mx, my = (x0 + x1) / 2, (y0 + y1) / 2
    bend = (x1 - x0) * 0.08
    return (f'<path d="M{x0:.1f},{y0:.1f} Q{mx + bend:.1f},{my - bend:.1f} {x1:.1f},{y1:.1f}" stroke="{NEW_EDGE}" '
            f'stroke-width="{w + 1:.1f}" stroke-linecap="round" fill="none" opacity=".55"/>'
            f'<path d="M{x0:.1f},{y0:.1f} Q{mx + bend:.1f},{my - bend:.1f} {x1:.1f},{y1:.1f}" stroke="{NEW}" '
            f'stroke-width="{w}" stroke-linecap="round" fill="none"/>')


def _wave(x, y, amp, lam, ph):
    return y + amp * math.sin(2 * math.pi * x / lam + ph)


def fiber(x0, x1, y, h, amp=1.6, lam=24, ph=0.0, kind="old", left_end=None, right_end=None, rnd=None):
    """One collagen fibre running from x0 to x1 (view coords) with a wavy crimp.
    left_end / right_end: None (runs off the view), "torn" (jagged, frayed) or "round" (smooth end)."""
    fill, edge = ("url(#ih-fib)", FIB_EDGE) if kind == "old" else ("url(#ih-grn)", GRN_EDGE)
    step = 1.5
    n = max(2, int((x1 - x0) / step))
    xs = [x0 + (x1 - x0) * i / n for i in range(n + 1)]
    top = [(x, _wave(x, y, amp, lam, ph)) for x in xs]
    bot = [(x, _wave(x, y + h, amp, lam, ph)) for x in xs]
    wisps = []

    def torn(xe, yt, yb, d):
        # jagged edge from top to bottom, teeth pointing outward (d = +1 right end, -1 left end)
        pts, k = [], 5
        for i in range(1, k):
            yy = yt + (yb - yt) * i / k
            off = (rnd.uniform(1.6, 5.0) if i % 2 else rnd.uniform(-1.4, 0.6)) * d
            pts.append((xe + off, yy))
        for _ in range(2):
            yy = rnd.uniform(yt + 2, yb - 2)
            ln = rnd.uniform(4.5, 8)
            ang = rnd.uniform(-0.4, 0.4)
            wisps.append(f'<path d="M{xe + d:.1f},{yy:.1f} q{d * ln * .5:.1f},{ang * ln * .2:.1f} {d * ln:.1f},{ang * ln:.1f}" '
                         f'stroke="{FIB_EDGE}" stroke-width=".85" fill="none" stroke-linecap="round"/>')
        return pts

    def cap(xe, yt, yb, d):
        # rounded end: a half ellipse bulging outward
        r = (yb - yt) / 2
        return [(xe + d * r * 0.9 * math.sin(math.pi * i / 6), yt + (yb - yt) * (1 - math.cos(math.pi * i / 6)) / 2)
                for i in range(1, 6)]

    pts = list(top)
    if right_end == "torn":
        pts += torn(x1, top[-1][1], bot[-1][1], 1)
    elif right_end == "round":
        pts += cap(x1, top[-1][1], bot[-1][1], 1)
    pts += bot[::-1]
    if left_end == "torn":
        pts += torn(x0, bot[0][1], top[0][1], -1)
    elif left_end == "round":
        pts += [(x, y_) for x, y_ in cap(x0, bot[0][1], top[0][1], -1)]
    d = "M" + " L".join(f"{px:.1f},{py:.1f}" for px, py in pts) + " Z"
    return (f'<path d="{d}" fill="{fill}" stroke="{edge}" stroke-width=".8" stroke-linejoin="round"/>' + "".join(wisps))


def _blob(cx, cy, rx, ry, rnd, n=14, j=0.16):
    """Smooth irregular closed shape (a clot) through jittered points on an ellipse."""
    pts = []
    for i in range(n):
        a = 2 * math.pi * i / n
        k = 1 + rnd.uniform(-j, j)
        pts.append((cx + rx * k * math.cos(a), cy + ry * k * math.sin(a)))
    d = [f"M{(pts[0][0] + pts[-1][0]) / 2:.1f},{(pts[0][1] + pts[-1][1]) / 2:.1f}"]
    for i in range(n):
        p, q = pts[i], pts[(i + 1) % n]
        d.append(f"Q{p[0]:.1f},{p[1]:.1f} {(p[0] + q[0]) / 2:.1f},{(p[1] + q[1]) / 2:.1f}")
    return "".join(d) + "Z"


def vessel(y0, x0=0, x1=PW, loops=()):
    """Small blood vessel across the top of a view, with red cells inside (and new capillary loops)."""
    h = 13
    o = []
    for sx, depth, wd in loops:            # new capillaries: thin loops hanging into the repair zone
        d = (f"M{sx},{y0 + h - 1} C{sx - 2},{y0 + h + depth * .6} {sx + wd * .1},{y0 + h + depth} {sx + wd / 2},{y0 + h + depth} "
             f"C{sx + wd * .9},{y0 + h + depth} {sx + wd + 2},{y0 + h + depth * .6} {sx + wd},{y0 + h - 1}")
        o.append(f'<path d="{d}" stroke="{VES_EDGE}" stroke-width="3.4" fill="none" stroke-linecap="round"/>'
                 f'<path d="{d}" stroke="{VES}" stroke-width="1.9" fill="none" stroke-linecap="round"/>')
    o += [f'<rect x="{x0 - 2}" y="{y0}" width="{x1 - x0 + 4}" height="{h}" fill="{VES}" stroke="{VES_EDGE}" stroke-width=".9"/>',
          f'<rect x="{x0 - 2}" y="{y0 + 2.6}" width="{x1 - x0 + 4}" height="{h - 5.2}" fill="{VES_LUM}"/>']
    for k, x in enumerate(range(x0 + 16, x1 - 8, 46)):
        o.append(red_cell(x + (k % 2) * 7, y0 + h / 2, 0, 0.92))
    return "".join(o)


# ============================================================== one magnified view
def _ends(rnd):
    """Where each fibre broke: staggered ends either side of the tear."""
    return [(GAPX - 15 + rnd.uniform(-9, 4), GAPX + 15 + rnd.uniform(-4, 9)) for _ in range(NF)]


ENDS = _ends(random.Random(5))


def view(i):
    """Phase i (0, 1, 2) of the same ligament, in view coords (0..PW, 0..VH)."""
    rnd = random.Random(31 + i)
    mid = (BAND0 + BAND1) / 2
    o = [f'<clipPath id="ih-vc{i}"><rect width="{PW}" height="{VH}" rx="10"/></clipPath>',
         f'<g clip-path="url(#ih-vc{i})"><rect width="{PW}" height="{VH}" fill="{BG}"/>']
    loops = [(60, 30, 15), (113, 40, 14)] if i == 1 else []
    o.append(vessel(10, 0, PW, loops))
    for k in range(NF):
        y = BAND0 + k * (FH + FGAP)
        le, re = ENDS[k]
        if i == 0:
            o.append(fiber(-4, le, y, FH, right_end="torn", rnd=rnd))
            o.append(fiber(re, PW + 4, y, FH, left_end="torn", rnd=rnd))
        elif i == 1:
            o.append(fiber(-4, le - 1, y, FH, right_end="round"))
            o.append(fiber(re + 1, PW + 4, y, FH, left_end="round"))
        else:
            o.append(fiber(-4, le + 1, y, FH, right_end="round"))
            o.append(fiber(re - 1, PW + 4, y, FH, left_end="round"))
    if i == 0:
        # swelling haze over the hurt area, the clot between the torn ends, red cells and immune cells
        o.append(f'<ellipse cx="{GAPX}" cy="{mid}" rx="92" ry="70" fill="url(#ih-swell)"/>')
        o.append(f'<path d="{_blob(GAPX, mid, 19, (BAND1 - BAND0) / 2 + 3, rnd, 16, 0.2)}" fill="#D9535B" fill-opacity=".5" '
                 'stroke="#B23A42" stroke-width=".8" stroke-opacity=".75"/>')
        for _ in range(10):   # fibrin strands of the clot
            a = rnd.uniform(0, math.pi)
            cx, cy = GAPX + rnd.uniform(-9, 9), rnd.uniform(BAND0 + 4, BAND1 - 4)
            o.append(f'<path d="M{cx - 8 * math.cos(a):.1f},{cy - 8 * math.sin(a):.1f} L{cx + 8 * math.cos(a):.1f},{cy + 8 * math.sin(a):.1f}" '
                     'stroke="#FBE0E0" stroke-width=".7" opacity=".9"/>')
        for x, y, r in [(GAPX - 6, BAND0 + 6 * SC, 20), (GAPX + 7, BAND0 + 16 * SC, -30), (GAPX - 5, BAND0 + 33 * SC, 60),
                        (GAPX + 6, BAND0 + 44 * SC, 10), (GAPX - 7, BAND0 + 57 * SC, -15), (GAPX + 5, BAND0 + 69 * SC, 35)]:
            o.append(red_cell(x, y, r))
        for x, y in [(GAPX + 3, BAND0 + 25 * SC), (GAPX - 9, BAND0 + 46 * SC), (GAPX + 9, BAND0 + 58 * SC), (GAPX - 1, BAND0 + 76 * SC),
                     (GAPX - 23, BAND0 - 6), (GAPX + 25, BAND0 - 4), (GAPX - 33, BAND1 + 7), (GAPX + 31, BAND1 + 9)]:
            o.append(immune(x, y))
        # two more immune cells squeezing out of the vessel, heading for the tear
        for x, y, dx in [(GAPX - 44, 31, 7), (GAPX + 43, 31, -7)]:
            o.append(immune(x, y))
            o.append(f'<path d="M{x + dx * .4:.1f},{y + 5.5} L{x + dx:.1f},{y + 12}" stroke="{IMM_EDGE}" stroke-width="1.3" '
                     'marker-end="url(#ih-ap)" fill="none"/>')
    elif i == 1:
        o.append(f'<ellipse cx="{GAPX}" cy="{mid}" rx="70" ry="54" fill="url(#ih-swell)" opacity=".35"/>')
        # a loose criss-cross of thin new collagen bridging the gap
        segs = []
        for _ in range(44):
            cx, cy = GAPX + rnd.uniform(-22, 22), rnd.uniform(BAND0 + 1 * SC, BAND1 - 1)
            a = rnd.uniform(-1.25, 1.25) + (math.pi / 2 if rnd.random() < 0.3 else 0)
            ln = rnd.uniform(10, 19)
            segs.append((cx - ln / 2 * math.cos(a), cy - ln / 2 * math.sin(a), cx + ln / 2 * math.cos(a), cy + ln / 2 * math.sin(a)))
        o.append(f'<clipPath id="ih-nc"><ellipse cx="{GAPX}" cy="{mid}" rx="33" ry="{(BAND1 - BAND0) / 2 + 3}"/></clipPath>')
        o.append('<g clip-path="url(#ih-nc)">' + "".join(new_collagen(*s, w=1.25) for s in segs) + "</g>")
        for x, y, r in [(GAPX - 12, BAND0 + 9 * SC, 35), (GAPX + 12, BAND0 + 19 * SC, -25), (GAPX - 5, BAND0 + 38 * SC, -62),
                        (GAPX + 13, BAND0 + 52 * SC, 18), (GAPX - 15, BAND0 + 63 * SC, -8), (GAPX + 4, BAND0 + 72 * SC, 40)]:
            o.append(fibroblast(x, y, r))
        for x, y in [(GAPX + 5, BAND0 + 31 * SC), (GAPX - 21, BAND0 + 33 * SC)]:
            o.append(immune(x, y))
    else:
        # the patch, now made of new fibres lined up with the old ones (green), a few flat fibroblasts
        for k in range(NF):
            y = BAND0 + k * (FH + FGAP)
            le, re = ENDS[k]
            a0, a1, f = le - 3.5, re + 3.5, 3.5
            o.append(f'<linearGradient id="ih-gm{k}" gradientUnits="userSpaceOnUse" x1="{a0:.1f}" y1="0" x2="{a1:.1f}" y2="0">'
                     f'<stop offset="0" stop-color="#fff" stop-opacity="0"/><stop offset="{f / (a1 - a0):.3f}" stop-color="#fff"/>'
                     f'<stop offset="{1 - f / (a1 - a0):.3f}" stop-color="#fff"/><stop offset="1" stop-color="#fff" stop-opacity="0"/>'
                     f'</linearGradient><mask id="ih-m{k}"><rect x="{a0:.1f}" y="{y - 4}" width="{a1 - a0:.1f}" height="{FH + 8}" '
                     f'fill="url(#ih-gm{k})"/></mask>')
            o.append(f'<g mask="url(#ih-m{k})">{fiber(a0, a1, y, FH, kind="new")}</g>')
        for x, y in [(GAPX - 9, BAND0 + FH + FGAP / 2), (GAPX + 11, BAND0 + 4 * (FH + FGAP) - FGAP / 2),
                     (GAPX - 3, BAND0 + 6 * (FH + FGAP) - FGAP / 2)]:
            o.append(fibroblast(x, y, 0, 0.6))
        # the pull of movement, along the fibres
        ay = BAND1 + 17
        o.append(f'<path d="M{22},{ay} H{PW - 22}" stroke="{PULL}" stroke-width="2.6" marker-start="url(#ih-pl)" '
                 'marker-end="url(#ih-pl)" fill="none"/>')
    o.append("</g>")
    o.append(f'<rect x=".6" y=".6" width="{PW - 1.2}" height="{VH - 1.2}" rx="10" fill="none" stroke="#C9D2D9" stroke-width="1.2"/>')
    return "".join(o)


# ============================================================== whiplash inset
# Head and neck in profile, facing right (toward the magnified views).  Proportions from a standard
# lateral view: the cervical bodies sit just behind the middle of the neck, C1 at the level of the
# ear lobe, C7 at the base of the neck, with the normal forward (lordotic) curve.
HEAD_D = ("M23,101 C15,92 8,78 8,60 C8,34 25,12 50,10 C68,9 80,20 82,36 C83,40 83.5,43 82.6,45.8 "
          "C84.6,50 87.4,55 89.6,59.6 C90.4,61.4 89.2,62.8 87,63.2 L84.2,63.8 C84.8,65.4 84.8,66.6 84.2,67.6 "
          "C85.4,68.8 85.2,70.4 83.8,71.2 C84.4,72.8 84,74.4 82.6,75.4 C82.4,77.6 83.6,79.6 83.4,82 "
          "C83,85.6 80.4,87.8 76.4,88.4 C72,89 67.6,89.4 64.2,91.4 C62.4,96 62.6,103 64.6,109 "
          "C66,113 68,116 70,117.6 C76.4,120.6 83,124.6 86,131 L86,136 L3,136 L3,131 C8,124.6 15.6,120.8 22,117.6 "
          "C23.6,112 24.2,106 23,101 Z")
EAR_D = ("M34.6,49.6 C32.4,52.6 32.2,58.6 34.4,62.4 C35.6,64.6 37.6,64.4 38.6,62.6 C39.6,60.8 40.8,60.6 41.8,58.6 "
         "C43.2,55.4 42.6,50.6 40,48.6 C38.2,47.2 35.8,47.8 34.6,49.6 Z")
# C1 at the level of the ear lobe, C7 at the base of the neck, gentle forward curve (lordosis).
SPINE_PTS = [(47.0, 71.5), (49.0, 78.0), (50.2, 84.6), (50.6, 91.2), (50.0, 97.8), (48.6, 104.4), (46.4, 111.0)]
PIVOT = (46.0, 114.0)          # rotation point for the motion ghosts (base of the neck)


def _spine():
    """C1 to C7: vertebral bodies (rounded blocks), discs and spinous processes along the curve."""
    o = []
    pts = SPINE_PTS
    angs = []
    for k, (x, y) in enumerate(pts):
        a, b = pts[max(k - 1, 0)], pts[min(k + 1, len(pts) - 1)]
        angs.append(math.degrees(math.atan2(b[1] - a[1], b[0] - a[0])) - 90)
    for k, ((x, y), ang) in enumerate(zip(pts, angs)):
        w, h = (8.6, 4.2) if k == 0 else (10.4, 5.0)
        sp = 9.5 if k == 0 else 11.0 + k * 0.7          # spinous processes lengthen toward C7
        o.append(f'<g transform="translate({x:.1f},{y:.1f}) rotate({ang:.1f})">'
                 f'<path d="M-3.4,-1.2 L{-3.4 - sp:.1f},{1.6 + k * .25:.1f} C{-4.6 - sp:.1f},{2.3 + k * .25:.1f} '
                 f'{-4.2 - sp:.1f},{3.9 + k * .25:.1f} {-2.8 - sp:.1f},{3.7 + k * .25:.1f} L-3.4,2.6 Z" '
                 f'fill="{BONE}" stroke="{BONE_EDGE}" stroke-width=".55" stroke-linejoin="round"/>'
                 f'<rect x="{-w / 2:.1f}" y="{-h / 2:.1f}" width="{w}" height="{h}" rx="1.6" fill="{BONE}" '
                 f'stroke="{BONE_EDGE}" stroke-width=".65"/></g>')
    for k in range(len(pts) - 1):
        (x, y), (nx, ny) = pts[k], pts[k + 1]
        mx, my = (x + nx) / 2, (y + ny) / 2
        ang = (angs[k] + angs[k + 1]) / 2
        o.append(f'<ellipse cx="{mx:.1f}" cy="{my:.1f}" rx="4.7" ry=".95" fill="{DISC}" stroke="#6E9DBA" '
                 f'stroke-width=".35" transform="rotate({ang:.1f} {mx:.1f} {my:.1f})"/>')
    return "".join(o)


def _ghost(deg):
    """Faint dashed outline of the head alone (cut off above the neck), turned about the base of the neck."""
    px, py = PIVOT
    return ('<linearGradient id="ih-ghg" gradientUnits="userSpaceOnUse" x1="0" y1="0" x2="0" y2="96">'
            '<stop offset="0" stop-color="#fff"/><stop offset=".62" stop-color="#fff"/><stop offset="1" stop-color="#fff" stop-opacity="0"/>'
            '</linearGradient><mask id="ih-gm"><rect x="-20" y="-10" width="130" height="106" fill="url(#ih-ghg)"/></mask>'
            f'<g transform="rotate({deg} {px} {py})"><path d="{HEAD_D}" mask="url(#ih-gm)" fill="#F6E3D7" fill-opacity=".8" '
            f'stroke="#9AA8B4" stroke-width="1.1" stroke-dasharray="3.2 2.4" stroke-linejoin="round"/></g>')


FIG_S, FIG_X, FIG_Y = 1.42, 19.0, 28.0      # figure scale and placement inside the inset
LENS = (FIG_X + 54.0 * FIG_S, FIG_Y + 108.6 * FIG_S, 8.6)   # lens: front of the neck, C6 to C7


def _arc_arrow(d, n, nx, ny):
    return (f'<path d="{d}" stroke="{INK}" stroke-width="2.3" fill="none" stroke-linecap="round" marker-end="url(#ih-ar)"/>'
            f'<circle cx="{nx}" cy="{ny}" r="7.6" fill="{INK}"/>' + T(nx, ny + 3.6, str(n), 10, 800, "#FFFFFF", "middle"))


def whiplash_inset():
    top, bot = HY - 18, PART_Y + 34
    cx = (IX0 + IX1) / 2
    o = [f'<rect x="{IX0 + .6}" y="{top}" width="{IX1 - IX0 - 1.2}" height="{bot - top}" rx="10" '
         'fill="#F2F7FB" stroke="#D3DEE8" stroke-width="1.2"/>']
    fig = [f'<g transform="translate({FIG_X},{FIG_Y}) scale({FIG_S})">',
           _ghost(-19),
           f'<path d="{HEAD_D}" fill="url(#ih-skin)" stroke="{SKIN_EDGE}" stroke-width=".9" stroke-linejoin="round"/>',
           f'<path d="{EAR_D}" fill="{SKIN_SH}" stroke="{SKIN_EDGE}" stroke-width=".7"/>',
           f'<path d="M36.6,53 C35.4,55.6 35.8,58.8 37.4,60.4" stroke="{SKIN_EDGE}" stroke-width=".6" fill="none"/>',
           # soft jaw line: from below the ear to the angle, then forward toward the chin
           f'<path d="M43,67 C43.4,74 45,79.4 49,82.6 C55,86.6 64,88.4 72.4,88.2" stroke="{SKIN_EDGE}" stroke-width=".7" '
           'fill="none" opacity=".55"/>',
           f'<path d="M79.2,47.2 C77.6,48.4 77.4,50.2 78.8,51" stroke="{SKIN_EDGE}" stroke-width=".6" fill="none" opacity=".7"/>',
           _spine(), "</g>"]
    o += fig
    # motion: 1 snaps back, 2 whips forward
    o.append(_arc_arrow("M70,26 C52,24 33,34 22,54", 1, 81, 23))
    o.append(_arc_arrow("M141,36 C151,44 156,57 155,73", 2, 131, 25))
    o.append(T(cx, bot - 70, "WHIPLASH", 12.5, 800, "#123F60", "middle", ls=1.2))
    o.append(T(cx, bot - 53, ["A crash snaps the head", "back, then forward.", "Neck ligaments and", "muscles overstretch."],
               10.6, 600, INK, "middle", lh=1.22))
    return "".join(o)


# ============================================================== headings, ribbon, captions
PHASES = [
    # name, time window ([LEONG20]: inflammation starts at once, fibroblasts from about day 2,
    # remodelling from about 2 weeks and for months to years; windows overlap [THOMO15])
    ("INFLAMMATION", "Days 0 to 5"),
    ("REPAIR", "Days 3 to 21"),
    ("REMODEL", "Week 3 to a year or more"),
]
PCOL = [P1, P2, P3]
PTX = [P1_TX, P2_TX, P3_TX]
CAPS = [
    # [LEONG20]: clot first; neutrophils, then macrophages clear the damaged tissue
    ["Torn fibers bleed and clot.", "Inflammation brings swelling", "and immune cells that clean up."],
    ["Repair cells (fibroblasts)", "lay down new collagen, first", "in a loose criss-cross."],
    ["Steady pull lines the new", "fibers up, so the patch grows", "stronger over many months."],
]
PARTS = [("Protect it.", "Gentle motion as advised."),
         ("Move it gently.", "Easy, pain-free range."),
         ("Load it.", "Keep up your exercises.")]


def headings():
    o = []
    for i, (name, when) in enumerate(PHASES):
        cx = PXS[i] + PW / 2
        fs, br, gap = 13.5, 9.5, 6
        w = 2 * br + gap + tw(name, fs, 800, 0.6)
        bx = cx - w / 2 + br
        o.append(f'<circle cx="{bx:.1f}" cy="{HY - 4.6}" r="{br}" fill="{PCOL[i]}"/>'
                 + T(bx, HY - 0.6, str(i + 1), 11.5, 800, "#FFFFFF", "middle")
                 + T(bx + br + gap, HY, name, fs, 800, INK, ls=0.6))
    # ribbon: one arrow of time from the injury on, colours blending where the phases overlap
    x0, x1, h = PXS[0], PXS[2] + PW, 9
    o.append(f'<path d="M{x0 + h / 2},{RY - h / 2} H{x1 - 14} V{RY - 8} L{x1},{RY} L{x1 - 14},{RY + 8} V{RY + h / 2} '
             f'H{x0 + h / 2} A{h / 2},{h / 2} 0 0 1 {x0 + h / 2},{RY - h / 2} Z" fill="url(#ih-rib)"/>')
    for i, (name, when) in enumerate(PHASES):
        cx = PXS[i] + PW / 2
        tw_ = tw(when, 10.5, 700) + 14
        o.append(f'<rect x="{cx - tw_ / 2:.1f}" y="{RY - 8}" width="{tw_:.1f}" height="16" rx="8" fill="#FFFFFF" '
                 f'stroke="{PCOL[i]}" stroke-width="1.3"/>' + T(cx, RY + 3.7, when, 10.5, 700, PTX[i], "middle"))
    return "".join(o)


def captions():
    o = []
    for i in range(3):
        x = PXS[i] + 6
        o.append(T(x, CAP_Y, CAPS[i], 10.8, 600, INK, lh=1.25))
        y = PART_Y
        o.append(f'<rect x="{PXS[i]}" y="{y}" width="{PW}" height="34" rx="8" fill="#FFFFFF" stroke="{PCOL[i]}" stroke-width="1.4"/>'
                 f'<rect x="{PXS[i]}" y="{y}" width="6" height="34" rx="3" fill="{PCOL[i]}"/>')
        o.append(T(PXS[i] + 14, y + 14, "YOUR PART", 9.8, 800, PTX[i], ls=0.9))
        a, b = PARTS[i]
        o.append(T(PXS[i] + 14 + tw("YOUR PART", 9.8, 800, 0.9) + 7, y + 14, a, 11.2, 800, INK))
        o.append(T(PXS[i] + 14, y + 28, b, 10.6, 600, INK))
    return "".join(o)


def zoom():
    """Callout from the lens on the front of the neck into the ligament band of the first view."""
    lx, ly, lr = LENS
    vx, vy1 = PXS[0], VY0 + BAND1 - 6
    # tangent points on the lens toward the two target corners
    def tan(px, py, sgn):
        dx, dy = px - lx, py - ly
        d = math.hypot(dx, dy)
        a = math.atan2(dy, dx) + sgn * math.acos(lr / d)
        return lx + lr * math.cos(a), ly + lr * math.sin(a)
    # under-chin outline points (figure coords): the top edge of the cone must pass below them
    chin = [(FIG_X + x * FIG_S, FIG_Y + y * FIG_S) for x, y in
            ((64.2, 91.4), (70, 89), (76.4, 88.4), (80.4, 87.8), (83, 85.6), (83.4, 82), (84.2, 76))]

    def clear(vy):
        t = tan(vx, vy, -1)
        for px, py in chin:
            if t[0] < px < vx and t[1] + (vy - t[1]) * (px - t[0]) / (vx - t[0]) < py + 3.5:
                return False
        return True
    vy0 = VY0 + BAND0 + 6
    while not clear(vy0):
        vy0 += 1
    t0, t1 = tan(vx, vy0, -1), tan(vx, vy1, 1)
    return (f'<path d="M{t0[0]:.1f},{t0[1]:.1f} L{vx},{vy0} L{vx},{vy1} L{t1[0]:.1f},{t1[1]:.1f} Z" fill="#FFFFFF" fill-opacity=".6"/>'
            f'<path d="M{t0[0]:.1f},{t0[1]:.1f} L{vx},{vy0} M{t1[0]:.1f},{t1[1]:.1f} L{vx},{vy1}" '
            'stroke="#6F7A82" stroke-width="1.1" stroke-opacity=".8" fill="none"/>'
            f'<circle cx="{lx:.1f}" cy="{ly:.1f}" r="{lr}" fill="#FFFFFF" fill-opacity=".3" stroke="#FFFFFF" stroke-width="2.2"/>'
            f'<circle cx="{lx:.1f}" cy="{ly:.1f}" r="{lr + 1.5}" fill="none" stroke="#2F3A42" stroke-width="1" stroke-opacity=".75"/>')


# ============================================================== KEY
def _key_items():
    fib = (f'<g transform="translate(-12,-5)">{fiber(0, 24, 1, 8, amp=1.2, lam=14)}</g>')
    swell = (f'<ellipse rx="12" ry="8" fill="url(#ih-swell)"/><ellipse rx="12" ry="8" fill="none" stroke="{SWELL}" '
             'stroke-width=".8" stroke-dasharray="2 1.6" opacity=".7"/>')
    clot = (f'<path d="{_blob(0, 0, 11, 7.5, random.Random(3), 12, 0.18)}" fill="#D9535B" fill-opacity=".5" stroke="#B23A42" '
            'stroke-width=".8" stroke-opacity=".75"/><path d="M-6,-3 L5,4 M-4,4 L6,-3" stroke="#FBE0E0" stroke-width=".7"/>'
            + red_cell(1, 0, 20, 0.8))
    ves = (f'<rect x="-13" y="-6" width="26" height="12" rx="2" fill="{VES}" stroke="{VES_EDGE}" stroke-width=".8"/>'
           f'<rect x="-13" y="-3.6" width="26" height="7.2" fill="{VES_LUM}"/>')
    newc = ('<g>' + new_collagen(-11, 5, 9, -6) + new_collagen(-10, -5, 11, 4) + new_collagen(-3, -7, 2, 7) + '</g>')
    grn = (f'<g transform="translate(-12,-4)">{fiber(0, 24, 0, 8, amp=0.8, lam=14, kind="new")}</g>')
    pull = (f'<path d="M-12,0 H12" stroke="{PULL}" stroke-width="2.4" marker-start="url(#ih-pl)" marker-end="url(#ih-pl)"/>')
    bone = (f'<path d="M-3,-1 L-13,1.6 C-14.4,2.2 -14.2,3.6 -12.8,3.6 L-3,2.6 Z" fill="{BONE}" stroke="{BONE_EDGE}" stroke-width=".6"/>'
            f'<rect x="-4.2" y="-6.4" width="11" height="5" rx="1.6" fill="{BONE}" stroke="{BONE_EDGE}" stroke-width=".7"/>'
            f'<ellipse cx="1.3" cy="0.2" rx="5.2" ry="1.1" fill="{DISC}" stroke="#6E9DBA" stroke-width=".4"/>'
            f'<rect x="-4.2" y="1.6" width="11" height="5" rx="1.6" fill="{BONE}" stroke="{BONE_EDGE}" stroke-width=".7"/>')
    lens = ('<path d="M3,-5 L13,-9 M3,5 L13,9" stroke="#6F7A82" stroke-width="1"/>'
            '<circle cx="-2" r="6.5" fill="#FFFFFF" stroke="#2F3A42" stroke-width="1.4"/>')
    return [(fib, "Healthy fibers"), (swell, "Swelling (inflammation)"), (clot, "Blood clot"), (ves, "Small blood vessel"),
            (red_cell(0, 0, 0, 1.15), "Red blood cell"), (immune(0, 0), "Immune cell"),
            (fibroblast(0, 0, -20, 0.85), "Fibroblast (repair cell)"), (newc, "New collagen"),
            (grn, "Lined-up new fibers"), (pull, "Pull of movement"), (bone, "Neck bone and disc"), (lens, "Magnified spot")]


def key_box(y):
    items = _key_items()
    x0, x1 = 0.6, W - 0.6
    o = [f'<rect x="{x0}" y="{y}" width="{x1 - x0}" height="{KEY_H}" rx="8" fill="#FFFFFF" stroke="#CFD6DA" stroke-width="1.2"/>',
         T(14, y + KEY_H / 2 + 3.8, "KEY", 11, 800, INK, ls=1.4)]
    cols, sw_w, gap = 4, 28, 7
    start = 56
    col_w = (x1 - 12 - start) / cols
    for n, (sw, lab) in enumerate(items):
        r, c = divmod(n, cols)
        cx = start + c * col_w
        cy = y + 14 + r * 22
        o.append(f'<g transform="translate({cx + sw_w / 2:.1f},{cy:.1f})">{sw}</g>')
        o.append(T(round(cx + sw_w + gap, 1), cy + 3.9, lab, 11, 600, INK))
    return "".join(o)


def art_phases():
    pl = (f'<marker id="ih-pl" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="3.6" markerHeight="3.6" '
          f'orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="{PULL}"/></marker>')
    body = [ih_defs().replace("</defs>", pl + "</defs>"), whiplash_inset(), zoom(), headings()]
    for i in range(3):
        body.append(f'<g transform="translate({PXS[i]},{VY0})">{view(i)}</g>')
    body.append(captions())
    body.append(key_box(KEY_Y))
    return svg(W, H, "".join(body),
               "Whiplash overstretches the soft tissue of the neck. A magnified ligament heals in three overlapping "
               "phases: inflammation with a clot, swelling and immune cells; repair, with fibroblasts laying new "
               "collagen in a criss-cross; and remodelling, where steady pull lines the new fibers up.")


# ============================================================== front page blocks
# This sheet's own icons (64 x 64 grid, stroked like kit.icon).
IC_COUCH = ('<path d="M13 30v-6a6 6 0 0 1 6-6h26a6 6 0 0 1 6 6v6"/>'
            '<path d="M7 35a5 5 0 0 1 10 0v4h30v-4a5 5 0 0 1 10 0v12H7z"/><path d="M11 47v6M53 47v6"/>'
            '<path d="M27 11h6l-6 6h6M37 5h5l-5 5h5"/>')                       # couch with "zz": too much rest
IC_RUSH = ('<path d="M14 26v12M20 20v24M44 20v24M50 26v12M20 32h24"/>'
           '<path d="M8 50h48" stroke-dasharray="2 5"/><path d="M41 9l7-3 3 7"/><path d="M48 6 37 17"/>')  # weights + jump arrow


def _ic(body, size="0.33in", sw=2.8):
    return (f'<svg class="ic" viewBox="0 0 64 64" style="width:{size};height:{size}" fill="none" stroke="currentColor" '
            f'stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{body}</svg>')


SLOWERS = [  # what can slow healing
    ("smoke", "Smoking or<br>nicotine"),          # [GUO10] smoking; nicotine narrows vessels
    ("moon", "Short or<br>poor sleep"),           # [SMITH18] "relatively modest sleep disruption delays wound healing"
    ("egg", "Too little<br>protein"),             # [GUO10] nutrition; Tipton 2015 (PMID 26553492): avoid protein shortfall
    ("bloodsugar", "High blood<br>sugar"),        # [GUO10] diabetes
    ("glass", "Alcohol"),                         # [GUO10] alcohol exposure impairs healing
    ("breath", "Ongoing<br>stress"),              # [GUO10] stress
    ("couch", "Too much<br>rest"),                # [KHAN09] load drives repair; [PEACE20] LOVE: load, exercise
    ("rush", "Too much,<br>too soon"),            # [PEACE20] load without making pain worse
]


def slow_row():
    cells = []
    for ic, lab in SLOWERS:
        art = (_ic(IC_COUCH) if ic == "couch" else _ic(IC_RUSH) if ic == "rush" else icon(ic, "0.33in", sw=2.8))
        cells.append(f'<div class="ihl-sf"><span class="ihl-disc">{art}</span><span class="ihl-sl">{lab}</span></div>')
    return f'<div class="ihl-slow">{"".join(cells)}</div>'


def care_box():
    # 911 now: [CDC-VTE] chest pain or trouble breathing; [CDC-TBI] danger signs after a head injury;
    # [AAOS] new weakness or numbness with loss of bladder or bowel control.
    now = ["<b>Chest pain</b> or sudden trouble breathing",
           "<b>After a crash or blow to the head:</b> a headache that keeps getting worse, repeated vomiting, "
           "slurred speech, confusion or unusual sleepiness",
           "<b>New weakness or numbness</b> with loss of bladder or bowel control"]
    # Same day: [CDC-VTE] leg swelling or pain ("contact your provider as soon as possible");
    # [CDC-SSI] redness, pain, cloudy drainage or fever after surgery; [NINDS]/[AAOS] new nerve signs.
    today = ["<b>Calf pain or swelling</b> in one leg",
             "<b>Fever,</b> or redness, warmth or cloudy drainage at a surgery cut",
             "<b>New numbness or tingling</b> in an arm or leg",
             "<b>Pain or swelling getting worse</b> instead of better, or you cannot put weight on it"]
    li = lambda xs: "".join(f"<li>{x}</li>" for x in xs)
    return ('<div class="ihl-care"><div class="ihl-ch"><b>Get care right away</b><span>Healing should get a little better '
            'week by week. Some signs cannot wait.</span></div><div class="ihl-cc">'
            f'<div class="ihl-now"><h4>Call 911 now</h4><ul>{li(now)}</ul></div>'
            f'<div class="ihl-today"><h4>Call your doctor the same day</h4><ul>{li(today)}</ul></div></div></div>')


def front(t, ed):
    return ('<div class="ihl"><h2 class="ihl-h">The three phases of healing</h2>'
            f'<div class="ihl-art">{art_phases()}</div>'
            '<div class="ihl-h2"><h2 class="ihl-h">What can slow healing</h2>'
            # [LEONG20]: sprains and strains heal with scar that "can take years to remodel"; bigger
            # injuries and surgical repairs follow the same phases on a longer clock.
            '<span>Times above are typical. Bigger injuries and surgery take longer.</span></div>'
            f'{slow_row()}{care_box()}</div>')


CSS = r"""
.ihl .ihl-art svg{display:block;width:100%;height:auto}
.ihl-h{display:flex;align-items:center;gap:0.1in;font:900 11pt/1.2 Merriweather,Georgia,serif;color:var(--c1);
  letter-spacing:.04em;text-transform:uppercase;margin:0.02in 0 0.06in}
.ihl-h::after{content:"";flex:1;height:2px;border-radius:2px;background:linear-gradient(90deg,var(--soft),rgba(227,238,246,0))}
.ihl-h2{display:flex;align-items:baseline;gap:0.16in;margin-top:0.13in}
.ihl-h2 .ihl-h{flex:1;margin:0 0 0.06in}
.ihl-h2>span{flex:none;font-size:7.6pt;font-style:italic;color:#56626A}
.ihl-slow{display:grid;grid-template-columns:repeat(8,1fr);gap:0 0.04in}
.ihl-sf{display:flex;flex-direction:column;align-items:center;text-align:center}
.ihl-disc{width:0.56in;height:0.56in;border-radius:50%;background:var(--soft);color:var(--c1);display:flex;
  align-items:center;justify-content:center;box-shadow:inset 0 0 0 1.5px rgba(31,94,140,.12)}
.ihl-sl{display:block;font-size:7.8pt;font-weight:600;line-height:1.22;color:#2F373C;margin-top:0.03in}
.ihl-care{margin-top:0.13in;border:1.5px solid #E3B7B2;border-radius:10px;background:#FFFFFF;overflow:hidden}
.ihl-ch{display:flex;align-items:baseline;gap:0.14in;padding:0.06in 0.12in 0.04in}
.ihl-ch b{flex:none;font:900 11pt/1.2 Merriweather,Georgia,serif;color:#A5281E;letter-spacing:.04em;text-transform:uppercase}
.ihl-ch span{font-size:8.2pt;color:#2B3236}
.ihl-cc{display:grid;grid-template-columns:1fr 1fr;gap:0.1in;padding:0 0.1in 0.08in}
.ihl-cc>div{border-radius:7px;padding:0.05in 0.1in 0.06in}
.ihl-now{background:#FDF0EE;border-left:4px solid #C0392B}
.ihl-today{background:#FEF6E7;border-left:4px solid #D99A1C}
.ihl-cc h4{margin:0 0 2px;font:800 7.6pt Inter,sans-serif;letter-spacing:.12em;text-transform:uppercase}
.ihl-now h4{color:#A5281E}
.ihl-today h4{color:#8C5F05}
.ihl-cc ul{margin:0;padding:0 0 0 11px}
.ihl-cc li{font-size:7.9pt;line-height:1.3;color:#2B3236;margin:0 0 1px}
.ihl-cc li b{color:#1F2A2E}
"""

SHEET = {
    "slug": "injury-healing", "code": "ND-MS-601", "order": 12, "theme": "msk", "series": "Pain and Movement Series",
    "title": "Healing After Injury", "sub": "Sprains, strains, whiplash and recovery from surgery",
    # Three overlapping phases; inflammation is part of repair, not the enemy [LEONG20]; Tipton 2015
    # (PMID 26553492): "attempting to drastically reduce inflammation may not be ideal for optimal recovery".
    # Collagen I is the main protein of tendons and ligaments (65-80% of dry weight) [LEONG20].
    "intro": ("After a sprain, strain, whiplash or surgery, your body repairs the hurt tissue in three overlapping "
              "phases. <b>Inflammation</b> comes first, and it is part of healing. Next, repair cells lay down new "
              "<b>collagen</b>, the rope-like protein that ligaments and tendons are made of. Then, over months, the "
              "patch is <b>remodeled</b> and grows stronger. How you eat, sleep and move between visits helps each "
              "phase do its job."),
    "front": front,
    "css": CSS,
    "back": {
        "life_title": "Lifestyle Recommendations", "style": "circle",
        "life": [
            # Tipton 2015 (PMID 26553492): avoid protein and energy shortfalls; higher protein while immobilised.
            ("egg", "Protein every meal", "A palm-size portion of fish, eggs, chicken or beans. Repair runs on protein."),
            # NIH ODS vitamin C fact sheet: vitamin C is required to make collagen.
            ("apple", "Color for vitamin C", "Citrus, kiwi, berries and peppers. Your body needs vitamin C to build collagen."),
            # [SMITH18] short sleep delayed wound healing; AASM/SRS: adults need 7 or more hours.
            ("moon", "Sleep 7 to 9 hours", "Short sleep slows repair. Keep a steady bedtime, even on weekends."),
            # [KHAN09] mechanotherapy; [LEONG20] fibres align "in the direction of stress".
            ("walk", "Move as advised", "Gentle motion early, then your exercises. Load lines the new fibers up."),
            # [GUO10] smoking and alcohol impair healing; [LEONG20] collagen synthesis is oxygen dependent.
            ("smoke", "Skip smoking", "Smoking starves healing tissue of oxygen. Keep alcohol low, too."),
        ],
        "cols": [
            {"p": "ih_inflam_eze_plus", "need": "Balance inflammation", "needsub": "ginger, curcumin, boswellia + 3 herbs",
             "start": True, "bullets": ["Supports a healthy inflammatory response", "Supports joint and muscle comfort"],
             "dose": "dose_from_db"},
            {"p": "ih_prm_resolve", "need": "Resolve inflammation", "needsub": "pro-resolving mediators from fish oil",
             "bullets": ["Supports the natural resolution of inflammation", "Omega-3 EPA and DHA for healthy tissue"],
             "dose": "dose_from_db"},
            {"p": "ih_collagen_renew", "need": "Rebuild collagen", "needsub": "collagen peptides for tendon, ligament, bone",
             # Shaw 2017 (PMID 27852613): vitamin C-enriched gelatin 1 hour before exercise doubled a collagen-synthesis
             # marker; Bischof 2024 (PMID 39060741): collagen peptides plus training, 19 RCTs.
             "bullets": ["Building blocks for tendons, ligaments and bone", "Pair with vitamin C, an hour before exercise"],
             "dose": "dose_from_db"},
            {"p": "ih_muscle_eze", "need": "Relax tight muscles", "needsub": "magnesium, L-theanine, passion flower",
             # NutriDyn's own language (blast 2026-09-22-muscle-guarding): "Helps relax muscle tissue, supports calmness".
             "bullets": ["Helps relax muscle tissue", "Supports calmness at bedtime"], "dose": "dose_from_db"},
            {"p": "ih_nerve_eze", "need": "Nerve comfort", "needsub": "PEA + alpha lipoic acid",
             # Vina 2025 (PMID 39798151) and Lang-Illievich 2023 (PMID 36986081) meta-analyses of PEA; PEA is a
             # naturally occurring fatty acid amide.  NutriDyn: "PEA with alpha lipoic acid for healthy nerve function".
             "bullets": ["Supports healthy nerve function", "PEA: a natural fat compound your body makes"],
             "dose": "dose_from_db"},
        ],
        # Willow bark is a salicylate (aspirin relative) and, with ginger and fish oil, may add to bleeding risk
        # (MedlinePlus herb monographs; NIH ODS omega-3 fact sheet).  Surgery: the American Society of
        # Anesthesiologists advises stopping herbal supplements before surgery (about 2 weeks).  Muscle Eze label:
        # "may cause drowsiness".  Alpha lipoic acid can lower blood sugar (MedlinePlus).
        "rx": {
            "practitioner": [
                "<b>Blood thinner, aspirin or NSAIDs?</b> White willow (a salicylate), ginger and fish oil may add "
                "to bleeding risk. Check with {who} first.",
                "<b>Surgery coming up?</b> Your surgeon may want herbs and fish oil stopped 1 to 2 weeks before.",
                "<b>Muscle relaxers, opioids, sleep aids:</b> Muscle Eze may add drowsiness. <b>Diabetes medicine:</b> "
                "alpha lipoic acid can lower blood sugar."],
            "pharmacy": [
                "<b>Warfarin, apixaban, clopidogrel or aspirin?</b> White willow, ginger and fish oil may add to "
                "bleeding risk. Let {who} check your list.",
                "<b>Allergic to aspirin?</b> Skip Inflam-Eze Plus: white willow contains salicin, a natural relative of aspirin.",
                "<b>Muscle relaxers, opioids, sleep aids:</b> Muscle Eze may add drowsiness. <b>Diabetes medicine:</b> "
                "alpha lipoic acid can lower blood sugar."],
        },
    },
}
