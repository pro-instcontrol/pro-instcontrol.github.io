# -*- coding: utf-8 -*-
"""Vector figures for the Safety Instrumented Systems book, chapters 3 to 5.

Each function returns (svg, caption_vi, caption_en, aria_vi, aria_en).
Chapter 5 has no numbered figures — it carries two tables instead.
"""
import math

from vfig import (BLUE, GOLD, GREEN, GREY, INK, PAPER, RED, _arrow, _axes, _box,
                  _circle, _curve, _defs, _ellipse, _f, _fig, _label, _line,
                  _path, _poly, _rect, _txt, svg)
from pcfig import _finish


# ---------------------------------------------------------------- 3.1
def fig_3_1():
    """The HSE one-page picture: two boxes over one plant."""
    o = [_txt(330, 20, "Khuyến nghị của HSE Anh: tách rời điều khiển và bảo vệ", 8.8, weight="600")]
    o.append(_txt(330, 38, "hai hệ độc lập — không chung cảm biến, không chung bộ xử lý, không chung van",
                  6.8, color=RED))
    # the two systems, side by side
    o.append(_box(52, 54, 196, 44, "Hệ thống điều khiển", fill="#eef3fb", size=8.2))
    o.append(_box(412, 54, 196, 44, "Hệ thống bảo vệ", fill="#f6e6c8", size=8.2))
    # the plant they both act on
    o.append(_box(196, 132, 268, 50, "Thiết bị vận hành", fill="#f3f1ea", size=8.4))
    # two separate paths down into it
    o.append(_arrow(150, 98, 150, 132, sw=1.2))
    o.append(_arrow(510, 98, 510, 132, sw=1.2))
    o.append(_label(158, 118, "tín hiệu điều khiển", 6.6, GREY, anchor="start"))
    o.append(_label(518, 118, "tín hiệu cắt", 6.6, GREY, anchor="start"))
    # the barrier: drawn only above the plant, so it separates the two systems
    # rather than bisecting the equipment they both act on
    o.append(_line(330, 44, 330, 126, sw=1.1, color=RED, dash="6 5"))
    # the sentence the HSE puts on the same page
    o.append(_rect(196, 196, 268, 34, "#ffffff", sw=0.8, stroke="#d8d8d8"))
    o.append(_txt(330, 210, "“Nên bố trí hệ thống điều khiển và", 6.8, color=INK))
    o.append(_txt(330, 221, "hệ thống bảo vệ riêng biệt.”", 6.8, color=INK))
    return _finish(o, 660, 240,
                   "Hình 3-1 · Khuyến nghị của HSE Anh: cảm biến riêng, bộ xử lý riêng, van riêng cho "
                   "chức năng bảo vệ. Hình này chiếm trọn một trang trong tài liệu dành cho quản lý của HSE.",
                   "Figure 3-1 · The U.K. Health & Safety Executive recommendation: separate sensors, "
                   "separate logic, separate valves for the protection function. In the HSE document for "
                   "managers this picture fills a whole page.")


# ---------------------------------------------------------------- 4.1
def fig_4_1():
    """Swiss cheese: solid layers versus layers with holes that line up."""
    o = [_txt(330, 18, "Mô hình “lát phô mai Thụy Sĩ” của James Reason", 8.6, weight="600")]
    # (a) the ideal
    o.append(_txt(148, 40, "(a) Lý thuyết: các lớp đặc, rắn", 7.2, color=GREY))
    for i in range(4):
        o.append(_rect(44 + i * 56, 50, 40, 108, "#eef3fb", sw=1.0))
    o.append(_arrow(20, 104, 40, 104, sw=1.0, color=GREEN))
    o.append(_txt(18, 96, "sự cố", 6.4, color=GREY, anchor="start"))
    # the failure stops dead at the last plate
    o.append(_line(258, 96, 258, 112, sw=1.6, color=GREEN))
    o.append(_txt(264, 100, "bị chặn", 6.4, color=GREEN, anchor="start"))
    # (b) reality
    o.append(_txt(498, 40, "(b) Thực tế: các lỗ trùng nhau", 7.2, color=GREY))
    # every hole straddles y = 104, so the dashed path really does pass through
    holes = [(100, 14), (108, 16), (102, 12), (106, 15)]
    for i, (cy, r) in enumerate(holes):
        x = 380 + i * 56
        o.append(_rect(x, 50, 40, 108, "#f6e6c8", sw=1.0))
        o.append(_circle(x + 20, cy, r, fill=PAPER, sw=0.9, color="#b9a97e"))
    o.append(_arrow(356, 104, 376, 104, sw=1.0, color=RED))
    o.append(_txt(354, 96, "sự cố", 6.4, color=GREY, anchor="start"))
    o.append(_line(620, 104, 636, 104, sw=1.4, color=RED))
    o.append(_arrow(636, 104, 652, 104, sw=1.0, color=RED))
    o.append(_txt(652, 96, "sự kiện", 6.4, color=RED, anchor="end"))
    o.append(_line(360, 104, 640, 104, sw=1.1, color=RED, dash="5 4"))
    o.append(_txt(330, 186, "Lỗ do lỗi quản lý, thiết kế, vận hành và bảo dưỡng tạo ra — "
                            "và chúng luôn di chuyển.", 6.8, color=GREY))
    return _finish(o, 660, 200,
                   "Hình 4-1 · (a) Các lớp bảo vệ trong lý thuyết là những tấm đặc, nên sự cố không thể "
                   "xuyên qua. (b) Trong thực tế mỗi lớp đầy lỗ do lỗi quản lý, thiết kế, vận hành và bảo "
                   "dưỡng; khi các lỗ thẳng hàng, sự cố đi qua hết.",
                   "Figure 4-1 · (a) Protection layers as designed: solid plates, so a failure cannot "
                   "propagate. (b) Protection layers in reality: full of holes made by management, design, "
                   "operations and maintenance errors, and when the holes line up the failure goes "
                   "straight through.")


# ---------------------------------------------------------------- 4.2
def fig_4_2():
    """The onion: process at the centre, response at the rim."""
    o = [_txt(330, 18, "Các lớp bảo vệ — sơ đồ “củ hành”", 8.6, weight="600")]
    cx, cy = 320, 132
    rings = [
        (18, "#e9e4f2", "Quá trình"),
        (30, "#eef3fb", "Điều khiển quá trình cơ bản (BPCS)"),
        (42, "#f6e6c8", "Cảnh báo · con người can thiệp"),
        (54, "#fbe3d8", "Hệ thống đo lường an toàn (SIS)"),
        (66, "#e6f0e6", "Bảo vệ vật lý (van an toàn, đĩa vỡ)"),
        (78, "#f3f1ea", "Bảo vệ vật lý (bờ bao)"),
        (88, "#dfe7ef", "Ứng phó khẩn cấp của nhà máy"),
        (98, "#d5dee9", "Ứng phó khẩn cấp của cộng đồng"),
    ]
    # fill from the outside in, so the inner discs sit on top
    for r, fill, _lab in reversed(rings):
        o.append(_circle(cx, cy, r, fill=fill, sw=1.0))
    # one radial leader per ring, fanned across the right half
    n = len(rings)
    for i, (r, _fill, lab) in enumerate(rings):
        th = math.radians(-50.0 + i * 100.0 / (n - 1.0))
        ca, sa = math.cos(th), math.sin(th)
        o.append(_line(cx + r * ca, cy - r * sa, cx + 126 * ca, cy - 126 * sa, sw=0.7, color=GREY))
        ly = cy - 126 * sa
        xe = cx + 126 * ca
        o.append(_line(xe, ly, 464, ly, sw=0.7, color=GREY))
        o.append(_txt(470, ly + 2.4, lab, 6.6, anchor="start", color=INK))
    # which half of the onion does what
    o.append(_txt(30, 250, "vòng trong: ngăn ngừa sự kiện xảy ra", 6.8, color=BLUE, anchor="start"))
    o.append(_txt(30, 264, "vòng ngoài: giảm nhẹ hậu quả khi sự kiện đã xảy ra", 6.8, color=RED,
                  anchor="start"))
    return _finish(o, 660, 274,
                   "Hình 4-2 · Sơ đồ “củ hành”: các lớp bên trong nhằm ngăn sự kiện nguy hiểm xảy ra, các "
                   "lớp bên ngoài nhằm giảm hậu quả một khi nó đã xảy ra.",
                   "Figure 4-2 · The onion diagram: the inner layers exist to stop a hazardous event from "
                   "happening, the outer layers to reduce the consequences once it has.")


# ---------------------------------------------------------------- 4.3
def fig_4_3():
    """Risk reduction: five factors of ten, laid end to end on a log axis."""
    o = [_txt(330, 18, "Giảm rủi ro bằng nhiều lớp bảo vệ", 8.6, weight="600")]
    x0, y0, W, H = 96, 54, 470, 94
    o.append(_arrow(x0, y0 + H, x0 + W + 18, y0 + H, sw=1.0))
    o.append(_arrow(x0, y0 + H, x0, y0 - 10, sw=1.0))
    o.append(_txt(x0 - 4, y0 - 16, "tần suất sự kiện (năm⁻¹)", 7.2, anchor="start", color=GREY))
    ticks = [(0, "1"), (1, "1/10"), (2, "1/100"), (3, "1/1.000"),
             (4, "1/10.000"), (5, "1/100.000")]
    for v, lab in ticks:
        px = x0 + W - v / 5.0 * W
        o.append(_line(px, y0 + H, px, y0 + H + 4, sw=0.8))
        o.append(_txt(px, y0 + H + 14, lab, 6.6, color=GREY))
    xr, xt = x0 + W, x0
    ybar = y0 + 50
    # five segments of equal width, end to end, each one factor of ten
    layers = [("BPCS", "#7d9bc4"), ("Cảnh báo", "#c9a227"), ("SIS", "#b45309"),
              ("Cơ khí", "#5b8c5b"), ("Khác", "#8b7fb0")]
    seg = W / 5.0
    for i, (lab, col) in enumerate(layers):
        xa = xr - i * seg
        xb = xr - (i + 1) * seg
        o.append(_line(xa, ybar, xb + 4, ybar, sw=9, color=col))
        o.append(_txt((xa + xb) / 2.0, ybar + 20, lab, 6.6, color=col))
    # the two reference lines and their labels, above the bar
    o.append(_line(xr, y0, xr, y0 + H, sw=1.0, color=RED, dash="5 4"))
    o.append(_txt(xr - 4, ybar - 10, "rủi ro vốn có: 1/năm", 6.8, color=RED, anchor="end"))
    o.append(_line(xt, y0, xt, y0 + H, sw=1.0, color=GREEN, dash="5 4"))
    o.append(_txt(xt + 4, ybar - 10, "mức chấp nhận được", 6.8, color=GREEN, anchor="start"))
    o.append(_txt(330, 186, "mỗi đoạn là một hệ số 10; năm lớp độc lập cộng lại thành 100.000",
                  6.8, color=GREY))
    return _finish(o, 660, 200,
                   "Hình 4-3 · Mỗi lớp bảo vệ chỉ đóng góp được một hệ số giảm rủi ro nhất định — BPCS bị "
                   "giới hạn ở hệ số 10. Không lớp nào một mình đưa được tần suất sự kiện từ 1/năm xuống "
                   "1/100.000 năm; năm lớp độc lập thì làm được.",
                   "Figure 4-3 · Each protection layer can only claim a limited risk reduction factor — the "
                   "BPCS is capped at 10. No single layer takes an event from once a year to once in "
                   "100,000 years; five independent layers do.")
