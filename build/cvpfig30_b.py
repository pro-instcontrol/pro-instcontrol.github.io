# -*- coding: utf-8 -*-
"""Vector redraws of Figures 30-3 and 30-4 in Baumann Chapter 30,
*Control Valve Primer*, 5th ed. -- "The Bus System to the Rescue, or What
the Future May Bring".

Figure 30-3 is a dense P&ID-style patent drawing of a distributed
temperature-control loop in which a vortex flow meter and the control valve
perform the primary flow regulation; a compact block diagram below repeats
the signal path.  Figure 30-4 shows an I/P-fed, air-loaded pressure regulator
in cross-section (upper) and the corresponding temperature-control loop
(lower).  Both are genuine labelled SVG schematics with bilingual VI/EN
callouts; no raster images are used.  Architecture mirrors `cvpfig26.py`.
"""
from vfig import (BLUE, GREEN, GREY, INK, PAPER, _arrow, _circle, _defs,
                  _fig, _line, _path, _poly, _rect, _txt, svg)

FIGS = {}


def _reg(f):
    FIGS[f.__name__] = f()
    return f


def esc(s):
    return (str(s).replace("&", "&amp;").replace("<", "&lt;")
            .replace(">", "&gt;").replace('"', "&quot;"))


def T(x, y, s, size=7.0, **kw):
    return _txt(x, y, esc(s), size, **kw)


def _lead(o, x, y, tx, ty, text, size=6.6, color=INK, anchor="end"):
    """A grey leader line plus a bilingual T() label."""
    o.append(_line(x, y, tx, ty, sw=0.8, color=GREY))
    lx = tx - 3 if anchor == "end" else tx + 3
    o.append(T(lx, ty + 2.3, text, size, anchor=anchor, color=color))
    return o


def _tag(o, x, y, n):
    """A small patent-drawing reference numeral."""
    o.append(T(x, y, n, 6.4, color=GREY, weight="600"))


def _bub(o, cx, cy, label, r=11, size=7.2, fill=PAPER):
    """An instrument bubble with a centred letter/tag."""
    o.append(_circle(cx, cy, r, fill=fill, sw=1.0))
    o.append(T(cx, cy + size * 0.36, label, size, weight="600"))


def _ctrl(o, x, y, label="C", w=30, h=24):
    o.append(_rect(x, y, w, h, fill="#eef3fb", sw=1.0))
    o.append(T(x + w / 2.0, y + h / 2.0 + 3, label, 8.4, weight="600"))


def _valve(o, cx, cy, w=26, h=20, color=INK):
    """The conventional two-triangle (bow-tie) valve symbol."""
    o.append(_poly([(cx - w / 2.0, cy - h / 2.0), (cx, cy),
                    (cx - w / 2.0, cy + h / 2.0)],
                   fill=PAPER, sw=1.1, color=color, close=True))
    o.append(_poly([(cx + w / 2.0, cy - h / 2.0), (cx, cy),
                    (cx + w / 2.0, cy + h / 2.0)],
                   fill=PAPER, sw=1.1, color=color, close=True))


def _blk(o, x, y, w, h, vi, en, size=6.9, fill="#eef3fb"):
    """A two-line bilingual block used in the compact block diagram."""
    o.append(_rect(x, y, w, h, fill=fill, sw=1.0))
    o.append(T(x + w / 2.0, y + h / 2.0 - 2, vi, size, weight="600"))
    o.append(T(x + w / 2.0, y + h / 2.0 + 8, en, size - 0.7, color=GREY))


@_reg
def fig_f303():
    """Figure 30-3 -- distributed control loop with a vortex flow meter."""
    w, h = 680, 520
    o = [_defs()]
    o.append(T(340, 18,
               "Hệ thống điều khiển phân tán / Distributed control system — bản vẽ sáng chế / patent drawing",
               9.4, color=INK, weight="600"))

    # ---- Main P&ID drawing ------------------------------------------------
    # Main process line, left to right into the heat-exchanger vessel.
    o.append(_line(18, 205, 530, 205, sw=1.6, color=INK))
    o.append(_arrow(64, 205, 116, 205, sw=1.6, color=GREEN))
    o.append(T(40, 197, "Đầu vào / Inlet", 6.8, color=GREEN))
    _tag(o, 26, 194, "4")

    # Vortex flow meter (7) on the inlet pipe.
    o.append(_rect(94, 193, 22, 24, fill="#dbe8f2", sw=1.1))
    o.append(_line(100, 193, 100, 217, sw=0.8, color=GREY))
    o.append(_line(110, 193, 110, 217, sw=0.8, color=GREY))
    _tag(o, 105, 190, "7")
    _lead(o, 94, 205, 34, 178, "Đồng hồ xoáy / Vortex meter", 6.6, anchor="start")

    # Control valve (5) with piston actuator (6) and E/P converter (11).
    _valve(o, 185, 205, 30, 24)
    _tag(o, 205, 224, "5")
    o.append(_rect(157, 138, 56, 40, fill="#eef3fb", sw=1.2))
    o.append(_poly([(163, 138), (207, 138), (215, 154), (155, 154)],
                   fill="#dbe8f2", sw=1.1, close=True))
    o.append(_line(174, 178, 174, 193, sw=1.6, color=INK))
    o.append(_line(196, 178, 196, 193, sw=1.6, color=INK))
    _tag(o, 219, 148, "6")
    _lead(o, 157, 150, 120, 128, "Bộ truyền động / Actuator", 6.6)
    o.append(_rect(158, 92, 46, 24, fill="url(#h6)", sw=1.1))
    o.append(T(181, 108, "E/P", 8.0, weight="600"))
    _tag(o, 208, 96, "11")
    o.append(_arrow(181, 116, 181, 138, sw=1.2, color=INK))

    # Controller C (8): sensed by the vortex meter, output to the E/P.
    _ctrl(o, 118, 236, "C", 30, 24)
    _tag(o, 152, 234, "8")
    o.append(_line(105, 217, 105, 248, sw=0.9, color=GREY))
    o.append(_line(105, 248, 118, 248, sw=0.9, color=GREY))
    o.append(_line(148, 248, 166, 248, sw=0.9, color=GREY))
    o.append(_line(166, 248, 166, 104, sw=0.9, color=GREY))
    o.append(_line(166, 104, 158, 104, sw=0.9, color=GREY))
    _lead(o, 118, 248, 34, 272, "Bộ điều khiển / Controller", 6.6, anchor="start")

    # Central computer (9).
    o.append(_rect(392, 50, 92, 68, fill="#eef3fb", sw=1.3))
    o.append(T(438, 74, "MÁY TÍNH", 8.2, weight="600"))
    o.append(T(438, 88, "TRUNG TÂM", 8.2, weight="600"))
    o.append(T(438, 104, "Central computer", 6.8, color=GREY))
    _tag(o, 490, 55, "9")
    for yy in (64, 76, 88):
        o.append(_line(484, yy, 492, yy, sw=0.9, color=GREY))

    # Heat-exchanger vessel (3), sectioned shell and internal tube bundle.
    o.append(_path("M 570,120 H 600 Q 640,120 640,158 V 252 Q 640,290 600,290 "
                   "H 570 Q 530,290 530,252 V 158 Q 530,120 570,120 Z",
                   fill=PAPER, sw=1.4))
    o.append(_path("M 532,150 H 638", sw=0.9, color=GREY))
    o.append(_path("M 532,260 H 638", sw=0.9, color=GREY))
    for yy in (174, 196, 218, 240):
        o.append(_line(540, yy, 632, yy, sw=0.7, color=GREY))
    o.append(_line(585, 158, 585, 252, sw=0.9, color=GREY))
    o.append(T(585, 112, "Bình trao đổi nhiệt / Heat exchanger", 7.0))
    _tag(o, 648, 132, "3")
    o.append(_line(505, 205, 530, 205, sw=1.6, color=INK))

    # Temperature transmitter (10a) between the vessel and the computer.
    _bub(o, 470, 140, "T", 11)
    _tag(o, 484, 156, "10a")
    o.append(_line(481, 140, 530, 140, sw=0.9, color=GREY))
    o.append(_line(470, 129, 470, 118, sw=0.9, color=GREY))
    _lead(o, 470, 140, 410, 160, "Cảm biến nhiệt / Temperature sensor", 6.6)

    # Vessel return line feeding the lower bypass loop.
    o.append(_line(530, 270, 400, 270, sw=1.4, color=INK))
    o.append(_line(400, 270, 400, 300, sw=1.4, color=INK))

    # Bypass line with shutoff valves (12), a T tap (10b) and controllers.
    o.append(_line(18, 300, 650, 300, sw=1.6, color=INK))
    o.append(T(340, 316, "Đường tắt / Bypass line", 6.8, color=GREY))
    _valve(o, 130, 300, 20, 16)
    o.append(_line(130, 292, 130, 284, sw=1.0, color=INK))
    o.append(_line(122, 284, 138, 284, sw=1.0, color=INK))
    _tag(o, 130, 280, "12")
    _bub(o, 270, 300, "T", 11)
    _tag(o, 270, 284, "10b")
    _ctrl(o, 330, 278, "C", 30, 24)
    _tag(o, 364, 276, "8")
    o.append(_line(281, 300, 330, 290, sw=0.9, color=GREY))
    o.append(_rect(390, 278, 30, 24, fill="url(#h6)", sw=1.0))
    o.append(_line(360, 290, 390, 290, sw=0.9, color=GREY))
    _valve(o, 520, 300, 20, 16)
    _tag(o, 520, 280, "12")

    # Second controller, driven from the vessel return temperature.
    _ctrl(o, 250, 244, "C", 30, 24)
    o.append(_line(265, 268, 265, 289, sw=0.9, color=GREY))
    o.append(_line(400, 270, 280, 270, sw=0.9, color=GREY))
    o.append(_line(280, 270, 280, 244, sw=0.9, color=GREY))

    # Temperature transmitter (10c) at the lower right.
    _bub(o, 600, 330, "T", 11)
    _tag(o, 614, 334, "10c")
    o.append(_line(600, 290, 600, 319, sw=0.9, color=GREY))
    o.append(_line(600, 319, 600, 300, sw=0.9, color=GREY))

    # Signal risers from the lower controllers into the computer.
    o.append(_line(420, 278, 420, 118, sw=0.9, color=GREY))
    o.append(_line(450, 278, 450, 118, sw=0.9, color=GREY))

    # ---- Compact block diagram --------------------------------------------
    o.append(_line(18, 344, 662, 344, sw=0.7, color=GREY, dash="4,3"))
    o.append(T(340, 356, "Sơ đồ khối tóm tắt / Compact block diagram",
               7.2, color=BLUE, weight="600"))

    _blk(o, 36, 364, 96, 34, "Máy tính trung tâm", "Central computer")
    _tag(o, 40, 361, "9")
    _ctrl(o, 162, 370, "C", 32, 22)
    _tag(o, 166, 367, "8")
    _ctrl(o, 226, 370, "E/P", 42, 22)
    _tag(o, 230, 367, "11")
    o.append(_circle(304, 381, 16, fill="#dbe8f2", sw=1.1))
    o.append(T(304, 380, "V", 8.4, weight="600"))
    o.append(T(304, 391, "5", 6.2, color=GREY))
    _blk(o, 356, 364, 84, 34, "Quá trình", "Process")
    _tag(o, 360, 361, "4")

    for x1, x2 in ((132, 162), (194, 226), (268, 288), (320, 356)):
        o.append(_arrow(x1, 381, x2, 381, sw=1.2, color=INK))

    _blk(o, 226, 436, 94, 28, "Cảm biến lưu lượng", "Flow sensor")
    _tag(o, 230, 433, "7")
    _blk(o, 420, 436, 100, 28, "Cảm biến quá trình", "Process sensor")
    _tag(o, 424, 433, "10a")

    o.append(_line(340, 381, 340, 450, sw=0.9, color=GREY, dash="4,3"))
    o.append(_arrow(340, 450, 320, 450, sw=1.0, color=GREY, dash="4,3"))
    o.append(_arrow(226, 450, 178, 450, sw=1.0, color=INK))
    o.append(_line(178, 450, 178, 392, sw=1.0, color=INK))
    o.append(_line(440, 381, 470, 381, sw=0.9, color=GREY, dash="4,3"))
    o.append(_arrow(470, 381, 470, 436, sw=1.0, color=GREY, dash="4,3"))
    o.append(_line(520, 450, 540, 450, sw=1.0, color=INK))
    o.append(_line(540, 450, 540, 474, sw=1.0, color=INK))
    o.append(_line(540, 474, 84, 474, sw=1.0, color=INK))
    o.append(_arrow(84, 474, 84, 398, sw=1.0, color=INK))

    # Bilingual caption strip inside the drawing.
    o.append(T(340, 488,
               "Hình 30-3 · Hệ thống điều khiển phân tán: van + đồng hồ xoáy trong vòng nhiệt độ",
               6.8, color=INK))
    o.append(T(340, 502,
               "Figure 30-3 · Distributed control: valve + vortex meter in a temperature loop",
               6.8, color=GREY))

    return _fig(svg(w, h, "".join(o),
                    esc("Sơ đồ P&ID hệ thống điều khiển phân tán có đồng hồ lưu lượng xoáy")),
                "Hình 30-3 · Bản vẽ bằng sáng chế (tác giả) của hệ thống điều khiển phân tán, trong đó van kết hợp với đồng hồ lưu lượng kiểu xoáy đảm nhiệm chức năng điều khiển lưu lượng chính trong vòng điều khiển nhiệt độ.",
                "Figure 30-3 · Patent drawing (by the author) of a distributed control system in which the control valve, in combination with a vortex-type flow meter, fulfills the primary flow rate controlling function in a temperature control loop.",
                "Bản vẽ P&ID dày đặc: đường ống chính từ trái qua đồng hồ lưu lượng xoáy số 7 và van có bộ truyền động số 6 do bộ chuyển đổi E/P số 11 điều khiển, máy tính trung tâm số 9 ở trên phải, bình trao đổi nhiệt số 3 với cảm biến nhiệt độ số 10a, đường tắt có các van ngắt số 12 và cảm biến số 10b, cảm biến số 10c ở dưới phải; bên dưới là sơ đồ khối máy tính trung tâm đến bộ điều khiển C, E/P, van và quá trình với phản hồi cảm biến lưu lượng và cảm biến quá trình.",
                "Dense P&ID patent drawing: a main process line from the left through the vortex flow meter 7 and a valve with actuator 6 driven by an E/P converter 11, a central computer 9 at the upper right, a heat-exchanger vessel 3 with temperature sensor 10a, a bypass line with shutoff valves 12 and a temperature tap 10b, and a temperature transmitter 10c at the lower right; below it a compact block diagram runs central computer to C to E/P to valve to process, with flow-sensor and process-sensor feedback paths.")


@_reg
def fig_f304():
    """Figure 30-4 -- air-loaded regulator used as a flow controller."""
    w, h = 680, 500
    o = [_defs()]
    o.append(T(340, 18,
               "Bộ điều áp nạp khí / Air-loaded regulator — điều khiển lưu lượng qua lỗ tiết lưu / flow over an orifice",
               9.4, color=INK, weight="600"))

    # ---- Upper cross-section ----------------------------------------------
    # I/P transducer fed by a pneumatic signal at the left.
    o.append(_path("M 14,152 Q 28,150 40,158", sw=1.1, color=INK))
    o.append(_path("M 14,172 Q 28,174 40,172", sw=1.1, color=INK))
    o.append(_rect(40, 142, 72, 50, fill="#eef3fb", sw=1.2))
    o.append(T(76, 166, "I/P", 9.4, weight="600"))
    o.append(T(76, 182, "Bộ chuyển / Transducer", 6.2, color=GREY))
    o.append(T(76, 134, "Bộ chuyển I/P / I/P transducer", 6.6))
    o.append(_line(112, 167, 140, 167, sw=1.1, color=INK))

    # Diaphragm housing with bolted flanges, diaphragm and adjustable spring.
    o.append(_path("M 178,96 H 362 Q 400,96 400,135 Q 400,174 362,174 "
                   "H 178 Q 140,174 140,135 Q 140,96 178,96 Z",
                   fill="#eef3fb", sw=1.4))
    o.append(_rect(136, 120, 8, 30, fill="url(#h6)", sw=1.0))
    o.append(_rect(400, 120, 8, 30, fill="url(#h6)", sw=1.0))
    o.append(_line(148, 135, 392, 135, sw=5.0, color="#1a1a1a"))
    o.append(_rect(252, 128, 36, 14, fill="#cbd5df", sw=1.0))
    o.append(_path("M 270,128 L 261,121 L 279,114 L 261,107 L 279,100 L 270,96",
                   sw=1.6, color=INK))
    o.append(_line(270, 96, 270, 58, sw=1.4, color=INK))
    o.append(_rect(262, 46, 16, 12, fill="url(#h6)", sw=1.0))
    o.append(_line(252, 52, 288, 52, sw=1.2, color=INK))
    o.append(T(200, 84, "Vỏ màng / Diaphragm housing", 6.8))
    _lead(o, 270, 112, 350, 72, "Lò xo chỉnh / Adjustable spring", 6.6,
          anchor="start")
    _lead(o, 160, 135, 100, 206, "Màng / Diaphragm", 6.6, anchor="start")

    # Stem and valve body set into the horizontal process line.
    o.append(_rect(266, 135, 8, 134, fill="#dfe7f0", sw=1.1))
    _lead(o, 270, 220, 350, 202, "Thân / Stem", 6.6, anchor="start")
    o.append(_rect(236, 256, 64, 14, fill="url(#h6)", sw=1.1))
    o.append(_rect(236, 286, 64, 14, fill="url(#h6)", sw=1.1))
    o.append(_poly([(268, 270), (292, 270), (280, 286), (256, 286)],
                   fill="#dbe8f2", sw=1.1, close=True))
    _lead(o, 236, 282, 180, 252, "Thân van / Valve body", 6.6)

    # Main process line with a fixed orifice (FO) downstream of the valve.
    o.append(_line(24, 278, 656, 278, sw=1.6, color=INK))
    o.append(_arrow(56, 278, 104, 278, sw=1.5, color=GREEN))
    o.append(_arrow(404, 278, 452, 278, sw=1.5, color=GREEN))
    o.append(T(120, 270, "Dòng quá trình / Process flow", 6.8, color=GREEN))
    o.append(_rect(344, 264, 4, 28, fill="url(#h6)", sw=0.9))
    o.append(_rect(372, 264, 4, 28, fill="url(#h6)", sw=0.9))
    o.append(_poly([(348, 268), (348, 288), (358, 278)],
                   fill="#dbe8f2", sw=1.0, close=True))
    o.append(_poly([(372, 268), (372, 288), (362, 278)],
                   fill="#dbe8f2", sw=1.0, close=True))
    o.append(T(360, 256, "FO", 7.6, weight="600"))
    o.append(T(360, 302, "Lỗ cố định / Fixed orifice", 6.6))

    # Pressure gauge and its tubing loop back to the process line.
    o.append(_circle(555, 88, 25, fill=PAPER, sw=1.3))
    o.append(_circle(555, 88, 20, sw=0.8, color=GREY))
    for ang in (-120, -60, 0, 60, 120, 180):
        import math
        ra = math.radians(ang)
        o.append(_line(555 + 15 * math.cos(ra), 88 + 15 * math.sin(ra),
                       555 + 19 * math.cos(ra), 88 + 19 * math.sin(ra),
                       sw=0.8, color=GREY))
    o.append(_line(555, 88, 566, 72, sw=1.3, color=INK))
    o.append(T(555, 50, "Đồng hồ áp suất / Pressure gauge", 6.8))
    o.append(_line(555, 113, 555, 128, sw=1.1, color=INK))
    o.append(_line(555, 128, 608, 128, sw=1.1, color=INK))
    o.append(_line(608, 128, 608, 278, sw=1.1, color=INK))
    o.append(_rect(598, 268, 20, 20, fill="url(#h6)", sw=1.0))

    # Two sensing lines from the valve body up to the diaphragm housing.
    o.append(_path("M 200,174 V 236 H 250 V 256", sw=1.1, color=INK))
    o.append(_path("M 340,174 V 236 H 292 V 256", sw=1.1, color=INK))

    # ---- Lower control-loop diagram ---------------------------------------
    o.append(_line(18, 296, 662, 296, sw=0.7, color=GREY, dash="4,3"))
    o.append(T(340, 310, "Sơ đồ vòng điều khiển / Control-loop diagram",
               7.2, color=BLUE, weight="600"))

    # Dashed instrument-air line from the I/P to the temperature bubbles.
    o.append(_line(100, 324, 470, 324, sw=1.1, color=GREY, dash="5,3"))
    for x in (140, 160, 180):
        o.append(_line(x - 3, 328, x + 3, 320, sw=0.9, color=GREY))

    _bub(o, 100, 344, "I/P", 14, size=7.0)
    o.append(_line(88, 354, 112, 334, sw=1.0, color=INK))
    o.append(_circle(150, 344, 12, fill=PAPER, sw=1.1))
    o.append(_line(138, 344, 162, 344, sw=1.3, color=INK))
    o.append(T(150, 370, "Bộ điều áp / Regulator", 6.2))
    o.append(_line(150, 356, 150, 382, sw=1.1, color=INK))

    _bub(o, 350, 324, "TIC", 14, size=6.6)
    o.append(T(350, 350, "Điều khiển / Controller", 6.2))
    _bub(o, 420, 324, "TE", 14, size=7.0)
    o.append(T(420, 364, "Cảm biến / Sensor", 6.2))

    o.append(_rect(470, 302, 90, 100, fill="#eef3fb", sw=1.2))
    o.append(T(515, 340, "BÌNH TRAO ĐỔI", 7.2, weight="600"))
    o.append(T(515, 353, "NHIỆT", 7.2, weight="600"))
    o.append(T(515, 368, "HEAT EXCHANGER", 6.4, color=GREY))
    for yy in (322, 344):
        o.append(_arrow(560, yy, 594, yy, sw=1.1, color=GREEN))
    o.append(_arrow(594, 388, 560, 388, sw=1.1, color=GREEN))

    o.append(_line(30, 388, 470, 388, sw=1.6, color=INK))
    o.append(_arrow(56, 388, 100, 388, sw=1.4, color=GREEN))
    o.append(T(60, 380, "Hơi / Steam", 6.6, color=GREEN))
    _valve(o, 150, 388, 26, 20)
    o.append(_poly([(260, 378), (260, 398), (268, 388)],
                   fill="#dbe8f2", sw=1.0, close=True))
    o.append(_poly([(280, 378), (280, 398), (272, 388)],
                   fill="#dbe8f2", sw=1.0, close=True))
    o.append(T(270, 374, "FO", 7.4, weight="600"))
    o.append(T(270, 412, "Lỗ tiết lưu / Orifice", 6.4))

    # Bilingual caption strip inside the drawing.
    o.append(T(340, 466,
               "Hình 30-4 · Bộ điều áp nạp khí và lỗ tiết lưu FO trong vòng nhiệt độ",
               6.8, color=INK))
    o.append(T(340, 480,
               "Figure 30-4 · Air-loaded regulator with fixed orifice FO in a temperature loop",
               6.8, color=GREY))

    return _fig(svg(w, h, "".join(o),
                    esc("Sơ đồ cắt bộ điều áp nạp khí và vòng điều khiển nhiệt độ với lỗ tiết lưu")),
                "Hình 30-4 · Bộ điều áp nạp khí đóng vai trò bộ điều khiển lưu lượng phối hợp với lỗ tiết lưu cố định hoặc thay đổi (FO) như một phần của vòng điều khiển nhiệt độ.",
                "Figure 30-4 · Air-loaded regulator serves as a flow controller in conjunction with a fixed or variable orifice (FO) as part of a temperature control loop.",
                "Nửa trên là sơ đồ cắt bộ điều áp có vỏ màng bắt bulông, lò xo chỉnh, màng, thân và thân van, hộp chuyển I/P ở bên trái dẫn khí vào vỏ màng, lỗ tiết lưu cố định FO trên đường ống ngang và đồng hồ áp suất nối bằng vòng ống dẫn về đường ống; nửa dưới là sơ đồ vòng với I/P, bộ điều áp, bóng TIC và TE, bình trao đổi nhiệt có mũi tên dòng chảy, FO trên đường vào và van trên đường hơi.",
                "The upper cross-section shows an air-loaded regulator with a bolted diaphragm housing, adjustable spring, diaphragm, stem and valve body, an I/P transducer box feeding the housing from the left, a fixed orifice FO in the horizontal process line, and a pressure gauge connected by a tubing loop back to the line; the lower diagram shows the loop with the I/P, regulator, TIC and TE bubbles, a heat exchanger with flow arrows, the FO in the inlet line and a valve in the steam line.")
