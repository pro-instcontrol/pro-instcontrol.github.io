# -*- coding: utf-8 -*-
"""Aggregated vector figures for IPC Chapter 3, "Transducers - III".

Four supplier modules (1-18, 19-36, 37-54, 55-72) register their evaluated
5-tuples in ``ipcfig3_common.make_registry()``. This module merges them and
exposes the conventional ``fig_fNN()`` callables to prose writers and the page
builder.
"""
import importlib

FIGS = {}

for _mod in ("ipcfig3_a", "ipcfig3_b", "ipcfig3_c", "ipcfig3_d"):
    try:
        _supplier = importlib.import_module(_mod)
    except ImportError as exc:
        print("ipcfig3: %s not available yet (%s)" % (_mod, exc))
        continue
    FIGS.update(_supplier.FIGS)

for _name, _tuple in FIGS.items():
    globals()[_name] = (lambda _t=_tuple: _t)
