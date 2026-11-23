# -*- coding: utf-8 -*-
"""Page shell for Book 7c — Emerson, Control Valve Handbook, 6th ed. (2020).
Guide*, 5th ed. (ISA / Wiley, 2011).

Reuses the proven `bolton_common.py` markup helpers, breadcrumb, chapter
navigation and bilingual page shell. The 204-page book splits into 32 site
units, one per source chapter — the chapters are short (2–6 pages each) and
each poses a practical question, so this maps naturally.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import bolton_common as _B  # noqa: E402
from reader_book import BOOKS  # noqa: E402

ROOT = _B.ROOT
BOOK = _B.BOOK
SLUGS = _B.SLUGS

BOOK["cvh6"] = {
    "spec": BOOKS["cvh6"],
    "base": "/books/read/control-valve-handbook-emerson-6th/",
    "base_vi": "/vi/books/read/control-valve-handbook-emerson-6th/",
}

# Populated incrementally as chapters are built — nav() only links to units
# that exist, so an in-progress book never ships a broken "next" link.
SLUGS["cvh6"] = {
    1: "ch01-introduction-to-control-valves",
    2: "ch02-control-valve-performance",
    3: "ch03-valve-and-actuator-types",
    4: "ch04-control-valve-accessories",
}

# Re-export the shared helpers so chapter modules can `import cvh6_common as C`.
(p, lead, h2, h3, h4, eq, quote, ul, ol, note, refs, table, fig, keyterms,
 nav, page, write, build) = (
    _B.p, _B.lead, _B.h2, _B.h3, _B.h4, _B.eq, _B.quote, _B.ul, _B.ol,
    _B.note, _B.refs, _B.table, _B.fig, _B.keyterms, _B.nav, _B.page,
    _B.write, _B.build,
)


def T(vi, en, lang):
    """Pick the Vietnamese or English rendering of one content fragment."""
    return vi if lang == "vi" else en
