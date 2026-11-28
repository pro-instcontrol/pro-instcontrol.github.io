# -*- coding: utf-8 -*-
"""Vector redraws of Figures 13.6-13.12 in A. McMillan, *Electrical
Installations in Hazardous Areas*, Chapter 13 "Intrinsic safety 'i'".

All seven drawings are simplified vector redraws of the rendered pages
p368-p373 and p382.  The printed English captions, including their Note
lines and quirks, are reproduced verbatim with a bilingual prefix:
"threshold/inductive", the literal "<24 V", "0.5" with no unit, the two
printed "1.000" axis ends, the lower-case "voltage/current profile"
versus "Voltage current profile", and the ampersand of "fixed & sealed"
are all retained in the English strings.  Printed ticks, curve labels and
component call-outs are transcribed onto the drawings; descriptive
call-outs are also localized in Vietnamese.  Each public callable returns
the standard five-tuple through ``vfig._fig()`` and is registered in
``FIGS`` by the ``_reg`` decorator.
"""
import sys
import os
import math

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

from vfig import (BLUE, GREEN, GREY, INK, PAPER, RED, _f, _arrow, _circle,
                  _defs, _fig, _line, _path, _poly, _rect, _txt, svg)

FIGS = {}


def _reg(f):
    FIGS[f.__name__] = f()
    return f


def esc(s):
    """Literal Unicode throughout; XML-significant characters are escaped."""
    return (str(s).replace("&", "&amp;")
            .replace("<", "&lt;").replace(">", "&gt;"))


def T(x, y, s, size=8.0, **kw):
    """One canvas text item, clamped to the 6.8-9.5 px contract."""
    size = max(6.8, min(9.5, size))
    return _txt(x, y, esc(s), size, **kw)


# ------------------------------------------------------------------ helpers

def _title(o, n, vi, en, size=7.2):
    o.append(T(340, 15, "Hình 13.%d · %s / Figure 13.%d · %s"
               % (n, vi, n, en), size, color=INK, weight="600"))


def _sub(o, s, size=6.8):
    o.append(T(340, 29, s, max(6.8, size), color=GREY))


def _bi(o, x, y, vi, en, size=6.8, weight=""):
    """Vietnamese call-out with the printed English term beneath it."""
    size = max(6.8, size)
    o.append(T(x, y, vi, size, color=INK, weight=weight))
    o.append(T(x, y + size + 1.5, "(" + en + ")", size, color=GREY))


def _lines(o, x, y, items, size=6.8, leading=None, anchor="middle",
           color=INK, weight=""):
    leading = leading or (size + 1.6)
    for i, s in enumerate(items):
        o.append(T(x, y + i * leading, s, size, anchor=anchor,
                   color=color, weight=weight))


def _lead(x1, y1, x2, y2, sw=0.8, color=INK):
    return _arrow(x1, y1, x2, y2, sw=sw, color=color, head="a7")


def _rot(x, y, s, size=7.4, color=GREY):
    """Rotated axis title, explicitly escaped."""
    return ('<text x="%s" y="%s" transform="rotate(-90 %s %s)" '
            'style="font:%spx Inter,Helvetica,sans-serif;fill:%s">%s</text>'
            % (_f(x), _f(y), _f(x), _f(y), size, color, esc(s)))


def _plotbox(o, x0, y0, w, h):
    o.append(_rect(x0, y0, w, h, fill="#ffffff", sw=1.0))


def _px(v, x0, x1, lo, hi):
    return x0 + (math.log10(v) - math.log10(lo)) / (
        math.log10(hi) - math.log10(lo)) * (x1 - x0)


def _py(v, y0, y1, lo, hi):
    return y1 - (math.log10(v) - math.log10(lo)) / (
        math.log10(hi) - math.log10(lo)) * (y1 - y0)


def _loggrid(o, x0, y0, x1, y1, xlo, xhi, ylo, yhi):
    """Log-log grid: heavier decade lines, lighter 2-9 minor lines."""
    for dv in range(int(round(math.log10(xlo))),
                    int(round(math.log10(xhi))) + 1):
        for k in range(1, 10):
            v = (10 ** dv) * k
            if v < xlo - 1e-9 or v > xhi + 1e-9:
                continue
            px = _px(v, x0, x1, xlo, xhi)
            o.append(_line(px, y0, px, y1, sw=0.9 if k == 1 else 0.45,
                           color="#9a9a9a" if k == 1 else "#cccccc"))
    for dv in range(int(round(math.log10(ylo))),
                    int(round(math.log10(yhi))) + 1):
        for k in range(1, 10):
            v = (10 ** dv) * k
            if v < ylo - 1e-9 or v > yhi + 1e-9:
                continue
            py = _py(v, y0, y1, ylo, yhi)
            o.append(_line(x0, py, x1, py, sw=0.9 if k == 1 else 0.45,
                           color="#9a9a9a" if k == 1 else "#cccccc"))


def _xticks(o, x0, x1, y1, lo, hi, ticks, label_y, size=6.8):
    for v, lab in ticks:
        px = _px(v, x0, x1, lo, hi)
        o.append(_line(px, y1, px, y1 + 3, sw=0.8))
        o.append(T(px, label_y, lab, size, color=INK))


def _yticks(o, x0, y0, y1, lo, hi, ticks, size=6.8):
    for v, lab in ticks:
        py = _py(v, y0, y1, lo, hi)
        o.append(_line(x0 - 3, py, x0, py, sw=0.8))
        o.append(T(x0 - 6, py + 2.4, lab, size, anchor="end", color=INK))


def _logline(pts, x0, x1, y0, y1, xlo, xhi, ylo, yhi, color=INK, sw=1.7,
             dash=""):
    mapped = [(_px(a, x0, x1, xlo, xhi), _py(b, y0, y1, ylo, yhi))
              for a, b in pts]
    return _poly(mapped, fill="none", sw=sw, color=color, dash=dash)


def _dot(x, y, r=2.0, fill=INK):
    return _circle(x, y, r, fill=fill, sw=0)


def _note(o, y, vi, en):
    o.append(T(340, y, vi, 6.8, color=INK))
    o.append(T(340, y + 12, en, 6.8, color=INK))


# ------------------------------------------------------------------ 13.6

@_reg
def fig_f1306():
    """Figure 13.6 - inductive-circuit ignition thresholds below 24 V."""
    w, h = 680, 392
    o = [_defs(), _rect(0, 0, w, h, fill=PAPER, sw=0)]
    _title(o, 6, "Ngưỡng đánh lửa/mạch cảm ứng ở <24 V",
           "Ignition threshold/inductive circuits at <24 V", 7.2)
    _sub(o, "Đồ thị log-log · L mH theo dòng đánh lửa nhỏ nhất I A / "
            "Log-log plot · inductance against minimum igniting current", 6.8)

    x0, x1, y0, y1 = 74, 592, 48, 318
    _plotbox(o, x0, y0, x1 - x0, y1 - y0)
    _loggrid(o, x0, y0, x1, y1, 0.01, 10, 0.01, 100)

    yt = [(100, "100"), (30, "30"), (10, "10"), (3, "3"), (1, "1"),
          (0.3, "0.3"), (0.1, "0.1"), (0.03, "0.03"), (0.01, "0.01")]
    xt = [(0.01, "0.01"), (0.03, "0.03"), (0.1, "0.1"), (0.3, "0.3"),
          (1, "1"), (3, "3"), (10, "10")]
    _yticks(o, x0, y0, y1, 0.01, 100, yt)
    _xticks(o, x0, x1, y1, 0.01, 10, xt, y1 + 13)
    o.append(T(340, y1 + 27, "Minimum igniting current I, A", 7.4, color=GREY))
    o.append(_rot(20, (y0 + y1) / 2 + 46, "Inductance L, mH", 7.4))

    # The common 40 uJ asymptote, then the fan of voltage curves below it.
    o.append(_logline([(0.018, 100), (0.30, 2.0), (2.8, 0.012)],
                      x0, x1, y0, y1, 0.01, 10, 0.01, 100,
                      color=INK, sw=2.0))
    fan = [
        ("24V", (0.12, 3.0), (0.16, 0.011)),
        ("22V", (0.14, 3.0), (0.23, 0.011)),
        ("20V", (0.16, 3.0), (0.34, 0.011)),
        ("18V", (0.20, 3.4), (0.62, 0.011)),
        ("16V", (0.24, 3.8), (0.95, 0.011)),
        ("12V", (0.22, 2.4), (2.05, 0.011)),
        ("8V", (0.28, 2.4), (3.05, 0.011)),
        ("4V", (0.36, 2.4), (4.40, 0.011)),
    ]
    for lab, a, b in fan:
        o.append(_logline([a, b], x0, x1, y0, y1, 0.01, 10, 0.01, 100,
                          color="#333333", sw=1.3))

    # 40 uJ arrow onto the common line.
    o.append(T(352, 96, "40 µJ", 7.4, color=INK))
    o.append(_lead(346, 100, 300, 119))

    # Right-hand voltage call-outs.
    for lab, ty, tx, ly in [("4V", 256, 2.75, 0.052),
                            ("8V", 271, 3.60, 0.038),
                            ("12V", 286, 4.55, 0.026)]:
        o.append(T(566, ty, lab, 6.8, color=INK))
        o.append(_lead(558, ty - 1, _px(tx, x0, x1, 0.01, 10),
                       _py(ly, y0, y1, 0.01, 100)))

    # Bottom-left and lower-middle voltage call-outs.
    for lab, ty, tx in [("24V", 290, 0.16), ("22V", 302, 0.23),
                        ("20V", 314, 0.34)]:
        o.append(T(96, ty, lab, 6.8, color=INK))
        o.append(_lead(122, ty - 2, _px(tx, x0, x1, 0.01, 10),
                       _py(0.013, y0, y1, 0.01, 100)))
    for lab, ty, tx in [("16V", 298, 0.95), ("18V", 312, 0.62)]:
        o.append(T(404, ty, lab, 6.8, color=INK))
        o.append(_lead(394, ty - 2, _px(tx, x0, x1, 0.01, 10),
                       _py(0.014, y0, y1, 0.01, 100)))

    _note(o, 364,
          "Lưu ý: Ngưỡng đánh lửa của mạch cảm ứng được chỉ ra trong Hình 13.4 "
          "đối với các giá trị nhỏ hơn 24 V",
          "Note: Ignition thresholds for inductive circuit shown in Fig. 13.4 "
          "for values of less than 24 V")

    return _fig(svg(w, h, "".join(o), esc("Fig 13.6")),
                "Hình 13.6 · Ngưỡng đánh lửa/mạch cảm ứng ở <24 V. Lưu ý: "
                "Ngưỡng đánh lửa của mạch cảm ứng được chỉ ra trong Hình 13.4 "
                "đối với các giá trị nhỏ hơn 24 V",
                "Figure 13.6 · Ignition threshold/inductive circuits at <24 V. "
                "Note: Ignition thresholds for inductive circuit shown in "
                "Fig. 13.4 for values of less than 24 V",
                "Đồ thị log-log có trục tung Inductance L, mH từ 0,01 đến 100 mH "
                "và trục hoành Minimum igniting current I, A từ 0,01 đến 10 A. "
                "Một đường chéo dày đi từ góc trên bên trái xuống dưới, được mũi "
                "tên 40 µJ chỉ vào; từ vùng khoảng 1 mH nó tách thành nhiều "
                "đường dốc dần xuống đáy. Các nhãn 4V, 8V, 12V được đặt ở phía "
                "bên phải với mũi tên chỉ vào ba đường chéo ngoài cùng, còn "
                "16V, 18V, 20V, 22V, 24V được đặt gần đáy với mũi tên chỉ vào "
                "các đường gần thẳng đứng hơn. Vùng dưới các đường là vùng an "
                "toàn về năng lượng cảm ứng",
                "A log-log chart with the vertical axis Inductance L, mH running "
                "from 0.01 to 100 mH and the horizontal axis Minimum igniting "
                "current I, A from 0.01 to 10 A. A heavy diagonal runs down from "
                "the upper left, picked out by the 40 µJ arrow, then fans into "
                "steeper lines below about 1 mH. The 4V, 8V and 12V labels at "
                "the right point to the three outer diagonals, while 16V, 18V, "
                "20V, 22V and 24V near the foot point to the nearly vertical "
                "branches. Points below the curves lie under the inductive "
                "ignition threshold")


# ------------------------------------------------------------------ 13.7

@_reg
def fig_f1307():
    """Figure 13.7 - capacitive spark production test circuit."""
    w, h = 680, 320
    o = [_defs(), _rect(0, 0, w, h, fill=PAPER, sw=0)]
    _title(o, 7, "Phát tia lửa điện dung", "Capacitive spark production", 7.2)
    _sub(o, "Sơ đồ thử · nguồn một chiều, điện trở hạn dòng R, tụ C và thiết bị thử tia lửa / "
            "Test circuit · dc source, limiting resistor, capacitor and spark test apparatus", 6.8)

    # Supply branch, top resistor and the two parallel output branches.
    lx, rx, ty, by = 150, 470, 84, 226
    o.append(_line(lx, ty, 232, ty, sw=1.4))
    zig = []
    for i in range(8):
        zig.append((232 + i * 10, ty if i % 2 == 0 else ty - 9))
    zig.append((312, ty))
    o.append(_poly(zig, fill="none", sw=1.5))
    o.append(_line(312, ty, rx, ty, sw=1.4))
    o.append(_line(lx, by, rx, by, sw=1.4))

    o.append(_circle(lx, 134, 3.2, fill="#ffffff", sw=1.2))
    o.append(_circle(lx, 182, 3.2, fill="#ffffff", sw=1.2))
    o.append(T(lx + 10, 138, "+", 8.0, color=INK))
    o.append(T(lx + 10, 186, "−", 8.0, color=INK))
    o.append(_line(lx, ty, lx, 134, sw=1.4))
    o.append(_line(lx, 182, lx, by, sw=1.4))
    o.append(_lead(128, 126, 128, 190, sw=1.0))
    o.append(T(120, 158, "V", 8.0, color=INK, anchor="end"))

    # Variable-resistor wiper across R.
    o.append(_line(244, ty + 14, 300, ty - 17, sw=1.2))
    o.append(_lead(300, ty - 17, 288, ty - 9, sw=1.0))

    # Capacitor branch: two horizontal plates in a vertical conductor.
    cx = 400
    o.append(_circle(cx, ty, 2.4, fill=INK, sw=0))
    o.append(_line(cx, ty, cx, 156, sw=1.4))
    o.append(_rect(cx - 20, 156, 40, 10, fill=INK, sw=0))
    o.append(_rect(cx - 20, 169, 40, 10, fill=INK, sw=0))
    o.append(_line(cx, 179, cx, by, sw=1.4))
    o.append(_circle(cx, by, 2.4, fill=INK, sw=0))

    # Spark test apparatus: opposed solid triangles with a small gap.
    o.append(_poly([(rx, 150), (rx - 13, 132), (rx + 13, 132)],
                   fill=INK, sw=0, close=True))
    o.append(_poly([(rx, 158), (rx - 13, 176), (rx + 13, 176)],
                   fill=INK, sw=0, close=True))
    o.append(_line(rx, ty, rx, 132, sw=1.4))
    o.append(_line(rx, 176, rx, by, sw=1.4))

    _bi(o, 190, 52, "Điện trở hạn dòng", "Limiting resistor (Note 1)", 6.8)
    o.append(_lead(190, 62, 256, 73))
    o.append(T(272, 70, "R", 8.5, color=INK))
    _bi(o, 62, 108, "Điện áp nguồn một chiều", "dc supply voltage", 6.8)
    o.append(_lead(126, 116, 146, 134))
    _bi(o, 350, 118, "Tụ điện", "Capacitor", 6.8)
    o.append(_lead(382, 132, 390, 158))
    o.append(T(370, 178, "C", 8.5, color=INK))
    _bi(o, 556, 116, "Thiết bị thử tia lửa", "Spark test apparatus", 6.8)
    o.append(_lead(544, 130, 492, 155))

    _note(o, 252,
          "Lưu ý: Giá trị của R luôn phải sao cho dòng điện không vượt quá 0,5, "
          "dòng ngưỡng đối với mạch điện trở – xem Hình 12.11.",
          "Note: Value of R must always be such that current does not exceed 0.5, "
          "the threshold current for resistive circuits – see Fig. 12.11.")
    o.append(T(340, 284,
               "Ngoài ra, R có thể được thay bằng công tắc mở trước khi thiết bị thử "
               "tia lửa phát tia (tia lửa đóng)", 6.8, color=INK))
    o.append(T(340, 299,
               "Alternatively, R may be replaced by a switch which opens before the "
               "spark test apparatus sparks (make spark)", 6.8, color=INK))

    return _fig(svg(w, h, "".join(o), esc("Fig 13.7")),
                "Hình 13.7 · Phát tia lửa điện dung. Lưu ý: Giá trị của R luôn phải "
                "sao cho dòng điện không vượt quá 0,5, dòng ngưỡng đối với mạch "
                "điện trở – xem Hình 12.11. Ngoài ra, R có thể được thay bằng một "
                "công tắc mở ra trước khi thiết bị thử tia lửa tạo tia lửa "
                "(tia lửa đóng)",
                "Figure 13.7 · Capacitive spark production. Note: Value of R must "
                "always be such that current does not exceed 0.5, the threshold "
                "current for resistive circuits – see Fig. 12.11. Alternatively, "
                "R may be replaced by a switch which opens before the spark test "
                "apparatus sparks (make spark)",
                "Sơ đồ mạch hình chữ nhật. Nhánh trái là nguồn một chiều với hai "
                "đầu hở đánh dấu + và − và mũi tên V chỉ chiều điện áp. Trên đỉnh "
                "mạch là điện trở zigzag R có cần chỉnh, được nhãn Limiting "
                "resistor (Note 1). Bên phải, tụ điện C gồm hai bản cực đậm nằm "
                "ngang mắc song song với thiết bị thử tia lửa gồm hai hình tam "
                "giác đỉnh hướng vào nhau. Các chú thích dưới hình nêu giới hạn "
                "0,5 không đơn vị và khả năng thay R bằng công tắc mở trước khi "
                "phát tia",
                "A rectangular circuit. The left branch is the dc supply with two "
                "open terminals marked + and − and a V arrow for the voltage; the "
                "top branch carries a zigzag variable resistor R labelled Limiting "
                "resistor (Note 1). On the right a capacitor C with two heavy "
                "horizontal plates is in parallel with the spark test apparatus, "
                "drawn as two solid triangles with their points facing across a "
                "gap. The notes below give the unitless 0.5 current limit and "
                "describe replacing R by a switch that opens before the spark")


# ------------------------------------------------------------------ 13.8

@_reg
def fig_f1308():
    """Figure 13.8 - capacitive-circuit ignition thresholds, groups II A-C."""
    w, h = 680, 392
    o = [_defs(), _rect(0, 0, w, h, fill=PAPER, sw=0)]
    _title(o, 8, "Ngưỡng đánh lửa – mạch điện dung",
           "Ignition threshold – capacitive circuits", 7.4)
    _sub(o, "Đồ thị log-log · điện dung theo điện áp đánh lửa nhỏ nhất / "
            "Log-log plot · capacitance against minimum igniting voltage", 6.8)

    x0, x1, y0, y1 = 74, 592, 48, 318
    _plotbox(o, x0, y0, x1 - x0, y1 - y0)
    _loggrid(o, x0, y0, x1, y1, 1, 1000, 0.01, 1000)

    yt = [(1000, "1.000"), (300, "300"), (100, "100"), (30, "30"),
          (10, "10"), (3, "3"), (1, "1"), (0.3, "0.3"), (0.1, "0.1"),
          (0.03, "0.03"), (0.01, "0.01")]
    xt = [(1, "1"), (3, "3"), (10, "10"), (30, "30"), (100, "100"),
          (300, "300"), (1000, "1.000")]
    _yticks(o, x0, y0, y1, 0.01, 1000, yt)
    _xticks(o, x0, x1, y1, 1, 1000, xt, y1 + 13)
    o.append(T(340, y1 + 27, "Minimum igniting voltage", 7.4, color=GREY))
    o.append(_rot(20, (y0 + y1) / 2 + 34, "Capacitance", 7.4))

    curves = [
        ("II C", [(6, 1000), (10, 200), (25, 20), (45, 2), (85, 0.01)],
         348, 290, 58),
        ("II B", [(9, 1000), (15, 200), (45, 20), (110, 2), (240, 0.01)],
         428, 290, 165),
        ("II A", [(14, 1000), (22, 200), (75, 20), (180, 2), (600, 0.01)],
         556, 270, 430),
    ]
    for lab, pts, lx, ly, tx in curves:
        o.append(_logline(pts, x0, x1, y0, y1, 1, 1000, 0.01, 1000,
                          color=INK, sw=1.8))
        o.append(_lead(lx - 4, ly - 2,
                       _px(tx, x0, x1, 1, 1000),
                       _py(0.035, y0, y1, 0.01, 1000)))
        o.append(T(lx, ly, lab, 7.2, color=INK,
                   anchor="start" if lx > 500 else "middle"))

    o.append(T(340, 364,
               "Các đường II A, II B, II C: cùng độ dốc, nhóm nhạy hơn nằm bên trái / "
               "Parallel II A, II B and II C thresholds: the more sensitive group lies to the left",
               6.8, color=INK))

    return _fig(svg(w, h, "".join(o), esc("Fig 13.8")),
                "Hình 13.8 · Ngưỡng đánh lửa – mạch điện dung",
                "Figure 13.8 · Ignition threshold – capacitive circuits",
                "Đồ thị log-log có trục tung Capacitance và trục hoành Minimum "
                "igniting voltage; cả hai đầu giá trị cao đều được in là 1.000. "
                "Ba đường chéo song song dốc xuống từ trái sang phải, trong đó "
                "đường II C nằm xa nhất bên trái, II B ở giữa và II A ở bên phải. "
                "Mũi tên chữ II C, II B, II A ở gần đáy chỉ lần lượt vào ba "
                "đường. Với cùng một điện dung, điện áp đánh lửa tăng dần từ "
                "nhóm IIC đến IIA",
                "A log-log chart with a Capacitance ordinate and a Minimum "
                "igniting voltage abscissa; both high ends are printed literally "
                "as 1.000. Three parallel diagonals slope down to the right, "
                "II C farthest left, II B in the middle and II A farthest right. "
                "Small arrows by the II C, II B and II A labels near the foot "
                "identify each curve. At a given capacitance the igniting "
                "voltage rises from group IIC to group IIA")


# ------------------------------------------------------------------ 13.9

@_reg
def fig_f1309():
    """Figure 13.9 - resistive and voltage-limited constant-current circuits."""
    w, h = 680, 430
    o = [_defs(), _rect(0, 0, w, h, fill=PAPER, sw=0)]
    _title(o, 9, "Ngưỡng đánh lửa – mạch điện trở và mạch dòng không đổi giới hạn áp",
           "Ignition threshold – resistive and voltage limited constant current circuits", 7.0)
    _sub(o, "Bốn hình · hai sơ đồ mạch và hai đường đặc tính tải / "
            "Four panels · two test circuits and two load profiles", 6.8)

    # ---- upper-left: resistively limited circuit
    o.append(_line(118, 68, 180, 68, sw=1.4))
    zig = [(180 + i * 9, 68 if i % 2 == 0 else 59) for i in range(8)]
    zig.append((252, 68))
    o.append(_poly(zig, fill="none", sw=1.4))
    o.append(_line(252, 68, 348, 68, sw=1.4))
    o.append(_line(118, 164, 348, 164, sw=1.4))
    o.append(_line(118, 68, 118, 104, sw=1.4))
    o.append(_line(118, 142, 118, 164, sw=1.4))
    o.append(_circle(118, 108, 3, fill="#ffffff", sw=1.1))
    o.append(_circle(118, 146, 3, fill="#ffffff", sw=1.1))
    o.append(T(126, 112, "+", 8.0, color=INK))
    o.append(T(126, 150, "−", 8.0, color=INK))
    o.append(_poly([(348, 118), (337, 100), (359, 100)],
                   fill=INK, sw=0, close=True))
    o.append(_poly([(348, 120), (337, 138), (359, 138)],
                   fill=INK, sw=0, close=True))
    o.append(_line(348, 68, 348, 100, sw=1.4))
    o.append(_line(348, 138, 348, 164, sw=1.4))
    _bi(o, 210, 44, "Điện trở hạn dòng", "Current limiting resistor", 6.8)
    o.append(_lead(192, 52, 210, 62))
    _lines(o, 6, 96, ["Nguồn một chiều", "(dc supply voltage)"], 6.8,
           leading=9.4, anchor="start")
    o.append(_lead(100, 106, 116, 108))
    o.append(_lead(210, 174, 220, 164))
    o.append(T(226, 176, "Circuit / Mạch", 6.8, color=GREY))
    _bi(o, 300, 192, "Thiết bị thử tia lửa", "Spark test apparatus", 6.8)
    o.append(_lead(300, 184, 350, 130))

    # ---- upper-right: resistive voltage/current profile
    ox, oy = 402, 164
    o.append(_lead(ox, oy, ox, 56, sw=1.2))
    o.append(_lead(ox, oy, 626, oy, sw=1.2))
    o.append(_poly([(ox, 78), (552, oy)], fill="none", sw=1.7))
    o.append(_line(ox - 5, 78, ox + 6, 78, sw=1.0))
    o.append(_line(552, oy - 6, 552, oy + 3, sw=1.0))
    o.append(T(390, 176, "0", 6.8, color=INK))
    _lines(o, 402, 48, ["Voltage", "across", "load"], 6.8,
           leading=9.0, color=INK)
    o.append(T(452, 92, "Open circuit voltage", 6.8, color=INK))
    o.append(T(556, 140, "Short circuit current", 6.8, color=INK))
    o.append(T(500, 179, "Current through load", 6.8, color=INK))
    o.append(T(500, 192, "voltage/current profile", 6.8, color=INK))
    o.append(T(500, 206, "Resistively limited power source", 6.8, color=INK))

    o.append(_line(46, 226, 634, 226, sw=0.7, color=GREY))

    # ---- lower-left: current-limited and voltage-limited circuit
    o.append(_line(118, 270, 170, 270, sw=1.4))
    o.append(_rect(170, 260, 60, 20, fill="#e8e8e8", sw=1.1))
    o.append(_rect(170, 250, 32, 10, fill=INK, sw=0))
    o.append(_line(230, 270, 292, 270, sw=1.4))
    o.append(_line(292, 270, 292, 320, sw=1.4))
    o.append(_line(292, 320, 224, 320, sw=1.4))
    o.append(_line(224, 320, 224, 280, sw=1.4))
    o.append(_rect(186, 306, 38, 26, fill="#e8e8e8", sw=1.1))
    o.append(_line(205, 280, 205, 306, sw=1.4))
    o.append(_rect(300, 264, 40, 70, fill="#ffffff", sw=1.2))
    o.append(_line(320, 264, 320, 334, sw=1.4))
    o.append(_poly([(320, 294), (310, 304), (330, 304)],
                   fill="none", sw=1.0))
    o.append(_line(310, 303, 330, 303, sw=1.0))
    o.append(_line(340, 270, 340, 292, sw=1.4))
    o.append(_poly([(340, 290), (329, 308), (351, 308)],
                   fill=INK, sw=0, close=True))
    o.append(_poly([(340, 326), (329, 310), (351, 310)],
                   fill=INK, sw=0, close=True))
    o.append(_line(118, 360, 340, 360, sw=1.4))
    o.append(_line(118, 270, 118, 296, sw=1.4))
    o.append(_line(118, 330, 118, 360, sw=1.4))
    o.append(_circle(118, 300, 3, fill="#ffffff", sw=1.1))
    o.append(_circle(118, 338, 3, fill="#ffffff", sw=1.1))
    o.append(T(126, 304, "+", 8.0, color=INK))
    o.append(T(126, 342, "−", 8.0, color=INK))
    o.append(_line(340, 326, 340, 360, sw=1.4))
    _bi(o, 186, 234, "Mạch hạn dòng", "Current limiting circuit", 6.8)
    o.append(_lead(196, 244, 210, 266))
    _bi(o, 310, 234, "Mạch hạn áp", "Voltage limiting circuit", 6.8)
    o.append(_lead(316, 244, 318, 266))
    _lines(o, 6, 292, ["Nguồn một chiều", "(dc supply voltage)"], 6.8,
           leading=9.4, anchor="start")
    o.append(_lead(100, 300, 116, 300))
    _bi(o, 186, 376, "Thiết bị thử tia lửa", "Spark test apparatus", 6.8)
    o.append(_lead(234, 368, 340, 318))
    o.append(T(298, 394, "Circuit / Mạch", 6.8, color=GREY))

    # ---- lower-right: rectangular voltage/current profile
    ox, oy = 402, 360
    o.append(_lead(ox, oy, ox, 266, sw=1.2))
    o.append(_lead(ox, oy, 626, oy, sw=1.2))
    o.append(_poly([(ox, 282), (510, 282), (510, oy)],
                   fill="none", sw=1.7))
    o.append(T(390, 372, "0", 6.8, color=INK))
    _lines(o, 402, 258, ["Voltage", "across", "load"], 6.8,
           leading=9.0, color=INK)
    o.append(T(452, 278, "Maximum voltage", 6.8, color=INK))
    o.append(T(486, 375, "Maximum current", 6.8, color=INK))
    o.append(T(590, 373, "Current through load", 6.8, color=INK))
    o.append(T(502, 405, "Voltage current profile", 6.8, color=INK))

    o.append(T(340, 421,
               "Hai kiểu giới hạn · điện trở thuần cho đường chéo, mạch hạn áp cho đường góc vuông / "
               "Resistive source slopes; constant-current voltage-limited source is rectangular",
               6.8, color=INK))

    return _fig(svg(w, h, "".join(o), esc("Fig 13.9")),
                "Hình 13.9 · Ngưỡng đánh lửa – mạch điện trở và mạch dòng không đổi "
                "giới hạn áp",
                "Figure 13.9 · Ignition threshold – resistive and voltage limited "
                "constant current circuits",
                "Bốn hình ghép thành hai cặp. Cặp trên: bên trái là mạch thử có nguồn "
                "một chiều với đầu + và −, điện trở hạn dòng trên đỉnh và khe tia "
                "lửa ở nhánh phải; bên phải là đồ thị có trục tung Voltage across "
                "load và trục hoành Current through load, với một đường chéo từ "
                "Open circuit voltage ở đỉnh xuống Short circuit current ở đáy, "
                "chú thích Resistively limited power source và voltage/current profile "
                "viết thường. Cặp dưới: bên trái là mạch có khối hạn dòng và khối "
                "hạn áp cùng khe tia lửa; bên phải là đồ thị hình chữ nhật với "
                "Maximum voltage và Maximum current, chú thích Voltage current "
                "profile viết hoa và không có dấu gạch chéo",
                "Four panels in two pairs. The upper pair shows a test circuit on "
                "the left, with a dc supply and +/− terminals, a current limiting "
                "resistor on the top edge and a spark gap on the right branch, and "
                "on the right a graph with a Voltage across load ordinate and a "
                "Current through load abscissa: a diagonal falls from Open circuit "
                "voltage at the top to Short circuit current at the foot, captioned "
                "Resistively limited power source and the lower-case "
                "voltage/current profile. The lower pair shows a circuit with "
                "current limiting and voltage limiting blocks and a spark gap, and "
                "a rectangular profile with Maximum voltage and Maximum current, "
                "captioned Voltage current profile with a capital and no slash")


# ------------------------------------------------------------------ 13.10

@_reg
def fig_f1310():
    """Figure 13.10 - open-circuit voltage/short-circuit current thresholds."""
    w, h = 680, 392
    o = [_defs(), _rect(0, 0, w, h, fill=PAPER, sw=0)]
    _title(o, 10, "Đặc tính điện áp hở mạch/dòng ngắn mạch ngưỡng cho mạch điện trở",
           "Open circuit voltage/short circuit current threshold profile for resistive circuits", 6.9)
    _sub(o, "Đồ thị log-log · dòng ngắn mạch theo điện áp hở mạch / "
            "Log-log plot · short-circuit current against open-circuit voltage", 6.8)

    x0, x1, y0, y1 = 74, 592, 48, 318
    _plotbox(o, x0, y0, x1 - x0, y1 - y0)
    xlo, xhi, ylo, yhi = 10.0, 500.0, 0.01, 5.0
    _loggrid(o, x0, y0, x1, y1, xlo, xhi, ylo, yhi)

    yt = [(5, "5A"), (2, "2A"), (1, "1A"), (0.5, "500mA"),
          (0.2, "200mA"), (0.1, "100mA"), (0.05, "50mA"),
          (0.02, "20mA"), (0.01, "10mA")]
    xt = [(10, "10V"), (20, "20V"), (50, "50V"), (100, "100V"),
          (200, "200V"), (500, "500V")]
    _yticks(o, x0, y0, y1, ylo, yhi, yt)
    _xticks(o, x0, x1, y1, xlo, xhi, xt, y1 + 13)
    o.append(T(340, y1 + 27, "Open circuit voltage / Short circuit current", 7.0, color=GREY))

    curves = [
        ("IIC", [(15, 5), (20, 1.2), (30, 0.3), (50, 0.06),
                 (100, 0.02), (300, 0.01)], INK, 2.1),
        ("IIB", [(20, 5), (28, 1.2), (45, 0.35), (80, 0.1),
                 (150, 0.035), (320, 0.018)], "#555555", 1.4),
        ("IIA", [(23, 5), (33, 1.2), (55, 0.35), (100, 0.1),
                 (220, 0.035), (380, 0.02)], "#777777", 1.4),
    ]
    for lab, pts, color, sw in curves:
        o.append(_logline(pts, x0, x1, y0, y1, xlo, xhi, ylo, yhi,
                          color=color, sw=sw))

    for lab, lx, ly, tx, ty in [
            ("IIA", 400, 166, 72, 0.27),
            ("IIB", 400, 196, 60, 0.17),
            ("IIC", 258, 242, 50, 0.055)]:
        o.append(T(lx, ly, lab, 7.2, color=INK))
        o.append(_lead(lx - 4, ly - 2,
                       _px(tx, x0, x1, xlo, xhi),
                       _py(ty, y0, y1, ylo, yhi)))

    o.append(T(340, 364,
               "Đường IIC dày nằm bên trái, IIB và IIA mỏng dần sang phải / "
               "Thick IIC curve at left, thinner IIB and IIA thresholds to the right",
               6.8, color=INK))

    return _fig(svg(w, h, "".join(o), esc("Fig 13.10")),
                "Hình 13.10 · Đường đặc tính điện áp hở mạch/dòng ngắn mạch ngưỡng "
                "đối với mạch điện trở",
                "Figure 13.10 · Open circuit voltage/short circuit current threshold "
                "profile for resistive circuits",
                "Đồ thị log-log có các vạch dòng 5A, 2A, 1A, 500mA, 200mA, 100mA, "
                "50mA, 20mA, 10mA và các vạch điện áp 10V, 20V, 50V, 100V, 200V, "
                "500V, unit không có khoảng trắng. Ba đường cong dốc xuống bên phải: "
                "đường IIC đậm nhất nằm bên trái, IIB ở giữa và IIA mỏng nhất nằm "
                "bên phải; mũi tên chữ chỉ từng đường ở vùng 50-100 V. Với cùng một "
                "dòng ngắn mạch, điện áp hở mạch ngưỡng tăng từ IIC đến IIA",
                "A log-log chart with current ticks 5A, 2A, 1A, 500mA, 200mA, "
                "100mA, 50mA, 20mA, 10mA and voltage ticks 10V, 20V, 50V, 100V, "
                "200V, 500V with no space before the unit. Three curves fall to "
                "the right: the heavy IIC curve lies leftmost, IIB is middle and "
                "the thin IIA curve rightmost; lettered arrows in the 50-100 V "
                "region identify them. For a given short-circuit current the "
                "open-circuit voltage threshold rises from IIC to IIA")


# ------------------------------------------------------------------ 13.11

@_reg
def fig_f1311():
    """Figure 13.11 - constant-voltage current-limited threshold profiles."""
    w, h = 680, 400
    o = [_defs(), _rect(0, 0, w, h, fill=PAPER, sw=0)]
    _title(o, 11, "Đặc tính điện áp hở mạch/dòng ngắn mạch cho mạch dòng không đổi giới hạn áp",
           "Open circuit voltage/short circuit current profile for constant voltage current limited circuits", 6.8)
    _sub(o, "Trục tung gãy: 1–0,1 tuyến tính, rồi 0,09–0,01 tuyến tính / "
            "Split linear ordinate: 1 to 0.1, then 0.09 to 0.01", 6.8)

    x0, x1, y0, y1 = 74, 592, 45, 330
    _plotbox(o, x0, y0, x1 - x0, y1 - y0)
    half = (y1 - y0) / 2.0

    def y11(v):
        if v >= 0.1:
            return y0 + (1.0 - v) / 0.9 * half
        return y0 + half + (0.1 - v) / 0.09 * half

    def x11(v):
        return x0 + (v - 5.0) / 50.0 * (x1 - x0)

    # Grid: ten upper lines and nine lower lines, verticals every 5 V.
    upper = [1.0 - i * 0.1 for i in range(10)]
    lower = [0.09 - i * 0.01 for i in range(9)]
    for v in upper + lower:
        py = y11(v)
        o.append(_line(x0, py, x1, py, sw=0.8, color="#aaaaaa"))
    for v in range(5, 56, 5):
        px = x11(v)
        o.append(_line(px, y0, px, y1, sw=0.8, color="#aaaaaa"))
    o.append(_line(x0, y0, x0, y1, sw=1.2))
    o.append(_line(x0, y1, x1, y1, sw=1.2))

    for v in upper + lower:
        if v < 0.1:
            lab = "%.2f" % v
        elif abs(v - 1.0) < 1e-9:
            lab = "1"
        else:
            lab = "%.1f" % v
        py = y11(v)
        o.append(_line(x0 - 3, py, x0, py, sw=0.8))
        o.append(T(x0 - 6, py + 2.4, lab, 6.8, anchor="end", color=INK))
    for v in range(5, 51, 5):
        o.append(_line(x11(v), y1, x11(v), y1 + 3, sw=0.8))
        o.append(T(x11(v), y1 + 13, str(v), 6.8, color=INK))
    o.append(T(340, y1 + 27, "Max voltage V", 7.4, color=GREY))
    o.append(_rot(20, (y0 + y1) / 2.0, "Minimum igniting current A", 7.4))

    # Three smooth falling curves; only IIB and IIC are lettered in print.
    def f_top(v):
        return min(1.0, 0.42 + 0.58 * math.exp(-(v - 9.0) / 7.0))

    def f_mid(v):
        return min(1.0, 0.29 + 0.71 * math.exp(-(v - 13.0) / 6.5))

    def f_low(v):
        return min(1.0, 0.012 + 0.988 * math.exp(-(v - 10.0) / 9.0))

    for fn, color, sw in [(f_top, "#777777", 1.3),
                          (f_mid, INK, 1.8),
                          (f_low, INK, 1.8)]:
        pts = []
        for i in range(101):
            v = 9.0 + 46.0 * i / 100.0
            pts.append((x11(v), y11(fn(v))))
        o.append(_poly(pts, fill="none", sw=sw, color=color))

    o.append(T(420, y11(0.40), "Group IIB", 7.2, color=INK))
    o.append(_lead(414, y11(0.40) - 2, x11(38), y11(f_mid(38))))
    o.append(T(420, y11(0.14), "Group IIC", 7.2, color=INK))
    o.append(_lead(414, y11(0.14) - 2, x11(40), y11(f_low(40))))

    o.append(T(340, 378,
               "Ba đường cong · trên cùng không được gắn nhãn, giữa là Group IIB, dưới là "
               "Group IIC / Three curves · unlabelled top, Group IIB middle, Group IIC bottom",
               6.8, color=INK))
    o.append(T(340, 392,
               "Trục tung được chia thành hai khối tuyến tính xếp chồng / "
               "The ordinate is printed as two stacked linear blocks", 6.8, color=GREY))

    return _fig(svg(w, h, "".join(o), esc("Fig 13.11")),
                "Hình 13.11 · Đường đặc tính điện áp hở mạch/dòng ngắn mạch đối với "
                "mạch dòng không đổi giới hạn áp",
                "Figure 13.11 · Open circuit voltage/short circuit current profile "
                "for constant voltage current limited circuits",
                "Đồ thị có trục hoành Max voltage V từ 5 đến 50 V và trục tung "
                "Minimum igniting current A gồm hai khối tuyến tính xếp chồng: "
                "1 đến 0,1 rồi 0,09 đến 0,01. Ba đường cong giảm dần từ khoảng "
                "10-15 V ở đỉnh xuống phía bên phải; đường trên cùng không có "
                "nhãn, đường giữa được gắn Group IIB và đường thấp nhất được gắn "
                "Group IIC. Các đường gần như nằm ngang ở điện áp cao và dốc xuống "
                "khi điện áp giảm",
                "A chart with a Max voltage V abscissa from 5 to 50 V and a "
                "Minimum igniting current A ordinate drawn as two stacked linear "
                "blocks, 1 to 0.1 and then 0.09 to 0.01. Three falling curves "
                "start near 10-15 V at the top and descend to the right; the "
                "upper curve is unlabelled, the middle is Group IIB and the "
                "lowest is Group IIC. The curves flatten at high voltage and "
                "steepen as voltage falls")


# ------------------------------------------------------------------ 13.12

@_reg
def fig_f1312():
    """Figure 13.12 - typical cell construction, two cross-sections."""
    w, h = 680, 430
    o = [_defs(), _rect(0, 0, w, h, fill=PAPER, sw=0)]
    _title(o, 12, "Cấu tạo pin điển hình", "Typical cell construction", 7.6)
    _sub(o, "Hai kiểu cấu trúc · pin vỏ kim loại có vòng đệm và pin vỏ nhựa có nút xả áp / "
            "Metal cell with compressed washer; plastic cell with pressure release plug", 6.8)

    # ---- upper: upright cylindrical cell
    o.append(_path("M308 76 Q308 68 316 68 L364 68 Q372 68 372 76 "
                   "L372 196 Q372 208 360 208 L320 208 Q308 208 308 196 Z",
                   fill="#ffffff", sw=1.4))
    o.append(_path("M313 78 Q313 73 318 73 L362 73 Q367 73 367 78 "
                   "L367 194 Q367 203 358 203 L322 203 Q313 203 313 194 Z",
                   fill="none", sw=0.9, color="#888888"))
    # Cell top and the central positive electrode.
    o.append(_line(304, 73, 376, 73, sw=1.4))
    o.append(_rect(335, 58, 10, 18, fill="#dedede", sw=1.1))
    o.append(_line(340, 58, 340, 76, sw=0.6, color=GREY))
    # Compressed insulating sealing washer (hatched).
    o.append(_rect(316, 65, 19, 8, fill="url(#h6)", sw=1.0))
    o.append(_rect(345, 65, 19, 8, fill="url(#h6)", sw=1.0))
    _lines(o, 342, 42, ["Centre (positive) electrode", "fixed and sealed to cell top"],
           6.8, leading=9.4)
    o.append(_lead(340, 57, 340, 60))
    _lines(o, 172, 78, ["Compressed insulating", "sealing washer", "(Note 1)"],
           6.8, leading=9.4, anchor="end")
    o.append(_lead(232, 84, 320, 69))
    _lines(o, 502, 80, ["Cell top either metal", "or plastic"], 6.8,
           leading=9.4)
    o.append(_lead(496, 86, 372, 72))
    _lines(o, 168, 146, ["Cell body usually", "extruded metal"], 6.8,
           leading=9.4, anchor="end")
    o.append(_lead(232, 148, 310, 150))

    # ---- lower: horizontal plastic cell with release plug
    o.append(_path("M158 274 Q158 268 164 268 L516 268 Q522 268 522 274 "
                   "L522 348 Q522 354 516 354 L164 354 Q158 354 158 348 Z",
                   fill="#ffffff", sw=1.4))
    o.append(_path("M163 276 Q163 273 166 273 L514 273 Q519 273 519 276 "
                   "L519 346 Q519 351 514 351 L166 351 Q163 351 163 346 Z",
                   fill="none", sw=0.9, color="#888888"))
    o.append(_line(158, 273, 522, 273, sw=1.2))
    # Two electrode posts through the top, with small inner feet.
    for px in (202, 478):
        o.append(_rect(px - 6, 254, 12, 22, fill="#dedede", sw=1.1))
        o.append(_line(px, 256, px, 276, sw=0.6, color=GREY))
        o.append(_poly([(px, 276), (px - 10, 288), (px + 9, 288)],
                       fill="none", sw=0.9))
    # Specially fitted release plug at the middle of the top.
    o.append(_rect(326, 267, 26, 9, fill=INK, sw=0))
    o.append(_line(326, 271, 352, 271, sw=0.6, color="#ffffff"))
    _lines(o, 340, 234, ["Electrodes fixed & sealed to cell body"], 6.8)
    o.append(_lead(318, 244, 204, 256))
    o.append(_lead(362, 244, 476, 256))
    _lines(o, 566, 306, ["Plastic cell", "body"], 6.8, leading=9.4)
    o.append(_lead(552, 306, 520, 320))
    _lines(o, 340, 378, ["Pressure release plug", "(Note 2)"], 6.8,
           leading=9.4)
    o.append(_lead(340, 366, 340, 278))

    o.append(T(340, 402,
               "Lưu ý: (1) xả áp qua vòng đệm nén; (2) xả áp qua nút xả được lắp riêng / "
               "Notes: (1) release via compressed washer; (2) release via specially fitted release plug",
               6.8, color=INK))
    o.append(T(340, 418,
               "Bản in dùng 'fixed & sealed' và 'either metal or plastic' / "
               "Printed wording 'fixed & sealed' and 'either metal or plastic' is retained",
               6.8, color=GREY))

    return _fig(svg(w, h, "".join(o), esc("Fig 13.12")),
                "Hình 13.12 · Cấu tạo pin điển hình. Lưu ý: (1) Trường hợp áp suất quá "
                "cao trong pin, sự xả áp diễn ra qua vòng đệm nén. (2) Trường hợp áp "
                "suất quá cao, sự xả áp diễn ra qua nút xả được lắp riêng.",
                "Figure 13.12 · Typical cell construction. Notes: (1) In case of "
                "excessive pressure in cell, release is via compressed washer. "
                "(2) In case of excessive pressure, release is via specially fitted "
                "release plug.",
                "Hai bản cắt pin. Bên trên là pin đứng vỏ kim loại: nắp pin phẳng, "
                "điện cực dương trung tâm nhô lên và được bịt kín, hai miếng vòng đệm "
                "cách điện gạch chéo ép ở hai bên điện cực, thân vỏ có thành đôi và "
                "đáy bo tròn. Bên dưới là pin nằm ngang vỏ nhựa: hai điện cực xuyên "
                "qua nắp ở hai đầu có chân nhỏ ben trong, và một nút xả áp đậm ở giữa "
                "nắp. Các đường dẫn chữ gắn nhãn từng bộ phận; chú thích (1) và (2) "
                "mô tả đường xả áp tương ứng",
                "Two cell cross-sections. Above, an upright metal cell: a flat "
                "top, a central positive electrode protruding through the top and "
                "sealed by two hatched compressed insulating washers, and a "
                "double-walled can with a rounded base. Below, a horizontal "
                "plastic cell: two electrode posts entering through the top near "
                "each end with small feet inside, and a dark pressure release plug "
                "at the centre of the top. Leader lines name each part, and Notes "
                "(1) and (2) describe the two pressure-relief paths")
