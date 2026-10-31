# -*- coding: utf-8 -*-
"""Safety Instrumented Systems, Chapter 15 — SIS Design Checklist."""
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

# --- numbers behind figure 15-1 -----------------------------------------
# U.K. Health and Safety Executive, 34 accidents caused by control and
# safety system failures, as reproduced in the source figure.
CAUSES = [
    ("Đặc tả (chức năng và toàn vẹn)", 44),
    ("Thay đổi sau khi chạy thử", 20),
    ("Thiết kế và thực hiện", 15),
    ("Vận hành và bảo trì", 15),
    ("Lắp đặt và chạy thử", 6),
]


def _vtxt(x, y, s, size=7.0, color=GREY):
    """Text rotated 90 degrees anticlockwise about (x, y)."""
    return ('<text x="%s" y="%s" font-size="%s" fill="%s" text-anchor="middle" '
            'transform="rotate(-90 %s %s)">%s</text>' % (x, y, size, color, x, y, s))


def fig_15_1():
    """Where the accidents actually came from."""
    o = [_txt(330, 20, "Nguyên nhân chính của 34 vụ tai nạn do hệ điều khiển và an toàn hỏng",
              8.2, weight="600")]

    x0 = 218          # left edge of the bars
    unit = 7.6        # pixels per percent
    base = 50

    for i, (label, pct) in enumerate(CAUSES):
        y = 62 + i * 38
        # the two largest causes are both user activities
        fill = "#f0d3cd" if i < 2 else "#dde5ef"
        stroke = DARKRED if i < 2 else "#8fa6bf"
        o.append(_txt(x0 - 10, y + 4, label, 6.0, anchor="end",
                      color=INK if i < 2 else GREY,
                      weight="600" if i < 2 else ""))
        o.append(_rect(x0, y - 9, pct * unit, 18, fill, sw=1.1, stroke=stroke))
        o.append(_txt(x0 + pct * unit + 8, y + 4, "%d %%" % pct, 6.4, anchor="start",
                      color=DARKRED if i < 2 else GREY, weight="600"))

    # the axis
    o.append(_line(x0, base, x0, 244, sw=1.2, color=INK))
    o.append(_line(x0, 244, x0 + 320, 244, sw=1.2, color=INK))
    for v in (0, 10, 20, 30, 40):
        x = x0 + v * unit
        o.append(_line(x, 244, x, 249, sw=1.0))
        o.append(_txt(x, 259, "%d" % v, 5.4, color=GREY))
    o.append(_txt(x0 + 160, 272, "phần trăm số vụ tai nạn", 5.4, color=GREY))

    o.append(_txt(330, 296, "Hai nhóm lớn nhất — 64 % — đều là hoạt động của chính người sử dụng: "
                            "viết đặc tả và quản lý thay đổi. Đó chính là hai chỗ mà danh sách kiểm "
                            "tra này nhắm tới.", 5.4, color=GREY))

    return _finish(o, 660, 310,
                   "Hình 15-1. Nguyên nhân chính gây tai nạn, theo pha thiết kế, do Cơ quan An toàn và "
                   "Sức khoẻ lao động Anh (HSE) công bố. HSE xem xét 34 vụ tai nạn là hậu quả trực tiếp "
                   "của việc hệ điều khiển và hệ an toàn bị hỏng. 44 % số vụ bắt nguồn từ đặc tả sai hoặc "
                   "thiếu (cả đặc tả chức năng lẫn đặc tả mức toàn vẹn), và 20 % từ những thay đổi được "
                   "thực hiện sau khi chạy thử. Cộng lại, 64 % số vụ nằm ở phía người sử dụng — không phải "
                   "ở thiết bị.",
                   "Figure 15-1. Primary accident cause by design phase, as published by the U.K. Health "
                   "and Safety Executive. The HSE reviewed 34 accidents that were the direct result of "
                   "control and safety system failures. Forty-four percent were due to incorrect or "
                   "incomplete specifications, functional and integrity alike, and 20 % to changes made "
                   "after commissioning. Together, 64 % of the accidents sit on the user's side of the "
                   "fence, not the equipment's.",
                   "Biểu đồ cột ngang: năm nguyên nhân tai nạn theo phần trăm, dẫn đầu là đặc tả 44 phần "
                   "trăm và thay đổi sau chạy thử 20 phần trăm.",
                   "A horizontal bar chart of five accident causes by percentage, led by specification at "
                   "44 percent and changes after commissioning at 20 percent.")


FIGURES = [fig_15_1]
