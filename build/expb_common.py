# -*- coding: utf-8 -*-
"""Page shell for the R. STAHL *ExProtection Global-America-Basics* reader.

Reuses the proven `bolton_common.py` markup helpers, breadcrumb, chapter
navigation and bilingual page shell. The 14-page primer splits into six
site units, one per logical section.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import bolton_common as _B  # noqa: E402
from reader_book import BOOKS  # noqa: E402

ROOT = _B.ROOT
BOOK = _B.BOOK
SLUGS = _B.SLUGS

BOOK["expb"] = {
    "spec": BOOKS["expb"],
    "base": "/books/read/exprotection-global-america-basics/",
    "base_vi": "/vi/books/read/exprotection-global-america-basics/",
}

SLUGS["expb"] = {
    1: "ch01-hazardous-locations-and-the-two-systems",
    2: "ch02-classes-groups-and-temperature-classes",
    3: "ch03-protection-methods-and-enclosure-types",
    4: "ch04-environmental-protection-and-ingress-protection",
    5: "ch05-north-american-equipment-certification",
    6: "ch06-atex-ce-marking-and-the-iec-ex-scheme",
}

(p, lead, h2, h3, h4, eq, quote, ul, ol, note, refs, table, fig, keyterms,
 nav, page, write, build) = (
    _B.p, _B.lead, _B.h2, _B.h3, _B.h4, _B.eq, _B.quote, _B.ul, _B.ol,
    _B.note, _B.refs, _B.table, _B.fig, _B.keyterms, _B.nav, _B.page,
    _B.write, _B.build,
)


def T(vi, en, lang):
    """Pick the Vietnamese or English rendering of one content fragment."""
    return vi if lang == "vi" else en
