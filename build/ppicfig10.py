# -*- coding: utf-8 -*-
"""Aggregated vector figures for PPIC Chapter 10 (reliability models).

Three supplier modules register their evaluated 5-tuples in
``ppicfig10_common.make_registry()``. This module merges them and exposes
``fig_f01()`` … ``fig_f05()`` to prose writers and the page builder.
"""
import importlib

FIGS = {}

for _mod in ("ppicfig10_a", "ppicfig10_b", "ppicfig10_c"):
    try:
        _supplier = importlib.import_module(_mod)
    except ImportError as exc:
        print("ppicfig10: %s not available yet (%s)" % (_mod, exc))
        continue
    FIGS.update(_supplier.FIGS)

for _name, _tuple in FIGS.items():
    globals()[_name] = (lambda _t=_tuple: _t)
