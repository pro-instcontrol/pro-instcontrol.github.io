# -*- coding: utf-8 -*-
"""Aggregated vector figures for PPIC Chapter 5 (thorium/uranium HTRs).

Three supplier modules (figs 1-6, 7-12, 13-17) register their evaluated
5-tuples in ``ppicfig5_common.make_registry()``. This module merges them and
exposes the conventional ``fig_fNN()`` callables to prose writers and the page
builder.
"""
import importlib

FIGS = {}

for _mod in ("ppicfig5_a", "ppicfig5_b", "ppicfig5_c"):
    try:
        _supplier = importlib.import_module(_mod)
    except ImportError as exc:
        print("ppicfig5: %s not available yet (%s)" % (_mod, exc))
        continue
    FIGS.update(_supplier.FIGS)

for _name, _tuple in FIGS.items():
    globals()[_name] = (lambda _t=_tuple: _t)
