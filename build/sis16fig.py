# -*- coding: utf-8 -*-
"""Safety Instrumented Systems, Chapter 16 — Case Study."""
from vfig import (BLUE, GOLD, GREEN, GREY, INK, PAPER, RED, _arrow, _box,
                  _circle, _ellipse, _line, _path, _poly, _rect, _txt)
from pcfig import _finish

DARKRED = "#7f1d1d"
AMBER = "#f6e0b8"
PALE_GREEN = "#dcecdc"
PALE_RED = "#f3d6d2"
PALE_BLUE = "#e8eef6"
PALE_GOLD = "#f7efdd"
EDGE = "#b9b3a4"
SIG = "3 2.5"          # dash pattern for signal lines


# ------------------------------------------------------------------ helpers
def _valve(x, y, color=INK, fill="#fff"):
    """A bow-tie valve body centred on (x, y); returns a list."""
    return [_poly([(x - 12, y - 7), (x, y), (x - 12, y + 7)], fill=fill, sw=1.1,
                  color=color, close=True),
            _poly([(x, y), (x + 12, y + 7), (x + 12, y - 7)], fill=fill, sw=1.1,
                  color=color, close=True)]


def _actuator(cx, vy, color=INK):
    """A diaphragm actuator sitting on a valve whose centre is (cx, vy)."""
    return [_rect(cx - 10, vy - 19, 20, 12, "#fff", sw=1.1, stroke=color)]


def _handvalve(x, y, color=INK):
    """A manual gate valve: bow-tie plus hand-wheel bar."""
    out = _valve(x, y, color=color)
    out.append(_line(x, y - 7, x, y - 13, sw=1.0, color=color))
    out.append(_line(x - 5, y - 13, x + 5, y - 13, sw=1.2, color=color))
    return out


def _bubble(x, y, tag, num="", r=9, color=INK, fill="#fff", size=4.8):
    """A field instrument bubble. With a number, the circle is divided."""
    out = [_circle(x, y, r, fill=fill, sw=1.1, color=color)]
    if num:
        out.append(_line(x - r * 0.72, y + 1.4, x + r * 0.72, y + 1.4, sw=0.55, color=color))
        out.append(_txt(x, y - 1.0, tag, size, color=color, weight="600"))
        out.append(_txt(x, y + r - 1.6, num, size - 0.4, color=color, weight="600"))
    else:
        out.append(_txt(x, y + 1.6, tag, size, color=color, weight="600"))
    return out


def _ctrl(x, y, tag, w=34, h=20, color=INK, fill="#fff", size=4.9):
    """A panel-mounted function block (controller, alarm, logic)."""
    return [_rect(x, y, w, h, fill, sw=1.1, stroke=color),
            _txt(x + w / 2.0, y + h / 2.0 + 1.7, tag, size, color=color, weight="600")]


def _coil(x0, x1, y, amp=5, n=7):
    """A furnace coil pass drawn as a zigzag between two wall points."""
    pts = [(x0, y)]
    for i in range(1, n):
        pts.append((x0 + (x1 - x0) * i / float(n), y + (amp if i % 2 else -amp)))
    pts.append((x1, y))
    return _poly(pts, fill="none", sw=1.0, color=INK)


def _flame(x, y, h=24, w=7):
    d = ("M %g %g C %g %g, %g %g, %g %g C %g %g, %g %g, %g %g Z"
         % (x, y,
            x - w, y - h * 0.45, x - w * 0.62, y - h * 0.84, x, y - h,
            x + w * 0.62, y - h * 0.84, x + w, y - h * 0.45, x, y))
    return _path(d, fill=PALE_GOLD, sw=1.0, color=GOLD)


def _vtxt(x, y, s, size=7.0, color=GREY, weight=""):
    w = ' font-weight="%s"' % weight if weight else ""
    return ('<text x="%s" y="%s" font-size="%s" fill="%s" text-anchor="middle"%s '
            'transform="rotate(-90 %s %s)">%s</text>' % (x, y, size, color, w, x, y, s))


# ------------------------------------------------------------------ 16.2 / 16.3
def _pid(o, sis=False):
    """The fired heater with its basic process controls.

    With sis=True the safety instrumented functions of figure 16-3 are
    overlaid in dark red on top of the same geometry, so the two drawings
    can be compared element by element.
    """
    r = DARKRED if sis else INK

    # ---- fired heater
    o.append(_poly([(518, 54), (510, 26), (556, 26), (548, 54)], fill="#fff", sw=1.2,
                   close=True))
    o.append(_rect(460, 54, 130, 206, "#fff", sw=1.2, stroke=INK))
    o.append(_txt(525, 72, "BUỒNG ĐỐT", 5.0, color=GREY, weight="600"))
    o.append(_coil(460, 590, 96))
    o.append(_coil(460, 590, 144))
    o.append(_line(590, 96, 590, 144, sw=1.2))
    o.append(_line(460, 210, 590, 210, sw=1.0))
    for fx in (484, 523, 562):
        o.append(_flame(fx, 210, h=22))

    # ---- feed, two passes
    o.append(_txt(34, 116, "FEED", 5.2, anchor="start", weight="600"))
    o.append(_line(66, 120, 110, 120, sw=1.2))
    o.append(_line(110, 96, 110, 144, sw=1.2))
    o.append(_line(110, 96, 460, 96, sw=1.2))
    o.append(_line(110, 144, 460, 144, sw=1.2))

    o.extend(_bubble(182, 96, "FT", "10"))
    o.extend(_valve(280, 96))
    o.extend(_actuator(280, 96))
    o.extend(_ctrl(232, 50, "FC-10", 36, 20))
    o.append(_path("M 232 60 L 182 60 L 182 87", sw=0.8, color=GREY, dash=SIG))
    o.append(_path("M 268 60 L 280 60 L 280 77", sw=0.8, color=GREY, dash=SIG))

    o.extend(_bubble(182, 144, "FT", "9"))
    o.extend(_valve(280, 144))
    o.extend(_actuator(280, 144))
    o.extend(_ctrl(206, 170, "FC-9", 36, 20))
    o.append(_path("M 206 180 L 182 180 L 182 153", sw=0.8, color=GREY, dash=SIG))
    o.append(_path("M 242 180 L 300 180 L 300 131 L 290 131", sw=0.8, color=GREY, dash=SIG))

    # ---- outlet
    o.append(_line(590, 120, 654, 120, sw=1.2))
    o.append(_arrow(644, 120, 654, 120, sw=1.2))
    o.extend(_bubble(610, 120, "TT", "8"))
    o.extend(_ctrl(593, 76, "TC-8", 34, 20))
    o.append(_path("M 610 96 L 610 111", sw=0.8, color=GREY, dash=SIG))
    o.append(_txt(650, 112, "OUTLET", 5.2, anchor="end", weight="600"))

    # ---- pilot gas, rising into the burner floor
    o.append(_txt(34, 290, "PILOT GAS", 5.2, anchor="start", weight="600"))
    o.append(_line(66, 296, 488, 296, sw=1.2))
    o.append(_line(488, 296, 488, 260, sw=1.2))
    o.extend(_valve(132, 296))
    o.extend(_actuator(132, 296))
    o.append(_txt(132, 271, "PCV-6", 4.8, color=GREY))
    o.extend(_bubble(206, 296, "PT", "7"))
    o.append(_line(215, 296, 256, 296, sw=1.2))
    o.extend(_ctrl(256, 287, "PI-7", 26, 18, size=4.6))

    # ---- fuel gas through the knockout drum
    o.append(_txt(34, 380, "FUEL GAS", 5.2, anchor="start", weight="600"))
    o.append(_line(66, 386, 118, 386, sw=1.2))
    o.append(_path("M 118 367 Q 147 349 176 367 L 176 410 L 118 410 Z",
                   fill="#fff", sw=1.2))
    o.append(_txt(147, 384, "K.O.", 4.8, color=GREY, weight="600"))
    o.append(_txt(147, 395, "DRUM", 4.8, color=GREY, weight="600"))
    o.append(_line(147, 358, 147, 330, sw=1.2))
    o.append(_line(147, 330, 570, 330, sw=1.2))
    o.append(_line(570, 330, 570, 260, sw=1.2))

    o.append(_line(176, 368, 185, 368, sw=1.0))
    o.extend(_bubble(192, 368, "LG", "1", r=7, size=4.2))
    o.append(_line(176, 388, 205, 388, sw=1.0))
    o.extend(_bubble(212, 388, "LT", "2", r=7, size=4.2))
    o.append(_line(219, 388, 250, 388, sw=1.0))
    o.extend(_ctrl(250, 379, "LI-2", 26, 18, size=4.6))

    o.extend(_bubble(206, 330, "FT", "3"))
    o.extend(_bubble(250, 330, "PT", "4"))
    o.extend(_ctrl(266, 321, "PI-4", 26, 18, size=4.6))
    o.extend(_valve(320, 330))
    o.extend(_actuator(320, 330))
    o.extend(_ctrl(303, 266, "FC-3", 34, 20))
    o.append(_path("M 303 276 L 206 276 L 206 321", sw=0.8, color=GREY, dash=SIG))
    o.append(_path("M 337 276 L 346 276 L 346 317 L 330 317", sw=0.8, color=GREY, dash=SIG))
    o.extend(_bubble(376, 330, "PT", "5"))
    o.extend(_ctrl(394, 321, "PI-5", 26, 18, size=4.6))

    if not sis:
        return

    # ---- the safety instrumented functions of figure 16-3
    o.extend(_bubble(238, 296, "PT", "24", color=DARKRED, fill=PALE_RED))
    o.extend(_bubble(436, 96, "FT", "22", color=DARKRED, fill=PALE_RED))
    o.extend(_bubble(448, 144, "FT", "23", color=DARKRED, fill=PALE_RED))

    for x in (380, 414):
        o.extend(_valve(x, 296, color=DARKRED))
        o.extend(_actuator(x, 296, color=DARKRED))
    for x in (492, 532):
        o.extend(_valve(x, 330, color=DARKRED))
        o.extend(_actuator(x, 330, color=DARKRED))

    # the logic solver
    o.append(_rect(420, 350, 200, 48, PALE_RED, sw=1.3, stroke=DARKRED))
    o.append(_txt(520, 368, "S/D LOGIC YC-20", 5.6, color=DARKRED, weight="600"))
    o.append(_txt(520, 384, "PLC an toàn dư thừa · logic thang", 4.8, color=DARKRED))

    # the hard-wired manual shutdown switch
    o.append(_rect(318, 340, 88, 28, "#fff", sw=1.1, stroke=DARKRED))
    o.append(_txt(362, 353, "HS-21", 5.0, color=DARKRED, weight="600"))
    o.append(_txt(362, 363, "nút dừng tay", 4.2, color=GREY))
    o.append(_path("M 406 354 L 420 354", sw=0.9, color=DARKRED, dash=SIG))

    # signals in
    o.append(_path("M 436 105 L 436 350", sw=0.9, color=DARKRED, dash=SIG))
    o.append(_path("M 448 153 L 448 350", sw=0.9, color=DARKRED, dash=SIG))
    o.append(_path("M 238 305 L 238 314 L 300 314 L 300 384 L 420 384",
                   sw=0.9, color=DARKRED, dash=SIG))

    # signals out to the pilot gas valves
    o.append(_path("M 458 350 L 458 266 L 372 266", sw=0.9, color=DARKRED, dash=SIG))
    o.append(_path("M 380 266 L 380 277", sw=0.9, color=DARKRED, dash=SIG))
    o.append(_path("M 414 266 L 414 277", sw=0.9, color=DARKRED, dash=SIG))

    # signals out to the fuel gas valves
    o.append(_path("M 508 350 L 508 309 L 492 309 L 492 317", sw=0.9, color=DARKRED, dash=SIG))
    o.append(_path("M 508 309 L 532 309 L 532 317", sw=0.9, color=DARKRED, dash=SIG))


def fig_16_2():
    """Fired heater and basic process controls."""
    o = [_txt(330, 18, "Lò nung và các vòng điều khiển điều chỉnh cơ bản", 8.2, weight="600")]
    _pid(o, False)
    o.append(_txt(330, 432, "Cả bốn vòng điều chỉnh ở đây nằm trong BPCS đặt cách lò khoảng 60 m. "
                            "Trong hình chưa có một chức năng an toàn nào.", 5.4, color=GREY))
    return _finish(o, 660, 444,
                   "Hình 16-2. Lò nung và các vòng điều khiển điều chỉnh cơ bản. Dòng liệu vào chia "
                   "làm hai nhánh A và B, mỗi nhánh có một lưu lượng kế và một van điều chỉnh riêng "
                   "(FT-9/FV-9 và FT-10/FV-10) do FC-9 và FC-10 điều khiển. Nhiệt độ đầu ra cuộn "
                   "ống do TT-8 đo và TC-8 điều khiển, ở chế độ cascade với FC-3 trên dòng khí đốt. "
                   "PCV-6 tự điều chỉnh áp suất khí mồi. Khí đốt đi qua bình tách lỏng K.O. trước "
                   "khi vào đầu đốt. Toàn bộ vòng điều chỉnh nằm trong BPCS, cách lò khoảng 60 m.",
                   "Figure 16-2. The fired heater and its basic process controls. The feed splits "
                   "into passes A and B, each with its own flow element and control valve "
                   "(FT-9/FV-9 and FT-10/FV-10) driven by FC-9 and FC-10. Coil outlet temperature "
                   "is measured by TT-8 and controlled by TC-8, cascaded to FC-3 on the fuel gas. "
                   "PCV-6 regulates the pilot gas pressure on its own. Fuel gas passes through the "
                   "K.O. drum before reaching the burners. All of these loops live in the BPCS, "
                   "some 200 feet from the furnace.",
                   "Sơ đồ ống và thiết bị đo của một lò nung: dòng liệu hai nhánh, dòng khí đốt qua "
                   "bình tách lỏng, dòng khí mồi, và các vòng điều chỉnh lưu lượng, nhiệt độ, áp suất.",
                   "A piping and instrument diagram of a fired heater: two feed passes, a fuel gas "
                   "line through a knockout drum, a pilot gas line, and the flow, temperature and "
                   "pressure control loops.")


def fig_16_3():
    """The same P&ID with the proposed SIFs overlaid."""
    o = [_txt(330, 18, "Các chức năng an toàn được đề xuất, chồng lên sơ đồ cũ", 8.2, weight="600")]
    o.append(_rect(36, 40, 9, 7, PALE_RED, sw=1.0, stroke=DARKRED))
    o.append(_txt(50, 46, "hạng mục SIS thêm vào", 5.0, color=GREY, anchor="start"))
    o.append(_rect(36, 54, 9, 7, "#fff", sw=1.0, stroke=INK))
    o.append(_txt(50, 60, "hạng mục BPCS sẵn có", 5.0, color=GREY, anchor="start"))
    _pid(o, True)
    o.append(_txt(330, 432, "Ba cảm biến mới và bốn van cắt mới đều nối về một bộ logic riêng, "
                            "tách khỏi BPCS; đường nét đứt là tín hiệu, không phải đường ống.",
                  5.4, color=GREY))
    return _finish(o, 660, 444,
                   "Hình 16-3. Các chức năng an toàn được đề xuất, vẽ chồng lên sơ đồ ống và thiết "
                   "bị của hình 16-2. Ba cảm biến mới — FT-22 và FT-23 trên hai nhánh liệu, PT-24 "
                   "trên dòng khí mồi — đưa vào bộ logic cắt YC-20; bộ logic này đóng bốn van cắt: "
                   "XV-30A/B trên dòng khí mồi và XV-31A/B trên dòng khí đốt. HS-21 là nút dừng tay "
                   "đi dây cứng, độc lập với hệ khả trình. Toàn bộ hạng mục SIS vẽ bằng màu đỏ.",
                   "Figure 16-3. The proposed safety instrumented functions, drawn over the piping "
                   "and instrument diagram of figure 16-2. Three new transmitters — FT-22 and FT-23 "
                   "on the two feed passes, PT-24 on the pilot gas — feed a shutdown logic block "
                   "YC-20, which closes four trip valves: XV-30A/B on the pilot gas and XV-31A/B on "
                   "the fuel gas. HS-21 is a hard-wired manual shutdown switch, independent of the "
                   "programmable system. Everything added by the SIS is drawn in red.",
                   "Sơ đồ ống và thiết bị của lò nung có chồng thêm ba cảm biến, một bộ logic cắt và "
                   "bốn van cắt, tất cả vẽ màu đỏ.",
                   "A piping and instrument diagram of the fired heater with three transmitters, a "
                   "shutdown logic block and four trip valves overlaid in red.")


# ---------------------------------------------------------------- 16.2 lifecycle
def fig_16_1():
    """Three phases, one continuous management thread."""
    o = [_txt(330, 20, "Ba pha của vòng đời, và một sợi chỉ chạy suốt cả ba", 8.2, weight="600")]

    # the vertical thread on the left
    o.append(_rect(36, 56, 62, 294, PALE_BLUE, sw=1.1, stroke="#8fa6bf"))
    o.append(_vtxt(56, 203, "Quản lý an toàn chức năng", 6.2, color=INK, weight="600"))
    o.append(_vtxt(80, 203, "lập kế hoạch · kiểm chứng", 5.4, color=GREY))

    phases = [
        ("Pha phân tích rủi ro", [
            "Phân tích mối nguy quá trình",
            "Nhận diện các chức năng an toàn (SIF)",
            "Xác định mức toàn vẹn an toàn (SIL)",
            "Lập đặc tả yêu cầu an toàn (SRS)",
        ], 56, 88),
        ("Pha thiết kế và thực hiện", [
            "Thiết kế khái niệm SIS",
            "Tính kiểm chứng SIL",
            "Thiết kế chi tiết SIS",
            "Lắp đặt và chạy thử SIS",
        ], 164, 88),
        ("Pha vận hành và bảo trì", [
            "Vận hành SIS",
            "Bảo trì SIS",
            "Sửa đổi",
        ], 272, 78),
    ]
    for title, items, y, h in phases:
        o.append(_rect(116, y, 508, h, "#fff", sw=1.2, stroke=INK))
        o.append(_rect(116, y, 508, 20, PALE_GOLD, sw=1.2, stroke=INK))
        o.append(_txt(370, y + 14, title, 6.6, weight="600"))
        for i, it in enumerate(items):
            o.append(_txt(134, y + 34 + i * 13, "– " + it, 5.6, anchor="start", color="#333"))

    o.append(_arrow(370, 148, 370, 162, sw=1.3))
    o.append(_arrow(370, 256, 370, 270, sw=1.3))

    o.append(_txt(330, 370, "Sợi chỉ bên trái không phải một pha thứ tư: nó là công việc phải làm trong "
                            "suốt cả ba pha — và là phần hay bị cắt trước tiên khi tiến độ gấp.",
                  5.4, color=GREY))

    return _finish(o, 660, 382,
                   "Hình 16-1. Các pha của vòng đời an toàn. Ba pha nối tiếp nhau — phân tích rủi ro, "
                   "thiết kế và thực hiện, vận hành và bảo trì — nhưng công việc quản lý an toàn chức năng, "
                   "lập kế hoạch vòng đời và kiểm chứng thì chạy song song với cả ba, như khối dọc bên trái. "
                   "Đây là bản giản lược của vòng đời trong ANSI/ISA-84.00.01-2004.",
                   "Figure 16-1. The safety lifecycle phases. Three phases run in sequence — risk analysis, "
                   "design and implementation, operation and maintenance — but functional safety "
                   "management, lifecycle planning and verification run alongside all three, as the vertical "
                   "block on the left indicates. This is a simplified version of the lifecycle in "
                   "ANSI/ISA-84.00.01-2004.",
                   "Sơ đồ ba pha vòng đời xếp dọc, bên trái là một khối dọc cho công việc quản lý an toàn "
                   "chức năng chạy song song.",
                   "A diagram of three lifecycle phases stacked vertically, with a vertical block on the "
                   "left for functional safety management running alongside.")


# ---------------------------------------------------------------- 16.4 / 16.5
def fig_16_4():
    """The proposed SIS, at the block level."""
    o = [_txt(330, 20, "Thiết kế khái niệm: ba nhóm cảm biến, một PLC an toàn, hai cặp van", 8.2,
              weight="600")]

    lx, lw = 30, 176
    mx, mw = 240, 168
    rx, rw = 452, 178

    left = [
        ("FT-22", "lưu lượng dòng A", "1 cảm biến", 60),
        ("FT-23", "lưu lượng dòng B", "1 cảm biến", 122),
        ("PT-7 & PT-24", "áp suất khí mồi", "1oo2", 184),
    ]
    right = [
        ("XV-30A/B", "van cắt khí mồi", "1oo2", 74),
        ("XV-31A/B", "van cắt khí đốt", "1oo2", 174),
    ]

    for tag, desc, red, y in left:
        o.append(_rect(lx, y, lw, 50, PALE_BLUE, sw=1.1, stroke="#8fa6bf"))
        o.append(_txt(lx + lw / 2, y + 19, tag, 6.4, weight="600"))
        o.append(_txt(lx + lw / 2, y + 32, desc, 5.4, color=GREY))
        o.append(_txt(lx + lw / 2, y + 43, red, 5.2, color=DARKRED))
        o.append(_arrow(lx + lw + 2, y + 25, mx - 2, y + 25, sw=1.2))

    o.append(_rect(mx, 60, mw, 178, "#fff", sw=1.3, stroke=INK))
    o.append(_txt(mx + mw / 2, 108, "PLC an toàn dư thừa", 6.4, weight="600"))
    o.append(_txt(mx + mw / 2, 126, "đã được chứng nhận", 5.4, color=GREY))
    o.append(_txt(mx + mw / 2, 144, "đặt trong toà nhà điều khiển", 5.2, color=GREY))
    o.append(_txt(mx + mw / 2, 162, "logic thang", 5.2, color=GREY))
    o.append(_line(mx + 14, 178, mx + mw - 14, 178, sw=0.8, color=EDGE, dash="4 3"))
    o.append(_txt(mx + mw / 2, 198, "S/D logic YC-20", 5.8, color=DARKRED, weight="600"))

    for tag, desc, red, y in right:
        o.append(_rect(rx, y, rw, 50, PALE_GOLD, sw=1.1, stroke="#c0a878"))
        o.append(_txt(rx + rw / 2, y + 19, tag, 6.4, weight="600"))
        o.append(_txt(rx + rw / 2, y + 32, desc, 5.4, color=GREY))
        o.append(_txt(rx + rw / 2, y + 43, red, 5.2, color=DARKRED))
        o.append(_arrow(mx + mw + 2, y + 25, rx - 2, y + 25, sw=1.2))

    o.append(_txt(330, 258, "Hai chức năng dòng chảy (A và B) cần SIL 2; chức năng áp suất khí mồi cần "
                            "SIL 3, nên chỉ nhóm này có cảm biến và van dự phòng 1oo2.", 5.4, color=GREY))

    return _finish(o, 660, 272,
                   "Hình 16-4. Thiết kế SIS khái niệm được đề xuất. Ba nhóm cảm biến đưa vào một PLC an "
                   "toàn dư thừa, PLC đóng hai cặp van cắt — một cặp cho khí mồi, một cặp cho khí đốt. Chỉ "
                   "nhóm áp suất khí mồi (SIL 3) có dự phòng 1oo2 ở cả cảm biến lẫn van; hai chức năng dòng "
                   "chảy (SIL 2) dùng cảm biến đơn.",
                   "Figure 16-4. The proposed conceptual SIS design. Three sensor groups feed a redundant "
                   "safety PLC, which closes two pairs of trip valves — one pair on pilot gas, one on fuel "
                   "gas. Only the pilot gas pressure group (SIL 3) is 1oo2 at both the sensors and the "
                   "valves; the two pass-flow functions (SIL 2) use single sensors.",
                   "Sơ đồ khối: ba nhóm cảm biến nối vào một PLC an toàn, PLC nối ra hai cặp van cắt.",
                   "A block diagram: three sensor groups into one safety PLC, which drives two pairs of "
                   "trip valves.")


def fig_16_5():
    """The pilot gas shutdown function on its own, with its PFD terms."""
    o = [_txt(330, 20, "Chức năng cắt áp suất thấp khí mồi, tách riêng để tính PFD", 8.2,
              weight="600")]

    o.append(_rect(30, 70, 150, 56, PALE_BLUE, sw=1.1, stroke="#8fa6bf"))
    o.append(_txt(105, 90, "PT-7 & PT-24", 6.4, weight="600"))
    o.append(_txt(105, 104, "bỏ phiếu 1oo2", 5.6, color=DARKRED))
    o.append(_txt(105, 116, "chẩn đoán 90 %", 5.2, color=GREY))
    o.append(_txt(105, 140, "PFD = 6,25 × 10⁻⁶", 5.2, color=DARKRED))

    o.append(_arrow(182, 98, 216, 98, sw=1.2))
    o.append(_rect(218, 70, 138, 56, "#fff", sw=1.2, stroke=INK))
    o.append(_txt(287, 92, "PLC an toàn", 6.4, weight="600"))
    o.append(_txt(287, 106, "dư thừa", 5.6, color=GREY))
    o.append(_txt(287, 118, "PFD theo nhà cung cấp", 5.2, color=GREY))
    o.append(_txt(287, 140, "PFD = 5 × 10⁻⁵", 5.2, color=DARKRED))

    o.append(_line(356, 98, 392, 98, sw=1.2))
    o.append(_line(392, 58, 392, 138, sw=1.2))
    o.append(_arrow(392, 58, 424, 58, sw=1.2))
    o.append(_arrow(392, 138, 424, 138, sw=1.2))

    o.append(_rect(426, 34, 190, 48, PALE_GOLD, sw=1.1, stroke="#c0a878"))
    o.append(_txt(521, 54, "XV-30A/B", 6.4, weight="600"))
    o.append(_txt(521, 68, "van cắt khí mồi · 1oo2", 5.4, color=GREY))

    o.append(_rect(426, 114, 190, 48, PALE_GOLD, sw=1.1, stroke="#c0a878"))
    o.append(_txt(521, 134, "XV-31A/B", 6.4, weight="600"))
    o.append(_txt(521, 148, "van cắt khí đốt · 1oo2", 5.4, color=GREY))

    o.append(_txt(521, 176, "PFD = 2,5 × 10⁻⁴ (cả bốn van)", 5.2, color=DARKRED))

    o.append(_txt(330, 198, "Cả hai nhánh van đều nằm trên đường của cùng một chức năng: mất khí mồi thì "
                            "phải cắt cả khí mồi lẫn khí đốt.", 5.4, color=GREY))
    o.append(_txt(330, 212, "PFD tổng = 6,25×10⁻⁶ + 5×10⁻⁵ + 2,5×10⁻⁴ ≈ 3,06×10⁻⁴ → RRF ≈ 3.300, "
                            "nằm trong dải 1.000–10.000 của SIL 3.", 5.4, color=DARKRED))

    return _finish(o, 660, 224,
                   "Hình 16-5. Sơ đồ khối của chức năng cắt áp suất thấp khí mồi, kèm các số hạng PFD. "
                   "Hai cảm biến bỏ phiếu 1oo2 đưa vào PLC an toàn dư thừa; PLC đóng cả cặp van khí mồi "
                   "lẫn cặp van khí đốt, vì mất khí mồi thì phải cắt cả hai dòng. Vì vậy phép tính PFD "
                   "của chức năng này gồm bốn van, không phải hai. Tổng ba số hạng cho 3,06×10⁻⁴, dưới "
                   "ngưỡng 10⁻³ của SIL 3.",
                   "Figure 16-5. Block diagram for the low pilot gas pressure shutdown function, with its "
                   "PFD terms. Two 1oo2 transmitters feed a redundant safety PLC, and the PLC closes both "
                   "the pilot gas valve pair and the fuel gas valve pair, because losing the pilots "
                   "requires shutting off both streams. The PFD calculation for this function therefore "
                   "covers four valves, not two. The three terms add to 3.06×10⁻⁴, below the 10⁻³ "
                   "threshold for SIL 3.",
                   "Sơ đồ khối: hai cảm biến bỏ phiếu 1oo2 vào một PLC an toàn, PLC đóng hai cặp van song "
                   "song, kèm giá trị PFD của từng khối.",
                   "A block diagram: two 1oo2 transmitters into a safety PLC, which closes two valve pairs "
                   "in parallel, with the PFD of each block shown.")


# ---------------------------------------------------------------- 16.12
def fig_16_6():
    """The trip system as the operator sees it during the quarterly test."""
    o = [_txt(330, 16, "Hệ cắt áp suất thấp khí mồi, nhìn theo góc của người vận hành", 8.2,
              weight="600")]

    # the fire box the two streams feed
    o.append(_rect(572, 56, 80, 212, PALE_GOLD, sw=1.1, stroke="#c0a878"))
    o.append(_vtxt(612, 162, "BUỒNG ĐỐT", 5.6, color=GOLD, weight="600"))

    # ---- pilot gas
    o.append(_txt(34, 98, "PILOT GAS", 5.2, anchor="start", weight="600"))
    o.append(_line(36, 104, 572, 104, sw=1.2))
    o.extend(_valve(120, 104))
    o.extend(_actuator(120, 104))
    o.append(_txt(120, 79, "PCV-6", 4.8, color=GREY))

    o.extend(_bubble(196, 104, "PT", "7"))
    o.extend(_ctrl(176, 123, "PAL-7", 40, 18, color=DARKRED, size=4.8))
    o.append(_path("M 196 113 L 196 123", sw=0.9, color=DARKRED, dash=SIG))

    o.extend(_bubble(256, 104, "PT", "24"))
    o.extend(_ctrl(236, 123, "PAL-24", 40, 18, color=DARKRED, size=4.8))
    o.append(_path("M 256 113 L 256 123", sw=0.9, color=DARKRED, dash=SIG))

    o.extend(_valve(390, 104, color=DARKRED))
    o.extend(_actuator(390, 104, color=DARKRED))
    o.extend(_valve(422, 104, color=DARKRED))
    o.extend(_actuator(422, 104, color=DARKRED))

    # bypass around the pilot gas pair
    o.append(_path("M 356 104 L 356 144 L 446 144 L 446 104", sw=1.1, color=DARKRED))
    o.extend(_handvalve(401, 144, color=DARKRED))
    o.append(_txt(401, 161, "HV-25", 4.8, color=DARKRED, weight="600"))
    o.extend(_ctrl(472, 135, "ZA-25", 40, 18, color=DARKRED, size=4.8))
    o.append(_path("M 413 144 L 472 144", sw=0.9, color=DARKRED, dash=SIG))

    # ---- fuel gas
    o.append(_txt(34, 220, "FUEL GAS", 5.2, anchor="start", weight="600"))
    o.append(_line(36, 226, 572, 226, sw=1.2))

    o.extend(_valve(390, 226, color=DARKRED))
    o.extend(_actuator(390, 226, color=DARKRED))
    o.extend(_valve(422, 226, color=DARKRED))
    o.extend(_actuator(422, 226, color=DARKRED))

    o.append(_path("M 356 226 L 356 266 L 446 266 L 446 226", sw=1.1, color=DARKRED))
    o.extend(_handvalve(401, 266, color=DARKRED))
    o.append(_txt(401, 283, "HV-26", 4.8, color=DARKRED, weight="600"))
    o.extend(_ctrl(472, 257, "ZA-26", 40, 18, color=DARKRED, size=4.8))
    o.append(_path("M 413 266 L 472 266", sw=0.9, color=DARKRED, dash=SIG))

    # ---- the logic solver
    o.append(_rect(150, 34, 190, 46, PALE_RED, sw=1.3, stroke=DARKRED))
    o.append(_txt(245, 54, "S/D LOGIC YC-20", 5.6, color=DARKRED, weight="600"))
    o.append(_txt(245, 70, "PLC an toàn dư thừa", 4.8, color=DARKRED))

    o.append(_path("M 196 95 L 196 80", sw=0.9, color=DARKRED, dash=SIG))
    o.append(_path("M 256 95 L 256 80", sw=0.9, color=DARKRED, dash=SIG))

    o.append(_path("M 340 44 L 390 44 L 390 85", sw=0.9, color=DARKRED, dash=SIG))
    o.append(_path("M 340 58 L 422 58 L 422 85", sw=0.9, color=DARKRED, dash=SIG))
    o.append(_path("M 340 70 L 460 70 L 460 196 L 390 196", sw=0.9, color=DARKRED, dash=SIG))
    o.append(_path("M 390 196 L 390 207", sw=0.9, color=DARKRED, dash=SIG))
    o.append(_path("M 422 196 L 422 207", sw=0.9, color=DARKRED, dash=SIG))

    o.append(_txt(330, 294, "HV-25 và HV-26 mở ra để thử trực tuyến; ZA-25 và ZA-26 báo về BPCS khi "
                            "van nhánh rẽ còn mở — đó là lý do quy trình bắt buộc đóng lại và kiểm tra "
                            "báo động đã tan.", 5.4, color=GREY))

    return _finish(o, 660, 306,
                   "Hình 16-6. Sơ đồ hệ cắt áp suất thấp khí mồi, vẽ theo góc nhìn của người vận hành "
                   "làm thử nghiệm ba tháng một lần. PT-7 và PT-24 cùng đo áp suất khí mồi; PAL-7 và "
                   "PAL-24 báo động cứng về phòng điều khiển. Bộ logic YC-20 đóng bốn van: XV-30A/B "
                   "trên khí mồi, XV-31A/B trên khí đốt. Muốn thử mà không cắt lò thì phải mở HV-25 và "
                   "HV-26 trước; ZA-25 và ZA-26 là báo động nhánh rẽ, và quy trình bắt buộc phải đóng "
                   "lại và xác nhận báo động đã tan trước khi kết thúc.",
                   "Figure 16-6. The low pilot gas pressure trip system drawn the way the operator sees "
                   "it during the quarterly test. PT-7 and PT-24 both measure pilot gas pressure; PAL-7 "
                   "and PAL-24 are hard-wired alarms to the control room. Logic YC-20 closes four "
                   "valves: XV-30A/B on the pilot gas and XV-31A/B on the fuel gas. Testing without "
                   "tripping the furnace requires opening HV-25 and HV-26 first; ZA-25 and ZA-26 are "
                   "the bypass alarms, and the procedure requires closing the bypasses and confirming "
                   "the alarms have cleared before finishing.",
                   "Sơ đồ hai dòng khí mồi và khí đốt, mỗi dòng có một cặp van cắt và một van nhánh rẽ "
                   "có báo động, nối về một bộ logic cắt chung.",
                   "A diagram of the pilot gas and fuel gas lines, each with a trip valve pair and a "
                   "bypassed test valve with its alarm, all feeding one shutdown logic block.")


FIGURES = [fig_16_1, fig_16_2, fig_16_3, fig_16_4, fig_16_5, fig_16_6]
