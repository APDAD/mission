"""Inflammatory Bowel Disease (ND-GI-103).  Self-contained sheet module: front copy,
front art, front builder and back data all live here.  Shared helpers come from
svgkit / kit; nothing is imported from sheets.py or art.py any more.

Front page, top to bottom:
  intro (SHEET["intro"]) -> "Where the inflammation is" -> the two figures (ulcerative
  colitis VS Crohn's disease: identical bodies, identical anatomy, only the red differs)
  with a heading above and an equal-length caption under each, VS and the KEY between them
  -> the comparison table (column chips, same centre line) -> what can stir up a flare ->
  nutrients that often run low -> the colonoscopy reminder.

Asher's notes on the first draft (2026-11-03), all answered here:
  "Make it look like a real intestines. Make it look like a real human."  Both figures
    are one drawing (figure()) of a proportioned human (head, neck, shoulders, torso,
    thighs fading out) with the whole tract inside: esophagus, stomach, duodenum diving
    behind the colon, the small intestine as a pile of soft, rounded, overlapping loops
    that starts under the transverse colon and ends in the side of the cecum, and the
    colon framing it (cecum pouch at the patient's lower right, which is the viewer's
    left, then ascending, transverse, descending and sigmoid colon and the rectum).
    check_inside() proves nothing crosses the body outline.
  "The bottom of the intestines are going over the body."  The rectum ends well above
    the crotch; every organ is also clipped to the body outline.
  "One has a red dot on the head, the other one doesn't."  Gone.  No unexplained marks:
    the only colour code is inflamed (red) versus healthy (pink), and the KEY names both.
    Crohn's reach "from mouth to anus" is said in words.
  "It needs to be even ... more centered."  The two figures sit at 25% and 75% of the
    width with the VS circle on the centre line; headings, captions and the comparison
    table share that grid and the same styles.

Art-director review (2026-11-03), answered: no leader touches red (check_leaders());
"End of the small intestine" is called out on both figures; the small intestine is an
organic, grown coil (tools note below); the duodenum dives under the colon and the
jejunum comes out below it; stomach in front of the colon; cecum is a real pouch; no bed
slivers; KEY airier; VS out of the red; head and neck re-proportioned.

Final front review (2026-11-03), answered without redesigning the page: the two "End of
the small intestine" callouts are an exact pair (same baseline, same offset from the hips,
same route under the cecum, TI_VIA), with the VS and the KEY raised so the KEY ends well
above the Crohn's one; the rectum is drawn after the colon from the colon's own end and
end tangent, cut flat there and flaring from the colon's widths (rectum_tube()), so the
joint reads as one bowel; the sigmoid meets it higher, so the rectum is 21 units long, not
a stub; the cecum's highlight starts on the colon stripe (no kink); the Crohn's stomach dot
sits inside the stomach; the heading bars clear the head crowns; the flare band runs deep to
c1 (white caps 4.6:1 or better); the capsule icon is full size and the germ is a round cell
with pili and a flagellum; curly apostrophes throughout; the Fistulas cell says what a
fistula is.  check_inside(), check_leaders() and check_text() run clean at import.

Back page (2026-11-03): NutriDyn's IBD program (sources below) in the competitor's five
nutrient slots, the medicine line under the band title, protocol-aligned lifestyle steps,
and edition-specific checks.  Sources for the back:
  [ND584]  NutriDyn 5R GI Restoration Program guide ND584 Rev. 1/22: REPAIR (days 1-10,
           with the IBD note "If the patient exhibits significant GI inflammation, replace
           the Dynamic GI Integrity with Dynamic Inflam-Eze"), RESTORE & RETAIN (GI Restore,
           days 11-24), clean-eating, reintroduction, exercise and stress sections.
  [AUTO23] Asher's Autoimmune Diseases protocol email, 2023-05-08 (lists IBD; Inflam-Eze,
           UltraBiotic Defense, D3 with K2; Mediterranean-type diet; know the vitamin D level;
           90-120 days before judging the plan).
  [BLAST26] NutriDyn Direct Mail blast "New Research on Inflammation", 2026-04-06 (wild-caught
           fish; olive, flax and walnut oils; 5-7 vegetable servings a day).
  [AGA24]  Hashash JG et al. AGA Clinical Practice Update on Diet and Nutritional Therapies in
           Patients With IBD. Gastroenterology 2024;166:521-532. doi:10.1053/j.gastro.2023.11.303
           (BPA 1 Mediterranean diet low in ultraprocessed food and added sugar; BPA 2 soft
           texture with strictures; BPA 9 malnutrition screening; BPA 10 vitamin D, iron, B12).
  [ESPEN17] Forbes A et al. ESPEN guideline: Clinical nutrition in IBD. Clin Nutr
           2017;36:321-347. doi:10.1016/j.clnu.2016.12.027 (protein needs rise in some
           patients; exclusion diets generally not recommended).
  [ACR17]  Buckley L et al. 2017 ACR Guideline for Glucocorticoid-Induced Osteoporosis.
           Arthritis Care Res 2017;69:1095-1110. doi:10.1002/acr.23279 (calcium and vitamin D
           for long-term glucocorticoid users).
  [SKV11]  Skversky AL et al. J Clin Endocrinol Metab 2011;96:3838-45. doi:10.1210/jc.2011-1600
           (steroid users had twice the odds of 25(OH)D under 10 ng/mL, NHANES 2001-2006).
  [ODSK]   NIH Office of Dietary Supplements, Vitamin K fact sheet (vitamin K and warfarin).
  [DRUGS-C] Drugs.com interaction checker: curcumin with warfarin, moderate (bleeding); web
           search 2026-11-03.
  Label facts and product sources: build/products.d/ibd.json.

Sources for every number and claim on the front (also tagged inline):
  [LEW23]  Lewis JD et al. Incidence, prevalence, and racial and ethnic distribution
           of IBD in the United States. Gastroenterology 2023;165:1197-1205.
           doi:10.1053/j.gastro.2023.07.003 (an estimated 2.39 million Americans are
           diagnosed with IBD; physician-diagnosed, claims data).  Checked in PubMed.
  [NCHS26] CDC/NCHS Health E-Stat 122, "Inflammatory Bowel Disease Among Adults Age 18
           and Older: United States, 2023-2024" (Aug 2026): 1.6% of adults had ever been
           told they have Crohn's disease or ulcerative colitis (NHIS self-report).
           cdc.gov could not be opened from the build machine; title, number and date
           were confirmed from the CDC listing in a web search.  "More than 2 million"
           rests on [LEW23] alone and is the conservative floor of both counts.
  [ACGUC]  Rubin DT et al. ACG Clinical Guideline: Ulcerative Colitis in Adults.
           Am J Gastroenterol 2019;114:384-413. doi:10.14309/ajg.0000000000000152
           (UC starts in the rectum and spreads continuously up the colon; affects
           the inner lining; bloody diarrhea; surveillance colonoscopy).
  [ACGCD]  Lichtenstein GR et al. ACG Clinical Guideline: Management of Crohn's
           Disease in Adults. Am J Gastroenterol 2025;120:1225-64.
           doi:10.14309/ajg.0000000000003465 (any part of the tract from mouth to
           anus, most often the terminal ileum and colon; skip lesions; transmural, so
           fistulas (penetrating disease) can form; smoking worsens Crohn's; colon cancer
           surveillance in Crohn's colitis).
  [CCUK]   Crohn's & Colitis UK, "Living with a fistula" (patient guide): about 1 in 4
           people with Crohn's develop a fistula at some time; fistulas are much less
           common in UC (about 1 in 35).  Basis of "Uncommon" in the table.
  [CCF-T]  Crohn's & Colitis Foundation patient pages on the types of UC and Crohn's:
           left-sided colitis gives cramping and pain on the LEFT side of the belly
           ("Living with Ulcerative Colitis": "The pain may be stronger on the left
           side"); ileocolitis and ileitis, the most common Crohn's types, give pain in
           the lower RIGHT or middle of the belly.  The ACG guidelines do not give pain
           location, so the Pain row is tagged to these pages.  (The CCF site could not
           be opened from the build machine; wording confirmed from search excerpts.)
  [WEI15]  Weisshof R, Chermesh I. Micronutrient deficiencies in IBD. Curr Opin Clin
           Nutr Metab Care 2015;18:576-81. doi:10.1097/MCO.0000000000000226
           (deficiencies in more than half of patients; most common iron, B12,
           vitamin D, folic acid, zinc among others; iron deficiency is the most
           common cause of anemia).
  [HWA12]  Hwang C, Ross V, Mahadevan U. Micronutrient deficiencies in IBD: from A to
           zinc. Inflamm Bowel Dis 2012;18:1961-81. doi:10.1002/ibd.22906 (iron and
           blood loss; B12 and the ileum; folate and sulfasalazine/methotrexate;
           zinc lost with diarrhea; vitamin D and bone).
  [KIM20]  Kim KB et al. Inflammatory bowel disease and vitamin D. Korean J Gastroenterol
           2020;76:275-81. doi:10.4166/kjg.2020.160 (low vitamin D in IBD "may be caused
           by low exposure to sunlight, dietary malabsorption" and impaired activation);
           also Margulies SL et al. J Dig Dis 2015;16:617-33, doi:10.1111/1751-2980.12283
           (insufficient sunlight and inflammation).  Basis of the Vitamin D coin.
  [ANA13]  Ananthakrishnan AN et al. Sleep disturbance and risk of active disease in
           Crohn's disease and ulcerative colitis. Clin Gastroenterol Hepatol
           2013;11:965-71. doi:10.1016/j.cgh.2013.01.021 (poor sleep doubled the
           risk of active Crohn's at 6 months, aOR 2.00; no effect in UC, OR 1.14,
           95% CI 0.75-1.74; so the trigger is labelled "(Crohn's)").
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
GI = {   # healthy tract: one family of soft pinks (the small intestine is a hair lighter than the colon)
    "edge": "#C47A62", "body": "#EFAC93", "hi": "#FAD8CB", "band": "#D88E74",
    "si_edge": "#C27B64", "si_body": "#F1B49D", "si_shade": "#E49E86", "si_hi": "#FCDDD1",
    "si_under": "#D48B75", "cavity": "#E4A893",
    "shadow": "#7A3B2C", "st_top": "#F4BCA6", "st_bot": "#E6957B",
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


def frac_at(segs, s):
    """Arc-length fraction of the point `s` units from the start (negative: from the end)."""
    total = length(segs)
    return (s if s >= 0 else total + s) / total


def nearest(segs, pt):
    """The point on a spline closest to pt."""
    return min((p for p, _ in sample(segs, 0.4)), key=lambda p: math.hypot(p[0] - pt[0], p[1] - pt[1]))


# ----------------------------------------------------------------------------- the body
# Local frame: x = 0 on the midline, y = 0 at the crown, head height H = 62.  Proportions
# follow the classic canon: chin 1H, nipples 2H, navel 3H, crotch 4H, shoulders about 2.2H
# wide, waist about 1.5H.  The head is 44.4 wide (0.72 of H) and the neck 30 wide (0.68 of
# the head), so it reads as a person, not a mannequin.  Right half (viewer's right = the
# patient's LEFT), crown first.
BODY_R = [(0, 0), (11.5, 1.9), (18.5, 7.6), (21.6, 16.2), (22.2, 25.5), (22.0, 30.5),
          (24.0, 32.4), (24.6, 36.6), (23.6, 41.2), (21.4, 43.8),                 # ear
          (19.9, 48.4), (17.4, 53.3), (15.6, 57.2),                               # jaw to neck
          (15.0, 62.5), (15.0, 69.5), (16.0, 76.0), (18.8, 81.2), (27.0, 85.5),
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

# Duodenum: the short bulb from the pylorus, then down behind the hepatic flexure and the
# transverse colon.  It ends (cap included) under the colon, so nothing dangles below it;
# the rest of the C-loop is hidden, as in a real front view, and the small intestine comes
# back out from under the transverse colon just left of the midline (SI_PTS[0..5]).
DUO = _cr([(-11.0, 152.4), (-15.8, 153.6), (-19.4, 157.4), (-20.4, 162.2), (-20.2, 166.0)])
W_DUO = 5.6

# Colon: cecum (start) -> ascending -> hepatic flexure -> transverse -> splenic flexure ->
# descending -> sigmoid (end).  The rectum is its own smooth tube.
COLON = _cr([(-34.6, 226.0), (-34.2, 214.0), (-33.8, 201.0), (-33.6, 188.0), (-34.0, 176.0),
             (-31.4, 167.6), (-24.0, 164.4), (-13.0, 168.2), (-1.5, 173.2), (10.5, 173.0),
             (21.5, 168.0), (30.0, 161.6), (35.6, 158.0), (38.6, 162.6), (37.4, 172.0),
             (35.6, 183.5), (35.0, 195.5), (35.4, 206.5), (33.0, 215.0), (26.6, 220.2),
             (18.4, 220.6), (11.6, 216.6), (6.6, 212.6), (2.8, 212.4), (1.0, 215.6)])
W_COLON = 11.0
# The rectum is drawn AFTER the colon, starting exactly at the colon's end with the colon's own end
# tangent and a flat (butt) top, so it covers the colon's round end cap: one continuous bowel, no
# seam arc (front recheck 2026-11-03).  The sigmoid now meets it higher (about y 215), so the rectum
# is 21 units long instead of a 13-unit stub; its round bottom cap ends at y 243, inside the crotch
# line at 250.6 (check_inside()).
_CEND = COLON[-1][3]
_CTAN = (COLON[-1][3][0] - COLON[-1][2][0], COLON[-1][3][1] - COLON[-1][2][1])
_CL = math.hypot(*_CTAN)
RECTUM = [(_CEND, (_CEND[0] + _CTAN[0] / _CL * 6.0, _CEND[1] + _CTAN[1] / _CL * 6.0),
           (0.0, 229.6), (0.0, 236.0))]
W_RECT = 12.0
# Cecum: the colon's widened blind pouch, drawn in the colon's own style and continuous with
# the ascending colon: it widens from the colon's 11 units at the top to 14.3 (1.3x) at the
# bottom.  The terminal ileum runs into its inner (medial) wall.
CEC_TOP, CEC_BOT, CEC_W = (-34.6, 218.0), (-35.1, 230.2), 14.3

# Small intestine: ONE continuous, non-crossing tube, about 290 units long.  The centre line
# was GROWN, not ruled, and is baked here as plain points: constrained differential growth
# (a chain that lengthens a point at a time, folds kept one tube-width (6.7) apart, pushed
# off the colon, rectum and cecum), then Taubin-smoothed, with the jejunum's first hook and
# the bend into the terminal ileum rounded by hand.  Edit points freely, then re-run
# check_inside() and check_leaders(); keep neighbouring runs at least ~6.3 apart.  It
# starts under the transverse colon just left of the midline (the duodenojejunal flexure),
# coils as jejunum through the upper left of the belly (the viewer's upper right), crosses to
# the lower right as ileum, and its last run, the terminal ileum, enters the cecum's side.
SI_PTS = [(5.2, 170.5), (5.5, 172.8), (5.8, 175.0), (6.0, 177.2), (5.9, 179.4), (5.2, 181.4), (3.8, 183.0),
          (1.9, 183.8), (-0.1, 183.8), (-1.8, 183.6), (-3.1, 185.2), (-3.4, 187.4), (-2.6, 189.3), (-0.9, 190.7),
          (1.2, 191.4), (3.3, 190.9), (5.3, 189.9), (7.4, 189.3), (9.2, 190.4), (10.9, 191.8), (12.8, 192.6),
          (14.5, 191.3), (15.7, 189.4), (15.6, 187.4), (14.4, 185.6), (13.4, 183.6), (13.6, 181.4), (15.1, 179.9),
          (17.1, 179.1), (19.3, 178.9), (20.3, 180.8), (21.2, 182.8), (22.7, 184.5), (24.5, 185.6), (26.4, 186.6),
          (27.2, 188.6), (27.4, 190.8), (27.4, 193.0), (27.0, 195.1), (25.6, 196.5), (23.6, 195.8), (21.8, 194.5),
          (19.8, 195.1), (18.3, 196.7), (17.7, 198.7), (18.9, 200.6), (20.4, 202.1), (22.3, 203.3), (24.2, 204.3),
          (25.2, 206.2), (24.7, 208.3), (23.3, 210.0), (21.4, 211.0), (19.3, 210.4), (17.6, 209.1), (16.0, 207.6),
          (14.6, 205.9), (13.3, 204.1), (12.1, 202.3), (10.9, 200.4), (9.3, 198.9), (7.3, 198.0), (5.3, 198.5),
          (3.9, 200.2), (3.4, 202.2), (4.3, 204.1), (6.0, 205.5), (6.8, 207.4), (6.4, 209.5), (4.7, 210.8),
          (2.5, 211.2), (0.4, 210.8), (-1.3, 209.4), (-3.2, 208.3), (-4.7, 206.7), (-5.3, 204.7), (-4.8, 202.6),
          (-3.8, 200.6), (-4.2, 198.5), (-5.4, 196.6), (-7.1, 195.4), (-8.9, 194.0), (-9.9, 192.2), (-10.1, 190.0),
          (-10.5, 187.8), (-11.5, 185.9), (-13.4, 185.2), (-15.2, 186.3), (-16.6, 188.0), (-17.7, 189.9), (-18.6, 191.9),
          (-18.2, 193.9), (-16.6, 195.3), (-15.0, 196.9), (-13.8, 198.7), (-12.9, 200.7), (-12.3, 202.8), (-12.5, 204.9),
          (-14.0, 206.4), (-16.2, 206.7), (-18.1, 205.8), (-19.1, 203.8), (-19.9, 201.8), (-21.6, 200.5), (-23.7, 200.5),
          (-25.4, 201.7), (-25.9, 203.8), (-25.9, 206.0), (-25.6, 208.2), (-25.1, 210.4), (-24.6, 212.5), (-23.7, 214.5),
          (-21.9, 215.7), (-19.7, 215.8), (-17.5, 215.5), (-15.5, 214.7), (-13.5, 213.7), (-11.5, 212.8), (-9.4, 212.3),
          (-7.4, 213.1), (-5.9, 214.6), (-5.2, 216.7), (-5.6, 218.9), (-7.1, 220.6), (-9.2, 221.5), (-11.5, 221.8),
          (-13.8, 222.0), (-16.2, 222.2), (-18.7, 222.5), (-20.9, 222.6), (-23.1, 222.8), (-25.3, 222.9), (-27.5, 223.1),
          (-29.6, 223.4), (-31.8, 223.7), (-34.0, 224.0)]
SI = _cr(SI_PTS)
W_SI = 5.8
SI_LOOP = 23.0          # the coil is drawn as separate loops about this long, each on top of the one before

# Where the red goes (arc-length fractions of each centre line).
UC_COLON = (0.47, 1.0)          # mid-transverse colon -> splenic flexure -> descending -> sigmoid
CD_COLON = [(0.12, 0.25), (0.40, 0.49), (0.62, 0.69)]   # ascending; transverse; descending (splenic flexure healthy)
CD_SI = (frac_at(SI, -36.0), 1.0)   # terminal ileum: its last 36 units, into the cecum
TI_DOT = nearest(SI, (-16.0, 222.0))   # where both "End of the small intestine" leaders land (on the terminal ileum)


# ----------------------------------------------------------------------------- drawing
def _stroke(d, col, w, extra="", cap="round"):
    return (f'<path d="{d}" fill="none" stroke="{col}" stroke-width="{w:.2f}" stroke-linecap="{cap}" '
            f'stroke-linejoin="round"{extra}/>')


def glow(segs, w):
    """The soft red halo of an inflamed stretch.  Drawn UNDER the healthy organs, so it shows
    on the skin around the bowel but never tints a healthy neighbour."""
    d = _d(segs)
    return _stroke(d, RED["glow"], w + 6.5, ' opacity=".22"') + _stroke(d, RED["glow"], w + 3.4, ' opacity=".3"')


def tube(segs, w, pal, kind="si"):
    """A tube along a centre line.  kind: si (smooth), colon (haustra), plain."""
    d = _d(segs)
    out = []
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


def rectum_tube(pal, cid):
    """The rectum, drawn after the colon so it hides the colon's round end cap: a run of discs along its
    centre line, cut flat exactly at the joint (clip `cid`, the half-plane past the colon's end, square to
    the colon's end tangent).  It starts at the colon's own outline and body widths and flares smoothly
    to its full width over its first 7 units, so the outline runs on without a step; the last disc is the
    round bottom.  The highlight stripe uses the colon stripe's offset and width, so the sheen runs on
    through the joint too."""
    (jx, jy), (cx1, cy1) = RECTUM[0][0], RECTUM[0][1]
    tl = math.hypot(cx1 - jx, cy1 - jy)
    tx, ty = (cx1 - jx) / tl, (cy1 - jy) / tl
    nx, ny = -ty, tx
    quad = [(jx + nx * 60, jy + ny * 60), (jx + nx * 60 + tx * 80, jy + ny * 60 + ty * 80),
            (jx - nx * 60 + tx * 80, jy - ny * 60 + ty * 80), (jx - nx * 60, jy - ny * 60)]
    total = length(RECTUM)
    pts = sample(RECTUM, 0.3)
    k = len(pts) - 1
    edge0, edge1 = (W_COLON + 1.9) / 2, (W_RECT + 2.0) / 2     # colon outline: solid 12.3, bulges 13.5 wide
    body0, body1 = (W_COLON - 0.75) / 2, W_RECT / 2            # colon body: solid 9.4, bulges 11.1 wide
    flare = lambda i, a, b: a + (b - a) * _smooth01(min(1.0, total * i / k / 7.0))
    edge = "".join(f'<circle cx="{p[0]:.2f}" cy="{p[1]:.2f}" r="{flare(i, edge0, edge1):.2f}"/>' for i, (p, _) in enumerate(pts))
    body = "".join(f'<circle cx="{p[0]:.2f}" cy="{p[1]:.2f}" r="{flare(i, body0, body1):.2f}"/>' for i, (p, _) in enumerate(pts))
    poly = " ".join(f"{x:.2f},{y:.2f}" for x, y in quad)
    return (f'<clipPath id="{cid}"><polygon points="{poly}"/></clipPath>'
            f'<g clip-path="url(#{cid})"><g fill="{pal["edge"]}">{edge}</g><g fill="{pal["body"]}">{body}</g></g>'
            f'<g transform="translate(-0.7,-0.9)">{_stroke(_d(RECTUM), pal["hi"], W_COLON * 0.26, " opacity=.85")}</g>')


def si_coil(segs, w=W_SI):
    """The small intestine as a pile of loops.  The coil is cut into loops about SI_LOOP
    long; each loop is drawn whole (soft shadow, outline, darker underside, body, one short
    highlight) on top of the loops before it, so wherever two loops touch, the later one
    tucks over the earlier one and shades it.  Seams sit inside a loop's outline: the body
    of each loop reaches back over the seam, so the tube reads as one."""
    total = length(segs)
    k = max(1, round(total / SI_LOOP))
    cuts = [i / k for i in range(k + 1)]
    back = lambda f, units: max(0.0, f - units / total)
    # one soft underlay for the whole coil fills the pinholes where three loops meet
    out = [_stroke(_d(segs), GI["si_under"], w + 3.6, ' opacity=".55"')]
    for a, b in zip(cuts, cuts[1:]):
        d = _d(sub(segs, a, b))
        d1 = _d(sub(segs, back(a, 0.6), b))     # outline and underside overlap the seam a little...
        d2 = _d(sub(segs, back(a, 1.8), b))     # ...and the body overlaps it further, so no seam line shows
        out.append(_stroke(d, GI["shadow"], w + 5.0, ' opacity=".10"', "butt"))
        out.append(_stroke(d, GI["shadow"], w + 3.4, ' opacity=".14"', "butt"))
        out.append(_stroke(d1, GI["si_edge"], w + 1.8, "", "butt"))
        out.append(_stroke(d1, GI["si_shade"], w - 0.1, "", "butt"))
        out.append(f'<g transform="translate(-0.35,-0.45)">{_stroke(d2, GI["si_body"], w - 1.5, "", "butt")}</g>')
        h = _d(sub(segs, a + (b - a) * 0.28, a + (b - a) * 0.66))
        out.append(f'<g transform="translate(-0.85,-1.1)">{_stroke(h, GI["si_hi"], 1.25, " opacity=.85")}</g>')
    return "".join(out)


def _smooth01(t):
    return t * t * (3 - 2 * t)


def _colon_x_at(y):
    """x of the ascending colon's centre line at height y (its first stretch, above the cecum)."""
    pts = [p for p, _ in sample(sub(COLON, 0.0, 0.08), 0.2)]
    return min(pts, key=lambda p: abs(p[1] - y))[0]


def cecum(mode, pal=GI):
    """The cecum: a short, wider stretch of colon, continuous with the ascending colon above
    it.  Drawn as a run of discs whose size grows toward the round bottom, in the colon's
    layers (outline with haustral bulges, body, haustral folds, highlight), and cut flat at
    the top where it meets the ascending colon, so the two join without a seam.  `mode`
    only keeps the clip id unique per figure."""
    (x0, y0), (x1, y1) = CEC_TOP, CEC_BOT
    n = 36
    c = [(x0 + (x1 - x0) * i / n, y0 + (y1 - y0) * i / n, W_COLON + (CEC_W - W_COLON) * _smooth01(i / n))
         for i in range(n + 1)]
    at = lambda s: c[min(n, max(0, round(s / (y1 - y0) * n)))]       # disc nearest s units below the top
    knobs = [at(s) for s in (2.0, 8.0) if s <= y1 - y0] + [c[-1]]
    cid = f"{U}-ceclip-{mode}"
    g = []
    for x, y, w in c:
        g.append(f'<circle cx="{x:.2f}" cy="{y:.2f}" r="{w / 2 + 0.65:.2f}" fill="{pal["edge"]}"/>')
    for x, y, w in knobs:
        g.append(f'<circle cx="{x:.2f}" cy="{y:.2f}" r="{(w + 2.5) / 2:.2f}" fill="{pal["edge"]}"/>')
    for x, y, w in c:
        g.append(f'<circle cx="{x:.2f}" cy="{y:.2f}" r="{w / 2 - 0.8:.2f}" fill="{pal["body"]}"/>')
    for x, y, w in knobs:
        g.append(f'<circle cx="{x:.2f}" cy="{y:.2f}" r="{(w + 0.1) / 2:.2f}" fill="{pal["body"]}"/>')
    for s in (5.0, 11.0):                                           # haustral folds between the bulges
        x, y, w = at(s)
        hw = (w - 2.2) / 2
        g.append(f'<path d="M{x - hw:.2f},{y:.2f} Q{x:.2f},{y + 1.3:.2f} {x + hw:.2f},{y:.2f}" fill="none" '
                 f'stroke="{pal["band"]}" stroke-width="0.95" stroke-linecap="round" opacity=".75"/>')
    xb, yb, wb = c[-1]
    # The highlight picks up exactly where the colon's own highlight stripe is cut off by the cecum's top
    # (the colon draws its stripe along the centre line shifted (-0.7, -0.9), at width W_COLON * 0.26),
    # then curves gently outward over the pouch: no kink at the seam (front recheck 2026-11-03).
    hx = _colon_x_at(y0 + 0.9) - 0.7
    g.append(f'<path d="M{hx:.2f},{y0:.2f} C{hx - 0.15:.2f},{y0 + 4.5:.2f} {xb - 4.6:.2f},{yb - 3:.2f} {xb - 3.2:.2f},{yb + 2.6:.2f}" '
             f'fill="none" stroke="{pal["hi"]}" stroke-width="{W_COLON * 0.26:.2f}" stroke-linecap="round" opacity=".85"/>')
    return (f'<clipPath id="{cid}"><rect x="-80" y="{y0:.2f}" width="160" height="80"/></clipPath>'
            f'<g clip-path="url(#{cid})">{"".join(g)}</g>')


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


def cavity_d():
    """The belly space inside the colon frame, behind the coil: a muted rose, so the gaps between
    loops read as depth instead of holes.  Its outline runs only along centre lines that tubes
    cover (the colon all the way round, the rectum's top, the terminal ileum back to the cecum),
    so no edge of it can show."""
    pts = [p for p, _ in sample(COLON, 1.0)]
    pts += [(-5.0, 223.0), (-7.6, 221.0)]
    ti = [p for p, _ in sample(sub(SI, frac_at(SI, -30.0), 1.0), 1.0)]
    pts += ti
    return "M" + " L".join(f"{x:.2f},{y:.2f}" for x, y in pts) + " Z"


def red_parts(mode):
    """[(centre line, tube width)] of every inflamed stretch in one figure."""
    if mode == "uc":
        return [(sub(COLON, *UC_COLON), W_COLON), (RECTUM, W_RECT)]
    return [(sub(COLON, a, b), W_COLON) for a, b in CD_COLON] + [(sub(SI, *CD_SI), W_SI + 1.4)]


def figure(mode, x, y, s=1.0):
    """One human figure with the whole digestive tract.  mode: 'uc' or 'cd'.  Both modes
    draw the identical body and anatomy; only the red differs.  Layers, back to front:
    skin; esophagus; duodenum (shaded where it goes behind the colon); the red halos;
    the small intestine coil; an inflamed terminal ileum (Crohn's); the colon's soft contact
    shadow; colon and its red stretches; rectum (after the colon, so it hides the colon's
    round end cap); cecum; stomach, which lies in front of the transverse colon in a real
    belly."""
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
    g.append(f'<g mask="url(#{U}-esofade)">{tube(ESO, W_ESO, {"edge": GI["edge"], "body": GI["st_top"], "hi": GI["hi"]})}</g>')
    g.append(tube(DUO, W_DUO, {"edge": GI["edge"], "body": GI["st_bot"], "hi": GI["hi"]}))
    g.append(_stroke(_d(DUO), f"url(#{U}-duo)", W_DUO + 0.2))          # darkens as it dives behind the colon
    g.append(f'<path d="{cavity_d()}" fill="{GI["cavity"]}" opacity=".55"/>')
    reds = red_parts(mode)
    g += [glow(segs, w) for segs, w in reds]
    g.append(si_coil(SI))
    if mode == "cd":   # an inflamed ileum is swollen, so it is drawn a little thicker
        g.append(tube(sub(SI, *CD_SI), W_SI + 1.4, RED))
    # the colon, rectum and cecum sit a little in front of the coil: a soft contact shadow
    for segs, w in ((COLON, W_COLON), (RECTUM, W_RECT)):
        g.append(_stroke(_d(segs), GI["shadow"], w + 4.6, ' opacity=".09"') + _stroke(_d(segs), GI["shadow"], w + 2.8, ' opacity=".11"'))
    g.append(tube(COLON, W_COLON, GI, "colon"))
    for segs, w in reds:
        if w == W_COLON:
            g.append(tube(segs, W_COLON, RED, "colon"))
    g.append(rectum_tube(RED if mode == "uc" else GI, f"{k}-rclip"))     # after the colon: covers its end cap
    g.append(cecum(mode))
    g.append(stomach())
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
            f'<linearGradient id="{U}-duo" gradientUnits="userSpaceOnUse" x1="-16.6" y1="154.4" x2="-20.3" y2="160.6">'
            f'<stop offset="0" stop-color="{GI["shadow"]}" stop-opacity="0"/>'
            f'<stop offset="1" stop-color="{GI["shadow"]}" stop-opacity=".55"/></linearGradient>'
            # thighs fade into the page instead of being chopped off
            f'<linearGradient id="{U}-fadeg" gradientUnits="userSpaceOnUse" x1="0" y1="247" x2="0" y2="272">'
            '<stop offset="0" stop-color="#fff"/><stop offset="1" stop-color="#000"/></linearGradient>'
            f'<mask id="{U}-fade" maskUnits="userSpaceOnUse" x="-80" y="-10" width="160" height="320">'
            f'<rect x="-80" y="-10" width="160" height="320" fill="url(#{U}-fadeg)"/></mask>'
            f'<linearGradient id="{U}-esog" gradientUnits="userSpaceOnUse" x1="0" y1="60" x2="0" y2="76">'
            '<stop offset="0" stop-color="#000"/><stop offset="1" stop-color="#fff"/></linearGradient>'
            f'<mask id="{U}-esofade" maskUnits="userSpaceOnUse" x="-80" y="-10" width="160" height="320">'
            f'<rect x="-80" y="-10" width="160" height="320" fill="url(#{U}-esog)"/></mask>'
            "</defs>")


# ----------------------------------------------------------------------------- QA helpers
def _inside_fn(poly):
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
    return inside


def check_inside(margin=3.0):
    """Every tube edge (centre line +/- half width + outline + margin) must sit inside
    the body polygon.  Returns a list of (organ, x, y) points that fail; [] means clean.
    Run by hand while editing:
      cd build && python3 -c 'import conditions.ibd as m; print(m.check_inside(), m.check_leaders())'"""
    inside = _inside_fn(body_polygon())
    bad = []
    for name, segs, w, mg in [("esophagus", sub(ESO, 0.12, 1), W_ESO, margin), ("duodenum", DUO, W_DUO, margin),
                              ("small intestine", SI, W_SI, margin), ("colon", COLON, W_COLON + 1.3, margin),
                              ("rectum", RECTUM, W_RECT, margin + 3), ("red glow", COLON, W_COLON + 6.5, 0.5),
                              ("rectum glow", RECTUM, W_RECT + 6.5, 0.5), ("ileum glow", SI, W_SI + 1.4 + 6.5, 0.5)]:
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
    (x0, y0), (x1, y1) = CEC_TOP, CEC_BOT
    for a in range(0, 360, 10):                          # the cecum's bottom disc and its bulges
        r = (CEC_W + 2.5) / 2 + 1 + margin
        qx, qy = x1 + r * math.cos(math.radians(a)), y1 + r * math.sin(math.radians(a))
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
AW, AH = 760, 280
LAB_X = 70.0     # labels end (left figure) or start (right figure) this far from the midline
NAME, GLOSS = 11.6, 10.0                 # label sizes (8.4 pt and 7.3 pt printed)

SI_DOT_L = nearest(SI, (-25.2, 205.0))   # "Small intestine" lands on a coil, never in a gap
SI_DOT_R = nearest(SI, (24.4, 206.5))

# Anatomy labels, identical on both figures and mirrored to the outer side of each.
# Leaders are polylines in figure-local units: they start beside the text and end on the dot;
# "via" points route a leader around an organ.  The Crohn's terminal-ileum callout cannot come
# from the outer side without crossing the whole belly, so it sits in the clear band under
# the KEY and reaches the ileum through the gap between the cecum and the rectum (art_ibd()).
TI_VIA = (-28.5, 242.8)   # both "End of the small intestine" leaders pass under the cecum through this point
LABELS = [
    # both Stomach dots sit inside the stomach body (the right one was on its outline, half on skin)
    {"name": ["Stomach"], "y": 143.0, "L": [(15.0, 142.0)], "R": [(27.0, 141.0)]},
    {"name": ["Colon"], "gloss": "large intestine", "y": 178.0, "L": [(-40.4, 180.0)], "R": [(42.6, 180.0)]},
    {"name": ["Small intestine"], "y": 212.0, "L": [SI_DOT_L], "R": [SI_DOT_R]},
    {"name": ["End of the", "small intestine"], "y": 232.0, "from": 1,          # leader leaves the 2nd line
     "L": [TI_VIA, TI_DOT], "R": None},                                         # routed under the cecum
    {"name": ["Rectum"], "y": 268.0, "L": [(-3.0, 239.6)], "R": [(3.0, 239.6)]},   # low on the rectum: 6 units clear of the TI leader
]
# Crohn's terminal-ileum callout: right-aligned text end and first baseline (art units).  It shares the
# Ulcerative colitis callout's baseline (FY + 232) and its offset from the figure (70 units left of the
# midline, so both texts end 15 units short of the hips), and its leader takes the same route under the
# cecum (TI_VIA), so the two callouts are an exact pair.  The KEY above it ends at art y 212.
CD_TI = {"x": FX2 - LAB_X, "y": FY + 232.0, "via": TI_VIA}


def leader(pts):
    d = "M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in pts)
    ax, ay = pts[-1]
    return (f'<path d="{d}" stroke="#fff" stroke-width="3.2" opacity=".85" fill="none" stroke-linecap="round" stroke-linejoin="round"/>'
            f'<path d="{d}" stroke="{LEAD}" stroke-width="1.1" fill="none" stroke-linejoin="round"/>'
            f'<circle cx="{ax:.1f}" cy="{ay:.1f}" r="2.3" fill="{INK}" stroke="#fff" stroke-width="1"/>')


def leaders():
    """Every leader on the art in art units: [(figure mode, label, [points])]."""
    out = []
    for mode, side, fx in (("uc", -1, FX1), ("cd", 1, FX2)):
        for lab in LABELS:
            route = lab["L"] if side < 0 else lab["R"]
            if route is None:
                continue
            y = FY + (lab["y"] + lab.get("from", 0) * NAME * 1.22) * FS
            xt = fx + side * LAB_X
            start = (xt - side * 4.5, y - 4.2)
            out.append((mode, lab["name"][-1], [start] + [(fx + px * FS, FY + py * FS) for px, py in route]))
    y2 = CD_TI["y"] + NAME * 1.22
    out.append(("cd", "small intestine", [(CD_TI["x"] + 4.5, y2 - 4.2)] +
                [(FX2 + px * FS, FY + py * FS) for px, py in (CD_TI["via"], TI_DOT)]))
    return out


def labels():
    o = [leader(pts) for _, _, pts in leaders()]
    for side, fx in ((-1, FX1), (1, FX2)):
        anchor = "end" if side < 0 else "start"
        xt = fx + side * LAB_X
        for lab in LABELS:
            if (lab["L"] if side < 0 else lab["R"]) is None:
                continue
            o.append(T(xt, FY + lab["y"] * FS, lab["name"], NAME, 800, INK, anchor))
            if lab.get("gloss"):
                o.append(T(xt, FY + lab["y"] * FS + 12.6, lab["gloss"], GLOSS, 500, INK_SOFT, anchor))
    o.append(T(CD_TI["x"], CD_TI["y"], ["End of the", "small intestine"], NAME, 800, INK, "end"))
    return "".join(o)


def check_leaders(halo=1.6, land=10.5):
    """QA: no leader may run over red bowel or its glow, and no two leaders may cross.
    A leader whose dot is meant to sit on a red stretch (Rectum on UC, Colon or the
    terminal ileum on Crohn's) may enter the red only within `land` units of its dot.
    Returns a list of problems; [] means clean."""
    bad = []
    reds = {}
    for mode, fx in (("uc", FX1), ("cd", FX2)):
        pts = []
        for segs, w in red_parts(mode):
            r = (w + 6.5) / 2 + halo
            pts += [((fx + p[0] * FS, FY + p[1] * FS), r) for p, _ in sample(segs, 0.6)]
        reds[mode] = pts
    lines = leaders()
    for mode, name, pts in lines:
        end = pts[-1]
        for (ax, ay), (bx, by) in zip(pts, pts[1:]):
            n = max(2, int(math.hypot(bx - ax, by - ay) / 0.5))
            for k in range(n + 1):
                x, y = ax + (bx - ax) * k / n, ay + (by - ay) * k / n
                if math.hypot(x - end[0], y - end[1]) < land:
                    continue
                for (cx, cy), r in reds[mode]:
                    if math.hypot(x - cx, y - cy) < r:
                        bad.append((mode, name, "over red", round(x, 1), round(y, 1)))
                        break

    def cross(p1, p2, p3, p4):
        d = lambda a, b, c: (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])
        return (d(p3, p4, p1) * d(p3, p4, p2) < 0) and (d(p1, p2, p3) * d(p1, p2, p4) < 0)
    for i in range(len(lines)):
        for j in range(i + 1, len(lines)):
            for a, b in zip(lines[i][2], lines[i][2][1:]):
                for c, e in zip(lines[j][2], lines[j][2][1:]):
                    if cross(a, b, c, e):
                        bad.append((lines[i][0], lines[i][1], "crosses", lines[j][1]))
    return bad


def check_text(margin=6.0):
    """QA: every label's text box (Inter, measured with PIL when it is installed) sits inside
    the viewBox with `margin` units to spare.  Returns problems; [] means clean."""
    try:
        from PIL import ImageFont
        font = ImageFont.truetype("/usr/share/fonts/opentype/inter/Inter-ExtraBold.otf", 1160)
    except Exception:
        return ["(PIL or Inter not available: text not measured)"]
    bad = []
    for side, fx in ((-1, FX1), (1, FX2)):
        xt = fx + side * LAB_X
        for lab in LABELS:
            if (lab["L"] if side < 0 else lab["R"]) is None:
                continue
            for ln in lab["name"]:
                w = font.getlength(ln) / 100
                x0, x1 = (xt - w, xt) if side < 0 else (xt, xt + w)
                if x0 < margin or x1 > AW - margin:
                    bad.append((ln, round(x0, 1), round(x1, 1)))
    return bad


def key_swatch(red):
    """A short stretch of colon drawn exactly like the art."""
    segs = [line((-13, 0), (13, 0))]
    return (glow(segs, 9.0) if red else "") + tube(segs, 9.0, RED if red else GI, "colon")


def key_svg(cx, y):
    w, h = 166, 78
    x = cx - w / 2
    rows = [(True, "Inflamed", "red, swollen, sore"), (False, "Healthy bowel", "no inflammation")]
    o = [f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="9" fill="#fff" stroke="#C9D6D5" stroke-width="1.3"/>',
         f'<rect x="{cx - 21}" y="{y - 7}" width="42" height="14" rx="7" fill="#fff"/>',
         T(cx, y + 4, "KEY", 10, 800, "#0D5A56", "middle", ls=1.8)]
    for i, (red, a, b) in enumerate(rows):
        ry = y + 26 + i * 30
        o.append(f'<g transform="translate({x + 30},{ry})">{key_swatch(red)}</g>')
        o.append(T(x + 54, ry - 1.4, a, 11.2, 800, INK))
        o.append(T(x + 54, ry + 10.6, b, 9.8, 500, INK_SOFT))
    return "".join(o)


def art_ibd(t):
    o = [defs_svg(), figure("uc", FX1, FY, FS), figure("cd", FX2, FY, FS), labels()]
    # the centre line: VS, then the key.  Raised so the key box ends at art y 212, well above the
    # Crohn's callout that shares the Ulcerative colitis callout's baseline (y 236).
    o.append(f'<circle cx="380" cy="{FY + 78}" r="33" fill="#fff" stroke="{t["c1"]}" stroke-width="3"/>')
    o.append(T(380, FY + 89, "VS", 30, 900, t["deep"], "middle"))
    o.append(key_svg(380, FY + 130))
    return svg(AW, AH, "".join(o), "Two identical human figures with the whole digestive tract inside. In ulcerative "
               "colitis, one unbroken stretch of the colon is red, from the rectum up. In Crohn’s disease, separate red "
               "patches sit at the end of the small intestine and in the colon, with healthy bowel between them.")


# ----------------------------------------------------------------------------- front blocks
CAPTIONS = [("Ulcerative colitis",     # [ACGUC]
             "One unbroken stretch of inflammation that starts in the rectum and climbs the colon."),
            ("Crohn’s disease",        # [ACGCD]
             "Patchy inflammation with healthy gaps, most often at the end of the small intestine.")]

COMPARE = [   # (row, ulcerative colitis, Crohn's disease)
    ("Where", "Colon and rectum only",                                          # [ACGUC]
     "Anywhere from mouth to anus, most often the end of the small intestine"),  # [ACGCD]
    ("Depth", "The inner lining of the bowel", "Can go through the whole bowel wall"),   # [ACGUC] [ACGCD]
    # a fistula is a tunnel from the bowel to the skin or another organ (front recheck: "through the bowel wall"
    # repeated the Depth row and undersold it); "from the bowel" is left to the row, so the cell stays one line
    ("Fistulas", "Uncommon", "Can form: tunnels to the skin or another organ"),   # [CCUK] [ACGCD]
    ("Pain", "Often the left side of the belly", "Often the lower right belly"),         # [CCF-T]
    ("Bleeding", "Common, with bowel movements", "Less common"),                         # [ACGUC] [ACGCD]
]

# What can stir up a flare: [CCF] missed doses, NSAIDs, antibiotics, smoking, stress;
# [ANA13] poor sleep (Crohn's only, so it is labelled); [ACGCD] smoking worsens Crohn's
# (it is not a UC trigger, so it is labelled); gut infections such as C. difficile [ACGUC];
# trigger foods differ by person.  NSAIDs wear the pill bottle, the same icon the back
# page's "Ask about NSAIDs" uses; antibiotics wear the capsule.
TRIGGERS = [("headache", "Stress"), ("moon", "Poor sleep (Crohn’s)"), ("sensitive", "Trigger foods"),
            ("rx", "NSAID pain relievers"), ("capsule", "Antibiotics"), ("germ", "Gut infections"),
            ("smoke", "Smoking (Crohn’s)"), ("calendar", "Missed medicine")]

# Nutrients that often run low [WEI15] [HWA12]; vitamin D's reason [KIM20]
NUTRIENTS = [("Fe", "Iron", "lost with bleeding"),
             ("D", "Vitamin D", "less sun and poor absorption"),
             ("B12", "Vitamin B12", "absorbed at the end of the small intestine"),
             ("B9", "Folate", "lowered by some IBD medicines"),
             ("Zn", "Zinc", "lost with diarrhea")]

# Line icons this sheet draws itself (64x64, stroked with currentColor; _ic() prefers these over kit.ICONS).
# Front recheck 2026-11-03: the capsule now fills the same footprint as its neighbours (kit's is about half
# their size), two-tone so it reads as a pill; the germ is a round-bodied cell with short pili and one wavy
# flagellum, so its outline no longer echoes the capsule beside it (the old rod read as a wrapped sweet).
MY_ICONS = {
    "capsule": '<g transform="translate(32 32) rotate(-45)">'
               '<path d="M0 -9H-16a9 9 0 0 0 0 18H0z" fill="currentColor" stroke="none" opacity=".35"/>'
               '<path d="M-16 -9H16a9 9 0 0 1 0 18H-16a9 9 0 0 1 0-18z"/><path d="M0 -9V9"/></g>',
    "germ": '<ellipse cx="27.5" cy="35" rx="15.5" ry="11" transform="rotate(-22 27.5 35)"/>'
            '<path d="M29.4 47.5L30.3 51.9M18.4 47.3L16.3 51.3M11.7 41.4L7.6 43.1M11.9 33.6L7.5 32.6M17.7 26.3L14.7 22.9'
            'M27.1 22.2L26.5 17.7M36.6 22.7L38.7 18.7M38.4 42.8L41.7 45.9"/>'
            '<path d="M42.9 31.4c3.2-1.6 4.6 2.2 7.8 0.4s3-5 6.2-6.4 3.6 0.8 6.4-1.6"/>'
            '<circle cx="23" cy="36.5" r="2.1" fill="currentColor" stroke="none"/>'
            '<circle cx="32" cy="32.5" r="2.1" fill="currentColor" stroke="none"/>',
}


def _ic(name, size, sw=3.0):
    body = MY_ICONS.get(name) or ICONS[name]
    return (f'<svg class="ic" viewBox="0 0 64 64" style="width:{size};height:{size}" fill="none" stroke="currentColor" '
            f'stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{body}</svg>')


def front(t, ed):
    heads = "".join(f"<div><b>{h}</b></div>" for h, _ in CAPTIONS)
    caps = "".join(f"<div><p>{c}</p></div>" for _, c in CAPTIONS)
    chips = "".join(f"<span>{h}</span>" for h, _ in CAPTIONS)
    rows = "".join(f'<div class="{U}-row"><div>{a}</div><span>{k}</span><div>{b}</div></div>' for k, a, b in COMPARE)
    trig = "".join(f"<div>{_ic(ic, '0.23in', 3.2)}<span>{lab}</span></div>" for ic, lab in TRIGGERS)
    coins = "".join(f'<div><b>{s}</b><em>{n}</em><span>{why}</span></div>' for s, n, why in NUTRIENTS)
    return (f'<div class="{U}-f">'
            f'<div class="{U}-h {U}-kick">Where the inflammation is</div>'
            f'<div class="{U}-heads">{heads}</div>'
            f'<div class="art {U}-art">{art_ibd(t)}</div>'
            f'<div class="{U}-caps">{caps}</div>'
            f'<div class="{U}-cmp"><div class="{U}-chips">{chips}</div>{rows}</div>'
            f'<div class="{U}-h">What can stir up a flare</div><div class="{U}-trig">{trig}</div>'
            f'<div class="{U}-h">Nutrients that often run low in IBD</div>'
            f'<div class="{U}-nut"><div class="{U}-stat"><b>More than half</b><p>of people with IBD run low on at '
            'least one vitamin or mineral, more often in Crohn’s and during flares.</p></div>'
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
/* room between each heading's teal bar and the head crown under it (it sat on the head like a hat) */
.ibx-heads{margin-bottom:0.05in}
.ibx-heads b{font:900 13.5pt Merriweather,Georgia,serif;color:var(--deep);letter-spacing:-.005em}
.ibx-heads div{display:flex;flex-direction:column;align-items:center}
.ibx-heads div::after{content:"";width:0.42in;height:3px;border-radius:2px;background:var(--c1);margin-top:3px}
.ibx-caps p{margin:1px auto 0;max-width:3.0in;font-size:8.6pt;line-height:1.25;color:#2B3236;text-wrap:balance}
.ibx-cmp{margin-top:0.06in}
.ibx-chips{display:grid;grid-template-columns:1fr 1fr;justify-items:center;padding-bottom:2px;border-bottom:1px solid #D5E4E2}
.ibx-chips span{font:800 7.4pt Inter,sans-serif;color:var(--deep);background:var(--soft);border-radius:99px;padding:1.5px 10px 1.5px}
.ibx-row{position:relative;display:grid;grid-template-columns:1fr 1fr;border-bottom:1px solid #D5E4E2}
.ibx-row:nth-child(odd){background:var(--tint)}
.ibx-row>div{padding:1.5px 0.54in;text-align:center;font-size:8.4pt;line-height:1.22;color:#2B3236;
  display:flex;align-items:center;justify-content:center;min-height:0.19in;text-wrap:balance}
.ibx-row>span{position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);width:0.9in;text-align:center;
  font:800 7.1pt Inter,sans-serif;letter-spacing:.12em;text-transform:uppercase;color:#fff;background:var(--c1);
  border-radius:99px;padding:1.6px 0}
.ibx-h{font:800 7.5pt Inter,sans-serif;letter-spacing:.14em;text-transform:uppercase;color:var(--deep);
  text-align:center;margin:0.065in 0 0.032in}
.ibx-kick{margin:0 0 0.03in}
/* deep to c1: white 7.2 pt caps keep 4.6:1 or better across the band (c1 to c2 fell to 3.0:1 at the light end) */
.ibx-trig{display:grid;grid-template-columns:repeat(8,1fr);background:linear-gradient(90deg,var(--deep),var(--c1));
  border-radius:6px;padding:0.035in 0.04in}
.ibx-trig>div{display:flex;flex-direction:column;align-items:center;text-align:center;color:#fff;padding:0 2px}
.ibx-trig span{font:800 7.2pt Inter,sans-serif;letter-spacing:.05em;text-transform:uppercase;line-height:1.15;margin-top:2px}
.ibx-nut{display:grid;grid-template-columns:1.62in 1fr;gap:0.12in;align-items:center;
  background:var(--soft);border-radius:10px;padding:0.05in 0.1in 0.05in 0.14in}
.ibx-stat b{display:block;font:900 15pt/1.05 Merriweather,Georgia,serif;color:var(--c1)}
.ibx-stat p{margin:3px 0 0;font-size:8pt;line-height:1.3;color:#2B3236}
.ibx-dep{background:#fff;border-radius:8px;padding:0.045in 0.05in 0.035in}
.ibx-coins{display:grid;grid-template-columns:repeat(5,1fr);gap:0.05in}
.ibx-ask{text-align:center;font-size:7.6pt;color:#3F4A50;margin-top:2px}
.ibx-coins>div{display:flex;flex-direction:column;align-items:center;text-align:center}
.ibx-coins b{width:0.32in;height:0.32in;border-radius:50%;background:var(--c1);color:#fff;display:flex;align-items:center;
  justify-content:center;font:800 9.4pt Inter,sans-serif;box-shadow:0 0 0 2px #fff,0 0 0 3.2px #9FD0CB}
.ibx-coins em{font-style:normal;font:800 7.7pt Inter,sans-serif;color:#1F2A2E;margin-top:3px}
.ibx-coins span{font-size:7.1pt;line-height:1.15;color:#3F4A50}
.ibx-scope{margin:0.065in auto 0;text-align:center;font-size:8.4pt;line-height:1.3;color:#2B3236;background:var(--soft);
  border-radius:6px;padding:0.04in 0.16in;width:100%}
.ibx-scope b{color:var(--deep)}
/* ---- this sheet's back page only (the page holding the .ibx-back marker in the lifestyle title) */
/* the medicine line under the band title: one quiet line, not a second heading */
.sheet.back:has(.ibx-back) .band h2 small{font:600 8.6pt Inter,sans-serif;letter-spacing:0;color:#FFE6D4;margin-top:3px}
/* every header keeps a little band for the START HERE badge, so it never touches the title under it, and all
   five are one height (two of the sub-lines wrap), so the photos and names start on one line */
.sheet.back:has(.ibx-back) .col .need{padding-top:10px;min-height:0.56in}
/* a little less air above the band title and the Nutrient Solutions title, so the footer keeps its margin
   (the same two tweaks as the Intestinal Permeability sheet) */
.sheet.back:has(.ibx-back) .band{padding-top:0.24in!important}
.sheet.back:has(.ibx-back) .ns-title{margin-top:0.1in}
/* the daily rhythm gets the wider half: morning and evening hold three and four products, bedtime one */
.sheet.back:has(.ibx-back) .duo{grid-template-columns:1.5fr 1fr}
.sheet.back:has(.ibx-back) .rhythm{grid-template-columns:1.3fr 1.3fr .8fr}
"""


def _qa():
    """Runs at import, so every build says out loud when an edit breaks the art: an organ
    over the body outline, a leader over red, crossing leaders, or a label off the edge.
    It warns instead of raising, because a failed import would silently drop the sheet
    from a full build."""
    import sys
    probs = check_inside()[:4] + check_leaders()[:4] + [p for p in check_text() if not str(p).startswith("(")][:4]
    if probs:
        print(f"WARNING: ibd.py art QA failed: {probs}", file=sys.stderr)


_qa()


# ----------------------------------------------------------------------------- the sheet
SHEET = {
    "slug": "ibd", "code": "ND-GI-103", "order": 3, "theme": "teal", "series": "Gut Health Series",
    # same left-to-right order as the two figures
    "title": "Inflammatory Bowel Disease", "sub": "Ulcerative colitis and Crohn’s disease",
    # "More than 2 million": [LEW23] 2.39 million diagnosed (claims data); [NCHS26] 1.6% of adults self-report,
    # so 2 million is the floor of both.  Shared symptoms; flares and quiet stretches (remission): [ACGUC] [ACGCD].
    "intro": ("Inflammatory bowel disease (IBD) is a long-term condition in which the immune system keeps part of the digestive "
              "tract inflamed. <b>More than 2 million Americans</b> live with it. The two main types, <b>ulcerative colitis</b> "
              "and <b>Crohn’s disease</b>, share belly pain, urgent diarrhea, tiredness and weight loss, with flares that come "
              "and go between quieter stretches. A gastroenterologist leads the care. Food, lifestyle and nutrient support "
              "work alongside that care, never instead of it."),
    "front": front,
    "css": CSS,
    # ------------------------------------------------------------------------- back page
    # NutriDyn's IBD program is the 5R with its IBD switch [ND584] plus the autoimmune core [AUTO23] (sources in
    # the module docstring).  The five columns are the five program products that fill the
    # competitor's five nutrient slots: high-potency probiotic -> UltraBiotic Defense; complete turmeric matrix
    # -> Dynamic Inflam-Eze; vitamin D3 -> D3 5000 with K2; L-glutamine + DGL + aloe -> GI Restore (ND584 takes
    # GI Integrity out of an inflamed gut, so its DGL formula is not on this sheet); serum-derived bovine
    # immunoglobulin -> GI Defend.  PRM Resolve (autoimmune core) fills no competitor slot, so it stays off.
    # Left to right in the order they start: the days 1 to 10 shake (Inflam-Eze + GI Defend), the shake that
    # replaces it from day 11 (GI Restore), then the two all-along pills.  Label facts, sources and photo notes:
    # build/products.d/ibd.json.  The span marks this back page for the scoped CSS (.sheet.back:has(.ibx-back)).
    "back": {
        "life_title": f'Lifestyle Modifications<span class="{U}-back"></span>',
        # the pairing every NutriDyn IBD page carries, said once where the back page starts
        "life_sub": ("Keep every prescribed IBD medicine; your gastroenterologist leads. "
                     "These steps and nutrients work alongside that care."),
        "style": "hex",
        "life": [
            # [AGA24] BPA 1: a Mediterranean diet "rich in a variety of fresh fruits and vegetables, monounsaturated
            # fats ... and lean proteins and low in ultraprocessed foods, added sugar, and salt"; [AUTO23] "an
            # anti-inflammatory Mediterranean-type diet"; [BLAST26] wild-caught fish, olive, flax and walnut oils
            # daily, 5 to 7 vegetable servings; [ND584] REMOVE: sugar, artificial sweeteners, processed foods.
            ("fish", "Mediterranean", "Fish, olive oil and lots of vegetables; less sugar and processed food."),
            # [ND584] steps 1 and 2: remove gluten, dairy and soy (with sugar and alcohol) on days 1 to 10, then
            # bring back one category at a time, 1 serving a day for 3 days.  Kept to the 10-day pause with
            # reintroduction: long exclusion diets are not advised in IBD [ESPEN17].
            ("sensitive", "Spot triggers", "Skip gluten, dairy and soy for 10 days, then add back one at a time."),
            # [AGA24] BPA 2 (cook or process produce to a soft texture if strictures make raw produce hard to
            # tolerate) and BPA 9 (screen for malnutrition); [ND584] "Peel, lightly cook, or puree produce if you are
            # fiber sensitive" and "3 small meals and 2 ... snacks"; [ESPEN17] protein needs rise in some patients.
            ("plate", "Flare days", "Small meals with protein. Cook or blend produce if raw hurts."),
            # [ND584] "Stress causes digestive issues"; "Block out just 10 minutes daily to focus on relaxation
            # techniques."  [CCF] stress is a common flare trigger.
            ("breath", "Lower stress", "Take 10 calm minutes a day. Stress can stir up a flare."),
            # [ND584] 30 minutes of cardio 5 days a week and daily light stretching; "most days" keeps it gentle.
            ("walk", "Move gently", "Walk, swim or stretch most days."),
            # [CCF] NSAIDs (ibuprofen, naproxen) can trigger flares.  Antibiotics are on the front's flare band.
            ("rx", "Skip NSAIDs", "Ibuprofen and naproxen can trigger flares. Ask what to take instead."),
        ],
        "cols": [
            {"p": "ibd_inflam_eze", "need": "Inflammatory balance", "needsub": "turmeric shake, days 1 to 10", "start": True,
             "bullets": ["Supports a healthy inflammatory response", "Turmeric, quercetin and ginger in a protein shake"],
             "dose": "dose_from_db"},
            {"p": "ibd_gi_defend", "need": "Gut barrier support", "needsub": "antibody proteins from cow serum",
             "bullets": ["Helps bind microbial toxins in the gut", "Supports gut barrier function"],
             "dose": "dose_from_db"},
            {"p": "ibd_gi_restore", "need": "Gut lining support", "needsub": "L&#8209;glutamine and aloe shake, from day 11",
             "bullets": ["Supports the gut lining and its mucus layer", "Feeds your friendly gut bacteria"],
             "dose": "dose_from_db"},
            {"p": "ibd_ultrabiotic_defense", "need": "Microbiome balance", "needsub": "3 strains, with S.&nbsp;boulardii",
             "bullets": ["Supports a balanced gut microbiome", "Take it 2 hours away from antibiotics"],
             "dose": "dose_from_db"},
            {"p": "ibd_d3_5000_k2", "need": "Vitamin D support", "needsub": "D3 with K2",
             "bullets": ["Supports healthy vitamin D levels", "Supports bone and immune health"],
             "dose": "dose_from_db"},
        ],
        # Three medicine-and-nutrient notes per edition: the pharmacist checks interactions and depletions, the
        # provider orders labs, refers and adjusts.
        "rx": {
            "pharmacy": [
                # Glucocorticoids cut intestinal calcium absorption and thin bone; calcium + vitamin D for long-term
                # users [ACR17]; steroid users had twice the odds of 25(OH)D under 10 ng/mL [SKV11].  Budesonide is
                # gentler on bone than prednisone but long courses still count.
                "<b>Steroids</b> (prednisone, budesonide) can thin bones: they cut calcium absorption and are "
                "linked to low vitamin D. Ask about bone health.",
                # [HWA12]: sulfasalazine and methotrexate are folate antagonists (folate is on the front's coins).
                "<b>Sulfasalazine and methotrexate</b> lower folate. Ask {who} whether you need folic acid.",
                # [ODSK] vitamin K can blunt warfarin (D3 5000 with K2: 60 mcg K2 + 15 mcg K1 a softgel);
                # [DRUGS-C] curcumin with warfarin rated a moderate interaction (bleeding).
                "<b>On warfarin or another blood thinner?</b> The vitamin K in D3 5000 with K2 can weaken warfarin, "
                "and the turmeric in Dynamic Inflam-Eze may add to bleeding. Ask {who} first.",
            ],
            "practitioner": [
                # [AGA24] BPA 10: monitor every IBD patient for vitamin D and iron deficiency, and B12 with ileal
                # disease or resection; [AUTO23] know the vitamin D level, dose higher only if it is very low.
                "<b>Labs first.</b> {Who} may check vitamin D, iron, B12 and folate, then set your vitamin D dose "
                "to your level.",
                # [ACR17] calcium and vitamin D, and a fracture-risk check, for long-term glucocorticoid users; [SKV11].
                "<b>On steroids?</b> They cut calcium absorption and thin bones: {who} may check your bones and your "
                "calcium and vitamin D.",
                # [ACGUC] [ACGCD]: severe or worsening disease is managed by the gastroenterologist.
                "<b>Fever, heavy bleeding or a flare that won’t settle?</b> {Who} sends you back to your "
                "gastroenterologist right away.",
            ],
        },
    },
}
