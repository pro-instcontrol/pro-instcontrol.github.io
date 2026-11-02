# -*- coding: utf-8 -*-
"""Figures 86.1–86.7 for Handbook Chapter 86 — Computers.

86.1   elements of a computer-based instrumentation system
86.2   an overview of a single-board computer
86.3   a simplified model of a computer bus
86.4   the VMEbus arbitration daisy chain
86.5   (a) a software-handshake and (b) a hardware-handshake null modem
86.6   two timers producing pulse-width modulation
86.7   the layer model of instrumentation software

All seven were read off the 200 dpi page rasters; 86.5 was additionally read at
600 dpi because the pin mnemonics are set at about 6 pt. Nothing here is
generated from a formula — every wire in 86.5 and every level in 86.6 is a
transcription of the printed drawing.

Two printed defects are reproduced as-is and flagged in the chapter note:
Figure 86.3 draws four rails but four stubs per card in a staircase, so the
figure does not distinguish data from control lines within a card; and the
caption of 86.5 describes scheme (b) as "DTR–DSR" when the drawing crosses
DTR to the *other* device's DSR.

NOTE: never emit <sub>/<sup> inside <svg> text — both are on the HTML parser's
breakout list and eject the parser from SVG foreign content.
"""
from hbfig import svg, _fig
from hb93base import (E, S, _defs, _lbl, _line, _arr, _rect, _path, _dot)

GREY = "#8a8a8a"

# The shared .tm class is 9.5 px, sized for the dense schematics of Chapters
# 87 and 93. These seven figures are block diagrams with very few words, and
# at 9.5 px the labels sit at about a third of the box width the print gives
# them. A local class at 12.5 px restores the printed proportion; it is
# declared after _defs() so it wins on source order.
_EXTRA = ('<style>'
          '.tl{font:12.5px Inter,Helvetica,sans-serif;fill:#222}'
          '.tls{font:11px Inter,Helvetica,sans-serif;fill:#555}'
          '.tlt{font:13px Inter,Helvetica,sans-serif;fill:#111}'
          '</style>')


def _start(tag):
    return _defs(tag) + _EXTRA


# ================================================================ helpers
def _box(x, y, w, h, lines, sw=1.3, lh=14.0, cls="tl"):
    """A rectangle with centred, multi-line text."""
    o = [_rect(x, y, w, h, sw)]
    n = len(lines)
    for i, t in enumerate(lines):
        yy = y + h / 2.0 + (i - (n - 1) / 2.0) * lh + 3.4
        o.append(_lbl(x + w / 2.0, yy, t, cls, "middle"))
    return "".join(o)


def _rail(x1, x2, y, sw=1.6):
    return _line(x1, y, x2, y, sw)


def _stair(x0, y0, segs, sw=1.4):
    """A polyline from (x0,y0) through a list of (dx, dy) steps."""
    pts = [(x0, y0)]
    x, y = x0, y0
    for dx, dy in segs:
        x += dx
        y += dy
        pts.append((x, y))
    return _path(pts, sw)


def _square(x0, p, n, hi, lo, sw=1.5):
    """An n-cycle square wave of period p between levels hi and lo."""
    pts = [(x0, lo), (x0, hi)]
    x = x0
    for _ in range(n):
        pts.append((x + p / 2.0, hi))
        pts.append((x + p / 2.0, lo))
        x += p
        pts.append((x, lo))
        pts.append((x, hi))
    pts.append((x, lo))
    return _path(pts, sw)


def _pulse(x0, w, n, period, hi, lo, sw=1.5):
    """n narrow positive pulses of width w, one every `period`."""
    pts = [(x0, lo)]
    x = x0
    for _ in range(n):
        pts += [(x, hi), (x + w, hi), (x + w, lo)]
        x += period
        pts.append((x, lo))
    return _path(pts, sw)


def _blocks(x0, x1, blocks, hi, lo, sw=1.5):
    """blocks = [(start, end), ...] in canvas x; high inside, low outside."""
    pts = [(x0, hi)]
    for i, (a, b) in enumerate(blocks):
        if i:
            pts += [(a, lo), (a, hi)]
        pts += [(b, hi), (b, lo)]
    pts.append((x1, lo))
    return _path(pts, sw)


# ================================================================ 86.1
def fig_86_1():
    tag = "861"
    b = [_start(tag)]
    b.append(_box(210, 14, 260, 72,
                  ["Sensors and Signal", "Conditioning", "Circuitry"]))
    b.append(_arr(340, 86, 340, 110, tag))
    b.append(_box(210, 112, 260, 56, ["Digitizer"]))
    # the spine
    b.append(_line(340, 168, 340, 392, 1.5))
    b.append(_box(200, 394, 280, 58, ["Central Processing", "Unit (CPU)"]))
    # branches
    b.append(_line(340, 237, 430, 237, 1.5))
    b.append(_box(430, 210, 200, 54, ["Data store", "e.g. RAM disk"]))
    b.append(_line(270, 265, 340, 265, 1.5))
    b.append(_rect(70, 190, 200, 150, 1.3))
    b.append(_lbl(170, 214, "Human Computer", "tl", "middle"))
    b.append(_lbl(170, 227, "Interface e.g.", "tl", "middle"))
    for i, w in enumerate(["keyboard", "mouse", "vdu", "printer"]):
        yy = 254 + i * 20
        b.append(_dot(96, yy - 3.2, 1.9))
        b.append(_lbl(106, yy, w, "tl"))
    b.append(_line(340, 344, 430, 344, 1.5))
    b.append(_box(430, 300, 200, 88,
                  ["Communications", "Interface e.g.", "Ethernet, IEEE-488,",
                   "RS-232"], lh=14))
    body = "".join(b)
    return _fig(
        svg(680, 470, body, "Các thành phần của một hệ đo lường dựa trên máy tính"),
        "Hình 86.1 · Các thành phần của một hệ đo lường dựa trên máy tính.",
        "Figure 86.1 · Elements of a computer-based instrumentation system.",
        "Sơ đồ khối: cảm biến và mạch điều kiện tín hiệu, bộ số hoá, rồi một trục bus "
        "nối tới giao diện người–máy, kho dữ liệu, giao diện truyền thông và CPU",
        "Block diagram: sensors and signal conditioning, digitizer, then a bus spine "
        "feeding the human-computer interface, data store, communications interface and CPU")


# ================================================================ 86.2
def fig_86_2():
    tag = "862"
    b = [_start(tag)]
    # buses
    b.append(_line(390, 350, 390, 96, 2.8))                  # data bus, thick
    b.append(_line(300, 350, 300, 96, 1.3, E, "7 5"))        # address bus
    # microprocessor
    b.append(_box(245, 350, 190, 54, ["Microprocessor"]))
    # parallel interface with its two 8-bit ports
    b.append(_box(245, 40, 190, 56, ["Parallel Interface"]))
    b.append(_arr(272, 40, 272, 16, tag))
    b.append(_arr(408, 16, 408, 40, tag))
    b.append(_lbl(264, 30, "8", "tls", "end"))
    b.append(_lbl(416, 30, "8", "tls", "start"))
    # memory
    b.append(_box(60, 120, 130, 60, ["RAM"]))
    b.append(_box(60, 230, 130, 60, ["ROM/EPROM"]))
    # serial
    b.append(_box(470, 140, 120, 150, ["Serial", "Interface"], lh=16))
    b.append(_arr(590, 190, 660, 190, tag))
    b.append(_arr(660, 300, 590, 300, tag))
    # data-bus branches (solid, arrow into the peripheral)
    b.append(_arr(390, 150, 190, 150, tag))
    b.append(_arr(390, 260, 190, 260, tag))
    b.append(_arr(390, 190, 470, 190, tag))
    # address-bus branches (dashed)
    b.append(_arr(300, 168, 190, 168, tag, 1.15, E, "h"))
    b.append(_arr(300, 278, 190, 278, tag, 1.15, E, "h"))
    b.append(_arr(300, 225, 470, 225, tag, 1.15, E, "h"))
    # bus labels with leaders
    b.append(_lbl(150, 340, "Address Bus", "tl", "end"))
    b.append(_line(156, 336, 292, 326, 0.9, GREY))
    b.append(_lbl(470, 340, "Data Bus", "tl", "start"))
    b.append(_line(464, 336, 398, 326, 0.9, GREY))
    body = "".join(b)
    return _fig(
        svg(680, 420, body, "Sơ lược một máy tính một bảng mạch"),
        "Hình 86.2 · Sơ lược một máy tính một bảng mạch.",
        "Figure 86.2 · An overview of a single board computer.",
        "Sơ đồ máy tính một bảng mạch: vi xử lý nối với bus dữ liệu và bus địa chỉ, "
        "qua đó tới RAM, ROM/EPROM, giao diện song song và giao diện nối tiếp",
        "Single-board-computer diagram: a microprocessor driving a data bus and an "
        "address bus that reach RAM, ROM/EPROM, a parallel interface and a serial interface")


# ================================================================ 86.3
def fig_86_3():
    tag = "863"
    b = [_start(tag)]
    rails = [(120, "Data"), (144, "Control"), (168, "Arbitration"), (192, "Utility")]
    cards = [(118, ["SBC card 1"]), (240, ["Peripheral", "card 1"]),
             (362, ["Peripheral", "card 2"]), (484, ["SBC card 2"])]
    for cx, lines in cards:
        b.append(_box(cx, 16, 92, 58, lines, lh=14))
    # the stubs: stub j of each card lands on rail j
    for cx, _lines in cards:
        for j in range(4):
            x = cx + 12 + j * 24
            b.append(_line(x, 74, x, rails[j][0], 1.5))
    for y, lab in rails:
        b.append(_rail(60, 588, y))
        b.append(_lbl(602, y + 4.4, lab, "tl", "start"))
    body = "".join(b)
    return _fig(
        svg(680, 230, body, "Mô hình đơn giản hoá của một bus máy tính"),
        "Hình 86.3 · Mô hình đơn giản hoá của một bus máy tính.",
        "Figure 86.3 · A simplified model of a computer bus.",
        "Bốn thẻ mạch cắm xuống bốn đường ray bus nằm ngang: dữ liệu, điều khiển, "
        "phân xử và tiện ích",
        "Four circuit cards dropping onto four horizontal bus rails: data, control, "
        "arbitration and utility")


# ================================================================ 86.4
def fig_86_4():
    tag = "864"
    b = [_start(tag)]
    y0, yd = 120, 88
    # the four card boundaries
    for x in (225, 315, 425, 515):
        b.append(_line(x, 24, x, 180, 1.1, GREY))
    # the grant line, with a ramp up into each card's BGIN pin
    b.append(_line(90, y0, 205, y0, 1.5))
    b.append(_path([(205, y0), (265, yd)], 1.5))
    b.append(_line(265, y0, 395, y0, 1.5))
    b.append(_path([(395, y0), (455, yd)], 1.5))
    b.append(_line(455, y0, 600, y0, 1.5))
    for x in (265, 455):
        b.append(_dot(x, yd, 3.1))
        b.append(_dot(x, y0, 3.1))
        b.append(_lbl(x, yd - 9, "BGIN", "tl", "middle"))
        b.append(_lbl(x, y0 + 20, "BGOUT", "tl", "middle"))
    body = "".join(b)
    return _fig(
        svg(680, 200, body, "Chuỗi nối tiếp phân xử trên VMEbus"),
        "Hình 86.4 · Chuỗi nối tiếp (daisy chain) phân xử trên VMEbus.",
        "Figure 86.4 · VMEbus arbitration daisy chain.",
        "Đường cấp bus đi qua từng thẻ: vào ở chân BGIN và ra ở chân BGOUT, nên thẻ "
        "gần bộ điều khiển hệ thống nhất có độ ưu tiên cao nhất",
        "The bus-grant line passes through each card, entering at BGIN and leaving at "
        "BGOUT, so cards nearest the system controller have the highest priority")


# ================================================================ 86.5
_PINS = ["GND", "RI", "DTR", "DCD", "DSR", "RTS", "CTS", "TxD", "RxD"]
_PY = [46 + i * 24 for i in range(9)]


def _pin(y):
    return _PY[_PINS.index(y)]


def _panel(b, tag, xl, xr, w, letter, scheme):
    """One null-modem panel. xl/xr are the left edges of the two boxes."""
    o = []
    pl, pr = xl + w, xr                       # inner edges
    o.append(_lbl((xl + xr + w) / 2.0, 16, letter, "tl", "middle"))
    o.append(_rect(xl, 30, w, 232, 1.3))
    o.append(_rect(xr, 30, w, 232, 1.3))
    for p, y in zip(_PINS, _PY):
        o.append(_lbl(pl - 6, y + 3.2, p, "tl", "end"))
        o.append(_lbl(xr + 6, y + 3.2, p, "tl", "start"))
    # GND runs straight across
    o.append(_line(pl, _pin("GND"), xr, _pin("GND"), 1.3))

    if scheme == "a":
        # inside each box DTR is strapped to DCD, DSR and CTS
        for edge, xb, sgn in ((pl, pl + 9, -1), (xr, xr - 9, 1)):
            y1, y2 = _pin("DTR"), _pin("CTS")
            o.append(_line(edge, y1, xb, y1, 1.3))
            o.append(_line(xb, y1, xb, y2, 1.3))
            for pin in ("DCD", "DSR", "CTS"):
                yy = _pin(pin)
                o.append(_arr(xb, yy, edge, yy, tag, 1.15, E, "h"))
    else:
        # DTR of one device shows the other that it is present
        for a, bb in (("DTR", "DSR"), ("DSR", "DTR")):
            ya, yb = _pin(a), _pin(bb)
            left = a == "DTR"
            x0, x1 = (pl, xr) if left else (xr, pl)
            o.append(_path([(x0, ya), (x0 + (14 if left else -14), ya),
                            (x1 - (14 if left else -14), yb), (x1, yb)], 1.3))
            o.append(_arr(x1 + (-10 if left else 10), yb, x1, yb, tag, 1.15, E, "h"))
        # RTS of one device drives the other device's DCD
        ya, yb = _pin("RTS"), _pin("DCD")
        o.append(_path([(pl, ya), (pl + 14, ya), (xr - 14, yb), (xr, yb)], 1.3))
        o.append(_arr(xr - 10, yb, xr, yb, tag, 1.15, E, "h"))
        o.append(_path([(xr, ya), (xr - 14, ya), (pl + 14, yb), (pl, yb)], 1.3))
        o.append(_arr(pl + 10, yb, pl, yb, tag, 1.15, E, "h"))
        # RTS looped back to the local CTS
        for edge, xb, sgn in ((pl, pl + 9, -1), (xr, xr - 9, 1)):
            y1, y2 = _pin("RTS"), _pin("CTS")
            o.append(_line(edge, y1, xb, y1, 1.3))
            o.append(_line(xb, y1, xb, y2, 1.3))
            o.append(_arr(xb, y2, edge, y2, tag, 1.15, E, "h"))

    # TxD and RxD cross over
    for a, bb in (("TxD", "RxD"), ("RxD", "TxD")):
        ya, yb = _pin(a), _pin(bb)
        o.append(_path([(pl, ya), (pl + 10, ya), (xr - 10, yb), (xr, yb)], 1.3))
    return "".join(o)


def fig_86_5():
    tag = "865"
    b = [_start(tag)]
    b.append(_panel(b, tag, 44, 214, 76, "(a)", "a"))
    b.append(_panel(b, tag, 390, 560, 76, "(b)", "b"))
    body = "".join(b)
    return _fig(
        svg(680, 290, body, "Hai bộ null modem nối DTE với DTE"),
        "Hình 86.5 · Hai bộ null modem để nối DTE với DTE. Ở (a) toàn bộ việc bắt tay "
        "phải do phần mềm thực hiện: đường DTR “đánh lừa” giao diện nối tiếp rằng nó "
        "đang được nối với các đường bắt tay của một thiết bị khác. Sơ đồ (b) thực hiện "
        "bắt tay bằng phần cứng: đường nối DTR–DSR cho mỗi thiết bị biết rằng thiết bị "
        "kia đang hiện diện, còn các đường RTS — được nối với DCD của thiết bị kia, "
        "đường mà thiết bị đó có thể theo dõi — được dùng để điều khiển luồng dữ liệu "
        "theo cả hai chiều.",
        "Figure 86.5 · Two null modems for connecting DTE to DTE. In (a) all handshaking "
        "must be in software. The DTR line “fools” the serial interface that it is "
        "connected to the handshake lines of another device. Scheme (b) implements a "
        "hardware handshake. The DTR–DSR connection shows each device that the other is "
        "present. The RTS lines, connected to the DCD of the other device, which it can "
        "monitor, are used to control the flow of data in either direction.",
        "Hai sơ đồ null modem cạnh nhau, mỗi sơ đồ gồm hai hộp chân nối đối diện: ở (a) "
        "DTR được nối tắt cục bộ với DCD, DSR và CTS; ở (b) DTR và DSR bắt chéo nhau "
        "giữa hai thiết bị, RTS của bên này nối vào DCD của bên kia, còn RTS nối tắt "
        "với CTS tại chỗ",
        "Two null-modem panels, each with two facing pin blocks: in (a) DTR is strapped "
        "locally to DCD, DSR and CTS; in (b) DTR and DSR cross between the devices, each "
        "RTS drives the other device's DCD, and RTS is looped to the local CTS")


# ================================================================ 86.6
def fig_86_6():
    tag = "866"
    b = [_start(tag)]
    # the two timers
    b.append(_rect(150, 30, 140, 100, 1.3))
    b.append(_lbl(220, 50, "T1", "tl", "middle"))
    b.append(_lbl(158, 74, "trigger", "tl", "start"))
    b.append(_lbl(158, 102, "count", "tl", "start"))
    b.append(_lbl(282, 88, "output", "tl", "end"))
    b.append(_rect(390, 30, 140, 100, 1.3))
    b.append(_lbl(460, 50, "T2", "tl", "middle"))
    b.append(_lbl(398, 74, "trigger", "tl", "start"))
    b.append(_lbl(398, 102, "count", "tl", "start"))
    b.append(_lbl(522, 88, "output", "tl", "end"))
    # unused trigger stub on T1
    b.append(_line(120, 71, 150, 71, 1.3))
    # T1 output -> B -> T2 trigger
    b.append(_path([(290, 85), (348, 85), (348, 71), (390, 71)], 1.3))
    b.append(_lbl(356, 65, "B", "tl", "start"))
    # T2 output -> C
    b.append(_line(530, 85, 572, 85, 1.3))
    b.append(_lbl(578, 89, "C", "tl", "start"))
    # the external clock feeding both count inputs
    b.append(_line(90, 180, 368, 180, 1.3))
    b.append(_path([(128, 180), (128, 99), (150, 99)], 1.3))
    b.append(_path([(368, 180), (368, 99), (390, 99)], 1.3))
    b.append(_lbl(38, 172, "From", "tl", "start"))
    b.append(_lbl(38, 185, "clock", "tl", "start"))
    b.append(_lbl(100, 176, "A", "tl", "start"))
    # waveforms
    x0, p, n = 90, 30, 18
    b.append(_square(x0, p, n, 226, 250))
    b.append(_pulse(x0, 0.6 * p, 3, 6 * p, 286, 310))
    b.append(_blocks(x0, x0 + 18 * p,
                     [(x0, x0 + 4 * p), (x0 + 6 * p, x0 + 10 * p),
                      (x0 + 12 * p, x0 + 16 * p)], 346, 370))
    for lab, y in (("A", 238), ("B", 298), ("C", 358)):
        b.append(_lbl(62, y, lab, "tl", "middle"))
    body = "".join(b)
    return _fig(
        svg(680, 400, body, "Dùng hai bộ định thời tạo điều chế độ rộng xung"),
        "Hình 86.6 · Dùng hai bộ định thời để tạo điều chế độ rộng xung dưới sự điều "
        "khiển của phần mềm. Cả hai bộ định thời đều nhận xung vào ở tần số không đổi "
        "từ một đồng hồ ngoài, như hình A. Bộ định thời T1 làm việc ở chế độ liên tục; "
        "ở chế độ này xung kích không có tác dụng. Đầu ra của T1 là một xung dương đơn "
        "khi nó đã đếm đủ số xung vào do phần mềm quy định, như hình B. Bộ định thời T2 "
        "làm việc ở chế độ một lần (one-shot): mỗi khi nhận một xung kích, đầu ra của nó "
        "lên mức cao trong một số đếm do phần mềm quy định, như hình C. Bằng cách đó, "
        "tần số của đầu ra C do số đếm quy định cho T1 quyết định, còn độ rộng phần "
        "dương của C do số đếm quy định cho T2 quyết định.",
        "Figure 86.6 · Using two timers to produce pulse-width modulation under software "
        "control. Both timers receive input pulses at a constant frequency from an "
        "external clock, as shown at A. Timer T1 operates in continuous mode. The trigger "
        "has no effect in this mode. The output of T1 is a single positive-going pulse "
        "when it has counted the specified (by software) number of input pulses, as shown "
        "at B. Timer T2 operates in one-shot mode. Each time it receives a trigger pulse, "
        "its output goes high for a specified (again by software) number of counts, as "
        "shown at C. In this way the frequency of the output at C is controlled by the "
        "count specified for T1 and the width of the positive-going part of C is "
        "controlled by the count specified for T2.",
        "Sơ đồ hai bộ định thời T1 và T2 nối tiếp nhau, phía dưới là ba dạng sóng: A là "
        "chuỗi xung đồng hồ đều, B là xung hẹp lặp lại sau mỗi sáu chu kỳ, C là xung "
        "rộng có độ rộng thay đổi theo chu kỳ",
        "Two cascaded timers T1 and T2, above three waveforms: A is the regular clock "
        "train, B a narrow pulse every six cycles, C a wide pulse whose width varies "
        "cycle by cycle")


# ================================================================ 86.7
def fig_86_7():
    tag = "867"
    b = [_start(tag)]
    b.append(_rect(160, 20, 360, 56, 1.3))
    b.append(_lbl(340, 42, "Application Layer", "tl", "middle"))
    b.append(_lbl(340, 62, "– acquisition, analysis and presentation –", "tls", "middle"))
    b.append(_rect(160, 76, 360, 34, 1.3))
    b.append(_lbl(340, 97, "Instrument Drivers", "tl", "middle"))
    b.append(_rect(160, 110, 360, 34, 1.3))
    b.append(_lbl(340, 131, "Device Drivers", "tl", "middle"))
    body = "".join(b)
    return _fig(
        svg(680, 168, body, "Mô hình phân lớp cho các hệ đo lường"),
        "Hình 86.7 · Mô hình phân lớp cho các hệ đo lường.",
        "Figure 86.7 · A layer model for instrumentation systems.",
        "Ba lớp xếp chồng: lớp ứng dụng ở trên, rồi tới bộ điều khiển thiết bị đo và "
        "bộ điều khiển thiết bị phần cứng ở dưới",
        "Three stacked layers: the application layer on top, then instrument drivers, "
        "then device drivers")
