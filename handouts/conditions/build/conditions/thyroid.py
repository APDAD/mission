"""Thyroid Health (ND-HM-502), Hormone Health Series.  Slug "thyroid".

Self-contained sheet module (no legacy / sheets.py / art.py drawing code).  Built from scratch
2026-11-03 for Asher's standards (pictures carry the sheet, a KEY for every symbol, nothing
clipped, plain words, structure/function product language, original art and wording).

FRONT, top to bottom
  intro -> "HOW YOUR THYROID WORKS": a front view of the neck (jaw to collarbones) with the
  butterfly-shaped gland on the windpipe below the voice box, beside the control loop: a
  side-view brain inset (hypothalamus sends TRH, pituitary sends TSH) -> thyroid makes T4 ->
  liver, kidneys and muscles turn T4 into active T3 -> every cell -> feedback to the brain.
  Gold gears name the nutrients each step needs (iodine, iron, selenium, zinc).  Numbered
  steps sit in their own strip under the art, then one KEY strip.
  -> "HASHIMOTO'S": magnified thyroid tissue, healthy beside Hashimoto's (immune cells between
  the follicles, TPO antibodies on the thyroid cells), four numbered steps, the usual treatment,
  and a KEY.  -> signs of an underactive thyroid (icons) + who is at higher risk
  -> "Know your numbers" (TSH scale, free T4, TPO antibodies, ferritin, vitamin D) with the
  biotin warning.
BACK: hexagon lifestyle band, five NutriDyn picks (Essential Multi starts), daily rhythm built
around thyroid medicine (nothing in the morning but the probiotic, minerals 4 hours later), and
three Pharmacist / Provider check notes.
Every SVG id and CSS class starts with "thy", so nothing collides in the all-sheets bundle.
Edition wording: "{who}" / "{Who}" become "your provider" or "your pharmacist" (build.ed_text).

SOURCES (tags sit in comments next to each number or claim on the page; PubMed records read
2026-11-03 through the PubMed connector)
  [NIDDK]    NIDDK, "Hypothyroidism (Underactive Thyroid)": Hashimoto's is the most common cause in
             the U.S.; symptom list (fatigue, weight gain, trouble tolerating cold, constipation,
             dry skin, dry thinning hair, heavy or irregular periods, depression, slowed heart
             rate, joint and muscle pain); higher risk: women, age over 60, family history, type 1
             diabetes / celiac / other autoimmune disease, pregnancy or a baby in the past 6
             months, thyroid surgery, radioactive iodine or radiation to the neck or chest.
             (Page could not be re-opened this session: niddk.nih.gov is outside the network
             allow-list.  Wording is from the published page as known; flagged in the report.)
  [ATA]      American Thyroid Association, general information / press room: women are five to
             eight times more likely than men to have thyroid problems.  (Same network caveat.)
  [HOLL02]   Hollowell JG et al. J Clin Endocrinol Metab 2002;87:489-99. PMID 11836274,
             doi:10.1210/jcem.87.2.8182 (NHANES III: hypothyroidism in 4.6% of the U.S. aged 12+,
             0.3% clinical and 4.3% mild; TPO antibodies in 11.3%, more in women and with age;
             many people unknowingly have thyroid disease on labs)
  [SURKS04]  Surks MI et al. JAMA 2004;291:228-38. PMID 14722150, doi:10.1001/jama.291.2.228
             (TSH reference range 0.45 to 4.5 mIU/L; mild disease 4.5-10 or 0.1-0.45)
  [HUW24]    Huwiler VV et al. Thyroid 2024;34:295-313. PMID 38243784, doi:10.1089/thy.2023.0556
             (Hashimoto's is the most common cause of hypothyroidism in iodine-sufficient areas;
             selenium lowered TSH without thyroid hormone, lowered TPO antibodies; safe;
             moderate certainty)
  [ZHANG25]  Zhang H et al. Medicine 2025;104:e44043. PMID 40898469, doi:10.1097/MD.0000000000044043
             (21 RCTs, 1,610 people: selenium lowered TPOAb at 3 and 6 months; selenomethionine
             best form)
  [HU17]     Hu S, Rayman MP. Thyroid 2017;27:597-610. PMID 28290237, doi:10.1089/thy.2016.0635
             (high iodine intake and low selenium and iron are implicated in Hashimoto's, with a
             possible role for vitamin D; TPO is a heme, iron-containing enzyme; Hashimoto's
             patients are often iron deficient; check iron and vitamin D and correct deficiency;
             selenium 50-100 mcg/day may be appropriate where intake is low)
  [KNEZ20]   Knezevic J et al. Nutrients 2020;12:1769. PMID 32545596, doi:10.3390/nu12061769
             ("Iodine, iron, and copper are crucial for thyroid hormone synthesis, selenium and
             zinc are needed for converting T4 to T3, and vitamin D assists in regulating the
             immune response"; gut microbes and the thyroid; probiotics reviewed)
  [MAIA05]   Maia AL et al. J Clin Invest 2005;115:2524-33. PMID 16127464, doi:10.1172/JCI25083
             (most T3 is made outside the thyroid, by deiodinases in skeletal muscle and liver)
  [BIAN06]   Bianco AC, Kim BW. J Clin Invest 2006;116:2571-9. PMID 17016550,
             doi:10.1172/JCI29812 (deiodinases activate T4 to T3 in tissues)
  [CATU14]   Caturegli P et al. Autoimmun Rev 2014;13:391-7. PMID 24434360,
             doi:10.1016/j.autrev.2014.01.007 (lymphocytes infiltrate between the follicles;
             thyroid cells atrophy; diagnosis by TPO / Tg antibodies; most forms end in
             hypothyroidism; treatment is synthetic thyroid hormone)
  [ATA14]    Jonklaas J et al. Thyroid 2014;24:1670-751. PMID 25266247, doi:10.1089/thy.2014.0028
             (levothyroxine is the standard of care; take it consistently, 60 minutes before
             breakfast or at bedtime; separate from calcium and iron)
  [LT4-PI]   FDA-approved levothyroxine labeling: take on an empty stomach, one-half to one hour
             before breakfast; take at least 4 hours before or after drugs that bind it (calcium,
             iron, antacids and others).
  [LI17]     Li D et al. JAMA 2017;318:1150-60. PMID 28973622, doi:10.1001/jama.2017.13705
             (10 mg/day biotin made thyroid immunoassays read falsely high or falsely low).  The
             2 to 3 day stop window follows FDA (biotin safety communication 2017, updated 2019)
             and ATA patient advice; it could not be re-checked live this session.
  [KANG13]   Kang GY et al. Thyroid 2013;23:1233-7. PMID 23758055, doi:10.1089/thy.2013.0101
             (9 of 10 "thyroid support" supplements contained T3, 5 of 10 contained T4, some at
             treatment doses)
  [TENG06]   Teng W et al. N Engl J Med 2006;354:2783-93. PMID 16807415, doi:10.1056/NEJMoa054022
             (more than adequate or excessive iodine intake led to more hypothyroidism and
             autoimmune thyroiditis)
  [ATA15]    Leung AM et al. Thyroid 2015;25:145-6. PMID 25275241, doi:10.1089/thy.2014.0331
             (ATA statement on the risks of excess iodine ingestion, including supplements)
  [PEAR13]   Pearce EN et al. Thyroid 2013;23:523-8. PMID 23472655, doi:10.1089/thy.2013.0128
             (the United States is generally iodine-sufficient)
  [WANG18]   Wang S et al. Endocrine 2018;59:499-505. PMID 29388046, doi:10.1007/s12020-018-1532-5
             (6 RCTs, 344 people: vitamin D lowered TPO antibodies at about 6 months)
  [ROY16]    Roy A et al. Thyroid 2016;26:880-90. PMID 27256300, doi:10.1089/thy.2016.0108
             (celiac disease in about 1 in 62 people with autoimmune thyroid disease; screening
             argued)
  [ODS]      NIH Office of Dietary Supplements fact sheets: tolerable upper intake levels for
             adults, vitamin D 4,000 IU (100 mcg), zinc 40 mg, selenium 400 mcg, iron 45 mg;
             food sources of selenium, zinc and iron.  (ods.od.nih.gov is outside this session's
             network allow-list; the ULs are the published IOM values.)
  [WYNE22]   Wyne KL et al. J Endocr Soc 2022;7:bvac172. PMID 36466005, doi:10.1210/jendso/bvac172
             (hypothyroidism about 9.6% of the U.S. in NHANES 2009-12 and 9.5% -> 11.7% in 2012-19
             claims data, counting people already treated; TSH cut-off 4.0 in the NHANES arm; the
             rise is probably more mild (subclinical) cases).  Replaces [HOLL02]'s older 4.6%.
  [IOM11]    Ross AC et al. J Clin Endocrinol Metab 2011;96:53-8. PMID 21118827,
             doi:10.1210/jc.2010-2704 (a 25-hydroxyvitamin D level of at least 20 ng/mL meets the
             needs of 97.5% of people; below that is low).  Holick MF et al. JCEM 2011;96:1911-30,
             PMID 21646368 (Endocrine Society: deficiency below 20 ng/mL).
  [BSG21]    Snook J et al. Gut 2021;70:2030-51. PMID 34497146, doi:10.1136/gutjnl-2021-325210
             (British Society of Gastroenterology: "SF levels of less than 30 ug/L are generally
             indicative of low body iron stores"; lab lower limits run 15-30; ug/L = ng/mL).
  [KOTW20]   Kotwal A et al. J Clin Endocrinol Metab 2020;105:dgaa672. PMID 32954428,
             doi:10.1210/clinem/dgaa672 ("hypothyroidism is associated with hypercholesterolemia and
             hypertriglyceridemia"; levothyroxine improves the lipid profile)
  [NSF15]    Hirshkowitz M et al. Sleep Health 2015;1:40-3. PMID 29073412,
             doi:10.1016/j.sleh.2014.12.010 (National Sleep Foundation: 7 to 9 hours for adults,
             7 to 8 for older adults).  AASM/SRS (Watson NF, Sleep 2015;38:843-4, PMID 26039963)
             says 7 or more.
  [ND-LABEL] NutriDyn sell sheets (Supplement Facts panels) in Dropbox /NutriDyn/Sales/Practitioner
             Resource/NutriDyn Marketing Materials/: Essential Multi ND476 Rev. 08/25 (per 3 capsules
             includes biotin 500 mcg, iodine 150 mcg, D3 1,000 IU, selenium 100 mcg, zinc 15 mg, no
             iron); D3 5000 with K2 ND382 Rev. 6/24 (label: exceeds the adult upper limit, monitor
             levels; K2 not for people on blood thinners); Iron Support ND563 Rev. 12/25.
"""
import math
import os
import random

from kit import ICONS
from svgkit import T, svg

SLUG = "thyroid"

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
    """Advance width of `text` in Inter at `size` px; a generous guess if the font is missing."""
    try:
        w = _face(_WEIGHTS[weight]).getlength(text) * size / 100
    except Exception:
        w = len(text) * size * (0.68 if text.isupper() else 0.6)
    return w + ls * len(text)


# ============================================================== palette (every symbol is in a KEY)
INK, INK2 = "#2B3236", "#56616A"
T4C, T4E = "#2F6DB5", "#1B4C86"          # T4, the storage form: blue dot
T3C, T3E = "#2E9B5F", "#1C7345"          # T3, the active form: green dot
FEED = "#5F5868"                          # feedback: dashed grey arrow
GEAR, GEAR_E, GEAR_IN, GEAR_TX = "#F2B632", "#9A6A08", "#FFF4D6", "#5E3D00"   # gold gear: nutrient
SKIN, SKIN_EDGE, SKIN_LN = "#F7E4DA", "#EECDBF", "#C4968A"
BONE, BONE_LN = "#F5EDDA", "#BFA57B"
CART, CART_LN, CART_GAP = "#E8EEF2", "#8FA3AE", "#D0DAE0"                     # cartilage (voice box, windpipe)
GLAND_A, GLAND_B, GLAND_LN = "#DC6A70", "#A93744", "#7A2330"                  # thyroid tissue
HYPO, HYPO_LN = "#EF7A3A", "#B8501E"      # hypothalamus (named in the art)
PITU, PITU_LN = "#9B6BC4", "#6A3F91"      # pituitary (named in the art)
CELL_F, CELL_LN, COLLOID, COLLOID_LN = "#E8958C", "#B85F59", "#F8DCAE", "#DDB173"   # thyroid cells / stored hormone
IMMUNE, IMMUNE_N = "#7C5CC0", "#4F3590"   # immune cell (lymphocyte): purple
ANTI = "#D23F37"                          # TPO antibody: red Y
STROMA = "#FBEDEA"


# ============================================================== geometry helpers
def _spline(pts, closed=True):
    """Catmull-Rom curve through pts [(x, y) or (x, y, tension)] as cubic Bezier path data.
    Low tension (0.2-0.5) gives a near-sharp corner at that point."""
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


def _mirror(right):
    """`right` runs from the top centre (x = 0) down the right side to the bottom centre (x = 0).
    Returns the full outline, exactly symmetric about x = 0."""
    return list(right) + [(-p[0], p[1]) + tuple(p[2:]) for p in reversed(right[1:-1])]


def _flip(pts):
    return [(-p[0], p[1]) + tuple(p[2:]) for p in pts]


def _halo_line(d, color, sw=1.2, halo=3.6, dash=""):
    da = f' stroke-dasharray="{dash}"' if dash else ""
    return (f'<path d="{d}" fill="none" stroke="#fff" stroke-width="{halo}" stroke-linecap="round" stroke-linejoin="round"/>'
            f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round"{da}/>')


def badge(x, y, n, fill, r=8.2, size=10.5):
    """Numbered step badge (white halo so it reads on any background)."""
    return (f'<circle cx="{x}" cy="{y}" r="{r + 1.6}" fill="#fff"/><circle cx="{x}" cy="{y}" r="{r}" fill="{fill}"/>'
            + T(x, y + size * 0.36, str(n), size, 800, "#fff", "middle"))


# ============================================================== symbols (same code draws the art and the KEY)
def t4(x, y, r=4.3):
    return f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="{T4C}" stroke="{T4E}" stroke-width=".9"/>'


def t3(x, y, r=4.3):
    return f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="{T3C}" stroke="{T3E}" stroke-width=".9"/>'


def gear(cx, cy, r, sym):
    """Gold gear (a nutrient that step needs) with the nutrient's symbol in its hub."""
    teeth, pts = 8, []
    for i in range(teeth):
        a0 = 2 * math.pi * i / teeth
        for da, rr in ((-0.20, 0.80), (-0.12, 1.0), (0.12, 1.0), (0.20, 0.80)):
            a = a0 + da * 2 * math.pi / teeth * 1.35
            pts.append(f"{cx + r * rr * math.cos(a):.2f},{cy + r * rr * math.sin(a):.2f}")
    fs = 9.8 if len(sym) == 1 else 9.7
    return (f'<polygon points="{" ".join(pts)}" fill="url(#thy-gear)" stroke="{GEAR_E}" stroke-width="1" '
            f'stroke-linejoin="round"/><circle cx="{cx}" cy="{cy}" r="{r * 0.64:.2f}" fill="{GEAR_IN}" '
            f'stroke="{GEAR_E}" stroke-width=".7"/>' + T(cx, cy + fs * 0.36, sym, fs, 800, GEAR_TX, "middle"))


def gear_tag(x, y, sym, label, r=11.8, size=10.5):
    """Gear + its nutrient name to the right.  Returns (markup, right edge x)."""
    lx = x + r + 4
    return gear(x, y, r, sym) + T(lx, y + size * 0.36, label, size, 700, "#6E4A00"), lx + tw(label, size, 700)


def antibody(x, y, ang=0, s=1.0):
    """TPO antibody: a red Y; its two arms grip the thyroid cell, the stem points away."""
    return (f'<g transform="translate({x:.1f},{y:.1f}) rotate({ang:.0f}) scale({s})">'
            f'<path d="M0,0 V6.4 M0,0 L-3.6,-3.9 M0,0 L3.6,-3.9" fill="none" stroke="#fff" stroke-width="3.6" '
            'stroke-linecap="round"/>'
            f'<path d="M0,0 V6.4 M0,0 L-3.6,-3.9 M0,0 L3.6,-3.9" fill="none" stroke="{ANTI}" stroke-width="1.9" '
            'stroke-linecap="round"/></g>')


def lymphocyte(x, y, r=3.5):
    return (f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="{IMMUNE}" stroke="{IMMUNE_N}" stroke-width=".8"/>'
            f'<circle cx="{x - r * .25:.1f}" cy="{y - r * .25:.1f}" r="{r * .5:.2f}" fill="#A890E0" opacity=".7"/>')


def defs_common():
    mk = lambda i, c, w=4.0: (f'<marker id="{i}" viewBox="0 0 10 10" refX="6.4" refY="5" markerWidth="{w}" '
                              f'markerHeight="{w}" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="{c}"/></marker>')
    return ('<radialGradient id="thy-gear" cx=".38" cy=".34" r=".75"><stop offset="0" stop-color="#FFE7A0"/>'
            f'<stop offset=".6" stop-color="{GEAR}"/><stop offset="1" stop-color="#D99812"/></radialGradient>'
            + mk("thy-ah-sig", "#9B3F68") + mk("thy-ah-t4", T4C, 4.4) + mk("thy-ah-t3", T3C, 4.4)
            + mk("thy-ah-fb", FEED, 4.6))


# ============================================================== the neck, front view (local units)
# Proportions: neck about 1.4 times the gland's width; the voice box (thyroid cartilage, with the
# V notch and its horns) above the cricoid ring; the gland's isthmus crosses windpipe rings 2 to 4,
# the upper poles reach the middle of the thyroid cartilage, the lower poles ring 6.  The skin is
# drawn see-through so the parts inside show, as in a medical atlas.
NECK_R = [(0, 30), (74, 30, 0.4), (73.5, 56), (72, 90), (72.8, 126), (76.5, 160), (87, 181), (110, 195),
          (138, 205), (158, 217), (167, 236), (169, 300, 0.4), (0, 300)]
HEAD_R = [(0, -40), (84, -40, 0.4), (95, -10), (96.5, 12), (92.5, 30), (83.5, 44), (66, 56.5), (44.5, 66),
          (23, 72.5), (0, 75.5)]
CARTILAGE_R = [(0, 100.5, 0.55), (5, 95.6), (14, 93.2), (24.5, 93.6), (30.6, 87.4, 0.35), (33.6, 94), (32.6, 106),
               (29.6, 118), (25.8, 127.6), (23.8, 134.6, 0.4), (18, 132.8), (9.5, 130.6), (0, 131.2)]
CRICOID_R = [(0, 136.6), (12, 136.1), (21, 137.6), (22.8, 141.8), (21.2, 147.6), (12, 148.8), (0, 149.2)]
GLAND_R = [(0, 158.6), (7, 157.9), (13, 156.2), (16.6, 150), (18.6, 140), (20.6, 128), (23, 116.5),
           (26.6, 107.6, 0.45), (31.6, 110), (38, 121), (44.6, 136), (49.6, 152), (52, 168), (51, 182.6),
           (46.4, 193.6), (38.4, 200.4), (29, 201.8), (21.4, 197.4), (17, 189.6), (14.6, 182.4), (8, 181.4),
           (0, 182.8)]
CLAV_R = [(11, 231.5), (38, 229), (78, 232.5), (114, 226.5), (149, 218.5, 0.5), (151, 225.5, 0.5), (116, 234.5),
          (79, 240.5), (40, 237.6), (12, 242, 0.6)]
MANUB = [(0, 239.5), (8, 237.6), (16.5, 236.5), (19, 246), (22, 300, 0.4), (-22, 300, 0.4), (-19, 246),
         (-16.5, 236.5), (-8, 237.6)]

NECK_D, HEAD_D = _spline(_mirror(NECK_R)), _spline(_mirror(HEAD_R))
CART_D, CRIC_D, GLAND_D = (_spline(_mirror(CARTILAGE_R)), _spline(_mirror(CRICOID_R)), _spline(_mirror(GLAND_R)))
CLAV_RD, CLAV_LD, MANUB_D = _spline(CLAV_R), _spline(_flip(CLAV_R)), _spline(MANUB)
RINGS = [150.6 + 8.45 * i for i in range(14)]          # windpipe ring tops (height 5.5)


def neck_defs():
    return ('<linearGradient id="thy-skin" x1="-1" y1="0" x2="1" y2="0" gradientUnits="objectBoundingBox">'
            f'<stop offset="0" stop-color="{SKIN_EDGE}"/><stop offset=".5" stop-color="#FCEFE8"/>'
            f'<stop offset="1" stop-color="{SKIN_EDGE}"/></linearGradient>'
            '<radialGradient id="thy-face" cx=".5" cy=".2" r=".9"><stop offset="0" stop-color="#FCEEE7"/>'
            f'<stop offset="1" stop-color="{SKIN_EDGE}"/></radialGradient>'
            '<linearGradient id="thy-gland" x1="0" y1="0" x2="1" y2="1">'
            f'<stop offset="0" stop-color="{GLAND_A}"/><stop offset=".55" stop-color="#C44C57"/>'
            f'<stop offset="1" stop-color="{GLAND_B}"/></linearGradient>'
            '<linearGradient id="thy-cart" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#D7E1E7"/>'
            f'<stop offset=".5" stop-color="#F6F9FA"/><stop offset="1" stop-color="#D7E1E7"/></linearGradient>'
            '<radialGradient id="thy-chin" cx=".5" cy="0" r=".9"><stop offset="0" stop-color="#C99A8A" stop-opacity=".45"/>'
            '<stop offset="1" stop-color="#C99A8A" stop-opacity="0"/></radialGradient>'
            f'<clipPath id="thy-neckclip"><path d="{NECK_D}"/></clipPath>'
            f'<clipPath id="thy-glandclip"><path d="{GLAND_D}"/></clipPath>'
            '<linearGradient id="thy-fadeg" x1="0" y1="246" x2="0" y2="290" gradientUnits="userSpaceOnUse">'
            '<stop offset="0" stop-color="#fff"/><stop offset="1" stop-color="#000"/></linearGradient>'
            '<mask id="thy-fade" maskUnits="userSpaceOnUse" x="-200" y="-60" width="400" height="380">'
            '<rect x="-200" y="-60" width="400" height="380" fill="url(#thy-fadeg)"/></mask>')


def _gland_texture():
    """Soft lobules inside the gland plus a sheen on each lobe, clipped to the gland."""
    rnd = random.Random(19)
    o = []
    for s in (1, -1):
        for _ in range(26):
            x = s * rnd.uniform(18, 50)
            y = rnd.uniform(112, 199)
            o.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{rnd.uniform(3.4, 5.6):.1f}" fill="none" '
                     'stroke="#8E2A37" stroke-width=".7" opacity=".28"/>')
        o.append(f'<ellipse cx="{s * 31}" cy="146" rx="6.5" ry="20" fill="#fff" opacity=".13" '
                 f'transform="rotate({-14 * s} {s * 31} 146)"/>')
    for x, y in ((-8, 165), (8, 165), (0, 172)):
        o.append(f'<circle cx="{x}" cy="{y}" r="3.6" fill="none" stroke="#8E2A37" stroke-width=".7" opacity=".28"/>')
    return f'<g clip-path="url(#thy-glandclip)">{"".join(o)}</g>'


def neck_figure():
    """The neck in local units (centre line x = 0, chin bottom y = 75.5)."""
    skin = (f'<path d="{NECK_D}" fill="{SKIN}" stroke="{SKIN_LN}" stroke-width="2.4" stroke-linejoin="round"/>'
            f'<path d="{NECK_D}" fill="url(#thy-skin)"/>')
    # neck muscles (sternocleidomastoid) as soft form shading, and the shadow the chin casts
    form = ('<g clip-path="url(#thy-neckclip)">'
            + "".join(f'<path d="M{70 * s},48 C{58 * s},110 {32 * s},176 {15 * s},236" fill="none" stroke="#E2B6A6" '
                      'stroke-width="17" stroke-linecap="round" opacity=".32"/>' for s in (1, -1))
            + '<ellipse cx="0" cy="78" rx="78" ry="26" fill="url(#thy-chin)"/></g>')
    head = (f'<path d="{HEAD_D}" fill="url(#thy-face)" stroke="{SKIN_LN}" stroke-width="2" stroke-linejoin="round"/>'
            '<path d="M-60,60 C-34,73 34,73 60,60" fill="none" stroke="#D8AE9F" stroke-width="1.4" opacity=".7"/>')
    bones = (f'<path d="{MANUB_D}" fill="{BONE}" stroke="{BONE_LN}" stroke-width="1"/>'
             f'<path d="{CLAV_RD}" fill="{BONE}" stroke="{BONE_LN}" stroke-width="1"/>'
             f'<path d="{CLAV_LD}" fill="{BONE}" stroke="{BONE_LN}" stroke-width="1"/>')
    rings = "".join(f'<rect x="-17.8" y="{y:.1f}" width="35.6" height="5.5" rx="2.6" fill="url(#thy-cart)" '
                    f'stroke="{CART_LN}" stroke-width=".7"/>' for y in RINGS)
    windpipe = (f'<rect x="-17.8" y="146" width="35.6" height="160" rx="3" fill="{CART_GAP}" stroke="{CART_LN}" '
                f'stroke-width=".8"/>{rings}')
    larynx = (f'<path d="{CRIC_D}" fill="url(#thy-cart)" stroke="{CART_LN}" stroke-width=".9"/>'
              f'<path d="{CART_D}" fill="url(#thy-cart)" stroke="{CART_LN}" stroke-width="1"/>'
              '<path d="M0,101 C-.4,108 -.3,116 0,123" stroke="#B7C6CE" stroke-width="2.2" fill="none" '
              'stroke-linecap="round"/>'                                                   # the Adam's-apple ridge
              f'<path d="M-30,96 C-24,108 -23,120 -24,128 M30,96 C24,108 23,120 24,128" fill="none" stroke="{CART_LN}" '
              'stroke-width=".7" opacity=".55"/>')
    gland = (f'<path d="{GLAND_D}" fill="url(#thy-gland)" stroke="{GLAND_LN}" stroke-width="1.3" '
             f'stroke-linejoin="round"/>{_gland_texture()}')
    # the windpipe passes behind the breastbone: draw it, then the breastbone and collarbones on top
    body = (f'<g mask="url(#thy-fade)">{skin}{form}{windpipe}{bones}{larynx}{gland}</g>{head}')
    return body


# ============================================================== the brain, side view (facing left)
def brain_side():
    """Midline view: cerebrum, corpus callosum, thalamus, HYPOTHALAMUS (orange) and the PITUITARY
    (violet) hanging from its stalk into the bony saddle (sella), brainstem and cerebellum."""
    cere = [(-52, 3), (-50.5, -14), (-41.5, -29.5), (-24, -40.5), (-2, -44.5), (20, -41.5), (38.5, -31.5),
            (49.5, -15.5), (52.5, 1.5), (47, 12), (36, 15.2), (24, 11.6), (14, 7.6), (3, 10.4), (-8, 13.4),
            (-19, 13.2), (-31, 13.2), (-43, 10.4)]
    cbl = [(17, 19), (29, 11.6), (42.6, 12.6), (50.6, 21.6), (48.4, 32.4), (37.6, 38.4), (25, 36.6), (18.4, 29.6)]
    stem = [(1, 7), (11, 4), (16.6, 11), (19.2, 22), (17.6, 34), (16.4, 49, 0.4), (8.4, 49, 0.4), (7.2, 38),
            (2.6, 31), (-1.6, 22), (-0.6, 13)]
    folds = ["M-33,-6 C-28,-18 -15,-25 -2,-26.5 C12,-27.5 24,-23 32,-14",
             "M-44,-4 C-42,-13 -37,-20 -30,-25.5", "M-19,-33 C-17,-29 -13,-27.5 -10.5,-29.5",
             "M3,-36.5 C4.6,-32.5 6.6,-30 7.6,-27", "M22,-32.5 C21.6,-28.6 23.6,-26 27,-24.4",
             "M38,-22 C33.6,-16 31.6,-8 31.2,1", "M31.2,1 C35.6,0 41.6,-.4 46.6,-2.4",
             "M-41.6,4.6 C-35.6,2 -29.6,2.8 -24.6,5.4", "M-13,-18.4 C-9,-20.4 -3,-21 2,-20.4"]
    o = [f'<path d="{_spline(cbl)}" fill="#DDA0B2" stroke="#B57790" stroke-width=".9"/>']
    for k in range(4):
        o.append(f'<path d="M{21 + k * 1.2},{17 + k * 4.4} C{28 + k},{15 + k * 4.4} {37 + k * .6},{17 + k * 4.6} '
                 f'{44 - k * 1.4},{21 + k * 4.4}" fill="none" stroke="#C07E96" stroke-width=".9" stroke-linecap="round"/>')
    o.append(f'<path d="{_spline(stem)}" fill="#E5ADB9" stroke="#B57790" stroke-width=".9"/>')
    o.append(f'<path d="{_spline(cere)}" fill="#F0C6D2" stroke="#B57790" stroke-width="1.05"/>')
    o += [f'<path d="{d}" fill="none" stroke="#CD93A7" stroke-width="1.15" stroke-linecap="round"/>' for d in folds]
    cc = "M-21,-1 C-20,-11 -9,-16 3,-15.6 C14,-15.2 22.6,-11 24.4,-5 C25.2,-1.6 23,.6 20,0"
    o.append(f'<path d="{cc}" fill="none" stroke="#C995A8" stroke-width="6.6" stroke-linecap="round"/>'
             f'<path d="{cc}" fill="none" stroke="#FAE7EE" stroke-width="4.8" stroke-linecap="round"/>')
    o.append('<ellipse cx="4.4" cy="1.4" rx="9.2" ry="5.4" fill="#E6AABD" stroke="#B57790" stroke-width=".8"/>')   # thalamus
    # bony saddle under the pituitary
    o.append(f'<path d="M-21,21.6 C-20.6,31.4 -4,31.8 -2.6,21.4" fill="none" stroke="{BONE_LN}" stroke-width="3.4" '
             'stroke-linecap="round"/>'
             f'<path d="M-21,21.6 C-20.6,31.4 -4,31.8 -2.6,21.4" fill="none" stroke="{BONE}" stroke-width="1.8" '
             'stroke-linecap="round"/>')
    # stalk, pituitary, hypothalamus (with a soft glow)
    o.append(f'<path d="M-9,12.6 L-11.2,19" stroke="#A9739A" stroke-width="2.4" stroke-linecap="round"/>')
    o.append(f'<ellipse cx="-11.6" cy="23.2" rx="6.4" ry="4.7" fill="url(#thy-pitu)" stroke="{PITU_LN}" stroke-width=".9"/>')
    o.append('<circle cx="-8.4" cy="8.2" r="10.5" fill="#F7A56A" opacity=".25"/>'
             f'<ellipse cx="-8.4" cy="8.2" rx="7" ry="4.6" fill="url(#thy-hypo)" stroke="{HYPO_LN}" stroke-width=".9" '
             'transform="rotate(-12 -8.4 8.2)"/>')
    return "".join(o)


def brain_defs():
    return ('<radialGradient id="thy-hypo" cx=".4" cy=".35" r=".75"><stop offset="0" stop-color="#FFC59A"/>'
            f'<stop offset="1" stop-color="{HYPO}"/></radialGradient>'
            '<radialGradient id="thy-pitu" cx=".4" cy=".35" r=".75"><stop offset="0" stop-color="#D7B8F0"/>'
            f'<stop offset="1" stop-color="{PITU}"/></radialGradient>'
            '<radialGradient id="thy-lens" cx=".5" cy=".45" r=".6"><stop offset="0" stop-color="#FFFFFF"/>'
            '<stop offset="1" stop-color="#F6E8EE"/></radialGradient>')


# ============================================================== small organ and cell drawings
LIVER_PTS = [(-20, -6), (-14, -12.6), (0, -13.6), (14, -12), (21.6, -9.6), (20.4, -5), (11, 1.2), (1, 7.4),
             (-8, 11.6), (-15.6, 10.2), (-20.6, 3.4)]


def liver_icon(x, y, s=1.0):
    return (f'<g transform="translate({x},{y}) scale({s})"><path d="{_spline(LIVER_PTS)}" fill="url(#thy-liver)" '
            'stroke="#7E2F24" stroke-width=".9"/><path d="M8,-11.4 C6.6,-6 4.6,-1.4 2.6,3.4" stroke="#7E2F24" '
            'stroke-width=".8" fill="none" opacity=".6"/><path d="M-14,-9 C-8,-11.6 -1,-12 6,-11.4" stroke="#fff" '
            'stroke-width="1.6" fill="none" opacity=".45" stroke-linecap="round"/></g>')


def kidney_icon(x, y, s=1.0):
    bean = [(0, -13), (7.4, -11.4), (10.6, -4), (10.4, 5.4), (6.4, 12.4), (-0.4, 13), (-3.6, 8), (-1.4, 3.6),
            (-2, -2.4), (-4.4, -7.4)]
    return (f'<g transform="translate({x},{y}) scale({s})"><path d="{_spline(bean)}" fill="url(#thy-kidney)" '
            'stroke="#7A2A2E" stroke-width=".9"/><path d="M-1.4,1 C-5,1 -8,2.6 -10,6" stroke="#B85D62" '
            'stroke-width="2" fill="none" stroke-linecap="round"/></g>')


def muscle_icon(x, y, s=1.0):
    belly = [(0, -15), (5.4, -9), (6.8, 0), (5.4, 9), (0, 15), (-5.4, 9), (-6.8, 0), (-5.4, -9)]
    fib = "".join(f'<path d="M{dx * .55},-12 C{dx},-5 {dx},5 {dx * .55},12" stroke="#B04F49" stroke-width=".6" '
                  'fill="none" opacity=".6"/>' for dx in (-4, -1.4, 1.4, 4))
    return (f'<g transform="translate({x},{y}) scale({s})"><path d="M0,-21 V-14 M0,14 V21" stroke="#E9E2D6" '
            'stroke-width="3.2" stroke-linecap="round"/><path d="M0,-21 V-14 M0,14 V21" stroke="#BFB6A6" '
            f'stroke-width="3.2" stroke-linecap="round" opacity=".5"/><path d="{_spline(belly)}" fill="url(#thy-muscle)" '
            f'stroke="#8E3530" stroke-width=".9"/>{fib}</g>')


def body_cell(x, y, r=27):
    """A body cell: membrane and nucleus (the T3 dots drawn on it are keyed)."""
    o = [f'<circle cx="{x}" cy="{y}" r="{r}" fill="#FDF1EC" stroke="#D69A90" stroke-width="2"/>',
         f'<circle cx="{x}" cy="{y}" r="{r - 3}" fill="none" stroke="#F3D4CC" stroke-width="1"/>',
         f'<circle cx="{x + 3}" cy="{y + 2}" r="{r * .36:.1f}" fill="#E7D3EA" stroke="#A98AB5" stroke-width="1"/>',
         f'<circle cx="{x + 5}" cy="{y + 4}" r="2.2" fill="#A98AB5"/>']
    return "".join(o)


def organ_defs():
    return ('<linearGradient id="thy-liver" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#C8654F"/>'
            '<stop offset="1" stop-color="#8F3A2A"/></linearGradient>'
            '<linearGradient id="thy-kidney" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#D0706F"/>'
            '<stop offset="1" stop-color="#97383F"/></linearGradient>'
            '<linearGradient id="thy-muscle" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#C4544D"/>'
            '<stop offset=".5" stop-color="#E07F72"/><stop offset="1" stop-color="#C4544D"/></linearGradient>')


# ============================================================== text-fit guard
def _plain(s):
    import re
    return re.sub(r"<[^>]+>", "", s).replace("&#8220;", '"').replace("&#8221;", '"').replace("&#8217;", "'") \
        .replace("&amp;", "&")


def _rich_w(text, size, weight):
    """Width of text that may hold one <tspan font-weight='800'> lead-in (measured bold) before a body."""
    import re
    m = re.match(r"\s*<tspan font-weight='(\d+)'>(.*?)</tspan>(.*)$", text)
    if not m:
        return tw(_plain(text), size, weight)
    return tw(_plain(m.group(2)), size, int(m.group(1))) + tw(_plain(m.group(3)), size, weight)


def fit(text, size, weight, maxw, where):
    """Raise if SVG text would run past its column (so overflow can never ship silently)."""
    w = _rich_w(text, size, weight)
    if w > maxw:
        raise ValueError(f"thyroid sheet: text too wide in {where}: {w:.0f} > {maxw:.0f}: {_plain(text)!r}")
    return text


def _wrap(text, width, size, weight=500):
    lines, cur = [], ""
    for w in text.split():
        t_ = (cur + " " + w).strip()
        if cur and tw(_plain(t_), size, weight) > width:
            lines.append(cur)
            cur = w
        else:
            cur = t_
    if cur:
        lines.append(cur)
    return lines


# ============================================================== picture 1: how your thyroid works
W = 760
P1_HDR = 24
FX, FY, FS = 170, -14.6, 0.84       # neck figure: local (0, 0) -> (FX, FY), scale FS (local y 46 = top of the art)
P1_ART = 218                        # bottom of the art band; the step strip and the KEY sit below it
BR_C, BR_R = (398, 84), 50          # brain inset
ORG = (404, 148, 566, 208)          # liver / kidneys / muscles node (x0, y0, x1, y1)
CELL_C, CELL_R = (690, 176), 24     # every cell
P1_STEPS = 222
P1_KEY = 279                        # 5 units of air under badge 3 of the step strip
P1_H = P1_KEY + 35                  # KEY strip (27 tall) + 8 units of margin above the panel border


def _fig(x, y):
    """Local neck-figure units -> viewBox units."""
    return FX + FS * x, FY + FS * y


def _arrow(d, color, sw, marker, dash=""):
    da = f' stroke-dasharray="{dash}"' if dash else ""
    return (f'<path d="{d}" fill="none" stroke="#fff" stroke-width="{sw + 3.4}" stroke-linecap="round" '
            f'stroke-linejoin="round" opacity=".92"/><path d="{d}" fill="none" stroke="{color}" stroke-width="{sw}" '
            f'stroke-linecap="round" stroke-linejoin="round"{da} marker-end="url(#{marker})"/>')


def _q(p0, c, p1, t):
    return tuple((1 - t) ** 2 * p0[i] + 2 * (1 - t) * t * c[i] + t * t * p1[i] for i in (0, 1))


def _tag(x, y, text, fill, size=10.8):
    w = tw(text, size, 800) + 14
    return (f'<rect x="{x - w / 2:.1f}" y="{y - 8.5:.1f}" width="{w:.1f}" height="17" rx="8.5" fill="{fill}" '
            'stroke="#fff" stroke-width="1.6"/>' + T(x, y + size * 0.36, text, size, 800, "#fff", "middle"))


def label_left(x, y, title, sub, target, tcolor=INK, size=10.6, maxw=96):
    """Anatomy label in the clear column left of the neck, with a leader to `target` (viewBox units)."""
    fit(title, size, 800, maxw, "anatomy label")
    o = [T(x, y, title, size, 800, tcolor, ls=0.3)]
    if sub:
        fit(sub, 10, 500, maxw, "anatomy label")
        o.append(T(x, y + 12.4, sub, 10, 500, INK2, italic=True))
    sx, sy = x + tw(title, size, 800, 0.3) + 5, y - size * 0.34
    o.append(_halo_line(f"M{sx:.1f},{sy:.1f} L{target[0]:.1f},{target[1]:.1f}", "#4F4549", 1.1, 3.2))
    o.append(f'<circle cx="{target[0]:.1f}" cy="{target[1]:.1f}" r="2.3" fill="#4F4549" stroke="#fff" stroke-width="1"/>')
    return "".join(o)


def _panel(h, title, aside, c1):
    return (f'<rect x=".7" y=".7" width="{W - 1.4}" height="{h - 1.4}" rx="10" fill="#fff" stroke="#E3D1DA" stroke-width="1.4"/>'
            f'<path d="M.7,24 V10.7 A10,10 0 0 1 10.7,.7 H{W - 10.7} A10,10 0 0 1 {W - .7},10.7 V24 Z" fill="{c1}"/>'
            + T(14, 16.6, title, 12, 800, "#fff", ls=1.0)
            + T(W - 14, 16.4, aside, 10.4, 600, "#FBE3EE", "end", italic=True))


def picture1(t):
    c1, deep, soft = t["c1"], t["deep"], t["soft"]
    o = [f'<defs>{defs_common()}{neck_defs()}{brain_defs()}{organ_defs()}'
         f'<clipPath id="thy-p1clip"><rect x="0" y="{P1_HDR}" width="336" height="{P1_ART - P1_HDR}"/></clipPath>'
         f'<clipPath id="thy-brclip"><circle cx="{BR_C[0]}" cy="{BR_C[1]}" r="{BR_R - 1}"/></clipPath></defs>',
         _panel(P1_H, "HOW YOUR THYROID WORKS", "a feedback loop, like a thermostat", c1)]

    # ---- the neck, jaw to collarbones (clipped to the art band)
    o.append(f'<g clip-path="url(#thy-p1clip)"><g transform="translate({FX},{FY}) scale({FS})">{neck_figure()}</g></g>')
    o.append(label_left(10, 62, "VOICE BOX", "(larynx)", _fig(-12, 104)))
    o.append(label_left(10, 104, "THYROID GLAND", "butterfly shape", _fig(-42, 156), c1))
    o.append(label_left(10, 148, "WINDPIPE", "(trachea)", _fig(-5, 221)))
    # COLLARBONE: label on a white pill under the bone, with a real leader up to a dot on the
    # middle of the left clavicle (local (-96, 233.6): the bone runs about y 229.5-237.7 there)
    cx_, cy_ = _fig(-96, 258)
    bone = _fig(-96, 233.6)
    o.append(_halo_line(f"M{cx_:.1f},{cy_ - 9:.1f} L{bone[0]:.1f},{bone[1]:.1f}", "#4F4549", 1.1, 3.2))
    o.append(f'<circle cx="{bone[0]:.1f}" cy="{bone[1]:.1f}" r="2.3" fill="#4F4549" stroke="#fff" stroke-width="1"/>')
    o.append(f'<rect x="{cx_ - 38:.1f}" y="{cy_ - 9:.1f}" width="76" height="15" rx="5" fill="#fff" opacity=".92"/>'
             + T(cx_, cy_ + 2.4, "COLLARBONE", 9.8, 800, INK, "middle", ls=0.4))
    if cy_ + 6 > P1_ART - 2:
        raise ValueError("thyroid sheet: COLLARBONE label runs past the art band")

    # ---- 1 and 2: the brain inset (hypothalamus -> TRH, pituitary -> TSH)
    bx, by = BR_C
    o.append(T(bx - BR_R - 8, 48, "BRAIN", 10.4, 800, INK, "end", ls=0.5)
             + T(bx - BR_R - 8, 60.4, "side view", 10, 500, INK2, "end", italic=True))
    o.append(f'<circle cx="{bx}" cy="{by}" r="{BR_R + 2.4}" fill="#fff"/><circle cx="{bx}" cy="{by}" r="{BR_R}" fill="url(#thy-lens)"/>')
    sc = 0.86
    o.append(f'<g clip-path="url(#thy-brclip)"><g transform="translate({bx + 1},{by - 2}) scale({sc})">{brain_side()}</g></g>')
    o.append(f'<circle cx="{bx}" cy="{by}" r="{BR_R}" fill="none" stroke="{c1}" stroke-width="2"/>')
    hyp = (bx + 1 - 8.4 * sc, by - 2 + 8.2 * sc)
    pit = (bx + 1 - 11.6 * sc, by - 2 + 23.2 * sc)
    lx = bx + BR_R + 20
    for (px, py), ly, n, title, sub in ((hyp, 66, 1, "HYPOTHALAMUS", "checks levels, sends TRH"),
                                        (pit, 104, 2, "PITUITARY", "answers with TSH")):
        o.append(_halo_line(f"M{px:.1f},{py:.1f} L{lx - 11:.1f},{ly - 4:.1f}", "#4F4549", 1.1, 3.0))
        o.append(f'<circle cx="{px:.1f}" cy="{py:.1f}" r="2" fill="#4F4549" stroke="#fff" stroke-width=".8"/>')
        o.append(badge(lx, ly - 4, n, c1))
        o.append(T(lx + 13, ly, fit(title, 11.2, 800, 150, "brain label"), 11.2, 800, deep, ls=0.4))
        o.append(T(lx + 13, ly + 13, fit(sub, 10.4, 500, 136, "brain label"), 10.4, 500, INK))

    # ---- TSH: pituitary -> thyroid
    a0 = (bx + BR_R * math.cos(math.radians(172)), by + BR_R * math.sin(math.radians(172)))
    a1 = _fig(40, 116)
    a1 = (a1[0] + 8, a1[1])
    ac = (288, 86)
    o.append(_arrow(f"M{a0[0]:.1f},{a0[1]:.1f} Q{ac[0]},{ac[1]} {a1[0]:.1f},{a1[1]:.1f}", c1, 3.0, "thy-ah-sig"))
    o.append(_tag(*_q(a0, ac, a1, 0.3), "TSH", c1))

    # ---- 3: the thyroid makes T4 (needs iodine and iron)
    b0 = _fig(46, 190)
    b0 = (b0[0] + 6, b0[1])
    b1, bc = (ORG[0] - 8, (ORG[1] + ORG[3]) / 2), (296, 184)
    o.append(_arrow(f"M{b0[0]:.1f},{b0[1]:.1f} Q{bc[0]},{bc[1]} {b1[0]:.1f},{b1[1]:.1f}", T4C, 2.6, "thy-ah-t4"))
    for tt in (0.3, 0.52, 0.74):
        o.append(t4(*_q(b0, bc, b1, tt)))
    tx_, ty_ = _q(b0, bc, b1, 0.6)
    o.append(_tag(tx_, ty_ - 15, "T4", T4C))
    # gx 280: badge 3 (x 245-265) clears the neck/shoulder contour (about x 237 at that height), the
    # Fe gear clears the shoulder, the labels end left of the brain lens, the TSH tag sits above
    gx = 280
    g1, r1x = gear_tag(gx, 115, "I", "iodine")
    g2, r2x = gear_tag(gx, 138, "Fe", "iron")
    o += [g1, g2, badge(gx - 25, 126.5, 3, c1)]
    lens_x = BR_C[0] - math.sqrt(BR_R ** 2 - (115 - BR_C[1]) ** 2)
    if max(r1x, r2x) > lens_x - 8:
        raise ValueError("thyroid sheet: step-3 gear labels run into the brain lens")

    # ---- 4: liver, kidneys and muscles turn T4 into active T3 (need selenium and zinc)
    x0, y0, x1, y1 = ORG
    o.append(f'<rect x="{x0}" y="{y0}" width="{x1 - x0}" height="{y1 - y0}" rx="13" fill="{soft}" stroke="#D9AFC3" stroke-width="1.3"/>')
    mid = (x0 + x1) / 2
    o.append(liver_icon(x0 + 36, y0 + 24, 1.02) + kidney_icon(mid + 2, y0 + 24, 0.9) + muscle_icon(x1 - 30, y0 + 25, 0.84))
    for xx, lab in ((x0 + 36, "liver"), (mid + 2, "kidneys"), (x1 - 30, "muscles")):
        o.append(T(xx, y1 - 8, lab, 10.2, 700, deep, "middle"))
    o.append(badge(x0 + 3, y0 + 3, 4, c1))
    # x0+44 / x0+130: the Se gear now clears the brain lens's white halo (r + 2.4) by about 5 units
    gse = (x0 + 44, y0 - 16)
    g3, _ = gear_tag(*gse, "Se", "selenium")
    g4, r4x = gear_tag(x0 + 130, y0 - 16, "Zn", "zinc")
    o += [g3, g4]
    if math.hypot(gse[0] - BR_C[0], gse[1] - BR_C[1]) - 11.8 < BR_R + 2.4 + 3 or r4x > W - 12:
        raise ValueError("thyroid sheet: selenium / zinc gears collide with the brain lens or the edge")

    # ---- T3 to every cell (5)
    cxc, cyc = CELL_C
    r0, r1 = (x1 + 6, (y0 + y1) / 2), (cxc - CELL_R - 9, cyc)
    o.append(_arrow(f"M{r0[0]},{r0[1]} L{r1[0]},{r1[1]}", T3C, 2.6, "thy-ah-t3"))
    o.append(t3(r0[0] + (r1[0] - r0[0]) * 0.28, r0[1] + (r1[1] - r0[1]) * 0.28))
    o.append(_tag((r0[0] + r1[0]) / 2 + 8, r0[1] - 15, "T3", T3C))
    o.append(body_cell(cxc, cyc, CELL_R))
    for dx, dy in ((-7, 14), (2, -10)):
        o.append(t3(cxc + dx, cyc + dy, 3.4))
    o.append(badge(cxc - CELL_R + 2, cyc - CELL_R + 2, 5, c1))
    o.append(T(cxc, cyc + CELL_R + 13, "every cell", 10.2, 700, deep, "middle"))

    # ---- feedback: hormone in the blood tells the brain to ease off (runs round the outside, crosses nothing)
    ea = math.radians(-52)
    e1 = (bx + (BR_R + 6) * math.cos(ea), by + (BR_R + 6) * math.sin(ea))
    d = (f"M{cxc + CELL_R + 3},{cyc} H{736} Q{744},{cyc} {744},{cyc - 8} V{44} Q{744},{35} {735},{35} "
         f"H{e1[0] + 22:.1f} Q{e1[0] + 6:.1f},{35} {e1[0]:.1f},{e1[1]:.1f}")
    o.append(_arrow(d, FEED, 1.9, "thy-ah-fb", "5 4"))
    o.append(f'<rect x="622" y="47" width="112" height="31" rx="7" fill="#fff" stroke="#D8D2DC" stroke-width="1"/>'
             + T(630, 59.6, fit("Enough hormone?", 10.2, 800, 98, "feedback"), 10.2, 800, FEED)
             + T(630, 72, fit("The brain eases off.", 10.2, 500, 98, "feedback"), 10.2, 500, FEED))

    # ---- step strip: the words live here, not on the art
    o.append(f'<path d="M12,{P1_STEPS} H{W - 12}" stroke="#EADDE3" stroke-width="1"/>')
    B = "<tspan font-weight='800'>"
    steps = [f"{B}Hypothalamus:</tspan> checks levels, sends TRH, a wake-up signal.",
             f"{B}Pituitary:</tspan> answers with TSH, the &#8220;make more&#8221; signal.",
             f"{B}Thyroid:</tspan> uses iodine and iron to make T4 (and a little T3).",
             f"{B}Liver, kidneys, muscles:</tspan> turn T4 into active T3.",
             f"{B}Every cell:</tspan> T3 sets your pace: energy, warmth, heartbeat.",
             f"{B}Feedback:</tspan> when levels are right, the brain eases off."]
    for i, s in enumerate(steps):
        col, row = divmod(i, 3)
        x = 22 + col * 376
        y = P1_STEPS + 15 + row * 15.8
        fit(s, 10.6, 500, 352 if col == 0 else 338, "step strip")
        if i < 5:
            o.append(badge(x, y - 3.8, i + 1, c1, 7.4, 9.8))
        else:
            o.append(f'<circle cx="{x}" cy="{y - 3.8}" r="7.4" fill="#fff" stroke="{FEED}" stroke-width="1.5" '
                     'stroke-dasharray="2.6 1.8"/>' + T(x, y - 0.3, "&#8635;", 10, 800, FEED, "middle"))
        o.append(T(x + 13, y, s, 10.6, 500, INK))
    o.append(key1(P1_KEY, c1))
    return svg(W, P1_H, "".join(o),
               "How your thyroid works: a front view of the neck with the butterfly-shaped thyroid gland on the "
               "windpipe below the voice box, and the control loop. The hypothalamus sends TRH, the pituitary sends "
               "TSH, the thyroid makes T4, the liver, kidneys and muscles turn T4 into active T3, T3 reaches every "
               "cell, and hormone in the blood tells the brain to ease off.")


def _key_strip(y, items, w=W, h=27):
    """One-row KEY: items = [(swatch markup centred on 0,0, swatch half-width, label)]."""
    o = [f'<rect x="8" y="{y}" width="{w - 16}" height="{h}" rx="8" fill="#fff" stroke="#D9CBD2" stroke-width="1.2"/>',
         T(20, y + h / 2 + 3.7, "KEY", 10.4, 800, INK, ls=1.3)]
    start = 58
    widths = [2 * hw + 7 + tw(lab, 10.6, 600) for _, hw, lab in items]
    space = (w - 24 - start - sum(widths)) / (len(items) - 1)
    if space < 10:
        raise ValueError("thyroid sheet: KEY strip too crowded")
    x = start
    for (sw, hw, lab), wd in zip(items, widths):
        o.append(f'<g transform="translate({x + hw:.1f},{y + h / 2:.1f})">{sw}</g>')
        o.append(T(round(x + 2 * hw + 7, 1), y + h / 2 + 3.8, lab, 10.6, 600, INK))
        x += wd + space
    return "".join(o)


def key1(y, c1):
    sig = f'<path d="M-12,0 H6" stroke="{c1}" stroke-width="3"/><path d="M4,-5 L12,0 L4,5 Z" fill="{c1}"/>'
    fb = (f'<path d="M-12,0 H5" stroke="{FEED}" stroke-width="1.9" stroke-dasharray="4 3"/>'
          f'<path d="M4,-4.4 L12,0 L4,4.4 Z" fill="{FEED}"/>')
    return _key_strip(y, [(t4(0, 0), 5, "T4, the storage form"), (t3(0, 0), 5, "T3, the active form"),
                          (sig, 12, "Signal from the brain"), (fb, 12, "Feedback"),
                          (gear(0, 0, 11.2, "Se"), 12, "A nutrient that step needs")])


# ============================================================== picture 2: Hashimoto's, magnified
P2_HDR = 24
P2_H = 174
CR = 52
CIRC = [((68, 94), "HEALTHY", "#2F7D59"), ((206, 94), "HASHIMOTO&#8217;S", "#A5281E")]
FOLLICLES = [(-30, -30, 20), (12, -36, 17), (42, -8, 17), (-40, 10, 16), (-6, 4, 19), (28, 30, 18), (-20, 40, 15),
             (52, -40, 11), (-56, -14, 10), (6, 50, 9), (56, 30, 9), (-52, 40, 9)]


def _follicle(fx, fy, R, damaged=False, rnd=None):
    """Thyroid follicle: a ring of thyroid cells around stored hormone (colloid)."""
    tc = max(4.2, min(6.0, R * 0.36))
    o = [f'<circle cx="{fx:.1f}" cy="{fy:.1f}" r="{R:.1f}" fill="{CELL_F}" stroke="{CELL_LN}" stroke-width=".8"/>',
         f'<circle cx="{fx:.1f}" cy="{fy:.1f}" r="{R - tc:.1f}" fill="{COLLOID}" stroke="{COLLOID_LN}" stroke-width=".7"/>']
    n = max(6, int(2 * math.pi * R / 6.6))
    for i in range(n):
        a = 2 * math.pi * i / n + (rnd.uniform(-.05, .05) if rnd else 0)
        ca, sa = math.cos(a), math.sin(a)
        o.append(f'<path d="M{fx + (R - tc) * ca:.1f},{fy + (R - tc) * sa:.1f} L{fx + R * ca:.1f},{fy + R * sa:.1f}" '
                 'stroke="#F6C3BC" stroke-width=".8"/>')
        am, rm = a + math.pi / n, R - tc / 2
        o.append(f'<circle cx="{fx + rm * math.cos(am):.1f}" cy="{fy + rm * math.sin(am):.1f}" r="1.3" fill="#8E3043"/>')
    if damaged:     # a gap where thyroid cells were destroyed
        o.append(f'<path d="M{fx + R * .2:.1f},{fy - R * .98:.1f} A{R:.1f},{R:.1f} 0 0 1 {fx + R * .86:.1f},{fy - R * .5:.1f}" '
                 f'fill="none" stroke="{STROMA}" stroke-width="{tc + 1.8:.1f}"/>')
    return "".join(o)


def tissue(cx, cy, r, hashi, uid):
    rnd = random.Random(31 if hashi else 7)
    k = r / 62
    o = [f'<clipPath id="{uid}"><circle cx="{cx}" cy="{cy}" r="{r}"/></clipPath>',
         f'<g clip-path="url(#{uid})"><rect x="{cx - r}" y="{cy - r}" width="{2 * r}" height="{2 * r}" fill="{STROMA}"/>']
    fol = []
    for dx, dy, R in FOLLICLES:
        R *= k * (0.72 if hashi else 1.0)
        fol.append((cx + dx * k, cy + dy * k, R))
    for i, (fx, fy, R) in enumerate(fol):
        o.append(_follicle(fx, fy, R, damaged=hashi and i in (1, 3, 5), rnd=rnd))
    if hashi:
        # immune cells crowd the spaces between the shrunken follicles; antibodies tag the thyroid cells
        placed = []

        def free(x, y, rr):
            if math.hypot(x - cx, y - cy) > r - 1:
                return False
            if any(math.hypot(x - fx, y - fy) < R + rr + 0.7 for fx, fy, R in fol):
                return False
            return all(math.hypot(x - px, y - py) > rr * 2 + 0.5 for px, py in placed)
        for _ in range(6000):
            x, y = rnd.uniform(cx - r, cx + r), rnd.uniform(cy - r, cy + r)
            if free(x, y, 3.2):
                placed.append((x, y))
            if len(placed) >= 70:
                break
        for x, y in placed:
            o.append(lymphocyte(x, y, 3.2))
        for i in (0, 2, 4, 6):
            fx, fy, R = fol[i]
            for a in (rnd.uniform(0, 6.28) for _ in range(3)):
                ax, ay = fx + (R + 1.0) * math.cos(a), fy + (R + 1.0) * math.sin(a)
                o.append(antibody(ax, ay, math.degrees(a) + 90, 0.9))
    o.append("</g>")
    o.append(f'<circle cx="{cx}" cy="{cy}" r="{r + 2.2}" fill="none" stroke="#fff" stroke-width="2.4"/>'
             f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="#5C4650" stroke-width="2"/>')
    return "".join(o)


def _key_follicle():
    return (f'<path d="M-8,4 A9,9 0 0 1 8,4" fill="none" stroke="{CELL_F}" stroke-width="5.4"/>'
            '<circle cx="-4.6" cy="-2.8" r="1.4" fill="#8E3043"/><circle cx="0" cy="-4.8" r="1.4" fill="#8E3043"/>'
            '<circle cx="4.6" cy="-2.8" r="1.4" fill="#8E3043"/>')


def picture2(t):
    c1 = t["c1"]
    o = ['<defs><marker id="thy-ah-red" viewBox="0 0 10 10" refX="6.4" refY="5" markerWidth="4" markerHeight="4" '
         'orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#A5281E"/></marker></defs>',
         _panel(P2_H, "HASHIMOTO&#8217;S: THE IMMUNE SYSTEM TURNS ON THE THYROID", "thyroid tissue, magnified", c1)]
    for i, ((cx, cy), lab, col) in enumerate(CIRC):
        o.append(tissue(cx, cy, CR, i == 1, f"thy-tc{i}"))
        w = tw(_plain(lab), 10.2, 800, 0.6) + 16
        o.append(f'<rect x="{cx - w / 2:.1f}" y="{cy + CR - 8:.1f}" width="{w:.1f}" height="16.5" rx="8.2" fill="{col}" '
                 'stroke="#fff" stroke-width="1.6"/>' + T(cx, cy + CR + 3.8, lab, 10.2, 800, "#fff", "middle", ls=0.6))
    ax0, ax1 = CIRC[0][0][0] + CR + 6, CIRC[1][0][0] - CR - 8
    o.append(f'<path d="M{ax0},{CIRC[0][0][1]} H{ax1}" stroke="#A5281E" stroke-width="2.4" marker-end="url(#thy-ah-red)"/>')
    # steps: [CATU14] lymphocytes infiltrate between follicles, cells atrophy, TPO / Tg antibodies; [HU17]
    # TPO (thyroid peroxidase) is the gland's hormone-making enzyme.  [SURKS04] on a routine panel a high
    # TSH with normal free T4 (mild disease) comes first; TPO antibodies often appear years earlier, but
    # only show if someone tests for them, so step 4 says "routine blood test".
    sx, sy, sw = 282, P2_HDR + 22, 286
    steps = ["Immune cells mistake the thyroid for a threat.",
             "They move in, and antibodies tag TPO, the gland&#8217;s hormone-making enzyme.",
             "Over months or years, the gland makes less hormone.",
             "The pituitary pushes harder, so TSH rises. On a routine blood test, this is usually the first sign."]
    y = sy
    for i, s in enumerate(steps):
        lines = _wrap(s, sw, 10.6, 500)
        o.append(badge(sx, y - 3.8, i + 1, "#A5281E", 7.4, 9.8))
        o.append(T(sx + 13, y, lines, 10.6, 500, INK, lh=1.2))
        y += 12.7 * len(lines) + 5.6
    # [HU17] [TENG06]: high iodine intake is linked to Hashimoto's.  The nutrients are framed as what the
    # gland and immune cells need ([KNEZ20]: iron for hormone synthesis, selenium for T4 -> T3 and gland
    # protection, vitamin D helps regulate the immune response), not as causes, so the back's columns do
    # not read as a disease claim.
    ly = y + 2
    o.append(f'<rect x="{sx - 10}" y="{ly - 11}" width="{sw + 22}" height="31" rx="7" fill="#FFF7E2" stroke="#E9C979" stroke-width="1"/>')
    l1 = fit("<tspan font-weight='800'>Linked to Hashimoto&#8217;s:</tspan> too much iodine. Your thyroid", 10.2, 500,
             sw + 6, "linked")
    l2 = fit("relies on selenium and iron; immune cells rely on vitamin D.", 10.2, 500, sw + 6, "linked")
    o.append(T(sx - 2, ly + 1.6, l1, 10.2, 500, "#5A4300") + T(sx - 2, ly + 14, l2, 10.2, 500, "#5A4300"))
    if ly + 20 > P2_H - 6:
        raise ValueError("thyroid sheet: Hashimoto steps run past the panel")
    # KEY and the usual treatment, right column
    kx, kw = 590, 162
    items = [(f'<g transform="scale(.9)">{_key_follicle()}</g>', "Thyroid cells"),
             (f'<circle r="6" fill="{COLLOID}" stroke="{COLLOID_LN}" stroke-width=".8"/>', "Stored hormone"),
             (lymphocyte(0, 0, 4.2), "Immune cell"),
             (antibody(0, -1, 0, 1.2), "TPO antibody")]
    ky = P2_HDR + 6
    kh = 21 + 16 * len(items)
    o.append(f'<rect x="{kx}" y="{ky}" width="{kw}" height="{kh}" rx="8" fill="#fff" stroke="#D9CBD2" stroke-width="1.2"/>'
             + T(kx + 12, ky + 15, "KEY", 10.4, 800, INK, ls=1.3))
    for i, (swatch, lab) in enumerate(items):
        yy = ky + 30 + i * 16
        o.append(f'<g transform="translate({kx + 20},{yy - 3.6})">{swatch}</g>' + T(kx + 36, yy, lab, 10.4, 600, INK))
    # [ATA14] levothyroxine is the standard of care; [CATU14] synthetic thyroid hormone corrects the shortfall
    ty = ky + kh + 5
    tl = _wrap("Levothyroxine pills replace the missing hormone.", kw - 20, 10.2, 500)
    o.append(f'<rect x="{kx}" y="{ty}" width="{kw}" height="{P2_H - 8 - ty}" rx="8" fill="#EAF5EE" stroke="#9CCBB0" stroke-width="1"/>'
             + T(kx + 10, ty + 13, "USUAL TREATMENT", 9.8, 800, "#1F6B47", ls=0.8)
             + T(kx + 10, ty + 25.5, tl, 10.2, 500, "#1F4D36", lh=1.17))
    if ty + 25.5 + 11.95 * (len(tl) - 1) > P2_H - 12:
        raise ValueError("thyroid sheet: treatment text runs past the panel")
    return svg(W, P2_H, "".join(o),
               "Magnified thyroid tissue. Healthy: round follicles, rings of thyroid cells around stored hormone. "
               "Hashimoto's: immune cells crowd between smaller follicles and TPO antibodies tag the thyroid cells.")


# ============================================================== blocks under the art (HTML)
def _ico(name, px, sw=2.9):
    return (f'<svg viewBox="0 0 64 64" style="width:{px};height:{px}" fill="none" stroke="currentColor" '
            f'stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICONS[name]}</svg>')


# [NIDDK] symptom list
SIGNS = [("battery", "Tired, low<br>energy"), ("thermo", "Always<br>cold"), ("scale", "Weight<br>gain"),
         ("hair", "Dry skin,<br>thinning hair"), ("gut", "Constipation"), ("brain", "Foggy thinking,<br>low mood"),
         ("calendar", "Heavy or<br>irregular periods"), ("heartpulse", "Slow<br>heartbeat")]


def signs_block():
    cells = "".join(f'<div class="thy-sg"><span class="thy-disc">{_ico(ic, "0.27in")}</span><span>{lab}</span></div>'
                    for ic, lab in SIGNS)
    # [WYNE22] about 9.6% (NHANES 2009-12) to 11.7% (2019 claims) of the U.S., counting people already treated
    # (the older 1 in 20 is [HOLL02], NHANES III 1988-94); [NIDDK] [CATU14] it develops slowly, over years;
    # [NIDDK] higher-risk groups; [ATA] women 5 to 8 times; [KOTW20] [NIDDK] a slow thyroid raises cholesterol
    return ('<div class="thy-signs"><div class="thy-sh"><b>Signs of an underactive thyroid</b>'
            '<span>They creep in slowly. About 1 in 10 Americans has it, counting those already treated.</span></div>'
            f'<div class="thy-sgrow">{cells}</div>'
            '<p class="thy-risk"><b>Higher risk:</b> women (5 to 8 times more likely than men), age 60 or older, a family '
            'history, type 1 diabetes, celiac or another autoimmune disease, a baby in the past 6 months, past thyroid '
            'surgery, radioactive iodine or neck radiation. <b>It can also</b> raise cholesterol.</p></div>')


def numbers_block():
    # [SURKS04] TSH reference range 0.45 to 4.5 mIU/L; high TSH with normal free T4 = mild (subclinical)
    tsh = ('<div class="thy-tsh"><h4>TSH <span>the &#8220;make more&#8221; signal, mIU/L</span></h4>'
           '<div class="thy-tl"><div class="thy-t lo"><i>Below 0.45</i><em>may be overactive, or too much medicine</em></div>'
           '<div class="thy-t ok"><i>0.45 to 4.5</i><em>a common normal range; your lab&#8217;s may differ a little</em></div>'
           '<div class="thy-t hi"><i>Above 4.5</i><em>may be underactive: the brain pushes harder</em></div>'
           '<div class="thy-mine"><span>My result</span></div></div></div>')
    # [CATU14] TPO antibodies mark Hashimoto's; [HU17] check iron (ferritin) and vitamin D.
    # Low cut-offs: [BSG21] ferritin under 30 ng/mL "generally indicative of low body iron stores";
    # [IOM11] [ODS] 25-hydroxy vitamin D under 20 ng/mL is below what 97.5% of people need.
    boxes = [("Free T4", "the main thyroid hormone", ""), ("TPO antibodies", "positive: a sign of Hashimoto&#8217;s", ""),
             ("Ferritin", "your iron stores", "low: under 30 ng/mL"),
             ("Vitamin D", "25-hydroxy vitamin D", "low: under 20 ng/mL")]
    cells = "".join(f'<div class="thy-bx"><div><b>{a}</b><span>{b}</span>'
                    + (f'<span class="thy-low">{c}</span>' if c else "") + '</div><i></i></div>' for a, b, c in boxes)
    # [LI17] biotin makes thyroid immunoassays read falsely high or low; stop window per FDA / ATA advice.
    # [ND-LABEL] Essential Multi (the Start-here pick on the back) has 500 mcg biotin per 3 capsules.
    biotin = ('<div class="thy-bio"><b>Before any thyroid blood test</b><span>Stop <strong>biotin</strong> 2 to 3 days '
              'ahead, Essential Multi too. Many multis and hair, skin and nail formulas have it. It can make results '
              'look falsely high or low.</span></div>')
    # Edition-neutral on purpose: results go back to whoever ordered the test, not to the pharmacist.
    return ('<div class="thy-nums"><div class="thy-nh"><b>Know your numbers</b><span>Write your results in the boxes, '
            'then go over them with the provider who ordered them.</span></div>'
            f'<div class="thy-ngrid">{tsh}{biotin}<div class="thy-bxs">{cells}</div></div>'
            '<p class="thy-src">Sources: NIDDK; American Thyroid Association; Surks, JAMA 2004; Wyne, J Endocr Soc 2022; '
            'Hu and Rayman, Thyroid 2017; Li, JAMA 2017; IOM 2011; BSG 2021; Kotwal, JCEM 2020.</p></div>')


def front(t, ed):
    return ('<div class="thy">'
            f'<div class="thy-art">{picture1(t)}</div>'
            f'<div class="thy-art thy-art2">{picture2(t)}</div>'
            f'{signs_block()}{numbers_block()}</div>')


CSS = r"""
.thy .thy-art svg{display:block;width:100%;height:auto}
.thy .thy-art2{margin-top:0.06in}
.thy .thy-signs{margin-top:0.06in}
.thy .thy-sh{display:flex;align-items:baseline;gap:0.12in;margin:0 0 0.035in}
.thy .thy-sh b{flex:none;font:900 10.4pt Merriweather,Georgia,serif;color:var(--c1)}
.thy .thy-sh span{font-size:7.8pt;color:#4A555C}
.thy .thy-sgrow{display:grid;grid-template-columns:repeat(8,1fr);gap:0 0.04in}
.thy .thy-sg{display:flex;flex-direction:column;align-items:center;text-align:center}
.thy .thy-disc{flex:none;width:0.36in;height:0.36in;border-radius:50%;background:var(--soft);color:var(--c1);display:flex;
  align-items:center;justify-content:center;box-shadow:inset 0 0 0 1.5px rgba(155,63,104,.12)}
.thy .thy-sg>span:last-child{font-size:7.4pt;font-weight:600;line-height:1.18;color:#2F373C;margin-top:0.025in}
.thy .thy-risk{margin:0.045in 0 0;font-size:7.6pt;line-height:1.3;color:#2F373C;background:var(--tint);border-radius:6px;
  padding:0.03in 0.1in;border-left:3px solid var(--c2)}
.thy .thy-risk b{color:var(--deep)}
.thy .thy-nums{margin-top:0.06in;border:1px solid #E7D3DC;border-radius:10px;padding:0.05in 0.11in 0.04in;background:#fff}
.thy .thy-nh{display:flex;align-items:baseline;gap:10px;margin:0 0 3px}
.thy .thy-nh b{font:900 11pt Merriweather,Georgia,serif;color:var(--c1)}
.thy .thy-nh span{font-size:7.8pt;color:#56626A}
.thy .thy-ngrid{display:grid;grid-template-columns:1.9fr 1fr;gap:5px 0.12in;align-items:stretch}
.thy .thy-tsh h4{margin:0 0 3px;font:800 8.4pt Inter,sans-serif;color:#2B3236;white-space:nowrap}
.thy .thy-tsh h4 span{font-weight:500;font-size:7.2pt;color:#5E686F}
.thy .thy-tl{display:grid;grid-template-columns:1fr 1fr 1fr 0.56in;gap:4px}
.thy .thy-t{border-radius:5px;padding:2px 3px 3px;text-align:center;border-top:3px solid}
.thy .thy-t i{display:block;font:800 8.2pt/1.2 Inter,sans-serif;font-style:normal;white-space:nowrap}
.thy .thy-t em{display:block;font-style:normal;font-size:7pt;line-height:1.18;margin-top:1px}
.thy .thy-t.ok{background:#E4F2EA;color:#1F6B47;border-color:#2F8A5E}
.thy .thy-t.lo{background:#E6EEF8;color:#22508A;border-color:#3A78C2}
.thy .thy-t.hi{background:#F8E1DD;color:#9A2620;border-color:#C2392E}
.thy .thy-mine{border:1.3px dashed #9AA5AC;border-radius:5px;display:flex;align-items:flex-start;justify-content:center}
.thy .thy-mine span{font:700 7pt Inter,sans-serif;color:#6A747B;margin-top:2px;text-align:center}
.thy .thy-bxs{grid-column:1/-1;display:grid;grid-template-columns:repeat(4,1fr);gap:5px}
.thy .thy-bx{display:flex;align-items:center;justify-content:space-between;gap:4px;background:var(--tint);
  border:1px solid #EEDDE5;border-radius:6px;padding:2px 4px 2px 6px}
.thy .thy-bx b{display:block;font:800 7.6pt/1.15 Inter,sans-serif;color:#2B3236;white-space:nowrap}
.thy .thy-bx span{display:block;font-size:7pt;line-height:1.15;color:#4A555C}
.thy .thy-bx span.thy-low{font-weight:700;color:var(--deep)}
.thy .thy-bx i{flex:none;width:0.5in;height:0.28in;border-radius:4px;background:#fff;border:1.2px dashed #9AA5AC}
.thy .thy-bio{background:#F6ECD6;border:1px solid #E3C88C;border-radius:7px;padding:3px 7px 4px;color:#5A3B00}
.thy .thy-bio b{display:block;font:800 7.2pt/1.2 Inter,sans-serif;color:#814800;text-transform:uppercase;letter-spacing:.05em}
.thy .thy-bio span{display:block;font-size:7.4pt;line-height:1.26;margin-top:1px}
.thy .thy-bio strong{color:#814800}
.thy .thy-src{margin:3px 0 0;font-size:7pt;color:#5E686F;line-height:1.3}
/* back page: scoped with :has() to the marker span in this sheet's lifestyle title.  (The kit now sets
   every back-page text run, footer and disclaimer at 7 pt or more, so no size overrides are needed.) */
.sheet.back:has(.thy-back) .col .need{height:0.5in;min-height:0.5in}
.sheet.back:has(.thy-back) .life b{font-size:9.2pt}
/* the kit has no rule for class="x": draw this sheet's "avoid" slash in NutriDyn coral */
.sheet.back:has(.thy-back) .life svg .x{stroke:#F15F3F}
"""

# ============================================================== lifestyle icon (registered under a thy_ prefix)
# A dropper bottle (iodine drops) with a drop on its label and a coral "avoid" slash (CSS rule above):
# skip high-dose iodine unless prescribed.
ICONS.setdefault("thy_drops", '<path d="M27.5 15v-4.5a4.5 4.5 0 0 1 9 0V15"/><rect x="24" y="15" width="16" height="7" rx="2"/>'
                              '<path d="M26 22v3.5l-5 5V52a5 5 0 0 0 5 5h12a5 5 0 0 0 5-5V30.5l-5-5V22"/>'
                              '<path d="M32 35.5c-3.2 4.2-4.8 6.6-4.8 8.8a4.8 4.8 0 0 0 9.6 0c0-2.2-1.6-4.6-4.8-8.8z"/>'
                              '<path class="x" d="M9 57 55 11"/>')

# ============================================================== the sheet
SHEET = {
    "slug": SLUG, "code": "ND-HM-502", "order": 19, "theme": "hormone", "series": "Hormone Health Series",
    "title": "Thyroid Health", "sub": "Underactive thyroid and Hashimoto&#8217;s",
    # [NIDDK] Hashimoto's is the most common cause in the U.S. ([HUW24]: in iodine-sufficient areas).
    "intro": ("Your <b>thyroid</b>, a butterfly-shaped gland in your neck, sets the pace of nearly every cell. Too little "
              "hormone slows the body down: an <b>underactive thyroid</b> (hypothyroidism). In the U.S. the usual cause is "
              "<b>Hashimoto&#8217;s</b>, an immune attack on the gland."),
    "front": front,
    "css": CSS,
    "back": {
        # the empty span lets this sheet's CSS reach its own back page (see CSS)
        "life_title": 'Lifestyle Recommendations<span class="thy-back"></span>',
        "style": "hex",
        "life": [
            # [ODS] food sources: seafood, meat, eggs, beans, nuts and seeds bring selenium, zinc and iron
            ("plate", "Whole-food plate", "Fish, eggs, beans, nuts and seeds bring selenium, zinc and iron."),
            # [PEAR13] the U.S. is generally iodine-sufficient; [TENG06] [HU17] [ATA15] high or excess iodine can
            # harm.  150 mcg is the adult RDA [ODS], the amount in Essential Multi [ND-LABEL], so the tile and the
            # Start-here pick agree.
            ("thy_drops", "No high-dose iodine", "Skip kelp and iodine drops. Iodized salt or a basic multi (150 mcg) is plenty."),
            # Physical Activity Guidelines for Americans, 2nd ed. (HHS 2018)
            ("walk", "Move every day", "Walk most days. Add strength work 2 to 3 days a week."),
            # [NSF15] National Sleep Foundation 2015: 7 to 9 hours for adults (7 to 8 at 65+)
            ("moon", "Sleep 7 to 9 hours", "Steady sleep helps energy, mood and weight."),
            # [ROY16] about 1 in 62 people with autoimmune thyroid disease has celiac disease; test while eating gluten
            ("wheat", "Ask about celiac", "More common with thyroid disease. Test before you cut gluten."),
            # [ATA14] take levothyroxine the same way every day; [LT4-PI]
            ("clock", "Same time daily", "Take thyroid medicine the same way each day, with water only."),
        ],
        "cols": [
            {"p": "thy_essential_multi", "need": "Thyroid nutrient base", "needsub": "selenium, zinc and more",
             "start": True,
             # [HUW24] [ZHANG25] selenium; [HU17] 50-100 mcg selenium a day where intake is low; [KNEZ20] zinc for
             # T4 to T3; 150 mcg iodine = the adult RDA, not a high dose ([ATA15] warns about high doses)
             "bullets": ["Selenium and zinc support healthy thyroid function",
                         "Iodine at a normal daily amount (150 mcg), not a high dose"],
             "dose": "3 capsules with dinner", "dosesub": "4 hours after thyroid medicine", "sched": [("pm", 3, "capsules")]},
            {"p": "thy_d3_5000_k2", "need": "Vitamin D", "needsub": "only if your level is low",
             # [HU17] check vitamin D and correct a deficiency; [WANG18]; [KNEZ20] vitamin D and immune regulation
             "bullets": ["Supports healthy immune function", "K2 helps put calcium to work in bone"],
             "dose": "1 softgel with dinner", "dosesub": "recheck your vitamin D level",
             "sched": [("pm", 1, "softgel, if vitamin D is low")]},
            {"p": "thy_iron_support", "need": "Iron", "needsub": "only if ferritin is low",
             # [HU17] TPO is a heme (iron) enzyme; Hashimoto's patients are often iron deficient; check and correct
             "bullets": ["Supports healthy iron levels and energy", "TPO, the thyroid&#8217;s hormone-making enzyme, needs iron"],
             "dose": "1 capsule at bedtime", "dosesub": "4 hours from thyroid medicine",
             "sched": [("bed", 1, "capsule, if ferritin is low")]},
            {"p": "thy_ultrabiotic_dms", "need": "Gut balance", "needsub": "the gut-thyroid link",
             # [KNEZ20] the thyroid-gut axis (gut microbes take part in thyroid hormone and mineral handling);
             # constipation is one of the front's signs [NIDDK]; label directions one capsule daily [ND-LABEL]
             "bullets": ["Supports a healthy gut microbiome", "Supports regular, comfortable digestion"],
             "dose": "1 capsule with breakfast", "dosesub": "", "sched": [("am", 1, "capsule")]},
            {"p": "thy_omega_1000", "need": "Omega-3s", "needsub": "for heart health",
             # front: a slow thyroid can raise cholesterol [KOTW20]; EPA/DHA and triglycerides, structure/function
             # wording only (no thyroid-population claim on the back)
             "bullets": ["Supports a healthy inflammatory response", "Supports heart health and healthy triglycerides"],
             "dose": "1 softgel with dinner", "dosesub": "", "sched": [("pm", 1, "softgel")]},
        ],
        "rx": {
            "pharmacy": [
                # [LT4-PI] empty stomach, half to one hour before breakfast, 4 hours from binders; [ATA14] bedtime dosing
                # is also accepted, and then the iron / multi times shift
                "<b>Thyroid medicine first, alone:</b> water only, empty stomach, 30 to 60 minutes before breakfast. "
                "Iron, calcium, magnesium, antacids and multis 4 hours later. Take it at bedtime? Ask {who} to re-time "
                "the iron and multi.",
                # [LI17] biotin interference; FDA biotin safety communication; [ND-LABEL] Essential Multi 500 mcg biotin
                "<b>Biotin skews thyroid labs.</b> It is in many hair, skin and nail formulas and multivitamins, "
                "Essential Multi too. Stop it 2 to 3 days before a blood test.",
                # [HU17] check and correct low levels; [ODS] vitamin D UL 4,000 IU; [ND-LABEL] D3 5000 label: exceeds the
                # UL, monitor levels; K2 not recommended with blood thinners.  5,000 + 1,000 (Essential Multi) = 6,000 IU
                "<b>D3 5000 and Iron Support are for low lab levels.</b> D3 5000 plus the multi is 6,000 IU a day, above "
                "the 4,000 IU upper limit, so recheck your level. On a blood thinner? Skip the K2 formula.",
                # [KANG13] thyroid supplements with T4/T3; [TENG06] [ATA15] iodine; never self-adjust
                "<b>Never change your thyroid dose on your own.</b> Skip kelp and iodine drops with Hashimoto&#8217;s. "
                "Glandular thyroid products can hold real hormone: use them only if your prescriber says so.",
            ],
            "practitioner": [
                # [HU17] check iron and vitamin D; [ODS] vitamin D UL 4,000 IU; [ND-LABEL] D3 label warnings; the
                # multi adds 1,000 IU, so the plan totals 6,000 IU
                "<b>Test first:</b> TSH, free T4, TPO antibodies, ferritin, vitamin D. Iron Support and D3 5000 are for "
                "low levels. With Essential Multi&#8217;s 1,000 IU that is 6,000 IU a day, above the 4,000 IU upper limit, "
                "so recheck. K2 is not for people on blood thinners.",
                # [LT4-PI] [ATA14] (bedtime dosing accepted); [LI17]; [ND-LABEL] biotin 500 mcg in Essential Multi
                "<b>Thyroid medicine alone:</b> water, empty stomach, 30 to 60 minutes before breakfast; minerals and "
                "multis 4 hours later. Taken at bedtime? Ask {who} to re-time the iron and multi. Stop biotin, Essential "
                "Multi too, 2 to 3 days before labs.",
                # [KANG13] [TENG06] [ATA15]
                "<b>Never change thyroid medicine without {who}.</b> Skip kelp and iodine drops with Hashimoto&#8217;s. "
                "Glandular thyroid products can hold active hormone: use them only under {who}&#8217;s care.",
            ],
        },
    },
}
