# -*- coding: utf-8 -*-
"""Aggregated vector figures for IPC Chapter 2, "Transducers - II".

The 58 figures are produced by three supplier modules (1-20, 21-40, 41-58)
that register evaluated 5-tuples in ``ipcfig2_common.make_registry()``.  This
module merges the registries and exposes the conventional ``fig_fNN()``
callable for the prose writers and the page builder.
"""
import importlib

FIGS = {}

for _mod in ("ipcfig2_a", "ipcfig2_b", "ipcfig2_c"):
    try:
        _supplier = importlib.import_module(_mod)
    except ImportError as exc:
        print("ipcfig2: %s not available yet (%s)" % (_mod, exc))
        continue
    FIGS.update(_supplier.FIGS)

for _name, _tuple in FIGS.items():
    globals()[_name] = (lambda _t=_tuple: _t)
