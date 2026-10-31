# -*- coding: utf-8 -*-
"""Safety Instrumented Systems, Chapter 10 — Engineering a System."""
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


# ---------------------------------------------------------------- 10.1
def fig_10_1():
    """The software V-model: every requirement has a matching verification step."""
    o = [_txt(330, 20, "Mô hình V của phát triển phần mềm", 8.2, weight="600")]

    left = [(112, 62, "Yêu cầu phần mềm"),
            (150, 112, "Kiến trúc phần mềm"),
            (188, 162, "Thiết kế chi tiết")]
    right = [(548, 62, "Kiểm tra chấp nhận"),
             (510, 112, "Kiểm tra tích hợp"),
             (472, 162, "Kiểm tra đơn vị")]

    for (lx, ly, lt), (rx, ry, rt) in zip(left, right):
        o.append(_rect(lx - 62, ly - 14, 124, 28, PALE_BLUE, sw=1.0))
        o.append(_txt(lx, ly + 2.6, lt, 6.2, weight="600"))
        o.append(_rect(rx - 62, ry - 14, 124, 28, PALE_GREEN, sw=1.0))
        o.append(_txt(rx, ry + 2.6, rt, 6.2, weight="600"))
        o.append(_arrow(lx + 64, ly, rx - 64, ry, sw=0.9, color=GREY, dash="4 3"))

    o.append(_rect(252, 208, 126, 30, PALE_GOLD, sw=1.1))
    o.append(_txt(315, 226, "Lập trình", 6.6, weight="600"))

    o.append(_line(40, 208, 40, 48, sw=1.1))
    o.append(_line(620, 208, 620, 48, sw=1.1))
    for y in (62, 112, 162):
        o.append(_line(40, y, 50, y, sw=1.1))
        o.append(_line(610, y, 620, y, sw=1.1))
    o.append(_line(40, 208, 252, 208, sw=1.1))
    o.append(_line(378, 208, 620, 208, sw=1.1))
    for x in (40, 620):
        o.append(_arrow(x, 60, x, 46, sw=1.1, color=INK))

    o.append(_txt(330, 268, "Mỗi khối bên trái là một cam kết; mỗi khối bên phải là cách chứng minh "
                            "cam kết ấy đã được giữ.", 6.2, color=GREY))
    o.append(_txt(330, 284, "Mũi tên nét đứt là đường kiểm chứng — nó phải tồn tại trước khi viết dòng "
                            "mã đầu tiên.", 6.2, color=GREY))
    return _finish(o, 660, 300,
                   "Hình 10-1. Mô hình V. Trục trái đi xuống từ yêu cầu tới mã; trục phải đi lên từ "
                   "kiểm tra đơn vị tới kiểm tra chấp nhận. Điểm mấu chốt không phải hình chữ V mà là "
                   "những đường nét đứt: mỗi bước kiểm tra phải được thiết kế trước bước viết mã tương "
                   "ứng, nếu không thì nó chỉ là việc kiểm tra lại điều mình vừa làm.",
                   "Figure 10-1. The V-model. The left leg descends from requirements to code; the right "
                   "leg climbs from unit test to acceptance test. The point is not the shape but the "
                   "dashed links: each verification step has to be designed before the corresponding "
                   "coding step, or it is only a check on what you just did.",
                   "Mô hình chữ V: bên trái là yêu cầu, kiến trúc, thiết kế chi tiết xuống tới lập "
                   "trình; bên phải là kiểm tra đơn vị, tích hợp, chấp nhận đi lên, nối bằng các đường "
                   "kiểm chứng nét đứt.",
                   "A V-model: requirements, architecture and detailed design descend on the left to "
                   "coding; unit, integration and acceptance testing climb on the right, joined by "
                   "dashed verification links.")


# ---------------------------------------------------------------- 10.2
def fig_10_2():
    """Energise-to-trip versus de-energise-to-trip, and why inverting is not enough."""
    o = [_txt(330, 20, "Cắt bằng ngắt điện và cắt bằng cấp điện: hai thiết kế khác nhau", 8.2,
              weight="600")]

    o.append(_rect(30, 40, 290, 214, "#fbfaf7", sw=1.0))
    o.append(_txt(175, 58, "Bình thường CÓ điện · cắt bằng ngắt điện", 6.6, weight="600"))
    o.append(_txt(175, 72, "trạng thái khoẻ mạnh = 1", 5.8, color=GREY))

    rows_l = [("Bình thường", "1", "đang chạy", GREEN),
              ("Hư hỏng an toàn", "0", "cắt — đúng chiều an toàn", GOLD),
              ("Mất nguồn / đứt dây", "0", "cắt — đúng chiều an toàn", GOLD),
              ("Hư hỏng nguy hiểm", "1 (kẹt)", "không cắt — phải thử mới thấy", DARKRED)]
    for i, (a, b, c, col) in enumerate(rows_l):
        y = 96 + i * 46
        o.append(_circle(48, y - 3, 3.0, fill=col, sw=0.6))
        o.append(_txt(60, y, a, 6.0, anchor="start"))
        o.append(_txt(60, y + 12, c, 5.6, anchor="start", color=GREY))
        o.append(_rect(258, y - 10, 46, 16, "#fff", sw=0.8, stroke=EDGE))
        o.append(_txt(281, y + 1.6, b, 6.4, weight="600", color=col))

    o.append(_rect(340, 40, 290, 214, "#fbfaf7", sw=1.0))
    o.append(_txt(485, 58, "Bình thường KHÔNG điện · cắt bằng cấp điện", 6.6, weight="600"))
    o.append(_txt(485, 72, "trạng thái khoẻ mạnh = 0", 5.8, color=GREY))

    rows_r = [("Bình thường", "0", "đang chạy", GREEN),
              ("Hư hỏng an toàn", "1", "cắt nhầm — nhưng vẫn an toàn", GOLD),
              ("Mất nguồn / đứt dây", "0", "trông y như bình thường", DARKRED),
              ("Hư hỏng nguy hiểm", "0", "không cắt — và không ai biết", DARKRED)]
    for i, (a, b, c, col) in enumerate(rows_r):
        y = 96 + i * 46
        o.append(_circle(358, y - 3, 3.0, fill=col, sw=0.6))
        o.append(_txt(370, y, a, 6.0, anchor="start"))
        o.append(_txt(370, y + 12, c, 5.6, anchor="start", color=GREY))
        o.append(_rect(568, y - 10, 46, 16, "#fff", sw=0.8, stroke=EDGE))
        o.append(_txt(591, y + 1.6, b, 6.4, weight="600", color=col))

    o.append(_txt(330, 280, "Đảo logic chỉ đổi bảng chân trị, không đổi hành vi khi hỏng: ở cột phải, "
                            "mất nguồn trùng với trạng thái khoẻ mạnh.", 6.2, color=GREY))
    return _finish(o, 660, 298,
                   "Hình 10-2 (bổ sung). Hai chiều thiết kế. Bên trái, mọi hư hỏng đều đẩy hệ về phía "
                   "cắt — an toàn, nhưng cắt nhầm nhiều lần. Bên phải, hư hỏng an toàn cũng gây cắt nhầm, "
                   "nhưng hư hỏng nguy hiểm và mất nguồn đều đẩy hệ về 0, trùng với trạng thái khoẻ mạnh; "
                   "vì thế chốt, cầu chì báo hỏng và giám sát đường dây là bắt buộc chứ không phải tuỳ chọn, "
                   "để phân biệt “không có điện vì bình thường” với “không có điện vì hỏng”.",
                   "Figure 10-2 (added). The two design directions. On the left, every failure pushes the "
                   "system toward a trip — safe, but noisy. On the right, a safe failure still causes a "
                   "spurious trip, but dangerous failures and loss of power both leave the output at 0, "
                   "identical to the healthy state — which is why latching, alarm fuses and line monitoring "
                   "are mandatory rather than optional.",
                   "Hai bảng so sánh: hệ bình thường có điện và hệ bình thường không điện, mỗi bảng bốn "
                   "trạng thái và mã logic tương ứng.",
                   "Two comparison tables: normally energised and normally de-energised, four states each "
                   "with the corresponding logic value.")


FIGURES = [fig_10_1, fig_10_2]
