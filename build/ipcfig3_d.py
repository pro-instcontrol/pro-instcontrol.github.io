# -*- coding: utf-8 -*-
"""Figures 3.55-3.72 for IPC Chapter 3 (liquid level measurement figures)."""
import math

from ipcfig3_common import (BLUE, GREEN, GREY, INK, RED, H, W, T, _ar, _b,
                            _circle, _defs, _ellipse, _fig, _frame, _legend,
                            _line, _path, _poly, _rect, _mk, _series,
                            _wavey, make_registry)

FIGS, _reg = make_registry()


def _valve_h(x, y, fill="#dfe5ec"):
    """Bowtie isolation-valve symbol on a horizontal pipe."""
    return (_poly([(x - 7, y - 6), (x, y), (x - 7, y + 6)],
                  fill=fill, sw=1.0, close=True)
            + _poly([(x + 7, y - 6), (x, y), (x + 7, y + 6)],
                    fill=fill, sw=1.0, close=True))


def _valve_v(x, y, fill="#dfe5ec"):
    """Bowtie isolation-valve symbol on a vertical pipe."""
    return (_poly([(x - 6, y - 7), (x + 6, y - 7), (x, y)],
                  fill=fill, sw=1.0, close=True)
            + _poly([(x - 6, y + 7), (x + 6, y + 7), (x, y)],
                    fill=fill, sw=1.0, close=True))


def _tag(x, y, label, tx, ty, anchor="middle", size=7.2, color=INK):
    """A text label with a thin leader line ending in a dot at the target."""
    return (T(x, y, label, size, anchor=anchor, color=color)
            + _line(x, y + 2, tx, ty, sw=0.6, color=GREY)
            + _circle(tx, ty, 1.0, fill=GREY, sw=0))


def _water(x, y, w, h, step=7, color="#9dbfd6"):
    """Horizontal dashed hatching used for a liquid body."""
    o = []
    yy = float(y)
    while yy <= y + h:
        o.append(_line(x, yy, x + w, yy, sw=0.55, color=color, dash="5,3"))
        yy += step
    return "".join(o)


def _corr(cx, y0, y1, step=6, amp=3):
    """A short corrugated diaphragm line."""
    pts = []
    i = 0
    y = float(y0)
    while y <= y1:
        pts.append((cx + (amp if i % 2 else -amp), y))
        y += step
        i += 1
    return _poly(pts, sw=1.1, color=INK)


# ---------------------------------------------------------------- 3.55
@_reg
def fig_f55():
    """Fig. 3.55 - boiler drum gage glass with insulated chamber."""
    o = [_defs()]
    o.append(_path("M170,58 C108,58 74,84 74,120 C74,156 108,182 170,182 Z",
                   fill="#eef3fb", sw=1.4))
    o.append(_water(80, 118, 86, 60))
    o.append(_line(80, 114, 168, 114, sw=0.9, color=BLUE, dash="5,3"))
    o.append(_line(170, 84, 320, 84, sw=1.4))
    o.append(_line(170, 156, 320, 156, sw=1.4))
    o.append(_valve_h(232, 84))
    o.append(_valve_h(232, 156))
    o.append(_rect(320, 66, 42, 110, fill="url(#h6)", sw=1.3))
    o.append(_line(362, 84, 386, 84, sw=1.3))
    o.append(_line(362, 156, 386, 156, sw=1.3))
    o.append(_rect(386, 76, 20, 92, fill="#fbfaf7", sw=1.3))
    o.append(_water(388, 114, 16, 52, step=6))
    o.append(_line(388, 112, 404, 112, sw=1.0, color=BLUE))
    o.append(_valve_v(396, 178))
    o.append(_line(396, 168, 396, 194, sw=1.2))
    o.append(_tag(122, 40, "Boiler drum", 122, 58))
    o.append(T(122, 96, "Steam", 7.4))
    o.append(T(122, 146, "BFW", 7.4))
    o.append(_tag(200, 48, "Isolation valve", 232, 76))
    o.append(_tag(342, 44, "Insulated chamber", 340, 66))
    o.append(_tag(456, 100, "Gage glass", 406, 100, anchor="start"))
    o.append(_tag(456, 182, "Drain", 396, 188, anchor="start"))
    return _mk(55, o, "Boiler drum gage glass",
               "Kin hien thi boi hoi nuoi bang buong cach nhiet va van xa",
               "Boiler drum gage glass with insulated chamber and drain",
               "So do kin hien thi muc nuoi noi voi tang hoi va nuoi bang buong cach nhiet, co van xa duoi",
               "Gage glass on a boiler drum, connected through isolation valves to an insulated chamber with a drain")


# ---------------------------------------------------------------- 3.56
@_reg
def fig_f56():
    """Fig. 3.56 - remote level indicator with temperature equalising column."""
    o = [_defs()]
    o.append(_path("M160,48 C100,48 64,72 64,100 C64,130 100,152 160,152 Z",
                   fill="#eef3fb", sw=1.4))
    o.append(_water(70, 106, 86, 42))
    o.append(_line(70, 102, 158, 102, sw=0.9, color=BLUE, dash="5,3"))
    o.append(_line(160, 72, 248, 72, sw=1.3))
    o.append(_line(160, 132, 248, 132, sw=1.3))
    o.append(_valve_h(208, 72))
    o.append(_valve_h(208, 132))
    o.append(_rect(248, 60, 42, 42, fill="url(#h6)", sw=1.3))
    o.append(_line(268, 64, 268, 94, sw=1.0, color=BLUE))
    o.append(_line(290, 84, 326, 84, sw=1.3))
    o.append(_line(326, 84, 326, 190, sw=1.3))
    o.append(_line(290, 132, 358, 132, sw=1.3))
    o.append(_line(358, 132, 358, 190, sw=1.3))
    o.append(_path("M326,190 H358", sw=3.0, color=RED))
    o.append(_line(358, 152, 410, 152, sw=1.3))
    o.append(_rect(410, 118, 26, 78, fill="#fbfaf7", sw=1.3))
    o.append(_rect(412, 150, 22, 44, fill="#e6b7ae", sw=0))
    for yy in (126, 138, 162, 174, 186):
        o.append(_line(412, yy, 434, yy, sw=0.5, color=GREY))
    o.append(_tag(112, 36, "Boiler drum", 112, 48))
    o.append(T(112, 88, "Steam", 7.4))
    o.append(T(112, 124, "BFW", 7.4))
    o.append(_tag(330, 54, "Temperature equalising column", 288, 70,
                  anchor="start"))
    o.append(_tag(330, 96, "Overflow tube", 268, 92, anchor="start"))
    o.append(_tag(340, 216, "Red colour liquid (Sudan IV)", 342, 190))
    o.append(_tag(492, 156, "Remote indicator", 436, 156, anchor="start"))
    return _mk(56, o, "Remote level indicator",
               "Chi bao muc tu xa co cot can bang nhiet do va chat do mau",
               "Remote boiler level indicator with equalising column",
               "So do boiler drum noi voi cot can bang nhiet do, ong tran va chi bao tu xa co chat long do mau",
               "Remote indicator fed from a boiler drum through a temperature equalising column and overflow tube")


# ---------------------------------------------------------------- 3.57
@_reg
def fig_f57():
    """Fig. 3.57 - water column with probes, detection box and display unit."""
    o = [_defs()]
    o.append(_path("M70,62 Q70,48 100,48 Q130,48 130,62 V150 Q130,164 100,164 "
                   "Q70,164 70,150 Z", fill="#fbfaf7", sw=1.3))
    o.append(_water(72, 110, 56, 50))
    for yy in (72, 88, 104, 120, 136):
        o.append(_line(100, yy, 128, yy, sw=1.2, color=BLUE))
        o.append(_line(118, yy - 4, 118, yy + 4, sw=0.9, color=INK))
    o.append(_line(40, 64, 70, 64, sw=1.3))
    o.append(_ar(40, 64, 68, 64, color=BLUE))
    o.append(_line(40, 134, 70, 134, sw=1.3))
    o.append(_ar(40, 134, 68, 134, color=BLUE))
    o.append(_line(100, 164, 100, 180, sw=1.3))
    o.append(_ar(100, 164, 100, 178, color=GREEN))
    o.append(_poly([(208, 184), (338, 184), (358, 196), (228, 196)],
                   fill="#eef3fb", sw=1.3, close=True))
    o.append(_poly([(208, 184), (338, 184), (338, 214), (208, 214)],
                   fill="#eef3fb", sw=1.3, close=True))
    o.append(_poly([(338, 184), (358, 196), (358, 226), (338, 214)],
                   fill="#dfe5ec", sw=1.3, close=True))
    o.append(T(273, 203, "Detection Box", 7.6))
    o.append(_poly([(130, 80), (182, 80), (182, 190), (208, 190)], sw=1.3,
                   color=BLUE))
    o.append(_poly([(358, 206), (470, 206), (470, 124), (500, 124)], sw=1.3,
                   color=BLUE))
    o.append(_rect(500, 60, 54, 100, fill="#fbfaf7", sw=1.3))
    o.append(_rect(506, 68, 42, 84, fill="#faf6e6", sw=0.8))
    for yy in (76, 86, 96, 106, 116, 126, 136, 146):
        o.append(_line(510, yy, 544, yy, sw=2.0, color=INK))
    o.append(_tag(100, 36, "Water column with probes", 100, 48))
    o.append(_tag(178, 96, "Conducting probes", 122, 104, anchor="start"))
    o.append(_tag(50, 50, "Steam Inlet", 56, 64))
    o.append(_tag(48, 156, "Water Inlet", 56, 134))
    o.append(_tag(130, 178, "Condensate blow down", 102, 172))
    o.append(_tag(198, 168, "Control cable", 186, 150, anchor="start"))
    o.append(_tag(414, 196, "Control cable", 448, 206))
    o.append(_tag(527, 46, "Display unit", 527, 60))
    return _mk(57, o, "Boiler level with probes",
               "He thong ba bo phan: cot nudoc voi dau do, hop phat hien va man hinh hien thi",
               "Conductivity boiler level system overview",
               "So do cot nuoc co cac dau do dan dien noi den hop phat hien va bo phan hien thi qua day dieu khien",
               "Three-unit resistivity level system: probed water column, detection box and remote display")


# ---------------------------------------------------------------- 3.58
@_reg
def fig_f58():
    """Fig. 3.58 - water column with twelve probes and junction box."""
    o = [_defs()]
    o.append(_path("M250,66 Q250,52 295,52 Q340,52 340,66 V158 Q340,172 295,172 "
                   "Q250,172 250,158 Z", fill="#fbfaf7", sw=1.4))
    o.append(_line(250, 66, 340, 66, sw=1.0, color=GREY))
    left = [(70, "12"), (88, "10"), (106, "8"), (124, "6"), (142, "4"), (160, "2")]
    right = [(79, "11"), (97, "9"), (115, "7"), (133, "5"), (151, "3"), (169, "1")]
    for yy, lab in left:
        o.append(_line(212, yy, 250, yy, sw=1.1, color=BLUE))
        o.append(_line(240, yy - 4, 240, yy + 4, sw=0.9))
        o.append(T(206, yy + 2.4, lab, 6.8, anchor="end"))
    for yy, lab in right:
        o.append(_line(340, yy, 378, yy, sw=1.1, color=BLUE))
        o.append(_line(350, yy - 4, 350, yy + 4, sw=0.9))
        o.append(T(386, yy + 2.4, lab, 6.8, anchor="start"))
    o.append(_poly([(212, 70), (212, 212), (270, 212)], sw=1.2, color=GREEN))
    o.append(_poly([(378, 79), (378, 212), (330, 212)], sw=1.2, color=GREEN))
    o.append(_rect(270, 196, 60, 30, fill="#eef3fb", sw=1.3))
    o.append(T(300, 214, "Junction box", 7.2))
    o.append(_tag(456, 92, "Probe", 382, 97, anchor="start"))
    o.append(_tag(452, 214, "Probe cable", 382, 212, anchor="start"))
    return _mk(58, o, "Probed water column",
               "Cot nuoc voi 12 dau do dan dien va hop dau cuoi day probe",
               "Probed water column with junction box",
               "So do cot nuoc co 12 dau do dan dien xep doi den hop dau cuoi va day dan probe",
               "Water column carrying twelve conducting probes wired to a junction box")


# ---------------------------------------------------------------- 3.59
@_reg
def fig_f59():
    """Fig. 3.59 - float and cable level indicator on an open tank."""
    o = [_defs()]
    o.append(_rect(80, 92, 220, 104, fill="#fbfaf7", sw=1.3))
    o.append(_ellipse(190, 92, 110, 16, fill="#ffffff", sw=1.3))
    o.append(_water(82, 132, 216, 62))
    o.append(_line(82, 130, 298, 130, sw=0.9, color=BLUE, dash="5,3"))
    o.append(_ellipse(190, 128, 34, 9, fill="#f0dcb4", sw=1.2))
    o.append(_line(190, 128, 190, 62, sw=1.5, color=INK))
    o.append(_path("M190,60 Q190,44 208,44 Q226,44 226,60", sw=1.5, color=INK))
    o.append(_line(226, 60, 226, 140, sw=1.5, color=INK))
    o.append(_rect(216, 140, 20, 20, fill="#dfe5ec", sw=1.2))
    o.append(_rect(52, 100, 18, 80, fill="#fbfaf7", sw=1.2))
    for yy in (108, 120, 132, 144, 156, 168):
        o.append(_line(52, yy, 61, yy, sw=0.7))
    o.append(_ar(66, 128, 82, 128, color=RED))
    o.append(_tag(380, 56, "Guide for the cable", 214, 46, anchor="start"))
    o.append(_tag(380, 96, "Metallic chain cable", 226, 92, anchor="start"))
    o.append(_tag(300, 128, "Float", 224, 128, anchor="start"))
    o.append(_tag(380, 152, "Indicator weight", 236, 150, anchor="start"))
    o.append(_tag(60, 86, "Indicator scale", 60, 100))
    o.append(_tag(190, 212, "Open tank", 190, 196))
    return _mk(59, o, "Float and cable level indicator",
               "Phao noi tren mat chat long va day xich dan doi trong",
               "Float and cable level indicator in an open tank",
               "So do phao noi tren mat nuoc, day xich qua ray dan va doi trong doi truoc thang chi",
               "A float rides the liquid surface; a metallic chain over a guide balances a counterweight against a scale")


# ---------------------------------------------------------------- 3.60
@_reg
def fig_f60():
    """Fig. 3.60 - purge (bubble) system for level measurement."""
    o = [_defs()]
    o.append(_rect(60, 112, 200, 88, fill="#fbfaf7", sw=1.3))
    o.append(_ellipse(160, 112, 100, 14, fill="#ffffff", sw=1.3))
    o.append(_water(62, 142, 196, 56))
    o.append(_line(62, 140, 258, 140, sw=0.9, color=BLUE, dash="5,3"))
    o.append(_line(20, 154, 62, 154, sw=1.3))
    o.append(_ar(20, 154, 60, 154, color=BLUE))
    o.append(_rect(146, 66, 16, 8, fill="#dfe5ec", sw=1.1))
    o.append(_line(154, 74, 154, 186, sw=3.0, color=INK))
    for yy in (176, 182, 188):
        o.append(_circle(154, yy, 2.4, fill="none", sw=0.8, color=BLUE))
    o.append(_poly([(118, 186), (122, 186), (122, 198), (118, 198)],
                   fill="none", sw=0.9))
    o.append(_ar(120, 187, 120, 197, color=GREY))
    o.append(_ar(120, 198, 120, 187, color=GREY))
    o.append(_poly([(154, 96), (330, 96), (330, 146), (420, 146)], sw=1.3,
                   color=BLUE))
    o.append(_rect(420, 60, 30, 100, fill="#fbfaf7", sw=1.3))
    o.append(_ar(435, 138, 435, 74, color=GREEN))
    for yy in (70, 84, 98, 112, 126, 152):
        o.append(_line(420, yy, 428, yy, sw=0.6))
    o.append(_poly([(154, 126), (300, 126), (300, 184), (340, 184)], sw=1.3,
                   color=BLUE))
    o.append(_rect(340, 152, 16, 36, fill="#fbfaf7", sw=1.2))
    o.append(_ellipse(348, 168, 6, 4, fill="#e0c98f", sw=0.9))
    o.append(_line(356, 184, 468, 184, sw=1.3))
    o.append(_valve_h(392, 184))
    o.append(_ar(468, 184, 408, 184, color=GREEN))
    o.append(_tag(40, 138, "Liquid in", 56, 154))
    o.append(_tag(212, 62, "Bubble pipe", 158, 88, anchor="start"))
    o.append(_tag(286, 42, "Pressure cleaning plug", 160, 66,
                  anchor="start"))
    o.append(_tag(262, 216, "Clearance at least 3 inches from the base",
                  124, 192))
    o.append(_tag(500, 108, "Level indicator", 450, 108, anchor="start"))
    o.append(_tag(348, 138, "Purge rotameter", 348, 152))
    o.append(_tag(470, 172, "Dry and clean air", 440, 184, anchor="start"))
    o.append(_tag(470, 210, "Needle valve for adjustment of flow", 396, 188))
    return _mk(60, o, "Purge bubble level system",
               "He thong thoi khi tao ap suat nguoc de do muc chat long",
               "Purge (bubble) system for level measurement",
               "So do ong thoi khi ngam trong bon, rotameter, van kim dieu chinh va dong ho chi muc",
               "Dry air bubbles through a dip pipe; back pressure measured by a rotameter and level indicator gives level")


# ---------------------------------------------------------------- 3.61
@_reg
def fig_f61():
    """Fig. 3.61 - displacer / buoyancy torque-tube level system."""
    o = [_defs()]
    o.append(_path("M72,84 Q72,48 102,48 Q132,48 132,84 V112 Q132,122 102,122 "
                   "Q72,122 72,112 Z", fill="#eef3fb", sw=1.3))
    o.append(_rect(80, 82, 44, 26, fill="#dfe5ec", sw=1.2))
    o.append(_line(120, 72, 228, 62, sw=2.0, color=INK))
    o.append(_poly([(222, 56), (236, 62), (222, 68)], fill=INK, sw=0,
                   close=True))
    o.append(_rect(240, 50, 90, 22, fill="url(#h6)", sw=1.2))
    for xx in range(246, 330, 7):
        o.append(_line(xx, 52, xx + 4, 70, sw=0.5, color=GREY))
    o.append(_rect(330, 44, 14, 34, fill="#dfe5ec", sw=1.2))
    for yy in (50, 72):
        o.append(_circle(337, yy, 1.6, fill=INK, sw=0))
    o.append(_line(344, 58, 372, 58, sw=1.3))
    o.append(_poly([(344, 52), (360, 58), (344, 64)], fill="none", sw=1.0))
    o.append(_ar(462, 58, 398, 58, color=GREEN))
    o.append(_tag(160, 104, "Float", 126, 96, anchor="start"))
    o.append(_tag(176, 42, "Torque arm", 180, 67))
    o.append(_tag(252, 88, "Knife edge bearing", 230, 66, anchor="start"))
    o.append(_tag(286, 28, "Torque tube assembly", 286, 50))
    o.append(_tag(400, 44, "Outer flange", 344, 52, anchor="start"))
    o.append(_tag(476, 92, "Flapper - Nozzle system", 362, 60,
                  anchor="start"))
    o.append(_tag(476, 112, "Instrument air supply 1.4 kg/cm2", 440, 58,
                  anchor="start"))
    o.append(_path("M92,152 Q92,138 130,138 Q168,138 168,152 V198 Q168,212 130,212 "
                   "Q92,212 92,198 Z", fill="#fbfaf7", sw=1.3))
    o.append(_water(94, 170, 72, 38))
    o.append(_rect(78, 158, 14, 12, fill="url(#h6)", sw=1.0))
    o.append(_rect(168, 158, 14, 12, fill="url(#h6)", sw=1.0))
    o.append(_rect(168, 174, 30, 16, fill="url(#h6)", sw=1.0))
    o.append(_rect(118, 210, 24, 8, fill="url(#h6)", sw=1.0))
    o.append(_tag(232, 150, "Float chamber", 170, 152, anchor="start"))
    o.append(_tag(62, 156, "Main tank flange", 84, 164, anchor="end"))
    o.append(_tag(232, 180, "Torque arm flange", 198, 182, anchor="start"))
    o.append(_tag(232, 214, "Drain flange", 142, 214, anchor="start"))
    return _mk(61, o, "Displacer torque-tube level",
               "Co che phao chinh luu voi ong xoan va he thong vo phun",
               "Displacer and buoyancy torque-tube level system",
               "So do phao hinh tru trong buong phao, can momen, ong xoan va he thong vo phun voi cap khi",
               "Buoyancy displacer in an external chamber turns a torque tube driving a flapper-nozzle with instrument air")


# ---------------------------------------------------------------- 3.62
@_reg
def fig_f62():
    """Fig. 3.62 - differential pressure transmitter in simplest form."""
    o = [_defs()]
    o.append(_rect(306, 60, 36, 118, fill="#eef3fb", sw=1.4))
    o.append(_line(324, 178, 324, 96, sw=2.0, color=INK))
    o.append(_rect(360, 34, 92, 32, fill="#eef3fb", sw=1.3))
    o.append(T(406, 52, "Pneumatic relay", 7.2))
    o.append(_line(342, 70, 360, 60, sw=1.3))
    o.append(_poly([(342, 82), (360, 74)], sw=1.3))
    o.append(_line(342, 96, 354, 84, sw=1.3))
    o.append(_rect(262, 128, 40, 20, fill="none", sw=1.1))
    o.append(_path("M266,132 l6,-4 l6,8 l6,-8 l6,8 l6,-4", sw=0.9,
                   color=GREY))
    o.append(_poly([(280, 148), (280, 160), (324, 160)], sw=1.0, color=GREY))
    o.append(_ar(520, 50, 452, 50, color=GREEN))
    o.append(_ar(342, 166, 420, 166, color=BLUE))
    o.append(_rect(272, 178, 104, 34, fill="#fbfaf7", sw=1.4))
    o.append(_line(324, 179, 324, 211, sw=1.5))
    o.append(_corr(320, 182, 208, step=5, amp=2.4))
    o.append(_poly([(272, 182), (324, 182), (324, 205), (272, 205)],
                   fill="#cdd9e8", sw=0))
    o.append(_poly([(324, 182), (376, 182), (376, 205), (324, 205)],
                   fill="#e6d5cc", sw=0))
    o.append(_tag(424, 88, "Flapper nozzle system", 358, 78,
                  anchor="start"))
    o.append(_tag(528, 46, "Air supply", 480, 50, anchor="start"))
    o.append(_tag(250, 112, "Force bar", 306, 116, anchor="end"))
    o.append(_tag(250, 142, "Feed back bellows", 264, 138, anchor="end"))
    o.append(_tag(430, 162, "Output", 416, 166, anchor="start"))
    o.append(_tag(260, 194, "L.P. side", 274, 194, anchor="end"))
    o.append(_tag(388, 194, "H.P. side", 374, 194, anchor="start"))
    o.append(_tag(324, 224, "Diaphragm", 324, 211))
    return _mk(62, o, "Differential pressure transmitter",
               "Bo truyen ap suat chenh co thanh luc, he thong vo phun va bellows phan hoi",
               "Simplified differential pressure transmitter",
               "So do bo truyen ap suat chenh don gian voi mang, thanh luc, vo phun, relay khi va bellows phan hoi",
               "Simplified DP cell: the sensing diaphragm moves a force bar and flapper; a pneumatic relay and feedback bellows produce the output")


# ---------------------------------------------------------------- 3.63
@_reg
def fig_f63():
    """Fig. 3.63 - DP level schemes for open and closed tanks with 3-valve manifold."""
    o = [_defs()]
    o.append(_rect(40, 62, 120, 106, fill="#fbfaf7", sw=1.3))
    o.append(_ellipse(100, 62, 60, 11, fill="#ffffff", sw=1.3))
    o.append(_water(42, 96, 116, 70))
    o.append(_line(42, 80, 158, 80, sw=0.8, color=BLUE, dash="5,3"))
    o.append(_line(42, 142, 158, 142, sw=0.8, color=BLUE, dash="5,3"))
    o.append(_poly([(176, 80), (176, 142)], sw=1.2, color=GREEN))
    o.append(_ar(176, 82, 176, 94, color=GREEN))
    o.append(_ar(176, 140, 176, 128, color=GREEN))
    o.append(_line(100, 168, 100, 184, sw=1.3))
    o.append(_rect(58, 184, 52, 24, fill="#eef3fb", sw=1.3))
    o.append(T(84, 200, "D.P.", 7.2))
    o.append(_poly([(58, 192), (26, 192)], sw=1.3, color=BLUE))
    o.append(_ar(26, 192, 26, 176, color=BLUE))
    o.append(_tag(168, 76, "Level maximum", 154, 80, anchor="start"))
    o.append(_tag(168, 142, "Level minimum", 154, 142, anchor="start"))
    o.append(_tag(200, 112, "Range", 176, 112, anchor="start"))
    o.append(_tag(30, 168, "Atmosphere", 26, 180, anchor="start"))
    o.append(_tag(84, 216, "D.P. transmitter", 84, 208))
    o.append(_rect(430, 56, 130, 108, fill="#fbfaf7", sw=1.3))
    o.append(_ellipse(495, 56, 65, 11, fill="#ffffff", sw=1.3))
    o.append(_water(432, 92, 126, 70))
    o.append(_line(432, 78, 558, 78, sw=0.8, color=BLUE, dash="5,3"))
    o.append(_line(432, 140, 558, 140, sw=0.8, color=BLUE, dash="5,3"))
    o.append(_poly([(600, 78), (600, 140)], sw=1.2, color=GREEN))
    o.append(_ar(600, 80, 600, 92, color=GREEN))
    o.append(_ar(600, 138, 600, 126, color=GREEN))
    o.append(_line(430, 70, 370, 70, sw=1.3))
    o.append(_valve_h(400, 70))
    o.append(_line(370, 70, 370, 152, sw=1.3))
    o.append(_line(430, 136, 392, 136, sw=1.3))
    o.append(_rect(300, 152, 70, 28, fill="#eef3fb", sw=1.3))
    o.append(T(335, 169, "D.P. transmitter", 6.8))
    o.append(_line(324, 180, 324, 196, sw=1.2))
    o.append(_line(346, 180, 346, 196, sw=1.2))
    o.append(_line(316, 196, 356, 196, sw=1.2))
    o.append(_valve_v(324, 196))
    o.append(_valve_v(346, 196))
    o.append(_valve_h(370, 196))
    o.append(_ar(324, 202, 324, 218, color=GREY))
    o.append(_valve_v(324, 212))
    o.append(_ar(356, 200, 356, 218, color=GREY))
    o.append(_valve_v(356, 212))
    o.append(_tag(574, 74, "Level maximum", 556, 78, anchor="start"))
    o.append(_tag(574, 140, "Level minimum", 556, 140, anchor="start"))
    o.append(_tag(616, 110, "Range", 600, 110, anchor="start"))
    o.append(_tag(408, 42, "Isolation valve", 400, 66))
    o.append(_tag(240, 206, "Equaliser valve", 316, 194, anchor="end"))
    o.append(_tag(404, 194, "3-valve manifold", 372, 196, anchor="start"))
    o.append(_tag(404, 222, "Drain valves", 356, 214, anchor="start"))
    return _mk(63, o, "DP level installations",
               "Lap dat do muc ap suat chenh cho bon ho va bon kin co manifold ba van",
               "DP level measurement on open and closed tanks",
               "So do lap dat bo truyen ap suat chenh cho bon ho va bon kin voi manifold ba van, van can bang va van xa",
               "Open-tank and closed-tank DP level schemes with a three-valve manifold, equaliser valve and drain valves")


# ---------------------------------------------------------------- 3.64
@_reg
def fig_f64():
    """Fig. 3.64 - extended and flat diaphragm capsules."""
    o = [_defs()]
    o.append(_rect(96, 30, 78, 28, fill="#eef3fb", sw=1.3))
    o.append(T(135, 47, "Transmitter unit", 7.2))
    o.append(_path("M135,58 V76", sw=2.0))
    o.append(_ellipse(246, 92, 30, 42, fill="url(#h6)", sw=1.3))
    for ang in (0, 60, 120, 180, 240, 300):
        a = math.radians(ang)
        o.append(_circle(246 + 26 * math.cos(a), 92 + 38 * math.sin(a),
                         2.2, fill="#ffffff", sw=0.8))
    o.append(_rect(276, 76, 78, 32, fill="url(#h6)", sw=1.3))
    o.append(_ellipse(354, 92, 8, 16, fill="#ffffff", sw=1.3))
    o.append(_circle(354, 92, 5, fill="#dfe5ec", sw=0.9))
    o.append(_line(135, 70, 96, 70, sw=1.2))
    o.append(_valve_v(102, 70))
    o.append(_tag(160, 68, "Drain", 106, 70, anchor="start"))
    o.append(_tag(76, 80, "L.P. connection", 104, 72, anchor="end"))
    o.append(_tag(408, 78, "Extended diaphragm capsule (H.P. connection)",
                  356, 92, anchor="start"))
    o.append(_rect(96, 140, 78, 26, fill="#eef3fb", sw=1.3))
    o.append(T(135, 156, "Transmitter unit", 7.2))
    o.append(_path("M135,166 V180", sw=2.0))
    o.append(_ellipse(246, 188, 28, 38, fill="url(#h6)", sw=1.3))
    for ang in (0, 60, 120, 180, 240, 300):
        a = math.radians(ang)
        o.append(_circle(246 + 24 * math.cos(a), 188 + 34 * math.sin(a),
                         2.2, fill="#ffffff", sw=0.8))
    o.append(_ellipse(276, 188, 11, 26, fill="#ffffff", sw=1.3))
    o.append(_ellipse(276, 188, 6, 18, fill="#dfe5ec", sw=0.9))
    o.append(_line(135, 176, 96, 176, sw=1.2))
    o.append(_valve_v(102, 176))
    o.append(_tag(320, 168, "Flat diaphragm capsule (H.P. connection)",
                  282, 188, anchor="start"))
    return _mk(64, o, "Remote diaphragm capsules",
               "Dang mang chup mo rong va mang chup phang cua bo truyen",
               "Extended and flat diaphragm capsules",
               "So do hai kieu mang chup cach ly: kieu mo rong va kieu phang gan truc tiep vao van bon",
               "Two remote seal designs: an extended diaphragm that removes dead cavities and a flush flat diaphragm")


# ---------------------------------------------------------------- 3.65
@_reg
def fig_f65():
    """Fig. 3.65 - internal arrangements of remote diaphragm seals."""
    o = [_defs()]
    o.append(_rect(276, 48, 92, 104, fill="url(#h6)", sw=1.3))
    o.append(_path("M316,38 h16 v10 h-16 Z", fill="#dfe5ec", sw=1.1))
    o.append(_line(324, 34, 324, 38, sw=0.9))
    o.append(_corr(372, 62, 118))
    o.append(_rect(348, 96, 24, 34, fill="#dce9f2", sw=0))
    o.append(_corr(292, 152, 352, step=8, amp=2.5))
    o.append(_rect(252, 152, 140, 10, fill="url(#h6)", sw=1.2))
    o.append(_tag(408, 34, "Pivot and seal", 330, 38, anchor="start"))
    o.append(_tag(456, 78, "Primary diaphragm", 374, 84, anchor="start"))
    o.append(_tag(204, 118, "Isolation liquid", 350, 114, anchor="end"))
    o.append(_tag(408, 158, "Process diaphragm", 352, 156, anchor="start"))
    o.append(_rect(276, 176, 92, 40, fill="url(#h6)", sw=1.3))
    o.append(_path("M316,166 h16 v10 h-16 Z", fill="#dfe5ec", sw=1.1))
    o.append(_line(324, 162, 324, 166, sw=0.9))
    o.append(_line(252, 184, 276, 184, sw=1.3))
    o.append(_circle(252, 184, 2.5, fill="#ffffff", sw=0.9))
    o.append(_line(248, 200, 276, 200, sw=1.3))
    o.append(_valve_h(258, 200))
    o.append(_corr(270, 186, 208, step=5, amp=2.0))
    o.append(_corr(372, 180, 212, step=5, amp=2.5))
    o.append(_rect(348, 194, 24, 22, fill="#dce9f2", sw=0))
    o.append(_corr(292, 218, 352, step=8, amp=2.5))
    o.append(_rect(252, 218, 140, 8, fill="url(#h6)", sw=1.2))
    o.append(_tag(180, 178, "Air vent", 254, 184, anchor="end"))
    o.append(_tag(172, 200, "Compensating connection", 250, 200,
                  anchor="end"))
    o.append(_tag(408, 194, "Compensating diaphragm", 272, 198,
                  anchor="start"))
    o.append(_tag(456, 180, "Primary diaphragm", 374, 186, anchor="start"))
    o.append(_tag(204, 220, "Isolation liquid", 350, 204, anchor="end"))
    o.append(_tag(408, 222, "Process diaphragm", 352, 218, anchor="start"))
    return _mk(65, o, "Remote seal internal details",
               "Mat cat ben trong cua mang chup tu xa co chat long cach ly va mang bu",
               "Internal arrangement of remote diaphragm seals",
               "So do mat cat hai kieu dau noi mang: co mang chup chinh, mang bu va chat long cach ly",
               "Cross-sections of remote seals showing the primary and compensating diaphragms, isolating liquid and process diaphragm")


# ---------------------------------------------------------------- 3.66
@_reg
def fig_f66():
    """Fig. 3.66 - capacitance type level measurement installation."""
    o = [_defs()]
    o.append(_rect(140, 76, 180, 122, fill="#fbfaf7", sw=1.4))
    o.append(_ellipse(230, 76, 90, 15, fill="#ffffff", sw=1.4))
    o.append(_water(142, 130, 176, 66))
    o.append(_line(142, 128, 318, 128, sw=0.9, color=BLUE, dash="5,3"))
    o.append(_rect(214, 40, 32, 26, fill="#eef3fb", sw=1.3))
    o.append(_rect(222, 66, 16, 112, fill="#f6f2e6", sw=1.1))
    o.append(_line(230, 66, 230, 176, sw=1.6, color=INK))
    o.append(_line(246, 168, 246, 182, sw=1.3))
    o.append(_line(258, 168, 258, 182, sw=1.3))
    o.append(_poly([(246, 176), (258, 176)], sw=1.3, color=BLUE))
    o.append(_poly([(246, 64), (356, 64), (356, 84), (420, 84)], sw=1.3,
                   color=BLUE))
    o.append(_rect(420, 70, 80, 28, fill="#eef3fb", sw=1.3))
    o.append(_circle(440, 84, 8, fill="#ffffff", sw=1.0))
    o.append(_ar(440, 90, 444, 78, color=RED))
    o.append(_tag(230, 28, "Probe head", 230, 40))
    o.append(_tag(104, 104, "Probe", 222, 116, anchor="end"))
    o.append(_tag(460, 56, "Electronic Indicator", 460, 70))
    o.append(_tag(354, 158, "Tank", 320, 158, anchor="start"))
    return _mk(66, o, "Capacitance level probe",
               "Dau do dien dung duoc dat cung chot tren dinh bon va noi voi bo chi",
               "Capacitance type level measurement",
               "So do bon chua co dau do dien dung duoc giu cung tren dinh, cap vao bo thiet bi dien tu hien thi",
               "A rigid insulated probe forms a capacitor with the tank wall; the changing capacitance drives an electronic indicator")


# ---------------------------------------------------------------- 3.67
@_reg
def fig_f67():
    """Fig. 3.67 - capacitance level electronic circuit block diagram."""
    o = [_defs()]
    o.append(T(40, 44, "230 V", 7.4, anchor="start"))
    o.append(T(40, 58, "A.C.", 7.4, anchor="start"))
    o.append(_circle(102, 44, 2.6, fill="none", sw=1.0))
    o.append(_circle(102, 58, 2.6, fill="none", sw=1.0))
    o.append(_line(104, 44, 160, 44, sw=1.3))
    o.append(_line(104, 58, 160, 58, sw=1.3))
    o.append(_b(160, 30, 190, 42,
                "Power supply unit\n(Transformer and rectifier)", size=7.0))
    o.append(_ar(30, 130, 68, 130, color=GREEN))
    o.append(T(30, 120, "Probe", 7.2, anchor="start"))
    o.append(_b(70, 110, 110, 42, "Oscillator\ncircuit", size=7.4))
    o.append(_b(230, 110, 120, 42, "Sensing\namplifier", size=7.4))
    o.append(_rect(400, 110, 130, 42, fill="#eef3fb", sw=1.2))
    o.append(_line(400, 110, 530, 152, sw=1.0))
    o.append(T(435, 126, "Relay unit", 7.2))
    o.append(T(470, 144, "Trans-ducer unit", 7.0))
    o.append(_line(180, 131, 230, 131, sw=1.3, color=BLUE))
    o.append(_line(350, 131, 400, 131, sw=1.3, color=BLUE))
    o.append(_line(200, 72, 125, 110, sw=1.2))
    o.append(_line(268, 72, 288, 110, sw=1.2))
    o.append(_poly([(330, 72), (468, 72), (468, 110)], sw=1.2))
    return _mk(67, o, "Capacitance circuit blocks",
               "So khoi mach dieu khien: nguon, bo dao dong, khuong khuech dai va relay",
               "Capacitance level electronic circuit",
               "So do khoi mach gom nguon 230 V, bo dao dong noi dau do, bo khuech dai tin hieu va relay hoac bo transducer",
               "Block diagram: a 230 V supply feeds the probe oscillator, sensing amplifier and relay or transducer unit")


# ---------------------------------------------------------------- 3.68
@_reg
def fig_f68():
    """Fig. 3.68 - magnetic level gauge float with inner and outer magnets."""
    o = [_defs()]
    o.append(_line(160, 92, 420, 92, sw=0.9, color=BLUE, dash="6,4"))
    o.append(_path("M252,84 Q252,46 292,46 Q332,46 332,84 V108 Q332,146 292,146 "
                   "Q252,146 252,108 Z", fill="#fbfaf7", sw=1.4))
    o.append(_rect(254, 82, 76, 20, fill=INK, sw=0))
    o.append(_rect(174, 80, 232, 24, fill="#ecf0f5", sw=1.2))
    o.append(_rect(254, 80, 76, 24, fill=INK, sw=0))
    o.append(_line(174, 92, 406, 92, sw=0.6, color=GREY))
    o.append(_tag(178, 52, "Float", 258, 62, anchor="end"))
    o.append(_tag(418, 72, "Inner magnet", 332, 92, anchor="start"))
    o.append(_tag(476, 116, "Outer magnet", 404, 92, anchor="start"))
    return _mk(68, o, "Magnetic float and magnets",
               "Phao co nam cham ben trong va nam cham ben ngoai di theo muc chat long",
               "Magnetic gauge float with inner and outer magnets",
               "So do phao hinh tru co nam cham dat ben trong, doi theo nam cham ben ngoai buong phao",
               "A cylindrical float carrying an inner magnet follows the level and couples to an outer indicating magnet")


# ---------------------------------------------------------------- 3.69
@_reg
def fig_f69():
    """Fig. 3.69 - magnetic level gauge installed on a main tank."""
    o = [_defs()]
    o.append(_path("M100,40 C70,80 70,150 100,192", sw=1.3, color=GREY,
                   dash="6,4"))
    o.append(_line(96, 80, 200, 80, sw=1.3))
    o.append(_line(96, 150, 200, 150, sw=1.3))
    o.append(_valve_h(142, 80))
    o.append(_valve_h(142, 150))
    o.append(_path("M202,84 Q202,48 240,48 Q278,48 278,84 V166 Q278,178 240,178 "
                   "Q202,178 202,166 Z", fill="#fbfaf7", sw=1.4))
    o.append(_water(204, 150, 72, 24))
    o.append(_rect(218, 98, 44, 28, fill="#fbfaf7", sw=1.2))
    o.append(_rect(218, 108, 44, 8, fill=INK, sw=0))
    o.append(_line(240, 178, 240, 196, sw=1.2))
    o.append(_valve_v(240, 192))
    o.append(_tag(42, 68, "Main tank", 88, 70, anchor="start"))
    o.append(_tag(142, 58, "Isolation valves", 142, 76))
    o.append(_tag(326, 96, "Float", 262, 102, anchor="start"))
    o.append(_tag(326, 120, "Magnet embedded", 262, 112, anchor="start"))
    o.append(_tag(326, 162, "Float chamber", 280, 160, anchor="start"))
    o.append(_tag(300, 196, "Drain valve", 246, 192, anchor="start"))
    return _mk(69, o, "Magnetic gauge installation",
               "Lap dat buong phao tu tinh vao bon chinh qua van cach ly co van xa day",
               "Magnetic level gauge installation",
               "So do buong phao duoc noi voi bon chinh bang hai van cach ly, co phao nam cham ben trong va van xa",
               "Magnetic float chamber connected to the main tank by two isolation valves with a bottom drain valve")


# ---------------------------------------------------------------- 3.70
@_reg
def fig_f70():
    """Fig. 3.70 - wafer indicator of a magnetic level gauge."""
    o = [_defs()]
    o.append(_path("M120,90 Q120,50 156,50 Q192,50 192,90 V150 Q192,190 156,190 "
                   "Q120,190 120,150 Z", sw=1.2, color=GREY, dash="6,4"))
    o.append(_rect(128, 96, 56, 28, fill="#fbfaf7", sw=1.2))
    o.append(_rect(128, 106, 56, 8, fill=INK, sw=0))
    o.append(_rect(214, 60, 34, 124, fill="#fbfaf7", sw=1.3))
    for yy in (70, 82, 94, 106):
        o.append(_poly([(219, yy), (231, yy + 6), (219, yy + 12)],
                       fill="none", sw=1.2))
    for yy in (126, 138, 150, 162, 174):
        o.append(_poly([(219, yy), (231, yy + 6), (219, yy + 12)],
                       fill=INK, sw=0, close=True))
    o.append(_tag(286, 70, "Wafer indicator", 248, 70, anchor="start"))
    o.append(_tag(286, 100, "Yellow wafer", 233, 100, anchor="start"))
    o.append(_tag(286, 152, "Black wafer", 233, 152, anchor="start"))
    return _mk(70, o, "Magnetic wafer indicator",
               "Day wafer hai mau lat 180 do theo phao tu tinh de chi muc chat long",
               "Magnetic gauge wafer indicator",
               "So do day wafer hai mau: wafer vang chi phan hoi, wafer den chi phan chat long theo chuyen dong cua phao",
               "Twin-colour wafers flip as the magnetic float passes: yellow marks vapour space and black marks liquid level")


# ---------------------------------------------------------------- 3.71
@_reg
def fig_f71():
    """Fig. 3.71 - nucleonic level measurement arrangement."""
    o = [_defs()]
    o.append(_path("M80,86 h28 v26 h-28 Z", fill="#eef3fb", sw=1.3))
    o.append(_line(88, 86, 88, 78, sw=1.2))
    o.append(_rect(84, 74, 8, 4, fill=INK, sw=0))
    o.append(_rect(200, 65, 180, 110, fill="#fbfaf7", sw=1.3))
    o.append(_ellipse(290, 65, 90, 13, fill="#ffffff", sw=1.3))
    o.append(_water(202, 112, 176, 61))
    o.append(_line(202, 110, 378, 110, sw=0.9, color=BLUE, dash="5,3"))
    o.append(_line(108, 100, 402, 78, sw=1.1, color=RED, dash="6,4"))
    o.append(_line(108, 100, 402, 126, sw=1.1, color=RED, dash="6,4"))
    o.append(_path("M402,66 Q418,66 414,88 Q410,110 420,118 Q414,142 402,142 "
                   "Q390,142 394,118 Q404,110 400,88 Q396,66 402,66 Z",
                   fill="url(#h6)", sw=1.3))
    o.append(_line(420, 104, 522, 104, sw=1.3))
    o.append(_rect(522, 90, 78, 28, fill="#eef3fb", sw=1.3))
    o.append(T(561, 107, "Control unit", 7.2))
    o.append(_tag(94, 136, "Source unit", 96, 112))
    o.append(_tag(268, 56, "Range of radiation", 268, 88))
    o.append(_tag(500, 66, "Detector unit", 412, 78, anchor="start"))
    return _mk(71, o, "Nucleonic level measurement",
               "Nguon phong xa chieu qua bon den dau do va bo dieu khien",
               "Nucleonic level measurement arrangement",
               "So do nguon Co-60 phat tia gamma qua bon chua, dau do o ben kia va bo dieu khien hien thi",
               "A gamma source projects a radiation beam through the vessel to a detector whose signal is sent to a control unit")


# ---------------------------------------------------------------- 3.72
@_reg
def fig_f72():
    """Fig. 3.72 - radiation danger warning sign."""
    o = [_defs()]
    o.append(_rect(210, 24, 260, 190, fill="#ffffff", sw=1.6))
    o.append(_rect(240, 44, 200, 130, fill="none", sw=1.2))
    o.append(T(340, 62, "Danger radiation", 8.2))
    cx, cy = 340, 116
    for ang in (-90, 30, 150):
        pts = []
        r0, r1, half = 10.0, 36.0, 26.0
        for i in range(9):
            a = math.radians(ang - half + 2 * half * i / 8.0)
            pts.append((cx + r1 * math.cos(a), cy + r1 * math.sin(a)))
        for i in range(8, -1, -1):
            a = math.radians(ang - half + 2 * half * i / 8.0)
            pts.append((cx + r0 * math.cos(a), cy + r0 * math.sin(a)))
        o.append(_poly(pts, fill=INK, sw=0, close=True))
    o.append(_circle(cx, cy, 9, fill="#ffffff", sw=0))
    o.append(T(340, 158, "Obtain safety permit", 7.8))
    o.append(T(340, 170, "before entering", 7.8))
    return _mk(72, o, "Radiation danger sign",
               "Bien bao hiem nguy phong xa va yeu cau giay phep truoc khi vao",
               "Radiation danger warning sign",
               "So do bien bao co bien tuong tron phong xa, dong chu Danger radiation va can giay phep truoc khi vao",
               "Warning placard with the trefoil radiation symbol, the words Danger radiation and a safety-permit notice")
