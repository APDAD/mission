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
Art-director pass (front only; SHEET["back"] is frozen for the products pass): immune cells
never stack (a cell is skipped when no free spot exists), scar bands are drawn edges-then-fills
so they merge into one septum, every arc end and T-bar stops clear of the white ring, the band
holds the arcs and their labels, the livers sit bottom-aligned 4 units above the band, the key
reads "KEY TO THE CLOSE-UPS" with a "Zoomed in" tag on the first beam, the sugar icon's slash is
hidden, all three check cards end in two sourced dots, and the pharmacy edition says the doctor
orders the checks.
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
              2024;81:492-542. doi:10.1016/j.jhep.2024.04.031 (spectrum: steatosis, MASH, fibrosis,
              cirrhosis; stepwise FIB-4 then transient elastography)
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
# contribute to the NASH phenotype" [AASLD23]; ongoing inflammation drives fibrosis).
DRIVERS = [["Insulin resistance", "sends extra fat", "into liver cells"],
           ["Stressed cells and", "gut-bacteria waste", "spark inflammation"],
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


def _cubic_d(p0, p1, p2, p3, t):
    m = 1 - t
    return tuple(3 * m * m * (p1[k] - p0[k]) + 6 * m * t * (p2[k] - p1[k]) + 3 * t * t * (p3[k] - p2[k]) for k in (0, 1))


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
LIVER_FILL = [("#C55B47", "#8C2E24"), ("#EEC468", "#C88E2E"), ("#DE8457", "#A8432A"), ("#A99689", "#6C5D54")]
LIVER_EDGE = ["#6E241C", "#94661D", "#84331F", "#51463F"]


def _liver_texture(stage):
    if stage == 1:   # pale fat mottling
        return "".join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="#FFF2C6" opacity=".55"/>'
                       for x, y, r in [(30, 30, 9), (57, 20, 6.5), (50, 45, 8), (84, 27, 6), (112, 21, 5), (24, 55, 6), (73, 38, 5)])
    if stage == 2:   # red, angry patches with a little fat left
        return ("".join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="#9E2A1C" opacity=".3"/>'
                        for x, y, r in [(34, 32, 10), (63, 42, 9), (92, 25, 7), (118, 19, 5), (22, 52, 7)])
                + "".join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="#FFE3A6" opacity=".5"/>'
                          for x, y, r in [(52, 20, 5.5), (78, 32, 4.5), (40, 50, 4)]))
    if stage == 3:   # cirrhosis: a lumpy surface of uneven regrowth nodules
        rnd = random.Random(77)
        out = []
        for row in range(9):
            for col in range(15):
                x = col * 10.2 + (5.1 if row % 2 else 0) + rnd.uniform(-1.8, 1.8)
                y = 2 + row * 8.8 + rnd.uniform(-1.6, 1.6)
                r = rnd.uniform(3.6, 5.9)
                out.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r:.1f}" fill="rgba(255,255,255,.09)" '
                           f'stroke="rgba(48,36,30,.42)" stroke-width="1.1"/>'
                           f'<circle cx="{x - r * .3:.1f}" cy="{y - r * .32:.1f}" r="{r * .38:.1f}" fill="rgba(255,255,255,.16)"/>')
        return "".join(out)
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
def _hex(px, py, r):
    return " ".join(f"{px + r * math.cos(math.radians(a)):.1f},{py + r * math.sin(math.radians(a)):.1f}"
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


SCAR_FIBRE = "#B5AAA1"        # faint collagen strands along each scar band


def _ribbon(p, w, wobble=0.0, phase=0.0, n=48):
    """A band of width w (gently swelling and thinning by +-wobble) along the cubic p = (p0, p1, p2, p3).
    Returns the outline path and two fibre lines that run along it."""
    left, right, fib = [], [], ([], [])
    for i in range(n + 1):
        t = i / n
        x, y = _cubic(*p, t)
        dx, dy = _cubic_d(*p, t)
        m = math.hypot(dx, dy) or 1
        nx, ny = -dy / m, dx / m
        hw = w / 2 * (1 + wobble * math.sin(2 * math.pi * (1.3 * t + phase)))
        left.append((x + nx * hw, y + ny * hw))
        right.append((x - nx * hw, y - ny * hw))
        for k, f in enumerate((-0.42, 0.36)):
            fib[k].append((x + nx * hw * f, y + ny * hw * f))
    poly = lambda pts: "M" + " L".join(f"{a:.1f},{b:.1f}" for a, b in pts)
    return poly(left + right[::-1]) + "Z", [poly(f) for f in fib]


def _scar_network(bands):
    """Every band's dark edge first, then every pale fill, then the fibres, so where bands cross
    they merge into one continuous septum instead of one tube passing over another."""
    shapes = [_ribbon(p, w, wob, ph) for p, w, wob, ph in bands]
    return ("".join(f'<path d="{o}" fill="{SCAR_EDGE}" stroke="{SCAR_EDGE}" stroke-width="3" stroke-linejoin="round"/>'
                    for o, _ in shapes)
            + "".join(f'<path d="{o}" fill="{SCAR}"/>' for o, _ in shapes)
            + "".join(f'<path d="{f}" fill="none" stroke="{SCAR_FIBRE}" stroke-width=".8" stroke-linecap="round"/>'
                      for _, fs in shapes for f in fs))


def sw_scar():
    """Key swatch: a short band with the same edge, fill and fibres as the art (round ends, as it is not clipped)."""
    d = "M-11,2.5 C-5,-3.5 4,4 11,-2.5"
    return (f'<path d="{d}" fill="none" stroke="{SCAR_EDGE}" stroke-width="9" stroke-linecap="round"/>'
            f'<path d="{d}" fill="none" stroke="{SCAR}" stroke-width="6" stroke-linecap="round"/>'
            f'<path d="M-9.5,0.6 C-4.5,-4.3 3.5,2.2 9.5,-3.6" fill="none" stroke="{SCAR_FIBRE}" stroke-width=".8" stroke-linecap="round"/>'
            f'<path d="M-9.5,4.0 C-4.5,-0.6 4.5,5.6 9.5,0.6" fill="none" stroke="{SCAR_FIBRE}" stroke-width=".8" stroke-linecap="round"/>')


def tissue(cx, cy, r, stage):
    """Magnified liver tissue: a honeycomb of liver cells, then fat, immune cells, scar."""
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
    p_fat = {0: 0, 1: 0.66, 2: 0.5, 3: 0.2}[stage]
    for px, py in cells:
        out.append(f'<polygon points="{_hex(px, py, cr)}" fill="{CELL}" stroke="{CELL_EDGE}" stroke-width="1.6"/>')
        if rnd.random() < p_fat:
            big = rnd.uniform(6.6, 9.4) if stage < 3 else rnd.uniform(4.6, 6.8)
            fx, fy = px + rnd.uniform(-1, 1), py + rnd.uniform(-1, 1)
            out.append(sw_fat(big, fx, fy))
            a = rnd.uniform(0, 2 * math.pi)       # the nucleus is squeezed to the cell's edge
            nx, ny = px + 8.6 * math.cos(a), py + 8.6 * math.sin(a)
            out.append(f'<ellipse cx="{nx:.1f}" cy="{ny:.1f}" rx="2.7" ry="1.7" fill="{NUC}" '
                       f'transform="rotate({math.degrees(a) + 90:.0f} {nx:.1f} {ny:.1f})"/>')
        else:
            out.append(f'<circle cx="{px:.1f}" cy="{py:.1f}" r="3.6" fill="{NUC}"/>')
            if stage in (1, 2) and rnd.random() < 0.55:   # a few small droplets beside the nucleus
                a = rnd.uniform(0, 2 * math.pi)
                out.append(sw_fat(rnd.uniform(2.4, 3.4), px + 6.4 * math.cos(a), py + 6.4 * math.sin(a)))
    if stage == 3:   # bridging bands of scar tissue cut the field into nodules (ends run past the clip)
        o = lambda dx, dy: (cx + dx, cy + dy)
        out.append(_scar_network([
            ((o(-64, -22), o(-30, -42), o(8, -2), o(64, -24)), 7.4, 0.16, 0.0),
            ((o(-64, 24), o(-26, 8), o(16, 42), o(64, 20)), 7.4, 0.16, 0.37),
            ((o(-8, -64), o(-22, -26), o(18, 14), o(2, 64)), 7.4, 0.16, 0.71)]))
    if stage >= 2:   # immune cells gather in small clusters (inflammation)
        spots = ([(-22, -15, 4), (21, 12, 4), (3, -33, 3), (-11, 31, 3)] if stage == 2
                 else [(-24, -21, 2), (27, -12, 2), (-14, 22, 2)])
        placed = []
        for sx, sy, n in spots:
            for _ in range(n):
                for _try in range(60):
                    ix, iy = cx + sx + rnd.uniform(-13, 13), cy + sy + rnd.uniform(-11, 11)
                    # a free spot only: whole ring inside the circle, never on top of another ring
                    if (math.hypot(ix - cx, iy - cy) <= r - IMM_R - 2.9
                            and all(math.hypot(ix - qx, iy - qy) >= IMM_GAP for qx, qy in placed)):
                        placed.append((ix, iy))
                        out.append(sw_immune(IMM_R, ix, iy))
                        break                 # no free spot after 60 tries: skip this cell
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
    """LEAST SEVERE ====gradient arrow====> MOST SEVERE, across the top of the diagram."""
    fs, ls = 12.5, 0.8
    wl, wr = tw("LEAST SEVERE", fs, 800, ls), tw("MOST SEVERE", fs, 800, ls)
    m, gap = 14, 12
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


def _key(y):
    """KEY to everything drawn inside the magnified circles (same swatch code as the art)."""
    # (swatch, half-width of the swatch incl. stroke, label)
    items = [(sw_cell(), 9.5, "Liver cell"), (sw_fat(), 7, "Fat droplet"),
             (sw_immune(), 6, "Immune cell (inflammation)"), (sw_scar(), 16, "Scar tissue")]
    x0, x1, h = 8, W - 8, KEY_H
    title, fs, base = "KEY TO THE CLOSE-UPS", 11.5, y + h / 2 + 4.1
    tx = x0 + 14
    start = tx + tw(title, 10.5, 800, 1.2) + 24
    widths = [2 * hw + 7 + tw(lab, fs, 600) for _, hw, lab in items]
    gap = (x1 - 16 - start - sum(widths)) / (len(items) - 1)
    out = [f'<rect x="{x0}" y="{y}" width="{x1 - x0}" height="{h}" rx="8" fill="#FFFFFF" stroke="#D9D1CD" stroke-width="1.2"/>',
           T(tx, base - 0.2, title, 10.5, 800, INK, ls=1.2)]
    x = start
    for (sw, hw, lab), wd in zip(items, widths):
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
    """'Zoomed in' tag sitting inside the first zoom beam, so a reader knows the circles are
    close-ups of the liver.  Checked: the pill stays inside the beam (see the assert)."""
    lab, fs = "Zoomed in", 10.2
    w, h = tw(lab, fs, 700) + 9, 14.5
    assert w / 2 + 3 <= _cone_half(y), "zoom tag too wide for the beam"
    return (f'<rect x="{cx - w / 2:.1f}" y="{y - h / 2:.1f}" width="{w:.1f}" height="{h}" rx="{h / 2}" '
            'fill="#FFFFFF" stroke="#B9AFA9" stroke-width=".9"/>'
            + T(cx, y + 3.7, lab, fs, 700, INK2, "middle"))


def art_progression(t):
    defs = ['<defs>',
            f'<clipPath id="fl-lclip"><path d="{LIVER_D}"/></clipPath>',
            '<linearGradient id="fl-band" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#E7F0E1"/>'
            '<stop offset=".5" stop-color="#F6F0E4"/><stop offset="1" stop-color="#F8E0DB"/></linearGradient>']
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
    out.append(f'<path d="M16,{top} H696 L756,{mid} L696,{bot} H16 Q4,{bot} 4,{bot - 12} V{top + 12} Q4,{top} 16,{top} Z" '
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
RISKS = [  # icons kept from the first draft; each factor is named in [AASLD23]
    ("sugar", "Sugary drinks,<br>added sugar"),
    ("meter", "Insulin resistance<br>or diabetes"),            # T2DM: "the most impactful risk factor"
    ("waist", "Weight carried<br>at the belly"),
    ("heartpulse", "High blood<br>pressure"),
    ("tube", "High blood fats<br>(triglycerides)"),
    ("calendar", "PCOS (polycystic<br>ovary syndrome)"),       # 2- to 4-fold higher MASLD prevalence
    ("dna", "Family history<br>and genes"),                     # PNPLA3; relatives of NASH cirrhosis
    ("gut", "Gut imbalance<br>(dysbiosis)"),                    # [AASLD23]: products from the gut microbiome "may also contribute"
]

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
#  - serum aminotransferases "can be normal in patients with diabetes, NASH, and advanced hepatic fibrosis"
#  - "normal values provided by most laboratories are higher than what should be considered normal in
#    NAFLD, in which a true normal alanine aminotransferase (ALT) ranges from 29 to 33 U/L in men and
#    from 19 to 25 U/L in women" (an upper limit, hence "Healthy ALT limit" on the card)
#  - FIB-4 is "based upon age, ALT, AST, and platelet count"; low risk is "FIB-4 <1.3"
#  - FIB-4 >= 1.3 -> VCTE (eg, FibroScan) favoured as the secondary test in primary care; it measures
#    liver stiffness, and its CAP reading "provides a point-of-care semiquantitative assessment of
#    hepatic steatosis but does not accurately quantify" liver fat (hence "estimates")
#  - VCTE "LSM <8 kPa can be used to rule out advanced fibrosis"; intermediate or high risk on the
#    secondary test -> "referred to specialty care"
CHECKS = [
    ("vial", "Liver enzymes (ALT, AST)",
     "A routine blood test. High levels can mean the liver is irritated, but normal levels do not rule out "
     "fatty liver.",
     [(SEV[0], "Healthy ALT limit, women: 19 to 25 U/L"), (SEV[0], "Healthy ALT limit, men: 29 to 33 U/L")]),
    ("gauge", "FIB-4 score",
     "Worked out from your age and routine labs (ALT, AST, platelets) to estimate the risk of advanced scarring.",
     [(SEV[0], "Under 1.3: low risk"), (SEV[1], "1.3 or higher: step 3 is next")]),
    ("probe", "FibroScan (elastography)",
     "A no-needle scan that measures liver stiffness (scarring) and estimates liver fat. "
     "The next step if FIB-4 is 1.3 or higher.",
     [(SEV[0], "Under 8 kPa: low risk"), (SEV[1], "8 kPa or more: see a liver specialist")]),
]


def _ed(x, ed):
    return x.replace("{who}", ed["who"]).replace("{Who}", ed["Who"])


def risk_strip():
    cells = "".join(f'<div class="flv-rf"><span class="flv-disc">{icon(ic, "0.33in", sw=2.8)}</span>'
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
"""

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
    # BACK: unchanged from the first draft (a later pass revises the products).
    "back": {
        "life_title": "Lifestyle Recommendations", "style": "circle",
        "life": [("plate", "Eat Mediterranean", "Vegetables, lean protein, olive oil, nuts and fish. Cut sugary drinks, juice and refined carbs: they turn into liver fat fastest."),
                 ("scale", "Lose 7 to 10 percent", "Losing 7 to 10 percent of body weight is the change most tied to clearing liver fat and calming inflammation."),
                 ("walk", "Move every day", "150 minutes a week of brisk walking plus 2 strength days. A 10-minute walk after meals blunts the sugar spike."),
                 ("glass", "Go easy on alcohol", "Even though alcohol did not cause it, alcohol adds to the liver's load. Keep it minimal or skip it.")],
        "cols": [
            {"p": "berberine", "need": "Steady sugar and fat", "needsub": "berberine", "start": True,
             "bullets": ["Supports healthy glucose metabolism", "Supports healthy lipid levels already in a normal range"], "dose": "dose_from_db"},
            {"p": "lipo_flow", "need": "Help the liver process fat", "needsub": "lipotropic nutrients",
             "bullets": ["Supports normal fat metabolism in the liver", "Supports healthy bile flow"], "dose": "dose_from_db"},
            {"p": "omega_1000", "need": "Balance fats", "needsub": "omega-3 fatty acids, EPA and DHA",
             "bullets": ["Supports healthy triglyceride levels", "Supports a healthy inflammatory response"], "dose": "dose_from_db"},
            {"p": "mito", "need": "Protect cells", "needsub": "alpha lipoic acid, NAC, carnitine",
             "bullets": ["Antioxidants that work in water and fat", "Supports cellular energy"], "dose": "dose_from_db"},
        ],
        "rx": ["<b>Statins:</b> often used alongside. They can lower CoQ10. Ask whether CoQ10 fits.",
               "<b>Metformin</b> long term can lower B12. Ask for a B12 check once a year.",
               "<b>Acetaminophen:</b> stay within label limits and never combine it with alcohol."],
    },
}
