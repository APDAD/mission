"""Stress and Cortisol (ND-EN-801), Energy and Stress Series.  Slug "stress-cortisol".

Self-contained sheet module (no legacy / sheets.py / art.py drawing code).
FRONT, top to bottom:
  intro -> "Your stress system": a front-view adult, head to hips, drawn from mirrored splines (exactly
  symmetric), with the brain, the spine, both kidneys and the two adrenal glands (right one a pyramid,
  left one a crescent, as in life).  A magnified side view of the brain shows the hypothalamus and the
  pituitary; a magnified adrenal shows its outer layer (cortex, makes cortisol) and core (medulla,
  makes adrenaline).  Blue arrows = the brain's stress signals (CRH, ACTH); gold dots = cortisol; a grey
  dashed loop = the brake (cortisol's feedback to the brain).  Four numbered steps and a KEY (which also names the
  yellow adrenal glands); the kidneys and spine carry their own labels.  Both zoom cones are drawn over the figure
  (under the arrows, dots, labels and lens rings), so each one runs unbroken to its lens ring, callout style; the
  kidneys and adrenals are drawn after the cones, so the adrenal cone passes behind the kidney; every
  brain-inset label sits inside its circle (_check_inset fails the build otherwise), and the adrenal inset's labels
  sit to its left, clear of its cone.  No SVG text is stroked (stroked text prints as a Type 3 font): labels sit in
  clear space instead of on white halos.
  -> "Your cortisol clock": a healthy daily curve (green) beside a flattened stressed curve (red dashed),
  with its own KEY cards -> "Signs your stress system is working overtime" (tick tiles)
  -> "Is it 'adrenal fatigue'?" beside "See {who} soon" (too-low and too-high cortisol signs, steroid
  medicines, 988).
BACK: hex lifestyle band and product headers (both deepened for 4.5:1 contrast), five NutriDyn picks with full
label lines, daily rhythm (four products: Adrenal Renew, a glandular, is only for people already stepping off one,
so it is left out of the rhythm and its daily total; its column says it REPLACES the current glandular, and its dose
bar gives the time and the step-down), one medicine check for both editions ({who} is the only
difference), and a bold, boxed FDA disclaimer tied by a diamond to every structure/function statement [CFR93].  Back-page CSS is scoped by the empty <i class="scx-bk">
in the band title.
Every SVG id starts with "scx-" and every CSS class with "scx-", so nothing collides with other sheets
in the all-sheets bundle.  Edition wording: "{who}" / "{Who}" (build.ed_text).

SOURCES (tags sit in comments next to each number or claim on the page)
  [SMITH06]  Smith SM, Vale WW. Dialogues Clin Neurosci 2006;8:383-95. PMID 17290797.
             doi:10.31887/DCNS.2006.8.4/ssmith (stress -> hypothalamic CRH -> pituitary ACTH -> adrenal cortex
             glucocorticoids; glucocorticoid feedback inhibition limits the size and length of the response;
             the sympathetic adrenomedullary arm releases adrenaline)
  [SAP00]    Sapolsky RM, Romero LM, Munck AU. Endocr Rev 2000;21:55-89. PMID 10696570 (glucocorticoids
             raise blood glucose, support blood pressure and restrain inflammation in the stress response)
  [DEBONO09] Debono M et al. J Clin Endocrinol Metab 2009;94:1548-54. PMID 19223520.
             doi:10.1210/jc.2008-2380 (healthy 24-h cortisol: peak about 08:30, nadir under 2 ug/dL near
             00:18, quiet phase from about 19:45 to 05:30) -> the green curve's shape
  [STALDER16] Stalder T et al. Psychoneuroendocrinology 2016;63:414-32. PMID 26563991.
             doi:10.1016/j.psyneuen.2015.10.010 (cortisol awakening response: a marked rise over the first
             30-45 min after waking) -> "peak 30 to 45 minutes after waking"
  [MILLER07] Miller GE, Chen E, Zhou ES. Psychol Bull 2007;133:25-45. PMID 17201569.
             doi:10.1037/0033-2909.133.1.25 (meta-analysis: hormone output is high at the start of a stressor
             and falls with time; uncontrollable, traumatic stressors give a high, FLAT daily cortisol profile)
             -> the red dashed curve's shape (smaller morning rise, higher evening)
  [ADAM17]   Adam EK et al. Psychoneuroendocrinology 2017;83:25-41. PMID 28578301.
             doi:10.1016/j.psyneuen.2017.05.018 (80 studies: flatter morning-to-evening slopes go with poorer
             mental and physical health, largest for immune/inflammation outcomes)
  [CADE16]   Cadegiani FA, Kater CE. BMC Endocr Disord 2016;16:48. PMID 27557747.
             doi:10.1186/s12902-016-0128-4 (systematic review, 58 studies: no substantiation that "adrenal
             fatigue" is a medical condition; not recognised by any endocrinology society)
  [AKTURK18] Akturk HK et al. Mayo Clin Proc 2018;93:284-90. PMID 29502560. doi:10.1016/j.mayocp.2017.10.019
             (all 12 over-the-counter "adrenal support" supplements tested held thyroid hormone, most a
             steroid hormone, none on the label) -> glandular caution on the back
  [SEGER04]  Segerstrom SC, Miller GE. Psychol Bull 2004;130:601-30. PMID 15250815 (chronic stress
             suppresses cellular and humoral immunity) -> "getting sick more often"
  [EPEL00]   Epel ES et al. Psychosom Med 2000;62:623-32. PMID 11020091 (more stress-induced cortisol in
             women with central fat) -> "weight gain at the belly"
  [LEP97]    Leproult R et al. Sleep 1997;20:865-70. PMID 9415946 (one short night: 37-45% higher cortisol
             the next evening)
  [MAYO]     Mayo Clinic, "Stress symptoms: Effects on your body and behavior" (headache, muscle tension,
             fatigue, sleep problems, stomach upset, anxiety, irritability, sadness, lack of focus).
             Named source, not reopened in this session (nih.gov and mayoclinic.org hosts blocked here).
  [ES16AI]   Bornstein SR et al. Endocrine Society guideline, primary adrenal insufficiency. J Clin
             Endocrinol Metab 2016;101:364-89. PMID 26760044 (fatigue, weight loss, salt craving, postural
             dizziness and low blood pressure, darker skin in primary disease, nausea and belly pain;
             glucocorticoid patients need stress dosing and must not stop suddenly)
  [ES08CS]   Nieman LK et al. Endocrine Society guideline, diagnosis of Cushing's syndrome. J Clin
             Endocrinol Metab 2008;93:1526-40. PMID 18334580 (most telling signs: easy bruising, facial
             plethora, proximal muscle weakness, reddish-purple striae over 1 cm wide; also central weight
             gain, a fatty hump, new high blood pressure or diabetes; most cases come from steroid medicines)
  [FLES21]   Fleseriu M et al. Pituitary Society consensus, Cushing's disease: a guideline update. Lancet Diabetes
             Endocrinol 2021;9:847-75. PMID 34687601. doi:10.1016/S2213-8587(21)00235-7 (current companion to
             [ES08CS]; same clinical signs)
  [BEUS24]   Beuschlein F et al. ESE/Endocrine Society joint guideline, glucocorticoid-induced adrenal insufficiency.
             J Clin Endocrinol Metab 2024;109:1657-83. PMID 38724043. doi:10.1210/clinem/dgae250 (at least 1% of
             people take long-term steroids; stopping or tapering needs care because the HPA axis is suppressed)
             -> "On a steroid such as prednisone? Never stop it suddenly."
  [988]      988 Suicide & Crisis Lifeline (call or text 988), SAMHSA, live since July 2022.
  [ANAT]     Gray's Anatomy (42nd ed.): kidneys at T12-L3, the right a little lower than the left; right
             adrenal pyramidal on the upper pole, left adrenal crescentic along the medial border above the
             hilum; adrenal cortex outside (cortisol, zona fasciculata), medulla inside (adrenaline).
  Back-page evidence (comments only; product copy stays structure/function):
  [AKH22]    Akhgarjand C et al. Phytother Res 2022;36:4115-24. PMID 36017529. doi:10.1002/ptr.7598
             (12 RCTs, 1,002 adults: ashwagandha lowered stress and anxiety; stress benefit at 300-600 mg/d;
             low certainty)
  [ARU24]    Arumugam V et al. Explore 2024;20:103062. PMID 39348746. doi:10.1016/j.explore.2024.103062
             (9 RCTs, 558 patients: lower Perceived Stress Scale scores and serum cortisol than placebo)
  [TALB13]   Talbott SM et al. J Int Soc Sports Nutr 2013;10:37. PMID 23924268 (Relora, 4 weeks: salivary
             cortisol 18% lower than placebo, better mood scores)
  [OLSS09]   Olsson EM et al. Planta Med 2009;75:105-12. PMID 19016404 (rhodiola SHR-5 in stress-related
             fatigue: less burnout, lower cortisol response to waking)
  [HID19]    Hidese S et al. Nutrients 2019;11:2362. PMID 31623400 (L-theanine 200 mg/d, 4 weeks: better
             stress, sleep and mood scores)
  [PATAK04]  Patak P et al. Endocr Res 2004;30:871-5. PMID 15666839 (the adrenal gland holds one of the
             body's highest vitamin C levels; vitamin C is a cofactor for adrenaline and steroid synthesis)
  [PICK20]   Pickering G et al. Nutrients 2020;12:3672. PMID 33260549 (stress and low magnesium can feed
             each other: the magnesium-stress vicious circle)
  [SHARMA18] Sharma AK et al. J Altern Complement Med 2018;24:243-8. PMID 28829155 (ashwagandha 600 mg/d
             raised T3 and T4 and lowered TSH) -> "can make ... thyroid pills stronger" in the medicine check
  [BJORN20]  Bjornsson HK et al. Liver Int 2020;40:825-9. PMID 31991029. doi:10.1111/liv.14393 (rare ashwagandha
             liver injury: five cases, all with jaundice after 2-12 weeks) -> the "yellow skin or eyes" line on the back
  [VDIER09]  van Diermen D et al. J Ethnopharmacol 2009;122:397-401. PMID 19168123. doi:10.1016/j.jep.2009.01.007
             (rhodiola root extracts inhibit MAO-A and MAO-B in vitro) -> antidepressants in the medicine check
  [JAMS17]   Jamshidi N, Cohen MM. Evid Based Complement Alternat Med 2017;2017:9217567. PMID 28400848 (holy basil
             / tulsi in 24 human studies: lowered blood sugar in metabolic studies) and [SINGH01] Singh S et al.
             J Ethnopharmacol 2001;78:139-43. PMID 11694358 (holy basil oil lengthened clotting time in animals)
             -> holy basil (Adrenal Renew) beside ginseng in the warfarin / diabetes line
  [EFSA23]   EFSA NDA Panel. EFSA J 2023;21(5):e08006. PMID 37207271. doi:10.2903/j.efsa.2023.8006 (vitamin B6
             upper limit 12 mg a day for adults, set on peripheral neuropathy; the US limit is 100 mg a day, IOM 1998)
             -> "With Adrenal Renew, B6 reaches 65 mg" with the tingling caution (5 mg a day without it)
  [DRAKE13]  Drake C et al. J Clin Sleep Med 2013;9:1195-200. PMID 24235903. doi:10.5664/jcsm.3170 (400 mg of
             caffeine at bedtime, 3 h or even 6 h before bed disrupted sleep and cut total sleep time) -> "Coffee by
             noon: late coffee can cost you sleep."  [LOV05] Lovallo WR et al. Psychosom Med 2005;67:734-9 (caffeine
             raises cortisol, but daily users are partly tolerant) is no longer quoted on the page.
  [LEP01]    Leproult R et al. J Clin Endocrinol Metab 2001;86:151-7. PMID 11231993 (bright light in the
             early morning raised cortisol by more than 50%; afternoon light did not)
  [BALB23]   Balban MY et al. Cell Rep Med 2023;4:100895. PMID 36630953 (5 min a day of exhale-focused
             cyclic sighing for a month: better mood, slower breathing, more than mindfulness)
  [HEIN03]   Heinrichs M et al. Biol Psychiatry 2003;54:1389-98. PMID 14675803 (support from a friend
             lowered the cortisol response to a stress test)
  [CFR93]    21 CFR 101.93(d)-(e): the disclaimer sits next to each structure/function statement, or is linked to
             it by a symbol at the end of the statement and then set off in a box; it is in bold type no smaller
             than one-sixteenth inch.  -> a diamond after every product statement, a bold boxed disclaimer
  [HHS18]    Physical Activity Guidelines for Americans, 2nd ed. (HHS 2018): 150 minutes a week of moderate
             activity; [AASM15] Watson NF et al. Sleep 2015;38:843-4 (adults: 7 or more hours).
"""
import math
import os
import re

import kit
from kit import icon
from svgkit import T, svg

SLUG = "stress-cortisol"

# ============================================================== text measuring (Inter via Pillow)
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
    """Advance width of `text` in Inter at `size` px (a generous guess if the font is missing)."""
    text = re.sub(r"<[^>]+>", "", text).replace("&amp;", "&")
    try:
        w = _face(_WEIGHTS[weight]).getlength(text) * size / 100
    except Exception:
        w = len(text) * size * (0.68 if text.isupper() else 0.6)
    return w + ls * len(text)


def wrap(text, width, size, weight=500):
    """Greedy word wrap to `width` px; returns the lines."""
    lines, cur = [], ""
    for w in text.split():
        t = (cur + " " + w).strip()
        if cur and tw(t, size, weight) > width:
            lines.append(cur)
            cur = w
        else:
            cur = t
    if cur:
        lines.append(cur)
    return lines


# ============================================================== geometry helpers
def spline(pts, closed=True):
    """Catmull-Rom curve through pts [(x, y) or (x, y, tension)] as cubic Bezier path data.
    A low tension (0.2-0.5) gives a near-sharp corner at that point."""
    P = [(p[0], p[1], p[2] if len(p) > 2 else 1.0) for p in pts]
    n = len(P)

    def tan(i):
        if closed:
            a, b = P[i - 1], P[(i + 1) % n]
        else:
            a, b = P[max(i - 1, 0)], P[min(i + 1, n - 1)]
        k = P[i][2]
        return k * (b[0] - a[0]) / 2, k * (b[1] - a[1]) / 2

    tg = [tan(i) for i in range(n)]
    d = [f"M{P[0][0]:.2f},{P[0][1]:.2f}"]
    for i in range(n if closed else n - 1):
        j = (i + 1) % n
        (xa, ya, _), (xb, yb, _) = P[i], P[j]
        d.append(f"C{xa + tg[i][0] / 3:.2f},{ya + tg[i][1] / 3:.2f} {xb - tg[j][0] / 3:.2f},{yb - tg[j][1] / 3:.2f} "
                 f"{xb:.2f},{yb:.2f}")
    return "".join(d) + ("Z" if closed else "")


def mirror(right):
    """`right` runs from the top centre (x = 0) down the right side to the bottom centre (x = 0).
    Returns the whole outline, exactly symmetric about x = 0."""
    return list(right) + [(-p[0], p[1]) + tuple(p[2:]) for p in reversed(right[1:-1])]


def flip(pts):
    return [(-p[0], p[1]) + tuple(p[2:]) for p in pts]


def scale_pts(pts, k, dx=0.0, dy=0.0):
    return [(p[0] * k + dx, p[1] * k + dy) + tuple(p[2:]) for p in pts]


def rot_pts(pts, deg, cx=0.0, cy=0.0):
    a = math.radians(deg)
    ca, sa = math.cos(a), math.sin(a)
    out = []
    for p in pts:
        x, y = p[0] - cx, p[1] - cy
        out.append((cx + x * ca - y * sa, cy + x * sa + y * ca) + tuple(p[2:]))
    return out


def tangents(c1, r1, c2, r2):
    """Outer tangent segments between circle 1 and circle 2 (for a zoom cone)."""
    (x1, y1), (x2, y2) = c1, c2
    dx, dy = x2 - x1, y2 - y1
    d = math.hypot(dx, dy)
    ux, uy = dx / d, dy / d
    out = []
    for sgn in (1, -1):
        c = (r1 - r2) / d
        h = math.sqrt(max(0.0, 1 - c * c))
        nx, ny = c * ux - sgn * h * uy, c * uy + sgn * h * ux
        out.append(((x1 + r1 * nx, y1 + r1 * ny), (x2 + r2 * nx, y2 + r2 * ny)))
    return out


def pill(cx, cy, text, size, fg, bg="#FFFFFF", edge=None, weight=800, padx=6.0, h=None):
    """A rounded label (white backdrop) centred on (cx, cy), so text reads cleanly over art."""
    w = tw(text, size, weight) + 2 * padx
    h = h or size * 1.5
    e = f' stroke="{edge}" stroke-width="1"' if edge else ""
    return (f'<rect x="{cx - w / 2:.1f}" y="{cy - h / 2:.1f}" width="{w:.1f}" height="{h:.1f}" rx="{h / 2:.1f}" fill="{bg}"{e}/>'
            + T(round(cx, 1), round(cy + size * 0.36, 1), text, size, weight, fg, "middle")), w


# ============================================================== palette (every symbol is in a KEY or labelled)
INK, INK2 = "#2B3236", "#56616A"
SKIN, SKIN_EDGE, SKIN_LN = "#F2D9C9", "#E3BCA6", "#B5836F"
BRAIN, BRAIN_LN, BRAIN_FOLD = "#F2C8D1", "#BF7D90", "#D69AAB"
HYPO, HYPO_LN = "#EF7B33", "#B9521A"          # hypothalamus (labelled)
PIT, PIT_LN = "#9C5BA8", "#6C3779"            # pituitary gland (labelled)
KID_A, KID_B, KID_LN = "#C9675C", "#94403A", "#73302B"   # kidney (labelled)
CORTEX, CORTEX_B, CORTEX_LN = "#F5C24C", "#E09A2C", "#9A6414"   # adrenal outer layer (labelled)
MEDULLA, MEDULLA_LN = "#B04A3C", "#7C2E25"    # adrenal core (labelled)
BONE, BONE_LN = "#EFE6D5", "#CDBB9C"          # spine (labelled)
SIGNAL = "#2F6DB5"                            # blue arrow: the brain's stress signals (KEY)
CORT, CORT_LN = "#F3B21E", "#9C6A06"          # gold dot: cortisol (KEY)
BRAKE = "#7C868D"                             # grey dashed arrow: the brake / feedback (KEY)
HEALTHY = "#2F8A5E"                           # green line: healthy daily rhythm (chart KEY)
STRESSED = "#C8402F"                          # red dashed line: stressed, flattened rhythm (chart KEY)


def figure_defs():
    return ('<linearGradient id="scx-skin" x1="-100" y1="0" x2="100" y2="0" gradientUnits="userSpaceOnUse">'
            f'<stop offset="0" stop-color="{SKIN_EDGE}"/><stop offset=".28" stop-color="#F5E1D4"/>'
            '<stop offset=".5" stop-color="#F9EAE0"/><stop offset=".72" stop-color="#F5E1D4"/>'
            f'<stop offset="1" stop-color="{SKIN_EDGE}"/></linearGradient>'
            '<radialGradient id="scx-face" cx=".46" cy=".42" r=".72"><stop offset="0" stop-color="#F9EAE0"/>'
            f'<stop offset="1" stop-color="{SKIN_EDGE}"/></radialGradient>'
            '<radialGradient id="scx-brain" cx=".42" cy=".36" r=".75"><stop offset="0" stop-color="#F8DCE2"/>'
            f'<stop offset="1" stop-color="{BRAIN}"/></radialGradient>'
            f'<linearGradient id="scx-kid" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{KID_A}"/>'
            f'<stop offset="1" stop-color="{KID_B}"/></linearGradient>'
            f'<linearGradient id="scx-adr" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#F9D673"/>'
            f'<stop offset="1" stop-color="{CORTEX_B}"/></linearGradient>'
            '<radialGradient id="scx-cort" cx=".36" cy=".32" r=".75"><stop offset="0" stop-color="#FFE7A3"/>'
            f'<stop offset=".55" stop-color="{CORT}"/><stop offset="1" stop-color="#D99210"/></radialGradient>'
            '<radialGradient id="scx-hypo" cx=".4" cy=".35" r=".75"><stop offset="0" stop-color="#FFC59A"/>'
            f'<stop offset="1" stop-color="{HYPO}"/></radialGradient>'
            '<radialGradient id="scx-pit" cx=".4" cy=".35" r=".75"><stop offset="0" stop-color="#D7A3DF"/>'
            f'<stop offset="1" stop-color="{PIT}"/></radialGradient>'
            '<radialGradient id="scx-lens" cx=".5" cy=".45" r=".6"><stop offset="0" stop-color="#FFFFFF"/>'
            '<stop offset="1" stop-color="#FBF1E3"/></radialGradient>')


# ============================================================== the figure (head height = 1 unit, crown at y 0)
# Adult proportions, front view, about 7.5 heads tall, shown to just below the hips: chin 0.98, shoulder line
# 1.37, armpit 1.72, waist 2.75, hips 3.35.  Shoulders about 1.8 heads across, waist 1.2, hips 1.5.  Vertebral
# levels (head units): T12 2.31, L1 2.47, L3 2.79, L4 2.95 [ANAT], so the kidneys sit from 2.27 (left, higher)
# / 2.33 (right) down 0.48, beside the spine, and the adrenals sit on their upper poles.
HEAD_R = [(0, 0), (0.19, 0.022), (0.312, 0.095), (0.372, 0.215), (0.388, 0.35), (0.383, 0.47), (0.362, 0.585),
          (0.322, 0.695), (0.262, 0.795), (0.18, 0.885), (0.092, 0.948), (0, 0.968)]
EAR_R = [(0.372, 0.37), (0.405, 0.365), (0.428, 0.40), (0.433, 0.46), (0.424, 0.53), (0.402, 0.585),
         (0.372, 0.60)]
BODY_R = [(0, 0.80), (0.158, 0.80), (0.163, 0.95), (0.172, 1.08), (0.198, 1.165), (0.30, 1.228), (0.46, 1.282),
          (0.60, 1.33), (0.70, 1.37), (0.75, 1.45), (0.712, 1.62), (0.686, 1.80), (0.668, 2.02), (0.645, 2.28),
          (0.617, 2.55), (0.598, 2.76), (0.608, 2.95), (0.655, 3.15), (0.715, 3.36), (0.735, 3.62, 0.3),
          (0, 3.62)]
# arms hang a little away from the waist, so the gap between arm and body shows (0.16 head at the waist)
ARM_R = [(0.58, 1.34), (0.70, 1.36), (0.80, 1.40), (0.88, 1.47), (0.935, 1.57), (0.968, 1.70), (0.99, 1.86),
         (1.008, 2.05), (1.03, 2.30), (1.05, 2.55), (1.065, 2.74), (1.085, 2.97), (1.105, 3.25), (1.12, 3.62, 0.3),
         (0.86, 3.62, 0.3), (0.84, 3.35), (0.818, 3.08), (0.797, 2.82), (0.775, 2.58), (0.748, 2.32), (0.72, 2.06),
         (0.695, 1.86), (0.675, 1.72), (0.645, 1.56), (0.60, 1.44)]
# brain, front view: cerebrum above the eyes, temporal lobes lower at the sides; brainstem on the midline
BRAIN_R = [(0, 0.045), (0.13, 0.055), (0.245, 0.10), (0.318, 0.18), (0.348, 0.28), (0.34, 0.38), (0.31, 0.47),
           (0.262, 0.545), (0.205, 0.575), (0.15, 0.555), (0.11, 0.515), (0.075, 0.49), (0.04, 0.488), (0, 0.49)]
LENS_Y = 0.505          # hypothalamus and pituitary: midline, about eye level, deep in the head

# kidney outline (head units), viewer's-left kidney, hilum facing the midline (+x), centred on (0, 0)
KIDNEY = [(0, -0.245), (-0.082, -0.222), (-0.124, -0.158), (-0.137, -0.06), (-0.133, 0.05), (-0.115, 0.152),
          (-0.07, 0.222), (0, 0.247), (0.058, 0.228), (0.094, 0.178), (0.094, 0.11, 0.5), (0.056, 0.066),
          (0.044, 0.0), (0.056, -0.066), (0.094, -0.11, 0.5), (0.096, -0.172), (0.062, -0.226)]
KID_L = (-0.285, 2.57, 11)     # viewer's left = the person's RIGHT kidney (a little lower), tilt in degrees
KID_R = (0.285, 2.515, -11)    # viewer's right = the person's LEFT kidney


def _kidney_pts(spec, k):
    cx, cy, tilt = spec
    pts = KIDNEY if cx < 0 else flip(KIDNEY)
    return scale_pts(rot_pts(pts, tilt), k, cx * k, cy * k)


def _adrenals(k):
    """The person's right adrenal (viewer's left) is a pyramid capping the upper pole; the left adrenal
    (viewer's right) is a crescent along the medial edge above the hilum [ANAT]."""
    # right adrenal: rounded triangle, base along the top of the upper pole
    ra = [(-0.205, 2.105, 0.55), (-0.15, 2.205), (-0.105, 2.318, 0.6), (-0.19, 2.34), (-0.29, 2.338, 0.6),
          (-0.262, 2.24)]
    # left adrenal: crescent, convex side medial, hugging the medial upper border of the left kidney
    la = [(0.165, 2.10, 0.6), (0.135, 2.18), (0.13, 2.27), (0.152, 2.36, 0.6), (0.19, 2.33), (0.198, 2.25),
          (0.215, 2.17), (0.232, 2.115, 0.6)]
    return spline(scale_pts(ra, k)), spline(scale_pts(la, k))


def figure(k, kidneys=True):
    """The person, in viewBox units with the centre line at x 0 and the crown at y 0 (k = head height).
    kidneys=False leaves out the kidneys and adrenals, so the caller can draw them later, over the zoom cones."""
    S = lambda pts: scale_pts(pts, k)
    body = spline(S(mirror(BODY_R)))
    arms = [spline(S(ARM_R)), spline(S(flip(ARM_R)))]
    head = spline(S(mirror(HEAD_R)))
    ears = [spline(S(EAR_R), closed=False), spline(S(flip(EAR_R)), closed=False)]
    skin = arms + [body]
    o = ['<g mask="url(#scx-fade)">']
    o += [f'<path d="{d}" fill="{SKIN}" stroke="{SKIN_LN}" stroke-width="2.2" stroke-linejoin="round"/>' for d in skin]
    o += [f'<path d="{d}" fill="url(#scx-skin)"/>' for d in skin]
    # collarbones and the armpit creases, drawn faint
    for s in (1, -1):
        o.append(f'<path d="M{s * 0.07 * k:.1f},{1.205 * k:.1f} C{s * 0.25 * k:.1f},{1.235 * k:.1f} {s * 0.42 * k:.1f},'
                 f'{1.24 * k:.1f} {s * 0.6 * k:.1f},{1.30 * k:.1f}" fill="none" stroke="#D5AE9F" stroke-width="1.3" '
                 'stroke-linecap="round" opacity=".8"/>')
        o.append(f'<path d="M{s * 0.655 * k:.1f},{1.62 * k:.1f} C{s * 0.665 * k:.1f},{1.70 * k:.1f} {s * 0.668 * k:.1f},'
                 f'{1.76 * k:.1f} {s * 0.664 * k:.1f},{1.82 * k:.1f}" fill="none" stroke="#D5AE9F" stroke-width="1.1" '
                 'stroke-linecap="round" opacity=".7"/>')
    o.append(f'<g clip-path="url(#scx-torso)">{_spine(k)}{_kidneys(k) if kidneys else ""}</g>')
    o.append("</g>")
    # head on top of the neck
    o += [f'<path d="{d}" fill="{SKIN}" stroke="{SKIN_LN}" stroke-width="1.6" stroke-linecap="round"/>' for d in ears]
    o.append(f'<path d="{head}" fill="url(#scx-face)" stroke="{SKIN_LN}" stroke-width="1.8"/>')
    o.append(_brain_front(k))
    return "".join(o), body


def _brain_front(k):
    S = lambda pts: scale_pts(pts, k)
    d = spline(S(mirror(BRAIN_R)))
    o = [f'<path d="{d}" fill="url(#scx-brain)" stroke="{BRAIN_LN}" stroke-width="1.2" opacity=".95"/>']
    # the long fissure between the hemispheres and a few folds, mirrored
    o.append(f'<path d="M0,{0.05 * k:.1f} V{0.33 * k:.1f}" stroke="{BRAIN_LN}" stroke-width="1.1" opacity=".75"/>')
    folds = [[(0.05, 0.11), (0.12, 0.13), (0.17, 0.10)], [(0.20, 0.16), (0.26, 0.20), (0.30, 0.17)],
             [(0.06, 0.22), (0.14, 0.24), (0.22, 0.25), (0.27, 0.30)], [(0.29, 0.36), (0.24, 0.40), (0.18, 0.43)],
             [(0.08, 0.33), (0.15, 0.35), (0.19, 0.32)], [(0.22, 0.50), (0.27, 0.47), (0.30, 0.42)]]
    for f in folds:
        for s in (1, -1):
            pts = [(s * x * k, y * k) for x, y in f]
            o.append(f'<path d="{spline(pts, closed=False)}" fill="none" stroke="{BRAIN_FOLD}" stroke-width="1.15" '
                     'stroke-linecap="round"/>')
    # brainstem
    o.append(f'<path d="M{-0.05 * k:.1f},{0.49 * k:.1f} C{-0.048 * k:.1f},{0.56 * k:.1f} {-0.042 * k:.1f},{0.62 * k:.1f} '
             f'{-0.036 * k:.1f},{0.68 * k:.1f} L{0.036 * k:.1f},{0.68 * k:.1f} C{0.042 * k:.1f},{0.62 * k:.1f} '
             f'{0.048 * k:.1f},{0.56 * k:.1f} {0.05 * k:.1f},{0.49 * k:.1f} Z" fill="#E7AFBE" stroke="{BRAIN_LN}" '
             'stroke-width=".9" opacity=".9"/>')
    # hypothalamus (orange) and pituitary (purple) where the lens sits
    o.append(f'<ellipse cx="0" cy="{(LENS_Y - 0.02) * k:.1f}" rx="{0.05 * k:.1f}" ry="{0.026 * k:.1f}" fill="url(#scx-hypo)" '
             f'stroke="{HYPO_LN}" stroke-width=".7"/>'
             f'<circle cx="0" cy="{(LENS_Y + 0.035) * k:.1f}" r="{0.022 * k:.1f}" fill="url(#scx-pit)" stroke="{PIT_LN}" '
             'stroke-width=".7"/>')
    return "".join(o)


def _spine(k):
    """Vertebral bodies T10 to L5 (faint bone), behind the kidneys."""
    o = []
    y = 1.96
    while y < 3.55:
        h = 0.118 if y < 2.4 else 0.13
        w = 0.17 if y < 2.4 else 0.2
        o.append(f'<rect x="{-w / 2 * k:.1f}" y="{y * k:.1f}" width="{w * k:.1f}" height="{h * k:.1f}" rx="{0.03 * k:.1f}" '
                 f'fill="{BONE}" stroke="{BONE_LN}" stroke-width="1"/>')
        y += h + 0.03
    return f'<g opacity=".95">{"".join(o)}</g>'


def _kidneys(k):
    o = []
    for spec in (KID_L, KID_R):
        pts = _kidney_pts(spec, k)
        o.append(f'<path d="{spline(pts)}" fill="url(#scx-kid)" stroke="{KID_LN}" stroke-width="1.2"/>')
        # soft highlight on the outer curve
        cx, cy, tilt = spec
        s = -1 if cx < 0 else 1
        hl = [(cx + s * 0.07, cy - 0.16), (cx + s * 0.1, cy - 0.05), (cx + s * 0.092, cy + 0.07)]
        o.append(f'<path d="{spline(scale_pts(rot_pts(hl, tilt, cx, cy), k), closed=False)}" fill="none" '
                 'stroke="#E9958A" stroke-width="2.2" stroke-linecap="round" opacity=".75"/>')
    ra, la = _adrenals(k)
    for d in (ra, la):
        o.append(f'<path d="{d}" fill="url(#scx-adr)" stroke="{CORTEX_LN}" stroke-width="1.1"/>')
    return "".join(o)


# ============================================================== magnified brain (side view, facing left)
def brain_side():
    """Midline (sagittal) view in local units (about 124 x 100): cerebrum with folds, corpus callosum,
    thalamus, the HYPOTHALAMUS (orange) and the PITUITARY (purple) on its stalk below it, brainstem and
    cerebellum.  Returns (markup, hypothalamus centre, pituitary centre)."""
    cere = [(-60, 6), (-58.5, -12), (-50, -29), (-34, -42), (-12, -49), (11, -48), (32, -40), (48, -27), (58, -10),
            (61, 6), (57, 18), (45, 21), (31, 17), (20, 10), (9, 9), (-2, 13, 0.6), (-14, 16), (-30, 16), (-46, 13)]
    o = [f'<path d="{spline(cere)}" fill="url(#scx-brain)" stroke="{BRAIN_LN}" stroke-width="1.3"/>']
    folds = ["M-44,-14 C-38,-26 -24,-35 -8,-38 C9,-40 26,-35 38,-24",
             "M-53,-4 C-50,-14 -44,-22 -36,-28", "M-24,-44 C-21,-39 -16,-37 -12,-39",
             "M2,-48 C3,-43 6,-40 8,-36", "M24,-44 C23,-39 26,-35 31,-33",
             "M46,-24 C40,-16 37,-6 37,4", "M37,4 C43,3 50,3 57,1",
             "M-52,8 C-44,5 -36,6 -29,9", "M-34,-24 C-30,-18 -25,-16 -20,-17"]
    o += [f'<path d="{d}" fill="none" stroke="{BRAIN_FOLD}" stroke-width="1.3" stroke-linecap="round"/>' for d in folds]
    # corpus callosum (pale band) and the thalamus
    cc = "M-27,2 C-26,-11 -12,-19 4,-19 C19,-19 30,-13 32,-5 C33,-1 30,1.5 26,1"
    o.append(f'<path d="{cc}" fill="none" stroke="#C88D9F" stroke-width="7.6" stroke-linecap="round"/>'
             f'<path d="{cc}" fill="none" stroke="#FBE9EE" stroke-width="5.6" stroke-linecap="round"/>')
    o.append(f'<ellipse cx="3" cy="1.5" rx="11" ry="6.4" fill="#EBB2C2" stroke="{BRAIN_LN}" stroke-width=".9"/>')
    # brainstem: midbrain, pons (bulge in front) and medulla
    o.append(f'<path d="M5,8 C9,14 10,20 9,26 C13,30 14,36 13,42 C13,47 14,52 15,57 L7.5,57 C6.6,52 5.6,47 4.6,43 '
             f'C1,40 -1,34 0,28 C1,22 2,15 0,10 Z" fill="#E4A7B6" stroke="{BRAIN_LN}" stroke-width="1"/>')
    # cerebellum with its folds
    cbl = [(18, 22), (30, 18.5), (42, 21), (50, 29), (48, 39), (37, 45), (25, 43), (17, 35)]
    o.append(f'<path d="{spline(cbl)}" fill="#DD9FB1" stroke="{BRAIN_LN}" stroke-width="1.1"/>')
    for i in range(4):
        o.append(f'<path d="M{20 + i * 1.4:.1f},{25 + i * 5:.1f} C{28 + i:.1f},{22.5 + i * 5:.1f} {38 + i * .5:.1f},'
                 f'{24 + i * 5:.1f} {47 - i * 1.6:.1f},{28.5 + i * 4.6:.1f}" fill="none" stroke="#C37C95" stroke-width="1" '
                 'stroke-linecap="round"/>')
    # hypothalamus: below and in front of the thalamus, floor of the third ventricle
    hx, hy = -10.5, 10.5
    o.append(f'<circle cx="{hx}" cy="{hy}" r="11" fill="{HYPO}" opacity=".22"/>'
             f'<ellipse cx="{hx}" cy="{hy}" rx="7.6" ry="5" fill="url(#scx-hypo)" stroke="{HYPO_LN}" stroke-width="1" '
             f'transform="rotate(-12 {hx} {hy})"/>')
    # pituitary on its stalk (infundibulum), sitting below the hypothalamus
    px, py = -15.5, 25.5
    o.append(f'<path d="M-11.5,15 C-12.5,18 -13.5,20 -14.2,21.6" stroke="#B9708F" stroke-width="2.6" stroke-linecap="round" fill="none"/>'
             f'<ellipse cx="{px}" cy="{py}" rx="6.4" ry="4.8" fill="url(#scx-pit)" stroke="{PIT_LN}" stroke-width="1"/>')
    return "".join(o), (hx, hy), (px, py)


# ============================================================== magnified adrenal (cut open)
def adrenal_close():
    """The person's right adrenal sitting on the upper pole of the kidney, cut open to show the outer
    layer (cortex, makes cortisol) and the core (medulla, makes adrenaline).  Local units, centre (0, 0).
    Returns (markup, cortex point, medulla point) for the leader lines."""
    kid = [(-70, 60), (-66, 30), (-52, 13), (-30, 4), (-6, 1), (18, 4), (40, 12), (56, 26), (64, 46), (64, 62)]
    o = [f'<path d="{spline(kid, closed=False)} L64,90 L-70,90 Z" fill="url(#scx-kid)" stroke="{KID_LN}" stroke-width="1.4"/>',
         '<path d="M-50,27 C-37,15 -18,10 0,10" fill="none" stroke="#E9958A" stroke-width="3" stroke-linecap="round" opacity=".7"/>']
    # adrenal: pyramid capping the kidney, its base following the kidney's curve
    adr = [(-5, -48, 0.5), (9, -29), (24, -9, 0.75), (31, 4, 0.45), (9, 2.5), (-15, 3), (-36, 7, 0.45), (-31, -7, 0.75),
           (-18, -29)]
    o.append(f'<path d="{spline(adr)}" fill="url(#scx-adr)" stroke="{CORTEX_LN}" stroke-width="1.5"/>')
    # cut face: a thin core of medulla inside a thick band of cortex
    med = [(-5, -27, 0.55), (3, -16), (10, -5, 0.6), (-5, -3.5), (-19, -3, 0.6), (-13, -15)]
    o.append(f'<path d="{spline(med)}" fill="{MEDULLA}" stroke="{MEDULLA_LN}" stroke-width="1.1"/>')
    # leader anchors on the LEFT half (the labels sit to the inset's left): mid-cortex band, mid-medulla
    return "".join(o), (-20, -15), (-5, -11)


def cort(x, y, r=4.6):
    """Gold dot: cortisol."""
    return f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="url(#scx-cort)" stroke="{CORT_LN}" stroke-width=".8"/>'


def marker(x, y, n, fill):
    return (f'<circle cx="{x:.1f}" cy="{y:.1f}" r="9" fill="{fill}" stroke="#FFFFFF" stroke-width="2"/>'
            + T(round(x, 1), round(y + 3.9, 1), str(n), 11, 800, "#FFFFFF", "middle"))


def arrow_head(x, y, ang, size, color):
    """Solid triangle with its tip at (x, y), pointing along `ang` degrees."""
    a = math.radians(ang)
    ux, uy = math.cos(a), math.sin(a)
    bx, by = x - ux * size, y - uy * size
    px, py = -uy * size * 0.55, ux * size * 0.55
    return f'<path d="M{x:.1f},{y:.1f} L{bx + px:.1f},{by + py:.1f} L{bx - px:.1f},{by - py:.1f} Z" fill="{color}"/>'


def signal_path(p0, c1_, c2_, p3, width=3.2, head=8.5, halo=True):
    """Blue stress-signal arrow along one cubic Bezier, with its head on the end tangent.  The line stops
    short of the tip so the head's point is sharp."""
    ang = math.degrees(math.atan2(p3[1] - c2_[1], p3[0] - c2_[0]))
    a = math.radians(ang)
    q3 = (p3[0] - math.cos(a) * head * 0.7, p3[1] - math.sin(a) * head * 0.7)
    d = (f"M{p0[0]:.1f},{p0[1]:.1f} C{c1_[0]:.1f},{c1_[1]:.1f} {c2_[0]:.1f},{c2_[1]:.1f} {q3[0]:.1f},{q3[1]:.1f}")
    o = ""
    if halo:
        o += f'<path d="{d}" stroke="#FFFFFF" stroke-width="{width + 3}" fill="none" stroke-linecap="round" opacity=".85"/>'
    o += f'<path d="{d}" stroke="{SIGNAL}" stroke-width="{width}" fill="none" stroke-linecap="round"/>'
    return o + arrow_head(p3[0], p3[1], ang, head, SIGNAL)


def leader(pts, color, w=1.1):
    d = "M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in pts)
    return (f'<path d="{d}" fill="none" stroke="#FFFFFF" stroke-width="{w + 2.6}" stroke-linejoin="round" '
            f'stroke-linecap="round"/><path d="{d}" fill="none" stroke="{color}" stroke-width="{w}" stroke-linejoin="round"/>')


# ============================================================== picture 1: the stress system
A_W, A_H = 760, 292
FX, FY, FK = 352, 5, 76.0        # figure centre line, crown, head height (viewBox units)
BI_C, BI_R = (104, 86), 80       # brain inset: big enough that every label sits inside its frame
AI_C, AI_R = (214, 244), 44      # adrenal inset, beside the figure; its labels sit to its LEFT, clear of its cone
NX, NW = 486, 274                # notes column: left edge and width
KEY_PAD = 27                     # KEY box height = KEY_PAD + 15.5 per row (title band plus bottom padding)

# The four steps of the stress response [SMITH06][SAP00].  "Pea-sized" pituitary: NIH MedlinePlus.
# Each step is two lines, so the KEY below has room for its fourth row (the yellow adrenal glands).
STEPS = [
    ("THE ALARM", "When stress hits, your hypothalamus, deep in the brain, sends out a signal called CRH."),
    ("THE RELAY", "Your pea-sized pituitary gland answers with ACTH, which travels through the blood."),
    ("THE RESPONSE", "Your adrenal glands, on your kidneys, release cortisol. It raises blood sugar for quick "
                     "fuel."),
    ("THE BRAKE", "Cortisol tells the brain to ease off. When stress never lets up, the alarm stays on."),
]


def notes_col(t, y0):
    """Numbered steps (badge, caps title, wrapped text) from y0 down; returns markup and the bottom y."""
    c1, deep = t["c1"], t["deep"]
    o, y = [], y0
    for i, (title, text) in enumerate(STEPS):
        lines = wrap(text, NW - 30, 10.4, 500)
        o.append(marker(NX + 9, y + 1, i + 1, c1))
        o.append(T(NX + 26, y + 5, title, 11, 800, deep, ls=0.6))
        o.append(T(NX + 26, y + 19, lines, 10.4, 500, INK, lh=1.25))
        y += 19 + 13 * (len(lines) - 1) + 17
    return "".join(o), y


def _adrenal_swatch(cx, cy):
    """A small yellow adrenal (the same rounded pyramid and gradient as the figure) for the KEY."""
    pts = [(cx, cy - 6.5, 0.55), (cx + 4.5, cy - 1), (cx + 7.5, cy + 5.2, 0.6), (cx, cy + 5.6), (cx - 7.5, cy + 5.2, 0.6),
           (cx - 4.5, cy - 1)]
    return f'<path d="{spline(pts)}" fill="url(#scx-adr)" stroke="{CORTEX_LN}" stroke-width="1"/>'


def key_col(x, y, w):
    """KEY for picture 1: every symbol drawn on it, and the one colour-coded organ that has no label of its own."""
    rows = [
        (lambda cx, cy: signal_path((cx - 13, cy), (cx - 6, cy), (cx + 2, cy), (cx + 13, cy), 2.6, 7.5, False),
         "Blue arrow: a stress signal (CRH, ACTH)"),
        (lambda cx, cy: cort(cx, cy, 4.6), "Gold dot: cortisol"),
        (lambda cx, cy: (f'<path d="M{cx - 13},{cy} H{cx + 5}" stroke="{BRAKE}" stroke-width="2.4" stroke-dasharray="6 4" '
                         'stroke-linecap="round"/>' + arrow_head(cx + 13, cy, 0, 8, BRAKE)),
         "Grey dashed arrow: the brake"),
        (_adrenal_swatch, "Yellow: adrenal glands, on the kidneys"),
    ]
    # 27 + 15.5 per row: about as much clear space under the last row as above "KEY" (21 left the adrenal row's
    # swatch and descenders 2 units off the bottom border).  art_axis sizes the box with the same formula.
    h = KEY_PAD + 15.5 * len(rows)
    o = [f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="#FFFFFF" stroke="#D9CFBF" stroke-width="1.3"/>',
         T(x + 12, y + 15, "KEY", 10, 800, INK, ls=1.3)]
    for i, (sw, lab) in enumerate(rows):
        cy = y + 28.5 + i * 15.5
        o.append(sw(x + 26, cy) + T(x + 48, cy + 3.8, lab, 10.4, 600, INK))
    return "".join(o), h


def art_axis(t):
    c1, deep = t["c1"], t["deep"]
    k = FK
    fig, body_d = figure(k, kidneys=False)      # the kidneys and adrenals go on after the zoom cones, below
    out = [f'<defs>{figure_defs()}'
           f'<clipPath id="scx-torso"><path d="{body_d}"/></clipPath>'
           f'<linearGradient id="scx-fadeg" x1="0" y1="{3.2 * k:.1f}" x2="0" y2="{3.56 * k:.1f}" gradientUnits="userSpaceOnUse">'
           '<stop offset="0" stop-color="#fff"/><stop offset="1" stop-color="#000"/></linearGradient>'
           '<mask id="scx-fade" maskUnits="userSpaceOnUse" x="-140" y="-10" width="280" height="330">'
           '<rect x="-140" y="-10" width="280" height="330" fill="url(#scx-fadeg)"/></mask>'
           f'<clipPath id="scx-bi"><circle cx="{BI_C[0]}" cy="{BI_C[1]}" r="{BI_R - 1}"/></clipPath>'
           f'<clipPath id="scx-ai"><circle cx="{AI_C[0]}" cy="{AI_C[1]}" r="{AI_R - 1}"/></clipPath>'
           '</defs>']
    G = lambda x, y: (FX + x * k, FY + y * k)          # head units -> viewBox

    out.append(f'<g transform="translate({FX},{FY})">{fig}</g>')

    # ---- zoom cones, callout style: drawn OVER the figure (and under the arrows, dots, labels and lens rings
    # that follow), so each cone runs unbroken from its inset to its lens ring.  Drawn under the figure, the
    # adrenal cone vanished at the arm, seemed to point at the elbow, and left stubs in the arm-to-torso gap.
    lens_c, lens_r = G(0, LENS_Y + 0.012), 9.5
    adr_c, adr_r = G(-0.205, 2.23), 11.5
    for (c, r), (ic, ir) in (((lens_c, lens_r), (BI_C, BI_R)), ((adr_c, adr_r), (AI_C, AI_R))):
        (a1, b1), (a2, b2) = tangents(c, r, ic, ir)
        out.append(f'<path d="M{a1[0]:.1f},{a1[1]:.1f} L{b1[0]:.1f},{b1[1]:.1f} L{b2[0]:.1f},{b2[1]:.1f} '
                   f'L{a2[0]:.1f},{a2[1]:.1f} Z" fill="{c1}" fill-opacity=".035"/>')
        for a, b in ((a1, b1), (a2, b2)):
            out.append(f'<path d="M{a[0]:.1f},{a[1]:.1f} L{b[0]:.1f},{b[1]:.1f}" stroke="{c1}" stroke-width="1" '
                       'stroke-opacity=".45"/>')
    # The kidneys and adrenals are drawn here, over the cones (and only here: a second copy would double their
    # see-through highlights), so the adrenal cone's lower edge passes BEHIND the viewer's-left kidney instead of
    # crossing it like a stray leader line; the lens rings, arrows, dots and labels drawn below stay on top.  The
    # kidneys sit above the hip fade and inside the torso, so they need neither the fade mask nor the torso clip.
    out.append(f'<g transform="translate({FX},{FY})">{_kidneys(k)}</g>')

    # ---- ACTH: the blue signal runs from the pituitary down to both adrenals
    top, fork = G(0, LENS_Y + 0.075), G(0, 1.90)
    trunk = f"M{top[0]:.1f},{top[1]:.1f} L{fork[0]:.1f},{fork[1]:.1f}"
    out.append(f'<path d="{trunk}" stroke="#FFFFFF" stroke-width="6.2" stroke-linecap="round" opacity=".85"/>'
               f'<path d="{trunk}" stroke="{SIGNAL}" stroke-width="3.2" stroke-linecap="round"/>')
    for sx, ex, ey in ((-1, -0.205, 2.085), (1, 0.172, 2.078)):
        out.append(signal_path(fork, G(0, 1.97), G(ex * 0.75, 1.975), G(ex, ey), 3.2, 8.5))
    out.append(pill(FX, FY + 1.47 * k, "ACTH", 10.5, SIGNAL, "#FFFFFF", SIGNAL)[0])

    # ---- cortisol leaving both adrenals into the body (gold dots)
    for x, y in ((-0.395, 2.06), (-0.47, 2.15), (-0.43, 2.27), (0.39, 2.25), (0.455, 2.14)):
        out.append(cort(*G(x, y), 4.2))

    # ---- the brake: cortisol travels back up to the brain (grey dashed loop, viewer's right)
    p0, tip = G(0.255, 2.11), G(0.13, LENS_Y + 0.01)
    loop = (f"M{p0[0]:.1f},{p0[1]:.1f} C{G(0.78, 1.93)[0]:.1f},{G(0.78, 1.93)[1]:.1f} {G(1.30, 2.02)[0]:.1f},"
            f"{G(1.30, 2.02)[1]:.1f} {G(1.29, 1.45)[0]:.1f},{G(1.29, 1.45)[1]:.1f} "
            f"C{G(1.28, 0.95)[0]:.1f},{G(1.28, 0.95)[1]:.1f} {G(0.98, 0.46)[0]:.1f},{G(0.98, 0.46)[1]:.1f} "
            f"{tip[0] + 8:.1f},{tip[1]:.1f}")
    out.append(f'<path d="{loop}" fill="none" stroke="#FFFFFF" stroke-width="5.6" stroke-linecap="round" opacity=".9"/>'
               f'<path d="{loop}" fill="none" stroke="{BRAKE}" stroke-width="2.6" stroke-dasharray="7 5" '
               'stroke-linecap="round"/>' + arrow_head(tip[0], tip[1], 180, 9, BRAKE))
    for x, y in ((1.235, 1.78), (1.282, 1.33), (1.205, 0.88)):
        out.append(cort(*G(x, y), 4.2))
    out.append(marker(*G(1.29, 1.08), 4, c1))

    # ---- kidneys and spine, labelled in the quiet lower torso.  The two kidney leaders run up to each
    # kidney's lower pole (the KIDNEY outline's bottom point, turned by its tilt).
    kx, ky = G(0, 2.985)
    kid_pill, kid_w = pill(kx, ky, "Kidneys", 9.8, KID_B, "#FFFFFF", KID_A, 700, 5)
    for spec in (KID_L, KID_R):
        cx_k, cy_k, tilt = spec
        a = math.radians(tilt)
        pole = G(cx_k - 0.247 * math.sin(a), cy_k + 0.247 * math.cos(a))
        side = -1 if cx_k < 0 else 1
        out.append(leader([(kx + side * (kid_w / 2 - 9), ky - 6.5), (pole[0] - side * 1.5, pole[1] + 1.2)], KID_LN, 1.1))
    out.append(kid_pill)
    sx_, sy_ = G(0, 3.30)
    out.append(pill(sx_, sy_, "Spine", 9.8, "#7D6A4C", "#FFFFFF", BONE_LN, 700, 5)[0])

    # ---- lens on the head, and the brain inset.  Every label sits inside the circle (checked in
    # _check_inset below); the CRH arrow runs from the hypothalamus down to the pituitary.
    out.append(f'<circle cx="{lens_c[0]:.1f}" cy="{lens_c[1]:.1f}" r="{lens_r}" fill="#FFFFFF" fill-opacity=".25" '
               f'stroke="{c1}" stroke-width="1.6"/>')
    bx, by = BI_C
    out.append(f'<circle cx="{bx}" cy="{by}" r="{BI_R + 2.2}" fill="#FFFFFF"/>'
               f'<circle cx="{bx}" cy="{by}" r="{BI_R}" fill="url(#scx-lens)"/>')
    bmark, hpos, ppos = brain_side()
    bs, bdx, bdy = 0.92, bx + 8, by - 14
    out.append(f'<g clip-path="url(#scx-bi)"><g transform="translate({bdx},{bdy}) scale({bs})">{bmark}</g></g>')
    out.append(f'<circle cx="{bx}" cy="{by}" r="{BI_R}" fill="none" stroke="{c1}" stroke-width="2"/>')
    hx, hy = bdx + hpos[0] * bs, bdy + hpos[1] * bs
    px, py = bdx + ppos[0] * bs, bdy + ppos[1] * bs
    out.append(signal_path((hx - 7, hy + 1.5), (hx - 25, hy + 1), (px - 23, py + 2), (px - 6.6, py + 1), 2.3, 6.2, False))
    pills = [(hx - 47, hy + 9, "CRH", 10, SIGNAL, SIGNAL), (hx - 16, hy - 37, "Hypothalamus", 10.2, "#A34612", HYPO),
             (px - 1, py + 42, "Pituitary gland", 10.2, PIT_LN, PIT)]
    out.append(leader([(hx - 3, hy - 4.5), (hx - 11, hy - 29)], HYPO_LN, 1.2))
    out.append(leader([(px - 0.5, py + 4.6), (px - 1, py + 34.5)], PIT_LN, 1.2))
    for cx_p, cy_p, text, size, fg, edge in pills:
        out.append(pill(cx_p, cy_p, text, size, fg, "#FFFFFF", edge)[0])
    _check_inset(BI_C, BI_R, [(cx_p, cy_p, tw(text, size, 800) + 12, size * 1.5) for cx_p, cy_p, text, size, _, _ in pills])
    out.append(marker(hx + 9, hy - 13, 1, c1) + marker(px + 14, py + 2, 2, c1))
    out.append(T(bx, by + BI_R + 14, "Your brain, seen from the side", 10.2, 700, deep, "middle", italic=True))

    # ---- adrenal inset: cut open to show its two layers.  Its labels sit in the clear space to its left,
    # away from the zoom cone, which leaves the circle on its right.
    ax, ay = AI_C
    out.append(f'<circle cx="{adr_c[0]:.1f}" cy="{adr_c[1]:.1f}" r="{adr_r}" fill="#FFFFFF" fill-opacity=".2" '
               f'stroke="{c1}" stroke-width="1.6"/>')
    out.append(f'<circle cx="{ax}" cy="{ay}" r="{AI_R + 2.2}" fill="#FFFFFF"/>'
               f'<circle cx="{ax}" cy="{ay}" r="{AI_R}" fill="url(#scx-lens)"/>')
    amark, cpt, mpt = adrenal_close()
    asx, adx, ady = 0.8, ax + 4, ay + 6
    out.append(f'<g clip-path="url(#scx-ai)"><g transform="translate({adx},{ady}) scale({asx})">{amark}</g></g>')
    out.append(f'<circle cx="{ax}" cy="{ay}" r="{AI_R}" fill="none" stroke="{c1}" stroke-width="2"/>')
    for x, y in ((19, -27), (28, -20), (34, -10)):     # cortisol leaving the outer layer, inside the circle
        out.append(cort(ax + x, ay + y, 3.6))
    out.append(T(ax + 2, ay + 33, "Kidney", 10.2, 800, "#FFFFFF", "middle"))
    cx_, cy_ = adx + cpt[0] * asx, ady + cpt[1] * asx
    mx_, my_ = adx + mpt[0] * asx, ady + mpt[1] * asx
    lx = ax - AI_R - 11                                  # right edge of the label column (text-anchor end)
    out.append(T(lx, ay - 38, ["One adrenal", "gland, cut open"], 10.2, 700, deep, "end", lh=1.18, italic=True))
    out.append(leader([(lx + 3, ay - 11.5), (cx_, cy_)], CORTEX_LN, 1.1))
    out.append(T(lx, ay - 8, ["Outer layer:", "makes cortisol"], 10.2, 700, "#7A4E08", "end", lh=1.18))
    out.append(leader([(lx + 3, ay + 18.5), (mx_ - 13, ay + 18.5), (mx_, my_)], MEDULLA_LN, 1.1))
    out.append(T(lx, ay + 22, ["Core: makes", "adrenaline"], 10.2, 700, MEDULLA_LN, "end", lh=1.18))
    out.append(marker(ax - AI_R * 0.71, ay - AI_R * 0.71, 3, c1))

    # ---- the four steps and the KEY
    notes, _ = notes_col(t, 12)
    out.append(notes)
    kh = KEY_PAD + 15.5 * 4
    kmark, _ = key_col(NX, A_H - kh - 2, NW)
    out.append(kmark)
    return svg(A_W, A_H, "".join(out),
               "Your stress system. A person's body with the brain, spine, kidneys and the yellow adrenal glands on top "
               "of the kidneys. A close-up of the brain from the side shows the hypothalamus sending CRH to the "
               "pituitary gland, which sends ACTH through the blood to the adrenal glands. A close-up of one adrenal "
               "gland shows its outer layer, which makes cortisol, and its core, which makes adrenaline. A dashed loop "
               "shows cortisol travelling back to the brain as a brake.")


def _check_inset(c, r, boxes, margin=2.0):
    """Fail the build if a rounded label (cx, cy, w, h) pokes out of its inset circle."""
    for cx, cy, w, h in boxes:
        cap = h / 2
        for ex in (cx - (w / 2 - cap), cx + (w / 2 - cap)):
            d = math.hypot(ex - c[0], cy - c[1]) + cap
            assert d <= r - margin, f"label at ({cx:.0f},{cy:.0f}) leaves its inset by {d - r + margin:.1f}"


# ============================================================== picture 2: the cortisol clock
B_W, B_H = 760, 146
PX0, PX1, PY0, PY1 = 40, 470, 20, 114        # plot area (y grows down)
WAKE = 6.5                                     # 6:30 AM wake-up in this example day


def _hx(h):
    return PX0 + (h - 6) / 18 * (PX1 - PX0)


def _vy(v):
    return PY1 - v * (PY1 - PY0 - 6)


# Healthy day [DEBONO09][STALDER16]: already rising before waking, a sharp rise over the first 30-45 min after
# waking (peak), then a steady fall through the day to its lowest near midnight (shape only; no units).
HEALTHY_PTS = [(6.0, 0.47), (6.5, 0.60), (6.85, 0.86), (7.15, 1.0), (7.6, 0.95), (8.5, 0.84), (9.5, 0.73),
               (11, 0.61), (12.5, 0.53), (14, 0.46), (15.5, 0.39), (17, 0.33), (18.5, 0.27), (20, 0.21),
               (21.5, 0.15), (23, 0.09), (24, 0.065)]
# Long-term stress [MILLER07][ADAM17]: a flatter day: a smaller morning rise, then a slower fall, so evening levels
# stay above the healthy curve.  The evening tail still falls toward night (0.29 at 9 PM, 0.20 at midnight):
# those studies show flatter slopes, not a lost night-time low, which is the Cushing's pattern the front sends
# to a doctor [ES08CS].
STRESSED_PTS = [(6.0, 0.38), (6.5, 0.44), (6.9, 0.55), (7.2, 0.60), (7.8, 0.60), (9, 0.585), (10.5, 0.56),
                (12, 0.53), (13.5, 0.495), (15, 0.46), (16.5, 0.42), (18, 0.38), (19.5, 0.335), (21, 0.29),
                (22.5, 0.245), (24, 0.20)]


def _curve(pts):
    return spline([(_hx(h), _vy(v)) for h, v in pts], closed=False)


def art_clock(t):
    c1, deep = t["c1"], t["deep"]
    o = []
    # plot frame: day band, a quieter night band (from 8:30 PM, inside the quiet phase that starts near 7:45 PM
    # [DEBONO09], and wide enough to hold the "Wired at night" label), recessive grid
    nx = _hx(20.5)
    o.append(f'<rect x="{PX0}" y="{PY0 - 6}" width="{PX1 - PX0}" height="{PY1 - PY0 + 6}" rx="6" fill="#FFFBF3"/>'
             f'<rect x="{nx:.1f}" y="{PY0 - 6}" width="{PX1 - nx:.1f}" height="{PY1 - PY0 + 6}" fill="#EEF0F8"/>'
             f'<rect x="{PX1 - 6}" y="{PY0 - 6}" width="6" height="{PY1 - PY0 + 6}" fill="#EEF0F8"/>')
    for v in (0.25, 0.5, 0.75):
        o.append(f'<path d="M{PX0},{_vy(v):.1f} H{PX1}" stroke="#EFE5D6" stroke-width="1"/>')
    # "12 AM", not "MIDNIGHT": the longer word ran into "9 PM"
    ticks = [(6, "6 AM"), (9, "9 AM"), (12, "NOON"), (15, "3 PM"), (18, "6 PM"), (21, "9 PM"), (24, "12 AM")]
    for h, lab in ticks:
        x = _hx(h)
        anchor = "start" if h == 6 else ("end" if h == 24 else "middle")
        o.append(f'<path d="M{x:.1f},{PY1} V{PY1 + 4}" stroke="#B9AE9C" stroke-width="1.2"/>'
                 + T(round(x, 1), PY1 + 16, lab, 9.8, 700, INK2, anchor, ls=0.3))
    o.append(f'<path d="M{PX0},{PY1} H{PX1}" stroke="#B9AE9C" stroke-width="1.4"/>')
    # y axis: an arrow labelled "more cortisol"
    o.append(f'<path d="M{PX0 - 12},{PY1} V{PY0 + 2}" stroke="#9A8F7E" stroke-width="1.6"/>'
             + arrow_head(PX0 - 12, PY0 - 4, -90, 7, "#9A8F7E"))
    o.append(f'<text x="{PX0 - 18}" y="{(PY0 + PY1) / 2:.1f}" font-family="Inter, Helvetica, Arial, sans-serif" '
             f'font-size="9.8" font-weight="800" fill="{INK2}" text-anchor="middle" letter-spacing="0.6" '
             f'transform="rotate(-90 {PX0 - 18} {(PY0 + PY1) / 2:.1f})">MORE CORTISOL</text>')
    # wake-up line and the night moon
    wx = _hx(WAKE)
    o.append(f'<path d="M{wx:.1f},{PY0 - 4} V{PY1}" stroke="#C9B07A" stroke-width="1.2" stroke-dasharray="2 3"/>')
    o.append(T(round(wx + 4, 1), PY1 - 6, "Wake up", 9.8, 700, "#8A6A1E"))
    mx, my = PX1 - 14, PY0 + 6
    o.append(f'<path d="M{mx + 4:.1f},{my - 6:.1f} a7,7 0 1 0 5,11.5 a5.6,5.6 0 1 1 -5,-11.5z" fill="#8C95BE"/>')
    o.append(T(round(mx - 8, 1), my + 4, "Night", 9.8, 700, "#5D668F", "end"))
    # the two curves: a soft green wash under the healthy one
    h_d = _curve(HEALTHY_PTS)
    o.append(f'<path d="{h_d} L{_hx(24):.1f},{PY1} L{_hx(6):.1f},{PY1} Z" fill="{HEALTHY}" fill-opacity=".09"/>')
    o.append(f'<path d="{_curve(STRESSED_PTS)}" fill="none" stroke="#FFFFFF" stroke-width="6" stroke-linecap="round"/>'
             f'<path d="{_curve(STRESSED_PTS)}" fill="none" stroke="{STRESSED}" stroke-width="2.8" stroke-dasharray="7 5" '
             'stroke-linecap="round"/>')
    o.append(f'<path d="{h_d}" fill="none" stroke="#FFFFFF" stroke-width="6.4" stroke-linecap="round"/>'
             f'<path d="{h_d}" fill="none" stroke="{HEALTHY}" stroke-width="3.2" stroke-linecap="round"/>')
    # labels sit in clear space beside each curve: no grid line, curve or band edge runs under any of them
    # (plain text, no stroked halo: stroked text prints as a Type 3 font)
    px_, py_ = _hx(7.15), _vy(1.0)
    o.append(f'<circle cx="{px_:.1f}" cy="{py_:.1f}" r="3.4" fill="{HEALTHY}" stroke="#fff" stroke-width="1.4"/>')
    # The peak label sits ABOVE the falling curve: baseline 2 units above the peak (y 24; caps from about y 16.6,
    # inside the day band that starts at y 14), so the green line and its halo pass under the text with a clear gap.
    # At py_ + 4 the label's baseline sat on the curve and the green stroke ran into the foot of "He".
    o.append(T(round(px_ + 10, 1), round(py_ - 2, 1), "Healthy peak, 30 to 45 min after waking", 10.2, 700, HEALTHY))
    o.append(f'<circle cx="{_hx(24):.1f}" cy="{_vy(0.065):.1f}" r="3.4" fill="{HEALTHY}" stroke="#fff" stroke-width="1.4"/>')
    o.append(T(round(_hx(7.7), 1), round(_vy(0.5) + 12, 1), "Tired in the morning", 10.2, 700, STRESSED))
    o.append(T(round(_hx(23.6), 1), round(_vy(0.5) + 11, 1), "Wired at night", 10.2, 700, STRESSED, "end"))

    # ---- KEY cards on the right (each names its line)
    kx, kw = 492, 268
    cards = [(HEALTHY, False, "GREEN LINE: HEALTHY RHYTHM",
              "High soon after you wake, to get you going. Lowest near midnight, so you can sleep."),
             (STRESSED, True, "RED DASHED LINE: LONG STRESS",
              "The curve can flatten: a smaller morning rise and higher evening levels.")]
    y = PY0 - 6
    for col, dashed, title, text in cards:
        lines = wrap(text, kw - 22, 10.2, 500)
        h = 26 + 12.8 * len(lines)
        dash = ' stroke-dasharray="6 4"' if dashed else ""
        o.append(f'<rect x="{kx}" y="{y}" width="{kw}" height="{h:.1f}" rx="7" fill="#FFFFFF" stroke="#E3D9C9" stroke-width="1.2"/>'
                 f'<rect x="{kx}" y="{y}" width="5" height="{h:.1f}" rx="2.5" fill="{col}"/>'
                 f'<path d="M{kx + 14},{y + 13} H{kx + 36}" stroke="{col}" stroke-width="3"{dash} stroke-linecap="round"/>'
                 + T(kx + 43, y + 16.6, title, 10, 800, col, ls=0.5)
                 + T(kx + 14, y + 31, lines, 10.2, 500, INK, lh=1.25))
        y += h + 7
    o.append(T(kx + 2, round(y + 7, 1), "Shapes after Debono 2009, Stalder 2016, Miller 2007", 9.8, 500, "#6A737A",
               italic=True))
    return svg(B_W, B_H, "".join(o),
               "Cortisol across one day. A green healthy curve rises soon after waking, peaks 30 to 45 minutes later, "
               "then falls to its lowest near midnight. A red dashed curve for long-term stress starts lower in the "
               "morning and stays higher in the evening: tired in the morning, wired at night.")


# ============================================================== this sheet's icons (64 x 64, stroke style)
# Registered into kit.ICONS under "sc-" names so the back page's lifestyle band can use them too.
SC_ICONS = {
    # a worried face: eyes and a wavy mouth (anxious, irritable or low)
    "sc-mood": ('<circle cx="32" cy="32" r="23"/><path d="M24 27v.5M40 27v.5"/>'
                '<path d="M21 43c3.6-3.2 7.4-3.2 11 0s7.4 3.2 11 0"/><path d="M20 21l7 3M44 21l-7 3"/>'),
    # two people side by side (time with friends and family)
    "sc-people": ('<circle cx="22" cy="20" r="8"/><circle cx="43" cy="22" r="7"/>'
                  '<path d="M7 55c0-10 7-18 15-18s15 8 15 18"/><path d="M33 40c3-3 6-4 10-4 7 0 13 7 13 16"/>'),
    # a tired battery-face: drooping eyes (tired even after sleep)
    "sc-tired": ('<rect x="8" y="17" width="44" height="30" rx="5"/><path d="M52 26h4v12h-4"/>'
                 '<rect x="13" y="22" width="8" height="20" rx="1.5" fill="currentColor" stroke="none"/>'
                 '<path d="M28 33c2 2 5 2 7 0M39 33c2 2 5 2 7 0"/>'),
}
for _k, _v in SC_ICONS.items():
    kit.ICONS.setdefault(_k, _v)


def _ic(name, size="0.3in", sw=3.3):
    return icon(name, size, sw=sw)


# ============================================================== front page blocks
# Signs that the stress system is working overtime: [MAYO] for sleep, tiredness, headache and muscle tension,
# focus, anxiety, irritability or low mood, stomach upset; [SEGER04] immunity; [EPEL00] belly fat.
# "Sick more often" wears the thermometer: the kit's microbe (a ring with straight rays) read as a sun, and the back
# page's "Morning light" hexagon is a sun.
SIGNS = [("moon", "Trouble<br>sleeping"), ("sc-tired", "Tired, even<br>after sleep"),
         ("headache", "Headaches,<br>tight muscles"), ("brain", "Foggy, hard<br>to focus"),
         ("sc-mood", "Anxious, cranky<br>or low"), ("gut", "Upset<br>stomach"),
         ("thermo", "Sick more<br>often"), ("waist", "Slow belly<br>weight gain")]
# "Slow" on purpose.  The red flag on the same page names the telling signs instead of only the speed: a rounder,
# redder face (moon face, facial plethora [ES08CS]) with FAST belly weight gain, so a patient can tell them apart.


def signs_block():
    tiles = "".join(f'<div class="scx-sg"><span class="scx-bx"></span>{_ic(ic)}<span class="scx-sl">{lab}</span></div>'
                    for ic, lab in SIGNS)
    return (f'<div class="scx-h"><span>When stress runs too long</span>'
            f'<i>tick the signs that fit you, then go over them with {{who}}</i></div><div class="scx-signs">{tiles}</div>')


def low_block():
    # [CADE16]: 58 studies, no substantiation that "adrenal fatigue" exists; not recognised by any
    # endocrinology society.  Habits that move the rhythm: [LEP01] light, [LEP97] sleep, [DRAKE13] caffeine and sleep.
    myth = ('<div class="scx-myth"><h4>Is it &ldquo;adrenal fatigue&rdquo;?</h4>'
            '<p>You may hear stress-tiredness called that, but it is <b>not a medical diagnosis</b>. A review of 58 '
            'studies found no proof that stress wears out the adrenal glands. What can change is your cortisol rhythm, '
            'and the daily habits on the back can help reset it.</p></div>')
    # [ES16AI] too little cortisol: fatigue with weight loss, dizziness or fainting on standing (low blood
    # pressure), salt craving, darker skin (primary disease), nausea, vomiting, belly pain.
    # [ES08CS] too much cortisol: central weight gain with a round, red face (facial plethora is one of the most
    # telling signs), wide reddish-purple stretch marks, easy bruising, weak thigh and upper-arm muscles, new high
    # blood pressure or blood sugar.
    # Steroid medicines: never stop suddenly [ES16AI][BEUS24].  [988] crisis line.  Signs of too much cortisol
    # are checked against [FLES21] as well as [ES08CS].
    low = ["Weight loss with deep tiredness", "Dizzy or faint when you stand", "Craving salt, darkening skin",
           "Nausea, vomiting or belly pain"]
    high = ["A rounder, redder face with fast belly weight gain", "Wide purple stretch marks",
            "Easy bruising, weak thigh muscles", "New high blood pressure or blood sugar"]
    li = lambda xs: "".join(f"<li>{x}</li>" for x in xs)
    flags = ('<div class="scx-flag"><h4>See a doctor soon if you notice</h4><div class="scx-cols">'
             f'<div><b>Signs of too <em>little</em> cortisol</b><ul>{li(low)}</ul></div>'
             f'<div><b>Signs of too <em>much</em> cortisol</b><ul>{li(high)}</ul></div></div>'
             '<p class="scx-foot"><b>On a steroid such as prednisone?</b> Never stop it suddenly. '
             '<b>Thinking of harming yourself?</b> Call or text <b>988</b>, any time.</p></div>')
    return f'<div class="scx-low">{myth}{flags}</div>'


def front(t, ed):
    return ('<div class="scx">'
            f'<div class="scx-h"><span>Your stress system</span><i>the HPA axis: H for hypothalamus, P for pituitary, '
            f'A for adrenal glands</i></div>'
            f'<div class="art scx-art">{art_axis(t)}</div>'
            f'<div class="scx-h"><span>Your cortisol clock</span><i>one day, two rhythms</i></div>'
            f'<div class="art scx-art">{art_clock(t)}</div>'
            f'{signs_block()}{low_block()}'
            '<p class="scx-src">Sources: Endocrine Society guidelines (adrenal insufficiency 2016, 2024; '
            'Cushing&rsquo;s 2008); Pituitary Society 2021; Cadegiani 2016; Smith 2006; Miller 2007.</p>'
            '</div>')


CSS = r"""
.scx .scx-h{display:flex;align-items:baseline;gap:10px;margin:0.04in 0 0.02in;font:900 11pt Merriweather,Georgia,serif;
  color:var(--c1);letter-spacing:.02em;text-transform:uppercase}
.scx .scx-h::after{content:"";flex:1;height:1.5px;background:var(--c2);opacity:.45;align-self:center}
.scx .scx-h i{order:2;font:italic 600 7.8pt Inter,sans-serif;color:#5E686F;letter-spacing:0;text-transform:none}
.scx .scx-h span{order:1}
.scx .scx-h::after{order:3}
.scx .scx-art svg{display:block;width:100%;height:auto}
.scx .scx-signs{display:grid;grid-template-columns:repeat(8,1fr);gap:0.05in}
.scx .scx-sg{position:relative;display:flex;flex-direction:column;align-items:center;text-align:center;background:var(--tint);
  border:1px solid #EFDFC3;border-radius:7px;padding:4px 3px 4px}
.scx .scx-sg .ic{color:var(--c1)}
.scx .scx-sl{font-size:7.8pt;line-height:1.2;color:#2B3236;margin-top:2px}
.scx .scx-bx{position:absolute;top:4px;right:4px;width:0.12in;height:0.12in;border:1.5px solid var(--deep);border-radius:2px;background:#fff}
.scx .scx-low{display:grid;grid-template-columns:2.55in 1fr;gap:0.1in;margin-top:0.07in;align-items:stretch}
.scx .scx-myth{background:var(--soft);border-radius:8px;padding:0.06in 0.12in 0.07in}
.scx .scx-myth h4,.scx .scx-flag h4{margin:0 0 2px;font:900 10pt Merriweather,Georgia,serif;color:var(--deep)}
.scx .scx-myth p{margin:0;font-size:8pt;line-height:1.32;color:#2B3236}
.scx .scx-myth b{color:var(--deep)}
.scx .scx-flag{border:1.5px solid #C0392B;background:#FDF3F1;border-radius:8px;padding:0.06in 0.12in 0.06in}
.scx .scx-flag h4{color:#A5281E}
/* the "too much" list carries the longest line ("A rounder, redder face with fast belly weight gain"), so it gets
   the wider share; every item in both lists stays on one line */
.scx .scx-cols{display:grid;grid-template-columns:1fr 1.36fr;gap:0.12in}
.scx .scx-cols b{display:block;font:800 7.6pt Inter,sans-serif;color:#7A2219;letter-spacing:.02em}
.scx .scx-cols em{font-style:normal;text-decoration:underline;text-underline-offset:1.5px}
.scx .scx-cols ul{margin:1px 0 0;padding:0;list-style:none}
.scx .scx-cols li{position:relative;padding-left:9px;font-size:7.8pt;line-height:1.27;color:#2B3236}
.scx .scx-cols li::before{content:"";position:absolute;left:0;top:4.5px;width:4px;height:4px;border-radius:50%;background:#C0392B}
.scx .scx-foot{margin:4px 0 0;padding-top:3px;border-top:1px solid #EBC9C3;font-size:7.8pt;line-height:1.3;color:#2B3236}
.scx .scx-foot b{color:#A5281E}
.scx .scx-src{margin:4px 0 0;font-size:7pt;color:#5E686F;line-height:1.3}
/* ---- footers and the back page.  The kit gives the back page no sheet class, so the band title carries an empty
   <i class="scx-bk"> marker and every back rule is scoped by .sheet.back:has(.scx-bk); the front is found by its
   .scx body.  No other sheet carries either class. ---- */
/* Standard 3 (7 pt floor): the shared kit sets all fine print (footers, badge, header sub-lines, sizes, dose
   sub-lines, rhythm) to 7 pt, so nothing is pinned here; the label facts, the most-read small text, get 7.2 pt. */
.sheet.back:has(.scx-bk) .col .key{font-size:7.2pt;line-height:1.3}
/* FDA disclaimer [CFR93]: bold, boxed, and linked by the diamond that ends every product statement.  8 pt, not
   7: Inter Bold's lowercase o is 0.564 em, so 8 pt gives a 4.5 pt (1/16 in) o, which meets the rule even read the
   strict way (lowercase o, as in 21 CFR 101.2(c)); 7 pt passes only on capital height.  The sheet code wraps onto
   two lines so the box is wide enough to stay three lines tall. */
.sheet.back:has(.scx-bk) .foot .disc{font-size:8pt;font-weight:700;color:#36424A;line-height:1.28;
  border:1px solid #8D99A1;border-radius:4px;padding:3px 7px 4px;max-width:5.88in}
.sheet.back:has(.scx-bk) .foot>div:last-child{flex:none;width:1.62in}
.sheet.back:has(.scx-bk) .foot .code{white-space:normal;line-height:1.3}
.scx-dia{color:var(--c1);margin-left:2px}
.scx-nw{white-space:nowrap}
/* hex band: a deeper amber, so the habit lines read at 4.5:1 or better from one end of the band to the other */
.sheet.back:has(.scx-bk) .band{background:linear-gradient(120deg,#8C510B,#A65F0E)}
.sheet.back:has(.scx-bk) .band h2 small{color:#FFF6EE}
.sheet.back:has(.scx-bk) .life p{color:#FFFFFF}
/* product headers: the same deeper amber, so the white titles and 7 pt sub-lines clear 4.5:1 everywhere on the
   gradient (white on #A65F0E about 4.9:1, on #7A480A about 7.6:1); the theme's gold measured 2.5-3.3:1 on paper.
   Sub-lines at full opacity, not the kit's .92. */
.sheet.back:has(.scx-bk) .col .need{background:linear-gradient(160deg,#7A480A,#A65F0E)}
.sheet.back:has(.scx-bk) .col .need i{opacity:1}
/* room for the full label lines and the longer check: smaller hexes, tighter gaps, two write-in lines */
.sheet.back:has(.scx-bk) .band{padding-bottom:.13in}
.sheet.back:has(.scx-bk) .band h2{margin-bottom:.07in}
.sheet.back:has(.scx-bk) .life.hex .disc2{width:.76in;height:.66in}
.sheet.back:has(.scx-bk) .life .disc2 svg{width:.42in!important;height:.42in!important}
.sheet.back:has(.scx-bk) .life b{margin:.05in 0 .02in}
.sheet.back:has(.scx-bk) .ns-title{margin-top:.1in}
.sheet.back:has(.scx-bk) .notes{margin-top:.08in}
.sheet.back:has(.scx-bk) .notes .ln:last-child{display:none}
.sheet.back:has(.scx-bk) .notes .ln{height:.22in}
.sheet.back:has(.scx-bk) .recby{margin-top:.06in}
/* need headers: every title and every sub-line is one line here, so one short height lines them all up */
.sheet.back:has(.scx-bk) .col .need{min-height:.42in;padding-left:.05in;padding-right:.05in}
/* column widths follow the content: Calm's label is two lines (plus its old name), Adrenal Renew's is ten
   ingredients long, so Calm gives up a little width (its name, photo and dose still fit) and Adrenal Renew takes it */
.sheet.back:has(.scx-bk) .cols{grid-template-columns:1fr 1fr .84fr 1fr 1.16fr!important}
/* every column has three name-and-size lines; one line height for both keeps the bullets level */
.sheet.back:has(.scx-bk) .col .pick .nm,.sheet.back:has(.scx-bk) .col .pick .sz{line-height:9.9pt}
/* daily rhythm: a count never splits from its unit.  Morning holds two products (one wraps), so it gets a
   full-height left slot and Evening sits over Bedtime on the right.  The medicine check gets 1.5 parts of the row:
   its five lines need the width, and the rhythm, with four products, still ends above it */
.sheet.back:has(.scx-bk) .slot li em{white-space:nowrap}
.sheet.back:has(.scx-bk) .rhythm{grid-template-columns:1.2fr 1fr;grid-auto-rows:auto}
.sheet.back:has(.scx-bk) .rhythm .slot:first-child{grid-row:span 2}
.sheet.back:has(.scx-bk) .duo{grid-template-columns:1fr 1.5fr}
"""

# ============================================================== back page helpers
def sf(text):
    """A structure/function statement, ending in the diamond that ties it to the boxed FDA disclaimer in the footer
    [CFR93].  The diamond is drawn (kit.DIAMOND, inline SVG), never a font glyph, so the PDF has no Type 3 font;
    the last word and the diamond never split across lines."""
    head, _, last = text.rpartition(" ")
    return f'{head} <span class="scx-nw">{last}<span class="scx-dia">{kit.DIAMOND}</span></span>'


# ============================================================== the sheet
SHEET = {
    "slug": SLUG, "code": "ND-EN-801", "order": 18, "theme": "energy", "series": "Energy and Stress Series",
    "title": "Stress and Cortisol", "sub": "How your stress system works, and how to steady it",
    # [SMITH06] the HPA axis and cortisol's feedback; [SAP00] fuel and focus; [MILLER07][ADAM17] a flattened
    # daily rhythm with long stress.
    "intro": ("Your brain and <b>adrenal glands</b> answer every stress, from a deadline to a sleepless night, as one "
              "team: the <b>HPA axis</b>. Its messenger, the hormone <b>cortisol</b>, gives you fuel and focus, then "
              "switches off. When stress never lets up, the system stays on alert and your daily rhythm can flatten: "
              "<b>tired in the morning, wired at night</b>."),
    "front": front,
    "css": CSS,
    "back": {
        # [LEP01] morning light; [BALB23] slow, exhale-focused breathing; [HHS18] 150 minutes a week;
        # [AASM15] 7+ hours, [LEP97] one short night raises next-evening cortisol; [DRAKE13] a late cup costs sleep;
        # [HEIN03] support from a friend lowers the cortisol response.
        # The empty <i class="scx-bk"> is the back page's marker: every back-page rule in CSS is scoped by it.
        "life_title": 'Steady Your Stress Response<i class="scx-bk"></i>',
        "life_sub": "Six daily habits that help reset your cortisol rhythm",
        "style": "hex",
        "life": [("sun", "Morning light", "Get outdoors within an hour of waking."),
                 ("breath", "Slow breathing", "Five minutes a day of long, slow exhales."),
                 ("walk", "Move daily", "150 minutes a week. A brisk walk counts."),
                 ("moon", "Protect sleep", "7+ hours. Short nights raise cortisol."),
                 ("coffee", "Coffee by noon", "Late coffee can cost you sleep."),
                 ("sc-people", "Lean on people", "Friends soften your stress response.")],
        # Every structure/function statement ends in the diamond (sf), which points to the boxed FDA disclaimer.
        "cols": [
            # [ARU24][AKH22] ashwagandha; [TALB13] Relora; [OLSS09] rhodiola; [HID19] L-theanine
            {"p": "sc_cortisol_pro", "need": "Stress response", "needsub": "stress herbs (adaptogens)",
             "start": True,
             "bullets": [sf("Supports a healthy stress response"), sf("Helps maintain healthy cortisol levels")],
             "dose": "dose_from_db"},
            # Header sub-lines are the plain-language layer, so no ingredient jargon there: cordyceps is a mushroom
            # (Cordyceps militaris fruiting body, ND422); GABA and L-theanine are both amino acids (ND856).  Each
            # sub-line stays one line in its column, so the headers stay one height.
            {"p": "sc_balance", "need": "Daytime energy", "needsub": "mushroom plus stress herbs",
             "bullets": [sf("Supports energy and stamina under stress"), sf("Helps your body adapt to daily demands")],
             "dose": "dose_from_db"},
            {"p": "sc_calm", "need": "Quiet a busy mind", "needsub": "calming amino acids",
             "bullets": [sf("Promotes a calm, relaxed mood"), sf("Helps you unwind in the evening")],
             "dose": "dose_from_db"},
            # [PICK20] stress and low magnesium feed each other (the magnesium-stress vicious circle)
            {"p": "sc_mag_calm_pro", "need": "Restore magnesium", "needsub": "magnesium, inositol, taurine",
             "bullets": [sf("Supports relaxation and restful sleep"), "Stress can use up magnesium"],
             "dose": "dose_from_db"},
            # Framed around its real use (topic research: Asher's 2026-10-05 advice to step a patient down from
            # Ortho's Adren-All), so the back never says the adrenals need "renewing" after the front's myth box
            # [CADE16].  It is itself a glandular (300 mg dried cow adrenal), the product class [AKTURK18] found
            # carrying unlabelled thyroid and steroid hormones, so it is ONLY for someone who already takes one and is
            # coming off it: "sched": [] keeps it out of the daily rhythm and its pill total (7 pills and 1 scoop),
            # and the header says "only".  Bullet 1 says it REPLACES the glandular the patient is on (taken on top of
            # another brand's glandular it would double the glandular dose), and the medicine check repeats "never with
            # another".  The dose bar (products.d) gives the one patient it is for a time and a way off: "2 capsules at
            # breakfast" (label: two capsules daily; NutriDyn's Stress Essentials chart V3, 10/2024: with food, earlier
            # in the day) / "then step down as directed".  Wording sized to the column: both bullets fit four lines like
            # every other column, so "In each serving" stays level, and each dose line fits one line, so the dose bars do.
            # [PATAK04] vitamin C in the adrenal gland; pantothenic acid builds coenzyme A for steroid synthesis.
            {"p": "sc_adrenal_renew", "need": "Coming off a glandular?", "needsub": "only if you already take one",
             "bullets": ["Replaces your current glandular (dried cow adrenal)",
                         sf("B vitamins and vitamin C for a healthy stress response")],
             "sched": [], "dose": "dose_from_db"},
        ],
        # One list for both editions; {who} is the only difference.  Each line is sized to the panel (1.5 parts of
        # the row): eleven lines in both editions, the same height the four-line list had, so the page keeps its
        # footer room.
        # 1. Ashwagandha: [AKH22] 300-600 mg/d studied (mostly root extracts); Sensoril's own stress trials used
        #    125-500 mg/d.  150 mg (Cortisol Pro) + 400 mg (Balance at 3 capsules once a day, half its label dose,
        #    which the dose bar says) = 550 mg a day as scheduled; at the label dose it would be 950 mg.  It can add
        #    to sedatives (benzodiazepines, sleep pills) and [SHARMA18] raised T3/T4, so on thyroid pills it can push
        #    levels higher: "can make sleep, anxiety or thyroid pills stronger".  [BJORN20] Bjornsson HK et al.
        #    Liver Int 2020;40:825-9, PMID 31991029, doi:10.1111/liv.14393 (five cases of ashwagandha liver injury,
        #    all with jaundice after 2-12 weeks; one also took rhodiola) and NIH LiverTox (ashwagandha entry, named
        #    source, not reopened here: nih.gov is blocked) -> "Yellow skin or eyes, or dark urine? Stop both and call
        #    a doctor" ("both": the bullet names two ashwagandha products, and stopping only one would leave the herb
        #    in; a doctor in both editions: possible liver injury needs a medical visit, not a pharmacy call).
        # 2. Glandulars: [AKTURK18] hidden thyroid and steroid hormones; steroids are never stopped suddenly
        #    [ES16AI][BEUS24].  Who Adrenal Renew is for sits in its column ("only if you already take one", "Replaces
        #    your current glandular"); "never with another" says it here too, so nobody doubles a glandular dose by
        #    adding it on top of another brand's.  Sized to stay two lines in both editions (page 2 keeps its footer room).
        # 3. Antidepressants: [VDIER09] van Diermen D et al. J Ethnopharmacol 2009;122:397-401, PMID 19168123,
        #    doi:10.1016/j.jep.2009.01.007 (rhodiola root extracts inhibit MAO-A and MAO-B, so rhodiola may add to
        #    MAOIs and other antidepressants).  Asian ginseng can lower blood sugar, with mixed evidence that it
        #    changes warfarin's effect (NCCIH herb-drug interaction digest, seen through web search); holy basil lowers
        #    blood sugar [JAMS17] and lengthened clotting time in animals [SINGH01].  "Heart medicine": Balance's label
        #    caution, "If taking heart medications... inform your healthcare practitioner".  Hence "can change how
        #    some of these work".
        # 4. Daily totals as scheduled (Adrenal Renew is outside the rhythm): rhodiola 350 mg (Cortisol Pro 250 +
        #    Balance 100); L-theanine 400 mg (Cortisol Pro 100 + Calm 200 + Mag Calm Pro 100); B6 5 mg (Mag Calm
        #    Pro), 65 mg only with Adrenal Renew's 60 mg, against the US upper limit of 100 mg and EFSA's 12 mg
        #    [EFSA23], hence the tingling caution on that clause.
        # 5. Pregnancy: Cortisol Pro's label "Do not use if pregnant" (nursing: consult), Balance's "Do not use if
        #    pregnant or nursing", and "If pregnant, nursing... consult your healthcare practitioner" on Calm, Mag
        #    Calm Pro and Adrenal Renew; none of the five labels claims pregnancy safety, so the line covers them all.
        "rx": [
            "<b>Ashwagandha</b> (Cortisol Pro, Balance): 550 mg a day. It can make sleep, anxiety or thyroid pills "
            "stronger: tell {who} if you take any. Yellow skin or eyes, or dark urine? Stop both and call a doctor.",
            "<b>Adrenal Renew is a glandular</b> (dried cow adrenal): never with another. On prednisone, hydrocortisone "
            "or thyroid pills? Ask {who} first, and stop glandulars slowly.",
            "<b>On warfarin, an antidepressant, or diabetes or heart medicine?</b> Rhodiola, ginseng and holy basil can "
            "change how some of these work. Ask {who} first.",
            "<b>A day adds up to</b> 350 mg rhodiola and 400 mg L-theanine. With Adrenal Renew, B6 reaches 65 mg: "
            "tingling or numb hands or feet? Tell {who}.",
            "<b>Pregnant, trying to get pregnant or breastfeeding?</b> Skip Cortisol Pro and Balance, and ask {who} "
            "before the others.",
        ],
    },
}
