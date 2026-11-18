# -*- coding: utf-8 -*-
"""Page shell for Book 6 — Smith & Zappe, *Valve Selection Handbook*, 5th ed.
(Gulf Professional Publishing / Elsevier, 2004).

Reuses the proven `bolton_common.py` markup helpers, breadcrumb, chapter
navigation and bilingual page shell, exactly like `isd_common.py`. This module
only registers a sixth book in the shared ``BOOK`` / ``SLUGS`` tables and adds
the ``T(vi, en, lang)`` selector, so all readers stay on one implementation.

The 387-page book splits into 21 site units: the ten source chapters are kept
whole where practical, but the very long chapters (Fundamentals ≈ 40 pp.,
Manual Valves ≈ 106 pp., Pressure Relief Valves ≈ 58 pp., Rupture Discs ≈ 42
pp.) are split into consecutive parts, and the appendices (A–E) form one
reference unit.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import bolton_common as _B  # noqa: E402
from reader_book import BOOKS  # noqa: E402

ROOT = _B.ROOT

BOOK = _B.BOOK
SLUGS = _B.SLUGS

BOOK["vsh"] = {
    "spec": BOOKS["vsh"],
    "base": "/books/read/valve-selection-handbook/",
    "base_vi": "/vi/books/read/valve-selection-handbook/",
}

# Populated incrementally as units are built — `nav()` only links to units that
# exist, so an in-progress book never ships a broken "next" link.  Full plan:
#   2 ch02-fluid-tightness-and-sealing     12 ch12-check-valves
#   3 ch03-seatings-gaskets-stem-seals     13 ch13-prv-direct-loaded
#   4 ch04-flow-through-valves             14 ch14-prv-pilot-operated
#   5 ch05-manual-valves-selection-globe   15 ch15-rupture-discs-construction
#   6 ch06-piston-parallel-gate-valves     16 ch16-rupture-discs-selection
#   7 ch07-wedge-gate-valves               17 ch17-sizing-pressure-relief-devices
#   8 ch08-plug-valves                     18 ch18-actuators
#   9 ch09-ball-valves                     19 ch19-double-block-and-bleed
#  10 ch10-butterfly-pinch-valves          20 ch20-mechanical-locking-devices
#  11 ch11-diaphragm-stainless-steel-valves 21 ch21-appendices
SLUGS["vsh"] = {
    1: "ch01-introduction",
    2: "ch02-fluid-tightness-and-sealing",
    3: "ch03-seatings-gaskets-stem-seals",
    4: "ch04-flow-through-valves",
    5: "ch05-manual-valves-selection-globe",
    6: "ch06-piston-parallel-gate-valves",
    7: "ch07-wedge-gate-valves",
    8: "ch08-plug-valves",
    9: "ch09-ball-valves",
    10: "ch10-butterfly-pinch-valves",
    11: "ch11-diaphragm-stainless-steel-valves",
    12: "ch12-check-valves",
    13: "ch13-prv-direct-loaded",
    14: "ch14-prv-pilot-operated",
    15: "ch15-rupture-discs-construction",
}

# Re-export the shared helpers so chapter modules can `import vsh_common as C`.
(p, lead, h2, h3, h4, eq, quote, ul, ol, note, refs, table, fig, keyterms,
 nav, page, write, build) = (
    _B.p, _B.lead, _B.h2, _B.h3, _B.h4, _B.eq, _B.quote, _B.ul, _B.ol,
    _B.note, _B.refs, _B.table, _B.fig, _B.keyterms, _B.nav, _B.page,
    _B.write, _B.build,
)


def T(vi, en, lang):
    """Pick the Vietnamese or English rendering of one content fragment."""
    return vi if lang == "vi" else en
