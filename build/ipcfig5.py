# -*- coding: utf-8 -*-
"""Aggregated vector figures for IPC Chapter 5, "Signal Conditioning and
Data Acquisition System".

Four supplier modules (1-11, 12-22, 23-33, 34-43) register their evaluated
5-tuples in ``ipcfig5_common.make_registry()``. This module merges them and
exposes the conventional ``fig_fNN()`` callables to prose writers and the page
builder.
"""
import importlib

FIGS = {}

for _mod in ("ipcfig5_a", "ipcfig5_b", "ipcfig5_c", "ipcfig5_d"):
    try:
        _supplier = importlib.import_module(_mod)
    except ImportError as exc:
        print("ipcfig5: %s not available yet (%s)" % (_mod, exc))
        continue
    FIGS.update(_supplier.FIGS)

for _name, _tuple in FIGS.items():
    globals()[_name] = (lambda _t=_tuple: _t)
