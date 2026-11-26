# -*- coding: utf-8 -*-
"""Page shell for Book 10 — Prasad, Jayaswal & Priye, Instrumentation and
Process Control (I.K. International, 2019).

Reuses the proven `bolton_common.py` markup helpers, breadcrumb, chapter
navigation and bilingual page shell. The 403-page textbook splits into 8
site units, one per source chapter.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import bolton_common as _B  # noqa: E402
from reader_book import BOOKS  # noqa: E402

ROOT = _B.ROOT
BOOK = _B.BOOK
SLUGS = _B.SLUGS

BOOK["ipc"] = {
    "spec": BOOKS["ipc"],
    "base": "/books/read/instrumentation-and-process-control/",
    "base_vi": "/vi/books/read/instrumentation-and-process-control/",
}

# Populated incrementally as chapters are built — nav() only links to units
# that exist, so an in-progress book never ships a broken "next" link.
SLUGS["ipc"] = {
    1: "ch01-transducers-i",
    2: "ch02-transducers-ii",
    3: "ch03-transducers-iii",
    4: "ch04-telemetry",
    5: "ch05-signal-conditioning-and-data-acquisition-system",
    6: "ch06-process-control",
    7: "ch07-display-devices-and-recorders",
    8: "ch08-microprocessor-based-instrumentation-system",
}

# Re-export the shared helpers so chapter modules can `import ipc_common as C`.
(p, lead, h2, h3, h4, eq, quote, ul, ol, note, refs, table, fig, keyterms,
 nav, page, write, build) = (
    _B.p, _B.lead, _B.h2, _B.h3, _B.h4, _B.eq, _B.quote, _B.ul, _B.ol,
    _B.note, _B.refs, _B.table, _B.fig, _B.keyterms, _B.nav, _B.page,
    _B.write, _B.build,
)


def T(vi, en, lang):
    """Pick the Vietnamese or English rendering of one content fragment."""
    return vi if lang == "vi" else en
