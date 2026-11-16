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
                  _arrow, _axes, _box, _circle, _curve, _defs, _f as fmt,
                  _fig, _line, _path, _poly, _rect, _txt, svg)


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


def fig_c04_stages():
    """Editorial schematic (Ch. 4): where the methods fit in the design stages.

    Chapter 4 has no figures of its own; this map is derived from the prose on
    pp. 19–20 and 22 (Dow/Mond best in later stages, conventional Hazop needs
    final P&IDs, PIIS and the five preliminary methods usable early).
    """
    w, h = 680, 282
    o = [_defs()]
    o.append(_rect(24, 38, 306, 196, fill="#eef3fb", sw=1.0))
    o.append(_rect(350, 38, 306, 196, fill="#fdf3e6", sw=1.0))
    o.append(_txt(177, 58, "Conceptual / preliminary design", 9.4, weight="600"))
    o.append(_txt(177, 72, "Thiết kế sơ bộ · thông tin còn ít", 7.8, color=GREY))
    o.append(_txt(503, 58, "Detailed engineering / later stages", 9.4, weight="600"))
    o.append(_txt(503, 72, esc("Thiết kế chi tiết · đã có P&ID"), 7.8, color=GREY))
    o.append(_line(340, 38, 340, 234, sw=1.0, dash="4 4", color=GREY))

    # early-stage chips
    for i, lab in enumerate(("CSR", "CE", "CHA", "PCA", "PHA")):
        o.append(_box(40 + i * 55, 88, 50, 26, lab, fill="#f8fbff", sw=0.8, size=7.8))
    o.append(_box(40, 132, 130, 40, "PIIS\nchọn lộ trình quá trình",
                  fill="#eaf6ee", sw=1.2, size=8.0))
    o.append(_rect(182, 132, 132, 40, fill="#ffffff", sw=1.0, dash="3 2"))
    o.append(_txt(248, 148, "Flowsheet Hazop", 8.2))
    o.append(_txt(248, 162, "ít được dùng / rarely used", 7.2, color=GREY))
    o.append(_txt(177, 202, "Năm phương pháp sơ bộ · Wells et al. (1993)",
                  7.6, color=GREY))
    o.append(_txt(177, 218, "PIIS dùng được khi thiếu chi tiết quá trình",
                  7.6, color=GREY))

    # later-stage chips
    o.append(_box(366, 96, 130, 36, esc("Dow F&E Index\ncháy và nổ"),
                  fill="#fff8ec", sw=1.0, size=8.2))
    o.append(_box(510, 96, 130, 36, "Mond Index\ncả độc tính",
                  fill="#fff8ec", sw=1.0, size=8.2))
    o.append(_box(366, 150, 274, 36,
                  esc("Conventional Hazop\ncần sơ đồ P&ID hoàn chỉnh"),
                  fill="#fff8ec", sw=1.0, size=8.2))
    o.append(_txt(503, 205, "Phù hợp nhất khi đã biết thiết bị, hóa chất, điều kiện",
                  7.6, color=GREY))
    o.append(_txt(503, 221, "best when equipment, substances and conditions are known",
                  7.2, color=GREY))
    o.append(_txt(340, 258,
                  "Sơ đồ biên tập theo văn bản chương 4 · không có hình tương ứng trong nguyên bản",
                  7.4, color=GREY))
    s = svg(w, h, "".join(o),
            esc("Editorial map: safety analysis methods versus design stage"))
    return _fig(s,
                "Sơ đồ B · Vị trí điển hình của các phương pháp phân tích an toàn theo giai "
                "đoạn thiết kế: năm phương pháp sơ bộ và PIIS ở thiết kế sơ bộ, còn Dow, Mond "
                "và Hazop thông thường ở giai đoạn chi tiết. Sơ đồ biên tập theo văn bản "
                "chương 4 (tr. 19–22), không có trong nguyên bản.",
                "Figure B · Where the safety analysis methods typically fit: the five "
                "preliminary methods and PIIS in conceptual design, Dow, Mond and conventional "
                "Hazop in detailed engineering. Editorial schematic after the prose of "
                "Chapter 4 (pp. 19–22); not present in the original.",
                "Sơ đồ so sánh nhóm phương pháp dùng sớm và nhóm phương pháp dùng muộn trong thiết kế",
                "Comparison diagram of early-stage versus late-stage safety analysis methods")


def fig_c04_indices():
    """Editorial schematic (Ch. 4): structures of the Dow F&EI and the PIIS."""
    w, h = 680, 300
    o = [_defs()]
    o.append(_txt(170, 28, esc("Dow Fire & Explosion Index (§4.1)"), 9.6, weight="600"))
    o.append(_txt(510, 28, "Prototype Index of Inherent Safety (§4.4)", 9.6, weight="600"))
    o.append(_line(340, 38, 340, 268, sw=1.0, dash="4 4", color=GREY))

    # Dow panel: MF and UHF converge on the index
    o.append(_box(30, 66, 130, 40, "Material factor  MF\nflammability · reactivity",
                  fill="#f4f7fb", sw=1.0, size=7.6))
    o.append(_box(186, 46, 120, 30, "General process hazards  GPH",
                  fill="#f4f7fb", sw=1.0, size=7.0))
    o.append(_box(186, 86, 120, 30, "Special process hazards  SPH",
                  fill="#f4f7fb", sw=1.0, size=7.0))
    o.append(_arrow(246, 116, 246, 130, sw=1.0, head="a7"))
    o.append(_box(186, 130, 120, 34, "UHF = GPH × SPH",
                  fill="#eaf6ee", sw=1.0, size=7.8))
    o.append(_arrow(95, 106, 130, 202, sw=1.0, head="a7"))
    o.append(_arrow(246, 164, 215, 202, sw=1.0, head="a7"))
    o.append(_box(60, 202, 240, 42, esc("F&EI = MF × UHF  =  MF × GPH × SPH"),
                  fill="#fdf3e6", sw=1.4, size=9.0))
    o.append(_txt(170, 264, "Hệ số đơn vị × hệ số vật liệu · Dow (1987)",
                  7.6, color=GREY))

    # PIIS panel: two scores side by side converge on the total
    o.append(_box(352, 62, 142, 76,
                  "Chemical score\ninventory · flammability\nexplosiveness · toxicity",
                  fill="#f4f7fb", sw=1.0, size=7.4))
    o.append(_box(506, 62, 142, 76,
                  "Process score\ntemperature · pressure\nyield",
                  fill="#f4f7fb", sw=1.0, size=7.4))
    o.append(_arrow(423, 138, 452, 202, sw=1.0, head="a7"))
    o.append(_arrow(577, 138, 548, 202, sw=1.0, head="a7"))
    o.append(_box(376, 202, 248, 42, "Total score = chemical + process",
                  fill="#fdf3e6", sw=1.4, size=8.6))
    o.append(_txt(500, 264, esc("Tổng điểm = điểm hóa học + điểm quá trình · "
                                "Edwards & Lawrence (1993)"), 7.4, color=GREY))
    o.append(_txt(340, 286,
                  "Sơ đồ biên tập theo §4.1 và §4.4 · không có hình tương ứng trong nguyên bản",
                  7.4, color=GREY))
    s = svg(w, h, "".join(o), esc("Editorial schematic of the Dow F&EI and PIIS index structures"))
    return _fig(s,
                "Sơ đồ C · Cấu trúc của hai chỉ số: Dow F&amp;EI = MF × (GPH × SPH) và PIIS = "
                "điểm hóa học + điểm quá trình. Sơ đồ biên tập theo §4.1 và §4.4, không có "
                "trong nguyên bản.",
                "Figure C · Structure of the two indices: Dow F&amp;EI = MF × (GPH × SPH) and "
                "PIIS = chemical score + process score. Editorial schematic after §4.1 "
                "and §4.4; not present in the original.",
                "Sơ đồ cấu trúc công thức của chỉ số Dow và chỉ số PIIS",
                "Structure diagram of the Dow fire and explosion index and the PIIS total score")


def fig_c05_curves():
    """Editorial schematic (Ch. 5): information grows, cheap safety leverage shrinks.

    Drawn from the prose on pp. 25–26 — in predesign, information is scarce but
    changes for safety are most profitable because nothing has been built or
    ordered yet; index methods (ISI / PIIS) have low information requirements.
    """
    w, h = 680, 320
    o = [_defs()]
    x0, y0, W, H = 72, 44, 556, 196
    # the predesign window
    o.append(_rect(x0 + 0.11 * W, y0, 0.20 * W, H, fill="#eaf6ee", sw=0))
    o.append(_txt(x0 + 0.21 * W, y0 + 16,
                  esc("Cửa sổ ISI / PIIS · predesign window"), 7.6, color=GREEN))

    info = lambda t: 0.05 + 0.90 / (1.0 + math.exp(-9.0 * (t - 0.52)))
    lever = lambda t: 0.95 - 0.88 * (t ** 0.85)
    o.append(_curve(info, x0, y0, W, H, sw=2.2, color=BLUE))
    o.append(_curve(lever, x0, y0, W, H, sw=2.2, color=RED))
    o.append(_axes(x0, y0, W, H,
                   esc("Tiến độ thiết kế / design progress →"),
                   esc("Mức tương đối / relative level"),
                   xt=[(0.0, esc("R&D")), (0.21, "Predesign"), (0.46, "Basic eng."),
                       (0.72, "Detailed eng."), (1.0, "Operation")],
                   yt=[(0.0, "0"), (1.0, "1")]))
    o.append(_txt(x0 + 0.64 * W, y0 + 44, "Thông tin có sẵn / information available",
                  8.0, color=BLUE))
    o.append(_txt(x0 + 0.07 * W, y0 + 42, "Thay đổi an toàn còn rẻ / cheap safety changes",
                  8.0, anchor="start", color=RED))
    o.append(_txt(x0 + 0.21 * W, y0 + 176,
                  "Ít dữ liệu nhưng ảnh hưởng lớn nhất", 7.6, color=GREEN))
    o.append(_line(x0 + 0.60 * W, 270, x0 + 0.60 * W + 26, 270, sw=2.2, color=BLUE))
    o.append(_txt(x0 + 0.60 * W + 32, 273, "information", 7.8, anchor="start"))
    o.append(_line(x0 + 0.78 * W, 270, x0 + 0.78 * W + 26, 270, sw=2.2, color=RED))
    o.append(_txt(x0 + 0.78 * W + 32, 273, "leverage", 7.8, anchor="start"))
    o.append(_txt(340, 302,
                  "Sơ đồ biên tập theo văn bản tr. 25–26 · không có hình tương ứng trong nguyên bản",
                  7.4, color=GREY))
    s = svg(w, h, "".join(o),
            esc("Editorial curves: process information rises while cheap safety leverage falls"))
    return _fig(s,
                "Sơ đồ D · Thông tin về quá trình tăng dần theo tiến độ thiết kế, trong khi "
                "khả năng thay đổi thiết kế vì an toàn với chi phí thấp giảm dần. Vùng thiết "
                "kế sơ bộ là nơi ít dữ liệu nhưng có ảnh hưởng lớn nhất — chính là cửa sổ của "
                "các chỉ số ISI / PIIS. Sơ đồ biên tập theo tr. 25–26, không có trong nguyên bản.",
                "Figure D · Process information grows with design progress while the ability "
                "to make cheap safety changes shrinks. The predesign window has the least data "
                "but the greatest leverage — the niche of the ISI / PIIS index methods. "
                "Editorial schematic after pp. 25–26; not present in the original.",
                "Hai đường cong biểu diễn thông tin tăng và khả năng thay đổi giảm theo tiến độ thiết kế",
                "Two curves showing rising process information and falling safety-change leverage")


def fig_c05_gap():
    """Editorial schematic (Ch. 5): the information gap between Tables 2 and 3."""
    w, h = 680, 296
    o = [_defs()]
    o.append(_rect(22, 38, 306, 184, fill="#eaf6ee", sw=1.0))
    o.append(_rect(352, 38, 306, 184, fill="#fdf3e6", sw=1.0))
    o.append(_txt(175, 58, esc("Thiết kế sơ bộ: thông tin CÓ"), 9.2, weight="600"))
    o.append(_txt(175, 72, "Predesign · information AVAILABLE (p. 25, Table 2)",
                  7.4, color=GREY))
    o.append(_txt(505, 58, esc("Dow / Mond / Hazop: thông tin CẦN"), 9.2, weight="600"))
    o.append(_txt(505, 72, "Detailed methods · information REQUIRED (Table 3)",
                  7.4, color=GREY))
    left = ["Nguyên liệu / raw materials", "Sản phẩm / products",
            "Phụ phẩm / by-products", "Công suất sơ bộ / rough capacity",
            "Các pha chính / main process phases", "Khoảng T, p / rough T and p range"]
    right = ["Mặt bằng / plot plan", "Sơ đồ dòng / flow sheet",
             esc("P&ID / sơ đồ đường ống"), "Loại thiết bị / equipment types",
             "Điều kiện vận hành / operating data", "Đội phân tích / expert team"]
    for i, lab in enumerate(left):
        o.append(_box(36, 86 + i * 22, 278, 19, esc(lab),
                      fill="#ffffff", sw=0.6, size=7.2))
    for i, lab in enumerate(right):
        o.append(_box(366, 86 + i * 22, 278, 19, lab,
                      fill="#ffffff", sw=0.6, size=7.2))
    o.append(_line(340, 40, 340, 220, sw=1.0, dash="4 4", color=GREY))
    o.append(_txt(340, 234, esc("Khoảng trống / the gap"), 8.2, color=GREY))
    o.append(_box(190, 246, 300, 32, esc("ISI / PIIS: 7 thông số, không cần sơ đồ"),
                  fill="#e6f1fb", sw=1.2, size=8.4))
    o.append(_txt(340, 290,
                  "Sơ đồ biên tập so sánh Bảng 2 và Bảng 3 · không có hình tương ứng trong nguyên bản",
                  7.4, color=GREY))
    s = svg(w, h, "".join(o),
            esc("Editorial schematic of the information gap between Tables 2 and 3"))
    return _fig(s,
                "Sơ đồ E · So sánh thông tin có được ở thiết kế sơ bộ (Bảng 2, tr. 27–28) với "
                "thông tin mà Dow, Mond và Hazop đòi hỏi (Bảng 3, tr. 29–30): khoảng trống "
                "được lấp bằng các chỉ số ISI / PIIS chỉ cần bảy thông số. Sơ đồ biên tập, "
                "không có trong nguyên bản.",
                "Figure E · Information available in predesign (Table 2, pp. 27–28) versus "
                "the information demanded by Dow, Mond and Hazop (Table 3, pp. 29–30): the "
                "gap is filled by the ISI / PIIS indices, which need only seven parameters. "
                "Editorial schematic; not present in the original.",
                "Hai cột so sánh thông tin sẵn có và thông tin cần thiết của các phương pháp",
                "Two-column comparison of available predesign data versus detailed-method requirements")


def fig_c06_kletz():
    """Redraw of source Figure 4 (p. 36, Kletz 1991): inherently safer features
    become harder to install as a project progresses."""
    w, h = 640, 300
    o = [_defs()]
    x0, y0, W, H = 70, 40, 530, 180        # plot box: x 70..600, y 40..220
    stages = ["Conceptual\nThiết kế khái niệm", "Flowsheet\nSơ đồ dòng",
              "P&ID", "Detailed design\nThiết kế chi tiết",
              "Construction\nThi công", "Start up\nKhởi động",
              "Operation\nVận hành"]
    n = len(stages)
    # the original shows a broad wedge: wide (high opportunity) at the left,
    # narrowing to almost nothing at the right
    top = [(x0 + W * (i + 0.5) / n, y0 + H * 0.06 + 78 * math.exp(-0.55 * i))
           for i in range(n)]
    bot = [(x0 + W * (i + 0.5) / n, y0 + H - 8 - 62 * math.exp(-0.72 * i))
           for i in range(n)]
    o.append(_poly(top + bot[::-1], fill="#e8eff8", sw=0, close=True))
    # opportunity curve down the middle of the wedge
    mid = [(x0 + W * (i + 0.5) / n, (top[i][1] + bot[i][1]) / 2.0)
           for i in range(n)]
    o.append(_poly(mid, fill="none", sw=2.0, color=BLUE))
    for pnt in mid:
        o.append(_circle(pnt[0], pnt[1], 3, fill=BLUE, sw=0, color=BLUE))
    # baseline
    o.append(_line(x0, y0 + H, x0 + W + 10, y0 + H, sw=1.0, color=INK))
    # stage labels, alternating rows to avoid collisions
    for i, s in enumerate(stages):
        px = x0 + W * (i + 0.5) / n
        lines = s.split("\n")
        line1 = lines[0]
        line2 = lines[1] if len(lines) > 1 else ""
        yy = y0 + H + 16 if i % 2 == 0 else y0 + H + 40
        o.append(_txt(px, yy, esc(line1), 8.0, color=INK))
        if line2:
            o.append(_txt(px, yy + 12, line2, 7.0, color=GREY))
    o.append(_txt(x0 + W / 2.0, y0 - 12,
                  "Cơ hội áp dụng đặc tính an toàn nội tại · Opportunities for installing "
                  "inherently safer features", 8.2, color=GREY))
    # right-side annotation: cheaper early / expensive late
    o.append(_txt(x0 + 58, y0 + 28, "Dễ · rẻ", 8.4, color=GREEN, weight="600"))
    o.append(_txt(x0 + 58, y0 + 40, "easy, cheap", 7.0, color=GREY))
    o.append(_txt(x0 + W - 4, y0 + H - 16, "Khó · đắt", 8.4, anchor="end",
                  color=RED, weight="600"))
    o.append(_txt(x0 + W - 4, y0 + H - 5, "hard, costly", 7.0, anchor="end", color=GREY))
    o.append(_txt(x0 + W / 2.0, h - 8,
                  "Vẽ lại theo Hình 4 (tr. 36) — Kletz (1991)", 7.4, color=GREY))
    s = svg(w, h, "".join(o),
            esc("Inherently safer features become harder to install as a project progresses"))
    return _fig(s,
                "Hình 4 · Cơ hội áp dụng các đặc tính an toàn nội tại giảm dần theo tiến độ "
                "dự án: dễ và rẻ ở thiết kế khái niệm, gần như không còn ở vận hành. "
                "Vẽ lại theo Hình 4 của Kletz (1991), tr. 36.",
                "Figure 4 · Opportunities for installing inherently safer features decline as "
                "the project progresses: easy and cheap at the conceptual stage, almost "
                "exhausted by the operating stage. Redrawn after Figure 4 in Kletz (1991), p. 36.",
                "Đồ thị cơ hội áp dụng an toàn nội tại giảm dần qua bảy giai đoạn dự án",
                "Declining opportunity for installing inherently safer features across seven project stages")


def fig_c06_principles():
    """Editorial schematic: Kletz's principles of inherent safety grouped into
    three tiers — avoid, moderate, simplify/control. Not present in the source."""
    w, h = 640, 330
    o = [_defs()]
    # tier 1 — eliminate the hazard
    o.append(_box(60, 30, 250, 64,
                  "Loại bỏ mối nguy · Eliminate\nIntensification — thứ bạn không có, "
                  "sẽ không rò rỉ\nSubstitution — thay vật liệu/nguyên liệu",
                  fill="#eaf6ee", sw=1.3, size=8.2))
    # tier 2 — moderate
    o.append(_box(60, 110, 250, 52,
                  "Làm dịu · Moderate\nAttenuation — điều kiện/reactant dịu hơn\n"
                  "Limitation of effects — giới hạn hệ quả",
                  fill="#eef3fb", sw=1.2, size=8.2))
    # tier 3 — simplify and control
    o.append(_box(60, 178, 250, 64,
                  "Đơn giản hóa · Simplify\nSimplification — ít lỗi hơn, thiết bị ít hơn\n"
                  "Ease of control — điều khiển bằng nguyên lý vật lý\n"
                  "Tolerance — chịu được vận hành sai",
                  fill="#fdf3e6", sw=1.2, size=8.2))
    # right column — practices
    o.append(_box(360, 30, 230, 118,
                  "Nguyên tắc hỗ trợ · Supporting\nChange Early — nhận diện mối nguy sớm\n"
                  "Avoiding knock-on effects — vách chống cháy\n"
                  "Making status clear — dễ nhận biết trạng thái\n"
                  "Incorrect assembly impossible\nAdministrative controls",
                  fill="#f6f2ec", sw=1.2, size=8.2))
    o.append(_rect(360, 168, 230, 74, fill="#ffffff", sw=1.0, dash="3 2"))
    o.append(_txt(475, 186, "Chọn thời điểm · Timing", 8.2, weight="600"))
    o.append(_txt(475, 202, "Áp dụng tốt nhất ở thiết kế khái niệm —", 8.0))
    o.append(_txt(475, 216, "khi còn chọn lộ trình quá trình", 8.0))
    o.append(_txt(475, 230, "(xem Figure 4: cơ hội giảm dần)", 7.4, color=GREY))
    # arrows between tiers
    o.append(_arrow(185, 94, 185, 108, sw=1.2, color=GREY, head="a6"))
    o.append(_arrow(185, 162, 185, 176, sw=1.2, color=GREY, head="a6"))
    o.append(_line(318, 76, 360, 76, sw=1.0, dash="3 2", color=GREY))
    o.append(_txt(320, 276,
                  "Sơ đồ biên tập theo 12 nguyên tắc của Kletz (1984, 1991) trình bày trong "
                  "mục 6.1 — không có trong nguyên bản",
                  7.4, color=GREY))
    s = svg(w, h, "".join(o),
            esc("Editorial schematic: Kletz's principles of inherent safety grouped in tiers"))
    return _fig(s,
                "Sơ đồ A · Ba tầng nguyên tắc an toàn nội tại theo Kletz: loại bỏ mối nguy "
                "(cường tập hóa, thay thế), làm dịu (suy yếu, giới hạn hệ quả), đơn giản hóa "
                "và điều khiển; bên phải là các nguyên tắc hỗ trợ. Sơ đồ biên tập theo mục 6.1 "
                "— không có trong nguyên bản.",
                "Figure A · Three tiers of Kletz's inherent-safety principles: eliminate the "
                "hazard (intensification, substitution), moderate (attenuation, limitation of "
                "effects), simplify and control; supporting principles at right. Editorial "
                "schematic after Section 6.1 — not present in the original.",
                "Sơ đồ phân tầng các nguyên tắc an toàn nội tại của Kletz",
                "Tiered schematic of Kletz's inherent safety principles")


def fig_c07_index():
    """Redraw of source Figure 5 (p. 40): principle of the formation of the
    index — principles → parameters → subindices."""
    w, h = 560, 300
    o = [_defs()]
    o.append(_box(120, 24, 320, 56,
                  "NGUYÊN TẮC AN TOÀN NỘI TẠI\nInherent safety principles\n"
                  "(Kletz — Chương 6.1)",
                  fill="#eaf6ee", sw=1.3, size=8.6))
    o.append(_box(120, 118, 320, 56,
                  "THAM SỐ AN TOÀN NỘI TẠI\nInherent safety parameters\n"
                  "(Bảng 5 — 19 tham số)",
                  fill="#eef3fb", sw=1.3, size=8.6))
    o.append(_box(120, 212, 320, 56,
                  "CHỈ SỐ THÀNH PHẦN AN TOÀN NỘI TẠI\nInherent safety subindices\n"
                  "(11 chỉ số — Chương 8–11)",
                  fill="#fdf3e6", sw=1.3, size=8.6))
    o.append(_arrow(280, 80, 280, 116, sw=1.6, color=GREY, head="a6"))
    o.append(_arrow(280, 174, 280, 210, sw=1.6, color=GREY, head="a6"))
    o.append(_txt(288, 101, "mô tả thành", 7.2, anchor="start", color=GREY))
    o.append(_txt(288, 195, "chọn quan trọng nhất", 7.2, anchor="start", color=GREY))
    o.append(_txt(280, h - 10,
                  "Vẽ lại theo Hình 5 (tr. 40) — nguyên tắc hình thành chỉ số",
                  7.4, color=GREY))
    s = svg(w, h, "".join(o),
            esc("Redrawn Figure 5: principle of the formation of the inherent safety index"))
    return _fig(s,
                "Hình 5 · Nguyên tắc hình thành chỉ số: các nguyên tắc an toàn nội tại "
                "được mô tả thành tham số, rồi các tham số quan trọng nhất được chọn làm "
                "chỉ số thành phần. Vẽ lại theo Hình 5, tr. 40.",
                "Figure 5 · Principle of the formation of the index: the inherent safety "
                "principles are described as parameters, and the most important parameters "
                "are selected as subindices. Redrawn after Figure 5, p. 40.",
                "Sơ đồ ba tầng hình thành chỉ số an toàn nội tại",
                "Three-tier formation of the inherent safety index")


def fig_c08_index():
    """Editorial schematic (not in the source) of Table 7 (p. 57): the total
    inherent safety index I_TI = I_CI + I_PI and its two subindex families."""
    w, h = 560, 340
    o = [_defs()]
    o.append(_box(160, 18, 240, 52,
                  "I<sub>TI</sub> — TỔNG CHỈ SỐ AN TOÀN NỘI TẠI\n"
                  "Total Inherent Safety Index  (Eq. 3)",
                  fill="#fdf3e6", sw=1.4, size=8.6))
    o.append(_box(30, 108, 235, 52,
                  "I<sub>CI</sub> — CHỈ SỐ AN TOÀN NỘI TẠI HÓA HỌC\n"
                  "Chemical Inherent Safety Index  (Eq. 4)",
                  fill="#eef3fb", sw=1.3, size=8.2))
    o.append(_box(295, 108, 235, 52,
                  "I<sub>PI</sub> — CHỈ SỐ AN TOÀN NỘI TẠI QUÁ TRÌNH\n"
                  "Process Inherent Safety Index  (Eq. 5)",
                  fill="#eef3fb", sw=1.3, size=8.2))
    o.append(_arrow(250, 70, 150, 106, sw=1.5, color=GREY, head="a6"))
    o.append(_arrow(310, 70, 410, 106, sw=1.5, color=GREY, head="a6"))
    o.append(_txt(158, 88, "+", 12, color=GREY, weight="700"))

    o.append(_rect(30, 178, 235, 122, "#f7fafd", 1.0))
    o.append(_txt(147, 192, "Phản ứng · Reaction hazards", 8.0,
                  color=BLUE, weight="600"))
    o.append(_txt(40, 208, "• nhiệt phản ứng chính  I<sub>RM</sub>", 7.6, color=INK))
    o.append(_txt(40, 224, "• nhiệt phản ứng phụ  I<sub>RS</sub>", 7.6, color=INK))
    o.append(_txt(40, 240, "• tương tác hóa học  I<sub>INT</sub>", 7.6, color=INK))
    o.append(_txt(147, 258, "Chất nguy hiểm · Substances", 8.0,
                  color=BLUE, weight="600"))
    o.append(_txt(40, 274, "• cháy  I<sub>FL</sub> · nổ  I<sub>EX</sub>", 7.6, color=INK))
    o.append(_txt(40, 290, "• độc tính  I<sub>TOX</sub> · ăn mòn  I<sub>COR</sub>",
                 7.6, color=INK))

    o.append(_rect(295, 178, 235, 122, "#f7fafd", 1.0))
    o.append(_txt(412, 192, "Điều kiện quá trình · Conditions", 8.0,
                  color=GREEN, weight="600"))
    o.append(_txt(305, 208, "• tồn kho  I<sub>I</sub>", 7.6, color=INK))
    o.append(_txt(305, 224, "• nhiệt độ  I<sub>T</sub> · áp suất  I<sub>P</sub>",
                  7.6, color=INK))
    o.append(_txt(412, 258, "Hệ thống quá trình · System", 8.0,
                  color=GREEN, weight="600"))
    o.append(_txt(305, 274, "• an toàn thiết bị  I<sub>EQ</sub>", 7.6, color=INK))
    o.append(_txt(305, 290, "• cấu trúc quá trình an toàn  I<sub>ST</sub>",
                  7.6, color=INK))

    o.append(_txt(280, h - 8,
                  "Sơ đồ A — cấu trúc chỉ số theo Bảng 7 (tr. 57); không có trong tài liệu gốc",
                  7.4, color=GREY))
    s = svg(w, h, "".join(o),
            esc("Schematic: total inherent safety index decomposition into chemical and process subindices (Table 7)"))
    return _fig(s,
                "Sơ đồ A · Tổng chỉ số an toàn nội tại I<sub>TI</sub> = I<sub>CI</sub> + "
                "I<sub>PI</sub> và các chỉ số thành phần theo Bảng 7. Sơ đồ biên soạn — "
                "không có trong tài liệu gốc.",
                "Figure A · Total inherent safety index I<sub>TI</sub> = I<sub>CI</sub> + "
                "I<sub>PI</sub> and its subindex families after Table 7. Editorial schematic "
                "— not in the original.",
                "Phân rã tổng chỉ số an toàn nội tại thành các nhóm chỉ số hóa học và quá trình",
                "Decomposition of the total inherent safety index into chemical and process subindex groups")


def fig_c09_weights():
    """Editorial bar chart (not in the source) of Table 8 (p. 61): the score
    range of each subindex, chemical group in blue, process group in green."""
    w, h = 560, 360
    o = [_defs()]
    rows = [
        # (label_vi, label_en, max, group)  scale: 6 -> 300 px
        ("Độc tính  I<sub>TOX</sub>", "Toxic exposure", 6, "c"),
        ("Tồn kho  I<sub>I</sub>", "Inventory", 5, "p"),
        ("Cấu trúc quá trình an toàn  I<sub>ST</sub>", "Safe process structure", 5, "p"),
        ("Nhiệt phản ứng chính  I<sub>RM</sub>", "Heat of main reaction", 4, "c"),
        ("Nhiệt phản ứng phụ  I<sub>RS</sub>", "Heat of side reaction", 4, "c"),
        ("Tương tác hóa học  I<sub>INT</sub>", "Chemical interaction", 4, "c"),
        ("Khả cháy  I<sub>FL</sub>", "Flammability", 4, "c"),
        ("Khả nổ  I<sub>EX</sub>", "Explosiveness", 4, "c"),
        ("Nhiệt độ quá trình  I<sub>T</sub>", "Process temperature", 4, "p"),
        ("Áp suất quá trình  I<sub>P</sub>", "Process pressure", 4, "p"),
        ("An toàn thiết bị (Isbl/Osbl)  I<sub>EQ</sub>", "Equipment safety", 4, "p"),
        ("Khả ăn mòn  I<sub>COR</sub>", "Corrosiveness", 2, "c"),
    ]
    x0, bw = 268, 4.0          # bar origin, px per score point
    y = 34
    for lv, le, mx, g in rows:
        col = "#4a7fb5" if g == "c" else "#3d8b62"
        o.append(_txt(x0 - 6, y + 4, lv, 7.4, anchor="end", color=INK))
        o.append(_rect(x0, y, bw * mx, 11, "#f0f4f8", 0))
        o.append(_rect(x0, y, bw * mx, 11, col, 0))
        o.append(_txt(x0 + bw * mx + 5, y + 4, "0–%d" % mx, 7.2,
                      anchor="start", color=GREY))
        y += 22
    o.append(_txt(268 + 24 + 6, y + 6, "điểm tối đa · max score", 7.4,
                  anchor="middle", color=GREY))
    # legend
    o.append(_rect(30, 30, 10, 10, "#4a7fb5", 0))
    o.append(_txt(45, 39, "hóa học I<sub>CI</sub> · chemical", 7.6,
                  anchor="start", color=INK))
    o.append(_rect(30, 46, 10, 10, "#3d8b62", 0))
    o.append(_txt(45, 55, "quá trình I<sub>PI</sub> · process", 7.6,
                  anchor="start", color=INK))
    o.append(_txt(280, h - 8,
                  "Sơ đồ A — trực quan hóa Bảng 8 (tr. 61); không có trong tài liệu gốc",
                  7.4, color=GREY))
    s = svg(w, h, "".join(o),
            esc("Bar chart of the maximum score of each inherent safety subindex after Table 8"))
    return _fig(s,
                "Sơ đồ A · Phạm vi điểm tối đa của từng chỉ số thành phần theo Bảng 8 — "
                "độc tính (6) và tồn kho (5) chiếm trọng số cao nhất. Sơ đồ biên soạn — "
                "không có trong tài liệu gốc.",
                "Figure A · Maximum score of each subindex after Table 8 — toxicity (6) "
                "and inventory (5) carry the highest weights. Editorial schematic — not "
                "in the original.",
                "Biểu đồ phạm vi điểm các chỉ số thành phần an toàn nội tại",
                "Score-range chart of the inherent safety subindices")


def fig_c11_levels():
    """Redraw of source Figure 6 (p. 88): the levels of the process as used in
    the CBR database (0=process ... 5=detail), with a hydrogenation example."""
    w, h = 560, 372
    o = [_defs()]
    rows = [
        ("0 · QUÁ TRÌNH", "Process", "Phân xưởng hiđro hóa", "Hydrogenation unit",
         "#fdf3e6"),
        ("1 · QUÁ TRÌNH CON", "Subprocess", "Phần phản ứng", "Reactor section",
         "#eef3fb"),
        ("2 · HỆ THỐNG", "System", "Cột chưng cất + trợ giúp", "Distillation column with auxiliaries",
         "#eef3fb"),
        ("3 · HỆ CON", "Subsystem", "Hệ đỉnh cột", "Column overhead system",
         "#eaf6ee"),
        ("4 · THIẾT BỊ", "Equipment", "Bộ trao đổi nhiệt / cột", "Heat exchanger / column",
         "#eaf6ee"),
        ("5 · CHI TIẾT", "Detail", "Khay chưng cất / van điều khiển", "Tray / control valve",
         "#eaf6ee"),
    ]
    y = 26
    for i, (lv, len_, ex_vi, ex_en, col) in enumerate(rows):
        o.append(_rect(60, y, 150, 38, col, 1.2))
        o.append(_txt(135, y + 15, lv, 7.8, color=INK, weight="600"))
        o.append(_txt(135, y + 28, len_, 7.0, color=GREY))
        o.append(_txt(226, y + 19, "→", 11, color=GREY))
        o.append(_txt(246, y + 15, ex_vi, 7.8, color=INK))
        o.append(_txt(246, y + 28, ex_en, 7.0, color=GREY))
        if i < len(rows) - 1:
            o.append(_line(135, y + 38, 135, y + 50, 1.2, GREY))
        y += 52
    o.append(_txt(280, h - 8,
                  "Vẽ lại theo Hình 6 (tr. 88) — các mức quá trình trong cơ sở dữ liệu CBR",
                  7.4, color=GREY))
    s = svg(w, h, "".join(o),
            esc("Redrawn Figure 6: the six levels of the process used in the case-based reasoning database"))
    return _fig(s,
                "Hình 6 · Ví dụ về các mức của quá trình trong cơ sở dữ liệu CBR "
                "(0 = quá trình, 1 = quá trình con, 2 = hệ thống, 3 = hệ con, "
                "4 = thiết bị, 5 = chi tiết). Vẽ lại theo tài liệu gốc, tr. 88.",
                "Figure 6 · Example of the levels of the process as used in the CBR "
                "database (0 = process, 1 = subprocess, 2 = system, 3 = subsystem, "
                "4 = equipment, 5 = detail). Redrawn after the original, p. 88.",
                "Sơ đồ các mức quá trình trong cơ sở dữ liệu CBR",
                "The six process levels used in the CBR database")


def fig_c12_flowsheet():
    """Redraw of source Figure 7 (p. 92): flowsheet of the acetic acid process
    (methanol carbonylation) — seven numbered units."""
    w, h = 560, 300
    o = [_defs()]

    def unit(x, y, num, vi, en, wd=86, fill="#eef3fb"):
        o.append(_rect(x, y, wd, 46, fill, 1.2))
        o.append(_circle(x + 13, y + 13, 9, "#fdf3e6", 1.0))
        o.append(_txt(x + 13, y + 16, str(num), 8.2, color=INK, weight="600"))
        o.append(_txt(x + wd / 2 + 6, y + 16, vi, 7.6, color=INK, weight="600"))
        o.append(_txt(x + wd / 2 + 6, y + 29, en, 6.6, color=GREY))

    # top row: reaction section
    unit(20, 60, 1, "Lò phản ứng", "Reactor", 92)
    unit(160, 60, 2, "Bộ tách", "Separator", 86)
    unit(300, 60, 3, "Tháp rửa", "Scrubber", 86)
    # bottom row: distillation train
    unit(60, 180, 4, "Cột đầu nhẹ", "Light ends", 86)
    unit(190, 180, 5, "Cột sấy", "Drying", 76)
    unit(310, 180, 6, "Cột sản phẩm", "Product", 82)
    unit(436, 180, 7, "Cột tinh chế", "Finishing", 84)

    # streams
    o.append(_arrow(112, 83, 158, 83, 1.4, GREY, head="a6"))
    o.append(_txt(135, 74, "", 7))
    o.append(_arrow(246, 83, 298, 83, 1.4, GREY, head="a6"))
    o.append(_arrow(343, 74, 343, 40, 1.2, GREY, head="a6"))
    o.append(_txt(349, 46, "CO", 7.6, anchor="start", color=BLUE))
    o.append(_arrow(203, 106, 203, 178, 1.4, GREY, head="a6"))
    o.append(_txt(209, 140, "lỏng · liquid", 7.0, anchor="start", color=GREY))
    # methanol recycle scrubber -> reactor
    o.append(_line(300, 96, 250, 96, 1.2, GREY))
    o.append(_line(250, 96, 250, 130, 1.2, GREY))
    o.append(_line(250, 130, 66, 130, 1.2, GREY))
    o.append(_arrow(66, 130, 66, 108, 1.2, GREY, head="a6"))
    o.append(_txt(256, 124, "MeOH hồi lưu · recycle", 7.0, anchor="start", color=GREY))
    # feed arrows
    o.append(_arrow(20, 20, 52, 58, 1.2, GREY, head="a6"))
    o.append(_txt(24, 16, "CO + MeOH", 7.6, anchor="start", color=BLUE))
    o.append(_arrow(146, 226, 188, 226, 1.4, GREY, head="a6"))
    o.append(_txt(167, 219, "axit axetic · acetic acid", 6.8, anchor="middle", color=GREY))
    o.append(_arrow(266, 226, 308, 226, 1.4, GREY, head="a6"))
    o.append(_arrow(392, 226, 434, 226, 1.4, GREY, head="a6"))
    o.append(_txt(411, 219, "", 7))
    o.append(_arrow(222, 180, 222, 150, 1.2, GREY, head="a6"))
    o.append(_txt(228, 156, "nước · water", 7.0, anchor="start", color=GREY))
    o.append(_arrow(351, 180, 351, 150, 1.2, GREY, head="a6"))
    o.append(_txt(357, 156, "đầu nặng · heavy ends", 7.0, anchor="start", color=GREY))
    o.append(_arrow(520, 226, 546, 226, 1.4, GREY, head="a6"))
    o.append(_txt(546, 216, "axit axetic · acetic acid", 7.2, anchor="end", color=BLUE))
    o.append(_txt(280, h - 8,
                  "Vẽ lại theo Hình 7 (tr. 92) — sơ đồ quá trình axit axetic (cacbonyl hóa methanol)",
                  7.4, color=GREY))
    s = svg(w, h, "".join(o),
            esc("Redrawn Figure 7: flowsheet of the acetic acid process with seven numbered units"))
    return _fig(s,
                "Hình 7 · Sơ đồ quá trình axit axetic: 1) lò phản ứng, 2) bộ tách, "
                "3) tháp rửa, 4) cột tách đầu nhẹ, 5) cột sấy, 6) thu hồi sản phẩm, "
                "7) tinh chế sản phẩm. Vẽ lại theo tài liệu gốc, tr. 92.",
                "Figure 7 · Flowsheet of the acetic acid process: 1) reactor, "
                "2) separator, 3) scrubber, 4) light-ends separator, 5) drying "
                "column, 6) product recovery, 7) product finishing. Redrawn after "
                "the original, p. 92.",
                "Sơ đồ quá trình sản xuất axit axetic",
                "Flowsheet of the acetic acid process")


def fig_c13_cooling():
    """Redraw of source Figure 8 (p. 101): recommendation to avoid the feedback
    loop between reactor heat rise and coolant-temperature rise."""
    w, h = 560, 240
    o = [_defs()]

    def reactor(x, y, fill="#eef3fb"):
        o.append(_rect(x, y, 90, 56, fill, 1.3))
        o.append(_txt(x + 45, y + 24, "LÒ PHẢN ỨNG", 7.4, color=INK, weight="600"))
        o.append(_txt(x + 45, y + 37, "REACTOR", 6.6, color=GREY))

    def hx(x, y, label_vi, label_en, fill="#eaf6ee"):
        o.append(_rect(x, y, 96, 40, fill, 1.2))
        o.append(_txt(x + 48, y + 16, label_vi, 7.2, color=INK, weight="600"))
        o.append(_txt(x + 48, y + 28, label_en, 6.4, color=GREY))

    # left — recommended: coolant temperature independent of reactor
    o.append(_txt(140, 18, "KHUYẾN NGHỊ · RECOMMENDED", 8.2,
                  color="#1f5f8b", weight="700"))
    reactor(20, 40)
    hx(20, 150, "Sinh hơi MP · Steam gen", "BFW → MP STM")
    o.append(_arrow(65, 96, 65, 148, 1.4, GREY, head="a6"))
    o.append(_arrow(65, 190, 65, 210, 1.4, GREY, head="a6"))
    o.append(_txt(58, 206, "MP STM", 7.2, anchor="end", color=BLUE))
    o.append(_arrow(16, 170, 2, 170, 1.2, GREY, head="a6"))
    o.append(_txt(30, 164, "BFW", 7.2, anchor="start", color=BLUE))
    o.append(_arrow(112, 62, 148, 62, 1.4, GREY, head="a6"))
    o.append(_txt(130, 55, "O₂", 7.4, anchor="middle", color=BLUE))
    o.append(_arrow(112, 90, 148, 90, 1.4, GREY, head="a6"))
    o.append(_txt(130, 102, "PRODUCT", 7.0, anchor="middle", color=GREY))
    o.append(_txt(16, 232, "Nhiệt độ coolant độc lập với nhiệt độ lò phản ứng",
                  7.2, anchor="start", color=GREY))

    # right — not recommended: feedback loop LP STM/BFW heated by reactor
    o.append(_txt(430, 18, "KHÔNG KHUYẾN NGHỊ · NOT RECOMMENDED", 8.2,
                  color=RED, weight="700"))
    reactor(310, 40, "#fdeaea")
    hx(310, 150, "Làm mát tuần hoàn", "LP STM / BFW", "#fdeaea")
    o.append(_arrow(355, 96, 355, 148, 1.4, GREY, head="a6"))
    o.append(_arrow(355, 190, 355, 210, 1.4, GREY, head="a6"))
    o.append(_txt(348, 206, "LP STM", 7.2, anchor="end", color=RED))
    o.append(_arrow(306, 170, 292, 170, 1.2, GREY, head="a6"))
    o.append(_txt(320, 164, "BFW", 7.2, anchor="start", color=BLUE))
    # feedback loop arrow: coolant temp rises with reactor temp
    o.append(_line(408, 170, 440, 170, 1.4, RED))
    o.append(_line(440, 170, 440, 68, 1.4, dash="4 3", color=RED))
    o.append(_arrow(440, 68, 402, 68, 1.4, RED, head="a6"))
    o.append(_txt(446, 120, "vòng phản hồi\n(feedback)", 7.0, anchor="start", color=RED))
    o.append(_txt(306, 232, "Nhiệt độ coolant tăng theo nhiệt độ lò phản ứng",
                  7.2, anchor="start", color=GREY))
    s = svg(w, h, "".join(o),
            esc("Redrawn Figure 8: recommended vs not-recommended reactor cooling systems"))
    return _fig(s,
                "Hình 8 · Khuyến nghị tránh vòng phản hồi giữa mức tăng nhiệt của lò "
                "phản ứng và mức tăng nhiệt độ chất làm mát. Vẽ lại theo tài liệu "
                "gốc, tr. 101.",
                "Figure 8 · A recommendation to avoid the feedback loop between a "
                "reactor heat rise and a rise in coolant temperature. Redrawn after "
                "the original, p. 101.",
                "So sánh hệ làm mát lò phản ứng khuyến nghị và không khuyến nghị",
                "Recommended vs not-recommended reactor cooling systems")


def fig_c13_preheat():
    """Redraw of source Figure 9 (p. 102): recommendation for preheating the
    feed of an exothermic reactor."""
    w, h = 560, 240
    o = [_defs()]

    def reactor(x, y, fill="#eef3fb"):
        o.append(_rect(x, y, 90, 56, fill, 1.3))
        o.append(_txt(x + 45, y + 24, "LÒ PHẢN ỨNG", 7.4, color=INK, weight="600"))
        o.append(_txt(x + 45, y + 37, "REACTOR", 6.6, color=GREY))

    def hx(x, y, vi, en, fill="#eaf6ee"):
        o.append(_rect(x, y, 100, 40, fill, 1.2))
        o.append(_txt(x + 50, y + 16, vi, 7.2, color=INK, weight="600"))
        o.append(_txt(x + 50, y + 28, en, 6.4, color=GREY))

    # left — NOT recommended: feed heated by product (feedback)
    o.append(_txt(140, 18, "KHÔNG KHUYẾN NGHỊ · NOT RECOMMENDED", 8.2,
                  color=RED, weight="700"))
    reactor(20, 40, "#fdeaea")
    hx(20, 150, "Sấy nóng bằng sản phẩm", "Feed ↔ product", "#fdeaea")
    o.append(_arrow(20, 210, 20, 160, 1.4, GREY, head="a6"))
    o.append(_txt(24, 216, "FEED", 7.2, anchor="start", color=BLUE))
    o.append(_arrow(70, 96, 70, 148, 1.4, GREY, head="a6"))
    o.append(_arrow(112, 68, 150, 68, 1.4, GREY, head="a6"))
    o.append(_txt(131, 61, "PRODUCT", 7.0, anchor="middle", color=GREY))
    o.append(_line(150, 68, 150, 124, 1.4, dash="4 3", color=RED))
    o.append(_arrow(150, 124, 74, 160, 1.4, RED, head="a6"))
    o.append(_txt(158, 120, "sản phẩm sấy nóng feed", 7.0, anchor="start", color=RED))
    o.append(_txt(16, 232, "Nhiệt độ lò tăng → nhiệt độ feed tăng (vòng phản hồi)",
                  7.2, anchor="start", color=GREY))

    # right — recommended: heat transfer via MP steam generation
    o.append(_txt(424, 18, "KHUYẾN NGHỊ · RECOMMENDED", 8.2,
                  color="#1f5f8b", weight="700"))
    reactor(300, 40)
    hx(300, 150, "Sinh hơi MP trung gian", "MPS generation")
    o.append(_arrow(300, 210, 300, 160, 1.4, GREY, head="a6"))
    o.append(_txt(304, 216, "FEED", 7.2, anchor="start", color=BLUE))
    o.append(_arrow(350, 96, 350, 148, 1.4, GREY, head="a6"))
    o.append(_arrow(392, 68, 430, 68, 1.4, GREY, head="a6"))
    o.append(_txt(411, 61, "PRODUCT", 7.0, anchor="middle", color=GREY))
    o.append(_arrow(350, 190, 350, 214, 1.4, GREY, head="a6"))
    o.append(_txt(356, 208, "MPS · hơi áp trung", 7.0, anchor="start", color=BLUE))
    o.append(_txt(296, 232, "Liên kết nhiệt đứt qua hơi trung áp — an toàn hơn",
                  7.2, anchor="start", color=GREY))
    s = svg(w, h, "".join(o),
            esc("Redrawn Figure 9: recommended vs not-recommended feed preheating of an exothermic reactor"))
    return _fig(s,
                "Hình 9 · Khuyến nghị sấy nóng cấp feed của lò phản ứng tỏa nhiệt — "
                "truyền nhiệt qua sinh hơi trung áp thay vì bằng sản phẩm. Vẽ lại "
                "theo tài liệu gốc, tr. 102.",
                "Figure 9 · A recommendation for preheating the feed of an "
                "exothermic reactor — heat transfer via medium-pressure steam "
                "generation instead of the product. Redrawn after the original, "
                "p. 102.",
                "So sánh phương án sấy nóng feed khuyến nghị và không khuyến nghị",
                "Recommended vs not-recommended feed preheating")


FIGS = {
    "isd_intro": fig_isd_intro,
    "f01": fig_f01,
    "f02": fig_f02,
    "f03": fig_f03,
    "c04_stages": fig_c04_stages,
    "c04_indices": fig_c04_indices,
    "c05_curves": fig_c05_curves,
    "c05_gap": fig_c05_gap,
    "c06_kletz": fig_c06_kletz,
    "c06_principles": fig_c06_principles,
    "c07_index": fig_c07_index,
    "c08_index": fig_c08_index,
    "c09_weights": fig_c09_weights,
    "c11_levels": fig_c11_levels,
    "c12_flowsheet": fig_c12_flowsheet,
    "c13_cooling": fig_c13_cooling,
    "c13_preheat": fig_c13_preheat,
}


def fig_c14_synthesis():
    """Redraw of source Figure 10 (p. 104): approach of Hurme and
    Järveläinen (1995) — synthesis with simulation, costing, profitability."""
    w, h = 560, 250
    o = [_defs()]
    o.append(_box(30, 30, 110, 46, "CƠ SỞ LUẬT\nRule base", fill="#eef3fb", sw=1.2, size=8.2))
    o.append(_box(30, 100, 110, 40, "Người dùng\nUser", fill="#fdf3e6", sw=1.2, size=8.2))
    o.append(_box(190, 46, 110, 44, "TỔNG HỢP\nSynthesis", fill="#eaf6ee", sw=1.3, size=8.4))
    o.append(_box(340, 20, 90, 34, "PT 1 · Alt 1", fill="#f7fafd", sw=1.0, size=8))
    o.append(_box(340, 62, 90, 34, "PT 2 · Alt 2", fill="#f7fafd", sw=1.0, size=8))
    o.append(_box(340, 104, 90, 34, "PT 3 · Alt 3", fill="#f7fafd", sw=1.0, size=8))
    o.append(_box(340, 152, 90, 60, "MÔ PHỎNG\nSimulation\n→ chi phí · costing\n→ lợi nhuận · profitability",
                  fill="#eef3fb", sw=1.1, size=7.6))
    o.append(_box(452, 152, 88, 60, "PHƯƠNG ÁN\nĐƯỢC CHỌN\nChosen\nalternative",
                  fill="#eaf6ee", sw=1.3, size=7.8))
    o.append(_arrow(140, 60, 188, 66, 1.3, GREY, head="a6"))
    o.append(_arrow(140, 118, 188, 74, 1.3, GREY, head="a6"))
    o.append(_arrow(300, 68, 338, 40, 1.3, GREY, head="a6"))
    o.append(_arrow(300, 68, 338, 78, 1.3, GREY, head="a6"))
    o.append(_arrow(300, 68, 338, 120, 1.3, GREY, head="a6"))
    for yy in (37, 79, 121):
        o.append(_arrow(430, yy, 430, 150, 1.0, GREY, head="a6"))
    o.append(_arrow(430, 182, 450, 182, 1.4, GREY, head="a6"))
    o.append(_txt(280, h - 8,
                  "Vẽ lại theo Hình 10 (tr. 104) — nguyên lý tiếp cận Hurme và Järveläinen (1995)",
                  7.4, color=GREY))
    s = svg(w, h, "".join(o), esc("Redrawn Figure 10: combined process synthesis, simulation and costing"))
    return _fig(s,
                "Hình 10 · Nguyên lý của cách tiếp cận Hurme và Järveläinen (1995): "
                "tổng hợp dựa trên luật, mô phỏng, đánh giá chi phí và phân tích "
                "lợi nhuận. Vẽ lại theo tài liệu gốc, tr. 104.",
                "Figure 10 · The principle of the approach by Hurme and Järveläinen "
                "(1995): rule-based synthesis, simulation, costing and "
                "profitability analysis. Redrawn after the original, p. 104.",
                "Sơ đồ tổng hợp quá trình kết hợp mô phỏng",
                "Combined process synthesis and simulation system")


def fig_c14_combined():
    """Redraw of source Figure 11 (p. 105): combined synthesis with
    environmental and safety aspects (Heikkilä et al., 1996)."""
    w, h = 560, 300
    o = [_defs()]
    o.append(_box(20, 30, 92, 42, "Cơ sở luật\nRule base", fill="#eef3fb", sw=1.1, size=7.8))
    o.append(_box(20, 86, 92, 36, "Người dùng\nUser", fill="#fdf3e6", sw=1.1, size=7.8))
    o.append(_box(150, 42, 100, 40, "Tổng hợp\nSynthesis", fill="#eaf6ee", sw=1.2, size=8.2))
    o.append(_box(288, 42, 92, 40, "Mô phỏng\nSimulation", fill="#eef3fb", sw=1.1, size=8))
    o.append(_box(288, 96, 92, 40, "Chi phí &amp;\nlợi nhuận\nCosting &amp; profit.", fill="#eef3fb", sw=1.1, size=7.6))
    o.append(_box(288, 150, 92, 40, "Phân tích\nmôi trường\nEnvironmental", fill="#eef3fb", sw=1.1, size=7.6))
    o.append(_box(410, 96, 118, 46, "SO SÁNH AN TOÀN\nSafety comparison\n(chỉ số ISI)",
                  fill="#fdeaea", sw=1.3, size=7.8))
    o.append(_box(430, 170, 100, 42, "Phương án\nđược chọn\nChosen alternative",
                  fill="#eaf6ee", sw=1.3, size=7.8))
    # databanks row
    for i, (vi, en) in enumerate([
            ("Ngân hàng\năn mòn", "corrosion"),
            ("Tính chất\nan toàn", "safety props."),
            ("An toàn\nthiết bị", "equipment"),
            ("Tương tác\nhóa học", "chem. interact."),
            ("Cấu trúc\nquá trình", "proc. structure")]):
        x = 118 + i * 88
        o.append(_rect(x, 226, 82, 42, "#f7fafd", 1.0))
        o.append(_txt(x + 41, 240, vi, 7.0, color=INK))
        o.append(_txt(x + 41, 256, en, 6.4, color=GREY))
        o.append(_line(x + 41, 226, x + 41, 216, 1.0, GREY))
    o.append(_line(334, 216, 469, 130, 1.0, dash="3 2", color=GREY))
    o.append(_txt(334, 222, "dữ liệu hỗ trợ so sánh an toàn · data supporting the safety comparison",
                  7.0, color=GREY))
    o.append(_arrow(112, 52, 148, 60, 1.3, GREY, head="a6"))
    o.append(_arrow(112, 104, 148, 72, 1.3, GREY, head="a6"))
    o.append(_arrow(250, 62, 286, 62, 1.3, GREY, head="a6"))
    o.append(_arrow(334, 82, 380, 106, 1.3, GREY, head="a6"))
    o.append(_arrow(334, 116, 380, 116, 1.3, GREY, head="a6"))
    o.append(_arrow(334, 170, 380, 132, 1.3, GREY, head="a6"))
    o.append(_arrow(469, 142, 476, 168, 1.3, GREY, head="a6"))
    o.append(_txt(280, h - 8,
                  "Vẽ lại theo Hình 11 (tr. 105) — tổng hợp quá trình kết hợp môi trường và an toàn",
                  7.4, color=GREY))
    s = svg(w, h, "".join(o), esc("Redrawn Figure 11: combined synthesis with environmental and safety analysis"))
    return _fig(s,
                "Hình 11 · Nguyên lý tổng hợp quá trình kết hợp của Heikkilä và cộng "
                "sự (1996): mô phỏng, chi phí–lợi nhuận, phân tích môi trường và so "
                "sánh an toàn theo ISI. Vẽ lại theo tài liệu gốc, tr. 105.",
                "Figure 11 · The principles of the combined process synthesis by "
                "Heikkilä et al. (1996): simulation, costing and profitability, "
                "environmental analysis and ISI-based safety comparison. Redrawn "
                "after the original, p. 105.",
                "Sơ đồ tổng hợp kết hợp phân tích môi trường và an toàn",
                "Combined synthesis with environmental and safety analysis")


def fig_c14_ga():
    """Redraw of source Figure 12 (p. 108): the structure of a classical GA
    (Moraga and Bexten, 1997)."""
    w, h = 560, 250
    o = [_defs()]
    steps = [
        ("Quần thể\nhiện tại", "Actual\npopulation"),
        ("Tính độ thích\nnghi (fitness)", "Computation of\nthe fitness"),
        ("Lựa chọn", "Selection"),
        ("Sinh sản", "Reproduction"),
        ("Ghép cặp", "Mating"),
        ("Lai ghép", "Crossover"),
        ("Đột biến", "Mutation"),
    ]
    n = len(steps)
    for i, (vi, en) in enumerate(steps):
        x = 24 + i * 76
        o.append(_rect(x, 60, 68, 50, "#eef3fb" if i else "#fdf3e6", 1.1))
        o.append(_txt(x + 34, 78, vi, 7.2, color=INK, weight="600"))
        o.append(_txt(x + 34, 94, en, 6.4, color=GREY))
        if i < n - 1:
            o.append(_arrow(x + 68, 85, x + 76, 85, 1.3, GREY, head="a6"))
    # loop back
    o.append(_line(526, 110, 526, 160, 1.3, GREY))
    o.append(_line(526, 160, 58, 160, 1.3, GREY))
    o.append(_arrow(58, 160, 58, 112, 1.3, GREY, head="a6"))
    o.append(_txt(292, 174, "lặp cho tới điều kiện dừng · repeat until termination condition",
                  7.2, color=GREY))
    o.append(_txt(280, h - 8,
                  "Vẽ lại theo Hình 12 (tr. 108) — cấu trúc giải thuật di truyền cổ điển (Moraga và Bexten, 1997)",
                  7.4, color=GREY))
    s = svg(w, h, "".join(o), esc("Redrawn Figure 12: structure of a classical genetic algorithm"))
    return _fig(s,
                "Hình 12 · Cấu trúc của giải thuật di truyền cổ điển (Moraga và Bexten, "
                "1997): đánh giá độ thích nghi, lựa chọn, sinh sản, ghép cặp, lai ghép "
                "và đột biến, lặp tới điều kiện dừng. Vẽ lại theo tài liệu gốc, tr. 108.",
                "Figure 12 · The structure of a classical GA (Moraga and Bexten, "
                "1997): fitness computation, selection, reproduction, mating, "
                "crossover and mutation, repeated until a termination condition. "
                "Redrawn after the original, p. 108.",
                "Chu trình giải thuật di truyền",
                "The genetic-algorithm cycle")


def fig_c14_separations():
    """Redraw of source Figure 13 (p. 111): two process configurations for
    separating five components 1–5 by three methods 1–3."""
    w, h = 560, 250
    o = [_defs()]

    def node(cx, cy, label, r=15, fill="#eef3fb"):
        o.append(_circle(cx, cy, r, fill, 1.1))
        o.append(_txt(cx, cy + 3, label, 7.8, color=INK, weight="600"))

    def split(x1, y1, x2, y2, x3, y3):
        o.append(_line(x1, y1, x2, y2, 1.2, GREY))
        o.append(_line(x1, y1, x3, y3, 1.2, GREY))

    # left tree: gene 23 12 14 11
    o.append(_txt(140, 20, "CÂY 1 · mã gen 23 12 14 11", 8.0, color="#1f5f8b", weight="700"))
    node(140, 60, "1,2,3,4,5")
    split(140, 75, 70, 120, 210, 120)
    o.append(_txt(100, 92, "PP2", 7.2, color=GREY))
    node(70, 135, "1,2,3")
    node(210, 135, "4,5")
    split(70, 150, 40, 190, 105, 190)
    o.append(_txt(50, 168, "PP1", 7.2, color=GREY))
    node(40, 205, "1")
    node(105, 205, "2,3")
    o.append(_txt(140, 210, "PP1", 7.2, color=GREY))
    o.append(_line(210, 150, 210, 175, 1.2, GREY))
    node(210, 190, "4")
    node(262, 190, "5")

    # right tree: gene 12 23 14 11 (variant)
    o.append(_txt(430, 20, "CÂY 2 · phương án thay thế", 8.0, color="#1f5f8b", weight="700"))
    node(430, 60, "1,2,3,4,5")
    split(430, 75, 360, 120, 500, 120)
    o.append(_txt(390, 92, "PP1", 7.2, color=GREY))
    node(360, 135, "1")
    node(500, 135, "2,3,4,5")
    split(500, 150, 445, 190, 530, 190)
    o.append(_txt(468, 168, "PP3", 7.2, color=GREY))
    node(445, 205, "2")
    node(530, 205, "3,4,5")
    o.append(_txt(500, 235, "PP1 · PP2 tiếp tục · continued", 7.0, color=GREY))
    o.append(_txt(280, h - 8,
                  "Vẽ lại theo Hình 13 (tr. 111) — hai cấu hình tách 5 cấu tử bằng 3 phương pháp (PP)",
                  7.4, color=GREY))
    s = svg(w, h, "".join(o), esc("Redrawn Figure 13: two separation configurations for five components"))
    return _fig(s,
                "Hình 13 · Hai cấu hình quá trình để tách năm cấu tử 1–5 bằng ba "
                "phương pháp 1–3 (cây tách nhị phân; PP = phương pháp tách). "
                "Vẽ lại theo tài liệu gốc, tr. 111.",
                "Figure 13 · Two process configurations for separating five "
                "components 1–5 by three methods 1–3 (binary separation trees; "
                "PP = separation method). Redrawn after the original, p. 111.",
                "Hai cây tách quá trình",
                "Two separation process configurations")


def fig_c14_polymer():
    """Redraw of source Figure 14 (p. 116): the synthesized emulsion
    polymerization system."""
    w, h = 560, 250
    o = [_defs()]
    o.append(_rect(120, 60, 110, 90, "#eef3fb", 1.3))
    o.append(_txt(175, 84, "LÒ PHẢN ỨNG", 8.0, color=INK, weight="600"))
    o.append(_txt(175, 98, "REACTOR · semibatch", 7.0, color=GREY))
    o.append(_txt(175, 112, "áo khoác làm mát · jacket", 6.6, color=GREY))
    o.append(_txt(175, 124, "2 khuấy cùng trục · 2 mixers", 6.6, color=GREY))
    o.append(_txt(175, 136, "thép tráng bóng · polished steel", 6.6, color=GREY))
    # reflux condenser above
    o.append(_rect(140, 18, 70, 28, "#eaf6ee", 1.1))
    o.append(_txt(175, 30, "BỘ NGƯNG · RD", 7.0, color=INK, weight="600"))
    o.append(_txt(175, 40, "reflux condenser", 6.2, color=GREY))
    o.append(_line(175, 46, 175, 58, 1.2, GREY))
    o.append(_arrow(140, 84, 118, 84, 1.3, GREY, head="a6"))
    o.append(_txt(116, 78, "N₂", 7.4, anchor="end", color=BLUE))
    o.append(_arrow(20, 110, 118, 110, 1.3, GREY, head="a6"))
    o.append(_txt(24, 102, "monome + xúc tác · monomers &amp; catalyst", 7.2, anchor="start", color=BLUE))
    o.append(_arrow(20, 136, 118, 136, 1.3, GREY, head="a6"))
    o.append(_txt(24, 128, "chất ức chế · inhibitor", 7.2, anchor="start", color=BLUE))
    # to quench tank
    o.append(_arrow(230, 120, 280, 120, 1.4, GREY, head="a6"))
    o.append(_rect(282, 96, 104, 48, "#fdeaea", 1.2))
    o.append(_txt(334, 114, "BỨT DẬP", 7.8, color=INK, weight="600"))
    o.append(_txt(334, 128, "quench tank · RD + quench", 6.6, color=GREY))
    # to flare
    o.append(_arrow(386, 110, 436, 110, 1.4, GREY, head="a6"))
    o.append(_txt(442, 106, "xả tới ống đốt", 7.2, anchor="start", color=GREY))
    o.append(_txt(442, 118, "vent to flare", 6.6, anchor="start", color=GREY))
    # to product tank
    o.append(_arrow(334, 144, 334, 176, 1.4, GREY, head="a6"))
    o.append(_rect(282, 178, 104, 44, "#eaf6ee", 1.2))
    o.append(_txt(334, 196, "BỒN SẢN PHẨM", 7.8, color=INK, weight="600"))
    o.append(_txt(334, 210, "product tank · latex", 6.6, color=GREY))
    o.append(_txt(280, h - 8,
                  "Vẽ lại theo Hình 14 (tr. 116) — hệ trùng hợp nhũ từ được tổng hợp (an toàn nội tại tối ưu)",
                  7.4, color=GREY))
    s = svg(w, h, "".join(o), esc("Redrawn Figure 14: the synthesized emulsion polymerization system"))
    return _fig(s,
                "Hình 14 · Hệ trùng hợp nhũ từ được tổng hợp: lò phản ứng bán liên "
                "tục với áo khoác làm mát và bộ ngưng hồi lưu, đĩa nổ + bể dập, "
                "xả tới ống đốt, bồn sản phẩm. Vẽ lại theo tài liệu gốc, tr. 116.",
                "Figure 14 · The synthesized emulsion polymerization system: "
                "semibatch reactor with cooling jacket and reflux condenser, "
                "rupture disk + quench tank, vent to flare, product tank. Redrawn "
                "after the original, p. 116.",
                "Hệ trùng hợp nhũ tổng hợp",
                "The synthesized emulsion polymerization system")


FIGS.update({
    "c14_synthesis": fig_c14_synthesis,
    "c14_combined": fig_c14_combined,
    "c14_ga": fig_c14_ga,
    "c14_separations": fig_c14_separations,
    "c14_polymer": fig_c14_polymer,
})
