"""Shoulder and Tendon Pain (ND-MS-603), Pain and Movement Series.  Slug "tendon-shoulder".

Self-contained sheet module (new in wave 2, nothing from the legacy sheets.py / art.py).

FRONT, top to bottom
  intro -> one inline-SVG plate with three panels and a KEY strip:
     1. the rotator cuff FROM THE FRONT (subscapularis, the supraspinatus tendon, the acromion
        "roof", the collarbone and the bursa, drawn red, at the pinch point under the roof);
     2. FROM THE BACK (supraspinatus, infraspinatus, teres minor on the shoulder blade), with a
        lens on the cuff tendon that opens into panel 3;
     3. INSIDE A TENDON: healthy collagen (neat, parallel fibers) beside an overloaded tendon
        (frayed gold fibers, new blood vessels), and "how to help it rebuild": collagen + vitamin C,
        wait about an hour, then load the tendon (the routine the studies used; loading is the signal).
  -> where tendon pain shows up (shoulder, elbow, heel; coral dot keyed in the header)
  -> what raises your risk (8 icons) -> the exercise pain guide (0-10 traffic light + "12 weeks")
  -> when to get checked right away (red flags, 911 for arm pain with heart-attack signs).
BACK: six lifestyle circles; five NutriDyn columns (Collagen Renew starts, Vitamin C 1000 is its pair,
Inflam-Eze Plus, Omega Pure EPA-DHA 1000, D3 5000 with K2); rhythm; three edition-aware checks ({who}).
Products: ts_* entries live in products.d/tendon-shoulder.json (label facts + "src"); omega_1000 is the
shared products.py entry; sheet-specific dose lines and schedules are set per column below.

Geometry: the anatomy is drawn once in "scapula units" (posterior view of a right shoulder blade,
medial border at x = 0, inferior angle at y = 1.0, about 16 cm in life) and mapped into each panel;
the front view is the same bones mirrored, with the front-only parts (coracoid, collarbone,
subscapularis) added.  Every SVG id starts with "ts-", every CSS class with "tsp-".

SOURCES (each number or fact on the page carries one of these tags in a comment)
  [KANNUS00]  Kannus P. Structure of the tendon connective tissue. Scand J Med Sci Sports 2000;10:312-20.
              PMID 11085557. Collagen, mostly type I, is 65-80% of tendon dry mass.
  [MILLAR21]  Millar NL et al. Tendinopathy. Nat Rev Dis Primers 2021;7:1. PMID 33414454. Commonest sites:
              rotator cuff, elbow, patellar, gluteal, Achilles; disorganised collagen fibres, more small
              vessels and sensory nerves.
  [COOK09]    Cook JL, Purdam CR. Br J Sports Med 2009;43:409-16. PMID 18812414 (load-induced tendinopathy).
  [KHAN02]    Khan KM et al. Time to abandon the "tendinitis" myth. BMJ 2002;324:626-7. PMID 11895810.
  [WHITTLE15] Whittle S, Buchbinder R. In the clinic: rotator cuff disease. Ann Intern Med 2015;162:ITC1-15.
              PMID 25560729. Shoulder pain is the third most frequent musculoskeletal reason to present
              to primary care.
  [ZHANG25]   Zhang W et al. J Orthop Surg Res 2025;20:1075. PMID 41276811. Rotator cuff-related shoulder
              pain is the most common cause of shoulder pain.
  [LEWIS16]   Lewis J. Man Ther 2016;23:57-68. PMID 27083390. A graduated exercise approach gives at least
              the benefit of surgery for subacromial pain, cuff tendinopathy and atraumatic tears.
  [CPG20]     Doiron-Cadrin P et al. Arch Phys Med Rehabil 2020;101:1233-42. PMID 32007452. All rotator
              cuff guidelines recommend an exercise program.
  [CPG24]     Lowry V et al. Arch Phys Med Rehabil 2024;105:411-26. PMID 37832814. Evaluate red flags first;
              exercise recommended for all shoulder disorders.
  [LEONG19]   Leong HT et al. J Rehabil Med 2019;51:627-37. PMID 31489438. Age over 50 (OR 3.31), diabetes
              (OR 2.24), work with the arm above shoulder height (OR 2.41).
  [GIRI22]    Giri A et al. Ann Phys Rehabil Med 2023;66:101631. PMID 35257948. High cholesterol (OR 1.48).
  [RANGER16]  Ranger TA et al. Br J Sports Med 2016;50:982-9. PMID 26598716. Diabetes and tendinopathy.
  [BISHOP15]  Bishop JY et al. Arthroscopy 2015;31:1598-605. PMID 25801046. Smoking and cuff tears.
  [HARVIE04]  Harvie P et al. J Bone Joint Surg Br 2004;86:696-700. PMID 15274266. Siblings RR 2.42.
  [YU19]      Yu X et al. Drug Saf 2019;42:1025-33. PMID 31077091. Fluoroquinolones: tendon disorders OR 1.89.
  [FDA16]     FDA boxed warning on fluoroquinolone antibiotics (2008, updated 2016): tendinitis and tendon
              rupture, risk higher over age 60 and with corticosteroids.
  [XERGIA22]  Xergia SA et al. Phys Sportsmed 2023;51:506-16. PMID 35670156. Achilles rupture: steroids,
              quinolones.
  [SHIRI06]   Shiri R et al. Am J Epidemiol 2006;164:1065-74. PMID 16968862. Tennis elbow in 1.3% of adults
              30-64; forceful plus repetitive arm work (OR 5.6); smoking.
  [BISSET15]  Bisset LM, Vicenzino B. J Physiother 2015;61:174-81. PMID 26361816 (lateral elbow pain, gripping).
  [ACH18]     Martin RL et al. APTA midportion Achilles tendinopathy guideline. JOSPT 2018;48(5):A1-A38.
              PMID 29712543. Pain 2-6 cm above the heel insertion, morning stiffness, pain with loading.
  [SHAW17]    Shaw G et al. Am J Clin Nutr 2017;105:136-43. PMID 27852613. Vitamin C-enriched gelatin:
              amino acids peak 1 h after; 15 g 1 h before exercise doubled a collagen-synthesis marker.
  [PRAET19]   Praet SFE et al. Nutrients 2019;11:76. PMID 30609761. TENDOFORTE peptides + calf loading.
  [BISCHOF24] Bischof K et al. Sports Med 2024;54:2865-88. PMID 39060741. 19 RCTs, collagen + training.
  [KJAER04]   Kjaer M. Physiol Rev 2004;84:649-98. PMID 15044685. Loading raises collagen synthesis,
              inactivity lowers it; overuse needs adjusted loading, not immobilisation.
  [SILB07]    Silbernagel KG et al. Am J Sports Med 2007;35:897-906. PMID 17307888. Pain-monitoring model:
              0-2 safe, 2-5 acceptable, above 5 too much; pain after exercise settles by next morning.
  [ALF98]     Alfredson H et al. Am J Sports Med 1998;26:360-6. PMID 9617396 (12-week loading program).
  [BEYER15]   Beyer R et al. Am J Sports Med 2015;43:1704-11. PMID 26018970 (12-week programs, gains held
              at 52 weeks).
  [AHA]       American Heart Association, heart attack warning signs (pain in one or both arms, back, neck,
              jaw; shortness of breath; cold sweat): call 911.
  [VC96]      Van Cauter E, Plat L. J Pediatr 1996;128:S32-7. PMID 8627466. The largest growth hormone pulse
              comes with the first deep (slow-wave) sleep.
  [NSF15]     Hirshkowitz M et al. Sleep Health 2015;1:40-3. PMID 29073412. Adults: 7 to 9 hours.
  [ODS-C]     NIH Office of Dietary Supplements, Vitamin C fact sheet: needed to make collagen.
"""
import math
import os
import random

import kit
from kit import icon
from svgkit import T, svg

SLUG = "tendon-shoulder"

# ============================================================== text measuring (Inter metrics via Pillow)
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


def tw(text, size, weight=700, ls=0.0):
    """Advance width of `text` in Inter at `size` px (generous fallback without Pillow or the font)."""
    try:
        w = _face(_WEIGHTS[weight]).getlength(text) * size / 100
    except Exception:
        w = len(text) * size * (0.68 if text.isupper() else 0.6)
    return w + ls * len(text)


# ============================================================== palette (every colour-coded thing is in the KEY)
INK, INK2 = "#23292D", "#56616A"
MUS, MUS_D, MUS_EDGE, MUS_FIB = "#F2A39A", "#CF625C", "#9E3F3B", "#B5504B"      # muscle: pink
TEN, TEN_D, TEN_EDGE, TEN_FIB = "#FFFDF7", "#EADFCB", "#B9A989", "#D9CCB2"      # tendon: white / ivory
BONE, BONE_D, BONE_EDGE = "#F7EAD0", "#DDC296", "#A9864F"                       # bone: tan
BURSA, BURSA_D, BURSA_EDGE = "#EC5A50", "#C12F2A", "#8F1F1B"                    # irritated bursa: red
FRAY = "#E3A21F"                                                               # frayed fibers: gold
VESSEL = "#C8343B"                                                             # new blood vessels: red
FIELD = "#F2E9DA"                                                              # tendon tissue background
GOOD, BAD = "#2F7D59", "#B23A30"
LEAD = "#5B666E"

# ============================================================== plate geometry
W = 760
S = 170.0                      # one scapula unit in viewBox units
AX = 0.955                     # anatomy width in scapula units (medial border to greater tubercle)
P1X, P2X, P3X = 0, 256, 518    # panel left edges (front, back, zoom)
PW, P3W = 252, 242
PANEL_H = 300
KEY_Y, KEY_H = 308, 32
H = KEY_Y + KEY_H + 2
OY = 66                        # anatomy origin y (scapula superior angle)
FRONT_X = P1X + 34             # screen x of the lateral edge (x = AX) in the mirrored front view
BACK_X = P2X + 60              # screen x of the medial border (x = 0) in the back view


def _front(x, y):
    return FRONT_X + (AX - x) * S, OY + y * S


def _back(x, y):
    return BACK_X + x * S, OY + y * S


def _f(v):
    return f"{v:.1f}"


def _path(pts, m, closed=True):
    """Catmull-Rom curve through pts [(x, y, tension)] mapped by m, as cubic Bezier path data."""
    P = [(*m(x, y), k) for x, y, k in pts]
    n = len(P)
    tan = []
    for i in range(n):
        if closed:
            a, b = P[i - 1], P[(i + 1) % n]
        else:
            a, b = P[max(i - 1, 0)], P[min(i + 1, n - 1)]
        k = P[i][2]
        tan.append((k * (b[0] - a[0]) / 2, k * (b[1] - a[1]) / 2))
    d = [f"M{_f(P[0][0])},{_f(P[0][1])}"]
    last = n if closed else n - 1
    for i in range(last):
        j = (i + 1) % n
        (xa, ya, _), (xb, yb, _) = P[i], P[j]
        d.append(f"C{_f(xa + tan[i][0] / 3)},{_f(ya + tan[i][1] / 3)} "
                 f"{_f(xb - tan[j][0] / 3)},{_f(yb - tan[j][1] / 3)} {_f(xb)},{_f(yb)}")
    return "".join(d) + ("Z" if closed else "")


# ---- bones (scapula units, posterior view of a right shoulder; third value = curve tension)
SCAPULA = [
    (0.075, 0.000, 0.5), (0.200, 0.030, 1.0), (0.330, 0.062, 1.0), (0.405, 0.080, 0.8), (0.432, 0.103, 0.4),
    (0.468, 0.090, 0.6), (0.530, 0.083, 1.0), (0.585, 0.106, 0.8), (0.632, 0.132, 0.6), (0.655, 0.182, 1.0),
    (0.662, 0.236, 1.0), (0.652, 0.296, 1.0), (0.628, 0.340, 0.6), (0.585, 0.398, 1.0), (0.505, 0.528, 1.0),
    (0.410, 0.678, 1.0), (0.320, 0.822, 1.0), (0.250, 0.936, 0.9), (0.205, 1.000, 0.35), (0.158, 0.972, 0.9),
    (0.105, 0.860, 1.0), (0.055, 0.640, 1.0), (0.018, 0.420, 1.0), (0.000, 0.256, 0.6), (0.018, 0.120, 1.0),
    (0.045, 0.035, 0.8),
]
SPINE = [  # spine of the scapula rising into the acromion (back view only)
    (0.024, 0.228, 0.6), (0.100, 0.206, 1.0), (0.240, 0.176, 1.0), (0.380, 0.141, 1.0), (0.500, 0.106, 1.0),
    (0.570, 0.072, 1.0), (0.612, 0.020, 1.0), (0.680, -0.012, 1.0), (0.770, -0.020, 1.0), (0.836, -0.004, 0.8),
    (0.864, 0.028, 0.6), (0.851, 0.062, 0.8), (0.800, 0.080, 1.0), (0.720, 0.085, 1.0), (0.652, 0.100, 1.0),
    (0.606, 0.160, 0.7), (0.560, 0.176, 1.0), (0.450, 0.196, 1.0), (0.300, 0.236, 1.0), (0.150, 0.271, 1.0),
    (0.046, 0.298, 0.6), (0.026, 0.278, 0.8),
]
ACROMION = [  # the acromion seen from the front (the roof over the ball)
    (0.640, -0.006, 0.8), (0.700, -0.032, 1.0), (0.780, -0.036, 1.0), (0.840, -0.016, 0.8), (0.866, 0.024, 0.6),
    (0.852, 0.062, 0.8), (0.800, 0.080, 1.0), (0.722, 0.084, 1.0), (0.668, 0.064, 0.8),
]
CLAVICLE = [  # collarbone: a gentle S from the acromion toward the breastbone (runs off the panel)
    (0.672, -0.020, 0.6), (0.610, -0.030, 1.0), (0.520, -0.040, 1.0), (0.400, -0.058, 1.0), (0.270, -0.060, 1.0),
    (0.140, -0.050, 1.0), (0.010, -0.040, 1.0), (-0.120, -0.048, 1.0), (-0.300, -0.074, 0.3), (-0.300, -0.006, 0.3),
    (-0.120, 0.012, 1.0), (0.010, 0.020, 1.0), (0.140, 0.020, 1.0), (0.270, 0.010, 1.0), (0.400, 0.006, 1.0),
    (0.520, 0.014, 1.0), (0.610, 0.026, 1.0), (0.668, 0.036, 0.6),
]
CORACOID = [  # the hook on the front of the shoulder blade, just under the collarbone
    (0.498, 0.104, 0.7), (0.528, 0.066, 1.0), (0.596, 0.068, 1.0), (0.664, 0.094, 1.0), (0.706, 0.130, 0.6),
    (0.688, 0.158, 0.8), (0.628, 0.142, 1.0), (0.572, 0.136, 1.0), (0.536, 0.152, 0.7),
]
HUMERUS = [
    (0.700, 0.420, 1.0), (0.655, 0.360, 1.0), (0.642, 0.285, 1.0), (0.660, 0.205, 1.0), (0.710, 0.152, 1.0),
    (0.785, 0.138, 1.0), (0.850, 0.150, 1.0), (0.900, 0.178, 1.0), (0.940, 0.222, 1.0), (0.952, 0.285, 1.0),
    (0.932, 0.360, 1.0), (0.892, 0.430, 1.0), (0.866, 0.520, 1.0), (0.861, 0.800, 1.0), (0.859, 1.100, 0.2),
    (0.736, 1.100, 0.2), (0.739, 0.800, 1.0), (0.733, 0.520, 1.0),
]
HEAD_C, HEAD_R = (0.785, 0.285), 0.145      # ball of the arm bone

# ---- muscles
SUPRA = [  # supraspinatus belly, above the spine (runs under the acromion)
    (0.060, 0.030, 0.7), (0.180, 0.028, 1.0), (0.320, 0.050, 1.0), (0.450, 0.066, 1.0), (0.560, 0.070, 1.0),
    (0.668, 0.086, 1.0), (0.668, 0.128, 1.0), (0.560, 0.122, 1.0), (0.450, 0.152, 1.0), (0.320, 0.186, 1.0),
    (0.180, 0.214, 1.0), (0.050, 0.236, 0.7), (0.028, 0.130, 1.0),
]
SUPRA_FRONT = [  # the same muscle seen from the front: a strip above the shoulder blade, behind the collarbone
    (0.080, -0.010, 0.7), (0.200, -0.020, 1.0), (0.340, -0.010, 1.0), (0.460, 0.010, 1.0), (0.560, 0.030, 1.0),
    (0.640, 0.060, 1.0), (0.646, 0.112, 1.0), (0.560, 0.098, 1.0), (0.460, 0.082, 1.0), (0.340, 0.066, 1.0),
    (0.200, 0.040, 1.0), (0.085, 0.022, 0.7),
]
INFRA = [  # infraspinatus belly, below the spine
    (0.040, 0.300, 0.7), (0.160, 0.276, 1.0), (0.300, 0.246, 1.0), (0.450, 0.212, 1.0), (0.560, 0.200, 1.0),
    (0.672, 0.212, 0.8), (0.682, 0.300, 0.8), (0.560, 0.344, 1.0), (0.470, 0.424, 1.0), (0.360, 0.544, 1.0),
    (0.255, 0.660, 1.0), (0.160, 0.756, 1.0), (0.104, 0.800, 0.7), (0.062, 0.640, 1.0), (0.030, 0.450, 1.0),
]
TMINOR = [  # teres minor, along the outer border of the shoulder blade
    (0.682, 0.302, 0.8), (0.560, 0.344, 1.0), (0.470, 0.424, 1.0), (0.360, 0.544, 1.0), (0.255, 0.660, 1.0),
    (0.200, 0.718, 0.6), (0.226, 0.776, 0.6), (0.330, 0.664, 1.0), (0.432, 0.534, 1.0), (0.522, 0.424, 1.0),
    (0.600, 0.364, 1.0), (0.686, 0.352, 0.8),
]
SUBSC = [  # subscapularis on the front of the shoulder blade
    (0.070, 0.050, 0.7), (0.200, 0.076, 1.0), (0.330, 0.100, 1.0), (0.440, 0.126, 1.0), (0.560, 0.166, 1.0),
    (0.668, 0.226, 0.8), (0.674, 0.336, 0.8), (0.560, 0.412, 1.0), (0.470, 0.542, 1.0), (0.370, 0.692, 1.0),
    (0.270, 0.842, 1.0), (0.200, 0.928, 0.7), (0.150, 0.898, 1.0), (0.095, 0.760, 1.0), (0.050, 0.540, 1.0),
    (0.025, 0.320, 1.0), (0.035, 0.150, 1.0),
]

# ---- tendons.  BACK: one cuff hood over the back of the ball (supraspinatus on top, infraspinatus,
# teres minor), split by fine seams; FRONT: the supraspinatus tendon over the top of the ball and the
# subscapularis tendon across its front to the lesser tubercle.
CUFF_BACK = [(0.598, 0.086, 0.8), (0.700, 0.118, 1.0), (0.785, 0.128, 1.0), (0.870, 0.150, 1.0), (0.926, 0.196, 1.0),
             (0.950, 0.252, 1.0), (0.946, 0.310, 1.0), (0.928, 0.348, 0.6), (0.850, 0.356, 1.0), (0.750, 0.360, 1.0),
             (0.660, 0.354, 1.0), (0.642, 0.348, 0.6), (0.634, 0.300, 1.0), (0.624, 0.240, 1.0), (0.612, 0.196, 1.0),
             (0.600, 0.130, 1.0)]
SEAMS_BACK = [[(0.614, 0.204, 1), (0.700, 0.196, 1), (0.800, 0.198, 1), (0.890, 0.208, 1), (0.940, 0.226, 1)],
              [(0.636, 0.304, 1), (0.720, 0.298, 1), (0.820, 0.296, 1), (0.900, 0.298, 1), (0.948, 0.304, 1)]]
T_SUPRA_FRONT = [(0.600, 0.090, 0.8), (0.700, 0.118, 1.0), (0.785, 0.127, 1.0), (0.870, 0.150, 1.0), (0.926, 0.196, 1.0),
                 (0.948, 0.244, 0.6), (0.916, 0.236, 0.8), (0.868, 0.184, 1.0), (0.785, 0.160, 1.0), (0.700, 0.152, 1.0),
                 (0.600, 0.134, 0.8)]
T_SUBSC = [(0.600, 0.212, 0.7), (0.700, 0.214, 1.0), (0.780, 0.232, 1.0), (0.834, 0.258, 0.7), (0.849, 0.302, 1.0),
           (0.836, 0.350, 0.7), (0.780, 0.368, 1.0), (0.700, 0.380, 1.0), (0.612, 0.372, 0.7), (0.588, 0.330, 1.0),
           (0.586, 0.260, 1.0)]
GROOVE = [(0.872, 0.232, 1), (0.874, 0.300, 1), (0.868, 0.400, 1), (0.858, 0.520, 1)]   # bicipital groove (front)


def bursa_pts():
    """The bursa as a soft pillow following the ball: thin under the acromion, fullest over the outer side."""
    cx, cy = HEAD_C
    ri = HEAD_R + 0.024
    a0, a1, n = 226.0, 352.0, 20
    outer, inner = [], []
    for i in range(n + 1):
        u = i / n
        a = math.radians(a0 + (a1 - a0) * u)
        th = 0.006 + 0.040 * math.sin(math.pi * u ** 0.85) ** 1.1
        inner.append((cx + ri * math.cos(a), cy + ri * math.sin(a), 1.0))
        outer.append((cx + (ri + th) * math.cos(a), cy + (ri + th) * math.sin(a), 1.0))
    pts = outer + inner[::-1]
    pts[0] = (*pts[0][:2], 0.5)
    pts[n] = (*pts[n][:2], 0.5)
    pts[n + 1] = (*pts[n + 1][:2], 0.5)
    pts[-1] = (*pts[-1][:2], 0.5)
    return pts


def plate_defs():
    lin = lambda i, a, b, x2=1, y2=1: (f'<linearGradient id="{i}" x1="0" y1="0" x2="{x2}" y2="{y2}">'
                                       f'<stop offset="0" stop-color="{a}"/><stop offset="1" stop-color="{b}"/></linearGradient>')
    return ("<defs>"
            + lin("ts-bone", BONE, BONE_D) + lin("ts-mus", MUS, MUS_D) + lin("ts-ten", TEN, TEN_D, 0, 1)
            + lin("ts-bur", BURSA, BURSA_D, 0, 1) + lin("ts-band", "#FFFFFF", "#F4F8FB", 0, 1)
            + lin("ts-spine", "#FCF3E1", "#D2B27C", 0, 1)
            + '<linearGradient id="ts-mhi" x1="0" y1="0" x2=".7" y2="1"><stop offset="0" stop-color="#FFFFFF" stop-opacity=".34"/>'
              '<stop offset=".55" stop-color="#FFFFFF" stop-opacity="0"/></linearGradient>'
            + '<radialGradient id="ts-cuff" cx=".42" cy=".38" r=".7"><stop offset="0" stop-color="#FFFFFF"/>'
              f'<stop offset=".7" stop-color="#F6EFE1"/><stop offset="1" stop-color="{TEN_D}"/></radialGradient>'
            + '<radialGradient id="ts-ball" cx=".38" cy=".34" r=".75"><stop offset="0" stop-color="#FFF8EA"/>'
              f'<stop offset=".6" stop-color="{BONE}"/><stop offset="1" stop-color="{BONE_D}"/></radialGradient>'
            + '<radialGradient id="ts-fossa" cx=".45" cy=".45" r=".6"><stop offset="0" stop-color="#E2C99E"/>'
              f'<stop offset="1" stop-color="{BONE}"/></radialGradient>'
            + '<linearGradient id="ts-fade" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#fff"/>'
              '<stop offset=".8" stop-color="#fff"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></linearGradient>'
            + "</defs>")


def _shape(pts, m, fill, edge, sw=1.1, extra=""):
    return f'<path d="{_path(pts, m)}" fill="{fill}" stroke="{edge}" stroke-width="{sw}" stroke-linejoin="round"{extra}/>'


def _lerp(p, q, t):
    return p[0] + (q[0] - p[0]) * t, p[1] + (q[1] - p[1]) * t


def _fibers(uid, pts, m, src, dst, n, color=MUS_FIB, sw=0.9, op=0.5, bow=0.0):
    """Fibre lines clipped to a shape: from points along an origin edge to points along the far edge.
    bow lifts the middle of each line (scapula units, negative = up) so lines can follow a curved surface."""
    lines = []
    for i in range(n):
        t = (i + 0.5) / n
        p0, p1 = _lerp(src[0], src[1], t), _lerp(dst[0], dst[1], t)
        a, b = m(*p0), m(*p1)
        if bow:
            c = m((p0[0] + p1[0]) / 2, (p0[1] + p1[1]) / 2 + bow * (1.2 - t))
            lines.append(f"M{_f(a[0])},{_f(a[1])}Q{_f(c[0])},{_f(c[1])} {_f(b[0])},{_f(b[1])}")
        else:
            lines.append(f"M{_f(a[0])},{_f(a[1])}L{_f(b[0])},{_f(b[1])}")
    return (f'<clipPath id="{uid}"><path d="{_path(pts, m)}"/></clipPath>'
            f'<path d="{"".join(lines)}" stroke="{color}" stroke-width="{sw}" opacity="{op}" fill="none" '
            f'stroke-linecap="round" clip-path="url(#{uid})"/>')


def _muscle(uid, pts, m, src, dst, n):
    """Muscle belly: pink gradient, fibre lines toward its tendon, a soft highlight for volume."""
    d = _path(pts, m)
    return (f'<path d="{d}" fill="url(#ts-mus)" stroke="{MUS_EDGE}" stroke-width="1.1" stroke-linejoin="round"/>'
            + _fibers(uid, pts, m, src, dst, n)
            + f'<path d="{d}" fill="url(#ts-mhi)" stroke="none"/>')


def _hood(uid, pts, m, src, dst, n, seams=(), bow=-0.022, fade=0.07):
    """Tendon that wraps the ball: ivory, lit from the upper left, fine collagen lines curving over the ball.
    Its first `fade` scapula units (from the muscle end, src) fade in, so the muscle flows into the tendon."""
    out = [_shape(pts, m, "url(#ts-cuff)", TEN_EDGE, 1.0),
           _fibers(uid, pts, m, src, dst, n, TEN_FIB, 0.8, 0.95, bow)]
    for sm in seams:
        out.append(f'<path d="{_path(sm, m, closed=False)}" stroke="#C6B593" stroke-width="1.1" fill="none"/>')
    (sx0, sy0), (sx1, sy1) = _lerp(src[0], src[1], .5), _lerp(dst[0], dst[1], .5)
    ln = math.hypot(sx1 - sx0, sy1 - sy0)
    a, b = m(sx0, sy0), m(sx0 + (sx1 - sx0) * fade / ln, sy0 + (sy1 - sy0) * fade / ln)
    big = 400
    return (f'<linearGradient id="{uid}-g" gradientUnits="userSpaceOnUse" x1="{_f(a[0])}" y1="{_f(a[1])}" '
            f'x2="{_f(b[0])}" y2="{_f(b[1])}"><stop offset="0" stop-color="#fff" stop-opacity="0"/>'
            f'<stop offset="1" stop-color="#fff"/></linearGradient>'
            f'<mask id="{uid}-m" maskUnits="userSpaceOnUse" x="{-big}" y="{-big}" width="{3 * big}" height="{3 * big}">'
            f'<rect x="{-big}" y="{-big}" width="{3 * big}" height="{3 * big}" fill="url(#{uid}-g)"/></mask>'
            f'<g mask="url(#{uid}-m)">{"".join(out)}</g>')


def _humerus(m, uid):
    hx, hy = m(*HEAD_C)
    r = HEAD_R * S
    gx = [m(p[0], p[1]) for p in GROOVE]
    return (f'<mask id="{uid}" maskUnits="userSpaceOnUse"><rect x="{_f(hx - 70)}" y="{OY - 10}" width="140" '
            f'height="{_f(1.11 * S + 12)}" fill="url(#ts-fade)"/></mask>'
            f'<g mask="url(#{uid})">' + _shape(HUMERUS, m, "url(#ts-bone)", BONE_EDGE, 1.2)
            + f'<circle cx="{_f(hx)}" cy="{_f(hy)}" r="{_f(r - 1.5)}" fill="url(#ts-ball)"/>'
            + f'<path d="M{_f(gx[1][0])},{_f(gx[1][1])} Q{_f(gx[2][0])},{_f(gx[2][1])} {_f(gx[3][0])},{_f(gx[3][1] + 40)}" '
              f'stroke="{BONE_EDGE}" stroke-width=".9" opacity=".45" fill="none"/></g>')


def _label(x, y, text, tx, ty, anchor="start", size=10.5, weight=700, color=INK, side=None, sub=None):
    """Label in clear space with a thin leader to (tx, ty) ending in a dot on the structure.
    side: where the leader leaves the text ('below', 'above', 'left', 'right')."""
    w = tw(text, size, weight)
    x0 = {"start": x, "middle": x - w / 2, "end": x - w}[anchor]
    cxm = x0 + w / 2
    if side == "below":
        lx, ly = cxm, y + 3.5 + (12 if sub else 0)
    elif side == "above":
        lx, ly = cxm, y - size * 0.95
    elif side == "left":
        lx, ly = x0 - 3, y - size * 0.34
    else:
        lx, ly = x0 + w + 3, y - size * 0.34
    out = (f'<path d="M{_f(lx)},{_f(ly)} L{_f(tx)},{_f(ty)}" stroke="{LEAD}" stroke-width=".9" fill="none"/>'
           f'<circle cx="{_f(tx)}" cy="{_f(ty)}" r="2.1" fill="{LEAD}" stroke="#fff" stroke-width=".8"/>'
           + T(x, y, text, size, weight, color, anchor))
    if sub:
        out += T(x, y + 12, sub, 10, 500, INK2, anchor, italic=True)
    return out


def _panel_card(x, w, title, sub=None):
    out = [f'<rect x="{x + .6}" y=".6" width="{w - 1.2}" height="{PANEL_H - 1.2}" rx="10" fill="url(#ts-band)" '
           f'stroke="#D3DFE8" stroke-width="1.2"/>']
    out.append(T(x + w / 2, 19, title, 11.5, 800, "#123F60", "middle", ls=1.1))
    if sub:
        out.append(T(x + w / 2, 33, sub, 10, 600, INK2, "middle", italic=True))
    return "".join(out)


def _ridge(pts_top, m, color="#FFFFFF", op=0.75, sw=1.6):
    return f'<path d="{_path(pts_top, m, closed=False)}" stroke="{color}" stroke-width="{sw}" opacity="{op}" fill="none" stroke-linecap="round"/>'


# ============================================================== panel 1: from the front
def panel_front():
    m = _front
    out = [_panel_card(P1X, PW, "FROM THE FRONT", "big outer shoulder muscle lifted away"),
           f'<clipPath id="ts-p1"><rect x="{P1X + 1}" y="1" width="{PW - 2}" height="{PANEL_H - 2}" rx="10"/></clipPath>',
           '<g clip-path="url(#ts-p1)">']
    out.append(_shape(SCAPULA, m, "url(#ts-fossa)", BONE_EDGE, 1.2))
    out.append(_muscle("ts-f-supf", SUPRA_FRONT, m, [(0.085, -0.008), (0.088, 0.02)], [(0.640, 0.066), (0.646, 0.108)], 5))
    out.append(_humerus(m, "ts-hm1"))
    out.append(_hood("ts-t-supf", T_SUPRA_FRONT, m, [(0.600, 0.092), (0.600, 0.132)], [(0.926, 0.196), (0.916, 0.236)], 3))
    out.append(_muscle("ts-f-subsc", SUBSC, m, [(0.05, 0.10), (0.19, 0.91)], [(0.660, 0.236), (0.670, 0.330)], 16))
    out.append(_hood("ts-t-subsc", T_SUBSC, m, [(0.596, 0.222), (0.606, 0.364)], [(0.838, 0.266), (0.838, 0.344)], 7, bow=-0.010))
    out.append(_shape(bursa_pts(), m, "url(#ts-bur)", BURSA_EDGE, 1.0))
    bh = [(HEAD_C[0] + (HEAD_R + 0.056) * math.cos(math.radians(a)), HEAD_C[1] + (HEAD_R + 0.056) * math.sin(math.radians(a)), 1)
          for a in (262, 280, 298, 316, 330)]
    out.append(_ridge(bh, m, "#FFD3CC", 0.8, 1.4))
    out.append(_shape(CORACOID, m, "url(#ts-bone)", BONE_EDGE, 1.1))
    out.append(_shape(ACROMION, m, "url(#ts-spine)", BONE_EDGE, 1.2))
    out.append(_shape(CLAVICLE, m, "url(#ts-spine)", BONE_EDGE, 1.2))
    out.append(_ridge([(0.640, -0.014, 1), (0.520, -0.028, 1), (0.380, -0.044, 1), (0.200, -0.040, 1), (0.000, -0.028, 1),
                       (-0.200, -0.040, 1)], m))
    aj = [m(0.668, -0.020), m(0.664, 0.036)]          # the joint between acromion and collarbone
    out.append(f'<path d="M{_f(aj[0][0])},{_f(aj[0][1])} L{_f(aj[1][0])},{_f(aj[1][1])}" stroke="{BONE_EDGE}" stroke-width="1.3"/>')
    out.append("</g>")
    # labels, all in clear space
    ax, ay = m(0.79, 0.020)
    out.append(_label(P1X + 10, 52, "Acromion: the roof", ax, ay, "start", side="below"))
    cx, cy = m(0.05, -0.005)
    out.append(_label(P1X + PW - 10, 52, "Collarbone", cx, cy, "end", side="below"))
    bx, by = m(0.985, 0.215)
    out.append(_label(P1X + 9, 156, "Bursa", bx, by, "start", side="above", sub="a cushion"))
    sx, sy = m(0.22, 0.78)
    out.append(_label(P1X + PW - 10, 282, "Subscapularis", sx, sy, "end", side="above"))
    hx, hy = m(0.80, 0.86)
    out.append(_label(P1X + 9, 282, "Arm bone", hx, hy, "start", side="above"))
    return "".join(out)


# ============================================================== panel 2: from the back
LENS = (0.862, 0.262)


def panel_back():
    m = _back
    out = [_panel_card(P2X, PW, "FROM THE BACK", "big outer shoulder muscle lifted away"),
           f'<clipPath id="ts-p2"><rect x="{P2X + 1}" y="1" width="{PW - 2}" height="{PANEL_H - 2}" rx="10"/></clipPath>',
           '<g clip-path="url(#ts-p2)">']
    out.append(_shape(SCAPULA, m, "url(#ts-bone)", BONE_EDGE, 1.2))
    out.append(_humerus(m, "ts-hm2"))
    out.append(_muscle("ts-f-infra", INFRA, m, [(0.05, 0.31), (0.11, 0.79)], [(0.664, 0.222), (0.680, 0.300)], 15))
    out.append(_muscle("ts-f-tmin", TMINOR, m, [(0.208, 0.722), (0.226, 0.772)], [(0.680, 0.308), (0.686, 0.350)], 4))
    out.append(_muscle("ts-f-supra", SUPRA, m, [(0.040, 0.040), (0.050, 0.232)], [(0.664, 0.090), (0.664, 0.124)], 7))
    out.append(_hood("ts-t-cuff", CUFF_BACK, m, [(0.600, 0.090), (0.642, 0.348)], [(0.930, 0.200), (0.928, 0.346)], 11,
                     seams=SEAMS_BACK, bow=-0.016))
    out.append(f'<path d="{_path(SPINE, m)}" fill="#6B4A22" opacity=".18" transform="translate(0.8,2.4)"/>')
    out.append(_shape(SPINE, m, "url(#ts-spine)", BONE_EDGE, 1.2))
    out.append(_ridge([(0.034, 0.234, 1), (0.120, 0.208, 1), (0.260, 0.178, 1), (0.400, 0.142, 1), (0.520, 0.104, 1),
                       (0.600, 0.040, 1), (0.690, -0.002, 1), (0.790, -0.010, 1), (0.846, 0.012, 1)], m))
    out.append("</g>")
    # labels
    sx, sy = m(0.26, 0.11)
    out.append(_label(P2X + 10, 52, "Supraspinatus", sx, sy, "start", side="below"))
    ax, ay = m(0.76, 0.026)
    out.append(_label(P2X + PW - 10, 52, "Acromion", ax, ay, "end", side="below"))
    ix, iy = m(0.14, 0.62)
    out.append(_label(P2X + 9, 282, "Infraspinatus", ix, iy, "start", side="above"))
    tx_, ty_ = m(0.34, 0.66)
    out.append(_label(P2X + 172, 240, "Teres minor", tx_, ty_, "middle", side="above"))
    bx, by = m(0.205, 0.955)
    out.append(_label(P2X + 140, 282, "Shoulder blade", bx, by, "middle", side="above"))
    # the lens on the cuff tendon that opens into panel 3
    lx, ly = m(*LENS)
    out.append(f'<circle cx="{_f(lx)}" cy="{_f(ly)}" r="9.5" fill="#FFFFFF" fill-opacity=".3" stroke="#123F60" stroke-width="2.2"/>')
    return "".join(out)


# ============================================================== panel 3: inside a tendon
def _fiber_band(x0, x1, y, h):
    return (f'<rect x="{_f(x0)}" y="{_f(y)}" width="{_f(x1 - x0)}" height="{_f(h)}" rx="{_f(h / 2)}" fill="url(#ts-ten)" '
            f'stroke="{TEN_EDGE}" stroke-width=".7"/>'
            f'<path d="M{_f(x0 + 3)},{_f(y + h * .38)} H{_f(x1 - 3)}" stroke="#FFFFFF" stroke-width="1.1" opacity=".9"/>')


def _frayed(x0, x1, y, n=4, bulge=5.2, sw=1.2):
    """A frayed stretch of fibre from x0 to x1 around height y: the fibre comes apart into n loose,
    wiggly gold strands that bulge away from each other, like an unravelling rope."""
    parts, w = [], x1 - x0
    for i in range(n):
        f = (i - (n - 1) / 2) / ((n - 1) / 2 or 1)          # -1 .. 1 across the fibre
        ys, ym = y + f * 1.7, y + f * bulge
        wig = 1.5 * (1 if i % 2 else -1)
        parts.append(f"M{_f(x0)},{_f(ys)} C{_f(x0 + w * .22)},{_f(ym + wig)} {_f(x0 + w * .40)},{_f(ym - wig)} "
                     f"{_f(x0 + w * .5)},{_f(ym)} S{_f(x1 - w * .22)},{_f(ys - wig)} {_f(x1)},{_f(ys)}")
    return f'<path d="{" ".join(parts)}" fill="none" stroke="{FRAY}" stroke-width="{sw}" stroke-linecap="round"/>'


def _wavy(x0, x1, y, amp, period, phase, h, taper=(False, False), y_end=None):
    """A wavy, swollen fibre: a ribbon whose centre line is a sine.  taper=(left, right) narrows that end to a
    point over its last 9 units (a fibre coming apart); y_end pins the centre line there to height y_end."""
    top, bot = [], []
    n = max(8, int((x1 - x0) / 3))
    for i in range(n + 1):
        x = x0 + (x1 - x0) * i / n
        c = y + amp * math.sin((x - x0) / period * 2 * math.pi + phase)
        hh = h
        for on, dist in ((taper[0], x - x0), (taper[1], x1 - x)):
            if on and dist < 9:
                hh = min(hh, 2.4 + (h - 2.4) * dist / 9)
                if y_end is not None:
                    c = y_end + (c - y_end) * dist / 9
        top.append((x, c - hh / 2))
        bot.append((x, c + hh / 2))
    d = "M" + " L".join(f"{_f(a)},{_f(b)}" for a, b in top) + " L" + " L".join(f"{_f(a)},{_f(b)}" for a, b in reversed(bot)) + "Z"
    return f'<path d="{d}" fill="url(#ts-ten)" stroke="{TEN_EDGE}" stroke-width=".7" stroke-linejoin="round"/>'


def _vessel(pts, sw=1.6):
    d = "M" + " ".join(f"{_f(x)},{_f(y)}" for x, y in pts)
    return f'<path d="{d}" fill="none" stroke="{VESSEL}" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round"/>'


def zoom_circle(cx, cy, r, healthy, uid):
    out = [f'<clipPath id="{uid}"><circle cx="{cx}" cy="{cy}" r="{r}"/></clipPath>',
           f'<g clip-path="url(#{uid})"><rect x="{cx - r}" y="{cy - r}" width="{2 * r}" height="{2 * r}" fill="{FIELD}"/>']
    if healthy:
        y, k = cy - r - 2, 0
        while y < cy + r:
            h = 8.6
            out.append(_fiber_band(cx - r - 8, cx + r + 8, y, h))
            y += h + 1.6
            k += 1
    else:
        rnd = random.Random(7)
        y, k = cy - r - 1, 0
        breaks = []
        while y < cy + r:
            h = rnd.uniform(6.5, 10)
            amp = rnd.uniform(1.6, 3.6)
            per = rnd.uniform(22, 34)
            ph = rnd.uniform(0, 6.28)
            if k in (2, 5, 8):          # broken fibres: a gap with frayed ends
                gx = cx + rnd.uniform(-r * .45, r * .45)
                out.append(_wavy(cx - r - 6, gx - 14, y + h / 2, amp, per, ph, h, (False, True), y + h / 2))
                out.append(_wavy(gx + 14, cx + r + 6, y + h / 2, amp, per, ph + 1.3, h, (True, False), y + h / 2))
                breaks.append((gx, y + h / 2))
            else:
                out.append(_wavy(cx - r - 6, cx + r + 6, y + h / 2, amp, per, ph, h))
            y += h + rnd.uniform(2.2, 4.8)
            k += 1
        for gx, gy in breaks:
            out.append(_frayed(gx - 16, gx + 16, gy, 4, 5.0))
        out.append(_vessel([(cx - r, cy + 16), (cx - 24, cy + 10), (cx - 6, cy + 18), (cx + 14, cy + 6), (cx + r, cy + 10)]))
        out.append(_vessel([(cx - 6, cy + 18), (cx - 2, cy + 32), (cx + 6, cy + r)], 1.3))
        out.append(_vessel([(cx - 24, cy + 10), (cx - 30, cy - 4), (cx - 22, cy - 20)], 1.2))
    out.append("</g>")
    out.append(f'<circle cx="{cx}" cy="{cy}" r="{r + 2}" fill="none" stroke="#FFFFFF" stroke-width="2.4"/>')
    out.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="#2F3A40" stroke-width="2.2"/>')
    return "".join(out)


def _mini(name, cx, cy, r=17):
    """Step disc with a line icon (64-grid icon bodies)."""
    s = 2 * r * 0.62 / 64
    body = STEP_ICONS[name]
    return (f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#FFFFFF" stroke="#1F5E8C" stroke-width="1.8"/>'
            f'<g transform="translate({_f(cx - 32 * s)},{_f(cy - 32 * s)}) scale({s:.4f})" fill="none" stroke="#1F5E8C" '
            f'stroke-width="{2.1 / s:.2f}" stroke-linecap="round" stroke-linejoin="round">{body}</g>')


STEP_ICONS = {
    "scoop": ('<path d="M19 22h26l-3.5 33a4 4 0 0 1-4 3.5h-11a4 4 0 0 1-4-3.5z"/><path d="M17 14h30v8H17z"/>'
              '<path d="M28 14V8h8v6"/><path d="M22 36h20"/>'),
    "clock": '<circle cx="32" cy="34" r="22"/><path d="M32 20v14l9 6"/><path d="M26 6h12"/>',
    "load": kit.ICONS["dumbbell"],
}


def panel_zoom():
    x, w = P3X, P3W
    out = [_panel_card(x, w, "INSIDE A TENDON", "magnified many times")]
    c1, c2, cy, r = x + 64, x + w - 64, 88, 46
    out.append(zoom_circle(c1, cy, r, True, "ts-zh"))
    out.append(zoom_circle(c2, cy, r, False, "ts-zo"))
    out.append(T(c1, cy + r + 17, "HEALTHY", 11, 800, GOOD, "middle", ls=0.6))
    out.append(T(c1, cy + r + 30, ["Neat, parallel", "collagen fibers"], 10, 600, INK, "middle"))
    out.append(T(c2, cy + r + 17, "OVERLOADED", 11, 800, BAD, "middle", ls=0.6))
    out.append(T(c2, cy + r + 30, ["Frayed, tangled fibers;", "new blood vessels"], 10, 600, INK, "middle"))
    # how tendons rebuild
    y0 = 188
    out.append(f'<path d="M{x + 14},{y0} H{x + w - 14}" stroke="#D3DFE8" stroke-width="1.2"/>')
    out.append(T(x + w / 2, y0 + 16, "HOW TO HELP IT REBUILD", 10.5, 800, "#123F60", "middle", ls=1.0))
    xs = [x + 42, x + w / 2, x + w - 42]
    dy = y0 + 40
    labels = [["Collagen +", "vitamin C"], ["Wait about", "1 hour"], ["Load the", "tendon"]]
    for i, (sx, lab) in enumerate(zip(xs, labels)):
        out.append(_mini(["scoop", "clock", "load"][i], sx, dy))
        out.append(T(sx, dy + 31, lab, 10, 700, INK, "middle"))
        if i < 2:
            ax0, ax1 = sx + 22, xs[i + 1] - 22
            out.append(f'<path d="M{_f(ax0)},{dy} H{_f(ax1 - 6)}" stroke="#2E8FC8" stroke-width="2.2" stroke-linecap="round"/>'
                       f'<path d="M{_f(ax1 - 7)},{dy - 4.5} L{_f(ax1)},{dy} L{_f(ax1 - 7)},{dy + 4.5} Z" fill="#2E8FC8"/>')
    out.append(T(x + w / 2, PANEL_H - 10, "Exercise is the signal to rebuild.", 10, 600, INK2, "middle", italic=True))
    return "".join(out)


def lens_cone():
    lx, ly = _back(*LENS)
    return (f'<path d="M{_f(lx + 6)},{_f(ly - 7)} L{P3X + 2},{38} L{P3X + 2},{170} L{_f(lx + 6)},{_f(ly + 7)} Z" '
            f'fill="#2E8FC8" fill-opacity=".08" stroke="none"/>'
            f'<path d="M{_f(lx + 6)},{_f(ly - 7)} L{P3X + 2},{38} M{_f(lx + 6)},{_f(ly + 7)} L{P3X + 2},{170}" '
            f'stroke="#2E8FC8" stroke-width="1.1" stroke-dasharray="3 3" fill="none"/>')


# ============================================================== key strip
def _sw_muscle():
    return (f'<rect x="-12" y="-7" width="24" height="14" rx="4" fill="url(#ts-mus)" stroke="{MUS_EDGE}" stroke-width="1"/>'
            f'<path d="M-7,-5 L-3,5 M-1,-5 L3,5 M5,-5 L9,5" stroke="{MUS_FIB}" stroke-width=".9" opacity=".6"/>')


def _sw_tendon():
    return (f'<rect x="-12" y="-5" width="24" height="10" rx="5" fill="url(#ts-ten)" stroke="{TEN_EDGE}" stroke-width="1"/>'
            f'<path d="M-8,-1.5 H8 M-8,1.8 H8" stroke="{TEN_FIB}" stroke-width=".8"/>')


def _sw_bone():
    return f'<rect x="-12" y="-7" width="24" height="14" rx="4" fill="url(#ts-bone)" stroke="{BONE_EDGE}" stroke-width="1"/>'


def _sw_bursa():
    return (f'<path d="M-12,1 C-8,-7 8,-7 12,1 C8,6 -8,6 -12,1 Z" fill="url(#ts-bur)" stroke="{BURSA_EDGE}" stroke-width="1"/>')


def _sw_fibers():
    return (f'<rect x="-12" y="-8" width="24" height="16" rx="3" fill="{FIELD}"/>'
            + "".join(f'<rect x="-11" y="{y}" width="22" height="4" rx="2" fill="url(#ts-ten)" stroke="{TEN_EDGE}" stroke-width=".5"/>'
                      for y in (-7, -2, 3)))


def _sw_fray():
    return (f'<rect x="-14" y="-3" width="8" height="6" rx="3" fill="url(#ts-ten)" stroke="{TEN_EDGE}" stroke-width=".6"/>'
            f'<rect x="6" y="-3" width="8" height="6" rx="3" fill="url(#ts-ten)" stroke="{TEN_EDGE}" stroke-width=".6"/>'
            + _frayed(-8, 8, 0, 4, 5.5, 1.15))


def _sw_vessel():
    return _vessel([(-12, 3), (-4, -1), (4, 3), (12, -2)]) + _vessel([(-4, -1), (-1, -7)], 1.2)


KEY_ITEMS = [(_sw_muscle, "Muscle"), (_sw_tendon, "Tendon"), (_sw_bone, "Bone"), (_sw_bursa, "Irritated bursa"),
             (_sw_fibers, "Collagen fibers"), (_sw_fray, "Frayed fibers"), (_sw_vessel, "New blood vessels")]


def key_strip(y):
    fs = 11
    out = [f'<rect x=".6" y="{y}" width="{W - 1.2}" height="{KEY_H}" rx="8" fill="#FFFFFF" stroke="#CFD6DA" stroke-width="1.2"/>',
           T(14, y + KEY_H / 2 + 3.8, "KEY", 10.5, 800, INK, ls=1.3)]
    start, sw_w, gap = 54, 26, 7
    total = sum(sw_w + gap + tw(lab, fs, 600) for _, lab in KEY_ITEMS)
    space = (W - 14 - start - total) / (len(KEY_ITEMS) - 1)
    x = start
    for sw, lab in KEY_ITEMS:
        out.append(f'<g transform="translate({_f(x + sw_w / 2)},{_f(y + KEY_H / 2)})">{sw()}</g>')
        out.append(T(_f(x + sw_w + gap), y + KEY_H / 2 + 3.9, lab, fs, 600, INK))
        x += sw_w + gap + tw(lab, fs, 600) + space
    return "".join(out)


def art_cuff(t=None):
    body = [plate_defs(), panel_front(), panel_back(), panel_zoom(), lens_cone(), key_strip(KEY_Y)]
    return svg(W, H, "".join(body),
               "The rotator cuff seen from the front and from the back: four muscles whose tendons wrap the ball "
               "of the arm bone, the acromion roof and the bursa beneath it; and a magnified view of healthy, "
               "parallel collagen fibers beside frayed, overloaded fibers with new blood vessels.")


# ============================================================== blocks under the art
def _ic(body, px, sw=3.0, color="currentColor"):
    """Line icon on the kit's 64 grid (same look as kit.icon) for this sheet's own drawings."""
    return (f'<svg class="ic" viewBox="0 0 64 64" style="width:{px};height:{px};color:{color}" fill="none" '
            f'stroke="currentColor" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round" '
            f'aria-hidden="true">{body}</svg>')


SPOT = "#F15F3F"     # coral: where it usually hurts (named in the section's own key)


def _spot(x, y):
    return (f'<circle cx="{x}" cy="{y}" r="9.5" fill="{SPOT}" fill-opacity=".22" stroke="none"/>'
            f'<circle cx="{x}" cy="{y}" r="5" fill="{SPOT}" stroke="#fff" stroke-width="1.6"/>')


SITE_ICONS = {  # 64-grid silhouettes (soft fill, theme outline), each with its pain spot
    # head and shoulders from the front; the spot sits on the person's right shoulder
    "shoulder": ('<circle cx="32" cy="13.5" r="8.5" fill="#E3EEF6"/>'
                 '<path d="M7 62V49C7 37.5 15 31 27 28.6V24h10v4.6C49 31 57 37.5 57 49v13z" fill="#E3EEF6"/>'
                 '<path d="M16 43v19M48 43v19"/>' + _spot(15.5, 35.5)),
    # a bent arm, fist up (upper arm across, forearm rising to the fist); the spot sits on the outer elbow
    "elbow": ('<path d="M3 31C10 24.5 21 22 30 26.5c4.5 2.2 7.5 4.3 9.5 6.5L41.5 18c-3-1.5-4-5.5-2.2-9 2-4 7.5-5.4 12.4-4.2'
              ' 4.6 1.2 7 4.6 6.6 8.7-.3 3.2-1.8 5.4-3.8 6.6L57 41c.4 5.3-2.6 9.6-8.4 10.8-6.6 1.3-14.5.8-23-.6L3 48z" fill="#E3EEF6"/>'
              '<path d="M43.5 11.5c2.8-1.6 6.6-1.2 8.6.6M41.5 18c3.8 1.5 8.4 1.6 12.4.4"/>' + _spot(52, 45)),
    # lower leg and foot from the side; the spot sits on the Achilles tendon above the heel
    "heel": ('<path d="M20 2c-5.5 10-6 20-1.5 30 2.5 5.5 3.5 9 2 14-2 5.5-1 12 5.5 12H55c4.5 0 6-3 4-5.5-2-2.5-9-4-14-7'
             '-4-2.5-5.5-5.5-6-10.5C38 25 37 14 37 2" fill="#E3EEF6"/>' + _spot(21.5, 40.5)),
}

# Where tendon pain shows up.  Shoulder: pain on the outer upper arm with lifting, night pain lying on it,
# pain reaching behind [LEWIS16][WHITTLE15].  Tennis elbow: pain at the outer bony bump with gripping
# [BISSET15]; tied to forceful, repetitive arm work, not just tennis [SHIRI06].  Achilles: pain 2 to 6 cm
# (about 1 to 2 inches) above the heel, morning stiffness, pain with running and jumping [ACH18].
SITES = [
    ("shoulder", "Shoulder", "rotator cuff",
     ["Ache on the outer upper arm", "Worse when you lift your arm", "Hurts to lie on it at night"]),
    ("elbow", "Elbow", "tennis elbow",
     ["Pain on the outer elbow bump", "Worse when you grip or twist", "Common with gripping work"]),
    ("heel", "Heel", "Achilles tendon",
     ["Pain just above the heel bone", "Stiff with your first steps", "Sore with running or jumping"]),
]

RISK_ICONS = {
    "overhead": ('<circle cx="32" cy="15" r="5"/><path d="M32 21v18M32 39l-7 19M32 39l7 19M32 26 21 12M32 26l11-14"/>'
                 '<path d="M14 9h36"/>'),
    "spike": '<path d="M8 8v48h48"/><path d="M14 46l9-2 9-2 6-26 7 4"/><path d="M44 14l1 7-6 1" />',
}
# What raises your risk: age over 50, diabetes, work with the arm above shoulder height [LEONG19];
# a sudden rise in load [COOK09]; high cholesterol [GIRI22]; smoking [BISHOP15][SHIRI06]; family history
# [HARVIE04]; fluoroquinolone antibiotics and steroids [FDA16][YU19][XERGIA22].
RISKS = [("age", "Age over 50"), ("overhead", "Overhead work or sports"), ("spike", "A sudden jump in training"),
         ("bloodsugar", "Diabetes"), ("tube", "High cholesterol"), ("smoke", "Smoking"), ("dna", "Family history"),
         ("rx", "Some antibiotics and steroids")]


def sites_block():
    cards = "".join(
        f'<div class="tsp-site"><div class="tsp-sic">{_ic(SITE_ICONS[k], "0.54in", 2.6)}</div>'
        f'<div><p><b>{t}</b> <i>{sub}</i></p><ul>{"".join(f"<li>{x}</li>" for x in xs)}</ul></div></div>'
        for k, t, sub, xs in SITES)
    return ('<div class="tsp-h"><span>Where tendon pain shows up</span>'
            f'<em><i class="tsp-dot"></i>where it usually hurts</em></div><div class="tsp-sites">{cards}</div>')


def risk_block():
    cells = "".join(
        f'<div class="tsp-rf"><span class="tsp-disc">'
        f'{_ic(RISK_ICONS[ic], "0.3in", 3.2) if ic in RISK_ICONS else icon(ic, "0.3in", sw=3.0)}</span>'
        f'<span class="tsp-rl">{lab}</span></div>' for ic, lab in RISKS)
    return f'<div class="tsp-h"><span>What raises your risk</span></div><div class="tsp-risk">{cells}</div>'


def pain_block():
    # Pain-monitoring model [SILB07]: 0-2 safe, up to 5 acceptable if it settles by the next morning,
    # above 5 too much; morning pain and stiffness should not build from week to week.
    zone = lambda n: "g" if n <= 2 else ("a" if n <= 5 else "r")
    cells = "".join(f'<span class="tsp-c {zone(n)}">{n}</span>' for n in range(11))
    return ('<div class="tsp-pain"><div><div class="tsp-bh">Your pain guide during exercise '
            '<span>0 = no pain, 10 = the worst pain</span></div>'
            f'<div class="tsp-scale">{cells}</div>'
            '<div class="tsp-zones"><div class="g"><b>0 to 2: safe</b>Keep going.</div>'
            '<div class="a"><b>3 to 5: OK</b>if it settles by the next morning.</div>'
            '<div class="r"><b>6 or more: too much</b>Ease off next time.</div></div></div>'
            # 12-week loading programs [ALF98][BEYER15] (cuff trials run 4 to 16 weeks, Dube 2024 JOSPT PMID 38832666);
            # gains held at a year [BEYER15]
            '<div class="tsp-weeks"><b>12</b><span><strong>weeks</strong> is a typical length for a tendon exercise plan. '
            'Tendons rebuild slowly, and the gains last.</span></div></div>')


def flags_block():
    # Red flags first [CPG24]; heart attack warning signs include arm pain with chest discomfort,
    # shortness of breath or a cold sweat: call 911 [AHA].
    return ('<div class="tsp-flag">' + icon("warning", "0.3in", sw=3.4) +
            '<p><b>Get checked right away</b> for a sudden pop or weakness after a fall or heavy lift, an arm you cannot '
            'lift, a hot, red, swollen joint or a fever, or numbness running down the arm. <b>Shoulder or arm pain with '
            'chest pressure, shortness of breath or a cold sweat can be a heart attack: call 911.</b></p></div>')


def front(t, ed):
    return (f'<div class="tsp"><div class="art tsp-art">{art_cuff(t)}</div>'
            f'{sites_block()}{risk_block()}{pain_block()}{flags_block()}</div>')


CSS = r"""
.tsp .tsp-art svg{display:block;width:100%;height:auto}
.tsp .tsp-h{display:flex;align-items:center;gap:0.1in;margin:0.11in 0 0.05in;font:900 10.5pt/1.2 Merriweather,Georgia,serif;
  color:var(--c1);letter-spacing:.04em;text-transform:uppercase}
.tsp .tsp-h::after{content:"";flex:1;height:2px;border-radius:2px;background:linear-gradient(90deg,var(--soft),rgba(227,238,246,0));order:1}
.tsp .tsp-h em{order:2;font:italic 600 7.6pt Inter,sans-serif;letter-spacing:0;text-transform:none;color:#4A555C;
  display:inline-flex;align-items:center;gap:5px}
.tsp .tsp-dot{display:inline-block;width:9px;height:9px;border-radius:50%;background:#F15F3F;box-shadow:0 0 0 3px rgba(241,95,63,.22)}
.tsp .tsp-sites{display:grid;grid-template-columns:repeat(3,1fr);gap:0.09in}
.tsp .tsp-site{display:flex;gap:0.08in;align-items:center;background:var(--tint);border:1px solid #D9E5EE;border-radius:9px;
  padding:0.06in 0.08in 0.06in 0.06in}
.tsp .tsp-sic{flex:none;width:0.6in;height:0.6in;border-radius:50%;background:#fff;color:var(--c1);display:flex;align-items:center;
  justify-content:center;box-shadow:inset 0 0 0 1.5px rgba(31,94,140,.14)}
.tsp .tsp-site p{margin:0 0 2px;line-height:1.15}
.tsp .tsp-site b{font:800 9.4pt/1.15 Inter,sans-serif;color:var(--deep)}
.tsp .tsp-site i{font:italic 600 7.6pt/1.15 Inter,sans-serif;color:#4A555C;margin-left:3px}
.tsp .tsp-site ul{margin:0;padding:0;list-style:none}
.tsp .tsp-site li{position:relative;padding-left:9px;font-size:7.9pt;line-height:1.28;color:#2B3236;margin:0 0 1px}
.tsp .tsp-site li::before{content:"";position:absolute;left:0;top:4.5px;width:4px;height:4px;border-radius:50%;background:var(--c2)}
.tsp .tsp-risk{display:grid;grid-template-columns:repeat(8,1fr);gap:0 0.04in}
.tsp .tsp-rf{display:flex;flex-direction:column;align-items:center;text-align:center}
.tsp .tsp-disc{width:0.46in;height:0.46in;border-radius:50%;background:var(--soft);color:var(--c1);display:flex;align-items:center;
  justify-content:center;box-shadow:inset 0 0 0 1.5px rgba(31,94,140,.10)}
.tsp .tsp-rl{display:block;font-size:7.7pt;font-weight:600;line-height:1.2;color:#2F373C;margin-top:0.03in}
.tsp .tsp-pain{display:grid;grid-template-columns:1fr 1.95in;gap:0.14in;align-items:center;margin-top:0.12in;border:1px solid #D9E5EE;
  border-radius:9px;padding:0.06in 0.1in 0.07in;background:#fff}
.tsp .tsp-bh{font:900 9.6pt/1.2 Merriweather,Georgia,serif;color:var(--c1);letter-spacing:.03em;text-transform:uppercase;margin:0 0 0.05in}
.tsp .tsp-bh span{font:italic 600 7.4pt Inter,sans-serif;letter-spacing:0;text-transform:none;color:#4A555C;margin-left:6px}
.tsp .tsp-scale{display:grid;grid-template-columns:repeat(11,1fr);gap:2px}
.tsp .tsp-c{display:flex;align-items:center;justify-content:center;height:0.2in;font:800 8pt Inter,sans-serif;color:#fff;border-radius:3px}
.tsp .tsp-c.g{background:#2F8A5E}.tsp .tsp-c.a{background:#B67A0B}.tsp .tsp-c.r{background:#C2392E}
.tsp .tsp-zones{display:grid;grid-template-columns:3fr 3fr 5fr;gap:2px;margin-top:3px}
.tsp .tsp-zones div{font-size:7.5pt;line-height:1.25;color:#2B3236;padding:2px 4px 0;border-top:3px solid}
.tsp .tsp-zones b{display:block;font-size:7.7pt}
.tsp .tsp-zones .g{border-color:#2F8A5E}.tsp .tsp-zones .g b{color:#1F6B47}
.tsp .tsp-zones .a{border-color:#B67A0B}.tsp .tsp-zones .a b{color:#7E5300}
.tsp .tsp-zones .r{border-color:#C2392E}.tsp .tsp-zones .r b{color:#9A2620}
.tsp .tsp-weeks{display:flex;align-items:center;gap:0.08in;background:var(--soft);border-radius:8px;padding:0.06in 0.1in;align-self:stretch}
.tsp .tsp-weeks b{font:900 26pt/1 Merriweather,Georgia,serif;color:var(--c1)}
.tsp .tsp-weeks span{font-size:7.9pt;line-height:1.3;color:#2B3236}
.tsp .tsp-weeks strong{color:var(--deep);font-size:8.6pt}
.tsp .tsp-flag{display:flex;gap:0.08in;align-items:center;margin-top:0.11in;border:1.5px solid #C0392B;background:#FDF1EF;
  border-radius:8px;padding:0.05in 0.1in}
.tsp .tsp-flag .ic{flex:none;color:#B23A30}
.tsp .tsp-flag p{margin:0;font-size:7.9pt;line-height:1.33;color:#2B3236}
.tsp .tsp-flag b{color:#A5281E}
"""

# ============================================================== back-page icons (registered by name for build.life_block)
kit.ICONS.setdefault("ts_steps", '<path d="M6 56h14V44h12V32h12V20h14"/><path d="M10 34 30 14"/><path d="M21 14h9v9"/>')
kit.ICONS.setdefault("ts_ladder", '<path d="M21 58 29 7h6l8 51"/><path d="M24.4 40h15.2M26.6 24h10.8"/><path d="M47 18v20"/>'
                                  '<path d="M42 23l5-5 5 5"/>')

SHEET = {
    "slug": SLUG, "code": "ND-MS-603", "order": 14, "theme": "msk", "series": "Pain and Movement Series",
    "title": "Shoulder and Tendon Pain", "sub": "Rotator cuff, tennis elbow and Achilles",
    # Collagen, mostly type I, is 65-80% of tendon [KANNUS00].  Most tendon pain is overuse, a load the tendon
    # was not ready for [COOK09][MILLAR21], with disorganised (fraying) collagen fibres [MILLAR21].  Shoulder
    # pain: third most common musculoskeletal reason to see primary care [WHITTLE15]; rotator cuff the most
    # common cause [ZHANG25].  Load the right way: exercise is first-line in every guideline [CPG20][LEWIS16],
    # and loading drives collagen building [KJAER04].
    "intro": ("Tendons are tough cords of <b>collagen</b> that join muscle to bone. Most tendon pain is not one big injury: "
              "it builds when a tendon does more than it is ready for, and its rope-like fibers fray. Shoulder pain is the "
              "<b>third most common</b> muscle and joint reason to see a family doctor, usually from the <b>rotator cuff</b>. "
              "The good news: tendons rebuild with the right load."),
    "front": front,
    "css": CSS,
    "back": {
        "life_title": "Lifestyle Recommendations", "life_sub": "Habits that help tendons rebuild", "style": "circle",
        "life": [
            # Loading raises collagen building; inactivity lowers it; overuse needs adjusted loading, not rest [KJAER04]
            ("dumbbell", "Load, don't rest", "Exercise most days. Full rest weakens tendons."),
            # A sudden rise in load drives tendinopathy [COOK09]
            ("ts_steps", "Build up slowly", "Add weight, miles or reps in small steps."),
            # Work with the arm above shoulder height raises cuff risk [LEONG19]
            ("ts_ladder", "Lower your reach", "Keep heavy lifting below shoulder height."),
            # Vitamin C is needed to make collagen [ODS-C]
            ("plate", "Feed the rebuild", "Eat protein and vitamin C foods like citrus."),
            # Adults need 7 to 9 hours [NSF15]; the day's biggest growth hormone pulse comes in deep sleep [VC96]
            ("moon", "Sleep 7 to 9 hours", "Growth hormone peaks in deep sleep."),
            # Smoking is tied to cuff tears, shoulder pain and poorer function [BISHOP15]
            ("smoke", "Stop smoking", "Smoking is tied to more rotator cuff tears."),
        ],
        "cols": [
            {"p": "ts_collagen_renew", "need": "Tendon building blocks", "needsub": "collagen peptides", "start": True,
             "bullets": ["Supports tendons, ligaments and joints",
                         "With TENDOFORTE, studied for tendons"],                          # [PRAET19]
             "dose": "1 scoop daily", "dosesub": "about 1 hour before exercise",          # [SHAW17]
             "sched": [("am", 1, "scoop")]},
            {"p": "ts_vitamin_c_1000", "need": "Build collagen", "needsub": "vitamin C",
             "bullets": ["Your body needs it to build collagen",                           # [ODS-C]
                         "Collagen Renew has none, so pair them"],                        # labels.json R190: no vitamin C
             "dose": "1 capsule daily", "dosesub": "with your collagen", "sched": [("am", 1, "capsule")]},
            {"p": "ts_inflam_eze_plus", "need": "Comfort after activity", "needsub": "ginger, curcumin, boswellia",
             "bullets": ["Supports joint and muscle comfort", "Supports a healthy inflammatory response"],
             "dose": "3 capsules daily", "dosesub": "with food", "sched": [("pm", 3, "capsules")]},
            {"p": "omega_1000", "need": "Inflammatory balance", "needsub": "omega-3s EPA and DHA",
             "bullets": ["Supports a balanced inflammatory response", "Supports muscle, joint and heart health"],
             "dose": "2 softgels daily", "dosesub": "with your evening meal",     # label: up to 3 a day with food
             "sched": [("pm", 2, "softgels")]},
            {"p": "ts_d3_5000_k2", "need": "Muscle and bone", "needsub": "vitamin D3 with K2",
             "bullets": ["Supports muscle and bone health",
                         "High dose: check your vitamin D level first"],   # 5,000 IU is above the 4,000 IU adult UL (NIH ODS)
             "dose": "1 softgel daily", "dosesub": "with breakfast", "sched": [("am", 1, "softgel")]},
        ],
        # Edition-aware via {who}: "your provider" (practitioner) / "your pharmacist" (pharmacy).
        "rx": [
            # Omega-3s and these herbs may add to anticoagulant effects; vitamin K counters warfarin (NIH ODS fact sheets)
            "<b>Blood thinner or aspirin?</b> Fish oil and Inflam-Eze Plus herbs can add to bleeding, and the vitamin K in "
            "D3 5000 with K2 affects warfarin. Ask {who}.",
            # [FDA16][YU19]
            "<b>Fluoroquinolone antibiotics</b> (ciprofloxacin, levofloxacin) can injure tendons, more so after 60 or with "
            "steroids. Tendon pain on one? Call your prescriber.",
            # White willow bark carries salicin, a salicylate (labels.json R856: 200 mg, 25% salicin)
            "<b>Aspirin allergy?</b> White willow in Inflam-Eze Plus is a salicylate: skip it. Ask {who} before pairing it "
            "with ibuprofen or naproxen.",
        ],
    },
}
