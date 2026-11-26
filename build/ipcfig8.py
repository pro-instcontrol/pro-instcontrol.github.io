# -*- coding: utf-8 -*-
"""Aggregated vector figures for IPC Chapter 8, "Microprocessor Based Instrumentation System".

Four supplier modules (1-9, 10-18, 19-26, 27-34) register their evaluated
5-tuples in ``ipcfig8_common.make_registry()``. This module merges them and
exposes the conventional ``fig_fNN()`` callables to prose writers and the
page builder.
"""
import importlib

FIGS = {}

for _mod in ("ipcfig8_a", "ipcfig8_b", "ipcfig8_c", "ipcfig8_d"):
    try:
        _supplier = importlib.import_module(_mod)
    except ImportError as exc:
        print("ipcfig8: %s not available yet (%s)" % (_mod, exc))
        continue
    FIGS.update(_supplier.FIGS)

for _name, _tuple in FIGS.items():
    globals()[_name] = (lambda _t=_tuple: _t)
