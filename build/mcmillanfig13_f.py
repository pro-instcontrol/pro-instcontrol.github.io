# -*- coding: utf-8 -*-
"""Vector redraws of Figures 13.36-13.45 in A. McMillan, *Electrical
Installations in Hazardous Areas*, Chapter 13 "Protection concept intrinsic
safety 'i'".

All ten drawings are simplified vector redraws of the rendered pages p432,
p433, p435, p437, p439, p440, p443, p444 and p446.  Printed English labels,
parameter lists, fault-count tables, legends and Note lines are transcribed
onto the drawings; the printed English captions, including their quirks (the
truncated Fig. 13.39 caption and the duplicated Fig. 13.42/13.43 caption),
are returned verbatim after a bilingual prefix.  No raster artwork is used.
Each public callable returns the standard five-tuple through vfig._fig() and
is registered in FIGS by the _reg decorator.
"""
import sys
import os

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

from vfig import (BLUE, GREEN, GREY, INK, PAPER, RED, _arrow, _circle,
                  _defs, _ellipse, _fig, _line, _poly, _rect, _txt, svg)

FIGS = {}


def _reg(f):
    FIGS[f.__name__] = f()
    return f


def esc(s):
    """Every displayed string is literal Unicode with raw ampersands escaped."""
    return str(s).replace("&", "&amp;")


def T(x, y, s, size=8.0, **kw):
    """Plain text: clamp to the font contract, vet, then delegate to _txt()."""
    size = max(6.8, min(9.5, size))
    return _txt(x, y, esc(s), size, **kw)


# ------------------------------------------------------------------ helpers

def _title(o, n, vi, en, size=7.4):
    """Bilingual short heading on canvas; full captions live in the tuple."""
    o.append(T(340, 16, "Hình 13.%d · %s / Figure 13.%d · %s" % (n, vi, n, en),
               size, color=INK, weight="600"))


def _lines(o, x, y, items, step=12, size=7.6, color=INK, anchor="start"):
    for i, s in enumerate(items):
        o.append(T(x, y + i * step, s, size, color=color, anchor=anchor))


def _panel(o, x, y, w, h, lines, size=7.8, step=12, fill="#ffffff"):
    o.append(_rect(x, y, w, h, fill=fill, sw=1.1))
    _lines(o, x + 8, y + 14, lines, step=step, size=size)


def _ground(o, x, y):
    o.append(_line(x, y - 12, x, y, sw=1.0, color=INK))
    for i, w in enumerate((12, 8, 4)):
        o.append(_line(x - w / 2.0, y + i * 3.5, x + w / 2.0, y + i * 3.5,
                       sw=0.9, color=INK))


def _zigzag(o, x1, y1, x2, y2, amp=4.0, turns=5, color=INK):
    """A small resistor zigzag between two points."""
    pts = []
    if abs(y2 - y1) < 0.01:                      # horizontal resistor
        dx = (x2 - x1) / float(2 * turns)
        pts.append((x1, y1))
        for i in range(1, 2 * turns):
            pts.append((x1 + i * dx, y1 + (-amp if i % 2 else amp)))
        pts.append((x2, y2))
    else:                                        # vertical resistor
        dy = (y2 - y1) / float(2 * turns)
        pts.append((x1, y1))
        for i in range(1, 2 * turns):
            pts.append((x1 + (-amp if i % 2 else amp), y1 + i * dy))
        pts.append((x2, y2))
    o.append(_poly(pts, fill="none", sw=1.1, color=color))


def _zener(o, x, y0, y1, label, lx=None, ly=None):
    """Vertical zener: cathode bar with bent ends, printed label alongside."""
    ym = (y0 + y1) / 2.0
    o.append(_line(x, y0, x, ym - 4, sw=1.1, color=INK))
    o.append(_poly([(x - 6, ym - 4), (x + 6, ym - 4),
                    (x + 6, ym + 1), (x - 6, ym - 9)],
                   fill="none", sw=1.1, color=INK))
    o.append(_line(x, ym + 1, x, y1, sw=1.1, color=INK))
    if label:
        o.append(T(x + 8 if lx is None else lx,
                   ym + 3 if ly is None else ly, label, 7.2, anchor="start"))


def _cap(o, x, y0, y1, label, lx=None, ly=None):
    """Vertical shunt capacitor with two horizontal plates."""
    ym = (y0 + y1) / 2.0
    o.append(_line(x, y0, x, ym - 4, sw=1.1, color=INK))
    o.append(_line(x - 8, ym - 4, x + 8, ym - 4, sw=1.3, color=INK))
    o.append(_line(x - 8, ym + 2, x + 8, ym + 2, sw=1.3, color=INK))
    o.append(_line(x, ym + 2, x, y1, sw=1.1, color=INK))
    if label:
        o.append(T(x + 11 if lx is None else lx,
                   ym - 6 if ly is None else ly, label, 7.2, anchor="start"))


def _dim(o, x1, x2, y, label, below=False):
    """Dimension line with end ticks and a centred printed label."""
    o.append(_line(x1, y, x2, y, sw=0.9, color=GREY))
    for xx in (x1, x2):
        o.append(_line(xx, y - 5, xx, y + 5, sw=0.9, color=GREY))
    ty = y + 10 if below else y - 4
    o.append(T((x1 + x2) / 2.0, ty, label, 7.2, color=GREY))


def _fault_x(o, x, y, letter, above=10):
    o.append(_line(x - 4, y - 4, x + 4, y + 4, sw=1.4, color=RED))
    o.append(_line(x - 4, y + 4, x + 4, y - 4, sw=1.4, color=RED))
    o.append(T(x, y - above, letter, 7.4, color=RED, weight="600"))


def _note(o, y, vi, en, size=6.8):
    o.append(T(340, y, vi, size, color=INK))
    o.append(T(340, y + 11, en, size, color=INK))


# ------------------------------------------------------------------ 13.36

@_reg
def fig_f1336():
    """Figure 13.36 - two typical apparatus labels, associated and IS."""
    w, h = 680, 344
    o = [_defs(), _rect(0, 0, w, h, fill=PAPER, sw=0)]
    _title(o, 36, "Nhãn thiết bị điển hình", "Typical apparatus labels")

    _panel(o, 170, 42, 340, 132, [], size=8.4)
    _lines(o, 178, 57, ["Acme Products plc", "Controller type ×R2",
                        "Serial No × 2643", "EEx [ia] IIc"], step=13, size=8.4)
    _lines(o, 178, 117, ["U_m = 250 V rms", "U_o = 30 V dc",
                         "I_o = 0.1 A", "P_o = 0.75 W"], step=13, size=8.4)
    _lines(o, 366, 117, ["L_o = 22 mH", "C_o = 0.1 μF",
                         "L_o/R_o = 25 μH/ohm"], step=13, size=8.4)
    o.append(T(340, 188, "Nhãn thiết bị liên kết điển hình · "
                         "Typical associated apparatus label", 7.6))

    _panel(o, 170, 202, 340, 116, [], size=8.4)
    _lines(o, 178, 217, ["Exelsior Transmitters Ltd.",
                         "Temperature transmitter type TR6",
                         "Serial No. 2", "EEx ia IIC T6"], step=13, size=8.4)
    _lines(o, 178, 277, ["U_i = 30 V", "I_i = 0.1 A", "P_i = 0.75 W"],
           step=13, size=8.4)
    _lines(o, 366, 277, ["L_i = 22 mH", "C_i = 0.1 μF"], step=13, size=8.4)
    o.append(T(340, 334, "Nhãn thiết bị an toàn nội tại điển hình · "
                         "Typical intrinsically safe apparatus label", 7.6))

    return _fig(svg(w, h, "".join(o), esc("Fig 13.36")),
                "Hình 13.36 · Nhãn thiết bị điển hình",
                "Figure 13.36 · Typical apparatus labels",
                "Hai nhãn thiết bị trong hộp chữ nhật, xếp chồng lên nhau. Nhãn trên "
                "của Acme Products plc ghi loại bộ điều khiển ×R2, số serial × 2643, "
                "ký hiệu EEx [ia] IIc với chữ c viết thường, cùng các thông số U_m "
                "250 V rms, U_o 30 V dc, I_o 0,1 A, P_o 0,75 W, L_o 22 mH, C_o "
                "0,1 μF và L_o/R_o 25 μH/ohm. Nhãn dưới của Exelsior Transmitters "
                "Ltd. ghi bộ transmitter nhiệt độ TR6, số serial 2, ký hiệu EEx ia "
                "IIC T6 viết hoa và các thông số U_i, I_i, P_i, L_i, C_i. Mỗi hộp "
                "có dòng mô tả bên dưới bằng tiếng Việt và tiếng Anh",
                "Two rectangular apparatus labels stacked one above the other. The "
                "upper Acme Products plc box gives controller type ×R2, serial No "
                "× 2643, the marking EEx [ia] IIc with a lower-case c, and the "
                "parameters U_m 250 V rms, U_o 30 V dc, I_o 0.1 A, P_o 0.75 W, L_o "
                "22 mH, C_o 0.1 microfarad and L_o/R_o 25 microhenry per ohm. The "
                "lower Exelsior Transmitters Ltd. box gives a TR6 temperature "
                "transmitter, serial No. 2, EEx ia IIC T6 with capital IIC, and the "
                "input parameters U_i, I_i, P_i, L_i and C_i. A descriptive line "
                "sits below each box in Vietnamese and English")


# ------------------------------------------------------------------ 13.37

@_reg
def fig_f1337():
    """Figure 13.37 - associated apparatus source circuit and equivalents."""
    w, h = 680, 412
    o = [_defs(), _rect(0, 0, w, h, fill=PAPER, sw=0)]
    _title(o, 37, "Số lần hỏng trong thiết bị liên kết",
           "Fault counts in associated apparatus")
    o.append(T(340, 29, "Mạch nguồn không thể hỏng · "
                        "Infallible source and equivalent power source", 6.8,
               color=GREY))

    # Mains, transformer and bridge rectifier.
    for yy in (72, 188):
        o.append(_circle(52, yy, 3, fill="#ffffff", sw=1.0))
    o.append(_line(52, 72, 52, 188, sw=1.0, color=INK))
    o.append(_line(52, 72, 92, 72, sw=1.0, color=INK))
    o.append(_line(52, 188, 92, 188, sw=1.0, color=INK))
    _zigzag(o, 92, 92, 92, 168, amp=4, turns=4)
    o.append(_line(92, 72, 92, 92, sw=1.0, color=INK))
    o.append(_line(92, 168, 92, 188, sw=1.0, color=INK))
    o.append(T(26, 130, "Mains", 7.2, anchor="start"))
    o.append(T(92, 206, "Transformer", 7.2))
    _zigzag(o, 110, 100, 110, 160, amp=4, turns=4)
    o.append(_line(110, 100, 180, 100, sw=1.0, color=INK))
    o.append(_line(110, 160, 180, 160, sw=1.0, color=INK))
    o.append(_poly([(146, 130), (180, 100), (214, 130), (180, 160)],
                   fill="none", sw=1.2, close=True))
    for px, py in ((163, 115), (197, 115), (163, 145), (197, 145)):
        o.append(_poly([(px - 5, py - 3), (px + 5, py), (px - 5, py + 3)],
                       fill=INK, sw=0, close=True))
    o.append(T(180, 133, "Rectifier", 7.0))
    o.append(T(130, 178, "Vo/c = 39 V", 7.2, anchor="start"))
    o.append(T(130, 188, "(peak)", 7.2, anchor="start"))

    # DC rail with three infallible resistors and two zeners.
    o.append(_line(180, 100, 520, 100, sw=1.2, color=INK))
    o.append(_line(180, 160, 180, 190, sw=1.2, color=INK))
    o.append(_line(180, 190, 520, 190, sw=1.2, color=INK))
    for x1, x2, lab in ((280, 320, "R1 (700 Ω)"), (350, 390, "R2 (30 Ω)"),
                        (430, 470, "R3 (300 Ω)")):
        _zigzag(o, x1, 100, x2, 100, amp=4, turns=4)
        o.append(T((x1 + x2) / 2.0, 88, lab, 7.2))
    o.append(T(370, 114, "Infallible resistors", 7.0))
    _zener(o, 340, 100, 190, "Z1 (30 V)", lx=348, ly=146)
    _zener(o, 410, 100, 190, "Z2 (28 V)", lx=418, ly=146)
    _cap(o, 246, 100, 190, "C", lx=256, ly=136)
    _ground(o, 340, 190)
    o.append(_circle(520, 100, 3, fill="#ffffff", sw=1.0))
    o.append(T(520, 88, "Output", 7.2))

    o.append(T(340, 234, "Nguồn tương đương · Equivalent power source",
               8.0, weight="600"))
    _lines(o, 60, 254, [
        "[ib]   V_o   = 30 V (V_z1)",
        "       I_o   = 39/1030 A (V_o/c/R1 + R2 + R3)",
        "       P_o   = 0.37 W",
        "       L_o   = 0.22 mH (from Fig. 13.5 - no internal inductance)",
        "       L_o/R_o = 96 μH/ohm (from formula - no internal inductance)",
        "       C_o   = 0.067 μF (from Fig. 13.8 no internal capacitance)",
    ], step=12, size=7.4)
    _lines(o, 60, 334, [
        "[ia]   V_o   = 39 V (V_o/c)",
        "       I_o   = 39/1030 A (V_o/c/R1 + R2 + R3)",
        "       P_o   = 0.37 W",
        "       L_o   = 0.22 mH (see above)",
        "       L_o/R_o = 96 μH/ohm (see above)",
        "       C_o   = 0.033 μF (see above)",
    ], step=12, size=7.4)

    return _fig(svg(w, h, "".join(o), esc("Fig 13.37")),
                "Hình 13.37 · Số lần hỏng trong thiết bị liên kết",
                "Figure 13.37 · Fault counts in associated apparatus",
                "Sơ đồ nguồn gồm đầu vào mains qua biến áp cách ly, cầu chỉnh lưu "
                "bốn diode và tụ C, sau đó là ba điện trở không thể hỏng R1 700 Ω, "
                "R2 30 Ω, R3 300 Ω trên đường dẫn trên, hai diode zener Z1 30 V và "
                "Z2 28 V mắc xuống đường dẫn dưới có tiếp địa và đầu ra ở bên phải. "
                "Ghi chú Vo/c bằng 39 V đỉnh. Phía dưới là hai nhóm thông số [ib] và "
                "[ia] với V_o, I_o, P_o, L_o, L_o/R_o và C_o; nhóm [ia] có C_o "
                "0,033 μF còn nhóm [ib] có 0,067 μF. Ký hiệu ngoặc vuông in là "
                "[ib] chữ thường",
                "Circuit source with mains input through a transformer, a four-diode "
                "bridge rectifier and capacitor C, followed by three infallible "
                "resistors R1 700 ohm, R2 30 ohm and R3 300 ohm along the upper rail, "
                "zener diodes Z1 30 V and Z2 28 V shunting to the earthed lower rail, "
                "and an output terminal at the right. Vo/c is marked 39 V peak. "
                "Below, two printed parameter groups [ib] and [ia] list V_o, I_o, "
                "P_o, L_o, L_o/R_o and C_o, with C_o 0.067 microfarad for [ib] and "
                "0.033 microfarad for [ia]. The printed bracketed designator uses "
                "lower-case ib")


# ------------------------------------------------------------------ 13.38

@_reg
def fig_f1338():
    """Figure 13.38 - intrinsically safe sensor circuit and equivalents."""
    w, h = 680, 398
    o = [_defs(), _rect(0, 0, w, h, fill=PAPER, sw=0)]
    _title(o, 38, "Số lần hỏng trong thiết bị an toàn nội tại",
           "Fault counts in intrinsically safe apparatus")

    o.append(_line(180, 58, 560, 58, sw=1.2, color=INK))
    o.append(_line(180, 188, 560, 188, sw=1.2, color=INK))
    for yy in (105, 135):
        o.append(_circle(150, yy, 2.5, fill="#ffffff", sw=1.0))
    o.append(T(96, 122, "To sensor", 7.2, anchor="start"))
    for xx, lab in ((215, "R5"), (250, "R4"), (285, "R3"), (320, "R2")):
        _zigzag(o, xx, 58, xx, 105, amp=3.5, turns=4)
        o.append(T(xx, 50, lab, 7.2))
    for xx, lab in ((215, "R7"), (250, "R6"), (285, "R1")):
        _zigzag(o, xx, 143, xx, 188, amp=3.5, turns=4)
        o.append(T(xx, 200, lab, 7.2))
    _zigzag(o, 180, 143, 180, 188, amp=3.5, turns=4)
    o.append(T(180, 200, "R8", 7.2))
    o.append(_poly([(340, 100), (340, 150), (390, 125)],
                   fill="#eef3fb", sw=1.1, close=True))
    for xx in (220, 255, 290, 325):
        o.append(_line(xx, 105, xx, 143, sw=0.9, color=INK))
    _cap(o, 445, 58, 188, "C (0.033 μF)", lx=455, ly=100)
    _zener(o, 500, 58, 188, "Z1 (19 v)", lx=510, ly=134)
    o.append(_poly([(556, 52), (568, 58), (556, 64)],
                   fill=INK, sw=0, close=True))
    o.append(T(562, 48, "D1", 7.2))
    o.append(T(600, 125, "V_in", 7.6, anchor="start"))

    o.append(T(340, 222, "Thông số thiết bị an toàn nội tại tương đương · "
                         "Equivalent intrinsically safe apparatus parameters",
               7.6, weight="600"))
    _lines(o, 130, 240, [
        "ib    V_i = 30 V (To accommodate ib power source - Fig. 13.37)",
        "      I_i = 38 mA (To accommodate ib power source - Fig. 13.37)",
        "      P_i = 0.37 W (To accommodate ib power source)",
        "      L_i = 0 (No inductance present)",
        "      C_i = 0 (Effective - see text)",
    ], step=11, size=7.4)
    o.append(_poly([(124, 293), (118, 293), (118, 311), (124, 311)],
                   fill="none", sw=1.0, color=INK))
    _lines(o, 130, 293, ["To Sensor { V_o = 30 V",
                         "          { I_o = See text"], step=11, size=7.4)
    _lines(o, 130, 317, [
        "ia    V_i = 39 V (See above)",
        "      I_i = 38 mA (See above)",
        "      P_i = 0.37 W (See above)",
        "      L_i = 0",
        "      C_i = 0.033 μF (Z1 o/c and D1 s/c)",
    ], step=11, size=7.4)
    o.append(_poly([(124, 370), (118, 370), (118, 388), (124, 388)],
                   fill="none", sw=1.0, color=INK))
    _lines(o, 130, 370, ["To Sensor { V_o = 30 V",
                         "          { I_o = See text"], step=11, size=7.4)

    return _fig(svg(w, h, "".join(o), esc("Fig 13.38")),
                "Hình 13.38 · Số lần hỏng trong thiết bị an toàn nội tại",
                "Figure 13.38 · Fault counts in intrinsically safe apparatus",
                "Mạch cảm biến có các điện trở R5, R4, R3, R2 ở phía trên và R8, R7, "
                "R6, R1 ở phía dưới quanh phần tử khuếch đại ở giữa, hai đầu nối To "
                "sensor bên trái, diode D1 trên đường trên cùng, nguồn V_in bên phải, "
                "tụ C 0,033 μF và diode zener Z1 ghi 19 v chữ thường mắc song song "
                "xuống đường dưới. Bên dưới mạch là bảng thông số ib và ia gồm V_i, "
                "I_i, P_i, L_i, C_i cùng hai cặp dòng To Sensor có ngoặc nhọn; "
                "giá trị C_i của ia là 0,033 μF khi Z1 hở mạch và D1 ngắn mạch",
                "Sensor circuit with resistors R5, R4, R3 and R2 above and R8, R7, "
                "R6 and R1 below a central amplifier element, two To sensor terminals "
                "at the left, diode D1 on the upper rail, V_in at the right, and a "
                "0.033 microfarad capacitor C plus a zener Z1 marked 19 v with a "
                "lower-case v shunting to the lower rail. Underneath, the ib and ia "
                "parameter lists give V_i, I_i, P_i, L_i and C_i, followed by two "
                "braced To Sensor pairs. The ia capacitance is 0.033 microfarad for "
                "Z1 open circuit and D1 short circuit")


# ------------------------------------------------------------------ 13.39

@_reg
def fig_f1339():
    """Figure 13.39 - system input/output assessment and necessary truths."""
    w, h = 680, 456
    o = [_defs(), _rect(0, 0, w, h, fill=PAPER, sw=0)]
    _title(o, 39, "Đánh giá hệ thống theo thông số vào ra",
           "System assessment from input and output definitions", 7.2)

    _panel(o, 30, 48, 186, 104, [
        "'ia'", "Associate apparatus", "(power source)",
        "V_o = V_1  I_o = I_1", "P_o = P_1",
        "L_o = L_1  C_o = C_1", "L_o/R_o = L_1/R_1",
    ], size=7.8, step=12)
    o.append(T(123, 166, "(No earth connection)", 7.2))

    _panel(o, 30, 196, 186, 104, [
        "'ia'", "Associate apparatus", "computer",
        "V_o = V_2  I_o = I_2", "P_o = P_2",
        "L_o = L_2  C_o = C_2", "L_o/R_o  L_2/R_2",
    ], size=7.8, step=12)
    o.append(T(123, 314, "No earth connection", 7.2))
    o.append(T(123, 328, "necessary truths", 7.2, color=GREY))

    _panel(o, 430, 100, 216, 136, [
        "'ia'", "Intrinsically safe", "apparatus",
        "V_i = V_3  I_i = I_3", "P_i = P_3",
        "L_i = L_3  C_i = C_3", "L_i/R_i = L_3/R_3",
        "V_i = V_4  I_i = I_4", "P_i = P_4",
        "L_i = L_4  C_i = C_4", "L_i/R_i = L_4/R_4",
    ], size=7.4, step=11)

    # Two cable runs, each with a dashed junction section.
    o.append(_poly([(216, 100), (300, 100), (300, 150), (430, 150)],
                   fill="none", sw=1.1, color=INK))
    o.append(_poly([(216, 248), (300, 248), (300, 200), (430, 200)],
                   fill="none", sw=1.1, color=INK))
    for yy in (150, 200):
        o.append(_rect(302, yy - 9, 100, 18, fill="#ffffff",
                       sw=0.9, dash="3 2"))
        o.append(T(352, yy - 11, "(L_c) (C_c)", 7.2))

    _lines(o, 30, 346, ["V_3 ≥ V_1 + V_2", "I_3 ≥ I_1 + I_2",
                        "P_3 ≥ P_1 + P_2"], step=12, size=7.4)
    _lines(o, 350, 346, ["V_4 ≥ V_1 + V_2", "I_4 ≥ I_1 + I_2",
                         "P_4 ≥ P_1 + P_2"], step=12, size=7.4)
    _lines(o, 30, 388, [
        "L_3 + L_4 + L_c ≤ permissible inductance for I_1 + I_2",
        "C_3 + C_4 + C_c ≤ permissible capacitance for V_1 + V_2",
        "L_o/R_o and L_3/R_3 and L_4/R_4 ≤ L_1/R_1",
    ], step=12, size=7.4)
    o.append(T(270, 424, "≤ L_2/R_2", 7.4))
    o.append(T(30, 440, "UR ≤ UR permissible for composite power source.",
               7.4, anchor="start"))

    return _fig(svg(w, h, "".join(o), esc("Fig 13.39")),
                "Hình 13.39 · Đánh giá hệ thống dựa trên định nghĩa đầu vào và đầu ra "
                "của thiết bị (dựa trên đánh giá từng thiết bị riêng lẻ). Lưu ý: Nếu "
                "đáp ứng yêu cầu L/R thì không cần đáp ứng yêu cầu về điện cảm",
                "Figure 13.39 · Assessment of systems on the basis of input and output "
                "definitions for apparatus (based on assessment of each item of "
                "apparatus alone). Note: If L/R requirements are met the inductance "
                "requirements need not be",
                "Ba hộp thiết bị nối bằng hai đường cáp có đoạn gạch đứt mang nhãn "
                "(L_c) (C_c). Hộp trên bên trái là thiết bị liên kết nguồn với các "
                "thông số V_o, I_o, P_o, L_o, C_o và L_o/R_o, hộp dưới bên trái là "
                "máy tính liên kết tương tự nhưng dòng L_o/R_o không có toán tử; "
                "hộp bên phải là thiết bị an toàn nội tại với hai bộ thông số V_i, "
                "I_i, P_i, L_i, C_i và L_i/R_i. Các chú thích No earth connection "
                "và necessary truths nằm dưới các hộp. Phía dưới là các bất đẳng thức "
                "so sánh V_3, I_3, P_3 với V_4, I_4, P_4, giới hạn L_3 + L_4 + L_c "
                "và C_3 + C_4 + C_c, xét L_o/R_o, L_3/R_3, L_4/R_4 so với L_1/R_1 "
                "và L_2/R_2, cuối cùng là UR. Caption in bị cụt giữa chừng ở cụm "
                "'need not be'",
                "Three apparatus boxes joined by two cable runs with dashed sections "
                "labelled (L_c) (C_c). The upper-left box is associate apparatus as a "
                "power source with V_o, I_o, P_o, L_o, C_o and L_o/R_o; the lower-left "
                "box is associate apparatus as a computer with analogous values but "
                "no operator in the L_o/R_o line; the right box is intrinsically safe "
                "apparatus with two sets of input parameters. No earth connection and "
                "necessary truths appear below the boxes. The lower block compares "
                "V_3, I_3, P_3 with V_4, I_4, P_4, bounds L_3 plus L_4 plus L_c and "
                "C_3 plus C_4 plus C_c, compares L_o/R_o, L_3/R_3 and L_4/R_4 with "
                "L_1/R_1 and L_2/R_2, and ends with UR. The printed caption is cut "
                "off mid-sentence at 'need not be'")


# ------------------------------------------------------------------ 13.40

@_reg
def fig_f1340():
    """Figure 13.40 - three apparatus boxes and the printed fault-count table."""
    w, h = 680, 442
    o = [_defs(), _rect(0, 0, w, h, fill=PAPER, sw=0)]
    _title(o, 40, "Đếm số lần hỏng của hệ thống", "System fault counting", 7.6)
    o.append(T(340, 29, "Bảng số lần hỏng trong hình · In-figure fault-count table",
               6.8, color=GREY))

    _panel(o, 30, 44, 186, 104, [
        "'ia'", "Associated", "apparatus", "(power source)",
        "V_o = V_1   I_o = I_1", "P_o = P_1",
        "L_o = L_1   C_o = C_1", "L_o/R_o = L_1/R_1",
    ], size=7.6, step=12)
    o.append(T(123, 160, "Apparatus 1", 7.6))
    _panel(o, 30, 186, 186, 104, [
        "'ia'", "Associated", "apparatus", "(computer)",
        "V_o = V_2   I_o = I_2", "P_o = P_2",
        "L_o = L_2   C_o = C_2", "L_o / L_2   L_2/R_2",
    ], size=7.6, step=12)
    o.append(T(123, 302, "Apparatus 2", 7.6))
    _panel(o, 430, 96, 216, 140, [
        "'ia'", "Intrinsically safe", "apparatus",
        "V_i = V_3   I_i = I_3", "P_i = P_3",
        "L_i = L_3   C_i = C_3", "L_i/R_i = L_3/R_3",
        "V_i = V_4   I_i = I_4", "P_i = P_4",
        "L_i = L_4   C_i = C_4", "L_i/R_i = L_4/R_4",
    ], size=7.4, step=11)
    o.append(T(538, 248, "Apparatus 3", 7.6))

    o.append(_poly([(216, 100), (300, 100), (300, 140), (430, 140)],
                   fill="none", sw=1.1, color=INK))
    o.append(_poly([(216, 248), (300, 248), (300, 200), (430, 200)],
                   fill="none", sw=1.1, color=INK))
    for yy in (140, 200):
        o.append(_rect(302, yy - 9, 100, 18, fill="#ffffff",
                       sw=0.9, dash="3 2"))
    o.append(T(352, 218, "Type'C' cable", 7.4))

    # Fault-count table rebuilt as vector diagram elements.
    o.append(T(340, 320, "Fault count", 8.0, weight="600"))
    o.append(_line(60, 328, 620, 328, sw=1.0, color=INK))
    for xx in (240, 375, 525):
        o.append(_line(xx, 328, xx, 430, sw=0.8, color=GREY))
    for xx, lab in ((300, "Apparatus 1"), (450, "Apparatus 2"),
                    (600, "Apparatus 3")):
        o.append(T(xx, 343, lab, 7.8, weight="600"))
    o.append(_line(60, 349, 620, 349, sw=0.9, color=INK))
    rows = [("Case 1", 2, 0, 0), ("Case 2", 1, 1, 0),
            ("Case 3", 1, 0, 1), ("Case 4", 0, 1, 1),
            ("Case 5", 0, 2, 0), ("Case 6", 0, 0, 2)]
    for i, (lab, a, b, c) in enumerate(rows):
        yy = 363 + i * 12
        o.append(T(70, yy, lab, 7.6, anchor="start"))
        o.append(T(300, yy, str(a), 7.6))
        o.append(T(450, yy, str(b), 7.6))
        o.append(T(600, yy, str(c), 7.6))
        o.append(_line(60, yy + 5, 620, yy + 5, sw=0.6, color=GREY))
    o.append(_line(60, 430, 620, 430, sw=1.0, color=INK))

    return _fig(svg(w, h, "".join(o), esc("Fig 13.40")),
                "Hình 13.40 · Đếm số lần hỏng của hệ thống. Lưu ý: Điều trên có nghĩa "
                "là chỉ trong các trường hợp 1, 5 và 6 thì bất kỳ thông số nào quy "
                "định cho thiết bị mới nhất thiết đúng, thay vì chỉ mang tính hạn "
                "chế, và chỉ một bộ thông số cho một thiết bị là phù hợp với mỗi "
                "trường hợp",
                "Figure 13.40 · System fault counting. Note: The above means that "
                "only in cases 1, 5 and 6 are any of the parameters specified for the "
                "apparatus necessarily true, rather than restrictive, and only the "
                "set for one piece of apparatus is appropriate to each case",
                "Ba hộp thiết bị nối bằng hai đường cáp có đoạn gạch đứt mang nhãn "
                "Type'C' cable và có nhãn Apparatus 1, 2, 3 bên dưới. Hộp 1 và 2 là "
                "thiết bị liên kết nguồn và máy tính, hộp 3 là thiết bị an toàn nội "
                "tại có hai bộ thông số đầu vào. Phía dưới là bảng Fault count gồm "
                "bốn cột với sáu trường hợp: Case 1 là 2, 0, 0; Case 2 là 1, 1, 0; "
                "Case 3 là 1, 0, 1; Case 4 là 0, 1, 1; Case 5 là 0, 2, 0; Case 6 "
                "là 0, 0, 2. Caption in kèm Note nói chỉ các trường hợp 1, 5 và 6 "
                "mới bắt buộc đúng các thông số",
                "Three apparatus boxes joined by two cable runs with dashed sections "
                "labelled Type'C' cable and captioned Apparatus 1, 2 and 3. Boxes 1 "
                "and 2 are associate apparatus as power source and computer; box 3 is "
                "intrinsically safe apparatus with two sets of input parameters. Below "
                "is a ruled fault-count table with four columns and six cases: Case 1 "
                "2, 0, 0; Case 2 1, 1, 0; Case 3 1, 0, 1; Case 4 0, 1, 1; Case 5 "
                "0, 2, 0; Case 6 0, 0, 2. The printed caption includes a Note stating "
                "that only cases 1, 5 and 6 make the apparatus parameters necessarily "
                "true rather than restrictive")


# ------------------------------------------------------------------ 13.41

@_reg
def fig_f1341():
    """Figure 13.41 - three individual cables joined via a multicore cable."""
    w, h = 680, 318
    o = [_defs(), _rect(0, 0, w, h, fill=PAPER, sw=0)]
    _title(o, 41, "Cách dùng điển hình của cáp nhiều lõi",
           "Typical use of multicore cables")

    o.append(T(200, 50, "Associated apparatus", 7.6))
    o.append(T(480, 50, "Intrinsically safe apparatus", 7.6))
    for yy, num in ((64, "1"), (164, "2"), (264, "3")):
        o.append(_rect(170, yy, 60, 36, fill="#eef3fb", sw=1.1))
        o.append(T(200, yy + 22, num, 8.4, weight="600"))
        o.append(_rect(450, yy, 60, 36, fill="#eef3fb", sw=1.1))
        o.append(T(480, yy + 22, num, 8.4, weight="600"))

    o.append(_rect(300, 150, 22, 52, fill="#ffffff", sw=1.1))
    o.append(_rect(370, 150, 22, 52, fill="#ffffff", sw=1.1))
    o.append(T(311, 142, "Junction Box", 6.8))
    o.append(T(381, 142, "Junction Box", 6.8))
    for yy in (160, 168, 176, 184):
        o.append(_line(322, yy, 370, yy, sw=0.9, color=INK))
        o.append(_circle(322, yy, 1.8, fill=INK, sw=0))
        o.append(_circle(370, yy, 1.8, fill=INK, sw=0))
    o.append(T(346, 122, "Multicircuit", 7.0))
    o.append(T(346, 132, "multicore cable", 7.0))

    left = [((230, 82), (300, 160)), ((230, 182), (300, 170)),
            ((230, 282), (300, 184))]
    right = [((392, 160), (450, 82)), ((392, 170), (450, 182)),
             ((392, 184), (450, 282))]
    for (x1, y1), (x2, y2) in left + right:
        o.append(_line(x1, y1, x2, y2, sw=1.0, color=INK))
        o.append(_circle(x1, y1, 2.2, fill="#ffffff", sw=0.9))
        o.append(_circle(x2, y2, 2.2, fill="#ffffff", sw=0.9))
    o.append(T(258, 118, "Individual cables", 7.0))
    o.append(T(422, 118, "Individual cables", 7.0))

    return _fig(svg(w, h, "".join(o), esc("Fig 13.41")),
                "Hình 13.41 · Cách dùng điển hình của cáp nhiều lõi",
                "Figure 13.41 · Typical use of multicore cables",
                "Ba hộp thiết bị liên kết bên trái đánh số 1, 2, 3 nối bằng các dây "
                "riêng lẻ tới một hộp nối dây, tương tự ba hộp thiết bị an toàn nội "
                "tại bên phải. Giữa hai hộp nối dây là bốn sợi dây song song của cáp "
                "đa mạch nhiều lõi; các nhãn Individual cables, Junction Box và "
                "Multicircuit multicore cable được đặt cạnh các nhóm dây",
                "Three associate apparatus boxes numbered 1, 2 and 3 on the left link "
                "by individual cables to a junction box, mirrored by three "
                "intrinsically safe apparatus boxes on the right. Four parallel lines "
                "between the two junction boxes form the multicircuit multicore cable. "
                "The labels Individual cables, Junction Box and Multicircuit multicore "
                "cable sit beside the respective cable groups")


# ------------------------------------------------------------------ 13.42

@_reg
def fig_f1342():
    """Figure 13.42 - four faults A-D in three parallel power-source circuits."""
    w, h = 680, 520
    o = [_defs(), _rect(0, 0, w, h, fill=PAPER, sw=0)]
    _title(o, 42, "Ảnh hưởng của sự cố trong cáp nhiều lõi",
           "Effects of faults in multicore cables", 7.2)

    o.append(T(190, 52, "Associated apparatus", 7.4))
    o.append(T(490, 52, "Intrinsically safe apparatus", 7.4))
    o.append(T(340, 48, "Multicore cable", 7.4))
    o.append(T(340, 59, "type 'C'", 7.4))

    for i, yy in enumerate((70, 215, 360), start=1):
        o.append(_rect(150, yy, 80, 60, fill="#eef3fb", sw=1.1))
        _lines(o, 190, yy + 22, ["Power", "source", str(i)],
               step=11, size=7.4)
        o.append(_rect(440, yy, 80, 60, fill="#eef3fb", sw=1.1))
        o.append(T(480, yy + 35, str(i), 8.4, weight="600"))
        _ground(o, 190, yy + 84)
        for ly in (yy + 20, yy + 40):
            o.append(_line(230, ly, 440, ly, sw=1.0, color=INK))
        o.append(_circle(365, yy + 20, 2.6, fill=INK, sw=0))
        o.append(_circle(365, yy + 40, 2.6, fill=INK, sw=0))

    o.append(_line(365, 90, 365, 160, sw=1.1, color=RED))
    o.append(_line(365, 174, 365, 255, sw=1.1, color=RED))
    o.append(T(372, 168, "A", 7.4, color=RED, weight="600"))
    o.append(_line(400, 255, 400, 310, sw=1.1, color=RED))
    o.append(_line(400, 324, 400, 380, sw=1.1, color=RED))
    o.append(T(407, 318, "B", 7.4, color=RED, weight="600"))
    _fault_x(o, 385, 235, "C")
    _fault_x(o, 420, 380, "D")

    _lines(o, 60, 452, [
        "A = Short circuit fault 1",
        "B = Short circuit fault 2",
        "C = Open circuit fault",
        "D = Open circuit fault.",
        "Power supplies 1, 2 and 3 connected in parallel to intrinsically",
        "safe apparatus",
    ], step=11, size=7.6)

    return _fig(svg(w, h, "".join(o), esc("Fig 13.42")),
                "Hình 13.42 · Ảnh hưởng của sự cố trong cáp nhiều lõi",
                "Figure 13.42 · Effects of faults in multicore cables",
                "Ba nguồn năng lượng ở bên trái đánh số 1, 2, 3 mắc song song tới ba "
                "hộp thiết bị an toàn nội tại bên phải bằng cáp nhiều lõi type 'C' "
                "gồm hai dẫn mỗi nhánh, mỗi nguồn có ký hiệu tiếp địa. Các vết đứt "
                "ngắn mạch màu đỏ nối các dẫn giữa các nhánh được ghi A và B; các "
                "dấu chéo hở mạch ghi C trên dẫn trên của nhánh giữa và D trên dẫn "
                "trên của nhánh dưới. Chú thích A đến D liệt kê hai lỗi ngắn mạch "
                "và hai lỗi hở mạch, trong đó chỉ dòng D có dấu chấm cuối",
                "Three power sources numbered 1, 2 and 3 on the left feed three blank "
                "intrinsically safe apparatus boxes on the right through type 'C' "
                "multicore cable with two conductors per run and an earth mark at each "
                "source. Red vertical links between runs mark short circuits A and B; "
                "red crosses mark open circuits C on the middle upper conductor and D "
                "on the bottom upper conductor. The legend lists A and B as short "
                "circuit faults 1 and 2 and C and D as open circuit faults, with the "
                "final full stop carried only by D, followed by the note that the "
                "power supplies are connected in parallel")


# ------------------------------------------------------------------ 13.43

@_reg
def fig_f1343():
    """Figure 13.43 - six faults A-F with blank right-hand apparatus boxes."""
    w, h = 680, 478
    o = [_defs(), _rect(0, 0, w, h, fill=PAPER, sw=0)]
    _title(o, 43, "Ảnh hưởng của sự cố trong cáp nhiều lõi",
           "Effects of faults in multicore cables", 7.2)

    o.append(T(190, 48, "Associated apparatus", 7.4))
    o.append(T(490, 48, "Intrinsically safe apparatus", 7.4))
    o.append(T(340, 44, "Multicore cable", 7.4))
    o.append(T(340, 55, "type 'C'", 7.4))

    for i, yy in enumerate((64, 190, 316), start=1):
        o.append(_rect(150, yy, 80, 56, fill="#eef3fb", sw=1.1))
        _lines(o, 190, yy + 21, ["Power", "source", str(i)],
               step=10, size=7.2)
        o.append(_rect(440, yy, 80, 56, fill="#ffffff", sw=1.1))
        _ground(o, 190, yy + 78)
        for ly in (yy + 18, yy + 36):
            o.append(_line(230, ly, 440, ly, sw=1.0, color=INK))
        o.append(_circle(390, yy + 18, 2.6, fill=INK, sw=0))
        o.append(_circle(390, yy + 36, 2.6, fill=INK, sw=0))

    o.append(_line(390, 82, 390, 140, sw=1.1, color=RED))
    o.append(_line(390, 154, 390, 208, sw=1.1, color=RED))
    o.append(T(397, 147, "A", 7.4, color=RED, weight="600"))
    o.append(_line(390, 226, 390, 280, sw=1.1, color=RED))
    o.append(_line(390, 294, 390, 334, sw=1.1, color=RED))
    o.append(T(397, 287, "B", 7.4, color=RED, weight="600"))
    _fault_x(o, 360, 82, "C")
    _fault_x(o, 330, 208, "D")
    _fault_x(o, 375, 226, "E")
    _fault_x(o, 360, 334, "F")

    _lines(o, 60, 408, [
        "A = Short circuit fault 1",
        "B = Short circuit fault 2",
        "C = Open circuit fault",
        "D = Open circuit fault",
        "E = Open circuit fault",
        "F = Open circuit fault",
    ], step=10.5, size=7.6)

    return _fig(svg(w, h, "".join(o), esc("Fig 13.43")),
                "Hình 13.43 · Ảnh hưởng của sự cố trong cáp nhiều lõi",
                "Figure 13.43 · Effects of faults in multicore cables",
                "Ba nguồn năng lượng bên trái đánh số 1, 2, 3 nối tới ba hộp thiết bị "
                "an toàn nội tại bên phải để trống bằng cáp nhiều lõi type 'C'. Các "
                "đường đỏ thẳng đứng giữa các nhánh dây biểu thị hai lỗi ngắn mạch A "
                "và B. Các dấu chéo hở mạch màu đỏ nằm trên dẫn trên của nhánh thứ "
                "nhất C, dẫn trên của nhánh thứ hai D, dẫn dưới của nhánh thứ hai E "
                "và dẫn trên của nhánh thứ ba F. Chú thích sáu dòng A đến F không có "
                "dấu chấm ở cuối dòng nào",
                "Three power sources numbered 1, 2 and 3 at the left connect through "
                "type 'C' multicore cable to three blank intrinsically safe apparatus "
                "boxes at the right. Red vertical links between cable runs show short "
                "circuit faults A and B. Red crosses show open circuit faults C on the "
                "first upper conductor, D on the second upper conductor, E on the "
                "second lower conductor and F on the third upper conductor. The six "
                "legend lines A through F have no final full stop")


# ------------------------------------------------------------------ 13.44

@_reg
def fig_f1344():
    """Figure 13.44 - screened cable cross-section and capacitance derivation."""
    w, h = 680, 326
    o = [_defs(), _rect(0, 0, w, h, fill=PAPER, sw=0)]
    _title(o, 44, "Ảnh hưởng của màn chắn đến điện dung cáp C_T",
           "Effects of screen on cable capacitance C_T", 7.2)

    o.append(_circle(340, 150, 95, fill="#ffffff", sw=1.4))
    o.append(_circle(340, 150, 91, fill="none", sw=0.8, color=GREY, dash="3 2"))
    for xx in (300, 380):
        o.append(_circle(xx, 150, 7, fill=INK, sw=0))
    o.append(_line(307, 150, 373, 150, sw=1.0, color=GREY, dash="3 2"))
    o.append(T(340, 143, "C_1", 7.8))
    o.append(T(276, 143, "C_s1", 7.6))
    o.append(T(404, 143, "C_s2", 7.6))
    o.append(T(230, 72, "Cable cores", 7.6, anchor="start"))
    o.append(_arrow(278, 78, 298, 143, sw=0.9, color=GREY, head="a7"))
    o.append(_arrow(288, 78, 378, 143, sw=0.9, color=GREY, head="a7"))
    o.append(T(430, 72, "Screen", 7.6, anchor="start"))
    o.append(_arrow(430, 78, 405, 90, sw=0.9, color=GREY, head="a7"))

    _lines(o, 340, 268, [
        "Capacitance between cores at worst",
        "C_T = C_1 + C_2 × C_3/C_2 + C_3",
        "If C_2 = C_3",
        "C_T = C_1 + 1/2C_2",
    ], step=14, size=8.4)

    return _fig(svg(w, h, "".join(o), esc("Fig 13.44")),
                "Hình 13.44 · Ảnh hưởng của màn chắn đến điện dung cáp C_T",
                "Figure 13.44 · Effects of screen on cable capacitance C_T",
                "Mặt cắt ngang của cáp có hai lõi dẫn màu đen nằm trong vòng màn chắn "
                "tròn. Một đường gạch đứt nối hai lõi mang nhãn C_1, trong khi các "
                "đoạn nhỏ ở hai bên mang nhãn C_s1 và C_s2. Mũi tên chỉ vào hai lõi "
                "với chú thích Cable cores và mũi tên chỉ vào vòng ngoài với chú "
                "thích Screen. Phía dưới là bốn dòng suy luận bắt đầu bằng "
                "Capacitance between cores at worst, công thức C_T bằng C_1 cộng "
                "C_2 nhân C_3 chia C_2 cộng C_3, giả thiết C_2 bằng C_3 và kết quả "
                "C_T bằng C_1 cộng một nửa C_2",
                "Cross-section of a cable with two dark core conductors inside a "
                "circular screen. A dashed line between the cores is labelled C_1 and "
                "the small sections on either side are C_s1 and C_s2. Arrows identify "
                "Cable cores and Screen. Below, four derivation lines start with "
                "Capacitance between cores at worst, give C_T as C_1 plus C_2 times "
                "C_3 over C_2 plus C_3, set C_2 equal to C_3 and conclude that C_T is "
                "C_1 plus half of C_2; the unusual printed algebra is retained")


# ------------------------------------------------------------------ 13.45

@_reg
def fig_f1345():
    """Figure 13.45 - two-core loop, split loops and stored-energy derivation."""
    w, h = 680, 400
    o = [_defs(), _rect(0, 0, w, h, fill=PAPER, sw=0)]
    _title(o, 45, "Ảnh hưởng của ngắn mạch cáp đến năng lượng cảm ứng",
           "Effect of short circuit cable faults on inductive stored energy", 7.2)

    _dim(o, 250, 560, 48, "Loop inductance L")
    for yy in (76, 96):
        o.append(_circle(250, yy, 3, fill="#ffffff", sw=1.0))
    o.append(_poly([(250, 76), (560, 76), (560, 96), (250, 96)],
                   fill="none", sw=1.2, color=INK))
    o.append(_arrow(190, 76, 238, 76, sw=1.0, color=INK, head="a7"))
    o.append(T(160, 70, "Current i", 7.6, anchor="start"))
    o.append(T(405, 112, "Two core cable", 7.6))
    o.append(T(405, 132, "Stored energy = 0.5 L i²", 8.2))

    _dim(o, 290, 560, 162, "Loop inductance L")
    for yy in (200, 210):
        o.append(_circle(225, yy, 2.5, fill="#ffffff", sw=1.0))
    o.append(_circle(260, 205, 3.5, fill=INK, sw=0))
    o.append(_line(225, 200, 260, 205, sw=1.0, color=INK))
    o.append(_line(225, 210, 260, 205, sw=1.0, color=INK))
    for yy in (180, 195, 220, 235):
        o.append(_line(260, 205, 290, yy, sw=1.0, color=INK))
        o.append(_line(290, yy, 560, yy, sw=1.1, color=INK))
    for ya, yb in ((180, 195), (220, 235)):
        o.append(_line(560, ya, 560, yb, sw=1.1, color=INK))
    o.append(T(272, 192, "0.5 i", 7.2, anchor="start"))
    o.append(T(272, 222, "0.5 i", 7.2, anchor="start"))
    o.append(T(150, 194, "Current", 7.6, anchor="start"))
    o.append(T(150, 207, "i", 7.6, anchor="start"))
    _dim(o, 290, 560, 255, "Loop inductance L", below=True)

    _lines(o, 60, 296, ["Stored energy", "", "Total stored energy", ""],
           step=14, size=8.0)
    _lines(o, 270, 296, ["= 0.5 L × (0.5 i)²", "= 0.125L i²",
                         "= 2 × 0.125 L i²", "= 0.25 L i²"],
           step=14, size=8.0)
    o.append(T(340, 362, "Lưu ý: Phép tính này không tính đến liên kết giữa hai vòng,",
               6.8))
    o.append(T(340, 373, "nhưng cho thấy ảnh hưởng của việc chia dòng điện.", 6.8))
    o.append(T(340, 384, "Note: This does not take account of mutual coupling between "
                         "the two loops but does indicate the effects of current division.",
               6.8))

    return _fig(svg(w, h, "".join(o), esc("Fig 13.45")),
                "Hình 13.45 · Ảnh hưởng của sự cố ngắn mạch cáp đến năng lượng tích "
                "trữ cảm ứng",
                "Figure 13.45 · Effect of short circuit cable faults on inductive "
                "stored energy",
                "Hình trên là cáp hai lõi tạo thành một vòng dẫn kín có độ tự cảm "
                "L mang dòng i và năng lượng tích trữ 0,5 L i². Hình dưới cho thấy "
                "sau ngắn mạch dòng điện được chia thành hai nhánh 0,5 i chạy trong "
                "hai vòng song song, mỗi vòng có độ tự cảm L. Các dòng công thức ghi "
                "năng lượng mỗi vòng 0,125L i² và tổng năng lượng 0,25 L i². Một "
                "Note hai ngôn ngữ nhắc rằng phép tính không xét liên kết giữa hai "
                "vòng nhưng cho thấy ảnh hưởng của việc chia dòng",
                "Upper drawing: a two-core cable forming a single closed loop of "
                "inductance L carrying current i, with stored energy 0.5 L i squared. "
                "Lower drawing: after a short-circuit fault the current divides into "
                "two 0.5 i paths in two parallel loops, each of inductance L. The "
                "derivation lines give 0.125L i squared per loop and a total of "
                "0.25 L i squared. A bilingual Note says the calculation ignores "
                "mutual coupling between the loops but shows the effect of current "
                "division")
