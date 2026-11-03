"""Fatty Liver Disease (MASLD) condition sheet, slug "fatty-liver".

Self-contained: the art below was copied out of art.py / sheets.py and rebuilt on
2026-11-03 for Asher's notes on the first draft.
  1. The stage labels sit inside the viewBox with real top margin, large and crisp.
  2. The least-to-most-severe direction is a labelled gradient arrow across the top and
     the stages are numbered 1 to 4.  The green "often reversible" arcs and the red
     "hardest to reverse" bracket keep the first draft's logic (Asher approved it).
  3. A KEY names everything inside the magnified tissue circles.
  4. The old empty space at the bottom holds an "Ask about liver checks" panel.
  5. The risk-factor icons stay, polished into one row of tinted discs.
Art-director pass (front only): immune cells never stack, scar is drawn edges-then-fills, every arc end
and T-bar stops clear of the white ring, the band holds the arcs and their labels, the livers sit
bottom-aligned 4 units above the band, all three check cards end in two sourced dots, and the pharmacy
edition says the doctor orders the checks.
Front recheck pass (2026-11-03, front_rechecks_BC.json), no redesign beyond the listed items:
  - ALT dots read as upper limits, the FIB-4 dot names the FibroScan, the specialist dot is red.
  - The zoom tag says "Close-up", the same word as the key.  Every key swatch sits on a dark tissue
    chip like the art, the scar swatch is a straight piece of septum, the key names the pink nucleus.
  - The cirrhotic liver is warm tan-brown, its nodules packed without overlap, lit by a soft lower
    shadow and a highlight instead of dark rings.
  - Close-up 4 shows rounded nodules ringed by scar: a gapped Voronoi layout (septa 6 to 11 wide that
    swell, thin and fork where three nodules meet), each nodule with its own tilted cell grid.
  - Close-up 3's immune cells sit in four tight foci of three in the gaps between cells, never on fat
    or a nucleus (checked by asserts).
  - The gut caption and the gut risk label are hedged ("may add to it", "being studied").
  - The sugar icon is a soda cup with a straw; PCOS is a uterus-and-ovaries glyph in the kit's style.
  - The severity row, the band and the key share one 8-unit margin on both sides.
Back (products pass, same day): four columns, the competitor's count, matching its four nutrient
categories (berberine; bergamot + artichoke; aged black garlic; alpha lipoic acid) with NutriDyn's own
protocol products.  Berberine Pro, Milk Thistle Complex and Mito Recharge are on Rick Mayfield's GLC 2026
"Metabolic Fatty Liver (MAFLD, MASLD, MASH)" list [MAYFIELD26]; Lipo-Flow is the NutriDyn science-team
lipotropic (400 mg artichoke + tangerine peel: the citrus-and-artichoke match) Asher sends "to promote healthy
liver function".  Milk Thistle Complex stands in for aged black garlic (both are antioxidant liver-cell
support; NutriDyn has no liver protocol with garlic).  Label facts: products.d/fatty-liver.json (fl_* keys, so
no other sheet's override reaches this page), each with its sell-sheet source.
Shared helpers come only from svgkit / kit.  Every SVG id starts with "fl-" and every
CSS class with "flv-", so nothing collides with other sheets in the all-sheets bundle.

SOURCES (each number on the page carries one of these tags in a comment)
  [AASLD23]   Rinella ME et al. AASLD Practice Guidance on the clinical assessment and
              management of NAFLD. Hepatology 2023;77:1797-1835.
              doi:10.1097/HEP.0000000000000323 (full text read via PubMed Central, PMC10735173)
  [DELPHI23]  Rinella ME et al. A multisociety Delphi consensus statement on new fatty liver
              disease nomenclature, June 2023 (NAFLD -> MASLD, NASH -> MASH).
              doi:10.1016/j.aohep.2023.101133 (published jointly in Hepatology / J Hepatol)
  [NHANES25]  Kim D et al. Current burden of steatotic liver disease and fibrosis among adults
              in the United States, 2017-2023. Clin Mol Hepatol 2025;31:382-393.
              doi:10.3350/cmh.2024.0987 (US adults, age-adjusted MASLD prevalence 31.9%)
  [YOUNOSSI23] Younossi ZM et al. The global epidemiology of NAFLD and NASH. Hepatology
              2023;77:1335-1347. doi:10.1097/HEP.0000000000000004 (global 30%; 38% in 2016-2019)
  [EASL24]    EASL-EASD-EASO Clinical Practice Guidelines on the management of MASLD. J Hepatol
              2024;81:492-542. doi:10.1016/j.jhep.2024.04.031; executive summary read in full,
              Diabetologia 2024;67:2375-2392, doi:10.1007/s00125-024-06196-3 (PMC11519095)
  [HHS18]     Physical Activity Guidelines for Americans, 2nd ed. US HHS, 2018 (muscle-strengthening
              activity on 2 or more days a week).
  [REYNOLDS16] Reynolds AN et al. Advice to walk after meals is more effective for lowering postprandial
              glycaemia in type 2 diabetes. Diabetologia 2016;59:2572-2578. doi:10.1007/s00125-016-4085-2
  [ZHANG08]   Zhang Y et al. Treatment of type 2 diabetes and dyslipidemia with the natural plant alkaloid
              berberine. J Clin Endocrinol Metab 2008;93:2559-2565 (cited on Berberine Pro SS ND1130)
  [GUO12]     Guo Y et al. Repeated administration of berberine inhibits cytochromes P450 in humans.
              Eur J Clin Pharmacol 2012;68:213-217. doi:10.1007/s00228-011-1108-2 (CYP2D6, 2C9, 3A4)
  [ODSK]      NIH Office of Dietary Supplements, Vitamin K fact sheet for health professionals
              (vitamin K works against warfarin; people on warfarin keep vitamin K intake consistent)
  [BANACH15]  Banach M et al. Statin therapy and plasma coenzyme Q10 concentrations: meta-analysis of
              placebo-controlled trials. Pharmacol Res 2015;99:329-336. doi:10.1016/j.phrs.2015.07.008
  [USP20]     Oketch-Rabah HA et al. USP comprehensive review of the hepatotoxicity of green tea extracts.
              Toxicol Rep 2020;7:386-402. doi:10.1016/j.toxrep.2020.02.008 (fasting bolus doses raise EGCG
              exposure; case reports at 140 to about 1000 mg/day EGCG; USP label: take with food, stop
              and call if dark urine or yellow skin or eyes)
  [MAYFIELD26] Rick Mayfield DC (NutriDyn CSO), FINAL_GLC 2026 PROTOCOL RICK.pdf, Dropbox
              /NutriDyn/Public Share Folder/GLC 2026 Notes/3 - Rick Mayfield/ (id:xHepYs_Ou4AAAAAAAA7oHg),
              read 2026-11-03: "Metabolic Fatty Liver (MAFLD, MASLD, MASH)": PPC Silymarin (coming soon),
              Ganoderma Plus, Inflam-Eze Plus, Milk Thistle Complex, Berberine Pro, Detox, Mito Recharge,
              UltraBiotic Prebiotic.  His GLC 2026 outline (Dropbox "GLC 2026 outline marketing.docx",
              id:xHepYs_Ou4AAAAAAAA4B1A, per scratchpad/protocols/metabolic.md) covers the gut barrier and the
              "total toxic load of xenobiotics and inflammatory endotoxins".
  [MAYFIELD24] Mayfield, GLC2024 Rick Mayfield Protocols.pdf (id:xHepYs_Ou4AAAAAAAArn1w, per
              scratchpad/wf/protocol-fatty-liver.json): UltraBiotic Prebiotic's polyphenols "all reduce LPS",
              listed as an Akkermansia booster.  Asher's Direct Mail blast "NutriDyn New Formula: Akkermansia
              Plus" (Gmail 18f5f05aa7b72a44, 2024-05-09) ties Akkermansia to "colon and liver health".
  [LABELS]    NutriDyn sell sheets read 2026-11-03 (Dropbox NutriDyn Marketing Materials): Berberine Pro
              ND1130 Rev. 11/25, Lipo-Flow ND606 Rev. 4/26, Milk Thistle Complex ND764 Rev. 2/25,
              Mito Recharge ND812 Rev. 2/25.  Amounts are in products.d/fatty-liver.json.
"""
import math
import os
import random

from kit import icon
from svgkit import T, svg

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


def tw(text, size, weight=700, ls=0.0):
    """Advance width of `text` in Inter at `size` px.  Used to centre badge+label groups
    and to space the key.  Without Pillow or the font it falls back to a generous guess
    (checked: the layout still fits with the guess)."""
    try:
        w = _face(_WEIGHTS[weight]).getlength(text) * size / 100
    except Exception:
        w = len(text) * size * (0.68 if text.isupper() else 0.6)
    return w + ls * len(text)


# ============================================================== palette
INK, INK2 = "#23292D", "#57616A"
SEV = ("#3E8A27", "#B87A0C", "#D2611F", "#BE2F2F")        # stage badges, green -> red (white text >= 3.6:1)
SEV_BAR = ("#4E9A2E", "#E8A824", "#E26A2A", "#C8343B")    # the brighter severity arrow
GREEN, GREEN_TX = "#5A9E2C", "#3E7F22"                    # "often reversible" arcs + label
RED, RED_TX = "#D23F37", "#B32A2A"                        # "hardest to reverse" bracket + label
# magnified tissue (same values feed the art and the key, so they always match)
TISSUE_BG, CELL, CELL_EDGE, NUC = "#5A1C1F", "#8E3B3D", "#4A1416", "#C9787A"
FAT, FAT_EDGE, FAT_HI = "#F2B72E", "#C98A12", "#FFF4CF"
IMM, IMM_RING = "#FFFFFF", "#E2463E"
SCAR, SCAR_EDGE = "#D3CAC2", "#968B83"

# ============================================================== geometry
W = 760                       # viewBox width; rendered 7.66 in wide (1 unit = 0.73 pt, so 7 pt text >= 9.7)
EDGE = 8                      # one outer margin for the severity row, the band and the key, both sides
XS = (95, 285, 475, 665)      # stage centres, symmetric about x = 380
BAND = (156, 357)             # light arrow band behind the circles (top, bottom); it holds the arcs AND their labels
LIVER_S = 0.92                # base liver scale (each stage multiplies its own factor below)
LIVER_BOT = BAND[0] - 4       # every liver's lowest point (stroke included) sits 4 units above the band
LENS_Y, LENS_R = 116, 10      # the magnified spot, mid-body on all four livers
CY, R = 258, 54               # magnified tissue circles
ANCHOR = R + 11               # arc ends and bracket bars sit here, so tips and caps stop clear of the
                              # white ring round each circle (outer edge R + 3.4)
LOW_Y = 331                   # lowest point of every arc and of the bracket (so the labels share one baseline)
LABEL_Y = LOW_Y + 18          # baseline of OFTEN REVERSIBLE / HARDEST TO REVERSE (8 above the band bottom)
KEY_Y, KEY_H = BAND[1] + 6, 28
H = KEY_Y + KEY_H + 3         # total viewBox height

STAGES = [
    # label, subtitle (2023 names per [DELPHI23]), liver scale (fatty livers enlarge, cirrhotic ones shrink)
    ("HEALTHY", "little or no fat", 1.00),
    ("FATTY LIVER", "first stage of MASLD", 1.07),      # MASLD spans steatosis -> MASH -> fibrosis -> cirrhosis [EASL24]
    ("INFLAMED", "MASH, formerly NASH", 1.04),
    ("SCARRING", "fibrosis, then cirrhosis", 0.90),
]
# What pushes each step forward (plain words; mechanisms per [AASLD23] pathogenesis section:
# insulin resistance raises fat delivery to the liver; lipotoxic stress on liver cells drives the
# inflammation of MASH, and "exposure to products derived from the gut microbiome ... may also
# contribute to the NASH phenotype" [AASLD23], hence the hedge "may add to it"; ongoing inflammation
# drives fibrosis).
DRIVERS = [["Insulin resistance", "sends extra fat", "into liver cells"],
           ["Stressed cells spark", "inflammation; gut", "bacteria may add to it"],
           ["Years of", "inflammation", "leave scars"]]

# ============================================================== the liver
# Anterior view: the big right lobe is on the viewer's left, the left lobe tapers right.
# Points walk clockwise; the third value is tangent tension (low = a sharper corner, used
# for the left-lobe tip and the notch where the round ligament enters).
_LIVER_PTS = [
    (3, 38, 1.0), (12, 15, 1.0), (36, 4, 1.0), (64, 3, 1.0), (88, 9, 1.0), (100, 11.5, 0.7),
    (118, 10, 1.0), (134, 15, 0.9), (141, 21, 0.3), (132, 27, 1.0), (112, 34, 1.0),
    (96, 41, 0.6), (90, 46.5, 0.25), (82, 49, 0.8), (62, 59, 1.0), (40, 69, 1.0),
    (20, 70, 1.0), (7, 58, 1.0),
]


def _spline(pts):
    """Closed Catmull-Rom curve through pts as cubic Bezier path data."""
    n = len(pts)
    tan = []
    for i in range(n):
        (x0, y0, _), (_, _, k), (x2, y2, _) = pts[i - 1], pts[i], pts[(i + 1) % n]
        tan.append((k * (x2 - x0) / 2, k * (y2 - y0) / 2))
    d = [f"M{pts[0][0]},{pts[0][1]}"]
    for i in range(n):
        j = (i + 1) % n
        (xa, ya, _), (xb, yb, _) = pts[i], pts[j]
        d.append(f"C{xa + tan[i][0] / 3:.1f},{ya + tan[i][1] / 3:.1f} "
                 f"{xb - tan[j][0] / 3:.1f},{yb - tan[j][1] / 3:.1f} {xb},{yb}")
    return "".join(d) + "Z"


LIVER_D = _spline(_LIVER_PTS)


def _cubic(p0, p1, p2, p3, t):
    m = 1 - t
    return tuple(m ** 3 * p0[k] + 3 * m * m * t * p1[k] + 3 * m * t * t * p2[k] + t ** 3 * p3[k] for k in (0, 1))


def _path_extent(d):
    """(x0, y0, x1, y1) of an M/C path, sampled: the spline bulges a little past its points."""
    nums = [float(v) for v in d.replace("M", " ").replace("C", " ").replace("Z", " ").replace(",", " ").split()]
    cur, pts = (nums[0], nums[1]), []
    for i in range(2, len(nums), 6):
        c1, c2, end = (nums[i], nums[i + 1]), (nums[i + 2], nums[i + 3]), (nums[i + 4], nums[i + 5])
        pts += [_cubic(cur, c1, c2, end, k / 32) for k in range(33)]
        cur = end
    return (min(p[0] for p in pts), min(p[1] for p in pts), max(p[0] for p in pts), max(p[1] for p in pts))


LIVER_EXT = _path_extent(LIVER_D)       # about (2.8, 2.4, 141.0, 71.0) in liver units
# stage 4 is a warm tan-brown (a diseased liver), not grey stone
LIVER_FILL = [("#C55B47", "#8C2E24"), ("#EEC468", "#C88E2E"), ("#DE8457", "#A8432A"), ("#B8936E", "#7A5843")]
LIVER_EDGE = ["#6E241C", "#94661D", "#84331F", "#5A3E2C"]


def _nodule_layout():
    """Regrowth nodules for the cirrhotic liver, packed without overlap (centre spacing at least
    r1 + r2 + 0.8), biggest first, so they read as separate bumps rather than bubble wrap.  A 12-unit
    grid keeps the packing fast (it only ever compares neighbours)."""
    rnd = random.Random(77)
    x0, y0, x1, y1 = LIVER_EXT
    placed, grid, g, tries = [], {}, 12.0, 40000
    for k in range(tries):
        hi = 5.6 - 3.0 * min(1.0, k / (tries * 0.6))
        r = rnd.uniform(max(2.6, hi - 1.2), hi)
        x, y = rnd.uniform(x0 - 3, x1 + 3), rnd.uniform(y0 - 3, y1 + 3)
        gx, gy = int(x // g), int(y // g)
        if all(math.hypot(x - a, y - b) >= r + rb + 0.8
               for i in (gx - 1, gx, gx + 1) for j in (gy - 1, gy, gy + 1) for a, b, rb in grid.get((i, j), ())):
            placed.append((x, y, r))
            grid.setdefault((gx, gy), []).append((x, y, r))
    return placed


NODULES = _nodule_layout()


def _liver_texture(stage):
    if stage == 1:   # pale fat mottling
        return "".join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="#FFF2C6" opacity=".55"/>'
                       for x, y, r in [(30, 30, 9), (57, 20, 6.5), (50, 45, 8), (84, 27, 6), (112, 21, 5), (24, 55, 6), (73, 38, 5)])
    if stage == 2:   # red, angry patches with a little fat left
        return ("".join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="#9E2A1C" opacity=".3"/>'
                        for x, y, r in [(34, 32, 10), (63, 42, 9), (92, 25, 7), (118, 19, 5), (22, 52, 7)])
                + "".join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="#FFE3A6" opacity=".5"/>'
                          for x, y, r in [(52, 20, 5.5), (78, 32, 4.5), (40, 50, 4)]))
    if stage == 3:   # cirrhosis: separate regrowth nodules, each a lit bump with a soft shadow below it
        return "".join(f'<circle cx="{x + r * .10:.1f}" cy="{y + r * .30:.1f}" r="{r * 1.02:.1f}" fill="#4A2E1E" opacity=".34"/>'
                       f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r:.1f}" fill="url(#fl-nod)"/>'
                       f'<circle cx="{x - r * .34:.1f}" cy="{y - r * .36:.1f}" r="{r * .34:.1f}" fill="#FFF1DC" opacity=".38"/>'
                       for x, y, r in NODULES)
    return ""


def liver(cx, bot, s, stage):
    """One liver at scale s, centred on cx, its lowest point (half the 1.4 stroke included) on y = bot.
    Bottom-aligned, so all four sit the same distance above the band whatever their size."""
    x0, _, x1, y1 = LIVER_EXT
    return (f'<g transform="translate({cx - (x0 + x1) / 2 * s:.1f},{bot - (y1 + 0.7) * s:.1f}) scale({s:.3f})">'
            f'<path d="{LIVER_D}" fill="url(#fl-lv{stage})" stroke="{LIVER_EDGE[stage]}" stroke-width="1.4"/>'
            f'<g clip-path="url(#fl-lclip)">{_liver_texture(stage)}</g>'
            # falciform ligament, and a soft sheen along the dome
            '<path d="M100,12.5 C97,24 93.5,35 90.5,45.5" stroke="rgba(0,0,0,.2)" stroke-width="1.4" fill="none"/>'
            '<path d="M17,19 C29,10 46,7.5 62,7.5" stroke="rgba(255,255,255,.5)" stroke-width="3" fill="none" '
            'stroke-linecap="round"/></g>')


# ============================================================== magnified tissue
def _hex(px, py, r, rot=0.0):
    return " ".join(f"{px + r * math.cos(math.radians(a + rot)):.1f},{py + r * math.sin(math.radians(a + rot)):.1f}"
                    for a in range(30, 390, 60))


def sw_cell(r=8.5):
    return (f'<polygon points="{_hex(0, 0, r)}" fill="{CELL}" stroke="{CELL_EDGE}" stroke-width="1.4"/>'
            f'<circle r="{r * 0.3:.1f}" fill="{NUC}"/>')


def sw_fat(r=6.2, x=0, y=0):
    return (f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r:.1f}" fill="{FAT}" stroke="{FAT_EDGE}" stroke-width="1"/>'
            f'<circle cx="{x - r * 0.36:.1f}" cy="{y - r * 0.36:.1f}" r="{r * 0.26:.1f}" fill="{FAT_HI}" opacity=".85"/>')


IMM_R = 4.4                   # immune cell radius in the art; its ring's outer edge is IMM_R + 0.9
IMM_GAP = 11.5                # minimum centre spacing, so rings (10.6 across) never stack


def sw_immune(r=5.0, x=0, y=0):
    return f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r:.1f}" fill="{IMM}" stroke="{IMM_RING}" stroke-width="1.8"/>'


SCAR_FIBRE = "#B5AAA1"        # faint collagen strands along each band of scar

# Close-up 3 (INFLAMED): the immune cells, relative to the circle centre.  Four tight foci of three
# (top, left, bottom, lower right), all in the dark gaps between liver cells.  The positions came from a
# free-space search over this circle's own droplets and nuclei (seed 2026 + 2): every spot keeps
# droplet r + IMM_R + 1 from fat, nucleus r + IMM_R + 1.2 from a nucleus and IMM_GAP from its neighbours.
# _immune_foci re-checks all of that, so the build fails if the tissue ever changes under them.
IMM_FOCI = [(-4, -34), (2, -23), (8, -33),        # top
            (-41, 10), (-36, -1), (-29, 11),      # left
            (-8, 32), (-3, 21), (4, 31),          # bottom
            (21, 30), (28, 20), (33, 31)]         # lower right


def _immune_foci(cx, cy, r, drops, nucs):
    out, placed = [], []
    for ix, iy in IMM_FOCI:
        x, y = cx + ix, cy + iy
        assert math.hypot(ix, iy) <= r - IMM_R - 2.9, "immune cell outside the close-up"
        assert all(math.hypot(x - a, y - b) >= rd + IMM_R + 1 for a, b, rd in drops), "immune cell on fat"
        assert all(math.hypot(x - a, y - b) >= rn + IMM_R + 1.2 for a, b, rn in nucs), "immune cell on a nucleus"
        assert all(math.hypot(x - a, y - b) >= IMM_GAP for a, b in placed), "immune cells stacked"
        placed.append((x, y))
        out.append(sw_immune(IMM_R, x, y))
    return "".join(out)


def tissue(cx, cy, r, stage):
    """Magnified liver tissue: a honeycomb of liver cells, then fat and immune cells.
    Stage 3 (scarring) has its own nodular layout, see _tissue_scarred."""
    if stage == 3:
        return _tissue_scarred(cx, cy, r)
    rnd = random.Random(2026 + stage)
    out = [f'<clipPath id="fl-tc{stage}"><circle cx="{cx}" cy="{cy}" r="{r}"/></clipPath>',
           f'<g clip-path="url(#fl-tc{stage})"><rect x="{cx - r}" y="{cy - r}" width="{2 * r}" height="{2 * r}" fill="{TISSUE_BG}"/>']
    cr, dx, dy = 12, 25, 21.65
    cells = []
    for gy in range(-3, 4):
        for gx in range(-3, 4):
            px, py = cx + gx * dx + (dx / 2 if gy % 2 else 0), cy + gy * dy
            if math.hypot(px - cx, py - cy) < r + cr:
                cells.append((px, py))
    p_fat = {0: 0, 1: 0.66, 2: 0.5}[stage]
    drops, nucs = [], []
    for px, py in cells:
        out.append(f'<polygon points="{_hex(px, py, cr)}" fill="{CELL}" stroke="{CELL_EDGE}" stroke-width="1.6"/>')
        if rnd.random() < p_fat:
            big = rnd.uniform(6.6, 9.4)
            fx, fy = px + rnd.uniform(-1, 1), py + rnd.uniform(-1, 1)
            out.append(sw_fat(big, fx, fy))
            drops.append((fx, fy, big))
            a = rnd.uniform(0, 2 * math.pi)       # the nucleus is squeezed to the cell's edge
            nx, ny = px + 8.6 * math.cos(a), py + 8.6 * math.sin(a)
            out.append(f'<ellipse cx="{nx:.1f}" cy="{ny:.1f}" rx="2.7" ry="1.7" fill="{NUC}" '
                       f'transform="rotate({math.degrees(a) + 90:.0f} {nx:.1f} {ny:.1f})"/>')
            nucs.append((nx, ny, 2.7))
        else:
            out.append(f'<circle cx="{px:.1f}" cy="{py:.1f}" r="3.6" fill="{NUC}"/>')
            nucs.append((px, py, 3.6))
            if stage in (1, 2) and rnd.random() < 0.55:   # a few small droplets beside the nucleus
                a = rnd.uniform(0, 2 * math.pi)
                rs = rnd.uniform(2.4, 3.4)
                sx, sy = px + 6.4 * math.cos(a), py + 6.4 * math.sin(a)
                out.append(sw_fat(rs, sx, sy))
                drops.append((sx, sy, rs))
    if stage == 2:
        out.append(_immune_foci(cx, cy, r, drops, nucs))
    out.append("</g>")
    out.append(f'<circle cx="{cx}" cy="{cy}" r="{r + 2.2}" fill="none" stroke="#FFFFFF" stroke-width="2.4"/>')
    out.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="#2F2222" stroke-width="2.6"/>')
    return "".join(out)


# ---- close-up 4: rounded nodules ringed by scar
SCAR_SEEDS = [(-6, 0), (22, -34), (40, -2), (16, 38), (-30, 30), (-36, -24)]   # one nodule each, centre first
SCAR_WIDTH = (6, 11)          # septum width between two nodules, drawn per pair
SCAR_CR = 10.5                # liver cells in the nodules (a touch smaller, so each nodule holds more)


def _clip_half(poly, nx, ny, c):
    """The part of a polygon where nx*x + ny*y <= c (Sutherland-Hodgman)."""
    out = []
    for i in range(len(poly)):
        a, b = poly[i], poly[(i + 1) % len(poly)]
        da, db = nx * a[0] + ny * a[1] - c, nx * b[0] + ny * b[1] - c
        if da <= 0:
            out.append(a)
        if (da < 0) != (db < 0) and da != db:
            t = da / (da - db)
            out.append((a[0] + t * (b[0] - a[0]), a[1] + t * (b[1] - a[1])))
    return out


def _voronoi(seeds, widths, reach):
    """Each seed's Voronoi cell inside a circle of radius `reach`, pulled back from every neighbour by
    half the septum width between them (widths[(i, j)], 0 when absent)."""
    base = [(reach * math.cos(math.pi * k / 36), reach * math.sin(math.pi * k / 36)) for k in range(72)]
    cells = []
    for i, s in enumerate(seeds):
        poly = base
        for j, t in enumerate(seeds):
            if i != j:
                m = math.hypot(t[0] - s[0], t[1] - s[1])
                ux, uy = (t[0] - s[0]) / m, (t[1] - s[1]) / m
                mx, my = (s[0] + t[0]) / 2, (s[1] + t[1]) / 2
                poly = _clip_half(poly, ux, uy, ux * mx + uy * my - widths.get((min(i, j), max(i, j)), 0) / 2)
        cells.append(poly)
    return cells


def _rounded(poly, rho, step=1.2):
    """Dense outline of a convex polygon whose corners are rounded (quadratic, about radius rho)."""
    n, pts = len(poly), []
    for i in range(n):
        p0, p1, p2 = poly[i - 1], poly[i], poly[(i + 1) % n]
        l1, l2 = math.hypot(p1[0] - p0[0], p1[1] - p0[1]), math.hypot(p2[0] - p1[0], p2[1] - p1[1])
        if l1 < 1e-6 or l2 < 1e-6:
            continue
        t1, t2 = min(rho / l1, 0.5), min(rho / l2, 0.5)
        a = (p1[0] + (p0[0] - p1[0]) * t1, p1[1] + (p0[1] - p1[1]) * t1)
        b = (p1[0] + (p2[0] - p1[0]) * t2, p1[1] + (p2[1] - p1[1]) * t2)
        k = max(3, int((l1 * t1 + l2 * t2) / step))
        for s in range(k):
            u = s / k
            pts.append(((1 - u) ** 2 * a[0] + 2 * (1 - u) * u * p1[0] + u * u * b[0],
                        (1 - u) ** 2 * a[1] + 2 * (1 - u) * u * p1[1] + u * u * b[1]))
        a2 = (p2[0] + (p1[0] - p2[0]) * t2, p2[1] + (p1[1] - p2[1]) * t2)   # the next corner's start
        k = max(1, int(math.hypot(a2[0] - b[0], a2[1] - b[1]) / step))
        pts += [(b[0] + (a2[0] - b[0]) * s / k, b[1] + (a2[1] - b[1]) * s / k) for s in range(k)]
    return pts


def _wobble(pts, amp, rnd):
    """Push each outline point along its outward normal by a smooth random wave, so nodule edges
    (and the scar between them) swell and thin a little like real septa."""
    n = len(pts)
    ph1, ph2 = rnd.uniform(0, 6.28), rnd.uniform(0, 6.28)
    f1, f2 = rnd.choice([3, 4, 5]), rnd.choice([7, 8, 9])
    mx, my = sum(p[0] for p in pts) / n, sum(p[1] for p in pts) / n
    out = []
    for i, (x, y) in enumerate(pts):
        a, b = pts[i - 1], pts[(i + 1) % n]
        tx, ty = b[0] - a[0], b[1] - a[1]
        m = math.hypot(tx, ty) or 1
        nx, ny = ty / m, -tx / m
        if (x - mx) * nx + (y - my) * ny < 0:
            nx, ny = -nx, -ny
        s = i / n * 2 * math.pi
        w = amp * (0.7 * math.sin(f1 * s + ph1) + 0.3 * math.sin(f2 * s + ph2))
        out.append((x + nx * w, y + ny * w))
    return out


def _inside(poly, x, y):
    c = False
    for i in range(len(poly)):
        (x1, y1), (x2, y2) = poly[i], poly[(i + 1) % len(poly)]
        if (y1 > y) != (y2 > y) and x < x1 + (y - y1) * (x2 - x1) / (y2 - y1):
            c = not c
    return c


def _seg_in_circle(a, b, rr):
    """The part of segment a-b inside a circle of radius rr round the origin, or None."""
    dx, dy = b[0] - a[0], b[1] - a[1]
    qa, qb, qc = dx * dx + dy * dy, 2 * (a[0] * dx + a[1] * dy), a[0] ** 2 + a[1] ** 2 - rr * rr
    disc = qb * qb - 4 * qa * qc
    if qa < 1e-9 or disc <= 0:
        return None
    t0, t1 = max(0.0, (-qb - math.sqrt(disc)) / (2 * qa)), min(1.0, (-qb + math.sqrt(disc)) / (2 * qa))
    if t1 - t0 < 1e-6:
        return None
    return (a[0] + dx * t0, a[1] + dy * t0), (a[0] + dx * t1, a[1] + dy * t1)


def _tissue_scarred(cx, cy, r):
    """Close-up 4 (cirrhosis): rounded nodules of liver cells walled off by scar.  Six seeds make a Voronoi
    layout; each nodule is its seed's cell pulled back by half the septum width on every side (6 to 11
    units, per pair), its corners rounded and its edge given a gentle wobble.  Where three nodules meet
    the scar forks.  Each nodule has its own tilted cell grid, so cell rows never run on across the scar.
    A few immune cells sit on the scar's edge (inflammation at the border)."""
    wr = random.Random(5)
    n = len(SCAR_SEEDS)
    widths = {(i, j): wr.uniform(*SCAR_WIDTH) for i in range(n) for j in range(i + 1, n)}
    rnd = random.Random(4)
    nodules = _voronoi(SCAR_SEEDS, widths, r + 30)
    plain = _voronoi(SCAR_SEEDS, {}, r + 30)
    out = [f'<clipPath id="fl-tc3"><circle cx="{cx}" cy="{cy}" r="{r}"/></clipPath>',
           f'<g clip-path="url(#fl-tc3)"><rect x="{cx - r}" y="{cy - r}" width="{2 * r}" height="{2 * r}" fill="{SCAR}"/>']
    # collagen fibres: two faint strands along every septum centre line (the plain Voronoi edges),
    # trimmed short of the junctions so strands from different septa do not cross there
    for poly in plain:
        for k in range(len(poly)):
            a, b = poly[k], poly[(k + 1) % len(poly)]
            if math.hypot(*a) > r + 25 and math.hypot(*b) > r + 25:
                continue                       # part of the outer frame, not a septum
            tx, ty = b[0] - a[0], b[1] - a[1]
            m = math.hypot(tx, ty) or 1
            ux, uy, nx, ny = tx / m, ty / m, -ty / m, tx / m
            a, b = (a[0] + ux * 3.5, a[1] + uy * 3.5), (b[0] - ux * 3.5, b[1] - uy * 3.5)
            for off in (-1.6, 1.4):
                out.append(f'<path d="M{cx + a[0] + nx * off:.1f},{cy + a[1] + ny * off:.1f} '
                           f'L{cx + b[0] + nx * off:.1f},{cy + b[1] + ny * off:.1f}" stroke="{SCAR_FIBRE}" '
                           'stroke-width=".8" fill="none" stroke-linecap="round"/>')
    drops, nucs, rims = [], [], []
    ddx, ddy = SCAR_CR * math.sqrt(3), SCAR_CR * 1.5
    for i, poly in enumerate(nodules):
        rim = [(cx + x, cy + y) for x, y in _wobble(_rounded(poly, 7), 1.1, rnd)]
        rims.append(rim)
        d = "M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in rim) + "Z"
        out.append(f'<clipPath id="fl-isl{i}"><path d="{d}"/></clipPath><g clip-path="url(#fl-isl{i})">'
                   f'<path d="{d}" fill="{TISSUE_BG}"/>')
        rot = rnd.uniform(-25, 25)
        ox, oy = rnd.uniform(0, 2 * SCAR_CR), rnd.uniform(0, 2 * SCAR_CR)
        ca, sa = math.cos(math.radians(rot)), math.sin(math.radians(rot))
        sx, sy = cx + SCAR_SEEDS[i][0], cy + SCAR_SEEDS[i][1]
        for gy in range(-6, 7):
            for gx in range(-6, 7):
                lx, ly = gx * ddx + (ddx / 2 if gy % 2 else 0) + ox, gy * ddy + oy
                px, py = sx + lx * ca - ly * sa, sy + lx * sa + ly * ca
                edge = min(math.hypot(px - q[0], py - q[1]) for q in rim)
                inside = _inside(rim, px, py)
                if not inside and edge > SCAR_CR:
                    continue
                out.append(f'<polygon points="{_hex(px, py, SCAR_CR, rot)}" fill="{CELL}" stroke="{CELL_EDGE}" stroke-width="1.5"/>')
                if rnd.random() < 0.18:
                    big = rnd.uniform(4.2, 6.0)
                    fx, fy = px + rnd.uniform(-1, 1), py + rnd.uniform(-1, 1)
                    a = rnd.uniform(0, 2 * math.pi)
                    if inside and edge >= big + 1.5:      # fat only where the whole droplet fits in the nodule
                        out.append(sw_fat(big, fx, fy))
                        drops.append((fx, fy, big))
                        nx, ny = px + 7.4 * math.cos(a), py + 7.4 * math.sin(a)
                        out.append(f'<ellipse cx="{nx:.1f}" cy="{ny:.1f}" rx="2.4" ry="1.5" fill="{NUC}" '
                                   f'transform="rotate({math.degrees(a) + 90:.0f} {nx:.1f} {ny:.1f})"/>')
                        nucs.append((nx, ny, 2.4))
                        continue
                out.append(f'<circle cx="{px:.1f}" cy="{py:.1f}" r="3.2" fill="{NUC}"/>')
                if inside:                            # a centre outside the nodule is clipped away
                    nucs.append((px, py, 3.2))
        out.append("</g>")
        out.append(f'<path d="{d}" fill="none" stroke="{SCAR_EDGE}" stroke-width="1.6" stroke-linejoin="round"/>')
    # immune cells in the scar: points along each septum's centre line inside the view (its middle,
    # then its thirds), kept clear of fat, visible nuclei, each other and the circle's edge
    placed = []
    for i in range(n):
        for j in range(i + 1, n):
            si, sj = SCAR_SEEDS[i], SCAR_SEEDS[j]
            m = math.hypot(sj[0] - si[0], sj[1] - si[1])
            ux, uy = (sj[0] - si[0]) / m, (sj[1] - si[1]) / m
            mx, my = (si[0] + sj[0]) / 2, (si[1] + sj[1]) / 2
            on = [v for v in plain[i] if abs((v[0] - mx) * ux + (v[1] - my) * uy) < 1e-6]
            if len(on) < 2:
                continue                       # not neighbours
            seg = _seg_in_circle(on[0], on[1], r - IMM_R - 6)
            if not seg:
                continue
            (ax, ay), (bx, by) = seg
            for f in (0.5, 0.33, 0.67):
                x, y = cx + ax + (bx - ax) * f, cy + ay + (by - ay) * f
                if (all(math.hypot(x - a, y - b) >= rd + IMM_R + 1 for a, b, rd in drops)
                        and all(math.hypot(x - a, y - b) >= rn + IMM_R + 0.9 for a, b, rn in nucs)
                        and all(math.hypot(x - a, y - b) >= 2 * IMM_GAP for a, b in placed)):
                    placed.append((x, y))
                    out.append(sw_immune(IMM_R, x, y))
                    break
            if len(placed) == 5:
                break
        if len(placed) == 5:
            break
    out.append("</g>")
    out.append(f'<circle cx="{cx}" cy="{cy}" r="{r + 2.2}" fill="none" stroke="#FFFFFF" stroke-width="2.4"/>')
    out.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="#2F2222" stroke-width="2.6"/>')
    return "".join(out)


def _cone(cx):
    """Zoom callout: the two outer tangents from the lens on the liver to its tissue circle."""
    d = CY - LENS_Y
    s = (R - LENS_R) / d
    c = math.sqrt(1 - s * s)
    p1y, p2y = LENS_Y - LENS_R * s, CY - R * s
    a, b = LENS_R * c, R * c
    # the beam runs round the underside of the lens, so the lens itself stays one even tint
    beam = (f"M{cx - a:.1f},{p1y:.1f} A{LENS_R},{LENS_R} 0 1 0 {cx + a:.1f},{p1y:.1f} "
            f"L{cx + b:.1f},{p2y:.1f} L{cx - b:.1f},{p2y:.1f} Z")
    return (f'<path d="{beam}" fill="#FFFFFF" fill-opacity=".45"/>'
            f'<path d="M{cx - a:.1f},{p1y:.1f} L{cx - b:.1f},{p2y:.1f} M{cx + a:.1f},{p1y:.1f} L{cx + b:.1f},{p2y:.1f}" '
            'stroke="#6F6763" stroke-width="1.2" stroke-opacity=".7" fill="none"/>')


def _lens(cx):
    return (f'<circle cx="{cx}" cy="{LENS_Y}" r="{LENS_R}" fill="#FFFFFF" fill-opacity=".18" stroke="#FFFFFF" stroke-width="2.4"/>'
            f'<circle cx="{cx}" cy="{LENS_Y}" r="{LENS_R + 1.6}" fill="none" stroke="#2F2222" stroke-width=".9" stroke-opacity=".55"/>')


# ============================================================== arrows and labels
def _q(p0, c, p1, t):
    return tuple((1 - t) ** 2 * p0[i] + 2 * (1 - t) * t * c[i] + t * t * p1[i] for i in (0, 1))


def _unit(vx, vy):
    m = math.hypot(vx, vy) or 1
    return vx / m, vy / m


def _on_circle(cx, deg, rr):
    return cx + rr * math.cos(math.radians(deg)), CY + rr * math.sin(math.radians(deg))


def _span(s, e):
    """Control point that puts the curve's lowest point on LOW_Y (s and e sit at the same height)."""
    return ((s[0] + e[0]) / 2, 2 * LOW_Y - (s[1] + e[1]) / 2)


def _reverse_arc(a, b):
    """Green arc from under circle a back to circle b (toward healthy), arrowhead at b.
    Both ends stop at ANCHOR, so the tail and the arrow tip sit just clear of the white ring."""
    s, e = _on_circle(XS[a], 125, ANCHOR), _on_circle(XS[b], 55, ANCHOR)
    c = _span(s, e)
    ux, uy = _unit(e[0] - c[0], e[1] - c[1])
    tip = (e[0] + ux * 6, e[1] + uy * 6)
    base = (e[0] - ux * 7, e[1] - uy * 7)
    head = (f"{tip[0]:.1f},{tip[1]:.1f} {base[0] - uy * 8:.1f},{base[1] + ux * 8:.1f} "
            f"{base[0] + uy * 8:.1f},{base[1] - ux * 8:.1f}")
    low = _q(s, c, e, 0.5)
    return (f'<path d="M{s[0]:.1f},{s[1]:.1f} Q{c[0]:.1f},{c[1]:.1f} {e[0]:.1f},{e[1]:.1f}" stroke="{GREEN}" '
            f'stroke-width="6" fill="none" stroke-linecap="round"/><polygon points="{head}" fill="{GREEN}" stroke="{GREEN}" '
            f'stroke-width="1.5" stroke-linejoin="round"/>', low)


def _hard_bracket(a, b):
    """Red bracket spanning circles a..b: the step that is hardest to undo.  Its T-bars are centred
    on ANCHOR, so even their round caps stop short of the white ring."""
    s, e = _on_circle(XS[a], 55, ANCHOR), _on_circle(XS[b], 125, ANCHOR)
    c = _span(s, e)
    out = [f'<path d="M{s[0]:.1f},{s[1]:.1f} Q{c[0]:.1f},{c[1]:.1f} {e[0]:.1f},{e[1]:.1f}" stroke="{RED}" '
           'stroke-width="6" fill="none" stroke-linecap="round"/>']
    for p, (tx, ty) in ((s, (c[0] - s[0], c[1] - s[1])), (e, (e[0] - c[0], e[1] - c[1]))):
        ux, uy = _unit(tx, ty)
        out.append(f'<path d="M{p[0] - uy * 9:.1f},{p[1] + ux * 9:.1f} L{p[0] + uy * 9:.1f},{p[1] - ux * 9:.1f}" '
                   f'stroke="{RED}" stroke-width="6" stroke-linecap="round"/>')
    return "".join(out), _q(s, c, e, 0.5)


def _severity_row(y):
    """LEAST SEVERE ====gradient arrow====> MOST SEVERE, across the top of the diagram, on the shared margin."""
    fs, ls = 12.5, 0.8
    wl, wr = tw("LEAST SEVERE", fs, 800, ls), tw("MOST SEVERE", fs, 800, ls)
    m, gap = EDGE, 12
    x0, x1 = m + wl + gap, W - m - wr - gap
    h, hh = 10, 9.5          # bar thickness, arrowhead half-height
    bar = (f'<path d="M{x0 + h / 2:.1f},{y - h / 2} H{x1 - 20:.1f} V{y - hh} L{x1:.1f},{y} L{x1 - 20:.1f},{y + hh} '
           f'V{y + h / 2} H{x0 + h / 2:.1f} A{h / 2},{h / 2} 0 0 1 {x0 + h / 2:.1f},{y - h / 2} Z" fill="url(#fl-sev)"/>')
    grad = ('<linearGradient id="fl-sev" gradientUnits="userSpaceOnUse" '
            f'x1="{x0:.1f}" y1="0" x2="{x1:.1f}" y2="0">'
            + "".join(f'<stop offset="{o}" stop-color="{c}"/>' for o, c in zip((0, .38, .68, 1), SEV_BAR))
            + "</linearGradient>")
    return grad, (bar + T(m, y + 4.5, "LEAST SEVERE", fs, 800, GREEN_TX, ls=ls)
                  + T(W - m, y + 4.5, "MOST SEVERE", fs, 800, RED_TX, "end", ls=ls))


def _stage_label(i, cx):
    lab, sub, _ = STAGES[i]
    fs, ls, br, gap = 17, 0.6, 12, 7
    w = 2 * br + gap + tw(lab, fs, 800, ls)
    bx = cx - w / 2 + br
    return (f'<circle cx="{bx:.1f}" cy="49" r="{br}" fill="{SEV[i]}"/>'
            + T(bx, 53.6, str(i + 1), 13, 800, "#FFFFFF", "middle")
            + T(bx + br + gap, 55, lab, fs, 800, INK, ls=ls)
            + T(cx, 73, sub, 11.5, 600, INK2, "middle", italic=True))


# ---- the key: every swatch sits on a small dark tissue chip, exactly as it looks in the close-ups
CHIP_W, CHIP_H = 26, 19


def _chip(inner, clip_id=None):
    x, y = -CHIP_W / 2, -CHIP_H / 2
    rect = f'<rect x="{x}" y="{y}" width="{CHIP_W}" height="{CHIP_H}" rx="4" fill="{TISSUE_BG}"/>'
    if not clip_id:
        return rect + inner
    return (f'<clipPath id="{clip_id}"><rect x="{x}" y="{y}" width="{CHIP_W}" height="{CHIP_H}" rx="4"/></clipPath>'
            + rect + f'<g clip-path="url(#{clip_id})">{inner}</g>')


def sw_scar():
    """Key swatch: a straight piece of septum as wide as the art's bands, with the same pale fill,
    dark edges (the nodule rims) and two fibre strands, cut off by its chip."""
    hw = 3.9
    band = (f'<g transform="rotate(-26)"><rect x="-22" y="{-hw}" width="44" height="{2 * hw}" fill="{SCAR}"/>'
            f'<path d="M-22,{-hw} H22 M-22,{hw} H22" stroke="{SCAR_EDGE}" stroke-width="1.6"/>'
            f'<path d="M-22,-1.6 H22 M-22,1.4 H22" stroke="{SCAR_FIBRE}" stroke-width=".8"/></g>')
    return _chip(band, "fl-kscar")


def _key(y):
    """KEY to everything drawn inside the magnified circles (same swatch code as the art)."""
    hw = CHIP_W / 2
    items = [(_chip(sw_cell(7.4)), "Liver cell (pink = nucleus)"), (_chip(sw_fat(5.8)), "Fat droplet"),
             (_chip(sw_immune(4.6)), "Immune cell"), (sw_scar(), "Scar tissue")]
    x0, x1, h = EDGE, W - EDGE, KEY_H
    title, fs, base = "KEY TO THE CLOSE-UPS", 11.5, y + h / 2 + 4.1
    tx = x0 + 14
    start = tx + tw(title, 10.5, 800, 1.2) + 24
    widths = [2 * hw + 7 + tw(lab, fs, 600) for _, lab in items]
    gap = (x1 - 16 - start - sum(widths)) / (len(items) - 1)
    assert gap >= 14, "key too crowded"
    out = [f'<rect x="{x0}" y="{y}" width="{x1 - x0}" height="{h}" rx="8" fill="#FFFFFF" stroke="#D9D1CD" stroke-width="1.2"/>',
           T(tx, base - 0.2, title, 10.5, 800, INK, ls=1.2)]
    x = start
    for (sw, lab), wd in zip(items, widths):
        out.append(f'<g transform="translate({x + hw:.1f},{y + h / 2})">{sw}</g>')
        out.append(T(f"{x + 2 * hw + 7:.1f}", base, lab, fs, 600, INK))
        x += wd + gap
    return "".join(out)


def _cone_half(y):
    """Half-width of a zoom beam at height y (between the tangent points it is a straight taper)."""
    s = (R - LENS_R) / (CY - LENS_Y)
    c = math.sqrt(1 - s * s)
    p1y, p2y = LENS_Y - LENS_R * s, CY - R * s
    return LENS_R * c + (R - LENS_R) * c * (y - p1y) / (p2y - p1y)


def _zoom_tag(cx, y):
    """'Close-up' tag inside the first zoom beam (the key's own word), so a reader knows the circles are
    close-ups of the liver.  Checked: the pill stays inside the beam with room to spare (see the assert)."""
    lab, fs = "Close-up", 10.2
    w, h = tw(lab, fs, 700) + 9, 14.5
    assert w / 2 + 6 <= _cone_half(y), "zoom tag too wide for the beam"
    return (f'<rect x="{cx - w / 2:.1f}" y="{y - h / 2:.1f}" width="{w:.1f}" height="{h}" rx="{h / 2}" '
            'fill="#FFFFFF" stroke="#B9AFA9" stroke-width=".9"/>'
            + T(cx, y + 3.7, lab, fs, 700, INK2, "middle"))


def art_progression(t):
    defs = ['<defs>',
            f'<clipPath id="fl-lclip"><path d="{LIVER_D}"/></clipPath>',
            '<linearGradient id="fl-band" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#E7F0E1"/>'
            '<stop offset=".5" stop-color="#F6F0E4"/><stop offset="1" stop-color="#F8E0DB"/></linearGradient>',
            # a cirrhotic nodule: lit from the upper left, darker at its rim
            '<radialGradient id="fl-nod" cx=".4" cy=".36" r=".72"><stop offset="0" stop-color="#D9B994"/>'
            '<stop offset=".7" stop-color="#B48C66"/><stop offset="1" stop-color="#9C7652"/></radialGradient>']
    for i, (c1, c2) in enumerate(LIVER_FILL):
        defs.append(f'<linearGradient id="fl-lv{i}" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{c1}"/>'
                    f'<stop offset="1" stop-color="{c2}"/></linearGradient>')
    sev_grad, sev_row = _severity_row(18)
    defs.append(sev_grad)
    defs.append("</defs>")
    out = ["".join(defs), sev_row]
    for i, cx in enumerate(XS):
        out.append(_stage_label(i, cx))
    top, bot = BAND
    mid = (top + bot) / 2
    e = EDGE
    out.append(f'<path d="M{e + 12},{top} H{W - e - 60} L{W - e},{mid} L{W - e - 60},{bot} H{e + 12} '
               f'Q{e},{bot} {e},{bot - 12} V{top + 12} Q{e},{top} {e + 12},{top} Z" '
               'fill="url(#fl-band)" stroke="#E2D8D2" stroke-width="1"/>')
    for i, cx in enumerate(XS):
        out.append(liver(cx, LIVER_BOT, LIVER_S * STAGES[i][2], i))
    for cx in XS:
        out.append(_cone(cx))
        out.append(_lens(cx))
    out.append(_zoom_tag(XS[0], 188))
    for i, cx in enumerate(XS):
        out.append(tissue(cx, CY, R, i))
    for i, lines in enumerate(DRIVERS):
        gx = (XS[i] + XS[i + 1]) / 2
        out.append(T(gx, 174, lines, 10.2, 700, "#454C52", "middle", lh=1.22))
        out.append(f'<path d="M{gx - 14},211 H{gx + 7}" stroke="#8A9096" stroke-width="2.4" stroke-linecap="round"/>'
                   f'<path d="M{gx + 5},205.5 L{gx + 14},211 L{gx + 5},216.5 Z" fill="#8A9096"/>')
    for a, b in ((1, 0), (2, 1)):
        arc, low = _reverse_arc(a, b)
        out.append(arc)
        out.append(T(low[0], LABEL_Y, "OFTEN REVERSIBLE", 12.5, 800, GREEN_TX, "middle", ls=0.4))
    br, low = _hard_bracket(2, 3)
    out.append(br)
    out.append(T(low[0], LABEL_Y, "HARDEST TO REVERSE", 12.5, 800, RED_TX, "middle", ls=0.4))
    out.append(_key(KEY_Y))
    return svg(W, H, "".join(out), "How fatty liver disease progresses from a healthy liver to scarring, "
               "with magnified views of the liver tissue at each stage")


# ============================================================== blocks under the art
RISKS = [  # each factor is named in [AASLD23]
    ("soda", "Sugary drinks,<br>added sugar"),
    ("meter", "Insulin resistance<br>or diabetes"),            # T2DM: "the most impactful risk factor"
    ("waist", "Weight carried<br>at the belly"),
    ("heartpulse", "High blood<br>pressure"),
    ("tube", "High blood fats<br>(triglycerides)"),
    ("ovaries", "PCOS (polycystic<br>ovary syndrome)"),        # 2- to 4-fold higher MASLD prevalence
    ("dna", "Family history<br>and genes"),                     # PNPLA3; relatives of NASH cirrhosis
    ("gut", "Gut imbalance<br>(being studied)"),                # [AASLD23]: gut microbiome products "may also contribute"
]

# Two glyphs drawn here in the kit's line style (64-unit grid, round caps, stroke 2.8 like the rest of the row)
_RISK_ICONS = {
    # a soda cup with a dome lid and a straw: "sugary drinks" at a glance (the kit's sugar cube read as a box)
    "soda": ('<path d="M18 25h28"/><path d="M21 25a11 6 0 0 1 22 0"/>'
             '<path d="M20 25l3.6 29.2a3 3 0 0 0 3 2.6h10.8a3 3 0 0 0 3-2.6L44 25"/>'
             '<path d="M34 19.2 37.6 7H45"/><path d="M21.5 37h21"/>'),
    # a uterus with its tubes and ovaries (PCOS), in place of the abstract calendar
    "ovaries": ('<path d="M25 21c0-4 14-4 14 0 0 9-3 15-4.6 19.5V50h-4.8V40.5C28 36 25 30 25 21z"/>'
                '<path d="M25.5 21.5C20 15 13 15 10 21"/><path d="M38.5 21.5C44 15 51 15 54 21"/>'
                '<ellipse cx="12.5" cy="29" rx="5.5" ry="4.3"/><ellipse cx="51.5" cy="29" rx="5.5" ry="4.3"/>'),
}


def _risk_icon(name, size="0.33in", sw=2.8):
    if name not in _RISK_ICONS:
        return icon(name, size, sw=sw)
    return (f'<svg class="ic" viewBox="0 0 64 64" style="width:{size};height:{size};color:currentColor" fill="none" '
            f'stroke="currentColor" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round" '
            f'aria-hidden="true">{_RISK_ICONS[name]}</svg>')


_STEP_ICONS = {
    "vial": ('<g transform="rotate(20 32 32)"><path d="M22 7h20"/><path d="M26.5 7v39a5.5 5.5 0 0 0 11 0V7"/>'
             '<path d="M26.5 28h11v18a5.5 5.5 0 0 1-11 0z" fill="currentColor" fill-opacity=".3" stroke="none"/>'
             '<path d="M26.5 28h11"/></g>'),
    "gauge": ('<path d="M9 45a23 23 0 0 1 46 0"/><path d="M15.7 29.7l3.6 3M32 22v5M48.3 29.7l-3.6 3"/>'
              '<path d="M32 45 43.5 31.5"/><circle cx="32" cy="45" r="4" fill="currentColor" stroke="none"/><path d="M13 54h38"/>'),
    "probe": ('<path d="M26 6h12v20l-2.5 12h-7L26 26z"/><path d="M8 44h48"/>'
              '<path d="M22 50.5c6 3.6 14 3.6 20 0M16.5 57.5c9 5 22 5 31 0"/>'),
}


def _ico(name, px=24):
    return (f'<svg viewBox="0 0 64 64" style="width:{px}px;height:{px}px" fill="none" stroke="currentColor" '
            f'stroke-width="4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{_STEP_ICONS[name]}</svg>')


_ARROW = ('<svg viewBox="0 0 12 22" style="width:9px;height:17px" aria-hidden="true"><path d="M2.5 2.5 9.5 11 2.5 19.5" '
          'fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/></svg>')

# The three checks, in the order AASLD 2023 lays them out for primary care [AASLD23]:
#  - "Serum AST levels are often used clinically to identify patients with liver disease but can be normal
#    in patients with diabetes, NASH, and advanced hepatic fibrosis" (hence "normal levels do not rule out")
#  - "normal values provided by most laboratories are higher than what should be considered normal in
#    NAFLD, in which a true normal alanine aminotransferase (ALT) ranges from 29 to 33 U/L in men and
#    from 19 to 25 U/L in women": upper limits, so the dots give the top of each range ("about ... or less")
#  - FIB-4 is "based upon age, ALT, AST, and platelet count"; low risk is "FIB-4 <1.3"
#  - FIB-4 >= 1.3 -> VCTE (eg, FibroScan) favoured as the secondary test in primary care; it measures
#    liver stiffness, and its CAP reading "provides a point-of-care semiquantitative assessment of
#    hepatic steatosis but does not accurately quantify" liver fat (hence "estimates")
#  - VCTE "LSM <8 kPa can be used to rule out advanced fibrosis"; intermediate or high risk on the
#    secondary test -> "referred to specialty care" (red: the most serious result on the page)
CHECKS = [
    ("vial", "Liver enzymes (ALT, AST)",
     "A routine blood test. High levels can mean the liver is irritated, but normal levels do not rule out "
     "fatty liver.",
     [(SEV[0], "Healthy ALT, women: about 25 or less"), (SEV[0], "Healthy ALT, men: about 33 or less")]),
    ("gauge", "FIB-4 score",
     "Worked out from your age and routine labs (ALT, AST, platelets) to estimate the risk of advanced scarring.",
     [(SEV[0], "Under 1.3: low risk"), (SEV[1], "1.3 or higher: a FibroScan is next")]),
    ("probe", "FibroScan (elastography)",
     "A no-needle scan that measures liver stiffness (scarring) and estimates liver fat. "
     "The next step if FIB-4 is 1.3 or higher.",
     [(SEV[0], "Under 8 kPa: low risk"), (SEV[3], "8 kPa or more: see a liver specialist")]),
]


def _ed(x, ed):
    return x.replace("{who}", ed["who"]).replace("{Who}", ed["Who"])


def risk_strip():
    cells = "".join(f'<div class="flv-rf"><span class="flv-disc">{_risk_icon(ic)}</span>'
                    f'<span class="flv-rl">{lab}</span></div>' for ic, lab in RISKS)
    return f'<div class="flv-risk">{cells}</div>'


def ask_panel(ed):
    cards = []
    for n, (ic, title, body, dots) in enumerate(CHECKS, 1):
        extra = ""
        if dots:
            extra = '<ul class="flv-dots">' + "".join(f'<li><i style="background:{c}"></i>{x}</li>' for c, x in dots) + "</ul>"
        cards.append(f'<div class="flv-step"><div class="flv-sh"><span class="flv-n">{n}</span>{_ico(ic)}<b>{title}</b></div>'
                     f'<p>{body}</p>{extra}</div>')
    steps = f'<div class="flv-arr">{_ARROW}</div>'.join(cards)
    # [AASLD23]: "In most patients, NAFLD is asymptomatic or associated with vague symptoms"
    lead = "You may feel fine. Ask {who} which checks fit you."
    if "pharmacist" in ed["who"]:    # a pharmacist can advise, but a doctor orders the labs and the scan
        lead = "You may feel fine. Ask {who} which checks fit you; your doctor can order them."
    # [AASLD23]: ">= 2 metabolic risk factors, particularly prediabetes or T2DM ... FIB-4 every 1-2 years"
    foot = "<b>Two or more metabolic risks, like prediabetes or belly fat?</b> Check FIB-4 every 1 to 2 years."
    return (f'<div class="flv-ask"><div class="flv-askhd"><b>Ask about liver checks</b><span>{_ed(lead, ed)}</span></div>'
            f'<div class="flv-steps">{steps}</div>'
            f'<div class="flv-foot"><span>{foot}</span><small>AASLD practice guidance, 2023</small></div></div>')


def front(t, ed):
    return ('<div class="flv">'
            '<h2 class="flv-h">How fatty liver progresses</h2>'
            f'<div class="art flv-art">{art_progression(t)}</div>'
            '<h2 class="flv-h">What raises your risk</h2>'
            f'{risk_strip()}{ask_panel(ed)}</div>')


CSS = r"""
.flv-h{display:flex;align-items:center;gap:0.1in;font:900 11pt/1.2 Merriweather,Georgia,serif;color:var(--c1);
  letter-spacing:.04em;text-transform:uppercase;margin:0.02in 0 0.06in}
.flv-h::after{content:"";flex:1;height:2px;border-radius:2px;background:linear-gradient(90deg,var(--soft),rgba(246,228,225,0))}
.flv-art+.flv-h{margin-top:0.08in}
.flv-risk{display:grid;grid-template-columns:repeat(8,1fr);gap:0 0.04in}
.flv-risk .x{display:none}
.flv-rf{display:flex;flex-direction:column;align-items:center;text-align:center}
.flv-disc{width:0.52in;height:0.52in;border-radius:50%;background:var(--soft);color:var(--c1);display:flex;
  align-items:center;justify-content:center;box-shadow:inset 0 0 0 1.5px rgba(138,27,34,.10)}
.flv-rl{display:block;font-size:7.8pt;font-weight:600;line-height:1.22;color:#2F373C;margin-top:0.03in}
.flv-ask{margin-top:0.11in;background:var(--tint);border:1px solid #EBD3CE;border-radius:10px;padding:0.08in 0.12in 0.07in}
.flv-askhd{display:flex;align-items:baseline;gap:0.12in;margin:0 0 0.06in}
.flv-askhd b{flex:none;font:900 11pt/1.2 Merriweather,Georgia,serif;color:var(--c1);letter-spacing:.04em;text-transform:uppercase}
.flv-askhd span{font-size:8.4pt;line-height:1.3;color:#2B3236}
.flv-steps{display:grid;grid-template-columns:1fr 16px 1fr 16px 1fr;align-items:stretch}
.flv-step{background:#fff;border:1px solid #EDDDD9;border-radius:8px;padding:0.06in 0.08in 0.07in;box-shadow:0 1px 2px rgba(80,20,20,.06)}
.flv-sh{display:flex;align-items:center;gap:6px;margin:0 0 4px}
.flv-n{flex:none;width:17px;height:17px;border-radius:50%;background:var(--c1);color:#fff;font:800 8pt/1 Inter,sans-serif;
  display:flex;align-items:center;justify-content:center}
.flv-sh svg{flex:none;color:var(--c1)}
.flv-sh b{font:800 8.8pt/1.15 Inter,sans-serif;color:var(--deep)}
.flv-step p{margin:0;font-size:7.8pt;line-height:1.32;color:#2B3236}
.flv-dots{list-style:none;margin:4px 0 0;padding:0}
.flv-dots li{display:flex;align-items:center;gap:5px;font-size:7.6pt;font-weight:700;line-height:1.3;color:#2B3236;margin:1px 0}
.flv-dots i{flex:none;width:8px;height:8px;border-radius:50%}
.flv-arr{display:flex;align-items:center;justify-content:center;color:var(--c2)}
.flv-foot{display:flex;justify-content:space-between;align-items:baseline;gap:0.2in;margin-top:0.06in;font-size:7.4pt;color:#3F4A50}
.flv-foot b{color:var(--deep)}
.flv-foot small{font-size:7.2pt;color:#6A747B;white-space:nowrap}
/* back page, scoped by the marker span in the lifestyle title */
.sheet.back:has(.flv-back) .life .disc2{width:0.74in;height:0.74in}
.sheet.back:has(.flv-back) .life .disc2 svg{width:0.44in!important;height:0.44in!important}
.sheet.back:has(.flv-back) .band h2{margin-bottom:0.07in}
.sheet.back:has(.flv-back) .rhythm{grid-template-columns:1fr 1fr .5fr}
"""

# ============================================================== back page
# Lifestyle: guideline steps [EASL24][AASLD23], plus the protocol's gut-liver angle [MAYFIELD26] (gut barrier,
# endotoxins; UltraBiotic Prebiotic on the fatty-liver list, Akkermansia in Asher's 2024 launch blast).
LIFE = [
    # [EASL24]: "improving diet quality (similar to the Mediterranean dietary pattern), limiting the consumption of
    # ultra-processed food (rich in sugars and saturated fat) and avoiding sugar-sweetened beverages"; [AASLD23]:
    # "dietary sugars (eg, fructose, sucrose, and glucose), drive the formation and accumulation of intrahepatic fat"
    ("plate", "Eat Mediterranean",
     "Vegetables, beans, olive oil, nuts and fish. Skip sugary drinks and sweets: sugar easily turns into liver fat."),
    # [EASL24]: weight loss "should aim at a sustained reduction of >=5% to reduce liver fat, 7-10% to improve
    # liver inflammation and >=10% to improve fibrosis"
    ("scale", "Lose 7 to 10 percent",
     "5 percent of your weight cuts liver fat; 7 to 10 percent calms inflammation; 10 or more eases scarring."),
    # [EASL24]/[AASLD23]: ">150 min/week of moderate ... physical activity"; 2 strength days [HHS18];
    # 10-minute walks after meals lowered after-meal glucose more than one 30-minute walk [REYNOLDS16]
    ("walk", "Move every day",
     "150 minutes a week of brisk walking plus 2 strength days. A 10-minute walk after meals blunts the sugar spike."),
    # gut barrier and endotoxins [MAYFIELD26]; plant polyphenols and fiber as Akkermansia boosters [MAYFIELD24];
    # [AASLD23]: gut-microbiome products "may also contribute"
    ("gut", "Feed your gut",
     "Fiber and colorful plants feed helpful gut bacteria, like Akkermansia, that help keep the gut lining strong."),
    # [EASL24]: people with steatotic liver disease "should be discouraged from consuming alcohol"; "All alcohol
    # consumption should be stopped completely and permanently in individuals with advanced fibrosis or cirrhosis"
    ("glass", "Go easy on alcohol",
     "It did not cause this, but alcohol adds to the liver's load. Less is better; none at all if there is scarring."),
]

COLS = [
    # [MAYFIELD26]; label [LABELS] ND1130 via products.d (fl_berberine).  The first driver on the front is insulin
    # resistance, and berberine is the competitor's first nutrient, so this is the one to start with.
    {"p": "fl_berberine", "need": "Steady sugar and fat", "needsub": "berberine (as dihydroberberine)", "start": True,
     "bullets": ["Supports healthy glucose metabolism", "Supports lipid levels already in a normal range"],
     "dose": "dose_from_db"},
    # NutriDyn science-team lipotropic; 400 mg artichoke + tangerine peel = the competitor's bergamot + artichoke
    {"p": "fl_lipo_flow", "need": "Help the liver process fat", "needsub": "artichoke, citrus peel, inositol",
     "bullets": ["Supports healthy fat metabolism in the liver", "Supports healthy bile flow"], "dose": "dose_from_db"},
    # [MAYFIELD26]; antioxidant liver-cell support, the stand-in for the competitor's aged black garlic.
    # Claims stay structure/function: [AASLD23] calls silymarin's effect in NASH "inconclusive".
    {"p": "fl_milk_thistle", "need": "Protect liver cells", "needsub": "milk thistle (silymarin), NAC",
     "bullets": ["Antioxidant support for healthy liver function", "Supports the liver's natural detox processes"],
     "dose": "dose_from_db"},
    # [MAYFIELD26]; alpha lipoic acid (75 mg + 45 mg R-lipoic) = the competitor's ALA
    {"p": "fl_mito", "need": "Help cells make energy", "needsub": "alpha lipoic acid, CoQ10, NAC",
     "bullets": ["Supports energy production in cells", "Promotes healthy antioxidant status"], "dose": "dose_from_db"},
]

# Medicine-and-nutrient checks for this page's own products.  Pharmacists check interactions and depletions;
# providers order labs and adjust doses.
#  - berberine lowers blood sugar [ZHANG08], so it adds to diabetes medicines; it slowed CYP2D6, 2C9 and 3A4 in
#    people [GUO12]; Berberine Pro label: "If you are ... taking medication, consult your healthcare practitioner"
#  - Mito Recharge: 250 mcg vitamin K1 per 3 capsules [LABELS ND812]; vitamin K works against warfarin and intake
#    should stay steady [ODSK]
#  - statins are safe "across the disease spectrum" [AASLD23] and lower plasma CoQ10 [BANACH15]; Mito Recharge has
#    100 mg CoQ10 and 100 mg EGCG from green tea extract [LABELS ND812]; take green tea extract with food, stop if
#    dark urine or yellow skin [USP20]
RX = {
    "pharmacy": [
        "<b>Diabetes medicines:</b> Berberine Pro adds to their sugar-lowering effect, and it can slow the liver "
        "enzymes that clear some drugs (CYP2D6, 2C9, 3A4), so {who} checks your other medicines.",
        "<b>Warfarin:</b> Mito Recharge has 250 mcg vitamin K1, which works against it. Take it the same way every "
        "day, and tell {who} before you start.",
        "<b>Statins</b> are safe with fatty liver but lower CoQ10; Mito Recharge has 100 mg. It has green tea "
        "extract: take it with food. Dark urine or yellow skin? Stop it and call your doctor.",
    ],
    "practitioner": [
        "<b>Diabetes medicines:</b> Berberine Pro adds to their sugar-lowering effect, so {who} may check your "
        "blood sugar more often and adjust doses.",
        "<b>Warfarin:</b> Mito Recharge has 250 mcg vitamin K1, which works against it. Keep the dose steady; "
        "{who} may recheck your INR after you start.",
        "<b>Statins</b> are safe with fatty liver but lower CoQ10; Mito Recharge has 100 mg. It has green tea "
        "extract: take it with food. Dark urine or yellow skin? Stop it and call {who}.",
    ],
}

SHEET = {
    "slug": "fatty-liver", "code": "ND-CM-201", "theme": "metab", "series": "Metabolic Health Series",
    "order": 4,
    "title": "Fatty Liver Disease", "sub": "MASLD, the condition formerly called NAFLD",
    # Renamed MASLD in June 2023 [DELPHI23].  "About 1 in 3 adults": US 31.9% [NHANES25], global 30%,
    # 38% in 2016-2019 [YOUNOSSI23] (AASLD 2023 gives 25-30% [AASLD23]).  Usually silent [AASLD23].
    # "Most common liver condition": "MASLD has become the most common chronic liver disease" [EASL24].
    # Often reversible: "weight loss of 3%-5% improves steatosis ... (>10%) ... NASH and fibrosis" [AASLD23].
    "intro": ("Fatty liver disease means extra fat is stored inside liver cells, and it is <b>not caused by heavy drinking</b>. "
              "In 2023, liver specialists renamed it <b>MASLD</b> (metabolic dysfunction-associated steatotic liver disease) "
              "because it goes hand in hand with insulin resistance, belly fat, high triglycerides and high blood pressure. "
              "It is the most common liver condition in the world, affecting about <b>1 in 3 adults</b>, and most people "
              "feel nothing. Caught early, it is often reversible."),
    "front": front,
    "css": CSS,
    "back": {
        # the span marks this sheet's back page for the scoped CSS (.sheet.back:has(.flv-back))
        "life_title": 'Lifestyle Recommendations<span class="flv-back"></span>', "style": "circle",
        "life": LIFE,
        "cols": COLS,
        "rx": RX,
    },
}
