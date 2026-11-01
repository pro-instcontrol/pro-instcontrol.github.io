# -*- coding: utf-8 -*-
"""Figures for Handbook Chapter 100 — Explosion-Proof Instruments
(Sam S. Khalilieh, P.E., Earth Tech).

The source chapter contains seven figures (100.1–100.7); 100.6 and 100.7 are
photographs in the print, redrawn here as line pictograms from their captions.

NOTE: never emit <sub>/<sup> inside <svg> text. Both tags are on the HTML
"breakout" list, so the parser pops out of SVG foreign content at the first
one and every following element renders as loose HTML. Subscripts here use
<tspan dy=...> instead.
"""
import math

from hbfig import _f, svg, _fig

E = "#2a2a2a"
S = "#888888"
GRID = "#e4e4e4"


def _lbl(x, y, txt, cls="t", anchor="start"):
    return ('<text class="%s" x="%s" y="%s" text-anchor="%s">%s</text>'
            % (cls, _f(x), _f(y), anchor, txt))


def _rich(x, y, parts, anchor="start", cls="t"):
    """Text with real subscripts: parts is [(txt, is_subscript), ...]."""
    s, prev = "", False
    for txt, is_sub in parts:
        if is_sub:
            s += '<tspan font-size="7.5" dy="2.5">%s</tspan>' % txt
        elif prev:
            s += '<tspan dy="-2.5">%s</tspan>' % txt
        else:
            s += txt
        prev = is_sub
    return ('<text class="%s" x="%s" y="%s" text-anchor="%s">%s</text>'
            % (cls, _f(x), _f(y), anchor, s))


def _defs(tag, hatch=False):
    h = ""
    if hatch:
        h = ('<pattern id="h%s" width="7" height="7" patternUnits="userSpaceOnUse" '
             'patternTransform="rotate(45)"><line x1="0" y1="0" x2="0" y2="7" '
             'stroke="#cdc3a8" stroke-width="1.3"/></pattern>' % tag)
    return ('<defs>'
            '<marker id="a%s" markerWidth="9" markerHeight="9" refX="7" refY="3" '
            'orient="auto"><path d="M0,0 L7,3 L0,6 z" fill="%s"/></marker>%s'
            '<style>.tl{font:9.5px Inter,Helvetica,sans-serif;fill:#666}'
            '.tf{font:10px Inter,Helvetica,sans-serif;fill:#555;font-style:italic}'
            '</style></defs>' % (tag, E, h))


def _line(x1, y1, x2, y2, sw=1.4, col=E, dash=""):
    d = ' stroke-dasharray="%s"' % dash if dash else ""
    return ('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="%s"%s/>'
            % (_f(x1), _f(y1), _f(x2), _f(y2), col, sw, d))


def _arr(x1, y1, x2, y2, tag="100", sw=1.4, col=E):
    return ('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="%s" '
            'marker-end="url(#a%s)"/>'
            % (_f(x1), _f(y1), _f(x2), _f(y2), col, sw, tag))


def _rect(x, y, w, h, sw=1.4, fill="#fff", dash="", rx=0):
    d = ' stroke-dasharray="%s"' % dash if dash else ""
    r = ' rx="%s"' % _f(rx) if rx else ""
    return ('<rect x="%s" y="%s" width="%s" height="%s"%s fill="%s" stroke="%s" '
            'stroke-width="%s"%s/>'
            % (_f(x), _f(y), _f(w), _f(h), r, fill, E, sw, d))


def _box(x, y, w, h, lines, fs=None):
    o = [_rect(x, y, w, h)]
    n = len(lines)
    for i, ln in enumerate(lines):
        cy = y + h / 2.0 + (i - (n - 1) / 2.0) * 15 + 4
        o.append(_lbl(x + w / 2.0, cy, ln, "t", "middle"))
    return "".join(o)


def _res_h(x, y, w=60):
    """Horizontal resistor centred on (x, y), spanning w."""
    o = [_line(x, y, x + 4, y, 1.4)]
    pts, n = [], 6
    for i in range(n + 1):
        pts.append((x + 4 + (w - 8) * i / float(n), y + (-7 if i % 2 else 7)))
    d = "M" + " L".join("%s %s" % (_f(a), _f(b)) for a, b in pts)
    o.append('<path d="%s" fill="none" stroke="%s" stroke-width="1.4"/>' % (d, E))
    o.append(_line(x + w - 4, y, x + w, y, 1.4))
    return "".join(o)


def _fuse_h(x, y, w=60):
    return (_line(x, y, x + w, y, 1.4)
            + _rect(x + 6, y - 7, w - 12, 14, 1.2))


def _zener_v(cx, ytop, ybot):
    """Vertical Zener, anode at the top, cathode bar (with wings) at the bottom."""
    hw = 9
    ty = ybot - 16
    # the lead stops at the triangle: it must not be drawn through the symbol
    o = [_line(cx, ytop, cx, ty, 1.4)]
    o.append('<path d="M%s %s L%s %s L%s %s z" fill="#fff" stroke="%s" '
             'stroke-width="1.3"/>'
             % (_f(cx - hw), _f(ty), _f(cx + hw), _f(ty), _f(cx), _f(ybot), E))
    o.append(_line(cx - hw - 2, ybot, cx + hw + 2, ybot, 1.7))
    o.append(_line(cx - hw - 2, ybot, cx - hw - 6, ybot + 5, 1.7))
    o.append(_line(cx + hw + 2, ybot, cx + hw + 6, ybot - 5, 1.7))
    return "".join(o)


def _gnd(cx, ytop):
    o = [_line(cx, ytop, cx, ytop + 8, 1.4)]
    for i, ww in enumerate((22, 14, 7)):
        o.append(_line(cx - ww / 2.0, ytop + 8 + i * 5, cx + ww / 2.0,
                       ytop + 8 + i * 5, 1.4))
    return "".join(o)


# ---------------------------------------------------------------- 100.1
def fig_100_1():
    o = [_defs("100")]
    Y = 186
    o.append(_line(164, 70, 164, 300, 1.2, S, "5 4"))
    o.append(_lbl(40, 46, "Khu vực nguy hiểm", "ts"))
    o.append(_lbl(188, 46, "Khu vực không nguy hiểm", "ts"))
    # field device
    o.append(_box(36, 152, 104, 68, ["Thiết bị", "trường"]))
    # barrier enclosure
    o.append(_rect(180, 118, 420, 178, 1.2))
    o.append(_lbl(390, 108, "Rào an toàn", "ts", "middle"))
    # signal path
    o.append(_line(140, Y, 208, Y, 1.4))
    o.append(_res_h(208, Y, 60))
    o.append(_line(268, Y, 312, Y, 1.4))
    o.append(_line(312, Y, 392, Y, 1.4))
    o.append(_line(392, Y, 440, Y, 1.4))
    o.append(_fuse_h(440, Y, 60))
    o.append(_line(500, Y, 600, Y, 1.4))
    o.append(_arr(600, Y, 618, Y))
    o.append(_lbl(628, 181, "Điện áp vào", "ts"))
    o.append(_lbl(628, 195, "đến 250 V", "ts"))
    # zener pair
    o.append(_zener_v(312, Y, 230))
    o.append(_line(312, 230, 312, 248, 1.4))
    o.append(_zener_v(392, Y, 230))
    o.append(_line(392, 230, 392, 248, 1.4))
    o.append(_line(312, 248, 392, 248, 1.4))
    o.append(_line(352, 248, 352, 266, 1.4))
    o.append(_gnd(352, 266))
    o.append(_lbl(374, 282, "(R < 1 Ω)", "ts"))
    # component labels
    o.append(_lbl(238, 158, "Điện trở", "ts", "middle"))
    o.append(_lbl(238, 170, "hạn chế dòng", "ts", "middle"))
    o.append(_lbl(470, 166, "Cầu chì", "ts", "middle"))
    o.append(_lbl(296, 216, "Điốt Zener 1", "ts", "end"))
    o.append(_lbl(408, 216, "Điốt Zener 2", "ts"))
    return _fig(svg(780, 330, "".join(o),
                    "Sơ đồ rào an toàn Zener: điện trở hạn chế dòng, cầu chì, hai điốt Zener và điểm nối đất"),
                "Hình 100.1 · Các thành phần chính của mạch rào an toàn: điện trở hạn chế dòng (I<sub>sc</sub>), "
                "cầu chì, và hai điốt Zener mắc song song để dự phòng, tất cả đấu về đất có điện trở nhỏ "
                "hơn 1 Ω.",
                "Figure 100.1 · Major components of the barrier circuit: the current-limiting resistor "
                "(I<sub>sc</sub>), the fuse, and two Zener diodes in parallel for redundancy, all "
                "returned to a ground of less than 1 Ω.",
                "Sơ đồ mạch rào an toàn gồm thiết bị trường, điện trở, hai điốt Zener, cầu chì và điểm nối đất",
                "Zener safety barrier: field device, resistor, two Zener diodes, fuse and ground")


# ---------------------------------------------------------------- 100.2
def _panel(ax, ay, w, h, xr, yr, xlab, ylab, xt, yt, curves, legend, title):
    """Log-log ignition-curve panel. xr/yr are (log10 min, log10 max)."""
    o = []

    def X(v):
        return ax + (math.log10(v) - xr[0]) * w / (xr[1] - xr[0])

    def Y(v):
        return ay + h - (math.log10(v) - yr[0]) * h / (yr[1] - yr[0])

    for i in range(int(math.ceil(xr[0])), int(xr[1]) + 1):
        o.append(_line(X(10 ** i), ay, X(10 ** i), ay + h, 0.7, GRID))
    for i in range(int(math.ceil(yr[0])), int(yr[1]) + 1):
        o.append(_line(ax, Y(10 ** i), ax + w, Y(10 ** i), 0.7, GRID))

    for fn in curves:
        seg, segs = [], []
        for i in range(0, 241):
            lg = xr[0] + (xr[1] - xr[0]) * i / 240.0
            v = fn(10 ** lg)
            if not v or v <= 0:
                continue
            ly = math.log10(v)
            if yr[0] <= ly <= yr[1]:
                seg.append((X(10 ** lg), Y(v)))
            elif seg:
                segs.append(seg)
                seg = []
        if seg:
            segs.append(seg)
        for sg in segs:
            if len(sg) > 1:
                d = "M" + " L".join("%s %s" % (_f(a), _f(b)) for a, b in sg)
                o.append('<path d="%s" fill="none" stroke="%s" stroke-width="1.5"/>'
                         % (d, E))

    o.append(_line(ax, ay + h, ax + w, ay + h, 1.3))
    o.append(_line(ax, ay, ax, ay + h, 1.3))

    for v, lab in xt:
        x = X(v)
        o.append(_line(x, ay + h, x, ay + h + 4, 1.2))
        o.append(_lbl(x, ay + h + 16, lab, "tl", "middle"))
    for v, lab in yt:
        y = Y(v)
        o.append(_line(ax - 4, y, ax, y, 1.2))
        o.append(_lbl(ax - 7, y + 3.5, lab, "tl", "end"))

    o.append(_rich(ax + w / 2.0, ay + h + 36, xlab, "middle", "ts")
             if isinstance(xlab, list)
             else _lbl(ax + w / 2.0, ay + h + 36, xlab, "ts", "middle"))
    o.append('<text class="ts" x="%s" y="%s" text-anchor="middle" '
             'transform="rotate(-90 %s %s)">%s</text>'
             % (_f(ax - 78), _f(ay + h / 2.0), _f(ax - 78), _f(ay + h / 2.0), ylab))
    o.append(_lbl(ax + w / 2.0, ay + h + 58, title, "tb", "middle"))
    for i, s in enumerate(legend):
        o.append(_lbl(ax + w - 6, ay + 16 + i * 13, s, "tl", "end"))
    return "".join(o)


def fig_100_2():
    o = [_defs("100")]

    # ---- (a) ignition current vs source voltage
    def ia(v, i20, n):
        return i20 * (v / 20.0) ** (-n) * (1.0 + (11.0 / v) ** 3)

    curves_a = [lambda v: ia(v, 0.70, 1.22),
                lambda v: ia(v, 0.42, 1.26),
                lambda v: ia(v, 0.30, 1.30),
                lambda v: ia(v, 0.24, 1.34)]
    o.append(_panel(110, 64, 250, 200, (1, 2.4), (-2, 0.301),
                    "điện áp nguồn (V)", "dòng mồi",
                    [(10, "10"), (20, "20"), (50, "50"), (100, "100"), (200, "200")],
                    [(0.01, "10 mA"), (0.05, "50 mA"), (0.1, "100 mA"),
                     (0.5, "500 mA"), (1, "1 A"), (2, "2 A")],
                    curves_a,
                    ["Mêtan", "Nhóm D, F, G", "Nhóm C, E", "Nhóm A, B"],
                    "(a) mạch điện trở"))

    # ---- (b) inductance vs short-circuit current
    def ib(i, l10, n):
        return l10 * (i / 0.1) ** (-n) * (1.0 + (0.012 / i) ** 2)

    curves_b = [lambda i: ib(i, 0.090, 1.45),
                lambda i: ib(i, 0.045, 1.42),
                lambda i: ib(i, 0.026, 1.40),
                lambda i: ib(i, 0.012, 1.38)]
    o.append(_panel(540, 64, 250, 200, (-2, 0), (-4, 0),
                    [("dòng ngắn mạch I", False), ("sc", True)], "điện cảm L",
                    [(0.01, "10 mA"), (0.02, "20 mA"), (0.05, "50 mA"),
                     (0.1, "100 mA"), (0.2, "200 mA"), (0.5, "500 mA"), (1, "1 A")],
                    [(1e-4, "100 µH"), (1e-3, "1 mH"), (1e-2, "10 mH"),
                     (1e-1, "100 mH"), (1, "1 H")],
                    curves_b,
                    ["Mêtan", "Nhóm D, F, G", "Nhóm C, E", "Nhóm A, B"],
                    "(b) mạch điện cảm, 24 V"))

    # ---- (c) capacitance vs open-circuit voltage
    def ic(v, c30, n):
        return c30 * (v / 30.0) ** (-n) * (1.0 + (14.0 / v) ** 2)

    curves_c = [lambda v: ic(v, 3.0, 1.55),
                lambda v: ic(v, 1.6, 1.55),
                lambda v: ic(v, 0.85, 1.55),
                lambda v: ic(v, 0.42, 1.55)]
    o.append(_panel(110, 356, 250, 200, (0, 3.5), (-5, 1),
                    [("điện áp hở mạch V", False), ("oc", True)], "điện dung C",
                    [(1, "1 V"), (3, "3 V"), (10, "10 V"), (30, "30 V"),
                     (100, "100 V"), (300, "300 V"), (1000, "1000 V")],
                    [(1e-5, "0,01 µF"), (1e-4, "0,1 µF"), (1e-3, "1 µF"),
                     (1e-2, "10 µF"), (1e-1, "100 µF"), (1, "1000 µF"),
                     (1e1, "10.000 µF")],
                    curves_c,
                    ["C + 400 Ω", "C + 150 Ω", "C + 5,4 Ω", "C + 0 Ω"],
                    "(c) mạch điện dung, nhóm A và B"))

    o.append(_lbl(470, 392, "Đường cong mồi: vùng nằm dưới đường", "tf"))
    o.append(_lbl(470, 406, "cong là an toàn — không đủ năng lượng", "tf"))
    o.append(_lbl(470, 420, "để mồi hỗn hợp khí thuộc nhóm tương", "tf"))
    o.append(_lbl(470, 434, "ứng. Mỗi nhóm bốn đường cong, xếp", "tf"))
    o.append(_lbl(470, 448, "từ trên xuống theo thứ tự chú giải.", "tf"))

    return _fig(svg(860, 640, "".join(o),
                    "Ba đồ thị đường cong mồi theo điện trở, điện cảm và điện dung cho các nhóm khí"),
                "Hình 100.2 · (a) Đường cong mồi của mạch điện trở cho mọi kim loại làm mạch. (b) Đường "
                "cong mồi của mạch điện cảm ở 24 V cho mọi kim loại làm mạch. (c) Đường cong mồi của "
                "mạch điện dung cho nhóm A và B với mọi kim loại làm mạch.",
                "Figure 100.2 · (a) Resistance circuit ignition curves for all circuit metals. (b) "
                "Inductance circuit ignition curves at 24 V for all circuit metals. (c) Capacitance "
                "circuit ignition curves for groups A and B for all circuit metals.",
                "Ba đồ thị log-log của đường cong mồi: dòng theo điện áp, điện cảm theo dòng ngắn mạch, "
                "điện dung theo điện áp hở mạch",
                "Three log-log ignition-curve charts: current vs voltage, inductance vs short-circuit "
                "current, capacitance vs open-circuit voltage")


# ---------------------------------------------------------------- 100.3
def fig_100_3():
    o = [_defs("100")]
    o.append(_lbl(40, 36, "Khu vực nguy hiểm", "ts"))
    o.append(_lbl(400, 36, "Khu vực không nguy hiểm", "ts"))
    o.append(_line(300, 44, 300, 130, 1.2, S, "5 4"))
    o.append(_box(40, 60, 130, 64, ["Thiết bị an toàn", "nội"]))
    o.append(_box(420, 60, 140, 64, ["Thiết bị liên hợp", "an toàn nội"]))
    o.append(_line(170, 78, 420, 78, 1.4))
    o.append(_line(170, 106, 420, 106, 1.4))
    o.append(_lbl(295, 144, "Dây dẫn hiện trường", "ts", "middle"))

    # three parameter columns
    o.append(_lbl(105, 182, "Tham số thiết bị trường", "tb", "middle"))
    o.append(_lbl(295, 182, "Tham số dây dẫn", "tb", "middle"))
    o.append(_lbl(490, 182, "Tham số thiết bị liên hợp", "tb", "middle"))
    o.append(_line(30, 188, 180, 188, 0.9, S))
    o.append(_line(232, 188, 358, 188, 0.9, S))
    o.append(_line(404, 188, 576, 188, 0.9, S))

    left = [("V", "min", " = 12 V"), ("V", "max", " = 30 V"),
            ("I", "max", " = 0,5 A"), ("C", "i", " = 0,3 µF"),
            ("L", "i", " = 2,0 mH")]
    mid = [("C", "", " = 150 pF/m"), ("L", "", " = 2,0 µH/m"),
           ("R", "", " = 48 Ω/km")]
    right = [("V", "oc", " = 24 V"), ("I", "sc", " = 0,3 A"),
             ("C", "a", " = 0,45 µF"), ("L", "a", " = 3,5 mH"),
             ("L/R", "", " = 60 µH/Ω")]
    for i, (base, sub, tail) in enumerate(left):
        parts = [(base, False)] + ([(sub, True)] if sub else []) + [(tail, False)]
        o.append(_rich(40, 208 + i * 18, parts))
    for i, (base, sub, tail) in enumerate(mid):
        parts = [(base, False)] + ([(sub, True)] if sub else []) + [(tail, False)]
        o.append(_rich(232, 208 + i * 18, parts))
    for i, (base, sub, tail) in enumerate(right):
        parts = [(base, False)] + ([(sub, True)] if sub else []) + [(tail, False)]
        o.append(_rich(418, 208 + i * 18, parts))

    return _fig(svg(720, 300, "".join(o),
                    "Sơ đồ phân tích hệ an toàn nội: thiết bị trường, dây dẫn và thiết bị liên hợp với "
                    "các tham số tương ứng"),
                "Hình 100.3 · Phân tích một hệ an toàn nội. Cột bên trái là tham số của thiết bị trường, "
                "cột giữa là tham số của dây dẫn hiện trường, cột bên phải là tham số của thiết bị liên "
                "hợp (rào an toàn).",
                "Figure 100.3 · Analysis of an intrinsically safe system. The left column holds the field "
                "device parameters, the middle the field wiring parameters, and the right the associated "
                "apparatus (barrier) parameters.",
                "Sơ đồ hai khối thiết bị nối bằng dây dẫn hiện trường, phía dưới là ba cột tham số",
                "Two blocks joined by field wiring, with three columns of parameters beneath")


# ---------------------------------------------------------------- 100.4 / 100.5
def _approval(tag, loop, extra=None):
    o = []
    o.append(_lbl(26, 34, "Khu vực nguy hiểm", "ts"))
    o.append(_lbl(360, 34, "Khu vực không nguy hiểm", "ts"))
    if loop:
        o.append('<rect x="18" y="50" width="486" height="122" fill="url(#h%s)" '
                 'stroke="%s" stroke-width="1.1" stroke-dasharray="4 3"/>' % (tag, S))
    o.append(_box(34, 74, 112, 62, ["Thiết bị an toàn nội"]))
    o.append(_box(252, 74, 112, 62, ["Thiết bị liên hợp", "an toàn nội"]))
    o.append(_line(200, 62, 200, 152, 5.5))
    o.append(_arr(148, 92, 250, 92, tag))
    o.append(_arr(250, 118, 148, 118, tag))
    o.append(_lbl(200, 190, "Cùng loại dây dẫn", "ts", "middle"))
    if extra:
        o.append(extra)
    return "".join(o)


def fig_100_4():
    o = [_defs("100", hatch=True), _approval("100", True)]
    o.append(_lbl(26, 214, "Vùng gạch: thiết bị trường và rào được đánh giá cùng nhau", "ts"))
    return _fig(svg(620, 238, "".join(o),
                    "Sơ đồ phê duyệt theo vòng: thiết bị an toàn nội và thiết bị liên hợp được đánh giá "
                    "cùng nhau trong một vùng gạch"),
                "Hình 100.4 · Phê duyệt theo vòng (loop approval). Thiết bị an toàn nội và thiết bị liên "
                "hợp được đánh giá cùng nhau; vùng gạch chỉ phạm vi đã được đánh giá.",
                "Figure 100.4 · Loop approval. The intrinsically safe apparatus and the associated "
                "apparatus are evaluated together; the shaded area marks what has been evaluated.",
                "Hai khối thiết bị được bao trong một vùng gạch, nối với nhau qua vách ngăn",
                "Two blocks inside a hatched region, joined across the boundary")


def fig_100_5():
    o = [_defs("100")]
    o.append(_approval("100", False))
    o.append(_box(492, 74, 128, 62, ["Phòng điều khiển"]))
    o.append(_line(364, 105, 492, 105, 1.4))
    return _fig(svg(700, 212, "".join(o),
                    "Sơ đồ phê duyệt theo thực thể: thiết bị an toàn nội và thiết bị liên hợp được đánh "
                    "giá riêng, sau đó ghép với phòng điều khiển"),
                "Hình 100.5 · Phê duyệt theo thực thể (entity approval). Thiết bị an toàn nội và thiết bị "
                "liên hợp được đánh giá riêng rồi ghép lại theo các tham số thực thể ở Bảng 100.3.",
                "Figure 100.5 · Entity approval. The intrinsically safe apparatus and the associated "
                "apparatus are evaluated separately and then matched by the entity parameters of "
                "Table 100.3.",
                "Hai khối thiết bị đánh giá riêng, nối qua vách ngăn, thêm khối phòng điều khiển",
                "Two separately evaluated blocks across the boundary, plus a control room block")


# ---------------------------------------------------------------- 100.6 / 100.7
def fig_100_6():
    o = [_defs("100")]
    # conduits, each running up to the body
    o.append(_rect(40, 84, 106, 28, 1.3))
    o.append(_rect(314, 84, 106, 28, 1.3))
    # threads where the conduit screws into the body
    for x0 in (128, 314):
        for k in range(4):
            o.append(_line(x0 + k * 4.5, 84, x0 + k * 4.5, 112, 1.0, S))
    # cast body
    o.append(_rect(146, 64, 168, 68, 1.6, "#fff", rx=5))
    # plug on top
    o.append(_rect(210, 34, 34, 30, 1.3))
    for k in range(3):
        o.append(_line(210, 40 + k * 7, 244, 40 + k * 7, 1.0, S))
    o.append(_lbl(83, 78, "Ống dẫn", "ts", "middle"))
    o.append(_lbl(367, 78, "Ống dẫn", "ts", "middle"))
    o.append(_lbl(252, 52, "Nút bịt", "ts"))
    o.append(_lbl(230, 156, "Thân đúc", "ts", "middle"))
    # leader from the right-hand thread run down to its label
    o.append(_line(322, 116, 336, 146, 0.9, S))
    o.append(_lbl(340, 158, "Mối nối ren", "ts"))
    return _fig(svg(520, 200, "".join(o),
                    "Hình vẽ dạng nét của một khớp bịt chống nổ: thân đúc, hai đầu ren nối ống và nút bịt"),
                "Hình 100.6 · Khớp bịt chống nổ (seal-off fitting). Bản gốc là ảnh chụp của Crouse-Hinds "
                "(Cooper Industries); ở đây được vẽ lại bằng nét để đọc rõ trên màn hình nhỏ.",
                "Figure 100.6 · Explosion-proof seal-off fitting. The original is a photograph courtesy "
                "of Crouse-Hinds Division of Cooper Industries; it is redrawn here as a line pictogram "
                "so that it stays legible on a small screen.",
                "Hình nét của khớp bịt chống nổ với thân đúc, hai đầu ren và nút bịt phía trên",
                "Line drawing of a seal-off fitting: cast body, two threaded ends and a top plug")


def fig_100_7():
    o = [_defs("100")]
    o.append(_rect(56, 42, 244, 162, 1.7))
    o.append(_rect(68, 54, 220, 138, 1.1, "#fafafa"))
    for col in (0, 1):
        for row in range(5):
            x = 88 + col * 100
            y = 70 + row * 23
            o.append(_rect(x, y, 36, 13, 1.0))
            o.append(_line(x + 18, y + 13, x + 18, y + 23, 1.2))
    o.append(_lbl(178, 32, "Vỏ đúc", "ts", "middle"))
    # callouts on the right
    o.append(_line(300, 62, 344, 76, 0.9, S))
    o.append(_lbl(348, 72, "Cửa có bản lề", "ts"))
    o.append(_lbl(348, 86, "và ốc khoá", "ts"))
    o.append(_line(288, 138, 344, 132, 0.9, S))
    o.append(_lbl(348, 128, "Mặt bích dày,", "ts"))
    o.append(_lbl(348, 142, "khe hở hẹp", "ts"))
    o.append(_line(300, 190, 344, 190, 0.9, S))
    o.append(_lbl(348, 186, "Cầu dao", "ts"))
    o.append(_lbl(348, 200, "aptomat", "ts"))
    return _fig(svg(560, 224, "".join(o),
                    "Hình vẽ dạng nét của một bảng điện chiếu sáng vỏ chống nổ có các aptomat bên trong"),
                "Hình 100.7 · Bảng điện chiếu sáng vỏ chống nổ. Bản gốc là ảnh chụp của Crouse-Hinds "
                "(Cooper Industries); ở đây được vẽ lại bằng nét.",
                "Figure 100.7 · Explosion-proof lighting panelboard. The original is a photograph "
                "courtesy of Crouse-Hinds Division of Cooper Industries; it is redrawn here as a line "
                "pictogram.",
                "Hình nét của bảng điện chống nổ với vỏ đúc dày và các aptomat bên trong",
                "Line drawing of an explosion-proof panelboard: thick cast enclosure with breakers inside")


FIGS = [fig_100_1, fig_100_2, fig_100_3, fig_100_4, fig_100_5, fig_100_6, fig_100_7]


def fig(n):
    return FIGS[n - 1]()
