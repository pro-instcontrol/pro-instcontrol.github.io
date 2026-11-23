# -*- coding: utf-8 -*-
"""Page shell for Book 8 — 3G E-learning, Illustrated Handbook of
Industrial Instrumentation & Control (2018).

Reuses the proven `bolton_common.py` markup helpers, breadcrumb, chapter
navigation and bilingual page shell. The 348-page book splits into 8 site
units, one per source chapter.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import bolton_common as _B  # noqa: E402
from reader_book import BOOKS  # noqa: E402

ROOT = _B.ROOT
BOOK = _B.BOOK
SLUGS = _B.SLUGS

BOOK["iih"] = {
    "spec": BOOKS["iih"],
    "base": "/books/read/illustrated-handbook-industrial-instrumentation-control/",
    "base_vi": "/vi/books/read/illustrated-handbook-industrial-instrumentation-control/",
}

# Populated incrementally as chapters are built — nav() only links to units
# that exist, so an in-progress book never ships a broken "next" link.
SLUGS["iih"] = {
    1: "ch01-measurement-of-temperature",
    2: "ch02-measurement-of-pressure",
    3: "ch03-measurement-of-level",
    4: "ch04-ph-measurement",
    5: "ch05-measurement-of-flow-rate",
    6: "ch06-mechanical-flow-meters",
    7: "ch07-gas-and-liquid-sampling-techniques",
}

# Re-export the shared helpers so chapter modules can `import iih_common as C`.
(p, lead, h2, h3, h4, eq, quote, ul, ol, note, refs, table, fig, keyterms,
 nav, page, write, build) = (
    _B.p, _B.lead, _B.h2, _B.h3, _B.h4, _B.eq, _B.quote, _B.ul, _B.ol,
    _B.note, _B.refs, _B.table, _B.fig, _B.keyterms, _B.nav, _B.page,
    _B.write, _B.build,
)


def T(vi, en, lang):
    """Pick the Vietnamese or English rendering of one content fragment."""
    return vi if lang == "vi" else en
