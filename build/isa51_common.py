# -*- coding: utf-8 -*-
"""Page shell for the ANSI/ISA-5.1 *Instrumentation Symbols* reader.

The markup helpers, breadcrumb, chapter navigation and bilingual page shell
are exactly the ones proven by the Bolton / PC / SIS readers.  This module
only registers a second book in the shared ``BOOK`` and ``SLUGS`` tables and
re-exports the helpers, so both books stay on one implementation.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import bolton_common as _B  # noqa: E402
from reader_book import BOOKS  # noqa: E402

ROOT = _B.ROOT

BOOK = _B.BOOK
SLUGS = _B.SLUGS

BOOK["isa51"] = {
    "spec": BOOKS["isa51"],
    "base": "/books/read/isa-5-1-instrumentation-symbols/",
    "base_vi": "/vi/books/read/isa-5-1-instrumentation-symbols/",
}

SLUGS["isa51"] = {
    1: "ch01-purpose-and-scope",
    2: "ch02-definitions",
    3: "ch03-identification-system",
    4: "ch04-identification-letters",
    5: "ch05-letter-combinations-function-blocks",
    6: "ch06-instrument-symbols",
    7: "ch07-worked-examples",
}

p, lead, h2, h3, h4 = _B.p, _B.lead, _B.h2, _B.h3, _B.h4
eq, quote, ul, ol = _B.eq, _B.quote, _B.ul, _B.ol
note, refs, table, fig, keyterms = (
    _B.note, _B.refs, _B.table, _B.fig, _B.keyterms)
nav, page, write, build = _B.nav, _B.page, _B.write, _B.build


def T(vi, en, lang):
    """Pick the Vietnamese or English rendering of one content fragment."""
    return vi if lang == "vi" else en
