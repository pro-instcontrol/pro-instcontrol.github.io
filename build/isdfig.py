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


def fig_f01():
    """Figure 1 (p. 15) — Kletz's methods of identifying / assessing hazards.

    The source figure's labels have no Unicode text layer (they are PDF glyph
    names), so the wording below was recovered by decoding those glyph codes
    and cross-checking against a render of p. 15.  Source labels are kept
    verbatim in English; the chapter supplies a Vietnamese gloss in a table.
    """
    w, h = 680, 300
    o = [_defs()]

    # column headings
    o.append(_txt(168, 30, "Methods of identifying hazards", 10.2, weight="600"))
    o.append(_txt(512, 30, "Methods of assessing hazards", 10.2, weight="600"))
    o.append(_rect(16, 42, 304, 1.1, fill="#d8dde3", sw=0))
    o.append(_rect(360, 42, 304, 1.1, fill="#d8dde3", sw=0))

    # eight source labels, top to bottom in each column
    left = ["Obvious", "See what happens", "Check list", "Hazop"]
    right = ["Obvious", "Experience", "Codes of practice",
             "Hazard analysis (Hazan)"]
    rows = [92, 136, 180, 224]

    # central box
    bx, by, bw, bh = 285, 140, 110, 38
    o.append(_rect(bx, by, bw, bh, fill="#fdf3e6", sw=1.6))
    o.append(_txt(bx + bw / 2, by + bh / 2 + 4.2, "HAZARDS", 11.4, weight="600"))

    # fan of lines: from the box outwards, arrowheads at the outer ends
    attach = [147, 154, 164, 171]
    for i, y in enumerate(rows):
        o.append(_arrow(bx, attach[i], 196, y, sw=1.0, color=INK, head="a7"))
        o.append(_arrow(bx + bw, attach[i], 484, y, sw=1.0, color=INK, head="a7"))
        o.append(_txt(16, y + 3.2, left[i], 9.2, anchor="start"))
        o.append(_txt(496, y + 3.2, right[i], 9.2, anchor="start"))

    o.append(_txt(340, 276,
                  "Nhãn giữ nguyên theo nguyên bản · Source labels kept verbatim",
                  7.6, color=GREY))
    s = svg(w, h, "".join(o),
            esc("Methods of identifying and assessing hazards (Kletz, 1992a)"))
    return _fig(s,
                "Hình 1 · Các phương pháp nhận diện mối nguy (trái) và đánh giá mối nguy "
                "(phải) tỏa ra từ mối nguy trung tâm, theo Kletz (1992a). Vẽ lại từ nguyên bản, "
                "tr. 15.",
                "Figure 1 · Methods of identifying hazards (left) and assessing hazards "
                "(right) radiating from the central hazard, after Kletz (1992a). Redrawn "
                "from the original, p. 15.",
                "Sơ đồ hình quạt gồm bốn phương pháp nhận diện và bốn phương pháp đánh giá mối nguy",
                "Fan diagram with four hazard-identification and four hazard-assessment methods")


def fig_f02():
    """Figure 2 (p. 17) — steps of a safety and risk analysis (Suokas & Kakko, 1993)."""
    w, h = 680, 440
    o = [_defs()]
    INK2 = INK

    # central column of stages
    o.append(_box(250, 30, 220, 32, "SYSTEM DEFINITION", size=8.6))
    o.append(_box(250, 95, 220, 32, "HAZARD IDENTIFICATION", size=8.6))
    o.append(_box(250, 160, 220, 32, "ACCIDENT MODELLING", size=8.6))
    o.append(_box(250, 320, 220, 32, "RISK ESTIMATION", size=8.6))
    o.append(_box(250, 385, 220, 32, "DOCUMENTATION OF THE RESULTS", size=8.2))
    # two parallel estimations
    o.append(_box(80, 235, 215, 40, "ESTIMATION OF\nACCIDENT FREQUENCIES",
                  size=8.0))
    o.append(_box(385, 235, 215, 40, "ESTIMATION OF\nACCIDENT CONSEQUENCES",
                  size=8.0))

    # SYSTEM CHANGES: tall side box with rotated lettering (as in the source)
    o.append(_rect(20, 95, 50, 265, fill="#f4f7fb", sw=1.0))
    o.append('<text x="45" y="228" transform="rotate(-90 45 228)" '
             'text-anchor="middle" style="font:9px Inter,Helvetica,sans-serif;'
             'fill:%s;letter-spacing:.5px">SYSTEM CHANGES</text>' % INK2)

    # main downward chain
    o.append(_arrow(360, 62, 360, 95, sw=1.2, head="a7"))
    o.append(_arrow(360, 127, 360, 160, sw=1.2, head="a7"))
    o.append(_arrow(360, 350, 360, 385, sw=1.2, head="a7"))

    # thick branch from accident modelling into the two parallel estimations
    o.append(_line(360, 192, 360, 212, sw=2.0))
    o.append(_line(187, 212, 492, 212, sw=2.0))
    o.append(_line(187, 212, 187, 226, sw=2.0))
    o.append(_line(492, 212, 492, 226, sw=2.0))
    o.append(_arrow(187, 226, 187, 235, sw=1.6, head="a6"))
    o.append(_arrow(492, 226, 492, 235, sw=1.6, head="a6"))

    # both estimations converge on risk estimation
    o.append(_arrow(187, 275, 300, 320, sw=1.2, head="a7"))
    o.append(_arrow(492, 275, 420, 320, sw=1.2, head="a7"))

    # feedback: three stage results feed SYSTEM CHANGES
    for y in (142, 205, 300):
        o.append(_arrow(250, y, 70, y, sw=1.0, head="a7"))
    # and SYSTEM CHANGES loops back to system definition and to documentation
    o.append(_line(45, 95, 45, 46))
    o.append(_arrow(45, 46, 250, 46, sw=1.0, head="a7"))
    o.append(_line(45, 360, 45, 401))
    o.append(_arrow(45, 401, 250, 401, sw=1.0, head="a7"))

    s = svg(w, h, "".join(o), esc("Steps of a safety and risk analysis (Suokas and Kakko, 1993)"))
    return _fig(s,
                "Hình 2 · Các bước của phân tích an toàn và rủi ro theo Suokas và Kakko (1993): "
                "định nghĩa hệ thống → nhận diện mối nguy → mô hình hóa tai nạn → ước lượng tần "
                "suất và hệ quả → ước lượng rủi ro → lập hồ sơ kết quả, với vòng phản hồi "
                "<i>thay đổi hệ thống</i>. Vẽ lại từ nguyên bản, tr. 17.",
                "Figure 2 · Steps of a safety and risk analysis (Suokas and Kakko, 1993): "
                "system definition → hazard identification → accident modelling → parallel "
                "estimation of frequencies and consequences → risk estimation → documentation, "
                "with the system-changes feedback loop. Redrawn from the original, p. 17.",
                "Sơ đồ quy trình tám bước phân tích an toàn và rủi ro cùng vòng phản hồi thay đổi hệ thống",
                "Eight-step safety and risk analysis flowchart with a system-changes feedback loop")


# ---- Figure 3 data (CCPS, 1992, p. 18) -------------------------------------
_PHASES = [
    "Research & Development", "Conceptual Design", "Pilot Plant Operation",
    "Detailed Engineering", "Construction/Start-up", "Routine Operation",
    "Expansion or Modification", "Incident Investigation", "Decommissioning",
]
_TECHNIQUES = [
    "Safety Review", "Checklist", "Relative Ranking", "PHA", "What-If",
    "What-if/Checklist", "HAZOP", "FMEA", "Fault Tree", "Event Tree", "CCA", "HRA",
]
# F = commonly used (filled dot), O = rarely used or inappropriate (hollow).
_MATRIX = [
    "OOFFFOOOOOOO",   # Research & Development
    "OFFFFFOOOOOO",   # Conceptual Design
    "OFOFFFFFFFFF",   # Pilot Plant Operation
    "OFOFFFFFFFFF",   # Detailed Engineering
    "FFOOFFOOOOOF",   # Construction/Start-up
    "FFOOFFFFFFFF",   # Routine Operation
    "FFFFFFFFFFFF",   # Expansion or Modification
    "OOOOFOFFFFFF",   # Incident Investigation
    "FFOOFFOOOOOO",   # Decommissioning
]


def fig_f03():
    """Figure 3 (p. 18) — CCPS matrix of hazard evaluation techniques vs life cycle."""
    w, h = 680, 430
    o = [_defs()]
    x0, dx, y0, dy = 252, 35, 148, 26
    for c, name in enumerate(_TECHNIQUES):
        x = x0 + c * dx
        o.append('<text x="%d" y="126" transform="rotate(-90 %d 126)" '
                 'text-anchor="start" style="font:8px Inter,Helvetica,sans-serif;'
                 'fill:%s">%s</text>' % (x, x, INK, esc(name)))
    for r, phase in enumerate(_PHASES):
        y = y0 + r * dy
        o.append(_txt(238, y + 3, esc(phase), 8.6, anchor="end"))
        for c, mark in enumerate(_MATRIX[r]):
            x = x0 + c * dx
            if mark == "F":
                o.append('<circle cx="%d" cy="%d" r="5.2" fill="%s"/>'
                         % (x, y, INK))
            else:
                o.append('<circle cx="%d" cy="%d" r="5.2" fill="#ffffff" '
                         'stroke="%s" stroke-width="1.1"/>' % (x, y, INK))
    # legend
    ly = 392
    o.append('<circle cx="252" cy="%d" r="5.2" fill="#ffffff" stroke="%s" '
             'stroke-width="1.1"/>' % (ly, INK))
    o.append(_txt(264, ly + 3.2, "Rarely used or inappropriate", 8.6, anchor="start"))
    o.append('<circle cx="462" cy="%d" r="5.2" fill="%s"/>' % (ly, INK))
    o.append(_txt(474, ly + 3.2, "Commonly used", 8.6, anchor="start"))
    o.append(_txt(340, 416,
                  "Chấm đen = thường dùng · chấm rỗng = ít dùng hoặc không phù hợp",
                  7.4, color=GREY))
    s = svg(w, h, "".join(o),
            esc("Typical uses of hazard evaluation techniques (CCPS, 1992)"))
    return _fig(s,
                "Hình 3 · Mức độ sử dụng điển hình của 12 kỹ thuật đánh giá mối nguy qua 9 giai "
                "đoạn vòng đời nhà máy, theo CCPS (1992). Chấm đen = thường dùng; chấm rỗng = "
                "ít dùng hoặc không phù hợp. Vẽ lại từ nguyên bản, tr. 18.",
                "Figure 3 · Typical uses of twelve hazard evaluation techniques across nine "
                "plant life-cycle phases (CCPS, 1992). Filled dot = commonly used; hollow dot = "
                "rarely used or inappropriate. Redrawn from the original, p. 18.",
                "Ma trận 9 giai đoạn vòng đời nhân 12 kỹ thuật đánh giá mối nguy",
                "Nine-by-twelve matrix of life-cycle phases versus hazard evaluation techniques")


FIGS = {
    "isd_intro": fig_isd_intro,
    "f01": fig_f01,
    "f02": fig_f02,
    "f03": fig_f03,
}
