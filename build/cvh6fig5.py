# -*- coding: utf-8 -*-
"""Vector figures for Chapter 5 "Control Valve Sizing" of Emerson,
*Control Valve Handbook*, 6th ed. (2020), printed pp. 108-136.

Eighteen simplified but faithful figures ``fig_f5_01`` ... ``fig_f5_18``.
Every function is registered with :func:`_reg` and returns the standard
5-tuple ``(svg, caption_vi, caption_en, aria_vi, aria_en)`` through
:func:`_finish`.  All text is XML-escaped with :func:`T` / :func:`esc`.
"""
import math

from cvh6fig import (_reg, _finish, _leader, _labels, _c4_labels, esc, T,
                     _defs, _rect, _line, _circle, _ellipse, _poly, _path,
                     _arrow, _spring, _num, svg, INK, GREY, BLUE, RED, GREEN,
                     _axes, _curve)
# GOLD / FILL / PAPER are part of the shared palette but live in `vfig`,
# not in `cvh6fig` (verified by import); import them from their real home.
from vfig import GOLD, FILL, PAPER  # noqa: F401


# ---------------------------------------------------------------------------
# small local helpers
# ---------------------------------------------------------------------------
def _trow(o, x, y, widths, cells, rh, fs=7.3, fill="#f7f9fb"):
    """One table row.  ``cells`` is ``[(text, anchor), ...]``; text may
    contain a newline for a second line."""
    o.append(_rect(x, y, sum(widths), rh, fill=fill, sw=1.0))
    cx = x
    for wd, (txt, al) in zip(widths, cells):
        lines = str(txt).split("\n")
        cy = y + rh / 2.0 - (len(lines) - 1) * (fs + 1) / 2.0 + fs * 0.35
        for ln in lines:
            tx = cx + 4 if al == "start" else (cx + wd - 4 if al == "end"
                                               else cx + wd / 2.0)
            o.append(T(tx, cy, ln, fs, anchor=al))
            cy += fs + 1
        cx += wd


def _table(o, x, y, widths, headers, rows, rh=21, hh=30, fs=7.3):
    """A light bilingual table with alternating row fills."""
    _trow(o, x, y, widths, [(h, "middle") for h in headers], hh,
          fs=fs, fill="#e9eef4")
    for i, row in enumerate(rows):
        _trow(o, x, y + hh + i * rh, widths, row, rh, fs=fs,
              fill="#fdfcf9" if i % 2 == 0 else "#f2f6fa")
    cx = x
    for wd in widths[:-1]:
        cx += wd
        o.append(_line(cx, y, cx, y + hh + len(rows) * rh, sw=0.7, color=GREY))


def _chart_axes(o, x, y, W, H, xr, yr, xlab, ylab, xt, yt, fs=7.0):
    """Manual axes with real-value ticks ``[(value, label), ...]``.
    Returns the two mapping functions ``px, py``."""
    def px(v):
        return x + (v - xr[0]) / (xr[1] - xr[0]) * W

    def py(v):
        return y + H - (v - yr[0]) / (yr[1] - yr[0]) * H

    o.append(_line(x, y + H, x + W, y + H, sw=1.2, color=INK))
    o.append(_line(x, y, x, y + H, sw=1.2, color=INK))
    o.append(T(x + W / 2.0, y + H + 32, xlab, 7.4, color=INK))
    o.append(T(x - 4, y - 12, ylab, 7.4, color=INK, anchor="start"))
    for v, lab in xt:
        o.append(_line(px(v), y + H, px(v), y + H + 3, sw=0.8))
        o.append(T(px(v), y + H + 13, lab, fs, color=GREY))
    for v, lab in yt:
        o.append(_line(x - 3, py(v), x, py(v), sw=0.8))
        o.append(T(x - 5, py(v) + 2.4, lab, fs, color=GREY, anchor="end"))
    return px, py


# ---------------------------------------------------------------------------
# Chapter 5 figures
# ---------------------------------------------------------------------------
@_reg
def fig_f5_01():
    """Figure 5.1 (p. 108) - Inherent flow characteristic curves."""
    w, h = 640, 380
    o = [_defs()]
    x0, y0, W, H = 88, 62, 372, 236
    _chart_axes(o, x0, y0, W, H, (0, 1), (0, 1),
                "Hành trình định mức (%) / Rated travel (%)",
                "Hệ số dòng định mức (%) / Rated flow coefficient (%)",
                [(0, "0"), (0.5, "50"), (1, "100")],
                [(0, "0"), (0.5, "50"), (1, "100")], fs=7.0)
    o.append(_curve(lambda t: t, x0, y0, W, H, sw=1.9, color=BLUE))
    o.append(_curve(lambda t: (math.exp(2.6 * t) - 1.0) / (math.exp(2.6) - 1.0),
                    x0, y0, W, H, sw=1.9, color=GREEN))
    o.append(_curve(lambda t: t ** 0.34, x0, y0, W, H, sw=1.9, color=RED))
    for yy, col, lab in [(104, BLUE, "Tuyến tính / Linear"),
                         (136, GREEN, "Phần trăm bằng / Equal-percentage"),
                         (168, RED, "Mở nhanh / Quick-opening")]:
        o.append(_line(474, yy, 488, yy, sw=2.2, color=col))
        o.append(T(494, yy + 3, lab, 6.6, anchor="start"))
    o.append(T(300, 354,
               "Đường đặc tính vốn có, chênh áp không đổi / Inherent curves at constant differential pressure",
               7.0, color=GREY))
    return _finish(w, h, o,
                   "Figure 5.1 - Inherent flow characteristic curves",
                   "Hình 5.1 (tr. 108) · Đường đặc tính dòng vốn có",
                   "Hình 5.1 (tr. 108) · Ba đường đặc tính dòng vốn có: tuyến tính, phần trăm bằng "
                   "và mở nhanh, cho thấy quan hệ giữa lưu lượng và hành trình khi chênh áp qua "
                   "van không đổi.",
                   "Figure 5.1 (p. 108) · Three inherent flow characteristic curves - linear, "
                   "equal-percentage and quick-opening - relating flow rate to valve travel at "
                   "constant differential pressure.",
                   "Biểu đồ ba đường đặc tính dòng vốn có theo hành trình van",
                   "Chart of three inherent flow characteristic curves versus valve travel")


@_reg
def fig_f5_02():
    """Figure 5.2 (p. 123) - Typical unbalance areas of control valves."""
    w, h = 640, 400
    o = [_defs()]
    widths = [112, 232, 216]
    headers = ["Cổng (in) / Port (in)",
               "Van một chỗ, không cân bằng (in2)\nUnbalanced, single-seat (in2)",
               "Van cân bằng (in2)\nBalanced (in2)"]
    data = [("1/4", "0.028", "-"), ("3/8", "0.110", "-"),
            ("1/2", "0.196", "-"), ("3/4", "0.441", "-"),
            ("1", "0.785", "-"), ("1-5/16", "1.35", "0.04"),
            ("1-7/8", "2.76", "0.062"), ("2-5/16", "4.20", "0.27"),
            ("3-7/16", "9.28", "0.118"), ("4-3/8", "15.03", "0.154"),
            ("7", "38.48", "0.81"), ("8", "50.24", "0.86")]
    rows = [[(a, "middle"), (b, "middle"), (c, "middle")] for a, b, c in data]
    _table(o, 36, 52, widths, headers, rows, rh=19, hh=34, fs=7.0)
    o.append(T(320, 352,
               "Diện tích cổng là diện tích mất cân bằng điển hình của van một chỗ / "
               "Port area is the typical unbalance area of a single-seat valve",
               7.0, color=GREY))
    return _finish(w, h, o,
                   "Figure 5.2 - Typical unbalance areas of control valves",
                   "Hình 5.2 (tr. 123) · Diện tích mất cân bằng điển hình của van",
                   "Hình 5.2 (tr. 123) · Bảng diện tích mất cân bằng theo đường kính cổng cho van "
                   "một chỗ không cân bằng và van cân bằng; diện tích cổng được dùng làm diện tích "
                   "mất cân bằng khi tính lực áp suất.",
                   "Figure 5.2 (p. 123) · Table of typical unbalance areas by port diameter for "
                   "single-seat unbalanced and balanced valves; the port area is used as the "
                   "unbalance area when estimating pressure unbalance force.",
                   "Bảng diện tích mất cân bằng theo đường kính cổng van",
                   "Table of valve unbalance area versus port diameter")


@_reg
def fig_f5_03():
    """Figure 5.3 (p. 124) - Minimum required seat load, classes II-V."""
    w, h = 640, 400
    o = [_defs()]
    x, y, W, H = 88, 62, 386, 246
    px, py = _chart_axes(
        o, x, y, W, H, (1000, 6000), (0, 1000),
        "Tải chỗ ngồi yêu cầu (lb/in chu vi) / Required seat load (lb per lineal inch)",
        "Chênh áp đóng (psi) / Shutoff pressure drop (psi)",
        [(1000, "1000"), (2000, "2000"), (3000, "3000"), (4000, "4000"),
         (5000, "5000"), (6000, "6000")],
        [(0, "0"), (200, "200"), (400, "400"), (600, "600"), (800, "800"),
         (1000, "1000")], fs=6.4)
    curves = [(BLUE, 1300, 0.42, "Class II"),
              (GREEN, 2000, 0.50, "Class III"),
              (RED, 2750, 0.56, "Class IV"),
              (GOLD, 3500, 0.62, "Class V (metal seat)"),
              ("#7d3c98", 4200, 0.66, "Class V (C-Seal)")]
    for col, base, slope, _ in curves:
        pts = [(px(1000 + t * 5000), py(base + slope * t))
               for t in (i / 24.0 for i in range(25))]
        o.append(_poly(pts, sw=1.8, color=col))
    o.append(T(x + W / 2.0, 68,
               "Quan hệ minh họa / Illustrative relationships", 7.2, color=GREY))
    for i, (col, _, _, lab) in enumerate(curves):
        yy = 108 + i * 22
        o.append(_line(496, yy, 510, yy, sw=2.0, color=col))
        o.append(T(516, yy + 3, lab, 7.1, anchor="start"))
    o.append(T(300, 366,
               "Tham khảo dữ liệu nhà sản xuất để có giá trị thiết kế / "
               "Consult manufacturer data for design values", 7.0, color=GREY))
    return _finish(w, h, o,
                   "Figure 5.3 - Minimum required seat load for improved seat life",
                   "Hình 5.3 (tr. 124) · Tải chỗ ngồi tối thiểu để tăng tuổi thọ",
                   "Hình 5.3 (tr. 124) · Các đường quan hệ minh họa giữa chênh áp đóng và tải chỗ "
                   "ngồi yêu cầu cho van đế kim loại các cấp II đến V; tải tăng dần theo cấp rò "
                   "rỉ nghiêm ngặt hơn.",
                   "Figure 5.3 (p. 124) · Illustrative curves relating shutoff pressure drop to "
                   "required seat load for metal-seated valves in leak classes II through V; the "
                   "required load rises with stricter leak class.",
                   "Biểu đồ tải chỗ ngồi tối thiểu theo chênh áp đóng cho các cấp rò rỉ",
                   "Chart of minimum required seat load versus shutoff pressure drop by leak class")


@_reg
def fig_f5_04():
    """Figure 5.4 (p. 124) - Recommended seat load table."""
    w, h = 640, 380
    o = [_defs()]
    widths = [104, 466]
    headers = ["Cấp rò rỉ / Leak class",
               "Tải chỗ ngồi khuyến nghị / Recommended seat load"]
    rows = [
        [(u"Class I", "middle"),
         ("Theo yêu cầu người dùng, không thử rò tại nhà máy\n"
          "As required by user specification, no factory leak test", "start")],
        [(u"Class II", "middle"),
         ("20 lb trên mỗi inch chu vi cổng / 20 lb per lineal inch of port circumference", "start")],
        [(u"Class III", "middle"),
         ("40 lb trên mỗi inch chu vi cổng / 40 lb per lineal inch of port circumference", "start")],
        [(u"Class IV", "middle"),
         ("40 lb/in cho cổng đến 4-3/8 in; 80 lb/in cho cổng lớn hơn\n"
          "40 lb/in up to 4-3/8 in port; 80 lb/in for larger ports", "start")],
        [(u"Class V", "middle"),
         ("Xác định từ Hình 5.2 / Determine from Figure 5.2", "start")],
        [(u"Class VI", "middle"),
         ("300 lb trên mỗi inch chu vi cổng / 300 lb per lineal inch of port circumference", "start")],
    ]
    _table(o, 35, 52, widths, headers, rows, rh=36, hh=30, fs=7.1)
    o.append(T(320, 338,
               "Tải chỗ ngồi: pound trên mỗi inch chu vi cổng / "
               "Seat load: pounds per lineal inch of port circumference",
               7.0, color=GREY))
    return _finish(w, h, o,
                   "Figure 5.4 - Recommended seat load",
                   "Hình 5.4 (tr. 124) · Tải chỗ ngồi khuyến nghị theo cấp rò rỉ",
                   "Hình 5.4 (tr. 124) · Bảng tải chỗ ngồi khuyến nghị cho các cấp rò rỉ I đến VI, "
                   "tính bằng pound trên mỗi inch chu vi cổng, từ không yêu cầu thử đến 300 lb/in.",
                   "Figure 5.4 (p. 124) · Table of recommended seat load for leak classes I "
                   "through VI, expressed in pounds per lineal inch of port circumference, from "
                   "no factory test required to 300 lb per inch.",
                   "Bảng tải chỗ ngồi khuyến nghị cho các cấp rò rỉ I đến VI",
                   "Table of recommended seat load for leak classes I through VI")


@_reg
def fig_f5_05():
    """Figure 5.5 (p. 125) - Typical packing friction values."""
    w, h = 640, 400
    o = [_defs()]
    x, y, W, H = 92, 62, 380, 226
    px, py = _chart_axes(
        o, x, y, W, H, (0, 4.4), (0, 450),
        "Kích thước thân / cấp áp lực / Stem size, pressure class",
        "Lực ma sát (lb) / Friction force (lb)",
        [(0.6, "5/16"), (1.6, "3/8 (125)"), (2.6, "1/2 (125)"),
         (3.6, "1/2 (300)")],
        [(0, "0"), (100, "100"), (200, "200"), (300, "300"), (400, "400")],
        fs=6.8)
    groups = [(0.6, 20, 30), (1.6, 38, 56), (2.6, 50, 75), (3.6, 230, None)]
    for gx, single, double in groups:
        o.append(_rect(px(gx) - 28, py(single), 20, y + H - py(single),
                       fill="#dbe7f3", sw=1.1, stroke=BLUE))
        if double is not None:
            o.append(_rect(px(gx) - 2, py(double), 20, y + H - py(double),
                           fill="#dcefe2", sw=1.1, stroke=GREEN))
    o.append(_rect(486, 100, 14, 10, fill="#dbe7f3", sw=1.1, stroke=BLUE))
    o.append(T(505, 109, "PTFE đơn / single", 7.4, anchor="start"))
    o.append(_rect(486, 130, 14, 10, fill="#dcefe2", sw=1.1, stroke=GREEN))
    o.append(T(505, 139, "PTFE đôi / double", 7.4, anchor="start"))
    o.append(T(320, 356,
               "Giá trị điển hình; tham khảo dữ liệu nhà sản xuất / "
               "Indicative values; consult manufacturer data", 7.0, color=GREY))
    return _finish(w, h, o,
                   "Figure 5.5 - Typical packing friction values",
                   "Hình 5.5 (tr. 125) · Giá trị ma sát đệm điển hình",
                   "Hình 5.5 (tr. 125) · Biểu đồ cột so sánh lực ma sát đệm PTFE đơn và đôi theo "
                   "kích thước thân và cấp áp lực; giá trị chỉ mang tính điển hình, cần tham khảo "
                   "dữ liệu nhà sản xuất.",
                   "Figure 5.5 (p. 125) · Bar comparison of typical single and double PTFE packing "
                   "friction by stem size and pressure class; values are indicative and "
                   "manufacturer data should be consulted.",
                   "Biểu đồ cột lực ma sát đệm PTFE đơn và đôi",
                   "Bar chart of single and double PTFE packing friction")


@_reg
def fig_f5_06():
    """Figure 5.6 (p. 128) - Vena contracta illustration."""
    w, h = 640, 350
    o = [_defs()]
    o.append(_line(60, 130, 600, 130, sw=2.0, color=INK))
    o.append(_line(60, 230, 600, 230, sw=2.0, color=INK))
    o.append(_poly([(270, 130), (330, 130), (300, 168)],
                   fill="#dfe7ef", sw=1.4, close=True))
    o.append(_poly([(270, 230), (330, 230), (300, 192)],
                   fill="#dfe7ef", sw=1.4, close=True))
    o.append(_path("M 80 150 C 230 150 300 152 355 172 C 420 190 500 180 580 180",
                   sw=1.0, dash="4 3", color=BLUE))
    o.append(_path("M 80 180 C 230 180 300 180 355 180 C 430 180 500 180 580 180",
                   sw=1.0, dash="4 3", color=BLUE))
    o.append(_path("M 80 210 C 230 210 300 208 355 188 C 420 172 500 180 580 180",
                   sw=1.0, dash="4 3", color=BLUE))
    o.append(_arrow(80, 180, 150, 180, sw=1.8, color=GREEN))
    o.append(_arrow(520, 180, 590, 180, sw=1.8, color=GREEN))
    o.append(T(96, 116, "P1", 8.4, color=INK, weight="600"))
    o.append(T(572, 116, "P2", 8.4, color=INK, weight="600"))
    o.append(T(150, 258, "Dòng chảy / Flow", 7.8, color=GREEN))
    o.append(_leader(355, 172, 430, 76))
    o.append(T(434, 72, "Vena contracta", 7.8, anchor="start"))
    o.append(_leader(292, 148, 210, 76))
    o.append(T(206, 72, "Hạn chế / Restriction", 7.8, anchor="end"))
    o.append(T(320, 310,
               "Vận tốc lớn nhất và áp suất thấp nhất tại vena contracta / "
               "Highest velocity and lowest pressure occur at the vena contracta",
               7.0, color=GREY))
    return _finish(w, h, o,
                   "Figure 5.6 - Vena contracta illustration",
                   "Hình 5.6 (tr. 128) · Minh họa chỗ co hẹp dòng vena contracta",
                   "Hình 5.6 (tr. 128) · Sơ đồ dòng chất lỏng qua một hạn chế: dòng co hẹp ngay sau "
                   "hạn chế tại vena contracta, nơi vận tốc lớn nhất và áp suất thấp nhất, rồi "
                   "giãn ra về phía hạ lưu.",
                   "Figure 5.6 (p. 128) · Flow through a restriction: the stream contracts just "
                   "downstream at the vena contracta, where velocity is highest and pressure "
                   "lowest, then expands downstream.",
                   "Sơ đồ dòng chảy qua hạn chế và vị trí vena contracta",
                   "Schematic of flow through a restriction and the vena contracta")


@_reg
def fig_f5_07():
    """Figure 5.7 (p. 128) - Pressure profiles, high- and low-recovery."""
    w, h = 660, 440
    o = [_defs()]
    panels = [(56, "Van phục hồi cao (van bi) / High-recovery valve (ball)",
               BLUE, 74, 92),
              (238, "Van phục hồi thấp / Low-recovery valve",
               RED, 94, 112)]
    for pt, title, col, rec_y, dip_y in panels:
        o.append(T(64, pt - 10, title, 8.0, anchor="start", weight="600"))
        o.append(_line(64, pt + 6, 602, pt + 6, sw=1.5, color=INK))
        o.append(_line(64, pt + 46, 602, pt + 46, sw=1.5, color=INK))
        o.append(_rect(298, pt + 6, 14, 20, fill="#dfe7ef", sw=1.2))
        o.append(_rect(298, pt + 28, 14, 18, fill="#dfe7ef", sw=1.2))
        o.append(_arrow(80, pt + 26, 160, pt + 26, sw=1.6, color=GREEN))
        prof = [(64, pt + 60), (280, pt + 60), (300, pt + 68),
                (330, pt + dip_y), (352, pt + dip_y + 4), (396, pt + rec_y + 18),
                (470, pt + rec_y + 4), (602, pt + rec_y)]
        o.append(_poly(prof, sw=2.0, color=col))
        o.append(T(74, pt + 55, "P1", 7.6, anchor="start"))
        o.append(T(594, pt + rec_y - 8, "P2", 7.6, anchor="end"))
        o.append(T(350, pt + dip_y - 9, "Pvc", 7.6, color=col))
        o.append(_line(64, pt + 128, 602, pt + 128, sw=0.7, dash="3 3", color=GREY))
    o.append(T(330, 416,
               "Phục hồi càng cao, P2 càng gần P1 / Higher recovery brings P2 closer to P1",
               7.0, color=GREY))
    return _finish(w, h, o,
                   "Figure 5.7 - Pressure profiles for high- and low-recovery valves",
                   "Hình 5.7 (tr. 128) · So sánh đường áp suất van phục hồi cao và thấp",
                   "Hình 5.7 (tr. 128) · So sánh đường áp suất minh họa: van phục hồi cao giảm áp "
                   "sâu tại vena contracta rồi phục hồi gần áp suất đầu vào, trong khi van phục "
                   "hồi thấp phục hồi kém hơn do tổn thất rối mạnh hơn.",
                   "Figure 5.7 (p. 128) · Illustrative pressure profiles: a high-recovery valve "
                   "drops to a low vena-contracta pressure then recovers close to inlet pressure, "
                   "while a low-recovery valve recovers less because of greater turbulent "
                   "dissipation.",
                   "Hai đường áp suất so sánh van phục hồi cao và thấp",
                   "Two pressure profiles comparing high- and low-recovery valves")


@_reg
def fig_f5_08():
    """Figure 5.8 (p. 129) - Typical appearance of flashing damage."""
    w, h = 620, 360
    o = [_defs()]
    o.append(_rect(70, 90, 480, 190, fill="#eef2f5", sw=1.8))
    o.append(_rect(96, 112, 428, 146, fill="#f8fafb", sw=1.1))
    for yy in (140, 168, 196, 224):
        o.append(_path("M 118 %d C 230 %d 360 %d 500 %d"
                       % (yy, yy - 7, yy + 7, yy - 2),
                       sw=3.2, color="#b9c6d1"))
        o.append(_path("M 128 %d C 240 %d 350 %d 492 %d"
                       % (yy + 4, yy - 3, yy + 9, yy + 2),
                       sw=1.0, color="#ffffff"))
    for cx, cy in [(430, 132), (452, 148), (470, 130), (444, 172), (486, 160)]:
        o.append(_circle(cx, cy, 4, fill="none", sw=1.0, color=BLUE))
    o.append(_leader(250, 168, 250, 60))
    o.append(T(250, 56, "Bề mặt mòn nhẵn, bóng / Smooth, polished eroded surface",
               7.8, anchor="middle"))
    o.append(_leader(452, 148, 540, 314))
    o.append(T(600, 318, "Bọt hơi cuốn theo dòng / Vapor bubbles downstream",
               7.0, anchor="end"))
    o.append(T(310, 334,
               "Hư hỏng do flashing: vùng xói mòn nhẵn gần đường đế của nút và vòng chỗ ngồi / "
               "Flashing damage: smooth erosion near the plug seat line",
               7.0, color=GREY))
    return _finish(w, h, o,
                   "Figure 5.8 - Typical appearance of flashing damage",
                   "Hình 5.8 (tr. 129) · Dạng hư hỏng do flashing: bề mặt mòn nhẵn",
                   "Hình 5.8 (tr. 129) · Sơ đồ bề mặt bị flashing xói mòn: vùng mòn nhẵn, bóng do "
                   "các giọt lỏng va đập ở tốc độ cao gần đường đế của nút và vòng chỗ ngồi.",
                   "Figure 5.8 (p. 129) · Vector schematic of flashing damage: a smooth, polished "
                   "eroded surface caused by high-velocity liquid droplet impingement near the "
                   "plug seat line.",
                   "Sơ đồ bề mặt mòn nhẵn bóng do flashing",
                   "Schematic of smooth polished surface from flashing erosion")


@_reg
def fig_f5_09():
    """Figure 5.9 (p. 130) - Typical appearance of cavitation damage."""
    w, h = 620, 360
    o = [_defs()]
    o.append(_rect(70, 90, 480, 190, fill="#efe7e0", sw=1.8))
    o.append(_rect(96, 112, 428, 146, fill="#f8f3ee", sw=1.1))
    pits = [(132, 132), (160, 150), (146, 176), (182, 128), (198, 166),
            (224, 142), (240, 184), (266, 124), (282, 158), (304, 138),
            (322, 182), (348, 150), (366, 174), (392, 126), (408, 160),
            (430, 140), (452, 180), (474, 152), (496, 130), (506, 172)]
    for i, (cx, cy) in enumerate(pits):
        r = 5 if i % 3 else 8
        o.append(_circle(cx, cy, r, fill="#c9bdb0", sw=1.0, color="#8a7b6d"))
        o.append(_circle(cx - 1, cy - 1, max(1.5, r - 3), fill="#6f6257", sw=0))
    for cx, cy in [(350, 210), (380, 214), (410, 208)]:
        o.append(_circle(cx, cy, 5, fill="none", sw=1.0, color=BLUE))
        o.append(_line(cx - 7, cy - 7, cx - 3, cy - 3, sw=0.9, color=BLUE))
        o.append(_line(cx + 3, cy - 7, cx + 7, cy - 3, sw=0.9, color=BLUE))
    o.append(_leader(250, 168, 250, 60))
    o.append(T(250, 56, "Bề mặt sần xốp như tro / Rough, cinder-like pitted surface",
               7.8, anchor="middle"))
    o.append(_leader(380, 214, 540, 314))
    o.append(T(600, 318, "Bọt hơi vỡ / Collapsing vapor bubbles",
               7.0, anchor="end"))
    o.append(T(310, 334,
               "Cavitation để lại bề mặt sần, khác với flashing nhẵn bóng / "
               "Cavitation is rough, unlike smooth flashing",
               7.0, color=GREY))
    return _finish(w, h, o,
                   "Figure 5.9 - Typical appearance of cavitation damage",
                   "Hình 5.9 (tr. 130) · Dạng hư hỏng do cavitation: bề mặt sần xốp",
                   "Hình 5.9 (tr. 130) · Sơ đồ bề mặt bị cavitation: các hố xói sần xốp như tro do "
                   "bọt hơi vỡ giải phóng năng lượng ngay sát bề mặt kim loại, khác với vùng mòn "
                   "nhẵn của flashing.",
                   "Figure 5.9 (p. 130) · Vector schematic of cavitation damage: a rough, "
                   "cinder-like pitted surface produced when vapor bubbles collapse against the "
                   "metal surface, unlike the smooth flashing erosion.",
                   "Sơ đồ bề mặt sần xốp có hố do cavitation",
                   "Schematic of rough pitted surface from cavitation")


@_reg
def fig_f5_10():
    """Figure 5.10 (pp. 132-133) - Valve trim for aerodynamic noise."""
    w, h = 640, 450
    o = [_defs()]
    o.append(T(150, 40, "Cage một cấp, khe hẹp song song / Single-stage slotted cage",
               8.0, anchor="start", weight="600"))
    o.append(_rect(150, 56, 300, 104, fill="#f4f7fb", sw=1.6))
    for sx in range(166, 440, 18):
        o.append(_rect(sx, 68, 6, 78, fill="#ffffff", sw=0.9, stroke=GREY))
    o.append(_poly([(280, 92), (320, 92), (312, 142), (288, 142)],
                   fill="#fdf3e6", sw=1.4, close=True))
    o.append(_arrow(150, 156, 450, 156, sw=1.6, color=GREEN))
    o.append(T(470, 92, "Dòng khí giãn nở / Expanding gas flow", 7.4, anchor="start"))
    o.append(T(470, 116, "Giảm 15-20 dBA / 15-20 dBA", 7.4, anchor="start", color=BLUE))
    o.append(T(150, 212, "Cage hai cấp tách chênh áp / Two-stage cage trim",
               8.0, anchor="start", weight="600"))
    o.append(_rect(150, 228, 300, 120, fill="#f4f7fb", sw=1.6))
    for sx in range(166, 440, 22):
        o.append(_rect(sx, 240, 7, 42, fill="#ffffff", sw=0.9, stroke=GREY))
        o.append(_rect(sx + 8, 298, 7, 40, fill="#ffffff", sw=0.9, stroke=GREY))
    o.append(_line(150, 288, 450, 288, sw=1.4, color=INK))
    o.append(_arrow(150, 366, 450, 366, sw=1.6, color=GREEN))
    o.append(T(470, 268, "Cấp 1 / Stage 1", 7.4, anchor="start"))
    o.append(T(470, 318, "Cấp 2 / Stage 2", 7.4, anchor="start"))
    o.append(T(470, 344, "Đến 30 dBA / Up to 30 dBA", 7.4, anchor="start", color=BLUE))
    o.append(T(320, 408,
               "Hai dạng trim cage xử lý nguồn ồn: khe hẹp và tiết lưu nhiều tầng / "
               "Two source-treatment cage trims: narrow slots and staged restrictions",
               7.0, color=GREY))
    return _finish(w, h, o,
                   "Figure 5.10 - Valve trim design for reducing aerodynamic noise",
                   "Hình 5.10 (tr. 132) · Thiết kế trim giảm ồn khí động",
                   "Hình 5.10 (tr. 132) · Hai dạng trim cage giảm ồn: cage một cấp có nhiều khe hẹp "
                   "song song và cage hai cấp tách chênh áp thành nhiều tầng, giảm ồn lần lượt "
                   "khoảng 15-20 và đến 30 dBA.",
                   "Figure 5.10 (p. 132) · Two noise-abatement cage trims: a single-stage cage "
                   "with many narrow parallel slots and a two-stage cage that splits the drop "
                   "into steps, giving about 15-20 and up to 30 dBA reduction.",
                   "Hai kiểu cage giảm ồn một cấp và hai cấp",
                   "Single-stage and two-stage noise abatement cages")


@_reg
def fig_f5_11():
    """Figure 5.11 (p. 133) - Valve and inline diffuser combination."""
    w, h = 660, 340
    o = [_defs()]
    o.append(_rect(268, 126, 332, 60, fill="#f7f9fb", sw=1.5))
    o.append(_rect(150, 110, 120, 92, fill="#f4f7fb", sw=1.6))
    o.append(_rect(130, 138, 22, 36, fill="#e9eef4", sw=1.3))
    o.append(_line(210, 110, 210, 76, sw=2.6, color=INK))
    o.append(_rect(190, 76, 40, 12, fill="#dfe7ef", sw=1.2))
    o.append(_poly([(196, 158), (224, 158), (218, 182), (202, 182)],
                   fill="#fdf3e6", sw=1.4, close=True))
    o.append(_rect(360, 136, 96, 40, fill="#eef3fb", sw=1.5))
    for sx in range(370, 450, 12):
        o.append(_circle(sx, 156, 3, fill="#ffffff", sw=0.9, color=BLUE))
    o.append(_arrow(278, 156, 350, 156, sw=1.8, color=GREEN))
    o.append(_arrow(462, 156, 590, 156, sw=1.8, color=GREEN))
    o.append(T(210, 66, "Van điều khiển / Control valve", 7.6, anchor="middle"))
    o.append(T(408, 122, "Bộ khuếch tán nội tuyến / Inline diffuser", 7.6, anchor="middle"))
    o.append(T(88, 142, "P1", 8.4, color=INK))
    o.append(T(606, 142, "P2", 8.4, color=INK))
    o.append(_leader(210, 202, 210, 240))
    o.append(T(210, 252, "Tiết lưu / Throttling", 7.4, anchor="middle"))
    o.append(_leader(408, 180, 408, 240))
    o.append(T(408, 252, "Chia chênh áp / Shared pressure drop", 7.4, anchor="middle"))
    o.append(T(330, 306,
               "Tổng chênh áp được chia giữa van và bộ khuếch tán / "
               "The total pressure drop is shared between valve and diffuser",
               7.0, color=GREY))
    return _finish(w, h, o,
                   "Figure 5.11 - Valve and inline diffuser combination",
                   "Hình 5.11 (tr. 133) · Van kết hợp bộ khuếch tán nội tuyến",
                   "Hình 5.11 (tr. 133) · Lắp đặt điển hình với van điều khiển và bộ khuếch tán cố "
                   "định ở hạ lưu; tổng chênh áp được chia cho hai phần tử để giảm ồn khi tỷ lệ "
                   "chênh áp cao.",
                   "Figure 5.11 (p. 133) · Typical installation of a control valve with a fixed "
                   "downstream diffuser; the total pressure drop is shared between the two "
                   "elements to reduce noise at high pressure ratios.",
                   "Sơ đồ van và bộ khuếch tán nội tuyến phía hạ lưu",
                   "Schematic of valve and downstream inline diffuser")


@_reg
def fig_f5_12():
    """Figure 5.12 (p. 133) - Valve and vent diffuser combination."""
    w, h = 660, 340
    o = [_defs()]
    o.append(_rect(180, 126, 250, 60, fill="#f7f9fb", sw=1.5))
    o.append(_rect(100, 110, 100, 92, fill="#f4f7fb", sw=1.6))
    o.append(_rect(82, 138, 20, 36, fill="#e9eef4", sw=1.3))
    o.append(_line(150, 110, 150, 76, sw=2.6, color=INK))
    o.append(_rect(132, 76, 36, 12, fill="#dfe7ef", sw=1.2))
    o.append(_poly([(138, 158), (164, 158), (159, 182), (143, 182)],
                   fill="#fdf3e6", sw=1.4, close=True))
    o.append(_rect(300, 136, 92, 40, fill="#eef3fb", sw=1.5))
    for sx in range(310, 386, 12):
        o.append(_circle(sx, 156, 3, fill="#ffffff", sw=0.9, color=BLUE))
    o.append(_rect(430, 70, 44, 116, fill="#eef3fb", sw=1.5))
    o.append(_arrow(398, 156, 428, 156, sw=1.8, color=GREEN))
    o.append(_path("M 452 70 C 452 44 468 44 468 24", sw=1.6, color=GREEN))
    o.append(_path("M 440 70 C 440 48 452 48 452 28", sw=1.2, color=GREEN))
    o.append(T(150, 66, "Van điều khiển / Control valve", 7.6, anchor="middle"))
    o.append(T(346, 122, "Bộ khuếch tán cổng xả / Vent diffuser", 7.4, anchor="middle"))
    o.append(T(600, 40, "Xả ra khí quyển / Vent to atmosphere", 7.2, anchor="end"))
    o.append(T(600, 60, "Giảm đến 40 dBA / Up to 40 dBA", 7.2, anchor="end", color=BLUE))
    o.append(T(60, 142, "P1", 8.4, color=INK))
    o.append(T(330, 300,
               "Chia chênh áp giữa van và cổng xả giúp giảm ồn cho cả hai / "
               "Sharing the drop between valve and vent quiets both",
               7.0, color=GREY))
    return _finish(w, h, o,
                   "Figure 5.12 - Valve and vent diffuser combination",
                   "Hình 5.12 (tr. 133) · Van kết hợp bộ khuếch tán cổng xả",
                   "Hình 5.12 (tr. 133) · Hệ thống xả ra khí quyển gồm van điều khiển và bộ khuếch "
                   "tán cổng xả phía trước; chia chênh áp giúp giảm ồn cho cả van và cổng xả, có "
                   "thể tới 40 dBA.",
                   "Figure 5.12 (p. 133) · An atmospheric vent system with a control valve and an "
                   "upstream vent diffuser; sharing the drop quiets both valve and vent, with "
                   "reductions up to 40 dBA.",
                   "Sơ đồ van và bộ khuếch tán cổng xả ra khí quyển",
                   "Schematic of valve and atmospheric vent diffuser")


@_reg
def fig_f5_13():
    """Figure 5.13 (p. 133) - Special valve design to eliminate cavitation."""
    w, h = 640, 380
    o = [_defs()]
    o.append(_rect(150, 110, 340, 150, fill="#f4f7fb", sw=1.8))
    o.append(_rect(130, 160, 22, 50, fill="#e9eef4", sw=1.3))
    o.append(_rect(488, 160, 22, 50, fill="#e9eef4", sw=1.3))
    o.append(_line(320, 110, 320, 74, sw=2.6, color=INK))
    o.append(_rect(302, 74, 36, 12, fill="#dfe7ef", sw=1.2))
    for i in range(5):
        sx = 186 + i * 58
        o.append(_rect(sx, 132, 30, 106, fill="#e9eef4", sw=1.2))
        for hy in range(142, 232, 16):
            o.append(_circle(sx + 15, hy, 3, fill="#ffffff", sw=0.8, color=BLUE))
    o.append(_arrow(150, 186, 180, 186, sw=1.6, color=GREEN))
    o.append(_arrow(474, 186, 508, 186, sw=1.6, color=GREEN))
    o.append(_line(170, 264, 500, 264, sw=0.8, dash="4 3", color=RED))
    o.append(T(504, 268, "Pv", 7.4, anchor="start", color=RED))
    o.append(T(108, 182, "P1", 8.4, color=INK))
    o.append(T(526, 182, "P2", 8.4, color=INK))
    o.append(_leader(320, 74, 430, 52))
    o.append(T(434, 48, "Trim nhiều tầng / Multi-stage trim", 7.6, anchor="start"))
    o.append(T(320, 312,
               "Mỗi tầng giữ áp suất trên Pv nên không hình thành bọt hơi / "
               "Each stage keeps pressure above vapor pressure so no bubbles form",
               7.0, color=GREY))
    o.append(T(320, 344,
               "Tiết lưu nối tiếp triệt tiêu cavitation / Series restrictions eliminate cavitation",
               7.0, color=GREY))
    return _finish(w, h, o,
                   "Figure 5.13 - Special valve design to eliminate cavitation",
                   "Hình 5.13 (tr. 133) · Thiết kế van đặc biệt triệt tiêu cavitation",
                   "Hình 5.13 (tr. 133) · Trim nhiều tầng tiết lưu nối tiếp chia tổng chênh áp thành "
                   "các phần nhỏ, giữ áp suất tại mỗi vena contracta trên áp suất hơi hóa nên không "
                   "hình thành bọt hơi gây cavitation.",
                   "Figure 5.13 (p. 133) · A multi-stage series-restriction trim splits the total "
                   "drop into small steps so that pressure at each vena contracta stays above "
                   "vapor pressure and no cavitation bubbles form.",
                   "Sơ đồ trim nhiều tầng triệt tiêu cavitation",
                   "Schematic of multi-stage trim eliminating cavitation")


@_reg
def fig_f5_14():
    """Figure 5.14 (p. 135) - Typical inline silencer."""
    w, h = 640, 330
    o = [_defs()]
    o.append(_line(60, 130, 580, 130, sw=1.8, color=INK))
    o.append(_line(60, 210, 580, 210, sw=1.8, color=INK))
    o.append(_rect(230, 130, 200, 80, fill="url(#h6)", sw=1.6, stroke=INK))
    o.append(_rect(246, 142, 168, 56, fill="#fdfdfd", sw=1.4))
    for sx in range(258, 410, 14):
        o.append(_circle(sx, 156, 3, fill="#ffffff", sw=0.9, color=BLUE))
        o.append(_circle(sx, 184, 3, fill="#ffffff", sw=0.9, color=BLUE))
    o.append(_arrow(80, 170, 220, 170, sw=1.8, color=GREEN))
    o.append(_arrow(442, 170, 570, 170, sw=1.8, color=GREEN))
    o.append(_leader(330, 130, 330, 72))
    o.append(T(330, 68, "Vật liệu tiêu âm / Absorptive material", 7.6, anchor="middle"))
    o.append(_leader(330, 210, 330, 264))
    o.append(T(330, 274, "Ống đục lỗ / Perforated tube", 7.6, anchor="middle"))
    o.append(T(600, 250, "Suy giảm chèn khoảng 25 dBA / About 25 dBA insertion loss",
               7.0, anchor="end", color=BLUE))
    o.append(T(320, 308,
               "Tiêu hao năng lượng âm bên trong dòng chất lỏng / "
               "Acoustic energy is dissipated inside the flow stream", 7.0, color=GREY))
    return _finish(w, h, o,
                   "Figure 5.14 - Typical inline silencer",
                   "Hình 5.14 (tr. 135) · Bộ tiêu âm nội tuyến điển hình",
                   "Hình 5.14 (tr. 135) · Ống tiêu âm nội tuyến gồm ống đục lỗ bao quanh bằng vật "
                   "liệu hấp thụ âm; tiêu hao năng lượng âm trong dòng chất lỏng, suy giảm chèn "
                   "thường giới hạn khoảng 25 dBA.",
                   "Figure 5.14 (p. 135) · A typical inline silencer with a perforated tube "
                   "surrounded by absorptive material, dissipating acoustic energy in the flow "
                   "stream; insertion loss is usually limited to about 25 dBA.",
                   "Sơ đồ bộ tiêu âm nội tuyến có ống đục lỗ và vật liệu hấp thụ",
                   "Schematic of inline silencer with perforated tube and absorptive material")


@_reg
def fig_f5_15():
    """Figure 5.15 (p. 135) - Globe valve with noise abatement cage."""
    w, h = 620, 420
    o = [_defs()]
    o.append(_ellipse(300, 52, 88, 20, fill="#eef3fb", sw=1.5))
    o.append(_spring(300, 60, 112, width=30))
    o.append(_rect(286, 112, 28, 46, fill="#e9eef4", sw=1.2))
    o.append(_line(300, 152, 300, 178, sw=2.6, color=INK))
    o.append(_rect(170, 178, 260, 118, fill="#f4f7fb", sw=1.8))
    o.append(_rect(150, 222, 22, 30, fill="#e9eef4", sw=1.3))
    o.append(_rect(428, 222, 22, 30, fill="#e9eef4", sw=1.3))
    o.append(_rect(232, 194, 136, 86, fill="#e9eef4", sw=1.4))
    for sx in range(242, 362, 14):
        o.append(_rect(sx, 204, 6, 66, fill="#ffffff", sw=0.8, stroke=GREY))
    o.append(_poly([(282, 216), (318, 216), (312, 254), (288, 254)],
                   fill="#fdf3e6", sw=1.4, close=True))
    o.append(_arrow(170, 258, 232, 258, sw=1.6, color=GREEN))
    o.append(_arrow(368, 258, 430, 258, sw=1.6, color=GREEN))
    o.append(_leader(300, 194, 470, 150))
    o.append(T(600, 146, "Cage giảm ồn / Noise abatement cage", 7.0, anchor="end"))
    o.append(T(300, 56, "Cơ cấu chấp hành / Actuator", 7.4, anchor="middle", color=GREY))
    o.append(T(300, 340,
               "Khí giãn nở qua khe hẹp và diện tích tăng dần / "
               "Gas expands through narrow slots into increasing area", 7.0, color=GREY))
    o.append(T(300, 374,
               "Giảm ồn khí động bằng xử lý tại nguồn / Aerodynamic noise treated at the source",
               7.0, color=GREY))
    return _finish(w, h, o,
                   "Figure 5.15 - Globe-style valve with noise abatement cage",
                   "Hình 5.15 (tr. 135) · Van cầu có cage giảm ồn cho dòng khí",
                   "Hình 5.15 (tr. 135) · Van cầu kiểu thân trượt lắp cage giảm ồn quanh nút van; cage "
                   "có khe hẹp và diện tích giãn nở tăng dần làm giảm ồn khí động phát sinh khi khí "
                   "giãn nở qua van.",
                   "Figure 5.15 (p. 135) · A sliding-stem globe valve fitted with a noise-abatement "
                   "cage around the plug; narrow slots and expanding areas reduce aerodynamic "
                   "noise as gas expands through the valve.",
                   "Van cầu có cage giảm ồn quanh nút van",
                   "Globe valve with noise abatement cage around the plug")


@_reg
def fig_f5_16():
    """Figure 5.16 (p. 135) - Ball valve with attenuator for hydrodynamic noise."""
    w, h = 620, 380
    o = [_defs()]
    o.append(_line(60, 140, 580, 140, sw=1.8, color=INK))
    o.append(_line(60, 210, 580, 210, sw=1.8, color=INK))
    o.append(_circle(220, 175, 46, fill="#f4f7fb", sw=1.8))
    o.append(_rect(198, 140, 44, 70, fill="#ffffff", sw=1.2))
    o.append(_line(220, 140, 220, 96, sw=2.6, color=INK))
    o.append(_rect(206, 82, 28, 14, fill="#dfe7ef", sw=1.2))
    o.append(_rect(340, 142, 110, 66, fill="#eef3fb", sw=1.5))
    for sx in range(350, 444, 12):
        o.append(_circle(sx, 158, 3, fill="#ffffff", sw=0.8, color=BLUE))
        o.append(_circle(sx, 192, 3, fill="#ffffff", sw=0.8, color=BLUE))
    o.append(_arrow(80, 175, 172, 175, sw=1.8, color=GREEN))
    o.append(_arrow(270, 175, 330, 175, sw=1.6, color=GREEN))
    o.append(_arrow(456, 175, 570, 175, sw=1.8, color=GREEN))
    o.append(_leader(220, 129, 220, 62))
    o.append(T(220, 58, "Van bi / Ball valve", 7.6, anchor="middle"))
    o.append(_leader(395, 142, 395, 250))
    o.append(T(395, 264, "Bộ giảm âm / Attenuator", 7.6, anchor="middle"))
    o.append(T(310, 320,
               "Dòng chất lỏng được tách và tiêu hao năng lượng áp suất / "
               "The liquid stream is divided and pressure energy is dissipated",
               7.0, color=GREY))
    o.append(T(310, 352,
               "Xử lý ồn thủy động phía hạ lưu / Hydrodynamic noise treated downstream",
               7.0, color=GREY))
    return _finish(w, h, o,
                   "Figure 5.16 - Ball valve with attenuator to reduce noise",
                   "Hình 5.16 (tr. 135) · Van bi có bộ giảm âm cho dòng chất lỏng",
                   "Hình 5.16 (tr. 135) · Van bi lắp thêm bộ giảm âm ở hạ lưu để xử lý ồn thủy động; "
                   "bộ phận này tách dòng và tiêu hao năng lượng áp suất trước khi chất lỏng đi ra "
                   "khỏi van.",
                   "Figure 5.16 (p. 135) · A ball valve with a downstream attenuator for "
                   "hydrodynamic noise; the device divides the stream and dissipates pressure "
                   "energy before the liquid leaves the valve.",
                   "Van bi có bộ giảm âm phía hạ lưu",
                   "Ball valve with downstream hydrodynamic noise attenuator")


@_reg
def fig_f5_17():
    """Figure 5.17 (p. 136) - Application guidelines, 100 PPM service."""
    w, h = 680, 470
    o = [_defs()]
    x, y, W, H = 92, 54, 470, 296
    px, py = _chart_axes(
        o, x, y, W, H, (-46, 315), (0, 140),
        "Nhiệt độ đóng gói, °C / Packing temperature, °C",
        "Áp suất (bar) / Pressure (bar)",
        [(-46, "-46"), (-18, "-18"), (65, "65"), (149, "149"),
         (232, "232"), (315, "315")],
        [(0, "0"), (28, "28"), (55, "55"), (83, "83"), (110, "110"), (138, "138")],
        fs=6.8)
    bands = [
        (-46, 93, 0, 21, "#e8eef6", "ENVIRO-SEAL PTFE"),
        (-18, 93, 21, 62, "#e4f0e8", "Single PTFE V-Ring"),
        (-46, 232, 62, 97, "#f3ebdc", "ENVIRO-SEAL Duplex"),
        (-46, 260, 97, 124, "#e9e3f1", "ENVIRO-SEAL Graphite ULF / HIGH-SEAL Graphite ULF"),
        (-46, 315, 124, 138, "#f6e6e2", "ENVIRO-SEAL H2 Duplex"),
        (65, 260, 28, 55, "#fdf3e6", "KALREZ with VESPEL CR-6100 (KVSP500)"),
    ]
    for xa, xb, ya, yb, fill, _ in bands:
        o.append(_rect(px(xa), py(yb), px(xb) - px(xa), py(ya) - py(yb),
                       fill=fill, sw=0.8, stroke=GREY))
    o.append(T(x + W, y - 12, "°F: -50 to 600    psi: 0 to 2000",
               7.0, anchor="end", color=GREY))
    for bx, by, blab in [
        (182, 328, "ENVIRO-SEAL PTFE"),
        (198, 262, "V-Ring đơn / Single"),
        (263, 182, "ENVIRO-SEAL Duplex"),
        (281, 116, "Graphite ULF / HIGH-SEAL"),
        (327, 73, "ENVIRO-SEAL H2 Duplex"),
        (350, 262, "KALREZ / VESPEL"),
    ]:
        o.append(T(bx, by, blab, 7.0, color=INK, weight="600"))
    o.append(T(340, 412,
               "Vùng ứng dụng minh họa theo nhiệt độ và áp suất / "
               "Illustrative application envelopes versus temperature and pressure",
               7.0, color=GREY))
    o.append(T(340, 438,
               "Chỉ dùng làm hướng dẫn chọn đệm, không phải giới hạn thiết kế / "
               "Selection guidance only, not design limits", 7.0, color=GREY))
    return _finish(w, h, o,
                   "Figure 5.17 - Application guidelines chart for 100 PPM service",
                   "Hình 5.17 (tr. 136) · Vùng chọn đệm cho dịch vụ 100 PPM",
                   "Hình 5.17 (tr. 136) · Biểu đồ vùng ứng dụng minh họa theo nhiệt độ và áp suất "
                   "cho các hệ thống đệm trong dịch vụ giới hạn 100 PPM; mỗi vùng tương ứng với "
                   "một loại đệm hoặc cụm đệm.",
                   "Figure 5.17 (p. 136) · Illustrative application envelopes versus temperature "
                   "and pressure for packing systems in 100 PPM service; each band corresponds "
                   "to a packing type or packing set.",
                   "Biểu đồ vùng chọn đệm theo nhiệt độ và áp suất cho dịch vụ 100 PPM",
                   "Packing selection envelope chart for 100 PPM service")


@_reg
def fig_f5_18():
    """Figure 5.18 (p. 136) - Application guidelines, non-environmental."""
    w, h = 680, 470
    o = [_defs()]
    x, y, W, H = 92, 54, 470, 296
    px, py = _chart_axes(
        o, x, y, W, H, (-240, 649), (0, 350),
        "Nhiệt độ đóng gói (°C) / Packing temperature (°C)",
        "Áp suất (bar) / Pressure (bar)",
        [(-240, "-240"), (-129, "-129"), (-18, "-18"), (94, "94"),
         (205, "205"), (316, "316"), (427, "427"), (538, "538"), (649, "649")],
        [(0, "0"), (69, "69"), (138, "138"), (207, "207"), (276, "276"), (345, "345")],
        fs=6.4)
    bands = [
        (-240, 38, 0, 103, "#e8eef6", "ENVIRO-SEAL Graphite ULF"),
        (-18, 232, 103, 207, "#f3ebdc", "ENVIRO-SEAL PTFE and ENVIRO-SEAL Duplex"),
        (-73, 260, 207, 259, "#e4f0e8", "Single and Double PTFE V-Ring"),
        (-18, 371, 259, 293, "#fdf3e6", "KALREZ with VESPEL CR-6100 (KVSP500)"),
        (-240, 649, 293, 328, "#f6e6e2", "ENVIRO-SEAL H2 Duplex"),
        (-46, 538, 328, 345, "#e9e3f1", "HIGH-SEAL Graphite ULF / Graphite ULF / Braided Filament"),
    ]
    for xa, xb, ya, yb, fill, _ in bands:
        o.append(_rect(px(xa), py(yb), px(xb) - px(xa), py(ya) - py(yb),
                       fill=fill, sw=0.8, stroke=GREY))
    o.append(T(x + W, y - 12, "°F: -400 to 1200    psi: 0 to 5000",
               7.0, anchor="end", color=GREY))
    for bx, by, blab in [
        (165, 307, "ENVIRO-SEAL Graphite ULF"),
        (275, 220, "ENVIRO-SEAL PTFE / Duplex"),
        (317, 154, "PTFE V-Ring đơn / đôi"),
        (358, 118, "KALREZ / VESPEL CR-6100"),
        (327, 89, "ENVIRO-SEAL H2 Duplex"),
        (297, 69, "HIGH-SEAL Graphite ULF"),
    ]:
        o.append(T(bx, by, blab, 7.0, color=INK, weight="600"))
    o.append(T(340, 412,
               "Vùng ứng dụng minh họa, phạm vi rộng hơn dịch vụ 100 PPM / "
               "Illustrative envelopes, wider than the 100 PPM chart", 7.0, color=GREY))
    o.append(T(340, 438,
               "Chỉ dùng làm hướng dẫn chọn đệm, không phải giới hạn thiết kế / "
               "Selection guidance only, not design limits", 7.0, color=GREY))
    return _finish(w, h, o,
                   "Figure 5.18 - Application guidelines chart for non-environmental service",
                   "Hình 5.18 (tr. 136) · Vùng chọn đệm cho dịch vụ phi môi trường",
                   "Hình 5.18 (tr. 136) · Biểu đồ vùng ứng dụng minh họa cho dịch vụ không yêu cầu "
                   "giới hạn phát thải; phạm vi nhiệt độ và áp suất rộng hơn so với dịch vụ 100 PPM.",
                   "Figure 5.18 (p. 136) · Illustrative application envelopes for non-environmental "
                   "service, covering wider temperature and pressure ranges than the 100 PPM "
                   "service chart.",
                   "Biểu đồ vùng chọn đệm cho dịch vụ phi môi trường",
                   "Packing selection envelope chart for non-environmental service")
