# -*- coding: utf-8 -*-
"""Safety Instrumented Systems, Chapter 9 — Issues Relating to Field Devices."""
import math

from vfig import (BLUE, GOLD, GREEN, GREY, INK, PAPER, RED, _arrow, _box,
                  _circle, _line, _path, _poly, _rect, _txt)
from pcfig import _finish

DARKRED = "#7f1d1d"
AMBER = "#f6e0b8"
PALE_GREEN = "#dcecdc"
PALE_RED = "#f3d6d2"
PALE_BLUE = "#e8eef6"
PALE_GOLD = "#f7efdd"
EDGE = "#b9b3a4"


def _vtxt(x, y, s, size=7.0, color=GREY):
    """A text label rotated 90 degrees anticlockwise about (x, y)."""
    return ('<text x="%s" y="%s" text-anchor="middle" transform="rotate(-90 %s %s)" '
            'style="font:%spx Inter,Helvetica,sans-serif;fill:%s;">%s</text>'
            % (x, y, x, y, size, color, s))


def _wedge(cx, cy, r, a0, a1, fill, n=16, sw=0.9, color=EDGE):
    """A pie slice between two angles in degrees, measured anticlockwise from +x."""
    pts = [(cx, cy)]
    for i in range(n + 1):
        a = math.radians(a0 + (a1 - a0) * i / float(n))
        pts.append((cx + r * math.cos(a), cy - r * math.sin(a)))
    return _poly(pts, fill=fill, sw=sw, color=color, close=True)


def _res_h(x, y, w, label=""):
    """A horizontal resistor: a zigzag of width w starting at (x, y)."""
    o = []
    n, amp = 6, 5.0
    step = w / float(n)
    pts = [(x, y)]
    for i in range(n):
        sgn = 1 if i % 2 == 0 else -1
        pts.append((x + step * (i + 0.5), y + sgn * amp))
    pts.append((x + w, y))
    o.append(_poly(pts, fill="none", sw=1.1, color=INK))
    if label:
        o.append(_txt(x + w / 2.0, y - 12, label, 5.8, color=GREY))
    return "".join(o)


def _cont(x, y, label="", closed=True, size=6.0):
    """A relay contact drawn horizontally at (x, y), width 34."""
    o = [_circle(x, y, 2.2, fill=INK, sw=0.6)]
    o.append(_circle(x + 34, y, 2.2, fill=INK, sw=0.6))
    if closed:
        o.append(_line(x, y, x + 34, y, sw=1.6))
    else:
        o.append(_line(x, y, x + 30, y - 12, sw=1.6))
    if label:
        o.append(_txt(x + 17, y + 16, label, size, color=GREY))
    return "".join(o)


# ---------------------------------------------------------------- 9.1
def fig_9_1():
    """Where the failures actually are."""
    cx, cy, r = 178, 148, 96
    o = [_txt(330, 20, "Phân bố hư hỏng của một SIS điển hình", 8.2, weight="600")]

    o.append(_wedge(cx, cy, r, 90, 90 - 151.2, PALE_GOLD))
    o.append(_wedge(cx, cy, r, 90 - 151.2, 90 - 151.2 - 180, PALE_RED))
    o.append(_wedge(cx, cy, r, 90 - 151.2 - 180, 90 - 151.2 - 180 - 28.8, PALE_BLUE))
    o.append(_circle(cx, cy, r, fill="none", sw=1.1))

    def lab(a, txt, sub, col):
        x = cx + 58 * math.cos(math.radians(a))
        y = cy - 58 * math.sin(math.radians(a))
        return (_txt(x, y - 4, txt, 9.4, color=col, weight="600")
                + _txt(x, y + 10, sub, 5.8, color=GREY))

    o.append(lab(90 - 75.6, "42 %", "cảm biến", GOLD))
    o.append(lab(90 - 151.2 - 90, "50 %", "phần tử cuối", DARKRED))
    o.append(lab(90 - 151.2 - 180 - 14.4, "8 %", "logic", BLUE))

    o.append(_txt(300, 62, "Một hệ gồm: một cảm biến áp suất, bốn rơ-le logic,", 6.2,
                  anchor="start", color=GREY))
    o.append(_txt(300, 74, "một van điện từ và một van dừng. Tổng PFD 0,06 —", 6.2,
                  anchor="start", color=GREY))
    o.append(_txt(300, 86, "tức RRF 16, vừa đủ SIL 1.", 6.2, anchor="start", color=GREY))

    o.append(_rect(300, 104, 14, 12, PALE_GOLD, sw=0.8, stroke=EDGE))
    o.append(_txt(322, 114, "Cảm biến — 42 %", 6.4, anchor="start"))
    o.append(_rect(300, 126, 14, 12, PALE_RED, sw=0.8, stroke=EDGE))
    o.append(_txt(322, 136, "Phần tử cuối — 50 % (van điện từ 25 + van dừng 25)", 6.4,
                  anchor="start"))
    o.append(_rect(300, 148, 14, 12, PALE_BLUE, sw=0.8, stroke=EDGE))
    o.append(_txt(322, 158, "Logic — 8 %", 6.4, anchor="start"))

    o.append(_txt(300, 190, "Thiết bị trường: 92 %. Hộp logic: 8 %.", 6.6,
                  anchor="start", weight="600"))
    o.append(_txt(300, 208, "Mọi cuộc tranh luận về PLC, TMR hay 1oo2D chỉ đang", 6.2,
                  anchor="start", color=GREY))
    o.append(_txt(300, 220, "nói về tám phần trăm ấy.", 6.2, anchor="start", color=GREY))
    return _finish(o, 660, 296,
                   "Hình 9-1. Phân bố hư hỏng theo phần trăm, tính từ Bảng 9-1. Một hệ SIL 1 với một cảm "
                   "biến, bốn rơ-le, một van điện từ và một van dừng cho RRF 16. Hai mươi lăm phần trăm "
                   "nằm ở chiếc van điện từ — thứ rẻ nhất và ít được bàn nhất trong cả hệ.",
                   "Figure 9-1. The percentage split of failures, computed from Table 9-1. A SIL 1 system "
                   "with one sensor, four relays, a solenoid and a shutdown valve comes to RRF 16. A "
                   "quarter of the failures sit in the solenoid — the cheapest and least discussed item in "
                   "the loop.",
                   "Biểu đồ tròn: cảm biến 42 phần trăm, phần tử cuối 50 phần trăm, logic 8 phần trăm.",
                   "A pie chart: sensors 42 percent, final elements 50 percent, logic 8 percent.")


# ---------------------------------------------------------------- 9.2
def fig_9_2():
    """One transmitter with diagnostics: two signals out of one device."""
    o = [_txt(330, 20, "1oo1D: một bộ chuyển đổi, hai tín hiệu ra", 8.2, weight="600")]

    o.append(_line(24, 120, 58, 120, sw=1.6))
    o.append(_line(24, 112, 24, 128, sw=1.6))
    o.append(_txt(38, 106, "quá trình", 5.6, color=GREY))

    o.append(_rect(58, 96, 96, 48, PAPER, sw=1.1))
    o.append(_txt(106, 116, "Bộ chuyển đổi", 6.6, weight="600"))
    o.append(_txt(106, 130, "4–20 mA + HART", 5.8, color=GREY))

    o.append(_arrow(154, 108, 300, 108, sw=1.2))
    o.append(_txt(226, 100, "4–20 mA", 5.8, color=GREY))

    o.append(_rect(300, 52, 150, 140, "#fbfaf7", sw=1.1))
    o.append(_txt(375, 68, "Hệ logic", 6.8, weight="600"))
    o.append(_rect(312, 78, 126, 34, PALE_GOLD, sw=0.8, stroke=EDGE))
    o.append(_txt(375, 92, "tiếp điểm trạng thái", 5.8))
    o.append(_txt(375, 103, "quá trình", 5.8))
    o.append(_rect(312, 140, 126, 34, PALE_BLUE, sw=0.8, stroke=EDGE))
    o.append(_txt(375, 154, "tiếp điểm trạng thái", 5.8))
    o.append(_txt(375, 165, "bộ chuyển đổi", 5.8))

    o.append(_path("M 106 144 L 106 236 L 300 236", fill="none", sw=1.1, color=GOLD,
                   dash="4 3"))
    o.append(_txt(120, 230, "tín hiệu HART", 5.6, anchor="start", color=GOLD))

    o.append(_rect(300, 212, 150, 46, PAPER, sw=1.1))
    o.append(_txt(375, 230, "Giám sát HART", 6.4, weight="600"))
    o.append(_txt(375, 244, "kiểm tra chẩn đoán", 5.6, color=GREY))

    o.append(_arrow(375, 212, 375, 194, sw=1.2))
    o.append(_txt(383, 205, "báo hỏng", 5.6, anchor="start", color=GREY))

    o.append(_arrow(450, 120, 492, 120, sw=1.2))
    o.append(_txt(498, 116, "cắt", 6.0, anchor="start"))
    o.append(_txt(498, 128, "hoặc báo động", 6.0, anchor="start"))

    o.append(_txt(330, 274, "Bộ giám sát HART đọc phần số của tín hiệu và bắt được bốn kiểu hỏng mà "
                            "dòng 4–20 mA không thể hiện.", 6.0, color=GREY))
    return _finish(o, 660, 290,
                   "Hình 9-2. Một bộ chuyển đổi, hai đường ra. Dòng 4–20 mA mang giá trị quá trình; tín "
                   "hiệu HART đi kèm mang tình trạng của chính thiết bị. Bộ giám sát HART biến thông tin "
                   "ấy thành một tiếp điểm thứ hai, và tiếp điểm ấy nâng độ phủ chẩn đoán lên khoảng 20 "
                   "điểm phần trăm.",
                   "Figure 9-2. One transmitter, two outputs. The 4–20 mA loop carries the process value; "
                   "the HART signal riding on it carries the health of the device. The HART monitor turns "
                   "that into a second contact, and that contact adds roughly twenty points of diagnostic "
                   "coverage.",
                   "Sơ đồ: bộ chuyển đổi phát dòng 4 đến 20 miliampe tới hệ logic, đồng thời phát tín hiệu "
                   "HART xuống bộ giám sát, bộ này báo hỏng về hệ logic.",
                   "A diagram: the transmitter sends 4–20 mA to the logic solver and a HART signal down to "
                   "a monitor, which reports faults back to the logic solver.")


# ---------------------------------------------------------------- 9.3
def fig_9_3():
    """A supervised circuit: how the logic solver sees four different states."""
    o = [_txt(330, 20, "Mạch có giám sát: bốn trạng thái, một dòng điện", 8.2,
              weight="600")]

    o.append(_line(44, 74, 44, 176, sw=1.4))
    o.append(_line(38, 74, 50, 74, sw=1.6))
    o.append(_line(34, 176, 54, 176, sw=1.6))
    o.append(_txt(30, 70, "+", 8.0, anchor="end"))
    o.append(_txt(30, 180, "−", 8.0, anchor="end"))
    o.append(_txt(24, 126, "24 VDC", 5.8, anchor="start", color=GREY))

    o.append(_line(44, 74, 74, 74, sw=1.4))
    o.append(_cont(74, 74, "tiếp điểm", closed=False))
    o.append(_line(108, 74, 150, 74, sw=1.4))
    o.append(_res_h(150, 74, 44, "R cuối đường"))
    o.append(_line(194, 74, 232, 74, sw=1.4))
    o.append(_line(232, 74, 232, 108, sw=1.4))
    o.append(_arrow(232, 108, 268, 108, sw=1.2))

    o.append(_rect(268, 84, 96, 88, "#fbfaf7", sw=1.1))
    o.append(_txt(316, 100, "Khối vào", 6.6, weight="600"))
    o.append(_txt(316, 114, "đo dòng", 5.8, color=GREY))
    o.append(_txt(316, 130, "I ≈ 2 mA", 5.8, color=GREEN))
    o.append(_txt(316, 146, "= mạch tốt", 5.8, color=GREEN))

    o.append(_line(44, 176, 316, 176, sw=1.4))
    o.append(_arrow(316, 176, 316, 172, sw=1.2))

    states = [("Tiếp điểm mở (bình thường)", "≈ 2 mA", "mạch tốt, không cắt", GREEN),
              ("Tiếp điểm đóng (quá trình sự cố)", "≈ 40 mA", "cắt", DARKRED),
              ("Ngắn mạch dây", "> 60 mA", "báo lỗi mạch", DARKRED),
              ("Đứt dây", "0 mA", "báo lỗi mạch", DARKRED)]
    o.append(_txt(388, 74, "Bốn trạng thái", 6.8, anchor="start", weight="600"))
    for i, (a, b, c, col) in enumerate(states):
        y = 96 + i * 34
        o.append(_circle(394, y - 3, 2.6, fill=col, sw=0.6))
        o.append(_txt(404, y, a, 6.0, anchor="start"))
        o.append(_txt(404, y + 11, b + " → " + c, 5.8, anchor="start", color=GREY))

    o.append(_txt(330, 218, "Dòng điện phân biệt được bốn trạng thái, nên đứt dây và ngắn mạch không "
                            "còn giống nhau nữa.", 6.0, color=GREY))
    o.append(_txt(330, 234, "Đây là ý nghĩa của “đánh thức để cắt”: mất điện cũng là một lệnh cắt, "
                            "nhưng mất điện thì phải nhìn thấy được.", 6.0, color=GREY))
    return _finish(o, 660, 252,
                   "Hình 9-3 (bổ sung). Mạch có giám sát. Điện trở cuối đường cho một dòng điện nhỏ chạy "
                   "qua ngay cả khi tiếp điểm mở, nên khối vào phân biệt được bốn trạng thái thay vì hai. "
                   "Đổi lại, mọi hư hỏng đều tiêu tốn dòng, và bản thân điện trở ấy trở thành một linh "
                   "kiện có thể hỏng.",
                   "Figure 9-3 (added). A supervised circuit. The end-of-line resistor lets a small current "
                   "flow even with the contact open, so the input card sees four states instead of two. In "
                   "exchange, every healthy state draws current, and that resistor becomes one more "
                   "component that can fail.",
                   "Sơ đồ mạch giám sát: nguồn 24 vôn một chiều, tiếp điểm, điện trở cuối đường và khối "
                   "vào đo dòng, kèm bốn trạng thái.",
                   "A supervised-circuit diagram: 24 V DC supply, contact, end-of-line resistor and a "
                   "current-sensing input card, with the four states listed.")


FIGURES = [fig_9_1, fig_9_2, fig_9_3]
