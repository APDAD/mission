"""Shared kit for the NutriDyn condition sheets: palette, CSS, logo, line icons,
page frames and product cards.  Generated pages only; edit content.py / art.py
and re-run build.py.  Nothing in here may carry account data: this repo is public.
"""
import html

E = html.escape

BRAND_GREEN = "#14664D"
BRAND_CORAL = "#F15F3F"

# One theme per condition family, mirroring the colour-coded sheet families
# pharmacists already file by (gut / reflux / cardiometabolic / immune).
THEMES = {
    "gut":    {"c1": "#0E6A7A", "c2": "#2C8DB4", "soft": "#E3F1F4", "deep": "#0A4B57", "tint": "#F2F8F9"},
    "teal":   {"c1": "#13827C", "c2": "#3A9FC4", "soft": "#E2F2F0", "deep": "#0D5A56", "tint": "#F1F8F7"},
    "gerd":   {"c1": "#CF4A1C", "c2": "#EE9A2E", "soft": "#FCEADB", "deep": "#8E3110", "tint": "#FEF6EF"},
    "metab":  {"c1": "#8A1B22", "c2": "#C2392E", "soft": "#F6E4E1", "deep": "#62121A", "tint": "#FBF3F2"},
    "immune": {"c1": "#4A2B80", "c2": "#7A52B3", "soft": "#EDE6F6", "deep": "#34205C", "tint": "#F7F3FB"},
    # families for the next wave (pain and movement, brain and nerves, hormones)
    "msk":     {"c1": "#1F5E8C", "c2": "#2E8FC8", "soft": "#E3EEF6", "deep": "#123F60", "tint": "#F2F7FB"},
    "neuro":   {"c1": "#3D4E6B", "c2": "#5F7CA8", "soft": "#E6EAF2", "deep": "#26324A", "tint": "#F4F6FA"},
    "hormone": {"c1": "#9B3F68", "c2": "#C96A8E", "soft": "#F6E6EE", "deep": "#6E2747", "tint": "#FBF3F7"},
    "energy":  {"c1": "#B06A12", "c2": "#E0A030", "soft": "#FAEFD9", "deep": "#7A480A", "tint": "#FDF8EE"},
}

# NutriDyn wordmark (vector, from the brand file in peptide-seminar/).  The
# wordmark paths use currentColor; the mark stays coral.
LOGO_SVG = open(__file__.rsplit("/", 1)[0] + "/../../../peptide-seminar/nutridyn-logo.svg").read()


def logo(height="0.30in", color=BRAND_GREEN):
    svg = LOGO_SVG.replace("<svg ", f'<svg style="height:{height};width:auto;color:{color};display:block" ', 1)
    svg = svg.replace('width="174" height="31" ', "")
    return svg


# ---------------------------------------------------------------- line icons
# 64x64 viewBox, stroked with currentColor.  class="x" paths draw in coral
# (used for "avoid / limit" slashes).
ICONS = {
    "plate": '<circle cx="34" cy="34" r="19"/><circle cx="34" cy="34" r="11"/><path d="M9 12v11a3.5 3.5 0 0 0 7 0V12M12.5 23v29"/><path d="M58 12c-4 3-5 9-5 14h5v26"/>',
    "leaf": '<path d="M12 52C12 27 28 12 54 10c-1 25-16 41-42 42z"/><path d="M12 52 40 24"/><path d="M26 38h10M33 31h9"/>',
    "apple": '<path d="M32 21c-6-4-19-3-19 12 0 12 8 23 14 23 2 0 3-1 5-1s3 1 5 1c6 0 14-11 14-23 0-15-13-16-19-12z"/><path d="M32 21c0-5 2-9 6-11"/><path d="M35 16c4-3 9-2 11 0-3 3-8 4-11 0z"/>',
    "wheat": '<path d="M32 58V10"/><path d="M32 24c-6 0-10-4-10-9 6 0 10 4 10 9zM32 24c6 0 10-4 10-9-6 0-10 4-10 9zM32 36c-6 0-10-4-10-9 6 0 10 4 10 9zM32 36c6 0 10-4 10-9-6 0-10 4-10 9zM32 48c-6 0-10-4-10-9 6 0 10 4 10 9zM32 48c6 0 10-4 10-9-6 0-10 4-10 9z"/>',
    "drop": '<path d="M32 7C24 21 15 30 15 41a17 17 0 0 0 34 0C49 30 40 21 32 7z"/><path d="M24 43a8 8 0 0 0 8 8"/>',
    "moon": '<path d="M45 41A20 20 0 0 1 25 14a21 21 0 1 0 20 27z"/><path d="M40 11h9l-9 9h9M51 25h6l-6 6h6"/>',
    "breath": '<path d="M7 23h30a7 7 0 1 0-7-7M7 33h41a7 7 0 1 1-7 7M7 43h20"/>',
    "walk": '<circle cx="37" cy="10" r="5"/><path d="M35 18l-6 16 8 6 4 17M29 34l-7 21M35 22l10 8 8-2M33 22l-11 6-4 8"/>',
    "dumbbell": '<path d="M9 26v12M16 19v26M48 19v26M55 26v12M16 32h32"/>',
    "glass": '<path d="M21 8h22c0 13-5 21-11 21S21 21 21 8zM32 29v20M23 55h18"/><path class="x" d="M10 55 54 9"/>',
    "sugar": '<path d="M13 24 32 14l19 10v21L32 55 13 45z"/><path d="M13 24l19 10 19-10M32 34v21"/><path class="x" d="M8 56 56 8"/>',
    "scale": '<rect x="10" y="10" width="44" height="44" rx="10"/><path d="M21 25a13 13 0 0 1 22 0"/><path d="M32 25l5-7"/><path d="M24 44h16"/>',
    "clock": '<circle cx="32" cy="32" r="23"/><path d="M32 17v15l10 6"/>',
    "bed": '<path d="M6 49h52M10 49V22M54 49V36M10 41l44-7"/><rect x="13" y="28" width="11" height="7" rx="3"/><path d="M40 10v13M34 16l6-6 6 6"/>',
    "portion": '<circle cx="32" cy="32" r="22"/><circle cx="32" cy="32" r="9"/><path d="M14 14l7 7M50 14l-7 7M14 50l7-7M50 50l-7-7"/>',
    "smoke": '<rect x="7" y="33" width="40" height="9" rx="2"/><path d="M39 33v9M53 28v19M59 31v13"/><path class="x" d="M10 56 54 10"/>',
    "mouthwash": '<path d="M26 7h12v8l6 8v33H20V23l6-8z"/><path d="M20 34h24"/><path class="x" d="M8 56 56 8"/>',
    "nose": '<path d="M30 7c0 14-12 25-12 34 0 5 5 7 10 7 3 0 5-2 7-2"/><path d="M42 30h15M44 38h13M42 46h15"/>',
    "sun": '<circle cx="32" cy="32" r="10"/><path d="M32 5v8M32 51v8M5 32h8M51 32h8M13 13l6 6M45 45l6 6M13 51l6-6M45 19l6-6"/>',
    "coffee": '<path d="M11 25h33v13a14 14 0 0 1-14 14h-5a14 14 0 0 1-14-14z"/><path d="M44 29h4a6 6 0 0 1 0 12h-4"/><path d="M21 8c-2 4 2 6 0 11M30 8c-2 4 2 6 0 11"/>',
    "salt": '<path d="M21 26h22l-3 30H24z"/><path d="M21 26c0-9 5-15 11-15s11 6 11 15"/><path d="M28 18h1M35 18h1M31.5 15h1"/><path class="x" d="M9 56 55 10"/>',
    "beet": '<path d="M32 23c10 0 17 7 17 16S40 56 32 58c-8-2-17-10-17-19s7-16 17-16z"/><path d="M32 23c-2-6-8-11-15-11 0 7 7 11 15 11zM32 23c2-6 8-11 15-11 0 7-7 11-15 11zM32 23V8"/>',
    "heartpulse": '<path d="M32 54S10 40 10 24a11 11 0 0 1 22-3 11 11 0 0 1 22 3c0 16-22 30-22 30z"/><path d="M13 32h10l4-8 6 16 4-8h14"/>',
    "rx": '<rect x="15" y="7" width="34" height="10" rx="2"/><path d="M19 17h26v36a4 4 0 0 1-4 4H23a4 4 0 0 1-4-4z"/><path d="M26 28v16M26 28h6a4 4 0 0 1 0 8h-6M31 36l8 9M39 36l-8 9"/>',
    "jar": '<path d="M20 13h24v6l4 6v29a4 4 0 0 1-4 4H20a4 4 0 0 1-4-4V25l4-6z"/><path d="M16 34h32M22 43c2-2 4 2 6 0s4 2 6 0 4 2 6 0"/>',
    "shirt": '<path d="M23 8 9 15l4 30h8V27v29h22V27v18h8l4-30-14-7c-2 4-6 6-9 6s-7-2-9-6z"/>',
    "dryer": '<rect x="12" y="7" width="40" height="50" rx="4"/><circle cx="32" cy="36" r="12"/><path d="M12 17h40"/><path d="M28 32c-2 3 2 5 0 8M36 32c-2 3 2 5 0 8"/>',
    "shower": '<path d="M12 57V20a10 10 0 0 1 20 0"/><path d="M23 20h18"/><path d="M27 28v4M33 28v4M39 28v4M30 38v4M36 38v4M27 48v4M33 48v4M39 48v4"/>',
    "paw": '<circle cx="19" cy="23" r="5"/><circle cx="32" cy="16" r="5"/><circle cx="45" cy="23" r="5"/><path d="M32 30c-8 0-15 9-15 15 0 6 7 8 15 6 8 2 15 0 15-6 0-6-7-15-15-15z"/>',
    "house": '<path d="M7 30 32 10l25 20M13 26v29h38V26"/><path d="M32 30c-4 6-7 9-7 13a7 7 0 0 0 14 0c0-4-3-7-7-13z"/>',
    "filter": '<rect x="9" y="11" width="46" height="42" rx="4"/><path d="M9 21h46M9 32h46M9 43h46M20 11v42M32 11v42M44 11v42"/>',
    "sauna": '<path d="M7 51h50M13 51V40h38v11"/><path d="M20 31c-3-4 3-6 0-10s3-6 0-10M32 31c-3-4 3-6 0-10s3-6 0-10M44 31c-3-4 3-6 0-10s3-6 0-10"/>',
    "plastic": '<path d="M26 6h12v6l4 6v38H22V18l4-6z"/><path d="M22 30h20M22 40h20"/><path class="x" d="M8 56 56 8"/>',
    "fish": '<path d="M14 32c8-10 17-14 26-14 9 0 15 7 19 14-4 7-10 14-19 14-9 0-18-4-26-14z"/><path d="M14 32 5 24v16z"/><circle cx="46" cy="29" r="1.6"/>',
    "sensitive": '<path d="M12 15h17l-2 40H14z"/><path d="M13 27h15"/><path d="M46 57V24M46 32c-5 0-8-3-8-7 5 0 8 3 8 7zM46 32c5 0 8-3 8-7-5 0-8 3-8 7zM46 43c-5 0-8-3-8-7 5 0 8 3 8 7zM46 43c5 0 8-3 8-7-5 0-8 3-8 7z"/>',
    "clipboard": '<rect x="14" y="10" width="36" height="47" rx="4"/><path d="M24 10V6h16v4M21 25l4 4 8-8M21 41l4 4 8-8M37 27h7M37 43h7"/>',
    "brain": '<path d="M30 12a8 8 0 0 0-14 4 8 8 0 0 0-5 13 8 8 0 0 0 3 13 8 8 0 0 0 12 6 6 6 0 0 0 4-2z"/><path d="M34 12a8 8 0 0 1 14 4 8 8 0 0 1 5 13 8 8 0 0 1-3 13 8 8 0 0 1-12 6 6 6 0 0 1-4-2z"/><path d="M32 12v38"/>',
    "battery": '<rect x="7" y="19" width="44" height="26" rx="4"/><path d="M51 27h6v10h-6"/><rect x="12" y="24" width="9" height="16" rx="1" fill="currentColor" stroke="none"/>',
    "bone": '<path d="M20 44 44 20"/><path d="M16 40a6 6 0 1 0 1 9 6 6 0 1 0 8-8M48 24a6 6 0 1 0-1-9 6 6 0 1 0-8 8"/>',
    "flame": '<path d="M32 6c2 10 15 16 15 30a15 15 0 0 1-30 0c0-8 6-12 8-18 2 6 6 9 6 9s1-13 1-21z"/>',
    "headache": '<path d="M38 57V47h6l2-10-4-4c0-14-8-23-20-23S8 19 8 31c0 8 4 12 8 16v10"/><path d="M50 7l-5 9h7l-5 9"/>',
    "dna": '<path d="M22 6c0 14 20 18 20 32s-20 14-20 20M42 6c0 14-20 18-20 32s20 14 20 20M25 14h14M25 50h14M27 22h10M27 42h10"/>',
    "gut": '<path d="M27 6v12c0 6-12 7-12 19 0 10 8 17 18 17 12 0 20-8 20-18 0-8-6-12-12-12s-9 4-15 4"/><path d="M22 44c3 2 6 2 9 0s6-2 9 0"/>',
    "heart": '<path d="M32 54S10 40 10 24a11 11 0 0 1 22-3 11 11 0 0 1 22 3c0 16-22 30-22 30z"/>',
    "kidney": '<path d="M26 10c-10 0-16 10-16 22s6 22 16 22c6 0 8-6 6-12-2-4-6-6-6-10s4-6 6-10c2-6 0-12-6-12z"/><path d="M38 10c10 0 16 10 16 22s-6 22-16 22c-6 0-8-6-6-12 2-4 6-6 6-10s-4-6-6-10c-2-6 0-12 6-12z"/>',
    "hormone": '<circle cx="23" cy="28" r="10"/><path d="M23 38v15M17 47h12"/><circle cx="41" cy="34" r="10"/><path d="M48 27l8-8M49 19h7v7"/>',
    "age": '<circle cx="27" cy="9" r="5"/><path d="M27 16c-4 10-4 18 2 24l-4 17M29 40l6 17M26 24l12 8"/><path d="M42 32v25M42 32c0-3 4-3 4 0"/>',
    "burger": '<path d="M11 28c0-10 10-16 21-16s21 6 21 16z"/><path d="M9 35h46M12 41h40a4 4 0 0 1-4 7H16a4 4 0 0 1-4-7z"/>',
    "waist": '<path d="M20 7c-4 10-4 18 0 25s4 15 0 25M44 7c4 10 4 18 0 25s-4 15 0 25"/><path d="M13 32h38"/><path d="M19 29v6M25 29v6M31 29v6M37 29v6M43 29v6"/>',
    "tube": '<path d="M21 8v36a8 8 0 0 0 16 0V8M17 8h24M21 30h16"/><path d="M51 42V16M45 22l6-6 6 6"/>',
    "meter": '<rect x="16" y="6" width="32" height="52" rx="6"/><rect x="22" y="12" width="20" height="14" rx="2"/><path d="M32 33c-3 5-5 8-5 11a5 5 0 0 0 10 0c0-3-2-6-5-11z"/>',
    "microbe": '<circle cx="32" cy="32" r="12"/><path d="M32 8v8M32 48v8M8 32h8M48 32h8M15 15l6 6M43 43l6 6M15 49l6-6M43 21l6-6"/><circle cx="28" cy="29" r="2" fill="currentColor" stroke="none"/><circle cx="36" cy="36" r="2" fill="currentColor" stroke="none"/>',
    "warning": '<path d="M32 8 58 54H6z"/><path d="M32 24v15M32 47v1"/>',
    "capsule": '<path d="M19 45a9 9 0 0 1 0-13l13-13a9 9 0 0 1 13 13L32 45a9 9 0 0 1-13 0z"/><path d="M25.5 25.5l13 13"/>',
    "calendar": '<rect x="10" y="12" width="44" height="42" rx="4"/><path d="M10 24h44M22 8v8M42 8v8M19 32l6 6M25 32l-6 6M38 41l6 6M44 41l-6 6"/>',
    "acne": '<circle cx="32" cy="32" r="22"/><circle cx="24" cy="26" r="3"/><circle cx="38" cy="22" r="2"/><circle cx="40" cy="38" r="4"/><circle cx="26" cy="41" r="2"/>',
    "hair": '<path d="M14 50c0-20 8-36 18-36s18 16 18 36"/><path d="M24 20c-2 10-2 22 0 32M32 16v36M40 20c2 10 2 22 0 32"/>',
    "baby": '<circle cx="32" cy="22" r="12"/><path d="M14 56c2-10 9-16 18-16s16 6 18 16"/><path d="M27 21h1M36 21h1M29 27c2 1 4 1 6 0"/>',
    "thermo": '<path d="M27 38V12a5 5 0 0 1 10 0v26a10 10 0 1 1-10 0z"/><path d="M32 22v20"/>',
    "egg": '<path d="M32 8c-10 0-18 16-18 28a18 18 0 0 0 36 0C50 24 42 8 32 8z"/>',
    "tick": '<ellipse cx="32" cy="35" rx="10" ry="13"/><circle cx="32" cy="18" r="5"/><path d="M23 28l-11-6M22 35H9M23 42l-11 7M41 28l11-6M42 35h13M41 42l11 7"/>',
    "bug": '<ellipse cx="32" cy="35" rx="10" ry="13"/><circle cx="32" cy="18" r="5"/><path d="M23 28l-11-6M22 35H9M23 42l-11 7M41 28l11-6M42 35h13M41 42l11 7"/>',
    "lungs": '<path d="M32 10v20M32 30c-4-2-6 2-8 0-4-4-12 0-12 14 0 8 4 12 10 12 8 0 10-6 10-14M32 30c4-2 6 2 8 0 4-4 12 0 12 14 0 8-4 12-10 12-8 0-10-6-10-14"/>',
    "bloodsugar": '<path d="M32 7C24 21 15 30 15 41a17 17 0 0 0 34 0C49 30 40 21 32 7z"/><path d="M24 38h4l3-6 4 12 3-6h4"/>',
    "stethoscope": '<path d="M16 8v14a10 10 0 0 0 20 0V8"/><path d="M26 32v8a12 12 0 0 0 24 0v-6"/><circle cx="50" cy="30" r="5"/>',
}


def html_key(items, title="KEY"):
    """HTML legend row for a diagram.  items = [(css_background, label, shape)] with
    shape in dot | square | hex | ring | line.  Every diagram with symbols needs one
    (or an in-SVG svgkit.key_box)."""
    cells = []
    for bg, lab, *shape in items:
        sh = (shape or ["dot"])[0]
        st = {"dot": "border-radius:50%", "square": "border-radius:2px",
              "hex": "clip-path:polygon(25% 5%,75% 5%,100% 50%,75% 95%,25% 95%,0 50%);border-radius:0",
              "ring": "border-radius:50%;box-shadow:inset 0 0 0 2px #E2463E", "line": "height:4px;width:16px;border-radius:2px"}[sh]
        cells.append(f'<span><i style="background:{bg};{st}"></i>{lab}</span>')
    return f'<div class="keyrow"><b>{title}</b>{"".join(cells)}</div>'


def icon(name, size="0.42in", color="currentColor", sw=3.2):
    body = ICONS[name]
    return (f'<svg class="ic" viewBox="0 0 64 64" style="width:{size};height:{size};color:{color}" '
            f'fill="none" stroke="currentColor" stroke-width="{sw}" stroke-linecap="round" '
            f'stroke-linejoin="round" aria-hidden="true">{body}</svg>')


# ---------------------------------------------------------------------- CSS
CSS = r"""
@page { size: 8.5in 11in; margin: 0; }
*{box-sizing:border-box}
html,body{margin:0;padding:0}
body{background:#E8E5DE;color:#1F2A2E;font-family:Inter,"Helvetica Neue",Arial,sans-serif;
  -webkit-print-color-adjust:exact;print-color-adjust:exact;font-size:9pt;line-height:1.32}
.toolbar{position:sticky;top:0;z-index:5;display:flex;gap:10px;flex-wrap:wrap;align-items:center;
  justify-content:space-between;padding:10px 16px;background:rgba(247,245,240,.96);border-bottom:1px solid #D9D4C8;
  font-size:14px}
.toolbar b{font-family:Merriweather,Georgia,serif;font-size:15px;color:#14664D}
.toolbar .btns{display:flex;gap:8px;flex-wrap:wrap}
.toolbar a,.toolbar button{display:inline-flex;align-items:center;min-height:44px;padding:0 16px;border-radius:99px;
  background:#14664D;color:#fff;text-decoration:none;font:600 14px Inter,sans-serif;border:0;cursor:pointer}
.toolbar a.ghost{background:transparent;color:#14664D;border:1.5px solid #14664D}
.stack{padding:18px 0 40px}
.sheet{width:8.5in;height:11in;margin:0 auto 22px;background:#fff;position:relative;overflow:hidden;
  box-shadow:0 6px 24px rgba(30,30,20,.14);break-after:page;page-break-after:always}
.sheet:last-child{break-after:auto;page-break-after:auto}
@media print{body{background:#fff}.toolbar{display:none}.stack{padding:0}.sheet{margin:0;box-shadow:none;zoom:1!important}}
.inner{position:absolute;inset:0.38in 0.42in 0.36in 0.42in;display:flex;flex-direction:column}
.rule-top{position:absolute;left:0;right:0;top:0;height:0.13in;background:linear-gradient(90deg,var(--c1),var(--c2))}
.rule-top::after{content:"";position:absolute;left:0.42in;right:0.42in;top:0.2in;height:2px;background:var(--c2);opacity:.55}
.rule-bot{position:absolute;left:0;right:0;bottom:0;height:0.13in;background:linear-gradient(90deg,var(--c2),var(--c1))}
h1,h2,h3{margin:0}
.serif{font-family:Merriweather,Georgia,serif}
.headrow{display:flex;justify-content:space-between;align-items:center;margin-top:0.06in}
.series{font:700 7pt Inter,sans-serif;letter-spacing:.16em;text-transform:uppercase;color:var(--deep)}
.fields{display:grid;grid-template-columns:auto 1fr auto 1.25in;gap:6px 10px;align-items:center;margin:0.16in 0 0.1in;
  font:700 8.5pt Inter,sans-serif;color:#2B3236}
.fields span.box{height:0.27in;border-radius:6px;background:#E9ECEE;border:1px solid #D6DBDF}
.title{font-family:Merriweather,Georgia,serif;font-weight:900;color:var(--c1);font-size:30pt;line-height:1.05;
  letter-spacing:-.01em;margin:0.02in 0 0.05in}
.title small{font-size:15pt;font-weight:700;color:var(--deep)}
.intro{font-size:9.4pt;line-height:1.42;color:#2B3236;margin:0 0 0.08in}
.intro b{color:var(--deep)}
.art{display:block;width:100%}
.art svg{display:block;width:100%;height:auto}
.foot{margin-top:auto;display:flex;justify-content:space-between;align-items:flex-end;gap:12px;padding-top:6px;
  font-size:6.6pt;color:#6A747B}
.foot .code{font:600 6.6pt Inter,sans-serif;letter-spacing:.06em;color:#5B666D;text-align:right;white-space:nowrap}
.disc{font-size:6.3pt;color:#5E686F;line-height:1.3;max-width:5.2in}
.disc sup,.mark{color:var(--c1);font-weight:700}

/* back page */
.band{margin:0 -0.42in;padding:0.16in 0.42in 0.18in;background:linear-gradient(120deg,var(--c1),var(--c2));color:#fff;
  position:relative}
.band h2{font-family:Merriweather,Georgia,serif;font-weight:700;font-size:21pt;text-align:center;margin:0 0 0.1in;color:#fff}
.band h2 small{display:block;font-size:10pt;font-weight:700;color:#FFE6D4;margin-top:2px}
.lifes{display:grid;gap:0.1in;align-items:start}
.life{display:flex;flex-direction:column;align-items:center;text-align:center}
.life .disc2{width:0.86in;height:0.86in;border-radius:50%;background:#fff;display:flex;align-items:center;justify-content:center;
  box-shadow:0 2px 0 rgba(0,0,0,.08) inset,0 0 0 3px rgba(255,255,255,.35);color:var(--c1)}
.life.hex .disc2{border-radius:0;clip-path:polygon(25% 3%,75% 3%,100% 50%,75% 97%,25% 97%,0 50%);width:0.98in;height:0.86in}
.life b{display:block;font-family:Merriweather,Georgia,serif;font-size:9.6pt;margin:0.06in 0 0.03in;color:#fff}
.life p{margin:0;font-size:7.5pt;line-height:1.3;color:#F5F7F8}
.checks{display:grid;grid-template-columns:1fr 1fr;gap:0.06in 0.3in;background:#fff;border-radius:10px;padding:0.14in 0.2in;color:#1F2A2E}
.chk{display:flex;gap:8px;align-items:flex-start}
.chk .bx{flex:none;width:0.15in;height:0.15in;border:1.6px solid var(--deep);border-radius:2px;margin-top:2px}
.chk b{font-size:9pt;color:var(--deep)}
.chk ul{margin:2px 0 0;padding:0;list-style:none}
.chk li{font-size:8pt;margin:1px 0;padding-left:15px;position:relative}
.chk li::before{content:"";position:absolute;left:0;top:4px;width:8px;height:8px;border:1.4px solid var(--c2);border-radius:50%}
.ns-title{font-family:Merriweather,Georgia,serif;font-weight:900;color:var(--c1);font-size:19pt;margin:0.14in 0 0.02in;
  display:flex;align-items:baseline;gap:10px}
.ns-title span{font:600 8pt Inter,sans-serif;color:#56626A;letter-spacing:.02em}
.cols{display:grid;gap:0.08in;margin-top:0.06in}
.col{display:flex;flex-direction:column;background:#fff;border-radius:6px;overflow:hidden;
  box-shadow:0 1px 0 #E3E7EA,0 2px 6px rgba(20,30,40,.10);border:1px solid #E1E5E8}
.col .need{background:linear-gradient(160deg,var(--c1),var(--c2));color:#fff;padding:0.07in 0.07in 0.06in;text-align:center;
  min-height:0.5in;display:flex;flex-direction:column;justify-content:center}
.col .need b{font-size:8.2pt;line-height:1.2;display:block}
.col .need i{font-style:normal;font-size:6.8pt;opacity:.92;display:block;margin-top:2px;line-height:1.2}
.col .pick{display:flex;flex-direction:column;align-items:center;padding:0.06in 0.07in 0.04in;background:var(--tint)}
.col .pick img{height:0.98in;width:auto;max-width:100%;object-fit:contain;display:block;filter:drop-shadow(0 2px 2px rgba(0,0,0,.12))}
.col .pick .nm{font:800 8.6pt Inter,sans-serif;color:#1A2226;margin-top:0.04in;text-align:center;line-height:1.15}
.col .pick .sz{font-size:6.6pt;color:#5E696F;text-align:center}
.col .what{padding:0.06in 0.08in 0.05in;flex:1;font-size:7.3pt;line-height:1.28;color:#283035}
.col .what ul{margin:0;padding:0;list-style:none}
.col .what li{position:relative;padding-left:9px;margin:0 0 2px}
.col .what li::before{content:"";position:absolute;left:0;top:4px;width:4px;height:4px;border-radius:50%;background:var(--c2)}
.col .key{border-top:1px dashed #D3DADF;margin-top:4px;padding-top:3px;font-size:6.7pt;color:#3F4A50}
.col .key b{color:var(--deep);font-size:6.5pt;letter-spacing:.06em;text-transform:uppercase}
.col .dose{background:var(--deep);color:#fff;text-align:center;font:700 7.6pt Inter,sans-serif;padding:0.06in 0.05in;line-height:1.2}
.col .dose small{display:block;font-weight:500;font-size:6.4pt;opacity:.9}
.duo{display:grid;grid-template-columns:1.35fr 1fr;gap:0.1in;margin-top:0.1in}
.panel{border:1px solid #DCE2E6;border-radius:8px;padding:0.08in 0.12in;background:#FBFCFC}
.panel h3{font:800 7.4pt Inter,sans-serif;letter-spacing:.14em;text-transform:uppercase;color:var(--c1);margin:0 0 4px}
.rhythm{display:grid;grid-template-columns:repeat(3,1fr);gap:6px}
.slot{background:#fff;border:1px solid #E2E6E9;border-radius:6px;padding:5px 6px}
.slot .when{font:800 7pt Inter,sans-serif;color:var(--deep);display:flex;align-items:center;gap:4px}
.slot .when svg{width:13px;height:13px}
.slot ul{margin:3px 0 0;padding:0;list-style:none}
.slot li{font-size:7pt;line-height:1.25;margin:1px 0}
.slot li em{font-style:normal;color:#5E696F}
.total{font-size:7pt;color:#3F4A50;margin-top:4px}
.total b{color:var(--deep)}
.rx ul{margin:0;padding:0 0 0 12px}
.rx li{font-size:7.2pt;line-height:1.28;margin:0 0 2px}
.rx li b{color:var(--deep)}
.notes{margin-top:0.1in;border:1px solid #CCD3D8;border-radius:8px;padding:0.07in 0.14in 0.09in;background:#F6F7F8}
.notes b{font-size:8.6pt;color:#4B565C;font-weight:600}
.notes .ln{height:0.24in;border-bottom:1px solid #9FA9AF}
.recby{display:flex;gap:8px;align-items:flex-end;font-size:7pt;color:#4B565C;margin-top:0.08in}
.recby .ln2{flex:1;border-bottom:1px solid #9FA9AF;height:0.18in;font:700 9pt Inter,sans-serif;color:#1F2A2E;padding-left:4px}
.small{font-size:7.2pt;color:#5B666D}
.tag{display:inline-block;font:800 6.6pt Inter,sans-serif;letter-spacing:.1em;text-transform:uppercase;color:#fff;
  background:var(--c1);border-radius:3px;padding:2px 6px}
"""


def theme_vars(theme):
    return ";".join(f"--{k}:{v}" for k, v in THEMES[theme].items())


def page_shell(title, body, theme="gut", extra_css=""):
    vars_ = theme_vars(theme)
    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{E(title)}</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Merriweather:wght@700;900&display=swap" rel="stylesheet">
<style>:root{{{vars_}}}{CSS}{extra_css}</style>
</head><body>
{body}
<script>
// Fit each printable sheet to small screens without horizontal scroll; print is always 1:1.
(function(){{function fit(){{var w=Math.min(1,(window.innerWidth-16)/816);
document.querySelectorAll('.sheet').forEach(function(s){{s.style.zoom=w<1?w:'';}});}}
window.addEventListener('resize',fit);fit();
var p=new URLSearchParams(location.search).get('for');
if(p){{document.querySelectorAll('[data-for]').forEach(function(e){{e.textContent=p.slice(0,80);}});}}}})();
</script>
</body></html>"""


def toolbar(label, pdf_href, back_href="index.html"):
    return (f'<div class="toolbar"><b>{E(label)}</b><div class="btns">'
            f'<a class="ghost" href="{back_href}">All sheets</a>'
            f'<a href="{pdf_href}">Download PDF</a>'
            f'<button onclick="window.print()">Print</button></div></div>')
