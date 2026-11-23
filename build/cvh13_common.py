# -*- coding: utf-8 -*-
"""Shared helpers for Chapter 13 "Engineering Data" section modules.

This chapter is a data reference: 42 printed pages, ZERO figures, almost
entirely numeric property tables.  Table DATA (numbers, chemical formulas,
compound symbols, units) is language-neutral and is shared verbatim between
the EN and VI pages; only headings, prose, list items, table HEADERS and
captions are language-specific.  These helpers make that split explicit so a
section module cannot accidentally leak Vietnamese into the English table.

Every section module exposes ``section(lang)`` returning one HTML string.
"""
import cvh6_common as C


def T(vi, en, lang):
    """Pick the Vietnamese or English rendering of one fragment."""
    return vi if lang == "vi" else en


def H(vi, en, lang, lvl=2):
    """Localized heading; lvl is 2, 3 or 4."""
    return {2: C.h2, 3: C.h3, 4: C.h4}[lvl](T(vi, en, lang))


def P(vi, en, lang):
    """Localized paragraph."""
    return C.p(T(vi, en, lang))


def LEAD(vi, en, lang):
    return C.lead(T(vi, en, lang))


def B(vi_items, en_items, lang, cls=""):
    """Localized bulleted list from parallel VI/EN item lists."""
    return C.ul([T(a, b, lang) for a, b in zip(vi_items, en_items)], cls=cls)


def N(vi, en, lang):
    """Localized note box."""
    return C.note(T(vi, en, lang))


def TB(hdr_vi, hdr_en, rows, lang, cap_vi="", cap_en=""):
    """Localized table.  `rows` is language-neutral (numeric data).

    A row may be a plain string for a full-width group band, matching the
    shared `table()` helper.  Header lists and caption are selected by lang.
    """
    return C.table(T(hdr_vi, hdr_en, lang), rows,
                   caption=T(cap_vi, cap_en, lang))
