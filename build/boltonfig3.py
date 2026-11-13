# -*- coding: utf-8 -*-
"""Vector figures for Bolton *Control Systems* (Newnes, 2002), Chapter 3.

Chapter 3 (System response) has only three figures; the rest is largely
algebra and a table of Laplace transform pairs. Each function returns
(svg, caption_vi, caption_en, aria_vi, aria_en).
"""
import math

from vfig import (BLUE, GOLD, GREY, INK, PAPER, RED, GREEN, _arrow, _axes,
                  _box, _circle, _curve, _defs, _ellipse, _f, _fig, _hatch,
                  _label, _line, _path, _poly, _rect, _ring, _txt, svg)


def _svg(w, h, objs, title=""):
    return svg(w, h, _defs() + "".join(objs), title)


def _f(o, w, h, vi, en, aria_vi="", aria_en=""):
    return _fig(_svg(w, h, o, vi), vi, en, aria_vi or vi, aria_en or en)


def tx(x, y, s, size=7.6, anchor="middle", color=INK, weight=""):
    return _txt(x, y, s, size, anchor=anchor, color=color, weight=weight)


# =====================================================================
# Figure 3.1 - Forms of input: (a) step, (b) impulse, (c) ramp
# =====================================================================
def fig_3_1():
    o = []
    # (a) step
    o.append(_axes(20, 30, 90, 70, "Time", ""))
    o.append(_poly([(20, 100), (48, 100), (48, 30), (110, 30)], color=INK, sw=1.4))
    o.append(tx(65, 16, "(a) step", 7))
    # (b) impulse
    o.append(_axes(150, 30, 90, 70, "Time", ""))
    o.append(_poly([(166, 100), (172.5, 30), (179, 100)], color=INK, sw=1.4))
    o.append(tx(195, 16, "(b) impulse", 7))
    # (c) ramp
    o.append(_axes(280, 30, 90, 70, "Time", ""))
    o.append(_poly([(280, 100), (370, 30)], color=INK, sw=1.4))
    o.append(tx(325, 16, "(c) ramp", 7))
    return _f(o, 400, 120,
              "Các dạng đầu vào chuẩn: (a) bậc — nhảy lên giá trị không đổi, (b) xung — tồn tại rất ngắn, (c) dốc — tăng đều theo thời gian.",
              "Forms of standard input: (a) step — jumps to a constant value, (b) impulse — exists only briefly, (c) ramp — increases at a constant rate.")


# =====================================================================
# Figure 3.2 - First-order impulse response
# =====================================================================
def fig_3_2():
    o = []
    x0, y0, W, H = 45, 30, 300, 150
    o.append(_axes(x0, y0, W, H, "Time", "Output"))
    o.append(_curve(lambda t: math.exp(-t), x0, y0, W, H, xr=(0, 4), yr=(0, 1.05), color=BLUE, sw=1.4))
    for t, y, lab in [(1, 0.368, "0.37"), (2, 0.135, "0.14"), (3, 0.05, "0.05")]:
        px = x0 + t / 4.0 * W
        py = y0 + H - y / 1.05 * H
        o.append(_circle(px, py, 2.4, fill=RED))
        o.append(_line(px, py, px, y0 + H, color=GREY, sw=0.6, dash="2 3"))
        o.append(_txt(px - 4, py - 6, lab, 6.5, anchor="end", color=RED))
    return _f(o, 400, 200,
              "Đáp ứng xung của hệ bậc nhất: tại t=0 đạt cực đại, sau 1τ còn 0,37; 2τ còn 0,14; 3τ còn 0,05; sau ~4τ xấp xỉ không.",
              "Output of a first-order system to a unit impulse: maximum at t=0, then 0.37 after 1τ, 0.14 after 2τ, 0.05 after 3τ, effectively zero after about 4τ.")


# =====================================================================
# Figure 3.3 - First-order step response
# =====================================================================
def fig_3_3():
    o = []
    x0, y0, W, H = 45, 30, 300, 150
    o.append(_axes(x0, y0, W, H, "Time", "Output"))
    o.append(_curve(lambda t: 1 - math.exp(-t), x0, y0, W, H, xr=(0, 4), yr=(0, 1.1), color=BLUE, sw=1.4))
    for t, y, lab in [(1, 0.632, "0.63k"), (2, 0.865, "0.86k"), (3, 0.95, "0.95k"), (4, 0.982, "0.98k")]:
        px = x0 + t / 4.0 * W
        py = y0 + H - y / 1.1 * H
        o.append(_circle(px, py, 2.4, fill=RED))
        o.append(_line(px, py, px, y0 + H, color=GREY, sw=0.6, dash="2 3"))
        o.append(_txt(px - 4, py - 6, lab, 6.5, anchor="end", color=RED))
    return _f(o, 400, 200,
              "Đáp ứng bậc của hệ bậc nhất: tại 1τ đạt 0,63k, 2τ đạt 0,86k, 3τ đạt 0,95k, 4τ đạt giá trị xác lập k.",
              "Behaviour of a first-order system to a unit step input: 0.63k after 1τ, 0.86k after 2τ, 0.95k after 3τ, steady value k after 4τ.")


FIGS = {n: globals()[n] for n in dir() if n.startswith("fig_")}
