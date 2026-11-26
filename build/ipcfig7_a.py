# -*- coding: utf-8 -*-
"""Chapter 7 figure supplier A: recorders (figures 7.1-7.11, pages 329-336)."""
from ipcfig7_common import (BLUE, GREEN, GREY, INK, RED, H, W, T, _ar, _b,
                            _circle, _defs, _ellipse, _fig, _frame, _legend,
                            _line, _path, _poly, _rect, _mk, _series,
                            _wavey, make_registry)
import math

FIGS, _reg = make_registry()


# ----------------------------------------------------------------- helpers
def _coil(x, y, w, n=4, amp=9, color=INK):
    """A horizontal winding of ``n`` semicircular humps."""
    step = w / float(n)
    d = "M %s,%s" % (x, y)
    for i in range(n):
        d += " q %s,%s %s,0" % (step / 2.0, -amp, step)
    return _path(d, sw=1.3, color=color)


def _tri(x, y, w, h, label):
    """Amplifier triangle with its label above."""
    o = [_poly([(x, y), (x, y + h), (x + w, y + h / 2.0)],
               fill="#ffffff", sw=1.3, close=True)]
    o.append(T(x + w / 2.0, y - 4, label, 7.0))
    return "".join(o)


# ----------------------------------------------------------------- 7.1
@_reg
def fig_f01():
    """Fig. 7.1 - self-balancing potentiometric recorder loop."""
    o = [_defs()]
    # potentiometer strip and its sliding contact
    o.append(_rect(45, 25, 125, 48, fill="#fbfaf7"))
    o.append(_line(45, 32, 170, 32, sw=1.4))
    o.append(T(107, 19, "Potentiometer", 7.6))
    o.append(_ar(128, 68, 106, 38, color=INK, sw=1.3))
    # unknown-potential terminals
    o.append(_line(62, 73, 62, 196, sw=1.0))
    o.append(_circle(62, 200, 2.6, fill="#ffffff"))
    o.append(_line(153, 73, 153, 196, sw=1.0))
    o.append(_circle(153, 200, 2.6, fill="#ffffff"))
    o.append(T(107, 218, "Unknown potential", 7.2))
    # wiper shaft down to converter
    o.append(_line(128, 68, 128, 140, sw=1.0))
    o.append(_line(128, 140, 205, 140, sw=1.0))
    o.append(_b(205, 126, 80, 28, "Converter", size=7.6))
    o.append(_line(285, 135, 340, 140, sw=1.0))
    o.append(_line(285, 148, 340, 155, sw=1.0))
    o.append(_b(340, 130, 86, 40, "A.C.\namplifier", size=7.2))
    # input winding feeding the servomotor
    o.append(_line(360, 130, 360, 112, sw=1.0))
    o.append(_coil(360, 112, 48, 3, 10))
    o.append(_line(408, 112, 408, 96, sw=1.0))
    o.append(_line(408, 96, 470, 96, sw=1.0))
    # servomotor and mechanical feedback coupling
    o.append(_circle(470, 80, 16, fill="#fbfaf7", sw=1.4))
    o.append(_circle(470, 80, 2.6, fill=INK, sw=0))
    o.append(T(470, 52, "A.C. servomotor", 7.4))
    o.append(_line(128, 80, 454, 80, sw=1.0, dash="6 4", color=GREY))
    o.append(T(290, 74, "Mechanical coupling", 7.2, color=GREY))
    # reference winding on the stator
    o.append(_coil(498, 80, 50, 4, 9))
    o.append(_line(498, 80, 498, 66, sw=1.0))
    o.append(_line(498, 66, 566, 66, sw=1.0))
    o.append(_circle(570, 66, 2.4, fill="#ffffff"))
    o.append(_line(548, 80, 548, 94, sw=1.0))
    o.append(_line(548, 94, 566, 94, sw=1.0))
    o.append(_circle(570, 94, 2.4, fill="#ffffff"))
    o.append(T(578, 80, "Reference winding", 7.0, anchor="start"))
    return _mk(1, o, "Potentiometric recorder null-balance loop",
               "Vòng cân bằng tự động của máy ghi thế kế",
               "Potentiometric recorder null-balance loop",
               "Sơ đồ vòng cân bằng: thế chưa biết qua bộ chuyển đổi và khuếch đại xoay chiều để điều khiển động cơ servo; khớp nối cơ học đưa con trò về cân bằng, cuộn tham chiếu cấp nguồn cho động cơ.",
               "Block diagram of the null-balance loop: the unknown potential passes through a converter and an A.C. amplifier to drive a servomotor; a mechanical coupling returns the wiper to balance while a reference winding energises the motor.")


# ----------------------------------------------------------------- 7.2
@_reg
def fig_f02():
    """Fig. 7.2 - circular chart with its 24-hour drive."""
    o = [_defs()]
    cx, cy, r = 215, 122, 84
    o.append(_circle(cx, cy, r, fill="#fbfaf7", sw=1.5))
    for rr in (22, 42, 62):
        o.append(_circle(cx, cy, rr, sw=0.6, color="#c4c4c4"))
    for a in range(0, 360, 30):
        rad = math.radians(a)
        o.append(_line(cx + 22 * math.cos(rad), cy + 22 * math.sin(rad),
                       cx + r * math.cos(rad), cy + r * math.sin(rad),
                       sw=0.6, color="#cfcfcf"))
    for a in range(0, 360, 15):
        rad = math.radians(a)
        o.append(_line(cx + (r - 5) * math.cos(rad), cy + (r - 5) * math.sin(rad),
                       cx + r * math.cos(rad), cy + r * math.sin(rad), sw=0.9))
    o.append(_circle(cx, cy, 9, fill="#eef3fb", sw=1.2))
    o.append(_circle(cx, cy, 2.4, fill=INK, sw=0))
    # pen arm and nib
    o.append(_line(cx, cy, cx + 58, cy - 58, sw=2.0, color=RED))
    o.append(_poly([(cx + 58, cy - 58), (cx + 66, cy - 68), (cx + 60, cy - 54)],
                   fill=RED, sw=0.6, close=True))
    o.append(T(cx - 10, cy + 17, "0", 7.0))
    o.append(T(282, 58, "100", 7.0, anchor="start"))
    o.append(T(282, 72, "10", 7.0, anchor="start"))
    # dashed rotation arc
    pts = []
    for a in range(200, 341, 20):
        rad = math.radians(a)
        pts.append((cx + 94 * math.cos(rad), cy + 94 * math.sin(rad)))
    o.append(_poly(pts, sw=1.0, color=GREY, dash="4 3"))
    o.append(_ar(pts[-2][0], pts[-2][1], pts[-1][0], pts[-1][1],
                 color=GREY, sw=1.0))
    o.append(T(cx, 226, "One revolution / 24 h", 7.0, color=GREY))
    # annotation list
    o.append(T(345, 46, "Circular chart", 8.4, weight="bold"))
    o.append(_line(300, 62, 338, 74, color=GREY, sw=0.9))
    o.append(T(345, 78, "Pen arm on chart", 7.4))
    o.append(_line(224, 122, 338, 100, color=GREY, sw=0.9))
    o.append(T(345, 104, "Chart hub / centre", 7.4))
    o.append(T(345, 130, "0-100 linear scale", 7.4))
    o.append(T(345, 152, "0-10 square-root scale", 7.4))
    o.append(T(345, 174, "Light spring on pen tip", 7.4))
    o.append(T(345, 196, "8 A.M. to 8 A.M. next day", 7.4))
    return _mk(2, o, "Circular chart mechanism",
               "Cơ cấu biểu đồ tròn",
               "Circular chart mechanism",
               "Đĩa biểu đồ tròn có lưới đồng tâm và vạch thời gian 24 giờ; cần bút đặt nhẹ trên mặt giấy, quay một vòng mỗi ngày quanh trục tâm biểu đồ.",
               "Circular chart with a concentric grid and 24-hour time marks; the spring-loaded pen arm rests on the chart, which turns one revolution per day about its central hub.")


# ----------------------------------------------------------------- 7.3
@_reg
def fig_f03():
    """Fig. 7.3 - strip chart mechanism with pen mounting levers."""
    o = [_defs()]
    o.append(T(325, 26, "Mounting arrangement for pen", 7.8))
    o.append(_rect(200, 36, 250, 168, fill="#fbfaf7", sw=1.4))
    # chart disc and hub
    o.append(_circle(325, 132, 46, fill="#ffffff", sw=1.2))
    for rr in (12, 24, 36):
        o.append(_circle(325, 132, rr, sw=0.6, color="#c4c4c4"))
    for a in range(0, 360, 45):
        rad = math.radians(a)
        o.append(_line(325 + 12 * math.cos(rad), 132 + 12 * math.sin(rad),
                       325 + 46 * math.cos(rad), 132 + 46 * math.sin(rad),
                       sw=0.6, color="#cfcfcf"))
    o.append(_circle(325, 132, 7, fill="#eef3fb", sw=1.1))
    o.append(_circle(325, 132, 2, fill=INK, sw=0))
    # three mounting levers A, B, C
    o.append(_line(270, 60, 325, 70, sw=1.2))
    o.append(_line(325, 58, 325, 70, sw=1.2))
    o.append(_line(380, 60, 325, 70, sw=1.2))
    for xx, yy, lab in ((270, 58, "A"), (325, 56, "B"), (380, 58, "C")):
        o.append(_circle(xx, yy, 2.6, fill="#ffffff"))
        o.append(T(xx, yy - 8, lab, 7.4))
    # pen arm down to the chart
    o.append(_line(325, 70, 325, 130, sw=2.0, color=RED))
    o.append(_poly([(321, 130), (329, 130), (325, 138)],
                   fill=RED, sw=0.6, close=True))
    # time slots along the lower edge
    for i in range(10):
        o.append(_rect(210 + i * 23, 185, 18, 8, fill="#eef3fb", sw=0.8))
    # left-hand callouts
    for ly, lab, tx in ((62, "Penlifting system", 72),
                        (90, "Measuring assembly", 100),
                        (118, "Pen arm", 112),
                        (146, "Recorder pen", 136),
                        (174, "Time slots", 190)):
        o.append(T(195, ly, lab, 7.0, anchor="end"))
        o.append(_line(198, ly - 2, 250 if ly < 130 else 285, tx,
                       color=GREY, sw=0.8))
    # right-hand callouts
    o.append(_line(380, 60, 455, 62, color=GREY, sw=0.8))
    for ry, lab in ((64, "Base end point"), (92, "Chart hub"),
                    (120, "Casing"), (148, "Chart drive")):
        o.append(T(459, ry, lab, 7.0))
    return _mk(3, o, "Strip chart mechanism with pen arm",
               "Cơ cấu biểu đồ dải với cần bút",
               "Strip chart mechanism with pen arm",
               "Mặt trước cơ cấu ghi: vỏ máy, đĩa biểu đồ và trục, cần bút nối ba cần A, B, C, hệ nâng bút, các khe thời gian và đầu bút ghi.",
               "Front view of the recording mechanism: casing, chart disc and hub, pen arm linked to levers A, B and C, pen-lifting system, time slots and recorder pen.")


# ----------------------------------------------------------------- 7.4
@_reg
def fig_f04():
    """Fig. 7.4 - strip chart with dual linear and square-root scales."""
    o = [_defs()]
    o.append(T(340, 18, "Dual scale: 0-100 linear / 0-10 square root", 8.2))
    o.append(_rect(170, 36, 300, 154, fill="#fbfaf7", sw=1.3))
    for i in range(9):
        yy = 48 + i * 16
        o.append(_line(170, yy, 470, yy, sw=0.5, color="#d8d8d8"))
        o.append(T(164, yy + 2.4, str(20 + i * 10), 7.0, anchor="end"))
    for i in range(10):
        o.append(T(477, 48 + i * 15.5, str(i + 1), 7.0, anchor="start"))
    for xx in range(200, 471, 30):
        o.append(_path("M %s,36 Q %s,111 %s,190" % (xx, xx + 8, xx),
                       sw=0.6, color="#d8d8d8"))
    # active and dummy rollers
    for xx in (185, 455):
        for yy in (30, 196):
            o.append(_circle(xx, yy, 6, fill="#ffffff", sw=1.1))
            o.append(_circle(xx, yy, 1.8, fill=INK, sw=0))
    o.append(T(185, 212, "Active roller", 7.0))
    o.append(T(455, 212, "Dummy roller", 7.0))
    # pen trace
    trace = [(198, 150), (230, 122), (262, 142), (294, 110), (326, 132),
             (358, 100), (390, 124), (422, 104), (452, 120)]
    o.append(_poly(trace, sw=1.8, color=BLUE))
    # ink reservoir and servo-linked pen arm
    o.append(_rect(500, 26, 28, 10, fill=INK, sw=0.8))
    o.append(T(514, 22, "Ink reservoir", 7.0, anchor="start"))
    o.append(_line(500, 32, 440, 32, sw=1.3))
    o.append(_line(440, 32, 430, 92, sw=1.3, color=RED))
    o.append(_poly([(430, 92), (424, 86), (428, 96)],
                   fill=RED, sw=0.6, close=True))
    o.append(T(444, 100, "Pen tip", 7.0))
    o.append(_circle(505, 122, 2.4, fill=INK, sw=0))
    o.append(T(513, 119, "Connected to", 7.0, anchor="start"))
    o.append(T(513, 131, "servo system", 7.0, anchor="start"))
    return _mk(4, o, "Strip chart with dual linear and square-root scales",
               "Biểu đồ dải với thang kép tuyến tính và căn bậc hai",
               "Strip chart with dual linear and square-root scales",
               "Giấy biểu đồ cuộn giữa hai trục, thang trái 0-100 tuyến tính và thang phải 0-10 căn bậc hai; bút được cấp mực từ hộp chứa và nối với hệ servo.",
               "Chart paper running between two rollers, with a linear 0-100 scale on the left and a square-root 0-10 scale on the right; the pen is fed from an ink reservoir and linked to the servo system.")


# ----------------------------------------------------------------- 7.5
@_reg
def fig_f05():
    """Fig. 7.5 - fanfold chart folded in a zig-zag stack."""
    o = [_defs()]
    o.append(T(340, 28, "Fanfold chart - zig-zag folding", 8.6))
    o.append(_rect(130, 50, 420, 145, fill="#fbfaf7", sw=1.2))
    o.append(_line(150, 80, 530, 80, sw=0.8, color="#cfcfcf"))
    o.append(_line(150, 170, 530, 170, sw=0.8, color="#cfcfcf"))
    pts = []
    for i in range(13):
        pts.append((150 + i * 31.6, 80 if i % 2 == 0 else 170))
    o.append(_poly(pts, sw=1.3, color=BLUE))
    for px, py in pts:
        o.append(_circle(px, py, 1.8, fill="#ffffff", sw=0.9))
    # drive roller with engaging teeth
    o.append(_circle(565, 125, 17, fill="#eef3fb", sw=1.3))
    o.append(_circle(565, 125, 3, fill=INK, sw=0))
    for a in range(0, 360, 45):
        rad = math.radians(a)
        o.append(_line(565 + 17 * math.cos(rad), 125 + 17 * math.sin(rad),
                       565 + 22 * math.cos(rad), 125 + 22 * math.sin(rad),
                       sw=0.9))
    o.append(T(565, 160, "Drive roller", 7.0))
    o.append(T(210, 210, "Zig-zag pleats", 7.0))
    o.append(T(370, 210, "Corner perforations", 7.0))
    o.append(T(535, 210, "Roller teeth", 7.0))
    return _mk(5, o, "Fanfold chart zig-zag folding",
               "Giấy biểu đồ xếp nếp zig-zag",
               "Fanfold chart zig-zag folding",
               "Giấy biểu đồ xếp thành các nếp gấp zig-zag đều, có lỗ đục ở hai góc để ăn khớp với răng của trục lăn dẫn giấy.",
               "Chart paper folded into regular zig-zag pleats, with punched corner holes that engage the teeth of the chart drive roller.")


# ----------------------------------------------------------------- 7.6
@_reg
def fig_f06():
    """Fig. 7.6 - felt ink-pad and its pen."""
    o = [_defs()]
    o.append(T(300, 26, "Felt ink-pad pen", 8.6))
    o.append(_circle(300, 78, 42, fill="#fbfaf7", sw=1.4))
    o.append(_circle(300, 78, 21, sw=1.0, color="#bdbdbd"))
    o.append(_circle(300, 78, 3, fill=INK, sw=0))
    o.append(_line(300, 120, 300, 127, sw=1.4, color=RED))
    o.append(_rect(255, 127, 90, 42, fill="#f6e6c8", sw=1.2))
    for xx in (270, 285, 300, 315, 330):
        o.append(_line(xx, 127, xx, 169, sw=0.9, dash="4 3", color="#9a7b50"))
    o.append(_line(253, 148, 347, 148, sw=0.9, dash="4 3", color="#9a7b50"))
    o.append(T(370, 62, "Pen head", 7.2))
    o.append(_line(342, 72, 366, 64, color=GREY, sw=0.9))
    o.append(T(370, 92, "Centre dot", 7.2))
    o.append(_line(303, 78, 366, 88, color=GREY, sw=0.9))
    o.append(T(370, 140, "Six felt buckets", 7.2))
    o.append(_line(347, 140, 366, 140, color=GREY, sw=0.9))
    o.append(T(300, 188, "Ink-impregnated felt, six colours", 7.4))
    return _mk(6, o, "Felt ink-pad pen",
               "Bút với miếng nỉ thấm mực",
               "Felt ink-pad pen",
               "Đầu bút tròn tiếp xúc miếng đệm gồm sáu ngăn nỉ thấm mực, mỗi ngăn một màu cho cơ cấu in chấm nhiều điểm.",
               "A round pen head contacts a six-bucket felt pad, each bucket impregnated with a different ink for multi-point dot printing.")


# ----------------------------------------------------------------- 7.7
@_reg
def fig_f07():
    """Fig. 7.7 - circular pen-tip with six impregnated points."""
    o = [_defs()]
    cx, cy, r = 300, 122, 60
    o.append(T(cx, 28, "Circular pen-tip", 8.6))
    # six bucket-like teeth around the rim
    for i in range(1, 7):
        a = math.radians(-90 + (i - 1) * 60)
        a1 = math.radians(-90 + (i - 1) * 60 - 20)
        a2 = math.radians(-90 + (i - 1) * 60 + 20)
        p1 = (cx + r * math.cos(a1), cy + r * math.sin(a1))
        p2 = (cx + r * math.cos(a2), cy + r * math.sin(a2))
        tip = (cx + (r + 17) * math.cos(a), cy + (r + 17) * math.sin(a))
        o.append(_path("M %s,%s Q %s,%s %s,%s"
                       % (p1[0], p1[1], tip[0], tip[1], p2[0], p2[1]),
                       sw=1.5, color=INK))
        o.append(_line(p1[0], p1[1], p2[0], p2[1], sw=1.0, color=GREY))
    o.append(_circle(cx, cy, r, fill="#fbfaf7", sw=1.4))
    for i in range(1, 7):
        a = math.radians(-90 + (i - 1) * 60)
        lx = cx + (r - 18) * math.cos(a)
        ly = cy + (r - 18) * math.sin(a)
        o.append(T(lx, ly + 2.8, str(i), 8.0))
    o.append(_circle(cx, cy, 3, fill=INK, sw=0))
    o.append(T(cx, 210, "Six ink-impregnated points", 7.4))
    o.append(T(cx, 226, "Pen rotates to select a colour", 7.0, color=GREY))
    return _mk(7, o, "Circular pen-tip with six ink points",
               "Đầu bút tròn có sáu điểm thấm mực",
               "Circular pen-tip with six ink points",
               "Đầu bút dạng đĩa có sáu điểm nhọn hình xô quanh chu vi, đánh số 1 đến 6; đầu bút quay để chọn màu mực.",
               "A disc-shaped pen tip with six bucket-like points around its rim, numbered 1 to 6; the tip rotates to select the required ink colour.")


# ----------------------------------------------------------------- 7.8
@_reg
def fig_f08():
    """Fig. 7.8 - fanfold chart stack and model numbers."""
    o = [_defs()]
    o.append(T(340, 28, "Fanfold chart stack - model numbers", 8.4))
    o.append(_rect(110, 44, 460, 150, fill="#fbfaf7", sw=1.2))
    for x0 in (160, 220, 280, 340, 400, 460):
        pts = [(x0 + (12 if j % 2 else -12), 58 + j * 19)
               for j in range(8)]
        o.append(_poly(pts, sw=1.2, color=BLUE))
    o.append(_circle(122, 52, 2.4, fill="#ffffff"))
    o.append(_circle(558, 52, 2.4, fill="#ffffff"))
    for k, lab in enumerate(("08/40", "MOD.1", "05/40", "05/01", "08/01")):
        yy = 66 + k * 26
        o.append(_rect(500, yy - 10, 60, 20, fill="#eef3fb", sw=0.8))
        o.append(T(530, yy + 2.8, lab, 7.2))
    for xx, lab in ((150, "24"), (235, "19"), (300, "20"),
                    (365, "21"), (430, "22")):
        o.append(T(xx, 212, lab, 7.2))
    return _mk(8, o, "Fanfold chart stack and model numbers",
               "Chồng giấy biểu đồ xếp nếp và mã mẫu",
               "Fanfold chart stack and model numbers",
               "Chồng giấy biểu đồ xếp nếp dạng sóng trong khay, ký hiệu mã mẫu ở cột phải và số thứ tự nếp gấp ở dưới đáy.",
               "A pleated fanfold chart stack in its tray, with model codes in a right-hand column and fold numbers along the bottom edge.")


# ----------------------------------------------------------------- 7.9
@_reg
def fig_f09():
    """Fig. 7.9 - magnetic tape recorder with write and read heads."""
    o = [_defs()]
    o.append(T(340, 26, "Magnetic tape recorder - write and read heads", 8.4))
    o.append(T(45, 82, "Input", 7.4, anchor="start"))
    o.append(_ar(88, 78, 116, 78, color=INK, sw=1.2))
    o.append(_tri(116, 64, 40, 28, "Amplifier"))
    o.append(_line(156, 78, 156, 150, sw=1.1))
    o.append(_line(156, 150, 168, 150, sw=1.1))
    # tape line and reels
    o.append(_line(110, 150, 520, 150, sw=1.6))
    for xx in (110, 520):
        o.append(_circle(xx, 150, 7, fill="#ffffff", sw=1.1))
        o.append(_circle(xx, 150, 2, fill=INK, sw=0))
    # write head
    o.append(_path("M 168,150 L 168,141 A 10,10 0 0 1 188,141 L 188,150",
                   sw=1.3))
    o.append(T(178, 172, "Write head", 7.2))
    # read head
    o.append(_path("M 320,150 L 320,141 A 10,10 0 0 1 340,141 L 340,150",
                   sw=1.3))
    o.append(_line(330, 141, 330, 133, sw=1.0, color=GREY))
    o.append(T(330, 172, "Read head", 7.2))
    # read amplifier chain
    o.append(_line(330, 133, 330, 78, sw=1.1))
    o.append(_ar(330, 78, 358, 78, color=INK, sw=1.2))
    o.append(_tri(358, 64, 40, 28, "Amplifier"))
    o.append(_ar(398, 78, 432, 78, color=INK, sw=1.2))
    o.append(T(438, 82, "Output", 7.4, anchor="start"))
    o.append(_ar(220, 140, 270, 140, color=GREY, sw=1.0))
    o.append(T(245, 134, "tape motion", 7.0, color=GREY))
    o.append(T(315, 196, "Plastic tape coated with magnetic material", 7.4))
    o.append(_ar(410, 188, 425, 154, color=GREY, sw=0.9))
    return _mk(9, o, "Magnetic tape recorder with write and read heads",
               "Máy ghi băng từ với đầu ghi và đầu đọc",
               "Magnetic tape recorder with write and read heads",
               "Tín hiệu vào khuếch đại tới đầu ghi, ghi từ tính lên băng nhựa phủ vật liệu từ tính; đầu đọc nhận tín hiệu rồi khuếch đại thành đầu ra.",
               "The input is amplified and applied to the write head, which magnetises plastic tape coated with magnetic material; a read head senses the flux changes and feeds an output amplifier.")


# ----------------------------------------------------------------- 7.10
@_reg
def fig_f10():
    """Fig. 7.10 - digital tape NRZ saturation waveform."""
    o = [_defs()]
    o.append(T(340, 26, "Digital tape recording - NRZ saturation waveform", 8.2))
    bits = [1, 1, 1, 0, 1, 0, 0, 1]
    levels = [1, -1, 1, -1, -1, 1, 1, 1]
    x0, cw = 90, 52
    ypos = {1: 80, -1: 180}
    for i, b in enumerate(bits):
        o.append(T(x0 + cw * i + cw / 2.0, 52, str(b), 8.0))
    pts = [(x0, ypos[levels[0]])]
    for i in range(8):
        pts.append((x0 + cw * (i + 1), ypos[levels[i]]))
        if i < 7 and levels[i] != levels[i + 1]:
            pts.append((x0 + cw * (i + 1), ypos[levels[i + 1]]))
        elif i == 7:
            pts.append((x0 + cw * 8, ypos[-1]))
    o.append(_poly(pts, sw=1.7, color=BLUE))
    o.append(_line(x0, 130, x0 + cw * 8, 130, sw=1.0))
    o.append(T(x0 - 8, 134, "0", 7.2, anchor="end"))
    o.append(_line(x0, 80, x0 + cw * 8, 80, sw=0.6, dash="4 4", color="#cccccc"))
    o.append(_line(x0, 180, x0 + cw * 8, 180, sw=0.6, dash="4 4", color="#cccccc"))
    o.append(T(526, 84, "Positive saturation level", 6.8, anchor="start"))
    o.append(T(526, 184, "Negative saturation level", 6.8, anchor="start"))
    o.append(T(300, 214, "NRZ: flux reversal = 1, no reversal = 0", 7.0,
               color=GREY))
    return _mk(10, o, "Digital tape saturation waveform (NRZ)",
               "Dạng sóng bão hòa số theo mã NRZ",
               "Digital tape saturation waveform (NRZ)",
               "Dãy bit 1 1 1 0 1 0 0 1 mã hóa thành sóng vuông giữa hai mức bão hòa dương và âm; bit 1 đảo chiều từ thông, bit 0 giữ nguyên.",
               "The bit pattern 1 1 1 0 1 0 0 1 is encoded as a square wave between positive and negative saturation levels; a 1 reverses flux direction while a 0 keeps it unchanged.")


# ----------------------------------------------------------------- 7.11
@_reg
def fig_f11():
    """Fig. 7.11 - X-Y plotter servo drives and pen assembly."""
    o = [_defs()]
    o.append(T(340, 22, "X-Y plotter - servo drives and pen assembly", 8.2))
    # X channel
    o.append(T(32, 64, "X-input", 7.2, anchor="start"))
    o.append(_ar(86, 60, 104, 60, color=INK, sw=1.1))
    o.append(_b(104, 45, 88, 30, "Balancing\nsystem", size=7.0))
    o.append(_ar(192, 60, 210, 60, color=INK, sw=1.1))
    o.append(_b(210, 45, 82, 30, "Chopper\ncircuit", size=7.0))
    o.append(_ar(292, 60, 312, 60, color=INK, sw=1.1))
    o.append(_tri(312, 45, 40, 30, "Servo-amplifier"))
    o.append(_line(352, 60, 374, 60, sw=1.1))
    o.append(_circle(382, 60, 8, fill="#ffffff", sw=1.2))
    o.append(T(382, 84, "Pen drive servo", 7.0))
    # Y channel
    o.append(T(32, 184, "Y-input", 7.2, anchor="start"))
    o.append(_ar(86, 180, 104, 180, color=INK, sw=1.1))
    o.append(_b(104, 165, 88, 30, "Balancing\nsystem", size=7.0))
    o.append(_ar(192, 180, 210, 180, color=INK, sw=1.1))
    o.append(_b(210, 165, 82, 30, "Chopper\ncircuit", size=7.0))
    o.append(_ar(292, 180, 312, 180, color=INK, sw=1.1))
    o.append(_tri(312, 165, 40, 30, "Servo-amplifier"))
    o.append(_line(352, 180, 374, 180, sw=1.1))
    o.append(_circle(382, 180, 8, fill="#ffffff", sw=1.2))
    o.append(T(382, 204, "Assembly drive servo", 7.0))
    # potentiometer and standard supply linking the two channels
    o.append(_line(120, 75, 120, 165, sw=1.0, color=GREY))
    o.append(_ar(120, 120, 141, 120, color=INK, sw=1.0))
    o.append(_rect(142, 92, 12, 56, fill="#ffffff", sw=1.2))
    o.append(T(160, 116, "Eb", 7.2, anchor="start"))
    o.append(_line(154, 120, 186, 120, color=GREY, sw=0.8))
    o.append(T(190, 123, "Standard supply", 7.0, anchor="start"))
    # chart paper and pen carriage
    o.append(_rect(452, 40, 148, 150, fill="#fbfaf7", sw=1.2))
    for gx in range(477, 578, 25):
        o.append(_line(gx, 40, gx, 190, sw=0.5, color="#e2e2e2"))
    for gy in range(65, 190, 25):
        o.append(_line(452, gy, 600, gy, sw=0.5, color="#e2e2e2"))
    o.append(_rect(500, 90, 40, 10, fill="#eef3fb", sw=1.0))
    o.append(_line(520, 100, 520, 135, sw=2.0, color=RED))
    o.append(_poly([(516, 135), (524, 135), (520, 143)],
                   fill=RED, sw=0.6, close=True))
    o.append(_ar(390, 60, 448, 72, color=GREY, sw=1.0))
    o.append(_ar(390, 180, 448, 158, color=GREY, sw=1.0))
    o.append(T(526, 34, "Chart paper", 7.2))
    o.append(_ar(470, 170, 510, 170, color=GREY, sw=0.9))
    o.append(T(490, 166, "X", 6.8, color=GREY))
    o.append(_ar(584, 150, 584, 110, color=GREY, sw=0.9))
    o.append(T(590, 132, "Y", 6.8, color=GREY))
    o.append(T(526, 205, "Pen and arm", 7.2))
    o.append(T(526, 222, "Complete assembly", 7.0, color=GREY))
    return _mk(11, o, "X-Y plotter servo, chart and pen assembly",
               "Máy vẽ X-Y với cơ cấu servo và cần bút",
               "X-Y plotter servo, chart and pen assembly",
               "Tín hiệu X và Y qua hệ cân bằng, mạch chopper và bộ khuếch đại servo để điều khiển riêng động cơ cần bút và động cơ cụm bút trên giấy biểu đồ.",
               "X and Y inputs pass through balancing systems, chopper circuits and servo amplifiers to drive separate pen and assembly servomotors that position the pen over the chart paper.")
