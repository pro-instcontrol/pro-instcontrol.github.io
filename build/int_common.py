# -*- coding: utf-8 -*-
"""Page shell for Book 3 — CSIA *Guide for Selecting & Working with a Control
Systems Integrator*, Volume 1 (2000).

Like `isa51_common.py`, this module reuses the proven `bolton_common.py`
markup helpers, breadcrumb, chapter navigation and bilingual page shell.  It
only registers a third book in the shared ``BOOK`` / ``SLUGS`` tables and adds
the ``T(vi, en, lang)`` selector, so all readers stay on one implementation.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import bolton_common as _B  # noqa: E402
from reader_book import BOOKS  # noqa: E402

ROOT = _B.ROOT

BOOK = _B.BOOK
SLUGS = _B.SLUGS

BOOK["int"] = {
    "spec": BOOKS["int"],
    "base": "/books/read/working-with-an-integrator-guide/",
    "base_vi": "/vi/books/read/working-with-an-integrator-guide/",
}

SLUGS["int"] = {
    1: "ch01-general",
    2: "ch02-decision-analysis-tool",
    3: "ch03-scoring-and-levels",
    4: "ch04-registration-and-general-management",
    5: "ch05-human-and-project-management",
    6: "ch06-quality-financial-business",
    7: "ch07-technical",
    8: "ch08-integrator-types",
    9: "ch09-decision-worksheet",
}

p, lead, h2, h3, h4 = _B.p, _B.lead, _B.h2, _B.h3, _B.h4
eq, quote, ul, ol = _B.eq, _B.quote, _B.ul, _B.ol
note, refs, table, fig, keyterms = (
    _B.note, _B.refs, _B.table, _B.fig, _B.keyterms)
nav, page, write, build = _B.nav, _B.page, _B.write, _B.build


def T(vi, en, lang):
    """Pick the Vietnamese or English rendering of one content fragment."""
    return vi if lang == "vi" else en
