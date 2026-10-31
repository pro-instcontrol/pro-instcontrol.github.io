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


FIGURES = [fig_10_1, fig_10_2, fig_10_3, fig_10_4, fig_10_5, fig_10_6, fig_10_7]
