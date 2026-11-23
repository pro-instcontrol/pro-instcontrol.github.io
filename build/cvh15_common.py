# -*- coding: utf-8 -*-
"""Shared helpers for Chapter 15 "Conversions and Equivalents" section modules.

Chapter 15 is the final data chapter: 31 printed pages (324-355), ZERO figures,
conversion-factor tables plus the book's Index and Additional Resources back
matter.  Table DATA (numbers, factors, formulas, units) is language-neutral
and shared verbatim between EN and VI; only headings, prose, list items, table
HEADERS and captions are localized.  Re-exports the proven cvh13/cvh14 helpers.

Every section module exposes ``section(lang)`` returning one HTML string.
"""
from cvh13_common import T, H, P, LEAD, B, N, TB  # noqa: F401
