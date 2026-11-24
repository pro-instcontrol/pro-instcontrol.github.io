# -*- coding: utf-8 -*-
"""Vector figures for Book 7 - Baumann, *Control Valve Primer*, 5th ed.

Chapter 9 "Why Most People Choose 'Equal Percentage' as a Flow Characteristic":
simplified vector re-drawings of source Figures 9-1 to 9-4.  Each function
returns the standard 5-tuple ``(svg, caption_vi, caption_en, aria_vi, aria_en)``.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from vfig import (BLUE, GREEN, GREY, INK, RED, _arrow, _box, _circle,
                  _defs, _ellipse, _f, _fig, _line, _path, _poly, _rect,
                  _txt, svg)

FIGS = {}


def _reg(f):
    FIGS[f.__name__] = f
    return f


def esc(s):
    s = str(s)
    s = s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    return s.replace('"', "&quot;")


@_reg
def fig_f91():
    """Figure 9-1 - typical inherent flow characteristics (Cv versus travel)."""
    w, h = 680, 430
    o = [_defs()]
    o.append(_txt(340, 18,
                  esc("Dac tinh luong luong vo hien dien hinh cua van cac loai"),
                  10.6, color=INK, weight="600"))
    o.append(_txt(340, 36,
                  esc("Truc ngang: % cua Cv dinh muc  -  Truc doc: % hanh trinh van "
                      "(pham vi thao tac dien hinh)"),
                  7.4, color=GREY))

    L, T, R, B = 80, 68, 622, 312
    PW, PH = R - L, B - T

    def px(v):
        return L + v / 100.0 * PW

    def py(v):
        return B - v / 100.0 * PH

    def smooth(pts, per=12):
        out = []
        n = len(pts)
        for i in range(n - 1):
            p0, p1 = pts[max(0, i - 1)], pts[i]
            p2, p3 = pts[i + 1], pts[min(n - 1, i + 2)]
            for j in range(per):
                t = j / float(per)
                t2, t3 = t * t, t * t * t
                x = 0.5 * (2 * p1[0] + (-p0[0] + p2[0]) * t
                           + (2 * p0[0] - 5 * p1[0] + 4 * p2[0] - p3[0]) * t2
                           + (-p0[0] + 3 * p1[0] - 3 * p2[0] + p3[0]) * t3)
                y = 0.5 * (2 * p1[1] + (-p0[1] + p2[1]) * t
                           + (2 * p0[1] - 5 * p1[1] + 4 * p2[1] - p3[1]) * t2
                           + (-p0[1] + 3 * p1[1] - 3 * p2[1] + p3[1]) * t3)
                out.append((x, y))
        out.append(pts[-1])
        return out

    # grid and ticks
    for g in range(0, 101, 10):
        o.append(_line(px(g), T, px(g), B, sw=0.7, color="#e6e6e6"))
        o.append(_txt(px(g), B + 13, str(g), 6.8, color=GREY))
        o.append(_line(L, py(g), R, py(g), sw=0.7, color="#e6e6e6"))
        o.append(_txt(L - 6, py(g) + 2.4, str(g), 6.8, anchor="end", color=GREY))
    o.append(_rect(L, T, PW, PH, fill="#fdfcf9", sw=1.2))
    o.append(_txt(L, 50, esc("TYPICAL OPERATION RANGE"), 7.2,
                  anchor="start", color=INK, weight="600"))
    o.append(_txt(L, 60, esc("% OF VALVE TRAVEL"), 7.2,
                  anchor="start", color=INK, weight="600"))
    o.append(_txt(R, B + 30, esc("% OF RATED Cv"), 8.2,
                  anchor="end", color=INK, weight="600"))

    # dashed IDEAL curve (sits above the real curves across the mid range)
    ideal = [(1, 2), (5, 26), (10, 43), (15, 54), (20, 61), (30, 70),
             (40, 77), (50, 82), (60, 86), (70, 89), (80, 93),
             (90, 96), (100, 100)]
    o.append(_poly([(px(x), py(y)) for x, y in smooth(ideal)],
                   sw=1.7, color=INK, dash="6 4"))

    # solid equal-percentage / typical curve: steep rise then a near plateau
    eqp = [(1, 0), (5, 22), (10, 39), (15, 49), (20, 55), (30, 64),
           (40, 69.5), (50, 73.5), (55, 77.5), (65, 80), (75, 84),
           (85, 89), (92, 94), (100, 100)]
    o.append(_poly([(px(x), py(y)) for x, y in smooth(eqp)],
                   sw=2.2, color=BLUE))

    # straight linear characteristic
    o.append(_line(px(0), py(0), px(100), py(100), sw=2.0, color=GREEN))

    # leaders and curve labels
    o.append(_line(px(40), py(80), px(35), py(76), sw=0.9, color=GREY))
    o.append(_txt(px(40) + 3, py(80) + 2.5, esc("IDEAL"), 7.4,
                  anchor="start", color=INK, weight="600"))
    o.append(_line(px(57), py(81), px(61), py(73), sw=0.9, color=GREY))
    o.append(_txt(px(62), py(72), esc("TYPICAL"), 7.4,
                  anchor="start", color=BLUE, weight="600"))
    o.append(_line(px(13), py(51), px(17), py(45), sw=0.9, color=GREY))
    o.append(_txt(px(18), py(44), esc("EQUAL PERCENTAGE"), 7.4,
                  anchor="start", color=BLUE, weight="600"))
    o.append(_line(px(41), py(38), px(45), py(32), sw=0.9, color=GREY))
    o.append(_txt(px(46), py(31), esc("LINEAR"), 7.4,
                  anchor="start", color=GREEN, weight="600"))

    o.append(_txt(340, 386,
                  esc("Duong net xanh: equal percentage / typical  -  duong net luc: "
                      "linear  -  duong dot: ideal"),
                  7.2, color=INK))
    o.append(_txt(340, 409,
                  esc("Ve lai don gian theo Baumann, Control Valve Primer, 5th ed. (Fig. 9-1)"),
                  7.0, color=GREY))

    s = svg(w, h, "".join(o),
            esc("Typical inherent flow characteristics for control valves"))
    return _fig(s,
                "Hình 9.1 · Đồ thị đơn giản hóa các đặc tính lưu lượng vốn có điển hình của van "
                "điều khiển: trục hoành là phần trăm Cv định mức (0–100), trục tung là phần trăm "
                "hành trình van (0–100). Đường đứt nét IDEAL nằm phía trên; đường liền màu xanh "
                "là đặc tính equal percentage, dốc mạnh ở đầu rồi gần như nằm ngang ở phần trên "
                "(nhãn TYPICAL); đường thẳng màu xanh lá là đặc tính linear. Đây là bản vẽ lại "
                "dạng vector, đã đơn giản hóa.",
                "Figure 9.1 · Simplified redrawing of the typical inherent flow characteristics "
                "of control valves: x is percent of rated Cv (0–100), y is percent valve travel "
                "(0–100). The dashed IDEAL curve lies above the others; the solid blue curve is "
                "the equal-percentage characteristic, rising steeply and then nearly flattening "
                "near the top (labelled TYPICAL); the straight green line is the linear "
                "characteristic. This is a simplified vector redrawing.",
                "Bieu do dac tinh luong luong vo hien: duong dot ideal, duong equal percentage "
                "dop manh roi nam ngang va duong thang linear",
                "Inherent flow characteristic chart with a dashed ideal curve, a steep then "
                "flattening equal-percentage curve and a straight linear line")


@_reg
def fig_f92():
    """Figure 9-2 - typical installed flow characteristic and stable gain band."""
    w, h = 680, 420
    o = [_defs()]
    o.append(_txt(340, 18,
                  esc("Dac tinh luong luong lap dat va vung on dinh cua he so dieu khien"),
                  10.6, color=INK, weight="600"))
    o.append(_txt(340, 36,
                  esc("Bo dieu khien chinh tai 20% luong (28% tin hieu)  -  "
                      "gioi han on dinh +/-50% quanh do doc tham chieu"),
                  7.4, color=GREY))

    L, T, R, B = 80, 58, 622, 310
    PW, PH = R - L, B - T

    def px(v):
        return L + v / 100.0 * PW

    def py(v):
        return B - v / 100.0 * PH

    def smooth(pts, per=12):
        out = []
        n = len(pts)
        for i in range(n - 1):
            p0, p1 = pts[max(0, i - 1)], pts[i]
            p2, p3 = pts[i + 1], pts[min(n - 1, i + 2)]
            for j in range(per):
                t = j / float(per)
                t2, t3 = t * t, t * t * t
                x = 0.5 * (2 * p1[0] + (-p0[0] + p2[0]) * t
                           + (2 * p0[0] - 5 * p1[0] + 4 * p2[0] - p3[0]) * t2
                           + (-p0[0] + 3 * p1[0] - 3 * p2[0] + p3[0]) * t3)
                y = 0.5 * (2 * p1[1] + (-p0[1] + p2[1]) * t
                           + (2 * p0[1] - 5 * p1[1] + 4 * p2[1] - p3[1]) * t2
                           + (-p0[1] + 3 * p1[1] - 3 * p2[1] + p3[1]) * t3)
                out.append((x, y))
        out.append(pts[-1])
        return out

    # grid and ticks
    for g in range(0, 101, 20):
        o.append(_line(px(g), T, px(g), B, sw=0.8, color="#e6e6e6"))
        o.append(_txt(px(g), B + 13, str(g), 6.8, color=GREY))
        o.append(_line(L, py(g), R, py(g), sw=0.8, color="#e6e6e6"))
        o.append(_txt(L - 6, py(g) + 2.4, str(g), 6.8, anchor="end", color=GREY))
    o.append(_rect(L, T, PW, PH, fill="#fdfcf9", sw=1.2))
    o.append(_txt(L, T - 9, esc("% FLOW"), 8.2,
                  anchor="start", color=INK, weight="600"))
    o.append(_txt(R, B + 31, esc("% SIGNAL(S)"), 8.2,
                  anchor="end", color=INK, weight="600"))

    # vertical band of stable controller gain (about 8% to 58% signal)
    o.append(_line(px(8), py(12), px(8), py(93), sw=1.0, color=GREY))
    o.append(_line(px(58), py(12), px(58), py(93), sw=1.0, color=GREY))
    o.append(_arrow(px(30), py(88), px(10), py(88), sw=1.0, color=GREY))
    o.append(_arrow(px(36), py(88), px(56), py(88), sw=1.0, color=GREY))
    for i, line in enumerate(("RANGE OF STABLE", "CONTROL FOR GIVEN",
                              "CONTROLLER SETTING", "AT 20% FLOW")):
        o.append(_txt(px(33), 62 + i * 8.5, esc(line), 7.0,
                      color=GREY, weight="600"))

    # reference constant-gain line at the tuning point and its +/- 50% limits
    o.append(_line(px(0), py(8), px(100), py(70), sw=1.3, color=INK))
    o.append(_line(px(0), py(8), px(76), py(100), sw=1.5, color=INK, dash="6 4"))
    o.append(_line(px(0), py(8), px(100), py(47), sw=1.5, color=INK, dash="6 4"))
    o.append(_txt(px(63), py(60), esc("CONSTANT GAIN"), 7.0,
                  anchor="middle", color=INK))
    o.append(_txt(px(63), py(55), esc("AT 20% FLOW"), 7.0,
                  anchor="middle", color=INK))
    o.append(_txt(px(30), py(37), esc("1.5 × CONSTANT GAIN"), 7.0,
                  anchor="middle", color=INK))
    o.append(_txt(px(82), py(41), esc("0.5 × CONSTANT GAIN"), 7.0,
                  anchor="middle", color=INK))

    # installed characteristic, S-shaped through the tuning point
    inst = [(0, 8), (10, 12), (20, 16), (28, 20), (35, 25), (40, 30),
            (47, 38), (57, 55), (65, 68), (72, 79), (78, 87),
            (88, 95), (100, 100)]
    o.append(_poly([(px(x), py(y)) for x, y in smooth(inst)],
                   sw=2.3, color=BLUE))
    o.append(_txt(px(73), py(74), esc("INSTALLED FLOW CHARACTERISTIC"), 6.9,
                  anchor="middle", color=BLUE, weight="600"))

    # the two operating limits quoted in the source caption
    o.append(_circle(px(8), py(10), 3.2, fill="#ffffff", sw=1.2, color=RED))
    o.append(_txt(px(11), py(8), esc("10% flow (8% signal)"), 6.6,
                  anchor="start", color=RED))
    o.append(_circle(px(78), py(57), 3.2, fill="#ffffff", sw=1.2, color=RED))
    o.append(_txt(px(76), py(63), esc("57% flow (78% signal)"), 6.6,
                  anchor="end", color=RED))

    o.append(_txt(340, 383,
                  esc("Duong xanh dam: dac tinh lap dat  -  duong dot: gioi han do doc "
                      "+/-50%  -  vung xam: vung on dinh"),
                  7.2, color=INK))
    o.append(_txt(340, 405,
                  esc("Ve lai don gian theo Baumann, Control Valve Primer, 5th ed. (Fig. 9-2)"),
                  7.0, color=GREY))

    s = svg(w, h, "".join(o),
            esc("Installed flow characteristic and stable controller gain range"))
    return _fig(s,
                "Hình 9.2 · Đồ thị đơn giản hóa đặc tính lưu lượng lắp đặt điển hình: trục hoành "
                "là phần trăm tín hiệu (0–100), trục tung là phần trăm lưu lượng (0–100). Đường "
                "cong chữ S màu xanh là đặc tính lắp đặt; đường liền và hai đường đứt nét là hệ "
                "số không đổi tại điểm chỉnh 20% lưu lượng (28% tín hiệu) và các giới hạn +/-50% "
                "(1,5 × và 0,5 × hệ số không đổi). Dải đứng giữa khoảng 8% và 58% tín hiệu là "
                "vùng điều khiển ổn định. Các mốc đó là 10% lưu lượng (8% tín hiệu) và 57% lưu "
                "lượng (78% tín hiệu). Đây là bản vẽ lại dạng vector, đã đơn giản hóa.",
                "Figure 9.2 · Simplified installed flow characteristic: x is percent signal "
                "(0–100), y is percent flow (0–100). The solid blue S-curve is the installed "
                "characteristic; the solid and two dashed lines are the constant gain at the "
                "tuning point of 20% flow (28% signal) and its +/-50% limits (1.5 × and 0.5 × "
                "constant gain). The vertical band between roughly 8% and 58% signal marks the "
                "range of stable controller gain. The quoted limits are 10% flow (8% signal) "
                "and 57% flow (78% signal). This is a simplified vector redrawing.",
                "Dac tinh lap dat dang ch S, duong he so khong doi va hai gioi han 1.5 lan "
                "0.5 lan, kem dai on dinh giua 8 va 58 phan tram tin hieu",
                "S-shaped installed characteristic with constant-gain lines at 1.5 and 0.5 "
                "times and a stable-gain band between 8 and 58 percent signal")


@_reg
def fig_f93():
    """Figure 9-3 - pressure distribution in a typical flow-control piping system."""
    w, h = 680, 330
    o = [_defs()]
    o.append(_txt(340, 18,
                  esc("Phan bo ap suat trong he thong ong danh cho dieu khien luong"),
                  10.6, color=INK, weight="600"))
    o.append(_txt(340, 34,
                  esc("So do don gian: bon chua nuoc 70 F  -  bom ly tam  -  ong 6 in Sch. 40 "
                      " -  van dieu khien  -  binh cong nghe"),
                  7.4, color=GREY))

    pipe_y = 112

    # storage tank
    o.append(_rect(34, 84, 52, 58, fill="#d7d7d7", sw=1.2))
    o.append(_ellipse(60, 84, 26, 8, fill="#eeeeee", sw=1.0))
    o.append(_txt(60, 58, esc("70 F"), 8.0, color=INK, weight="600"))
    o.append(_txt(60, 69, esc("Water"), 8.0, color=INK, weight="600"))

    # centrifugal pump and its base
    o.append(_line(86, pipe_y, 96, pipe_y, sw=3.0, color=GREY))
    o.append(_circle(116, pipe_y, 20, fill="#c9c9c9", sw=1.2))
    o.append(_poly([(102, 132), (130, 132), (116, 150)],
                   fill="#bdbdbd", sw=1.1, color=INK, close=True))
    o.append(_line(136, pipe_y, 148, pipe_y, sw=3.0, color=GREY))

    # pump discharge gauge Pp
    o.append(_line(148, pipe_y + 2, 148, 134, sw=0.9, color=GREY))
    o.append(_circle(148, 145, 11, fill="#eeeeee", sw=1.1))
    o.append(_txt(148, 148, esc("Pp"), 7.4, color=INK, weight="600"))

    # reducers either side of the straight run
    o.append(_poly([(160, 99), (160, 125), (178, pipe_y)],
                   fill="url(#h6)", sw=1.1, color=INK, close=True))
    o.append(_line(178, pipe_y, 360, pipe_y, sw=5.0, color="#b9c3cc"))
    o.append(_line(178, pipe_y, 360, pipe_y, sw=0.7, color=INK))
    o.append(_poly([(360, pipe_y), (378, 99), (378, 125)],
                   fill="url(#h6)", sw=1.1, color=INK, close=True))

    # flow controller station
    o.append(_line(250, pipe_y, 250, 96, sw=0.9, color=GREY))
    o.append(_circle(250, 86, 10, fill="#eef3fb", sw=1.1))
    o.append(_txt(250, 89, esc("FC"), 7.4, color=BLUE, weight="600"))
    o.append(_txt(269, 89, esc("6 in Sch. 40"), 7.6,
                  anchor="start", color=INK, weight="600"))
    o.append(_txt(270, 135, esc("580 ft (equiv. pipe & fittings)"), 7.2,
                  anchor="start", color=GREY))
    o.append(_arrow(214, pipe_y, 236, pipe_y, sw=1.3, color=BLUE))

    # upstream gauge P1
    o.append(_line(388, pipe_y + 2, 388, 134, sw=0.9, color=GREY))
    o.append(_circle(388, 145, 11, fill="#eeeeee", sw=1.1))
    o.append(_txt(388, 148, esc("P1"), 7.4, color=INK, weight="600"))

    # control valve body and actuator
    o.append(_poly([(396, 99), (396, 125), (416, pipe_y)],
                   fill="url(#h6)", sw=1.2, color=INK, close=True))
    o.append(_poly([(436, 99), (436, 125), (416, pipe_y)],
                   fill="url(#h6)", sw=1.2, color=INK, close=True))
    o.append(_line(416, 99, 416, 80, sw=1.2, color=INK))
    o.append(_path("M404,80 A12,12 0 0 1 428,80 Z", fill="#c9c9c9", sw=1.1))

    # downstream gauge P2
    o.append(_line(450, pipe_y + 2, 450, 134, sw=0.9, color=GREY))
    o.append(_circle(450, 145, 11, fill="#eeeeee", sw=1.1))
    o.append(_txt(450, 148, esc("P2"), 7.4, color=INK, weight="600"))

    # downstream pipe and vessel inlet gauge
    o.append(_line(452, pipe_y, 556, pipe_y, sw=5.0, color="#b9c3cc"))
    o.append(_line(452, pipe_y, 556, pipe_y, sw=0.7, color=INK))
    o.append(_txt(504, 135, esc("230 ft"), 7.2, color=GREY))
    o.append(_arrow(486, pipe_y, 508, pipe_y, sw=1.3, color=BLUE))
    o.append(_line(556, pipe_y + 2, 556, 134, sw=0.9, color=GREY))
    o.append(_circle(556, 145, 13, fill="#eeeeee", sw=1.1))
    o.append(_txt(556, 143, esc("24.7"), 6.4, color=INK, weight="600"))
    o.append(_txt(556, 153, esc("P3"), 6.0, color=GREY))

    # process vessel with inlet and outlet arrows
    o.append(_rect(568, 74, 48, 76, fill="#bdbdbd", sw=1.2))
    o.append(_ellipse(592, 74, 24, 7, fill="#d2d2d2", sw=1.0))
    o.append(_arrow(578, 48, 578, 70, sw=1.2, color=INK))
    o.append(_arrow(578, 70, 600, 70, sw=1.2, color=INK))
    o.append(_arrow(616, pipe_y, 652, pipe_y, sw=1.3, color=INK))

    # compact data table carrying every number of both source rows
    tx, ty, tw, rh = 32, 180, 616, 31
    cw = tw / 7.0
    header = ("Flow\ngpm", "Pp\npsia", "Pipe Loss\n(up)", "P1\npsia",
              "Pipe Loss\n(down)", "P2\npsia", "ΔP")
    rows = [("80", "56.8", "0.1", "56.7", "0.05", "24.7", "32"),
            ("550", "51.7", "5", "46.7", "2", "26.7", "20")]

    def cell(x, y, ww, hh, lines, size=8.0, weight=""):
        o.append(_rect(x, y, ww, hh, fill="#ffffff", sw=0.9))
        ls = lines.split("\n")
        cy = y + hh / 2.0 - (len(ls) - 1) * size * 0.55
        for i, ln in enumerate(ls):
            o.append(_txt(x + ww / 2.0, cy + i * size * 1.15, esc(ln),
                          size, color=INK, weight=weight))

    for i, lab in enumerate(header):
        cell(tx + i * cw, ty, cw, rh, lab, size=7.4, weight="600")
    for r, row in enumerate(rows):
        for i, val in enumerate(row):
            cell(tx + i * cw, ty + rh * (r + 1), cw, rh, val, size=8.6)

    o.append(_txt(340, 310,
                  esc("Bang so lieu: hai dieu kien luong 80 va 550 gpm  -  "
                      "Pp/P1/P2 tinh bang psia  -  ΔP = P1 - P2"),
                  7.0, color=GREY))
    o.append(_txt(340, 325,
                  esc("Ve lai don gian theo Baumann, Control Valve Primer, 5th ed. (Fig. 9-3)"),
                  7.0, color=GREY))

    s = svg(w, h, "".join(o),
            esc("Pressure distribution in a typical piping system for flow control"))
    return _fig(s,
                "Hình 9.3 · Sơ đồ đơn giản hóa phân bố áp suất trong hệ thống ống dẫn: nước "
                "70 °F từ bồn chưa qua bơm ly tâm (Pp), ống 6 in Sch. 40 dài 580 ft tương đương "
                "kể cả bốn cút, van điều khiển (P1 trước, P2 sau), rồi 230 ft ống đến bình công "
                "nghệ. Bảng số liệu gồm hai chế độ 80 và 550 gpm: Pp 56,8/51,7 psia, tổn thất "
                "ống trước 0,1/5 psi, P1 56,7/46,7 psia, tổn thất van 0,05/2 psi, P2 24,7/26,7 "
                "psia và ΔP 32/20 psi. Đây là bản vẽ lại dạng vector, đã đơn giản hóa.",
                "Figure 9.3 · Simplified pressure-distribution schematic: 70 °F water from a "
                "storage tank through a centrifugal pump (Pp), 6 in Sch. 40 pipe of 580 ft "
                "equivalent length including four elbows, the control valve (P1 upstream, P2 "
                "downstream), then 230 ft of pipe to the process vessel. The compact table "
                "keeps both source rows: 80 and 550 gpm; Pp 56.8/51.7 psia; upstream pipe loss "
                "0.1/5 psi; P1 56.7/46.7 psia; valve loss 0.05/2 psi; P2 24.7/26.7 psia; "
                "ΔP 32/20 psi. This is a simplified vector redrawing.",
                "So do phan bo ap suat: bon chua, bom, ong 580 ft, van, ong 230 ft va "
                "binh, kem bang hai hang so lieu 80 va 550 gpm",
                "Pressure-distribution schematic with tank, pump, 580 ft pipe, valve, "
                "230 ft pipe, vessel and a two-row data table")


@_reg
def fig_f94():
    """Figure 9-4 - installed characteristic of a 6 in butterfly valve, curves A and B."""
    w, h = 680, 430
    o = [_defs()]
    o.append(_txt(340, 18,
                  esc("Dac tinh luong luong lap dat: duong A va duong B sau khi "
                      "chinh sua tin hieu ra"),
                  10.2, color=INK, weight="600"))
    o.append(_txt(340, 36,
                  esc("Van canh buom goc 6 in  -  truc ngang % tin hieu  -  truc doc luong GPM"),
                  7.4, color=GREY))

    L, T, R, B = 80, 52, 622, 330
    PW, PH = R - L, B - T
    YMAX = 1750

    def px(v):
        return L + v / 100.0 * PW

    def py(v):
        return B - v / float(YMAX) * PH

    def smooth(pts, per=12):
        out = []
        n = len(pts)
        for i in range(n - 1):
            p0, p1 = pts[max(0, i - 1)], pts[i]
            p2, p3 = pts[i + 1], pts[min(n - 1, i + 2)]
            for j in range(per):
                t = j / float(per)
                t2, t3 = t * t, t * t * t
                x = 0.5 * (2 * p1[0] + (-p0[0] + p2[0]) * t
                           + (2 * p0[0] - 5 * p1[0] + 4 * p2[0] - p3[0]) * t2
                           + (-p0[0] + 3 * p1[0] - 3 * p2[0] + p3[0]) * t3)
                y = 0.5 * (2 * p1[1] + (-p0[1] + p2[1]) * t
                           + (2 * p0[1] - 5 * p1[1] + 4 * p2[1] - p3[1]) * t2
                           + (-p0[1] + 3 * p1[1] - 3 * p2[1] + p3[1]) * t3)
                out.append((x, y))
        out.append(pts[-1])
        return out

    def rot_txt(x, y, s, ang, size=7.0, color=INK):
        return ('<text x="%s" y="%s" text-anchor="middle" '
                'style="font:%spx Inter,Helvetica,sans-serif;fill:%s;'
                'font-weight:600" transform="rotate(%s,%s,%s)">%s</text>'
                % (_f(x), _f(y), size, color, _f(ang), _f(x), _f(y), esc(s)))

    # grid, ticks and frame
    for g in range(0, 101, 10):
        o.append(_line(px(g), T, px(g), B, sw=0.7, color="#e6e6e6"))
        if g % 20 == 0:
            o.append(_txt(px(g), B + 13, str(g), 6.8, color=GREY))
    for g in range(0, YMAX + 1, 250):
        o.append(_line(L, py(g), R, py(g), sw=0.7, color="#e6e6e6"))
        if g % 500 == 0:
            o.append(_txt(L - 6, py(g) + 2.4, str(g), 6.8,
                          anchor="end", color=GREY))
    o.append(_rect(L, T, PW, PH, fill="#fdfcf9", sw=1.2))
    o.append(_txt(L, T - 9, esc("FLOW, GPM"), 8.2,
                  anchor="start", color=INK, weight="600"))
    o.append(_txt(R, B + 31, esc("% OF SIGNAL"), 8.2,
                  anchor="end", color=INK, weight="600"))

    # dashed gain references
    o.append(_line(px(0), py(0), px(58.3), py(YMAX),
                   sw=1.4, color=INK, dash="7 5"))
    o.append(_line(px(30), py(230), px(100), py(1300),
                   sw=1.3, color=GREY, dash="6 5"))
    o.append(_line(px(40), py(1080), px(78), py(1240),
                   sw=1.2, color=GREY, dash="5 4"))

    # curve A - actual installed characteristic, steep then saturating near 1250 gpm
    curve_a = [(0, 0), (5, 140), (10, 280), (15, 390), (20, 470),
               (25, 620), (30, 830), (35, 960), (40, 1030), (45, 1080),
               (50, 1120), (60, 1175), (70, 1205), (80, 1230),
               (90, 1250), (100, 1270)]
    o.append(_poly([(px(x), py(y)) for x, y in smooth(curve_a)],
                   sw=2.3, color=INK))
    # x markers retained from the source at the measured operating points
    for mx, my in ((10, 280), (20, 470), (45, 1080), (75, 1220)):
        o.append(_line(px(mx) - 4, py(my) - 4, px(mx) + 4, py(my) + 4,
                       sw=1.5, color=INK))
        o.append(_line(px(mx) - 4, py(my) + 4, px(mx) + 4, py(my) - 4,
                       sw=1.5, color=INK))

    # curve B - same system with the output signal modified
    curve_b = [(30, 230), (35, 350), (40, 470), (45, 600), (50, 720),
               (55, 820), (60, 900), (65, 990), (70, 1050), (75, 1100),
               (80, 1140), (90, 1200), (100, 1240)]
    o.append(_poly([(px(x), py(y)) for x, y in smooth(curve_b)],
                   sw=2.2, color=BLUE))

    # curve labels with short leaders
    o.append(_line(px(36), py(880), px(32), py(910), sw=0.9, color=GREY))
    o.append(_txt(px(37), py(880), esc("A"), 8.0,
                  anchor="start", color=INK, weight="600"))
    o.append(_line(px(38), py(430), px(33), py(430), sw=0.9, color=GREY))
    o.append(_txt(px(39), py(430), esc("B"), 8.0,
                  anchor="start", color=BLUE, weight="600"))

    # gain and signal-modification annotations
    o.append(rot_txt(px(26), py(780),
                     "GAIN = 300 GPM/10% SIGNAL", -41.5, 7.2, INK))
    o.append(_txt(px(60), py(1290),
                  esc("GAIN = 45 GPM/10% SIGNAL"), 7.6,
                  anchor="start", color=INK, weight="600"))
    o.append(_line(px(56), py(1284), px(48), py(1130), sw=0.8, color=GREY))
    o.append(_txt(px(64), py(700), esc("WITH OUTPUT SIGNAL"), 7.2,
                  anchor="start", color=BLUE, weight="600"))
    o.append(_txt(px(64), py(645), esc("MODIFIED, So = 0.9 (Si)^2"), 7.2,
                  anchor="start", color=BLUE, weight="600"))
    o.append(_line(px(63), py(715), px(61), py(830), sw=0.9, color=GREY))

    o.append(_txt(340, 391,
                  esc("Duong den: dac tinh that (A)  -  duong xanh: tin hieu ra da chinh sua (B) "
                      " -  duong dot: do doc tham chieu"),
                  7.2, color=INK))
    o.append(_txt(340, 412,
                  esc("Ve lai don gian theo Baumann, Control Valve Primer, 5th ed. (Fig. 9-4)"),
                  7.0, color=GREY))

    s = svg(w, h, "".join(o),
            esc("Installed characteristics with gain limits and modified output signal"))
    return _fig(s,
                "Hình 9.4 · Đồ thị đơn giản hóa đặc tính lưu lượng lắp đặt của van bướm góc 6 in: "
                "trục hoành là phần trăm tín hiệu (0–100), trục tung là lưu lượng GPM (0–1500). "
                "Đường A màu đen là đặc tính lắp đặt thực tế, tăng dốc rồi bão hòa gần 1250 gpm; "
                "đường B màu xanh là cùng hệ thống sau khi chỉnh sửa tín hiệu ra theo "
                "So = 0,9 (Si)². Các ghi chú giữ lại GAIN = 300 GPM/10% SIGNAL và "
                "GAIN = 45 GPM/10% SIGNAL cùng các đường đứt nét tương ứng. Đây là bản vẽ lại "
                "dạng vector, đã đơn giản hóa.",
                "Figure 9.4 · Simplified installed-characteristic chart for a 6 in angle-seating "
                "butterfly valve: x is percent of signal (0–100), y is flow in GPM (0–1500). "
                "Curve A (black) is the actual installed characteristic, rising steeply and "
                "saturating near 1250 gpm; curve B (blue) is the same system after the output "
                "signal is modified as So = 0.9 (Si)². The annotations GAIN = 300 GPM/10% "
                "SIGNAL and GAIN = 45 GPM/10% SIGNAL are retained with their dashed reference "
                "lines. This is a simplified vector redrawing.",
                "Bieu do luong GPM theo phan tram tin hieu, duong A tang nhanh va bao hoa "
                "gan 1250, duong B thap hon sau khi chinh sua tin hieu ra",
                "Flow versus percent signal chart, steep curve A saturating near 1250 gpm and "
                "lower curve B after output-signal modification, with gain annotations")
