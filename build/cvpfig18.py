# -*- coding: utf-8 -*-
"""Vector figure for Book 7 - Baumann, *Control Valve Primer*, 5th ed.

Chapter 18 "The ABC Method for Gases" has one printed figure: Figure 18-1,
the 8-inch segmented V-ball valve air test data. The function returns the
standard 5-tuple ``(svg, caption_vi, caption_en, aria_vi, aria_en)``.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from vfig import (BLUE, GREY, INK, RED, _circle, _fig, _line, _poly,
                  _rect, _txt, svg)

FIGS = {}


def _reg(f):
    FIGS[f.__name__] = f()
    return f


def esc(s):
    s = str(s)
    s = s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    return s.replace('"', "&quot;")


@_reg
def fig_f181():
    """Figure 18-1 - actual air test data on an 8-inch ball valve."""
    w, h = 680, 360
    L, T, R, B = 82, 58, 636, 298
    PW, PH = R - L, B - T
    o = []

    o.append(_txt(340, 17,
                  esc("8 in Segmented V-Ball Valve, in 16 in pipe, Cv = 134, "
                      "P1 = 1.1 to 6 bar"),
                  10.2, color=INK, weight="600"))
    o.append(_txt(340, 31,
                  esc("a0, FL = 0.6, Fd = 0.4, P2 = 1 bar(a)"),
                  8.0, color=GREY))

    # legend, kept above the plotting frame
    o.append(_line(286, 45, 306, 45, sw=1.6, color=INK))
    o.append(_circle(296, 45, 2.7, fill=INK, sw=0))
    o.append(_txt(311, 48, esc("Test Data"), 7.2, anchor="start", color=INK))
    o.append(_line(383, 45, 403, 45, sw=1.5, color=BLUE))
    o.append(_txt(408, 48, esc("Series2"), 7.2, anchor="start", color=INK))

    def px(x):
        return L + (x - 1.0) / 7.0 * PW

    def py(v):
        return B - v / 120.0 * PH

    o.append(_rect(L, T, PW, PH, fill="#fdfcf9", sw=1.1))
    for v in range(0, 121, 20):
        o.append(_line(L, py(v), R, py(v), sw=0.8, color="#c9cdd2"))
        o.append(_txt(L - 8, py(v) + 2.6, str(v), 7.0,
                      anchor="end", color=GREY))
    for x in range(1, 9):
        o.append(_line(px(x), T, px(x), B, sw=0.7, color="#dedfe1"))
        o.append(_txt(px(x), B + 13, str(x), 7.0, color=GREY))

    o.append(_txt(L - 26, T - 6, esc("Sound Level in dBA at 1 m"),
                  7.4, anchor="start", color=INK))
    o.append(_txt((L + R) / 2.0, B + 29,
                  esc("10 × X, Pressure ratio, (P1 − P2)/P1"),
                  7.6, color=INK))

    data = [(1, 55), (2, 69), (3, 76), (4, 82),
            (5, 87), (6, 91), (7, 95), (8, 99)]
    o.append(_poly([(px(x), py(v)) for x, v in data],
                   sw=1.7, color=BLUE))
    for x, v in data:
        o.append(_circle(px(x), py(v), 3.0, fill="#ffffff", sw=1.2, color=RED))

    o.append(_txt(340, 337,
                  esc("From 10X to 80X the slope follows 30 log(10X); "
                      "the marked point at 10X = 6 is the worked example."),
                  7.0, color=GREY))

    title = "Baumann Figure 18-1: air test data, 8-inch segmented ball valve"
    caption_vi = ("Hình 18-1. Số liệu thử nghiệm không khí thực tế trên van bi phân đoạn "
                  "8 inch (xem mô tả ở trên). Lưu ý rằng độ dốc của đường cong từ 10X đến "
                  "80X khớp chính xác với luật mức ồn bên ngoài phải tuân theo 30 log(10X) "
                  "được nêu ở nơi khác trong sách.")
    caption_en = ("Figure 18-1. Actual air test data on an 8-inch ball valve (see earlier "
                  "description). Note that the slope of the curve from 10X to 80X "
                  "corresponds exactly to the law that exterior sound level should follow "
                  "30 log(10X) stated elsewhere in this book.")
    aria_vi = ("Đồ thị mức ồn dBA tại 1 m theo 10 nhân áp suất giảm P1 trừ P2 chia P1, "
               "từ 55 đến 99 dBA khi 10X tăng từ 1 đến 8, có đường cong và các điểm thử nghiệm.")
    aria_en = ("Chart of sound level in dBA at 1 m against 10 times the pressure drop "
               "ratio from 1 to 8, rising from about 55 to 99 dBA with a fitted curve "
               "and eight measured points.")
    return _fig(svg(w, h, "".join(o), esc(title)),
                caption_vi, caption_en, aria_vi, aria_en)
