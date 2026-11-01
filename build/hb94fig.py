# -*- coding: utf-8 -*-
"""Figures for Handbook Chapter 94 — Electroluminescent Displays
(William A. Barrow, Planar Systems).

Ten figures, 94.1–94.10.

NOTE: never emit <sub>/<sup> inside <svg> text — both are on the HTML parser's
breakout list and eject the parser from SVG foreign content. Subscripts use
<tspan dy=...> via _rich().
"""
import math

from hbfig import _f, svg, _fig, Box

E = "#2a2a2a"
S = "#8a8a8a"
GRID = "#e2e2e2"
GOLD = "#b45309"
BLUE = "#1d4ed8"
TEAL = "#0f766e"


# ---------------------------------------------------------------- helpers
def _lbl(x, y, txt, cls="tm", anchor="start"):
    return ('<text class="%s" x="%s" y="%s" text-anchor="%s">%s</text>'
            % (cls, _f(x), _f(y), anchor, txt))


def _rich(x, y, parts, anchor="start", cls="tm"):
    """parts = [(text, is_sub), ...] — subscript via tspan, never <sub>."""
    s, prev = "", False
    for txt, is_sub in parts:
        if is_sub:
            s += '<tspan font-size="7.6" dy="2.2">%s</tspan>' % txt
        elif prev:
            s += '<tspan dy="-2.2">%s</tspan>' % txt
        else:
            s += txt
        prev = is_sub
    return ('<text class="%s" x="%s" y="%s" text-anchor="%s">%s</text>'
            % (cls, _f(x), _f(y), anchor, s))


def _vlab(x, y, txt, cls="ts"):
    return ('<text class="%s" x="%s" y="%s" text-anchor="middle" '
            'transform="rotate(-90 %s %s)">%s</text>'
            % (cls, _f(x), _f(y), _f(x), _f(y), txt))


def _defs(tag):
    return ('<defs>'
            '<marker id="a%s" markerWidth="9" markerHeight="9" refX="7" refY="3" '
            'orient="auto"><path d="M0,0 L7,3 L0,6 z" fill="%s"/></marker>'
            '<marker id="h%s" markerWidth="7" markerHeight="7" refX="5" refY="2.4" '
            'orient="auto"><path d="M0,0 L5,2.4 L0,4.8 z" fill="%s"/></marker>'
            '<style>.ts{font:9.5px Inter,Helvetica,sans-serif;fill:#666}'
            '.tm{font:9.5px Inter,Helvetica,sans-serif;fill:#222}'
            '.tf{font:11px "Cambria Math",Georgia,serif;fill:#111}'
            '.tb{font:9.5px Inter,Helvetica,sans-serif;fill:#111;font-weight:700}'
            '.tcap{font:9px Inter,Helvetica,sans-serif;fill:#555}'
            '.txs{font:8px Inter,Helvetica,sans-serif;fill:#444}'
            '</style></defs>' % (tag, E, tag, E))


def _line(x1, y1, x2, y2, sw=1.2, col=E, dash=""):
    d = ' stroke-dasharray="%s"' % dash if dash else ""
    return ('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="%s"%s/>'
            % (_f(x1), _f(y1), _f(x2), _f(y2), col, sw, d))


def _arr(x1, y1, x2, y2, tag="941", sw=1.15, col=E, head="a"):
    return ('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="%s" '
            'marker-end="url(#%s%s)"/>'
            % (_f(x1), _f(y1), _f(x2), _f(y2), col, sw, head, tag))


def _rect(x, y, w, h, sw=1.2, fill="#fff", dash="", col=E):
    d = ' stroke-dasharray="%s"' % dash if dash else ""
    return ('<rect x="%s" y="%s" width="%s" height="%s" fill="%s" stroke="%s" '
            'stroke-width="%s"%s/>'
            % (_f(x), _f(y), _f(w), _f(h), fill, col, sw, d))


def _poly(pts, sw=1.2, fill="#fff", col=E, dash=""):
    d = ' stroke-dasharray="%s"' % dash if dash else ""
    s = " ".join("%s,%s" % (_f(a), _f(b)) for a, b in pts)
    return ('<polygon points="%s" fill="%s" stroke="%s" stroke-width="%s"%s/>'
            % (s, fill, col, sw, d))


def _path(pts, sw=1.5, col=E, dash="", fill="none"):
    d = ' stroke-dasharray="%s"' % dash if dash else ""
    s = "M" + " L".join("%s %s" % (_f(a), _f(b)) for a, b in pts)
    return ('<path d="%s" fill="%s" stroke="%s" stroke-width="%s"%s/>'
            % (s, fill, col, sw, d))


def _dot(x, y, r=2.4, col=E):
    return '<circle cx="%s" cy="%s" r="%s" fill="%s"/>' % (_f(x), _f(y), _f(r), col)


def _hatch(tag, x, y, w, h, step=9, col="#9a9a9a"):
    """Diagonal hatching clipped to a rectangle (used for the glass substrate)."""
    o = ['<clipPath id="c%s"><rect x="%s" y="%s" width="%s" height="%s"/></clipPath>'
         % (tag, _f(x), _f(y), _f(w), _f(h)),
         '<g clip-path="url(#c%s)">' % tag]
    k = -int(h)
    while k < w + h:
        o.append(_line(x + k, y + h, x + k + h, y, 0.7, col))
        k += step
    o.append("</g>")
    return "".join(o)


def _blk(x, y, w, h, parts, cls="tm", sw=1.2, fill="#fff"):
    o = [_rect(x, y, w, h, sw, fill)]
    n = len(parts)
    for i, ln in enumerate(parts):
        cy = y + h / 2.0 + (i - (n - 1) / 2.0) * 12 + 3.4
        if isinstance(ln, list):
            o.append(_rich(x + w / 2.0, cy, ln, "middle", cls))
        else:
            o.append(_lbl(x + w / 2.0, cy, ln, cls, "middle"))
    return "".join(o)


# ---------------------------------------------------------------- 94.1
def fig_94_1():
    tag = "941"
    o = [_defs(tag)]
    top, bot = 58, 232

    # transparent substrate
    o.append(_rect(70, top, 66, bot - top, 1.2, "#ffffff"))
    o.append(_hatch(tag, 70, top, 66, bot - top))

    # the thin active layers, left to right
    layers = [(140, 12, ""), (156, 16, ""), (176, 34, ""), (214, 16, ""), (234, 10, "")]
    for x, w, _ in layers:
        o.append(_rect(x, top, w, bot - top, 1.1, "#ffffff"))

    o.append(_lbl(103, top - 12, "TRANSPARENT", "tb", "middle"))
    o.append(_lbl(103, top - 2, "SUBSTRATE", "tb", "middle"))

    # leader labels to the right
    for ly, txt, tx in [(76, "ITO", 146), (104, "LOWER INSULATOR", 164),
                        (140, "PHOSPHOR (ZnS:Mn)", 193), (176, "UPPER INSULATOR", 222),
                        (206, "ALUMINUM", 239)]:
        o.append(_line(tx, ly, 330, ly, 0.8, S))
        o.append(_lbl(334, ly + 3.4, txt, "tb"))

    # light leaving to the left
    o.append(_arr(66, 146, 30, 146, tag, 1.4))
    o.append(_lbl(30, 134, "LIGHT", "tb"))

    # drive source
    o.append('<circle cx="336" cy="252" r="16" fill="none" stroke="%s" stroke-width="1.2"/>'
             % E)
    o.append('<path d="M328 256 h5 v-8 h6 v8 h5" fill="none" stroke="%s" '
             'stroke-width="1.1"/>' % E)
    o.append(_line(146, bot, 146, 276, 1.1))
    o.append(_line(146, 276, 336, 276, 1.1))
    o.append(_line(336, 276, 336, 268, 1.1))
    o.append(_line(239, bot, 239, 252, 1.1))
    o.append(_line(239, 252, 320, 252, 1.1))

    return _fig(svg(520, 300, "".join(o),
                    "Mặt cắt cấu trúc linh kiện ACTFEL"),
                "Hình 94.1 · Sơ đồ mặt cắt của cấu trúc linh kiện ACTFEL cơ bản.",
                "FIGURE 94.1 · Schematic, cross-sectional diagram of the basic ACTFEL "
                "device structure.",
                "Mặt cắt thẳng đứng của chồng lớp: đế thuỷ tinh trong suốt có gạch chéo, "
                "rồi lần lượt các lớp mỏng ITO, cách điện dưới, chất phát quang ZnS:Mn, "
                "cách điện trên và nhôm. Ánh sáng phát ra theo mũi tên sang trái, nguồn "
                "xoay chiều nối giữa lớp ITO và lớp nhôm",
                "Vertical cross-section of the layer stack: a hatched transparent glass "
                "substrate, then the thin layers ITO, lower insulator, ZnS:Mn phosphor, "
                "upper insulator and aluminium. Light leaves along an arrow to the left; "
                "an ac source connects the ITO and the aluminium layer")


# ---------------------------------------------------------------- 94.2
def fig_94_2():
    tag = "942"
    o = [_defs(tag)]
    x0, w = 88, 266

    # aluminium stripes
    n = 7
    cw = w / float(n)
    for i in range(n):
        o.append(_rect(x0 + i * cw + 3, 62, cw - 8, 10, 1.0, "#ffffff"))
    o.append(_lbl(x0 + w / 2.0, 50, "ALUMINUM", "tb", "middle"))

    o.append(_rect(x0, 80, w, 22, 1.1, "#ffffff"))
    o.append(_lbl(x0 + w / 2.0, 94, "UPPER INSULATOR", "tb", "middle"))

    o.append(_rect(x0, 104, w, 26, 1.1, "#ffffff"))
    for i, name in enumerate(["RED", "GREEN", "BLUE", "RED", "GREEN", "BLUE", "RED"]):
        cx = x0 + i * cw
        if i:
            o.append(_line(cx, 104, cx, 130, 1.0))
        o.append(_lbl(cx + cw / 2.0, 121, name, "txs", "middle"))
    o.append(_line(x0 + w, 117, x0 + w + 34, 117, 0.8, S))
    o.append(_lbl(x0 + w + 38, 120, "PHOSPHORS", "tb"))

    o.append(_rect(x0, 130, w, 22, 1.1, "#ffffff"))
    o.append(_lbl(x0 + w / 2.0, 144, "LOWER INSULATOR", "tb", "middle"))

    o.append(_rect(x0, 152, w, 14, 1.1, "#ffffff"))
    o.append(_line(x0 + w, 159, x0 + w + 34, 159, 0.8, S))
    o.append(_lbl(x0 + w + 38, 162, "ITO", "tb"))

    o.append(_rect(x0, 166, w, 46, 1.1, "#ffffff"))
    o.append(_lbl(x0 + w / 2.0, 193, "SUBSTRATE", "tb", "middle"))

    o.append(_arr(x0 + w / 2.0, 218, x0 + w / 2.0, 258, tag, 1.4))
    o.append(_lbl(x0 + w / 2.0, 274, "LIGHT", "tb", "middle"))

    return _fig(svg(520, 290, "".join(o),
                    "Mặt cắt linh kiện ACTFEL màu"),
                "Hình 94.2 · Sơ đồ mặt cắt của một linh kiện ACTFEL màu, với ba màu sơ cấp "
                "đỏ, lục và lam được tạo ra bằng các vạch chất phát quang màu đã được tạo "
                "hình. Trong hình này các vạch phát quang màu được nhìn theo đầu mút.",
                "FIGURE 94.2 · Schematic, cross-sectional diagram of a color ACTFEL device "
                "with the red, green, and blue primary colors produced by patterned color "
                "phosphor stripes. The color phosphor stripes are end on in this view.",
                "Mặt cắt ngang của chồng lớp: các vạch nhôm rời nhau ở trên cùng, rồi lớp "
                "cách điện trên, dải chất phát quang chia thành bảy ô đỏ, lục, lam lặp "
                "lại, lớp cách điện dưới, lớp ITO và đế. Ánh sáng phát ra theo mũi tên "
                "hướng xuống",
                "Horizontal cross-section of the layer stack: separated aluminium stripes "
                "on top, then the upper insulator, a phosphor band split into seven "
                "repeating red, green and blue cells, the lower insulator, the ITO layer "
                "and the substrate. Light leaves along a downward arrow")


# ---------------------------------------------------------------- 94.3
def fig_94_3():
    tag = "943"
    o = [_defs(tag)]
    ax, ay = 112, 176

    o.append(_line(ax, 52, ax, 292, 1.2))
    o.append(_line(ax, ay, 596, ay, 1.2))
    o.append(_arr(590, ay, 604, ay, tag, 1.0))
    o.append(_arr(ax, 58, ax, 50, tag, 1.0))
    o.append(_rich(ax - 6, 48, [("V", False), ("(t)", False)], "end"))
    o.append(_lbl(610, ay + 4, "t", "tf"))

    # trapezoidal, alternating-polarity waveform
    wav = [(118, ay), (128, ay), (146, 88), (270, 88), (288, ay),
           (370, ay), (388, 264), (468, 264), (486, ay), (566, ay)]
    o.append(_path(wav, 1.7))

    # A-L markers
    marks = [(120, ay, "A", -6, 15), (133, 152, "B", -12, 4),
             (138, 128, "C", -12, 4), (146, 96, "D", -12, 3),
             (266, 82, "E", 3, -6), (288, ay, "F", -12, 14),
             (370, ay, "G", -6, -8), (375, 200, "H", 4, 4),
             (381, 232, "I", 4, 4), (388, 264, "J", -6, 24),
             (468, 264, "K", 4, 24), (486, ay, "L", 4, 15)]
    for mx, my, s, dx, dy in marks:
        o.append(_lbl(mx + dx, my + dy, s, "ts"))

    # Vto / Vth / VP: level indicators standing in the clear gap between the
    # two pulses, so neither arrow is drawn on top of an edge.
    for xv, ytop in ((306, 152), (330, 128), (352, 88)):
        o.append(_arr(xv, ay, xv, ytop, tag, 0.9, S, "h"))
        o.append(_arr(xv, ytop, xv, ay, tag, 0.9, S, "h"))
    o.append(_rich(306, 146, [("V", False), ("to", True)], "middle", "ts"))
    o.append(_rich(330, 122, [("V", False), ("th", True)], "middle", "ts"))
    o.append(_rich(352, 82, [("V", False), ("P", True)], "middle", "ts"))

    return _fig(svg(620, 300, "".join(o),
                    "Dạng sóng xung điều khiển lưỡng cực"),
                "Hình 94.3 · Dạng sóng xung điều khiển lưỡng cực điển hình. Các chữ cái "
                "A–L đánh dấu các điểm trên dạng sóng điều khiển, được tham chiếu về sau "
                "trong các Hình 94.5 và 94.6. Độ rộng xung thường khoảng 30 µs và tần số "
                "nằm trong khoảng 60 đến 500 Hz đối với màn hiển thị ma trận thụ động.",
                "FIGURE 94.3 · Typical alternating polarity, pulse drive waveform. Letters "
                "A–L mark points on the drive waveform which are referenced later in Figs. "
                "94.5 and Fig. 94.6. The pulse width would generally be about 30 µs and the "
                "frequency would be between 60 and 500 Hz for a passive matrix-addressed "
                "display.",
                "Đồ thị điện áp theo thời gian với dạng xung thang lưỡng cực: một xung "
                "dương rồi một xung âm có cùng biên độ. Các chữ cái từ A đến L đánh dấu "
                "các điểm dọc theo sườn lên, đỉnh, sườn xuống và đáy của hai xung; ba mũi "
                "tên hai chiều ghi V th, V to và V P",
                "Voltage against time with a bipolar trapezoidal pulse train: one positive "
                "pulse then an equal negative pulse. Letters A to L mark points along the "
                "rising edge, the plateau, the falling edge and the trough of both pulses; "
                "three double-headed arrows label V-th, V-to and V-P")


# ---------------------------------------------------------------- 94.4
def fig_94_4():
    tag = "944"
    o = [_defs(tag)]
    x_ito, x_i1, x_p2, x_i2 = 96, 190, 440, 520

    # electrode blocks
    o.append(_rect(58, 118, 38, 96, 1.2, "#e8e8e8"))
    o.append(_lbl(77, 170, "ITO", "tb", "middle"))
    o.append(_rect(520, 132, 38, 96, 1.2, "#e8e8e8"))
    o.append(_lbl(539, 184, "Al", "tb", "middle"))

    # band edges
    cond = [(x_ito, 88), (x_i1, 88), (x_p2, 128), (x_i2, 128), (558, 128)]
    val = [(x_ito, 214), (x_i1, 214), (x_p2, 252), (x_i2, 252), (558, 252)]
    o.append(_poly([(x_ito, 88), (x_i1, 88), (x_p2, 128), (x_i2, 128),
                    (x_i2, 252), (x_p2, 252), (x_i1, 214), (x_ito, 214)],
                   0.0, "#f2f2f2", "#f2f2f2"))
    o.append(_path(cond, 1.9))
    o.append(_path(val, 1.9))

    # interface states at the left phosphor boundary
    for sy in (100, 112, 124, 136, 148, 160, 172, 184, 196):
        o.append(_line(x_i1 - 6, sy, x_i1 + 2, sy, 1.1, E))
    o.append(_lbl(150, 66, "INTERFACE", "tb", "middle"))
    o.append(_lbl(150, 76, "STATES", "tb", "middle"))

    # tunnelling electron
    o.append(_arr(196, 118, 216, 96, tag, 1.1))
    o.append(_dot(196, 118, 2.2))

    # hot electron drifting across the phosphor
    o.append(_arr(222, 100, 404, 122, tag, 1.2))

    # Mn2+ centres with impact excitation
    for mx, my in [(262, 152), (330, 176), (396, 196)]:
        o.append(_dot(mx, my, 2.6))
        o.append(_rich(mx + 5, my + 3, [("Mn", False), ("2+", True)], "start", "txs"))
        o.append(_arr(mx - 26, my - 34, mx - 4, my - 6, tag, 0.9, S))
        o.append(_arr(mx - 4, my - 6, mx - 24, my - 38, tag, 0.9, GOLD))

    # layer labels
    o.append(_lbl(240, 246, "ZnS:Mn", "tb", "middle"))
    o.append(_lbl(150, 232, "LOWER", "tb", "middle"))
    o.append(_lbl(150, 244, "INSULATOR", "tb", "middle"))
    o.append(_lbl(476, 226, "UPPER", "tb", "middle"))
    o.append(_lbl(476, 238, "INSULATOR", "tb", "middle"))
    o.append(_line(480, 138, 480, 214, 0.8, S))

    return _fig(svg(600, 270, "".join(o),
                    "Giản đồ vùng năng lượng của linh kiện ACTFEL"),
                "Hình 94.4 · Giản đồ vùng năng lượng của một linh kiện ACTFEL tại đỉnh xung "
                "điện áp đặt vào. Các điện tử đường hầm từ các trạng thái bề mặt "
                "cách điện/chất phát quang vào vùng dẫn, bị quét ngang qua lớp phát quang, "
                "và trên đường đi va chạm kích thích các tâm phát xạ cho tới khi chúng "
                "được nhiệt hoá và bị bẫy tại bề mặt đối diện.",
                "FIGURE 94.4 · Energy band diagram of an ACTFEL device during the peak of "
                "the applied voltage pulse. Electrons tunnel out of insulator/phosphor "
                "interface states into the conduction band, are swept across the phosphor "
                "layer, and impact exciting emission centers as they go until they are "
                "finally thermalized and trapped at the opposite interface.",
                "Giản đồ vùng năng lượng nghiêng từ trái sang phải. Điện cực ITO ở bên "
                "trái, lớp cách điện, rồi tới lớp ZnS:Mn có các tâm Mn hai cộng; một điện "
                "tử đường hầm thoát khỏi trạng thái bề mặt và chạy ngang qua lớp phát "
                "quang, va chạm vào các tâm mangan trên đường đi, cuối cùng bị bẫy ở bề "
                "mặt đối diện gần điện cực nhôm",
                "Energy bands sloping down from left to right. The ITO electrode on the "
                "left, then the insulator, then the ZnS:Mn layer holding Mn-two-plus "
                "centres; an electron tunnels out of an interface state and drifts across "
                "the phosphor, striking the manganese centres on its way before being "
                "trapped at the far interface near the aluminium electrode")


# ---------------------------------------------------------------- 94.5
def fig_94_5():
    tag = "945"
    b = Box(560, 360, (-250, 250), (-4, 4), pad=(74, 26, 30, 56))
    o = [_defs(tag)]
    o.append(b.axes("Điện áp (V)", "Điện tích ngoài (µC/cm²)",
                    xt=[(-250, "−250"), (-150, "−150"), (-50, "−50"),
                        (50, "50"), (150, "150"), (250, "250")],
                    yt=[(-4, "−4"), (-3, "−3"), (-2, "−2"), (-1, "−1"),
                        (0, "0"), (1, "1"), (2, "2"), (3, "3"), (4, "4")]))
    # below-threshold line
    o.append(b.curve([(-250, -1.35), (250, 1.35)], "c3"))
    # the open loop
    loop = [(-200, -2.9), (-205, -2.6), (-170, -1.5), (-140, 1.2),
            (-60, 1.45), (-35, 1.5), (200, 2.95), (185, 2.6),
            (150, 0.6), (100, -1.4), (-100, -2.35), (-120, -2.5), (-200, -2.9)]
    o.append(b.curve(loop, "c1"))
    marks = [(-200, -2.9, "K", 2, 14), (-205, -2.6, "J", -14, 2),
             (-170, -1.5, "I", -12, 0), (-140, 1.2, "H", -2, -8),
             (-60, 1.45, "G", -2, -8), (-35, 1.5, "F", 2, -8),
             (200, 2.95, "E", 4, -6), (185, 2.6, "D", 5, 8),
             (150, 0.6, "C", 6, 0), (100, -1.4, "B", 6, 4),
             (-100, -2.35, "A", -6, -8), (-120, -2.5, "L", -12, -8)]
    for xv, yv, s, dx, dy in marks:
        o.append(_lbl(b.x(xv) + dx, b.y(yv) + dy, s, "ts"))
    # Vto / Vth / VP: downward ticks standing on the voltage axis, keyed to
    # points B, C and D/E of the loop (see the Defining Terms block).
    for xv, sub in ((100, "to"), (150, "th"), (200, "P")):
        o.append(_poly([(b.x(xv) - 4.5, b.y(0) - 8), (b.x(xv) + 4.5, b.y(0) - 8),
                        (b.x(xv), b.y(0) - 1)], 0.9, E))
        o.append(_rich(b.x(xv), b.y(0) + 14, [("V", False), (sub, True)],
                       "middle", "ts"))
    return _fig(svg(560, 360, "".join(o),
                    "Vòng QV lý tưởng của linh kiện ACTFEL"),
                "Hình 94.5 · Vòng QV lý tưởng, không có rò điện tích từ các trạng thái bề "
                "mặt giữa các xung điều khiển. Các chữ cái A–L đánh dấu các điểm trên vòng "
                "QV trùng thời điểm với các điểm A–L trên dạng sóng điều khiển ở Hình 94.3. "
                "Đường đứt là vòng QV cho trường hợp vừa dưới ngưỡng. Đường liền là vòng "
                "mở ở trên ngưỡng. Diện tích vòng QV biểu diễn năng lượng mà linh kiện tiêu "
                "tán trong mỗi chu kỳ của dạng sóng điều khiển.",
                "FIGURE 94.5 · Idealized QV loop with no charge leakage from interface states "
                "between drive pulses. Letters A–L mark points on the QV loop which are "
                "coincident in time with the points labeled A–L on the drive waveform in "
                "Fig. 94.3. The dashed line is the QV loop for the case just below "
                "threshold. The solid line is the open loop above threshold. The area of the "
                "QV loop represents the energy dissipated by the device per cycle of the "
                "drive waveform.",
                "Đồ thị điện tích ngoài theo điện áp. Đường đứt là một đường thẳng nghiêng "
                "nhẹ qua gốc toạ độ ứng với trường hợp dưới ngưỡng. Đường liền khép kín "
                "thành một vòng hình bình hành rộng, đi lên theo cạnh trái, chạy ngang "
                "sang phải tới đỉnh rồi xuống theo cạnh phải; các chữ cái từ A đến L nằm "
                "dọc theo vòng",
                "External charge against voltage. The dashed line is a shallow straight "
                "line through the origin for the below-threshold case. The solid line "
                "closes into a wide parallelogram loop, rising up the left side, running "
                "across to the apex and descending the right side; letters A to L sit along "
                "the loop")


# ---------------------------------------------------------------- 94.6
def fig_94_6():
    tag = "946"
    b = Box(500, 340, (-1.5, 1.5), (-2.5, 2.5), pad=(80, 26, 30, 56))
    o = [_defs(tag)]
    o.append(b.axes("Điện trường trong lớp phát quang (MV/cm)",
                    "Điện tích trong (µC/cm²)",
                    xt=[(-1.5, "−1.5"), (-1, "−1"), (-0.5, "−0.5"), (0, "0"),
                        (0.5, "0.5"), (1, "1"), (1.5, "1.5")],
                    yt=[(-2.5, "−2.5"), (-2, "−2"), (-1.5, "−1.5"), (-1, "−1"),
                        (-0.5, "−0.5"), (0, "0"), (0.5, "0.5"), (1, "1"),
                        (1.5, "1.5"), (2, "2"), (2.5, "2.5")]))
    loop = [(-1.35, 2.3), (1.4, 2.25), (1.45, -1.9), (1.3, -2.3),
            (-1.4, -2.3), (-1.4, 1.5), (-1.35, 2.3)]
    o.append(b.curve(loop, "c1"))
    marks = [(-1.35, 2.3, "E", 4, -6), (-1.4, 1.5, "D", 4, 4),
             (1.4, 2.25, "H", -4, -8), (1.45, -1.9, "J", 4, 0),
             (1.3, -2.3, "K", -2, -8), (-1.4, -2.3, "B", 4, -8)]
    for xv, yv, s, dx, dy in marks:
        o.append(_lbl(b.x(xv) + dx, b.y(yv) + dy, s, "ts"))
    return _fig(svg(500, 340, "".join(o),
                    "Vòng QpFp của linh kiện ACTFEL"),
                "Hình 94.6 · Vòng Q<sub>p</sub>F<sub>p</sub> tương ứng với vòng QV trên "
                "ngưỡng ở Hình 94.5. Vòng này biểu diễn dòng điện tích qua lớp phát quang "
                "như một hàm của điện trường trong lớp phát quang.",
                "FIGURE 94.6 · Q<sub>p</sub>F<sub>p</sub> loop corresponding to the above "
                "threshold QV loop in Fig. 94.5. This loop represents the charge flow "
                "across the phosphor layer as a function of the electric field across the "
                "phosphor layer.",
                "Đồ thị điện tích trong theo điện trường trong lớp phát quang. Đường khép "
                "kín gần như một hình chữ nhật rộng, chạy ngang qua đỉnh từ trái sang "
                "phải, xuống theo cạnh phải, chạy ngược lại theo đáy và lên theo cạnh "
                "trái; các chữ cái B, D, E, H, J, K nằm ở các góc",
                "Internal charge against phosphor field. The closed curve is nearly a wide "
                "rectangle, running across the top from left to right, down the right side, "
                "back along the bottom and up the left side; letters B, D, E, H, J and K "
                "sit at the corners")


# ---------------------------------------------------------------- 94.7 / 94.9 / 94.10
def _tri(x, y, w, h, tag):
    return ('<polygon points="%s,%s %s,%s %s,%s" fill="#fff" stroke="%s" '
            'stroke-width="1.2"/>'
            % (_f(x), _f(y), _f(x), _f(y + h), _f(x + w), _f(y + h / 2.0), E))


def _gpib(o, x1, y1, x2, y2, tag, both=True):
    o.append(_arr(x1, y1, x2, y2, tag, 1.0))
    if both:
        o.append(_arr(x2, y2 + 9, x1, y1 + 9, tag, 1.0))
    mid = ((x1 + x2) / 2.0, (y1 + y2) / 2.0)
    o.append(_lbl(mid[0], mid[1] - 6 if both else mid[1] - 4, "GPIB", "txs", "middle"))


def _gnd(x, y):
    """Three-bar earth symbol hanging from (x, y)."""
    return "".join([_line(x - 11, y, x + 11, y, 1.2),
                    _line(x - 7, y + 4, x + 7, y + 4, 1.1),
                    _line(x - 3.5, y + 8, x + 3.5, y + 8, 1.0)])


def _rack(tag, mode="photo"):
    """Instrument rack shared by figures 94.7, 94.9 and 94.10.

    mode = "photo"  photometer only, no HV, no PMT      (Fig. 94.7)
           "pmt"    PMT on an HV supply, 1 kΩ load      (Fig. 94.9)
           "mono"   PMT + monochrometer in front of it  (Fig. 94.10)

    Routing is kept strictly orthogonal with a dedicated channel per net, so
    no wire crosses another and nothing runs through a box.
    """
    o = []
    pmt = mode in ("pmt", "mono")

    # ---------------------------------------------------------- the DUT
    # A five-layer stack drawn edge-on, light leaving to the left.
    o.append(_lbl(428, 34, "DUT", "tb", "middle"))
    for by, bh in ((44, 8), (58, 8), (72, 10), (86, 8), (100, 8)):
        o.append(_rect(400, by, 56, bh, 1.1, "#ffffff"))

    # ------------------------------------------------------ light path
    dx = 192 if mode == "pmt" else 302          # right edge of last detector
    o.append(_rect(dx, 65, 8, 18, 1.1, "#ffffff"))   # input window
    o.append(_arr(398, 74, dx, 74, tag, 1.4))
    o.append(_lbl((398 + dx) / 2.0, 65, "LIGHT", "tb", "middle"))

    # --------------------------------------------------- detector chain
    if mode == "photo":
        o.append(_blk(206, 50, 96, 48, ["PHOTOMETER"], "tm"))
    else:
        o.append(_blk(46, 50, 74, 48, ["HV", "POWER", "SUPPLY"], "txs"))
        o.append(_blk(136, 52, 56, 44, ["PMT"], "tm"))
        o.append(_line(120, 74, 136, 74, 1.1))
        if mode == "mono":
            o.append(_blk(206, 44, 96, 60, ["MONOCHROMETER"], "txs"))
            o.append(_line(192, 74, 206, 74, 1.1))

    # ------------------------------------- PMT anode: 1 kΩ load to earth
    if pmt:
        o.append(_line(164, 96, 164, 140, 1.1))
        o.append(_rect(156, 140, 16, 26, 1.1, "#ffffff"))
        o.append(_lbl(176, 152, "1 kΩ", "txs"))
        o.append(_line(164, 166, 164, 172, 1.1))
        o.append(_gnd(164, 172))
        # the light signal is taken off across that load into the scope
        o.append(_dot(164, 124, 2.0))
        o.append(_path([(164, 124), (230, 124), (230, 178)], 1.1))

    # ------------------------------------------- drive side: Al electrode
    # Al (top bar) -> round the outside -> amplifier output.
    o.append(_path([(456, 48), (620, 48), (620, 122), (604, 122)], 1.1))
    o.append(_tri(556, 98, 48, 48, tag))
    o.append(_lbl(573, 116, "AMP", "txs", "middle"))

    # ------------------------------- sense side: transparent bottom bar
    o.append(_path([(400, 104), (378, 104), (378, 140)], 1.1))
    o.append(_rect(370, 140, 16, 26, 1.1, "#ffffff"))
    o.append(_line(378, 166, 378, 172, 1.1))
    o.append(_gnd(378, 172))
    o.append(_lbl(394, 146, "SENSE", "txs"))
    o.append(_lbl(394, 156, "RESISTOR", "txs"))

    # ----------------------------------------------------- instruments
    o.append(_blk(196, 178, 132, 56, ["OSCILLOSCOPE"], "txs"))
    o.append(_blk(196, 296, 132, 52,
                  ["ARBITRARY", "WAVEFORM", "GENERATOR"], "txs"))
    o.append(_blk(56, 178, 96, 62, ["COMPUTER"], "txs"))

    # ------------------------------------------------- scope channels
    # I(t): tapped above the sense resistor, own channel at x = 352.
    o.append(_path([(378, 130), (352, 130), (352, 224), (328, 224)], 1.1))
    o.append(_lbl(356, 126, "I(t)", "txs"))
    # V(t): tapped on the Al run, own channel at x = 500.
    o.append(_path([(500, 48), (500, 208), (328, 208)], 1.1))
    o.append(_lbl(400, 204, "V(t)", "txs"))

    # --------------------------------------------- AWG -> amplifier in
    o.append(_path([(328, 322), (540, 322), (540, 122), (556, 122)], 1.1))

    # ------------------------------------------------ GPIB connections
    _gpib(o, 152, 196, 196, 196, tag)                 # computer <-> scope
    o.append(_path([(120, 240), (120, 322), (196, 322)], 1.1))   # -> AWG
    o.append(_arr(150, 322, 194, 322, tag, 1.0))
    o.append(_lbl(150, 314, "GPIB", "txs", "middle"))

    if mode != "pmt":                                  # -> photometer/mono
        target = 98 if mode == "photo" else 104
        o.append(_path([(88, 178), (88, 112), (214, 112), (214, target + 24)], 1.1))
        o.append(_arr(214, target + 24, 214, target, tag, 1.0))
        o.append(_lbl(132, 107, "GPIB", "txs", "middle"))

    return o


def fig_94_7():
    tag = "947"
    o = [_defs(tag)]
    o += _rack(tag, "photo")
    return _fig(svg(660, 372, "".join(o),
                    "Hệ đo độ chói và hiệu suất của linh kiện"),
                "Hình 94.7 · Sơ đồ hệ thống đo độ chói và hiệu suất như các hàm của điện áp "
                "đỉnh điều khiển. Dạng sóng điện áp V(t) được đo bằng dao động ký tại điện "
                "cực Al của linh kiện cần đo. Dạng sóng dòng I(t) được dao động ký đo bằng "
                "điện áp trên điện trở cảm biến chia cho trị số của nó. Độ chói được đo "
                "bằng quang kế.",
                "FIGURE 94.7 · Schematic diagram of a system for measuring luminance and "
                "efficiency as functions of the peak drive voltage. The voltage waveform, "
                "V(t), is measured by the oscilloscope at the Al electrode of the device "
                "under test. The current waveform, I(t), is measured by the oscilloscope as "
                "the voltage across the sense resistor divided by its resistance. The "
                "luminance is measured by the photometer.",
                "Sơ đồ khối hệ đo: máy tính nối qua bus GPIB tới dao động ký và bộ tạo dạng "
                "sóng tuỳ ý; bộ tạo dạng sóng qua bộ khuếch đại tới linh kiện cần đo; ánh "
                "sáng từ linh kiện tới quang kế; điện áp và dòng của linh kiện được lấy qua "
                "điện trở cảm biến đưa về dao động ký",
                "Measurement block diagram: a computer linked over GPIB to an oscilloscope "
                "and an arbitrary waveform generator; the generator drives the device under "
                "test through an amplifier; light from the device reaches the photometer; "
                "the device voltage and current are tapped across a sense resistor back to "
                "the oscilloscope")


def fig_94_8():
    tag = "948"
    b = Box(560, 340, (160, 260), (0, 250), pad=(72, 26, 78, 56))
    o = [_defs(tag)]
    o.append(b.axes("Điện áp (V)", "Độ chói (cd/m²)",
                    xt=[(160, "160"), (180, "180"), (200, "200"), (220, "220"),
                        (240, "240"), (260, "260")],
                    yt=[(0, "0"), (50, "50"), (100, "100"), (150, "150"),
                        (200, "200"), (250, "250")]))
    # right-hand efficiency scale
    o.append(_line(b.l + b.pw, b.t, b.l + b.pw, b.t + b.ph, 1.2))
    for v in (0, 2, 4, 6, 8):
        y = b.t + b.ph - (v / 8.0) * b.ph
        o.append(_line(b.l + b.pw, y, b.l + b.pw + 4, y, 1.1))
        o.append(_lbl(b.l + b.pw + 7, y + 3.4, str(v), "ts"))
    o.append(_vlab(b.l + b.pw + 46, b.t + b.ph / 2.0, "Hiệu suất (lm/W)", "ts"))

    lum = [(170, 2), (180, 6), (186, 14), (192, 34), (198, 74), (204, 112),
           (210, 140), (218, 164), (228, 184), (240, 198), (250, 206), (260, 208)]
    o.append(b.curve(lum, "c1"))

    def ey(v):
        return b.t + b.ph - (v / 8.0) * b.ph

    eff = [(170, 0.2), (180, 0.7), (186, 2.2), (192, 5.0), (197, 7.0),
           (200, 7.6), (204, 7.0), (210, 5.2), (220, 3.4), (232, 2.4),
           (245, 1.9), (260, 1.6)]
    d = "M" + " L".join("%s %s" % (_f(b.x(x)), _f(ey(v))) for x, v in eff)
    o.append('<path d="%s" fill="none" stroke="%s" stroke-width="2" '
             'stroke-dasharray="7 5"/>' % (d, GOLD))
    return _fig(svg(560, 340, "".join(o),
                    "Độ chói và hiệu suất theo điện áp đỉnh"),
                "Hình 94.8 · Đồ thị độ chói và hiệu suất như các hàm của điện áp đỉnh điều "
                "khiển. Đường liền là độ chói và đường đứt là hiệu suất.",
                "FIGURE 94.8 · Plots of luminance and efficiency as functions of peak drive "
                "voltage. The solid line is the luminance and the dashed line is the "
                "efficiency.",
                "Đồ thị hai trục tung theo điện áp từ 160 đến 260 vôn. Đường liền là độ "
                "chói, tăng theo dạng chữ S từ gần không tới hơn 200 candela trên mét "
                "vuông. Đường đứt là hiệu suất, dựng nhanh tới đỉnh khoảng 7,6 lumen trên "
                "oát quanh 200 vôn rồi giảm dần",
                "Dual-axis plot against voltage from 160 to 260 volts. The solid line is "
                "luminance, rising in an S-shape from near zero to just over 200 candelas "
                "per square metre. The dashed line is efficiency, climbing steeply to a "
                "peak of about 7.6 lumens per watt near 200 volts and then falling away")


def fig_94_9():
    tag = "949"
    o = [_defs(tag)]
    o += _rack(tag, "pmt")
    return _fig(svg(660, 372, "".join(o),
                    "Hệ đo thời gian tắt phát quang"),
                "Hình 94.9 · Thiết bị đo thời gian tắt phát quang của chất phát quang "
                "ACTFEL. Tín hiệu ánh sáng được dao động ký đo trên điện trở cảm biến ở "
                "đầu ra của ống nhân quang. Dao động ký được kích hoạt theo xung điều khiển.",
                "FIGURE 94.9 · Apparatus for measuring the luminescent decay time of the "
                "ACTFEL phosphor. The light signal is measured by the oscilloscope across "
                "the sense resistor on the output of the PMT. The oscilloscope is triggered "
                "on the drive pulse.",
                "Sơ đồ khối như hình 94.7 nhưng thay quang kế bằng ống nhân quang có nguồn "
                "cao áp riêng; đầu ra ống nhân quang qua điện trở một kilôôm về dao động "
                "ký, còn linh kiện cần đo vẫn được nuôi qua bộ khuếch đại từ bộ tạo dạng "
                "sóng",
                "The same block diagram as figure 94.7 but with a photomultiplier tube on "
                "its own high-voltage supply replacing the photometer; the tube output goes "
                "through a one-kilohm resistor to the oscilloscope, while the device under "
                "test is still driven through an amplifier by the waveform generator")


def fig_94_10():
    tag = "9410"
    o = [_defs(tag)]
    o += _rack(tag, "mono")
    return _fig(svg(660, 372, "".join(o),
                    "Hệ đo phổ phát xạ phân giải thời gian"),
                "Hình 94.10 · Hệ đo phổ phát xạ phân giải thời gian của một linh kiện "
                "ACTFEL. Dao động ký được đặt ở chế độ tích phân tín hiệu ánh sáng từ ống "
                "nhân quang trong một cửa sổ thời gian đã chọn. Bước sóng của máy đơn sắc "
                "được quét trên toàn dải phổ và dữ liệu cường độ phát xạ được thu từ dao "
                "động ký.",
                "FIGURE 94.10 · System for measuring the time-resolved emission spectrum of "
                "an ACTFEL device. The oscilloscope is set to integrate the light signal "
                "from the PMT during a selected time window. The monochrometer wavelength "
                "is scanned over the entire spectral range and the emission intensity data "
                "is collected from the oscilloscope.",
                "Sơ đồ khối như hình 94.9 nhưng có thêm máy đơn sắc đặt giữa linh kiện cần "
                "đo và ống nhân quang; ánh sáng đi qua máy đơn sắc trước khi tới ống nhân "
                "quang, dao động ký tích phân tín hiệu trong một cửa sổ thời gian chọn "
                "trước",
                "The same block diagram as figure 94.9 with a monochrometer inserted "
                "between the device under test and the photomultiplier tube; light passes "
                "through the monochrometer before reaching the tube, and the oscilloscope "
                "integrates the signal over a chosen time window")


# ---------------------------------------------------------------- dispatch
_FIGS = {
    1: fig_94_1, 2: fig_94_2, 3: fig_94_3, 4: fig_94_4, 5: fig_94_5,
    6: fig_94_6, 7: fig_94_7, 8: fig_94_8, 9: fig_94_9, 10: fig_94_10,
}


def fig(n):
    return _FIGS[n]()
