# -*- coding: utf-8 -*-
"""Vector figures 5-8 for PPIC chapter 4 (fuzzy fault detection).

All markup is produced with the shared primitives in ``ppicfig4_common``;
``make_registry`` collects the evaluated figure tuples for the aggregator.
"""
import math

from ppicfig4_common import (BLUE, GREEN, GREY, INK, RED, W, H, T, _ar, _b,
                             _circle, _defs, _fig, _frame, _legend, _line, _path,
                             _poly, _rect, _series, _tri_membership, _mk,
                             make_registry)

FIGS, _reg = make_registry()


@_reg
def fig_f05():
    """Reactor core exit temperature trace with a spurious spike."""
    o = [_defs()]
    x0, y0, w, h = 72.0, 38.0, 552.0, 224.0
    xt = [(v, str(v)) for v in range(0, 351, 50)]
    yt = [(v, str(v)) for v in range(700, 881, 20)]
    body, mx, my = _frame(x0, y0, w, h, (0, 350), (700, 880),
                          xt, yt, "Time (min)", "Temperature (°F)")
    o.append(body)

    # Piecewise-linear reconstruction of the printed startup trace:
    # ramp to 755 F, plateau near 780 F, one narrow spike, then three steps.
    anchors = [
        (0, 702), (25, 702), (35, 705), (45, 716), (55, 734), (65, 750),
        (75, 757), (82, 755), (92, 753), (100, 756), (110, 770),
        (122, 779), (150, 779), (172, 779), (176, 779),
        (177, 872), (178, 779), (182, 780), (190, 793), (200, 804),
        (215, 805), (230, 806), (238, 818), (245, 832), (260, 833),
        (272, 834), (278, 838), (286, 858), (295, 869), (305, 870),
        (320, 869), (335, 871), (350, 870),
    ]
    pts = []
    for i, (a, b) in enumerate(zip(anchors, anchors[1:])):
        steps = max(1, int((b[0] - a[0]) / 4))
        for k in range(steps):
            t = a[0] + (b[0] - a[0]) * k / steps
            v = a[1] + (b[1] - a[1]) * k / steps
            v += 0.55 * math.sin(i * 2.3 + k * 1.7)
            pts.append((t, v))
    pts.append(anchors[-1])
    o.append(_series(pts, mx, my, BLUE, dot=0.7))
    o.append(T(298, 28, "spurious spike", 7.0, color=RED, anchor="start"))
    o.append(_line(347, 32, mx(177) - 3, my(872) - 3, color=RED, sw=0.8))

    return _mk(5, o,
               "Reactor core exit temperature measurement with spurious behavior",
               "Đo nhiệt độ đầu ra lò phản ứng với hành vi giả tạo",
               "Reactor core exit temperature measurement with spurious "
               "behavior during startup operations",
               "Đồ thị nhiệt độ đầu ra lò phản ứng với một xung nhiễu giả tạo",
               "Temperature trace over 0 to 350 minutes with a stepwise rise "
               "and one narrow spurious spike near 177 minutes")


@_reg
def fig_f06():
    """Signal flow between the two processing stages and the FLDM."""
    o = [_defs()]
    o.append(T(154, 26, "Measurements", 8.0))
    for xx in (114, 154, 194):
        o.append(_ar(xx, 32, xx, 48, color=INK, sw=1.0))

    o.append(_b(52, 50, 204, 56,
                "Stage 1\nGeneral-purpose signal\nprocessing modules", size=7.4))
    o.append(_b(388, 50, 210, 56,
                "Stage 2\nSystem-specific signal\nprocessing techniques", size=7.4))
    o.append(_ar(256, 78, 388, 78, color=INK, sw=1.2))

    o.append(_b(252, 142, 176, 70,
                "Fuzzy logic\n- Fuzzifier\n- Inference engine\n- Defuzzifier",
                size=7.4))
    o.append(_b(38, 244, 216, 64,
                "Knowledge base\n(If-then rules)\n- Physical relations\n"
                "- Operator experience\n- Expert knowledge", size=7.0))
    o.append(_b(426, 244, 216, 64,
                "Database\n- Component reliability\n- Historical trends\n"
                "- Maintenance records\n- Sensor accuracy", size=7.0))

    # Two-way exchange between the FLDM and each surrounding element.
    for x1, y1, x2, y2 in (
        (228, 106, 278, 142), (292, 142, 242, 106),
        (420, 106, 404, 142), (388, 142, 408, 106),
        (280, 212, 218, 244), (210, 244, 272, 212),
        (400, 212, 460, 244), (452, 244, 392, 212),
    ):
        o.append(_ar(x1, y1, x2, y2, color=INK, sw=1.0))

    return _mk(6, o,
               "Connection between fuzzy decision making and signal validation",
               "Liên kết giữa ra quyết định logic mờ và xử lý tín hiệu",
               "Connection between the fuzzy logic decision making and the "
               "signal processing modules and other related information of "
               "importance",
               "Sơ đồ luồng từ phép đo qua hai giai đoạn xử lý tới bộ logic mờ, "
               "tri thức và cơ sở dữ liệu",
               "Signal-flow diagram: measurements feed two processing stages; "
               "a fuzzy logic core exchanges information with a knowledge base "
               "and a database")


@_reg
def fig_f07():
    """Tree database: plant, measurement type, location and sensors."""
    o = [_defs()]

    def node(cx, cy, ww, hh, label, size=7.2):
        return _b(cx - ww / 2.0, cy - hh / 2.0, ww, hh, label, size=size)

    sensors = [
        (56, "T1"), (121, "F1"), (186, "P1"), (251, "T2"), (316, "T3"),
        (381, "P2"), (446, "F2"), (511, "P3"), (576, "T4"), (641, "F3"),
    ]

    # Links first so that node frames mask the line ends.
    for ex in (166, 500):
        o.append(_line(340, 48, ex, 66, color=INK, sw=0.9))
    for ex in (76, 176, 270):
        o.append(_line(166, 86, ex, 108, color=INK, sw=0.9))
    for ex in (386, 480, 574):
        o.append(_line(500, 86, ex, 108, color=INK, sw=0.9))

    by_type = {76: (56, 251, 316, 576),
               176: (121, 446, 641),
               270: (186, 381, 511)}
    by_site = {386: (56, 121, 186, 251),
               480: (316, 381, 446, 511),
               574: (576, 641)}
    for src, targets in by_type.items():
        for sx in targets:
            o.append(_line(src, 128, sx, 248, color=BLUE, sw=0.55))
    for src, targets in by_site.items():
        for sx in targets:
            o.append(_line(src, 128, sx, 248, color=GREEN, sw=0.55))

    o.append(node(340, 38, 56, 20, "Plant", size=7.4))
    o.append(node(166, 76, 128, 20, "Measurement type"))
    o.append(node(500, 76, 100, 20, "Location"))
    o.append(node(76, 118, 104, 20, "Temperature"))
    o.append(node(176, 118, 56, 20, "Flow"))
    o.append(node(270, 118, 80, 20, "Pressure"))
    o.append(node(386, 118, 84, 20, "System 1"))
    o.append(node(480, 118, 84, 20, "System 2"))
    o.append(node(574, 118, 84, 20, "System 3"))
    for sx, lab in sensors:
        o.append(node(sx, 257, 30, 18, lab, size=7.0))
    o.append(T(340, 286, "Sensors", 8.0))

    return _mk(7, o,
               "Tree-structured plant database",
               "Cơ sở dữ liệu dạng cây mô tả nhà máy và mạng cảm biến",
               "The tree-structured database containing a physical "
               "description of the power plant and its sensory network",
               "Cây phân loại nhà máy theo kiểu đo và vị trí, liên kết tới "
               "các cảm biến T1 đến F3",
               "Tree linking the plant to measurement types and locations, "
               "then to redundant temperature, flow and pressure sensors")


@_reg
def fig_f08():
    """Universe of discourse of the deviation delta fuzzy input."""
    o = [_defs()]
    ox, oy, sx, sy = 90.0, 252.0, 40.0, 170.0

    def X(s):
        return ox + s * sx

    def Y(m):
        return oy - m * sy

    o.append(_ar(ox, oy, ox, 62, color=INK, sw=1.3))
    o.append(_ar(ox, oy, 638, oy, color=INK, sw=1.3))
    for s in range(0, 14):
        o.append(_line(X(s), oy, X(s), oy + 4, color=INK, sw=0.8))
        if s in (0, 3, 6, 9, 12):
            o.append(T(X(s), oy + 14, str(s), 7.2, color=INK))
    for m, lab in ((0, "0"), (1, "1")):
        o.append(_line(ox - 4, Y(m), ox, Y(m), color=INK, sw=0.9))
        o.append(T(ox - 8, Y(m) + 2.5, lab, 7.2, color=INK, anchor="end"))
    o.append(T(X(6.4), 290, "Deviation (σ)", 8.0))

    # Small: falling shoulder; Medium: symmetric triangle; Large: rising
    # ramp that saturates at unity, as printed.
    o.append(_line(X(0), Y(1), X(5.2), Y(0), color=GREEN, sw=1.6, dash="4 3"))
    o.append(_poly([(X(3), Y(0)), (X(6), Y(1)), (X(9), Y(0))],
                   color=RED, sw=1.5, dash="2 2"))
    o.append(_poly([(X(7), Y(0)), (X(9), Y(1))], color=BLUE, sw=2.0))
    o.append(_line(X(9), Y(1), X(13.0), Y(1), color=BLUE, sw=2.0))
    o.append(_ar(X(12.3), Y(1), X(13.5), Y(1), color=BLUE, sw=1.6))

    o.append(T(X(1.0), 98, "Small", 8.5, color=GREEN))
    o.append(T(X(6), Y(0.5) + 3, "Medium", 8.5, color=RED))
    o.append(T(X(11), Y(0.55), "Large", 8.5, color=BLUE))

    return _mk(8, o,
               "Universe of discourse for the deviation fuzzy input",
               "Tập vực thảo luận cho biến đầu vào mờ độ lệch (δ)",
               "Universe of discourse for the deviation (δ) fuzzy input variable",
               "Đồ thị ba hàm thuộc Small, Medium, Large trên trục 0 đến 12σ",
               "Three overlapping fuzzy membership functions Small, Medium "
               "and Large over a deviation range of 0 to 12 sigma")
