"""NutriDyn product facts for the condition sheets.  One entry per product:
label-checked amounts only (sources noted per entry).  `sched` drives the
"Your daily rhythm" panel: (slot, count, unit) with slot in am / pm / bed.
"""
import glob
import json
import os
import re
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))

ASSETS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "blasts", "assets")
EXTRACTED = os.environ.get("ND_PRODUCT_IMG", "")

P = {
    "gi_integrity": dict(
        name="GI Integrity", size="About 28 servings &middot; Peach Tea, Berry or Chocolate",
        img_src="gi-integrity.png",
        key="3 g L-glutamine, 16 mg zinc (as zinc carnosine), 400 mg DGL, 300 mg aloe, 200 mg slippery elm, marshmallow, okra, no added sugar",
        dose="1 scoop daily", dosesub="in 6 to 8 oz water", sched=[("am", 1, "scoop")],
        src="NutriDyn practice kit, label panel (one scoop, 8.5 g)"),
    "ultrabiotic_dms": dict(
        name="UltraBiotic Daily Multi-Strain", size="Practitioner exclusive",
        img_src=None,
        key="30 billion CFU, seven strains: four Lactobacillus, B. lactis, Bacillus coagulans, Saccharomyces boulardii",
        dose="1 capsule daily", dosesub="", sched=[("bed", 1, "capsule")],
        src="NutriDyn PCOS handout and blast, label read"),
    "mag_glycinate": dict(
        name="Magnesium Glycinate", size="60, 120, 160 or 320 capsules",
        img_src="magnesium-glycinate.png",
        key="260 mg magnesium per 2 capsules, Albion chelated (di-magnesium malate, lysinate glycinate)",
        dose="2 capsules, 1 to 2 times daily", dosesub="with food", sched=[("bed", 2, "capsules")],
        src="NutriDyn magnesium blast 2026-10-12, label read"),
    "gluco_ir": dict(
        name="Gluco IR", size="150 capsules &middot; 30 servings",
        img_src="gluco-ir.png",
        key="100 mg dihydroberberine (GlucoVantage), 300 mg alpha lipoic acid, 500 mg Ceylon cinnamon, 600 mcg chromium, 200 mg gymnema, green tea",
        dose="5 capsules daily", dosesub="with meals", sched=[("am", 3, "capsules"), ("pm", 2, "capsules")],
        src="NutriDyn blood sugar handout, label read"),
    "immunity_pro": dict(
        name="Immunity Pro", size="Practitioner exclusive",
        img_src="immunity-pro.png",
        key="250 mg Wellmune beta-glucan, 85 mg FiberAid larch arabinogalactan",
        dose="1 capsule daily", dosesub="", sched=[("am", 1, "capsule")],
        src="NutriDyn beta-glucan blast 2026-11-09, label read"),
}


def _x(code):
    return f"{code}.png"

P.update({
    "gi_defend": dict(name="GI Defend", size="Practitioner exclusive &middot; powder", img_src=_x("R191"),
        key="2.5 g ImmunoLin serum-derived bovine immunoglobulin per scoop", dose="1 scoop daily", dosesub="before breakfast",
        sched=[("am", 1, "scoop")], src="switch chart (Microbiome Labs) label read; NutriDyn 60-day protocol"),
    "curcumin_bcm95": dict(name="Curcumin 400X", size="Practitioner exclusive &middot; softgels", img_src=_x("R268"),
        key="800 mg curcumin per 2 softgels, an enhanced-absorption form", dose="2 softgels daily", dosesub="with breakfast",
        sched=[("am", 2, "softgels")], src="product DB from switch charts (R268); NutriDyn protocol doc lists Curcumin 400x"),
    "enzymes": dict(name="Digestive Vegetarian", size="180 capsules", img_src=_x("R712"),
        key="Per 2 capsules: 24,000 DU amylase, 20,000 PC + 4,100 HUT protease, 800 LU lipase, 400 ALU lactase, 2,000 CU cellulase",
        dose="2 capsules", dosesub="with your largest meal", sched=[("pm", 2, "capsules")], src="switch chart (Pure) label read"),
    "zinc_carnosine": dict(name="Zinc-Carnosine", size="60 capsules", img_src=_x("R154"),
        key="75 mg zinc-carnosine complex: 17 mg zinc + 58 mg L-carnosine", dose="1 capsule twice daily", dosesub="between meals",
        sched=[("am", 1, "capsule"), ("pm", 1, "capsule")], src="switch chart (Metagenics) label read"),
    "methyl_b": dict(name="Methyl Complete", size="120 capsules", img_src=_x("R187"),
        key="Per 2 capsules: 1 mg B12 (methyl + adenosyl), 800 mcg DFE folate as L-5-MTHF, 10 mg P5P, 700 mg TMG, 500 mg NAC",
        dose="2 capsules daily", dosesub="with breakfast", sched=[("am", 2, "capsules")], src="switch chart (Pure) label read"),
    "berberine": dict(name="Berberine Pro", size="90 capsules", img_src="berberine-pro.png",
        key="100 mg dihydroberberine + 84 mg organic cinnamon extract per capsule", dose="1 capsule 3 times daily", dosesub="before meals",
        sched=[("am", 1, "capsule"), ("pm", 2, "capsules")], src="switch chart (DFH) label read"),
    "d3_5000_k2": dict(name="D3 5000 with K2", size="60 capsules", img_src="d3-5000-with-k2.png",
        key="5,000 IU vitamin D3, 60 mcg vitamin K2 (MK-7), 15 mcg vitamin K1", dose="1 capsule daily", dosesub="with your evening meal",
        sched=[("pm", 1, "capsule")], src="switch chart (DFH) label read"),
    "omega_1000": dict(name="Omega Pure EPA-DHA 1000", size="120 softgels", img_src="omega-pure-epa-dha-1000.png",
        key="1,000 mg EPA + DHA per softgel (730 mg EPA, 270 mg DHA)", dose="1 softgel daily", dosesub="with your evening meal",
        sched=[("pm", 1, "softgel")], src="switch chart (Pure) label read"),
    "coq10": dict(name="CoQ10 Ubiquinol", size="30 softgels", img_src=_x("R350U"),
        key="100 mg ubiquinol, the ready-to-use form of CoQ10, per softgel", dose="1 softgel daily", dosesub="with food",
        sched=[("am", 1, "softgel")], src="switch chart (Pure) label read"),
    "mito": dict(name="Mito Recharge", size="90 capsules", img_src=_x("R167"),
        key="Per 3 capsules: 200 mg acetyl-L-carnitine, 100 mg NAC, 45 mg R-lipoic + 75 mg alpha lipoic acid, 100 mg resveratrol, 100 mg EGCG",
        dose="3 capsules daily", dosesub="with breakfast", sched=[("am", 3, "capsules")], src="switch chart (Ortho) label read"),
    "lipo_flow": dict(name="Lipo-Flow", size="Practitioner exclusive &middot; tablets", img_src=_x("R863"),
        key="Lipotropic liver formula with 200 mg beet root per 2 tablets", dose="2 tablets with meals", dosesub="up to 3 times daily",
        sched=[("am", 2, "tablets"), ("pm", 2, "tablets")], src="switch chart (Standard Process) label read"),
    "glutathione": dict(name="Liposomal Glutathione", size="Liquid", img_src=_x("R2188"),
        key="100 mg glutathione per 1 mL dropper, liposomal for absorption", dose="1 dropper, 2 to 4 times daily", dosesub="shake well",
        sched=[("am", 1, "dropper"), ("pm", 1, "dropper")], src="switch chart (Pure) label read"),
    "nac600": dict(name="NAC-600", size="60 capsules", img_src=_x("R280"),
        key="600 mg N-acetyl-L-cysteine per capsule, the building block of glutathione", dose="1 capsule daily", dosesub="",
        sched=[("am", 1, "capsule")], src="switch chart (Pure/IT) label read"),
    "inositol": dict(name="Myo-Inositol Complex", size="180 capsules", img_src=_x("R279"),
        key="Myo-inositol blend; follow the label for capsules per serving", dose="As directed", dosesub="split morning and evening",
        sched=[("am", 1, "serving"), ("pm", 1, "serving")], src="switch chart (Pure) official match"),
    "ultrabiotic_xs": dict(name="UltraBiotic Daily Extra Strength", size="Practitioner exclusive", img_src=_x("R892"),
        key="60 billion CFU per capsule, two strains at 30 billion each", dose="1 capsule daily", dosesub="at bedtime",
        sched=[("bed", 1, "capsule")], src="switch chart (Ortho) label read"),
})
P["ultrabiotic_dms"].update(img_src=_x("R829"), key="30 billion CFU, seven strains: S. boulardii, L. reuteri, B. lactis, L. plantarum, L. acidophilus, L. gasseri, B. coagulans")

# ---------------------------------------------------------------- product links
# Product photos and names link to the product page.  nutridyn.com slugs come
# from the NutriDyn 60-day protocol doc (Drive, 2025); others fall back to a
# catalog search.  LINK_BASE can later point at an OpenFunctional storefront.
LINK_BASE = os.environ.get("ND_LINK_BASE", "https://nutridyn.com/")
SLUGS = {
    "gi_defend": "dynamic-gi-defend-r191", "ultrabiotic_dms": "ultrabiotic-daily-multi-strain",
    "curcumin_bcm95": "curcumin-400x-r268", "d3_5000_k2": "d3-5000-with-k2", "omega_1000": "omega-pure-epa-dha-1000",
    "mag_glycinate": "magnesium-glycinate", "lipo_flow": "lipo-flow", "methyl_b": "methyl-complete-r187",
    "mito": "mito-recharge-r167", "immunity_pro": "immunity-pro", "inflam_eze": "inflam-eze-plus",
}


def url_for(k, p):
    if p.get("url"):
        return p["url"]
    if k in SLUGS:
        return LINK_BASE + SLUGS[k]
    from urllib.parse import quote_plus
    return LINK_BASE + "catalogsearch/result/?q=" + quote_plus(re.sub(r"<[^>]+>|&[a-z]+;", " ", p["name"]).strip())


# ---------------------------------------------------------------- per-sheet additions
# Sheet agents add products in products.d/<slug>.json ({"key": {...same fields...}})
# so nobody edits this shared file in parallel.
for _f in sorted(glob.glob(os.path.join(HERE, "products.d", "*.json"))):
    try:
        _d = json.load(open(_f))
    except Exception as _e:  # a half-written file from a parallel editor must not break other builds
        print(f"WARNING: skipped {os.path.basename(_f)}: {_e}")
        continue
    for _k, _v in _d.items():
        if _k in P:
            P[_k].update(_v)
        else:
            P[_k] = _v

PLACEHOLDER = dict(name="[product]", size="", img_src=None, key="[label facts]", dose="[dose]", dosesub="", sched=[], placeholder=True)


def get(k):
    p = P.get(k, dict(PLACEHOLDER, name=f"[{k}]"))
    p.setdefault("href", url_for(k, p))
    return p


def check_complete(keys):
    return sorted({k for k in keys if k not in P or P[k].get("placeholder")})


HIRES = os.path.join(HERE, "img-src")  # committed print-quality sources: <key>.png or <CODE>.png
MIN_PRINT_PX = 600


def stage_images(dst, report=None):
    """Copy the best image per product into img/ and set p['img'] (relative to
    the edition folder) and p['img_px'] (pixel height)."""
    from PIL import Image
    for k, p in P.items():
        cands = []
        code = (p.get("img_src") or "").replace(".png", "")
        for base, names in ((HIRES, [f"{k}.png", f"{code}.png", p.get("img_src") or ""]),
                            (ASSETS, [p.get("img_src") or ""]), (EXTRACTED, [p.get("img_src") or ""])):
            for n in names:
                if base and n:
                    c = os.path.join(base, n)
                    if os.path.exists(c):
                        cands.append(c)
        best, best_h = None, 0
        for c in cands:
            try:
                h = Image.open(c).size[1]
            except Exception:
                continue
            if h > best_h:
                best, best_h = c, h
        name = f"nd-{k.replace('_', '-')}.png"
        if best:
            out = os.path.join(dst, name)
            if not (os.path.exists(out) and os.path.getsize(out) == os.path.getsize(best)):
                tmpf = out + f".{os.getpid()}.tmp"
                shutil.copyfile(best, tmpf)
                os.replace(tmpf, out)
            p["img"] = f"../img/{name}"
            p["img_px"] = best_h
        else:
            p["img"] = "../img/nd-missing.png"
            p["img_px"] = 0
        if report is not None:
            report[k] = (best_h, best)
    PLACEHOLDER["img"] = "../img/nd-missing.png"
