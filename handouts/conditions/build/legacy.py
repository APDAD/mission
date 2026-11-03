"""Bridge from the first-draft sheets.py/art.py into per-sheet modules.
A sheet module that has been fully rewritten no longer imports this."""
import copy
import sheets

_BY = {s["slug"]: s for s in sheets.SHEETS}


def get(slug):
    s = _BY[slug]
    out = copy.deepcopy({k: v for k, v in s.items() if k != "front"})
    out["front"] = s["front"]
    return out
