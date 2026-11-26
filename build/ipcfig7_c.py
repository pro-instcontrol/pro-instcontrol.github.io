# -*- coding: utf-8 -*-
"""Vector figure supplier for IPC Chapter 7, figures 7.23 - 7.32.

Registered through ``ipcfig7_common.make_registry()``; the aggregate module
``ipcfig7`` merges this registry with the other two suppliers.
"""
from ipcfig7_common import (BLUE, GREEN, GREY, INK, RED, H, W, T, _ar, _b,
                            _circle, _defs, _ellipse, _fig, _frame, _legend,
                            _line, _path, _poly, _rect, _mk, _series,
                            _wavey, make_registry)

FIGS, _reg = make_registry()


# ------------------------------------------------------------------ helpers
def _rot_ellipse(cx, cy, rx, ry, deg, sw=1.0):
    """An ellipse rotated by ``deg`` degrees about its own centre."""
    return ('<g transform="rotate(%s %s %s)">%s</g>'
            % (_f(deg), _f(cx), _f(cy),
               _ellipse(cx, cy, rx, ry, sw=sw)))


def _f(v):
    return ("%.2f" % v).rstrip("0").rstrip(".")


def _wire(pts, sw=0.9, color=INK):
    return _poly(pts, sw=sw, color=color)


def _open(cx, cy, r=3.2, color=INK):
    return _circle(cx, cy, r, fill="#ffffff", sw=1.0, color=color)


def _ground(cx, y):
    """Ground symbol: stem and three shrinking horizontal bars."""
    return (_line(cx, y, cx, y + 4, sw=1.0)
            + _line(cx - 9, y + 4, cx + 9, y + 4, sw=1.0)
            + _line(cx - 6, y + 8, cx + 6, y + 8, sw=1.0)
            + _line(cx - 3, y + 12, cx + 3, y + 12, sw=1.0))


def _wavy_v(x, y0, y1, amp=2.6, step=7.0, color=INK):
    """A vertical wavy line (rough glass surface or heated electrode)."""
    pts = []
    n = int((y1 - y0) / step)
    for i in range(n + 1):
        yy = y0 + i * step
        pts.append((x + (amp if i % 2 else -amp), min(y1, yy)))
    return _poly(pts, sw=0.9, color=color)


def _cell_end(x, y0, y1, color=GREY):
    """Hatched end seal inside a cell."""
    return _rect(x, y0, 15, y1 - y0, fill="url(#h6)", sw=1.0, stroke=color)


# ---------------------------------------------------------------------- 7.23
@_reg
def fig_f23():
    """Fig. 7.23 - smectic liquid crystal: molecules in distinct layers."""
    o = [_defs()]
    o.append(T(340, 28, "SMECTIC LIQUID CRYSTAL - MOLECULES IN LAYERS", 9.0))
    o.append(_rect(232, 48, 216, 130, fill="#fbfaf7", sw=1.3))
    for yy in (91, 134):
        o.append(_line(236, yy, 444, yy, sw=0.6, dash="4 4", color="#bbbbbb"))
    for yy in (72, 113, 154):
        for xx in (290, 390):
            o.append(_ellipse(xx, yy, 30, 8.5, sw=1.15))
    o.append(T(340, 198, "SMECTIC", 10.0, color=BLUE))
    o.append(T(340, 214, "each layer is ordered like a molecular sheet", 7.4,
               color=GREY))
    return _mk(23, o, "Smectic liquid crystal layers",
               "Cấu trúc tinh thể lỏng smectic: các phân tử xếp thành từng lớp",
               "Smectic liquid crystal: molecules arranged in distinct layers",
               "Sơ đồ ba lớp phân tử tinh thể lỏng smectic, các phân tử hình elip nằm ngang và xếp đều theo từng lớp trong một ô kính.",
               "Diagram of three smectic liquid-crystal layers, with horizontal elliptical molecules aligned in regular rows inside a glass cell.")


# ---------------------------------------------------------------------- 7.24
@_reg
def fig_f24():
    """Fig. 7.24 - nematic liquid crystal: no layered order."""
    o = [_defs()]
    o.append(T(340, 28, "NEMATIC LIQUID CRYSTAL - NO LAYERED ORDER", 9.0))
    o.append(_rect(210, 44, 260, 140, fill="#fbfaf7", sw=1.3))
    dots = [(250, 64), (332, 57), (420, 66), (292, 92), (400, 86),
            (238, 120), (350, 118), (438, 128), (266, 158), (386, 160)]
    for xx, yy in dots:
        o.append(_ellipse(xx, yy, 22, 8, sw=1.1))
    o.append(T(340, 203, "NEMATIC", 10.0, color=BLUE))
    o.append(T(340, 219, "molecules share a direction but form no layers", 7.2,
               color=GREY))
    return _mk(24, o, "Nematic liquid crystal layers",
               "Cấu trúc tinh thể lỏng nematic: phân tử phân bố không theo lớp",
               "Nematic liquid crystal: molecules without layered order",
               "Sơ đồ các phân tử hình elip nằm ngang, phân bố rải rác trong ô nhưng không xếp thành lớp như tinh thể smectic.",
               "Diagram of horizontal elliptical molecules scattered inside a cell with no layered order, in contrast with the smectic structure.")


# ---------------------------------------------------------------------- 7.25
@_reg
def fig_f25():
    """Fig. 7.25 - cholesteric layers with a helical twist."""
    o = [_defs()]
    o.append(T(340, 26, "CHOLESTERIC LIQUID CRYSTAL - TWISTED LAYERS", 9.0))
    for y0 in (38, 92, 146):
        o.append(_rect(235, y0, 210, 46, fill="#fbfaf7", sw=1.2))
    for xx in (272, 324, 376, 428):
        o.append(_ellipse(xx, 53, 15, 5, sw=1.0))
        o.append(_ellipse(xx, 70, 15, 5, sw=1.0))
        o.append(_ellipse(xx, 107, 5, 15, sw=1.0))
        o.append(_ellipse(xx, 124, 5, 15, sw=1.0))
        o.append(_rot_ellipse(xx, 161, 15, 5, 35))
        o.append(_rot_ellipse(xx, 178, 15, 5, 35))
    o.append(T(340, 205, "CHOLESTERIC", 10.0, color=BLUE))
    o.append(T(340, 221, "each successive layer is rotated about the axis", 7.2,
               color=GREY))
    return _mk(25, o, "Cholesteric liquid crystal layers",
               "Cấu trúc tinh thể lỏng cholesteric: các lớp xoắn lần nhau",
               "Cholesteric liquid crystal: successive layers with a helical twist",
               "Ba lớp phân tử xếp chồng: lớp trên nằm ngang, lớp giữa đứng thẳng, lớp dưới nghiêng, thể hiện sự xoắn kiểu cholesteric.",
               "Three stacked molecular layers: horizontal ellipses on top, vertical ellipses in the middle and tilted ellipses below, showing the cholesteric helical twist.")


# --------------------------------------------------------- 7.26 / 7.27 cells
def _scatter_cell(voltage):
    """Shared cross-section for figs. 7.26 and 7.27."""
    o = [_defs()]
    tag = ("VOLTAGE APPLIED - OPAQUE STATE" if voltage
           else "NO VOLTAGE - TRANSPARENT STATE")
    o.append(T(340, 26, "DYNAMIC-SCATTERING LCD CELL - " + tag, 9.0))
    # glass plates and cell cavity
    o.append(_rect(105, 70, 415, 13, fill="#fbfaf7", sw=1.1))
    o.append(_rect(105, 167, 415, 13, fill="#fbfaf7", sw=1.1))
    o.append(_rect(105, 83, 415, 84, fill="#ffffff", sw=1.1))
    # end seals
    o.append(_cell_end(114, 83, 167))
    o.append(_cell_end(496, 83, 167))
    # transparent electrodes (metal-oxide coating)
    o.append(_rect(360, 83, 136, 15, fill="url(#h6)", sw=1.0))
    o.append(_rect(360, 152, 136, 15, fill="url(#h6)", sw=1.0))
    # incoming light beams
    for xx in (180, 245, 310):
        o.append(_ar(xx, 48, xx, 205, color=BLUE, sw=1.4))
    # molecular arrangement
    if voltage:
        for xx, yy, ang in [(388, 108, 28), (430, 114, -34), (472, 106, 18),
                            (400, 138, -22), (456, 140, 40)]:
            o.append(_rot_ellipse(xx, yy, 9, 4.5, ang, sw=1.0))
        o.append(_ar(428, 148, 428, 118, color=RED, sw=1.5))
        o.append(T(428, 204, "Opaque", 7.8, color=RED))
        o.append(_ar(428, 198, 428, 168, color=RED, sw=1.0))
    else:
        for xx in (148, 212, 277):
            for yy in (108, 146):
                o.append(_ellipse(xx, yy, 6.5, 11, sw=1.05))
    # right-hand voltage bracket
    o.append(_open(547, 98))
    o.append(_open(547, 166))
    o.append(_line(547, 102, 547, 162, sw=1.0))
    o.append(_ar(547, 118, 547, 104, sw=1.0))
    o.append(_ar(547, 146, 547, 160, sw=1.0))
    o.append(T(563, 132, "Voltage applied" if voltage else "No voltage",
               7.8, anchor="start"))
    # labels
    o.append(T(105, 62, "Glass", 7.6, anchor="start"))
    o.append(_ar(111, 65, 114, 72, sw=0.9))
    o.append(T(105, 213, "Glass", 7.6, anchor="start"))
    o.append(_ar(111, 208, 114, 200, sw=0.9))
    o.append(T(105, 132, "Sealing", 7.6, anchor="end"))
    o.append(_ar(133, 130, 112, 130, sw=0.9))
    o.append(T(245, 222, "Light", 7.8, color=BLUE))
    o.append(T(428, 225, "Metal oxide coating", 7.6, anchor="middle"))
    o.append(_ar(428, 217, 428, 168, sw=0.9, color=GREY))
    return o


@_reg
def fig_f26():
    """Fig. 7.26 - dynamic-scattering LCD cell, no voltage applied."""
    return _mk(26, _scatter_cell(False), "Dynamic-scattering LCD cell, no voltage",
               "Ô LCD tán xạ động khi chưa có điện áp: trạng thái trong suốt",
               "Dynamic-scattering LCD cell with no voltage: transparent state",
               "Sơ đồ ô LCD có hai bản kính, lớp phủ oxit kim loại làm điện cực và keo bịt hai đầu; khi chưa có điện áp các phân tử thẳng hàng và ánh sáng đi xuyên qua.",
               "Cross-section of a dynamic-scattering LCD cell with two glass plates, metal-oxide electrode coating and end seals; with no voltage the molecules stay aligned and light passes straight through.")


@_reg
def fig_f27():
    """Fig. 7.27 - the same cell with voltage applied (opaque state)."""
    return _mk(27, _scatter_cell(True), "Dynamic-scattering LCD cell, voltage applied",
               "Ô LCD tán xạ động khi có điện áp: trạng thái mờ đục",
               "Dynamic-scattering LCD cell with voltage applied: opaque state",
               "Sơ đồ ô LCD tương tự khi đặt điện áp vào lớp phủ oxit kim loại; các phân tử bị xáo trộn, ánh sáng bị tán xạ và vùng hiển thị trở nên mờ đục.",
               "The same LCD cell with voltage applied across the metal-oxide coating; the molecular alignment is disturbed, light is scattered and the active area becomes opaque.")


# ---------------------------------------------------------------------- 7.28
@_reg
def fig_f28():
    """Fig. 7.28 - seven-segment LCD layout with a common connection."""
    o = [_defs()]
    o.append(T(340, 26, "SEVEN-SEGMENT LCD LAYOUT WITH COMMON CONNECTION", 9.0))
    o.append(_rect(120, 38, 180, 170, fill="#fbfaf7", sw=1.2))
    # seven segments (filled electrodes) with their letter labels
    segs = {
        "a": (199, 46, 22, 8), "b": (232, 73, 8, 24),
        "c": (232, 132, 8, 24), "d": (199, 166, 22, 8),
        "e": (180, 132, 8, 24), "f": (180, 73, 8, 24),
        "g": (199, 104, 22, 8),
    }
    lab = {"a": (192, 44), "b": (225, 87), "c": (225, 146), "d": (192, 180),
           "e": (172, 141), "f": (172, 80), "g": (172, 105)}
    for name, (x, y, w, h) in segs.items():
        o.append(_rect(x, y, w, h, fill=INK, sw=0))
    for name, (x, y) in lab.items():
        o.append(T(x, y, name, 8.0, anchor="end"))
    # common bus down the left side of the display
    o.append(_line(150, 50, 150, 196, sw=0.9))
    for yc, xe in ((50, 199), (85, 180), (108, 199), (144, 180), (170, 199)):
        o.append(_line(150, yc, xe, yc, sw=0.9))
    # individual leads to the terminals on the right
    routes = {
        "a": [(221, 50), (470, 50), (470, 46), (480, 46)],
        "b": [(240, 85), (460, 85), (460, 70), (480, 70)],
        "c": [(240, 144), (450, 144), (450, 98), (480, 98)],
        "d": [(221, 170), (440, 170), (440, 124), (480, 124)],
        "Common": [(150, 196), (430, 196), (430, 148), (480, 148)],
        "e": [(180, 156), (180, 162), (420, 162), (420, 170), (480, 170)],
        "g": [(221, 108), (410, 108), (410, 192), (480, 192)],
        "f": [(180, 73), (180, 62), (400, 62), (400, 214), (480, 214)],
    }
    for name, pts in routes.items():
        o.append(_wire(pts))
    for name, yy in (("a", 46), ("b", 70), ("c", 98), ("d", 124),
                     ("Common", 148), ("e", 170), ("g", 192), ("f", 214)):
        o.append(_open(480, yy, r=2.4))
        o.append(T(491, yy + 3, name, 7.6, anchor="start"))
    o.append(T(340, 228, "Seven segment crystal display unit", 7.6, color=GREY))
    return _mk(28, o, "Seven-segment LCD layout",
               "Bố trí LCD bảy đoạn với điểm nối chung",
               "Seven-segment LCD layout with a common connection",
               "Sơ đồ bảy đoạn a đến g của LCD, mỗi đoạn có đường dẫn riêng tới cọc ra và một đầu nối chung, được bọc trong khối hiển thị.",
               "Layout of the seven LCD segments a to g, each with its own lead to a terminal and a shared common connection inside the display unit.")


# ---------------------------------------------------------------------- 7.29
@_reg
def fig_f29():
    """Fig. 7.29 - Nixie tube with anode and ten digit cathodes 0-9."""
    o = [_defs()]
    o.append(T(340, 26, "NIXIE TUBE - ANODE AND TEN DIGIT CATHODES", 9.0))
    # glass envelope
    o.append(_path("M 150 100 H 520 A 32 32 0 0 1 520 164 H 150 "
                   "A 32 32 0 0 1 150 100 Z", sw=1.3))
    # anode bar, resistor and positive supply
    o.append(_line(160, 112, 510, 112, sw=3.2))
    o.append(_line(335, 112, 335, 76, sw=1.0))
    o.append(_poly([(331, 76), (339, 72), (331, 68), (339, 64),
                    (331, 60), (339, 56), (335, 52)], sw=1.0))
    o.append(_line(335, 52, 335, 46, sw=1.0))
    o.append(_open(335, 42, r=3.0))
    o.append(T(320, 45, "+", 9.0, color=RED, anchor="end"))
    o.append(T(372, 78, "Anode", 7.8, anchor="start"))
    o.append(_ar(368, 80, 348, 106, sw=0.9))
    # ten cathodes
    o.append(T(70, 170, "Cathodes", 7.8, anchor="start"))
    o.append(_ar(130, 168, 150, 168, sw=0.9))
    o.append(_line(130, 200, 505, 200, sw=1.0))
    for i in range(10):
        xx = 155 + i * 38
        o.append(_circle(xx, 130, 3.2, fill=INK, sw=0))
        o.append(_line(xx, 133, xx, 163, sw=1.0))
        o.append(_open(xx, 167, r=3.4))
        o.append(_line(xx - 7, 193, xx + 5, 181, sw=1.0))
        o.append(_open(xx - 7, 195, r=3.2))
        o.append(_line(xx - 7, 198, xx - 7, 200, sw=0.9))
        o.append(T(xx, 217, str(i), 8.0))
    # common return and ground
    o.append(_line(130, 200, 130, 205, sw=1.0))
    o.append(_ground(130, 205))
    return _mk(29, o, "Nixie tube with digit-shaped cathodes",
               "Ống Nixie với anôt và mười catôt dạng chữ số 0 đến 9",
               "Nixie tube with an anode and ten digit-shaped cathodes 0-9",
               "Sơ đồ ống phóng điện có anôt dạng thanh nối với nguồn dương qua điện trở và mười catôt hình chữ số 0 đến 9, mỗi catôt có công tắc nối về đường chung.",
               "Diagram of a gas-discharge tube with a bar anode fed from the positive supply through a resistor and ten digit-shaped cathodes 0-9, each with a switch to the common line.")


# ---------------------------------------------------------------------- 7.30
@_reg
def fig_f30():
    """Fig. 7.30 - fifteen-segment Nixie tube for alphanumeric display."""
    o = [_defs()]
    o.append(T(340, 24, "FIFTEEN-SEGMENT NIXIE TUBE", 9.0))
    # bulb envelope with flared base
    o.append(_path("M 165 195 C 150 150 155 92 220 62 C 260 44 340 44 380 62 "
                   "C 445 92 450 150 435 195 L 470 208 L 130 208 Z", sw=1.3))
    o.append(_rect(190, 70, 220, 120, fill="none", sw=1.0,
                   stroke=GREY, dash="5 4"))
    strokes = [
        ((240, 78), (360, 78)),      # top horizontal
        ((214, 88), (214, 128)),     # upper-left vertical
        ((386, 88), (386, 128)),     # upper-right vertical
        ((240, 130), (360, 130)),    # middle horizontal
        ((214, 132), (214, 172)),    # lower-left vertical
        ((386, 132), (386, 172)),    # lower-right vertical
        ((240, 178), (360, 178)),    # bottom horizontal
        ((300, 80), (300, 126)),     # centre vertical, upper
        ((300, 134), (300, 176)),    # centre vertical, lower
        ((242, 86), (290, 126)),     # upper-left diagonal
        ((358, 86), (310, 126)),     # upper-right diagonal
        ((242, 174), (290, 136)),    # lower-left diagonal
        ((358, 174), (310, 136)),    # lower-right diagonal
        ((210, 184), (180, 202)),    # lower-left outer diagonal
        ((390, 184), (420, 202)),    # lower-right outer diagonal
    ]
    for (x1, y1), (x2, y2) in strokes:
        o.append(_line(x1, y1, x2, y2, sw=1.9))
    for i in range(8):
        xx = 250 + i * 14.3
        o.append(_line(xx, 208, xx, 228, sw=1.0))
    o.append(T(340, 38, "15 segments - decimal digits and letters", 7.2,
               color=GREY))
    return _mk(30, o, "Fifteen-segment Nixie tube",
               "Ống Nixie mười lăm đoạn dùng để hiển thị chữ cái",
               "Fifteen-segment Nixie tube for alphanumeric display",
               "Sơ đồ ống Nixie có mười lăm đoạn phát sáng gồm các nét ngang, dọc và chéo bên trong khung đứt nét, với các chân đế bên dưới.",
               "Diagram of a fifteen-segment Nixie tube whose glowing strokes include horizontal, vertical and diagonal segments inside a dashed outline, with pins along the base.")


# ---------------------------------------------------------------------- 7.31
@_reg
def fig_f31():
    """Fig. 7.31 - liquid-vapour display cell (LVD)."""
    o = [_defs()]
    o.append(T(340, 22, "LIQUID-VAPOUR DISPLAY CELL", 9.0))
    # cell outline
    o.append(_rect(180, 55, 290, 140, fill="#fbfaf7", sw=1.1))
    # rough front glass, heated electrode and painted rear block
    o.append(_line(180, 55, 180, 195, sw=1.1))
    o.append(_wavy_v(194, 58, 192, amp=2.4, step=6))
    o.append(_wavy_v(225, 58, 192, amp=5.0, step=14, color=BLUE))
    o.append(_line(445, 55, 445, 195, sw=1.0))
    o.append(_rect(456, 55, 14, 140, fill=INK, sw=0))
    # viewer
    o.append(T(70, 118, "Viewer", 7.8, anchor="start"))
    o.append(_ar(118, 124, 172, 124, sw=1.2))
    # heating circuit
    o.append(_line(225, 55, 225, 35, sw=1.0))
    o.append(_line(225, 35, 275, 35, sw=1.0))
    o.append(_rect(275, 28, 45, 14, fill="#ffffff", sw=1.0))
    o.append(_line(281, 40, 314, 30, sw=1.0))
    o.append(_line(320, 35, 360, 35, sw=1.0))
    o.append(_line(360, 28, 360, 42, sw=1.4))
    o.append(_line(368, 31, 368, 39, sw=1.4))
    o.append(T(382, 32, "Eb", 7.8, anchor="start"))
    o.append(_line(368, 35, 510, 35, sw=1.0))
    o.append(_line(510, 35, 510, 72, sw=1.0))
    o.append(_ground(510, 72))
    # labels
    o.append(T(145, 213, "Rough glass surface", 7.4, anchor="end"))
    o.append(_ar(158, 208, 190, 190, sw=0.9))
    o.append(T(240, 213, "Electrode", 7.4, anchor="start"))
    o.append(_ar(238, 208, 227, 190, sw=0.9))
    o.append(T(520, 130, "Painted block", 7.8, anchor="start"))
    o.append(_ar(516, 128, 472, 128, sw=0.9))
    return _mk(31, o, "Liquid-vapour display cell",
               "Ô hiển thị lỏng-hơi: bề mặt kính nhám và bản cực gia nhiệt",
               "Liquid-vapour display cell with rough glass and a heated electrode",
               "Sơ đồ ô chứa chất lỏng giữa kính nhám và khối sơn đen; bản cực mỏng nhúng trong lỏng được nguồn Eb đốt nóng qua công tắc, người xem quan sát từ bên trái.",
               "Diagram of a cell with liquid between rough glass and a painted dark block; a thin electrode dipped in the liquid is heated by supply Eb through a switch, with the viewer on the left.")


# ---------------------------------------------------------------------- 7.32
@_reg
def fig_f32():
    """Fig. 7.32 - electrophoretic display cell (EPI)."""
    o = [_defs()]
    o.append(T(330, 24, "ELECTROPHORETIC DISPLAY CELL (EPI)", 9.0))
    # glass plates and base
    o.append(_rect(150, 58, 360, 14, fill="#fbfaf7", sw=1.1))
    o.append(_rect(150, 171, 360, 14, fill="#fbfaf7", sw=1.1))
    o.append(_rect(150, 72, 360, 99, fill="#ffffff", sw=1.1))
    # electrodes: left segmented, right common
    o.append(_rect(160, 72, 14, 99, fill="url(#h6)", sw=1.0))
    o.append(_rect(496, 72, 14, 99, fill="url(#h6)", sw=1.0))
    # liquid texture
    for yy in (90, 102, 114, 126, 138, 150):
        o.append(_line(184, yy, 492, yy, sw=0.8, dash="6 5",
                       color="#a9a9a9"))
    # pigment particles gathered at the two electrodes
    for i in range(11):
        o.append(_circle(184 + i * 11, 87, 3.0, fill="#ffffff", sw=0.9))
        o.append(_circle(376 + i * 11, 158, 3.0, fill="#ffffff", sw=0.9))
    # segmented electrode gap in the lower plate
    o.append(_rect(300, 171, 90, 8, fill="#ffffff", sw=1.0))
    # drive circuits
    o.append(_wire([(167, 185), (167, 195), (110, 195), (110, 211)]))
    o.append(_ground(110, 211))
    o.append(_wire([(503, 72), (540, 72), (540, 196)]))
    o.append(_line(528, 196, 552, 196, sw=1.4))
    o.append(_line(533, 202, 547, 202, sw=1.4))
    o.append(T(560, 201, "Ea", 7.8, anchor="start"))
    o.append(_line(540, 202, 540, 210, sw=1.0))
    o.append(_ground(540, 210))
    # labels
    o.append(T(145, 100, "Pigment particles", 7.4, anchor="end"))
    o.append(_ar(152, 98, 184, 88, sw=0.9))
    o.append(T(145, 166, "Electrode", 7.4, anchor="end"))
    o.append(_ar(152, 164, 162, 158, sw=0.9))
    o.append(T(520, 50, "Glass plate", 7.6, anchor="start"))
    o.append(_ar(516, 52, 480, 60, sw=0.9))
    o.append(T(520, 74, "Electrode (common)", 7.4, anchor="start"))
    o.append(_ar(516, 76, 504, 82, sw=0.9))
    o.append(T(520, 134, "Liquid", 7.6, anchor="start"))
    o.append(_ar(516, 132, 494, 130, sw=0.9))
    o.append(T(345, 212, "Base", 7.6, anchor="start"))
    o.append(_ar(340, 208, 322, 187, sw=0.9))
    return _mk(32, o, "Electrophoretic display cell",
               "Ô hiển thị điện di EPI với các hạt sắc tố trong chất lỏng",
               "Electrophoretic (EPI) display cell with pigment particles in liquid",
               "Sơ đồ ô EPI gồm hai bản kính, điện cực chung và điện cực đoạn, chất lỏng có các hạt sắc tố di chuyển khi đặt điện áp; phần đế nằm bên dưới.",
               "Cross-section of an EPI cell with two glass plates, a common electrode and segmented electrodes; charged pigment particles suspend in the liquid and migrate under an applied voltage, with the base below.")
