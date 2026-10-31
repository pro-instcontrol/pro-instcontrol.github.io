# -*- coding: utf-8 -*-
"""Safety Instrumented Systems, Chapter 13 — Managing Changes to a System."""
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

RAIL_L, RAIL_R = 54, 606
COIL_X = 470


def _contact(x, y, nc=False):
    """One ladder contact centred at (x, y); nc draws the normally-closed slash."""
    o = [_line(x - 14, y, x, y, sw=1.2),
         _line(x, y - 7, x, y + 7, sw=1.6),
         _line(x + 9, y - 7, x + 9, y + 7, sw=1.6),
         _line(x + 9, y, x + 23, y, sw=1.2)]
    if nc:
        o.append(_line(x - 1, y + 7, x + 10, y - 7, sw=1.1))
    return o


def _coil(x, y):
    """A ladder coil at (x, y): two facing arcs."""
    return [_path("M %s %s A 3,8 0 0 0 %s %s" % (x, y - 8, x, y + 8), sw=1.5),
            _path("M %s %s A 3,8 0 0 1 %s %s" % (x + 10, y - 8, x + 10, y + 8), sw=1.5)]


def _rung(y, ncontacts, nc_flags=None):
    """A full rung from the left rail to the right rail."""
    o = [_line(RAIL_L, y, 90 - 14, y, sw=1.2)]
    x = 90
    for i in range(ncontacts):
        nc = bool(nc_flags and i < len(nc_flags) and nc_flags[i])
        o.extend(_contact(x, y, nc))
        x += 36
    o.append(_line(x - 13, y, COIL_X, y, sw=1.2))
    o.extend(_coil(COIL_X, y))
    o.append(_line(COIL_X + 10, y, RAIL_R, y, sw=1.2))
    return o


# ---------------------------------------------------------------- 13.5
def fig_13_1():
    """The original ladder: the shutdown rung already carries a long contact chain."""
    o = [_txt(330, 20, "Logic thang gốc: dòng cuối đã có một chuỗi tiếp điểm dài", 8.2,
              weight="600")]

    top, bot = 44, 252
    o.append(_line(RAIL_L, top, RAIL_L, bot, sw=2.0))
    o.append(_line(RAIL_R, top, RAIL_R, bot, sw=2.0))

    for i, y in enumerate((64, 106, 148, 190)):
        o.extend(_rung(y, 2))
    o.extend(_rung(232, 6, [False, True, False, True, False, False]))

    o.append(_txt(COIL_X + 3, 220, "CẮT TOÀN GIÀN", 5.6, weight="600", color=DARKRED))
    o.append(_txt(180, 246, "sáu tiếp điểm nối tiếp trên cùng một dòng", 5.2, color=GREY))
    o.append(_txt(330, 276, "Chỉ cần một tiếp điểm trong chuỗi này hở là cả giàn bị cắt — và cũng chỉ "
                            "cần một chỗ để sửa sai là mất luôn chức năng ấy.", 5.4, color=GREY))

    return _finish(o, 660, 292,
                   "Hình 13-1. Logic thang gốc. Dòng cuối cùng là dòng cắt toàn giàn: một chuỗi sáu tiếp "
                   "điểm nối tiếp, chỉ cần một tiếp điểm hở là cuộn dây mất điện và cả giàn dừng. Cũng vì "
                   "chuỗi đã dài kín chỗ, người lập trình sau này không còn chỗ để thêm tiếp điểm mới — và "
                   "đó chính là chỗ tai nạn bắt đầu.",
                   "Figure 13-1. The original ladder. The last rung is the platform-wide shutdown: a chain "
                   "of six contacts in series, any one of which opening de-energises the coil and stops the "
                   "whole platform. Because the chain was already full, the next programmer had nowhere to "
                   "add a contact — which is exactly where the accident starts.",
                   "Sơ đồ thang: năm dòng, dòng cuối cùng gồm sáu tiếp điểm nối tiếp và một cuộn dây cắt.",
                   "A ladder diagram: five rungs, the last one carrying six contacts in series and a "
                   "shutdown coil.")


# ---------------------------------------------------------------- 13.5
def fig_13_2():
    """The revision that broke it: the same coil written twice."""
    o = [_txt(330, 20, "Bản sửa: cùng một cuộn dây được ghi ở hai dòng — dòng sau thắng", 8.2,
              weight="600")]

    top, bot = 44, 306
    o.append(_line(RAIL_L, top, RAIL_L, bot, sw=2.0))
    o.append(_line(RAIL_R, top, RAIL_R, bot, sw=2.0))

    for y in (64, 106, 148, 190):
        o.extend(_rung(y, 2))
    o.extend(_rung(232, 6, [False, True, False, True, False, False]))
    o.append(_txt(COIL_X + 3, 220, "CẮT TOÀN GIÀN", 5.6, weight="600", color=DARKRED))

    # the added rung
    o.append(_rect(40, 256, 580, 54, PALE_RED, sw=1.0, dash="4 3", stroke=DARKRED))
    o.extend(_rung(281, 1))
    o.append(_txt(COIL_X + 3, 269, "CẮT TOÀN GIÀN (lần 2)", 5.6, weight="600", color=DARKRED))
    o.append(_txt(150, 324, "dòng thêm vào", 5.2, weight="600", color=DARKRED))

    o.append(_txt(330, 344, "Trong logic thang, mọi giá trị chỉ được ghi vào bộ nhớ trong một vòng quét; "
                            "cuộn dây ở dòng cuối ghi đè lên kết quả của dòng trước. Dòng gốc ra lệnh cắt, "
                            "dòng mới ghi lại trạng thái “bình thường”.", 5.4, color=GREY))

    return _finish(o, 660, 356,
                   "Hình 13-2. Bản sửa đã gây ra sự cố. Không còn chỗ trên chuỗi tiếp điểm, người lập trình "
                   "thêm một dòng mới và lặp lại chính cuộn dây cắt ấy. Logic thang không ghi thẳng ra đầu "
                   "ra trong lúc quét: giá trị nằm trong bộ nhớ cho tới cuối vòng quét, nên dòng sau ghi đè "
                   "lên dòng trước — dòng gốc ra lệnh cắt, dòng mới đặt lại về “bình thường”, và đầu ra "
                   "không bao giờ mất điện. Người dùng chỉ thử phần vừa sửa, nên không phát hiện ra.",
                   "Figure 13-2. The revision that caused the incident. With no room left on the contact "
                   "chain, the programmer added a new rung and repeated the same shutdown coil. Ladder logic "
                   "does not write to outputs during the scan: values sit in memory until the scan ends, so "
                   "the later rung overwrites the earlier one — the original rung calls for a shutdown, the "
                   "new one resets it to normal, and the output never de-energises. The revision was tested; "
                   "the original logic was not.",
                   "Sơ đồ thang đã sửa: sáu dòng, trong đó dòng thứ sáu lặp lại cùng cuộn dây cắt, được "
                   "đánh dấu bằng khung nét đứt.",
                   "The modified ladder: six rungs, the sixth repeating the same shutdown coil inside a "
                   "dashed box.")


# ---------------------------------------------------------------- 13.5 (added)
def fig_13_3():
    """A change sends the lifecycle back to the first affected phase."""
    o = [_txt(330, 20, "Một thay đổi kéo cả vòng đời quay lại pha đầu tiên bị ảnh hưởng", 8.2,
              weight="600")]

    o.append(_rect(150, 56, 10, 7, PALE_BLUE, sw=1.0, stroke=EDGE))
    o.append(_txt(166, 62, "pha không bị chạm tới", 5.2, color=GREY, anchor="start"))
    o.append(_rect(302, 56, 10, 7, PALE_GOLD, sw=1.0, stroke=EDGE))
    o.append(_txt(318, 62, "pha phải chạy lại", 5.2, color=GREY, anchor="start"))

    phases = ["Đặc tả", "Thiết kế", "Chế tạo", "Lắp đặt", "Thẩm định", "Vận hành"]
    xs = [26 + i * 104 for i in range(6)]
    for i, (x, ph) in enumerate(zip(xs, phases)):
        fill = PALE_GOLD if i >= 1 else PALE_BLUE
        o.append(_rect(x, 74, 92, 36, fill, sw=1.1, stroke=EDGE))
        o.append(_txt(x + 46, 96, ph, 5.8, weight="600"))
        if i < 5:
            o.append(_arrow(x + 93, 92, x + 101, 92, sw=1.0))

    # the change, at the operating end
    o.append(_txt(xs[5] + 46, 128, "thay đổi đề xuất", 5.2, color=DARKRED, weight="600"))

    # back to the first affected phase
    o.append(_path("M %s 136 L %s 136 L %s 176 L %s 176 L %s 118"
                   % (xs[5] + 46, xs[5] + 46, xs[5] + 46, xs[1] + 46, xs[1] + 46),
                   sw=1.2, color=DARKRED, dash="4 3"))
    o.append(_arrow(xs[1] + 46, 118, xs[1] + 46, 114, sw=1.2, color=DARKRED))
    o.append(_txt(330, 192, "quay lại pha đầu tiên mà thay đổi ấy chạm tới", 5.4, color=DARKRED))

    # everything downstream must be re-run
    o.append(_line(xs[1], 208, xs[5] + 92, 208, sw=1.0, color=GREY))
    o.append(_line(xs[1], 208, xs[1], 200, sw=1.0, color=GREY))
    o.append(_line(xs[5] + 92, 208, xs[5] + 92, 200, sw=1.0, color=GREY))
    o.append(_txt(330, 222, "rồi phải chạy lại toàn bộ các pha sau đó — kể cả kiểm chứng và cập nhật "
                            "tài liệu", 5.4, color=GREY))

    o.append(_txt(330, 250, "Không có đường tắt: sửa một tiếp điểm trong logic cũng là sửa thiết kế, và "
                            "thiết kế thì phải được thẩm định lại.", 5.4, color=GREY))

    return _finish(o, 660, 264,
                   "Hình 13-3 (bổ sung). Mọi thay đổi đều đưa vòng đời an toàn trở về pha đầu tiên mà nó "
                   "chạm tới, rồi các pha sau đó phải chạy lại — kể cả kiểm chứng và cập nhật tài liệu. "
                   "Đây là yêu cầu của tiêu chuẩn, nhưng cũng là điều dễ bị coi nhẹ nhất: một tiếp điểm "
                   "thêm vào trông như việc của mười phút, cho tới khi người ta nhớ ra nó là một thay đổi "
                   "thiết kế.",
                   "Figure 13-3 (added). Every change sends the safety lifecycle back to the first phase it "
                   "touches, and every later phase must then be re-run, verification and documentation "
                   "included. This is a requirement of the standard, but it is also the one most easily "
                   "dismissed: adding a contact looks like ten minutes' work, until someone remembers that "
                   "it is a design change.",
                   "Sơ đồ sáu pha của vòng đời nối tiếp nhau, với một mũi tên nét đứt từ pha vận hành "
                   "quay ngược về pha thiết kế và một dấu ngoặc đánh dấu các pha phải chạy lại.",
                   "A six-phase lifecycle chain with a dashed arrow running back from operation to design, "
                   "and a bracket marking the phases that must be re-run.")


FIGURES = [fig_13_1, fig_13_2, fig_13_3]
