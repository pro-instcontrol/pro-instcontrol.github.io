# -*- coding: utf-8 -*-
"""Page shell for Book 9 — L. N. Jalali (ed.), Handbook on Power Plant
Instrumentation and Control (Bibliotex, 2019).

Reuses the proven `bolton_common.py` markup helpers, breadcrumb, chapter
navigation and bilingual page shell. The 308-page edited volume splits into
11 site units, one per source chapter.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import bolton_common as _B  # noqa: E402
from reader_book import BOOKS  # noqa: E402

ROOT = _B.ROOT
BOOK = _B.BOOK
SLUGS = _B.SLUGS

BOOK["ppic"] = {
    "spec": BOOKS["ppic"],
    "base": "/books/read/handbook-power-plant-instrumentation-control/",
    "base_vi": "/vi/books/read/handbook-power-plant-instrumentation-control/",
}

# Populated incrementally as chapters are built — nav() only links to units
# that exist, so an in-progress book never ships a broken "next" link.
SLUGS["ppic"] = {
    1: "ch01-catalytic-reduction-of-dissolved-oxygen",
    2: "ch02-advanced-measuring-methods-for-nuclear-installations",
    3: "ch03-study-of-control-strategy-of-the-converter",
    4: "ch04-nuclear-power-plant-instrumentation-fault-detection",
    5: "ch05-analysis-of-spatial-separation-effects",
}

# Re-export the shared helpers so chapter modules can `import ppic_common as C`.
(p, lead, h2, h3, h4, eq, quote, ul, ol, note, refs, table, fig, keyterms,
 nav, page, write, build) = (
    _B.p, _B.lead, _B.h2, _B.h3, _B.h4, _B.eq, _B.quote, _B.ul, _B.ol,
    _B.note, _B.refs, _B.table, _B.fig, _B.keyterms, _B.nav, _B.page,
    _B.write, _B.build,
)


def T(vi, en, lang):
    """Pick the Vietnamese or English rendering of one content fragment."""
    return vi if lang == "vi" else en
