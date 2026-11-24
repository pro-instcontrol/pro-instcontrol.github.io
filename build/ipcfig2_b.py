# -*- coding: utf-8 -*-
"""Vector figures 2.21-2.40 for IPC Chapter 2 (Transducers - II).

Supplier module for ``ipcfig2.py``.  Every figure is a simplified but
technically faithful redraw of the printed page: pressure transmitters
(2.21-2.33), displacement transducers (2.34-2.39) and the start of the
velocity section (2.40).  All visible text passes through ``T()``.
"""
from ipcfig2_common import (make_registry, T, _b, _ar, _frame, _series,
                            _legend, _wavey, _mk, _defs, _line, _circle,
                            _rect, _ellipse, _path, _poly, BLUE, GREEN, GREY, INK, RED)
FIGS, _reg = make_registry()


# ----------------------------------------------------------------- helpers
def _cap_h(x, y, plate=9.0, gap=4.0):
    """Capacitor inserted in a horizontal wire (vertical plates)."""
    return (_line(x - gap, y - plate, x - gap, y + plate, sw=1.2)
            + _line(x + gap, y - plate, x + gap, y + plate, sw=1.2))


def _cap_v(x, y, plate=9.0, gap=4.0):
    """Capacitor inserted in a vertical wire (horizontal plates)."""
    return (_line(x - plate, y - gap, x + plate, y - gap, sw=1.2)
            + _line(x - plate, y + gap, x + plate, y + gap, sw=1.2))


def _res(x0, y0, x1, y1, color=INK):
    """Zig-zag resistor between two points."""
    dx, dy = x1 - x0, y1 - y0
    ln = max((dx * dx + dy * dy) ** 0.5, 1.0)
    nx, ny = -dy / ln, dx / ln
    pts = [(x0 + dx * i / 8.0 + nx * (3.4 if i % 2 else -3.4),
            y0 + dy * i / 8.0 + ny * (3.4 if i % 2 else -3.4))
           for i in range(9)]
    return _poly(pts, sw=1.1, color=color)


def _coil_v(x, y0, y1, turns=4, amp=6.0, color=INK):
    """Vertical winding drawn as alternate loops."""
    n = turns * 2
    pts = [(x + (amp if i % 2 else -amp), y0 + (y1 - y0) * i / n)
           for i in range(n + 1)]
    return _poly(pts, sw=1.2, color=color)


def _coil_h(x0, x1, y, turns=4, amp=6.0, color=INK):
    """Horizontal winding drawn as alternate loops."""
    n = turns * 2
    pts = [(x0 + (x1 - x0) * i / n, y + (amp if i % 2 else -amp))
           for i in range(n + 1)]
    return _poly(pts, sw=1.2, color=color)


def _tri(x, y, w, h, label="", point="right", labdy=11):
    """Amplifier / detector triangle with an optional label below."""
    pts = ([(x + w, y), (x + w, y + h), (x, y + h / 2.0)] if point == "left"
           else [(x, y), (x, y + h), (x + w, y + h / 2.0)])
    o = [_poly(pts, close=True, fill="#eef3fb")]
    if label:
        o.append(T(x + w / 2.0, y + h + labdy, label, 6.4))
    return "".join(o)


def _valve(cx, cy, r=6.0):
    """Bow-tie isolation / tapping valve symbol."""
    return (_poly([(cx - r, cy - r), (cx, cy), (cx - r, cy + r)],
                  close=True, fill="#ffffff", sw=1.0)
            + _poly([(cx + r, cy - r), (cx, cy), (cx + r, cy + r)],
                    close=True, fill="#ffffff", sw=1.0))


def _gnd(x, y):
    return (_line(x, y, x, y + 5)
            + _line(x - 6, y + 5, x + 6, y + 5)
            + _line(x - 4, y + 8, x + 4, y + 8)
            + _line(x - 2, y + 11, x + 2, y + 11))


def _port(x, y):
    return _circle(x, y, 3.5, fill="#ffffff", sw=1.0)


# --------------------------------------------------------------- figures
@_reg
def fig_f21():
    """Practical capacitance pressure transmitter - block diagram."""
    o = [_defs()]
    o.append(T(340, 22, "Practical capacitance pressure transmitter", 9.6, color=INK))
    # sensor and oscillator front end
    o.append(T(62, 40, "Sensor", 6.8))
    o.append(_line(38, 55, 58, 55))
    o.append(_cap_h(62, 55))
    o.append(_ar(66, 55, 102, 55))
    o.append(_b(102, 41, 84, 28, "Demodulator"))
    o.append(_b(245, 41, 92, 28, "Current\ndetector"))
    o.append(_ar(186, 55, 245, 55))
    o.append(_line(337, 55, 362, 55))
    o.append(_line(362, 55, 362, 88))
    o.append(_b(387, 75, 94, 26, "Current limiter"))
    o.append(_ar(362, 88, 387, 88))
    # output load and terminal
    o.append(_res(497, 88, 537, 88))
    o.append(_ar(481, 88, 497, 88))
    o.append(_ar(537, 88, 595, 88))
    o.append(T(517, 78, "Load", 6.4))
    o.append(T(593, 79, "Signal output", 6.4, anchor="end"))
    o.append(_circle(600, 88, 3.0, fill="#ffffff", sw=1.0))
    # oscillator and its control amplifier
    o.append(_b(35, 108, 82, 26, "Oscillator"))
    o.append(_tri(120, 104, 36, 34, "Osc. control amp.", point="left"))
    o.append(_ar(120, 120, 118, 120))
    o.append(_ar(76, 108, 58, 63))
    o.append(_ar(156, 121, 290, 121, color=BLUE))
    # regulator and current-control loop
    o.append(_b(245, 137, 100, 28, "Voltage\nregulator"))
    o.append(_tri(372, 137, 38, 34, "Current control amp.", point="left"))
    o.append(_ar(291, 69, 291, 150))
    o.append(_ar(291, 150, 372, 150))
    o.append(_ar(345, 151, 372, 151))
    o.append(_b(422, 184, 84, 26, "Current control"))
    o.append(_ar(410, 154, 410, 184))
    o.append(_b(512, 137, 122, 28, "Reverse polarity\nprotection"))
    o.append(_ar(410, 154, 512, 154))
    return _mk(21, o, "Practical capacitance pressure transmitter - block diagram",
               "So do khoi bo phat ap suat dien dung thuc te",
               "Block diagram of a practical capacitance pressure transmitter",
               "So do khoi bo phat ap suat dien dung voi cam bien, bo giai dieu che, dao dong va dau ra tin hieu",
               "Block diagram with sensor, demodulator, oscillator, control amplifiers, current limiter and signal output")


@_reg
def fig_f22():
    """Sensing diaphragm held under initial tension."""
    o = [_defs()]
    o.append(T(340, 22, "Sensing diaphragm of the capacitance cell", 9.6, color=INK))
    # upper and lower clamped supports
    o.append(_line(250, 58, 336, 58, sw=1.4))
    for x in range(253, 337, 9):
        o.append(_line(x, 58, x - 5, 52, sw=0.8))
    o.append(_line(250, 178, 336, 178, sw=1.4))
    for x in range(253, 337, 9):
        o.append(_line(x, 178, x - 5, 172, sw=0.8))
    # deflected diaphragm
    o.append(_path("M293,58 C269,86 315,105 293,118 C271,133 315,152 293,178",
                   sw=2.2))
    # tension arrows
    o.append(_ar(293, 54, 293, 34, color=BLUE))
    o.append(T(293, 29, "Initial tension", 6.8))
    o.append(_ar(293, 182, 293, 202, color=BLUE))
    o.append(T(293, 212, "Initial tension", 6.8))
    # applied pressure
    o.append(_ar(420, 118, 353, 118, color=RED, sw=2.0))
    o.append(T(430, 115, "Applied pressure", 7.0))
    # diaphragm label
    o.append(_ar(212, 150, 274, 134, color=GREY, sw=1.0))
    o.append(T(197, 151, "Sensing diaphragm", 6.8, anchor="end"))
    return _mk(22, o, "Sensing diaphragm under initial tension and applied pressure",
               "Mang cam bien chiu luc dang ban dau va ap suat tac dung",
               "Sensing diaphragm under initial tension and applied pressure",
               "Mang cam bien cong giua hai dau co dinh, co luc dang ban dau va ap suat tac dung ngang o giua",
               "A curved sensing diaphragm clamped at both ends with initial tension arrows and an applied pressure arrow")


@_reg
def fig_f23():
    """Variable inductance pressure transmitter - mechanical assembly."""
    o = [_defs()]
    o.append(T(340, 20, "Variable inductance pressure transmitter", 9.6, color=INK))
    # bourdon tube (dashed C) and force bar
    o.append(_path("M170,112 A38,38 0 1 0 170,188", sw=1.6, dash="5,4"))
    o.append(_line(170, 150, 215, 150, sw=1.4))
    o.append(_b(215, 72, 12, 116, "", fill="#eef3fb"))
    o.append(T(160, 196, "Bourdon element", 6.4))
    o.append(T(120, 140, "Force bar", 6.8))
    o.append(_ar(178, 140, 212, 140, color=GREY, sw=1.0))
    # flexure pivots
    for cy in (92, 160):
        o.append(_circle(221, cy, 4.0, fill="#ffffff", sw=1.1))
    o.append(T(150, 84, "Flexure pivot", 6.4))
    o.append(_line(225, 92, 205, 87, sw=0.9))
    o.append(T(150, 168, "Flexure pivot", 6.4))
    o.append(_line(225, 160, 205, 164, sw=0.9))
    # suppression / elevation spring and span adjustment
    o.append(_res(225, 48, 295, 48))
    o.append(T(310, 51, "Suppression / Elevation spring", 6.4))
    o.append(_line(260, 55, 260, 70, sw=1.0))
    o.append(_line(255, 70, 268, 70, sw=1.4))
    o.append(T(295, 72, "Span adjustment", 6.4))
    o.append(_ar(288, 70, 268, 70, color=GREY, sw=0.9))
    # vector linkage and flexure arm
    o.append(_line(227, 100, 300, 112, sw=1.6))
    o.append(T(315, 110, "Vector linkage", 6.4))
    o.append(_line(245, 124, 295, 124, sw=1.4))
    o.append(T(200, 120, "Flexure arm", 6.4))
    # position transducer and secondary beam
    o.append(_b(238, 86, 62, 18, "Position\ntransducer", size=5.8))
    o.append(_line(235, 138, 340, 138, sw=1.6))
    o.append(T(365, 141, "Secondary beam", 6.4))
    # force coil and magnet
    o.append(_coil_v(305, 118, 146, turns=4, amp=7))
    o.append(_b(299, 150, 14, 26, "", fill="#e9e3d6"))
    o.append(T(345, 128, "Force coil", 6.4))
    o.append(T(345, 168, "Magnet", 6.4))
    o.append(_line(319, 128, 340, 128, sw=0.9))
    o.append(_line(306, 162, 340, 162, sw=0.9))
    # electronic unit, zero adjustment and output
    o.append(_b(250, 184, 84, 28, "Electronic\nunit", size=6.4))
    o.append(_circle(352, 184, 4.0, fill="#ffffff", sw=1.1))
    o.append(T(390, 184, "Zero adjustment", 6.4))
    o.append(_line(356, 184, 358, 184, sw=0.9))
    o.append(_line(334, 198, 364, 210, sw=1.2))
    o.append(_ar(364, 210, 396, 210))
    o.append(T(412, 213, "Output", 6.4))
    return _mk(23, o, "Variable inductance pressure transmitter - mechanical assembly",
               "Bo phat ap suat cam ung bien doi - cau truc co khi",
               "Variable inductance pressure transmitter - mechanical assembly",
               "Cum co khi gom ong bourdon, thanh luc, ban le, lien ket vector, cuon luc, nam cham va bo khuech dai dien tu",
               "Mechanical assembly showing bourdon element, force bar, flexure pivots, vector linkage, force coil, magnet and electronic unit")


@_reg
def fig_f24():
    """Resonant frequency pressure transmitter - block diagram."""
    o = [_defs()]
    o.append(T(340, 20, "Resonant frequency pressure transmitter", 9.6, color=INK))
    # sensor wire, oscillator and pulse shaper
    o.append(_b(35, 44, 74, 28, "Sensor unit"))
    o.append(_coil_v(24, 48, 68, turns=4, amp=5))
    o.append(_ar(109, 58, 145, 58))
    o.append(_b(145, 44, 76, 28, "Oscillator"))
    o.append(_ar(221, 58, 258, 58))
    o.append(_b(258, 44, 88, 28, "Pulse shaper"))
    o.append(T(300, 36, "two complementary frequencies", 6.0))
    # split to two frequency converters
    o.append(_line(346, 58, 380, 58))
    o.append(_line(380, 58, 380, 96))
    o.append(_line(380, 58, 380, 146))
    o.append(_ar(380, 96, 410, 96))
    o.append(_ar(380, 146, 410, 146))
    o.append(_b(410, 81, 104, 30, "Frequency\nconverter"))
    o.append(_b(410, 131, 104, 30, "Frequency\nconverter"))
    # output amplifier and output
    o.append(_line(514, 96, 536, 96))
    o.append(_line(536, 146, 536, 96))
    o.append(_ar(536, 121, 566, 121))
    o.append(_b(566, 106, 80, 30, "Output\namplifier"))
    o.append(_ar(646, 121, 672, 121))
    # zero adjustment and balance
    o.append(_res(470, 62, 510, 62))
    o.append(_ar(490, 54, 490, 62, color=BLUE))
    o.append(T(492, 76, "Zero adjustment", 6.2))
    o.append(_res(145, 88, 145, 122))
    o.append(T(120, 108, "Balance", 6.2, anchor="end"))
    # span network, inverter, reference and voltage regulator
    o.append(_res(258, 148, 258, 176))
    o.append(T(240, 164, "Coarse span jumper", 6.0, anchor="end"))
    o.append(_res(300, 150, 300, 176))
    o.append(T(310, 170, "Fine span", 6.2))
    o.append(_b(395, 182, 96, 26, "Frequency inverter"))
    o.append(_b(230, 182, 78, 26, "Reference"))
    o.append(_b(318, 182, 70, 26, "Voltage\nregulator", size=6.0))
    o.append(_ar(269, 195, 318, 195))
    o.append(_ar(388, 195, 395, 195))
    o.append(_ar(443, 182, 443, 161))
    return _mk(24, o, "Resonant frequency pressure transmitter - block diagram",
               "So do khoi bo phat ap suat tan so cong huong",
               "Resonant frequency pressure transmitter - block diagram",
               "So do khoi gom cam bien day cong huong, dao dong, tao xung, bo doi tan so, khuec dai dau ra va nguon tham chieu",
               "Block diagram with resonant wire sensor, oscillator, pulse shaper, frequency converters, output amplifier and reference supply")


@_reg
def fig_f25():
    """Quartz resonant pressure sensor - cross-section."""
    o = [_defs()]
    o.append(T(340, 20, "Quartz resonant pressure sensor", 9.6, color=INK))
    # pressure housing with hatched wall
    o.append(_rect(150, 62, 380, 108, fill="#ffffff", sw=1.2))
    o.append(_rect(158, 70, 364, 92, fill="url(#h7)", sw=1.0))
    # inlet passage
    o.append(_line(100, 100, 158, 100, sw=1.2))
    o.append(_line(100, 128, 158, 128, sw=1.2))
    o.append(_ar(88, 114, 128, 114, color=BLUE))
    o.append(T(94, 150, "Pressure inlet", 6.6))
    # central quartz crystal pressure sensor
    o.append(_rect(250, 80, 120, 72, fill="#fbfaf7", sw=1.2))
    for yy in range(86, 150, 8):
        o.append(_line(256, yy, 364, yy, sw=0.4, color="#d8d2c4"))
    o.append(T(310, 122, "Quartz crystal", 6.8))
    o.append(T(310, 132, "pressure sensor", 6.8))
    o.append(_ar(310, 56, 310, 78, color=GREY, sw=0.9))
    # spacer, reference crystal and temperature crystal
    o.append(_rect(222, 132, 28, 18, fill="#e9e3d6", sw=1.0))
    o.append(T(236, 166, "Spacer", 6.4))
    o.append(_rect(452, 78, 48, 18, fill="#eef3fb", sw=1.0))
    o.append(T(476, 70, "Reference crystal", 6.2))
    o.append(_rect(452, 132, 48, 18, fill="#eef3fb", sw=1.0))
    o.append(T(476, 166, "Crystal for temperature", 6.0))
    o.append(T(476, 174, "sensor", 6.0))
    # electrical pins
    for yy in (86, 100, 114, 128, 142):
        o.append(_line(500, yy, 570, yy, sw=1.2))
        o.append(_circle(570, yy, 2.4, fill="#ffffff", sw=1.0))
    o.append(T(340, 188, "Pressure housing", 6.6))
    o.append(_line(340, 184, 152, 170, sw=0.9, color=GREY))
    return _mk(25, o, "Quartz resonant pressure sensor - cross-section",
               "Cam bien ap suat cong huong thach anh - mat cat",
               "Quartz resonant pressure sensor - cross-section",
               "Mat cat vo cam bien gom cua vao ap suat, tinh the thach anh cam ap, tinh the tham chieu va tinh the cam nhiet do",
               "Cross-section of the pressure housing with inlet, quartz pressure sensor, reference crystal and temperature crystal")


@_reg
def fig_f26():
    """Smart transmitter using a capacitance sensing element."""
    o = [_defs()]
    o.append(T(340, 18, "Smart transmitter with capacitance sensing element", 9.4, color=INK))
    # signal bus
    o.append(_line(60, 46, 630, 46, sw=1.8))
    o.append(T(345, 39, "Signal Bus System", 7.0))
    # bus-mounted blocks
    blocks = [(64, "A/D\nconverter"), (152, "System I\nPROM"), (236, "Sensor\nPROM"),
              (320, "System II\nPROM"), (404, "EEP-\nROM"), (472, "RAM"),
              (530, "D/A\nconverter")]
    for x, lab in blocks:
        w = 76 if x in (64, 152, 236, 320, 530) else 56
        o.append(_b(x, 53, w, 28, lab, size=6.0))
        o.append(_line(x + w / 2.0, 53, x + w / 2.0, 46, sw=0.9))
    # microprocessor and digital output
    o.append(_b(300, 108, 120, 30, "Microprocessor unit", size=7.0))
    o.append(_b(530, 108, 78, 30, "Digital output", size=6.4))
    o.append(_ar(360, 108, 360, 81, color=BLUE))
    o.append(_ar(488, 123, 530, 123))
    # sensors
    o.append(_b(104, 150, 92, 26, "Temperature sensor", size=6.2))
    o.append(_b(104, 190, 92, 26, "Pressure sensor", size=6.4))
    o.append(_ar(150, 150, 150, 81, color=GREY))
    o.append(_ar(150, 190, 150, 150, color=BLUE))
    o.append(_ar(196, 203, 300, 128, color=BLUE))
    # calibration and ambient pressure arrows
    o.append(_b(286, 184, 104, 26, "Calibration adjustment", size=6.2))
    o.append(_ar(338, 184, 338, 138, color=GREY))
    o.append(_ar(30, 213, 102, 213, color=GREY))
    o.append(T(28, 208, "Atmospheric pressure", 6.2, anchor="end"))
    o.append(_ar(280, 213, 198, 213, color=GREY))
    o.append(T(282, 208, "Process pressure", 6.2))
    # output signal and hand-held communicator
    o.append(_ar(608, 123, 654, 123, color=RED))
    o.append(T(652, 115, "Output signal", 6.2, anchor="end"))
    o.append(_rect(566, 148, 62, 58, fill="#eef3fb", sw=1.1))
    for yy in (158, 168, 178, 188):
        o.append(_line(572, yy, 622, yy, sw=0.7, color=GREY))
    o.append(T(597, 216, "HHC", 6.6))
    o.append(_ar(598, 148, 598, 138, color=GREY))
    return _mk(26, o, "Smart transmitter using capacitance sensing element",
               "Bo phat thong minh dung phan tu cam bien dien dung",
               "Smart transmitter using a capacitance sensing element",
               "So do bo phat thong minh gom A/D, bo vi xu ly, PROM, EEPROM, RAM, D/A, dau ra so va may lien lac cam tay HHC",
               "Smart transmitter block diagram with A/D converter, microprocessor, PROM, EEPROM, RAM, D/A, digital output and HHC")


@_reg
def fig_f27():
    """Resonant silicon sensing element with two H-shaped resonators."""
    o = [_defs()]
    o.append(T(340, 20, "Resonant silicon sensing element (90 kHz)", 9.6, color=INK))
    # excitation coil and ground on the left
    o.append(_coil_v(52, 84, 158, turns=5, amp=7))
    o.append(_gnd(52, 158))
    o.append(_line(52, 84, 130, 84, sw=1.2))
    o.append(_line(52, 158, 130, 158, sw=1.2))
    o.append(_coil_v(130, 96, 146, turns=4, amp=6))
    # two H-shaped resonators
    for x, w in ((170, 34), (230, 34)):
        o.append(_line(x, 78, x, 164, sw=2.2))
        o.append(_line(x + w, 78, x + w, 164, sw=2.2))
        o.append(_line(x, 121, x + w, 121, sw=2.2))
        for px, py, s in ((x + 3, 81, "+"), (x + w - 3, 81, "-"),
                          (x + 3, 161, "-"), (x + w - 3, 161, "+")):
            o.append(_circle(px, py, 5.0, fill="#ffffff", sw=0.9))
            o.append(T(px, py + 2.4, s, 6.0))
    o.append(T(187, 178, "Outer resonator", 6.2))
    o.append(T(247, 178, "Central resonator", 6.2))
    # pick-up coil, buffer and output
    o.append(_line(264, 84, 296, 84, sw=1.2))
    o.append(_line(264, 158, 296, 158, sw=1.2))
    o.append(_coil_v(304, 96, 146, turns=4, amp=6))
    o.append(T(304, 76, "E", 7.4))
    o.append(_tri(338, 96, 42, 50, "", point="right"))
    o.append(_ar(380, 121, 470, 121))
    o.append(T(475, 118, "Output", 6.6))
    o.append(T(475, 128, "(frequency)", 6.6))
    o.append(T(340, 200, "Applied pressure changes the resonant frequencies", 6.6, color=GREY))
    return _mk(27, o, "Resonant silicon sensing element with two H-shaped resonators",
               "Phan tu cam bien silicon cong huong voi hai bo cong huong chu H",
               "Resonant silicon sensing element with two H-shaped resonators",
               "Hai bo cong huong chu H duoc kich thich o tan so tu nhien 90 kHz, tao dau ra tan so",
               "Two H-shaped resonators excited at their natural frequency of 90 kHz with a frequency output")


@_reg
def fig_f28():
    """Resonant frequency versus applied pressure."""
    o = [_defs()]
    fr, mrx, mry = _frame(130, 32, 420, 150, (0, 10000), (70, 110),
                          [(0, "0"), (5000, "5000"), (10000, "10000")],
                          [(70, "70"), (80, "80"), (90, "90"),
                           (100, "100"), (110, "110")],
                          "Pressure mm WG.", "Frequency KHz")
    o.append(fr)
    fa = [(0, 92), (2500, 96), (5000, 100), (7500, 104), (10000, 108)]
    fb = [(0, 88), (2500, 84), (5000, 80), (7500, 76), (10000, 72)]
    o.append(_series(fa, mrx, mry, BLUE))
    o.append(_series(fb, mrx, mry, RED))
    o.append(T(mrx(7700), mry(104.4) - 6, "Fa", 7.4, color=BLUE))
    o.append(T(mrx(7700), mry(76.5) + 9, "Fb", 7.4, color=RED))
    o.append(T(340, 20, "Resonant frequency versus applied pressure", 9.4, color=INK))
    return _mk(28, o, "Resonant frequency versus applied pressure",
               "Tan so cong huong theo ap suat tac dung",
               "Resonant frequency versus applied pressure",
               "Do thi tan so Fa tang va Fb giam theo ap suat tu 0 den 10000 mm WG",
               "Graph of rising Fa and falling Fb resonant frequencies against pressure from 0 to 10000 mm WG")


@_reg
def fig_f29():
    """Pulsation dampener with pigtail syphon."""
    o = [_defs()]
    o.append(T(340, 20, "Pulsation dampener (pigtail syphon)", 9.4, color=INK))
    # process pipe and butt weld
    o.append(_rect(196, 202, 128, 14, fill="#eef3fb", sw=1.2))
    o.append(_ellipse(196, 209, 9, 7, fill="#ffffff", sw=1.0))
    o.append(_ellipse(324, 209, 9, 7, fill="#ffffff", sw=1.0))
    o.append(T(360, 213, "Butt weld", 6.4))
    o.append(_line(352, 209, 324, 204, sw=0.9, color=GREY))
    # half coupling and tapping valve
    o.append(_rect(248, 186, 26, 16, fill="#e9e3d6", sw=1.0))
    o.append(T(175, 190, "Half coupling", 6.4, anchor="end"))
    o.append(_line(196, 189, 246, 189, sw=0.9, color=GREY))
    o.append(_valve(261, 172, 7))
    o.append(_line(261, 186, 261, 179, sw=1.2))
    o.append(T(300, 172, "Tapping valve", 6.4))
    o.append(_line(268, 172, 296, 172, sw=0.9, color=GREY))
    # pigtail loop and riser
    o.append(_line(261, 165, 261, 148, sw=1.2))
    o.append(_circle(261, 130, 20, fill="none", sw=1.4))
    o.append(_ar(282, 130, 322, 130, color=GREY, sw=0.9))
    o.append(T(326, 127, "Pigtail", 6.6))
    o.append(_line(261, 110, 261, 88, sw=1.2))
    # pressure gauge
    o.append(_circle(261, 66, 22, fill="#ffffff", sw=1.4))
    o.append(_line(261, 66, 273, 52, sw=1.4, color=RED))
    o.append(_circle(261, 66, 2.0, fill=INK, sw=0))
    o.append(_ar(295, 66, 285, 66, color=GREY, sw=0.9))
    o.append(T(300, 62, "Pressure gage", 6.6))
    o.append(T(340, 200, "Half coupling details: Figure 2.32", 6.0, color=GREY))
    return _mk(29, o, "Pulsation dampener with pigtail syphon",
               "Bo giam xung voi ong xoan pigtail",
               "Pulsation dampener with pigtail syphon",
               "Dong ho ap suat noi qua ong xoan pigtail, van lay mau, moi han va khop noi vao duong ong",
               "Pressure gauge connected through a pigtail loop, tapping valve and half coupling to the process pipe")


@_reg
def fig_f30():
    """Temperature equalizing column for steam service."""
    o = [_defs()]
    o.append(T(340, 20, "Temperature equalizing column", 9.6, color=INK))
    # column vessel with liquid level
    o.append(_path("M300,58 L300,112 A34,34 0 0 0 368,112 L368,58", sw=1.4))
    o.append(_line(295, 58, 373, 58, sw=1.2))
    o.append(_line(302, 104, 366, 104, sw=1.0))
    for yy in (108, 114, 120, 126):
        o.append(_line(307, yy, 361, yy, sw=0.6, color="#9a9a9a"))
    o.append(_ar(456, 66, 372, 66, color=RED, sw=1.6))
    o.append(T(458, 63, "Saturated steam", 6.6))
    # downcomer and return leg
    o.append(_line(334, 146, 334, 186, sw=1.4))
    o.append(_path("M334,186 Q334,198 322,198 L254,198 Q242,198 242,186 L242,172",
                   sw=1.4))
    o.append(_ar(150, 172, 240, 172, color=BLUE, sw=1.6))
    o.append(T(200, 166, "Boiler feed water", 6.6))
    o.append(T(200, 175, "(BFW) at elevated temperature", 6.2))
    o.append(T(334, 214, "Equalizing column condenses steam", 6.4, color=GREY))
    return _mk(30, o, "Temperature equalizing column for steam service",
               "Cot can bang nhiet do cho duong hoi",
               "Temperature equalizing column for steam service",
               "Cot chua hoi bao hoa noi voi nuoc cap lo hoi o nhiet do cao de on dinh nhiet do",
               "Column connecting saturated steam to boiler feed water at elevated temperature")


@_reg
def fig_f31():
    """Seal pot with glycerene sealing liquid."""
    o = [_defs()]
    o.append(T(340, 20, "Seal pot", 9.6, color=INK))
    # vessel
    o.append(_path("M286,54 L286,186 A36,20 0 0 0 358,186 L358,54", sw=1.3))
    o.append(_ellipse(322, 54, 36, 10, fill="#ffffff", sw=1.2))
    o.append(_ellipse(322, 186, 36, 10, fill="#ffffff", sw=1.2))
    # glycerene fill
    for yy in range(102, 182, 8):
        o.append(_line(290, yy, 354, yy, sw=0.6, color="#9a9a9a"))
    o.append(T(400, 130, "Glycerene", 6.8))
    o.append(_line(394, 130, 356, 130, sw=0.9, color=GREY))
    # measurement fluid inlet
    o.append(_ar(322, 30, 322, 50, color=BLUE, sw=1.6))
    o.append(T(322, 24, "Measurement fluid", 6.6))
    # plugging arrangements
    o.append(_rect(276, 82, 12, 16, fill="#e9e3d6", sw=1.0))
    o.append(_rect(356, 82, 12, 16, fill="#e9e3d6", sw=1.0))
    o.append(T(250, 82, "Plugging", 6.2, anchor="end"))
    o.append(T(250, 91, "arrangement", 6.2, anchor="end"))
    o.append(T(404, 82, "Plugging", 6.2))
    o.append(T(404, 91, "arrangement", 6.2))
    # outlet to instrument
    o.append(_ar(322, 196, 322, 218, color=BLUE, sw=1.4))
    o.append(T(322, 230, "To measuring instrument", 6.6))
    return _mk(31, o, "Seal pot with glycerene sealing liquid",
               "Binh chan voi chat long lam kin glycerin",
               "Seal pot with glycerene sealing liquid",
               "Binh chan chua glycerin, co hai cong bang va duong dan toi thiet bi do",
               "Seal pot filled with glycerene, two plugging arrangements and a line to the measuring instrument")


@_reg
def fig_f32():
    """Details of half coupling."""
    o = [_defs()]
    o.append(T(340, 20, "Details of half coupling", 9.6, color=INK))
    o.append(_line(330, 50, 330, 178, sw=0.8, dash="5,4", color=GREY))
    o.append(_line(370, 50, 370, 178, sw=0.8, dash="5,4", color=GREY))
    # half inch pipe walls
    o.append(_line(340, 64, 340, 118, sw=1.4))
    o.append(_line(360, 64, 360, 118, sw=1.4))
    # butt weld
    o.append(_path("M338,118 L342,112 L346,118 L350,112 L354,118 L358,112 L362,118",
                   sw=1.3, color=RED))
    # half coupling body
    o.append(_rect(334, 118, 32, 46, fill="url(#h6)", sw=1.2))
    o.append(_line(334, 142, 366, 142, sw=0.8, color=GREY))
    # labels
    o.append(T(400, 78, "1/2 inch pipe", 6.6))
    o.append(_line(394, 78, 362, 78, sw=0.9, color=GREY))
    o.append(T(400, 112, "Butt weld", 6.6))
    o.append(_line(394, 112, 364, 114, sw=0.9, color=GREY))
    o.append(T(400, 146, "Half coupling", 6.6))
    o.append(_line(394, 146, 368, 146, sw=0.9, color=GREY))
    o.append(T(350, 190, "Section through the pipe wall", 6.2, color=GREY))
    return _mk(32, o, "Details of half coupling",
               "Chi tiet khop noi nua",
               "Details of half coupling",
               "Mat cat chi tiet ong nua inch, moi han va khop noi nua",
               "Cross-section detail of the half inch pipe, butt weld and half coupling")


@_reg
def fig_f33():
    """Typical impulse line installation."""
    o = [_defs()]
    o.append(T(340, 18, "Typical impulse line installation", 9.4, color=INK))
    # main pipe and flow
    o.append(_rect(96, 52, 24, 142, fill="#eef3fb", sw=1.2))
    o.append(_ellipse(108, 52, 12, 6, fill="#ffffff", sw=1.0))
    o.append(_ellipse(108, 194, 12, 6, fill="#ffffff", sw=1.0))
    o.append(_ar(108, 44, 108, 24, color=BLUE))
    o.append(T(108, 18, "Process flow", 6.4))
    o.append(T(72, 122, "Main pipe", 6.2, anchor="end"))
    # two tapping valves
    o.append(_line(120, 104, 152, 104, sw=1.2))
    o.append(_line(120, 132, 152, 132, sw=1.2))
    o.append(_valve(138, 104, 6))
    o.append(_valve(138, 132, 6))
    o.append(T(182, 92, "1/2 inch tapping valves", 6.2))
    o.append(_line(180, 95, 145, 102, sw=0.9, color=GREY))
    # tee joint 1 and plug
    o.append(_rect(190, 96, 44, 44, fill="#ffffff", sw=1.2))
    o.append(_rect(207, 86, 10, 10, fill="#e9e3d6", sw=1.0))
    o.append(T(270, 92, "1/2 inch plug", 6.2))
    o.append(_line(266, 92, 218, 92, sw=0.9, color=GREY))
    o.append(T(266, 118, "Tee-joint-1 (1/2 inch)", 6.2))
    # impulse pipe down to tee 2
    o.append(_line(212, 140, 212, 178, sw=1.4))
    o.append(T(268, 152, "1/2 inch impulse pipe", 6.2))
    o.append(_line(262, 152, 214, 152, sw=0.9, color=GREY))
    o.append(_rect(236, 168, 36, 22, fill="#ffffff", sw=1.1))
    o.append(T(258, 204, "Tee-joint-2", 6.2))
    # drain leg
    o.append(_line(246, 190, 246, 206, sw=1.2))
    o.append(_valve(246, 208, 6))
    o.append(_ar(246, 214, 246, 226, color=GREY, sw=1.0))
    o.append(T(268, 224, "Drain", 6.2))
    # isolation valve, union joint and transducer
    o.append(_line(272, 179, 300, 179, sw=1.2))
    o.append(_valve(310, 179, 6))
    o.append(_line(316, 179, 338, 179, sw=1.2))
    o.append(_rect(338, 171, 16, 16, fill="#e9e3d6", sw=1.0))
    o.append(T(346, 204, "1/2 inch union joint", 6.0))
    o.append(_line(346, 204, 346, 187, sw=0.9, color=GREY))
    o.append(_line(354, 179, 380, 179, sw=1.2))
    o.append(_b(380, 160, 56, 38, "Pressure\ntransducer", size=6.0))
    o.append(_line(436, 179, 470, 179, sw=1.2))
    o.append(_rect(486, 142, 14, 76, fill="#eef3fb", sw=1.1))
    o.append(_line(470, 179, 486, 179, sw=1.2))
    o.append(T(520, 150, "Mounting stand", 6.2))
    o.append(_line(516, 150, 500, 150, sw=0.9, color=GREY))
    o.append(T(408, 206, "Clamp", 6.2))
    o.append(_line(408, 202, 408, 198, sw=0.9, color=GREY))
    return _mk(33, o, "Typical impulse line installation",
               "Lap dat duong dan xung dien hinh",
               "Typical impulse line installation",
               "Lap dat duong dan xung gom hai van lay mau, T noi, van xa, khop noi va bo chuyen doi ap suat",
               "Impulse line installation with tapping valves, tee joints, drain, union joint and pressure transducer")


@_reg
def fig_f34():
    """Variable resistance displacement transducer."""
    o = [_defs()]
    o.append(T(340, 20, "Variable resistance displacement transducer", 9.4, color=INK))
    # supply battery and potentiometer track
    o.append(_line(120, 72, 120, 116, sw=1.4))
    o.append(_line(112, 116, 128, 116, sw=1.6))
    o.append(_line(116, 124, 124, 124, sw=1.1))
    o.append(_line(120, 124, 120, 176, sw=1.4))
    o.append(T(102, 126, "Eb", 7.0, anchor="end"))
    o.append(_line(120, 72, 280, 72, sw=1.2))
    o.append(_res(280, 74, 280, 172))
    o.append(_line(120, 176, 280, 176, sw=1.2))
    # wiper and load
    o.append(_line(372, 118, 290, 118, sw=1.0, color=BLUE, dash="4,3"))
    o.append(_ar(298, 118, 286, 118, color=BLUE, sw=1.4))
    o.append(_line(372, 118, 372, 140, sw=1.2))
    o.append(_res(372, 140, 372, 174))
    o.append(_line(372, 174, 280, 174, sw=1.2))
    o.append(T(388, 156, "R0", 6.8))
    # output voltage arrow
    o.append(_ar(412, 174, 412, 118, color=RED, sw=1.4))
    o.append(T(428, 148, "E0", 7.0))
    # displacement indication
    o.append(_ar(458, 110, 458, 84, color=GREY, sw=1.2))
    o.append(_ar(458, 110, 458, 136, color=GREY, sw=1.2))
    o.append(T(490, 112, "Displacement", 6.6))
    o.append(T(340, 202, "Wiper motion changes the divided output voltage", 6.4, color=GREY))
    return _mk(34, o, "Variable resistance displacement transducer",
               "Bo chuyen doi dich chuyen dien tro bien doi",
               "Variable resistance displacement transducer",
               "Mach chiet ap voi nguon Eb, can tiep diem dich chuyen, dien tro R0 va dien ap ra E0",
               "Potentiometer circuit with source Eb, moving wiper, resistor R0 and output voltage E0")


@_reg
def fig_f35():
    """LVDT construction."""
    o = [_defs()]
    o.append(T(340, 20, "LVDT construction", 9.6, color=INK))
    # body cylinder
    o.append(_rect(280, 82, 100, 104, fill="#ffffff", sw=1.3))
    o.append(_ellipse(330, 82, 50, 12, fill="#ffffff", sw=1.2))
    o.append(_ellipse(330, 186, 50, 12, fill="#ffffff", sw=1.2))
    # primary coil on the left
    o.append(_coil_v(268, 110, 158, turns=5, amp=8))
    o.append(_port(238, 110))
    o.append(_port(238, 158))
    o.append(_line(238, 110, 260, 110, sw=1.1))
    o.append(_line(238, 158, 260, 158, sw=1.1))
    o.append(T(196, 126, "Source voltage", 6.4))
    # movable core and arm
    o.append(_rect(324, 52, 12, 88, fill="#e9e3d6", sw=1.2))
    o.append(_line(330, 52, 330, 42, sw=1.4))
    o.append(_line(312, 42, 348, 42, sw=1.4, dash="5,3"))
    o.append(T(280, 36, "Arm", 6.6))
    o.append(_ar(362, 44, 362, 64, color=GREY, sw=1.1))
    o.append(_ar(362, 44, 362, 24, color=GREY, sw=1.1))
    o.append(T(400, 42, "Range of displacement", 6.4))
    # two secondary coils
    o.append(_coil_v(392, 100, 126, turns=3, amp=8))
    o.append(_coil_v(392, 142, 168, turns=3, amp=8))
    o.append(_port(424, 100))
    o.append(_port(424, 126))
    o.append(_port(424, 142))
    o.append(_port(424, 168))
    for yy in (100, 126, 142, 168):
        o.append(_line(400, yy, 424, yy, sw=1.1))
    o.append(_ar(452, 126, 452, 100, color=GREY, sw=1.1))
    o.append(_ar(452, 126, 452, 168, color=GREY, sw=1.1))
    o.append(T(462, 138, "Output", 6.6))
    o.append(T(340, 212, "Movable magnetic core inside three coaxial coils", 6.2, color=GREY))
    return _mk(35, o, "LVDT construction",
               "Cau truc LVDT",
               "LVDT construction",
               "Cau truc LVDT gom cuon so cap, hai cuon thu cap va loi tu di dong",
               "LVDT construction with a primary coil, two secondary coils and a movable magnetic core")


@_reg
def fig_f36():
    """LVDT rectifier circuit with two secondary coils."""
    o = [_defs()]
    o.append(T(340, 20, "LVDT diode rectifier circuit", 9.6, color=INK))
    # source winding
    o.append(_port(118, 106))
    o.append(_port(118, 154))
    o.append(_coil_v(170, 106, 154, turns=4, amp=8))
    o.append(_line(118, 106, 162, 106, sw=1.1))
    o.append(_line(118, 154, 162, 154, sw=1.1))
    o.append(T(96, 132, "Source voltage", 6.2, anchor="end"))
    # core
    o.append(_rect(232, 84, 12, 92, fill="#e9e3d6", sw=1.2))
    o.append(T(238, 190, "Core", 6.4))
    o.append(_ar(238, 78, 238, 58, color=GREY, sw=1.1))
    o.append(_ar(238, 78, 238, 98, color=GREY, sw=1.1))
    o.append(T(286, 58, "Displacement", 6.4))
    # secondary windings
    o.append(_coil_v(286, 100, 126, turns=3, amp=8))
    o.append(_coil_v(286, 138, 164, turns=3, amp=8))
    o.append(T(318, 98, "Secondary 1", 6.2))
    o.append(T(318, 174, "Secondary 2", 6.2))
    # diodes and resistors
    for cy, lab in ((112, "D1"), (150, "D2")):
        o.append(_line(294, cy, 380, cy, sw=1.1))
        o.append(_poly([(380, cy - 6), (392, cy), (380, cy + 6)], close=True, fill="#ffffff", sw=1.1))
        o.append(_line(392, cy - 6, 392, cy + 6, sw=1.2))
        o.append(T(386, cy - 10, lab, 6.2))
        o.append(_line(400, cy, 444, cy, sw=1.1))
    o.append(_res(444, 112, 444, 150))
    o.append(T(458, 126, "R1", 6.2))
    o.append(_ar(420, 124, 420, 108, color=BLUE, sw=1.0))
    o.append(T(424, 102, "I1", 6.0))
    o.append(_ar(420, 138, 420, 154, color=BLUE, sw=1.0))
    o.append(T(424, 162, "I2", 6.0))
    # output polarity arrow
    o.append(_ar(500, 110, 500, 168, color=RED, sw=1.4))
    o.append(T(518, 142, "eout", 7.0))
    o.append(_line(444, 110, 500, 110, sw=1.0))
    o.append(_line(444, 168, 500, 168, sw=1.0))
    return _mk(36, o, "LVDT rectifier circuit with two secondary coils",
               "Mach chinh luu LVDT voi hai cuon thu cap",
               "LVDT rectifier circuit with two secondary coils",
               "Mach gom D1, D2, R1, R2 tao dien ap ra eout theo dich chuyen cua loi",
               "Circuit with diodes D1 D2 and resistors R1 R2 producing output eout")


@_reg
def fig_f37():
    """LVDT secondary coils in series opposition."""
    o = [_defs()]
    o.append(T(340, 20, "Secondary coils in series opposition", 9.6, color=INK))
    # source winding
    o.append(_port(122, 106))
    o.append(_port(122, 154))
    o.append(_coil_v(174, 106, 154, turns=4, amp=8))
    o.append(_line(122, 106, 166, 106, sw=1.1))
    o.append(_line(122, 154, 166, 154, sw=1.1))
    o.append(T(100, 132, "Source voltage", 6.2, anchor="end"))
    # core and movement
    o.append(_rect(238, 84, 12, 92, fill="#e9e3d6", sw=1.2))
    o.append(_line(244, 84, 244, 70, sw=1.2))
    o.append(_line(232, 70, 256, 70, sw=1.2, dash="4,3"))
    o.append(T(244, 190, "Core", 6.4))
    # upper secondary with polarity
    o.append(_coil_v(292, 100, 124, turns=3, amp=8))
    o.append(_port(328, 100))
    o.append(_line(300, 100, 328, 100, sw=1.1))
    o.append(T(344, 98, "+", 8.0))
    o.append(T(344, 126, "-", 8.0))
    o.append(T(392, 114, "e01", 7.0))
    # lower secondary with reversed polarity
    o.append(_coil_v(292, 140, 164, turns=3, amp=8))
    o.append(_port(328, 164))
    o.append(_line(300, 164, 328, 164, sw=1.1))
    o.append(T(344, 140, "-", 8.0))
    o.append(T(344, 168, "+", 8.0))
    o.append(T(392, 154, "e02", 7.0))
    o.append(_line(328, 100, 328, 124, sw=1.0, color=GREY))
    o.append(_line(328, 140, 328, 164, sw=1.0, color=GREY))
    o.append(T(340, 202, "Opposite polarity gives an AC output proportional to displacement", 6.2, color=GREY))
    return _mk(37, o, "LVDT secondary coils connected in series opposition",
               "Hai cuon thu cap LVDT mac nguoc pha",
               "LVDT secondary coils connected in series opposition",
               "Hai cuon thu cap mac nguoc pha cho e01 va e02 doi nhau",
               "Two secondary coils in series opposition with opposite polarity e01 and e02")


@_reg
def fig_f38():
    """RVDT rotary displacement transducer."""
    o = [_defs()]
    o.append(T(340, 20, "RVDT - rotary variable differential transformer", 9.0, color=INK))
    # outer arc secondary coils (split at the top)
    o.append(_path("M224,116 Q280,48 332,56", sw=13, color=INK))
    o.append(_path("M348,56 Q400,48 456,116", sw=13, color=INK))
    o.append(T(196, 82, "Secondary 1", 6.6))
    o.append(_line(214, 84, 242, 100, sw=0.9, color=GREY))
    o.append(T(472, 82, "Secondary 2", 6.6))
    o.append(_line(470, 84, 440, 100, sw=0.9, color=GREY))
    # cam-shaped magnetic core
    o.append(_path("M274,136 A70,70 0 0 1 406,136 Z", fill="url(#h6)", sw=1.2))
    o.append(T(226, 142, "Core", 6.6))
    o.append(_line(252, 140, 278, 136, sw=0.9, color=GREY))
    # shaft and rotor bar
    o.append(_line(340, 136, 340, 190, sw=2.0))
    o.append(_rect(302, 188, 76, 8, fill="#ffffff", sw=1.2))
    for xx in (322, 344, 366):
        o.append(_line(xx, 188, xx, 196, sw=0.8))
    # primary arc
    o.append(_path("M292,166 Q340,142 388,166", sw=11, color=INK))
    o.append(T(430, 174, "Primary", 6.6))
    o.append(_line(426, 172, 390, 166, sw=0.9, color=GREY))
    o.append(T(340, 220, "RVDT", 7.4, color=INK))
    return _mk(38, o, "RVDT rotary displacement transducer",
               "Bo chuyen doi dich chuyen quay RVDT",
               "RVDT rotary displacement transducer",
               "RVDT gom loi cam quay giua cac cuon hinh cung: so cap va hai thu cap",
               "RVDT with a rotating cam-shaped core between arc-shaped primary and secondary coils")


@_reg
def fig_f39():
    """Variable capacitance displacement transducer circuit."""
    o = [_defs()]
    o.append(T(340, 20, "Variable capacitance displacement transducer", 9.4, color=INK))
    # sine wave source and variable capacitor
    o.append(_ar(80, 100, 152, 100, color=BLUE, sw=1.4))
    o.append(T(80, 76, "Sine wave supply input", 6.4))
    o.append(T(80, 86, "ei", 6.8))
    o.append(_line(152, 100, 166, 100, sw=1.2))
    o.append(_cap_h(174, 100, plate=10, gap=5))
    o.append(_ar(174, 80, 174, 92, color=GREY, sw=1.0))
    o.append(T(196, 92, "Cp", 6.8))
    o.append(_line(179, 100, 250, 100, sw=1.2))
    # op-amp with feedback capacitor
    o.append(_poly([(250, 74), (250, 132), (314, 103)], close=True, fill="#ffffff", sw=1.3))
    o.append(T(268, 96, "-", 9.0))
    o.append(T(268, 124, "+", 9.0))
    o.append(_line(250, 118, 230, 118, sw=1.1))
    o.append(_gnd(230, 118))
    o.append(_line(250, 80, 250, 52, sw=1.1))
    o.append(_line(314, 100, 314, 52, sw=1.1))
    o.append(_cap_h(282, 52, plate=10, gap=5))
    o.append(T(282, 38, "C", 7.0))
    o.append(_line(289, 52, 314, 52, sw=1.1))
    o.append(_line(250, 52, 277, 52, sw=1.1))
    # ADC converter and output
    o.append(_line(314, 103, 356, 103, sw=1.2))
    o.append(_b(356, 82, 156, 42, "ADC Converter\n-cum-filter combination", size=6.4))
    o.append(_ar(512, 103, 566, 103, color=RED, sw=1.4))
    o.append(T(580, 100, "eo output", 6.8))
    o.append(T(340, 198, "Cp = rho A / d0, so eo depends on A, d0 or dielectric", 6.2, color=GREY))
    return _mk(39, o, "Variable capacitance displacement transducer circuit",
               "Mach bo chuyen doi dich chuyen dien dung bien doi",
               "Variable capacitance displacement transducer circuit",
               "Mach dung tu bien doi Cp trong phan hoi khuec dai va bo loc ADC cho dau ra eo",
               "Circuit with variable capacitor Cp in amplifier feedback and ADC filter giving output eo")


@_reg
def fig_f40():
    """Moving magnet velocity transducer."""
    o = [_defs()]
    o.append(T(340, 20, "Moving magnet velocity transducer", 9.6, color=INK))
    # stationary coils on both sides
    for x in (250, 390):
        o.append(_rect(x, 86, 40, 92, fill="#ffffff", sw=1.2))
        o.append(_coil_v(x + 10, 92, 172, turns=6, amp=5.0))
        o.append(_coil_v(x + 30, 92, 172, turns=6, amp=5.0))
    # moving magnet rod between the coils
    o.append(_rect(326, 80, 28, 92, fill="#eef3fb", sw=1.3))
    o.append(_line(326, 126, 354, 126, sw=1.0))
    o.append(T(340, 108, "N", 8.4))
    o.append(T(340, 150, "S", 8.4))
    # movement and magnet labels
    o.append(_ar(340, 52, 340, 76, color=RED, sw=1.6))
    o.append(T(400, 58, "Movement", 6.6))
    o.append(_line(396, 58, 344, 58, sw=0.9, color=GREY))
    o.append(T(408, 90, "Magnet", 6.6))
    o.append(_line(404, 90, 356, 88, sw=0.9, color=GREY))
    o.append(T(208, 104, "Coil", 6.8))
    o.append(_line(232, 104, 250, 104, sw=0.9, color=GREY))
    o.append(T(466, 104, "Coil", 6.8))
    o.append(_line(442, 104, 430, 104, sw=0.9, color=GREY))
    # coil terminals and induced emf
    o.append(_line(270, 178, 270, 196, sw=1.1))
    o.append(_line(410, 178, 410, 196, sw=1.1))
    o.append(_port(270, 196))
    o.append(_port(410, 196))
    o.append(_line(270, 196, 302, 196, sw=1.0, color=GREY))
    o.append(_line(378, 196, 410, 196, sw=1.0, color=GREY))
    o.append(_ar(320, 196, 360, 196, color=RED, sw=1.3))
    o.append(T(396, 192, "E", 7.4))
    o.append(T(340, 222, "Induced emf is proportional to the magnet velocity", 6.2, color=GREY))
    return _mk(40, o, "Moving magnet velocity transducer",
               "Bo chuyen doi van toc nam cham di dong",
               "Moving magnet velocity transducer",
               "Nam cham N-S di dong trong khe ho cua hai cuon co dinh sinh ra E ti le van toc",
               "A moving N-S magnet inside two stationary coils inducing an emf E proportional to velocity")
