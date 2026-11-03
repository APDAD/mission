"""Loads every condition sheet module in this folder.  One module = one sheet
(front art + copy + back data), so sheets can be edited in parallel without
touching each other.  Each module exposes SHEET (dict) with an 'order' key.
A module that fails to import (for example mid-edit by another agent) is skipped
with a warning so it cannot break anyone else's build."""
import importlib
import os
import pkgutil
import traceback

HERE = os.path.dirname(os.path.abspath(__file__))


def load(strict=()):
    sheets = []
    for m in pkgutil.iter_modules([HERE]):
        if m.name.startswith("_"):
            continue
        try:
            mod = importlib.import_module(f"conditions.{m.name}")
        except Exception:
            if m.name in strict:
                raise
            print(f"WARNING: skipped conditions/{m.name}.py (import failed):\n" + traceback.format_exc(limit=2))
            continue
        s = getattr(mod, "SHEET", None)
        if s and not s.get("disabled"):
            s.setdefault("module", m.name)
            sheets.append(s)
    return sorted(sheets, key=lambda s: (s.get("order", 99), s["slug"]))
