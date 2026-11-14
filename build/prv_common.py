# -*- coding: utf-8 -*-
"""Page shell for Book 4 — Crosby *Pressure Relief Valve Engineering Handbook*
(Technical Document TP-V300, 1997).

Reuses the proven `bolton_common.py` markup helpers, breadcrumb, chapter
navigation and bilingual page shell, exactly like `isa51_common.py` and
`int_common.py`. This module only registers a fourth book in the shared
``BOOK`` / ``SLUGS`` tables and adds the ``T(vi, en, lang)`` selector, so all
readers stay on one implementation.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import bolton_common as _B  # noqa: E402
from reader_book import BOOKS  # noqa: E402

ROOT = _B.ROOT

BOOK = _B.BOOK
SLUGS = _B.SLUGS

BOOK["prv"] = {
    "spec": BOOKS["prv"],
    "base": "/books/read/pressure-relief-valve-engineering-handbook/",
    "base_vi": "/vi/books/read/pressure-relief-valve-engineering-handbook/",
}

# Populated incrementally as chapters are built — `nav()` only links to chapters
# that exist, so an in-progress book never ships a broken "next" link.
SLUGS["prv"] = {
    1: "ch01-introduction",
    2: "ch02-fundamentals",
    3: "ch03-terminology",
    4: "ch04-codes-standards",
    5: "ch05-sizing-uscs",
}

# Re-export the shared helpers so chapter modules can `import prv_common as C`.
(p, lead, h2, h3, h4, eq, quote, ul, ol, note, refs, table, fig, keyterms,
 nav, page, write, build) = (
    _B.p, _B.lead, _B.h2, _B.h3, _B.h4, _B.eq, _B.quote, _B.ul, _B.ol,
    _B.note, _B.refs, _B.table, _B.fig, _B.keyterms, _B.nav, _B.page,
    _B.write, _B.build,
)


def T(vi, en, lang):
    """Pick the Vietnamese or English rendering of one content fragment."""
    return vi if lang == "vi" else en
