# -*- coding: utf-8 -*-
"""Page shell for Book 7 — Hans D. Baumann, *Control Valve Primer: A User's
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

BOOK["cvp"] = {
    "spec": BOOKS["cvp"],
    "base": "/books/read/control-valve-primer-baumann/",
    "base_vi": "/vi/books/read/control-valve-primer-baumann/",
}

# Populated incrementally as chapters are built — nav() only links to units
# that exist, so an in-progress book never ships a broken "next" link.
SLUGS["cvp"] = {
    1: "ch01-what-is-a-control-valve-and-how-does",
    2: "ch02-why-not-use-a-speed-controlled-pump",
    3: "ch03-what-valve-type-shall-i-choose",
    4: "ch04-the-self-acting-regulator-why-not",
    5: "ch05-valve-sizing-made-easy",
    6: "ch06-high-recovery-valves",
    7: "ch07-sizing-and-selection-let-the-computer-do-it-all",
    8: "ch08-what-about-fail-safe",
    9: "ch09-why-most-people-choose-equal-percentage",
    10: "ch10-valve-positioners",
    11: "ch11-the-mystery-of-line-pressure-produced-valve-stem-forces",
    12: "ch12-how-to-install-a-control-valve",
    13: "ch13-how-good-is-the-valve-i-purchased",
    14: "ch14-when-do-i-need-to-hard-face-the-valve-trim",
    15: "ch15-cavitation",
    16: "ch16-concern-for-the-environment",
    17: "ch17-will-my-valve-be-too-noisy",
    18: "ch18-the-abc-method-for-gases",
    19: "ch19-the-graphical-abc-method-for-gases",
    20: "ch20-methods-of-aerodynamic-valve-noise-reduction",
    21: "ch21-the-abc-method-for-estimating-hydrodynamic-sound-level",
    22: "ch22-graphical-estimation-of-noise-produced-by-turbulence-and-cavitation-of-liquids",
    23: "ch23-flashing",
    24: "ch24-avoiding-leaky-valve-stem-packing",
    25: "ch25-seat-leakage-and-seat-materials",
    26: "ch26-valves-for-sanitary-or-aseptic-service",
    27: "ch27-sixteen-commandments-what-you-shall-not-do",
    28: "ch28-electric-versus-pneumatic-actuators",
    29: "ch29-saving-energy",
    30: "ch30-the-bus-system-to-the-rescue",
    31: "ch31-thinking-green-and-saving-metal",
}

# Re-export the shared helpers so chapter modules can `import cvp_common as C`.
(p, lead, h2, h3, h4, eq, quote, ul, ol, note, refs, table, fig, keyterms,
 nav, page, write, build) = (
    _B.p, _B.lead, _B.h2, _B.h3, _B.h4, _B.eq, _B.quote, _B.ul, _B.ol,
    _B.note, _B.refs, _B.table, _B.fig, _B.keyterms, _B.nav, _B.page,
    _B.write, _B.build,
)


def T(vi, en, lang):
    """Pick the Vietnamese or English rendering of one content fragment."""
    return vi if lang == "vi" else en
