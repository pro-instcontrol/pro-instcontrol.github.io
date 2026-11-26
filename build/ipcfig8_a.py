# -*- coding: utf-8 -*-
"""Figure supplier A for IPC Chapter 8: figures 8.1-8.9 (PDF pp. 354-361).

Each figure is a simplified vector redraw of the printed raster diagram.
"""
from ipcfig8_common import (BLUE, GREEN, GREY, INK, RED, H, W, T, _ar, _b,
                            _circle, _defs, _ellipse, _fig, _frame, _legend,
                            _line, _path, _poly, _rect, _mk, _series,
                            _wavey, make_registry)

FIGS, _reg = make_registry()


def _blk(x, y, w, h, label, size=7.4, fill="#eef3fb"):
    """Compact labelled block; newlines start further text lines."""
    lines = str(label).split("\n")
    o = [_rect(x, y, w, h, fill)]
    step = size * 1.15
    top = y + h / 2.0 - (len(lines) - 1) * step / 2.0 + size * 0.32
    for i, ln in enumerate(lines):
        o.append(T(x + w / 2.0, top + i * step, ln, size))
    return "".join(o)


def _dots(o, x, ys, r=1.6):
    for yy in ys:
        o.append(_circle(x, yy, r, fill=INK, sw=0))


@_reg
def fig_f01():
    """Fig 8.1: three functional blocks of an instrumentation system."""
    o = [_defs()]
    o.append(T(340, 28,
               "Three functional blocks of a microprocessor-based instrumentation system",
               8.6))
    xs = (20, 245, 470)
    heads = (("Measurement", "systems"), ("Display", "devices"),
             ("Control", "actions"))
    bodies = (
        ["Smart functions;", "remote calibration", "adjustment and",
         "other programm-", "ing operations."],
        ["Programmable", "recorder and", "indication", "functions."],
        ["Generation of fast", "and precise control", "actions with",
         "programmable", "functions."],
    )
    for i, x in enumerate(xs):
        o.append(_rect(x, 45, 190, 110))
        o.append(_line(x, 72, x + 190, 72, sw=1.0))
        o.append(T(x + 95, 57, heads[i][0], 8.0))
        o.append(T(x + 95, 67, heads[i][1], 8.0))
        for j, ln in enumerate(bodies[i]):
            o.append(T(x + 95, 86 + j * 12, ln, 7.3))
    o.append(_ar(211, 60, 243, 60))
    o.append(_ar(436, 60, 468, 60))
    return _mk(
        1, o, "Three functional blocks of microprocessor-based instrumentation",
        "Sơ đồ ba khối đo lường, hiển thị và điều khiển của hệ thống thiết bị đo",
        "Three functional blocks of measurement, display and control",
        "Sơ đồ ba khối chức năng đo lường, hiển thị và điều khiển",
        "Block diagram of the three functional blocks: measurement, display and control")


@_reg
def fig_f02():
    """Fig 8.2: a microcomputer formed by microprocessor, memory and I/O."""
    o = [_defs()]
    for y in (90, 120, 150):
        o.append(_line(45, y, 640, y, sw=1.2))
    o.append(T(28, 86, "A", 7.5))
    o.append(T(60, 85, "Address Bus", 6.8, anchor="start"))
    o.append(T(28, 116, "C", 7.5))
    o.append(T(60, 115, "Control Bus", 6.8, anchor="start"))
    o.append(T(28, 146, "D", 7.5))
    o.append(T(60, 145, "Data Bus", 6.8, anchor="start"))
    o.append(_blk(70, 38, 95, 40, "Microprocessor", 7.4))
    o.append(_blk(225, 38, 120, 40, "Memory having\nstored program\nand data", 6.9))
    o.append(_blk(420, 38, 150, 40, "I/O interface", 7.8))
    o.append(_blk(400, 4, 95, 24, "Parallel\nI/O devices", 6.8))
    o.append(_blk(510, 4, 95, 24, "Serial\nI/O devices", 6.8))
    o.append(_ar(447, 28, 447, 38))
    o.append(_ar(557, 28, 557, 38))
    for x in (117, 285, 495):
        o.append(_line(x, 78, x, 150, sw=0.8, color=GREY))
        o.append(_ar(x, 89, x, 80, color=BLUE, sw=1.1))
        o.append(_ar(x, 97, x, 113, color=BLUE, sw=1.1))
        o.append(_ar(x + 5, 113, x + 5, 97, color=BLUE, sw=1.1))
        o.append(_ar(x, 127, x, 143, color=BLUE, sw=1.1))
        o.append(_ar(x + 5, 143, x + 5, 127, color=BLUE, sw=1.1))
    return _mk(
        2, o, "Microcomputer with microprocessor, memory and I/O",
        "Sơ đồ vi tính gồm bộ vi xử lý, bộ nhớ và I/O trên các bus địa chỉ, điều khiển, dữ liệu",
        "Microcomputer with microprocessor, memory and I/O on address, control and data buses",
        "Sơ đồ vi tính với bộ vi xử lý, bộ nhớ và các thiết bị I/O trên ba bus",
        "Microcomputer built from a microprocessor, memory and I/O devices on three buses")


@_reg
def fig_f03():
    """Fig 8.3: 3-to-8 address decoder selecting input and output ports."""
    o = [_defs()]
    o.append(T(340, 18, "Address decoding with a 3-to-8 decoder", 9.0))
    o.append(_path("M 70 48 L 70 80 C 108 80 108 48 70 48 Z", fill="#eef3fb"))
    for i, lab in enumerate(("A0", "A1", "A2", "A3")):
        yy = 53 + i * 8
        o.append(_line(40, yy, 70, yy, sw=0.9))
        o.append(T(37, yy + 2.2, lab, 6.4, anchor="end"))
    o.append(_line(96, 64, 160, 64, sw=1.0))
    o.append(_line(160, 64, 160, 80, sw=1.0))
    o.append(_rect(150, 80, 85, 75))
    for x in (160, 190, 220):
        o.append(_circle(x, 80, 2.4, fill="#ffffff", sw=1.0))
    o.append(T(160, 76, "E1", 6.0))
    o.append(T(190, 76, "E2", 6.0))
    o.append(T(220, 76, "E3", 6.0))
    for i, lab in enumerate(("A4", "A5", "A6")):
        yy = 100 + i * 15
        o.append(_line(120, yy, 150, yy, sw=0.9))
        o.append(T(117, yy + 2.2, lab, 6.4, anchor="end"))
    o.append(T(192, 143, "Address", 6.5))
    o.append(T(192, 151, "decoder", 6.5))
    for yy, lab in ((100, "O7"), (130, "O6")):
        o.append(_circle(235, yy, 2.0, fill="#ffffff", sw=1.0))
        o.append(T(242, yy - 4, lab, 6.0, anchor="start"))
    # upper NOR gate: O7 combined with IOR
    o.append(_path("M 300 85 Q 330 85 338 101 Q 330 117 300 117 Q 310 101 300 85 Z",
                   fill="#eef3fb"))
    o.append(_circle(341, 101, 2.4, fill="none", sw=1.0))
    o.append(_line(235, 100, 285, 100, sw=1.0))
    o.append(_line(285, 100, 285, 93, sw=1.0))
    o.append(_line(285, 93, 300, 93, sw=1.0))
    o.append(_line(285, 112, 300, 112, sw=1.0))
    o.append(T(282, 115, "IOR", 6.2, anchor="end"))
    o.append(T(240, 92, "11111111", 6.2, anchor="start"))
    o.append(_line(343, 101, 475, 101, sw=1.0))
    o.append(_line(475, 101, 475, 110, sw=1.0))
    o.append(T(395, 97, "I/O Select line", 6.2))
    # lower NOR gate: O6 combined with IOW
    o.append(_path("M 300 135 Q 330 135 338 151 Q 330 167 300 167 Q 310 151 300 135 Z",
                   fill="#eef3fb"))
    o.append(_circle(341, 151, 2.4, fill="none", sw=1.0))
    o.append(_line(235, 130, 285, 130, sw=1.0))
    o.append(_line(285, 130, 285, 143, sw=1.0))
    o.append(_line(285, 143, 300, 143, sw=1.0))
    o.append(_line(285, 160, 300, 160, sw=1.0))
    o.append(T(282, 163, "IOW", 6.2, anchor="end"))
    o.append(T(240, 126, "11111110", 6.2, anchor="start"))
    o.append(_line(343, 151, 475, 151, sw=1.0))
    o.append(_line(475, 151, 475, 215, sw=1.0))
    o.append(T(395, 147, "I/O Select line", 6.2))
    # input buffer port
    o.append(_rect(430, 35, 90, 75))
    o.append(T(475, 55, "Input", 7.2))
    o.append(T(475, 64, "buffer", 7.2))
    o.append(T(475, 73, "port", 7.2))
    o.append(T(475, 104, "EN", 6.4))
    ys = [42, 50, 58, 66, 74, 82, 90, 98]
    for yy in ys:
        o.append(_line(520, yy, 600, yy, sw=0.9))
    _dots(o, 520, ys)
    _dots(o, 600, ys)
    o.append(T(560, 30, "Data bus", 6.4))
    # output latching port
    o.append(_rect(430, 140, 90, 75))
    o.append(T(475, 160, "Output", 7.2))
    o.append(T(475, 169, "latching", 7.2))
    o.append(T(475, 178, "port", 7.2))
    o.append(T(475, 208, "EN", 6.4))
    ys = [147, 155, 163, 171, 179, 187, 195, 203]
    for yy in ys:
        o.append(_line(520, yy, 600, yy, sw=0.9))
    _dots(o, 520, ys)
    _dots(o, 600, ys)
    o.append(T(560, 135, "Data bus", 6.4))
    return _mk(
        3, o, "Address decoding with a 3-to-8 decoder",
        "Sơ đồ giải mã địa chỉ 3 trên 8 cho cổng vào đệm và cổng ra chốt",
        "Address decoding with a 3-to-8 decoder for buffer and latching ports",
        "Sơ đồ giải mã địa chỉ chọn cổng vào đệm và cổng ra chốt",
        "Address decoder driving an input buffer port and an output latching port")


@_reg
def fig_f04():
    """Fig 8.4: ADC interface using polling and an address decoder."""
    o = [_defs()]
    o.append(T(340, 22, "ADC interfacing by polling", 9.0))
    o.append(_blk(20, 62, 72, 30, "Transducer", 7.0))
    o.append(T(116, 55, "Analog input line", 6.6))
    o.append(_ar(92, 80, 135, 80))
    o.append(_blk(135, 60, 62, 64, "ADC", 8.0))
    o.append(_ar(166, 42, 166, 60))
    o.append(T(180, 48, "Vcc", 6.6))
    ys = [66, 73, 80, 87, 94, 101, 108, 115]
    for yy in ys:
        o.append(_line(197, yy, 230, yy, sw=0.9))
    o.append(_blk(230, 60, 55, 64, "Buffer", 7.4))
    for yy in ys:
        o.append(_line(285, yy, 320, yy, sw=0.9))
    o.append(_line(320, 63, 320, 118, sw=1.2))
    _dots(o, 320, ys)
    o.append(_ar(320, 92, 415, 92))
    o.append(T(370, 80, "Digital output line", 6.8))
    o.append(T(370, 104, "Data bus", 6.8))
    o.append(T(150, 132, "ST", 6.6))
    o.append(T(180, 132, "DR", 6.6))
    o.append(_blk(20, 152, 100, 55, "Address\ndecoder", 7.2))
    for yy, lab in ((162, "3 (10000010)"), (180, "2 (10000001)"),
                    (198, "1 (10000000)")):
        o.append(T(125, yy, lab, 6.2, anchor="start"))
    o.append(_line(120, 166, 150, 166, sw=1.0))
    o.append(_line(150, 166, 150, 124, sw=1.0))
    o.append(_line(120, 184, 257, 184, sw=1.0))
    o.append(_line(257, 184, 257, 124, sw=1.0))
    o.append(_line(120, 202, 325, 202, sw=1.0))
    o.append(_line(325, 202, 325, 170, sw=1.0))
    o.append(_line(180, 124, 180, 155, sw=1.0))
    o.append(_line(180, 155, 300, 155, sw=1.0))
    o.append(_rect(300, 138, 50, 32))
    o.append(T(325, 158, "Buffer", 7.0))
    o.append(T(325, 178, "EN", 6.2))
    o.append(_line(325, 138, 325, 118, sw=1.0))
    return _mk(
        4, o, "ADC interfacing by polling",
        "Sơ đồ giao tiếp ADC theo phương pháp thăm dò với bộ giải mã địa chỉ",
        "ADC interfacing by polling with an address decoder and tri-state buffers",
        "Sơ đồ giao tiếp ADC theo chế độ thăm dò, có bộ giải mã địa chỉ và buf",
        "Polled ADC interface showing the address decoder, buffers, data bus and ST/DR lines")


@_reg
def fig_f05():
    """Fig 8.5: ADC interface using interrupts."""
    o = [_defs()]
    o.append(T(340, 22, "ADC interfacing by interrupt", 9.0))
    o.append(_blk(20, 68, 72, 30, "Transducer", 7.0))
    o.append(T(116, 61, "Analog input line", 6.6))
    o.append(_ar(92, 86, 135, 86))
    o.append(_blk(135, 58, 70, 70, "ADC", 8.2))
    o.append(_ar(170, 40, 170, 58))
    o.append(T(184, 46, "Vcc", 6.6))
    ys = [64, 71, 78, 85, 92, 99, 106, 113]
    for yy in ys:
        o.append(_line(205, yy, 245, yy, sw=0.9))
    o.append(_line(245, 61, 245, 116, sw=1.2))
    _dots(o, 245, ys)
    o.append(_ar(245, 88, 330, 88))
    o.append(T(288, 75, "ADC Data bus", 6.8))
    for x, lab in ((150, "WR"), (175, "RD"), (200, "CS")):
        o.append(T(x, 137, lab, 6.6))
    o.append(_line(150, 128, 150, 196, sw=1.0))
    o.append(_line(150, 196, 345, 196, sw=1.0))
    o.append(_circle(348, 196, 2.2, fill=INK, sw=0))
    o.append(T(355, 199, "MEMW", 6.8, anchor="start"))
    o.append(_line(175, 128, 175, 180, sw=1.0))
    o.append(_line(175, 180, 345, 180, sw=1.0))
    o.append(_circle(348, 180, 2.2, fill=INK, sw=0))
    o.append(T(355, 183, "MEMR", 6.8, anchor="start"))
    o.append(_line(200, 128, 200, 150, sw=1.0))
    o.append(_line(200, 150, 255, 150, sw=1.0))
    o.append(_line(255, 150, 255, 170, sw=1.0))
    for yy in (150, 170):
        o.append(_poly([(255, yy - 7), (255, yy + 7), (272, yy)], fill="#eef3fb"))
        o.append(_circle(275, yy, 2.2, fill="none", sw=1.0))
        o.append(_ar(278, yy, 345, yy))
    o.append(T(353, 153, "Interrupt line", 6.8, anchor="start"))
    o.append(T(353, 173, "Address line", 6.8, anchor="start"))
    return _mk(
        5, o, "ADC interfacing by interrupt",
        "Sơ đồ giao tiếp ADC theo chế độ ngắt với các tín hiệu WR, RD, CS",
        "ADC interfacing by interrupt with WR, RD and CS control signals",
        "Sơ đồ giao tiếp ADC dùng ngắt, có đường ngắt và các tín hiệu MEMR, MEMW",
        "Interrupt-driven ADC interface with chip select, interrupt line and memory control lines")


@_reg
def fig_f06():
    """Fig 8.6: hand-held configurator and PC configuration link."""
    o = [_defs()]
    o.append(T(340, 14,
               "Smart transducer configuration: hand-held communicator and PC",
               8.4))
    o.append(_rect(75, 26, 315, 150))
    o.append(T(232, 38, "Hand held configurator", 8.2))
    top = (("Display", 85), ("Keyboard", 157),
           ("Micro-\nprocessor", 230), ("RAM 1", 303))
    bot = (("MODEM", 85), ("ROM", 157), ("RAM 2", 230), ("RS232C", 303))
    for lab, x in top:
        o.append(_blk(x, 46, 62, 24, lab, 6.8))
        o.append(_line(x + 31, 70, x + 31, 86, sw=0.8, color=GREY))
    o.append(_line(90, 86, 375, 86, sw=1.0))
    o.append(T(88, 89, "Bus", 6.2, anchor="end"))
    for lab, x in bot:
        o.append(_line(x + 31, 86, x + 31, 102, sw=0.8, color=GREY))
        o.append(_blk(x, 102, 62, 24, lab, 6.8))
    o.append(_blk(5, 93, 60, 26, "Field\ntransducer", 6.4))
    o.append(_ar(65, 100, 85, 100, sw=1.0))
    o.append(_ar(85, 112, 65, 112, sw=1.0))
    o.append(_blk(5, 135, 60, 26, "Receiver\ninstrument", 6.2))
    o.append(_line(35, 119, 35, 135, sw=0.9))
    o.append(_line(365, 114, 395, 114, sw=1.0))
    o.append(_line(395, 114, 395, 90, sw=1.0))
    o.append(_line(395, 90, 430, 90, sw=1.0))
    o.append(_blk(430, 75, 50, 30, "PC", 7.6))
    o.append(_blk(495, 75, 62, 30, "MODEM", 7.0))
    o.append(_line(480, 90, 495, 90, sw=1.0))
    o.append(_blk(400, 122, 62, 26, "Printer", 7.0))
    o.append(_line(455, 105, 455, 122, sw=0.9))
    o.append(_blk(495, 122, 62, 26, "Receiver\ninstrument", 6.2))
    o.append(_line(526, 105, 526, 122, sw=0.9))
    o.append(_blk(575, 122, 70, 26, "Field\ntransducer", 6.4))
    o.append(_line(557, 135, 575, 135, sw=1.0))
    return _mk(
        6, o, "Hand-held configurator for smart instruments",
        "Sơ đồ cấu hình bộ chuyển đổi thông minh bằng bộ lập trình cầm tay và máy tính PC",
        "Configuration of smart transducers with a hand-held configurator and a PC",
        "Sơ đồ hệ thống lập trình cầm tay gồm microprocessor, bộ nhớ, MODEM và bàn phím",
        "Hand-held configurator with display, keyboard, processor, memory, MODEM and PC link")


@_reg
def fig_f07():
    """Fig 8.7: a host processor configuring a PIA over the bus."""
    o = [_defs()]
    o.append(T(340, 38,
               "Host processor configures the PIA through command and status registers",
               8.4))
    o.append(_blk(15, 82, 92, 40, "Host\nprocessor", 7.4))
    o.append(_ar(107, 102, 160, 102))
    o.append(T(134, 95, "Bus", 6.8))
    o.append(_blk(160, 82, 100, 40, "Bus\ninterfacing", 7.4))
    o.append(_ar(260, 102, 292, 102))
    o.append(_blk(292, 82, 66, 40, "PIA", 8.4))
    o.append(_ar(358, 102, 390, 102))
    o.append(_blk(390, 76, 140, 52, "Discrete and analog\nI/O interface card", 7.2))
    o.append(_ar(530, 92, 612, 92))
    o.append(T(618, 95, "Discrete I/O", 6.8, anchor="start"))
    o.append(_ar(530, 112, 612, 112))
    o.append(T(618, 115, "Analog I/O", 6.8, anchor="start"))
    return _mk(
        7, o, "Host processor and PIA interface",
        "Sơ đồ bộ xử lý chính cấu hình PIA qua thanh ghi lệnh và trạng thái",
        "Host processor configuring the PIA via command and status registers",
        "Sơ đồ nối bộ xử lý chủ với PIA và thẻ I/O rời rạc, tương tự",
        "Chain from host processor through bus interfacing and PIA to the I/O interface card")


@_reg
def fig_f08():
    """Fig 8.8: optical isolation of a digital input driving a solenoid."""
    o = [_defs()]
    o.append(T(340, 22, "Optical isolation of a digital input driving a solenoid",
               8.8))
    o.append(T(60, 100, "Digital input", 7.0, anchor="end"))
    o.append(_ar(62, 105, 130, 105))
    o.append(_rect(130, 70, 180, 92))
    o.append(T(220, 82, "optocoupler", 6.2, color=GREY))
    o.append(_poly([(150, 94), (150, 116), (168, 105)], fill="#eef3fb"))
    o.append(_line(172, 91, 172, 119, sw=1.6))
    o.append(_line(130, 105, 150, 105, sw=1.0))
    o.append(_ar(180, 99, 212, 93, color=RED, sw=1.2))
    o.append(_ar(180, 111, 212, 117, color=RED, sw=1.2))
    o.append(_line(230, 90, 230, 120, sw=1.2))
    o.append(_line(230, 98, 250, 91, sw=1.1))
    o.append(_line(230, 112, 250, 119, sw=1.1))
    o.append(_line(250, 91, 250, 78, sw=1.0))
    o.append(_line(250, 78, 355, 78, sw=1.0))
    o.append(_line(355, 78, 355, 90, sw=1.0))
    o.append(_line(250, 119, 250, 145, sw=1.0))
    o.append(_line(244, 145, 256, 145, sw=1.0))
    o.append(_line(247, 149, 253, 149, sw=1.0))
    o.append(_blk(320, 90, 70, 28, "Solenoid", 7.4))
    o.append(_line(390, 104, 430, 104, sw=1.0))
    o.append(_circle(432, 104, 2.4, fill=INK, sw=0))
    o.append(T(442, 99, "Vin for", 6.6, anchor="start"))
    o.append(T(442, 108, "solenoid", 6.6, anchor="start"))
    o.append(T(442, 117, "operation", 6.6, anchor="start"))
    return _mk(
        8, o, "Optical isolation of an input line",
        "Sơ đồ cách ly quang đầu vào số dùng đèn LED và phototransistor để điều khiển solenoid",
        "Optical isolation of a digital input using an LED and a phototransistor",
        "Sơ đồ cách ly quang giữa đầu vào số và cuộn solenoid",
        "Optocoupler diagram with an LED input, light rays, phototransistor and solenoid load")


@_reg
def fig_f09():
    """Fig 8.9: masking a data bit with an AND gate."""
    o = [_defs()]
    o.append(T(340, 24, "Masking a data bit with an AND gate", 9.0))
    o.append(T(48, 96, "Masking bit", 7.4, anchor="end"))
    o.append(T(48, 146, "Data bit", 7.4, anchor="end"))
    o.append(_line(55, 93, 200, 93, sw=1.1))
    o.append(_line(55, 143, 200, 143, sw=1.1))
    o.append(_circle(55, 93, 2.6, fill=INK, sw=0))
    o.append(_circle(55, 143, 2.6, fill=INK, sw=0))
    o.append(_path("M 200 75 L 200 161 C 248 161 248 75 200 75 Z",
                   fill="#eef3fb"))
    o.append(_line(236, 118, 320, 118, sw=1.1))
    o.append(_circle(323, 118, 2.6, fill="none", sw=1.0))
    o.append(T(334, 121, "Output bit", 7.4, anchor="start"))
    return _mk(
        9, o, "Masking a data bit with an AND gate",
        "Sơ đồ che dữ liệu: bit dữ liệu AND với bit mặt nạ qua cổng logic",
        "Masking a data bit by ANDing it with a mask bit through a logic gate",
        "Sơ đồ cổng AND với hai đầu vào là bit mặt nạ và bit dữ liệu",
        "AND gate with mask bit and data bit inputs and the resulting output bit")
