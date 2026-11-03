#!/usr/bin/env python3
"""Copy print-quality product photos into build/img-src/ from a hunt manifest.

  python3 stage_hires.py <manifest.json>

The manifest is a list (or {"images": [...]}) of {product, code, path, width, height,
source, upscaled}.  Each image is saved as img-src/<CODE>.png (and <key>.png when a
products.py key matches), only when it is taller than what we already have.
Sources are logged to img-src/SOURCES.md so every photo is traceable.
"""
import json
import os
import shutil
import sys

from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import products  # noqa: E402

DST = os.path.join(HERE, "img-src")


def norm(s):
    return "".join(ch for ch in (s or "").lower() if ch.isalnum())


def main(manifest):
    data = json.load(open(manifest))
    items = data.get("images", data) if isinstance(data, dict) else data
    by_code = {}
    by_name = {}
    for k, p in products.P.items():
        code = (p.get("img_src") or "").replace(".png", "")
        if code:
            by_code[code.upper()] = k
        by_name[norm(p["name"])] = k
    os.makedirs(DST, exist_ok=True)
    log = []
    for it in items:
        src = it.get("path")
        if not src or not os.path.exists(src):
            continue
        try:
            w, h = Image.open(src).size
        except Exception:
            continue
        code = (it.get("code") or "").upper().strip()
        key = by_code.get(code) or by_name.get(norm(it.get("product")))
        names = [n for n in ({f"{code}.png"} if code else set()) | ({f"{key}.png"} if key else set())]
        if not names:
            names = [norm(it.get("product")) + ".png"]
        for n in names:
            out = os.path.join(DST, n)
            have = Image.open(out).size[1] if os.path.exists(out) else 0
            if h > have:
                shutil.copyfile(src, out)
                log.append(f"| {n} | {w}x{h} | {'upscaled' if it.get('upscaled') else 'original'} | {it.get('source', '')} |")
    with open(os.path.join(DST, "SOURCES.md"), "a") as f:
        if log:
            f.write("\n| file | px | kind | source |\n|---|---|---|---|\n" + "\n".join(log) + "\n")
    print(f"staged {len(log)} images into {DST}")


if __name__ == "__main__":
    main(sys.argv[1])
