# -*- coding: utf-8 -*-
"""Figure supplier D for IPC Chapter 8: figures 8.27-8.34 (PDF pp. 380-390).

Each figure is a simplified vector redraw of the printed raster diagram:
packaged and modular PLC units, PC programming link, two ladder diagrams,
DCS architecture, DCS hardware interconnection and a controller slot.
"""
from ipcfig8_common import (BLUE, GREEN, GREY, INK, RED, H, W, T, _ar, _b,
                            _circle, _defs, _ellipse, _fig, _frame, _legend,
                            _line, _path, _poly, _rect, _mk, _series,
                            _wavey, make_registry)

FIGS, _reg = make_registry()


def _no(x, y, h=15):
    """A normally-open ladder contact centred on (x, y)."""
    return "".join((_line(x - 16, y, x - 5, y),
                    _line(x - 5, y - h / 2.0, x - 5, y + h / 2.0),
                    _line(x + 5, y - h / 2.0, x + 5, y + h / 2.0),
                    _line(x + 5, y, x + 16, y)))


def _nc(x, y, h=15):
    """A normally-closed ladder contact centred on (x, y)."""
    return _no(x, y, h) + _line(x - 7, y + 7, x + 7, y - 7)


def _sw(x, y, label, size=6.4):
    """An open switch contact with a printed terminal label above."""
    return "".join((_line(x - 16, y, x - 10, y),
                    _circle(x - 10, y, 2.2, fill="#ffffff"),
                    _circle(x + 10, y, 2.2, fill="#ffffff"),
                    _line(x - 8, y - 1, x + 8, y - 9),
                    _line(x + 10, y, x + 16, y),
                    T(x, y - 13, label, size)))


def _coil(x, y, label, rx=17, ry=10, size=7.0, above=True):
    """A ladder output coil and its label."""
    yy = y - 15 if above else y + 17
    return _ellipse(x, y, rx, ry) + T(x, yy, label, size)


def _rails(xl, xr, y0, y1, n1="1", n2="2"):
    o = [_line(xl, y0, xl, y1, sw=1.3), _line(xr, y0, xr, y1, sw=1.3)]
    for xx in (xl, xr):
        o.append(_circle(xx, y0, 2.4, fill="#ffffff"))
        o.append(_circle(xx, y1, 2.4, fill="#ffffff"))
    o.append(T(xl + 13, y0 + 4, n1, 6.0))
    o.append(T(xr + 13, y0 + 4, n2, 6.0))
    o.append(T(xl + 13, y1 + 5, n1, 6.0))
    o.append(T(xr + 13, y1 + 5, n2, 6.0))
    return "".join(o)


def _txcircle(cx, cy):
    o = [_circle(cx, cy, 8, fill="#ffffff"),
         _line(cx - 5, cy - 5, cx + 5, cy + 5),
         _line(cx + 5, cy - 5, cx - 5, cy + 5)]
    return "".join(o)


def _valve(cx, cy):
    return "".join((_poly([(cx - 7, cy - 6), (cx, cy), (cx - 7, cy + 6)],
                          sw=1.1),
                    _poly([(cx + 7, cy - 6), (cx, cy), (cx + 7, cy + 6)],
                          sw=1.1),
                    _line(cx, cy + 6, cx, cy + 11)))


@_reg
def fig_f27():
    """Fig 8.27: packaged micro PLC with input switches, outputs and supply."""
    o = [_defs()]
    o.append(T(340, 13, "Packaged PLC unit for the interlock example", 8.6))
    o.append(_rect(238, 24, 190, 118))
    o.append(T(333, 38, "Micro PLC", 8.2))
    for i, lab in enumerate(("1 – 0", "1 – 1", "1 – 2")):
        o.append(_b(256, 50 + i * 22, 38, 16, lab, size=6.8))
    for i, lab in enumerate(("0 – 0", "0 – 1", "0 – 2")):
        o.append(_b(372, 50 + i * 22, 38, 16, lab, size=6.8))
    o.append(_line(150, 58, 150, 164, sw=1.2))
    for yy in (58, 80):
        o.append(_line(150, yy, 164, yy, sw=1.2))
        o.append(_circle(164, yy, 2.2, fill="#ffffff"))
        o.append(_line(166, yy - 1, 182, yy - 8, sw=1.2))
        o.append(_circle(186, yy, 2.2, fill="#ffffff"))
        o.append(_line(186, yy, 294, yy, sw=1.2))
    for yy, lab in ((58, "SV1"), (80, "SV2")):
        o.append(_line(410, yy, 470, yy, sw=1.2))
        o.append(_b(470, yy - 8, 40, 16, lab, size=7.2))
    for xx in (282, 384):
        o.append(_line(xx, 142, xx, 150, sw=1.0, dash="3 3", color=GREY))
    o.append(_rect(238, 150, 190, 40))
    o.append(T(333, 170, "Power supply unit", 7.8))
    o.append(T(246, 160, "+", 7.0))
    o.append(T(246, 179, "−", 7.0))
    o.append(_line(150, 164, 238, 164, sw=1.2))
    o.append(_line(210, 190, 210, 178, sw=1.1))
    o.append(_line(202, 178, 218, 178, sw=1.0))
    o.append(_line(205, 183, 215, 183, sw=1.0))
    o.append(_line(208, 188, 212, 188, sw=1.0))
    o.append(_line(428, 160, 470, 160, sw=1.2))
    o.append(_circle(472, 160, 2.0, fill="#ffffff"))
    o.append(_line(428, 179, 470, 179, sw=1.2))
    o.append(_circle(472, 179, 2.0, fill="#ffffff"))
    o.append(T(548, 169, "230 volt A.C.", 7.2))
    return _mk(
        27, o, "Packaged micro PLC unit",
        "Sơ đồ PLC dạng gói với các tiếp điểm vào, đầu ra SV1, SV2 và bộ nguồn",
        "Packaged PLC with input switches, SV1/SV2 outputs and power supply unit",
        "Sơ đồ PLC gói gồm các cổng vào 1 – 0 đến 1 – 2, cổng ra 0 – 0 đến 0 – 2 và bộ nguồn",
        "Packaged PLC unit showing input terminals, output terminals driving SV1 and SV2, and the power supply")


@_reg
def fig_f28():
    """Fig 8.28: modular PLC with power supply, CPU and eight I/O slots."""
    o = [_defs()]
    o.append(T(340, 13, "Modular PLC: power supply, CPU and eight I/O slots", 8.6))
    o.append(T(135, 24, "230 volt A.C.", 7.0))
    o.append(_line(118, 30, 118, 55, sw=1.1))
    o.append(_circle(118, 30, 2.0, fill="#ffffff"))
    o.append(_line(152, 30, 152, 55, sw=1.1))
    o.append(_circle(152, 30, 2.0, fill="#ffffff"))
    o.append(_rect(90, 55, 500, 95))
    o.append(_line(185, 55, 185, 150, sw=1.1))
    o.append(_line(295, 55, 295, 150, sw=1.1))
    o.append(T(137, 95, "Power supply", 7.2))
    o.append(T(137, 106, "module", 7.2))
    o.append(T(240, 95, "Microprocessor", 7.0))
    o.append(T(240, 106, "unit", 7.0))
    for i in range(9):
        xx = 295 + i * 37.0
        o.append(_line(xx, 55, xx, 150, sw=0.8, dash="4 3", color=GREY))
    o.append(T(443, 70, "I/O modules from 0 to 7", 7.4))
    o.append(_ar(305, 80, 580, 80, color=BLUE, sw=1.2))
    o.append(_ar(580, 80, 305, 80, color=BLUE, sw=1.2))
    o.append(_ar(293, 122, 268, 122, color=BLUE, sw=1.2))
    for i in range(8):
        o.append(T(313.5 + i * 37.0, 164, str(i), 6.8))
    return _mk(
        28, o, "Modular PLC unit in a rack",
        "Sơ đồ PLC dạng mô-đun gồm bộ nguồn, bộ vi xử lý và tám khe I/O từ 0 đến 7",
        "Modular PLC rack with power supply module, microprocessor unit and I/O modules 0 to 7",
        "Sơ đồ PLC mô-đun: bộ nguồn, bộ vi xử lý và các mô-đun I/O được lắp trên giá từ khe 0 đến 7",
        "Modular PLC rack with a power supply module, a microprocessor unit and eight interchangeable I/O modules")


@_reg
def fig_f29():
    """Fig 8.29: PC-based programming unit linked to the PLC PCBs."""
    o = [_defs()]
    o.append(T(340, 13, "PC-based programming and SCADA link", 8.6))
    o.append(_b(90, 105, 95, 44, "Power supply\nPCB", size=7.2))
    o.append(_b(185, 105, 120, 44, "Microprocessor\nPCB", size=7.2))
    o.append(_b(305, 105, 155, 44, "I/O modules PCB", size=7.4))
    o.append(_ar(440, 127, 482, 127, color=BLUE, sw=1.3))
    o.append(_b(210, 30, 140, 44, "Personal computer\nwith keyboard", size=7.2))
    o.append(_b(370, 34, 95, 36, "Monitor", size=7.8))
    o.append(_line(350, 52, 370, 52, sw=1.1))
    o.append(_line(280, 74, 280, 90, sw=1.1))
    o.append(_ar(280, 90, 245, 90, color=BLUE, sw=1.3))
    o.append(_ar(245, 90, 245, 105, color=BLUE, sw=1.3))
    o.append(T(300, 84, "programming", 6.2, color=BLUE))
    return _mk(
        29, o, "Personal computer used as PLC programming unit",
        "Sơ đồ máy tính cá nhân có bàn phím và màn hình lập trình cho PLC qua PCB vi xử lý",
        "PC with keyboard and monitor connected to the PLC microprocessor PCB",
        "Sơ đồ hệ thống lập trình PLC bằng máy tính cá nhân có bàn phím, màn hình và phần mềm SCADA",
        "Personal computer with keyboard and monitor linked to the PLC power supply, microprocessor and I/O PCBs")


@_reg
def fig_f30():
    """Fig 8.30: relay interlock ladder with LLS/HLS and SV1/SV2 coils."""
    o = [_defs()]
    o.append(_rails(60, 620, 22, 210))
    o.append(_line(60, 56, 154, 56, sw=1.2))
    o.append(_sw(170, 56, "LLS"))
    o.append(_line(186, 56, 432, 56, sw=1.2))
    o.append(_coil(450, 56, "R1"))
    o.append(_line(467, 56, 620, 56, sw=1.2))
    o.append(T(148, 70, "1", 5.8))
    o.append(T(196, 70, "3", 5.8))
    o.append(T(418, 42, "1", 5.8, anchor="end"))

    o.append(_line(60, 92, 154, 92, sw=1.2))
    o.append(_sw(170, 92, "HLS"))
    o.append(_line(186, 92, 432, 92, sw=1.2))
    o.append(_coil(450, 92, "R2"))
    o.append(_line(467, 92, 620, 92, sw=1.2))
    o.append(T(148, 106, "1", 5.8))
    o.append(T(196, 106, "4", 5.8))

    o.append(_line(60, 126, 154, 126, sw=1.2))
    o.append(_no(170, 126))
    o.append(_line(186, 126, 452, 126, sw=1.2))
    o.append(_coil(470, 126, "SV1"))
    o.append(_line(487, 126, 620, 126, sw=1.2))
    o.append(T(170, 145, "1R1", 6.2))
    o.append(_line(130, 126, 130, 152, sw=1.1))
    o.append(_line(130, 152, 154, 152, sw=1.1))
    o.append(_nc(170, 152))
    o.append(_line(186, 152, 205, 152, sw=1.1))
    o.append(_line(205, 152, 205, 126, sw=1.1))
    o.append(T(170, 171, "2R2", 6.2))
    o.append(T(212, 158, "6", 5.8))
    o.append(T(447, 142, "7", 5.8))
    o.append(T(495, 142, "2", 5.8))

    o.append(_line(60, 190, 154, 190, sw=1.2))
    o.append(_no(170, 190))
    o.append(_line(186, 190, 452, 190, sw=1.2))
    o.append(_coil(470, 190, "SV2"))
    o.append(_line(487, 190, 620, 190, sw=1.2))
    o.append(T(170, 178, "1R2", 6.2))
    o.append(T(447, 178, "5", 5.8))
    o.append(T(495, 178, "2", 5.8))
    return _mk(
        30, o, "Relay interlock ladder for overhead tank level control",
        "Sơ đồ bậc thang liên khóa bằng relay gồm công tắc LLS, HLS, tiếp điểm 1R1, 2R2, 1R2 và cuộn SV1, SV2",
        "Relay interlock ladder with LLS, HLS switches, 1R1/2R2/1R2 contacts and R1/R2/SV1/SV2 coils",
        "Sơ đồ bậc thang điều khiển mức bể: LLS và HLS điều khiển relay R1, R2; 1R1 và 2R2 điều khiển SV1; 1R2 điều khiển SV2",
        "Four-rung relay ladder: LLS energises R1, HLS energises R2, contact 1R1 in parallel with NC 2R2 energises SV1, and 1R2 energises SV2")


@_reg
def fig_f31():
    """Fig 8.31: equivalent PLC ladder program with four address-labelled rungs."""
    o = [_defs()]
    o.append(_rails(60, 620, 20, 212))
    for i, yy in enumerate((48, 88, 128, 182), 1):
        o.append(T(22, yy + 3, "rung %d" % i, 6.6, anchor="start"))
    o.append(_line(60, 48, 144, 48, sw=1.2))
    o.append(_no(160, 48))
    o.append(_line(176, 48, 462, 48, sw=1.2))
    o.append(_coil(480, 48, "0:000/00", rx=26))
    o.append(_line(506, 48, 620, 48, sw=1.2))
    o.append(T(160, 68, "I:000/00", 6.6))

    o.append(_line(60, 88, 144, 88, sw=1.2))
    o.append(_no(160, 88))
    o.append(_line(176, 88, 462, 88, sw=1.2))
    o.append(_coil(480, 88, "0:001/00", rx=26))
    o.append(_line(506, 88, 620, 88, sw=1.2))
    o.append(T(160, 108, "I:001/00", 6.6))

    o.append(_line(60, 128, 144, 128, sw=1.2))
    o.append(_no(160, 128))
    o.append(_line(176, 128, 454, 128, sw=1.2))
    o.append(_coil(480, 128, "0:002/00", rx=26, above=False))
    o.append(_line(506, 128, 620, 128, sw=1.2))
    o.append(T(160, 146, "0:000/01", 6.4))
    o.append(_line(130, 128, 130, 154, sw=1.1))
    o.append(_line(130, 154, 144, 154, sw=1.1))
    o.append(_nc(160, 154))
    o.append(_line(176, 154, 205, 154, sw=1.1))
    o.append(_line(205, 154, 205, 128, sw=1.1))
    o.append(T(160, 171, "0:001/02", 6.4))

    o.append(_line(60, 182, 144, 182, sw=1.2))
    o.append(_no(160, 182))
    o.append(_line(176, 182, 454, 182, sw=1.2))
    o.append(_coil(480, 182, "0:003/00", rx=26, above=False))
    o.append(_line(506, 182, 620, 182, sw=1.2))
    o.append(T(160, 201, "0:001/01", 6.4))
    return _mk(
        31, o, "Equivalent PLC ladder program with four rungs",
        "Sơ đồ bậc thang PLC gồm bốn nhánh với địa chỉ I:000/00, I:001/00, 0:000/01, 0:001/02 và các cuộn 0:000/00 đến 0:003/00",
        "PLC ladder program with four rungs and address labels I:000/00, I:001/00, 0:000/01 and 0:001/02",
        "Sơ đồ bậc thang PLC tương đương: nhánh 1 và 2 dùng tiếp điểm thường hở I:000/00, I:001/00; nhánh 3 dùng 0:000/01 song song 0:001/02; nhánh 4 dùng 0:001/01",
        "Four PLC ladder rungs: rung 1 uses NO I:000/00 to coil 0:000/00; rung 2 uses NO I:001/00 to coil 0:001/00; rung 3 uses NO 0:000/01 in parallel with NC 0:001/02 to coil 0:002/00; rung 4 uses NO 0:001/01 to coil 0:003/00")


@_reg
def fig_f32():
    """Fig 8.32: DCS architecture with stations, highway and two process units."""
    o = [_defs()]
    o.append(_b(55, 16, 100, 26, "Operator\nstation", size=7.0))
    o.append(_b(55, 44, 100, 26, "Communication\ncard", size=6.8))
    o.append(_b(285, 14, 110, 34, "Engineering\nconfiguration\nstation", size=6.6))
    o.append(_b(285, 50, 110, 24, "Communication\ncard", size=6.8))
    o.append(_b(525, 16, 100, 26, "Process\ncomputer", size=7.0))
    o.append(_b(525, 44, 100, 26, "Communication\ncard", size=6.8))
    for xx, y0 in ((105, 70), (340, 74), (575, 70)):
        o.append(_line(xx, y0, xx, 92, sw=1.2))
    o.append(_line(20, 92, 660, 92, sw=1.8))
    o.append(T(400, 85, "Main plant data highway", 7.2))
    o.append(_ar(455, 87, 480, 91, color=INK, sw=1.1))

    for cx in (130, 520):
        o.append(_line(cx, 92, cx, 104, sw=1.2))
        o.append(_b(cx - 45, 104, 90, 22, "Communication\ncard", size=6.6))
        o.append(_line(cx, 126, cx, 130, sw=1.2))
        o.append(_b(cx - 35, 130, 70, 18, "Controller files", size=6.4))
        o.append(_ar(cx, 148, cx, 160, color=INK, sw=1.1))
    o.append(_line(30, 160, 650, 160, sw=1.5))
    o.append(T(78, 157, "Local I/O interface Bus", 6.2))
    o.append(T(558, 157, "Local I/O interface Bus", 6.2))

    for cx in (130, 520):
        o.append(_line(cx, 160, cx, 164, sw=1.1))
        o.append(_b(cx - 35, 164, 70, 18, "I/O interface\nmodule", size=6.2))

    o.append(_line(110, 182, 110, 188, sw=1.1))
    o.append(_line(110, 188, 60, 188, sw=1.1))
    o.append(_line(110, 188, 130, 188, sw=1.1))
    o.append(_line(110, 188, 190, 188, sw=1.1))
    o.append(_txcircle(60, 194))
    o.append(T(74, 198, "Tx", 6.6))
    o.append(_valve(130, 194))
    o.append(T(130, 211, "FCE", 6.2))
    o.append(_b(165, 184, 58, 22, "PH\nanalyzer", size=6.4))
    for xx in (60, 130, 190):
        o.append(_line(xx, 204, xx, 208, sw=1.0))
    o.append(_b(55, 208, 150, 20, "Process operation unit", size=6.8))

    o.append(_line(500, 182, 500, 188, sw=1.1))
    o.append(_line(500, 188, 470, 188, sw=1.1))
    o.append(_line(500, 188, 540, 188, sw=1.1))
    o.append(_line(500, 188, 580, 188, sw=1.1))
    o.append(_txcircle(470, 194))
    o.append(T(484, 198, "Tx", 6.6))
    o.append(_valve(540, 194))
    o.append(T(540, 211, "FCE", 6.2))
    o.append(_b(555, 184, 80, 22, "Oxygen\nanalyzer", size=6.4))
    for xx in (470, 540, 580):
        o.append(_line(xx, 204, xx, 208, sw=1.0))
    o.append(_b(465, 208, 160, 20, "Process operation unit", size=6.8))

    o.append(_rect(235, 200, 210, 28, fill="#ffffff", sw=0.9))
    o.append(T(240, 212, "Tx : Process transmitters", 5.8, anchor="start"))
    o.append(T(240, 223, "FCE : Final control Element.", 5.8, anchor="start"))
    return _mk(
        32, o, "Distributed control system architecture",
        "Sơ đồ kiến trúc DCS gồm trạm vận hành, trạm cấu hình kỹ thuật, máy tính quá trình trên đường truyền dữ liệu chính và hai đơn vị quá trình trường",
        "DCS architecture with operator station, engineering configuration station and process computer on the main plant data highway",
        "Sơ đồ hệ thống điều khiển phân tán: các trạm vận hành và cấu hình nối qua đường truyền dữ liệu chính tới bộ điều khiển, mô-đun I/O, transmitter Tx và phần tử điều khiển cuối FCE",
        "Distributed control system: operator, engineering configuration and process computer stations on the main plant data highway, with controller files, local I/O bus, transmitters, analyzers, final control elements and process operation units")


@_reg
def fig_f33():
    """Fig 8.33: DCS hardware interconnection on primary and back-up highways."""
    o = [_defs()]
    o.append(T(18, 12, "DCS hardware interconnection", 7.4, anchor="start"))
    for xx, lab in ((300, "PLC"), (355, "PLC"), (410, "PLC"), (455, "")):
        o.append(_b(xx, 16, 44, 16, lab, size=6.6))
    o.append(_line(285, 38, 465, 38, sw=1.2))
    o.append(T(436, 34, "PLCD", 5.8, anchor="end"))
    o.append(_line(322, 32, 322, 42, sw=1.0))
    o.append(_line(432, 32, 432, 42, sw=1.0))

    for xx, lab, ww in ((30, "PVIU", 52), (95, "PVIU", 52),
                        (160, "BC", 46), (225, "HLC", 46), (290, "DHP", 46)):
        o.append(_b(xx, 44, ww, 20, lab, size=6.8))
        cx = xx + ww / 2.0
        o.append(_line(cx, 64, cx, 78, sw=1.0))
        o.append(_line(cx + 4, 64, cx + 4, 86, sw=0.9, dash="3 2", color=GREY))
    o.append(_line(20, 78, 470, 78, sw=1.5))
    o.append(_line(20, 86, 470, 86, sw=1.1, dash="5 3", color=GREY))
    o.append(T(470, 74, "Primary cable", 5.8, anchor="end"))
    o.append(T(470, 99, "Back-up cable", 5.8, anchor="end"))

    o.append(_rect(200, 112, 66, 22))
    o.append(T(233, 126, "HTCM", 7.6))
    o.append(_line(238, 86, 238, 112, sw=1.1))
    o.append(_line(244, 86, 244, 112, sw=0.9, dash="3 2", color=GREY))
    o.append(_line(266, 123, 300, 123, sw=1.1))
    o.append(T(280, 120, "PAL", 5.8))
    o.append(_b(300, 113, 42, 18, "PC", size=7.0))
    o.append(_line(266, 131, 368, 131, sw=1.1))
    o.append(T(355, 128, "PAL", 5.8))
    o.append(_b(368, 122, 38, 18, "OS", size=7.0))

    o.append(_b(30, 140, 38, 18, "OS", size=7.0))
    o.append(_b(100, 140, 42, 18, "ECS", size=7.0))
    o.append(_line(49, 140, 49, 132, sw=1.0))
    o.append(_line(49, 132, 200, 132, sw=1.0))
    o.append(T(120, 129, "PAL", 5.8))
    o.append(_line(121, 140, 121, 136, sw=1.0))
    o.append(_line(121, 136, 210, 136, sw=1.0))
    o.append(_b(300, 140, 42, 18, "LOS", size=6.8))
    o.append(_line(266, 134, 300, 134, sw=1.0))

    o.append(_b(270, 166, 40, 18, "MC", size=7.0))
    o.append(_b(350, 166, 40, 18, "MC", size=7.0))
    o.append(_line(290, 158, 290, 166, sw=1.0))
    o.append(_line(321, 158, 321, 162, sw=1.0, dash="3 2", color=GREY))
    o.append(_line(310, 158, 370, 158, sw=0.9, dash="3 2", color=GREY))
    o.append(_line(370, 158, 370, 166, sw=1.0, dash="3 2", color=GREY))

    o.append(_line(20, 196, 470, 196, sw=1.5))
    o.append(_line(20, 204, 470, 204, sw=1.1, dash="5 3", color=GREY))
    for xx, lab, ww in ((30, "PVIU", 52), (95, "PVIU", 52),
                        (160, "BC", 46), (225, "HLC", 46)):
        o.append(_b(xx, 208, ww, 18, lab, size=6.6))
        cx = xx + ww / 2.0
        o.append(_line(cx, 196, cx, 208, sw=1.0))
        o.append(_line(cx + 4, 204, cx + 4, 208, sw=0.9, dash="3 2", color=GREY))
    o.append(T(470, 192, "Primary cable", 5.8, anchor="end"))
    o.append(T(470, 216, "Back-up cable", 5.8, anchor="end"))

    o.append(_rect(478, 12, 196, 214, fill="#ffffff", sw=0.9))
    o.append(T(484, 24, "LEGENDS", 6.6, anchor="start", weight="bold"))
    legend = (
        "HTCM : Highway Traffic Controller Module.",
        "ECS : Engineering Configuration Station.",
        "OS : Operator Station.",
        "PVIU : Process Variables Interface Unit.",
        "BC : Basic Controller.",
        "HLC : High-level Controller",
        "PC : Process Computer",
        "DHP : Data Highway Port.",
        "MC : Multifunction Controller.",
        "LOS : Local Controller Station.",
        "PLC : Programmable Logic Controller.",
        "PLCD : PLC Data Highway",
        "PAL : Preferential Access Link.",
    )
    for i, line in enumerate(legend):
        o.append(T(484, 37 + i * 14, line, 5.4, anchor="start"))
    return _mk(
        33, o, "DCS hardware interconnection and plant data highway",
        "Sơ đồ kết nối phần cứng DCS với HTCM, hai cáp chính và cáp dự phòng, PLC qua PLCD và các thiết bị PVIU, BC, HLC, DHP, PC, OS, ECS, LOS, MC",
        "DCS hardware interconnection with HTCM, primary and back-up cables, PLC data highway and connected devices",
        "Sơ đồ phần cứng DCS: HTCM điều phối các thiết bị trên đường truyền dữ liệu, PLC nối qua PLCD và DHP, các trạm OS, ECS, PC, LOS nối qua PAL",
        "DCS hardware interconnection showing the highway traffic controller module (HTCM), primary and back-up cables, PLCs on the PLC data highway (PLCD), and PVIU, BC, HLC, DHP, PC, OS, ECS, LOS and multifunction controllers connected through preferential access links")


@_reg
def fig_f34():
    """Fig 8.34: a basic controller (BC) slot with inputs and alarm outputs."""
    o = [_defs()]
    o.append(T(340, 16, "Basic controller (BC) control slot", 8.4))
    o.append(_poly([(300, 52), (300, 162), (378, 107)], close=True,
                   fill="#eef3fb", sw=1.3))
    o.append(T(322, 113, "BC", 8.2))
    o.append(_ar(180, 80, 298, 80, color=INK, sw=1.3))
    o.append(T(178, 76, "Input PV", 7.2, anchor="end"))
    o.append(_ar(180, 136, 298, 136, color=INK, sw=1.3))
    o.append(T(178, 132, "Input SP", 7.2, anchor="end"))
    o.append(_line(340, 62, 340, 46, sw=1.1))
    o.append(_line(340, 46, 470, 46, sw=1.1))
    o.append(_circle(472, 46, 2.6, fill="#ffffff"))
    o.append(T(478, 49, "High alarm output", 7.2, anchor="start"))
    o.append(_line(378, 107, 470, 107, sw=1.1))
    o.append(_circle(472, 107, 2.6, fill="#ffffff"))
    o.append(T(478, 110, "Control output (Co)", 7.2, anchor="start"))
    o.append(_line(340, 152, 340, 168, sw=1.1))
    o.append(_line(340, 168, 470, 168, sw=1.1))
    o.append(_circle(472, 168, 2.6, fill="#ffffff"))
    o.append(T(478, 171, "Low alarm output", 7.2, anchor="start"))
    o.append(T(340, 196, "Each slot: two inputs, one control output and two alarm outputs",
               7.0, color=GREY))
    return _mk(
        34, o, "Basic controller slot of a multifunction controller",
        "Sơ đồ khe điều khiển cơ bản BC gồm đầu vào PV, đầu vào SP, đầu ra điều khiển Co và hai đầu ra báo động cao, thấp",
        "Basic controller slot with PV and SP inputs, control output and high/low alarm outputs",
        "Sơ đồ khe điều khiển BC: đầu vào biến quá trình PV, đầu vào giá trị cài đặt SP, đầu ra điều khiển Co cùng đầu ra báo động cao và báo động thấp",
        "Basic controller slot showing the process variable input PV, set point input SP, control output Co, and separate high and low alarm outputs")
