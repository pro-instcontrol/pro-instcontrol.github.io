# -*- coding: utf-8 -*-
"""Aggregated vector figures for PPIC Chapter 9, "Predictive Maintenance Based
on Control Charts Applied at Thermoelectric Power Plant".

Three supplier modules (1-4, 5-8, 9-11) register their evaluated 5-tuples in
``ppicfig9_common.make_registry()``. This module merges them and exposes
``fig_f01()`` … ``fig_f11()`` to the prose writers and page builder.
"""
import importlib

FIGS = {}

for _mod in ("ppicfig9_a", "ppicfig9_b", "ppicfig9_c"):
    try:
        _supplier = importlib.import_module(_mod)
    except ImportError as exc:
        print("ppicfig9: %s not available yet (%s)" % (_mod, exc))
        continue
    FIGS.update(_supplier.FIGS)

for _name, _tuple in FIGS.items():
    globals()[_name] = (lambda _t=_tuple: _t)
