# -*- coding: utf-8 -*-
"""Figures 93.11–93.20 for Handbook Chapter 93 — Plasma-Driven Flat Panel Displays.

Helpers live in `hb93base.py`; figures 93.1–93.10 are in `hb93fig.py`.

The measured curves (current traces, hysteresis, spectra, quantum efficiency,
MgO transmission) are rebuilt from the printed data points and drawn through
them; the computed ones (Paschen, Townsend, potential profiles) are evaluated
from their own formulas in this file.
"""
import math

from hbfig import svg, _fig
from hb93base import (E, S, GRID, GOLD, BLUE, TEAL, RED, GREEN, GLASS, DIELE, METAL,
                      _defs, _lbl, _r, _line, _arr, _rect, _poly, _path, _dot, _circ,
                      _hatch, _slab, _isostrip, _isostrip_d, Frame)


def _mk(fr, x, y, kind="o", col=E, r=2.2):
    """A data marker on a Frame."""
    px, py = fr.X(x), fr.Y(y)
    if kind == "o":
        return _circ(px, py, r, col, "#fff", 1.0)
    if kind == "f":
        return _dot(px, py, r, col)
    if kind == "x":
        return (_line(px - r, py - r, px + r, py + r, 1.0, col)
                + _line(px - r, py + r, px + r, py - r, 1.0, col))
    if kind == "t":
        return _poly([(px, py - r - 1), (px + r + 1, py + r), (px - r - 1, py + r)], 0.9, "#fff",
                     col)
    if kind == "s":
        return _rect(px - r, py - r, 2 * r, 2 * r, 0.9, "#fff", "", col)
    if kind == "d":
        return _poly([(px, py - r - 1.4), (px + r + 1.4, py), (px, py + r + 1.4),
                      (px - r - 1.4, py)], 0.9, "#fff", col)
    return ""


def _glyph(x, y, kind="o", col=E, r=2.2):
    """The same markers as _mk, but at absolute canvas coordinates (for legends)."""
    if kind == "o":
        return _circ(x, y, r, col, "#fff", 1.0)
    if kind == "f":
        return _dot(x, y, r, col)
    if kind == "x":
        return (_line(x - r, y - r, x + r, y + r, 1.0, col)
                + _line(x - r, y + r, x + r, y - r, 1.0, col))
    if kind == "t":
        return _poly([(x, y - r - 1), (x + r + 1, y + r), (x - r - 1, y + r)], 0.9, "#fff", col)
    if kind == "s":
        return _rect(x - r, y - r, 2 * r, 2 * r, 0.9, "#fff", "", col)
    if kind == "d":
        return _poly([(x, y - r - 1.4), (x + r + 1.4, y), (x, y + r + 1.4),
                      (x - r - 1.4, y)], 0.9, "#fff", col)
    return ""


# ================================================================ 93.11
def fig_93_11():
    tag = "9311"
    o = [_defs(tag)]
    Fa = Frame(96, 40, 430, 130, (0, 100), (0, 150))
    Fb = Frame(96, 208, 430, 130, (0, 100), (0, 150))

    for F, letter in ((Fa, "a)"), (Fb, "b)")):
        o.append(F.frame())
        o.append(F.hgrid([25, 50, 75, 100, 125]))
        o.append(F.vgrid([20, 40, 60, 80]))
        o.append(F.yticks([(0, "0"), (25, "25"), (50, "50"), (75, "75"), (100, "100"),
                           (125, "125"), (150, "150")]))
        o.append(_lbl(96 + 6, F.y + 12, letter, "tb"))
    o.append(Fa.ylab("Potential (V)", -46))
    o.append(Fb.xticks([(0, "0"), (20, "20"), (40, "40"), (60, "60"), (80, "80"), (100, "100")]))
    o.append(Fb.xlab("Position (µm)", 32))
    o.append(_lbl(96, 26, "cathode", "txs"))
    o.append(_lbl(526, 26, "anode", "txs", "end"))

    # (a) high electron density: thin sheaths, flat plasma plateau
    pts = []
    for i in range(0, 101):
        x = i * 1.0
        if x < 60:
            v = 132 * (1 - math.exp(-x / 2.2))
        elif x < 92:
            v = 132 + 0.35 * (x - 60) / 32
        else:
            v = 132.4 + 18 * ((x - 92) / 8.0) ** 1.7
        pts.append((x, v))
    o.append(Fa.curve(pts, 1.8))
    o.append(_lbl(Fa.X(34), Fa.Y(139), "plasma", "txs"))
    o.append(_lbl(Fa.X(3), Fa.Y(58), "sheath", "txs"))
    o.append(_lbl(Fa.X(96), Fa.Y(139), "sheath", "txs", "end"))

    # (b) low electron density: the field fills the gap
    pts = []
    for i in range(0, 101):
        x = i
        t = x / 100.0
        pts.append((x, 150 * (3 * t * t - 2 * t * t * t)))
    o.append(Fb.curve(pts, 1.8))
    return _fig(
        svg(660, 360, "".join(o),
            "Prôfin thế năng trong khe điểm ảnh với mật độ điện tử cao và thấp"),
        "Hình 93.11 · Prôfin thế năng trong khe điểm ảnh: (a) phóng điện mật độ điện tử cao — thế "
        "gần như phẳng trên cả khe, toàn bộ độ giảm tập trung trong hai lớp vỏ mỏng sát điện cực; "
        "(b) phóng điện mật độ điện tử thấp — lớp vỏ chiếm phần lớn khe và prôfin trải đều.",
        "Figure 93.11 · Potential profiles in the pixel gap region: (a) a high-electron-density "
        "discharge, where the potential is nearly flat across the gap and the whole drop sits in "
        "two thin sheaths at the electrodes; (b) a low-electron-density discharge, where the sheath "
        "occupies most of the gap and the profile spreads out.",
        "Hai đồ thị thế năng theo vị trí: trên là prôfin phẳng với hai lớp vỏ mỏng, dưới là đường "
        "cong trải đều khắp khe 100 µm",
        "Two potential-versus-position plots: above a flat profile with two thin sheaths, below a "
        "smooth curve spread across the whole 100 µm gap")


# ================================================================ 93.12
def fig_93_12():
    tag = "9312"
    o = [_defs(tag)]
    F = Frame(96, 40, 400, 240, (0, 300), (0, 2.6))
    o.append(F.frame())
    o.append(F.vgrid([50, 100, 150, 200, 250]))
    o.append(F.hgrid([0.5, 1.0, 1.5, 2.0, 2.5]))
    o.append(F.xticks([(0, "0"), (100, "100"), (200, "200"), (300, "300")]))
    o.append(F.yticks([(0, "0"), (0.5, "0,5"), (1.0, "1"), (1.5, "1,5"), (2.0, "2"),
                       (2.5, "2,5")]))
    o.append(F.xlab("Drive voltage (V)", 34))
    o.append(F.ylab("Pixel current (10⁻⁴ A)", -54))

    # load lines, drawn at the endpoints printed in the source; each one is
    # marked with the supply voltage it belongs to
    for (v0, i0, v1) in ((75, 2.0, 175), (125, 2.0, 225), (175, 2.0, 275)):
        o.append(F.curve([(v0, i0), (v1, 0.0)], 1.4))
        o.append(_lbl(F.X(v0) - 4, F.Y(i0) - 6, "%d V" % v1, "txs", "end"))
    o.append(_lbl(F.X(4), F.Y(2.46), "đường tải 500 kΩ", "txs"))
    o.append(F.curve([(0, 0.7), (175, 0.0)], 1.4))
    o.append(_lbl(F.X(16), F.Y(0.80), "5 MΩ – 175 V", "txs"))

    # the discharge characteristic, traced from the printed curve
    ch = [(0, 0.02), (180, 0.02), (230, 0.025), (243, 0.05), (247, 0.12), (250, 0.30),
          (253, 0.62), (257, 0.95), (262, 1.14), (267, 1.22), (273, 1.18), (280, 1.02),
          (288, 0.82), (300, 0.60)]
    o.append(F.curve(ch, 2.0))

    # the three operating regions of the printed figure, marked on the curve and
    # keyed in the empty right margin (the printed load lines do not actually
    # intersect the negative-resistance branch — see the translator's note)
    o.append(_mk(F, 40, 0.02, "o", E, 2.6))
    o.append(_mk(F, 251, 0.42, "x", E, 2.6))
    o.append(_mk(F, 286, 0.88, "f", E, 2.4))
    o.append(_lbl(508, 56, "Trạng thái", "tb"))
    o.append(_glyph(514, 80, "o", E, 2.6))
    o.append(_lbl(524, 83, "bền – tắt", "ts"))
    o.append(_glyph(514, 106, "x", E, 2.6))
    o.append(_lbl(524, 109, "không bền", "ts"))
    o.append(_glyph(514, 132, "f", E, 2.4))
    o.append(_lbl(524, 135, "bền – bật", "ts"))
    return _fig(
        svg(660, 330, "".join(o),
            "Đặc tuyến dòng–áp của điểm ảnh một chiều khi đánh thủng khí, kèm các đường tải"),
        "Hình 93.12 · Đặc tuyến dòng–áp tiêu biểu của một điểm ảnh một chiều có điện áp đánh thủng "
        "250 V, kèm bốn đường tải. Điện áp 175 V giữ điểm ảnh luôn tắt, 275 V giữ nó luôn sáng; ở "
        "225 V điểm ảnh có hai trạng thái bền nên nhớ được trạng thái của mình.",
        "Figure 93.12 · A representative current–voltage characteristic of a dc pixel with a 250 V "
        "breakdown voltage, with four load lines. At 175 V the pixel is always off, at 275 V always "
        "on; at 225 V it has two stable states, which is what gives it memory.",
        "Đồ thị dòng điện theo điện áp với đặc tuyến có đoạn điện trở âm và bốn đường tải cắt nhau, "
        "kèm chú thích trạng thái bền và không bền",
        "Current-versus-voltage plot with a negative-resistance section and four load lines, "
        "annotated with the stable and unstable operating points")


# ================================================================ 93.13
def fig_93_13():
    tag = "9313"
    o = [_defs(tag)]
    T = 1e-7

    def panel(top, second, title):
        F = Frame(104, top, 380, 110, (1.0, 5.0), (-150, 150))
        G = Frame(104, top, 380, 110, (1.0, 5.0), (-0.5, 2.0))
        p = [F.frame(), F.hgrid([-100, -50, 0, 50, 100]), F.vgrid([1, 2, 3, 4, 5])]
        p.append(F.yticks([(-150, "-150"), (-75, "-75"), (0, "0"), (75, "75"), (150, "150")]))
        p.append(_lbl(482, top - 6, title, "tb", "end"))
        # current axis on the right-hand edge of the same frame
        p.append(_line(484, top, 484, top + 110, 1.2))
        for v in (-0.5, 0, 0.5, 1, 1.5, 2):
            py = G.Y(v)
            p.append(_line(484, py, 488, py, 1.0))
            p.append(_lbl(492, py + 3.2, ("%.1f" % v).replace(".", ","), "ts"))

        t0 = 1.35e-7
        vpts, ipts = [], []
        t = 1.0e-7
        while t <= 5.0e-7:
            if t < t0:
                v = -120.0
            else:
                v = 118.0 + 6 * math.exp(-(t - t0) / 6e-9)
            vpts.append((t / T, v))
            cur = (-0.16 * math.exp(-((t - (t0 - 6e-9)) / 5e-9) ** 2)
                   + 1.62 * math.exp(-(t - t0) / 9e-9) * (1 if t >= t0 else 0))
            if second:
                cur += 0.52 * math.exp(-((t - 2.78e-7) / 2.4e-8) ** 2)
            ipts.append((t / T, cur))
            t += 1.2e-9
        p.append(F.curve(vpts, 1.7))
        p.append(G.curve(ipts, 1.7, GOLD))
        for k in range(0, len(vpts), 6):
            p.append(_mk(F, vpts[k][0], vpts[k][1], "o", E, 2.0))
        return "".join(p)

    o.append(panel(36, False, "a) on state — 117 V"))
    o.append(panel(190, True, "b) off state — 127 V"))
    o.append(_lbl(294, 334, "Time (s)", "ts", "middle"))
    for v in (1, 2, 3, 4, 5):
        o.append(_lbl(104 + 380 * (v - 1) / 4.0, 314, "%d·10⁻⁷" % v, "ts", "middle"))
    o.append('<text class="ts" x="66" y="%s" text-anchor="middle" transform="rotate(-90 66 %s)">'
             'Voltage (V)</text>' % (91, 91))
    o.append('<text class="ts" x="532" y="%s" text-anchor="middle" transform="rotate(-90 532 %s)">'
             'Current (A)</text>' % (91, 91))
    return _fig(
        svg(660, 344, "".join(o),
            "Dạng sóng điện áp và dòng điện của mảng 45 × 45 điểm ảnh plasma xoay chiều"),
        "Hình 93.13 · Dạng sóng điện áp (đường đen) và dòng điện (đường nâu) của mảng 45 × 45 điểm "
        "ảnh plasma xoay chiều ở trạng thái (a) bật và (b) tắt, với biên độ điện áp điều khiển 117 "
        "và 127 V. Xung dòng hẹp ở sườn lên là dòng nạp điện dung; ở trạng thái tắt xuất hiện thêm "
        "một gò dòng thứ hai do phóng điện trong khe khí.",
        "Figure 93.13 · Voltage (black) and current (brown) traces for a 45 × 45 array of ac plasma "
        "pixels in the (a) on and (b) off states, at drive amplitudes of 117 and 127 V. The narrow "
        "spike on the leading edge is the capacitive displacement current; in the off state a second "
        "hump appears from the discharge in the gas gap.",
        "Hai cặp dạng sóng xếp trên dưới: điện áp xung vuông chuyển từ âm sang dương và dòng điện "
        "có xung nhọn ở sườn lên",
        "Two stacked waveform pairs: a square voltage step from negative to positive with a sharp "
        "current spike on its leading edge")


# ================================================================ 93.14
def fig_93_14():
    tag = "9314"
    o = [_defs(tag)]
    F = Frame(96, 40, 400, 250, (100, 250), (0, 6.4))
    o.append(F.frame())
    o.append(F.vgrid([120, 140, 160, 180, 200, 220, 240]))
    o.append(F.hgrid([1, 2, 3, 4, 5, 6]))
    o.append(F.xticks([(100, "100"), (120, "120"), (140, "140"), (160, "160"), (180, "180"),
                       (200, "200"), (220, "220"), (240, "240")]))
    o.append(F.yticks([(0, "0"), (1, "1"), (2, "2"), (3, "3"), (4, "4"), (5, "5"), (6, "6")]))
    o.append(F.xlab("Applied voltage amplitude (V)", 34))
    o.append(F.ylab("Charge displacement (10⁻⁹ C)", -54))

    up = [(100, 0), (128, 0), (133, 0.05), (140, 0.18), (148, 0.45), (156, 0.78),
          (164, 1.20), (172, 1.62), (180, 2.05), (190, 2.80), (200, 3.70), (210, 4.35),
          (220, 4.95), (230, 5.40), (240, 5.80), (250, 6.15)]
    dn = [(100, 0), (190, 0), (195, 0.10), (200, 0.45), (205, 1.05), (210, 2.20),
          (216, 3.35), (222, 4.30), (230, 5.10), (240, 5.70), (250, 6.10)]
    o.append(F.curve(up, 1.7))
    o.append(F.curve(dn, 1.7, BLUE))
    for i in range(0, len(up), 1):
        o.append(_mk(F, up[i][0], up[i][1], "x", E, 2.6))
    for i in range(0, len(dn), 1):
        o.append(_mk(F, dn[i][0], dn[i][1], "t", BLUE, 2.6))

    o.append(_rect(106, 94, 142, 40, 1.0, "#fff"))
    o.append(_line(112, 108, 128, 108, 1.6))
    o.append(_line(116, 104, 124, 112, 1.0, E) + _line(116, 112, 124, 104, 1.0, E))
    o.append(_lbl(134, 111, "Increasing voltage", "txs"))
    o.append(_line(112, 124, 128, 124, 1.6, BLUE))
    o.append(_lbl(134, 127, "Decreasing voltage", "txs"))

    o.append(_lbl(F.X(152), F.Y(2.6), "on", "tb"))
    o.append(_lbl(F.X(178), F.Y(0.45), "off", "tb"))
    for v, lab in ((118, "erase"), (160, "sustain"), (200, "address")):
        px = F.X(v)
        o.append(_line(px, F.y + 16, px, F.y + F.h, 0.9, S, "4 3"))
        o.append(_arr(px, F.y + 30, px, F.y + F.h - 2, tag, 1.0, E, "h"))
        o.append(_r(px, F.y + 11, [("V", False), (lab, True)], "middle", "ts"))
    return _fig(
        svg(660, 356, "".join(o),
            "Dịch chuyển điện tích theo biên độ điện áp đặt vào, cho mảng 45 × 45 điểm ảnh"),
        "Hình 93.14 · Điện tích dịch chuyển của mảng 45 × 45 điểm ảnh xoay chiều điện cực đối diện "
        "trong hỗn hợp khí He–Xe (2 %) ở 53,3 kPa (400 Torr). Vòng trễ giữa nhánh tăng và nhánh "
        "giảm điện áp chính là tính nhớ của điểm ảnh; ba mũi tên đánh dấu điện áp xoá, điện áp duy "
        "trì và điện áp địa chỉ.",
        "Figure 93.14 · Discharge charge displacement for a 45 × 45 array of ac opposed-electrode "
        "pixels in a He–Xe (2%) mixture at 53.3 kPa (400 Torr). The loop between the increasing and "
        "decreasing branches is the pixel's memory; the three arrows mark the erase, sustain and "
        "address voltages.",
        "Đồ thị điện tích theo biên độ điện áp với hai nhánh tạo thành vòng trễ, đánh dấu ba mức "
        "điện áp xoá, duy trì và địa chỉ",
        "Charge-versus-voltage plot with two branches forming a hysteresis loop, marking the erase, "
        "sustain and address voltages")


# ================================================================ 93.15
def fig_93_15():
    tag = "9315"
    o = [_defs(tag)]
    W, X0 = 400, 104
    rows = [([("V", False), ("sustain", True)], 36, -200, 200),
            ([("V", False), ("address", True)], 130, -200, 200),
            ([("Pixel current density (kA/m²)", False)], 224, -20, 20),
            ([("V", False), ("surface", True)], 318, -200, 200)]

    def X(x):
        return X0 + (x / 6.5) * W

    for parts, top, lo, hi in rows:
        F = Frame(X0, top, W, 74, (0, 6.5), (lo, hi))
        o.append(F.frame())
        o.append(F.hgrid([0]))
        o.append(F.yticks([(lo, "%d" % lo), (0, "0"), (hi, "%d" % hi)]))
        o.append(_r(X0, top - 5, parts, "start", "txs"))

    # sustain: alternating ±180 V square wave
    seq = []
    x = 0.2
    sign = 1
    for k in range(7):
        seq.append((x, sign * 180))
        seq.append((x + 0.45, sign * 180))
        x += 0.45
        sign = -sign
        seq.append((x, sign * 180))
    Fs = Frame(X0, 36, W, 74, (0, 6.5), (-200, 200))
    o.append(Fs.curve(seq, 1.6))

    # address pulses
    Fa = Frame(X0, 130, W, 74, (0, 6.5), (-200, 200))
    o.append(Fa.curve([(0, 0), (1.55, 0), (1.55, 200), (2.0, 200), (2.0, 0), (4.1, 0),
                       (4.1, -120), (4.5, -120), (4.5, 0), (6.5, 0)], 1.6, BLUE))

    # current density: a spike at every sustain edge, dying away after the erase
    Fc = Frame(X0, 224, W, 74, (0, 6.5), (-20, 20))
    amps = [17, 15, 13, 10, 7, 4, 2.5]
    p = []
    for k, a in enumerate(amps):
        xe = 0.2 + k * 0.9
        p += [(xe - 0.03, 0), (xe, a), (xe + 0.05, -a * 0.55), (xe + 0.12, 0)]
    o.append(Fc.curve(p, 1.4, GOLD))

    # wall voltage: ±160 V, decaying to zero after the erase pulse
    Fw = Frame(X0, 318, W, 74, (0, 6.5), (-200, 200))
    w = []
    x = 0.2
    s = 1
    for k in range(5):
        w += [(x, 0), (x + 0.06, s * 160), (x + 0.45, s * 160), (x + 0.51, 0)]
        x += 0.9
        s = -s
    w += [(4.55, -110), (5.0, 60), (5.6, 40), (6.2, 8), (6.5, 0)]
    o.append(Fw.curve(w, 1.6))

    o.append(_lbl(X(1.75), 120, "address", "ts", "middle"))
    o.append(_lbl(X(4.3), 120, "erase", "ts", "middle"))
    o.append(_lbl(X0 + W / 2.0, 408, "thời gian (theo chu kỳ duy trì)", "ts", "middle"))
    return _fig(
        svg(660, 420, "".join(o),
            "Dạng sóng duy trì và địa chỉ của điểm ảnh plasma xoay chiều"),
        "Hình 93.15 · Dạng sóng điện áp duy trì và điện áp địa chỉ của điểm ảnh plasma xoay chiều, "
        "kèm mật độ dòng điện điểm ảnh và điện áp thành (do điện tích bề mặt). Xung địa chỉ 200 V "
        "bật điểm ảnh; xung xoá 120 V làm điện tích bề mặt suy giảm nên các xung duy trì sau đó "
        "không còn gây phóng điện.",
        "Figure 93.15 · Sustain and address voltage waveforms for ac plasma pixels, with the pixel "
        "current density and the wall voltage produced by the surface charge. A 200 V address pulse "
        "turns the pixel on; a 120 V erase pulse lets the surface charge decay so that the "
        "following sustain pulses no longer fire the cell.",
        "Bốn dạng sóng xếp dọc: điện áp duy trì xung vuông đối xứng, xung địa chỉ và xung xoá, mật "
        "độ dòng điện có gai ở mỗi sườn, và điện áp thành tắt dần sau xung xoá",
        "Four stacked waveforms: a symmetric square sustain voltage, address and erase pulses, a "
        "current density spiking at every edge, and a wall voltage decaying after the erase pulse")


# ================================================================ 93.16
def fig_93_16():
    tag = "9316"
    o = [_defs(tag)]
    o.append(_lbl(24, 26, "(a) driver system", "tb"))
    o.append(_lbl(360, 20, "(b) temporal sequences", "tb"))

    # ---- block diagram
    o.append(_rect(70, 34, 190, 18, 1.1, "#fff"))
    o.append(_lbl(165, 46, "HDTV Signal Processor", "txs", "middle"))
    o.append(_lbl(165, 30, "HDTV signal", "txs", "middle"))
    o.append(_line(165, 34, 165, 28, 1.0))
    o.append(_line(165, 52, 165, 62, 1.0))
    o.append(_rect(30, 62, 290, 196, 1.0, "none", "4 3", S))
    o.append(_lbl(300, 252, "40-in. Display", "txs", "end"))

    for i, name in enumerate(("Upper Display Anode Driver", "Upper Auxiliary Anode Driver")):
        o.append(_rect(78, 70 + i * 20, 190, 15, 1.0, "#fff"))
        o.append(_lbl(173, 81 + i * 20, name, "txs", "middle"))
    for i, name in enumerate(("Lower Auxiliary Anode Driver", "Lower Display Anode Driver")):
        o.append(_rect(78, 206 + i * 20, 190, 15, 1.0, "#fff"))
        o.append(_lbl(173, 217 + i * 20, name, "txs", "middle"))

    # the panel
    o.append(_rect(120, 116, 120, 76, 1.0, "#fafafa"))
    for r in range(7):
        o.append(_line(120, 122 + r * 10, 240, 122 + r * 10, 0.6, "#c9c9c9"))
    for c in range(9):
        o.append(_line(126 + c * 13, 116, 126 + c * 13, 192, 0.6, "#c9c9c9"))
    o.append(_lbl(180, 156, "40-in. panel", "txs", "middle"))
    o.append(_line(173, 110, 173, 116, 1.0))
    o.append(_line(173, 192, 173, 206, 1.0))

    # cathode drivers and interface
    o.append(_rect(92, 116, 20, 76, 1.0, "#fff"))
    o.append('<text class="txs" x="%s" y="%s" text-anchor="middle" transform="rotate(-90 %s %s)">'
             'Cathode drivers</text>' % (102, 154, 102, 154))
    o.append(_rect(42, 130, 22, 48, 1.0, "#fff"))
    o.append('<text class="txs" x="%s" y="%s" text-anchor="middle" transform="rotate(-90 %s %s)">'
             'Interface</text>' % (53, 154, 53, 154))
    o.append(_line(64, 154, 92, 154, 1.0))

    # ---- timing diagram
    tx0, tw = 372, 268
    def TX(u):
        return tx0 + u * tw

    o.append(_lbl(tx0 - 6, 48, "Upper", "txs", "end"))
    o.append(_lbl(tx0 - 6, 58, "anode", "txs", "end"))
    o.append(_lbl(tx0 - 6, 100, "Upper", "txs", "end"))
    o.append(_lbl(tx0 - 6, 110, "cathodes", "txs", "end"))
    o.append(_lbl(tx0 - 6, 168, "Lower", "txs", "end"))
    o.append(_lbl(tx0 - 6, 178, "cathodes", "txs", "end"))
    o.append(_lbl(tx0 - 6, 232, "Lower", "txs", "end"))
    o.append(_lbl(tx0 - 6, 242, "anode", "txs", "end"))

    # upper anode: sustain pulses, write pulse, erase pulse
    o.append(_path([(TX(0.02), 74), (TX(0.10), 74), (TX(0.10), 52), (TX(0.16), 52),
                    (TX(0.16), 74), (TX(0.26), 74), (TX(0.26), 52), (TX(0.32), 52),
                    (TX(0.32), 74), (TX(0.52), 74), (TX(0.52), 44), (TX(0.60), 44),
                    (TX(0.60), 74), (TX(0.74), 74), (TX(0.74), 52), (TX(0.80), 52),
                    (TX(0.80), 74), (TX(0.90), 74), (TX(0.90), 64), (TX(0.96), 64),
                    (TX(0.96), 74), (TX(1.0), 74)], 1.3))
    o.append(_lbl(TX(0.12), 32, "Sustain pulse (two-step)", "txs"))
    o.append(_lbl(TX(0.56), 38, "Write", "txs", "middle"))
    o.append(_lbl(TX(0.93), 56, "Erase", "txs", "middle"))

    # upper cathodes: scan pulses
    for i in range(4):
        y = 92 + i * 8
        o.append(_path([(TX(0.02), y), (TX(0.12 + i * 0.04), y),
                        (TX(0.12 + i * 0.04), y - 12), (TX(0.17 + i * 0.04), y - 12),
                        (TX(0.17 + i * 0.04), y), (TX(1.0), y)], 1.1, E if i < 2 else S))
    o.append(_lbl(TX(0.34), 132, "Scan pulse", "txs"))

    # lower cathodes
    for i in range(3):
        y = 160 + i * 8
        o.append(_path([(TX(0.02), y), (TX(0.30 + i * 0.06), y), (TX(0.30 + i * 0.06), y - 10),
                        (TX(0.36 + i * 0.06), y - 10), (TX(0.36 + i * 0.06), y), (TX(1.0), y)],
                       1.1, E if i < 2 else S))

    # lower anode: on-state pulses
    o.append(_path([(TX(0.02), 236), (TX(0.16), 236), (TX(0.16), 216), (TX(0.30), 216),
                    (TX(0.30), 236), (TX(0.44), 236), (TX(0.44), 216), (TX(0.58), 216),
                    (TX(0.58), 236), (TX(0.72), 236), (TX(0.72), 216), (TX(0.86), 216),
                    (TX(0.86), 236), (TX(1.0), 236)], 1.3))
    o.append(_lbl(TX(0.38), 208, "On-state pulses", "txs"))
    o.append(_lbl(TX(0.60), 262, "thời gian", "ts", "middle"))
    o.append(_line(TX(0.02), 250, TX(1.0), 250, 1.0))
    return _fig(
        svg(660, 330, "".join(o),
            "Sơ đồ khối hệ vi điều khiển và giản đồ thời gian của màn hình plasma một chiều NHK"),
        "Hình 93.16 · Chế độ nhớ xung của màn hình plasma một chiều NHK: (a) sơ đồ khối hệ điều "
        "khiển và mảng điểm ảnh; (b) giản đồ thời gian của chế độ nhớ xung, với các xung duy trì, "
        "xung ghi, xung xoá và các xung quét trên cathode.",
        "Figure 93.16 · Pulsed memory operation of the NHK dc plasma display: (a) block diagram of "
        "the driver system and pixel array; (b) the temporal sequences, with sustain, write and "
        "erase pulses and the scan pulses on the cathodes.",
        "Sơ đồ khối bên trái với bốn bộ điều khiển anode, bộ điều khiển cathode và giao diện; bên "
        "phải là bốn dãy xung thời gian",
        "Block diagram on the left with four anode drivers, cathode drivers and an interface; four "
        "timing traces on the right")


# ================================================================ 93.17
def fig_93_17():
    tag = "9317"
    o = [_defs(tag)]
    bx, bw, dx, dy = 168, 300, 52, 28
    yf, yr = 150, 268

    # rear plate + cathodes
    o.append(_slab(bx, yr, bw, 150, 9, dx, dy))
    for i in range(5):
        o.append(_isostrip_d(bx + 26 + i * 56, yr, 8, 0.9, dx, dy))

    # cells: barriers with phosphor on the inner walls, two rows deep
    cols = [RED, GREEN, BLUE, RED, GREEN]
    for i in range(5):
        x = bx + 22 + i * 56
        o.append(_rect(x, yr - 40, 8, 40, 0.9, "#f0f0f0"))
        o.append(_poly([(x, yr - 40), (x + 8, yr - 40), (x + 8 + dx, yr - 40 - dy),
                        (x + dx, yr - 40 - dy)], 0.9, "#fafafa"))
        o.append(_rect(x + 9, yr - 34, 44, 34, 0.9, cols[i]))
        o.append(_poly([(x + 9, yr - 34), (x + 53, yr - 34), (x + 53 + dx, yr - 34 - dy),
                        (x + 9 + dx, yr - 34 - dy)], 0.9, "#ffffff", S))
    # the sixth barrier closes the row
    x = bx + 22 + 5 * 56
    o.append(_rect(x, yr - 40, 8, 40, 0.9, "#f0f0f0"))

    # front plate with display and auxiliary anodes
    o.append(_slab(bx, yf, bw, 150, 8, dx, dy, "#fbfbfb"))
    for d0 in (0.3, 0.62):
        o.append(_isostrip(bx + 6, yf, bw - 12, d0, 0.12, dx, dy, "#e9eef5", "#8fa6bf"))

    # leaders
    o.append(_line(bx + 40, yf + 4, 120, 128, 0.8, S))
    o.append(_lbl(116, 124, "Front plate", "tb", "end"))
    o.append(_line(bx + bw * 0.2 + dx * 0.62, yf - dy * 0.62, 508, 92, 0.8, S))
    o.append(_lbl(512, 86, "Upper auxiliary", "tb"))
    o.append(_lbl(512, 97, "anode", "tb"))
    o.append(_line(bx + bw * 0.55 + dx * 0.3, yf - dy * 0.3, 508, 118, 0.8, S))
    o.append(_lbl(512, 112, "Upper display", "tb"))
    o.append(_lbl(512, 123, "anode", "tb"))
    o.append(_line(bx + bw + 10, yr - 24, 508, 160, 0.8, S))
    o.append(_lbl(512, 156, "Phosphor (R, G, B)", "tb"))
    o.append(_line(bx + bw + 8, yr + 4, 508, 214, 0.8, S))
    o.append(_lbl(512, 212, "Rear plate", "tb"))
    o.append(_line(bx + 90, yr + 5, 120, 236, 0.8, S))
    o.append(_lbl(116, 232, "Cathode", "tb", "end"))
    o.append(_line(bx + 30, yr - 12, 120, 300, 0.8, S))
    o.append(_lbl(116, 296, "Barrier", "tb", "end"))
    o.append(_lbl(bx + 60, yr + 30, "Display cell", "txs"))
    o.append(_lbl(bx + 230, yr + 30, "Auxiliary cell", "txs"))
    # the label belongs in the gap between the plate and the barrier tops,
    # not across the barrier top faces (yr-54 landed inside the cells)
    o.append(_lbl(bx + 150, 186, "Priming space", "txs", "middle"))
    o.append(_line(bx + 150, 190, bx + 150, 198, 0.7, S))
    return _fig(
        svg(660, 330, "".join(o),
            "Cấu trúc màn hiển thị plasma màu 40 inch của NHK"),
        "Hình 93.17 · Cấu trúc màn hiển thị màu 102 cm (40 in.) của NHK: tấm trước mang điện cực "
        "anode hiển thị và anode phụ, tấm sau mang cathode, giữa là các ô tổ ong có vách phủ "
        "phosphor đỏ, lục, lam; ô thứ tư của mỗi cụm là ô phụ tạo điện tử mồi.",
        "Figure 93.17 · Structure of the 40-in. colour display manufactured by NHK: the front plate "
        "carries the display and auxiliary anodes, the rear plate the cathodes, and between them a "
        "honeycomb of cells whose walls carry red, green and blue phosphors; the fourth cell of each "
        "group is an auxiliary cell that supplies priming electrons.",
        "Sơ đồ lớp của màn hình plasma màu: tấm trước có hai loại anode, các ô tổ ong phủ phosphor "
        "ba màu, tấm sau có cathode",
        "Layer diagram of the colour plasma display: front plate with two kinds of anode, honeycomb "
        "cells coated with three phosphor colours, and a rear plate carrying the cathodes")


# ================================================================ 93.18
def fig_93_18():
    tag = "9318"
    o = [_defs(tag)]
    F = Frame(96, 40, 400, 250, (120, 250), (0, 2.8))
    o.append(F.frame())
    o.append(F.vgrid([120, 140, 160, 180, 200, 220, 240]))
    o.append(F.hgrid([0.5, 1.0, 1.5, 2.0, 2.5]))
    o.append(F.xticks([(120, "120"), (140, "140"), (160, "160"), (180, "180"), (200, "200"),
                       (220, "220"), (240, "240")]))
    o.append(F.yticks([(0, "0"), (0.5, "0,5"), (1.0, "1"), (1.5, "1,5"), (2.0, "2"),
                       (2.5, "2,5")]))
    o.append(F.xlab("Wavelength (nm)", 34))
    o.append(F.ylab("Intensity (arbitrary units)", -54))

    # Xe fraction: (atomic 147 nm, atomic 129 nm, dimer band)
    data = [("0,1%", 1.50, 0.12, 0.04, "f"), ("1%", 0.78, 0.10, 0.32, "o"),
            ("2%", 0.36, 0.05, 0.10, "-"), ("5%", 0.26, 0.04, 0.85, "t"),
            ("10%", 0.16, 0.03, 1.45, "s"), ("20%", 0.10, 0.02, 2.65, "d")]
    for name, a147, a129, ad, mk in data:
        pts = []
        lam = 120.0
        while lam <= 250:
            v = (a147 * math.exp(-((lam - 147.0) / 2.4) ** 2)
                 + a129 * math.exp(-((lam - 129.0) / 2.0) ** 2)
                 + ad * math.exp(-((lam - 173.0) / 9.5) ** 2))
            pts.append((lam, v))
            lam += 0.5
        if mk == "-":
            o.append(F.curve(pts, 1.2, "#9a9a9a"))
        else:
            o.append(F.curve(pts, 1.4, E if mk in ("f", "d") else "#555"))
            for i in range(0, len(pts), 14):
                o.append(_mk(F, pts[i][0], pts[i][1], mk, E if mk in ("f", "d") else "#555", 1.9))

    o.append(_rect(390, 50, 116, 88, 1.0, "#fff"))
    for i, (name, _a, _b, _c, mk) in enumerate(data):
        y = 64 + i * 13
        if mk == "-":
            o.append(_line(396, y - 3, 404, y - 3, 1.2, "#9a9a9a"))
        else:
            o.append(_glyph(400, y - 3, mk, E, 1.9))
        o.append(_lbl(410, y, name + " Xe", "txs"))
    return _fig(
        svg(660, 330, "".join(o),
            "Phổ phát xạ tử ngoại chân không của điểm ảnh plasma xoay chiều trong hỗn hợp He/Xe"),
        "Hình 93.18 · Phổ phát xạ tử ngoại chân không (VUV) của điểm ảnh plasma xoay chiều điện cực "
        "đối diện trong hỗn hợp He/Xe. Mỗi phổ đo ở gần điện áp duy trì cực tiểu của hỗn hợp đó, từ "
        "150 V với 0,1 % Xe đến 350 V với 20 % Xe. Vạch 147 nm của Xe tắt dần khi tăng nồng độ Xe, "
        "trong khi dải rộng của dimer Xe₂* quanh 173 nm lớn lên.",
        "Figure 93.18 · VUV emission spectra from opposed-electrode ac plasma pixels in He/Xe "
        "mixtures. Each spectrum was taken near the minimum sustain voltage for that mixture, from "
        "150 V at 0.1% Xe to 350 V at 20% Xe. The 147 nm atomic xenon line fades as the xenon "
        "fraction rises while the broad Xe₂* dimer band near 173 nm grows.",
        "Sáu phổ chồng nhau: vạch nhọn ở 147 nm và dải rộng quanh 173 nm, dải rộng lớn dần khi nồng "
        "độ xenon tăng",
        "Six overlaid spectra: a sharp line at 147 nm and a broad band near 173 nm that grows with "
        "the xenon fraction")


# ================================================================ 93.19
def fig_93_19():
    tag = "9319"
    o = [_defs(tag)]
    F = Frame(96, 40, 380, 250, (140, 260), (0, 1.8))
    o.append(F.frame())
    o.append(F.vgrid([140, 160, 180, 200, 220, 240, 260]))
    o.append(F.hgrid([0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8]))
    o.append(F.xticks([(140, "140"), (160, "160"), (180, "180"), (200, "200"), (220, "220"),
                       (240, "240"), (260, "260")]))
    o.append(F.yticks([(0, "0"), (0.2, "0,2"), (0.4, "0,4"), (0.6, "0,6"), (0.8, "0,8"),
                       (1.0, "1,0"), (1.2, "1,2"), (1.4, "1,4"), (1.6, "1,6"), (1.8, "1,8")]))
    o.append(F.xlab("Wavelength (nm)", 34))
    o.append(F.ylab("Relative quantum efficiency", -54))

    # LaPO4:Tb — high and flat to ~200 nm, then falling
    la = [(140, 1.16), (150, 1.22), (160, 1.20), (170, 1.26), (180, 1.27), (190, 1.22),
          (200, 1.05), (210, 0.85), (220, 0.76), (230, 0.88), (240, 0.92), (250, 0.74),
          (260, 0.70)]
    # Zn2SiO4:Mn, commercial 3
    z3 = [(140, 0.30), (150, 0.36), (160, 0.44), (170, 0.50), (180, 0.56), (190, 0.60),
          (200, 0.52), (210, 0.28), (220, 0.22), (230, 0.26), (240, 0.30), (250, 0.40),
          (260, 0.44)]
    # Zn2SiO4:Mn, commercial 1
    z1 = [(140, 0.34), (150, 0.40), (160, 0.50), (170, 0.60), (180, 0.78), (190, 0.82),
          (200, 0.80), (210, 0.72), (220, 0.82), (230, 0.95), (240, 0.92), (250, 0.78),
          (260, 0.74)]
    for pts, dash, col in ((la, "8 3 2 3", E), (z3, "2 3", "#666"), (z1, "", E)):
        dense = []
        for i in range(len(pts) - 1):
            x0, y0 = pts[i]
            x1, y1 = pts[i + 1]
            for k in range(8):
                dense.append((x0 + (x1 - x0) * k / 8.0, y0 + (y1 - y0) * k / 8.0))
        dense.append(pts[-1])
        o.append(F.curve(dense, 1.6, col, dash))

    o.append(_rect(100, 46, 214, 50, 1.0, "#fff"))
    for i, (txt, dash) in enumerate((("(La₀.₈₇Tb₀.₁₃)PO₄", "8 3 2 3"),
                                     ("Zn₂SiO₄:Mn²⁺ (commercial 3)", "2 3"),
                                     ("Zn₂SiO₄:Mn²⁺ (commercial 1)", ""))):
        y = 60 + i * 14
        o.append(_line(106, y - 3, 126, y - 3, 1.6, E, dash))
        o.append(_lbl(132, y, txt, "txs"))
    return _fig(
        svg(660, 330, "".join(o),
            "Hiệu suất lượng tử tương đối của vài loại phosphor lục theo bước sóng kích thích"),
        "Hình 93.19 · Hiệu suất lượng tử tương đối của phosphor lục LaPO₄:Tb so với hai loại "
        "Zn₂SiO₄:Mn thương mại, theo bước sóng kích thích. Hiệu suất phụ thuộc mạnh vào bước sóng "
        "của photon VUV dùng để kích thích.",
        "Figure 93.19 · Relative quantum efficiencies of a Tb-activated lanthanum phosphate against "
        "two commercial Zn₂SiO₄:Mn phosphors, as a function of excitation wavelength. The efficiency "
        "depends strongly on the wavelength of the VUV photon that excites it.",
        "Ba đường cong hiệu suất lượng tử theo bước sóng: một loại cao và phẳng tới 200 nm, hai loại "
        "thấp hơn có đỉnh nhọn",
        "Three quantum-efficiency curves against wavelength: one high and flat to 200 nm, two lower "
        "ones with sharper peaks")


# ================================================================ 93.20
def fig_93_20():
    tag = "9320"
    o = [_defs(tag)]
    F = Frame(96, 40, 380, 250, (120, 220), (0.001, 1.0), ylog=True)
    o.append(F.frame())
    o.append(F.vgrid([120, 140, 160, 180, 200, 220]))
    o.append(F.hgrid([0.001, 0.01, 0.1, 1.0]))
    o.append(F.xticks([(120, "120"), (140, "140"), (160, "160"), (180, "180"), (200, "200"),
                       (220, "220")]))
    o.append(F.yticks([(0.001, "0,001"), (0.01, "0,01"), (0.1, "0,1"), (1, "1")]))
    o.append(F.xlab("Wavelength (nm)", 34))
    o.append(F.ylab("Transmission", -54))

    curves = [
        ("LiF w/75,3 nm MgO pre-bake", "o", "",
         [(132, 0.020), (140, 0.038), (150, 0.052), (156, 0.045), (160, 0.05), (165, 0.16),
          (170, 0.30), (178, 0.40), (190, 0.48), (200, 0.52), (210, 0.56), (220, 0.60)]),
        ("LiF w/200 nm MgO pre-bake", "o", "5 3",
         [(132, 0.006), (140, 0.008), (150, 0.008), (156, 0.007), (160, 0.012), (165, 0.05),
          (170, 0.09), (178, 0.20), (190, 0.30), (200, 0.36), (210, 0.40), (220, 0.42)]),
        ("LiF w/75,3 nm MgO post-bake", "t", "8 3 2 3",
         [(132, 0.030), (140, 0.055), (150, 0.070), (156, 0.060), (160, 0.12), (165, 0.40),
          (170, 0.55), (178, 0.62), (190, 0.68), (200, 0.74), (210, 0.80), (220, 0.90)]),
        ("LiF w/200 nm MgO post-bake", "s", "8 3 2 3",
         [(132, 0.007), (140, 0.009), (150, 0.008), (156, 0.005), (160, 0.02), (165, 0.10),
          (170, 0.25), (178, 0.42), (190, 0.50), (200, 0.55), (210, 0.58), (220, 0.62)]),
    ]
    for name, mk, dash, pts in curves:
        dense = []
        for i in range(len(pts) - 1):
            x0, y0 = pts[i]
            x1, y1 = pts[i + 1]
            for k in range(6):
                dense.append((x0 + (x1 - x0) * k / 6.0,
                              math.exp(math.log(y0) + (math.log(y1) - math.log(y0)) * k / 6.0)))
        dense.append(pts[-1])
        o.append(F.curve(dense, 1.5, E, dash))
        for p in pts:
            o.append(_mk(F, p[0], p[1], mk, E, 2.0))

    o.append(_rect(300, 198, 172, 80, 1.0, "#fff"))
    o.append(_lbl(306, 212, "LiF window, MgO film:", "txs"))
    for i, (name, mk, dash, _p) in enumerate(curves):
        y = 228 + i * 13
        o.append(_line(306, y - 3, 330, y - 3, 1.5, E, dash))
        o.append(_glyph(318, y - 3, mk, E, 1.9))
        o.append(_lbl(336, y, name.replace("LiF w/", "").replace("MgO ", ""), "txs"))
    return _fig(
        svg(660, 330, "".join(o),
            "Độ truyền qua của màng MgO theo bước sóng, trước và sau khi nung khử nước"),
        "Hình 93.20 · Độ truyền qua photon của màng MgO theo bước sóng, trước và sau khi nung để "
        "đuổi hơi nước. Vạch 129 và 147 nm của Xe bị màng MgO dày 75 nm làm suy giảm tới 95 %, "
        "trong khi dải dimer quanh 173 nm chỉ còn 30–50 %.",
        "Figure 93.20 · Photon transmission through MgO films against wavelength, before and after "
        "bake-out to remove water vapour. The 129 and 147 nm xenon lines are attenuated by up to 95% "
        "by a 75 nm MgO film, while the dimer band near 173 nm keeps 30–50%.",
        "Bốn đường cong truyền qua theo bước sóng trên thang log, nhóm trước nung thấp hơn nhóm sau "
        "nung",
        "Four transmission curves against wavelength on a log scale, the pre-bake group lower than "
        "the post-bake group")
