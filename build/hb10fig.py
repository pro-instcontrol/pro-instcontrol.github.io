# -*- coding: utf-8 -*-
"""Vector figures for Handbook Chapter 10 — Position, Location, Altitude Measurement.

Section 10.1 (Altitude Measurement, D. E. Manolakis) uses figures 10.1 to 10.7.
Charts are computed from the relation named in the caption; the two bias plots
follow the second-order Taylor term of Equation 10.44, so the bias grows with
the square of the horizontal distance.

Every function returns (svg, caption_vi, caption_en, aria_vi, aria_en).
"""
import math

from hbfig import GOLD, INK, MUTED, TXT, _f, svg, _fig

BLUE = "#2f5d8a"
RED = "#a8322d"
GREEN = "#3f6b47"
SAND = "#f7f4ed"
BAND = "#eef2f6"
PAPER = "#ffffff"

STY = ('<style>'
       '.b10{font:9.2px Inter,Helvetica,sans-serif;fill:#111;font-weight:600}'
       '.t10{font:8.8px Inter,Helvetica,sans-serif;fill:#111}'
       '.s10{font:8.0px Inter,Helvetica,sans-serif;fill:#555}'
       '.k10{font:7.4px Inter,Helvetica,sans-serif;fill:#666}'
       '</style>')


# ---------------------------------------------------------------- primitives
def _t(x, y, s, fs=8.8, anchor="middle", fill=TXT, bold=False, rot=None):
    w = ' font-weight="600"' if bold else ""
    r = ' transform="rotate(%s %s %s)"' % (rot, _f(x), _f(y)) if rot else ""
    return ('<text x="%s" y="%s" font-size="%s" fill="%s" text-anchor="%s"%s%s>%s</text>'
            % (_f(x), _f(y), fs, fill, anchor, w, r, s))


def _l(x1, y1, x2, y2, sw=1.0, color=INK, dash=""):
    d = ' stroke-dasharray="%s"' % dash if dash else ""
    return ('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="%s"%s/>'
            % (_f(x1), _f(y1), _f(x2), _f(y2), color, sw, d))


def _r(x, y, w, h, fill="none", sw=1.0, stroke=INK, rx=0):
    return ('<rect x="%s" y="%s" width="%s" height="%s" rx="%s" fill="%s" stroke="%s" '
            'stroke-width="%s"/>' % (_f(x), _f(y), _f(w), _f(h), _f(rx), fill, stroke, sw))


def _c(cx, cy, r, fill="none", sw=1.0, stroke=INK):
    return ('<circle cx="%s" cy="%s" r="%s" fill="%s" stroke="%s" stroke-width="%s"/>'
            % (_f(cx), _f(cy), _f(r), fill, stroke, sw))


def _poly(pts, fill="none", sw=1.0, stroke=INK, close=False):
    d = "M " + " L ".join("%s %s" % (_f(x), _f(y)) for x, y in pts) + (" Z" if close else "")
    return ('<path d="%s" fill="%s" stroke="%s" stroke-width="%s"/>' % (d, fill, stroke, sw))


def _p(d, fill="none", sw=1.0, color=INK, dash=""):
    ds = ' stroke-dasharray="%s"' % dash if dash else ""
    return ('<path d="%s" fill="%s" stroke="%s" stroke-width="%s"%s/>' % (d, fill, color, sw, ds))


def _arrow(x1, y1, x2, y2, sw=1.0, color=INK, dash=""):
    ang = math.atan2(y2 - y1, x2 - x1)
    L, W = 7.0, 3.0
    xa, ya = x2 - L * math.cos(ang) + W * math.sin(ang), y2 - L * math.sin(ang) - W * math.cos(ang)
    xb, yb = x2 - L * math.cos(ang) - W * math.sin(ang), y2 - L * math.sin(ang) + W * math.cos(ang)
    return (_l(x1, y1, x2, y2, sw, color, dash)
            + _poly([(x2, y2), (xa, ya), (xb, yb)], color, 0.8, color, close=True))


def _dot(x, y, r=3.0, fill=INK):
    return _c(x, y, r, fill, 0.8, fill)


# ---------------------------------------------------------------- chart kit
def _axes(x0, y0, w, h, xr, yr, xt, yt, xlab, ylab, ylab_up=True):
    """Framed axes with inward ticks; returns (svg, X(u), Y(v)) helpers."""
    o = [_l(x0, y0, x0 + w, y0, 1.1) + _l(x0, y0, x0, y0 - h, 1.1)]
    o.append(_l(x0 + w, y0, x0 + w, y0 - h, 0.7, "#bbb"))
    o.append(_l(x0, y0 - h, x0 + w, y0 - h, 0.7, "#bbb"))
    for u, lab in xt:
        px = x0 + (u - xr[0]) / (xr[1] - xr[0]) * w
        o.append(_l(px, y0, px, y0 + 3.5, 0.9))
        if lab:
            o.append(_t(px, y0 + 13, lab, 7.6, "middle", "#555"))
    for v, lab in yt:
        py = y0 - (v - yr[0]) / (yr[1] - yr[0]) * h
        o.append(_l(x0, py, x0 - 3.5, py, 0.9))
        if lab:
            o.append(_t(x0 - 6, py + 2.6, lab, 7.6, "end", "#555"))
    o.append(_t(x0 + w / 2.0, y0 + 27, xlab, 8.2, "middle", "#444"))
    rot = -90 if ylab_up else 90
    o.append('<text x="%s" y="%s" font-size="8.2" fill="#444" text-anchor="middle" '
             'transform="rotate(%d %s %s)">%s</text>'
             % (_f(x0 - 30), _f(y0 - h / 2.0), rot, _f(x0 - 30), _f(y0 - h / 2.0), ylab))

    def X(u):
        return x0 + (u - xr[0]) / (xr[1] - xr[0]) * w

    def Y(v):
        return y0 - (v - yr[0]) / (yr[1] - yr[0]) * h

    return "".join(o), X, Y


def _curve(X, Y, fn, xr, yr, color=INK, sw=1.6, dash="", n=140, clip=True):
    """Draw fn over xr; with clip the curve stops at the frame rather than
    running flat along the axis."""
    pts = []
    for i in range(n + 1):
        u = xr[0] + (xr[1] - xr[0]) * i / float(n)
        v = fn(u)
        if clip and (v < yr[0] or v > yr[1]):
            break
        pts.append((X(u), Y(v)))
    if len(pts) < 2:
        return ""
    d = "M " + " L ".join("%s %s" % (_f(x), _f(y)) for x, y in pts)
    ds = ' stroke-dasharray="%s"' % dash if dash else ""
    return '<path d="%s" fill="none" stroke="%s" stroke-width="%s"%s/>' % (d, color, sw, ds)


def _legend(x, y, items, title=None):
    """items: list of (label, color, dash, sw)"""
    o = []
    if title:
        o.append(_t(x, y, title, 7.6, "start", "#444", True))
        y += 11
    for lab, col, dash, sw in items:
        o.append(_l(x, y - 2.6, x + 20, y - 2.6, sw, col, dash))
        o.append(_t(x + 25, y, lab, 7.6, "start", "#444"))
        y += 11
    return "".join(o)


# ---------------------------------------------------------------- 10.1
def fig_10_1():
    """NAMS geometry: O antenna, C overhead at height z, B and A on the flightpath.

    C, B and A all sit on the flightpath, which is a level line; the slight slope
    is perspective only, so the height z is OC for every point on it.
    """
    b = []
    O = (250, 250)

    def fy(x):
        return 126.0 + (x - 100.0) * (-14.0 / 408.0)

    C = (250, fy(250))
    B = (370, fy(370))
    A = (450, fy(450))

    b.append(_arrow(O[0], O[1], O[0], 66, 1.1))
    b.append(_t(O[0], 58, "Z", 9.6, "middle", INK, True))
    b.append(_arrow(O[0], O[1], 100, 289, 1.1))
    b.append(_t(88, 298, "X", 9.6, "middle", INK, True))
    b.append(_arrow(O[0], O[1], 436, 289, 1.1))
    b.append(_t(448, 298, "Y", 9.6, "middle", INK, True))

    # the airlane: the flightpath with its two beam edges
    b.append(_l(100, fy(100), 508, fy(508), 2.0))
    b.append(_l(120, fy(120) - 16, 500, fy(500) - 16, 0.7, "#999"))
    b.append(_l(120, fy(120) + 16, 500, fy(500) + 16, 0.7, "#999"))
    b.append(_t(106, fy(106) - 9, "đường bay", 7.8, "start", "#555"))

    # slant ranges, each labelled off its own line
    b.append(_l(O[0], O[1], B[0], B[1], 1.0))
    b.append(_l(O[0], O[1], A[0], A[1], 1.0))
    b.append(_t(319, 191, "R′", 9.0, "middle", INK, True))
    b.append(_t(357, 192, "R", 9.0, "middle", INK, True))

    # z, y, x
    b.append(_t(240, 186, "z", 8.8, "middle", GREEN, True))
    b.append(_l(C[0], C[1], B[0], C[1], 0.0, GREEN))
    b.append(_t(310, 108, "y", 8.8, "middle", GREEN, True))
    b.append(_t(410, 104, "x", 8.8, "middle", GREEN, True))

    # depression angle beta at O, between the vertical and OB
    ang = math.atan2(B[0] - O[0], O[1] - B[1])
    r = 62.0
    ex, ey = O[0] + r * math.sin(ang), O[1] - r * math.cos(ang)
    b.append(_p("M %s %s A %s %s 0 0 1 %s %s" % (_f(O[0]), _f(O[1] - r), _f(r), _f(r),
                                                 _f(ex), _f(ey)), "none", 1.2, RED))
    b.append(_t(O[0] + 21, O[1] - r + 23, "β", 9.0, "middle", RED, True))

    for p, lab, dx, dy in ((C, "C", 0, -9), (B, "B", 0, -8), (A, "A", 12, -7)):
        b.append(_dot(p[0], p[1], 3.0))
        b.append(_t(p[0] + dx, p[1] + dy, lab, 9.0, "middle", INK, True))
    b.append(_t(470, 104, "máy bay", 7.8, "start", "#444"))
    b.append(_t(O[0], O[1] + 20, "ăng ten", 7.8, "middle", "#444"))

    return _fig(svg(560, 312, STY + "".join(b), "Hình học hệ NAMS"),
                "Hình 10-1. Hình học của Hệ đo độ chính xác dẫn đường (NAMS). BA = x, CB = y, "
                "OC = z, R′ = z/cos β.",
                "Figure 10-1. Geometry of the Navigation Accuracy Measurement System (NAMS). "
                "BA = x, CB = y, OC = z, R′ = z/cos β.",
                "Sơ đồ ba chiều: ăng ten dưới đất, đường bay phía trên, các đoạn x, y, z và góc hạ beta.",
                "A three-dimensional sketch of an antenna below an airlane with the segments x, y, z and the depression angle beta.")


def fig_10_2():
    """Single ATC radar: bearing beta measured from the Y axis."""
    b = []
    O = (150, 240)
    Xe = (392, 279)
    Ye = (302, 182)
    far = (Xe[0] + Ye[0] - O[0], Xe[1] + Ye[1] - O[1])
    b.append(_poly([O, Xe, far, Ye], BAND, 0.8, "#c9d3dd", close=True))

    a, bb = 0.62, 0.45
    Bp = (O[0] + a * (Xe[0] - O[0]) + bb * (Ye[0] - O[0]),
          O[1] + a * (Xe[1] - O[1]) + bb * (Ye[1] - O[1]))
    Cp = (O[0] + a * (Xe[0] - O[0]), O[1] + a * (Xe[1] - O[1]))
    Dp = (O[0] + bb * (Ye[0] - O[0]), O[1] + bb * (Ye[1] - O[1]))
    Ap = (Bp[0], Bp[1] - 108)

    b.append(_arrow(O[0], O[1], O[0], 70, 1.1))
    b.append(_t(O[0], 62, "Z", 9.6, "middle", INK, True))
    b.append(_arrow(O[0], O[1], Xe[0], Xe[1], 1.1))
    b.append(_t(Xe[0] + 10, Xe[1] + 6, "X", 9.6, "middle", INK, True))
    b.append(_arrow(O[0], O[1], Ye[0], Ye[1], 1.1))
    b.append(_t(Ye[0] + 6, Ye[1] - 6, "Y", 9.6, "middle", INK, True))

    b.append(_l(O[0], O[1], Cp[0], Cp[1], 1.6, GREEN))
    b.append(_l(O[0], O[1], Dp[0], Dp[1], 1.6, GREEN))
    b.append(_l(Bp[0], Bp[1], Cp[0], Cp[1], 0.8, GREEN, "4 3"))
    b.append(_l(Bp[0], Bp[1], Dp[0], Dp[1], 0.8, GREEN, "4 3"))
    b.append(_l(O[0], O[1], Bp[0], Bp[1], 0.9, "#999", "5 4"))

    b.append(_l(Bp[0], Bp[1], Ap[0], Ap[1], 1.8))
    b.append(_l(Bp[0] - 70, Bp[1] - 24, Ap[0] + 42, Ap[1] - 14, 1.8))

    b.append(_t((O[0] + Cp[0]) / 2.0, (O[1] + Cp[1]) / 2.0 + 13, "x", 8.8, "middle", GREEN, True))
    b.append(_t((O[0] + Dp[0]) / 2.0 - 9, (O[1] + Dp[1]) / 2.0 - 4, "y", 8.8, "middle", GREEN, True))
    b.append(_t(Bp[0] + 8, (Bp[1] + Ap[1]) / 2.0, "z", 8.8, "start", GREEN, True))

    # beta = angle BOD, measured from the Y axis
    a1 = math.atan2(Dp[0] - O[0], O[1] - Dp[1])
    a2 = math.atan2(Bp[0] - O[0], O[1] - Bp[1])
    r = 56.0
    p1 = (O[0] + r * math.sin(a1), O[1] - r * math.cos(a1))
    p2 = (O[0] + r * math.sin(a2), O[1] - r * math.cos(a2))
    b.append(_p("M %s %s A %s %s 0 0 1 %s %s" % (_f(p1[0]), _f(p1[1]), _f(r), _f(r),
                                                 _f(p2[0]), _f(p2[1])), "none", 1.2, RED))
    b.append(_t(O[0] + 30, O[1] - 46, "β", 9.0, "middle", RED, True))

    for p, lab, dx, dy in ((Bp, "B", 0, 14), (Cp, "C", 4, 12), (Dp, "D", -10, 0),
                           (Ap, "A", 14, -2)):
        b.append(_dot(p[0], p[1], 2.8))
        b.append(_t(p[0] + dx, p[1] + dy, lab, 9.0, "middle", INK, True))
    b.append(_t(Ap[0] + 16, Ap[1] - 12, "máy bay", 7.6, "start", "#444"))
    b.append(_t(O[0] - 10, O[1] + 16, "rađa", 7.6, "end", "#444"))

    return _fig(svg(560, 306, STY + "".join(b), "Hình học một rađa không lưu"),
                "Hình 10-2. Cấu hình hình học của hệ đo độ cao bằng một rađa không lưu. OC = x, "
                "OD = y, AB = z, β = ∠BOD.",
                "Figure 10-2. Geometric configuration of the height measurement system with a "
                "single air-traffic control radar. OC = x, OD = y, AB = z, β = ∠BOD.",
                "Sơ đồ ba chiều với mặt phẳng ngang OXY, điểm B là hình chiếu của máy bay A, góc beta đo từ trục Y.",
                "A three-dimensional sketch with the horizontal plane OXY, B the projection of the aircraft A, and beta measured from the Y axis.")


def fig_10_3():
    """SSROR: one SSR at the origin plus a distant omni radar."""
    b = []
    O = (90, 170)
    Xe = (470, 215)
    Ye = (210, 105)
    far = (Xe[0] + Ye[0] - O[0], Xe[1] + Ye[1] - O[1])
    b.append(_poly([O, Xe, far, Ye], BAND, 0.8, "#c9d3dd", close=True))

    M1 = (400, 170)
    M = (400, 80)
    M2 = (392, 125)
    Ax = (455, 190)
    A1 = (455, 203)

    b.append(_arrow(O[0], O[1], O[0], 50, 1.1))
    b.append(_t(O[0], 42, "Z", 9.4, "middle", INK, True))
    b.append(_arrow(O[0], O[1], Xe[0], Xe[1], 1.1))
    b.append(_t(Xe[0] + 8, Xe[1] + 8, "X", 9.4, "middle", INK, True))
    b.append(_arrow(O[0], O[1], Ye[0], Ye[1], 1.1))
    b.append(_t(Ye[0] + 4, Ye[1] - 8, "Y", 9.4, "middle", INK, True))

    # the horizontal triangle O - M1 - A1
    b.append(_l(O[0], O[1], M1[0], M1[1], 0.9, "#999", "5 4"))
    b.append(_l(O[0], O[1], A1[0], A1[1], 0.9, "#999", "5 4"))
    b.append(_l(M1[0], M1[1], A1[0], A1[1], 0.9, "#999", "5 4"))

    # slant ranges
    b.append(_l(O[0], O[1], M[0], M[1], 1.1))
    b.append(_t(245, 116, "Rs", 9.0, "middle", INK, True))
    b.append(_l(O[0], O[1], M1[0], M1[1], 1.1))
    b.append(_t(245, 163, "R", 9.0, "middle", INK, True))
    b.append(_l(M[0], M[1], Ax[0], Ax[1], 1.1, BLUE))
    b.append(_t(444, 122, "Ra", 9.0, "middle", BLUE, True))

    b.append(_l(M1[0], M1[1], M[0], M[1], 1.8))
    b.append(_t(M[0] + 9, (M1[1] + M[1]) / 2.0, "z", 8.8, "start", GREEN, True))
    b.append(_l(M1[0], M1[1], A1[0], A1[1], 1.6, GREEN))
    b.append(_t((M1[0] + A1[0]) / 2.0, M1[1] + 14, "xₐ", 8.8, "middle", GREEN, True))

    # theta: bearing at O, measured from the Y axis to the horizontal sight line
    r1 = 40.0
    a_y = math.atan2(Ye[1] - O[1], Ye[0] - O[0])
    p1 = (O[0] + r1 * math.cos(a_y), O[1] + r1 * math.sin(a_y))
    b.append(_p("M %s %s A %s %s 0 0 1 %s %s" % (_f(p1[0]), _f(p1[1]), _f(r1), _f(r1),
                                                 _f(O[0] + r1), _f(O[1])), "none", 1.1, RED))
    b.append(_t(140, 157, "θ", 8.8, "middle", RED, True))

    # phi: elevation angle at O, between the horizontal sight line and OM
    r2 = 95.0
    a_m = math.atan2(M[1] - O[1], M[0] - O[0])
    b.append(_p("M %s %s A %s %s 0 0 0 %s %s" % (_f(O[0] + r2), _f(O[1]), _f(r2), _f(r2),
                                                 _f(O[0] + r2 * math.cos(a_m)),
                                                 _f(O[1] + r2 * math.sin(a_m))), "none", 1.1, RED))
    b.append(_t(197, 152, "φ", 8.8, "middle", RED, True))

    for p, lab, dx, dy, an in ((M, "M", 13, -5, "start"), (M1, "M₁", -7, 14, "end"),
                               (M2, "M₂", -9, 4, "end"), (Ax, "A", 12, 3, "start"),
                               (A1, "A₁", 13, 8, "start"), (O, "O", -11, 13, "end")):
        b.append(_dot(p[0], p[1], 2.6))
        b.append(_t(p[0] + dx, p[1] + dy, lab, 8.6, an, INK, True))
    b.append(_t(O[0] - 13, O[1] - 2, "SSR", 8.0, "end", "#444"))
    b.append(_t(Ax[0] + 16, Ax[1] - 12, "omni", 7.8, "start", "#444"))
    b.append(_t(M[0] + 26, M[1] - 14, "máy bay", 7.8, "start", "#444"))

    return _fig(svg(560, 236, STY + "".join(b), "Hình học hệ SSROR"),
                "Hình 10-3. Hình học của hệ đo độ cao gồm một SSR và một rađa đẳng hướng (SSROR). "
                "Khoảng cách xₐ giữa hai rađa thường từ 80 km tới 160 km. M₁M = z.",
                "Figure 10-3. Geometry of the height estimation system with one SSR and one "
                "omnidirectional radar (SSROR). The distance xₐ of the radars typically ranges "
                "from 80 km up to 160 km. M₁M = z.",
                "Sơ đồ ba chiều: SSR tại gốc tọa độ, rađa đẳng hướng ở xa, máy bay phía trên với các tầm Rs, R và Ra.",
                "A three-dimensional sketch with the SSR at the origin, a distant omni radar, and the aircraft above with ranges Rs, R and Ra.")


def _bias_mult(x, z):
    """Range bias multiplier of eq. 10.15: 2*sqrt(x^2+z^2) - x, in km."""
    return 2.0 * math.sqrt(x * x + z * z) - x


def fig_10_4():
    b = []
    x0, y0, w, h = 96, 232, 396, 168
    xr, yr = (0.0, 80.0), (0.0, 90.0)
    ax, X, Y = _axes(x0, y0, w, h, xr, yr,
                     [(v, str(v)) for v in range(0, 81, 10)],
                     [(v, str(v)) for v in range(0, 91, 10)],
                     "khoảng cách ngang tới rađa omni [km]", "a [km]")
    b.append(ax)
    b.append(_curve(X, Y, lambda u: _bias_mult(u, 6.0), xr, yr, "#777", 1.3))
    b.append(_curve(X, Y, lambda u: _bias_mult(u, 9.0), xr, yr, INK, 2.2))
    b.append(_curve(X, Y, lambda u: _bias_mult(u, 12.0), xr, yr, BLUE, 1.4, "6 4"))
    b.append(_legend(x0 + w - 118, y0 - 34, [("z = 6 km", "#777", "", 1.3),
                                             ("z = 9 km", INK, "", 2.2),
                                             ("z = 12 km", BLUE, "6 4", 1.4)]))
    return _fig(svg(560, 268, STY + "".join(b), "Hệ số khuếch đại sai lệch theo tầm"),
                "Hình 10-4. Hệ số khuếch đại sai lệch tầm trong phép đo bình phương độ cao, theo "
                "khoảng cách ngang của máy bay tới rađa omni. Ba độ cao bay khác nhau được khảo "
                "sát. Rađa omni đặt tại vị trí (150 km, 0, 0).",
                "Figure 10-4. Range bias multiplier in squared height measurements as a function "
                "of the aircraft distance from the omni radar. Three different flight heights are "
                "examined. The omni radar is at position (150 km, 0, 0).",
                "Đồ thị hệ số khuếch đại a theo khoảng cách ngang, ba đường ứng với độ cao 6, 9 và 12 km.",
                "A chart of the multiplier a against horizontal distance, with three curves for flight heights of 6, 9 and 12 km.")


def fig_10_5():
    b = []
    T = (280, 62)
    st = [(104, 208), (176, 200), (280, 224), (348, 200), (452, 208)]
    labs = ["S₀", "S₁", "S₂", "S₃", "Sₙ₋₁"]
    rl = ["R₀", "R₁", "R₂", "R₃", "Rₙ₋₁"]
    for i, (s, lab, r) in enumerate(zip(st, labs, rl)):
        b.append(_l(T[0], T[1], s[0], s[1], 0.9))
        b.append(_dot(s[0], s[1], 2.8))
        b.append(_t(s[0], s[1] + 15, lab, 8.6, "middle", INK, True))
        mx, my = (T[0] + s[0]) / 2.0, (T[1] + s[1]) / 2.0
        b.append(_t(mx + (6 if s[0] < T[0] else -6), my - 4, r, 8.2, "middle", "#555"))
    for x in (392, 414, 436):
        b.append(_dot(x, 210, 1.6, "#666"))
    b.append(_poly([(262, 56), (272, 50), (292, 52), (298, 62), (288, 68), (266, 66)], "#fff", 1.1, INK, close=True))
    b.append(_t(T[0] + 30, T[1] - 4, "bộ phát đáp", 7.8, "start", "#444"))
    b.append(_t(280, 250, "một trạm phát hỏi, các trạm còn lại chỉ thu", 7.8, "middle", "#555"))
    return _fig(svg(560, 262, STY + "".join(b), "Cấu hình hệ N trạm SSR"),
                "Hình 10-5. Cấu hình tiêu biểu của hệ đo độ cao dựa trên N trạm SSR. Một trạm là "
                "trạm tích cực, nghĩa là vừa phát câu hỏi vừa thu trả lời, còn các trạm khác chỉ thu.",
                "Figure 10-5. Typical configuration of the height estimation systems that are based "
                "on N SSR stations. One of the stations is active, i.e., it both transmits the "
                "interrogations and receives the replies, whereas the other stations are receivers only.",
                "Sơ đồ bộ phát đáp trên máy bay và N trạm mặt đất bên dưới, mỗi trạm có một tầm Ri.",
                "A sketch of the aircraft transponder above N ground stations, each with its range Ri.")


def fig_10_6():
    b = []
    T = (280, 62)
    st = [(150, 206), (280, 226), (412, 206)]
    labs = ["DME 1", "DME 2", "DME 3"]
    rl = ["R₁", "R₂", "R₃"]
    for s, lab, r in zip(st, labs, rl):
        b.append(_l(T[0], T[1], s[0], s[1], 0.9))
        b.append(_dot(s[0], s[1], 2.8))
        b.append(_t(s[0], s[1] + 16, lab, 8.4, "middle", INK, True))
        mx, my = (T[0] + s[0]) / 2.0, (T[1] + s[1]) / 2.0
        b.append(_t(mx + (8 if s[0] < T[0] else (-8 if s[0] > T[0] else 8)), my - 3, r, 8.2,
                    "middle", "#555"))
    b.append(_poly([(262, 56), (272, 50), (292, 52), (298, 62), (288, 68), (266, 66)], "#fff", 1.1, INK, close=True))
    b.append(_t(T[0] + 30, T[1] - 4, "thiết bị DME", 7.8, "start", "#444"))
    b.append(_t(280, 252, "ba trạm mặt đất nằm dưới một đường hàng không", 7.8, "middle", "#555"))
    return _fig(svg(560, 264, STY + "".join(b), "Cấu hình hệ DME"),
                "Hình 10-6. Cấu hình của hệ đo độ cao trên máy bay dùng các phép đo khoảng cách "
                "từ thiết bị DME.",
                "Figure 10-6. Configuration of the on-board height estimation system that utilizes "
                "the distance measurements derived from the DME equipment.",
                "Sơ đồ máy bay với thiết bị DME và ba trạm mặt đất, các tầm R1, R2, R3.",
                "A sketch of an aircraft with DME equipment and three ground stations, with ranges R1, R2 and R3.")


def fig_10_7():
    b = []
    x0, y0, w, h = 104, 250, 388, 176
    xr, yr = (0.0, 35.0), (-160.0, 0.0)
    yt = [(0.0, "0")] + [(-v, "−%d" % v) for v in range(20, 161, 20)]
    ax, X, Y = _axes(x0, y0, w, h, xr, yr,
                     [(v, str(v)) for v in range(0, 36, 5)], yt,
                     "khoảng cách ngang từ tâm [km]", "sai lệch cố hữu [m]")
    b.append(ax)

    # second-order Taylor term of eq. 10.44: the bias grows with the square of the
    # horizontal distance, scaled by the triangle side
    specs = [(2.0, 10.0, INK, "", 1.6, 125.0), (8.0, 27.0, "#555", "", 1.6, 125.0),
             (16.0, 35.0, BLUE, "7 3", 1.5, 50.0), (24.0, 35.0, GREEN, "", 1.2, 20.0)]
    for side, xs, col, dash, sw, A in specs:
        b.append(_curve(X, Y, lambda u, A=A, xs=xs: -A * (u / xs) ** 2, xr, yr, col, sw, dash))
    for u in range(0, 36, 4):
        v = -20.0 * (u / 35.0) ** 2
        b.append(_dot(X(u), Y(max(-160.0, min(0.0, v))), 1.8, GREEN))

    # legend above the frame, on a single row, clear of every curve
    lx, ly = x0, y0 - h - 16
    b.append(_t(lx, ly, "cạnh tam giác [km]", 7.6, "start", "#444", True))
    cx = lx + 96
    for lab, col, dash, sw in (("2", INK, "", 1.6), ("8", "#555", "", 1.6),
                               ("16", BLUE, "7 3", 1.5), ("24", GREEN, "", 1.2)):
        b.append(_l(cx, ly - 2.6, cx + 18, ly - 2.6, sw, col, dash))
        b.append(_t(cx + 22, ly, lab, 7.6, "start", "#444"))
        cx += 46
    return _fig(svg(560, 292, STY + "".join(b), "Sai lệch cố hữu của thuật toán DME"),
                "Hình 10-7. Sai lệch cố hữu do thuật toán ước lượng độ cao của hệ dùng phép đo DME "
                "sinh ra. Vị trí các trạm tạo thành một tam giác đều. Sai lệch cố hữu được biểu "
                "diễn theo khoảng cách ngang từ tâm, với vài giá trị cạnh tam giác. Độ cao bay "
                "z = 9 km và độ lệch chuẩn sai số đo khoảng cách σ_R = 90 m.",
                "Figure 10-7. Bias inherently generated by the height estimation algorithm of the "
                "system based on DME measurements. The stations' sites form an equilateral triangle. "
                "The inherent bias is shown as function of the horizontal distance from the center "
                "for various magnitudes of the triangle side. The flight height is z = 9 km, and "
                "the SD of the distance measurement error is σ_R = 90 m.",
                "Đồ thị sai lệch cố hữu theo khoảng cách ngang từ tâm, bốn đường ứng với cạnh tam giác 2, 8, 16 và 24 km.",
                "A chart of the inherent bias against horizontal distance from the centre, with four curves for triangle sides of 2, 8, 16 and 24 km.")


# ---------------------------------------------------------------- 10.2
def _arc(cx, cy, r, a1, a2, color=RED, sw=1.2, dash=""):
    """Arc from a1 to a2 degrees, measured from +x with y up (so a2 > a1 reads
    counter-clockwise on screen, which needs sweep-flag 0)."""
    x1, y1 = cx + r * math.cos(math.radians(a1)), cy - r * math.sin(math.radians(a1))
    x2, y2 = cx + r * math.cos(math.radians(a2)), cy - r * math.sin(math.radians(a2))
    large = 1 if abs(a2 - a1) > 180 else 0
    sweep = 0 if a2 > a1 else 1
    return _p("M %s %s A %s %s 0 %d %d %s %s"
              % (_f(x1), _f(y1), _f(r), _f(r), large, sweep, _f(x2), _f(y2)),
              "none", sw, color, dash)


def _hatch(x0, y0, w, h, step=7, color="#b9b0a0"):
    """45-degree hatch inside a box, for a cut-away section."""
    o = []
    x = x0 - h
    while x < x0 + w:
        ax, ay = x, y0 + h
        bx, by = x + h, y0
        if ax < x0:
            ay -= (x0 - ax)
            ax = x0
        if bx > x0 + w:
            by += (bx - (x0 + w))
            bx = x0 + w
        if ax < bx and ay > by:
            o.append(_l(ax, ay, bx, by, 0.6, color))
        x += step
    return "".join(o)


def fig_10_8():
    """Servo accelerometer: the beam is torqued back to null, so the coil
    current — not the deflection — is the measure of acceleration."""
    b = []
    b.append(_r(72, 44, 200, 232, "none", 1.3))
    b.append(_r(80, 52, 184, 216, "none", 1.0))
    # ring magnet: the two hatched walls
    b.append(_r(80, 52, 15, 216, "#e7e1d2", 0.8, "#b3aa99"))
    b.append(_hatch(80, 52, 15, 216))
    b.append(_r(249, 52, 15, 216, "#e7e1d2", 0.8, "#b3aa99"))
    b.append(_hatch(249, 52, 15, 216))

    # the beam, hanging from a flexure hinge at its foot — free at the top, so it
    # is a cantilever and not a strut between two walls
    b.append(_r(176, 66, 8, 134, "#c9d3dd", 0.9, "#8d99a6"))
    b.append(_r(170, 108, 20, 46, "#c9d3dd", 0.9, "#8d99a6"))
    b.append(_l(180, 200, 180, 230, 1.6))
    b.append(_c(180, 234, 5, PAPER, 1.2))

    # deflection pickups, one each side of the beam
    for px in (134, 226):
        b.append(_c(px, 78, 11, PAPER, 1.0))
        b.append(_poly([(px - 4, 84), (px + 4, 84), (px, 72)], INK, 0.8, INK, True))

    # torque coils, sitting in the magnet gap
    for cx in (122, 238):
        for dy in (-10, 0, 10):
            b.append('<ellipse cx="%s" cy="%s" rx="12" ry="4.5" fill="none" stroke="%s" stroke-width="1"/>'
                     % (_f(cx), _f(178 + dy), INK))

    # pickup leads, over the top of the case, into the amplifier
    b.append(_p("M 123 78 L 123 34 L 357 34 L 357 150", "none", 0.9))
    b.append(_p("M 237 78 L 237 42 L 347 42 L 347 150", "none", 0.9))

    b.append(_r(322, 150, 70, 50, PAPER, 1.1))
    b.append(_t(357, 170, "khuếch đại", 7.4, "middle", "#222", True))
    b.append(_t(357, 182, "servo", 7.4, "middle", "#222", True))

    # restoring current fed back to the coil
    b.append(_arrow(330, 212, 252, 196, 1.0, RED, "4 3"))
    b.append(_t(292, 226, "dòng bù", 7.4, "middle", RED))

    # supplies and output
    b.append(_l(392, 162, 406, 162, 0.9))
    b.append(_c(408, 162, 2.6, PAPER, 0.9))
    b.append(_t(416, 165, "±15 V (DC)", 7.4, "start", "#444"))
    b.append(_l(392, 188, 406, 188, 0.9))
    b.append(_c(408, 188, 2.6, PAPER, 0.9))
    b.append(_t(416, 191, "đầu ra", 7.4, "start", "#444"))

    # input axis
    b.append(_arrow(140, 300, 220, 300, 1.0))
    b.append(_t(180, 316, "trục vào", 7.6, "middle", "#444"))

    # callouts
    b.append(_t(56, 62, "đầu dò độ lệch", 7.4, "end", "#444"))
    b.append(_l(60, 64, 122, 76, 0.7, "#999"))
    b.append(_t(56, 152, "nam châm", 7.4, "end", "#444"))
    b.append(_l(60, 152, 84, 156, 0.7, "#999"))
    b.append(_t(56, 232, "cuộn mô-men", 7.4, "end", "#444"))
    b.append(_l(60, 230, 108, 196, 0.7, "#999"))
    b.append(_t(158, 204, "chùm quán tính", 7.2, "start", "#444", False, -90))
    b.append(_t(196, 250, "bản lề uốn", 7.4, "start", "#444"))

    return _fig(svg(486, 328, STY + "".join(b), "Gia tốc kế kiểu servo"),
                "Hình 10-8. Gia tốc kế kiểu servo. Chùm quán tính được giữ ở vị trí không bằng "
                "mô-men do cuộn dây sinh ra, nên dòng điện bù tỉ lệ với gia tốc cần đo.",
                "Figure 10-8. Servo-type accelerometer. The beam is held at null by the torque "
                "the coil produces, so the restoring current is proportional to the acceleration.",
                "Sơ đồ cắt gia tốc kế kiểu servo: vỏ, nam châm vòng, chùm quán tính trên bản lề uốn, "
                "hai đầu dò độ lệch, hai cuộn mô-men và bộ khuếch đại servo.",
                "A cut-away schematic of a servo accelerometer: case, ring magnet, a beam on a flexure "
                "hinge, two deflection pickups, two torque coils and the servo amplifier.")


def fig_10_9():
    """Dielectric inclinometer: a bubble in an electrolyte bridges the outer
    electrodes and the common centre electrode."""
    b = []
    C = (190, 158)
    R = 112
    b.append(_c(C[0], C[1], R, "none", 1.4))
    b.append(_c(C[0], C[1], 92, "none", 1.0))
    for i in range(44):
        a = i * (360.0 / 44.0)
        ca, sa = math.cos(math.radians(a)), math.sin(math.radians(a))
        b.append(_l(C[0] + 92 * ca, C[1] - 92 * sa, C[0] + R * ca, C[1] - R * sa, 0.6, "#b9b0a0"))
    b.append(_c(C[0], C[1], 54, "none", 0.8, "#999"))

    for a in (90, 180, 270, 0):
        px = C[0] + 54 * math.cos(math.radians(a))
        py = C[1] - 54 * math.sin(math.radians(a))
        b.append(_c(px, py, 5.5, INK, 0.8, INK))
    b.append(_c(C[0], C[1], 6.5, INK, 0.8, INK))

    # the bubble, displaced from the centre by the tilt
    Bx, By = C[0] - 17, C[1] - 19
    b.append(_c(Bx, By, 8, PAPER, 1.2, BLUE))

    b.append(_t(52, 96, "bong bóng", 7.6, "start", "#444"))
    b.append(_l(104, 100, Bx - 7, By - 4, 0.7, "#999"))
    b.append(_t(300, 112, "điện cực ngoài", 7.6, "start", "#444"))
    b.append(_l(296, 116, C[0] + 58, C[1] - 4, 0.7, "#999"))
    b.append(_t(300, 196, "điện cực chung", 7.6, "start", "#444"))
    b.append(_l(296, 192, C[0] + 9, C[1] + 2, 0.7, "#999"))

    return _fig(svg(452, 300, STY + "".join(b), "Nghiêng kế kiểu điện môi"),
                "Hình 10-9. Nghiêng kế kiểu điện môi (nhìn chính diện). Bong bóng khí dịch khỏi "
                "tâm khi cảm biến nghiêng, làm thay đổi điện dung giữa các điện cực ngoài và "
                "điện cực chung.",
                "Figure 10-9. Dielectric-type inclinometer (front view). The bubble shifts away from "
                "the centre as the sensor tilts, changing the capacitance between the outer "
                "electrodes and the common electrode.",
                "Mặt cắt nghiêng kế kiểu điện môi: vỏ tròn có vành gạch, bốn điện cực ngoài trên "
                "vòng tròn nét đứt, điện cực chung ở tâm và bong bóng khí lệch khỏi tâm.",
                "A front view of a dielectric inclinometer: a round case with a hatched rim, four outer "
                "electrodes on a dashed circle, a common centre electrode and a gas bubble off centre.")


def fig_10_10():
    """Ship: O is where the rolling and pitching axes cross; A sits L above it."""
    b = []
    # hull, in side elevation
    b.append(_p("M 132 120 L 438 120 L 412 176 Q 300 198 180 176 Z", "#eef2f6", 1.2, INK))
    b.append(_l(132, 120, 438, 120, 1.6))
    # a deckhouse toward the bow
    b.append(_p("M 372 120 L 372 92 Q 400 84 424 96 L 424 120", PAPER, 1.1))

    O = (280, 148)
    A = (280, 120)
    b.append(_l(110, 148, 508, 148, 0.8, "#888", "6 4"))

    # heaving, offset left so it does not sit on the L dimension
    b.append(_arrow(250, 148, 250, 58, 1.1, GREEN))
    b.append(_t(250, 50, "nâng hạ", 7.8, "middle", GREEN, True))

    # rolling axis, fore and aft
    b.append(_arrow(300, 148, 512, 148, 1.1))
    b.append(_t(516, 145, "trục lăn", 7.8, "start", "#444"))
    b.append(_arc(470, 148, 15, -70, 70, RED, 1.3))
    b.append(_arrow(470 + 15 * math.cos(math.radians(70)), 148 - 15 * math.sin(math.radians(70)),
                    470 + 19 * math.cos(math.radians(88)), 148 - 19 * math.sin(math.radians(88)), 1.1, RED))

    # pitching axis, transverse, drawn in perspective
    b.append(_arrow(O[0], O[1], 352, 62, 1.1))
    b.append(_t(358, 56, "trục chòng chành", 7.8, "start", "#444"))
    # the pitch rotation, drawn clear of the hull below it
    b.append(_arc(200, 208, 15, 20, 150, RED, 1.3))
    b.append(_arrow(200 + 15 * math.cos(math.radians(150)), 208 - 15 * math.sin(math.radians(150)),
                    200 + 19 * math.cos(math.radians(168)), 208 - 19 * math.sin(math.radians(168)), 1.1, RED))
    b.append(_t(200, 234, "chòng chành", 7.4, "middle", RED))

    # the L dimension between O and A
    b.append(_l(280, 124, 280, 144, 1.0, BLUE))
    b.append(_l(276, 120, 284, 120, 1.0, BLUE))
    b.append(_l(276, 148, 284, 148, 1.0, BLUE))
    b.append(_t(292, 138, "L", 8.6, "start", BLUE, True))

    b.append(_dot(O[0], O[1], 3.2))
    b.append(_t(266, 164, "O", 8.6, "middle", INK, True))
    b.append(_dot(A[0], A[1], 3.2))
    b.append(_t(266, 116, "A", 8.6, "middle", INK, True))

    b.append(_t(132, 196, "đuôi", 7.6, "middle", "#444"))
    b.append(_t(444, 196, "mũi", 7.6, "middle", "#444"))
    b.append(_t(170, 112, "boong", 7.4, "start", "#444"))

    return _fig(svg(570, 240, STY + "".join(b), "Vị trí các cảm biến trên tàu"),
                "Hình 10-10. Vị trí các cảm biến. Hai nghiêng kế kiểu servo và một gia tốc kế kiểu "
                "servo đặt trên boong tại điểm A, cách giao điểm O của trục lăn và trục chòng chành "
                "một đoạn L.",
                "Figure 10-10. Location of sensors. Two servo inclinometers and one servo accelerometer "
                "sit on the deck at point A, a distance L from O, where the rolling and pitching axes "
                "cross.",
                "Hình chiếu cạnh tàu: trục lăn nằm ngang, trục chòng chành vẽ theo phối cảnh, mũi tên "
                "nâng hạ thẳng đứng, điểm O ở giao điểm và điểm A trên boong cách O một đoạn L.",
                "A ship in side elevation: the rolling axis runs fore and aft, the pitching axis is drawn "
                "in perspective, a heaving arrow points up, O marks the crossing and A sits L above it on deck.")


def fig_10_11():
    """Crane lifter: trolley on the rail, then two pendulum stages to the load."""
    b = []
    # rail with hatching above it
    b.append(_l(84, 54, 356, 54, 2.0))
    for x in range(88, 356, 9):
        b.append(_l(x, 54, x + 6, 44, 0.7, "#999"))

    # trolley sitting on the rail, with the hoist drum carried inside it
    b.append(_r(150, 54, 86, 32, PAPER, 1.1))
    b.append(_r(160, 60, 66, 18, "#f2efe6", 1.0))
    b.append(_c(166, 69, 6, PAPER, 1.0))
    b.append(_c(220, 69, 6, PAPER, 1.0))

    # hoist ropes, pulley, hook
    b.append(_l(170, 86, 170, 145, 1.0))
    b.append(_l(216, 86, 216, 145, 1.0))
    b.append(_c(193, 154, 11, PAPER, 1.1))
    b.append(_c(193, 154, 3, INK, 0.6, INK))
    b.append(_l(193, 165, 193, 178, 1.2))
    b.append(_p("M 193 178 q 9 0 9 7 q 0 6 -8 6", "none", 1.4))

    # primary pendulum, then the platform, then the secondary pendulum
    b.append(_l(193, 191, 160, 228, 1.3))
    b.append(_l(193, 191, 226, 228, 1.3))
    b.append(_r(152, 228, 82, 9, "#eef2f6", 1.0))
    b.append(_l(170, 237, 150, 288, 1.3))
    b.append(_l(216, 237, 236, 288, 1.3))

    # the coil being lifted
    b.append(_p("M 142 292 L 244 292 A 12 12 0 0 1 244 316 L 142 316 A 12 12 0 0 1 142 292 Z",
                "#e7e1d2", 1.2))

    # brace for the lifter frame
    b.append(_p("M 258 186 q 8 0 8 8 L 266 282 q 0 8 8 8", "none", 1.0, "#888"))

    b.append(_t(300, 38, "ray", 7.6, "start", "#444"))
    b.append(_t(146, 76, "trolley", 7.6, "end", "#444"))
    b.append(_t(240, 74, "drum", 7.4, "start", "#444"))
    b.append(_l(238, 72, 229, 69, 0.7, "#999"))
    b.append(_t(164, 120, "dây cáp", 7.4, "end", "#444"))
    b.append(_t(212, 152, "puli", 7.4, "start", "#444"))
    b.append(_t(210, 186, "móc", 7.4, "start", "#444"))
    b.append(_t(282, 240, "bộ nâng", 7.6, "start", "#444"))
    b.append(_t(193, 334, "cuộn dây (tải)", 7.6, "middle", "#444"))

    return _fig(svg(360, 348, STY + "".join(b), "Hệ cần cẩu nâng tải"),
                "Hình 10-11. Hệ cần cẩu nâng tải. Xe con chạy trên ray, tang cuốn cáp hạ puli, và "
                "bộ nâng hai tầng tạo thành hai con lắc nối tiếp mang cuộn dây.",
                "Figure 10-11. A crane lifter system. The trolley runs on the rail, the drum pays out "
                "the rope to the pulley, and the two-stage lifter forms two pendulums in series "
                "carrying the coil.",
                "Sơ đồ cần cẩu: ray, xe con, tang cuốn, hai sợi cáp, puli, móc, bộ nâng hai tầng và "
                "cuộn dây ở dưới cùng.",
                "A crane schematic: rail, trolley, drum, two ropes, pulley, hook, a two-stage lifter "
                "and the coil at the bottom.")


def fig_10_12():
    """Trolley lifter as two pendulums; theta1 at the trolley, theta2 at the pulley."""
    b = []
    O = (210, 96)
    P = (256, 210)
    L = (300, 316)

    b.append(_arrow(110, 96, 462, 96, 1.1))
    b.append(_t(474, 100, "x", 9.0, "middle", INK, True))
    b.append(_arrow(210, 96, 210, 40, 1.1))
    b.append(_t(210, 32, "y", 9.0, "middle", INK, True))
    b.append(_r(186, 76, 48, 20, "#eef2f6", 1.1))
    b.append(_l(210, 96, 210, 340, 0.8, "#aaa", "5 4"))

    # the rope and the lifter, drawn as the two pendulum links
    b.append(_l(210, 96, P[0], P[1], 1.4))
    b.append(_c(P[0], P[1], 10, PAPER, 1.1))
    b.append(_c(P[0], P[1], 3, INK, 0.6, INK))
    b.append(_l(P[0], P[1] + 10, P[0], P[1] + 22, 1.2))
    b.append(_p("M 256 232 q 8 0 8 6 q 0 5 -7 5", "none", 1.3))
    b.append(_l(P[0], P[1] + 34, L[0], L[1], 1.4))
    b.append(_r(L[0] - 13, L[1], 26, 28, "#e7e1d2", 1.1))

    # the two deflection angles, at different radii so they never merge
    b.append(_arc(O[0], O[1], 52, -90, -68, RED, 1.3))
    b.append(_t(218, 138, "θ₁", 8.4, "end", RED, True))
    b.append(_arc(P[0], P[1], 34, -90, -68, RED, 1.3))
    b.append(_t(272, 258, "θ₂", 8.4, "middle", RED, True))

    b.append(_dot(268, 262, 2.6))
    b.append(_t(256, 258, "G", 8.2, "end", INK, True))

    # the four segment labels all sit on the left of the wire, clear of it
    b.append(_t(228, 166, "ℓ", 8.6, "end", GREEN, True))
    b.append(_t(238, 196, "ℓ₁", 8.4, "end", GREEN, True))
    b.append(_t(264, 280, "ℓ₂", 8.4, "end", GREEN, True))
    b.append(_t(286, 308, "ℓ′₂", 8.4, "end", GREEN, True))

    b.append(_t(182, 68, "xe con", 7.4, "end", "#444"))
    b.append(_t(272, 202, "puli", 7.4, "start", "#444"))
    b.append(_t(272, 238, "móc", 7.4, "start", "#444"))
    b.append(_t(318, 296, "bộ nâng", 7.4, "start", "#444"))
    b.append(_t(318, 308, "(+ tải)", 7.4, "start", "#444"))
    b.append(_t(232, 116, "dây cáp", 7.4, "start", "#444"))

    return _fig(svg(490, 366, STY + "".join(b), "Động học hệ xe con và bộ nâng"),
                "Hình 10-12. Động học của hệ xe con – bộ nâng. Xe con chạy dọc trục x, dây cáp lệch "
                "góc θ₁ so với phương thẳng đứng, bộ nâng lệch tiếp góc θ₂ tại puli.",
                "Figure 10-12. Dynamics of a trolley lifter system. The trolley runs along x, the rope "
                "deflects by θ₁ from the vertical, and the lifter deflects a further θ₂ at the pulley.",
                "Hình phẳng: trục x nằm ngang, trục y thẳng đứng, xe con trên trục x, dây cáp lệch góc "
                "θ₁, bộ nâng treo dưới puli lệch góc θ₂, các đoạn ℓ, ℓ₁, ℓ₂, ℓ′₂ và điểm trọng tâm G.",
                "A planar diagram: x horizontal, y vertical, the trolley on x, the rope at θ₁, the lifter "
                "hanging from the pulley at θ₂, the segments ℓ, ℓ₁, ℓ₂, ℓ′₂ and the centre of gravity G.")


def fig_10_13():
    """Vertical gyro: the four directions and the three small angles between them."""
    b = []
    O = (200, 268)
    ang = {"lv": 100.0, "gyro": 90.0, "z": 78.0, "f": 72.0}

    def tip(a, r):
        return (O[0] + r * math.cos(math.radians(a)), O[1] - r * math.sin(math.radians(a)))

    # aircraft body at the origin, tilted with the roll
    b.append('<g transform="rotate(12 %s %s)">%s</g>'
             % (_f(O[0]), _f(O[1]), _r(O[0] - 34, O[1] - 6, 68, 12, "#eef2f6", 1.0)))

    b.append(_arrow(O[0], O[1], *tip(ang["lv"], 150), sw=1.1, color="#888", dash="5 4"))
    b.append(_t(166, 124, "phương thẳng đứng cục bộ", 7.4, "end", "#555"))
    b.append(_arrow(O[0], O[1], *tip(ang["gyro"], 190), sw=1.2, color=BLUE))
    b.append(_t(200, 70, "trục con quay", 7.4, "middle", BLUE, True))
    b.append(_arrow(O[0], O[1], *tip(ang["z"], 215), sw=1.2, color=GREEN))
    b.append(_t(254, 54, "trục Z máy bay", 7.4, "start", GREEN))
    b.append(_arrow(O[0], O[1], *tip(ang["f"], 245), sw=1.4, color=RED))
    b.append(_t(286, 32, "f (lực riêng)", 7.4, "start", RED))

    # components of f: f_v down the vertical, f_s across to it
    P = tip(ang["f"], 245)
    b.append(_l(P[0], P[1], O[0], P[1], 0.9, RED, "3 3"))
    b.append(_l(O[0], O[1], O[0], P[1], 0.9, RED, "3 3"))
    b.append(_t(203, 96, "f_v", 7.4, "start", RED))
    b.append(_t((O[0] + P[0]) / 2.0, P[1] - 6, "f_s", 7.4, "middle", RED))

    # the three error angles, each at its own radius
    b.append(_arc(O[0], O[1], 118, ang["z"], ang["lv"], RED, 1.2))
    b.append(_t(208, 140, "φ", 8.6, "start", RED, True))
    b.append(_arc(O[0], O[1], 146, ang["z"], ang["gyro"], BLUE, 1.2))
    b.append(_t(*tip(84, 158), s="φ_s", fs=8.2, anchor="middle", fill=BLUE, bold=True))
    b.append(_arc(O[0], O[1], 88, ang["f"], ang["gyro"], GREEN, 1.2))
    b.append(_t(*tip(81, 88), s="φ_B", fs=8.2, anchor="middle", fill=GREEN, bold=True))

    return _fig(svg(470, 320, STY + "".join(b), "Phân tích con quay thẳng đứng"),
                "Hình 10-13. Phân tích con quay thẳng đứng. Máy bay nghiêng góc φ so với phương thẳng "
                "đứng cục bộ; góc cảm nhận được là hiệu giữa góc nghiêng thực và sai lệch trôi φ_Δ, "
                "còn cảm biến lực riêng đo φ_B qua tỉ số f_s/f_v.",
                "Figure 10-13. Vertical gyro analysis. The aircraft rolls by φ from the local vertical; "
                "the sensed roll is the true roll less the drift error φ_Δ, and the specific-force "
                "sensor measures φ_B through the ratio f_s/f_v.",
                "Bốn mũi véc-tơ từ một gốc chung: phương thẳng đứng cục bộ, trục con quay, trục Z máy "
                "bay và lực riêng, kèm các góc φ, φ_s, φ_B và hai thành phần f_v, f_s.",
                "Four vectors from a common origin — local vertical, gyro axis, aircraft Z axis and the "
                "specific force — with the angles φ, φ_s, φ_B and the components f_v, f_s.")


def fig_10_14():
    """Two cones of constant angle about z, and the vectors that cut them."""
    b = []
    O = (235, 288)
    b.append(_arrow(O[0], O[1], O[0], 52, 1.1))
    b.append(_t(O[0], 44, "ẑ", 9.2, "middle", INK, True))
    b.append(_arrow(O[0], O[1], 432, O[1], 1.1))
    b.append(_t(444, O[1] + 4, "ŷ", 9.2, "middle", INK, True))
    b.append(_arrow(O[0], O[1], 148, 342, 1.1))
    b.append(_t(136, 350, "x̂", 9.2, "middle", INK, True))

    # outer and inner cones of constant angle about z
    for half, rx, ry in ((40.0, 126.0, 34.0), (17.0, 46.0, 13.0)):
        cy = 136.0
        b.append(_l(O[0], O[1], O[0] - rx, cy, 0.9, "#999"))
        b.append(_l(O[0], O[1], O[0] + rx, cy, 0.9, "#999"))
        b.append(_l(O[0], O[1], O[0], cy - ry, 0.7, "#bbb", "3 3"))
        b.append('<ellipse cx="%s" cy="%s" rx="%s" ry="%s" fill="none" stroke="%s" stroke-width="0.9"/>'
                 % (_f(O[0]), _f(cy), _f(rx), _f(ry), "#999"))

    def tip(a, r):
        return (O[0] + r * math.cos(math.radians(a)), O[1] - r * math.sin(math.radians(a)))

    b.append(_arrow(O[0], O[1], *tip(128, 152), sw=1.4, color=BLUE))
    b.append(_t(*tip(130, 166), s="S", fs=9.2, anchor="middle", fill=BLUE, bold=True))
    b.append(_arrow(O[0], O[1], *tip(52, 176), sw=1.4, color=GREEN))
    b.append(_t(*tip(50, 206), s="E", fs=9.2, anchor="middle", fill=GREEN, bold=True))
    b.append(_arrow(O[0], O[1], *tip(96, 122), sw=1.4, color=RED))
    b.append(_t(*tip(96, 136), s="A₁", fs=8.8, anchor="middle", fill=RED, bold=True))
    b.append(_arrow(O[0], O[1], *tip(88, 58), sw=1.4, color=RED))
    b.append(_t(248, 234, "A₂", 8.8, "start", RED, True))

    b.append(_arc(O[0], O[1], 72, 90, 128, BLUE, 1.2))
    b.append(_t(*tip(111, 84), s="β_S", fs=8.2, anchor="middle", fill=BLUE, bold=True))
    b.append(_arc(O[0], O[1], 104, 52, 90, GREEN, 1.2))
    b.append(_t(*tip(69, 118), s="Γ_N", fs=8.2, anchor="middle", fill=GREEN, bold=True))

    return _fig(svg(470, 360, STY + "".join(b), "Quan hệ giữa các véc-tơ chuẩn và nón thái độ"),
                "Hình 10-14. Quan hệ giữa các véc-tơ chuẩn và nón thái độ một trục. Mỗi nguồn chuẩn "
                "xác định một nón góc không đổi quanh trục ẑ; giao của hai nón cho hai nghiệm thái độ "
                "A₁ và A₂.",
                "Figure 10-14. Relationship between reference vectors and single-axis attitude cones. "
                "Each reference source defines a cone of constant angle about ẑ; where two cones cut "
                "each other there are two attitude solutions, A₁ and A₂.",
                "Hệ trục ẑ, ŷ, x̂ với hai nón góc không đổi quanh ẑ, các véc-tơ S và E cùng hai nghiệm "
                "A₁, A₂ và các góc β_S, Γ_N.",
                "The axes ẑ, ŷ, x̂ with two cones of constant angle about ẑ, the vectors S and E, the two "
                "solutions A₁ and A₂, and the angles β_S and Γ_N.")


def fig_10_15():
    """Trace averaging: the true solution is the dense knot, not the scattered tail."""
    def rnd(seed):
        s = [seed]

        def f():
            s[0] = (1103515245 * s[0] + 12345) % 2147483648
            return s[0] / 2147483648.0
        return f

    def band(d):
        return 168.0 - 0.74 * (d + 30.0)

    pts = []
    r = rnd(20251031)
    # the scattered, wrong solutions
    for i in range(22):
        d = -30.0 + 50.0 * i / 21.0
        pts.append((d + (r() - 0.5) * 2.0, band(d) + (r() - 0.5) * 4.0))
    # the knot of correct solutions
    for i in range(16):
        d = -14.0 + 8.0 * r()
        pts.append((d, band(d) + (r() - 0.5) * 1.6))

    frame, X, Y = _axes(96, 250, 306, 190, (-36, 36), (172, 128),
                        [(-30, "−30"), (-20, "−20"), (-10, "−10"), (0, "0"), (10, "10"), (20, "20"), (30, "30")],
                        [(170, "170"), (160, "160"), (150, "150"), (140, "140"), (130, "130")],
                        "độ lệch (độ)", "xích kinh (độ)", ylab_up=False)
    b = [frame]
    for d, ra in pts:
        b.append(_dot(X(d), Y(ra), 2.2, INK))

    b.append(_arrow(330, 200, 218, 176, 1.0, RED))
    b.append(_t(336, 204, "nghiệm đúng", 7.8, "start", RED, True))

    return _fig(svg(470, 306, STY + "".join(b), "Phương pháp lấy trung bình vết"),
                "Hình 10-15. Phương pháp lấy trung bình vết để phân giải nghiệm thái độ nhập nhằng. "
                "Nghiệm đúng tụ thành một cụm dày trên đồ thị xích kinh – độ lệch, còn nghiệm sai "
                "phân tán rộng.",
                "Figure 10-15. Method of trace averaging for resolving ambiguous attitude solutions. "
                "The correct solution forms a dense cluster on the right-ascension versus declination "
                "plot; the incorrect one is scattered much more widely.",
                "Đồ thị phân tán xích kinh theo độ lệch, trục tung đảo ngược, một cụm điểm dày ở giữa "
                "và nhiều điểm phân tán, kèm mũi tên chỉ cụm nghiệm đúng.",
                "A scatter plot of right ascension against declination with an inverted vertical axis, "
                "one dense cluster in the middle, scattered outliers, and an arrow marking the correct cluster.")


def fig_10_16():
    """Panoramic annular lens: a 360-degree ring of directions folded onto a plane."""
    b = []
    C = (300, 160)
    b.append(_l(70, 160, 462, 160, 0.8, "#888", "6 4"))
    b.append(_t(74, 152, "trục quang", 7.6, "start", "#555"))

    # the lens body, a section through the annular element
    b.append(_p("M 300 96 C 348 96 372 126 372 160 C 372 194 348 224 300 224 Z", "#eef2f6", 1.2))
    b.append(_p("M 300 96 C 286 96 278 126 278 160 C 278 194 286 224 300 224", "none", 1.0, "#8d99a6"))

    # the mirrored annular surface
    b.append(_p("M 306 116 A 48 48 0 0 1 306 204", "none", 2.6, GOLD))

    # field of view, hatched, opening to the left
    b.append(_p("M %s %s L 118 96 L 118 224 Z" % (_f(C[0]), _f(C[1])), "#f7f4ed", 0.8, "#c9c0aa"))
    for y in range(99, 224, 7):
        xr = 118 + ((y - 96) if y <= 160 else (224 - y)) * 2.844
        if xr > 126:
            b.append(_l(120, y, min(xr, C[0] - 3), y, 0.5, "#c9c0aa"))
    b.append(_t(100, 84, "trường nhìn", 7.6, "start", "#555", True))

    # rays: in at the rim, folded at the mirrored surface, out to the image plane
    for y0, y1 in ((118, 176), (202, 144)):
        ym = 160 + (y0 - 160) * 0.30
        b.append(_l(122, y0, 333, ym, 0.9, BLUE))
        b.append(_l(333, ym, 398, y1, 0.9, BLUE))

    # the image plane
    b.append(_r(398, 132, 7, 58, PAPER, 1.1))
    b.append(_t(412, 128, "mặt phẳng ảnh PAL", 7.6, "start", "#444"))

    return _fig(svg(486, 250, STY + "".join(b), "Sơ đồ tia của thấu kính vòng toàn cảnh"),
                "Hình 10-16. Sơ đồ tia của thấu kính vòng toàn cảnh (PAL). Thấu kính một khối chiết "
                "suất cao, mặt ngoài tráng gương, gấp trường nhìn vành khuyên 65°–110° quanh trục "
                "quang thành ảnh phẳng.",
                "Figure 10-16. Panoramic annular lens ray diagram. A single high-index element with a "
                "mirrored annular surface folds the 65°–110° ring of directions about the optical axis "
                "onto a flat image plane.",
                "Sơ đồ tia: trường nhìn vành khuyên gạch chéo bên trái, thấu kính một khối có mặt "
                "gương cung vàng, trục quang nằm ngang và mặt phẳng ảnh ở bên phải.",
                "A ray diagram: the hatched annular field of view on the left, a single-element lens with "
                "a gold mirrored arc, the horizontal optical axis and the image plane on the right.")


# ---------------------------------------------------------------- 10.3
def _hexa(cx, cy, w, h, fill=PAPER):
    """Hexagon, the block-diagram symbol for a disturbance."""
    hw, hh = w / 2.0, h / 2.0
    pts = [(cx - hw + 10, cy - hh), (cx + hw - 10, cy - hh), (cx + hw, cy),
           (cx + hw - 10, cy + hh), (cx - hw + 10, cy + hh), (cx - hw, cy)]
    return _poly(pts, fill, 1.1, INK, close=True)


def _iso(x, y, w, d, h, ft=PAPER, fl=BAND, fr=SAND):
    """Isometric box standing on (x, y) — the front-bottom vertex. w runs up-right,
    d runs up-left, h is the height, so the box rises from y."""
    ax, ay = 0.866, 0.5

    def P(u, v, z):
        return (x + (u - v) * ax, y - (u + v) * ay - z)

    p0, p1, p2, p3 = P(0, 0, 0), P(w, 0, 0), P(w, d, 0), P(0, d, 0)
    t0, t1, t2, t3 = P(0, 0, h), P(w, 0, h), P(w, d, h), P(0, d, h)
    o = [_poly([p0, p1, t1, t0], fr, 0.9), _poly([p0, p3, t3, t0], fl, 0.9),
         _poly([t0, t1, t2, t3], ft, 0.9)]
    return "".join(o)


def _box(x, y, w, h, label, fs=7.4, fill=PAPER, lines=None):
    """A plain labelled block."""
    o = [_r(x, y, w, h, fill, 1.1)]
    rows = lines or [label]
    n = len(rows)
    for i, s in enumerate(rows):
        o.append(_t(x + w / 2.0, y + h / 2.0 + (i - (n - 1) / 2.0) * 11 + 3, s, fs, "middle", "#222",
                    i == 0))
    return "".join(o)


def fig_10_17():
    """Body axes of an aircraft: roll about the fuselage, pitch about the wing,
    yaw about the vertical."""
    b = []
    # plan silhouette, nose to the left
    b.append(_poly([(150, 170), (205, 160), (300, 157), (340, 163), (340, 179),
                    (300, 186), (205, 180), (150, 176)], "#eef2f6", 1.1, close=True))
    b.append(_poly([(235, 163), (203, 112), (241, 115), (286, 160)], BAND, 1.0, close=True))
    b.append(_poly([(235, 182), (203, 232), (241, 229), (286, 184)], BAND, 1.0, close=True))
    b.append(_poly([(316, 160), (330, 138), (343, 142), (333, 164)], SAND, 1.0, close=True))
    b.append(_poly([(316, 180), (330, 202), (343, 198), (333, 176)], SAND, 1.0, close=True))

    O = (245, 171)
    b.append(_arrow(O[0], O[1], 118, 171, 1.2))
    b.append(_t(110, 175, "Y", 9.2, "middle", INK, True))
    b.append(_arrow(O[0], O[1], 402, 216, 1.2))
    b.append(_t(412, 222, "X", 9.2, "middle", INK, True))
    b.append(_arrow(O[0], O[1], 245, 292, 1.2))
    b.append(_t(245, 304, "Z", 9.2, "middle", INK, True))

    b.append(_t(200, 148, "U", 8.6, "middle", GREEN, True))
    b.append(_t(232, 242, "W", 8.6, "middle", GREEN, True))

    # the three rotation rates
    b.append(_p("M 172 148 A 7 22 0 0 1 172 194", "none", 1.3, RED))
    b.append(_arrow(172, 150, 168, 145, 1.1, RED))
    b.append(_t(166, 140, "P", 8.4, "middle", RED, True))
    b.append(_t(160, 210, "lăn", 7.6, "middle", RED))

    b.append('<ellipse cx="352" cy="196" rx="22" ry="7" fill="none" stroke="%s" stroke-width="1.3" '
             'transform="rotate(30 352 196)"/>' % RED)
    b.append(_arrow(338, 186, 334, 180, 1.1, RED))
    b.append(_t(370, 180, "Q", 8.4, "middle", RED, True))
    b.append(_t(382, 206, "chúc", 7.6, "start", RED))

    b.append('<ellipse cx="245" cy="256" rx="22" ry="7" fill="none" stroke="%s" stroke-width="1.3"/>' % RED)
    b.append(_arrow(223, 256, 219, 252, 1.1, RED))
    b.append(_t(258, 274, "R", 8.4, "middle", RED, True))
    b.append(_t(286, 258, "hướng", 7.6, "start", RED))

    return _fig(svg(470, 318, STY + "".join(b), "Các trục thân máy bay"),
                "Hình 10-17. Trong dẫn đường quán tính, chuyển động của xe, tên lửa, tàu thuỷ, máy bay, "
                "rô-bốt… được theo dõi so với một hệ trục quy chiếu. Trên mặt đất, hệ quy chiếu quy ước "
                "là các trục cố định của Trái Đất — Bắc, Đông và Hướng xuống. Một phương tiện như máy "
                "bay hay tàu biển có các trục cục bộ riêng, gọi là lăn, chúc và hướng.",
                "Figure 10-17. In inertial navigation, the movement of a vehicle, rocket, ship, aircraft "
                "or robot is monitored with respect to a reference frame. On the Earth's surface the "
                "conventional frame is the Earth's fixed axes — North, East and Down. A vehicle has its "
                "own local axes, known as roll, pitch and yaw.",
                "Hình chiếu bằng máy bay với ba trục X, Y, Z, các thành phần U và W, và ba mũi tên quay "
                "lăn P, chúc Q, hướng R.",
                "A plan view of an aircraft with the X, Y and Z axes, the U and W components, and three "
                "rotation arrows for roll P, pitch Q and yaw R.")


def fig_10_18():
    """Navigational platform: gyros null the gimbals, the computer integrates."""
    b = []
    for i, nm in enumerate(("Gyro X", "Gyro Y", "Gyro Z")):
        b.append(_box(50, 56 + i * 30, 70, 20, nm, 7.2))
    b.append(_l(120, 66, 132, 66, 0.9))
    b.append(_l(120, 96, 132, 96, 0.9))
    b.append(_l(120, 126, 132, 126, 0.9))
    b.append(_l(132, 66, 132, 126, 0.9))
    b.append(_l(132, 96, 200, 96, 0.9))
    b.append(_t(150, 90, "vòng không", 7.4, "start", "#444", True))
    b.append(_arrow(200, 96, 200, 148, 0.9))

    # gimbal assembly
    b.append(_r(160, 150, 150, 146, PAPER, 1.1))
    b.append(_c(235, 223, 56, "none", 1.2))
    b.append('<ellipse cx="235" cy="223" rx="42" ry="52" fill="none" stroke="%s" stroke-width="1"/>' % "#8d99a6")
    b.append(_c(235, 223, 22, "#e7e1d2", 1.0))
    b.append(_l(235, 150, 235, 168, 1.0))
    b.append(_l(235, 278, 235, 296, 1.0))
    b.append(_t(330, 142, "các gimbal", 7.4, "start", "#444"))
    b.append(_l(326, 146, 282, 176, 0.7, "#999"))

    b.append(_box(400, 180, 130, 108, "", 7.4))
    b.append(_t(465, 202, "MÁY TÍNH", 7.6, "middle", "#222", True))
    b.append(_t(465, 214, "DẪN ĐƯỜNG", 7.6, "middle", "#222", True))
    for i, s in enumerate(("tích phân", "hiệu chỉnh", "(Coriolis)", "(trọng lực)")):
        b.append(_t(465, 232 + i * 12, s, 7.2, "middle", "#444"))

    b.append(_arrow(310, 214, 400, 214, 1.0))
    b.append(_t(355, 206, "vị trí, tốc độ, thái độ", 7.2, "middle", "#444"))
    b.append(_t(355, 234, "góc gimbal (synchro)", 7.2, "middle", "#444"))
    b.append(_arrow(400, 262, 310, 262, 1.0))
    b.append(_t(355, 276, "mô-men bù", 7.2, "middle", RED))

    # accelerometers
    for i, nm in enumerate(("Accel X", "Accel Y", "Accel Z")):
        b.append(_box(50, 300 + i * 28, 70, 20, nm, 7.2))
    b.append(_l(120, 310, 132, 310, 0.9))
    b.append(_l(120, 338, 132, 338, 0.9))
    b.append(_l(120, 366, 132, 366, 0.9))
    b.append(_l(132, 310, 132, 366, 0.9))
    b.append(_l(132, 338, 465, 338, 0.9))
    b.append(_arrow(465, 338, 465, 288, 0.9))
    b.append(_t(240, 332, "gia tốc", 7.4, "start", "#444", True))

    # fixed axes
    b.append(_arrow(96, 396, 60, 396, 1.0))
    b.append(_arrow(524, 396, 560, 396, 1.0))
    b.append(_t(310, 400, "TRỤC CỐ ĐỊNH", 7.4, "middle", "#444", True))

    return _fig(svg(620, 414, STY + "".join(b), "Sơ đồ khối hệ dẫn đường dùng bệ"),
                "Hình 10-18. Một số hệ dẫn đường quán tính (INS) dựa trên bệ dẫn đường. Các cảm biến "
                "quán tính được gắn sao cho chúng luôn nằm ngang và hướng theo một phương cố định. Hệ "
                "dùng một bộ gimbal và các cảm biến gắn trên ba trục x, y, z để theo dõi liên tục góc "
                "và gia tốc. Máy tính dẫn đường hiệu chỉnh các ảnh hưởng Coriolis, trọng lực và các "
                "hiệu ứng khác.",
                "Figure 10-18. Some inertial navigation systems are based on a navigational platform. "
                "The inertial sensors are mounted so that they stay level and point in a fixed "
                "direction. A set of gimbals and sensors on the x, y and z axes monitors the angles and "
                "accelerations constantly, and the navigation computer corrects for Coriolis, gravity "
                "and other effects.",
                "Sơ đồ khối: ba con quay qua vòng không vào cụm gimbal, máy tính dẫn đường nhận vị trí, "
                "tốc độ, thái độ và trả mô-men bù về gimbal; ba gia tốc kế cấp tín hiệu gia tốc.",
                "A block diagram: three gyros close null loops around the gimbal assembly, the navigation "
                "computer takes position, speed and attitude and returns torquing signals, and three "
                "accelerometers feed acceleration.")


def fig_10_19():
    """Strapdown: the same sensors, bolted to the frame, no gimbals."""
    b = []
    b.append('<ellipse cx="290" cy="292" rx="188" ry="44" fill="#f2efe6" stroke="%s" stroke-width="1.2"/>'
             % INK)
    for i in range(28):
        a = math.pi * 2 * i / 28.0
        b.append(_l(290 + 188 * math.cos(a), 292 + 44 * math.sin(a),
                    290 + 178 * math.cos(a), 292 + 40 * math.sin(a), 0.6, "#b9b0a0"))

    # back to front: the computer bay, two sensor blocks, then the front pair
    b.append(_iso(348, 236, 50, 50, 70))
    b.append(_iso(206, 256, 50, 50, 44))
    b.append(_iso(286, 256, 50, 50, 44))
    b.append(_iso(166, 310, 50, 50, 44))
    b.append(_iso(246, 310, 50, 50, 44))

    # sensing axes, drawn up the front faces
    b.append(_arrow(191, 306, 191, 274, 2.6))
    b.append(_arrow(271, 306, 271, 274, 2.6))
    b.append(_arrow(231, 252, 231, 220, 2.6))
    b.append(_arrow(311, 252, 311, 220, 2.6))

    b.append(_t(166, 328, "Gyro Y", 7.4, "middle", "#222", True))
    b.append(_t(246, 328, "Accel Y", 7.4, "middle", "#222", True))
    b.append(_t(178, 250, "Gyro X", 7.4, "end", "#222", True))
    b.append(_t(316, 250, "Accel X", 7.4, "start", "#222", True))
    b.append(_t(396, 226, "Gyro Z", 7.4, "start", "#222", True))
    b.append(_t(436, 140, "máy tính và", 7.4, "start", "#444", True))
    b.append(_t(436, 152, "xử lý tín hiệu", 7.4, "start", "#444"))
    b.append(_l(432, 146, 380, 168, 0.7, "#999"))

    return _fig(svg(560, 346, STY + "".join(b), "Hệ gắn cứng trên thân"),
                "Hình 10-19. Hệ gắn cứng (strapdown) loại bỏ nhu cầu về gimbal. Con quay và gia tốc kế "
                "được gắn chặt lên kết cấu phương tiện, và các phép đo quy về trục cục bộ lăn, chúc, "
                "hướng. Con quay đo chuyển động góc trên ba trục trong những khoảng thời gian ngắn để "
                "máy tính xử lý; kết hợp với đầu ra của gia tốc kế, máy tính dựng lại các trục dẫn đường.",
                "Figure 10-19. A strapdown system needs no gimbals. The gyros and accelerometers are "
                "mounted rigidly on the vehicle structure, and the measurements are referred to the local "
                "roll, pitch and yaw axes. The gyros measure angular motion in the three axes over short "
                "intervals; together with the accelerometer outputs the computer resolves the navigation axes.",
                "Khối cảm biến ba chiều gồm các hộp Gyro X, Gyro Y, Gyro Z và Accel X, Accel Y, Accel Z "
                "gắn cứng trên một đế tròn, kèm các mũi tên chỉ trục cảm nhận.",
                "A three-dimensional sensor cluster of Gyro X, Gyro Y, Gyro Z and Accel X, Accel Y, Accel Z "
                "boxes bolted to a round base, with thick arrows marking the sensing axes.")


def fig_10_20():
    """Gyroscope: torque orthogonal to the spin axis turns the axis, not the speed."""
    b = []
    C = (312, 212)
    b.append(_c(C[0], C[1], 52, "#f2efe6", 1.3))
    b.append(_p("M %s %s A 52 52 0 0 1 %s %s" % (_f(C[0] - 20), _f(C[1] - 48),
                                                 _f(C[0] + 20), _f(C[1] - 48)), "none", 2.2, "#8d99a6"))
    b.append(_t(C[0] - 6, C[1] + 4, "ω", 9.4, "middle", INK, True))

    # spin axis and angular momentum
    b.append(_arrow(C[0], C[1], 176, C[1], 1.3))
    b.append(_t(166, C[1] + 6, "H", 9.4, "middle", INK, True))
    b.append(_t(238, C[1] - 10, "H = Iω", 8.4, "middle", "#444"))
    b.append(_t(238, C[1] + 24, "trục quay", 7.6, "middle", "#444"))

    # dH at a small angle to H
    b.append(_arrow(176, C[1], 150, 182, 1.2, BLUE))
    b.append(_t(140, 176, "dH", 8.2, "middle", BLUE, True))
    b.append(_arc(176, C[1], 36, 180, 132, BLUE, 1.2))
    b.append(_t(148, 206, "dθ", 8.0, "middle", BLUE, True))

    # output and input axes
    b.append(_arrow(C[0], C[1], C[0], 104, 1.3))
    b.append(_t(C[0] - 10, 92, "Ω", 9.4, "middle", INK, True))
    b.append(_t(C[0] + 10, 100, "trục ra (tiến động)", 7.6, "start", "#444"))

    b.append(_arrow(C[0], C[1], 396, 274, 1.3))
    b.append(_t(402, 282, "T", 9.4, "start", INK, True))
    b.append(_t(406, 266, "trục vào (mô-men)", 7.6, "start", "#444"))

    b.append(_t(400, 196, "chiều quay", 7.6, "start", "#444"))
    b.append(_t(400, 208, "bánh đà", 7.6, "start", "#444"))
    b.append(_arc(C[0], C[1], 40, -74, -12, "#444", 1.3))
    b.append(_arrow(343, 213, 351, 204, 1.2, "#444"))

    return _fig(svg(520, 300, STY + "".join(b), "Nguyên lý con quay"),
                "Hình 10-20. Nguyên lý hoạt động của con quay dựa trên động lượng góc của một vật quay "
                "được chế tạo cẩn thận. Động lượng góc giữ ổn định hệ thống: nó không đổi trừ khi có "
                "mô-men tác dụng. Nếu mô-men vuông góc với trục quay, nó không đổi được độ lớn của vận "
                "tốc góc nhưng đổi được hướng của vận tốc góc, theo cùng chiều với mô-men.",
                "Figure 10-20. A gyroscope works on the angular momentum of a carefully built rotating "
                "body. The angular momentum stabilises the system: it stays unchanged unless a torque "
                "acts. A torque orthogonal to the spin axis cannot change the magnitude of the angular "
                "velocity, but it does change its direction, in the same sense as the torque.",
                "Bánh đà quay với vận tốc góc omega, véc-tơ động lượng góc H dọc trục quay, véc-tơ dH "
                "lệch góc dθ, trục ra tiến động Ω và trục vào mô-men T.",
                "A spinning wheel with angular velocity omega, the angular momentum H along the spin axis, "
                "the increment dH at angle dθ, the precession output axis Ω and the torque input axis T.")


def fig_10_21():
    """Two-axis flywheel gyro: rotor, inner gimbal, outer gimbal, outer pivot."""
    b = []
    C = (250, 196)
    b.append('<ellipse cx="%s" cy="%s" rx="78" ry="96" fill="none" stroke="%s" stroke-width="1.5"/>'
             % (_f(C[0]), _f(C[1]), INK))
    b.append('<ellipse cx="%s" cy="%s" rx="58" ry="72" fill="none" stroke="%s" stroke-width="1.3"/>'
             % (_f(C[0]), _f(C[1]), "#8d99a6"))
    b.append('<defs><clipPath id="rot21"><circle cx="214" cy="168" r="27"/></clipPath></defs>')
    b.append(_c(214, 168, 27, "#ded7c6", 1.2))
    b.append('<g clip-path="url(#rot21)">%s</g>' % _hatch(187, 141, 54, 54, 6, "#b9b0a0"))
    b.append(_c(214, 168, 27, "none", 1.2))
    b.append(_l(178, 126, 252, 212, 1.0))
    b.append(_l(C[0], 100, C[0], 74, 1.6))
    b.append(_l(C[0], 292, C[0], 318, 1.6))

    b.append(_t(160, 120, "trục quay", 7.6, "end", "#444"))
    b.append(_l(164, 124, 196, 142, 0.7, "#999"))
    b.append(_t(120, 210, "khối quay", 7.6, "end", "#444"))
    b.append(_l(124, 208, 186, 182, 0.7, "#999"))
    b.append(_t(340, 176, "gimbal trong", 7.6, "start", "#444"))
    b.append(_l(336, 180, 296, 190, 0.7, "#999"))
    b.append(_t(340, 258, "gimbal ngoài", 7.6, "start", "#444"))
    b.append(_l(336, 254, 314, 232, 0.7, "#999"))
    b.append(_t(250, 334, "trục ngoài", 7.6, "middle", "#444"))

    return _fig(svg(470, 346, STY + "".join(b), "Con quay bánh đà hai trục"),
                "Hình 10-21. Trong con quay bánh đà hai trục, rô-to quay bằng động cơ điện được treo "
                "trên một cặp ổ trục chính xác ma sát thấp ở hai đầu trục rô-to. Các ổ này tựa trên một "
                "vành gimbal trong hình vành khuyên; vành trong quay trên bộ ổ thứ hai gắn vào vành "
                "gimbal ngoài. Vành ngoài gắn vào khung thiết bị bằng bộ ổ thứ ba xác định trục thẳng "
                "đứng. Cách treo này luôn bảo toàn hướng trục quay đã định trước trong không gian quán tính.",
                "Figure 10-21. In a two-axis flywheel gyro an electrically driven rotor is suspended in a "
                "pair of precision low-friction bearings at the ends of the rotor axle. Those bearings are "
                "carried by a circular inner gimbal ring, which turns on a second set of bearings attached "
                "to the outer gimbal ring. The outer ring is attached to the instrument frame by a third "
                "set of bearings that defines the vertical axis. The suspension always preserves the "
                "predetermined spin-axis direction in inertial space.",
                "Hai vành gimbal lồng nhau, khối rô-to gạch chéo ở phía trên bên trái, đường trục quay "
                "xiên và hai trục ngoài ở trên và dưới.",
                "Two nested gimbal rings, the hatched rotor mass at the upper left, the slanted spin axis "
                "and the two outer pivots above and below.")


def fig_10_22():
    """Fibre-optic gyro: the Sagnac ring, its coupler, and the rate output."""
    b = []
    b.append(_t(58, 122, "nguồn", 7.6, "start", "#444"))
    b.append(_r(96, 110, 20, 20, "#ded7c6", 1.0))
    b.append(_hatch(96, 110, 20, 20, 5, "#b9b0a0"))
    b.append(_t(106, 100, "đi-ốt", 7.4, "middle", "#444"))
    b.append(_l(116, 120, 138, 120, 0.9))
    b.append(_c(146, 120, 7, PAPER, 1.0))
    b.append(_c(159, 120, 7, PAPER, 1.0))
    b.append(_t(152, 142, "PC", 7.4, "middle", "#444"))
    b.append(_l(166, 120, 196, 120, 0.9))

    # coupler
    b.append(_poly([(196, 110), (216, 110), (206, 124)], PAPER, 1.0, close=True))
    b.append(_poly([(196, 130), (216, 130), (206, 118)], PAPER, 1.0, close=True))
    b.append(_t(206, 150, "bộ ghép", 7.4, "middle", "#444"))
    b.append(_r(196, 82, 22, 12, "#ded7c6", 1.0))
    b.append(_t(207, 76, "kính phân cực", 7.4, "middle", "#444"))
    b.append(_l(216, 120, 288, 120, 0.9))
    b.append(_c(296, 120, 7, PAPER, 1.0))
    b.append(_c(309, 120, 7, PAPER, 1.0))
    b.append(_t(302, 100, "điều khiển phân cực", 7.4, "middle", "#444"))
    b.append(_l(316, 120, 400, 152, 0.9))

    # the sensing coil
    CX, CY = 470, 206
    for r in (42, 49, 56, 63):
        b.append(_c(CX, CY, r, "none", 0.9, "#8d99a6"))
    b.append(_t(CX, 124, "cuộn sợi quang", 7.4, "middle", "#222", True))
    b.append(_t(CX, 136, "100 – 1000 m", 7.4, "middle", "#444"))
    b.append(_t(398, 178, "t⁺", 7.6, "middle", BLUE, True))
    b.append(_t(542, 178, "t⁻", 7.6, "middle", BLUE, True))
    b.append(_arrow(CX, CY, CX + 63, CY, 0.9))
    b.append(_t(CX + 34, CY - 6, "R", 8.2, "middle", INK, True))
    b.append(_arc(CX, CY, 76, -64, -22, RED, 1.1))
    b.append(_t(CX + 52, CY + 60, "Ω", 9.0, "middle", RED, True))

    # detector and rate output
    b.append(_l(206, 130, 206, 214, 0.9))
    b.append(_r(180, 214, 20, 20, "#ded7c6", 1.0))
    b.append(_hatch(180, 214, 20, 20, 5, "#b9b0a0"))
    b.append(_t(160, 220, "đầu thu", 7.4, "end", "#444"))
    b.append(_l(200, 224, 240, 224, 0.9))
    b.append(_box(240, 208, 78, 32, "", 7.2))
    b.append(_t(279, 221, "khuếch đại", 7.2, "middle", "#222", True))
    b.append(_t(279, 233, "khoá pha", 7.2, "middle", "#222", True))
    b.append(_arrow(318, 224, 396, 224, 1.0))
    b.append(_t(324, 216, "ra tốc độ (analogue)", 7.2, "start", "#444"))

    # bias coil and oscillator
    for i in range(5):
        b.append('<ellipse cx="430" cy="%s" rx="18" ry="5" fill="none" stroke="%s" stroke-width="1"/>'
                 % (_f(296 + i * 11), INK))
    b.append(_t(430, 288, "cuộn thiên áp", 7.2, "middle", "#444"))
    b.append(_box(280, 352, 78, 24, "dao động", 7.2))
    b.append(_l(358, 364, 430, 364, 0.9))
    b.append(_arrow(430, 364, 430, 342, 0.9))
    b.append(_l(300, 352, 300, 240, 0.9))
    b.append(_arrow(300, 246, 300, 240, 0.9))

    return _fig(svg(620, 386, STY + "".join(b), "Sơ đồ con quay sợi quang"),
                "Hình 10-22. Một con quay sợi quang điển hình. Nó dựa trên tính chất quán tính của ánh "
                "sáng, cụ thể là hiệu ứng Sagnac: hiệu ứng này làm dịch pha các vân giao thoa theo tốc "
                "độ quay. Hai sóng ánh sáng lan truyền ngược chiều nhau quanh một vòng bán kính R, cùng "
                "khởi phát từ nguồn. Khi con quay đứng yên, hai sóng tới đầu thu cùng lúc và không ghi "
                "nhận lệch pha nào. Khi vòng quay, sóng truyền ngược chiều quay trở về sớm hơn sóng "
                "truyền cùng chiều.",
                "Figure 10-22. A typical fibre-optic gyroscope, based on the inertial properties of light "
                "— the Sagnac effect, which shifts the interference fringes according to rotation rate. "
                "Two light waves circulate in opposite directions around a loop of radius R, starting "
                "from the same source. With the gyro at rest the two arrive together and no phase "
                "difference is recorded; when the loop rotates, the wave travelling against the rotation "
                "returns sooner than the one travelling with it.",
                "Sơ đồ quang: nguồn, đi-ốt, bộ điều khiển phân cực, bộ ghép có kính phân cực, cuộn sợi "
                "quang bán kính R quay với tốc độ Ω, đầu thu, khuếch đại khoá pha, cuộn thiên áp và dao động.",
                "An optical schematic: source, diode, polarisation controllers, a coupler with a polariser, "
                "the fibre coil of radius R rotating at Ω, a detector, a lock-in amplifier, a bias coil and "
                "an oscillator.")


def fig_10_23():
    """Micromachined accelerometers: a wafer of them, one of them magnified."""
    b = []
    b.append(_c(268, 196, 108, "none", 1.3))
    x0, y0, cell, n = 193, 121, 30, 5
    for i in range(n + 1):
        b.append(_l(x0 + i * cell, y0, x0 + i * cell, y0 + n * cell, 0.7, "#8d99a6"))
        b.append(_l(x0, y0 + i * cell, x0 + n * cell, y0 + i * cell, 0.7, "#8d99a6"))
    for i in range(n):
        for j in range(n):
            cx, cy = x0 + (i + 0.5) * cell, y0 + (j + 0.5) * cell
            b.append(_r(cx - 9, cy - 4, 18, 8, PAPER, 0.8, "#555"))
            for k in range(3):
                b.append(_l(cx - 6 + k * 4, cy - 4, cx - 6 + k * 4, cy + 4, 0.6, "#555"))

    b.append(_c(452, 216, 40, PAPER, 1.2))
    b.append(_r(434, 208, 36, 16, PAPER, 1.0, "#555"))
    for k in range(4):
        b.append(_l(438 + k * 8, 208, 438 + k * 8, 224, 0.9, "#555"))
    b.append(_l(340, 158, 414, 200, 0.8, "#999"))
    b.append(_l(340, 196, 414, 224, 0.8, "#999"))

    b.append(_t(352, 100, "phiến silic", 7.6, "start", "#444"))
    b.append(_l(348, 104, 316, 122, 0.7, "#999"))
    b.append(_t(268, 348, "đường cắt", 7.6, "middle", "#444"))
    b.append(_l(268, 338, 268, 272, 0.7, "#999"))
    b.append(_t(508, 268, "một gia tốc kế", 7.6, "start", "#444"))
    b.append(_t(508, 280, "riêng lẻ", 7.6, "start", "#444"))

    return _fig(svg(600, 366, STY + "".join(b), "Gia tốc kế vi cơ"),
                "Hình 10-23. Ví dụ điển hình về một gia tốc kế vi cơ hiện đại. Nhiều gia tốc kế có thể "
                "được gắn trên cùng một phiến, cảm nhận gia tốc theo các hướng x, y và z. Phần xử lý tín "
                "hiệu sơ cấp cũng nằm ngay trên cùng phiến, và đầu ra thường ở dạng số.",
                "Figure 10-23. A typical modern micromachined accelerometer. Many accelerometers can be "
                "mounted on one chip, sensing acceleration in the x, y and z directions. The primary "
                "signal conditioning sits on the same chip, and the output is usually digital.",
                "Phiến silic tròn chia thành lưới ô vuông, mỗi ô chứa một cảm biến lược, và một ô được "
                "phóng to ở bên phải.",
                "A round silicon wafer divided into a grid of square cells, each holding a comb transducer, "
                "with one cell magnified at the right.")


def fig_10_24():
    """Stabilisation loop: a gyro senses dip, the torquer drives it back to null."""
    b = []
    b.append(_arrow(66, 92, 116, 92, 1.0))
    b.append(_c(128, 92, 12, PAPER, 1.2))
    b.append(_t(121, 86, "+", 9.0, "middle", "#222", True))
    b.append(_t(121, 106, "+", 9.0, "middle", "#222", True))
    b.append(_arrow(140, 92, 276, 92, 1.0))
    b.append(_box(276, 70, 74, 44, "bệ", 7.6))
    b.append(_arrow(350, 92, 540, 92, 1.0))
    b.append(_l(540, 92, 540, 196, 1.0))
    b.append(_t(534, 132, "góc nghiêng của bệ", 7.4, "end", "#444"))
    b.append(_arrow(540, 196, 512, 196, 1.0))
    b.append(_box(412, 176, 100, 40, "", 7.2, lines=["con quay", "một trục"]))
    b.append(_arrow(412, 196, 384, 196, 1.0))
    b.append(_box(318, 176, 66, 40, "", 7.2, lines=["khuếch đại", "giải điều chế"]))
    b.append(_arrow(318, 196, 292, 196, 1.0))
    b.append(_box(242, 176, 50, 40, "", 7.2, lines=["hiệu", "chỉnh"]))
    b.append(_arrow(242, 196, 216, 196, 1.0))
    b.append(_box(120, 176, 96, 46, "", 7.2,
                  lines=["khuếch đại công suất", "điều chế", "động cơ mô-men"]))
    b.append(_l(168, 176, 168, 140, 1.0))
    b.append(_l(168, 140, 128, 140, 1.0))
    b.append(_arrow(128, 140, 128, 106, 1.0))
    b.append(_t(60, 124, "mô-men phân bố", 7.2, "start", "#444"))
    b.append(_t(60, 136, "lên bệ", 7.2, "start", "#444"))

    return _fig(svg(600, 240, STY + "".join(b), "Vòng ổn định bệ"),
                "Hình 10-24. Ổn định đạt được nhờ các bệ được thiết kế để giữ gia tốc kế và con quay "
                "luôn nằm ngang và định hướng theo phương vị một cách chính xác. Trong một số trường "
                "hợp, bệ được dẫn động quanh trục bằng động cơ servo và động cơ điện; đầu ra của các bộ "
                "tích phân kép được dùng trực tiếp để điều khiển tốc độ tiến động của con quay trục cấp. "
                "Các đầu dò nhạy trên con quay phát tín hiệu sai lệch để duy trì độ ổn định mong muốn "
                "khi có mô-men nhiễu.",
                "Figure 10-24. Stabilisation is obtained with platforms designed to hold accelerometers "
                "and gyros level and oriented in azimuth. In some cases the platform is driven about its "
                "axis by servo amplifiers and electric motors; pick-offs on the gyros feed error signals "
                "that keep the platform stable in the presence of disturbing torques.",
                "Sơ đồ khối vòng kín: khối bệ, góc nghiêng của bệ hồi tiếp qua con quay một trục, "
                "khuếch đại và giải điều chế, hiệu chỉnh, rồi khuếch đại công suất về điểm tổng.",
                "A closed-loop block diagram: the platform, its dip angle fed back through a single-axis "
                "gyro, an amplifier and demodulator, an equaliser, then a power amplifier back to the "
                "summing junction.")


def fig_10_25():
    """Aircraft stability: guidance, actuators, airframe, sensors, flight controller."""
    b = []
    b.append(_t(64, 70, "lệnh hướng", 7.4, "start", "#444"))
    b.append(_arrow(64, 84, 176, 84, 1.0))
    b.append(_box(176, 66, 82, 40, "", 7.2, lines=["điều khiển bay", "sơ cấp"]))
    b.append(_l(258, 86, 402, 86, 1.0))
    b.append(_arrow(402, 86, 402, 164, 1.0))
    b.append(_dot(402, 176, 2.6))

    b.append(_box(96, 150, 74, 40, "", 7.2, lines=["hệ dẫn", "đường"]))
    b.append(_arrow(170, 170, 196, 170, 1.0))
    b.append(_c(208, 170, 11, PAPER, 1.2))
    b.append(_t(202, 165, "+", 8.4, "middle", "#222", True))
    b.append(_t(202, 184, "+", 8.4, "middle", "#222", True))
    b.append(_arrow(219, 170, 250, 170, 1.0))
    b.append(_box(250, 150, 76, 40, "", 7.2, lines=["cơ cấu", "chấp hành"]))
    b.append(_arrow(326, 170, 356, 170, 1.0))
    b.append(_c(368, 170, 11, PAPER, 1.2))
    b.append(_t(362, 165, "+", 8.4, "middle", "#222", True))
    b.append(_t(362, 184, "+", 8.4, "middle", "#222", True))
    b.append(_arrow(379, 170, 414, 170, 1.0))
    b.append(_box(414, 148, 92, 44, "", 7.2, lines=["động học", "máy bay"]))
    b.append(_arrow(506, 170, 566, 170, 1.0))
    b.append(_t(512, 158, "chuyển động", 7.4, "start", "#444"))
    b.append(_t(346, 206, "góc lệch", 7.2, "middle", "#444"))

    b.append(_hexa(368, 108, 78, 30))
    b.append(_t(368, 112, "nhiễu", 7.4, "middle", "#222", True))
    b.append(_arrow(368, 123, 368, 157, 1.0))

    # the feedback path
    b.append(_l(560, 170, 560, 250, 1.0))
    b.append(_l(560, 250, 500, 250, 1.0))
    b.append(_arrow(500, 250, 486, 250, 1.0))
    b.append(_box(400, 232, 86, 36, "cảm biến", 7.4))
    b.append(_l(400, 250, 384, 250, 1.0))
    b.append(_c(372, 250, 11, PAPER, 1.2))
    b.append(_t(366, 245, "+", 8.4, "middle", "#222", True))
    b.append(_t(366, 264, "+", 8.4, "middle", "#222", True))
    b.append(_hexa(372, 300, 76, 28))
    b.append(_t(372, 304, "tạp âm", 7.4, "middle", "#222", True))
    b.append(_arrow(372, 286, 372, 262, 1.0))
    b.append(_arrow(361, 250, 336, 250, 1.0))
    b.append(_box(258, 232, 78, 36, "", 7.2, lines=["bộ điều khiển", "bay"]))
    b.append(_l(258, 250, 230, 250, 1.0))
    b.append(_l(230, 250, 230, 182, 1.0))
    b.append(_arrow(230, 182, 208, 182, 1.0))

    return _fig(svg(600, 330, STY + "".join(b), "Vòng ổn định máy bay"),
                "Hình 10-25. Trên nhiều máy bay dân dụng, con quay và gia tốc kế đặt đúng chỗ cấp tín "
                "hiệu điều khiển độ ổn định. Do nhiễu loạn ngẫu nhiên trong chuyến bay như trôi con "
                "quay, sai số thang đo và sai lệch điểm không của gia tốc kế, sai số hướng mong muốn "
                "tăng dần theo thời gian; các sai số tích luỹ này phải được bù định kỳ bằng thông tin "
                "bên ngoài như hệ dẫn đường Omega.",
                "Figure 10-25. On many commercial aircraft, suitably located gyroscopes and accelerometers "
                "supply signals that control stability. Random in-flight disturbances such as gyro drift, "
                "scale-factor error and accelerometer bias make the orientation error grow with time; "
                "these accumulated errors are compensated periodically from external information such as "
                "Omega navigation systems.",
                "Sơ đồ khối vòng điều khiển máy bay: lệnh hướng vào điều khiển bay sơ cấp, hệ dẫn đường "
                "qua cơ cấu chấp hành và điểm tổng thứ hai có nhiễu, tới động học máy bay; cảm biến hồi "
                "tiếp qua bộ điều khiển bay về điểm tổng thứ nhất.",
                "An aircraft control-loop block diagram: the heading command into primary flying controls, "
                "guidance through the actuators and a second summing junction with disturbances into the "
                "airframe dynamics, and sensors feeding back through the flight controller to the first junction.")


FIGURES = [fig_10_1, fig_10_2, fig_10_3, fig_10_4, fig_10_5, fig_10_6, fig_10_7,
           fig_10_8, fig_10_9, fig_10_10, fig_10_11, fig_10_12, fig_10_13, fig_10_14,
           fig_10_15, fig_10_16, fig_10_17, fig_10_18, fig_10_19, fig_10_20, fig_10_21,
           fig_10_22, fig_10_23, fig_10_24, fig_10_25]
