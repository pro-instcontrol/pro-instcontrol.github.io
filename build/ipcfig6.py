# -*- coding: utf-8 -*-
"""Aggregated vector figures for IPC Chapter 6, "Process Control".

Three supplier modules (1-9, 10-18, 19-26) register their evaluated
5-tuples in ``ipcfig6_common.make_registry()``. This module merges them and
exposes the conventional ``fig_fNN()`` callables to prose writers and the
page builder.
"""
import importlib

FIGS = {}

for _mod in ("ipcfig6_a", "ipcfig6_b", "ipcfig6_c"):
    try:
        _supplier = importlib.import_module(_mod)
    except ImportError as exc:
        print("ipcfig6: %s not available yet (%s)" % (_mod, exc))
        continue
    FIGS.update(_supplier.FIGS)

for _name, _tuple in FIGS.items():
    globals()[_name] = (lambda _t=_tuple: _t)
