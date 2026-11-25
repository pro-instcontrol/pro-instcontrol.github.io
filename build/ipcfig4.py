# -*- coding: utf-8 -*-
"""Aggregated vector figures for IPC Chapter 4, "Telemetry".

Two supplier modules (1-15, 16-30) register their evaluated 5-tuples in
``ipcfig4_common.make_registry()``. This module merges them and exposes the
conventional ``fig_fNN()`` callables to prose writers and the page builder.
"""
import importlib

FIGS = {}

for _mod in ("ipcfig4_a", "ipcfig4_b"):
    try:
        _supplier = importlib.import_module(_mod)
    except ImportError as exc:
        print("ipcfig4: %s not available yet (%s)" % (_mod, exc))
        continue
    FIGS.update(_supplier.FIGS)

for _name, _tuple in FIGS.items():
    globals()[_name] = (lambda _t=_tuple: _t)
