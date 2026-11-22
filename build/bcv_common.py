# -*- coding: utf-8 -*-
"""Page shell for Book 7b — Guy Borden Jr. (ed.), *Control Valves*, ISA
Practical Guides for Measurement and Control (1998).

The local source is a 12-page scan of Chapter 5, "Control Valve Actuators"
(printed pp. 93-103).  One site unit.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import bolton_common as _B  # noqa: E402
from reader_book import BOOKS  # noqa: E402

ROOT = _B.ROOT
BOOK = _B.BOOK
SLUGS = _B.SLUGS

BOOK["bcv"] = {
    "spec": BOOKS["bcv"],
    "base": "/books/read/control-valves-borden-practical-guide/",
    "base_vi": "/vi/books/read/control-valves-borden-practical-guide/",
}

SLUGS["bcv"] = {
    5: "ch05-control-valve-actuators",
}

(p, lead, h2, h3, h4, eq, quote, ul, ol, note, refs, table, fig, keyterms,
 nav, page, write, build) = (
    _B.p, _B.lead, _B.h2, _B.h3, _B.h4, _B.eq, _B.quote, _B.ul, _B.ol,
    _B.note, _B.refs, _B.table, _B.fig, _B.keyterms, _B.nav, _B.page,
    _B.write, _B.build,
)


def T(vi, en, lang):
    return vi if lang == "vi" else en
