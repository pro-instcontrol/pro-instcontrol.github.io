# -*- coding: utf-8 -*-
"""Vector figures for Handbook Chapter 8 — Proximity Sensing for Robotics.

The source chapter carries seventeen figures and one table.  Each diagram
here redraws the principle the text describes; the response curves are
computed from the relation named in the caption, never sketched.

Every function returns (svg, caption_vi, caption_en, aria_vi, aria_en).
"""
import math

from hbfig import GOLD, INK, MUTED, TXT, _f, svg, _fig

BLUE = "#2f5d8a"
RED = "#a8322d"
GREEN = "#3f6b47"
SAND = "#f7f4ed"
BAND = "#eef2f6"

STY = ('<style>'
       '.b8{font:9.2px Inter,Helvetica,sans-serif;fill:#111;font-weight:600}'
       '.t8{font:8.8px Inter,Helvetica,sans-serif;fill:#111}'
       '.s8{font:8.0px Inter,Helvetica,sans-serif;fill:#555}'
       '.k8{font:7.6px Inter,Helvetica,sans-serif;fill:#666}'
       '</style>')


# ---------------------------------------------------------------- primitives
def _t(x, y, s, fs=8.8, anchor="middle", fill=TXT, bold=False):
    w = ' font-weight="600"' if bold else ""
    return ('<text x="%s" y="%s" font-size="%s" fill="%s" text-anchor="%s"%s>%s</text>'
            % (_f(x), _f(y), fs, fill, anchor, w, s))


def _l(x1, y1, x2, y2, sw=1.0, color=INK, dash=""):
    d = ' stroke-dasharray="%s"' % dash if dash else ""
    return ('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="%s"%s/>'
            % (_f(x1), _f(y1), _f(x2), _f(y2), color, sw, d))


def _r(x, y, w, h, fill="#fff", sw=1.0, color=INK, dash=""):
    d = ' stroke-dasharray="%s"' % dash if dash else ""
    return ('<rect x="%s" y="%s" width="%s" height="%s" fill="%s" stroke="%s" '
            'stroke-width="%s"%s/>' % (_f(x), _f(y), _f(w), _f(h), fill, color, sw, d))


def _c(x, y, r, fill="#fff", sw=1.0, color=INK):
    return ('<circle cx="%s" cy="%s" r="%s" fill="%s" stroke="%s" stroke-width="%s"/>'
            % (_f(x), _f(y), _f(r), fill, color, sw))


def _p(d, fill="none", sw=1.0, color=INK, dash=""):
    ds = ' stroke-dasharray="%s"' % dash if dash else ""
    return ('<path d="%s" fill="%s" stroke="%s" stroke-width="%s"%s/>'
            % (d, fill, color, sw, ds))


def _poly(pts, fill="none", sw=1.0, color=INK, close=False):
    d = "M " + " L ".join("%s %s" % (_f(a), _f(b)) for a, b in pts)
    if close:
        d += " Z"
    return _p(d, fill, sw, color)


def _arrow(x1, y1, x2, y2, sw=1.0, color=INK, dash=""):
    a = math.atan2(y2 - y1, x2 - x1)
    h = 5.0
    p1 = (x2 - h * math.cos(a - 0.42), y2 - h * math.sin(a - 0.42))
    p2 = (x2 - h * math.cos(a + 0.42), y2 - h * math.sin(a + 0.42))
    return (_l(x1, y1, x2, y2, sw, color, dash)
            + _poly([p1, (x2, y2), p2], color, sw * 0.8, color, close=True))


def _axes(x, y, xl, yl, xr=30, yu=26, color=INK):
    """A two-axis glyph with arrowheads and axis labels."""
    return (_arrow(x, y, x + xr, y, 1.1, color) + _arrow(x, y, x, y - yu, 1.1, color)
            + _t(x + xr + 2, y + 3, xl, 8.0, "start", color)
            + _t(x, y - yu - 5, yl, 8.0, "middle", color))


def _plot(x0, y0, w, h, xlab, ylab, xt, yt, fn, n=90, color=INK, sw=1.6, xr=(0, 1)):
    """A framed plot with ticks; fn(u) -> v with u in xr, v normalised 0..1."""
    out = [_l(x0, y0, x0 + w, y0, 1.1) + _l(x0, y0, x0, y0 - h, 1.1)]
    for u, lab in xt:
        px = x0 + u * w
        out.append(_l(px, y0, px, y0 + 3.5, 0.9))
        out.append(_t(px, y0 + 13, lab, 7.6, "middle", "#555"))
    for v, lab in yt:
        py = y0 - v * h
        out.append(_l(x0, py, x0 - 3.5, py, 0.9))
        out.append(_t(x0 - 6, py + 2.6, lab, 7.6, "end", "#555"))
    pts = []
    for i in range(n + 1):
        u = xr[0] + (xr[1] - xr[0]) * i / float(n)
        pts.append((x0 + (u - xr[0]) / (xr[1] - xr[0]) * w, y0 - fn(u) * h))
    out.append(_poly(pts, "none", sw, color))
    out.append(_t(x0 + w / 2.0, y0 + 27, xlab, 8.0, "middle", "#555"))
    out.append('<text x="%s" y="%s" font-size="8" fill="#555" text-anchor="middle" '
               'transform="rotate(-90 %s %s)">%s</text>'
               % (_f(x0 - 22), _f(y0 - h / 2.0), _f(x0 - 22), _f(y0 - h / 2.0), ylab))
    return "".join(out)


# ---------------------------------------------------------------- 8.1
def fig_8_1():
    b = []
    # the sensor body
    b.append(_r(46, 96, 62, 40, SAND, 1.1))
    b.append(_t(77, 120, "cảm biến", 8.0, "middle", "#333"))
    b.append(_axes(108, 116, "Xp", "Yp", 34, 30))
    b.append(_t(96, 152, "Zp", 8.0, "start", "#333"))
    b.append(_arrow(108, 116, 82, 140, 1.0, INK))
    b.append(_t(46, 88, "Fp", 8.6, "start", INK, True))

    # the object surface, drawn as a slanted plane in perspective
    b.append(_poly([(250, 44), (352, 78), (352, 200), (250, 166)], SAND, 1.1, close=True))
    b.append(_poly([(352, 78), (410, 56), (410, 178), (352, 200)], "#efece4", 1.1, close=True))
    b.append(_t(300, 108, "bề mặt vật", 8.0, "middle", "#444"))

    # the measured point and its frame
    P = (250, 104)
    b.append(_c(P[0], P[1], 2.6, INK))
    b.append(_t(P[0] - 5, P[1] - 6, "P", 8.4, "end", INK, True))
    b.append(_arrow(108, 116, P[0] - 4, P[1] + 1, 1.2, RED))
    b.append(_t(176, 100, "x", 9.4, "middle", RED, True))

    # surface frame at P
    b.append(_arrow(P[0], P[1], P[0] + 26, P[1] - 12, 1.0, BLUE))
    b.append(_t(P[0] + 30, P[1] - 12, "Yr", 8.0, "start", BLUE))
    b.append(_arrow(P[0], P[1], P[0] - 16, P[1] - 22, 1.0, BLUE))
    b.append(_t(P[0] - 22, P[1] - 26, "Zr", 8.0, "end", BLUE))
    b.append(_t(P[0] + 8, P[1] + 14, "Fr", 8.6, "start", BLUE, True))

    # the two orientation angles
    b.append(_p("M 108 116 A 44 44 0 0 0 130 142", "none", 1.0, GREEN, "4 3"))
    b.append(_t(120, 156, "u", 9.0, "start", GREEN, True))
    b.append(_p("M 232 96 A 26 26 0 0 1 236 116", "none", 1.0, GREEN, "4 3"))
    b.append(_t(214, 104, "v", 9.0, "end", GREEN, True))

    b.append(_t(280, 226, "x: dịch theo Xp   ·   u: quay quanh Yp   ·   v: quay quanh Zr",
                8.2, "middle", "#555"))
    return _fig(svg(560, 240, STY + "".join(b), "Sơ đồ ba tham số tư thế của vật"),
                "Hình 8-1. Ba tham số tư thế. x là khoảng dịch từ gốc hệ quy chiếu của cảm biến Fp "
                "tới điểm P trên bề mặt vật, đo dọc theo Xp. Tại P dựng hệ quy chiếu bề mặt Fr; u là "
                "góc nghiêng dọc của bề mặt, tức phép quay quanh Yp của hệ đã dịch, và v là góc "
                "nghiêng ngang, tức phép quay quanh Zr.",
                "Figure 8-1. The three pose parameters. x is the translation from the sensor frame Fp "
                "to a point P on the object surface, measured along Xp. At P a surface frame Fr is "
                "set up; u is the vertical orientation of the surface, a rotation about Yp of the "
                "translated frame, and v is the horizontal orientation, a rotation about Zr.",
                "Sơ đồ ba tham số tư thế: khoảng dịch x từ cảm biến tới điểm P, và hai góc nghiêng u, v.",
                "Diagram of the three pose parameters: the translation x from sensor to point P, and "
                "the two tilt angles u and v.")


# ---------------------------------------------------------------- 8.2
def fig_8_2():
    b = []
    b.append(_r(40, 52, 66, 30, BAND, 1.1))
    b.append(_t(73, 71, "nguồn 1", 8.2, "middle", "#333"))
    b.append(_r(40, 116, 66, 30, BAND, 1.1))
    b.append(_t(73, 135, "nguồn 2", 8.2, "middle", "#333"))

    b.append(_poly([(150, 30), (232, 74), (232, 140), (150, 96)], SAND, 1.1, close=True))
    b.append(_t(192, 92, "bề mặt", 7.8, "middle", "#444"))

    b.append(_arrow(108, 67, 152, 62, 1.0))
    b.append(_arrow(108, 131, 152, 104, 1.0))
    b.append(_t(122, 52, "Vem1", 7.6, "start", "#444"))
    b.append(_t(122, 132, "Vem2", 7.6, "start", "#444"))

    b.append(_arrow(190, 62, 150, 152, 1.0, RED))
    b.append(_r(120, 152, 62, 28, "#fff", 1.1, RED))
    b.append(_t(151, 170, "tách sóng", 8.0, "middle", RED))
    b.append(_t(206, 132, "Vrec", 8.0, "middle", RED, True))

    # the two drive waveforms, 90 degrees apart
    for k, (col, lab) in enumerate([(INK, "cos ωt"), (GOLD, "sin ωt")]):
        y0 = 178 + k * 32
        pts = [(300 + i * 1.2, y0 - 11 * math.cos(math.pi * i / 22.0 + k * math.pi / 2))
               for i in range(61)]
        b.append(_l(298, y0, 380, y0, 0.7, "#ccc"))
        b.append(_poly(pts, "none", 1.5, col))
        b.append(_t(386, y0 + 3, lab, 7.8, "start", col))

    b.append(_t(150, 214, "hai nguồn lệch pha 90°", 8.2, "middle", "#555"))
    b.append(_t(340, 60, "tín hiệu thu là chồng chập", 8.2, "middle", "#555"))
    b.append(_t(340, 74, "của hai tín hiệu phản xạ", 8.2, "middle", "#555"))
    return _fig(svg(560, 236, STY + "".join(b), "Sơ đồ cảm biến tiệm cận điều chế pha"),
                "Hình 8-2. Cấu hình cơ bản của cảm biến tiệm cận điều chế pha. Hai nguồn sáng được "
                "điều khiển bằng hai tín hiệu sin lệch pha 90°, nên tín hiệu thu là chồng chập của hai "
                "tín hiệu phản xạ; pha tổng hợp của nó mang thông tin khoảng cách.",
                "Figure 8-2. The basic phase-modulated proximity sensor. Two light sources are driven "
                "by sinusoidal signals 90° apart, so the received signal is a superposition of the two "
                "reflected signals; its combined phase carries the distance information.",
                "Sơ đồ cảm biến tiệm cận điều chế pha với hai nguồn lệch pha 90 độ và một bộ tách sóng.",
                "A phase-modulated proximity sensor with two sources 90 degrees apart and one detector.")


# ---------------------------------------------------------------- 8.3 / 8.4
def fig_8_3():
    b = []
    # the head seen face on: a ring of six LEDs about a central phototransistor
    b.append('<ellipse cx="200" cy="110" rx="52" ry="36" fill="%s" stroke="%s" stroke-width="1.2"/>'
             % (SAND, INK))
    b.append(_c(200, 110, 3.4, INK))
    for x, y, lab, anchor in [(148, 110, "4", "middle"), (174, 110, "1", "middle"),
                              (226, 110, "3", "middle"), (252, 110, "2", "middle"),
                              (174, 74, "5", "middle"), (226, 146, "6", "middle")]:
        b.append(_c(x, y, 6.0, "#fff", 1.0, BLUE))
        b.append(_t(x, y + 2.8, lab, 7.2, "middle", BLUE))

    # the two axes of the sensor frame
    b.append(_arrow(112, 110, 286, 110, 1.0, INK))
    b.append(_t(292, 113, "y", 8.4, "start", INK, True))
    b.append(_arrow(200, 110, 200, 54, 1.0, INK))
    b.append(_t(200, 46, "z", 8.4, "middle", INK, True))

    # the two spacings, 2a for the inner pair and 2b for the outer
    b.append(_l(174, 166, 174, 172, 0.9) + _l(226, 166, 226, 172, 0.9))
    b.append(_arrow(174, 169, 226, 169, 0.9, GREEN) + _arrow(226, 169, 174, 169, 0.9, GREEN))
    b.append(_t(200, 184, "2a", 8.2, "middle", GREEN, True))
    b.append(_l(148, 192, 148, 198, 0.9) + _l(252, 192, 252, 198, 0.9))
    b.append(_arrow(148, 195, 252, 195, 0.9, RED) + _arrow(252, 195, 148, 195, 0.9, RED))
    b.append(_t(200, 210, "2b", 8.2, "middle", RED, True))

    # legend
    b.append(_c(372, 74, 5.0, "#fff", 1.0, BLUE))
    b.append(_t(386, 77, "LED", 8.2, "start", "#333"))
    b.append(_c(372, 96, 3.4, INK))
    b.append(_t(386, 99, "phototransistor", 8.2, "start", "#333"))
    b.append(_t(372, 132, "sáu LED bố trí vòng quanh", 8.0, "middle", "#555"))
    b.append(_t(372, 144, "một phototransistor ở tâm", 8.0, "middle", "#555"))
    b.append(_t(372, 168, "hai khoảng cách 2a và 2b", 8.0, "middle", "#555"))
    b.append(_t(372, 180, "là các tham số hình học", 8.0, "middle", "#555"))
    return _fig(svg(560, 222, STY + "".join(b), "Đầu đo sáu LED và một phototransistor"),
                "Hình 8-3. Đầu đo của cảm biến dùng kỹ thuật điều chế pha: sáu nguồn sáng LED bố trí "
                "thành vòng quanh một phototransistor ở tâm. Hai khoảng cách 2a và 2b giữa các cặp LED "
                "đối xứng là các tham số hình học quyết định góc tới trong Hình 8-4.",
                "Figure 8-3. The sensor head of the phase-modulated sensor: six LED sources arranged "
                "on a ring about a central phototransistor. The two spacings 2a and 2b between the "
                "opposed LED pairs are the geometrical parameters that fix the incidence angles of "
                "Figure 8-4.",
                "Đầu đo gồm sáu LED xếp vòng quanh một phototransistor ở giữa, với hai khoảng cách 2a và 2b.",
                "A sensor head with six LEDs on a ring about a central phototransistor, and the two spacings 2a and 2b.")



def fig_8_4():
    b = []
    # the housing, clear of every ray
    b.append(_r(40, 60, 126, 30, SAND, 1.1))
    b.append(_t(103, 80, "đầu đo", 8.0, "middle", "#333"))

    # the four emitters used for the distance measurement, and the receiver
    for x, lab in [(64, "L4"), (86, "L1"), (120, "L3"), (142, "L2")]:
        b.append(_c(x, 112, 5.0, "#fff", 1.0, BLUE))
        b.append(_t(x, 102, lab, 6.6, "middle", BLUE))
    b.append(_c(103, 112, 5.4, "#fff", 1.0, RED))

    # the sensor frame: y along the emitter row, z down the axis
    b.append(_arrow(30, 112, 176, 112, 0.9, INK))
    b.append(_t(182, 115, "y", 8.2, "start", INK, True))

    # the two half-spacings, dimensioned on the row itself
    b.append(_l(86, 118, 86, 124, 0.9) + _l(103, 118, 103, 124, 0.9))
    b.append(_arrow(86, 121, 103, 121, 0.9, GREEN) + _arrow(103, 121, 86, 121, 0.9, GREEN))
    b.append(_t(97, 135, "a", 8.4, "middle", GREEN, True))
    b.append(_l(64, 142, 64, 148, 0.9) + _l(103, 142, 103, 148, 0.9))
    b.append(_arrow(64, 145, 103, 145, 0.9, RED) + _arrow(103, 145, 64, 145, 0.9, RED))
    b.append(_t(74, 159, "b", 8.4, "middle", RED, True))

    # the target surface, a distance x down the z axis
    b.append(_l(30, 206, 250, 206, 1.1))
    b.append(_t(140, 220, "bề mặt vật", 8.0, "middle", "#555"))
    b.append(_c(103, 206, 2.4, INK))
    b.append(_t(109, 200, "P", 8.2, "start", INK, True))
    b.append(_arrow(103, 112, 103, 204, 0.9, MUTED))
    b.append(_t(108, 180, "x", 9.0, "start", "#666", True))

    # the four rays from the emitters down to the measured point
    for x in (64, 86, 120, 142):
        b.append(_l(x, 117, 103, 204, 0.9, BLUE, "4 3"))

    b.append(_t(370, 96, "cos α = x / √(a² + x²)", 8.4, "middle", "#333"))
    b.append(_t(370, 114, "cos β = x / √(b² + x²)", 8.4, "middle", "#333"))
    b.append(_t(370, 144, "bốn nguồn, hai cặp đối xứng,", 8.0, "middle", "#555"))
    b.append(_t(370, 156, "cho phép tách x khỏi C", 8.0, "middle", "#555"))
    b.append(_t(370, 178, "α: góc tới của chùm từ cặp trong", 8.0, "middle", "#555"))
    b.append(_t(370, 190, "β: góc tới của chùm từ cặp ngoài", 8.0, "middle", "#555"))
    return _fig(svg(560, 232, STY + "".join(b), "Sơ đồ bố trí bốn nguồn và các tham số đo"),
                "Hình 8-4. Các tham số đo của cảm biến bốn nguồn. Hai cặp LED đối xứng qua trục, cách "
                "trục các đoạn a và b; góc tới của mỗi chùm là α và β, với cos α = x/√(a² + x²). Nhờ "
                "tính đối xứng, độ sáng thu được phụ thuộc x qua pha chứ không qua hệ số phản xạ C của "
                "bề mặt.",
                "Figure 8-4. Measurement parameters of the four-source sensor. Two LED pairs sit "
                "symmetrically about the axis at distances a and b; the incidence angles are α and β, "
                "with cos α = x/√(a² + x²). The symmetry makes the received brightness depend on x "
                "through the phase rather than through the surface reflection factor C.",
                "Sơ đồ bốn nguồn LED đối xứng quanh trục, với các khoảng a, b và khoảng cách x tới bề mặt.",
                "Four LEDs placed symmetrically about the axis, with the spacings a and b and the distance x to the surface.")



def fig_8_5():
    b = []
    b.append(_r(50, 70, 56, 26, BAND, 1.1))
    b.append(_t(78, 87, "nguồn", 8.0, "middle", "#333"))
    b.append(_arrow(106, 83, 190, 96, 1.0))
    b.append(_poly([(196, 40), (300, 64), (300, 156), (196, 132)], SAND, 1.1, close=True))
    b.append(_t(248, 104, "bề mặt", 7.8, "middle", "#444"))
    b.append(_r(50, 118, 90, 58, "#fff", 1.1, RED))
    b.append(_t(84, 140, "ba bộ", 7.6, "middle", RED))
    b.append(_t(84, 150, "tách sóng", 7.6, "middle", RED))
    for i in range(3):
        b.append(_c(124, 132 + i * 15, 3.4, "#fff", 1.0, RED))
        b.append(_arrow(198, 98, 127, 132 + i * 15, 0.9, RED, "3 3"))
    b.append(_t(84, 192, "rec1 · rec2 · rec3", 7.8, "middle", RED))

    b.append(_t(390, 82, "một nguồn, nhiều bộ thu", 8.2, "middle", "#555"))
    b.append(_t(390, 96, "biên độ phản xạ quyết định tư thế", 8.2, "middle", "#555"))
    b.append(_t(390, 126, "cặp rec1–rec2 đo góc nghiêng", 8.0, "middle", "#555"))
    b.append(_t(390, 138, "cặp rec1–rec3 đo khoảng cách", 8.0, "middle", "#555"))
    return _fig(svg(560, 200, STY + "".join(b), "Sơ đồ cảm biến tiệm cận điều chế biên độ"),
                "Hình 8-5. Cấu hình cơ bản của cảm biến tiệm cận điều chế biên độ: một nguồn sáng và "
                "nhiều bộ tách sóng. Độ lớn ánh sáng phản xạ mang thông tin tư thế; ba bộ thu cho phép "
                "ghép cặp — rec1 với rec2 để đo góc nghiêng, rec1 với rec3 để đo khoảng cách.",
                "Figure 8-5. The basic amplitude-modulated proximity sensor: one light source and "
                "several photodetectors. The magnitude of the reflected light carries the pose "
                "information; three receivers allow pairing — rec1 with rec2 for orientation, rec1 with "
                "rec3 for distance.",
                "Sơ đồ cảm biến điều chế biên độ: một nguồn sáng và ba bộ tách sóng ghép cặp.",
                "An amplitude-modulated sensor: one light source and three paired photodetectors.")


def fig_8_6():
    b = []
    b.append(_r(56, 52, 150, 44, SAND, 1.1))
    b.append(_t(131, 72, "đầu đo", 8.2, "middle", "#333"))
    b.append(_t(131, 86, "mặt phẳng chuẩn", 7.4, "middle", "#666"))

    # emitter and receiver fibres leaving the head
    b.append(_l(96, 96, 96, 150, 1.6, BLUE))
    b.append(_t(90, 148, "phát", 7.8, "end", BLUE, True))
    b.append(_l(150, 96, 172, 150, 1.6, RED))
    b.append(_t(182, 148, "thu", 7.8, "start", RED, True))

    # separation d and inclination theta
    b.append(_l(96, 118, 150, 118, 0.9, MUTED, "4 3"))
    b.append(_t(123, 113, "d", 8.8, "middle", "#444", True))
    b.append(_p("M 150 96 A 62 62 0 0 1 168 128", "none", 0.9, GREEN))
    b.append(_t(176, 108, "ϑ", 8.6, "start", GREEN, True))

    b.append(_l(30, 176, 300, 176, 1.1))
    b.append(_t(165, 190, "bề mặt vật", 8.0, "middle", "#555"))
    b.append(_c(118, 176, 2.4, INK))
    b.append(_t(118, 168, "P", 8.2, "middle", INK, True))
    b.append(_l(96, 150, 118, 176, 0.8, BLUE, "3 3"))
    b.append(_l(172, 150, 118, 176, 0.8, RED, "3 3"))

    b.append(_t(420, 100, "sợi quang dẫn sáng", 8.2, "middle", "#555"))
    b.append(_t(420, 112, "tới và đi khỏi bề mặt", 8.2, "middle", "#555"))
    b.append(_t(420, 136, "nhờ đó mạch điện tử nhạy", 8.0, "middle", "#555"))
    b.append(_t(420, 148, "nằm xa nguồn nhiễu của rô bốt", 8.0, "middle", "#555"))
    return _fig(svg(560, 204, STY + "".join(b), "Sơ đồ đầu đo kiểu dẫn Y"),
                "Hình 8-6. Đầu đo kiểu dẫn Y. Sợi phát đặt vuông góc với mặt phẳng chuẩn của đầu đo; "
                "sợi thu nghiêng một góc ϑ và cách sợi phát một khoảng d. Cấu hình này đưa phần điện tử "
                "nhạy ra xa rô bốt, nơi có nhiễu điện từ.",
                "Figure 8-6. The Y-guide transducer. The emitting fibre is perpendicular to the "
                "transducer face; the receiving fibre is inclined at ϑ and separated from the emitter by "
                "d. This configuration moves the sensitive electronics away from the robot's "
                "electromagnetic interference.",
                "Sơ đồ đầu đo kiểu dẫn Y với sợi phát vuông góc và sợi thu nghiêng góc theta.",
                "A Y-guide transducer with a perpendicular emitter fibre and a receiver inclined at theta.")


def fig_8_7():
    def resp(u):
        # convolution of the emitter cone with the receiver acceptance, normalised:
        # a gamma-shaped response that rises to a peak then falls as 1/x^2
        v = (u / 0.34) * math.exp(1 - u / 0.34)
        return max(0.0, min(1.0, v))

    b = [_plot(90, 176, 300, 120, "khoảng cách x", "độ sáng thu",
               [(0, "0"), (0.25, "xmin"), (0.5, ""), (0.75, ""), (1, "")],
               [(0, "0"), (1, "1")], resp, xr=(0.0, 1.0))]
    b.append(_l(90 + 0.34 * 300, 176, 90 + 0.34 * 300, 56, 0.9, RED, "4 3"))
    b.append(_t(90 + 0.34 * 300, 50, "đỉnh", 7.8, "middle", RED))
    b.append(_t(105, 72, "vùng không", 7.6, "middle", "#555"))
    b.append(_t(105, 82, "đơn điệu", 7.6, "middle", "#555"))
    b.append(_t(430, 96, "dưới xmin, cường độ", 8.0, "middle", "#555"))
    b.append(_t(430, 108, "không còn đơn điệu,", 8.0, "middle", "#555"))
    b.append(_t(430, 120, "nên phép đo vô nghiệm", 8.0, "middle", "#555"))
    b.append(_t(430, 140, "vì một giá trị cường độ", 8.0, "middle", "#555"))
    b.append(_t(430, 152, "ứng với hai khoảng cách", 8.0, "middle", "#555"))
    return _fig(svg(560, 208, STY + "".join(b), "Đường đáp ứng của đầu đo dẫn Y theo khoảng cách"),
                "Hình 8-7. Đáp ứng của đầu đo dẫn Y theo khoảng cách, tính từ tích chập của hình nón "
                "phát với góc thu nhận của sợi thu rồi chuẩn hoá. Đường cong không đơn điệu: nó lên tới "
                "một đỉnh rồi giảm theo 1/x². Vì vậy khoảng cách làm việc nhỏ nhất xmin phải được chọn "
                "sao cho đoạn sử dụng nằm hoàn toàn trên sườn dốc.",
                "Figure 8-7. The Y-guide response against distance, computed as the convolution of the "
                "emitter cone with the receiver fibre's acceptance and normalised. The curve is not "
                "monotonic: it rises to a peak and then falls as 1/x². The minimum operating distance "
                "xmin must therefore be chosen so that the working range lies entirely on the falling "
                "slope.",
                "Đồ thị đáp ứng của đầu đo dẫn Y: lên tới đỉnh rồi giảm, đánh dấu khoảng cách nhỏ nhất.",
                "A response curve that rises to a peak then falls, with the minimum distance marked.")


def fig_8_8():
    b = []
    b.append(_r(150, 40, 260, 52, SAND, 1.1))
    b.append(_t(280, 62, "đầu đo", 8.2, "middle", "#333"))
    b.append(_t(280, 78, "mặt phẳng chuẩn", 7.4, "middle", "#666"))
    for x, lab, col in [(200, "rec1", RED), (280, "phát", BLUE), (360, "rec2", RED)]:
        b.append(_l(x, 92, x, 148, 1.6, col))
        b.append(_t(x, 164, lab, 7.8, "middle", col, True))
    b.append(_l(30, 148, 500, 148, 1.1))
    b.append(_c(280, 148, 2.6, INK))
    b.append(_t(286, 143, "P", 8.2, "start", INK, True))
    b.append(_t(468, 118, "đối xứng qua trục", 7.8, "middle", "#666"))
    return _fig(svg(560, 190, STY + "".join(b), "Bố trí cặp bộ thu đối xứng để đo góc nghiêng"),
                "Hình 8-8. Bố trí cặp bộ thu điển hình để đo góc nghiêng: sợi phát ở giữa, hai sợi thu "
                "đặt đối xứng hai bên. Khi bề mặt nghiêng, một bộ thu nhận nhiều sáng hơn bộ kia, và "
                "hiệu chuẩn hoá của hai tín hiệu cho ra góc nghiêng.",
                "Figure 8-8. The typical receiver-pair constellation for orientation measurement: the "
                "emitter in the centre and two receivers placed symmetrically either side. As the "
                "surface tilts, one receiver collects more light than the other, and the normalised "
                "difference of the two signals gives the tilt angle.",
                "Sơ đồ ba sợi quang: một phát ở giữa, hai thu đối xứng hai bên.",
                "Three fibres: one emitter in the centre and two receivers placed symmetrically.")


def fig_8_9():
    def c1(u):                       # receiver on the left, tilted surface
        return math.exp(-((u - 0.30) / 0.26) ** 2)

    def c2(u):
        return math.exp(-((u + 0.30) / 0.26) ** 2)

    b = [_plot(90, 184, 300, 118, "góc nghiêng của bề mặt", "cường độ thu",
               [(0, "−30°"), (0.5, "0"), (1, "+30°")], [(0, "0"), (1, "1")], c1, xr=(-1, 1))]
    pts = []
    for i in range(91):
        u = -1 + 2 * i / 90.0
        pts.append((90 + (u + 1) / 2.0 * 300, 184 - c2(u) * 118))
    b.append(_poly(pts, "none", 1.5, RED))
    b.append(_l(90 + 0.5 * 300, 184, 90 + 0.5 * 300, 66, 0.8, MUTED, "4 3"))
    b.append(_t(90 + 0.35 * 300, 56, "rec1", 7.8, "middle", INK, True))
    b.append(_t(90 + 0.65 * 300, 56, "rec2", 7.8, "middle", RED, True))
    b.append(_c(240, 184 - 0.264 * 118, 2.4, INK))
    b.append(_t(248, 148, "giao điểm", 7.6, "start", "#555"))
    b.append(_t(430, 100, "hiệu chuẩn hoá hai tín hiệu", 8.0, "middle", "#555"))
    b.append(_t(430, 112, "cho ra góc nghiêng, đồng thời", 8.0, "middle", "#555"))
    b.append(_t(430, 124, "khử được biến thiên công suất", 8.0, "middle", "#555"))
    b.append(_t(430, 136, "phát xạ của nguồn", 8.0, "middle", "#555"))
    return _fig(svg(560, 216, STY + "".join(b), "Cường độ thu của mỗi bộ thu theo góc nghiêng bề mặt"),
                "Hình 8-9. Cường độ sáng mà mỗi bộ thu nhận được, theo góc nghiêng của bề mặt, tính theo "
                "một hàm Gauss lệch tâm cho từng bộ thu. Hai đường cắt nhau tại góc nghiêng bằng không; "
                "độ lệch giữa chúng là thước đo góc nghiêng.",
                "Figure 8-9. The light intensity each receiver collects against surface orientation, "
                "computed as an offset Gaussian for each receiver. The two curves cross at zero tilt; "
                "their separation is the measure of the tilt angle.",
                "Đồ thị hai đường cường độ theo góc nghiêng, cắt nhau tại góc không.",
                "Two intensity curves against tilt angle, crossing at zero tilt.")


def fig_8_10():
    b = []
    b.append(_r(130, 40, 300, 52, SAND, 1.1))
    b.append(_t(280, 70, "đầu đo", 8.2, "middle", "#333"))
    b.append(_l(200, 92, 200, 146, 1.6, BLUE))
    b.append(_t(200, 162, "phát", 7.8, "middle", BLUE, True))
    b.append(_l(360, 92, 386, 146, 1.6, RED))
    b.append(_t(396, 162, "rec", 7.8, "start", RED, True))
    b.append(_l(30, 146, 500, 146, 1.1))
    b.append(_c(292, 146, 2.6, INK))
    b.append(_t(292, 172, "P", 8.2, "middle", INK, True))
    b.append(_l(200, 118, 360, 118, 0.9, MUTED, "4 3"))
    b.append(_t(280, 112, "khoảng cách bất đối xứng", 7.6, "middle", "#555"))
    b.append(_t(280, 194, "cấu hình bất đối xứng dùng cho phép đo khoảng cách", 8.2, "middle", "#555"))
    return _fig(svg(560, 206, STY + "".join(b), "Bố trí cặp bộ thu bất đối xứng để đo khoảng cách"),
                "Hình 8-10. Bố trí cặp bộ thu bất đối xứng dùng cho phép đo khoảng cách. Cần lưu ý rằng "
                "tuy phép đo góc nghiêng không bị ảnh hưởng bởi khoảng cách, phép đo khoảng cách lại bị "
                "ảnh hưởng đáng kể bởi góc nghiêng của bề mặt; vì vậy phải xác định góc trước, rồi mới "
                "xác định khoảng cách.",
                "Figure 8-10. An asymmetrical receiver pair used for distance measurement. Note that "
                "while orientation measurements are unaffected by distance, distance measurements are "
                "strongly affected by surface orientation; the angle must therefore be estimated first, "
                "and the distance afterwards.",
                "Sơ đồ cặp bộ thu bất đối xứng dùng cho phép đo khoảng cách.",
                "An asymmetrical receiver pair arranged for distance measurement.")


def fig_8_11():
    b = []
    # (a) top view: one emitter at the centre, eight receivers on a ring
    b.append(_t(140, 24, "(a) nhìn từ trên", 8.4, "middle", "#333", True))
    b.append(_c(140, 108, 58, SAND, 1.1))
    b.append(_c(140, 108, 7.0, "#fff", 1.1, BLUE))
    b.append(_t(140, 128, "phát", 7.4, "middle", BLUE, True))
    for i in range(8):
        a = math.radians(-90 + i * 45)
        x = 140 + 42 * math.cos(a)
        y = 108 + 42 * math.sin(a)
        b.append(_c(x, y, 5.4, "#fff", 1.0, RED))
    b.append(_t(140, 190, "tám bộ thu trên một vòng", 7.8, "middle", "#555"))

    # (b) front view: the receivers are inclined towards the axis
    b.append(_t(420, 24, "(b) nhìn từ phía trước", 8.4, "middle", "#333", True))
    b.append(_r(300, 44, 240, 26, SAND, 1.1))
    b.append(_t(420, 61, "mặt phẳng chuẩn", 7.6, "middle", "#555"))
    for i, (x, s) in enumerate([(330, -1), (372, -1), (452, 1), (494, 1)]):
        b.append(_l(x, 70, x + s * 18, 128, 1.4, RED))
        b.append(_c(x + s * 18, 128, 4.0, "#fff", 1.0, RED))
    b.append(_l(420, 70, 420, 128, 1.4, BLUE))
    b.append(_c(420, 128, 4.0, "#fff", 1.0, BLUE))
    b.append(_l(240, 148, 580, 148, 1.1))
    b.append(_t(420, 164, "các bộ thu nghiêng vào trục", 7.8, "middle", "#555"))
    b.append(_t(420, 190, "một phát vuông góc, tám thu nghiêng", 7.8, "middle", "#555"))
    return _fig(svg(560, 204, STY + "".join(b), "Thiết kế đầu đo điều chế biên độ một phát tám thu"),
                "Hình 8-11. Thiết kế đầu đo điều chế biên độ: (a) nhìn từ trên, một bộ phát ở tâm và "
                "tám bộ thu trên một vòng; (b) nhìn từ phía trước, bộ phát đặt vuông góc còn tám bộ thu "
                "nghiêng vào trục. Cách ghép cặp tám tín hiệu cho phép xác định cả khoảng cách lẫn hai "
                "góc nghiêng với độ chính xác cao.",
                "Figure 8-11. The AM transducer design: (a) top view, one emitter at the centre and "
                "eight receivers on a ring; (b) front view, the emitter perpendicular and the eight "
                "receivers inclined towards the axis. Pairing the eight signals resolves the distance "
                "and both tilt angles to high accuracy.",
                "Hai hình: nhìn từ trên với một phát ở tâm và tám thu trên vòng; nhìn nghiêng với tám thu nghiêng vào trục.",
                "Two views: from above with one emitter and eight receivers on a ring; from the front with the receivers inclined.")


# ---------------------------------------------------------------- 8.12 / 8.13
def fig_8_12():
    b = []
    b.append(_r(50, 46, 132, 34, SAND, 1.1))
    b.append(_t(116, 67, "đầu đo", 8.2, "middle", "#333"))
    b.append(_c(80, 80, 4.2, "#fff", 1.0, BLUE))
    b.append(_t(80, 96, "laser", 7.2, "middle", BLUE))
    b.append(_l(100, 80, 100, 108, 1.0))
    b.append(_t(100, 120, "khe", 7.2, "middle", "#555"))
    for i in range(6):
        b.append(_r(120 + i * 9, 92, 7, 7, "#fff", 0.9, RED))
    b.append(_t(148, 118, "dãy thu", 7.2, "middle", RED))

    b.append(_l(320, 30, 320, 190, 1.1))
    b.append(_t(328, 44, "bề mặt", 7.6, "start", "#555"))
    b.append(_c(320, 104, 2.6, INK))
    b.append(_t(328, 108, "P", 8.2, "start", INK, True))

    b.append(_arrow(84, 82, 316, 104, 1.0, BLUE))
    b.append(_arrow(320, 104, 152, 96, 1.0, RED))
    b.append(_t(150, 156, "h: khoảng cách khe tới dãy thu", 7.8, "middle", "#555"))
    b.append(_t(150, 168, "yo: vị trí điểm ảnh", 7.8, "middle", "#555"))
    b.append(_t(150, 180, "yi: vị trí vệt sáng trên dãy", 7.8, "middle", "#555"))

    b.append(_t(420, 84, "quét dãy thu để tìm đường", 8.0, "middle", "#555"))
    b.append(_t(420, 96, "sáng cho tín hiệu cực đại;", 8.0, "middle", "#555"))
    b.append(_t(420, 108, "đường đó là đường hiệu dụng", 8.0, "middle", "#555"))
    b.append(_t(420, 132, "x/(x+h) = yo/yi", 8.6, "middle", "#333"))
    return _fig(svg(560, 196, STY + "".join(b), "Nguyên lý tam giác đạc để đo khoảng cách"),
                "Hình 8-12. Nguyên lý cơ bản của cảm biến tiệm cận đo khoảng cách bằng tam giác đạc. Một "
                "chùm sáng hẹp chiếu vào điểm P; dãy thu quét để tìm đường sáng cho tín hiệu cực đại — "
                "đường hiệu dụng. Từ vị trí vệt sáng yi, khoảng cách khe tới dãy thu h và vị trí yo suy "
                "ra khoảng cách x theo x/(x + h) = yo/yi.",
                "Figure 8-12. The basic principle of a triangulation proximity sensor. A narrow beam "
                "illuminates point P; the receiver array is scanned to find the light path giving the "
                "maximum signal — the effective light path. From the spot position yi, the slit-to-array "
                "distance h and the reference position yo, the distance follows from x/(x + h) = yo/yi.",
                "Sơ đồ tam giác đạc: tia laser chiếu tới điểm P, phản xạ qua khe vào dãy thu.",
                "A triangulation diagram: a laser beam reaches point P and reflects through a slit onto a receiver array.")


def fig_8_13():
    b = []
    b.append(_r(40, 50, 96, 40, SAND, 1.1))
    b.append(_t(88, 74, "sáu LED", 8.0, "middle", "#333"))
    for i in range(3):
        b.append(_l(136, 62 + i * 8, 214, 84 + i * 10, 1.0, BLUE))
    b.append(_c(224, 100, 17, "#fff", 1.2))
    b.append(_t(224, 98, "thấu", 6.8, "middle", "#444"))
    b.append(_t(224, 108, "kính", 6.8, "middle", "#444"))
    b.append(_poly([(300, 34), (386, 60), (386, 152), (300, 126)], SAND, 1.1, close=True))
    b.append(_t(343, 96, "bề mặt", 7.8, "middle", "#444"))
    for yy in (56, 96, 136):
        b.append(_arrow(241, 100, 296, yy, 0.9, BLUE, "3 3"))
    # the detector sits behind the lens, on the same optical bench
    b.append(_r(202, 128, 44, 24, "#fff", 1.0, RED))
    b.append(_t(224, 143, "dãy thu", 7.2, "middle", RED))
    b.append(_arrow(224, 117, 224, 128, 0.9, RED, "3 3"))
    b.append(_arrow(330, 120, 242, 106, 0.9, RED, "3 3"))

    b.append(_t(470, 80, "sáu nguồn phát lần lượt,", 8.0, "middle", "#555"))
    b.append(_t(470, 92, "tạo một hình nón sáng cố định", 8.0, "middle", "#555"))
    b.append(_t(470, 116, "mỗi lần một LED, chụp vệt sáng,", 8.0, "middle", "#555"))
    b.append(_t(470, 128, "được sáu điểm ba chiều;", 8.0, "middle", "#555"))
    b.append(_t(470, 140, "khớp mặt phẳng qua sáu điểm", 8.0, "middle", "#555"))
    return _fig(svg(560, 172, STY + "".join(b), "Cảm biến tiệm cận nhiều nguồn sáng"),
                "Hình 8-13. Cảm biến tiệm cận nhiều nguồn sáng. Sáu LED hồng ngoại lần lượt được phát "
                "xung, mỗi lần tạo một vệt sáng trên bề mặt; thấu kính hội tụ ảnh vệt đó xuống chip thu "
                "diện tích. Sáu điểm ba chiều thu được đủ để khớp một mặt phẳng, từ đó suy ra khoảng "
                "cách và góc nghiêng.",
                "Figure 8-13. The multilight-source proximity sensor. Six infrared LEDs are pulsed in "
                "turn, each producing one spot on the surface; an objective lens images that spot onto an "
                "area-array detector chip. The six resulting three-dimensional points are enough to fit a "
                "plane, which yields both the distance and the orientation.",
                "Sơ đồ cảm biến nhiều nguồn sáng: sáu LED, thấu kính và dãy thu diện tích.",
                "A multilight-source sensor with six LEDs, a lens and an area detector.")


# ---------------------------------------------------------------- 8.14 / 8.15
def fig_8_14():
    b = []
    b.append(_l(40, 116, 460, 116, 0.9, MUTED, "5 4"))
    b.append(_t(468, 119, "trục quang", 7.6, "start", "#777"))
    b.append(_l(250, 56, 250, 176, 2.2))
    b.append(_t(250, 48, "thấu kính", 7.8, "middle", "#444"))

    b.append(_c(70, 116, 2.8, INK))
    b.append(_t(70, 106, "P", 8.2, "middle", INK, True))
    b.append(_arrow(70, 116, 246, 68, 1.0, BLUE))
    b.append(_arrow(246, 164, 74, 122, 1.0, BLUE))
    b.append(_t(120, 132, "tia giới hạn PN", 7.6, "middle", BLUE))
    b.append(_arrow(70, 116, 430, 116, 1.0, RED))
    b.append(_t(150, 110, "x", 9.2, "middle", RED, True))
    b.append(_arrow(254, 116, 430, 96, 1.0, GREEN))
    b.append(_arrow(254, 116, 430, 136, 1.0, GREEN))
    b.append(_l(430, 96, 430, 136, 1.2, GREEN))
    b.append(_t(436, 142, "ảnh", 7.8, "middle", GREEN))
    b.append(_t(340, 138, "w", 9.0, "middle", GREEN, True))

    b.append(_t(300, 192, "x = f·w / (w − f)", 9.0, "middle", "#333"))
    return _fig(svg(560, 206, STY + "".join(b), "Nguyên lý định luật thấu kính Gauss"),
                "Hình 8-14. Nguyên lý đo khoảng cách theo định luật thấu kính Gauss. Chùm sáng trùng "
                "trục quang tạo một vệt trên bề mặt; ánh sáng tán xạ từ vệt được thấu kính thu lại. PN "
                "là tia giới hạn mà thấu kính còn thu được. Khoảng cách tới vật x suy ra từ tiêu cự f và "
                "vị trí ảnh w theo x = f·w/(w − f).",
                "Figure 8-14. Distance measurement by the Gaussian lens law. A beam collinear with the "
                "optical axis forms a spot on the surface; light scattered from it is collected by the "
                "lens. PN is the limiting ray the lens can still gather. The target distance x follows "
                "from the focal length f and the image position w as x = f·w/(w − f).",
                "Sơ đồ định luật thấu kính Gauss: tia tới, thấu kính, tia giới hạn và vị trí ảnh.",
                "A Gaussian lens diagram: incident ray, lens, limiting ray and image position.")


def fig_8_15():
    b = []
    cx, cy, R = 180, 92, 26
    cells = [(cx, cy)]
    for i in range(6):
        a = math.radians(-90 + i * 60)
        cells.append((cx + R * math.sqrt(3) * math.cos(a), cy + R * math.sqrt(3) * math.sin(a)))
    for (x, y) in cells:
        b.append(_poly([(x, y - R), (x + R * 0.87, y - R / 2), (x + R * 0.87, y + R / 2),
                        (x, y + R), (x - R * 0.87, y + R / 2), (x - R * 0.87, y - R / 2)],
                       SAND, 1.0, close=True))
        b.append(_c(x, y, 3.6, "#fff", 0.9, BLUE))
    b.append(_t(cx, cy + R * 2.75 + 14, "bảy khối cảm nhận xếp hình lục giác", 7.8, "middle", "#555"))
    b.append(_t(cx, cy + R * 2.75 + 26, "mỗi khối: thấu kính, gương nón,", 7.8, "middle", "#555"))
    b.append(_t(cx, cy + R * 2.75 + 38, "sáu dãy thu tuyến tính, một laser", 7.8, "middle", "#555"))

    b.append(_t(450, 84, "ba khối kề nhau lập thành", 8.0, "middle", "#555"))
    b.append(_t(450, 96, "một khối đo góc nghiêng;", 8.0, "middle", "#555"))
    b.append(_t(450, 108, "sáu khối như vậy cho sáu phép đo,", 8.0, "middle", "#555"))
    b.append(_t(450, 120, "tích phân lại thành góc cục bộ", 8.0, "middle", "#555"))
    return _fig(svg(560, 214, STY + "".join(b), "Bố trí bảy khối cảm nhận của HexEye"),
                "Hình 8-15. Bố trí của HexEye nhìn từ trên: bảy khối cảm nhận giống nhau xếp theo hình "
                "lục giác. Mỗi khối gồm một thấu kính vật, một gương nón, sáu dãy thu tuyến tính và một "
                "laser diode. Ba khối kề nhau lập thành một khối đo góc nghiêng, và sáu khối như vậy cho "
                "phép tích phân ra góc nghiêng cục bộ của bề mặt.",
                "Figure 8-15. The HexEye layout, top view: seven identical sensing units arranged in a "
                "hexagonal pattern. Each unit holds an objective lens, a conical mirror, six linear "
                "receiver arrays and a laser diode. Three neighbouring units form an orientation "
                "measurement unit, and the six such units integrate to the local surface orientation.",
                "Sơ đồ bảy khối cảm nhận xếp hình lục giác của HexEye.",
                "Seven sensing units arranged in a hexagonal pattern.")


# ---------------------------------------------------------------- 8.16 / 8.17
def fig_8_16():
    b = []
    b.append(_t(150, 22, "(a) cấu tạo", 8.4, "middle", "#333", True))
    b.append(_r(60, 40, 180, 14, "#fff", 1.2, INK))
    b.append(_t(150, 34, "bản cực của cảm biến", 7.4, "middle", "#444"))
    b.append(_r(60, 106, 180, 14, "#fff", 1.2, INK))
    b.append(_t(150, 132, "vật dẫn cần đo", 7.4, "middle", "#444"))
    b.append(_l(150, 54, 150, 106, 0.9, MUTED, "4 3"))
    b.append(_t(156, 82, "khe hở", 7.6, "start", "#555"))
    b.append(_t(150, 156, "C = εA / d", 8.8, "middle", "#333"))

    def cap(u):
        return min(1.0, 0.055 / max(u, 0.055))

    b.append(_t(420, 22, "(b) đáp ứng", 8.4, "middle", "#333", True))
    b.append(_plot(340, 150, 200, 96, "khe hở d", "điện dung C",
                   [(0, "0"), (0.5, ""), (1, "")], [(0, "0"), (1, "")], cap, xr=(0.05, 1.0)))
    b.append(_t(440, 190, "phi tuyến mạnh;", 7.8, "middle", "#555"))
    b.append(_t(440, 202, "độ nhạy tụt khi khe lớn", 7.8, "middle", "#555"))
    return _fig(svg(560, 214, STY + "".join(b), "Cảm biến tiệm cận điện dung kiểu bản cực song song"),
                "Hình 8-16. Cảm biến tiệm cận điện dung theo nguyên lý bản cực song song: (a) cấu tạo — "
                "bản cực của cảm biến là một bản, vật dẫn cần đo là bản kia; (b) đáp ứng — điện dung tỉ "
                "lệ nghịch với khe hở nên đường cong phi tuyến mạnh và độ nhạy tụt nhanh khi khe hở "
                "lớn. Đây là một trong ba hạn chế chính của kiểu cảm biến này.",
                "Figure 8-16. A capacitive proximity sensor on the parallel-plate principle: (a) the "
                "structure — the transducer forms one plate and the conducting target the other; (b) the "
                "response — capacitance is inversely proportional to the gap, so the curve is strongly "
                "non-linear and the sensitivity falls away quickly at large gaps. This is one of the "
                "three main limitations of the type.",
                "Hai hình: cấu tạo bản cực song song, và đường đáp ứng điện dung giảm theo khe hở.",
                "Two views: the parallel-plate structure, and the capacitance response falling with gap.")


def fig_8_17():
    b = []
    b.append(_t(150, 22, "(a) bố trí đầu đo", 8.4, "middle", "#333", True))
    cx, cy, R = 150, 108, 54
    b.append(_c(cx, cy, R, "none", 0.9, MUTED))
    b.append(_c(cx, cy, 5.4, "#fff", 1.1, BLUE))
    b.append(_t(cx, cy + 20, "T", 8.0, "middle", BLUE, True))
    for i in range(6):
        a = math.radians(-90 + i * 60)
        x, y = cx + R * math.cos(a), cy + R * math.sin(a)
        b.append(_c(x, y, 4.6, "#fff", 1.0, RED))
    b.append(_t(cx, cy + R + 22, "R: bán kính vòng thu", 7.8, "middle", "#555"))

    def delta(u):
        # path-length difference between two adjacent receivers on the ring,
        # δ = 2R sin(θ) sin(π/n), normalised to its value at the largest angle
        return math.sin(u * math.pi / 2.0)

    b.append(_t(420, 22, "(b) góc nghiêng theo δ", 8.4, "middle", "#333", True))
    b.append(_plot(340, 150, 200, 96, "góc nghiêng", "δ",
                   [(0, "0"), (0.5, ""), (1, "30°")], [(0, "0"), (1, "δmax")],
                   delta, xr=(0.0, 1.0)))
    b.append(_t(440, 190, "tăng số bộ thu hoặc giảm R", 7.8, "middle", "#555"))
    b.append(_t(440, 202, "sẽ mở rộng dải đo", 7.8, "middle", "#555"))
    return _fig(svg(560, 214, STY + "".join(b), "Cảm biến siêu âm đo góc nghiêng bằng hiệu quang trình"),
                "Hình 8-17. Cảm biến siêu âm đo góc nghiêng: (a) đầu đo phẳng với n bộ thu cách đều trên "
                "một vòng bán kính R quanh bộ phát T; (b) quan hệ giữa góc nghiêng của bề mặt và hiệu "
                "độ dài δ của hai đường phản xạ tới một cặp bộ thu kề nhau, tính theo δ = 2R·sin θ·sin(π/n). "
                "Tăng số bộ thu hoặc giảm R đều mở rộng được dải đo.",
                "Figure 8-17. An ultrasonic orientation sensor: (a) a planar head with n equally spaced "
                "receivers on a circle of radius R about the transmitter T; (b) the relation between the "
                "surface inclination and the path-length difference δ for an adjacent receiver pair, "
                "computed as δ = 2R·sin θ·sin(π/n). More receivers, or a smaller R, widen the measuring "
                "range.",
                "Hai hình: vòng sáu bộ thu quanh bộ phát, và đường quan hệ giữa góc nghiêng và hiệu quang trình.",
                "Two views: six receivers on a ring about the transmitter, and the relation between tilt and path difference.")


FIGURES = [fig_8_1, fig_8_2, fig_8_3, fig_8_4, fig_8_5, fig_8_6, fig_8_7, fig_8_8, fig_8_9,
           fig_8_10, fig_8_11, fig_8_12, fig_8_13, fig_8_14, fig_8_15, fig_8_16, fig_8_17]
