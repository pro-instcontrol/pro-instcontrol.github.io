# -*- coding: utf-8 -*-
"""Aggregated vector figures for PPIC Chapter 8 (coal-bucket dampers).

Three supplier modules register their evaluated 5-tuples via
``ppicfig8_common.make_registry()``; this module merges them and exposes the
conventional ``fig_fNN()`` callables to prose writers and the page builder.
"""
import importlib

FIGS = {}

for _mod in ("ppicfig8_a", "ppicfig8_b", "ppicfig8_c"):
    try:
        _supplier = importlib.import_module(_mod)
    except ImportError as exc:
        print("ppicfig8: %s not available yet (%s)" % (_mod, exc))
        continue
    FIGS.update(_supplier.FIGS)

for _name, _tuple in FIGS.items():
    globals()[_name] = (lambda _t=_tuple: _t)
