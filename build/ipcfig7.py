# -*- coding: utf-8 -*-
"""Aggregated vector figures for IPC Chapter 7, "Display Devices and Recorders".

Three supplier modules (1-11, 12-22, 23-32) register their evaluated
5-tuples in ``ipcfig7_common.make_registry()``. This module merges them and
exposes the conventional ``fig_fNN()`` callables to prose writers and the
page builder.
"""
import importlib

FIGS = {}

for _mod in ("ipcfig7_a", "ipcfig7_b", "ipcfig7_c"):
    try:
        _supplier = importlib.import_module(_mod)
    except ImportError as exc:
        print("ipcfig7: %s not available yet (%s)" % (_mod, exc))
        continue
    FIGS.update(_supplier.FIGS)

for _name, _tuple in FIGS.items():
    globals()[_name] = (lambda _t=_tuple: _t)
