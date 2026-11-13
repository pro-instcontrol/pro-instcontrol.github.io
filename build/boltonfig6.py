# -*- coding: utf-8 -*-
"""Vector figures for Bolton *Control Systems* (Newnes, 2002), Chapter 6.

Every figure is redrawn as a clean vector so it stays legible on a phone,
matching the standard used for the other readers. Chapter 6 is Nyquist diagrams,
so a small complex-plane (real/imaginary) helper is provided.
"""
import math

from vfig import (BLUE, GOLD, GREY, INK, PAPER, RED, GREEN, _arrow, _axes,
                  _box, _circle, _curve, _defs, _ellipse, _f, _fig, _hatch,
                  _label, _line, _path, _poly, _rect, _ring, _txt, svg)


# ----------------------------------------------------------------- helpers
def _svg(w, h, objs, title=""):
    return svg(w, h, _defs() + "".join(objs), title)


def _f(o, w, h, vi, en, aria_vi="", aria_en=""):
    return _fig(_svg(w, h, o, vi), vi, en, aria_vi or vi, aria_en or en)


def tx(x, y, s, size=7.6, anchor="middle", color=INK, weight=""):
    return _txt(x, y, s, size, anchor=anchor, color=color, weight=weight)


def ln(x1, y1, x2, y2, dash="", color=INK, sw=0.9):
    return _line(x1, y1, x2, y2, sw=sw, dash=dash, color=color)


# ---- complex plane (real horizontal, imaginary vertical) -------------------
def _cplane(o, x0, y0, W, H, xmin, xmax, ymin, ymax, mark_neg1=True):
    o.append(_rect(x0, y0, W, H, "#fff", sw=0.8))
    for i in range(1, 5):
        gx = x0 + W * i / 5.0
        o.append(ln(gx, y0, gx, y0 + H, color=GREY, sw=0.3))
        gy = y0 + H * i / 5.0
        o.append(ln(x0, gy, x0 + W, gy, color=GREY, sw=0.3))
    xo = x0 + (0 - xmin) / (xmax - xmin) * W
    yo = y0 + H - (0 - ymin) / (ymax - ymin) * H
    o.append(ln(x0, yo, x0 + W, yo, color=INK, sw=0.7))
    o.append(ln(xo, y0, xo, y0 + H, color=INK, sw=0.7))
    o.append(tx(x0 + W - 3, yo - 4, "Real", 6.5, anchor="end", color=GREY))
    o.append(tx(xo + 4, y0 + 8, "Imag.", 6.5, anchor="start", color=GREY))
    if mark_neg1 and xmin <= -1 <= xmax:
        px = x0 + (-1 - xmin) / (xmax - xmin) * W
        o.append(_circle(px, yo, 2.6, fill=RED))
        o.append(tx(px, yo + 11, "-1", 6.5, anchor="middle", color=RED))


def _map_pt(real, imag, x0, y0, W, H, xmin, xmax, ymin, ymax):
    px = x0 + (real - xmin) / (xmax - xmin) * W
    py = y0 + H - (imag - ymin) / (ymax - ymin) * H
    px = max(x0 + 1, min(x0 + W - 1, px))
    py = max(y0 + 1, min(y0 + H - 1, py))
    return px, py


def _curve_xy(o, pts, x0, y0, W, H, xmin, xmax, ymin, ymax, color=BLUE, sw=1.3, dash=""):
    pix = [_map_pt(r, i, x0, y0, W, H, xmin, xmax, ymin, ymax) for (r, i) in pts]
    o.append(_poly(pix, fill="none", sw=sw, color=color, dash=dash))


def _nyq(fn, wmin=1e-3, wmax=1000.0, N=300):
    out = []
    for k in range(N + 1):
        w = wmin * (wmax / wmin) ** (k / N)
        z = fn(complex(0, w))
        out.append((z.real, z.imag))
    return out


# ---- polar grid -------------------------------------------------------------
def _polar_grid(o, cx, cy, R):
    for r in [0.25, 0.5, 0.75, 1.0]:
        o.append(_circle(cx, cy, R * r, fill="none", sw=0.4, color=GREY))
    for ang in range(0, 360, 30):
        a = math.radians(ang)
        o.append(ln(cx, cy, cx + R * math.cos(a), cy - R * math.sin(a), color=GREY, sw=0.3))
    o.append(ln(cx - R, cy, cx + R, cy, color=INK, sw=0.6))
    o.append(ln(cx, cy - R, cx, cy + R, color=INK, sw=0.6))


def _pol_pt(r, deg, cx, cy, R):
    a = math.radians(deg)
    return cx + R * r * math.cos(a), cy - R * r * math.sin(a)


# =====================================================================
# Figure 6.1 - Cartesian vs polar graph
# =====================================================================
def fig_6_1():
    o = []
    # (a) cartesian
    o.append(tx(70, 14, "(a) Cartesian", 7))
    o.append(_rect(20, 28, 110, 90, "#fff", sw=0.8))
    o.append(ln(20, 73, 130, 73, color=INK, sw=0.6))
    o.append(ln(75, 28, 75, 118, color=INK, sw=0.6))
    o.append(tx(20, 76, "x", 6.5, anchor="end", color=GREY))
    o.append(tx(78, 116, "y", 6.5, anchor="start", color=GREY))
    o.append(_circle(110, 45, 2.6, fill=RED))
    o.append(tx(114, 44, "(x, y)", 6.5, anchor="start", color=RED))
    # (b) polar
    o.append(tx(250, 14, "(b) Polar", 7))
    _polar_grid(o, 250, 73, 55)
    rx, ry = _pol_pt(0.8, 50, 250, 73, 55)
    o.append(_circle(rx, ry, 2.6, fill=RED))
    o.append(tx(rx + 4, ry, "(r, \u03b8)", 6.5, anchor="start", color=RED))
    return _f(o, 360, 130,
              "So sánh hai cách biểu diễn điểm: (a) đồ thị Descartes theo tọa độ x, y; (b) đồ thị cực theo bán kính r và góc \u03b8.",
              "Comparing two ways to specify a point: (a) a Cartesian graph by x and y values, (b) a polar graph by radial distance r and angle \u03b8.")


# =====================================================================
# Figure 6.2 - Polar plot traced by phasor tips (0 to infinity)
# =====================================================================
def fig_6_2():
    o = []
    _polar_grid(o, 130, 110, 95)
    # sample locus: radius shrinks as frequency rises, angle goes negative
    pts = []
    for t in range(0, 110, 5):
        ang = -t
        r = 1.0 / (1 + t / 60.0)
        pts.append(_pol_pt(r, ang, 130, 110, 95))
    o.append(_poly(pts, fill="none", sw=1.4, color=BLUE))
    # arrow indicating increasing frequency
    o.append(tx(pts[-1][0], pts[-1][1] - 8, "increasing frequency", 6.5, anchor="middle", color=GREY))
    return _f(o, 260, 220,
              "Biểu đồ cực của đáp ứng tần số là đường cong được vẽ bởi các đỉnh phasor khi tần số thay đổi từ 0 đến vô cực.",
              "The polar plot of the frequency response is the line traced out by the tips of the phasors as the frequency is changed from zero to infinity.")


# =====================================================================
# Figure 6.3 - Example polar plot (tabulated data)
# =====================================================================
def fig_6_3():
    o = []
    _polar_grid(o, 130, 110, 95)
    data = [(1.6, -150), (1.0, -160), (0.6, -170), (0.4, -180), (0.2, -190)]
    pts = [_pol_pt(r, d, 130, 110, 95) for (r, d) in data]
    o.append(_poly(pts, fill="none", sw=1.4, color=BLUE))
    for (r, d), (px, py) in zip(data, pts):
        o.append(_circle(px, py, 2.4, fill=RED))
    return _f(o, 260, 220,
              "Ví dụ biểu đồ cực từ dữ liệu thực nghiệm: độ lớn 1,6\u21920,2 và pha -150\u00b0\u2192-190\u00b0 khi tần số tăng 1,4\u21923,8 rad/s.",
              "Example polar plot from tabulated data: magnitude 1.6\u21920.2 and phase -150\u00b0\u2192-190\u00b0 as frequency rises from 1.4 to 3.8 rad/s.")


# =====================================================================
# Figure 6.4 - Nyquist diagram for a first-order system 1/(1+tau s)
# =====================================================================
def fig_6_4():
    o = []
    _cplane(o, 30, 30, 230, 190, 0, 1.1, -1.1, 0.1)
    pts = _nyq(lambda s: 1 / (1 + s), wmin=1e-3, wmax=1000, N=200)
    _curve_xy(o, pts, 30, 30, 230, 190, 0, 1.1, -1.1, 0.1, color=BLUE)
    # arrow at start
    return _f(o, 290, 230,
              "Biểu đồ Nyquist của hệ bậc nhất G(s)=1/(1+\u03c4s): nửa đường tròn dưới, từ (1,0) tại \u03c9=0 đến gốc tọa độ tại \u03c9=\u221e.",
              "Nyquist diagram of the first-order system G(s)=1/(1+\u03c4s): a lower semicircle from (1,0) at \u03c9=0 to the origin at \u03c9=\u221e.")


# =====================================================================
# Figure 6.5 - Nyquist for 1/[s(s+1)]
# =====================================================================
def fig_6_5():
    o = []
    _cplane(o, 30, 30, 230, 190, -1.6, 0.3, -4.0, 0.3)
    pts = _nyq(lambda s: 1 / (s * (s + 1)), wmin=0.3, wmax=200, N=300)
    _curve_xy(o, pts, 30, 30, 230, 190, -1.6, 0.3, -4.0, 0.3, color=BLUE)
    return _f(o, 290, 230,
              "Biểu đồ Nyquist của 1/[s(s+1)]: đi từ xa dọc trục ảnh rồi vòng qua góc phần tư ba về gốc tọa độ.",
              "Nyquist plot of 1/[s(s+1)]: it comes from far along the imaginary axis, loops through the third quadrant and returns to the origin.")


# =====================================================================
# Figure 6.6 - Stability and the Nyquist plot (stable / marginal / unstable)
# =====================================================================
def fig_6_6():
    o = []
    _cplane(o, 30, 30, 230, 200, -2.0, 1.2, -1.6, 1.6, mark_neg1=True)

    def loop(points, color, dash=""):
        _curve_xy(o, points, 30, 30, 230, 200, -2.0, 1.2, -1.6, 1.6, color=color, sw=1.4, dash=dash)

    # stable: stays in right half (never reaches -1)
    loop([(1, 0), (0.9, -0.3), (0.6, -0.5), (0.3, -0.5), (0.1, -0.3), (0, 0)], BLUE)
    # marginally stable: passes through (-1,0)
    loop([(1, 0), (0.5, -0.4), (-0.3, -0.55), (-1, 0), (-0.3, 0.55), (0.5, 0.4), (0, 0)], GOLD)
    # unstable: encloses -1 (goes left of it)
    loop([(1, 0), (0.1, -0.7), (-1.6, 0), (0.1, 0.7), (0, 0)], RED)
    o.append(tx(60, 50, "Stable", 7, anchor="start", color=BLUE))
    o.append(tx(60, 64, "Marginally stable", 7, anchor="start", color=GOLD))
    o.append(tx(60, 78, "Unstable", 7, anchor="start", color=RED))
    return _f(o, 290, 240,
              "Tiêu chuẩn ổn định Nyquist: quỹ đạo vòng hở không bao quanh điểm -1 thì ổn định; bao quanh thì không ổn định; đi qua -1 thì ở biên ổn định.",
              "Nyquist stability criterion: if the open-loop locus does not encircle the -1 point the system is stable; encircling it is unstable; passing through -1 is marginally stable.")


# =====================================================================
# Figure 6.7 - Nyquist K/(s+a), stable for all K>0
# =====================================================================
def fig_6_7():
    o = []
    _cplane(o, 30, 30, 230, 190, -1.6, 1.2, -1.1, 0.1)
    pts = _nyq(lambda s: 1 / (s + 1), wmin=1e-3, wmax=1000, N=200)
    _curve_xy(o, pts, 30, 30, 230, 190, -1.6, 1.2, -1.1, 0.1, color=BLUE)
    o.append(tx(140, 60, "stable for all K > 0", 6.5, anchor="start", color=GREY))
    return _f(o, 290, 230,
              "Nyquist của K/(s+a): nửa đường tròn dưới nằm hoàn toàn ở nửa phải, không bao giờ bao quanh -1 \u2192 ổn định với mọi K>0.",
              "Nyquist of K/(s+a): a lower semicircle entirely in the right half-plane, never encircling -1 \u2192 stable for all K>0.")


# =====================================================================
# Figure 6.8 - Nyquist K/s(s+a), stable for all K>0
# =====================================================================
def fig_6_8():
    o = []
    _cplane(o, 30, 30, 230, 190, -1.6, 0.3, -4.0, 0.3)
    pts = _nyq(lambda s: 1 / (s * (s + 1)), wmin=0.3, wmax=200, N=300)
    _curve_xy(o, pts, 30, 30, 230, 190, -1.6, 0.3, -4.0, 0.3, color=BLUE)
    o.append(tx(40, 50, "stable for all K > 0", 6.5, anchor="start", color=GREY))
    return _f(o, 290, 230,
              "Nyquist của K/s(s+a): quỹ đạo ở góc phần tư ba, không bao giờ cắt trục thực âm trước gốc \u2192 ổn định với mọi K>0.",
              "Nyquist of K/s(s+a): a third-quadrant locus that never crosses the negative real axis before the origin \u2192 stable for all K>0.")


# =====================================================================
# Figure 6.9 - Nyquist K/(s+a)(s+b), stable for all K>0
# =====================================================================
def fig_6_9():
    o = []
    _cplane(o, 30, 30, 230, 190, -0.9, 0.7, -0.7, 0.1)
    pts = _nyq(lambda s: 1 / ((s + 1) * (s + 2)), wmin=1e-3, wmax=1000, N=300)
    _curve_xy(o, pts, 30, 30, 230, 190, -0.9, 0.7, -0.7, 0.1, color=BLUE)
    o.append(tx(40, 50, "stable for all K > 0", 6.5, anchor="start", color=GREY))
    return _f(o, 290, 230,
              "Nyquist của K/(s+a)(s+b): cắt trục thực âm tại -K/(ab) (ở bên phải -1 với K nhỏ) \u2192 ổn định với mọi K>0.",
              "Nyquist of K/(s+a)(s+b): it crosses the negative real axis at -K/(ab) (to the right of -1 for small K) \u2192 stable for all K>0.")


# =====================================================================
# Figure 6.10 - Nyquist K/s(s+a)(s+b): unstable for large K
# =====================================================================
def fig_6_10():
    o = []
    _cplane(o, 30, 30, 230, 190, -1.4, 0.3, -1.4, 0.3)
    pts = _nyq(lambda s: 1 / (s * (s + 1) * (s + 2)), wmin=0.3, wmax=200, N=300)
    _curve_xy(o, pts, 30, 30, 230, 190, -1.4, 0.3, -1.4, 0.3, color=BLUE)
    o.append(tx(40, 50, "stable for small K, unstable for large K", 6.3, anchor="start", color=GREY))
    return _f(o, 290, 230,
              "Nyquist của K/s(s+a)(s+b): cắt trục thực âm tại -K/(a+b); ổn định khi -K/(a+b) > -1, tức K < a+b (không ổn định nếu K lớn).",
              "Nyquist of K/s(s+a)(s+b): it crosses the negative real axis at -K/(a+b); stable when -K/(a+b) > -1, i.e. K < a+b (unstable for large K).")


# =====================================================================
# Figure 6.11 - Example Nyquist K/(s+1)(s+2)(s+3), K=20
# =====================================================================
def fig_6_11():
    o = []
    _cplane(o, 30, 30, 230, 190, -1.3, 3.6, -1.2, 0.3)
    pts = _nyq(lambda s: 20 / ((s + 1) * (s + 2) * (s + 3)), wmin=1e-3, wmax=1000, N=300)
    _curve_xy(o, pts, 30, 30, 230, 190, -1.3, 3.6, -1.2, 0.3, color=BLUE)
    # mark crossing -K/60 = -1/3
    x0, y0, W, H = 30, 30, 230, 190
    xmin, xmax, ymin, ymax = -1.3, 3.6, -1.2, 0.3
    cx = x0 + (-1.0 / 3 - xmin) / (xmax - xmin) * W
    cy = y0 + H - (0 - ymin) / (ymax - ymin) * H
    o.append(_circle(cx, cy, 2.6, fill=GREEN))
    o.append(tx(cx, cy + 11, "-K/60 = -1/3", 6.5, anchor="middle", color=GREEN))
    return _f(o, 290, 230,
              "Ví dụ Nyquist của K/[(s+1)(s+2)(s+3)] với K=20: cắt trục thực tại -K/60 = -1/3 (bên phải -1) \u2192 ổn định; mất ổn định khi K\u226560.",
              "Example Nyquist of K/[(s+1)(s+2)(s+3)] with K=20: it crosses the real axis at -K/60 = -1/3 (right of -1) \u2192 stable; unstable when K\u226560.")


# =====================================================================
# Figure 6.12 - Phase crossover and gain margin
# =====================================================================
def fig_6_12():
    o = []
    _cplane(o, 30, 30, 230, 190, -1.6, 1.0, -1.1, 0.1)
    # a stable Nyquist curve (first-order-like) crossing negative real axis at -x with x<1
    pts = _nyq(lambda s: 1 / (1 + s), wmin=1e-3, wmax=1000, N=200)
    _curve_xy(o, pts, 30, 30, 230, 190, -1.6, 1.0, -1.1, 0.1, color=BLUE)
    x0, y0, W, H, xmin, xmax, ymin, ymax = 30, 30, 230, 190, -1.6, 1.0, -1.1, 0.1
    # mark where it crosses real axis: -0.5 (x)
    cx = x0 + (-0.5 - xmin) / (xmax - xmin) * W
    yo = y0 + H - (0 - ymin) / (ymax - ymin) * H
    o.append(_circle(cx, yo, 2.6, fill=GREEN))
    o.append(tx(cx, yo + 11, "-x", 6.5, anchor="middle", color=GREEN))
    o.append(ln(cx, yo, x0 + (-1 - xmin) / (xmax - xmin) * W, yo, color=RED, sw=1.0, dash="3 3"))
    o.append(tx((cx + x0 + (-1 - xmin) / (xmax - xmin) * W) / 2, yo - 5, "gain margin", 6.3, anchor="middle", color=RED))
    return _f(o, 290, 230,
              "Trên biểu đồ Nyquist: tần số cắt pha là giao điểm với trục thực âm (tại -x). Dự trữ lợi = 20 lg(1/x); điểm -1 tương ứng biên ổn định.",
              "On a Nyquist plot the phase crossover is where the locus crosses the negative real axis (at -x). Gain margin = 20 lg(1/x); the -1 point is the stability boundary.")


# =====================================================================
# Figure 6.13 - Phase margin (gain crossover rotated to -1)
# =====================================================================
def fig_6_13():
    o = []
    _cplane(o, 30, 30, 230, 190, -1.6, 1.0, -1.1, 0.1)
    x0, y0, W, H, xmin, xmax, ymin, ymax = 30, 30, 230, 190, -1.6, 1.0, -1.1, 0.1
    cx = x0 + (0 - xmin) / (xmax - xmin) * W
    cy = y0 + H - (0 - ymin) / (ymax - ymin) * H
    o.append(_circle(cx, cy, 1.0 / (xmax - xmin) * W, fill="none", color=GREY, sw=0.6))
    pts = _nyq(lambda s: 1 / (1 + s), wmin=1e-3, wmax=1000, N=200)
    _curve_xy(o, pts, 30, 30, 230, 190, -1.6, 1.0, -1.1, 0.1, color=BLUE)
    # gain crossover point on the unit circle
    gx = x0 + (0.7 - xmin) / (xmax - xmin) * W
    gy = y0 + H - (-0.7 - ymin) / (ymax - ymin) * H
    o.append(_circle(gx, gy, 2.6, fill=GREEN))
    o.append(tx(gx, gy - 6, "gain crossover", 6.3, anchor="middle", color=GREEN))
    # line from origin through gain crossover to -1
    x1 = x0 + (-1 - xmin) / (xmax - xmin) * W
    o.append(ln(cx, cy, x1, cy, color=RED, sw=0.9, dash="3 3"))
    o.append(ln(cx, cy, gx, gy, color=RED, sw=0.9, dash="3 3"))
    o.append(tx(x1 - 6, cy - 6, "-1", 6.5, anchor="end", color=RED))
    return _f(o, 290, 230,
              "Dự trữ pha là góc phải quay đường thẳng từ gốc qua điểm cắt lợi (trên đường tròn bán kính 1) để đi qua điểm (-1, j0).",
              "The phase margin is the angle through which the line from the origin through the gain-crossover point (on the unit circle) must be rotated to pass through (-1, j0).")


FIGS = {n: globals()[n] for n in dir() if n.startswith("fig_")}
