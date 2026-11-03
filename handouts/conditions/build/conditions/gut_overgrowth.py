"""Gut Overgrowth: Yeast, Parasites and SIBO (ND-GI-104), Gut Health Series.

Self-contained sheet module: the front art, the front copy and the back data all live here.  Shared
helpers come from svgkit (T, svg) and kit (icon).  Every SVG id and CSS class starts with "gov" because
all sheets share one document in the bundle PDFs.

This is the REMOVE step of NutriDyn's 5R gut plan.  The Intestinal Permeability sheet (ND-GI-101) covers
Repair and Rebalance; the 5R ribbon on the front points there.  The ribbon uses NutriDyn's own names and
order from ND584 (Remove, Replace, Reinoculate, Repair, Retain), not the generic "Rebalance".

FRONT, top to bottom
  intro -> art: one front-view digestive tract in the centre (esophagus, stomach, the whole small
  intestine from duodenum to ileum, the colon with its haustra from cecum to rectum, appendix), with
  lens-and-beam zooms into the small intestine and the colon.  Left column BALANCED, right column
  OVERGROWTH; small intestine on top, colon below, so the four circles compare at a glance.  Organ
  names sit on the circle rims; each circle has a one-line caption in clear space ->
  KEY (every symbol, same drawing code as the art) -> three kinds of overgrowth (SIBO, yeast,
  parasites: clues, risks, which test) -> breath test "know your numbers" strip (consensus cut-offs and a
  write-in box) -> red-flag line -> the 5R ribbon with Remove marked "this sheet".
Testing is always the practitioner's: the front says "your provider" in both editions (never {who}).
Anatomy notes: villi are drawn only in the small intestine; the colon lining is flat with crypts (the
colon has no villi).  The stomach sits on the viewer's right (the patient's left), the cecum and
appendix on the viewer's lower left, the splenic flexure higher than the hepatic flexure, and the
transverse colon passes in front of the duodenum.

SOURCES (each fact on the page carries one of these tags in a comment next to it)
  [ACG20]   Pimentel M, Saad RJ, Long MD, Rao SSC. ACG Clinical Guideline: Small Intestinal Bacterial
            Overgrowth. Am J Gastroenterol 2020;115:165-178. PMID 32023228. doi:10.14309/ajg.0000000000000501
  [NAC17]   Rezaie A et al. Hydrogen and methane-based breath testing in gastrointestinal disorders: the
            North American Consensus. Am J Gastroenterol 2017;112:775-784. PMID 28323273 (full text read,
            PMC5418558): SIBO = microbes "normally found in the large intestine" crowding the small bowel;
            healthy small bowel <=10^3 CFU/mL; H2 rise >=20 ppm by 90 min = SIBO positive; CH4 >=10 ppm =
            methane positive; methane-type 5x more likely to have constipation; 8-12 h fast; no
            antibiotics for 4 weeks before; SIBO testing can be limited to 2 hours.
  [SENDER16] Sender R, Fuchs S, Milo R. PLoS Biol 2016;14:e1002533. PMID 27541692: 3.8 x 10^13 bacteria in
            the body, almost all in the colon.
  [SU18]    Su T et al. Meta-analysis: proton pump inhibitors moderately increase the risk of SIBO
            (OR 1.71). J Gastroenterol 2018;53:27-36. PMID 28770351.
  [MMC12]   Deloose E et al. The migrating motor complex. Nat Rev Gastroenterol Hepatol 2012;9:271-85.
            PMID 22450306: fasting "housekeeper" waves, interrupted by eating; absent MMC goes with SIBO.
  [CANDIDA20] Kumamoto CA, Gresnigt MS, Hube B. Curr Opin Microbiol 2020;56:7-15. PMID 32604030: Candida
            is a regular gut resident in most people; dysbiosis, immune suppression and a weak barrier
            let it overgrow.
  [SAMONIS93] Samonis G et al. Antimicrob Agents Chemother 1993;37:51-53. PMID 8431017: broad-spectrum
            antibiotics raise gut yeast colonization.
  [CDC-CAND] CDC, Candidiasis (thrush; vaginal candidiasis): risk factors antibiotics, corticosteroids,
            diabetes, weakened immune system.
  [CDC-GIA] CDC, Giardia: diarrhea, gas, greasy stools that can float, cramps; spread by untreated or
            recreational water, food, surfaces, people and animals.
  [CDC-PIN] CDC, Pinworm: most common worm infection in the US; itching around the anus at night; child
            care and households; diagnosed with a tape test (stool tests not recommended).
  [SCFA13]  den Besten G et al. J Lipid Res 2013;54:2325-40. PMID 23821742: colon bacteria ferment fiber.
  [ND584]   NutriDyn 5R GI Restoration Program ND584 Rev. 1/22: Remove, Replace, Reinoculate, Repair, then
            Restore & Retain; "The first 4 R's last 10 days and all four steps should be done at the same
            time. The final R is from day 11 to day 24." Remove-step diet (sugar, alcohol, processed
            food); "Avoid eating within 2 hours of bedtime"; "Avoid eating under stress. Eat slowly."
  [ALARM]   NIDDK, Diarrhea (see a doctor for blood or black stools, high fever, dehydration); ACG
            Clinical Guideline: Management of IBS, Lacy BE et al. Am J Gastroenterol 2021;116:17-44,
            PMID 33315591 (alarm features: bleeding, unintended weight loss).
  Back-page safety notes: berberine CYP3A4/2D6/2C9 inhibition, Guo Y et al. Eur J Clin Pharmacol
  2012;68:213-7, PMID 21870106; berberine lowers blood sugar like metformin, Yin J et al. Metabolism
  2008;57:712-7, PMID 18442638; berberine and newborn jaundice (NCCIH/MedlinePlus goldenseal; the
  Spectrum BR label advises against use in pregnancy and nursing); invasive Saccharomyces infection,
  catheters the main risk, Enache-Angoulvant A, Hennequin C. Clin Infect Dis 2005;41:1559-68,
  PMID 16267727; S. boulardii is a yeast, so antibacterial antibiotics do not kill it, Kelesidis T,
  Pothoulakis C. Ther Adv Gastroenterol 2012;5:111-25, PMID 22423260; garlic and pau d'arco bleeding
  cautions (NCCIH garlic; pau d'arco interaction monographs); chlorella vitamin K (MedlinePlus).
  Research anchors behind the product picks (not quoted on the page): Chedid V et al. Glob Adv Health
  Med 2014;3:16-24, PMID 24891990 (herbal therapy incl. CandiBactin-BR, which Spectrum BR matches);
  Redondo-Cuevas L et al. Nutrients 2024;16:1083, PMID 38613116; Bustos Fernandez LM et al. Dig Dis
  2023;41:798-809, PMID 36630947 (S. boulardii CNCM I-745, a different strain).
"""
import math
import os
import random

from kit import icon
from svgkit import T, svg

U = "gov"
SLUG = "gut-overgrowth"

# ============================================================== text measuring (for centred pills)
_FACES = {}
_W8 = {400: "Regular", 500: "Medium", 600: "SemiBold", 700: "Bold", 800: "ExtraBold", 900: "Black"}


def tw(text, size, weight=700, ls=0.0):
    """Advance width of text in Inter at size px (falls back to a generous estimate)."""
    try:
        if weight not in _FACES:
            from PIL import ImageFont
            for d in ("/usr/share/fonts/opentype/inter", "/usr/share/fonts/truetype/inter",
                      os.path.expanduser("~/Library/Fonts"), "/Library/Fonts"):
                for ext in ("otf", "ttf"):
                    f = os.path.join(d, f"Inter-{_W8[weight]}.{ext}")
                    if os.path.exists(f):
                        _FACES[weight] = ImageFont.truetype(f, 100)
                        break
                if weight in _FACES:
                    break
        w = _FACES[weight].getlength(text) * size / 100
    except Exception:
        w = len(text) * size * (0.7 if text.isupper() else 0.6)
    return w + ls * len(text)


# ============================================================== palette (every symbol is in the KEY)
INK, INK2 = "#23292D", "#56606A"
OK, OK_TX = "#2F7D59", "#24684A"          # BALANCED
BAD, BAD_TX = "#B3362B", "#9C2C22"        # OVERGROWTH
GOOD_E = "#256F43"                        # friendly bacteria: green rods
OVER_E = "#8E231B"                        # overgrowth bacteria: red rods with short hairs
YEAST_E = "#4A3290"                       # yeast (Candida): purple budding ovals
GAS, GAS_E = "#F6C84A", "#B98A12"         # gas (hydrogen, methane): gold bubbles
EGG, EGG_E, EGG_IN = "#EEDCB4", "#86663A", "#D7B77D"   # parasite egg: tan oval
VIL, VIL_E = "#F6C0AE", "#C0735E"         # villi
SI, SI_E, SI_HI = "#F4BBA6", "#B86E5B", "#FDE4DA"      # small intestine (figure)
CO, CO_E, CO_HA, CO_HI = "#E8B58E", "#99673F", "#B57E55", "#FAE0C6"   # colon (figure)
ST_E = "#A6564A"                          # stomach / esophagus outline

# ============================================================== geometry helpers
def _cr(pts, per=14, closed=False):
    """Catmull-Rom curve through pts, densely sampled (list of points)."""
    n = len(pts)
    P = (pts[-1:] + pts + pts[:2]) if closed else ([pts[0]] + pts + [pts[-1]])
    out = []
    for i in range(n if closed else n - 1):
        p0, p1, p2, p3 = P[i], P[i + 1], P[i + 2], P[i + 3]
        for k in range(per):
            t = k / per
            t2, t3 = t * t, t * t * t
            out.append(tuple(0.5 * (2 * p1[j] + (-p0[j] + p2[j]) * t + (2 * p0[j] - 5 * p1[j] + 4 * p2[j] - p3[j]) * t2
                                    + (-p0[j] + 3 * p1[j] - 3 * p2[j] + p3[j]) * t3) for j in (0, 1)))
    if not closed:
        out.append(tuple(pts[-1]))
    return out


def _resample(pts, step):
    """Points every `step` units of arc length along a dense polyline; returns (points, lengths)."""
    cum = [0.0]
    for a, b in zip(pts, pts[1:]):
        cum.append(cum[-1] + math.hypot(b[0] - a[0], b[1] - a[1]))
    L = cum[-1]
    out, ss, j = [], [], 0
    s = 0.0
    while s <= L + 1e-6:
        while j < len(cum) - 2 and cum[j + 1] < s:
            j += 1
        seg = cum[j + 1] - cum[j] or 1
        f = (s - cum[j]) / seg
        out.append((pts[j][0] + (pts[j + 1][0] - pts[j][0]) * f, pts[j][1] + (pts[j + 1][1] - pts[j][1]) * f))
        ss.append(s)
        s += step
    return out, ss


def _normals(pts):
    ns = []
    for i in range(len(pts)):
        a, b = pts[max(i - 1, 0)], pts[min(i + 1, len(pts) - 1)]
        dx, dy = b[0] - a[0], b[1] - a[1]
        m = math.hypot(dx, dy) or 1
        ns.append((-dy / m, dx / m))
    return ns


def _poly(pts, close=False):
    d = "M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in pts)
    return d + ("Z" if close else "")


def _smooth_d(pts, closed=True):
    """Smooth path data through pts (Catmull-Rom as cubic Beziers)."""
    n = len(pts)
    P = (pts[-1:] + pts + pts[:2]) if closed else ([pts[0]] + pts + [pts[-1]])
    d = [f"M{pts[0][0]:.1f},{pts[0][1]:.1f}"]
    for i in range(n if closed else n - 1):
        p0, p1, p2, p3 = P[i], P[i + 1], P[i + 2], P[i + 3]
        c1 = (p1[0] + (p2[0] - p0[0]) / 6, p1[1] + (p2[1] - p0[1]) / 6)
        c2 = (p2[0] - (p3[0] - p1[0]) / 6, p2[1] - (p3[1] - p1[1]) / 6)
        d.append(f"C{c1[0]:.1f},{c1[1]:.1f} {c2[0]:.1f},{c2[1]:.1f} {p2[0]:.1f},{p2[1]:.1f}")
    return " ".join(d) + (" Z" if closed else "")


# ============================================================== symbols (drawn centred on x, y)
def rod(x, y, rot=0.0, kind="ok", L=12.5, w=5.4):
    """One rod-shaped bacterium.  kind ok = friendly (smooth green); bad = overgrowth (red, short hairs:
    the hairs let the two kinds be told apart without colour)."""
    edge = GOOD_E if kind == "ok" else OVER_E
    hairs = ""
    if kind == "bad":
        hs = "".join(f"M{-L / 2 + 2.6 + i * (L - 5.2) / 3:.2f},{-w / 2:.2f} l-.9,-2.6 "
                     f"M{-L / 2 + 2.6 + i * (L - 5.2) / 3:.2f},{w / 2:.2f} l-.9,2.6 " for i in range(4))
        hairs = f'<path d="{hs}" stroke="{edge}" stroke-width=".85" stroke-linecap="round" fill="none"/>'
    return (f'<g transform="translate({x:.1f},{y:.1f}) rotate({rot:.0f})">{hairs}'
            f'<rect x="{-L / 2:.2f}" y="{-w / 2:.2f}" width="{L}" height="{w}" rx="{w / 2:.2f}" fill="url(#{U}-r{kind})" '
            f'stroke="{edge}" stroke-width=".8"/>'
            f'<path d="M{-L / 2 + 2.4:.2f},{-w * 0.17:.2f} H{L / 2 - 2.4:.2f}" stroke="#FFFFFF" stroke-opacity=".5" '
            'stroke-width="1.1" stroke-linecap="round"/></g>')


def yeast(x, y, rot=0.0, s=1.0, bud=True):
    """A budding yeast cell (Candida): an oval mother cell with a smaller bud and a pale vacuole."""
    b = ""
    if bud:
        b = (f'<ellipse cx="7.3" cy="-2.6" rx="3.7" ry="3.1" transform="rotate(-24 7.3 -2.6)" fill="url(#{U}-ye)" '
             f'stroke="{YEAST_E}" stroke-width=".9"/>')
    return (f'<g transform="translate({x:.1f},{y:.1f}) rotate({rot:.0f}) scale({s})">{b}'
            f'<ellipse rx="6.7" ry="5.3" fill="url(#{U}-ye)" stroke="{YEAST_E}" stroke-width="1"/>'
            '<ellipse cx="-1.2" cy=".6" rx="2.2" ry="1.7" fill="#E3D8F7" opacity=".85"/>'
            '<path d="M-4.2,-2.6 Q-2,-4.4 1,-4.3" stroke="#FFFFFF" stroke-opacity=".55" stroke-width="1" fill="none" '
            'stroke-linecap="round"/></g>')


def hypha(x, y, ang, n=3, s=1.0):
    """A short chain of stretched yeast cells (a pseudohypha) growing from the lining at (x, y)."""
    o = []
    a = math.radians(ang)
    px, py = x, y
    for i in range(n):
        da = math.radians((-1) ** i * 9)
        cx, cy = px + 6.1 * s * math.cos(a), py + 6.1 * s * math.sin(a)
        o.append(f'<ellipse cx="{cx:.1f}" cy="{cy:.1f}" rx="{6.3 * s:.1f}" ry="{2.9 * s:.1f}" '
                 f'transform="rotate({math.degrees(a):.0f} {cx:.1f} {cy:.1f})" fill="url(#{U}-ye)" '
                 f'stroke="{YEAST_E}" stroke-width=".9"/>')
        px, py = px + 11.8 * s * math.cos(a), py + 11.8 * s * math.sin(a)
        a += da
    return "".join(o)


def bubble(x, y, r):
    """A gas bubble (hydrogen or methane made by microbes)."""
    return (f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r:.1f}" fill="{GAS}" fill-opacity=".92" stroke="{GAS_E}" stroke-width="1"/>'
            f'<circle cx="{x - r * .36:.1f}" cy="{y - r * .36:.1f}" r="{max(r * .26, .9):.1f}" fill="#FFFFFF" opacity=".85"/>')


def egg(x, y, rot=0.0, s=1.0):
    """A parasite egg: thick oval shell around a grainy embryo."""
    gran = "".join(f'<circle cx="{gx}" cy="{gy}" r="1.15" fill="#B48E55"/>'
                   for gx, gy in ((-3.6, -1.2), (-1, 1.6), (1.6, -1.4), (3.9, 1.1), (-.6, -2.6), (2.2, 2.4), (-3, 2.1)))
    return (f'<g transform="translate({x:.1f},{y:.1f}) rotate({rot:.0f}) scale({s})">'
            f'<ellipse rx="12" ry="7.7" fill="{EGG}" stroke="{EGG_E}" stroke-width="1.7"/>'
            '<ellipse rx="10.1" ry="5.9" fill="none" stroke="#BE9D66" stroke-width="1"/>'
            f'<ellipse rx="7.4" ry="4.4" fill="{EGG_IN}"/>{gran}'
            '<path d="M-8.4,-4.6 Q-4,-7 1.5,-6.8" stroke="#FFFFFF" stroke-opacity=".7" stroke-width="1.2" fill="none" '
            'stroke-linecap="round"/></g>')


def villus(x, base, h, tilt=0.0, w=8.2):
    """One finger-like villus rising from `base` (y) to a rounded tip h above it."""
    r = w / 2
    return (f'<g transform="rotate({tilt:.1f} {x:.1f} {base:.1f})">'
            f'<path d="M{x - r:.1f},{base + 3:.1f} V{base - h + r:.1f} A{r:.1f},{r:.1f} 0 0 1 {x + r:.1f},{base - h + r:.1f} '
            f'V{base + 3:.1f} Z" fill="url(#{U}-vi)" stroke="{VIL_E}" stroke-width=".8"/>'
            f'<path d="M{x:.1f},{base:.1f} V{base - h + 6:.1f}" stroke="#FDE6DD" stroke-width="1.3" stroke-linecap="round" '
            'opacity=".9"/></g>')


# ============================================================== the digestive tract (local 300 x 360 box)
# Front view, as if facing the person: their right side is on the viewer's left.
ESO = [(152, -2), (156, 26), (162, 50), (171, 69)]
STOMACH = [(171, 66), (178, 55), (194, 47), (214, 49), (231, 61), (242, 82), (245, 108), (239, 134), (224, 156),
           (201, 171), (174, 176), (149, 170), (131, 160), (120, 152), (116, 146), (121, 140), (136, 143),
           (153, 143), (168, 134), (176, 116), (176, 95), (172, 80)]
# Duodenum (C-loop round the pancreas head) then the coiled jejunum and ileum, ending at the cecum.
DUO = [(118, 148), (104, 150), (94, 159), (90, 176), (93, 192), (104, 202), (122, 207), (146, 206), (170, 201),
       (192, 196), (209, 199)]
ROWS = [214, 230, 246, 262, 278]
COLON = [(60, 302), (55, 288), (53, 270), (53, 248), (54, 226), (56, 204), (60, 185), (67, 171), (79, 163),
         (97, 166), (117, 176), (141, 186), (166, 190), (192, 186), (216, 176), (238, 162), (256, 151), (271, 147),
         (281, 153), (285, 167), (285, 190), (284, 214), (282, 238), (279, 260), (273, 278), (262, 292),
         (246, 301), (226, 305), (208, 301), (192, 302), (179, 310), (170, 321), (165, 333), (163, 343), (162, 350)]
SI_LENS = (164, 230)          # zoom spots, local coordinates
CO_LENS_L, CO_LENS_R = (54, 240), (283, 228)


def _si_center():
    """Centre line of the small intestine: duodenum C-loop, then five rows of coils, then the terminal ileum."""
    pts = list(DUO)
    ends = [(212, 97), (97, 249), (249, 93), (93, 246), (246, 104)]      # (start x, end x) per row
    for i, (y, (xa, xb)) in enumerate(zip(ROWS, ends)):
        n = 9
        for k in range(n + 1):
            x = xa + (xb - xa) * k / n
            if i == 0 and k == 0:
                continue
            pts.append((x, y + 1.7 * math.sin(x / 8.5 + i * 1.9)))
        if i < len(ROWS) - 1:
            d = 1 if xb > xa else -1
            pts.append((xb + d * 7.6, y + 8))
    pts += [(88, 281), (76, 286), (63, 291)]   # terminal ileum, ending under the cecum (ileocecal valve)
    return pts


def _tube_stroke(pts, w, fill, edge, hi, ew=1.2):
    d = _poly(pts)
    return (f'<path d="{d}" fill="none" stroke="{edge}" stroke-width="{w + 2 * ew}" stroke-linecap="round" stroke-linejoin="round"/>'
            f'<path d="{d}" fill="none" stroke="{fill}" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round"/>'
            f'<path d="{d}" fill="none" stroke="{hi}" stroke-width="{w * .32:.1f}" stroke-linecap="round" '
            'stroke-linejoin="round" opacity=".75"/>')


def _colon():
    """Colon from cecum to rectum: scalloped outline (haustra), fold lines, rim light, taenia band."""
    dense = _cr(COLON, per=16)
    pts, ss = _resample(dense, 1.4)
    ns = _normals(pts)
    L = ss[-1]
    P, rect, canal = 14.5, 48.0, 24.0       # haustra spacing; the rectum (last 48 units) is smooth, then the anal canal

    def base(s):
        if s < 22:
            return 15.2 - 1.4 * s / 22        # the cecum is the widest part
        if s > L - canal:                     # the rectum narrows smoothly into the short anal canal
            f = (s - (L - canal)) / canal
            return 13.9 - 7.3 * f * f * (3 - 2 * f)
        if s > L - rect:                      # rectal ampulla: smooth, a little fuller
            f = (s - (L - rect)) / (rect - canal)
            return 13.6 + 0.3 * math.sin(f * math.pi / 2)
        return 13.6

    def hw(s):
        b = base(s)
        if 10 < s < L - rect:
            return b * (0.86 + 0.14 * abs(math.sin(math.pi * (s - 10) / P)) ** 0.55)
        return b

    left = [(p[0] + n[0] * hw(s), p[1] + n[1] * hw(s)) for p, n, s in zip(pts, ns, ss)]
    right = [(p[0] - n[0] * hw(s), p[1] - n[1] * hw(s)) for p, n, s in zip(pts, ns, ss)]

    def cap(i, back):
        """Round end at sample i, bulging along -tangent (back=True, the cecum) or +tangent (the anal end)."""
        c, n = pts[i], ns[i]
        t = (-n[1], n[0]) if back else (n[1], -n[0])
        r = hw(ss[i])
        a_list = [math.pi * k / 16 for k in range(17)]
        if not back:
            a_list = a_list[::-1]
        return [(c[0] + r * (n[0] * math.cos(a) + t[0] * math.sin(a)), c[1] + r * (n[1] * math.cos(a) + t[1] * math.sin(a)))
                for a in a_list]

    # left side walked backwards to the cecum, round blind end, right side forwards, rounded anal end
    outline = _poly(left[::-1] + cap(0, True)[1:-1] + right + cap(len(pts) - 1, False)[1:-1], close=True)
    # fold lines at each haustral constriction
    folds = []
    k = 1
    while 10 + k * P < L - rect - 4:
        s = 10 + k * P
        i = min(range(len(ss)), key=lambda j: abs(ss[j] - s))
        (lx, ly), (rx, ry) = left[i], right[i]
        tx2, ty2 = ns[i][1], -ns[i][0]
        cx, cy = (lx + rx) / 2 - tx2 * 3.2, (ly + ry) / 2 - ty2 * 3.2
        folds.append(f"M{lx:.1f},{ly:.1f} Q{cx:.1f},{cy:.1f} {rx:.1f},{ry:.1f}")
        k += 1
    rim = _poly([(p[0] - n[0] * hw(s) * 0.55, p[1] - n[1] * hw(s) * 0.55) for p, n, s in zip(pts, ns, ss)][8:-20])
    taenia = _poly([(p[0] + n[0] * hw(s) * 0.18, p[1] + n[1] * hw(s) * 0.18) for p, n, s in zip(pts, ns, ss)][14:-34])
    return (f'<path d="{outline}" fill="url(#{U}-co)" stroke="{CO_E}" stroke-width="1.4" stroke-linejoin="round"/>'
            f'<path d="{" ".join(folds)}" fill="none" stroke="{CO_HA}" stroke-width="1.2" stroke-linecap="round" opacity=".8"/>'
            f'<path d="{taenia}" fill="none" stroke="#F3CFAE" stroke-width="2.2" stroke-linecap="round" opacity=".75"/>'
            f'<path d="{rim}" fill="none" stroke="{CO_HI}" stroke-width="2.4" stroke-linecap="round" opacity=".8"/>')


def _appendix():
    pts = _cr([(66, 309), (70, 318), (78, 326), (88, 330)], per=10)
    return _tube_stroke(pts, 5.6, "#E9B08E", CO_E, "#F8D9C2", 1.1)


def figure():
    """The whole digestive tract in local coordinates (about 300 x 360)."""
    # white ground inside the colon frame, so the zoom beams' soft fill shows only outside the organs
    o = [f'<path d="{_smooth_d(COLON[:-4])}" fill="#FFFFFF"/>']
    # esophagus (fades in at the top: the throat is above the picture)
    eso = _poly(_cr(ESO, per=12))
    o.append(f'<path d="{eso}" fill="none" stroke="url(#{U}-esoE)" stroke-width="13.4" stroke-linecap="butt"/>'
             f'<path d="{eso}" fill="none" stroke="url(#{U}-esoF)" stroke-width="11" stroke-linecap="butt"/>')
    # small intestine (duodenum, jejunum, ileum) sits behind the stomach and the colon
    si = _resample(_cr(_si_center(), per=8), 1.5)[0]
    o.append(_tube_stroke(si, 11.6, SI, SI_E, SI_HI))
    # stomach
    sd = _smooth_d(STOMACH)
    o.append(f'<path d="{sd}" fill="url(#{U}-st)" stroke="{ST_E}" stroke-width="1.4" stroke-linejoin="round"/>'
             '<path d="M186,58 C202,52 221,56 233,70" fill="none" stroke="#FFE3DA" stroke-width="3" stroke-linecap="round" opacity=".8"/>'
             f'<path d="M121.5,141 C118,144 118,150 121,153" fill="none" stroke="{ST_E}" stroke-width="2.2" stroke-linecap="round"/>')
    o.append(_appendix())
    o.append(_colon())
    return "".join(o)


# ============================================================== zoom circles
def _place(rng, n, r_item, ok, taken, gap=1.5, tries=6000):
    """Random spots for n round-ish items of radius r_item: inside ok(x, y), clear of everything taken."""
    out = []
    for _ in range(n):
        for _t in range(tries):
            x, y = rng.uniform(-80, 80), rng.uniform(-80, 80)
            if not ok(x, y, r_item):
                continue
            if any(math.hypot(x - a, y - b) < r_item + rb + gap for a, b, rb in taken + out):
                continue
            out.append((x, y, r_item))
            break
    return out


def _in_circle(R, top_cut):
    """Region test: inside the circle (with margin) and above the lining at y = top_cut."""
    return lambda x, y, r: math.hypot(x, y) < R - r - 3 and y < top_cut - r - 1


def si_zoom(cx, cy, R, over):
    rng = random.Random(41 if over else 17)
    floor = R * 0.42
    o = [f'<rect x="{cx - R}" y="{cy - R}" width="{2 * R}" height="{2 * R}" fill="url(#{U}-lu)"/>',
         f'<rect x="{cx - R}" y="{cy + floor}" width="{2 * R}" height="{R}" fill="url(#{U}-ti)"/>']
    x = -R - 3.0
    while x < R + 6:
        h = rng.uniform(26, 31)
        o.append(villus(cx + x, cy + floor, h, rng.uniform(-4, 4)))
        x += 10.6
    o.append(f'<path d="M{cx - R},{cy + floor + 3} H{cx + R}" stroke="{VIL_E}" stroke-width=".8" opacity=".35"/>')
    tips = floor - 31
    if not over:
        for (dx, dy, a) in [(-30, -30, 18), (14, -44, -28), (36, -10, 40), (-6, 2, -12)]:
            o.append(rod(cx + dx, cy + dy, a, "ok"))
        return "".join(o)
    taken = []
    gas = _place(rng, 4, 6.2, _in_circle(R, tips), taken, 3) + _place(rng, 7, 3.6, _in_circle(R, tips + 6), taken, 2.4)
    taken += gas
    bad = _place(rng, 26, 5.4, _in_circle(R, tips + 10), taken, 0.8)
    taken += bad
    good = _place(rng, 3, 5.4, _in_circle(R, tips + 6), taken, 1.2)
    for x, y, _ in good:
        o.append(rod(cx + x, cy + y, rng.uniform(0, 180), "ok"))
    for x, y, _ in bad:
        o.append(rod(cx + x, cy + y, rng.uniform(0, 180), "bad"))
    for x, y, r in gas:
        o.append(bubble(cx + x, cy + y, r))
    return "".join(o)


def colon_zoom(cx, cy, R, over):
    rng = random.Random(53 if over else 29)
    floor = R * 0.46
    o = [f'<rect x="{cx - R}" y="{cy - R}" width="{2 * R}" height="{2 * R}" fill="url(#{U}-lc)"/>']
    # flat lining with crypt openings (the colon has no villi)
    top = [(cx - R - 4 + k * 6, cy + floor + 1.4 * math.sin(k * 0.9)) for k in range(int((2 * R + 8) / 6) + 2)]
    o.append(f'<path d="{_poly(top)} V{cy + R + 4} H{cx - R - 4} Z" fill="url(#{U}-cw)" stroke="#C27A5F" stroke-width="1"/>')
    x = -R + 4.0
    while x < R:
        yy = cy + floor + 1.4 * math.sin((x + R + 4) / 6 * 0.9) + 1
        o.append(f'<rect x="{cx + x - 2.3:.1f}" y="{yy:.1f}" width="4.6" height="19" rx="2.3" fill="#D68C72"/>'
                 f'<ellipse cx="{cx + x:.1f}" cy="{yy + 1:.1f}" rx="2.6" ry="1.3" fill="#B96D55"/>')
        x += 11.5
    if not over:
        taken = []
        good = _place(rng, 56, 5.2, _in_circle(R, floor), taken, 0.3)
        for x, y, _ in good:
            o.append(rod(cx + x, cy + y, rng.uniform(0, 180), "ok"))
        return "".join(o)
    # overgrowth: yeast spreading on the lining, a parasite egg, fewer friendly bacteria, some overgrowth
    taken = []
    o.append(egg(cx + 22, cy + floor - 10, -12, 1.0))
    taken.append((22, floor - 10, 13))
    for (dx, a, s) in [(-38, -96, 1.0), (-8, -78, 0.95)]:
        o.append(hypha(cx + dx, cy + floor - 1, a, 3, s))
        taken += [(dx + 4 * math.cos(math.radians(a)) * k, floor - 6 * k, 6) for k in range(1, 6)]
    for (dx, dy, a, s, b) in [(-24, -6, 15, 1.0, True), (4, -5, -20, 0.95, True), (46, -6, 30, 0.9, False),
                              (-50, -8, -10, 0.9, True), (8, -17, 40, 0.85, False)]:
        o.append(yeast(cx + dx, cy + floor + dy, a, s, b))
        taken.append((dx, floor + dy, 8.5 * s))
    for (dx, dy, r) in [(-16, -40, 4.2), (30, -46, 3.2)]:
        o.append(bubble(cx + dx, cy + dy, r))
        taken.append((dx, dy, r))
    good = _place(rng, 15, 5.2, _in_circle(R, floor - 16), taken, 1.0)
    taken += good
    bad = _place(rng, 9, 5.4, _in_circle(R, floor - 16), taken, 1.0)
    for x, y, _ in good:
        o.append(rod(cx + x, cy + y, rng.uniform(0, 180), "ok"))
    for x, y, _ in bad:
        o.append(rod(cx + x, cy + y, rng.uniform(0, 180), "bad"))
    return "".join(o)


def zoom(cx, cy, R, fn, over, uid):
    return (f'<clipPath id="{U}-z{uid}"><circle cx="{cx}" cy="{cy}" r="{R}"/></clipPath>'
            f'<g clip-path="url(#{U}-z{uid})">{fn(cx, cy, R, over)}</g>'
            f'<circle cx="{cx}" cy="{cy}" r="{R + 2.2}" fill="none" stroke="#FFFFFF" stroke-width="2.4"/>'
            f'<circle cx="{cx}" cy="{cy}" r="{R}" fill="none" stroke="#33403F" stroke-width="2.4"/>')


def beam(c1, r1, c2, r2):
    """Zoom beam from a small lens to a zoom circle: the outer tangents to a circle of radius r2 at the
    zoom centre (r2 smaller than the zoom, so the beam enters on its near side).  Returns (fill, lines):
    the soft fill goes behind the organs, the two edge lines in front."""
    (x1, y1), (x2, y2) = c1, c2
    d = math.hypot(x2 - x1, y2 - y1)
    th = math.atan2(y2 - y1, x2 - x1)
    b = math.acos((r1 - r2) / d)
    p = []
    for sg in (1, -1):
        a = th + sg * b
        p.append(((x1 + r1 * math.cos(a), y1 + r1 * math.sin(a)), (x2 + r2 * math.cos(a), y2 + r2 * math.sin(a))))
    (a1, a2), (b1, b2) = p
    poly = f"M{a1[0]:.1f},{a1[1]:.1f} L{a2[0]:.1f},{a2[1]:.1f} L{b2[0]:.1f},{b2[1]:.1f} L{b1[0]:.1f},{b1[1]:.1f} Z"
    return (f'<path d="{poly}" fill="#E8EEF0" fill-opacity=".9"/>',
            f'<path d="M{a1[0]:.1f},{a1[1]:.1f} L{a2[0]:.1f},{a2[1]:.1f} M{b1[0]:.1f},{b1[1]:.1f} L{b2[0]:.1f},{b2[1]:.1f}" '
            'stroke="#6B777C" stroke-width="1.1" stroke-opacity=".75" fill="none"/>')


def lens(x, y, r=9):
    return (f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="#FFFFFF" fill-opacity=".22" stroke="#FFFFFF" stroke-width="2.4"/>'
            f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r + 1.7:.1f}" fill="none" stroke="#2F2A28" stroke-width=".9" stroke-opacity=".6"/>')


# ============================================================== the art
W, H = 760, 336
FS = 0.905                             # figure scale (local box 300 x 360)
FX, FY = 380 - 168 * FS, 5             # where the figure's local box sits (centre line x = 168 local)
LX, RX, R = 96, 664, 61                # zoom circle columns and radius
SY, CY = 99, 254                       # small-intestine row, colon row


def defs_svg():
    g = []
    lin = lambda i, a, b, x2=0, y2=1: (f'<linearGradient id="{U}-{i}" x1="0" y1="0" x2="{x2}" y2="{y2}">'
                                        f'<stop offset="0" stop-color="{a}"/><stop offset="1" stop-color="{b}"/></linearGradient>')
    g.append(lin("rok", "#9EDDAE", "#3D9B5C"))
    g.append(lin("rbad", "#F49A8A", "#C93A2D"))
    g.append(f'<radialGradient id="{U}-ye" cx=".38" cy=".34" r=".75"><stop offset="0" stop-color="#C8B5EE"/>'
             '<stop offset="1" stop-color="#7556BE"/></radialGradient>')
    g.append(lin("vi", "#FAD3C5", "#EDA690"))
    g.append(lin("ti", "#EFA48E", "#D9826C"))
    g.append(lin("lu", "#FFF8F1", "#FDEDE2"))
    g.append(lin("lc", "#FCF2E6", "#F6E3CF"))
    g.append(lin("cw", "#EFBDA3", "#DE9479"))
    g.append(lin("co", "#F0C29D", "#DFA67C", 1, 1))
    g.append(lin("st", "#F8C1B1", "#E28C77", 1, 1))
    g.append('<linearGradient id="gov-esoE" gradientUnits="userSpaceOnUse" x1="0" y1="-2" x2="0" y2="34">'
             f'<stop offset="0" stop-color="{ST_E}" stop-opacity="0"/><stop offset="1" stop-color="{ST_E}"/></linearGradient>')
    g.append('<linearGradient id="gov-esoF" gradientUnits="userSpaceOnUse" x1="0" y1="-2" x2="0" y2="34">'
             '<stop offset="0" stop-color="#F1AE9C" stop-opacity="0"/><stop offset="1" stop-color="#F1AE9C"/></linearGradient>')
    return "<defs>" + "".join(g) + "</defs>"


def _pill(cx, y, text, fill, size=12.5, h=22, color="#FFFFFF", stroke=None, ls=1.1):
    w = tw(text, size, 800, ls) + 2 * h * 0.62
    st = f' stroke="{stroke}" stroke-width="1.3"' if stroke else ""
    return (f'<rect x="{cx - w / 2:.1f}" y="{y}" width="{w:.1f}" height="{h}" rx="{h / 2}" fill="{fill}"{st}/>'
            + T(cx, y + h / 2 + size * 0.36, text, size, 800, color, "middle", ls=ls))


def _tag(cx, cy_top, text):
    """Organ name sitting on the top rim of a zoom circle (opaque, so it never sits on busy art)."""
    return _pill(cx, cy_top - 8.5, text, "#FFFFFF", 10.5, 17, INK, "#33403F", 1.0)


def art_overgrowth():
    gl = lambda p: (FX + p[0] * FS, FY + p[1] * FS)
    o = [defs_svg()]
    si_l = gl(SI_LENS)
    co_l, co_r = gl(CO_LENS_L), gl(CO_LENS_R)
    # beam fills behind the organs, the figure, beam edges in front, lenses, then the zoom circles
    beams = [beam(si_l, 8.5, (LX, SY), R * 0.6), beam(si_l, 8.5, (RX, SY), R * 0.6),
             beam(co_l, 8.5, (LX, CY), R * 0.6), beam(co_r, 8.5, (RX, CY), R * 0.6)]
    o.append("".join(f for f, _ in beams))
    o.append(f'<g transform="translate({FX:.1f},{FY}) scale({FS})">{figure()}</g>')
    o.append("".join(ln for _, ln in beams))
    o.append(lens(*si_l, 8.5) + lens(*co_l, 8.5) + lens(*co_r, 8.5))
    o.append(zoom(LX, SY, R, si_zoom, False, "a") + zoom(RX, SY, R, si_zoom, True, "b"))
    o.append(zoom(LX, CY, R, colon_zoom, False, "c") + zoom(RX, CY, R, colon_zoom, True, "d"))
    # column headers, organ tags on the circle rims, and what each circle shows (clear space only)
    o.append(_pill(LX, 1, "BALANCED", OK, h=21) + _pill(RX, 1, "OVERGROWTH", BAD, h=21))
    for cx in (LX, RX):
        o.append(_tag(cx, SY - R, "SMALL INTESTINE") + _tag(cx, CY - R, "COLON"))
    subs = [(LX, SY, "only a few bacteria", OK_TX), (RX, SY, "crowded with bacteria and gas", BAD_TX),
            (LX, CY, "a thick, friendly colony", OK_TX), (RX, CY, "yeast and parasites take hold", BAD_TX)]
    for cx, cy, s, col in subs:
        o.append(T(cx, cy + R + 15.5, s, 11.2, 700, col, "middle", italic=True))
    # one organ name the zooms do not carry
    sx, sy = gl((246, 92))
    o.append(f'<path d="M{sx - 4:.1f},{sy:.1f} H{sx + 13:.1f}" stroke="#7B848A" stroke-width="1.1"/>'
             + T(sx + 17, sy + 3.9, "Stomach", 11, 700, INK2))
    return svg(W, H, "".join(o), "The digestive tract with zoomed views of the small intestine and the colon. Balanced: "
               "only a few bacteria in the small intestine and a thick friendly colony in the colon. Overgrowth: the small "
               "intestine is crowded with bacteria and gas bubbles, and yeast and a parasite egg sit on the colon lining.")


# ============================================================== KEY (HTML, same drawing code as the art)
def _sw(markup, vb=30):
    h = vb / 2
    return f'<svg viewBox="{-h} {-h} {vb} {vb}" aria-hidden="true">{markup}</svg>'


def key_html():
    vil = (f'<rect x="-14" y="5" width="28" height="10" fill="url(#{U}-ti)"/>'
           + villus(-7.5, 7, 17, -3, 6.6) + villus(0, 7, 19, 0, 6.6) + villus(7.5, 7, 16, 4, 6.6))
    items = [
        (rod(0, 0, -30, "ok", 15, 6.2), "Friendly bacteria"),
        (rod(0, 0, -30, "bad", 15, 6.2), "Overgrowth bacteria"),
        (yeast(-2, 1, -10, 1.15), "Yeast (Candida)"),
        (bubble(-4, 3, 6.5) + bubble(6, -5, 4), "Gas: hydrogen, methane"),
        (egg(0, 0, -15, 0.95), "Parasite egg"),
        (vil, "Villi: gut lining"),
    ]
    cells = "".join(f'<div>{_sw(sw)}<b>{a}</b></div>' for sw, a in items)
    return f'<div class="{U}-key"><span class="{U}-kt">Key</span><div class="{U}-kg">{cells}</div></div>'


# ============================================================== three kinds of overgrowth
def _mini(markup, vb=34):
    h = vb / 2
    return f'<svg class="{U}-mi" viewBox="{-h} {-h} {vb} {vb}" aria-hidden="true">{markup}</svg>'


KINDS = [
    (_mini(rod(-6, -6, 20, "bad") + rod(6, 2, -35, "bad") + rod(-4, 8, 60, "bad") + bubble(8, -9, 4.2) + bubble(-11, 4, 3)),
     # [NAC17] SIBO = too many microbes "normally found in the large intestine" in the small bowel
     "SIBO", "small intestinal bacterial overgrowth",
     # [ACG20] [NAC17]: bloating, gas, pain, diarrhea; the methane type is 5x more likely to have constipation
     ["Bloating and gas after meals", "Belly pain, diarrhea", "Constipation (methane type)"],
     # [SU18] PPIs OR 1.71; [MMC12] [ACG20] slow motility (diabetes; opioids slow the gut); [ACG20] prior surgery
     ["Low stomach acid, acid blockers", "A slow gut (diabetes, opioids)", "Past belly surgery"],
     # [NAC17] [ACG20] glucose or lactulose breath test
     "Breath test (see below)"),
    (_mini(yeast(-3, 2, -10, 1.35) + yeast(9, -8, 30, 0.8, False)),
     # [CANDIDA20]: Candida is a regular member of the gut flora in most people
     "Yeast", "Candida, normally in small numbers",
     # [CDC-CAND] thrush and vaginal candidiasis
     ["White mouth patches (thrush)", "Repeat vaginal yeast infections"],
     # [SAMONIS93] antibiotics; [CDC-CAND] corticosteroids, diabetes, weakened immune system
     ["Antibiotics, steroid medicines", "High blood sugar", "A weakened immune system"],
     "Stool test (culture or DNA panel)"),
    (_mini(egg(0, 0, -15, 1.15)),
     # [CDC-GIA] [CDC-PIN]
     "Parasites", "such as Giardia or pinworm",
     # [CDC-GIA] diarrhea, gas, cramps, greasy stools that can float; [CDC-PIN] itching at night
     ["Diarrhea, cramps and gas", "Greasy stools that float", "Itchy bottom at night (pinworm)"],
     # [CDC-GIA] untreated or recreational water, travel, food, people, animals; [CDC-PIN] child care, households
     ["Untreated lake or stream water", "Travel, swimming, child care", "Close contact, pets"],
     # [CDC-GIA] stool samples; [CDC-PIN] tape test (stool tests are not recommended for pinworm)
     "Stool test (tape test for pinworm)"),
]


def kinds_html():
    cards = []
    li = lambda xs: "".join(f"<li>{x}</li>" for x in xs)
    for mi, name, sub, clues, feeds, test in KINDS:
        cards.append(f'<div class="{U}-kc"><div class="{U}-kh">{mi}<div><b>{name}</b><span>{sub}</span></div></div>'
                     f'<div class="{U}-kl"><i>Clues</i><ul>{li(clues)}</ul></div>'
                     f'<div class="{U}-kl {U}-kf"><i>Risks</i><ul>{li(feeds)}</ul></div>'
                     f'<div class="{U}-kl {U}-kt2"><i>Test</i><p>{test}</p></div></div>')
    return (f'<div class="{U}-sh">Three kinds of overgrowth<span>Testing shows which one you have. Ask your provider '
            'which test fits you.</span></div>'
            f'<div class="{U}-kinds">{"".join(cards)}</div>')


# ============================================================== breath test numbers + red flags
def numbers_html():
    tiles = (
        # [NAC17]: a rise of >=20 ppm from baseline in hydrogen by 90 min = positive for SIBO
        f'<div class="{U}-n"><i>Hydrogen</i><b>rises 20 ppm or more</b><span>within 90 minutes: SIBO</span></div>'
        # [NAC17] / [ACG20]: methane >=10 ppm = methane positive (ACG 2020 calls it intestinal methanogen overgrowth)
        f'<div class="{U}-n"><i>Methane</i><b>10 ppm or more</b><span>at any point: methane type</span></div>'
        f'<div class="{U}-mine"><span>My result</span></div>')
    # [NAC17]: 8-12 h fast; glucose or lactulose drink; SIBO testing can be limited to 2 hours
    lead = (f'<div class="{U}-nl">{icon("breath", "0.3in", sw=3.4)}<div><b>Breath test: know your numbers</b>'
            '<span>After an overnight fast you drink a sugar solution, then breathe into tubes for about 2 hours. '
            'Misplaced bacteria turn the sugar into gas, measured in ppm (parts per million).</span></div></div>')
    # [ALARM]: blood or black stools, high fever, unplanned weight loss; confirmed parasites are treated with medicine
    alarm = (f'<div class="{U}-alarm">{icon("warning", "0.19in", sw=4)}<p><b>Get checked soon</b> for blood or black '
             'stools, a high fever or weight loss you did not try for. Confirmed parasites usually need medicine.</p></div>')
    return f'<div class="{U}-nums">{lead}{tiles}</div>{alarm}'


# ============================================================== the 5R ribbon
FIVE = [("Remove", "clear the overgrowth", "This sheet"), ("Replace", "stomach acid, enzymes", None),
        ("Reinoculate", "friendly bacteria", None), ("Repair", "heal the lining", None),
        ("Retain", "keep the balance", None)]


def five_r_html():
    cells = []
    for i, (name, sub, tag) in enumerate(FIVE):
        cls = f' class="{U}-on"' if i == 0 else (f' class="{U}-rp"' if name == "Repair" else "")
        t = f'<em>{tag}</em>' if tag else ""
        cells.append(f'<div{cls}><b><i>{i + 1}</i>{name}</b><span>{sub}</span>{t}</div>')
    # [ND584] order: Remove, Replace, Reinoculate, Repair, Restore & Retain.  Repair lives on ND-GI-101.
    return (f'<div class="{U}-5r"><div class="{U}-5rh"><b>The 5R gut plan</b><span>Repair: see the '
            '<em>Intestinal Permeability</em> sheet.</span></div>'
            f'<div class="{U}-5rr">{"".join(cells)}</div></div>')


# ============================================================== front page
def front(t, ed):
    return (f'<div class="{U}">'
            f'<div class="art {U}-art">{art_overgrowth()}</div>'
            f'{key_html()}{kinds_html()}{numbers_html()}{five_r_html()}</div>')


CSS = r"""
.gov .gov-art svg{display:block;width:100%;height:auto}
.gov-key{position:relative;border:1.2px solid #C9D6DA;border-radius:8px;padding:8px 8px 5px;margin-top:6px}
.gov-kt{position:absolute;top:-7px;left:12px;background:#fff;padding:0 6px;font:800 7.2pt Inter,sans-serif;
  letter-spacing:.16em;text-transform:uppercase;color:var(--deep)}
.gov-kg{display:flex;justify-content:space-between;align-items:center;gap:6px}
.gov-kg>div{display:flex;align-items:center;gap:4px;min-width:0}
.gov-kg svg{flex:none;width:0.24in;height:0.24in;overflow:visible}
.gov-kg b{font-size:7.4pt;line-height:1.2;color:#1F2A2E;white-space:nowrap}
.gov-sh{display:flex;align-items:baseline;gap:0.12in;font:900 10.6pt/1.2 Merriweather,Georgia,serif;color:var(--c1);
  margin:0.08in 0 0.05in}
.gov-sh span{font:500 8.2pt Inter,sans-serif;color:#3B464C}
.gov-kinds{display:grid;grid-template-columns:repeat(3,1fr);gap:0.09in}
.gov-kc{display:flex;flex-direction:column;background:var(--tint);border:1px solid #D5E4E8;border-radius:8px;padding:0.05in 0.09in 0.06in}
.gov-kl.gov-kt2{margin-top:auto}
.gov-kh{display:flex;align-items:center;gap:7px;margin-bottom:3px}
.gov-mi{flex:none;width:0.36in;height:0.36in;background:#fff;border-radius:50%;box-shadow:0 0 0 1.3px #CFE0E4}
.gov-kh b{display:block;font:900 10.4pt/1.1 Merriweather,Georgia,serif;color:var(--deep)}
.gov-kh span{display:block;font-size:7.3pt;line-height:1.2;color:#4A555C}
.gov-kl{display:grid;grid-template-columns:0.5in 1fr;gap:4px;border-top:1px dashed #C9DADF;padding-top:2px;margin-top:2px}
.gov-kl i{font-style:normal;font:800 7pt/1.2 Inter,sans-serif;letter-spacing:.06em;text-transform:uppercase;color:var(--c1);padding-top:1px}
.gov-kl.gov-kf i{color:#9C2C22}
.gov-kl ul{margin:0;padding:0;list-style:none}
.gov-kl li{position:relative;padding-left:8px;font-size:7.6pt;line-height:1.26;color:#2B3236}
.gov-kl li::before{content:"";position:absolute;left:0;top:4px;width:4px;height:4px;border-radius:50%;background:var(--c2)}
.gov-kl.gov-kf li::before{background:#C9574B}
.gov-kl p{margin:0;font-size:7.6pt;line-height:1.26;font-weight:700;color:var(--deep)}
.gov-nums{display:grid;grid-template-columns:1fr 1.42in 1.42in 0.66in;gap:5px;margin-top:0.08in;align-items:stretch;
  border:1px solid #E8D9B6;background:#FFFCF4;border-radius:8px;padding:5px 6px}
.gov-nl{display:flex;align-items:center;gap:7px}
.gov-nl .ic{flex:none;color:var(--c1)}
.gov-nl b{display:block;font:900 9.6pt/1.2 Merriweather,Georgia,serif;color:var(--c1)}
.gov-nl span{display:block;font-size:7.5pt;line-height:1.28;color:#2B3236}
.gov-n{border-radius:5px;background:#F7EDD7;border-top:3px solid #D99A1E;padding:2px 6px 3px;color:#6E4A00}
.gov-n i{display:block;font:800 7pt Inter,sans-serif;letter-spacing:.07em;text-transform:uppercase;font-style:normal}
.gov-n b{display:block;font:800 8.6pt/1.15 Inter,sans-serif;color:#5B3C00}
.gov-n span{display:block;font-size:7.2pt;line-height:1.2;color:#6E5320}
.gov-mine{border:1.3px dashed #9AA5AC;border-radius:5px;display:flex;align-items:flex-start;justify-content:center;background:#fff}
.gov-mine span{font:700 7pt Inter,sans-serif;color:#6A747B;margin-top:2px}
.gov-alarm{display:flex;align-items:center;gap:7px;border:1.4px solid #C0392B;background:#FDF1EF;border-radius:7px;
  padding:2px 9px;margin-top:0.06in}
.gov-alarm .ic{flex:none;color:#B3362B}
.gov-alarm p{margin:0;font-size:7.7pt;line-height:1.3;color:#2B3236}
.gov-alarm b{color:#A5281E}
.gov-5r{display:grid;grid-template-columns:1.42in 1fr;gap:0.1in;align-items:center;margin-top:0.08in}
.gov-5rh b{display:block;font:900 10.6pt/1.15 Merriweather,Georgia,serif;color:var(--c1)}
.gov-5rh span{display:block;font-size:7.4pt;line-height:1.25;color:#4A555C;margin-top:1px}
.gov-5rh em{font-style:normal;font-weight:700;color:var(--deep)}
.gov-5rr{display:grid;grid-template-columns:repeat(5,1fr)}
.gov-5rr>div{position:relative;background:var(--soft);color:var(--deep);padding:4px 14px 4px 18px;min-height:0.42in;
  display:flex;flex-direction:column;justify-content:center;
  clip-path:polygon(0 0,calc(100% - 10px) 0,100% 50%,calc(100% - 10px) 100%,0 100%,10px 50%)}
.gov-5rr>div:first-child{clip-path:polygon(0 0,calc(100% - 10px) 0,100% 50%,calc(100% - 10px) 100%,0 100%);padding-left:9px}
.gov-5rr>div:nth-child(even){background:#D3E9EE}
.gov-5rr b{display:flex;align-items:center;gap:4px;font:800 8.2pt Inter,sans-serif;text-transform:uppercase;letter-spacing:.04em}
.gov-5rr b i{font-style:normal;display:inline-flex;align-items:center;justify-content:center;width:13px;height:13px;
  border-radius:50%;background:var(--c1);color:#fff;font:800 7pt/1 Inter,sans-serif}
.gov-5rr span{font-size:7pt;line-height:1.2;color:#3B464C}
.gov-5rr em{font-style:normal;font:800 7pt/1.15 Inter,sans-serif;letter-spacing:.04em;color:#B3362B;margin-top:1px}
.gov-5rr>div.gov-on{background:var(--c1);color:#fff}
.gov-5rr>div.gov-on b i{background:#fff;color:var(--c1)}
.gov-5rr>div.gov-on span{color:#E3F1F4}
/* the Paradex photo is a flat RGB image: blend its white ground into the column tint (this image only) */
.col .pick img[src$="nd-go-paradex.png"]{mix-blend-mode:multiply;filter:none}
.gov-5rr>div.gov-on em{color:#fff;background:#F15F3F;border-radius:3px;padding:1px 5px;align-self:flex-start;text-transform:uppercase}
"""


# ============================================================== the sheet
SHEET = {
    "slug": SLUG, "code": "ND-GI-104", "order": 11, "theme": "gut", "series": "Gut Health Series",
    "title": "Gut Overgrowth", "sub": "Yeast, parasites and SIBO",
    # [SENDER16] trillions of bacteria, almost all in the colon.  [ACG20] [MMC12] defences: stomach acid, the
    # fasting "housekeeper" waves, immunity.  [CANDIDA20] Candida is a normal resident.  [CDC-GIA] parasites.
    "intro": ("Your gut is home to trillions of microbes, and almost all of them live in the <b>colon</b> (large intestine). "
              "Stomach acid, the gut&rsquo;s sweeping waves and your immune system keep the <b>small intestine</b> nearly "
              "free of bacteria and keep yeast and parasites in check. When those defenses slip, microbes can "
              "<b>overgrow</b>: bacteria crowd the small intestine (<b>SIBO</b>), <b>Candida</b> yeast multiplies, or a "
              "<b>parasite</b> moves in. A test ordered by your provider shows which one is behind your symptoms."),
    "front": front,
    "css": CSS,
    "back": {
        "life_title": "Lifestyle Recommendations", "life_sub": "Starve it, sweep it, and keep new invaders out",
        "style": "circle",
        "life": [
            # [ND584] Remove step: sugar, alcohol, processed food out
            ("sugar", "Cut the sugar", "Skip added sugar, sweet drinks, alcohol and junk food during the plan."),
            # [MMC12] cleaning waves run only in the fasting state; [ND584] no food within 2 hours of bedtime
            ("clock", "Space your meals", "No grazing: the gut&rsquo;s cleaning waves run between meals. Stop eating 2 hours before bed."),
            # [CDC-GIA] prevention: hand washing, safe water, food hygiene
            ("drop", "Wash, cook, filter", "Wash hands and produce, cook meat through, and skip untreated lake or stream water."),
            # [ND584] "Avoid eating under stress. Eat slowly."
            ("plate", "Eat calm, chew well", "Slow, unhurried meals give stomach acid and enzymes a head start."),
            # [SU18] PPIs raise SIBO risk; stopping is a prescriber decision
            ("rx", "Review acid blockers", "They lower stomach acid, a key defense. Never stop one without your prescriber."),
        ],
        # Products: NutriDyn's own Remove-step picks.  GI-MAP protocol REMOVE line (Asher, Gmail 194b7cdf22b9133b,
        # 2025-01-30): "Nutricidin 1 softgel 3x daily away from probiotics; Spectrum BR 2 tabs 3x; ParaCleanse/Paradex
        # 1 cap 3x".  ND584 Remove = Spectrum BR (+ Spectrum AR, not in the product DB).  Kristi Hughes' NutriDyn grid
        # (Drive 1mbYXJNRcry81g...): Berberine Anti-microbial = Spectrum BR, Biofilm Aromatic Aid = NutriCidin,
        # Parasite Botanical = Paradex, BioToxin Binder = Binder Pro; "Sac B Anti-candida Probiotic" for Candida.
        # Mayfield 5R (GLC 2023): binders GI Defend, Binder Pro.  Facts and sources: products.d/gut-overgrowth.json.
        "cols": [
            {"p": "go_spectrum_br", "need": "Balance the flora", "needsub": "berberine, Oregon grape",
             "start": True, "dose": "dose_from_db",
             "bullets": ["Supports a healthy balance of gut bacteria and yeast",
                         "NutriDyn&rsquo;s Remove-step pick in the 5R plan"]},
            {"p": "go_nutricidin", "need": "Plant oils + enzyme", "needsub": "oregano oil and ginger",
             "dose": "dose_from_db",
             "bullets": ["Oregano oil and ginger support balanced gut flora",
                         "Adds a protein-digesting enzyme and EDTA"]},
            {"p": "go_paradex", "need": "Classic cleanse herbs", "needsub": "black walnut, wormwood",
             "dose": "dose_from_db",
             "bullets": ["Supports a healthy intestinal environment", "Five traditional cleanse herbs"]},
            {"p": "go_sboulardii", "need": "A friendly yeast", "needsub": "S. boulardii probiotic",
             "dose": "dose_from_db",
             "bullets": ["Supports a balanced gut microbiome",
                         "A yeast, so antibiotics do not wipe it out"]},
            {"p": "go_binder_pro", "need": "Bind and carry out", "needsub": "apple pectin, chlorella",
             "dose": "dose_from_db",
             "bullets": ["Binds unwanted compounds so they leave with the stool",
                         "Take apart from medicines and other pills"]},
        ],
        "rx": {
            "practitioner": [
                # [NAC17] [ACG20] testing; [CDC-GIA] [CDC-PIN] medicine for confirmed parasites
                "<b>Test, then treat.</b> A breath or stool test shows what is overgrown, so {who} can match the plan "
                "and decide how long you stay on it.",
                # Spectrum BR label: not in pregnancy or nursing; berberine and newborn jaundice (NCCIH/MedlinePlus)
                "<b>Pregnant or breastfeeding?</b> Skip Spectrum BR, Nutricidin and Paradex. These herbal formulas are "
                "not for pregnancy or nursing.",
                # Yin 2008 (berberine lowers glucose); Guo 2012 (CYP inhibition); garlic, pau d'arco bleeding cautions
                "<b>On diabetes medicine or a blood thinner?</b> Berberine adds to sugar-lowering drugs, and garlic and "
                "pau d&rsquo;arco can add to bleeding. Ask {who} first.",
            ],
            "pharmacy": [
                # Guo 2012 PMID 21870106; Yin 2008 PMID 18442638
                "<b>Berberine</b> (Spectrum BR) slows CYP3A4, 2D6 and 2C9 and adds to diabetes medicines. Bring your "
                "full medicine list.",
                # garlic and pau d'arco bleeding cautions; chlorella vitamin K and warfarin (MedlinePlus)
                "<b>Blood thinners:</b> garlic and pau d&rsquo;arco may add to bleeding, and chlorella (in Binder Pro) "
                "has vitamin K, which can weaken warfarin.",
                # Spectrum BR label (not in pregnancy or nursing); Enache-Angoulvant 2005 PMID 16267727 (catheters,
                # immune suppression); antifungal agents act on yeast, so they may inactivate S. boulardii
                "<b>Skip the herbs</b> in pregnancy or nursing. Skip <b>S. boulardii</b>, a live yeast, with a central IV "
                "line or weak immunity; antifungals may stop it working.",
            ],
        },
    },
}
