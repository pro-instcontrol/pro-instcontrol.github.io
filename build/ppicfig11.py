# -*- coding: utf-8 -*-
"""Aggregated vector figures for PPIC Chapter 11 (adaptive power control)."""
import importlib

FIGS = {}

for _mod in ("ppicfig11_a", "ppicfig11_b", "ppicfig11_c"):
    try:
        _supplier = importlib.import_module(_mod)
    except ImportError as exc:
        print("ppicfig11: %s not available yet (%s)" % (_mod, exc))
        continue
    FIGS.update(_supplier.FIGS)

for _name, _tuple in FIGS.items():
    globals()[_name] = (lambda _t=_tuple: _t)
