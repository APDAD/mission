"""Joint Pain and Osteoarthritis (ND-MS-602), Pain and Movement Series.  slug "joint-pain".

Self-contained sheet module: the front art, the front copy and the back data all live here.
Shared helpers come only from svgkit / kit.  Every SVG id starts with "jp-" and every CSS class
with "jpn-", so nothing collides with other sheets in the all-sheets bundle.  Built 2026-11-03
from the topic brief (scratchpad topics/topic-joint-pain.json, research rank 4 of 10).

FRONT, top to bottom
  intro -> one knee drawn as a front-to-back slice (a coronal section), split down the middle:
  the left half healthy, the right half with osteoarthritis (thin, cracked cartilage with a bald
  patch, bone spurs, a swollen red lining with extra fluid, a narrowed space, a frayed meniscus).
  Each half has a magnified circle of its cartilage (cartilage cells in their collagen mesh) and
  one KEY names every colour and symbol -> how it can feel / get checked promptly -> what raises
  your risk -> know your numbers.
  Anatomy: a right knee seen from the front, so the outer (lateral) side with the fibula is on the
  viewer's left and the inner (medial) side is on the right, where knee OA most often starts.
  Proportions: condyle width : femoral shaft about 2.7 : 1; cartilage about 3% of joint width
  (2 to 3 mm on an 80 mm knee), drawn a little thicker so the change reads; meniscus a wedge about
  twice cartilage height at its rim (Sophia Fox 2009, doi:10.1177/1941738109350438, PMID 23015907).
BACK: lifestyle band, 5 NutriDyn products (label facts in products.d/joint-pain.json, plus the
  shared omega_1000 entry), daily rhythm, an edition-specific check list.

SOURCES (tags used in the comments next to each number or claim)
  [WHO23]     WHO fact sheet "Osteoarthritis", 14 July 2023: 528 million people lived with OA in
              2019 (+113% since 1990); about 73% are older than 55; 60% are female; the knee is the
              most affected joint (365 million), then the hip and the hand.  (who.int is blocked
              from this machine; the figures were confirmed by a web search of the fact sheet.)
  [HUNTER19]  Hunter DJ, Bierma-Zeinstra S. Osteoarthritis. Lancet 2019;393:1745-59. PMID 31034380,
              doi:10.1016/S0140-6736(19)30417-9 (whole-joint disease; clinical diagnosis; core care
              is education, exercise and weight loss).
  [NICE22]    NICE guideline NG226 (2022) rec 1.1.1: diagnose OA clinically, without imaging, in people
              45 or over with activity-related joint pain and no morning stiffness, or stiffness that
              lasts no longer than 30 minutes.  NICE QS87: atypical features (trauma, prolonged
              morning stiffness, rapid worsening, deformity, a hot swollen joint) point to other
              causes such as gout, inflammatory arthritis, infection or cancer.
  [SILVER15]  Silverwood V et al. Osteoarthritis Cartilage 2015;23:507-15. PMID 25447976,
              doi:10.1016/j.joca.2014.11.019 (new knee pain/OA at 50+: overweight OR 1.98, obesity
              2.66, female 1.68, previous knee injury 2.83).
  [WANG20]    Wang X et al. Arthritis Care Res 2020;72:1213-23. PMID 32638548, doi:10.1002/acr.24333
              (physically demanding work OR 1.52; lifting, kneeling, squatting, climbing).
  [OIESTAD15] Oiestad BE et al. Osteoarthritis Cartilage 2015;23:171-7. PMID 25450853,
              doi:10.1016/j.joca.2014.10.008 (weak knee extensors, symptomatic knee OA OR 1.65).
  [MESSIER05] Messier SP et al. Arthritis Rheum 2005;52:2026-32. PMID 15986358, doi:10.1002/art.21139
              ("each pound of weight lost will result in a 4-fold reduction in the load exerted on
              the knee per step during daily activities").
  [ACR19]     Kolasinski SL et al. 2019 ACR/Arthritis Foundation OA guideline. Arthritis Care Res
              2020;72:149-62. PMID 31908149, doi:10.1002/acr.24131 (strong: exercise, weight loss,
              tai chi, cane, self-management, topical NSAIDs for the knee; conditional: yoga,
              balance work, heat or cold).
  [CDC-PA]    CDC "Physical Activity for Arthritis": at least 150 minutes a week of moderate activity
              plus 2 days of muscle strengthening; 5 or 10 minutes at a time counts.
  [FOX09]     Sophia Fox AJ et al. Sports Health 2009;1:461-8. PMID 23015907 (cartilage has no blood
              vessels; cells are fed from the joint fluid; zones, cells, collagen arcades).
  Behind the back-page picks (no claims are printed from these):
  [BIDESHKI24] PMID 38576215 doi:10.1002/ptr.8153  curcumin umbrella meta-analysis, knee OA.
  [ZHANG25]   PMID 40806131 doi:10.3390/nu17152547  network MA, 39 RCTs: boswellia ranked best;
              curcumin, collagen, ginger and krill oil also helped.
  [MATHIEU22] PMID 35458170 doi:10.3390/nu14081607  curcumin and ginger helped; omega-3 did not.
  [LUGO16]    PMID 26822714 doi:10.1186/s12937-016-0130-8  UC-II 40 mg a day for 180 days beat
              placebo and glucosamine + chondroitin on WOMAC.
  Caveats:    [WAI25] PMID 40731001 (certainty low); [EULAR22] PMID 35654458 (moderate evidence of
              small effects).  [KNUDSEN08] PMID 18363538 and EFSA 2011 (doi:10.2903/j.efsa.2011.2473):
              glucosamine with warfarin can raise the INR.
"""
import math
import os
import random

from kit import icon
from svgkit import T, svg, label_bg

SLUG = "joint-pain"

# ============================================================== text measuring
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


def tw(text, size, weight=600, ls=0.0, italic=False):
    """Advance width of `text` in Inter at `size` px (falls back to a generous guess)."""
    name = _WEIGHTS[weight]
    if italic:
        name = "Italic" if weight == 400 else name + "Italic"
    try:
        w = _face(name).getlength(text) * size / 100
    except Exception:
        w = len(text) * size * (0.68 if text.isupper() else 0.6)
    return w + ls * len(text)


# ============================================================== palette (every colour is in the KEY)
INK, INK2 = "#22303A", "#53616C"
BONE_EDGE = "#9A7444"                                                               # bone outline
CORTEX_HI, CORTEX_LO = "#E8CD9C", "#D3AF75"                                         # bone: outer shell
SPONGE_HI, SPONGE_LO, PORE = "#F7EBD2", "#EEDCB6", "#DDBF8B"                         # bone: spongy inside
CART_HI, CART_LO, CART_EDGE = "#C9E6F9", "#86BEE6", "#3B7DBA"                       # cartilage (blue)
MEN_HI, MEN_LO, MEN_EDGE = "#D3EFE8", "#92CFC1", "#378878"                          # meniscus (teal)
LIG, LIG_BACK, LIG_EDGE, LIG_FIB = "#FBF5E8", "#EFE2C6", "#B09460", "#D9C79E"       # ligament (ivory)
FLUID, FLUID_LT = "#F6D26C", "#FCEBB2"                                              # joint fluid (gold)
LINING, LINING_EDGE, LINING_HI = "#F0A49B", "#C8726A", "#F9D2CC"                    # calm lining (pink)
INFL, INFL_EDGE, INFL_HI = "#D6443B", "#97261F", "#EF8075"                          # inflamed lining (red)
SPUR, SPUR_HI, SPUR_EDGE = "#A8A297", "#CFCAC1", "#666057"                          # bone spur (grey)
CELL, CELL_NUC, LACUNA, LACUNA_EDGE = "#8668BF", "#47307D", "#F7F2FD", "#C3B4E4"     # cartilage cell (violet)
FIBER = "#5B9BD0"                                                                   # collagen fibers (blue)
GREEN, GREEN_DK = "#2E8A57", "#1F6B43"
RED, RED_DK = "#C23A2F", "#9C2B22"

# ============================================================== geometry (viewBox units)
W, H = 760, 416
CX = 380                       # the split line runs down the middle of the knee
FEM_TOP, TIB_BOT = 44, 344     # bone ends fade out above and below (local units)
K, YJ = 1.12, 214              # the knee is drawn in local units and scaled by K about the joint line
DROP = 8                       # the worn inner condyle sits lower: a narrowed joint space
KEY_Y, KEY_H = 362, 50
INS_R = 63
INS_L, INS_W = (100, 92), (660, 92)   # magnified circles (healthy, worn)


def _f(v):
    s = f"{v:.1f}"
    s = s.rstrip("0").rstrip(".") if "." in s else s
    return "0" if s in ("-0", "") else s


def _smooth(v):
    v = min(1.0, max(0.0, v))
    return v * v * (3 - 2 * v)


def _P(p):
    return (p[0], p[1], p[2] if len(p) > 2 else 1.0)


def _beziers(pts, closed=True):
    """Catmull-Rom through pts (third value = tangent tension; 0 = sharp corner) as cubic segments."""
    P = [_P(p) for p in pts]
    n = len(P)
    tg = []
    for i in range(n):
        if closed:
            a, b, f = P[i - 1], P[(i + 1) % n], 0.5
        else:
            a, b = P[max(i - 1, 0)], P[min(i + 1, n - 1)]
            f = 0.5 if 0 < i < n - 1 else 1.0
        k = P[i][2]
        tg.append((k * f * (b[0] - a[0]), k * f * (b[1] - a[1])))
    segs = []
    for i in range(n if closed else n - 1):
        j = (i + 1) % n
        p0, p3 = P[i][:2], P[j][:2]
        segs.append((p0, (p0[0] + tg[i][0] / 3, p0[1] + tg[i][1] / 3),
                     (p3[0] - tg[j][0] / 3, p3[1] - tg[j][1] / 3), p3))
    return segs


def path_d(pts, closed=True):
    segs = _beziers(pts, closed)
    d = [f"M{_f(segs[0][0][0])},{_f(segs[0][0][1])}"]
    for _, p1, p2, p3 in segs:
        d.append(f"C{_f(p1[0])},{_f(p1[1])} {_f(p2[0])},{_f(p2[1])} {_f(p3[0])},{_f(p3[1])}")
    return "".join(d) + ("Z" if closed else "")


def sample(pts, closed=True, per=16):
    """Points along the curve: [(x, y, segment_index)]."""
    out = []
    segs = _beziers(pts, closed)
    for si, (p0, p1, p2, p3) in enumerate(segs):
        for k in range(per):
            t = k / per
            m = 1 - t
            out.append((m ** 3 * p0[0] + 3 * m * m * t * p1[0] + 3 * m * t * t * p2[0] + t ** 3 * p3[0],
                        m ** 3 * p0[1] + 3 * m * m * t * p1[1] + 3 * m * t * t * p2[1] + t ** 3 * p3[1], si))
    if not closed:
        out.append((segs[-1][3][0], segs[-1][3][1], len(segs) - 1))
    return out


def _area(pts):
    n = len(pts)
    return 0.5 * sum(pts[i][0] * pts[(i + 1) % n][1] - pts[(i + 1) % n][0] * pts[i][1] for i in range(n))


def _offset(curve, th, sgn, closed=False):
    """Offset a polyline by per-point thickness th along its outward normal (sgn from _area);
    a negative thickness moves inward."""
    n, out = len(curve), []
    for i in range(n):
        if closed:
            a, b = curve[i - 1], curve[(i + 1) % n]
        else:
            a, b = curve[max(i - 1, 0)], curve[min(i + 1, n - 1)]
        tx, ty = b[0] - a[0], b[1] - a[1]
        m = math.hypot(tx, ty) or 1.0
        nx, ny = (-ty / m, tx / m) if sgn < 0 else (ty / m, -tx / m)
        out.append((curve[i][0] + nx * th[i], curve[i][1] + ny * th[i]))
    return out


def _poly(pts):
    return "M" + " L".join(f"{_f(x)},{_f(y)}" for x, y in pts) + "Z"


def _line(pts):
    return "M" + " L".join(f"{_f(x)},{_f(y)}" for x, y in pts)


def _arclen(curve):
    s = [0.0]
    for i in range(1, len(curve)):
        s.append(s[-1] + math.hypot(curve[i][0] - curve[i - 1][0], curve[i][1] - curve[i - 1][1]))
    tot = s[-1] or 1.0
    return [v / tot for v in s]


def _y_at(curve, x, pick=max, clamp=False):
    """y of a polyline at x (interpolated); pick chooses among several crossings.  With clamp,
    an x outside the curve takes the y of the nearest end."""
    ys = []
    for (x0, y0), (x1, y1) in zip(curve, curve[1:]):
        if (x0 - x) * (x1 - x) <= 0 and x0 != x1:
            ys.append(y0 + (y1 - y0) * (x - x0) / (x1 - x0))
    if ys:
        return pick(ys)
    if clamp:
        return min(curve, key=lambda p: abs(p[0] - x))[1]
    return None


def _s_at_x(curve, x):
    """Normalized arc length where the polyline first reaches x."""
    ss = _arclen(curve)
    for i in range(1, len(curve)):
        (x0, _), (x1, _) = curve[i - 1], curve[i]
        if (x0 - x) * (x1 - x) <= 0 and x0 != x1:
            return ss[i - 1] + (ss[i] - ss[i - 1]) * (x - x0) / (x1 - x0)
    return 0.5


# ---- bone outlines: left half (u = x - CX), mirrored for the right.  A right knee from the front.
FEM_L = [(-42, FEM_TOP, 0), (-42, 84), (-45, 104), (-53, 121), (-67, 136), (-86, 149), (-103, 159), (-111, 170),
         (-112, 180), (-109, 190), (-101, 200), (-86, 207), (-64, 210), (-44, 207), (-31, 199), (-25, 188),
         (-22, 175), (-17, 162), (-9, 154), (0, 151)]
FEM_ART = (8, 14)              # segments covered by cartilage on the outer condyle (rim -> notch edge)
TIB_L = [(-38, TIB_BOT, 0), (-38, 340), (-42, 324), (-52, 308), (-70, 292), (-92, 276), (-108, 262), (-116, 248),
         (-118, 237), (-114, 229), (-100, 225.5), (-76, 225), (-52, 225), (-36, 223), (-27, 219), (-20, 212),
         (-14, 203), (-8, 209), (0, 212)]
TIB_ART = (8, 13)              # segments covered by cartilage on the outer plateau
FIB = [(-104, 268), (-108, 255), (-118, 247), (-131, 246), (-142, 252), (-148, 264), (-146, 278), (-139, 290),
       (-134, 302), (-132, 318), (-131, TIB_BOT, 0), (-113, TIB_BOT, 0), (-113, 318), (-111, 304), (-107, 292),
       (-103, 280)]


def _mirror(pts, drop=0):
    out = []
    for p in pts:
        u, y, k = _P(p)
        out.append((-u, y + drop * _smooth((y - 168) / 38), k))
    return out


def _absx(pts):
    return [(CX + u, y, k) for u, y, k in (_P(p) for p in pts)]


FEM = _absx(FEM_L) + _absx(list(reversed(_mirror(FEM_L, DROP))))[1:]
TIB = _absx(TIB_L) + _absx(list(reversed(_mirror(TIB_L))))[1:]
FIBULA = _absx(FIB)
N_FEM, N_TIB = len(FEM), len(TIB)
FEM_ART_R = (N_FEM - 2 - FEM_ART[1], N_FEM - 2 - FEM_ART[0])   # the same segments, mirrored
TIB_ART_R = (N_TIB - 2 - TIB_ART[1], N_TIB - 2 - TIB_ART[0])

# joint lining (synovium): femur attachment -> tibia attachment.  The worn side bulges with extra fluid.
SYN_L = [(CX - 103, 159), (CX - 114, 164), (CX - 123, 175), (CX - 128, 191), (CX - 128.5, 208), (CX - 126, 224),
         (CX - 122, 237), (CX - 116.3, 247.5)]
SYN_R = [(CX + 103, 159), (CX + 119, 162), (CX + 133, 173), (CX + 142, 190), (CX + 144.5, 209), (CX + 143, 228),
         (CX + 137, 245), (CX + 124, 256), (CX + 112, 258.5)]


def _seg_pts(samples, rng):
    return [(x, y) for x, y, s in samples if rng[0] <= s <= rng[1]]


def _bands(surface, th, sgn, fill, edge, sw=0.9, cut=0.35):
    """Cartilage-style band(s) on a bone surface; runs thinner than `cut` leave bare bone."""
    off = _offset(surface, th, sgn)
    runs, run = [], []
    for i in range(len(surface)):
        if th[i] > cut:
            run.append(i)
        elif run:
            runs.append(run)
            run = []
    if run:
        runs.append(run)
    paths = []
    for r in runs:
        if len(r) < 2:
            continue
        pts = [surface[i] for i in r] + [off[i] for i in reversed(r)]
        paths.append(f'<path d="{_poly(pts)}" fill="{fill}" stroke="{edge}" stroke-width="{sw}" stroke-linejoin="round"/>')
    return "".join(paths), off


# ============================================================== the knee
def _bone(pts, uid, rnd, cortex, pore_box, pore_p, phys=None):
    """A bone in section: a solid outer shell (cortex), thick along the shaft and thin under the joint,
    around spongy bone near the joint end and smooth marrow up the shaft."""
    d = path_d(pts)
    sp = [(x, y) for x, y, _ in sample(pts, per=14)]
    sgn = -1 if _area(sp) < 0 else 1
    inner = _offset(sp, [-cortex(y) for _, y in sp], sgn, closed=True)
    o = [f'<clipPath id="jp-{uid}i"><path d="{_poly(inner)}"/></clipPath>',
         f'<path d="{d}" fill="url(#jp-cortex)"/>',
         f'<path d="{_poly(inner)}" fill="url(#jp-sponge)"/>',
         f'<g clip-path="url(#jp-{uid}i)">']
    x0, y0, x1, y1 = pore_box
    placed = []
    for _ in range(2600):
        x, y = rnd.uniform(x0, x1), rnd.uniform(y0, y1)
        if rnd.random() > pore_p(y):
            continue
        if all((x - px) ** 2 + (y - py) ** 2 > 6.4 ** 2 for px, py in placed):
            placed.append((x, y))
    for x, y in placed:
        rx, ry, a = rnd.uniform(1.5, 2.7), rnd.uniform(1.0, 1.8), rnd.uniform(0, 180)
        o.append(f'<ellipse cx="{_f(x)}" cy="{_f(y)}" rx="{_f(rx)}" ry="{_f(ry)}" transform="rotate({_f(a)} {_f(x)} {_f(y)})" '
                 f'fill="{PORE}" opacity=".62"/>')
    if phys:   # growth-plate scar, a faint line across the bone end
        o.append(f'<path d="{phys}" fill="none" stroke="#B88F57" stroke-width="1.1" opacity=".5" stroke-dasharray="1.2 2.4"/>')
    o.append("</g>")
    o.append(f'<path d="{_poly(inner)}" fill="none" stroke="#C49C62" stroke-width=".6" opacity=".55"/>')
    o.append(f'<path d="{d}" fill="none" stroke="{BONE_EDGE}" stroke-width="1.3" stroke-linejoin="round"/>')
    return "".join(o)


def _profile(s, power):
    return max(0.0, math.sin(math.pi * min(1.0, max(0.0, s)))) ** power


def _worn_thickness(curve, base, rnd, bald, cracks, full_cracks):
    """Thin, uneven cartilage: a bald patch (s range), V-shaped cracks, a frayed surface."""
    ss = _arclen(curve)
    th = []
    for s in ss:
        v = base * _profile(s, 0.5) * (0.84 + 0.3 * rnd.random())
        if bald[0] <= s <= bald[1]:
            v = 0.0
        else:
            for c in cracks:
                w = 0.024
                if abs(s - c) < w:
                    v *= abs(s - c) / w * 0.8 + (0.0 if c in full_cracks else 0.2)
        th.append(v)
    return th


def _meniscus(fem_surf, tib_surf, x_out, x_in, h_out, worn, rnd):
    """Wedge-shaped meniscus between the cartilage surfaces: in contact with the femur over its inner
    part, a free wedge at the rim.  x_out -> x_in may run either way."""
    n = 40
    top, bot = [], []
    for i in range(n + 1):
        x = x_out + (x_in - x_out) * i / n
        yb = _y_at(tib_surf, x, min, clamp=True) - 0.9
        h = h_out * (1 - i / n) ** 0.8 + 1.3
        yf = _y_at(fem_surf, x, max)
        ytop = yb - h
        if yf is not None:
            ytop = max(ytop, yf + 1.0)
        if worn and i > n * 0.7:          # frayed inner edge
            ytop += rnd.uniform(0, 1.6)
            yb -= rnd.uniform(0, 1.0)
        top.append((x, min(ytop, yb - 0.8)))
        bot.append((x, yb))
    sgn = -1 if x_out < x_in else 1
    rim = [(x_out + sgn * 2.4, top[0][1] * 0.55 + bot[0][1] * 0.45)]
    pts = top + list(reversed(bot)) + rim
    out = [f'<path d="{_poly(pts)}" fill="url(#jp-men)" stroke="{MEN_EDGE}" stroke-width="1" stroke-linejoin="round"/>']
    for f in (0.36, 0.64):   # circumferential fibres
        line = [(x, yt + (yb - yt) * f) for (x, yt), (_, yb) in zip(top[:int(n * 0.78)], bot[:int(n * 0.78)])]
        out.append(f'<path d="{_line(line)}" fill="none" stroke="#FFFFFF" stroke-width=".8" opacity=".6"/>')
    if worn:   # a tear running into the wedge
        a, b = int(n * 0.28), int(n * 0.9)
        line = [(x, yt + (yb - yt) * 0.52) for (x, yt), (_, yb) in zip(top[a:b], bot[a:b])]
        out.append(f'<path d="{_line(line)}" fill="none" stroke="{MEN_EDGE}" stroke-width="1.2" stroke-linecap="round"/>')
    return "".join(out)


def _syn_band(pts, worn, rnd):
    d = path_d(pts, closed=False)
    if not worn:
        return (f'<path d="{d}" fill="none" stroke="{LINING_EDGE}" stroke-width="6" stroke-linecap="round"/>'
                f'<path d="{d}" fill="none" stroke="{LINING}" stroke-width="4.2" stroke-linecap="round"/>'
                f'<path d="{d}" fill="none" stroke="{LINING_HI}" stroke-width="1.1" stroke-linecap="round" opacity=".9"/>')
    o = [f'<path d="{d}" fill="none" stroke="{INFL_EDGE}" stroke-width="10" stroke-linecap="round"/>',
         f'<path d="{d}" fill="none" stroke="{INFL}" stroke-width="7.8" stroke-linecap="round"/>']
    # finger-like folds (villi) of a swollen lining, reaching into the fluid
    curve = [(x, y) for x, y, _ in sample(pts, closed=False, per=10)]
    for i in range(6, len(curve) - 7, 4):
        (xa, ya), (xb, yb) = curve[i - 1], curve[i + 1]
        tx, ty = xb - xa, yb - ya
        m = math.hypot(tx, ty) or 1
        nx, ny = -ty / m, tx / m
        if abs(curve[i][0] + nx * 5 - CX) > abs(curve[i][0] - CX):   # point each fold toward the joint
            nx, ny = -nx, -ny
        r = 2.9 if i % 8 else 3.6
        fx, fy = curve[i][0] + nx * (3.9 + r * 0.7), curve[i][1] + ny * (3.9 + r * 0.7)
        o.append(f'<circle cx="{_f(fx)}" cy="{_f(fy)}" r="{r}" fill="{INFL}" stroke="{INFL_EDGE}" stroke-width=".9"/>')
    o.append(f'<path d="{d}" fill="none" stroke="{INFL_HI}" stroke-width="1.3" stroke-linecap="round" opacity=".85"/>')
    return "".join(o)


def _cruciates():
    """The two cruciate ligaments in the notch between the condyles: the back one (PCL) steeper and
    thicker, the front one (ACL) running from the outer condyle across to the front of the tibia."""
    o = []
    for (x0, y0), (x1, y1), w, fill in (((CX + 14, 160), (CX - 3, 213), 9.4, LIG_BACK),    # PCL, behind
                                        ((CX - 15, 165), (CX + 9, 210), 7.6, LIG)):         # ACL, in front
        d = f"M{x0},{y0} L{x1},{y1}"
        o.append(f'<path d="{d}" stroke="{LIG_EDGE}" stroke-width="{w + 2}" stroke-linecap="round"/>'
                 f'<path d="{d}" stroke="{fill}" stroke-width="{w}" stroke-linecap="round"/>')
        m = math.hypot(x1 - x0, y1 - y0)
        for k in (-w * 0.22, w * 0.22):
            nx, ny = -(y1 - y0) / m * k, (x1 - x0) / m * k
            o.append(f'<path d="M{_f(x0 + nx)},{_f(y0 + ny + 3)} L{_f(x1 + nx)},{_f(y1 + ny - 3)}" stroke="{LIG_FIB}" '
                     'stroke-width=".8"/>')
    return "".join(o)


def _spur(pts):
    return (f'<path d="{path_d(pts)}" fill="url(#jp-spur)" stroke="{SPUR_EDGE}" stroke-width="1.1" stroke-linejoin="round"/>')


def knee(rnd):
    fem_s = sample(FEM, per=16)
    tib_s = sample(TIB, per=16)
    sf = -1 if _area([(x, y) for x, y, _ in fem_s]) < 0 else 1
    st = -1 if _area([(x, y) for x, y, _ in tib_s]) < 0 else 1
    fem_l, fem_r = _seg_pts(fem_s, FEM_ART), _seg_pts(fem_s, FEM_ART_R)
    tib_l, tib_r = _seg_pts(tib_s, TIB_ART), _seg_pts(tib_s, TIB_ART_R)

    # cartilage thickness: healthy smooth and full; worn thin and cracked, worn through (a bald patch)
    # where the bones carry the most weight, the bottom of the inner condyle and the plateau under it
    th_fl = [7.4 * _profile(s, 0.42) for s in _arclen(fem_l)]
    th_tl = [6.4 * _profile(s, 0.42) for s in _arclen(tib_l)]
    bf = (_s_at_x(fem_r, CX + 50), _s_at_x(fem_r, CX + 80))
    bt = (_s_at_x(tib_r, CX + 52), _s_at_x(tib_r, CX + 78))
    th_fr = _worn_thickness(fem_r, 3.6, rnd, bf, (bf[0] - 0.12, bf[0] - 0.05, bf[1] + 0.07, bf[1] + 0.16),
                            (bf[0] - 0.05, bf[1] + 0.07))
    th_tr = _worn_thickness(tib_r, 3.3, rnd, bt, (bt[0] - 0.1, bt[1] + 0.12), (bt[1] + 0.12,))

    cart_fl, surf_fl = _bands(fem_l, th_fl, sf, "url(#jp-cart)", CART_EDGE)
    cart_tl, surf_tl = _bands(tib_l, th_tl, st, "url(#jp-cartu)", CART_EDGE)
    cart_fr, surf_fr = _bands(fem_r, th_fr, sf, "url(#jp-cart)", CART_EDGE)
    cart_tr, surf_tr = _bands(tib_r, th_tr, st, "url(#jp-cartu)", CART_EDGE)

    o = []
    # ---- joint fluid: the side pockets inside the lining, and the thin film between the cartilages
    for syn, inner in ((SYN_L, [(CX - 104, 240), (CX - 104, 172)]), (SYN_R, [(CX + 104, 248), (CX + 104, 172)])):
        sp = [(x, y) for x, y, _ in sample(syn, closed=False, per=12)]
        o.append(f'<path d="{_poly(sp + inner)}" fill="url(#jp-fluid)"/>')
    for fs, ts in ((fem_l, tib_l), (fem_r, tib_r)):
        o.append(f'<path d="{_poly(fs + list(reversed(ts)))}" fill="url(#jp-fluid)"/>')

    # ---- bones; the shafts fade out above and below
    o.append('<g mask="url(#jp-fade)">')
    o.append(_bone(FIBULA, "fib", rnd, lambda y: 1.8 + 3.0 * _smooth((y - 268) / 44),
                   (CX - 150, 244, CX - 100, 300), lambda y: 1.0 - _smooth((y - 282) / 18)))
    o.append(_bone(TIB, "tib", rnd, lambda y: 2.0 + 5.6 * _smooth((y - 246) / 64),
                   (CX - 122, 200, CX + 122, 300), lambda y: 1.0 - _smooth((y - 262) / 34)))
    o.append(_bone(FEM, "fem", rnd, lambda y: 2.0 + 5.6 * _smooth((150 - y) / 66),
                   (CX - 116, 96, CX + 116, 222), lambda y: _smooth((y - 112) / 44)))
    o.append("</g>")

    o.append(_cruciates())
    # ---- cartilage
    o += [cart_fl, cart_tl, cart_fr, cart_tr]
    # worn surface: tiny frays where the cartilage is breaking up
    for surf, th in ((surf_fr, th_fr), (surf_tr, th_tr)):
        for i in range(3, len(surf) - 3, 5):
            if th[i] > 1.0 and rnd.random() < 0.5:
                x, y = surf[i]
                o.append(f'<circle cx="{_f(x)}" cy="{_f(y)}" r="{_f(rnd.uniform(0.6, 1.0))}" fill="{CART_HI}" '
                         f'stroke="{CART_EDGE}" stroke-width=".5"/>')

    # ---- menisci: a healthy wedge at the rim; the worn one thinner, torn and pushed out past the edge
    o.append(_meniscus(surf_fl, surf_tl, CX - 118.5, CX - 80, 15, False, rnd))
    o.append(_meniscus(surf_fr, surf_tr, CX + 125, CX + 88, 9, True, rnd))

    # ---- bone spurs (osteophytes) at the edges of the worn joint, and a sharpened tibial spine
    o.append(_spur([(CX + 110.6, 179), (CX + 116.5, 182.5), (CX + 120.5, 189), (CX + 121.5, 196.5, 0.4),
                    (CX + 116.5, 197.5), (CX + 111, 195)]))
    o.append(_spur([(CX + 115.5, 229), (CX + 121.5, 228), (CX + 127, 229.5), (CX + 130.5, 233, 0.4), (CX + 126, 238),
                    (CX + 118.5, 242)]))
    o.append(_spur([(CX + 9.8, 208), (CX + 13, 199), (CX + 15.5, 191.5, 0.2), (CX + 18, 200), (CX + 20, 211)]))

    # ---- lining: thin and calm on the healthy side; thick, red and folded where it is inflamed
    o.append(_syn_band(SYN_L, False, rnd))
    o.append(_syn_band(SYN_R, True, rnd))
    # loose bits of worn cartilage floating in the extra fluid
    for x, y, a in ((CX + 129, 167, 20), (CX + 134, 214, -30), (CX + 136, 224, 55)):
        o.append(f'<path transform="translate({x},{y}) rotate({a})" d="M-3,-1.5 L1.1,-2.3 L3.2,0.2 L1.3,2.1 L-2.5,1.5 Z" '
                 f'fill="{CART_HI}" stroke="{CART_EDGE}" stroke-width=".8" stroke-linejoin="round"/>')
    return "".join(o), dict(surf_fl=surf_fl, surf_tl=surf_tl, surf_fr=surf_fr, surf_tr=surf_tr,
                            fem_l=fem_l, fem_r=fem_r, th_fl=th_fl)


# ============================================================== magnified cartilage
def _cell(x, y, rx=3.7, ry=3.7, rot=0, lac=1.6, empty=False):
    g = (f'<g transform="translate({_f(x)},{_f(y)}) rotate({_f(rot)})">'
         f'<ellipse rx="{_f(rx + lac)}" ry="{_f(ry + lac)}" fill="{LACUNA}" stroke="{LACUNA_EDGE}" stroke-width=".7"/>')
    if not empty:
        g += (f'<ellipse rx="{_f(rx)}" ry="{_f(ry)}" fill="{CELL}"/>'
              f'<circle r="{_f(min(rx, ry) * 0.42)}" fill="{CELL_NUC}"/>')
    return g + "</g>"


def _cluster(x, y, n, rot=0):
    """A clump of cartilage cells sharing one enlarged space (seen in worn cartilage)."""
    cells = [(-4.6, -2.4), (4.4, -2.6), (-4.4, 3.2), (4.6, 3.0), (0, -6.4), (0.2, 6.6)][:n]
    w = 10.5 if n <= 4 else 11.5
    g = [f'<g transform="translate({_f(x)},{_f(y)}) rotate({_f(rot)})">',
         f'<ellipse rx="{w}" ry="{w - 1.6 if n <= 4 else w}" fill="{LACUNA}" stroke="{LACUNA_EDGE}" stroke-width=".7"/>']
    for cx, cy in cells:
        g.append(f'<circle cx="{cx}" cy="{cy}" r="3.2" fill="{CELL}" stroke="{LACUNA}" stroke-width=".6"/>'
                 f'<circle cx="{cx}" cy="{cy}" r="1.3" fill="{CELL_NUC}"/>')
    g.append("</g>")
    return "".join(g)


def _place(rnd, box, n, mind, avoid=(), tries=4000):
    out = []
    for _ in range(tries):
        if len(out) >= n:
            break
        x, y = rnd.uniform(box[0], box[2]), rnd.uniform(box[1], box[3])
        if any((x - px) ** 2 + (y - py) ** 2 < mind ** 2 for px, py in out):
            continue
        if any((x - ax) ** 2 + (y - ay) ** 2 < ar ** 2 for ax, ay, ar in avoid):
            continue
        out.append((x, y))
    return out


def inset(c, worn):
    """A circle of cartilage magnified: joint fluid on top, cartilage (cells in a collagen mesh),
    the tidemark, then bone.  Healthy: thick, smooth, orderly.  Worn: thin, cracked, cells clumped."""
    cx, cy = c
    r = INS_R
    rnd = random.Random(41 if worn else 17)
    uid = "w" if worn else "h"
    S = cy - (10 if worn else 32)          # cartilage surface
    TM = cy + (20 if worn else 22)         # tidemark
    BN = cy + (27 if worn else 30)         # top of bone
    x0, x1 = cx - r - 4, cx + r + 4
    ring = RED_DK if worn else GREEN_DK
    o = [f'<clipPath id="jp-c{uid}"><circle cx="{cx}" cy="{cy}" r="{r}"/></clipPath>',
         f'<circle cx="{cx + 1.5}" cy="{cy + 2.5}" r="{r + 3}" fill="#2A3640" opacity=".09"/>',
         f'<g clip-path="url(#jp-c{uid})">',
         f'<rect x="{x0}" y="{cy - r - 4}" width="{2 * r + 8}" height="{2 * r + 8}" fill="url(#jp-fluidi)"/>']
    # cartilage outline (top edge); worn: frayed, with V-shaped cracks
    top = []
    cracks = [(-36, 22, 5.5), (-8, 30, 6.5), (24, 25, 5.0), (46, 15, 4.0)] if worn else []
    x = x0
    while x <= x1:
        y = S + 0.0016 * (x - cx) ** 2
        if worn:
            y += rnd.uniform(-1.8, 1.8)
        top.append((x, y))
        hit = next((cr for cr in cracks if abs(x - (cx + cr[0])) < 1.2), None)
        if hit:
            fx, depth, hw = cx + hit[0], hit[1], hit[2]
            top.append((fx - hw * 0.35, S + depth * 0.55))
            top.append((fx + rnd.uniform(-1, 1), S + depth))
            top.append((fx + hw * 0.4, S + depth * 0.5))
            top.append((fx + hw, S + 0.0016 * (fx + hw - cx) ** 2))
            x = fx + hw + 2
            continue
        x += 2.2
    clip = f'<clipPath id="jp-cl{uid}"><path d="{_poly(top + [(x1, BN), (x0, BN)])}"/></clipPath>'
    o.insert(0, clip)
    o.append(f'<path d="{_poly(top + [(x1, BN + 2), (x0, BN + 2)])}" fill="url(#{"jp-mtw" if worn else "jp-mt"})" '
             f'stroke="{CART_EDGE}" stroke-width="1.1" stroke-linejoin="round"/>')
    # collagen fibres: arches (arcades) that rise from deep down and turn to run along the surface
    fib = []
    step = 24
    xa = x0 - 6
    while xa < x1:
        h0 = S + (6 if not worn else 8)
        for dx in (0, step / 2):
            xs = xa + dx
            seg = (f"M{_f(xs)},{TM} V{_f(h0 + 13)} Q{_f(xs)},{_f(h0)} {_f(xs + step / 2)},{_f(h0)} "
                   f"Q{_f(xs + step)},{_f(h0)} {_f(xs + step)},{_f(h0 + 13)} V{TM}")
            if worn:   # a broken mesh: dashes with gaps
                fib.append(f'<path d="{seg}" fill="none" stroke="{FIBER}" stroke-width=".9" opacity=".5" '
                           f'stroke-dasharray="{rnd.randint(4, 8)} {rnd.randint(5, 9)}"/>')
            else:
                fib.append(f'<path d="{seg}" fill="none" stroke="{FIBER}" stroke-width=".75" opacity=".26"/>')
        xa += step
    if not worn:   # the smooth gliding skin at the surface
        fib.append(f'<path d="{_line([(x, S + 2.4 + 0.0016 * (x - cx) ** 2) for x in range(int(x0), int(x1) + 1, 3)])}" '
                   f'fill="none" stroke="{FIBER}" stroke-width="1.2" opacity=".7"/>')
    o.append(f'<g clip-path="url(#jp-cl{uid})">{"".join(fib)}</g>')
    # calcified layer and the wavy tidemark, then bone
    wav = [(x, TM + 1.5 * math.sin((x - x0) / 7.5)) for x in range(int(x0), int(x1) + 1, 2)]
    o.append(f'<path d="{_poly(wav + [(x1, BN + 2), (x0, BN + 2)])}" fill="#C3D8EA"/>')
    o.append(f'<path d="{_line(wav)}" fill="none" stroke="#5B84B0" stroke-width="1.2"/>')
    if worn:   # a doubled tidemark: the hard layer creeping up into the cartilage
        o.append(f'<path d="{_line([(x, y - 4.5) for x, y in wav])}" fill="none" stroke="#5B84B0" stroke-width="1" opacity=".8"/>')
    o.append(f'<rect x="{x0}" y="{BN}" width="{2 * r + 8}" height="{cy + r + 4 - BN}" fill="url(#jp-bonei)"/>')
    holes = _place(rnd, (x0, BN + 6, x1, cy + r + 4), 13 if worn else 22, 11 if worn else 9.5)
    for hx, hy in holes:
        rx, ry = (rnd.uniform(2.2, 3.4), rnd.uniform(1.5, 2.4)) if worn else (rnd.uniform(3.2, 4.8), rnd.uniform(2.2, 3.4))
        o.append(f'<ellipse cx="{_f(hx)}" cy="{_f(hy)}" rx="{_f(rx)}" ry="{_f(ry)}" fill="{SPONGE_HI}" '
                 f'stroke="#B98F57" stroke-width=".7" transform="rotate({rnd.randint(0, 180)} {_f(hx)} {_f(hy)})"/>')
    o.append(f'<path d="M{x0},{BN} H{x1}" stroke="{BONE_EDGE}" stroke-width="1.2" opacity=".7"/>')

    cells = []
    if not worn:
        for xx in range(int(x0) + 6, int(x1), 15):     # surface zone: flat cells along the surface
            yy = S + 7.5 + 0.0016 * (xx - cx) ** 2
            cells.append(_cell(xx + rnd.uniform(-2, 2), yy, 5.0, 1.8, rnd.uniform(-6, 6), 1.3))
        for xx, yy in _place(rnd, (x0 + 4, S + 17, x1 - 4, TM - 21), 12, 15.5):   # middle zone: round, scattered
            cells.append(_cell(xx, yy + 0.0008 * (xx - cx) ** 2, 3.5, 3.3, rnd.uniform(0, 180), 1.6))
        for xx in range(int(x0) + 9, int(x1), 17):     # deep zone: little stacks (columns) of cells
            for j in range(3):
                cells.append(_cell(xx + rnd.uniform(-1.2, 1.2), TM - 15 + j * 6.4, 3.0, 2.5, 0, 1.2))
    else:
        for dx, dy, n in ((-52, 9, 4), (-23, 13, 5), (8, 6, 6), (36, 12, 4), (58, 4, 3)):
            cells.append(_cluster(cx + dx, cy + dy, n, rnd.uniform(-20, 20)))
        for dx, dy in ((-62, -1), (-40, 4), (22, -1), (48, -1)):
            cells.append(_cell(cx + dx, cy + dy, 3.2, 3.0, 0, 1.6, empty=True))   # an empty space: a lost cell
        for dx in range(-60, 70, 19):
            cells.append(_cell(cx + dx + rnd.uniform(-2, 2), TM - 6, 3.0, 2.5, 0, 1.2))
    o.append(f'<g clip-path="url(#jp-cl{uid})">{"".join(cells)}</g>')
    if worn:   # flakes breaking off into the fluid
        for dx, dy, a in ((-42, -38, 15), (-6, -48, -25), (30, -32, 40), (12, -24, 70)):
            o.append(f'<path transform="translate({cx + dx},{cy + dy}) rotate({a})" d="M-4.6,-2 L1.4,-3.2 L4.6,0 L2,3 L-3.8,2.2 Z" '
                     f'fill="url(#jp-mtw)" stroke="{CART_EDGE}" stroke-width=".9" stroke-linejoin="round"/>')
    o.append("</g>")
    o.append(f'<circle cx="{cx}" cy="{cy}" r="{r + 2}" fill="none" stroke="#FFFFFF" stroke-width="3.4"/>')
    o.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{ring}" stroke-width="2.6"/>')
    return "".join(o)


def _lens(x, y, col, r=11):
    """A dashed ring on the knee marking the spot each magnified circle shows."""
    return (f'<circle cx="{_f(x)}" cy="{_f(y)}" r="{r + 1.5}" fill="none" stroke="#FFFFFF" stroke-width="3.4"/>'
            f'<circle cx="{_f(x)}" cy="{_f(y)}" r="{r}" fill="none" stroke="{col}" stroke-width="1.9" stroke-dasharray="3.4 2.4"/>')


# ============================================================== labels
def _leader(x0, y0, x1, y1):
    d = f"M{_f(x0)},{_f(y0)} L{_f(x1)},{_f(y1)}"
    return (f'<path d="{d}" stroke="#FFFFFF" stroke-width="3.4" stroke-linecap="round"/>'
            f'<path d="{d}" stroke="#46535D" stroke-width="1.2" stroke-linecap="round"/>'
            f'<circle cx="{_f(x1)}" cy="{_f(y1)}" r="2.6" fill="#46535D" stroke="#FFFFFF" stroke-width="1.2"/>')


def _badge(x, y, n, fill):
    return (f'<circle cx="{_f(x)}" cy="{_f(y)}" r="8.6" fill="{fill}"/>'
            + T(_f(x), _f(y + 3.8), str(n), 10.5, 800, "#FFFFFF", "middle"))


def _marker(x, y, n):
    return (f'<circle cx="{_f(x)}" cy="{_f(y)}" r="8.4" fill="#FFFFFF" stroke="{RED_DK}" stroke-width="1.8"/>'
            + T(_f(x), _f(y + 3.8), str(n), 10.5, 800, RED_DK, "middle"))


def _pill(cx, y, text, fill):
    fs, ls = 11.5, 1.0
    w = tw(text, fs, 800, ls) + 24
    return (f'<rect x="{_f(cx - w / 2)}" y="{y}" width="{_f(w)}" height="21" rx="10.5" fill="{fill}"/>'
            + T(_f(cx + ls / 2), y + 14.6, text, fs, 800, "#FFFFFF", "middle", ls=ls))


# ============================================================== key swatches (same code as the art)
def sw_bone():
    return ('<rect x="-12" y="-7" width="24" height="14" rx="3" fill="url(#jp-cortex)" stroke="#9A7444" stroke-width="1"/>'
            '<rect x="-9" y="-4" width="18" height="8" rx="2" fill="url(#jp-sponge)"/>'
            f'<ellipse cx="-4" cy="-0.6" rx="2" ry="1.3" fill="{PORE}" opacity=".7"/>'
            f'<ellipse cx="3.6" cy="1.2" rx="2.2" ry="1.4" fill="{PORE}" opacity=".7"/>')


def sw_cart():
    return f'<rect x="-12" y="-5" width="24" height="10" rx="4" fill="url(#jp-cart)" stroke="{CART_EDGE}" stroke-width="1"/>'


def sw_men():
    return (f'<path d="M-12,-6 L-12,6 L12,5 C4,3.8 -4,0 -12,-6 Z" fill="url(#jp-men)" stroke="{MEN_EDGE}" '
            'stroke-width="1" stroke-linejoin="round"/>')


def sw_lig():
    return (f'<rect x="-12" y="-4.6" width="24" height="9.2" rx="4.6" fill="{LIG}" stroke="{LIG_EDGE}" stroke-width="1"/>'
            f'<path d="M-9,-1.6 H9 M-9,1.6 H9" stroke="{LIG_FIB}" stroke-width=".8"/>')


def sw_fluid():
    return (f'<path d="M0,-8 C-4,-2.6 -7,0.4 -7,3.4 A7,7 0 0 0 7,3.4 C7,0.4 4,-2.6 0,-8 Z" fill="url(#jp-fluid)" '
            'stroke="#D6A22A" stroke-width="1"/>')


def sw_lining():
    return (f'<path d="M-12,0 H12" stroke="{LINING_EDGE}" stroke-width="6" stroke-linecap="round"/>'
            f'<path d="M-12,0 H12" stroke="{LINING}" stroke-width="4.2" stroke-linecap="round"/>')


def sw_infl():
    return (f'<path d="M-12,-1.6 H12" stroke="{INFL_EDGE}" stroke-width="9" stroke-linecap="round"/>'
            f'<path d="M-12,-1.6 H12" stroke="{INFL}" stroke-width="7" stroke-linecap="round"/>'
            + "".join(f'<circle cx="{x}" cy="4.2" r="2.6" fill="{INFL}" stroke="{INFL_EDGE}" stroke-width=".8"/>' for x in (-7, 0, 7)))


def sw_spur():
    return (f'<path d="M-12,7 C-6,6 -1,3 3,-1 C6,-4 8.5,-6.5 11.5,-7.5 C10,-3 7,1.8 3,4.8 C0,7 -6,8 -12,8 Z" '
            f'fill="url(#jp-spur)" stroke="{SPUR_EDGE}" stroke-width="1" stroke-linejoin="round"/>')


def sw_cell():
    return _cell(0, 0, 4.4, 3.8, 0, 1.9)


def sw_fiber():
    return (f'<path d="M-12,6 V0 Q-12,-6 -6,-6 Q0,-6 0,0 V6 M0,6 V0 Q0,-6 6,-6 Q12,-6 12,0 V6" fill="none" '
            f'stroke="{FIBER}" stroke-width="1.5"/>')


KEY_ROWS = [
    [(sw_bone, "Bone"), (sw_cart, "Cartilage"), (sw_men, "Meniscus (cushion)"), (sw_lig, "Ligament"),
     (sw_fluid, "Joint fluid")],
    [(sw_lining, "Calm lining"), (sw_infl, "Inflamed lining"), (sw_spur, "Bone spur"), (sw_cell, "Cartilage cell"),
     (sw_fiber, "Collagen fibers")],
]


def _key(y):
    """Two-row KEY; column widths follow the longest label in each column."""
    x0, x1, h = 8, W - 8, KEY_H
    fs = 11
    out = [f'<rect x="{x0}" y="{y}" width="{x1 - x0}" height="{h}" rx="9" fill="#FFFFFF" stroke="#CBD5DC" stroke-width="1.2"/>',
           T(x0 + 14, y + h / 2 + 3.8, "KEY", 10.5, 800, INK, ls=1.4)]
    start = x0 + 14 + tw("KEY", 10.5, 800, 1.4) + 20
    ncol = len(KEY_ROWS[0])
    widths = [max(24 + 8 + tw(row[i][1], fs, 600) for row in KEY_ROWS) for i in range(ncol)]
    gap = (x1 - 14 - start - sum(widths)) / (ncol - 1)
    xs, x = [], start
    for w in widths:
        xs.append(x)
        x += w + gap
    for r, row in enumerate(KEY_ROWS):
        cy = y + 14 + r * 22
        for (sw, lab), x in zip(row, xs):
            out.append(f'<g transform="translate({_f(x + 12)},{_f(cy)})">{sw()}</g>')
            out.append(T(_f(x + 32), _f(cy + 3.9), lab, fs, 600, INK))
    return "".join(out)


# ============================================================== the whole picture
HEALTHY_NOTES = [  # title, plain-words subtitle
    ("Smooth cartilage", "lets the bones glide"),
    ("Joint fluid", "oils and feeds the cartilage"),
    ("Meniscus", "a rubbery shock pad"),
]
WORN_NOTES = [  # the "what happens" sequence, numbered on the art
    ("Cartilage thins and cracks", "bits break off into the fluid"),
    ("Bone spurs grow", "at the edges of the joint"),
    ("The lining swells", "and makes extra fluid"),
    ("The space narrows", "so bone can rub on bone"),
]


def tf(x, y):
    """Local knee units -> viewBox units (the knee is drawn K times larger about the joint line)."""
    return CX + (x - CX) * K, YJ + (y - YJ) * K


def art_knee():
    rnd = random.Random(2026)
    body, g = knee(rnd)
    defs = ['<defs>',
            f'<linearGradient id="jp-cortex" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{CORTEX_HI}"/>'
            f'<stop offset="1" stop-color="{CORTEX_LO}"/></linearGradient>',
            f'<linearGradient id="jp-sponge" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{SPONGE_HI}"/>'
            f'<stop offset="1" stop-color="{SPONGE_LO}"/></linearGradient>',
            '<linearGradient id="jp-bonei" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#E9CF9F"/>'
            f'<stop offset="1" stop-color="{CORTEX_LO}"/></linearGradient>',
            f'<linearGradient id="jp-cart" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{CART_LO}"/>'
            f'<stop offset="1" stop-color="{CART_HI}"/></linearGradient>',
            f'<linearGradient id="jp-cartu" x1="0" y1="1" x2="0" y2="0"><stop offset="0" stop-color="{CART_LO}"/>'
            f'<stop offset="1" stop-color="{CART_HI}"/></linearGradient>',
            f'<linearGradient id="jp-men" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="{MEN_LO}"/>'
            f'<stop offset="1" stop-color="{MEN_HI}"/></linearGradient>',
            f'<linearGradient id="jp-fluid" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{FLUID_LT}"/>'
            f'<stop offset="1" stop-color="{FLUID}"/></linearGradient>',
            f'<linearGradient id="jp-fluidi" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FDF3D2"/>'
            f'<stop offset="1" stop-color="{FLUID_LT}"/></linearGradient>',
            '<linearGradient id="jp-mt" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#E9F5FD"/>'
            '<stop offset="1" stop-color="#C6E1F5"/></linearGradient>',
            '<linearGradient id="jp-mtw" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#F1F5F8"/>'
            '<stop offset="1" stop-color="#D5E3EE"/></linearGradient>',
            f'<linearGradient id="jp-spur" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{SPUR_HI}"/>'
            f'<stop offset="1" stop-color="{SPUR}"/></linearGradient>',
            f'<linearGradient id="jp-fadeg" gradientUnits="userSpaceOnUse" x1="0" y1="{FEM_TOP}" x2="0" y2="{TIB_BOT}">'
            '<stop offset="0" stop-color="#000"/><stop offset=".13" stop-color="#fff"/>'
            '<stop offset=".84" stop-color="#fff"/><stop offset="1" stop-color="#000"/></linearGradient>',
            f'<mask id="jp-fade" maskUnits="userSpaceOnUse" x="0" y="0" width="{W}" height="{H}">'
            f'<rect width="{W}" height="{H}" fill="url(#jp-fadeg)"/></mask>',
            '</defs>']
    o = ["".join(defs), f'<g transform="translate({_f(CX * (1 - K))},{_f(YJ * (1 - K))}) scale({K})">{body}</g>']

    # split line down the middle of the knee
    o.append(f'<path d="M{CX},{_f(tf(CX, FEM_TOP)[1] + 6)} V{_f(tf(CX, TIB_BOT)[1] - 4)}" stroke="#7D8A96" '
             'stroke-width="1.4" stroke-dasharray="5 4"/>')
    # headings over each half
    o.append(_pill(CX - 62, 2, "HEALTHY", GREEN))
    o.append(_pill(CX + 80, 2, "OSTEOARTHRITIS", RED))

    # bone names, in clear space on the shafts
    for y, lines in ((68, ["Thigh bone", "(femur)"]), (314, ["Shin bone", "(tibia)"])):
        o.append(label_bg(CX - 36, y - 12, 72, 30, "#FFFFFF", 0.9, 6))
        o.append(T(CX, y, lines[0], 10.5, 700, INK, "middle"))
        o.append(T(CX, y + 13, lines[1], 10, 500, INK2, "middle", italic=True))
    o.append(T(CX - 154, 322, "Calf bone", 10.5, 700, INK, "end"))
    o.append(T(CX - 154, 335, "(fibula)", 10, 500, INK2, "end", italic=True))

    # magnified circles, and the dashed rings on the knee that mark the spot each one shows
    lx, ly = tf(CX - 66, _y_at(g["fem_l"], CX - 66, max) + 3.4)
    rx, ry = tf(CX + 38, _y_at(g["fem_r"], CX + 38, max) + 1.6)
    o.append(inset(INS_L, False))
    o.append(inset(INS_W, True))
    o.append(_lens(lx, ly, GREEN_DK))
    o.append(_lens(rx, ry, RED_DK))
    for (cx, cy), title, sub, col in ((INS_L, "Healthy cartilage, up close", "cells sit in a springy, water-rich mesh", GREEN_DK),
                                      (INS_W, "Worn cartilage, up close", "the mesh frays and cracks, cells clump", RED_DK)):
        o.append(T(cx, cy + INS_R + 18, title, 11.5, 800, col, "middle"))
        o.append(T(cx, cy + INS_R + 31, sub, 10, 500, INK2, "middle", italic=True))

    # healthy side: names with leader lines (targets on the outer edge of the joint)
    fl, thl = g["fem_l"], g["th_fl"]
    i_c = min(range(len(fl)), key=lambda i: abs(fl[i][1] - 186) + (0 if fl[i][0] < CX - 100 else 99))
    cart_pt = (fl[i_c][0] - thl[i_c] * 0.5, fl[i_c][1])
    tgt = [tf(*cart_pt), tf(CX - 121, 205), tf(CX - 108, 214.5)]
    xt = 206
    for (title, sub), (tx, ty), y in zip(HEALTHY_NOTES, tgt, (205, 234, 263)):
        o.append(T(xt, y, title, 11.5, 800, INK, "end"))
        o.append(T(xt, y + 13, sub, 10, 500, INK2, "end", italic=True))
        o.append(_leader(xt + 6, y - 4, tx, ty))

    # worn side: numbered markers on the art, explained in a list on the right
    for i, (x, y) in enumerate([(CX + 62, 191), (CX + 100.5, 184), (CX + 159, 228), (CX + 72, 243)]):
        o.append(_marker(*tf(x, y), i + 1))
    xl = 566
    for i, (title, sub) in enumerate(WORN_NOTES):
        y = 212 + i * 33
        o.append(_badge(xl + 8.6, y - 4, i + 1, RED))
        o.append(T(xl + 23, y, title, 11.5, 800, INK))
        o.append(T(xl + 23, y + 13, sub, 10, 500, INK2, italic=True))

    o.append(_key(KEY_Y))
    return svg(W, H, "".join(o),
               "A knee joint seen from the front and split down the middle. Left, healthy: smooth cartilage, an even "
               "joint space, a thin lining and a little joint fluid, with a magnified circle of orderly cartilage cells. "
               "Right, osteoarthritis: thin and cracked cartilage, bone spurs, a narrowed space, a swollen red lining "
               "with extra fluid, and a magnified circle of cracked cartilage with clumped cells.")


# ============================================================== front page blocks
FEEL = [  # [NICE22] activity-related pain, short morning stiffness; [HUNTER19] crepitus, bony enlargement,
    # restricted motion, mild swelling, instability
    "Pain when you use the joint, easing with rest",
    "Stiff on waking or after sitting, loose within 30 minutes",
    "Creaking, grinding or clicking as it bends",
    "Some swelling, or a joint that feels unsteady",
    "Stairs, kneeling or opening jars get harder",
    "Hard knobs on the finger joints",
]
ALERT = [  # [NICE22] QS87 atypical features: hot swollen joint, prolonged stiffness, trauma, rapid worsening, deformity
    "A <b>hot, red, very swollen</b> joint, above all with a fever: <b>get care the same day</b>",
    "Morning stiffness <b>over 30 minutes</b>, or many sore joints",
    "It began with a <b>fall or injury</b>, or is worsening fast",
    "The joint <b>locks, gives way</b> or changes shape",
]

IC_WOMAN = '<circle cx="32" cy="23" r="13"/><path d="M32 36v21M23 48h18"/>'
IC_LIFT = ('<rect x="15" y="33" width="34" height="22" rx="3"/><path d="M15 42h34"/><path d="M27 33v-3h10v3"/>'
           '<path d="M32 24V7M25 14l7-7 7 7"/>')
RISKS = [  # (icon, label, custom)
    ("age", "Getting older", None),                           # [WHO23] about 73% are older than 55
    ("scale", "Extra body<br>weight", None),                  # [SILVER15] overweight OR 1.98, obesity 2.66
    ("bone", "An old joint<br>injury", None),                 # [SILVER15] previous knee injury OR 2.83
    ("woman", "Being<br>a woman", IC_WOMAN),                  # [SILVER15] OR 1.68; [WHO23] 60% female
    ("dna", "Family<br>history", None),                       # [HUNTER19] genetics
    ("lift", "Heavy lifting or<br>kneeling work", IC_LIFT),   # [WANG20] OR 1.52
    ("dumbbell", "Weak thigh<br>muscles", None),              # [OIESTAD15] OR 1.65
]


def _ic(body, size, sw=2.8):
    return (f'<svg class="ic" viewBox="0 0 64 64" style="width:{size};height:{size}" fill="none" stroke="currentColor" '
            f'stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{body}</svg>')


def _scale_0_10():
    """A 0 to 10 pain scale, green to red, for the patient to circle."""
    cols = ["#2E8A57", "#4E9A45", "#74A73A", "#9CB232", "#C2B52C", "#E0A82A", "#E58E2A", "#E1712B", "#D9552E",
            "#CC3D2F", "#B32A2A"]
    cells = "".join(f'<span style="background:{c}">{i}</span>' for i, c in enumerate(cols))
    return f'<div class="jpn-pain">{cells}</div><div class="jpn-pl"><span>No pain</span><span>Worst</span></div>'


def front(t, ed):
    feel = "".join(f"<li>{x}</li>" for x in FEEL)
    alert = "".join(f"<li>{x}</li>" for x in ALERT)
    risk = "".join(f'<div class="jpn-rf"><span class="jpn-disc">'
                   f'{_ic(custom, "0.3in") if custom else icon(ic, "0.3in", sw=2.8)}</span><span class="jpn-rl">{lab}</span></div>'
                   for ic, lab, custom in RISKS)
    nums = (
        # [MESSIER05] each pound lost = about a 4-fold drop in knee load per step
        '<div class="jpn-n"><b class="jpn-big">1 lb <i>&rarr;</i> 4 lb</b><span>Each pound you lose takes about '
        '<b>4 pounds</b> of load off your knee with every step.</span></div>'
        # [NICE22] OA morning stiffness lasts no longer than 30 minutes
        '<div class="jpn-n"><b class="jpn-big">30 min</b><span>OA stiffness usually eases within <b>30 minutes</b> '
        'of getting up. Longer? Get checked.</span></div>'
        # [CDC-PA] 150 minutes a week + 2 strength days; 5 or 10 minutes at a time counts
        '<div class="jpn-n"><b class="jpn-big">150 min</b><span>a week of walking, cycling or water exercise, plus '
        '<b>2 days</b> of strength work.</span></div>'
        f'<div class="jpn-n jpn-me"><b>My pain today</b>{_scale_0_10()}<span>Circle it today and at each visit.</span></div>')
    return ('<div class="jpn">'
            f'<div class="art jpn-art">{art_knee()}</div>'
            '<div class="jpn-row">'
            f'<div class="jpn-feel"><div class="jpn-sh">How it can feel</div><ul class="jpn-dots">{feel}</ul></div>'
            f'<div class="jpn-alert"><div class="jpn-ah">Get checked promptly if</div><ul>{alert}</ul></div></div>'
            f'<div class="jpn-sh jpn-sh2">What raises your risk</div><div class="jpn-risk">{risk}</div>'
            f'<div class="jpn-sh jpn-sh2">Know your numbers</div><div class="jpn-nums">{nums}</div>'
            '</div>')


CSS = r"""
.jpn .jpn-art{margin-top:0.02in}
.jpn .jpn-sh{font:800 7.6pt Inter,sans-serif;letter-spacing:.14em;text-transform:uppercase;color:var(--c1);margin:0 0 3px}
.jpn .jpn-sh2{margin-top:0.065in}
.jpn .jpn-row{display:grid;grid-template-columns:1fr 3.3in;gap:0.18in;margin-top:0.07in;align-items:start}
.jpn .jpn-dots{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:1fr;gap:1px 0}
.jpn .jpn-dots li{position:relative;padding-left:12px;font-size:8.2pt;line-height:1.27;color:#2B3236}
.jpn .jpn-dots li::before{content:"";position:absolute;left:0;top:4px;width:6px;height:6px;border-radius:50%;background:var(--c2)}
.jpn .jpn-alert{border:1.5px solid #C0392B;background:#FDF1EF;border-radius:8px;padding:4px 10px 5px}
.jpn .jpn-ah{font:800 7.6pt Inter,sans-serif;letter-spacing:.14em;text-transform:uppercase;color:#A5281E;margin:0 0 2px}
.jpn .jpn-alert ul{margin:0;padding:0 0 0 12px}
.jpn .jpn-alert li{font-size:8pt;line-height:1.27;color:#2B3236;margin:0 0 1px}
.jpn .jpn-alert li::marker{color:#C0392B}
.jpn .jpn-alert b{color:#8E2219}
.jpn .jpn-risk{display:grid;grid-template-columns:repeat(7,1fr);gap:0 0.05in}
.jpn .jpn-rf{display:flex;flex-direction:column;align-items:center;text-align:center}
.jpn .jpn-disc{width:0.46in;height:0.46in;border-radius:50%;background:var(--soft);color:var(--c1);display:flex;
  align-items:center;justify-content:center;box-shadow:inset 0 0 0 1.5px rgba(31,94,140,.12)}
.jpn .jpn-rl{display:block;font-size:7.9pt;font-weight:600;line-height:1.2;color:#2F373C;margin-top:0.03in}
.jpn .jpn-nums{display:grid;grid-template-columns:1fr 1fr 1fr 1.32fr;gap:0.08in}
.jpn .jpn-n{background:var(--tint);border:1px solid #D9E6F0;border-top:3px solid var(--c2);border-radius:7px;
  padding:4px 8px 5px;display:flex;flex-direction:column;gap:1px}
.jpn .jpn-big{font:900 14pt/1.1 Merriweather,Georgia,serif;color:var(--c1);white-space:nowrap}
.jpn .jpn-big i{font-style:normal;color:var(--c2);font-family:Inter,sans-serif;font-weight:800}
.jpn .jpn-n span{font-size:7.8pt;line-height:1.26;color:#2B3236}
.jpn .jpn-n span b{color:var(--deep)}
.jpn .jpn-me>b{font:800 8.4pt Inter,sans-serif;color:var(--deep)}
.jpn .jpn-pain{display:grid;grid-template-columns:repeat(11,1fr);gap:2px;margin-top:2px}
.jpn .jpn-pain span{display:flex;align-items:center;justify-content:center;height:0.2in;border-radius:3px;color:#fff;
  font:800 7.6pt Inter,sans-serif}
.jpn .jpn-pl{display:flex;justify-content:space-between;font-size:7pt;color:#5E686F;margin-top:1px}
.jpn .jpn-me>span{font-size:7.4pt;color:#4A555C}
"""

SHEET = {
    "slug": SLUG, "code": "ND-MS-602", "order": 13, "theme": "msk", "series": "Pain and Movement Series",
    "title": "Joint Pain and Osteoarthritis", "sub": "Knees, hips and hands",
    # [HUNTER19] most common arthritis, a whole-joint disease (cartilage, bone, lining).
    # [WHO23] 528 million people in 2019; knee most common, then hip and hand; about 73% over 55.
    "intro": ("Osteoarthritis (OA) is the most common kind of arthritis, and it changes the whole joint: the smooth "
              "<b>cartilage</b> on the ends of the bones thins and cracks, the bone underneath grows <b>spurs</b>, and "
              "the joint lining can swell. It shows up most in <b>knees, hips and hands</b> and affects about "
              "<b>528 million people</b> worldwide. Moving more, carrying less weight and the right nutrients help "
              "many people stay active."),
    "front": front,
    "css": CSS,
    "back": {
        "life_title": "Lifestyle Recommendations",
        "style": "circle",
        "life": [
            ("walk", "Move most days", "Moving feeds cartilage: walk, cycle or swim 150 minutes a week."),  # [FOX09] [CDC-PA] [ACR19]
            ("dumbbell", "Build strength", "Thigh and hip work 2 days a week takes load off the joint."),            # [CDC-PA] [OIESTAD15]
            ("scale", "Lighten the load", "Each pound lost takes about 4 pounds off your knees with every step."),   # [MESSIER05]
            ("breath", "Tai chi or yoga", "Slow, steady moves ease stiffness and build balance."),                     # [ACR19]
            ("fish", "Eat Mediterranean", "Fish, olive oil, beans, nuts and colorful plants. Fewer sugary drinks."),
            ("thermo", "Heat and support", "Warmth for stiffness, ice after a flare, a cane in the other hand."),     # [ACR19]
        ],
        "cols": [
            {"p": "jp_inflam_eze", "need": "Inflammatory balance", "needsub": "ginger, curcumin, boswellia", "start": True,
             "bullets": ["Supports a healthy inflammatory response", "Supports joint comfort and movement"],
             "dose": "dose_from_db"},
            {"p": "jp_chondro_ic", "need": "Building blocks", "needsub": "glucosamine and chondroitin",
             "bullets": ["Raw materials for cartilage and joint fluid", "Supports joint structure and flexibility"],
             "dose": "dose_from_db"},
            {"p": "jp_joint_eze", "need": "Joint comfort", "needsub": "UC-II undenatured collagen",
             "bullets": ["UC-II, studied at 40 mg a day for knee comfort", "Supports mobility and flexibility"],
             "dose": "dose_from_db"},
            {"p": "jp_collagen_renew", "need": "Collagen support", "needsub": "collagen peptides",
             "bullets": ["Supports cartilage, tendon and ligament structure", "Pair it with a vitamin C food, like an orange"],
             "dose": "dose_from_db"},
            # label: one softgel up to three times daily with food; 2 at one meal stays inside it
            {"p": "omega_1000", "need": "Balance fats", "needsub": "omega-3 EPA and DHA",
             "bullets": ["Supports a healthy inflammatory response", "Supports joint comfort and heart health"],
             "dose": "2 softgels daily", "dosesub": "with your evening meal", "sched": [("pm", 2, "softgels")]},
        ],
        "rx": {
            "practitioner": [
                "<b>On a blood thinner?</b> Fish oil, curcumin, ginger, willow and glucosamine can add to bleeding: "
                "ask {who} first.",
                "<b>Willow bark is aspirin's cousin.</b> Skip Inflam-Eze Plus with an aspirin allergy; ask before adding "
                "ibuprofen or naproxen.",
                "<b>Shellfish allergy?</b> Chondro-Relief Intensive Care has green-lipped mussel. <b>Pregnant or "
                "nursing?</b> Skip Joint Eze.",
            ],
            "pharmacy": [
                "<b>On a blood thinner?</b> Fish oil, curcumin, ginger, willow and glucosamine can add to bleeding: "
                "ask {who} first.",
                "<b>Willow works like mild aspirin:</b> skip it with an aspirin allergy; do not stack it with aspirin, "
                "ibuprofen or naproxen.",
                "<b>Shellfish allergy?</b> Chondro-Relief Intensive Care has green-lipped mussel. <b>Pregnant or "
                "nursing?</b> Skip Joint Eze.",
            ],
        },
    },
}
