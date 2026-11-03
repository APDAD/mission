"""Joint Pain and Osteoarthritis (ND-MS-602), Pain and Movement Series.  slug "joint-pain".

Self-contained sheet module: the front art, the front copy and the back data all live here.
Shared helpers come only from svgkit / kit.  Every SVG id starts with "jp-" and every CSS class
with "jpn-", so nothing collides with other sheets in the all-sheets bundle.  Built 2026-11-03
from the topic brief (scratchpad topics/topic-joint-pain.json, research rank 4 of 10).

FRONT, top to bottom
  intro -> one knee drawn as a front-to-back slice (a coronal section), split down the middle:
  the left half healthy, the right half with osteoarthritis (thin, cracked cartilage with a bald
  patch, bone spurs growing as lips of bone at the joint edges, a swollen red lining with extra
  fluid and loose flakes, a squeezed joint space, a torn meniscus pushed out past the rim).
  Matching I-beam brackets measure the joint space bone end to bone end on both sides (the squeezed
  one without arrowheads, so it stays an I-beam).  The four numbered OA steps each have a leader to
  the tissue they name.  Each half has a magnified circle of its shin-bone (tibial) cartilage, the
  same way up as the circle (fluid, cartilage, bone), tied to a dashed ring on the knee by a dashed
  connector, and one three-row KEY names every colour and symbol on the knee and in both circles.  Each meniscus rim meets the joint
  lining (the capsule holds it), with fluid pockets above it; on the worn side the pushed-out
  meniscus presses into the swollen lining -> how it can feel / get checked promptly -> what raises
  your risk -> good to know (1 lb -> 4 lb, where OA strikes as a front-view figure, 150 min, a pain
  scale).
  Anatomy: a right knee seen from the front, so the outer (lateral) side with the fibula is on the
  viewer's left and the inner (medial) side is on the right, where knee OA most often starts.
  Proportions: condyle width : femoral shaft about 2.7 : 1; cartilage about 3% of joint width
  (2 to 3 mm on an 80 mm knee), drawn a little thicker so the change reads; meniscus a wedge about
  twice cartilage height at its rim (Sophia Fox 2009, doi:10.1177/1941738109350438, PMID 23015907).
BACK: lifestyle band, 5 NutriDyn products (label facts in products.d/joint-pain.json): four make the
  daily plan and the fifth, Curcumin 400X, is the willow-free choice instead of Inflam-Eze Plus, so it
  stays out of the daily rhythm (morning and evening; no bedtime products, so that empty slot is
  hidden).  One check list reads right in both editions through {who}.  The back page is reached in
  CSS through the empty .jpn-bk marker in the lifestyle title; BACK_CSS gives every product name a
  two-line band (so all five columns line up row by row) and tightens spacing so that band and the
  six-point check list fit (all fine print, the START HERE badge and the diamond come from the kit).

SOURCES (tags used in the comments next to each number or claim)
  [GBD21]     GBD 2021 Osteoarthritis Collaborators. Lancet Rheumatol 2023;5:e508-22. PMID 37675071,
              doi:10.1016/S2665-9913(23)00163-7: 595 million people (7.6% of the world) had OA in 2020;
              the knee is the most common site.
  [KHAN04]    Khan AM et al. Ann R Coll Surg Engl 2004;86:119-21. PMID 15005931,
              doi:10.1308/003588404322827518: groin and buttock pain are significantly more common in
              hip OA (groin pain 84.3% sensitive); 47% also feel it below the knee.
  [RODDY15]   Roddy E et al. Ann Rheum Dis 2015;74:156-63. PMID 24255544, doi:10.1136/annrheumdis-2013-203804:
              symptomatic foot OA in 1 in 6 adults over 50; the big-toe joint (1st MTP) 7.8%, the most common.
  [KALICH08]  Kalichman L et al. Spine 2008;33:2560-5. PMID 18923337, doi:10.1097/BRS.0b013e318184ef95:
              lumbar facet-joint (spine) OA on CT in 59.6% of men and 66.7% of women (Framingham).
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
  Check panel (the herbal monographs; ema.europa.eu is blocked from this machine, so these were read
  through web-search summaries, 2026-11-03, not opened):
  [EMA-SALIX]   EU herbal monograph, willow bark (EMA/HMPC/80630/2016): not with hypersensitivity to
                salicylates; use with salicylates and other NSAIDs not recommended without medical advice;
                may increase the effect of anticoagulants such as coumarins.
  [EMA-CURCUMA] EU herbal monograph, turmeric (EMA/HMPC/329755/2017, 2018): not recommended with bile-duct
                obstruction, cholangitis, liver disease or gallstones (it stimulates bile).
  [COMM-E]      German Commission E, devil's claw: not with stomach or duodenal ulcers; with gallstones
                only after medical advice (the EU monograph EMA/HMPC/627057/2015 adds a warfarin bleeding
                caution).  Not re-confirmed this session; the panel line is an "ask first", not a rule.
  [TGA23]       TGA safety alert "Medicines containing turmeric or curcumin - risk of liver injury" (2023,
                https://www.tga.gov.au/safety/safety-alerts/medicines-containing-turmeric-or-curcumin-risk-liver-injury,
                read through web-search summaries 2026-11-03): rare liver injury; the risk may be higher with
                enhanced-absorption products and higher doses; people with liver problems should avoid them;
                watch for yellow skin or eyes, dark urine, unusual tiredness.  The sheet stacks two
                enhanced-absorption forms (CurQfen, BioCurc), hence the liver line and its stop sign.
  [MN-UL]       Institute of Medicine DRI report, 2001: adult upper limit for manganese 11 mg a day; MedlinePlus
                (manganese): people with chronic liver disease have trouble getting rid of manganese, so it can
                build up.  Chondro-Relief Intensive Care contains manganese ascorbate (Clinical Guide ND181, 2022);
                its only printed amount, 15 mg per 4 capsules, is from 2014 (products.d src), so the sheet prints
                no number and puts the product in the liver line.
  [ASA-HERB]    American Society of Anesthesiologists, as cited with Ang-Lee MK et al. JAMA 2001;286:208-16,
                PMID 11448284: tell the surgical team about herbal products and stop them about two weeks
                before surgery; ginger, turmeric, willow and devil's claw carry bleeding cautions.
  [CDC-AGS]     CDC "Products that may contain alpha-gal": gelatin and other products made from mammals (beef,
                pork) can trigger alpha-gal syndrome, the red-meat allergy spread by lone star tick bites.  CDC
                "Fast Facts: Products That May Contain Alpha-gal" (cdc.gov/alpha-gal-syndrome, read through a
                web-search summary 2026-11-03): there is no full list; providers can look for gelatin, glycerin,
                magnesium stearate and bovine extract, and each person's tolerance varies, so the panel says "ask
                first" for those and "skip" only for a product made from beef.  The CDC provider sheet
                (stacks.cdc.gov/view/cdc/131337) and University of Missouri Extension N1352 (2026, citing CDC) list
                gelatin capsules and magnesium stearate; both hosts are blocked from this machine, so neither was
                opened.  The products: Collagen Renew's only other ingredient is "Bovine Collagen Peptides"
                (labels.json R190), hence "skip".  Chondro-Relief Intensive Care: chondroitin sulfate is usually made
                from cow, pig, chicken or shark cartilage and no NutriDyn document here states its source; its only
                printed other ingredients are "Silicon dioxide, magnesium stearate, and gelatin" (2014 catalog,
                labels.json R160), the stearate not stated as vegetable.  Curcumin 400X: "Softgel (gelatin, sorbitol,
                glycerin, purified water, carob), coconut oil" (NutriDyn sell sheet Curcumin 400x SS ND466, Rev. 7/24,
                Dropbox Marketing Materials, read 2026-11-03).  Inflam-Eze Plus and Joint Eze use hypromellose
                (plant) capsules with vegetable magnesium stearate (their sell sheets, labels.json), so they are
                not named.
"""
import math
import os
import random

from kit import ICONS, icon
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
SPUR, SPUR_HI, SPUR_BASE = "#9C968A", "#C6BEAD", "#E2CA9C"                          # bone spur (bone greying to its tip)
CELL, CELL_NUC, LACUNA, LACUNA_EDGE = "#8668BF", "#47307D", "#F7F2FD", "#C3B4E4"     # cartilage cell (violet)
FIBER = "#5B9BD0"                                                                   # collagen fibers (blue)
GREEN, GREEN_DK = "#2E8A57", "#1F6B43"
RED, RED_DK = "#C23A2F", "#9C2B22"

# ============================================================== geometry (viewBox units)
W, H = 760, 418
CX = 380                       # the split line runs down the middle of the knee
FEM_TOP, TIB_BOT = 44, 344     # bone ends fade out above and below (local units): where the fade mask starts
FEM_CUT = FEM_TOP - 20         # the femur's cut top edge sits above the fade, in the fully masked zone, so the
                               # inner shell line that runs across it never shows as a pale "lid"
K, YJ = 1.12, 214              # the knee is drawn in local units and scaled by K about the joint line
DROP = 10                      # the worn inner condyle sits lower: a narrowed joint space
KEY_Y, KEY_H = 346, 68         # three-row KEY; its white box covers the faded shaft ends
TOP = 4                        # top margin above the heading pills (the art is drawn TOP units down)
INS_R = 63
INS_L, INS_W = (100, 92), (660, 92)   # magnified circles (healthy, worn)
# where the dashed rings sit on the TIBIAL cartilage (local u, healthy / worn), centred halfway through its thickness:
# the close-up circles show joint fluid on top, then cartilage, then bone, which is the shin bone's way up (the
# thigh bone's cartilage hangs under it, the other way up).  Each ring is in the clear window between its
# joint-space bracket (u -64 / +64) and the cartilage end or the meniscus tip, so a dashed connector can rise from
# it to its circle (the worn one between markers 1 and 2)
LENS_U = (-47, 80)
LENS_R = 10
SPACE_U = 64                   # the joint-space brackets, at the middle of each condyle


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
FEM_L = [(-42, FEM_CUT, 0), (-42, 84), (-45, 104), (-53, 121), (-67, 136), (-86, 149), (-103, 159), (-111, 170),
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

# joint lining (synovium): femur attachment -> tibia attachment.  The worn side bulges with extra fluid.  Each
# lining comes in to meet the outer rim of its meniscus at mid-height (the rim is held by the joint capsule), with
# the fluid pocket above it; on the worn side the pushed-out meniscus presses into the swollen lining.
SYN_L = [(CX - 103, 159), (CX - 114, 164), (CX - 123, 175), (CX - 128, 191), (CX - 128.4, 205), (CX - 123.6, 219),
         (CX - 122.8, 228.5), (CX - 121.6, 238), (CX - 116.3, 247.5)]
SYN_R = [(CX + 103, 159), (CX + 119, 162), (CX + 133, 173), (CX + 142, 190), (CX + 144.5, 209), (CX + 142.5, 224),
         (CX + 138, 234), (CX + 132.5, 246), (CX + 122, 255.5), (CX + 112, 258.5)]
MEN_W = (CX + 133, CX + 95)    # worn meniscus, outer and inner edge: pushed out past the plateau rim to the lining
VILLI_SKIP = (222, 241)        # no lining folds where the worn meniscus and the spur under it press on the lining


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


def _meniscus(fem_surf, tib_surf, x_out, x_in, h_out, worn, rim_y=None):
    """Wedge-shaped meniscus between the cartilage surfaces: in contact with the femur over its inner
    part, a free wedge at the rim.  x_out -> x_in may run either way.  The worn one is thinner, pushed out
    past the plateau rim (its outer part rests at rim_y, the height of the plateau edge) and split by one
    clean tear that opens at its inner edge."""
    n = 40
    xs = [x_out + (x_in - x_out) * i / n for i in range(n + 1)]
    ybs = [_y_at(tib_surf, x, min, clamp=True) - 0.9 for x in xs]
    yfs = [_y_at(fem_surf, x, max) for x in xs]
    if worn:   # the worn surfaces are frayed: rest the wedge on their smoothed line, so its edges stay clean
        ybs = [min(ybs[max(0, i - 3):i + 4]) for i in range(n + 1)]
        ybs = [sum(ybs[max(0, i - 3):i + 4]) / len(ybs[max(0, i - 3):i + 4]) for i in range(n + 1)]
        yfs = [None if v is None else max(w for w in yfs[max(0, i - 3):i + 4] if w is not None) for i, v in enumerate(yfs)]
    top, bot = [], []
    for i, (x, yb, yf) in enumerate(zip(xs, ybs, yfs)):
        if rim_y is not None:
            yb = min(yb, rim_y)
        h = h_out * (1 - i / n) ** 0.8 + 1.3
        ytop = yb - h
        if yf is not None:
            ytop = max(ytop, yf + 1.0)
        top.append((x, min(ytop, yb - 0.8)))
        bot.append((x, yb))
    sgn = -1 if x_out < x_in else 1
    t0, b0 = top[0][1], bot[0][1]
    if worn:   # a rounded outer face
        rim = [(x_out + sgn * 1.6, t0 * 0.72 + b0 * 0.28), (x_out + sgn * 2.3, (t0 + b0) / 2),
               (x_out + sgn * 1.6, t0 * 0.28 + b0 * 0.72)]
        step = 2
        pts = top[::step] + ([top[-1]] if n % step else []) + list(reversed(bot))[::step] + list(reversed(rim))
        body = path_d(pts)
    else:
        rim = [(x_out + sgn * 2.4, t0 * 0.55 + b0 * 0.45)]
        body = _poly(top + list(reversed(bot)) + rim)
    out = [f'<path d="{body}" fill="url(#jp-men)" stroke="{MEN_EDGE}" stroke-width="1" stroke-linejoin="round"/>']
    fibres = (0.36, 0.64) if not worn else (0.34,)
    for f in fibres:   # circumferential fibres
        stop = int(n * (0.78 if not worn else 0.4))
        line = [(x, yt + (yb - yt) * f) for (x, yt), (_, yb) in zip(top[1:stop], bot[1:stop])]
        out.append(f'<path d="{_line(line)}" fill="none" stroke="#FFFFFF" stroke-width=".8" opacity=".6"/>')
    if worn:   # one clean tear, running in from the free inner edge
        a, b = int(n * 0.36), n - 2
        line = [(x, yt + (yb - yt) * 0.56) for (x, yt), (_, yb) in zip(top[a:b + 1:2], bot[a:b + 1:2])]
        out.append(f'<path d="{path_d(line, closed=False)}" fill="none" stroke="{MEN_EDGE}" stroke-width="1.15" '
                   'stroke-linecap="round"/>')
    return "".join(out)


def _film(fs, ts, bow=5.0):
    """Joint fluid between two bone surfaces (the cartilage is drawn over it, so only the thin film between
    the cartilage shows).  At the notch end the film closes with a curved edge, the way fluid sits in a
    narrowing gap, instead of a straight cut."""
    fs, ts = list(fs), list(ts)
    if abs(fs[0][0] - CX) < abs(fs[-1][0] - CX):    # run both from the rim to the notch
        fs.reverse()
    if abs(ts[0][0] - CX) < abs(ts[-1][0] - CX):
        ts.reverse()
    a, b = fs[-1], ts[-1]
    out = -1 if a[0] < CX else 1                     # toward the rim, away from the notch
    c = ((a[0] + b[0]) / 2 + out * bow, (a[1] + b[1]) / 2)
    close = [((1 - t) ** 2 * a[0] + 2 * (1 - t) * t * c[0] + t * t * b[0],
              (1 - t) ** 2 * a[1] + 2 * (1 - t) * t * c[1] + t * t * b[1]) for t in (k / 12 for k in range(1, 12))]
    return f'<path d="{_poly(fs + close + list(reversed(ts)))}" fill="url(#jp-fluid)"/>'


def _lip(outline, sgn, i0, i1, height, peak=0.5, hook=0.0, sink=1.6):
    """A bone spur (osteophyte) as a lip of extra bone grown out of a bone outline: the outline between sample
    indices i0..i1 is pushed outward by a smooth bump that peaks at `peak` (0..1) and leans along the outline
    by `hook` (negative leans toward i0).  It shares the bone's edge stroke and sinks `sink` units into the bone,
    so no seam shows.  Returns (svg, tip point)."""
    pts = outline[i0:i1 + 1]
    n = len(pts)
    p = math.log(0.5) / math.log(peak)
    bump = [math.sin(math.pi * (k / (n - 1)) ** p) ** 1.8 for k in range(n)]
    outer = _offset(pts, [height * v for v in bump], sgn)
    for k in range(1, n - 1):
        (xa, ya), (xb, yb) = pts[k - 1], pts[k + 1]
        m = math.hypot(xb - xa, yb - ya) or 1
        s = hook * height * bump[k]
        outer[k] = (outer[k][0] + (xb - xa) / m * s, outer[k][1] + (yb - ya) / m * s)
    inner = _offset(pts, [-sink] * n, sgn)
    shell = _offset(outer, [-2.0 * v ** 0.5 for v in bump], sgn)    # the hard outer shell carries on into the lip
    tip = max(outer, key=lambda q: math.hypot(q[0] - pts[0][0], q[1] - pts[0][1]) + math.hypot(q[0] - pts[-1][0], q[1] - pts[-1][1]))
    svg_ = (f'<path d="{_poly(outer + list(reversed(inner)))}" fill="url(#jp-spur)"/>'
            f'<path d="{_line(shell)}" fill="none" stroke="#B5A88E" stroke-width=".6" opacity=".7"/>'
            f'<path d="{_line(outer)}" fill="none" stroke="{BONE_EDGE}" stroke-width="1.3" stroke-linejoin="round" '
            'stroke-linecap="round"/>')
    return svg_, tip


def _bracket(x, y0, y1, w=3.4):
    """A joint-space bracket: an I-beam between two bone ends with arrowheads pressing on its caps.  A squeezed
    gap (under 6 units, about 1.5 mm printed) keeps only the caps and the stem: arrowheads that short meet in the
    middle and the mark reads as an X, not as the KEY's I-beam."""
    d = f"M{_f(x - w)},{_f(y0)} H{_f(x + w)} M{_f(x - w)},{_f(y1)} H{_f(x + w)} M{_f(x)},{_f(y0)} V{_f(y1)}"
    if y1 - y0 < 6:
        return (f'<path d="{d}" stroke="#FFFFFF" stroke-width="3.2" stroke-linecap="round" fill="none"/>'
                f'<path d="{d}" stroke="{INK}" stroke-width="1.1" stroke-linecap="round" fill="none"/>')
    a = min(2.4, (y1 - y0) * 0.42)
    heads = (f"M{_f(x - 1.9)},{_f(y0 + a)} L{_f(x)},{_f(y0 + 0.5)} L{_f(x + 1.9)},{_f(y0 + a)} Z "
             f"M{_f(x - 1.9)},{_f(y1 - a)} L{_f(x)},{_f(y1 - 0.5)} L{_f(x + 1.9)},{_f(y1 - a)} Z")
    return (f'<path d="{d}" stroke="#FFFFFF" stroke-width="3.2" stroke-linecap="round" fill="none"/>'
            f'<path d="{heads}" fill="#FFFFFF" stroke="#FFFFFF" stroke-width="2" stroke-linejoin="round"/>'
            f'<path d="{d}" stroke="{INK}" stroke-width="1.1" stroke-linecap="round" fill="none"/>'
            f'<path d="{heads}" fill="{INK}"/>')


def _syn_band(pts, worn, rnd, skip=None):
    d = path_d(pts, closed=False)
    if not worn:
        return (f'<path d="{d}" fill="none" stroke="{LINING_EDGE}" stroke-width="6" stroke-linecap="round"/>'
                f'<path d="{d}" fill="none" stroke="{LINING}" stroke-width="4.2" stroke-linecap="round"/>'
                f'<path d="{d}" fill="none" stroke="{LINING_HI}" stroke-width="1.1" stroke-linecap="round" opacity=".9"/>')
    o = [f'<path d="{d}" fill="none" stroke="{INFL_EDGE}" stroke-width="10" stroke-linecap="round"/>',
         f'<path d="{d}" fill="none" stroke="{INFL}" stroke-width="7.8" stroke-linecap="round"/>']
    # finger-like folds (villi) of a swollen lining, reaching into the fluid (none in the `skip` y range, where
    # the pushed-out meniscus presses on the lining)
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
        if skip and skip[0] <= fy <= skip[1]:
            continue
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


def _near(curve, u, y):
    """Index of the outline sample nearest the local point (CX + u, y)."""
    return min(range(len(curve)), key=lambda i: (curve[i][0] - CX - u) ** 2 + (curve[i][1] - y) ** 2)


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
        o.append(_film(fs, ts))

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
    # (the worn surfaces show their fraying through the uneven thickness, the cracks and the keyed loose flakes;
    # no extra fray dots, which read as the KEY's "Lost cell" or as bubbles)
    o += [cart_fl, cart_tl, cart_fr, cart_tr]

    # ---- bone spurs (osteophytes): lips of extra bone growing out of the edges of the worn joint, where the
    # cartilage ends (femur: a beak hooking down past the cartilage edge; tibia: a shelf below the plateau rim)
    fpts = [(x, y) for x, y, _ in fem_s]
    tpts = [(x, y) for x, y, _ in tib_s]
    lip_f, tip_f = _lip(fpts, sf, _near(fpts, 111.5, 187.0), _near(fpts, 108.9, 165.8), 12.5, peak=0.36, hook=-0.62)
    lip_t, tip_t = _lip(tpts, st, _near(tpts, 117.9, 236.6), _near(tpts, 113.3, 253.9), 10.0, peak=0.3, hook=-0.5)
    o += [lip_f, lip_t]

    # ---- menisci: a healthy wedge at the rim; the worn one thinner, torn and pushed out past the plateau edge,
    # where it rests on the tibial spur and presses into the lining
    o.append(_meniscus(surf_fl, surf_tl, CX - 118.5, CX - 80, 15, False))
    o.append(_meniscus(surf_fr, surf_tr, MEN_W[0], MEN_W[1], 6.6, True, rim_y=tip_t[1] - 1.6))

    # ---- lining: thin and calm on the healthy side; thick, red and folded where it is inflamed.  Drawn after the
    # menisci, so each lining's inner edge overlaps its meniscus rim and the two read as joined.
    o.append(_syn_band(SYN_L, False, rnd))
    o.append(_syn_band(SYN_R, True, rnd, skip=VILLI_SKIP))
    # loose bits of worn cartilage floating in the extra fluid
    for x, y, a in FLAKES:
        o.append(_flake(CX + x, y, a))
    return "".join(o), dict(surf_fl=surf_fl, surf_tl=surf_tl, surf_fr=surf_fr, surf_tr=surf_tr,
                            fem_l=fem_l, fem_r=fem_r, tib_l=tib_l, tib_r=tib_r, th_fl=th_fl, th_fr=th_fr,
                            tip_f=tip_f, tip_t=tip_t, bf=bf)


FLAKES = [(124, 203, 20), (127, 214, -30), (131, 194, 55)]   # (u, y, angle): in the swollen pocket, clear of the lining


def _flake(x, y, a, s=1.0):
    return (f'<path transform="translate({_f(x)},{_f(y)}) rotate({a}) scale({s})" d="M-3,-1.5 L1.1,-2.3 L3.2,0.2 L1.3,2.1 '
            f'L-2.5,1.5 Z" fill="{CART_HI}" stroke="{CART_EDGE}" stroke-width=".8" stroke-linejoin="round"/>')


# ============================================================== magnified cartilage
def _cell(x, y, rx=3.7, ry=3.7, rot=0, lac=1.6, empty=False):
    edge, w = ("#A08ED2", ".9") if empty else (LACUNA_EDGE, ".7")   # an empty space gets a firmer rim so it reads
    g = (f'<g transform="translate({_f(x)},{_f(y)}) rotate({_f(rot)})">'
         f'<ellipse rx="{_f(rx + lac)}" ry="{_f(ry + lac)}" fill="{LACUNA}" stroke="{edge}" stroke-width="{w}"/>')
    if not empty:
        g += (f'<ellipse rx="{_f(rx)}" ry="{_f(ry)}" fill="{CELL}"/>'
              f'<circle r="{_f(min(rx, ry) * 0.42)}" fill="{CELL_NUC}"/>')
    return g + "</g>"


CLUSTER_CELLS = [(-4.6, -2.4), (4.4, -2.6), (-4.4, 3.2), (4.6, 3.0), (0, -6.4), (0.2, 6.6)]


def _cluster_box(n):
    """Centre offset and radii of the shared space around a clump of n cells (cell r 3.2, 1.8 margin)."""
    xs, ys = [c[0] for c in CLUSTER_CELLS[:n]], [c[1] for c in CLUSTER_CELLS[:n]]
    return ((min(xs) + max(xs)) / 2, (min(ys) + max(ys)) / 2,
            (max(xs) - min(xs)) / 2 + 5.0, (max(ys) - min(ys)) / 2 + 5.0)


def _cluster(x, y, n, rot=0):
    """A clump of cartilage cells sharing one enlarged space (seen in worn cartilage)."""
    ox, oy, rx, ry = _cluster_box(n)
    g = [f'<g transform="translate({_f(x)},{_f(y)}) rotate({_f(rot)})">',
         f'<ellipse cx="{_f(ox)}" cy="{_f(oy)}" rx="{_f(rx)}" ry="{_f(ry)}" fill="{LACUNA}" stroke="{LACUNA_EDGE}" '
         'stroke-width=".7"/>']
    for cx, cy in CLUSTER_CELLS[:n]:
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


# worn close-up (offsets from the circle centre; surface at -10, tidemark at +20, cracks at x -36, -8, 24, 44):
# every clump, lost cell and deep cell sits between the cracks and clear of its neighbours
WORN_CLUSTERS = [(-51, 3.6, 4), (-22, 3.0, 3), (8, 4.2, 5), (57, 5.5, 3)]   # (dx, dy, cells)
WORN_LOST = [(35, 0.5, 3.4), (42, 12.4, 2.6)]                             # (dx, dy, radius)
WORN_DEEP = [(31, 12.4)]
WORN_CRACKS = [(-36, 22, 5.5), (-8, 30, 6.5), (24, 25, 5.0), (44, 12, 3.6)]   # (dx, depth, half width)


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
    cracks = WORN_CRACKS if worn else []
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
        surf = [(xx + rnd.uniform(-1.2, 1.2), S + 7.5 + 0.0016 * (xx - cx) ** 2)   # surface zone: flat cells
                for xx in range(int(x0) + 6, int(x1), 15)]
        deep = [(xx + rnd.uniform(-1.2, 1.2), TM - 15 + j * 6.4)              # deep zone: little stacks (columns)
                for xx in range(int(x0) + 9, int(x1), 17) for j in range(3)]
        mid = []   # middle zone: round cells scattered between, each kept clear of the surface row and every column
        for _ in range(8000):
            if len(mid) >= 12:
                break
            x_ = rnd.uniform(x0 + 4, x1 - 4)
            y_ = rnd.uniform(S + 17, TM - 24) + 0.0016 * (x_ - cx) ** 2
            if (any(math.hypot(x_ - a, y_ - b) < 15.5 for a, b in mid)
                    or any(abs(x_ - a) < 12.4 and abs(y_ - b) < 9.2 for a, b in surf)
                    or any(math.hypot(x_ - a, y_ - b) < 5.1 + 4.2 + 1.2 for a, b in deep)):
                continue
            mid.append((x_, y_))
        cells += [_cell(a, b, 4.6, 1.8, rnd.uniform(-5, 5), 1.2) for a, b in surf]
        cells += [_cell(a, b, 3.5, 3.3, rnd.uniform(0, 180), 1.6) for a, b in mid]
        cells += [_cell(a, b, 3.0, 2.0, 0, 1.0) for a, b in deep]
    else:   # clumps between the cracks, a few lost cells (empty spaces), a thinned deep row
        for dx, dy, n in WORN_CLUSTERS:
            cells.append(_cluster(cx + dx, cy + dy, n, rnd.uniform(-6, 6)))
        for dx, dy, rr in WORN_LOST:
            cells.append(_cell(cx + dx, cy + dy, rr, rr * 0.92, 0, 1.4 if rr > 3 else 1.0, empty=True))
        for dx, dy in WORN_DEEP:
            cells.append(_cell(cx + dx, cy + dy, 2.6, 2.2, 0, 1.0))
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


def _connector(ring, ring_r, circle, lift, c2, col):
    """A faint dashed callout line, white halo under it, from the top of a dashed ring up and over to its
    magnified circle: it leaves the ring straight up for `lift` units, then bends through c2 and meets the
    circle head-on at its outer white rim."""
    (x0, y0), (cx, cy) = ring, circle
    p0 = (x0, y0 - ring_r - 2.2)
    c1 = (x0, p0[1] - lift)
    ux, uy = c2[0] - cx, c2[1] - cy
    m = math.hypot(ux, uy)
    p3 = (cx + ux / m * (INS_R + 3.6), cy + uy / m * (INS_R + 3.6))
    d = (f"M{_f(p0[0])},{_f(p0[1])} C{_f(c1[0])},{_f(c1[1])} {_f(c2[0])},{_f(c2[1])} "
         f"{_f(p3[0])},{_f(p3[1])}")
    return (f'<path d="{d}" fill="none" stroke="#FFFFFF" stroke-width="3.8" stroke-linecap="round" opacity=".92"/>'
            f'<path d="{d}" fill="none" stroke="{col}" stroke-width="1.35" stroke-dasharray="3.4 2.6" '
            'stroke-linecap="round" opacity=".9"/>')


# ============================================================== labels
def _leader(x0, y0, x1, y1, dot=True):
    d = f"M{_f(x0)},{_f(y0)} L{_f(x1)},{_f(y1)}"
    return (f'<path d="{d}" stroke="#FFFFFF" stroke-width="3.4" stroke-linecap="round"/>'
            f'<path d="{d}" stroke="#46535D" stroke-width="1.2" stroke-linecap="round"/>'
            + (f'<circle cx="{_f(x1)}" cy="{_f(y1)}" r="2.6" fill="#46535D" stroke="#FFFFFF" stroke-width="1.2"/>'
               if dot else ""))


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


def sw_lining():   # every swatch spans x -12..12, so the gap to its label is the same in every column
    return (f'<path d="M-9,0 H9" stroke="{LINING_EDGE}" stroke-width="6" stroke-linecap="round"/>'
            f'<path d="M-9,0 H9" stroke="{LINING}" stroke-width="4.2" stroke-linecap="round"/>')


def sw_infl():
    return (f'<path d="M-7.5,-1.6 H7.5" stroke="{INFL_EDGE}" stroke-width="9" stroke-linecap="round"/>'
            f'<path d="M-7.5,-1.6 H7.5" stroke="{INFL}" stroke-width="7" stroke-linecap="round"/>'
            + "".join(f'<circle cx="{x}" cy="4.2" r="2.6" fill="{INFL}" stroke="{INFL_EDGE}" stroke-width=".8"/>' for x in (-6, 0, 6)))


def sw_spur():   # the same lip as on the knee: extra bone growing out of a bone edge, greying toward its tip
    return ('<rect x="-12" y="-8" width="8.2" height="16" rx="2" fill="url(#jp-cortex)"/>'
            '<path d="M-5,-6.6 C1,-6.1 7.6,-2.4 11.4,5 C6.4,4.3 1,4.9 -5,6.6 Z" fill="url(#jp-spur)"/>'
            f'<path d="M-5,-8 V-6.6 C1,-6.1 7.6,-2.4 11.4,5 C6.4,4.3 1,4.9 -5,6.6 V8" fill="none" stroke="{BONE_EDGE}" '
            'stroke-width="1.1" stroke-linejoin="round" stroke-linecap="round"/>')


def sw_space():
    return _bracket(0, -7, 7, w=4)


def sw_ring():   # the dashed rings: green on the healthy side, red on the worn side
    return (f'<path d="M0,-7 A7,7 0 0 0 0,7" fill="none" stroke="{GREEN_DK}" stroke-width="1.8" stroke-dasharray="2.8 1.9"/>'
            f'<path d="M0,-7 A7,7 0 0 1 0,7" fill="none" stroke="{RED_DK}" stroke-width="1.8" stroke-dasharray="2.8 1.9"/>')


def sw_cell():
    return _cell(0, 0, 4.4, 3.8, 0, 1.9)


def sw_lost():
    return _cell(0, 0, 4.4, 3.8, 0, 1.9, empty=True)


def sw_fiber():
    return (f'<path d="M-12,6 V0 Q-12,-6 -6,-6 Q0,-6 0,0 V6 M0,6 V0 Q0,-6 6,-6 Q12,-6 12,0 V6" fill="none" '
            f'stroke="{FIBER}" stroke-width="1.5"/>')


def sw_base():   # the hard (calcified) base layer under cartilage, topped by the wavy tidemark, on bone
    wav = [(x, -3.2 + 1.2 * math.sin(x / 2.4)) for x in range(-12, 13, 1)]
    return (f'<path d="{_poly(wav + [(12, 3.6), (-12, 3.6)])}" fill="#C3D8EA"/>'
            f'<path d="{_line(wav)}" fill="none" stroke="#5B84B0" stroke-width="1.2"/>'
            '<rect x="-12" y="3.6" width="24" height="3.6" fill="url(#jp-bonei)"/>'
            f'<path d="M-12,3.6 H12" stroke="{BONE_EDGE}" stroke-width="1" opacity=".7"/>')


def sw_flake():
    return _flake(0, 0, 15, 1.7)


KEY_ROWS = [   # every colour and symbol on the knee and in both close-up circles
    [(sw_bone, "Bone"), (sw_cart, "Cartilage"), (sw_men, "Meniscus (cushion)"), (sw_lig, "Ligament"),
     (sw_fluid, "Joint fluid")],
    [(sw_lining, "Calm lining"), (sw_infl, "Inflamed lining"), (sw_spur, "Bone spur"), (sw_space, "Joint space"),
     (sw_ring, "Shown up close")],
    [(sw_cell, "Cartilage cell"), (sw_lost, "Lost cell"), (sw_fiber, "Collagen fibers"), (sw_base, "Hard base layer"),
     (sw_flake, "Loose flake")],
]


def _key(y):
    """Three-row KEY; column widths follow the longest label in each column."""
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
        cy = y + 13 + r * 21
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
            # bone spur: bone that greys toward its tip, so it reads as bone and still matches the grey KEY swatch
            f'<linearGradient id="jp-spur" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="{SPUR_BASE}"/>'
            f'<stop offset=".45" stop-color="{SPUR_HI}"/><stop offset="1" stop-color="{SPUR}"/></linearGradient>',
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

    # bone names, in clear space on the shafts (solid white boxes, so the dashed split line does not ghost through)
    for y, lines in ((68, ["Thigh bone", "(femur)"]), (314, ["Shin bone", "(tibia)"])):
        o.append(label_bg(CX - 36, y - 12, 72, 30, "#FFFFFF", 1, 6))
        o.append(T(CX, y, lines[0], 10.5, 700, INK, "middle"))
        o.append(T(CX, y + 13, lines[1], 10, 500, INK2, "middle", italic=True))
    o.append(T(CX - 154, 322, "Calf bone", 10.5, 700, INK, "end"))
    o.append(T(CX - 154, 335, "(fibula)", 10, 500, INK2, "end", italic=True))

    # magnified circles, and the dashed rings on the knee that mark the spot each one shows, each tied to its
    # circle by a dashed connector that rises from the ring and bends over to the circle through clear space (the
    # worn one passes between markers 1 and 2 and above the swollen lining)
    def _tib_mid(bone, top, u):   # halfway between the tibial bone surface and the cartilage's top at u
        x = CX + u
        return tf(x, (_y_at(bone, x, min) + _y_at(top, x, min)) / 2)
    lx, ly = _tib_mid(g["tib_l"], g["surf_tl"], LENS_U[0])
    rx, ry = _tib_mid(g["tib_r"], g["surf_tr"], LENS_U[1])
    o.append(inset(INS_L, False))
    o.append(inset(INS_W, True))
    o.append(_connector((lx, ly), LENS_R, INS_L, 66, (lx - 32, 104), GREEN_DK))
    o.append(_connector((rx, ry), LENS_R, INS_W, 80, (rx + 30, 100), RED_DK))   # stays left of the lining's top end
    o.append(_lens(lx, ly, GREEN_DK, LENS_R))
    o.append(_lens(rx, ry, RED_DK, LENS_R))

    # joint space, bone end to bone end, at the same spot on both sides: full height when healthy, squeezed
    # where the worn cartilage has gone
    sp = {}
    for side, fem, tib in (("h", g["fem_l"], g["tib_l"]), ("w", g["fem_r"], g["tib_r"])):
        u = CX + (-SPACE_U if side == "h" else SPACE_U)
        (bx, by0), (_, by1) = tf(u, _y_at(fem, u, max)), tf(u, _y_at(tib, u, min))
        sp[side] = (bx, by0, by1)
        o.append(_bracket(bx, by0, by1))
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

    # worn side: numbered markers, each with a short leader to the tissue it names, explained in a list on the
    # right.  1: the mouth of the deep crack beside the red ring; 2: the tip of the femoral spur; 3: sits on the
    # swollen lining itself; 4: the squeezed joint space at the bald patch.
    fr, sfr = g["fem_r"], g["surf_fr"]
    ss = _arclen(fr)
    ic = min(range(len(ss)), key=lambda i: abs(ss[i] - (g["bf"][0] - 0.05)))
    mouth = ((sfr[ic - 4][0] + sfr[ic + 4][0]) / 2, (sfr[ic - 4][1] + sfr[ic + 4][1]) / 2)
    bx, by0, by1 = sp["w"]
    marks = [(tf(CX + 60, 195), tf(*mouth), True), (tf(CX + 99, 185), tf(*g["tip_f"]), True),
             (tf(CX + 138.5, 212), None, False), (tf(CX + SPACE_U, 248), (bx, by1 + 1.2), False)]
    for (mx, my), tgt_, dot in marks:
        if tgt_:
            o.append(_leader(mx, my, tgt_[0], tgt_[1], dot))
    for i, ((mx, my), _, _) in enumerate(marks):
        o.append(_marker(mx, my, i + 1))
    xl = 566
    for i, (title, sub) in enumerate(WORN_NOTES):
        y = 212 + i * 33
        o.append(_badge(xl + 8.6, y - 4, i + 1, RED))
        o.append(T(xl + 23, y, title, 11.5, 800, INK))
        o.append(T(xl + 23, y + 13, sub, 10, 500, INK2, italic=True))

    o.append(_key(KEY_Y))
    # everything sits TOP units down, so the heading pills keep a margin from the top edge of the picture
    return svg(W, H + TOP, f'<g transform="translate(0,{TOP})">{"".join(o)}</g>',
               "A knee joint seen from the front and split down the middle. Left, healthy: smooth cartilage, a full "
               "joint space, a thin lining and a little joint fluid, with a magnified circle of orderly cartilage cells. "
               "Right, osteoarthritis: thin and cracked cartilage, bone spurs growing at the joint edges, a squeezed "
               "joint space, a swollen red lining with extra fluid and loose flakes, a torn meniscus pushed out past the "
               "edge, and a magnified circle of cracked cartilage with clumped and lost cells.")


# ============================================================== front page blocks
FEEL = [  # [NICE22] activity-related pain, short morning stiffness; [HUNTER19] crepitus, bony enlargement,
    # restricted motion, mild swelling, instability.  [KHAN04] hip OA pain sits mostly in the groin and buttock.
    # The 30-minute number lives once, in ALERT, where it is the threshold to act on.
    "Pain with use (stairs, kneeling, opening jars) that eases with rest",
    "Brief stiffness on waking or after sitting still",
    "Creaking, grinding or clicking as it bends",
    "Some swelling, or a joint that feels unsteady",
    "Hard knobs on the finger joints",
    "A sore hip often aches in the groin or buttock",
]
ALERT = [  # [NICE22] QS87 atypical features: hot swollen joint, prolonged stiffness, trauma, rapid worsening, deformity.
    # "suddenly" and "fast" keep these apart from the slow, typical signs in FEEL (unsteady joint, finger knobs)
    "A <b>hot, red, very swollen</b> joint, above all with a fever: <b>get care the same day</b>",
    # several joints swollen at once points to inflammatory arthritis, not OA; ordinary hand OA can make many
    # finger joints sore, so the line is about swelling, not soreness
    "Morning stiffness <b>over 30 minutes</b>, or several swollen joints at once",
    "It began with a <b>fall or injury</b>, or is worsening fast",
    "It <b>suddenly locks or gives way</b>, or <b>changes shape fast</b>",
]

IC_WOMAN = '<circle cx="32" cy="23" r="13"/><path d="M32 36v21M23 48h18"/>'
# a person squatting to lift a heavy box
IC_LIFT = ('<circle cx="20" cy="10" r="5.2"/><path d="M21.4 16.6 27.6 35"/><path d="M27.6 35 40.6 40 36.8 55.2H44"/>'
           '<path d="M23.4 21.6 42 27"/><rect x="41.4" y="18.5" width="17" height="16" rx="2.2"/><path d="M46.4 23h7"/>')
# a standing leg (side view: thigh, kneecap, calf, foot) with an arrow pointing down at the thigh muscle
IC_THIGH = ('<path d="M24 4.5C30.4 9 33.8 15.4 33.2 22.4 32.8 26.6 31 29 31.6 31.6 33.6 33.6 33.2 36.6 31.2 38.6L30.4 52.6'
            'C33.4 53.6 38.4 54.2 43 55.6 45.2 56.3 45 59 42.8 59H23.6C21.8 59 21.4 57 22 55 23 51 22.8 47.2 21.6 44.2'
            'C19.4 38.6 19.6 35 20.6 32 21.6 28.6 19.2 20 16.6 13.2L15.4 4.5"/><path d="M46 6.5v13M41 14.5l5 5 5-5"/>')
# an injured joint: the knee's two bone ends (thigh bone with its knobs, shin bone with its flat top) with a
# band-aid stuck across the joint; the band-aid is filled with the disc colour so it covers the bone lines under it
IC_INJURY = ('<path d="M24 3V13C24 18 15 18.5 15 25.5C15 30 19 32.5 23.5 31.5C27 30.7 29 29 32 29C35 29 37 30.7 40.5 31.5'
             'C45 32.5 49 30 49 25.5C49 18.5 40 18 40 13V3"/>'
             '<path d="M24 61V49C24 44.5 15 44 15 39.5C15 37 22 36 32 36C42 36 49 37 49 39.5C49 44 40 44.5 40 49V61"/>'
             '<g transform="rotate(-32 32 33)"><rect x="10" y="26.5" width="44" height="13" rx="6.5" '
             'style="fill:var(--soft)"/><rect x="25.5" y="29.5" width="13" height="7" rx="1.6"/></g>')
RISKS = [  # (icon, label, custom)
    ("age", "Getting older", None),                           # [WHO23] about 73% are older than 55
    ("scale", "Extra body<br>weight", None),                  # [SILVER15] overweight OR 1.98, obesity 2.66
    ("jp_injury", "An old joint<br>injury", IC_INJURY),       # [SILVER15] previous knee injury OR 2.83
    ("woman", "Being<br>a woman", IC_WOMAN),                  # [SILVER15] OR 1.68; [WHO23] 60% female
    ("dna", "Family<br>history", None),                       # [HUNTER19] genetics
    ("lift", "Heavy lifting or<br>kneeling work", IC_LIFT),   # [WANG20] OR 1.52
    ("thigh", "Weak thigh<br>muscles", IC_THIGH),             # [OIESTAD15] OR 1.65
]

# back page: a balance pose for "Tai chi or yoga" (the kit has no such figure; a namespaced key cannot collide)
ICONS.setdefault("jp_taichi", '<circle cx="32" cy="9" r="5"/><path d="M32 15.5V38"/><path d="M32 22 19.5 12.5M32 22l12.5-9.5"/>'
                               '<path d="M32 38v19.5"/><path d="M32 38l11 6.6-9.6 5.4"/><path d="M24 58h16"/>')
# and a heat pack with warmth rising off it for "Heat and support" (the kit's thermometer reads as fever)
ICONS.setdefault("jp_heatpack", '<rect x="8" y="32" width="48" height="23" rx="7"/><path d="M24 32v23M40 32v23"/>'
                                 '<path d="M20 25.5c-3.6-3.6 3.6-7 0-11.8M32 25.5c-3.6-3.6 3.6-7 0-11.8M44 25.5c-3.6-3.6 3.6-7 0-11.8"/>')

ARROW = ('<svg class="jpn-arr" viewBox="0 0 24 12" role="img" aria-label="becomes"><path d="M1.5 6H20.5M14.6 1.6 '
         '20.8 6l-6.2 4.4" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" '
         'stroke-linejoin="round"/></svg>')

# where OA strikes: a standing figure seen from the front, one arm held out from the body, with a faint dashed spine
# and red dots on the joints OA hits most.  [WHO23] knee, then hip and hand; [GBD21] knee the most common site;
# [KALICH08] spine facet-joint OA in about 60% of adults (CT, Framingham); [RODDY15] symptomatic big-toe (1st MTP) OA
# in 7.8% of adults 50+, the most common foot site.  Drawn 0.76in tall (84 units), so 1 unit = 0.23 mm: every pair of
# dots is at least 8.9 units (2.0 mm) apart, centre to centre.
WHERE_DOTS = [(19, 14.8), (19, 35.2), (38.6, 38.8), (24.6, 42.2), (14.55, 59.4), (22.3, 78.4)]   # neck, low back,
# the held-out hand, hip, knee, big toe (the inner front of the foot).  Proportions follow a standing adult: shoulders
# about 82%, waist 60%, hip joint 52%, crotch 47% and knee 28% of the height up from the soles.
WHERE_BODY = [   # (x, y, tension): down the figure's right side (viewer's left), across both feet, up the other side
    (17.4, 12.4, 0), (17.4, 15.2, .5), (13.2, 16.7), (10.0, 18.2), (8.4, 20.9), (7.6, 27), (7.1, 35), (6.7, 43.4),
    (6.6, 46.6), (8.3, 48.7), (9.9, 47.2), (10.1, 43.7), (10.6, 34.5), (11.4, 25.4, 0), (12.4, 29.8), (12.9, 34),
    (11.9, 38.4), (11.6, 42), (12.2, 50), (12.7, 59.4), (12.9, 66), (13.4, 73.6), (11.8, 77.6), (11.9, 79.8, .4),
    (17.0, 79.8, .4), (16.9, 76.4), (16.5, 73.4), (16.6, 66), (16.4, 59.4), (17.6, 50.4), (19, 45, .3), (20.4, 50.4),
    (21.6, 59.4), (21.4, 66), (21.5, 73.4), (21.1, 76.4), (21.0, 79.8, .4), (26.1, 79.8, .4), (26.2, 77.6), (24.6, 73.6),
    (25.1, 66), (25.3, 59.4), (25.8, 50), (26.4, 42), (26.1, 38.4), (25.1, 34), (25.6, 29.8), (26.6, 25.4, 0),
    (32.2, 30.6), (36.0, 36.6), (36.6, 39.6), (38.6, 41.5), (40.7, 40.0), (40.7, 37.0), (38.6, 34.8), (33.6, 26.0),
    (30.0, 19.7), (28.0, 18.2), (24.8, 16.7), (20.6, 15.2, .5), (20.6, 12.4, 0)]


def _where_fig():
    dots = "".join(f'<circle cx="{x}" cy="{y}" r="2.6" fill="{RED}" stroke="#FFFFFF" stroke-width="1.1"/>' for x, y in WHERE_DOTS)
    return ('<svg class="jpn-fig" viewBox="4.5 0 39 84" role="img" aria-label="A standing figure seen from the front, '
            'one arm held out, with red dots on the neck, low back, hand, hip, knee and big toe">'
            f'<path d="{path_d(WHERE_BODY)}" fill="#B7CFE3" stroke="#577FA2" stroke-width="1" stroke-linejoin="round"/>'
            '<circle cx="19" cy="7.6" r="5.4" fill="#B7CFE3" stroke="#577FA2" stroke-width="1"/>'
            '<path d="M19 16.6V43" stroke="#577FA2" stroke-width="1" stroke-dasharray="1.3 1.1" opacity=".55"/>'
            f'{dots}</svg>')


def _ic(body, size, sw=2.8):
    return (f'<svg class="ic" viewBox="0 0 64 64" style="width:{size};height:{size}" fill="none" stroke="currentColor" '
            f'stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{body}</svg>')


def _scale_0_10():
    """A 0 to 10 pain scale, green to red, for the patient to circle.  Every numeral reaches 4.5:1 (WCAG AA for
    small text; measured with kit._lum): white on the dark ends, 0 and 1 at 5.1 and 4.7:1, 8 to 10 at 4.8, 4.9 and
    6.4:1; ink on the light middle cells 2 to 7 at 4.7, 5.7, 6.4, 6.3, 5.3 and 4.6:1.  Cells 0, 1, 7 and 8 were
    darkened or lightened just enough to pass (they measured 4.3, 3.5, 4.25 and 4.0:1), keeping the ramp."""
    cols = ["#2A7D50", "#3A8237", "#74A73A", "#9CB232", "#C2B52C", "#E0A82A", "#E58E2A", "#E37A38", "#C8482A",
            "#CC3D2F", "#B32A2A"]
    cells = "".join(f'<span style="background:{c};color:{INK if 2 <= i <= 7 else "#FFFFFF"}">{i}</span>'
                    for i, c in enumerate(cols))
    return f'<div class="jpn-pain">{cells}</div><div class="jpn-pl"><span>No pain</span><span>Worst</span></div>'


def front(t, ed):
    feel = "".join(f"<li>{x}</li>" for x in FEEL)
    alert = "".join(f"<li>{x}</li>" for x in ALERT)
    risk = "".join(f'<div class="jpn-rf"><span class="jpn-disc">'
                   f'{_ic(custom, "0.3in") if custom else icon(ic, "0.3in", sw=2.8)}</span><span class="jpn-rl">{lab}</span></div>'
                   for ic, lab, custom in RISKS)
    nums = (
        # [MESSIER05] each pound lost = about a 4-fold drop in knee load per step
        f'<div class="jpn-n"><b class="jpn-big">1 lb {ARROW} 4 lb</b><span>Each pound you lose takes about '
        '<b>4 pounds</b> of load off your knee with every step.</span></div>'
        f'<div class="jpn-n jpn-where">{_where_fig()}<div><b>Where OA strikes</b><span><b>Red dots:</b> knees, hips '
        'and hands most; also the spine and big toe.</span></div></div>'
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
            f'<div class="jpn-sh jpn-sh2">Good to know</div><div class="jpn-nums">{nums}</div>'
            '</div>')


CSS = r"""
.jpn .jpn-art{margin-top:0.02in}
.jpn .jpn-sh{font:800 7.6pt Inter,sans-serif;letter-spacing:.14em;text-transform:uppercase;color:var(--c1);margin:0 0 3px}
.jpn .jpn-sh2{margin-top:0.1in}
.jpn .jpn-row{display:grid;grid-template-columns:1fr 3.3in;gap:0.18in;margin-top:0.09in;align-items:start}
.jpn .jpn-dots{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:1fr;gap:1px 0}
.jpn .jpn-dots li{position:relative;padding-left:12px;font-size:8.2pt;line-height:1.27;color:#2B3236}
.jpn .jpn-dots li::before{content:"";position:absolute;left:0;top:4px;width:6px;height:6px;border-radius:50%;background:var(--c2)}
.jpn .jpn-alert{border:1.5px solid #C0392B;background:#FDF1EF;border-radius:8px;padding:3px 10px 3px}
.jpn .jpn-ah{font:800 7.6pt Inter,sans-serif;letter-spacing:.14em;text-transform:uppercase;color:#A5281E;margin:0 0 2px}
.jpn .jpn-alert ul{margin:0;padding:0 0 0 12px}
.jpn .jpn-alert li{font-size:8pt;line-height:1.23;color:#2B3236;margin:0 0 1px}
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
.jpn .jpn-arr{display:inline-block;width:0.8em;height:0.4em;margin:0 0.08em;vertical-align:0.2em;color:var(--c2)}
.jpn .jpn-where{flex-direction:row;align-items:center;gap:6px}
.jpn .jpn-where>div{display:flex;flex-direction:column;gap:1px}
.jpn .jpn-where>div>b{font:800 8.4pt Inter,sans-serif;color:var(--deep)}
.jpn .jpn-fig{flex:none;height:0.76in;width:0.353in}
.jpn .jpn-n.jpn-where{padding:2px 6px 2px;gap:5px}
.jpn .jpn-n span{font-size:7.8pt;line-height:1.26;color:#2B3236}
.jpn .jpn-n span b{color:var(--deep)}
.jpn .jpn-me>b{font:800 8.4pt Inter,sans-serif;color:var(--deep)}
.jpn .jpn-pain{display:grid;grid-template-columns:repeat(11,1fr);gap:2px;margin-top:2px}
.jpn .jpn-pain span{display:flex;align-items:center;justify-content:center;height:0.2in;border-radius:3px;
  font:800 7.6pt Inter,sans-serif}
.jpn .jpn-pl{display:flex;justify-content:space-between;font-size:7pt;color:#5E686F;margin-top:1px}
.jpn .jpn-me>span{font-size:7.4pt;color:#4A555C}
"""

BACK_CSS = r"""
/* ---- this sheet's back page, reached through the empty .jpn-bk marker in the lifestyle title (the back page has
   no sheet class).  Fine print, the START HERE badge and the diamonds all come from the kit; these rules only make
   room for the six-point check list. ---- */
/* all five need bands stay one height (the kit's 0.5in) with column 2's two-line subtitle, so the photos line up */
.sheet.back:has(.jpn-bk) .col .need{padding:0.06in 0.06in 0.048in}
.sheet.back:has(.jpn-bk) .life .disc2{width:0.74in;height:0.74in}
.sheet.back:has(.jpn-bk) .life .disc2 svg{width:0.46in!important;height:0.46in!important}
.sheet.back:has(.jpn-bk) .band{padding-bottom:0.13in}
.sheet.back:has(.jpn-bk) .ns-title{margin-top:0.11in}
/* every product name gets a two-line band (one-line names sit centred in it), so the photos, names, sizes and
   bullet lists line up across all five columns; column 2's "Chondro-Relief Intensive Care" needs both lines */
.sheet.back:has(.jpn-bk) .col .pick .nm{min-height:2.1em;line-height:1.05;display:flex;align-items:center;
  justify-content:center}
/* room for that band and the two-line alpha-gal check: the same small trims other sheets use (measured: 3.4px
   left above the footer in both editions) */
.sheet.back:has(.jpn-bk) .duo{margin-top:0.07in}
.sheet.back:has(.jpn-bk) .notes{margin-top:0.07in}
.sheet.back:has(.jpn-bk) .notes .ln{height:0.22in}
"""

SHEET = {
    "slug": SLUG, "code": "ND-MS-602", "order": 13, "theme": "msk", "series": "Pain and Movement Series",
    "title": "Joint Pain and Osteoarthritis", "sub": "Knees, hips and hands",
    # [HUNTER19] most common arthritis, a whole-joint disease (cartilage, bone, lining); spurs (osteophytes) grow at
    # the joint margins while the bone under the cartilage thickens.
    # [GBD21] 595 million people (7.6% of the world) had OA in 2020, up 132% since 1990, and cases are projected to
    # keep rising to 2050 (knee +75%, hip +79%); [WHO23] knee most common, then hip and hand.
    "intro": ("Osteoarthritis (OA), the most common arthritis, changes the whole joint: the smooth "
              "<b>cartilage</b> on the bone ends thins and cracks, bone <b>spurs</b> grow at the joint's edges, and the "
              "lining can swell. It hits <b>knees, hips and hands</b> most. About <b>595 million people</b> had it in "
              "2020, and the number is rising. Moving more and carrying less weight help most people stay active."),
    "front": front,
    "css": CSS + BACK_CSS,
    "back": {
        "life_title": 'Lifestyle Recommendations<span class="jpn-bk"></span>',
        "style": "circle",
        "life": [
            ("walk", "Move most days", "Moving feeds cartilage: walk, cycle or swim 150&nbsp;minutes a week."),  # [FOX09] [CDC-PA] [ACR19]
            ("dumbbell", "Build strength", "Thigh and hip work 2&nbsp;days a week takes load off the joint."),            # [CDC-PA] [OIESTAD15]
            ("scale", "Lighten the load", "Each pound lost takes about 4&nbsp;pounds off your knees with every step."),   # [MESSIER05]
            ("jp_taichi", "Tai chi or yoga", "Slow, steady moves ease stiffness and build balance."),                       # [ACR19]
            ("fish", "Food for joints", "Mediterranean style: fish, olive oil, beans, nuts, colorful plants."),
            # [ACR19] cane (strong, knee and hip), heat or cold (conditional); "on your good side" = in the hand
            # opposite the sore side, said in plain words so the line stays three lines long
            ("jp_heatpack", "Heat and support", "Heat for stiffness, ice after a flare, a cane on your good side."),
        ],
        # Picks: boswellia and curcumin lead the evidence [ZHANG25] [BIDESHKI24]; omega-3 did not help knee-OA symptoms
        # [MATHIEU22], so the fifth column is Curcumin 400X, not fish oil (topics brief: "Omega Pure ... or Curcumin
        # 400X").  It is framed as the willow-free choice INSTEAD of Inflam-Eze Plus (for an aspirin allergy, see the
        # check list), never on top of it, so the plan does not stack two enhanced-absorption curcumins [TGA23] and
        # its "sched": [] keeps it out of the daily rhythm.  Chondro-Relief's glucosamine 500 mg / chondroitin 400 mg
        # are printed as label facts only, with no dose claim (they are a third of the 1,500 / 1,200 mg comparator in
        # [LUGO16]); its subtitle leads with MSM and green-lipped mussel, one of the two supplements with a clinically
        # important medium-term effect in Liu X et al. Br J Sports Med 2018;52:167-75 (PMID 29018060).
        "cols": [
            {"p": "jp_inflam_eze", "need": "Inflammatory balance", "needsub": "ginger, curcumin, boswellia", "start": True,
             "bullets": ["Supports a healthy inflammatory response", "Supports joint comfort and movement"],
             "dose": "dose_from_db"},
            {"p": "jp_chondro_ic", "need": "Building blocks", "needsub": "glucosamine, MSM, green‑lipped mussel",
             # both bullets start with an S/F verb, so build.py ties each to the FDA line with the diamond.  The first
             # runs to 3 lines on purpose: with the two-line name band (BACK_CSS) this column's 3 + 1 bullet lines
             # match the 2 + 2 of the others, so the bullets AND the IN EACH SERVING rows line up in all five
             "bullets": ["Provides raw materials for cartilage and joint fluid", "Supports joint tissues"],
             "dose": "dose_from_db"},
            # label: "Undenatured Collagen Blend (UC-II) 20 mg" per capsule, 1 capsule twice daily = 40 mg of the
            # blend a day.  [LUGO16] used 40 mg of UC-II itself; the label does not say the blend is all UC-II, so the
            # bullet says "blend" and makes no trial-dose claim.
            {"p": "jp_joint_eze", "need": "Joint comfort", "needsub": "UC-II undenatured collagen",
             "bullets": ["UC‑II blend, 40&nbsp;mg a day in 2&nbsp;capsules", "Supports joint comfort and flexibility"],
             "dose": "dose_from_db"},
            {"p": "jp_collagen_renew", "need": "Collagen support", "needsub": "collagen peptides",
             "bullets": ["Supports cartilage, tendons and ligaments", "Pair it with a vitamin C food, like an orange"],
             "dose": "dose_from_db"},
            # label: "Take two softgels daily" (products DB R268); the single active is BioCurc turmeric extract
            {"p": "jp_curcumin_400x", "need": "Willow-free option", "needsub": "curcumin on its own",
             "bullets": ["A curcumin pick without willow bark", "Supports a healthy inflammatory response"],
             "dose": "2 softgels daily", "dosesub": "instead of Inflam-Eze Plus", "sched": []},
        ],
        # One list for both editions; {who} reads "your provider" / "your pharmacist".  Every product is named in full
        # ("Chondro-Relief Intensive Care": NutriDyn also sells Chondro-Relief R150C and Chondro-Relief Plus R155).
        # A no-break hyphen (U+2011) and &nbsp; keep each product name on one line.
        # 1 [KNUDSEN08] glucosamine raises the INR on warfarin; willow [EMA-SALIX], devil's claw [COMM-E], ginger and
        #   curcumin carry bleeding / anticoagulant cautions; [ASA-HERB] pause herbs before surgery (bleeding).
        #   2 [EMA-SALIX] willow bark: not with salicylate allergy; not with aspirin or other NSAIDs without advice;
        #   Curcumin 400X has no willow (column 5).  3 [EMA-CURCUMA] turmeric: not with liver disease, gallstones or
        #   blocked bile ducts; [COMM-E] devil's claw: not with stomach or duodenal ulcers; [TGA23] rare liver injury,
        #   higher risk with enhanced-absorption curcumin, stop and see a doctor if the skin or eyes turn yellow or the
        #   urine dark; [MN-UL] Chondro-Relief Intensive Care's manganese clears through the liver.  4 green-lipped
        #   mussel is a shellfish (label).  5 [CDC-AGS] Collagen Renew is bovine collagen peptides (label): skip it.
        #   Chondro-Relief Intensive Care (chondroitin of unstated source, gelatin capsule and magnesium stearate in
        #   the 2014 panel) and Curcumin 400X (gelatin softgel with glycerin, sell sheet ND466): ask first, since
        #   the source is not stated and tolerance varies.  Inflam-Eze Plus and Joint Eze are plant capsules.  6 labels:
        #   Joint Eze "Do not use if pregnant or nursing"; Inflam-Eze Plus and Collagen Renew "consult your healthcare
        #   practitioner" if pregnant or nursing.  [EMA-SALIX] willow bark is not recommended in pregnancy or while
        #   nursing (salicylate), so the start pick is named with Joint Eze.  Manganese: Clinical Guide ND181 (2022)
        #   confirms it is in the formula but gives no amount; the only amount (2014 catalog) is 15 mg per 4 capsules,
        #   above the 11 mg adult upper limit [MN-UL], and the current catalog could not be opened from this session,
        #   so no number is printed and the multivitamin line asks before stacking more manganese.
        "rx": [
            "<b>On a blood thinner, or surgery coming up?</b> Ask {who} before Inflam‑Eze&nbsp;Plus, Curcumin&nbsp;400X "
            "or Chondro‑Relief Intensive&nbsp;Care: you may need to pause them.",
            "<b>Inflam‑Eze&nbsp;Plus has willow bark, a cousin of aspirin.</b> Aspirin allergy? Skip it; "
            "Curcumin&nbsp;400X is willow-free. On aspirin, ibuprofen or naproxen? Ask {who}.",
            "<b>Liver or gallbladder trouble, or a stomach ulcer?</b> Ask {who} before Inflam‑Eze&nbsp;Plus, "
            "Curcumin&nbsp;400X or Chondro‑Relief Intensive&nbsp;Care. Yellow skin or eyes, or dark urine? Stop them "
            "and call your doctor.",
            "<b>Shellfish allergy?</b> Skip Chondro‑Relief Intensive&nbsp;Care: it has green‑lipped mussel.",
            "<b>Red-meat (alpha-gal) allergy?</b> Skip Collagen&nbsp;Renew (beef). Chondro‑Relief Intensive&nbsp;Care "
            "and Curcumin&nbsp;400X may contain cow or pig gelatin or chondroitin: ask {who}.",
            "<b>Pregnant or nursing?</b> Skip Joint&nbsp;Eze and Inflam‑Eze&nbsp;Plus (willow bark); ask {who} "
            "about the rest. <b>Already take a multivitamin?</b> Chondro‑Relief Intensive&nbsp;Care adds manganese: "
            "ask {who}.",
        ],
    },
}


def _slots_used():
    """Daily-rhythm slots this plan fills: a column's own sched (an empty list keeps it out of the rhythm, as
    build.py reads it), else its product's sched in products.d."""
    import json
    f = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "products.d", f"{SLUG}.json")
    try:
        prods = json.load(open(f))
    except Exception:
        return {"am", "pm", "bed"}
    used = set()
    for c in SHEET["back"]["cols"]:
        sched = c["sched"] if "sched" in c else prods.get(c["p"], {}).get("sched", [("bed",)])
        for slot, *_ in sched:
            used.add(slot)
    return used


if "bed" not in _slots_used():   # no bedtime products: show the two slots in use instead of an empty "nothing" box
    SHEET["css"] += (".sheet.back:has(.jpn-bk) .rhythm{grid-template-columns:1fr 1fr}"
                     ".sheet.back:has(.jpn-bk) .rhythm .slot:nth-child(3){display:none}"
                     # two slots need less width, so the six-point check panel gets more and stays short
                     ".sheet.back:has(.jpn-bk) .duo{grid-template-columns:1fr 1.7fr}")
