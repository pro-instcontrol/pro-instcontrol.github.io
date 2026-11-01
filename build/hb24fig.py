# -*- coding: utf-8 -*-
"""Figures for Handbook Chapter 24 — Torque and Power Measurement
(Ivan J. Garshelis, Magnova, Inc.).

The source chapter contains exactly seven figures (24.1–24.7).
FIGS is a 7-figure set — nothing is padded.
"""
import math as _m

from hbfig import GOLD, INK, MUTED, TXT, _f, svg, _fig

E = "#2a2a2a"
G = "#b45309"
S = "#888888"
P = "#ffffff"
FILL = "#eef2f7"
WARM = "#fdf6e3"


def _lbl(x, y, txt, cls="t", anchor="start"):
    return '<text class="%s" x="%s" y="%s" text-anchor="%s">%s</text>' % (
        cls, _f(x), _f(y), anchor, txt)


def _subs(x, y, parts, anchor="start", cls="t"):
    """Text with real subscripts: parts is [(txt, is_subscript), ...]."""
    s = ""
    prev = False
    for txt, is_sub in parts:
        if is_sub:
            s += '<tspan font-size="8" dy="3">%s</tspan>' % txt
        elif prev:
            s += '<tspan dy="-3">%s</tspan>' % txt
        else:
            s += txt
        prev = is_sub
    return ('<text class="%s" x="%s" y="%s" text-anchor="%s">%s</text>'
            % (cls, _f(x), _f(y), anchor, s))


def _defs():
    return ('<defs>'
            '<marker id="ah24" markerWidth="9" markerHeight="9" refX="7" refY="3" '
            'orient="auto"><path d="M0,0 L7,3 L0,6 z" fill="%s"/></marker>'
            '<marker id="ah24g" markerWidth="9" markerHeight="9" refX="7" refY="3" '
            'orient="auto"><path d="M0,0 L7,3 L0,6 z" fill="%s"/></marker>'
            '<marker id="ah24s" markerWidth="9" markerHeight="9" refX="7" refY="3" '
            'orient="auto"><path d="M0,0 L7,3 L0,6 z" fill="%s"/></marker>'
            '</defs>' % (E, G, S))


def _arr(x1, y1, x2, y2, col=E, marker="ah24", sw=1.4):
    return ('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="%s" '
            'marker-end="url(#%s)"/>' % (_f(x1), _f(y1), _f(x2), _f(y2), col, sw, marker))


def _box(x, y, w, h, t, col=E, fill="#ffffff", fs=11, rx=5):
    o = ['<rect x="%s" y="%s" width="%s" height="%s" rx="%s" fill="%s" stroke="%s" '
         'stroke-width="1.3"/>' % (_f(x), _f(y), _f(w), _f(h), _f(rx), fill, col)]
    lines = t.split("\n")
    for i, ln in enumerate(lines):
        yy = y + h / 2.0 + (i - (len(lines) - 1) / 2.0) * (fs + 3) + fs * 0.35
        o.append(_lbl(x + w / 2.0, yy, ln, "tb", "middle"))
    return "".join(o)


def _rect(x, y, w, h, fill=FILL, col=E, sw=1.4, dash=None):
    d = (' stroke-dasharray="%s"' % dash) if dash else ""
    return ('<rect x="%s" y="%s" width="%s" height="%s" fill="%s" stroke="%s" '
            'stroke-width="%s"%s/>' % (_f(x), _f(y), _f(w), _f(h), fill, col, _f(sw), d))


def _dot(x, y, r=3.4, col=E):
    return '<circle cx="%s" cy="%s" r="%s" fill="%s"/>' % (_f(x), _f(y), _f(r), col)


def _line(x1, y1, x2, y2, col=S, sw=1.0, dash=None):
    d = (' stroke-dasharray="%s"' % dash) if dash else ""
    return ('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="%s"%s/>'
            % (_f(x1), _f(y1), _f(x2), _f(y2), col, _f(sw), d))


def _path(d, col=E, sw=1.4, fill="none", dash=None):
    ds = (' stroke-dasharray="%s"' % dash) if dash else ""
    return ('<path d="%s" fill="%s" stroke="%s" stroke-width="%s"%s/>'
            % (d, fill, col, _f(sw), ds))


def _circ(cx, cy, r, fill="none", col=E, sw=1.4, dash=None):
    ds = (' stroke-dasharray="%s"' % dash) if dash else ""
    return ('<circle cx="%s" cy="%s" r="%s" fill="%s" stroke="%s" stroke-width="%s"%s/>'
            % (_f(cx), _f(cy), _f(r), fill, col, _f(sw), ds))


def _ground(x, y, w=34):
    """Ground symbol (hatched base) centred at x, top edge at y."""
    o = [_line(x - w / 2, y, x + w / 2, y, E, 1.6)]
    for i in range(5):
        xx = x - w / 2 + 4 + i * (w - 8) / 4.0
        o.append(_line(xx, y, xx - 5, y + 8, S, 1.0))
    return "".join(o)


# ---------------------------------------------------------------- 24.1
def fig_24_1():
    o = [_defs()]
    # ---- (a) off-axis force producing a torque
    ox, oy, r = 140, 152, 80
    o.append(_circ(ox, oy, r, FILL, E, 1.6))
    o.append(_circ(ox, oy, 5, E, E, 1.0))
    px = ox + r * _m.cos(_m.radians(42))
    py = oy - r * _m.sin(_m.radians(42))
    o.append(_line(ox, oy, px, py, E, 1.2, "5 4"))
    o.append(_lbl((ox + px) / 2.0 + 9, (oy + py) / 2.0 + 13, "l", "t", "middle"))
    o.append(_dot(px, py, 3.4))
    o.append(_lbl(px + 6, py - 6, "P", "tb"))
    # tangent (CW direction)
    tx, ty = _m.sin(_m.radians(42)), _m.cos(_m.radians(42))
    o.append(_line(px - 38 * tx, py - 38 * ty, px + 46 * tx, py + 46 * ty, S, 1.0, "4 4"))
    # force at angle beta to the tangent
    fx, fy = _m.cos(_m.radians(18)), _m.sin(_m.radians(18))
    o.append(_arr(px, py, px + 62 * fx, py + 62 * fy))
    o.append(_lbl(px + 66 * fx, py + 66 * fy + 4, "F"))
    # tangential component
    o.append(_arr(px, py, px + 60 * tx, py + 60 * ty, G, "ah24g"))
    o.append(_subs(px + 60 * tx + 7, py + 60 * ty + 11, [("F", False), ("t", True)], "start", "t"))
    o.append(_path("M%s,%s A26,26 0 0 0 %s,%s"
                   % (_f(px + 26 * fx), _f(py + 26 * fy), _f(px + 26 * tx), _f(py + 26 * ty)),
                   S, 1.0))
    o.append(_lbl(px + 30 * (fx + tx) / 2.0 + 6, py + 30 * (fy + ty) / 2.0 + 6, "β"))
    # CW rotation arrow about the axis
    o.append(_path("M%s,%s A30,30 0 0 1 %s,%s"
                   % (_f(ox - 30), _f(oy + 4), _f(ox + 4), _f(oy + 30)), E, 1.3))
    o.append(_arr(ox + 2, oy + 30, ox + 12, oy + 28))
    o.append(_lbl(ox - 4, oy + 46, "T", "tb", "middle"))
    o.append(_lbl(170, 258, "(a) lực lệch trục tạo ra mômen xoắn", "ts", "middle"))

    # ---- (b) shaft twisted through phi
    sx0, sx1, sy0, sy1 = 420, 626, 118, 152
    o.append(_rect(sx0, sy0, sx1 - sx0, sy1 - sy0, FILL, E, 1.5))
    o.append(_rect(408, sy0 - 6, 12, 48, "#ffffff", E, 1.4))
    for i in range(4):
        yy = sy0 - 4 + i * 13
        o.append(_line(408, yy, 398, yy + 8, S, 1.0))
    o.append('<ellipse cx="%s" cy="%s" rx="7" ry="17" fill="none" stroke="%s" stroke-width="1.3"/>'
             % (_f(sx1), _f((sy0 + sy1) / 2.0), E))
    o.append(_line(sx1, sy0, sx1, sy1, E, 1.2))
    ph = _m.radians(26)
    ex, ey = (sy1 - sy0) / 2.0, 0.0
    o.append(_line(sx1, (sy0 + sy1) / 2.0 - 17, sx1 + 7 * _m.sin(ph), (sy0 + sy1) / 2.0 - 17 * _m.cos(ph),
                   G, 1.5))
    o.append(_line(sx1, (sy0 + sy1) / 2.0 + 17, sx1 + 7 * _m.sin(ph), (sy0 + sy1) / 2.0 + 17 * _m.cos(ph),
                   G, 1.5))
    o.append(_lbl(sx1 + 16, sy0 + 4, "φ", "t"))
    o.append(_path("M%s,%s A18,18 0 0 0 %s,%s"
                   % (_f(sx1 + 20), _f(sy0 + 8), _f(sx1 + 18), _f(sy0 + 30)), S, 1.0))
    o.append(_line(420, 190, 626, 190, S, 1.0))
    o.append(_line(420, 186, 420, 194, S, 1.0))
    o.append(_line(626, 186, 626, 194, S, 1.0))
    o.append(_lbl(523, 206, "L", "t", "middle"))
    o.append(_lbl(470, 84, "T", "tb", "middle"))
    o.append(_arr(470, 92, 470, 112))
    o.append(_lbl(523, 258, "(b) trục bị xoắn một góc φ trên chiều dài L", "ts", "middle"))

    return _fig(svg(680, 268, "".join(o),
                    "Lực lệch trục tạo mômen xoắn và trục bị xoắn dưới tác dụng của mômen"),
                "Hình 24.1 · (a) Lực lệch trục F tại P tạo ra mômen xoắn T = (F cos β)l có xu hướng làm "
                "vật quay theo chiều kim đồng hồ. (b) Truyền mômen xoắn T trên chiều dài L làm trục xoắn "
                "một góc φ.",
                "Figure 24.1 · (a) The off-axis force F at P produces a torque T = (F cos β)l tending to "
                "rotate the body clockwise. (b) Transmitting torque T over length L twists the shaft "
                "through angle φ.",
                "Đĩa tròn có lực lệch trục sinh mômen, và trục bị xoắn một góc phi",
                "A disk with an off-axis force producing torque, and a shaft twisted by phi")


# ---------------------------------------------------------------- 24.2
def fig_24_2():
    o = [_defs()]
    y = 118
    o.append(_box(52, y, 116, 74, "B\nđộng cơ", E, FILL, 10))
    o.append(_box(452, y, 116, 74, "F\ntải", E, FILL, 10))
    # couplings and transmitting region
    o.append(_rect(172, y + 24, 22, 26, WARM, E, 1.3))
    o.append(_rect(394, y + 24, 22, 26, WARM, E, 1.3))
    o.append(_rect(198, y + 30, 192, 14, "#ffffff", E, 1.3))
    o.append(_lbl(294, y + 24, "D", "tb", "middle"))
    o.append(_lbl(183, y + 18, "C", "tb", "middle"))
    o.append(_lbl(405, y + 18, "E", "tb", "middle"))
    # reaction supports
    o.append(_arr(110, y + 74, 110, y + 100))
    o.append(_ground(110, y + 100, 40))
    o.append(_lbl(110, y + 124, "A", "tb", "middle"))
    o.append(_arr(510, y + 74, 510, y + 100))
    o.append(_ground(510, y + 100, 40))
    o.append(_lbl(510, y + 124, "G", "tb", "middle"))
    # torque arrows
    o.append(_path("M%s,%s A22,22 0 0 1 %s,%s" % (_f(84), _f(y - 8), _f(120), _f(y - 8)), G, 1.3))
    o.append(_arr(116, y - 10, 124, y - 6, G, "ah24g"))
    o.append(_path("M%s,%s A22,22 0 0 1 %s,%s" % (_f(484), _f(y - 8), _f(520), _f(y - 8)), G, 1.3))
    o.append(_arr(516, y - 10, 524, y - 6, G, "ah24g"))
    o.append(_lbl(294, y - 16, "mômen truyền qua D", "ts", "middle"))
    o.append(_lbl(294, 268, "A và G là các phản lực trên khung máy; B và F là mômen cần đo", "ts", "middle"))

    return _fig(svg(680, 278, "".join(o),
                    "Sơ đồ bố trí thiết bị đo mômen xoắn và công suất"),
                "Hình 24.2 · Sơ đồ bố trí các thiết bị dùng để đo mômen xoắn và công suất.",
                "Figure 24.2 · Schematic arrangement of devices used for the measurement of torque and "
                "power.",
                "Sơ đồ khối động cơ, khớp nối, đoạn truyền mômen, tải và các phản lực",
                "Block diagram of driver, couplings, transmitting region, load and reactions")


# ---------------------------------------------------------------- 24.3
def fig_24_3():
    o = [_defs()]

    # (a) surface strain: four gages + slip rings
    o.append(_rect(36, 66, 250, 28, FILL, E, 1.4))
    for xx in (86, 176):
        o.append(_rect(xx, 61, 30, 6, G, G, 1.0))
        o.append(_rect(xx, 93, 30, 6, "#ffffff", E, 1.1))
    for i in range(3):
        o.append(_rect(252 + i * 11, 62, 7, 36, "#ffffff", E, 1.2))
    o.append(_rect(254, 44, 22, 8, E, E, 1.0))
    o.append(_rect(254, 108, 22, 8, E, E, 1.0))
    o.append(_lbl(150, 44, "bốn gage biến dạng", "ts", "middle"))
    o.append(_lbl(268, 132, "vòng trượt và chổi than", "ts", "middle"))
    o.append(_lbl(176, 158, "(a) biến dạng bề mặt", "ts", "middle"))

    # (b) twist angle: two toothed wheels + pickups
    o.append(_rect(392, 74, 190, 14, "#ffffff", E, 1.3))
    for xx in (376, 578):
        o.append(_rect(xx, 56, 16, 50, FILL, E, 1.4))
        for i in range(4):
            o.append(_rect(xx - 4, 60 + i * 12, 4, 6, E, E, 1.0))
            o.append(_rect(xx + 16, 60 + i * 12, 4, 6, E, E, 1.0))
    o.append(_rect(384, 34, 20, 12, WARM, E, 1.2))
    o.append(_rect(570, 34, 20, 12, WARM, E, 1.2))
    o.append(_lbl(394, 28, "đầu thu 1", "ts", "middle"))
    o.append(_lbl(580, 28, "đầu thu 2", "ts", "middle"))
    o.append(_lbl(487, 118, "thanh xoắn", "ts", "middle"))
    o.append(_lbl(487, 158, "(b) góc xoắn", "ts", "middle"))

    # (c) stress: two grooved regions with sense windings
    o.append(_rect(36, 226, 250, 26, FILL, E, 1.4))
    for xx in (96, 196):
        for i in range(4):
            o.append(_rect(xx + i * 9, 226, 4, 26, "#ffffff", S, 1.0))
    for xx in (110, 210):
        o.append(_path("M%s,214 q10,-14 20,0 q-10,10 -20,0" % _f(xx), G, 1.4))
        o.append(_line(xx + 10, 214, xx + 10, 224, G, 1.0))
    o.append(_lbl(96, 196, "cuộn cảm nhận", "ts", "middle"))
    o.append(_subs(262, 214, [("V", False), ("1", True)]))
    o.append(_subs(262, 236, [("V", False), ("2", True)]))
    o.append(_lbl(176, 288, "(c) ứng suất", "ts", "middle"))

    # (d) type 2: magnetized ring + field sensor
    o.append(_rect(392, 226, 190, 24, FILL, E, 1.4))
    o.append(_rect(452, 210, 70, 56, WARM, E, 1.4))
    o.append(_line(487, 210, 487, 266, E, 1.2))
    for yy in (220, 250):
        o.append(_arr(462, yy, 476, yy, E, "ah24"))
        o.append(_arr(512, yy, 498, yy, E, "ah24"))
    o.append(_arr(462, 236, 480, 244, G, "ah24g"))
    o.append(_arr(512, 236, 494, 244, G, "ah24g"))
    o.append(_rect(474, 182, 26, 14, "#ffffff", E, 1.2))
    o.append(_lbl(487, 176, "cảm biến từ trường", "ts", "middle"))
    o.append(_lbl(487, 288, "(d) vòng từ hóa", "ts", "middle"))

    return _fig(svg(680, 300, "".join(o),
                    "Bốn kỹ thuật đo mômen xoắn truyền qua trục"),
                "Hình 24.3 · Bốn kỹ thuật đang được dùng để đo mômen xoắn truyền qua trục. (a) Biến dạng "
                "xoắn trong trục làm thay đổi điện trở của bốn gage biến dạng mắc thành cầu Wheatstone; ở "
                "đây các kết nối điện đi qua vòng trượt và chổi than. (b) Độ xoắn của đoạn trục làm dịch "
                "góc các đặc điểm bề mặt trên hai bánh răng, tạo ra sai pha giữa tín hiệu của hai đầu "
                "thu. (c) Độ từ thẩm của hai vùng xẻ rãnh thay đổi ngược chiều nhau theo ứng suất xoắn, "
                "được cảm nhận như hiệu điện áp của hai cuộn cảm nhận. (d) Ứng suất xoắn làm từ hóa ban "
                "đầu theo chu vi trong vòng bị nghiêng đi, sinh ra các cực từ tại vách đômen và hai mặt "
                "đầu vòng; từ trường tạo ra được cảm nhận bằng cảm biến từ trường.",
                "Figure 24.3 · Four techniques in present use for measuring transmitted torque. (a) "
                "Torsional strain alters the resistance of four strain gages in a Wheatstone bridge, with "
                "connections through slip rings and brushes. (b) Twist of the torsion section displaces "
                "the surface features on two toothed wheels, creating a phase difference between the two "
                "pickup signals. (c) The permeabilities of the two grooved regions change oppositely with "
                "torsional stress, sensed as a difference in the two sense-winding voltages. (d) "
                "Torsional stress tilts the initially circumferential magnetization in the ring, so "
                "poles appear at the domain wall and ring ends and a field sensor detects the resulting "
                "field.",
                "Bốn sơ đồ: gage biến dạng với vòng trượt, hai bánh răng với đầu thu, hai vùng xẻ rãnh "
                "với cuộn cảm nhận, và vòng từ hóa với cảm biến từ trường",
                "Four schemes: strain gages with slip rings, two toothed wheels with pickups, grooved "
                "regions with sense windings, and a magnetized ring with a field sensor")


# ---------------------------------------------------------------- 24.4
def fig_24_4():
    o = [_defs()]
    # housing
    o.append(_rect(112, 96, 386, 78, FILL, E, 1.6))
    # shaft
    o.append(_rect(64, 126, 482, 18, "#ffffff", E, 1.4))
    # bearings
    for xx in (168, 442):
        o.append(_rect(xx, 118, 16, 34, "#ffffff", E, 1.2))
    # keyways at both shaft ends
    o.append(_rect(64, 126, 16, 6, WARM, E, 1.1))
    o.append(_rect(530, 138, 16, 6, WARM, E, 1.1))
    # connector on top
    o.append(_rect(286, 78, 42, 18, WARM, E, 1.2))
    o.append(_line(307, 78, 307, 62, E, 1.2))
    o.append(_lbl(316, 58, "cáp tín hiệu", "ts"))
    # optional feet (dashed)
    o.append(_rect(150, 174, 40, 16, "#ffffff", S, 1.2, "5 4"))
    o.append(_rect(420, 174, 40, 16, "#ffffff", S, 1.2, "5 4"))
    o.append(_lbl(470, 186, "chân đế (tuỳ chọn)", "ts"))
    # labels
    o.append(_lbl(305, 118, "vỏ", "ts", "middle"))
    o.append(_lbl(176, 110, "ổ bi", "ts", "middle"))
    o.append(_lbl(112, 112, "rãnh then", "ts", "middle"))
    o.append(_line(88, 116, 76, 124, S, 0.9))
    o.append(_lbl(305, 210, "trục xuyên qua, hai đầu có rãnh then hoặc mặt phẳng để nối khớp", "ts", "middle"))

    return _fig(svg(680, 222, "".join(o),
                    "Cấu tạo chung của một đầu đo mômen xoắn kiểu môđun"),
                "Hình 24.4 · Đầu đo mômen xoắn kiểu môđun, cho thấy các đặc điểm chung và hai cách lắp: "
                "thả nổi hoặc gắn cứng. Ổ bi chỉ dùng cho các mẫu quay. Các đoạn trục nối có rãnh then "
                "hoặc đặc điểm khác để thuận tiện nối mômen.",
                "Figure 24.4 · Modular torque transducer showing generic features and alternative "
                "arrangements for free-floating or rigid mounting. Bearings are used only on rotational "
                "models. Shaft extensions have keyways or other features to facilitate torque coupling.",
                "Mặt cắt đầu đo mômen xoắn kiểu môđun có vỏ, ổ bi, trục và đầu nối",
                "Section of a modular torque transducer with housing, bearings, shaft and connector")


# ---------------------------------------------------------------- 24.5
def fig_24_5():
    o = [_defs()]
    # table top and legs
    o.append(_rect(150, 176, 300, 16, FILL, E, 1.5))
    o.append(_rect(164, 192, 16, 54, "#ffffff", E, 1.2))
    o.append(_rect(420, 192, 16, 54, "#ffffff", E, 1.2))
    # machine under test (dashed)
    o.append(_rect(206, 118, 190, 58, "#ffffff", S, 1.3, "6 4"))
    o.append(_lbl(301, 142, "máy cần đo", "ts", "middle"))
    o.append(_lbl(301, 160, "(đặt trên bàn)", "ts", "middle"))
    # centre of rotation
    o.append(_line(301, 176, 301, 192, E, 1.2))
    o.append(_circ(301, 184, 4, "none", E, 1.2))
    o.append(_lbl(301, 208, "tâm quay", "ts", "middle"))
    # front upright with lever arm
    o.append(_rect(110, 96, 24, 150, FILL, E, 1.5))
    o.append(_circ(122, 132, 7, "#ffffff", E, 1.3))
    o.append(_line(122, 132, 46, 132, E, 1.4))
    o.append(_lbl(84, 126, "r", "t", "middle"))
    o.append(_rect(36, 132, 16, 16, WARM, E, 1.2))
    o.append(_lbl(44, 164, "quả cân", "ts", "middle"))
    o.append(_lbl(122, 88, "trụ trước", "ts", "middle"))
    # keyway in the table
    o.append(_rect(390, 176, 30, 6, WARM, E, 1.1))
    o.append(_lbl(405, 168, "rãnh then", "ts", "middle"))

    return _fig(svg(680, 262, "".join(o),
                    "Hệ đỡ dùng để đo mômen phản lực của một máy quay"),
                "Hình 24.5 · Hệ đỡ dùng để đo mômen phản lực của một máy quay. Trục của máy phải được đặt "
                "chính xác trên “tâm quay”. Các lỗ và rãnh then trên bàn giúp lắp và căn chỉnh máy. Các "
                "lỗ trên trụ phía trước dùng để gắn một tay đòn treo quả cân hiệu chuẩn.",
                "Figure 24.5 · Support system for measuring the reaction torque of a rotating machine. "
                "The axis of the machine must be accurately set on the “center of rotation.” The holes "
                "and keyway in the table facilitate machine mounting and alignment. Holes in the front "
                "upright provide for attaching a lever arm from which calibrating weights may be hung.",
                "Bàn đỡ có trụ trước, tay đòn treo quả cân và máy đặt trên bàn với tâm quay",
                "Support table with front upright, lever arm with weight, and the machine on the table")


# ---------------------------------------------------------------- 24.6
def fig_24_6():
    o = [_defs()]
    cx, cy, r = 200, 178, 82
    o.append(_circ(cx, cy, r, FILL, E, 1.6))
    o.append(_circ(cx, cy, r - 16, "none", S, 1.2))
    o.append(_circ(cx, cy, 7, "#ffffff", E, 1.3))
    # friction block clamped over the rim (top arc)
    o.append(_path("M127,127 A89,89 0 0 1 273,127", E, 7.0))
    o.append(_path("M116,119 A103,103 0 0 1 284,119", E, 1.3))
    # clamping bolts at the block ends
    o.append(_rect(110, 121, 17, 13, WARM, E, 1.1))
    o.append(_rect(273, 121, 17, 13, WARM, E, 1.1))
    o.append(_lbl(108, 152, "bu lông kẹp", "ts", "end"))
    # torque arm and reaction force
    o.append(_line(281, 124, 470, 124, E, 1.6))
    o.append(_arr(470, 124, 470, 160))
    o.append(_lbl(478, 146, "F"))
    o.append(_lbl(376, 116, "r", "t", "middle"))
    o.append(_lbl(470, 180, "lực kế", "ts", "middle"))
    o.append(_lbl(470, 192, "hoặc cân", "ts", "middle"))
    # direct labels
    o.append(_lbl(200, 58, "khối ma sát", "ts", "middle"))
    o.append(_lbl(200, 292, "vành bánh đà", "ts", "middle"))
    o.append(_line(200, 286, 200, 262, S, 1.0))
    o.append(_lbl(548, 214, "làm nguội bằng", "ts", "middle"))
    o.append(_lbl(548, 228, "nước tuần hoàn", "ts", "middle"))
    o.append(_line(498, 208, 274, 219, S, 1.0))

    return _fig(svg(680, 300, "".join(o),
                    "Phanh prony cổ điển: khối ma sát kẹp vành bánh đà, tay đòn đo phản lực"),
                "Hình 24.6 · Một phanh prony cổ điển. Phanh này mang đầy đủ các đặc điểm định nghĩa của "
                "mọi dynamometer hấp thụ: biến cơ năng thành nhiệt và xác định công suất từ các giá trị "
                "đo được của mômen phản lực và tốc độ quay.",
                "Figure 24.6 · A classical prony brake. This brake embodies the defining features of all "
                "absorbing dynamometers: conversion of mechanical work into heat and determination of "
                "power from measured values of reaction torque and rotational velocity.",
                "Bánh đà bị hai khối ma sát kẹp, tay đòn dài r với lực F ở đầu",
                "A flywheel clamped by friction blocks, with a torque arm of length r and force F")


def fig_24_7():
    o = [_defs()]
    # ---- cross-section (left): stators either side of a toothed rotor
    o.append(_rect(52, 96, 78, 118, FILL, E, 1.5))
    o.append(_rect(194, 96, 78, 118, FILL, E, 1.5))
    for i in range(3):
        o.append(_rect(62, 108 + i * 34, 22, 22, WARM, E, 1.2))
        o.append(_rect(240, 108 + i * 34, 22, 22, WARM, E, 1.2))
    o.append(_rect(150, 104, 24, 102, "#ffffff", E, 1.5))
    for i in range(5):
        o.append(_rect(136, 110 + i * 20, 14, 9, E, E, 1.0))
        o.append(_rect(174, 110 + i * 20, 14, 9, E, E, 1.0))
    o.append(_lbl(94, 84, "stato có cuộn dây", "ts", "middle"))
    o.append(_lbl(233, 84, "nước làm mát", "ts", "middle"))
    o.append(_lbl(162, 232, "(a) mặt cắt", "ts", "middle"))
    o.append(_lbl(162, 246, "rôto có răng ở giữa", "ts", "middle"))
    # ---- front view (right)
    cx, cy, r = 512, 152, 82
    o.append(_circ(cx, cy, r, FILL, E, 1.6))
    for i in range(12):
        a = _m.radians(i * 30)
        o.append(_rect(cx + (r + 2) * _m.cos(a) - 6, cy + (r + 2) * _m.sin(a) - 6, 12, 12, E, E, 1.0))
    o.append(_circ(cx, cy, 24, "#ffffff", E, 1.3))
    o.append(_lbl(cx, cy + 4, "trục", "ts", "middle"))
    o.append(_lbl(cx + 66, 62, "G", "tb", "middle"))
    o.append(_line(cx + 62, 68, cx + 58, 96, S, 1.0))
    o.append(_rect(cx - 104, cy - 13, 18, 26, WARM, E, 1.2))
    o.append(_lbl(cx - 95, cy - 20, "S", "tb", "middle"))
    o.append(_lbl(cx, 250, "(b) nhìn chính diện", "ts", "middle"))

    return _fig(svg(680, 258, "".join(o),
                    "Dynamometer dòng xoáy: mặt cắt và hình nhìn chính diện"),
                "Hình 24.7 · Mặt cắt (trái) và hình nhìn chính diện (phải) của một dynamometer dòng xoáy. "
                "G là bánh răng, S là cảm biến tốc độ. Các ống dẫn nước làm mát và cáp cấp điện cho stato "
                "không được vẽ.",
                "Figure 24.7 · Cross-section (left) and front view (right) of an eddy current dynamometer. "
                "G is a gear wheel and S is a speed sensor. Hoses carrying cooling water and cable "
                "carrying electric power to the stator are not shown.",
                "Mặt cắt stato và rôto có răng, cùng hình tròn có răng với cảm biến tốc độ",
                "Section through stator and toothed rotor, plus the toothed front view with speed sensor")


FIGS = [fig_24_1, fig_24_2, fig_24_3, fig_24_4, fig_24_5, fig_24_6, fig_24_7]


def fig(n):
    return FIGS[n - 1]()
