"""Acid Reflux and GERD (ND-GI-102).  Self-contained sheet module: front copy,
front art, front builder and back data all live here.  Shared helpers come
from svgkit / kit; nothing is imported from sheets.py or art.py any more.

Front page, top to bottom:
  intro (SHEET["intro"]) -> anatomy diagram with a zoom on the open LES valve
  -> KEY row -> how it can feel + get-care-now box -> common-trigger picture
  row -> acid-blocker nutrient strip -> FDA footnote.

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
  [FDA]    FDA Drug Safety Communications: PPIs and fractures (May 2010,
           updated Mar 2011); low magnesium with long-term PPI use (Mar 2011).
  [LAM13]  Lam JR et al. JAMA 2013;310:2435-42. doi:10.1001/jama.2013.280490
           (2+ years of PPIs or H2 blockers linked to B12 deficiency).
  [LAM17]  Lam JR et al. Gastroenterology 2017;152:821-9.
           doi:10.1053/j.gastro.2016.11.023 (2+ years linked to iron deficiency).
  [OC05]   O'Connell MB et al. Am J Med 2005;118:778-81.
           doi:10.1016/j.amjmed.2005.02.007 (omeprazole cut calcium carbonate
           absorption).
  [FA11]   Farrell CP et al. Gastroenterology Res 2011;4:243-51.
           doi:10.4021/gr379w (long-term PPI users absorbed less zinc; small study).
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
DIA, DIA_EDGE, DIA_FIBRE = "#EBDCD3", "#CDB3A6", "#F7EFEA"        # diaphragm
INK, INK_SOFT, LEAD = "#22292D", "#56626A", "#59646B"
DEEP = "#8E3110"

W, H = 735, 328          # diagram viewBox: 1 unit = 1 px at the 7.66 in content width
OX, OY = 215, 8          # anatomy origin inside the diagram
ZX, ZY, ZR = 614, 150, 108   # zoom circle
SX, SY, SR = 100, 102, 25    # zoom source ring (local coords, centred on the LES)


def _defs():
    return ("<defs>"
            # one radial gradient in user space so the silhouette and the wall stroke match exactly
            '<radialGradient id="gx-wall" gradientUnits="userSpaceOnUse" cx="120" cy="120" r="230">'
            f'<stop offset="0" stop-color="{WALL_HI}"/><stop offset=".55" stop-color="{WALL_MID}"/>'
            f'<stop offset="1" stop-color="{WALL_LO}"/></radialGradient>'
            '<linearGradient id="gx-lining" gradientUnits="userSpaceOnUse" x1="0" y1="100" x2="0" y2="315">'
            f'<stop offset="0" stop-color="{LINING_TOP}"/><stop offset="1" stop-color="{LINING_BOT}"/></linearGradient>'
            '<linearGradient id="gx-acid" x1="0" y1="0" x2="0" y2="1">'
            f'<stop offset="0" stop-color="{ACID_TOP}"/><stop offset=".35" stop-color="{ACID_MID}"/>'
            f'<stop offset="1" stop-color="{ACID_BOT}"/></linearGradient>'
            '<linearGradient id="gx-jet" x1="0" y1="0" x2="1" y2="0">'
            f'<stop offset="0" stop-color="{ACID_BOT}"/><stop offset=".45" stop-color="{ACID_TOP}"/>'
            f'<stop offset="1" stop-color="{ACID_MID}"/></linearGradient>'
            # cylinder shading laid over the outside of the esophagus
            '<linearGradient id="gx-cyl" x1="0" y1="0" x2="1" y2="0">'
            '<stop offset="0" stop-color="#7A2A1A" stop-opacity=".16"/>'
            '<stop offset=".32" stop-color="#FFFFFF" stop-opacity=".42"/>'
            '<stop offset=".6" stop-color="#FFFFFF" stop-opacity="0"/>'
            '<stop offset="1" stop-color="#7A2A1A" stop-opacity=".22"/></linearGradient>'
            '<linearGradient id="gx-topfade" x1="0" y1="0" x2="0" y2="1">'
            '<stop offset="0" stop-color="#FFFFFF" stop-opacity="1"/>'
            '<stop offset="1" stop-color="#FFFFFF" stop-opacity="0"/></linearGradient>'
            '<radialGradient id="gx-zbg" cx=".5" cy=".4" r=".62">'
            '<stop offset="0" stop-color="#FFF8F4"/><stop offset="1" stop-color="#FBE6DC"/></radialGradient>'
            '<linearGradient id="gx-les" x1="0" y1="0" x2="1" y2="0">'
            f'<stop offset="0" stop-color="{LES_DARK}"/><stop offset=".45" stop-color="{LES}"/>'
            f'<stop offset="1" stop-color="{LES_DARK}"/></linearGradient>'
            '<radialGradient id="gx-lesz" cx=".5" cy=".45" r=".6">'
            f'<stop offset="0" stop-color="#2DB3A5"/><stop offset=".7" stop-color="{LES}"/>'
            f'<stop offset="1" stop-color="{LES_DARK}"/></radialGradient>'
            + ''.join(f'<linearGradient id="gx-dia{k}" gradientUnits="userSpaceOnUse" x1="28" y1="0" x2="292" y2="0">'
                      f'<stop offset="0" stop-color="{c}" stop-opacity="0"/><stop offset=".2" stop-color="{c}"/>'
                      f'<stop offset=".82" stop-color="{c}"/><stop offset="1" stop-color="{c}" stop-opacity="0"/></linearGradient>'
                      for k, c in (("e", DIA_EDGE), ("f", DIA)))
            + '<marker id="gx-arr" viewBox="0 0 10 10" refX="5.2" refY="5" markerWidth="3.1" markerHeight="3.1" '
            f'orient="auto-start-reverse" markerUnits="strokeWidth"><path d="M0,0 L10,5 L0,10 z" fill="{REFLUX}"/></marker>'
            '<marker id="gx-arrh" viewBox="0 0 10 10" refX="5.2" refY="5" markerWidth="3.1" markerHeight="3.1" '
            'orient="auto-start-reverse" markerUnits="strokeWidth"><path d="M0,0 L10,5 L0,10 z" fill="#FFFFFF"/></marker>'
            "</defs>")


# ------------------------------------------------------------- anatomy (local coords)
# Front view.  The esophagus comes down a little left of the stomach's middle and
# enters at the cardia; the fundus domes up beside it (the angle of His); the body
# hangs down the right; the antrum hooks left and rises to the pylorus, where the
# duodenum (first part of the small intestine) leaves and turns down.
ESO_L, ESO_R = 83, 117
_STOMACH = ("C82,150 98,196 118,222 C123,229 121,235 111,236 "          # lesser curvature + angular notch
            "C86,236 58,229 36,229 C31,229 28,229 26,229 L26,255 "       # antrum roof -> pylorus
            "C52,290 100,315 141,313 C196,311 237,268 243,200 "          # antrum floor, greater curvature
            "C247,150 237,108 209,90 C187,77 151,75 131,87 "             # up the side, over the fundus
            "C123,92 119,99 117,106 ")                                  # down into the angle of His
STOM = "M83,95 L83,106 " + _STOMACH + "L117,95 Z"        # the cut-open stomach (opens into the tube under the LES)
SILH = "M83,-20 L83,106 " + _STOMACH + "L117,-20 Z"      # esophagus + stomach outline
DUO = "M44,242 C26,241 8,236 -6,244 C-20,252 -24,272 -19,294 L-16,305"   # duodenum centre line
ACID = ("M20,253 C52,245 80,259 112,251 C140,244 168,257 196,249 C214,244 232,250 260,246")
DIA_LINE = "M28,97 C68,89 108,82 134,76 C164,66 200,56 240,58 C260,59 276,65 292,74"


def _diaphragm():
    return (f'<path d="{DIA_LINE}" stroke="url(#gx-diae)" stroke-width="12" fill="none"/>'
            f'<path d="{DIA_LINE}" stroke="url(#gx-diaf)" stroke-width="9" fill="none"/>'
            f'<path d="{DIA_LINE}" stroke="{DIA_FIBRE}" stroke-width="1.4" fill="none" stroke-dasharray="7 5" '
            'stroke-linecap="round" opacity=".9"/>')


def _duodenum():
    out = []
    for w, c in ((30, WALL_LO), (25, "#E5866E"), (15, "#F0A28C"), (6, "#F6BBA7")):
        out.append(f'<path d="{DUO}" stroke="{c}" stroke-width="{w}" fill="none"/>')
    # cut end of the tube: the small intestine carries on from here
    out.append(f'<ellipse cx="-16" cy="305" rx="15" ry="5" fill="{LINING_BOT}" stroke="{WALL_LO}" stroke-width="2.4" '
               'transform="rotate(-16 -16 305)"/>')
    return "".join(out)


def _rugae():
    folds = ["M152,104 C198,110 226,150 224,214", "M136,120 C178,128 204,168 202,240",
             "M120,140 C152,152 174,186 174,244", "M108,168 C124,184 136,206 142,244",
             "M190,96 C216,104 234,128 238,160"]
    out = []
    for f in folds:
        out.append(f'<path d="{f}" stroke="{RUGA_LO}" stroke-width="3.2" fill="none" stroke-linecap="round" '
                   'opacity=".5" transform="translate(2.2,2.2)"/>')
        out.append(f'<path d="{f}" stroke="{RUGA_HI}" stroke-width="2.6" fill="none" stroke-linecap="round" opacity=".9"/>')
    return "".join(out)


def _acid_pool():
    bubbles = [(150, 272, 3.2), (182, 284, 2.4), (122, 290, 2.8), (204, 266, 2.2), (92, 274, 2.4), (58, 262, 2.0), (165, 300, 2.6)]
    drops = [(133, 226, 4.2), (121, 200, 3.4), (143, 208, 2.6), (112, 172, 2.8)]
    out = [f'<path d="{ACID} L260,330 L20,330 Z" fill="url(#gx-acid)"/>',
           f'<path d="{ACID}" stroke="#F3F7C2" stroke-width="2.2" fill="none" opacity=".9"/>']
    out += [f'<circle cx="{x}" cy="{y}" r="{r}" fill="#EEF3A6" opacity=".8"/>' for x, y, r in bubbles]
    # a splash thrown up toward the cardia
    out.append('<path d="M125,251 C121,240 125,231 132,228 C137,234 136,243 141,249 Z" fill="url(#gx-acid)"/>')
    out += [f'<circle cx="{x}" cy="{y}" r="{r}" fill="{ACID_MID}" stroke="{ACID_EDGE}" stroke-width=".9"/>' for x, y, r in drops]
    return "".join(out)


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
               'marker-end="url(#gx-arrh)" opacity=".95"/>')
    return out + f'<path d="{d}" stroke="{REFLUX}" stroke-width="{w}" fill="none" stroke-linecap="round" marker-end="url(#gx-arr)"/>'


def _anatomy():
    return "".join([
        f'<g transform="translate({OX},{OY})">', _diaphragm(), _duodenum(),
        # pylorus: the muscle ring where the stomach empties into the duodenum
        f'<rect x="20" y="226" width="11" height="32" rx="5" fill="{WALL_LO}"/>',
        _les_hoop("back"),
        f'<path d="{SILH}" fill="url(#gx-wall)" stroke="{WALL_LO}" stroke-width="1.6" stroke-linejoin="round"/>',
        f'<rect x="{ESO_L}" y="-20" width="{ESO_R - ESO_L}" height="124" fill="url(#gx-cyl)"/>',
        f'<clipPath id="gx-stom"><path d="{STOM}"/></clipPath>',
        '<g clip-path="url(#gx-stom)">',
        f'<path d="{STOM}" fill="url(#gx-lining)"/>', _rugae(), _acid_pool(),
        # wall rim: a stroke clipped to the outline gives an even 10-unit cut wall all round
        f'<path d="{STOM}" fill="none" stroke="{CUT}" stroke-width="23.5"/>',
        f'<path d="{STOM}" fill="none" stroke="url(#gx-wall)" stroke-width="20"/>',
        "</g>",
        f'<path d="M83,106 {_STOMACH}" fill="none" stroke="{WALL_LO}" stroke-width="1.6" stroke-linejoin="round"/>',
        _arrow("M152,262 C140,214 108,172 101,126 L100,42"),
        _les_hoop("front"),
        "</g>"])


# ------------------------------------------------------------------ zoom circle
# A slice through the junction, magnified about 3x.  The tube wall thickens into
# the LES (teal); below it the wall flares out into the stomach and rises on the
# right into the fundus (the same angle of His as the main view).  The ring is cut
# in half: its two cut faces sit in the walls and its back half shows across the
# far wall of the tube.
Z_SILH = ("M-46,-140 L-46,-72 C-46,-60 -55,-50 -55,-36 C-55,-22 -46,-12 -46,-2 "
          "C-46,22 -76,42 -140,54 L-140,140 L140,140 L140,-40 C112,-40 86,-28 68,-14 "
          "C60,-8 54,-3 50,0 C48,-6 46,-9 46,-14 C46,-22 55,-26 55,-38 C55,-50 46,-60 46,-72 L46,-140 Z")
Z_LUMEN = ("M-24,-140 L-24,-72 C-24,-60 -13,-50 -13,-36 C-13,-22 -24,-12 -24,-2 "
           "C-24,26 -60,52 -140,76 L-140,140 L140,140 L140,-20 C112,-18 92,-8 78,2 "
           "C66,11 54,16 42,16 C32,16 24,8 24,-2 C24,-12 13,-22 13,-36 C13,-50 24,-60 24,-72 L24,-140 Z")
Z_LES_L = "M-35,-74 C-52,-64 -53,-12 -37,-2 C-21,-9 -17,-60 -35,-74 Z"
Z_LES_R = "M35,-74 C52,-64 53,-12 37,-2 C21,-9 17,-60 35,-74 Z"
Z_POOL = "M-140,60 C-104,52 -76,66 -44,58 C-18,51 -2,62 22,55 C48,47 70,60 96,52 C116,46 130,52 140,50"
Z_JET = ("M-26,58 C-15,38 -10,12 -8,-14 C-7,-34 -10,-50 -12,-62 "
         "C-15,-71 -9,-79 -4,-71 C-3,-81 6,-84 7,-72 C10,-79 18,-74 14,-63 "
         "C11,-50 8,-34 8,-14 C9,12 14,38 27,58 Z")


def _zoom_les(d, side, k):
    fibres = "".join(
        f'<path d="M{side * 14},{y} C{side * 26},{y - 4} {side * 40},{y - 4} {side * 56},{y}" stroke="{LES_HI}" '
        'stroke-width="1.3" fill="none" opacity=".55"/>' for y in (-62, -50, -38, -26, -14))
    return (f'<clipPath id="gx-zles{k}"><path d="{d}"/></clipPath>'
            f'<path d="{d}" fill="url(#gx-lesz)" stroke="{LES_DARK}" stroke-width="1.5"/>'
            f'<g clip-path="url(#gx-zles{k})">{fibres}</g>')


def _zoom():
    r = ZR - 4
    drops = [(-20, -82, 4.2), (17, -88, 3.5), (-3, -97, 3.0), (25, -71, 2.4), (-26, -64, 2.1), (6, -108, 2.2)]
    return "".join([
        f'<circle cx="{ZX + 1.5}" cy="{ZY + 2.5}" r="{ZR + 3}" fill="#5A2A1A" opacity=".08"/>',
        f'<g transform="translate({ZX},{ZY})">',
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
        # back half of the LES ring, seen across the far wall of the open tube
        f'<path d="M-16,-34 Q0,-50 16,-34" stroke="{LES_DARK}" stroke-width="15" fill="none" opacity=".35"/>',
        f'<path d="M-16,-34 Q0,-50 16,-34" stroke="{LES}" stroke-width="10" fill="none" opacity=".45"/>',
        f'<path d="M-62,40 C-48,32 -40,24 -33,14 M-104,62 C-84,54 -66,46 -54,32 M70,24 C84,12 100,4 124,0 '
        f'M62,38 C82,26 106,20 136,18" stroke="{RUGA_HI}" stroke-width="3" fill="none" stroke-linecap="round" opacity=".9"/>',
        # acid pool, and the splash forced up through the open valve
        f'<path d="{Z_POOL} L140,140 L-140,140 Z" fill="url(#gx-acid)"/>',
        f'<path d="{Z_POOL}" stroke="#F3F7C2" stroke-width="2.4" fill="none"/>',
        f'<path d="{Z_JET}" fill="url(#gx-jet)" stroke="{ACID_EDGE}" stroke-width="1" stroke-linejoin="round"/>',
        '<path d="M-3,46 C-4,20 -3,-14 -4,-52" stroke="#F6F9CF" stroke-width="2" fill="none" stroke-linecap="round" opacity=".85"/>',
        "".join(f'<circle cx="{x}" cy="{y}" r="{rr}" fill="{ACID_MID}" stroke="{ACID_EDGE}" stroke-width="1"/>' for x, y, rr in drops),
        "</g>",
        # cut face of the walls, then the two cut faces of the LES ring inside the thickened wall
        f'<path d="{Z_LUMEN}" fill="none" stroke="{CUT}" stroke-width="3"/>',
        _zoom_les(Z_LES_L, -1, 0), _zoom_les(Z_LES_R, 1, 1),
        f'<path d="M2,36 C1,10 -1,-14 0,-44 L1,-86" stroke="#FFFFFF" stroke-width="7.4" fill="none" stroke-linecap="round" '
        'opacity=".75"/>',
        _arrow("M2,36 C1,10 -1,-14 0,-44 L1,-86", 4.4, halo=False),
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
    a = math.acos((r1 - ZR) / d)
    pts = []
    for s in (-1, 1):
        ang = base + s * a
        pts.append(((x1 + r1 * math.cos(ang), y1 + r1 * math.sin(ang)),
                    (ZX + ZR * math.cos(ang), ZY + ZR * math.sin(ang))))
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
            f'<rect x="{OX + ESO_L - 6}" y="0" width="{ESO_R - ESO_L + 12}" height="30" fill="url(#gx-topfade)"/>',
            _zoom(),
            T(ZX, 22, "UP CLOSE AT THE VALVE", 10.5, 800, DEEP, "middle", ls=1.6),
            T(ZX, 288, "The relaxed valve stays open,", 13.5, 800, INK, "middle"),
            T(ZX, 305, "so acid splashes back up.", 13.5, 800, INK, "middle"),
            _label(168, 48, "Esophagus", "your food tube", OX + ESO_L - 1, OY + 36),
            _label(168, 92, "Diaphragm", "breathing muscle", OX + 70, OY + 89),
            _label(168, 142, "LES valve", "a ring of muscle", OX + SX - 21, OY + SY + 4),
            _label(168, 208, "Stomach", None, OX + 97, OY + 196),
            _label(168, 284, "Small intestine", None, OX - 22, OY + 275)]
    return svg(W, H, "".join(body), "How acid reflux happens: the LES valve at the bottom of the esophagus relaxes and stomach acid splashes up")


def key_row():
    """KEY for the diagram, using the exact symbols drawn in the art."""
    def sw(inner, vb="-12 -11 24 22"):
        return f'<svg viewBox="{vb}" width="24" height="22" aria-hidden="true">{inner}</svg>'
    acid = sw('<path d="M-11,-2 C-7,-7 -3,1 1,-3 C5,-7 8,-3 11,-4 L11,8 L-11,8 Z" '
              f'fill="{ACID_MID}" stroke="{ACID_EDGE}" stroke-width=".9"/>'
              '<path d="M-11,-2 C-7,-7 -3,1 1,-3 C5,-7 8,-3 11,-4" stroke="#F3F7C2" stroke-width="1.6" fill="none"/>')
    les = sw(f'<rect x="-6" y="-11" width="12" height="22" fill="{WALL_MID}"/>'
             f'<path d="M-10,1 A10,3.4 0 0 0 10,1" stroke="{LES_DARK}" stroke-width="5.4" fill="none" stroke-linecap="round"/>'
             f'<path d="M-10,1 A10,3.4 0 0 0 10,1" stroke="{LES}" stroke-width="3.4" fill="none" stroke-linecap="round"/>')
    arrow = sw(f'<path d="M0,10 V-3" stroke="{REFLUX}" stroke-width="3.6" stroke-linecap="round"/>'
               f'<path d="M-6,-1 L0,-10 L6,-1 Z" fill="{REFLUX}"/>')
    return ('<div class="gx-key"><b>Key</b>'
            f'<span>{acid}<em>Stomach acid</em></span>'
            f'<span>{les}<em>LES valve</em><i>the ring of muscle that shuts the stomach</i></span>'
            f'<span>{arrow}<em>Reflux</em><i>acid moving up</i></span></div>')


# ------------------------------------------------------------- trigger picture row
# 64x64 line icons, stroked with currentColor (same grammar as kit.ICONS).
# Foods and habits named by [ACG22]; peppermint and alcohol also by NIDDK.
TRIGGERS = [
    ("Fried or fatty food",
     '<path d="M17 30h30l-4 25a3 3 0 0 1-3 2.6H24a3 3 0 0 1-3-2.6z"/><path d="M23 30l-2-17M29.5 30V10M36 30l1-18M42.5 30l3-15"/>'
     '<path d="M24 41c5 3 11 3 16 0"/>'),
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
    cells = "".join(f'<div class="gx-tr"><span class="gx-badge">{_ic(b, "0.31in", t["deep"], 3.1)}</span><span>{lab}</span></div>'
                    for lab, b in TRIGGERS)
    return (f'<div class="gx-trig"><div class="gx-h">Common triggers <i>They differ from person to person. '
            f'Notice which ones bother you.</i></div><div class="gx-trow">{cells}</div></div>')


# ----------------------------------------------------------- nutrient strip
NUTRIENTS = [("Mg", "Magnesium"),    # [FDA] 2011: low magnesium with long-term PPI use
             ("B12", "Vitamin B12"),  # [LAM13]
             ("Ca", "Calcium"),       # [OC05]; [FDA] fracture warning
             ("Fe", "Iron"),          # [LAM17]
             ("Zn", "Zinc")]          # [FA11]


def depletion_strip(t, ed):
    pharmacy = ed.get("who") == "your pharmacist"
    stop = ("Never stop one on your own: ask your pharmacist and prescriber for a plan."
            if pharmacy else "Never stop one on your own: ask your provider for a plan.")
    coins = "".join(f'<div class="gx-coin"><b>{s}</b><span>{n}</span></div>' for s, n in NUTRIENTS)
    return ('<div class="gx-strip"><div class="gx-meds"><div class="gx-h">Long-term acid blockers can lower</div>'
            '<p>PPIs (like omeprazole) and H2 blockers (like famotidine) help many people heal. But stomach acid also helps you '
            'absorb nutrients, and the FDA has warned about low magnesium and broken bones with long-term, high-dose PPI use.'
            f'<sup>1</sup> {stop}</p></div>'
            f'<div class="gx-dep"><div class="gx-coins">{coins}</div>'
            '<div class="gx-ask">Ask {who} whether a nutrient check makes sense.</div></div></div>')


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
         "You lose weight without trying"]        # [ACG22] weight loss


def front(t, ed):
    feel = "".join(f"<li>{x}</li>" for x in FEEL)
    alarm = "".join(f"<li>{x}</li>" for x in ALARM)
    return (f'<div class="gxf"><div class="gx-art">{art_reflux()}{key_row()}</div>'
            '<div class="gx-row">'
            f'<div class="gx-feel"><div class="gx-h">How it can feel</div><ul>{feel}</ul>'
            '<p class="gx-why"><b>Why treat it?</b> Left alone, acid can inflame, narrow or scar the esophagus.</p></div>'
            f'<div class="gx-alarm"><div class="gx-h">Get care right away if</div><ul>{alarm}</ul>'
            # [ACG22]: chest pain needs heart disease ruled out before anyone calls it reflux
            '<p><b>Chest pain or pressure? Call 911.</b> Heart trouble can feel like heartburn.</p></div>'
            '</div>'
            f'{trigger_row(t)}{depletion_strip(t, ed)}'
            '<p class="gx-fn">1. U.S. Food and Drug Administration. Drug Safety Communications on proton pump inhibitors: '
            'possible increased risk of fractures (2010) and low magnesium levels with long-term use (2011).</p></div>')


CSS = r"""
.gxf{display:flex;flex-direction:column;gap:0.07in}
.gxf .gx-art>svg{display:block;width:100%;height:auto}
.gxf .gx-key{display:flex;align-items:center;justify-content:center;gap:4px 18px;flex-wrap:wrap;margin:2px auto 0;
  padding:3px 14px;border:1px solid #EAD9CF;border-radius:99px;background:#FFFBF8;width:max-content;max-width:100%}
.gxf .gx-key>b{font:800 7pt Inter,sans-serif;letter-spacing:.16em;text-transform:uppercase;color:var(--deep)}
.gxf .gx-key span{display:inline-flex;align-items:center;gap:5px;font-size:8pt;color:#2B3236}
.gxf .gx-key em{font-style:normal;font-weight:700}
.gxf .gx-key i{font-style:normal;color:#56626A}
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
.gxf .gx-alarm p{margin:3px 0 0;font-size:8.3pt;line-height:1.3;color:#2B3236}
.gxf .gx-alarm p b{color:#A5281E}
.gxf .gx-trow{display:grid;grid-template-columns:repeat(10,1fr);gap:0 0.04in}
.gxf .gx-tr{display:flex;flex-direction:column;align-items:center;text-align:center}
.gxf .gx-badge{width:0.47in;height:0.47in;border-radius:50%;background:var(--soft);display:flex;align-items:center;justify-content:center;
  box-shadow:inset 0 0 0 1.5px #F3D3BC}
.gxf .gx-tr>span:last-child{font-size:7.5pt;line-height:1.18;color:#2B3236;margin-top:3px;font-weight:600}
.gxf .gx-strip{display:grid;grid-template-columns:1.18fr 1fr;gap:0.14in;align-items:center;background:var(--soft);border-radius:10px;
  padding:0.07in 0.12in 0.07in 0.14in}
.gxf .gx-meds p{margin:0;font-size:8.2pt;line-height:1.34;color:#2B3236}
.gxf .gx-meds sup{color:var(--c1);font-weight:700}
.gxf .gx-dep{background:#fff;border-radius:8px;padding:0.05in 0.08in 0.05in}
.gxf .gx-coins{display:grid;grid-template-columns:repeat(5,1fr);gap:0.04in}
.gxf .gx-coin{display:flex;flex-direction:column;align-items:center}
.gxf .gx-coin b{width:0.4in;height:0.4in;border-radius:50%;background:var(--c1);color:#fff;display:flex;align-items:center;justify-content:center;
  font:800 10pt Inter,sans-serif;box-shadow:0 0 0 2px #fff,0 0 0 3.2px #F0B89A}
.gxf .gx-coin span{font-size:7.2pt;font-weight:700;color:#2B3236;margin-top:3px;text-align:center;line-height:1.1}
.gxf .gx-ask{font-size:7.6pt;color:#3F4A50;text-align:center;margin-top:3px}
.gxf .gx-fn{margin:0;font-size:6.6pt;color:#5E686F;line-height:1.3}
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
