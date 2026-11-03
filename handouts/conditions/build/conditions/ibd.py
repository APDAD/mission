"""Inflammatory Bowel Disease (ND-GI-103).  Self-contained sheet module: front copy,
front art, front builder and back data all live here.  Shared helpers come from
svgkit / kit; nothing is imported from sheets.py or art.py any more.

Front page, top to bottom:
  intro (SHEET["intro"]) -> the two figures (ulcerative colitis VS Crohn's disease:
  identical bodies, identical anatomy, only the red differs) with a heading above and
  an equal-length caption under each, the KEY between them -> the comparison table,
  on the same centre line -> what can stir up a flare -> nutrients that often run low
  -> the colonoscopy reminder.

Asher's notes on the first draft (2026-11-03), all answered here:
  "Make it look like a real intestines. Make it look like a real human."  Both figures
    are one drawing (figure()) of a proportioned human (head, neck, shoulders, torso,
    thighs fading out) with the whole tract inside: esophagus, stomach, small intestine
    coiled in the centre and framed by the colon (cecum at the patient's lower right,
    which is the viewer's left, then ascending, transverse, descending and sigmoid
    colon and the rectum).  check_inside() proves nothing crosses the body outline.
  "The bottom of the intestines are going over the body."  The rectum now ends well
    above the crotch; every organ is also clipped to the body outline.
  "One has a red dot on the head, the other one doesn't."  Gone.  No unexplained
    marks: the only colour coding is inflamed (red) versus healthy (pink), and the KEY
    names both.  Crohn's reach "from mouth to anus" is said in words.
  "It needs to be even ... more centered."  The two figures sit at 25% and 75% of the
    width with the VS circle on the centre line; headings, captions and the comparison
    table share that grid and the same styles.

Sources for every number and claim on the front (also tagged inline):
  [LEW23]  Lewis JD et al. Incidence, prevalence, and racial and ethnic distribution
           of IBD in the United States. Gastroenterology 2023;165:1197-1205.
           doi:10.1053/j.gastro.2023.07.003 (an estimated 2.39 million Americans are
           diagnosed with IBD; physician-diagnosed, claims data).
  [NCHS26] CDC/NCHS Health E-Stat 122 (Aug 2026): 1.6% of U.S. adults reported ever
           being diagnosed with IBD in 2023-2024 (self-report), so "more than 2
           million" is the conservative floor of both counts.
  [ACGUC]  Rubin DT et al. ACG Clinical Guideline: Ulcerative Colitis in Adults.
           Am J Gastroenterol 2019;114:384-413. doi:10.14309/ajg.0000000000000152
           (UC starts in the rectum and spreads continuously up the colon; affects
           the inner lining; bloody diarrhea; surveillance colonoscopy).
  [ACGCD]  Lichtenstein GR et al. ACG Clinical Guideline: Management of Crohn's
           Disease in Adults. Am J Gastroenterol 2025;120:1225-64.
           doi:10.14309/ajg.0000000000003465 (any part of the tract from mouth to
           anus, most often the terminal ileum and colon; skip lesions; transmural;
           smoking worsens Crohn's; colon cancer surveillance in Crohn's colitis).
  [WEI15]  Weisshof R, Chermesh I. Micronutrient deficiencies in IBD. Curr Opin Clin
           Nutr Metab Care 2015;18:576-81. doi:10.1097/MCO.0000000000000226
           (deficiencies in more than half of patients; most common iron, B12,
           vitamin D, folic acid, zinc among others; iron deficiency is the most
           common cause of anemia).
  [HWA12]  Hwang C, Ross V, Mahadevan U. Micronutrient deficiencies in IBD: from A to
           zinc. Inflamm Bowel Dis 2012;18:1961-81. doi:10.1002/ibd.22906 (iron and
           blood loss; B12 and the ileum; folate and sulfasalazine/methotrexate;
           zinc lost with diarrhea; vitamin D).
  [ANA13]  Ananthakrishnan AN et al. Sleep disturbance and risk of active disease in
           Crohn's disease and ulcerative colitis. Clin Gastroenterol Hepatol
           2013;11:965-71. doi:10.1016/j.cgh.2013.01.021 (poor sleep doubled the
           risk of active Crohn's at 6 months).
  [CCF]    Crohn's & Colitis Foundation, "Managing Flares and Other IBD Symptoms"
           (missed or wrong medicine doses, NSAIDs, antibiotics, smoking and stress
           as possible flare triggers).
"""
import math

from kit import ICONS
from svgkit import T, svg

U = "ibx"   # prefix for every SVG id and CSS class: all sheets share one document in the bundle

# ----------------------------------------------------------------------------- palette
SKIN_EDGE, SKIN_MID, SKIN_HI, SKIN_LINE = "#EBD3C3", "#F5E5DA", "#F9EFE8", "#D6B9A6"
GI = {   # healthy tract: soft pinks
    "edge": "#C47A62", "body": "#EFAC93", "hi": "#FAD8CB", "band": "#D88E74",
    "si_edge": "#CC8670", "si_body": "#F6C3AD", "si_hi": "#FDE5DA", "si_bed": "#E8B09B",
    "st_top": "#F4BCA6", "st_bot": "#E6957B",
}
RED = {  # inflamed
    "edge": "#8E1A16", "body": "#D8332A", "hi": "#F2806F", "band": "#B3231C", "glow": "#E0392F",
}
INK, INK_SOFT, LEAD = "#22292D", "#56626A", "#59646B"


# ----------------------------------------------------------------------------- geometry
def _cr(pts):
    """Uniform Catmull-Rom spline through pts -> list of cubic Bezier segments."""
    segs = []
    n = len(pts)
    for i in range(n - 1):
        p0 = pts[i - 1] if i else pts[i]
        p1, p2 = pts[i], pts[i + 1]
        p3 = pts[i + 2] if i + 2 < n else p2
        c1 = (p1[0] + (p2[0] - p0[0]) / 6, p1[1] + (p2[1] - p0[1]) / 6)
        c2 = (p2[0] - (p3[0] - p1[0]) / 6, p2[1] - (p3[1] - p1[1]) / 6)
        segs.append((p1, c1, c2, p2))
    return segs


def _d(segs, move=True, close=False):
    out = [f"M{segs[0][0][0]:.2f},{segs[0][0][1]:.2f}"] if move else []
    out += [f"C{a[0]:.2f},{a[1]:.2f} {b[0]:.2f},{b[1]:.2f} {c[0]:.2f},{c[1]:.2f}" for _, a, b, c in segs]
    if close:
        out.append("Z")
    return " ".join(out)


def _bez(seg, t):
    p0, p1, p2, p3 = seg
    u = 1 - t
    return (u ** 3 * p0[0] + 3 * u * u * t * p1[0] + 3 * u * t * t * p2[0] + t ** 3 * p3[0],
            u ** 3 * p0[1] + 3 * u * u * t * p1[1] + 3 * u * t * t * p2[1] + t ** 3 * p3[1])


def _split(seg, t):
    """de Casteljau: split one cubic at t -> (left, right)."""
    p0, p1, p2, p3 = seg
    lerp = lambda a, b: (a[0] + (b[0] - a[0]) * t, a[1] + (b[1] - a[1]) * t)
    a, b, c = lerp(p0, p1), lerp(p1, p2), lerp(p2, p3)
    d, e = lerp(a, b), lerp(b, c)
    f = lerp(d, e)
    return (p0, a, d, f), (f, e, c, p3)


def _table(segs, n=40):
    """Arc-length table: [(seg index, t, s)] at n samples per segment."""
    rows, s, prev = [(0, 0.0, 0.0)], 0.0, segs[0][0]
    for i, seg in enumerate(segs):
        for k in range(1, n + 1):
            t = k / n
            p = _bez(seg, t)
            s += math.hypot(p[0] - prev[0], p[1] - prev[1])
            rows.append((i, t, s))
            prev = p
    return rows


def _locate(rows, s):
    for k in range(1, len(rows)):
        if rows[k][2] >= s:
            i0, t0, s0 = rows[k - 1]
            i1, t1, s1 = rows[k]
            f = 0 if s1 == s0 else (s - s0) / (s1 - s0)
            if i0 != i1:          # crossed into a new segment
                return i1, t1 * f
            return i1, t0 + (t1 - t0) * f
    return rows[-1][0], 1.0


def length(segs):
    return _table(segs)[-1][2]


def sub(segs, f0, f1):
    """The part of a spline between arc-length fractions f0 and f1 (0..1)."""
    rows = _table(segs)
    total = rows[-1][2]
    i0, t0 = _locate(rows, f0 * total)
    i1, t1 = _locate(rows, f1 * total)
    out = []
    for i in range(i0, i1 + 1):
        seg = segs[i]
        a = t0 if i == i0 else 0.0
        b = t1 if i == i1 else 1.0
        if b <= a + 1e-6:
            continue
        right = _split(seg, a)[1] if a > 0 else seg
        piece = _split(right, (b - a) / (1 - a))[0] if b < 1 else right
        out.append(piece)
    return out


def line(p, q):
    return (p, (p[0] + (q[0] - p[0]) / 3, p[1] + (q[1] - p[1]) / 3),
            (p[0] + 2 * (q[0] - p[0]) / 3, p[1] + 2 * (q[1] - p[1]) / 3), q)


def rounded(pts, r):
    """A polyline with 90-degree corners, each corner rounded into a quarter circle of
    radius r (cubic approximation).  Two corners one pitch (2r) apart make a clean U-turn."""
    k = 0.5523 * r
    segs, cur = [], pts[0]
    for i in range(1, len(pts) - 1):
        a, b, c = pts[i - 1], pts[i], pts[i + 1]
        ux, uy = (b[0] - a[0]), (b[1] - a[1])
        lu = math.hypot(ux, uy)
        ux, uy = ux / lu, uy / lu
        vx, vy = (c[0] - b[0]), (c[1] - b[1])
        lv = math.hypot(vx, vy)
        vx, vy = vx / lv, vy / lv
        p_in = (b[0] - ux * r, b[1] - uy * r)
        p_out = (b[0] + vx * r, b[1] + vy * r)
        if math.hypot(p_in[0] - cur[0], p_in[1] - cur[1]) > 1e-6:
            segs.append(line(cur, p_in))
        segs.append((p_in, (p_in[0] + ux * k, p_in[1] + uy * k), (p_out[0] - vx * k, p_out[1] - vy * k), p_out))
        cur = p_out
    segs.append(line(cur, pts[-1]))
    return segs


def displace(segs, f):
    """Push every control point through f(x, y) -> (dx, dy): a gentle, coherent wobble."""
    mv = lambda p: (p[0] + f(*p)[0], p[1] + f(*p)[1])
    return [tuple(mv(p) for p in seg) for seg in segs]


def sample(segs, step=0.8):
    """Points with unit normals along a spline, every `step` units."""
    rows = _table(segs, 60)
    total = rows[-1][2]
    out = []
    n = max(2, int(total / step))
    for k in range(n + 1):
        i, t = _locate(rows, total * k / n)
        p = _bez(segs[i], t)
        q = _bez(segs[i], min(1.0, t + 1e-3)) if t < 1 else p
        r = _bez(segs[i], max(0.0, t - 1e-3)) if t > 0 else p
        dx, dy = q[0] - r[0], q[1] - r[1]
        L = math.hypot(dx, dy) or 1.0
        out.append((p, (-dy / L, dx / L)))
    return out


# ----------------------------------------------------------------------------- the body
# Local frame: x = 0 on the midline, y = 0 at the crown, head height H = 62.  Proportions
# follow the classic canon: chin 1H, nipples 2H, navel 3H, crotch 4H, shoulders about 2.2H
# wide, waist about 1.5H.  Right half (viewer's right = the patient's LEFT), crown first.
BODY_R = [(0, 0), (12.2, 1.9), (19.6, 7.6), (22.9, 16.2), (23.6, 25.5), (23.4, 30.5),
          (25.3, 32.4), (25.9, 36.6), (24.9, 41.2), (22.6, 43.8),                 # ear
          (20.9, 48.4), (17.9, 53.6), (14.3, 57.4),                               # jaw to neck
          (13.0, 62.5), (12.9, 69.5), (13.9, 76.5), (17.2, 81.6), (26.5, 85.6),
          (40.0, 89.0), (52.0, 92.4), (60.6, 96.4), (65.6, 101.6), (67.4, 108.8),  # shoulder
          (66.6, 116.6), (63.0, 124.8), (57.8, 132.6), (54.8, 141.0), (53.6, 151.0),
          (52.4, 162.0), (50.4, 172.2), (48.9, 181.6), (49.2, 191.0), (50.8, 200.6),  # waist
          (52.8, 211.0), (54.1, 222.5), (54.5, 233.0), (53.7, 244.0), (52.2, 256.0),  # hips
          (50.6, 266.0), (49.2, 275.0), (48.0, 284.0)]                                # thighs, fading out
CROTCH_R = [(5.6, 284.0), (4.6, 275.0), (3.6, 266.0), (2.3, 257.0), (0, 250.6)]


def body_segs():
    """The closed silhouette as one list of Bezier runs (outer run is one smooth spline
    from the left thigh over the crown to the right thigh, so the crown stays smooth)."""
    left = [(-x, y) for x, y in reversed(BODY_R[1:])]
    outer = _cr(left + BODY_R)
    inner = _cr(CROTCH_R + [(-x, y) for x, y in reversed(CROTCH_R[:-1])])
    return outer, inner


def body_d():
    outer, inner = body_segs()
    return (_d(outer) + f" L{inner[0][0][0]:.2f},{inner[0][0][1]:.2f} " + _d(inner, move=False)
            + f" L{outer[0][0][0]:.2f},{outer[0][0][1]:.2f} Z")


def body_polygon(step=0.6):
    outer, inner = body_segs()
    pts = [p for p, _ in sample(outer, step)] + [p for p, _ in sample(inner, step)]
    return pts


# ----------------------------------------------------------------------------- the tract
# Centre lines (local frame).  Viewer's left = the patient's right.
ST_DY = -6.0   # the stomach sits this far above its drawn coordinates, so its whole J clears the colon
ESO = _cr([(0.0, 58.0), (0.2, 74.0), (0.6, 92.0), (1.4, 106.0), (3.6, 118.4), (7.6, 126.6), (9.6, 129.4)])
W_ESO = 6.2

# Stomach outline: angle of His -> fundus -> greater curvature -> antrum -> pylorus,
# back along the lesser curvature (angular notch) to the cardia.
STOM_GREATER = [(11.0, 130.4), (14.0, 126.4), (20.4, 123.6), (27.4, 125.0), (32.4, 130.8), (34.6, 139.6),
                (34.0, 150.4), (29.8, 160.4), (21.4, 167.2), (10.6, 170.0), (0.4, 168.8), (-6.4, 165.4),
                (-10.6, 161.4)]
STOM_LESSER = [(-10.6, 155.4), (-4.6, 156.8), (1.6, 155.4), (6.2, 149.6), (7.0, 142.2), (6.0, 134.8)]

DUO = _cr([(-11.0, 152.4), (-15.8, 153.6), (-19.4, 157.4), (-20.2, 163.0), (-19.8, 172.0)])
W_DUO = 5.6

# Colon: cecum (start) -> ascending -> hepatic flexure -> transverse -> splenic flexure ->
# descending -> sigmoid (end).  The rectum is its own smooth tube.
COLON = _cr([(-34.6, 226.0), (-34.2, 214.0), (-33.8, 201.0), (-33.6, 188.0), (-34.0, 176.0),
             (-31.4, 167.6), (-24.0, 164.4), (-13.0, 168.2), (-1.5, 173.2), (10.5, 173.0),
             (21.5, 168.0), (30.0, 161.6), (35.6, 158.0), (38.6, 162.6), (37.4, 172.0),
             (35.6, 183.5), (35.0, 195.5), (35.4, 206.5), (33.6, 216.0), (27.4, 222.6),
             (18.6, 223.4), (11.0, 219.4), (5.4, 218.6), (2.0, 221.6), (0.7, 226.4)])
W_COLON = 11.0
RECTUM = _cr([(0.8, 224.6), (0.4, 230.0), (0.1, 234.4), (0.0, 237.6)])
W_RECT = 12.0
CECUM = (-34.6, 227.6, 8.6, 9.0)     # cx, cy, rx, ry

# Small intestine: ONE continuous, non-crossing tube, laid on a 6.8-unit grid inside the
# colon frame (columns c = 0..7 from the patient's right, rows r = 0..6 from the top) and
# rounded so every corner is a true quarter circle.  The jejunum starts on the patient's
# left, tucked under the transverse colon, and hangs in tall upright loops; the ileum sweeps
# across in rows toward the patient's right; the last row, the terminal ileum, runs into the
# side of the cecum.  Loops pack with a hairline between them, like real coils, and a gentle
# coherent wobble keeps it from looking ruled.
_P = 6.8
_SX = [-23.0 + _P * c for c in range(8)]
_SY = [181.0 + _P * r for r in range(7)]
_SI_CELLS = [(7, 0), (7, 1), (7, 2), (7, 3), (7, 4), (6, 4), (6, 3), (6, 2), (6, 1), (6, 0), (5, 0), (4, 0),
             (4, 1), (5, 1), (5, 2), (5, 3), (5, 4), (4, 4), (4, 3), (4, 2), (3, 2), (3, 1), (3, 0),
             (2, 0), (1, 0), (0, 0), (0, 1), (1, 1), (2, 1), (2, 2), (1, 2), (0, 2), (0, 3), (1, 3), (2, 3),
             (3, 3), (3, 4), (2, 4), (1, 4), (0, 4), (0, 5), (1, 5), (2, 5), (2, 6), (1, 6), (0, 6)]
# (cells (3,5) and (3,6) sit under the rectum, so the path skips them: the last U-turn, where the
#  terminal ileum leaves the coils, stays in plain sight instead of vanishing behind the rectum)


def _si_polyline():
    """Corner points of the grid path (straight runs merged), plus a hidden start under
    the transverse colon and a hidden end inside the cecum."""
    pts = [(_SX[c], _SY[r]) for c, r in _SI_CELLS]
    keep = [pts[0]]
    for i in range(1, len(pts) - 1):
        a, b, c = pts[i - 1], pts[i], pts[i + 1]
        if (b[0] - a[0]) * (c[1] - b[1]) - (b[1] - a[1]) * (c[0] - b[0]) != 0:   # a real corner
            keep.append(b)
    keep.append(pts[-1])
    return [(_SX[7], 172.0)] + keep[1:] + [(-31.0, _SY[6])]


SI = displace(rounded(_si_polyline(), _P / 2),
              lambda x, y: (0.55 * math.sin(y / 6.4 + x / 17.0), 0.45 * math.sin(x / 5.6 + y / 23.0)))
W_SI = 5.8


def frac_near(segs, pt):
    """Arc-length fraction of the point on a spline closest to pt."""
    pts = sample(segs, 0.5)
    best = min(range(len(pts)), key=lambda i: math.hypot(pts[i][0][0] - pt[0], pts[i][0][1] - pt[1]))
    return best / (len(pts) - 1)


# Where the red goes (arc-length fractions of each centre line).
UC_COLON = (0.47, 1.0)          # mid-transverse colon -> splenic flexure -> descending -> sigmoid
CD_COLON = [(0.12, 0.25), (0.40, 0.49), (0.71, 0.79)]   # ascending; transverse; descending
CD_SI = (frac_near(SI, (_SX[1] + 2.4, _SY[5])), 1.0)    # terminal ileum: the last U-turn and row, into the cecum
SI_BED = [(-26.6, 179.0), (-12.0, 176.6), (4.0, 177.6), (20.0, 175.0), (28.6, 177.4), (28.8, 196.0),
          (28.6, 211.6), (8.0, 212.6), (0.4, 212.6), (-5.0, 218.0), (-9.0, 225.0), (-18.0, 226.4),
          (-26.8, 225.8), (-27.4, 205.0), (-26.6, 179.0)]


# ----------------------------------------------------------------------------- drawing
def _stroke(d, col, w, extra=""):
    return (f'<path d="{d}" fill="none" stroke="{col}" stroke-width="{w:.2f}" stroke-linecap="round" '
            f'stroke-linejoin="round"{extra}/>')


def tube(segs, w, pal, kind="si", glow=False):
    """A tube along a centre line.  kind: si (smooth), colon (haustra), plain."""
    d = _d(segs)
    out = []
    if glow:
        out.append(_stroke(d, RED["glow"], w + 6.5, ' opacity=".22"'))
        out.append(_stroke(d, RED["glow"], w + 3.4, ' opacity=".3"'))
    if kind == "colon":
        p = 6.0
        out.append(_stroke(d, pal["edge"], w + 2.5, f' stroke-dasharray="0 {p}"'))
        out.append(_stroke(d, pal["edge"], w + 1.3))
        out.append(_stroke(d, pal["body"], w + 0.1, f' stroke-dasharray="0 {p}"'))
        out.append(_stroke(d, pal["body"], w - 1.6))
        out.append(f'<path d="{d}" fill="none" stroke="{pal["band"]}" stroke-width="{w - 2.2:.2f}" '
                   f'stroke-dasharray="0.9 {p - 0.9:.2f}" stroke-dashoffset="{-p / 2 + 0.45:.2f}" opacity=".75"/>')
        out.append(f'<g transform="translate(-0.7,-0.9)">{_stroke(d, pal["hi"], w * 0.26, " opacity=.85")}</g>')
    else:
        out.append(_stroke(d, pal["edge"], w + 2.0))
        out.append(_stroke(d, pal["body"], w))
        out.append(f'<g transform="translate(-0.45,-0.6)">{_stroke(d, pal["hi"], w * 0.24, " opacity=.7")}</g>')
    return "".join(out)


def si_pal(red=False):
    if red:
        return RED
    return {"edge": GI["si_edge"], "body": GI["si_body"], "hi": GI["si_hi"]}


def stomach():
    pts = STOM_GREATER + STOM_LESSER
    segs = _cr(pts + [pts[0]])
    d = _d(segs, close=True)
    return (f'<g transform="translate(0,{ST_DY})">'
            f'<path d="{d}" fill="url(#{U}-stom)" stroke="{GI["edge"]}" stroke-width="1.5" stroke-linejoin="round"/>'
            # a soft sheen and two gastric folds
            f'<path d="M15.5,129.4 C22,126.4 28.6,128 31.4,134.6" fill="none" stroke="#FCE2D8" stroke-width="2.6" '
            'stroke-linecap="round" opacity=".85"/>'
            f'<path d="M11,147 C17,141 25,141 29.6,147.4 M4,160 C11,153.6 21,153.4 27.4,158.2" fill="none" '
            f'stroke="{GI["band"]}" stroke-width="1.3" stroke-linecap="round" opacity=".55"/></g>')


def figure(mode, x, y, s=1.0):
    """One human figure with the whole digestive tract.  mode: 'uc' or 'cd'.  Both modes
    draw the identical body and anatomy; only the red overlays differ."""
    k = f"{U}-{mode}"
    body = body_d()
    g = [f'<g transform="translate({x},{y}) scale({s})">',
         f'<clipPath id="{k}-clip"><path d="{body}"/></clipPath>',
         f'<g mask="url(#{U}-fade)">',
         f'<path d="{body}" fill="url(#{U}-skin)" stroke="{SKIN_LINE}" stroke-width="1.4" stroke-linejoin="round"/>',
         # collarbones and the notch between them: quiet cues that this is a person
         f'<path d="M-4.6,90.6 C-14,88.2 -27,88.6 -45,93.2 M4.6,90.6 C14,88.2 27,88.6 45,93.2" fill="none" '
         f'stroke="{SKIN_EDGE}" stroke-width="1.9" stroke-linecap="round"/>',
         f'<path d="M-4.4,88.4 C-2,91.6 2,91.6 4.4,88.4" fill="none" stroke="{SKIN_EDGE}" stroke-width="1.5" stroke-linecap="round"/>',
         "</g>",
         f'<g clip-path="url(#{k}-clip)">']
    # esophagus (fades in under the jaw) and stomach
    g.append(f'<g mask="url(#{U}-esofade)">{tube(ESO, W_ESO, {"edge": GI["edge"], "body": GI["st_top"], "hi": GI["hi"]})}</g>')
    g.append(tube(DUO, W_DUO, {"edge": GI["edge"], "body": GI["st_bot"], "hi": GI["hi"]}))
    g.append(stomach())
    # small intestine on a darker bed, so the gaps between loops read as depth
    g.append(f'<path d="{_d(_cr(SI_BED), close=True)}" fill="{GI["si_bed"]}" opacity=".7"/>')
    g.append(tube(SI, W_SI, si_pal()))
    if mode == "cd":   # an inflamed ileum is swollen, so it is drawn a little thicker
        g.append(tube(sub(SI, *CD_SI), W_SI + 1.4, si_pal(True), glow=True))
    # rectum, cecum, colon
    g.append(tube(RECTUM, W_RECT, GI, "plain") if mode == "cd" else tube(RECTUM, W_RECT, RED, "plain", glow=True))
    cx, cy, rx, ry = CECUM      # healthy in both figures
    g.append(f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="{GI["body"]}" stroke="{GI["edge"]}" stroke-width="1.4"/>')
    g.append(f'<ellipse cx="{cx - 2}" cy="{cy - 2.4}" rx="{rx * 0.45:.1f}" ry="{ry * 0.36:.1f}" fill="{GI["hi"]}" opacity=".6"/>')
    g.append(tube(COLON, W_COLON, GI, "colon"))
    if mode == "uc":
        g.append(tube(sub(COLON, *UC_COLON), W_COLON, RED, "colon", glow=True))
    else:
        for a, b in CD_COLON:
            g.append(tube(sub(COLON, a, b), W_COLON, RED, "colon", glow=True))
    g.append("</g></g>")
    return "".join(g)


def defs_svg():
    return ("<defs>"
            f'<linearGradient id="{U}-skin" x1="0" y1="0" x2="1" y2="0">'
            f'<stop offset="0" stop-color="{SKIN_EDGE}"/><stop offset=".22" stop-color="{SKIN_MID}"/>'
            f'<stop offset=".5" stop-color="{SKIN_HI}"/><stop offset=".78" stop-color="{SKIN_MID}"/>'
            f'<stop offset="1" stop-color="{SKIN_EDGE}"/></linearGradient>'
            f'<linearGradient id="{U}-stom" x1="0" y1="0" x2=".35" y2="1">'
            f'<stop offset="0" stop-color="{GI["st_top"]}"/><stop offset="1" stop-color="{GI["st_bot"]}"/></linearGradient>'
            # thighs fade into the page instead of being chopped off
            f'<linearGradient id="{U}-fadeg" gradientUnits="userSpaceOnUse" x1="0" y1="250" x2="0" y2="281">'
            '<stop offset="0" stop-color="#fff"/><stop offset="1" stop-color="#000"/></linearGradient>'
            f'<mask id="{U}-fade" maskUnits="userSpaceOnUse" x="-80" y="-10" width="160" height="320">'
            f'<rect x="-80" y="-10" width="160" height="320" fill="url(#{U}-fadeg)"/></mask>'
            f'<linearGradient id="{U}-esog" gradientUnits="userSpaceOnUse" x1="0" y1="60" x2="0" y2="76">'
            '<stop offset="0" stop-color="#000"/><stop offset="1" stop-color="#fff"/></linearGradient>'
            f'<mask id="{U}-esofade" maskUnits="userSpaceOnUse" x="-80" y="-10" width="160" height="320">'
            f'<rect x="-80" y="-10" width="160" height="320" fill="url(#{U}-esog)"/></mask>'
            "</defs>")


# ----------------------------------------------------------------------------- QA helper
def check_inside(margin=3.0):
    """Every tube edge (centre line +/- half width + outline + margin) must sit inside
    the body polygon.  Returns a list of (organ, x, y) points that fail; [] means clean.
    Run by hand while editing: python3 -c 'import conditions.ibd as m; print(m.check_inside())'"""
    poly = body_polygon()

    def inside(px, py):
        c = False
        j = len(poly) - 1
        for i in range(len(poly)):
            xi, yi = poly[i]
            xj, yj = poly[j]
            if (yi > py) != (yj > py) and px < (xj - xi) * (py - yi) / (yj - yi) + xi:
                c = not c
            j = i
        return c

    bad = []
    for name, segs, w, mg in [("esophagus", sub(ESO, 0.12, 1), W_ESO, margin), ("duodenum", DUO, W_DUO, margin),
                              ("small intestine", SI, W_SI, margin), ("colon", COLON, W_COLON + 1.3, margin),
                              ("rectum", RECTUM, W_RECT, margin + 3), ("red glow", COLON, W_COLON + 6.5, 0.5),
                              ("rectum glow", RECTUM, W_RECT + 6.5, 0.5)]:
        pts = sample(segs, 1.0)
        r = w / 2 + 1.0 + mg
        for (px, py), (nx, ny) in pts:
            for sgn in (-1, 1):
                qx, qy = px + sgn * nx * r, py + sgn * ny * r
                if not inside(qx, qy):
                    bad.append((name, round(qx, 1), round(qy, 1)))
        # the round end caps, tested along the tangent (the normal turned 90 degrees)
        for (px, py), (nx, ny), sgn in ((pts[0][0], pts[0][1], -1), (pts[-1][0], pts[-1][1], 1)):
            qx, qy = px + sgn * ny * r, py - sgn * nx * r
            if not inside(qx, qy):
                bad.append((name + " cap", round(qx, 1), round(qy, 1)))
    cx, cy, rx, ry = CECUM
    for a in range(0, 360, 10):
        qx = cx + (rx + 1 + margin) * math.cos(math.radians(a))
        qy = cy + (ry + 1 + margin) * math.sin(math.radians(a))
        if not inside(qx, qy):
            bad.append(("cecum", round(qx, 1), round(qy, 1)))
    stom = _cr(STOM_GREATER + STOM_LESSER + [STOM_GREATER[0]])
    for (px, py), (nx, ny) in sample(stom, 1.0):          # the stomach outline, pushed outward by the margin
        for sgn in (-1, 1):
            qx, qy = px + sgn * nx * (1 + margin), py + ST_DY + sgn * ny * (1 + margin)
            if not inside(qx, qy):
                bad.append(("stomach", round(qx, 1), round(qy, 1)))
    return bad


# ----------------------------------------------------------------------------- the art
FX1, FX2, FY, FS = 190, 570, 4, 1.0     # figure centres sit at 25% and 75% of the width
AW, AH = 760, 286

# Anatomy labels, identical on both figures and mirrored to the outer side of each:
# (name, gloss, label baseline y, target on the LEFT figure, target on the RIGHT figure),
# all in figure-local units.
LABELS = [("Stomach", None, 143.0, (6.6, 139.0), (34.4, 139.0)),
          ("Colon", "large intestine", 178.0, (-40.4, 180.0), (42.6, 180.0)),
          ("Small intestine", None, 214.0, (-18.0, 207.0), (20.0, 207.0)),
          ("Rectum", None, 250.0, (-5.6, 239.6), (5.6, 239.6))]
LAB_X = 70.0     # labels end (left figure) or start (right figure) this far from the midline


def labels(side, fx):
    """side = -1: labels to the left of the figure centred at fx; +1: to the right."""
    o = []
    for name, gloss, y, tl, tr in LABELS:
        tx, ty = tl if side < 0 else tr
        xt = fx + side * LAB_X                 # where the text ends (left side) or starts (right side)
        ax, ay = fx + tx * FS, FY + ty * FS
        y = y * FS
        sx, sy = xt - side * 4.5, FY + y - 4.2  # the leader starts a clear gap away from the text
        d = f"M{sx:.1f},{sy:.1f} L{ax:.1f},{ay:.1f}"
        o.append(f'<path d="{d}" stroke="#fff" stroke-width="3.2" opacity=".85" fill="none" stroke-linecap="round"/>')
        o.append(f'<path d="{d}" stroke="{LEAD}" stroke-width="1.1" fill="none"/>')
        o.append(f'<circle cx="{ax:.1f}" cy="{ay:.1f}" r="2.3" fill="{INK}" stroke="#fff" stroke-width="1"/>')
        anchor = "end" if side < 0 else "start"
        o.append(T(xt, FY + y, name, 11.6, 800, INK, anchor))
        if gloss:
            o.append(T(xt, FY + y + 12.6, gloss, 10, 500, INK_SOFT, anchor))
    return "".join(o)


def key_swatch(red):
    """A short stretch of colon drawn exactly like the art."""
    segs = [line((-13, 0), (13, 0))]
    return tube(segs, 9.0, RED if red else GI, "colon", glow=red)


def key_svg(cx, y):
    w, h = 158, 66
    x = cx - w / 2
    rows = [(True, "Inflamed", "red, swollen, sore"), (False, "Healthy bowel", "no inflammation")]
    o = [f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="9" fill="#fff" stroke="#C9D6D5" stroke-width="1.3"/>',
         f'<rect x="{cx - 21}" y="{y - 7}" width="42" height="14" rx="7" fill="#fff"/>',
         T(cx, y + 4, "KEY", 10, 800, "#0D5A56", "middle", ls=1.8)]
    for i, (red, a, b) in enumerate(rows):
        ry = y + 22 + i * 25
        o.append(f'<g transform="translate({x + 26},{ry})">{key_swatch(red)}</g>')
        o.append(T(x + 50, ry - 1.2, a, 11.2, 800, INK))
        o.append(T(x + 50, ry + 10.4, b, 9.8, 500, INK_SOFT))
    return "".join(o)


def art_ibd(t):
    o = [defs_svg(), figure("uc", FX1, FY, FS), figure("cd", FX2, FY, FS),
         labels(-1, FX1), labels(1, FX2)]
    # the centre line: what the picture shows, VS, and the key
    o.append(T(380, FY + 34, "WHERE IT", 11, 800, t["deep"], "middle", ls=1.8))
    o.append(T(380, FY + 48, "SHOWS UP", 11, 800, t["deep"], "middle", ls=1.8))
    o.append(f'<circle cx="380" cy="{FY + 128}" r="33" fill="#fff" stroke="{t["c1"]}" stroke-width="3"/>')
    o.append(T(380, FY + 139, "VS", 30, 900, "#D0442E", "middle"))
    o.append(key_svg(380, FY + 196))
    return svg(AW, AH, "".join(o), "Two identical human figures with the whole digestive tract inside. In ulcerative "
               "colitis, one unbroken stretch of the colon is red, from the rectum up. In Crohn's disease, separate red "
               "patches sit at the end of the small intestine and in the colon, with healthy bowel between them.")


# ----------------------------------------------------------------------------- front blocks
CAPTIONS = [("Ulcerative colitis",     # [ACGUC]
             "One unbroken stretch of inflammation that starts in the rectum and climbs the colon."),
            ("Crohn's disease",        # [ACGCD]
             "Patchy inflammation with healthy gaps, most often at the end of the small intestine.")]

COMPARE = [   # (row, ulcerative colitis, Crohn's disease)   [ACGUC] [ACGCD]
    ("Where", "Colon and rectum only", "Anywhere from mouth to anus, most often the end of the small intestine"),
    ("Pattern", "One continuous stretch, no gaps", "Patches, with healthy bowel between them"),
    ("Depth", "The inner lining of the bowel", "Can go through the whole bowel wall"),
    ("Pain", "Often the lower left belly", "Often the lower right belly"),
    ("Bleeding", "Common, with bowel movements", "Less common"),
]

# What can stir up a flare: [CCF] missed doses, NSAIDs, antibiotics, smoking, stress;
# [ANA13] poor sleep (Crohn's); [ACGCD] smoking worsens Crohn's (it is not a UC trigger,
# so it is labelled); gut infections such as C. difficile [ACGUC]; trigger foods differ by person.
TRIGGERS = [("headache", "Stress"), ("moon", "Poor sleep"), ("sensitive", "Trigger foods"),
            ("capsule", "NSAID pain relievers"), ("rx", "Antibiotics"), ("microbe", "Gut infections"),
            ("smoke", "Smoking (Crohn's)"), ("calendar", "Missed medicine")]

# Nutrients that often run low [WEI15] [HWA12]
NUTRIENTS = [("Fe", "Iron", "lost with bleeding"),
             ("D", "Vitamin D", "key for strong bones"),
             ("B12", "Vitamin B12", "absorbed at the end of the small intestine"),
             ("B9", "Folate", "lowered by some IBD medicines"),
             ("Zn", "Zinc", "lost with diarrhea")]


def _ic(name, size, sw=3.0):
    return (f'<svg class="ic" viewBox="0 0 64 64" style="width:{size};height:{size}" fill="none" stroke="currentColor" '
            f'stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICONS[name]}</svg>')


def front(t, ed):
    heads = "".join(f"<div><b>{h}</b></div>" for h, _ in CAPTIONS)
    caps = "".join(f"<div><p>{c}</p></div>" for _, c in CAPTIONS)
    rows = "".join(f'<div class="{U}-row"><div>{a}</div><span>{k}</span><div>{b}</div></div>' for k, a, b in COMPARE)
    trig = "".join(f"<div>{_ic(ic, '0.25in', 3.2)}<span>{lab}</span></div>" for ic, lab in TRIGGERS)
    coins = "".join(f'<div><b>{s}</b><em>{n}</em><span>{why}</span></div>' for s, n, why in NUTRIENTS)
    return (f'<div class="{U}-f">'
            f'<div class="{U}-heads">{heads}</div>'
            f'<div class="art {U}-art">{art_ibd(t)}</div>'
            f'<div class="{U}-caps">{caps}</div>'
            f'<div class="{U}-cmp">{rows}</div>'
            f'<div class="{U}-h">What can stir up a flare</div><div class="{U}-trig">{trig}</div>'
            f'<div class="{U}-h">Nutrients that often run low in IBD</div>'
            f'<div class="{U}-nut"><div class="{U}-stat"><b>More than half</b><p>of people with IBD run low on at '
            'least one vitamin or mineral, more often in Crohn\'s and during flares.</p></div>'
            f'<div class="{U}-dep"><div class="{U}-coins">{coins}</div>'
            f'<div class="{U}-ask">Ask {{who}} whether a nutrient check makes sense for you.</div></div></div>'
            # [ACGUC] [ACGCD]: surveillance colonoscopy for long-standing colitis
            f'<p class="{U}-scope">Years of colon inflammation raise colon cancer risk: keep every '
            '<b>colonoscopy</b>, even in good stretches.</p>'
            '</div>')


CSS = r"""
.ibx-f{display:flex;flex-direction:column}
.ibx-art svg{display:block;width:100%;height:auto}
.ibx-heads,.ibx-caps{display:grid;grid-template-columns:1fr 1fr;text-align:center}
.ibx-heads b{font:900 13.5pt Merriweather,Georgia,serif;color:var(--deep);letter-spacing:-.005em}
.ibx-heads div{display:flex;flex-direction:column;align-items:center}
.ibx-heads div::after{content:"";width:0.42in;height:3px;border-radius:2px;background:var(--c1);margin-top:3px}
.ibx-caps p{margin:1px auto 0;max-width:3.0in;font-size:8.6pt;line-height:1.3;color:#2B3236;text-wrap:balance}
.ibx-cmp{margin-top:0.08in;border-top:1px solid #D5E4E2}
.ibx-row{position:relative;display:grid;grid-template-columns:1fr 1fr;border-bottom:1px solid #D5E4E2}
.ibx-row:nth-child(even){background:var(--tint)}
.ibx-row>div{padding:3px 0.54in;text-align:center;font-size:8.4pt;line-height:1.25;color:#2B3236;
  display:flex;align-items:center;justify-content:center;min-height:0.22in;text-wrap:balance}
.ibx-row>span{position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);width:0.9in;text-align:center;
  font:800 7.1pt Inter,sans-serif;letter-spacing:.12em;text-transform:uppercase;color:#fff;background:var(--c1);
  border-radius:99px;padding:2.5px 0}
.ibx-h{font:800 7.5pt Inter,sans-serif;letter-spacing:.14em;text-transform:uppercase;color:var(--deep);
  text-align:center;margin:0.09in 0 0.035in}
.ibx-trig{display:grid;grid-template-columns:repeat(8,1fr);background:linear-gradient(90deg,var(--c1),var(--c2));
  border-radius:6px;padding:0.045in 0.04in}
.ibx-trig>div{display:flex;flex-direction:column;align-items:center;text-align:center;color:#fff;padding:0 2px}
.ibx-trig span{font:800 7.2pt Inter,sans-serif;letter-spacing:.05em;text-transform:uppercase;line-height:1.15;margin-top:2px}
.ibx-nut{display:grid;grid-template-columns:1.62in 1fr;gap:0.12in;align-items:center;
  background:var(--soft);border-radius:10px;padding:0.06in 0.1in 0.06in 0.14in}
.ibx-stat b{display:block;font:900 15pt/1.05 Merriweather,Georgia,serif;color:var(--c1)}
.ibx-stat p{margin:3px 0 0;font-size:8pt;line-height:1.3;color:#2B3236}
.ibx-dep{background:#fff;border-radius:8px;padding:0.05in 0.05in 0.04in}
.ibx-coins{display:grid;grid-template-columns:repeat(5,1fr);gap:0.05in}
.ibx-ask{text-align:center;font-size:7.6pt;color:#3F4A50;margin-top:3px}
.ibx-coins>div{display:flex;flex-direction:column;align-items:center;text-align:center}
.ibx-coins b{width:0.36in;height:0.36in;border-radius:50%;background:var(--c1);color:#fff;display:flex;align-items:center;
  justify-content:center;font:800 9.6pt Inter,sans-serif;box-shadow:0 0 0 2px #fff,0 0 0 3.2px #9FD0CB}
.ibx-coins em{font-style:normal;font:800 7.7pt Inter,sans-serif;color:#1F2A2E;margin-top:3px}
.ibx-coins span{font-size:7.1pt;line-height:1.18;color:#3F4A50}
.ibx-scope{margin:0.08in auto 0;text-align:center;font-size:8.4pt;line-height:1.3;color:#2B3236;background:var(--soft);
  border-radius:6px;padding:0.045in 0.16in;width:100%}
.ibx-scope b{color:var(--deep)}
"""


# ----------------------------------------------------------------------------- the sheet
SHEET = {
    "slug": "ibd", "code": "ND-GI-103", "order": 3, "theme": "teal", "series": "Gut Health Series",
    # same left-to-right order as the two figures
    "title": "Inflammatory Bowel Disease", "sub": "Ulcerative colitis and Crohn's disease",
    # "More than 2 million": [LEW23] 2.39 million diagnosed (claims data); [NCHS26] 1.6% of adults self-report,
    # so 2 million is the floor of both.  Shared symptoms; flares and quiet stretches (remission): [ACGUC] [ACGCD].
    "intro": ("Inflammatory bowel disease (IBD) is a long-term condition in which the immune system keeps part of the digestive "
              "tract inflamed. <b>More than 2 million Americans</b> live with it. The two main types, <b>ulcerative colitis</b> "
              "and <b>Crohn's disease</b>, share belly pain, urgent diarrhea, tiredness and weight loss, with flares that come "
              "and go between quieter stretches. A gastroenterologist leads the care. Food, lifestyle and nutrient support "
              "work alongside that care, never instead of it."),
    "front": front,
    "css": CSS,
    # Back page: unchanged from the first draft (a later pass revises the products).
    "back": {
        "life_title": "Lifestyle Modifications", "style": "hex",
        "life": [("sensitive", "Find food triggers", "Remove foods your care team identifies as a sensitivity or intolerance."),
                 ("sugar", "Limit sugar", "Sugar and ultra-processed food feed the wrong microbes."),
                 ("fish", "Eat enough", "More protein and calories during flares, to protect weight and muscle."),
                 ("breath", "Lower stress", "Stress is one of the most common flare triggers."),
                 ("rx", "Ask about NSAIDs", "Ibuprofen and naproxen can trigger flares. Use antibiotics only when needed."),
                 ("walk", "Move gently", "Regular low to moderate exercise.")],
        "cols": [
            {"p": "ultrabiotic_xs", "need": "Rebalance the microbiome", "needsub": "high-potency probiotic",
             "bullets": ["Supports a balanced gut microbiome", "Supports healthy bowel function"], "dose": "dose_from_db"},
            {"p": "curcumin_bcm95", "need": "Inflammatory balance", "needsub": "curcumin", "start": True,
             "bullets": ["Supports a healthy inflammatory response", "Enhanced-absorption curcumin"], "dose": "dose_from_db"},
            {"p": "d3_5000_k2", "need": "Vitamin D", "needsub": "D3 with K2",
             "bullets": ["Supports normal immune function", "Low vitamin D is common in IBD"], "dose": "dose_from_db"},
            {"p": "gi_integrity", "need": "Repair the lining", "needsub": "L-glutamine, DGL, aloe",
             "bullets": ["Fuel for the cells that line your gut", "Soothing botanicals"], "dose": "1 scoop daily", "dosesub": "in 6 to 8 oz water"},
            {"p": "gi_defend", "need": "Barrier and tolerance", "needsub": "serum-derived bovine immunoglobulins",
             "bullets": ["Binds microbial toxins in the gut", "Supports barrier function"], "dose": "dose_from_db"},
        ],
        "rx": ["<b>Steroids</b> (prednisone, budesonide) lower vitamin D and calcium. Ask about bone health.",
               "<b>Sulfasalazine and methotrexate</b> lower folate. Ask whether you need a folate supplement.",
               "<b>Never stop IBD medicine</b> during a good stretch without your gastroenterologist. Ask before any new supplement."],
    },
}
