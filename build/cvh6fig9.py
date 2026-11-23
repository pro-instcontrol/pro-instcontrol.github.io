# -*- coding: utf-8 -*-
"""Vector figures for Chapter 9 "Standards and Approvals" of Emerson,
*Control Valve Handbook*, 6th ed. (2020), printed pp. 192-209.

Seven faithful vector redrawings ``fig_f9_01`` ... ``fig_f9_07``. Each
function is registered with :func:`_reg` and returns the standard 5-tuple
``(svg, caption_vi, caption_en, aria_vi, aria_en)`` through :func:`_finish`.
All text goes through :func:`T` / :func:`esc` so no bare ampersand can reach
an SVG attribute.

Source quirk: Figures 9.2 and 9.3 carry the *identical* caption "Zones vs.
Equipment Protection Levels" on printed p. 202. Their captions here keep
that source wording visible but add a distinguishing clause and note the
duplication; see ``source_notes`` in the prose module. Several source tables
are OCR-flattened (merged cells, stray X marks, jumbled EPL letters); they
are presented here as legible grids without changing the data.
"""
from cvh6fig import (_reg, _finish, esc, T, _defs, _rect, _line, _circle,
                     _poly, _arrow, svg, INK, GREY, BLUE, RED, GREEN)
# GOLD / FILL / PAPER live in `vfig`, not re-exported by `cvh6fig`.
from vfig import GOLD, FILL, PAPER  # noqa: F401


# ---------------------------------------------------------------------------
# small local helpers for the tabular figures
# ---------------------------------------------------------------------------
def _cell(o, x, y, w, h, text, fill="#ffffff", size=8.0, weight="",
          color=INK, anchor="middle", pad=8.0):
    """One bordered table cell; `text` may be a string or a list of lines."""
    o.append(_rect(x, y, w, h, fill=fill, sw=1.0))
    lines = text if isinstance(text, (list, tuple)) else [text]
    n = len(lines)
    if anchor == "middle":
        tx, anc = x + w / 2.0, "middle"
    else:
        tx, anc = x + pad, "start"
    lh = size + 2.6
    y0 = y + h / 2.0 + size * 0.36 - (n - 1) * lh / 2.0
    for i, ln in enumerate(lines):
        o.append(T(tx, y0 + i * lh, ln, size, weight=weight, color=color,
                   anchor=anc))


def _tbl(o, x, y, widths, row_h, rows, header_rows=1, size=8.0):
    """Simple grid. A row given as a plain string is a full-width section band."""
    xs = [x]
    for wd in widths:
        xs.append(xs[-1] + wd)
    total = sum(widths)
    for ri, row in enumerate(rows):
        yy = y + ri * row_h
        if isinstance(row, str):
            o.append(_rect(x, yy, total, row_h, fill="#e9eef4", sw=1.0))
            o.append(T(x + total / 2.0, yy + row_h / 2.0 + 3, row, size,
                       weight="600"))
            continue
        fill = "#eef3fb" if ri < header_rows else "#ffffff"
        for ci, cell in enumerate(row):
            _cell(o, xs[ci], yy, widths[ci], row_h, cell, fill=fill,
                  size=size, weight="600" if ri < header_rows else "")
    return y + len(rows) * row_h


# ---------------------------------------------------------------------------
# Figure 9.1 - Equipment Groups (printed p. 199)
# ---------------------------------------------------------------------------
@_reg
def fig_f9_01():
    """Figure 9.1 (p. 199) - Equipment groups and their suitable applications."""
    w, h = 680, 400
    o = [_defs()]
    o.append(T(340, 30, "Nhóm thiết bị / Equipment Groups", 9.2, weight="600"))
    o.append(T(340, 49, "Theo Hình 9.1 trong bản in / As printed in Figure 9.1",
               7.4, color=GREY))
    rows = [
        ["Nhóm thiết bị / Group", "Ứng dụng phù hợp / Suitable Applications"],
        "Khí / Gas",
        ["IIC", "IIC, IIB, IIA"],
        ["IIB", "IIB, IIA"],
        ["IIA", "IIA"],
        "Bụi / Dust",
        ["IIC", "IIC, IIB, IIA"],
        ["IIB", "IIB, IIA"],
        ["IIA", "IIA"],
    ]
    _tbl(o, 85, 70, [170, 340], 30, rows, size=8.4)
    o.append(T(340, 362,
               "Thiết bị nhóm cao hơn phù hợp cho ứng dụng nhóm thấp hơn / "
               "A higher-group device suits lower-group applications",
               7.4, color=GREY))
    return _finish(w, h, o,
                   "Figure 9.1 (p. 199) - Equipment Groups",
                   "Hình 9.1 (tr. 199) · Nhóm thiết bị",
                   "Hình 9.1 (tr. 199) · Nhóm thiết bị và các ứng dụng phù hợp cho từng nhóm khí "
                   "và bụi; thiết bị được đánh dấu nhóm cao hơn thì dùng được cho ứng dụng yêu cầu "
                   "nhóm thấp hơn.",
                   "Figure 9.1 (p. 199) · Equipment groups and the applications each gas and dust "
                   "group suits; equipment marked with a higher group is suitable for applications "
                   "requiring a lower group.",
                   "Bảng Hình 9.1 (tr. 199) nhóm thiết bị và ứng dụng phù hợp",
                   "Table of Figure 9.1 (p. 199) equipment groups and suitable applications")


# ---------------------------------------------------------------------------
# Figure 9.2 - Zones vs. EPL, table form (printed p. 202)
# ---------------------------------------------------------------------------
@_reg
def fig_f9_02():
    """Figure 9.2 (p. 202) - Zone numbers mapped to equipment protection levels."""
    w, h = 680, 420
    o = [_defs()]
    o.append(T(340, 30, "Vùng và mức bảo vệ thiết bị / Zones vs. Equipment "
               "Protection Levels", 8.8, weight="600"))
    o.append(T(340, 49, "Bảng ánh xạ mặc định / Default mapping — chú thích gốc "
               "trùng với Hình 9.3", 7.2, color=GREY))
    rows = [
        ["Zone / Vùng", "Equipment Protection Level (EPL)"],
        "Khí / Gas",
        ["0", "Ga"],
        ["1", "Ga or Gb"],
        ["2", "Ga or Gb or Gc"],
        "Bụi / Dust",
        ["20", "Da"],
        ["21", "Da or Db"],
        ["22", "Da or Db or Dc"],
    ]
    _tbl(o, 175, 68, [140, 290], 34, rows, size=8.6)
    return _finish(w, h, o,
                   "Figure 9.2 (p. 202) - Zones vs. Equipment Protection Levels",
                   "Hình 9.2 (tr. 202) · Vùng và mức bảo vệ thiết bị",
                   "Hình 9.2 (tr. 202) · Bảng ánh xạ mặc định giữa các vùng khí và bụi (0, 1, 2, 20, "
                   "21, 22) với mức bảo vệ thiết bị (EPL). Chú thích gốc của hình này trùng với "
                   "chú thích Hình 9.3.",
                   "Figure 9.2 (p. 202) · The default mapping of gas and dust zones (0, 1, 2, 20, 21, "
                   "22) to equipment protection levels (EPL). The source caption is identical to "
                   "the caption of Figure 9.3.",
                   "Bảng Hình 9.2 (tr. 202) vùng và mức bảo vệ thiết bị",
                   "Table of Figure 9.2 (p. 202) zones and equipment protection levels")


# ---------------------------------------------------------------------------
# Figure 9.3 - Zones vs. EPL, graphical form (printed p. 202)
# ---------------------------------------------------------------------------
@_reg
def fig_f9_03():
    """Figure 9.3 (p. 202) - Zone frequency, EPL and protection level matrix."""
    w, h = 680, 410
    o = [_defs()]
    o.append(T(340, 27, "Vùng, EPL và mức bảo vệ / Zones vs. Equipment Protection "
               "Levels", 8.6, weight="600"))
    o.append(T(340, 45, "Dạng sơ đồ · chú thích gốc trùng với Hình 9.2 / "
               "Graphical form · source caption duplicated from Figure 9.2",
               7.2, color=GREY))
    x0, lw, cw = 20, 146, 164
    y = 66
    rh = 46
    _cell(o, x0, y, lw, rh, ["Zone / Vùng", "(khí và bụi)"], fill="#eef3fb",
          size=7.8, weight="600")
    for i, lab in enumerate(["2 · 22", "1 · 21", "0 · 20"]):
        _cell(o, x0 + lw + i * cw, y, cw, rh, lab, fill="#eef3fb",
              size=9.4, weight="600")
    y += rh
    grid = [
        (["Frequency and Duration", "Tần suất và thời gian"],
         ["Low / Thấp", "High / Cao", "Very High / Rất cao"]),
        (["EPL / Mức bảo vệ thiết bị"],
         ["Gc / Dc", "Gb / Db", "Ga / Da"]),
        (["Level of Protection", "Mức bảo vệ"],
         ["Moderate / Trung bình", "High / Cao", "Very High / Rất cao"]),
    ]
    for li, (lab, cells) in enumerate(grid):
        fill = "#ffffff" if li % 2 == 0 else "#f8fafc"
        _cell(o, x0, y, lw, rh, lab, fill=fill, size=7.8, weight="600")
        for i, txt in enumerate(cells):
            _cell(o, x0 + lw + i * cw, y, cw, rh, txt, fill=fill,
                  size=8.0, weight="600" if li == 1 else "",
                  color=BLUE if li == 1 else INK)
        y += rh
    o.append(_rect(x0, 306, lw + 3 * cw, 32, fill="#fdf3e6", sw=1.1, stroke=GOLD))
    o.append(T(x0 + (lw + 3 * cw) / 2.0, 326,
               "Default Risk Levels / Mức rủi ro mặc định: "
               "Unacceptable / Không chấp nhận  →  Acceptable / Chấp nhận",
               7.4))
    o.append(T(340, 360,
               "Các chữ cái EPL trong bản dump bị xáo trộn; ở đây trình bày theo cặp "
               "Gc/Dc, Gb/Db, Ga/Da / EPL letters are cleaned up here",
               7.0, color=GREY))
    return _finish(w, h, o,
                   "Figure 9.3 (p. 202) - Zones vs. Equipment Protection Levels",
                   "Hình 9.3 (tr. 202) · Vùng và mức bảo vệ thiết bị",
                   "Hình 9.3 (tr. 202) · Sơ đồ đối chiếu vùng 2/22, 1/21 và 0/20 theo tần suất và "
                   "thời gian tồn tại của khí quyển nổ với EPL và mức bảo vệ tương ứng. Nguồn dùng "
                   "lại nguyên văn chú thích của Hình 9.2 cho hình này.",
                   "Figure 9.3 (p. 202) · Zones 2/22, 1/21 and 0/20 by frequency and duration of an "
                   "explosive atmosphere mapped to EPL and level of protection. The source reuses "
                   "the Figure 9.2 caption verbatim for this figure.",
                   "Sơ đồ Hình 9.3 (tr. 202) vùng, EPL và mức bảo vệ",
                   "Matrix of Figure 9.3 (p. 202) zones, EPL and protection levels")


# ---------------------------------------------------------------------------
# Figure 9.4 - Temperature Codes (printed p. 203)
# ---------------------------------------------------------------------------
@_reg
def fig_f9_04():
    """Figure 9.4 (p. 203) - T codes and their maximum surface temperatures."""
    w, h = 680, 360
    o = [_defs()]
    o.append(T(340, 30, "Mã nhiệt độ / Temperature Codes", 9.2, weight="600"))
    o.append(T(340, 48, "Nhiệt độ bề mặt tối đa / Maximum surface temperature",
               7.4, color=GREY))
    rows = [
        ["T Code / Mã T", "Maximum Surface Temperature / Nhiệt độ bề mặt tối đa"],
        ["T1", "450°C (842°F)"],
        ["T2", "300°C (572°F)"],
        ["T3", "200°C (392°F)"],
        ["T4", "135°C (275°F)"],
        ["T5", "100°C (212°F)"],
        ["T6", "85°C (185°F)"],
    ]
    _tbl(o, 160, 64, [175, 300], 36, rows, size=8.4)
    return _finish(w, h, o,
                   "Figure 9.4 (p. 203) - Temperature Codes",
                   "Hình 9.4 (tr. 203) · Mã nhiệt độ",
                   "Hình 9.4 (tr. 203) · Mã nhiệt độ T1 đến T6 và nhiệt độ bề mặt tối đa tương ứng, "
                   "từ 450°C cho T1 đến 85°C cho T6.",
                   "Figure 9.4 (p. 203) · Temperature codes T1 through T6 and their maximum surface "
                   "temperatures, from 450°C for T1 down to 85°C for T6.",
                   "Bảng Hình 9.4 (tr. 203) mã nhiệt độ T1 đến T6",
                   "Table of Figure 9.4 (p. 203) temperature codes T1 to T6")


# ---------------------------------------------------------------------------
# Figure 9.5 - IEC Ratings vs. ATEX Ratings (printed p. 204)
# ---------------------------------------------------------------------------
@_reg
def fig_f9_05():
    """Figure 9.5 (p. 204) - IEC 60079 ratings compared with ATEX ratings."""
    w, h = 680, 440
    o = [_defs()]
    o.append(T(340, 27, "Xếp hạng IEC so với ATEX / IEC Ratings vs. ATEX Ratings",
               8.8, weight="600"))
    o.append(T(340, 44, "Per IEC 60079 Series  ·  Directive 2014/34/EU",
               7.4, color=GREY))
    x0 = 16
    widths = [90, 108, 170, 282]
    xs = [x0]
    for wd in widths:
        xs.append(xs[-1] + wd)
    y, rh = 60, 24
    # merged two-level header
    o.append(_rect(xs[0], y, widths[0] + widths[1], rh, fill="#eef3fb", sw=1.0))
    o.append(T((xs[0] + xs[2]) / 2.0, y + 16, "IEC Equipment Ratings", 7.8,
               weight="600"))
    o.append(_rect(xs[2], y, widths[2] + widths[3], rh, fill="#eef3fb", sw=1.0))
    o.append(T((xs[2] + xs[4]) / 2.0, y + 16, "ATEX Equipment Ratings", 7.8,
               weight="600"))
    y += rh
    o.append(_rect(xs[0], y, widths[0] + widths[1], rh, fill="#eef3fb", sw=1.0))
    o.append(T((xs[0] + xs[2]) / 2.0, y + 16, "Per IEC 60079 Series", 7.6))
    o.append(_rect(xs[2], y, widths[2] + widths[3], rh, fill="#eef3fb", sw=1.0))
    o.append(T((xs[2] + xs[4]) / 2.0, y + 16, "Directive 2014/34/EU", 7.6))
    y += rh
    for ci, lab in enumerate(["EPL", "Group", "Equipment Group",
                              "Equipment Category & Environment"]):
        _cell(o, xs[ci], y, widths[ci], rh, lab, fill="#f4f7fb", size=7.4,
              weight="600")
    y += rh
    body = [
        "Mines / Hầm lò",
        ["Ma", "I", "I", "M1"],
        ["Mb", "I", "I", "M2"],
        "Gas / Khí",
        ["Ga", "II", "II", "1G"],
        ["Gb", "II", "II", "2G"],
        ["Gc", "II", "II", "3G"],
        "Dust / Bụi",
        ["Da", "III", "II", "1D"],
        ["Db", "III", "II", "2D"],
        ["Dc", "III", "II", "3D"],
    ]
    for row in body:
        if isinstance(row, str):
            o.append(_rect(x0, y, sum(widths), rh, fill="#e9eef4", sw=1.0))
            o.append(T(x0 + 10, y + 16, row, 7.6, weight="600", anchor="start"))
        else:
            for ci, val in enumerate(row):
                _cell(o, xs[ci], y, widths[ci], rh, val, size=8.2,
                      weight="600" if ci == 0 else "")
        y += rh
    o.append(T(340, 402,
               "Các ô nhóm lặp lại được gộp trong bản dump; ở đây mở rộng thành từng ô / "
               "Repeated group cells are expanded here", 7.0, color=GREY))
    return _finish(w, h, o,
                   "Figure 9.5 (p. 204) - IEC Ratings vs. ATEX Ratings",
                   "Hình 9.5 (tr. 204) · Xếp hạng IEC so với ATEX",
                   "Hình 9.5 (tr. 204) · Đối chiếu EPL và nhóm thiết bị theo IEC 60079 với nhóm, "
                   "category và môi trường theo Chỉ thị ATEX 2014/34/EU, cho hầm lò, khí và bụi.",
                   "Figure 9.5 (p. 204) · EPL and equipment groups per IEC 60079 compared with "
                   "equipment group, category and environment under Directive 2014/34/EU, for "
                   "mines, gas and dust.",
                   "Bảng Hình 9.5 (tr. 204) xếp hạng IEC và ATEX",
                   "Table of Figure 9.5 (p. 204) IEC and ATEX equipment ratings")


# ---------------------------------------------------------------------------
# Figure 9.6 - Explanation of Enclosure Ratings (printed p. 209)
# ---------------------------------------------------------------------------
@_reg
def fig_f9_06():
    """Figure 9.6 (p. 209) - NEMA 250 enclosure type ratings by test condition."""
    w, h = 680, 430
    o = [_defs()]
    o.append(T(340, 28, "Giải thích xếp hạng vỏ bọc / Explanation of Enclosure "
               "Ratings", 8.8, weight="600"))
    o.append(T(340, 46, "NEMA 250 · dấu X = đạt điều kiện thử / X = rated for "
               "that condition", 7.4, color=GREY))
    types = ["3", "3X", "3R", "3RX", "3S", "3SX", "4", "4X"]
    x0, lw, cw = 30, 226, 47
    y, hh = 58, 28
    _cell(o, x0, y, lw, hh, "Điều kiện thử / Test condition", fill="#eef3fb",
          size=7.8, weight="600", anchor="start")
    for i, t in enumerate(types):
        _cell(o, x0 + lw + i * cw, y, cw, hh, t, fill="#eef3fb", size=8.2,
              weight="600")
    y += hh
    rows = [
        ("cond", ["General / Access to hazardous parts (5.2)"], [1] * 8),
        ("sec", "Ingress of Solid Foreign Objects / Xâm nhập vật lạ rắn", None),
        ("cond", ["Falling dirt (5.5.2)"], [1] * 8),
        ("cond", ["Windblown dust, lint fibers (5.5.1)"],
         [1, 1, 0, 0, 1, 1, 1, 1]),
        ("sec", "Ingress of Water / Xâm nhập nước", None),
        ("cond", ["Dripping and light splashing (5.3)"], [1] * 8),
        ("cond", ["Rain, snow, sleet, ice* (5.4)"], [1] * 8),
        ("cond", ["Rain, snow, sleet, ice** (5.6)"], [0, 0, 0, 0, 1, 1, 0, 0]),
        ("cond", ["Hose-directed and splashing water (5.7)"],
         [0, 0, 0, 0, 0, 0, 1, 1]),
        ("sec", "Additional Protection / Bảo vệ bổ sung", None),
        ("cond", ["Corrosion (5.9 & 5.10)"], [0, 1, 0, 1, 0, 1, 0, 1]),
    ]
    for kind, label, flags in rows:
        if kind == "sec":
            rh = 20
            o.append(_rect(x0, y, lw + 8 * cw, rh, fill="#e9eef4", sw=1.0))
            o.append(T(x0 + 8, y + 15, label, 7.6, weight="600", anchor="start"))
        else:
            rh = 30
            _cell(o, x0, y, lw, rh, label, size=7.4, anchor="start")
            for i, flag in enumerate(flags):
                _cell(o, x0 + lw + i * cw, y, cw, rh, "X" if flag else "",
                      size=9.2, weight="600", color=GREEN if flag else GREY)
        y += rh
    o.append(T(30, 374,
               "* External operating mechanisms are not required to be operable when the "
               "enclosure is ice covered.", 6.8, anchor="start", color=GREY))
    o.append(T(30, 390,
               "** External operating mechanisms are operable when the enclosure is ice "
               "covered.", 6.8, anchor="start", color=GREY))
    return _finish(w, h, o,
                   "Figure 9.6 (p. 209) - Explanation of Enclosure Ratings",
                   "Hình 9.6 (tr. 209) · Giải thích xếp hạng vỏ bọc",
                   "Hình 9.6 (tr. 209) · Bảng đối chiếu các loại vỏ bọc NEMA 250 từ Type 3 đến "
                   "Type 4X với các điều kiện thử về bụi, nước, băng giá và ăn mòn.",
                   "Figure 9.6 (p. 209) · NEMA 250 enclosure types 3 through 4X compared with the "
                   "test conditions for dust, water, ice and corrosion.",
                   "Bảng Hình 9.6 (tr. 209) xếp hạng vỏ bọc NEMA",
                   "Matrix of Figure 9.6 (p. 209) NEMA enclosure ratings")


# ---------------------------------------------------------------------------
# Figure 9.7 - Description of Ingress Protection Numerals (printed p. 209)
# ---------------------------------------------------------------------------
@_reg
def fig_f9_07():
    """Figure 9.7 (p. 209) - Meaning of the two IP code numerals."""
    w, h = 680, 420
    o = [_defs()]
    o.append(T(340, 28, "Mô tả chữ số bảo vệ xâm nhập / Description of Ingress "
               "Protection Numerals", 8.6, weight="600"))
    o.append(T(340, 46, "Mã IP gồm IP + hai chữ số đặc trưng / IP code = IP + "
               "two characteristic numerals", 7.2, color=GREY))
    lx, rx, cwid = 36, 352, 292
    hy, hhh = 62, 38
    _cell(o, lx, hy, cwid, hhh,
          ["First Numeral / Chữ số thứ nhất",
           "Protection Against Solid Bodies / Chống vật rắn"],
          fill="#eef3fb", size=7.8, weight="600")
    _cell(o, rx, hy, cwid, hhh,
          ["Second Numeral / Chữ số thứ hai",
           "Protection Against Liquid / Chống chất lỏng"],
          fill="#eef3fb", size=7.8, weight="600")
    left = [
        "0 - No protection",
        "1 - Objects greater than 50 mm",
        "2 - Objects greater than 12.5 mm",
        "3 - Objects greater than 2.5 mm",
        "4 - Objects greater than 1.0 mm",
        "5 - Dust-protected",
        "6 - Dust-tight",
    ]
    right = [
        "0 - No protection",
        "1 - Vertically dripping water",
        "2 - Angled dripping water (75 to 90 degrees)",
        "3 - Sprayed water",
        "4 - Splashed water",
        "5 - Jetting",
        "6 - Powerful jetting",
        "7 - Temporary immersion",
        "8 - Permanent immersion",
        "9 - High-pressure and temperature water jet",
    ]
    y, rh = 100, 28
    for i in range(10):
        lfill = "#ffffff" if i % 2 == 0 else "#f8fafc"
        rfill = "#f8fafc" if i % 2 == 0 else "#ffffff"
        _cell(o, lx, y, cwid, rh, left[i] if i < len(left) else "",
              fill=lfill, size=7.6, anchor="start")
        _cell(o, rx, y, cwid, rh, right[i], fill=rfill, size=7.6,
              anchor="start")
        y += rh
    return _finish(w, h, o,
                   "Figure 9.7 (p. 209) - Description of Ingress Protection Numerals",
                   "Hình 9.7 (tr. 209) · Chữ số bảo vệ xâm nhập",
                   "Hình 9.7 (tr. 209) · Ý nghĩa của hai chữ số trong mã IP: chữ số thứ nhất "
                   "chống vật rắn và tiếp xúc, chữ số thứ hai chống sự xâm nhập của nước.",
                   "Figure 9.7 (p. 209) · Meaning of the two numerals in an IP code: the first "
                   "against solid bodies and contact, the second against the ingress of water.",
                   "Bảng Hình 9.7 (tr. 209) ý nghĩa chữ số mã IP",
                   "Table of Figure 9.7 (p. 209) ingress protection numerals")
