"""Gut Overgrowth: Yeast, Parasites and SIBO (ND-GI-104), Gut Health Series.

Self-contained sheet module: the front art, the front copy and the back data all live here.  Shared
helpers come from svgkit (T, svg) and kit (icon).  Every SVG id and CSS class starts with "gov" because
all sheets share one document in the bundle PDFs.  The back page is reached in CSS with
.sheet.back:has(.gov-back) (a marker span in the lifestyle title).

This is the REMOVE step of NutriDyn's 5R gut plan.  The Intestinal Permeability sheet (ND-GI-101) covers
Repair and Rebalance; the 5R ribbon on the front points there.  The ribbon uses NutriDyn's own names and
order from ND584 (Remove, Replace, Reinoculate, Repair, Retain), not the generic "Rebalance".

FRONT, top to bottom
  intro -> art: one front-view digestive tract in the centre (esophagus, stomach, the whole small
  intestine from duodenum to ileum as a pile of loops of different sizes, near loops passing over far
  ones and the far ones a little darker; the colon with its haustra from cecum to rectum, appendix).
  ONE lens on the small intestine and ONE on the sigmoid colon, each with two beams: the same spot shown
  BALANCED (left column) and OVERGROWN (right column); small intestine on top, colon below.  The SIBO
  circle is crowded with the colon's own (green) bacteria plus gas, because SIBO is colon bacteria in the
  wrong place [NAC17]; red "unfriendly" bacteria appear only in the colon circle.  The colon parasite is
  a pinworm, the worm that lives in the colon [CDC-PIN].  Organ names sit on the circle rims, and the figure
  itself names the stomach, the small intestine (pink loops, leader to the duodenum where it leaves the
  stomach) and the colon (tan pouched tube), each in clear space; each circle has a one-line caption.
  Zoom-circle symbols are placed by a seeded random fill that keeps every item clear of the others (rods are
  tested as capsules, hairs included), above the tallest villus tip in the small intestine, and clear of the
  organ tag on the rim.  The balanced colon holds one small yeast cell, because a little yeast is normal ->
  KEY (every symbol, same drawing code as the art, two rows) -> three kinds of overgrowth (SIBO, yeast,
  parasites: clues, risks, which test) -> breath test "know your numbers" strip (consensus cut-offs and a
  write-in box for each gas) -> red-flag line -> the 5R ribbon with Remove marked "this sheet".
Testing is always the practitioner's: the front says "your provider" in both editions (never {who}).
Anatomy notes: villi are drawn only in the small intestine; the colon lining is flat with crypts (the
colon has no villi).  The stomach sits on the viewer's right (the patient's left), the cecum and
appendix on the viewer's lower left, the splenic flexure higher than the hepatic flexure, and the
transverse colon passes in front of the duodenum.  The jejunum's loops start on the viewer's upper right
(the patient's upper left) and the ileum ends on the viewer's lower left at the cecum.

SOURCES (each fact on the page carries one of these tags in a comment next to it)
  [ACG20]   Pimentel M, Saad RJ, Long MD, Rao SSC. ACG Clinical Guideline: Small Intestinal Bacterial
            Overgrowth. Am J Gastroenterol 2020;115:165-178. PMID 32023228. doi:10.14309/ajg.0000000000000501
            (methane excess is renamed intestinal methanogen overgrowth, IMO: methane is made by archaea).
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
            is a regular gut resident in most people (so finding some in stool is normal, and there is no
            validated stool cut-off: the provider reads the result); dysbiosis, immune suppression and a
            weak barrier let it overgrow.  Candida grows as round budding cells and as chains of stretched
            cells (pseudohyphae and hyphae).
  [SAMONIS93] Samonis G et al. Antimicrob Agents Chemother 1993;37:51-53. PMID 8431017: broad-spectrum
            antibiotics raise gut yeast colonization.
  [CDC-CAND] CDC, Candidiasis (thrush; vaginal candidiasis): risk factors antibiotics, corticosteroids,
            diabetes, weakened immune system.  These are separate infections elsewhere that share those risk
            factors, not signs of gut yeast; there is no single gut sign.  So the card says only that they share
            the same risks.
  [CDC-GIA] CDC, Giardia: diarrhea, gas, greasy stools that can float, cramps; spread by untreated or
            recreational water, food, surfaces and people; diagnosed from stool samples.  CDC, Giardia and
            pets: the chance of getting Giardia from dogs or cats is small (people and pets usually carry
            different types), so "pets" is not listed as a risk.  Giardia lives in the small intestine.
  [CDC-PIN] CDC, Pinworm: most common worm infection in the US; adult worms live in the colon and rectum,
            females lay eggs on the skin around the anus at night (itching); spreads only between people
            (child care, households); diagnosed with a tape test (stool tests not recommended).
  [SCFA13]  den Besten G et al. J Lipid Res 2013;54:2325-40. PMID 23821742: colon bacteria ferment fiber.
  [ND584]   NutriDyn 5R GI Restoration Program ND584 Rev. 1/22: Remove, Replace, Reinoculate, Repair, then
            Restore & Retain; "The first 4 R's last 10 days and all four steps should be done at the same
            time. The final R is from day 11 to day 24." Remove-step diet (sugar, alcohol, processed
            food); "Avoid eating within 2 hours of bedtime"; "Avoid eating under stress. Eat slowly."
  [ALARM]   NIDDK, Diarrhea (see a doctor for blood or black stools, high fever, dehydration); ACG
            Clinical Guideline: Management of IBS, Lacy BE et al. Am J Gastroenterol 2021;116:17-44,
            PMID 33315591 (alarm features: bleeding, unintended weight loss).
  [LBT180]  Santos ANR et al. Rev Paul Pediatr 2020;38:e2018164, PMID 31939507: a lactulose breath test with
            hydrogen and methane read for 180 minutes.  With [NAC17] (SIBO testing can stop at 2 hours) the
            front says "2 to 3 hours".
  [DPDX-PIN] CDC DPDx, Enterobiasis: adult female pinworms are 8 to 13 mm long, males 2 to 5 mm (not
            re-opened this session: cdc.gov is outside the allowed network), so the KEY says "about 1 cm".
  Back-page safety notes (both editions): labels opened 2026-11-03: Spectrum BR ND505 Rev. 8/24
  "Warning: Do not use if pregnant or nursing" and "If taking medication including cyclosporine, consult your
  healthcare practitioner"; Nutricidin ND949 Rev. 2/25, UltraBiotic S. boulardii ND170 Rev. 8/25 and Binder
  Pro ND1141 Rev. 12/25 "If you are pregnant, nursing, or taking medication, consult your healthcare
  practitioner"; Paradex retail listings (web search, label not opened) "Not to be used by pregnant or
  lactating women" and "may contain traces of tree nuts".  Berberine CYP3A4/2D6/2C9 inhibition, Guo Y et
  al. Eur J Clin Pharmacol 2012;68:213-7, PMID 21870106; berberine lowers blood sugar like metformin, Yin J
  et al. Metabolism 2008;57:712-7, PMID 18442638; invasive Saccharomyces infection, central venous catheters
  and immune suppression the main risks, Enache-Angoulvant A, Hennequin C. Clin Infect Dis
  2005;41:1559-68, PMID 16267727; S. boulardii is a yeast, so antibacterial antibiotics do not kill it and
  antifungals can, Kelesidis T, Pothoulakis C. Ther Adv Gastroenterol 2012;5:111-25, PMID 22423260.
  Bleeding: ginger (in the Spectrum BR blend, ND505, and in Nutricidin), clove and garlic are among the herbs
  that may raise bleeding risk with warfarin, Heck AM
  et al. Am J Health Syst Pharm 2000;57:1221-7, PMID 10902065; serratiopeptidase breaks down fibrin
  (anticoagulant, fibrinolytic), Hosseini SB et al. Arch Microbiol 2024;206:180, PMID 38502196 and Jadhav SB
  et al. Biotechnol Rep 2020;28:e00544, PMID 33134103; pau d'arco's lapachol blocks vitamin K recycling
  as warfarin does, Preusch PC et al. Arch Biochem Biophys 1989;269:18-24, PMID 2916837; chlorella vitamin K
  and warfarin (MedlinePlus chlorella monograph; not re-opened this session).  Licorice (in the Spectrum BR
  blend, ND505; not DGL): glycyrrhizin raises blood pressure and lowers potassium (apparent mineralocorticoid
  excess), Deutch MR et al. Foods 2019;8:495, PMID 31615045; Kwon YJ et al. J Med Food 2020;23:12-20, PMID
  31874059; so the pharmacy edition flags diuretics, digoxin and steroids and the provider edition's lead names
  high blood pressure.  Warfarin: berberine slows CYP2C9 (Guo 2012), the enzyme that clears S-warfarin, Kaminsky
  LS, Zhang ZY. Pharmacol Ther 1997;73:67-74, PMID 9014207, so both blood-thinner lines name Spectrum BR and the
  pharmacy edition lists warfarin beside cyclosporine.  Children: every label dose is an
  adult dose, and berberine displaces bilirubin and is best avoided in jaundiced newborns, Chan E. Biol
  Neonate 1993;63:201-8, PMID 8513024, so both editions say "ask first" for a child.
  Plan length: ND584 runs the Remove step 10 days within a 24-day program; Chedid 2014 (below) gave herbal
  therapy for 4 weeks and retested, so "often a few weeks, then may retest".
  Research anchors behind the product picks (not quoted on the page): Chedid V et al. Glob Adv Health
  Med 2014;3:16-24, PMID 24891990 (herbal therapy incl. CandiBactin-BR, which Spectrum BR matches);
  Redondo-Cuevas L et al. Nutrients 2024;16:1083, PMID 38613116; Bustos Fernandez LM et al. Dig Dis
  2023;41:798-809, PMID 36630947 (S. boulardii CNCM I-745, a different strain).
"""
import math
import os
import random

from kit import icon
from svgkit import T, label_bg, svg

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
OVER_E = "#8E231B"                        # unfriendly bacteria: red rods with short hairs
YEAST_E = "#4A3290"                       # yeast (Candida): purple budding cells and chains
GAS, GAS_E = "#F6C84A", "#B98A12"         # gas (hydrogen, methane): gold bubbles
WORM_E = "#6E5C42"                        # parasite: a thin white pinworm
VIL, VIL_E = "#F6C0AE", "#C0735E"         # villi
SI, SI_E, SI_HI = "#F4BBA6", "#B86E5B", "#FDE4DA"      # small intestine, near loops
SI_F, SI_FE, SI_FHI = "#E7A28D", "#A35A48", "#F5CDBF"  # small intestine, far loops (a little darker)
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


def _mix(c1, c2, t):
    """Blend two #RRGGBB colours (t = 0 gives c1, 1 gives c2)."""
    t = min(max(t, 0.0), 1.0)
    a = [int(c1[i:i + 2], 16) for i in (1, 3, 5)]
    b = [int(c2[i:i + 2], 16) for i in (1, 3, 5)]
    return "#" + "".join(f"{round(x + (y - x) * t):02X}" for x, y in zip(a, b))


# ============================================================== symbols (drawn centred on x, y)
def rod(x, y, rot=0.0, kind="ok", L=12.5, w=5.4):
    """One rod-shaped bacterium.  kind ok = friendly (smooth green); bad = unfriendly (red, short hairs:
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
    """A gas bubble (hydrogen or methane made by microbes).  Solid fill, so nothing behind it ghosts through."""
    return (f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r:.1f}" fill="{GAS}" stroke="{GAS_E}" stroke-width="1"/>'
            f'<circle cx="{x - r * .36:.1f}" cy="{y - r * .36:.1f}" r="{max(r * .26, .9):.1f}" fill="#FFFFFF" opacity=".85"/>')


def _worm_line(L, bend, n=36):
    return [(L * (i / n - 0.5), bend * 3.2 * math.sin(math.pi * (1.5 * i / n - 0.25))) for i in range(n + 1)]


def pinworm(x, y, rot=0.0, s=1.0, L=56.0, w=3.9, bend=1.8, sw=1.0):
    """A pinworm (Enterobius), the worm that lives in the colon [CDC-PIN]: thin and white, a blunt head with
    the small swelling and the round food bulb pinworms have behind it, and a long, finely pointed tail (the
    female, the one that lays the eggs).  Drawn head left, centred on x, y; sw is the outline width as
    printed, whatever the scale."""
    cl = _worm_line(L, bend)
    n = len(cl) - 1
    ns = _normals(cl)

    def half(t):
        if t < 0.06:                                   # rounded head
            return w / 2 * (0.3 + 0.7 * math.sqrt(t / 0.06))
        if t < 0.15:                                   # the small head swelling
            return w / 2 * (1.0 + 0.14 * math.sin(math.pi * (t - 0.06) / 0.09))
        if t < 0.7:
            return w / 2
        f = min((t - 0.7) / 0.3, 1.0)                  # long, finely pointed tail
        return w / 2 * max(0.04, (1 - f) ** 1.15)

    left = [(p[0] + q[0] * half(i / n), p[1] + q[1] * half(i / n)) for i, (p, q) in enumerate(zip(cl, ns))]
    right = [(p[0] - q[0] * half(i / n), p[1] - q[1] * half(i / n)) for i, (p, q) in enumerate(zip(cl, ns))]
    nose = (cl[0][0] - w * 0.12, cl[0][1])
    body = _smooth_d([nose] + left + right[::-1], closed=True)
    gut = _poly(cl[8:25])
    shine = _poly([(p[0] + q[0] * w * 0.2, p[1] + q[1] * w * 0.2) for p, q in zip(cl[2:19], ns[2:19])])
    bx, by = cl[5]
    ang = math.degrees(math.atan2(cl[6][1] - cl[4][1], cl[6][0] - cl[4][0]))
    k = sw / s
    return (f'<g transform="translate({x:.1f},{y:.1f}) rotate({rot:.0f}) scale({s})">'
            f'<path d="{body}" fill="url(#{U}-wm)" stroke="{WORM_E}" stroke-width="{k:.2f}" stroke-linejoin="round"/>'
            f'<path d="{gut}" fill="none" stroke="#D6C9AB" stroke-width="{0.7 * k:.2f}" stroke-linecap="round"/>'
            f'<ellipse cx="{bx:.1f}" cy="{by:.1f}" rx="{w * 0.42:.1f}" ry="{w * 0.27:.1f}" transform="rotate({ang:.0f} {bx:.1f} {by:.1f})" '
            f'fill="#E3D5B6" stroke="#AD9670" stroke-width="{0.5 * k:.2f}"/>'
            f'<path d="{shine}" fill="none" stroke="#FFFFFF" stroke-width="{0.9 * k:.2f}" stroke-linecap="round" opacity=".95"/></g>')


def _worm_spots(x, y, rot, s=1.0, L=56.0, bend=1.8):
    """Circles that cover a pinworm, so other symbols are placed clear of it (circle-relative coords)."""
    a = math.radians(rot)
    out = []
    for px, py in _worm_line(L, bend, 10):
        out.append((x + s * (px * math.cos(a) - py * math.sin(a)), y + s * (px * math.sin(a) + py * math.cos(a)), 3.8 * s))
    return out


def _yeast_spots(x, y, rot=0.0, s=1.0, bud=True):
    """Circles that cover a budding yeast cell as drawn by yeast() (mother cell and bud, outlines included), so
    other symbols are placed clear of it (circle-relative coords)."""
    out = [(x, y, 7.2 * s)]
    if bud:
        a = math.radians(rot)
        bx, by = 7.3 * s, -2.6 * s
        out.append((x + bx * math.cos(a) - by * math.sin(a), y + bx * math.sin(a) + by * math.cos(a), 4.2 * s))
    return out


def villus(x, base, h, tilt=0.0, w=8.2):
    """One finger-like villus rising from `base` (y) to a rounded tip h above it."""
    r = w / 2
    return (f'<g transform="rotate({tilt:.1f} {x:.1f} {base:.1f})">'
            f'<path d="M{x - r:.1f},{base + 3:.1f} V{base - h + r:.1f} A{r:.1f},{r:.1f} 0 0 1 {x + r:.1f},{base - h + r:.1f} '
            f'V{base + 3:.1f} Z" fill="url(#{U}-vi)" stroke="{VIL_E}" stroke-width=".8"/>'
            f'<path d="M{x:.1f},{base:.1f} V{base - h + 6:.1f}" stroke="#FDE6DD" stroke-width="1.3" stroke-linecap="round" '
            'opacity=".9"/></g>')


def crypts(x0, x1, top, bottom, k0=0, gap=11.5, depth=19):
    """The flat colon lining (no villi) from x0 to x1 with crypt openings, between y = top and y = bottom."""
    edge = [(min(x0 + k * 6, x1), top + 1.4 * math.sin((k + k0) * 0.9)) for k in range(int((x1 - x0) / 6) + 2)]
    o = [f'<path d="{_poly(edge)} V{bottom} H{x0} Z" fill="url(#{U}-cw)" stroke="#C27A5F" stroke-width="1"/>']
    x = x0 + 8.0
    while x < x1 - 2:
        yy = top + 1.4 * math.sin(((x - x0) / 6 + k0) * 0.9) + 1
        o.append(f'<rect x="{x - 2.3:.1f}" y="{yy:.1f}" width="4.6" height="{depth}" rx="2.3" fill="#D68C72"/>'
                 f'<ellipse cx="{x:.1f}" cy="{yy + 1:.1f}" rx="2.6" ry="1.3" fill="#B96D55"/>')
        x += gap
    return "".join(o)


# ============================================================== the digestive tract (local 300 x 360 box)
# Front view, as if facing the person: their right side is on the viewer's left.
# The esophagus bends into the cardia and ends well inside the stomach outline (the stomach is drawn over it),
# so both of its edges meet the stomach and no cut end shows beside it.
ESO = [(152, -2), (156, 26), (163, 48), (172, 63), (184, 74)]
STOMACH = [(171, 66), (178, 55), (194, 47), (214, 49), (231, 61), (242, 82), (245, 108), (239, 134), (224, 156),
           (201, 171), (174, 176), (149, 170), (131, 160), (120, 152), (116, 146), (121, 140), (136, 143),
           (153, 143), (168, 134), (176, 116), (176, 95), (172, 80)]
COLON = [(60, 302), (55, 288), (53, 270), (53, 248), (54, 226), (56, 204), (60, 185), (67, 171), (79, 163),
         (97, 166), (117, 176), (141, 186), (166, 190), (192, 186), (216, 176), (238, 162), (256, 151), (271, 147),
         (281, 153), (285, 167), (285, 190), (284, 214), (282, 238), (279, 260), (273, 278), (262, 292),
         (246, 301), (226, 305), (208, 301), (192, 302), (179, 310), (170, 321), (165, 333), (163, 343), (162, 350)]
# The small intestine as ONE tube: the duodenum (start tucked inside the stomach, round the C-loop behind the
# transverse colon), then the jejunum's loops on the viewer's upper right, then the ileum's loops on the left,
# ending under the cecum at the ileocecal valve.  Loops differ in size and direction, one loop lies across
# another, and none of the rows repeat.  Index numbers are used by SI_DEPTH.
SI_PATH = [
    (130, 150), (118, 148), (104, 150), (94, 159), (90, 176), (93, 192), (104, 202), (122, 207), (146, 206),  # 0-8
    (170, 201), (192, 196), (209, 199), (226, 202), (244, 207), (257, 219), (254, 233), (238, 238),           # 9-16
    (219, 233), (202, 226), (189, 226), (182, 237), (182, 251), (191, 259), (208, 257), (226, 252),           # 17-24
    (244, 252), (258, 260), (262, 274), (251, 284), (232, 286), (213, 281), (196, 279), (181, 287),           # 25-32
    (164, 294), (144, 295), (125, 289), (112, 276), (116, 261), (133, 253), (156, 250), (175, 244),           # 33-40
    (183, 230), (174, 216), (156, 210), (134, 209), (112, 213), (91, 224), (80, 240), (82, 257), (79, 272),   # 41-49
    (72, 283), (67, 289), (63, 291)]                                                                         # 50-52
# depth along the tube (0 = far, drawn first and a little darker; 1 = near), keyed by SI_PATH index
SI_DEPTH = {0: 0.0, 11: 0.0, 19: 0.1, 22: 0.35, 26: 0.3, 32: 0.25, 36: 0.5, 39: 1.0, 42: 1.0, 45: 0.7, 52: 0.8}
# far loops seen through the gaps between nearer loops; every arm ends ON the centre line of the nearer loop
# that hides it, so no cut end shows
SI_GAPS = [
    [(110, 213), (106, 225), (114, 237), (129, 240), (140, 229), (137, 209)],      # hangs from under the top-left arc
    [(129, 290), (130, 279), (141, 270), (155, 272), (161, 284), (158, 294)],      # rises from under the bottom arc
    [(266, 268), (247, 267), (229, 270), (211, 270), (198, 264), (191, 259)],      # between the right-hand loops
]
SI_LENS = (146, 251)          # zoom spot on a near loop of the small intestine (local coordinates)
CO_LENS = (214, 302)          # zoom spot on the sigmoid colon, bottom centre


def _depth(k, anchors):
    """Depth at fractional path index k: smoothstep between the anchors."""
    ks = sorted(anchors)
    if k <= ks[0]:
        return anchors[ks[0]]
    for a, b in zip(ks, ks[1:]):
        if k <= b:
            f = (k - a) / (b - a)
            return anchors[a] + (anchors[b] - anchors[a]) * f * f * (3 - 2 * f)
    return anchors[ks[-1]]


def _tube_chunks(center, anchors=None, const=0.0, step=6):
    """Cut a tube along `center` into short chunks tagged with a depth.  Drawn far to near, every chunk has its
    own outline, so a nearer loop passes over a farther one with a clean edge.  Outline, fill and highlight
    reach 1, 2 and 3 samples into the neighbouring chunks, so the joins leave no seam."""
    per = 10
    dense = _cr(center, per=per)
    cum = [0.0]
    for a, b in zip(dense, dense[1:]):
        cum.append(cum[-1] + math.hypot(b[0] - a[0], b[1] - a[1]))
    wp = [cum[k * per] for k in range(len(center))]          # arc length at each waypoint
    pts, ss = _resample(dense, 1.5)
    n = len(pts)

    def k_of(s):
        for k in range(len(wp) - 1):
            if s <= wp[k + 1]:
                return k + (s - wp[k]) / max(wp[k + 1] - wp[k], 1e-6)
        return len(wp) - 1

    out = []
    for i in range(0, n - 1, step):
        sl = [pts[max(i - e, 0):min(i + step + e + 1, n)] for e in (1, 2, 3)]
        d = const if anchors is None else _depth(k_of(ss[min(i + step // 2, n - 1)]), anchors)
        out.append((d, i, *sl))
    return out


def _small_intestine(w=11.6, ew=1.2):
    chunks = _tube_chunks(SI_PATH, SI_DEPTH)
    for g, gap in enumerate(SI_GAPS):
        chunks += [(-0.01, 10 ** 6 * (g + 1) + c[1]) + c[2:] for c in _tube_chunks(gap)]
    o = []
    for d, _i, se, sf, sh in sorted(chunks, key=lambda c: (round(c[0], 3), c[1])):
        fill, edge = _mix(SI_F, SI, d), _mix(SI_FE, SI_E, d)
        hi = _mix(fill, _mix(SI_FHI, SI_HI, d), .75)       # solid colour, so overlapping chunks never stack up
        o.append(f'<path d="{_poly(se)}" fill="none" stroke="{edge}" stroke-width="{w + 2 * ew:.1f}" stroke-linejoin="round"/>'
                 f'<path d="{_poly(sf)}" fill="none" stroke="{fill}" stroke-width="{w}" stroke-linejoin="round"/>'
                 f'<path d="{_poly(sh)}" fill="none" stroke="{hi}" stroke-width="{w * .32:.1f}" stroke-linejoin="round"/>')
    return "".join(o)


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
    # white ground inside the colon frame, so the zoom beams' soft fill shows only outside the organs.  It runs on
    # past the frame's open bottom (cecum to rectum, under the lowest small-intestine loop) to y = 322: the colon
    # beam's lower edge crosses that gap at y = 312 to 313, so no grey sliver of it shows between the cecum, the
    # appendix and the rectum.  The added edge lies inside the cecum and rectum or below the beam (white on white).
    o = [f'<path d="{_smooth_d(COLON[:-4] + [(176, 322), (62, 322)])}" fill="#FFFFFF"/>']
    # esophagus (fades in at the top: the throat is above the picture)
    eso = _poly(_cr(ESO, per=12))
    o.append(f'<path d="{eso}" fill="none" stroke="url(#{U}-esoE)" stroke-width="13.4" stroke-linecap="butt"/>'
             f'<path d="{eso}" fill="none" stroke="url(#{U}-esoF)" stroke-width="11" stroke-linecap="butt"/>')
    # small intestine (duodenum, jejunum, ileum) sits behind the stomach and the colon
    o.append(_small_intestine())
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


def _in_circle(R, top_cut, tag_half=0.0):
    """Region test: inside the circle (with margin), above the lining at y = top_cut, and clear of the organ tag
    on the top rim (the tag covers |x| < tag_half down to 8.5 below the rim, so nothing hides under it)."""
    def ok(x, y, r):
        if math.hypot(x, y) >= R - r - 3 or y >= top_cut - r - 1:
            return False
        return not (abs(x) < tag_half + r + 1.5 and y < -R + 10.5 + r)
    return ok


def _seg_dist(p, a, b):
    """Distance from point p to the segment a-b."""
    dx, dy = b[0] - a[0], b[1] - a[1]
    L2 = dx * dx + dy * dy
    t = 0.0 if L2 == 0 else max(0.0, min(1.0, ((p[0] - a[0]) * dx + (p[1] - a[1]) * dy) / L2))
    return math.hypot(p[0] - a[0] - t * dx, p[1] - a[1] - t * dy)


def _segs_dist(a1, a2, b1, b2):
    """Distance between the segments a1-a2 and b1-b2 (0 when they cross)."""
    def side(p, q, r):
        return (q[0] - p[0]) * (r[1] - p[1]) - (q[1] - p[1]) * (r[0] - p[0])
    if (side(b1, b2, a1) > 0) != (side(b1, b2, a2) > 0) and (side(a1, a2, b1) > 0) != (side(a1, a2, b2) > 0):
        return 0.0
    return min(_seg_dist(a1, b1, b2), _seg_dist(a2, b1, b2), _seg_dist(b1, a1, a2), _seg_dist(b2, a1, a2))


ROD_L, ROD_W = 12.5, 5.4


def _rod_capsule(x, y, rot, kind):
    """The capsule a rod covers as printed: its axis end points and radius.  A friendly rod is its rounded body
    plus the outline stroke (0.4 outside); an unfriendly rod's capsule also takes in its short hairs (2.6 past
    the body on both long sides, 0.85 wide)."""
    hl, rr = (2.2, ROD_W / 2 + 2.6 + 0.45) if kind == "bad" else (ROD_L / 2 - ROD_W / 2, ROD_W / 2 + 0.4)
    a = math.radians(rot)
    c, s = math.cos(a) * hl, math.sin(a) * hl
    return (x - c, y - s), (x + c, y + s), rr


def _place_rods(rng, n, kind, ok, taken, rods, gap=0.5, tries=30000):
    """Random rods (x, y, rot) inside ok(), tested as capsules: clear of every circle in `taken` and of every
    rod already in `rods` (which this extends) by `gap` of white space, so no two rods touch, not even end to
    end.  Each count below is what fits, so no rod is silently dropped."""
    out = []
    for _ in range(n):
        for _t in range(tries):
            x, y, rot = rng.uniform(-80, 80), rng.uniform(-80, 80), float(round(rng.uniform(0, 180)))
            p1, p2, rr = _rod_capsule(x, y, rot, kind)
            if not (ok(*p1, rr) and ok(*p2, rr) and ok(x, y, rr)):
                continue
            if any(_seg_dist((a, b), p1, p2) < rb + rr + gap for a, b, rb in taken):
                continue
            if any(_segs_dist(p1, p2, q1, q2) < rr + rq + gap for q1, q2, rq in rods):
                continue
            rods.append((p1, p2, rr))
            out.append((x, y, rot))
            break
    if len(out) < n:
        print(f"WARNING {SLUG}: only {len(out)} of {n} {kind} rods fit in a zoom circle")
    return out


def _tag_half(text):
    """Half the width of an organ tag on a circle rim (see _tag), stroke included."""
    return (tw(text, 10.5, 800, 1.0) + 2 * 17 * 0.62) / 2 + 0.65


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
    tips = floor - 31                     # the top of the tallest villus: every symbol sits above this line
    if not over:
        for (dx, dy, a) in [(-30, -30, 18), (14, -44, -28), (36, -16, 40), (-6, -14, -12)]:   # all 5+ clear of the villi
            o.append(rod(cx + dx, cy + dy, a, "ok"))
        return "".join(o)
    # SIBO: the colon's own (friendly, green) bacteria crowd in and ferment food into gas [NAC17].  The big
    # bubbles go first and join `taken` before the small ones are placed, so no two bubbles overlap.  Bubbles
    # and rods all stay above the villus tips (rods tested as capsules), so nothing lies across the villi.
    th = _tag_half("SMALL INTESTINE")
    taken = []
    big = _place(rng, 4, 6.2, _in_circle(R, tips, th), taken, 3)
    taken += big
    small = _place(rng, 7, 3.6, _in_circle(R, tips, th), taken, 2.4)
    taken += small
    clear = [(x, y, r + 0.5) for x, y, r in taken]          # the bubbles' outline stroke
    crowd = _place_rods(rng, 12, "ok", _in_circle(R, tips + 1, th), clear, [])   # 12: every one fits above the tips
    for x, y, a in crowd:
        o.append(rod(cx + x, cy + y, a, "ok"))
    for x, y, r in big + small:
        o.append(bubble(cx + x, cy + y, r))
    return "".join(o)


def colon_zoom(cx, cy, R, over):
    rng = random.Random(53 if over else 29)
    floor = R * 0.46
    th = _tag_half("COLON")
    o = [f'<rect x="{cx - R}" y="{cy - R}" width="{2 * R}" height="{2 * R}" fill="url(#{U}-lc)"/>',
         crypts(cx - R - 4, cx + R + 4, cy + floor, cy + R + 4)]     # flat lining with crypts (no villi)
    if not over:
        # [CANDIDA20] a little yeast is normal: one small budding cell rests on the lining among the friendly
        # colony, so the picture never teaches that any yeast at all is overgrowth (the Yeast card says the same)
        yx, yy, ya, ys = 14, floor - 6, -12, 0.7
        o.append(yeast(cx + yx, cy + yy, ya, ys))
        good = _place_rods(rng, 44, "ok", _in_circle(R, floor, th), _yeast_spots(yx, yy, ya, ys), [])  # all 44 fit
        for x, y, a in good:
            o.append(rod(cx + x, cy + y, a, "ok"))
        return "".join(o)
    # overgrowth: yeast cells and chains on the lining, a pinworm, fewer friendly and some unfriendly bacteria
    taken = []
    wx, wy, wr = 8, -16, 6
    o.append(pinworm(cx + wx, cy + wy, wr, 1.0))
    taken += _worm_spots(wx, wy, wr)
    for (dx, a, s) in [(-38, -96, 1.0), (-8, -78, 0.95)]:
        o.append(hypha(cx + dx, cy + floor - 1, a, 3, s))
        taken += [(dx + 4 * math.cos(math.radians(a)) * k, floor - 6 * k, 6) for k in range(1, 6)]
    for (dx, dy, a, s, b) in [(-24, -6, 15, 1.0, True), (6, -5, -20, 0.95, True), (44, -6, 30, 0.9, False),
                              (-50, -8, -10, 0.9, True), (24, -8, 40, 0.85, True)]:
        o.append(yeast(cx + dx, cy + floor + dy, a, s, b))
        taken.append((dx, floor + dy, 8.5 * s))
    for (dx, dy, r) in [(-18, -40, 4.2), (34, -42, 3.2)]:
        o.append(bubble(cx + dx, cy + dy, r))
        taken.append((dx, dy, r + 0.5))
    rods = []
    ok = _in_circle(R, floor - 16, th)
    bad = _place_rods(rng, 9, "bad", ok, taken, rods)        # the hairy rods first: they need the most room
    good = _place_rods(rng, 14, "ok", ok, taken, rods)
    for x, y, a in good:
        o.append(rod(cx + x, cy + y, a, "ok"))
    for x, y, a in bad:
        o.append(rod(cx + x, cy + y, a, "bad"))
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
TOP = 4                                # top margin above the column headers


def defs_svg():
    g = []
    lin = lambda i, a, b, x2=0, y2=1: (f'<linearGradient id="{U}-{i}" x1="0" y1="0" x2="{x2}" y2="{y2}">'
                                        f'<stop offset="0" stop-color="{a}"/><stop offset="1" stop-color="{b}"/></linearGradient>')
    g.append(lin("rok", "#9EDDAE", "#3D9B5C"))
    g.append(lin("rbad", "#F49A8A", "#C93A2D"))
    g.append(f'<radialGradient id="{U}-ye" cx=".38" cy=".34" r=".75"><stop offset="0" stop-color="#C8B5EE"/>'
             '<stop offset="1" stop-color="#7556BE"/></radialGradient>')
    g.append(lin("wm", "#FFFFFF", "#E4D7BD"))
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


def _organ_label(lines, x, y, anchor, p0, p1, size=11, lh=12.5):
    """An organ name in clear space on a white backdrop (svgkit.label_bg), styled like "Stomach", with a thin
    leader from p0 to the organ at p1.  Lines stack down from the first baseline y; anchor is start or end."""
    w = max(tw(s, size, 700) for s in lines)
    x0 = x - w if anchor == "end" else x
    top = y - size * 0.8
    h = size * 0.8 + (len(lines) - 1) * lh + size * 0.25
    return (label_bg(round(x0 - 3, 1), round(top - 2.5, 1), round(w + 6, 1), round(h + 5, 1), rx=4)
            + f'<path d="M{p0[0]:.1f},{p0[1]:.1f} L{p1[0]:.1f},{p1[1]:.1f}" stroke="#7B848A" stroke-width="1.1" '
              'stroke-linecap="round"/>'
            + "".join(T(x, round(y + i * lh, 1), s, size, 700, INK2, anchor) for i, s in enumerate(lines)))


def art_overgrowth():
    gl = lambda p: (FX + p[0] * FS, FY + p[1] * FS)
    o = [defs_svg()]
    si_l, co_l = gl(SI_LENS), gl(CO_LENS)
    # one lens per organ, two beams from each: the same spot, balanced (left) and overgrown (right).
    # Beam fills go behind the organs, then the figure, beam edges in front, lenses, then the zoom circles.
    beams = [beam(si_l, 8.5, (LX, SY), R * 0.6), beam(si_l, 8.5, (RX, SY), R * 0.6),
             beam(co_l, 8.5, (LX, CY), R * 0.6), beam(co_l, 8.5, (RX, CY), R * 0.6)]
    o.append("".join(f for f, _ in beams))
    o.append(f'<g transform="translate({FX:.1f},{FY}) scale({FS})">{figure()}</g>')
    o.append("".join(ln for _, ln in beams))
    o.append(lens(*si_l, 8.5) + lens(*co_l, 8.5))
    o.append(zoom(LX, SY, R, si_zoom, False, "a") + zoom(RX, SY, R, si_zoom, True, "b"))
    o.append(zoom(LX, CY, R, colon_zoom, False, "c") + zoom(RX, CY, R, colon_zoom, True, "d"))
    # column headers (with a top margin), organ tags on the circle rims, and what each circle shows
    o.append(_pill(LX, TOP, "BALANCED", OK, h=21) + _pill(RX, TOP, "OVERGROWTH", BAD, h=21))
    for cx in (LX, RX):
        o.append(_tag(cx, SY - R, "SMALL INTESTINE") + _tag(cx, CY - R, "COLON"))
    # [NAC17] SIBO = bacteria normally found in the large intestine, in the small intestine.  Each caption is
    # short enough to sit centred under its circle, clear of the zoom beams (the gas is named in the KEY).
    subs = [(LX, SY, "only a few bacteria", OK_TX), (RX, SY, "colon bacteria move in", BAD_TX),
            (LX, CY, "a thick, friendly colony", OK_TX), (RX, CY, "yeast and parasites take hold", BAD_TX)]
    for cx, cy, s, col in subs:
        half = tw(s, 11.2, 700) / 2 + 1.5           # +1.5: the italic runs a little wider than the upright face
        x = min(max(cx, 6 + half), W - 6 - half)
        o.append(T(round(x, 1), cy + R + 15.5, s, 11.2, 700, col, "middle", italic=True))
    # The figure names its organs, each in clear space on a white backdrop, so the pink small intestine and the
    # tan colon can be told apart without tracing a beam.  Stomach: leader to the greater curvature.  Small
    # intestine: above the left beam, leader to the duodenum where it leaves the stomach (above the transverse
    # colon).  Colon: in the pocket between the two right-hand beams, leader to the descending colon.
    sx, sy = gl((246, 92))
    o.append(f'<path d="M{sx - 4:.1f},{sy:.1f} H{sx + 13:.1f}" stroke="#7B848A" stroke-width="1.1"/>'
             + T(sx + 17, sy + 3.9, "Stomach", 11, 700, INK2))
    o.append(_organ_label(["Small intestine"], 306, 121, "end", (309, 120.5), gl((107, 146))))
    o.append(_organ_label(["Colon", "(large intestine)"], 507, 208.5, "start", (504, 205), (gl((284, 213))[0] + 7.5, 205)))
    return svg(W, H, "".join(o), "The digestive tract, with the stomach, the small intestine (pink loops) and the colon "
               "(tan pouched tube) labelled, and one spot in the small intestine and one spot in the colon shown "
               "up close. Balanced: only a few bacteria in the small intestine and a thick friendly colony with one "
               "small yeast cell in the colon. "
               "Overgrowth: the colon's own bacteria crowd the small intestine and make gas bubbles, and in the colon yeast "
               "cells and chains, a pinworm and some unfriendly bacteria take hold.")


# ============================================================== KEY (HTML, same drawing code as the art)
def _sw(markup, vb=30, wide=False):
    h = vb / 2
    if wide:
        return f'<svg class="{U}-kw" viewBox="{-h * 1.5} {-h} {vb * 1.5} {vb}" aria-hidden="true">{markup}</svg>'
    return f'<svg viewBox="{-h} {-h} {vb} {vb}" aria-hidden="true">{markup}</svg>'


def key_html():
    vil = (f'<rect x="-14" y="5" width="28" height="10" fill="url(#{U}-ti)"/>'
           + villus(-7.5, 7, 17, -3, 6.6) + villus(0, 7, 19, 0, 6.6) + villus(7.5, 7, 16, 4, 6.6))
    lining = crypts(-14, 14, 0, 14, 0, 9.5, 12)
    spot = (_tube_stroke([(-8.5, 2), (8.5, 2)], 9, SI, SI_E, SI_HI) + lens(0, 2, 7.2))
    items = [
        (_sw(rod(0, 0, -30, "ok", 15, 6.2)), "Friendly bacteria"),
        (_sw(rod(0, 0, -30, "bad", 15, 6.2)), "Unfriendly bacteria"),
        (_sw(bubble(-4, 3, 6.5) + bubble(6, -5, 4)), "Gas: hydrogen, methane"),
        (_sw(yeast(-11, 3, -10, 0.95) + hypha(2, 12, -62, 3, 0.62), wide=True), "Yeast (Candida): cells and chains"),
        # [DPDX-PIN] an adult female pinworm is 8 to 13 mm: drawn far smaller than life next to the bacteria,
        # so the KEY gives its real size (parents may look for them at night)
        (_sw(pinworm(0, 0, -22, 0.48, w=4.6, sw=0.85)), "Parasite (pinworm, about 1 cm)"),
        (_sw(vil), "Villi: small-intestine lining"),
        (_sw(lining), "Colon lining (no villi)"),
        (_sw(spot), "Zoomed spot"),
    ]
    cells = "".join(f'<div>{sw}<b>{a}</b></div>' for sw, a in items)
    return f'<div class="{U}-key"><span class="{U}-kt">Key</span><div class="{U}-kg">{cells}</div></div>'


# ============================================================== three kinds of overgrowth
def _mini(markup, vb=34):
    h = vb / 2
    return f'<svg class="{U}-mi" viewBox="{-h} {-h} {vb} {vb}" aria-hidden="true">{markup}</svg>'


KINDS = [
    (_mini(rod(-6, -6, 20, "ok") + rod(6, 2, -35, "ok") + rod(-4, 8, 60, "ok") + bubble(8, -9, 4.2) + bubble(-11, 4, 3)),
     # [NAC17] SIBO = too many microbes "normally found in the large intestine" in the small bowel
     "SIBO", "small intestinal bacterial overgrowth",
     # [ACG20] [NAC17]: bloating, gas, pain, diarrhea; methane excess (IMO, [ACG20]) goes with constipation
     ["Bloating and gas after meals", "Belly pain, diarrhea", "Constipation (methane, IMO)"],
     # [SU18] PPIs OR 1.71; [MMC12] [ACG20] slow motility (diabetes; opioids slow the gut); [ACG20] prior surgery
     ["Low stomach acid, acid blockers", "A slow gut (diabetes, opioids)", "Past belly surgery"],
     # [NAC17] [ACG20] glucose or lactulose breath test
     "Breath test (see below)"),
    (_mini(yeast(-3, 2, -10, 1.35) + yeast(9, -8, 30, 0.8, False)),
     # [CANDIDA20]: Candida is a regular member of the gut flora in most people
     "Yeast", "Candida, normally in small numbers",
     # [CDC-CAND] thrush and vaginal candidiasis are separate infections that share these risk factors
     # (antibiotics, steroids, diabetes, weak immunity); no source makes them a sign of gut yeast, so the card
     # says only that they share the risks.  There is no single gut sign.
     ["No single gut sign", "Mouth or vaginal yeast infections share the same risks"],
     # [SAMONIS93] antibiotics; [CDC-CAND] corticosteroids, diabetes, weakened immune system
     ["Antibiotics, steroid medicines", "High blood sugar", "A weakened immune system"],
     # [CANDIDA20] some Candida in stool is normal and there is no validated cut-off: the provider reads it
     "Stool test; some yeast is normal"),
    (_mini(pinworm(0, 0, -26, 0.54, w=4.6, sw=0.85)),
     # [CDC-GIA] [CDC-PIN]
     "Parasites", "such as Giardia or pinworm",
     # [CDC-GIA] diarrhea, gas, cramps, greasy stools that can float; [CDC-PIN] itching at night
     ["Diarrhea, cramps and gas", "Greasy stools that float", "Itchy bottom at night (pinworm)"],
     # [CDC-GIA] untreated or recreational water, travel, child care, people; pets are a small risk (CDC);
     # [CDC-PIN] pinworm spreads only between people (child care, households)
     ["Untreated lake or stream water", "Travel, swimming, child care", "Someone close to you has it"],
     # [CDC-GIA] stool samples; [CDC-PIN] tape test (stool tests are not recommended for pinworm)
     "Stool test; tape test for pinworm"),
]


def kinds_html():
    cards = []
    li = lambda xs: "".join(f"<li>{x}</li>" for x in xs)
    for mi, name, sub, clues, feeds, test in KINDS:
        cards.append(f'<div class="{U}-kc"><div class="{U}-kh">{mi}<div><b>{name}</b><span>{sub}</span></div></div>'
                     f'<div class="{U}-kl"><i>Clues</i><ul>{li(clues)}</ul></div>'
                     f'<div class="{U}-kl {U}-kf"><i>Risks</i><ul>{li(feeds)}</ul></div>'
                     f'<div class="{U}-kl {U}-kt2"><i>Test</i><p>{test}</p></div></div>')
    # plan length: ND584 runs the Remove step 10 days in a 24-day program; Chedid 2014 used 4 weeks of herbs
    return (f'<div class="{U}-sh">Three kinds of overgrowth<span>Testing shows which one you have. Your provider sets '
            'the plan and its length, often a few weeks.</span></div>'
            f'<div class="{U}-kinds">{"".join(cards)}</div>')


# ============================================================== breath test numbers + red flags
def numbers_html():
    tiles = (
        # [NAC17]: a rise of >=20 ppm from baseline in hydrogen by 90 min = positive for SIBO
        f'<div class="{U}-n"><i>Hydrogen</i><b>rises 20 ppm or more</b><span>within 90 minutes: SIBO</span></div>'
        # [NAC17]: methane >=10 ppm at any point = positive; [ACG20] names it intestinal methanogen overgrowth (IMO)
        f'<div class="{U}-n"><i>Methane</i><b>10 ppm or more</b><span>at any point: methane overgrowth (IMO)</span></div>'
        # the test reports two gases, so the write-in box has a labelled line for each
        f'<div class="{U}-mine"><b>My result</b><div><span>Hydrogen</span><i></i></div>'
        '<div><span>Methane</span><i></i></div></div>')
    # [NAC17]: 8-12 h fast; glucose or lactulose drink; SIBO testing can be limited to 2 hours; [LBT180] lactulose
    # tests are often read for 3 hours, so "2 to 3 hours".  "Microbes", not "bacteria": hydrogen comes from
    # bacteria, methane from archaea [ACG20]
    lead = (f'<div class="{U}-nl">{icon("breath", "0.3in", sw=3.4)}<div><b>Breath test: know your numbers</b>'
            '<span>After an overnight fast you drink a sugar solution, then breathe into tubes for 2 to 3 hours. '
            'Misplaced microbes turn the sugar into gas, measured in ppm (parts per million).</span></div></div>')
    # [ALARM]: blood or black stools, high fever, unplanned weight loss; confirmed parasites are treated with medicine
    alarm = (f'<div class="{U}-alarm">{icon("warning", "0.19in", sw=4)}<p><b>Get checked soon</b> for blood or black '
             'stools, a high fever or weight loss you did not try for. Confirmed parasites usually need medicine.</p></div>')
    return f'<div class="{U}-nums">{lead}{tiles}</div>{alarm}'


# ============================================================== the 5R ribbon
# [ND584] Remove = take out unwanted microbes and trigger foods.  The ribbon says what is removed, with no disease
# word ("clear the overgrowth"), which next to "this sheet" would tie the back page's products to treating one.
# The sub is one line (trigger foods are the back page's "Cut the sugar"), so the Remove arrow has room to breathe.
# The back page no longer calls Spectrum BR a 5R step, so the ribbon stays front-page education.
FIVE = [("Remove", "unwanted microbes", "This sheet"), ("Replace", "stomach acid, enzymes", None),
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
.gov .gov-art svg{display:block;width:96.6%;height:auto;margin:0 auto}   /* a hair under full width: the room pays for the
   5R ribbon's height, the KEY gap and the gas boxes */
.gov-key{position:relative;border:1.2px solid #C9D6DA;border-radius:8px;padding:7px 8px 4px;margin-top:10px}
.gov-kt{position:absolute;top:-7px;left:12px;background:#fff;padding:0 6px;font:800 7.2pt Inter,sans-serif;
  letter-spacing:.16em;text-transform:uppercase;color:var(--deep)}
.gov-kg{display:grid;grid-template-columns:repeat(4,auto);justify-content:space-between;align-items:center;gap:2px 8px}
.gov-kg>div{display:flex;align-items:center;gap:4px;min-width:0}
.gov-kg svg{flex:none;width:0.22in;height:0.22in;overflow:visible}
.gov-kg svg.gov-kw{width:0.33in}
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
.gov-nums{display:grid;grid-template-columns:1fr 1.42in 1.42in 1in;gap:5px;margin-top:0.08in;align-items:stretch;
  border:1px solid #E8D9B6;background:#FFFCF4;border-radius:8px;padding:5px 6px}
.gov-nl{display:flex;align-items:center;gap:7px}
.gov-nl .ic{flex:none;color:var(--c1)}
.gov-nl b{display:block;font:900 9.6pt/1.2 Merriweather,Georgia,serif;color:var(--c1)}
.gov-nl span{display:block;font-size:7.5pt;line-height:1.28;color:#2B3236}
.gov-n{border-radius:5px;background:#F7EDD7;border-top:3px solid #D99A1E;padding:2px 6px 3px;color:#6E4A00}
.gov-n i{display:block;font:800 7pt Inter,sans-serif;letter-spacing:.07em;text-transform:uppercase;font-style:normal}
.gov-n b{display:block;font:800 8.6pt/1.15 Inter,sans-serif;color:#5B3C00}
.gov-n span{display:block;font-size:7.2pt;line-height:1.2;color:#6E5320}
.gov-mine{border:1.3px dashed #9AA5AC;border-radius:5px;background:#fff;display:flex;flex-direction:column;
  justify-content:space-between;padding:2px 6px 4px}
.gov-mine b{font:700 7pt/1.15 Inter,sans-serif;color:#6A747B;text-align:center}
.gov-mine div{display:flex;align-items:flex-end;gap:3px}
.gov-mine span{font:600 7pt/1 Inter,sans-serif;color:#56606A}
.gov-mine i{flex:1;height:14px;border-bottom:1px solid #9AA5AC}
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
/* min-height keeps the ribbon at the height it had with a two-line Remove sub: the one-line sub now leaves the Remove
   arrow (title, sub and THIS SHEET tag) clear room above and below, like its neighbours */
.gov-5rr>div{position:relative;background:var(--soft);color:var(--deep);padding:3px 14px 3px 18px;min-height:0.568in;
  display:flex;flex-direction:column;justify-content:center;
  clip-path:polygon(0 0,calc(100% - 10px) 0,100% 50%,calc(100% - 10px) 100%,0 100%,10px 50%)}
.gov-5rr>div:first-child{clip-path:polygon(0 0,calc(100% - 10px) 0,100% 50%,calc(100% - 10px) 100%,0 100%);padding-left:9px}
.gov-5rr>div:nth-child(even){background:#D3E9EE}
.gov-5rr b{display:flex;align-items:center;gap:4px;font:800 8.2pt Inter,sans-serif;text-transform:uppercase;letter-spacing:.04em}
.gov-5rr b i{font-style:normal;display:inline-flex;align-items:center;justify-content:center;width:13px;height:13px;
  border-radius:50%;background:var(--c1);color:#fff;font:800 7pt/1 Inter,sans-serif}
.gov-5rr span{font-size:7pt;line-height:1.12;color:#3B464C}
.gov-5rr>div:first-child span{white-space:nowrap}   /* "unwanted microbes" fits the arrow with 5 px to spare: never wrap it */
.gov-5rr em{font-style:normal;font:800 7pt/1.15 Inter,sans-serif;letter-spacing:.04em;color:#B3362B;margin-top:1px}
.gov-5rr>div.gov-on{background:var(--c1);color:#fff}
.gov-5rr>div.gov-on b i{background:#fff;color:var(--c1)}
.gov-5rr>div.gov-on span{color:#E3F1F4}
.gov-5rr>div.gov-on em{color:#fff;background:#F15F3F;border-radius:3px;padding:1px 5px;align-self:flex-start;text-transform:uppercase}
/* ---- this sheet's back page only (the page holding the .gov-back marker in the lifestyle title).  The shared
   kit sets all fine print at 7 pt and draws the START HERE badge (.startb) on the column's top edge. */
/* the Paradex photo is a flat RGB image: blend its white ground into the column tint (this image only) */
.sheet.back:has(.gov-back) .col .pick img[alt="NutriDyn Paradex bottle"]{mix-blend-mode:multiply;filter:none}
/* Nutricidin's label lists 12 lines: its column is wider so the full list fits */
.sheet.back:has(.gov-back) .cols{grid-template-columns:1fr 1.4fr 1.06fr 1fr .96fr!important}
/* rows line up across the five columns.  Every header keeps a top band for the START HERE badge, so the badge
   never touches the first column's title, and all five titles sit at the same height (each needsub is one
   line); every name is one line ("S. boulardii", with UltraBiotic on the size line) and every column's two
   bullets take four lines, so the bullets and the "In each serving" lines start level in all five. */
.sheet.back:has(.gov-back) .col .need{padding-top:13px}
/* the check list gets half the row; the bedtime box holds one product */
.sheet.back:has(.gov-back) .duo{grid-template-columns:1fr 1fr}
.sheet.back:has(.gov-back) .rhythm{grid-template-columns:1.2fr 1.2fr .6fr}
.sheet.back:has(.gov-back) .life .disc2{width:0.76in;height:0.76in}
/* the two safety panels need the room: slightly tighter gaps between the back page's blocks */
.sheet.back:has(.gov-back) .band{padding-bottom:0.12in}
.sheet.back:has(.gov-back) .ns-title{margin-top:0.1in}
.sheet.back:has(.gov-back) .cols{margin-top:0.06in}
.sheet.back:has(.gov-back) .duo{margin-top:0.06in}
.sheet.back:has(.gov-back) .notes{margin-top:0.06in}
/* the Pharmacist check's Spectrum BR line needs a fourth line (CYP2C9 and warfarin, low blood sugar, licorice and
   its three drug classes): in the pharmacy edition only, 1 px between the check bullets and none after the last
   pays for it, with the gaps above.  The provider edition has room and keeps the kit's 2 px. */
.sheet.back:has(.gov-edh) .rx li{margin-bottom:1px}
.sheet.back:has(.gov-edh) .rx li:last-child{margin-bottom:0}
/* The kit's plan line ends "start with the Start here pick, then add one product a week", which would stretch
   a Remove step with a set length (ND584: 10 days) to five weeks.  This sheet's line keeps the kit's count, names
   the Start here pick (Spectrum BR, the one column with start: True) and leaves the pace of the rest to each
   edition's checker (.gov-edp / .gov-edh mark the edition).  The check panel sets the row height, so the
   rhythm panel has room for the second line this takes. */
.sheet.back:has(.gov-back) .total:has(> b + b){font-size:0}
.sheet.back:has(.gov-back) .total:has(> b + b) > b:first-of-type{font-size:7pt}
.sheet.back:has(.gov-back) .total:has(> b + b) > b + b{display:none}
.sheet.back:has(.gov-back) .total:has(> b + b)::before{content:"The full plan is ";font-size:7pt}
.sheet.back:has(.gov-edp) .total:has(> b + b)::after{content:". Start with Spectrum BR; ask your provider when to add the rest.";font-size:7pt}
.sheet.back:has(.gov-edh) .total:has(> b + b)::after{content:". Start with Spectrum BR; ask your pharmacist when to add the rest.";font-size:7pt}
/* The kit's rhythm has no between-meals slot.  The second box holds the evening-meal pills and S. boulardii's
   mid-afternoon capsule (2 hours from the herbs, apart from dinner), so on this sheet it is labelled
   "Afternoon + dinner" (the same font-size:0 + ::after trick; gap 0 so the hidden label adds no second gap). */
.sheet.back:has(.gov-back) .slot:nth-child(2) .when{font-size:0;gap:0}
.sheet.back:has(.gov-back) .slot:nth-child(2) .when svg{margin-right:4px}
.sheet.back:has(.gov-back) .slot:nth-child(2) .when::after{content:"Afternoon + dinner";font-size:7pt}
"""


# ============================================================== the sheet
SHEET = {
    "slug": SLUG, "code": "ND-GI-104", "order": 11, "theme": "gut", "series": "Gut Health Series",
    "title": "Gut Overgrowth", "sub": "Yeast, parasites and SIBO",
    # [SENDER16] trillions of bacteria, almost all in the colon.  [ACG20] [MMC12] defences: stomach acid, the
    # fasting "housekeeper" waves, immunity.  [NAC17] a healthy upper small bowel holds up to about 10^3 CFU/mL and
    # the ileum more [ACG20], so "few", never "free of bacteria".  [CANDIDA20] Candida is a normal resident.
    # [CDC-GIA] [CDC-PIN] parasites come from exposure (untreated water, food, another person), not from weak
    # defenses, so they get their own sentence.  The test sentence lives in the "Three kinds" header just below.
    "intro": ("Trillions of microbes live in your gut, almost all of them in the <b>colon</b> (large intestine). "
              "Stomach acid, the gut&rsquo;s sweeping waves and your immune system keep bacteria in the "
              "<b>small intestine</b> few and yeast in check. When those defenses slip, bacteria crowd the "
              "small intestine (<b>SIBO</b>) or <b>Candida</b> yeast multiplies. <b>Parasites</b> are caught from "
              "water, food or people."),
    "front": front,
    "css": CSS,
    "back": {
        # the span marks this sheet's back page for the scoped CSS (.sheet.back:has(.gov-back))
        "life_title": f'Lifestyle Recommendations<span class="{U}-back"></span>',
        # no disease words here: the line sits over the product page
        "life_sub": "Cut the sugar, let your gut sweep, and keep new germs out",
        "style": "circle",
        "life": [
            # [ND584] Remove step: sugar, alcohol, processed food out
            ("sugar", "Cut the sugar", "Skip added sugar, sweet drinks, alcohol and junk food during the plan."),
            # [MMC12] cleaning waves run only in the fasting state; [ND584] no food within 2 hours of bedtime
            ("clock", "Space your meals", "No grazing: the gut sweeps itself between meals. Stop eating 2 hours before bed."),
            # [CDC-GIA] prevention: hand washing, food hygiene, and boil or filter untreated water before drinking it
            ("drop", "Wash, cook, filter", "Wash hands and produce, cook meat through, and boil or filter lake water."),
            # [ND584] "Avoid eating under stress. Eat slowly."
            ("plate", "Eat calm, chew well", "Slow, unhurried meals give stomach acid and enzymes a head start."),
            # [SU18] PPIs raise SIBO risk; stopping is a prescriber decision
            ("rx", "Review acid blockers", "They lower stomach acid, a key defense. Never stop one without your prescriber."),
        ],
        # Products: NutriDyn's own Remove-step picks.  Asher's GI-MAP protocol, REMOVE line (his email of
        # 2025-01-30): "Nutricidin 1 softgel 3x daily away from probiotics; Spectrum BR 2 tabs 3x; ParaCleanse/Paradex
        # 1 cap 3x".  ND584 Remove = Spectrum BR (+ Spectrum AR, not in the product DB).  NutriDyn's 5R product grid:
        # Berberine Anti-microbial = Spectrum BR, Biofilm Aromatic Aid = NutriCidin, Parasite Botanical = Paradex,
        # BioToxin Binder = Binder Pro; "Sac B Anti-candida Probiotic" for Candida.  NutriDyn GLC 2023 5R talk:
        # binders GI Defend, Binder Pro.  Facts and sources: products.d/gut-overgrowth.json.
        # Timing: the herbs go with meals; S. boulardii, a live yeast, sits between meals, 2 hours from the herbs
        # (Asher's rule from his case notes: probiotics 2 hours away from antimicrobials); Binder Pro is alone at
        # bedtime, 2 hours from every other pill, so it cannot carry the probiotic or a medicine out with the stool.
        # Claim bullets start with their verb, so the kit ends each one with the diamond tied to the FDA line.
        "cols": [
            # ND505 Rev. 8/24, the sell sheet's own claim: "Promote a healthy gastrointestinal tract".  Bullet 2 is a
            # formula fact (berberine HCl plus the label's six-herb blend), not "Step 1 of the 5R plan": next to the
            # front's "Remove unwanted microbes: this sheet" a 5R step would read as an antimicrobial claim.
            {"p": "go_spectrum_br", "need": "Balance the flora", "needsub": "berberine, Oregon grape",
             "start": True, "dose": "dose_from_db",
             "bullets": ["Promotes a healthy gastrointestinal tract",
                         "Berberine plus a six&#8209;herb blend"]},
            # ND949 Rev. 2/25: ginger plus eight oils; serratiopeptidase and calcium EDTA "support healthy biofilms"
            {"p": "go_nutricidin", "need": "Plant oils + enzyme", "needsub": "oregano, thyme, clove and more",
             "dose": "dose_from_db",
             "bullets": ["Supports balanced gut flora with eight plant oils and ginger",
                         "Supports healthy biofilms with an enzyme and a mineral binder"]},
            # "wormwood", the catalog's word: the species is not confirmed (see products.d src)
            {"p": "go_paradex", "need": "Herbal cleanse", "needsub": "black walnut, wormwood",
             "dose": "dose_from_db",
             "bullets": ["Supports a healthy intestinal environment", "Five traditional cleanse herbs"]},
            # ND170 Rev. 8/25: one capsule twice daily.  S. boulardii is a yeast: antibacterial antibiotics leave it
            # alone and antifungals (nystatin, fluconazole: a likely co-prescription on a yeast sheet) can kill it,
            # Kelesidis 2012 PMID 22423260; printed in both editions
            {"p": "go_sboulardii", "need": "A friendly yeast", "needsub": "S. boulardii probiotic",
             "dose": "dose_from_db",
             "bullets": ["Supports a balanced gut microbiome",
                         "Antifungals harm it; antibiotics do not"]},
            # the header says "Bind and carry out"; a binder taken with other pills can carry them out too, so it
            # sits 2 hours from medicines and other pills (both bullets fit two lines in this narrow column)
            {"p": "go_binder_pro", "need": "Bind and carry out", "needsub": "apple pectin, chlorella",
             "dose": "dose_from_db",
             "bullets": ["Helps bind unwanted compounds",
                         "Take 2 hours from medicines and pills"]},
        ],
        "rx": {
            # Both editions go to patients, worded for who checks them.  No disease words next to the products
            # (the "test first" line moved off this page: the front says testing shows which overgrowth it is).
            # The empty .gov-edp / .gov-edh spans mark the edition for the plan line's CSS (see CSS).
            "practitioner": [
                # Guo 2012 (berberine slows CYP3A4/2D6/2C9; ND505 names cyclosporine); Yin 2008 (berberine lowers
                # blood sugar, so with diabetes drugs the risk is low blood sugar); licorice root in the ND505 blend
                # (not DGL) can raise blood pressure, Deutch 2019, Kwon 2020: the lead names high blood pressure so a
                # reader on no medicine still stops here; all labels: "taking medication ... consult"
                f'<span class="{U}-edp"></span><b>On any medicine or high blood pressure?</b> Berberine changes how '
                "the liver clears many medicines, such as cyclosporine, and can push blood sugar too low with "
                "diabetes drugs; Spectrum BR&rsquo;s licorice can raise blood pressure. Bring your list to {who}.",
                # Spectrum BR: the ND505 blend's ginger root (Heck 2000), and berberine slows CYP2C9 (Guo 2012), the
                # enzyme that clears S-warfarin (Kaminsky LS, Zhang ZY. Pharmacol Ther 1997;73:67-74, PMID 9014207).
                # Heck 2000 (ginger, clove, garlic); Hosseini 2024, Jadhav 2020 (serratiopeptidase breaks down fibrin);
                # Preusch 1989 (pau d'arco's lapachol); chlorella vitamin K vs warfarin (MedlinePlus)
                "<b>On a blood thinner?</b> Spectrum BR, Nutricidin, Paradex and Binder Pro can affect it. "
                "Ask {who} first.",
                # ND505 (Spectrum BR) "Do not use if pregnant or nursing"; Paradex retail label: not in pregnancy or
                # nursing; ND949, ND170, ND1141: "consult"; all doses are adult label doses; Chan 1993 (berberine
                # and newborns)
                "<b>Pregnant or nursing?</b> Do not take Spectrum BR or Paradex; ask {who} about the rest. "
                "<b>For a child?</b> These are adult doses: ask first.",
                # Enache-Angoulvant 2005 (invasive Saccharomyces infection: central venous catheters and immune
                # suppression are the main risks, so skip it, as the pharmacy edition says); Paradex: black walnut,
                # "may contain traces of tree nuts" (retail listing)
                "<b>Central IV line or weak immunity?</b> Skip S. boulardii unless {who} says yes. "
                "<b>Tree-nut allergy?</b> Ask before Paradex.",
            ],
            "pharmacy": [
                # Guo 2012 PMID 21870106 (berberine slows CYP3A4, 2D6, 2C9); ND505 cyclosporine caution; CYP2C9
                # clears S-warfarin, Kaminsky 1997 PMID 9014207; Yin 2008 PMID 18442638 (berberine lowers blood
                # sugar, so with diabetes drugs it can go too low).  Licorice root is in the ND505 blend (not DGL):
                # Deutch 2019 PMID 31615045, Kwon 2020 PMID 31874059 (blood pressure up, potassium down), hence
                # diuretics, digoxin and steroids
                f'<span class="{U}-edh"></span><b>Spectrum BR:</b> berberine slows liver enzymes (CYP3A4, 2D6, '
                "2C9: cyclosporine, warfarin) and can push blood sugar too low with diabetes drugs; its licorice can "
                "raise blood pressure and lower potassium (diuretics, digoxin, steroids).",
                # Each product named with its own herbs.  Spectrum BR: the ND505 blend's ginger root; Heck 2000 PMID
                # 10902065 (ginger, clove, garlic; it lists licorice root too); Hosseini 2024 PMID 38502196 and Jadhav
                # 2020 PMID 33134103 (serratiopeptidase); Preusch 1989 PMID 2916837 (pau d'arco); chlorella vitamin K
                # and warfarin (MedlinePlus)
                "<b>Blood thinners:</b> Spectrum BR (ginger), Nutricidin (ginger, clove oil, serratiopeptidase) and "
                "Paradex (garlic, pau d&rsquo;arco) may add to bleeding; Binder Pro&rsquo;s chlorella (vitamin K) can "
                "weaken warfarin.",
                # ND505 + Paradex retail label: not in pregnancy or nursing; the other three labels: consult; adult
                # label doses; Chan 1993 PMID 8513024 (berberine displaces bilirubin in newborns)
                "<b>Pregnant or nursing?</b> Do not take Spectrum BR or Paradex; ask {who} about the rest. "
                "<b>For a child?</b> These are adult doses: ask first.",
                # Enache-Angoulvant 2005 PMID 16267727 (catheters, immune suppression); Kelesidis 2012 (antifungals
                # act on yeast, so they may inactivate S. boulardii); Paradex tree-nut trace warning (retail listing)
                "<b>S. boulardii</b> is a live yeast: skip it with a central IV line or weak immunity; antifungals "
                "stop it. <b>Tree-nut allergy?</b> Ask before Paradex.",
            ],
        },
    },
}
