# -*- coding: utf-8 -*-
"""Figures for the ANSI/ISA-5.1 reader.

``sheet(page)`` returns the standard 5-tuple for one of the 37 drawing sheets
of Section 6.  Those sheets have no text layer in the PDF — every symbol and
label is a path — so `make_isa51_sheets.py` converts the PDF drawing operators
into a compact standalone SVG (see `pdfvec.py`).  ``fig_tag_numbers()`` is a
clean bilingual redraw of the standard's only numbered figure (Figure 1).
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from vfig import _f, _line, _rect, _txt, svg  # noqa: E402

SHEET_DIR = os.path.join(HERE, "isa51_sheets")

# clause -> (English heading, Vietnamese heading)
SECTIONS = {
    "5.4": ("Table 3 — Function blocks, function designators",
            "Bảng 3 — Khối chức năng, ký hiệu chức năng"),
    "6.2": ("Instrument line symbols", "Ký hiệu đường tín hiệu thiết bị"),
    "6.3": ("General instrument or function symbols",
            "Ký hiệu chung cho thiết bị hoặc chức năng"),
    "6.4": ("Control valve body symbols, damper symbols",
            "Ký hiệu thân van điều khiển và cánh chắn"),
    "6.5": ("Actuator symbols", "Ký hiệu cơ cấu chấp hành"),
    "6.6": ("Symbols for self-actuated regulators, valves, and other devices",
            "Ký hiệu bộ điều chỉnh tự lực, van và thiết bị khác"),
    "6.7": ("Actuator action on failure of actuator power",
            "Trạng thái cơ cấu chấp hành khi mất nguồn"),
    "6.8": ("Primary element symbols", "Ký hiệu phần tử sơ cấp"),
    "6.9": ("Examples — functions", "Ví dụ — các chức năng"),
    "6.10": ("Examples — miscellaneous combinations", "Ví dụ — các tổ hợp khác"),
    "6.11": ("Example — complex combinations", "Ví dụ — tổ hợp phức tạp"),
    "6.12": ("Example — degree of detail", "Ví dụ — mức độ chi tiết"),
}

# standard page -> clause
PAGE_SECTION = {
    23: "5.4", 24: "5.4", 25: "5.4", 26: "5.4",
    28: "6.2",
    29: "6.3", 30: "6.3",
    31: "6.4",
    32: "6.5", 33: "6.5",
    34: "6.6", 35: "6.6", 36: "6.6",
    37: "6.7",
    38: "6.8", 39: "6.8", 40: "6.8", 41: "6.8", 42: "6.8",
    43: "6.8", 44: "6.8", 45: "6.8", 46: "6.8", 47: "6.8",
    48: "6.9", 49: "6.9", 50: "6.9", 51: "6.9", 52: "6.9",
    53: "6.9", 54: "6.9", 55: "6.9",
    56: "6.10", 57: "6.10", 58: "6.10", 59: "6.10", 60: "6.10",
    61: "6.11",
    62: "6.12", 63: "6.12", 64: "6.12",
}

# pages that continue a clause that started on an earlier page
FIRST_PAGE_OF = {
    "5.4": 23,
    "6.2": 28, "6.3": 29, "6.4": 31, "6.5": 32, "6.6": 34,
    "6.7": 37, "6.8": 38, "6.9": 48, "6.10": 56, "6.11": 61,
    "6.12": 62,
}


def sheet(page):
    """Return (svg, caption_vi, caption_en, aria_vi, aria_en) for a sheet."""
    path = os.path.join(SHEET_DIR, "p%d.svg" % page)
    if not os.path.isfile(path):
        raise RuntimeError("missing vector sheet %s — run make_isa51_sheets.py" % path)
    svg_s = open(path, encoding="utf-8").read()
    clause = PAGE_SECTION[page]
    en, vi = SECTIONS[clause]
    cont = page != FIRST_PAGE_OF[clause]
    tail_en = " (continued)" if cont else ""
    tail_vi = " (tiếp theo)" if cont else ""
    cap_vi = "Hình %s · %s%s — tờ %d của tiêu chuẩn." % (clause, vi, tail_vi, page)
    cap_en = "Figure %s · %s%s — standard sheet, page %d." % (clause, en, tail_en, page)
    aria_vi = "Tờ ký hiệu %s: %s%s, trang %d của ANSI/ISA-5.1." % (
        clause, vi, tail_vi, page)
    aria_en = "Symbol sheet %s: %s%s, ANSI/ISA-5.1 page %d." % (
        clause, en, tail_en, page)
    return (svg_s, cap_vi, cap_en, aria_vi, aria_en)


# --------------------------------------------------------------- Figure 1
def fig_tag_numbers():
    """Bilingual redraw of 'Figure 1 — Tag numbers' (clause 4.1)."""
    o = []
    o.append(_rect(12, 12, 556, 246, fill="#fffdf7", stroke="#22303f", sw=1.1))
    o.append(_txt(290, 34, "SỐ THẺ / TAG NUMBER", size=11, weight="bold"))
    o.append(_line(12, 44, 568, 44, sw=0.8, color="#22303f"))

    # left panel: typical tag number
    o.append(_txt(150, 62, "SỐ THẺ ĐIỂN HÌNH / TYPICAL TAG NUMBER",
                  size=9, weight="bold"))
    o.append(_txt(150, 88, "TIC 103", size=19, weight="bold"))
    rows_left = [
        ("T     103", "Nhận dạng thiết bị / Instrument identification"),
        ("103", "Số vòng lặp / Loop number"),
        ("TIC", "Nhận dạng chức năng / Functional identification"),
        ("T", "Chữ cái đầu / First-letter"),
        ("IC", "Các chữ cái tiếp theo / Succeeding-letters"),
    ]
    for i, (code, lab) in enumerate(rows_left):
        y = 108 + i * 22
        o.append(_txt(46, y, code, size=10, anchor="start", weight="bold"))
        o.append(_txt(112, y, lab, size=8, anchor="start"))

    # right panel: expanded tag number
    o.append(_line(290, 56, 290, 246, sw=0.8, color="#22303f"))
    o.append(_txt(430, 62, "SỐ THẺ MỞ RỘNG / EXPANDED TAG NUMBER",
                  size=9, weight="bold"))
    o.append(_txt(430, 88, "10-PAH-5A", size=17, weight="bold"))
    rows_right = [
        ("10-PAH-5A", "Số thẻ / Tag number"),
        ("10", "Tiền tố tùy chọn / Optional prefix"),
        ("PAH", "Nhận dạng chức năng / Functional identification"),
        ("5", "Số vòng lặp / Loop number"),
        ("A", "Hậu tố tùy chọn / Optional suffix"),
    ]
    for i, (code, lab) in enumerate(rows_right):
        y = 108 + i * 22
        o.append(_txt(312, y, code, size=10, anchor="start", weight="bold"))
        o.append(_txt(386, y, lab, size=8, anchor="start"))

    o.append(_line(12, 232, 568, 232, sw=0.8, color="#22303f"))
    o.append(_txt(290, 248, "Dấu gạch nối là tùy chọn / Hyphens are optional as separators",
                  size=8))
    s = svg(580, 264, "".join(o), "Sơ đồ cấu trúc số thẻ theo ANSI/ISA-5.1")
    return (s,
            "Hình 1 · Cấu trúc số thẻ: số thẻ điển hình và số thẻ mở rộng.",
            "Figure 1 · Tag numbers: typical tag number and expanded tag number.",
            "Sơ đồ giải thích các thành phần của số thẻ thiết bị đo.",
            "Diagram explaining the parts of an instrument tag number.")


def fig_sama_blocks():
    """Redraw of the six core SAMA function-block designators (Table 3)."""
    o = []
    o.append(_rect(8, 8, 664, 300, fill="#fffdf7", stroke="#22303f", sw=1.1))
    blocks = [
        ("Σ", "M = X1 + X2 + … + Xn", "Cộng / Summing"),
        ("Σ/n", "M = (X1 + … + Xn)/n", "Trung bình / Averaging"),
        ("Δ", "M = X1 − X2", "Hiệu / Difference"),
        ("K", "M = KX", "Tỷ lệ / Proportional"),
        ("∫", "M = (1/TI) ∫ X dt", "Tích phân / Integral"),
        ("d/dt", "M = TD · dX/dt", "Vi phân / Derivative"),
    ]
    for i, (sym, formula, name) in enumerate(blocks):
        col, row = i % 3, i // 3
        x, y = 20 + col * 216, 22 + row * 140
        o.append(_rect(x, y, 204, 126, fill="#ffffff", stroke="#22303f", sw=0.9))
        o.append(_rect(x + 14, y + 18, 56, 34, fill="#eef3fb",
                       stroke="#22303f", sw=0.8))
        o.append(_txt(x + 42, y + 40, sym, size=14, weight="bold"))
        o.append(_txt(x + 102, y + 36, name, size=8.5, anchor="start"))
        o.append(_line(x + 14, y + 66, x + 190, y + 66, sw=0.6, color="#8899aa"))
        o.append(_txt(x + 102, y + 90, formula, size=10))
        o.append(_txt(x + 102, y + 110, "No. %d" % (i + 1), size=7.5, color="#888"))
    s = svg(680, 316, "".join(o), "Sáu khối chức năng SAMA cơ bản trong Bảng 3")
    return (s,
            "Hình 2 · Sáu khối chức năng cơ bản của Bảng 3 (phương pháp SAMA), được vẽ lại.",
            "Figure 2 · The six basic function blocks of Table 3 (SAMA method), redrawn.",
            "Sáu ô chứa ký hiệu, tên chức năng và biểu thức toán học.",
            "Six panels each holding a designator, a function name and its equation.")


FIGS = {"tag_numbers": fig_tag_numbers, "sama_blocks": fig_sama_blocks}
