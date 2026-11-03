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
Final front review fixes (2026-11-03, third round; the approved layout is unchanged):
  - Vessel: one "Bloodstream" runs the full width with a cut end at each side, and BOTH ovaries get
    the same side branch: same 20-unit width, same corner radius, same rounded fillets where it
    leaves the trunk, mirrored about the uterus (the uterus group moved 14 units left to make room
    for the right cut end).  No taper and no L-bend any more, so nothing looks pinched.
  - Molecules in the bloodstream are half size next to the red cells (9 red cells now); the close-up
    says "not to scale"; the key reads "Bloodstream: carries insulin everywhere".
  - Insulin leaving the pancreas: dots sit clear of the dashed lines, and each arrow tip touches
    the bloodstream's outline.
  - Fallopian tubes: the tube itself widens into the funnel (no seam), with six soft, wavy fimbriae
    of different lengths; the longest reaches down onto the ovary.
  - Ring: new front-view "Thinning scalp hair" (wide bare part, a few strands), "Dark skin patches"
    as a velvety patch on the side of the neck, a face with raised spots for "Acne", a waist that
    bulges with a tape measure, a one-line pregnancy test for "Trouble getting pregnant", and
    "Skin tags" (sourced) in place of "Blood sugar swings" (not in the cited symptom lists).
  - Words: cells "answer insulin poorly"; the ovaries make the androgens; "every body size" moved
    to the facts; weight gain and diabetes added to the risk factors; the pharmacy edition sends the
    blood sugar test to "your doctor".
Independent review fixes (2026-11-03, fourth round):
  - Public repo: the source notes cite documents (NutriDyn GLC 2023 PCOS protocol, NutriDyn GLC 2026
    PMOS protocol, Asher's emails and pages), never a speaker, a Gmail thread id or a private link.
  - Front: the 2026 rename (PCOS, now also called PMOS) in the subtitle and the facts; AMH glossed; the
    endometrial line ([GUIDE23H] 1.11); "Why it matters" runs full width under both fact boxes.
  - Art: the zoom circle moved 8 units left, clear of the left branch, and the small circle on the
    bloodstream holds the same three things the close-up shows; captions are upright (no faked italic).
  - Icons: thinning hair lies flat across a pale part; skin tags rise from a curved edge of skin; the
    pregnancy test is a slim stick with a wide window and a cap.
  - Back: omega claims are ND416's own (no triglyceride claim); Berberine Pro's lunch dose sits in the
    Morning box; the check panel names the fenugreek in Myo-Inositol Complex for pregnancy, sends a
    blood-sugar medicine change to the doctor who prescribes it, warns about vitamin K and warfarin
    and about berberine's drug enzymes in both editions, and gives B12 and short-term vitamin D an
    action; product names get two lines in every column so the rows line up.
  - PRINT HOLD: the Myo-Inositol Complex photo is a soft stopgap (see products.d/pcos.json), so the
    sheet is web-only until the real bottle is staged.
Glucose (purple hexagon) and insulin (gold dot) use the same symbols as the insulin-resistance
sheet, so the Metabolic Health Series reads as one system.
Every SVG id starts with "pc" and every CSS class with "pc-" (all under .pcf), so nothing
collides with other sheets in the all-sheets bundle.

SOURCES (tags appear in comments next to each number on the page)
  [GUIDE23H] Teede HJ et al. Recommendations from the 2023 International Evidence-based Guideline
             for PCOS. Hum Reprod 2023;38:1655-79. doi:10.1093/humrep/dead156, full text PMC10477934
             (read on PubMed 2026-11-03): "PCOS prevalence is between 10 to 13%" (introduction) and
             rec 1.6.1 "10-13% globally"; 1.9.8 women with type 1 and type 2 diabetes have an increased
             risk of PCOS; 1.9.9 the 75-g OGTT is the most accurate glucose test in PCOS; 1.8.3 a lipid
             profile for all at diagnosis; 1.10.2 sleep apnea symptoms "snoring in combination with
             waking unrefreshed from sleep, daytime sleepiness or fatigue"; 3.4.5 "at least 30 minutes
             daily on most days"; 4.7.1 and 5.8.1-5.8.3 inositol (limited harm; experimental for
             fertility; safety not known).  Same guideline as [GUIDE23].
  [WHO23]    WHO fact sheet "Polycystic ovary syndrome" (2023): up to 70% of affected women
             undiagnosed worldwide.  who.int is outside this machine's allowed network (re-tried
             2026-11-03), so the figure is cross-checked against [MARCH10]; the prevalence figure on
             the page now cites [GUIDE23H] instead.
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
  [PMOS26]   The 2026 rename, all read on PubMed 2026-11-03.  Bahri-Khomami M et al. Am J Obstet
             Gynecol 2026;235:999-1002, PMID 42665241, doi:10.1016/j.ajog.2026.08.024 (renamed
             polyendocrine metabolic ovarian syndrome after a consensus endorsed by 56 professional and
             patient organizations; the ovarian look "reflects numerous arrested antral follicles, not
             pathologic cysts"; "Diagnostic criteria remain unchanged").  Piltonen TT et al. Hum Reprod
             2026, PMID 42905432, doi:10.1093/humrep/deag150 ("in May 2026, a multi-step global consensus
             process culminating in a Lancet statement renamed the condition"; the guideline update that
             consolidates it is due in 2028).  Castelo-Branco C et al. (European Society of Gynaecology
             position paper) Gynecol Endocrinol 2026;42:2695512, PMID 42367168,
             doi:10.1080/09513590.2026.2695512 ("prioritizing patient communication" and "prolonged dual
             terminology use"), hence PCOS stays the headline and PMOS is added once.

  Back-page safety sources (all read 2026-11-03):
  [CHAN93]   Chan E. Biol Neonate 1993;63:201-8. doi:10.1159/000243932 (berberine displaces bilirubin;
             "best avoided in jaundiced neonates and pregnant women").
  [GUO12]    Guo Y et al. Eur J Clin Pharmacol 2012;68:213-7. doi:10.1007/s00228-011-1108-2 (berberine
             300 mg three times daily for 2 weeks lowered CYP2D6, 2C9 and 3A4 activity).
  [AROD16]   Aroda VR et al. J Clin Endocrinol Metab 2016;101:1754-61. doi:10.1210/jc.2015-3754
             (long-term metformin and B12 deficiency; routine B12 testing should be considered).
  [PALM13]   Palmery M et al. Eur Rev Med Pharmacol Sci 2013;17:1804-13, PMID 23852908 (oral
             contraceptives deplete folic acid, B2, B6, B12, C, E, magnesium, selenium and zinc).
  [GRANT10]  Grant P. Phytother Res 2010;24:186-8. doi:10.1002/ptr.2900 (spearmint tea twice a day,
             42 women, 30 days: free and total testosterone fell; the NutriDyn GLC 2026 PMOS protocol,
            , uses it: "Spearmint: tea or extract twice daily").
  [OUZIR16]  Ouzir M et al. Food Chem Toxicol 2016;96:145-54, PMID 27498339, doi:10.1016/j.fct.2016.08.003
             (review: teratogenic, anti-fertility, anti-implantation and abortifacient findings, so
             fenugreek "is not recommended for use during pregnancy"; read on PubMed 2026-11-03).
  [KHALKI10] Khalki L et al. J Ethnopharmacol 2010;131:321-5, PMID 20600755, doi:10.1016/j.jep.2010.06.033
             (fenugreek seed extract through pregnancy in mice: more foetal deaths, smaller litters,
             malformations; read on PubMed 2026-11-03).
  [ADA-S9]   ADA Standards of Care in Diabetes, Section 9: consider periodic vitamin B12 measurement on
             long-term metformin (with [AROD16]); the insulin-resistance sheet cites the same.
  Labels: the five NutriDyn sell sheets (ND680, ND1130, ND382, ND416, ND460), opened from Dropbox;
  details and claim wording per product in build/products.d/pcos.json.

BACK (product pass, 2026-11-03): five products, the competitor's count, all from NutriDyn's own PCOS
protocols (NutriDyn GLC 2023 PCOS protocol; NutriDyn GLC 2026 PMOS
protocol; Asher's PCOS handout and his Myo-Inositol Complex email to a
practitioner, 2026-09-25).  Competitor categories: vitamin D -> D3 5000 with K2, omega-3 -> Omega
Pure EPA-DHA 1000, berberine -> Berberine Pro; melatonin and turmeric have no place in these protocols,
so Myo-Inositol Complex and UltraBiotic Daily Multi-Strain (both protocol picks) take those columns.
Berberine Pro, not Gluco IR: it is the competitor's own category, it is on both PCOS protocols, it has
no biotin (biotin can distort the hormone tests PCOS is diagnosed and followed with), and it does not
double the chromium and fenugreek already in Myo-Inositol Complex.
"""
import math
import os
import random

from kit import DIAMOND, icon
from svgkit import T, svg, label_bg


def claim(text):
    """A back-page claim bullet ending in the drawn FDA-disclaimer diamond (kit.DIAMOND), bound to its last
    word so the diamond never sits on a line of its own: Chromium will break between the kit's &nbsp; and an
    inline SVG.  Every bullet in a column must use this, since the kit then adds no marks of its own there."""
    head, _, last = text.rpartition(" ")
    return f'{head} <span class="nw">{last}&nbsp;<span class="mark">{DIAMOND}</span></span>'

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
    return (f'<g transform="translate({x:.1f},{y:.1f}) rotate({rot:.1f}) scale({s})"><ellipse rx="12.5" ry="7" fill="url(#pcRc)" '
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


def frond(p0, d, length, bw, bend, wave, tipw=1.6, n=16):
    """One fimbria: a soft finger from the funnel rim along unit direction d, tapering from bw to a
    rounded tip tipw wide.  It droops sideways by `bend` toward its tip (positive = toward the ovary)
    and ripples by `wave`, so the fringe looks soft rather than like stiff spikes."""
    px, py = -d[1], d[0]
    cl, ws = [], []
    for k in range(n + 1):
        u = k / n
        off = bend * u * u + wave * math.sin(2 * math.pi * u)
        cl.append((p0[0] + d[0] * length * u + px * off, p0[1] + d[1] * length * u + py * off))
        ws.append(bw + (tipw - bw) * u)
    L, R = sides(cl, ws)
    (cx, cy), (tx, ty) = cl[-1], tangents(cl)[-1]
    nx, ny, r = -ty, tx, tipw / 2
    tip = [(cx + r * (nx * math.cos(a) + tx * math.sin(a)), cy + r * (ny * math.cos(a) + ty * math.sin(a)))
           for a in (math.pi * j / 8 for j in range(1, 8))]
    return poly_d(L + tip + R[::-1])


# fimbriae: (rim position, fan angle, length, base width, bend, wave).  Six soft fingers of uneven
# length fan out of the funnel rim; positive angles lean toward the ovary, and the last, longest one
# (the fimbria that holds the ovary) reaches down onto it.
FRONDS = [(-7.4, -24, 7.4, 3.4, -0.7, 0.6), (-4.4, -9, 10.6, 3.6, 0.9, -0.7), (-1.4, 5, 8.2, 3.6, -0.6, 0.65),
          (1.6, 17, 11.4, 3.6, 1.0, -0.65), (4.6, 30, 8.8, 3.5, 0.7, 0.6), (7.3, 44, 15.0, 3.8, 1.7, -0.75)]
FUNNEL = 9.0      # the tube's last 9 units widen into the funnel (infundibulum)


def tube_geom():
    """Centreline and widths of the Fallopian tube: narrow at the uterus, gently wider outward, then
    flaring smoothly into the funnel over its last FUNNEL units (one outline, so no seam)."""
    c = resample(crs(TUBE, per=16), 1.5)
    n = len(c)
    cum = [0.0]
    for a, b in zip(c, c[1:]):
        cum.append(cum[-1] + math.dist(a, b))
    w = []
    for k in range(n):
        u = max(0.0, (cum[k] - (cum[-1] - FUNNEL)) / FUNNEL)
        w.append(6.2 + 4.2 * (k / (n - 1)) ** 1.3 + 8.6 * u * u)
    return c, w, cum


def tube_shape():
    """The tube (drawn under the ovary) and, separately, the fringe: the fimbriae plus the funnel end
    of the same tube outline laid over them, drawn after the ovary so the fringe drapes over it."""
    c, w, cum = tube_geom()
    tube = f'<path d="{ribbon(c, w)}" fill="{U_BASE}" stroke="{U_EDGE}" stroke-width="1.5" stroke-linejoin="round"/>'
    (ex, ey), (tx, ty) = c[-1], tangents(c)[-1]
    nx, ny = -ty, tx
    f = []
    for k, (y, ang, ln, bw, bend, wav) in enumerate(FRONDS):
        a = math.radians(ang)
        d = (tx * math.cos(a) + nx * math.sin(a), ty * math.cos(a) + ny * math.sin(a))
        p0 = (ex + nx * y - tx * 1.8, ey + ny * y - ty * 1.8)          # starts just inside the funnel
        f.append(f'<path d="{frond(p0, d, ln, bw, bend, wav)}" fill="{"#E3929A" if k % 2 else U_BASE}" '
                 f'stroke="{U_EDGE}" stroke-width=".95" stroke-linejoin="round"/>')
    # the funnel end of the tube again, on top of the frond roots: fill, plus its two side edges only,
    # so it continues the tube with no line across it
    k0 = next(k for k, s in enumerate(cum) if s >= cum[-1] - 13)
    L, R = sides(c[k0:], w[k0:])
    f.append(f'<path d="{poly_d(L + R[::-1])}" fill="{U_BASE}"/>')
    for side in (L, R):
        f.append(f'<path d="{poly_d(side, closed=False)}" fill="none" stroke="{U_EDGE}" stroke-width="1.5" '
                 'stroke-linecap="round" stroke-linejoin="round"/>')
    # the opening (ostium), a soft curve just inside the rim
    hw = w[-1] / 2 - 2.2
    a_ = (ex - nx * hw - tx * .9, ey - ny * hw - ty * .9)
    b_ = (ex + nx * hw - tx * .9, ey + ny * hw - ty * .9)
    q_ = (ex + tx * 1.6, ey + ty * 1.6)
    f.append(f'<path d="M{a_[0]:.2f},{a_[1]:.2f} Q{q_[0]:.2f},{q_[1]:.2f} {b_[0]:.2f},{b_[1]:.2f}" fill="none" '
             'stroke="#B9525C" stroke-width=".9" opacity=".7"/>')
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
UX, UY, US = 552, 82, 0.94           # uterus group (14 left of centre-right, so the bloodstream can end past it)
TY, TW, WALL = 28, 34, 5              # bloodstream centre line, width, wall thickness
TX0, TX1 = 14, 752                    # the bloodstream's two cut ends
BW, RF = 20.0, 6.0                    # branch width; radius of the fillets where a branch leaves the trunk
BX, BY, BR = 310, 144, 54             # zoom circle (clear of the left branch; the pancreas tail and label stay clear)
R_IND = 21                            # the small circle on the bloodstream that the zoom circle magnifies


def fillet(xc, yb, half, r, side):
    """Concave corner piece where a branch (centre x xc, half-width half) leaves the trunk's bottom
    edge yb: bounded by a quarter circle of radius r tangent to both edges.  side +1 = right corner,
    -1 = left.  It overlaps the trunk and the branch slightly, so the layers join without a gap."""
    xe = xc + side * half
    cx, cy = xe + side * r, yb + r
    return (f"M{xe - side * .8:.2f},{yb - 1.6:.2f} L{cx:.2f},{yb - 1.6:.2f} L{cx:.2f},{yb:.2f} "
            f"A{r:.2f},{r:.2f} 0 0 {0 if side > 0 else 1} {xe:.2f},{cy:.2f} L{xe - side * .8:.2f},{cy:.2f}Z")


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

    # One bloodstream runs the full width (cut ends at both sides: it carries insulin everywhere).  Each
    # ovary gets the SAME side branch, mirrored about the uterus: it leaves the trunk straight down
    # through two rounded fillets, then a true arc of radius R2 turns it into a straight run of S units
    # that ends in the arrowhead.  Solved backwards from each head, so both drops sit at mirrored x.
    S, R2 = 14.0, 18.0
    wave = crs([(TX0, TY), (100, TY - 1), (200, TY + 1), (300, TY - 1), (400, TY), (500, TY), (600, TY - 1), (680, TY),
                (TX1, TY)], per=16)
    tc = resample(wave, 2.0)

    def yc(x):
        """Height of the trunk's centre line at x."""
        for p, q in zip(tc, tc[1:]):
            if p[0] <= x <= q[0]:
                return p[1] + (q[1] - p[1]) * (x - p[0]) / ((q[0] - p[0]) or 1.0)
        return TY

    def branch(base, d):
        hd = math.degrees(math.atan2(d[1], d[0]))
        e = (base[0] - d[0] * S, base[1] - d[1] * S)
        turn = 1 if d[0] < 0 else -1                 # right ovary: bend clockwise; left ovary: counter-clockwise
        c2 = (e[0] - turn * R2 * math.sin(math.radians(hd)), e[1] + turn * R2 * math.cos(math.radians(hd)))
        xv = c2[0] + turn * R2                       # the straight drop
        y0 = yc(xv)
        assert c2[1] > y0 + TW / 2 + RF + 8, "no room for the branch's straight drop"
        return xv, resample(line_pts((xv, y0), (xv, c2[1])) + arc_pts(c2, R2, 90, hd, turn)[1:] + line_pts(e, base)[1:], 2.0)
    xR, rc = branch(baseR, dR)
    xL, lc = branch(baseL, dL)
    assert abs((xR - UX) - (UX - xL)) < 0.05, "the two branches are not mirrored about the uterus"
    # The head points along the branch's LAST direction; its tip is where that line meets the ovary
    # outline, plus 1.2 units, so it always touches the ovary whatever the curve does.
    tips = []
    for c, oc, side in ((rc, ocR, 1), (lc, ocL, -1)):
        t_ = tangents(c)[-1]
        hit = ray_ellipse(c[-1], t_, oc, OV_RX * US, OV_RY * US, side * OV_ROT)
        assert hit is not None and abs(hit + 1.2 - HL) < 3, "arrowhead does not reach the ovary"
        tips.append((c[-1][0] + t_[0] * (hit + 1.2), c[-1][1] + t_[1] * (hit + 1.2)))
    tipR, tipL = tips
    tw_ = [TW] * len(tc)
    bw_ = {id(rc): [BW] * len(rc), id(lc): [BW] * len(lc)}

    # ---------------------------------------------------------- pancreas
    o.append(f'<g transform="translate({PX},{PY}) scale({PS})">{duodenum()}{pancreas()}</g>')

    # ---------------------------------------------------------- vessel: outline, wall, inside
    # Three layers, so the branches join the trunk without a seam: every outline first (a 2.4-unit
    # stroke around each one-piece shape), then every wall, then every inside.  The fillets have their
    # own wall and inside pieces, concentric with each other.
    shapes = [ribbon(tc, tw_), arrow_tube(rc, bw_[id(rc)], tipR, HW, BACK), arrow_tube(lc, bw_[id(lc)], tipL, HW, BACK)]
    lumens = [ribbon(tc, [w - 2 * WALL for w in tw_])]
    for xv, c in ((xR, rc), (xL, lc)):
        yb = yc(xv) + TW / 2
        for side in (1, -1):
            shapes.append(fillet(xv, yb, BW / 2, RF, side))
            lumens.append(fillet(xv, yb - WALL, BW / 2 - WALL, RF + WALL, side))
        lumens.append(arrow_lumen(c, [w - 2 * WALL for w in bw_[id(c)]], HL * .42))
    for s in shapes:
        o.append(f'<path d="{s}" fill="{V_OUT}" stroke="{V_OUT}" stroke-width="2.4" stroke-linejoin="round"/>')
    for s in shapes:
        o.append(f'<path d="{s}" fill="{V_WALL}"/>')
    for s in lumens:
        o.append(f'<path d="{s}" fill="{V_LUM}" stroke="{V_LUM}" stroke-width=".6" stroke-linejoin="round"/>')
    tl = [w - 2 * WALL for w in tw_]
    o.append(f'<path d="{ribbon(tc, [x * .35 for x in tl])}" fill="#FFFFFF" opacity=".35"/>')
    # cut ends at both sides, so the bloodstream reads as a tube that carries on past the picture
    for xe in (TX0, TX1):
        o.append(f'<ellipse cx="{xe}" cy="{TY}" rx="5.4" ry="{TW / 2 + 1.2}" fill="{V_WALL}" stroke="{V_OUT}" stroke-width="1.3"/>'
                 f'<ellipse cx="{xe}" cy="{TY}" rx="3.2" ry="{TW / 2 - WALL}" fill="#E7A39B"/>')

    # ---------------------------------------------------------- insulin rising from the pancreas into the blood
    # Dots sit fully clear of the dashed lines; each arrow tip lands on the bloodstream's outline.
    # The marker head reaches (10 - refX) / 10 * markerWidth * stroke = 3.5/10 * 4.4 * 1.8 = 2.77 units
    # past the end of its path.
    for k0, (x0, y0) in enumerate(((160, 120), (204, 108))):
        yb = yc(x0) + TW / 2
        o.append(f'<path d="M{x0},{y0} V{yb + 0.6 + 2.77:.2f}" stroke="{INS_EDGE}" stroke-width="1.8" stroke-dasharray="3 3" '
                 'marker-end="url(#pcAy)" fill="none"/>')
        for k, yy in enumerate((y0 - 8, y0 - 26, y0 - 44)):
            if yy > yb + 13:                   # keep the top dot clear of the arrowhead
                o.append(insulin(x0 + (7 if (k + k0) % 2 else -7), yy, 3.4))

    # what the blood carries: glucose, insulin, red blood cells.  Sugar and insulin are drawn at half
    # the size of the red cells (still far larger than life: the close-up says "not to scale").
    lab_w = tw("Bloodstream", 10.5, 800) + 14
    lab_x0 = 34

    tg = tangents(tc)
    # The small circle on the bloodstream holds exactly what the zoom circle shows, in the same kinds: a red
    # cell in the middle, a sugar and an insulin on each side (placed, not random, so it can never come out
    # empty or sugar-only).  The random symbols keep out of it.
    yi = yc(BX)
    ind = [(BX - 12.5, yi - 3.4, 3.2, "g"), (BX - 12.5, yi + 5.0, 3.2, "i"), (BX, yi + 0.4, 7.6, "r"),
           (BX + 12.5, yi - 3.4, 3.2, "i"), (BX + 12.5, yi + 5.0, 3.2, "g")]
    for px, py, r, kind in ind:
        reach = 4.6 if kind == "r" else r
        assert math.dist((px, py), (BX, yi)) + (7.6 if kind == "r" else r) < R_IND - 1, "indicator symbol leaves its circle"
        assert abs(py - yi) + reach < (TW - 2 * WALL) / 2 - 1.0, "indicator symbol leaves the bloodstream"
    placed = [(px, py, r, kind) for px, py, r, kind in ind]
    kinds = ["g"] * 16 + ["i"] * 12 + ["r"] * 9
    rng.shuffle(kinds)
    idx = list(range(12, len(tc) - 12))
    for kind in kinds:
        r = 7.6 if kind == "r" else 3.2
        for _ in range(600):
            i = rng.choice(idx)
            (x, y), (tx, ty) = tc[i], tg[i]
            lim = (tl[i] / 2) - (3.6 if kind == "r" else r) - 1.2
            u = rng.uniform(-lim, lim)
            px, py = x - ty * u, y + tx * u
            if lab_x0 - 4 < px < lab_x0 + lab_w + 4:       # keep the "Bloodstream" label clear
                continue
            if any(abs(px - xv) < BW / 2 + RF + 3 for xv in (xR, xL)):   # keep the branch openings clear
                continue
            if abs(px - BX) < R_IND + r + 1.5:                         # keep the indicator circle to its five
                continue
            if any(math.dist((px, py), (qx, qy)) < r + qr + 2.4 for qx, qy, qr, _ in placed):
                continue
            placed.append((px, py, r, kind))
            break
    assert len(placed) == len(kinds) + len(ind), f"bloodstream: placed {len(placed) - len(ind)} of {len(kinds)} symbols"
    for k, (px, py, r, kind) in enumerate(placed):
        rot = -6 if k < len(ind) else rng.uniform(-12, 12)
        o.append(glucose(px, py, 3.0) if kind == "g" else insulin(px, py, 2.9) if kind == "i" else
                 red_cell(px, py, rot, 0.6))
    # insulin riding both branches all the way to the ovaries (the same three spots on each)
    for xv, c in ((xR, rc), (xL, lc)):
        run = [p for p in c if p[1] > yc(xv) + TW / 2 + RF + 3]
        n = len(run)
        for f in (0.12, 0.45, 0.78):
            x, y = run[int(n * f)]
            o.append(insulin(x, y, 2.9))
    o.append(label_bg(lab_x0, TY - 9, lab_w, 18, "#FFFFFF", 0.94, 5)
             + T(lab_x0 + lab_w / 2, TY + 3.8, "Bloodstream", 10.5, 800, "#8E1F28", "middle"))

    # ---------------------------------------------------------- zoom circle: the crowded blood
    r_ind = R_IND
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
    # Captions are upright: the shipped fonts have no italic face, and a faked slant is not print quality.
    # They read as captions by their lighter weight and muted colour next to the bold part names.
    o.append(T(BX, BY + BR + 15, "close-up of the blood (not to scale)", 10, 500, "#5E6A72", "middle"))

    # ---------------------------------------------------------- uterus, tubes, ovaries, androgens
    o.append(reproductive(UX, UY, US))
    for side in (-1, 1):
        for lx, ly, r in [(126, 60, 5.4), (136, 72, 5.0), (146, 84, 4.6)]:
            o.append(androgen(UX + side * lx * US, UY + ly * US, r))
        o.append(T(UX + side * 146 * US, UY + 104 * US, "extra androgens", 10, 600, AND_EDGE, "middle"))

    # ---------------------------------------------------------- labels and step markers
    o.append(T(214, 162, "Pancreas", 11.5, 800, "#7A4318", "middle"))
    # under the C-loop of the duodenum, well away from the zoom caption (no leader needed)
    o.append(T(PX + 80 * PS, H_ART - 8, "small intestine", 10, 500, "#8A5A50", "middle"))
    for side in (-1, 1):
        o.append(T(UX + side * 92 * US, UY + 80 * US, "Ovary", 11, 800, "#8A2F3A", "middle"))
    o.append(T(UX, UY + 134 * US + 15, "Uterus", 11, 800, "#8A2F3A", "middle"))
    o.append(marker(120, 78, 1, c1) + marker(BX, 72, 2, c1) + marker(UX, 60, 3, c1))
    return svg(W_ART, H_ART, "".join(o),
               "The pancreas makes insulin. The bloodstream carries sugar and insulin from the pancreas all over the body; "
               "a branch to each ovary ends in an arrow touching it. A zoom circle shows extra sugar and extra insulin "
               "in the blood. The ovaries hold many small follicles and release extra androgens.")


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
    fr = "".join(f'<path d="{frond((1.0, y), (math.cos(math.radians(ang)), math.sin(math.radians(ang))), ln, 1.05, curl, 0, .45, 8)}" '
                 f'fill="{U_BASE}" stroke="{U_EDGE}" stroke-width=".45"/>'
                 for y, ang, ln, curl in ((-2.4, -16, 3.2, -.2), (-.9, 6, 4.2, .2), (.7, 26, 3.8, .4), (2.2, 46, 3.0, .4)))
    return (f'<path d="M-10.5,5 C-7,-3 -1,-5 4.2,-1.8" fill="none" stroke="{U_EDGE}" stroke-width="4.2" stroke-linecap="round"/>'
            f'<path d="M-10.5,5 C-7,-3 -1,-5 4.2,-1.8" fill="none" stroke="{U_BASE}" stroke-width="2.5" stroke-linecap="round"/>'
            f'<g transform="translate(4.2,-1.8) rotate(32)">{fr}'
            f'<path d="M-1.2,-1.9 C.2,-2 1,-2.6 1.6,-3.3 Q2,0 1.6,3.3 C1,2.6 .2,2 -1.2,1.9Z" fill="{U_BASE}" stroke="{U_EDGE}" '
            'stroke-width=".6" stroke-linejoin="round"/></g>')


def key():
    ves_mini = (f'<rect x="-8.5" y="-5.5" width="17" height="11" rx="2" fill="{V_WALL}" stroke="{V_OUT}" stroke-width="1"/>'
                f'<rect x="-8.5" y="-2.8" width="17" height="5.6" fill="{V_LUM}"/>')
    # Column-major, 2 rows: what is in the blood; the red cell with the pancreas; the bloodstream with the
    # androgens; the ovary parts.  Paired so the four columns fit the page width with "Bloodstream:
    # carries insulin all over" in (the widths are measured with the real font: 640 of 657 px).
    # Both entries in a column get the same swatch width, so their words start on one line.
    W2, VB2 = 24, "-12 -8 24 16"
    items = [
        (sw(glucose(0, 0, 6.2)), "Glucose", "sugar in the blood"),
        (sw(insulin(0, 0, 6)), "Insulin", "lets sugar into cells"),
        (sw(red_cell(0, 0, 0, .64), W2, 16, VB2), "Red blood cell", ""),
        (sw(pan_mini(), W2, 16, VB2), "Pancreas", "makes insulin"),
        (sw(ves_mini, W2, 16, VB2), "Bloodstream", "carries insulin all over"),
        (sw(androgen(0, 0, 6.4), W2, 16, VB2), "Androgens", "male-type hormones"),
        (sw(follicle(0, 0, 5.6), W2, 16, VB2), "Follicle", "egg sac, the &ldquo;cyst&rdquo;"),
        (sw(tube_mini(), W2, 16, VB2), "Fallopian tube", "carries eggs"),
    ]
    cells = "".join(f'<span>{m}<b>{a}</b>{(" " + b) if b else ""}</span>' for m, a, b in items)
    return f'<div class="pc-key"><em>KEY</em>{cells}</div>'


def steps():
    # [STEPTO13] insulin resistance = cells respond poorly; the extra insulin keeps blood sugar near
    # normal for years, which is why the risk of diabetes comes later (facts box).
    st = [("The pancreas makes insulin.", "Insulin moves sugar out of the blood and into your cells for fuel."),
          ("Cells answer insulin poorly.", "So the pancreas pumps out more to keep sugar in check."),
          ("Extra insulin reaches the ovaries.", "The ovaries make extra androgens, and eggs get stuck in "
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
# Thinning scalp hair, front view: long hair frames the face; the hair is parted in the middle and the part
# has widened into a pale wedge of scalp (lighter than the hair) that is widest at the crown.  Three fine
# strands lie flat across the bare wedge, following the curve of the head.
SCALP_THIN = (
    # bare scalp: the widened part, a pale wedge from the front hairline to the crown
    '<path d="M32 19.4 23.6 11.2C26 9.5 28.8 8.6 32 8.6s6 .9 8.4 2.6z" fill="currentColor" stroke="none" opacity=".15"/>'
    # hair, combed away from the part on each side, down past the shoulders
    '<path d="M32 19.4 23.6 11.2c-4.6 3.2-7.4 9-7.8 16.4-.4 8.8.6 16.4-3.6 24.8 3.6 1.4 7.4 1.2 10.6-.8'
    '-2.4-5.6-3.4-11.4-3.2-17.4.2-6 2.8-10.8 8.2-13.6 2.8-1.4 5.4-2 8.2-2.2z" fill="currentColor" stroke="none" opacity=".66"/>'
    '<path d="M32 19.4 40.4 11.2c4.6 3.2 7.4 9 7.8 16.4.4 8.8-.6 16.4 3.6 24.8-3.6 1.4-7.4 1.2-10.6-.8'
    ' 2.4-5.6 3.4-11.4 3.2-17.4-.2-6-2.8-10.8-8.2-13.6-2.8-1.4-5.4-2-8.2-2.2z" fill="currentColor" stroke="none" opacity=".66"/>'
    # head and face outline, neck and shoulders
    '<path d="M32 8.6c-9.4 0-15.4 8-15.4 18.6 0 11.6 6.6 20.6 15.4 20.6s15.4-9 15.4-20.6C47.4 16.6 41.4 8.6 32 8.6z"/>'
    '<path d="M27.6 46.6v4.2c-6.6 1.2-12.4 3.8-15.2 8.6M36.4 46.6v4.2c6.6 1.2 12.4 3.8 15.2 8.6"/>'
    # a few fine strands lying flat across the bare part, curved with the head
    # (uneven: one crosses the whole part, one starts from the right and stops short, one short from the left)
    '<path d="M25.2 13.4c2.6-1.6 5.6-2 8.6-1.3 1.8.4 3.4 1.1 4.8 2M40.2 12.9c-3.2-.3-6.4.6-9.3 2.5M28.4 17.2c1.5-.9 3-1.2 4.4-1"'
    ' stroke-width="1.15"/>'
    # eyes and mouth
    '<path d="M26.2 30h2.6M35.2 30h2.6M29.6 39c1.6 1 3.2 1 4.8 0" stroke-width="2.2"/>')
# Dark skin patches (acanthosis nigricans): the same profile language as FACE_HAIR (bun, hairline), no
# facial hair, an ear, and an irregular dark velvety patch on the side and back of the neck below the
# ear, with two skin creases and a speckled edge.  It stops short of the throat, so it cannot read as
# a collar or a scarf.
DARK_PATCH = ('<path d="M33.2 41.6c2.6-1.4 5.6-1.6 8.8-1.2v12.8c-2.2 1.2-4.8.6-6.8 1.6-2 1-4.2.4-5-1.6-1-2.4 1-3.6.4-5.8'
              '-.6-2.4.4-4.6 2.6-5.8z" fill="currentColor" stroke="none" opacity=".82"/>'
              '<path d="M33.6 46.2c2-.8 4.6-1 7-.6M32.6 50.2c2.4-.8 5.4-1 8-.6" stroke="#F4EAE6" stroke-width="1.1"/>'
              '<g fill="currentColor" stroke="none" opacity=".75"><circle cx="30.6" cy="44.2" r=".9"/>'
              '<circle cx="29.2" cy="48.4" r=".8"/><circle cx="31.4" cy="55.6" r=".8"/><circle cx="36.6" cy="56.2" r=".9"/>'
              '<circle cx="31.6" cy="40.8" r=".7"/></g>'
              '<path d="M42 57v-9c5-3 8-8 8-15 0-11-8-19-18-19-8.5 0-14.5 5.5-16 13l-3.5 8.5 4 1.2v4.3c0 3 2.2 5 5 5h3.5v11"/>'
              '<path d="M24.5 15.5c5-3 13-3.5 19 1.5"/><circle cx="48" cy="15.5" r="5.5"/>'
              '<path d="M36.6 27.6c2.6-1.4 5.4.4 5.2 3.4-.2 2.6-2.4 3.6-4.4 3.4" stroke-width="2.4"/>')
# Acne: a face from the front with raised spots on the cheeks, chin and forehead (the two biggest
# carry a faint red-ring halo).
ACNE = ('<path d="M32 9c-10.4 0-17 8.6-17 20.4C15 42 22.6 55 32 55s17-13 17-25.6C49 17.6 42.4 9 32 9z"/>'
        '<path d="M15.4 25c3.2-7.6 9.4-11.6 16.6-11.6S45.4 17.4 48.6 25" stroke-width="2.2"/>'
        '<path d="M24.4 30.6h3.4M36.2 30.6h3.4M28.8 44.2c2 1.2 4.4 1.2 6.4 0" stroke-width="2.4"/>'
        '<g fill="currentColor" stroke="none"><circle cx="22.4" cy="38.6" r="2.4"/><circle cx="41.8" cy="37.6" r="2.7"/>'
        '<circle cx="45" cy="43.4" r="1.9"/><circle cx="37.4" cy="50" r="2"/><circle cx="35.6" cy="21.4" r="1.9"/></g>'
        '<g fill="none" stroke-width="1.2" opacity=".55"><circle cx="22.4" cy="38.6" r="4.4"/><circle cx="41.8" cy="37.6" r="4.8"/></g>')
# Weight gain at the waist: a torso whose sides bulge outward at the middle, with a tape measure
# around the widest part.
WAIST = ('<path d="M22.6 6.6c-1.2 7-4.4 11.4-7.4 16.4-3 5-4.2 9.6-3.2 15 1 5.6 4.6 10.6 5.6 19.4"/>'
         '<path d="M41.4 6.6c1.2 7 4.4 11.4 7.4 16.4 3 5 4.2 9.6 3.2 15-1 5.6-4.6 10.6-5.6 19.4"/>'
         '<path d="M11.2 29.6c13.6 3.4 28 3.4 41.6 0v7.6c-13.6 3.4-28 3.4-41.6 0z" fill="currentColor" stroke="none" opacity=".3"/>'
         '<path d="M11.2 29.6c13.6 3.4 28 3.4 41.6 0M11.2 37.2c13.6 3.4 28 3.4 41.6 0"/>'
         '<path d="M18 31.6v3M24.6 32.8v3M32 33.2v3M39.4 32.8v3M46 31.6v3" stroke-width="2"/>'
         '<path d="M52.8 33.4h4.4v8.6h-4.4" stroke-width="2.6"/>'
         '<circle cx="32" cy="45.4" r="1.4" fill="currentColor" stroke="none"/>')
# Trouble getting pregnant: a home pregnancy test, tilted: a wide handle with a wide result window that shows
# only one line (the control line: not pregnant yet), and a narrower capped tip with the absorbent end.
PREG_TEST = (
    '<g transform="rotate(-38 32 32)">'
    '<rect x="24.6" y="3" width="14.8" height="41.4" rx="7.4"/>'
    '<path d="M27.6 44.4V56a4.4 4.4 0 0 0 8.8 0V44.4"/>'
    '<path d="M28.8 47.4h6.4V56a3.2 3.2 0 0 1-6.4 0z" fill="currentColor" stroke="none" opacity=".45"/>'
    '<rect x="27" y="13.6" width="10" height="17.2" rx="3.6" stroke-width="2.3"/>'
    '<path d="M29 19.4h6" stroke-width="2.8"/>'
    '</g>')
# Skin tags: a close-up of a gently curved edge of skin, shaded below its surface and fading out (no tray,
# no bottom edge), with a few pores; three small soft growths on narrow stalks rise from the surface.
SKIN_TAG = (
    '<defs><radialGradient id="pcSkinFade" cx="32" cy="36" r="25" gradientUnits="userSpaceOnUse" '
    'gradientTransform="matrix(1.34 0 0 1 -10.88 0)">'
    '<stop offset="0" stop-color="currentColor" stop-opacity=".38"/><stop offset=".55" stop-color="currentColor" stop-opacity=".2"/>'
    '<stop offset="1" stop-color="currentColor" stop-opacity="0"/></radialGradient></defs>'
    '<g transform="translate(0 3)">'
    '<path d="M3 42.6C12.6 37.4 22.2 35 32 35s19.4 2.4 29 7.6V61H3z" fill="url(#pcSkinFade)" stroke="none"/>'
    '<path d="M3 42.6C12.6 37.4 22.2 35 32 35s19.4 2.4 29 7.6"/>'
    # each tag: a narrow stalk from the surface widening into a soft rounded bulb, square to the curve, drawn
    # 1.22 times larger about its base (stroke 1.9 x 1.22 = the ring's usual 2.3)
    '<g fill="currentColor" fill-opacity=".55" stroke-width="1.9">'
    '<path transform="translate(17.85 38.7) scale(1.22) translate(-17.85 -38.7)" '
    'd="M16.4 38.9c-.5-1.6-1.6-2.7-2.9-4.1-2.2-2.4-1.5-6.2 1.6-7.1 3.2-1 5.8 1.3 5.8 4.2 0 2.2-1.1 3.9-1.5 5.6l-.1 1z"/>'
    '<path transform="translate(32.25 35.1) scale(1.22) translate(-32.25 -35.1)" '
    'd="M30.5 35.1c-.1-2-1.3-3.4-2.6-5.2-2-2.9-.6-7.2 3.4-7.6 4-.4 6.2 2.7 5.3 6.1-.6 2.3-2 3.8-2.5 5.6l-.1 1.1z"/>'
    '<path transform="translate(47 38) scale(1.22) translate(-47 -38)" '
    'd="M45.7 37.4c.2-1.4 0-2.6-.6-4-1-2.3.6-4.8 3.1-4.8 2.7 0 4 2.7 2.9 4.9-.7 1.5-1.9 2.6-2.6 4.2l-.2.9z"/></g>'
    '<g fill="currentColor" stroke="none" opacity=".5"><circle cx="11" cy="49" r="1"/><circle cx="22.4" cy="46" r="1"/>'
    '<circle cx="38.6" cy="45.6" r="1"/><circle cx="51.6" cy="48.6" r="1"/><circle cx="30" cy="52" r="1"/>'
    '<circle cx="18" cy="55" r=".9"/><circle cx="44" cy="54.6" r=".9"/></g></g>')


def ring():
    # Signs a reader can notice herself.  [OWH] Office on Women's Health PCOS fact sheet and NIH NICHD
    # "What are the symptoms of PCOS?": irregular periods, hirsutism, acne, thinning scalp hair, weight
    # gain, darkened skin along neck creases and body folds (acanthosis nigricans, a sign of insulin
    # resistance), skin tags, infertility.  [GUIDE23] adds anxiety and depression (2.2.1-2.2.2), and
    # [GUIDE23H] 1.10.2 lists "daytime sleepiness or fatigue" among the sleep-apnea symptoms every woman
    # with PCOS should be asked about (the source for "Fatigue").  "Blood sugar swings" is gone: it is in
    # none of these lists.
    items = [(icon("calendar", "0.34in", sw=3), "Irregular or<br>missed periods"),
             (ic(ACNE, "0.36in"), "Acne"),
             (ic(FACE_HAIR, "0.36in"), "Extra facial or<br>body hair"),
             (ic(SCALP_THIN, "0.36in"), "Thinning<br>scalp hair"),
             (ic(WAIST, "0.36in"), "Weight gain<br>at the waist"),
             (icon("battery", "0.34in", sw=3), "Fatigue"),
             (icon("brain", "0.34in", sw=3), "Mood changes,<br>anxiety"),
             (ic(PREG_TEST, "0.36in"), "Trouble getting<br>pregnant"),
             (ic(DARK_PATCH, "0.36in"), "Dark skin patches<br>(neck, armpits)"),
             (ic(SKIN_TAG, "0.36in"), "Skin tags")]
    cells = "".join(f'<div class="pc-rg"><div class="pc-c">{s}</div><span>{lab}</span></div>' for s, lab in items)
    return f'<div class="pc-head">SIGNS AND SYMPTOMS</div><div class="pc-ring">{cells}</div>'


def facts(ed):
    # Glucose tests ([GUIDE23H] 1.9.9-1.9.10: an OGTT, or fasting glucose / A1c) are ordered by a doctor;
    # most pharmacists cannot order them, so the pharmacy edition points the reader to her doctor.  The
    # same goes for months-long gaps between periods (an exam, maybe an ultrasound).
    test_who = "your doctor" if (ed or {}).get("who") == "your pharmacist" else "{who}"
    return ('<div class="pc-facts">'
            '<div class="pc-fbox"><h4>PCOS facts</h4><p>'
            # [GUIDE23H] "PCOS prevalence is between 10 to 13%" (Rotterdam 11.9% in [MARCH10]) -> "about 1 in 8"
            # (12.5%, inside the range; "up to 1 in 8" would understate the 13% top);
            # [WHO23] up to 70% undiagnosed ([MARCH10]: 68-69% had no prior diagnosis) -> "up to 7 in 10".
            'About <b>1 in 8</b> women of childbearing age has PCOS, and up to <b>7 in 10</b> of them have never been '
            'diagnosed. '
            # [STEPTO13] insulin resistance in 75% of LEAN women with PCOS; [GUIDE23] PCOS occurs across all BMIs.
            'It happens at every body size, even at a healthy weight. '
            # [GUIDE23] adults: 2 of 3 = irregular cycles; clinical or biochemical high androgens; polycystic ovaries
            # on ultrasound OR a high AMH blood test; other causes excluded.  [PENA25] teens: irregular cycles AND
            # high androgens (no ultrasound, no AMH), so the 2-of-3 line says "Adults".  AMH (anti-Mullerian
            # hormone) is made by the small follicles, so it runs high when there are many of them.
            'Adults are diagnosed with <b>2 of 3</b>: irregular periods, high androgens (a blood test or signs like extra '
            'hair) or many follicles on ultrasound (or a blood test showing high AMH, a follicle hormone), once other '
            'causes are ruled out. You can have PCOS without &ldquo;cysts.&rdquo; '
            # [PMOS26]: renamed in May 2026 (56 organizations); "numerous arrested antral follicles, not pathologic
            # cysts"; "Diagnostic criteria remain unchanged".  The European Society of Gynaecology asks for long dual
            # naming with patient communication first, so PCOS stays the headline and PMOS is named once, here and in
            # the subtitle.
            'In&nbsp;2026 experts renamed it polyendocrine metabolic ovarian syndrome (<b>PMOS</b>), because the '
            '&ldquo;cysts&rdquo; are really stalled egg follicles. Same condition, same&nbsp;tests.</p></div>'
            '<div class="pc-fbox"><h4>Risk factors</h4><ul>'
            # [GUIDE23] strong family clustering; first-degree relatives with PCOS or type 2 diabetes.
            '<li><b>Runs in families:</b> a mother or sister with PCOS or type 2 diabetes raises your risk.</li>'
            # [GUIDE23H] 1.9.8: women with type 1 and type 2 diabetes have an increased risk of PCOS.  One line, so
            # this box and the facts box end level (7 lines each).
            '<li><b>Diabetes:</b> type 1 or 2 raises the risk.</li>'
            # [GUIDE23] weight gain worsens insulin resistance and androgen excess (hence the guideline's focus on
            # preventing weight gain, 3.1.2); lifestyle (diet, activity, sleep, stress) worsens or eases PCOS
            # features but is not shown to cause it.  Hormone-disrupting chemicals (BPA in some plastics,
            # phthalates in fragrances): higher levels go with higher androgens in women with PCOS in observational
            # studies only, hence "can make it worse".
            '<li><b>Can make it worse (you can change):</b> weight gain at the waist, a high-sugar diet, '
            'sitting most of the day, poor sleep, stress and hormone-disrupting chemicals (in some plastics and '
            'fragrances).</li></ul></div></div>'
            # Full width under both boxes, so the two columns stay level.
            # [GUIDE23] broader features: metabolic risk (type 2 diabetes), cardiovascular disease, sleep apnoea, mood.
            # [GUIDE23H] 1.11.1-1.11.3: markedly higher risk of endometrial hyperplasia and cancer (overall chance
            # low, no routine screening); long-standing untreated amenorrhea and a persistently thickened endometrium
            # add to the risk; 1.11.4: cycle regulation is part of prevention -> one calm line with an action.
            '<p class="pc-why"><b>Why it matters:</b> PCOS raises the risk of type 2 diabetes, heart disease and sleep '
            f'apnea (breathing pauses in sleep), so ask {test_who} about a blood sugar test. Long gaps between periods '
            f'can thicken the womb lining, so tell {test_who} if yours are often months&nbsp;apart.</p>')


def front(t, ed):
    return (f'<div class="pcf"><div class="pc-art">{art_pcos(t)}</div>{steps()}{key()}{ring()}{facts(ed)}</div>')


CSS = r"""
.pcf .pc-art svg{display:block;width:100%;height:auto}
.pcf .pc-steps{display:grid;grid-template-columns:1fr 1fr 1fr;gap:0.12in;margin:0.04in 0 0}
.pcf .pc-steps>div{display:flex;gap:6px;align-items:flex-start}
.pcf .pc-n{flex:none;width:0.2in;height:0.2in;border-radius:50%;background:var(--c1);color:#fff;font:800 8pt Inter,sans-serif;
  display:flex;align-items:center;justify-content:center;margin-top:1px}
.pcf .pc-steps p{margin:0;font-size:8.2pt;line-height:1.3;color:#2B3236}
.pcf .pc-steps b{color:var(--deep)}
.pcf .pc-key{display:grid;grid-template-rows:auto auto;grid-auto-flow:column;justify-content:space-between;align-items:center;
  gap:3px 8px;margin-top:0.07in;padding:5px 10px 5px 12px;border:1px solid #D9DEE2;border-radius:8px;background:#FFFFFF;font-size:7.4pt;
  line-height:1.2;color:#3A4247}
.pcf .pc-key em{grid-row:span 2;font:800 7.4pt Inter,sans-serif;letter-spacing:.14em;color:#2B3236;font-style:normal}
.pcf .pc-key span{display:inline-flex;align-items:center;gap:4px;white-space:nowrap}
.pcf .pc-key svg{flex:none;display:block}
.pcf .pc-key b{color:#1F2A2E;font-weight:800}
.pcf .pc-head{font:900 12pt Merriweather,Georgia,serif;color:var(--c1);text-align:center;margin:0.08in 0 0.05in;letter-spacing:.02em}
.pcf .pc-ring{display:grid;grid-template-columns:repeat(5,1fr);gap:0.06in 0.06in}
.pcf .pc-rg{display:flex;flex-direction:column;align-items:center;text-align:center}
.pcf .pc-c{width:0.53in;height:0.53in;border-radius:50%;background:#F1E7E2;display:flex;align-items:center;justify-content:center;
  color:#8A5A52;box-shadow:0 0 0 2px #fff,0 0 0 3px #E8D8D1}
.pcf .pc-rg span{font-size:7.8pt;line-height:1.2;margin-top:3px;color:#3A4247}
.pcf .pc-facts{display:grid;grid-template-columns:1.62fr 1fr;gap:0.14in;margin-top:0.08in}
.pcf .pc-fbox h4{margin:0 0 4px;background:var(--c1);color:#fff;font:800 8.2pt Inter,sans-serif;letter-spacing:.08em;
  text-transform:uppercase;padding:3px 10px;border-radius:3px}
.pcf .pc-fbox p,.pcf .pc-fbox li{font-size:8.2pt;line-height:1.33;margin:0;color:#2B3236}
.pcf .pc-fbox ul{margin:0;padding-left:13px}
.pcf .pc-fbox li{margin-bottom:1px}
.pcf .pc-fbox b{color:var(--deep)}
/* "Why it matters" spans both fact boxes, on a pale band with the theme rule on its left */
.pcf p.pc-why{font-size:8.2pt;line-height:1.33;margin:6px 0 0;color:#2B3236;background:var(--tint);
  border-left:3px solid var(--c1);border-radius:0 4px 4px 0;padding:3px 9px 4px}
.pcf p.pc-why b{color:var(--deep)}
/* Back page, this sheet only.  Nothing is taken at bedtime, so the empty Bedtime box of "Your daily rhythm"
   is hidden (the kit draws Morning, Evening meal, Bedtime in that order) and the two meal boxes share the
   panel; the check panel holds four notes, so it takes half the row. */
.sheet.back:has(.pc-back) .duo{grid-template-columns:1fr 1fr}
.sheet.back:has(.pc-back) .rhythm{grid-template-columns:1fr 1fr}
.sheet.back:has(.pc-back) .rhythm .slot:nth-child(3){display:none}
/* Two name lines in every column (two names wrap), so the bullets, serving lines and dose bars start at the
   same height across the row: the photo link is as tall as the photo, its 0.04 in gap and two 8.6 pt name
   lines, and the name sits at its bottom, next to the size line.  (The name itself stays a block: making it
   a flex box would split names that carry no-break spans.) */
.sheet.back:has(.pc-back) .col a.plink{min-height:calc(1.02in + 19.78pt)}
.sheet.back:has(.pc-back) .col .pick .nm{margin-top:auto}
/* Myo-Inositol Complex's serving line (five ingredients) is the longest and sets the row's height, so the
   START HERE column is a little wider (the kit's inline style is repeat(5,1fr)).  1.04 is the widest it
   can go before "Blood sugar and insulin" wraps in the narrower columns (measured). */
.sheet.back:has(.pc-back) .cols{grid-template-columns:1.04fr 1fr 1fr 1fr 1fr!important}
/* The four-note check panel sets the duo's height; the room comes from a little less red above and below
   the lifestyle cards (shared 0.3 in / 0.18 in, as on the insulin-resistance sheet), a smaller gap over
   "Nutrient Solutions", and slightly tighter leading in the check panel. */
.sheet.back:has(.pc-back) .band{padding-top:0.22in!important;padding-bottom:0.13in}
.sheet.back:has(.pc-back) .band h2{margin-bottom:0.07in}
.sheet.back:has(.pc-back) .life .disc2{width:0.8in;height:0.8in}
.sheet.back:has(.pc-back) .ns-title{margin-top:0.11in}
.sheet.back:has(.pc-back) .cols{margin-top:0.07in}
.sheet.back:has(.pc-back) .duo{margin-top:0.08in}
.sheet.back:has(.pc-back) .rx li{line-height:1.24;margin-bottom:1px}
.sheet.back:has(.pc-back) .notes{margin-top:0.08in;padding-bottom:0.07in}
.sheet.back:has(.pc-back) .recby{margin-top:0.07in}
"""

SHEET = {
    "slug": "pcos", "code": "ND-CM-204", "theme": "metab", "series": "Metabolic Health Series",
    "order": 6,
    # [PMOS26]: PCOS stays the headline during the dual-naming years; the new name is added once.
    "title": "Polycystic Ovary Syndrome", "sub": "PCOS, now also called PMOS",
    # [STEPTO13] insulin resistance in 75% of lean and 95% of overweight women with PCOS -> "most women".
    "intro": ("PCOS is a common hormone condition. The ovaries make extra <b>androgens</b>. These are male-type hormones "
              "like testosterone; women normally make a little. Too much can upset periods, ovulation (releasing an egg) "
              "and fertility, and it shows up in skin, hair, weight and mood. Genes play a part, but in most women with PCOS "
              "<b>insulin resistance</b> (cells answer insulin poorly) helps drive it. That is why food, movement, sleep and "
              "stress change how PCOS behaves."),
    "front": front,
    "css": CSS,
    "back": {
        # the span marks this sheet's back page for the scoped CSS (.sheet.back:has(.pc-back))
        "life_title": 'Lifestyle Recommendations<span class="pc-back"></span>',
        "style": "circle",
        "life": [
            # PCOS handout "Always avoid": sugar-sweetened drinks; carbohydrates eaten on their own, without
            # protein or fat; "Protein ... start here at every meal" (low-glycemic eating, Sun X 2026, 25 RCTs).
            ("plate", "Protein first", "Start every meal with protein. Never eat carbs on their own, and skip sugary drinks."),
            # PCOS handout food table: fermented foods 1 to 2 servings a day (plain kefir, live-culture yogurt,
            # sauerkraut ...); non-starchy vegetables 4 to 6 servings ("the fiber your gut bacteria feed on").
            ("jar", "Feed your gut", "Plain kefir, yogurt or sauerkraut daily, plus 4 to 6 servings of vegetables."),
            # [GUIDE23H] 3.4.2-3.4.5: activity per population guidelines, "at least 30 minutes daily on most
            # days"; muscle strengthening on 2 days a week (US Physical Activity Guidelines, 2nd ed., 2018).
            ("dumbbell", "Move and lift", "At least 30 minutes on most days, plus strength work 2 days a week."),
            # 7 to 9 hours: National Sleep Foundation adult range.  [GUIDE23H] 1.10.2: ask about snoring with
            # waking unrefreshed, daytime sleepiness or fatigue (sleep apnea, named on the front).
            ("moon", "Sleep 7 to 9 hours", "Snoring or always tired? Ask about sleep apnea."),
            # [GRANT10]: spearmint tea twice a day for 30 days, 42 women with PCOS: free and total testosterone
            # fell (the hair score itself did not change in that time, hence "small study" and no promise).
            # In the NutriDyn GLC 2026 PMOS protocol ("Spearmint: tea or extract twice daily").
            ("leaf", "Spearmint tea", "Two cups a day. In a small 30-day study, testosterone came down."),
        ],
        # Five products (the competitor sheet's count), all from NutriDyn PCOS protocols: the NutriDyn GLC 2023
        # PCOS protocol: Myo-Inositol Complex 3 BID, Berberine Pro TID, Vit D3
        # 5000 IU, fish oils 2 BID), the NutriDyn GLC 2026 PMOS protocol:
        # Myo-Inositol Complex, Berberine Pro 1 cap TID, Omega Pure EPA-DHA 1000 "for the triglycerides"), both
        # re-opened 2026-11-03, and Asher's own PCOS handout and blast (UltraBiotic Daily Multi-Strain, give it 12
        # weeks).  Label facts, doses and claim sources per product: products.d/pcos.json (the five sell sheets).
        # Start here: Myo-Inositol Complex, the one formula made for this condition ("Support for Healthy Ovarian
        # Function"), the product Asher offers by name for PCOS patients, and the one the NutriDyn GLC 2026 PMOS
        # protocol calls "the best-supported supplement here"; [GUIDE23H] 4.7.1 notes inositol's limited harm.
        "cols": [
            # ND680: "Support healthy ovarian function", "Support healthy menstrual cycles", "Support optimal blood
            # glucose balance"
            {"p": "pc_inositol", "need": "Ovaries and cycles", "needsub": "myo- + D-chiro-inositol",
             "start": True, "dose": "dose_from_db",
             "bullets": [claim("Supports healthy ovaries and cycles"), claim("Supports optimal blood glucose balance")]},
            # ND1130: "Promotes healthy glucose metabolism", "Supports heart health & optimal lipid balance";
            # GlucoVantage is dihydroberberine, a form of berberine (the serving line names it exactly)
            {"p": "pc_berberine", "need": "Blood sugar and insulin", "needsub": "berberine + cinnamon",
             "dose": "dose_from_db",
             "bullets": [claim("Promotes healthy glucose metabolism"), claim("Supports heart health and lipid balance")]},
            # ND382: "help ensure users obtain adequate amounts"; "Supports healthy mood and stress levels",
            # "Supports bone and skin tissues", "Supports immune function"
            {"p": "pc_d3_5000_k2", "need": "Vitamin D", "needsub": "D3 5,000 IU with K2", "dose": "dose_from_db",
             "bullets": [claim("Supports healthy vitamin D levels"), claim("Supports mood, bone and immune health")]},
            # The NutriDyn GLC 2026 PMOS protocol uses it "for the triglycerides", but ND416 (Rev. 4/25, re-opened
            # 2026-11-03) makes no triglyceride claim, so neither does the card.  Its claims: "Healthy cardiovascular
            # function", "Healthy immune function", "Skin vitality".  Bullet 1 says "heart" for cardiovascular and
            # bullet 2 joins the last two: "cardiovascular function" and "immune function and skin" each ran to a
            # third line in these five narrow columns, leaving a word and the diamond alone.  The need names the
            # nutrient (ND416: omega-3s are "essential" because the body does not make them), as on the
            # insulin-resistance sheet; the old "Healthy blood fats" implied the triglyceride claim.
            {"p": "pc_omega", "need": "Essential omega-3 fats", "needsub": "EPA + DHA from fish oil",
             "dose": "dose_from_db",
             "bullets": [claim("Supports healthy heart&nbsp;function"), claim("Supports healthy immunity and skin")]},
            # ND460: "Support a healthy gut microbiome"; its text: "promote healthy hormone functions".  The no-break
            # space keeps "microbiome" off a line of its own.
            {"p": "pc_ultrabiotic", "need": "Gut and hormones", "needsub": "7-strain probiotic",
             "dose": "dose_from_db",
             "bullets": [claim("Supports a healthy gut&nbsp;microbiome"), claim("Promotes healthy hormone function")]},
        ],
        # Four notes per edition (2026-11-03 review).  Pharmacists check interactions, pregnancy and depletions;
        # providers order labs, and a change to a blood-sugar medicine goes to the doctor who prescribes it (a DC or
        # ND handing out the practitioner edition usually cannot adjust insulin or a sulfonylurea).  The medicine
        # notes are cautions, never "adds to the drug's effect": wording that a product augments a drug action reads
        # as an implied disease claim (21 CFR 101.93(g)(2)), as the insulin-resistance sheet's review found.
        # Pregnancy: [CHAN93] berberine displaces bilirubin from albumin, "best avoided in jaundiced neonates and
        # pregnant women"; Myo-Inositol Complex carries 500 mg fenugreek seed extract a day (ND680) and fenugreek
        # "is not recommended for use during pregnancy" [OUZIR16] (animal developmental toxicity [KHALKI10]), so the
        # START HERE product is named too; every one of the five labels says to consult a practitioner if pregnant
        # or nursing; [GUIDE23H] 5.8.1-5.8.3: inositol is experimental for fertility and its safety is not known.
        # Nursing: the berberine-bilirubin concern [CHAN93] is for newborns; the LactMed goldenseal (berberine)
        # record, PMID 30000926, could not be opened from this machine.
        # Blood sugar: dihydroberberine (ND1130) and Myo-Inositol Complex's chromium, fenugreek and cinnamon (ND680)
        # bear on blood sugar; low blood sugar is mainly a risk with insulin or a sulfonylurea (glipizide).  Yin J
        # et al. Metabolism 2008;57:712-7, doi:10.1016/j.metabol.2008.01.013 (berberine with existing diabetes
        # treatment, read on PubMed 2026-11-03) is why the prescriber hears first.
        # Drug enzymes: [GUO12] plain berberine 300 mg three times daily for 2 weeks lowered CYP2D6, 2C9 and 3A4
        # activity, a result for plain berberine, not for this product, hence "can slow"; in both editions, as on the
        # fatty-liver sheet.  Vitamin K: D3 5000 has 60 mcg K2 and 15 mcg K1 (ND382); vitamin K works against
        # warfarin (a vitamin K antagonist), and the ND382 label says K2 "is not recommended for patients on
        # blood-thinning medications", so the note names warfarin and covers any blood thinner.
        # B12: [AROD16] and [ADA-S9] (periodic B12 checks on metformin).  [PALM13] the pill and B6, B12, folate,
        # magnesium and zinc.  Vitamin D: the D3 5000 label (ND382) says it exceeds the adult upper intake level
        # (4,000 IU, NIH Office of Dietary Supplements) and that "use should be short-term and include regular
        # monitoring of 25-(OH)" vitamin D (also on the dose bar: "short-term; check your level").
        # Labs: [GUIDE23H] 1.9.9 (OGTT, or A1c), 1.8.3 (lipids); Asher's handout: recheck testosterone and
        # triglycerides at months 1 to 3.
        # "Keep any prescribed medicine" leads the medicine note in both editions (Asher's PCOS handout: "If you
        # are on medication for PCOS, keep taking it exactly as prescribed").
        "rx": {
            "practitioner": [
                "<b>Trying to get pregnant, pregnant or nursing?</b> Do not take Berberine&nbsp;Pro. Myo&#8209;Inositol&nbsp;"
                "Complex has fenugreek, which is not advised in pregnancy: ask {who} before taking it or the rest.",
                "<b>Keep any prescribed medicine.</b> On a blood-sugar medicine? Before you start Berberine&nbsp;Pro or "
                "Myo&#8209;Inositol&nbsp;Complex, tell the doctor who prescribes it: the dose may need a change.",
                "<b>On warfarin or another blood thinner?</b> The vitamin K (K1 and K2) in D3&nbsp;5000 can weaken "
                "warfarin, and berberine can slow the enzymes (CYP3A4, 2D6, 2C9) that clear many drugs: ask {who} "
                "first.",
                "<b>Labs now and at 3 months:</b> blood sugar (glucose tolerance or A1c), lipids, testosterone, "
                "vitamin D (5,000&nbsp;IU is above the 4,000&nbsp;IU upper limit, so use it short-term and recheck), "
                "plus B12 if you take metformin.",
            ],
            "pharmacy": [
                "<b>Trying to get pregnant, pregnant or nursing?</b> Do not take Berberine&nbsp;Pro. Myo&#8209;Inositol&nbsp;"
                "Complex has fenugreek, which is not advised in pregnancy: ask {who} before taking it or the rest.",
                "<b>Keep any prescribed medicine.</b> Insulin or a sulfonylurea (such as glipizide)? Ask the "
                "prescriber first and watch for low blood sugar. Berberine can slow CYP3A4, 2D6 and 2C9, which "
                "clear many drugs.",
                "<b>On warfarin?</b> The vitamin K (K1 and K2) in D3&nbsp;5000 can weaken it. On&nbsp;any blood thinner, "
                "ask first.",
                "<b>The pill</b> can lower B6, B12, folate, magnesium and zinc, and <b>metformin</b> can lower B12 "
                "over time: ask about a check.",
            ],
        },
    },
}
