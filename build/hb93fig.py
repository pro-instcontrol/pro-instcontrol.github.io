# -*- coding: utf-8 -*-
"""Figures 93.1–93.10 for Handbook Chapter 93 — Plasma-Driven Flat Panel Displays.

Helpers live in `hb93base.py`; figures 93.11–93.20 are in `hb93figb.py`.

Figures 93.3 and 93.4 are photographs in the source. They are redrawn here as
line art of the same assemblies, following the convention set for Chapters 27
and 28: the subject is drawn, the screen content is not invented.
"""
import math

from hbfig import svg, _fig
from hb93base import (E, S, GRID, GOLD, BLUE, TEAL, RED, GREEN, GLASS, DIELE, METAL,
                      _defs, _lbl, _r, _line, _arr, _rect, _poly, _path, _dot, _circ,
                      _hatch, _slab, _isostrip, _isostrip_d, Frame)


# ================================================================ 93.1
def fig_93_1():
    tag = "931"
    o = [_defs(tag)]
    bx, bw, dx, dy = 176, 286, 44, 24
    y1, y2, y3 = 108, 188, 262

    o.append(_slab(bx, y3, bw, 146, 10, dx, dy))
    for i in range(5):
        o.append(_isostrip_d(bx + 24 + i * 55, y3, 7, 0.92, dx, dy))

    o.append(_slab(bx, y2, bw, 146, 8, dx, dy, DIELE))
    for i in range(5):
        for j in range(3):
            d0 = 0.22 + j * 0.3
            hx = bx + 30 + i * 55 + dx * d0
            hy = y2 - dy * d0
            o.append(_poly([(hx, hy), (hx + 17, hy), (hx + 17 + dx * 0.2, hy - dy * 0.2),
                            (hx + dx * 0.2, hy - dy * 0.2)], 0.9, "#ffffff", S, "2 2"))

    o.append(_slab(bx, y1, bw, 146, 8, dx, dy, "#fbfbfb"))
    for d0 in (0.2, 0.44, 0.68, 0.92):
        o.append(_isostrip(bx + 8, y1, bw - 16, d0, 0.11, dx, dy, "#e9eef5", "#8fa6bf"))

    o.append(_line(bx + dx * 0.44 + bw * 0.55, y1 - dy * 0.44, 534, 44, 0.8, S))
    o.append(_lbl(538, 38, "Transparent", "tb"))
    o.append(_lbl(538, 49, "electrodes", "tb"))

    o.append(_line(bx + 30, y1 + 3, 104, 88, 0.8, S))
    o.append(_lbl(100, 80, "Front glass plate", "tb", "end"))

    o.append(_line(bx + dx * 0.52 + 30, y2 - dy * 0.52, 104, 168, 0.8, S))
    o.append(_lbl(100, 156, "Perforated glass", "tb", "end"))
    o.append(_lbl(100, 167, "dielectric", "tb", "end"))

    o.append(_line(bx + 40, y2 + 6, 104, 216, 0.8, S))
    o.append(_lbl(100, 208, "Glass dielectric", "tb", "end"))

    o.append(_line(bx + bw + dx * 0.62, y2 + 6 - dy * 0.62, 534, 196, 0.8, S))
    o.append(_lbl(538, 190, "Gas cavity", "tb"))
    o.append(_lbl(bx + bw - 8, y3 + 24, "Rear glass", "txs", "end"))
    return _fig(
        svg(660, 300, "".join(o),
            "Cấu trúc tấm hiển thị plasma xoay chiều phát minh tại Đại học Illinois"),
        "Hình 93.1 · Cấu trúc tấm hiển thị plasma xoay chiều do Bitzer và Slottow phát minh tại "
        "Đại học Illinois năm 1966: hai tấm thuỷ tinh mang các dây dẫn song song đặt vuông góc "
        "với nhau, ngăn cách bằng một lớp điện môi thuỷ tinh đục lỗ, khoang khí trơ ở giữa.",
        "Figure 93.1 · Structure of the ac plasma display invented at the University of Illinois: "
        "two glass plates carrying parallel conductor wires at right angles, separated by a "
        "perforated glass dielectric spacer, with the inert gas in the cavity between them.",
        "Sơ đồ ba lớp của tấm hiển thị plasma: tấm trước có điện cực trong suốt, lớp điện môi đục "
        "lỗ, tấm sau có điện cực ngang và khoang khí ở giữa",
        "Three-layer diagram of the plasma panel: front plate with transparent electrodes, "
        "perforated dielectric spacer, rear plate with horizontal electrodes, gas cavity between")


# ================================================================ 93.2
def fig_93_2():
    tag = "932"
    o = [_defs(tag)]
    cols, rows = 12, 6
    x0, y0, sx, sy = 128, 70, 28, 24
    x1 = x0 + (cols - 1) * sx
    y1 = y0 + (rows - 1) * sy

    for c in range(cols):
        cx = x0 + c * sx
        o.append(_line(cx, y0 - 8, cx, 48, 1.0, S))
        o.append(_line(cx, 48, 446, 48, 1.0, S))
    for r in range(rows):
        ry = y0 + r * sy
        o.append(_line(x0 - 8, ry, 100, ry, 1.0, S))
        o.append(_line(100, ry, 100, 252, 1.0, S))

    for r in range(rows):
        for c in range(cols):
            o.append(_circ(x0 + c * sx, y0 + r * sy, 7.2, E, "#fff", 1.1))

    o.append(_rect(450, 22, 132, 46, 1.2, "#fff"))
    o.append(_lbl(516, 38, "Data switches", "tb", "middle"))
    o.append(_lbl(516, 50, "one per column", "txs", "middle"))
    o.append(_line(446, 48, 450, 48, 1.2))
    for i in range(3):
        gx = 468 + i * 34
        o.append(_line(gx, 58, gx + 9, 52, 1.0, S))
        o.append(_dot(gx, 60, 1.6))
        o.append(_dot(gx + 9, 60, 1.6))

    o.append(_rect(44, 262, 152, 46, 1.2, "#fff"))
    o.append(_lbl(120, 278, "Scan switches", "tb", "middle"))
    o.append(_lbl(120, 292, "close one at a time", "txs", "middle"))
    for i in range(3):
        gx = 60 + i * 40
        o.append(_line(gx, 252, gx + 10, 262, 1.0, S))
        o.append(_dot(gx, 252, 1.6))
        o.append(_dot(gx + 10, 252, 1.6))

    o.append(_lbl(x0, y1 + 34, "Pixels at the intersections of one row wire and one column wire",
                  "txs"))
    return _fig(
        svg(660, 326, "".join(o),
            "Màn hiển thị plasma ma trận điểm với các chuyển mạch quét và chuyển mạch dữ liệu"),
        "Hình 93.2 · Màn hiển thị plasma ma trận điểm đơn giản với các chuyển mạch quét dữ liệu: "
        "chuyển mạch quét đóng lần lượt từng hàng, chuyển mạch dữ liệu quyết định điểm ảnh trên "
        "hàng đó có phát sáng hay không.",
        "Figure 93.2 · A simple dot matrix plasma display and data scanning switches: the scan "
        "switches close one row at a time while the data switches decide which pixels on that row "
        "fire.",
        "Lưới điểm ảnh plasma với các dây hàng nối tới chuyển mạch quét ở dưới bên trái và các dây "
        "cột nối tới chuyển mạch dữ liệu ở trên bên phải",
        "Matrix of plasma pixels with row wires going to the scan switches at lower left and "
        "column wires going to the data switches at upper right")


# ================================================================ 93.3
def fig_93_3():
    tag = "933"
    o = [_defs(tag)]
    o.append(_rect(168, 34, 324, 214, 1.6, "#ffffff"))
    o.append(_rect(184, 50, 292, 170, 1.2, "#fafafa"))
    o.append(_rect(192, 58, 276, 154, 1.0, "#fdfdfd"))
    o.append(_lbl(200, 74, "40 Plasma Display", "tb"))
    o.append(_poly([(192, 212), (192, 150), (250, 126), (330, 140), (420, 120), (468, 132),
                    (468, 212)], 0.9, "#efefef", "#dcdcdc"))
    o.append(_line(192, 186, 468, 186, 0.8, "#dcdcdc"))
    o.append(_lbl(330, 202, "ảnh hiển thị — lược bỏ", "tcap", "middle"))
    o.append(_poly([(286, 248), (374, 248), (388, 266), (272, 266)], 1.4, "#f4f4f4"))
    o.append(_rect(240, 266, 180, 8, 1.2, "#eeeeee"))
    return _fig(
        svg(660, 300, "".join(o),
            "Màn hiển thị plasma một chiều 40 inch của NHK"),
        "Hình 93.3 · Màn hiển thị plasma 102 cm (40 in.) điều khiển một chiều của NHK. Bản gốc là "
        "ảnh chụp; ở đây dựng lại bằng nét vẽ, phần nội dung ảnh trên màn hình được lược bỏ.",
        "Figure 93.3 · The 40-in. diagonal dc-driven plasma display from NHK. The original is a "
        "photograph; it is redrawn here as line art with the screen content omitted.",
        "Màn hiển thị plasma cỡ lớn đặt trên đế, khung viền dày, màn hình phẳng",
        "Large plasma display on a stand with a thick bezel and a flat screen")


# ================================================================ 93.4
def fig_93_4():
    tag = "934"
    o = [_defs(tag)]
    o.append(_rect(172, 26, 316, 206, 1.6, "#ffffff"))
    o.append(_rect(188, 40, 284, 164, 1.2, "#fafafa"))
    o.append(_rect(196, 48, 268, 148, 1.0, "#fdfdfd"))
    o.append(_poly([(196, 196), (196, 138), (262, 116), (338, 130), (420, 112), (464, 124),
                    (464, 196)], 0.9, "#efefef", "#dcdcdc"))
    o.append(_lbl(330, 186, "ảnh hiển thị — lược bỏ", "tcap", "middle"))
    o.append(_poly([(292, 232), (368, 232), (380, 248), (280, 248)], 1.4, "#f4f4f4"))
    o.append(_rect(252, 248, 156, 7, 1.2, "#eeeeee"))
    o.append(_poly([(126, 268), (398, 268), (416, 292), (108, 292)], 1.4, "#fbfbfb"))
    for r in range(3):
        for c in range(13):
            o.append(_rect(124 + c * 21 - r * 4, 273 + r * 7, 15, 5, 0.6, "#ffffff", "", S))
    return _fig(
        svg(660, 310, "".join(o),
            "Màn hiển thị plasma xoay chiều 30 inch của Photonics Imaging cùng bàn phím"),
        "Hình 93.4 · Màn hiển thị plasma 76 cm (30 in.) điều khiển xoay chiều của Photonics "
        "Imaging, đặt cùng bàn phím. Bản gốc là ảnh chụp; ở đây dựng lại bằng nét vẽ, phần nội "
        "dung ảnh trên màn hình được lược bỏ.",
        "Figure 93.4 · The 30-in. diagonal ac-driven plasma display from Photonics Imaging, shown "
        "with its keyboard. The original is a photograph; it is redrawn here as line art with the "
        "screen content omitted.",
        "Màn hình plasma kiểu màn hình máy tính đặt trên đế, phía trước là bàn phím rời",
        "Computer-style plasma monitor on a stand with a separate keyboard in front of it")


# ================================================================ 93.5
def fig_93_5():
    tag = "935"
    o = [_defs(tag)]

    def panel(top, ac):
        p = []
        gl, gh = top, 16
        gap = 12 if ac else 6
        p.append(_rect(150, gl, 370, gh, 1.2, GLASS))
        p.append(_lbl(516, gl - 5, "Front glass", "txs", "end"))
        for x in (176, 306, 436):
            p.append(_rect(x, gl + gh, 66, 6, 1.0, METAL, "", S))
            if ac:
                p.append(_rect(x - 5, gl + gh - 4, 76, 14, 0.8, "#dcdcdc", "", "#aaa"))
                p.append(_line(x - 5, gl + gh + 11, x + 71, gl + gh + 11, 1.6, "#6f6f6f"))
        p.append(_rect(150, gl + gh + gap, 370, 118 - gh - gap, 0.9, "#ffffff", "5 4", S))
        p.append(_lbl(335, gl + 50, "Working gas options:", "txs", "middle"))
        p.append(_lbl(335, gl + 62, "a) Ne + 0.1% Ar, 3×10⁴ Pa (~400 Torr)", "txs", "middle"))
        p.append(_lbl(335, gl + 74, "b) He + 2% Xe, 3×10⁴ Pa (~400 Torr)", "txs", "middle"))
        p.append(_rect(150, gl + 118, 370, gh, 1.2, GLASS))
        p.append(_lbl(516, gl + 118 + gh + 13, "Rear glass", "txs", "end"))
        p.append(_rect(158, gl + 112, 356, 6, 1.0, METAL, "", S))
        if ac:
            p.append(_rect(153, gl + 108, 366, 14, 0.8, "#dcdcdc", "", "#aaa"))
            p.append(_line(153, gl + 108, 519, gl + 108, 1.6, "#6f6f6f"))
        p.append(_line(168, gl + gh + 3, 122, gl + gh - 8, 0.8, S))
        p.append(_lbl(118, gl + gh - 12, "Vertical", "tb", "end"))
        p.append(_lbl(118, gl + gh - 1, "conductor", "tb", "end"))
        p.append(_line(160, gl + 115, 122, gl + 106, 0.8, S))
        p.append(_lbl(118, gl + 100, "Horizontal", "tb", "end"))
        p.append(_lbl(118, gl + 111, "conductor", "tb", "end"))
        if ac:
            p.append(_line(178, gl + gh + 11, 126, gl + gh + 20, 0.8, S))
            p.append(_lbl(122, gl + gh + 24, "MgO film", "tb", "end"))
            p.append(_line(540, gl + gh + 2, 522, gl + gh - 2, 0.8, S))
            p.append(_lbl(544, gl + gh - 4, "PbO", "tb"))
            p.append(_lbl(544, gl + gh + 7, "dielectric", "tb"))
            p.append(_line(540, gl + 104, 522, gl + 100, 0.8, S))
            p.append(_lbl(544, gl + 96, "MgO film", "tb"))
        return "".join(p)

    o.append(panel(24, False))
    o.append(_lbl(150, 180, "(a) dc pixel", "tb"))
    o.append(panel(198, True))
    o.append(_lbl(150, 356, "(b) ac pixel", "tb"))
    return _fig(
        svg(660, 380, "".join(o),
            "Mặt cắt điểm ảnh plasma điện cực đối diện kiểu một chiều và xoay chiều"),
        "Hình 93.5 · Sơ đồ mặt cắt điểm ảnh plasma điện cực đối diện: (a) kiểu một chiều, khí làm "
        "việc tiếp xúc trực tiếp với điện cực; (b) kiểu xoay chiều, điện cực được phủ lớp điện môi "
        "PbO dày ~25 µm và màng MgO mỏng 50–200 nm. Hình gốc in “3 Pa (~400 Torr)”; 400 Torr thực "
        "tế là 53,3 kPa nên ở đây ghi 3×10⁴ Pa.",
        "Figure 93.5 · Schematic cross-sections of opposed-electrode plasma pixels: (a) dc, with "
        "the working gas in direct contact with the electrodes; (b) ac, with the electrodes covered "
        "by a ~25 µm PbO dielectric and a 50–200 nm MgO film. The original prints “3 Pa (~400 "
        "Torr)”; 400 Torr is 53.3 kPa, so 3×10⁴ Pa is shown here.",
        "Hai mặt cắt xếp trên dưới: điểm ảnh một chiều có điện cực trần, điểm ảnh xoay chiều có "
        "thêm lớp điện môi PbO và màng MgO phủ điện cực",
        "Two stacked cross-sections: a dc pixel with bare electrodes and an ac pixel with PbO "
        "dielectric and MgO films over the electrodes")


# ================================================================ 93.6
def fig_93_6():
    tag = "936"
    o = [_defs(tag)]
    bx, bw, dx, dy = 178, 262, 40, 22
    yr, h = 248, 26

    # ---- rear plate + address electrodes (running across, at three depths)
    o.append(_slab(bx, yr, bw, 138, 9, dx, dy))
    for d0 in (0.2, 0.48, 0.76):
        o.append(_isostrip(bx, yr, bw, d0, 0.05, dx, dy))

    # ---- barrier ribs: narrow walls running into the page, phosphor on the face
    cols = [RED, GREEN, BLUE]
    for i in range(7):
        x = bx + 14 + i * 36
        o.append(_rect(x, yr - h, 7, h, 0.9, cols[i % 3]))
        o.append(_poly([(x, yr - h), (x + 7, yr - h), (x + 7 + dx, yr - h - dy),
                        (x + dx, yr - h - dy)], 0.9, "#f4f4f4"))

    # ---- front assembly: glass, dielectric, MgO
    o.append(_slab(bx, 140, bw, 138, 8, dx, dy, "#fbfbfb"))
    for d0 in (0.2, 0.44, 0.68, 0.92):
        o.append(_isostrip(bx + 8, 140, bw - 16, d0, 0.11, dx, dy, "#e9eef5", "#8fa6bf"))
    o.append(_isostrip_d(bx + bw - 24, 140, 7, 0.92, dx, dy))
    o.append(_slab(bx, 158, bw, 138, 4, dx, dy, DIELE))
    o.append(_slab(bx, 170, bw, 138, 2, dx, dy, "#c9c9c9"))

    # ---- leaders
    o.append(_line(bx + 60 + dx * 0.3, 140 - dy * 0.3, 120, 40, 0.8, S))
    o.append(_lbl(116, 34, "Transparent display", "tb", "end"))
    o.append(_lbl(116, 45, "electrodes", "tb", "end"))
    o.append(_line(bx + bw + dx * 0.4, 140 - dy * 0.4, 508, 24, 0.8, S))
    o.append(_lbl(512, 22, "Front glass plate", "tb"))
    o.append(_line(bx + bw + 12, 146, 508, 48, 0.8, S))
    o.append(_lbl(512, 46, "Bus electrodes", "tb"))
    o.append(_line(bx + 6, 160, 148, 96, 0.8, S))
    o.append(_lbl(144, 92, "Dielectric layer", "tb", "end"))
    o.append(_line(bx + 6, 172, 148, 118, 0.8, S))
    o.append(_lbl(144, 114, "MgO layer", "tb", "end"))
    o.append(_line(bx + bw + 14, yr - 20, 508, 186, 0.8, S))
    o.append(_lbl(512, 184, "Barrier ribs", "tb"))
    o.append(_line(bx + bw + 10, yr + 4, 508, 246, 0.8, S))
    o.append(_lbl(512, 244, "Rear glass plate", "tb"))
    o.append(_line(bx + 70, yr + 5, 120, 266, 0.8, S))
    o.append(_lbl(116, 262, "Address electrodes", "tb", "end"))
    o.append(_line(bx + 14 + 36 + 3, yr - 14, 120, 296, 0.8, S))
    o.append(_lbl(116, 292, "Phosphors R, G, B", "tb", "end"))
    return _fig(
        svg(660, 306, "".join(o),
            "Cấu trúc màn hiển thị plasma màu xoay chiều của Fujitsu"),
        "Hình 93.6 · Cấu trúc màn hiển thị plasma màu xoay chiều của Fujitsu: ba điện cực kiểu "
        "phóng điện bề mặt, vách ngăn cao 100–150 µm phủ phosphor đỏ, lục, lam.",
        "Figure 93.6 · Structure of the ac colour plasma display manufactured by Fujitsu: a "
        "three-electrode surface-discharge design, with 100–150 µm barrier ribs carrying red, "
        "green and blue phosphors.",
        "Sơ đồ lớp của màn hình plasma màu: tấm trước có điện cực trong suốt và điện cực bus, lớp "
        "điện môi và MgO, các vách ngăn phủ phosphor đỏ lục lam, tấm sau có điện cực địa chỉ",
        "Layer diagram of the colour plasma panel: front plate with transparent and bus electrodes, "
        "dielectric and MgO layers, phosphor-coated barrier ribs, and a rear plate with address "
        "electrodes")


# ================================================================ 93.7
def fig_93_7():
    tag = "937"
    o = [_defs(tag)]
    o.append(_lbl(330, 16, "GAS DISCHARGE REACTIONS", "tb", "middle"))

    # ---- the cell
    o.append(_rect(40, 44, 26, 190, 1.1, "#e8e8e8"))
    o.append(_hatch(tag, 40, 44, 26, 190, 7, "#bcbcbc"))
    o.append(_rect(40, 44, 26, 190, 1.1, "none"))
    o.append(_rect(452, 44, 26, 190, 1.1, "#e8e8e8"))
    o.append(_hatch(tag + "b", 452, 44, 26, 190, 7, "#bcbcbc"))
    o.append(_rect(452, 44, 26, 190, 1.1, "none"))
    o.append(_lbl(53, 34, "CATHODE", "tb", "middle"))
    o.append(_lbl(465, 34, "ANODE", "tb", "middle"))

    o.append(_rect(66, 52, 386, 176, 0.9, "#ffffff", "4 4", S))
    o.append(_lbl(258, 68, "AVALANCHE", "tb", "middle"))
    o.append(_line(214, 74, 302, 74, 0.8, S))

    for y in (110, 152, 194):
        o.append(_arr(150, y, 218, y, tag, 1.0, E, "h"))
        o.append(_arr(214, y + 16, 156, y + 16, tag, 1.0, S, "h"))
    o.append(_lbl(182, 102, "electron", "txs", "middle"))
    o.append(_lbl(182, 180, "ion", "txs", "middle"))

    for (cx, cy) in ((248, 96), (300, 118), (256, 160), (316, 178)):
        o.append(_circ(cx, cy, 4.2, E, "#fff"))
        o.append(_line(cx - 14, cy, cx - 5, cy, 0.9, S))
        o.append(_arr(cx + 5, cy, cx + 14, cy - 8, tag, 0.9, E, "h"))
        o.append(_arr(cx + 5, cy, cx + 14, cy + 8, tag, 0.9, E, "h"))

    # photons
    for (x1, y1, x2, y2) in ((104, 224, 158, 206), (330, 216, 300, 200)):
        o.append(_path([(x1, y1), (x1 + 9, y1 - 5), (x1 + 18, y1), (x1 + 27, y1 - 5),
                        (x2, y2)], 1.0, GOLD))
        o.append(_arr(x2 - 12, y2 + 3, x2, y2, tag, 1.0, GOLD, "h"))

    o.append(_arr(70, 122, 112, 112, tag, 1.2, E, "h"))
    o.append(_lbl(70, 134, "ejection by ion", "txs"))
    o.append(_lbl(70, 238, "ejection by photon", "txs"))

    # ---- insets
    def inset(x, y, w, h, title):
        return _rect(x, y, w, h, 1.1, "#fff") + _lbl(x + w / 2.0, y + 14, title, "tb", "middle")

    # (M) metastable generation
    x, y = 492, 44
    o.append(inset(x, y, 152, 86, "(M)  metastable generation"))
    o.append(_poly([(x + 34, y + 26), (x + 68, y + 26), (x + 84, y + 54), (x + 68, y + 80),
                    (x + 34, y + 80), (x + 18, y + 54)], 1.0, "#fff"))
    o.append(_circ(x + 30, y + 54, 3.6, E, "#fff"))
    o.append(_circ(x + 64, y + 54, 3.6, E, "#fff"))
    o.append(_arr(x + 35, y + 54, x + 59, y + 54, tag, 1.0, E, "h"))
    o.append(_arr(x + 60, y + 58, x + 46, y + 70, tag, 1.0, S, "h"))
    o.append(_lbl(x + 30, y + 46, "Ne", "txs", "middle"))
    o.append(_lbl(x + 70, y + 46, "Ne", "txs", "middle"))
    o.append(_lbl(x + 48, y + 78, "Ne*", "txs", "middle"))

    # (I) ionisation
    x, y = 492, 138
    o.append(inset(x, y, 152, 74, "(I)  ionization"))
    o.append(_circ(x + 34, y + 44, 3.6, E, "#fff"))
    o.append(_arr(x + 39, y + 44, x + 58, y + 44, tag, 1.0, E, "h"))
    o.append(_circ(x + 64, y + 32, 3.6, E, "#fff"))
    o.append(_circ(x + 64, y + 56, 3.6, E, "#fff"))
    o.append(_lbl(x + 30, y + 36, "Ne", "txs", "middle"))
    o.append(_lbl(x + 90, y + 30, "Ne⁺", "txs", "middle"))
    o.append(_lbl(x + 90, y + 58, "e", "txs", "middle"))

    # (E) excitation
    x, y = 492, 220
    o.append(inset(x, y, 152, 74, "(E)  excitation"))
    o.append(_circ(x + 34, y + 44, 3.6, E, "#fff"))
    o.append(_arr(x + 39, y + 44, x + 58, y + 44, tag, 1.0, E, "h"))
    o.append(_circ(x + 66, y + 44, 3.6, E, "#fff"))
    o.append(_path([(x + 74, y + 34), (x + 82, y + 30), (x + 90, y + 34), (x + 98, y + 30)],
                   1.0, GOLD))
    o.append(_lbl(x + 30, y + 36, "Ne", "txs", "middle"))
    o.append(_lbl(x + 96, y + 62, "Ne*", "txs"))

    # (P) Penning ionisation
    o.append(_rect(300, 240, 150, 96, 1.1, "#fff"))
    o.append(_lbl(375, 254, "(P)  Penning ionisation", "tb", "middle"))
    o.append(_poly([(374, 264), (414, 288), (374, 312), (334, 288)], 1.0, "#fff"))
    o.append(_lbl(374, 280, "Ne*", "txs", "middle"))
    o.append(_arr(374, 284, 374, 300, tag, 1.0, E, "h"))
    o.append(_lbl(386, 296, "Ar", "txs"))
    o.append(_lbl(374, 324, "Ar⁺ + e", "txs", "middle"))

    # ---- legend, two columns
    leg = [("●", "electron", "drift right"), ("Ne", "neutral atom", "diffuse"),
           ("Ne⁺", "positive ion", "drift left"), ("Ar", "neutral atom", "diffuse"),
           ("Ar⁺", "positive ion", "drift left"), ("Ne*", "excited atom", "diffuse"),
           ("Ne*", "metastable atom", "diffuse"), ("∿", "photon", "propagate")]
    o.append(_rect(40, 240, 250, 96, 1.0, "#fff"))
    for i, (sym, name, act) in enumerate(leg):
        cx = 52 + (i % 2) * 122
        cy = 256 + (i // 2) * 22
        o.append(_lbl(cx, cy, sym, "txs"))
        o.append(_lbl(cx + 16, cy, name, "txs"))
        o.append(_lbl(cx + 16, cy + 9, act, "txs"))
    return _fig(
        svg(660, 348, "".join(o),
            "Sơ đồ tương tác va chạm và bề mặt trong phóng điện khí"),
        "Hình 93.7 · Các tương tác va chạm và bề mặt trong một phóng điện khí: điện cực âm bên "
        "trái, cực dương bên phải, thác điện tử ở giữa, kèm bốn ô phụ (M) sinh trạng thái "
        "metastable, (I) ion hoá, (E) kích thích và (P) ion hoá Penning.",
        "Figure 93.7 · Collisional and surface interactions in a gas discharge: cathode at the "
        "left, anode at the right, the avalanche between them, with four inset panels — (M) "
        "metastable generation, (I) ionisation, (E) excitation and (P) Penning ionisation.",
        "Sơ đồ phóng điện khí với cực âm, cực dương, vùng thác điện tử, các va chạm ion hoá và "
        "bốn ô phụ giải thích cơ chế metastable, ion hoá, kích thích và Penning",
        "Gas discharge diagram with cathode, anode, avalanche region, ionising collisions and four "
        "inset panels for metastable, ionisation, excitation and Penning processes")


# ================================================================ 93.8
def fig_93_8():
    tag = "938"
    o = [_defs(tag)]
    top, bot = 44, 292
    F = Frame(96, top, 34, bot - top, (0, 1), (0, 25))

    o.append(_line(96, bot, 96, top, 1.2))
    for v in (0, 5, 10, 15, 20, 25):
        o.append(_line(90, F.Y(v), 96, F.Y(v), 1.1))
        o.append(_lbl(86, F.Y(v) + 3.2, str(v), "ts", "end"))
    o.append(_lbl(96, bot + 18, "Năng lượng (eV)", "ts", "middle"))

    o.append(_line(600, bot, 600, top, 1.2))
    for v in (0, 5, 10, 15, 20, 25):
        o.append(_line(600, F.Y(v), 606, F.Y(v), 1.1))
        o.append(_lbl(610, F.Y(v) + 3.2, str(int(round(v * 8.066))), "ts"))
    o.append('<text class="ts" x="646" y="%s" text-anchor="middle" transform="rotate(-90 646 %s)">'
             'Energy (10³ cm⁻¹)</text>' % (F.Y(12.5), F.Y(12.5)))

    cols = [
        (108, 86, "Neon", [(16.62, 16.67, 16.72, 16.85), (18.38, 18.55, 18.70, 18.97)], 21.56,
         [(16.85, "74,4 nm", -13), (16.62, "73,6 nm", 13)]),
        (204, 86, "Argon", [(11.55, 11.62, 11.72, 11.83), (12.91, 13.02, 13.15, 13.33)], 15.76, []),
        (300, 86, "Helium", [(19.82, 20.62, 20.96, 21.22)], 24.59, []),
        (396, 86, "Xenon", [(8.32, 8.44, 9.45, 9.57), (9.73, 9.79, 9.93, 10.09, 10.97)], 12.13,
         [(9.57, "129 nm", -13), (8.44, "147 nm", 13)]),
    ]
    for x, w, name, groups, ion, arrows in cols:
        o.append(_rect(x, top, w, bot - top, 1.0, "#fdfdfd"))
        o.append(_lbl(x + w / 2.0, top - 6, name, "tb", "middle"))
        for g in groups:
            for v in g:
                o.append(_line(x + 6, F.Y(v), x + w - 6, F.Y(v), 1.0, E))
        o.append(_line(x + 6, F.Y(ion), x + w - 6, F.Y(ion), 1.8, "#7a7a7a"))
        o.append(_lbl(x + w - 8, F.Y(ion) + 15, "ion", "txs", "end"))
        for v, lab, off in arrows:
            ax = x + w / 2.0 + off
            o.append(_arr(ax, F.Y(v) - 2, ax, F.Y(0) + 8, tag, 1.0, E, "h"))
            o.append('<text class="txs" x="%s" y="%s" text-anchor="middle" '
                     'transform="rotate(-90 %s %s)">%s</text>'
                     % (ax + (4 if off < 0 else -4), F.Y(v / 2.0), ax + (4 if off < 0 else -4),
                        F.Y(v / 2.0), lab))

    # xenon dimer: a broad band rather than sharp levels
    x, w = 492, 86
    o.append(_rect(x, top, w, bot - top, 1.0, "#fdfdfd"))
    o.append(_lbl(x + w / 2.0, top - 6, "Xenon dimer", "tb", "middle"))
    o.append(_poly([(x + 6, F.Y(8.3)), (x + w - 6, F.Y(8.3)), (x + w - 6, F.Y(6.4)),
                    (x + 6, F.Y(6.4))], 1.0, "#ededed", S, "3 3"))
    o.append(_lbl(x + w / 2.0, F.Y(7.3) + 3, "Xe₂*", "tm", "middle"))
    for v, lab, ax in ((7.17, "173 nm", x + 24), (8.27, "150 nm", x + 62)):
        o.append(_arr(ax, F.Y(6.45), ax, F.Y(0) + 8, tag, 1.0, E, "h"))
        o.append('<text class="txs" x="%s" y="%s" text-anchor="middle" transform="rotate(-90 %s %s)">'
                 '%s</text>' % (ax - 4, F.Y(3.2), ax - 4, F.Y(3.2), lab))

    o.append(_rect(10, 56, 78, 92, 1.0, "#fff"))
    o.append(_lbl(14, 72, "Ne 2p → 1s:", "txs"))
    o.append(_lbl(14, 84, "vạch nhìn thấy", "txs"))
    o.append(_lbl(14, 96, "585,2–640,2 nm", "txs"))
    o.append(_line(88, 100, 108, 92, 0.8, S))

    o.append(_lbl(96, 330, "Mức năng lượng của các khí trơ; mũi tên chỉ bước sóng phát xạ VUV",
                  "txs"))
    return _fig(
        svg(660, 342, "".join(o),
            "Giản đồ mức năng lượng lượng tử của He, Ne, Ar, Xe và dimer Xe2"),
        "Hình 93.8 · Giản đồ mức năng lượng rút gọn của He, Ne, Ar, Xe và dimer Xe₂*: vạch đậm là "
        "mức ion hoá, mũi tên chỉ các bước sóng phát xạ tử ngoại chân không (74,4 và 73,6 nm của "
        "Ne; 129 và 147 nm của Xe; 150 và 173 nm của Xe₂*).",
        "Figure 93.8 · Simplified quantum energy level diagrams for He, Ne, Ar, Xe and the Xe₂* "
        "dimer: the heavy line is the ionisation level, and the arrows mark the vacuum-ultraviolet "
        "emission wavelengths (74.4 and 73.6 nm for Ne; 129 and 147 nm for Xe; 150 and 173 nm for "
        "Xe₂*).",
        "Năm cột mức năng lượng của neon, argon, heli, xenon và dimer xenon, có trục năng lượng "
        "bên trái theo eV và bên phải theo 10³ cm⁻¹",
        "Five energy-level columns for neon, argon, helium, xenon and the xenon dimer, with an "
        "energy axis in eV on the left and in 10³ cm⁻¹ on the right")


# ================================================================ 93.9
def fig_93_9():
    tag = "939"
    o = [_defs(tag)]
    F = Frame(104, 40, 392, 250, (1, 500), (0.03, 5), xlog=True, ylog=True)
    o.append(F.frame())
    o.append(F.vgrid([1, 2, 5, 10, 20, 50, 100, 200, 500]))
    o.append(F.hgrid([0.03, 0.05, 0.1, 0.2, 0.3, 0.5, 1, 2, 3, 5]))
    o.append(F.xticks([(1, "1"), (5, "5"), (20, "20"), (100, "100"), (500, "500")]))
    o.append(F.yticks([(0.03, "0,03"), (0.1, "0,1"), (0.3, "0,3"), (1, "1"), (3, "3"), (5, "5")]))
    o.append(F.xlab("E/P (V/cm·Torr)", 34))
    o.append(F.ylab("η (10² ion pairs/V)", -58))
    for v, lab in ((1, "0,075"), (5, "0,375"), (20, "1,5"), (100, "7,5"), (500, "37,5")):
        px = F.X(v)
        o.append(_line(px, 40, px, 36, 1.1))
        o.append(_lbl(px, 26, lab, "ts", "middle"))
    o.append(_lbl(F.X(20), 14, "E/P (V/m/Pa)", "ts", "middle"))

    # Ten curves, eight of them labelled by number only: the peaks sit within a
    # 30 px band and any in-line text label collides with its neighbour. The key
    # goes in the empty right margin, where nothing can overlap it.
    fam = [(1.02, 1.35, "1", "10⁻¹"), (1.15, 2.7, "2", "10⁻²"),
           (1.55, 2.8, "3", "10⁻³"), (2.3, 2.1, "4", "3·10⁻⁴"),
           (3.2, 2.6, "5", "10⁻⁴"), (5.4, 2.2, "6", "10⁻⁵"),
           (8.0, 1.8, "7", "3·10⁻⁵"), (13.0, 1.5, "8", "10⁻⁶"),
           (40.0, 1.6, "Ne", None), (62.0, 1.4, "Ar", None)]
    for b, pk, lab, frac in fam:
        pts = []
        v = 1.0
        while v <= 500:
            lr = math.log(v / b)
            sg = 0.42 if lr < 0 else 0.85
            val = pk * math.exp(-(lr * lr) / (2 * sg * sg))
            if val >= 0.028:
                pts.append((v, val))
            v *= 1.05
        o.append(F.curve(pts, 1.5, E))
        if frac is None:
            o.append(_lbl(F.X(b) + 4, F.Y(pk) + 11, lab, "ts"))
        elif lab == "1":
            # its peak falls on the axis itself — label it where the curve enters
            o.append(_lbl(F.X(1.02) + 2, F.Y(1.35) - 6, lab, "tb"))
        else:
            o.append(_lbl(F.X(b), F.Y(pk) - 5, lab, "tb", "middle"))

    # key, right margin
    o.append(_lbl(512, 44, "Tỉ lệ Ar", "tb"))
    for i, (b, pk, lab, frac) in enumerate(fam):
        if frac is None:
            continue
        ky = 62 + i * 17
        o.append(_lbl(512, ky, lab, "tb", "middle"))
        o.append(_lbl(522, ky, "= " + frac, "ts"))
    o.append(_lbl(96, 352, "Các đường cong dựng lại theo dạng Townsend α/p = A·exp(−B/(E/P)); "
                           "số trên đường tra theo bảng tỉ lệ Ar bên phải", "txs"))
    return _fig(
        svg(660, 362, "".join(o),
            "Va chạm ion hoá theo cường độ điện trường chia cho áp suất, cho hỗn hợp Ne/Ar"),
        "Hình 93.9 · Số cặp ion tạo được trên mỗi vôn đặt vào, theo E/P, cho các hỗn hợp Ne/Ar có "
        "tỉ lệ Ar khác nhau. Đỉnh dịch sang phải khi nồng độ Ar giảm.",
        "Figure 93.9 · Ion pairs produced per volt applied, against E/P, for Ne/Ar mixtures of "
        "different argon fractions. The peak moves to the right as the argon fraction falls.",
        "Họ đường cong có đỉnh trên trục log-log, đỉnh dịch sang phải khi nồng độ argon giảm",
        "Family of peaked curves on log-log axes, the peak moving right as the argon fraction "
        "decreases")


# ================================================================ 93.10
def fig_93_10():
    tag = "9310"
    o = [_defs(tag)]
    F = Frame(104, 40, 392, 250, (0.1, 300), (1e2, 1e4), xlog=True, ylog=True)
    o.append(F.frame())
    o.append(F.vgrid([0.1, 1, 10, 100]))
    o.append(F.hgrid([1e2, 1e3, 1e4]))
    o.append(F.xticks([(0.1, "0,1"), (1, "1"), (10, "10"), (100, "100")]))
    o.append(F.yticks([(1e2, "10²"), (1e3, "10³"), (1e4, "10⁴")]))
    o.append(F.xlab("Pd (Torr·cm)", 34))
    o.append(F.ylab("Breakdown voltage (V)", -58))
    for v, lab in ((0.13, "0,13"), (1.33, "1,33"), (13.3, "13,3"), (133.3, "133,3")):
        px = F.X(v)
        o.append(_line(px, 40, px, 36, 1.1))
        o.append(_lbl(px, 26, lab, "ts", "middle"))
    o.append(_lbl(F.X(10), 14, "Pd (Pa·m)", "ts", "middle"))

    C = math.log(math.log(1 + 1 / 0.01))
    gases = [(4.0, 80.0, "Ne"), (10.0, 140.0, "Ar"), (5.0, 110.0, "H₂"),
             (15.0, 365.0, "air"), (8.0, 243.0, "Hg")]
    labs = []
    for A, B, name in gases:
        pts = []
        x = 0.12
        while x <= 320:
            den = math.log(A * x) - C
            if den > 0.15:
                v = B * x / den
                if 95 <= v <= 1.15e4:
                    pts.append((x, v))
            x *= 1.04
        o.append(F.curve(pts, 1.6, E))
        if pts:
            pick = min(pts, key=lambda p: abs(p[0] - 90))
            labs.append([F.X(pick[0]), F.Y(pick[1]), name])
    labs.sort(key=lambda t: t[1])
    for i in range(1, len(labs)):
        if labs[i][1] - labs[i - 1][1] < 14:
            labs[i][1] = labs[i - 1][1] + 14
    for px, py, name in labs:
        o.append(_line(px + 1, py, px + 11, py, 0.8, S))
        o.append(_lbl(px + 14, py + 3, name, "tb"))

    o.append(_lbl(96, 352, "Đường cong dựng lại theo định luật Paschen với γ = 0,01; cực tiểu của "
                           "Ne và Ar khớp với hình gốc", "txs"))
    return _fig(
        svg(660, 362, "".join(o),
            "Điện áp đánh thủng theo tích áp suất nhân khoảng cách, cho các khí khác nhau"),
        "Hình 93.10 · Điện áp đánh thủng theo tích Pd (áp suất × khoảng cách) cho không khí, hơi "
        "thuỷ ngân, H₂, Ar và Ne. Mỗi khí có một cực tiểu ở một giá trị Pd riêng; thêm 0,1 % Ar "
        "vào neon hạ cực tiểu từ ~250 V xuống ~150 V.",
        "Figure 93.10 · Breakdown voltage against the Pd product (pressure × gap) for air, mercury "
        "vapour, H₂, Ar and Ne. Each gas has its minimum at its own Pd; adding 0.1% argon to neon "
        "lowers the minimum from ~250 V to ~150 V.",
        "Năm đường cong hình chữ V trên trục log-log, mỗi khí có một cực tiểu điện áp đánh thủng ở "
        "một giá trị Pd riêng",
        "Five V-shaped curves on log-log axes, each gas with its own minimum breakdown voltage at a "
        "particular Pd")
