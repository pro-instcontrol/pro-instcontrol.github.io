# -*- coding: utf-8 -*-
"""Generate the 37 vector symbol sheets of ANSI/ISA-5.1 Section 6.

The standard's drawing sheets (pages 28-64) contain no text layer: every
symbol and every label is a PDF path.  `pdfvec.page_svg` interprets those
path operators and emits a compact standalone SVG, so the reader can carry
a true vector reproduction of every sheet instead of a screenshot.

Run from the repository root::

    python build/make_isa51_sheets.py

Source PDF: D:/Process Control and Automation/Standard Isa -
Instrumentation Symbols And Identification.pdf
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from pdfvec import page_svg  # noqa: E402

ROOT = os.path.dirname(HERE)
OUT = os.path.join(HERE, "isa51_sheets")
PDF = ("D:/Process Control and Automation/"
       "Standard Isa - Instrumentation Symbols And Identification.pdf")

# Pages 21, 22 and 27 carry a genuine text layer, so they are rendered as
# bilingual HTML tables/prose instead of being traced.  Pages 23-26 (the four
# Table 3 function-block sheets) and 28-64 (the 37 clause-6 drawing sheets)
# are drawn entirely as PDF paths and are converted to real vectors.
PAGES = list(range(23, 27)) + list(range(28, 65))
# The four Table 3 sheets are printed sideways in the standard.
ROT_CANDIDATES = set(range(23, 27))


def _portrait(svg):
    m = re.search(r'viewBox="([-\d.]+) ([-\d.]+) ([-\d.]+) ([-\d.]+)"', svg)
    if not m:
        return False
    return float(m.group(4)) > float(m.group(3))


def main():
    if not os.path.isfile(PDF):
        raise SystemExit("source PDF not found: %s" % PDF)
    os.makedirs(OUT, exist_ok=True)
    total = 0
    for p in PAGES:
        kw = dict(eps=0.20, stroke="#22303f")
        svg = page_svg(PDF, p, "ANSI/ISA-5.1 sheet, standard page %d" % p, **kw)
        if p in ROT_CANDIDATES and _portrait(svg):
            svg = page_svg(PDF, p, "ANSI/ISA-5.1 sheet, standard page %d" % p,
                           rotate=90, **kw)
        if not svg:
            raise SystemExit("empty vector output for page %d" % p)
        path = os.path.join(OUT, "p%d.svg" % p)
        open(path, "w", encoding="utf-8").write(svg)
        total += len(svg)
        print("p%-3d %7d bytes  %3d paths  %s" %
              (p, len(svg), svg.count("<path"),
               "rotated" if "rotate(90)" in svg else "upright"))
    print("total %d sheets, %.2f MB" % (len(PAGES), total / 1048576))


if __name__ == "__main__":
    main()
