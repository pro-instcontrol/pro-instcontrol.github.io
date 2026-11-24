# -*- coding: utf-8 -*-
"""Vector figures 2.41-2.58 for IPC Chapter 2 "Transducers - II".

Registered through ``ipcfig2_common.make_registry()``; every label passes
through ``T()`` and every drawing stays inside the 680 x 250 viewBox.
"""
from ipcfig2_common import (make_registry, T, _b, _ar, _frame, _series,
                            _legend, _wavey, _mk, _defs, _line, _circle,
                            _rect, _ellipse, _path, _poly, BLUE, GREEN, GREY, INK, RED)
FIGS, _reg = make_registry()


@_reg
def fig_f41():
    """Fig. 2.41 - Moving-coil velocity transducer."""
    o = [_defs()]
    dark = "#3a3a3a"
    o.append(_rect(232, 168, 220, 16, fill=dark, sw=0))
    o.append(_rect(232, 88, 16, 96, fill=dark, sw=0))
    o.append(_rect(436, 88, 16, 96, fill=dark, sw=0))
    o.append(_rect(332, 100, 16, 84, fill=dark, sw=0))
    o.append(_rect(324, 96, 32, 10, fill=dark, sw=0))
    for cx in (282, 398):
        o.append(_rect(cx - 11, 104, 22, 58, fill="#eef3fb"))
        o.append(_rect(cx - 6, 110, 12, 46, fill="#ffffff"))
        for dy in (6, 16, 26, 36, 46):
            o.append(_circle(cx - 8.5, 110 + dy, 1.5, fill=BLUE, sw=0))
            o.append(_circle(cx + 8.5, 110 + dy, 1.5, fill=BLUE, sw=0))
    o.append(_line(288, 84, 392, 84, sw=1.0, color=GREY))
    o.append(_ar(296, 84, 344, 84, color=RED, sw=1.3))
    o.append(_ar(384, 84, 336, 84, color=RED, sw=1.3))
    o.append(T(340, 74, "E", 8.6, color=RED))
    o.append(T(214, 98, "coil", 7.6, anchor="end"))
    o.append(_line(218, 96, 270, 116, sw=0.9, color=GREY))
    o.append(T(340, 202, "Magnet", 7.6))
    o.append(_line(340, 194, 340, 186, sw=0.9, color=GREY))
    return _mk(41, o, "Figure 2.41 - Moving-coil velocity transducer",
               "Bộ chuyển đổi vận tốc kiểu cuộn dây di động: cuộn dây gắn vào thiết bị chuyển động trong khe hở của nam châm, suất điện động tỉ lệ với vận tốc.",
               "Moving-coil velocity transducer: a coil attached to the moving equipment cuts the permanent-magnet field in the air gap, so the induced emf is proportional to velocity.",
               "Cuộn dây di động trong khe hở nam châm có mũi tên điện áp E",
               "Moving coil in a magnet gap with an emf arrow E")


@_reg
def fig_f42():
    """Fig. 2.42 - Single-degree-of-freedom seismic system."""
    o = [_defs()]
    o.append(_rect(232, 178, 216, 14, fill="url(#h6)"))
    o.append(_rect(240, 56, 12, 122, fill="url(#h6)"))
    o.append(_rect(428, 56, 12, 122, fill="url(#h6)"))
    o.append(_rect(240, 56, 200, 10, fill="url(#h6)"))
    o.append(T(254, 50, "Case", 7.2, anchor="start", color=GREY))
    o.append(_line(260, 51, 252, 58, sw=0.8, color=GREY))
    o.append(_rect(310, 100, 60, 34, fill="#eef3fb"))
    o.append(T(340, 113, "Mass", 7.4))
    o.append(T(340, 126, "m", 8.4))
    o.append(_ar(340, 96, 340, 72, color=RED, sw=1.2))
    o.append(T(352, 80, "m d2x/dt2", 7.0, anchor="start", color=RED))
    sp = [(318 + (6 if i % 2 else -6), 136 + i * 5) for i in range(9)]
    o.append(_poly(sp, sw=1.6, color=BLUE))
    o.append(_line(318, 134, 318, 136, sw=1.0))
    o.append(_line(318, 176, 318, 178, sw=1.0))
    o.append(T(304, 168, "Ks x", 7.0, anchor="end", color=BLUE))
    o.append(_line(362, 134, 362, 148, sw=1.4))
    o.append(_rect(354, 148, 16, 18, fill="#ffffff"))
    o.append(_line(362, 166, 362, 178, sw=1.4))
    o.append(T(378, 164, "Kd dx/dt", 7.0, anchor="start", color=BLUE))
    o.append(_ar(394, 134, 394, 102, color=GREY, sw=1.0))
    o.append(T(402, 120, "x", 7.4, anchor="start"))
    o.append(_ar(470, 176, 470, 192, color=GREY, sw=1.0))
    o.append(T(478, 190, "y", 7.4, anchor="start"))
    o.append(T(340, 206, "Moving object", 7.4, color=GREY))
    o.append(_line(340, 198, 340, 194, sw=0.8, color=GREY))
    return _mk(42, o, "Figure 2.42 - Seismic spring-mass system",
               "Hệ khối lượng - lò xo - bộ giảm chấn một bậc tự do: khối m chỉ dịch chuyển theo một trục, lò xo Ks và giảm chấn Kd nối khối với vỏ đặt trên vật chuyển động.",
               "Single-degree-of-freedom seismic spring-mass system: mass m moves along one axis, with spring Ks and dashpot Kd joining it to a case mounted on the moving object.",
               "Khối m giữa lò xo Ks và giảm chấn Kd trong vỏ trên nền chuyển động",
               "Mass m between spring Ks and dashpot Kd inside a case on a moving base")


@_reg
def fig_f43():
    """Fig. 2.43 - D.C. generator tachometer."""
    o = [_defs()]
    o.append(_rect(258, 94, 32, 30, fill="#eef3fb"))
    o.append(T(274, 114, "N", 9.0, color=BLUE))
    o.append(_rect(390, 94, 32, 30, fill="#eef3fb"))
    o.append(T(406, 114, "S", 9.0, color=RED))
    o.append(_circle(340, 109, 34, fill="#ffffff"))
    o.append(_circle(340, 109, 26, fill="#fbfaf7"))
    o.append(_rect(334, 71, 12, 9, fill=GREY))
    o.append(_rect(334, 138, 12, 9, fill=GREY))
    o.append(_line(340, 71, 340, 58, sw=1.2))
    o.append(_line(340, 58, 470, 58, sw=1.2))
    o.append(_line(470, 58, 470, 160, sw=1.2))
    o.append(_line(340, 147, 340, 160, sw=1.2))
    o.append(_line(340, 160, 470, 160, sw=1.2))
    o.append(_line(462, 64, 462, 154, sw=1.0, color=RED))
    o.append(_ar(458, 72, 462, 64, color=RED, sw=1.0))
    o.append(_ar(458, 146, 462, 154, color=RED, sw=1.0))
    o.append(T(478, 112, "E", 8.6, color=RED))
    o.append(_ar(302, 152, 290, 134, color=GREEN, sw=1.2))
    o.append(T(276, 164, "Armature", 7.6, anchor="end"))
    o.append(_line(280, 160, 316, 134, sw=0.9, color=GREY))
    return _mk(43, o, "Figure 2.43 - D.C. generator tachometer",
               "Máy phát tốc độ một chiều: phần ứng quay trong từ trường nam châm vĩnh cửu sinh ra suất điện động một chiều tỉ lệ với tốc độ, đo bằng voltmet PMMC.",
               "D.C. generator tachometer: an armature revolving in a permanent-magnet field generates a d.c. emf proportional to speed, read on a PMMC voltmeter.",
               "Phần ứng quay giữa cực N và S có điện áp một chiều E",
               "Armature rotating between N and S poles with a d.c. output E")


@_reg
def fig_f44():
    """Fig. 2.44 - A.C. generator tachometer with bridge and RC filter."""
    o = [_defs()]
    o.append(_circle(120, 100, 26, fill="#ffffff"))
    o.append(_path("M105,100 q7,-11 15,0 t15,0", sw=1.4, color=BLUE))
    o.append(_ar(104, 64, 118, 56, color=GREEN, sw=1.2))
    o.append(T(100, 58, "Rotation", 7.2, anchor="end", color=GREEN))
    o.append(_line(120, 74, 120, 44, sw=1.2))
    o.append(_line(120, 44, 300, 44, sw=1.2))
    o.append(_line(300, 44, 300, 60, sw=1.2))
    o.append(_line(120, 126, 120, 166, sw=1.2))
    o.append(_line(120, 166, 300, 166, sw=1.2))
    o.append(_line(300, 166, 300, 150, sw=1.2))
    o.append(_poly([(246, 105), (300, 60), (354, 105), (300, 150)],
                   close=True, sw=0.8, color=GREY))
    o.append(_ar(252, 100, 292, 66, sw=1.1))
    o.append(_ar(252, 110, 292, 144, sw=1.1))
    o.append(_ar(306, 66, 348, 100, sw=1.1))
    o.append(_ar(306, 144, 348, 110, sw=1.1))
    o.append(_line(354, 105, 520, 105, sw=1.2))
    o.append(_line(246, 105, 246, 185, sw=1.2))
    o.append(_line(246, 185, 438, 185, sw=1.2))
    o.append(_line(410, 105, 410, 140, sw=1.2))
    o.append(_line(398, 140, 422, 140, sw=1.6))
    o.append(_line(398, 148, 422, 148, sw=1.6))
    o.append(_line(410, 148, 410, 185, sw=1.2))
    o.append(T(428, 146, "C", 7.6, anchor="start"))
    rz = [(438, 185), (443, 179), (448, 191), (453, 179),
          (458, 191), (463, 179), (468, 185)]
    o.append(_poly(rz, sw=1.3))
    o.append(T(453, 175, "R", 7.6))
    o.append(_line(468, 185, 520, 185, sw=1.2))
    o.append(_circle(520, 145, 16, fill="#ffffff"))
    o.append(T(520, 149, "V", 8.6))
    o.append(_line(520, 105, 520, 129, sw=1.2))
    o.append(_line(520, 161, 520, 185, sw=1.2))
    o.append(T(550, 141, "PMMC", 7.2, anchor="start"))
    o.append(T(550, 151, "indicator", 7.2, anchor="start"))
    return _mk(44, o, "Figure 2.44 - A.C. generator tachometer",
               "Máy phát tốc độ xoay chiều: rotor quay sinh điện áp xoay chiều qua mạch chỉnh lưu cầu và bộ lọc RC tới đồng hồ PMMC hiệu chỉnh theo tốc độ.",
               "A.C. generator tachometer: a revolving rotor induces an a.c. voltage that is bridge-rectified and RC-filtered before driving a PMMC speed indicator.",
               "Máy phát xoay chiều, cầu chỉnh lưu, bộ lọc RC và đồng hồ V",
               "A.C. generator, diode bridge, RC filter and a V meter")


@_reg
def fig_f45():
    """Fig. 2.45 - Industrial speed measurement system."""
    o = [_defs()]
    o.append(_rect(70, 100, 120, 12, fill="#eef3fb"))
    o.append(_ar(88, 92, 76, 76, color=GREEN, sw=1.2))
    o.append(T(70, 70, "Rotation", 7.0, anchor="end", color=GREEN))
    o.append(_rect(100, 86, 22, 14, fill="#eef3fb"))
    o.append(T(111, 96, "N", 6.6))
    o.append(_rect(122, 86, 22, 14, fill="#eef3fb"))
    o.append(T(133, 96, "S", 6.6))
    o.append(_rect(158, 88, 20, 24, fill="#ffffff"))
    o.append(T(168, 82, "pick-up coil", 6.8))
    o.append(_line(168, 112, 168, 150, sw=1.2))
    o.append(_line(168, 150, 215, 150, sw=1.2))
    o.append(_b(215, 136, 64, 28, "pulse\nshaper", size=6.8))
    o.append(_line(279, 150, 300, 150, sw=1.2))
    o.append(_rect(300, 116, 96, 68, fill="#fffdf7"))
    o.append(T(348, 110, "C max = 1uF", 7.0))
    o.append(_line(320, 132, 320, 166, sw=1.4))
    o.append(_line(320, 140, 336, 132, sw=1.2))
    o.append(_line(320, 150, 336, 158, sw=1.2))
    o.append(_line(338, 130, 338, 142, sw=1.6))
    o.append(_line(344, 130, 344, 142, sw=1.6))
    o.append(_line(396, 150, 440, 150, sw=1.2))
    o.append(_circle(470, 150, 16, fill="#ffffff"))
    o.append(_line(470, 150, 480, 140, sw=1.2, color=RED))
    o.append(_line(440, 150, 454, 150, sw=1.2))
    o.append(T(470, 180, "RPM", 7.2))
    o.append(T(470, 189, "indicator", 7.2))
    o.append(_line(420, 150, 420, 204, sw=1.1))
    o.append(_line(420, 204, 440, 204, sw=1.1))
    o.append(_b(440, 190, 152, 28, "For Trip / Alarm circuits", size=7.0))
    o.append(T(244, 178, "shielded cable", 6.6, color=GREY))
    return _mk(45, o, "Figure 2.45 - Industrial speed measurement system",
               "Hệ đo tốc độ công nghiệp: nam châm quay cùng trục sinh sóng sin trong cuộn thu, mạch điện tử đổi thành xung nạp tụ C max = 1 uF và đồng hồ RPM, có đầu ra báo động.",
               "Industrial speed measurement system: a shaft magnet induces a sine wave in a pickup coil; electronics convert it into charging pulses for C max = 1 uF and an RPM meter, with trip/alarm outputs.",
               "Nam châm quay, cuộn thu, mạch tụ C va đồng hồ RPM",
               "Rotating magnet, pickup coil, capacitor circuit and RPM meter")


@_reg
def fig_f46():
    """Fig. 2.46 - High-speed measurement system."""
    o = [_defs()]
    dirs = [(1, 0), (0.87, 0.5), (0.5, 0.87), (0, 1),
            (-0.5, 0.87), (-0.87, 0.5), (-1, 0), (-0.87, -0.5),
            (-0.5, -0.87), (0, -1), (0.5, -0.87), (0.87, -0.5)]
    o.append(_circle(100, 120, 34, fill="#ffffff"))
    for dx, dy in dirs:
        o.append(_line(100 + 34 * dx, 120 + 34 * dy,
                       100 + 42 * dx, 120 + 42 * dy, sw=3.0))
    o.append(_circle(100, 120, 7, fill="#ffffff"))
    o.append(T(100, 184, "Pole wheel", 7.4))
    o.append(_rect(170, 84, 124, 72, fill="#ffffff"))
    o.append(_rect(182, 104, 20, 14, fill="#eef3fb"))
    o.append(T(192, 114, "N", 6.6))
    o.append(_rect(202, 104, 20, 14, fill="#eef3fb"))
    o.append(T(212, 114, "S", 6.6))
    o.append(_line(186, 98, 186, 92, sw=1.2))
    o.append(_line(194, 98, 194, 92, sw=1.2))
    o.append(_line(202, 98, 202, 92, sw=1.2))
    o.append(_line(210, 98, 210, 92, sw=1.2))
    o.append(T(230, 112, "220", 7.0, anchor="start"))
    o.append(T(230, 132, "10V", 7.0, anchor="start"))
    o.append(_line(262, 96, 262, 104, sw=1.2))
    o.append(_line(254, 96, 270, 96, sw=1.6))
    o.append(_line(254, 104, 270, 104, sw=1.6))
    o.append(_line(294, 120, 324, 120, sw=1.2))
    o.append(_b(324, 104, 78, 32, "Converter", size=7.4))
    o.append(_line(402, 120, 416, 120, sw=1.2))
    o.append(_ar(416, 120, 432, 104, sw=1.3))
    o.append(_ar(416, 120, 432, 158, sw=1.3))
    o.append(_b(432, 86, 122, 36, "Speed\nindicator", size=7.4))
    o.append(_b(432, 140, 132, 36, "Trip / Alarm\nsystem", size=7.4))
    return _mk(46, o, "Figure 2.46 - High-speed measurement system",
               "Hệ đo tốc độ cao: bánh cực quay trước bộ phát ferostat, tín hiệu qua bộ chuyển đổi tới chỉ thị tốc độ và hệ thống trip/alarm; điện áp tỉ lệ nghịch với khe hở d0.",
               "High-speed measurement system: a pole wheel revolving before a ferrostate transmitter feeds a converter, speed indicator and trip/alarm system; the voltage varies with the gap d0.",
               "Bánh cực, bộ phát 220 ohm 10V, bộ đổi và chỉ thị tốc độ",
               "Pole wheel, 220 ohm 10V transmitter, converter and speed indicator")


@_reg
def fig_f47():
    """Fig. 2.47 - Transmitted voltage versus gap distance."""
    o = [_defs()]
    fr, mx, my = _frame(112, 30, 430, 150, (0, 3.1), (0, 720),
                        [(0.1, "0.1"), (0.4, "0.4"), (0.5, "0.5"),
                         (1.0, "1.0"), (1.5, "1.5"), (2.0, "2.0"),
                         (2.5, "2.5"), (3.0, "3.0")],
                        [(100, "100"), (200, "200"), (300, "300"),
                         (400, "400"), (500, "500"), (600, "600"),
                         (700, "700")],
                        "d_o (mm)", "V_o (mV)")
    o.append(fr)
    pts = [(0.1, 700), (0.15, 640), (0.2, 600), (0.3, 545),
           (0.4, 500), (0.5, 460), (0.7, 390), (1.0, 315),
           (1.3, 265), (1.6, 225), (2.0, 180), (2.5, 145), (3.0, 120)]
    o.append(_series(pts, mx, my, BLUE, dot=0))
    o.append(_line(mx(0.4), my(0), mx(0.4), my(500),
                   sw=0.9, color=RED, dash="4 4"))
    o.append(_line(mx(0.4), my(500), mx(1.0), my(500),
                   sw=0.8, color=GREY, dash="4 4"))
    o.append(T(mx(1.05), my(520), "usual d_o = 0.4 mm",
               6.8, anchor="start", color=RED))
    return _mk(47, o, "Figure 2.47 - Output voltage versus gap distance",
               "Đồ thị điện áp đầu ra V_o theo khe hở d_o: điện áp giảm nhanh khi khe hở tăng; giá trị d_o thường dùng ban đầu là 0,4 mm.",
               "Output voltage V_o versus gap distance d_o: the voltage falls rapidly as the gap widens; the usual initial value of d0 is 0.4 millimetre.",
               "Đường cong điện áp giảm theo khe hở với mốc 0,4 mm",
               "Curve of voltage falling with gap, marked at 0.4 mm")


@_reg
def fig_f48():
    """Fig. 2.48 - Stroboscope (strobometer) outer view."""
    o = [_defs()]
    o.append(_rect(152, 76, 148, 28, fill="#f1f1ee"))
    o.append(_path("M300,62 C370,42 470,44 496,72 C516,96 506,150 474,168 L300,168 Z",
                   fill="#f1f1ee"))
    o.append(_circle(152, 90, 14, fill="#ffffff"))
    o.append(_circle(152, 90, 3.2, fill=GREY))
    o.append(_ar(136, 84, 110, 80, color=BLUE, sw=1.2))
    o.append(_ar(136, 96, 110, 92, color=BLUE, sw=1.2))
    o.append(T(100, 62, "Flashing", 7.4, anchor="end"))
    o.append(T(100, 72, "light out", 7.4, anchor="end"))
    o.append(_line(238, 104, 238, 116, sw=1.8))
    o.append(_circle(238, 117, 2, fill=INK))
    o.append(T(214, 130, "On-off switch", 7.0))
    o.append(_line(232, 117, 226, 124, sw=0.8, color=GREY))
    ticks = [(1, 0), (0.87, 0.5), (0.5, 0.87), (0, 1),
             (-0.5, 0.87), (-0.87, 0.5), (-1, 0), (-0.87, -0.5),
             (-0.5, -0.87), (0, -1), (0.5, -0.87), (0.87, -0.5)]
    o.append(_circle(470, 84, 12, fill="#ffffff"))
    for dx, dy in ticks:
        o.append(_line(470 + 8 * dx, 84 + 8 * dy,
                       470 + 11 * dx, 84 + 11 * dy, sw=0.8))
    o.append(_circle(470, 84, 2.5, fill=INK))
    o.append(T(500, 66, "Scale and manual", 7.2, anchor="start"))
    o.append(T(500, 76, "adjustment knob", 7.2, anchor="start"))
    o.append(_line(483, 83, 496, 78, sw=0.8, color=GREY))
    return _mk(48, o, "Figure 2.48 - Stroboscope outer view",
               "Đèn stroboscope dạng cầm tay: cửa sổ phát sáng ở đầu, công tắc on-off và núm chỉnh cùng thang đo RPM trên thân máy; không tiếp xúc cơ khí với trục.",
               "Handheld stroboscope: a flashing-light window at the muzzle, an on-off switch and a calibrated speed adjustment knob on the body; it makes no mechanical contact with the shaft.",
               "Thân đèn stroboscope có cửa sổ phát sáng và núm chỉnh",
               "Stroboscope body with a flash window and adjustment knob")


@_reg
def fig_f49():
    """Fig. 2.49 - Potentiometric accelerometer."""
    o = [_defs()]
    o.append(_rect(210, 48, 310, 132, fill="#ffffff"))
    o.append(_rect(210, 180, 310, 12, fill="url(#h6)"))
    pot = [(288 + (6 if i % 2 else -6), 68 + i * 7) for i in range(13)]
    o.append(_poly(pot, sw=1.6, color=BLUE))
    o.append(_line(228, 104, 244, 104, sw=1.6))
    o.append(_line(231, 112, 241, 112, sw=1.0))
    o.append(_line(236, 104, 236, 68, sw=1.0))
    o.append(_line(236, 68, 288, 68, sw=1.0))
    o.append(_line(236, 112, 236, 152, sw=1.0))
    o.append(_line(236, 152, 288, 152, sw=1.0))
    o.append(T(220, 110, "Eb", 7.2, anchor="end"))
    o.append(_circle(218, 120, 2.4, fill="#ffffff"))
    o.append(_circle(218, 150, 2.4, fill="#ffffff"))
    o.append(_line(218, 120, 270, 120, sw=1.0))
    o.append(_line(270, 120, 270, 110, sw=1.0))
    o.append(_line(270, 110, 294, 110, sw=1.0))
    o.append(_line(218, 150, 288, 150, sw=1.0))
    o.append(T(206, 140, "eo", 7.2, anchor="end"))
    o.append(_rect(360, 96, 50, 30, fill="#eef3fb"))
    o.append(T(385, 115, "m", 8.4))
    o.append(_ar(360, 110, 296, 110, color=RED, sw=1.2))
    sp = [(385 + (6 if i % 2 else -6), 60 + i * 6) for i in range(6)]
    o.append(_poly(sp, sw=1.5, color=BLUE))
    o.append(T(402, 76, "Ks", 7.4, anchor="start", color=BLUE))
    o.append(_line(385, 126, 385, 140, sw=1.4))
    o.append(_rect(377, 140, 16, 18, fill="#ffffff"))
    o.append(_line(385, 158, 385, 180, sw=1.4))
    o.append(T(402, 156, "Kd", 7.4, anchor="start", color=BLUE))
    o.append(_ar(425, 126, 425, 98, color=GREY, sw=1.0))
    o.append(T(434, 116, "x", 7.4, anchor="start"))
    o.append(_ar(500, 164, 500, 180, color=GREY, sw=1.0))
    o.append(T(508, 178, "y", 7.4, anchor="start"))
    o.append(T(288, 42, "Potentiometer", 7.2))
    o.append(_line(288, 46, 288, 64, sw=0.8, color=GREY))
    return _mk(49, o, "Figure 2.49 - Potentiometric accelerometer",
               "Gia tốc kế điện thế: khối lượng địa chấn nối với cần quét của biến trở; chuyển động tương đối giữa khối và vỏ làm thay đổi điện áp đầu ra eo.",
               "Potentiometric accelerometer: a seismic mass drives the wiper of a potentiometer; its motion relative to the case changes the output voltage eo.",
               "Khối m nối cần quét biến trở giữa lò xo Ks và giảm chấn Kd",
               "Mass m driving a potentiometer wiper between spring Ks and damper Kd")


@_reg
def fig_f50():
    """Fig. 2.50 - Bonded strain-gage accelerometer."""
    o = [_defs()]
    o.append(_rect(210, 52, 310, 112, fill="#ffffff"))
    o.append(_rect(210, 52, 310, 8, fill="url(#h6)"))
    o.append(_rect(210, 52, 8, 112, fill="url(#h6)"))
    o.append(_rect(512, 52, 8, 112, fill="url(#h6)"))
    o.append(_rect(210, 164, 310, 10, fill="url(#h6)"))
    o.append(_poly([(218, 100), (402, 100), (402, 108), (218, 108)],
                   close=True, fill="#eef3fb"))
    o.append(_rect(248, 95, 24, 5, fill=INK))
    o.append(_rect(248, 108, 24, 5, fill=INK))
    o.append(T(226, 70, "Strain", 7.0, anchor="start"))
    o.append(T(226, 78, "gage pair", 7.0, anchor="start"))
    o.append(_line(258, 82, 258, 94, sw=0.8, color=GREY))
    o.append(_rect(402, 94, 48, 22, fill="#eef3fb"))
    o.append(T(426, 109, "m", 8.4))
    o.append(_ar(466, 114, 466, 96, color=GREY, sw=1.0))
    o.append(T(476, 110, "x", 7.4, anchor="start"))
    o.append(_line(218, 150, 426, 150, sw=1.0))
    o.append(_line(218, 145, 218, 155, sw=1.0))
    o.append(_line(426, 145, 426, 155, sw=1.0))
    o.append(T(322, 146, "L", 8.0))
    return _mk(50, o, "Figure 2.50 - Bonded strain-gage accelerometer",
               "Gia tốc kế dùng cặp strain gage dán trên dầm công-xôn: biến dạng do khối m dao động tỉ lệ với gia tốc và được đo qua đầu ra strain gage.",
               "Bonded strain-gage accelerometer: a gage pair on a cantilever senses the strain caused by the vibrating mass m, proportional to acceleration.",
               "Dầm công-xôn có cặp strain gage ở đầu cố định và khối m",
               "Cantilever with a strain-gage pair at the root and mass m")


@_reg
def fig_f51():
    """Fig. 2.51 - Strain-gage accelerometer with solid support."""
    o = [_defs()]
    o.append(_rect(220, 48, 260, 124, fill="#ffffff"))
    o.append(_rect(220, 48, 260, 8, fill="url(#h6)"))
    o.append(_rect(220, 48, 8, 124, fill="url(#h6)"))
    o.append(_rect(472, 48, 8, 124, fill="url(#h6)"))
    o.append(_rect(220, 172, 260, 10, fill="url(#h6)"))
    o.append(_rect(320, 70, 48, 24, fill="#eef3fb"))
    o.append(T(344, 86, "m", 8.4))
    for sx in (326, 344, 362):
        o.append(_rect(sx, 94, 6, 56, fill="#e9e3d6"))
        o.append(_rect(sx - 2, 112, 10, 4, fill=INK))
        o.append(_rect(sx - 2, 132, 10, 4, fill=INK))
    o.append(_ar(386, 92, 386, 72, color=GREY, sw=1.0))
    o.append(T(396, 86, "x", 7.4, anchor="start"))
    o.append(_ar(500, 156, 500, 172, color=GREY, sw=1.0))
    o.append(T(508, 168, "y", 7.4, anchor="start"))
    o.append(T(196, 104, "Set of bonded", 7.0, anchor="end"))
    o.append(T(196, 112, "strain gage", 7.0, anchor="end"))
    o.append(_line(200, 110, 320, 120, sw=0.8, color=GREY))
    o.append(T(500, 124, "Solid support", 7.0, anchor="start"))
    o.append(_line(496, 120, 372, 128, sw=0.8, color=GREY))
    return _mk(51, o, "Figure 2.51 - Solid-support strain-gage accelerometer",
               "Gia tốc kế strain gage có giá đỡ rắn cho khối lượng địa chấn; giá đỡ vừa tạo lò xo và giảm chấn, vừa chứa bộ strain gage đo biến dạng.",
               "Strain-gage accelerometer with a solid support for the seismic mass; the support supplies both spring and damping action and hosts the bonded gages.",
               "Khối m trên giá đỡ rắn có bộ strain gage dán",
               "Mass m on a solid support carrying bonded strain gages")


@_reg
def fig_f52():
    """Fig. 2.52 - LVDT accelerometer."""
    o = [_defs()]
    o.append(_rect(210, 48, 270, 124, fill="#ffffff"))
    o.append(_rect(210, 172, 270, 10, fill="url(#h6)"))
    o.append(_rect(286, 64, 34, 14, fill="#eef3fb"))
    o.append(_rect(370, 64, 34, 14, fill="#eef3fb"))
    for cx in (292, 300, 308, 376, 384, 392):
        o.append(_line(cx, 65, cx, 77, sw=0.9, color=BLUE))
    o.append(_line(320, 71, 370, 71, sw=1.0))
    o.append(_ar(350, 54, 320, 54, color=BLUE, sw=1.0))
    o.append(_ar(354, 54, 384, 54, color=BLUE, sw=1.0))
    o.append(T(352, 46, "eo", 7.4))
    o.append(_rect(300, 100, 80, 24, fill="#eef3fb"))
    o.append(T(340, 116, "Core", 8.0))
    o.append(_line(215, 112, 300, 112, sw=2.0, color=GREY))
    o.append(_line(380, 112, 475, 112, sw=2.0, color=GREY))
    o.append(_poly([(222 + (5 if i % 2 else -5), 96 + i * 6)
                    for i in range(7)], sw=1.4, color=BLUE))
    o.append(_poly([(468 + (5 if i % 2 else -5), 96 + i * 6)
                    for i in range(7)], sw=1.4, color=BLUE))
    o.append(T(252, 104, "Rod", 7.0, anchor="start"))
    o.append(T(442, 104, "Rod", 7.0, anchor="end"))
    o.append(T(226, 142, "Reed", 7.0, anchor="start"))
    o.append(T(462, 142, "Reed", 7.0, anchor="end"))
    o.append(_line(340, 124, 340, 140, sw=1.2))
    o.append(_line(330, 140, 350, 140, sw=1.6))
    o.append(_line(334, 147, 346, 147, sw=1.0))
    o.append(_line(340, 147, 340, 172, sw=1.2))
    o.append(T(358, 146, "Es", 7.2, anchor="start"))
    o.append(T(252, 166, "A.C. Supply", 7.0, anchor="middle"))
    return _mk(52, o, "Figure 2.52 - LVDT accelerometer",
               "Gia tốc kế LVDT: lõi cảm biến đồng thời là khối lượng địa chấn, được giữ bằng thanh và lá đàn hồi; đầu ra eo tỉ lệ với biên độ dao động.",
               "LVDT accelerometer: the transducer core is the seismic mass, held by rods and reeds that also provide spring action; the output eo is proportional to vibration amplitude.",
               "Lõi LVDT làm khối lượng địa chấn giữa thanh và lá đàn hồi",
               "LVDT core as seismic mass between rods and reeds")


@_reg
def fig_f53():
    """Fig. 2.53 - Piezoelectric accelerometer."""
    o = [_defs()]
    o.append(_rect(258, 48, 164, 124, fill="#ffffff"))
    o.append(_rect(258, 48, 164, 8, fill="url(#h6)"))
    o.append(_rect(258, 48, 8, 124, fill="url(#h6)"))
    o.append(_rect(414, 48, 8, 124, fill="url(#h6)"))
    o.append(_rect(258, 172, 164, 10, fill="url(#h6)"))
    o.append(_poly([(344 + (7 if i % 2 else -7), 56 + i * 6)
                    for i in range(6)], sw=1.5, color=BLUE))
    o.append(_line(344, 86, 344, 92, sw=1.2))
    o.append(_rect(326, 92, 36, 22, fill="#eef3fb"))
    o.append(T(344, 107, "m", 8.4))
    o.append(_rect(326, 132, 36, 18, fill="#eef3fb"))
    for gy in (136, 140, 144):
        o.append(_line(328, gy, 360, gy, sw=0.8, color=BLUE))
    o.append(_rect(340, 150, 8, 22, fill="#e9e3d6"))
    o.append(_line(362, 141, 400, 141, sw=1.2))
    o.append(_circle(402, 141, 2.4, fill="#ffffff"))
    o.append(T(410, 145, "eo", 7.6, anchor="start"))
    o.append(_ar(382, 114, 382, 94, color=GREY, sw=1.0))
    o.append(T(392, 108, "x", 7.4, anchor="start"))
    o.append(T(198, 64, "Heavy", 7.0, anchor="end"))
    o.append(T(198, 72, "spring", 7.0, anchor="end"))
    o.append(_line(202, 70, 336, 66, sw=0.8, color=GREY))
    o.append(T(196, 132, "Piezoelectric", 7.0, anchor="end"))
    o.append(T(196, 140, "crystal", 7.0, anchor="end"))
    o.append(_line(200, 138, 322, 140, sw=0.8, color=GREY))
    return _mk(53, o, "Figure 2.53 - Piezoelectric accelerometer",
               "Gia tốc kế áp điện: tinh thể áp điện đặt dưới khối lượng địa chấn và tựa vào lò xo nặng; ứng suất do gia tốc sinh điện áp eo không cần nguồn phụ.",
               "Piezoelectric accelerometer: a force-sensitive crystal sits under the seismic mass against a heavy spring; acceleration stresses the crystal and produces eo without auxiliary power.",
               "Tinh thể áp điện dưới khối m tựa vào lò xo nặng",
               "Piezoelectric crystal beneath mass m against a heavy spring")


@_reg
def fig_f54():
    """Fig. 2.54 - Stress-type torque meter with slip rings."""
    o = [_defs()]
    o.append(_rect(150, 100, 380, 40, fill="#eef3fb"))
    o.append(_ellipse(150, 120, 10, 20, fill="url(#h6)"))
    o.append(_ellipse(530, 120, 10, 20, fill="url(#h6)"))
    o.append(_line(140, 120, 540, 120, sw=0.8, color=GREY, dash="6 4"))
    o.append(_ar(170, 158, 150, 142, color=GREEN, sw=1.2))
    o.append(T(146, 166, "Rotation", 7.0, anchor="end", color=GREEN))
    for rx, tx in ((226, 206), (248, 238), (270, 282), (292, 314)):
        o.append(_ellipse(rx, 120, 5, 22, sw=1.4))
        o.append(_line(rx, 98, rx, 64, sw=1.0))
        o.append(_line(rx, 64, tx, 64, sw=1.0))
        o.append(_circle(tx, 64, 2.2, fill="#ffffff"))
    o.append(T(220, 54, "Supply", 7.0))
    o.append(T(298, 54, "Output", 7.0))
    for gx, gy, up, col, num, nx, ny in (
            (396, 112, False, RED, "4", 382, 106),
            (466, 112, True, BLUE, "3", 480, 106),
            (396, 128, True, BLUE, "1", 382, 136),
            (466, 128, False, RED, "2", 480, 136)):
        if up:
            o.append(_line(gx - 8, gy + 7, gx + 8, gy - 7, sw=3.0, color=col))
        else:
            o.append(_line(gx - 8, gy - 7, gx + 8, gy + 7, sw=3.0, color=col))
        o.append(T(nx, ny, num, 7.2, color=col))
    o.append(T(430, 80, "Set of bonded strain gage", 7.0))
    o.append(_line(430, 84, 430, 96, sw=0.8, color=GREY))
    o.append(T(248, 178, "Slip ring", 7.0))
    o.append(_line(248, 170, 248, 144, sw=0.8, color=GREY))
    o.append(T(540, 90, "Shaft", 7.2, anchor="start"))
    o.append(_line(536, 94, 520, 104, sw=0.8, color=GREY))
    o.append(T(350, 200, "Stress type torque meter", 6.6, color=GREY))
    return _mk(54, o, "Figure 2.54 - Bonded strain-gage torque meter",
               "Bộ đo mô-men xoắn dạng ứng suất: bốn strain gage dán ở góc ±45 độ trên trục quay, nối qua vòng trượt vào cầu Wheatstone; hai cặp đo biến dạng kéo và nén.",
               "Stress-type torque meter: four strain gages bonded at ±45 degrees on the rotating shaft, connected through slip rings to a Wheatstone bridge; two pairs sense tensile and compressive strain.",
               "Trục quay có bốn strain gage và vòng trượt cấp điện, đầu ra",
               "Rotating shaft with four gages and slip rings for supply and output")


@_reg
def fig_f55():
    """Fig. 2.55 - Electrical torque meter using an A.C. generator detector."""
    o = [_defs()]
    o.append(_rect(150, 64, 380, 14, fill="#eef3fb"))
    o.append(_ellipse(150, 71, 9, 7, fill="url(#h6)"))
    o.append(_ellipse(530, 71, 9, 7, fill="url(#h6)"))
    o.append(_line(145, 71, 535, 71, sw=0.8, color=GREY, dash="6 4"))
    o.append(T(140, 96, "Source side", 7.0, anchor="end"))
    o.append(T(540, 96, "Load side", 7.0, anchor="start"))
    o.append(T(452, 50, "Rotating shaft", 7.0, anchor="start"))
    o.append(_line(470, 54, 470, 62, sw=0.8, color=GREY))
    for gx in (250, 440):
        o.append(_rect(gx - 6, 46, 12, 50, fill="#eef3fb"))
        o.append(_line(gx, 96, gx, 105, sw=1.2))
        o.append(_circle(gx, 116, 11, fill="#ffffff"))
        o.append(_path("M%d,116 q4,-7 8,0 t8,0" % (gx - 8),
                       sw=1.1, color=BLUE))
        o.append(_line(gx, 127, gx, 154, sw=1.0))
        o.append(_poly([(gx - 30 + 6 * i, 160 + (-5 if i % 2 else 5))
                        for i in range(11)], sw=1.3, color=BLUE))
    o.append(T(250, 142, "A.C. generator", 6.6))
    o.append(T(250, 150, "coupled gear system", 6.6))
    o.append(T(440, 142, "A.C. generator", 6.6))
    o.append(T(440, 150, "coupled gear system", 6.6))
    o.append(_line(220, 160, 220, 174, sw=1.0))
    o.append(_line(220, 174, 470, 174, sw=1.0))
    o.append(_line(470, 174, 470, 160, sw=1.0))
    o.append(_line(280, 160, 280, 185, sw=1.0))
    o.append(_line(280, 185, 285, 185, sw=1.0))
    o.append(_line(410, 160, 410, 185, sw=1.0))
    o.append(_line(410, 185, 405, 185, sw=1.0))
    o.append(_poly([(285 + 6 * i, 185 + (-5 if i % 2 else 5))
                    for i in range(21)], sw=1.3, color=BLUE))
    o.append(_line(345, 190, 345, 200, sw=1.0))
    o.append(_b(300, 200, 90, 26, "A.C. Voltmeter", size=7.2))
    return _mk(55, o, "Figure 2.55 - A.C.-generator torque detector",
               "Bộ đo mô-men dùng máy phát xoay chiều: hai bánh răng trên trục truyền động cho hai máy phát cấp nguồn cho cuộn sơ cấp mắc ngược pha; hiệu điện áp cảm ứng ở cuộn thứ cấp tỉ lệ với mô-men.",
               "Electrical torque meter with an a.c.-generator detector: two gears drive generators feeding transformer primaries in phase opposition; the induced secondary voltage is proportional to torque.",
               "Hai máy phát xoay chiều, cuộn sơ cấp ngược pha và voltmet",
               "Two a.c. generators, opposed transformer primaries and a voltmeter")


@_reg
def fig_f56():
    """Fig. 2.56 - Electrical torque meter using proximity sensors."""
    o = [_defs()]
    o.append(_rect(150, 70, 380, 14, fill="#eef3fb"))
    o.append(_ellipse(150, 77, 9, 7, fill="url(#h6)"))
    o.append(_ellipse(530, 77, 9, 7, fill="url(#h6)"))
    o.append(_line(145, 77, 535, 77, sw=0.8, color=GREY, dash="6 4"))
    o.append(T(140, 100, "Source side", 7.0, anchor="end"))
    o.append(T(540, 100, "Load side", 7.0, anchor="start"))
    o.append(T(452, 54, "Rotating shaft", 7.0, anchor="start"))
    o.append(_line(470, 58, 470, 68, sw=0.8, color=GREY))
    for gx in (250, 440):
        o.append(_rect(gx - 6, 48, 12, 56, fill="#eef3fb"))
        o.append(_rect(gx - 6, 96, 12, 5, fill=INK))
        o.append(_line(gx, 104, gx, 120, sw=1.2))
        o.append(_rect(gx - 12, 120, 24, 20, fill="#eef3fb"))
    o.append(T(200, 116, "Gear system", 7.0, anchor="end"))
    o.append(_line(204, 112, 244, 100, sw=0.8, color=GREY))
    o.append(T(480, 116, "Gear system", 7.0, anchor="start"))
    o.append(_line(476, 112, 446, 100, sw=0.8, color=GREY))
    o.append(T(190, 132, "Proximity", 6.8, anchor="end"))
    o.append(T(190, 140, "sensor", 6.8, anchor="end"))
    o.append(_line(194, 134, 238, 130, sw=0.8, color=GREY))
    o.append(T(480, 132, "Proximity", 6.8, anchor="start"))
    o.append(T(480, 140, "sensor", 6.8, anchor="start"))
    o.append(_line(476, 134, 452, 130, sw=0.8, color=GREY))
    o.append(_b(300, 164, 84, 30, "Phase\ndetector", size=7.2))
    o.append(_ar(250, 140, 250, 174, color=BLUE, sw=1.1))
    o.append(_ar(250, 174, 300, 174, color=BLUE, sw=1.1))
    o.append(_ar(440, 140, 440, 174, color=BLUE, sw=1.1))
    o.append(_ar(440, 174, 384, 174, color=BLUE, sw=1.1))
    o.append(_ar(384, 179, 470, 179, color=RED, sw=1.2))
    o.append(T(476, 182, "Output", 7.2, anchor="start", color=RED))
    return _mk(56, o, "Figure 2.56 - Proximity-sensor torque detector",
               "Bộ đo mô-men dùng cảm biến tiệm cận: hai hệ bánh răng trên trục tạo chuỗi xung, bộ phát hiện pha đo lệch pha do tải, tỉ lệ với mô-men.",
               "Electrical torque meter with proximity sensors: two gear systems generate pulse trains, and a phase detector senses the load-induced phase shift proportional to torque.",
               "Hai cảm biến tiệm cận trước bộ phát hiện pha và đầu ra",
               "Two proximity sensors feeding a phase detector and output")


@_reg
def fig_f57():
    """Fig. 2.57 - Optical-sensor torque detector."""
    o = [_defs()]
    o.append(_rect(140, 70, 400, 14, fill="#eef3fb"))
    o.append(_ellipse(140, 77, 9, 7, fill="url(#h6)"))
    o.append(_ellipse(540, 77, 9, 7, fill="url(#h6)"))
    o.append(_line(135, 77, 545, 77, sw=0.8, color=GREY, dash="6 4"))
    o.append(T(130, 100, "Source side", 7.0, anchor="end"))
    o.append(T(548, 100, "Load side", 7.0, anchor="start"))
    offsets = [(0, -40), (0, 40), (-16, -20), (16, -20),
               (-16, 20), (16, 20)]
    for cx in (270, 430):
        o.append(_ellipse(cx, 77, 18, 42, sw=1.2))
        for dx, dy in offsets:
            o.append(_rect(cx + dx - 3, 77 + dy - 2, 6, 4,
                           fill="#ffffff", sw=0.9))
    o.append(T(300, 40, "Slotted disc", 7.0, anchor="start"))
    o.append(_line(296, 44, 286, 48, sw=0.8, color=GREY))
    for cx in (270, 430):
        o.append(_circle(cx - 14, 132, 4, fill="#ffffff"))
        o.append(_circle(cx + 14, 132, 4, fill="#ffffff"))
        o.append(_ar(cx - 8, 132, cx + 8, 132, color=RED, sw=1.0))
        o.append(T(cx - 18, 118, "+Vcc", 6.4, anchor="end"))
        o.append(T(cx + 18, 118, "+Vcc", 6.4, anchor="start"))
        for rx in (cx - 14, cx + 14):
            o.append(_poly([(rx + (4 if i % 2 else -4), 142 + i * 4)
                            for i in range(5)], sw=1.0))
            o.append(_line(rx - 6, 162, rx + 6, 162, sw=1.0))
        o.append(T(cx - 26, 152, "R", 6.6, anchor="end"))
        o.append(T(cx + 26, 152, "R", 6.6, anchor="start"))
    o.append(_b(310, 184, 80, 26, "Phase detector", size=7.0))
    o.append(_ar(256, 158, 256, 178, color=BLUE, sw=1.1))
    o.append(_ar(256, 178, 310, 178, color=BLUE, sw=1.1))
    o.append(_ar(444, 158, 444, 178, color=BLUE, sw=1.1))
    o.append(_ar(444, 178, 390, 178, color=BLUE, sw=1.1))
    o.append(_ar(390, 197, 470, 197, color=RED, sw=1.2))
    o.append(T(476, 200, "Output", 7.0, anchor="start", color=RED))
    return _mk(57, o, "Figure 2.57 - Optical-sensor torque detector",
               "Bộ đo mô-men dùng cảm biến quang: hai đĩa có khe trên trục, cặp LED - quang transistor tạo xung; vi sai truyền sáng giữa hai đĩa qua bộ phát hiện pha cho đầu ra tỉ lệ mô-men.",
               "Optical torque meter: two slotted discs on the shaft with LED-phototransistor pairs generating pulses; the light-propagation difference sensed by a phase detector gives a torque-proportional output.",
               "Hai đĩa có khe, cặp LED va quang transistor, bộ phát hiện pha",
               "Two slotted discs, LED-phototransistor pairs and a phase detector")


@_reg
def fig_f58():
    """Fig. 2.58 - Dynamometer torque meter (belt transmission)."""
    o = [_defs()]
    o.append(_line(330, 20, 330, 220, sw=0.8, color=GREY, dash="5 5"))
    o.append(_circle(330, 78, 50, fill="#ffffff"))
    o.append(_ar(330, 78, 366, 50, color=BLUE, sw=1.2))
    o.append(T(360, 60, "r", 7.6, color=BLUE))
    o.append(_line(280, 78, 280, 148, sw=1.6))
    o.append(_line(380, 78, 380, 148, sw=1.6))
    o.append(_ar(272, 100, 272, 130, color=RED, sw=1.2))
    o.append(T(264, 116, "T1", 7.6, anchor="end", color=RED))
    o.append(_ar(388, 100, 388, 130, color=RED, sw=1.2))
    o.append(T(396, 116, "T2", 7.6, anchor="start", color=RED))
    o.append(_line(250, 148, 470, 148, sw=2.4))
    o.append(_circle(280, 148, 9, fill="#ffffff"))
    o.append(_circle(380, 148, 9, fill="#ffffff"))
    o.append(_poly([(322, 148), (338, 148), (330, 138)],
                   close=True, fill="#e9e3d6"))
    o.append(_rect(320, 158, 20, 6, fill="url(#h6)"))
    o.append(T(330, 134, "A", 7.6))
    o.append(T(280, 134, "C", 7.6))
    o.append(T(380, 134, "B", 7.6))
    o.append(_line(280, 170, 330, 170, sw=1.0))
    o.append(_line(280, 166, 280, 174, sw=1.0))
    o.append(_line(330, 166, 330, 174, sw=1.0))
    o.append(T(305, 166, "l", 8.0))
    o.append(_line(330, 170, 380, 170, sw=1.0))
    o.append(_line(380, 166, 380, 174, sw=1.0))
    o.append(T(355, 166, "l", 8.0))
    o.append(_line(470, 148, 470, 184, sw=1.2))
    o.append(_rect(452, 184, 36, 26, fill="#eef3fb"))
    o.append(T(470, 201, "M", 8.4))
    o.append(_line(330, 212, 470, 212, sw=1.0))
    o.append(_line(330, 208, 330, 216, sw=1.0))
    o.append(_line(470, 208, 470, 216, sw=1.0))
    o.append(T(400, 208, "d_o", 8.0))
    o.append(T(490, 140, "Lever system", 7.2, anchor="start"))
    o.append(_line(486, 142, 466, 148, sw=0.8, color=GREY))
    return _mk(58, o, "Figure 2.58 - Dynamometer torque meter",
               "Bộ đo mô-men động lực kế dùng dây đai: hiệu sức căng T1 và T2 tác dụng lên cần đòn bẩy tựa tại A được cân bằng bởi khối M; mô-men đầu ra suy ra từ (T2 - T1) va r.",
               "Dynamometer torque meter with a belt: the tension difference T1 and T2 acts on a lever pivoted at A and is balanced by mass M; output torque follows from (T2 - T1) and r.",
               "Puli dai, cần đòn bẩy tựa tại A và khối cân bằng M",
               "Belt pulley, lever pivoted at A and the balancing mass M")
