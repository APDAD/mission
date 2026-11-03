"""Lyme Disease sheet (ND-IM-301).  Self-contained: front art, copy and back data.

Front rebuilt 2026-11-03 from Asher's notes on draft 1 ("That's pretty good...
Lyme disease, symptoms. That's a pretty good one"): same composition (how it
spreads, symptoms on the body beside three notes, know your ticks), plus
  * a KEY for every symbol (early dot, later dot, both looks of the rash),
  * every label at 7 pt or more and nothing clipped at any edge,
  * the three ticks drawn from life: blacklegged (deer) tick dark with a
    red-orange body, western blacklegged, and the lone star tick with the white
    dot on its back.

Fix round 2026-11-03 (art director's review of the rebuilt front):
  * purple and orange now mean only "early sign" and "later sign": card headers,
    note rules, arrows and the ACTUAL SIZE label moved to a neutral slate;
  * BITE caption no longer reassures (other germs pass faster than Lyme), the
    skin cut-away's red line is labelled "blood vessel", the other-infections card
    uses disease names with singular germ labels;
  * tick mouthparts drawn as two palps with a dark seam (no white cross), and the
    actual-size strip scaled from the drawing's real length;
  * the notes column fills the symptoms row, the Georgia card is no longer
    half-empty, the western-tick card teaches "where you live is the best clue",
    and the after-treatment note no longer ties the back-page products to Lyme.

Back-page pass 2026-11-03 (with the final front review's leftover defects):
  * FRONT: the feeding tick has EIGHT legs (four near, four paler far ones), a
    flatter half-fed body and a solid dark shield cap instead of a black band;
    Borrelia are drawn as real corkscrew helices; the body shows the rash as it
    most often looks (solid red, faint clearing) and the KEY shows both looks;
    the lone star tick's eyes no longer read as extra white dots; one skin
    gradient for the whole figure; "WAITS" step label with grass; the blood vessel
    stops short of its label; a missing CDC later sign ("more rashes on other
    parts of the body") fills the empty lower right; "OTHER INFECTIONS DEER TICKS
    CAN CARRY" (the western tick carries fewer); Georgia source note corrected.
  * BACK: rebuilt as RECOVERY SUPPORT (gut, immune, inflammatory balance, detox,
    energy) with five NutriDyn products from NutriDyn protocols, label facts in
    products.d/lyme.json, a daily rhythm that keeps magnesium away from
    doxycycline, and edition-specific medicine-and-nutrient checks.

Every SVG is drawn at 1:1 with its printed CSS size (viewBox width = rendered
width in CSS px), so an SVG font-size of 9.6 (the smallest used) prints at 7.2 pt.
Sources (each number below carries a short comment): CDC Lyme disease pages
(Signs and Symptoms of Untreated Lyme Disease; Transmission; Data and Statistics),
CDC tick pages (Regions Where Ticks Live; How Ticks Spread Disease; STARI), CDC MMWR
2017;66(15):408-409 (Powassan virus), Kugeler et al., Emerg Infect Dis 2021;27(2),
UGA Extension Circular 937 ("Protect Yourself from Ticks") and UGA CAES Newswire
("Ticks in Georgia", Nancy Hinkle) for Georgia.
"""
import math
import re

import kit
from svgkit import FONT, T, defs, svg

# Fine-tipped tweezers (angled, as people hold them) gripping a tick (eight legs) at the skin
# line, with an arrow for "pull straight up".
kit.ICONS.setdefault("ly_tweezers",
    '<path d="M51.5 6.5C55.5 6 58.2 9.6 57.6 13.6"/>'
    '<path d="M51.5 6.5 26.6 41.6"/><path d="M57.6 13.6 29.4 43.4"/>'
    '<path d="M40.2 20.4l3.4 2.6M44.6 25.6l3 2.8"/>'
    '<ellipse cx="25" cy="49.6" rx="4.4" ry="3.6" fill="currentColor" stroke="none"/>'
    '<circle cx="27.4" cy="45.6" r="1.8" fill="currentColor" stroke="none"/>'
    '<path d="M21.4 47.4l-4.2-2M20.8 49.4h-4.8M21 51.4l-4.2 2.2M22 53l-2.8 3.2'
    'M28.6 49.8l4.4-.6M28.8 51.6l4.2 2M27.8 53.2l2.6 3.4M26.4 53.6l.6 3.6" stroke-width="1.6"/>'
    '<path d="M7 59H57"/><path d="M12 40V20M7.4 24.6 12 20l4.6 4.6"/>')
# A magnifying glass over a tick (eight legs): "check your skin".
kit.ICONS.setdefault("ly_check",
    '<circle cx="27" cy="27" r="17"/><path d="M39.5 39.5 55 55"/>'
    '<ellipse cx="27" cy="29" rx="4.2" ry="5.2" fill="currentColor" stroke="none"/>'
    '<circle cx="27" cy="22.6" r="1.8" fill="currentColor" stroke="none"/>'
    '<path d="M23.4 25.6l-4.6-2.8M22.9 28.2l-5.2-.6M23 30.8l-5 1.8M23.8 33.2l-3.6 3.6'
    'M30.6 25.6l4.6-2.8M31.1 28.2l5.2-.6M31 30.8l5 1.8M30.2 33.2l3.6 3.6" stroke-width="1.6"/>')

EARLY = "#4A2C80"       # purple: early sign (the symptom key's colour; used nowhere else in the art)
LATER = "#D9873A"       # orange: later sign (likewise)
LATER_TXT = "#A65A16"   # darker orange for text on white
RASH = "#C8473C"        # erythema migrans red
INK = "#2B3236"
SOFT_INK = "#4A555C"
SLATE = "#3D4A53"       # neutral for card headers, note rules and arrows
SLATE_MID = "#5D6B74"
PALE = "#F2F4F5"        # neutral card fill
SKIN = ("#F4CBAA", "#E9B089", "#C98E67")   # light, mid, outline


def _f(v):
    return f"{v:.2f}".rstrip("0").rstrip(".")


def TR(x, y, lines, size=10, weight=600, fill=INK, anchor="start", lh=1.22, bold=800, bold_fill=None):
    """Like svgkit.T, but a line may hold *bold* and _italic_ runs."""
    if isinstance(lines, str):
        lines = [lines]
    out = [f'<text x="{_f(x)}" y="{_f(y)}" {FONT} font-size="{size}" font-weight="{weight}" fill="{fill}" '
           f'text-anchor="{anchor}">']
    bf = f' fill="{bold_fill}"' if bold_fill else ""
    for i, ln in enumerate(lines):
        out.append(f'<tspan x="{_f(x)}" dy="{0 if i == 0 else _f(size * lh)}">')
        for seg in re.split(r"(\*[^*]+\*|_[^_]+_)", ln.strip()):
            if len(seg) > 2 and seg[0] == seg[-1] == "*":
                out.append(f'<tspan font-weight="{bold}"{bf}>{seg[1:-1]}</tspan>')
            elif len(seg) > 2 and seg[0] == seg[-1] == "_":
                out.append(f'<tspan font-style="italic">{seg[1:-1]}</tspan>')
            else:
                out.append(seg)
        out.append("</tspan>")
    out.append("</text>")
    return "".join(out)


# ============================================================ ticks, top view
# Adult females unless noted.  Proportions and colours follow CDC and UGA
# identification photographs: Ixodes females have a small black shield (scutum),
# black legs and a red-orange (western: darker red-brown) body and long mouthparts;
# the lone star female is broader and rounder, chestnut brown, with festoons
# (the scalloped rear edge) and one silvery-white spot on her shield.
TICK_LOOK = {
    "deer": dict(rx=15.0, ry=20.0, body=("#E8834F", "#BF472A", "#6A2014"), shield=("#4E3D33", "#130D0A"),
                 legs="#1A1310", joint="#6A564A", scut=0.46, palp=14.5),
    "western": dict(rx=13.4, ry=21.8, body=("#B4503F", "#7F2C22", "#3E110C"), shield=("#4A3A30", "#110C0A"),
                    legs="#1A1310", joint="#6A564A", scut=0.44, palp=15.5),
    "lonestar": dict(rx=18.6, ry=18.8, body=("#C3804E", "#93522F", "#4F2814"), shield=("#7C5536", "#3A2313"),
                     legs="#74472B", joint="#C29468", scut=0.55, palp=15.0, festoons=True, spot=True),
    "nymph": dict(rx=14.0, ry=16.5, body=("#D2C2AC", "#A08E78", "#605244"), shield=("#4F4237", "#1E1712"),
                  legs="#33281F", joint="#6B5D52", scut=0.42, palp=10.0),
}

# Right-hand legs I-IV, root on the body edge to the claw, for a body 15 wide.
LEGS = [
    [(7.0, -8.5), (12.4, -16.2), (15.0, -24.0), (15.8, -31.0), (15.0, -37.4)],
    [(10.8, -4.0), (18.2, -8.4), (24.4, -13.4), (29.0, -16.8), (32.6, -20.6)],
    [(12.8, 0.8), (20.6, 1.8), (27.4, 5.2), (32.0, 9.2), (35.2, 14.0)],
    [(13.8, 5.6), (19.8, 11.0), (23.8, 18.4), (26.6, 25.8), (27.8, 32.6)],
]
QUEST_I = [(7.0, -8.5), (10.4, -17.5), (11.6, -27.0), (12.2, -36.0), (14.6, -45.0)]
LEG_W = (2.8, 2.4, 1.9, 1.35)


def _egg(rx, ry, cy):
    """Tick body outline: narrower at the head end, widest just behind the middle."""
    t, b, w = cy - ry * 0.85, cy + ry, cy + ry * 0.15
    return (f"M0,{_f(t)} C{_f(rx * .6)},{_f(t)} {_f(rx)},{_f(w - (w - t) * .62)} {_f(rx)},{_f(w)} "
            f"C{_f(rx)},{_f(w + (b - w) * .55)} {_f(rx * .56)},{_f(b)} 0,{_f(b)} "
            f"C{_f(-rx * .56)},{_f(b)} {_f(-rx)},{_f(w + (b - w) * .55)} {_f(-rx)},{_f(w)} "
            f"C{_f(-rx)},{_f(w - (w - t) * .62)} {_f(-rx * .6)},{_f(t)} 0,{_f(t)}Z"), t, b, w


def tick_top(kind, x, y, s=1.0, rot=0.0, uid="lyt", quest=False, shadow=True, minw=0.0):
    """A hard tick seen from above, head up, centred near its body.  minw is the
    thinnest printed leg stroke in CSS px (keeps actual-size drawings visible)."""
    k = TICK_LOOK[kind]
    rx, ry, cy = k["rx"], k["ry"], 6.0
    body, t, b, w = _egg(rx, ry, cy)
    grow = rx / 15.0
    out = [f'<g transform="translate({_f(x)},{_f(y)}) rotate({_f(rot)}) scale({s:.4f})">',
           f'<defs><radialGradient id="{uid}b" cx="38%" cy="32%" r="80%"><stop offset="0" stop-color="{k["body"][0]}"/>'
           f'<stop offset=".55" stop-color="{k["body"][1]}"/><stop offset="1" stop-color="{k["body"][2]}"/></radialGradient>'
           f'<radialGradient id="{uid}s" cx="38%" cy="28%" r="85%"><stop offset="0" stop-color="{k["shield"][0]}"/>'
           f'<stop offset="1" stop-color="{k["shield"][1]}"/></radialGradient>'
           f'<radialGradient id="{uid}g"><stop offset="0" stop-color="#fff" stop-opacity=".6"/>'
           f'<stop offset="1" stop-color="#fff" stop-opacity="0"/></radialGradient>'
           f'<clipPath id="{uid}c"><path d="{body}"/></clipPath></defs>']
    if shadow:
        out.append(f'<ellipse cx="1.8" cy="{_f(cy + 3.5)}" rx="{_f(rx * 1.04)}" ry="{_f(ry * .98)}" fill="#000" opacity=".12"/>')
    # legs (drawn under the body), mirrored left/right
    for side in (1, -1):
        for i, leg in enumerate(LEGS):
            pts = QUEST_I if (quest and i == 0) else leg
            dx = pts[0][0] * (grow - 1)
            pts = [((px + dx) * side, py) for px, py in pts]
            for j in range(4):
                (x0, y0), (x1, y1) = pts[j], pts[j + 1]
                wdt = max(LEG_W[j], minw / s if minw else 0)
                out.append(f'<line x1="{_f(x0)}" y1="{_f(y0)}" x2="{_f(x1)}" y2="{_f(y1)}" stroke="{k["legs"]}" '
                           f'stroke-width="{_f(wdt)}" stroke-linecap="round"/>')
            if s * 3 > 1.2:   # segment joints, only where they can be seen
                for j in (1, 2, 3):
                    out.append(f'<circle cx="{_f(pts[j][0])}" cy="{_f(pts[j][1])}" r="{_f(LEG_W[j] * .42)}" '
                               f'fill="{k["joint"]}" opacity=".55"/>')
    # body and its grooves
    out.append(f'<path d="{body}" fill="url(#{uid}b)" stroke="{k["body"][2]}" stroke-width="0.8"/>')
    g = [f'<g clip-path="url(#{uid}c)" fill="none" stroke="{k["body"][2]}" stroke-width=".75" opacity=".6">']
    lo = (b - w)
    if k.get("festoons"):
        angs = [22 + i * (136 / 11) for i in range(12)]
        for a in angs:
            ca, sa = math.cos(math.radians(a)), math.sin(math.radians(a))
            g.append(f'<line x1="{_f(rx * .86 * ca)}" y1="{_f(w + lo * .86 * sa)}" x2="{_f(rx * 1.1 * ca)}" y2="{_f(w + lo * 1.1 * sa)}"/>')
        arc = " ".join(f"{_f(rx * .86 * math.cos(math.radians(a)))},{_f(w + lo * .86 * math.sin(math.radians(a)))}"
                       for a in range(22, 159, 4))
        g.append(f'<polyline points="{arc}"/>')
    else:
        arc = " ".join(f"{_f(rx * .86 * math.cos(math.radians(a)))},{_f(w + lo * .86 * math.sin(math.radians(a)))}"
                       for a in range(8, 173, 4))
        g.append(f'<polyline points="{arc}" opacity=".7"/>')
    s1 = t + k["scut"] * (b - t)
    g.append(f'<path d="M0,{_f(s1 + 2)} V{_f(b - 4)}" opacity=".55"/>'
             f'<path d="M{_f(rx * .36)},{_f(s1 + 3)} Q{_f(rx * .42)},{_f((s1 + b) / 2)} {_f(rx * .3)},{_f(b - 6)}" opacity=".45"/>'
             f'<path d="M{_f(-rx * .36)},{_f(s1 + 3)} Q{_f(-rx * .42)},{_f((s1 + b) / 2)} {_f(-rx * .3)},{_f(b - 6)}" opacity=".45"/>')
    g.append("</g>")
    out.append("".join(g))
    # shield (scutum)
    s0, L = t - 0.8, s1 - (t - 0.8)
    sw = rx * (0.72 if k.get("spot") else 0.66)
    tail = 0.40 if k.get("spot") else 0.55        # lone star shield comes to a rounder point
    shield = (f"M{_f(-sw * .45)},{_f(s0)} Q0,{_f(s0 + 2.4)} {_f(sw * .45)},{_f(s0)} "
              f"C{_f(sw * .86)},{_f(s0 - .3)} {_f(sw)},{_f(s0 + L * .25)} {_f(sw)},{_f(s0 + L * .45)} "
              f"C{_f(sw)},{_f(s0 + L * .74)} {_f(sw * tail)},{_f(s1)} 0,{_f(s1)} "
              f"C{_f(-sw * tail)},{_f(s1)} {_f(-sw)},{_f(s0 + L * .74)} {_f(-sw)},{_f(s0 + L * .45)} "
              f"C{_f(-sw)},{_f(s0 + L * .25)} {_f(-sw * .86)},{_f(s0 - .3)} {_f(-sw * .45)},{_f(s0)}Z")
    out.append(f'<path d="{shield}" fill="url(#{uid}s)" stroke="{k["shield"][1]}" stroke-width=".6"/>')
    out.append(f'<ellipse cx="{_f(-sw * .34)}" cy="{_f(s0 + L * .32)}" rx="{_f(sw * .32)}" ry="{_f(L * .22)}" fill="url(#{uid}g)" opacity=".55"/>')
    if k.get("spot"):   # the "lone star": one silvery-white spot at the back of her shield
        out.append(f'<ellipse cx="0" cy="{_f(s1 - L * .23)}" rx="{_f(sw * .3)}" ry="{_f(L * .2)}" fill="#FBF8F0" '
                   f'stroke="#E2D5BC" stroke-width=".6"/>'
                   f'<ellipse cx="{_f(-sw * .08)}" cy="{_f(s1 - L * .28)}" rx="{_f(sw * .12)}" ry="{_f(L * .08)}" fill="#fff"/>'
                   f'<circle cx="{_f(sw * .93)}" cy="{_f(s0 + L * .3)}" r=".8" fill="#8A6A44"/>'
                   f'<circle cx="{_f(-sw * .93)}" cy="{_f(s0 + L * .3)}" r=".8" fill="#8A6A44"/>')
    # mouthparts (capitulum) from above: a short base, then two long palps held
    # together like a beak.  The palps are two separate shapes over a near-black
    # under-shape, so a thin DARK seam runs between them; no light strokes or
    # crossbars (at print size those read as a pill with a cross on it).
    pl, c0 = k["palp"], t - 3.4
    sh, hl = k["shield"][1], k["shield"][0]
    seam = "#0B0705"
    out.append(f'<defs><linearGradient id="{uid}m" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="{hl}"/>'
               f'<stop offset=".75" stop-color="{sh}"/></linearGradient></defs>')
    out.append(f'<path d="M-4.3,{_f(c0 + 4.4)} L-3.6,{_f(c0 + .6)} Q-3.45,{_f(c0)} -2.9,{_f(c0)} H2.9 '
               f'Q3.45,{_f(c0)} 3.6,{_f(c0 + .6)} L4.3,{_f(c0 + 4.4)}Z" fill="url(#{uid}m)" stroke="{seam}" stroke-width=".3"/>')

    def palp(sd, g):
        return (f'M{_f(g * sd)},{_f(c0 + .6)} C{_f(1.9 * sd)},{_f(c0 + .5)} {_f(3.5 * sd)},{_f(c0 - pl * .12)} '
                f'{_f(3.65 * sd)},{_f(c0 - pl * .42)} C{_f(3.78 * sd)},{_f(c0 - pl * .74)} {_f(2.7 * sd)},{_f(c0 - pl)} '
                f'{_f((g + .25) * sd)},{_f(c0 - pl)} Q{_f(g * sd)},{_f(c0 - pl)} {_f(g * sd)},{_f(c0 - pl + .6)}Z')
    out.append(f'<path d="{palp(1, 0)} {palp(-1, 0)}" fill="{seam}" stroke="{seam}" stroke-width=".35"/>')
    for sd in (-1, 1):
        out.append(f'<path d="{palp(sd, .3)}" fill="url(#{uid}m)"/>')
    out.append(f'<ellipse cx="{_f(-rx * .34)}" cy="{_f(cy + ry * .18)}" rx="{_f(rx * .26)}" ry="{_f(ry * .34)}" '
               f'fill="url(#{uid}g)" opacity=".8"/>')
    out.append("</g>")
    return "".join(out)


def tick_len(kind):
    """Palp tip to rear edge, in drawing units: the length CDC and Extension
    pages mean by a tick's size.  Rear = cy + ry; palp tip = (cy - .85 ry) - 3.4 - palp."""
    k = TICK_LOOK[kind]
    return 1.85 * k["ry"] + 3.4 + k["palp"]


def tick_feeding(hx, hy, uid="lyf"):
    """A blacklegged tick seen from the side, feeding: hypostome in the skin, palps
    resting on the surface, body tilted up, eight legs braced on the skin (the far
    four paler).  (hx, hy) = base of the mouthparts, just above the skin surface."""
    th = -48.0
    ca, sa = math.cos(math.radians(th)), math.sin(math.radians(th))

    def P(lx, ly):
        return hx + lx * ca - ly * sa, hy + lx * sa + ly * ca

    k = TICK_LOOK["deer"]
    sk = hy + 0.6                         # skin surface
    out = [f'<defs><linearGradient id="{uid}b" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{k["body"][0]}"/>'
           f'<stop offset=".6" stop-color="{k["body"][1]}"/><stop offset="1" stop-color="{k["body"][2]}"/></linearGradient>'
           f'<radialGradient id="{uid}g"><stop offset="0" stop-color="#fff" stop-opacity=".55"/>'
           f'<stop offset="1" stop-color="#fff" stop-opacity="0"/></radialGradient>'
           f'<radialGradient id="{uid}p"><stop offset="0" stop-color="{RASH}" stop-opacity=".55"/>'
           f'<stop offset="1" stop-color="{RASH}" stop-opacity="0"/></radialGradient></defs>']

    def leg(r, kn, tip, col, w0):
        # femur from under the body to the knee, then tibia and tarsus curving to a claw
        mx, my = (kn[0] + tip[0]) / 2 - .6, (kn[1] + tip[1]) / 2 - 1.2
        return (f'<path d="M{_f(r[0])},{_f(r[1])} L{_f(kn[0])},{_f(kn[1])}" stroke="{col}" stroke-width="{w0}" '
                f'stroke-linecap="round" fill="none"/>'
                f'<path d="M{_f(kn[0])},{_f(kn[1])} Q{_f(mx)},{_f(my)} {_f(tip[0])},{_f(tip[1])}" stroke="{col}" '
                f'stroke-width="{w0 * .72:.2f}" stroke-linecap="round" fill="none"/>')

    # EIGHT legs, all from under the belly: four near (dark) and four far (paler, drawn first so the
    # near legs pass in front of them).  Along the skin the tips alternate near/far, so all eight can
    # be counted: front pairs I-II reach forward, back pairs III-IV reach back.
    far = [(P(6, 6), (hx - 3, hy - 8), (hx - 12.5, sk - .8)),            # far I
           (P(10, 6.5), (hx - 8.5, hy - 7), (hx - 22.5, sk - .8)),       # far II
           (P(14, 6.5), (hx + 22, hy - 12), (hx + 28, sk - .8)),         # far III
           (P(20, 6.5), (hx + 32, hy - 10), (hx + 40, sk - .8))]         # far IV
    near = [(P(8, 7.5), (hx - 6.5, hy - 4), (hx - 17.5, sk)),            # I
            (P(12, 8), (hx - 11, hy - 9.5), (hx - 28, sk)),              # II
            (P(17, 8), (hx + 27, hy - 6), (hx + 33, sk)),                # III
            (P(22, 7.5), (hx + 37, hy - 14), (hx + 47, sk))]             # IV
    for r, kn, tp in far:
        out.append(leg(r, kn, tp, "#6B5A4E", 1.6))
    for r, kn, tp in near:
        out.append(leg(r, kn, tp, "#17110E", 2.0))
        out.append(f'<circle cx="{_f(kn[0])}" cy="{_f(kn[1])}" r=".7" fill="#6A564A"/>')
    tip = P(-19, 2.4)
    out.append(f'<ellipse cx="{_f(tip[0])}" cy="{_f(tip[1] - 1)}" rx="8" ry="5.5" fill="url(#{uid}p)"/>')
    # half-fed idiosoma: a flattened oval (back = local -y, belly = +y, toward the skin)
    body = ("M2.5,0 C2.5,-6.6 9,-10 19,-10 C29,-10 35.5,-6.2 35.5,0 C35.5,5.8 29,9 19,9 "
            "C9,9 2.5,6 2.5,0Z")
    out.append(f'<defs><clipPath id="{uid}c"><path d="{body}"/></clipPath>'
               f'<linearGradient id="{uid}s" x1="0" y1="0" x2=".35" y2="1"><stop offset="0" stop-color="#4E3D33"/>'
               f'<stop offset=".55" stop-color="#1E1511"/><stop offset="1" stop-color="#120C0A"/></linearGradient></defs>')
    out.append(f'<g transform="translate({_f(hx)},{_f(hy)}) rotate({_f(th)})">'
               # barbed hypostome into the skin, then the base of the mouthparts
               '<path d="M-3,-.4 L-19,2.4 L-3,2.6Z" fill="#2A1D17"/>'
               '<path d="M-8,0.4 l-1.2,1.6 M-12,1.1 l-1.2,1.5 M-16,1.8 l-1.1,1.2" stroke="#2A1D17" stroke-width=".6"/>'
               '<rect x="-4.8" y="-3" width="8.4" height="6" rx="1.7" fill="#1A1210"/>'
               f'<path d="{body}" fill="url(#{uid}b)"/>'
               f'<g clip-path="url(#{uid}c)">'
               # marginal groove behind the shield, kept faint
               '<path d="M15.5,-1.4 C21,-3 28,-3 33.5,-.8" stroke="#6A2014" stroke-width=".7" fill="none" opacity=".45"/>'
               # the shield (scutum): a solid dark cap over the front third of the back, its rear edge
               # bowed toward the middle of the body like the plate seen from above, not a thin band
               f'<path d="M-3,6 L2.2,4.6 C9,4.6 15.6,1.6 16.4,-4 C16.8,-7 16.6,-9.6 16.9,-12 L-3,-12Z" fill="url(#{uid}s)"/>'
               '<path d="M5.2,-4.6 Q8.6,-8.4 13.6,-8.9" stroke="#7A6656" stroke-width=".9" fill="none" '
               'stroke-linecap="round" opacity=".5"/>'
               '</g>'
               f'<path d="{body}" fill="none" stroke="{k["body"][2]}" stroke-width=".8"/>'
               f'<ellipse cx="25" cy="-5" rx="6.5" ry="2.2" fill="url(#{uid}g)" opacity=".4"/>'
               '</g>')
    # palps resting on the skin, just ahead of the bite
    out.append(f'<path d="M{_f(hx - 1)},{_f(sk - 1.6)} C{_f(hx - 4.5)},{_f(sk - 3)} {_f(hx - 8.6)},{_f(sk - 1.6)} '
               f'{_f(hx - 9)},{_f(sk - .2)} H{_f(hx - 1)}Z" fill="#1A1210"/>')
    return "".join(out)


# ============================================================ other art helpers
def leaf(x, y, length, ang, uid="lyl"):
    """A broad leaf from its stem point (x, y), pointing along ang degrees."""
    L = length
    veins = []
    for i in range(1, 6):
        u = i / 6.4
        veins.append(f"M{_f(L * u)},{_f(-L * .012 * math.sin(math.pi * u))} q{_f(L * .07)},{_f(-L * .09)} {_f(L * .15)},{_f(-L * .15 * (1 - u * .55))}")
        veins.append(f"M{_f(L * u)},{_f(-L * .012 * math.sin(math.pi * u))} q{_f(L * .07)},{_f(L * .07)} {_f(L * .14)},{_f(L * .12 * (1 - u * .55))}")
    return (f'<defs><linearGradient id="{uid}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#86C463"/>'
            f'<stop offset="1" stop-color="#3D8A33"/></linearGradient></defs>'
            f'<g transform="translate({_f(x)},{_f(y)}) rotate({_f(ang)})">'
            f'<path d="M{_f(-L * .13)},{_f(L * .05)} L0,0" stroke="#3E7A2C" stroke-width="3" stroke-linecap="round"/>'
            f'<path d="M0,0 C{_f(L * .2)},{_f(-L * .27)} {_f(L * .64)},{_f(-L * .31)} {_f(L)},0 '
            f'C{_f(L * .62)},{_f(L * .23)} {_f(L * .19)},{_f(L * .21)} 0,0Z" fill="url(#{uid})" stroke="#357A2B" stroke-width="1"/>'
            f'<path d="M0,0 Q{_f(L * .5)},{_f(-L * .03)} {_f(L * .98)},0" stroke="#2E6B25" stroke-width="1.4" fill="none"/>'
            f'<path d="{" ".join(veins)}" stroke="#2E6B25" stroke-width=".8" fill="none" opacity=".65"/></g>')


def spirochete(x, y, length, rot=0.0, waves=7, amp=3.2, back="#1B3A73", front="#3B76C6", shine="#B9D2F3"):
    """Borrelia: a long, thin corkscrew (helical) bacterium, tapered at both ends.  Drawn as a
    helix whose axis leans a little toward the viewer: each turn's BACK half (dark, thinner) is
    drawn first and its FRONT half (lighter, with a shine line) over it, so the coil reads in depth
    instead of as a flat wave."""
    lean = .35                                  # sin of the axis tilt: front half-turns lean forward

    def pt(u):
        taper = math.sin(math.pi * u) ** .6     # 0 at both tips
        ph = 2 * math.pi * waves * u
        r = amp * taper
        return length * u + lean * r * math.sin(ph), -r * math.cos(ph), taper

    halves = []
    for k in range(2 * waves):                  # one path per half-turn
        u0, u1 = k / (2 * waves), (k + 1) / (2 * waves)
        ps = [pt(u0 + (u1 - u0) * j / 12) for j in range(13)]
        tm = pt((u0 + u1) / 2)[2]
        halves.append((k % 2 == 0, ps, tm))     # sin(phase) > 0 on even half-turns = front
    out = [f'<g transform="translate({_f(x)},{_f(y)}) rotate({_f(rot)})" fill="none" stroke-linecap="round" stroke-linejoin="round">']
    for is_front, ps, tm in halves:             # back halves first
        if not is_front:
            d = "M" + " L".join(f"{_f(a)},{_f(b)}" for a, b, _ in ps)
            out.append(f'<path d="{d}" stroke="{back}" stroke-width="{_f(.45 + 1.2 * tm)}"/>')
    for is_front, ps, tm in halves:
        if is_front:
            d = "M" + " L".join(f"{_f(a)},{_f(b)}" for a, b, _ in ps)
            out.append(f'<path d="{d}" stroke="{front}" stroke-width="{_f(.6 + 1.6 * tm)}"/>')
            if tm > .45:
                hi = "M" + " L".join(f"{_f(a - .25)},{_f(b - .5 * tm)}" for a, b, _ in ps[3:10])
                out.append(f'<path d="{hi}" stroke="{shine}" stroke-width=".6" opacity=".9"/>')
    out.append("</g>")
    return "".join(out)


def card(x, y, w, h, title, head_fill, body_fill="#FFFFFF", border=None, title_fill="#FFFFFF"):
    """A rounded card with a coloured header strip (title sits on clear colour, never on art)."""
    border = border or head_fill
    return (f'<rect x="{_f(x)}" y="{_f(y)}" width="{_f(w)}" height="{_f(h)}" rx="8" fill="{body_fill}" stroke="{border}" stroke-width="1.6"/>'
            f'<path d="M{_f(x + .8)},{_f(y + 22)} V{_f(y + 8)} a7.2,7.2 0 0 1 7.2,-7.2 H{_f(x + w - 8)} a7.2,7.2 0 0 1 7.2,7.2 '
            f'V{_f(y + 22)}Z" fill="{head_fill}"/>'
            + T(x + 10, y + 15.4, title, 10, 800, title_fill, ls=0.9))


def arrow(d, col, w=3.2):
    return f'<path d="{d}" stroke="{col}" stroke-width="{w}" fill="none" stroke-linecap="round" marker-end="url(#ah)"/>'


# ============================================================ HOW IT SPREADS
def art_spread(t):
    W, H = 735, 222
    out = [defs()]
    # 1. waits on a leaf, with tall grass behind it.  CDC "How Ticks Spread Disease": ticks
    # wait "questing", holding leaves and grass with the third and fourth pairs of legs and
    # "the first pair of legs outstretched, waiting to climb onto the host".
    # the blades fade out at the bottom (no cut-off ends, no ground needed)
    out.append('<defs><linearGradient id="lygf" gradientUnits="userSpaceOnUse" x1="0" y1="58" x2="0" y2="92">'
               '<stop offset="0" stop-color="#fff"/><stop offset="1" stop-color="#000"/></linearGradient>'
               '<mask id="lygm"><rect x="0" y="0" width="60" height="96" fill="url(#lygf)"/></mask></defs><g mask="url(#lygm)">')
    for d, c in (("M5.5,92 C7,68 10,42 16,15 C13.6,42 11.4,68 10,92Z", "#5E9E43"),
                 ("M10.5,92 C17,71 28,49 41,29 C31,50 21.5,72 15,92Z", "#4E8B37"),
                 ("M2.5,92 C2.6,78 3.4,64 5.6,50 C5.9,65 6.2,79 6.4,92Z", "#73B254")):
        out.append(f'<path d="{d}" fill="{c}"/>')
    out.append('</g>')
    out.append(leaf(20, 74, 114, -21, "lyleaf"))
    out.append(tick_top("deer", 109, 33, 0.44, 69, "lyq", quest=True, shadow=False))
    out.append(T(146, 31, "WAITS", 11, 800, INK, ls=1))
    out.append(T(146, 44.5, ["on grass and leaves,", "front legs reaching out"], 10, 600, SOFT_INK, lh=1.15))
    # 2. climbs on
    out.append(arrow("M30,86 C16,106 18,126 40,140", SLATE))
    out.append(tick_top("deer", 86, 138, 0.92, 0, "lyb"))
    out.append(T(86, 179.5, "TICK", 11, 800, INK, "middle", ls=1))
    out.append(T(86, 192.5, ["Climbs on", "as you pass"], 10, 600, SOFT_INK, "middle", lh=1.15))
    # 3. bites and feeds: skin cut away to show the mouthparts in it
    out.append(arrow("M130,140 H150", SLATE))
    sx0, sx1, sy0, sy1 = 158, 272, 128, 166
    out.append(f'<defs><linearGradient id="lyskin" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#EDB596"/>'
               f'<stop offset="1" stop-color="#E29F80"/></linearGradient></defs>'
               f'<rect x="{sx0}" y="{sy0}" width="{sx1 - sx0}" height="{sy1 - sy0}" rx="6" fill="url(#lyskin)"/>'
               f'<path d="M{sx0},{sy0 + 6} a6,6 0 0 1 6,-6 H{sx1 - 6} a6,6 0 0 1 6,6 V{sy0 + 9} H{sx0}Z" fill="#F7D6C0"/>'
               f'<path d="M{sx0 + 6},{sy0} H{sx1 - 6}" stroke="#D29B7B" stroke-width="1.2"/>'
               # a small blood vessel in the dermis, labelled where the line ends
               f'<path d="M{sx0 + 4},{sy1 - 7} C{sx0 + 14},{sy1 - 10.5} {sx0 + 26},{sy1 - 5} {sx0 + 38},{sy1 - 8}" '
               f'stroke="#C0564B" stroke-width="2.2" fill="none" stroke-linecap="round" opacity=".8"/>')
    out.append(T(sx1 - 8, sy0 + 18, "SKIN", 9.6, 800, "#8A4A30", "end", ls=1))
    out.append(T(sx1 - 8, sy1 - 6, "blood vessel", 9.6, 600, "#9A3D33", "end"))
    out.append(tick_feeding(210, sy0 - 0.6, "lyfeed"))
    out.append(T(215, 179.5, "BITE", 11, 800, INK, "middle", ls=1))
    # CDC Transmission: "In most cases, the tick must be attached for 36 to 48 hours
    # or more before the Lyme disease bacterium can be transmitted."  Faster germs:
    # Powassan virus can pass "as quickly as 15 minutes after tick attachment"
    # (CDC MMWR 2017;66(15):408-409, citing Ebel and Kramer 2004).
    out.append(TR(215, 192.5, ["Lyme usually needs 36+ hours;", "some other germs pass faster.",
                               "*Remove ticks right away.*"], 10, 600, SOFT_INK, "middle", lh=1.15, bold=700, bold_fill=INK))
    # 4. what one bite can pass on
    out.append(arrow("M278,134 C290,132 292,70 306,66", SLATE))
    out.append(arrow("M278,146 C291,146 294,171 306,172", SLATE))
    # Lyme disease card
    out.append(card(314, 6, 160, 116, "LYME DISEASE", SLATE))
    out.append('<rect x="324" y="36" width="140" height="48" rx="6" fill="#E9EFF7"/>')
    for sx, sy, ln, rot, wv in ((332, 47, 88, -2, 7), (366, 60, 90, 2, 7), (338, 74, 74, -1.5, 6)):
        out.append(spirochete(sx, sy, ln, rot, wv, amp=3.0))
    out.append(T(394, 101, "Borrelia burgdorferi", 10.4, 700, INK, "middle", italic=True))
    out.append(T(394, 114, "the Lyme bacterium", 9.6, 600, SOFT_INK, "middle"))
    # Georgia card.  "The (lone star tick) is the most common tick in Georgia" (UGA entomologist
    # Nancy Hinkle, UGA CAES Newswire, "Ticks in Georgia", story 5470; the UGA Extension Field
    # Report "Summertime is tick time in Georgia" says the same).  UGA Extension Circular 937,
    # "Protect Yourself from Ticks", names the lone star, American dog and blacklegged ticks as
    # the three species most associated with people in Georgia, so deer ticks live here too.
    # CDC (STARI; Regions Where Ticks Live): the lone star tick is not known to spread the Lyme
    # bacterium.  Georgia is a low-incidence Lyme state in CDC surveillance.
    out.append(card(484, 6, 247, 116, "IN GEORGIA", SLATE_MID, PALE, border="#D3DADE"))
    out.append(TR(495, 48.5, ["Lyme is reported far less here than in", "the Northeast, but deer ticks live here",
                              "too. The tick people meet most here", "is the *lone star tick*, which is not",
                              "known to spread Lyme."], 11, 500, "#33404A", lh=1.32, bold=700, bold_fill=INK))
    # other infections card.  CDC "Regions Where Ticks Live", blacklegged (deer) tick: it also
    # spreads anaplasmosis (Anaplasma phagocytophilum, a bacterium), babesiosis (Babesia microti,
    # a parasite), Borrelia miyamotoi disease (a bacterium) and Powassan virus disease (a virus).
    # The western blacklegged tick spreads only anaplasmosis and B. miyamotoi besides Lyme, so
    # the title names deer ticks rather than "the same ticks" (which would take in the western one).
    ox, oy, ow, oh = 314, 134, 417, 83
    out.append(card(ox, oy, ow, oh, "OTHER INFECTIONS DEER TICKS CAN CARRY", SLATE))
    out.append(f'<path d="M{_f(ox + ow / 2)},{oy + 29} V{oy + oh - 8} M{ox + 14},{_f(oy + 22 + (oh - 22) / 2)} H{ox + ow - 14}" '
               'stroke="#E1E6E9" stroke-width="1"/>')
    items = [("Anaplasmosis", "bacterium"), ("Babesiosis", "parasite"),
             ('<tspan font-style="italic">B. miyamotoi</tspan> disease', "bacterium"), ("Powassan virus disease", "virus")]
    for i, (name, kind) in enumerate(items):
        cx = ox + ow / 4 * (1 + 2 * (i % 2))
        by = oy + 22 + (oh - 22) / 4 * (1 + 2 * (i // 2)) + 4
        out.append(f'<text x="{_f(cx)}" y="{_f(by)}" {FONT} font-size="11" font-weight="700" fill="#33404A" '
                   f'text-anchor="middle">{name}<tspan dx="7" font-size="9.6" font-weight="600" font-style="italic" '
                   f'fill="#5F6A71">{kind}</tspan></text>')
    return svg(W, H, "".join(out), "How a tick bite spreads Lyme disease and other infections")


# ============================================================ SYMPTOMS (body)
HEAD = ("M0,0 C8.4,0 13.8,6.4 13.8,16.4 C13.8,24 11.8,30.4 8.5,34.9 C6.3,37.9 3.5,40 0,40 "
        "C-3.5,40 -6.3,37.9 -8.5,34.9 C-11.8,30.4 -13.8,24 -13.8,16.4 C-13.8,6.4 -8.4,0 0,0Z")
# right half of neck, torso and leg (x >= 0), top to toe and back up the inner leg
BODY_R = [(8.4, 33.4),
          ((8.6, 40), (8.9, 44), (9.6, 47.2)),
          ((13, 51.4), (21, 52.6), (28, 55)),
          ((34, 57), (37, 62.5), (37.2, 70)),
          ((37.3, 76), (33, 80), (31, 84)),
          ((31.6, 96), (30.2, 108), (26.6, 119)),
          ((25.6, 127), (31.6, 140), (32.6, 153)),
          ((33.6, 166), (31.2, 185), (28.2, 203)),
          ((26.6, 212), (25.2, 218), (25.2, 224)),
          ((25.6, 234), (28.2, 244), (27.7, 255)),
          ((27.2, 266), (22.7, 277), (21.6, 287)),
          ((21.6, 291), (25.6, 294), (25.6, 297.6)),
          ((25.6, 300.6), (19, 301), (14, 300.6)),
          ((10.6, 300.3), (9.1, 298), (9.4, 294)),
          ((9.7, 290), (9.6, 286), (9.1, 280)),
          ((8.1, 268), (7.1, 258), (7.3, 247)),
          ((7.5, 238), (5.1, 230), (4.7, 223)),
          ((4.1, 210), (2.9, 190), (2.1, 175)),
          ((1.7, 168), (0.8, 164), (0, 163))]
ARM_R = ("M27.5,55.5 C33.5,56 38.5,60 39.5,68 C40.8,78 41.5,90 42.8,103 C43.6,111 44.6,116 45.6,121 "
         "C47.4,129 49,138 50,149 C50.8,156 51.5,160 52.2,164 C54.6,167 56,173 55.6,180 C55.2,187 53.4,193 50.2,194 "
         "C47.6,194.6 45.8,191 45.6,186 C45.4,180 45.2,173 45.4,166 C45.4,162 44.6,158 44,153 C42.8,143 40.6,134 38.6,126 "
         "C37.8,122 37,118 36.4,113 C35.2,104 33.4,95 31.2,86 C30.2,80 29.2,74 28.4,69 C27.6,63 26.6,58 27.5,55.5Z")


def _body_path():
    """Mirror BODY_R into one closed, symmetric outline."""
    start, segs = BODY_R[0], BODY_R[1:]
    d = [f"M{_f(start[0])},{_f(start[1])}"]
    for c1, c2, p in segs:
        d.append(f"C{_f(c1[0])},{_f(c1[1])} {_f(c2[0])},{_f(c2[1])} {_f(p[0])},{_f(p[1])}")
    pts = [start] + [sg[2] for sg in segs]
    for i in range(len(segs) - 1, -1, -1):
        c1, c2, _ = segs[i]
        p = pts[i]
        d.append(f"C{_f(-c2[0])},{_f(c2[1])} {_f(-c1[0])},{_f(c1[1])} {_f(-p[0])},{_f(p[1])}")
    return " ".join(d) + "Z"


def _mirror_path(d):
    """Negate every x in an absolute M/C/Z path."""
    out, toks = [], d.replace(",", " ").split()
    i, cmd = 0, ""
    while i < len(toks):
        tk = toks[i]
        if tk[0].isalpha():
            cmd = tk[0]
            out.append(cmd)
            rest = tk[1:]
            if rest:
                toks.insert(i + 1, rest)
            i += 1
            continue
        if cmd in "MCL":
            out.append(f"{_f(-float(tk))},{toks[i + 1]}")
            i += 2
        else:
            i += 1
    return " ".join(out)


def human(cx, top, s, uid="lyh"):
    """A standing figure, front view, 7.5 heads tall (300 units), arms slightly out."""
    body, arm = _body_path(), ARM_R
    arm_l = _mirror_path(arm)
    shapes = [HEAD, body, arm, arm_l]
    ears = '<ellipse cx="13.6" cy="21" rx="2.3" ry="4.4"/><ellipse cx="-13.6" cy="21" rx="2.3" ry="4.4"/>'
    # one gradient in figure units (userSpaceOnUse) shared by every part, so the shading runs on
    # across the neck and shoulders instead of restarting inside each shape
    out = [f'<defs><linearGradient id="{uid}" gradientUnits="userSpaceOnUse" x1="-56" y1="0" x2="56" y2="0">'
           f'<stop offset="0" stop-color="{SKIN[1]}"/><stop offset=".5" stop-color="{SKIN[0]}"/>'
           f'<stop offset="1" stop-color="{SKIN[1]}"/></linearGradient></defs>',
           f'<g transform="translate({_f(cx)},{_f(top)}) scale({s})">',
           # pass 1: outline (stroked union), pass 2: fill on top = one clean silhouette
           f'<g fill="{SKIN[2]}" stroke="{SKIN[2]}" stroke-width="2.4" stroke-linejoin="round">'
           + "".join(f'<path d="{p}"/>' for p in shapes) + ears + "</g>",
           f'<g fill="url(#{uid})">' + "".join(f'<path d="{p}"/>' for p in shapes) + ears + "</g>",
           # quiet anatomy: collarbones, navel, kneecaps
           f'<g fill="none" stroke="{SKIN[2]}" stroke-width=".9" stroke-linecap="round" opacity=".5">'
           '<path d="M-23,58.5 C-15,56.6 -8,58.6 -3.4,61"/><path d="M23,58.5 C15,56.6 8,58.6 3.4,61"/>'
           '<path d="M-9.6,221 Q-14.9,226 -20.4,221"/><path d="M9.6,221 Q14.9,226 20.4,221"/></g>'
           f'<ellipse cx="0" cy="128" rx="1.3" ry="1.7" fill="{SKIN[2]}" opacity=".6"/>',
           "</g>"]
    return "".join(out)


def rash_patch(x, y, rx, ry, uid="lyrp", rot=-12):
    """Erythema migrans as it most often looks: a solid, evenly red, expanding oval with a crisp
    edge, a faint clearing at most, and the bite in the middle.  CDC: the rash "sometimes clears
    as it enlarges, resulting in a target or bull's-eye appearance" and "does not always appear
    as a classic erythema migrans rash"."""
    return (f'<defs><radialGradient id="{uid}"><stop offset="0" stop-color="#fff" stop-opacity=".3"/>'
            f'<stop offset=".55" stop-color="#fff" stop-opacity=".1"/><stop offset="1" stop-color="#fff" stop-opacity="0"/>'
            f'</radialGradient></defs>'
            f'<g transform="translate({_f(x)},{_f(y)}) rotate({rot})">'
            f'<ellipse rx="{_f(rx)}" ry="{_f(ry)}" fill="{RASH}" fill-opacity=".86" stroke="#A9352C" stroke-width=".9"/>'
            f'<ellipse rx="{_f(rx * .55)}" ry="{_f(ry * .55)}" fill="url(#{uid})"/>'
            f'<circle r="{_f(max(.8, rx * .09))}" fill="#7E231C"/></g>')


def bullseye(x, y, r):
    """The bull's-eye form of erythema migrans: red ring, clearer middle, red centre."""
    return (f'<circle cx="{_f(x)}" cy="{_f(y)}" r="{_f(r)}" fill="{RASH}" fill-opacity=".14" stroke="{RASH}" '
            f'stroke-width="{_f(r * .36)}" stroke-opacity=".9"/>'
            f'<circle cx="{_f(x)}" cy="{_f(y)}" r="{_f(r * .34)}" fill="{RASH}" fill-opacity=".9"/>')


def dot(x, y, col, r=4.3):
    return f'<circle cx="{_f(x)}" cy="{_f(y)}" r="{r}" fill="{col}" stroke="#fff" stroke-width="1.6"/>'


def art_symptoms(t):
    W, H = 444, 332
    cx, top, s = 222, 37, 0.96

    def at(lx, ly):
        return cx + lx * s, top + ly * s

    out = [defs()]
    # column heads.  CDC, Signs and Symptoms of Untreated Lyme Disease: early signs
    # "3 to 30 days after tick bite"; later signs "days to months after tick bite".
    out.append(T(150, 15, "EARLY SIGNS", 10.4, 800, EARLY, "end", ls=1))
    out.append(T(150, 28, "3 to 30 days after the bite", 9.6, 600, SOFT_INK, "end"))
    out.append(T(294, 15, "LATER SIGNS", 10.4, 800, LATER_TXT, ls=1))
    out.append(T(294, 28, "days to months, if untreated", 9.6, 600, SOFT_INK))
    out.append(human(cx, top, s))
    rash = at(-15, 140)
    out.append(rash_patch(rash[0], rash[1], 11.5, 9.4))
    # (lines, first baseline, target).  Left = early (CDC early list), right = later.
    early = [(["Fever, chills, headache", "and tiredness"], 50, at(-7, 15)),
             (["Swollen lymph nodes"], 84, at(-7.5, 42)),
             (["Muscle and joint aches"], 114, at(-33, 63)),
             (["Expanding rash, sometimes", "like a bull's-eye"], 156, (rash[0] - 11.2, rash[1] + 1.5))]
    later = [(["Face droop (palsy), bad", "headache, stiff neck"], 50, at(7.5, 24)),
             (["Pounding or skipped", "heartbeat (Lyme carditis)"], 112, at(10, 88)),
             (["Nerve pain, numbness or", "tingling in hands or feet"], 190, at(50.5, 180)),
             (["Arthritis: swollen joints,", "most often the knees"], 244, at(15, 222)),
             (["More rashes on other", "parts of the body"], 288, at(17, 262))]
    for lines, by, (px, py) in early:
        ly = by - 3.6
        out.append(f'<path d="M154,{_f(ly)} L{_f(px)},{_f(py)}" stroke="{EARLY}" stroke-width="1.3" fill="none"/>')
        if not lines[0].startswith("Expanding"):      # the rash leader ends on the rash itself
            out.append(dot(px, py, EARLY))
        out.append(T(150, by, lines, 10.6, 700, INK, "end", lh=1.2))
    for lines, by, (px, py) in later:
        ly = by - 3.6
        out.append(f'<path d="M290,{_f(ly)} L{_f(px)},{_f(py)}" stroke="{LATER}" stroke-width="1.3" fill="none"/>')
        out.append(dot(px, py, LATER))
        out.append(T(294, by, lines, 10.6, 700, INK, lh=1.2))
    # KEY (Asher: "Have a key. Purple means this...")
    kx, ky, kw, kh = 6, 232, 178, 92
    out.append(f'<rect x="{kx}" y="{ky}" width="{kw}" height="{kh}" rx="8" fill="#FFFFFF" stroke="#CFD6DA" stroke-width="1.3"/>')
    out.append(T(kx + 11, ky + 17, "KEY", 9.6, 800, INK, ls=1.4))
    stub = '<path d="M{0},{1} H{2}" stroke="{3}" stroke-width="1.3"/>'
    rows = [(stub.format(kx + 10, ky + 35, kx + 22, EARLY) + dot(kx + 22, ky + 35, EARLY), "Early sign"),
            (stub.format(kx + 10, ky + 55, kx + 22, LATER) + dot(kx + 22, ky + 55, LATER), "Later sign")]
    for i, (sw, lab) in enumerate(rows):
        out.append(sw)
        out.append(T(kx + 36, ky + 38.6 + i * 20, lab, 10.4, 600, INK))
    out.append(rash_patch(kx + 16, ky + 76, 7, 5.6, "lyrpk", rot=0) + bullseye(kx + 33.5, ky + 76, 6.4))
    out.append(T(kx + 46, ky + 73.4, "Rash at the bite:", 10.4, 600, INK))
    out.append(T(kx + 46, ky + 85, "plain red or bull's-eye", 9.6, 600, SOFT_INK))
    return svg(W, H, "".join(out), "Early and later signs of Lyme disease on the body, with a key")


# ============================================================ actual size + tick cards
MM = 96 / 25.4    # CSS px per millimetre (1 in = 96 px), so this strip prints true to size


def art_actual_size():
    """Nymph and adult female deer tick at true printed size.  Sizes: CDC (nymph about
    the size of a poppy seed, under 2 mm); adult female about the size of a sesame
    seed, roughly 3 mm long with mouthparts before feeding (UMN Extension, CDC)."""
    W, H = 248, 42
    out = [T(1, 15, "ACTUAL SIZE", 9.6, 800, SLATE, ls=1.2), T(1, 29, "deer tick", 9.6, 600, SOFT_INK)]
    # scale each drawing so its palp-tip-to-rear length (tick_len: 43.9 units for the
    # nymph, 54.9 for the adult) prints at the real length
    nym = 1.5 * MM / tick_len("nymph")    # nymph with mouthparts about 1.5 mm
    adu = 3.0 * MM / tick_len("deer")     # unfed adult female about 3 mm
    out.append(tick_top("nymph", 96, 20, nym, 0, "lyan", shadow=False, minw=0.45))
    out.append(T(105, 24.5, "nymph", 10, 700, INK))
    out.append(T(105, 36, "poppy seed", 9.6, 600, SOFT_INK))
    out.append(tick_top("deer", 172, 19, adu, 0, "lyaa", shadow=False, minw=0.5))
    out.append(T(183, 24.5, "adult", 10, 700, INK))
    out.append(T(183, 36, "sesame seed", 9.6, 600, SOFT_INK))
    return svg(W, H, "".join(out), "Actual size of a deer tick nymph and adult")


def art_tick_card(kind, uid):
    W, H = 76, 84
    s = {"deer": 0.95, "western": 0.92, "lonestar": 0.92}[kind]
    return svg(W, H, tick_top(kind, 38, 45, s, 0, uid), f"{kind} tick, adult female, seen from above")


# ============================================================ front page
CSS = r"""
.ly-front{display:flex;flex-direction:column}
.ly-front .ly-h{font:900 12pt Merriweather,Georgia,serif;color:var(--c1);letter-spacing:.02em;margin:0.03in 0 0.02in}
.ly-front .ly-art svg{display:block;width:100%;height:auto}
.ly-front .ly-grid{display:grid;grid-template-columns:4.625in 1fr;gap:0.14in;align-items:stretch}
.ly-front .ly-notes{display:flex;flex-direction:column;justify-content:space-between;gap:0.07in}
.ly-front .ly-nt{border-left:4px solid #5D6B74;background:#F2F4F5;padding:0.06in 0.11in 0.07in;font-size:9pt;line-height:1.4;
  border-radius:0 6px 6px 0;color:#2B3236}
.ly-front .ly-nt b{color:#1F2A2E}
.ly-front .ly-nt svg{display:block;width:2.5833in;height:auto;margin:0.05in 0 0}
.ly-front .ly-tks{display:grid;grid-template-columns:repeat(3,1fr);gap:0.1in}
.ly-front .ly-tk{background:#F2F4F5;border-radius:8px;padding:0.03in 0.1in 0.03in 0.02in;display:flex;gap:4px;align-items:center}
.ly-front .ly-tk svg{flex:none;width:0.7917in;height:auto}
.ly-front .ly-tk b{display:block;font-size:8.8pt;color:#1F2A2E;line-height:1.2}
.ly-front .ly-tk span{display:block;font-size:7.8pt;color:#3A4247;line-height:1.28;margin-top:1px}
/* BACK PAGE.  Every rule is scoped by the empty .ly-back marker in life_title, so it touches
   only this sheet's back, in its own file and in the all-sheets bundle. */
/* the life icons keep their 0.6 in size inside a shorter box (the page needs the room) */
.sheet.back:has(.ly-back) .icons5 .life .disc2{height:0.56in}
.sheet.back:has(.ly-back) .icons5 .life .disc2 svg{width:0.54in!important;height:0.54in!important}
.sheet.back:has(.ly-back) .ns-title{margin-top:0.1in}
/* dose bands: a little more width so "2 to 3 hours from doxycycline" stays on one line */
.sheet.back:has(.ly-back) .col .dose{padding-left:0.025in;padding-right:0.025in}
/* products section: say the frame out loud.  The kit's generic subtitle is not rendered
   (display:none, so it is not in the PDF either) and the sheet's own line takes its place:
   "Recovery support", antibiotics first.  Same line in both editions. */
.sheet.back:has(.ly-back) .ns-title span{display:none}
.sheet.back:has(.ly-back) .ns-title::after{content:"Recovery support. Antibiotics prescribed by your clinician come first.";
  font:700 8pt Inter,sans-serif;color:var(--deep);letter-spacing:.02em}
"""


def front(t, ed):
    notes = (
        # CDC: people treated with appropriate antibiotics in the early stages usually recover rapidly and completely.
        '<div class="ly-nt"><b>See a clinician promptly</b> if a rash, fever, aches or swollen joints follow a tick '
        'bite or time outdoors. Early antibiotics work best.</div>'
        # CDC: the erythema migrans rash "occurs in approximately 70 to 80 percent of
        # infected persons" and only "sometimes" clears into a bull's-eye.
        '<div class="ly-nt"><b>Not everyone sees the tick.</b> Nymphs are poppy-seed small. Up to 3 in 10 '
        'people never get a rash, and many rashes are plain red, not a bull\'s-eye. Early Lyme can pass for the flu.'
        f'{art_actual_size()}</div>'
        # CDC: some people have pain, fatigue or difficulty thinking for more than
        # 6 months after treatment (post-treatment Lyme disease syndrome).  No product
        # claim here: the back page is structure/function only ({who} = edition token).
        '<div class="ly-nt"><b>After treatment,</b> some people have tiredness, pain or brain fog that lingers for '
        'months. That stretch is a good time to focus on food, sleep and steady habits. Ask {who} which '
        'support fits you.</div>')
    # tick ranges and diseases: CDC Regions Where Ticks Live; UGA Extension for Georgia.
    # Western vs deer: the two Ixodes species look nearly identical, so range is the clue.
    ticks = [("deer", "Blacklegged (deer) tick",
              "Black legs and shield, red-orange body. Eastern U.S., Georgia included. The main Lyme carrier."),
             ("western", "Western blacklegged tick",
              "Looks almost the same as the deer tick, so where you live is the best clue: Pacific coast states. "
              "It also spreads Lyme."),
             ("lonestar", "Lone star tick",
              "White dot on the female's back. Spreads ehrlichiosis and can trigger alpha-gal (red-meat) allergy.")]
    cards = "".join(f'<div class="ly-tk">{art_tick_card(k, "lyk" + k)}<div><b>{n}</b><span>{d}</span></div></div>'
                    for k, n, d in ticks)
    return ('<div class="ly-front">'
            '<h3 class="ly-h">HOW IT SPREADS</h3>'
            f'<div class="ly-art">{art_spread(t)}</div>'
            '<h3 class="ly-h">SYMPTOMS</h3>'
            f'<div class="ly-grid"><div class="ly-art">{art_symptoms(t)}</div><div class="ly-notes">{notes}</div></div>'
            '<h3 class="ly-h">KNOW YOUR TICKS <small style="font:600 7.8pt Inter,sans-serif;color:#5B666D;letter-spacing:0">'
            'adult females shown</small></h3>'
            f'<div class="ly-tks">{cards}</div></div>')


SHEET = {
    "slug": "lyme", "code": "ND-IM-301", "order": 8, "theme": "immune", "series": "Immune Health Series",
    "title": "Lyme Disease", "sub": "and other tickborne infections",
    # CDC: Lyme disease is the most common vector-borne disease in the U.S.; an
    # estimated 476,000 people are diagnosed and treated each year (Kugeler et al.,
    # Emerg Infect Dis 2021, insurance claims 2010-2018).  Caused by Borrelia
    # burgdorferi (rarely B. mayonii), spread by blacklegged ticks.
    "intro": ("Lyme disease is the most common illness spread by ticks in the U.S.: an estimated <b>476,000 Americans</b> "
              "are diagnosed and treated for it each year. <i>Borrelia</i> bacteria pass from the bite of an infected "
              "blacklegged (deer) tick, and the same tick can carry other germs too. Avoiding bites is the best defense; "
              "early treatment is the next best."),
    "front": front,
    "css": CSS,
    # BACK PAGE (back-page pass, 2026-11-03).  Framed as RECOVERY SUPPORT for gut, immune,
    # inflammatory balance, detox (die-off) and energy, in structure/function words only: no product
    # here treats Lyme, and "Antibiotics prescribed by your clinician come first" heads the products.
    # Five columns, the competitor's count.  Picks follow NutriDyn's own protocols first:
    #   Immune PRP Pro and Liposomal Glutathione: Jocelyn Strand ND, NutriDyn GLC 2019 "Botanical
    #     Medicines in Complex, Multi-Pathogen Disease" (Immune Support: Immune PRP Pro 2 capsules
    #     2x/day; Detoxification Support "for herxing": Liposomal Glutathione up to 4x/day).  The sheet
    #     never prints "Lyme" on that protocol: verification found it is not labelled for Lyme.
    #   Inflam-Eze Plus: Dr. Kristi Hughes ND's NutriDyn key ("Botanical Anti-inflam" = Inflam-eze
    #     Plus), Gut-Neuro-Immune Restoration plan, Asher's 2025 fatigue/immune seminar (which covered
    #     tick-borne disease); also the closest NutriDyn match to the competitor's turmeric matrix.
    #   Mito Recharge: the competitor's mitochondrial category (NAC, ALC, ALA) in one NutriDyn formula.
    #   UltraBiotic Daily Multi-Strain (START HERE): gut support during the antibiotics that come first;
    #     its S. boulardii is a yeast, which antibacterial antibiotics do not kill (sell sheet ND460
    #     cites McFarland 2010).  It stands in for the competitor's herbal antimicrobial, which on a
    #     Lyme sheet would read as treating the infection.
    # Label facts, sizes and links: products.d/lyme.json (each entry has its "src").
    # Lifestyle sources:
    #   permethrin on clothing and gear; EPA-registered DEET, picaridin, IR3535 or oil of lemon
    #   eucalyptus; tumble dry on HIGH for 10 minutes; shower within 2 hours of coming indoors;
    #   check under the arms, in and around the ears and hair, the waist, behind the knees, and
    #   pets: CDC "Preventing Tick Bites on People".  Light colours and pants tucked into socks:
    #   CDC/NIOSH tick-borne disease guidance for outdoor workers.
    #   Fine-tipped tweezers close to the skin, pull upward with steady pressure: CDC "Removing a
    #   Tick"; tell the doctor when and where the bite happened: CDC "Symptoms of Tickborne Illness".
    #   "Worse at first?": the Jarisch-Herxheimer reaction comes within 24 hours of starting
    #   antibiotics in 7 to 30% of treated Lyme patients and usually passes within a day (Butler T,
    #   Am J Trop Med Hyg 2017;96(1):46-52; StatPearls NBK557820).  Asher's own Herx explainer
    #   (Gmail 17541a5df3e6e6e5, 2020): "feeling worse before feeling better", and "the biggest
    #   problem ... is that people stop taking the supplement or medication".  So: keep the
    #   antibiotic, call the clinician.  The protocols' "go slow" advice (titrate slowly) is the
    #   kit's own rhythm line: start with the Start here pick, add one product a week.
    # Check-panel sources:
    #   Doxycycline label: "Absorption of tetracyclines is impaired by antacids containing aluminum,
    #   calcium, or magnesium ... and iron-containing preparations"; NHS doxycycline guidance keeps
    #   iron and zinc 2 hours away; HSE (Ireland) tetracycline guidance: iron 3 hours before or 2 to
    #   3 hours after.  Mito Recharge has 75 mg magnesium per 3 capsules (ND812).  Doxycycline label:
    #   "tetracyclines have been shown to depress plasma prothrombin activity, patients who are on
    #   anticoagulant therapy may require downward adjustment of their anticoagulant dosage."
    #   Vitamin K "can interact with ... warfarin" (NIH ODS vitamin K fact sheet); Mito Recharge has
    #   250 mcg vitamin K1 (ND812).  Willow bark: may raise bleeding risk with warfarin or other
    #   anticoagulants, avoid with salicylate (aspirin) allergy, and children should not take it
    #   (Reye syndrome), per MSKCC "About Herbs: Willow Bark" and MedlinePlus.  Probiotic 2 hours
    #   from each antibiotic dose: common practice with thin evidence (no guideline found), so the
    #   pharmacy line says the pharmacist "may suggest" it.  Doxycycline with milk or colostrum:
    #   overall absorption not significantly affected (doxycycline labelling, via PDR).
    "back": {
        "life_title": 'Lifestyle Recommendations<span class="ly-back"></span>',
        "life_sub": "Avoid the next bite, and pace your recovery",
        "style": "icons",
        "life": [("shirt", "Dress for ticks", "Light colors, long sleeves, pants in socks. Permethrin on gear."),
                 ("drop", "Repellent", "EPA-registered: DEET, picaridin, IR3535 or oil of lemon eucalyptus."),
                 ("dryer", "Dry, then shower", "Dry clothes on high heat for 10 minutes. Shower within 2 hours."),
                 ("ly_check", "Check daily", "Scalp, ears, armpits, waist and behind the knees. Pets, too."),
                 ("ly_tweezers", "Remove it right", "Fine-tipped tweezers at the skin, pull straight up. Note the date."),
                 ("thermo", "Worse at first?", "Can be germs dying off. Keep your antibiotic; call your clinician.")],
        "cols": [
            {"p": "ly_ultrabiotic_dms", "need": "Protect your gut", "needsub": "with <em>S. boulardii</em>", "start": True,
             "bullets": ["Supports a healthy gut microbiome",
                         "<i>S. boulardii</i>, a yeast, is not killed by antibiotics"]},
            {"p": "ly_immune_prp", "need": "Immune readiness", "needsub": "colostrum immunoglobulins",
             "bullets": ["Promotes healthy immune function", "Supports the gut lining"]},
            {"p": "ly_inflam_eze", "need": "Inflammatory balance", "needsub": "ginger, curcumin, boswellia",
             "bullets": ["Promotes healthy inflammatory markers", "Supports joint comfort"]},
            {"p": "ly_glutathione", "need": "Detox support", "needsub": "liposomal glutathione",
             "bullets": ["Supports healthy glutathione levels", "Provides antioxidant and detox support"]},
            {"p": "ly_mito", "need": "Cellular energy", "needsub": "mitochondrial support",
             "bullets": ["Supports your cells' energy production", "Promotes healthy antioxidant status"]},
        ],
        # Pharmacists check interactions and depletions; providers order labs, refer and adjust.
        "rx": {
            "pharmacy": [
                "<b>Doxycycline:</b> take it 2 to 3 hours apart from calcium, magnesium (Mito Recharge has some), "
                "iron, zinc and antacids, which block it.",
                "<b>Probiotic timing:</b> {who} may suggest taking UltraBiotic at least 2 hours apart from each "
                "antibiotic dose.",
                "<b>Blood thinners:</b> doxycycline can make warfarin stronger; the vitamin K1 in Mito Recharge can "
                "make it weaker. Inflam-Eze Plus has aspirin-like willow bark: not for children, teens or aspirin allergy."],
            "practitioner": [
                "<b>Doxycycline:</b> take it 2 to 3 hours apart from calcium, magnesium (Mito Recharge has some), "
                "iron, zinc and antacids, which block it.",
                "<b>Antibiotic days:</b> take UltraBiotic at least 2 hours apart from each antibiotic dose. "
                "{Who} can say how long to continue it.",
                "<b>On warfarin?</b> Doxycycline can make it stronger and Mito Recharge's vitamin K1 weaker, so {who} "
                "may check your INR (a clotting test). Inflam-Eze Plus has aspirin-like willow bark: not for children, "
                "teens or aspirin allergy."],
        },
    },
}
