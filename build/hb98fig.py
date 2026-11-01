# -*- coding: utf-8 -*-
"""Figures for Handbook Chapter 98 — Optimal Control (Halit Eren, Curtin
University of Technology).

Six figures (98.1–98.6). 98.1–98.3 are plots redrawn from the source curves;
98.4–98.6 are block diagrams redrawn block for block.

NOTE: never emit <sub>/<sup> inside <svg> text — both are on the HTML parser's
breakout list and eject the parser from SVG foreign content. Subscripts use
<tspan dy=...> via _rich().
"""
import math

from hbfig import _f, svg, _fig

E = "#2a2a2a"
S = "#888888"
GRID = "#e4e4e4"
GOLD = "#b45309"
BLUE = "#1d4ed8"


def _lbl(x, y, txt, cls="t", anchor="start"):
    return ('<text class="%s" x="%s" y="%s" text-anchor="%s">%s</text>'
            % (cls, _f(x), _f(y), anchor, txt))


def _rich(x, y, parts, anchor="start", cls="t"):
    s, prev = "", False
    for txt, is_sub in parts:
        if is_sub:
            s += '<tspan font-size="7" dy="2.4">%s</tspan>' % txt
        elif prev:
            s += '<tspan dy="-2.4">%s</tspan>' % txt
        else:
            s += txt
        prev = is_sub
    return ('<text class="%s" x="%s" y="%s" text-anchor="%s">%s</text>'
            % (cls, _f(x), _f(y), anchor, s))


def _defs(tag):
    return ('<defs>'
            '<marker id="a%s" markerWidth="9" markerHeight="9" refX="7" refY="3" '
            'orient="auto"><path d="M0,0 L7,3 L0,6 z" fill="%s"/></marker>'
            '<marker id="s%s" markerWidth="9" markerHeight="9" refX="7" refY="3" '
            'orient="auto"><path d="M0,0 L7,3 L0,6 z" fill="%s"/></marker>'
            '<style>.tl{font:9.5px Inter,Helvetica,sans-serif;fill:#555}'
            '.tm{font:9px Inter,Helvetica,sans-serif;fill:#333}'
            '.tf{font:9.5px Inter,Helvetica,sans-serif;fill:#555;font-style:italic}'
            '.tb{font:10px Inter,Helvetica,sans-serif;fill:#111;font-weight:700}'
            '</style></defs>' % (tag, E, tag, S))


def _line(x1, y1, x2, y2, sw=1.4, col=E, dash=""):
    d = ' stroke-dasharray="%s"' % dash if dash else ""
    return ('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="%s"%s/>'
            % (_f(x1), _f(y1), _f(x2), _f(y2), col, sw, d))


def _arr(x1, y1, x2, y2, tag="98", sw=1.3, col=E):
    return ('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="%s" '
            'marker-end="url(#a%s)"/>'
            % (_f(x1), _f(y1), _f(x2), _f(y2), col, sw, tag))


def _rect(x, y, w, h, sw=1.3, fill="#fff", dash="", rx=0):
    d = ' stroke-dasharray="%s"' % dash if dash else ""
    r = ' rx="%s"' % _f(rx) if rx else ""
    return ('<rect x="%s" y="%s" width="%s" height="%s"%s fill="%s" stroke="%s" '
            'stroke-width="%s"%s/>'
            % (_f(x), _f(y), _f(w), _f(h), r, fill, E, sw, d))


def _blk(x, y, w, h, parts, dash=""):
    o = [_rect(x, y, w, h, 1.3, "#fff", dash)]
    n = len(parts)
    for i, ln in enumerate(parts):
        cy = y + h / 2.0 + (i - (n - 1) / 2.0) * 13 + 3.6
        if isinstance(ln, list):
            o.append(_rich(x + w / 2.0, cy, ln, "middle", "tm"))
        else:
            o.append(_lbl(x + w / 2.0, cy, ln, "tm", "middle"))
    return "".join(o)


def _sum(cx, cy, r=10, signs=None, tag="98"):
    o = ['<circle cx="%s" cy="%s" r="%s" fill="#fff" stroke="%s" stroke-width="1.3"/>'
         % (_f(cx), _f(cy), _f(r), E)]
    if signs:
        pos = {"l": (cx - r - 10, cy - 5), "r": (cx + r + 3, cy - 5),
               "t": (cx - 2.5, cy - r - 5), "b": (cx - 9, cy + r + 12)}
        for k, s in signs.items():
            x, y = pos[k]
            o.append(_lbl(x, y, s, "tm"))
    return "".join(o)


def _path(pts, col=E, sw=1.8, dash=""):
    d = ' stroke-dasharray="%s"' % dash if dash else ""
    return ('<path d="M" fill="none" stroke="%s" stroke-width="%s"%s/>'
            % (col, sw, d)) if not pts else \
        ('<polyline points="%s" fill="none" stroke="%s" stroke-width="%s"%s/>'
         % (" ".join("%s,%s" % (_f(a), _f(b)) for a, b in pts), col, sw, d))


def _smooth(pts, col=E, sw=1.8):
    """Catmull-Rom-ish smooth curve through pts."""
    d = "M%s %s" % (_f(pts[0][0]), _f(pts[0][1]))
    for i in range(len(pts) - 1):
        x0, y0 = pts[i]
        x1, y1 = pts[i + 1]
        cx = (x0 + x1) / 2.0
        d += " C%s %s, %s %s, %s %s" % (_f(cx), _f(y0), _f(cx), _f(y1), _f(x1), _f(y1))
    return '<path d="%s" fill="none" stroke="%s" stroke-width="%s"/>' % (d, col, sw)


# ---------------------------------------------------------------- 98.1
def fig_98_1():
    o = [_defs("98")]
    ax = 90
    x0, x1 = 118, 636
    u_lo, u_hi = 0.02, 0.96
    ybase = 196                       # J = 0 / u axis
    ytop = 78
    yzero = 268                       # zero line of dJ/du

    u1, u2, u3 = 0.26, 0.46, 0.72

    def dJ(u):
        # cubic with roots at the three stationary points: + - + -
        return -(u - u1) * (u - u2) * (u - u3)

    def J(u):
        # J is the integral of dJ/du, evaluated from u_lo
        s, n = 0.0, 400
        du = (u - u_lo) / n
        for i in range(n):
            s += dJ(u_lo + (i + 0.5) * du) * du
        return s

    def X(u):
        return x0 + (u - u_lo) / (u_hi - u_lo) * (x1 - x0)

    us = [u_lo + (u_hi - u_lo) * i / 240.0 for i in range(241)]
    Js = [J(u) for u in us]
    jmin, jmax = min(Js), max(Js)

    def YJ(v):
        return ybase - (v - jmin) / (jmax - jmin) * (ybase - ytop)

    dmax = max(abs(dJ(u)) for u in us)

    def YD(v):
        return yzero - v / dmax * 44.0

    # axes
    o.append(_arr(ax, ybase, ax, ytop - 14))
    o.append(_lbl(ax - 6, ytop - 20, "J", "tm", "end"))
    o.append(_line(ax, ybase, x1 + 26, ybase, 1.4))
    o.append(_arr(x1 + 26, ybase, x1 + 54, ybase))
    o.append(_lbl(x1 + 58, ybase + 4, "u", "tm"))

    # derivative zero line
    o.append(_line(x0, yzero, x1, yzero, 0.9, GRID))
    o.append(_lbl(x0 - 6, yzero + 4, "0", "tm", "end"))
    o.append(_lbl(x1 + 6, yzero + 4, "dJ/du", "tm", "start"))

    # curves
    o.append(_path([(X(u), YJ(v)) for u, v in zip(us, Js)], E, 1.9))
    o.append(_path([(X(u), YD(dJ(u))) for u in us], GOLD, 1.5))

    # stationary points
    for u, lab in ((u1, "u1"), (u2, "u2"), (u3, "u3")):
        o.append(_line(X(u), YJ(J(u)), X(u), yzero, 0.9, S, "4 3"))
        o.append(_lbl(X(u), ybase + 16, lab, "tm", "middle"))
        o.append('<circle cx="%s" cy="%s" r="2.6" fill="%s"/>' % (_f(X(u)), _f(YJ(J(u))), E))
        o.append('<circle cx="%s" cy="%s" r="2.4" fill="%s"/>' % (_f(X(u)), _f(yzero), GOLD))

    o.append(_lbl(X(u1), YJ(J(u1)) - 10, "c\u1ef1c \u0111\u1ea1i \u0111\u1ecba ph\u01b0\u01a1ng", "tm", "middle"))
    o.append(_lbl(X(u2), YJ(J(u2)) + 18, "c\u1ef1c ti\u1ec3u \u0111\u1ecba ph\u01b0\u01a1ng", "tm", "middle"))
    o.append(_lbl(X(u3), YJ(J(u3)) - 10, "c\u1ef1c \u0111\u1ea1i to\u00e0n c\u1ee5c", "tm", "middle"))
    return _fig(svg(700, 330, "".join(o),
                    "K\u1ef9 thu\u1eadt leo d\u1ed1c: \u0111\u01b0\u1eddng cong J(u) c\u00f3 c\u1ef1c \u0111\u1ea1i \u0111\u1ecba ph\u01b0\u01a1ng, c\u1ef1c ti\u1ec3u \u0111\u1ecba ph\u01b0\u01a1ng "
                    "v\u00e0 c\u1ef1c \u0111\u1ea1i to\u00e0n c\u1ee5c, c\u00f9ng \u0111\u01b0\u1eddng \u0111\u1ea1o h\u00e0m dJ/du c\u1eaft tr\u1ee5c t\u1ea1i u1, u2, u3"),
                "H\u00ecnh 98.1 \u00b7 K\u1ef9 thu\u1eadt leo d\u1ed1c minh ho\u1ea1 trong v\u00f9ng c\u00f3 c\u1ef1c \u0111\u1ea1i to\u00e0n c\u1ee5c. D\u1ea5u c\u1ee7a \u0111\u1ea1o h\u00e0m "
                "b\u1eadc m\u1ed9t \u0111\u1ed5i d\u1ea5u khi \u0111\u1ea1o h\u00e0m \u0111i qua \u0111i\u1ec3m c\u1ef1c \u0111\u1ea1i; h\u00ecnh c\u0169ng ch\u1ec9 ra c\u00e1c c\u1ef1c \u0111\u1ea1i v\u00e0 c\u1ef1c "
                "ti\u1ec3u \u0111\u1ecba ph\u01b0\u01a1ng c\u1ea7n \u0111\u1ec1 ph\u00f2ng khi thi\u1ebft k\u1ebf \u0111i\u1ec1u khi\u1ec3n t\u1ed1i \u01b0u.",
                "Figure 98.1 \u00b7 The hill-climbing technique illustrated in the region of the absolute "
                "maximum. The sign of the first derivative changes as it passes through the maximum "
                "point; the local maxima and minima that optimal-control design must guard against "
                "are also shown.",
                "\u0110\u1ed3 th\u1ecb h\u00e0m m\u1ee5c ti\u00eau c\u00f3 nhi\u1ec1u c\u1ef1c tr\u1ecb v\u00e0 \u0111\u01b0\u1eddng \u0111\u1ea1o h\u00e0m b\u00ean d\u01b0\u1edbi",
                "Objective function with several extrema and its derivative below")


# ---------------------------------------------------------------- 98.2
def _contour(cx, cy, r, wob, n=40):
    """Closed irregular contour around (cx, cy)."""
    pts = []
    for i in range(n + 1):
        a = 2 * math.pi * i / n
        rr = r * (1 + wob * math.sin(3 * a + 0.7) + wob * 0.5 * math.sin(5 * a))
        pts.append((cx + rr * math.cos(a), cy + rr * 0.72 * math.sin(a)))
    return " ".join("%s,%s" % (_f(a), _f(b)) for a, b in pts)


def fig_98_2():
    o = [_defs("98")]

    def panel(ox, kind):
        g = []
        cx, cy = ox + 150, 128
        for i, r in enumerate((100, 78, 56, 36, 20)):
            g.append('<polygon points="%s" fill="none" stroke="%s" stroke-width="1.1"/>'
                     % (_contour(cx, cy, r, 0.11 - i * 0.014), E))
        g.append('<circle cx="%s" cy="%s" r="2.6" fill="%s"/>' % (_f(cx), _f(cy), E))
        if kind == "grad":
            # climbs up and to the left, sT0 -> sT5
            path = [(cx + 66, cy + 78), (cx + 22, cy + 62), (cx - 34, cy + 46),
                    (cx - 46, cy + 16), (cx - 28, cy - 8), (cx - 4, cy - 12)]
            lab = ["sT0", "sT1", "sT2", "sT3", "sT4", "sT5"]
            side = ["r", "r", "r", "l", "l", "r"]
        else:
            # wanders up from the lower left, sT0 -> sT7
            path = [(cx - 70, cy + 80), (cx - 12, cy + 64), (cx + 34, cy + 56),
                    (cx + 6, cy + 28), (cx + 2, cy - 2), (cx - 26, cy - 10),
                    (cx + 44, cy - 6), (cx + 66, cy + 12)]
            lab = ["sT0", "sT1", "sT2", "sT3", "sT4", "sT5", "sT6", "sT7"]
            side = ["r", "r", "r", "l", "r", "l", "r", "r"]
        for i, (px, py) in enumerate(path):
            g.append('<ellipse cx="%s" cy="%s" rx="5.2" ry="7" fill="%s"/>'
                     % (_f(px), _f(py), E))
            if side[i] == "r":
                g.append(_lbl(px + 8, py + 3.2, lab[i], "tm", "start"))
            else:
                g.append(_lbl(px - 8, py + 3.2, lab[i], "tm", "end"))
        return "".join(g)

    o.append(panel(30, "grad"))
    o.append(panel(390, "rand"))
    # direction-of-motion arrows: up-left in (a), up-right in (b)
    o.append(_arr(96, 262, 62, 226))
    o.append(_lbl(34, 280, "chiều chuyển động", "tm", "start"))
    o.append(_arr(600, 262, 634, 226))
    o.append(_lbl(617, 280, "chiều chuyển động", "tm", "middle"))
    o.append(_lbl(180, 306, "(a)", "tb", "middle"))
    o.append(_lbl(540, 306, "(b)", "tb", "middle"))
    return _fig(svg(760, 330, "".join(o),
                    "Hai ví dụ về phương pháp leo dốc: (a) theo gradient, (b) bước ngẫu nhiên"),
                "Hình 98.2 · Hai ví dụ của phương pháp leo dốc: (a) theo gradient, (b) bước ngẫu nhiên. "
                "Cả hai đều xuất phát từ một điểm ước lượng ban đầu, tại đó đạo hàm bậc một được đoán "
                "bằng không, rồi đi theo hướng dốc nhất lên hoặc xuống cho tới khi tìm được cực trị "
                "toàn cục.",
                "Figure 98.2 · Two examples of hill climbing: (a) gradient, (b) random walk. Both start "
                "from an initial estimate where the first derivative is guessed to be zero, then step "
                "in the direction of steepest ascent or descent until the absolute maximum or minimum "
                "is found.",
                "Hai bản đồ đường đồng mức với đường đi leo dốc",
                "Two contour maps with hill-climbing paths")


# ---------------------------------------------------------------- 98.3
def fig_98_3():
    o = [_defs("98")]
    ax, ay, w, h = 100, 60, 420, 220
    y0 = ay + h / 2.0          # error = 0
    ymax, ymin = ay, ay + h    # +1 / -1

    o.append(_arr(ax, ymin, ax, ay - 14))
    o.append(_arr(ax, y0, ax + w + 50, y0))
    o.append(_lbl(ax + w + 54, y0 + 4, "Thời gian", "tm"))
    o.append(_lbl(ax - 8, ay + 4, "+1", "tm", "end"))
    o.append(_lbl(ax - 8, y0 + 4, "0", "tm", "end"))
    o.append(_lbl(ax - 8, ymin + 4, "−1", "tm", "end"))
    o.append(_lbl(ax - 8, ay - 18, "Sai số", "tm", "end"))

    T = 8.0

    def X(t):
        return ax + t / T * w

    def Y(v):
        return y0 - v * (h / 2.0)

    # error: damped oscillation
    pts = []
    for i in range(0, 241):
        t = T * i / 240.0
        e = math.exp(-0.55 * t) * math.cos(2.6 * t)
        pts.append((X(t), Y(max(-1, min(1, e)))))
    o.append(_path(pts, E, 1.7))

    # integrals, scaled to the same box
    ia, isq, ita = 0.0, 0.0, 0.0
    pa, ps, pt = [], [], []
    dt = T / 240.0
    for i in range(0, 241):
        t = T * i / 240.0
        e = math.exp(-0.55 * t) * math.cos(2.6 * t)
        ia += abs(e) * dt
        isq += e * e * dt
        ita += t * abs(e) * dt
        pa.append((X(t), Y(min(1, ia / 0.95))))
        ps.append((X(t), Y(min(1, isq / 1.30))))
        pt.append((X(t), Y(min(1, ita / 2.55))))
    o.append(_path(pa, GOLD, 1.6))
    o.append(_path(ps, BLUE, 1.6))
    o.append(_path(pt, "#0f766e", 1.6))

    # labels above each curve's final value, nudged apart so they never collide
    ends = sorted([(Y(min(1.0, ita / 2.55)) - 9, "ITAE"),
                   (Y(min(1.0, ia / 0.95)) - 9, "IAE"),
                   (Y(min(1.0, isq / 1.30)) - 9, "ISE")])
    for i in range(1, len(ends)):
        if ends[i][0] - ends[i - 1][0] < 14:
            ends[i] = (ends[i - 1][0] + 14, ends[i][1])
    for yy, name in ends:
        o.append(_lbl(X(T) - 6, yy, name, "tm", "end"))
    o.append(_lbl(X(2.6), Y(-0.62), "sai số", "tm", "middle"))
    return _fig(svg(640, 340, "".join(o),
                    "Mô tả sai số giữa đáp ứng thực và đáp ứng mong muốn, cùng các chỉ tiêu IAE, ISE, ITAE"),
                "Hình 98.3 · Mô tả sai số giữa đáp ứng thực và đáp ứng mong muốn. Trong những bài toán "
                "điều khiển tối ưu đơn giản, sai số giữa đáp ứng mong muốn và đáp ứng thực được chọn "
                "làm chỉ tiêu chất lượng; mục tiêu là giữ sai số càng nhỏ càng tốt.",
                "Figure 98.3 · Errors between the actual and the desired response. In simple optimal "
                "control problems the error between desired and actual response is taken as the "
                "performance index, the aim being to keep the error as small as possible.",
                "Đồ thị sai số theo thời gian kèm ba đường tích phân IAE, ISE, ITAE",
                "Error versus time with the IAE, ISE and ITAE integrals")


# ---------------------------------------------------------------- 98.4
def fig_98_4():
    o = [_defs("98")]
    y = 96
    o.append(_lbl(16, y + 4, "x(k) = 0", "tb"))
    o.append(_arr(88, y, 116, y))
    o.append(_sum(128, y, 11, {"l": "+", "b": "−"}))
    o.append(_arr(139, y, 178, y))
    o.append(_lbl(146, y - 10, "u(k)", "tb"))
    o.append(_blk(178, y - 28, 300, 56, ["x(k+1) = Ax(k) + Bu(k)"]))
    o.append(_arr(478, y, 566, y))
    o.append(_lbl(506, y - 10, "x(k)", "tb"))
    o.append(_arr(566, y, 616, y))
    # feedback
    o.append(_line(560, y, 560, y + 66, 1.3))
    o.append(_line(560, y + 66, 128, y + 66, 1.3))
    o.append(_line(128, y + 66, 128, y + 11, 1.3))
    o.append(_blk(300, y + 50, 96, 32, ["K(k)"]))
    return _fig(svg(660, 210, "".join(o),
                    "Sơ đồ điều khiển tối ưu theo chỉ tiêu chất lượng bậc hai: vòng phản hồi trạng thái "
                    "qua hệ số khuếch đại K(k)"),
                "Hình 98.4 · Sơ đồ điều khiển tối ưu dựa trên chỉ tiêu chất lượng bậc hai. Luật điều "
                "khiển đòi hỏi phản hồi vectơ trạng thái với hệ số khuếch đại K(k) biến thiên theo "
                "thời gian; K(k) được tính trước khi quá trình bắt đầu để dùng về sau.",
                "Figure 98.4 · Optimal control scheme based on the quadratic performance index. The "
                "control law requires state feedback with a time-varying gain K(k), computed before "
                "the process begins.",
                "Sơ đồ khối điều khiển tối ưu có phản hồi trạng thái",
                "Optimal control block diagram with state feedback")


# ---------------------------------------------------------------- 98.5
def fig_98_5():
    o = [_defs("98")]
    y = 150
    # precomputation box, centred over -K(k)
    o.append(_blk(77, 34, 150, 46, ["Tính trước", "K(k)"]))
    o.append(_arr(152, 80, 152, y - 26))
    # forward chain
    o.append(_lbl(40, y - 8, "x(k)", "tb"))
    o.append(_arr(40, y, 114, y))
    o.append(_blk(114, y - 26, 76, 52, ["−K(k)"]))
    o.append(_arr(190, y, 220, y))
    o.append(_lbl(194, y - 11, "u(k)", "tb"))
    o.append(_blk(220, y - 26, 54, 52, ["B"]))
    o.append(_arr(274, y, 310, y))
    o.append(_sum(324, y, 11, {"l": "+", "b": "+"}))
    o.append(_arr(335, y, 374, y))
    o.append(_blk(374, y - 26, 84, 52, ["z⁻¹I"]))
    o.append(_arr(458, y, 614, y))
    o.append(_lbl(476, y - 11, "x(k)", "tb"))
    # A loop: tap -> left into A -> out of A -> up into the junction
    o.append(_line(526, y, 526, y + 96, 1.3))
    o.append(_arr(526, y + 96, 452, y + 96))
    o.append(_blk(390, y + 80, 62, 32, ["A"]))
    o.append(_line(390, y + 96, 324, y + 96, 1.3))
    o.append(_arr(324, y + 96, 324, y + 12))
    # outer rail: the state x(k) is distributed back to the input of -K(k)
    o.append(_line(594, y, 594, y + 158, 1.3))
    o.append(_line(594, y + 158, 76, y + 158, 1.3))
    o.append(_line(76, y + 158, 76, y, 1.3))
    return _fig(svg(640, 350, "".join(o),
                    "Thiết kế đặt cực cho hàm truyền vòng kín: khối tính trước K(k), khâu khuếch đại "
                    "trạng thái và khâu trễ z⁻¹I"),
                "Hình 98.5 · Thiết kế đặt cực cho hàm truyền vòng kín. Phương pháp này giả thiết các "
                "biến trạng thái đo được và sẵn sàng cho phản hồi.",
                "Figure 98.5 · Pole-placement design of the closed-loop transfer function. The method "
                "assumes the state variables are measurable and available for feedback.",
                "Sơ đồ khối đặt cực với khối tính trước hệ số khuếch đại",
                "Pole-placement block diagram with gain precomputation")


# ---------------------------------------------------------------- 98.6
def fig_98_6():
    o = [_defs("98")]
    y = 104
    o.append(_lbl(18, y + 4, "r(k)", "tb"))
    o.append(_arr(58, y, 84, y))
    o.append(_sum(96, y, 11, {"l": "+", "b": "+"}))
    o.append(_arr(107, y, 138, y))
    o.append(_lbl(112, y - 11, "u(k)", "tb"))
    # plant
    o.append(_blk(138, y - 34, 250, 68, ["Đối tượng", "x(k+1) = Ax(k) + Bu(k)"]))
    o.append(_arr(388, y, 420, y))
    # measurement
    o.append(_blk(420, y - 34, 220, 68, ["Đo lường", "y(k) = Cx(k)"]))
    o.append(_arr(640, y, 700, y))
    # feedback: y -> observer -> K -> summing junction
    o.append(_line(596, y + 34, 596, y + 112, 1.3))
    o.append(_arr(596, y + 112, 470, y + 112))
    o.append(_blk(370, y + 96, 100, 32, ["Bộ quan sát"]))
    o.append(_arr(370, y + 112, 300, y + 112))
    o.append(_blk(200, y + 96, 100, 32, ["K"]))
    o.append(_line(200, y + 112, 96, y + 112, 1.3))
    o.append(_arr(96, y + 112, 96, y + 12))
    o.append(_lbl(250, y + 74, "Khuếch đại", "tm", "middle"))
    o.append(_lbl(250, y + 86, "phản hồi trạng thái", "tm", "middle"))
    return _fig(svg(730, 250, "".join(o),
                    "Sử dụng bộ quan sát trạng thái: đầu ra đo được đưa qua bộ quan sát rồi qua khâu "
                    "khuếch đại phản hồi trạng thái về bộ cộng"),
                "Hình 98.6 · Sử dụng bộ quan sát trạng thái. Khi cần phản hồi từ các biến trạng thái, "
                "có thể quan sát trạng thái từ thông tin chứa trong đầu ra cũng như trong các biến đầu "
                "vào, dựa trên các số đo thu được.",
                "Figure 98.6 · Use of a state observer. When feedback from the state variables is "
                "required, the states may be observed from information contained in the output as well "
                "as in the input variables.",
                "Sơ đồ khối đối tượng, khâu đo, bộ quan sát và khuếch đại phản hồi",
                "Plant, measurement, observer and feedback-gain block diagram")


FIGS = [fig_98_1, fig_98_2, fig_98_3, fig_98_4, fig_98_5, fig_98_6]


def fig(n):
    return FIGS[n - 1]()
