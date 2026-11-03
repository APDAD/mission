"""Shared SVG helpers for condition-sheet illustrations.

Every diagram that uses symbols (dots, hexagons, crescents, pills...) MUST
carry a key: use key_box() inside the SVG, or kit.html_key() under it.
Asher's rule (2026-11-03): "Have a key. Purple means this. Yellow dot means
this." Labels must never sit on top of busy art: give them a backdrop with
label_bg() or move them to clear space.
"""
from art import (FONT, T, defs, svg, pill_label, nutrient, food_bit, bacterium,  # noqa: F401
                 capsule, rbc, liver, tissue, tick_drawing, uterus, LIVER)

GLUCOSE = "#6B6FC2"   # purple: glucose (sugar)
INSULIN = "#F2B632"   # gold: insulin
TOXIN = "#C8343B"     # red hexagon: toxin / mycotoxin
BINDER = "#2C6FB7"    # blue crescent: binder
FAT = "#F2B72E"       # yellow droplet: fat
IMMUNE = "#E2463E"    # white dot, red ring: immune / inflammatory cell
SCAR = "#B8AFA8"      # grey band: scar tissue


# ---- swatches, drawn centred on (0, 0); used by key_box and in the art itself
def sw_dot(color, r=6, stroke="none", sw=0):
    return f'<circle r="{r}" fill="{color}" stroke="{stroke}" stroke-width="{sw}"/>'


def sw_ring(fill="#FFFFFF", ring=IMMUNE, r=5):
    return f'<circle r="{r}" fill="{fill}" stroke="{ring}" stroke-width="2"/>'


def sw_hex(color=TOXIN, r=7):
    return (f'<polygon points="0,{-r} {r * .87:.1f},{-r / 2:.1f} {r * .87:.1f},{r / 2:.1f} 0,{r} '
            f'{-r * .87:.1f},{r / 2:.1f} {-r * .87:.1f},{-r / 2:.1f}" fill="{color}"/>')


def sw_crescent(color=BINDER):
    return f'<path d="M-2,-8 a10,10 0 1 1 0,16 a7,7 0 1 0 0,-16z" fill="{color}"/>'


def sw_rect(color, w=16, h=10, rx=2):
    return f'<rect x="{-w / 2}" y="{-h / 2}" width="{w}" height="{h}" rx="{rx}" fill="{color}"/>'


def sw_band(color=SCAR):
    return f'<rect x="-9" y="-3" width="18" height="6" rx="3" fill="{color}"/>'


def sw_arrow(color="#1E5FA8"):
    return f'<path d="M-9,0 H5" stroke="{color}" stroke-width="3"/><path d="M3,-5 L10,0 L3,5 Z" fill="{color}"/>'


def sw_svg(markup, scale=1.0):
    return f'<g transform="scale({scale})">{markup}</g>'


def key_box(x, y, items, title="KEY", cols=1, col_w=170, row_h=21, pad=10, size=11, bg="#FFFFFF",
            border="#CFD6DA", title_color="#2B3236", text_color="#2B3236"):
    """A boxed legend. items = [(swatch_markup, label), ...] (swatch centred on 0,0)."""
    rows = -(-len(items) // cols)
    w = pad * 2 + cols * col_w
    h = pad * 2 + 16 + rows * row_h
    out = [f'<g transform="translate({x},{y})">',
           f'<rect width="{w}" height="{h}" rx="8" fill="{bg}" stroke="{border}" stroke-width="1.4"/>',
           T(pad, pad + 11, title, 10, 800, title_color, ls=1.2)]
    for i, (sw, lab) in enumerate(items):
        c, r = divmod(i, rows)
        cx = pad + c * col_w + 11
        cy = pad + 16 + r * row_h + row_h / 2
        out.append(f'<g transform="translate({cx},{cy})">{sw}</g>')
        out.append(T(cx + 18, cy + size * 0.36, lab, size, 600, text_color))
    out.append("</g>")
    return "".join(out)


def label_bg(x, y, w, h, fill="#FFFFFF", opacity=0.92, rx=6):
    """Backdrop so a caption reads cleanly over art."""
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" opacity="{opacity}"/>'
