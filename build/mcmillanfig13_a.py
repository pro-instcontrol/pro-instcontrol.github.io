# -*- coding: utf-8 -*-
"""Vector redraws of Figures 13.1-13.5 in A. McMillan, *Electrical
Installations in Hazardous Areas*, Chapter 13 "Intrinsic safety".

The five drawings are simplified vector redraws of the rendered pages
p355, p361, p362, p366 and p367.  Printed English captions (including
their numbered Notes), in-figure labels, call-out keys and dimension
text are transcribed from the authoritative survey; every displayed
string is literal Unicode with raw ampersands escaped.  Printed quirks
are retained: the Note 2 wording "etc.,", the twice-printed "Upper disc
dimension 38 mm" label, the IIB (160 uJ) curve label that conflicts with
the prose list IIB = 120 uJ, and the non-ascending call-out order of
Fig. 13.2.  Each public callable returns the standard five-tuple through
``vfig._fig()`` and is registered in ``FIGS`` by the ``_reg`` decorator.
"""
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

from vfig import (BLUE, GREEN, GREY, INK, PAPER, RED, _arrow, _circle,
                  _defs, _fig, _line, _path, _poly, _rect, _txt, svg)

FIGS = {}


def _reg(f):
    FIGS[f.__name__] = f()
    return f


def esc(s):
    """Every displayed string is literal Unicode with raw ampersands escaped."""
    return str(s).replace("&", "&amp;")


def T(x, y, s, size=7.6, **kw):
    """Plain text: clamp into the 6.8-9.5 px contract, vet, delegate to vfig."""
    size = min(9.5, max(6.8, float(size)))
    return _txt(x, y, esc(s), size, **kw)


# ------------------------------------------------------------------ helpers

def _title(o, n, vi, en, size=7.2):
    o.append(T(340, 15, "Hình 13.%d · %s / Figure 13.%d · %s" % (n, vi, n, en),
               size, color=INK, weight="600"))


def _sub(o, vi, en=None, size=6.8):
    s = vi if en is None else vi + " / " + en
    o.append(T(340, 29, s, size, color=GREY))


def _lead(x1, y1, x2, y2, sw=0.8):
    return _arrow(x1, y1, x2, y2, sw=sw, color=INK, head="a7")


def _badge(o, cx, cy, n):
    o.append(_circle(cx, cy, 7, fill="#ffffff", sw=1.0))
    o.append(T(cx, cy + 2.4, str(n), 6.8, color=INK, weight="600"))


def _dim(o, x1, y1, x2, y2, label=None, lx=None, ly=None, size=6.8):
    """A dimension line with end caps and an optional bilingual label."""
    o.append(_line(x1, y1, x2, y2, sw=0.9, color=GREY))
    dx, dy = x2 - x1, y2 - y1
    ln = math.hypot(dx, dy) or 1.0
    nx, ny = -dy / ln * 3, dx / ln * 3
    for x, y in ((x1, y1), (x2, y2)):
        o.append(_line(x - nx, y - ny, x + nx, y + ny, sw=0.9, color=GREY))
    if label:
        o.append(T(lx if lx is not None else (x1 + x2) / 2.0,
                   ly if ly is not None else (y1 + y2) / 2.0 - 3, label, size))


def _resistor(o, x1, y, x2):
    n = 7
    pts = [(x1, y), (x1 + 6, y)]
    step = (x2 - x1 - 12) / float(n)
    for i in range(n):
        pts.append((x1 + 6 + i * step + step / 2.0, y - 6 if i % 2 == 0 else y + 6))
        pts.append((x1 + 6 + (i + 1) * step, y))
    pts.append((x2, y))
    o.append(_poly(pts, fill="none", sw=1.2, color=INK))


def _coil(o, cx, y0, y1, fill="#fbfbfb"):
    """A coil of semicircular humps inside a dashed component outline."""
    o.append(_rect(cx - 20, y0 - 6, 40, (y1 - y0) + 12,
                   fill=fill, sw=1.0, dash="3 3"))
    pts = []
    y = y0
    side = -1
    while y <= y1:
        pts.append((cx + side * 7, y))
        side = -side
        y += 6
    o.append(_poly(pts, fill="none", sw=1.2, color=INK))


# ------------------------------------------------------------------ 13.1

@_reg
def fig_f1301():
    """Figure 13.1 - blocks of a complete intrinsically safe system."""
    w, h = 680, 320
    o = [_defs(), _rect(0, 0, w, h, fill=PAPER, sw=0)]
    _title(o, 1, "Hệ thống an toàn bản chất", "The intrinsically safe system", 7.2)
    _sub(o, "Sơ đồ khối · ranh giới khu vực và các thành phần theo chú thích in / "
            "Block diagram · area boundary and components per the printed key")

    # Area divider and the two area headers.
    o.append(_line(340, 56, 340, 252, sw=1.4, dash="6 4", color=GREY))
    o.append(T(190, 64, "Khu vực không nguy hiểm / Non-hazardous area", 7.2, weight="600"))
    o.append(T(490, 64, "Khu vực nguy hiểm / Hazardous area", 7.2, weight="600"))

    # Spanning brackets: whole system, then the intrinsically safe circuit.
    o.append(_line(150, 90, 590, 90, sw=1.0))
    o.append(_line(150, 84, 150, 90, sw=1.0))
    o.append(_line(590, 84, 590, 90, sw=1.0))
    o.append(T(370, 84, "Hệ thống an toàn bản chất / Intrinsically safe system", 7.0))
    o.append(_line(262, 114, 590, 114, sw=1.0))
    o.append(_line(262, 108, 262, 114, sw=1.0))
    o.append(_line(590, 108, 590, 114, sw=1.0))
    o.append(T(426, 108, "Mạch an toàn bản chất / Intrinsically safe circuit", 6.8))

    # Interconnected boxes.
    o.append(_rect(40, 136, 88, 70, fill="#eef3fb", sw=1.2))
    o.append(T(84, 166, "Nguồn cung cấp", 7.0))
    o.append(T(84, 178, "và đầu ra", 7.0))
    o.append(T(84, 194, "(Note 2)", 6.8, color=GREY))
    o.append(T(84, 222, "Power supply and output", 6.8, color=GREY))

    o.append(_rect(150, 136, 108, 70, fill="#f6e6c8", sw=1.2))
    o.append(_line(244, 138, 244, 204, sw=1.0, dash="4 3", color=GREY))
    o.append(T(204, 166, "Thiết bị liên kết", 7.0))
    o.append(T(204, 194, "Associated apparatus", 6.8, color=GREY))

    o.append(_rect(262, 136, 40, 70, fill="#dbe9d5", sw=1.2))
    o.append(T(282, 166, "Giao", 6.8))
    o.append(T(282, 178, "diện", 6.8))
    o.append(T(282, 194, "(1)", 6.8, color=GREY))
    o.append(T(282, 222, "Intrinsically safe", 6.8, color=GREY))
    o.append(T(282, 234, "interface (Note 1)", 6.8, color=GREY))

    o.append(_line(302, 171, 388, 171, sw=1.4))
    o.append(_circle(302, 171, 2.4, fill=INK, sw=0))
    o.append(_circle(388, 171, 2.4, fill=INK, sw=0))
    o.append(T(345, 252, "Cáp liên kết", 7.0))
    o.append(T(345, 264, "Interconnecting cable", 6.8, color=GREY))

    o.append(_rect(388, 148, 60, 46, fill="#eef3fb", sw=1.2))
    o.append(T(418, 168, "Thiết bị", 6.8))
    o.append(T(418, 180, "đơn giản", 6.8))
    o.append(T(418, 192, "(3)", 6.8, color=GREY))
    o.append(T(418, 222, "Simple device", 6.8, color=GREY))
    o.append(T(418, 234, "(Note 3)", 6.8, color=GREY))

    o.append(_line(448, 171, 490, 171, sw=1.4))
    o.append(_rect(490, 136, 100, 70, fill="#eef3fb", sw=1.2))
    o.append(T(540, 166, "Thiết bị an toàn", 7.0))
    o.append(T(540, 178, "bản chất", 7.0))
    o.append(T(540, 194, "Intrinsically safe", 6.8, color=GREY))
    o.append(T(540, 206, "apparatus", 6.8, color=GREY))

    o.append(_line(128, 171, 150, 171, sw=1.2))
    o.append(_line(258, 171, 262, 171, sw=1.2))

    o.append(T(340, 274, "Giao diện thường nằm bên trong thiết bị liên kết, không nằm ở các cực của nó · "
                "The interface is normally within the associated apparatus, not at its terminals",
              6.8, color=GREY))
    o.append(T(340, 292, "Các thiết bị đơn giản có thể thêm vào với ít đánh giá bổ sung · "
                "Simple devices may be added with little additional evaluation", 6.8, color=GREY))

    return _fig(svg(w, h, "".join(o), esc("Fig 13.1")),
                "Hình 13.1 · Hệ thống an toàn bản chất. Ghi chú: (1) Giao diện an toàn bản chất "
                "(điểm mà sau đó điện áp, dòng điện, công suất và năng lượng được kiểm soát ở mức "
                "an toàn bản chất) thường nằm bên trong thiết bị liên kết, không phải ở các cực "
                "của thiết bị này. (2) Nguồn cấp cho thiết bị liên kết và các thiết bị đọc chỉ số "
                "v.v., thường được giả định ở điện thế lưới điện. (3) Các vật được định nghĩa là "
                "thiết bị đơn giản có thể được thêm vào mạch an toàn bản chất mà không cần đánh "
                "giá bổ sung đáng kể",
                "Figure 13.1 · The intrinsically safe system. Notes: (1) The intrinsically safe "
                "interface (the point beyond which voltages, currents, power and energy are "
                "controlled to an intrinsically safe level) is normally within the associated "
                "apparatus, not at its terminals. (2) Power supplies to associated apparatus and "
                "readouts etc., are normally assumed to be at mains potential. (3) Items defined "
                "as simple devices may be added in intrinsically safe circuits with little "
                "additional evaluation",
                "Sơ đồ khối hệ thống an toàn bản chất gồm hai vùng ngăn cách bằng đường đứt nét đứng: "
                "bên trái là khu vực không nguy hiểm với ô Nguồn cung cấp và đầu ra (Note 2), ô "
                "Thiết bị liên kết có đường đứt nét bên trong và ô Giao diện an toàn bản chất hẹp "
                "(Note 1); bên phải là khu vực nguy hiểm với ô Thiết bị đơn giản (Note 3) và ô "
                "Thiết bị an toàn bản chất. Một đường cáp nối liền các ô, và hai kẹp trên đỉnh chỉ "
                "phạm vi của toàn hệ thống và của mạch an toàn bản chất. Chú thích ở cuối nhắc "
                "rằng giao diện nằm bên trong thiết bị liên kết, nguồn nuôi thường ở điện thế "
                "lưới điện và thiết bị đơn giản cần rất ít đánh giá bổ sung",
                "Block diagram of an intrinsically safe system split by a vertical dashed boundary "
                "into a non-hazardous area on the left and a hazardous area on the right. On the "
                "left are the Power supply and output (Note 2) box, the Associated apparatus box "
                "with an internal dashed line, and the narrow Intrinsically safe interface "
                "(Note 1) box; on the right are the Simple device (Note 3) box and the Intrinsically "
                "safe apparatus box, all joined by a horizontal interconnecting cable. Brackets "
                "above mark the full intrinsically safe system and the shorter intrinsically safe "
                "circuit. Two footer lines restate that the interface lies inside the associated "
                "apparatus, supplies are at mains potential, and simple devices need little extra "
                "evaluation")


# ------------------------------------------------------------------ 13.2

@_reg
def fig_f1302():
    """Figure 13.2 - spark test apparatus cross-section and 1-18 key."""
    w, h = 680, 330
    o = [_defs(), _rect(0, 0, w, h, fill=PAPER, sw=0)]
    _title(o, 2, "Thiết bị thử tia lửa điển hình", "Typical spark test apparatus", 7.2)
    _sub(o, "Mặt cắt · số gọi ý theo chú thích in (không theo thứ tự từ trên xuống) / "
            "Cross-section · call-out numbers follow the printed key, not top-to-bottom order")

    # Simplified section of the apparatus between x=80 and x=300.
    o.append(_rect(160, 70, 80, 8, fill="#dedede", sw=1.0))
    o.append(_rect(194, 78, 12, 54, fill="#cfcfcf", sw=1.0))
    o.append(_rect(186, 124, 28, 12, fill="#eeeeee", sw=1.0))
    o.append(_path("M126,232 L126,150 A74,74 0 0 1 274,150 L274,232 Z",
                   fill="#fbfbfb", sw=1.1))
    o.append(_rect(150, 166, 100, 7, fill="#bdbdbd", sw=1.1))
    o.append(_rect(150, 194, 100, 7, fill="#cfcfcf", sw=1.1))
    o.append(_rect(194, 174, 12, 18, fill="#eeeeee", sw=1.0))
    o.append(_line(200, 174, 200, 194, sw=1.3))
    o.append(_rect(108, 188, 18, 6, fill="#eeeeee", sw=1.0))
    o.append(_rect(274, 188, 18, 6, fill="#eeeeee", sw=1.0))
    o.append(_circle(112, 214, 4, fill="#eeeeee", sw=1.0))
    o.append(_circle(288, 214, 4, fill="#eeeeee", sw=1.0))
    o.append(_rect(96, 204, 32, 7, fill="#dedede", sw=1.0))
    o.append(_rect(252, 204, 32, 7, fill="#dedede", sw=1.0))
    o.append(_rect(100, 220, 24, 6, fill="#cfcfcf", sw=1.0))
    o.append(_rect(256, 220, 24, 6, fill="#cfcfcf", sw=1.0))
    o.append(_rect(120, 228, 160, 6, fill="#eeeeee", sw=1.0))
    o.append(_rect(96, 234, 208, 8, fill="url(#h6)", sw=1.0))
    o.append(_rect(80, 242, 240, 10, fill="#dedede", sw=1.2))
    o.append(_rect(140, 258, 58, 18, fill="#dedede", sw=1.1))  # drive motor body
    o.append(_rect(114, 252, 8, 12, fill="#eeeeee", sw=1.0))
    o.append(_rect(278, 252, 8, 12, fill="#eeeeee", sw=1.0))
    o.append(_rect(96, 252, 14, 6, fill="#cfcfcf", sw=1.0))
    o.append(_rect(270, 252, 14, 6, fill="#cfcfcf", sw=1.0))
    o.append(_rect(194, 252, 12, 8, fill="#eeeeee", sw=1.0))
    o.append(_circle(200, 266, 13, fill="#eeeeee", sw=1.1))
    for a in range(0, 360, 45):
        r1 = math.radians(a)
        r2 = math.radians(a + 22)
        o.append(_line(200 + 14 * math.cos(r1), 266 + 14 * math.sin(r1),
                       200 + 18 * math.cos(r2), 266 + 18 * math.sin(r2),
                       sw=0.8, color=GREY))
    o.append(T(200, 296, "Cổng khí vào / ra · gas inlet / outlet", 6.8, color=GREY))

    # Numbered call-outs: badge position (x,y) then part (x,y).
    calls = [
        (4, 48, 126, 200, 130), (7, 48, 142, 200, 180),
        (8, 48, 158, 206, 184), (13, 48, 174, 160, 170),
        (5, 48, 190, 118, 190), (9, 48, 206, 112, 214),
        (11, 48, 222, 106, 222), (1, 48, 238, 104, 237),
        (2, 48, 254, 104, 255),
        (12, 332, 126, 270, 145), (15, 332, 142, 292, 190),
        (10, 332, 158, 284, 207), (6, 332, 174, 312, 247),
        (3, 332, 190, 282, 258), (17, 332, 206, 206, 256),
        (16, 332, 222, 212, 266), (18, 332, 238, 190, 268),
        (14, 332, 254, 274, 231),
    ]
    for n, bx, by, tx, ty in calls:
        o.append(_lead(bx + 7 if bx < 100 else bx - 7, by, tx, ty))
    for n, bx, by, tx, ty in calls:
        _badge(o, bx, by, n)

    # The printed 1-18 key, fully localized in the second half of each row.
    key = [
        (1, "Tấm cách điện", "Insulating plate"),
        (2, "Điểm nối dòng điện", "Current connection"),
        (3, "Bu lông cách điện", "Insulated bolt"),
        (4, "Ổ bi cách điện", "Insulated bearing"),
        (5, "Đầu ra khí", "Gas outlet"),
        (6, "Tấm đế", "Base plate"),
        (7, "Dây tiếp điểm", "Contact wire"),
        (8, "Giá giữ tiếp điểm", "Contact holder"),
        (9, "Vít kẹp", "Clamping screw"),
        (10, "Tấm ép", "Pressure plate"),
        (11, "Kẹp", "Clamp"),
        (12, "Buồng thử", "Chamber"),
        (13, "Đĩa tiếp điểm", "Contact disc"),
        (14, "Gioăng cao su", "Rubber seal"),
        (15, "Đầu vào khí", "Gas inlet"),
        (16, "Bánh răng dẫn 50 : 12", "Gear wheel drive 50 : 12"),
        (17, "Khớp nối cách điện", "Insulated coupling"),
        (18, "Động cơ giảm tốc 80 vòng/phút",
         "Drive motor with reduction gears 80 rev/min"),
    ]
    o.append(T(503, 62, "Chú thích / Key", 7.0, color=INK, weight="600"))
    for i, (n, vi, en) in enumerate(key):
        o.append(T(352, 80 + 13 * i, "%2d  %s / %s" % (n, vi, en), 6.8, anchor="start"))

    return _fig(svg(w, h, "".join(o), esc("Fig 13.2")),
                "Hình 13.2 · Thiết bị thử tia lửa điển hình. 1 Tấm cách điện, 2 Điểm nối dòng điện, "
                "3 Bu lông cách điện, 4 Ổ bi cách điện, 5 Đầu ra khí, 6 Tấm đế, 7 Dây tiếp điểm, "
                "8 Giá giữ tiếp điểm, 9 Vít kẹp, 10 Tấm ép, 11 Kẹp, 12 Buồng thử, 13 Đĩa tiếp "
                "điểm, 14 Gioăng cao su, 15 Đầu vào khí, 16 Bánh răng dẫn 50 : 12, 17 Khớp nối "
                "cách điện, 18 Động cơ với hộp giảm tốc 80 vòng/phút",
                "Figure 13.2 · Typical spark test apparatus. 1 Insulating plate, 2 Current "
                "connection, 3 Insulated bolt, 4 Insulated bearing, 5 Gas outlet, 6 Base plate, "
                "7 Contact wire, 8 Contact holder, 9 Clamping screw, 10 Pressure plate, 11 Clamp, "
                "12 Chamber, 13 Contact disc, 14 Rubber seal, 15 Gas inlet, 16 Gear wheel drive "
                "50 : 12, 17 Insulated coupling, 18 Drive motor with reduction gears 80 rev/min",
                "Mặt cắt đơn giản hóa của thiết bị thử tia lửa: buồng dạng vòm nằm trên tấm cách "
                "điện gạch chéo và tấm đế, trục dọc xuyên qua ổ bi cách điện, hai đĩa tiếp điểm "
                "đối mặt với dây tiếp điểm và giá giữ ở giữa, các cổng vào/ra khí hai bên, vít "
                "kẹp và tấm ép ở đế, cùng cơ cấu bánh răng, khớp nối cách điện và động cơ giảm "
                "tốc bên dưới. Mười tám số gọi ý được đặt quanh bản vẽ, trong đó số 9-13, 14, "
                "4/3/2, 16, 17, 18 ở một phía và 8/7, 6-1 ở phía kia đúng thứ tự in không tăng "
                "dần; bảng chú thích 1-18 ở bên phải liệt kê đầy đủ tên từng chi tiết",
                "Simplified cross-section of the spark test apparatus: a domed chamber stands on "
                "a hatched insulating plate and base plate, a vertical spindle passes through "
                "an insulated bearing, two opposing contact discs carry a contact wire and holder "
                "between them, gas inlet and outlet ports and clamping screws sit at the base, and "
                "a gear wheel, insulated coupling and reduction-gear motor hang below. Eighteen "
                "numbered call-outs surround the drawing in the printed non-ascending order "
                "(9-13, 14, 4/3/2, 16, 17, 18 on one side; 8/7 and 6-1 on the other), while the "
                "1-18 key at the right lists every part name in full")


# ------------------------------------------------------------------ 13.3

@_reg
def fig_f1303():
    """Figure 13.3 - side elevation and plan view with printed dimensions."""
    w, h = 680, 548
    o = [_defs(), _rect(0, 0, w, h, fill=PAPER, sw=0)]
    _title(o, 3, "Kích thước điển hình của thiết bị thử tia lửa",
           "Typical spark test apparatus dimensions", 7.2)
    _sub(o, "Hình chiếu cạnh ở trên và mặt bằng ở dưới · tất cả kích thước theo bản in / "
            "Side elevation above, plan view below · all dimensions per the printed drawing")

    # ---- side elevation
    o.append(_rect(180, 72, 340, 96, fill="#fbfbfb", sw=1.2))
    for xx in range(180, 521, 14):
        o.append(_line(xx, 72, xx + 6, 66, sw=0.7, color=GREY))
    o.append(_rect(140, 184, 420, 12, fill="#dedede", sw=1.1))
    o.append(_rect(140, 222, 420, 12, fill="#dedede", sw=1.1))
    o.append(_rect(250, 110, 90, 7, fill="#bdbdbd", sw=1.0))
    o.append(_rect(380, 136, 90, 7, fill="#cfcfcf", sw=1.0))
    o.append(_line(340, 117, 340, 136, sw=1.3))
    o.append(_rect(336, 120, 8, 10, fill="#eeeeee", sw=0.9))
    o.append(_line(340, 66, 340, 234, sw=0.8, dash="5 4", color=GREY))
    o.append(_rect(246, 136, 8, 8, fill="#eeeeee", sw=0.9))
    o.append(_rect(474, 164, 8, 8, fill="#eeeeee", sw=0.9))

    o.append(T(430, 58, "Buồng thử 250 cc tối thiểu / Chamber 250 cc minimum", 6.8))
    o.append(_lead(430, 60, 444, 73))
    for i, s in enumerate(["Dây vonfram tối thiểu 0,2 mm / 0.2 mm minimum",
                           "tungsten wire length 11 mm / chiều dài 11 mm"]):
        o.append(T(48, 100 + 13 * i, s, 6.8, anchor="start"))
    o.append(_lead(168, 110, 334, 126))
    o.append(T(528, 100, "Khoảng cách đĩa 10 mm", 6.8, anchor="start"))
    o.append(T(528, 112, "Separation of discs 10 mm", 6.8, anchor="start"))
    o.append(_lead(526, 108, 346, 116))
    o.append(T(528, 146, "Độ sâu rãnh 2 mm", 6.8, anchor="start"))
    o.append(T(528, 158, "Depth of slots 2 mm", 6.8, anchor="start"))
    o.append(_lead(526, 154, 480, 168))
    _dim(o, 250, 208, 340, 208, None)

    # ---- plan view
    o.append(_circle(300, 370, 86, fill="#fbfbfb", sw=1.2))
    o.append(_circle(430, 370, 44, fill="#f7f7f7", sw=1.1))
    o.append(_line(196, 370, 492, 370, sw=0.8, dash="5 4", color=GREY))
    o.append(_line(300, 272, 300, 468, sw=0.8, dash="5 4", color=GREY))
    o.append(_line(430, 320, 430, 420, sw=0.8, dash="5 4", color=GREY))
    for sx, sy in ((361, 309), (239, 309), (361, 431), (239, 431)):
        o.append(_line(sx - 5, sy + 5, sx + 5, sy - 5, sw=1.3, color=INK))
    o.append(_circle(278, 370, 5, fill="#dedede", sw=1.0))
    o.append(_circle(296, 370, 5, fill="#dedede", sw=1.0))
    o.append(_circle(430, 370, 7, fill="#dedede", sw=1.0))

    o.append(T(52, 292, "Đường kính đĩa trên 38 mm", 6.8, anchor="start"))
    o.append(T(52, 304, "Upper disc dimension 38 mm", 6.8, anchor="start"))
    o.append(_lead(214, 300, 244, 313))
    o.append(T(52, 470, "Đường kính đĩa trên 38 mm (in lại lần hai)", 6.8, anchor="start"))
    o.append(T(52, 482, "Upper disc dimension 38 mm (printed twice)", 6.8, anchor="start"))
    o.append(_lead(280, 476, 252, 430))
    o.append(T(510, 336, "Đĩa cadmi đường kính 38 mm", 6.8, anchor="start"))
    o.append(T(510, 348, "Cadmium disc diameter 38 mm", 6.8, anchor="start"))
    o.append(_lead(508, 352, 474, 368))
    for i, s in enumerate(["Mép trong của rãnh cách", "đường tâm đĩa 6,5 mm.",
                           "Inner edge of slots 6.5 mm", "from centre line of disc."]):
        o.append(T(510, 386 + 12 * i, s, 6.8, anchor="start"))
    o.append(_lead(508, 400, 400, 404))
    o.append(T(510, 442, "Chiều rộng rãnh 2 mm.", 6.8, anchor="start"))
    o.append(T(510, 454, "Slot width 2 mm.", 6.8, anchor="start"))
    o.append(T(200, 502, "Đĩa trên cách tâm buồng 10 mm", 6.8))
    o.append(T(200, 514, "Upper disc 10 mm from chamber centre", 6.8))
    o.append(T(440, 502, "Tâm đĩa dưới cách tâm đĩa trên 31 mm", 6.8))
    o.append(T(440, 514, "Lower disc centre 31 mm from upper disc centre", 6.8))
    o.append(T(440, 526, "along chamber centre line / theo đường tâm buồng", 6.8))
    _dim(o, 300, 466, 386, 466, None)
    _dim(o, 430, 420, 430, 470, None)

    return _fig(svg(w, h, "".join(o), esc("Fig 13.3")),
                "Hình 13.3 · Kích thước điển hình của thiết bị thử tia lửa",
                "Figure 13.3 · Typical spark test apparatus dimensions",
                "Bản vẽ gồm hình chiếu cạnh ở trên và hình mặt bằng ở dưới của thiết bị thử tia "
                "lửa. Hình chiếu cạnh cho thấy buồng thử 250 cc tối thiểu, dây vonfram tối thiểu "
                "0,2 mm dài 11 mm, hai đĩa cách nhau 10 mm, rãnh sâu 2 mm. Mặt bằng cho thấy "
                "đĩa trên đường kính 38 mm (nhãn này được in hai lần), đĩa cadmi đường kính "
                "38 mm, mép trong của rãnh cách đường tâm đĩa 6,5 mm, rãnh rộng 2 mm, đĩa trên "
                "cách tâm buồng 10 mm và tâm đĩa dưới cách tâm đĩa trên 31 mm dọc theo đường tâm "
                "buồng. Các mũi tên kích thước nối nhãn tới đúng chi tiết tương ứng",
                "A side elevation above and a plan view below of the spark test apparatus. The "
                "elevation shows the 250 cc minimum chamber, 0.2 mm minimum tungsten wire 11 mm "
                "long, discs separated by 10 mm and slots 2 mm deep. The plan view shows the "
                "upper disc dimension 38 mm (a label printed twice), the cadmium disc diameter "
                "38 mm, slot inner edges 6.5 mm from the disc centre line, slot width 2 mm, the "
                "upper disc 10 mm from the chamber centre, and the lower disc centre 31 mm from "
                "the upper disc centre along the chamber centre line. Leader lines and dimension "
                "arrows tie each printed label to its feature")


# ------------------------------------------------------------------ 13.4

@_reg
def fig_f1304():
    """Figure 13.4 - inductive spark production, contacts closed and open."""
    w, h = 680, 540
    o = [_defs(), _rect(0, 0, w, h, fill=PAPER, sw=0)]
    _title(o, 4, "Sự phát sinh tia lửa trong mạch cảm ứng", "Inductive spark production", 7.2)
    _sub(o, "Hai trạng thái · tiếp điểm đóng (trên) và tiếp điểm hở (dưới) / "
            "Two states · contacts closed above, contacts open below")

    def circuit(y, closed):
        # Top and bottom rails, plus the open-left dc source.
        o.append(_line(100, y, 560, y, sw=1.3))
        o.append(_line(100, y + 140, 560, y + 140, sw=1.3))
        o.append(_line(100, y, 100, y + 46, sw=1.3))
        o.append(_line(100, y + 94, 100, y + 140, sw=1.3))
        o.append(_circle(100, y + 50, 3.2, fill="#ffffff", sw=1.1))
        o.append(_circle(100, y + 90, 3.2, fill="#ffffff", sw=1.1))
        o.append(T(112, y + 50, "+ V", 6.8, anchor="start"))
        o.append(T(112, y + 94, "−", 6.8, anchor="start"))
        o.append(T(86, y + 62, "Nguồn một chiều", 6.8, anchor="end"))
        o.append(T(86, y + 74, "dc power source", 6.8, anchor="end"))

        _resistor(o, 150, y, 224)
        o.append(T(185, y - 30, "Điện trở giới hạn dòng", 6.8))
        o.append(T(185, y - 18, "Current defining resistor", 6.8))

        if closed:
            o.append(_poly([(298, y - 8), (318, y), (298, y + 8)],
                           fill="#c9c9c9", sw=1.1, close=True))
            o.append(_poly([(362, y - 8), (342, y), (362, y + 8)],
                           fill="#c9c9c9", sw=1.1, close=True))
            o.append(T(372, y - 30, "Thiết bị thử tia lửa (tiếp điểm đóng)", 6.8))
            o.append(T(372, y - 18, "Spark test apparatus (contacts closed)", 6.8))
            o.append(_lead(400, y - 14, 352, y - 6))
            o.append(_arrow(410, y, 452, y, sw=1.3))
            o.append(T(432, y - 6, "i", 7.4))
            o.append(T(520, y - 30, "Dòng ổn định", 6.8))
            o.append(T(520, y - 18, "Steady state current", 6.8))
            o.append(_lead(520, y - 14, 478, y - 3))
        else:
            o.append(_poly([(298, y - 8), (318, y), (298, y + 8)],
                           fill="#c9c9c9", sw=1.1, close=True))
            o.append(_poly([(362, y - 8), (342, y), (362, y + 8)],
                           fill="#c9c9c9", sw=1.1, close=True))
            o.append(_poly([(324, y), (330, y - 5), (334, y + 1), (340, y)],
                           fill="none", sw=1.0, color=RED))
            o.append(T(372, y - 30, "Thiết bị thử tia lửa (tiếp điểm hở)", 6.8))
            o.append(T(372, y - 18, "Spark test apparatus (contacts open)", 6.8))
            o.append(T(330, y + 22, "Khe hở hồ quang/tia lửa / Arc/spark gap", 6.8))

        _coil(o, 560, y + 34, y + 104)
        o.append(_line(560, y, 560, y + 28, sw=1.3))
        o.append(_line(560, y + 110, 560, y + 140, sw=1.3))
        o.append(_circle(560, y + 28, 3, fill="#ffffff", sw=1.0))
        o.append(_circle(560, y + 110, 3, fill="#ffffff", sw=1.0))
        o.append(T(498, y + 72, "Cuộn cảm / Inductor", 6.8, anchor="end"))
        o.append(_lead(502, y + 72, 538, y + 72))

    circuit(110, True)
    circuit(320, False)
    o.append(T(60, 510, "L = độ tự cảm · r = điện trở trong", 6.8, anchor="start"))
    o.append(T(60, 524, "L = inductance · r = internal resistance", 6.8, anchor="start"))
    o.append(T(620, 510, "Các vòng tròn đầu cực có ký hiệu in không đọc được · "
                "terminal marks are unreadable", 6.8, anchor="end"))

    return _fig(svg(w, h, "".join(o), esc("Fig 13.4")),
                "Hình 13.4 · Sự phát sinh tia lửa trong mạch cảm ứng",
                "Figure 13.4 · Inductive spark production",
                "Hai sơ đồ mạch mắc nối tiếp gồm nguồn một chiều, điện trở giới hạn dòng, thiết bị "
                "thử tia lửa và cuộn cảm được khoanh đứt nét. Sơ đồ trên có các tiếp điểm đóng, "
                "mũi tên dòng i chạy từ phải sang trái trên dây dẫn và nhãn dòng ổn định; sơ đồ "
                "dưới có các tiếp điểm hở với khe hở hồ quang/tia lửa được tô đỏ giữa hai tiếp "
                "điểm. Hai đầu cực nhỏ trên cuộn cảm mang ký tự in không đọc được, nên chỉ vẽ "
                "dưới dạng vòng tròn. Dòng chú thích cuối hình định nghĩa L là độ tự cảm và r là "
                "điện trở trong",
                "Two series circuits each containing a dc power source, a current defining "
                "resistor, the spark test apparatus and a dashed-outline inductor. The upper "
                "circuit shows closed contacts, a current arrow i on the top rail pointing left "
                "and a steady state current label; the lower circuit shows open contacts with a "
                "small red zigzag drawn in the arc/spark gap between them. The tiny terminal "
                "circles at each end of the inductor carry printed glyphs that are unreadable, "
                "so only the circles are shown. Footer lines define L as inductance and r as "
                "internal resistance")


# ------------------------------------------------------------------ 13.5

@_reg
def fig_f1305():
    """Figure 13.5 - log-log ignition thresholds for inductive circuits."""
    w, h = 680, 450
    o = [_defs(), _rect(0, 0, w, h, fill=PAPER, sw=0)]
    _title(o, 5, "Ngưỡng cháy nổ · mạch cảm ứng ở 24 V trở lên",
           "Ignition threshold/inductive circuits at 24 V and above", 7.2)
    _sub(o, "Trục log-log · giá trị năng lượng theo nhãn đường cong in / "
            "Log-log axes · energy values per the printed curve labels")

    x0, x1 = 110, 580
    y0, y1 = 62, 380

    def px(v):
        return x0 + (math.log10(v) + 2.0) / 2.0 * (x1 - x0)

    def py(v):
        return y1 - (math.log10(v) + 4.0) / 4.0 * (y1 - y0)

    o.append(_rect(x0, y0, x1 - x0, y1 - y0, fill="#fbfbfb", sw=1.2))

    # Major log grid at the printed tick values.
    for v, lab in [(0.01, "0.01"), (0.03, "0.03"),
                   (0.1, "0.1"), (0.3, "0.3"), (0.5, "0.5"), (1.0, "1.0")]:
        xx = px(v)
        o.append(_line(xx, y0, xx, y1, sw=0.6, color="#cccccc"))
        o.append(_line(xx, y1, xx, y1 + 4, sw=0.9, color=GREY))
        o.append(T(xx, y1 + 16, lab, 6.8, color=INK))
    for v, lab in [(1.0, "1.0"), (0.3, "0.3"), (0.1, "0.1"), (0.03, "0.03"),
                   (0.01, "0.01"), (0.003, "0.003"), (0.001, "0.001"),
                   (0.0003, "0.0003"), (0.0001, "0.0001")]:
        yy = py(v)
        o.append(_line(x0, yy, x1, yy, sw=0.6, color="#cccccc"))
        o.append(_line(x0 - 4, yy, x0, yy, sw=0.9, color=GREY))
        o.append(T(x0 - 7, yy + 2.4, lab, 6.8, anchor="end", color=INK))

    # Three constant-energy lines: L = E / (400000 * I^2).
    def inductance(e, cur):
        return e / (400000.0 * cur * cur)

    for e, col in ((320, BLUE), (160, GREEN), (40, RED)):
        pts = []
        for k in range(241):
            cur = 10 ** (-2.0 + k * 2.0 / 240.0)
            lv = inductance(e, cur)
            if lv > 1.0:
                lv = 1.0
            if lv < 0.0001:
                lv = 0.0001
            pts.append((px(cur), py(lv)))
        o.append(_poly(pts, fill="none", sw=1.8, color=col))

    # Curve labels with short leaders to the printed energy lines.
    for e, vi, en, col, cur, ox, oy in (
            (320, "IIA (320 μJ)", "IIA (320 μJ)", BLUE, 0.16, 8, -6),
            (160, "IIB (160 μJ)", "IIB (160 μJ)", GREEN, 0.22, 8, -6),
            (40, "IIC (40 μJ)", "IIC (40 μJ)", RED, 0.15, -104, 24)):
        lv = inductance(e, cur)
        cx, cy = px(cur), py(lv)
        o.append(T(cx + ox, cy + oy, en, 7.2, anchor="start", color=col, weight="600"))
        o.append(_lead(cx + ox - 2, cy + oy - 2, cx, cy))

    # Axis titles in both languages.
    o.append(T((x0 + x1) / 2.0, 422, "Minimum igniting current / Dòng cháy nhỏ nhất gây cháy",
               7.4, weight="600"))
    _yc = (y0 + y1) / 2.0
    o.append(T(24, _yc, "Inductance / Độ tự cảm", 7.4, anchor="middle",
               color=INK, weight="600").replace(
                   ">", ' transform="rotate(-90 24 %s)">' % _yc, 1))
    o.append(T(340, 442, "Ghi chú: ngưỡng cháy nổ của mạch cảm ứng như trong Hình 13.4 với V = 24 V · "
                "Note: threshold for the inductive circuit in Fig. 13.4 with V = 24 V",
               6.8, color=GREY))

    return _fig(svg(w, h, "".join(o), esc("Fig 13.5")),
                "Hình 13.5 · Ngưỡng cháy nổ/mạch cảm ứng ở 24 V trở lên. Ghi chú: Ngưỡng cháy nổ "
                "của mạch cảm ứng như minh họa trong Hình 13.4 với V = 24 V",
                "Figure 13.5 · Ignition threshold/inductive circuits at 24 V and above. Note: "
                "Ignition threshold for inductive circuit shown in Fig. 13.4 with V = 24 V",
                "Đồ thị log-log có trục tung Độ tự cảm (Inductance) với các vạch 1,0 đến 0,0001 "
                "và trục hoành Dòng cháy nhỏ nhất gây cháy (Minimum igniting current) với các "
                "vạch 0,01 đến 1,0. Ba đường thẳng dốc xuống từ trái sang phải, song song và xếp "
                "từ trên xuống là IIA (320 μJ), IIB (160 μJ) và IIC (40 μJ); nhãn IIB 160 μJ "
                "được giữ nguyên dù danh sách trong văn bản ghi IIB = 120 μJ. Chú thích dưới "
                "đồ thị nói rằng đây là ngưỡng cháy nổ của mạch cảm ứng như Hình 13.4 với V = 24 V",
                "A log-log plot with the vertical Inductance axis labelled from 1.0 down to "
                "0.0001 and the horizontal Minimum igniting current axis labelled from 0.01 to "
                "1.0. Three parallel descending straight lines run from upper left to lower "
                "right, stacked from top to bottom as IIA (320 μJ), IIB (160 μJ) and IIC "
                "(40 μJ); the printed IIB 160 μJ label is retained even though the prose list "
                "gives IIB = 120 μJ. The printed Note states that this is the ignition threshold "
                "for the inductive circuit of Fig. 13.4 with V = 24 V")
