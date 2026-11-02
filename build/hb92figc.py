# -*- coding: utf-8 -*-
"""Figures 92.13–92.16 for Handbook Chapter 92 — Liquid Crystal Displays.

92.13  AM LCD module electronics (a) and a magnified view of the TFT array (b)
92.14  cross-section through an AM LCD
92.15  plan layout of one TFT-LCD pixel
92.16  pixel equivalent circuit, gate waveform, data and pixel waveforms
"""
import math

from hbfig import svg, _fig, _f
from hb92base import (E, S, GRID, GOLD, BLUE, TEAL, RED, GREEN, GLASS, DIELE, METAL,
                      INK, ROD, RODHI, GLASSBLUE, POLAR, ITO,
                      _defs, _lbl, _r, _line, _arr, _rect, _poly, _path, _dot, _circ,
                      _hatch, Frame)


# ---------------------------------------------------------------- helpers
def _box(x, y, w, h, lines, fill="#fdfdfd", sw=1.0, col=E, cls="ts"):
    o = [_rect(x, y, w, h, sw, fill, "", col)]
    n = len(lines)
    for i, t in enumerate(lines):
        yy = y + h / 2.0 + (i - (n - 1) / 2.0) * 12 + 3.4
        o.append(_lbl(x + w / 2.0, yy, t, cls, "middle"))
    return "".join(o)


def _cap_h(xc, yc, col=E):
    """A capacitor on a vertical wire: two horizontal plates."""
    return (_line(xc - 7, yc - 3, xc + 7, yc - 3, 1.3, col)
            + _line(xc - 7, yc + 3, xc + 7, yc + 3, 1.3, col))


def _cap_v(xc, yc, col=E):
    """A capacitor on a horizontal wire: two vertical plates."""
    return (_line(xc - 3, yc - 7, xc - 3, yc + 7, 1.3, col)
            + _line(xc + 3, yc - 7, xc + 3, yc + 7, 1.3, col))


def _pxcell(x, y, w, h):
    """One pixel of the schematic array: TFT, node, C_LC down, C_S across."""
    o = []
    o.append(_rect(x + 6, y + 6, 20, 14, 0.9, "#fff", "", E))
    o.append(_line(x + 16, y, x + 16, y + 6, 0.9, E))            # gate lead
    o.append(_line(x, y + 13, x + 6, y + 13, 0.9, E))            # source
    o.append(_line(x + 26, y + 13, x + 44, y + 13, 0.9, E))      # drain
    o.append(_dot(x + 44, y + 13, 2.2, E))
    # C_LC down to the common rail
    o.append(_line(x + 44, y + 13, x + 44, y + h - 20, 0.9, E))
    o.append(_cap_h(x + 44, y + h - 16))
    o.append(_line(x + 44, y + h - 13, x + 44, y + h, 0.9, E))
    # C_S across, then up to the gate line
    o.append(_line(x + 44, y + 13, x + w - 26, y + 13, 0.9, E))
    o.append(_cap_v(x + w - 23, y + 13))
    o.append(_line(x + w - 20, y + 13, x + w - 12, y + 13, 0.9, E))
    o.append(_line(x + w - 12, y + 13, x + w - 12, y, 0.9, E))
    return "".join(o)


# ================================================================ 92.13
def fig_92_13():
    tag = "9213"
    o = [_defs(tag)]

    # ------------------------------------------------ (a) block diagram
    o.append(_lbl(18, 20, "(a)", "ts"))
    o.append(_box(18, 84, 90, 52, ["Host", "điều khiển"]))
    o.append(_box(140, 68, 142, 84,
                  ["Khối điều khiển", "dịch mức · thời gian", "chức năng tương tự"]))
    o.append(_box(316, 36, 96, 36, ["Driver cột"]))
    o.append(_box(316, 128, 96, 36, ["Driver hàng"]))
    o.append(_box(140, 176, 142, 32, ["Nguồn cấp"]))

    o.append(_rect(450, 30, 192, 158, 1.1, "#fcfcfc", "", E))
    o.append(_lbl(546, 46, "Panel LCD (ma trận TFT)", "ts", "middle"))
    for i in range(5):
        o.append(_line(466 + i * 40, 56, 466 + i * 40, 174, 0.7, "#cccccc"))
    for j in range(4):
        o.append(_line(466, 56 + j * 39.3, 626, 56 + j * 39.3, 0.7, "#cccccc"))

    o.append(_arr(108, 110, 140, 110, tag, 1.1, S, "h"))
    o.append(_arr(282, 90, 316, 56, tag, 1.1, S, "h"))
    o.append(_arr(282, 130, 316, 144, tag, 1.1, S, "h"))
    o.append(_arr(412, 54, 450, 54, tag, 1.1, S, "h"))
    o.append(_arr(412, 146, 450, 146, tag, 1.1, S, "h"))
    # power feeds control, the row driver and (routed round the outside) the
    # column driver
    o.append(_arr(211, 176, 211, 152, tag, 0.9, S, "h"))
    o.append(_arr(364, 176, 364, 164, tag, 0.9, S, "h"))
    o.append(_line(282, 192, 430, 192, 0.9, S))
    # the vertical run hops over the row-driver -> panel arrow (gap, no join)
    o.append(_line(430, 192, 430, 152, 0.9, S))
    o.append(_line(430, 140, 430, 54, 0.9, S))
    o.append(_arr(430, 54, 412, 54, tag, 0.9, S, "h"))

    # ------------------------------------------------ (b) magnified array
    o.append(_lbl(18, 244, "(b)", "ts"))
    xs = [100, 210, 320, 430]
    ys = [272, 370]
    h = 76
    for x in xs:                                   # data lines
        o.append(_line(x, 272, x, 446, 0.9, E))
    for y in ys:
        o.append(_line(100, y, 430, y, 0.9, E))    # gate lines
        o.append(_line(100, y + h, 430, y + h, 0.8, S, "5 4"))   # common rail
    for y in ys:
        for x in xs[:-1]:
            o.append(_pxcell(x, y, 110, h))

    # labels around the array
    o.append(_lbl(160, 252, "Đường cổng", "ts", "middle"))
    o.append(_line(160, 256, 160, 270, 0.7, S))
    o.append(_lbl(30, 268, "TFT", "ts"))
    o.append(_line(54, 264, 106, 280, 0.7, S))
    o.append(_r(30, 340, [("C", False), ("LC", True)], "start", "ts"))
    o.append(_line(60, 336, 140, 332, 0.7, S))
    o.append(_r(470, 286, [("C", False), ("S", True)], "start", "ts"))
    o.append(_line(466, 282, 410, 285, 0.7, S))
    o.append(_lbl(470, 340, "Đường dữ liệu", "ts"))
    o.append(_line(466, 336, 432, 340, 0.7, S))
    o.append(_r(470, 362, [("V", False), ("com", True)], "start", "ts"))
    o.append(_line(466, 358, 432, 348, 0.7, S))

    return _fig(
        svg(660, 470, "".join(o),
            "Điện tử mô-đun LCD ma trận chủ động"),
        "Hình 92.13 · (a) Sơ đồ khối điện tử của mô-đun LCD ma trận chủ động: bộ điều khiển chủ "
        "đưa dữ liệu số tới khối điều khiển, khối này tạo xung nhịp và mức tín hiệu cho các driver "
        "cột và hàng để quét ma trận TFT trên panel. (b) Phóng to một vùng của ma trận: mỗi điểm "
        "ảnh có một TFT, điện dung lớp tinh thể lỏng C<sub>LC</sub> và tụ tích trữ C<sub>S</sub>.",
        "Figure 92.13 · (a) Block diagram of the electronics of an active-matrix LCD module: the "
        "host controller feeds digital data to the control block, which generates the timing and "
        "signal levels for the column and row drivers that scan the TFT array on the panel. "
        "(b) Magnified region of the array: each pixel has a TFT, the liquid-crystal capacitance "
        "C<sub>LC</sub> and a storage capacitor C<sub>S</sub>.",
        "Sơ đồ khối mô-đun LCD ma trận chủ động và sơ đồ mạch phóng to của lưới điểm ảnh TFT",
        "A block diagram of an active-matrix LCD module beside a magnified schematic of the TFT "
        "pixel grid")


# ================================================================ 92.14
def fig_92_14():
    tag = "9214"
    o = [_defs(tag)]
    bx, bw = 180, 230
    y = 30
    rows = [
        (6,  POLAR,     "Phin phân cực trên"),
        (20, GLASSBLUE, "Kính trên"),
        (5,  ITO,       "Điện cực chung ITO"),
        (24, None,      "Lọc màu R/G/B"),
        (5,  "#e8e8e8", "Lớp định hướng"),
        (52, "#fbfbfb", "Tinh thể lỏng"),
        (5,  "#e8e8e8", "Lớp định hướng"),
        (5,  ITO,       "Điện cực ITO"),
        (20, GLASSBLUE, "Kính dưới"),
        (6,  POLAR,     "Phin phân cực dưới"),
    ]
    mids, tops = [], []
    for (th, fill, lab) in rows:
        tops.append(y)
        mids.append(y + th / 2.0)
        if fill is None:
            seg = bw / 3.0
            for c, cc in enumerate(("#f6cccc", "#cbe7cc", "#ccdcf6")):
                o.append(_rect(bx + c * seg + 1, y, seg - 2, th, 0.7, cc, "", S))
            for c in (1, 2):
                o.append(_rect(bx + c * seg - 2, y, 4, th, 0.6, "#1c1c1c", "", S))
        else:
            o.append(_rect(bx, y, bw, th, 0.9, fill, "", S))
        y += th

    # the ITO pixel electrode covers most of the cell; the TFT sits on the
    # glass at the right-hand end
    o.append(_rect(bx, tops[7], 168, rows[7][0], 0.9, ITO, "", S))
    o.append(_rect(bx + 168, tops[7], bw - 168, rows[7][0], 0.9, "#fdfdfd", "", S))
    o.append(_rect(bx + 172, tops[7] - 12, 52, 12, 0.8, "#dfe8f2", "", S))
    o.append(_rect(bx + 176, tops[7] - 16, 44, 4, 0.8, "#3a3a3a", "", S))
    o.append(_lbl(bx + bw + 44, tops[7] - 22, "TFT (a-Si)", "ts"))
    o.append(_line(bx + bw + 40, tops[7] - 18, bx + 204, tops[7] - 12, 0.7, S))

    # storage capacitor: the pixel electrode overlaps the gate metal
    o.append(_rect(bx + 96, tops[7] + 1, 46, rows[7][0] - 2, 0.7, "none", "3 3", GOLD))
    o.append(_lbl(bx + 119, tops[7] - 22, "C_S", "txs", "middle"))
    o.append(_line(bx + 119, tops[7] - 18, bx + 119, tops[7] - 2, 0.6, S))

    # fanned labels on the left, in ascending order so no leaders cross
    slots = [34 + i * 20 for i in range(10)]
    for (lab, mid, slot) in zip([r[2] for r in rows], mids, slots):
        o.append(_line(148, slot, bx - 4, mid, 0.7, S))
        o.append(_lbl(144, slot + 3.2, lab, "ts", "end"))

    return _fig(
        svg(660, 250, "".join(o),
            "Mặt cắt một LCD ma trận chủ động"),
        "Hình 92.14 · Mặt cắt qua một LCD ma trận chủ động, cho thấy TFT màng mỏng, điện cực "
        "điểm ảnh ITO, tụ tích trữ, hai lớp định hướng polyimide, kính lọc màu và ma trận đen. "
        "Lớp tinh thể lỏng nằm giữa hai lớp định hướng; các phin phân cực ở hai mặt ngoài.",
        "Figure 92.14 · Cross-section through an active-matrix LCD, showing the thin-film "
        "transistor, the ITO pixel electrode, the storage capacitor, the two polyimide alignment "
        "layers, the colour filter and the black matrix. The liquid crystal sits between the two "
        "alignment layers, with a polarizer on each outer face.",
        "Mặt cắt xếp lớp của một LCD ma trận chủ động với TFT, điện cực ITO và kính lọc màu",
        "A layered cross-section of an active-matrix LCD with the TFT, ITO electrode and colour "
        "filter")


# ================================================================ 92.15
def fig_92_15():
    tag = "9215"
    o = [_defs(tag)]
    x0, y0, w, h = 170, 50, 300, 230

    # buses
    o.append(_rect(x0, y0, w, 16, 0.9, "#dcdcdc", "", S))
    o.append(_rect(x0, y0 + h - 16, w, 16, 0.9, "#dcdcdc", "", S))
    o.append(_rect(x0, y0, 16, h, 0.9, "#dcdcdc", "", S))
    o.append(_rect(x0 + w - 16, y0, 16, h, 0.9, "#dcdcdc", "", S))

    # the ITO pixel electrode
    o.append(_rect(x0 + 28, y0 + 30, w - 56, h - 62, 0.9, "#eef4fb", "", BLUE))
    o.append(_lbl(x0 + w / 2.0, y0 + 118, "Điện cực ITO", "ts", "middle"))

    # the TFT at the top-left corner
    o.append(_rect(x0 + 18, y0 + 20, 30, 20, 0.9, "#fff", "", E))
    o.append(_lbl(x0 + 33, y0 + 33, "TFT", "txs", "middle"))

    # the storage capacitor: overlap of the pixel electrode with the gate bus
    o.append(_rect(x0 + 44, y0 + h - 46, w - 88, 12, 0.7, "none", "3 3", GOLD))

    o.append(_lbl(x0 + w / 2.0, 38, "Đường cổng (gate)", "ts", "middle"))
    o.append(_line(x0 + w / 2.0, 42, x0 + w / 2.0, 52, 0.7, S))
    o.append(_lbl(158, 160, "Đường dữ liệu (data)", "ts", "end"))
    o.append(_line(162, 156, 172, 156, 0.7, S))
    o.append(_r(x0 + w / 2.0, 306, [("Tụ tích trữ C", False), ("S", True)], "middle", "ts"))
    o.append(_line(x0 + w / 2.0, 296, x0 + w / 2.0, y0 + h - 40, 0.7, S))

    return _fig(
        svg(660, 330, "".join(o),
            "Bố cục một điểm ảnh TFT-LCD"),
        "Hình 92.15 · Bố cục một điểm ảnh của TFT-LCD: đường cổng chạy ngang, đường dữ liệu chạy "
        "dọc, TFT đặt ở góc, điện cực ITO phủ phần lớn ô và tụ tích trữ hình thành ở chỗ điện cực "
        "chồng lên đường cổng của hàng kế tiếp.",
        "Figure 92.15 · Layout of one TFT-LCD pixel: the gate bus runs across, the data bus runs "
        "down, the TFT sits in the corner, the ITO electrode fills most of the cell and the "
        "storage capacitor is formed where the electrode overlaps the gate bus of the next row.",
        "Sơ đồ mặt bằng một điểm ảnh với đường cổng, đường dữ liệu, TFT và điện cực ITO",
        "A plan view of one pixel with its gate bus, data bus, TFT and ITO electrode")


# ================================================================ 92.16
def fig_92_16():
    tag = "9216"
    o = [_defs(tag)]

    # ------------------------------------------------ (a) equivalent circuit
    o.append(_lbl(18, 20, "(a)", "ts"))
    o.append(_line(120, 50, 120, 190, 0.9, E))          # data line
    o.append(_lbl(120, 44, "D", "txs", "middle"))
    o.append(_line(80, 60, 260, 60, 0.9, E))            # gate line
    o.append(_lbl(84, 54, "G", "txs"))

    o.append(_rect(132, 66, 34, 22, 0.9, "#fff", "", E))
    o.append(_lbl(149, 80, "TFT", "txs", "middle"))
    o.append(_line(149, 60, 149, 66, 0.9, E))
    o.append(_line(120, 77, 132, 77, 0.9, E))
    o.append(_line(166, 77, 196, 77, 0.9, E))
    o.append(_dot(196, 77, 2.4, E))
    o.append(_r(202, 74, [("V", False), ("p", True)], "start", "ts"))

    # C_LC to the common rail
    o.append(_line(196, 77, 196, 146, 0.9, E))
    o.append(_cap_h(196, 150))
    o.append(_line(196, 153, 196, 166, 0.9, E))
    o.append(_r(208, 150, [("C", False), ("LC", True)], "start", "ts"))
    # C_S to the common rail
    o.append(_line(196, 77, 236, 77, 0.9, E))
    o.append(_cap_v(240, 77))
    o.append(_line(243, 77, 252, 77, 0.9, E))
    o.append(_line(252, 77, 252, 166, 0.9, E))
    o.append(_r(256, 72, [("C", False), ("S", True)], "start", "ts"))
    o.append(_line(170, 166, 280, 166, 0.9, E))
    o.append(_r(286, 169, [("V", False), ("com", True)], "start", "ts"))

    # ------------------------------------------------ (b) gate waveform
    o.append(_lbl(330, 20, "(b)", "ts"))
    G = Frame(360, 48, 260, 108, (0, 4), (0, 10))
    o.append(G.frame())
    o.append(G.xticks([(0, "0"), (1, "1"), (2, "2"), (3, "3"), (4, "4")]))
    o.append(G.yticks([(1, ""), (9, "")]))
    o.append(G.xlab("thời gian (chu kỳ hàng)", 26))
    o.append(G.ylab("V_g", -34))
    pts = [(0, 1), (1, 1), (1, 9), (1.2, 9), (1.2, 1), (4, 1)]
    o.append(G.curve(pts, 1.6, E))
    o.append(_lbl(G.X(1.1), G.Y(9) - 5, "V_g,sel", "txs", "middle"))
    o.append(_lbl(G.X(2.6), G.Y(1) - 6, "V_g,non-sel", "txs", "middle"))

    # ------------------------------------------------ (c) data and pixel
    o.append(_lbl(80, 236, "(c)", "ts"))
    C = Frame(110, 258, 480, 150, (0, 4), (-6, 6))
    o.append(C.frame())
    o.append(C.xticks([(0, "0"), (1, "1"), (2, "2"), (3, "3"), (4, "4")]))
    o.append(C.yticks([(-4, "−V_d"), (0, "0"), (4, "+V_d")]))
    o.append(C.xlab("thời gian", 28))
    o.append(C.ylab("điện áp", -40))

    # data voltage: a square wave at +Vd and -Vd
    dp = [(0, 4), (2, 4), (2, -4), (4, -4)]
    o.append(C.curve(dp, 1.3, BLUE, "5 4"))
    # pixel voltage: charge to Vd, drop by dVp, hold; then the negative frame
    vp = [(0, 0), (0.18, 0), (0.30, 4.0), (0.30, 3.2), (2.0, 3.2),
          (2.18, 3.2), (2.30, -4.0), (2.30, -4.8), (4.0, -4.8)]
    o.append(C.curve(vp, 1.7, E))
    o.append(_r(C.X(0.55), C.Y(4.7), [("V", False), ("d", True)], "start", "ts"))
    o.append(_r(C.X(0.55), C.Y(2.6), [("V", False), ("p", True)], "start", "ts"))
    # the shift, marked at the end of the row time
    o.append(_line(C.X(0.30), C.Y(4.0), C.X(0.30), C.Y(3.2), 1.2, RED))
    o.append(_r(C.X(0.36), C.Y(3.5), [("ΔV", False), ("p", True)], "start", "txs"))

    return _fig(
        svg(660, 430, "".join(o),
            "Mạch tương đương và dạng sóng của một điểm ảnh TFT-LCD"),
        "Hình 92.16 · (a) Mạch tương đương của một điểm ảnh TFT-LCD: TFT nối đường dữ liệu với "
        "nút điểm ảnh, nơi có điện dung lớp tinh thể lỏng C<sub>LC</sub> và tụ tích trữ "
        "C<sub>S</sub> nối xuống điện cực chung. (b) Xung cổng: một xung chọn V<sub>g,sel</sub> "
        "trong thời gian một hàng, phần còn lại của khung ở mức không chọn. (c) Điện áp dữ liệu "
        "±V<sub>d</sub> và điện áp điểm ảnh: nạp tới V<sub>d</sub> trong thời gian hàng rồi tụt "
        "một lượng ΔV<sub>p</sub> khi cổng tắt, và đảo dấu ở khung kế tiếp.",
        "Figure 92.16 · (a) Equivalent circuit of a TFT-LCD pixel: the TFT connects the data line "
        "to the pixel node, which carries the liquid-crystal capacitance C<sub>LC</sub> and the "
        "storage capacitor C<sub>S</sub> to the common electrode. (b) Gate waveform: one select "
        "pulse V<sub>g,sel</sub> per row time, with the rest of the frame at the non-select "
        "level. (c) Data voltage ±V<sub>d</sub> and pixel voltage: the pixel charges to "
        "V<sub>d</sub> during the row time, drops by ΔV<sub>p</sub> when the gate switches off, "
        "and reverses sign in the next frame.",
        "Mạch tương đương một điểm ảnh TFT-LCD, xung cổng và dạng sóng điện áp dữ liệu, điện áp "
        "điểm ảnh",
        "The equivalent circuit of a TFT-LCD pixel, the gate pulse, and the data and pixel "
        "voltage waveforms")
