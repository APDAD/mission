"""Better Sleep (ND-NR-702), Brain and Nerve Series.  slug "sleep", order 17, theme "neuro".

Self-contained sheet module (no legacy / sheets.py / art.py drawing code), new on 2026-11-03.

FRONT, top to bottom
  1. "Your brain's clock": a side view of the head, cut down the middle so the deep midline parts
     show (cerebrum with the corpus callosum and thalamus, brainstem, cerebellum).  BY DAY (sun)
     daylight enters the eye and the teal DAY SIGNAL runs along the optic nerve to the master clock
     (SCN, just above the optic chiasm), which keeps melatonin off; AT NIGHT (moon) the dark-gray
     NIGHT SIGNAL, which carries a moon badge, runs from the clock to the pineal gland, and the pineal
     gland releases melatonin into a vein (great cerebral vein and straight sinus, back along the border
     between cerebrum and cerebellum to the confluence of sinuses at the back of the skull, where the
     drawn vein stops: from there the blood leaves sideways, out of the midline plane).  The skull's
     bone rim runs round the cerebrum and on, as the occipital bone, round the back and underside of
     the cerebellum to the foramen magnum behind the brainstem.  Two colours for the two times, so the
     frame never reads as "light makes melatonin".  Beside it, a 24-hour dial: melatonin (the only
     blue on the sheet's art) rises in the evening and peaks in the small hours; cortisol (gold, the
     wake-up and stress hormone) climbs before dawn and peaks after waking; the outer ring (yellow
     day, dark-gray night) is named in the card.
  2. "One night of sleep": a sleep-stage strip (awake, REM, light, deep) for a typical adult
     night of about 5 cycles, with three plain-language notes.  One two-row KEY names every symbol
     in both pictures (row 1 the clock, row 2 the sleep stages).
  3. "What can throw your clock off": 8 risk-factor icons.
  4. "Know your sleep": hours needed by age, the 3-part long-term (chronic) insomnia check, and the
     STOP-Bang sleep apnea check (tick boxes, "3 or more ticks? Ask about a sleep apnea test (a
     doctor orders it)").  A pharmacist can go over the check but cannot order the study, so the line
     says who orders it without sending a practitioner-edition reader "to your doctor".
     STOP-Bang is the property of University Health Network (UHN, Toronto; stopbang.ca), and the
     Sources line names it.  PERMISSION IS STILL OPEN: the ATS questionnaire listing says use needs the
     developer's permission (UHN contact), so NutriDyn must ask UHN before this sheet is printed.  If
     UHN says no, set APNEA_PANEL = "signs": an unnamed, unscored list of apnea warning signs in our
     own words (APNEA_SIGNS) replaces the STOP-Bang list, same box, same height.
BACK: "Reset your sleep clock" (CBT-I habits by morning / day / night, with sleep drive explained) and
5 NutriDyn products: GoodNight (start here), Stress Essentials Calm, Mag Calm Pro, Magnesium Glycinate (the
capsule alternative to Mag Calm Pro: one magnesium, never both), Stress Essentials Cortisol Pro (facts and
sources in products.d/sleep.json).

Every SVG id starts with "slp-" and every CSS class with "slp-", so nothing collides with other
sheets in the all-sheets bundle.  SVG text is never below 10 units (7.3 pt printed; the viewBox is
760 wide and prints 7.66 in wide).  The back page carries an empty <i class="slp-bk"> in its band
title so this module's back-page CSS can be scoped with .sheet.back:has(.slp-bk) (the build puts no
sheet class on the back page).

SOURCES (each number on the page carries one of these tags in a comment)
  [CDCFS]     CDC FastStats: Sleep in Adults (BRFSS 2022; seen through web search, cdc.gov is not
              reachable from the build machine): short sleep (< 7 h) "stayed the same from 2013 to
              2022"; 2022 state range 30% (VT) to 46% (HI).  National 2022 weighted prevalence 36.1%
              (UNMC analysis of BRFSS 2022).  Earlier anchor: Liu Y et al. MMWR 2016;65:137, PMID
              26890214 (2014 BRFSS, 34.8% < 7 h).  So "more than 1 in 3" holds.
  [CDCNEED]   CDC, About Sleep: How much sleep do I need? (18-60 y: 7 or more h; 61-64: 7-9 h;
              65+: 7-8 h), built on the AASM/SRS consensus, Watson NF et al. Sleep 2015;38:843.
              PMID 26039963
  [OHAYON02]  Ohayon MM. Epidemiology of insomnia. Sleep Med Rev 2002;6:97-111. PMID 12531146
              (about 1/3 have insomnia symptoms; 9-15% with daytime consequences)
  [ICSD3TR]   AASM International Classification of Sleep Disorders, 3rd ed., text revision
              (ICSD-3-TR, 2023), same chronic-insomnia criteria as ICSD-3 (Sateia MJ, Chest
              2014;146:1387, PMID 25367475): trouble falling or staying asleep or waking too early,
              despite the chance to sleep, with daytime effects, 3+ nights a week for 3+ months
  [ACP16]     Qaseem A et al. Ann Intern Med 2016;165:125. PMID 27136449 (CBT-I is the initial
              treatment for chronic insomnia, strong recommendation)
  [AASM21]    Edinger JD et al. J Clin Sleep Med 2021;17:255. PMID 33164742 (multicomponent CBT-I,
              strong; stimulus control, sleep restriction, relaxation; sleep hygiene alone not enough)
  [AASM17]    Sateia MJ et al. J Clin Sleep Med 2017;13:307. PMID 27998379 (pharmacologic guideline;
              melatonin, tryptophan and valerian not suggested as stand-alone chronic insomnia
              treatment; why the back sells support, not a cure)
  [STOPBANG]  Chung F et al. STOP-Bang questionnaire. Chest 2016;149:631. PMID 26378880 (8 yes/no
              items; collar 17 in+ men, 16 in+ women; score 3+ = intermediate or high risk).  Owner:
              University Health Network (copies in circulation read "Property of University Health
              Network, www.stopbang.ca"; ATS sleep-questionnaire listing, site.thoracic.org/assemblies/
              srn/sleep-related-questionnaires/stop-bang: "permission required from developer").
              stopbang.ca itself is not reachable from the build machine.
  [AASMOSA]   Epstein LJ et al. (AASM Adult OSA Task Force). J Clin Sleep Med 2009;5:263-76. PMID
              19960649 (symptoms: snoring, witnessed apneas, gasping or choking, daytime sleepiness;
              exam: neck over 17 in in men, 16 in in women; hypertension among the high-risk groups;
              diagnosis by a sleep study) and NHLBI, Sleep Apnea (loud snoring, choking or gasping,
              very sleepy by day; about half of people with sleep apnea have high blood pressure; seen
              through web search).  Basis of the fallback list APNEA_SIGNS, which is not scored.
  [ZISAPEL18] Zisapel N. Br J Pharmacol 2018;175:3190. PMID 29318587 (SCN-driven, light-inhibited
              melatonin conveys "darkness"); [DLMO] Pandi-Perumal SR et al. Prog
              Neuropsychopharmacol Biol Psychiatry 2007;31:1. PMID 16884842 (dim-light melatonin
              onset in the evening, about 2 h before habitual sleep; night peak)
  [BENARROCH08] Benarroch EE. Suprachiasmatic nucleus and melatonin. Neurology 2008;71:594.
              PMID 18711114 (retina -> SCN -> pineal pathway; the SCN sits above the optic chiasm)
  [DEBONO09]  Debono M et al. J Clin Endocrinol Metab 2009;94:1548. PMID 19223520 (cortisol:
              nadir about 00:18, quiet 19:43-05:31, peak about 08:32)
  [GOOLEY11]  Gooley JJ et al. J Clin Endocrinol Metab 2011;96:E463. PMID 21193540 (room light
              before bed delayed melatonin onset in 99% and shortened it by about 90 minutes)
  [CHANG15]   Chang AM et al. PNAS 2015;112:1232. PMID 25535358 (light-emitting e-readers at night:
              later clock, less melatonin, longer to fall asleep)
  [VGONTZAS01] Vgontzas AN et al. J Clin Endocrinol Metab 2001;86:3787. PMID 11502812 (insomnia:
              higher cortisol, most in the evening and first half of the night)
  [DRAKE13]   Drake C et al. J Clin Sleep Med 2013;9:1195. PMID 24235903 (caffeine even 6 h before
              bed disrupts sleep)
  [EBRAHIM13] Ebrahim IO et al. Alcohol Clin Exp Res 2013;37:539. PMID 23347102 (alcohol: more
              broken sleep in the second half of the night, less REM)
  [OHAYON04]  Ohayon MM et al. Sleep 2004;27:1255. PMID 15586779 (normal adult sleep stages; deep
              sleep falls and wake-ups rise with age)
  [NHLBI]     NHLBI, Insomnia: Causes and Risk Factors (2022): caffeine, nicotine, alcohol,
              irregular schedules and shift work, stress, pain, hot flashes, sleep apnea, and
              medicines such as decongestants and steroids.
  [AASMHAB]   AASM sleepeducation.org, Healthy Sleep Habits: consistent schedule, bed only for
              sleep, out of bed if not asleep in about 20 minutes, screens off before bed, cool,
              dark, quiet room, no caffeine late or alcohol before bed.
  [BOYER05]   Boyer EW, Shannon M. The serotonin syndrome. N Engl J Med 2005;352:1112. PMID 15784664
              (L-tryptophan is among the drugs linked with serotonin syndrome).
  [ODSMG]     NIH Office of Dietary Supplements, Magnesium fact sheet (upper limit 350 mg/day from
              supplements, set because of diarrhea; kidney disease raises the risk of too much;
              bisphosphonates: take at least 2 hours apart; tetracycline and quinolone antibiotics: at
              least 2 hours before or 4-6 hours after a magnesium supplement).  ODS does not list
              thyroid pills; that spacing comes from [LT4LBL].  So the page says "at least 4 hours":
              one gap that meets all three rules.
  [LT4LBL]    Levothyroxine sodium tablets, FDA prescribing information (DailyMed; sections 2 and 7):
              give it at least 4 hours before or after agents that interfere with its absorption;
              antacids (aluminum and magnesium hydroxides), calcium carbonate and iron are listed.
              MedlinePlus Levothyroxine drug information (a682461) says the same for patients.
  [BORBELY82] Borbely AA. A two process model of sleep regulation. Hum Neurobiol 1982;1:195,
              PMID 7185792 (sleep pressure, "sleep drive", builds with time awake and is spent by
              sleep, naps included); applied in CBT-I sleep restriction [AASM21] (fixed wake time,
              no long naps).
  [EFSA23]    EFSA NDA Panel. EFSA J 2023;21(5):e08006. PMID 37207271 (vitamin B6 upper limit 12 mg a
              day for adults, set on peripheral neuropathy; the US limit is 100 mg a day, IOM 1998).
              GoodNight carries 40 mg B6 per 2 capsules and Mag Calm Pro 5 mg per scoop [LABELS], so the
              back says "Its B6 (up to 40 mg) adds up" with the tingling caution, the same caution the
              stress and neuropathy sheets carry.
  [SHARMA18]  Sharma AK et al. J Altern Complement Med 2018;24:243-8. PMID 28829155 (ashwagandha
              600 mg/d raised T3 and T4 and lowered TSH) -> "can raise thyroid levels".
  [ODSASH]    NIH ODS, Ashwagandha: Is it helpful for stress, anxiety, or sleep? (consumer fact sheet,
              seen through web search; ods.od.nih.gov is not reachable from the build machine): it may
              affect thyroid function, so it could interact with thyroid medicines, and it might
              interact with sedatives -> "add to sleep pills".  Same policy as the stress sheet's
              Cortisol Pro note (stress_cortisol.py rx).
  [LABELS]    NutriDyn sell sheets and the products DB, cited per product in products.d/sleep.json.
"""
import math
import os

from kit import icon
from svgkit import T, svg

SLUG = "sleep"

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


def tw(text, size, weight=600, ls=0.0):
    """Advance width of `text` in Inter at `size` px (falls back to a generous estimate)."""
    try:
        w = _face(_WEIGHTS[weight]).getlength(text) * size / 100
    except Exception:
        w = len(text) * size * (0.68 if text.isupper() else 0.6)
    return w + ls * len(text)


# ============================================================== palette (every symbol is in the KEY)
INK, INK2 = "#2B3236", "#56616A"
MEL, MEL_EDGE = "#2C4BA8", "#172F70"            # melatonin: blue dots and the blue band on the dial (the only blue)
COR, COR_EDGE, COR_TX = "#EAA828", "#B07A0C", "#7E5200"   # cortisol: gold band; darker gold for text
SUN, SUN_EDGE = "#FFD23F", "#E0A70F"            # daylight: yellow ray and sun
SIG = "#0F8A8F"                                 # day signal: teal dashed arrow, eye to clock (and the SCN dot)
AWAKE, REM, LITE, DEEP = "#E47C5C", "#7D55B9", "#7FB0E4", "#2E8A5D"   # sleep stages
# Night is dark gray, not navy, so that melatonin is the only blue on the dial: the night half of the
# ring, the dial's moon, the night signal (clock to pineal, with a moon badge) and the "at night" words.
NIGHT, DAY = "#3A3F4A", "#FCEBB1"               # the dial's night and day ring
VEIN, VEIN_EDGE = "#C9D2E8", "#8E9CC2"          # the vein melatonin rides in (named by "into blood")
# anatomy (named directly on the picture, not colour codes)
SKIN, SKIN_EDGE = "#F6E2D4", "#D7B49F"
BRAIN, BRAIN_EDGE, SULCUS = "#E9E4F2", "#A69EBF", "#C4BCD9"
STEM, CBL, CBL_LINE = "#DDD6EA", "#DAD3E9", "#B5ACCF"
THAL, CALLOSUM = "#D6CDE6", "#F7F4FB"
# optic nerve: a neutral nerve tone, NOT the daylight yellow (a yellow nerve read as light travelling
# through the head).  No pituitary is drawn: an unlabelled lavender blob under the clock only invited
# confusion with the SCN.
NERVE, NERVE_EDGE = "#EDE4D3", "#B3A285"
PINE, PINE_EDGE = "#E59A50", "#9C571C"


def _f(v):
    return f"{v:.1f}"


# ============================================================== curves
def _bezier_segments(pts, closed):
    """The cubic Bezier segments [(p0, c1, c2, p1)] of the Catmull-Rom curve through pts."""
    n = len(pts)

    def p(i):
        return pts[i % n] if closed else pts[max(0, min(n - 1, i))]

    tan = []
    for i in range(n):
        a, b, c = p(i - 1), p(i), p(i + 1)
        k = b[2] if len(b) > 2 else 1.0
        tan.append((k * (c[0] - a[0]) / 2, k * (c[1] - a[1]) / 2))
    segs = []
    for i in range(n if closed else n - 1):
        j = (i + 1) % n
        (xa, ya), (xb, yb) = pts[i][:2], pts[j][:2]
        segs.append(((xa, ya), (xa + tan[i][0] / 3, ya + tan[i][1] / 3), (xb - tan[j][0] / 3, yb - tan[j][1] / 3), (xb, yb)))
    return segs


def spline(pts, closed=True):
    """Catmull-Rom curve through pts [(x, y) or (x, y, tension)] as cubic Bezier path data.
    Low tension makes a sharper corner (used for the nose, lips and chin)."""
    d = [f"M{_f(pts[0][0])},{_f(pts[0][1])}"]
    for _, c1, c2, b in _bezier_segments(pts, closed):
        d.append(f"C{_f(c1[0])},{_f(c1[1])} {_f(c2[0])},{_f(c2[1])} {_f(b[0])},{_f(b[1])}")
    return "".join(d) + ("Z" if closed else "")


def spline_tail(pts, skip):
    """The open curve through pts, drawn from pts[skip] on: the skipped points only steer the start
    tangent, so it carries on another curve through the same points without a kink."""
    segs = _bezier_segments(pts, False)[skip:]
    d = [f"M{_f(segs[0][0][0])},{_f(segs[0][0][1])}"]
    for _, c1, c2, b in segs:
        d.append(f"C{_f(c1[0])},{_f(c1[1])} {_f(c2[0])},{_f(c2[1])} {_f(b[0])},{_f(b[1])}")
    return "".join(d)


def spline_at(pts, dists, closed=False, steps=60):
    """Points on the same curve at the given arc lengths from its start (beyond the end: the end)."""
    poly = []
    for a, c1, c2, b in _bezier_segments(pts, closed):
        for k in range(0 if not poly else 1, steps + 1):
            u = k / steps
            poly.append(tuple((1 - u) ** 3 * a[i] + 3 * (1 - u) ** 2 * u * c1[i] + 3 * (1 - u) * u * u * c2[i] + u ** 3 * b[i]
                              for i in (0, 1)))
    out, run, i = [], 0.0, 0
    for d in sorted(dists):
        while i < len(poly) - 1 and run + math.dist(poly[i], poly[i + 1]) < d:
            run += math.dist(poly[i], poly[i + 1])
            i += 1
        if i >= len(poly) - 1:
            out.append(poly[-1])
            continue
        seg = math.dist(poly[i], poly[i + 1]) or 1
        t = (d - run) / seg
        out.append((poly[i][0] + (poly[i + 1][0] - poly[i][0]) * t, poly[i][1] + (poly[i + 1][1] - poly[i][1]) * t))
    return out


def _arrowhead(x, y, ux, uy, size, color):
    """Filled triangle with its tip at (x, y) pointing along the unit vector (ux, uy)."""
    bx, by = x - ux * size, y - uy * size
    px, py = -uy * size * 0.55, ux * size * 0.55
    return (f'<path d="M{_f(x)},{_f(y)} L{_f(bx + px)},{_f(by + py)} L{_f(bx - px)},{_f(by - py)} Z" '
            f'fill="{color}"/>')


def signal_arrow(p0, c, p1, color=SIG, sw=2.0, head=6.5):
    """Dashed quadratic curve p0 -> p1 (control c) ending in an arrowhead at p1 (nerve signal)."""
    ex, ey = p1[0] - c[0], p1[1] - c[1]
    m = math.hypot(ex, ey) or 1
    ux, uy = ex / m, ey / m
    end = (p1[0] - ux * head * 0.8, p1[1] - uy * head * 0.8)
    return (f'<path d="M{_f(p0[0])},{_f(p0[1])} Q{_f(c[0])},{_f(c[1])} {_f(end[0])},{_f(end[1])}" fill="none" '
            f'stroke="{color}" stroke-width="{sw}" stroke-dasharray="4 3" stroke-linecap="round"/>'
            + _arrowhead(p1[0], p1[1], ux, uy, head, color))


# ============================================================== the head (local units, facing right)
# Proportions follow an adult profile: eyes at half the vertex-to-chin height, the face in thirds
# (brow, nose base, chin), ear behind the jaw, the eyeball recessed behind the brow and nose bridge.
HEAD_PTS = [
    (104, 330), (99, 292), (89, 262, 1.0), (72, 238), (57, 210), (49, 172), (50, 130), (63, 88),
    (91, 52), (133, 27), (182, 18), (230, 25), (264, 50), (281, 86), (287, 120, 0.8),
    (284, 139, 0.55), (279, 150, 0.35),                    # brow ridge, nose bridge (nasion)
    (289, 171, 0.9), (303, 194, 0.7), (306, 205, 0.4),     # nose ridge to the tip
    (296, 212, 0.5), (284, 214, 0.3),                      # under the nose
    (288, 225, 0.6), (288, 233, 0.45), (282, 238, 0.3),    # upper lip, mouth line
    (286, 245, 0.5), (280, 255, 0.4),                      # lower lip, the dip above the chin
    (284, 268, 0.8), (277, 283, 0.7), (260, 291, 0.9),     # chin, under the chin
    (242, 295, 0.9), (230, 303, 0.8), (225, 330),          # jaw underside, throat, front of the neck
]
# Cerebrum seen cut down the middle (medial surface): frontal pole on the right, occipital pole on the
# left, the lower edge running back along the eye socket roof, the base of the hypothalamus and the
# tentorium above the cerebellum.
BRAIN_PTS = [
    (205, 147, 0.8), (234, 142), (260, 133), (271, 114, 0.9), (269, 84), (253, 56), (222, 37),
    (180, 31), (135, 37), (98, 56), (72, 87), (61, 122), (65, 152, 0.9), (83, 166, 0.8),
    (117, 167, 0.8), (145, 158, 0.8), (161, 151, 0.7), (178, 152, 0.7), (191, 154, 0.7),
]
CEREBELLUM_PTS = [(151, 177), (147, 199), (136, 215), (114, 223), (90, 220), (72, 207), (66, 189), (76, 173),
                  (100, 166), (129, 168)]
STEM_PTS = [(147, 153), (178, 153), (183, 165), (191, 182), (191, 198), (181, 212), (169, 230), (163, 262),
            (160, 330), (141, 330), (143, 262), (147, 232), (151, 210), (152, 190), (149, 173)]
EYE_C, EYE_R = (252, 158), 13.0
CHIASM = (201, 151)
SCN_L = (197, 144)
PINEAL_L = (137, 124)
# The vein melatonin leaves by.  The pineal gland drains into the great cerebral vein and the straight
# sinus, which runs back along the border between the cerebrum and the cerebellum (the tentorium, drawn
# here as the cerebrum's lower edge, local y about 166-168 for x 80-120) to the confluence of sinuses at
# the internal occipital protuberance, on the inside of the back of the skull [BENARROCH08].  From there
# the blood runs sideways (transverse and sigmoid sinuses) to the jugular foramen and the internal jugular
# vein, all out of this midline plane, so the drawn vein STOPS at the confluence, inside the skull: it
# never leaves through the back of the skull or runs down the back of the neck.
VEIN_PTS = [(132, 129), (127.5, 147), (121, 163.3), (104, 166.8), (86, 167.6), (72, 168.2), (64.5, 170.6)]
VEIN_W = 4.4                     # local units (3.4 printed units at the head's 0.78 scale)
# Melatonin dots along the vein: every 12.6 local units (about 9.8 printed units) from 9.5 units.  The
# last of the 6 sits where the vein leaves the cerebellum's top; the vein runs on bare for about 21 units
# to the confluence, and that bare stretch is what "Melatonin into blood" points at (arc 82, inside the
# skull, 7 printed units clear of the last dot: a leader that ends on a dot reads as pointing at the dot).
MEL_DOTS = [9.5 + 12.6 * i for i in range(6)]
VEIN_LABEL_AT = spline_at(VEIN_PTS, [82.0])[0]
# The occipital bone: it carries the skull's bone rim on from the back of the cerebrum (it starts on the
# vault's own point (61, 122); the two points before it only steer its start, see spline_tail), over the
# confluence of sinuses (where the bone is thickest: the internal occipital protuberance), round the back
# and underside of the cerebellum along its outline, and on to the back edge of the foramen magnum,
# stopping about 5 units behind the brainstem so the spinal cord has its opening.
OCCIPITAL_PTS = [(98, 56), (72, 87), (61, 122), (61.8, 148), (63, 170), (65.9, 191), (70, 204), (82.2, 216),
                 (97, 222.3), (112, 224.6), (126, 225.6), (137, 226.2)]
OCCIPITAL_SKIP = 2
# The notch between the back of the cerebrum and the top of the cerebellum is the tentorium and the
# confluence of sinuses, against the thick internal occipital protuberance.  It is filled in the bone's
# own cream so the two bone strokes show no inner edge lines there.  Every edge of this polygon lies under
# the cerebrum or cerebellum (drawn later) or inside the bone's fill band, so it adds no outline of its own.
NOTCH_PTS = [(62, 140), (70, 150), (84, 163), (96, 166), (96, 170), (80, 174), (70, 184), (66.5, 192),
             (64.5, 192), (63.5, 170), (62.5, 150)]


def _head_local(uid):
    """The whole head drawing in local units (about 48..306 x 18..330)."""
    # The neck fades out from local y 284 to 308, fully clear 2 units above the card's step-strip divider
    # (ART_B = 258 printed = local 310.3), so the divider never slices a half-faded neck.
    o = [f'<defs><linearGradient id="{uid}fade" gradientUnits="userSpaceOnUse" x1="0" y1="284" x2="0" y2="308">'
         '<stop offset="0" stop-color="#fff"/><stop offset="1" stop-color="#000"/></linearGradient>'
         f'<mask id="{uid}mask" maskUnits="userSpaceOnUse" x="0" y="0" width="360" height="340">'
         f'<rect x="0" y="0" width="360" height="340" fill="url(#{uid}fade)"/></mask>'
         f'<radialGradient id="{uid}pine" cx=".4" cy=".35" r=".75"><stop offset="0" stop-color="#F8C58E"/>'
         f'<stop offset="1" stop-color="{PINE}"/></radialGradient>'
         f'<radialGradient id="{uid}eye" cx=".62" cy=".42" r=".7"><stop offset="0" stop-color="#FFFFFF"/>'
         '<stop offset="1" stop-color="#E4E8EC"/></radialGradient></defs>']
    o.append(f'<g mask="url(#{uid}mask)">')
    # skin silhouette
    o.append(f'<path d="{spline(HEAD_PTS, closed=False)} L104,330 Z" fill="{SKIN}" stroke="{SKIN_EDGE}" stroke-width="1.6"/>')
    # face details: eyebrow, nostril, mouth line
    o.append('<path d="M262,140 Q273,134.5 284,137.5" fill="none" stroke="#9A7564" stroke-width="2.6" stroke-linecap="round"/>'
             '<path d="M289,206 Q294,201.5 299,206.5" fill="none" stroke="#C3907A" stroke-width="1.5" stroke-linecap="round"/>'
             '<path d="M282.5,238 L275,237.2" fill="none" stroke="#C3907A" stroke-width="1.4" stroke-linecap="round"/>')
    # skull: a bone rim around the brain (drawn under the cerebrum and cerebellum, so only the outer half
    # shows): the vault round the cerebrum, then the occipital bone round the cerebellum (OCCIPITAL_PTS).
    # Both edge strokes go down before both fill strokes, so where the two paths overlap there is no seam.
    vault, occ = spline(BRAIN_PTS[1:15], closed=False), spline_tail(OCCIPITAL_PTS, OCCIPITAL_SKIP)
    o.append("".join(f'<path d="{d}" fill="none" stroke="#D8C2AF" stroke-width="12" stroke-linecap="round"/>' for d in (vault, occ))
             + "".join(f'<path d="{d}" fill="none" stroke="#F1E5D9" stroke-width="9.6" stroke-linecap="round"/>' for d in (vault, occ))
             + '<path d="M' + " L".join(f"{x},{y}" for x, y in NOTCH_PTS) + 'Z" fill="#F1E5D9"/>')
    # neck: vertebral bodies in front of the spinal cord (four: a fifth would sit wholly in the fade)
    for y0 in (240, 256, 272, 288):
        o.append(f'<rect x="166" y="{y0}" width="21" height="13" rx="3.5" fill="#F1E5D9" stroke="#D2BBA7" stroke-width="1"/>')
    # spinal cord and brainstem, cerebellum, cerebrum
    o.append(f'<path d="{spline(STEM_PTS)}" fill="{STEM}" stroke="{BRAIN_EDGE}" stroke-width="1.2"/>')
    o.append(f'<path d="{spline(CEREBELLUM_PTS)}" fill="{CBL}" stroke="{BRAIN_EDGE}" stroke-width="1.2"/>')
    for k, (a, b, c) in enumerate([((146, 186), (110, 166), (72, 186)), ((143, 197), (108, 179), (69, 198)),
                                   ((138, 207), (106, 193), (75, 209)), ((128, 215), (104, 205), (84, 216))]):
        o.append(f'<path d="M{a[0]},{a[1]} Q{b[0]},{b[1]} {c[0]},{c[1]}" fill="none" stroke="{CBL_LINE}" stroke-width="1.1"/>')
    o.append(f'<path d="{spline(BRAIN_PTS)}" fill="{BRAIN}" stroke="{BRAIN_EDGE}" stroke-width="1.4"/>')
    # medial sulci: cingulate (follows the corpus callosum), central, parieto-occipital, calcarine, frontal
    for d in ("M232,113 C228,86 202,70 168,70 C140,70 118,82 110,104",
              "M166,33 C164,44 160,52 161,62",
              "M96,62 C104,80 108,96 113,113",
              "M64,136 C80,128 96,122 113,116",
              "M252,72 C244,82 238,92 236,104",
              "M206,38 C204,48 200,56 194,62",
              "M128,41 C132,52 136,60 136,70",
              "M232,44 C228,54 222,62 214,68",
              "M70,100 C78,104 86,110 92,118",
              "M266,108 C258,112 250,118 244,126"):
        o.append(f'<path d="{d}" fill="none" stroke="{SULCUS}" stroke-width="1.5" stroke-linecap="round"/>')
    # corpus callosum (the white bridge between the two halves), thalamus, hypothalamus floor
    o.append(f'<path d="M222,118 C226,104 214,92 194,90 C170,88 146,93 132,102 C124,107 122,115 128,118 '
             f'C136,121 140,113 150,108 C164,101 186,99 200,102 C210,104 214,111 212,118 Z" fill="{CALLOSUM}" '
             f'stroke="#B4ABCB" stroke-width="1.2"/>')
    o.append(f'<ellipse cx="170" cy="129" rx="21" ry="11.5" transform="rotate(-8 170 129)" fill="{THAL}" '
             f'stroke="#A79DC3" stroke-width="1.1"/>')
    # optic nerve: from the back of the eyeball to the optic chiasm
    o.append(f'<path d="M240,155.5 C226,153 214,150.5 203,148.5 L203,153.5 C214,155.5 226,158.5 240,161.5 Z" '
             f'fill="{NERVE}" stroke="{NERVE_EDGE}" stroke-width="1"/>')
    o.append(f'<ellipse cx="{CHIASM[0]}" cy="{CHIASM[1]}" rx="5.2" ry="3.6" fill="{NERVE}" stroke="{NERVE_EDGE}" stroke-width="1"/>')
    # the eye (eyeball, iris and pupil seen from the side, upper and lower lids)
    ex, ey = EYE_C
    o.append(f'<circle cx="{ex}" cy="{ey}" r="{EYE_R}" fill="url(#{uid}eye)" stroke="#AEB6BE" stroke-width="1.2"/>'
             f'<ellipse cx="{ex + 11.2}" cy="{ey}" rx="2.6" ry="6.8" fill="#5D8CCB" stroke="#3E6BA6" stroke-width=".8"/>'
             f'<ellipse cx="{ex + 12.3}" cy="{ey}" rx="1.2" ry="3.2" fill="#1E2A38"/>'
             f'<path d="M{ex + 4},{ey - 12.2} C{ex + 12},{ey - 12} {ex + 18},{ey - 9} {ex + 19},{ey - 4}" fill="none" '
             f'stroke="#C99A82" stroke-width="2.2" stroke-linecap="round"/>'
             f'<path d="M{ex + 5},{ey + 12.2} C{ex + 12},{ey + 12} {ex + 17},{ey + 9} {ex + 18.5},{ey + 4.5}" fill="none" '
             f'stroke="#C99A82" stroke-width="1.8" stroke-linecap="round"/>')
    # the vein (a two-tone tube, so it reads as a vessel and not as another nerve signal)
    vein = spline(VEIN_PTS, closed=False)
    o.append(f'<path d="{vein}" fill="none" stroke="{VEIN_EDGE}" stroke-width="{VEIN_W}" stroke-linecap="round"/>'
             f'<path d="{vein}" fill="none" stroke="{VEIN}" stroke-width="{VEIN_W - 1.8}" stroke-linecap="round"/>')
    # pineal gland: a small pine-cone shape behind the thalamus, under the back of the corpus callosum
    px, py = PINEAL_L
    o.append(f'<g transform="translate({px},{py}) rotate(18)">'
             f'<path d="M8,0 C6,-5 -2,-6 -8,-3 C-11,-1.5 -11,1.5 -8,3 C-2,6 6,5 8,0 Z" fill="url(#{uid}pine)" '
             f'stroke="{PINE_EDGE}" stroke-width="1"/>'
             '<path d="M3,-3.6 L1,0 L3,3.6 M-2,-4.4 L-4,0 L-2,4.4" fill="none" stroke="#B5692A" stroke-width=".8" opacity=".8"/>'
             '</g>')
    # SCN (the master clock): a teal dot with a white ring, sitting on top of the chiasm
    sx, sy = SCN_L
    o.append(f'<circle cx="{sx}" cy="{sy}" r="5.4" fill="#FFFFFF" opacity=".9"/>'
             f'<circle cx="{sx}" cy="{sy}" r="3.8" fill="{SIG}" stroke="#0B5F63" stroke-width=".9"/>')
    o.append("</g>")
    return "".join(o)


def head_art(tx, ty, s, uid="slp-h"):
    """Head drawn at main coordinates: local point (x, y) -> (tx + s*x, ty + s*y)."""
    def m(p):
        return (tx + s * p[0], ty + s * p[1])
    g = f'<g transform="translate({_f(tx)},{_f(ty)}) scale({s})">{_head_local(uid)}</g>'
    return g, m


# ============================================================== the 24-hour dial
def _theta(h):
    """Clock hour (0-24) to a dial angle in radians: noon at the top, time running clockwise."""
    return math.radians((h - 12) / 24 * 360)


def _polar(cx, cy, r, h):
    a = _theta(h)
    return cx + r * math.sin(a), cy - r * math.cos(a)


def _interp_periodic(knots, h):
    """Smooth periodic (24 h) interpolation through (hour, value) knots (Catmull-Rom)."""
    ks = sorted(knots)
    n = len(ks)
    h %= 24
    for i in range(n):
        h0, v0 = ks[i]
        h1, v1 = ks[(i + 1) % n]
        span = (h1 - h0) % 24 or 24
        if (h - h0) % 24 <= span:
            t = ((h - h0) % 24) / span
            vm, vp = ks[i - 1][1], ks[(i + 2) % n][1]
            m0, m1 = (v1 - vm) / 2, (vp - v0) / 2
            t2, t3 = t * t, t * t * t
            return (2 * t3 - 3 * t2 + 1) * v0 + (t3 - 2 * t2 + t) * m0 + (-2 * t3 + 3 * t2) * v1 + (t3 - t2) * m1
    return ks[0][1]


def melatonin_level(h):
    """0..1.  Low by day; rises from about 8:30 pm (dim-light onset, about 2 h before a 10:30 pm
    bedtime [DLMO]), peaks about 2-4 am, back near zero by about 8:30 am [ZISAPEL18]."""
    t = (h - 20.5) % 24            # hours since 8:30 pm
    if t > 12:
        return 0.0
    if t < 6.5:                    # 8:30 pm -> 3:00 am rise
        return 0.5 * (1 - math.cos(math.pi * t / 6.5))
    return 0.5 * (1 + math.cos(math.pi * (t - 6.5) / 5.5))   # 3:00 am -> 8:30 am fall


# Cortisol knots (relative): nadir near midnight, quiet until about 5:30 am, peak about 8:30 am,
# falling through the day [DEBONO09].
_COR_KNOTS = [(0, .05), (2, .07), (4, .2), (6, .6), (7.5, .92), (8.5, 1.0), (10, .84), (12, .62), (14, .46),
              (16, .35), (18, .25), (20, .15), (22, .08)]


def cortisol_level(h):
    return max(0.03, min(1.0, _interp_periodic(_COR_KNOTS, h)))


def _band(cx, cy, r, wmax, level, h0, h1, wmin=0.0, step=1 / 12):
    """Ring band of varying width around the dial from hour h0 to h1 (clockwise)."""
    span = (h1 - h0) % 24 or 24
    n = int(span / step) + 1
    outer, inner = [], []
    for i in range(n + 1):
        h = h0 + span * i / n
        w = max(wmin, wmax * level(h % 24))
        outer.append(_polar(cx, cy, r + w / 2, h))
        inner.append(_polar(cx, cy, r - w / 2, h))
    pts = outer + inner[::-1]
    return "M" + " L".join(f"{_f(x)},{_f(y)}" for x, y in pts) + "Z"


def _sun(x, y, r=6.5, rays=True):
    o = [f'<circle cx="{_f(x)}" cy="{_f(y)}" r="{r}" fill="{SUN}" stroke="{SUN_EDGE}" stroke-width="1"/>']
    if rays:
        for k in range(8):
            a = math.radians(k * 45)
            o.append(f'<path d="M{_f(x + (r + 2.6) * math.cos(a))},{_f(y + (r + 2.6) * math.sin(a))} '
                     f'L{_f(x + (r + 6.2) * math.cos(a))},{_f(y + (r + 6.2) * math.sin(a))}" stroke="{SUN_EDGE}" '
                     'stroke-width="1.6" stroke-linecap="round"/>')
    return "".join(o)


def _moon(x, y, r=7.0, fill=NIGHT):
    return (f'<path d="M{_f(x + r * .35)},{_f(y - r)} A{r},{r} 0 1 0 {_f(x + r * .95)},{_f(y + r * .5)} '
            f'A{r * .78:.1f},{r * .78:.1f} 0 1 1 {_f(x + r * .35)},{_f(y - r)} Z" fill="{fill}"/>')


def moon_badge(x, y, r=5.6):
    """A white disc with a night-coloured ring and crescent: rides on the night signal (art and KEY)."""
    return (f'<circle cx="{_f(x)}" cy="{_f(y)}" r="{r}" fill="#FFFFFF" stroke="{NIGHT}" stroke-width=".9"/>'
            + _moon(x - r * .08, y, r * .6, NIGHT))


def dial(cx, cy, R):
    o = []
    ring_w = 11
    # day/night ring, in 10-minute segments so dawn and dusk blend
    def mix(a, b, t):
        a, b = a.lstrip("#"), b.lstrip("#")
        return "#" + "".join(f"{round(int(a[i:i + 2], 16) * (1 - t) + int(b[i:i + 2], 16) * t):02X}" for i in (0, 2, 4))

    def daylight(h):     # 1 = full day, 0 = night; soft dawn 5:30-7:30 and dusk 6-8 pm
        if 7.5 <= h <= 18:
            return 1.0
        if 5.5 < h < 7.5:
            return (h - 5.5) / 2
        if 18 < h < 20:
            return 1 - (h - 18) / 2
        return 0.0
    for i in range(144):
        h0, h1 = i / 6, (i + 1) / 6
        c = mix(NIGHT, DAY, daylight((h0 + h1) / 2))
        a0, a1 = _polar(cx, cy, R, h0), _polar(cx, cy, R, h1 + 0.02)
        b0, b1 = _polar(cx, cy, R - ring_w, h0), _polar(cx, cy, R - ring_w, h1 + 0.02)
        o.append(f'<path d="M{_f(a0[0])},{_f(a0[1])} A{R},{R} 0 0 1 {_f(a1[0])},{_f(a1[1])} L{_f(b1[0])},{_f(b1[1])} '
                 f'A{R - ring_w},{R - ring_w} 0 0 0 {_f(b0[0])},{_f(b0[1])} Z" fill="{c}"/>')
    o.append(f'<circle cx="{cx}" cy="{cy}" r="{R - ring_w}" fill="#FFFFFF"/>')
    o.append(f'<circle cx="{cx}" cy="{cy}" r="{R}" fill="none" stroke="#C9D0D6" stroke-width="1.2"/>')
    # tiny stars in the night part of the ring
    for h in (21.3, 22.8, 0.4, 1.9, 3.4):
        x, y = _polar(cx, cy, R - ring_w / 2, h)
        o.append(f'<circle cx="{_f(x)}" cy="{_f(y)}" r="1.1" fill="#FFFFFF" opacity=".85"/>')
    # hour ticks
    for hh in range(24):
        major = hh % 6 == 0
        r0 = R - ring_w - (8 if major else 4.5)
        a, b = _polar(cx, cy, R - ring_w - 1.5, hh), _polar(cx, cy, r0, hh)
        o.append(f'<path d="M{_f(a[0])},{_f(a[1])} L{_f(b[0])},{_f(b[1])}" stroke="{"#7C868D" if major else "#B9C1C7"}" '
                 f'stroke-width="{1.6 if major else 1}" stroke-linecap="round"/>')
    # hormone bands: melatonin (outer track), cortisol (inner track)
    rm, rc = R - ring_w - 21, R - ring_w - 44
    o.append(f'<circle cx="{cx}" cy="{cy}" r="{rm}" fill="none" stroke="#E6E9F2" stroke-width="1" stroke-dasharray="2 3"/>'
             f'<circle cx="{cx}" cy="{cy}" r="{rc}" fill="none" stroke="#F1E6CF" stroke-width="1" stroke-dasharray="2 3"/>')
    o.append(f'<path d="{_band(cx, cy, rm, 17, melatonin_level, 20.4, 8.6)}" fill="{MEL}" stroke="{MEL_EDGE}" '
             'stroke-width=".7" stroke-linejoin="round"/>')
    o.append(f'<path d="{_band(cx, cy, rc, 15, cortisol_level, 0, 24, wmin=1.4)}" fill="{COR}" stroke="{COR_EDGE}" '
             'stroke-width=".6" stroke-linejoin="round"/>')
    # centre: sun above (day half), moon below (night half, in the night colour)
    o.append(_sun(cx, cy - 12, 5.2) + _moon(cx - 1, cy + 13, 6.4, NIGHT))
    # hour labels
    lab = lambda x, y, t, a="middle": T(_f(x), _f(y), t, 10.2, 800, "#4D585F", a, ls=0.6)
    o.append(lab(cx, cy - R - 7, "NOON") + lab(cx, cy + R + 16, "MIDNIGHT")
             + lab(cx - R - 7, cy + 3.6, "6 AM", "end") + lab(cx + R + 7, cy + 3.6, "6 PM", "start"))
    return "".join(o), rm, rc


# ============================================================== small parts
def marker(x, y, n, r=8.4, fill="#FFFFFF", ink=INK):
    return (f'<circle cx="{_f(x)}" cy="{_f(y)}" r="{r}" fill="{fill}" stroke="{ink}" stroke-width="1.5"/>'
            + T(_f(x), _f(y + 3.8), str(n), 10.8, 800, ink, "middle"))


def step_dot(x, y, n, fill, r=7.0):
    return (f'<circle cx="{_f(x)}" cy="{_f(y - 3.9)}" r="{r}" fill="{fill}"/>'
            + T(_f(x), _f(y), str(n), 10.2, 800, "#FFFFFF", "middle"))


def card(x, y, w, h, title, sub, uid, c1):
    """White card with a theme-coloured header bar, clipped to rounded corners."""
    return (f'<clipPath id="{uid}"><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="11"/></clipPath>'
            f'<g clip-path="url(#{uid})"><rect x="{x}" y="{y}" width="{w}" height="{h}" fill="#FFFFFF"/>'
            f'<rect x="{x}" y="{y}" width="{w}" height="24" fill="{c1}"/></g>'
            f'<rect x="{x + .6}" y="{y + .6}" width="{w - 1.2}" height="{h - 1.2}" rx="11" fill="none" stroke="#D3D9DE" stroke-width="1.2"/>'
            + T(x + 13, y + 16.6, title, 11.6, 900, "#FFFFFF", ls=0.9)
            + T(x + w - 13, y + 16.4, sub, 10.2, 600, "#E6EBF4", "end", italic=True))


# ============================================================== picture 1: clock
W = 760
LW, RX = 398, 410            # left card width, right card x
P1H = 314                    # card height (the 3-line step strip needs about 4.6 units clear top and bottom)
ART_B = 258                  # bottom of the drawing area; the step strip sits below
STEP_Y0, STEP_DY, STEP_R = 15.5, 15.8, 7.0   # strip baselines ART_B + 15.5 + i * 15.8; dot radius
# Cortisol leader: from 7.5 units right of its gloss ("the wake-up and") to the gold band at 9:30 am.
# Checked numerically, edge to edge with stroke widths: 5.9 units clear of the melatonin band (whose thin
# end is at 8:36 am) and 3.1 units clear of the nearest hour tick (9 am).
CORTISOL_LEADER_FROM, CORTISOL_LEADER_H = (RX + 104, 73.0), 9.5


def art_clock(t):
    c1 = t["c1"]
    # The picture is ONE frame, so the words carry the timing: light acts BY DAY (it switches melatonin
    # off and sets the clock), melatonin flows AT NIGHT [ZISAPEL18].  Sun = "by day", moon = "at night".
    o = [card(0, 0, LW, P1H, "YOUR BRAIN'S CLOCK", "light by day, melatonin by night", "slp-c1", c1),
         # "HORMONES", not "SIGNALS": the KEY's "Day signal" / "Night signal" are the arrows on the head,
         # while this card shows the two hormones, cortisol and melatonin.
         card(RX, 0, W - RX, P1H, "ONE DAY, TWO HORMONES", "your 24-hour rhythm", "slp-c2", c1)]

    # ---------------- left: the head
    hx, hy, s = 46.0, 16.0, 0.78
    g, m = head_art(hx, hy, s)
    o.append(f'<clipPath id="slp-hclip"><rect x="1" y="24" width="{LW - 2}" height="{ART_B - 24}"/></clipPath>'
             f'<g clip-path="url(#slp-hclip)">{g}</g>')
    eye_c, cornea = m(EYE_C), m((EYE_C[0] + 13.4, EYE_C[1]))
    scn, chi, pin = m(SCN_L), m(CHIASM), m(PINEAL_L)
    # daylight: sun and a beam converging on the cornea
    sun = (372, 84)
    ux, uy = cornea[0] - sun[0], cornea[1] - sun[1]
    L = math.hypot(ux, uy)
    ux, uy = ux / L, uy / L
    nx, ny = -uy, ux
    a0 = (sun[0] + ux * 16, sun[1] + uy * 16)
    beam = (f'M{_f(a0[0] + nx * 11)},{_f(a0[1] + ny * 11)} L{_f(cornea[0] + nx * 3.2)},{_f(cornea[1] + ny * 3.2)} '
            f'L{_f(cornea[0] - nx * 3.2)},{_f(cornea[1] - ny * 3.2)} L{_f(a0[0] - nx * 11)},{_f(a0[1] - ny * 11)} Z')
    o.append('<defs><linearGradient id="slp-beam" gradientUnits="userSpaceOnUse" '
             f'x1="{_f(a0[0])}" y1="{_f(a0[1])}" x2="{_f(cornea[0])}" y2="{_f(cornea[1])}">'
             f'<stop offset="0" stop-color="{SUN}" stop-opacity=".95"/><stop offset="1" stop-color="#FFE98C" stop-opacity=".75"/>'
             '</linearGradient></defs>')
    o.append(f'<path d="{beam}" fill="url(#slp-beam)" stroke="{SUN_EDGE}" stroke-width=".8" stroke-opacity=".6"/>')
    for off in (-5.5, 0, 5.5):
        p = (a0[0] + nx * off, a0[1] + ny * off)
        q = (cornea[0] + nx * off * 0.22 - ux * 6, cornea[1] + ny * off * 0.22 - uy * 6)
        o.append(f'<path d="M{_f(p[0])},{_f(p[1])} L{_f(q[0])},{_f(q[1])}" stroke="#FFFFFF" stroke-width="1" opacity=".7"/>')
    o.append(_sun(*sun, r=10.5))
    o.append(T(sun[0], 60, "by day", 10.4, 700, INK2, "middle", italic=True))
    # Two signals, two colours, two times.  BY DAY the teal day signal runs from the eye along the optic
    # nerve to the SCN; AT NIGHT the dark-gray night signal, with a moon badge near its start, runs from
    # the SCN to the pineal gland under the thalamus [BENARROCH08].
    back_eye = m((EYE_C[0] - 11, EYE_C[1] + 1))
    o.append(signal_arrow(back_eye, ((back_eye[0] + chi[0]) / 2, chi[1] + 3.5), (scn[0] + 4.2, scn[1] + 2.4), sw=1.8, head=5.6))
    n0, nc, n1 = (scn[0] - 4, scn[1] + 3), (scn[0] - 22, scn[1] + 22), (pin[0] + 4.6, pin[1] + 4.6)
    o.append(signal_arrow(n0, nc, n1, color=NIGHT, sw=1.8, head=5.6))
    bt = 0.24
    o.append(moon_badge((1 - bt) ** 2 * n0[0] + 2 * (1 - bt) * bt * nc[0] + bt ** 2 * n1[0],
                        (1 - bt) ** 2 * n0[1] + 2 * (1 - bt) * bt * nc[1] + bt ** 2 * n1[1]))
    # Melatonin leaving the pineal gland rides the vein (VEIN_PTS, drawn with the head): the third dot is
    # already on the border between cerebrum and cerebellum, the rest run back along it to the confluence
    # at the back of the skull, where the vein ends.  Dots every 12.6 local units (MEL_DOTS, about 9.8
    # printed units).
    for k, q in enumerate(spline_at(VEIN_PTS, MEL_DOTS)):
        x, y = m(q)
        o.append(f'<circle cx="{_f(x)}" cy="{_f(y)}" r="{2.9 if k < 2 else 2.6}" fill="{MEL}" stroke="#FFFFFF" '
                 'stroke-width=".7"/>')
    # labels in clear space, with leader lines.  "Daylight" sits 9.7 units inside the card edge and its
    # marker about 5 units under the beam.
    o.append(marker(330, 127, 1) + T(342, 131.2, "Daylight", 11.2, 800, INK))
    # Master clock: the leader runs up from marker 2, passes under the teal arrowhead and ends INSIDE the
    # clock dot, which is redrawn on top so the line plugs into the dot (not into the chiasm below it).
    mk = (300, 222)
    tip = (scn[0] - 1.2, scn[1] + 2.7)
    dx, dy = tip[0] - mk[0], tip[1] - mk[1]
    dl = math.hypot(dx, dy)
    st = (mk[0] + dx / dl * 9.4, mk[1] + dy / dl * 9.4)
    o.append(f'<path d="M{_f(st[0])},{_f(st[1])} L{_f(tip[0])},{_f(tip[1])}" stroke="#7A858C" stroke-width="1.1"/>'
             f'<circle cx="{_f(scn[0])}" cy="{_f(scn[1])}" r="{_f(5.4 * s)}" fill="#FFFFFF"/>'
             f'<circle cx="{_f(scn[0])}" cy="{_f(scn[1])}" r="{_f(3.8 * s)}" fill="{SIG}" stroke="#0B5F63" stroke-width=".7"/>')
    o.append(marker(*mk, 2) + T(mk[0] + 12, mk[1] + 4, "Master clock", 11.2, 800, INK)
             + T(mk[0] + 12, mk[1] + 18, "(SCN)", 10.6, 600, INK2))
    px0 = 80
    o.append(f'<path d="M{px0},{_f(pin[1] - 9)} L{_f(pin[0] - 5.5)},{_f(pin[1] - 4.6)}" stroke="#7A858C" stroke-width="1.1"/>'
             f'<circle cx="{_f(pin[0] - 5.5)}" cy="{_f(pin[1] - 4.6)}" r="1.6" fill="#7A858C"/>')
    o.append(marker(18, pin[1] - 16, 3) + T(30, pin[1] - 12, "Pineal", 11.2, 800, INK)
             + T(30, pin[1] + 2, "gland", 11.2, 800, INK))
    # "at night" (with a moon, in the night colour), then "Melatonin into blood"; the leader runs from the
    # label to the edge of the bare vein past the last dot (VEIN_LABEL_AT, inside the skull), so "into
    # blood" points at a blood vessel.  The block sits 13 units lower than the vein's level so the leader
    # meets the (nearly level) vein at about 37 degrees instead of lying along it; it stays 12+ units clear
    # of the back-of-head outline.
    my = pin[1] + 37.3                          # baseline of "at night"
    o.append(_moon(20.5, my - 3.8, 5.2, NIGHT) + T(29, my, "at night", 10.4, 700, NIGHT, italic=True))
    vx, vy = m(VEIN_LABEL_AT)
    lead0 = (73.5, my + 20.8)
    ux_, uy_ = vx - lead0[0], vy - lead0[1]
    ul = math.hypot(ux_, uy_)
    vend = (vx - ux_ / ul * (VEIN_W * s / 2 + 0.6), vy - uy_ / ul * (VEIN_W * s / 2 + 0.6))
    o.append(f'<path d="M{_f(lead0[0])},{_f(lead0[1])} L{_f(vend[0])},{_f(vend[1])}" stroke="#5E6C93" stroke-width="1.1"/>')
    o.append(T(14, my + 14.6, "Melatonin", 11, 800, MEL) + T(14, my + 27.8, "into blood", 10.4, 600, MEL, italic=True))

    # ---------------- right: the dial
    cx, cy, R = RX + 194, 141, 92
    d, rm, rc = dial(cx, cy, R)
    o.append(d)
    o.append(T(W - 12, 40, "Wider band", 10.2, 600, INK2, "end", italic=True)
             + T(W - 12, 52.5, "= more hormone", 10.2, 600, INK2, "end", italic=True))
    # callouts: cortisol (upper left), melatonin (lower left).  Cortisol gets its plain-words gloss here.
    # Its leader starts beside the gloss and aims at 9:30 am, where the gold band is still about 90% wide
    # [DEBONO09 peak about 8:30], so it passes clear of the thin end of the melatonin band (8:36 am).
    hc = CORTISOL_LEADER_H
    cpk = _polar(cx, cy, rc + 15 * cortisol_level(hc) / 2 + 0.8, hc)
    c0 = CORTISOL_LEADER_FROM
    o.append(f'<path d="M{_f(c0[0])},{_f(c0[1])} L{_f(cpk[0])},{_f(cpk[1])}" stroke="#8C7A52" stroke-width="1.1"/>'
             f'<circle cx="{_f(cpk[0])}" cy="{_f(cpk[1])}" r="1.7" fill="#8C7A52"/>')
    o.append(marker(RX + 20, 52, 4) + T(RX + 32, 56.2, "Cortisol", 11.4, 800, COR_TX)
             + T(RX + 12, 72, ["the wake-up and", "stress hormone,", "peaks soon", "after waking"], 10.4, 600, INK2,
                 lh=1.22))
    mpk = _polar(cx, cy, rm + 9, 3.0)
    o.append(f'<path d="M{RX + 98},{cy + 70} L{_f(mpk[0])},{_f(mpk[1])}" stroke="#5E6C93" stroke-width="1.1"/>'
             f'<circle cx="{_f(mpk[0])}" cy="{_f(mpk[1])}" r="1.7" fill="#5E6C93"/>')
    o.append(T(RX + 12, cy + 62, "Melatonin", 11.4, 800, MEL)
             + T(RX + 12, cy + 77, ["peaks about", "2 to 4 am"], 10.4, 600, INK2, lh=1.22))
    # the outer ring is a colour code too, so it is named here (lower right, clear of the ring and MIDNIGHT)
    o.append(T(W - 12, 204, "Outer ring:", 10.2, 700, INK2, "end")
             + T(W - 12, 217.4, ["yellow = day,", "dark gray = night"], 10.2, 600, INK2, "end", italic=True, lh=1.2))
    # time runs clockwise, like a clock: a small arrow outside the ring, 2:40 to 4:10 pm
    ra = R + 7.5
    a0, a1 = _polar(cx, cy, ra, 14 + 40 / 60), _polar(cx, cy, ra, 16 + 10 / 60)
    th = _theta(16 + 10 / 60)
    tx_, ty_ = math.cos(th), math.sin(th)       # clockwise tangent at the arrow tip
    o.append(f'<path d="M{_f(a0[0])},{_f(a0[1])} A{ra},{ra} 0 0 1 {_f(a1[0] - tx_ * 4)},{_f(a1[1] - ty_ * 4)}" '
             'fill="none" stroke="#8D979E" stroke-width="1.5" stroke-linecap="round"/>'
             + _arrowhead(a1[0] + tx_ * 1.5, a1[1] + ty_ * 1.5, tx_, ty_, 6, "#8D979E"))

    # ---------------- step strips (about 4.6 units clear above the first dot and below the last)
    o.append(f'<rect x="1.2" y="{ART_B}" width="{LW - 2.4}" height="{P1H - ART_B - 1.8}" fill="#FFFFFF"/>'
             f'<path d="M1,{ART_B} H{LW - 1} M{RX + 1},{ART_B} H{W - 1}" stroke="#E3E7EA" stroke-width="1"/>')
    left = ["Morning light sets your master clock and turns melatonin off.",
            "When it gets dark, the clock signals the pineal gland.",
            "The pineal gland releases melatonin, the body's night hormone."]
    for i, txt in enumerate(left):
        y = ART_B + STEP_Y0 + i * STEP_DY
        o.append(step_dot(16, y, i + 1, c1) + T(30, y, txt, 10.6, 600, INK))
    right = [("4", c1, "Before dawn, melatonin fades and cortisol rises."),
             ("!", "#B5452F", "Bright light late at night delays melatonin."),
             ("!", "#B5452F", "Stress can keep cortisol up at bedtime.")]
    for i, (n, c, txt) in enumerate(right):
        y = ART_B + STEP_Y0 + i * STEP_DY
        o.append(step_dot(RX + 16, y, n, c) + T(RX + 30, y, txt, 10.6, 600, INK))
    return svg(W, P1H, "".join(o),
               "Side view of the head. By day, light enters the eye and a teal day signal sets the master clock (SCN) "
               "above the optic chiasm, which keeps melatonin switched off. At night a dark-gray night signal runs from "
               "the clock to the pineal gland, which releases melatonin into a vein that carries it into the blood. "
               "Beside it, a 24-hour dial: melatonin rises in the evening and peaks at night; cortisol, the wake-up and "
               "stress hormone, rises before dawn and peaks after waking; the outer ring is yellow by day and dark gray "
               "by night.")


# ============================================================== picture 2: one night + key
# A typical adult night, minutes after lights out at 10:30 pm (0) to waking at 6:30 am (480):
# about 15 minutes to fall asleep, 5 cycles of about 90 minutes, deep sleep in the first cycles,
# REM periods growing toward morning, short wake-ups between cycles [OHAYON04; AASM manual].
# Totals: about 7.3 h asleep, REM 25%, deep 21%, light 55%, a typical young-to-middle-aged adult night
# [OHAYON04].  The two mid-night wake-ups are drawn 6 minutes long (5.5 units) so they print; real ones
# are often shorter and go unnoticed.
NIGHT_SEQ = [("W", 0, 15), ("L", 15, 35), ("D", 35, 75), ("L", 75, 87), ("R", 87, 95),
             ("L", 95, 115), ("D", 115, 150), ("L", 150, 167), ("R", 167, 185), ("W", 185, 191),
             ("L", 191, 215), ("D", 215, 230), ("L", 230, 253), ("R", 253, 275),
             ("L", 275, 337), ("R", 337, 365), ("W", 365, 371),
             ("L", 371, 426), ("R", 426, 458), ("L", 458, 465), ("W", 465, 480)]
CYCLES = [(15, 95), (95, 188), (188, 275), (275, 368), (368, 465)]
STAGES = {"W": ("Awake", AWAKE), "R": ("REM (dreams)", REM), "L": ("Light", LITE), "D": ("Deep", DEEP)}
ROW_Y = {"W": 45, "R": 59.5, "L": 74, "D": 88.5}
BAND_Y0, BAND_Y1 = 28.5, 96.5            # shaded cycle bands
AXIS_Y = 107.8                           # time-axis baseline: 5 units clear of the card's bottom border
P2H, KEY_Y, KEY_H = 116, 121, 38   # the two-row key (38 units; the page-1 room comes from the Know panel)
CX0, CX1 = 118, 556          # chart x for minute 0 and minute 480


def _mx(minute):
    return CX0 + (CX1 - CX0) * minute / 480


def art_night(t):
    o = [card(0, 0, W, P2H, "ONE NIGHT OF SLEEP", "you cycle through these stages about every 90 minutes", "slp-c3", t["c1"])]
    # cycle bands and labels
    for i, (a, b) in enumerate(CYCLES):
        x0, x1 = _mx(a), _mx(b)
        if i % 2 == 0:
            o.append(f'<rect x="{_f(x0)}" y="{BAND_Y0}" width="{_f(x1 - x0)}" height="{BAND_Y1 - BAND_Y0}" rx="4" fill="#F3F5FA"/>')
        o.append(T(_f((x0 + x1) / 2), 36.4, f"Cycle {i + 1}", 10, 700, "#5E686F", "middle"))   # 5.7:1 on the band
    # row labels and guide lines
    for k in ("W", "R", "L", "D"):
        lab, col = STAGES[k]
        y = ROW_Y[k]
        o.append(f'<path d="M{CX0},{y} H{CX1}" stroke="#E7EAEE" stroke-width="1"/>')
        o.append(T(CX0 - 10, y + 3.7, lab, 10.6, 700, INK, "end"))
    # stepped connector, then the coloured stage bars on top
    path = []
    for i, (k, a, b) in enumerate(NIGHT_SEQ):
        y = ROW_Y[k]
        path.append(f"{'M' if i == 0 else 'L'}{_f(_mx(a))},{y} L{_f(_mx(b))},{y}")
    o.append(f'<path d="{" ".join(path)}" fill="none" stroke="#9AA4AB" stroke-width="1.2" stroke-linejoin="round"/>')
    for k, a, b in NIGHT_SEQ:
        x0, x1 = _mx(a), _mx(b)
        o.append(f'<rect x="{_f(x0)}" y="{ROW_Y[k] - 5}" width="{_f(max(x1 - x0, 5.0))}" height="10" rx="2.2" '
                 f'fill="{STAGES[k][1]}"/>')
    # time axis: short ticks (2.5 units) that stop 6 units above their labels
    for minute, lab in ((0, "10:30 pm"), (90, "midnight"), (210, "2 am"), (330, "4 am"), (480, "6:30 am")):
        x = _mx(minute)
        anchor = "start" if minute == 0 else ("end" if minute == 480 else "middle")
        o.append(f'<path d="M{_f(x)},{BAND_Y1} V{BAND_Y1 + 2.5}" stroke="#9AA4AB" stroke-width="1"/>'
                 + T(_f(x + (-2 if minute == 0 else 2 if minute == 480 else 0)), AXIS_Y, lab, 10, 600, INK2, anchor))
    # three notes, right of the chart
    nx = CX1 + 22
    notes = [(DEEP, ["Deep sleep comes mostly", "early in the night."]),
             (REM, ["REM (dream) sleep grows", "longer toward morning."]),
             (AWAKE, ["Short wake-ups between", "cycles are normal."])]
    for i, (c, lines) in enumerate(notes):
        y = 40 + i * 25.8
        o.append(f'<circle cx="{nx}" cy="{y - 3.6}" r="4" fill="{c}"/>' + T(nx + 10, y, lines, 10.4, 600, INK, lh=1.17))
    o.append(key_strip(KEY_Y))
    return svg(W, KEY_Y + KEY_H + 1, "".join(o),
               "One night of sleep for a typical adult: about 15 minutes to fall asleep, then five cycles of light, "
               "deep and REM sleep. Deep sleep comes mostly early in the night, REM grows longer toward morning, and "
               "short wake-ups between cycles are normal.")


# ============================================================== key
def _sw_beam():
    return (f'<path d="M-11,-5 L9,-1.6 L9,1.6 L-11,5 Z" fill="{SUN}" stroke="{SUN_EDGE}" stroke-width=".8"/>'
            f'<circle cx="-11" cy="0" r="4" fill="{SUN}" stroke="{SUN_EDGE}" stroke-width=".8"/>')


def _sw_signal():
    return (f'<path d="M-11,0 H4" stroke="{SIG}" stroke-width="2" stroke-dasharray="4 3" stroke-linecap="round"/>'
            + _arrowhead(11, 0, 1, 0, 6, SIG))


def _sw_night():
    """The night signal as drawn on the head: dark-gray dashes, arrowhead, moon badge near the start."""
    return (f'<path d="M-9,0 H4" stroke="{NIGHT}" stroke-width="2" stroke-dasharray="4 3" stroke-linecap="round"/>'
            + _arrowhead(11, 0, 1, 0, 6, NIGHT) + moon_badge(-8.2, 0, 4.9))


def _sw_mel():
    return (f'<rect x="-12" y="-3.5" width="14" height="7" rx="3.5" fill="{MEL}"/>'
            f'<circle cx="8.5" cy="0" r="3.4" fill="{MEL}" stroke="#FFFFFF" stroke-width=".7"/>')


def _sw_cor():
    return f'<path d="M-12,1.5 Q0,-8 12,1.5 Q0,-1 -12,1.5 Z" fill="{COR}" stroke="{COR_EDGE}" stroke-width=".6"/>'


def _sw_bar(c):
    return f'<rect x="-11" y="-5" width="22" height="10" rx="2.6" fill="{c}"/>'


# Two rows: the clock picture's symbols, then the sleep stages (nine entries do not fit one row at a
# readable size).  Columns line up across the rows; the last column ends flush with the strip's right pad.
KEY_ROWS = [[(_sw_beam, "Daylight"), (_sw_signal, "Day signal"), (_sw_night, "Night signal"), (_sw_mel, "Melatonin"),
             (_sw_cor, "Cortisol")],
            [(lambda: _sw_bar(AWAKE), "Awake"), (lambda: _sw_bar(REM), "REM sleep"),
             (lambda: _sw_bar(LITE), "Light sleep"), (lambda: _sw_bar(DEEP), "Deep sleep")]]
KEY_ROW_DY = 13.6                 # distance between the two row centres


def key_strip(y, w=W, h=KEY_H, fs=10.6):
    o = [f'<rect x=".6" y="{y}" width="{w - 1.2}" height="{h}" rx="8" fill="#FFFFFF" stroke="#CFD6DA" stroke-width="1.2"/>',
         T(13, y + h / 2 + 3.7, "KEY", 10.4, 800, INK, ls=1.3)]
    sw_w, gap = 24, 6
    ncol = max(len(r) for r in KEY_ROWS)
    colw = [max(sw_w + gap + tw(r[c][1], fs, 600) for r in KEY_ROWS if c < len(r)) for c in range(ncol)]
    x0, x1 = 50, w - 12
    space = (x1 - x0 - sum(colw)) / (ncol - 1)
    xs = [x0 + sum(colw[:c]) + space * c for c in range(ncol)]
    for r, row in enumerate(KEY_ROWS):
        cy = y + h / 2 + (r - (len(KEY_ROWS) - 1) / 2) * KEY_ROW_DY
        for c, (sw, lab) in enumerate(row):
            o.append(f'<g transform="translate({_f(xs[c] + sw_w / 2)},{_f(cy)})">{sw()}</g>')
            o.append(T(_f(xs[c] + sw_w + gap), _f(cy + 3.8), lab, fs, 600, INK))
    return "".join(o)


# ============================================================== HTML blocks under the art
_IC = {
    # this sheet's own line icons (64 x 64, stroked like kit.ICONS)
    "phone": '<rect x="19" y="8" width="24" height="46" rx="5"/><path d="M27 47h8"/><path d="M49 18l7-4M51 29h8M49 40l7 4"/>',
    "wine": '<path d="M21 8h22c0 14-5 22-11 22S21 22 21 8z"/><path d="M32 30v19M23 55h18"/><path d="M23 17h18"/>',
    # a sleeping head in profile: closed eye, open mouth, two sound arcs and one Z
    "snore": '<path d="M20 55C12 49 9 38 12 28C15 17 24 11 33 11C41 11 46 17 47 24L51 31L47.5 33V35.5"/>'
             '<path d="M47 40.5C47 45 43 47.5 39 47.5L37 55"/>'
             '<path d="M35 25.5C37 27.5 40 27.5 42 25.5"/>'
             '<path d="M53 35C55 37 55 39.5 53 41.5M57.5 31.5C61.5 35.5 61.5 41 57.5 45"/>'
             '<path d="M51 5.5H59L51 13.5H59"/>',
    "shift": '<circle cx="32" cy="34" r="20"/><path d="M32 22v12l8 5"/><path d="M14 10l-5 7M50 10l5 7"/>',
}


def _ico(name, size="0.32in", sw=2.8):
    if name in _IC:
        return (f'<svg class="ic" viewBox="0 0 64 64" style="width:{size};height:{size}" fill="none" stroke="currentColor" '
                f'stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{_IC[name]}</svg>')
    return icon(name, size, sw=sw)


RISKS = [  # [NHLBI]; caffeine [DRAKE13]; evening light [GOOLEY11, CHANG15]; alcohol [EBRAHIM13]; stress [VGONTZAS01]
    ("coffee", "Caffeine late<br>in the day"),
    ("phone", "Screens, bright<br>light at night"),
    ("wine", "Alcohol close<br>to bedtime"),
    ("shift", "Changing sleep<br>schedules"),
    ("brain", "Stress and a<br>racing mind"),
    # a flame (heat) for hot flashes, not a thermometer (which reads as fever or room temperature); the
    # kit's "headache" head would sit right beside the snoring head
    ("flame", "Hot flashes<br>or pain"),
    ("snore", "Loud snoring,<br>sleep apnea"),
    ("rx", "Decongestants,<br>some medicines"),
]


def risk_strip():
    cells = "".join(f'<div class="slp-rf"><span class="slp-disc">{_ico(ic)}</span><span class="slp-rl">{lab}</span></div>'
                    for ic, lab in RISKS)
    return f'<div class="slp-risk">{cells}</div>'


# STOP-Bang belongs to University Health Network (see the docstring): until NutriDyn has UHN's permission
# the sheet must not go to print.  If UHN says no, set APNEA_PANEL = "signs" and rebuild; the fallback was
# rendered in both editions on 2026-11-03 and fits the same box.
APNEA_PANEL = "stopbang"
APNEA_SIGNS = ["Loud snoring", "Sleepy or tired by day", "Gasping or breathing pauses in sleep",
               "High blood pressure", "Large collar size"]


def know_panel(mode=APNEA_PANEL):
    # [CDCNEED] hours of sleep by age, written with the CDC's own en-dash ranges so each row fits the
    # 1.3 in column on one line
    need = "".join(f'<div class="slp-age"><i>{a}</i><b>{b}</b></div>' for a, b in
                   (("Ages 18&ndash;60", "7+ hours"), ("Ages 61&ndash;64", "7&ndash;9 hours"),
                    ("Ages 65+", "7&ndash;8 hours")))
    # [ICSD3TR] chronic insomnia: all three parts.  The heading says "long-term" (chronic), because
    # trouble that lasts less than 3 months is short-term insomnia, which is still insomnia.
    ins = "".join(f'<li><span class="slp-bx"></span><span>{x}</span></li>' for x in (
        "Trouble falling or staying asleep, or waking too early",
        "3 or more nights a week, for 3+ months",
        "Your days suffer: tired, moody or foggy"))
    if mode == "signs":
        # Fallback if UHN does not give permission: generic warning signs in our own words, not scored and
        # not in questionnaire order [AASMOSA].  Ordered so the two-column grid reads row by row.
        apnea = (f'<div><h4>Sleep apnea warning signs</h4><ul class="slp-sb">'
                 + "".join(f'<li><span class="slp-bx"></span><span>{x}</span></li>' for x in APNEA_SIGNS)
                 + '</ul><p class="slp-act"><b>Any of these?</b> Ask about a sleep test (a doctor orders it).</p></div>')
        src = "Sources: CDC; AASM (ICSD-3-TR; sleep apnea guideline 2009); American College of Physicians 2016."
    else:
        # [STOPBANG] the eight yes/no items, in questionnaire order (Chung 2016 wording, shortened).
        # B is BMI > 35 kg/m2; most people do not know theirs, so the line says who can work it out.
        sb = [("S", "Snore loudly"), ("T", "Tired or sleepy by day"),
              ("O", "Seen to stop breathing or gasp"), ("P", "High blood pressure, or pills for it"),
              ("B", "BMI over 35 (ask {who})"), ("A", "Age over 50"),
              ("N", "Collar 17 in+ (men), 16 in+ (women)"), ("G", "Male")]
        sbl = "".join(f'<li><span class="slp-bx"></span><em>{a}</em><span>{b}</span></li>' for a, b in sb)
        # Both editions: say who orders the sleep study (a doctor; a pharmacist cannot) without sending the
        # reader away from the provider who handed out the sheet.  [STOPBANG] 3+ = intermediate/high risk.
        apnea = (f'<div><h4>Sleep apnea check <span>(STOP-Bang)</span></h4><ul class="slp-sb">{sbl}</ul>'
                 '<p class="slp-act"><b>3 or more ticks?</b> Ask about a sleep apnea test (a doctor orders it).</p></div>')
        # The owner is named in words ("property of"), never with a copyright glyph (Type 3 risk), and on the
        # same single line, because page 1 has under 5 px of slack above the footer.
        src = ("Sources: CDC; AASM (ICSD-3-TR); STOP-Bang (Chung 2016), property of University Health Network "
               "(stopbang.ca); American College of Physicians 2016.")
    return ('<div class="slp-know"><div class="slp-kh"><b>Know your sleep</b><span>Tick what fits you, then go over it '
            'with {who}.</span></div><div class="slp-kg">'
            f'<div><h4>How much sleep?</h4>{need}'
            '<div class="slp-mine"><span>My usual</span><i></i><span>hours</span></div></div>'
            f'<div><h4>Is it long-term insomnia?</h4><ul class="slp-ul">{ins}</ul>'
            # [ACP16, AASM21].  The same words as the back page's subtitle; no-break hyphens (the kit prints them
            # as plain hyphens in an unbreakable span) so "sleep-coaching" no longer splits at its hyphen.
            '<p class="slp-act"><b>All 3?</b> Ask about <b>CBT&#8209;I</b>, the sleep&#8209;coaching program experts '
            'recommend first.</p></div>'
            f'{apnea}</div><p class="slp-src">{src}</p></div>')


def front(t, ed):
    return ('<div class="slp">'
            f'<div class="slp-art">{art_clock(t)}</div>'
            f'<div class="slp-art slp-art2">{art_night(t)}</div>'
            '<h2 class="slp-h">What gets in the way of sleep</h2>'
            f'{risk_strip()}{know_panel()}</div>')


CSS = r"""
.slp .slp-art svg{display:block;width:100%;height:auto}
.slp .slp-art2{margin-top:0.07in}
.slp .slp-h{display:flex;align-items:center;gap:0.1in;font:900 10.5pt/1.2 Merriweather,Georgia,serif;color:var(--c1);
  letter-spacing:.04em;text-transform:uppercase;margin:0.08in 0 0.05in}
.slp .slp-h::after{content:"";flex:1;height:2px;border-radius:2px;background:linear-gradient(90deg,var(--soft),rgba(230,234,242,0))}
.slp .slp-risk{display:grid;grid-template-columns:repeat(8,1fr);gap:0 0.04in}
.slp .slp-rf{display:flex;flex-direction:column;align-items:center;text-align:center}
.slp .slp-disc{width:0.48in;height:0.48in;border-radius:50%;background:var(--soft);color:var(--c1);display:flex;
  align-items:center;justify-content:center;box-shadow:inset 0 0 0 1.5px rgba(61,78,107,.12)}
.slp .slp-rl{display:block;font-size:7.6pt;font-weight:600;line-height:1.2;color:#2F373C;margin-top:0.03in}
.slp .slp-know{margin-top:0.06in;border:1px solid #D9DFE8;border-radius:10px;padding:0.06in 0.12in 0.05in;background:#FFFFFF}
.slp .slp-kh{display:flex;align-items:baseline;gap:10px;margin:0 0 3px}
.slp .slp-kh b{font:900 11.5pt Merriweather,Georgia,serif;color:var(--c1)}
.slp .slp-kh span{font-size:7.8pt;color:#56626A}
/* The age column only needs about 1.25 in; the spare width goes to the STOP-Bang list, whose long items
   (O, B, N) sit in its left half, so B's "ask ..." gloss and the apnea line each stay on one line. */
.slp .slp-kg{display:grid;grid-template-columns:1.3in 2.3in 1fr;gap:0.14in;align-items:start}
.slp .slp-kg h4{margin:0 0 3px;font:800 8.1pt Inter,sans-serif;color:#2B3236;white-space:nowrap}
.slp .slp-kg h4 span{font-weight:600;color:#5E686F}
.slp .slp-age{display:flex;justify-content:space-between;align-items:baseline;gap:4px;background:var(--tint);
  border-left:3px solid var(--c2);border-radius:0 5px 5px 0;padding:1.5px 5px;margin:0 0 3px}
.slp .slp-age i{font-style:normal;font-size:7.3pt;color:#4A555C;white-space:nowrap}
.slp .slp-age b{font:800 7.8pt Inter,sans-serif;color:var(--deep);white-space:nowrap}
.slp .slp-mine{display:flex;align-items:center;gap:5px;font:700 7.3pt Inter,sans-serif;color:#4A555C;margin-top:4px}
.slp .slp-mine i{display:block;width:0.4in;height:0.21in;border-radius:5px;background:#E9ECEE;border:1px solid #D6DBDF}
.slp .slp-ul,.slp .slp-sb{list-style:none;margin:0;padding:0}
.slp .slp-ul li,.slp .slp-sb li{display:flex;align-items:flex-start;gap:5px;font-size:7.4pt;line-height:1.22;color:#2B3236;margin:0 0 2.5px}
.slp .slp-sb{display:grid;grid-template-columns:1.185fr .815fr;gap:0 0.08in}
.slp .slp-sb em{flex:none;font:800 7.4pt/1.22 Inter,sans-serif;font-style:normal;color:var(--c1);width:8px}
.slp .slp-sb li{gap:4.5px}
.slp .slp-bx{flex:none;width:0.115in;height:0.115in;border:1.5px solid var(--deep);border-radius:2px;background:#fff;margin-top:.5px}
.slp .slp-act{margin:2px 0 0;font-size:7.4pt;line-height:1.25;color:#2B3236;background:var(--soft);border-radius:5px;padding:2px 7px}
.slp .slp-act b{color:var(--deep)}
.slp .slp-src{margin:3px 0 0;font-size:7pt;color:#5E686F;line-height:1.3}
/* Back-page rules are scoped by the empty <i class="slp-bk"> in the band title (no other sheet carries it).
   The shared kit already sets all fine print to 7 pt, so this sheet no longer overrides it.
   Smaller habit discs give the bullets room, so the band does not grow. */
.sheet.back:has(.slp-bk) .life.l3 .disc2{width:0.64in;height:0.64in}
.sheet.back:has(.slp-bk) .life.l3 .disc2 svg{width:0.42in!important;height:0.42in!important}
/* the medicine check carries four notes, so it gets the wider part of the duo row: at 1.25 the pharmacy
   check is 11 lines and each rhythm slot is still wide enough for "Evening meal" on one line */
.sheet.back:has(.slp-bk) .duo{grid-template-columns:1fr 1.25fr}
/* the need headers hold two short lines, so they do not need the kit's 0.5 in minimum */
.sheet.back:has(.slp-bk) .col .need{min-height:0.44in}
"""

# ============================================================== the sheet
# Back-page check lines shared by both editions.  Each one was fitted on the rendered page: with these the
# pharmacy and practitioner checks are both 11 lines and the back keeps its 5.5 px above the footer.
# GoodNight: [BOYER05] tryptophan + serotonergic drugs; label drowsiness and driving caution [LABELS]; B6
# 40 mg per 2 capsules [LABELS ND521] (plus 5 mg per Mag Calm Pro scoop) against the 12 mg EFSA and 100 mg US
# upper limits, with the tingling caution the stress and neuropathy sheets carry [EFSA23].  "(up to 40 mg)"
# because the dose is 1 or 2 capsules.
_RX_GOODNIGHT = ("<b>Ask {who} before GoodNight</b> if you take antidepressants (SSRIs, SNRIs, MAOIs), migraine "
                 "triptans or sleep pills: its tryptophan adds to serotonin, and its melatonin and valerian add "
                 "drowsiness. Do not drive after taking it. Its B6 (up&nbsp;to&nbsp;40&nbsp;mg) adds up: tingling hands "
                 "or feet? Tell {who}.")
# Magnesium: one source, never both [LABELS]; the 350 mg supplement limit and kidney disease [ODSMG]; "at least
# 4 hours" meets the levothyroxine label's 4 hours [LT4LBL], ODS's 2 hours for bisphosphonates and its 2 hours
# before / 4-6 hours after for tetracycline and quinolone antibiotics [ODSMG].  No-break spaces keep "260 mg"
# and "350 mg" whole.
_RX_MAG = ("<b>Pick Mag Calm Pro (200&nbsp;mg magnesium) or Magnesium Glycinate (260&nbsp;mg), not both:</b> either "
           "stays under the 350&nbsp;mg daily limit for supplements. Kidney disease? Ask first. Keep it at least 4 hours "
           "from thyroid, bone or antibiotic pills.")
# Pregnancy and medicines: the three label cautions [LABELS]; Cortisol Pro's 150 mg Sensoril ashwagandha can
# raise thyroid hormone [SHARMA18] and may add to sedatives [ODSASH], the same note as the stress sheet.
_RX_PREG = ("<b>Pregnant, nursing or on medicine?</b> Ask {who} first. <b>No Cortisol Pro if pregnant.</b> Its "
            "ashwagandha can raise thyroid levels and add to sleep pills.")

SHEET = {
    "slug": SLUG, "code": "ND-NR-702", "order": 17, "theme": "neuro", "series": "Brain and Nerve Series",
    "title": "Better Sleep", "sub": "When falling asleep or staying asleep is hard",
    # "More than 1 in 3" < 7 h: [CDCFS] (BRFSS 2022, unchanged since 2013).  7+ h for adults: [CDCNEED].
    # Insomnia definition: [ICSD3TR].  Body clock, light and melatonin: [ZISAPEL18, BENARROCH08].
    "intro": ("Adults need <b>7 or more hours</b> of sleep, yet <b>more than 1 in 3</b> U.S. adults usually get less (CDC). "
              "<b>Insomnia</b> means trouble falling asleep, staying asleep, or waking too early, even with time to sleep. "
              "Sleep runs on a <b>body clock</b> in your brain: light sets it each morning, and the hormone "
              "<b>melatonin</b> tells your body that night has come."),
    "front": front,
    "css": CSS,
    "back": {
        # [AASM21] CBT-I parts (stimulus control, a regular wake time, relaxation), [AASMHAB] habits (bed for
        # sleep only, out of bed after about 20 minutes awake), [BORBELY82] sleep drive.  The subtitle names
        # CBT-I as coaching, not as something the products treat.
        "life_title": 'Reset Your Sleep Clock<i class="slp-bk"></i>',
        "life_sub": "Habits from CBT-I, the sleep-coaching program experts recommend first",
        "style": "circle3",
        # Morning bullet 3 is the morning half of stimulus control [AASM21, AASMHAB]: out of bed once awake,
        # because the bed is for sleep (the night column carries screens and the 20-minute rule).  Same two
        # lines as the bullet it replaced, so the band does not grow.
        "life": [("sun", "Morning: set the clock",
                  ["Get up at the same time every day, even after a rough night",
                   "Get outdoor light within an hour of waking",
                   "Once you wake, get up: your bed is for sleep"]),
                 # "walk" (an active day builds sleep drive), never the coffee cup page 1 uses as a sleep risk
                 ("walk", "Day: build sleep drive",
                  ["Sleep drive builds while you are awake; naps drain it",
                   "Skip naps, or keep them short and early",
                   "Caffeine in the morning only", "Move your body most days"]),
                 ("moon", "Night: wind down",
                  ["Dim lights and put screens away an hour before bed", "No alcohol or big meals late",
                   "A cool, dark, quiet bedroom",
                   "Awake 20 minutes? Get up. Go back to bed when sleepy"])],
        # Doses: every one is inside its label's directions [LABELS].  Magnesium is a choice, not a stack:
        # Mag Calm Pro (1 scoop, 200 mg) OR Magnesium Glycinate (2 capsules = one label serving, 260 mg; label:
        # 2 capsules twice daily); either one stays under the 350 mg supplement limit [ODSMG].  Magnesium
        # Glycinate has no rhythm entry of its own (sched []), so the plan counts one magnesium source; its column
        # says it replaces Mag Calm Pro, and the Mag Calm Pro cell in the rhythm names the swap ("1 scoop, or 2
        # Magnesium Glycinate capsules at bedtime"), so a patient who picks the capsules finds them in the plan.
        # The kit still counts that cell as the scoop, so the total reads "5 pills and 1 scoop".  L-theanine across
        # the plan: GoodNight 1 capsule 100 mg + Stress Essentials Calm
        # 200 mg + Mag Calm Pro 100 mg + Cortisol Pro 100 mg = 500 mg a day (600 mg with 2 GoodNight); it is not
        # printed, because the number alone tells a patient nothing.  GoodNight's label says one hour before
        # bedtime, so its rhythm line says so too.  Stress Essentials Calm sits at bedtime, matching its "wind-down
        # hours before bed" bullet (label: two capsules daily, no time of day given).
        # Claim bullets (starting "Supports" / "Helps") get the FDA diamond from the shared kit.
        "cols": [
            {"p": "sleep_goodnight", "need": "Ease into sleep", "needsub": "melatonin + calming herbs", "start": True,
             "bullets": ["Supports falling asleep and restful sleep",
                         "Melatonin plus lemon balm, hops and valerian"],
             "dose": "1 to 2 capsules", "dosesub": "1 hour before bed",
             "sched": [("bed", 1, "capsule, 1 hour before bed")]},
            {"p": "sleep_stress_calm", "need": "Quiet a busy mind", "needsub": "GABA + L-theanine",
             "bullets": ["Supports a calm, relaxed state of mind", "For the wind-down hours before bed"],
             "dose": "2 capsules", "dosesub": "before bed", "sched": [("bed", 2, "capsules")]},
            {"p": "sleep_mag_calm_pro", "need": "Evening wind-down", "needsub": "magnesium drink",
             "bullets": ["Supports relaxation and a calm mood", "Magnesium, inositol and taurine in one drink"],
             "dose": "1 scoop in 6 oz water", "dosesub": "after dinner",
             "sched": [("pm", 1, "scoop, or 2 Magnesium Glycinate capsules at bedtime")]},
            {"p": "sleep_mag_glycinate", "need": "Magnesium, no drink", "needsub": "instead of Mag Calm Pro",
             "bullets": ["Helps maintain normal muscle and nerve function", "Supports relaxation at bedtime"],
             "dose": "2 capsules", "dosesub": "at bedtime", "sched": []},
            {"p": "sleep_cortisol_pro", "need": "Handle daily stress", "needsub": "cortisol support",
             # the bottle's own claim ("Adaptogenic Support for Healthy Stress Response"); short enough that the
             # kit's FDA diamond stays on the line instead of wrapping onto a line of its own
             "bullets": ["Supports a healthy stress response", "Helps keep cortisol at healthy levels"],
             "dose": "2 capsules", "dosesub": "in the morning", "sched": [("am", 2, "capsules")]},
        ],
        # Label cautions [LABELS]: GoodNight "If you are pregnant, nursing, or taking medications such as SSRIs or
        # MAOIs consult your healthcare practitioner before use. May cause drowsiness. Use with caution if driving
        # or operating machinery."  Mag Calm Pro "If pregnant, nursing, or taking medication, consult your
        # healthcare practitioner before use."  Cortisol Pro "Do not use if pregnant. If nursing or taking
        # medication, consult your healthcare practitioner before use."  Bullet 4 carries all three (and covers
        # Calm and Magnesium Glycinate too).  [BOYER05] L-tryptophan + serotonergic drugs (antidepressants,
        # triptans).  [STOPBANG] apnea.  The four lines and their sources are in _RX_* just above SHEET; only
        # bullet 2 differs between the editions.
        "rx": {
            "pharmacy": [_RX_GOODNIGHT,
                         # a pharmacist goes over the check; a doctor orders the test
                         "<b>Snoring or gasping?</b> Go over the apnea check on page 1 with {who}. A doctor orders "
                         "the sleep test; supplements are no substitute for apnea care.",
                         _RX_MAG, _RX_PREG],
            "practitioner": [_RX_GOODNIGHT,
                             "<b>Loud snoring, gasping or sleepy days?</b> Ask {who} about a sleep apnea test (check on "
                             "page 1). Supplements are no substitute for apnea care.",
                             _RX_MAG, _RX_PREG],
        },
    },
}
