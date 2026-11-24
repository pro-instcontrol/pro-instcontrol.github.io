# -*- coding: utf-8 -*-
"""Vector figures 3.37-3.54 for the IPC Chapter 3 bilingual reader."""
import math
from ipcfig3_common import (BLUE, GREEN, GREY, INK, RED, H, W, T, _ar, _b,
                            _circle, _defs, _ellipse, _fig, _frame, _legend,
                            _line, _path, _poly, _rect, _mk, _series, _wavey,
                            make_registry)

FIGS, _reg = make_registry()


def _hatchv(x, y, w, h, step=6, color=GREY):
    """Light vertical hatching for metal walls and plates."""
    o = []
    for yy in range(int(y), int(y + h), step):
        o.append(_line(x, yy, x + w, min(y + h, yy + 5), sw=0.5, color=color))
    return "".join(o)


def _oval(cx, cy, rx, ry, ang=0.0, n=28):
    """Points of an ellipse rotated by ang radians (oval-gear rotor)."""
    ca, sa = math.cos(ang), math.sin(ang)
    pts = []
    for i in range(n):
        t = 2.0 * math.pi * i / n
        u, v = rx * math.cos(t), ry * math.sin(t)
        pts.append((cx + u * ca - v * sa, cy + u * sa + v * ca))
    return pts


# ---------------------------------------------------------------- 3.37
@_reg
def fig_f37():
    """Variable area meter: float balanced in a tapered metering tube."""
    o = [_defs()]
    # tapered meter tube, narrow at the inlet and wide at the outlet
    o.append(_poly([(302, 45), (306, 45), (326, 190), (322, 190)],
                   fill="#dfe6ef", sw=0.9, close=True))
    o.append(_poly([(374, 45), (378, 45), (358, 190), (354, 190)],
                   fill="#dfe6ef", sw=0.9, close=True))
    o.append(_line(302, 45, 322, 190, sw=1.3))
    o.append(_line(378, 45, 358, 190, sw=1.3))
    o.append(_hatchv(302, 50, 5, 136, step=9))
    o.append(_hatchv(374, 50, 5, 136, step=9))
    # the float
    o.append(_rect(324, 108, 32, 26, "#e9e3d6", sw=1.2))
    o.append(_ellipse(340, 108, 16, 4, fill="#f4f6fa", sw=1.0))
    o.append(_ellipse(340, 134, 16, 4, fill="#d9d1be", sw=1.0))
    # flow through the tube
    o.append(_ar(340, 196, 340, 222, color=BLUE))
    o.append(T(340, 231, "Inlet flow", 7.0, color=BLUE))
    o.append(_ar(340, 42, 340, 16, color=BLUE))
    o.append(T(340, 11, "Outlet flow", 7.0, color=BLUE))
    # force balance on the float
    o.append(_ar(340, 106, 340, 76, color=GREEN))
    o.append(T(352, 82, "Upward thrust", 7.0, color=GREEN))
    o.append(_ar(340, 136, 340, 166, color=RED))
    o.append(T(328, 162, "Weight of the float", 7.0, color=RED, anchor="end"))
    o.append(T(58, 92, "Differential pressure", 7.0))
    o.append(T(58, 102, "acting upon the float", 7.0))
    o.append(_ar(160, 108, 315, 122, color=GREY))
    o.append(T(185, 178, "Meter tube", 7.0))
    o.append(_ar(248, 175, 322, 175, color=GREY))
    o.append(T(405, 128, "Float", 7.0))
    o.append(_ar(398, 125, 358, 122, color=GREY))
    return _mk(37, o, "Figure 3.37 - Variable area meter",
               "Rotameter: phao nổi cân bằng trong ống đo loe dần",
               "Rotameter: a float in equilibrium inside a tapered meter tube",
               "Sơ đồ rotameter với ống loe dần, phao nổi, dòng vào và dòng ra, lực đẩy lên, trọng lực và áp suất chênh lệch",
               "Simplified variable area meter showing the tapered tube, float, inlet and outlet flow, upward thrust, float weight and differential pressure")


# ---------------------------------------------------------------- 3.38
@_reg
def fig_f38():
    """Electromagnetic flowmeter with coils, electrodes and V-B-e triad."""
    o = [_defs()]
    o.append(_rect(120, 100, 420, 44, "#eef3fb", sw=1.2))
    o.append(_line(120, 122, 540, 122, sw=0.5, dash="4,4", color=GREY))
    o.append(_ar(165, 112, 245, 112, color=BLUE))
    o.append(T(205, 135, "Process fluid", 6.8, color=BLUE))
    # magnet poles and exciting coils
    o.append(_rect(250, 56, 100, 38, "#f4f6fa", sw=1.1))
    o.append(_rect(250, 150, 100, 38, "#f4f6fa", sw=1.1))
    for i in range(6):
        o.append(_line(258 + i * 16, 58, 258 + i * 16, 92, sw=0.8, color=GREY))
        o.append(_line(258 + i * 16, 152, 258 + i * 16, 186, sw=0.8, color=GREY))
    o.append(T(300, 50, "Electromagnet / exciting coil", 7.2, weight="bold"))
    o.append(T(300, 82, "N", 8.0, color=RED))
    o.append(T(300, 176, "S", 8.0, color=BLUE))
    # flush electrodes
    o.append(_circle(470, 100, 4.5, fill="#ffffff", sw=1.0))
    o.append(_circle(470, 144, 4.5, fill="#ffffff", sw=1.0))
    o.append(_line(470, 95, 470, 82, sw=1.0))
    o.append(_line(470, 149, 470, 162, sw=1.0))
    o.append(T(505, 92, "Electrodes", 7.0))
    o.append(_ar(500, 95, 475, 99, color=GREY))
    # internal diameter and tube
    o.append(_ar(148, 100, 148, 144, color=GREY, sw=1.0))
    o.append(T(140, 125, "d", 7.5, anchor="end"))
    o.append(T(180, 172, "Measuring tube", 7.0))
    o.append(_ar(215, 168, 215, 146, color=GREY))
    # vector triad V, B, e
    ox, oy = 586, 196
    o.append(_ar(ox, oy, ox - 26, oy - 24, color=INK))
    o.append(T(ox - 34, oy - 28, "V", 8.0))
    o.append(_ar(ox, oy, ox + 14, oy + 22, color=GREEN))
    o.append(T(ox + 18, oy + 27, "B", 8.0, color=GREEN))
    o.append(_ar(ox, oy, ox + 38, oy - 6, color=RED))
    o.append(T(ox + 44, oy - 9, "e", 8.0, color=RED))
    o.append(T(340, 214, "Induced emf e = d v B", 7.2))
    return _mk(38, o, "Figure 3.38 - Magnetic flowmeter",
               "Lưu lượng kế điện từ: cuộn kích từ và điện cực",
               "Magnetic flowmeter: exciting coils and electrodes on an insulating tube",
               "Sơ đồ lưu lượng kế điện từ với ống đo, cuộn kích từ, cực nam châm, điện cực và bộ ba véctơ V, B, e",
               "Magnetic flowmeter schematic with measuring tube, field coils, flush electrodes and the velocity, flux and emf vector triad")


# ---------------------------------------------------------------- 3.39
@_reg
def fig_f39():
    """Turbine flowmeter: bladed rotor, flow tube and magnetic pickup."""
    o = [_defs()]
    o.append(_rect(120, 92, 440, 66, "#fbfaf7", sw=1.2))
    o.append(_rect(120, 86, 14, 78, "#e9e3d6", sw=1.0))
    o.append(_rect(546, 86, 14, 78, "#e9e3d6", sw=1.0))
    cx, cy = 340, 125
    o.append(_circle(cx, cy, 42, fill="none", sw=0.8, color=GREY, dash="3,3"))
    o.append(_line(160, cy, 520, cy, sw=1.3, color=GREY))
    for k in range(6):
        a = math.radians(k * 60)
        p = []
        for r, off in ((12, -6), (40, -11), (40, 11), (12, 6)):
            p.append((cx + r * math.cos(a) - off * math.sin(a),
                      cy + r * math.sin(a) + off * math.cos(a)))
        o.append(_poly(p, fill="#dfe6ef", sw=1.0, close=True))
    o.append(_circle(cx, cy, 11, fill="#eef3fb", sw=1.1))
    o.append(_ar(155, 110, 225, 110, color=BLUE))
    o.append(T(165, 100, "Flow", 7.0, color=BLUE))
    o.append(_ar(455, 140, 525, 140, color=BLUE))
    o.append(_ar(362, 100, 380, 110, color=GREEN, sw=1.0))
    # pickup coil under the rotor
    o.append(_rect(322, 158, 36, 16, "#f4f6fa", sw=1.1))
    for i in range(4):
        o.append(_line(327 + i * 8, 160, 327 + i * 8, 172, sw=0.8, color=GREY))
    o.append(_ar(340, 188, 340, 176, color=GREY))
    o.append(T(340, 197, "Magnetic pickup coil", 7.0))
    o.append(_ar(360, 164, 432, 170, color=RED))
    o.append(T(480, 173, "Pulse output", 7.0, color=RED))
    o.append(T(250, 54, "Turbine blades", 7.2, weight="bold"))
    o.append(_ar(272, 58, 315, 96, color=GREY))
    o.append(T(160, 190, "Flow tube", 7.0))
    o.append(_ar(198, 186, 198, 160, color=GREY))
    return _mk(39, o, "Figure 3.39 - Turbine flowmeter",
               "Lưu lượng kế tuabin: cánh quay trong ống dẫn",
               "Turbine flowmeter: a bladed rotor turning inside the flow tube",
               "Sơ đồ lưu lượng kế tuabin với cánh quạt, trục, ống dẫn và cuộn cảm biến phát xung",
               "Turbine flowmeter with the bladed rotor in the flow tube and the magnetic pickup coil generating pulses")


# ---------------------------------------------------------------- 3.40
@_reg
def fig_f40():
    """Turbine meter K-factor curves: cycles, output voltage and d.p."""
    o = [_defs()]
    fr, mx, my = _frame(90, 50, 360, 140, (0, 100), (0, 150),
                        [(0, "0"), (50, "50"), (100, "100")],
                        [(0, "0"), (50, "50"), (100, "100"), (150, "150")],
                        "Percent flow", "Output")
    volt = [(0, 0), (8, 60), (18, 92), (30, 110), (45, 119),
            (60, 124), (80, 128), (100, 130)]
    dp = [(i, 115.0 * (i / 100.0) ** 2) for i in range(0, 101, 10)]
    o.append(_series(volt, mx, my, GREEN, dot=1.4))
    o.append(_series(dp, mx, my, BLUE, dot=1.4))
    o.append(_line(mx(0), my(132), mx(100), my(132),
                   sw=1.5, color=RED, dash="5,3"))
    o.append(_line(mx(0), my(100), mx(100), my(100),
                   sw=0.7, color=GREY, dash="3,3"))
    o.append(T(478, 72, "Cycles per gallon", 7.0))
    o.append(_ar(474, 75, mx(96), my(132), color=GREY))
    o.append(T(478, 100, "Voltage and frequency", 7.0, color=GREEN))
    o.append(_ar(474, 103, mx(70), my(126), color=GREEN))
    o.append(T(478, 150, "Differential pressure", 7.0, color=BLUE))
    o.append(T(478, 159, "across the meter", 7.0, color=BLUE))
    o.append(_ar(474, 153, mx(86), my(85), color=BLUE))
    return _mk(40, o, "Figure 3.40 - Turbine meter K-factor curve",
               "Đường cong hệ số K của lưu lượng kế tuabin",
               "Turbine meter K-factor: cycles, voltage and pressure drop against flow",
               "Đồ thị hệ số K: số chu kỳ trên gallon, điện áp tần số và chênh áp theo phần trăm lưu lượng",
               "K-factor curves of cycles per gallon, voltage and frequency, and differential pressure versus percent flow")


# ---------------------------------------------------------------- 3.41
@_reg
def fig_f41():
    """Target flowmeter with integral force-balance pneumatic transmitter."""
    o = [_defs()]
    o.append(_rect(60, 45, 250, 125, "#fbfaf7", sw=1.2))
    # pneumatic supply chain inside the transmitter
    o.append(_ar(60, 58, 96, 58, color=GREY))
    o.append(T(68, 50, "Air", 7.0))
    o.append(_rect(100, 52, 28, 12, "#e9e3d6", sw=0.9))
    o.append(T(160, 56, "Restrictor", 7.0))
    o.append(_ar(155, 56, 130, 58, color=GREY))
    o.append(_rect(100, 80, 28, 20, "#f4f6fa", sw=0.9))
    o.append(T(160, 90, "Relay", 7.0))
    o.append(_ar(155, 90, 130, 90, color=GREY))
    o.append(_line(190, 62, 206, 74, sw=1.2))
    o.append(_rect(206, 68, 10, 8, "#e9e3d6", sw=0.9))
    o.append(T(235, 66, "Flapper nozzle", 7.0))
    o.append(_ar(230, 68, 218, 72, color=GREY))
    o.append(_circle(190, 110, 10, fill="#f4f6fa", sw=1.0))
    o.append(T(235, 108, "Range wheel", 7.0))
    o.append(_ar(230, 110, 202, 110, color=GREY))
    o.append(_rect(100, 130, 30, 18, "#f4f6fa", sw=0.9))
    for i in range(5):
        o.append(_line(104 + i * 6, 131, 104 + i * 6, 147, sw=0.7, color=GREY))
    o.append(T(160, 145, "Feed back bellows", 7.0))
    o.append(_ar(155, 142, 132, 139, color=GREY))
    o.append(_circle(190, 150, 6, fill="#ffffff", sw=1.0))
    o.append(_line(185, 150, 195, 150, sw=0.8))
    o.append(T(235, 150, "Zero adjust", 7.0))
    o.append(_ar(230, 150, 198, 150, color=GREY))
    o.append(_ar(95, 155, 60, 155, color=BLUE))
    o.append(T(95, 180, "Output signal", 7.0))
    o.append(_ar(92, 176, 88, 157, color=GREY))
    # target in the pipeline and the force bar
    o.append(_rect(330, 178, 320, 30, "#eef3fb", sw=1.2))
    o.append(_rect(330, 172, 12, 42, "#e9e3d6", sw=1.0))
    o.append(_rect(638, 172, 12, 42, "#e9e3d6", sw=1.0))
    o.append(_poly([(480, 178), (480, 105), (300, 105)], sw=1.5, color=INK))
    o.append(_circle(480, 172, 5, fill="#ffffff", sw=1.0))
    o.append(_rect(476, 179, 8, 28, "#cfd8e3", sw=1.1))
    o.append(_ar(560, 193, 620, 193, color=BLUE))
    o.append(T(590, 170, "Flow", 7.0, color=BLUE))
    o.append(T(400, 96, "Force bar", 7.0))
    o.append(_ar(405, 99, 440, 105, color=GREY))
    o.append(T(520, 160, "Seal", 7.0))
    o.append(_ar(516, 160, 486, 169, color=GREY))
    o.append(T(520, 224, "Target", 7.0))
    o.append(_ar(516, 220, 485, 200, color=GREY))
    return _mk(41, o, "Figure 3.41 - Target flowmeter force balance",
               "Lưu lượng kế mục tiêu với bộ cân bằng lực",
               "Target flowmeter: disc target and force-balance transmitter",
               "Sơ đồ lưu lượng kế mục tiêu: đĩa cản trong ống, thanh lực, bánh răng chỉnh dải, vòi phản lực và ống khí nén",
               "Target flowmeter showing the disc in the pipe, force bar, range wheel, flapper nozzle, relay and feedback bellows")


# ---------------------------------------------------------------- 3.42
@_reg
def fig_f42():
    """Drag-type target flowmeter with a strain gage force arm."""
    o = [_defs()]
    o.append(_rect(140, 100, 400, 84, "#eef3fb", sw=1.2))
    o.append(_rect(134, 92, 12, 100, "#e9e3d6", sw=1.0))
    o.append(_rect(534, 92, 12, 100, "#e9e3d6", sw=1.0))
    o.append(_ar(165, 142, 245, 142, color=BLUE))
    o.append(T(170, 88, "Flow", 7.0, color=BLUE))
    o.append(_rect(352, 140, 8, 44, "#cfd8e3", sw=1.1))
    o.append(_line(356, 140, 356, 62, sw=1.4))
    o.append(_rect(326, 44, 60, 22, "#f4f6fa", sw=1.1))
    o.append(T(356, 59, "Strain gage", 6.6))
    o.append(T(450, 58, "Strain gage transducer", 7.0))
    o.append(_ar(444, 58, 388, 55, color=GREY))
    o.append(T(420, 100, "Force arm", 7.0))
    o.append(_ar(414, 100, 360, 100, color=GREY))
    o.append(T(420, 170, "Target", 7.0))
    o.append(_ar(414, 167, 363, 160, color=GREY))
    return _mk(42, o, "Figure 3.42 - Drag type target flowmeter",
               "Lưu lượng kế mục tiêu kiểu cản: cảm biến biến dạng",
               "Drag type flowmeter: target on a strain gage force arm",
               "Sơ đồ lưu lượng kế kiểu cản với đĩa mục tiêu, cần lực và đầu đo biến dạng gắn trên ống",
               "Drag type flowmeter with the target disc carried by a force arm and a strain gage transducer mounted on the pipe")


# ---------------------------------------------------------------- 3.43
@_reg
def fig_f43():
    """Annubar averaging sensor with inlet ports and rear port."""
    o = [_defs()]
    o.append(_rect(110, 112, 380, 92, "#eef3fb", sw=1.2))
    for yy in (126, 148, 170, 192):
        o.append(_ar(140, yy, 205, yy, color=BLUE, sw=1.1))
    o.append(_path("M 215,114 C 250,140 250,176 215,202",
                   sw=1.0, color=GREY, dash="4,3"))
    o.append(_rect(326, 113, 10, 88, "#dfe6ef", sw=1.1))
    for yy in (128, 148, 168, 188):
        o.append(_rect(320, yy - 3, 7, 6, "#ffffff", sw=0.9))
    o.append(_rect(334, 160, 8, 6, "#ffffff", sw=0.9))
    o.append(_rect(310, 50, 44, 28, "#f4f6fa", sw=1.1))
    o.append(_poly([(310, 56), (294, 44), (294, 40)], sw=1.0, color=GREY))
    o.append(_poly([(354, 56), (370, 44), (370, 40)], sw=1.0, color=GREY))
    o.append(_rect(325, 78, 14, 35, "#e9e3d6", sw=1.0))
    o.append(T(430, 48, "Head available here", 7.0))
    o.append(_ar(424, 50, 362, 56, color=GREY))
    o.append(T(250, 88, "Sensor", 7.0))
    o.append(_ar(256, 92, 322, 114, color=GREY))
    o.append(T(250, 108, "Tube", 7.0))
    o.append(_ar(272, 110, 328, 136, color=GREY))
    o.append(T(180, 132, "Inlet port", 7.0))
    o.append(_ar(220, 130, 318, 128, color=GREY))
    o.append(T(410, 205, "Rear port", 7.0))
    o.append(_ar(406, 201, 344, 165, color=GREY))
    return _mk(43, o, "Figure 3.43 - Annubar sensor",
               "Đầu đo Annubar: cảm biến áp suất xung lực trung bình",
               "Annubar: averaging impact-pressure sensor in a pipeline",
               "Sơ đồ đầu đo Annubar với ống cảm biến, các cổng vào phía thượng lưu, cổng sau và đầu nối áp suất",
               "Annubar schematic showing the sensor tube, averaged inlet ports facing the flow, the rear port and the instrument head")


# ---------------------------------------------------------------- 3.44
@_reg
def fig_f44():
    """Vortex flowmeter: bluff-body shredder and Karman vortex street."""
    o = [_defs()]
    for y in (68, 182):
        o.append(_line(80, y, 620, y, sw=1.4))
        s = -1 if y < 100 else 1
        for x in range(90, 621, 14):
            o.append(_line(x, y, x + 6, y + 6 * s, sw=0.5, color=GREY))
    o.append(_poly([(218, 120), (250, 112), (250, 164), (218, 156)],
                   fill="#dfe6ef", sw=1.2, close=True))
    o.append(_ar(206, 120, 206, 156, color=GREY))
    o.append(T(198, 140, "D", 8.0, anchor="end"))
    o.append(_ar(105, 140, 200, 140, color=BLUE))
    o.append(T(105, 128, "Flow", 7.0, color=BLUE))
    for x, y in ((300, 122), (360, 158), (420, 122), (480, 158), (540, 122)):
        o.append(_circle(x, y, 9, fill="none", sw=1.2, color=BLUE))
        o.append(_ar(x, y + 3, x + 5, y - 2, color=BLUE, sw=0.9))
    o.append(T(240, 205, "Vortex shredder", 7.0))
    o.append(_ar(238, 201, 235, 166, color=GREY))
    o.append(T(520, 200, "Karman vortex", 7.0))
    o.append(_ar(514, 197, 486, 166, color=GREY))
    return _mk(44, o, "Figure 3.44 - Vortex flowmeter",
               "Lưu lượng kế xoáy: vật cản và dãy xoáy Karman",
               "Vortex flowmeter: bluff body and Karman vortex street",
               "Sơ đồ lưu lượng kế xoáy với vật cản hình thang, dòng chảy và dãy xoáy Karman phía sau",
               "Vortex flowmeter with a trapezoidal bluff body, the oncoming flow and the alternating Karman vortex street")


# ---------------------------------------------------------------- 3.45
@_reg
def fig_f45():
    """Strouhal geometry: bluff-body width D and vortex interval L."""
    o = [_defs()]
    for y in (62, 190):
        o.append(_line(80, y, 620, y, sw=1.4))
        s = -1 if y < 100 else 1
        for x in range(90, 621, 14):
            o.append(_line(x, y, x + 6, y + 6 * s, sw=0.5, color=GREY))
    o.append(_poly([(150, 100), (196, 100), (196, 156), (150, 156)],
                   fill="#dfe6ef", sw=1.2, close=True))
    o.append(_ar(138, 100, 138, 156, color=GREY))
    o.append(T(130, 130, "D", 8.0, anchor="end"))
    for x, y in ((260, 110), (340, 110), (420, 110),
                 (300, 150), (380, 150), (460, 150)):
        o.append(_circle(x, y, 8, fill="none", sw=1.1, color=BLUE))
        o.append(_ar(x, y + 2, x + 4, y - 3, color=BLUE, sw=0.8))
    o.append(_ar(302, 178, 378, 178, color=GREY))
    o.append(T(340, 195, "L", 8.0))
    o.append(T(250, 84, "Bluff body width D", 7.0))
    o.append(_ar(245, 88, 198, 104, color=GREY))
    o.append(T(540, 110, "St = L / D", 8.0, weight="bold"))
    o.append(T(450, 212, "Vortex interval L", 7.0, color=GREY))
    return _mk(45, o, "Figure 3.45 - Strouhal number geometry",
               "Hình học hệ số Strouhal: chiều rộng D và khoảng cách xoáy L",
               "Strouhal geometry: bluff-body width D and vortex spacing L",
               "Sơ đồ xác định hệ số Strouhal với chiều rộng vật cản D và khoảng cách giữa hai xoáy liên tiếp L",
               "Definition of the Strouhal number showing the bluff-body width D and the vortex spacing L")


# ---------------------------------------------------------------- 3.46
@_reg
def fig_f46():
    """Strouhal number versus Reynolds number: measurable and normal ranges."""
    o = [_defs()]
    fr, mx, my = _frame(95, 55, 380, 128, (3.5, 7.1), (0, 0.32),
                        [(math.log10(5e3), "5x10³"),
                         (math.log10(2e4), "2x10⁴"),
                         (math.log10(7e6), "7x10⁶")],
                        [(0, "0"), (0.1, "0.1"), (0.2, "0.2"), (0.3, "0.3")],
                        "Reynolds number Rd", "St")
    pts = [(3.70, 0.215), (3.85, 0.205), (4.05, 0.19), (4.30, 0.18),
           (5.0, 0.18), (6.0, 0.18), (6.845, 0.18)]
    o.append(_series(pts, mx, my, BLUE, dot=1.6))
    o.append(_line(mx(4.30), my(0.18), mx(7.0), my(0.18),
                   sw=1.0, color=GREEN, dash="5,3"))
    for v in (3.70, 4.30, 6.845):
        o.append(_line(mx(v), my(0), mx(v), my(0.30),
                       sw=0.8, color=GREY, dash="3,3"))
    x1, x2 = mx(3.70), mx(6.845)
    o.append(_line(x1, 40, x2, 40, sw=1.0, color=GREY))
    o.append(_line(x1, 36, x1, 44, sw=1.0, color=GREY))
    o.append(_line(x2, 36, x2, 44, sw=1.0, color=GREY))
    o.append(T((x1 + x2) / 2.0, 33, "Measurable range", 7.5, weight="bold"))
    o.append(T(mx(5.6), 84, "Normal operating range", 7.0, color=GREEN))
    o.append(_ar(mx(5.6), 88, mx(5.6), my(0.18) + 3, color=GREEN))
    return _mk(46, o, "Figure 3.46 - Strouhal number range",
               "Miền giá trị của hệ số Strouhal theo số Reynolds",
               "Strouhal number against Reynolds number and operating ranges",
               "Đồ thị hệ số Strouhal theo số Reynolds với miền đo được và miền làm việc thông thường",
               "Strouhal number versus Reynolds number on a log scale, with the measurable and normal operating ranges marked")


# ---------------------------------------------------------------- 3.47
@_reg
def fig_f47():
    """Coriolis mass flowmeter: vibrating flow-tube assembly and detectors."""
    o = [_defs()]
    o.append(_rect(150, 78, 390, 118, fill="none", sw=0.9, dash="4,3",
                   stroke=GREY))
    o.append(_path("M 170,96 L 470,96 C 520,96 520,156 470,156 L 170,156",
                   sw=2.0, color=BLUE))
    o.append(_path("M 170,108 L 458,108 C 500,108 500,144 458,144 L 170,144",
                   sw=2.0, color=GREEN))
    o.append(_rect(96, 112, 18, 28, "#e9e3d6", sw=1.0))
    o.append(_rect(96, 108, 6, 36, "#ffffff", sw=1.0))
    o.append(_line(114, 126, 170, 126, sw=1.0))
    o.append(_ar(60, 112, 110, 112, color=BLUE))
    o.append(T(60, 103, "Inlet", 7.0, color=BLUE))
    o.append(_ar(110, 140, 60, 140, color=BLUE))
    o.append(T(60, 158, "Outlet", 7.0, color=BLUE))
    o.append(_rect(310, 56, 44, 22, "#f4f6fa", sw=1.1))
    for i in range(5):
        o.append(_line(316 + i * 8, 58, 316 + i * 8, 76, sw=0.7, color=GREY))
    o.append(T(332, 50, "Drive coil", 7.0, weight="bold"))
    o.append(_ar(332, 79, 332, 92, color=GREY))
    o.append(_rect(250, 158, 24, 14, "#f4f6fa", sw=1.0))
    o.append(_rect(360, 158, 24, 14, "#f4f6fa", sw=1.0))
    o.append(T(317, 184, "Position detectors", 7.0))
    o.append(_ar(300, 180, 274, 172, color=GREY))
    o.append(_ar(345, 180, 372, 172, color=GREY))
    o.append(_ar(440, 88, 450, 80, color=RED, sw=1.0))
    o.append(T(480, 88, "Coriolis twist", 7.0, color=RED))
    o.append(_ar(476, 86, 452, 82, color=RED))
    o.append(T(560, 68, "Sensor housing", 7.0, color=GREY))
    o.append(_ar(556, 70, 538, 80, color=GREY))
    o.append(T(250, 208, "Vibrating flow tubes", 7.0))
    o.append(_ar(260, 204, 240, 158, color=GREY))
    return _mk(47, o, "Figure 3.47 - Coriolis flow tube assembly",
               "Cụm ống đo của lưu lượng kế khối lượng Coriolis",
               "Coriolis mass flowmeter: vibrating tube assembly inside the sensor",
               "Sơ đồ cụm ống đo rung của lưu lượng kế khối lượng Coriolis với cuộn dẫn động, đầu dò vị trí và momen xoắn",
               "Coriolis mass flowmeter sensor showing the twin vibrating tubes, drive coil, position detectors and induced twist")


# ---------------------------------------------------------------- 3.48
@_reg
def fig_f48():
    """Oval-gear positive displacement meter, three rotor positions."""
    o = [_defs()]
    for j, cx in enumerate((150, 340, 530)):
        o.append(_circle(cx, 120, 60, fill="#eef3fb", sw=1.2))
        a = math.radians(20 + j * 35)
        o.append(_poly(_oval(cx - 22, 120, 22, 34, a),
                       fill="#cfd8e3", sw=1.0, close=True))
        o.append(_poly(_oval(cx + 22, 120, 22, 34, -a),
                       fill="#cfd8e3", sw=1.0, close=True))
        o.append(T(cx, 203, "(%s)" % "abc"[j], 7.5, color=GREY))
    o.append(_ar(55, 120, 88, 120, color=BLUE))
    o.append(T(60, 108, "Flow in", 7.0, color=BLUE))
    o.append(_ar(595, 120, 628, 120, color=BLUE))
    o.append(T(625, 108, "Flow out", 7.0, color=BLUE, anchor="end"))
    o.append(T(340, 40, "Oval-gear positive displacement meter", 8.0, weight="bold"))
    o.append(T(230, 62, "Housing", 7.0))
    o.append(_ar(232, 66, 205, 76, color=GREY))
    o.append(T(450, 205, "Oval rotors", 7.0, color=GREY))
    o.append(_ar(448, 201, 545, 148, color=GREY))
    return _mk(48, o, "Figure 3.48 - Oval-gear meter",
               "Lưu lượng kế thể tích bánh răng ô van",
               "Oval-gear positive displacement meter in three rotor positions",
               "Sơ đồ ba vị trí quay của cặp bánh răng ô van trong buồng đo, chiều vào và chiều ra của dòng chất lỏng",
               "Three positions of the meshing oval-gear rotors in a positive displacement meter, with flow in and flow out")


# ---------------------------------------------------------------- 3.49
@_reg
def fig_f49():
    """Open-channel weirs: V-notch and rectangular notch plates."""
    o = [_defs()]
    o.append(_poly([(70, 72), (148, 72), (180, 122), (212, 72),
                    (290, 72), (290, 185), (70, 185)],
                   fill="#eef3fb", sw=1.2, close=True))
    o.append(T(180, 50, "Angle of notch", 7.5))
    o.append(_ar(180, 56, 180, 112, color=GREY))
    o.append(T(180, 205, "(a) V-notch weir", 7.5))
    o.append(_poly([(390, 72), (458, 72), (458, 120), (542, 120),
                    (542, 72), (610, 72), (610, 185), (390, 185)],
                   fill="#eef3fb", sw=1.2, close=True))
    o.append(_ar(414, 66, 456, 66, color=GREY))
    o.append(T(435, 60, "A", 7.0))
    o.append(_ar(544, 66, 586, 66, color=GREY))
    o.append(T(565, 60, "B", 7.0))
    o.append(_ar(462, 102, 538, 102, color=GREY))
    o.append(T(500, 97, "x = crest length", 6.6))
    o.append(_ar(500, 124, 500, 180, color=GREY))
    o.append(T(508, 155, "C", 7.0))
    o.append(T(500, 205, "(b) Rectangular notch", 7.5))
    o.append(T(340, 220, "A and B = end contractions; C = bottom contraction",
               6.4, color=GREY))
    return _mk(49, o, "Figure 3.49 - V-notch and rectangular weirs",
               "Đập đo lưu lượng dạng chữ V và dạng chữ nhật",
               "Open-channel weirs: V-notch and rectangular notch",
               "Sơ đồ đập chữ V với góc cắt và đập chữ nhật với chiều dài đỉnh x, co ngang A, B và co đáy C",
               "V-notch and rectangular notch weir plates with the notch angle, crest length x and end and bottom contractions")


# ---------------------------------------------------------------- 3.50
@_reg
def fig_f50():
    """Cippoletti weir with 4:1 end contractions."""
    o = [_defs()]
    o.append(_poly([(150, 70), (262, 70), (280, 138), (400, 138),
                    (418, 70), (530, 70), (530, 195), (150, 195)],
                   fill="#eef3fb", sw=1.2, close=True))
    o.append(T(340, 34, "Cippoletti weir, 4 to 1 end contractions",
               8.0, weight="bold"))
    o.append(_ar(245, 72, 245, 136, color=GREY))
    o.append(T(237, 105, "4", 7.5, anchor="end"))
    o.append(_ar(263, 62, 279, 62, color=GREY))
    o.append(T(271, 55, "1", 7.5))
    o.append(T(470, 150, "Crest", 7.2))
    o.append(_ar(464, 147, 404, 139, color=GREY))
    o.append(T(340, 215, "Trapezoidal notch plate", 7.0, color=GREY))
    return _mk(50, o, "Figure 3.50 - Cippoletti weir",
               "Đập Cippoletti với co ngang tỉ lệ 4 trên 1",
               "Cippoletti weir with 4 to 1 end contractions",
               "Sơ đồ đập Cippoletti có thành cắt dốc 4 đứng trên 1 ngang và đỉnh đập nằm ngang",
               "Cippoletti weir plate showing the 4 to 1 side slopes of the notch and the horizontal crest")


# ---------------------------------------------------------------- 3.51
@_reg
def fig_f51():
    """Water profile over a weir: head, drawdown, nappe and aeration."""
    o = [_defs()]
    o.append(_line(70, 202, 620, 202, sw=1.4))
    o.append(_rect(70, 78, 260, 124, "#dbe7f2", sw=0))
    for yy in range(84, 200, 8):
        o.append(_line(76, yy, 326, yy, sw=0.5, color=BLUE))
    o.append(_path("M 70,78 C 100,74 130,82 160,78 C 190,74 220,82 "
                   "250,78 C 280,74 310,82 330,78", sw=1.0, color=BLUE))
    o.append(_poly([(330, 202), (330, 120), (344, 120), (344, 202)],
                   fill="#e9e3d6", sw=1.2, close=True))
    o.append(_rect(360, 172, 260, 30, "#dbe7f2", sw=0))
    for yy in range(178, 201, 7):
        o.append(_line(366, yy, 616, yy, sw=0.5, color=BLUE))
    o.append(_path("M 344,120 C 390,122 420,145 460,170",
                   sw=1.6, color=BLUE))
    o.append(_path("M 344,126 C 386,130 414,152 448,172",
                   sw=1.0, color=BLUE))
    o.append(_ar(368, 162, 390, 152, color=GREEN, sw=1.0))
    o.append(T(470, 160, "Aeration", 7.0, color=GREEN))
    o.append(_ar(464, 157, 400, 152, color=GREEN))
    o.append(_ar(300, 80, 300, 118, color=GREY))
    o.append(T(292, 102, "H", 8.0, anchor="end"))
    o.append(T(240, 66, "Draw down", 7.0))
    o.append(_ar(276, 70, 318, 80, color=GREY))
    o.append(T(500, 130, "Nappe", 7.0))
    o.append(_ar(494, 127, 430, 145, color=BLUE))
    o.append(T(345, 218, "Weir", 7.0, color=GREY))
    return _mk(51, o, "Figure 3.51 - Nappe over a weir",
               "Dòng nước qua đập: chiều cao H và vùng thông khí",
               "Water profile over a weir: head H, nappe and aeration",
               "Sơ đồ mặt cắt dòng nước qua đập với chiều cao H, độ hạ thấp, dòng nước nappe và vùng thông khí",
               "Side view of flow over a weir showing the measured head H, drawdown, aerated nappe and downstream level")


# ---------------------------------------------------------------- 3.52
@_reg
def fig_f52():
    """Parshall flume plan: converging, throat and diverging sections."""
    o = [_defs()]
    o.append(_path("M 100,72 L 285,72 C 315,72 330,112 350,112 "
                   "L 390,112 C 415,112 435,72 465,72 L 580,72", sw=1.6))
    o.append(_path("M 100,188 L 285,188 C 315,188 330,148 350,148 "
                   "L 390,148 C 415,148 435,188 465,188 L 580,188", sw=1.6))
    o.append(_line(100, 72, 100, 188, sw=1.4))
    o.append(_line(580, 72, 580, 188, sw=1.4))
    o.append(_ar(55, 130, 98, 130, color=BLUE))
    o.append(T(55, 118, "Flow", 7.0, color=BLUE))
    o.append(_ar(582, 130, 625, 130, color=BLUE))
    o.append(T(200, 130, "Converging", 7.2))
    o.append(T(370, 130, "Throat", 7.2))
    o.append(T(505, 130, "Diverging", 7.2))
    o.append(_line(300, 72, 300, 52, sw=1.0))
    o.append(_line(294, 52, 306, 52, sw=1.2))
    o.append(T(300, 46, "H", 7.5))
    o.append(_line(400, 112, 400, 92, sw=1.0))
    o.append(_line(394, 92, 406, 92, sw=1.2))
    o.append(T(400, 86, "H", 7.5))
    o.append(_ar(412, 114, 412, 146, color=GREY))
    o.append(T(420, 133, "L", 7.5))
    o.append(T(340, 28, "Parshall flume: plan view of the channel",
               8.0, weight="bold"))
    return _mk(52, o, "Figure 3.52 - Parshall flume",
               "Máng Parshall: đoạn hội tụ, cổ hẹp và đoạn phân kỳ",
               "Parshall flume: converging, throat and diverging sections",
               "Sơ đồ mặt bằng máng Parshall với đoạn hội tụ, cổ hẹp rộng L, đoạn phân kỳ và hai vị trí đo đầu nước H",
               "Plan of a Parshall flume with its converging section, throat of width L, diverging section and two head measuring stations")


# ---------------------------------------------------------------- 3.53
@_reg
def fig_f53():
    """Sight or gage glass on open and closed vessels."""
    o = [_defs()]
    # (a) open vessel
    o.append(_poly([(80, 80), (80, 190), (240, 190), (240, 80)],
                   fill="none", sw=1.2))
    o.append(_rect(82, 122, 156, 66, "#dbe7f2", sw=0))
    for yy in range(128, 188, 7):
        o.append(_line(84, yy, 236, yy, sw=0.5, color=BLUE))
    o.append(T(160, 70, "Open vessel", 7.5, weight="bold"))
    o.append(_rect(262, 112, 14, 74, "#eaf3fb", sw=1.1))
    o.append(_rect(263, 122, 12, 62, "#dbe7f2", sw=0))
    o.append(_line(240, 186, 249, 186, sw=1.0))
    o.append(_circle(253, 186, 4, fill="#ffffff", sw=1.0))
    o.append(_line(257, 186, 262, 186, sw=1.0))
    o.append(_rect(286, 112, 14, 74, "#ffffff", sw=1.0))
    for yy in range(116, 186, 8):
        o.append(_line(286, yy, 294, yy, sw=0.6))
    o.append(T(310, 120, "Indicator", 7.0))
    o.append(T(310, 129, "scale", 7.0))
    o.append(_ar(306, 124, 302, 142, color=GREY))
    o.append(T(310, 182, "Isolation", 7.0))
    o.append(T(310, 191, "valve", 7.0))
    o.append(_ar(306, 186, 260, 186, color=GREY))
    o.append(T(170, 210, "(a)", 7.5, color=GREY))
    # (b) closed vessel
    o.append(_rect(400, 80, 140, 110, fill="none", sw=1.2))
    o.append(_rect(402, 130, 136, 58, "#dbe7f2", sw=0))
    for yy in range(136, 188, 7):
        o.append(_line(404, yy, 536, yy, sw=0.5, color=BLUE))
    o.append(T(470, 70, "Closed vessel", 7.5, weight="bold"))
    o.append(_line(540, 95, 558, 95, sw=1.0))
    o.append(_circle(548, 95, 4, fill="#ffffff", sw=1.0))
    o.append(_line(558, 95, 558, 118, sw=1.0))
    o.append(_rect(558, 118, 14, 68, "#eaf3fb", sw=1.1))
    o.append(_rect(559, 128, 12, 56, "#dbe7f2", sw=0))
    o.append(_line(540, 180, 558, 180, sw=1.0))
    o.append(_circle(548, 180, 4, fill="#ffffff", sw=1.0))
    o.append(_rect(582, 118, 14, 68, "#ffffff", sw=1.0))
    for yy in range(122, 186, 8):
        o.append(_line(582, yy, 590, yy, sw=0.6))
    o.append(T(620, 130, "Indicator", 7.0))
    o.append(T(620, 139, "scale", 7.0))
    o.append(_ar(616, 134, 598, 150, color=GREY))
    o.append(T(470, 210, "(b)", 7.5, color=GREY))
    return _mk(53, o, "Figure 3.53 - Sight or gage glass",
               "Ống thủy tinh chỉ mức cho bình hở và bình kín",
               "Sight glass level indicator on open and closed vessels",
               "Sơ đồ ống thủy tinh chỉ mức đấu với bình hở và bình kín, có thang chỉ thị và van cô lập",
               "Sight glass level indicators connected to an open vessel and a closed vessel, with scale and isolation valves")


# ---------------------------------------------------------------- 3.54
@_reg
def fig_f54():
    """Reflex gage glass assembly with the boiler drum connections."""
    o = [_defs()]
    o.append(_path("M 132,52 L 208,52 Q 230,52 230,74 L 230,176 "
                   "Q 230,198 208,198 L 132,198 Q 110,198 110,176 "
                   "L 110,74 Q 110,52 132,52 Z", fill="#f4f6fa", sw=1.3))
    o.append(_rect(160, 66, 20, 118, "#dbe7f2", sw=1.1))
    for yy in (84, 102, 120, 138, 156):
        o.append(_line(160, yy, 180, yy, sw=0.6, color=BLUE))
    o.append(_line(160, 132, 180, 132, sw=1.4, color=BLUE))
    for yy in (78, 98, 118, 138, 158, 178):
        o.append(_circle(137, yy, 4.2, fill="#ffffff", sw=0.9))
        o.append(_circle(203, yy, 4.2, fill="#ffffff", sw=0.9))
    o.append(_path("M 140,52 C 140,38 200,38 200,52", sw=1.2))
    o.append(_path("M 140,198 C 140,212 200,212 200,198", sw=1.2))
    o.append(T(300, 62, "U-Bolt", 7.2))
    o.append(_ar(294, 60, 206, 48, color=GREY))
    o.append(T(300, 100, "Tempered Glass", 7.2))
    o.append(_ar(294, 98, 184, 92, color=GREY))
    o.append(T(300, 140, "Gage glass", 7.2))
    o.append(_ar(294, 138, 182, 132, color=GREY))
    # drum connections and remote indication
    o.append(_path("M 420,80 C 400,100 400,160 420,180", sw=1.3))
    o.append(T(440, 92, "Steam", 7.0))
    o.append(_ar(436, 90, 422, 98, color=GREY))
    o.append(T(440, 156, "BFW", 7.0))
    o.append(_ar(434, 154, 414, 152, color=GREY))
    o.append(_rect(470, 100, 18, 80, "#e9e3d6", sw=1.0))
    o.append(_hatchv(470, 100, 18, 80, step=8))
    o.append(T(520, 108, "Insulated", 7.0))
    o.append(T(520, 117, "chamber", 7.0))
    o.append(_ar(514, 112, 490, 120, color=GREY))
    o.append(_rect(530, 122, 14, 42, "#dbe7f2", sw=1.1))
    o.append(T(600, 138, "Remote gage", 7.0))
    o.append(_ar(594, 136, 546, 140, color=GREY))
    o.append(_line(537, 164, 537, 184, sw=1.0))
    o.append(_circle(537, 184, 4, fill="#ffffff", sw=1.0))
    o.append(T(570, 194, "Drain", 7.0))
    o.append(_ar(566, 191, 541, 184, color=GREY))
    o.append(T(340, 28, "Reflex gage glass level indicator",
               8.0, weight="bold"))
    return _mk(54, o, "Figure 3.54 - Gage glass level indicator",
               "Kính chỉ mức dạng phản xạ cho lò hơi",
               "Reflex gage glass boiler level indicator",
               "Sơ đồ kính chỉ mức cường lực có bulông chữ U và sơ đồ đấu nối hơi, nước cấp, buồng cách nhiệt và van xả",
               "Reflex gage glass assembly with tempered glass and U-bolts, plus boiler drum connections for steam, feed water, insulated chamber and drain")
