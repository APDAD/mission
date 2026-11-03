"""Nerve Pain and Neuropathy (ND-NR-701), Brain and Nerve Series.  Slug "neuropathy".

Self-contained sheet module (no legacy / sheets.py / art.py drawing code).
FRONT, top to bottom:
  intro -> one picture in two halves:
    left  "WHERE YOU FEEL IT": a standing figure with the spinal cord and nerves in yellow and
          the "stocking and glove" zones shaded blue (feet first, then hands);
    right "INSIDE ONE NERVE FIBER": a healthy myelinated fiber (signal jumps gap to gap) above a
          damaged one (frayed coat, thinned and broken fiber, oxidative-stress sparks, extra glucose);
    one KEY under both halves names every symbol and colour.
  -> "What you may feel" + "Common causes" cards
  -> "Ask for these checks" (A1c, B12 + MMA, thyroid, yearly foot test) + a get-help-now strip.
BACK: lifestyle band, five NutriDyn columns (label facts in products.py / products.d/neuropathy.json),
daily rhythm and three Pharmacist / Provider checks.
Every SVG id starts "nrp-" and every CSS class ".nrp", so nothing collides in the all-sheets bundle.

SOURCES (each number or fact on the page carries one of these tags in a comment)
  [NINDS]   NINDS Peripheral Neuropathy fact sheet (2025-05): "more than 20 million people in the
            United States have been estimated to have some form of peripheral neuropathy";
            "diabetes is the leading cause of polyneuropathy in the United States".
  [ADA17]   Pop-Busui R et al. Diabetic Neuropathy: a position statement by the American Diabetes
            Association. Diabetes Care 2017;40:136-154. PMID 27999003, doi:10.2337/dc16-2042.
            DSPN in 10-15% of newly diagnosed type 2 diabetes, "rates increasing to 50% after 10 years";
            "oxidative and inflammatory stress may, in the context of metabolic dysfunction, damage
            nerve cells"; typical pattern "starting distally (the dorsal aspect of the hallux) on both
            sides and move proximally"; linked to "height (perhaps as a proxy for nerve length),
            smoking"; pain "burning, lancinating, tingling, or shooting (electric shock-like) ...
            typically worse at night", touch of "socks, shoes, and bedclothes"; large fibres:
            "numbness, tingling, poor balance"; "a major contributor to falls"; "the most important
            cause of foot ulceration"; "up to half of the patients may be asymptomatic"; exclude other
            causes with "serum B12, folic acid, thyroid function, complete blood count, metabolic panel,
            and a serum protein immunoelectrophoresis"; "annual 10-g monofilament testing"; atypical
            features (rapid onset, asymmetry, motor > sensory) need further work-up; non-diabetic causes
            table: HIV, hepatitis B, Lyme, CIDP, B12, pyridoxine, thiamine, alcohol, amiodarone,
            colchicine, vinca alkaloids, platinum, taxanes, arsenic, mercury, hereditary.
  [AAN09]   England JD et al. Practice Parameter: evaluation of distal symmetric polyneuropathy: role of
            laboratory and genetic testing. Neurology 2009;72:185-192. PMID 19056666,
            doi:10.1212/01.wnl.0000336370.51010.a1. Highest-yield tests: blood glucose, serum B12 with
            metabolites (methylmalonic acid +/- homocysteine), serum protein immunofixation; consider a
            glucose tolerance test when routine glucose is not diagnostic.
  [ADA26]   American Diabetes Association. Standards of Care in Diabetes-2026: 2. Diagnosis and
            Classification (A1C <5.7% normal, 5.7-6.4% prediabetes, >=6.5% diabetes); 9. Pharmacologic
            Approaches (B12 monitoring with long-term metformin); 12. Retinopathy, Neuropathy, and Foot
            Care (PMID 41358886, doi:10.2337/dc26-S012).
  [AROD16]  Aroda VR et al. Long-term metformin use and vitamin B12 deficiency in the DPP Outcomes Study.
            J Clin Endocrinol Metab 2016;101:1754-61. PMID 26900641, doi:10.1210/jc.2015-3754.
  [LAM13]   Lam JR et al. PPI and H2 blocker use and vitamin B12 deficiency. JAMA 2013;310:2435-42.
            PMID 24327038, doi:10.1001/jama.2013.280490.
  [EFSA23]  EFSA NDA Panel. Tolerable upper intake level for vitamin B6. EFSA J 2023;21:e08006.
            PMID 37207271: excess B6 -> peripheral neuropathy "is well established"; adult UL 12 mg/day.
  Product evidence (kept to comments; the back page stays structure/function):
  [HSIEH23] Hsieh RY et al. Nutrients 2023;15:3634. PMID 37630823: oral ALA, 10 RCTs, 1,242 patients,
            dose-related symptom improvement (600-1,800 mg/day).
  [PRADO24] Prado MB, Adiao KJB. Can J Diabetes 2024;48:233. PMID 38295879: ALA 600 mg/day vs placebo.
  [VINA25]  Vina I, Lopez-Moreno M. Nutr Rev 2025;83:e1604. PMID 39798151: PEA, 18 RCTs, neuropathic
            pain SMD -0.97.  [LANG23] Lang-Illievich K et al. Nutrients 2023;15:1350. PMID 36986081.
  [LEWIS17] Lewis EJH et al. Neurology 2017;88:2294. PMID 28515269: 12 months of omega-3, corneal nerve
            fibre length +29% in type 1 diabetes (open-label pilot).
  [FONS13]  Fonseca VA et al. Metanx in type 2 diabetes with peripheral neuropathy. Am J Med 2013;126:141-9.
            PMID 23218892: L-methylfolate 3 mg + methylcobalamin 2 mg + P5P 35 mg, 24 weeks, improved symptom
            scores (NTSS-6) and lowered homocysteine vs placebo.
  Alpha-Lipoic Acid R270 (200 mg, SS ND283) was the planned fifth column, but the only photo on hand
  (products/img/R270.png) shows the Progressive Professional 60-capsule ALA bottle (P872, panel not found),
  so Methyl Complete took its place; Nerve Eze + Gluco IR still give 600 mg ALA a day.
"""
import math
import os
import random

from kit import ICONS, icon
from svgkit import T, svg

SLUG = "neuropathy"

# ============================================================== text measuring (Inter, via Pillow)
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
    """Advance width of `text` in Inter at `size` px (generous guess without Pillow or the font)."""
    try:
        w = _face(_WEIGHTS[weight]).getlength(text) * size / 100
    except Exception:
        w = len(text) * size * (0.68 if text.isupper() else 0.6)
    return w + ls * len(text)


# ============================================================== palette (every colour is named in the KEY)
INK, INK2 = "#232B33", "#56616B"
NERVE, NERVE_HI, NERVE_LO, NERVE_EDGE = "#F2C14E", "#FFE9A6", "#D19A22", "#9C6C0E"   # nerve fiber (axon): yellow
MY_HI, MY_MID, MY_LO, MY_EDGE = "#FFFFFF", "#F8F2E4", "#E4D8BE", "#AE9F80"         # myelin coat: ivory white
SIGNAL = "#2E8B57"                         # nerve signal: green arrows
SPARK, SPARK_CORE = "#E0462B", "#FFD34D"   # oxidative stress ("rust"): red spark
GLU, GLU_EDGE = "#6B6FC2", "#45499A"       # extra blood sugar: purple hexagon (same purple as svgkit.GLUCOSE)
NUMB = "#3D7FD9"                           # numb or tingling area: blue shading
SKIN_EDGE = "#AEB8C6"                      # outline of the figure (neutral grey, not a colour code)
GREEN_HD, RED_HD = "#2F7D59", "#A3302A"    # card headers: healthy / damaged
CARD_BG, CARD_LN = "#F5F7FA", "#D2D9E2"

W = 760
TOP = 24                       # card tops (titles sit above, in clear space)
A_X0, A_X1 = 0, 246            # left card
B_X0, B_X1 = 258, 760          # right cards
B_H, GAP = 130, 10             # each fiber card
HDR = 24                       # fiber-card header band
CAP = 24                       # fiber-card caption strip
A_Y1 = TOP + 2 * B_H + GAP     # bottom of the left card (= bottom of the damaged card)
KEY_Y, KEY_H = A_Y1 + 8, 46
H = KEY_Y + KEY_H + 2


# ============================================================== shared defs
def nrp_defs():
    return ('<defs>'
            '<linearGradient id="nrp-ax" x1="0" y1="0" x2="0" y2="1">'
            f'<stop offset="0" stop-color="{NERVE_HI}"/><stop offset=".45" stop-color="{NERVE}"/>'
            f'<stop offset="1" stop-color="{NERVE_LO}"/></linearGradient>'
            '<linearGradient id="nrp-my" x1="0" y1="0" x2="0" y2="1">'
            f'<stop offset="0" stop-color="{MY_HI}"/><stop offset=".5" stop-color="{MY_MID}"/>'
            f'<stop offset="1" stop-color="{MY_LO}"/></linearGradient>'
            '<linearGradient id="nrp-myd" x1="0" y1="0" x2="0" y2="1">'
            '<stop offset="0" stop-color="#FCF8EE"/><stop offset=".5" stop-color="#F1E8D3"/><stop offset="1" stop-color="#D9CBAA"/>'
            '</linearGradient>'
            '<radialGradient id="nrp-face" cx=".5" cy=".5" r=".5">'
            f'<stop offset="0" stop-color="{MY_MID}"/><stop offset="1" stop-color="#EFE5CF"/></radialGradient>'
            '<radialGradient id="nrp-axf" cx=".42" cy=".38" r=".7">'
            f'<stop offset="0" stop-color="{NERVE_HI}"/><stop offset="1" stop-color="{NERVE}"/></radialGradient>'
            '<linearGradient id="nrp-skin" x1="0" y1="0" x2="1" y2="0">'
            f'<stop offset="0" stop-color="#DCE2EA"/><stop offset=".5" stop-color="#EEF1F5"/><stop offset="1" stop-color="#DCE2EA"/>'
            '</linearGradient>'
            '<linearGradient id="nrp-sock" x1="0" y1="1" x2="0" y2="0">'
            f'<stop offset="0" stop-color="{NUMB}" stop-opacity=".95"/><stop offset=".35" stop-color="{NUMB}" stop-opacity=".78"/>'
            f'<stop offset=".75" stop-color="{NUMB}" stop-opacity=".32"/><stop offset="1" stop-color="{NUMB}" stop-opacity="0"/></linearGradient>'
            '<linearGradient id="nrp-glove" x1="0" y1="1" x2="0" y2="0">'
            f'<stop offset="0" stop-color="{NUMB}" stop-opacity=".85"/><stop offset=".55" stop-color="{NUMB}" stop-opacity=".55"/>'
            f'<stop offset="1" stop-color="{NUMB}" stop-opacity="0"/></linearGradient>'
            '<linearGradient id="nrp-numbsw" x1="0" y1="1" x2="0" y2="0">'
            f'<stop offset="0" stop-color="{NUMB}" stop-opacity=".9"/><stop offset="1" stop-color="{NUMB}" stop-opacity=".25"/></linearGradient>'
            '<marker id="nrp-ar" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="4.4" markerHeight="4.4" '
            f'orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="{SIGNAL}"/></marker>'
            '</defs>')


# ============================================================== the figure (left card)
def _spline(pts, closed=True):
    """Catmull-Rom curve through (x, y, tension) points as cubic Bezier path data."""
    n = len(pts)
    tan = []
    for i in range(n):
        if closed:
            (x0, y0, _), (_, _, k), (x2, y2, _) = pts[i - 1], pts[i], pts[(i + 1) % n]
        else:
            (x0, y0, _) = pts[max(i - 1, 0)]
            (_, _, k) = pts[i]
            (x2, y2, _) = pts[min(i + 1, n - 1)]
        tan.append((k * (x2 - x0) / 2, k * (y2 - y0) / 2))
    d = [f"M{pts[0][0]:.2f},{pts[0][1]:.2f}"]
    last = n if closed else n - 1
    for i in range(last):
        j = (i + 1) % n
        (xa, ya, _), (xb, yb, _) = pts[i], pts[j]
        d.append(f"C{xa + tan[i][0] / 3:.2f},{ya + tan[i][1] / 3:.2f} "
                 f"{xb - tan[j][0] / 3:.2f},{yb - tan[j][1] / 3:.2f} {xb:.2f},{yb:.2f}")
    return "".join(d) + ("Z" if closed else "")


def _offset(center):
    """Outer and inner edges of a limb from its centre line [(x, y, half_width)]."""
    outer, inner = [], []
    n = len(center)
    for i, (x, y, hw) in enumerate(center):
        xa, ya, _ = center[max(i - 1, 0)]
        xb, yb, _ = center[min(i + 1, n - 1)]
        dx, dy = xb - xa, yb - ya
        m = math.hypot(dx, dy) or 1
        nx, ny = dy / m, -dx / m                     # points outward (+x) for a limb running down
        outer.append((x + nx * hw, y + ny * hw))
        inner.append((x - nx * hw, y - ny * hw))
    return outer, inner


# Right half of a standing figure in anatomical position (palms forward, thumbs out), figure units:
# centre line x = 0, top of head y = 0, soles y = 300, head height 37.5 (8 heads), shoulders 1.85
# heads wide, hips 1.55, crotch at 4 heads, knees near 5.9, fingertips at mid-thigh.
_ARM_C = [(32.6, 64, 7.4), (36.0, 87, 6.5), (39.4, 109, 5.4), (42.6, 127, 5.8), (45.6, 145, 4.2)]
_LEG_C = [(15.2, 156, 13.9), (16.0, 184, 11.8), (16.2, 218, 7.6), (16.2, 243, 8.9), (13.2, 268, 6.6), (11.2, 286, 5.2)]


def _half():
    ao, ai = _offset(_ARM_C)
    lo, li = _offset(_LEG_C)
    k = lambda pts, t=1: [(x, y, t) for x, y in pts]
    pts = [(0, 0, 1), (8.5, 1.9, 1), (12.4, 7.9, 1), (13.2, 15.4, 1), (12.6, 23.4, 1), (10.6, 30.4, 1),
           (7.5, 35.4, .8), (6.1, 39.2, .7),                                   # head, jaw
           (5.9, 43.4, .9), (6.9, 47.4, .8), (11.8, 50.4, 1), (21.6, 52.9, 1), (30.4, 55.6, 1),
           (35.8, 59.2, 1), (39.0, 65.4, 1)]                                   # neck, shoulder slope, deltoid
    pts += k(ao[1:])                                                           # outer arm
    w = ao[-1]
    pts += [(w[0] + 2.8, w[1] + 5.2, .8), (w[0] + 6.0, w[1] + 10.6, .9), (w[0] + 6.4, w[1] + 16.0, .8),
            (w[0] + 4.2, w[1] + 17.6, .45),                                    # thumb
            (w[0] + 4.4, w[1] + 23.2, .9), (w[0] + 3.4, w[1] + 30.0, 1), (w[0] + .2, w[1] + 33.4, 1),
            (w[0] - 3.4, w[1] + 32.4, 1), (w[0] - 5.4, w[1] + 25.6, 1), (w[0] - 6.4, w[1] + 13.2, 1)]   # fingers, palm
    pts += k(list(reversed(ai))[:-1])                                          # inner arm up
    pts += [(29.9, 80.5, .3)]                                                  # armpit
    pts += [(29.4, 90, 1), (28.0, 100, 1), (25.9, 110, 1), (25.4, 116, 1), (26.9, 127, 1), (28.9, 138, 1),
            (29.6, 147, 1)]                                                    # torso side, waist, hip
    pts += k(lo[1:])                                                           # outer leg
    a = lo[-1]
    pts += [(a[0] + 2.0, a[1] + 4.6, .9), (a[0] + 4.4, a[1] + 9.6, .85), (a[0] + 3.4, a[1] + 13.4, .75),
            (13.0, 300.6, 1), (5.6, 300.0, .8), (3.4, 296.2, .9), (4.4, 291.2, .9)]   # foot, front view
    pts += k(list(reversed(li))[:-1])                                          # inner leg up
    pts += [(3.2, 166, 1), (0, 153, .3)]                                       # inner thigh, crotch
    return pts


def _body_outline():
    right = _half()
    left = [(-x, y, k) for (x, y, k) in reversed(right[1:-1])]
    return _spline(right + left)


def _mirror(d_pts):
    return [(-x, y) for x, y in d_pts]


def _poly(pts):
    """Smooth open path through (x, y) points."""
    return _spline([(x, y, 1) for x, y in pts], closed=False)


# nerve paths on the figure's right side (mirrored for the left), figure units: the spinal cord,
# one trunk down each arm (branching to thumb and fingers) and down each leg (the sciatic nerve,
# splitting near the knee into the tibial and peroneal nerves that reach the toes)
_CORD = [(0, 33), (0, 62), (0, 96), (0, 124)]
_ARM = [(1.0, 50.5), (12.4, 54.6), (24.6, 61.4), (31.4, 73.5), (34.8, 90), (38.2, 110), (41.8, 128), (45.2, 145.5)]
_HAND = [[(45.2, 145.5), (48.6, 157), (50.6, 168), (51.0, 175.5)],
         [(45.2, 145.5), (46.0, 158), (46.4, 170), (46.8, 177.5)],
         [(46.2, 149.5), (50.4, 155), (53.0, 160.6)],
         [(45.6, 152), (43.6, 164), (42.6, 172.5)]]
_LEG = [(0.8, 122), (5.6, 135), (11.8, 151), (15.0, 174), (16.0, 198), (16.2, 216)]
_TIB = [(16.2, 216), (14.8, 240), (12.6, 264), (10.8, 283), (10.4, 292)]
_PER = [(16.2, 216), (19.6, 230), (18.0, 252), (15.6, 275), (14.8, 288)]
_TOES = [[(10.4, 292), (7.6, 297.8)], [(10.4, 292), (11.8, 298.6)], [(14.8, 288), (16.6, 297.4)]]


def _nerve(pts, w):
    d = _poly(pts)
    return (f'<path d="{d}" fill="none" stroke="{NERVE_EDGE}" stroke-width="{w + 1.15:.2f}" stroke-linecap="round" '
            f'stroke-linejoin="round"/><path d="{d}" fill="none" stroke="{NERVE}" stroke-width="{w:.2f}" '
            'stroke-linecap="round" stroke-linejoin="round"/>')


def figure(cx, top, s):
    """The standing figure, its nerves and the stocking-and-glove shading, at scale s."""
    body = _body_outline()
    o = [f'<g transform="translate({cx},{top}) scale({s})">',
         f'<clipPath id="nrp-body"><path d="{body}"/></clipPath>',
         f'<path d="{body}" fill="url(#nrp-skin)" stroke="{SKIN_EDGE}" stroke-width="{1.3 / s:.2f}" stroke-linejoin="round"/>',
         '<g clip-path="url(#nrp-body)">',
         # stocking: soles up to mid-calf; glove: fingertips to the wrist (x-limited so the thighs stay clear)
         '<rect x="-40" y="226" width="80" height="78" fill="url(#nrp-sock)"/>',
         '<rect x="36" y="146" width="26" height="33.5" fill="url(#nrp-glove)"/>',
         '<rect x="-62" y="146" width="26" height="33.5" fill="url(#nrp-glove)"/>',
         '</g>']
    # brain (soft, inside the skull) and spinal cord, then the nerves
    o.append(f'<path d="M0,6.4 C5.6,6.4 8.6,9.6 8.6,13.6 C8.6,17.8 5.8,20.4 2.2,21.2 L1.4,33 H-1.4 L-2.2,21.2 '
             f'C-5.8,20.4 -8.6,17.8 -8.6,13.6 C-8.6,9.6 -5.6,6.4 0,6.4Z" fill="#FBE5A8" stroke="{NERVE_EDGE}" '
             f'stroke-width="{0.9 / s:.2f}" stroke-opacity=".75"/>')
    o.append(f'<path d="M0,7.4 V20.4 M-4.2,9.2 C-2.8,11.4 -3,14.2 -5,16.4 M4.2,9.2 C2.8,11.4 3,14.2 5,16.4" fill="none" '
             f'stroke="{NERVE_EDGE}" stroke-width="{0.7 / s:.2f}" stroke-opacity=".5"/>')
    o.append(_nerve(_CORD, 2.4))
    for side in (1, -1):
        f = (lambda pts: pts) if side == 1 else _mirror
        o.append(_nerve(f(_ARM), 1.45))
        for h in _HAND:
            o.append(_nerve(f(h), .8))
        o.append(_nerve(f(_LEG), 1.8))
        o.append(_nerve(f(_TIB), 1.2))
        o.append(_nerve(f(_PER), 1.0))
        for tpts in _TOES:
            o.append(_nerve(f(tpts), .8))
    o.append("</g>")
    return "".join(o)


def card_a():
    x0, x1, y0, y1 = A_X0, A_X1, TOP, A_Y1
    s, fcx, ftop = 0.8, 70, TOP + 11
    P = lambda fx, fy: (fcx + fx * s, ftop + fy * s)      # figure units -> svg
    o = [f'<rect x="{x0 + .6}" y="{y0 + .6}" width="{x1 - x0 - 1.2}" height="{y1 - y0 - 1.2}" rx="12" fill="{CARD_BG}" '
         f'stroke="{CARD_LN}" stroke-width="1.2"/>',
         figure(fcx, ftop, s)]

    def callout(fx, fy, lx, num, lines):
        """Dashed leader from a point on the figure to a label; a numbered badge sits on the leader's line,
        an un-numbered label block is centred on it."""
        ax, ay = P(fx, fy)
        out = [f'<path d="M{ax:.1f},{ay:.1f} H{lx - 13:.1f}" stroke="#7D8894" stroke-width="1.1" stroke-dasharray="2.5 2.5"/>',
               f'<circle cx="{ax:.1f}" cy="{ay:.1f}" r="2.4" fill="#7D8894"/>']
        if num:
            out.append(f'<circle cx="{lx - 2:.1f}" cy="{ay:.1f}" r="8.2" fill="{NUMB}"/>'
                       + T(round(lx - 2, 1), round(ay + 3.8, 1), str(num), 10.5, 800, "#FFFFFF", "middle"))
            out.append(T(lx + 10, round(ay + 4, 1), lines, 11.5, 700, INK, lh=1.2))
        else:
            first = ay + 3.9 - (len(lines) - 1) * 11 * 1.22 / 2
            out.append(T(lx - 9, round(first, 1), lines, 11, 600, INK2, lh=1.22))
        return "".join(out)

    o.append(callout(52.4, 166, 150, 2, ["Then hands,", "like gloves"]))
    o.append(callout(20.4, 280, 150, 1, ["Feet first,", "like socks"]))
    o.append(callout(36.6, 92, 160, 0, ["Nerves run from", "the spinal cord", "to your toes and", "fingertips"]))
    return "".join(o)


# ============================================================== nerve fibers (right cards)
def _myelin_seg(xa, xb, cy, ra, rm, taper=11):
    """One internode of myelin: a capsule that tapers into the axon at both nodes."""
    t = min(taper, (xb - xa) / 2.2)
    top = (f"M{xa:.1f},{cy - ra - .4:.1f} C{xa:.1f},{cy - rm + 3:.1f} {xa + t * .35:.1f},{cy - rm:.1f} {xa + t:.1f},{cy - rm:.1f} "
           f"H{xb - t:.1f} C{xb - t * .35:.1f},{cy - rm:.1f} {xb:.1f},{cy - rm + 3:.1f} {xb:.1f},{cy - ra - .4:.1f} ")
    bot = (f"V{cy + ra + .4:.1f} C{xb:.1f},{cy + rm - 3:.1f} {xb - t * .35:.1f},{cy + rm:.1f} {xb - t:.1f},{cy + rm:.1f} "
           f"H{xa + t:.1f} C{xa + t * .35:.1f},{cy + rm:.1f} {xa:.1f},{cy + rm - 3:.1f} {xa:.1f},{cy + ra + .4:.1f} Z")
    d = top + bot
    wraps = []
    x = xa + t + 2
    while x < xb - t - 4:          # the wrap: myelin is a sheet rolled around the fiber many times
        wraps.append(f"M{x:.1f},{cy - rm + 1.2:.1f} L{x + 5.5:.1f},{cy + rm - 1.2:.1f}")
        x += 7.5
    return (f'<path d="{d}" fill="url(#nrp-my)" stroke="{MY_EDGE}" stroke-width="1.15"/>'
            + (f'<path d="{" ".join(wraps)}" stroke="#D9CCB0" stroke-width=".9" opacity=".55"/>' if wraps else "")
            + f'<path d="M{xa + t:.1f},{cy - rm + 3.2:.1f} H{xb - t:.1f}" stroke="#FFFFFF" stroke-width="2.2" '
              'stroke-linecap="round" opacity=".9"/>')


def _axon(xa, xb, cy, ra):
    return (f'<rect x="{xa:.1f}" y="{cy - ra:.1f}" width="{xb - xa:.1f}" height="{2 * ra:.1f}" fill="url(#nrp-ax)" '
            f'stroke="{NERVE_EDGE}" stroke-width=".9"/>')


def _cut_face(x, cy, ra, rm, k=.42, rings=4, broken=False):
    """The cut end of the myelin coat (concentric wraps) with the fiber through its centre."""
    o = [f'<ellipse cx="{x}" cy="{cy}" rx="{rm * k:.1f}" ry="{rm}" fill="url(#nrp-face)" stroke="{MY_EDGE}" stroke-width="1.15"/>']
    for i in range(1, rings + 1):
        r = ra + (rm - ra) * i / (rings + 1)
        dash = ' stroke-dasharray="3 2.6"' if broken else ""
        o.append(f'<ellipse cx="{x}" cy="{cy}" rx="{r * k:.1f}" ry="{r:.1f}" fill="none" stroke="#CDBD9B" '
                 f'stroke-width=".85"{dash}/>')
    return "".join(o)


def _axon_stub(x_face, x_end, cy, ra, k=.42):
    """Fiber poking out past the cut coat, ending in its own round face (the cable-end view)."""
    return (f'<rect x="{x_end:.1f}" y="{cy - ra:.1f}" width="{x_face - x_end:.1f}" height="{2 * ra:.1f}" fill="url(#nrp-ax)"/>'
            f'<path d="M{x_end:.1f},{cy - ra:.1f} H{x_face:.1f} M{x_end:.1f},{cy + ra:.1f} H{x_face:.1f}" '
            f'stroke="{NERVE_EDGE}" stroke-width=".9"/>'
            f'<ellipse cx="{x_end:.1f}" cy="{cy}" rx="{ra * k:.1f}" ry="{ra}" fill="url(#nrp-axf)" stroke="{NERVE_EDGE}" stroke-width=".9"/>')


def spark(x, y, r=7.5, rot=0):
    """Oxidative stress ('rust'): an eight-point red spark with a hot core."""
    pts = []
    for i in range(16):
        a = math.radians(rot + i * 22.5)
        rr = r if i % 2 == 0 else r * .42
        pts.append(f"{x + rr * math.cos(a):.1f},{y + rr * math.sin(a):.1f}")
    return (f'<polygon points="{" ".join(pts)}" fill="{SPARK}" stroke="#A82A16" stroke-width=".7" stroke-linejoin="round"/>'
            f'<circle cx="{x}" cy="{y}" r="{r * .26:.1f}" fill="{SPARK_CORE}"/>')


def glucose(x, y, r=5.4):
    pts = " ".join(f"{x + r * c:.1f},{y + r * s:.1f}" for c, s in
                   ((1, 0), (.5, .866), (-.5, .866), (-1, 0), (-.5, -.866), (.5, -.866)))
    return f'<polygon points="{pts}" fill="{GLU}" stroke="{GLU_EDGE}" stroke-width="1" stroke-linejoin="round"/>'


def _card_frame(x0, y0, w, h, head, sub, hcol, cap):
    cid = f"nrp-cc{int(y0)}"
    return (f'<clipPath id="{cid}"><rect x="{x0}" y="{y0}" width="{w}" height="{h}" rx="12"/></clipPath>',
            f'<g clip-path="url(#{cid})"><rect x="{x0}" y="{y0}" width="{w}" height="{h}" fill="#FFFFFF"/>'
            f'<rect x="{x0}" y="{y0 + HDR}" width="{w}" height="{h - HDR - CAP}" fill="#EEF2F7"/>'
            f'<rect x="{x0}" y="{y0}" width="{w}" height="{HDR}" fill="{hcol}"/>'
            + T(x0 + 14, y0 + 16.5, head, 12.5, 900, "#FFFFFF", ls=.8)
            + T(x0 + w - 14, y0 + 16.3, sub, 10.5, 600, "#FFFFFF", "end", italic=True)
            + f'<rect x="{x0}" y="{y0 + h - CAP}" width="{w}" height="{CAP}" fill="#FFFFFF"/>'
            + f'<path d="M{x0},{y0 + h - CAP} H{x0 + w}" stroke="#E1E6EC" stroke-width="1"/>'
            + T(x0 + 14, y0 + h - 8, cap, 11, 600, INK),
            f'<rect x="{x0 + .6}" y="{y0 + .6}" width="{w - 1.2}" height="{h - 1.2}" rx="12" fill="none" '
            f'stroke="{CARD_LN}" stroke-width="1.2"/>')


def card_healthy():
    x0, y0, w, h = B_X0, TOP, B_X1 - B_X0, B_H
    clip, frame, border = _card_frame(x0, y0, w, h, "HEALTHY NERVE", "signals travel fast and clear", GREEN_HD,
                                      "A thick coat (myelin) wraps the fiber, so signals jump fast from gap to gap.")
    cy = y0 + HDR + (h - HDR - CAP) / 2 + 9
    ra, rm = 8.0, 20.0
    cut = x0 + 48
    segs, x, L, g = [], cut, 84, 7
    first = 76
    segs.append((cut, cut + first))
    x = cut + first + g
    while x < x0 + w - 12:
        segs.append((x, min(x + L, x0 + w + 1)))
        x += L + g
    nodes = [(a + b) / 2 for a, b in zip([s[1] for s in segs[:-1]], [s[0] for s in segs[1:]])]
    o = [clip, frame, _axon(cut, x0 + w + 1, cy, ra)]
    for a, b in segs:
        o.append(_myelin_seg(a, b, cy, ra, rm))
    o.append(_cut_face(cut, cy, ra, rm))
    o.append(_axon_stub(cut, cut - 20, cy, ra))
    # the signal: a pulse at each gap (node) and arcs that leap from gap to gap
    for nx in nodes[:4]:
        o.append(f'<circle cx="{nx:.1f}" cy="{cy}" r="6.5" fill="{SIGNAL}" opacity=".28"/>'
                 f'<circle cx="{nx:.1f}" cy="{cy}" r="2.6" fill="{SIGNAL}"/>')
    for a, b in zip(nodes[:3], nodes[1:4]):
        top = cy - rm - 19
        o.append(f'<path d="M{a + 2:.1f},{cy - rm - 2:.1f} C{a + 22:.1f},{top:.1f} {b - 24:.1f},{top:.1f} {b - 3:.1f},{cy - rm - 4:.1f}" '
                 f'fill="none" stroke="{SIGNAL}" stroke-width="2.4" stroke-linecap="round" marker-end="url(#nrp-ar)"/>')
    o.append("</g>")
    o.append(border)
    return "".join(o)


def _tube(xa, xb, cy, rtop, rbot, step=1.6):
    """Closed tube outline from xa to xb whose top and bottom radii follow rtop(x) and rbot(x)."""
    n = max(2, int((xb - xa) / step))
    xs = [xa + (xb - xa) * i / n for i in range(n + 1)]
    top = " L".join(f"{x:.1f},{cy - rtop(x):.1f}" for x in xs)
    bot = " L".join(f"{x:.1f},{cy + rbot(x):.1f}" for x in reversed(xs))
    return f"M{top} L{bot}Z"


def _worn(xa, xb, ra, rm, notches_top, notches_bot, seed):
    """Radius functions for a worn-down internode: thin, uneven, with bites taken out of the coat."""
    rnd = random.Random(seed)
    wob = [(rnd.uniform(0, 6.28), rnd.uniform(.25, .5)) for _ in range(3)]
    t = min(9, (xb - xa) / 3)

    def make(notches):
        def r(x):
            e = max(0.0, min(1.0, (x - xa) / t, (xb - x) / t))
            base = ra + .3 + (rm - ra - .3) * (math.sin(e * math.pi / 2) ** .9)
            base += sum(a * math.sin(x / (5 + i * 3.1) + ph) for i, (ph, a) in enumerate(wob)) * e
            for xc, depth, wd in notches:
                base -= depth * math.exp(-((x - xc) / wd) ** 2)
            return max(ra + .3, base)
        return r
    return make(notches_top), make(notches_bot)


def card_damaged():
    x0, y0, w, h = B_X0, TOP + B_H + GAP, B_X1 - B_X0, B_H
    clip, frame, border = _card_frame(x0, y0, w, h, "DAMAGED NERVE", "signals slow, misfire or stop", RED_HD,
                                      "High sugar, low B12 and “rust” (oxidative stress) wear down the coat and the fiber.")
    cy = y0 + HDR + (h - HDR - CAP) / 2 + 2
    ra, rm = 5.4, 13.6
    cut = x0 + 48
    brk = x0 + 402
    o = [clip, frame]
    # the fiber: thinner, with beaded (swollen and pinched) bare stretches, then broken into pieces
    def r_ax(x):
        if x < x0 + 190 or (x0 + 282 < x < x0 + 336):
            return ra
        return ra * (1 + .2 * math.sin((x - x0) / 6.2)) * (1 - .25 * math.exp(-((x - (x0 + 372)) / 12) ** 2))
    o.append(f'<path d="{_tube(cut, brk, cy, r_ax, r_ax)}" fill="url(#nrp-ax)" stroke="{NERVE_EDGE}" stroke-width=".9" '
             'stroke-linejoin="round"/>')
    o.append(f'<path d="M{brk:.1f},{cy - r_ax(brk):.1f} l2.6,2.2 -2.2,2.1 2.8,2.2 -2.4,2.1 2.2,2.3" fill="none" '
             f'stroke="{NERVE_EDGE}" stroke-width=".9"/>')
    for bx, bw, rr in ((brk + 15, 22, .8), (brk + 45, 12, .72), (brk + 65, 7, .62)):
        o.append(f'<rect x="{bx:.1f}" y="{cy - ra * rr:.1f}" width="{bw}" height="{2 * ra * rr:.1f}" rx="{ra * rr:.1f}" '
                 f'fill="url(#nrp-ax)" stroke="{NERVE_EDGE}" stroke-width=".9"/>')
    # coat: three worn internodes with bites out of them, a wide gap and a stretch with no coat at all
    for (a, b), nt, nb, sd in (((cut, cut + 60), [(cut + 30, 4.2, 4)], [(cut + 44, 3.4, 3.5)], 3),
                               ((x0 + 124, x0 + 190), [(x0 + 146, 5.2, 4.5)], [(x0 + 168, 4.6, 4), (x0 + 136, 2.6, 3)], 5),
                               ((x0 + 282, x0 + 336), [(x0 + 318, 4.8, 4.2)], [(x0 + 296, 3.8, 3.6)], 9)):
        rt, rb = _worn(a, b, ra, rm, nt, nb, sd)
        o.append(f'<path d="{_tube(a, b, cy, rt, rb)}" fill="url(#nrp-myd)" stroke="{MY_EDGE}" stroke-width="1.05" '
                 'stroke-linejoin="round"/>')
    o.append(_cut_face(cut, cy, ra, rm, rings=3, broken=True))
    o.append(_axon_stub(cut, cut - 16, cy, ra))
    # the misfiring signal: one weak hop that never lands
    n1 = (cut + 60 + x0 + 124) / 2
    top = cy - rm - 17
    o.append(f'<circle cx="{n1:.1f}" cy="{cy}" r="2.4" fill="#8C959E"/>')
    o.append(f'<path d="M{n1 + 2:.1f},{cy - rm - 2:.1f} C{n1 + 20:.1f},{top:.1f} {n1 + 44:.1f},{top:.1f} {n1 + 56:.1f},{cy - rm - 9:.1f}" '
             'fill="none" stroke="#8C959E" stroke-width="2.2" stroke-dasharray="4 3.2" stroke-linecap="round"/>')
    xx, xy = n1 + 64, cy - rm - 8
    o.append(f'<path d="M{xx - 5},{xy - 5} l10,10 M{xx + 5},{xy - 5} l-10,10" stroke="{RED_HD}" stroke-width="2.6" '
             'stroke-linecap="round"/>')
    # oxidative stress sparks and extra glucose in the fluid around the fiber (kept off the signal arc)
    for x, y, r, rot in ((x0 + 100, cy + 23, 7.2, 14), (x0 + 236, cy + 23, 7.8, 20), (x0 + 252, cy - 26, 7.4, 4),
                         (x0 + 356, cy - 25, 7.0, 10), (x0 + 318, cy + 24, 6.6, 0), (x0 + 436, cy + 23, 7.4, 6)):
        o.append(spark(x, y, r, rot))
    for x, y in ((x0 + 74, cy - 26), (x0 + 214, cy - 27), (x0 + 302, cy - 27), (x0 + 412, cy - 24), (x0 + 472, cy - 25),
                 (x0 + 158, cy + 24), (x0 + 276, cy + 24), (x0 + 374, cy + 23), (x0 + 480, cy + 20)):
        o.append(glucose(x, y))
    o.append("</g>")
    o.append(border)
    return "".join(o)


# ============================================================== key strip
def _key():
    def sw_fiber():
        return (f'<rect x="-11" y="-4.2" width="22" height="8.4" rx="1" fill="url(#nrp-ax)" stroke="{NERVE_EDGE}" stroke-width=".9"/>'
                f'<ellipse cx="-11" cy="0" rx="1.8" ry="4.2" fill="url(#nrp-axf)" stroke="{NERVE_EDGE}" stroke-width=".8"/>')

    def sw_myelin():
        return _myelin_seg(-12, 12, 0, 3.2, 8.2, taper=6)

    def sw_signal():
        return (f'<path d="M-11,4 C-6,-7 4,-7 9,1" fill="none" stroke="{SIGNAL}" stroke-width="2.3" stroke-linecap="round" '
                'marker-end="url(#nrp-ar)"/>')

    def sw_numb():
        return f'<rect x="-8" y="-8" width="16" height="16" rx="3" fill="url(#nrp-numbsw)"/>'

    rows = [[(sw_fiber(), "Nerves and nerve fiber"), (sw_myelin(), "Myelin coat"),
             (sw_signal(), "Nerve signal")],
            [(spark(0, 0, 7.4), "Oxidative stress (“rust”)"), (glucose(0, 0, 6), "Extra blood sugar (glucose)"),
             (sw_numb(), "Numb or tingling area")]]
    y, h = KEY_Y, KEY_H
    start = 14 + tw("KEY", 10.5, 800, 1.2) + 24
    col_w = (W - 10 - start) / 3
    o = [f'<rect x=".6" y="{y}" width="{W - 1.2}" height="{h}" rx="8" fill="#FFFFFF" stroke="#CFD6DE" stroke-width="1.2"/>',
         T(14, y + h / 2 + 3.7, "KEY", 10.5, 800, INK, ls=1.2),
         f'<path d="M{start - 12:.1f},{y + 8} V{y + h - 8}" stroke="#DDE2E8" stroke-width="1.2"/>']
    for r, items in enumerate(rows):
        cy = y + 13 + r * 20
        for c, (sw, lab) in enumerate(items):
            x = start + c * col_w
            o.append(f'<g transform="translate({x + 12:.1f},{cy:.1f})">{sw}</g>')
            o.append(T(round(x + 31, 1), round(cy + 3.9, 1), lab, 11, 600, INK))
    return "".join(o)


def art_neuro(t):
    titles = (T(8, 15, "WHERE YOU FEEL IT", 12, 800, t["c1"], ls=1.0)
              + T(B_X0 + 8, 15, "INSIDE ONE NERVE FIBER", 12, 800, t["c1"], ls=1.0)
              + T(B_X0 + 8 + tw("INSIDE ONE NERVE FIBER", 12, 800, 1.0) + 8, 15, "magnified", 11, 600, INK2, italic=True))
    body = [nrp_defs(), titles, card_a(), card_healthy(), card_damaged(), _key()]
    return svg(W, H, "".join(body),
               "Left: a standing figure with the spinal cord and nerves in yellow; numb or tingling zones shaded blue "
               "on the feet and lower legs (first) and on the hands (later). Right: a healthy nerve fiber wrapped in a "
               "thick myelin coat, its signal jumping from gap to gap, above a damaged fiber with a frayed coat, a "
               "thinned and broken fiber, red oxidative-stress sparks and extra purple glucose, where the signal stops.")


# ============================================================== this sheet's icons (64 x 64, stroke style)
# Registered into kit.ICONS under "nrp-" names so the back page's lifestyle band can use them too.
NRP_ICONS = {
    "nrp-foot": ('<path d="M33.5 61C28.4 61 25.4 57.6 25.4 53c0-4.4 3.2-7.8 4.6-12 1-3.2-1.8-6.4-4.6-9.2-2.6-2.6-3.2-6.4-2-9.8 '
                 '1.6-4.4 6-6.8 10.8-6.8 6 0 10.4 3.6 10.4 9.4 0 5.8-1.6 10-1.8 15.8-.2 5.6 1.2 9.2.8 13.4-.4 4.4-4.2 7.2-10.1 7.2z"/>'
                 '<circle cx="26.4" cy="9.8" r="3.7"/><circle cx="33.2" cy="7.4" r="2.7"/><circle cx="38.6" cy="8.2" r="2.3"/>'
                 '<circle cx="43" cy="10.8" r="2"/><circle cx="46.2" cy="14.6" r="1.7"/>'),
    "nrp-shoe": ('<path d="M8 46.5V33c0-2.4 2.4-3.7 4.5-2.6l6.8 3.6c3.9 2.1 8.6 2 12.4-.3l2.6-1.6 9.6 6.8c2.9 2 6.3 3.1 9.8 3.1 '
                 '2.6 0 4.6 2 4.6 4.6v-.1z"/><path d="M5.5 46.5h53.5v3.6a3 3 0 0 1-3 3H8.5a3 3 0 0 1-3-3z"/>'
                 '<path d="M30.5 37.5l4.2-3.1M35.6 41l4.2-3.1M40.8 44.2l4.2-3.1"/>'),
    "nrp-sock": ('<path d="M21.5 5.5h19v8.5h-19z"/><path d="M21.5 14v19.5c0 3.2 1.3 6.1 3.6 8.2l12.6 11.6c3.7 3.4 9.4 3.2 '
                 '12.8-.5 3.4-3.7 3.2-9.4-.5-12.8L40.5 31V14"/><path d="M41 45.6c2.2-1.6 3.6-4 3.8-6.8"/>'),
    "nrp-tingle": ('<path d="M19 6.5l2.6 7.6 7.6 2.6-7.6 2.6-2.6 7.6-2.6-7.6-7.6-2.6 7.6-2.6z"/>'
                   '<path d="M44 20l2 5.8 5.8 2-5.8 2-2 5.8-2-5.8-5.8-2 5.8-2z"/>'
                   '<path d="M25 37l1.7 5 5 1.7-5 1.7-1.7 5-1.7-5-5-1.7 5-1.7z"/>'
                   '<circle cx="47" cy="50" r="2.2"/><circle cx="12" cy="36" r="1.8"/><circle cx="37.5" cy="9.5" r="1.8"/>'),
    "nrp-thyroid": ('<path d="M28.5 5v54M35.5 5v54M28.5 12h7M28.5 19h7M28.5 47h7M28.5 54h7"/>'
                    '<path d="M28.5 25.5c-3.6-6.4-13.6-8.6-17-2.6-3.4 6.2-.4 17.6 6.6 21.4 4.4 2.4 8.4.6 10.4-3.1z"/>'
                    '<path d="M35.5 25.5c3.6-6.4 13.6-8.6 17-2.6 3.4 6.2.4 17.6-6.6 21.4-4.4 2.4-8.4.6-10.4-3.1z"/>'
                    '<path d="M28.5 35h7"/>'),
    "nrp-b12": ('<rect x="7" y="15" width="50" height="34" rx="10"/><text x="32" y="39.6" text-anchor="middle" '
                'font-family="Inter, Arial, sans-serif" font-size="19" font-weight="800" fill="currentColor" stroke="none" '
                'letter-spacing="-.5">B12</text>'),
    "nrp-glass": ICONS["glass"].split('<path class="x"')[0],      # the glass without the "avoid" slash
}
for _k, _v in NRP_ICONS.items():
    ICONS.setdefault(_k, _v)


def _ed(x, ed):
    return x.replace("{who}", ed["who"]).replace("{Who}", ed["Who"])


# ============================================================== front page blocks
# [ADA17] pain "burning, lancinating, tingling, or shooting (electric shock-like) ... typically worse at night";
# large fibres "numbness, tingling, poor balance"; "a major contributor to falls"; "the most important cause of
# foot ulceration"; "up to half of the patients may be asymptomatic" (so: sometimes no signs at first).
# [NINDS] motor nerve damage: muscle weakness, painful cramps.
FEEL = [("flame", "<b>Burning</b> or sharp, electric jolts"),
        ("nrp-tingle", "<b>Tingling</b>, pins and needles"),
        ("nrp-sock", "<b>Numb</b>, as if wearing socks or gloves"),
        ("moon", "Often <b>worse at night</b>"),
        ("age", "<b>Poor balance</b>, stumbles and falls"),
        ("nrp-foot", "Cuts or blisters you <b>do not feel</b>"),
        ("dumbbell", "<b>Weak</b> muscles or cramps"),
        ("stethoscope", "Sometimes <b>no signs</b> at first")]

# [NINDS] diabetes is the leading cause; [ADA17] prediabetes too (10-30% with impaired glucose tolerance), and the
# non-diabetic causes table (B12, alcohol, chemotherapy drugs: vinca alkaloids, platinum, taxanes; amiodarone,
# colchicine; HIV, hepatitis B, Lyme; CIDP; hereditary) + work-up incl. thyroid function [ADA17, AAN09];
# [AROD16] long-term metformin and [LAM13] acid blockers lower B12; kidney disease per NINDS.
CAUSES = [("meter", "<b>High blood sugar:</b> diabetes or prediabetes", True),
          ("nrp-b12", "<b>Low vitamin B12</b>, as with metformin or acid blockers", False),
          ("nrp-glass", "<b>Heavy alcohol</b> use", False),
          ("rx", "<b>Chemotherapy</b> and some other medicines", False),
          ("nrp-thyroid", "<b>Low thyroid</b> (hypothyroidism)", False),
          ("kidney", "<b>Kidney disease</b>", False),
          ("microbe", "<b>Infections</b> or autoimmune disease", False),
          ("dna", "<b>Family genes</b>", False)]


def feel_causes():
    feel = "".join(f'<li>{icon(ic, "0.25in", sw=3.4)}<span>{txt}</span></li>' for ic, txt in FEEL)
    causes = "".join(f'<li{" class=nrp-top" if top else ""}>{icon(ic, "0.25in", sw=3.4)}<span>{txt}'
                     f'{"<em>top cause</em>" if top else ""}</span></li>' for ic, txt, top in CAUSES)
    return ('<div class="nrp-two">'
            f'<div class="nrp-card"><h3>What you may feel</h3><ul class="nrp-list">{feel}</ul></div>'
            f'<div class="nrp-card"><h3>Common causes</h3><ul class="nrp-list">{causes}</ul></div></div>')


def checks(ed):
    # [ADA26] Table 2.1/2.2: A1C <5.7% normal, 5.7-6.4% prediabetes, >=6.5% diabetes (a repeat test confirms).
    # [AAN09] if routine glucose is not diagnostic, a glucose tolerance test may be considered.
    a1c = ('<div class="nrp-a1c"><div class="ok"><i>Normal</i><b>under 5.7%</b></div>'
           '<div class="pre"><i>Prediabetes</i><b>5.7 to 6.4%</b></div>'
           '<div class="dm"><i>Diabetes</i><b>6.5% or more</b></div></div>')
    mine = '<div class="nrp-mine"><span>{}</span><i></i></div>'
    tiles = [
        ("meter", "Blood sugar", "A1c",
         a1c + '<p>A normal A1c? A 2-hour glucose test can still catch early sugar trouble.</p>', "My A1c"),
        # [AAN09] serum B12 "with metabolites (methylmalonic acid ...)"; [AROD16]/[ADA26] yearly with metformin.
        ("nrp-b12", "Vitamin B12", "",
         '<p>Low or borderline? An <b>MMA</b> test can show if it is really low. On metformin or an acid blocker: test yearly.</p>', "My B12"),
        # [ADA17] thyroid function is part of the work-up to exclude other causes.
        ("nrp-thyroid", "Thyroid", "TSH",
         '<p>An underactive thyroid can cause tingling too, and it is easy to test.</p>', "My TSH"),
        # [ADA17] "annual 10-g monofilament testing"; [ADA26] comprehensive foot evaluation at least yearly.
        ("nrp-foot", "Foot touch test", "",
         '<p>A soft nylon thread pressed on your feet (10-gram monofilament), <b>every year</b>.</p>', "Date"),
    ]
    cells = "".join(f'<div class="nrp-tile"><h4>{icon(ic, "0.2in", sw=3.6)}{t}{f" <small>{sub}</small>" if sub else ""}</h4>'
                    f'{body}{mine.format(m)}</div>' for ic, t, sub, body, m in tiles)
    # [ADA17] "serum B12, folic acid, thyroid function, complete blood count, metabolic panel, and a serum protein
    # immunoelectrophoresis"; [AAN09] serum protein immunofixation is a high-yield test.
    # Lab orders come from the prescriber, so the pharmacy edition says "your doctor" here.
    who = "Your doctor" if "pharmacist" in ed["who"] else ed["Who"]
    more = (f'{who} may also check folate, a blood count, kidney and liver tests and a blood protein test. '
            '<small>ADA and American Academy of Neurology guidance</small>')
    return ('<div class="nrp-checks"><div class="nrp-ch"><b>Ask for these checks</b><span>New numbness, tingling or burning? '
            'These tests find the most common causes, and many can be fixed.</span></div>'
            f'<div class="nrp-tiles">{cells}</div><p class="nrp-more">{_ed(more, ed)}</p></div>')


def alarm():
    # [ADA17] atypical features (rapid onset, asymmetry, weakness more than numbness) need further work-up;
    # foot ulcers and Charcot foot (a red, hot, swollen foot) are urgent [ADA17, ADA26];
    # stroke warning signs per the American Stroke Association (BE FAST): call 911.
    return ('<div class="nrp-alarm">' + icon("warning", "0.24in", "#A5281E", sw=3.6)
            + '<p><b>Get care right away</b> for numbness or weakness that comes on fast, spreads over days or affects one '
            'side only, or for a foot sore that will not heal or a red, hot, swollen foot. <b>Sudden weakness on one side, '
            'a drooping face or slurred speech: call 911.</b></p></div>')


def front(t, ed):
    return (f'<div class="nrp"><div class="art nrp-art">{art_neuro(t)}</div>'
            f'{feel_causes()}{checks(ed)}{alarm()}</div>')


CSS = r"""
.nrp .nrp-art svg{display:block;width:100%;height:auto}
.nrp .nrp-two{display:grid;grid-template-columns:1fr 1.22fr;gap:0.12in;margin-top:0.08in}
.nrp .nrp-card{border:1px solid #D6DCE4;border-radius:9px;background:#fff;padding:0.055in 0.11in 0.07in}
.nrp .nrp-card h3{font:800 7.6pt Inter,sans-serif;letter-spacing:.14em;text-transform:uppercase;color:var(--c1);margin:0 0 4px}
.nrp .nrp-list{display:grid;grid-template-columns:1fr 1fr;gap:3px 10px;margin:0;padding:0;list-style:none}
.nrp .nrp-list li{display:flex;align-items:center;gap:6px;font-size:8pt;line-height:1.2;color:#2B3236}
.nrp .nrp-list .ic{flex:none;color:var(--c2)}
.nrp .nrp-list b{color:var(--deep)}
.nrp .nrp-list li.nrp-top .ic{color:#A5281E}
.nrp .nrp-list em{display:inline-block;margin-left:5px;font:800 7pt Inter,sans-serif;font-style:normal;letter-spacing:.05em;
  text-transform:uppercase;color:#fff;background:#A5281E;border-radius:3px;padding:1px 4px;vertical-align:1px}
.nrp .nrp-checks{margin-top:0.08in;border:1px solid #D6DCE4;border-radius:10px;background:var(--tint);padding:0.06in 0.12in 0.07in}
.nrp .nrp-ch{display:flex;align-items:baseline;gap:10px;margin:0 0 5px}
.nrp .nrp-ch b{flex:none;font:900 11pt Merriweather,Georgia,serif;color:var(--c1)}
.nrp .nrp-ch span{font-size:8pt;line-height:1.3;color:#2B3236}
.nrp .nrp-tiles{display:grid;grid-template-columns:1.5fr 1fr 1fr 1fr;gap:6px}
.nrp .nrp-tile{background:#fff;border:1px solid #DDE3EA;border-radius:8px;padding:5px 7px 6px;display:flex;flex-direction:column}
.nrp .nrp-tile h4{margin:0;font:800 8.6pt Inter,sans-serif;color:var(--deep);display:flex;align-items:center;gap:5px}
.nrp .nrp-tile h4 .ic{flex:none;color:var(--c2)}
.nrp .nrp-tile h4 small{font-weight:700;color:#5E686F;font-size:7.4pt;margin-left:-1px}
.nrp .nrp-tile p{margin:3px 0 0;font-size:7.6pt;line-height:1.28;color:#2B3236}
.nrp .nrp-tile p b{color:var(--deep)}
.nrp .nrp-a1c{display:grid;grid-template-columns:repeat(3,1fr);gap:3px;margin-top:4px}
.nrp .nrp-a1c div{border-radius:4px;border-top:3px solid;padding:1px 2px 3px;text-align:center}
.nrp .nrp-a1c i{display:block;font:800 7pt Inter,sans-serif;font-style:normal;letter-spacing:.02em;text-transform:uppercase}
.nrp .nrp-a1c b{display:block;font:800 8.6pt/1.15 Inter,sans-serif;white-space:nowrap}
.nrp .nrp-a1c .ok{background:#E4F2EA;color:#1F6B47;border-color:#2F8A5E}
.nrp .nrp-a1c .pre{background:#FCEFD4;color:#7E5300;border-color:#D99A1E}
.nrp .nrp-a1c .dm{background:#F8E1DD;color:#9A2620;border-color:#C2392E}
.nrp .nrp-mine{margin-top:auto;display:flex;align-items:center;gap:6px;padding-top:5px;font:700 7pt Inter,sans-serif;color:#5E686F}
.nrp .nrp-mine span{white-space:nowrap}
.nrp .nrp-mine i{flex:1;height:0.2in;border-radius:4px;background:#E9ECEE;border:1px solid #D6DBDF}
.nrp .nrp-more{margin:5px 0 0;font-size:7.5pt;line-height:1.3;color:#3F4A50;display:flex;justify-content:space-between;gap:12px}
.nrp .nrp-more small{font-size:7pt;color:#6A747B;white-space:nowrap}
.nrp .nrp-alarm{margin-top:0.07in;border:1.5px solid #C0392B;background:#FDF1EF;border-radius:8px;padding:4px 10px 5px;
  display:flex;gap:8px;align-items:center}
.nrp .nrp-alarm .ic{flex:none}
.nrp .nrp-alarm p{margin:0;font-size:8pt;line-height:1.3;color:#2B3236}
.nrp .nrp-alarm b{color:#A5281E}
"""

# ============================================================== the sheet
SHEET = {
    "slug": SLUG, "code": "ND-NR-701", "order": 16, "theme": "neuro", "series": "Brain and Nerve Series",
    "title": "Nerve Pain and Neuropathy", "sub": "Burning, tingling or numb feet and hands",
    # [NINDS] "more than 20 million people in the United States"; "diabetes is the leading cause of polyneuropathy".
    # [ADA17] length-dependent: starts at the big toe on both sides and moves up; linked to height as a proxy for
    # nerve length; prediabetes can cause it; many non-diabetic causes are treatable (so: get checked).
    "intro": ("<b>Peripheral neuropathy</b> means the nerves that carry messages to your hands and feet are damaged. The "
              "longest nerves, the ones that reach your toes, are hit first, so it often starts as burning, tingling or numb "
              "feet. More than <b>20 million Americans</b> have it. <b>High blood sugar is the top cause</b>, and many "
              "others can be found and fixed."),
    "front": front,
    "css": CSS,
    "back": {
        "life_title": "Lifestyle Recommendations", "life_sub": "Protect your nerves and your feet", "style": "circle",
        "life": [
            # [ADA17] "Optimize glucose control to prevent or slow the progression of distal symmetric polyneuropathy
            # in people with type 2 diabetes"; prevention "focuses on glucose control and lifestyle modifications".
            ("meter", "Steady sugar", "Protein and veggies first, fewer sweets."),
            # [ADA17] an exercise program showed nerve fibre regrowth in type 2 diabetes; neuropathy is "a major
            # contributor to falls" (so: balance practice).
            ("walk", "Move most days", "Walk, bike or swim. Practice balance."),
            # [ADA17, ADA26] foot self-care: look daily; neuropathy is the main cause of foot ulcers.
            ("nrp-foot", "Check your feet", "Daily: look for cuts, blisters, red spots."),
            ("nrp-shoe", "Guard your feet", "No bare feet. Test bath water by elbow."),
            # [ADA17] alcohol is in the toxic-neuropathy table.
            ("glass", "Limit alcohol", "Alcohol is toxic to nerves. Keep it low."),
            # [ADA17] DSPN is associated with smoking; smoking slows wound healing.
            ("smoke", "Stop smoking", "Linked to nerve damage and slow healing."),
        ],
        "cols": [
            # Nerve Eze: SS ND633 (products.d/neuropathy.json). Evidence: PEA [VINA25, LANG23]; ALA [HSIEH23, PRADO24].
            {"p": "nrp_nerve_eze", "need": "Calm nerve signals", "needsub": "PEA + alpha lipoic acid", "start": True,
             "bullets": ["Supports healthy nerve function", "PEA is a fat-based messenger your body makes too"],
             "dose": "1 capsule twice daily", "dosesub": "morning and bedtime",
             "sched": [("am", 1, "capsule"), ("bed", 1, "capsule")]},
            # Gluco IR: products.py gluco_ir (label read). Blood sugar is the leading driver [NINDS, ADA17].
            # Its 300 mg ALA + Nerve Eze's 300 mg = 600 mg/day, the dose studied most [PRADO24, HSIEH23].
            {"p": "gluco_ir", "need": "Steady blood sugar", "needsub": "dihydroberberine, chromium, ALA",
             "bullets": ["Supports healthy glucose metabolism", "With Nerve Eze: 600 mg of ALA a day"],
             "dose": "dose_from_db"},
            # B12 Pro: DB R2181. Metformin [AROD16] and acid blockers [LAM13] lower B12; B12 is needed for myelin.
            {"p": "nrp_b12_pro", "need": "Feed the nerve coat", "needsub": "vitamin B12 as methylcobalamin",
             "bullets": ["Supports healthy myelin, the nerve's coat", "Metformin and acid blockers can lower B12"],
             "dose": "1 tablet daily", "dosesub": "let it dissolve in your mouth", "sched": [("am", 1, "tablet")]},
            # Methyl Complete: products.py methyl_b (switch-chart label read; DB R187 across 8 charts). Same three
            # active forms (L-methylfolate, methylcobalamin, P5P) as the Metanx RCT [FONS13], at lower doses.
            {"p": "methyl_b", "need": "The B-vitamin team", "needsub": "active folate, B6 and B12",
             "bullets": ["Active forms, ready for your body to use", "Supports healthy homocysteine levels"],
             "dose": "dose_from_db"},
            # Omega Pure EPA-DHA 1000: products.py omega_1000 (switch chart label read). Evidence: [LEWIS17].
            {"p": "omega_1000", "need": "Nerve membranes", "needsub": "omega-3s, EPA and DHA",
             "bullets": ["Building blocks of nerve cell membranes", "Supports a healthy inflammatory response"],
             "dose": "dose_from_db"},
        ],
        "rx": {
            # [AROD16], [ADA26] Section 9: B12 monitoring with long-term metformin; [LAM13] PPIs and H2 blockers.
            # Berberine and ALA both lower glucose (additive with diabetes medicines).  [EFSA23] excess B6 -> neuropathy.
            "practitioner": [
                "<b>Metformin or an acid blocker</b> (like omeprazole or famotidine) for years? Both can lower B12. "
                "Ask your provider for a B12 test every year.",
                "<b>On diabetes medicine?</b> Gluco IR (berberine plus alpha lipoic acid) can lower blood sugar further. "
                "Check it more often and tell your prescriber.",
                "<b>Vitamin B6 adds up.</b> Methyl Complete has 10 mg, and too much B6 can itself cause tingling. "
                "Bring every bottle so your provider can add up your B6."],
            "pharmacy": [
                "<b>Metformin or an acid blocker</b> (like omeprazole or famotidine) for years? Both can lower B12. "
                "Ask your prescriber for a B12 test every year.",
                "<b>On diabetes medicine?</b> Gluco IR (berberine plus alpha lipoic acid) can lower blood sugar further. "
                "Check it more often and tell your prescriber.",
                "<b>Vitamin B6 adds up.</b> Methyl Complete has 10 mg, and too much B6 can itself cause tingling. "
                "Bring every bottle so your pharmacist can add up your B6."],
        },
    },
}
