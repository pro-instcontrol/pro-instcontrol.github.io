# -*- coding: utf-8 -*-
"""Figures 5.34-5.43 for IPC Chapter 5 (signal conditioning and DAQ).

Supplier module ``_d``: DAC output currents, PC-based acquisition
architecture, serial interface standards, fieldbus wiring and the three
levels of I/O isolation.  Every figure is a simplified vector redraw of the
printed diagram; all labels stay inside the 680 x 250 canvas and above
y = 232 (the bilingual 5.n strip sits at 245).
"""
from ipcfig5_common import (BLUE, GREEN, GREY, INK, RED, H, W, T, _ar, _b,
                            _circle, _defs, _ellipse, _fig, _frame, _legend,
                            _line, _path, _poly, _rect, _mk, _series,
                            _wavey, make_registry)

FIGS, _reg = make_registry()


# ----------------------------------------------------------------- helpers
def _res_h(x1, x2, y, n=4, amp=3.0, color=INK):
    """Horizontal zig-zag resistor between two end points."""
    pts = []
    for i in range(2 * n + 1):
        pts.append((x1 + (x2 - x1) * i / float(2 * n),
                    y + (-amp if i % 2 else amp)))
    return _poly(pts, sw=1.0, color=color)


def _res_v(x, y1, y2, n=4, amp=3.0, color=INK):
    """Vertical zig-zag resistor between two end points."""
    pts = []
    for i in range(2 * n + 1):
        pts.append((x + (-amp if i % 2 else amp),
                    y1 + (y2 - y1) * i / float(2 * n)))
    return _poly(pts, sw=1.0, color=color)


def _gnd(x, y, color=INK):
    """Three-bar ground symbol with a short top stub."""
    return (_line(x, y - 5, x, y, sw=1.0, color=color)
            + _line(x - 6, y, x + 6, y, sw=1.0, color=color)
            + _line(x - 4, y + 3, x + 4, y + 3, sw=0.9, color=color)
            + _line(x - 2, y + 6, x + 2, y + 6, sw=0.8, color=color))


def _terminal(x, y, label=None, anchor="middle"):
    o = [_circle(x, y, 2.4, fill="#ffffff", sw=1.0)]
    if label:
        o.append(T(x, y + 10, label, 7.0, anchor=anchor))
    return "".join(o)


# ---------------------------------------------------------------- 5.34
@_reg
def fig_f34():
    """Fig. 5.34 - R-2R ladder dividing a 2 mA reference into bit currents."""
    o = [_defs()]
    rail = 72.0
    xs = [150, 270, 390, 510]
    nodes = ["D", "C", "B", "A"]
    bits = ["D3", "D2", "D1", "D0"]
    currents = ["1mA", "0.5mA", "0.25mA", "0.125mA"]

    # reference current source at the left end of the ladder
    o.append(_circle(90, 86, 10, fill="#ffffff", sw=1.2))
    o.append(_ar(90, 78, 90, 94, sw=1.3))
    o.append(_line(90, rail, 90, 76, sw=1.1))
    o.append(_line(90, 96, 90, 102, sw=1.1))
    o.append(_gnd(90, 102))
    o.append(T(108, 90, "2mA", 7.2, anchor="start"))

    # series R sections and terminating 2R
    o.append(_line(90, rail, 150, rail, sw=1.2))
    for a, b in zip(xs[:-1], xs[1:]):
        o.append(_res_h(a, b, rail))
    o.append(_line(510, rail, 600, rail, sw=1.2))
    for x, nm in zip(xs, nodes):
        o.append(T(x, rail - 8, nm, 8.0))
    for cx, lab in ((210, "1mA"), (330, "0.5mA"), (450, "0.25mA")):
        o.append(_ar(cx + 30, rail - 20, cx - 30, rail - 20,
                     sw=1.1, color=BLUE))
        o.append(T(cx, rail - 27, lab, 7.0, color=BLUE))

    # four shunt 2R branches with switch, bit line and weighted current
    for x, lab, bit in zip(xs, currents, bits):
        o.append(_line(x, rail, x, rail + 8, sw=1.1))
        o.append(_res_v(x, rail + 8, rail + 38))
        o.append(_line(x, rail + 38, x, rail + 46, sw=1.1))
        o.append(_circle(x, rail + 46, 2.0, fill=INK, sw=0))
        o.append(_line(x, rail + 46, x + 12, rail + 58, sw=1.2))
        o.append(_circle(x + 12, rail + 58, 2.0, fill=INK, sw=0))
        o.append(_line(x + 12, rail + 58, x + 12, rail + 62, sw=1.0))
        o.append(_gnd(x + 12, rail + 62))
        o.append(T(x + 9, rail + 32, "2R", 7.0, anchor="start"))
        o.append(_ar(x + 30, rail + 42, x + 30, rail + 20,
                     sw=1.1, color=GREEN))
        o.append(T(x + 34, rail + 36, lab, 7.0,
                   anchor="start", color=GREEN))
        bx = x - 16
        o.append(_circle(bx, rail + 76, 2.0, fill=INK, sw=0))
        o.append(_line(bx, rail + 76, bx, rail + 126, sw=1.0))
        o.append(T(bx - 6, rail + 79, bit, 7.4, anchor="end"))

    # output bus and termination
    o.append(_line(600, rail, 600, rail + 8, sw=1.1))
    o.append(_res_v(600, rail + 8, rail + 38))
    o.append(_line(600, rail + 38, 600, rail + 126, sw=1.1))
    o.append(T(608, rail + 32, "2R", 7.0, anchor="start"))
    o.append(_line(134, rail + 126, 600, rail + 126, sw=1.4))
    o.append(_line(600, rail + 126, 600, rail + 132, sw=1.1))
    o.append(_gnd(600, rail + 132))
    o.append(_ar(582, rail + 126, 548, rail + 126, sw=1.3))
    o.append(T(565, rail + 118, "Iout", 7.4, color=RED))
    o.append(T(340, 220, "Binary input D3 to D0 steers the weighted currents",
               6.8, color=GREY))
    return _mk(34, o, "R-2R ladder DAC output currents",
               "Dòng ra của DAC theo mạng R-2R",
               "R-2R ladder DAC output currents",
               "Sơ đồ mạng R-2R: dòng tham chiếu 2mA được chia thành 1mA, 0.5mA, 0.25mA và 0.125mA qua các khóa D3 đến D0 và tổng tại Iout.",
               "R-2R ladder diagram: a 2mA reference current is split into 1mA, 0.5mA, 0.25mA and 0.125mA branches selected by switches D3 to D0 and summed at Iout.")


# ---------------------------------------------------------------- 5.35
@_reg
def fig_f35():
    """Fig. 5.35 - block diagram of a PC-based data acquisition system."""
    o = [_defs()]
    # main rack: alarm, three universal input sections, power supply
    o.append(_rect(100, 58, 300, 74, fill="#ffffff", sw=1.4))
    for x in (150, 205, 260, 315):
        o.append(_line(x, 58, x, 132, sw=1.1))
    for i, x in enumerate((175, 230, 285)):
        o.append(T(x, 96, "Universal", 6.6))
        o.append(T(x, 106, "input", 6.6))
        o.append(T(x, 116, "module", 6.6))
    o.append(T(125, 90, "Alarm", 6.4))
    o.append(T(125, 100, "output", 6.4))
    o.append(T(125, 110, "module", 6.4))
    o.append(T(357, 92, "Power", 6.8))
    o.append(T(357, 102, "supply unit", 6.8))

    o.append(T(205, 44, "Universal input module", 7.4))
    o.append(_ar(205, 48, 205, 56, sw=1.1))
    o.append(T(355, 44, "Power supply unit", 7.4))
    o.append(_ar(355, 48, 355, 56, sw=1.1))
    o.append(T(92, 86, "Alarm output", 7.0, anchor="end"))
    o.append(T(92, 96, "module", 7.0, anchor="end"))
    o.append(_ar(94, 95, 100, 95, sw=1.1, color=GREY))

    # communication module and cable to the operator PC
    o.append(_line(100, 132, 500, 132, sw=1.4))
    o.append(_circle(315, 132, 3.2, fill=INK, sw=0))
    o.append(T(315, 160, "General-purpose", 7.0))
    o.append(T(315, 170, "communication module", 7.0))
    o.append(_ar(315, 152, 315, 136, sw=1.1, color=GREY))
    o.append(T(450, 94, "General-purpose", 6.8))
    o.append(T(450, 104, "communication cable", 6.8))
    o.append(_ar(450, 108, 450, 130, sw=1.1, color=GREY))

    # PC operator interface
    o.append(_rect(500, 80, 110, 66, fill="#fbfaf7", sw=1.4))
    o.append(_rect(512, 90, 86, 44, fill="#ffffff", sw=1.0))
    o.append(_line(555, 146, 555, 158, sw=1.2))
    o.append(_poly([(528, 158), (582, 158), (572, 166), (538, 166)],
                   fill="#eef3fb", sw=1.1, close=True))
    o.append(T(555, 180, "(PC) operator interface", 7.2))
    o.append(T(555, 190, "loaded with application", 7.2))
    o.append(T(555, 200, "software", 7.2))
    return _mk(35, o, "PC-based data acquisition architecture",
               "Kiến trúc hệ thống thu thập dữ liệu dùng PC",
               "PC-based data acquisition system architecture",
               "Sơ đồ khối gồm mô-đun vào đa năng, nguồn, mô-đun báo động, mô-đun và cáp truyền thông dùng chung nối với PC chạy phần mềm ứng dụng.",
               "Block diagram of a PC-based data acquisition system with universal input, power supply, alarm output, a shared communication module and cable linked to a PC running application software.")


# ---------------------------------------------------------------- 5.36
@_reg
def fig_f36():
    """Fig. 5.36 - printed 25-pin RS-232 connector signal assignments."""
    o = [_defs()]
    o.append(T(340, 28, "RS-232 25-pin connector signals", 8.4))
    o.append(_path("M330,60 Q330,48 340,48 Q350,48 350,60 "
                   "L350,190 Q350,202 340,202 Q330,202 330,190 Z",
                   fill="#fbfaf7", sw=1.4))
    left = ["Protective ground", "Transmitted data", "Received data",
            "Request to send", "Clear to send", "DCE ready", "Signal ground",
            "Data carrier detect", "", "", "Secondary data set ready",
            "Secondary clear to send", ""]
    right = ["Secondary transmitted data", "Transmitter clock",
             "Secondary received data", "Receiver clock", "Local loop back",
             "Secondary request to send", "DTE ready", "Remote loopback",
             "Ring indicator", "Data rate selector",
             "External transmitter clock", "Test mode"]
    for i in range(13):
        y = 56 + i * 11.5
        o.append(_circle(330, y, 2.2, fill="#ffffff", sw=1.0))
        if left[i]:
            o.append(T(326, y + 2.3, left[i], 6.6, anchor="end"))
    for i in range(12):
        y = 56 + i * 11.5
        o.append(_circle(350, y, 2.2, fill="#ffffff", sw=1.0))
        o.append(T(354, y + 2.3, right[i], 6.6, anchor="start"))
    o.append(T(340, 220, "DTE / DCE signal names by pin", 7.0, color=GREY))
    return _mk(36, o, "RS-232 25-pin connector signals",
               "Tín hiệu chân kết nối RS-232 25 chân",
               "RS-232 25-pin connector signal assignments",
               "Sơ đồ chân kết nối RS-232 25 chân với các tên tín hiệu bảo vệ, truyền và nhận dữ liệu, điều khiển, đồng hồ và các tín hiệu phụ ở hai cột.",
               "Diagram of the 25-pin RS-232 connector listing protective ground, data, control, clock and secondary signal names in two columns.")


# ---------------------------------------------------------------- 5.37
@_reg
def fig_f37():
    """Fig. 5.37 - three-wire RS-232 and four-wire RS-422 connections."""
    o = [_defs()]
    # upper panel: 3-wire RS-232
    o.append(_rect(70, 42, 180, 56, fill="#fbfaf7", sw=1.2))
    o.append(_rect(430, 42, 180, 56, fill="#fbfaf7", sw=1.2))
    for y, la, lb in ((56, "Transmitted data", "Received data"),
                      (70, "Received data", "Transmitted data"),
                      (84, "Ground", "Ground")):
        o.append(_line(250, y, 430, y, sw=1.1))
        o.append(_terminal(250, y))
        o.append(_terminal(430, y))
        o.append(T(244, y + 2.3, la, 6.6, anchor="end"))
        o.append(T(436, y + 2.3, lb, 6.6, anchor="start"))
    o.append(_ellipse(340, 70, 11, 20, fill="#ffffff", sw=1.1))
    o.append(T(340, 108, "3-wire RS-232 connection", 7.4))

    # lower panel: 4-wire RS-422 with two twisted pairs
    o.append(_rect(70, 126, 180, 70, fill="#fbfaf7", sw=1.2))
    o.append(_rect(430, 126, 180, 70, fill="#fbfaf7", sw=1.2))
    for y, la, lb in ((142, "Transmit", "Receive"),
                      (154, "", ""),
                      (168, "Receive", "Transmit"),
                      (180, "", "")):
        o.append(_line(250, y, 430, y, sw=1.1))
        o.append(_terminal(250, y))
        o.append(_terminal(430, y))
        if la:
            o.append(T(244, y + 2.3, la + " +", 6.6, anchor="end"))
            o.append(T(244, y + 12, "−", 6.6, anchor="end"))
            o.append(T(436, y + 2.3, "+ " + lb, 6.6, anchor="start"))
            o.append(T(436, y + 12, "−", 6.6, anchor="start"))
    o.append(_ellipse(300, 148, 8, 13, fill="#ffffff", sw=1.0))
    o.append(_ellipse(380, 174, 8, 13, fill="#ffffff", sw=1.0))
    o.append(T(340, 162, "Twisted pair", 6.6, color=GREY))
    o.append(T(340, 134, "Data", 6.8, color=BLUE))
    o.append(_ar(300, 139, 390, 139, sw=1.1, color=BLUE))
    o.append(T(340, 194, "Data", 6.8, color=GREEN))
    o.append(_ar(390, 199, 300, 199, sw=1.1, color=GREEN))
    o.append(T(340, 216, "4-wire RS-422 connection", 7.4))
    return _mk(37, o, "RS-232 and RS-422 connection wiring",
               "Đấu nối ba dây RS-232 và bốn dây RS-422",
               "Three-wire RS-232 and four-wire RS-422 connections",
               "So sánh hai sơ đồ đấu nối: RS-232 dùng ba dây truyền, nhận và mass; RS-422 dùng bốn dây với hai cặp xoắn đôi cho truyền và nhận ở hai đầu.",
               "Comparison of a three-wire RS-232 link and a four-wire RS-422 link with two twisted pairs for separate transmit and receive directions.")


# ---------------------------------------------------------------- 5.38
@_reg
def fig_f38():
    """Fig. 5.38 - RS-485 standard multidrop link with three attachments."""
    o = [_defs()]
    boxes = [(90, "Digital\nattachment 1"), (280, "Digital\nattachment 2"),
             (470, "Digital\nattachment 3")]
    for x, lab in boxes:
        o.append(_b(x, 45, 140, 50, lab, size=7.4))
    for x in (130, 320, 510):
        o.append(_terminal(x, 95, "+"))
        o.append(_line(x, 98, x, 130, sw=1.1))
    for x in (190, 380, 570):
        o.append(_terminal(x, 95, "−"))
        o.append(_line(x, 98, x, 152, sw=1.1))
    o.append(_line(80, 130, 620, 130, sw=1.5, color=BLUE))
    o.append(_line(80, 152, 620, 152, sw=1.5, color=GREEN))
    for x in (250, 445):
        o.append(_ellipse(x, 141, 9, 15, fill="#ffffff", sw=1.1))
    o.append(T(150, 174, "Twisted wire pair", 7.0))
    o.append(_ar(195, 170, 243, 152, sw=1.0, color=GREY))
    o.append(T(340, 194, "RS-485 standard link", 7.8))
    o.append(T(340, 214, "Bus topology with more than two digital attachments",
               6.8, color=GREY))
    return _mk(38, o, "RS-485 standard link",
               "Liên kết chuẩn RS-485 dạng bus",
               "RS-485 standard multidrop link",
               "Sơ đồ ba thiết bị số nối song song vào bus hai dây xoắn đôi RS-485 qua các cặp cọc dương và âm.",
               "Diagram of three digital attachments connected in parallel to a two-wire twisted-pair RS-485 bus through positive and negative terminals.")


# ---------------------------------------------------------------- 5.39
@_reg
def fig_f39():
    """Fig. 5.39 - printed Ethernet message packet field format."""
    o = [_defs()]
    o.append(T(340, 68, "Ethernet message packet format", 8.4))
    fields = [(40, 110, "Preamble", False),
              (110, 215, "Destination", True),
              (215, 310, "Source", True),
              (310, 385, "Type", True),
              (385, 490, "Data", True),
              (490, 640, "Frame Check", True)]
    for i, (x0, x1, name, two) in enumerate(fields):
        fill = "#eef3fb" if i % 2 == 0 else "#fbfaf7"
        o.append(_rect(x0, 90, x1 - x0, 50, fill=fill, sw=1.2))
        cx = (x0 + x1) / 2.0
        if two:
            o.append(T(cx, 112, name, 7.2))
            tail = {110: "Address", 215: "Address", 310: "Field",
                    385: "Field", 490: "Sequence"}[x0]
            o.append(T(cx, 124, tail, 7.2))
        else:
            o.append(T(cx, 118, name, 7.2))
    o.append(T(340, 166, "Fields of a frame sent over the Ethernet link",
               7.0, color=GREY))
    return _mk(39, o, "Ethernet message packet format",
               "Cấu trúc khung tin Ethernet",
               "Ethernet message packet field format",
               "Khung tin Ethernet gồm các trường preamble, địa chỉ đích, địa chỉ nguồn, loại, dữ liệu và chuỗi kiểm tra khung.",
               "Ethernet packet divided into preamble, destination address, source address, type field, data field and frame check sequence.")


# ---------------------------------------------------------------- 5.40
@_reg
def fig_f40():
    """Fig. 5.40 - CAN message frame field structure."""
    o = [_defs()]
    o.append(T(340, 72, "CAN message frame format", 8.4))
    names = ["SOF", "ARB", "RTR", "CTRL", "DATA", "CRC", "ACK", "EOF"]
    for i, nm in enumerate(names):
        x = 40 + i * 75
        fill = "#eef3fb" if i % 2 == 0 else "#fbfaf7"
        o.append(_rect(x, 95, 75, 50, fill=fill, sw=1.2))
        o.append(T(x + 37.5, 125, nm, 8.0))
    for cx, lab in ((302.5, "6 bit"), (377.5, "up to 8 bytes"),
                    (452.5, "16 bit"), (527.5, "2 bit")):
        o.append(T(cx, 160, lab, 6.6, color=GREY))
    o.append(T(340, 184, "ARB arbitration, RTR remote request, CRC error check",
               6.8, color=GREY))
    return _mk(40, o, "CAN message frame format",
               "Cấu trúc khung tin CAN",
               "CAN message frame field format",
               "Khung tin CAN gồm tám trường SOF, ARB, RTR, CTRL, DATA, CRC, ACK và EOF, trong đó CRC kiểm lỗi 16 bit và ACK chiếm 2 bit.",
               "CAN message frame with eight fields SOF, ARB, RTR, CTRL, DATA, CRC, ACK and EOF, including a 16-bit CRC and a 2-bit ACK.")


# ---------------------------------------------------------------- 5.41
@_reg
def fig_f41():
    """Fig. 5.41 - twin-axial cable link from host PC to universal I/O modules."""
    o = [_defs()]
    o.append(_rect(70, 50, 160, 80, fill="#fbfaf7", sw=1.4))
    for x in (95, 110, 125):
        o.append(_line(x, 62, x, 118, sw=1.6, color=BLUE))
    o.append(_ellipse(180, 90, 24, 28, fill="#ffffff", sw=1.2))
    o.append(T(150, 144, "Host PC", 7.6))
    o.append(T(150, 154, "loaded with software", 7.0))

    o.append(_line(230, 87, 390, 87, sw=1.2, color=BLUE))
    o.append(_line(230, 93, 390, 93, sw=1.2, color=GREEN))
    o.append(T(310, 78, "Twin axial cable", 7.0))

    o.append(_rect(390, 62, 80, 56, fill="#eef3fb", sw=1.4))
    o.append(_rect(405, 74, 50, 32, fill="#ffffff", sw=1.0))
    o.append(T(478, 84, "Power supply", 7.0, anchor="start"))
    o.append(T(478, 94, "system", 7.0, anchor="start"))

    for i in range(5):
        y = 130 + i * 16
        o.append(_rect(413, y, 34, 14, fill="#fbfaf7", sw=1.2))
        o.append(_rect(422, y + 3, 16, 8, fill="#ffffff", sw=0.9))
        if i < 4:
            o.append(_line(430, y + 14, 430, y + 16, sw=1.1))
    o.append(_line(430, 118, 430, 130, sw=1.1))
    o.append(_path("M500,140 Q534,174 456,204", sw=1.0,
                   color=GREY, dash="4,3"))
    o.append(_poly([(456, 204), (469, 200), (461, 213)],
                   fill=GREY, sw=0))
    o.append(T(534, 166, "Universal", 7.0, anchor="start"))
    o.append(T(534, 176, "I/O modules", 7.0, anchor="start"))
    return _mk(41, o, "Twin-axial DAQ link with power supply",
               "Liên kết DAQ dùng cáp đồng trục kép và nguồn",
               "Twin-axial cable link in a distributed DAQ system",
               "Sơ đồ PC chủ nối qua cáp đồng trục kép tới nguồn và chuỗi năm mô-đun I/O đa năng.",
               "Diagram of a host PC linked by twin-axial cable to a power supply unit and a chain of five universal I/O modules.")


# ---------------------------------------------------------------- 5.42
@_reg
def fig_f42():
    """Fig. 5.42 - two-wire EIA RS-485 network with a repeater."""
    o = [_defs()]
    # host PC
    o.append(_rect(300, 42, 60, 28, fill="#eef3fb", sw=1.2))
    o.append(_rect(307, 47, 46, 18, fill="#ffffff", sw=0.9))
    o.append(_poly([(315, 70), (345, 70), (352, 76), (308, 76)],
                   fill="#fbfaf7", sw=1.0, close=True))
    o.append(T(330, 34, "Host PC", 7.2))
    o.append(_line(330, 76, 330, 100, sw=1.2))

    # bus wires
    o.append(_line(60, 100, 628, 100, sw=1.5, color=BLUE))
    o.append(_line(60, 104, 628, 104, sw=1.5, color=GREEN))
    o.append(T(470, 88, "2-wire EIA RS-485 network", 7.4, anchor="start"))

    # universal input modules, three locations
    for x, y, w, bars in ((90, 140, 40, 3), (250, 140, 40, 3),
                          (175, 152, 50, 4)):
        o.append(_rect(x, y, w, 24, fill="#fbfaf7", sw=1.2))
        for k in range(bars):
            bx = x + 7 + k * ((w - 14) / max(1, bars - 1))
            o.append(_line(bx, y + 4, bx, y + 20, sw=1.1, color=BLUE))
        o.append(_line(x + w / 2.0, 104, x + w / 2.0, y, sw=1.1))
    o.append(T(200, 190, "Universal input modules", 6.8))
    o.append(T(200, 200, "installed on three locations", 6.8))

    # repeater in the bus
    o.append(_rect(360, 90, 70, 26, fill="#eef3fb", sw=1.3))
    o.append(T(395, 107, "Repeater", 7.2))

    # universal output modules
    for x in (480, 560):
        o.append(_rect(x, 140, 40, 24, fill="#fbfaf7", sw=1.2))
        for k in range(3):
            o.append(_line(x + 8 + k * 12, 144,
                           x + 8 + k * 12, 160, sw=1.1, color=GREEN))
        o.append(_line(x + 20, 104, x + 20, 140, sw=1.1))
    o.append(T(540, 190, "Universal output modules", 6.8))
    o.append(_ar(300, 122, 300, 108, sw=1.2, color=BLUE))
    o.append(_ar(545, 108, 545, 122, sw=1.2, color=GREEN))
    return _mk(42, o, "Two-wire RS-485 network with repeater",
               "Mạng RS-485 hai dây có bộ lặp",
               "Two-wire RS-485 network with a repeater",
               "Sơ đồ mạng RS-485 hai dây nối PC chủ với các mô-đun vào và ra qua một bộ lặp giữa bus.",
               "Diagram of a two-wire RS-485 network linking a host PC to universal input and output modules with a repeater in the bus.")


# ---------------------------------------------------------------- 5.43
@_reg
def fig_f43():
    """Fig. 5.43 - three levels of I/O, power and communication isolation."""
    o = [_defs()]
    # upper row: I/O module, local bus, host PC, opto-coupler, controller
    o.append(_b(50, 45, 115, 50, "Universal I/O\nModule with\ncounter",
                size=6.8))
    o.append(_ar(165, 70, 220, 70, sw=1.3))
    o.append(T(192, 60, "Local Bus", 6.8))
    o.append(_b(220, 45, 110, 50, "Host PC", size=7.8))
    o.append(_line(330, 70, 352, 70, sw=1.1))
    o.append(_path("M352,70 q5,-10 10,0 q5,-10 10,0", sw=1.1, color=BLUE))
    o.append(_path("M418,70 q-5,-10 -10,0 q-5,-10 -10,0",
                   sw=1.1, color=BLUE))
    o.append(_line(385, 52, 385, 88, sw=1.6, color=GREY))
    o.append(_line(418, 70, 440, 70, sw=1.1))
    o.append(T(385, 104, "Opto-coupler", 6.8))
    o.append(T(385, 114, "communication isolation", 6.2, color=GREY))
    o.append(_b(440, 45, 160, 50, "Communication\ncontroller", size=7.2))
    o.append(_ar(600, 62, 654, 62, sw=1.2))
    o.append(_ar(654, 84, 600, 84, sw=1.2))
    o.append(T(628, 54, "Data", 6.8))

    # watchdog timer and 5 V supply
    o.append(_b(100, 120, 130, 38, "Watch dog timer\nand reset", size=6.8))
    o.append(_ar(220, 139, 286, 139, sw=1.1, color=GREY))
    o.append(_b(300, 120, 90, 38, "+5V\nSupply", size=7.0))
    o.append(_line(345, 158, 345, 175, sw=1.1))
    o.append(_ar(250, 120, 250, 96, sw=1.2, color=BLUE))
    o.append(_line(250, 175, 250, 120, sw=1.1))

    # isolation transformer and converted supply
    o.append(_line(38, 190, 52, 190, sw=1.1))
    o.append(_path("M52,190 q5,-10 10,0 q5,-10 10,0", sw=1.1, color=BLUE))
    o.append(_line(78, 176, 78, 204, sw=1.6, color=GREY))
    o.append(_path("M104,190 q-5,-10 -10,0 q-5,-10 -10,0",
                   sw=1.1, color=BLUE))
    o.append(_line(104, 190, 110, 190, sw=1.1))
    o.append(_b(110, 174, 105, 36, "Rectifier\nand filter", size=6.8))
    o.append(_b(260, 174, 160, 36, "+10 to +30 volt\nconvertor", size=6.8))
    o.append(_line(215, 182, 260, 182, sw=1.1))
    o.append(_line(215, 202, 260, 202, sw=1.1))
    o.append(T(78, 218, "power isolation via transformer", 6.2,
               color=GREY))
    o.append(T(540, 192, "3000 V DC I/O and power", 6.4,
               anchor="start", color=GREY))
    o.append(T(540, 202, "2500 V DC communication", 6.4,
               anchor="start", color=GREY))
    return _mk(43, o, "Three-level I/O isolation",
               "Cách ly ba mức cho I/O và truyền thông",
               "Three-level I/O, power and communication isolation",
               "Sơ đồ cách ly ba mức: bus cục bộ cho I/O, biến áp cho nguồn và ghép quang cho bộ điều khiển truyền thông, kèm bộ đếm watchdog.",
               "Diagram of three isolation levels: local bus for I/O, transformer for power and opto-coupler for the communication controller, with a watchdog timer.")
