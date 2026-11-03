"""Muscle Cramps and Spasms (ND-MS-604), Pain and Movement Series.  slug "muscle-cramps".

Self-contained sheet module (no legacy sheets.py / art.py drawing code).  Built 2026-11-03, revised the same
day after an independent review (K2 retraction-and-replacement notice, magnesium grade, calcium message,
conditional products kept out of the daily plan, guarding angle for chiropractors, medicine checks), then polished
after a second review (back page fits again; no product tied to a cramp trial or a drug's side effect; kidney and
one-magnesium-at-a-time checks; the 2026 stockings-and-magnesium trial; heartburn pills; a guarding inset).

FRONT, top to bottom
  intro (cramp, spasm and guarding) -> "Contract, then let go": one picture that zooms in three steps
      YOUR CALF (lateral view of a lower leg: calf muscle, the deeper calf muscle, Achilles tendon, motor nerve,
      the red cramp knot), with a small GUARDING inset in its empty corner (the low back from behind: a back
      muscle beside the spine tightens to guard a joint)  ->  ONE MUSCLE FIBER (the nerve ending firing on a
      striped fiber, one thread of motors pulled out with the same stripe spacing, and the nerve's firing pattern:
      normal vs cramp)  ->  ONE TINY MOTOR (a sarcomere, RELAXED above and CONTRACTED below: calcium switches it
      on, ATP with magnesium's help switches it off)
  with a KEY for every symbol (the zoom ring and bracket included), a numbered 4-step strip, the common triggers,
  an honest "what the research says" panel and the get-checked red flags.
BACK: lifestyle band, five NutriDyn columns (Muscle Eze is Start here; Mag Calm Pro and Mag-K are swaps for it,
  CoQ10 is only for statin users, so none of those three is in the daily rhythm), daily rhythm (the empty Morning
  slot hidden) and the edition-specific medicine checks.

Every SVG id starts with "mc-" and every CSS class with "mcr-", so nothing collides with other sheets in the
all-sheets bundle.  Back-page CSS is scoped with BACK (the back <section> right after the front that holds
.mcr).  Text inside the SVG is never smaller than 10 viewBox units (the 760-unit art prints 7.66 in wide, so
10 units = 7.3 pt).

SOURCES (each fact on the page carries one of these tags in a comment beside it)
  [AAFP12]   Allen RE, Kirby KA. Nocturnal leg cramps. Am Fam Physician 2012;86(4):350-5. PMID 22963024.
             "Up to 60 percent of adults"; usually the calf; "probably caused by muscle fatigue and nerve
             dysfunction rather than electrolyte or other abnormalities"; linked conditions (vascular disease,
             lumbar stenosis, cirrhosis, hemodialysis, pregnancy) and medicines (IV iron sucrose, conjugated
             estrogens, raloxifene, naproxen, teriparatide); look-alikes: restless legs, CLAUDICATION, myositis,
             peripheral neuropathy; quinine no longer recommended.
  [MAISON16] Maisonneuve H et al. Prevalence of cramps in patients over the age of 60 in primary care.
             BMC Fam Pract 2016;17:111. PMID 27520635, doi:10.1186/s12875-016-0509-9 (46%; calves 80%).
  [MINETTO13] Minetto MA et al. Origin and development of muscle cramps. Exerc Sport Sci Rev 2013;41:3-10.
             PMID 23038243, doi:10.1097/JES.0b013e3182724817 (cramps come from motor-nerve over-excitability).
  [SCHW09]   Schwellnus MP. Cause of exercise associated muscle cramps. Br J Sports Med 2009;43:401-8.
             PMID 18981039, doi:10.1136/bjsm.2008.050401 (altered neuromuscular control with fatigue).
  [GARR12]   Garrison SR et al. Nocturnal leg cramps and prescription use that precedes them. Arch Intern Med
             2012;172:120-6. PMID 22157068, doi:10.1001/archinternmed.2011.1029. Adjusted sequence ratios:
             LABA inhalers 2.42, potassium-sparing diuretics 2.12, thiazide-like 1.48, loop 1.20 (P=.07),
             statins 1.16 ("statin and loop diuretic associations were small").
  [TAN24]    Tan J et al. Vitamin K2 in managing nocturnal leg cramps: a randomized clinical trial. JAMA Intern
             Med 2024;184(12):1443-7. PMID 39466236, doi:10.1001/jamainternmed.2024.5726. n=199, age 65+, MK-7
             180 mcg every night for 8 weeks; warfarin and diuretic users excluded; "vitamin K2 is not
             recommended for those undergoing warfarin therapy".  The ORIGINAL version printed a 95% CI of -2.86
             to -2.49 for the -2.67 difference; from its own SDs (1.41, 2.20) and n (103, 96) it should be about
             -3.19 to -2.15, one of the problems raised.
  [TAN25N]   Notice of Retraction and Replacement. Tan and Zhu. JAMA Intern Med 2025;185(7):904. PMID 40314950,
             doi:10.1001/jamainternmed.2025.2160. Retracted and replaced 2 May 2025 to fix errors in the
             intention-to-treat sample sizes after concerns raised by Avenell; the authors state the reduced-cramp
             finding remains (per web-search snippets; jamanetwork.com and ovid.com are blocked from this
             session, so the replacement's corrected numbers could NOT be read and none are printed).  DynaMed EBM
             Focus "Don't Jump at Vitamin K2 for Nocturnal Leg Cramps" questions the data (search snippet only).
             Still positive after the notice: Shaughnessy AF, AAFP POEM, Am Fam Physician 2025;112(2):217,
             PMID 40834386.  Hence the neutral EARLY tag and no numbers on the page.
  [COCH20]   Garrison SR et al. Magnesium for skeletal muscle cramps. Cochrane Database Syst Rev 2020;
             CD009402.pub3. PMID 32956536, doi:10.1002/14651858.CD009402.pub3: "unlikely that magnesium
             supplementation provides clinically meaningful cramp prophylaxis to older adults" (moderate to high
             certainty); pregnancy trials "conflicting"; no RCTs in exercise-associated cramps; GI side effects in
             11% to 37% of magnesium takers.
  [HALL12]   Hallegraeff JM et al. Stretching before sleep reduces the frequency and severity of nocturnal leg
             cramps in older adults. J Physiother 2012;58:17-22. PMID 22341378, doi:10.1016/S1836-9553(12)70068-1
             (n=80, over 55, calf AND hamstring stretches nightly for 6 weeks; not blinded).
  [COPPIN05] Coppin RJ et al. Managing nocturnal leg cramps: calf-stretching exercises and cessation of quinine
             treatment, a factorial RCT. Br J Gen Pract 2005;55:186-91. PMID 15808033 (191 patients: calf-only
             stretching "not effective in reducing the frequency or severity of night cramps").
  [KOVAC25]  Kovacic S et al. Effects of CoQ10 supplementation on myopathy in statin-treated patients. J Nutr Sci
             2025;14:e72. PMID 41158831, doi:10.1017/jns.2025.10043 (7 RCTs, 389 patients: small drop in muscle
             pain, WMD -0.96).
  [KENN20]   Kennedy C et al. Effect of CoQ10 on statin-associated myalgia and adherence. Atherosclerosis
             2020;299:1-8. PMID 32179207, doi:10.1016/j.atherosclerosis.2020.03.006 (7 RCTs, 321 patients: no
             benefit, WMD -0.42, 95% CI -1.47 to 0.62).
  [LAU19]    Lau WY et al. Water intake after dehydration makes muscles more susceptible to cramp but
             electrolytes reverse that effect. BMJ Open Sport Exerc Med 2019;5:e000478. PMID 30899546.
  [MAYO]     Mayo Clinic, Muscle cramp: symptoms and causes; diagnosis and treatment (causes: overuse,
             dehydration, holding a position a long time, low potassium, calcium or magnesium, diuretics;
             risk factors: age, dehydration, pregnancy, diabetes, nerve, liver or thyroid disorders; self-care:
             stretch and massage, heat; see a doctor for swelling, redness, weakness, frequent cramps).
  [SPASM]    Muscle guarding: a muscle tightens to protect an injured or painful back, neck or joint and stays
             tight (protective spasm), the main reason chiropractors give this sheet out (topic research, Asher's
             Academy booth plan: "Muscle Eze. Muscle guarding.").
  [ODS-MG]   NIH Office of Dietary Supplements, Magnesium fact sheet for health professionals (nerve impulse
             conduction and muscle contraction; UL 350 mg/day from supplements; separate magnesium from oral
             bisphosphonates by at least 2 hours; take tetracycline or quinolone antibiotics at least 2 hours
             before or 4 to 6 hours after magnesium; loop and thiazide diuretics raise magnesium loss,
             potassium-sparing diuretics lower it; proton pump inhibitors taken for a long time (usually over a
             year) can cause low magnesium; magnesium can build up when kidney function is impaired; food
             sources; low magnesium raises neuromuscular excitability, and muscle cramps are a sign of worsening
             deficiency).  The sheet was not re-opened this session (no host access); the PPI point is confirmed
             by [FDA-PPI].
  [FDA-PPI]  FDA Drug Safety Communication, 2 March 2011: prescription proton pump inhibitors may cause low serum
             magnesium if taken for a long time (in most cases over a year); low magnesium can cause muscle spasm
             (tetany), irregular heartbeat and seizures.  Read via drugs.com and Healio coverage of the notice
             (fda.gov/Drugs/DrugSafety/ucm245011.htm), web search 2026-11-03.
  [KUUS26]   Kuusipalo A et al. Secondary prevention of leg cramps using compression stockings or magnesium
             supplements: a three-arm randomized clinical trial. Trials 2026;27(1). PMID 41680812, PMC13005370,
             doi:10.1186/s13063-025-09370-z (full text read on PMC).  121 adults aged 50 to 85 with 2 or more leg
             cramps a week; 4 weeks of knee-high medical compression stockings (worn from waking to bedtime),
             magnesium hydrochloride (250 mg magnesium a day) or placebo pills.  Stockings vs placebo: -1.43 cramps a
             week (95% CI -2.36 to -0.50), fewer night wakings (-1.12), less pain; not blinded.  Magnesium vs placebo:
             -0.20 (95% CI -1.49 to 1.09), no benefit.  Excluded: diagnosed or suspected peripheral arterial disease,
             severe neuropathy, eGFR under 30, leg ulcers and other skin or leg problems.
  [CIPRO]    FDA ciprofloxacin label: take at least 2 hours before or 6 hours after products containing magnesium,
             calcium, iron or zinc.
  [LEVO]     FDA levothyroxine (Synthroid) label: take at least 4 hours apart from calcium carbonate and from
             magnesium-containing antacids.
  [ODS-K]    NIH ODS, Potassium fact sheet (ACE inhibitors, ARBs and potassium-sparing diuretics raise blood
             potassium; loop and thiazide diuretics lower it; food sources).
  [ODS-CA]   NIH ODS, Calcium fact sheet (low blood calcium raises nerve and muscle excitability).
  [ODS-VK]   NIH ODS, Vitamin K fact sheet (vitamin K and warfarin; MK-7 is long-acting; vitamin K activates
             bone proteins such as osteocalcin that bind calcium).
  [NCCIH]    NCCIH, Coenzyme Q10 (statins lower blood CoQ10; CoQ10 may make warfarin less effective).
  [FDA-ST]   FDA statin class labeling, Myopathy and Rhabdomyolysis (report unexplained muscle pain, tenderness
             or weakness promptly); MedlinePlus, Rhabdomyolysis (dark, red or cola-colored urine).
  [CDC-DVT]  CDC, Venous thromboembolism (blood clots): signs are swelling, pain, tenderness and redness of the leg.
  [LABEL]    Product labels (see products.d/muscle-cramps.json src): Muscle Eze and Mag Calm Pro "If pregnant,
             nursing, or taking medication, consult your healthcare practitioner"; Muscle Eze "may cause
             drowsiness", caution when driving; Vitamin K2 "one capsule daily with a meal or as directed by your
             healthcare practitioner".
  [PHYS]     Guyton and Hall Textbook of Medical Physiology, ch. 6, Contraction of skeletal muscle: the nerve
             signal (sodium in, potassium out) releases calcium; calcium lets myosin heads grab actin and pull;
             ATP releases the heads and powers the pump that returns calcium to storage (Mg-ATP is the working
             form); thick filaments keep their length while the sarcomere shortens.
"""
import math
import os

from kit import DIAMOND, ICONS
from svgkit import T, svg

SLUG = "muscle-cramps"


def _sf(text):
    """A claim bullet (structure/function) ending in the FDA diamond, drawn with kit.DIAMOND (never a font glyph).
    The diamond is glued to the bullet's last word inside an unbreakable span: an inline SVG is a line-break
    opportunity even after a no-break space, so without the glue it can wrap onto a line of its own.  Because
    these bullets carry their own mark, build.py adds none to this sheet's columns."""
    head, _, last = text.rpartition(" ")
    return f'{head} <span class="nw">{last}&nbsp;<span class="mark">{DIAMOND}</span></span>'

# =============================================================== text measuring
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


# =============================================================== palette (every coded colour is in the KEY)
INK, INK2 = "#23292D", "#56626A"
NERVE, NERVE_EDGE = "#F9D648", "#9A7000"          # yellow: nerve and its signal
CA, CA_EDGE = "#F2891D", "#9E5206"                # orange dot: calcium, the ON switch
MG, MG_EDGE = "#2EAD6B", "#15653D"                # green dot: magnesium, the OFF switch
NAK, NAK_EDGE = "#3F8FD8", "#1B5A95"              # blue drop: fluid and electrolytes (sodium, potassium)
ATP, ATP_EDGE = "#14A8B3", "#0A6870"              # teal bolt: ATP, the muscle's energy
ACT, ACT_A, ACT_B = "#EDB3AA", "#D6857A", "#F7CEC7"  # thin filament (actin): rose beads
MYO, MYO_HEAD, MYO_EDGE = "#6D4FA3", "#9A80CC", "#4A3274"  # thick filament (myosin): violet shaft + heads
ZLINE = "#2E4057"                                 # Z-line: the anchor at each end of a motor
KNOT = "#E1332C"                                  # red glow: the cramp knot
RED_TX, GREEN_TX, ORANGE_TX, ATP_TX = "#B42B24", "#17663F", "#A3540A", "#0A6870"
ZOOM_LINE = "#6F7C86"                             # white ring + grey lines: zooming in (keyed)
# anatomy (not coded, so not keyed)
SKIN_A, SKIN_B, SKIN_EDGE = "#FBE7DA", "#F1CDB8", "#C99579"
GAS_A, GAS_B, GAS_LN = "#D85B52", "#A93A35", "#7E2522"
SOL_A, SOL_B = "#C65A50", "#A23F38"
TEN, TEN_EDGE = "#F4E8D1", "#CDB68D"
FIB_A, FIB_I, FIB_Z, FIB_FACE = "#CF5F58", "#F2B7AE", "#9C3B37", "#B9433E"

W = 760
PB = (212, 26, 206, 250)          # panel B frame: x, y, w, h
PC = (426, 26, 330, 250)          # panel C frame
KEY_Y = 284


# =============================================================== small helpers
def _spline(pts, closed=False):
    """Catmull-Rom curve through pts as cubic Bezier path data (open curves keep their end points)."""
    n = len(pts)

    def p(i):
        return pts[i % n] if closed else pts[max(0, min(n - 1, i))]

    d = [f"M{pts[0][0]:.1f},{pts[0][1]:.1f}"]
    for i in range(n if closed else n - 1):
        p0, p1, p2, p3 = p(i - 1), p(i), p(i + 1), p(i + 2)
        c1 = (p1[0] + (p2[0] - p0[0]) / 6, p1[1] + (p2[1] - p0[1]) / 6)
        c2 = (p2[0] - (p3[0] - p1[0]) / 6, p2[1] - (p3[1] - p1[1]) / 6)
        d.append(f"C{c1[0]:.1f},{c1[1]:.1f} {c2[0]:.1f},{c2[1]:.1f} {p2[0]:.1f},{p2[1]:.1f}")
    return "".join(d) + ("Z" if closed else "")


def marker(x, y, n, ring=INK):
    """Numbered step marker (matches the numbered strip under the picture)."""
    return (f'<circle cx="{x}" cy="{y}" r="9.2" fill="#FFFFFF" stroke="{ring}" stroke-width="1.8"/>'
            + T(x, y + 4.1, str(n), 11.5, 800, ring, "middle"))


def ca_dot(x, y, r=3.4):
    return f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="{CA}" stroke="{CA_EDGE}" stroke-width="1"/>'


def mg_dot(x, y, r=3.4):
    return f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="{MG}" stroke="{MG_EDGE}" stroke-width="1"/>'


def drop(x, y, s=1.0):
    """Blue drop: fluid and electrolytes (sodium, potassium).  Point up, about 7 x 9.6 at s=1."""
    return (f'<path transform="translate({x:.1f},{y:.1f}) scale({s})" d="M0,-5.6 C1.6,-3.2 3.6,-1 3.6,1.4 '
            f'A3.6,3.6 0 0 1 -3.6,1.4 C-3.6,-1 -1.6,-3.2 0,-5.6Z" fill="{NAK}" stroke="{NAK_EDGE}" stroke-width=".9"/>')


def bolt(x, y, s=1.0):
    """Teal bolt: ATP, the muscle's energy.  About 7 x 11 at s=1."""
    return (f'<path transform="translate({x:.1f},{y:.1f}) scale({s})" d="M1.2,-5.6 L-3.2,0.8 L-0.2,0.8 '
            f'L-1.2,5.6 L3.2,-0.9 L0.2,-0.9 Z" fill="{ATP}" stroke="{ATP_EDGE}" stroke-width=".9" stroke-linejoin="round"/>')


def spark(x, y, r=6.5):
    """Yellow eight-point spark: the nerve signal arriving."""
    pts = []
    for i in range(16):
        a = math.pi * i / 8 - math.pi / 2
        rr = r if i % 2 == 0 else r * 0.45
        pts.append(f"{x + rr * math.cos(a):.1f},{y + rr * math.sin(a):.1f}")
    return f'<polygon points="{" ".join(pts)}" fill="{NERVE}" stroke="{NERVE_EDGE}" stroke-width="1" stroke-linejoin="round"/>'


def nerve_path(d, w=1.9):
    """A nerve: amber outline under a yellow core, so yellow still reads on a light background."""
    return (f'<path d="{d}" fill="none" stroke="{NERVE_EDGE}" stroke-width="{w + 1.9:.1f}" stroke-linecap="round" stroke-linejoin="round"/>'
            f'<path d="{d}" fill="none" stroke="{NERVE}" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round"/>')


def mc_defs(t):
    return ("<defs>"
            f'<linearGradient id="mc-skin" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="{SKIN_A}"/>'
            f'<stop offset="1" stop-color="{SKIN_B}"/></linearGradient>'
            f'<linearGradient id="mc-gas" x1="0" y1="0" x2="1" y2=".25"><stop offset="0" stop-color="{GAS_A}"/>'
            f'<stop offset="1" stop-color="{GAS_B}"/></linearGradient>'
            f'<linearGradient id="mc-sol" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="{SOL_A}"/>'
            f'<stop offset="1" stop-color="{SOL_B}"/></linearGradient>'
            '<radialGradient id="mc-knot"><stop offset="0" stop-color="#FF3B2F" stop-opacity=".95"/>'
            '<stop offset=".45" stop-color="#E1332C" stop-opacity=".62"/><stop offset="1" stop-color="#E1332C" stop-opacity="0"/></radialGradient>'
            '<linearGradient id="mc-cyl" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FFFFFF" stop-opacity=".42"/>'
            '<stop offset=".3" stop-color="#FFFFFF" stop-opacity="0"/><stop offset=".62" stop-color="#000000" stop-opacity="0"/>'
            '<stop offset="1" stop-color="#3A0C0A" stop-opacity=".34"/></linearGradient>'
            f'<linearGradient id="mc-rfade" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="{t["tint"]}" stop-opacity="0"/>'
            f'<stop offset="1" stop-color="{t["tint"]}"/></linearGradient>'
            "</defs>")


# =============================================================== panel A: the calf (lateral view, toes to the left)
S, HEEL_X, FLOOR = 4.7, 150.0, 274.0


def L(x, y):
    """Leg coordinates in cm (x = forward from the back of the heel, y = height off the floor) -> viewBox."""
    return (HEEL_X - x * S, FLOOR - y * S)


def Lp(pts):
    return [L(x, y) for x, y in pts]


# Adult proportions: knee crease about 49 cm up, foot 26.7 cm long, calf 13 cm deep, ankle 8 cm deep.
SKIN_PTS = [(12.0, 54.0), (12.5, 51.0), (12.45, 48.0), (11.95, 45.0), (11.55, 41.5), (11.1, 36.0), (10.8, 30.0),
            (10.55, 24.0), (10.4, 18.0), (10.45, 13.8), (11.1, 11.0), (12.8, 9.3), (15.5, 7.7), (18.8, 6.0),
            (21.6, 4.5), (23.7, 3.55), (25.1, 3.25), (26.25, 2.55), (26.75, 1.45), (26.35, 0.45), (25.1, 0.05),
            (21.5, 0.0), (16.0, 0.3), (10.0, 0.25), (5.0, 0.0), (1.8, 0.5), (0.35, 2.4), (0.15, 5.4), (0.9, 8.8),
            (1.6, 12.2), (1.75, 15.8), (1.1, 20.5), (-0.15, 26.0), (-1.15, 31.5), (-1.6, 36.5), (-1.3, 41.5),
            (-0.5, 45.5), (0.4, 48.6), (0.55, 51.4), (0.35, 54.0)]
# gastrocnemius, lateral head: the calf bulge, from behind the knee down to where it joins the tendon
GAS_PTS = [(2.0, 52.2), (0.75, 49.5), (-0.15, 45.6), (-0.95, 41.4), (-1.25, 36.6), (-0.85, 31.6), (0.1, 27.4),
           (1.3, 24.6), (2.6, 23.2), (3.8, 25.6), (5.0, 29.8), (5.9, 34.8), (6.25, 39.6), (6.05, 44.2),
           (5.2, 48.2), (3.7, 51.0)]
# soleus: the deeper calf muscle, showing in front of and below the gastrocnemius
SOL_PTS = [(6.0, 42.5), (7.4, 38.0), (8.05, 32.0), (7.9, 26.0), (7.0, 20.0), (5.4, 15.2), (3.8, 12.6),
           (3.0, 13.6), (2.7, 17.0), (3.0, 22.0), (4.2, 28.0), (5.2, 34.0), (5.6, 39.0)]
# Achilles tendon, from the calf muscles down to the heel bone
# (seen from the side it is only about 1 cm thick, widening a little where it joins the heel bone)
TEN_PTS = [(1.2, 23.4), (2.9, 23.2), (3.0, 19.0), (2.95, 15.0), (2.75, 11.0), (2.6, 7.5), (2.45, 4.6), (2.0, 3.6),
           (1.0, 3.8), (0.9, 6.5), (1.5, 9.8), (1.95, 13.5), (2.0, 16.5), (1.7, 20.0)]
LENS = (2.4, 46.0)
KNOT_C = (2.6, 36.6)


def panel_leg(t):
    o = []
    skin_d = _spline(Lp(SKIN_PTS)) + "Z"
    top = FLOOR - 54.0 * S
    # the leg is cut off above the knee: a mask fades the whole drawing out at the top
    o.append(f'<linearGradient id="mc-legfade" gradientUnits="userSpaceOnUse" x1="0" y1="{top:.1f}" x2="0" y2="{top + 22:.1f}">'
             '<stop offset="0" stop-color="#000"/><stop offset="1" stop-color="#FFF"/></linearGradient>'
             f'<mask id="mc-legmask" maskUnits="userSpaceOnUse" x="0" y="0" width="210" height="{FLOOR + 10:.0f}">'
             f'<rect x="0" y="0" width="210" height="{FLOOR + 10:.0f}" fill="url(#mc-legfade)"/></mask>')
    o.append('<g mask="url(#mc-legmask)">')
    o.append(f'<clipPath id="mc-legclip"><path d="{skin_d}"/></clipPath>')
    o.append(f'<path d="{skin_d}" fill="url(#mc-skin)"/>')
    o.append('<g clip-path="url(#mc-legclip)">')
    # outer ankle bone bump (lateral malleolus) and the knee cap, as soft shading
    mx, my = L(5.6, 9.2)
    o.append(f'<ellipse cx="{mx:.1f}" cy="{my:.1f}" rx="5.6" ry="4.6" fill="#E2B196" opacity=".5"/>')
    px, py = L(11.3, 49.8)
    o.append(f'<ellipse cx="{px:.1f}" cy="{py:.1f}" rx="5.5" ry="8.5" fill="#E8BFA6" opacity=".45"/>')
    # toes: a soft crease at the base of the toes and a nail at the tip
    a, b = L(22.6, 0.6), L(23.3, 3.1)
    o.append(f'<path d="M{a[0]:.1f},{a[1]:.1f} Q{a[0] - 3:.1f},{(a[1] + b[1]) / 2:.1f} {b[0]:.1f},{b[1]:.1f}" stroke="#D3A086" '
             'stroke-width="1" fill="none" opacity=".8"/>')
    n0, n1 = L(26.0, 2.45), L(24.9, 3.05)
    o.append(f'<path d="M{n0[0]:.1f},{n0[1]:.1f} Q{(n0[0] + n1[0]) / 2:.1f},{n1[1] - 1.6:.1f} {n1[0]:.1f},{n1[1]:.1f}" '
             'stroke="#D3A086" stroke-width="1.1" fill="none"/>')
    # soleus (deeper), then tendon, then the gastrocnemius on top
    sol_d = _spline(Lp(SOL_PTS), closed=True)
    o.append(f'<path d="{sol_d}" fill="url(#mc-sol)" stroke="#7A2622" stroke-width=".8" stroke-opacity=".5"/>')
    o.append(f'<clipPath id="mc-solclip"><path d="{sol_d}"/></clipPath><g clip-path="url(#mc-solclip)" '
             'stroke="#5C1714" stroke-opacity=".22" stroke-width="1" fill="none">')
    for y0 in (38.5, 34.5, 30.5, 26.5, 22.5, 18.5):          # feather-like fibres slanting into the tendon
        a, b = L(8.6, y0), L(2.6, y0 - 5.2)
        o.append(f'<path d="M{a[0]:.1f},{a[1]:.1f} L{b[0]:.1f},{b[1]:.1f}"/>')
    o.append("</g>")
    ten_d = _spline(Lp(TEN_PTS), closed=True)
    o.append(f'<path d="{ten_d}" fill="{TEN}" stroke="{TEN_EDGE}" stroke-width="1"/>')
    for f in (0.4,):
        a, b = L(1.75 + f * 1.0, 20.5), L(1.3 + f * 1.0, 5.0)
        o.append(f'<path d="M{a[0]:.1f},{a[1]:.1f} L{b[0]:.1f},{b[1]:.1f}" stroke="#D9C49E" stroke-width="1"/>')
    gas_d = _spline(Lp(GAS_PTS), closed=True)
    o.append(f'<path d="{gas_d}" fill="url(#mc-gas)" stroke="#741F1C" stroke-width=".9" stroke-opacity=".6"/>')
    o.append(f'<clipPath id="mc-gasclip"><path d="{gas_d}"/></clipPath><g clip-path="url(#mc-gasclip)" fill="none">')
    for k in range(7):                                         # fibres run from the knee down into the tendon
        f = (k + 0.5) / 7
        s0 = L(0.4 + f * 5.2, 51.6 - f * 0.8)
        c = L(-1.6 + f * 8.0, 37.5)
        e = L(1.8 + f * 1.6, 23.6 + f * 0.8)
        o.append(f'<path d="M{s0[0]:.1f},{s0[1]:.1f} Q{c[0]:.1f},{c[1]:.1f} {e[0]:.1f},{e[1]:.1f}" '
                 f'stroke="{GAS_LN}" stroke-opacity=".3" stroke-width="1.05"/>')
    hl = [L(-0.25, 45.0), L(-0.8, 39.5), L(-0.55, 33.5)]        # soft highlight along the bulge
    o.append(f'<path d="{_spline(hl)}" stroke="#FFFFFF" stroke-opacity=".3" stroke-width="2.6" stroke-linecap="round"/>')
    o.append("</g>")
    # the cramp knot (red glow) in the belly of the calf muscle
    kx, ky = L(*KNOT_C)
    o.append(f'<ellipse cx="{kx:.1f}" cy="{ky:.1f}" rx="17" ry="23" fill="url(#mc-knot)"/>')
    o.append("</g>")                                            # end leg clip
    # motor nerve (a tibial-nerve branch) entering the calf muscle from behind the knee
    a, b, c, d = L(2.5, 55.0), L(2.7, 51.0), L(2.8, 48.0), L(3.1, 41.8)
    br1, br2s, br2 = L(1.0, 43.6), L(2.95, 44.8), L(4.8, 41.6)
    o.append(nerve_path(f"M{a[0]:.1f},{a[1]:.1f} C{b[0]:.1f},{b[1]:.1f} {c[0]:.1f},{c[1]:.1f} {d[0]:.1f},{d[1]:.1f} "
                        f"M{c[0]:.1f},{c[1]:.1f} Q{L(1.7, 46.4)[0]:.1f},{L(1.7, 46.4)[1]:.1f} {br1[0]:.1f},{br1[1]:.1f} "
                        f"M{br2s[0]:.1f},{br2s[1]:.1f} Q{L(4.1, 43.9)[0]:.1f},{L(4.1, 43.9)[1]:.1f} {br2[0]:.1f},{br2[1]:.1f}", 1.5))
    o.append(f'<path d="{skin_d}" fill="none" stroke="{SKIN_EDGE}" stroke-width="1.3"/>')
    o.append("</g>")                                            # end fade mask
    return "".join(o)


GUARD = (3, 24, 82, 82)           # the guarding inset: x, y, w, h (panel A's empty top-left corner)


def guard_inset(t):
    """Muscle guarding [SPASM], for the chiropractors who hand this sheet out: the low back seen from behind.  Four
    lumbar vertebrae (body, two short wings, the spinous tab) with the long back muscles on either side; the right one
    is bunched and carries the same red knot glow as the calf (keyed "Cramp knot"), beside a spine joint.  Fills the
    empty corner left of the knee, clear of the panel title, the leg and the "Calf muscle" label."""
    x, y, w, h = GUARD
    cx = x + w / 2
    o = [f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="{t["tint"]}" stroke="#CBD9E4" stroke-width="1.2"/>',
         T(cx, y + 12.5, "GUARDING", 10.5, 800, t["deep"], "middle", ls=0.8)]
    top, bot = y + 17, y + 57                         # the picture's band, between the title and the caption
    mid = (top + bot) / 2

    def muscle(side, half):
        """A long back muscle (erector spinae): a smooth spindle beside the spine, `half` wide at its belly."""
        mx = cx + side * 13
        pts = [(mx, top), (mx + half * 0.55, top + 8), (mx + half, mid), (mx + half * 0.55, bot - 8), (mx, bot),
               (mx - half * 0.55, bot - 8), (mx - half, mid), (mx - half * 0.55, top + 8)]
        d = _spline(pts, closed=True)
        # Solid, pre-blended stroke colours (no stroke-opacity): in Chromium's PDF a gradient fill drawn right after a
        # translucent stroke came out at that stroke's opacity (the second muscle printed pale pink).
        fib = "".join(f'<path d="M{mx + k * half * 0.45:.1f},{top + 6} Q{mx + k * half * 0.75:.1f},{mid:.1f} '
                      f'{mx + k * half * 0.45:.1f},{bot - 6}" stroke="#A8443E" stroke-width=".9" fill="none"/>'
                      for k in (-1, 0, 1))
        return (f'<path d="{d}" fill="url(#mc-gas)" stroke="#8C3530" stroke-width=".9"/>' + fib)

    # four vertebrae with a pale disc between each pair.  Seen from behind, the long back muscles lie over the
    # vertebrae's side wings, so the wings go down first, then the muscles, then the bones and their midline tabs.
    step = (bot - top - 4) / 4
    rows = [top + 2 + step * (i + 0.5) for i in range(4)]
    for vy in rows:
        o.append(f'<rect x="{cx - 11:.1f}" y="{vy - 1.6:.1f}" width="22" height="3.2" rx="1.6" fill="{TEN}" '
                 f'stroke="{TEN_EDGE}" stroke-width=".8"/>')                       # the two wings
    o.append(muscle(-1, 4.6))                         # resting side
    o.append(muscle(1, 6.4))                          # guarding side: bunched up and tight
    for i, vy in enumerate(rows):
        if i:
            o.append(f'<rect x="{cx - 5.5:.1f}" y="{vy - step / 2 - 1:.1f}" width="11" height="2" rx="1" fill="#DCE5EC"/>')
        o.append(f'<rect x="{cx - 5.5:.1f}" y="{vy - 3.6:.1f}" width="11" height="7.2" rx="2.4" fill="{TEN}" '
                 f'stroke="{TEN_EDGE}" stroke-width=".9"/>')                       # the bone
        o.append(f'<ellipse cx="{cx:.1f}" cy="{vy:.1f}" rx="1.5" ry="2.3" fill="#E4D3B0"/>')   # the spinous tab
    # the guarding knot: next to the joint between the second and third vertebrae
    o.append(f'<ellipse cx="{cx + 12.5:.1f}" cy="{top + 2 + step * 2:.1f}" rx="8" ry="12" fill="url(#mc-knot)"/>')
    o.append(T(cx, y + h - 16, "Tightens to", 10, 600, INK, "middle"))
    o.append(T(cx, y + h - 5, "guard a joint", 10, 600, INK, "middle"))
    return "".join(o)


def lens_and_cone():
    lx, ly = L(*LENS)
    r = 11
    fx0, fy, fr = FIB[0], FIB[2], FIB[3]
    beam = (f'<path d="M{lx:.1f},{ly - r:.1f} L{fx0},{fy - fr} L{fx0},{fy + fr} L{lx:.1f},{ly + r:.1f} Z" '
            'fill="#FFFFFF" fill-opacity=".5"/>')
    lines = (f'<path d="M{lx:.1f},{ly - r:.1f} L{fx0},{fy - fr} M{lx:.1f},{ly + r:.1f} L{fx0},{fy + fr}" '
             'stroke="#6F7C86" stroke-width="1.1" stroke-opacity=".75" fill="none"/>')
    ring = (f'<circle cx="{lx:.1f}" cy="{ly:.1f}" r="{r}" fill="#FFFFFF" fill-opacity=".2" stroke="#FFFFFF" stroke-width="2.4"/>'
            f'<circle cx="{lx:.1f}" cy="{ly:.1f}" r="{r + 1.5}" fill="none" stroke="#2F2626" stroke-width=".9" stroke-opacity=".6"/>')
    return beam, lines + ring


# =============================================================== panel B: one muscle fiber
FIB = (240, 404, 90, 20)          # x0 (cut face), x1, centre y, radius
MYO_Y, MYO_R = 142, 6.5           # one myofibril, pulled out of the fiber
MYO_X0, MYO_X1, SARC = 250, 402, 24
ZB = (376, 400)                   # the bracketed sarcomere: Z-line to Z-line on the straight run


def fiber():
    x0, x1, cy, r = FIB
    o = [f'<clipPath id="mc-fibclip"><rect x="{x0}" y="{cy - r}" width="{x1 - x0}" height="{2 * r}"/></clipPath>',
         f'<rect x="{x0}" y="{cy - r}" width="{x1 - x0}" height="{2 * r}" fill="{FIB_I}"/>',
         '<g clip-path="url(#mc-fibclip)">']
    # striped: dark A bands, light I bands with a thin Z-line in the middle of each I band.  The stripe step is
    # SARC and the A band is 13 long, exactly as on the thread pulled out of this fiber, so the two match.
    x = x0 + 4
    while x < x1:
        o.append(f'<rect x="{x:.1f}" y="{cy - r}" width="13" height="{2 * r}" fill="{FIB_A}"/>')
        o.append(f'<path d="M{x + 18.5:.1f},{cy - r} V{cy + r}" stroke="{FIB_Z}" stroke-width="1.1" stroke-opacity=".75"/>')
        x += SARC
    o.append(f'<rect x="{x0}" y="{cy - r}" width="{x1 - x0}" height="{2 * r}" fill="url(#mc-cyl)"/>')
    o.append("</g>")
    o.append(f'<rect x="{x1 - 40}" y="{cy - r - 1}" width="42" height="{2 * r + 2}" fill="url(#mc-rfade)"/>')
    o.append(f'<path d="M{x0},{cy - r} H{x1 - 36} M{x0},{cy + r} H{x1 - 36}" stroke="#8E2E2A" stroke-width="1" stroke-opacity=".55"/>')
    # cut face: the threads (myofibrils) packed inside, seen end-on
    rx = 10.5
    o.append(f'<ellipse cx="{x0}" cy="{cy}" rx="{rx}" ry="{r}" fill="{FIB_FACE}" stroke="#7E2724" stroke-width="1"/>')
    sx = rx / r
    for row in range(-3, 4):
        yy = row * 5.6
        n = 4 if row % 2 else 3
        for j in range(-n, n + 1):
            xx = j * 5.6 + (2.8 if row % 2 else 0)
            if (xx / (r - 3)) ** 2 + (yy / (r - 3)) ** 2 <= 1:
                o.append(f'<ellipse cx="{x0 + xx * sx:.1f}" cy="{cy + yy:.1f}" rx="{2.3 * sx:.2f}" ry="2.3" fill="#F4C4BC" '
                         'stroke="#A2423D" stroke-width=".5"/>')
    return "".join(o)


def _cubic_len(p0, p1, p2, p3, n=200):
    """Arc length of a cubic Bezier, by sampling."""
    def at(t):
        u = 1 - t
        return (u ** 3 * p0[0] + 3 * u * u * t * p1[0] + 3 * u * t * t * p2[0] + t ** 3 * p3[0],
                u ** 3 * p0[1] + 3 * u * u * t * p1[1] + 3 * u * t * t * p2[1] + t ** 3 * p3[1])
    pts = [at(i / n) for i in range(n + 1)]
    return sum(math.hypot(b[0] - a[0], b[1] - a[1]) for a, b in zip(pts, pts[1:]))


def myofibril():
    """One thread (myofibril) leaves the fiber's cut face, bends down and runs straight.  It is ONE stroked path,
    banded with dash patterns, so the stripes (A bands, I bands, Z-lines) follow the bend."""
    x0, cy, r = FIB[0], FIB[2], FIB[3]
    y, rr = MYO_Y, MYO_R
    p0, p1, p2, p3 = (x0 - 1, cy + 9), (x0 - 15, cy + 24), (x0 - 10, y), (MYO_X0, y)
    lc = _cubic_len(p0, p1, p2, p3)
    d = (f"M{p0[0]},{p0[1]} C{p1[0]},{p1[1]} {p2[0]},{p2[1]} {p3[0]},{p3[1]} H{MYO_X1}")
    sz = lc + (ZB[0] - MYO_X0)            # arc length of a Z-line we want exactly at x = ZB[0]
    off_z = (0.8 - sz) % SARC              # Z-line dash (1.6 long) centred on sz
    off_a = (-(sz + 5.5)) % SARC           # A band (13 long) starts 5.5 after each Z-line
    w = 2 * rr
    o = [f'<path d="{d}" fill="none" stroke="#9C3B37" stroke-width="{w + 2}"/>',
         f'<path d="{d}" fill="none" stroke="{FIB_I}" stroke-width="{w}"/>',
         f'<path d="{d}" fill="none" stroke="{FIB_A}" stroke-width="{w}" stroke-dasharray="13 11" stroke-dashoffset="{off_a:.2f}"/>',
         f'<path d="{d}" fill="none" stroke="{FIB_Z}" stroke-width="{w}" stroke-dasharray="1.6 22.4" stroke-dashoffset="{off_z:.2f}"/>',
         f'<path d="{d}" fill="none" stroke="#FFFFFF" stroke-opacity=".22" stroke-width="{w * 0.32:.1f}" transform="translate(0,-2)"/>']
    return "".join(o)


def bracket_x():
    """The bracketed sarcomere: (left Z, right Z)."""
    return ZB


def trace(x0, x1, base, spikes, amp=13):
    """Nerve firing pattern: yellow spikes with an amber outline on a baseline."""
    d = [f"M{x0},{base}"]
    for sx in spikes:
        d.append(f"L{sx:.1f},{base} L{sx + 1.8:.1f},{base - amp} L{sx + 3.8:.1f},{base + 4} L{sx + 5.4:.1f},{base}")
    d.append(f"L{x1},{base}")
    return nerve_path(" ".join(d), 1.5)


def panel_fiber(t):
    bx, by, bw, bh = PB
    x0, x1, cy, r = FIB
    o = []
    o.append(fiber())
    o.append(myofibril())
    # motor nerve coming down to the fiber; the nerve ending (motor end plate) sits on its surface
    nx = 302
    o.append(nerve_path(f"M{nx + 8},{by - 0.5} C{nx + 8},{by + 18} {nx},{by + 22} {nx},{cy - r - 3}", 2.2))
    o.append(nerve_path(f"M{nx},{cy - r - 3} q-7,1.5 -11,4 M{nx},{cy - r - 3} q7,1.5 11,4 M{nx},{cy - r - 3} v4", 1.6))
    o.append(spark(nx, cy - r - 11, 7))
    for dx, dy, s in ((14, -24, .85), (28, -13, .95), (38, -22, .85)):   # sodium and potassium around the ending
        o.append(drop(nx + dx, cy - r + dy, s))
    o.append(T(bx + 10, by + 15, "Motor nerve", 10.5, 700, NERVE_EDGE))
    o.append(T(x1 - 2, by + 15, "Muscle fiber", 10.5, 700, "#8E2E2A", "end"))
    o.append(marker(nx - 22, cy - r - 12, 1))
    # bracket: one tiny motor (sarcomere) on the thread
    zl, zr = bracket_x()
    yb = MYO_Y - MYO_R - 5
    o.append(f'<path d="M{zl},{yb + 3} V{yb} H{zr} V{yb + 3}" fill="none" stroke="{INK}" stroke-width="1.4"/>')
    # The zoom beam to panel C rises from the bracket's right end and passes x 402 to 404 at this label's height, so
    # the label ends at x 397 (5 units clear of the line) instead of centring over the bracket.
    o.append(T(zr - 3, yb - 4, "1 motor", 10, 700, INK, "end"))
    o.append(T(MYO_X0 + 6, MYO_Y + MYO_R + 13, "a thread of tiny motors", 10, 600, INK2, italic=True))
    # firing pattern: normal vs cramp
    xa, xb = bx + 12, bx + bw - 22
    for (y0, label, tail, col, bg, spikes) in (
            (172, "NORMAL", "fires, then rests", INK, "#FFFFFF", [xa + 14 + i * 9 for i in range(5)]),
            (226, "CRAMP", "keeps firing", RED_TX, "#FDEEEC", [xa + 14 + i * 8.6 for i in range(17)])):
        o.append(f'<rect x="{xa}" y="{y0}" width="{xb - xa}" height="46" rx="8" fill="{bg}" stroke="#D5DEE5" stroke-width="1"/>')
        o.append(T(xa + 10, y0 + 15, label, 10.5, 800, col, ls=0.6))
        o.append(T(xa + 10 + tw(label, 10.5, 800, 0.6) + 5, y0 + 15, tail, 10.5, 600, INK2))
        o.append(trace(xa + 8, xb - 8, y0 + 35, spikes, 12))
    return "".join(o)


# =============================================================== panel C: one tiny motor (sarcomere)
XC = 591
ROW1, ROW2 = 86, 200
THIN = 92                          # thin-filament length from its Z-line
THICK = 72                         # half-length of a thick filament (it never changes length)
DY_THIN, DY_THICK = (-28, 0, 28), (-14, 14)


def zline(x, y):
    pts = []
    for i in range(13):
        pts.append(f"{x + (3 if i % 2 else -3):.1f},{y - 36 + i * 6:.1f}")
    return f'<polyline points="{" ".join(pts)}" fill="none" stroke="{ZLINE}" stroke-width="2.4" stroke-linejoin="round" stroke-linecap="round"/>'


def thin(xz, y, direction):
    """Thin filament (actin) from its Z-line at xz, running `direction` (+1 right, -1 left)."""
    x_end = xz + direction * THIN
    o = [f'<path d="M{xz},{y} H{x_end}" stroke="{ACT}" stroke-width="5.2" stroke-linecap="round"/>']
    n = int(THIN / 4.4)
    for i in range(n):
        x = xz + direction * (2.6 + i * 4.4)
        o.append(f'<circle cx="{x:.1f}" cy="{y - 1.3:.1f}" r="2.05" fill="{ACT_A}"/>')
        x2 = x + direction * 2.2
        if abs(x2 - xz) < THIN:
            o.append(f'<circle cx="{x2:.1f}" cy="{y + 1.3:.1f}" r="2.05" fill="{ACT_B}" stroke="{ACT_A}" stroke-width=".5"/>')
    return "".join(o)


def thick(y, contracted):
    """Thick filament (myosin): a shaft with heads on both halves (none in the middle bare zone)."""
    o = []
    heads = []
    for side in (-1, 1):
        for k in range(7):
            hx = XC + side * (16 + k * 9)
            for up in (-1, 1):
                if contracted:   # heads reach the thin filament and lean toward the middle (after the pull)
                    nx, ny = hx - side * 2.6, y + up * 7.6
                    ang = -side * up * 28
                else:            # heads cocked toward the Z-line, not touching
                    nx, ny = hx + side * 2.4, y + up * 5.2
                    ang = side * up * 30
                heads.append(f'<path d="M{hx},{y + up * 2.2} L{nx:.1f},{ny:.1f}" stroke="{MYO_EDGE}" stroke-width="1.5" stroke-linecap="round"/>'
                             f'<ellipse cx="{nx:.1f}" cy="{ny + up * 1.6:.1f}" rx="3.3" ry="2.1" fill="{MYO_HEAD}" stroke="{MYO_EDGE}" '
                             f'stroke-width=".8" transform="rotate({ang} {nx:.1f} {ny + up * 1.6:.1f})"/>')
    o.append(f'<path d="M{XC - THICK},{y} H{XC + THICK}" stroke="{MYO_EDGE}" stroke-width="6" stroke-linecap="round"/>')
    o.append(f'<path d="M{XC - THICK},{y} H{XC + THICK}" stroke="{MYO}" stroke-width="4.2" stroke-linecap="round"/>')
    o += heads
    return "".join(o)


def sarcomere(y, contracted):
    half = 104 if contracted else 130            # about 20% shorter when contracted
    zl, zr = XC - half, XC + half
    o = []
    for dy in DY_THIN:
        o.append(thin(zl, y + dy, 1))
        o.append(thin(zr, y + dy, -1))
    for dy in DY_THICK:
        o.append(thick(y + dy, contracted))
    o.append(zline(zl, y) + zline(zr, y))
    if contracted:                               # calcium sits on the thin filaments: switch ON
        for dy in DY_THIN:
            for k in range(4):
                o.append(ca_dot(zl + 16 + k * 22, y + dy))
                o.append(ca_dot(zr - 16 - k * 22, y + dy))
    else:                                        # magnesium and ATP: switch OFF, heads let go
        # drawn in the open light bands between each Z-line and the thick filaments, mirrored on both sides
        x_in = XC - THICK - 8                    # just outside the thick-filament ends
        for side in (-1, 1):
            for dx, dy, f in ((-24, -14, mg_dot), (-6, -14, bolt), (-24, 14, bolt), (-6, 14, mg_dot)):
                x = XC + side * (XC - (x_in + dx + 6))
                o.append(mg_dot(x, y + dy, 4.0) if f is mg_dot else bolt(x, y + dy, 1.22))
    return "".join(o)


def v_arrow(x, y_tail, y_tip, color, w=4.2):
    d = 1 if y_tip > y_tail else -1
    base = y_tip - d * 9
    return (f'<path d="M{x},{y_tail} V{base:.1f}" stroke="{color}" stroke-width="{w}" stroke-linecap="round"/>'
            f'<path d="M{x - 7},{base:.1f} L{x},{y_tip} L{x + 7},{base:.1f} Z" fill="{color}"/>')


def panel_sarcomere(t):
    cx, cy, cw, ch = PC
    o = []
    o.append(T(cx + 14, ROW1 - 46, "RELAXED", 11.5, 800, GREEN_TX, ls=0.6)
             + T(cx + 14 + tw("RELAXED", 11.5, 800, 0.6) + 6, ROW1 - 46, "the muscle lets go", 11, 600, INK2))
    o.append(sarcomere(ROW1, False))
    o.append(sarcomere(ROW2, True))
    # the switch: calcium turns it ON (down), magnesium + ATP turn it OFF (up)
    ya, yb = ROW1 + 44, ROW2 - 42
    xo, xg = cx + 56, cx + cw - 52
    o.append(v_arrow(xo, ya, yb, CA))
    o.append(marker(xo - 24, (ya + yb) / 2, 2))
    o.append(T(xo + 14, (ya + yb) / 2 - 2, "Calcium", 11.5, 800, ORANGE_TX) +
             T(xo + 14, (ya + yb) / 2 + 12, "switches it ON", 11, 600, INK))
    # ATP does the letting go (it frees the myosin heads and powers the calcium pump); magnesium helps, because
    # Mg-ATP is the working form [PHYS].  So the OFF arrow is ATP teal and ATP is named first.
    o.append(v_arrow(xg, yb, ya, ATP))
    o.append(marker(xg + 24, (ya + yb) / 2, 3))
    o.append(T(xg - 14, (ya + yb) / 2 - 2, "ATP + magnesium", 11.5, 800, ATP_TX, "end") +
             T(xg - 14, (ya + yb) / 2 + 12, "switch it OFF", 11, 600, INK, "end"))
    o.append(T(cx + 14, ROW2 + 52, "CONTRACTED", 11.5, 800, ORANGE_TX, ls=0.6)
             + T(cx + 14 + tw("CONTRACTED", 11.5, 800, 0.6) + 6, ROW2 + 52, "the muscle squeezes", 11, 600, INK2))
    o.append(T(cx + 14, ROW2 + 66, "A cramp is this squeeze, stuck ON.", 11, 700, RED_TX))
    return "".join(o)


def bracket_beam():
    zl, zr = bracket_x()
    cx, cy, cw, ch = PC
    y0, y1 = MYO_Y - MYO_R, MYO_Y + MYO_R
    beam = (f'<path d="M{zr},{y0} L{cx},{cy + 6} L{cx},{cy + ch - 6} L{zr},{y1} Z" fill="#FFFFFF" fill-opacity=".55"/>')
    lines = (f'<path d="M{zr},{y0} L{cx},{cy + 6} M{zr},{y1} L{cx},{cy + ch - 6}" stroke="#6F7C86" stroke-width="1.1" '
             'stroke-opacity=".75" fill="none"/>')
    return beam, lines


# =============================================================== key
def key_strip(y):
    """KEY: names every symbol and colour used in the picture.  Columns line up across both rows."""
    def thin_sw():
        return ('<path d="M-11,0 H11" stroke="' + ACT + '" stroke-width="5.2" stroke-linecap="round"/>'
                + "".join(f'<circle cx="{x}" cy="-1.3" r="2.05" fill="{ACT_A}"/>' for x in (-9, -4.6, -0.2, 4.2, 8.6))
                + "".join(f'<circle cx="{x}" cy="1.3" r="2.05" fill="{ACT_B}" stroke="{ACT_A}" stroke-width=".5"/>' for x in (-6.8, -2.4, 2, 6.4)))

    def thick_sw():
        hs = "".join(f'<path d="M{x},-2 L{x + 2},-5.6" stroke="{MYO_EDGE}" stroke-width="1.3"/>'
                     f'<ellipse cx="{x + 2.4}" cy="-7" rx="2.8" ry="1.8" fill="{MYO_HEAD}" stroke="{MYO_EDGE}" stroke-width=".7"/>'
                     for x in (-8, 0, 8))
        return (f'<path d="M-12,1 H12" stroke="{MYO_EDGE}" stroke-width="6" stroke-linecap="round"/>'
                f'<path d="M-12,1 H12" stroke="{MYO}" stroke-width="4.2" stroke-linecap="round"/>' + hs)

    def z_sw():
        pts = " ".join(f"{(3 if i % 2 else -3)},{-9 + i * 4.5}" for i in range(5))
        return f'<polyline points="{pts}" fill="none" stroke="{ZLINE}" stroke-width="2.2" stroke-linejoin="round"/>'

    def nerve_sw():
        return nerve_path("M-12,4 C-6,4 -4,0 2,0", 1.6) + spark(6, 0, 6)

    def knot_sw():
        return '<circle r="11" fill="url(#mc-knot)"/>'

    def zoom_sw():
        """The zoom device used twice in the picture: a white ring (calf to fiber) or a bracket (fiber to motor), each
        with grey lines opening out.  The swatch draws the ring and its lines."""
        return (f'<path d="M-6,-5.4 L13,-10 M-6,5.4 L13,10" stroke="{ZOOM_LINE}" stroke-width="1.1" stroke-opacity=".8"/>'
                f'<circle cx="-6" cy="0" r="6.4" fill="{SKIN_B}"/>'
                '<circle cx="-6" cy="0" r="4.6" fill="none" stroke="#FFFFFF" stroke-width="2.2"/>'
                '<circle cx="-6" cy="0" r="6.2" fill="none" stroke="#2F2626" stroke-width=".9" stroke-opacity=".6"/>')

    # Columns line up across the two rows, so each column pairs a long label with a short one (it only fits
    # the 760-unit width that way).  Calcium is ON, ATP is OFF, magnesium helps ATP [PHYS].  The zoom device is a
    # ring (calf to fiber) or a bracket (fiber to motor), each with lines opening out; "Ring or bracket + lines"
    # would leave no gap between the key's columns, and the swatch already draws the lines.
    rows = [[(nerve_sw, 13, "Nerve signal"), (lambda: ca_dot(0, 0, 4.2), 5, "Calcium: switch ON"),
             (lambda: bolt(0, 0, 1.15), 5, "ATP: energy, switch OFF"), (lambda: mg_dot(0, 0, 4.2), 5, "Magnesium: helps ATP"),
             (lambda: drop(0, 0.6, 1.15), 5, "Sodium, potassium")],
            [(knot_sw, 11, "Cramp knot"), (thin_sw, 12, "Thin filament (actin)"), (thick_sw, 12, "Thick filament (myosin)"),
             (zoom_sw, 13, "Ring or bracket: zoom in"), (z_sw, 4, "Z-line: the anchor")]]
    fs, gap_sw = 10.5, 6
    ncol = max(len(r) for r in rows)
    colw = [0.0] * ncol
    for r in rows:
        for c, (_, hw, lab) in enumerate(r):
            colw[c] = max(colw[c], 2 * hw + gap_sw + tw(lab, fs, 600))
    x0, x1, rh, top = 6, W - 6, 20, 8
    h = top * 2 + rh * len(rows)
    start = x0 + 14 + tw("KEY", 10.5, 800, 1.2) + 16
    space = (x1 - 12 - start - sum(colw)) / (ncol - 1)
    out = [f'<rect x="{x0}" y="{y}" width="{x1 - x0}" height="{h}" rx="8" fill="#FFFFFF" stroke="#CFD6DA" stroke-width="1.2"/>',
           T(x0 + 14, y + h / 2 + 3.8, "KEY", 10.5, 800, INK, ls=1.2),
           f'<path d="M{start - 9},{y + 8} V{y + h - 8}" stroke="#DDE2E5" stroke-width="1.2"/>']
    for ri, r in enumerate(rows):
        cyr = y + top + rh * ri + rh / 2
        x = start
        for c, (sw, hw, lab) in enumerate(r):
            out.append(f'<g transform="translate({x + hw:.1f},{cyr:.1f})">{sw()}</g>')
            out.append(T(round(x + 2 * hw + gap_sw, 1), round(cyr + 3.8, 1), lab, fs, 600, INK))
            x += colw[c] + space
    return "".join(out), h


# =============================================================== the whole picture
def art_cramp(t):
    bx, by, bw, bh = PB
    cx, cy, cw, ch = PC
    o = [mc_defs(t)]
    # panel titles
    o.append(T(96, 16, "YOUR CALF", 11.5, 800, t["deep"], "middle", ls=1.0))
    o.append(T(bx + bw / 2, 16, "ONE MUSCLE FIBER", 11.5, 800, t["deep"], "middle", ls=1.0))
    o.append(T(cx + cw / 2, 16, "ONE TINY MOTOR (SARCOMERE)", 11.5, 800, t["deep"], "middle", ls=1.0))
    # frames for the two magnified views
    for (x, y, w, h) in (PB, PC):
        o.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" fill="{t["tint"]}" stroke="#CBD9E4" stroke-width="1.2"/>')
    beam_a, lines_a = lens_and_cone()
    beam_b, lines_b = bracket_beam()
    o.append(guard_inset(t))
    o.append(beam_a)
    o.append(panel_leg(t))
    o.append(lines_a)
    o.append(beam_b)
    o.append(panel_fiber(t))
    o.append(lines_b)
    o.append(panel_sarcomere(t))
    # "Calf muscle" label in clear space in front of the shin, with a leader to the muscle
    gx, gy = L(4.9, 33.0)
    o.append(T(8, gy + 4, "Calf muscle", 11, 700, "#8E2E2A"))
    o.append(f'<path d="M{8 + tw("Calf muscle", 11, 700) + 4:.1f},{gy:.1f} H{gx:.1f}" stroke="{INK}" stroke-width="1.1"/>'
             f'<circle cx="{gx:.1f}" cy="{gy:.1f}" r="2.2" fill="{INK}"/>')
    # the darker strip is the soleus, the deeper calf muscle: label its lower part, below the calf bulge
    sx, sy = L(5.0, 19.2)
    o.append(T(8, sy - 2, "Deeper", 11, 700, "#7A2622") + T(8, sy + 11, "calf muscle", 11, 700, "#7A2622"))
    o.append(f'<path d="M{8 + tw("calf muscle", 11, 700) + 4:.1f},{sy + 7:.1f} L{sx - 9:.1f},{sy + 7:.1f} L{sx:.1f},{sy:.1f}" '
             f'stroke="{INK}" stroke-width="1.1" fill="none"/><circle cx="{sx:.1f}" cy="{sy:.1f}" r="2.2" fill="{INK}"/>')
    ax, ay = L(2.7, 11.6)
    o.append(T(8, ay + 4, "Achilles tendon", 11, 700, "#7A6648"))
    o.append(f'<path d="M{8 + tw("Achilles tendon", 11, 700) + 4:.1f},{ay:.1f} H{ax:.1f}" stroke="{INK}" stroke-width="1.1"/>'
             f'<circle cx="{ax:.1f}" cy="{ay:.1f}" r="2.2" fill="{INK}"/>')
    # step 4: the cramp knot
    kx, ky = L(*KNOT_C)
    o.append(f'<path d="M{kx + 14:.1f},{ky + 6:.1f} L{kx + 33:.1f},{ky + 16:.1f}" stroke="{RED_TX}" stroke-width="1.3"/>')
    o.append(marker(kx + 42, ky + 20, 4, RED_TX))
    key, kh = key_strip(KEY_Y)
    o.append(key)
    return svg(W, KEY_Y + kh + 2, "".join(o),
               "How a muscle tightens and lets go. Left: a calf muscle and the deeper calf muscle, with a red cramp knot "
               "and its motor nerve; a white ring and grey lines zoom in. Inset: guarding, the low back from behind, "
               "where a back muscle beside the spine tightens to guard a joint. Middle: one muscle fiber with the nerve "
               "ending firing on it, one thread of tiny motors, and the nerve's firing pattern, normal versus a cramp "
               "that keeps firing; a bracket and grey lines zoom in. Right: one tiny motor, a sarcomere, relaxed when "
               "ATP with magnesium's help lets go, and contracted with calcium.")


# =============================================================== blocks under the picture
STEPS = [  # [PHYS] for 1-3; [ODS-CA] [ODS-MG] enough blood calcium and magnesium keep nerves calm; [AAFP12] [SCHW09] [MINETTO13] for 4
    ("The nerve says &ldquo;squeeze.&rdquo;", "Sodium and potassium carry the signal into the muscle."),
    # inside the fiber calcium is the ON switch; in the blood, too little calcium or magnesium makes nerves over-fire,
    # which is why low calcium is a cramp trigger even though calcium switches the motor on
    ("Calcium switches it&nbsp;ON.", "Filaments grab and slide. In your blood, enough calcium and magnesium keep "
     "nerves calm; too little can set off cramps."),
    ("ATP switches it&nbsp;OFF.", "With magnesium&rsquo;s help, the filaments let go and calcium goes back into storage."),
    ("A cramp is the switch stuck&nbsp;ON.", "A tired or over-excited nerve keeps&nbsp;firing."),
]

# 64-grid stroke icons drawn for this sheet (kit.icon style)
IC = {
    "chair": '<path d="M20 8v26h22l2 22M20 34l-4 22M18 34h26"/><path d="M20 22h18"/>',
    "pregnant": ('<circle cx="31" cy="10" r="5"/><path d="M29 17c-3 4-4 10-3 16l2 23M33 17c3 3 4 7 4 11 6 2 9 7 8 13'
                 '-1 5-5 7-10 7l1 8"/>'),
    # a blood tube with a low level and a down arrow: low mineral levels (no tiny element letters to print)
    "lowlevels": ('<path d="M20 8v34a8 8 0 0 0 16 0V8"/><path d="M16 8h24"/><path d="M20 36h16"/>'
                  '<path d="M50 13v30"/><path d="M43 36l7 7 7-7"/>'),
    "sweat": ('<circle cx="40" cy="20" r="8"/><path d="M40 4v4M40 32v4M24 20h4M52 20h4M29 9l3 3M48 28l3 3M29 31l3-3M48 12l3-3"/>'
              '<path d="M18 30c-4 7-8 11-8 16a8 8 0 0 0 16 0c0-5-4-9-8-16z"/>'),
    # a bent knee (thigh, round joint, shin) with three short pain rays: an injury or a sore joint
    "joint": ('<path d="M12 8 24 26"/><circle cx="28" cy="32" r="7"/><path d="M25.8 38.6 20 56"/>'
              '<path d="M41 24l7-5M43 32h8M41 40l7 5"/>'),
}


def _ic(name, size="0.34in", sw=2.9):
    body = IC.get(name) or ICONS[name]
    return (f'<svg class="ic" viewBox="0 0 64 64" style="width:{size};height:{size}" fill="none" stroke="currentColor" '
            f'stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{body}</svg>')


TRIGGERS = [  # [MAYO] causes and risk factors; [AAFP12] linked conditions; [SCHW09] fatigue; [SPASM] guarding
    ("dumbbell", "Tired, overused muscles"),
    ("sweat", "Sweat, heat, too little fluid"),
    ("chair", "Sitting still for hours"),
    ("joint", "Injury or a sore joint"),
    ("age", "Getting older"),
    ("pregnant", "Pregnancy"),
    # [GARR12]: inhalers (LABA 2.42) and some water pills (potassium-sparing 2.12, thiazide-like 1.48) are the strong
    # links; loop diuretics (1.20) and statins (1.16) are weak ones, so statins come last.  [FDA-PPI] [ODS-MG]: long-term
    # heartburn pills (PPIs) can lower blood magnesium, and low magnesium can cause spasms.  This word order keeps the
    # label to three lines in the narrow cell.
    ("rx", "Some water and heartburn pills, inhalers, statins"),
    # [MAYO] too little potassium, calcium or magnesium; [ODS-CA] [ODS-MG] low blood levels make nerves over-fire
    ("lowlevels", "Low magnesium, calcium or potassium"),
    # [MAYO] diabetes, nerve, liver, thyroid; [AAFP12] hemodialysis (kidney) and cirrhosis (liver)
    # (this word order wraps in three lines in the narrow cell)
    ("stethoscope", "Diabetes, nerve, kidney, liver or thyroid problems"),
]

RESEARCH = [  # (css class, tag, tag sub-line, lead, text)
    # [HALL12] n=80, over 55, calf AND hamstring stretches nightly for 6 weeks (not blinded): fewer, milder cramps.
    # [COPPIN05] n=191, calf-only stretching: no change.  [KUUS26] n=121, ages 50 to 85: knee-high medical compression
    # stockings worn from waking to bedtime for 4 weeks, -1.43 cramps a week against placebo pills (95% CI -2.36 to
    # -0.50), fewer night wakings, less pain; stocking arm not blinded; peripheral arterial disease was excluded, hence
    # "people with good circulation".  One positive trial each.  The same trial is the 2026 magnesium result below,
    # so both of its arms are reported.
    ("ok", "Helped", "1 trial each", "Stretches and stockings.",
     "Adults over 55 who stretched calves and hamstrings nightly had fewer, milder night cramps; calf stretches "
     "alone did not. Knee-high compression stockings by day helped people with good circulation (2026)."),
    # [TAN24] 65+, MK-7 180 mcg nightly for 8 weeks.  [TAN25N] retracted and replaced in 2025 ("reissued with fixes");
    # the authors keep the finding, but the corrected numbers could not be re-checked here, so none are printed (and
    # no placebo detail).  The 180 mcg trial dose lives here only, never next to the product on the back.
    ("ea", "Early", "1 trial", "Vitamin K2 (MK-7).",
     "One trial (adults 65+, 180 mcg nightly) found fewer night cramps. Its report was reissued with fixes in 2025; "
     "it needs a second trial."),
    # [COCH20] unlikely to prevent cramps in older adults (moderate to high certainty).  [KUUS26] magnesium
    # hydrochloride, 250 mg magnesium a day for 4 weeks: -0.20 cramps a week against placebo (95% CI -1.49 to 1.09),
    # "a 2026 trial agreed".  The bridge to the back's magnesium products, without claiming they fix anything:
    # [ODS-MG] low magnesium itself causes cramps (muscle cramps are a sign of worsening deficiency); loop and
    # thiazide water pills raise magnesium loss; [FDA-PPI] long-term heartburn pills (PPIs) can lower it.
    ("np", "Not proven", "", "Magnesium.",
     "Unlikely to prevent ordinary night cramps in older adults (Cochrane 2020; a 2026 trial agreed). But low "
     "magnesium can itself cause cramps, and some water pills and heartburn pills lower it."),
    # [KOVAC25] 7 RCTs, 389 patients: small drop in statin muscle pain; [KENN20] 7 RCTs, 321 patients: no benefit
    ("mx", "Mixed", "", "CoQ10 with a statin.",
     "A 2025 review found a little less muscle pain. A 2020 review found no clear benefit."),
]

RED_FLAGS = [
    # [CDC-DVT]
    ("A sore calf that is <b>swollen, warm or red</b>.", "It can be a blood clot. Get care today."),
    # [FDA-ST]
    ("On a statin, with <b>unexplained muscle pain or weakness</b>, or <b>dark urine</b>.",
     "Call your prescriber&nbsp;now."),
    # [AAFP12] claudication is a look-alike: calf pain on walking that rest relieves means poor blood flow
    ("<b>Calf pain when you walk</b> that eases when you stop.", "Have your circulation checked."),
    # [MAYO] see a doctor: frequent, not better with self-care, weakness; [AAFP12] look-alikes (neuropathy etc.)
    ("Cramps that come <b>often</b>, or with <b>weakness or numbness</b>.",
     "Have a doctor check them."),
]


def steps_strip():
    cells = "".join(f'<div class="mcr-st"><span class="mcr-n{" r" if i == 4 else ""}">{i}</span>'
                    f'<p><b>{a}</b> {b}</p></div>' for i, (a, b) in enumerate(STEPS, 1))
    return f'<div class="mcr-steps">{cells}</div>'


def triggers():
    cells = "".join(f'<div class="mcr-rf"><span class="mcr-disc">{_ic(ic)}</span><span class="mcr-rl">{lab}</span></div>'
                    for ic, lab in TRIGGERS)
    return f'<div class="mcr-risk">{cells}</div>'


def research():
    rows = "".join(
        f'<div class="mcr-rr"><span class="mcr-tag {c}">{tag}{f"<small>{sub}</small>" if sub else ""}</span>'
        f'<p><b>{a}</b> {b}</p></div>' for c, tag, sub, a, b in RESEARCH)
    # source line: [HALL12] [COPPIN05] [KUUS26] [TAN24] [TAN25N] [COCH20] [KOVAC25] [KENN20]
    src = " &middot; ".join(x.replace(" ", "&nbsp;") for x in (
        "Hallegraeff 2012", "Coppin 2005", "Kuusipalo 2026", "Tan 2024 (notice 2025)", "Cochrane 2020",
        "Kovacic 2025", "Kennedy 2020"))
    return (f'<div class="mcr-res"><div class="mcr-ph">What the research says</div>{rows}'
            f'<p class="mcr-src">{src}</p></div>')


def red_flags():
    items = "".join(f'<li><span>{a}</span> <em>{b}</em></li>' for a, b in RED_FLAGS)
    return (f'<div class="mcr-flag"><div class="mcr-ph r">{_warn()} Get checked</div><ul>{items}</ul>'
            '<p class="mcr-q">Quinine pills are no longer advised for leg&nbsp;cramps.</p></div>')   # [AAFP12]


def _warn():
    return ('<svg viewBox="0 0 64 64" style="width:12px;height:12px;vertical-align:-1px" fill="none" stroke="currentColor" '
            'stroke-width="6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
            '<path d="M32 8 58 54H6z"/><path d="M32 26v12M32 46v1"/></svg>')


def front(t, ed):
    return ('<div class="mcr">'
            f'<div class="art mcr-art">{art_cramp(t)}</div>'
            f'{steps_strip()}'
            '<h2 class="mcr-h">What makes cramps more likely</h2>'
            f'{triggers()}'
            f'<div class="mcr-low">{research()}{red_flags()}</div>'
            '</div>')


# the back page of THIS sheet: the back <section> that follows the front holding .mcr (per-sheet HTML and bundle)
BACK = ".sheet.front:has(.mcr) + .sheet.back"

CSS = r"""
.mcr .mcr-art svg{display:block;width:100%;height:auto}
.mcr .mcr-steps{display:grid;grid-template-columns:1fr 1.22fr 1fr 0.86fr;gap:0.08in;margin-top:0.06in}
.mcr .mcr-st{display:flex;gap:6px;align-items:flex-start}
.mcr .mcr-n{flex:none;width:17px;height:17px;border-radius:50%;background:#fff;border:1.6px solid #23292D;color:#23292D;
  font:800 8pt/1 Inter,sans-serif;display:flex;align-items:center;justify-content:center;margin-top:1px}
.mcr .mcr-n.r{border-color:#B42B24;color:#B42B24}
.mcr .mcr-st p{margin:0;font-size:7.8pt;line-height:1.3;color:#2B3236}
.mcr .mcr-st b{color:var(--deep)}
.mcr .mcr-h{display:flex;align-items:center;gap:0.1in;font:900 10.5pt/1.2 Merriweather,Georgia,serif;color:var(--c1);
  letter-spacing:.04em;text-transform:uppercase;margin:0.07in 0 0.05in}
.mcr .mcr-h::after{content:"";flex:1;height:2px;border-radius:2px;background:linear-gradient(90deg,var(--soft),rgba(227,238,246,0))}
.mcr .mcr-risk{display:grid;grid-template-columns:repeat(9,1fr);gap:0 0.03in}
.mcr .mcr-rf{display:flex;flex-direction:column;align-items:center;text-align:center}
.mcr .mcr-disc{width:0.46in;height:0.46in;border-radius:50%;background:var(--soft);color:var(--c1);display:flex;
  align-items:center;justify-content:center;box-shadow:inset 0 0 0 1.5px rgba(31,94,140,.12)}
.mcr .mcr-rl{display:block;font-size:7.2pt;font-weight:600;line-height:1.2;color:#2F373C;margin-top:0.03in}
.mcr .mcr-low{display:grid;grid-template-columns:1.95fr 1fr;gap:0.12in;margin-top:0.07in;align-items:stretch}
.mcr .mcr-ph{font:800 7.6pt Inter,sans-serif;letter-spacing:.14em;text-transform:uppercase;color:var(--c1);margin:0 0 4px}
.mcr .mcr-ph.r{color:#A5281E}
.mcr .mcr-res{background:var(--tint);border:1px solid #D9E5EE;border-radius:9px;padding:0.07in 0.11in 0.06in}
.mcr .mcr-rr{display:grid;grid-template-columns:0.64in 1fr;gap:0.07in;align-items:start;margin:0 0 4px}
.mcr .mcr-tag{display:block;text-align:center;font:800 7pt/1.15 Inter,sans-serif;letter-spacing:.06em;text-transform:uppercase;
  color:#fff;border-radius:4px;padding:3px 2px;margin-top:1px}
.mcr .mcr-tag small{display:block;font:600 7pt/1.15 Inter,sans-serif;letter-spacing:.02em;text-transform:none;opacity:.95}
.mcr .mcr-tag.ok{background:#2E7D4F}
.mcr .mcr-tag.ea{background:#56687A}
.mcr .mcr-tag.np{background:#8A4F47}
.mcr .mcr-tag.mx{background:#756640}
.mcr .mcr-rr p{margin:0;font-size:7.7pt;line-height:1.3;color:#2B3236}
.mcr .mcr-rr b{color:var(--deep)}
.mcr .mcr-src{margin:2px 0 0;font-size:7pt;line-height:1.3;color:#5E686F}
.mcr .mcr-flag{border:1.5px solid #C0392B;background:#FDF3F1;border-radius:9px;padding:0.07in 0.12in 0.06in}
.mcr .mcr-flag ul{list-style:none;margin:0;padding:0}
.mcr .mcr-flag li{position:relative;padding-left:12px;font-size:7.8pt;line-height:1.3;color:#2B3236;margin:0 0 4px}
.mcr .mcr-flag li::before{content:"";position:absolute;left:0;top:4px;width:6px;height:6px;border-radius:50%;background:#C0392B}
.mcr .mcr-flag li b{color:#A5281E}
.mcr .mcr-flag li em{font-style:normal;font-weight:700;color:#2B3236}
.mcr .mcr-q{margin:2px 0 0;font-size:7.2pt;color:#5E686F;line-height:1.3}
""" + f"""
/* product columns: every need box is as tall as the tallest (a one-line need over a two-line list), so the photos,
   names and dark dose bars line up across the row; size lines and dose notes sit a little tighter */
{BACK} .col .need{{min-height:0.53in}}
{BACK} .col .pick .sz{{line-height:1.2}}
{BACK} .col .dose small{{line-height:1.25}}
/* only Muscle Eze and Vitamin K2 are in the daily plan, while the medicine check is long: a narrow rhythm panel with
   the times of day stacked (an empty slot is hidden, see _rhythm_css), beside a wide check panel */
{BACK} .duo{{grid-template-columns:1.9in 1fr}}
{BACK} .rhythm{{grid-template-columns:1fr;gap:4px}}
{BACK} .slot{{display:flex;align-items:center;gap:6px;padding:4px 6px}}
{BACK} .ns-title{{margin-top:0.1in}}
{BACK} .notes .ln{{height:0.22in}}
{BACK} .slot .when{{flex:none;width:0.84in}}
{BACK} .slot ul{{margin:0}}
/* the two Progressive Professional thumbnails come on an opaque white box: let the pale panel show through and
   drop the shadow that would outline the box */
{BACK} .pick img[src*="nd-mcr-vitamin-k2"],{BACK} .pick img[src*="nd-mcr-mag-k"]{{mix-blend-mode:multiply;filter:none}}
"""

# =============================================================== back: lifestyle icons (64 grid, kit.icon style)
# wall calf stretch: both hands on the wall, a clear torso leaning in, front knee bent, back leg straight, heel down
ICONS.setdefault("mcr_stretch", '<path d="M58 4v54M4 58h54"/><circle cx="41" cy="9" r="5"/><path d="M40 15 34 34"/>'
                 '<path d="M39 19 57 20M38.5 22 57 27"/><path d="M34 34 44 43 43 56h6"/><path d="M34 34 13 56h8"/>')
# stop a cramp: the seated towel stretch, side view, in the same stick-figure style as the wall stretch.  On a floor
# line, a figure leans forward from the hip with the leg straight; the foot stands up from a round heel, the sole
# rising to the ball and the toes tipped back toward the shin (with a toe crease); one arm holds a towel whose loop
# wraps the ball of the foot.  Drawn from y 8 to 56, so it sits centred in its disc.
ICONS.setdefault("mcr_foot", '<path d="M4 56H60"/><circle cx="17" cy="13" r="5"/><path d="M8.5 50 15.5 24.5"/>'
                 '<path d="M8.5 50H40"/>'
                 '<path d="M40 50C41.2 53.6 44 55 46.5 53.6L50.6 38.2C51.3 35.6 49.5 33.2 47 34.2L42.8 44.6"/>'
                 '<path d="M46.2 37.6 50 38.8"/><path d="M15.2 28.5 30 35"/>'
                 '<path d="M30 35 46.6 34.6M30 35C38 38 45.5 40.4 50.4 40.6C53.6 40.7 54.6 36.4 51.9 35.1"/>')

# =============================================================== the sheet
SHEET = {
    "slug": SLUG, "code": "ND-MS-604", "order": 15, "theme": "msk", "series": "Pain and Movement Series",
    "title": "Muscle Cramps and Spasms", "sub": "Why a muscle locks up, and how to help it let go",
    # [MAYO] sudden, involuntary contraction, most often the calf, foot or thigh; that other muscles (back, neck) can
    # cramp too is general reference knowledge (MedlinePlus, Muscle cramps; not opened this session).  Duration:
    # [TAN24] PMC full text, mean 1.15 to 1.3 minutes, so "seconds to minutes", not "will not let go".
    # [SPASM] guarding a sore back, neck or joint.  [AAFP12] "up to 60 percent of adults"; [MAISON16] 46% of
    # primary-care patients over 60, mostly in the calves (80%).
    "intro": ("A <b>cramp</b>, or spasm, is a muscle that suddenly tightens on its own and stays tight for seconds to "
              "minutes. It usually grabs the <b>calf</b>, foot or thigh, often at night, and it can strike the back or "
              "neck too. A spasm can also be a muscle <b>guarding</b> a sore back, neck or joint: it tightens to protect "
              "the sore spot and is slow to let go. Cramps are very common: <b>up to 6 in 10 adults</b> have had a night "
              "leg cramp, and nearly <b>half of people over 60</b> get them. Most are harmless, and simple habits help."),
    "front": front,
    "css": CSS,    # + _rhythm_css() below
    "back": {
        "life_title": "Lifestyle Recommendations", "style": "circle",
        "life": [
            # the title stays on one line, so this cell is no taller than its neighbours
            ("mcr_stretch", "Bedtime stretch",               # [HALL12]
             "Gently stretch your calves and the backs of your thighs every night before sleep."),
            # "salts" could read as table salt, so the electrolytes are named; the title stays on one line
            ("drop", "Drink enough",                          # [LAU19]; [MAYO] dehydration
             "Sip water all day. After long, sweaty workouts, add electrolytes, not just water."),
            ("leaf", "Eat your minerals",                     # [ODS-MG] [ODS-K] food sources
             "Magnesium: greens, beans, nuts and seeds. Potassium: potatoes and bananas."),
            ("dumbbell", "Build up slowly",                   # [SCHW09] [AAFP12] fatigue
             "Add exercise a little at a time. Tired muscles cramp more easily."),
            ("mcr_foot", "Stop a cramp",                      # [MAYO] self-care
             "Straighten the leg, pull your toes toward you, rub the knot, add warmth."),
            # [GARR12] water pills, inhalers, statins; [FDA-PPI] [ODS-MG] long-term heartburn pills (PPIs) lower blood
            # magnesium.  Four lines like its neighbours; "never stop one on your own" is in the medicine check below.
            ("rx", "Check medicines",
             "Water pills, heartburn pills, inhalers and statins can play a part. Ask before stopping."),
        ],
        # Back-page columns are not passed through ed_text, so no {who} here: edition wording lives in rx.
        # Only Muscle Eze and Vitamin K2 are in everyone's daily rhythm (4 pills).  Mag Calm Pro and Mag-K replace
        # Muscle Eze rather than add to it, so supplemental magnesium stays at 200 mg a day, under the 350 mg upper
        # limit [ODS-MG] (the rx panel says so: one magnesium product at a time); CoQ10 is only for statin users.
        # Headers are body needs with no drug names (21 CFR 101.93(g)(2)(x): a product tied to a drug's side effect
        # reads as a disease claim); who should skip what, with the drug names, lives in the rx panel.  Every need
        # is one line, every dose note is one line, and the .need boxes share one height (CSS below), so the
        # photos, names and dark dose bars all line up.  Claim bullets carry their own glued diamond (_sf).
        "cols": [
            # [LABEL] "Targeted Formula for Supporting and Relaxing Healthy Muscle Tissue"; not sold as a cramp cure
            # [COCH20]; a plain need, not "guarded" muscles, so it never reads as easing a spasm around an injury
            {"p": "mcr_muscle_eze", "need": "Relaxed muscles", "needsub": "magnesium + calcium,<br>theanine, passion flower",
             "start": True,
             "bullets": [_sf("Helps muscles relax"), _sf("Supports calm and rest")],
             "dose": "3 capsules at bedtime", "dosesub": "may cause drowsiness", "sched": [("bed", 3, "capsules")]},
            # [LABEL] "Healthy Stress and Relaxation Support"; label "Mix 1 scoop with 6 ounces of water 1-2 times
            # daily": one scoop, as a swap for Muscle Eze, keeps the day at 200 mg magnesium
            {"p": "mcr_mag_calm_pro", "need": "Calm busy nerves", "needsub": "magnesium, taurine,<br>B6, L-theanine",
             "bullets": [_sf("Supports relaxation"), _sf("Supports restful sleep")],
             "dose": "1 scoop in 6 oz water", "dosesub": "in place of Muscle Eze", "sched": []},
            # [ODS-VK] vitamin K activates bone proteins (osteocalcin) that bind calcium; [LABEL] "one capsule daily
            # with a meal".  The cramp trial [TAN24] stays on the front only, so the product is never tied to it.
            {"p": "mcr_vitamin_k2", "need": "Calcium balance", "needsub": "vitamin K2 as MK-7",
             "bullets": [_sf("Helps activate bone proteins that bind calcium"), "Long-acting MK-7 form"],
             "dose": "1 capsule daily", "dosesub": "with a meal", "sched": [("pm", 1, "capsule")]},
            # [NCCIH] statins lower blood CoQ10; [LABEL] R350U "one softgel daily with a meal"
            {"p": "coq10", "need": "Muscle cell energy", "needsub": "CoQ10 as ubiquinol",
             "bullets": [_sf("Fuel for energy-making in muscle cells"), "Statins lower the body&rsquo;s own CoQ10"],
             "dose": "1 softgel with a meal", "dosesub": "statin users only", "sched": []},
            # [ODS-MG] [ODS-K] magnesium and potassium for normal nerve and muscle signals.  No water-pill header:
            # "On a water pill?" would also invite spironolactone, triamterene and amiloride users, who must not add
            # potassium; the rx panel names those drugs.
            {"p": "mcr_mag_k", "need": "Mineral balance", "needsub": "magnesium + potassium",
             "bullets": [_sf("Supports normal muscle and nerve signals"), _sf("Supports healthy mineral levels")],
             "dose": "3 capsules with meals", "dosesub": "in place of Muscle Eze", "sched": []},
        ],
        # Both editions send every kidney and potassium decision to the PRESCRIBER: a pharmacist, DC or ND does not
        # manage kidney disease or those drugs.  No K2 dose line: the cramp trial's 180 mcg stays on the front.
        "rx": {
            "pharmacy": [
                # [GARR12] [AAFP12]; [FDA-PPI] [ODS-MG] heartburn pills (PPIs).  Pharmacists review the medicine list,
                # so this edition asks them to.
                "<b>Bring your medicine list.</b> {Who} can check it: some water pills, heartburn pills, asthma "
                "inhalers, statins and bone or estrogen medicines are linked to cramps. Never stop one on your own.",
                # [ODS-MG] UL 350 mg/day from supplements: each of the three gives 200 mg, so two would be 400 mg
                "<b>One magnesium product at a time:</b> Muscle Eze, Mag Calm Pro or Mag-K, never two.",
                # [ODS-MG] magnesium builds up when the kidneys are impaired; [ODS-K] ACE inhibitors, ARBs and
                # potassium-sparing diuretics raise blood potassium
                "<b>Kidney disease?</b> Ask your prescriber before any magnesium product. <b>On an ACE inhibitor or "
                "ARB, or spironolactone, triamterene or amiloride?</b> Skip Mag-K unless your prescriber says yes.",
                # [ODS-VK] [NCCIH] [TAN24] warfarin
                "<b>On warfarin (Coumadin)?</b> K2 and CoQ10 affect it. Start neither without your prescriber.",
                # [LABEL] pregnancy, nursing, medication; passion flower and theanine with sedatives; drowsiness
                "<b>Pregnant or nursing, or on sleep or anxiety medicine?</b> Ask {who} before any of these. "
                "Muscle Eze can make you drowsy.",
                # [LEVO] 4 hours; [CIPRO] 2 before or 6 after; [ODS-MG] bisphosphonates 2 hours, tetracyclines 2 before
                # or 4-6 after; calcium binds these too.  [COCH20] GI side effects.
                "<b>Thyroid pills:</b> 4 hours apart from magnesium or calcium. Take <b>alendronate, doxycycline or "
                "ciprofloxacin</b> 2 hours before magnesium or calcium, or 6 hours after. Loose stools mean too much "
                "magnesium.",
            ],
            "practitioner": [
                # [GARR12] [AAFP12] [FDA-PPI] [ODS-MG]
                "<b>Bring your medicine list.</b> Some water pills, heartburn pills, asthma inhalers, statins and bone "
                "or estrogen medicines are linked to cramps. Never stop one on your own.",
                # [ODS-MG]
                "<b>One magnesium product at a time:</b> Muscle Eze, Mag Calm Pro or Mag-K, never two.",
                # [ODS-MG] [ODS-K]
                "<b>Kidney disease?</b> Ask your prescriber before any magnesium product. <b>On an ACE inhibitor or "
                "ARB, or spironolactone, triamterene or amiloride?</b> Skip Mag-K unless your prescriber says yes.",
                # [ODS-VK] [NCCIH] [TAN24]
                "<b>On warfarin (Coumadin)?</b> K2 and CoQ10 affect it. Start neither without your prescriber.",
                # [LABEL]
                "<b>Pregnant or nursing, or on sleep or anxiety medicine?</b> Ask {who} before any of these. "
                "Muscle Eze can make you drowsy.",
                # [LEVO] [CIPRO] [ODS-MG] [COCH20]
                "<b>Thyroid pills:</b> 4 hours apart from magnesium or calcium. Take <b>alendronate, doxycycline or "
                "ciprofloxacin</b> 2 hours before magnesium or calcium, or 6 hours after. Loose stools mean too much "
                "magnesium.",
            ],
        },
    },
}


def _rhythm_css():
    """Hide the daily-rhythm slots this plan leaves empty (a column's own sched, else its product's sched), the way
    joint_pain.py does, instead of printing an empty "nothing to take" box."""
    import json
    here = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    try:
        prods = json.load(open(os.path.join(here, "products.d", f"{SLUG}.json")))
    except Exception:
        prods = {}
    used = set()
    for c in SHEET["back"]["cols"]:
        sched = c["sched"] if "sched" in c else prods.get(c["p"], {}).get("sched", [])
        used.update(s[0] for s in sched)
    return "".join(f"{BACK} .rhythm .slot:nth-child({i}){{display:none}}"
                   for i, slot in enumerate(("am", "pm", "bed"), 1) if slot not in used)


SHEET["css"] += _rhythm_css()
