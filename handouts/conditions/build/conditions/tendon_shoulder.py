"""Shoulder and Tendon Pain (ND-MS-603), Pain and Movement Series.  Slug "tendon-shoulder".

Self-contained sheet module (wave 2, nothing from the legacy sheets.py / art.py).

FRONT, top to bottom
  intro (it says what the rotator cuff is) -> one inline-SVG plate with three panels and a KEY strip:
     1. ROTATOR CUFF FROM THE FRONT: subscapularis, the supraspinatus tendon, the acromion "roof", the collarbone
        and the bursa, drawn red under the roof and keyed "Sore bursa" ("a cushion between the roof and cuff; it can
        get sore and swollen, as shown"); the bicipital groove is drawn in this view only, on the shaft below the ball;
     2. ROTATOR CUFF FROM THE BACK: supraspinatus, infraspinatus, teres minor along the outer border of the shoulder
        blade (the lower third of that border and the inferior angle left bare), with a lens on
        the supraspinatus band of the cuff, just lateral to the acromion, that opens into panel 3;
     3. INSIDE A TENDON ("the circled spot, magnified many times"): healthy collagen (tight, parallel bundles with an
        even crimp) beside an overloaded tendon (uneven fibers pulled apart, two slipped out of line and crossing the
        others, two broken with frayed gold ends, new blood vessels).  Under it, in its own box, HOW TENDONS GET
        STRONGER: plain physiology true of every tendon (load it -> feed it -> sleep on it), the same three habits as
        the back's lifestyle row.  No product and no timing on the front: the 1-hour collagen timing lives on the
        back, as the Collagen Renew direction.
  -> where tendon pain shows up (shoulder, elbow, ankle; coral dot keyed in the header)
  -> what raises your risk (8 icons) -> the exercise pain guide (0-10 traffic light + "12 weeks")
  -> when to get checked right away (shoulder AND Achilles red flags; 911 for arm pain with heart-attack signs).
BACK: six lifestyle circles; five NutriDyn columns (Collagen Renew starts, Vitamin C 1000 is its pair,
Inflam-Eze Plus, Omega Pure EPA-DHA 1000, D3 5000 with K2) on a shared four-row subgrid, so names, bullets, serving
facts and dose bars line up; a two-slot rhythm (no bedtime products) in which Vitamin C 1000 rides with the scoop;
five edition-aware checks ({who}) that carry every caution the sibling Pain and Movement sheets give for the same
products (bleeding and surgery, aspirin allergy, red-meat alpha-gal and fish allergy, diabetes medicine, yellow skin
or dark urine means stop, under 18, pregnancy and nursing, sleep aids and other medicines, ulcer, gallstones, liver
and kidney disease), plus the fluoroquinolone tendon warning.
Products: all five are ts_* entries in products.d/tendon-shoulder.json (label facts + "src"); sheet-specific dose
lines and schedules are set per column below.

CSS scoping: the front lives inside .tsp.  Back-page rules are scoped with .sheet.back:has(.tsp-bk), an empty
marker span in this sheet's lifestyle title (photo files are pooled across sheets, so their names cannot mark it).

Geometry: the anatomy is drawn once in "scapula units" (posterior view of a right shoulder blade,
medial border at x = 0, inferior angle at y = 1.0, about 16 cm in life) and mapped into each panel;
the front view is the same bones mirrored, with the front-only parts (coracoid, collarbone,
subscapularis) added.  Every SVG id starts with "ts-", every CSS class with "tsp-".

SOURCES (each number or fact on the page carries one of these tags in a comment)
  [KANNUS00]  Kannus P. Structure of the tendon connective tissue. Scand J Med Sci Sports 2000;10:312-20.
              PMID 11085557. Collagen, mostly type I, is 65-80% of tendon dry mass; fibres packed in bundles.
  [KHAN99]    Khan KM et al. Histopathology of common tendinopathies. Sports Med 1999;27:393-408. PMID 10418074.
              Healthy: tightly packed, parallel collagen bundles.  Painful tendon: discontinuous, disorganised
              fibres, more ground substance between them, prominent capillary (new vessel) growth.
  [RUI11]     Rui YF et al. Knee Surg Sports Traumatol Arthrosc 2012;20:1409-17. PMID 21946950. Loss of the
              collagen crimp structure in tendinopathy samples (healthy tendon keeps a regular crimp).
  [MILLAR21]  Millar NL et al. Tendinopathy. Nat Rev Dis Primers 2021;7:1. PMID 33414454. Commonest sites:
              rotator cuff, elbow, patellar, gluteal, Achilles; disorganised collagen fibres, more small
              vessels and sensory nerves.
  [ANAT]      Standard anatomy (e.g. Gray's Anatomy): the rotator cuff is supraspinatus, infraspinatus, teres minor
              and subscapularis, whose tendons blend into one cuff over the ball of the arm bone and hold it in the
              socket; the subacromial bursa lies between the cuff and the acromion and can become sore and swollen.
              The caption gives no mechanism on purpose: the older "the roof pinches it" (impingement) model is no
              longer taken as the cause of the pain, which is uncertain [LEWIS16].  Teres minor arises from the upper
              two-thirds of the lateral border of the scapula; the supraspinatus helps lift the arm, infraspinatus
              and teres minor turn it out, subscapularis turns it in.
  [COOK09]    Cook JL, Purdam CR. Br J Sports Med 2009;43:409-16. PMID 18812414 (load-induced tendinopathy).
  [KHAN02]    Khan KM et al. Time to abandon the "tendinitis" myth. BMJ 2002;324:626-7. PMID 11895810.
  [WHITTLE15] Whittle S, Buchbinder R. In the clinic: rotator cuff disease. Ann Intern Med 2015;162:ITC1-15.
              PMID 25560729. Shoulder pain is the third most frequent musculoskeletal reason to present
              to primary care.
  [ZHANG25]   Zhang W et al. J Orthop Surg Res 2025;20:1075. PMID 41276811. Rotator cuff-related shoulder
              pain is the most common cause of shoulder pain.
  [LEWIS16]   Lewis J. Man Ther 2016;23:57-68. PMID 27083390, doi:10.1016/j.math.2016.03.009 (abstract read via
              PubMed, 2026-11-03). A graduated exercise approach gives at least the benefit of surgery for
              subacromial pain, cuff tendinopathy and atraumatic tears; the "cause and source of symptoms" is listed
              among the open uncertainties, so the bursa caption states no pinching mechanism.
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
              rupture, risk higher over age 60 and with corticosteroids; the 2016 safety communication tells
              patients to stop the drug and call their health care professional right away at the first tendon pain.
  [XERGIA22]  Xergia SA et al. Phys Sportsmed 2023;51:506-16. PMID 35670156. Achilles rupture: steroids,
              quinolones.
  [BIGGS21]   Biggs A et al. Achilles tendon rupture: what you need to know. Br J Hosp Med 2021;82:1-7.
              PMID 33646025. Heel pain and a "pop" are the classic history; often missed or called a sprain.
  [CHIODO10]  Chiodo CP et al. AAOS guideline, acute Achilles tendon rupture. J Am Acad Orthop Surg
              2010;18:503-10. PMID 20675643 (exam: weak push-off, i.e. cannot rise on the toes; palpable gap).
  [SHIRI06]   Shiri R et al. Am J Epidemiol 2006;164:1065-74. PMID 16968862. Tennis elbow in 1.3% of adults
              30-64; forceful plus repetitive arm work (OR 5.6); smoking.
  [BISSET15]  Bisset LM, Vicenzino B. J Physiother 2015;61:174-81. PMID 26361816 (lateral elbow pain, gripping).
  [ACH18]     Martin RL et al. APTA midportion Achilles tendinopathy guideline. JOSPT 2018;48(5):A1-A38.
              PMID 29712543. Pain 2-6 cm above the heel insertion, morning stiffness, pain with loading.
  [SHAW17]    Shaw G et al. Am J Clin Nutr 2017;105:136-43. PMID 27852613. Vitamin C-enriched gelatin:
              amino acids peak 1 h after; 15 g 1 h before exercise doubled a collagen-synthesis marker
              (8 healthy men).  Used only for the back-page Collagen Renew timing, never on the front.
  [PRAET19]   Praet SFE et al. Nutrients 2019;11:76. PMID 30609761. TENDOFORTE peptides + calf loading (20-patient
              pilot).  Not cited on the page; the back states the formulation fact only.
  [BISCHOF24] Bischof K et al. Sports Med 2024;54:2865-88. PMID 39060741. 19 RCTs, collagen + training; tendon
              outcomes very low certainty.  Not cited on the page.
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

# ============================================================== text measuring (Inter metrics)
_FACES = {}
_WEIGHTS = {400: "Regular", 500: "Medium", 600: "SemiBold", 700: "Bold", 800: "ExtraBold", 900: "Black"}
_FONT_DIRS = ("/usr/share/fonts/opentype/inter", "/usr/share/fonts/truetype/inter",
              os.path.expanduser("~/Library/Fonts"), "/Library/Fonts")
_ADV = {  # Inter advance widths, 1/1000 em, for chr(32)..chr(126); generated from the Inter 4 OTFs
    500: ("267 304 494 639 646 993 653 313 369 369 521 667 303 462 303 370 646 415 616 627 656 618 630 571 629 630 303 315 667 667 667 527 982 709 657 733 722 603 589 748 745 272 575 688 565 913 756 767 "
          "642 769 648 646 653 740 709 1003 701 696 641 369 370 369 477 463 337 568 618 577 618 587 379 620 602 252 252 559 252 888 602 604 618 618 387 539 340 602 575 829 557 575 559 440 346 440 667"),
    600: ("252 321 523 644 650 1004 663 326 373 373 540 673 319 465 319 379 660 423 623 636 666 629 640 576 640 640 319 329 673 673 673 543 999 728 659 737 722 605 588 749 746 277 580 703 565 922 759 769 "
          "645 773 652 650 660 736 728 1020 720 713 652 373 379 373 481 469 351 574 624 583 624 591 389 625 612 262 262 569 262 900 612 609 624 624 397 549 353 612 587 839 569 588 566 455 359 455 673"),
    700: ("237 338 552 649 655 1016 672 339 377 377 559 679 334 468 334 388 674 431 630 646 676 639 649 582 651 649 334 343 679 679 679 560 1016 747 662 740 722 607 587 750 747 281 584 719 565 932 762 771 "
          "648 777 657 655 667 732 747 1038 738 731 664 377 388 377 487 476 365 581 630 588 630 596 398 632 623 271 271 580 271 913 623 613 630 630 407 560 366 623 600 850 580 602 573 469 372 469 679"),
    800: ("219 358 586 655 660 1029 683 354 382 382 583 686 353 471 353 400 692 441 638 657 688 652 662 588 664 662 353 360 686 686 686 579 1036 770 665 744 723 610 585 752 749 286 590 738 565 943 766 773 "
          "652 782 662 660 677 727 770 1059 761 752 679 382 400 382 493 484 382 588 638 595 638 601 410 639 635 283 283 593 283 927 635 619 638 638 420 573 382 635 615 863 594 618 581 486 388 486 686"),
}
_TAB = {}


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
    """Advance width of `text` in Inter at `size` px.  The installed Inter OTF through Pillow when it is there;
    otherwise the embedded Inter width table (_ADV, within 2% of the shaped width), so layout never rests on a guess."""
    try:
        w = _face(_WEIGHTS[weight]).getlength(text) * size / 100
    except Exception:
        k = min(_ADV, key=lambda v: abs(v - weight))
        if k not in _TAB:
            _TAB[k] = [int(v) for v in _ADV[k].split()]
        tab = _TAB[k]
        w = sum(tab[ord(c) - 32] if 32 <= ord(c) < 127 else tab[0] for c in text) * size / 1000
    return w + ls * len(text)


# ============================================================== palette (every colour-coded thing is in the KEY)
INK, INK2 = "#23292D", "#56616A"
MUS, MUS_D, MUS_EDGE, MUS_FIB = "#F2A39A", "#CF625C", "#9E3F3B", "#B5504B"      # muscle: pink
TEN, TEN_D, TEN_EDGE, TEN_FIB = "#FFFDF7", "#EADFCB", "#B9A989", "#D9CCB2"      # tendon: white / ivory
BONE, BONE_D, BONE_EDGE = "#F7EAD0", "#DDC296", "#A9864F"                       # bone: tan
BURSA, BURSA_D, BURSA_EDGE = "#EC5A50", "#C12F2A", "#8F1F1B"                    # sore bursa: red
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
KEY_Y = 308                    # KEY_H and H follow the KEY layout (key strip section)
OY = 66                        # anatomy origin y (scapula superior angle)
FRONT_X = P1X + 64             # screen x of the lateral edge (x = AX) in the mirrored front view: leaves a clear
                               # margin left of the arm bone for the bursa label
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


def _poly(pts):
    return "M" + " L".join(f"{_f(a)},{_f(b)}" for a, b in pts)


def _ribbon(top, bot):
    """Closed outline of a ribbon from its top and bottom edge points (left to right)."""
    return _poly(top) + " L" + " L".join(f"{_f(a)},{_f(b)}" for a, b in reversed(bot)) + "Z"


# ---- bones (scapula units, posterior view of a right shoulder; third value = curve tension)
SCAPULA = [
    (0.075, 0.000, 0.5), (0.200, 0.030, 1.0), (0.330, 0.062, 1.0), (0.405, 0.080, 0.8), (0.432, 0.103, 0.4),
    (0.468, 0.090, 0.6), (0.530, 0.083, 1.0), (0.585, 0.106, 0.8), (0.632, 0.132, 0.6), (0.655, 0.182, 1.0),
    (0.662, 0.236, 1.0), (0.652, 0.296, 1.0), (0.628, 0.340, 0.6), (0.585, 0.398, 1.0), (0.505, 0.528, 1.0),
    (0.410, 0.678, 1.0), (0.320, 0.822, 1.0), (0.250, 0.936, 0.9), (0.205, 1.000, 0.35), (0.158, 0.972, 0.9),
    (0.105, 0.860, 1.0), (0.055, 0.640, 1.0), (0.018, 0.420, 1.0), (0.000, 0.256, 0.6), (0.018, 0.120, 1.0),
    (0.045, 0.035, 0.8),
]
# The front view's shoulder blade: the same outline, except that its neck (points 8 and 9) reaches out under the
# coracoid to the ball, as the bone does in life, so no bare paper shows between the ball, the coracoid and the blade
# where the socket sits.  Both moved points lie under the coracoid and the arm bone, so the new outline stays hidden.
# The back view keeps SCAPULA: there the cuff covers this corner, and teres minor's border samples (_LAT, points
# 12-16) come from it, so nothing there moves.
SCAPULA_FRONT = SCAPULA[:8] + [(0.650, 0.128, 1.0), (0.700, 0.175, 1.0)] + SCAPULA[10:]
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
CLAVICLE = [  # collarbone: a gentle S from the acromion toward the breastbone; it runs on past the panel edge, where
    # the panel clip cuts it, so it never ends in a stub inside the picture
    (0.672, -0.020, 0.6), (0.610, -0.030, 1.0), (0.520, -0.040, 1.0), (0.400, -0.058, 1.0), (0.270, -0.060, 1.0),
    (0.140, -0.050, 1.0), (0.010, -0.040, 1.0), (-0.120, -0.048, 1.0), (-0.280, -0.066, 1.0), (-0.450, -0.082, 0.3),
    (-0.450, 0.000, 0.3), (-0.280, 0.006, 1.0), (-0.120, 0.012, 1.0), (0.010, 0.020, 1.0), (0.140, 0.020, 1.0),
    (0.270, 0.010, 1.0), (0.400, 0.006, 1.0), (0.520, 0.014, 1.0), (0.610, 0.026, 1.0), (0.668, 0.036, 0.6),
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
SUPRA = [  # supraspinatus belly, above the spine.  It runs on under the acromion, so its rounded tip (x = 0.60) ends
    # where the spine covers it completely (the spine spans y 0.035-0.16 there) and no stub shows below the roof; its
    # tendon comes out from under the acromion as the top band of the cuff hood.
    (0.060, 0.030, 0.7), (0.180, 0.028, 1.0), (0.320, 0.050, 1.0), (0.450, 0.066, 1.0), (0.560, 0.070, 1.0),
    (0.600, 0.080, 0.8), (0.602, 0.118, 0.8), (0.560, 0.122, 1.0), (0.450, 0.152, 1.0), (0.320, 0.186, 1.0),
    (0.180, 0.214, 1.0), (0.050, 0.236, 0.7), (0.028, 0.130, 1.0),
]
SUPRA_FRONT = [  # the same muscle seen from the front: a strip above the shoulder blade, behind the collarbone
    (0.080, -0.010, 0.7), (0.200, -0.020, 1.0), (0.340, -0.010, 1.0), (0.460, 0.010, 1.0), (0.560, 0.030, 1.0),
    (0.640, 0.060, 1.0), (0.646, 0.112, 1.0), (0.560, 0.098, 1.0), (0.460, 0.082, 1.0), (0.340, 0.066, 1.0),
    (0.200, 0.040, 1.0), (0.085, 0.022, 0.7),
]
def _cr_samples(P, per=32):
    """Dense samples of the closed Catmull-Rom curve through P [(x, y, tension)], with the same tangents and
    Bezier handles as _path, so a shape built from them lies exactly on the drawn outline (scapula units)."""
    n = len(P)
    tan = [(P[i][2] * (P[(i + 1) % n][0] - P[i - 1][0]) / 2, P[i][2] * (P[(i + 1) % n][1] - P[i - 1][1]) / 2)
           for i in range(n)]
    out = []
    for i in range(n):
        j = (i + 1) % n
        p0, p3 = P[i][:2], P[j][:2]
        p1 = (p0[0] + tan[i][0] / 3, p0[1] + tan[i][1] / 3)
        p2 = (p3[0] - tan[j][0] / 3, p3[1] - tan[j][1] / 3)
        for s in range(per):
            t = s / per
            u = 1 - t
            out.append(tuple(u ** 3 * p0[c] + 3 * u * u * t * p1[c] + 3 * u * t * t * p2[c] + t ** 3 * p3[c]
                             for c in (0, 1)))
    return out


# The lateral (outer) border of the shoulder blade, from just under the socket down toward the inferior angle:
# SCAPULA points 12 -> 16, sampled from the drawn curve.
_LAT = _cr_samples(SCAPULA)[12 * 32:16 * 32 + 1]


def _on_border(y):
    """(point, downward unit direction, outward unit normal) of the lateral border at height y."""
    for a, b in zip(_LAT, _LAT[1:]):
        if a[1] <= y <= b[1]:
            t = (y - a[1]) / (b[1] - a[1])
            p = (a[0] + (b[0] - a[0]) * t, y)
            ln = math.hypot(b[0] - a[0], b[1] - a[1])
            d = ((b[0] - a[0]) / ln, (b[1] - a[1]) / ln)
            return p, d, (d[1], -d[0])          # the border runs down and in, so (dy, -dx) points out of the bone
    raise ValueError(y)


# Teres minor arises from the upper two-thirds of the lateral border of the shoulder blade and runs up and out to the
# lowest facet of the greater tubercle, under infraspinatus [ANAT].  Its outer edge is the border itself (a hair
# outside, so the muscle covers the bone's outline and no bone shows between them); its inner edge is the border
# moved TM_W inward, narrowing toward the lower end.  Below it, along the lower third of the border, the bone is left
# bare: that is where teres major starts (not a cuff muscle, not drawn), and the inferior angle carries the
# "Shoulder blade" label.
TM_Y0, TM_Y1, TM_W, TM_OUT = 0.378, 0.735, 0.070, 0.006


def _tm_edges():
    """Parallel inner and outer edge points of teres minor, from its insertion under the cuff to its lower end."""
    inner = [(0.684, 0.304), (0.616, 0.318)]          # into the cuff's lowest band, between the seam and the hood edge
    outer = [(0.688, 0.354), (0.646, 0.361)]
    k = 9
    for i in range(k + 1):
        u = i / k
        p, d, nrm = _on_border(TM_Y0 + (TM_Y1 - TM_Y0) * u)
        w = TM_W - 0.024 * max(0.0, (u - 0.55) / 0.45) ** 1.5      # narrows over its lower part
        inner.append((p[0] - w * nrm[0], p[1] - w * nrm[1]))
        outer.append((p[0] + TM_OUT * nrm[0], p[1] + TM_OUT * nrm[1]))
    return inner, outer


TM_IN, TM_OUTER = _tm_edges()
_tp, _td, _tn = _on_border(TM_Y1)
TM_END = (_tp[0] + 0.016 * _td[0] - 0.016 * _tn[0], _tp[1] + 0.016 * _td[1] - 0.016 * _tn[1])   # rounded lower end
TMINOR = ([(x, y, 1.0) for x, y in TM_IN] + [(*TM_END, 0.9)] + [(x, y, 1.0) for x, y in reversed(TM_OUTER)])
TMINOR[0] = (*TMINOR[0][:2], 0.8)
TMINOR[-1] = (*TMINOR[-1][:2], 0.8)
# a point on teres minor's mid-line, half-way down its origin, for the label leader
_mp, _md, _mn = _on_border(0.56)
TM_MID = (_mp[0] - TM_W / 2 * _mn[0], _mp[1] - TM_W / 2 * _mn[1])

# Infraspinatus fills the fossa below the spine.  Its lower edge runs UNDER teres minor (along teres minor's
# mid-line, drawn first so teres minor covers it), leaves it at teres minor's lower end and crosses to the inner
# border just above the inferior angle, so no bone shows between the two muscles or between them and the border.
_im = [((a[0] + b[0]) / 2, (a[1] + b[1]) / 2) for a, b in zip(TM_IN[2:], TM_OUTER[2:])]
INFRA = ([(0.040, 0.300, 0.7), (0.160, 0.276, 1.0), (0.300, 0.246, 1.0), (0.450, 0.212, 1.0), (0.560, 0.200, 1.0),
          (0.672, 0.212, 0.8), (0.684, 0.302, 0.8), (0.640, 0.336, 1.0)]
         + [(x, y, 1.0) for x, y in _im[::3]] + [(*TM_END, 0.8)]          # _im[::3] ends on _im[-1]
         + [(0.300, 0.770, 1.0), (0.200, 0.800, 1.0), (0.112, 0.815, 0.7), (0.077, 0.700, 1.0),
            (0.058, 0.590, 1.0), (0.030, 0.450, 1.0)])
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
# Bicipital groove, FRONT VIEW ONLY (it lies on the front of the arm bone, so the back view never shows it).  It runs
# down from between the two bony bumps (greater and lesser tubercles), so it starts just below the ball (the ball's
# lower rim is at y 0.40 at this x) and stays 2-5 px inside the outer edge of the shaft: start, control, end.
GROOVE = [(0.862, 0.425), (0.851, 0.540), (0.844, 0.760)]


def bursa_pts():
    """The bursa as a soft pillow following the ball: thin under the acromion, fullest over the outer side.
    It starts at 236 degrees, where its inner tip lies under the coracoid (x 0.69, y 0.145), so no red speck shows
    below the coracoid's hook."""
    cx, cy = HEAD_C
    ri = HEAD_R + 0.024
    a0, a1, n = 236.0, 352.0, 20
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


def _strap(uid, pts, inner, outer, m, n):
    """A long, curving strap muscle (teres minor): the same pink, edge and highlight as _muscle, but its fibre lines
    follow the strap's own curve, between matching points of its inner and outer edges, instead of running straight."""
    d = _path(pts, m)
    lines = []
    for i in range(n):
        f = (i + 0.5) / n
        mid = [(a[0] + (b[0] - a[0]) * f, a[1] + (b[1] - a[1]) * f, 1.0) for a, b in zip(inner, outer)]
        lines.append(_path(mid, m, closed=False))
    return (f'<path d="{d}" fill="url(#ts-mus)" stroke="{MUS_EDGE}" stroke-width="1.1" stroke-linejoin="round"/>'
            f'<clipPath id="{uid}"><path d="{d}"/></clipPath>'
            f'<path d="{"".join(lines)}" stroke="{MUS_FIB}" stroke-width=".9" opacity=".5" fill="none" '
            f'stroke-linecap="round" clip-path="url(#{uid})"/>'
            + f'<path d="{d}" fill="url(#ts-mhi)" stroke="none"/>')


def _hood(uid, pts, m, src, dst, n, seams=(), bow=-0.022, fade=0.07, top=None):
    """Tendon that wraps the ball: ivory, lit from the upper left, fine collagen lines curving over the ball.
    Its first `fade` scapula units (from the muscle end, src) fade in, so the muscle flows into the tendon.
    top = (seam, x0, x1): the band above `seam` (one of `seams`) belongs to a muscle that ends under a bone, not in the
    open (the supraspinatus, under the acromion).  Its muscle cannot show through, so a long fade there would only
    let the ball and its outline show through as a pale strip; that band gets its own short fade, from x0 to x1
    (scapula units, at its very edge), and is solid beyond it."""
    out = [_shape(pts, m, "url(#ts-cuff)", TEN_EDGE, 1.0),
           _fibers(uid, pts, m, src, dst, n, TEN_FIB, 0.8, 0.95, bow)]
    for sm in seams:
        out.append(f'<path d="{_path(sm, m, closed=False)}" stroke="#C6B593" stroke-width="1.1" fill="none"/>')
    (sx0, sy0), (sx1, sy1) = _lerp(src[0], src[1], .5), _lerp(dst[0], dst[1], .5)
    ln = math.hypot(sx1 - sx0, sy1 - sy0)
    a, b = m(sx0, sy0), m(sx0 + (sx1 - sx0) * fade / ln, sy0 + (sy1 - sy0) * fade / ln)
    big = 400
    grads = (f'<linearGradient id="{uid}-g" gradientUnits="userSpaceOnUse" x1="{_f(a[0])}" y1="{_f(a[1])}" '
             f'x2="{_f(b[0])}" y2="{_f(b[1])}"><stop offset="0" stop-color="#fff" stop-opacity="0"/>'
             f'<stop offset="1" stop-color="#fff"/></linearGradient>')
    band = ""
    if top:
        seam, x0, x1 = top
        (tx0, _), (tx1, _) = m(x0, 0), m(x1, 0)
        grads += (f'<linearGradient id="{uid}-t" gradientUnits="userSpaceOnUse" x1="{_f(tx0)}" y1="0" x2="{_f(tx1)}" '
                  f'y2="0"><stop offset="0" stop-color="#fff" stop-opacity="0"/><stop offset="1" stop-color="#fff"/>'
                  f'</linearGradient>')
        # the region above the seam: the seam's own curve (traced right to left) is its lower edge, so the solid band
        # ends exactly on the drawn seam line
        (lx, ly), (rx, ry) = m(seam[0][0] - 0.10, seam[0][1]), m(seam[-1][0] + 0.10, seam[-1][1])
        (ux, uy), (vx, vy) = m(seam[0][0] - 0.10, -0.40), m(seam[-1][0] + 0.10, -0.40)
        back = _path(list(reversed(seam)), m, closed=False).replace("M", "L", 1)
        band = (f'<path d="M{_f(ux)},{_f(uy)} L{_f(vx)},{_f(vy)} L{_f(rx)},{_f(ry)} {back} L{_f(lx)},{_f(ly)}Z" '
                f'fill="url(#{uid}-t)"/>')
    return (grads +
            f'<mask id="{uid}-m" maskUnits="userSpaceOnUse" x="{-big}" y="{-big}" width="{3 * big}" height="{3 * big}">'
            f'<rect x="{-big}" y="{-big}" width="{3 * big}" height="{3 * big}" fill="url(#{uid}-g)"/>{band}</mask>'
            f'<g mask="url(#{uid}-m)">{"".join(out)}</g>')


def _humerus(m, uid, groove=False):
    """The arm bone and its ball; groove=True (front view only) adds the bicipital groove on the shaft."""
    hx, hy = m(*HEAD_C)
    r = HEAD_R * S
    g = ""
    if groove:
        (ax, ay), (bx, by), (cx, cy) = (m(*p) for p in GROOVE)
        g = (f'<path d="M{_f(ax)},{_f(ay)} Q{_f(bx)},{_f(by)} {_f(cx)},{_f(cy)}" stroke="{BONE_EDGE}" '
             f'stroke-width=".9" opacity=".45" fill="none" stroke-linecap="round"/>')
    return (f'<mask id="{uid}" maskUnits="userSpaceOnUse"><rect x="{_f(hx - 70)}" y="{OY - 10}" width="140" '
            f'height="{_f(1.11 * S + 12)}" fill="url(#ts-fade)"/></mask>'
            f'<g mask="url(#{uid})">' + _shape(HUMERUS, m, "url(#ts-bone)", BONE_EDGE, 1.2)
            + f'<circle cx="{_f(hx)}" cy="{_f(hy)}" r="{_f(r - 1.5)}" fill="url(#ts-ball)"/>' + g + '</g>')


def _label(x, y, text, tx, ty, anchor="start", size=10.5, weight=700, color=INK, side=None, sub=None):
    """Label in clear space with a thin leader to (tx, ty) ending in a dot on the structure.
    side: where the leader leaves the text ('below', 'above', 'left', 'right').  sub: one italic line or a list."""
    subs = [sub] if isinstance(sub, str) else list(sub or [])
    w = tw(text, size, weight)
    x0 = {"start": x, "middle": x - w / 2, "end": x - w}[anchor]
    cxm = x0 + w / 2
    if side == "below":
        lx, ly = cxm, y + 3.5 + 12 * len(subs)
    elif side == "above":
        lx, ly = cxm, y - size * 0.95
    elif side == "left":
        lx, ly = x0 - 3, y - size * 0.34
    else:
        lx, ly = x0 + w + 3, y - size * 0.34
    out = (f'<path d="M{_f(lx)},{_f(ly)} L{_f(tx)},{_f(ty)}" stroke="{LEAD}" stroke-width=".9" fill="none"/>'
           f'<circle cx="{_f(tx)}" cy="{_f(ty)}" r="2.1" fill="{LEAD}" stroke="#fff" stroke-width=".8"/>'
           + T(x, y, text, size, weight, color, anchor))
    for i, s in enumerate(subs):
        out += T(x, y + 12 * (i + 1), s, 10, 500, INK2, anchor, italic=True)
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
    # the four cuff muscles, their tendons over the ball, the roof and the cushion under it [ANAT]
    out = [_panel_card(P1X, PW, "ROTATOR CUFF FROM THE FRONT", "big outer shoulder muscle lifted away"),
           f'<clipPath id="ts-p1"><rect x="{P1X + 1}" y="1" width="{PW - 2}" height="{PANEL_H - 2}" rx="10"/></clipPath>',
           '<g clip-path="url(#ts-p1)">']
    out.append(_shape(SCAPULA_FRONT, m, "url(#ts-fossa)", BONE_EDGE, 1.2))
    out.append(_muscle("ts-f-supf", SUPRA_FRONT, m, [(0.085, -0.008), (0.088, 0.02)], [(0.640, 0.066), (0.646, 0.108)], 5))
    out.append(_humerus(m, "ts-hm1", groove=True))
    out.append(_hood("ts-t-supf", T_SUPRA_FRONT, m, [(0.600, 0.092), (0.600, 0.132)], [(0.926, 0.196), (0.916, 0.236)], 3))
    out.append(_muscle("ts-f-subsc", SUBSC, m, [(0.05, 0.10), (0.19, 0.91)], [(0.660, 0.236), (0.670, 0.330)], 16))
    out.append(_hood("ts-t-subsc", T_SUBSC, m, [(0.596, 0.222), (0.606, 0.364)], [(0.838, 0.266), (0.838, 0.344)], 7, bow=-0.010))
    out.append(_shape(bursa_pts(), m, "url(#ts-bur)", BURSA_EDGE, 1.0))
    # pale ridge along the bursa's crown, only where the bursa is thick enough to hold it
    bh = [(HEAD_C[0] + (HEAD_R + 0.056) * math.cos(math.radians(a)), HEAD_C[1] + (HEAD_R + 0.056) * math.sin(math.radians(a)), 1)
          for a in (262, 278, 294, 308)]
    out.append(_ridge(bh, m, "#FFD3CC", 0.8, 1.4))
    out.append(_shape(CORACOID, m, "url(#ts-bone)", BONE_EDGE, 1.1))
    out.append(_shape(ACROMION, m, "url(#ts-spine)", BONE_EDGE, 1.2))
    out.append(_shape(CLAVICLE, m, "url(#ts-spine)", BONE_EDGE, 1.2))
    out.append(_ridge([(0.640, -0.014, 1), (0.520, -0.028, 1), (0.380, -0.044, 1), (0.200, -0.040, 1), (0.000, -0.028, 1),
                       (-0.200, -0.042, 1), (-0.420, -0.058, 1)], m))
    aj = [m(0.668, -0.020), m(0.664, 0.036)]          # the joint between acromion and collarbone
    out.append(f'<path d="M{_f(aj[0][0])},{_f(aj[0][1])} L{_f(aj[1][0])},{_f(aj[1][1])}" stroke="{BONE_EDGE}" stroke-width="1.3"/>')
    out.append("</g>")
    # labels, all in clear space
    ax, ay = m(0.79, 0.020)
    out.append(_label(P1X + 10, 52, "Acromion: the roof", ax, ay, "start", side="below"))
    cx, cy = m(0.05, -0.005)
    out.append(_label(P1X + PW - 10, 52, "Collarbone", cx, cy, "end", side="below"))
    # the dot sits at mid-thickness of the bursa, clear of the acromion; the label stands in the margin left of the
    # arm bone, and its leader reaches the bursa without crossing bone [ANAT]
    bx, by = m(0.926, 0.167)
    # "as shown" ties the caption to the red drawing and to the KEY's "Sore bursa", so the two never disagree
    out.append(_label(P1X + 5, 160, "Bursa", bx, by, "start", side="above",       # [ANAT][LEWIS16]
                      sub=["a cushion", "between the", "roof and cuff;", "it can get sore", "and swollen,", "as shown"]))
    sx, sy = m(0.22, 0.78)
    out.append(_label(P1X + PW - 10, 282, "Subscapularis", sx, sy, "end", side="above"))
    hx, hy = m(0.80, 0.86)
    out.append(_label(P1X + 9, 282, "Arm bone", hx, hy, "start", side="above"))
    return "".join(out)


# ============================================================== panel 2: from the back
LENS = (0.85, 0.172)           # on the supraspinatus band of the cuff (above the first seam), just lateral to the acromion


def panel_back():
    m = _back
    out = [_panel_card(P2X, PW, "ROTATOR CUFF FROM THE BACK", "big outer shoulder muscle lifted away"),
           f'<clipPath id="ts-p2"><rect x="{P2X + 1}" y="1" width="{PW - 2}" height="{PANEL_H - 2}" rx="10"/></clipPath>',
           '<g clip-path="url(#ts-p2)">']
    out.append(_shape(SCAPULA, m, "url(#ts-bone)", BONE_EDGE, 1.2))
    out.append(_humerus(m, "ts-hm2"))
    out.append(_muscle("ts-f-infra", INFRA, m, [(0.05, 0.31), (0.11, 0.80)], [(0.664, 0.222), (0.680, 0.300)], 15))
    out.append(_strap("ts-f-tmin", TMINOR, TM_IN, TM_OUTER, m, 4))
    out.append(_muscle("ts-f-supra", SUPRA, m, [(0.040, 0.040), (0.050, 0.232)], [(0.598, 0.084), (0.598, 0.116)], 7))
    # the supraspinatus band comes out from under the acromion, so it is solid where it shows (short fade at its edge);
    # the infraspinatus and teres minor bands keep the long fade, so their muscles flow into them
    out.append(_hood("ts-t-cuff", CUFF_BACK, m, [(0.600, 0.090), (0.642, 0.348)], [(0.930, 0.200), (0.928, 0.346)], 11,
                     seams=SEAMS_BACK, bow=-0.016, top=(SEAMS_BACK[0], 0.600, 0.628)))
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
    tx_, ty_ = m(*TM_MID)        # on teres minor's mid-line, half-way down the border; the leader climbs clear space
    out.append(_label(P2X + 148, 240, "Teres minor", tx_, ty_, "middle", side="above"))   # clear of the arm bone
    bx, by = m(0.205, 0.955)
    out.append(_label(P2X + 140, 282, "Shoulder blade", bx, by, "middle", side="above"))
    # the lens on the cuff tendon that opens into panel 3
    lx, ly = m(*LENS)
    out.append(f'<circle cx="{_f(lx)}" cy="{_f(ly)}" r="9.5" fill="#FFFFFF" fill-opacity=".3" stroke="#123F60" stroke-width="2.2"/>')
    return "".join(out)


# ============================================================== panel 3: inside a tendon
def _crimp_band(x0, x1, yc, h, amp=1.2, period=9.5, hi=True):
    """Healthy fibre bundle: a ribbon whose centre line carries the fine, regular crimp of healthy tendon
    [KHAN99][RUI11].  Every band starts at the same x, so the crimp lines up from band to band."""
    n = max(8, int(x1 - x0))
    top, bot, mid = [], [], []
    for i in range(n + 1):
        x = x0 + (x1 - x0) * i / n
        c = yc + amp * math.sin((x - x0) / period * 2 * math.pi)
        top.append((x, c - h / 2))
        bot.append((x, c + h / 2))
        mid.append((x, c - h * 0.13))
    out = (f'<path d="{_ribbon(top, bot)}" fill="url(#ts-ten)" stroke="{TEN_EDGE}" stroke-width=".7" '
           f'stroke-linejoin="round"/>')
    if hi:
        out += f'<path d="{_poly(mid[3:-3])}" stroke="#FFFFFF" stroke-width="1.1" opacity=".9" fill="none"/>'
    return out


def _fray_end(x, y, dirn, h=6.0, n=4, length=12.0, sw=0.95, seed=1, depth=4.0):
    """A torn fibre end: its blunt tip at x, centred on y, pointing dirn (+1 right, -1 left).  Like the end of a
    frayed rope, n loose gold strands peel off across the end's width at slightly different depths, splay a little
    (the outer ones most) and stop at different lengths with a slight curl.  The strands of the two ends of a break
    never meet: a closed loop would read as a bead bridging the gap."""
    rnd = random.Random(seed)
    parts = []
    for i in range(n):
        f = (i - (n - 1) / 2) / ((n - 1) / 2 or 1)          # -1 .. 1 across the end
        x0 = x - dirn * rnd.uniform(0.5, depth)
        y0 = y + f * h * 0.32
        ln = length * rnd.uniform(0.6, 1.0)
        ang = math.radians(f * 20 + rnd.uniform(-8, 8))
        ex, ey = x0 + dirn * ln * math.cos(ang), y0 + ln * math.sin(ang)
        curl = rnd.uniform(0.8, 1.8) * (1 if f >= 0 else -1)
        parts.append(f"M{_f(x0)},{_f(y0)} C{_f(x0 + dirn * ln * .4)},{_f(y0 + (ey - y0) * .2 - curl * .5)} "
                     f"{_f(x0 + dirn * ln * .75)},{_f(y0 + (ey - y0) * .8 + curl)} {_f(ex)},{_f(ey)}")
    return f'<path d="{" ".join(parts)}" fill="none" stroke="{FRAY}" stroke-width="{sw}" stroke-linecap="round"/>'


def _wavy(x0, x1, y, amp, period, phase, h, taper=(False, False), y_end=None, edge=TEN_EDGE, ew=0.7, tip=(2.4, 9)):
    """An uneven, swollen fibre: a ribbon whose centre line is a sine, sampled once per unit so it stays smooth.
    taper=(left, right) narrows that end to tip[0] wide over its last tip[1] units (a fibre coming apart); y_end
    pins the centre line there to height y_end.  edge / ew: outline colour and width (darker for slipped fibres)."""
    top, bot = [], []
    n = max(8, int(x1 - x0))
    tw_, tl = tip
    for i in range(n + 1):
        x = x0 + (x1 - x0) * i / n
        c = y + amp * math.sin((x - x0) / period * 2 * math.pi + phase)
        hh = h
        for on, dist in ((taper[0], x - x0), (taper[1], x1 - x)):
            if on and dist < tl:
                hh = min(hh, tw_ + (h - tw_) * dist / tl)
                if y_end is not None:
                    c = y_end + (c - y_end) * dist / tl
        top.append((x, c - hh / 2))
        bot.append((x, c + hh / 2))
    return (f'<path d="{_ribbon(top, bot)}" fill="url(#ts-ten)" stroke="{edge}" stroke-width="{ew}" '
            f'stroke-linejoin="round"/>')


SLIP_EDGE = "#8E7B57"      # darker outline of the two fibres that slipped out of line, so they read as crossing


def _vessel(pts, sw=1.6):
    """A new blood vessel: a smooth curve through pts (Catmull-Rom) with round ends; branches get thinner strokes."""
    d = _path([(x, y, 1.0) for x, y in pts], lambda x, y: (x, y), closed=False)
    return (f'<path d="{d}" fill="none" stroke="{VESSEL}" stroke-width="{sw}" stroke-linecap="round" '
            f'stroke-linejoin="round"/>')


def zoom_circle(cx, cy, r, healthy, uid):
    out = [f'<clipPath id="{uid}"><circle cx="{cx}" cy="{cy}" r="{r}"/></clipPath>',
           f'<g clip-path="url(#{uid})"><rect x="{cx - r}" y="{cy - r}" width="{2 * r}" height="{2 * r}" fill="{FIELD}"/>']
    if healthy:
        # tight, parallel bundles with an even crimp [KHAN99][RUI11]
        y = cy - r - 2
        while y < cy + r:
            out.append(_crimp_band(cx - r - 8, cx + r + 8, y + 4.3, 8.6))
            y += 8.6 + 1.6
    else:
        # overloaded: uneven fibres pulled apart (more ground substance between them), two slipped out of line and
        # crossing the others, two broken with frayed ends, and new small blood vessels [KHAN99][MILLAR21]
        rnd = random.Random(5)
        rows, y = [], cy - r - 3
        while y < cy + r + 3:
            h = rnd.uniform(5.4, 8.4)
            rows.append((y + h / 2, h, rnd.uniform(1.4, 3.4), rnd.uniform(15, 30), rnd.uniform(0, 6.28)))
            y += h + rnd.uniform(2.8, 5.2)
        inner = [i for i, row in enumerate(rows) if abs(row[0] - cy) < r - 17]      # breaks stay clear of the rim
        breaks = {inner[len(inner) // 4]: -0.28, inner[(3 * len(inner)) // 4]: 0.24}
        frays = []
        for i, (yc, h, amp, per, ph) in enumerate(rows):
            x0, x1 = cx - r - 6, cx + r + 6
            if i in breaks:
                gx = cx + breaks[i] * r
                # blunt torn ends (a rope cut through, not a needle point); the gold strands peel off them below
                out.append(_wavy(x0, gx - 13, yc, amp, per, ph, h, (False, True), yc, tip=(0.5 * h, 6)))
                out.append(_wavy(gx + 13, x1, yc, amp, per, ph + 1.3, h, (True, False), yc, tip=(0.5 * h, 6)))
                frays.append((gx, yc, h))
            else:
                out.append(_wavy(x0, x1, yc, amp, per, ph, h))
        # the two slipped fibres cross the others at about 18 degrees, with a darker outline, well away from the two
        # breaks, so "tangled" shows and each break still reads on its own
        for ang, oy, h, ph in ((-18, -31, 6.0, 0.6), (18, 33, 5.4, 2.2)):
            out.append(f'<g transform="rotate({ang} {_f(cx)} {_f(cy + oy)})">'
                       + _wavy(cx - r - 22, cx + r + 22, cy + oy, 2.0, 21, ph, h, edge=SLIP_EDGE, ew=0.95) + "</g>")
        # each break: the strands of both torn ends fan out into the gap and stop short of each other
        for j, (gx, gy, gh) in enumerate(frays):
            out.append(_fray_end(gx - 13, gy, +1, gh, seed=11 + 2 * j) + _fray_end(gx + 13, gy, -1, gh, seed=12 + 2 * j))
        # new vessels grow in from the lower side, along the gaps between fibres and clear of the frayed breaks
        vessel = lambda pts, sw: _vessel([(cx + a, cy + b) for a, b in pts], sw)
        out.append(vessel([(-r - 4, 30), (-26, 25), (-8, 31), (10, 27), (28, 31), (r + 4, 24)], 1.9))
        out.append(vessel([(-8, 31), (-4, 38), (2, r + 4)], 1.3))
        out.append(vessel([(-26, 25), (-33, 15), (-36, 3), (-35, -8)], 1.05))
        out.append(vessel([(28, 31), (35, 23), (39, 13)], 0.85))
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


STEP_ICONS = {"load": kit.ICONS["dumbbell"], "feed": kit.ICONS["plate"], "sleep": kit.ICONS["moon"]}
STEPS = [  # how every tendon gets stronger: plain physiology, the same three habits as the back's lifestyle row
    ("load", "Load it", ["exercise is", "the signal"]),      # loading drives collagen building [KJAER04]
    ("feed", "Feed it", ["protein and", "vitamin C foods"]),  # vitamin C is needed to make collagen [ODS-C]
    ("sleep", "Sleep on it", ["7 to 9 hours", "a night"]),   # adults need 7 to 9 hours [NSF15]
]


def panel_zoom():
    x, w = P3X, P3W
    out = [_panel_card(x, w, "INSIDE A TENDON", "the circled spot, magnified many times")]
    c1, c2, cy, r = x + 64, x + w - 64, 88, 46
    out.append(zoom_circle(c1, cy, r, True, "ts-zh"))
    out.append(zoom_circle(c2, cy, r, False, "ts-zo"))
    out.append(T(c1, cy + r + 17, "HEALTHY", 11, 800, GOOD, "middle", ls=0.6))
    out.append(T(c1, cy + r + 30, ["Neat, parallel", "collagen fibers"], 10, 600, INK, "middle"))
    out.append(T(c2, cy + r + 17, "OVERLOADED", 11, 800, BAD, "middle", ls=0.6))
    out.append(T(c2, cy + r + 30, ["Frayed, tangled fibers;", "new blood vessels"], 10, 600, INK, "middle"))
    # HOW TENDONS GET STRONGER: true of every tendon, so it sits in its own box under both circles, not under one
    y0 = 188
    out.append(f'<rect x="{x + 8}" y="{y0}" width="{w - 16}" height="{PANEL_H - y0 - 8}" rx="8" fill="#EEF5FA" '
               f'stroke="#D3DFE8" stroke-width="1"/>')
    out.append(T(x + w / 2, y0 + 15, "HOW TENDONS GET STRONGER", 10.5, 800, "#123F60", "middle", ls=1.0))
    xs = [x + 44, x + w / 2, x + w - 44]
    dy = y0 + 39
    for i, (sx, (ic, head, sub)) in enumerate(zip(xs, STEPS)):
        out.append(_mini(ic, sx, dy))
        out.append(T(sx, dy + 31, head, 10.5, 800, INK, "middle"))
        out.append(T(sx, dy + 43, sub, 10, 500, INK2, "middle", lh=1.15))
        if i < 2:
            ax0, ax1 = sx + 22, xs[i + 1] - 22
            out.append(f'<path d="M{_f(ax0)},{dy} H{_f(ax1 - 6)}" stroke="#2E8FC8" stroke-width="2.2" stroke-linecap="round"/>'
                       f'<path d="M{_f(ax1 - 7)},{dy - 4.5} L{_f(ax1)},{dy} L{_f(ax1 - 7)},{dy + 4.5} Z" fill="#2E8FC8"/>')
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
            + "".join(_crimp_band(-11, 11, yc, 4.2, 0.6, 5.5, hi=False) for yc in (-5, 0, 5)))


def _sw_fray():
    """The KEY swatch drawn like the art: two tapered fibre ends whose gold strands splay into the gap, unjoined."""
    # it stays inside the KEY_SW slot (+-13), so the label keeps its full gap
    return (_wavy(-13, -5, 0, 0.0, 10, 0, 6.0, (False, True), 0, tip=(3.8, 3))
            + _wavy(5, 13, 0, 0.0, 10, 0, 6.0, (True, False), 0, tip=(3.8, 3))
            + _fray_end(-5, 0, +1, 6.0, 4, length=4.4, sw=0.95, seed=3, depth=1.6)
            + _fray_end(5, 0, -1, 6.0, 4, length=4.4, sw=0.95, seed=4, depth=1.6))


def _sw_vessel():
    return _vessel([(-12, 3), (-5, -1), (3, 2.5), (12, -2)], 1.7) + _vessel([(-5, -1), (-3.5, -5), (-1, -8)], 1.1)


KEY_ITEMS = [(_sw_muscle, "Muscle"), (_sw_tendon, "Tendon"), (_sw_bone, "Bone"), (_sw_bursa, "Sore bursa"),
             (_sw_fibers, "Collagen fibers"), (_sw_fray, "Frayed fibers"), (_sw_vessel, "New blood vessels")]
# The lens is explained where it opens: panel 3 is titled "the circled spot, magnified many times".
KEY_FS, KEY_SW, KEY_GAP, KEY_X0, KEY_X1, KEY_MIN = 11, 26, 4, 48, W - 14, 8


def _key_rows():
    """One row when every gap between neighbours stays >= KEY_MIN, so each swatch sits clearly nearer its own label
    (5 units) than the previous one; otherwise two rows."""
    span = [KEY_SW + KEY_GAP + tw(lab, KEY_FS, 600) for _, lab in KEY_ITEMS]
    if sum(span) + KEY_MIN * (len(span) - 1) <= KEY_X1 - KEY_X0:
        return [list(range(len(KEY_ITEMS)))]
    half = (len(KEY_ITEMS) + 1) // 2
    return [list(range(half)), list(range(half, len(KEY_ITEMS)))]


KEY_ROWS = _key_rows()
KEY_H = 32 if len(KEY_ROWS) == 1 else 52
H = KEY_Y + KEY_H + 2


def key_strip(y):
    out = [f'<rect x=".6" y="{y}" width="{W - 1.2}" height="{KEY_H}" rx="8" fill="#FFFFFF" stroke="#CFD6DA" stroke-width="1.2"/>']
    row_h = KEY_H if len(KEY_ROWS) == 1 else 22
    top = y if len(KEY_ROWS) == 1 else y + 4
    out.append(T(14, _f(top + row_h / 2 + 3.8), "KEY", 10.5, 800, INK, ls=1.3))
    for ri, row in enumerate(KEY_ROWS):
        yc = top + ri * row_h + row_h / 2
        span = [KEY_SW + KEY_GAP + tw(KEY_ITEMS[i][1], KEY_FS, 600) for i in row]
        space = max(KEY_MIN, (KEY_X1 - KEY_X0 - sum(span)) / max(1, len(row) - 1))
        x = KEY_X0
        for i, s in zip(row, span):
            sw, lab = KEY_ITEMS[i]
            out.append(f'<g transform="translate({_f(x + KEY_SW / 2)},{_f(yc)})">{sw()}</g>')
            out.append(T(_f(x + KEY_SW + KEY_GAP), _f(yc + 3.9), lab, KEY_FS, 600, INK))
            x += s + space
    return "".join(out)


def art_cuff(t=None):
    body = [plate_defs(), panel_front(), panel_back(), panel_zoom(), lens_cone(), key_strip(KEY_Y)]
    return svg(W, H, "".join(body),
               "The rotator cuff seen from the front and from the back: four muscles whose tendons wrap the ball "
               "of the arm bone, the acromion roof and the bursa beneath it; a magnified view of healthy, "
               "parallel collagen fibers beside frayed, overloaded fibers with new blood vessels; and how tendons "
               "get stronger: load, food and sleep.")


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
    # a bent arm from the side: the upper arm comes in from the left, the elbow is the lower right corner, the
    # forearm rises to a narrow wrist and a closed fist (a grip); the spot sits on the outer elbow
    "elbow": ('<path d="M3 35C10 31 22 30 29 34C31 35 32.5 36.5 33.5 38C35 33 36 28 37 24L36 21C33 20 33 16 33.5 13'
              'C34 8 38 7 42 7C47 7 50 9 50.5 13C51 17 49.5 20.5 47.5 22C48.5 31 50 40 50.5 46C51 52 48 55.5 43 56'
              'L3 54z" fill="#E3EEF6"/>'
              '<path d="M33.6 12.6h5.2M33.4 16.8h5.4"/>' + _spot(46, 49)),
    # lower leg and foot from the side; the spot sits on the Achilles tendon at the back of the ankle, above the heel
    "ankle": ('<path d="M20 2c-5.5 10-6 20-1.5 30 2.5 5.5 3.5 9 2 14-2 5.5-1 12 5.5 12H55c4.5 0 6-3 4-5.5-2-2.5-9-4-14-7'
              '-4-2.5-5.5-5.5-6-10.5C38 25 37 14 37 2" fill="#E3EEF6"/>' + _spot(21.5, 40.5)),
}

# Where tendon pain shows up.  Shoulder: pain on the outer upper arm with lifting, night pain lying on it,
# pain reaching behind [LEWIS16][WHITTLE15].  Tennis elbow: pain at the outer bony bump with gripping
# [BISSET15]; tied to forceful, repetitive arm work, not just tennis [SHIRI06].  Achilles: pain at the back of the
# ankle 2 to 6 cm (about 1 to 2 inches) above the heel bone, morning stiffness, pain with running and jumping [ACH18].
SITES = [
    ("shoulder", "Shoulder", "rotator cuff",
     ["Ache on the outer upper arm", "Worse when you lift your arm", "Hurts to lie on it at night"]),
    ("elbow", "Elbow", "tennis elbow",
     ["Pain on the outer elbow bump", "Worse when you grip or twist", "Common with gripping work"]),
    ("ankle", "Ankle", "Achilles tendon",
     ["Pain just above the heel bone", "Stiff in the morning", "Sore with running or jumping"]),
]

RISK_ICONS = {
    "overhead": ('<circle cx="32" cy="15" r="5"/><path d="M32 21v18M32 39l-7 19M32 39l7 19M32 26 21 12M32 26l11-14"/>'
                 '<path d="M14 9h36"/>'),
    # a training line that creeps up, then jumps, ending in a clean arrowhead
    "spike": '<path d="M8 8v48h48"/><path d="M14 46l9-2 9-2 8-28"/><path d="M35 19l5-5 1.7 6.8"/>',
    # a lit cigarette with smoke rising (no slash: a slash would read as "no smoking")
    "ts_cig": ('<rect x="6" y="37" width="40" height="9" rx="2"/><path d="M37 37v9"/>'
               '<path d="M51 33c-3.2-2.8-3.2-5.6 0-8.4s3.2-5.6 0-8.4"/><path d="M58 31c-2.4-2.1-2.4-4.2 0-6.3s2.4-4.2 0-6.3"/>'),
}
# What raises your risk: age over 50, diabetes, work with the arm above shoulder height [LEONG19];
# a sudden rise in load [COOK09]; high cholesterol [GIRI22]; smoking [BISHOP15][SHIRI06]; family history
# [HARVIE04]; fluoroquinolone antibiotics and steroids [FDA16][YU19][XERGIA22].
RISKS = [("age", "Age over 50"), ("overhead", "Overhead work or sports"), ("spike", "A sudden jump in training"),
         ("bloodsugar", "Diabetes"), ("tube", "High cholesterol"), ("ts_cig", "Smoking"), ("dna", "Family history"),
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
    # above 5 too much, which means lowering the load right then, not only next session; morning pain and stiffness
    # should not build from week to week.
    zone = lambda n: "g" if n <= 2 else ("a" if n <= 5 else "r")
    cells = "".join(f'<span class="tsp-c {zone(n)}">{n}</span>' for n in range(11))
    return ('<div class="tsp-pain"><div><div class="tsp-bh">Your pain guide during exercise '
            '<span>0 = no pain, 10 = the worst pain</span></div>'
            f'<div class="tsp-scale">{cells}</div>'
            '<div class="tsp-zones"><div class="g"><b>0 to 2: safe</b>Keep going.</div>'
            '<div class="a"><b>3 to 5: OK</b>if it settles by the next morning.</div>'
            '<div class="r"><b>6 or more: too much</b>Stop or go lighter now, and do less next time.</div></div></div>'
            # 12-week loading programs [ALF98][BEYER15] (cuff trials run 4 to 16 weeks, Dube 2024 JOSPT PMID 38832666);
            # gains held at a year [BEYER15]
            '<div class="tsp-weeks"><b>12</b><span><strong>weeks</strong> is a typical length for a tendon exercise plan. '
            'Tendons rebuild slowly, and the gains last.</span></div></div>')


def flags_block():
    # Red flags first [CPG24].  Achilles rupture: a sudden "pop" with pain at the back of the heel [BIGGS21]; weak
    # push-off on the hurt side, so you cannot rise up on the toes of THAT foot (a single-leg heel raise) [CHIODO10].
    # Many people with a rupture can still rise on both feet, so the line says "on that foot".  Heart attack warning
    # signs include arm pain with chest discomfort, shortness of breath or a cold sweat: call 911 [AHA].
    return ('<div class="tsp-flag">' + icon("warning", "0.3in", sw=3.4) +
            '<p><b>Get checked right away for:</b> a pop or sudden weakness after a fall or heavy lift. An arm you cannot '
            'lift. A hot, red, swollen joint, or a fever. Numbness running down the arm. A pop at the back of the ankle, '
            'or not being able to stand on tiptoe on that foot. <b>Shoulder or arm pain with chest pressure, shortness '
            'of breath or a cold sweat can be a heart attack: call 911.</b></p></div>')


def front(t, ed):
    return (f'<div class="tsp"><div class="art tsp-art">{art_cuff(t)}</div>'
            f'{sites_block()}{risk_block()}{pain_block()}{flags_block()}</div>')


_BK = '.sheet.back:has(.tsp-bk)'     # this sheet's back page: the marker span in its lifestyle title (photo file
                                      # names are pooled across sheets now, so they cannot identify the page)
CSS = r"""
.tsp .tsp-art svg{display:block;width:100%;height:auto}
.tsp .tsp-h{display:flex;align-items:center;gap:0.1in;margin:0.1in 0 0.05in;font:900 10.5pt/1.2 Merriweather,Georgia,serif;
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
.tsp .tsp-site i{font:italic 600 7.6pt/1.15 Inter,sans-serif;color:#4A555C;margin-left:3px;white-space:nowrap}
.tsp .tsp-site ul{margin:0;padding:0;list-style:none}
.tsp .tsp-site li{position:relative;padding-left:9px;font-size:7.9pt;line-height:1.28;color:#2B3236;margin:0 0 1px}
.tsp .tsp-site li::before{content:"";position:absolute;left:0;top:4.5px;width:4px;height:4px;border-radius:50%;background:var(--c2)}
.tsp .tsp-risk{display:grid;grid-template-columns:repeat(8,1fr);gap:0 0.04in}
.tsp .tsp-rf{display:flex;flex-direction:column;align-items:center;text-align:center}
.tsp .tsp-disc{width:0.46in;height:0.46in;border-radius:50%;background:var(--soft);color:var(--c1);display:flex;align-items:center;
  justify-content:center;box-shadow:inset 0 0 0 1.5px rgba(31,94,140,.10)}
.tsp .tsp-rl{display:block;font-size:7.7pt;font-weight:600;line-height:1.2;color:#2F373C;margin-top:0.03in}
.tsp .tsp-pain{display:grid;grid-template-columns:1fr 1.95in;gap:0.14in;align-items:center;margin-top:0.11in;border:1px solid #D9E5EE;
  border-radius:9px;padding:0.06in 0.1in 0.07in;background:#fff}
.tsp .tsp-bh{font:900 9.6pt/1.2 Merriweather,Georgia,serif;color:var(--c1);letter-spacing:.03em;text-transform:uppercase;margin:0 0 0.05in}
.tsp .tsp-bh span{font:italic 600 7.4pt Inter,sans-serif;letter-spacing:0;text-transform:none;color:#4A555C;margin-left:6px}
.tsp .tsp-scale{display:grid;grid-template-columns:repeat(11,1fr);gap:2px}
.tsp .tsp-c{display:flex;align-items:center;justify-content:center;height:0.2in;font:800 8pt Inter,sans-serif;color:#fff;border-radius:3px}
/* amber #9A6508: white 8 pt bold numbers on it measure about 4.9:1 (the old #B67A0B was about 3.6:1) */
.tsp .tsp-c.g{background:#2F8A5E}.tsp .tsp-c.a{background:#9A6508}.tsp .tsp-c.r{background:#C2392E}
.tsp .tsp-zones{display:grid;grid-template-columns:3fr 3fr 5fr;gap:2px;margin-top:3px}
.tsp .tsp-zones div{font-size:7.5pt;line-height:1.25;color:#2B3236;padding:2px 4px 0;border-top:3px solid}
.tsp .tsp-zones b{display:block;font-size:7.7pt}
.tsp .tsp-zones .g{border-color:#2F8A5E}.tsp .tsp-zones .g b{color:#1F6B47}
.tsp .tsp-zones .a{border-color:#9A6508}.tsp .tsp-zones .a b{color:#7E5300}
.tsp .tsp-zones .r{border-color:#C2392E}.tsp .tsp-zones .r b{color:#9A2620}
.tsp .tsp-weeks{display:flex;align-items:center;gap:0.08in;background:var(--soft);border-radius:8px;padding:0.06in 0.1in;align-self:stretch}
.tsp .tsp-weeks b{font:900 26pt/1 Merriweather,Georgia,serif;color:var(--c1)}
.tsp .tsp-weeks span{font-size:7.9pt;line-height:1.3;color:#2B3236}
.tsp .tsp-weeks strong{color:var(--deep);font-size:8.6pt}
.tsp .tsp-flag{display:flex;gap:0.08in;align-items:center;margin-top:0.1in;border:1.5px solid #C0392B;background:#FDF1EF;
  border-radius:8px;padding:0.05in 0.1in}
.tsp .tsp-flag .ic{flex:none;color:#B23A30}
.tsp .tsp-flag p{margin:0;font-size:7.9pt;line-height:1.33;color:#2B3236}
.tsp .tsp-flag b{color:#A5281E}
/* the rhythm keeps a count with its unit ("1 softgel"): an inline-block moves to the next line whole */
BK .slot li em{display:inline-block}
/* The five columns share four rows (a subgrid: header, photo and name, bullets and serving, dose), so the bullets,
   the IN EACH SERVING heads and the dose bars line up across the row although "Omega Pure / EPA-DHA 1000" needs two
   lines and the Collagen Renew dose needs three.  A one-line name sits on the row's bottom line, just above its
   size; the dose text is centred in its bar. */
BK .cols{grid-template-rows:repeat(4,auto);row-gap:0}
BK .col{display:grid;grid-row:1/span 4;grid-template-rows:subgrid;row-gap:0}
BK .col .pick a.plink{flex:1}
BK .col .pick .nm{margin-top:auto;padding-top:0.04in}
BK .col .dose{display:flex;flex-direction:column;justify-content:center}
/* two write-in lines instead of three pay for the aligned name row and the safety lines */
BK .notes .ln:last-child{display:none}
/* The eleven-line check panel is paid for with the spacing its Pain and Movement siblings already use (joint_pain,
   gut_overgrowth, intestinal_permeability, insulin_resistance, lyme, neuropathy, stress_cortisol, thyroid): a 0.14 in
   band foot, 0.07 to 0.11 in heading gaps, 0.08 in panel gaps, 0.22 in write-in lines and the notes padding of
   neuropathy; the check panel's leading is 1.25 (neuropathy's is 1.26).  Measured in print media, page 2 keeps
   about 5 px above its footer in both editions. */
BK .band{padding-bottom:0.14in}
BK .band h2{margin-bottom:0.07in}
BK .ns-title{margin-top:0.11in}
BK .cols{margin-top:0.07in}
BK .duo{margin-top:0.08in}
BK .notes{margin-top:0.08in;padding-top:0.05in;padding-bottom:0.055in}
BK .notes .ln{height:0.22in}
BK .rx li{line-height:1.25}
""".replace("BK", _BK)

# ============================================================== back-page icons (registered by name for build.life_block)
kit.ICONS["ts_steps"] = '<path d="M6 56h14V44h12V32h12V20h14"/><path d="M10 34 30 14"/><path d="M21 14h9v9"/>'
# a high shelf on two brackets, a box held lower down, and a down arrow: keep heavy lifting below shoulder height
kit.ICONS["ts_lower"] = ('<path d="M7 12h50M13 12v6M51 12v6"/><rect x="15" y="30" width="24" height="20" rx="2"/>'
                         '<path d="M15 37h24M27 30v7"/><path d="M50 24v25M44 43l6 6 6-6"/>')

SHEET = {
    "slug": SLUG, "code": "ND-MS-603", "order": 14, "theme": "msk", "series": "Pain and Movement Series",
    "title": "Shoulder and Tendon Pain", "sub": "Rotator cuff, tennis elbow and Achilles",
    # Collagen, mostly type I, is 65-80% of tendon [KANNUS00].  Most tendon pain is overuse, a load the tendon
    # was not ready for [COOK09][MILLAR21], with disorganised (fraying) collagen fibres [KHAN99][MILLAR21].  Shoulder
    # pain: third most common musculoskeletal reason to see primary care [WHITTLE15]; rotator cuff the most
    # common cause [ZHANG25].  The rotator cuff: 4 muscles whose tendons cover the ball and hold it in the socket; the
    # supraspinatus helps lift the arm, the other three turn it in and out [ANAT] (glosses the plate's Latin labels).
    "intro": ("Tendons are tough cords of <b>collagen</b> that join muscle to bone. Most tendon pain builds slowly, when a "
              "tendon does more than it is ready for and its rope-like fibers fray. Shoulder pain is the "
              "<b>third most common</b> muscle and joint reason to see a family doctor, usually from the "
              "<b>rotator cuff</b>: 4 muscles whose tendons hug the ball of the arm bone and keep it in its socket. "
              "The <b>supraspinatus</b> helps lift your arm. The other three turn it in and out."),
    "front": front,
    "css": CSS,
    "back": {
        # the empty span marks this sheet's back page for the scoped CSS (_BK)
        "life_title": 'Lifestyle Recommendations<span class="tsp-bk"></span>', "life_sub": "Habits that help tendons rebuild",
        "style": "circle",
        "life": [
            # Loading raises collagen building; inactivity lowers it; overuse needs adjusted loading, not rest [KJAER04]
            ("dumbbell", "Load, don&rsquo;t rest", "Exercise most days. Full rest weakens tendons."),   # curly apostrophe
            # A sudden rise in load drives tendinopathy [COOK09]
            ("ts_steps", "Build up slowly", "Add weight, miles or reps in small steps."),
            # Work with the arm above shoulder height raises cuff risk [LEONG19]
            ("ts_lower", "Lower your reach", "Keep heavy lifting below shoulder height."),
            # Vitamin C is needed to make collagen [ODS-C]
            # (a no-break space keeps "vitamin C" whole; the wording keeps the cell to two lines)
            ("plate", "Feed the rebuild", "Eat protein and foods rich in vitamin&nbsp;C."),
            # Adults need 7 to 9 hours [NSF15]; the day's biggest growth hormone (repair hormone) pulse comes in deep
            # sleep [VC96]
            ("moon", "Sleep 7 to 9 hours", "Your repair hormone peaks in deep sleep."),
            # Smoking is tied to cuff tears, shoulder pain and poorer function [BISHOP15]
            ("smoke", "Stop smoking", "Smoking is tied to more rotator cuff tears."),
        ],
        "cols": [
            {"p": "ts_collagen_renew", "need": "Tendon building blocks", "needsub": "collagen peptides", "start": True,
             # bullet 2 is a plain fact about the formula, not a claim (labels.json R190: Gelatin Hydrolysate
             # (TENDOFORTE), a collagen peptide, in each scoop), so only bullet 1 carries the FDA diamond.  The 5 g sits
             # in the serving box just below; with it, the bullet would wrap to 3 lines and drop this column's
             # IN EACH SERVING head out of line with the other four.
             "bullets": ["Supports tendons, ligaments and joints",
                         "Includes TENDOFORTE collagen peptides"],
             "dose": "1 scoop in 8 oz water",                                      # label: 1 scoop in 8 ounces of water
             # the timing is the sheet's, not the label's [SHAW17]: about 1 hour before exercise; on a rest day the
             # time does not matter.  The rhythm says the same, so a later workout never clashes with the Morning slot.
             "dosesub": "about 1 hour before exercise,<br>any time on rest days",
             "sched": [("am", 1, "scoop, or before exercise")]},
            {"p": "ts_vitamin_c_1000", "need": "Build collagen", "needsub": "vitamin C",
             "bullets": ["Your body needs it to build collagen",                            # [ODS-C]
                         "Collagen Renew has none, so pair them"],                         # labels.json R190: no vitamin C
             # the rhythm says "with the scoop" too, so on a day the scoop moves to before exercise, the pair moves
             # together (the unit still starts "capsule", so the rhythm still counts it as a pill)
             "dose": "1 capsule daily", "dosesub": "with your collagen", "sched": [("am", 1, "capsule, with the scoop")]},
            {"p": "ts_inflam_eze_plus", "need": "Comfort after activity", "needsub": "ginger, curcumin, boswellia",
             "bullets": ["Supports joint and muscle comfort", "Supports a healthy inflammatory response"],
             "dose": "3 capsules daily", "dosesub": "with food", "sched": [("pm", 3, "capsules")]},
            {"p": "ts_omega_1000", "need": "Inflammatory balance", "needsub": "omega-3s EPA and DHA",
             "bullets": ["Supports a balanced inflammatory response", "Supports muscle, joint and heart health"],
             # label: "Take one softgel up to three times daily with food", so one at a time, with two meals
             "dose": "1 softgel twice daily", "dosesub": "with meals",
             "sched": [("am", 1, "softgel"), ("pm", 1, "softgel")]},
            {"p": "ts_d3_5000_k2", "need": "Muscle and bone", "needsub": "vitamin D3 with K2",
             # Why vitamin D on a tendon sheet: a tendon joins muscle to bone, and both need vitamin D (NIH ODS
             # Vitamin D fact sheet: bones need it to absorb calcium; muscles need it to move).  Structure/function only.
             # The wording fits two lines, so this column's IN EACH SERVING head lines up with the other four.
             "bullets": ["Supports muscle and bone health",
                         "High dose: check your vitamin D level first"],   # 5,000 IU is above the 4,000 IU adult UL (NIH ODS)
             # label: "Take one softgel daily"; taken with the evening meal (fat helps absorption), which also keeps the
             # Morning and Evening rhythm slots the same height
             "dose": "1 softgel daily", "dosesub": "with your evening meal", "sched": [("pm", 1, "softgel")]},
        ],
        # Edition-aware via {who}: "your provider" (practitioner) / "your pharmacist" (pharmacy).
        # PARITY (checked line by line against both sibling panels, 2026-11-03): every caution the sibling Pain and
        # Movement sheets print for the products this sheet shares with them (Inflam-Eze Plus, Collagen Renew, fish
        # oil) is here, so a pharmacy holding both sees one story.
        #   joint_pain.py: blood thinner or surgery (check 1); willow bark and aspirin allergy, aspirin, ibuprofen or
        #   naproxen (checks 3, 1); liver or gallbladder trouble, stomach ulcer, and yellow skin or eyes or dark urine
        #   means stop (checks 5, 4); red-meat (alpha-gal) allergy and Collagen Renew (check 3); pregnant or nursing (5).
        #   injury_healing.py: blood thinners, aspirin, NSAIDs (1); aspirin allergy (3); surgery (1); diabetes medicine
        #   (4); under 18, pregnant, nursing, fish allergy, kidney disease, stomach ulcers, gallstones (3, 5); and its
        #   drowsiness line (muscle relaxers, opioids or sleep aids, with Muscle Eze and the hops in Inflam-Eze Plus),
        #   carried here as "On sleep aids or other medicines? Ask first" (5): Muscle Eze is not on this sheet, and
        #   the line has no room to name the hops.
        # Plus this sheet's own two: the vitamin K in D3 5000 with K2 and warfarin, and the fluoroquinolone tendon
        # warning.  The whole panel fits 11 lines: the duo split, the panel's 1.25 leading and the spacing in CSS above
        # pay for it.  Product names carry no-break spaces and hyphens (U+2011, printed as a plain hyphen) so none
        # splits across lines.
        "rx": [
            # 1 Bleeding: omega-3s and warfarin (NIH ODS Omega-3 fact sheet); willow bark contains salicin and may increase
            # the effect of coumarin anticoagulants [EMA-SALIX: EMA/HMPC/80630/2016]; ginger and turmeric/curcumin may
            # slow clotting, and MedlinePlus (Ginger; Turmeric) names aspirin, ibuprofen and naproxen among the
            # medicines that slow clotting.  Vitamin K counters warfarin (NIH ODS Vitamin K fact sheet).  Surgery: the
            # American Society of Anesthesiologists asks patients to stop herbal supplements 2 weeks before surgery.
            # The EMA, MedlinePlus and ASA points are as cited in conditions/joint_pain.py and
            # conditions/injury_healing.py (ema.europa.eu is blocked here; not re-opened for this sheet).
            "<b>Blood thinner, aspirin, ibuprofen, naproxen, or surgery soon?</b> Fish oil and the Inflam‑Eze&nbsp;Plus "
            "herbs can add to bleeding; many surgeons stop them 2 weeks before. D3&nbsp;5000 with&nbsp;K2&rsquo;s "
            "vitamin K affects warfarin. Ask {who} first.",
            # 2 [FDA16][YU19]: stop the antibiotic and call at the first tendon pain
            "<b>Fluoroquinolone antibiotics</b> (ciprofloxacin, levofloxacin) can injure tendons, more so after 60 or on "
            "steroids. Stop and call your doctor if a tendon hurts.",
            # 3 Aspirin allergy: white willow bark carries salicin, a salicylate (labels.json R856: 200 mg, 25% salicin),
            # so not with a salicylate allergy [EMA-SALIX]; "aspirin's cousin" says salicylate in plain words.  The
            # "aspirin or other NSAIDs" half of that caution is in check 1.  Red meat: Collagen Renew's only other
            # ingredient is "Bovine Collagen Peptides" (labels.json R190), and products made from mammals can trigger
            # alpha-gal syndrome, the red-meat allergy spread by lone star tick bites (CDC "Products that may contain
            # alpha-gal", as cited in conditions/joint_pain.py [CDC-AGS]).  Fish: Omega Pure EPA-DHA 1000 is "omega-3
            # fish oil (anchovy, sardine, mackerel)", "Contains: Fish" (NutriDyn sell sheet ND416, as recorded in
            # products.d/neuropathy.json and in this sheet's ts_omega_1000 "src").
            # (two questions, one per line in both editions: the break falls between the sentences)
            "<b>Allergic to aspirin?</b> Skip Inflam‑Eze&nbsp;Plus: its white willow is aspirin&rsquo;s cousin. "
            "<b>Red&nbsp;meat (alpha-gal) or fish?</b> Skip Collagen&nbsp;Renew (beef) or Omega&nbsp;Pure (fish oil).",
            # 4 Diabetes: ginger and turmeric might lower blood sugar, and with diabetes medicines it might drop too low
            # (MedlinePlus Ginger and Turmeric, as cited in conditions/injury_healing.py); Inflam-Eze Plus carries both
            # (labels.json R856: ginger 800 mg, CurQfen curcumin-fenugreek 250 mg).  Liver: rare liver injury with
            # turmeric or curcumin, more likely with enhanced-absorption forms (CurQfen is one); watch for yellow skin
            # or eyes and dark urine, and stop [TGA23: TGA safety alert 2023, as cited in conditions/joint_pain.py].
            # The stop line names the product, so "it" can never be read as the diabetes medicine.
            "<b>Diabetes medicine?</b> Ask {who}: Inflam‑Eze&nbsp;Plus may lower blood sugar. <b>Yellow skin or eyes, "
            "or dark urine?</b> Stop Inflam‑Eze&nbsp;Plus and call your doctor.",
            # 5 Under 18: willow bark, a salicylate, is not advised for children (Reye's syndrome; MedlinePlus Willow
            # bark, as cited in conditions/injury_healing.py).  Label caution (labels.json R856 and R190; ND416 for the
            # omega): "If you are pregnant, nursing, or taking medication, consult your healthcare practitioner before
            # use"; this line carries all of it and covers all five products.  Stomach ulcer: devil's claw, not with
            # stomach or duodenal ulcers (German Commission E [COMM-E]).  Gallstones: devil's claw only after advice
            # [COMM-E]; turmeric not with gallstones or blocked bile ducts [EMA-CURCUMA: EMA/HMPC/329755/2017].  Liver
            # disease: turmeric not with liver disease [EMA-CURCUMA]; people with liver problems should avoid
            # enhanced-absorption curcumin [TGA23].  Kidney disease: willow bark may harm weak kidneys (MedlinePlus, as
            # cited in conditions/injury_healing.py).  Sleep aids: hops can add sleepiness with sedatives (MedlinePlus
            # Hops, as cited in conditions/injury_healing.py; labels.json R856: hops extract 150 mg).  (The COMM-E, EMA
            # and TGA points are as cited in joint_pain.py.)
            "<b>Under 18, pregnant or nursing? On sleep aids or other medicines? Stomach ulcer, gallstones, or liver or "
            "kidney disease?</b> Ask {who} first.",
        ],
    },
}


def _slots_used():
    """Daily-rhythm slots the back page fills: each column's own sched, else its product's sched in products.d."""
    import json
    f = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "products.d", f"{SLUG}.json")
    try:
        prods = json.load(open(f))
    except Exception:
        return {"am", "pm", "bed"}
    return {slot for c in SHEET["back"]["cols"] for slot, *_ in (c.get("sched") or prods.get(c["p"], {}).get("sched", [("bed",)]))}


if "bed" not in _slots_used():
    # No bedtime products: two rhythm slots instead of an empty "nothing to take" box, and the freed width goes to
    # the check panel, which carries the most text on the page.  1fr 1.38fr is as far as the rhythm can narrow
    # without a new wrap (its widest unbreakable run, "1 scoop, or before exercise", needs 119 px of a 123 px slot);
    # the checks keep the same 11 lines anywhere from 1.34fr to 1.40fr in both editions.
    SHEET["css"] += (f"{_BK} .rhythm{{grid-template-columns:1fr 1fr}}"
                     f"{_BK} .rhythm .slot:nth-child(3){{display:none}}"
                     f"{_BK} .duo{{grid-template-columns:1fr 1.38fr}}")
