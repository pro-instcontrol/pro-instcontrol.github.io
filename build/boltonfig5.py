# -*- coding: utf-8 -*-
"""Vector figures for Bolton *Control Systems* (Newnes, 2002), Chapter 5.

Every figure is redrawn as a clean vector so it stays legible on a phone,
matching the standard used for the other readers. Chapter 5 is dominated by
Bode plots, so a small log-x Bode helper is provided alongside the shared
block-diagram / phasor helpers from boltonfig.py.
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


def bx(x, y, w, h, label, fill="#eef3fb", size=8):
    return _box(x, y, w, h, label, fill=fill, size=size)


def ar(x1, y1, x2, y2, dash="", color=INK, sw=1.2):
    return _arrow(x1, y1, x2, y2, sw=sw, color=color, dash=dash)


def ln(x1, y1, x2, y2, dash="", color=INK, sw=0.9):
    return _line(x1, y1, x2, y2, sw=sw, dash=dash, color=color)


def tx(x, y, s, size=7.6, anchor="middle", color=INK, weight=""):
    return _txt(x, y, s, size, anchor=anchor, color=color, weight=weight)


def sumj(x, y, signs, r=11):
    o = [_circle(x, y, r, fill="#fff")]
    pos = [(x, y - r - 4), (x + r + 5, y + 3), (x, y + r + 5), (x - r - 5, y + 3)]
    for i, s in enumerate(signs[:4]):
        if s:
            o.append(_txt(pos[i][0], pos[i][1], s, 8, anchor="middle", color=INK))
    return "".join(o)


def tap(x, y):
    return _circle(x, y, 2.6, fill=INK)


# ---- Bode helpers (log frequency axis, linear gain/phase) -------------------
def _bx(f, fmin, fmax, x0, W):
    return x0 + (math.log10(f) - math.log10(fmin)) / (math.log10(fmax) - math.log10(fmin)) * W


def _by(v, vmin, vmax, y0, H):
    return y0 + H - (v - vmin) / (vmax - vmin) * H


def _baxes(o, x0, y0, W, H, fmin, fmax, vmin, vmax, ylab):
    o.append(_rect(x0, y0, W, H, "#fff", sw=0.8))
    ticks = [0.1, 0.2, 0.5, 1, 2, 5, 10, 20, 50, 100, 200, 500, 1000]
    for t in ticks:
        if fmin <= t <= fmax:
            px = _bx(t, fmin, fmax, x0, W)
            o.append(ln(px, y0, px, y0 + H, color=GREY, sw=0.35))
    step = (vmax - vmin) / 4.0
    for i in range(5):
        vv = vmin + i * step
        py = _by(vv, vmin, vmax, y0, H)
        o.append(ln(x0, py, x0 + W, py, color=GREY, sw=0.35))
        o.append(tx(x0 - 4, py + 2, "%.0f" % vv, 6, anchor="end", color=GREY))
    for t in [0.1, 1, 10, 100, 1000]:
        if fmin <= t <= fmax:
            px = _bx(t, fmin, fmax, x0, W)
            o.append(tx(px, y0 + H + 10, "%.1g" % t, 6, anchor="middle", color=GREY))
    o.append(tx(x0 + W / 2, y0 + H + 22, "Frequency (rad/s)", 6.5, anchor="middle", color=GREY))
    if ylab:
        o.append(tx(x0 - 6, y0 - 6, ylab, 6.5, anchor="end", color=GREY))


def _bcurve(o, fn, x0, y0, W, H, fmin, fmax, vmin, vmax, color=BLUE, sw=1.3):
    pts = []
    N = 200
    for i in range(N + 1):
        f = 10 ** (math.log10(fmin) + (math.log10(fmax) - math.log10(fmin)) * i / N)
        v = fn(f)
        px = _bx(f, fmin, fmax, x0, W)
        py = _by(v, vmin, vmax, y0, H)
        pts.append((px, py))
    o.append(_poly(pts, fill="none", sw=sw, color=color))


def _bode2(o, x0, y0, W, H, fmin, fmax, gainfn, phasefn, gmin, gmax, pmin, pmax):
    _baxes(o, x0, y0, W, H, fmin, fmax, gmin, gmax, "Gain dB")
    _bcurve(o, gainfn, x0, y0, W, H, fmin, fmax, gmin, gmax, color=BLUE, sw=1.4)
    py0 = y0 + H + 34
    _baxes(o, x0, py0, W, H, fmin, fmax, pmin, pmax, "Phase \u00b0")
    _bcurve(o, phasefn, x0, py0, W, H, fmin, fmax, pmin, pmax, color=RED, sw=1.4)


# ---- phasor / Argand helpers ------------------------------------------------
def _phasor(o, cx, cy, R, angle_deg, with_wave=True):
    o.append(_circle(cx, cy, R, fill="#fff", sw=0.8))
    a = math.radians(angle_deg)
    ex, ey = cx + R * math.cos(a), cy - R * math.sin(a)
    o.append(ln(cx, cy, ex, ey, color=INK, sw=1.2))
    # y-axis (vertical) for the sinusoid projection
    o.append(ln(cx - R - 6, cy, cx + R + 6, cy, color=GREY, sw=0.5))
    o.append(ln(cx, cy - R - 6, cx, cy + R + 6, color=GREY, sw=0.5))
    if with_wave:
        o.append(ln(ex, ey, ex, cy, color=GREEN, sw=0.8, dash="2 2"))
        o.append(_circle(ex, ey, 2.4, fill=RED))
    return ex, ey


def _argand(o, x0, y0, W, H):
    o.append(_rect(x0, y0, W, H, "#fff", sw=0.8))
    cx, cy = x0 + W / 2, y0 + H / 2
    o.append(ln(x0, cy, x0 + W, cy, color=INK, sw=0.6))
    o.append(ln(cx, y0, cx, y0 + H, color=INK, sw=0.6))
    o.append(tx(x0 + W - 3, cy - 6, "Real", 6.5, anchor="end", color=GREY))
    o.append(tx(cx + 4, y0 + 8, "Imag.", 6.5, anchor="start", color=GREY))
    return cx, cy


# =====================================================================
# Figure 5.1 - Sinusoidal signals as rotating phasors
# =====================================================================
def fig_5_1():
    o = []
    o.append(tx(95, 16, "(a) y = Y sin \u03c9t", 7))
    _phasor(o, 95, 70, 45, 0)
    o.append(tx(95, 128, "(b) y = Y sin(\u03c9t + \u03b8)", 7))
    _phasor(o, 95, 182, 45, 50)
    return _f(o, 200, 215,
              "Tín hiệu sin được biểu diễn bằng một vectơ (phasor) quay: (a) tại t=0 nằm trên trục thực, (b) lệch một góc pha \u03b8.",
              "Sinusoidal signals represented by rotating phasors: (a) y = Y sin \u03c9t starts on the reference axis, (b) y = Y sin(\u03c9t+\u03b8) starts at phase angle \u03b8.")


# =====================================================================
# Figure 5.2 - Complex number on an Argand diagram
# =====================================================================
def fig_5_2():
    o = []
    cx, cy = _argand(o, 30, 30, 180, 150)
    # point at (a,b)
    a, b = 0.55, 0.5
    px, py = cx + a * 80, cy - b * 80
    o.append(ln(cx, cy, px, py, color=RED, sw=1.4))
    o.append(_circle(px, py, 2.6, fill=RED))
    o.append(tx((cx + px) / 2 + 6, (cy + py) / 2, "|z|", 7, anchor="start", color=RED))
    o.append(tx(px + 4, py - 4, "z = a + jb", 6.8, anchor="start", color=INK))
    o.append(tx(cx, cy + 6, "0", 6.5, anchor="end", color=GREY))
    return _f(o, 240, 195,
              "Một số phức z = a + jb được biểu diễn trên mặt phẳng Argand bởi một đoạn thẳng độ dài |z| và góc \u03b8.",
              "A complex number z = a + jb is represented on an Argand diagram by a line of length |z| at angle \u03b8.")


# =====================================================================
# Figure 5.3 - Phasors on an Argand diagram (a) no phase (b) phase \u03b8 (c) 90\u00b0
# =====================================================================
def fig_5_3():
    o = []
    specs = [("a", 0, 80, 30), ("b", 50, 100, 30), ("c", 90, 90, 120)]
    for lab, ang, x0, W in specs:
        o.append(tx(x0 + W / 2, 16, "(%s)" % lab, 7))
        cx, cy = _argand(o, x0, 28, W, 150)
        a = math.radians(ang)
        px, py = cx + 0.55 * 60 * math.cos(a), cy - 0.55 * 60 * math.sin(a)
        o.append(ln(cx, cy, px, py, color=RED, sw=1.3))
        o.append(_circle(px, py, 2.4, fill=RED))
        o.append(tx(cx, cy + 6, "0", 6, anchor="end", color=GREY))
    return _f(o, 360, 195,
              "Phasor trên mặt phẳng Argand: (a) không góc pha (trên trục thực), (b) góc pha \u03b8, (c) góc pha 90\u00b0 (trên trục ảo).",
              "Phasors on an Argand diagram: (a) no phase angle (real axis), (b) phase angle \u03b8, (c) phase 90\u00b0 (imaginary axis).")


# =====================================================================
# Figure 5.4 - Phasor rotated 0, 90, 180, 270 degrees
# =====================================================================
def fig_5_4():
    o = []
    specs = [("(a) 0\u00b0", 0, 20), ("(b) 90\u00b0", 90, 115), ("(c) 180\u00b0", 180, 210), ("(d) 270\u00b0", 270, 305)]
    for lab, ang, x0 in specs:
        o.append(tx(x0 + 45, 16, lab, 7))
        _phasor(o, x0 + 45, 80, 38, ang, with_wave=False)
    return _f(o, 390, 130,
              "Phasor quay: (a) 0\u00b0, (b) 90\u00b0 (nhân j), (c) 180\u00b0 (nhân j\u00b2 = -1), (d) 270\u00b0 (nhân j\u00b3 = -j).",
              "Phasor rotated by (a) 0\u00b0, (b) 90\u00b0 (multiply by j), (c) 180\u00b0 (j\u00b2 = -1), (d) 270\u00b0 (j\u00b3 = -j).")


# =====================================================================
# Figure 5.5 - Electrical system with sinusoidal input
# =====================================================================
def fig_5_5():
    o = []
    o.append(bx(30, 45, 110, 44, "Electrical\nsystem", fill="#eef3fb"))
    o.append(ar(10, 67, 30, 67))
    o.append(ar(140, 67, 200, 67))
    o.append(tx(6, 61, "Sinusoidal", 6.8, anchor="start"))
    o.append(tx(6, 71, "signal", 6.8, anchor="start"))
    o.append(tx(204, 61, "Sinusoidal", 6.8, anchor="start"))
    o.append(tx(204, 71, "signal", 6.8, anchor="start"))
    return _f(o, 290, 110,
              "Một hệ điện (như mạch trở–tụ nối tiếp) với đầu vào sin thì đầu ra cũng sin, cùng tần số nhưng khác biên độ và lệch pha.",
              "An electrical system (e.g. a resistor–capacitor series circuit) with a sinusoidal input gives a sinusoidal output of the same frequency but different amplitude and phase.")


# =====================================================================
# Figure 5.6 - Frequency response of a system
# =====================================================================
def fig_5_6():
    o = []
    o.append(bx(60, 50, 120, 46, "System", fill="#eef3fb"))
    o.append(ar(15, 73, 60, 73))
    o.append(ar(180, 73, 270, 73))
    o.append(tx(8, 68, "A sin \u03c9t", 7, anchor="start"))
    o.append(tx(278, 68, "B sin(\u03c9t+\u03c6)", 7, anchor="start"))
    # little sine wave under input/output
    x0, y0, W, H = 15, 110, 255, 60
    o.append(_curve(lambda t: 0.5 + 0.4 * math.sin(2 * math.pi * t), x0, y0, W, H, xr=(0, 4), yr=(0, 1), color=BLUE, sw=1.2))
    return _f(o, 300, 185,
              "Đáp ứng tần số của một hệ: đầu vào A sin \u03c9t cho đầu ra B sin(\u03c9t+\u03c6) — cùng tần số, khác biên độ và lệch pha.",
              "The frequency response of a system: an input A sin \u03c9t gives an output B sin(\u03c9t+\u03c6) — same frequency, different amplitude and phase.")


# =====================================================================
# Figure 5.7 - Systems in series
# =====================================================================
def fig_5_7():
    o = []
    for i, lab in enumerate(["System 1", "System 2", "System 3"]):
        x = 25 + i * 130
        o.append(bx(x, 45, 95, 44, lab, fill="#eef3fb"))
        if i < 2:
            o.append(ar(x + 95, 67, x + 130, 67))
    o.append(ar(10, 67, 25, 67))
    o.append(ar(380, 67, 430, 67))
    return _f(o, 440, 110,
              "Các hệ nối tiếp: tổng lợi (gain) là tích các lợi riêng, tổng góc pha là tổng các góc pha riêng.",
              "Systems in series: the overall gain is the product of the individual gains and the total phase is the sum of the individual phase shifts.")


def _const_gain(K):
    return (lambda f: 20 * math.log10(abs(K)),
            lambda f: (0.0 if K > 0 else -180.0))


# =====================================================================
# Figure 5.8 - Bode plot for constant transfer function (K>0 and K<0)
# =====================================================================
def fig_5_8():
    o = []
    o.append(tx(120, 14, "(a) K > 0", 7))
    g, p = _const_gain(10)
    _bode2(o, 30, 28, 200, 70, 0.1, 100, g, p, -20, 40, -180, 90)
    o.append(tx(340, 14, "(b) K < 0", 7))
    g2, p2 = _const_gain(-10)
    _bode2(o, 250, 28, 200, 70, 0.1, 100, g2, p2, -20, 40, -180, 90)
    return _f(o, 470, 210,
              "Bode của hàm truyền hằng số K = 10: lợi không đổi 20 dB; pha 0\u00b0 nếu K>0, -180\u00b0 nếu K<0.",
              "Bode plot for a constant transfer function K = 10: constant gain of 20 dB; phase 0\u00b0 for K>0, -180\u00b0 for K<0.")


# =====================================================================
# Figure 5.9 - Bode plot for transfer functions 1/s^n
# =====================================================================
def fig_5_9():
    o = []
    _baxes(o, 30, 28, 190, 150, 0.1, 100, -80, 20, "Gain dB")
    for n in [1, 2, 3]:
        _bcurve(o, lambda f, n=n: -20 * n * math.log10(f), 30, 28, 190, 150, 0.1, 100, -80, 20,
                color=[BLUE, GOLD, GREEN][n - 1], sw=1.3)
    o.append(tx(60, 44, "n=1", 6.5, color=BLUE))
    o.append(tx(60, 60, "n=2", 6.5, color=GOLD))
    o.append(tx(60, 76, "n=3", 6.5, color=GREEN))
    py0 = 28 + 150 + 34
    _baxes(o, 30, py0, 190, 150, 0.1, 100, -270, 0, "Phase \u00b0")
    for n in [1, 2, 3]:
        _bcurve(o, lambda f, n=n: -90 * n, 30, py0, 190, 150, 0.1, 100, -270, 0,
                color=[BLUE, GOLD, GREEN][n - 1], sw=1.3)
    return _f(o, 250, 410,
              "Bode của 1/s^n: lợi dốc -20n dB/thập kỷ; pha -n\u00b790\u00b0.",
              "Bode plot for 1/s^n: gain slope -20n dB/decade; phase -n\u00d790\u00b0.")


# =====================================================================
# Figure 5.10 - Bode plot for transfer functions s^m
# =====================================================================
def fig_5_10():
    o = []
    _baxes(o, 30, 28, 190, 150, 0.1, 100, -20, 80, "Gain dB")
    for m in [1, 2, 3]:
        _bcurve(o, lambda f, m=m: 20 * m * math.log10(f), 30, 28, 190, 150, 0.1, 100, -20, 80,
                color=[BLUE, GOLD, GREEN][m - 1], sw=1.3)
    o.append(tx(60, 150, "m=1", 6.5, color=BLUE))
    o.append(tx(60, 134, "m=2", 6.5, color=GOLD))
    o.append(tx(60, 118, "m=3", 6.5, color=GREEN))
    py0 = 28 + 150 + 34
    _baxes(o, 30, py0, 190, 150, 0.1, 100, 0, 270, "Phase \u00b0")
    for m in [1, 2, 3]:
        _bcurve(o, lambda f, m=m: 90 * m, 30, py0, 190, 150, 0.1, 100, 0, 270,
                color=[BLUE, GOLD, GREEN][m - 1], sw=1.3)
    return _f(o, 250, 410,
              "Bode của s^m (zero tại gốc): lợi dốc +20m dB/thập kỷ; pha +m\u00b790\u00b0.",
              "Bode plot for s^m (zero at the origin): gain slope +20m dB/decade; phase +m\u00d790\u00b0.")


# =====================================================================
# Figure 5.11 - Bode plot for transfer function 1/(1 + \u03c4s)
# =====================================================================
def fig_5_11(tau=1.0):
    o = []
    def g(f):
        return -10 * math.log10(1 + (f * tau) ** 2)
    def p(f):
        return -math.degrees(math.atan(f * tau))
    _bode2(o, 30, 28, 200, 70, 0.01, 100, g, p, -40, 20, -90, 0)
    return _f(o, 250, 210,
              "Bode của 1/(1+\u03c4s): lợi 0 dB ở tần thấp, dốc -20 dB/thập kỷ sau điểm gãy \u03c9=1/\u03c4; pha 0\u00b0\u2192-90\u00b0, -45\u00b0 tại điểm gãy.",
              "Bode plot for 1/(1+\u03c4s): gain 0 dB at low frequency, -20 dB/decade after the break at \u03c9=1/\u03c4; phase 0\u00b0\u2192-90\u00b0, -45\u00b0 at the break.")


# =====================================================================
# Figure 5.12 - Example Bode plot, transfer function 100/(s+100)
# =====================================================================
def fig_5_12():
    o = []
    tau = 1.0 / 100.0
    def g(f):
        return 20 * math.log10(100) - 10 * math.log10(1 + (f * tau) ** 2)
    def p(f):
        return -math.degrees(math.atan(f * tau))
    _bode2(o, 30, 28, 200, 70, 1, 1000, g, p, -40, 40, -90, 0)
    return _f(o, 250, 210,
              "Ví dụ Bode của 100/(s+100): điểm gãy tại 100 rad/s; lợi -20 dB/thập kỷ sau đó; pha -45\u00b0 tại điểm gãy.",
              "Example Bode plot for 100/(s+100): break point at 100 rad/s, gain -20 dB/decade beyond it, phase -45\u00b0 at the break.")


# =====================================================================
# Figure 5.13 - Bode plot for transfer function (1 + \u03c4s)  (zero)
# =====================================================================
def fig_5_13(tau=1.0):
    o = []
    def g(f):
        return 10 * math.log10(1 + (f * tau) ** 2)
    def p(f):
        return math.degrees(math.atan(f * tau))
    _bode2(o, 30, 28, 200, 70, 0.01, 100, g, p, -20, 40, 0, 90)
    return _f(o, 250, 210,
              "Bode của (1+\u03c4s) (zero): lợi 0 dB ở tần thấp, +20 dB/thập kỷ sau điểm gãy; pha 0\u00b0\u2192+90\u00b0.",
              "Bode plot for (1+\u03c4s) (a zero): gain 0 dB at low frequency, +20 dB/decade after the break; phase 0\u00b0\u2192+90\u00b0.")


# =====================================================================
# Figure 5.14 - Bode plot for \u03c9n\u00b2/(s\u00b2+2\u03b6\u03c9n s+\u03c9n\u00b2)
# =====================================================================
def fig_5_14():
    o = []
    wn = 1.0
    _baxes(o, 30, 28, 200, 150, 0.1, 10, -40, 20, "Gain dB")
    for z, c in [(0.2, BLUE), (0.5, GOLD), (1.0, GREEN)]:
        def g(f, z=z):
            r = (1 - (f / wn) ** 2) ** 2 + (2 * z * f / wn) ** 2
            return -10 * math.log10(r)
        _bcurve(o, g, 30, 28, 200, 150, 0.1, 10, -40, 20, color=c, sw=1.2)
    o.append(tx(60, 44, "\u03b6=0.2", 6.5, color=BLUE))
    o.append(tx(60, 60, "\u03b6=0.5", 6.5, color=GOLD))
    o.append(tx(60, 76, "\u03b6=1.0", 6.5, color=GREEN))
    py0 = 28 + 150 + 34
    _baxes(o, 30, py0, 200, 150, 0.1, 10, -180, 0, "Phase \u00b0")
    for z, c in [(0.2, BLUE), (0.5, GOLD), (1.0, GREEN)]:
        def p(f, z=z):
            return -math.degrees(math.atan2(2 * z * f / wn, 1 - (f / wn) ** 2))
        _bcurve(o, p, 30, py0, 200, 150, 0.1, 10, -180, 0, color=c, sw=1.2)
    return _f(o, 250, 410,
              "Bode của \u03c9n\u00b2/(s\u00b2+2\u03b6\u03c9n s+\u03c9n\u00b2): lợi 0 dB rồi -40 dB/thập kỷ; pha 0\u00b0\u2192-180\u00b0, hình dạng phụ thuộc \u03b6 (đỉnh càng cao khi \u03b6 nhỏ).",
              "Bode plot for \u03c9n\u00b2/(s\u00b2+2\u03b6\u03c9n s+\u03c9n\u00b2): gain 0 dB then -40 dB/decade; phase 0\u00b0\u2192-180\u00b0, shape depending on \u03b6 (peak higher for small \u03b6).")


# =====================================================================
# Figure 5.15 - Example Bode plot, 100/(s\u00b2+4s+100)  (\u03c9n=10, \u03b6=0.2)
# =====================================================================
def fig_5_15():
    o = []
    wn, z = 10.0, 0.2
    def g(f):
        r = (1 - (f / wn) ** 2) ** 2 + (2 * z * f / wn) ** 2
        return 20 * math.log10(100) - 10 * math.log10(r)
    def p(f):
        return -math.degrees(math.atan2(2 * z * f / wn, 1 - (f / wn) ** 2))
    _bode2(o, 30, 28, 200, 70, 1, 1000, g, p, -40, 40, -180, 0)
    return _f(o, 250, 210,
              "Ví dụ Bode của 100/(s\u00b2+4s+100): \u03c9n=10 rad/s, \u03b6=0,2; lợi -40 dB/thập kỷ sau điểm gãy; sai số +8 dB tại điểm gãy.",
              "Example Bode plot for 100/(s\u00b2+4s+100): \u03c9n=10 rad/s, \u03b6=0.2; gain -40 dB/decade beyond the break, +8 dB error at the break.")


# =====================================================================
# Figure 5.16 - Composite Bode plot, 50(s+2)/(s(s+10))
# =====================================================================
def fig_5_16():
    o = []
    def g(f):
        # 50 * (1+s/2) / (s * (1+s/10))
        val = 50.0
        val *= math.sqrt(1 + (f / 2.0) ** 2) / (f) / math.sqrt(1 + (f / 10.0) ** 2)
        return 20 * math.log10(val)
    def p(f):
        a = math.degrees(math.atan(f / 2.0)) - 90 - math.degrees(math.atan(f / 10.0))
        return a
    _bode2(o, 30, 28, 200, 70, 0.1, 100, g, p, -40, 40, -180, 90)
    return _f(o, 250, 210,
              "Bode tổng hợp của 50(s+2)/[s(s+10)] = 10\u00d7(1+s/2)\u00d71/s\u00d71/(1+s/10); cộng lợi và góc pha của từng thành phần.",
              "Composite Bode plot for 50(s+2)/[s(s+10)] = 10\u00d7(1+s/2)\u00d71/s\u00d71/(1+s/10); sum the gains and phases of the elements.")


# =====================================================================
# Figure 5.17 - Example magnitude plot, K=10, break at 10 rad/s (denominator)
# =====================================================================
def fig_5_17():
    o = []
    def g(f):
        return 20 if f < 10 else 20 - 20 * math.log10(f / 10)
    _baxes(o, 30, 28, 200, 150, 0.1, 100, -40, 40, "Gain dB")
    _bcurve(o, g, 30, 28, 200, 150, 0.1, 100, -40, 40, color=BLUE, sw=1.5)
    return _f(o, 250, 200,
              "Ví dụ: đường lợi ban đầu 0 dốc, K=10 (20 dB), gãy -20 dB/thập kỳ tại 10 rad/s \u2192 G(s)=10/(1+0,1s).",
              "Example: initial zero slope, K=10 (20 dB), -20 dB/decade break at 10 rad/s \u2192 G(s)=10/(1+0.1s).")


# =====================================================================
# Figure 5.18 - Example magnitude plot with 1/s and two breaks
# =====================================================================
def fig_5_18():
    o = []
    def g(f):
        # K=2, 1/s, (1+s), (1+0.1s)
        v = 2.0 / f / math.sqrt(1 + f ** 2) / math.sqrt(1 + (0.1 * f) ** 2)
        return 20 * math.log10(v)
    _baxes(o, 30, 28, 200, 150, 0.1, 100, -40, 40, "Gain dB")
    _bcurve(o, g, 30, 28, 200, 150, 0.1, 100, -40, 40, color=BLUE, sw=1.5)
    return _f(o, 250, 200,
              "Ví dụ: dốc ban đầu -20 dB/thập kỷ (1/s), K=2, gãy tại 1 rad/s và 10 rad/s \u2192 2/[s(1+s)(1+0,1s)].",
              "Example: initial -20 dB/decade (1/s), K=2, breaks at 1 rad/s and 10 rad/s \u2192 2/[s(1+s)(1+0.1s)].")


# =====================================================================
# Figure 5.19 - Example magnitude plot, -40 dB/decade at 1 rad/s
# =====================================================================
def fig_5_19():
    o = []
    def g(f):
        return 10 if f < 1 else 10 - 40 * math.log10(f)
    _baxes(o, 30, 28, 200, 150, 0.1, 100, -40, 40, "Gain dB")
    _bcurve(o, g, 30, 28, 200, 150, 0.1, 100, -40, 40, color=BLUE, sw=1.5)
    # mark the true-plot peak near the break (+~4 dB)
    o.append(tx(60, 40, "+4 dB", 6.5, color=RED))
    return _f(o, 250, 200,
              "Ví dụ: lợi ban đầu 10 dB (K\u22483,2), gãy -40 dB/thập kỷ tại 1 rad/s, đỉnh thực cao hơn ~4 dB \u2192 \u03b6\u22480,3.",
              "Example: initial gain 10 dB (K\u22483.2), -40 dB/decade break at 1 rad/s, true plot peaks ~4 dB above \u2192 \u03b6\u22480.3.")


# =====================================================================
# Figure 5.20 - Closed-loop system (stability)
# =====================================================================
def fig_5_20():
    o = []
    o.append(sumj(90, 60, ["+", "", "-"]))
    o.append(ar(15, 60, 79, 60))
    o.append(ar(101, 60, 180, 60))
    o.append(bx(180, 38, 110, 44, "G(s)", fill="#eef3fb"))
    o.append(ar(290, 60, 345, 60))
    o.append(ar(345, 60, 345, 95, dash="4 3"))
    o.append(ar(345, 95, 90, 95, dash="4 3"))
    o.append(ar(90, 95, 90, 71))
    o.append(bx(345, 38, 60, 44, "H(s)", fill="#eef3fb"))
    o.append(ar(305, 60, 345, 60))
    o.append(tx(8, 54, "Input", 6.8, anchor="start"))
    o.append(tx(353, 56, "Output", 6.8, anchor="start"))
    return _f(o, 430, 130,
              "Hệ vòng kín: tín hiệu sai lệch đi qua G(s), đầu ra phản hồi qua H(s) rồi trừ vào đầu vào.",
              "Closed-loop system: the error passes through G(s), the output is fed back through H(s) and subtracted from the input.")


# =====================================================================
# Figure 5.21 - Self-sustaining oscillation (input, fed-back, error)
# =====================================================================
def fig_5_21():
    o = []
    x0, y0, W, H = 20, 30, 120, 70
    o.append(tx(x0 + W / 2, 16, "(a) input", 6.8))
    o.append(_axes(x0, y0, W, H, "", ""))
    o.append(_curve(lambda t: 0.5 + 0.4 * (1 if (t % 2) < 1 else 0), x0, y0, W, H, xr=(0, 4), yr=(0, 1), color=BLUE, sw=1.2))
    x1 = 175
    o.append(tx(x1 + W / 2, 16, "(b) fed back", 6.8))
    o.append(_axes(x1, y0, W, H, "", ""))
    o.append(_curve(lambda t: 0.5 + 0.4 * (1 if (t % 2) < 1 else 0), x1, y0, W, H, xr=(0, 4), yr=(0, 1), color=RED, sw=1.2))
    x2 = 330
    o.append(tx(x2 + W / 2, 16, "(c) error", 6.8))
    o.append(_axes(x2, y0, W, H, "", ""))
    o.append(_curve(lambda t: 0.5 + 0.4 * (1 if (t % 2) < 1 else 0), x2, y0, W, H, xr=(0, 4), yr=(0, 1), color=GREEN, sw=1.2))
    return _f(o, 470, 120,
              "Dao động tự duy trì: tín hiệu đầu vào nửa chu kỳ được phản hồi về đúng thời điểm tiếp tục tín hiệu (hệ ở biên ổn định).",
              "Self-sustaining oscillation: the half-cycle input is fed back just in time to continue the signal (marginally stable).")


# =====================================================================
# Figure 5.22 - Stable system (input, fed-back decaying, error decaying)
# =====================================================================
def fig_5_22():
    o = []
    x0, y0, W, H = 20, 30, 120, 70
    o.append(tx(x0 + W / 2, 16, "(a) input", 6.8))
    o.append(_axes(x0, y0, W, H, "", ""))
    o.append(_curve(lambda t: 0.5 + 0.4 * (1 if (t % 2) < 1 else 0), x0, y0, W, H, xr=(0, 4), yr=(0, 1), color=BLUE, sw=1.2))
    x1 = 175
    o.append(tx(x1 + W / 2, 16, "(b) fed back", 6.8))
    o.append(_axes(x1, y0, W, H, "", ""))
    o.append(_curve(lambda t: 0.5 + 0.4 * math.exp(-0.6 * t) * (1 if (t % 2) < 1 else 0), x1, y0, W, H, xr=(0, 4), yr=(0, 1), color=RED, sw=1.2))
    x2 = 330
    o.append(tx(x2 + W / 2, 16, "(c) error", 6.8))
    o.append(_axes(x2, y0, W, H, "", ""))
    o.append(_curve(lambda t: 0.5 + 0.4 * math.exp(-0.6 * t) * (1 if (t % 2) < 1 else 0), x2, y0, W, H, xr=(0, 4), yr=(0, 1), color=GREEN, sw=1.2))
    return _f(o, 470, 120,
              "Hệ ổn định: tín hiệu phản hồi có biên độ nhỏ hơn đầu vào nên dao động tắt dần theo thời gian.",
              "Stable system: the fed-back signal has smaller amplitude than the input, so the oscillation dies away with time.")


# =====================================================================
# Figure 5.23 - Unstable system (input, fed-back growing, error growing)
# =====================================================================
def fig_5_23():
    o = []
    x0, y0, W, H = 20, 30, 120, 70
    o.append(tx(x0 + W / 2, 16, "(a) input", 6.8))
    o.append(_axes(x0, y0, W, H, "", ""))
    o.append(_curve(lambda t: 0.5 + 0.4 * (1 if (t % 2) < 1 else 0), x0, y0, W, H, xr=(0, 4), yr=(0, 1), color=BLUE, sw=1.2))
    x1 = 175
    o.append(tx(x1 + W / 2, 16, "(b) fed back", 6.8))
    o.append(_axes(x1, y0, W, H, "", ""))
    o.append(_curve(lambda t: 0.5 + 0.4 * math.exp(0.3 * t) * (1 if (t % 2) < 1 else 0), x1, y0, W, H, xr=(0, 4), yr=(0, 1), color=RED, sw=1.2))
    x2 = 330
    o.append(tx(x2 + W / 2, 16, "(c) error", 6.8))
    o.append(_axes(x2, y0, W, H, "", ""))
    o.append(_curve(lambda t: 0.5 + 0.4 * math.exp(0.3 * t) * (1 if (t % 2) < 1 else 0), x2, y0, W, H, xr=(0, 4), yr=(0, 1), color=GREEN, sw=1.2))
    return _f(o, 470, 120,
              "Hệ không ổn định: tín hiệu phản hồi có biên độ lớn hơn đầu vào nên dao động tăng dần.",
              "Unstable system: the fed-back signal has larger amplitude than the input, so the oscillation grows with time.")


# =====================================================================
# Figure 5.25 - Stability and Bode plots (margins)
# =====================================================================
def fig_5_25():
    o = []
    def g(f):
        return 20 - 20 * math.log10(f) if f < 1 else 20 * math.log10(1.0 / f) - 0  # simple -20 slope through 0 dB at f=1
    # simpler: gain = 10*log10(100/(1+(f)^2))? keep illustrative
    def g2(f):
        return 12 - 20 * math.log10(f)
    def p2(f):
        return -180 * f / (f + 0.5)
    _bode2(o, 30, 28, 200, 70, 0.1, 100, g2, p2, -40, 40, -180, 0)
    # mark 0 dB and -180 reference lines
    return _f(o, 250, 210,
              "Các thông số ổn định trên Bode: tần số cắt lợi (gain crossover), tần số cắt pha (phase crossover), dự trữ lợi và dự trữ pha.",
              "Stability parameters on a Bode plot: gain crossover, phase crossover, gain margin and phase margin.")


# =====================================================================
# Figure 5.26 - (a) stable, (b) unstable Bode plots
# =====================================================================
def fig_5_26():
    o = []
    o.append(tx(120, 14, "(a) stable", 7))
    _bode2(o, 30, 28, 200, 60, 0.1, 100,
            lambda f: 12 - 20 * math.log10(f), lambda f: -90 - 90 * f / (f + 2), -40, 40, -180, 0)
    o.append(tx(340, 14, "(b) unstable", 7))
    _bode2(o, 250, 28, 200, 60, 0.1, 100,
            lambda f: 24 - 20 * math.log10(f), lambda f: -90 - 90 * f / (f + 2), -40, 50, -180, 0)
    return _f(o, 470, 200,
              "(a) Hệ ổn định: lợi < 0 dB (1) khi pha = -180\u00b0. (b) Hệ không ổn định: lợi > 0 dB (>1) khi pha = -180\u00b0.",
              "(a) Stable: gain < 0 dB (1) when phase = -180\u00b0. (b) Unstable: gain > 0 dB (>1) when phase = -180\u00b0.")


# =====================================================================
# Figure 5.27 - Example Bode plot
# =====================================================================
def fig_5_27():
    o = []
    _bode2(o, 30, 28, 200, 70, 0.1, 100,
            lambda f: 8 - 20 * math.log10(f), lambda f: -90 - 60 * f / (f + 1), -40, 40, -180, 0)
    return _f(o, 250, 210,
              "Ví dụ Bode: hệ ổn định, dự trữ lợi ~12 dB, dự trữ pha ~30\u00b0.",
              "Example Bode plot: stable system, gain margin ~12 dB, phase margin ~30\u00b0.")


# =====================================================================
# Figure 5.28 - Cascade compensation block diagram
# =====================================================================
def fig_5_28():
    o = []
    o.append(bx(20, 45, 110, 44, "Compensator", fill="#eef3fb"))
    o.append(ar(10, 67, 20, 67))
    o.append(ar(130, 67, 190, 67))
    o.append(bx(190, 45, 110, 44, "System", fill="#eef3fb"))
    o.append(ar(300, 67, 360, 67))
    o.append(tx(6, 61, "Input", 6.8, anchor="start"))
    o.append(tx(368, 61, "Output", 6.8, anchor="start"))
    return _f(o, 410, 110,
              "Bộ bù (compensator) đặt nối tiếp trong đường truyền thuận để cải thiện đặc tính vòng kín.",
              "A compensator placed in cascade in the forward path to improve the closed-loop performance.")


# =====================================================================
# Figure 5.29 - Adjusting performance by introducing gain
# =====================================================================
def fig_5_29():
    o = []
    o.append(bx(20, 45, 90, 44, "Gain", fill="#eef3fb"))
    o.append(ar(10, 67, 20, 67))
    o.append(ar(110, 67, 170, 67))
    o.append(bx(170, 45, 110, 44, "System", fill="#eef3fb"))
    o.append(ar(280, 67, 360, 67))
    o.append(tx(6, 61, "Input", 6.8, anchor="start"))
    o.append(tx(368, 61, "Output", 6.8, anchor="start"))
    return _f(o, 410, 110,
              "Điều chỉnh đặc tính hệ bằng cách đổi lợi trong đường truyền thuận; tăng lợi sẽ đẩy điểm cắt 0 dB lên tần số cao hơn, giảm độ ổn định.",
              "Adjusting system performance by changing the forward-path gain; increasing gain shifts the 0 dB crossing to higher frequency, reducing stability.")


# =====================================================================
# Figure 5.30 - Effect of increasing the gain
# =====================================================================
def fig_5_30():
    o = []
    _bode2(o, 30, 28, 200, 70, 0.1, 100,
            lambda f: 4 - 20 * math.log10(f),
            lambda f: -90 - 60 * f / (f + 1), -40, 40, -180, 0)
    # draw two gain curves
    _bcurve(o, lambda f: 4 - 20 * math.log10(f), 30, 28, 200, 70, 0.1, 100, -40, 40, color=BLUE, sw=1.3)
    _bcurve(o, lambda f: 14 - 20 * math.log10(f), 30, 28, 200, 70, 0.1, 100, -40, 40, color=GOLD, sw=1.3)
    return _f(o, 250, 210,
              "Tăng lợi dịch chuyển đường lợi lên trên (vàng), điểm cắt 0 dB sang phải, dự trữ pha và dự trữ lợi giảm \u2192 hệ kém ổn định hơn.",
              "Increasing gain shifts the gain plot upward (gold); the 0 dB crossing moves right, reducing phase and gain margins \u2192 less stable.")


# =====================================================================
# Figure 5.31 - Example Bode plot
# =====================================================================
def fig_5_31():
    o = []
    _bode2(o, 30, 28, 200, 70, 0.1, 100,
            lambda f: 2 - 20 * math.log10(f), lambda f: -180 + 45 * f / (f + 2), -40, 40, -180, 0)
    return _f(o, 250, 210,
              "Ví dụ Bode: dự trữ pha 35\u00b0; muốn dự trữ pha 45\u00b0 cần giảm lợi khoảng 2 dB.",
              "Example Bode plot: phase margin 35\u00b0; to reach 45\u00b0 the gain must be reduced by about 2 dB.")


# =====================================================================
# Figure 5.32 - Phase-lead compensator circuit
# =====================================================================
def fig_5_32():
    o = []
    # simple RC lead network: Vin --R1--+--R2-- Vout ; C from node to ground
    x = 40
    y = 70
    o.append(_line(x, y, x + 40, y, color=INK, sw=1.2))
    o.append(_line(x + 40, y, x + 40, y - 30, color=INK, sw=1.2))
    o.append(_line(x + 40, y - 30, x + 110, y - 30, color=INK, sw=1.2))
    o.append(_line(x + 110, y - 30, x + 110, y, color=INK, sw=1.2))
    o.append(_line(x + 110, y, x + 150, y, color=INK, sw=1.2))
    o.append(_line(x + 40, y, x + 40, y + 30, color=INK, sw=1.2))
    o.append(_circle(x + 40, y + 40, 12, fill="none", color=INK, sw=1.0))  # capacitor plates
    o.append(_line(x + 40, y + 30, x + 40, y + 40 - 12, color=INK, sw=1.0))
    o.append(_line(x + 40, y + 40 + 12, x + 40, y + 60, color=INK, sw=1.0))
    o.append(tx(x + 10, y - 6, "R1", 6.5))
    o.append(tx(x + 75, y - 6, "R2", 6.5))
    o.append(tx(x + 48, y + 50, "C", 6.5))
    o.append(tx(x - 6, y - 4, "Vin", 6.8, anchor="end"))
    o.append(tx(x + 156, y - 4, "Vout", 6.8, anchor="start"))
    return _f(o, 210, 120,
              "Mạch bù sớm pha (phase-lead): trở R1, R2 và tụ C; a=(R1+R2)/R2, \u03c4=R1R2C/(R1+R2).",
              "Phase-lead compensator circuit: resistors R1, R2 and capacitor C; a=(R1+R2)/R2, \u03c4=R1R2C/(R1+R2).")


# =====================================================================
# Figure 5.33 - Bode plot for a phase-lead compensator
# =====================================================================
def fig_5_33():
    o = []
    a, tau = 5.0, 1.0
    def g(f):
        num = math.sqrt(1 + (a * f * tau) ** 2)
        den = math.sqrt(1 + (f * tau) ** 2)
        return 20 * math.log10(num / den)
    def p(f):
        return math.degrees(math.atan(a * f * tau)) - math.degrees(math.atan(f * tau))
    _bode2(o, 30, 28, 200, 70, 0.1, 100, g, p, -40, 40, -90, 90)
    return _f(o, 250, 210,
              "Bode của bộ bù sớm pha (1+a\u03c4s)/(1+\u03c4s), a>1: lợi tăng +20 dB/thập kỷ ở giữa, pha dương (đỉnh tại tần số gãy hình học).",
              "Bode plot for a phase-lead compensator (1+a\u03c4s)/(1+\u03c4s), a>1: gain rises +20 dB/decade in the middle, positive phase (peak at the geometric mean break).")


# =====================================================================
# Figure 5.34 - Bode plot for uncompensated 10/s\u00b2
# =====================================================================
def fig_5_34():
    o = []
    def g(f):
        return 20 * math.log10(10) - 40 * math.log10(f)
    def p(f):
        return -180
    _bode2(o, 30, 28, 200, 70, 0.1, 100, g, p, -80, 40, -180, 0)
    return _f(o, 250, 210,
              "Bode của hệ chưa bù 10/s\u00b2: lợi dốc -40 dB/thập kỷ, pha không đổi -180\u00b0.",
              "Bode plot for the uncompensated system 10/s\u00b2: gain slope -40 dB/decade, constant phase -180\u00b0.")


# =====================================================================
# Figure 5.35 - Phase-lag compensator circuit
# =====================================================================
def fig_5_35():
    o = []
    x, y = 40, 70
    o.append(_line(x, y, x + 40, y, color=INK, sw=1.2))
    o.append(_line(x + 40, y, x + 40, y - 30, color=INK, sw=1.2))
    o.append(_line(x + 40, y - 30, x + 110, y - 30, color=INK, sw=1.2))
    o.append(_line(x + 110, y - 30, x + 110, y, color=INK, sw=1.2))
    o.append(_line(x + 110, y, x + 150, y, color=INK, sw=1.2))
    o.append(_line(x + 40, y, x + 40, y + 30, color=INK, sw=1.2))
    o.append(_line(x + 40, y + 30, x + 40, y + 60, color=INK, sw=1.2))
    o.append(_line(x + 40, y + 60, x + 60, y + 60, color=INK, sw=1.0))
    o.append(tx(x + 10, y - 6, "R1", 6.5))
    o.append(tx(x + 75, y - 6, "R2", 6.5))
    o.append(tx(x + 30, y + 72, "C", 6.5))
    o.append(tx(x - 6, y - 4, "Vin", 6.8, anchor="end"))
    o.append(tx(x + 156, y - 4, "Vout", 6.8, anchor="start"))
    return _f(o, 210, 120,
              "Mạch bù trễ pha (phase-lag): a>1, \u03c4=R2C; đầu ra lấy sau tụ.",
              "Phase-lag compensator circuit: a>1, \u03c4=R2C; output taken after the capacitor.")


# =====================================================================
# Figure 5.36 - Bode plot for a phase-lag compensator
# =====================================================================
def fig_5_36():
    o = []
    a, tau = 5.0, 1.0
    def g(f):
        num = math.sqrt(1 + (f * tau) ** 2)
        den = math.sqrt(1 + (a * f * tau) ** 2)
        return 20 * math.log10(num / den)
    def p(f):
        return math.degrees(math.atan(f * tau)) - math.degrees(math.atan(a * f * tau))
    _bode2(o, 30, 28, 200, 70, 0.1, 100, g, p, -40, 20, -90, 0)
    return _f(o, 250, 210,
              "Bode của bộ bù trễ pha (1+\u03c4s)/(1+a\u03c4s), a>1: lợi giảm -20 dB/thập kỷ, pha âm.",
              "Bode plot for a phase-lag compensator (1+\u03c4s)/(1+a\u03c4s), a>1: gain falls -20 dB/decade, negative phase.")


# =====================================================================
# Figure 5.37 - Example Bode plot (phase-lag design)
# =====================================================================
def fig_5_37():
    o = []
    _bode2(o, 30, 28, 200, 70, 0.1, 100,
            lambda f: 20 - 20 * math.log10(f), lambda f: -90 - 60 * f / (f + 1), -40, 40, -180, 0)
    return _f(o, 250, 210,
              "Ví dụ Bode để thiết kế bộ bù trễ pha: chọn tần số cắt mới có dự trữ pha 40\u00b0, tính a từ lợi cần giảm.",
              "Example Bode plot for phase-lag design: pick the new crossover with 40\u00b0 phase margin and determine a from the required gain drop.")


# =====================================================================
# Figure 5.38 - Problem 6: five Bode gain plots (a)-(e)
# =====================================================================
def fig_5_38():
    o = []
    panels = [
        ("(a)", lambda f: 0.0, 0.1, 100, 0, 30),
        ("(b)", lambda f: 20 - 20 * math.log10(f) if f >= 1 else 20, 0.1, 100, -40, 30),
        ("(c)", lambda f: 20 - 40 * math.log10(f) if f >= 1 else 20, 0.1, 100, -60, 30),
        ("(d)", lambda f: -20 - 20 * math.log10(f), 0.1, 100, -60, 10),
        ("(e)", lambda f: 10 - 40 * math.log10(f) if f >= 1 else 10, 0.1, 100, -60, 30),
    ]
    for i, (lab, g, fmin, fmax, vmin, vmax) in enumerate(panels):
        cx = 20 + (i % 3) * 155
        cy = 20 + (i // 3) * 175
        if i == 3:
            cx = 20 + 1 * 155
        if i == 4:
            cx = 20 + 2 * 155
        o.append(tx(cx + 60, cy - 4, lab, 7))
        _baxes(o, cx, cy, 120, 140, fmin, fmax, vmin, vmax, "Gain dB")
        _bcurve(o, g, cx, cy, 120, 140, fmin, fmax, vmin, vmax, color=BLUE, sw=1.3)
    return _f(o, 500, 360,
              "Bài tập 6: xác định hàm truyền từ các đường lợi Bode (a)–(e) dựa vào độ dốc và tần số gãy.",
              "Problem 6: determine the transfer functions from the Bode gain plots (a)–(e) using the slopes and break frequencies.")


# =====================================================================
# Figure 5.39 - Problem 9: Bode plot
# =====================================================================
def fig_5_39():
    o = []
    _bode2(o, 30, 28, 200, 70, 0.1, 100,
            lambda f: 24 - 20 * math.log10(f), lambda f: -90 - 90 * f / (f + 3), -40, 40, -180, 0)
    return _f(o, 250, 210,
              "Bài tập 9: từ Bode xác định (a) ổn định không, (b) dự trữ lợi, (c) dự trữ pha.",
              "Problem 9: from the Bode plot determine (a) stability, (b) gain margin, (c) phase margin.")


# =====================================================================
# Figure 5.40 - Problem 12: Bode plot
# =====================================================================
def fig_5_40():
    o = []
    _bode2(o, 30, 28, 200, 70, 0.1, 100,
            lambda f: 4 - 20 * math.log10(f), lambda f: -90 - 60 * f / (f + 1), -40, 40, -180, 0)
    return _f(o, 250, 210,
              "Bài tập 12: hệ có dự trữ pha 10\u00b0; tính mức thay đổi lợi để đạt dự trữ pha 40\u00b0.",
              "Problem 12: the system has phase margin 10\u00b0; determine the gain change needed to reach a 40\u00b0 phase margin.")


FIGS = {n: globals()[n] for n in dir() if n.startswith("fig_")}
