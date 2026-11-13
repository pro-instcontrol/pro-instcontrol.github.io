# -*- coding: utf-8 -*-
"""Vector figures for Bolton *Control Systems* (Newnes, 2002), Chapter 4.

Every figure is redrawn as a clean vector so it stays legible on a phone,
matching the standard used for the Practical Process Control and SIS readers.
Each function returns (svg, caption_vi, caption_en, aria_vi, aria_en).

Re-uses the shared primitives in `vfig`; the small block-diagram composer
helpers below mirror those in boltonfig.py / boltonfig2.py.
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


def wire(o, pts, dash="", color=INK):
    for i in range(len(pts) - 1):
        o.append(ln(pts[i][0], pts[i][1], pts[i + 1][0], pts[i + 1][1], dash=dash, color=color))


# second-order unit step response y(t), natural angular frequency wn, damping zeta
def _step(t, zeta, wn=1.0):
    if zeta >= 1:
        if zeta == 1:
            return 1 - math.exp(-wn * t) * (1 + wn * t)
        sd = math.sqrt(zeta * zeta - 1) * wn
        return 1 - math.exp(-zeta * wn * t) * (math.cosh(sd * t) + zeta * wn / sd * math.sinh(sd * t))
    wd = wn * math.sqrt(1 - zeta * zeta)
    return 1 - math.exp(-zeta * wn * t) * (math.cos(wd * t) + (zeta / math.sqrt(1 - zeta * zeta)) * math.sin(wd * t))


# draw an s-plane (cross axes) with X marks at the given poles
def _splane(o, x0, y0, W, H, poles, label="", shade=False):
    scale = W / 8.0  # 2 units to each side
    if shade:
        o.append(_rect(x0, y0 - H / 2, W / 2, H, fill="#e8f3ea", sw=0))
    o.append(ln(x0, y0, x0 + W - 4, y0))
    o.append(_arrow(x0 + W - 4, y0, x0 + W, y0, sw=1))
    o.append(ln(x0 + W / 2, y0 + H / 2, x0 + W / 2, y0 - H / 2 + 4))
    o.append(_arrow(x0 + W / 2, y0 - H / 2 + 4, x0 + W / 2, y0 - H / 2, sw=1))
    o.append(tx(x0 + W - 3, y0 + 12, "Real", 6.5, anchor="end", color=GREY))
    o.append(tx(x0 + W / 2 + 6, y0 - H / 2 + 2, "Imag.", 6.5, anchor="start", color=GREY))
    if label:
        o.append(tx(x0 + W / 2, y0 + H / 2 + 15, label, 7, anchor="middle"))
    for (re, im) in poles:
        px = x0 + W / 2 + re * scale
        py = y0 - im * scale
        o.append(ln(px - 4, py - 4, px + 4, py + 4, color=RED, sw=1.4))
        o.append(ln(px - 4, py + 4, px + 4, py - 4, color=RED, sw=1.4))


# =====================================================================
# Figure 4.1 - Spring system step response with overshoot
# =====================================================================
def fig_4_1():
    o = []
    x0, y0, W, H = 50, 40, 320, 170
    o.append(_axes(x0, y0, W, H, "Time", "Output"))
    o.append(_curve(lambda t: _step(t, 0.3, 1.0), x0, y0, W, H, xr=(0, 9), yr=(0, 1.25), color=BLUE, sw=1.5))
    py = y0 + H - 1.0 / 1.25 * H
    o.append(ln(x0, py, x0 + W, py, color=GREY, sw=0.7, dash="4 3"))
    o.append(tx(x0 + W - 2, py - 5, "Steady state", 7, anchor="end", color=GREY))
    tp = 3.29
    yp = _step(tp, 0.3, 1.0)
    px = x0 + tp / 9.0 * W
    ppy = y0 + H - yp / 1.25 * H
    o.append(ln(px, ppy, px, y0 + H, color=GREY, sw=0.6, dash="2 3"))
    o.append(tx(px, ppy - 6, "Overshoot", 7, anchor="middle", color=RED))
    o.append(tx(x0 + W / 2, y0 + H + 16, "Time", 7.5))
    return _f(o, 420, 235,
              "Đáp ứng của hệ lò xo (hệ bậc hai giảm chấn kém) với đầu vào bậc: mất một thời gian để đạt giá trị xác lập và bị vượt quá trước khi dừng lại.",
              "A spring system (an under-damped second-order system) with a step input: it takes time to reach the steady state value and overshoots before settling.")


# =====================================================================
# Figure 4.2 - Step response of an under-damped system (annotated)
# =====================================================================
def fig_4_2():
    o = []
    x0, y0, W, H = 55, 45, 330, 180
    o.append(_axes(x0, y0, W, H, "Time", "Output"))
    o.append(_curve(lambda t: _step(t, 0.3, 1.0), x0, y0, W, H, xr=(0, 12), yr=(0, 1.25), color=BLUE, sw=1.5))
    yss = y0 + H - 1.0 / 1.25 * H
    o.append(ln(x0, yss, x0 + W, yss, color=GREY, sw=0.6, dash="4 3"))
    # rise time: first crossing of steady state
    tr = 3.29
    prx = x0 + tr / 12.0 * W
    o.append(ln(prx, yss, prx, y0 + H, color=GREY, sw=0.5, dash="2 3"))
    o.append(tx(prx, y0 + H + 12, "Rise time", 6.5, anchor="middle", color=GREY))
    # peak time
    tp = math.pi / (1.0 * math.sqrt(1 - 0.09))
    ypk = _step(tp, 0.3, 1.0)
    ppx = x0 + tp / 12.0 * W
    ppy = y0 + H - ypk / 1.25 * H
    o.append(ln(ppx, ppy, ppx, yss, color=RED, sw=0.6, dash="2 3"))
    o.append(tx(ppx + 4, (ppy + yss) / 2, "Overshoot", 6.5, anchor="start", color=RED))
    o.append(tx(ppx, ppy - 6, "Peak time", 6.5, anchor="middle", color=RED))
    # settling time (2%)
    ts = 4.0 / (0.3 * 1.0)
    psx = x0 + ts / 12.0 * W
    o.append(ln(psx, yss - 6, psx, yss + 10, color=GREEN, sw=0.8))
    o.append(tx(psx, y0 + H + 12, "Settling time", 6.5, anchor="middle", color=GREEN))
    o.append(tx(x0 + W / 2, y0 + H + 28, "Time", 7.5))
    return _f(o, 440, 260,
              "Đáp ứng bậc của hệ giảm chấn kém, minh họa thời gian trỗi (rise time), thời gian đạt đỉnh (peak time), độ vượt (overshoot) và thời gian xác lập (settling time).",
              "Step response of an under-damped system, showing the rise time, peak time, overshoot and settling time.")


# =====================================================================
# Figure 4.3 - Effect of natural angular frequency (same damping factor)
# =====================================================================
def fig_4_3():
    o = []
    # (a) low natural frequency
    ax, ay, W, H = 30, 30, 180, 150
    o.append(tx(ax + W / 2, ay - 6, "(a)  \u03c9n = 1 rad/s", 7, anchor="middle"))
    o.append(_axes(ax, ay, W, H, "Time", "Output"))
    o.append(_curve(lambda t: _step(t, 0.2, 1.0), ax, ay, W, H, xr=(0, 14), yr=(0, 1.2), color=BLUE, sw=1.4))
    o.append(tx(ax + W / 2, ay + H + 16, "Time in seconds", 6.5))
    # (b) high natural frequency
    bx_, by, W2, H2 = 250, 30, 180, 150
    o.append(tx(bx_ + W2 / 2, by - 6, "(b)  \u03c9n = 10 rad/s", 7, anchor="middle"))
    o.append(_axes(bx_, by, W2, H2, "Time", ""))
    o.append(_curve(lambda t: _step(t, 0.2, 10.0), bx_, by, W2, H2, xr=(0, 2), yr=(0, 1.2), color=BLUE, sw=1.4))
    o.append(tx(bx_ + W2 / 2, by + H2 + 16, "Time in seconds", 6.5))
    return _f(o, 440, 210,
              "Đáp ứng của hệ bậc hai hệ số khuyếch đại đơn vị với đầu vào bậc đơn vị, tỷ số giảm chấn như nhau (0,2): (a) tần số góc tự nhiên nhỏ phản ứng chậm, (b) tần số góc tự nhiên lớn phản ứng nhanh.",
              "Response of a unit-gain second-order system to a unit step input with the same damping factor (0.2): (a) a small natural angular frequency gives a slow response, (b) a large one gives a fast response.")


# =====================================================================
# Figure 4.4 - Effect of damping factor (same natural angular frequency)
# =====================================================================
def fig_4_4():
    o = []
    x0, y0, W, H = 60, 40, 320, 180
    o.append(_axes(x0, y0, W, H, "Time", "Output"))
    o.append(_curve(lambda t: _step(t, 0.3, 1.0), x0, y0, W, H, xr=(0, 3), yr=(0, 1.2), color=BLUE, sw=1.4))
    o.append(_curve(lambda t: _step(t, 0.7, 1.0), x0, y0, W, H, xr=(0, 3), yr=(0, 1.2), color=RED, sw=1.4))
    o.append(tx(x0 + 8, y0 + 14, "\u03b6 = 0.3 (vượt quá)", 6.5, anchor="start", color=BLUE))
    o.append(tx(x0 + 8, y0 + 28, "\u03b6 = 0.7 (trì trệ)", 6.5, anchor="start", color=RED))
    o.append(tx(x0 + W / 2, y0 + H + 16, "Time in seconds", 7))
    return _f(o, 440, 245,
              "Đáp ứng của hệ bậc hai hệ số khuyếch đại đơn vị với đầu vào bậc đơn vị, tần số góc tự nhiên như nhau: tỷ số giảm chấn nhỏ (0,3) gây vượt quá, tỷ số lớn (0,7) làm hệ trì trệ.",
              "Response of a unit-gain second-order system to a unit step input with the same natural angular frequency: a small damping factor (0.3) gives overshoot, a large one (0.7) gives a sluggish response.")


# =====================================================================
# Figure 4.5 - Feedback system (forward path K/[s(s+a)], feedback 1)
# =====================================================================
def fig_4_5():
    o = []
    o.append(sumj(95, 60, ["+", "", "-"]))
    o.append(ar(18, 60, 84, 60))
    o.append(ar(106, 60, 185, 60))
    o.append(bx(185, 38, 130, 44, "K/[s(s+a)]"))
    o.append(ar(315, 60, 370, 60))
    o.append(ar(370, 60, 370, 95, dash="4 3"))
    o.append(ar(370, 95, 95, 95, dash="4 3"))
    o.append(ar(95, 95, 95, 71))
    o.append(tx(8, 54, "Input", 6.8, anchor="start"))
    o.append(tx(8, 64, "signal", 6.8, anchor="start"))
    o.append(tx(378, 56, "Output", 6.8, anchor="start"))
    o.append(tx(378, 66, "signal", 6.8, anchor="start"))
    o.append(tx(242, 90, "Feedback", 6.3, anchor="middle", color=GREY))
    o.append(tx(248, 32, "G(s)", 6.5, anchor="middle", color=GREY))
    return _f(o, 430, 130,
              "Hệ phản hồi với đường truyền thuận G(s) = K/[s(s+a)] và đường phản hồi H(s) = 1; tín hiệu sai lệch được đưa vào khối truyền thuận.",
              "Feedback system with a forward path G(s) = K/[s(s+a)] and a feedback path H(s) = 1; the error signal is fed to the forward path.")


# =====================================================================
# Figure 4.6 - Poles at -1 and -2 (stable)
# =====================================================================
def fig_4_6():
    o = []
    _splane(o, 120, 120, 200, 170, [(-1, 0), (-2, 0)], "Poles at -1 and -2")
    return _f(o, 440, 235,
              "Mặt phẳng s với các cực tại -1 và -2 (hệ ổn định, quá giảm chấn).",
              "The s-plane with poles at -1 and -2 (a stable, overdamped system).")


# =====================================================================
# Figure 4.7 - Poles at +1 and +2 (unstable)
# =====================================================================
def fig_4_7():
    o = []
    _splane(o, 120, 120, 200, 170, [(1, 0), (2, 0)], "Poles at +1 and +2")
    return _f(o, 440, 235,
              "Mặt phẳng s với các cực tại +1 và +2 (hệ không ổn định).",
              "The s-plane with poles at +1 and +2 (an unstable system).")


# =====================================================================
# Figure 4.8 - Pole at -1 + j1.73 (stable, complex)
# =====================================================================
def fig_4_8():
    o = []
    _splane(o, 120, 120, 200, 170, [(-1, 1.73)], "Pole at -1 + j1.73")
    return _f(o, 440, 235,
              "Mặt phẳng s với cực tại -1 + j1,73 (hệ ổn định, giảm chấn kém, dao động).",
              "The s-plane with a pole at -1 + j1.73 (a stable, under-damped, oscillatory system).")


# =====================================================================
# Figure 4.9 - Pole at +1 + j1.73 (unstable, complex)
# =====================================================================
def fig_4_9():
    o = []
    _splane(o, 120, 120, 200, 170, [(1, 1.73)], "Pole at +1 + j1.73")
    return _f(o, 440, 235,
              "Mặt phẳng s với cực tại +1 + j1,73 (hệ không ổn định, dao động tăng biên độ).",
              "The s-plane with a pole at +1 + j1.73 (an unstable, growing-amplitude oscillatory system).")


# =====================================================================
# Figure 4.10 - Double pole at -1 (critical damping)
# =====================================================================
def fig_4_10():
    o = []
    _splane(o, 120, 120, 200, 170, [(-1, 0)], "Double pole at -1", )
    o.append(tx(220, 120, "(double)", 6.8, anchor="start", color=RED))
    return _f(o, 440, 235,
              "Mặt phẳng s với cực kép tại -1 (giảm chấn tới hạn).",
              "The s-plane with a double pole at -1 (critically damped).")


# =====================================================================
# Figure 4.11 - s-plane: stability when poles are in the left half
# =====================================================================
def fig_4_11():
    o = []
    _splane(o, 120, 130, 200, 180, [(-1, 0.8), (-1.5, -0.5)], "Stability when poles lie in the left half", shade=True)
    o.append(tx(170, 130, "Stable\nregion", 7, anchor="middle", color=GREEN))
    return _f(o, 440, 250,
              "Mặt phẳng s: một hệ ổn định khi tất cả các cực nằm ở nửa trái (vùng được tô).",
              "The s-plane: a system is stable when all its poles lie in the left half (the shaded region).")


# =====================================================================
# Figure 4.12 - Pole location and the resulting transient
# =====================================================================
def fig_4_12():
    o = []
    # s-plane on the left
    _splane(o, 30, 120, 180, 170, [(-1.5, 0), (-1, 1), (1, 1)], "")
    o.append(tx(120, 218, "s-plane", 7, anchor="middle"))
    # three transient sketches on the right
    def mini(cx, cy, fn, lab, color):
        w, h = 110, 70
        o.append(_axes(cx, cy, w, h, "", ""))
        o.append(_curve(fn, cx, cy, w, h, xr=(0, 4), yr=(0, 1.25), color=color, sw=1.3))
        o.append(tx(cx + w / 2, cy + h + 12, lab, 6.5, anchor="middle"))
    mini(250, 40, lambda t: 1 - math.exp(-t), "(a) real negative pole", BLUE)
    mini(250, 130, lambda t: _step(t, 0.3, 1.0), "(b) complex left-half pole", RED)
    mini(250, 220, lambda t: 1 + math.exp(0.3 * t) * math.sin(t), "(c) complex right-half pole", GREEN)
    o.append(tx(120, 250, "Hình 4.12  Mỗi dao động bắt nguồn từ một cặp cực a + jb", 6.5, anchor="middle", color=GREY))
    return _f(o, 400, 270,
              "Mối quan hệ giữa vị trí cực và dạng quá trình quá độ: (a) cực thực âm gây đáp ứng tắt dần, (b) cực phức nửa trái gây dao động tắt dần, (c) cực phức nửa phải gây dao động tăng biên độ.",
              "Relationship between pole location and the resulting transient: (a) a real negative pole gives a decaying response, (b) a complex left-half pole gives a decaying oscillation, (c) a complex right-half pole gives a growing oscillation.")


# =====================================================================
# Figure 4.13 - Problem 6: feedback system
# =====================================================================
def fig_4_13():
    o = []
    o.append(sumj(95, 60, ["+", "", "-"]))
    o.append(ar(18, 60, 84, 60))
    o.append(ar(106, 60, 185, 60))
    o.append(bx(185, 38, 130, 44, "K/[s(s+2)]"))
    o.append(ar(315, 60, 370, 60))
    o.append(ar(370, 60, 370, 95, dash="4 3"))
    o.append(ar(370, 95, 95, 95, dash="4 3"))
    o.append(ar(95, 95, 95, 71))
    o.append(tx(8, 54, "R(s)", 6.8, anchor="start"))
    o.append(tx(378, 56, "C(s)", 6.8, anchor="start"))
    o.append(tx(242, 90, "Feedback", 6.3, anchor="middle", color=GREY))
    o.append(tx(248, 32, "G(s)", 6.5, anchor="middle", color=GREY))
    return _f(o, 430, 130,
              "Bài tập 6: hệ phản hồi với đường truyền thuận G(s) = K/[s(s+2)] và phản hồi đơn vị.",
              "Problem 6: a feedback system with a forward path G(s) = K/[s(s+2)] and unity feedback.")


# =====================================================================
# Figure 4.14 - Problem 7: pole locations on s-planes
# =====================================================================
def fig_4_14():
    o = []
    _splane(o, 25, 70, 160, 130, [(-1.5, 0), (-0.5, 0)], "(a)")
    _splane(o, 255, 70, 160, 130, [(1.5, 0), (0.5, 0)], "(b)")
    _splane(o, 25, 230, 160, 130, [(-1, 1), (-1, -1)], "(c)")
    _splane(o, 255, 230, 160, 130, [(1, 1), (1, -1)], "(d)")
    return _f(o, 440, 360,
              "Bài tập 7: các vị trí cực trên mặt phẳng s — (a)(b) cực thực, (c)(d) cực phức. Xác định cực nào cho quá độ ổn định, cực nào cho dao động.",
              "Problem 7: pole locations on the s-plane — (a)(b) real poles, (c)(d) complex poles. Determine which give stable transients and which give oscillatory transients.")


# =====================================================================
# Figure 4.15 - Problem 9: feedback control system with unity feedback
# =====================================================================
def fig_4_15():
    o = []
    o.append(sumj(95, 60, ["+", "", "-"]))
    o.append(ar(18, 60, 84, 60))
    o.append(ar(106, 60, 185, 60))
    o.append(bx(185, 38, 130, 44, "G(s)"))
    o.append(ar(315, 60, 370, 60))
    o.append(ar(370, 60, 370, 95, dash="4 3"))
    o.append(ar(370, 95, 95, 95, dash="4 3"))
    o.append(ar(95, 95, 95, 71))
    o.append(tx(8, 54, "R(s)", 6.8, anchor="start"))
    o.append(tx(378, 56, "C(s)", 6.8, anchor="start"))
    o.append(tx(242, 90, "Unity feedback", 6.3, anchor="middle", color=GREY))
    o.append(tx(248, 32, "G(s)", 6.5, anchor="middle", color=GREY))
    return _f(o, 430, 130,
              "Bài tập 9: hệ điều khiển phản hồi với phản hồi đơn vị; xét tính ổn định với các giá trị K và G(s) khác nhau.",
              "Problem 9: a feedback control system with unity feedback; consider stability for the different values of K and G(s).")


FIGS = {n: globals()[n] for n in dir() if n.startswith("fig_")}
