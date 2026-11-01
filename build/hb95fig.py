# -*- coding: utf-8 -*-
"""Figures for Handbook Chapter 95 — Light-Emitting Diode Displays
(Mohammad A. Karim, University of Tennessee, Knoxville).

Eight figures, 95.1–95.8.

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
            '</style></defs>' % (tag, E, tag, E))


def _line(x1, y1, x2, y2, sw=1.2, col=E, dash=""):
    d = ' stroke-dasharray="%s"' % dash if dash else ""
    return ('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="%s"%s/>'
            % (_f(x1), _f(y1), _f(x2), _f(y2), col, sw, d))


def _arr(x1, y1, x2, y2, tag="951", sw=1.15, col=E, head="a"):
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


def _squig(x1, y1, x2, y2, tag="951", amp=3.0, n=3, col=E):
    """Wavy photon arrow from (x1,y1) to (x2,y2)."""
    dx, dy = x2 - x1, y2 - y1
    L = math.hypot(dx, dy) or 1.0
    ux, uy = dx / L, dy / L
    px, py = -uy, ux
    pts, steps = [], 26
    for i in range(steps + 1):
        t = i / float(steps)
        s = math.sin(t * n * 2 * math.pi) * amp * (1 - t * 0.35)
        pts.append((x1 + ux * L * t + px * s, y1 + uy * L * t + py * s))
    d = "M" + " L".join("%s %s" % (_f(a), _f(b)) for a, b in pts)
    return ('<path d="%s" fill="none" stroke="%s" stroke-width="1.3"/>'
            '<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="1.3" '
            'marker-end="url(#a%s)"/>'
            % (d, col, _f(pts[-2][0]), _f(pts[-2][1]), _f(x2), _f(y2), col, tag))


def _slab(x, y, w, h, dx, dy, fill="#fff"):
    """Cabinet-projection slab: front rect + top parallelogram + right face."""
    o = [_poly([(x, y), (x + w, y), (x + w, y + h), (x, y + h)], 1.2, fill),
         _poly([(x, y), (x + dx, y - dy), (x + w + dx, y - dy), (x + w, y)], 1.2, fill),
         _poly([(x + w, y), (x + w + dx, y - dy),
                (x + w + dx, y - dy + h), (x + w, y + h)], 1.2, fill)]
    return "".join(o)


# ---------------------------------------------------------------- 95.1
def _band(cx, cy, a, half, up=True):
    """Sampled parabola in screen coords; up=True gives a ∪ (band minimum)."""
    pts = []
    for i in range(41):
        u = -1 + 2 * i / 40.0
        x = cx + u * half
        y = cy - a * u * u if up else cy + a * u * u
        pts.append((x, y))
    return pts


def fig_95_1():
    tag = "951"
    o = [_defs(tag)]

    # ---------------- panel (a) direct gap
    ax, ay = 180, 250
    o += [_line(52, ay, 312, ay, 1.2), _line(ax, 46, ax, ay, 1.2)]
    o.append(_arr(306, ay, 316, ay, tag, 1.0))
    o.append(_arr(ax, 52, ax, 44, tag, 1.0))
    o.append(_lbl(320, ay + 4, "k", "tf"))
    o.append(_lbl(ax + 4, 42, "E", "tf"))
    o.append(_path(_band(ax, 118, 44, 84, True), 1.7))
    o.append(_path(_band(ax, 182, 38, 84, False), 1.7))
    # E_g marker, offset left of the energy axis
    o.append(_arr(ax - 34, 180, ax - 34, 122, tag, 1.0, S, "h"))
    o.append(_arr(ax - 34, 122, ax - 34, 180, tag, 1.0, S, "h"))
    o.append(_rich(ax - 42, 156, [("E", False), ("g", True)], "end"))
    # photon, right of the axis
    o.append(_squig(ax + 40, 176, ax + 40, 126, tag, 2.8, 2))
    o.append(_rich(ax + 48, 154, [("h", False), ("ν", False)]))
    o.append(_lbl(ax - 84, ay + 16, "k = −π/l", "ts", "middle"))
    o.append(_lbl(ax + 60, ay + 16, "k = π/l", "ts", "middle"))
    o.append(_lbl(ax, ay + 36, "(a)", "ts", "middle"))

    # ---------------- panel (b) indirect gap
    bx = 400                      # energy axis
    o += [_line(bx, ay, 656, ay, 1.2), _line(bx, 46, bx, ay, 1.2)]
    o.append(_arr(650, ay, 660, ay, tag, 1.0))
    o.append(_arr(bx, 52, bx, 44, tag, 1.0))
    o.append(_lbl(664, ay + 4, "k", "tf"))
    o.append(_lbl(bx + 4, 42, "E", "tf"))
    # conduction: minimum displaced to k = pi/l
    cond = [(x, 118 - 34 * ((x - 530) / 130.0) ** 2) for x in range(bx, 651, 4)]
    o.append(_path(cond, 1.7))
    # valence: maximum at k = 0
    val = [(x, 178 + 34 * ((x - bx) / 260.0) ** 2) for x in range(bx, 651, 4)]
    o.append(_path(val, 1.7))
    # gap at the conduction minimum
    o.append(_line(530, 118, 530, 186, 1.0, S, "4 3"))
    o.append(_arr(530, 184, 530, 122, tag, 1.0, S, "h"))
    o.append(_arr(530, 122, 530, 184, tag, 1.0, S, "h"))
    o.append(_rich(538, 154, [("E", False), ("g", True)]))
    o.append(_squig(430, 182, 522, 126, tag, 2.4, 2))
    o.append(_rich(432, 200, [("h", False), ("ν", False)]))
    o.append(_lbl(bx + 130, ay + 36, "(b)", "ts", "middle"))

    return _fig(svg(700, 300, "".join(o),
                    "Giản đồ năng lượng E theo vectơ sóng k"),
                "Hình 95.1 · E theo k đối với chất bán dẫn có (a) vùng cấm trực tiếp và "
                "(b) vùng cấm gián tiếp.",
                "FIGURE 95.1 · E versus k for semiconductors having (a) a direct band gap "
                "and (b) an indirect band gap.",
                "Hai giản đồ năng lượng theo vectơ sóng. Phần (a) vùng cấm trực tiếp: cực "
                "tiểu vùng dẫn và cực đại vùng hoá trị cùng nằm trên trục năng lượng, mũi "
                "tên E g và mũi tên photon thẳng đứng. Phần (b) vùng cấm gián tiếp: cực "
                "tiểu vùng dẫn lệch sang phải, mũi tên photon xiên",
                "Two energy-versus-wavevector diagrams. Part (a) direct band gap: the "
                "conduction minimum and valence maximum coincide on the energy axis, with "
                "a vertical E-g arrow and a vertical photon arrow. Part (b) indirect band "
                "gap: the conduction minimum is displaced to the right and the photon "
                "arrow is slanted")


# ---------------------------------------------------------------- 95.2
def _lum(lam, peak, s_lo, s_hi):
    s = s_lo if lam < peak else s_hi
    return math.exp(-((lam - peak) / s) ** 2)


def fig_95_2():
    tag = "952"
    b = Box(620, 300, (390, 710), (0, 1.08), pad=(72, 26, 26, 52))
    o = [_defs(tag)]
    o.append(b.axes("Bước sóng (nm)", "Hệ số hiệu quả sáng (tương đối)",
                    xt=[(400, "400"), (500, "500"), (600, "600"), (700, "700")],
                    yt=[(0, "0"), (0.2, "0.2"), (0.4, "0.4"),
                        (0.6, "0.6"), (0.8, "0.8"), (1.0, "1.0")]))
    o.append(_line(b.x(555), b.y(0), b.x(555), b.y(1.0), 0.8, S, "3 3"))
    o.append(_line(b.x(507), b.y(0), b.x(507), b.y(1.0), 0.8, S, "3 3"))
    pho = [(l, _lum(l, 555, 48, 62)) for l in range(390, 711, 3)]
    sco = [(l, _lum(l, 507, 40, 50)) for l in range(390, 711, 3)]
    o.append(b.curve(sco, "c3"))
    o.append(b.curve(pho, "c1"))
    o.append(_rich(b.x(560), b.y(1.045), [("V", False), ("λ", True)]))
    o.append(_rich(b.x(495), b.y(0.50), [("V'", False), ("λ", True)], "end"))
    return _fig(svg(620, 300, "".join(o),
                    "Đường cong hiệu quả sáng theo bước sóng"),
                "Hình 95.2 · Đường cong hiệu quả sáng phổ. Đường cong thị giác sáng "
                "V<sub>λ</sub> ứng với trường hợp thích nghi ban ngày, còn đường cong thị "
                "giác tối V′<sub>λ</sub> ứng với trường hợp thích nghi ban đêm.",
                "FIGURE 95.2 · Spectral luminous efficiency curves. The photopic curve "
                "V<sub>λ</sub> corresponds to the daylight-adapted case while the scotopic "
                "curve V′<sub>λ</sub> corresponds to the night-adapted case.",
                "Hai đường cong chuông trên trục bước sóng 400 đến 700 nanomét, có vạch "
                "đứt tại 507 và 555 nanomét. Đường thị giác sáng đỉnh tại 555 nm, đường "
                "thị giác tối đỉnh tại 507 nm và lệch về phía sóng ngắn",
                "Two bell curves on a 400-to-700-nanometre wavelength axis, with dashed "
                "markers at 507 and 555 nanometres. The photopic curve peaks at 555 nm and "
                "the scotopic curve peaks at 507 nm, shifted towards shorter wavelengths")


# ---------------------------------------------------------------- 95.3
def fig_95_3():
    tag = "953"
    b = Box(560, 340, (0, 1.0), (1.2, 3.0), pad=(86, 26, 30, 56))
    o = [_defs(tag)]
    o.append(b.axes("Phân số mol x", "Năng lượng vùng cấm E (eV)",
                    xt=[(0, "0"), (0.2, "0.2"), (0.4, "0.4"), (0.6, "0.6"),
                        (0.8, "0.8"), (1.0, "1.0")],
                    yt=[(1.5, "1.5"), (2.0, "2.0"), (2.5, "2.5"), (3.0, "3.0")]))
    o.append(b.curve([(0, 1.424), (0.45, 1.977), (1.0, 2.78)], "c1"))
    o.append(b.curve([(0, 1.75), (1.0, 2.261)], "c2"))
    o.append(_line(b.x(0.45), b.y(1.977), b.x(0.45), b.y(1.2), 0.9, S, "4 3"))
    o.append(_line(b.x(0), b.y(1.977), b.x(0.45), b.y(1.977), 0.9, S, "4 3"))
    o.append(b.dot(0.45, 1.977, 2.6))
    o.append(_line(b.x(0.462), b.y(2.02), b.x(0.472), b.y(2.30), 0.9, S, "3 3"))
    o.append(_lbl(b.x(0.478), b.y(2.44), "x = 0.45", "ts"))
    o.append(_rich(b.x(0.478), b.y(2.32), [("E", False), ("g", True),
                                           (" = 1.977", False)], "start", "ts"))
    o.append(_rich(b.x(0.03), b.y(1.37), [("E", False), ("g", True),
                                          (" = 1.424", False)]))
    o.append(_rich(b.x(0.72), b.y(1.95), [("E", False), ("g", True),
                                          (" = 2.261", False)]))
    o.append(_arr(b.x(0.86), b.y(1.99), b.x(0.965), b.y(2.235), tag, 0.9, S, "h"))
    o.append(_lbl(b.x(0.06), b.y(1.245), "GaAs", "ts"))
    o.append(_lbl(b.x(0.94), b.y(1.245), "GaP", "ts", "end"))
    o.append(_lbl(b.x(0.44), b.y(2.88), "T = 300 K", "ts"))
    o.append(_rich(b.x(0.44), b.y(2.77),
                   [("GaAs", False), ("1−x", True), ("P", False), ("x", True)]))
    return _fig(svg(560, 340, "".join(o),
                    "Năng lượng vùng cấm theo phân số mol x"),
                "Hình 95.3 · Năng lượng vùng cấm theo x trong GaAs<sub>1−x</sub>P<sub>x</sub>. "
                "(Từ Casey, H.J., Jr. và Parish, M.B., Eds., <i>Heterostructure Lasers</i>, "
                "Academic Press, New York, 1978. Được phép sử dụng.)",
                "FIGURE 95.3 · Band-gap energy versus x in GaAs<sub>1−x</sub>P<sub>x</sub>. "
                "(From Casey, H.J., Jr. and Parish, M.B., Eds., <i>Heterostructure Lasers</i>, "
                "Academic Press, New York, 1978. With permission.)",
                "Đồ thị năng lượng vùng cấm theo phân số mol x từ GaAs đến GaP. Đường vùng "
                "cấm trực tiếp dốc, đường vùng cấm gián tiếp thoải, hai đường cắt nhau tại "
                "x bằng 0,45 với năng lượng 1,977 electron-vôn",
                "Band-gap energy against mole fraction x from GaAs to GaP. The steep line "
                "is the direct gap and the shallow line the indirect gap; they cross at "
                "x = 0.45 and 1.977 electronvolts")


# ---------------------------------------------------------------- 95.4
def fig_95_4():
    tag = "954"
    o = [_defs(tag)]

    # ---- (a) quantum efficiency, log scale 0.001 .. 1.0
    ba = Box(360, 348, (0, 1.0), (-3.0, 0.0), pad=(78, 26, 14, 66))

    def lg(v):
        return math.log10(max(v, 1e-4))

    o.append(ba.axes("x, thành phần hợp kim", "Hiệu suất lượng tử (%)",
                     xt=[(0, "0"), (0.2, "0.2"), (0.4, "0.4"), (0.6, "0.6"),
                         (0.8, "0.8"), (1.0, "1.0")],
                     yt=[(lg(0.001), "0.001"), (lg(0.01), "0.01"),
                         (lg(0.1), "0.1"), (lg(1.0), "1.0")]))
    withN = [(0.0, 0.95), (0.15, 0.95), (0.30, 0.93), (0.42, 0.88), (0.48, 0.80),
             (0.55, 0.62), (0.65, 0.38), (0.75, 0.22), (0.85, 0.13), (1.0, 0.09)]
    noN = [(0.0, 0.90), (0.15, 0.90), (0.30, 0.88), (0.38, 0.70), (0.44, 0.30),
           (0.48, 0.075), (0.55, 0.018), (0.65, 0.008), (0.80, 0.005), (1.0, 0.004)]
    o.append(ba.curve([(x, lg(v)) for x, v in withN], "c1"))
    o.append(ba.curve([(x, lg(v)) for x, v in noN], "c2"))
    o.append(_line(ba.x(0.45), ba.t, ba.x(0.45), ba.t + ba.ph, 0.9, S, "4 3"))
    o.append(_lbl(ba.x(0.08), ba.y(lg(0.62)), "Direct", "ts"))
    o.append(_lbl(ba.x(0.58), ba.y(lg(0.62)), "Indirect", "ts"))
    o.append(_lbl(ba.x(0.50), ba.y(lg(0.16)), "With", "ts"))
    o.append(_lbl(ba.x(0.50), ba.y(lg(0.12)), "nitrogen", "ts"))
    o.append(_lbl(ba.x(0.05), ba.y(lg(0.028)), "Without", "ts"))
    o.append(_lbl(ba.x(0.05), ba.y(lg(0.021)), "nitrogen", "ts"))
    o.append(_lbl(ba.x(0.5), ba.h - 22, "(a)", "ts", "middle"))

    # ---- (b) peak emission wavelength
    bb = Box(320, 348, (0.3, 1.0), (548, 706), pad=(56, 26, 14, 66))
    q = ['<g transform="translate(370,0)">']
    q.append(bb.axes("x, thành phần hợp kim", "",
                     xt=[(0.4, "0.4"), (0.6, "0.6"), (0.8, "0.8"), (1.0, "1.0")],
                     yt=[(550, "550"), (600, "600"), (650, "650"), (700, "700")]))
    wN = [(0.30, 694), (0.38, 676), (0.46, 655), (0.54, 636), (0.62, 620),
          (0.72, 600), (0.82, 583), (0.92, 568), (1.0, 558)]
    woN = [(0.30, 641), (0.36, 628), (0.42, 616), (0.48, 606), (0.56, 598),
           (0.66, 590), (0.76, 578), (0.88, 566), (1.0, 557)]
    q.append(bb.curve(wN, "c1"))
    q.append(bb.curve(woN, "c2"))
    # legend, in the empty upper-right corner
    q.append(_line(bb.x(0.615), bb.y(692), bb.x(0.675), bb.y(692), 2.0, E))
    q.append(_lbl(bb.x(0.695), bb.y(688), "With nitrogen", "ts"))
    q.append(_line(bb.x(0.615), bb.y(674), bb.x(0.675), bb.y(674), 2.0, GOLD))
    q.append(_lbl(bb.x(0.695), bb.y(670), "Without nitrogen", "ts"))
    q.append(_lbl(bb.x(0.52), bb.t - 8, "300 K", "ts"))
    q.append(_lbl(bb.x(0.65), bb.h - 22, "(b)", "ts", "middle"))
    q.append("</g>")
    o += q
    o.append(_vlab(396, 170, "Bước sóng đỉnh phát xạ (nm)", "ts"))

    return _fig(svg(700, 348, "".join(o),
                    "Ảnh hưởng của pha tạp nitơ"),
                "Hình 95.4 · Ảnh hưởng của pha tạp nitơ trong GaAs<sub>1−x</sub>P<sub>x</sub>: "
                "(a) hiệu suất lượng tử theo x và (b) bước sóng đỉnh phát xạ theo x.",
                "FIGURE 95.4 · The effects of nitrogen doping in GaAs<sub>1−x</sub>P<sub>x</sub>: "
                "(a) quantum efficiency vs. x and (b) peak emission wavelength vs. x.",
                "Hai đồ thị cạnh nhau. Phần (a) hiệu suất lượng tử thang lôgarit theo x, "
                "đường có pha tạp nitơ nằm cao hơn và giảm chậm hơn, có vạch chia vùng "
                "trực tiếp và gián tiếp. Phần (b) bước sóng đỉnh từ 550 đến 700 nanomét "
                "theo x, đường có nitơ cho bước sóng dài hơn",
                "Two adjacent plots. Part (a): logarithmic quantum efficiency against x; "
                "the nitrogen-doped curve lies higher and falls more slowly, with the "
                "direct and indirect regions marked. Part (b): peak wavelength from 550 to "
                "700 nanometres against x, the nitrogen curve giving longer wavelengths")


# ---------------------------------------------------------------- 95.5
def fig_95_5():
    tag = "955"
    o = [_defs(tag)]

    # ---- (a) surface emitter
    o.append(_slab(46, 178, 118, 26, 32, 18))
    o.append(_slab(84, 146, 70, 22, 20, 12))
    o.append(_rect(104, 132, 26, 10, 1.1, "#e8e8e8"))
    o.append('<ellipse cx="117" cy="132" rx="13" ry="4" fill="none" stroke="%s" '
             'stroke-width="1.0"/>' % E)
    # emission cone rising from the window
    o.append(_line(112, 128, 72, 50, 1.2, E))
    o.append(_line(122, 128, 162, 50, 1.2, E))
    o.append('<ellipse cx="117" cy="50" rx="45" ry="13" fill="none" stroke="%s" '
             'stroke-width="1.1"/>' % E)
    o.append(_lbl(117, 240, "(a)", "ts", "middle"))

    # ---- (b) edge emitter
    o.append(_slab(300, 178, 132, 26, 32, 18))
    # active layer, inset within the top face
    o.append(_poly([(317, 174), (423, 174), (442, 164), (336, 164)], 1.0, "#e8e8e8"))
    o.append('<ellipse cx="522" cy="164" rx="34" ry="24" fill="none" stroke="%s" '
             'stroke-width="1.1"/>' % E)
    o.append(_line(462, 168, 500, 146, 1.2, E))
    o.append(_line(462, 176, 500, 186, 1.2, E))
    o.append(_lbl(430, 240, "(b)", "ts", "middle"))

    return _fig(svg(580, 258, "".join(o),
                    "Hai kiểu LED: phát xạ mặt và phát xạ cạnh"),
                "Hình 95.5 · Kiểu LED: (a) phát xạ mặt và (b) phát xạ cạnh.",
                "FIGURE 95.5 · LED type: (a) surface emitter and (b) edge emitter.",
                "Hai hình phối cảnh. Phần (a) một phiến bán dẫn nhiều lớp có cửa sổ nhỏ "
                "trên mặt, nón ánh sáng toả thẳng lên trên. Phần (b) một phiến mỏng có "
                "lớp hoạt động, chùm sáng phát ra từ cạnh bên theo phương nằm ngang",
                "Two perspective sketches. Part (a): a multilayer semiconductor slab with "
                "a small window on its face and a cone of light rising vertically. "
                "Part (b): a thin slab with an active layer, light leaving the side edge "
                "horizontally")


# ---------------------------------------------------------------- 95.6
def fig_95_6():
    tag = "956"
    o = [_defs(tag)]

    # hemispherical dome
    o.append(_rect(40, 104, 96, 18, 1.2, "#ffffff"))
    o.append('<path d="M40 104 A48 48 0 0 1 136 104" fill="none" stroke="%s" '
             'stroke-width="1.4"/>' % E)
    o.append(_rect(76, 92, 24, 12, 1.1, "#e8e8e8"))
    o.append(_lbl(88, 140, "Hemispherical", "ts", "middle"))

    # paraboloid cap
    o.append(_rect(190, 104, 96, 18, 1.2, "#ffffff"))
    o.append('<path d="M190 104 Q238 66 286 104" fill="none" stroke="%s" '
             'stroke-width="1.4"/>' % E)
    o.append(_rect(226, 94, 24, 10, 1.1, "#e8e8e8"))
    o.append(_lbl(238, 140, "Paraboloid", "ts", "middle"))

    # radiation pattern
    cx, cy = 440, 158
    o.append(_rect(340, 58, 200, 200, 1.0, "none"))
    o.append(_line(cx, 58, cx, 258, 0.8, S, "3 3"))
    o.append(_line(340, cy, 540, cy, 0.8, S, "3 3"))
    o.append('<ellipse cx="%s" cy="%s" rx="82" ry="46" fill="none" stroke="%s" '
             'stroke-width="1.3" stroke-dasharray="5 4"/>' % (_f(cx), _f(cy), S))
    o.append('<ellipse cx="%s" cy="%s" rx="34" ry="88" fill="none" stroke="%s" '
             'stroke-width="1.4"/>' % (_f(cx), _f(cy), E))
    o.append(_lbl(cx + 42, 78, "Paraboloid", "ts"))
    o.append(_lbl(346, 232, "Hemispherical", "ts"))
    return _fig(svg(580, 268, "".join(o),
                    "Hình học vỏ bọc LED và đồ thị phát xạ"),
                "Hình 95.6 · Các dạng hình học vỏ bọc LED và đồ thị phát xạ tương ứng.",
                "FIGURE 95.6 · LED encapsulation geometries and their radiation patterns.",
                "Bên trái là hai mặt cắt vỏ bọc: nắp bán cầu và nắp parabôlôit, mỗi vỏ "
                "đặt trên đế có chip phát xạ. Bên phải là đồ thị phát xạ cực với hai vòng: "
                "vòng hẹp và dài của parabôlôit, vòng rộng và thấp của bán cầu",
                "On the left, two encapsulation cross-sections: a hemispherical dome and "
                "a paraboloid cap, each on a base carrying the emitting chip. On the "
                "right, a polar radiation plot with two lobes: the narrow tall paraboloid "
                "lobe and the wide short hemispherical lobe")


# ---------------------------------------------------------------- 95.7
def _opto(x0, y0, tag, label=""):
    """Dashed 96x96 optocoupler block: LED at x0+24, phototransistor at x0+84.

    Terminals: LED anode (top-left), LED cathode (bottom-left),
    PT collector (top-right), PT emitter (bottom-right).
    """
    o = [_rect(x0, y0, 96, 96, 1.0, "none", "5 4", S)]
    lx, px = x0 + 24, x0 + 84
    # LED, pointing down (anode on top)
    o.append(_line(lx, y0, lx, y0 + 26, 1.2))
    o.append(_poly([(lx - 9, y0 + 26), (lx + 9, y0 + 26), (lx, y0 + 42)], 1.1, "#ffffff"))
    o.append(_line(lx - 9, y0 + 42, lx + 9, y0 + 42, 1.6))
    o.append(_line(lx, y0 + 42, lx, y0 + 96, 1.2))
    # emission arrows toward the transistor
    o.append(_arr(lx + 13, y0 + 30, lx + 34, y0 + 40, tag, 0.9, E, "h"))
    o.append(_arr(lx + 13, y0 + 46, lx + 34, y0 + 56, tag, 0.9, E, "h"))
    # phototransistor: base bar vertical, collector up-right, emitter down-right
    o.append(_line(px - 14, y0 + 34, px - 14, y0 + 62, 2.0))
    o.append(_line(px - 14, y0 + 40, px, y0 + 30, 1.2))
    o.append(_line(px, y0 + 30, px, y0, 1.2))
    o.append(_line(px - 14, y0 + 56, px, y0 + 66, 1.2))
    o.append(_arr(px - 8, y0 + 60, px - 1, y0 + 65, tag, 0.9, E, "h"))
    o.append(_line(px, y0 + 66, px, y0 + 96, 1.2))
    if label:
        o.append(_lbl(x0 + 102, y0 + 54, label, "ts"))
    return "".join(o)


def fig_95_7():
    tag = "957"
    o = [_defs(tag)]

    # rails
    o.append(_line(200, 46, 600, 46, 1.2))
    o.append(_rich(600, 40, [("+V", False), ("CC", True)], "start", "ts"))
    o.append(_line(60, 400, 640, 400, 1.2))

    # optocouplers
    o.append(_opto(300, 80, tag, "Optocoupler"))
    o.append(_opto(300, 264, tag, "Optocoupler"))

    # ---- control path
    o.append(_rect(150, 240, 56, 78, 1.3, "#ffffff"))
    o.append(_lbl(178, 284, "T", "tf", "middle"))
    o.append(_line(88, 282, 150, 282, 1.2))
    o.append(_lbl(88, 296, "Control", "ts"))
    o.append(_lbl(88, 308, "input", "ts"))
    o.append(_lbl(198, 258, "Q", "tm", "end"))
    o.append(_lbl(198, 306, "Q", "tm", "end"))
    o.append(_line(190, 297, 199, 297, 1.0))
    # Q -> upper LED cathode
    o.append(_line(206, 254, 240, 254, 1.2))
    o.append(_line(240, 254, 240, 196, 1.2))
    o.append(_line(240, 196, 324, 196, 1.2))
    o.append(_line(324, 196, 324, 176, 1.2))
    # Qbar -> lower LED cathode
    o.append(_line(206, 302, 256, 302, 1.2))
    o.append(_line(256, 302, 256, 384, 1.2))
    o.append(_line(256, 384, 324, 384, 1.2))
    o.append(_line(324, 384, 324, 360, 1.2))

    # ---- LED anodes to +Vcc
    o.append(_line(324, 80, 324, 46, 1.2))
    o.append(_line(324, 264, 420, 264, 1.2))
    o.append(_line(420, 264, 420, 46, 1.2))
    o.append(_dot(324, 46) + _dot(420, 46))

    # ---- V_in bus to both collectors
    o.append('<circle cx="64" cy="240" r="17" fill="none" stroke="%s" stroke-width="1.2"/>'
             % E)
    o.append('<path d="M56 240 q4 -7 8 0 q4 7 8 0" fill="none" stroke="%s" '
             'stroke-width="1.1"/>' % E)
    o.append(_rich(40, 244, [("V", False), ("in", True)], "end"))
    o.append(_line(64, 257, 64, 400, 1.2))
    o.append(_line(64, 223, 64, 212, 1.2))
    o.append(_line(64, 212, 250, 212, 1.2))
    o.append(_line(250, 212, 250, 64, 1.2))
    o.append(_line(250, 64, 384, 64, 1.2))
    o.append(_line(384, 64, 384, 80, 1.2))
    o.append(_line(250, 212, 250, 240, 1.2))
    o.append(_line(250, 240, 384, 240, 1.2))
    o.append(_line(384, 240, 384, 264, 1.2))
    o.append(_dot(250, 212))

    # ---- emitters to the summing node
    o.append(_line(384, 176, 384, 196, 1.2))
    o.append(_line(384, 196, 470, 196, 1.2))
    o.append(_line(470, 196, 470, 232, 1.2))
    o.append(_line(384, 360, 470, 360, 1.2))
    o.append(_line(470, 360, 470, 232, 1.2))
    o.append(_dot(470, 232))

    # ---- R1 into the inverting input
    o.append(_line(470, 232, 496, 232, 1.2))
    o.append(_rect(496, 225, 44, 14, 1.1, "#ffffff"))
    o.append(_lbl(512, 220, "R", "tm", "end"))
    o.append(_rich(514, 224, [("1", True)], "start", "ts"))
    o.append(_line(540, 232, 570, 232, 1.2))

    # ---- op-amp
    o.append(_poly([(570, 196), (570, 268), (636, 232)], 1.3, "#ffffff"))
    o.append(_lbl(582, 236, "−", "tf", "middle"))
    o.append(_lbl(582, 256, "+", "tf", "middle"))
    o.append(_line(570, 250, 552, 250, 1.2))
    o.append(_line(552, 250, 552, 300, 1.2))
    o.append(_rect(545, 300, 14, 34, 1.1, "#ffffff"))
    o.append(_lbl(530, 322, "R", "tm", "end"))
    o.append(_rich(532, 326, [("2", True)], "start", "ts"))
    o.append(_line(552, 334, 552, 400, 1.2))

    # ---- feedback Rf
    o.append(_line(556, 232, 556, 150, 1.2))
    o.append(_line(556, 150, 600, 150, 1.2))
    o.append(_rect(600, 143, 44, 14, 1.1, "#ffffff"))
    o.append(_lbl(622, 138, "R", "tm", "middle"))
    o.append(_rich(632, 138, [("f", True)], "start", "ts"))
    o.append(_line(644, 150, 676, 150, 1.2))
    o.append(_line(676, 150, 676, 232, 1.2))
    o.append(_line(636, 232, 676, 232, 1.2))
    o.append(_dot(556, 232))
    o.append(_dot(676, 232))
    o.append(_lbl(682, 236, "V", "tf"))
    o.append(_rich(694, 240, [("out", True)], "start", "ts"))

    # ground symbols
    for gx in (64, 552):
        o.append(_line(gx - 8, 400, gx + 8, 400, 1.4))
        o.append(_line(gx - 5, 405, gx + 5, 405, 1.1))
        o.append(_line(gx - 2, 410, gx + 2, 410, 0.9))

    return _fig(svg(720, 420, "".join(o),
                    "Mạch cắt tín hiệu dùng bộ khuếch đại thuật toán"),
                "Hình 95.7 · Mạch cắt tín hiệu có bộ khuếch đại.",
                "FIGURE 95.7 · A chopping circuit with an amplifier.",
                "Sơ đồ mạch: nguồn tín hiệu vào nối tới chân thu của hai bộ ghép quang "
                "kiểu LED và quang transistor, xung điều khiển qua trigơ T tạo hai pha "
                "ngược nhau nuôi hai LED; hai chân phát cộng lại thành nút rồi qua R một "
                "vào đầu đảo của bộ khuếch đại thuật toán, có hồi tiếp R f và R hai "
                "xuống đất, cho ra V out",
                "Circuit diagram: the input source feeds the collectors of two "
                "optocouplers built from an LED and a phototransistor, with a T flip-flop "
                "driving the two LEDs in antiphase; the emitters are summed into a node "
                "that reaches the inverting input through R-one, with feedback R-f and "
                "R-two to ground, giving V-out")


# ---------------------------------------------------------------- 95.8
_SEG16 = {
    "A": "a1 a2 f b e c g1 g2",
    "B": "a1 a2 f e b c g1 g2 d1 d2",
    "C": "a1 a2 f e d1 d2",
    "D": "a1 a2 f b c d1 d2",
    "E": "a1 a2 f e g1 g2 d1 d2",
    "F": "a1 a2 f e g1 g2",
    "G": "a1 a2 f e c d1 d2 g2",
    "H": "f e b c g1 g2",
    "I": "a1 a2 d1 d2 h j",
    "J": "a1 a2 b c d1 d2",
    "K": "f e m n",
    "L": "f e d1 d2",
    "M": "f e b c l m",
    "N": "f e b c l o",
    "O": "a1 a2 f e b c d1 d2",
    "P": "a1 a2 f e b g1 g2",
    "Q": "a1 a2 f e b c d1 d2 o",
    "R": "a1 a2 f e b g1 g2 n",
    "S": "a1 a2 f g1 g2 c d1 d2",
    "T": "a1 a2 h j",
    "U": "f e b c d1 d2",
    "V": "f e n o",
    "W": "f e b c n o",
    "X": "l m n o",
    "Y": "l m j",
    "Z": "a1 a2 m n d1 d2",
    "0": "a1 a2 f e b c d1 d2",
    "1": "b c",
    "2": "a1 a2 b g1 g2 e d1 d2",
    "3": "a1 a2 b c g1 g2 d1 d2",
    "4": "f b g1 g2 c",
    "5": "a1 a2 f g1 g2 c d1 d2",
    "6": "a1 a2 f e g1 g2 c d1 d2",
    "7": "a1 a2 b c",
    "8": "a1 a2 f e b c g1 g2 d1 d2",
    "9": "a1 a2 f b c g1 g2 d1 d2",
    "-": "g1 g2",
    "=": "g1 g2 d1 d2",
    "+": "g1 g2 h j",
    "/": "m n",
    ".": "",
}

_GEO = {
    "a1": (3, 0, 13, 3), "a2": (20, 0, 13, 3),
    "g1": (3, 26.5, 13, 3), "g2": (20, 26.5, 13, 3),
    "d1": (3, 53, 13, 3), "d2": (20, 53, 13, 3),
    "f": (0, 3, 3, 20.5), "e": (0, 29.5, 3, 20.5),
    "b": (33, 3, 3, 20.5), "c": (33, 29.5, 3, 20.5),
    "h": (16.5, 3, 3, 20.5), "j": (16.5, 29.5, 3, 20.5),
}
_DIA = {
    "l": ((3, 3), (16.5, 26.5)),
    "m": ((33, 3), (19.5, 26.5)),
    "n": ((3, 53), (16.5, 29.5)),
    "o": ((33, 53), (19.5, 29.5)),
}


def _seg16(dx, dy, s, segs, col=E):
    on = set(segs.split()) if segs else set()
    o = ['<g transform="translate(%s,%s) scale(%s)">' % (_f(dx), _f(dy), _f(s))]
    for k, (x, y, w, h) in _GEO.items():
        if k in on:
            o.append('<rect x="%s" y="%s" width="%s" height="%s" fill="%s"/>'
                     % (_f(x), _f(y), _f(w), _f(h), col))
    for k, (p, q) in _DIA.items():
        if k in on:
            o.append('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" '
                     'stroke-width="3"/>' % (_f(p[0]), _f(p[1]), _f(q[0]), _f(q[1]), col))
    if segs == "":
        o.append('<rect x="15" y="50" width="6" height="6" fill="%s"/>' % col)
    o.append("</g>")
    return "".join(o)


def _seg7(dx, dy, w, h, t=7):
    """Seven-segment figure-of-eight outline."""
    o = []
    for x, y, ww, hh in [(t, 0, w - 2 * t, t), (t, h / 2 - t / 2, w - 2 * t, t),
                         (t, h - t, w - 2 * t, t), (0, t, t, h / 2 - 1.5 * t),
                         (0, h / 2 + t / 2, t, h / 2 - 1.5 * t),
                         (w - t, t, t, h / 2 - 1.5 * t),
                         (w - t, h / 2 + t / 2, t, h / 2 - 1.5 * t)]:
        o.append('<rect x="%s" y="%s" width="%s" height="%s" fill="#bdbdbd"/>'
                 % (_f(dx + x), _f(dy + y), _f(ww), _f(hh)))
    return "".join(o)


def _matrix(dx, dy, cols, rows, pitch=7.4, on=None):
    o = []
    for r in range(rows):
        for c in range(cols):
            fill = E if (on and (r, c) in on) else "#c9c9c9"
            o.append('<rect x="%s" y="%s" width="4.8" height="4.8" fill="%s"/>'
                     % (_f(dx + c * pitch), _f(dy + r * pitch), fill))
    return "".join(o)


def fig_95_8():
    tag = "958"
    o = [_defs(tag)]

    # ---- (a) display formats
    o.append(_seg7(58, 26, 52, 86))
    o.append(_lbl(84, 132, "7-Segment", "ts", "middle"))
    o.append(_lbl(84, 144, "numeric", "ts", "middle"))

    glyph = {(0, 1), (0, 2), (1, 0), (1, 3), (2, 0), (2, 1), (2, 2), (2, 3),
             (3, 0), (3, 1), (3, 2), (3, 3), (4, 0), (4, 3), (5, 0), (5, 3),
             (6, 1), (6, 2)}
    o.append(_matrix(196, 30, 5, 7, 7.4, glyph))
    o.append(_lbl(211, 132, "5 × 7", "ts", "middle"))
    o.append(_lbl(211, 144, "Alphanumeric", "ts", "middle"))

    o.append(_matrix(330, 30, 4, 7, 7.4, glyph))
    o.append(_lbl(341, 132, "4 × 7", "ts", "middle"))
    o.append(_lbl(341, 144, "Hexadecimal", "ts", "middle"))

    o.append(_seg16(452, 26, 1.55, _SEG16["8"]))
    o.append(_lbl(480, 132, "16-Segment", "ts", "middle"))
    o.append(_lbl(480, 144, "alphanumeric", "ts", "middle"))
    o.append(_lbl(300, 170, "(a)", "ts", "middle"))

    # ---- (b) character grid
    rows = ["ABCDEFGHIJKLMN",
            "OPQRSTUVWXYZ-=",
            "0123456789+/."]
    x0, y0, s, gx, gy = 44, 200, 0.70, 41, 12
    for r, line in enumerate(rows):
        for c, ch in enumerate(line):
            o.append(_seg16(x0 + c * gx, y0 + r * (40 + gy), s, _SEG16.get(ch, "")))
    o.append(_lbl(300, y0 + 3 * (40 + gy) + 6, "(b)", "ts", "middle"))

    return _fig(svg(640, 368, "".join(o),
                    "Các dạng hiển thị LED và bộ ký tự"),
                "Hình 95.8 · (a) Các dạng hiển thị LED; và (b) các ký tự chữ và số hiển "
                "thị bằng màn 16 đoạn.",
                "FIGURE 95.8 · (a) LED display formats; and (b) displayed alphanumeric "
                "characters using 16-segment displays.",
                "Phần (a) bốn kiểu hiển thị: bảy đoạn số, ma trận điểm 5 nhân 7 chữ và "
                "số, ma trận 4 nhân 7 thập lục phân, và mười sáu đoạn chữ và số. Phần "
                "(b) bảng các ký tự từ A đến Z, các chữ số và ký hiệu được vẽ bằng đoạn "
                "của màn mười sáu đoạn",
                "Part (a): four display formats — seven-segment numeric, 5-by-7 dot "
                "matrix alphanumeric, 4-by-7 hexadecimal, and sixteen-segment "
                "alphanumeric. Part (b): a chart of the letters A to Z, the digits and "
                "symbols drawn with the segments of a sixteen-segment display")


# ---------------------------------------------------------------- dispatch
_FIGS = {
    1: fig_95_1, 2: fig_95_2, 3: fig_95_3, 4: fig_95_4,
    5: fig_95_5, 6: fig_95_6, 7: fig_95_7, 8: fig_95_8,
}


def fig(n):
    return _FIGS[n]()
