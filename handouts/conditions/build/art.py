"""Front-page illustrations for the condition sheets.  Hand-built inline SVG so
every label is real text, prints crisp at any size, and carries no third-party
artwork.  Each function returns one <svg>.
"""
import math
import random

FONT = 'font-family="Inter, Helvetica, Arial, sans-serif"'


def T(x, y, lines, size=11, weight=600, fill="#1F2A2E", anchor="start", lh=1.22, italic=False, ls=0):
    if isinstance(lines, str):
        lines = [lines]
    st = ' font-style="italic"' if italic else ""
    lsp = f' letter-spacing="{ls}"' if ls else ""
    out = [f'<text x="{x}" y="{y}" {FONT} font-size="{size}" font-weight="{weight}" fill="{fill}" text-anchor="{anchor}"{st}{lsp}>']
    for i, ln in enumerate(lines):
        dy = 0 if i == 0 else size * lh
        out.append(f'<tspan x="{x}" dy="{dy:.1f}">{ln}</tspan>')
    out.append("</text>")
    return "".join(out)


def defs(*extra):
    return ("<defs>"
            '<marker id="ah" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse">'
            '<path d="M0,0 L10,5 L0,10 z" fill="context-stroke"/></marker>'
            '<marker id="ahb" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="4.2" markerHeight="4.2" orient="auto-start-reverse">'
            '<path d="M0,0 L10,5 L0,10 z" fill="#1E5FA8"/></marker>'
            '<marker id="ahr" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="4.2" markerHeight="4.2" orient="auto-start-reverse">'
            '<path d="M0,0 L10,5 L0,10 z" fill="#C0392B"/></marker>'
            '<marker id="ahg" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="4.2" markerHeight="4.2" orient="auto-start-reverse">'
            '<path d="M0,0 L10,5 L0,10 z" fill="#2E8B57"/></marker>'
            + "".join(extra) + "</defs>")


def svg(w, h, body, label):
    return (f'<svg viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{label}">'
            f"{body}</svg>")


def pill_label(x, y, text, fill, w=None, size=12, color="#fff"):
    w = w or (len(text) * size * 0.58 + 26)
    return (f'<rect x="{x - w / 2:.1f}" y="{y - size * 0.95:.1f}" width="{w:.1f}" height="{size * 1.7:.1f}" rx="{size * 0.85:.1f}" fill="{fill}"/>'
            + T(x, y + size * 0.28, text, size, 700, color, "middle", italic=True))


def nutrient(x, y, sym, col, r=12, square=False):
    shape = (f'<rect x="{x - r}" y="{y - r}" width="{2 * r}" height="{2 * r}" rx="3" fill="{col}" stroke="#fff" stroke-width="2"/>'
             if square else f'<circle cx="{x}" cy="{y}" r="{r}" fill="{col}" stroke="#fff" stroke-width="2"/>')
    fs = 11 if len(sym) == 1 else 9.5
    return shape + T(x, y + fs * 0.36, sym, fs, 800, "#fff", "middle")


def food_bit(x, y, s=1.0, col="#B48A5F"):
    return (f'<path transform="translate({x},{y}) scale({s})" d="M-11,-3 C-12,-11 -2,-14 5,-11 C13,-8 14,1 9,7 C4,12 -6,12 -10,6 C-12,3 -11,0 -11,-3Z" '
            f'fill="{col}" stroke="#8C6440" stroke-width="1"/>')


def bacterium(x, y, rot=0, s=1.0, col="#7DAE5B"):
    legs = "".join(f'<path d="M{-12 + i * 6},-5 l-2,-5 M{-12 + i * 6},5 l-2,5" stroke="#4F7F35" stroke-width="1.2"/>' for i in range(5))
    return (f'<g transform="translate({x},{y}) rotate({rot}) scale({s})">{legs}'
            f'<rect x="-15" y="-6" width="30" height="12" rx="6" fill="{col}" stroke="#4F7F35" stroke-width="1.2"/>'
            f'<circle cx="-6" cy="0" r="1.6" fill="#3E6A28"/><circle cx="3" cy="-1" r="1.6" fill="#3E6A28"/><circle cx="9" cy="1" r="1.4" fill="#3E6A28"/></g>')


def capsule(x, y, rot=0, s=1.0):
    return (f'<g transform="translate({x},{y}) rotate({rot}) scale({s})">'
            f'<rect x="-14" y="-6.5" width="28" height="13" rx="6.5" fill="#fff" stroke="#2B5DA8" stroke-width="1.6"/>'
            f'<path d="M0,-6.5 H7.5 A6.5,6.5 0 0 1 7.5,6.5 H0 Z" fill="#2B5DA8"/></g>')


def rbc(x, y, s=1.0, rot=0):
    return (f'<g transform="translate({x},{y}) rotate({rot}) scale({s})">'
            f'<ellipse rx="15" ry="8.5" fill="#C9343C"/><ellipse rx="8" ry="3.6" fill="none" stroke="#9B1F27" stroke-width="2"/></g>')


# ===================================================================== 1. gut barrier
def art_gut_barrier(t):
    random.seed(7)
    out = [defs()]
    # trigger tabs
    tabs = [("Nutrients", "#2E8B57", "should pass"), ("Food particles", t["c2"], ""),
            ("Microbes", t["c2"], ""), ("Medications", t["c2"], "NSAIDs, antibiotics"),
            ("Stress", t["c2"], "and poor sleep")]
    for i, (lab, col, sub) in enumerate(tabs):
        x = 6 + i * 150
        out.append(f'<rect x="{x}" y="4" width="142" height="46" rx="6" fill="{col}"/>')
        out.append(f'<path d="M{x + 59},50 h24 l-12,11 z" fill="{col}"/>')
        out.append(T(x + 71, 25, lab, 13.5, 800, "#fff", "middle"))
        if sub:
            out.append(T(x + 71, 41, sub, 9.5, 500, "#EAF4F7", "middle"))
    # particles over each column
    syms = [("C", "#E07B24"), ("D", "#2F6DB5"), ("Mg", "#B4652E"), ("Zn", "#264D8C"), ("B", "#3C9A5F"), ("K", "#7A3E9D"), ("Ca", "#1F9AA6"), ("Fe", "#6B3A87")]
    pos = [(28, 92), (62, 118), (100, 88), (124, 124), (40, 148), (88, 150), (134, 158), (16, 124)]
    for (sx, sy), (s, c) in zip(pos, syms):
        out.append(nutrient(sx, sy, s, c, r=12, square=s in ("Ca", "Mg", "Zn", "Fe")))
    for (x, y, s) in [(176, 96, 1.0), (214, 122, 0.8), (250, 92, 1.1), (276, 140, 0.7), (196, 152, 0.9), (242, 162, 0.6)]:
        out.append(food_bit(x, y, s))
    for (x, y, r) in [(330, 98, 20), (372, 132, -30), (420, 96, 60), (346, 158, 10), (404, 160, -10)]:
        out.append(bacterium(x, y, r, 0.95))
    for (x, y, r) in [(486, 96, -20), (532, 126, 30), (572, 94, 10), (510, 158, 70), (566, 158, -40)]:
        out.append(capsule(x, y, r, 0.95))
    # stress: cortisol swirls
    for (x, y) in [(650, 104), (700, 140), (728, 98)]:
        out.append(f'<path d="M{x - 14},{y} c6,-12 18,-12 22,0 s-10,14 -14,6 s6,-8 8,-2" fill="none" stroke="#8E5BB5" stroke-width="2.6" stroke-linecap="round"/>')
    out.append(T(690, 172, "stress signals", 10, 600, "#6E4596", "middle", italic=True))

    # cells
    top, bot = 214, 338
    n = 10
    cw = 76
    for i in range(n):
        leaky = i >= 5
        x = i * cw
        gap = 7 if leaky else 1.5
        x0, x1 = x + gap, x + cw - gap
        if not leaky:
            fill, nuc = "#F5CDB8", "#E58E86"
            path = f'M{x0},{top + 14} Q{x0},{top} {x0 + 14},{top} H{x1 - 14} Q{x1},{top} {x1},{top + 14} V{bot} H{x0} Z'
        else:
            fill, nuc = "#EC8C79" if i % 2 else "#E37763", "#C6463F"
            jag = top + 8 + (i % 3) * 5
            path = (f'M{x0},{jag + 10} Q{x0 + 2},{jag} {x0 + 12},{jag + 2} L{x0 + 22},{jag - 4} L{x0 + 32},{jag + 6} '
                    f'L{x1 - 18},{jag - 2} Q{x1},{jag + 2} {x1},{jag + 16} V{bot} H{x0} Z')
        out.append(f'<path d="{path}" fill="{fill}" stroke="{"#E3A994" if not leaky else "#C9584B"}" stroke-width="1.2"/>')
        out.append(f'<ellipse cx="{x + cw / 2 + (3 if i % 2 else -3)}" cy="{top + 84}" rx="16" ry="13" fill="{nuc}" opacity=".9"/>')
        # microvilli
        step = 6.5 if not leaky else 9
        k = x0 + 5
        while k < x1 - 4:
            h = 11 if not leaky else random.choice([4, 6, 8, 0])
            if h:
                out.append(f'<line x1="{k:.1f}" y1="{top + (0 if not leaky else 6)}" x2="{k:.1f}" y2="{top - h + (0 if not leaky else 6)}" '
                           f'stroke="{"#E7A68D" if not leaky else "#D8705E"}" stroke-width="3.4" stroke-linecap="round"/>')
            k += step
        # tight junctions on healthy side
        if not leaky and i > 0:
            for j in range(4):
                out.append(f'<line x1="{x - 3}" y1="{top + 6 + j * 6}" x2="{x + 3}" y2="{top + 6 + j * 6}" stroke="#7E4A3A" stroke-width="1.6"/>')
    # arrows: nutrients through healthy cells
    for x in (120, 270):
        out.append(f'<path d="M{x},{top - 30} V{bot + 26}" stroke="#1E5FA8" stroke-width="5" fill="none" marker-end="url(#ahb)" opacity=".95"/>')
    out.append(nutrient(112, 270, "K", "#7A3E9D", 11))
    out.append(nutrient(262, 300, "Mg", "#B4652E", 11, True))
    # leaky gaps with intruders
    for i, item in zip([6, 7, 8, 9], ["food", "bact", "food", "bact"]):
        gx = i * cw
        out.append(f'<path d="M{gx},{top - 36} V{bot + 30}" stroke="#1E5FA8" stroke-width="5" fill="none" marker-end="url(#ahb)" opacity=".9"/>')
        if item == "food":
            out.append(food_bit(gx, top + 60, 0.75))
        else:
            out.append(bacterium(gx, top + 84, 90, 0.72))
    out.append(pill_label(108, top - 24, "Healthy barrier", t["deep"], 150, 12))
    out.append(pill_label(650, top - 24, "Leaky barrier", "#B94A3B", 140, 12))
    out.append(f'<rect x="168" y="{top + 92}" width="112" height="30" rx="6" fill="#FFF7F2" opacity=".93"/>')
    out.append(T(224, top + 104, "Tight junctions keep", 9.5, 700, "#7E4A3A", "middle"))
    out.append(T(224, top + 116, "the seams sealed", 9.5, 700, "#7E4A3A", "middle"))
    out.append(f'<path d="M190,{top + 92} L228,{top + 14}" stroke="#7E4A3A" stroke-width="1.2"/>')
    out.append(f'<rect x="470" y="{top + 90}" width="130" height="36" rx="6" fill="#FFF1EE" opacity=".94"/>')
    out.append(T(535, top + 105, "Inflammation", 13, 800, "#5D1914", "middle"))
    out.append(T(535, top + 119, "seams loosen, gaps open", 9, 600, "#5D1914", "middle", italic=True))
    out.append(f'<rect x="12" y="{top + 112}" width="96" height="18" rx="5" fill="#FFF7F2" opacity=".9"/>')
    out.append(T(60, top + 125, "Gut lining cells", 9.5, 700, "#8F4E3E", "middle", italic=True))

    # bloodstream
    b0 = bot + 8
    out.append(f'<path d="M0,{b0 + 22} Q380,{b0 - 14} 760,{b0 + 22} L760,{b0 + 118} Q380,{b0 + 82} 0,{b0 + 118} Z" fill="url(#bl)"/>')
    out.append('<defs><linearGradient id="bl" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#A3262D"/>'
               '<stop offset="1" stop-color="#6E141A"/></linearGradient></defs>')
    for (x, y, r) in [(40, b0 + 70, 10), (150, b0 + 56, -15), (330, b0 + 74, 20), (430, b0 + 52, -5), (520, b0 + 78, 25), (640, b0 + 70, -20), (720, b0 + 86, 10)]:
        out.append(rbc(x, y, 0.95, r))
    out.append(nutrient(96, b0 + 72, "D", "#2F6DB5", 11))
    out.append(nutrient(212, b0 + 64, "Zn", "#264D8C", 11, True))
    out.append(nutrient(272, b0 + 80, "C", "#E07B24", 11))
    out.append(food_bit(476, b0 + 76, 0.7))
    out.append(bacterium(580, b0 + 56, 20, 0.7))
    out.append(food_bit(690, b0 + 50, 0.62))
    out.append(T(120, b0 + 106, "Bloodstream", 12, 700, "#F6C9C9", "start", italic=True))
    out.append(T(640, b0 + 106, "things that should have stayed out", 11, 600, "#F6C9C9", "middle", italic=True))
    return svg(760, b0 + 122, "".join(out), "Healthy versus leaky gut barrier")


# ===================================================================== 2. fatty liver
LIVER = ("M4,34 C2,14 24,3 58,4 C84,5 110,8 124,15 C129,18 127,24 120,28 C104,39 82,53 61,63 "
         "C46,71 29,73 18,65 C9,58 5,47 4,34 Z")


def liver(x, y, s, fill, spots=None, tex=False):
    g = [f'<g transform="translate({x},{y}) scale({s})">',
         f'<path d="{LIVER}" fill="{fill}" stroke="rgba(0,0,0,.18)" stroke-width="1.5"/>',
         '<path d="M60,6 C62,24 60,40 52,60" stroke="rgba(255,255,255,.35)" stroke-width="2.4" fill="none"/>',
         '<path d="M14,22 C24,12 40,10 52,12" stroke="rgba(255,255,255,.45)" stroke-width="3" fill="none" stroke-linecap="round"/>']
    if spots:
        for (sx, sy, r) in spots:
            g.append(f'<circle cx="{sx}" cy="{sy}" r="{r}" fill="rgba(255,236,170,.75)"/>')
    if tex:
        for k in range(9):
            g.append(f'<path d="M{8 + k * 12},{14 + (k % 3) * 6} q6,8 2,16" stroke="rgba(60,50,45,.45)" stroke-width="1.4" fill="none"/>')
    g.append("</g>")
    return "".join(g)


def tissue(cx, cy, r, stage, uid):
    random.seed(uid)
    parts = [f'<clipPath id="cl{uid}"><circle cx="{cx}" cy="{cy}" r="{r}"/></clipPath>',
             f'<g clip-path="url(#cl{uid})"><rect x="{cx - r}" y="{cy - r}" width="{2 * r}" height="{2 * r}" fill="#5A1C1F"/>']
    # polygonal liver cells
    for gx in range(-3, 4):
        for gy in range(-3, 4):
            px = cx + gx * 26 + (13 if gy % 2 else 0)
            py = cy + gy * 23
            pts = " ".join(f"{px + 12.5 * math.cos(math.radians(a + 30)):.1f},{py + 12.5 * math.sin(math.radians(a + 30)):.1f}" for a in range(0, 360, 60))
            parts.append(f'<polygon points="{pts}" fill="#8E3B3D" stroke="#4A1416" stroke-width="2"/>')
            parts.append(f'<circle cx="{px}" cy="{py}" r="4" fill="#C2696B"/>')
    if stage >= 1:
        n = {1: 14, 2: 22, 3: 18}[stage]
        for _ in range(n):
            ang = random.uniform(0, 6.283)
            d = random.uniform(0, r - 8)
            rr = random.uniform(4, 9 if stage == 1 else 11)
            parts.append(f'<circle cx="{cx + d * math.cos(ang):.1f}" cy="{cy + d * math.sin(ang):.1f}" r="{rr:.1f}" fill="#F2B72E" stroke="#C98A12" stroke-width="1"/>')
    if stage == 2:
        for _ in range(12):
            ang = random.uniform(0, 6.283)
            d = random.uniform(0, r - 6)
            parts.append(f'<circle cx="{cx + d * math.cos(ang):.1f}" cy="{cy + d * math.sin(ang):.1f}" r="2.6" fill="#FFFFFF" stroke="#E2463E" stroke-width="1.4"/>')
    if stage == 3:
        for k in range(5):
            y0 = cy - r + 12 + k * (2 * r - 20) / 4
            parts.append(f'<path d="M{cx - r},{y0:.1f} C{cx - r / 3},{y0 - 12:.1f} {cx + r / 3},{y0 + 12:.1f} {cx + r},{y0 - 4:.1f}" stroke="#B8AFA8" stroke-width="7" fill="none" opacity=".9"/>')
    parts.append("</g>")
    parts.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="#3A2A2A" stroke-width="2.5"/>')
    return "".join(parts)


def art_fatty_liver(t):
    out = [defs()]
    out.append('<path d="M0,74 H708 L756,182 L708,290 H0 Z" fill="#8E8A95"/>')
    out.append('<path d="M0,74 H708 L756,182 L708,290 H0 Z" fill="url(#lg)" opacity=".9"/>')
    out.append('<defs><linearGradient id="lg" x1="0" x2="1"><stop offset="0" stop-color="#9D99A5"/><stop offset="1" stop-color="#6F6B78"/></linearGradient></defs>')
    stages = [("HEALTHY", "#A8392C", 0, None, False),
              ("FATTY LIVER", "#D8992C", 1, [(30, 30, 6), (70, 18, 5), (52, 44, 7), (88, 28, 5)], False),
              ("INFLAMED", "#A2603E", 2, [(40, 26, 5), (80, 22, 4)], False),
              ("SCARRING", "#857870", 3, None, True)]
    subs = ["", "MASLD, formerly NAFLD", "MASH, formerly NASH", "fibrosis, then cirrhosis"]
    xs = [96, 286, 476, 664]
    for i, ((lab, col, st, spots, tex), cx) in enumerate(zip(stages, xs)):
        out.append(f'<polygon points="{cx - 8},88 {cx + 8},88 {cx + 52},178 {cx - 52},178" fill="rgba(255,255,255,.16)"/>')
        out.append(liver(cx - 66, 12, 1.05, col, spots, tex))
        out.append(T(cx, 8, lab, 13, 800, "#2B3236", "middle", ls=0.6))
        out.append(tissue(cx, 224, 50, st, 100 + i))
        if subs[i]:
            out.append(T(cx, 296 + 14, subs[i], 9.6, 600, "#4A525A", "middle", italic=True))
    notes = [(190, ["Insulin resistance", "Extra free fatty", "acids reach liver", "High triglycerides"]),
             (381, ["Oxidative stress", "Gut-derived", "endotoxin", "Inflammatory", "signals"]),
             (570, ["Years of", "ongoing", "inflammation", "without change"])]
    for (x, lines) in notes:
        out.append(T(x, 108, lines, 10.2, 700, "#FFFFFF", "middle"))
    # reversible arcs
    out.append('<path d="M262,272 Q190,330 118,272" stroke="#6BA539" stroke-width="7" fill="none" marker-end="url(#ahg)"/>')
    out.append('<path d="M452,272 Q380,330 308,272" stroke="#6BA539" stroke-width="7" fill="none" marker-end="url(#ahg)"/>')
    out.append(T(190, 338, "OFTEN REVERSIBLE", 11.5, 800, "#4E8A26", "middle"))
    out.append(T(380, 338, "OFTEN REVERSIBLE", 11.5, 800, "#4E8A26", "middle"))
    out.append('<path d="M516,284 Q570,326 624,284" stroke="#D4423A" stroke-width="7" fill="none"/>'
               '<path d="M512,276 l-2,16 M628,276 l2,16" stroke="#D4423A" stroke-width="7" stroke-linecap="round"/>')
    out.append(T(570, 338, "HARDEST TO REVERSE", 11.5, 800, "#B8322B", "middle"))
    out.append('<rect x="0" y="150" width="84" height="48" rx="8" fill="#7DB342"/>' + T(42, 170, ["Least", "severe"], 12.5, 800, "#fff", "middle", 1.1))
    out.append('<rect x="676" y="150" width="84" height="48" rx="8" fill="#D9473E"/>' + T(718, 170, ["Most", "severe"], 12.5, 800, "#fff", "middle", 1.1))
    return svg(760, 346, "".join(out), "Progression of fatty liver disease")


# ===================================================================== 3. reflux
def art_reflux(t):
    out = [defs('<linearGradient id="stw" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#F6B655"/><stop offset="1" stop-color="#E07A2A"/></linearGradient>'
                '<radialGradient id="zg"><stop offset="0" stop-color="#FFE6DD"/><stop offset="1" stop-color="#F6C3B6"/></radialGradient>')]
    outer = ("M208,200 C222,172 262,158 296,176 C334,196 346,252 336,300 C326,352 296,396 240,408 C192,418 146,404 118,372 "
             "C108,360 102,352 100,348 L96,322 C120,322 150,330 178,334 C200,336 212,320 206,296 C200,268 176,246 172,222 "
             "C171,214 170,208 170,205 Z")
    inner = ("M212,216 C226,194 258,184 288,198 C318,214 326,256 320,296 C312,340 286,378 240,390 C200,398 162,388 136,362 "
             "C128,354 122,348 120,344 L118,338 C140,338 162,346 184,350 C214,354 230,330 222,294 C215,264 194,244 190,222 Z")
    # duodenum
    out.append('<path d="M100,336 C72,340 54,362 60,394 C64,412 78,422 94,424" stroke="#E7913A" stroke-width="26" fill="none" stroke-linecap="round"/>')
    out.append('<path d="M100,336 C72,340 54,362 60,394 C64,412 78,422 94,424" stroke="#9A4420" stroke-width="10" fill="none" stroke-linecap="round"/>')
    # esophagus
    out.append('<path d="M186,4 C186,70 186,140 189,205" stroke="#E7913A" stroke-width="40" fill="none" stroke-linecap="round"/>')
    out.append('<path d="M186,4 C186,70 186,140 189,205" stroke="#9A4420" stroke-width="18" fill="none"/>')
    out.append('<ellipse cx="186" cy="6" rx="20" ry="6" fill="#F4B26A" stroke="#C76D22" stroke-width="2"/>')
    # stomach
    out.append(f'<path d="{outer}" fill="url(#stw)" stroke="#C76D22" stroke-width="3"/>')
    out.append(f'<path d="{inner}" fill="#A2481F"/>')
    out.append(f'<clipPath id="lum"><path d="{inner}"/></clipPath>')
    out.append('<g clip-path="url(#lum)"><path d="M100,330 C170,318 250,326 340,300 L340,420 L100,420 Z" fill="#6E2410"/>'
               + "".join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="#B9618F" opacity=".9"/>' for (x, y, r) in
                         [(196, 368, 7), (226, 360, 5), (252, 350, 6), (172, 362, 5), (278, 336, 5), (214, 378, 4), (300, 318, 4)])
               + "".join(f'<circle cx="{x}" cy="{y}" r="2.6" fill="#F6CDA8"/>' for (x, y) in [(262, 266), (284, 250), (246, 290), (296, 286), (270, 300)])
               + "</g>")
    # LES ring
    out.append('<path d="M169,192 C178,199 200,199 209,192" stroke="#FBE3B8" stroke-width="8" fill="none" stroke-linecap="round"/>')
    # reflux arrows
    out.append('<path d="M232,270 C214,246 198,226 190,186" stroke="#E2402B" stroke-width="5.5" fill="none" marker-end="url(#ahr)"/>')
    out.append('<path d="M188,166 V96" stroke="#FF6B4F" stroke-width="4.5" fill="none" marker-end="url(#ahr)" stroke-dasharray="2 8" stroke-linecap="round"/>')
    # zoom
    out.append('<line x1="206" y1="190" x2="272" y2="146" stroke="#A6AEB3" stroke-width="1.4"/>'
               '<line x1="210" y1="204" x2="300" y2="166" stroke="#A6AEB3" stroke-width="1.4"/>')
    out.append('<circle cx="318" cy="92" r="72" fill="url(#zg)" stroke="#E2E5E8" stroke-width="5"/>')
    out.append('<clipPath id="zc"><circle cx="318" cy="92" r="70"/></clipPath><g clip-path="url(#zc)">'
               '<rect x="296" y="10" width="44" height="88" fill="#E7913A"/><rect x="306" y="10" width="24" height="88" fill="#9A4420"/>'
               '<path d="M240,112 C270,96 296,96 308,104 L328,104 C340,96 366,96 396,112 L396,180 L240,180 Z" fill="#E7913A"/>'
               '<path d="M250,124 C272,112 296,112 310,118 L326,118 C340,112 364,112 390,124 L390,180 L250,180 Z" fill="#7E2A12"/>'
               '<ellipse cx="303" cy="104" rx="8" ry="5" fill="#FBE3B8"/><ellipse cx="333" cy="104" rx="8" ry="5" fill="#FBE3B8"/>'
               '<path d="M318,150 C312,130 322,118 316,96 C312,80 320,66 318,44" stroke="#FF5A3C" stroke-width="4" fill="none" marker-end="url(#ahr)"/>'
               '<path d="M336,148 C330,132 336,124 330,112" stroke="#FF5A3C" stroke-width="3" fill="none" stroke-dasharray="2 5" stroke-linecap="round"/></g>')
    out.append(T(318, 184, "Relaxed valve lets stomach", 10.5, 800, "#7E2A12", "middle"))
    out.append(T(318, 197, "contents splash back up", 10.5, 800, "#7E2A12", "middle"))
    lab = lambda y, x2, text: (f'<line x1="78" y1="{y}" x2="{x2}" y2="{y}" stroke="#3B4247" stroke-width="1.3"/>'
                               + T(74, y + 4, text, 12, 800, "#22292D", "end"))
    out.append(lab(96, 166, "Esophagus"))
    out.append(lab(196, 168, "LES valve"))
    out.append(lab(262, 186, "Stomach"))
    out.append('<line x1="300" y1="350" x2="352" y2="372" stroke="#3B4247" stroke-width="1.3"/>' + T(356, 376, "Acid and", 12, 800, "#22292D") + T(356, 390, "enzymes", 12, 800, "#22292D"))
    return svg(420, 430, "".join(out), "Reflux at the lower esophageal valve")


# ===================================================================== 4. blood pressure
def art_bp(t):
    out = [defs()]
    steps = [("leaf", "Leafy greens and beets", "bring in nitrate"),
             ("microbe", "Friendly mouth bacteria", "turn nitrate into nitrite"),
             ("drop", "Your body turns nitrite", "into nitric oxide (NO)"),
             ("heartpulse", "NO relaxes vessel walls", "so pressure can ease")]
    for i, (ic, a, b) in enumerate(steps):
        y = 6 + i * 70
        out.append(f'<rect x="0" y="{y}" width="236" height="56" rx="10" fill="{t["soft"]}" stroke="{t["c2"]}" stroke-width="1.5"/>')
        out.append(f'<circle cx="30" cy="{y + 28}" r="20" fill="#fff" stroke="{t["c1"]}" stroke-width="2"/>')
        out.append(f'<g transform="translate(16,{y + 14}) scale(.44)" fill="none" stroke="{t["c1"]}" stroke-width="5" stroke-linecap="round" stroke-linejoin="round">'
                   + __import__("kit").ICONS[ic].replace('class="x"', '') + "</g>")
        out.append(T(60, y + 25, a, 12, 800, t["deep"]))
        out.append(T(60, y + 42, b, 11, 500, "#33404A"))
        if i < 3:
            out.append(f'<path d="M118,{y + 57} v11" stroke="{t["c1"]}" stroke-width="3" marker-end="url(#ah)"/>')
    # vessel comparison
    X0, Y0 = 262, 26
    out.append(T(X0 + 118, 14, "UNHEALTHY", 12, 800, "#2B3236", "middle", ls=0.8))
    out.append(T(X0 + 118, 30, "vessel tightened", 10.5, 600, "#5A646B", "middle", italic=True))
    out.append(T(X0 + 370, 14, "HEALTHY", 12, 800, "#2B3236", "middle", ls=0.8))
    out.append(T(X0 + 370, 30, "vessel relaxed", 10.5, 600, "#5A646B", "middle", italic=True))
    vy = 150
    # outer walls
    out.append(f'<rect x="{X0}" y="{vy - 104}" width="498" height="208" rx="18" fill="#E9B3A5"/>')
    out.append(f'<path d="M{X0},{vy - 90} H{X0 + 240} V{vy + 90} H{X0} Z" fill="#A7362F"/>')
    out.append(f'<path d="M{X0 + 248},{vy - 96} H{X0 + 498} V{vy + 96} H{X0 + 248} Z" fill="#B54A3C"/>')
    out.append(f'<rect x="{X0}" y="{vy - 34}" width="240" height="68" fill="#E6A49B"/>')
    out.append(f'<rect x="{X0 + 248}" y="{vy - 62}" width="250" height="124" fill="#EFB7AD"/>')
    out.append(f'<rect x="{X0 + 240}" y="{vy - 116}" width="8" height="232" fill="#B8BEC3"/>')
    for k in range(6):
        x = X0 + 22 + k * 36
        out.append(f'<path d="M{x},{vy - 82} v26" stroke="#2B1412" stroke-width="2.5" marker-end="url(#ah)"/>'
                   f'<path d="M{x},{vy + 82} v-26" stroke="#2B1412" stroke-width="2.5" marker-end="url(#ah)"/>')
    for k in range(5):
        x = X0 + 278 + k * 44
        out.append(f'<path d="M{x},{vy - 66} v-22" stroke="#2B1412" stroke-width="2.5" marker-end="url(#ah)"/>'
                   f'<path d="M{x},{vy + 66} v22" stroke="#2B1412" stroke-width="2.5" marker-end="url(#ah)"/>')
    for (x, y) in [(X0 + 30, vy - 10), (X0 + 196, vy + 14), (X0 + 300, vy - 34), (X0 + 330, vy + 30), (X0 + 470, vy - 30), (X0 + 452, vy + 34)]:
        out.append(rbc(x, y, 0.85, 10))
    out.append(f'<path d="M{X0 + 58},{vy} h124" stroke="#fff" stroke-width="15" stroke-linecap="round"/>'
               f'<path d="M{X0 + 182},{vy - 15} l26,15 l-26,15 z" fill="#fff"/>')
    out.append(T(X0 + 122, vy + 5, "High pressure", 12.5, 800, "#2B1412", "middle"))
    out.append(f'<path d="M{X0 + 320},{vy} h108" stroke="#fff" stroke-width="15" stroke-linecap="round"/>'
               f'<path d="M{X0 + 428},{vy - 15} l26,15 l-26,15 z" fill="#fff"/>')
    out.append(T(X0 + 376, vy + 5, "Normal pressure", 12.5, 800, "#2B1412", "middle"))
    out.append(T(X0 + 249, vy + 130, "Nitric oxide is the signal that tells vessel walls to relax.", 11, 600, "#33404A", "middle", italic=True))
    return svg(760, 290, "".join(out), "Nitric oxide pathway and vessel tone")


# ===================================================================== 5. IBD
def gi_tract(x, y, mode, t):
    g = [f'<g transform="translate({x},{y})">']
    # body outline
    g.append('<path d="M70,0 C96,0 104,18 104,30 C104,44 96,52 92,58 C124,66 140,90 140,130 L140,300 L0,300 L0,130 C0,90 16,66 48,58 C44,52 36,44 36,30 C36,18 44,0 70,0Z" fill="#F4E4DA" stroke="#E0C7B8" stroke-width="2"/>')
    g.append('<path d="M70,62 V120" stroke="#E7A07A" stroke-width="7" stroke-linecap="round"/>')  # esophagus
    g.append('<path d="M70,118 C92,112 104,128 98,142 C92,158 74,156 66,146" fill="#EDA07A" stroke="#D9875F" stroke-width="2"/>')
    # colon frame
    colon = "M30,252 C24,220 24,196 30,176 C34,166 46,162 58,164 H90 C104,164 112,170 112,184 C114,206 114,232 110,254 C106,268 96,276 84,280 L76,296"
    g.append(f'<path d="{colon}" stroke="#E0A886" stroke-width="14" fill="none" stroke-linecap="round" stroke-linejoin="round"/>')
    # small intestine coil
    g.append('<path d="M60,180 C80,176 92,186 86,198 C80,210 54,204 52,216 C50,230 82,226 88,238 C92,250 66,256 56,248" stroke="#EDB596" stroke-width="7" fill="none" stroke-linecap="round"/>')
    red = "#D63B33"
    if mode == "uc":
        g.append(f'<path d="M112,196 C114,216 114,236 110,254 C106,268 96,276 84,280 L76,296" stroke="{red}" stroke-width="14" fill="none" stroke-linecap="round"/>')
    else:
        g.append(f'<path d="M56,248 C62,252 70,252 76,248" stroke="{red}" stroke-width="8" fill="none" stroke-linecap="round"/>')
        g.append(f'<path d="M26,214 C25,204 26,196 28,190" stroke="{red}" stroke-width="14" fill="none" stroke-linecap="round"/>')
        g.append(f'<path d="M78,164 H92" stroke="{red}" stroke-width="14" fill="none" stroke-linecap="round"/>')
        g.append(f'<path d="M112,226 C112,234 112,240 111,246" stroke="{red}" stroke-width="14" fill="none" stroke-linecap="round"/>')
        g.append(f'<circle cx="70" cy="24" r="5" fill="{red}"/>')
        g.append(f'<path d="M84,214 C88,210 90,206 88,200" stroke="{red}" stroke-width="7" fill="none" stroke-linecap="round"/>')
    g.append("</g>")
    return "".join(g)


def art_ibd(t):
    out = [defs()]
    out.append(gi_tract(150, 8, "uc", t))
    out.append(gi_tract(470, 8, "cd", t))
    out.append(T(220, 330, "Ulcerative colitis", 15, 800, t["deep"], "middle"))
    out.append(T(540, 330, "Crohn's disease", 15, 800, t["deep"], "middle"))
    out.append(T(380, 64, "WHERE IT SHOWS UP", 12, 800, t["deep"], "middle", ls=1.2))
    out.append(f'<circle cx="380" cy="150" r="46" fill="#fff" stroke="{t["c1"]}" stroke-width="3"/>')
    out.append(T(380, 162, "VS", 34, 900, "#D0442E", "middle"))
    out.append('<rect x="20" y="140" width="110" height="40" rx="8" fill="#F4E4DA"/>')
    out.append('<rect x="30" y="153" width="14" height="14" rx="3" fill="#D63B33"/>' + T(50, 159, "Inflamed", 11, 700, "#3B2A24") + T(50, 172, "areas", 11, 700, "#3B2A24"))
    return svg(760, 340, "".join(out), "Where ulcerative colitis and Crohn's disease occur")


# ===================================================================== 6. insulin resistance
def cell_panel(x0, normal, t):
    g = [f'<g transform="translate({x0},0)">']
    g.append(f'<rect x="0" y="0" width="370" height="250" rx="12" fill="{"#F3F5F6" if normal else "#F7EFEE"}"/>')
    g.append(T(185, 28, "NORMAL" if normal else "INSULIN RESISTANCE", 17, 900, "#2B3236", "middle", ls=0.6))
    # vessel
    g.append('<path d="M18,70 C40,64 70,66 92,80 L120,230 C96,240 70,240 46,232 Z" fill="#A6262F"/>')
    g.append('<path d="M26,78 C44,74 66,76 84,86 L108,222 C90,228 70,228 52,222 Z" fill="#7E141C"/>')
    random.seed(3 if normal else 4)
    nglu = 10 if normal else 26
    for _ in range(nglu):
        gx, gy = random.uniform(40, 98), random.uniform(96, 220)
        g.append(f'<circle cx="{gx:.1f}" cy="{gy:.1f}" r="4" fill="#6B6FC2"/>')
    for _ in range(10):
        gx, gy = random.uniform(40, 98), random.uniform(96, 220)
        g.append(f'<circle cx="{gx:.1f}" cy="{gy:.1f}" r="2.8" fill="#F2B632"/>')
    g.append(T(70, 62, "Blood", 10.5, 700, "#7E141C", "middle", italic=True))
    # cell
    g.append('<circle cx="262" cy="150" r="78" fill="#F7CFC4" stroke="#E7A796" stroke-width="5"/>')
    inside = 14 if normal else 3
    random.seed(9)
    for _ in range(inside):
        a, d = random.uniform(0, 6.28), random.uniform(10, 62)
        g.append(f'<circle cx="{262 + d * math.cos(a):.1f}" cy="{150 + d * math.sin(a):.1f}" r="4.6" fill="#6B6FC2"/>')
    # receptor on membrane (left side)
    rx, ry = 187, 120
    g.append(f'<path d="M{rx - 6},{ry - 18} h22 v14 h-6 v10 h-10 v-10 h-6 z" fill="#E08A2E" stroke="#B4661B" stroke-width="1.5"/>')
    if normal:
        g.append(f'<path d="M{rx - 26},{ry - 10} h22" stroke="#F2B632" stroke-width="7" stroke-linecap="round"/>'
                 f'<circle cx="{rx - 30}" cy="{ry - 10}" r="7" fill="#F2B632"/>')
    else:
        g.append(f'<path d="M{rx - 46},{ry - 30} l16,8" stroke="#F2B632" stroke-width="7" stroke-linecap="round"/>'
                 f'<circle cx="{rx - 50}" cy="{ry - 32}" r="7" fill="#F2B632"/>'
                 f'<path d="M{rx - 22},{ry - 2} l7,7 M{rx - 15},{ry - 2} l-7,7" stroke="#C0392B" stroke-width="2.6"/>')
    # glucose door
    dx, dy = 192, 186
    if normal:
        g.append(f'<path d="M{dx - 10},{dy - 14} l-10,-6" stroke="#E08A2E" stroke-width="6" stroke-linecap="round"/>'
                 f'<path d="M{dx - 10},{dy + 14} l-10,6" stroke="#E08A2E" stroke-width="6" stroke-linecap="round"/>'
                 f'<path d="M{dx - 44},{dy} h42" stroke="#6B6FC2" stroke-width="3" marker-end="url(#ah)"/>')
    else:
        g.append(f'<path d="M{dx - 8},{dy - 16} v32" stroke="#E08A2E" stroke-width="7" stroke-linecap="round"/>')
    g.append(T(262, 244 - 4, "Fuel for muscle, liver and brain" if normal else "Sugar stays in the blood", 11, 700,
               "#2F5E3A" if normal else "#9B2A22", "middle", italic=True))
    labels = ([("1", 150, 72, "Insulin fits", "its receptor"), ("2", 140, 208, "Glucose door", "opens")] if normal else
              [("1", 150, 72, "Receptor stops", "responding"), ("2", 140, 208, "Glucose door", "stays shut")])
    for (n, lx, ly, a, b) in labels:
        g.append(f'<circle cx="{lx - 2}" cy="{ly - 5}" r="9" fill="#fff" stroke="#2B3236" stroke-width="1.6"/>' + T(lx - 2, ly - 1, n, 10.5, 800, "#2B3236", "middle"))
        g.append(T(lx + 12, ly - 6, a, 10.5, 700, "#2B3236") + T(lx + 12, ly + 7, b, 10.5, 700, "#2B3236"))
    g.append("</g>")
    return "".join(g)


def art_insulin(t):
    out = [defs(), cell_panel(0, True, t), cell_panel(390, False, t)]
    return svg(760, 252, "".join(out), "Normal insulin signalling versus insulin resistance")


# ===================================================================== 7. Lyme
def tick_drawing(x, y, s, body="#5B3A22", shield="#2A1A10"):
    legs = "".join(f'<path d="M0,{-6 + i * 7} C{-14},{-10 + i * 8} {-22},{-4 + i * 10} {-28},{2 + i * 11}" stroke="#2A1A10" stroke-width="2.2" fill="none"/>'
                   f'<path d="M0,{-6 + i * 7} C{14},{-10 + i * 8} {22},{-4 + i * 10} {28},{2 + i * 11}" stroke="#2A1A10" stroke-width="2.2" fill="none"/>' for i in range(4))
    return (f'<g transform="translate({x},{y}) scale({s})">{legs}'
            f'<ellipse cx="0" cy="8" rx="13" ry="17" fill="{body}"/><ellipse cx="0" cy="-2" rx="9" ry="9" fill="{shield}"/>'
            f'<path d="M-3,-14 L0,-22 L3,-14 Z" fill="{shield}"/></g>')


def art_lyme_transmission(t):
    out = [defs()]
    out.append('<path d="M20,40 C40,14 86,10 112,26 C104,44 96,58 70,62 C48,66 28,58 20,40 Z" fill="#4E9A3C"/>'
               '<path d="M24,40 C48,36 80,32 110,27" stroke="#2E6B22" stroke-width="2.5" fill="none"/>')
    out.append(tick_drawing(84, 24, 0.55))
    out.append('<path d="M56,74 C40,96 44,118 66,128" stroke="#4A2C80" stroke-width="3.5" fill="none" marker-end="url(#ah)"/>')
    out.append(tick_drawing(82, 140, 0.9))
    out.append(T(82, 186, "TICK", 11, 800, "#2B3236", "middle", ls=1))
    out.append('<path d="M120,140 h40" stroke="#4A2C80" stroke-width="3.5" marker-end="url(#ah)"/>')
    out.append('<rect x="170" y="128" width="78" height="40" rx="6" fill="#E9A07D"/><rect x="170" y="128" width="78" height="12" rx="4" fill="#F4C3A6"/>')
    out.append(T(209, 137, "SKIN", 7.5, 800, "#8A4A30", "middle"))
    out.append(tick_drawing(209, 118, 0.42))
    out.append(T(209, 186, "BITE", 11, 800, "#2B3236", "middle", ls=1))
    out.append('<path d="M256,140 h40" stroke="#4A2C80" stroke-width="3.5" marker-end="url(#ah)"/>')
    # boxes
    out.append(f'<rect x="306" y="20" width="160" height="88" rx="8" fill="#fff" stroke="{t["deep"]}" stroke-width="2"/>')
    out.append(T(386, 14, "LYME DISEASE", 10.5, 800, t["deep"], "middle", ls=0.8))
    out.append('<path d="M330,62 c12,-16 24,16 36,0 s24,16 36,0 s24,16 36,0" stroke="#3E6FB6" stroke-width="4" fill="none"/>')
    out.append(T(386, 96, "Borrelia burgdorferi", 10, 600, "#33404A", "middle", italic=True))
    out.append(f'<rect x="306" y="126" width="454" height="60" rx="8" fill="#fff" stroke="#D9873A" stroke-width="2"/>')
    out.append(T(533, 122 - 2, "OTHER INFECTIONS THE SAME TICKS CAN CARRY", 10, 800, "#B2621D", "middle", ls=0.6))
    co = ["Anaplasmosis", "Babesiosis", "Borrelia miyamotoi", "Powassan virus"]
    for i, c in enumerate(co):
        out.append(T(330 + i * 112 + 40, 160, c, 11, 700, "#33404A", "middle"))
    out.append(f'<rect x="480" y="20" width="280" height="88" rx="8" fill="{t["soft"]}"/>')
    out.append(T(494, 42, "IN GEORGIA", 10.5, 800, t["deep"], ls=0.8))
    out.append(T(494, 60, ["The lone star tick is the one people", "meet most. It can spread ehrlichiosis", "and trigger alpha-gal (red-meat) allergy."], 10.5, 500, "#33404A"))
    return svg(760, 192, "".join(out), "How tickborne infections spread")


def art_lyme_body(t):
    out = [defs()]
    body = ("M150,8 C170,8 182,22 182,42 C182,60 172,72 164,78 C196,84 214,100 218,130 L230,226 C232,238 222,242 216,232 "
            "L196,140 L194,236 L200,384 C201,396 186,398 182,388 L156,256 L144,256 L118,388 C114,398 99,396 100,384 L106,236 "
            "L104,140 L84,232 C78,242 68,238 70,226 L82,130 C86,100 104,84 136,78 C128,72 118,60 118,42 C118,22 130,8 150,8Z")
    out.append(f'<path d="{body}" fill="#E7B48C" stroke="#D49A70" stroke-width="2" transform="translate(40,0)"/>')
    out.append('<circle cx="216" cy="180" r="20" fill="none" stroke="#C8473C" stroke-width="5"/><circle cx="216" cy="180" r="8" fill="#C8473C" opacity=".8"/>')
    out.append(T(216, 214 - 2, "", 8, 600))
    left = [(24, "Expanding rash, sometimes", "bull's-eye shaped", 216, 180), (66, "Fever, chills, headache", "and fatigue", 182, 30),
            (108, "Swollen lymph nodes", "", 170, 86), (150, "Muscle and joint aches", "", 120, 140)]
    for (y, a, b, px, py) in left:
        out.append(f'<line x1="98" y1="{y}" x2="{px}" y2="{py}" stroke="#4A2C80" stroke-width="1.2"/><circle cx="{px}" cy="{py}" r="3" fill="#4A2C80"/>')
        out.append(T(92, y + 4, a, 10.5, 700, "#2B3236", "end"))
        if b:
            out.append(T(92, y + 17, b, 10.5, 700, "#2B3236", "end"))
    right = [(30, "Facial palsy, severe", "headache, stiff neck", 190, 40), (110, "Heart palpitations", "(Lyme carditis)", 196, 112),
             (190, "Nerve pain, numbness", "or tingling", 254, 210), (290, "Arthritis with joint", "swelling, often knees", 222, 300)]
    for (y, a, b, px, py) in right:
        out.append(f'<line x1="282" y1="{y}" x2="{px}" y2="{py}" stroke="#D9873A" stroke-width="1.2"/><circle cx="{px}" cy="{py}" r="3" fill="#D9873A"/>')
        out.append(T(288, y + 4, a, 10.5, 700, "#2B3236"))
        out.append(T(288, y + 17, b, 10.5, 700, "#2B3236"))
    return svg(420, 400, "".join(out), "Early and later Lyme symptoms").replace('viewBox="0 0 420 400"', 'viewBox="-96 0 516 400"')


# ===================================================================== 8. PCOS
def uterus(x, y, s):
    return (f'<g transform="translate({x},{y}) scale({s})">'
            '<path d="M-34,-6 C-60,-34 -96,-30 -118,-8" stroke="#B5434C" stroke-width="7" fill="none" stroke-linecap="round"/>'
            '<path d="M34,-6 C60,-34 96,-30 118,-8" stroke="#B5434C" stroke-width="7" fill="none" stroke-linecap="round"/>'
            '<path d="M-118,-8 c-8,-6 -18,-2 -18,6 M118,-8 c8,-6 18,-2 18,6" stroke="#B5434C" stroke-width="5" fill="none"/>'
            '<ellipse cx="-104" cy="20" rx="30" ry="21" fill="#E8A1A0" stroke="#B5434C" stroke-width="2.5"/>'
            '<ellipse cx="104" cy="20" rx="30" ry="21" fill="#E8A1A0" stroke="#B5434C" stroke-width="2.5"/>'
            + "".join(f'<circle cx="{cx}" cy="{cy}" r="5" fill="#FBE3DC" stroke="#C8686B" stroke-width="1.4"/>'
                      for (cx, cy) in [(-120, 12), (-108, 30), (-94, 14), (-114, 22), (-90, 28), (90, 14), (102, 30), (116, 16), (110, 6), (94, 28), (122, 26)])
            + '<path d="M-36,-14 C-36,-30 36,-30 36,-14 C36,20 18,46 10,62 L10,96 C10,104 -10,104 -10,96 L-10,62 C-18,46 -36,20 -36,-14Z" fill="#B5434C"/>'
            '<path d="M-22,-10 C-20,-20 20,-20 22,-10 C20,14 8,34 0,46 C-8,34 -20,14 -22,-10Z" fill="#E18A8D"/>'
            "</g>")


def art_pcos(t):
    out = [defs()]
    # pancreas
    out.append('<path d="M30,52 C52,34 96,36 128,46 C150,52 162,64 150,74 C136,84 104,70 78,74 C54,78 30,82 24,70 C20,64 22,58 30,52Z" fill="#F4C842" stroke="#C99A1A" stroke-width="2"/>')
    out.append(T(92, 100, "Pancreas", 11, 700, "#7A5A0E", "middle", italic=True))
    out.append(f'<circle cx="18" cy="140" r="12" fill="#fff" stroke="{t["c1"]}" stroke-width="2"/>' + T(18, 144, "1", 11, 800, t["c1"], "middle"))
    out.append(T(38, 136, ["Insulin is made here to move", "sugar out of the blood"], 11, 700, "#2B3236"))
    # insulin drops trail
    for i in range(9):
        out.append(f'<circle cx="{150 + i * 16}" cy="{64 + i * 9 + (i % 2) * 5}" r="4" fill="#E2A21E"/>')
    # vessel
    out.append('<path d="M262,90 C300,82 330,96 340,130 L372,250 C342,264 312,264 286,254 Z" fill="#A6262F"/>')
    random.seed(11)
    for _ in range(22):
        out.append(f'<circle cx="{random.uniform(292, 344):.1f}" cy="{random.uniform(112, 246):.1f}" r="3.6" fill="#6B6FC2"/>')
    for _ in range(10):
        out.append(f'<circle cx="{random.uniform(292, 344):.1f}" cy="{random.uniform(112, 246):.1f}" r="2.8" fill="#F2B632"/>')
    out.append(f'<circle cx="18" cy="196" r="12" fill="#fff" stroke="{t["c1"]}" stroke-width="2"/>' + T(18, 200, "2", 11, 800, t["c1"], "middle"))
    out.append(T(38, 192, ["When cells resist insulin, sugar", "stays in the blood and the", "pancreas pumps out even more"], 11, 700, "#2B3236"))
    # arrow to ovaries
    out.append('<path d="M360,262 C380,286 410,300 446,300" stroke="#2B3236" stroke-width="3" fill="none" marker-end="url(#ah)"/>')
    out.append(uterus(600, 210, 1.0))
    out.append(f'<circle cx="420" cy="62" r="12" fill="#fff" stroke="{t["c1"]}" stroke-width="2"/>' + T(420, 66, "3", 11, 800, t["c1"], "middle"))
    out.append(T(440, 52, ["High insulin pushes the ovaries to make", "extra androgens (testosterone), which", "disrupts ovulation and leaves many small", "follicles (the “cysts”) behind"], 11, 700, "#2B3236"))
    out.append(T(600, 338, "Ovaries with many small follicles", 10.5, 700, "#8A2F37", "middle", italic=True))
    return svg(760, 346, "".join(out), "How insulin resistance and PCOS connect")


# ===================================================================== 9. mold
def art_mold_home(t):
    out = [defs()]
    out.append('<path d="M10,120 L170,20 L330,120 Z" fill="#9AA6B2"/>')
    out.append('<rect x="30" y="118" width="280" height="180" fill="#F7F2E8" stroke="#B9AE9C" stroke-width="2"/>')
    out.append('<path d="M30,208 H310" stroke="#B9AE9C" stroke-width="5"/>')
    out.append('<path d="M170,118 V298" stroke="#B9AE9C" stroke-width="3"/>')
    out.append('<rect x="30" y="298" width="280" height="22" fill="#B7A48A"/>')  # crawl
    # rooms detail
    out.append('<rect x="60" y="150" width="60" height="36" fill="#CFE3EE" stroke="#8FB0C2" stroke-width="2"/>')  # window
    out.append('<rect x="206" y="236" width="70" height="40" rx="4" fill="#D9D2C6"/><rect x="214" y="226" width="54" height="12" fill="#B9AE9C"/>')  # sink cabinet
    out.append('<rect x="64" y="240" width="54" height="44" rx="6" fill="#C9C1B4"/>')  # couch
    # moisture/mold spots
    for (x, y, r) in [(240, 132, 14), (258, 140, 9), (226, 144, 7), (246, 288, 8), (80, 312, 10), (110, 314, 7), (286, 214, 7)]:
        out.append(f'<circle cx="{x}" cy="{y}" r="{r}" fill="#4F6B3E" opacity=".7"/>')
        out.append(f'<circle cx="{x + r * 0.5}" cy="{y - r * 0.3}" r="{r * 0.45}" fill="#33472A" opacity=".7"/>')
    out.append('<path d="M240,118 c-2,6 2,8 0,13" stroke="#3E77B3" stroke-width="2.5" fill="none"/><path d="M240,134 c-3,4 -3,7 0,9 c3,-2 3,-5 0,-9z" fill="#3E77B3"/>')
    for (x, y, a, b) in [(340, 140, "Ceilings and", "attic leaks"), (340, 214, "Behind walls", "and HVAC"), (340, 270, "Under sinks", ""), (340, 314, "Crawl space", "")]:
        out.append(T(x, y, a, 11, 700, "#2B3236"))
        if b:
            out.append(T(x, y + 14, b, 11, 700, "#2B3236"))
    for (x1, y1, x2, y2) in [(336, 136, 262, 136), (336, 210, 292, 214), (336, 266, 254, 284), (336, 310, 120, 312)]:
        out.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#4A525A" stroke-width="1.1" stroke-dasharray="3 3"/>')
    return svg(440, 330, "".join(out), "Where hidden mold grows at home")


def art_binder(t):
    out = [defs()]
    # liver
    out.append(liver(16, 8, 0.95, "#A8392C"))
    out.append(T(78, 96, "Liver", 11, 700, "#7A2A20", "middle", italic=True))
    # bile duct down to gut
    out.append('<path d="M110,64 C150,80 160,110 170,140" stroke="#5F9F3E" stroke-width="7" fill="none" stroke-linecap="round"/>')
    out.append(T(156, 92, "bile", 10.5, 700, "#3F7A26"))
    # gut tube
    out.append('<path d="M150,150 C250,130 300,170 400,150 C470,136 520,150 560,160" stroke="#EBC3B0" stroke-width="40" fill="none" stroke-linecap="round"/>')
    out.append('<path d="M150,150 C250,130 300,170 400,150 C470,136 520,150 560,160" stroke="#F6DCCE" stroke-width="26" fill="none" stroke-linecap="round"/>')
    hexes = [(196, 146), (236, 142), (282, 156), (322, 160), (372, 152), (420, 146), (470, 146), (512, 154)]
    for i, (x, y) in enumerate(hexes):
        out.append(f'<polygon points="{x},{y - 6} {x + 5},{y - 3} {x + 5},{y + 3} {x},{y + 6} {x - 5},{y + 3} {x - 5},{y - 3}" fill="#C8343B"/>')
        if i >= 3:
            out.append(f'<path d="M{x + 9},{y - 8} a10,10 0 1 1 0,16 a7,7 0 1 0 0,-16z" fill="#2C6FB7"/>')
    out.append('<path d="M570,160 h40" stroke="#2B3236" stroke-width="3" marker-end="url(#ah)"/>')
    out.append(T(618, 152, ["Bound toxins", "leave with stool"], 11, 800, "#2B3236"))
    # recirculation loop
    out.append('<path d="M236,128 C230,70 200,40 132,36" stroke="#C8343B" stroke-width="3.5" fill="none" stroke-dasharray="6 5" marker-end="url(#ahr)"/>')
    out.append(T(244, 50, ["Without a binder, many toxins are", "reabsorbed and sent back to the liver"], 10.5, 700, "#9B2A22"))
    # legend
    out.append('<polygon points="560,40 565,43 565,49 560,52 555,49 555,43" fill="#C8343B"/>' + T(578, 50, "Mycotoxins", 11, 700, "#2B3236"))
    out.append('<path d="M558,66 a10,10 0 1 1 0,16 a7,7 0 1 0 0,-16z" fill="#2C6FB7"/>' + T(578, 80, "Binder", 11, 700, "#2B3236"))
    return svg(760, 200, "".join(out), "How a binder helps carry toxins out")
