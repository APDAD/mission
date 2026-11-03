"""Menopause and Perimenopause (ND-HM-501), Hormone Health Series.  Slug "menopause".

Self-contained sheet module (no legacy / sheets.py / art.py drawing code).
FRONT, top to bottom:
  intro -> "One woman, every system": a standing woman drawn from mirrored splines (so she is
  exactly symmetric), with the parts each system note points to: hair, breasts, heart, liver,
  stomach and bowel, ovaries and uterus, bladder, pelvis and hip, thigh muscles.  A gold dot marks
  each place a change can show up; a magnified circle shows the hypothalamus (the thermostat).
  -> "Why hot flashes happen" (the comfort zone that narrows) beside "How your hormones change"
  (grey stage bands, a pink estrogen line that swings then falls, a purple dashed progesterone line
  that falls first, plus the hot-flash and fast-bone-loss windows) -> one KEY for every symbol.
  -> "Track your symptoms" (the 12 Menopause Map questions, 0 to 3) beside "Hot flashes: what works
  best" (hormone therapy first, said plainly) -> a "see your provider soon" strip.
BACK: lifestyle circles, five NutriDyn picks (one per system), daily rhythm, an edition check.
Every SVG id starts with "mnp-" and every CSS class with "mnp-", so nothing collides with other
sheets in the all-sheets bundle.  Edition wording: "{who}" / "{Who}" (build.ed_text).

SOURCES (tags sit in comments next to each number or claim on the page)
  [GOLD11]   Gold EB. Obstet Gynecol Clin North Am 2011;38:425-40. doi:10.1016/j.ogc.2011.05.002
             (median age at menopause 50 to 52; perimenopause onset 47.5; smokers 1-2 years earlier)
  [PARAM17]  Paramsothy P et al. Menopause 2017;24:142-9. doi:10.1097/GME.0000000000000736 (SWAN:
             median length of the transition 4.4 to 8.6 years, longer when it starts earlier)
  [SANT96]   Santoro N et al. J Clin Endocrinol Metab 1996;81:1495-501. doi:10.1210/jcem.81.4.8636357
             (perimenopause: estrogen often HIGHER than before, luteal progesterone LOWER)
  [SANT16]   Santoro N. J Womens Health 2016;25:332-9. doi:10.1089/jwh.2015.5556 (hot flashes in most
             women; sleep, mood and anxiety worsen across the transition; vaginal dryness and painful
             sex affect about 1 in 3 and do not go away without treatment)
  [FREE99]   Freedman RR, Krell W. Am J Obstet Gynecol 1999;181:66-70. doi:10.1016/s0002-9378(99)70437-0
             and Freedman RR. Curr Top Behav Neurosci 2014;21:245-56. doi:10.1007/7854_2014_325 (hot
             flashes = small core-temperature rises acting inside a greatly narrowed thermoneutral zone
             between the sweating and shivering thresholds)
  [AVIS15]   Avis NE et al. JAMA Intern Med 2015;175:531-9. doi:10.1001/jamainternmed.2014.8063 (SWAN:
             frequent hot flashes last a median 7.4 years, a median 4.5 years past the final period)
  [GREEN12]  Greendale GA et al. J Bone Miner Res 2012;27:111-8. doi:10.1002/jbmr.534 (SWAN: bone loss
             is fastest from 1 year before to 2 years after the final period, at spine and hip)
  [GREEN19]  Greendale GA et al. JCI Insight 2019;4:e124865. doi:10.1172/jci.insight.124865 (fat gain
             doubles and lean mass starts to fall at the start of the transition)
  [AHA20]    El Khoudary SR et al. Circulation 2020;142:e506-32. doi:10.1161/CIR.0000000000000912
             (the transition is a time of accelerating heart risk: lipids, belly fat, vessel health)
  [PETERS22] Peters BA et al. mSystems 2022;7:e0027322. doi:10.1128/msystems.00273-22 (the gut
             microbiome shifts after menopause)
  [THORN13]  Thornton MJ. Dermatoendocrinol 2013;5:264-70. doi:10.4161/derm.23872 (less estrogen:
             thinner, drier skin with less collagen; hair loss)
  [GSM20]    NAMS 2020 GSM position statement. Menopause 2020;27:976-92. doi:10.1097/GME.0000000000001609
             (genitourinary syndrome of menopause affects 27-84% of women after menopause; treatable)
  [HT22]     NAMS 2022 hormone therapy position statement. Menopause 2022;29:767-94.
             doi:10.1097/GME.0000000000002028 (most effective treatment for hot flashes and GSM; prevents
             bone loss; benefit-risk favorable under 60 or within 10 years of menopause, no
             contraindications)
  [NH23]     NAMS 2023 nonhormone position statement. Menopause 2023;30:573-90.
             doi:10.1097/GME.0000000000002200 (recommended: CBT, clinical hypnosis, SSRIs/SNRIs,
             gabapentin, fezolinetant, oxybutynin, weight loss, stellate ganglion block.  NOT
             recommended for hot flashes: supplements/herbal remedies, cooling, avoiding triggers,
             exercise, yoga, soy, acupuncture.  Hormone therapy remains the most effective treatment.)
  [ESTRO]    EstroG-100 trials.  Snigdha S et al. Menopause 2025;32:1036-45.
             doi:10.1097/GME.0000000000002608 (n=80, EstroG-100 514 mg + GABA 50 mg, 5 weeks; authors
             from OLLY PBC / Unilever, the maker of the tested product: industry funded).  Chang A et
             al. Phytother Res 2012;26:510-6. doi:10.1002/ptr.3597 (n=64, 12 weeks).  Farzaneh F et al.
             Explore 2024;20:334-9. doi:10.1016/j.explore.2023.09.004 (120 randomized, 70 analyzed).
  [ASHW24]   Arumugam V et al. Explore 2024;20:103062. doi:10.1016/j.explore.2024.103062 (9 RCTs:
             ashwagandha lowered perceived stress, anxiety and serum cortisol)
  [CREA26]   Naddafha S et al. J Int Soc Sports Nutr 2026;23:2668435. doi:10.1080/15502783.2026.2668435
             (7 RCTs after menopause: +7.5 kg leg press, +0.37 kg lean mass at >=5 g/day with
             training; bone density unchanged; kidney markers unchanged)
  [MAP]      Asher's "Menopause Map" protocol artifact: 12 symptom questions scored 0-3 (total /36),
             retest at 6 weeks; PeriMenopause Support within a year of the last period, Menopause
             Support after; D3 5000 with K2 for everyone; UltraBiotic Women's for dryness or UTIs.
  [ACOG]     ACOG Committee Opinion 734 (2018): any bleeding after menopause needs evaluation.  ACOG
             patient guidance: bleeding more often than every 3 weeks, or heavier and longer than
             usual, needs a check.  Menopause before 40 is premature and needs a work-up (NAMS).
"""
import math
import os

from kit import ICONS
from svgkit import T, svg

SLUG = "menopause"

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
    """Advance width of `text` in Inter at `size` px (falls back to a generous guess)."""
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


# ============================================================== palette (every symbol is in a KEY)
INK, INK2 = "#2B3236", "#56616A"
SKIN, SKIN_EDGE, SKIN_LN = "#F7E4DA", "#EFD0C3", "#C4968A"
HAIR_A, HAIR_B, HAIR_LN = "#6E4C3E", "#4C3329", "#3A261E"
GOLD, GOLD_LN = "#F2B632", "#8A5A00"          # gold dot: where a change can show up
LEAD = "#6F5F66"                              # leader lines
BONE, BONE_LN = "#F5EDDA", "#BFA57B"
MUSCLE, MUSCLE_LN = "#E39A8D", "#C47263"
UTER, UTER_LN = "#E3869C", "#A9506A"
OVARY, OVARY_LN = "#F6CBD5", "#BE6F86"
BLADDER, BLADDER_LN = "#F2DCA8", "#BE9852"
GUT_S, GUT_S_LN = "#F3C3AF", "#CF8C74"        # small intestine
GUT_L, GUT_L_LN = "#E7A48D", "#B56E59"        # large intestine
LIVER_A, LIVER_B = "#D58F78", "#B8644F"
STOM, STOM_LN = "#EDAA94", "#BE7862"
HEART_A, HEART_B = "#DC4E56", "#A3232D"
HYPO = "#EF7A3A"                              # hypothalamus (the thermostat), named in the art
E_LINE = "#E0457E"                            # estrogen: pink line
P_LINE = "#6B4FA8"                            # progesterone: purple dashed line
STAGE_A, STAGE_B = "#F1EFF2", "#E4E1E6"       # grey bands: life stages
ZONE, ZONE_LN = "#D3EBDA", "#5E9C72"          # comfort zone (green band)
SWEAT, SHIVER = "#D5573B", "#3F78BD"          # sweat line / shiver line
HEAT = "#3B4650"                              # body heat line
FLASH, FLASH_LN = "#F07A3A", "#B8501E"        # hot flash burst
HOTWIN, BONEWIN = "#E2A31B", "#A8875A"        # hot-flash window / fast-bone-loss window


# ============================================================== geometry helpers
def _spline(pts, closed=True):
    """Catmull-Rom curve through pts [(x, y) or (x, y, tension)] as cubic Bezier path data.
    Low tension (0.2-0.4) gives a near-sharp corner at that point."""
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


def _ic(name_or_body, cx, cy, size, color, sw=4.2):
    """A 64-grid line icon centred on (cx, cy), drawn inside an SVG."""
    body = ICONS.get(name_or_body, name_or_body)
    s = size / 64
    return (f'<g transform="translate({cx - size / 2:.1f},{cy - size / 2:.1f}) scale({s:.4f})" fill="none" '
            f'stroke="{color}" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round">{body}</g>')


# this sheet's own icons (64 grid, same stroke style as kit.ICONS)
IC_RIBBON = ('<path d="M24 56 39 31c4-7 5-13 1-18-2-3-5-4-8-4s-6 1-8 4c-4 5-3 11 1 18l15 25"/>'
             '<path d="M27 25c2-4 8-4 10 0"/>')
IC_UTERUS = ('<path d="M22 22c0 11 5 17 7 21v11h6V43c2-4 7-10 7-21 0-5-20-5-20 0z"/>'
             '<path d="M22 22c-5-6-11-6-14-1M42 22c5-6 11-6 14-1"/>'
             '<circle cx="9" cy="29" r="4.5"/><circle cx="55" cy="29" r="4.5"/>')
IC_BLADDER = ('<path d="M32 10c-10 0-19 9-19 21 0 9 6 15 13 17v6h12v-6c7-2 13-8 13-17 0-12-9-21-19-21z"/>'
              '<path d="M24 30c0 5 3 8 8 9"/>')


# ============================================================== the figure (local units, head = 80)
# Female proportions, front view, 7.5 heads tall (shown to mid-thigh): chin 1.0 head, shoulders 1.45,
# bust 2.1, waist 2.75, widest hip 3.5, crotch 3.95, mid-thigh 4.55.  Hips about as wide as the
# shoulders, waist about 0.65 of the hips.  Arms hang with a slight lift so the waist stays clear.
BODY_R = [(0, 64), (14.6, 66), (15.4, 78), (16.4, 89), (20.5, 96.5), (32, 101.5), (47.5, 106), (60, 110.5),
          (69.5, 116.5), (73, 126), (70.5, 136), (65, 145), (62.6, 157), (62.4, 168), (59.2, 181),
          (54.4, 194), (49.4, 208), (46.6, 220), (47.6, 233), (53.4, 248), (61.6, 263), (67.2, 279),
          (68.6, 294), (66.8, 312), (63.4, 338), (60.6, 368, 0.25), (10.5, 368, 0.25), (8.2, 346),
          (6.2, 331), (3.8, 322, 0.6), (0, 318.5)]
ARM_R = [(56, 112), (67.5, 110), (77.8, 116), (84.6, 126.5), (87.2, 143), (88.2, 165), (89.6, 188), (91.4, 208),
         (93.6, 232), (95.9, 258), (97.8, 282), (99.1, 295.5), (101.7, 307.5), (102.1, 322.5), (99.4, 335.6),
         (94.8, 342.4), (89.8, 340.8), (87.2, 331.5), (86, 316.5), (85.1, 300.5), (83.1, 284), (79.7, 258),
         (76.3, 232), (73.7, 210), (71.3, 188), (68.8, 168), (66.7, 152), (65.2, 141), (60, 127)]
HEAD_R = [(0, 0), (16.2, 2.6), (25.6, 11), (28.6, 25), (28.2, 39), (26.2, 51.2), (21.8, 62.2), (14.3, 72.2),
          (6.3, 78.6), (0, 80.2)]
HAIR_BACK_R = [(0, -5.8), (19.8, -3.1), (31.8, 7.4), (36.8, 23), (37.8, 40), (36.9, 56), (34.4, 68.5), (30.8, 77.2),
               (25, 81.2, 0.55), (19.2, 76.4), (17.2, 67), (0, 61)]
# side-swept fringe: parting at x = -8, hair sweeps to the viewer's right
HAIR_FRONT = [(-31.4, 25), (-31.8, 10.5), (-22.5, -1.6), (-6.5, -5.4), (10.5, -4.8), (24.6, 1.2), (33, 12.2), (33.4, 27),
              (27.4, 31.5), (22.6, 21), (12.6, 14.2), (1, 12.4), (-8, 14.2, 0.45), (-14.4, 16.6), (-22.4, 23.6),
              (-27, 33.2)]

BODY_D = _spline(_mirror(BODY_R))
ARM_RD, ARM_LD = _spline(ARM_R), _spline(_flip(ARM_R))
HEAD_D = _spline(_mirror(HEAD_R))
HAIR_BACK_D = _spline(_mirror(HAIR_BACK_R))
HAIR_FRONT_D = _spline(HAIR_FRONT)

# where each gold dot sits (local units)
DOT = {"hair": (31.5, 50), "breast": (-31, 169), "heart": (8, 158), "gut": (-9, 250), "ovary": (28.6, 275),
       "bladder": (8, 307), "hip": (-45, 287), "thigh": (-34, 338), "brain": (0, 41)}


def _pelvis():
    """Front view: iliac wings, sacrum, pubic ring with the two obturator holes, hip sockets,
    and both femurs (head, neck, greater trochanter, shaft angling toward the knee)."""
    o = []
    for s in (1, -1):
        wing = [(13 * s, 258), (20 * s, 249.5), (33 * s, 245.2), (46 * s, 246.4), (55 * s, 250.6), (59.6 * s, 258),
                (59 * s, 266.5), (54.8 * s, 274), (48.6 * s, 280), (41.5 * s, 285.5, 0.6), (33 * s, 281),
                (24.6 * s, 275.5), (17.4 * s, 270), (13.6 * s, 264)]
        ring = [(40.5 * s, 287), (35.6 * s, 293.4), (24.6 * s, 297.2), (8.4 * s, 299.6, 0.5), (4.2 * s, 302, 0.5),
                (4.4 * s, 309.6, 0.5), (9 * s, 312.4), (20 * s, 314), (31.5 * s, 312.4), (38.6 * s, 306),
                (42.6 * s, 296.5)]
        o.append(f'<path d="{_spline(wing)}" fill="{BONE}" stroke="{BONE_LN}" stroke-width=".9"/>')
        o.append(f'<path d="{_spline(ring)}" fill="{BONE}" stroke="{BONE_LN}" stroke-width=".9"/>')
        o.append(f'<ellipse cx="{21.5 * s}" cy="305.4" rx="8.6" ry="5.6" fill="{SKIN}" stroke="{BONE_LN}" '
                 f'stroke-width=".8" transform="rotate({-12 * s} {21.5 * s} 305.4)"/>')            # obturator hole
        o.append(f'<path d="M{47 * s - 4 * s},{276} A10.5,10.5 0 0 {1 if s > 0 else 0} {47 * s + 3 * s},{296.6}" '
                 f'fill="none" stroke="{BONE_LN}" stroke-width="1.3"/>')                        # hip-socket rim
        shaft = [(57.4 * s, 300), (58.2 * s, 318), (56.8 * s, 343), (52.8 * s, 369, 0.3), (43.4 * s, 369, 0.3),
                 (46.4 * s, 343), (48.6 * s, 318), (49.8 * s, 302)]
        o.append(f'<path d="{_spline(shaft)}" fill="{BONE}" stroke="{BONE_LN}" stroke-width=".9"/>')
        neck = [(45.2 * s, 280.5), (52.4 * s, 283.2), (59.6 * s, 286.4), (64 * s, 290.6), (64.6 * s, 297.2),
                (61.4 * s, 302.6), (55.4 * s, 303.2), (50.2 * s, 297.6), (45.6 * s, 294.2)]
        o.append(f'<path d="{_spline(neck)}" fill="{BONE}" stroke="{BONE_LN}" stroke-width=".9"/>')
        o.append(f'<circle cx="{46.2 * s}" cy="287.4" r="8.1" fill="{BONE}" stroke="{BONE_LN}" stroke-width=".9"/>')
    sac = [(-14.8, 253.6), (-5, 251.4), (5, 251.4), (14.8, 253.6), (13.2, 266), (7.4, 279), (0, 290, 0.5),
           (-7.4, 279), (-13.2, 266)]
    o.append(f'<path d="{_spline(sac)}" fill="#EFE4CB" stroke="{BONE_LN}" stroke-width=".9"/>')
    for y in (259, 267, 275):
        o.append(f'<circle cx="-5.2" cy="{y}" r="1.5" fill="{BONE_LN}" opacity=".45"/>'
                 f'<circle cx="5.2" cy="{y}" r="1.5" fill="{BONE_LN}" opacity=".45"/>')
    return "".join(o)


def _thigh_muscles():
    """Quadriceps on each thigh: vastus lateralis, rectus femoris, vastus medialis, fibre lines."""
    o = []
    for s in (1, -1):
        parts = [
            [(64.6 * s, 300), (65.6 * s, 322), (63.4 * s, 346), (60 * s, 370, 0.3), (50 * s, 370, 0.3),
             (53.6 * s, 346), (57 * s, 322), (58.2 * s, 302)],
            [(46 * s, 296.5), (49.6 * s, 316), (47.6 * s, 344), (40.4 * s, 370, 0.3), (28.6 * s, 370, 0.3),
             (33.2 * s, 344), (36.6 * s, 316), (38.4 * s, 298)],
            [(26.4 * s, 309), (28.8 * s, 330), (25.2 * s, 352), (18.8 * s, 370, 0.3), (11 * s, 370, 0.3),
             (13.2 * s, 350), (15.4 * s, 330), (16.4 * s, 314)],
        ]
        for p in parts:
            o.append(f'<path d="{_spline(p)}" fill="{MUSCLE}" fill-opacity=".5" stroke="{MUSCLE_LN}" '
                     f'stroke-width=".8" stroke-opacity=".7"/>')
        for x0, x1 in ((61 * s, 55 * s), (43 * s, 34.5 * s), (22 * s, 15 * s)):
            for k in (-2.4, 0, 2.4):
                o.append(f'<path d="M{x0 + k:.1f},{306} C{x0 + k + 1.2 * s:.1f},{328} {x1 + k + 1.6 * s:.1f},{346} '
                         f'{x1 + k - 1 * s:.1f},{368}" stroke="{MUSCLE_LN}" stroke-width=".55" fill="none" opacity=".55"/>')
    return "".join(o)


def _heart():
    """Front view: ventricles with the apex down and to her left, the aortic arch with its three
    branches, the superior vena cava (blue) and the pulmonary trunk (blue) in front."""
    body = [(-12.8, -6.5), (-13.6, 3), (-9.2, 11.4), (-1.6, 17.6), (6.4, 21.2), (11.6, 19.6), (14.6, 12),
            (14, 1), (10, -7.2), (3, -11), (-5.2, -10.6)]
    arch = "M0.5,-10 C-0.5,-21 7,-26 12.5,-21.5 C14.6,-19.6 15,-16 14.6,-12"
    return ('<g transform="translate(6,160)">'
            '<path d="M-7,-8 V-24" stroke="#3E4F8C" stroke-width="6.6" stroke-linecap="round"/>'
            '<path d="M-7,-8 V-24" stroke="#6F84C9" stroke-width="5" stroke-linecap="round"/>'
            + "".join(f'<path d="M{x},{y0} V{y1}" stroke="#7A1820" stroke-width="3.4" stroke-linecap="round"/>'
                      f'<path d="M{x},{y0} V{y1}" stroke="#C7363F" stroke-width="2" stroke-linecap="round"/>'
                      for x, y0, y1 in ((3.2, -21.5, -26.6), (6.8, -23.6, -28.4), (10.2, -23.2, -27.4)))
            + f'<path d="{arch}" fill="none" stroke="#7A1820" stroke-width="7" stroke-linecap="round"/>'
            f'<path d="{arch}" fill="none" stroke="#C7363F" stroke-width="5.4" stroke-linecap="round"/>'
            f'<path d="{_spline(body)}" fill="url(#mnp-heart)" stroke="#7A1820" stroke-width=".9"/>'
            '<path d="M3.6,-9.4 C5,-14 8.6,-16.4 13,-16.6" fill="none" stroke="#3E4F8C" stroke-width="6" stroke-linecap="round"/>'
            '<path d="M3.6,-9.4 C5,-14 8.6,-16.4 13,-16.6" fill="none" stroke="#6F84C9" stroke-width="4.4" stroke-linecap="round"/>'
            '<path d="M-2.6,-8.6 C1.4,0 5,9 8.6,19.4" fill="none" stroke="#8E1D25" stroke-width="1" opacity=".5"/>'
            '<ellipse cx="-6.6" cy="-2.6" rx="3.6" ry="2.2" fill="#fff" opacity=".22" transform="rotate(-30 -6.6 -2.6)"/>'
            '</g>')


def _breasts():
    o = []
    for s in (1, -1):
        o.append(f'<ellipse cx="{31 * s}" cy="171" rx="19.5" ry="17" fill="url(#mnp-breast)"/>')
        o.append(f'<path d="M{49.6 * s},{163} C{48.6 * s},{178} {41 * s},{187.6} {30.4 * s},{188.2} '
                 f'C{20.6 * s},{188.6} {13.6 * s},{182} {12.2 * s},{173.6}" fill="none" stroke="#C99383" '
                 'stroke-width="1.3" stroke-linecap="round"/>')
    return "".join(o)


def _abdomen():
    """Liver and stomach under the ribs, the large bowel framing the coiled small bowel."""
    liver = [(-58.4, 194), (-47, 185.4), (-24, 184.2), (-4, 187), (9, 189.2), (19.6, 193.6), (14.2, 199.6),
             (1.5, 205.6), (-12, 211.8), (-27, 218.4), (-42.4, 223.6), (-52.6, 221.6), (-58.4, 213)]
    stom = [(9.8, 190.6), (16.6, 184.6), (27, 183.2), (35.4, 187.2), (42.2, 196.6), (41.8, 208.8), (36.6, 220.6),
            (26.8, 227.4), (16, 227.6), (7.4, 224.8), (2, 220.2), (8.8, 217.6), (18.6, 215.2), (26.2, 210.6),
            (28.4, 202.6), (24.8, 196.4), (17.2, 196)]
    colon = ("M-36.4,271 C-40.2,262 -42.2,246 -41.4,233.4 C-40.8,225 -37.4,219.4 -31,218.4 "
             "C-18,220.4 -6.4,226.4 4,225.4 C16,224.4 28,218.4 37.2,215.2 C43.4,216.4 44.6,226.4 44.4,236.6 "
             "C44.2,248.4 44.4,256.4 42.2,262.6 C38.6,268.4 27.6,266.2 19.6,264.4 C13.8,263.2 9.8,265.4 7.4,268.8")
    small = ("M-23,238 C-17,233 -11,241 -5,237.5 C1,234 7,242 13,238 C18,235 22,236.5 24,241 "
             "C25.6,245.8 20.4,248.4 15,246.6 C9,244.4 3,250.6 -3,247.2 C-9,244 -15,250.6 -21,247.4 "
             "C-26.4,245.6 -28.6,251.6 -25,255 C-20.6,259 -14,253.6 -8,256.6 C-2,259.8 4,253.6 10,256.4 "
             "C15.6,259 20.6,254.6 24,257.6")
    return (f'<path d="{_spline(liver)}" fill="url(#mnp-liver)" stroke="#9A5240" stroke-width=".8" opacity=".9"/>'
            f'<path d="{_spline(stom)}" fill="{STOM}" stroke="{STOM_LN}" stroke-width=".9"/>'
            '<path d="M-29,233 C-31,226 -20,228.4 -6,231 C8,233.4 20,228.6 29,233 C34.6,236.4 34.2,252 31.4,258.4 '
            'C27.4,266.4 14,265.8 2,265 C-10,265.4 -23,266.4 -28.6,259.6 C-33,254 -31.4,241 -29,233 Z" '
            f'fill="{GUT_S}" stroke="{GUT_S_LN}" stroke-width=".8"/>'
            f'<path d="{small}" fill="none" stroke="{GUT_S_LN}" stroke-width="6.6" stroke-linecap="round" '
            'stroke-linejoin="round"/>'
            f'<path d="{small}" fill="none" stroke="#F7D3C4" stroke-width="4.6" stroke-linecap="round" '
            'stroke-linejoin="round"/>'
            f'<path d="{colon}" fill="none" stroke="{GUT_L_LN}" stroke-width="12.6" stroke-linecap="round"/>'
            f'<path d="{colon}" fill="none" stroke="{GUT_L}" stroke-width="10.6" stroke-linecap="round"/>'
            f'<path d="{colon}" fill="none" stroke="{GUT_L_LN}" stroke-width="10.6" stroke-dasharray="1.1 5.4" '
            'opacity=".55"/>')


def _pelvic_organs():
    """Uterus with tubes and ovaries; bladder in front of the cervix; the vagina below."""
    o = ['<rect x="-3.4" y="292" width="6.8" height="28" rx="3.4" fill="#E9A2B2" stroke="#B9627A" stroke-width=".7"/>']
    for s in (1, -1):
        o.append(f'<path d="M{12 * s},{266.6} C{17 * s},{259.4} {25.6 * s},{257.4} {31 * s},{264.6}" fill="none" '
                 f'stroke="{UTER_LN}" stroke-width="3.2" stroke-linecap="round"/>'
                 f'<path d="M{12 * s},{266.6} C{17 * s},{259.4} {25.6 * s},{257.4} {31 * s},{264.6}" fill="none" '
                 f'stroke="{UTER}" stroke-width="1.8" stroke-linecap="round"/>')
        for k in (-1, 0, 1):                       # fimbriae fanning toward the ovary
            o.append(f'<path d="M{31 * s},{264.6} l{(2.2 + k) * s:.1f},{3.6 - abs(k) * .6:.1f}" stroke="{UTER_LN}" '
                     'stroke-width="1" stroke-linecap="round"/>')
        o.append(f'<path d="M{12.5 * s},{269} L{22.6 * s},{273.6}" stroke="#D8899C" stroke-width="1.2"/>')
        o.append(f'<ellipse cx="{28.6 * s}" cy="275" rx="6.4" ry="4.4" fill="{OVARY}" stroke="{OVARY_LN}" '
                 f'stroke-width=".9" transform="rotate({18 * s} {28.6 * s} 275)"/>')
        for dx, dy in ((-1.8, -0.8), (1.6, 1.0)):
            o.append(f'<circle cx="{28.6 * s + dx}" cy="{275 + dy}" r="1.2" fill="#FFF2F5" stroke="{OVARY_LN}" '
                     'stroke-width=".5"/>')
    uterus = [(-13.2, 268.6), (-12, 263.6), (-6, 261.4), (6, 261.4), (12, 263.6), (13.2, 268.6), (11.4, 277),
              (6.8, 284.6), (4, 289, 0.5), (4.2, 296.6, 0.5), (-4.2, 296.6, 0.5), (-4, 289, 0.5), (-6.8, 284.6),
              (-11.4, 277)]
    o.append(f'<path d="{_spline(uterus)}" fill="url(#mnp-uterus)" stroke="{UTER_LN}" stroke-width=".9"/>')
    o.append('<path d="M-6.6,267.4 C-3,265.6 3,265.6 6.6,267.4 C5,273.4 2.4,277.6 0,281 C-2.4,277.6 -5,273.4 -6.6,267.4 Z" '
             'fill="#F6C2CE" opacity=".9"/>')
    bl = [(-13.4, 301), (-11, 294.6), (0, 292.4), (11, 294.6), (13.4, 301), (10.6, 308.6), (0, 312.4), (-10.6, 308.6)]
    o.append(f'<path d="{_spline(bl)}" fill="url(#mnp-bladder)" stroke="{BLADDER_LN}" stroke-width=".9"/>')
    o.append(f'<path d="M0,312.4 V318.6" stroke="{BLADDER_LN}" stroke-width="1.6" stroke-linecap="round"/>')
    return "".join(o)


def figure():
    """The woman, in local units (centre line x = 0, crown y = 0).  Skin shapes are drawn twice
    (outline pass, then fill pass) so body and arms read as one silhouette; organs are clipped
    to the torso; everything fades out at mid-thigh."""
    skin = [ARM_LD, ARM_RD, BODY_D]
    outline = "".join(f'<path d="{d}" fill="{SKIN}" stroke="{SKIN_LN}" stroke-width="2.6" stroke-linejoin="round"/>'
                      for d in skin)
    fill = "".join(f'<path d="{d}" fill="url(#mnp-skin)"/>' for d in skin)
    collar = "".join(f'<path d="M{7 * s},101.5 C{19 * s},104.6 {35 * s},104.2 {51 * s},108.6" fill="none" stroke="#D7A999" '
                     'stroke-width="1.3" stroke-linecap="round" opacity=".85"/>' for s in (1, -1))
    inner = (f'<g clip-path="url(#mnp-torso)">{collar}{_breasts()}{_heart()}{_abdomen()}{_pelvis()}'
             f'{_pelvic_organs()}{_thigh_muscles()}</g>')
    head = (f'<path d="{HAIR_BACK_D}" fill="url(#mnp-hair)" stroke="{HAIR_LN}" stroke-width="1.1"/>'
            f'<path d="{HEAD_D}" fill="url(#mnp-face)" stroke="{SKIN_LN}" stroke-width="1.3"/>'
            f'<path d="{HAIR_FRONT_D}" fill="url(#mnp-hair)" stroke="{HAIR_LN}" stroke-width="1.1"/>'
            '<path d="M-5,-1.5 C5,-3.4 17,-0.6 26,7.6" stroke="#9C7462" stroke-width="2" fill="none" '
            'stroke-linecap="round" opacity=".55"/>'
            '<path d="M-20,3 C-25,8 -28,15 -29,22" stroke="#9C7462" stroke-width="1.6" fill="none" '
            'stroke-linecap="round" opacity=".45"/>')
    return f'<g mask="url(#mnp-fade)">{outline}{fill}{inner}</g>{head}'


def figure_defs():
    return ('<linearGradient id="mnp-skin" x1="-1" y1="0" x2="1" y2="0" gradientUnits="objectBoundingBox">'
            f'<stop offset="0" stop-color="{SKIN_EDGE}"/><stop offset=".5" stop-color="#FCEEE7"/>'
            f'<stop offset="1" stop-color="{SKIN_EDGE}"/></linearGradient>'
            '<radialGradient id="mnp-face" cx=".45" cy=".42" r=".7"><stop offset="0" stop-color="#FCEEE7"/>'
            f'<stop offset="1" stop-color="{SKIN_EDGE}"/></radialGradient>'
            f'<linearGradient id="mnp-hair" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{HAIR_A}"/>'
            f'<stop offset="1" stop-color="{HAIR_B}"/></linearGradient>'
            f'<radialGradient id="mnp-heart" cx=".38" cy=".32" r=".8"><stop offset="0" stop-color="{HEART_A}"/>'
            f'<stop offset="1" stop-color="{HEART_B}"/></radialGradient>'
            '<radialGradient id="mnp-breast" cx=".5" cy=".55" r=".55"><stop offset="0" stop-color="#EFBDB2" stop-opacity=".55"/>'
            '<stop offset="1" stop-color="#EFBDB2" stop-opacity="0"/></radialGradient>'
            f'<linearGradient id="mnp-liver" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{LIVER_A}"/>'
            f'<stop offset="1" stop-color="{LIVER_B}"/></linearGradient>'
            '<linearGradient id="mnp-uterus" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#EC9AAD"/>'
            '<stop offset="1" stop-color="#CF6A83"/></linearGradient>'
            '<radialGradient id="mnp-bladder" cx=".42" cy=".38" r=".7"><stop offset="0" stop-color="#FBEBC4"/>'
            f'<stop offset="1" stop-color="{BLADDER}"/></radialGradient>'
            f'<clipPath id="mnp-torso"><path d="{BODY_D}"/></clipPath>'
            '<linearGradient id="mnp-fadeg" x1="0" y1="324" x2="0" y2="366" gradientUnits="userSpaceOnUse">'
            '<stop offset="0" stop-color="#fff"/><stop offset="1" stop-color="#000"/></linearGradient>'
            '<mask id="mnp-fade" maskUnits="userSpaceOnUse" x="-130" y="-20" width="260" height="400">'
            '<rect x="-130" y="-20" width="260" height="400" fill="url(#mnp-fadeg)"/></mask>'
            '<radialGradient id="mnp-gold" cx=".36" cy=".32" r=".75"><stop offset="0" stop-color="#FFE9A8"/>'
            f'<stop offset=".55" stop-color="{GOLD}"/><stop offset="1" stop-color="#D9960F"/></radialGradient>'
            '<radialGradient id="mnp-hypo" cx=".4" cy=".35" r=".75"><stop offset="0" stop-color="#FFC59A"/>'
            f'<stop offset="1" stop-color="{HYPO}"/></radialGradient>'
            '<radialGradient id="mnp-lensbg" cx=".5" cy=".45" r=".6"><stop offset="0" stop-color="#FFFFFF"/>'
            '<stop offset="1" stop-color="#F8E9EF"/></radialGradient>')


# ============================================================== magnified brain (side view, facing left)
def brain_side():
    """Midline (sagittal) view: cerebrum with its folds, corpus callosum, thalamus, the HYPOTHALAMUS
    (orange) with the pituitary hanging below it, brainstem and cerebellum."""
    cere = [(-46, 4), (-44.2, -12), (-36, -24), (-22, -32), (-4, -35.2), (14, -33.2), (30, -26), (41, -14), (46, 0),
            (42.4, 10), (30, 12.4), (18, 9.4), (8, 7.4), (-4, 11), (-14, 13.2), (-28, 13.4), (-40, 10.4)]
    cbl = [(19.6, 12.8), (33.6, 11.4), (43.6, 16.2), (46.4, 25.6), (40.4, 34), (28.4, 36.2), (18.4, 30.4), (15.4, 21)]
    folds = ["M-31,-5 C-27,-16 -15,-22.6 -3,-24.4 C10,-25.4 22,-21 30.4,-12.6",
             "M-41,-4 C-39,-12 -34.6,-18.4 -28,-23.4", "M-18,-31.4 C-16.4,-27.4 -12.4,-26 -10,-27.8",
             "M4,-35 C5.4,-31 7.4,-28.4 8.2,-25.4", "M22,-30.6 C21.6,-27 23.6,-24.6 27,-23",
             "M35.4,-21 C31.4,-15 29.6,-7 29.2,1.4", "M29.2,1.4 C33.6,0.6 39.6,0.2 44.6,-1.6",
             "M-39.4,5.4 C-33.4,3 -27.4,3.8 -22.4,6.4", "M-12,-17.6 C-8,-19.6 -2,-20 3,-19.4"]
    o = [f'<path d="{_spline(cere)}" fill="#EEBFCD" stroke="#B9788F" stroke-width="1.1"/>']
    o += [f'<path d="{d}" fill="none" stroke="#C98EA3" stroke-width="1.25" stroke-linecap="round"/>' for d in folds]
    o.append('<path d="M-20,-1.5 C-19,-10.6 -8,-15.6 4,-15.2 C15,-14.8 23.4,-10.4 25,-4.4 C25.8,-1.2 23.6,0.8 20.6,0.2" '
             'fill="none" stroke="#C995A9" stroke-width="6.8" stroke-linecap="round"/>'
             '<path d="M-20,-1.5 C-19,-10.6 -8,-15.6 4,-15.2 C15,-14.8 23.4,-10.4 25,-4.4 C25.8,-1.2 23.6,0.8 20.6,0.2" '
             'fill="none" stroke="#F9E5EC" stroke-width="5" stroke-linecap="round"/>')
    o.append('<path d="M6,5.6 C10.2,12 12.4,20 13.4,28 C14.2,34 14.2,40 13.2,47 L5.8,47 C5.8,40.4 5,34 4,28 '
             'C3,20.6 1.6,12.6 -0.6,8.4 Z" fill="#E4A9B5" stroke="#B9788F" stroke-width=".9"/>')
    o.append(f'<path d="{_spline(cbl)}" fill="#DE9EB3" stroke="#B9788F" stroke-width="1"/>')
    for k in range(4):
        o.append(f'<path d="M{21 + k * 1.2},{16 + k * 4.4} C{28 + k},{14 + k * 4.4} {37 + k * .6},{16 + k * 4.6} '
                 f'{43.6 - k * 1.4},{20 + k * 4.4}" fill="none" stroke="#C17C96" stroke-width="1" stroke-linecap="round"/>')
    o.append('<ellipse cx="4.6" cy="1.6" rx="9" ry="5.4" fill="#E5A7BB" stroke="#B9788F" stroke-width=".8"/>')
    o.append('<path d="M-8,11.4 L-9,16.4" stroke="#C17A92" stroke-width="1.8" stroke-linecap="round"/>'
             '<ellipse cx="-9.6" cy="19.2" rx="4.4" ry="3.3" fill="#D66E8D" stroke="#A84C69" stroke-width=".8"/>')
    o.append('<circle cx="-8.4" cy="7.6" r="10.5" fill="#F7A56A" opacity=".28"/>'
             '<ellipse cx="-8.4" cy="7.6" rx="6.6" ry="4.4" fill="url(#mnp-hypo)" stroke="#C25A22" stroke-width=".9" '
             'transform="rotate(-10 -8.4 7.6)"/>')
    return "".join(o)


def _tangents(c1, r1, c2, r2):
    """Outer tangent segments between circle 1 and circle 2 (for the zoom cone)."""
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


# ============================================================== callouts
def _dot(x, y, r=5.4):
    return (f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r + 1.9:.1f}" fill="#fff" stroke="{GOLD_LN}" stroke-width=".9"/>'
            f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r:.1f}" fill="url(#mnp-gold)"/>')


def _leader(pts):
    d = "M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in pts)
    return (f'<path d="{d}" fill="none" stroke="#fff" stroke-width="3.6" stroke-linejoin="round" stroke-linecap="round"/>'
            f'<path d="{d}" fill="none" stroke="{LEAD}" stroke-width="1.2" stroke-linejoin="round"/>')


def _serif(x, y, lines, size, fill, weight=900, ls=0.6, anchor="start", lh=1.22):
    """Merriweather text (the sheet's heading face) inside an SVG."""
    if isinstance(lines, str):
        lines = [lines]
    sp = "".join(f'<tspan x="{x}" dy="{0 if i == 0 else size * lh:.1f}">{ln}</tspan>' for i, ln in enumerate(lines))
    return (f'<text x="{x}" y="{y}" font-family="Merriweather, Georgia, serif" font-size="{size}" font-weight="{weight}" '
            f'fill="{fill}" letter-spacing="{ls}" text-anchor="{anchor}">{sp}</text>')


CALL_TS, CALL_BS, CALL_LH = 11.6, 10.5, 13.2     # title / body size (>= 7.6 pt printed), body line step


def callout(side, y, title, text, ico, t):
    """One system note.  Left: icon disc at x 20, text x 40 to 250, leader leaves at x 252.
    Right: text x 520 to 720, icon disc at x 740, leader leaves at x 508."""
    c1, soft = t["c1"], t["soft"]
    if side == "L":
        dx, tx, rule, width = 20, 40, (40, 252), 210
    else:
        dx, tx, rule, width = 740, 520, (508, 722), 200
    lines = wrap(text, width, CALL_BS, 500)
    o = [f'<circle cx="{dx}" cy="{y - 4}" r="14.5" fill="{soft}" stroke="{c1}" stroke-width="1.2"/>',
         _ic(ico, dx, y - 4, 20, c1, 4.6),
         T(tx, y, title, CALL_TS, 800, t["deep"], ls=0.5),
         f'<path d="M{rule[0]},{y + 5} H{rule[1]}" stroke="{c1}" stroke-width="1" opacity=".35"/>',
         T(tx, y + 5 + CALL_LH, lines, CALL_BS, 500, INK, lh=CALL_LH / CALL_BS)]
    anchor = (rule[1], y + 5) if side == "L" else (rule[0], y + 5)
    return "".join(o), anchor, y + 5 + CALL_LH * len(lines)


# ============================================================== picture 1: one woman, every system
FX, FY = 380, 8             # where the figure's crown sits in the viewBox
BM_W, BM_H = 760, 372
INSET_C, INSET_R = (200, 62), 50

NOTES_L = [  # (title baseline y, title, text, icon, dots)
    # [FREE99] thermostat; [SANT16] sleep, mood and anxiety; brain fog is on the [MAP] checklist
    (136, "BRAIN", "Its thermostat (the hypothalamus) misfires as estrogen falls: hot flashes, night sweats. "
                   "Sleep and mood can shift.", "brain", []),
    # breast tenderness with perimenopause estrogen surges [SANT96]; on the [MAP] checklist
    (206, "BREASTS", "Can feel tender while hormones swing. Keep up with mammograms and report any new lump.",
     IC_RIBBON, ["breast"]),
    # [GREEN19] fat gain doubles; [AHA20] belly fat; [PETERS22] gut microbiome shifts after menopause
    (272, "GUT AND WEIGHT", "Fat gain speeds up and shifts to the belly. Gut bacteria change too.", "gut", ["gut"]),
    # [GREEN12] fastest bone loss from 1 year before to 2 years after the last period;
    # [GREEN19] lean (muscle) mass starts to fall as the transition begins
    (328, "BONES AND MUSCLES", "Bone thins fastest around the last period. Muscle and strength slip too.", "bone",
     ["hip", "thigh"]),
]
NOTES_R = [
    # [THORN13]
    (28, "SKIN AND HAIR", "Less collagen, so skin gets thinner and drier. Hair can thin.", "hair", ["hair"]),
    # [AHA20]
    (124, "HEART AND VESSELS", "LDL (bad) cholesterol tends to rise, so heart risk climbs. Know your numbers.", "heart",
     ["heart"]),
    # [GOLD11] follicle loss -> less estradiol; [SANT96] uneven estrogen, less progesterone; [ACOG] bleeding
    (214, "OVARIES AND UTERUS", "Eggs run low, so hormones swing, then fall. Periods change, then stop. "
                                "Any bleeding after that needs a check.", IC_UTERUS, ["ovary"]),
    # [GSM20] 27-84% after menopause, treatable; [SANT16] does not go away without treatment
    (302, "BLADDER AND VAGINA", "Dryness, pain with sex, urgency and bladder infections. Common, and treatable.",
     IC_BLADDER, ["bladder"]),
]


def body_map(t):
    c1 = t["c1"]
    g = lambda k: (FX + DOT[k][0], FY + DOT[k][1])
    out = [f'<defs>{figure_defs()}<clipPath id="mnp-inset"><circle cx="{INSET_C[0]}" cy="{INSET_C[1]}" '
           f'r="{INSET_R - 1}"/></clipPath></defs>']
    out.append(f'<g transform="translate({FX},{FY})">{figure()}</g>')

    # ---- heading and KEY, top left
    out.append(_serif(4, 17, ["ONE WOMAN,", "EVERY SYSTEM"], 14, c1, lh=1.25))
    out.append(f'<rect x="4" y="46" width="128" height="56" rx="8" fill="#fff" stroke="#D9CBD2" stroke-width="1.2"/>'
               + T(14, 62, "KEY", 10.4, 800, INK, ls=1.3) + _dot(22, 84, 5)
               + T(34, 80.4, ["Where a change", "can show up"], 10.4, 600, INK, lh=1.2))

    # ---- magnified hypothalamus: lens on the head, zoom cone, circle with the side-view brain
    lens_c, lens_r = g("brain"), 7.5
    (a1, b1), (a2, b2) = _tangents(lens_c, lens_r, INSET_C, INSET_R)
    out.append(f'<path d="M{a1[0]:.1f},{a1[1]:.1f} L{b1[0]:.1f},{b1[1]:.1f} L{b2[0]:.1f},{b2[1]:.1f} '
               f'L{a2[0]:.1f},{a2[1]:.1f} Z" fill="{c1}" fill-opacity=".07"/>')
    for a, b in ((a1, b1), (a2, b2)):
        out.append(f'<path d="M{a[0]:.1f},{a[1]:.1f} L{b[0]:.1f},{b[1]:.1f}" stroke="{c1}" stroke-width="1" '
                   'stroke-opacity=".55"/>')
    out.append(f'<circle cx="{lens_c[0]:.1f}" cy="{lens_c[1]:.1f}" r="{lens_r}" fill="#fff" fill-opacity=".35" '
               f'stroke="{c1}" stroke-width="1.6"/>')
    out.append(f'<circle cx="{INSET_C[0]}" cy="{INSET_C[1]}" r="{INSET_R + 2.2}" fill="#fff"/>'
               f'<circle cx="{INSET_C[0]}" cy="{INSET_C[1]}" r="{INSET_R}" fill="url(#mnp-lensbg)"/>')
    out.append(f'<g clip-path="url(#mnp-inset)"><g transform="translate({INSET_C[0] + 1},{INSET_C[1] - 4}) scale(.92)">'
               f'{brain_side()}</g></g>')
    out.append(f'<circle cx="{INSET_C[0]}" cy="{INSET_C[1]}" r="{INSET_R}" fill="none" stroke="{c1}" stroke-width="2"/>')
    hx, hy = INSET_C[0] + 1 - 8.4 * .92, INSET_C[1] - 4 + 7.6 * .92
    lab = "Hypothalamus"
    lw = tw(lab, 10.2, 800) + 12
    lx, ly = hx - 15 - lw / 2 + 4, hy + 21
    out.append(f'<path d="M{hx - 3:.1f},{hy + 4:.1f} L{hx - 15:.1f},{hy + 21:.1f}" stroke="{HYPO}" stroke-width="1.3"/>')
    out.append(f'<rect x="{lx:.1f}" y="{ly:.1f}" width="{lw:.1f}" height="15" rx="7.5" fill="#fff" '
               f'stroke="{HYPO}" stroke-width="1.1"/>' + T(lx + lw / 2, ly + 11, lab, 10.2, 800, "#B04A14", "middle"))

    # ---- the eight system notes and their leaders
    marks = []
    for side, notes in (("L", NOTES_L), ("R", NOTES_R)):
        for y, title, text, ico, dots in notes:
            s, (ax, ay), _ = callout(side, y, title, text, ico, t)
            out.append(s)
            for k in dots:
                px, py = g(k)
                out.append(_leader([(ax, ay), (ax + (12 if side == "L" else -12), ay), (px, py)]))
                marks.append((px, py))
    for px, py in marks:
        out.append(_dot(px, py))
    out.append(_dot(*lens_c, r=4.2))          # the brain dot sits inside the lens on the head
    return svg(BM_W, BM_H, "".join(out),
               "A woman's body with notes on the changes menopause can bring: brain and thermostat, skin and hair, "
               "breasts, heart, gut and weight, ovaries and uterus, bladder and vagina, bones and muscles. "
               "A magnified circle shows the hypothalamus in the brain.")


# ============================================================== picture 2: hot flashes + hormone timeline
P2_W, P2_H = 760, 184


def _heat_trace(x0, x1, mid):
    """Core body heat over a few hours: small ups and downs, one small rise and a dip after it.
    The SAME trace is drawn in both charts."""
    pts = []
    n = 72
    for i in range(n + 1):
        u = i / n
        y = (mid + 2.2 * math.sin(u * 12.5) + 1.0 * math.sin(u * 29 + 1)
             - 13.0 * math.exp(-((u - 0.58) / 0.075) ** 2) + 12.5 * math.exp(-((u - 0.79) / 0.06) ** 2))
        pts.append((x0 + (x1 - x0) * u, y))
    return pts


def _poly(pts):
    return "M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in pts)


def _burst(cx, cy, r=8.5, n=9):
    p = []
    for i in range(2 * n):
        a = math.pi * i / n - math.pi / 2
        rr = r if i % 2 == 0 else r * 0.5
        p.append(f"{cx + rr * math.cos(a):.1f},{cy + rr * math.sin(a):.1f}")
    return f'<polygon points="{" ".join(p)}" fill="{FLASH}" stroke="{FLASH_LN}" stroke-width=".9" stroke-linejoin="round"/>'


def hotflash_panel(t):
    c1 = t["c1"]
    o = [T(0, 13, "WHY HOT FLASHES HAPPEN", 12.4, 800, c1, ls=0.6)]
    y0, y1, mid = 36, 104, 69
    for x0, title, top, bot in ((4, "STEADY ESTROGEN", 48, 90), (152, "LOW ESTROGEN", 62, 76)):
        w = 134
        o.append(T(x0 + w / 2, 30, title, 10.2, 800, "#4A3F45", "middle", ls=0.5))
        o.append(f'<rect x="{x0}" y="{y0}" width="{w}" height="{y1 - y0}" rx="6" fill="#fff" stroke="#D9CDD3" stroke-width="1.1"/>')
        o.append(f'<rect x="{x0 + 1}" y="{top}" width="{w - 2}" height="{bot - top}" fill="{ZONE}"/>')
        o.append(f'<path d="M{x0 + 1},{top} H{x0 + w - 1}" stroke="{SWEAT}" stroke-width="1.4" stroke-dasharray="3.2 2.4"/>'
                 f'<path d="M{x0 + 1},{bot} H{x0 + w - 1}" stroke="{SHIVER}" stroke-width="1.4" stroke-dasharray="3.2 2.4"/>')
        o.append(T(x0 + 6, top - 3.6, "sweat line", 10, 700, SWEAT))
        o.append(T(x0 + 6, bot + 11.6, "shiver line", 10, 700, SHIVER))
        tr = _heat_trace(x0 + 4, x0 + w - 4, mid)
        o.append(f'<path d="{_poly(tr)}" fill="none" stroke="{HEAT}" stroke-width="2.1" stroke-linejoin="round" '
                 'stroke-linecap="round"/>')
        if bot - top < 20:          # narrow zone: the SAME small rise now crosses the sweat line
            px, py = min(tr, key=lambda p: p[1])
            o.append(_burst(px, py, 8.4))
            o.append(T(px + 11, py - 3.5, "hot flash", 10, 800, FLASH_LN))
            qx, qy = max(tr, key=lambda p: p[1])
            o.append(T(qx + 2, bot + 11.6, "chills", 10, 800, SHIVER, "middle"))
    # [FREE99]: symptomatic women's zone is ~0.0 C vs 0.4 C; small core rises then trigger flushing and sweating
    lines = wrap("Low estrogen shrinks the brain’s comfort zone for body heat, so a small rise sets off a hot "
                 "flash, often followed by chills.", 284, 10.5, 500)
    o.append(T(4, 121, lines, 10.5, 500, INK, lh=1.24))
    return "".join(o)


# hormone timeline geometry.  The perimenopause and postmenopause stretch is drawn to one scale in
# years around menopause (12 months with no period); the reproductive years are shown shorter.
TL_X0, TL_X1, TL_TOP, TL_AX = 338, 748, 34, 116
X_PERI, X_MENO = 440, 620
PX_YR = (X_MENO - X_PERI) / 7.0          # perimenopause drawn as 7 years ([PARAM17]: median 4.4 to 8.6)


def _x_yr(yr):
    return X_MENO + yr * PX_YR


def _level_y(v):
    return TL_AX - 1.3 * v


def _g(x, c, h, s):
    return h * math.exp(-((x - c) / s) ** 2 / 2)


def _estrogen(x):
    if x < X_PERI:
        base = 12.0
    elif x < 562:
        base = 12.0 - 2.0 * (x - X_PERI) / 122
    elif x < 614:
        base = 10.0 - 5.0 * (x - 562) / 52
    else:
        base = 5.0
    v = base
    for k in range(3):                       # regular cycles: a mid-cycle peak, then a smaller luteal rise
        s0 = 340 + 34 * k
        v += _g(x, s0 + 14, 22, 3.6) + _g(x, s0 + 25, 10, 5.0)
    # perimenopause: erratic swings, some HIGHER than before [SANT96], then a steep fall
    for c, h, s in ((456, 26, 4.0), (471, 8, 5.0), (490, 34, 4.2), (511, 16, 4.6), (534, 36, 4.5), (556, 11, 5.0),
                    (578, 19, 5.0), (601, 8, 5.0)):
        v += _g(x, c, h, s)
    return v


def _progesterone(x):
    v = 2.4 if x < X_PERI else (2.0 if x < X_MENO else 1.4)
    for k in range(3):                       # a luteal hump after each ovulation
        v += _g(x, 340 + 34 * k + 25.5, 18, 5.0)
    # perimenopause: fewer ovulations, so progesterone falls FIRST [SANT96]
    for c, h, s in ((472, 13, 5.0), (512, 8, 5.0), (556, 4.5, 5.0)):
        v += _g(x, c, h, s)
    return v


def timeline_panel(t):
    c1, deep = t["c1"], t["deep"]
    o = [T(306, 13, "HOW YOUR HORMONES CHANGE", 12.4, 800, c1, ls=0.6)]
    bands = [(TL_X0, X_PERI, STAGE_A, "REPRODUCTIVE", "regular cycles"),
             (X_PERI, X_MENO, STAGE_B, "PERIMENOPAUSE", "periods change, often 4 to 8 years"),   # [PARAM17]
             (X_MENO, TL_X1, STAGE_A, "POSTMENOPAUSE", "the rest of life")]
    for a, b, fill, lab, sub in bands:
        o.append(f'<rect x="{a}" y="{TL_TOP - 14}" width="{b - a}" height="{TL_AX - TL_TOP + 14}" fill="{fill}"/>')
        o.append(T((a + b) / 2, TL_TOP - 3, lab, 10.2, 800, "#4A4550", "middle", ls=0.5))
        o.append(T((a + b) / 2, TL_TOP + 9.6, sub, 10, 600, "#6A6470", "middle", italic=True))
    o.append(f'<path d="M{TL_X0},{TL_TOP - 14} V{TL_AX} H{TL_X1 + 2}" fill="none" stroke="#8A838F" stroke-width="1.3"/>'
             f'<path d="M{TL_X1 + 1},{TL_AX - 4} L{TL_X1 + 8},{TL_AX} L{TL_X1 + 1},{TL_AX + 4} Z" fill="#8A838F"/>')
    cy = (TL_TOP + TL_AX) / 2 + 2
    o.append(f'<text x="{TL_X0 - 8}" y="{cy}" font-family="Inter, Helvetica, Arial, sans-serif" font-size="10" '
             f'font-weight="700" fill="#6A6470" text-anchor="middle" transform="rotate(-90 {TL_X0 - 8} {cy})">'
             'hormone level</text>')
    xs = [TL_X0 + 1 + i * 1.0 for i in range(int(TL_X1 - TL_X0 - 2))]
    o.append(f'<path d="{_poly([(x, _level_y(_progesterone(x))) for x in xs])}" fill="none" stroke="{P_LINE}" '
             'stroke-width="2" stroke-dasharray="5 3" stroke-linejoin="round"/>')
    o.append(f'<path d="{_poly([(x, _level_y(_estrogen(x))) for x in xs])}" fill="none" stroke="{E_LINE}" '
             'stroke-width="2.4" stroke-linejoin="round" stroke-linecap="round"/>')
    # menopause marker: 12 months in a row with no period
    o.append(f'<path d="M{X_MENO},{TL_TOP + 15} V{TL_AX}" stroke="{c1}" stroke-width="1.8"/>')
    mw = tw("MENOPAUSE", 10.2, 800, 0.5) + 14
    o.append(f'<rect x="{X_MENO - mw / 2:.1f}" y="{TL_TOP + 22}" width="{mw:.1f}" height="16" rx="8" fill="{c1}"/>'
             + T(X_MENO, TL_TOP + 33.6, "MENOPAUSE", 10.2, 800, "#fff", "middle", ls=0.5))
    o.append(T(X_MENO + 6, TL_TOP + 52, ["12 months in a row", "with no period"], 10, 700, deep, lh=1.18))
    # windows under the axis (the final period sits 1 year before the menopause marker):
    # frequent hot flashes [AVIS15] median 7.4 years in all, 4.5 of them after the final period;
    # fastest bone loss [GREEN12] from 1 year before to 2 years after the final period
    hot = (_x_yr(-1 - 2.9), _x_yr(-1 + 4.5))
    bone = (_x_yr(-1 - 1), _x_yr(-1 + 2))
    for (a, b), y, col, lab, tx in ((hot, TL_AX + 11, HOTWIN, "Hot flashes most likely", "#8A5D00"),
                                    (bone, TL_AX + 26, BONEWIN, "Bone loss fastest", "#6E5634")):
        o.append(f'<path d="M{a:.1f},{y - 4} V{y} H{b:.1f} V{y - 4}" fill="none" stroke="{col}" stroke-width="2.6" '
                 'stroke-linejoin="round" stroke-linecap="round"/>')
        o.append(T(a - 7, y + 3.4, lab, 10.2, 700, tx, "end"))
    return "".join(o)


def key_strip(y, w=760, h=28):
    items = [
        (f'<path d="M-11,0 H11" stroke="{E_LINE}" stroke-width="2.6" stroke-linecap="round"/>', "Estrogen"),
        (f'<path d="M-11,0 H11" stroke="{P_LINE}" stroke-width="2.2" stroke-dasharray="5 3"/>', "Progesterone"),
        (f'<rect x="-11" y="-7" width="11" height="14" fill="{STAGE_A}" stroke="#CFCAD3" stroke-width=".8"/>'
         f'<rect x="0" y="-7" width="11" height="14" fill="{STAGE_B}" stroke="#CFCAD3" stroke-width=".8"/>', "Life stages"),
        (f'<rect x="-11" y="-6" width="22" height="12" fill="{ZONE}"/><path d="M-11,-6 H11" stroke="{SWEAT}" '
         f'stroke-width="1.3" stroke-dasharray="3 2"/><path d="M-11,6 H11" stroke="{SHIVER}" stroke-width="1.3" '
         'stroke-dasharray="3 2"/>', "Comfort zone"),
        (f'<path d="M-11,2 C-6,-5 -2,6 3,-1 C6,-5 9,-2 11,-3" fill="none" stroke="{HEAT}" stroke-width="2"/>', "Body heat"),
        (_burst(0, 0, 7.6), "Hot flash"),
    ]
    o = [f'<rect x=".6" y="{y}" width="{w - 1.2}" height="{h}" rx="8" fill="#fff" stroke="#D9CBD2" stroke-width="1.2"/>',
         T(14, y + h / 2 + 3.7, "KEY", 10.4, 800, INK, ls=1.3)]
    sw, gap, x = 24, 7, 56
    widths = [sw + gap + tw(lab, 10.6, 600) for _, lab in items]
    space = (w - 14 - x - sum(widths)) / (len(items) - 1)
    for (s, lab), wd in zip(items, widths):
        o.append(f'<g transform="translate({x + sw / 2:.1f},{y + h / 2:.1f})">{s}</g>')
        o.append(T(round(x + sw + gap, 1), y + h / 2 + 3.8, lab, 10.6, 600, INK))
        x += wd + space
    return "".join(o)


def picture2(t):
    body = (f'{hotflash_panel(t)}<path d="M296,4 V{P2_H - 40}" stroke="#E6DCE1" stroke-width="1.2"/>'
            f'{timeline_panel(t)}{key_strip(P2_H - 29)}')
    return svg(P2_W, P2_H, body,
               "Left: two charts of body heat over time. With steady estrogen the comfort zone is wide; with low "
               "estrogen it is narrow, so the same small rise in heat crosses the sweat line and sets off a hot flash. "
               "Right: estrogen and progesterone across the reproductive years, perimenopause and postmenopause.")


# ============================================================== blocks under the art
TRACK = ["Hot flashes", "Poor sleep", "Mood or anxiety", "Vaginal dryness", "UTIs (bladder)", "Low sex drive",
         "Weight change", "Sore breasts", "Headaches", "Brain fog", "Joint aches", "Hair changes"]   # the 12 [MAP] items


def tracker():
    cells = "".join(f'<div class="mnp-it"><span>{lab}</span><em><i>0</i><i>1</i><i>2</i><i>3</i></em></div>'
                    for lab in TRACK)
    return ('<div class="mnp-track"><div class="mnp-th"><b>Track your symptoms</b>'
            '<span>Circle <strong>0</strong> none, <strong>1</strong> mild, <strong>2</strong> some days, '
            '<strong>3</strong> most days.</span></div>'
            f'<div class="mnp-grid">{cells}</div>'
            '<div class="mnp-tot"><span>Add them up. Bring this to your visit.</span>'
            '<b>Today</b><i></i><small>/ 36</small><b>In 6 weeks</b><i></i><small>/ 36</small></div></div>')


def best_box():
    # [HT22] most effective; favorable under 60 or within 10 years of menopause without contraindications.
    # [NH23] recommended nonhormone options; supplements and herbal remedies not recommended for hot flashes.
    # [ESTRO] small EstroG-100 trials; the 2025 one was run by the tested product's maker (OLLY / Unilever).
    return ('<div class="mnp-best"><h4>Hot flashes: what works best</h4><ol>'
            '<li><b>Hormone therapy works best.</b> For most healthy women under 60, the benefits outweigh the '
            'risks. Ask {who}.</li>'
            '<li><b>Also proven:</b> CBT, clinical hypnosis and some prescriptions.</li>'
            '<li><b>Supplements</b> are not recommended for hot flashes. EstroG&#8209;100, in Menopause Support, '
            'helped in small trials; the newest was paid for by a supplement company.</li></ol>'
            '<small>Source: The Menopause Society, 2022 and 2023</small></div>')


def front(t, ed):
    return ('<div class="mnp">'
            f'<div class="mnp-art">{body_map(t)}</div>'
            f'<div class="mnp-art mnp-art2">{picture2(t)}</div>'
            f'<div class="mnp-low">{tracker()}{best_box()}</div>'
            '</div>')


CSS = r"""
.mnp .mnp-art svg{display:block;width:100%;height:auto}
.mnp .mnp-art2{margin-top:0.04in}
.mnp .mnp-low{display:grid;grid-template-columns:1.72fr 1fr;gap:0.1in;margin-top:0.06in;align-items:stretch}
.mnp .mnp-track{border:1px solid #E7D3DC;border-radius:9px;background:var(--tint);padding:0.05in 0.1in 0.05in;
  display:flex;flex-direction:column}
.mnp .mnp-th{display:flex;align-items:baseline;gap:8px;margin-bottom:2px}
.mnp .mnp-th b{font:900 10.2pt Merriweather,Georgia,serif;color:var(--c1);white-space:nowrap}
.mnp .mnp-th span{font-size:7.6pt;color:#3F4A50}
.mnp .mnp-th strong{color:var(--deep)}
.mnp .mnp-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:0 12px}
.mnp .mnp-it{display:flex;align-items:center;justify-content:space-between;gap:4px;border-bottom:1px dotted #E2C9D4;
  padding:3px 0}
.mnp .mnp-it span{font-size:7.6pt;line-height:1.1;color:#2B3236;white-space:nowrap}
.mnp .mnp-it em{display:flex;gap:2px;font-style:normal;flex:none}
.mnp .mnp-it i{display:inline-flex;align-items:center;justify-content:center;width:0.14in;height:0.14in;border-radius:50%;
  border:1.1px solid var(--c2);font:700 7pt/1 Inter,sans-serif;font-style:normal;color:var(--deep);background:#fff}
.mnp .mnp-tot{display:flex;align-items:center;gap:5px;margin-top:auto;padding-top:4px;font-size:7.6pt;color:#3F4A50}
.mnp .mnp-tot span{flex:1}
.mnp .mnp-tot b{font:800 7.6pt Inter,sans-serif;color:var(--deep);white-space:nowrap}
.mnp .mnp-tot i{display:block;width:0.34in;height:0.19in;border-radius:5px;background:#fff;border:1px solid #D6C3CC}
.mnp .mnp-tot small{font-size:7.4pt;color:#5E686F;margin-right:4px}
.mnp .mnp-best{border:1px solid #E7D3DC;border-left:4px solid var(--c1);border-radius:0 9px 9px 0;background:#fff;
  padding:0.05in 0.1in 0.04in;display:flex;flex-direction:column}
.mnp .mnp-best h4{margin:0 0 2px;font:900 10.2pt Merriweather,Georgia,serif;color:var(--c1)}
.mnp .mnp-best ol{margin:0;padding-left:13px;font-size:7.4pt;line-height:1.24;color:#2B3236}
.mnp .mnp-best li{margin:0 0 1px}
.mnp .mnp-best li b{color:var(--deep)}
.mnp .mnp-best small{margin-top:1px;font-size:7pt;color:#6A747B}
/* back page: scoped with :has() to the marker span in this sheet's lifestyle title */
.sheet.back:has(.mnp-back) .col .need{height:0.56in;min-height:0.56in}
.sheet.back:has(.mnp-back) .col .need i{white-space:normal}
"""

# ============================================================== the sheet
SHEET = {
    "slug": SLUG, "code": "ND-HM-501", "order": 10, "theme": "hormone", "series": "Hormone Health Series",
    "title": "Menopause and Perimenopause", "sub": "Every system changes. Every system can be supported.",
    # 12 months in a row with no period = menopause (STRAW+10; NAMS).  Median age 50 to 52 [GOLD11].
    # Perimenopause often lasts 4 to 8 years [PARAM17].  Hormone therapy most effective [HT22, NH23].
    "intro": ("Menopause is the day you reach <b>12 months in a row with no period</b>, on average around age 51. "
              "The years before it, <b>perimenopause</b>, often last 4 to 8 years while estrogen and progesterone swing, "
              "then fall. These hormones act on nearly every tissue, so changes show up from head to toe. "
              "<b>Hormone therapy is the most effective treatment for hot flashes</b>: ask {who} if it fits you."),
    "front": front,
    "css": CSS,
    "back": {
        # the empty span lets this sheet's CSS reach its own back page (see CSS)
        "life_title": 'Lifestyle Recommendations<span class="mnp-back"></span>',
        "style": "circle",
        "life": [
            # Physical Activity Guidelines for Americans, 2nd ed. (HHS 2018): muscle strengthening 2+ days a week,
            # balance work for older adults; NAMS 2021 osteoporosis position statement: exercise for bone
            ("dumbbell", "Lift weights", "Strength work 2 to 3 days a week guards muscle and bone."),
            # Physical Activity Guidelines: 150 to 300 minutes of moderate activity a week
            ("walk", "Walk most days", "150 minutes a week helps your heart, mood, sleep and weight."),
            # NIH ODS calcium: 1,200 mg a day for women 51+
            ("plate", "Bone-smart plate", "Protein at each meal and calcium foods like yogurt and greens."),
            ("moon", "Guard your sleep", "Same bedtime, a cool dark room, less alcohol and late caffeine."),
            # [NH23]: CBT and clinical hypnosis recommended (Level I) for hot flashes
            ("brain", "Try CBT", "CBT and clinical hypnosis are proven to ease hot flashes."),
            # [GOLD11] smoking and earlier menopause; NIH NIAMS: smoking is an osteoporosis risk factor
            ("smoke", "Skip smoking", "Smoking speeds bone loss and raises heart risk."),
        ],
        "cols": [
            {"p": "meno_menopause_support", "need": "Menopausal comfort", "needsub": "EstroG&#8209;100, ashwagandha, black cohosh",
             "start": True,
             # [ESTRO] (the honest caveat is on the front); [ASHW24]; Peri vs Meno by stage [MAP]
             # PeriMenopause Support R199, sell sheet ND565 Rev. 8/24 (labels.json): per tablet Estro G-100 blend
             # 500 mg, ashwagandha root powder 500 mg, milk thistle seed powder 100 mg; same label caution
             "bullets": ["Supports comfort during hot flashes",
                         "Still having periods? Use PeriMenopause Support: 500 mg EstroG&#8209;100, 500 mg "
                         "ashwagandha, 100 mg milk thistle"],
             "dose": "1 tablet daily", "dosesub": "with food, same time each day", "sched": [("am", 1, "tablet")]},
            {"p": "meno_mag_calm_pro", "need": "Sleep and calm", "needsub": "magnesium, myo&#8209;inositol, L&#8209;theanine",
             "bullets": ["Supports relaxation and restful sleep", "Supports a healthy stress response and mood"],
             "dose": "1 scoop at bedtime", "dosesub": "in 6 oz water; up to 2 a day", "sched": [("bed", 1, "scoop")]},
            {"p": "meno_d3_5000_k2", "need": "Bone strength", "needsub": "vitamin D3 with vitamins K2 and K1",
             "bullets": ["Supports calcium absorption for strong bones", "K2 helps put calcium to work in bone"],
             "dose": "1 softgel daily", "dosesub": "with your evening meal", "sched": [("pm", 1, "softgel")]},
            {"p": "meno_ultrabiotic_womens", "need": "Healthy flora", "needsub": "women’s probiotic, 9 strains",
             # sell sheet ND1053 claims: healthy vaginal microbiome, healthy gut microbiome
             "bullets": ["Supports a healthy vaginal microbiome", "Supports a healthy gut microbiome"],
             "dose": "2 capsules daily", "dosesub": "at bedtime", "sched": [("bed", 2, "capsules")]},
            {"p": "meno_creatine", "need": "Muscle and strength", "needsub": "creatine monohydrate",
             # [CREA26]: >= 5 g a day with resistance training
             "bullets": ["Supports muscle and strength with strength training",
                         "5 g a day, the amount studied after menopause"],
             "dose": "1 scoop daily", "dosesub": "in 8 to 16 oz of any drink", "sched": [("am", 1, "scoop")]},
        ],
        "rx": {
            "practitioner": [
                # [HT22] [NH23]
                "<b>Hot flashes?</b> Hormone therapy works best. Ask your provider whether it fits you.",
                # label caution (sell sheet ND564); NIH ODS black cohosh: rare liver injury, stop with jaundice or dark urine
                "<b>Had breast cancer or another estrogen-dependent cancer?</b> The label says not to use Menopause "
                "Support. Stop it if urine darkens or skin yellows.",
                # USPSTF osteoporosis screening; NIH ODS vitamin D: upper limit 4,000 IU a day for adults
                "<b>Ask about</b> a bone density scan, cholesterol, A1c and vitamin D. D3 5000 is above the 4,000 IU "
                "daily upper limit: use it with level checks.",
            ],
            "pharmacy": [
                "<b>Had breast cancer or another estrogen-dependent cancer?</b> The label says not to use Menopause "
                "Support. Stop it if urine darkens or skin yellows.",
                # NIH ODS vitamin K (warfarin); NIH ODS / NCCIH ashwagandha interactions
                "<b>Warfarin?</b> Vitamin K in D3 5000 with K2 can shift your INR. <b>Thyroid or sedative "
                "drugs?</b> Ashwagandha can add to them.",
                # NIH ODS magnesium: separate from bisphosphonates and tetracycline or quinolone antibiotics;
                # creatine raises serum creatinine (de Souza Almeida 2026, cited in the creatine blast)
                "<b>Space magnesium</b> 2 hours from bisphosphonates and some antibiotics. <b>Creatine</b> raises "
                "creatinine on kidney labs.",
            ],
        },
    },
}
