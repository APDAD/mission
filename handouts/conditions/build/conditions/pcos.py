"""Polycystic Ovary Syndrome (PCOS) condition sheet, slug "pcos".

Self-contained: no legacy / sheets.py / art.py drawing code.  Front rebuilt 2026-11-03 for
Asher's notes on the first draft:
  1. "Pancreas, insulin is made... we need a key": a KEY under the diagram names and explains
     every symbol and part (glucose, insulin, red blood cell, blood vessel, pancreas, follicle =
     the "cysts", androgens).
  2. The pancreas is drawn as a pancreas: a lobulated head nested in the C-loop of the
     duodenum (small intestine), then neck, body and a tapering tail, with its main duct.
  3. ONE blood vessel runs from the pancreas to BOTH ovaries.  Each branch ends in an arrowhead
     whose tip touches the ovary.  A zoom circle shows the crowded blood (extra sugar AND extra
     insulin).  The step text sits in its own strip under the art, numbered to match.
  4. The signs-and-symptoms ring and the fact and risk boxes stay.  "Extra facial or body hair"
     and "Thinning scalp hair" have their own icons.
Art-director pass (2026-11-03, second round):
  - Vessel: centrelines are straight runs + true arcs; each branch and its arrowhead are ONE
    outline (head 1.6 x the vessel width, aimed along the vessel's last direction, tip ray-cast
    to the ovary outline), and the pale inside tapers into the head.
  - Close-up circle: 10 sugars, 8 insulin, 3 red cells, all placed (the build asserts it).
  - "small intestine" sits under the duodenal C-loop, clear of the zoom caption.
  - Fallopian tubes: funnel end with nine tapered fimbriae of different lengths draping over the
    ovary; the tube is in the KEY.  The KEY's pancreas is the drawing's own outline in miniature.
  - Ring: top-of-head "thinning" icon (widened part, lone strands); longer facial-hair strokes;
    "Low-grade inflammation" replaced by "Dark skin patches (neck, armpits)"; a pregnant
    profile for "Trouble getting pregnant".
  - Facts: "About 1 in 8", AMH and "once other causes are ruled out", "Why it matters" moved into
    the facts box, risk factors relabelled "Can make it worse (you can change)", boxes balanced.
  - Glosses for ovulation, insulin resistance and sleep apnea.
Glucose (purple hexagon) and insulin (gold dot) use the same symbols as the insulin-resistance
sheet, so the Metabolic Health Series reads as one system.
Every SVG id starts with "pc" and every CSS class with "pc-" (all under .pcf), so nothing
collides with other sheets in the all-sheets bundle.

SOURCES (tags appear in comments next to each number on the page)
  [WHO23]    WHO fact sheet "Polycystic ovary syndrome" (2023): about 10-13% of women of
             reproductive age; up to 70% undiagnosed worldwide.  who.int could not be opened from
             the build machine on 2026-11-03; both figures were cross-checked against [MARCH10].
  [MARCH10]  March WA et al. Hum Reprod 2010;25:544-51. doi:10.1093/humrep/dep399 (community
             birth cohort: Rotterdam-criteria prevalence 11.9%; 68-69% had no prior diagnosis)
  [STEPTO13] Stepto NK et al. Hum Reprod 2013;28:777-84. doi:10.1093/humrep/des463 (clamp study:
             insulin resistance in 75% of lean and 95% of overweight women with PCOS)
  [GUIDE23]  Teede HJ et al. Recommendations from the 2023 International Evidence-based Guideline
             for PCOS. Eur J Endocrinol 2023;189:G43-G64. doi:10.1093/ejendo/lvad096 (adults: 2 of
             3 = irregular cycles, clinical or biochemical high androgens, polycystic ovaries on
             ultrasound or high AMH, other causes excluded; broader features include metabolic
             risk, cardiovascular disease, sleep apnoea and mood)
  [PENA25]   Pena AS et al. BMC Med 2025;23:151. doi:10.1186/s12916-025-03901-w (teens: irregular
             cycles AND high androgens; ultrasound and AMH are not used)
  [OWH]      US Office on Women's Health, "Polycystic ovary syndrome" fact sheet, and NIH NICHD,
             "What are the symptoms of PCOS?": irregular periods, extra facial and body hair, acne,
             thinning scalp hair, weight gain, darkened skin along neck creases and body folds
             (acanthosis nigricans), skin tags, infertility.  Not re-opened from the build machine
             on 2026-11-03 (outbound sites are blocked); long-standing content of both pages.

BACK: SHEET["back"] is still the first draft (a later back-page pass revises the products).  The
Myo-Inositol Complex facts (amounts, 6 capsules a day as 3 + 3) come from build/products.d/pcos.json.
"""
import math
import os
import random

from kit import icon
from svgkit import T, svg, label_bg

# ================================================================== text measuring (Inter)
_FACES = {}
_WEIGHTS = {400: "Regular", 500: "Medium", 600: "SemiBold", 700: "Bold", 800: "ExtraBold", 900: "Black"}


def tw(text, size, weight=700):
    """Advance width of `text` in Inter at `size` px (Pillow + the installed font); a generous
    guess when either is missing, so the build never fails on another machine."""
    try:
        if weight not in _FACES:
            from PIL import ImageFont
            for d in ("/usr/share/fonts/opentype/inter", "/usr/share/fonts/truetype/inter",
                      os.path.expanduser("~/Library/Fonts"), "/Library/Fonts"):
                for ext in ("otf", "ttf"):
                    f = os.path.join(d, f"Inter-{_WEIGHTS[weight]}.{ext}")
                    if os.path.exists(f):
                        _FACES[weight] = ImageFont.truetype(f, 200)
                        break
                if weight in _FACES:
                    break
        return _FACES[weight].getlength(text) * size / 200
    except Exception:
        return len(text) * size * 0.6


# ================================================================== palette (all named in the KEY)
INK = "#2B3236"
GLU, GLU_EDGE = "#6B6FC2", "#45499A"            # glucose (sugar): purple hexagon
INS_EDGE = "#A8740C"                            # insulin: gold dot (gradient pcIn)
AND, AND_EDGE = "#1C8C86", "#0F5E5A"            # androgens: teal diamond
V_OUT, V_WALL, V_LUM = "#7A1A23", "#C0414A", "#FCE4DF"   # blood vessel: outline, wall, inside
P_EDGE, P_SEPTA = "#AA683C", "#E0A46E"          # pancreas outline and the lines between lobules
P_LOBES = ("#F6CFA3", "#F3C796", "#F8D5AD", "#F2C391", "#F5CB9D")
D_EDGE, D_FILL, D_HI, D_FOLD = "#B98273", "#EEC6BB", "#F8E0D8", "#CB988C"   # duodenum (kept quiet: the pancreas is the hero)
U_EDGE, U_BASE = "#A23F4A", "#DD7F87"           # uterus and tubes
O_EDGE = "#B95C69"                              # ovary outline
F_FILL, F_EDGE = "#FFF9F6", "#CF7983"           # follicle ("cyst")


def pc_defs():
    mk = lambda i, c: (f'<marker id="{i}" viewBox="0 0 10 10" refX="6.5" refY="5" markerWidth="4.4" markerHeight="4.4" '
                       f'orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="{c}"/></marker>')
    return ("<defs>"
            '<radialGradient id="pcIn" cx=".36" cy=".32" r=".78"><stop offset="0" stop-color="#FFE9A8"/>'
            '<stop offset=".55" stop-color="#F2B632"/><stop offset="1" stop-color="#DE9A14"/></radialGradient>'
            '<radialGradient id="pcRc" cx=".42" cy=".36" r=".75"><stop offset="0" stop-color="#E8656A"/>'
            '<stop offset="1" stop-color="#B0242D"/></radialGradient>'
            '<linearGradient id="pcPanShade" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FFFFFF" stop-opacity=".38"/>'
            '<stop offset=".42" stop-color="#FFFFFF" stop-opacity="0"/><stop offset="1" stop-color="#7A3E12" stop-opacity=".26"/></linearGradient>'
            '<radialGradient id="pcUt" cx=".4" cy=".28" r=".85"><stop offset="0" stop-color="#F0A9AD"/>'
            '<stop offset=".6" stop-color="#DE8189"/><stop offset="1" stop-color="#C9606B"/></radialGradient>'
            '<radialGradient id="pcOv" cx=".38" cy=".32" r=".8"><stop offset="0" stop-color="#FCEAE5"/>'
            '<stop offset="1" stop-color="#EDBDB7"/></radialGradient>'
            '<radialGradient id="pcFo" cx=".4" cy=".36" r=".7"><stop offset="0" stop-color="#FFFFFF"/>'
            '<stop offset="1" stop-color="#FBE3E0"/></radialGradient>'
            '<radialGradient id="pcLu" cx=".5" cy=".45" r=".65"><stop offset="0" stop-color="#FFF1EE"/>'
            '<stop offset="1" stop-color="#F8D3CC"/></radialGradient>'
            + mk("pcAy", INS_EDGE) +
            "</defs>")


# ================================================================== geometry helpers
def crs(pts, closed=False, per=12):
    """Dense points along a uniform Catmull-Rom spline through pts."""
    n = len(pts)

    def P(i):
        return pts[i % n] if closed else pts[max(0, min(n - 1, i))]
    out = []
    for i in range(n if closed else n - 1):
        p0, p1, p2, p3 = P(i - 1), P(i), P(i + 1), P(i + 2)
        for k in range(per):
            t = k / per
            t2, t3 = t * t, t * t * t
            out.append(tuple(0.5 * (2 * p1[j] + (p2[j] - p0[j]) * t + (2 * p0[j] - 5 * p1[j] + 4 * p2[j] - p3[j]) * t2
                                    + (3 * p1[j] - p0[j] - 3 * p2[j] + p3[j]) * t3) for j in (0, 1)))
    if not closed:
        out.append(pts[-1])
    return out


def cr_d(pts, closed=False):
    """SVG path (cubic Beziers) of the same Catmull-Rom spline."""
    n = len(pts)

    def P(i):
        return pts[i % n] if closed else pts[max(0, min(n - 1, i))]
    d = [f"M{pts[0][0]:.1f},{pts[0][1]:.1f}"]
    for i in range(n if closed else n - 1):
        p0, p1, p2, p3 = P(i - 1), P(i), P(i + 1), P(i + 2)
        c1 = (p1[0] + (p2[0] - p0[0]) / 6, p1[1] + (p2[1] - p0[1]) / 6)
        c2 = (p2[0] - (p3[0] - p1[0]) / 6, p2[1] - (p3[1] - p1[1]) / 6)
        d.append(f"C{c1[0]:.1f},{c1[1]:.1f} {c2[0]:.1f},{c2[1]:.1f} {p2[0]:.1f},{p2[1]:.1f}")
    return " ".join(d) + (" Z" if closed else "")


def resample(poly, step, closed=False):
    """Points every `step` units along a polyline."""
    pts = list(poly) + ([poly[0]] if closed else [])
    cum = [0.0]
    for a, b in zip(pts, pts[1:]):
        cum.append(cum[-1] + math.dist(a, b))
    total = cum[-1]
    n = max(2, int(round(total / step)))
    out, j = [], 0
    for k in range(n if closed else n + 1):
        d = total * k / n
        while j < len(cum) - 2 and cum[j + 1] < d:
            j += 1
        seg = (cum[j + 1] - cum[j]) or 1e-9
        t = (d - cum[j]) / seg
        a, b = pts[j], pts[j + 1]
        out.append((a[0] + (b[0] - a[0]) * t, a[1] + (b[1] - a[1]) * t))
    return out


def poly_d(pts, closed=True):
    return "M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in pts) + (" Z" if closed else "")


def tangents(c):
    out = []
    for i in range(len(c)):
        a, b = c[max(0, i - 1)], c[min(len(c) - 1, i + 1)]
        tx, ty = b[0] - a[0], b[1] - a[1]
        ln = math.hypot(tx, ty) or 1.0
        out.append((tx / ln, ty / ln))
    return out


def sides(c, widths):
    """Left and right edges of a band of varying width around the centreline polyline c."""
    L, R = [], []
    for (x, y), (tx, ty), w in zip(c, tangents(c), widths):
        L.append((x - ty * w / 2, y + tx * w / 2))
        R.append((x + ty * w / 2, y - tx * w / 2))
    return L, R


def ribbon(c, widths):
    """Closed outline of a band of varying width around the centreline polyline c."""
    L, R = sides(c, widths)
    return poly_d(L + R[::-1])


def arc_pts(c, r, a0, a1, turn, step=1.0):
    """Points on a circular arc of radius r about c, for travel headings a0 -> a1 (degrees).
    turn=+1 bends clockwise on screen (heading angle grows), turn=-1 counter-clockwise."""
    n = max(2, int(abs(math.radians(a1 - a0)) * r / step))
    out = []
    for k in range(n + 1):
        f = math.radians(a0 + (a1 - a0) * k / n)
        out.append((c[0] + turn * r * math.sin(f), c[1] - turn * r * math.cos(f)))
    return out


def line_pts(p, q, step=1.0):
    n = max(1, int(math.dist(p, q) / step))
    return [(p[0] + (q[0] - p[0]) * k / n, p[1] + (q[1] - p[1]) * k / n) for k in range(n + 1)]


def ray_ellipse(p, d, c, rx, ry, rot):
    """Distance along the unit ray p + t*d to where it first meets an ellipse (centre c, radii rx and
    ry, turned rot degrees as in SVG rotate()), or None when it misses."""
    a = math.radians(rot)
    ca, sa = math.cos(a), math.sin(a)
    qx, qy = p[0] - c[0], p[1] - c[1]
    qx, qy = qx * ca + qy * sa, -qx * sa + qy * ca
    dx, dy = d[0] * ca + d[1] * sa, -d[0] * sa + d[1] * ca
    A = (dx / rx) ** 2 + (dy / ry) ** 2
    B = 2 * (qx * dx / rx ** 2 + qy * dy / ry ** 2)
    C = (qx / rx) ** 2 + (qy / ry) ** 2 - 1
    disc = B * B - 4 * A * C
    return None if disc < 0 else (-B - math.sqrt(disc)) / (2 * A)


def arrow_tube(c, widths, tip, hw, back):
    """ONE closed outline for a tube that ends in an arrowhead: the band runs to c[-1], flares out to
    two barbs hw either side of the centreline (swept back by `back`), and closes at tip.  The head is
    aligned to the tube's last direction, so the outline wraps tube and head without a notch."""
    L, R = sides(c, widths)
    tx, ty = tangents(c)[-1]
    nx, ny = -ty, tx
    bx, by = c[-1]
    bl = (bx + nx * hw - tx * back, by + ny * hw - ty * back)
    br = (bx - nx * hw - tx * back, by - ny * hw - ty * back)
    return poly_d(L + [bl, tip] + [br] + R[::-1])


def arrow_lumen(c, widths, reach):
    """The pale inside of an arrow_tube: the same band, tapering to a point `reach` units into the
    head, so the inside flows into the arrow instead of stopping in a flat cut."""
    L, R = sides(c, widths)
    tx, ty = tangents(c)[-1]
    bx, by = c[-1]
    return poly_d(L + [(bx + tx * reach, by + ty * reach)] + R[::-1])


def inside(p, poly):
    x, y = p
    hit = False
    for (x1, y1), (x2, y2) in zip(poly, poly[1:] + poly[:1]):
        if (y1 > y) != (y2 > y) and x < x1 + (y - y1) * (x2 - x1) / (y2 - y1):
            hit = not hit
    return hit


def _clip(poly, a, b, c):
    """Keep the part of a convex polygon where a*x + b*y <= c."""
    out = []
    for i, P in enumerate(poly):
        Q = poly[(i + 1) % len(poly)]
        fp, fq = a * P[0] + b * P[1] - c, a * Q[0] + b * Q[1] - c
        if fp <= 0:
            out.append(P)
        if (fp < 0 < fq) or (fq < 0 < fp):
            t = fp / (fp - fq)
            out.append((P[0] + (Q[0] - P[0]) * t, P[1] + (Q[1] - P[1]) * t))
    return out


def voronoi(seeds, box, reach):
    """Voronoi cell (convex polygon) of every seed, by half-plane clipping inside box."""
    cells = []
    for i, p in enumerate(seeds):
        cell = [(box[0], box[1]), (box[2], box[1]), (box[2], box[3]), (box[0], box[3])]
        for j, q in enumerate(seeds):
            if i != j and (p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2 < reach * reach:
                cell = _clip(cell, q[0] - p[0], q[1] - p[1], (q[0] ** 2 + q[1] ** 2 - p[0] ** 2 - p[1] ** 2) / 2)
                if not cell:
                    break
        cells.append(cell)
    return cells


def rounded_cell(cell, inset):
    """A Voronoi cell shrunk toward its centre and drawn with rounded corners (one lobule)."""
    cx = sum(x for x, _ in cell) / len(cell)
    cy = sum(y for _, y in cell) / len(cell)
    v = []
    for x, y in cell:
        dx, dy = x - cx, y - cy
        ln = math.hypot(dx, dy) or 1.0
        k = max(0.0, (ln - inset) / ln)
        v.append((cx + dx * k, cy + dy * k))
    m = [((v[i][0] + v[(i + 1) % len(v)][0]) / 2, (v[i][1] + v[(i + 1) % len(v)][1]) / 2) for i in range(len(v))]
    d = [f"M{m[-1][0]:.1f},{m[-1][1]:.1f}"]
    for i in range(len(v)):
        d.append(f"Q{v[i][0]:.1f},{v[i][1]:.1f} {m[i][0]:.1f},{m[i][1]:.1f}")
    return " ".join(d) + "Z"


def scallop(outline, step=10.0, bump=2.6):
    """Lobulated edge: the smooth closed outline redrawn as a run of small outward bulges."""
    pts = resample(outline, step, closed=True)
    area = sum(a[0] * b[1] - b[0] * a[1] for a, b in zip(pts, pts[1:] + pts[:1]))
    s = 1 if area > 0 else -1          # outward normal side for this winding
    d = [f"M{pts[0][0]:.1f},{pts[0][1]:.1f}"]
    for a, b in zip(pts, pts[1:] + pts[:1]):
        mx, my = (a[0] + b[0]) / 2, (a[1] + b[1]) / 2
        tx, ty = b[0] - a[0], b[1] - a[1]
        ln = math.hypot(tx, ty) or 1.0
        nx, ny = s * ty / ln, -s * tx / ln
        d.append(f"Q{mx + nx * bump:.1f},{my + ny * bump:.1f} {b[0]:.1f},{b[1]:.1f}")
    return " ".join(d) + "Z"


# ================================================================== molecules and small parts
def glucose(x, y, r=4.8):
    pts = " ".join(f"{x + r * c:.1f},{y + r * s:.1f}" for c, s in
                   ((1, 0), (.5, .866), (-.5, .866), (-1, 0), (-.5, -.866), (.5, -.866)))
    return f'<polygon points="{pts}" fill="{GLU}" stroke="{GLU_EDGE}" stroke-width="1" stroke-linejoin="round"/>'


def insulin(x, y, r=4.8):
    return f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="url(#pcIn)" stroke="{INS_EDGE}" stroke-width="1"/>'


def red_cell(x, y, rot=0, s=1.0):
    return (f'<g transform="translate({x:.1f},{y:.1f}) rotate({rot}) scale({s})"><ellipse rx="12.5" ry="7" fill="url(#pcRc)" '
            'stroke="#8E1D25" stroke-width=".8"/><ellipse rx="6.2" ry="2.8" fill="none" stroke="#97202A" stroke-width="1.5" opacity=".75"/></g>')


def androgen(x, y, r=5.2):
    return (f'<path d="M{x:.1f},{y - r:.1f} L{x + r * .78:.1f},{y:.1f} L{x:.1f},{y + r:.1f} L{x - r * .78:.1f},{y:.1f}Z" '
            f'fill="{AND}" stroke="{AND_EDGE}" stroke-width="1" stroke-linejoin="round"/>')


def follicle(x, y, r):
    return (f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r:.1f}" fill="url(#pcFo)" stroke="{F_EDGE}" stroke-width="1.3"/>')


def marker(x, y, n, c1):
    return (f'<circle cx="{x}" cy="{y}" r="10.5" fill="{c1}" stroke="#FFFFFF" stroke-width="2"/>'
            + T(x, y + 4.1, str(n), 11.5, 800, "#FFFFFF", "middle"))


def scatter(rng, items, box, ok, pad=1.5, tries=6000):
    """Place round things (radius r each) inside box without overlap; ok(x, y, r) vetoes spots."""
    out = []
    for r in items:
        for _ in range(tries):
            x, y = rng.uniform(box[0] + r, box[2] - r), rng.uniform(box[1] + r, box[3] - r)
            if not ok(x, y, r):
                continue
            if any((x - px) ** 2 + (y - py) ** 2 < (r + pr + pad) ** 2 for px, py, pr in out):
                continue
            out.append((x, y, r))
            break
    return out


# ================================================================== pancreas + duodenum (local units)
# Anterior view, as in an anatomy atlas: head on the left inside the duodenal C, uncinate process
# hooking under the neck, then body and tail rising toward the spleen.
P_OUT = [(30, 33), (52, 23), (78, 25), (98, 37), (120, 33), (156, 26), (194, 17), (226, 9), (246, 6), (258, 11),
         (254, 22), (232, 31), (196, 43), (156, 56), (128, 66), (111, 78), (117, 96), (103, 110), (75, 116),
         (47, 112), (29, 100), (20, 78), (21, 52)]
DUO = [(114, 11), (74, 8), (38, 11), (18, 28), (10, 58), (13, 91), (29, 113), (60, 124), (100, 124), (132, 116),
       (152, 99)]
DUO_W = 21.0
DUCT = [(244, 13), (214, 22), (180, 32), (146, 43), (118, 52), (96, 60), (70, 68), (44, 72), (22, 74)]


def duodenum():
    o = [f'<path d="{cr_d(DUO)}" fill="none" stroke="{D_EDGE}" stroke-width="{DUO_W + 2.6}"/>',
         f'<path d="{cr_d(DUO)}" fill="none" stroke="{D_FILL}" stroke-width="{DUO_W}"/>',
         f'<path d="{cr_d(DUO)}" fill="none" stroke="{D_HI}" stroke-width="7" opacity=".75"/>']
    c = resample(crs(DUO, per=20), 1.0)
    tg = tangents(c)
    hw = DUO_W / 2 - 1.2
    # soft ring folds across the tube, as on an intestine drawn from the outside
    for i in range(16, len(c) - 16, 13):
        (x, y), (tx, ty) = c[i], tg[i]
        a = (x - ty * hw, y + tx * hw)
        b = (x + ty * hw, y - tx * hw)
        q = (x + tx * 3.2, y + ty * 3.2)
        o.append(f'<path d="M{a[0]:.1f},{a[1]:.1f} Q{q[0]:.1f},{q[1]:.1f} {b[0]:.1f},{b[1]:.1f}" fill="none" '
                 f'stroke="{D_FOLD}" stroke-width="1" opacity=".5"/>')
    # cut ends (the stomach is to the upper right, the jejunum continues from the far end)
    for (x, y), (tx, ty) in ((c[0], tg[0]), (c[-1], tg[-1])):
        ang = math.degrees(math.atan2(ty, tx))
        o.append(f'<g transform="translate({x:.1f},{y:.1f}) rotate({ang:.1f})">'
                 f'<ellipse rx="3.6" ry="{DUO_W / 2 + 1.1:.1f}" fill="{D_FILL}" stroke="{D_EDGE}" stroke-width="1.3"/>'
                 f'<ellipse rx="2.1" ry="{DUO_W / 2 - 4:.1f}" fill="#C98073"/></g>')
    return "".join(o)


def pancreas():
    rng = random.Random(5)
    smooth = crs(P_OUT, closed=True, per=14)
    edge = scallop(smooth, 10.5, 2.4)
    # lobules: Voronoi cells of a jittered grid, rounded and inset so the septa show between them
    seeds, s = [], 10.5
    for j in range(-1, 15):
        for i in range(-1, 27):
            x = i * s + (s / 2 if j % 2 else 0) + rng.uniform(-2.6, 2.6)
            y = j * s * 0.87 + rng.uniform(-2.2, 2.2)
            if inside((x, y), smooth) or any(math.dist((x, y), q) < 5 for q in smooth[::3]):
                seeds.append((x, y))
    cells = voronoi(seeds, (0, -5, 270, 130), s * 3)
    lob = "".join(f'<path d="{rounded_cell(c, 0.95)}" fill="{rng.choice(P_LOBES)}"/>' for c in cells if len(c) > 2)
    duct = cr_d(DUCT)
    return (f'<clipPath id="pcPanClip"><path d="{edge}"/></clipPath>'
            f'<path d="{edge}" fill="{P_SEPTA}"/>'
            f'<g clip-path="url(#pcPanClip)">{lob}'
            f'<path d="{duct}" fill="none" stroke="#C17B45" stroke-width="3.8" stroke-linecap="round" opacity=".8"/>'
            f'<path d="{duct}" fill="none" stroke="#FCE9D3" stroke-width="1.9" stroke-linecap="round"/>'
            f'<path d="{edge}" fill="url(#pcPanShade)"/></g>'
            f'<path d="{edge}" fill="none" stroke="{P_EDGE}" stroke-width="1.7" stroke-linejoin="round"/>')


# ================================================================== uterus, tubes, ovaries (local units)
UT_OUT = [(0, 0), (24, 2), (42, 10), (49, 26), (45, 50), (35, 76), (25, 96), (21, 106), (21, 122), (14, 132), (0, 134),
          (-14, 132), (-21, 122), (-21, 106), (-25, 96), (-35, 76), (-45, 50), (-49, 26), (-42, 10), (-24, 2)]
UT_CAV = [(0, 14), (17, 15), (30, 19), (21, 35), (11, 58), (5, 80), (2.5, 92), (0, 95), (-2.5, 92), (-5, 80), (-11, 58),
          (-21, 35), (-30, 19), (-17, 15)]
TUBE = [(40, 13), (57, 3), (77, -4), (95, -5), (106, -1), (111, 7)]
OV_C, OV_RX, OV_RY, OV_ROT = (106, 38), 31, 20, -12


def ov_pole(side):
    """Lateral pole of an ovary in local units (side = +1 right, -1 left)."""
    a = math.radians(OV_ROT)
    return (side * (OV_C[0] + OV_RX * math.cos(a)), OV_C[1] + OV_RX * math.sin(a))


def frond(x0, y0, ang, length, bw, curl, tw=1.05):
    """One fimbria: a thin finger from the funnel rim, tapering from bw to a rounded tip tw wide and
    bending sideways by `curl` (positive = toward the ovary)."""
    ca, sa = math.cos(math.radians(ang)), math.sin(math.radians(ang))

    def P(u, v):
        return f"{x0 + u * ca - v * sa:.2f},{y0 + u * sa + v * ca:.2f}"
    r = tw / 2
    return (f"M{P(-1.5, -bw / 2)} Q{P(length * .55, -bw * .42 + curl * .55)} {P(length, curl - r)} "
            f"A{r:.2f},{r:.2f} 0 0 1 {P(length, curl + r)} "
            f"Q{P(length * .55, bw * .42 + curl * .55)} {P(-1.5, bw / 2)}Z")


# fimbriae: (rim position, fan angle, length, base width, bend).  The fan leans toward the ovary
# (positive angles) and the lengths differ, like a real fringe draping over the ovary.
FRONDS = [(-8.7, -22, 8.2, 2.5, -0.5), (-6.5, -12, 11.6, 2.7, -0.2), (-4.3, -2, 9.4, 2.8, 0.4), (-2.1, 8, 13.6, 3.0, 0.8),
          (0.1, 18, 10.4, 3.0, 1.0), (2.3, 28, 14.0, 2.9, 1.3), (4.5, 38, 9.6, 2.8, 1.2), (6.7, 48, 11.8, 2.6, 1.4),
          (8.8, 58, 7.4, 2.4, 1.1)]


def tube_shape():
    """Fallopian tube (narrow near the uterus, widening outward) and, separately, its funnel end
    (infundibulum) with the fimbriae, which are drawn later so the fringe drapes over the ovary."""
    c = resample(crs(TUBE, per=16), 1.5)
    n = len(c)
    w = [6.2 + 4.2 * (k / (n - 1)) ** 1.3 for k in range(n)]
    tube = f'<path d="{ribbon(c, w)}" fill="{U_BASE}" stroke="{U_EDGE}" stroke-width="1.5" stroke-linejoin="round"/>'
    (ex, ey), (tx, ty) = c[-1], tangents(c)[-1]
    f = [f'<g transform="translate({ex:.1f},{ey:.1f}) rotate({math.degrees(math.atan2(ty, tx)):.1f})">']
    for k, (y, ang, ln, bw, curl) in enumerate(FRONDS):
        f.append(f'<path d="{frond(4.6, y, ang, ln, bw, curl)}" fill="{"#E3929A" if k % 2 else U_BASE}" stroke="{U_EDGE}" '
                 'stroke-width=".95" stroke-linejoin="round"/>')
    f.append(f'<path d="M-2.5,-5.3 C1.2,-5.5 3.4,-7.7 5.6,-9.9 Q7,-0 5.6,9.9 C3.4,7.7 1.2,5.5 -2.5,5.3Z" fill="{U_BASE}" '
             f'stroke="{U_EDGE}" stroke-width="1.3" stroke-linejoin="round"/>')
    f.append(f'<path d="M5.2,-8.4 Q6.3,0 5.2,8.4" fill="none" stroke="#B9525C" stroke-width=".9" opacity=".7"/>')
    f.append("</g>")
    return tube, "".join(f)


def ovary(rng):
    cx, cy = OV_C
    o = [f'<g transform="translate({cx},{cy}) rotate({OV_ROT})">',
         f'<ellipse rx="{OV_RX}" ry="{OV_RY}" fill="url(#pcOv)" stroke="{O_EDGE}" stroke-width="1.6"/>',
         f'<ellipse rx="{OV_RX * .5:.1f}" ry="{OV_RY * .42:.1f}" fill="#EBB7B1" opacity=".55"/>']
    n = 13
    for k in range(n):
        a = 2 * math.pi * (k + rng.uniform(-.18, .18)) / n
        r = rng.uniform(4.2, 5.3)
        o.append(follicle(OV_RX * .74 * math.cos(a), OV_RY * .64 * math.sin(a), r))
    o.append("</g>")
    return "".join(o)


def reproductive(UX, UY, US):
    """Uterus with both tubes and ovaries, mirror-symmetric about x = UX."""
    rng = random.Random(3)
    tube, fimb = tube_shape()
    right = (tube
             + f'<path d="M38,36 Q58,46 {OV_C[0] - OV_RX * .96:.1f},{OV_C[1] + 7:.1f}" fill="none" stroke="{U_EDGE}" '
               'stroke-width="6.2" stroke-linecap="round"/>'
             + f'<path d="M38,36 Q58,46 {OV_C[0] - OV_RX * .96:.1f},{OV_C[1] + 7:.1f}" fill="none" stroke="{U_BASE}" '
               'stroke-width="3.8" stroke-linecap="round"/>')
    ov = ovary(rng)
    body = (f'<path d="{cr_d(UT_OUT, True)}" fill="url(#pcUt)" stroke="{U_EDGE}" stroke-width="1.8"/>'
            f'<path d="{cr_d(UT_CAV, True)}" fill="#F6C1C2" stroke="#D9878F" stroke-width="1"/>'
            '<path d="M0,94 V127" stroke="#F3B5B8" stroke-width="3.4" stroke-linecap="round"/>')
    return (f'<g transform="translate({UX},{UY}) scale({US})">'
            f'<g>{right}</g><g transform="scale(-1,1)">{right}</g>{body}'
            f'<g>{ov}</g><g transform="scale(-1,1)">{ov}</g>'
            f'<g>{fimb}</g><g transform="scale(-1,1)">{fimb}</g>'
            "</g>")


# ================================================================== the diagram
W_ART, H_ART = 760, 242
PX, PY, PS = 16, 98, 0.90           # pancreas group
UX, UY, US = 566, 82, 0.94           # uterus group
TY, TW, WALL = 28, 34, 5              # vessel trunk centre line, width, wall thickness
BX, BY, BR = 318, 144, 54             # zoom circle


def art_pcos(t):
    c1 = t["c1"]
    rng = random.Random(17)
    o = [pc_defs()]

    # ---------------------------------------------------------- vessel geometry
    # Each branch ends in an arrowhead aimed along the ovary's long axis.  Its tip sits 1.2 units inside
    # the ovary outline (the ovary is drawn on top), so the arrow visibly touches the ovary.
    a = math.radians(OV_ROT)
    HL, HW, BACK = 19.0, 16.0, 2.5      # head length; half-width (head = 1.6 x the 20-unit vessel); barb sweep
    ends = {}
    for side in (1, -1):
        d = (-side * math.cos(a), -math.sin(a))                     # into this ovary, along its long axis
        oc = (UX + side * OV_C[0] * US, UY + OV_C[1] * US)
        pole = (UX + ov_pole(side)[0] * US, UY + ov_pole(side)[1] * US)
        ends[side] = (d, oc, (pole[0] - d[0] * (HL - 1.2), pole[1] - d[1] * (HL - 1.2)))
    dR, ocR, baseR = ends[1]
    dL, ocL, baseL = ends[-1]

    # Centrelines are straight runs joined by true circular arcs (no spline wobble), solved backwards
    # from each head: a straight run of S units into the base, an arc of radius R2 from heading straight
    # down, a straight drop, and an arc of radius R1 off the horizontal trunk.
    S, R1, R2, R3 = 14.0, 26.0, 18.0, 22.0

    def branch(base, d, r_top, start_x):
        hd = math.degrees(math.atan2(d[1], d[0]))
        e = (base[0] - d[0] * S, base[1] - d[1] * S)
        turn = 1 if d[0] < 0 else -1                 # right ovary: bend clockwise; left ovary: counter-clockwise
        c2 = (e[0] - turn * R2 * math.sin(math.radians(hd)), e[1] + turn * R2 * math.cos(math.radians(hd)))
        xv = c2[0] + turn * R2                       # the straight drop
        c1 = (xv - r_top, TY + r_top)
        assert c2[1] > c1[1] + 8, "no room for the vessel's straight drop"
        return (line_pts((start_x, TY), (c1[0], TY)) + arc_pts(c1, r_top, 0, 90, 1)[1:]
                + line_pts((xv, c1[1]), (xv, c2[1]))[1:] + arc_pts(c2, R2, 90, hd, turn)[1:] + line_pts(e, base)[1:])
    wave = crs([(14, TY), (100, TY - 1), (200, TY + 1), (300, TY - 1), (400, TY), (500, TY), (600, TY - 1), (684, TY)], per=16)
    tc = resample(wave[:-1] + branch(baseR, dR, R1, 684), 2.0)
    lc = resample(branch(baseL, dL, R3, 352), 2.0)
    # The head points along the tube's LAST direction; its tip is where that line meets the ovary
    # outline, plus 1.2 units, so it always touches the ovary whatever the curve does.
    tips = []
    for c, oc, side in ((tc, ocR, 1), (lc, ocL, -1)):
        t_ = tangents(c)[-1]
        hit = ray_ellipse(c[-1], t_, oc, OV_RX * US, OV_RY * US, side * OV_ROT)
        assert hit is not None and abs(hit + 1.2 - HL) < 3, "arrowhead does not reach the ovary"
        tips.append((c[-1][0] + t_[0] * (hit + 1.2), c[-1][1] + t_[1] * (hit + 1.2)))
    tipR, tipL = tips
    taper0 = next(i for i, p in enumerate(tc) if p[0] > 676)
    tw_ = [TW if i < taper0 else TW - (TW - 20) * min(1, (i - taper0) / 34) for i in range(len(tc))]
    lw_ = [20.0] * len(lc)

    # ---------------------------------------------------------- pancreas, then insulin rising into the blood
    o.append(f'<g transform="translate({PX},{PY}) scale({PS})">{duodenum()}{pancreas()}</g>')
    for x0, y0 in ((160, 120), (204, 108)):
        o.append(f'<path d="M{x0},{y0} V{TY + TW / 2 + 5}" stroke="{INS_EDGE}" stroke-width="1.8" stroke-dasharray="3 3" '
                 'marker-end="url(#pcAy)" fill="none"/>')
        for k, yy in enumerate((y0 - 14, y0 - 34, y0 - 54)):
            if yy > TY + TW / 2 + 14:          # keep the top dot clear of the arrowhead
                o.append(insulin(x0 + (3.5 if k % 2 else -3.5), yy, 4.4))

    # ---------------------------------------------------------- vessel: outline, wall, inside
    # Three layers, so the branch joins the trunk without a seam: every outline first (a 2.4-unit
    # stroke around the one-piece tube + head shape), then every wall, then every inside.
    shapes = [arrow_tube(tc, tw_, tipR, HW, BACK), arrow_tube(lc, lw_, tipL, HW, BACK)]
    for s in shapes:
        o.append(f'<path d="{s}" fill="{V_OUT}" stroke="{V_OUT}" stroke-width="2.4" stroke-linejoin="round"/>')
    for s in shapes:
        o.append(f'<path d="{s}" fill="{V_WALL}"/>')
    tl = [w - 2 * WALL for w in tw_]
    ll = [w - 2 * WALL for w in lw_]
    o.append(f'<path d="{arrow_lumen(tc, tl, HL * .42)}" fill="{V_LUM}" stroke="{V_LUM}" stroke-width=".6" stroke-linejoin="round"/>')
    o.append(f'<path d="{arrow_lumen(lc, ll, HL * .42)}" fill="{V_LUM}" stroke="{V_LUM}" stroke-width=".6" stroke-linejoin="round"/>')
    o.append(f'<path d="{arrow_lumen(tc, [x * .35 for x in tl], HL * .2)}" fill="#FFFFFF" opacity=".35"/>')
    # cut end at the far left, so the vessel reads as a tube
    o.append(f'<ellipse cx="14" cy="{TY}" rx="5.4" ry="{TW / 2 + 1.2}" fill="{V_WALL}" stroke="{V_OUT}" stroke-width="1.3"/>'
             f'<ellipse cx="14" cy="{TY}" rx="3.2" ry="{TW / 2 - WALL}" fill="#E7A39B"/>')

    # what the blood carries: glucose, insulin, red blood cells
    lab_w = tw("Blood vessel", 10.5, 800) + 14
    lab_x0 = 34

    tg = tangents(tc)
    placed = []
    kinds = ["g"] * 16 + ["i"] * 12 + ["r"] * 6
    rng.shuffle(kinds)
    idx = list(range(12, taper0 - 6))
    for kind in kinds:
        r = 7.6 if kind == "r" else 4.7
        for _ in range(400):
            i = rng.choice(idx)
            (x, y), (tx, ty) = tc[i], tg[i]
            lim = (tl[i] / 2) - (3.6 if kind == "r" else r) - 1.2
            u = rng.uniform(-lim, lim)
            px, py = x - ty * u, y + tx * u
            if lab_x0 - 4 < px < lab_x0 + lab_w + 4:       # keep the "Blood vessel" label clear
                continue
            if any(math.dist((px, py), (qx, qy)) < r + qr + 2.4 for qx, qy, qr, _ in placed):
                continue
            placed.append((px, py, r, kind))
            break
    for px, py, r, kind in placed:
        o.append(glucose(px, py) if kind == "g" else insulin(px, py) if kind == "i" else
                 red_cell(px, py, rng.uniform(-12, 12), 0.6))
    # insulin riding the branches all the way to the ovaries
    for c in (lc, tc[taper0 + 8:]):
        n = len(c)
        for f in (0.3, 0.55, 0.8):
            x, y = c[int(n * f)]
            o.append(insulin(x, y, 3.7))
    o.append(label_bg(lab_x0, TY - 9, lab_w, 18, "#FFFFFF", 0.94, 5)
             + T(lab_x0 + lab_w / 2, TY + 3.8, "Blood vessel", 10.5, 800, "#8E1F28", "middle"))

    # ---------------------------------------------------------- zoom circle: the crowded blood
    r_ind = 21
    d = BY - TY
    ny_ = (r_ind - BR) / d
    nx_ = math.sqrt(1 - ny_ * ny_)
    for sx in (-1, 1):
        a1 = (BX + sx * r_ind * nx_, TY + r_ind * ny_)
        a2 = (BX + sx * BR * nx_, BY + BR * ny_)
        o.append(f'<path d="M{a1[0]:.1f},{a1[1]:.1f} L{a2[0]:.1f},{a2[1]:.1f}" stroke="#7B868D" stroke-width="1.3"/>')
    o.append(f'<circle cx="{BX}" cy="{TY}" r="{r_ind}" fill="none" stroke="#4F5A61" stroke-width="1.8"/>')
    o.append(f'<clipPath id="pcZoom"><circle cx="{BX}" cy="{BY}" r="{BR}"/></clipPath>')
    o.append(f'<circle cx="{BX}" cy="{BY}" r="{BR + 2}" fill="#FFFFFF"/>')
    z = [f'<g clip-path="url(#pcZoom)"><rect x="{BX - BR}" y="{BY - BR}" width="{2 * BR}" height="{2 * BR}" fill="url(#pcLu)"/>']
    # The close-up magnifies the vessel's mix: more sugar than insulin, both crowded, a few red cells
    # (the vessel carries 16 sugars, 12 insulin, 6 red cells).  Every symbol asked for must be drawn.
    kinds = ["r"] * 3 + ["g"] * 10 + ["i"] * 8
    size = {"r": 9.2, "g": 6.3, "i": 6.0}
    items = [size[k] for k in kinds]
    for seed in range(29, 400):
        zr = random.Random(seed)
        zp = scatter(zr, items, (BX - BR + 2, BY - BR + 2, BX + BR - 2, BY + BR - 2),
                     lambda x, y, r: math.dist((x, y), (BX, BY)) < BR - r - 2.5, pad=2.0)
        if len(zp) == len(items):
            break
    assert len(zp) == len(items), f"close-up: placed {len(zp)} of {len(items)} symbols"
    for (x, y, r), k in zip(zp, kinds):
        if k == "r":
            z.append(red_cell(x, y, zr.uniform(-25, 25), 0.72))
    for (x, y, r), k in zip(zp, kinds):
        if k == "i":
            z.append(insulin(x, y, size["i"]))
        elif k == "g":
            z.append(glucose(x, y, size["g"]))
    z.append("</g>")
    o.append("".join(z))
    o.append(f'<circle cx="{BX}" cy="{BY}" r="{BR}" fill="none" stroke="#4F5A61" stroke-width="2"/>')
    o.append(T(BX, BY + BR + 15, "close-up of the blood", 10, 600, "#56626A", "middle", italic=True))

    # ---------------------------------------------------------- uterus, tubes, ovaries, androgens
    o.append(reproductive(UX, UY, US))
    for side in (-1, 1):
        for lx, ly, r in [(126, 60, 5.4), (136, 72, 5.0), (146, 84, 4.6)]:
            o.append(androgen(UX + side * lx * US, UY + ly * US, r))
        o.append(T(UX + side * 146 * US, UY + 104 * US, "extra androgens", 10, 700, AND_EDGE, "middle", italic=True))

    # ---------------------------------------------------------- labels and step markers
    o.append(T(214, 162, "Pancreas", 11.5, 800, "#7A4318", "middle"))
    # under the C-loop of the duodenum, well away from the zoom caption (no leader needed)
    o.append(T(PX + 80 * PS, H_ART - 8, "small intestine", 10, 600, "#8A5A50", "middle", italic=True))
    for side in (-1, 1):
        o.append(T(UX + side * 92 * US, UY + 80 * US, "Ovary", 11, 800, "#8A2F3A", "middle"))
    o.append(T(UX, UY + 134 * US + 15, "Uterus", 11, 800, "#8A2F3A", "middle"))
    o.append(marker(120, 78, 1, c1) + marker(BX, 72, 2, c1) + marker(UX, 60, 3, c1))
    return svg(W_ART, H_ART, "".join(o),
               "The pancreas makes insulin. A blood vessel carries sugar and insulin from the pancreas to both ovaries; "
               "each branch ends in an arrow touching an ovary. A zoom circle shows extra sugar and extra insulin in the "
               "blood. The ovaries hold many small follicles and release extra androgens.")


# ================================================================== HTML blocks under the art
def sw(markup, w=18, h=16, vb="-9 -8 18 16"):
    return f'<svg width="{w}" height="{h}" viewBox="{vb}" aria-hidden="true">{markup}</svg>'


def pan_mini():
    """The drawing's own pancreas outline (P_OUT) at key size: tan septa fill, lighter lobules, same edge."""
    s, cx, cy = 0.088, 139, 61
    out = [((x - cx) * s, (y - cy) * s) for x, y in P_OUT]
    smooth = crs(out, closed=True, per=10)
    dots = []
    for j in range(-3, 4):
        for i in range(-8, 9):
            x, y = i * 2.15 + (1.07 if j % 2 else 0), j * 1.9
            if inside((x, y), smooth) and min(math.dist((x, y), q) for q in smooth) > 1.05:
                dots.append(f'<circle cx="{x:.2f}" cy="{y:.2f}" r=".82" fill="{P_LOBES[(i + j) % len(P_LOBES)]}"/>')
    return (f'<path d="{cr_d(out, True)}" fill="{P_SEPTA}"/>{"".join(dots)}'
            f'<path d="{cr_d(out, True)}" fill="none" stroke="{P_EDGE}" stroke-width=".9" stroke-linejoin="round"/>')


def tube_mini():
    """A Fallopian tube at key size: the tube widening outward to its funnel and fringe."""
    fr = "".join(f'<path d="{frond(1.2, y, ang, ln, 1.05, curl, .45)}" fill="{U_BASE}" stroke="{U_EDGE}" stroke-width=".45"/>'
                 for y, ang, ln, curl in ((-2.4, -16, 3.2, -.2), (-.9, 6, 4.2, .2), (.7, 26, 3.8, .4), (2.2, 46, 3.0, .4)))
    return (f'<path d="M-10.5,5 C-7,-3 -1,-5 4.2,-1.8" fill="none" stroke="{U_EDGE}" stroke-width="4.2" stroke-linecap="round"/>'
            f'<path d="M-10.5,5 C-7,-3 -1,-5 4.2,-1.8" fill="none" stroke="{U_BASE}" stroke-width="2.5" stroke-linecap="round"/>'
            f'<g transform="translate(4.2,-1.8) rotate(32)">{fr}'
            f'<path d="M-1.2,-1.9 C.2,-2 1,-2.6 1.6,-3.3 Q2,0 1.6,3.3 C1,2.6 .2,2 -1.2,1.9Z" fill="{U_BASE}" stroke="{U_EDGE}" '
            'stroke-width=".6" stroke-linejoin="round"/></g>')


def key():
    ves_mini = (f'<rect x="-8.5" y="-5.5" width="17" height="11" rx="2" fill="{V_WALL}" stroke="{V_OUT}" stroke-width="1"/>'
                f'<rect x="-8.5" y="-2.8" width="17" height="5.6" fill="{V_LUM}"/>')
    # Column-major, 2 rows: what is in the blood, then the blood itself, then the two organs' parts
    # that need words, then the ovary parts.  Long entries share a column with short ones.
    # Both entries in a column get the same swatch width, so their words start on one line.
    W2, VB2 = 24, "-12 -8 24 16"
    items = [
        (sw(glucose(0, 0, 6.2)), "Glucose", "sugar in the blood"),
        (sw(insulin(0, 0, 6)), "Insulin", "lets sugar into cells"),
        (sw(red_cell(0, 0, 0, .64)), "Red blood cell", ""),
        (sw(ves_mini), "Blood vessel", ""),
        (sw(pan_mini(), W2, 16, VB2), "Pancreas", "makes insulin"),
        (sw(androgen(0, 0, 6.4), W2, 16, VB2), "Androgens", "male-type hormones"),
        (sw(follicle(0, 0, 5.6), W2, 16, VB2), "Follicle", "the &ldquo;cysts&rdquo;: stalled egg sacs"),
        (sw(tube_mini(), W2, 16, VB2), "Fallopian tube", "carries eggs to the uterus"),
    ]
    cells = "".join(f'<span>{m}<b>{a}</b>{(" " + b) if b else ""}</span>' for m, a, b in items)
    return f'<div class="pc-key"><em>KEY</em>{cells}</div>'


def steps():
    st = [("The pancreas makes insulin.", "Insulin moves sugar out of the blood and into your cells for fuel."),
          ("Cells stop listening to insulin.", "Sugar stays in the blood, so the pancreas pumps out even more."),
          ("Extra insulin reaches the ovaries.", "They make extra androgens, and eggs stay stuck in small "
                                                 "follicles (the &ldquo;cysts&rdquo;).")]
    return '<div class="pc-steps">' + "".join(
        f'<div><span class="pc-n">{i + 1}</span><p><b>{a}</b> {b}</p></div>' for i, (a, b) in enumerate(st)) + "</div>"


def ic(body, size="0.36in", sw_=3):
    return (f'<svg class="ic" viewBox="0 0 64 64" style="width:{size};height:{size}" fill="none" stroke="currentColor" '
            f'stroke-width="{sw_}" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{body}</svg>')


# Extra facial or body hair: a woman's profile (hair in a bun) with six long hairs along the upper
# lip, chin and jaw.
FACE_HAIR = ('<path d="M42 57v-9c5-3 8-8 8-15 0-11-8-19-18-19-8.5 0-14.5 5.5-16 13l-3.5 8.5 4 1.2v4.3c0 3 2.2 5 5 5h3.5v11"/>'
             '<path d="M24.5 15.5c5-3 13-3.5 19 1.5"/><circle cx="48" cy="15.5" r="5.5"/>'
             '<path d="M15.4 37.8l-3.6 2.4M15.6 40.2l-3.4 2.6M16.4 42.8l-3.6 3.4M18.2 45l-2.4 4.6M21 46.6l-1 5.2M23.4 47l.2 4"'
             ' stroke-width="2.3"/>')
# Thinning scalp hair: the head seen from above (ears at the sides, nose at the front).  Hair is a
# soft mass on both sides; the part has widened into a pale wedge, with two lone strands left in it.
SCALP_THIN = ('<path d="M32 11c-1.6 0-3 .1-4.4.4C19.6 13.2 14 21.6 14 32.4c0 6.4 2 12 5.4 15.6 2-1.8 5.2-3 8.6-3.4'
              'C28.8 40 28 35 27.8 30.6 27.6 23.6 29.4 16 32 11z" fill="currentColor" stroke="none" opacity=".5"/>'
              '<path d="M32 11c1.6 0 3 .1 4.4.4C44.4 13.2 50 21.6 50 32.4c0 6.4-2 12-5.4 15.6-2-1.8-5.2-3-8.6-3.4'
              'C35.2 40 36 35 36.2 30.6 36.4 23.6 34.6 16 32 11z" fill="currentColor" stroke="none" opacity=".5"/>'
              '<path d="M32 10c-10 0-18 9.6-18 22.6S22 56 32 56s18-10.4 18-23.4S42 10 32 10z"/>'
              '<path d="M14.2 29c-2.6.8-2.6 7.4 0 8.4M49.8 29c2.6.8 2.6 7.4 0 8.4"/><path d="M29.5 56.6c1 1.8 4 1.8 5 0"/>'
              '<path d="M19.6 47.8c3.8-3.2 8.2-3.8 12.4-3.8s8.6.6 12.4 3.8"/>'
              '<path d="M31.4 20l1.4 4.6M32.8 30.5l-1.2 4.4" stroke-width="2"/>')
# Dark skin patches (acanthosis nigricans): head and shoulders from behind (hair bun), with a dark,
# blotchy patch across the back of the neck (no beads or dots, so it cannot read as a necklace).
DARK_PATCH = ('<path d="M24.6 29.4C27 28.6 29.2 30.2 32 29.8 34.8 29.4 37 28.6 39.4 29.6 40.6 32 39.8 34.6 40.6 37.2 38 38.6 '
              '35.4 37.6 32.6 38.4 29.8 39 27 37.8 23.8 38 24.6 35.2 23.6 32.2 24.6 29.4Z" fill="currentColor" stroke="none" '
              'opacity=".6"/>'
              '<circle cx="32" cy="18.5" r="11"/><circle cx="32" cy="6.2" r="3.6"/>'
              '<path d="M26.5 28.5v8M37.5 28.5v8"/>'
              '<path d="M26.5 36.5c-8 .8-14 4.6-16 12.5v8M37.5 36.5c8 .8 14 4.6 16 12.5v8"/>')
# Trouble getting pregnant: a pregnant woman in profile, hand on the belly.
PREGNANT = ('<circle cx="29" cy="10.5" r="5.8"/>'
            '<path d="M26.5 18c-3 7-3.6 15-1.6 22 1.4 5 1.4 11 .6 18"/>'
            '<path d="M32 18c2.2 3 3 6.6 2.4 10.4 8.4 1.8 13 7.8 12.4 14.2-.6 6.4-6.2 9.4-13.4 9.2l.8 6.2"/>'
            '<path d="M28 23c.6 6 3.4 11.4 8.6 13.6"/>')


def ring():
    # Signs a reader can notice herself.  [OWH] Office on Women's Health PCOS fact sheet and NIH NICHD
    # "What are the symptoms of PCOS?": irregular periods, hirsutism, acne, thinning scalp hair, weight
    # gain, darkened skin along neck creases and body folds (acanthosis nigricans, a sign of insulin
    # resistance), skin tags, infertility; [GUIDE23] adds anxiety and depression.
    items = [(icon("calendar", "0.34in", sw=3), "Irregular or<br>missed periods"),
             (icon("acne", "0.34in", sw=3), "Acne"),
             (ic(FACE_HAIR, "0.36in"), "Extra facial or<br>body hair"),
             (ic(SCALP_THIN, "0.36in"), "Thinning<br>scalp hair"),
             (icon("waist", "0.34in", sw=3), "Weight gain<br>at the waist"),
             (icon("battery", "0.34in", sw=3), "Fatigue"),
             (icon("brain", "0.34in", sw=3), "Mood changes,<br>anxiety"),
             (ic(PREGNANT, "0.36in"), "Trouble getting<br>pregnant"),
             (ic(DARK_PATCH, "0.36in"), "Dark skin patches<br>(neck, armpits)"),
             (icon("meter", "0.34in", sw=3), "Blood sugar<br>swings")]
    cells = "".join(f'<div class="pc-rg"><div class="pc-c">{s}</div><span>{lab}</span></div>' for s, lab in items)
    return f'<div class="pc-head">SIGNS AND SYMPTOMS</div><div class="pc-ring">{cells}</div>'


def facts():
    return ('<div class="pc-facts">'
            '<div class="pc-fbox"><h4>PCOS facts</h4><p>'
            # [WHO23] 10-13% of women of reproductive age (Rotterdam 11.9% in [MARCH10]) -> "about 1 in 8"
            # (12.5%, inside the range; "up to 1 in 8" would understate the 13% top);
            # [WHO23] up to 70% undiagnosed ([MARCH10]: 68-69% had no prior diagnosis) -> "up to 7 in 10".
            'About <b>1 in 8</b> women of childbearing age has PCOS, and up to <b>7 in 10</b> of them have never been '
            'diagnosed. '
            # [GUIDE23] adults: 2 of 3 = irregular cycles; clinical or biochemical high androgens; polycystic ovaries
            # on ultrasound OR a high AMH blood test; other causes excluded.  [PENA25] teens: irregular cycles AND
            # high androgens (no ultrasound, no AMH), so the 2-of-3 line says "Adults".
            'Adults are diagnosed with <b>2 of 3</b>: irregular periods, high androgens (a blood test or signs like extra '
            'hair) or many follicles on ultrasound (or a high AMH blood test), once other causes are ruled out. '
            'You can have PCOS without&nbsp;&ldquo;cysts.&rdquo;</p>'
            # [GUIDE23] broader features: metabolic risk (type 2 diabetes), cardiovascular disease, sleep apnoea, mood.
            '<p class="pc-why"><b>Why it matters:</b> PCOS raises the risk of type 2 diabetes, heart disease and sleep apnea '
            '(breathing pauses during sleep), so ask {who} about checking your blood sugar.</p></div>'
            '<div class="pc-fbox"><h4>Risk factors</h4><ul>'
            # [GUIDE23] strong family clustering; first-degree relatives with PCOS or type 2 diabetes.
            '<li><b>Runs in families:</b> a mother or sister with PCOS or type 2 diabetes raises your risk.</li>'
            # [STEPTO13] insulin resistance in 75% of LEAN women with PCOS; [GUIDE23] PCOS occurs across all BMIs.
            '<li><b>Not just weight:</b> PCOS happens at every body size, even at a healthy weight.</li>'
            # [GUIDE23] lifestyle (diet, activity, sleep, stress) worsens or eases PCOS features; it is not shown to
            # cause PCOS.  Hormone-disrupting chemicals (BPA in some plastics, phthalates in fragrances): higher levels
            # go with higher androgens in women with PCOS in observational studies only, hence "can make it worse".
            '<li><b>Can make it worse (you can change):</b> a high-sugar, low-nutrient diet, sitting most of the day, '
            'poor sleep, chronic stress and hormone-disrupting chemicals (in some plastics and fragrances).</li></ul></div></div>')


def front(t, ed):
    return (f'<div class="pcf"><div class="pc-art">{art_pcos(t)}</div>{steps()}{key()}{ring()}{facts()}</div>')


CSS = r"""
.pcf .pc-art svg{display:block;width:100%;height:auto}
.pcf .pc-steps{display:grid;grid-template-columns:1fr 1fr 1fr;gap:0.12in;margin:0.04in 0 0}
.pcf .pc-steps>div{display:flex;gap:6px;align-items:flex-start}
.pcf .pc-n{flex:none;width:0.2in;height:0.2in;border-radius:50%;background:var(--c1);color:#fff;font:800 8pt Inter,sans-serif;
  display:flex;align-items:center;justify-content:center;margin-top:1px}
.pcf .pc-steps p{margin:0;font-size:8.2pt;line-height:1.3;color:#2B3236}
.pcf .pc-steps b{color:var(--deep)}
.pcf .pc-key{display:grid;grid-template-rows:auto auto;grid-auto-flow:column;justify-content:space-between;align-items:center;
  gap:3px 8px;margin-top:0.07in;padding:5px 10px 5px 12px;border:1px solid #D9DEE2;border-radius:8px;background:#FFFFFF;font-size:7.6pt;
  line-height:1.2;color:#3A4247}
.pcf .pc-key em{grid-row:span 2;font:800 7.4pt Inter,sans-serif;letter-spacing:.14em;color:#2B3236;font-style:normal}
.pcf .pc-key span{display:inline-flex;align-items:center;gap:4px;white-space:nowrap}
.pcf .pc-key svg{flex:none;display:block}
.pcf .pc-key b{color:#1F2A2E;font-weight:800}
.pcf .pc-head{font:900 12pt Merriweather,Georgia,serif;color:var(--c1);text-align:center;margin:0.1in 0 0.05in;letter-spacing:.02em}
.pcf .pc-ring{display:grid;grid-template-columns:repeat(5,1fr);gap:0.06in 0.06in}
.pcf .pc-rg{display:flex;flex-direction:column;align-items:center;text-align:center}
.pcf .pc-c{width:0.55in;height:0.55in;border-radius:50%;background:#F1E7E2;display:flex;align-items:center;justify-content:center;
  color:#8A5A52;box-shadow:0 0 0 2px #fff,0 0 0 3px #E8D8D1}
.pcf .pc-rg span{font-size:7.8pt;line-height:1.2;margin-top:3px;color:#3A4247}
.pcf .pc-facts{display:grid;grid-template-columns:1.5fr 1fr;gap:0.14in;margin-top:0.08in}
.pcf .pc-fbox h4{margin:0 0 4px;background:var(--c1);color:#fff;font:800 8.2pt Inter,sans-serif;letter-spacing:.08em;
  text-transform:uppercase;padding:3px 10px;border-radius:3px}
.pcf .pc-fbox p,.pcf .pc-fbox li{font-size:8.2pt;line-height:1.33;margin:0;color:#2B3236}
.pcf .pc-fbox p.pc-why{margin-top:4px}
.pcf .pc-fbox ul{margin:0;padding-left:13px}
.pcf .pc-fbox li{margin-bottom:1px}
.pcf .pc-fbox b{color:var(--deep)}
/* Back page, this sheet only (keyed to the Myo-Inositol Complex photo, which no other sheet uses):
   keep each count with its unit in "Your daily rhythm", so "3 capsules" never splits across lines. */
.sheet.back:has(img[src$="nd-inositol.png"]) .slot li em{white-space:nowrap}
"""

SHEET = {
    "slug": "pcos", "code": "ND-CM-204", "theme": "metab", "series": "Metabolic Health Series",
    "order": 6,
    "title": "Polycystic Ovary Syndrome", "sub": "PCOS",
    # [STEPTO13] insulin resistance in 75% of lean and 95% of overweight women with PCOS -> "most women".
    "intro": ("PCOS is a common hormone condition. The ovaries make more <b>androgens</b> (male-type hormones such as "
              "testosterone; women normally make a little) than usual. That can upset periods, ovulation (releasing an egg) "
              "and fertility, and it shows up in skin, hair, weight and mood. Genes play a part, but in most women with PCOS "
              "<b>insulin resistance</b> (cells stop answering insulin) helps drive it. That is why food, movement, sleep and "
              "stress change how PCOS behaves."),
    "front": front,
    "css": CSS,
    # ---- back: kept exactly as the first draft (sheets.py) until the product pass
    "back": {
        "life_title": "Lifestyle Recommendations", "style": "circle",
        "life": [("plate", "Diet", "Protein and fiber at every meal. Limit refined sugar and starch to steady blood sugar."),
                 ("dumbbell", "Exercise", "150 minutes a week of activity plus 2 strength days improves insulin sensitivity."),
                 ("moon", "Sleep", "Seven to eight hours a night supports weight and healthy hormone production."),
                 ("plastic", "Limit hormone disruptors", "Glass or steel containers, never heat food in plastic, fragrance-free products.")],
        "cols": [
            {"p": "gluco_ir", "need": "Blood sugar and insulin", "needsub": "dihydroberberine, chromium, ALA", "start": True,
             "bullets": ["Supports healthy glucose metabolism", "Supports insulin sensitivity"], "dose": "dose_from_db"},
            {"p": "inositol", "need": "Insulin signaling", "needsub": "inositol",
             "bullets": ["Supports healthy ovarian function", "Supports insulin signaling"], "dose": "dose_from_db"},
            {"p": "d3_5000_k2", "need": "Vitamin D", "needsub": "D3 with K2",
             "bullets": ["Low vitamin D is common in PCOS", "Supports hormone and immune health"], "dose": "dose_from_db"},
            {"p": "omega_1000", "need": "Calm inflammation", "needsub": "omega-3 fatty acids",
             "bullets": ["Supports a healthy inflammatory response", "Supports healthy triglycerides"], "dose": "dose_from_db"},
            {"p": "ultrabiotic_dms", "need": "Gut and hormones", "needsub": "multi-strain probiotic",
             "bullets": ["Your gut bacteria help process hormones", "Seven strains, one capsule"], "dose": "1 capsule daily", "dosesub": "same time each day"},
        ],
        "rx": ["<b>Birth control pills</b> can lower B6, B12, folate, magnesium and zinc. Ask about a quality multi.",
               "<b>Metformin</b> lowers B12 over time. Ask for a yearly check.",
               "<b>Spironolactone</b> raises potassium: avoid potassium supplements unless prescribed."],
    },
}
