# -*- coding: utf-8 -*-
"""Vector figures for Book 5 — Heikkilä, *Inherent Safety in Process Plant
Design* (VTT Publications 384, 1999).

Every function returns the standard 5-tuple
``(svg, caption_vi, caption_en, aria_vi, aria_en)``.  Figures whose number
matches the source (e.g. Figure 1, Figure 7) are redraws of the originals;
editorial schematics that do not exist in the source are labelled as such in
both captions.
"""
import math
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from vfig import (BLUE, GOLD, GREY, GREEN, INK, PAPER, RED,  # noqa: E402
                  _arrow, _axes, _box, _circle, _defs, _f as fmt, _fig, _line,
                  _path, _poly, _rect, _txt, svg)


def esc(s):
    """XML-escape SVG text, preserving entities already present in the data."""
    s = str(s)
    s = re.sub(r"&(?!amp;|lt;|gt;|quot;|apos;|#\d+;)", "&amp;", s)
    return s.replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")


def fig_isd_intro():
    """Editorial schematic: the Inherent Safety Index hierarchy (Abstract, p. 3)."""
    w, h = 560, 330
    o = [_defs()]
    # total index
    o.append(_box(170, 14, 220, 38,
                  "Inherent Safety Index  ISI\nChỉ số An toàn Nội tại",
                  fill="#fdf3e6", sw=1.6, size=9.5, color=INK))
    # two branches
    o.append(_box(24, 86, 244, 36, "Chemical Inherent Safety Index  ICI\nChỉ số hóa học",
                  fill="#eef3fb", sw=1.3, size=8.8))
    o.append(_box(292, 86, 244, 36, "Process Inherent Safety Index  IPI\nChỉ số quá trình",
                  fill="#eef3fb", sw=1.3, size=8.8))
    o.append(_arrow(250, 52, 146, 86, sw=1.2, color=INK, head="a6"))
    o.append(_arrow(310, 52, 414, 86, sw=1.2, color=INK, head="a6"))

    chem = ["IRM  main reaction heat", "IRS  side reaction heat",
            "IINT  chemical interaction", "IFL  flammability",
            "IEX  explosiveness", "ITOX  toxic exposure",
            "ICOR  corrosiveness"]
    proc = ["II  inventory", "IT  process temperature",
            "Ip  process pressure", "IEQ  equipment safety",
            "IST  safe process structure"]
    for i, lab in enumerate(chem):
        col, row = i % 2, i // 2
        o.append(_box(24 + col * 126, 140 + row * 34, 118, 26, lab,
                      fill="#f4f7fb", sw=1.0, size=7.2))
    for i, lab in enumerate(proc):
        col, row = i % 2, i // 2
        o.append(_box(292 + col * 126, 140 + row * 34, 118, 26, lab,
                      fill="#eaf6ee", sw=1.0, size=7.2))
    o.append(_txt(280, 306,
                  "Sơ đồ biên tập theo Tóm tắt (tr. 3) · không có hình tương ứng trong nguyên bản",
                  7.4, color=GREY))
    s = svg(w, h, "".join(o),
            esc("Editorial schematic of the Inherent Safety Index hierarchy"))
    return _fig(s,
                "Sơ đồ A · Cấu trúc Chỉ số An toàn Nội tại: nhánh hóa học (7 chỉ số thành phần) "
                "và nhánh quá trình (5 chỉ số thành phần). Sơ đồ biên tập theo Tóm tắt, không "
                "có trong nguyên bản.",
                "Figure A · The Inherent Safety Index hierarchy: a chemical branch (seven "
                "subindices) and a process branch (five subindices). Editorial schematic after "
                "the Abstract; not present in the original.",
                "Sơ đồ phân nhánh Chỉ số An toàn Nội tại thành hai nhánh hóa học và quá trình",
                "Hierarchy diagram splitting the Inherent Safety Index into chemical and process subindices")


FIGS = {
    "isd_intro": fig_isd_intro,
}
