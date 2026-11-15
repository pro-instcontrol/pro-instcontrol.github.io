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


FIGS = {
    "isd_intro": fig_isd_intro,
    "f01": fig_f01,
    "f02": fig_f02,
    "f03": fig_f03,
    "c04_stages": fig_c04_stages,
    "c04_indices": fig_c04_indices,
    "c05_curves": fig_c05_curves,
    "c05_gap": fig_c05_gap,
}
