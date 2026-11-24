# -*- coding: utf-8 -*-
"""Aggregated vector figures for PPIC Chapter 4 (fuzzy fault detection).

Three supplier modules (figs 1-4, 5-8, 9-11) register their evaluated
5-tuples in ``ppicfig4_common.make_registry()``. This module merges them and
exposes the conventional ``fig_fNN()`` callables to prose writers and the
page builder.
"""
import importlib

FIGS = {}

for _mod in ("ppicfig4_a", "ppicfig4_b", "ppicfig4_c"):
    try:
        _supplier = importlib.import_module(_mod)
    except ImportError as exc:
        print("ppicfig4: %s not available yet (%s)" % (_mod, exc))
        continue
    FIGS.update(_supplier.FIGS)

for _name, _tuple in FIGS.items():
    globals()[_name] = (lambda _t=_tuple: _t)
