# -*- coding: utf-8 -*-
"""Page shell for the Alan McMillan *Electrical Installations in Hazardous Areas* reader.

Reuses the proven `bolton_common.py` markup helpers, breadcrumb, chapter
navigation and bilingual page shell. The 678-page reference is translated as
22 site units, one per printed chapter.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import bolton_common as _B  # noqa: E402
from reader_book import BOOKS  # noqa: E402

ROOT = _B.ROOT
BOOK = _B.BOOK
SLUGS = _B.SLUGS

BOOK["mcmillan"] = {
    "spec": BOOKS["mcmillan"],
    "base": "/books/read/electrical-installations-hazardous-areas/",
    "base_vi": "/vi/books/read/electrical-installations-hazardous-areas/",
}

# Only translated chapters are registered; unbuilt chapters stay out of the
# navigation so the site never links to a 404.
SLUGS["mcmillan"] = {
    1: "ch01-introduction",
    2: "ch02-area-classification",
    3: "ch03-area-classification-practice",
    4: "ch04-calculation-of-release-rates-and-extents",
    5: "ch05-not-freely-ventilated-areas",
    6: "ch06-area-classification-practice-for-dusts",
    7: "ch07-design-philosophy-for-electrical-apparatus",
    8: "ch08-general-requirements-for-explosion-protected-apparatus",
    9: "ch09-apparatus-using-protection-concepts-encapsulation-oil-immersion-powder-filling",
    10: "ch10-apparatus-using-protection-concept-flameproof-enclosure-d",
    11: "ch11-apparatus-using-protection-concept-pressurization-p",
    12: "ch12-apparatus-with-protection-concept-increased-safety-e",
    13: "ch13-apparatus-and-systems-using-intrinsic-safety-i",
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
