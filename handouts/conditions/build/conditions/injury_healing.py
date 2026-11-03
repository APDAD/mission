"""Healing After Injury (ND-MS-601), Pain and Movement Series.  slug "injury-healing".

Self-contained sheet module (no legacy sheets.py / art.py drawing code): the front art, the
front copy and the back data all live here.  Shared helpers come only from svgkit / kit.
Every SVG id starts with "ih-" and every CSS class with "ihl-", so nothing collides with the
other sheets in the all-sheets bundle.  The back page is reached with .sheet.back:has(.ihl-back)
(an empty marker span in this sheet's lifestyle title).

FRONT, top to bottom
  intro (sprain = ligament, strain = muscle or tendon) -> THE THREE PHASES OF HEALING: a whiplash
  inset (head and neck in profile with a side-view cervical spine: C1 front arch, C2 body and dens,
  pedicles, stacked articular pillars, laminae and spinous processes, the spinal cord in the canal,
  the skull base; BACK / FORWARD motion tags; a lens on the front of C6-C7) zooms into one magnified
  ligament with a PARTIAL tear, drawn three times on a time ribbon:
    1 INFLAMMATION  the middle fibres torn, clot, swelling, immune cells leaving a small blood vessel;
                    the outer fibres intact but pulled straight (overstretched)
    2 REPAIR        fibroblasts laying new collagen in a loose criss-cross, new vessel sprouts
    3 REMODEL       new fibres lined up along the pull of movement
  each with "what is happening" and "your part", then a KEY naming every symbol (and the note that
  the times are typical) -> "What can slow healing" icon row -> "Get care right away".
BACK
  lifestyle band (circle style) -> 5 NutriDyn products (Start here: Inflam-Eze Plus; then PRM Resolve,
  Collagen Renew, Muscle Eze, Whey Protein) -> rhythm -> Provider / Pharmacist check (the same lines in both
  editions; only {who} differs).  Product facts live in products.d/injury-healing.json.

SOURCES (each number on the page carries one of these tags in a comment)
  [LEONG20]   Leong NL et al. Tendon and ligament healing and current approaches to tendon and
              ligament regeneration. J Orthop Res 2020;38(1):7-12. PMID 31529731,
              doi:10.1002/jor.24475 (full text PMC7307866, re-read 2026-11-03): tendons and ligaments
              connect "muscle to bone, and bone to bone, respectively"; "The inflammatory stage ...
              begins immediately after acute injury with clot formation"; "Approximately two days
              following injury ... initiate the proliferative stage by recruitment of fibroblasts";
              VEGF "stimulating angiogenesis" in the proliferative phase; "About two weeks following
              injury, remodeling of the injured area begins"; fibres "aligned in the direction of
              stress"; "This process continues for months and years"; sprains and strains form scar
              "which can take years to remodel"; "Collagen synthesis is a highly oxygen dependent process".
  [THOMO15]   Thomopoulos S et al. Mechanisms of tendon injury and repair. J Orthop Res
              2015;33(6):832-839. PMID 25641114, doi:10.1002/jor.22806 (full text PMC4418182): "a short
              inflammatory phase, which lasts about a week, followed by a proliferative phase, which
              lasts a few weeks, followed by a remodeling phase, which lasts many months".
  [NIAMS]     NIH NIAMS, Sprains and Strains: a sprain is a stretch or tear of a ligament (the band
              that connects bones); a strain is an injury to a muscle or tendon.
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
              backward and/or forward jerk of the head, most often in rear-end car crashes; most
              people recover (reassurance matters: the tear drawn here is partial, not a rupture).
  [CDC-TBI]   CDC HEADS UP, concussion danger signs (a headache that gets worse and does not go away,
              repeated vomiting, slurred speech, confusion, unusual drowsiness: call 911 / emergency).
  [AHA-STR]   American Stroke Association, stroke warning signs (F.A.S.T.: face drooping, arm
              weakness, speech difficulty; also sudden trouble seeing, sudden dizziness or loss of
              balance).  Neck trauma can rarely tear a neck artery and cause stroke: Biller J et al.,
              AHA/ASA statement, Stroke 2014;45:3155-3174, PMID 25104849.
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

import kit
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
BONE, BONE_EDGE, DISC, DISC_EDGE = "#FBF4E4", "#A8936F", "#9CC3DA", "#6E9DBA"
CORD, CORD_EDGE = "#F7E8A2", "#C7A947"     # spinal cord (pale yellow)

# ============================================================== geometry
W = 760
IX0, IX1 = 0, 160                 # whiplash inset column
PX0, PW, PG = 172, 190, 9         # first panel x, panel width, gap between panels
PXS = [PX0 + i * (PW + PG) for i in range(3)]
HY = 26                           # phase heading baseline row (badges centred at HY - 4.6)
RY = 46                           # time ribbon centre line
VY0, VH = 60, 166                 # tissue view: top, height
CAP_Y = VY0 + VH + 15             # first caption baseline
CAP_LH = 13.5                     # caption line step (10.8 px text)
PART_Y = CAP_Y + 2 * CAP_LH + 10 + CAP_LH   # "your part" pill top (3 caption lines + "You may feel")
KEY_Y = PART_Y + 44               # key box top
KEY_ROW, KEY_H = 20.5, 87         # key: 4 rows
H = KEY_Y + KEY_H + 1
BAND0, NF, FH, FGAP = 54, 8, 9.4, 1.4       # ligament band top (view coords), fibres, fibre height, gap
BAND1 = BAND0 + NF * FH + (NF - 1) * FGAP
GAPX = PW / 2                     # tear centre (view coords)
TORN = (2, 3, 4, 5)               # a PARTIAL tear: the middle four fibres; rows 0, 1, 6, 7 stay whole [NINDS]
TOR0 = BAND0 + TORN[0] * (FH + FGAP)                 # top of the torn rows
TOR1 = BAND0 + TORN[-1] * (FH + FGAP) + FH           # bottom of the torn rows
TMID, TRY = (TOR0 + TOR1) / 2, (TOR1 - TOR0) / 2 + 3  # torn zone centre and half-height (+ a little)


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
        f'<marker id="ih-pl" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="3.6" markerHeight="3.6" '
        f'orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="{PULL}"/></marker>',
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


def _bud(stem, tips, w=3.4):
    """A new capillary sprouting from a vessel (angiogenesis): one stem that splits into blind-ended tips.
    stem = (start, c1, c2, branch point) of a cubic; tips = [(control, tip)] quadratics from the branch point.
    One path for the outline and one for the lumen, so the branches join cleanly."""
    (x0, y0), (ax, ay), (bx, by), (px, py) = stem
    d = f"M{x0:.1f},{y0:.1f} C{ax:.1f},{ay:.1f} {bx:.1f},{by:.1f} {px:.1f},{py:.1f}"
    d += "".join(f" M{px:.1f},{py:.1f} Q{qx:.1f},{qy:.1f} {tx:.1f},{ty:.1f}" for (qx, qy), (tx, ty) in tips)
    return (f'<path d="{d}" stroke="{VES_EDGE}" stroke-width="{w}" fill="none" stroke-linecap="round" stroke-linejoin="round"/>'
            f'<path d="{d}" stroke="{VES}" stroke-width="{w - 1.5:.1f}" fill="none" stroke-linecap="round" stroke-linejoin="round"/>')


# Panel 2 sprouts (view coords): they leave the floor of the vessel, cross the intact top fibres and end
# inside the torn zone (tips within GAPX +/- 18, near TMID), partly behind the repair cells.  [LEONG20]: VEGF
# "stimulating angiogenesis" in the proliferative phase.
SPROUTS = [
    (((60, 16), (60, 42), (80, 50), (84, 79)), [((80, 87), (78, 94)), ((90, 85), (93, 91))]),
    (((132, 16), (133, 44), (111, 50), (107, 81)), [((102, 89), (101, 97)), ((112, 87), (113, 93))]),
]


def vessel(y0, x0=0, x1=PW):
    """Small blood vessel across the top of a view, with red cells inside."""
    h = 13
    o = [f'<rect x="{x0 - 2}" y="{y0}" width="{x1 - x0 + 4}" height="{h}" fill="{VES}" stroke="{VES_EDGE}" stroke-width=".9"/>',
         f'<rect x="{x0 - 2}" y="{y0 + 2.6}" width="{x1 - x0 + 4}" height="{h - 5.2}" fill="{VES_LUM}"/>']
    for k, x in enumerate(range(x0 + 16, x1 - 8, 46)):
        o.append(red_cell(x + (k % 2) * 7, y0 + h / 2, 0, 0.92))
    return "".join(o)


# ============================================================== one magnified view
def _ends(rnd):
    """Where each fibre broke: staggered ends either side of the tear."""
    return [(GAPX - 15 + rnd.uniform(-9, 4), GAPX + 15 + rnd.uniform(-4, 9)) for _ in range(NF)]


ENDS = _ends(random.Random(5))
# intact outer fibres: pulled straight just after the injury (overstretched), crimp coming back with time
AMP_WHOLE = (0.4, 1.0, 1.6)


def view(i):
    """Phase i (0, 1, 2) of the same ligament, in view coords (0..PW, 0..VH)."""
    rnd = random.Random(31 + i)
    o = [f'<clipPath id="ih-vc{i}"><rect width="{PW}" height="{VH}" rx="10"/></clipPath>',
         f'<g clip-path="url(#ih-vc{i})"><rect width="{PW}" height="{VH}" fill="{BG}"/>']
    if i != 1:                                 # panel 2 draws its vessel over the roots of the new sprouts
        o.append(vessel(10, 0, PW))
    for k in range(NF):
        y = BAND0 + k * (FH + FGAP)
        le, re = ENDS[k]
        if k not in TORN:                      # whole fibre, straightened by the overstretch
            o.append(fiber(-4, PW + 4, y, FH, amp=AMP_WHOLE[i], ph=k * 0.35))
        elif i == 0:
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
        o.append(f'<ellipse cx="{GAPX}" cy="{TMID}" rx="88" ry="60" fill="url(#ih-swell)"/>')
        o.append(f'<path d="{_blob(GAPX, TMID, 19, TRY, rnd, 16, 0.2)}" fill="#D9535B" fill-opacity=".5" '
                 'stroke="#B23A42" stroke-width=".8" stroke-opacity=".75"/>')
        for _ in range(7):   # fibrin strands of the clot
            a = rnd.uniform(0, math.pi)
            cx, cy = GAPX + rnd.uniform(-9, 9), rnd.uniform(TOR0 + 4, TOR1 - 4)
            o.append(f'<path d="M{cx - 8 * math.cos(a):.1f},{cy - 8 * math.sin(a):.1f} L{cx + 8 * math.cos(a):.1f},{cy + 8 * math.sin(a):.1f}" '
                     'stroke="#FBE0E0" stroke-width=".7" opacity=".9"/>')
        tz = TOR1 - TOR0
        for x, y, r in [(GAPX - 6, TOR0 + .08 * tz, 20), (GAPX + 7, TOR0 + .30 * tz, -30), (GAPX - 5, TOR0 + .55 * tz, 60),
                        (GAPX + 6, TOR0 + .78 * tz, 10), (GAPX - 7, TOR0 + .96 * tz, -15)]:
            o.append(red_cell(x, y, r))
        for x, y in [(GAPX + 3, TOR0 + .42 * tz), (GAPX - 9, TOR0 + .70 * tz), (GAPX + 9, TOR0 + .90 * tz),
                     (GAPX - 23, BAND0 - 6), (GAPX + 25, BAND0 - 4), (GAPX - 33, BAND1 + 7), (GAPX + 31, BAND1 + 9)]:
            o.append(immune(x, y))
        # two more immune cells squeezing out of the vessel, heading for the tear
        for x, y, dx in [(GAPX - 44, 31, 7), (GAPX + 43, 31, -7)]:
            o.append(immune(x, y))
            o.append(f'<path d="M{x + dx * .4:.1f},{y + 5.5} L{x + dx:.1f},{y + 12}" stroke="{IMM_EDGE}" stroke-width="1.3" '
                     'marker-end="url(#ih-ap)" fill="none"/>')
    elif i == 1:
        o.append(f'<ellipse cx="{GAPX}" cy="{TMID}" rx="66" ry="44" fill="url(#ih-swell)" opacity=".35"/>')
        # a loose criss-cross of thin new collagen bridging the gap in the torn rows
        segs = []
        for _ in range(30):
            cx, cy = GAPX + rnd.uniform(-22, 22), rnd.uniform(TOR0 + 1, TOR1 - 1)
            a = rnd.uniform(-1.25, 1.25) + (math.pi / 2 if rnd.random() < 0.3 else 0)
            ln = rnd.uniform(9, 17)
            segs.append((cx - ln / 2 * math.cos(a), cy - ln / 2 * math.sin(a), cx + ln / 2 * math.cos(a), cy + ln / 2 * math.sin(a)))
        o.append(f'<clipPath id="ih-nc"><ellipse cx="{GAPX}" cy="{TMID}" rx="33" ry="{TRY}"/></clipPath>')
        o.append('<g clip-path="url(#ih-nc)">' + "".join(new_collagen(*s, w=1.25) for s in segs) + "</g>")
        # new vessel sprouts reach into the repair zone; the vessel they grow from covers their roots
        o.extend(_bud(stem, tips) for stem, tips in SPROUTS)
        o.append(vessel(10, 0, PW))
        # repair cells scattered through the gap, lying roughly along the fibres (within about 30 degrees),
        # with a clear patch of the gold criss-cross left open between them; the immune cell sits off-centre
        tz = TOR1 - TOR0
        for x, y, r in [(GAPX - 14, TOR0 + .13 * tz, 14), (GAPX + 11, TOR0 + .25 * tz, -22), (GAPX - 18, TOR0 + .60 * tz, -9),
                        (GAPX + 16, TOR0 + .74 * tz, 25), (GAPX - 1, TOR0 + .93 * tz, 7)]:
            o.append(fibroblast(x, y, r))
        o.append(immune(GAPX - 24, TOR0 + .36 * tz))
    else:
        # the patch, now made of new fibres lined up with the old ones (green), a few flat fibroblasts
        for k in TORN:
            y = BAND0 + k * (FH + FGAP)
            le, re = ENDS[k]
            a0, a1, f = le - 3.5, re + 3.5, 3.5
            o.append(f'<linearGradient id="ih-gm{k}" gradientUnits="userSpaceOnUse" x1="{a0:.1f}" y1="0" x2="{a1:.1f}" y2="0">'
                     f'<stop offset="0" stop-color="#fff" stop-opacity="0"/><stop offset="{f / (a1 - a0):.3f}" stop-color="#fff"/>'
                     f'<stop offset="{1 - f / (a1 - a0):.3f}" stop-color="#fff"/><stop offset="1" stop-color="#fff" stop-opacity="0"/>'
                     f'</linearGradient><mask id="ih-m{k}"><rect x="{a0:.1f}" y="{y - 4}" width="{a1 - a0:.1f}" height="{FH + 8}" '
                     f'fill="url(#ih-gm{k})"/></mask>')
            o.append(f'<g mask="url(#ih-m{k})">{fiber(a0, a1, y, FH, kind="new")}</g>')
        for x, y in [(GAPX - 9, BAND0 + 3 * (FH + FGAP) - FGAP / 2), (GAPX + 10, BAND0 + 5 * (FH + FGAP) - FGAP / 2)]:
            o.append(fibroblast(x, y, 0, 0.6))
        # the pull of movement, along the fibres
        ay = BAND1 + 13
        o.append(f'<path d="M{22},{ay} H{PW - 22}" stroke="{PULL}" stroke-width="2.6" marker-start="url(#ih-pl)" '
                 'marker-end="url(#ih-pl)" fill="none"/>')
    o.append("</g>")
    o.append(f'<rect x=".6" y=".6" width="{PW - 1.2}" height="{VH - 1.2}" rx="10" fill="none" stroke="#C9D2D9" stroke-width="1.2"/>')
    return "".join(o)


# ============================================================== whiplash inset
# Head and neck in profile, facing right (toward the magnified views).
HEAD_D = ("M23,101 C15,92 8,78 8,60 C8,34 25,12 50,10 C68,9 80,20 82,36 C83,40 83.5,43 82.6,45.8 "
          "C84.6,50 87.4,55 89.6,59.6 C90.4,61.4 89.2,62.8 87,63.2 L84.2,63.8 C84.8,65.4 84.8,66.6 84.2,67.6 "
          "C85.4,68.8 85.2,70.4 83.8,71.2 C84.4,72.8 84,74.4 82.6,75.4 C82.4,77.6 83.6,79.6 83.4,82 "
          "C83,85.6 80.4,87.8 76.4,88.4 C72,89 67.6,89.4 64.2,91.4 C62.4,96 62.6,103 64.6,109 "
          "C66,113 68,116 70,117.6 C76.4,120.6 83,124.6 86,131 L86,136 L3,136 L3,131 C8,124.6 15.6,120.8 22,117.6 "
          "C23.6,112 24.2,106 23,101 Z")
EAR_D = ("M34.6,49.6 C32.4,52.6 32.2,58.6 34.4,62.4 C35.6,64.6 37.6,64.4 38.6,62.6 C39.6,60.8 40.8,60.6 41.8,58.6 "
         "C43.2,55.4 42.6,50.6 40,48.6 C38.2,47.2 35.8,47.8 34.6,49.6 Z")

# ---- cervical spine, side view (figure coords).  Body centres C1..C7 with the normal forward curve
# (lordosis); C1 sits under the skull base at ear-lobe level, C7 at the base of the neck; T1 fades out.
# Proportions from a lateral view (1 unit is about 3 mm): bodies about as deep as they are tall,
# a spinal canal about as deep as a body, short C3-C5 spinous processes, big C2 and longest C7.
SPINE_PTS = [(47.0, 69.5), (49.0, 76.0), (50.2, 82.6), (50.6, 89.2), (50.0, 95.8), (48.6, 102.4), (46.4, 109.0)]
COL_PTS = SPINE_PTS + [(43.8, 115.6)]          # + T1
PIVOT = (46.0, 114.0)          # rotation point for the motion ghost (base of the neck)
PF, PB = -6.0, -9.4            # front and back of the articular pillars (u: toward the front of the neck)
CORD_U, CORD_R = -4.65, 0.75   # spinal cord centre line and half-width, in the canal behind the bodies


def _tangents(pts):
    out = []
    for k in range(len(pts)):
        a, b = pts[max(k - 1, 0)], pts[min(k + 1, len(pts) - 1)]
        dx, dy = b[0] - a[0], b[1] - a[1]
        ln = math.hypot(dx, dy)
        out.append((dx / ln, dy / ln))
    return out


TANS = _tangents(COL_PTS)


def _pt(c, t, u, v):
    """Point u toward the front of the neck and v down the column from c, in the frame of tangent t."""
    return (c[0] + u * t[1] + v * t[0], c[1] - u * t[0] + v * t[1])


def _rot(t):
    return math.degrees(math.atan2(-t[0], t[1]))


def _joint(j):
    """Centre and frame of the level between vertebra j and j + 1 (j = 6 is C7/T1)."""
    a, b = COL_PTS[j], COL_PTS[j + 1]
    tx, ty = TANS[j][0] + TANS[j + 1][0], TANS[j][1] + TANS[j + 1][1]
    ln = math.hypot(tx, ty)
    return ((a[0] + b[0]) / 2, (a[1] + b[1]) / 2), (tx / ln, ty / ln)


def _facet(j, side):
    """Facet joint j as (front, back) points, nudged down (side +1) or up (-1) by half the joint space.
    Cervical facet joints slope down toward the back; C1/C2 (j = 0) is nearly flat."""
    c, t = _joint(j)
    dv = 0.3 if j == 0 else 1.25
    return _pt(c, t, PF, -dv + side * 0.35), _pt(c, t, PB, dv + side * 0.35)


def _poly(pts):
    return "M" + " L".join(f"{x:.2f},{y:.2f}" for x, y in pts) + " Z"


def _smooth(pts, closed=True):
    """Smooth path through points (quadratic midpoints), like _blob."""
    n = len(pts)
    if closed:
        d = [f"M{(pts[0][0] + pts[-1][0]) / 2:.2f},{(pts[0][1] + pts[-1][1]) / 2:.2f}"]
        for i in range(n):
            p, q = pts[i], pts[(i + 1) % n]
            d.append(f"Q{p[0]:.2f},{p[1]:.2f} {(p[0] + q[0]) / 2:.2f},{(p[1] + q[1]) / 2:.2f}")
        return "".join(d) + "Z"
    d = [f"M{pts[0][0]:.2f},{pts[0][1]:.2f}"]
    for i in range(1, n - 1):
        p, q = pts[i], pts[i + 1]
        d.append(f"Q{p[0]:.2f},{p[1]:.2f} {(p[0] + q[0]) / 2:.2f},{(p[1] + q[1]) / 2:.2f}")
    d.append(f"L{pts[-1][0]:.2f},{pts[-1][1]:.2f}")
    return "".join(d)


# local shapes, drawn in a vertebra's own frame (x: toward the front of the neck, y: down the column)
BODY_D = ("M-3.3,-1.7 Q-3.3,-2.5 -2.5,-2.5 Q0,-2.2 2.5,-2.55 Q3.3,-2.55 3.3,-1.7 L3.3,1.75 "
          "Q3.3,2.85 2.3,2.8 L-2.5,2.5 Q-3.3,2.5 -3.3,1.7 Z")
# C2: a taller body with the dens (odontoid peg) rising behind the front arch of C1; its back is in
# line with the back of the body.
C2_D = ("M-3.3,-2.4 L-3.3,1.8 Q-3.3,2.7 -2.3,2.65 L2.0,2.9 Q3.4,3.0 3.4,1.9 L3.3,-1.6 Q3.2,-2.5 2.2,-2.6 "
        "L1.3,-2.7 Q.55,-3.0 .5,-3.9 L.7,-6.2 Q.6,-8.0 -1.3,-8.1 Q-2.9,-8.0 -3.1,-6.4 Z")
PED_D = "M-2.9,-2.2 C-4.1,-1.9 -5.2,-1.9 -6.4,-2.1 L-6.4,-.45 C-5.2,-.75 -4.1,-.75 -2.9,-.5 Z"
C1_POST_D = "M-9.0,-.9 Q-11.4,-.65 -12.9,-.45 Q-14.7,-.6 -14.8,.5 Q-14.7,1.65 -12.9,1.45 Q-11.4,1.05 -9.0,.95 Z"
# lamina + spinous process from the back of the pillar: (root top, root bottom, length, drop, tip height)
SPINOUS = {1: (-2.1, 2.9, 6.4, 2.4, 2.7),       # C2: large and blunt
           2: (-.6, 2.2, 3.0, 1.6, 1.25),        # C3 to C5: short
           3: (-.6, 2.2, 3.0, 1.6, 1.25),
           4: (-.6, 2.2, 3.3, 1.7, 1.3),
           5: (-.5, 2.3, 5.0, 2.1, 1.45),        # C6: longer
           6: (-.4, 2.5, 8.2, 2.5, 1.9)}         # C7: the longest (vertebra prominens)


def _spinous_d(rt, rb, ln, drop, th):
    x0, x1 = PB + .7, PB - ln          # starts inside the pillar so the pillar hides the join
    ty = rt + drop
    return (f"M{x0:.2f},{rt:.2f} Q{(x0 + x1) / 2:.2f},{rt + drop * .42:.2f} {x1:.2f},{ty:.2f} "
            f"Q{x1 - th * .62:.2f},{ty + th / 2:.2f} {x1:.2f},{ty + th:.2f} "
            f"Q{(x0 + x1) / 2:.2f},{(rb + ty + th) / 2 + .3:.2f} {x0:.2f},{rb:.2f} Z")


BONE_ST = f'fill="{BONE}" stroke="{BONE_EDGE}" stroke-width=".55" stroke-linejoin="round"'


def _local(k, d, extra=BONE_ST):
    c, t = COL_PTS[k], TANS[k]
    return f'<path transform="translate({c[0]:.2f},{c[1]:.2f}) rotate({_rot(t):.2f})" d="{d}" {extra}/>'


def _cord_path():
    c0, t0 = COL_PTS[0], TANS[0]
    # The cord starts just above C1, where it leaves the skull through the foramen magnum.  It stops (and
    # fades in, see ih-cdg) below the ear lobe, so it never reads as a cable running into the ear.
    cl = [(c0, t0, -3.5)]
    for k in range(len(COL_PTS)):
        cl.append((COL_PTS[k], TANS[k], 0.0))
        if k < len(COL_PTS) - 1:
            c, t = _joint(k)
            cl.append((c, t, 0.0))
    cl.append((COL_PTS[-1], TANS[-1], 5.0))
    left = [_pt(c, t, CORD_U + CORD_R, v) for c, t, v in cl]
    right = [_pt(c, t, CORD_U - CORD_R, v) for c, t, v in cl]
    return _smooth(left, closed=False) + " L" + _smooth(right[::-1], closed=False)[1:] + " Z"


def _skull_base():
    """The skull base where the column meets the head, at ear-lobe level: the occipital condyle resting on
    the lateral mass of C1 (the C0/C1 joint).  No line runs back along the skull: unlabelled, it read as a
    crease or hairline on the head."""
    c0, t0 = COL_PTS[0], TANS[0]
    f = lambda u, v: "{:.2f},{:.2f}".format(*_pt(c0, t0, u, v))
    return (f'<path d="M{f(-5.5, -3.6)} C{f(-5.8, -2.25)} {f(-9.6, -2.15)} {f(-9.9, -3.4)} Z" fill="{BONE}" '
            f'stroke="{BONE_EDGE}" stroke-width=".5" stroke-linejoin="round"/>')


def _spine():
    """C1 to C7 (and the top of T1), side view: bodies and discs in front, the spinal cord in the canal
    behind them, pedicles crossing to the stacked articular pillars (the facet column), then the laminae
    and spinous processes.  C1 has no body: a small front arch, the lateral mass and a thin back arch."""
    o = []
    # spinal cord, fading out at both ends: clear above y 66 (the ear lobe ends near y 64.5), solid from
    # y 69 (just above C1) down to about y 110, then fading out again toward T1
    o.append('<linearGradient id="ih-cdg" gradientUnits="userSpaceOnUse" x1="0" y1="66" x2="0" y2="123">'
             '<stop offset="0" stop-color="#fff" stop-opacity="0"/><stop offset=".05" stop-color="#fff"/>'
             '<stop offset=".78" stop-color="#fff"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></linearGradient>'
             '<mask id="ih-cdm"><rect x="0" y="50" width="100" height="80" fill="url(#ih-cdg)"/></mask>')
    o.append(f'<path d="{_cord_path()}" mask="url(#ih-cdm)" fill="{CORD}" stroke="{CORD_EDGE}" stroke-width=".45"/>')
    o.append(_skull_base())
    # T1 and everything that belongs to it fades out toward the shoulders
    o.append('<linearGradient id="ih-t1g" gradientUnits="userSpaceOnUse" x1="0" y1="111" x2="0" y2="121">'
             '<stop offset="0" stop-color="#fff" stop-opacity=".9"/><stop offset="1" stop-color="#fff" stop-opacity="0"/>'
             '</linearGradient><mask id="ih-t1m"><rect x="0" y="100" width="100" height="30" fill="url(#ih-t1g)"/></mask>')
    t1 = []
    # discs (none between C1 and C2), tucked under the bodies
    for j in range(1, 7):
        c, t = _joint(j)
        disc = (f'<path transform="translate({c[0]:.2f},{c[1]:.2f}) rotate({_rot(t):.2f})" '
                f'd="M-3.0,-.95 Q0,-1.2 3.15,-.95 L3.2,.95 Q0,1.2 -3.0,.95 Z" fill="{DISC}" stroke="{DISC_EDGE}" stroke-width=".4"/>')
        (t1 if j == 6 else o).append(disc)
    # laminae + spinous processes, and the thin back arch of C1
    o.append(_local(0, C1_POST_D))
    for k, sp in SPINOUS.items():
        o.append(_local(k, _spinous_d(*sp)))
    # pedicles cross the canal (drawn over the cord, under the bodies and pillars)
    for k in range(1, 7):
        o.append(_local(k, PED_D))
    t1.append(_local(7, PED_D))
    # articular pillars: C1's lateral mass under the skull, then C2 to C7 stacked on the facet joints
    c0, t0 = COL_PTS[0], TANS[0]
    f0 = _facet(0, -1)
    a, b, m = _pt(c0, t0, -5.7, -2.5), _pt(c0, t0, -9.7, -2.2), _pt(c0, t0, -7.7, -1.6)
    o.append(f'<path d="M{a[0]:.2f},{a[1]:.2f} Q{m[0]:.2f},{m[1]:.2f} {b[0]:.2f},{b[1]:.2f} L{f0[1][0]:.2f},{f0[1][1]:.2f} '
             f'L{f0[0][0]:.2f},{f0[0][1]:.2f} Z" {BONE_ST}/>')
    for k in range(1, 7):
        top, bot = _facet(k - 1, 1), _facet(k, -1)
        o.append(f'<path d="{_poly([top[0], top[1], bot[1], bot[0]])}" {BONE_ST}/>')
    top = _facet(6, 1)
    c7, t7 = COL_PTS[7], TANS[7]
    t1.append(f'<path d="{_poly([top[0], top[1], _pt(c7, t7, PB, 3.0), _pt(c7, t7, PF, 1.6)])}" {BONE_ST}/>')
    # bodies: C2 with its dens, C3 to C7, and the front arch of C1 in front of the dens
    o.append(_local(1, C2_D, f'fill="{BONE}" stroke="{BONE_EDGE}" stroke-width=".6" stroke-linejoin="round"'))
    for k in range(2, 7):
        o.append(_local(k, BODY_D, f'fill="{BONE}" stroke="{BONE_EDGE}" stroke-width=".6" stroke-linejoin="round"'))
    t1.append(_local(7, BODY_D, f'fill="{BONE}" stroke="{BONE_EDGE}" stroke-width=".6" stroke-linejoin="round"'))
    # C1 front arch, as a midline view shows it: a slim upright oval (about 6 x 9 mm) pressed against the
    # front of the dens.  In C1's frame the dens front runs from about (1.06, 0.65) down to (0.73, 2.93), so
    # the oval is tilted 8 degrees to lie along it, not a round bubble perched on top of the column.
    o.append(f'<ellipse transform="translate({c0[0]:.2f},{c0[1]:.2f}) rotate({_rot(t0):.2f}) translate(1.95,.95) rotate(8)" '
             f'rx=".95" ry="1.6" {BONE_ST}/>')
    o.append('<g mask="url(#ih-t1m)">' + "".join(t1) + "</g>")
    return "".join(o)


def _ghost(deg):
    """Faint dashed outline of the head alone (cut off above the neck), turned about the base of the neck."""
    px, py = PIVOT
    return ('<linearGradient id="ih-ghg" gradientUnits="userSpaceOnUse" x1="0" y1="0" x2="0" y2="96">'
            '<stop offset="0" stop-color="#fff"/><stop offset=".62" stop-color="#fff"/><stop offset="1" stop-color="#fff" stop-opacity="0"/>'
            '</linearGradient><mask id="ih-ghm"><rect x="-20" y="-10" width="130" height="106" fill="url(#ih-ghg)"/></mask>'
            f'<g transform="rotate({deg} {px} {py})"><path d="{HEAD_D}" mask="url(#ih-ghm)" fill="#F6E3D7" fill-opacity=".8" '
            f'stroke="#9AA8B4" stroke-width="1.1" stroke-dasharray="3.2 2.4" stroke-linejoin="round"/></g>')


FIG_S, FIG_X, FIG_Y = 1.42, 19.0, 24.0      # figure scale and placement inside the inset


def _lens():
    """Lens on the front of the C6/C7 disc, where an extension injury stretches the front ligament."""
    c, t = _joint(5)
    x, y = _pt(c, t, 4.1, 0)
    return (FIG_X + x * FIG_S, FIG_Y + y * FIG_S, 8.6)


LENS = _lens()


def _tag(cx, cy, text):
    """Small word tag (dark pill, white caps) naming a motion arrow."""
    fs, ls = 9.7, 0.5
    w = tw(text, fs, 800, ls) + 9
    return (f'<rect x="{cx - w / 2:.1f}" y="{cy - 6.6:.1f}" width="{w:.1f}" height="13.2" rx="6.6" fill="{INK}"/>'
            + T(cx, cy + 3.4, text, fs, 800, "#FFFFFF", "middle", ls=ls))


def _arrow(d):
    return f'<path d="{d}" stroke="{INK}" stroke-width="2.3" fill="none" stroke-linecap="round" marker-end="url(#ih-ar)"/>'


def whiplash_inset():
    top, bot = HY - 18, PART_Y + 34
    cx = (IX0 + IX1) / 2
    o = [f'<rect x="{IX0 + .6}" y="{top}" width="{IX1 - IX0 - 1.2}" height="{bot - top}" rx="10" '
         'fill="#F2F7FB" stroke="#D3DEE8" stroke-width="1.2"/>']
    fig = [f'<g transform="translate({FIG_X},{FIG_Y}) scale({FIG_S})">',
           _ghost(-19),
           f'<path d="{HEAD_D}" fill="url(#ih-skin)" stroke="{SKIN_EDGE}" stroke-width=".9" stroke-linejoin="round"/>',
           # soft jaw line: the lower border of the jaw, in front of the neck bones, out to the chin
           f'<path d="M55.6,86.3 C60.2,87.9 65.8,88.7 72.4,88.2" stroke="{SKIN_EDGE}" stroke-width=".7" '
           'fill="none" opacity=".55"/>',
           f'<path d="M79.2,47.2 C77.6,48.4 77.4,50.2 78.8,51" stroke="{SKIN_EDGE}" stroke-width=".6" fill="none" opacity=".7"/>',
           _spine(),
           # the ear is the outermost layer; the cord ends below the lobe, where it enters the skull
           f'<path d="{EAR_D}" fill="{SKIN_SH}" stroke="{SKIN_EDGE}" stroke-width=".7"/>',
           f'<path d="M36.6,53 C35.4,55.6 35.8,58.8 37.4,60.4" stroke="{SKIN_EDGE}" stroke-width=".6" fill="none"/>',
           "</g>"]
    o += fig
    # motion: the head snaps BACK (the dashed outline), then whips FORWARD [NINDS]
    o.append(_arrow("M50,20 C37,20 25,28 17,44"))
    o.append(_tag(70, 18, "BACK"))
    o.append(_arrow("M143,26 C151,36 155,50 154,66"))
    o.append(_tag(124, 18, "FORWARD"))
    # caption block (WHIPLASH + four lines) centred in the space between the base of the neck and the
    # bottom of the inset: cap height of the 12.5 px title about 9.1, last baseline 16 + 3 x 12.9 below it
    lh = 10.6 * 1.22
    fig_bot, blk = FIG_Y + 136 * FIG_S, 9.1 + 16 + 3 * lh + 2
    ty = fig_bot + (bot - fig_bot - blk) / 2 + 9.1
    o.append(T(cx, ty, "WHIPLASH", 12.5, 800, "#123F60", "middle", ls=1.2))
    o.append(T(cx, ty + 16, ["A crash snaps the head", "back (dashed outline), then", "forward. Neck ligaments",
                             "and muscles overstretch."], 10.6, 600, INK, "middle", lh=1.22))
    return "".join(o)


# ============================================================== headings, ribbon, captions
PHASES = [
    # name, time window.  [THOMO15]: "a short inflammatory phase, which lasts about a week, followed by a
    # proliferative phase, which lasts a few weeks, followed by a remodeling phase, which lasts many months".
    # [LEONG20]: inflammation "begins immediately after acute injury"; "Approximately two days following
    # injury" fibroblasts start the proliferative stage; "About two weeks following injury, remodeling ...
    # begins" and "continues for months and years".  The windows overlap on purpose.
    ("INFLAMMATION", "Days 0 to 7"),
    ("REPAIR", "Day 2 to a few weeks"),
    ("REMODEL", "Week 3 to a year or more"),
]
PCOL = [P1, P2, P3]
PTX = [P1_TX, P2_TX, P3_TX]
CAPS = [
    # [LEONG20]: "The inflammatory stage ... begins immediately after acute injury with clot formation";
    # neutrophils, then macrophages clear the damaged tissue.  The small vessels in the tear bleed, not the
    # collagen fibres themselves.
    ["The tear bleeds and a clot", "forms. Swelling and immune cells", "move in to clean up."],
    # [LEONG20]: fibroblasts lay down scar; VEGF "stimulating angiogenesis" (new vessels)
    ["Repair cells (fibroblasts) lay", "down new collagen in a loose", "criss-cross. New vessels sprout."],
    # [LEONG20]: fibres "aligned in the direction of stress"; "continues for months and years"
    ["Steady pull lines the new", "fibers up, so the patch grows", "stronger over many months."],
]
# What the patient may notice in each phase: the classic signs of inflammation (swelling, warmth, pain);
# new repair tissue is still weak [LEONG20]; remodelling scar is stiff but gains strength with load [KHAN09].
FEELS = ["You may feel: swollen, warm, sore", "You may feel: less pain, still weak",
         "You may feel: stiff, but stronger"]
PARTS = [("Protect it.", "Gentle motion as advised."),     # [PEACE20] protect early
         ("Move it gently.", "Easy, pain-free range."),     # [PEACE20] load without making pain worse
         ("Load it.", "Keep up your exercises.")]          # [KHAN09] load drives remodelling


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
        o.append(T(x, CAP_Y, CAPS[i], 10.8, 600, INK, lh=CAP_LH / 10.8))
        o.append(T(x, CAP_Y + 3 * CAP_LH + 1, FEELS[i], 10.4, 600, PTX[i], italic=True))
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
def _key_bone():
    """Swatch: one side-view vertebra (body, pedicle, pillar, short spinous process) over its disc."""
    sp = _spinous_d(*SPINOUS[2])
    pil = _poly([(PF, -4.2), (PB, -1.7), (PB, 4.2), (PF, 1.7)])
    return (f'<g transform="translate(7.3,-.3) scale(1.6)">'
            f'<path d="M-3.0,2.0 Q0,1.75 3.15,2.0 L3.2,3.9 Q0,4.15 -3.0,3.9 Z" fill="{DISC}" stroke="{DISC_EDGE}" stroke-width=".4"/>'
            f'<path d="{sp}" {BONE_ST}/><path d="{PED_D}" {BONE_ST}/><path d="{pil}" {BONE_ST}/>'
            f'<path d="{BODY_D}" transform="translate(0,-.6)" fill="{BONE}" stroke="{BONE_EDGE}" stroke-width=".6"/></g>')


def _key_items():
    fib = (f'<g transform="translate(-12,-5)">{fiber(0, 24, 1, 8, amp=1.2, lam=14)}</g>')
    swell = (f'<ellipse rx="12" ry="8" fill="url(#ih-swell)"/><ellipse rx="12" ry="8" fill="none" stroke="{SWELL}" '
             'stroke-width=".8" stroke-dasharray="2 1.6" opacity=".7"/>')
    clot = (f'<path d="{_blob(0, 0, 11, 7.5, random.Random(3), 12, 0.18)}" fill="#D9535B" fill-opacity=".5" stroke="#B23A42" '
            'stroke-width=".8" stroke-opacity=".75"/><path d="M-6,-3 L5,4 M-4,4 L6,-3" stroke="#FBE0E0" stroke-width=".7"/>'
            + red_cell(1, 0, 20, 0.8))
    # a vessel with one new sprout branching off it, as in panel 2
    ves = (_bud(((-3, -3), (-3, 1), (-1, 2.5), (0, 4)), [((-1, 6), (-3.5, 8)), ((2, 5.5), (5, 7))], 2.8)
           + f'<rect x="-13" y="-8.5" width="26" height="9" rx="2" fill="{VES}" stroke="{VES_EDGE}" stroke-width=".8"/>'
           f'<rect x="-13" y="-6.6" width="26" height="5.2" fill="{VES_LUM}"/>')
    newc = ('<g>' + new_collagen(-11, 5, 9, -6) + new_collagen(-10, -5, 11, 4) + new_collagen(-3, -7, 2, 7) + '</g>')
    grn = (f'<g transform="translate(-12,-4)">{fiber(0, 24, 0, 8, amp=0.8, lam=14, kind="new")}</g>')
    pull = (f'<path d="M-12,0 H12" stroke="{PULL}" stroke-width="2.4" marker-start="url(#ih-pl)" marker-end="url(#ih-pl)"/>')
    cord = (f'<path d="M-12,-2.3 Q0,-3.1 12,-2.3 L12,2.3 Q0,1.5 -12,2.3 Z" fill="{CORD}" stroke="{CORD_EDGE}" stroke-width=".6"/>')
    lens = ('<path d="M3,-5 L13,-9 M3,5 L13,9" stroke="#6F7A82" stroke-width="1"/>'
            '<circle cx="-2" r="6.5" fill="#FFFFFF" stroke="#2F3A42" stroke-width="1.4"/>')
    return [(fib, "Healthy ligament fibers"), (swell, "Swelling (inflammation)"), (clot, "Blood clot"),
            (ves, "Blood vessel, new sprouts"),
            (red_cell(0, 0, 0, 1.15), "Red blood cell"), (immune(0, 0), "Immune cell"),
            (fibroblast(0, 0, -20, 0.85), "Fibroblast (repair cell)"), (newc, "New collagen"),
            (grn, "Lined-up new fibers"), (pull, "Pull of movement"), (_key_bone(), "Neck bones and disc"),
            (cord, "Spinal cord"), (lens, "Magnified spot")]


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
        cy = y + 13 + r * KEY_ROW
        o.append(f'<g transform="translate({cx + sw_w / 2:.1f},{cy:.1f})">{sw}</g>')
        o.append(T(round(cx + sw_w + gap, 1), cy + 3.9, lab, 11, 600, INK))
    # the last row's free cells carry the note on the time ribbon ([LEONG20]: sprains and strains can
    # take years to remodel; bigger injuries and surgical repairs follow the same phases on a longer clock)
    r, c = divmod(len(items), cols)
    o.append(T(round(start + c * col_w + 4, 1), y + 13 + r * KEY_ROW + 3.7,
               "Times on the ribbon are typical. Bigger injuries and surgery take longer.", 10.5, 500, "#4F5A61",
               italic=True))
    return "".join(o)


def art_phases():
    body = [ih_defs(), whiplash_inset(), zoom(), headings()]
    for i in range(3):
        body.append(f'<g transform="translate({PXS[i]},{VY0})">{view(i)}</g>')
    body.append(captions())
    body.append(key_box(KEY_Y))
    return svg(W, H, "".join(body),
               "Whiplash snaps the head back, then forward, and overstretches the soft tissue of the neck. A magnified "
               "ligament with a partial tear heals in three overlapping phases: inflammation with a clot, swelling and "
               "immune cells; repair, with fibroblasts laying new collagen in a criss-cross and new vessels sprouting; "
               "and remodelling, where steady pull lines the new fibers up.")


# ============================================================== front page blocks
# This sheet's own icons (64 x 64 grid, stroked like kit.icon).
IC_COUCH = ('<path d="M13 30v-6a6 6 0 0 1 6-6h26a6 6 0 0 1 6 6v6"/>'
            '<path d="M7 35a5 5 0 0 1 10 0v4h30v-4a5 5 0 0 1 10 0v12H7z"/><path d="M11 47v6M53 47v6"/>'
            '<path d="M27 11h6l-6 6h6M37 5h5l-5 5h5"/>')                       # couch with "zz": too much rest
# Too much, too soon: a heavy dumbbell rushing in (speed lines), not a rising "progress" chart.
IC_RUSH = ('<path d="M3 23h11M1 32h13M3 41h11"/>'
           '<rect x="20" y="22.5" width="6" height="19" rx="2"/><rect x="26" y="15" width="8" height="34" rx="2.5"/>'
           '<path d="M34 32h12"/>'
           '<rect x="46" y="15" width="8" height="34" rx="2.5"/><rect x="54" y="22.5" width="6" height="19" rx="2"/>')
# The row names problems, so these show the thing itself (no "don't" slash): a lit cigarette with its
# smoke, and a glass of wine.
IC_CIG = ('<rect x="4" y="39" width="43" height="9" rx="2"/><path d="M14 39v9"/>'
          '<path d="M47 39h4.5a2 2 0 0 1 2 2v5a2 2 0 0 1-2 2H47" fill="currentColor" fill-opacity=".35"/>'
          '<path d="M50 33c-3.5-3.5 3.5-6 0-10s3.5-6.5 0-10"/><path d="M58 31c-3-3 3-5.5 0-9s3-5.5 0-8.5"/>')
IC_WINE = ('<path d="M20 7h24c0 15-5 24-12 24S20 22 20 7z"/>'
           '<path d="M21.6 16.5c0 7 4 13 10.4 13s10.4-6 10.4-13z" fill="currentColor" fill-opacity=".3" stroke="none"/>'
           '<path d="M21.2 16.5h21.6M32 31v21M22 55c3-2.6 17-2.6 20 0"/>')
# Back-page lifestyle band: an orange slice for vitamin C (kit.ICONS has no citrus).  Registered under a
# sheet prefix, the way other sheets add band icons.
kit.ICONS.setdefault("ih-citrus", '<circle cx="32" cy="32" r="22"/><circle cx="32" cy="32" r="16.5"/>'
                                  '<path d="M32 15.5v33M17.7 23.75l28.6 16.5M17.7 40.25l28.6-16.5"/>')
IC_STRESS = ('<circle cx="32" cy="35" r="21"/><path d="M20 27l8 3.5M44 27l-8 3.5"/>'
             '<circle cx="25" cy="36" r="1.9" fill="currentColor" stroke="none"/>'
             '<circle cx="39" cy="36" r="1.9" fill="currentColor" stroke="none"/>'
             '<path d="M21 47l3.7-3 3.7 3 3.6-3 3.7 3 3.7-3 3.6 3"/>'
             '<path d="M13 8l3 6M32 3v7M51 8l-3 6"/>')               # tense face, gritted teeth, strain lines: stress


def _ic(body, size="0.33in", sw=2.8):
    return (f'<svg class="ic" viewBox="0 0 64 64" style="width:{size};height:{size}" fill="none" stroke="currentColor" '
            f'stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{body}</svg>')


SLOWERS = [  # what can slow healing
    ("cig", "Smoking or<br>nicotine"),            # [GUO10] smoking; nicotine narrows vessels
    ("moon", "Short or<br>poor sleep"),           # [SMITH18] "relatively modest sleep disruption delays wound healing"
    ("egg", "Too little<br>protein"),             # [GUO10] nutrition; Tipton 2015 (PMID 26553492): avoid protein shortfall
    ("bloodsugar", "High blood<br>sugar"),        # [GUO10] diabetes
    ("wine", "Alcohol"),                          # [GUO10] alcohol exposure impairs healing
    ("stress", "Ongoing<br>stress"),              # [GUO10] stress
    ("couch", "Too much<br>rest"),                # [KHAN09] load drives repair; [PEACE20] LOVE: load, exercise
    ("rush", "Too much,<br>too soon"),            # [PEACE20] load without making pain worse
]
OWN_ICONS = {"cig": IC_CIG, "wine": IC_WINE, "couch": IC_COUCH, "rush": IC_RUSH, "stress": IC_STRESS}


def slow_row():
    cells = []
    for ic, lab in SLOWERS:
        art = _ic(OWN_ICONS[ic]) if ic in OWN_ICONS else icon(ic, "0.33in", sw=2.8)
        cells.append(f'<div class="ihl-sf"><span class="ihl-disc">{art}</span><span class="ihl-sl">{lab}</span></div>')
    return f'<div class="ihl-slow">{"".join(cells)}</div>'


def care_box():
    # 911 now: [CDC-VTE] chest pain or trouble breathing; [AHA-STR] stroke signs (neck trauma can, rarely,
    # injure a neck artery); [CDC-TBI] danger signs after a head injury (its "slurred speech" is carried by the
    # stroke line's "trouble speaking"); [AAOS] new weakness or numbness with loss of bladder or bowel control.
    # Stroke line: F.A.S.T. plus sudden trouble seeing and dizziness [AHA-STR]; a sudden, severe headache or
    # neck pain is the earliest warning of a torn neck artery (Biller 2014: headache and neck pain are the most
    # common presenting symptoms of cervical artery dissection) and is on the ASA list ("sudden severe headache").
    now = ["<b>Chest pain</b> or sudden trouble breathing",
           "<b>Signs of stroke:</b> face drooping, arm weakness, trouble speaking or seeing, severe dizziness, "
           "or a sudden, severe headache or neck pain",
           "<b>After a crash or blow to the head:</b> a headache that keeps getting worse, repeated vomiting, "
           "confusion or unusual sleepiness",
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
            '<h2 class="ihl-h ihl-h2">What can slow healing</h2>'
            f'{slow_row()}{care_box()}</div>')


CSS = r"""
.ihl .ihl-art svg{display:block;width:100%;height:auto}
.ihl-h{display:flex;align-items:center;gap:0.1in;font:900 11pt/1.2 Merriweather,Georgia,serif;color:var(--c1);
  letter-spacing:.04em;text-transform:uppercase;margin:0.02in 0 0.06in}
.ihl-h::after{content:"";flex:1;height:2px;border-radius:2px;background:linear-gradient(90deg,var(--soft),rgba(227,238,246,0))}
.ihl .ihl-h2{margin-top:0.11in}
.ihl-slow{display:grid;grid-template-columns:repeat(8,1fr);gap:0 0.04in}
.ihl-sf{display:flex;flex-direction:column;align-items:center;text-align:center}
.ihl-disc{width:0.54in;height:0.54in;border-radius:50%;background:var(--soft);color:var(--c1);display:flex;
  align-items:center;justify-content:center;box-shadow:inset 0 0 0 1.5px rgba(31,94,140,.12)}
.ihl-sl{display:block;font-size:7.8pt;font-weight:600;line-height:1.22;color:#2F373C;margin-top:0.03in}
.ihl-care{margin-top:0.11in;border:1.5px solid #E3B7B2;border-radius:10px;background:#FFFFFF;overflow:hidden}
.ihl-ch{display:flex;align-items:baseline;gap:0.14in;padding:0.06in 0.12in 0.04in}
.ihl-ch b{flex:none;font:900 11pt/1.2 Merriweather,Georgia,serif;color:#A5281E;letter-spacing:.04em;text-transform:uppercase}
.ihl-ch span{font-size:8.2pt;color:#2B3236}
.ihl-cc{display:grid;grid-template-columns:1.14fr .86fr;gap:0.1in;padding:0 0.1in 0.08in}
.ihl-cc>div{border-radius:7px;padding:0.05in 0.1in 0.06in}
.ihl-now{background:#FDF0EE;border-left:4px solid #C0392B}
.ihl-today{background:#FEF6E7;border-left:4px solid #D99A1C}
.ihl-cc h4{margin:0 0 2px;font:800 7.6pt Inter,sans-serif;letter-spacing:.12em;text-transform:uppercase}
.ihl-now h4{color:#A5281E}
.ihl-today h4{color:#8C5F05}
.ihl-cc ul{margin:0;padding:0 0 0 11px}
.ihl-cc li{font-size:7.9pt;line-height:1.3;color:#2B3236;margin:0 0 1px}
.ihl-cc li b{color:#1F2A2E}
.ihl-nw{white-space:nowrap}
/* back page: scoped with :has() to the marker span in this sheet's lifestyle title (the 7 pt fine print and
   the Start here badge come from the shared kit).  Equal-height need headers, with 0.02in more room on top
   so the start column's title clears the badge that straddles the column edge (same inner height, so every
   title stays on one line across the five columns); the "In each serving" rows start on one line. */
.sheet.back:has(.ihl-back) .col .need{height:0.55in;min-height:0.55in;padding-top:0.09in}
.sheet.back:has(.ihl-back) .col .what ul{min-height:4.2em}
.sheet.back:has(.ihl-back) .slot li em{white-space:nowrap}
/* back layout: the same blocks as every sheet, re-placed with a grid so the six-line check panel can run
   full width in two columns; the daily rhythm and the notes box share the row under it. */
.sheet.back:has(.ihl-back) .inner{display:grid;grid-template-columns:1.6fr 1fr;column-gap:0.1in;
  grid-template-rows:auto auto auto auto auto auto 1fr auto}
.sheet.back:has(.ihl-back) .inner>*{grid-column:1/-1}
.sheet.back:has(.ihl-back) .band{grid-row:1}
.sheet.back:has(.ihl-back) .ns-title{grid-row:2}
.sheet.back:has(.ihl-back) .cols{grid-row:3}
.sheet.back:has(.ihl-back) .duo{display:contents}
.sheet.back:has(.ihl-back) .duo>.panel,.sheet.back:has(.ihl-back) .notes{margin-top:0.08in}
.sheet.back:has(.ihl-back) .ns-title{margin-top:0.1in}
.sheet.back:has(.ihl-back) .duo>.panel.rx{grid-row:4;grid-column:1/-1}
.sheet.back:has(.ihl-back) .duo>.panel:not(.rx){grid-row:5;grid-column:1}
.sheet.back:has(.ihl-back) .notes{grid-row:5;grid-column:2}
.sheet.back:has(.ihl-back) .recby{grid-row:6}
.sheet.back:has(.ihl-back) .foot{grid-row:8}
.sheet.back:has(.ihl-back) .panel.rx ul{columns:2;column-gap:0.26in}
.sheet.back:has(.ihl-back) .panel.rx li{break-inside:avoid}
/* the notes box is as tall as the rhythm panel beside it: share that height among the three write-in lines */
.sheet.back:has(.ihl-back) .notes{display:flex;flex-direction:column}
.sheet.back:has(.ihl-back) .notes .ln{flex:1 1 0;height:auto;min-height:0.24in}
"""

SHEET = {
    "slug": "injury-healing", "code": "ND-MS-601", "order": 12, "theme": "msk", "series": "Pain and Movement Series",
    "title": "Healing After Injury", "sub": "Sprains, strains, whiplash and recovery from surgery",
    # [NIAMS] sprain = ligament (bone to bone), strain = muscle or tendon; [LEONG20] tendons connect muscle to
    # bone, ligaments bone to bone.  Three overlapping phases; inflammation is part of repair, not the enemy
    # [LEONG20]; Tipton 2015 (PMID 26553492): "attempting to drastically reduce inflammation may not be ideal
    # for optimal recovery".  Collagen I is the main protein of tendons and ligaments [LEONG20].
    "intro": ("A <b>sprain</b> hurts a ligament, which ties bone to bone. A <b>strain</b> hurts a muscle or the tendon "
              "that ties it to bone. After a sprain, strain, whiplash or surgery, the body heals in three overlapping "
              "phases. <b>Inflammation</b> comes first, and it is part of healing. Then repair cells lay down new "
              "<b>collagen</b>, the rope-like protein of ligaments and tendons. Over months, the patch is "
              "<b>remodeled</b> and grows stronger. How you eat, sleep and move helps each phase."),
    "front": front,
    "css": CSS,
    "back": {
        # the empty span lets this sheet's CSS reach its own back page (see CSS)
        "life_title": 'Lifestyle Recommendations<span class="ihl-back"></span>', "style": "circle",
        "life": [
            # Tipton 2015 (PMID 26553492): avoid protein and energy shortfalls; higher protein while immobilised.
            ("egg", "Protein every meal", "Fish, eggs, chicken or beans, a palm-size portion."),
            # NIH ODS vitamin C fact sheet: vitamin C is required to make collagen; citrus fruits, red and
            # green peppers, kiwifruit and strawberries are among the best food sources.  Icon: an orange slice.
            ("ih-citrus", "Vitamin C every day", "Oranges, kiwi and peppers help you make collagen."),
            # [SMITH18] short sleep delayed wound healing; AASM/SRS: adults need 7 or more hours.
            ("moon", "Sleep 7 to 9 hours", "Short sleep slows repair. Keep a steady bedtime."),
            # [KHAN09] mechanotherapy; [LEONG20] fibres align "in the direction of stress".
            ("walk", "Move as advised", "Gentle motion early, then exercises that line fibers up."),
            # [GUO10] smoking and alcohol impair healing; [LEONG20] collagen synthesis is oxygen dependent.
            ("smoke", "Skip smoking", "Smoking starves tissue of oxygen. Go easy on alcohol."),
        ],
        # Need headers name what the body needs, not an outcome: 21 CFR 101.93(g) counts damage to a body part
        # (a torn ligament) as disease, and NutriDyn's own standard bars injury-outcome language.
        "cols": [
            {"p": "ih_inflam_eze_plus", "need": "Inflammation balance", "needsub": "ginger, curcumin, boswellia + 3 herbs",
             "start": True, "bullets": ["Supports a healthy inflammatory response", "Supports joint and muscle comfort"],
             "dose": "dose_from_db"},
            {"p": "ih_prm_resolve", "need": "Resolution support", "needsub": "PRMs from fish oil, the body's finish-up signals",
             # PRMs = pro-resolving mediators (label: 18-HEPE, 17-HDHA, 14-HDHA), made from omega-3s to wind
             # inflammation down; glossed in plain words in the needsub.  Framed as a normal body process.
             "bullets": ["Supports the body's natural resolution response", "EPA and DHA omega-3s"],
             "dose": "dose_from_db"},
            {"p": "ih_collagen_renew", "need": "Collagen support", "needsub": "collagen peptides for tendon, ligament, bone",
             # No vitamin C in the formula (blast 2026-10-19-collagen-tendon); NIH ODS: vitamin C is needed to make
             # collagen.  Timing is left to the dose bar and the rhythm (morning), so the sheet gives one instruction.
             "bullets": ["Supports healthy tendons and ligaments", "Pair with a vitamin C food, like an orange"],
             "dose": "dose_from_db"},
            {"p": "ih_muscle_eze", "need": "Muscle relaxation", "needsub": 'magnesium, <span class="ihl-nw">L-theanine</span>, '
             'passion flower',
             # NutriDyn's own language (blast 2026-09-22-muscle-guarding): "Helps relax muscle tissue, supports calmness".
             "bullets": ["Helps relax muscle tissue", "Supports calmness at bedtime"], "dose": "dose_from_db"},
            # Protein backs the front page's "Too little protein" and the band's "Protein every meal": Tipton 2015
            # (PMID 26553492) advises avoiding protein shortfall during injury recovery, and higher protein
            # while a limb is immobilised.  The claim is the bottle's own ("Supports Lean Body Mass"); "repair"
            # is avoided so the column never reads as healing the injury.  This column replaced Nerve Eze
            # (polish round 1): its photo is a soft thumbnail enlargement, its facts single-source, its page
            # unverified, and "nerve function" sat opposite the front's numbness red flag.
            {"p": "ih_whey_protein", "need": "Protein support", "needsub": "grass-fed whey isolate, a complete protein",
             "bullets": ["Supports lean muscle while you move less", "An easy way to get protein at a meal"],
             "dose": "dose_from_db"},
        ],
        # One list for both editions; only {who} changes ("your provider" / "your pharmacist").
        # Bleeding: willow bark contains salicin (MedlinePlus Willow bark; NCCIH); ginger and turmeric/curcumin may
        # slow clotting (MedlinePlus); devil's claw has warfarin interaction reports (MedlinePlus); omega-3s and
        # warfarin (NIH ODS).  Aspirin allergy: avoid willow bark (MedlinePlus).  Surgery: the American Society of
        # Anesthesiologists asks patients to stop herbal supplements 2 weeks before surgery; after surgery the
        # same bleeding cautions apply to a fresh wound and to clot-prevention medicines, so the line asks the
        # surgeon when to start.  Drowsiness: Muscle Eze label "may cause drowsiness"; hops can cause sleepiness
        # with sedatives (MedlinePlus Hops).  Diabetes: ginger and turmeric might lower blood sugar, and with
        # diabetes medicines it might drop too low (MedlinePlus Ginger and Turmeric, interactions with
        # antidiabetes drugs).  Calcium and magnesium bind tetracycline and quinolone antibiotics and reduce
        # levothyroxine absorption (NIH ODS magnesium and calcium fact sheets).  Kidney disease: magnesium builds
        # up when the kidneys are weak (NIH ODS magnesium), willow bark may harm weak kidneys (MedlinePlus), and
        # protein intake is often limited in kidney disease (NIDDK).  Stomach ulcers: devil's claw and willow bark
        # (MedlinePlus).  Gallstones: turmeric and devil's claw (MedlinePlus).  Labels: "If pregnant, nursing..."
        # (all); Muscle Eze "Adults take..."; willow bark (a salicylate source) is not advised for children
        # (Reye's syndrome, MedlinePlus); PRM Resolve "Contains: Fish (anchovy, sardine, squid, and mackerel)"
        # (squid is a mollusk, so shellfish); Whey Protein is a milk protein (products DB: "dairy-based").
        "rx": [
            "<b>Blood thinner (warfarin, apixaban, clopidogrel), aspirin, or NSAIDs like ibuprofen or naproxen?</b> "
            "White willow (contains salicin), ginger, curcumin, devil's claw and fish oil may add to bleeding risk. "
            "Ask {who} and your prescriber.",
            '<b>Allergic to aspirin?</b> Skip <span class="ihl-nw">Inflam-Eze Plus</span>: white willow contains salicin, '
            'a natural relative of aspirin.',
            "<b>Surgery coming up, or just had one?</b> Tell your surgeon about every supplement and ask when to start. "
            "Many ask you to stop herbs and fish oil 2 weeks before surgery.",
            '<b>Muscle relaxers, opioids or sleep aids?</b> <span class="ihl-nw">Muscle Eze</span> and the hops in '
            '<span class="ihl-nw">Inflam-Eze Plus</span> may add drowsiness. <b>Diabetes medicine?</b> The ginger and '
            'curcumin in <span class="ihl-nw">Inflam-Eze Plus</span> may lower blood sugar; ask {who} about checking it.',
            '<b>Antibiotics or thyroid medicine?</b> The calcium and magnesium in <span class="ihl-nw">Muscle Eze</span> '
            'can block some of them. Ask {who} how to space them.',
            "<b>Pregnant, nursing, under 18, allergic to fish, shellfish or milk, or have kidney disease, stomach "
            "ulcers or gallstones?</b> Ask {who} first.",
        ],
    },
}
