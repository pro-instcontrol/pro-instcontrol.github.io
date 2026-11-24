# -*- coding: utf-8 -*-
"""Vector figures for Book 7 - Baumann, *Control Valve Primer*, 5th ed.

Chapter 15 "Cavitation": simplified vector redrawings of source Figures 15-1
to 15-5. Each function returns the standard 5-tuple
``(svg, caption_vi, caption_en, aria_vi, aria_en)``.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from vfig import (BLUE, GREEN, GREY, INK, RED, _arrow, _circle, _defs, _f,
                  _fig, _line, _path, _poly, _rect, _txt, svg)

FIGS = {}


def _reg(f):
    FIGS[f.__name__] = f
    return f


def esc(s):
    s = str(s)
    s = s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    return s.replace('"', "&quot;")


def _marker(kind, x, y, color, r=3.2):
    if kind == "circle":
        return _circle(x, y, r, fill="#ffffff", sw=1.1, color=color)
    if kind == "square":
        return _rect(x - r, y - r, 2 * r, 2 * r, fill="#ffffff",
                     sw=1.0, stroke=color)
    if kind == "tri":
        return _poly([(x, y - r - 0.4), (x + r + 0.4, y + r),
                      (x - r - 0.4, y + r)], sw=1.0, color=color,
                     fill="#ffffff", close=True)
    return _line(x - r, y - r, x + r, y + r, sw=1.1, color=color) + \
        _line(x - r, y + r, x + r, y - r, sw=1.1, color=color)


@_reg
def fig_f151():
    """Figure 15-1 - theoretical turbulent and cavitation sound profiles."""
    w, h = 680, 400
    L, TOP, R, B = 62, 46, 628, 344
    PW, PH = R - L, B - TOP
    o = [_defs()]
    o.append(_txt(340, 16, esc("Theoretical turbulent and cavitation profiles vs X_Fz"),
                  10.6, color=INK, weight="600"))
    o.append(_txt(340, 30, esc("Simplified redrawing of Baumann Fig. 15-1; source: manufacturer data"),
                  7.4, color=GREY))

    def px(x):
        return L + (x - 1.0) / 9.0 * PW

    def py(v):
        return B - v / 60.0 * PH

    for v in range(0, 61, 10):
        o.append(_line(L, py(v), R, py(v), sw=0.8, color="#c9cdd2"))
        o.append(_txt(L - 7, py(v) + 2.6, str(v), 7.0, anchor="end", color=GREY))
    for x in range(1, 11):
        o.append(_line(px(x), TOP, px(x), B, sw=0.8, color="#d5d8dc"))
        o.append(_txt(px(x), B + 13, str(x), 7.0, color=GREY))
    o.append(_rect(L, TOP, PW, PH, fill="#fdfcf9", sw=1.1))

    o.append(_txt(L + 8, TOP + 14, esc("ΔL INCREASE DUE TO CAVITATION = 60 log(X / X_Fz)"),
                  7.0, anchor="start", color=INK, weight="600"))

    turb = [(1, 0), (2, 9), (3, 14), (4, 18), (5, 21),
            (6, 23), (7, 25), (8, 26), (9, 27), (10, 27)]
    curves = [
        ("X_Fz = 0.2", "diamond", GREY, "5 3",
         [(2, 9), (2.5, 25), (3, 30), (4, 36), (5, 43), (6, 51),
          (7, 47), (8, 40), (9, 33), (10, 27)]),
        ("X_Fz = 0.3", "square", BLUE, "",
         [(2, 9), (3, 15), (4, 25), (5, 36), (6, 42),
          (7, 38), (8, 34), (9, 30), (10, 27)]),
        ("X_Fz = 0.4", "tri", GREEN, "5 3",
         [(2, 9), (3, 14), (4, 22), (5, 29), (6, 35),
          (7, 37), (8, 33), (9, 30), (10, 27)]),
    ]
    o.append(_poly([(px(x), py(v)) for x, v in turb], sw=1.9, color=INK))
    for lab, kind, col, dash, pts in curves:
        o.append(_poly([(px(x), py(v)) for x, v in pts], sw=1.5,
                       color=col, dash=dash))
        for x, v in pts:
            o.append(_marker(kind, px(x), py(v), col, r=2.6))
    o.append(_marker("diamond", R - 98, TOP + 16, GREY, r=2.6))
    o.append(_txt(R - 90, TOP + 19, esc("X_Fz = 0.2"), 6.6,
                  anchor="start", color=GREY))
    o.append(_marker("square", R - 98, TOP + 27, BLUE, r=2.6))
    o.append(_txt(R - 90, TOP + 30, esc("X_Fz = 0.3"), 6.6,
                  anchor="start", color=BLUE))
    o.append(_marker("tri", R - 98, TOP + 38, GREEN, r=2.6))
    o.append(_txt(R - 90, TOP + 41, esc("X_Fz = 0.4"), 6.6,
                  anchor="start", color=GREEN))

    o.append(_txt(px(7.4), py(20), esc("F_L²"), 8.0, color=INK, weight="600"))
    for x, y, lab in ((6.0, 51, "Xy"), (6.0, 42, "Xy"), (7.0, 37, "Xy")):
        o.append(_txt(px(x), py(y) - 7, lab, 7.4, color=INK, weight="600"))
    o.append(_arrow(px(2.2), py(25), px(2.2), py(10), sw=1.0, color=INK))
    o.append(_txt(px(2.2) + 6, py(18), esc("L"), 8.0, color=INK, weight="600"))
    o.append(_txt(px(2.9), py(9) + 12, esc("X_Fz"), 7.0, color=GREY))
    o.append(_txt(px(4.2), py(19), esc("X_F2"), 7.0, color=GREY))

    o.append(_txt(R, B + 31, esc("X × 10"), 8.2, anchor="end",
                  color=INK, weight="600"))
    o.append('<text x="%s" y="%s" text-anchor="middle" '
             'style="font:8px Inter,Helvetica,sans-serif;fill:%s;font-weight:600" '
             'transform="rotate(-90,%s,%s)">%s</text>'
             % (_f(18), _f((TOP + B) / 2.0), INK,
                _f(18), _f((TOP + B) / 2.0),
                esc("Relative Sound Level in dB")))

    s = svg(w, h, "".join(o), esc("Theoretical turbulent and cavitation sound profiles"))
    return _fig(s,
                "Hình 15.1 · Bản vẽ lại đơn giản hóa các đường lý thuyết về tiếng ồn: trục hoành là X × 10 (tỷ số áp suất X = (P1 − P2)/(P1 − Pv), từ 0,1 đến 1,0), trục tung là mức ồn tương đối (dB, 0–60). Đường đen là tiếng ồn rối (turbulent), tiến tới nền F_L² khoảng 26 dB. Ba đường xâm thực ứng với X_Fz = 0,2 (kim cương đứt nét), 0,3 (ô vuông) và 0,4 (tam giác đứt nét) tăng dần tới đỉnh Xy rồi giảm về 27 dB; đỉnh cao nhất khoảng 51 dB. Mũi tên L tại X×10 ≈ 2,2 minh họa độ tăng 60 log(X/X_Fz). Nhà sản xuất thường cung cấp giá trị X_Fz cho van. Đây là bản vẽ lại dạng vector, đã đơn giản hóa.",
                "Figure 15.1 · Simplified redrawing of the theoretical sound profiles: x is X × 10 (pressure ratio X = (P1 − P2)/(P1 − Pv), 0.1 to 1.0), y is relative sound level (dB, 0–60). The black line is turbulent sound, approaching an F_L² plateau near 26 dB. The three cavitation curves for X_Fz = 0.2 (dashed diamonds), 0.3 (squares) and 0.4 (dashed triangles) rise to their Xy peaks and fall back to 27 dB; the highest peak is about 51 dB. The L arrow near X×10 ≈ 2.2 illustrates the 60 log(X/X_Fz) increase. Manufacturers normally specify X_Fz for their valves. This is a simplified vector redrawing.",
                "Đồ thị mức ồn lý thuyết theo tỷ số áp suất: đường rối tiến tới nền F_L², ba đường xâm thực với X_Fz = 0,2/0,3/0,4 có đỉnh Xy rồi giảm; mũi tên L chỉ độ tăng do xâm thực.",
                "Chart of turbulent and cavitation sound levels versus pressure ratio with three X_Fz curves, Xy peaks and an L increase arrow")


@_reg
def fig_f152():
    """Figure 15-2 - air injection through a hollow butterfly-valve stem."""
    w, h = 680, 320
    o = [_defs()]
    o.append(_txt(340, 18, esc("Cavitation reduction by air injection through the valve stem"),
                  10.6, color=INK, weight="600"))
    o.append(_txt(340, 32, esc("Simplified redrawing of Baumann Fig. 15-2; courtesy H. D. Baumann"),
                  7.4, color=GREY))

    # valve body: circular shell with pipe stubs
    o.append(_circle(390, 172, 118, fill="#fdfcf9", sw=1.6, color=INK))
    o.append(_circle(390, 172, 92, fill="#ffffff", sw=1.2, color="#9fa8b3"))
    o.append(_rect(508, 156, 118, 32, fill="#f4f6f8", sw=1.2, stroke=INK))
    o.append(_rect(164, 156, 100, 32, fill="#f4f6f8", sw=1.2, stroke=INK))
    o.append(_txt(390, 300, esc("BUTTERFLY VALVE BODY"), 7.6, color=GREY, weight="600"))

    # hollow stem across the body
    o.append(_rect(150, 164, 470, 16, fill="#dfe6ee", sw=1.2, stroke=INK))
    o.append(_line(150, 172, 620, 172, sw=0.8, dash="4 3", color=GREY))
    # exposed shaft holes pointing downstream
    for x in (362, 388, 414, 440, 466, 492):
        o.append(_circle(x, 172, 3.4, fill="#ffffff", sw=1.0, color=INK))
        o.append(_arrow(x, 178, x + 14, 196, sw=0.9, color=BLUE))
    o.append(_txt(430, 132, esc("EXPOSED SHAFT HOLES"), 7.0,
                  color=INK, weight="600"))
    o.append(_txt(430, 143, esc("POINTING DOWNSTREAM"), 7.0,
                  color=INK, weight="600"))

    # air inlet box and check valve
    o.append(_rect(112, 142, 78, 60, fill="#eef3fb", sw=1.2, stroke=INK))
    o.append(_txt(151, 158, esc("AIR INLET"), 7.2, color=INK, weight="600"))
    o.append(_arrow(120, 180, 174, 180, sw=1.2, color=BLUE))
    o.append(_poly([(172, 174), (182, 180), (172, 186)],
                   fill="#ffffff", sw=1.0, color=INK, close=True))
    o.append(_line(182, 170, 182, 190, sw=1.0, color=INK))
    o.append(_txt(151, 214, esc("CHECK VALVE"), 7.2, color=GREY, weight="600"))

    # tilted vane
    o.append(_poly([(322, 118), (372, 104), (458, 222), (408, 236)],
                   fill="#c9d4e0", sw=1.4, color=INK, close=True))
    o.append(_txt(330, 250, esc("VANE"), 7.6, color=INK, weight="600"))

    o.append(_txt(340, 290, esc("Internal vacuum from the high jet velocity sucks air through the stem — up to 10 dB sound-level saving"),
                  7.4, color=GREY))

    s = svg(w, h, "".join(o), esc("Air injection through hollow butterfly-valve stem"))
    return _fig(s,
                "Hình 15.2 · Sơ đồ cắt đơn giản hóa cơ chế phun khí vào dòng chảy qua thân van bướm rỗng: hộp AIR INLET ở bên trái có van một chiều (check valve), dẫn khí vào lỗ rỗng dọc trục van; các lỗ nhỏ trên trục hướng xuôi dòng (EXPOSED SHAFT HOLES POINTING DOWNSTREAM) đưa khí vào vùng chân không sinh ra do vận tốc tia cao. Cánh van (VANE) nghiêng trong thân van (BUTTERFLY VALVE BODY). Có thể giảm mức ồn tới 10 dB. Nguồn: H. D. Baumann. Đây là bản vẽ lại dạng vector, đã đơn giản hóa.",
                "Figure 15.2 · Simplified cutaway of air injection through a hollow butterfly-valve stem: an AIR INLET box with a check valve feeds the hollow stem, and small shaft holes pointing downstream (EXPOSED SHAFT HOLES POINTING DOWNSTREAM) admit air into the vacuum created by the high jet velocity. The tilted VANE sits in the BUTTERFLY VALVE BODY. Sound-level savings of up to 10 dB have been experienced. Source: H. D. Baumann. This is a simplified vector redrawing.",
                "Sơ đồ cắt van bướm: khí từ cổng vào qua van một chiều đi trong trục rỗng và phun qua các lỗ hướng xuôi dòng để giảm tiếng ồn xâm thực.",
                "Cutaway schematic of a butterfly valve with air inlet, check valve, hollow stem and downstream-facing shaft holes")


@_reg
def fig_f153():
    """Figure 15-3 - sharktooth anticavitation butterfly valve."""
    w, h = 680, 330
    o = [_defs()]
    o.append(_txt(340, 18, esc("Sharktooth anticavitation butterfly valve (simplified)"),
                  10.6, color=INK, weight="600"))
    o.append(_txt(340, 32, esc("Simplified redrawing of Baumann Fig. 15-3"),
                  7.4, color=GREY))

    # valve body ring (front view, slightly flattened)
    o.append(_circle(238, 172, 112, fill="#fdfcf9", sw=2.0, color=INK))
    o.append(_circle(238, 172, 88, fill="#ffffff", sw=1.4, color="#9fa8b3"))
    # seat teeth on the lower-right inner edge
    for i in range(7):
        a = -0.9 + i * 0.20
        import math
        x = 238 + 88 * math.cos(a)
        y = 172 + 88 * math.sin(a)
        o.append(_poly([(x, y), (x + 9 * math.cos(a + 0.7), y + 9 * math.sin(a + 0.7)),
                        (x + 9 * math.cos(a - 0.7), y + 9 * math.sin(a - 0.7))],
                       fill="#b8bfc6", sw=0.8, color=INK, close=True))

    # tilted vane plate with mating teeth
    o.append(_poly([(166, 108), (238, 92), (316, 224), (244, 240)],
                   fill="#dfe6ee", sw=1.6, color=INK, close=True))
    for i in range(5):
        t = 0.16 + i * 0.17
        x = 244 + (316 - 244) * t
        y = 240 + (224 - 240) * t
        o.append(_poly([(x, y), (x + 10, y - 3), (x + 4, y - 12)],
                       fill="#9fa8b3", sw=0.8, color=INK, close=True))
    o.append(_circle(238, 172, 9, fill="#ffffff", sw=1.4, color=INK))
    o.append(_line(238, 163, 238, 181, sw=1.0, color=INK))

    # turbulence and flow indication
    for yy in (132, 150, 168):
        o.append(_path("M%s,%s Q%s,%s %s,%s Q%s,%s %s,%s"
                       % (330, yy, 350, yy - 12, 372, yy + 4,
                          396, yy + 14, 424, yy - 3),
                       sw=1.0, color=BLUE))
    o.append(_arrow(330, 190, 430, 190, sw=1.2, color=BLUE))

    o.append(_txt(492, 110, esc("Teeth interacting with"), 8.0,
                  anchor="start", color=INK, weight="600"))
    o.append(_txt(492, 123, esc("the vane create high"), 8.0,
                  anchor="start", color=INK, weight="600"))
    o.append(_txt(492, 136, esc("turbulence, shifting"), 8.0,
                  anchor="start", color=INK, weight="600"))
    o.append(_txt(492, 149, esc("cavitation downstream"), 8.0,
                  anchor="start", color=INK, weight="600"))
    o.append(_txt(492, 178, esc("DN 150 (6 in)"), 7.6,
                  anchor="start", color=GREY, weight="600"))
    o.append(_txt(492, 192, esc("Cv = 340   FL = 0.8"), 7.6,
                  anchor="start", color=GREY))
    o.append(_txt(492, 206, esc("P1 = 7.7 bar (abs)"), 7.6,
                  anchor="start", color=GREY))
    o.append(_txt(492, 220, esc("XFz = 0.64   60° open"), 7.6,
                  anchor="start", color=GREY))
    o.append(_txt(340, 300, esc("Source figure is a photograph/rendering; redrawn here as a simplified vector schematic"),
                  7.2, color=GREY))

    s = svg(w, h, "".join(o), esc("Sharktooth anticavitation butterfly valve"))
    return _fig(s,
                "Hình 15.3 · Bản vẽ lại đơn giản hóa van bướm chống xâm thực do tác giả thiết kế: thân van dạng vòng, cánh van nghiêng với các răng lệch ở mép ăn khớp với răng trên bệ van; sự tương tác này tạo độ nhiễu loạn cao và dời xâm thực xuống phía dưới. Dòng chảy được biểu diễn bằng các đường cong phía sau cánh. Thông số ghi trong bản gốc: DN 150 (6 in), Cv = 340, FL = 0,8, P1 = 7,7 bar (abs), XFz = 0,64, độ mở 60°. Hình gốc là ảnh/mô phỏng; đây là sơ đồ vector đã đơn giản hóa.",
                "Figure 15.3 · Simplified redrawing of the author-designed anticavitation butterfly valve: a ring-shaped body, a tilted vane with offset teeth along its edge mating with teeth on the seat; their interaction creates high turbulence and shifts cavitation downstream. Flow is indicated by curved streamlines behind the vane. The source lists DN 150 (6 in), Cv = 340, FL = 0.8, P1 = 7.7 bar (abs), XFz = 0.64, 60° open. The source image is a photograph/rendering; this is a simplified vector schematic.",
                "Sơ đồ van bướm chống xâm thực có răng: cánh van răng cưa ăn khớp với răng bệ van tạo nhiễu loạn cao; kèm thông số DN 150, Cv 340, XFz 0,64.",
                "Simplified vector schematic of a sharktooth anticavitation butterfly valve with mating teeth and flow streamlines")


@_reg
def fig_f154():
    """Figure 15-4 - laboratory test data for the anticavitation butterfly valve."""
    w, h = 680, 420
    L, TOP, R, B = 62, 54, 626, 356
    PW, PH = R - L, B - TOP
    o = [_defs()]
    o.append(_txt(340, 14, esc("DN 150 (6 in) Sharktooth Butterfly Valve: Cv = 340, FL = 0.8, P1 = 7.7 bar (abs), XFz = 0.64"),
                  8.4, color=INK, weight="600"))
    o.append(_txt(340, 27, esc("Valve opening 60 degrees · simplified redrawing of Baumann Fig. 15-4"),
                  7.2, color=GREY))
    o.append(_txt(340, 39, esc("Calculated estimate"), 7.0, color=INK, weight="600"))

    def px(x):
        return L + (x - 1.0) / 9.0 * PW

    def py(v):
        return B - v / 100.0 * PH

    for v in range(0, 101, 10):
        o.append(_line(L, py(v), R, py(v), sw=0.7, color="#e2e5e8"))
        o.append(_txt(L - 7, py(v) + 2.6, str(v), 6.8, anchor="end", color=GREY))
    for x in range(1, 11):
        o.append(_line(px(x), TOP, px(x), B, sw=0.7, color="#d5d8dc"))
        o.append(_txt(px(x), B + 13, str(x), 7.0, color=GREY))
    o.append(_rect(L, TOP, PW, PH, fill="#fdfcf9", sw=1.1))

    # black turbulent line: proportional to 30 log(10X)
    turb = [(1, 74), (2, 80), (3, 84), (4, 87), (5, 89),
            (6, 91), (7, 92), (8, 94), (9, 95), (10, 95)]
    o.append(_poly([(px(x), py(v)) for x, v in turb], sw=1.8, color=INK))
    # measured / calculated estimate with square markers
    calc = [(1, 68), (2, 77), (3, 83), (4, 87), (5, 89),
            (6, 91), (7, 93), (8, 95), (9, 96), (10, 96)]
    o.append(_poly([(px(x), py(v)) for x, v in calc], sw=1.4,
                   color=GREY, dash="4 3"))
    for x, v in calc:
        o.append(_marker("square", px(x), py(v), INK, r=2.4))

    o.append(_txt(px(2.4), py(72) - 6, esc("BLACK LINE: TURBULENT FLOW"),
                  7.2, color=INK, weight="600"))
    o.append(_txt(px(2.4), py(72) + 5, esc("(proportional to 30 log(10X))"),
                  7.0, color=GREY))
    o.append(_line(px(8.0), py(91), px(8.0), py(96), sw=1.0, color=INK))
    o.append(_txt(px(7.9), py(86), esc("XFz = 0.64"), 7.4,
                  anchor="end", color=INK, weight="600"))
    o.append(_line(px(8.4), py(94), px(8.4), py(98), sw=1.0, color=INK))
    o.append(_line(px(8.4), py(98), px(10), py(98), sw=1.0, color=INK))
    o.append(_txt(px(9.2), py(99.2) - 5, esc("Cavitation amplitude 5.6 dB"),
                  7.0, color=INK, weight="600"))

    o.append(_txt(R, B + 31, esc("12.5 times X, X = (P1 − P2)/(P1 − Pv)"),
                  7.8, anchor="end", color=INK, weight="600"))
    o.append('<text x="%s" y="%s" text-anchor="middle" '
             'style="font:8px Inter,Helvetica,sans-serif;fill:%s;font-weight:600" '
             'transform="rotate(-90,%s,%s)">%s</text>'
             % (_f(18), _f((TOP + B) / 2.0), INK,
                _f(18), _f((TOP + B) / 2.0),
                esc("Sound Level in dBA at 1 m")))
    o.append(_txt(340, 402, esc("Laboratory test data with water; source caption retained in translation"),
                  7.0, color=GREY))

    s = svg(w, h, "".join(o), esc("Laboratory sound data for an anticavitation butterfly valve"))
    return _fig(s,
                "Hình 15.4 · Bản vẽ lại đơn giản hóa dữ liệu thử nghiệm trong phòng thí nghiệm với nước cho van bướm chống xâm thực: trục hoành là 12,5 lần X, với X = (P1 − P2)/(P1 − Pv), từ 1 đến 10; trục tung là mức ồn dBA ở 1 m (0–100). Đường đen là tiếng ồn rối tỷ lệ 30 log(10X); đường có ô vuông là giá trị tính toán tăng từ khoảng 68 dBA lên 96 dBA. XFz = 0,64 được chỉ ra gần X×12,5 ≈ 8; biên độ xâm thực chỉ 5,6 dB. Thông số van: DN 150 (6 in), Cv = 340, FL = 0,8, P1 = 7,7 bar (abs), độ mở 60°. Đây là bản vẽ lại dạng vector, đã đơn giản hóa.",
                "Figure 15.4 · Simplified redrawing of laboratory water test data for the anticavitation butterfly valve: x is 12.5 times X, with X = (P1 − P2)/(P1 − Pv), from 1 to 10; y is sound level in dBA at 1 m (0–100). The black line is turbulent sound proportional to 30 log(10X); the square-marked calculated estimate rises from about 68 to 96 dBA. XFz = 0.64 is indicated near X×12.5 ≈ 8; the cavitation amplitude is only 5.6 dB. Valve data: DN 150 (6 in), Cv = 340, FL = 0.8, P1 = 7.7 bar (abs), 60° open. This is a simplified vector redrawing.",
                "Đồ thị dữ liệu thử nghiệm mức ồn: đường tính toán tăng từ 68 lên 96 dBA, XFz = 0,64 và biên độ xâm thực 5,6 dB cho van bướm DN 150.",
                "Chart of measured and turbulent sound levels versus pressure ratio for a sharktooth butterfly valve")


@_reg
def fig_f155():
    """Figure 15-5 - cavitation-damaged valve plug and seat ring (vector sketch)."""
    w, h = 680, 330
    o = [_defs()]
    o.append(_txt(340, 18, esc("Cavitation damage: plug tip and seat ring (vector sketch)"),
                  10.6, color=INK, weight="600"))
    o.append(_txt(340, 32, esc("Simplified redrawing of Baumann Fig. 15-5; source photo courtesy Jon Monsen"),
                  7.4, color=GREY))

    # plug: smooth cylindrical body left, pitted parabolic tip right
    o.append(_rect(58, 96, 190, 82, fill="#dfe6ee", sw=1.4, stroke=INK))
    o.append(_path("M248,96 C320,96 372,116 410,137 C372,158 320,178 248,178 Z",
                   fill="#eef1f4", sw=1.4, color=INK))
    o.append(_line(248, 96, 248, 178, sw=1.0, dash="4 3", color=GREY))
    # pitting: small random-looking circles concentrated on the damaged half
    pits = [(268,108,4),(286,126,3),(300,102,2),(312,138,4),(330,112,3),
            (346,132,2),(358,120,3),(372,138,4),(386,129,2),(398,137,3),
            (276,148,3),(294,160,4),(316,152,2),(338,164,3),(360,151,4),
            (380,145,2),(330,140,3),(352,158,2),(390,136,3),(300,120,2)]
    for x, y, r in pits:
        o.append(_circle(x, y, r, fill="#b8bfc6", sw=0.7, color=GREY))
    o.append(_txt(150, 88, esc("ORIGINAL PLUG SURFACE"), 7.2,
                  color=GREY, weight="600"))
    o.append(_txt(330, 88, esc("CAVITATION PITTING"), 7.2,
                  color=RED, weight="600"))
    o.append(_txt(240, 202, esc("Parabolic plug tip — about half eaten away"),
                  7.4, color=INK, weight="600"))

    # seat ring: annular cross-section with pitted bore
    o.append(_circle(512, 244, 56, fill="#eef1f4", sw=1.5, color=INK))
    o.append(_circle(512, 244, 26, fill="#ffffff", sw=1.3, color=INK))
    for x, y, r in ((490,224,3),(500,214,2),(520,216,3),(536,228,2),
                    (542,244,3),(532,262,2),(514,270,3),(494,262,2),
                    (504,232,2),(524,252,3)):
        o.append(_circle(x, y, r, fill="#b8bfc6", sw=0.6, color=GREY))
    o.append(_txt(512, 316, esc("Damaged seat ring bore"), 7.4,
                  color=INK, weight="600"))

    o.append(_txt(340, 258, esc("No known trim material withstands cavitation"),
                  8.0, color=INK, weight="600"))
    o.append(_txt(340, 274, esc("impact pressures can exceed 100,000 psi"),
                  7.6, color=RED))
    o.append(_txt(340, 292, esc("Hardened trim only prolongs service life"),
                  7.4, color=GREY))

    s = svg(w, h, "".join(o), esc("Cavitation-damaged valve plug and seat ring"))
    return _fig(s,
                "Hình 15.5 · Bản vẽ lại dạng vector sơ đồ hóa ảnh gốc: bên trái là thân nút van nguyên vẹn, bên phải là đầu nút dạng parabol bị xâm thực ăn mòn khoảng một nửa với nhiều hố rỗ li ti (CAVITATION PITTING); bên dưới là vòng đế van bị hư hỏng ở lỗ trong. Mức ồn ngoài vượt 80 dBA có thể gây phá hủy tương tự; Jon Monsen đề xuất ngưỡng 85 dBA cho van 4–6 in, 90 dBA cho 8–14 in và 95 dBA cho cỡ lớn hơn. Không có vật liệu bộ lót nào chịu được áp suất va đập vượt 100.000 psi của bong bóng hơi implode; bộ lót tôi cứng chỉ kéo dài tuổi thọ. Ảnh gốc: Jon Monsen. Đây là bản vẽ lại dạng vector, đã đơn giản hóa.",
                "Figure 15.5 · Simplified vector redrawing of the source photo: on the left the plug shaft is intact, while on the right the parabolic plug tip has been about half eaten away by cavitation, with dense pitting; below it a seat ring is damaged at its bore. External sound above 80 dBA can cause similar destruction; Jon Monsen suggests 85 dBA for 4–6 in valves, 90 dBA for 8–14 in and 95 dBA for larger sizes. No known trim material withstands the imploding-bubble impact pressures exceeding 100,000 psi; hardened trim only prolongs service life. Source photo: Jon Monsen. This is a simplified vector redrawing.",
                "Sơ đồ nút van bị xâm thực ăn mòn một nửa đầu parabol và vòng đế van bị rỗ; chú thích ngưỡng ồn và giới hạn vật liệu.",
                "Vector sketch of a pitted, half-destroyed parabolic plug tip and a damaged seat ring bore")
