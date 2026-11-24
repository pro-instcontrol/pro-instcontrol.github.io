# -*- coding: utf-8 -*-
"""Vector figures for Book 7 - Baumann, *Control Valve Primer*, 5th ed.

Chapter 10: simplified vector re-drawings of source Figures 10-1 to 10-4.
Each function returns the standard 5-tuple
``(svg, caption_vi, caption_en, aria_vi, aria_en)``.
"""
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from vfig import (BLUE, FILL, GREEN, GREY, INK, RED, _arrow, _box, _circle,
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
def fig_f101():
    """Figure 10-1 - two-panel Bode chart of actuator/positioner dynamics."""
    w, h = 680, 512
    o = [_defs()]
    o.append(_txt(340, 18,
                  esc("Dap ung dong cua cum van - bo dinh vi (bode don gian)"),
                  10.6, color=INK, weight="600"))
    o.append(_txt(340, 34,
                  esc("Dai dieu chinh cua he so khuech dai va toc do anh huong den dap ung dong"),
                  7.4, color=GREY))
    o.append(_txt(340, 52, esc("BREAK FREQUENCY: 0.32 Hz / 0.75 Hz"),
                  8.0, color=INK, weight="600"))

    L, R = 88, 628
    PW = R - L
    T, B = 68, 252
    PH = B - T
    T2, B2 = 314, 454
    PH2 = B2 - T2

    def px(f):
        return L + (math.log10(f) + 2.0) / 3.0 * PW

    def py_amp(a):
        return T + (-math.log10(a)) / 2.0 * PH

    def py_phase(d):
        return T2 + (10.0 - d) / 370.0 * PH2

    def rot_txt(x, y, s, ang, size=8.2, color=INK):
        return ('<text x="%s" y="%s" text-anchor="middle" '
                'style="font:%spx Inter,Helvetica,sans-serif;fill:%s;'
                'font-weight:600" transform="rotate(%s,%s,%s)">%s</text>'
                % (_f(x), _f(y), size, color, _f(ang), _f(x), _f(y), esc(s)))

    # frames first so the grid stays visible
    o.append(_rect(L, T, PW, PH, fill="#fdfcf9", sw=1.2))
    o.append(_rect(L, T2, PW, PH2, fill="#fdfcf9", sw=1.2))

    # log-frequency grid shared by both panels
    for dec in range(-2, 2):
        for m in range(1, 10):
            f = m * (10.0 ** dec)
            if f < 0.01 - 1e-12 or f > 10.0 + 1e-12:
                continue
            xx = px(f)
            col = "#dcdcdc" if m == 1 else "#efefef"
            sw = 0.8 if m == 1 else 0.6
            o.append(_line(xx, T, xx, B, sw=sw, color=col))
            o.append(_line(xx, T2, xx, B2, sw=sw, color=col))
            if m == 1:
                o.append(_txt(xx, B + 13, "10^%d" % dec, 6.8, color=GREY))
                o.append(_txt(xx, B2 + 13, "10^%d" % dec, 6.8, color=GREY))

    # amplitude grid: 10^0, 10^-1, 10^-2 with half-decade minors
    for k in range(0, 5):
        a = 10.0 ** (-0.5 * k)
        yy = py_amp(a)
        major = (k % 2 == 0)
        o.append(_line(L, yy, R, yy, sw=0.8 if major else 0.6,
                       color="#dcdcdc" if major else "#efefef"))
        if major:
            lab = "10^0" if k == 0 else "10^-%d" % (k // 2)
            o.append(_txt(L - 6, yy + 2.4, lab, 6.8, anchor="end", color=GREY))

    # phase grid: every 45 degrees, 10 down to -360
    for d in (10, -45, -90, -135, -180, -225, -270, -315, -360):
        yy = py_phase(d)
        o.append(_line(L, yy, R, yy, sw=0.7, color="#e9e9e9"))
        o.append(_txt(L - 6, yy + 2.4, str(d), 6.6, anchor="end", color=GREY))

    o.append(rot_txt(30, (T + B) / 2.0, "AMPLITUDE", -90))
    o.append(rot_txt(30, (T2 + B2) / 2.0, "PHASE SHIFT, deg", -90))
    o.append(_txt(R, B2 + 32, esc("FREQUENCY, Hz"), 8.4,
                  anchor="end", color=INK, weight="600"))

    # annotated break frequencies on both panels
    for f in (0.32, 0.75):
        xx = px(f)
        o.append(_line(xx, T, xx, B, sw=0.9, color=GREY, dash="4 3"))
        o.append(_line(xx, T2, xx, B2, sw=0.9, color=GREY, dash="4 3"))
    o.append(_txt(px(0.32) - 4, T - 6, esc("0.32 Hz"), 6.8,
                  anchor="end", color=GREY))
    o.append(_txt(px(0.75) + 4, T - 6, esc("0.75 Hz"), 6.8,
                  anchor="start", color=GREY))

    # two response cases: second-order-style roll-off past the break frequency
    for fb, color in ((0.75, BLUE), (0.32, RED)):
        pa, pp = [], []
        for i in range(121):
            f = 10.0 ** (-2.0 + 3.0 * i / 120.0)
            r2 = (f / fb) ** 2
            pa.append((px(f), py_amp(1.0 / (1.0 + r2))))
            pp.append((px(f), py_phase(-10.0 - 170.0 * r2 / (1.0 + r2))))
        o.append(_poly(pa, sw=2.2, color=color))
        o.append(_poly(pp, sw=2.2, color=color))
        for f in (0.01, 0.03, 0.1, 0.3, 1.0, 3.0):
            r2 = (f / fb) ** 2
            o.append(_circle(px(f), py_amp(1.0 / (1.0 + r2)), 2.6,
                             fill="#ffffff", sw=1.1, color=color))
            o.append(_circle(px(f),
                             py_phase(-10.0 - 170.0 * r2 / (1.0 + r2)), 2.6,
                             fill="#ffffff", sw=1.1, color=color))

    # compact legend in the empty top-right of the amplitude panel
    o.append(_rect(458, 76, 166, 40, fill="#ffffff", sw=0.9, stroke="#cccccc"))
    o.append(_line(466, 88, 486, 88, sw=2.2, color=BLUE))
    o.append(_txt(492, 91, esc("Q = 2.4, K = 20 (0.75 Hz)"), 6.8,
                  anchor="start", color=INK))
    o.append(_line(466, 104, 486, 104, sw=2.2, color=RED))
    o.append(_txt(492, 107, esc("Q = 0.6, K = 67 (0.32 Hz)"), 6.8,
                  anchor="start", color=RED))

    o.append(_txt(340, 500,
                  esc("Ve lai don gian theo Baumann, Control Valve Primer, 5th ed. "
                      "(Fig. 10-1) - Nguon: SAMSON AG"),
                  7.0, color=GREY))

    s = svg(w, h, "".join(o),
            esc("Dynamic response Bode charts of an actuator and positioner"))
    return _fig(s,
                "Hình 10.1 · Đồ thị Bode đơn giản hóa cho thấy dải chỉnh được của hệ số khuếch đại và tốc độ ảnh hưởng thế nào đến đáp ứng động của cụm van và bộ định vị. Trục hoành chung là tần số (Hz, thang log từ 10^-2 đến 10^1); ô trên là biên độ (10^0 đến 10^-2), ô dưới là độ lệch pha (10 đến -360 độ). Hai trường hợp được gắn nhãn và đánh dấu: Q = 2.4, K = 20 (hệ số thấp hơn, nhanh hơn, tần số gãy 0,75 Hz) và Q = 0.6, K = 67 (hệ số cao hơn, chậm hơn, tần số gãy 0,32 Hz); cả hai tần số gãy đều có đường đứt nét và nhãn riêng. Đây là bản vẽ lại dạng vector, đã đơn giản hóa. (Nguồn: SAMSON AG.)",
                "Figure 10.1 · Simplified Bode charts showing how the adjustable gain and speed settings change the dynamic response of an actuator/positioner combination. The shared x-axis is frequency in Hz on a log scale from 10^-2 to 10^1; the upper plot is amplitude (10^0 to 10^-2) and the lower plot is phase shift in degrees (10 down to -360). Two cases are marked and labelled: Q = 2.4, K = 20 (lower gain, faster, break frequency 0.75 Hz) and Q = 0.6, K = 67 (higher gain, slower, break frequency 0.32 Hz); both break frequencies carry their own dashed line and label. This is a simplified vector redrawing. (Source: courtesy of SAMSON AG.)",
                "Hai biểu đồ Bode xếp chồng: biên độ và độ lệch pha theo tần số, với hai đường cong Q = 2,4, K = 20 gãy ở 0,75 Hz và Q = 0,6, K = 67 gãy ở 0,32 Hz",
                "Two stacked Bode plots of amplitude and phase versus frequency, with curves Q = 2.4, K = 20 breaking at 0.75 Hz and Q = 0.6, K = 67 breaking at 0.32 Hz")


@_reg
def fig_f102():
    """Figure 10-2 - smart valve with local mass-flow control in a cascade loop."""
    w, h = 680, 380
    o = [_defs()]
    o.append(_txt(340, 18,
                  esc("So do chuc nang: van dieu khien thong minh dieu khien luong khoi tai che"),
                  10.4, color=INK, weight="600"))
    o.append(_txt(340, 34,
                  esc("Vong lap cap: may tinh giam sat dat luong mong muon - van co cam bien P, T, rho - luong thuc phan hoi"),
                  7.2, color=GREY))
    o.append(_txt(664, 18, esc("Nguon: Flowserve Inc."),
                  7.0, anchor="end", color=GREY))

    # supervisory computer at the right; its master setpoint runs left along the top
    o.append(_box(548, 56, 108, 40, "SUPERVISORY\nCOMPUTER",
                  fill="#eef3fb", size=8.2))
    o.append(_arrow(546, 76, 122, 76, sw=1.5, color=BLUE))
    o.append(_txt(334, 69, esc("MASTER MASS-FLOW SETPOINT"),
                  7.6, color=BLUE, weight="600"))
    o.append(_arrow(120, 76, 120, 162, sw=1.4, color=BLUE))

    # summing junction for the desired mass flow
    o.append(_circle(120, 176, 14, fill="#ffffff", sw=1.4, color=INK))
    o.append(_txt(120, 180, esc("Σ"), 12, color=INK))
    o.append(_txt(102, 170, esc("+"), 8, color=INK))
    o.append(_txt(102, 188, esc("−"), 9, color=INK))
    o.append(_arrow(134, 176, 186, 176, sw=1.4, color=INK))

    # functional mass-flow relation
    o.append(_box(188, 150, 196, 52,
                  "MASS-FLOW RELATION\nm = f(Cv, ΔP, rho)",
                  fill=FILL, size=8.4))
    o.append(_arrow(384, 176, 430, 176, sw=1.4, color=INK))

    # valve with its pressure/temperature-sensing block
    o.append(_box(432, 142, 168, 68,
                  "CONTROL VALVE\n+ P, T, rho SENSING",
                  fill="#eef3fb", size=8.4))
    o.append(_poly([(496, 192), (496, 204), (508, 198)],
                   fill="#b8bfc6", sw=1.1, color=INK, close=True))
    o.append(_poly([(536, 192), (536, 204), (524, 198)],
                   fill="#b8bfc6", sw=1.1, color=INK, close=True))
    o.append(_arrow(600, 176, 654, 176, sw=1.6, color=INK))
    o.append(_txt(628, 167, esc("TO PROCESS"),
                  8.0, color=INK, weight="600"))

    # flow measurement and its feedback to the summing junction
    o.append(_arrow(620, 180, 620, 256, sw=1.3, color=BLUE))
    o.append(_box(568, 258, 104, 44, "FLOW\nMEASUREMENT",
                  fill="#eef3fb", size=8.0))
    o.append(_line(620, 302, 620, 332, sw=1.3, color=BLUE))
    o.append(_line(620, 332, 28, 332, sw=1.3, color=BLUE))
    o.append(_line(28, 332, 28, 176, sw=1.3, color=BLUE))
    o.append(_arrow(28, 176, 104, 176, sw=1.3, color=BLUE))
    o.append(_txt(324, 324, esc("ACTUAL MASS FLOW (feedback)"),
                  7.4, color=BLUE, weight="600"))

    # compact relation legend instead of the tiny source symbols
    o.append(_txt(340, 352,
                  esc("m = A u sqrt(2 rho (P1 - P2))     A: effective area   "
                      "u: valve travel   rho: density"),
                  7.0, color=INK))
    o.append(_txt(340, 368,
                  esc("ΔP = P1 - P2   Cv: valve coefficient   "
                      "local loop holds mass flow; supervisory loop sets it"),
                  7.0, color=GREY))

    s = svg(w, h, "".join(o),
            esc("Functional diagram of a smart valve with local mass-flow control"))
    return _fig(s,
                "Hình 10.2 · Sơ đồ chức năng đơn giản hóa của van điều khiển thông minh có khả năng điều khiển lưu lượng khối tại chỗ trong vòng lặp xếp tầng: máy tính giám sát ở bên phải gửi lưu lượng mong muốn tới điểm cộng, quan hệ m = f(Cv, ΔP, rho) (tương đương m = A u sqrt(2 rho (P1 - P2))) nối tới van kèm khối cảm biến áp suất và nhiệt độ P, T, rho; dòng chảy đi TIẾN TRÌNH và lưu lượng thực được đo rồi phản hồi về điểm cộng. Chú giải quan hệ được trình bày gọn ở dưới. Đây là bản vẽ lại dạng vector, đã đơn giản hóa. (Nguồn: Flowserve Inc.)",
                "Figure 10.2 · Simplified functional diagram of a smart control valve capable of local mass-flow control within a cascade loop: the supervisory computer at the right sends the desired mass flow to a summing junction, the relation m = f(Cv, ΔP, rho) (equivalently m = A u sqrt(2 rho (P1 - P2))) drives the valve with its pressure/temperature-sensing block P, T, rho; flow goes TO PROCESS and the measured process flow is fed back to the summing junction. A compact relation legend is kept at the bottom. This is a simplified vector redrawing. (Source: courtesy of Flowserve Inc.)",
                "Sơ đồ chức năng: máy tính giám sát đặt lưu lượng khối, điểm cộng, quan hệ lưu lượng qua van, van có cảm biến áp suất và nhiệt độ, dòng chảy tới quá trình và phản hồi lưu lượng thực",
                "Functional diagram with supervisory setpoint, summing junction, flow relation, valve with pressure and temperature sensing, flow to process and measured-flow feedback")


@_reg
def fig_f103():
    """Figure 10-3 - principle diagram of an intelligent digital valve positioner."""
    w, h = 680, 400
    o = [_defs()]
    o.append(_txt(340, 18,
                  esc("Nguyen ly hoat dong cua bo dinh vi van so thong minh"),
                  10.6, color=INK, weight="600"))
    o.append(_txt(340, 34,
                  esc("Duong dieu khien, phan hoi vi tri than va cam bien ap suat de chuan doan"),
                  7.4, color=GREY))

    # positioner enclosure, drawn behind the blocks
    o.append(_rect(216, 112, 424, 208, fill="#fcfbf8", sw=1.0,
                   dash="5 4", stroke="#bbbbbb"))
    o.append(_txt(630, 126, esc("POSITIONER"), 7.4, anchor="end", color=GREY))

    # terminals at the top
    o.append(_ellipse(420, 78, 72, 22, fill="#e9e9e9", sw=1.2))
    for cx in (384, 408, 432, 456):
        o.append(_circle(cx, 78, 6, fill="#ffffff", sw=1.0, color=INK))
    o.append(_arrow(636, 78, 494, 78, sw=1.4, color=BLUE))
    o.append(_txt(566, 69, esc("4–20 mA + HART"),
                  8.2, color=BLUE, weight="600"))
    o.append(_txt(250, 74, esc("AUXILIARY"), 7.4, anchor="end", color=INK))
    o.append(_txt(250, 84, esc("TERMINALS"), 7.4, anchor="end", color=INK))
    o.append(_line(252, 80, 346, 80, sw=1.0, color=GREY))

    # printed wiring board with onboard controller
    o.append(_arrow(420, 100, 420, 118, sw=1.4, color=INK))
    o.append(_box(316, 120, 208, 46,
                  "PRINTED WIRING BOARD\n(ONBOARD CONTROLLER)",
                  fill="#eef3fb", size=8.2))

    # separate pressure sensor for advanced diagnostics
    o.append(_box(96, 170, 150, 54,
                  "PRESSURE SENSOR\n(ADVANCED DIAGNOSTICS)",
                  fill=FILL, size=7.8))
    o.append(_arrow(246, 197, 314, 160, sw=1.4, color=GREEN, dash="5 3"))
    o.append(_arrow(188, 344, 188, 226, sw=1.3, color=GREEN, dash="5 3"))

    # I/P converter, supply pressure and relay/booster
    o.append(_arrow(420, 166, 420, 186, sw=1.4, color=INK))
    o.append(_box(356, 188, 128, 38, "I/P CONVERTER",
                  fill=FILL, size=8.2))
    o.append(_arrow(640, 207, 486, 207, sw=1.4, color=INK))
    o.append(_txt(566, 198, esc("SUPPLY PRESSURE"),
                  7.8, color=INK, weight="600"))
    o.append(_arrow(420, 226, 420, 244, sw=1.4, color=INK))
    o.append(_box(356, 246, 128, 38, "RELAY / BOOSTER",
                  fill=FILL, size=8.2))

    # output pressure to the diaphragm actuator
    o.append(_arrow(354, 265, 192, 265, sw=1.5, color=INK))
    o.append(_txt(272, 256, esc("OUTPUT PRESSURE"),
                  7.8, color=INK, weight="600"))
    o.append(_arrow(190, 267, 190, 298, sw=1.5, color=INK))

    # diaphragm, stem and valve
    o.append(_path("M150,300 A40,26 0 0 1 230,300 Z", fill="#d7d7d7", sw=1.2))
    o.append(_line(146, 300, 234, 300, sw=1.6, color=INK))
    o.append(_rect(186, 300, 8, 40, fill="#c9c9c9", sw=1.0))
    o.append(_poly([(150, 342), (150, 370), (186, 356)],
                   fill="#bfbfbf", sw=1.2, color=INK, close=True))
    o.append(_poly([(222, 342), (222, 370), (186, 356)],
                   fill="#bfbfbf", sw=1.2, color=INK, close=True))
    o.append(_line(112, 356, 150, 356, sw=2.0, color="#9aa5ae"))
    o.append(_line(222, 356, 260, 356, sw=2.0, color="#9aa5ae"))
    o.append(_arrow(232, 356, 256, 356, sw=1.2, color=BLUE))
    o.append(_txt(186, 386, esc("VALVE"), 7.8, color=INK, weight="600"))

    # stem-position feedback path back to the board
    o.append(_line(186, 322, 70, 322, sw=1.4, color=BLUE, dash="6 3"))
    o.append(_line(70, 322, 70, 130, sw=1.4, color=BLUE, dash="6 3"))
    o.append(_arrow(70, 130, 314, 130, sw=1.4, color=BLUE, dash="6 3"))
    o.append(_txt(140, 314, esc("STEM POSITION FEEDBACK"),
                  7.4, color=BLUE, weight="600"))

    # short legend note
    o.append(_rect(392, 330, 272, 54, fill="#f4f4f4", sw=0.9, stroke="#cccccc"))
    o.append(_txt(528, 350, esc("BOARD COMPARES COMMAND AND STEM FEEDBACK"),
                  7.0, color=INK))
    o.append(_txt(528, 366, esc("PRESSURE SENSOR SUPPORTS DIAGNOSTICS"),
                  7.0, color=INK))

    s = svg(w, h, "".join(o),
            esc("Principle of operation of an intelligent digital valve positioner"))
    return _fig(s,
                "Hình 10.3 · Sơ đồ nguyên lý đơn giản hóa của bộ định vị van số thông minh: các cọc 4–20 mA + HART và cọc phụ ở trên, bo mạch in có bộ điều khiển trên bo, bộ chuyển đổi I/P, áp suất cấp, rơle và bộ khuếch đại, áp suất ra tới cơ cấu màng, thân van và van, đường phản hồi vị trí thân về bo mạch, cùng cảm biến áp suất riêng cho chẩn đoán nâng cao. Bo mạch so sánh lệnh với phản hồi vị trí thân; cảm biến áp suất hỗ trợ chẩn đoán. Đây là bản vẽ lại dạng vector, đã đơn giản hóa.",
                "Figure 10.3 · Simplified principle diagram of an intelligent digital valve positioner: 4–20 mA + HART and auxiliary terminals at the top, the printed wiring board with onboard controller, I/P converter, supply pressure, relay and booster, output pressure to a diaphragm actuator, stem and valve, stem-position feedback back to the board, and a separate pressure sensor for advanced diagnostics. The board compares the command with stem feedback; the pressure sensor supports diagnostics. This is a simplified vector redrawing.",
                "Sơ đồ bộ định vị van số: đường tín hiệu từ cọc 4–20 mA + HART qua bo mạch, I/P và rơle tới cơ cấu màng và van; có phản hồi vị trí thân và phản hồi áp suất để chẩn đoán",
                "Digital valve positioner schematic with 4–20 mA + HART terminals, board, I/P converter, relay, diaphragm actuator and valve, plus stem-position feedback and a diagnostic pressure sensor")


@_reg
def fig_f104():
    """Figure 10-4 - simplified field-based architecture with intelligent devices."""
    w, h = 680, 430
    o = [_defs()]
    o.append(_txt(340, 16, esc("FIELD-BASED ARCHITECTURE"),
                  11.0, color=INK, weight="600"))
    o.append(_txt(340, 30,
                  esc("Kien truc truong thiet bi thong minh (don gian hoa)"),
                  7.4, color=GREY))
    o.append(_txt(664, 16, esc("Nguon: Emerson Process Control"),
                  7.0, anchor="end", color=GREY))

    def mini_pc(x, y):
        return (_rect(x, y, 40, 22, fill="#e8e8e8", sw=1.1)
                + _rect(x + 4, y + 3, 32, 13, fill="#b9c3cc", sw=0.8)
                + _line(x + 6, y + 19, x + 34, y + 19, sw=0.9, color=GREY))

    # top bus with engineering and management
    o.append(mini_pc(170, 46))
    o.append(mini_pc(450, 46))
    o.append(_txt(218, 60, esc("ENGINEERING"), 8.2,
                  anchor="start", color=INK, weight="600"))
    o.append(_txt(498, 60, esc("MANAGEMENT"), 8.2,
                  anchor="start", color=INK, weight="600"))
    o.append(_line(190, 68, 190, 80, sw=1.1, color=INK))
    o.append(_line(470, 68, 470, 80, sw=1.1, color=INK))
    o.append(_line(40, 80, 640, 80, sw=1.8, color=INK))
    o.append(_line(40, 84, 640, 84, sw=1.0, color=INK))

    # operations / modular software / maintenance layer
    o.append(_line(40, 110, 640, 110, sw=1.4, color=INK))
    o.append(_arrow(70, 110, 40, 110, sw=1.4, color=INK, head="a7"))
    o.append(_arrow(610, 110, 640, 110, sw=1.4, color=INK, head="a7"))
    o.append(mini_pc(60, 118))
    o.append(_line(80, 110, 80, 118, sw=1.1, color=INK))
    o.append(_txt(80, 154, esc("OPERATIONS"), 7.8, color=INK, weight="600"))
    o.append(_line(340, 110, 340, 116, sw=1.1, color=INK))
    o.append(_box(232, 116, 216, 34,
                  "INTEGRATED MODULAR\nSOFTWARE APPLICATIONS",
                  fill="#ececec", size=7.8))
    o.append(mini_pc(580, 118))
    o.append(_line(600, 110, 600, 118, sw=1.1, color=INK))
    o.append(_txt(600, 154, esc("MAINTENANCE"), 7.8, color=INK, weight="600"))

    # network / system technology band
    o.append(_line(340, 150, 340, 168, sw=1.1, color=INK))
    o.append(_rect(176, 168, 328, 26, fill="#ececec", sw=1.1, stroke=INK))
    o.append(_txt(340, 185, esc("NETWORK/SYSTEM TECHNOLOGY"),
                  8.4, color=INK, weight="600"))
    o.append(_line(340, 194, 340, 214, sw=1.1, color=INK))

    # field bus with representative intelligent devices
    o.append(_line(40, 214, 640, 214, sw=1.4, color=INK))
    o.append(_arrow(70, 214, 40, 214, sw=1.4, color=INK, head="a7"))
    o.append(_arrow(610, 214, 640, 214, sw=1.4, color=INK, head="a7"))

    def item(cx, kind, lines):
        g = [_line(cx, 214, cx, 222, sw=1.0, color=GREY)]
        cy = 234
        if kind == "gauge":
            g.append(_circle(cx, cy, 12, fill="#ffffff", sw=1.1))
            g.append(_line(cx, cy, cx + 7, cy - 6, sw=1.2, color=BLUE))
            g.append(_line(cx - 5, cy + 11, cx + 5, cy + 11, sw=1.0))
        elif kind == "valve":
            g.append(_poly([(cx - 12, cy - 9), (cx - 12, cy + 9), (cx, cy)],
                           fill="#b8bfc6", sw=1.1, color=INK, close=True))
            g.append(_poly([(cx + 12, cy - 9), (cx + 12, cy + 9), (cx, cy)],
                           fill="#b8bfc6", sw=1.1, color=INK, close=True))
            g.append(_line(cx - 18, cy, cx - 12, cy, sw=1.3))
            g.append(_line(cx + 12, cy, cx + 18, cy, sw=1.3))
        elif kind == "controller":
            g.append(_rect(cx - 13, cy - 10, 26, 20, fill="#eef3fb", sw=1.1))
            g.append(_line(cx - 8, cy - 4, cx + 8, cy - 4, sw=0.9, color=GREY))
            g.append(_line(cx - 8, cy + 2, cx + 8, cy + 2, sw=0.9, color=GREY))
        elif kind == "flow":
            g.append(_circle(cx, cy, 11, fill="#ffffff", sw=1.1))
            g.append(_line(cx - 8, cy, cx + 8, cy, sw=1.0, color=GREY))
            g.append(_line(cx, cy - 8, cx, cy + 8, sw=1.0, color=GREY))
        elif kind == "analyzer":
            g.append(_rect(cx - 12, cy - 11, 24, 22, fill="#eef3fb", sw=1.1))
            g.append(_rect(cx - 8, cy - 7, 16, 8, fill="#b9c3cc", sw=0.8))
            g.append(_line(cx - 8, cy + 5, cx + 8, cy + 5, sw=0.9, color=GREY))
        elif kind == "meter":
            g.append(_circle(cx, cy + 2, 10, fill="#ffffff", sw=1.1))
            g.append(_line(cx, cy + 2, cx + 6, cy - 3, sw=1.1, color=BLUE))
            g.append(_rect(cx - 6, cy - 13, 12, 5, fill="#b8bfc6", sw=0.9))
        elif kind == "smart":
            g.append(_rect(cx - 13, cy - 10, 26, 20, fill="#eef3fb", sw=1.1))
            g.append(_circle(cx - 5, cy, 4, fill="#ffffff", sw=0.9))
            g.append(_line(cx + 2, cy - 4, cx + 9, cy - 4, sw=0.9, color=GREY))
            g.append(_line(cx + 2, cy + 2, cx + 9, cy + 2, sw=0.9, color=GREY))
            g.append(_line(cx + 2, cy + 8, cx + 9, cy + 8, sw=0.9, color=GREY))
        elif kind == "motor":
            g.append(_circle(cx, cy, 11, fill="#e8e8e8", sw=1.1))
            for deg in (0, 60, 120):
                a = math.radians(deg)
                g.append(_line(cx - 9 * math.cos(a), cy - 9 * math.sin(a),
                               cx + 9 * math.cos(a), cy + 9 * math.sin(a),
                               sw=0.9, color=GREY))
        elif kind == "wireless":
            g.append(_rect(cx - 12, cy - 10, 24, 17, fill="#dfe5ea", sw=1.1))
            g.append(_line(cx - 16, cy + 9, cx + 16, cy + 9, sw=1.4))
            g.append(_path("M%d,%d Q%d,%d %d,%d"
                           % (cx + 8, cy - 12, cx + 14, cy - 18, cx + 18, cy - 12),
                           sw=1.0, color=BLUE))
        for i, ln in enumerate(lines):
            g.append(_txt(cx, 258 + i * 7.6, esc(ln), 6.0, color=INK))
        return "".join(g)

    items = [
        (74,  "gauge",      ["MEASUREMENT", "- PRESSURE", "- TEMP", "- FLOW", "- LEVEL"]),
        (141, "valve",      ["VALVES"]),
        (207, "controller", ["SMART I/O", "AND FIELD", "CONTROLLERS"]),
        (273, "flow",       ["MASS FLOW"]),
        (340, "analyzer",   ["ANALYTICAL", "INSTRUMENTS", "- PROCESS", "- ENVIRON"]),
        (407, "meter",      ["PD METERS"]),
        (473, "smart",      ["SMART DEVICES", "AND SYSTEM", "INTERFACES"]),
        (540, "motor",      ["OTHER DEVICES", "- PUMPS", "- CONDITION",
                             "  MONITORS", "- DRIVERS", "- MOTORS"]),
        (607, "wireless",   ["WIRELESS", "CONFIGURATION", "AND",
                             "MAINTENANCE", "TOOLS"]),
    ]
    for cx, kind, lines in items:
        o.append(item(cx, kind, lines))

    # closing band and source note
    o.append(_rect(176, 318, 328, 26, fill="#ececec", sw=1.1, stroke=INK))
    o.append(_txt(340, 335, esc("INTELLIGENT FIELD DEVICES"),
                  8.6, color=INK, weight="600"))
    o.append(_txt(340, 370,
                  esc("Ve lai don gian theo Baumann, Control Valve Primer, 5th ed. "
                      "(Fig. 10-4)"),
                  7.0, color=GREY))

    s = svg(w, h, "".join(o),
            esc("Field-based architecture with intelligent field devices"))
    return _fig(s,
                "Hình 10.4 · Kiến trúc dựa trên trường thiết bị được đơn giản hóa: ENGINEERING và MANAGEMENT ở trên cùng; lớp OPERATIONS, INTEGRATED MODULAR SOFTWARE APPLICATIONS và MAINTENANCE; băng NETWORK/SYSTEM TECHNOLOGY; rồi các nhóm thiết bị trường tiêu biểu gồm đo lường áp suất, nhiệt độ, lưu lượng và mức, van, I/O thông minh và bộ điều khiển trường, lưu lượng khối, thiết bị phân tích, đồng hồ PD, thiết bị thông minh và giao diện hệ thống, các thiết bị khác như bơm, thiết bị giám sát tình trạng, bộ truyền động và động cơ, cùng công cụ cấu hình và bảo trì không dây; kết thúc bằng băng INTELLIGENT FIELD DEVICES. Kiến trúc này chuyển điều khiển và trí tuệ từ phòng điều khiển tập trung DCS xuống chính các thiết bị trường. (Nguồn: Emerson Process Control.)",
                "Figure 10.4 · Simplified field-based architecture: ENGINEERING and MANAGEMENT at the top; an OPERATIONS, INTEGRATED MODULAR SOFTWARE APPLICATIONS and MAINTENANCE layer; a NETWORK/SYSTEM TECHNOLOGY band; representative intelligent field device groups covering pressure, temperature, flow and level measurement, valves, smart I/O and field controllers, mass flow, analytical instruments, PD meters, smart devices and system interfaces, other devices such as pumps, condition monitors, drivers and motors, and wireless configuration and maintenance tools; closing with an INTELLIGENT FIELD DEVICES band. This architecture moves control and intelligence out of a DCS-centric control room and into the field devices. (Source: courtesy Emerson Process Control.)",
                "Sơ đồ kiến trúc theo tầng: kỹ sư và quản lý, vận hành và bảo trì quanh phần mềm tích hợp, băng công nghệ mạng, các nhóm thiết bị trường và băng thiết bị trường thông minh",
                "Layered field-based architecture diagram with engineering and management, operations and maintenance, a network technology band, field device groups and an intelligent field devices band")
