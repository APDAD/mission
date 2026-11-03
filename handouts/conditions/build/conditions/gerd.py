"""Acid Reflux and GERD (ND-GI-102).  Self-contained sheet module: front copy,
front art, front builder and back data all live here.  Shared helpers come
from svgkit / kit; nothing is imported from sheets.py or art.py any more.

Front page, top to bottom:
  intro (SHEET["intro"]) -> anatomy diagram with a zoom on the open LES valve
  -> KEY row -> how it can feel + get-care box -> common-trigger picture
  row -> acid-blocker nutrient strip -> FDA footnote.

Art-director pass (2026-11-03), front only (SHEET["back"] is owned by the
back-page pass and is left exactly as it was):
  * one continuous outline from the esophagus through the stomach, a tapered
    pyloric canal, a pylorus ring the height of the duodenum and the duodenum
    itself (smooth cross-shading, no stripes);
  * esophagus starts 4 units below the SVG edge under a fully opaque fade, so
    the PDF prints no hard cap line;
  * diaphragm drawn as muscle (diagonal fibres, no dashed line), ending before
    the zoom, and lifted clear of the dashed source ring (the ring now holds
    only the LES, which is what the close-up shows);
  * close-up: the channel at the LES is open wall to wall (+-22.5), the teal
    ring halves are thinner and sit inside the wall, no droplet is sliced;
  * reflux arrow and droplets moved into open lumen; "Stomach" now points into
    the stomach chamber, not at the wall band under the esophagus;
  * KEY names all four symbols; text fixes from the review (FDA wording, taper
    advice, alarm list), coin labels spaced, footer at 7 pt.

Sources for every number and claim on the front (also tagged inline):
  [ACG22]  Katz PO et al. ACG Clinical Guideline for the Diagnosis and
           Management of GERD. Am J Gastroenterol 2022;117:27-56.
           doi:10.14309/ajg.0000000000001538 (trigger foods; alcohol, smoking,
           chocolate, peppermint and fatty food lower LES pressure; meals 2-3 h
           before bed; alarm symptoms; chest pain needs a heart check first;
           hoarseness, throat clearing, cough, dental erosions).
  [ES14]   El-Serag HB et al. Update on the epidemiology of GERD: a systematic
           review. Gut 2014;63:871-80. doi:10.1136/gutjnl-2012-304269
           (prevalence 18.1-27.8% in North America; NIDDK states about 20%).
  [FDA10]  FDA Drug Safety Communication, 2010-05-25 (updated 2011-03-23):
           possible increased risk of hip, wrist and spine fractures with PPIs;
           greatest risk with high doses or use for one year or longer.
  [FDA11]  FDA Drug Safety Communication, 2011-03-02: low magnesium can follow
           prolonged PPI use (in most cases longer than one year), any dose.
  [LAM13]  Lam JR et al. JAMA 2013;310:2435-42. doi:10.1001/jama.2013.280490
           (2+ years of PPIs or H2 blockers linked to B12 deficiency).
  [LAM17]  Lam JR et al. Gastroenterology 2017;152:821-9.
           doi:10.1053/j.gastro.2016.11.023 (2+ years linked to iron deficiency).
  [OC05]   O'Connell MB et al. Am J Med 2005;118:778-81.
           doi:10.1016/j.amjmed.2005.02.007 (omeprazole cut calcium carbonate
           absorption).
  [FA11]   Farrell CP et al. Gastroenterology Res 2011;4:243-51.
           doi:10.4021/gr379w (long-term PPI users absorbed less zinc; small study).
  [REB09]  Reimer C et al. Gastroenterology 2009;137:80-7.
           doi:10.1053/j.gastro.2009.03.058 (acid rebound after stopping 8 weeks
           of PPI), the reason for "do not stop suddenly".
"""
import math

from svgkit import T, svg
from kit import ICONS

# ----------------------------------------------------------------- palette
WALL_HI, WALL_MID, WALL_LO = "#F8C3AF", "#EE9C84", "#D9765F"      # stomach / esophagus wall
LINING_TOP, LINING_BOT = "#CF5C53", "#B3423F"                     # stomach lining (cut open)
RUGA_HI, RUGA_LO = "#E3806F", "#A13A36"                           # gastric folds
CUT = "#F9D6C9"                                                   # cut face of the wall
ESO_LINING = "#FBE4DB"                                            # esophagus lining (zoom)
ACID_TOP, ACID_MID, ACID_BOT, ACID_EDGE = "#E1EA7C", "#BCCD3A", "#A2B52C", "#7C8F1E"
LES, LES_DARK, LES_HI = "#1E9A8E", "#0F6B63", "#7AD6CA"          # teal: the LES valve
REFLUX = "#D52F1E"                                                # red: reflux direction
DIA, DIA_EDGE, DIA_FIBRE = "#EDCFC2", "#C99F8F", "#D2A897"        # diaphragm muscle
PYL_EDGE = "#B9563F"                                              # pylorus ring edge
INK, INK_SOFT, LEAD = "#22292D", "#56626A", "#59646B"
DEEP = "#8E3110"

W, H = 735, 322          # diagram viewBox: 1 unit = 1 px at the 7.66 in content width
OX, OY = 215, 4          # anatomy origin inside the diagram
ZX, ZY, ZR = 606, 152, 108   # zoom circle (ZR in zoom units); 12 px clear of the right edge
ZS = 1.04                    # zoom scale: on the page the circle radius is ZR * ZS
SX, SY, SR = 100, 102, 25    # zoom source ring (local coords, centred on the LES)
TOP = 0                      # local y where the esophagus starts: SVG y 4, under the opaque fade


# ------------------------------------------------------------- geometry helpers
def _bez(s, t):
    (x0, y0), (x1, y1), (x2, y2), (x3, y3) = s
    u = 1 - t
    return (u * u * u * x0 + 3 * u * u * t * x1 + 3 * u * t * t * x2 + t * t * t * x3,
            u * u * u * y0 + 3 * u * u * t * y1 + 3 * u * t * t * y2 + t * t * t * y3)


def _bez_d(s, t):
    (x0, y0), (x1, y1), (x2, y2), (x3, y3) = s
    u = 1 - t
    return (3 * u * u * (x1 - x0) + 6 * u * t * (x2 - x1) + 3 * t * t * (x3 - x2),
            3 * u * u * (y1 - y0) + 6 * u * t * (y2 - y1) + 3 * t * t * (y3 - y2))


def _sample(segs, step=1.5):
    """(x, y, tx, ty) along a chain of cubic segments, about `step` units apart."""
    out = []
    for i, s in enumerate(segs):
        n = max(4, int(sum(math.dist(_bez(s, k / 24), _bez(s, (k + 1) / 24)) for k in range(24)) / step))
        for k in range(0 if i == 0 else 1, n + 1):
            x, y = _bez(s, k / n)
            dx, dy = _bez_d(s, k / n)
            m = math.hypot(dx, dy)
            out.append((x, y, dx / m, dy / m))
    return out


def _pl(pts):
    return " ".join(f"L{x:.1f},{y:.1f}" for x, y in pts)


def _cubic(segs):
    return "M%g,%g " % segs[0][0] + " ".join("C%g,%g %g,%g %g,%g" % (*a, *b, *c) for _, a, b, c in segs)


# ------------------------------------------------------------- anatomy (local coords)
# Front view.  The esophagus comes down a little left of the stomach's middle and
# enters at the cardia; the fundus domes up beside it (the angle of His); the body
# hangs down the right; the antrum hooks left and tapers into a short pyloric canal.
# The pylorus (a ring of muscle the height of the duodenum) closes it off, and the
# duodenum (first part of the small intestine) carries on left and turns down.
ESO_L, ESO_R = 83, 117
_LESSER = ("C82,150 98,196 118,222 C123,229 121,235 111,236 "            # lesser curvature + angular notch
           "C86,236 62,229.5 48,229.5")                                  # antrum roof tapers into the canal
_FLOOR = ("C62,256.5 98,312 141,313 C196,311 237,268 243,200 "         # antrum floor, greater curvature
          "C247,150 238,104 211,86 C188,71 151,70 130,83 "              # up the side, over the fundus
          "C123.2,87.2 118.5,91 117,97")                                # down into the angle of His (under the LES ring)
# centre line of the pyloric canal + duodenum; the tube is 2 * R_DUO tall all the way
DUO_SEGS = [((48, 243), (30, 243), (16, 241.6), (4, 243.2)),
            ((4, 243.2), (-12, 245.4), (-22, 259), (-21.5, 279)),
            ((-21.5, 279), (-21.2, 290), (-19, 298.5), (-16.5, 306))]
R_DUO = 13.5
_DP = _sample(DUO_SEGS)
_DTOP = [(x - R_DUO * ty, y + R_DUO * tx) for x, y, tx, ty in _DP]     # outer / upper edge
_DBOT = [(x + R_DUO * ty, y - R_DUO * tx) for x, y, tx, ty in _DP]     # inner / lower edge
_TUBE = _pl(_DTOP[1:]) + " " + _pl(_DBOT[::-1])                          # canal + duodenum, out and back
OUTLINE = f"M{ESO_L},{TOP} L{ESO_L},106 {_LESSER} {_TUBE} {_FLOOR} L{ESO_R},{TOP}"   # open at the top
SILH = OUTLINE + " Z"
# the cut-open stomach: opens into the tube under the LES, ends in a funnel at the canal
_FUNNEL = "C38,229.5 32,238 32,243 C32,248 38,256.5 48,256.5"         # window tip pointing into the canal
STOM = f"M83,95 L83,106 {_LESSER} {_FUNNEL} {_FLOOR} L117,95 Z"
# interior edges of the window (not on the outline): painted over in wall colour so the
# clipped lining cannot leave an anti-aliased seam there
WINDOW_SEAMS = f"M48,229.5 {_FUNNEL} M83,95 L117,95"
_I30 = next(i for i, p in enumerate(_DP) if p[0] <= 30)                 # duodenum shading starts here
DUO_POLY = "M" + _pl(_DTOP[_I30:])[1:] + " " + _pl(_DBOT[_I30:][::-1]) + " Z"
DUO_AXIS = "M" + _pl([(x, y) for x, y, _, _ in _DP[_I30:]])[1:]
ACID = ("M20,253 C52,245 80,259 112,251 C140,244 168,257 196,249 C214,244 232,250 260,246")
# Diaphragm: a dome over the fundus, crossing behind the esophagus above the LES
# (clear of the dashed source ring) and fading out before the zoom cone widens.
DIA_SEGS = [((30, 78.5), (58, 71.5), (82, 65.5), (104, 62.5)),
            ((104, 62.5), (134, 57), (166, 55), (196, 55.5)),
            ((196, 55.5), (222, 56), (240, 60.5), (254, 67.5))]
DIA_LINE = _cubic(DIA_SEGS)
DIA_W = 11
# Reflux path: rises out of the pool through open lumen (far clear of the angular
# notch), eases into the cardia and runs straight up the esophagus.
ARROW = "M170,262 C168,206 112.8,171.9 110,142 C108.5,126 102.5,112 101,100 L100,42"


def _diaphragm():
    """A band of muscle: edge, body, short diagonal fibres and a soft top highlight.
    No centre line.  Both ends fade out (gx-dia* gradients run x 30 -> 254)."""
    fib = []
    for x, y, tx, ty in _sample(DIA_SEGS, 4.2):
        nx, ny = -ty, tx
        h = DIA_W / 2 - 1.5
        fib.append(f"M{x - 2.4 * tx - h * nx:.1f},{y - 2.4 * ty - h * ny:.1f}"
                   f"L{x + 2.4 * tx + h * nx:.1f},{y + 2.4 * ty + h * ny:.1f}")
    # highlight 2.9 units toward the band's upper edge (the -normal side)
    hl = "".join(f"{'M' if i == 0 else 'L'}{x + 2.9 * ty:.1f},{y - 2.9 * tx:.1f}"
                 for i, (x, y, tx, ty) in enumerate(_sample(DIA_SEGS, 6)))
    return (f'<path d="{DIA_LINE}" stroke="url(#gx-diae)" stroke-width="{DIA_W + 2.4}" fill="none"/>'
            f'<path d="{DIA_LINE}" stroke="url(#gx-diaf)" stroke-width="{DIA_W}" fill="none"/>'
            f'<path d="{"".join(fib)}" stroke="url(#gx-diak)" stroke-width="1" fill="none" stroke-linecap="round" opacity=".8"/>'
            f'<path d="{hl}" stroke="url(#gx-diah)" stroke-width="1.6" fill="none" stroke-linecap="round" opacity=".38"/>')


def _mix(a, b, t):
    """Blend two #RRGGBB colours, t from 0 (a) to 1 (b)."""
    ra, rb = ([int(c[i:i + 2], 16) for i in (1, 3, 5)] for c in (a, b))
    return "#%02X%02X%02X" % tuple(round(x + (y - x) * t) for x, y in zip(ra, rb))


def _duodenum_shade():
    """One smooth cross-gradient along the curved duodenum (the curved-tube version
    of gx-cyl): 27 opaque strokes half a unit apart, so no band edge can show.
    Darker at both edges, highlight a little up and left of the axis."""
    edge, mid, hi = "#CC6650", "#E99079", "#F7BFAB"
    out = [f'<clipPath id="gx-duo"><path d="{DUO_POLY}"/></clipPath>',
           '<g clip-path="url(#gx-duo)" fill="none" stroke-linejoin="round">']
    n = 27
    for k in range(n):
        t = k / (n - 1)                              # 0 at the tube edge, 1 on the axis
        b = math.sin(t * math.pi / 2)
        col = _mix(edge, mid, b / .62) if b < .62 else _mix(mid, hi, (b - .62) / .38)
        w = 2 * R_DUO + 1 - k * (2 * R_DUO) / n
        out.append(f'<path d="{DUO_AXIS}" stroke="{col}" stroke-width="{w:.2f}" '
                   f'transform="translate({-1.5 * t:.2f},{-2 * t:.2f})"/>')
    out.append("</g>")
    return "".join(out)


def _pylorus():
    """The pylorus: a thickened ring of muscle exactly as tall as the tube."""
    x, y, tx, ty = min(_DP, key=lambda p: abs(p[0] - 26))
    a = math.degrees(math.atan2(ty, tx))
    return (f'<g clip-path="url(#gx-silh)"><ellipse cx="{x:.1f}" cy="{y:.1f}" rx="4.9" ry="{R_DUO + 3}" '
            f'transform="rotate({a:.1f} {x:.1f} {y:.1f})" fill="url(#gx-pyl)" stroke="{PYL_EDGE}" stroke-width="1.1"/></g>')


def _duo_end():
    """Cut end of the duodenum: the small intestine carries on from here."""
    x, y, tx, ty = _DP[-1]
    a = math.degrees(math.atan2(tx, -ty))
    return (f'<ellipse cx="{x:.1f}" cy="{y:.1f}" rx="{R_DUO - 0.6}" ry="4.4" transform="rotate({a:.1f} {x:.1f} {y:.1f})" '
            f'fill="{LINING_BOT}" stroke="{WALL_LO}" stroke-width="2.2"/>')


def _rugae():
    # gastric folds fan down the body; the strip between the lesser curvature and the
    # arrow stays plain so the "Stomach" leader dot and the droplets sit on clear lining
    folds = ["M152,100 C198,106 226,150 224,214", "M136,120 C178,128 204,168 202,240",
             "M126,136 C160,148 186,182 189,228", "M184,90 C214,98 234,124 238,160"]
    out = []
    for f in folds:
        out.append(f'<path d="{f}" stroke="{RUGA_LO}" stroke-width="3.2" fill="none" stroke-linecap="round" '
                   'opacity=".5" transform="translate(2.2,2.2)"/>')
        out.append(f'<path d="{f}" stroke="{RUGA_HI}" stroke-width="2.6" fill="none" stroke-linecap="round" opacity=".9"/>')
    return "".join(out)


def _acid_pool():
    bubbles = [(150, 272, 3.2), (182, 284, 2.4), (122, 290, 2.8), (204, 266, 2.2), (92, 278, 2.4), (165, 300, 2.6)]
    out = [f'<path d="{ACID} L260,330 L20,330 Z" fill="url(#gx-acid)"/>',
           f'<path d="{ACID}" stroke="#F3F7C2" stroke-width="2.2" fill="none" opacity=".9"/>']
    out += [f'<circle cx="{x}" cy="{y}" r="{r}" fill="#EEF3A6" opacity=".8"/>' for x, y, r in bubbles]
    return "".join(out)


# Droplets splashing off the pool where the arrow leaves it and rising beside it, all
# in open lumen: at least 8 units clear of the arrow's white halo and of the cut wall.
DROPS = [(150, 242, 3.0), (188, 239, 3.8), (178, 221, 2.8), (167, 197, 3.3), (152, 171, 2.6)]


def _drops():
    return "".join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{ACID_MID}" stroke="{ACID_EDGE}" stroke-width=".9"/>'
                   for x, y, r in DROPS)


def _les_hoop(part):
    """The LES as a teal ring of muscle hugging the bottom of the esophagus.
    part='back' is drawn under the tube, 'front' over it."""
    rx, ry = 20.5, 6.2
    x0, x1 = SX - rx, SX + rx
    if part == "back":
        return (f'<path d="M{x0},{SY} A{rx},{ry} 0 0 1 {x1},{SY}" stroke="{LES_DARK}" stroke-width="8.4" fill="none"/>'
                f'<path d="M{x0},{SY} A{rx},{ry} 0 0 1 {x1},{SY}" stroke="{LES}" stroke-width="6" fill="none"/>')
    return (f'<path d="M{x0},{SY} A{rx},{ry} 0 0 0 {x1},{SY}" stroke="{LES_DARK}" stroke-width="9" fill="none" stroke-linecap="round"/>'
            f'<path d="M{x0},{SY} A{rx},{ry} 0 0 0 {x1},{SY}" stroke="url(#gx-les)" stroke-width="6.4" fill="none" stroke-linecap="round"/>'
            f'<path d="M{x0 + 4},{SY + 1.2} A{rx - 4},{ry - 1.6} 0 0 0 {x1 - 4},{SY + 1.2}" stroke="{LES_HI}" stroke-width="1.5" '
            'fill="none" stroke-linecap="round" opacity=".9"/>')


def _arrow(d, w=5.5, halo=True):
    """Red reflux arrow; the white halo keeps it readable on any tissue."""
    out = ""
    if halo:
        out = (f'<path d="{d}" stroke="#FFFFFF" stroke-width="{w + 4.5}" fill="none" stroke-linecap="round" '
               'stroke-linejoin="round" marker-end="url(#gx-arrh)" opacity=".95"/>')
    return out + (f'<path d="{d}" stroke="{REFLUX}" stroke-width="{w}" fill="none" stroke-linecap="round" '
                  'stroke-linejoin="round" marker-end="url(#gx-arr)"/>')


def _defs():
    fade = (lambda k, c, x0, x1: f'<linearGradient id="gx-dia{k}" gradientUnits="userSpaceOnUse" x1="{x0}" y1="0" x2="{x1}" y2="0">'
            f'<stop offset="0" stop-color="{c}" stop-opacity="0"/><stop offset=".14" stop-color="{c}"/>'
            f'<stop offset=".86" stop-color="{c}"/><stop offset="1" stop-color="{c}" stop-opacity="0"/></linearGradient>')
    return ("<defs>"
            # one radial gradient in user space so the silhouette and the wall rim match exactly
            '<radialGradient id="gx-wall" gradientUnits="userSpaceOnUse" cx="120" cy="120" r="230">'
            f'<stop offset="0" stop-color="{WALL_HI}"/><stop offset=".55" stop-color="{WALL_MID}"/>'
            f'<stop offset="1" stop-color="{WALL_LO}"/></radialGradient>'
            '<linearGradient id="gx-lining" gradientUnits="userSpaceOnUse" x1="0" y1="100" x2="0" y2="315">'
            f'<stop offset="0" stop-color="{LINING_TOP}"/><stop offset="1" stop-color="{LINING_BOT}"/></linearGradient>'
            '<linearGradient id="gx-acid" x1="0" y1="0" x2="0" y2="1">'
            f'<stop offset="0" stop-color="{ACID_TOP}"/><stop offset=".35" stop-color="{ACID_MID}"/>'
            f'<stop offset="1" stop-color="{ACID_BOT}"/></linearGradient>'
            # cylinder shading laid over the outside of the esophagus
            '<linearGradient id="gx-cyl" x1="0" y1="0" x2="1" y2="0">'
            '<stop offset="0" stop-color="#7A2A1A" stop-opacity=".16"/>'
            '<stop offset=".32" stop-color="#FFFFFF" stop-opacity=".42"/>'
            '<stop offset=".6" stop-color="#FFFFFF" stop-opacity="0"/>'
            '<stop offset="1" stop-color="#7A2A1A" stop-opacity=".22"/></linearGradient>'
            # top fade: fully opaque from above the SVG edge to y 8 (the tube starts at y 4), then clear by y 30
            '<linearGradient id="gx-topfade" gradientUnits="userSpaceOnUse" x1="0" y1="-6" x2="0" y2="30">'
            '<stop offset="0" stop-color="#FFFFFF" stop-opacity="1"/><stop offset=".39" stop-color="#FFFFFF" stop-opacity="1"/>'
            '<stop offset="1" stop-color="#FFFFFF" stop-opacity="0"/></linearGradient>'
            '<radialGradient id="gx-zbg" cx=".5" cy=".4" r=".62">'
            '<stop offset="0" stop-color="#FFF8F4"/><stop offset="1" stop-color="#FBE6DC"/></radialGradient>'
            '<linearGradient id="gx-les" x1="0" y1="0" x2="1" y2="0">'
            f'<stop offset="0" stop-color="{LES_DARK}"/><stop offset=".45" stop-color="{LES}"/>'
            f'<stop offset="1" stop-color="{LES_DARK}"/></linearGradient>'
            '<radialGradient id="gx-lesz" cx=".5" cy=".45" r=".6">'
            f'<stop offset="0" stop-color="#2DB3A5"/><stop offset=".7" stop-color="{LES}"/>'
            f'<stop offset="1" stop-color="{LES_DARK}"/></radialGradient>'
            '<linearGradient id="gx-pyl" x1="0" y1="0" x2="1" y2="0">'
            '<stop offset="0" stop-color="#C9644E"/><stop offset=".42" stop-color="#EE9C84"/>'
            '<stop offset=".62" stop-color="#E58A72"/><stop offset="1" stop-color="#C25C46"/></linearGradient>'
            + fade("e", DIA_EDGE, 30, 254) + fade("f", DIA, 30, 254) + fade("k", DIA_FIBRE, 30, 254)
            + fade("h", "#FFFFFF", 30, 254)
            + '<marker id="gx-arr" viewBox="0 0 10 10" refX="5.2" refY="5" markerWidth="3.1" markerHeight="3.1" '
            f'orient="auto-start-reverse" markerUnits="strokeWidth"><path d="M0,0 L10,5 L0,10 z" fill="{REFLUX}"/></marker>'
            '<marker id="gx-arrh" viewBox="0 0 10 10" refX="5.2" refY="5" markerWidth="3.1" markerHeight="3.1" '
            'orient="auto-start-reverse" markerUnits="strokeWidth"><path d="M0,0 L10,5 L0,10 z" fill="#FFFFFF"/></marker>'
            "</defs>")


def _anatomy():
    return "".join([
        f'<g transform="translate({OX},{OY})">', _diaphragm(), _les_hoop("back"),
        f'<clipPath id="gx-silh"><path d="{SILH}"/></clipPath>',
        f'<path d="{SILH}" fill="url(#gx-wall)"/>',
        _duodenum_shade(),
        f'<clipPath id="gx-stom"><path d="{STOM}"/></clipPath>',
        '<g clip-path="url(#gx-stom)">',
        f'<path d="{STOM}" fill="url(#gx-lining)"/>', _rugae(), _acid_pool(),
        # wall rim: a stroke clipped to the outline gives an even 10-unit cut wall all round
        f'<path d="{STOM}" fill="none" stroke="{CUT}" stroke-width="23.5"/>',
        f'<path d="{STOM}" fill="none" stroke="url(#gx-wall)" stroke-width="20"/>',
        _drops(),
        "</g>",
        f'<path d="{WINDOW_SEAMS}" fill="none" stroke="url(#gx-wall)" stroke-width="2.4" clip-path="url(#gx-silh)"/>',
        _pylorus(),
        # cylinder shading on the esophagus, laid after the window so it runs unbroken down to the LES ring
        f'<rect x="{ESO_L}" y="{TOP}" width="{ESO_R - ESO_L}" height="{104 - TOP}" fill="url(#gx-cyl)"/>',
        # one continuous outline: esophagus, stomach, canal, pylorus and duodenum (open at the faded top)
        f'<path d="{OUTLINE}" fill="none" stroke="{WALL_LO}" stroke-width="1.6" stroke-linejoin="round"/>',
        _duo_end(), _arrow(ARROW), _les_hoop("front"),
        "</g>"])


# ------------------------------------------------------------------ zoom circle
# A slice through the junction, magnified about 3x.  The tube wall thickens into
# the LES (teal); below it the wall flares out into the stomach and rises on the
# right into the fundus (the same angle of His as the main view).  The ring is cut
# in half: its two cut faces sit inside the walls.  The valve is relaxed, so the
# channel stays open wall to wall (+-22.5) and acid surges up through it.
Z_SILH = ("M-46,-140 L-46,-72 C-46,-60 -54,-50 -54,-37 C-54,-24 -46,-12 -46,-2 "
          "C-46,22 -76,42 -140,54 L-140,140 L140,140 L140,-40 C112,-40 86,-28 68,-14 "
          "C60,-8 54,-3 50,0 C48,-6 46,-9 46,-14 C46,-24 54,-26 54,-37 C54,-50 46,-60 46,-72 L46,-140 Z")
Z_LUMEN = ("M-24,-140 L-24,-72 C-24,-60 -22.5,-50 -22.5,-37 C-22.5,-24 -24,-12 -24,-2 "
           "C-24,26 -60,52 -140,76 L-140,140 L140,140 L140,-20 C112,-18 92,-8 78,2 "
           "C66,11 54,16 42,16 C32,16 24,8 24,-2 C24,-12 22.5,-24 22.5,-37 C22.5,-50 24,-60 24,-72 L24,-140 Z")
Z_LES_L = "M-39,-72 C-52,-62 -53,-14 -40,-4 C-27,-12 -26,-62 -39,-72 Z"
Z_LES_R = "M39,-72 C52,-62 53,-14 40,-4 C27,-12 26,-62 39,-72 Z"
# The refluxed acid is one liquid body clipped to the lumen: the pool mounds up into
# the funnel, fills the open valve wall to wall and climbs the tube to a wavy crest.
Z_ACID = ("M-140,88 C-110,86 -84,80 -62,64 C-42,48 -30,20 -30,-12 L-30,-60 "
          "C-22,-70 -14,-58 -5,-68 C3,-77 12,-60 20,-68 C25,-73 29,-68 30,-64 "
          "L30,-12 C30,12 42,32 62,46 C84,60 110,68 140,68 L140,140 L-140,140 Z")
Z_CREST = ("M-30,-60 C-22,-70 -14,-58 -5,-68 C3,-77 12,-60 20,-68 C25,-73 29,-68 30,-64")
# droplets above the crest: every one at least 2 units inside the 22.5-unit channel
Z_DROPS = [(-14, -84, 3.4), (11, -90, 3.0), (-4, -98, 2.4), (15, -78, 2.4), (-17, -74, 2.0), (7, -96, 1.8)]


def _zoom_les(d, side, k):
    fibres = "".join(
        f'<path d="M{side * 14},{y} C{side * 26},{y - 4} {side * 40},{y - 4} {side * 56},{y}" stroke="{LES_HI}" '
        'stroke-width="1.3" fill="none" opacity=".55"/>' for y in (-62, -50, -38, -26, -14))
    return (f'<clipPath id="gx-zles{k}"><path d="{d}"/></clipPath>'
            f'<path d="{d}" fill="url(#gx-lesz)" stroke="{LES_DARK}" stroke-width="1.5"/>'
            f'<g clip-path="url(#gx-zles{k})">{fibres}</g>')


def _zoom():
    r = ZR - 4
    return "".join([
        f'<circle cx="{ZX + 1.5}" cy="{ZY + 2.5}" r="{ZR * ZS + 3}" fill="#5A2A1A" opacity=".08"/>',
        f'<g transform="translate({ZX},{ZY}) scale({ZS})">',
        f'<clipPath id="gx-zc"><circle r="{r}"/></clipPath>',
        f'<clipPath id="gx-zl"><path d="{Z_LUMEN}"/></clipPath>',
        '<g clip-path="url(#gx-zc)">',
        f'<rect x="-{ZR}" y="-{ZR}" width="{2 * ZR}" height="{2 * ZR}" fill="url(#gx-zbg)"/>',
        f'<path d="{Z_SILH}" fill="{WALL_MID}" stroke="{WALL_LO}" stroke-width="1.6" stroke-linejoin="round"/>',
        '<g clip-path="url(#gx-zl)">',
        f'<rect x="-140" y="-140" width="280" height="280" fill="{LINING_TOP}"/>',
        # pale esophagus lining above a soft wavy Z-line; deep-rose stomach lining below
        f'<path d="M-40,-140 L40,-140 L40,6 C30,2 22,10 12,6 C2,2 -6,10 -16,6 C-24,3 -32,8 -40,5 Z" fill="{ESO_LINING}"/>',
        '<path d="M-12,-140 V-86 M0,-140 V-92 M12,-140 V-86" stroke="#F2D3C8" stroke-width="1.5" stroke-linecap="round"/>',
        f'<path d="M-66,50 C-52,42 -44,32 -38,20 M-108,70 C-88,64 -72,56 -60,44 M70,22 C84,10 100,2 124,-2 '
        f'M66,36 C86,24 108,18 138,16 M92,48 C106,40 120,36 140,34" stroke="{RUGA_HI}" stroke-width="3" fill="none" '
        'stroke-linecap="round" opacity=".9"/>',
        # acid: the pool mounds up into the funnel and surges through the open valve
        f'<path d="{Z_ACID}" fill="url(#gx-acid)"/>',
        f'<path d="{Z_CREST}" stroke="#F6F9CF" stroke-width="2.6" fill="none" stroke-linecap="round"/>',
        "".join(f'<circle cx="{x}" cy="{y}" r="{rr}" fill="#EEF3A6" opacity=".85"/>' for x, y, rr in
                ((-10, 18, 2.6), (12, -2, 2.0), (-14, -30, 1.8), (14, -44, 2.4), (-30, 78, 2.4), (40, 76, 2.0), (86, 86, 2.6), (-70, 96, 2.2))),
        "".join(f'<circle cx="{x}" cy="{y}" r="{rr}" fill="{ACID_MID}" stroke="{ACID_EDGE}" stroke-width="1"/>' for x, y, rr in Z_DROPS),
        "</g>",
        # cut face of the walls, then the two cut faces of the LES ring inside the thickened wall
        f'<path d="{Z_LUMEN}" fill="none" stroke="{CUT}" stroke-width="3"/>',
        _zoom_les(Z_LES_L, -1, 0), _zoom_les(Z_LES_R, 1, 1),
        f'<path d="M1,44 C1,14 -1,-14 0,-40 L0,-78" stroke="#FFFFFF" stroke-width="7.4" fill="none" stroke-linecap="round" '
        'opacity=".75"/>',
        _arrow("M1,44 C1,14 -1,-14 0,-40 L0,-78", 4.4, halo=False),
        "</g>",
        f'<circle r="{r}" fill="none" stroke="#FFFFFF" stroke-width="7"/>',
        f'<circle r="{ZR}" fill="none" stroke="#D8C7BE" stroke-width="1.3"/>',
        "</g>"])


def _wedge():
    """Soft cone from the LES out to the zoom circle, drawn BEHIND the anatomy so
    no connector line ever crosses the art."""
    x1, y1, r1 = OX + SX, OY + SY, SR
    dx, dy = ZX - x1, ZY - y1
    d = math.hypot(dx, dy)
    base = math.atan2(dy, dx)
    R = ZR * ZS
    a = math.acos((r1 - R) / d)
    pts = []
    for s in (-1, 1):
        ang = base + s * a
        pts.append(((x1 + r1 * math.cos(ang), y1 + r1 * math.sin(ang)),
                    (ZX + R * math.cos(ang), ZY + R * math.sin(ang))))
    (p1u, p2u), (p1l, p2l) = pts
    poly = f"{p1u[0]:.1f},{p1u[1]:.1f} {p2u[0]:.1f},{p2u[1]:.1f} {p2l[0]:.1f},{p2l[1]:.1f} {p1l[0]:.1f},{p1l[1]:.1f}"
    return f'<polygon points="{poly}" fill="#F2E8E2"/>'


def _source_ring():
    cx, cy = OX + SX, OY + SY
    return (f'<circle cx="{cx}" cy="{cy}" r="{SR}" fill="none" stroke="#FFFFFF" stroke-width="3.2" opacity=".9"/>'
            f'<circle cx="{cx}" cy="{cy}" r="{SR}" fill="none" stroke="#6E787E" stroke-width="1.2" stroke-dasharray="4 3"/>')


# ------------------------------------------------------------------ labels
def _label(x, y, title, sub, tx, ty):
    """Right-aligned label ending at x (baseline y) with a leader to (tx, ty)."""
    out = [f'<path d="M{x + 6},{y - 4.5} L{tx},{ty}" stroke="{LEAD}" stroke-width="1.1" fill="none"/>',
           f'<circle cx="{tx}" cy="{ty}" r="2.4" fill="{INK}" stroke="#FFFFFF" stroke-width="1"/>',
           T(x, y, title, 13, 800, INK, "end")]
    if sub:
        out.append(T(x, y + 14, sub, 11, 500, INK_SOFT, "end"))
    return "".join(out)


def art_reflux():
    body = [_defs(), _wedge(), _anatomy(), _source_ring(),
            # fade the esophagus into the page at the top rather than chopping it off
            f'<rect x="{OX + ESO_L - 6}" y="-6" width="{ESO_R - ESO_L + 12}" height="36" fill="url(#gx-topfade)"/>',
            _zoom(),
            T(ZX, 21, "UP CLOSE AT THE VALVE", 10.5, 800, DEEP, "middle", ls=1.6),
            T(ZX, 290, "The relaxed valve stays open,", 13.5, 800, INK, "middle"),
            T(ZX, 307, "so acid splashes back up.", 13.5, 800, INK, "middle"),
            _label(168, 48, "Esophagus", "your food tube", OX + ESO_L - 1, OY + 36),
            _label(168, 90, "Diaphragm", "breathing muscle", OX + 64, OY + 70),
            _label(168, 140, "LES valve", "a ring of muscle", OX + SX - 21, OY + SY + 4),
            # the dot sits on the stomach lining inside the chamber, between the wall and the arrow
            _label(168, 205, "Stomach", None, OX + 126, OY + 197),
            _label(168, 284, "Small intestine", None, OX - 20, OY + 280)]
    return svg(W, H, "".join(body), "How acid reflux happens: the LES valve at the bottom of the esophagus relaxes and stomach acid splashes up")


def key_row():
    """KEY for the diagram, using the exact symbols drawn in the art."""
    def sw(inner, w=24):
        return f'<svg viewBox="{-w / 2} -12 {w} 24" width="{w}" height="24" aria-hidden="true">{inner}</svg>'
    acid = sw('<path d="M-11,1 C-7,-4 -3,4 1,0 C5,-4 8,0 11,-1 L11,10 L-11,10 Z" '
              f'fill="{ACID_MID}" stroke="{ACID_EDGE}" stroke-width=".9"/>'
              '<path d="M-11,1 C-7,-4 -3,4 1,0 C5,-4 8,0 11,-1" stroke="#F3F7C2" stroke-width="1.6" fill="none"/>'
              f'<circle cx="-3.5" cy="-6.5" r="2.4" fill="{ACID_MID}" stroke="{ACID_EDGE}" stroke-width=".8"/>'
              f'<circle cx="4" cy="-9.4" r="1.8" fill="{ACID_MID}" stroke="{ACID_EDGE}" stroke-width=".8"/>')
    ring = sw(f'<path d="M-10,1 A10,3.4 0 0 1 10,1" stroke="{LES_DARK}" stroke-width="4.6" fill="none"/>'
              f'<rect x="-6" y="-11" width="12" height="22" fill="{WALL_MID}"/>'
              f'<path d="M-10,1 A10,3.4 0 0 0 10,1" stroke="{LES_DARK}" stroke-width="5.4" fill="none" stroke-linecap="round"/>'
              f'<path d="M-10,1 A10,3.4 0 0 0 10,1" stroke="{LES}" stroke-width="3.4" fill="none" stroke-linecap="round"/>')
    halves = sw(f'<rect x="-10" y="-11" width="20" height="22" rx="2" fill="{WALL_MID}"/>'
                f'<rect x="-3.4" y="-11" width="6.8" height="22" fill="{ESO_LINING}"/>'
                f'<path d="M-6,-8 C-9,-5 -9,5 -6,8 C-4.4,5 -4.4,-5 -6,-8 Z" fill="{LES}" stroke="{LES_DARK}" stroke-width=".9"/>'
                f'<path d="M6,-8 C9,-5 9,5 6,8 C4.4,5 4.4,-5 6,-8 Z" fill="{LES}" stroke="{LES_DARK}" stroke-width=".9"/>', 20)
    arrow = sw(f'<path d="M0,10 V-3" stroke="{REFLUX}" stroke-width="3.6" stroke-linecap="round"/>'
               f'<path d="M-6,-1 L0,-10 L6,-1 Z" fill="{REFLUX}"/>')
    ring2 = sw('<circle r="8.6" fill="none" stroke="#FFFFFF" stroke-width="3"/>'
               '<circle r="8.6" fill="none" stroke="#6E787E" stroke-width="1.2" stroke-dasharray="3.4 2.4"/>')

    def item(swatches, name, gloss):
        return f'<span class="gx-ki">{swatches}<span><em>{name}</em><i>{gloss}</i></span></span>'
    return ('<div class="gx-key"><b>Key</b>'
            + item(acid, "Stomach acid", "the pool and drops")
            + item(ring + halves, "LES valve", "ring of muscle, cut in half up close")
            + item(arrow, "Reflux", "acid moving up")
            + item(ring2, "Dashed circle", "the spot shown up close") + "</div>")


# ------------------------------------------------------------- trigger picture row
# 64x64 line icons, stroked with currentColor (same grammar as kit.ICONS).
# Foods and habits named by [ACG22]; peppermint and alcohol also by NIDDK.
TRIGGERS = [
    ("Fried or fatty food",
     '<path d="M17 30h30l-4 25a3 3 0 0 1-3 2.6H24a3 3 0 0 1-3-2.6z"/><path d="M23 30l-2-17M29.5 30V10M36 30l1-18M42.5 30l3-15"/>'
     '<path d="M20 40h24"/>'),
    ("Spicy food",
     '<path d="M44 20c5 2 7 8 5 15-3 11-15 19-31 20-3 0-4-3-1-4 11-4 17-12 19-21 1-6 4-10 8-10z"/>'
     '<path d="M45 20c0-5 3-9 8-10"/><path d="M40 21c2-2 5-2 7 0"/>'),
    ("Chocolate",
     '<rect x="17" y="8" width="30" height="48" rx="3"/><path d="M17 20h30M17 32h30M32 8v24"/>'
     '<path d="M14 36h36v18a3 3 0 0 1-3 3H17a3 3 0 0 1-3-3z"/><path d="M14 36l6 5 6-5 6 5 6-5 6 5 6-5"/>'),
    ("Peppermint",
     '<circle cx="32" cy="32" r="13"/><path d="M32 32c0-6 4-11 10-12M32 32c6 0 11 4 12 10M32 32c0 6-4 11-10 12M32 32c-6 0-11-4-12-10"/>'
     '<path d="M19 32l-11-7v14zM45 32l11-7v14z"/>'),
    ("Coffee", ICONS["coffee"]),
    ("Alcohol",
     '<path d="M21 8h22c0 13-5 21-11 21S21 21 21 8z"/><path d="M22 16h20"/><path d="M32 29v20M23 55h18"/>'),
    ("Citrus and tomato",
     '<circle cx="40" cy="36" r="15"/><path d="M40 21l-5-5M40 21l5-5M40 21v-7M40 21l-8 1M40 21l8 1"/>'
     '<path d="M6 54a13 13 0 0 1 26 0z"/><path d="M19 54V43M19 54l-8-6M19 54l8-6"/>'),
    ("Fizzy drinks",
     '<path d="M19 20h26l-4 36a2 2 0 0 1-2 2H25a2 2 0 0 1-2-2z"/><path d="M36 20l6-13h7"/>'
     '<circle cx="28" cy="33" r="2"/><circle cx="35" cy="41" r="2.3"/><circle cx="28" cy="48" r="1.8"/><circle cx="36" cy="29" r="1.5"/>'),
    ("Big or late meals",
     '<circle cx="27" cy="38" r="18"/><circle cx="27" cy="38" r="9.5"/><path d="M53 8a9 9 0 1 0 7 14 7.5 7.5 0 1 1-7-14z"/>'),
    ("Smoking",
     '<rect x="7" y="38" width="42" height="9" rx="2"/><path d="M38 38v9"/><path d="M55 38v9"/>'
     '<path d="M53 31c-3-4 2-6 0-10s2-6 0-10"/><path d="M45 30c-2-3 2-5 0-8"/>'),
]


def _ic(body, size, color, sw=3):
    return (f'<svg class="gx-ic" viewBox="0 0 64 64" style="width:{size};height:{size};color:{color}" fill="none" '
            f'stroke="currentColor" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{body}</svg>')


def trigger_row(t):
    cells = "".join(f'<div class="gx-tr"><span class="gx-badge">{_ic(b, "0.33in", t["deep"], 3.1)}</span><span>{lab}</span></div>'
                    for lab, b in TRIGGERS)
    return (f'<div class="gx-trig"><div class="gx-h">Common triggers <i>They differ from person to person. '
            f'Notice which ones bother you.</i></div><div class="gx-trow">{cells}</div></div>')


# ----------------------------------------------------------- nutrient strip
NUTRIENTS = [("Mg", "Magnesium"),    # [FDA11]: low magnesium with prolonged PPI use
             ("B12", "Vitamin B12"),  # [LAM13]: PPIs and H2 blockers
             ("Ca", "Calcium"),       # [OC05]; [FDA10] fracture warning
             ("Fe", "Iron"),          # [LAM17]: PPIs and H2 blockers
             ("Zn", "Zinc")]          # [FA11]


def depletion_strip(t, ed):
    coins = "".join(f'<div class="gx-coin"><b>{s}</b><span>{n}</span></div>' for s, n in NUTRIENTS)
    # [FDA11] low magnesium: prolonged use, any dose.  [FDA10] fractures: mostly high doses or 1+ year.
    # [REB09] acid can rebound when a long-used PPI is stopped suddenly; an OTC 14-day course is not "months".
    return ('<div class="gx-strip"><div class="gx-meds"><div class="gx-h">About acid-blocking medicines</div>'
            '<p>PPIs (like omeprazole) and H2 blockers (like famotidine) help many people heal. But acid also helps you '
            'absorb nutrients. The FDA has warned about low magnesium with long-term PPI use, and about broken bones, '
            'mostly at high doses or after a year or more.<sup>1</sup> <b>Taken one for months? Do not stop suddenly:</b> '
            'ask {who} or your prescriber for a plan.</p></div>'
            f'<div class="gx-dep"><div class="gx-dephead">Long-term acid blockers can lower</div><div class="gx-coins">{coins}</div>'
            '<div class="gx-ask">Ask {who} if a nutrient check makes sense.</div></div></div>')


# ---------------------------------------------------------------- front page
FEEL = ["Burning behind the breastbone",          # [ACG22] heartburn, the most common symptom
        "A sour taste, or food coming up",        # [ACG22] regurgitation
        "Hoarse voice, throat clearing",          # [ACG22] extraesophageal symptoms
        "A dry cough that hangs on",              # [ACG22]
        "Upset stomach after meals",
        "Bad breath, worn tooth enamel"]          # [ACG22] dental erosions
ALARM = ["Food sticks, or it hurts to swallow",   # [ACG22] dysphagia is an alarm symptom
         "You throw up blood or coffee-ground bits",  # [ACG22] GI bleeding
         "Your stools are black or tarry",
         # [ACG22]: chest pain needs heart disease ruled out before anyone calls it reflux
         "<b>Chest pain: call 911.</b> It can be the heart."]
# [ACG22] weight loss is an alarm feature that needs a prompt work-up, not an emergency visit
SOON = "<b>See a doctor soon</b> if you lose weight without trying."


def front(t, ed):
    feel = "".join(f"<li>{x}</li>" for x in FEEL)
    alarm = "".join(f"<li>{x}</li>" for x in ALARM)
    return (f'<div class="gxf"><div class="gx-art">{art_reflux()}{key_row()}</div>'
            '<div class="gx-row">'
            f'<div class="gx-feel"><div class="gx-h">How it can feel</div><ul>{feel}</ul>'
            '<p class="gx-why"><b>Why treat it?</b> Left alone, acid can inflame, narrow or scar the esophagus.</p></div>'
            f'<div class="gx-alarm"><div class="gx-h">Get care right away if</div><ul>{alarm}</ul><p>{SOON}</p></div>'
            '</div>'
            f'{trigger_row(t)}{depletion_strip(t, ed)}'
            '<p class="gx-fn">1. U.S. FDA Drug Safety Communications on proton pump inhibitors (PPIs): possible fracture risk '
            '(2010); low magnesium with long-term use (2011).</p></div>')


CSS = r"""
.gxf{display:flex;flex-direction:column;gap:0.08in}
.gxf .gx-art>svg{display:block;width:100%;height:auto}
.gxf .gx-key{display:flex;align-items:center;justify-content:center;gap:0 15px;flex-wrap:nowrap;margin:3px auto 0;
  padding:3px 16px 3px 14px;border:1px solid #EAD9CF;border-radius:99px;background:#FFFBF8;width:max-content;max-width:100%}
.gxf .gx-key>b{font:800 7pt Inter,sans-serif;letter-spacing:.16em;text-transform:uppercase;color:var(--deep)}
.gxf .gx-ki{display:inline-flex;align-items:center;gap:5px}
.gxf .gx-ki>span{display:flex;flex-direction:column;line-height:1.14}
.gxf .gx-key em{font-style:normal;font-weight:700;font-size:8pt;color:#2B3236}
.gxf .gx-key i{font-style:normal;font-size:7.4pt;color:#56626A}
.gxf .gx-key svg{display:block;flex:none}
.gxf .gx-h{font:800 7.4pt Inter,sans-serif;letter-spacing:.14em;text-transform:uppercase;color:var(--c1);margin:0 0 3px}
.gxf .gx-h i{font:italic 500 7.6pt Inter,sans-serif;letter-spacing:0;text-transform:none;color:#56626A;margin-left:6px}
.gxf .gx-row{display:grid;grid-template-columns:1.22fr 1fr;gap:0.14in;align-items:stretch}
.gxf .gx-feel ul{margin:0;padding:0;list-style:none;columns:2;column-gap:0.14in}
.gxf .gx-feel li{position:relative;padding-left:12px;font-size:8.4pt;line-height:1.3;margin:0 0 3px;break-inside:avoid;color:#2B3236}
.gxf .gx-feel li::before{content:"";position:absolute;left:0;top:4px;width:6px;height:6px;border-radius:50%;background:var(--c2)}
.gxf .gx-why{margin:4px 0 0;font-size:8.4pt;line-height:1.32;color:#2B3236}
.gxf .gx-why b{color:var(--deep)}
.gxf .gx-alarm{border:1.6px solid #C0392B;border-radius:8px;background:#FDF1EF;padding:0.05in 0.12in 0.06in}
.gxf .gx-alarm .gx-h{color:#A5281E}
.gxf .gx-alarm ul{margin:0;padding:0 0 0 13px;font-size:8.3pt;line-height:1.3;color:#2B3236}
.gxf .gx-alarm li{margin:0}
.gxf .gx-alarm li::marker{color:#C0392B}
.gxf .gx-alarm p{margin:3px 0 0;padding-top:3px;border-top:1px dashed #E7B3AC;font-size:8.3pt;line-height:1.3;color:#2B3236}
.gxf .gx-alarm p b{color:#8E3110}
.gxf .gx-trow{display:grid;grid-template-columns:repeat(10,1fr);gap:0 0.04in}
.gxf .gx-tr{display:flex;flex-direction:column;align-items:center;text-align:center}
.gxf .gx-badge{width:0.5in;height:0.5in;border-radius:50%;background:var(--soft);display:flex;align-items:center;justify-content:center;
  box-shadow:inset 0 0 0 1.5px #F3D3BC}
.gxf .gx-tr>span:last-child{font-size:7.5pt;line-height:1.18;color:#2B3236;margin-top:3px;font-weight:600}
.gxf .gx-strip{display:grid;grid-template-columns:1.42fr 1fr;gap:0.14in;align-items:center;background:var(--soft);border-radius:10px;
  padding:0.07in 0.12in 0.07in 0.14in}
.gxf .gx-meds p{margin:0;font-size:8.2pt;line-height:1.34;color:#2B3236}
.gxf .gx-meds p b{color:var(--deep)}
.gxf .gx-meds sup{color:var(--c1);font-weight:700;font-size:7.2pt;line-height:0}
.gxf .gx-dep{background:#fff;border-radius:8px;padding:0.05in 0.09in 0.05in}
.gxf .gx-dephead{font:800 7.4pt Inter,sans-serif;letter-spacing:.12em;text-transform:uppercase;color:var(--deep);text-align:center;margin:0 0 5px}
.gxf .gx-coins{display:flex;justify-content:space-between;gap:0 10px}
.gxf .gx-coin{display:flex;flex-direction:column;align-items:center;flex:none;min-width:0.4in}
.gxf .gx-coin b{width:0.4in;height:0.4in;border-radius:50%;background:var(--c1);color:#fff;display:flex;align-items:center;justify-content:center;
  font:800 10pt Inter,sans-serif;box-shadow:0 0 0 2px #fff,0 0 0 3.2px #F0B89A}
.gxf .gx-coin span{font-size:7pt;font-weight:700;color:#2B3236;margin-top:3px;text-align:center;line-height:1.1;white-space:nowrap}
.gxf .gx-ask{font-size:7.6pt;color:#3F4A50;text-align:center;margin-top:3px}
.gxf .gx-fn{margin:0;font-size:7pt;color:#5E686F;line-height:1.3}
.gxf~.foot,.gxf~.foot .code{font-size:7pt}
"""

SHEET = {
    "slug": "gerd", "code": "ND-GI-102", "order": 2, "theme": "gerd", "series": "Gut Health Series",
    "title": "Acid Reflux and GERD", "sub": "Gastroesophageal reflux disease",
    # 1 in 5: [ES14] 18.1-27.8% in North America; NIDDK puts U.S. GERD at about 20%.
    # "opens when it should not, or does not close well": transient LES relaxations and a weak LES [ACG22].
    "intro": ("Reflux now and then is normal. When it happens often or harms the food tube, it is called <b>GERD</b>, "
              "and about <b>1 in 5 U.S. adults</b> has it. A ring of muscle, the <b>LES valve</b> (lower esophageal sphincter), "
              "sits where the food tube (the <b>esophagus</b>) meets the stomach. It opens to let food in, then shuts tight. "
              "In GERD it opens when it should not, or does not close well, so acid splashes up. The stomach has a coat "
              "that shields it from acid; the esophagus does not, so it burns (<b>heartburn</b>)."),
    "front": front,
    "css": CSS,
    # Back page: unchanged from the first draft (a later pass revises the products).
    "back": {
        "life_title": "Lifestyle Modifications", "style": "hex",
        "life": [("clock", "Close the kitchen early", "Finish eating 3 hours before you lie down."),
                 ("bed", "Raise the head", "Lift the head of your bed 6 to 8 inches."),
                 ("portion", "Smaller meals", "Eat slowly and stop before full."),
                 ("scale", "A healthy weight", "Even a few pounds lighter eases pressure on the valve."),
                 ("coffee", "Know your triggers", "Fried food, chocolate, mint, caffeine, alcohol, citrus, tomato, fizzy drinks."),
                 ("smoke", "Stop smoking", "Smoking relaxes the valve and slows healing.")],
        "cols": [
            {"p": "gi_integrity", "need": "Coat and soothe", "needsub": "DGL, aloe, slippery elm, marshmallow, glutamine", "start": True,
             "bullets": ["Sip it slowly so it coats your throat on the way down", "Zinc carnosine supports the stomach lining"],
             "dose": "1 scoop daily", "dosesub": "sip over 10 minutes"},
            {"p": "zinc_carnosine", "need": "Protect the stomach lining", "needsub": "zinc carnosine",
             "bullets": ["Supports the stomach's natural mucosal defenses", "Studied for gastric comfort"], "dose": "dose_from_db"},
            {"p": "ultrabiotic_dms", "need": "Balance the gut", "needsub": "probiotic + S. boulardii",
             "bullets": ["Seven friendly strains", "Supports comfortable digestion"], "dose": "1 capsule daily", "dosesub": "at bedtime"},
            {"p": "mag_glycinate", "need": "Refill magnesium", "needsub": "chelated magnesium",
             "bullets": ["Acid blockers can drain magnesium", "Chelated forms are gentle on the stomach"], "dose": "dose_from_db"},
            {"p": "methyl_b", "need": "Refill B12", "needsub": "active B vitamins",
             "bullets": ["Stomach acid is needed to absorb B12", "Methylated forms, ready to use"], "dose": "dose_from_db"},
        ],
        "rx": ["<b>PPIs and H2 blockers</b> can lower magnesium, B12, calcium and iron over time. Ask for levels once a year.",
               "<b>Take soothing powders 2 hours apart</b> from other medicines: coating herbs can slow their absorption.",
               "<b>Want to taper an acid blocker?</b> Plan it with your prescriber; stopping suddenly can bring a rebound."],
    },
}
