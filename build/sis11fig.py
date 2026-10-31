# -*- coding: utf-8 -*-
"""Safety Instrumented Systems, Chapter 11 — Installing a System."""
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
    """Text rotated 90 degrees anticlockwise about (x, y)."""
    return ('<text x="%s" y="%s" text-anchor="middle" transform="rotate(-90 %s %s)" '
            'style="font:%spx Inter,Helvetica,sans-serif;fill:%s;">%s</text>'
            % (x, y, x, y, size, color, s))


def _wrap(s, n):
    """Greedy word wrap at n characters."""
    out, cur = [], ""
    for w in s.split():
        if not cur:
            cur = w
        elif len(cur) + 1 + len(w) <= n:
            cur += " " + w
        else:
            out.append(cur)
            cur = w
    if cur:
        out.append(cur)
    return out


# ---------------------------------------------------------------- 11.1-11.6
def fig_11_1():
    """Four gates between design and operation; each proves something different."""
    o = [_txt(330, 20, "Bốn cổng kiểm tra: mỗi cổng chứng minh một thứ khác nhau", 8.2,
              weight="600")]

    # the path
    o.append(_line(40, 138, 622, 138, sw=1.3))
    o.append(_arrow(614, 138, 632, 138, sw=1.3))

    gates = [
        (135, "FAT", "§11.3",
         "Phần cứng và phần mềm rời xưởng đúng đặc tả",
         "Không nói gì về đấu dây tại hiện trường"),
        (285, "Kiểm tra lắp đặt", "§11.4.1",
         "Đấu dây, ghi nhãn và hiệu chuẩn đúng bản vẽ",
         "Chưa cấp điện, logic chưa hề chạy"),
        (435, "SAT / Thẩm định", "§11.5",
         "Hệ đạt đặc tả yêu cầu an toàn, từng chức năng",
         "Không thay được con mắt của người ngoài"),
        (565, "FSA / PSSR", "§11.6",
         "Phán xét dựa trên bằng chứng, có người ngoài nhóm thiết kế",
         "Không sửa được thiếu sót nằm trong thiết kế"),
    ]

    for x, name, ref, proves, notp in gates:
        o.append(_line(x, 112, x, 138, sw=2.6, color=INK))
        o.append(_circle(x, 138, 3.2, fill=INK, sw=0.6))
        o.append(_txt(x, 84, name, 6.3, weight="600"))
        o.append(_txt(x, 98, ref, 5.4, color=GREY))

        y = 180
        o.append(_txt(x, y, "CHỨNG MINH", 5.0, color="#2f6b3a", weight="600"))
        for ln in _wrap(proves, 30):
            y += 11
            o.append(_txt(x, y, ln, 5.4))
        y += 20
        o.append(_txt(x, y, "KHÔNG CHỨNG MINH", 5.0, color="#8a5a4a", weight="600"))
        for ln in _wrap(notp, 30):
            y += 11
            o.append(_txt(x, y, ln, 5.4, color=GREY))

    work = [(87, "thiết kế, chế tạo"), (210, "lắp đặt"), (360, "chạy thử chức năng"),
            (500, "khắc phục khiếm khuyết"), (598, "khởi động")]
    for x, s in work:
        o.append(_txt(x, 156, s, 5.4, color=GREY))

    return _finish(o, 660, 258,
                   "Hình 11-1. Bốn cổng trên đường từ thiết kế tới vận hành. Mỗi cổng trả lời một câu "
                   "hỏi khác nhau, và không cổng nào thay được cổng kia: FAT kiểm phần cứng và phần mềm "
                   "trước khi rời xưởng, kiểm tra lắp đặt kiểm đấu dây và hiệu chuẩn khi chưa cấp điện, "
                   "SAT thẩm định hệ đã lắp, FSA/PSSR là phán xét độc lập cuối cùng trước khi có nguy hiểm.",
                   "Figure 11-1. Four gates between design and operation. Each gate answers a different "
                   "question and none substitutes for another: FAT checks hardware and software before "
                   "shipment, installation checks verify wiring and calibration before power is applied, "
                   "SAT validates the installed system, and FSA/PSSR is the independent judgement made "
                   "before hazards are introduced.",
                   "Sơ đồ bốn cổng kiểm tra nối tiếp nhau trên một đường ngang, mỗi cổng ghi điều nó "
                   "chứng minh và điều nó không chứng minh.",
                   "A diagram of four sequential verification gates on a horizontal path, each annotated "
                   "with what it proves and what it does not.")


# ---------------------------------------------------------------- 11.3
def fig_11_3():
    """The FAT bench: field devices simulated at the vendor's works."""
    o = [_txt(330, 20, "Bàn thử FAT: giả lập thiết bị trường ngay tại xưởng chế tạo", 8.2,
              weight="600")]

    o.append(_txt(95, 48, "Giả lập trường", 6.0, weight="600", color=GREY))
    o.append(_txt(600, 48, "Quan sát", 6.0, weight="600", color=GREY))

    # simulated field devices
    sims = [(64, "Công tắc số", "mỗi công tắc là một tiếp điểm"),
            (106, "Chiết áp 4–20 mA", "quay tay để đặt giá trị"),
            (148, "Cặp nhiệt / xung", "bơm tín hiệu milivôn")]
    for y, name, sub in sims:
        o.append(_rect(34, y, 122, 34, PALE_GOLD, sw=1.0, stroke=EDGE))
        o.append(_txt(95, y + 14, name, 5.9, weight="600"))
        o.append(_txt(95, y + 26, sub, 5.0, color=GREY))
        o.append(_arrow(158, y + 17, 196, y + 17, sw=1.0))

    # input module, logic solver, output module
    o.append(_rect(200, 76, 76, 104, PALE_BLUE, sw=1.1, stroke=EDGE))
    o.append(_txt(238, 126, "Mô-đun vào", 5.9, weight="600"))
    o.append(_txt(238, 138, "địa chỉ vật lý", 5.0, color=GREY))

    o.append(_rect(316, 88, 120, 84, "#fff", sw=1.3))
    o.append(_txt(376, 124, "Bộ giải logic", 6.4, weight="600"))
    o.append(_txt(376, 138, "chạy theo sơ đồ nhân quả", 5.0, color=GREY))

    o.append(_rect(476, 76, 76, 104, PALE_BLUE, sw=1.1, stroke=EDGE))
    o.append(_txt(514, 126, "Mô-đun ra", 5.9, weight="600"))
    o.append(_txt(514, 138, "rơ-le / 4–20 mA", 5.0, color=GREY))

    o.append(_arrow(278, 130, 312, 130, sw=1.1))
    o.append(_arrow(438, 130, 472, 130, sw=1.1))

    # output lamps
    o.append(_rect(566, 76, 66, 104, PALE_GREEN, sw=1.1, stroke=EDGE))
    o.append(_txt(599, 90, "Đèn báo", 5.9, weight="600"))
    for i, yy in enumerate((112, 132, 152)):
        o.append(_circle(599, yy, 5.0, fill="#fff", sw=1.1))
        o.append(_txt(599, yy + 2, str(i + 1), 5.0, color=GREY))
    o.append(_arrow(554, 130, 564, 130, sw=1.1))

    # the automated alternative
    o.append(_rect(300, 214, 152, 44, "#fff", sw=1.0, dash="4 3", stroke=GREY))
    o.append(_txt(376, 232, "PC: kịch bản thử", 5.9, weight="600"))
    o.append(_txt(376, 244, "chạy nhanh hơn và tự ghi biên bản", 5.0, color=GREY))
    o.append(_arrow(376, 212, 376, 174, sw=1.0, dash="4 3", color=GREY))

    o.append(_txt(330, 278, "Người thử bấm công tắc và quay chiết áp, rồi so đèn báo với sơ đồ nhân quả.",
                  5.6, color=GREY))

    return _finish(o, 660, 292,
                   "Hình 11-3. Bàn thử FAT. Các thiết bị trường được thay bằng công tắc, chiết áp và cặp "
                   "nhiệt, mỗi thứ dán nhãn đúng như thiết bị thật; đèn báo thay cho cơ cấu chấp hành. "
                   "Toàn bộ hệ — kể cả mô-đun vào ra — được đấu thử trước khi xuống công trường. Đường "
                   "nét đứt là cách làm tự động: PC chạy kịch bản và tự ghi biên bản.",
                   "Figure 11-3. The FAT bench. Field devices are replaced by switches, potentiometers and "
                   "thermocouples, each labelled exactly as the real instrument; lamps stand in for the "
                   "final elements. The whole system, I/O modules included, is wired and exercised before "
                   "it leaves the works. The dashed path is the automated alternative, with a PC running "
                   "the script and writing the record itself.",
                   "Sơ đồ bàn thử FAT: thiết bị giả lập bên trái, mô-đun vào, bộ giải logic và mô-đun ra ở "
                   "giữa, đèn báo bên phải, và một PC chạy kịch bản thử nối vào bộ giải logic.",
                   "A FAT bench schematic: simulated field devices on the left, input module, logic solver "
                   "and output module in the middle, indicator lamps on the right, and a PC running the "
                   "test script connected to the logic solver.")


# ---------------------------------------------------------------- 11.2
def fig_11_2():
    """Verification, validation, FSA and PSSR: what each one actually covers."""
    o = [_txt(330, 20, "Kiểm chứng, thẩm định, đánh giá an toàn: ba phạm vi khác nhau", 8.2,
              weight="600")]

    # lane 1 — verification, phase by phase
    o.append(_txt(24, 80, "KIỂM CHỨNG", 6.3, anchor="start", weight="600"))
    o.append(_txt(24, 92, "từng pha, từng bước", 5.2, anchor="start", color=GREY))
    phases = ["Đặc tả", "Thiết kế", "Chế tạo", "Lắp đặt", "Vận hành"]
    for i, ph in enumerate(phases):
        x = 200 + i * 86
        o.append(_rect(x, 66, 82, 24, PALE_BLUE, sw=1.0, stroke=EDGE))
        o.append(_txt(x + 41, 81.5, ph, 5.6))

    # lane 2 — validation, once, for the whole system
    o.append(_txt(24, 148, "THẨM ĐỊNH", 6.3, anchor="start", weight="600"))
    o.append(_txt(24, 160, "một phần của kiểm chứng;", 5.2, anchor="start", color=GREY))
    o.append(_txt(24, 170, "không phải một pha", 5.2, anchor="start", color=GREY))
    o.append(_rect(200, 136, 426, 24, PALE_GREEN, sw=1.0, dash="5 3", stroke=EDGE))
    o.append(_txt(413, 151.5, "so cả hệ với đặc tả yêu cầu an toàn — một lần, không lặp theo pha", 5.6))

    # lane 3 — functional safety assessment / PSSR
    o.append(_txt(24, 216, "ĐÁNH GIÁ AN TOÀN", 6.3, anchor="start", weight="600"))
    o.append(_txt(24, 228, "phán xét độc lập, dựa trên bằng chứng", 5.2, anchor="start", color=GREY))
    o.append(_rect(200, 204, 240, 24, PALE_GOLD, sw=1.0, stroke=EDGE))
    o.append(_txt(320, 219.5, "đánh giá chức năng an toàn (FSA)", 5.6))
    o.append(_rect(452, 204, 174, 24, PALE_GOLD, sw=1.0, stroke=EDGE))
    o.append(_txt(539, 219.5, "PSSR", 5.9, weight="600"))

    # the equality bracket between FSA's final instance and PSSR
    o.append(_line(320, 232, 320, 240, sw=0.9, dash="3 2", color=GREY))
    o.append(_line(320, 240, 539, 240, sw=0.9, dash="3 2", color=GREY))
    o.append(_line(539, 240, 539, 232, sw=0.9, dash="3 2", color=GREY))
    o.append(_txt(430, 254, "lần FSA cuối và PSSR là cùng một việc, chỉ khác tên gọi", 5.4, color=GREY))
    o.append(_txt(24, 254, "Nét đứt: việc làm một lần, không phải một pha.", 5.2, anchor="start", color=GREY))

    return _finish(o, 660, 270,
                   "Hình 11-2. Ba phạm vi. Kiểm chứng chạy song song với từng pha của vòng đời và hỏi "
                   "“pha này đã xong đúng chưa”; thẩm định chỉ làm một lần, sau khi lắp đặt, và hỏi “cả hệ "
                   "có đạt đặc tả yêu cầu an toàn không” — nên nó là một phần của kiểm chứng chứ không "
                   "phải từ đồng nghĩa. Đánh giá an toàn là phán xét độc lập; lần cuối cùng của nó ở một "
                   "số nước được gọi là PSSR.",
                   "Figure 11-2. Three scopes. Verification runs alongside every phase of the lifecycle "
                   "and asks whether that phase is finished correctly; validation happens once, after "
                   "installation, and asks whether the whole system meets the safety requirements "
                   "specification — which makes it a part of verification, not a synonym. The functional "
                   "safety assessment is an independent judgement, and its final instance is called the "
                   "PSSR in some countries.",
                   "Ba làn so sánh: kiểm chứng gồm năm ô theo từng pha, thẩm định là một ô dài cho cả hệ, "
                   "và đánh giá an toàn là hai ô, trong đó PSSR là tên gọi khác của lần đánh giá cuối.",
                   "Three comparison lanes: verification as five phase cells, validation as one long cell "
                   "covering the whole system, and the functional safety assessment as two cells, with "
                   "PSSR being another name for the final assessment.")


FIGURES = [fig_11_1, fig_11_2, fig_11_3]
