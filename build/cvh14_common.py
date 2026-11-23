# -*- coding: utf-8 -*-
"""Shared helpers for Chapter 14 "Pipe Data" section modules.

Chapter 14 is a data reference like Chapter 13: 22 printed pages, ZERO figures,
almost entirely numeric pipe / flange dimension tables.  Table DATA (numbers,
NPS/DN designations, class labels, units) is language-neutral and shared
verbatim between EN and VI; only headings, prose, list items, table HEADERS and
captions are localized.  Re-exports the proven cvh13_common helpers unchanged.

Every section module exposes ``section(lang)`` returning one HTML string.
"""
from cvh13_common import T, H, P, LEAD, B, N, TB  # noqa: F401
