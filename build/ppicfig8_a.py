# -*- coding: utf-8 -*-
"""Vector figures 8.1-8.7 for PPIC chapter 8 (coal-bucket dampers).

Genuine vector redraws of the printed figures on PDF pages 173-185: the
simplified plant with and without three CBDs, the 1:30 shaking-table model and
its dimensions, the first vibration control mode, the transfer functions with
and without optimal CBDs, the objective-function surfaces and sections, the
CBD assembly schematic, and the CBD mechanical model / construction / layout.
"""
import math

from ppicfig8_common import (BLUE, GREEN, GREY, INK, RED, H, W, T, _ar, _b,
                             _circle, _defs, _ellipse, _fig, _frame, _legend,
                             _line, _path, _poly, _rect, _mk, _series,
                             _wavey, make_registry)

FIGS, _reg = make_registry()

STEEL = "#7f8c8d"
BUCKET = "#2e8b57"
ROD = "#d4ac0d"
ELAST = "#8e44ad"


# ------------------------------------------------------------------ helpers
def _ground(o, x0, x1, y):
    o.append(_line(x0, y, x1, y, sw=1.2))
    x = x0
    while x <= x1:
        o.append(_line(x, y, x - 5, y + 6, sw=0.7, color=GREY))
        x += 10


def _spring(o, x1, x2, y, turns=4, amp=5, color=INK):
    n = turns * 2
    pts = [(x1, y)]
    for i in range(1, n):
        pts.append((x1 + (x2 - x1) * i / float(n), y + (amp if i % 2 else -amp)))
    pts.append((x2, y))
    o.append(_poly(pts, sw=1.1, color=color))


def _dashpot(o, x1, x2, y, color=INK):
    mid = (x1 + x2) / 2.0
    o.append(_line(x1, y, mid - 5, y, sw=1.0, color=color))
    o.append(_rect(mid - 5, y - 4, 10, 8, fill="none", sw=1.0, stroke=color))
    o.append(_line(mid, y - 5, mid, y + 5, sw=1.0, color=color))
    o.append(_line(mid + 5, y, x2, y, sw=1.0, color=color))


def _tri(o, cx, cy, r, color=BLUE):
    o.append(_poly([(cx, cy - r), (cx + r * 0.9, cy + r * 0.75),
                    (cx - r * 0.9, cy + r * 0.75)],
                   fill=color, sw=0, color=color, close=True))


def _plant(o, x0, x1, ytop, ybase, cbd=False):
    """Three-bay, four-storey shear frame; CBDs sit at the third storey."""
    bw = (x1 - x0) / 3.0
    sh = (ybase - ytop) / 4.0
    for i in range(4):
        xx = x0 + i * bw
        o.append(_line(xx, ytop, xx, ybase, sw=1.7))
    for j in range(5):
        yy = ytop + j * sh
        o.append(_line(x0, yy, x1, yy, sw=1.2))
    _ground(o, x0 - 12, x1 + 12, ybase)
    yb = ytop + 2 * sh
    yt = ytop + 3 * sh
    for i in range(3):
        cx = x0 + (i + 0.5) * bw
        o.append(_rect(cx - 11, yb + 7, 22, sh - 14,
                       fill="#3f3f3f" if not cbd else BUCKET, sw=0.8))
        if cbd:
            _spring(o, x0 + i * bw + 3, cx - 12, yb + sh / 2.0, turns=3, amp=4, color=BLUE)
            _dashpot(o, cx + 12, x0 + (i + 1) * bw - 3, yb + sh / 2.0, color=RED)
    return bw, sh, yb, yt


# ------------------------------------------------------------------- fig 1
@_reg
def fig_f01():
    o = [_defs()]
    o.append(T(340, 14, "Simplified model of a coal-fired power plant building",
               9.0, color=INK, weight="600"))

    o.append(T(175, 30, "(a) Traditional plant", 7.8, color=INK))
    _plant(o, 55, 295, 50, 220, cbd=False)
    o.append(T(175, 68, "Coal buckets", 7.2, color=INK))
    o.append(_line(175, 72, 175, 140, sw=0.8, color=GREY, dash="3 2"))
    o.append(_rect(48, 93, 254, 87, fill="none", sw=1.0,
                   stroke=RED, dash="5 3"))

    o.append(T(500, 30, "(b) Power plant with CBDs", 7.8, color=INK))
    _plant(o, 385, 625, 50, 220, cbd=True)
    o.append(T(500, 68, "CBDs", 7.2, color=INK))
    o.append(_line(500, 72, 500, 140, sw=0.8, color=GREY, dash="3 2"))
    o.append(_rect(378, 93, 254, 87, fill="none", sw=1.0,
                   stroke=RED, dash="5 3"))
    o.append(T(437, 132, "k", 6.8, color=BLUE))
    o.append(T(465, 132, "c", 6.8, color=RED))

    o.append(T(175, 250, "Bucket mass fixed to the storey", 6.8, color=GREY))
    o.append(T(500, 250, "Bucket coupled by springs and dampers", 6.8, color=GREY))
    return _mk(1, o, "Simplified coal-fired power plant model",
               "Mô hình đơn giản của nhà máy điện than",
               "Simplified coal-fired power plant model",
               "Tòa nhà bốn tầng, ba nhịp; (a) phễu than cố định, (b) ba CBD được nối bằng lò xo và bộ giảm chấn.",
               "Four-storey, three-bay frame: (a) fixed coal buckets, (b) three CBDs coupled by springs and dampers.")


# ------------------------------------------------------------------- fig 2
@_reg
def fig_f02():
    o = [_defs()]
    o.append(T(340, 14, "Shaking-table test model and structure dimensions",
               9.0, color=INK, weight="600"))

    # (a) reduced-scale frame on the shaking table
    o.append(T(170, 30, "(a) 1:30 shaking-table model", 7.8, color=INK))
    x0, x1, ytop, ybase = 50, 290, 52, 212
    bw, sh = (x1 - x0) / 3.0, (ybase - ytop) / 4.0
    for i in range(4):
        xx = x0 + i * bw
        o.append(_line(xx, ytop, xx, ybase, sw=1.6))
    for j in range(5):
        yy = ytop + j * sh
        o.append(_line(x0, yy, x1, yy, sw=1.1))
    for i, lab in enumerate(("CBD3", "CBD2", "CBD1")):
        cx = x0 + (i + 0.5) * bw
        o.append(_rect(cx - 21, ytop + 2 * sh + 8, 42, sh - 16,
                       fill="#5d6d7e", sw=0.8))
        o.append(T(cx, ytop + 2 * sh + sh / 2.0 + 2, lab, 6.0, color="#ffffff"))
    o.append(_rect(x0 - 12, ybase, (x1 - x0) + 24, 11, fill="#bdc3c7", sw=1.0))
    _ground(o, x0 - 18, x1 + 18, ybase + 11)
    o.append(_ar(78, 239, 262, 239, color=BLUE, sw=1.2))
    o.append(_ar(262, 239, 78, 239, color=BLUE, sw=1.2))
    o.append(T(170, 257, "horizontal excitation", 6.8, color=GREY))

    # (b) dimensioned four-bay elevation with CBD1-3
    o.append(T(495, 30, "(b) Dimensioned structure", 7.8, color=INK))
    bx = [370, 410, 450, 490, 530]
    by = [62, 97, 132, 167, 202]
    o.append(_line(490, 44, 530, 44, sw=1.2))
    for xx in (490, 530):
        o.append(_line(xx, 44, xx, 202, sw=1.5))
    for i in range(4):
        o.append(_line(bx[i], by[0], bx[i], by[-1], sw=1.5))
    o.append(_line(530, by[0], 530, by[-1], sw=1.5))
    for yy in by:
        o.append(_line(bx[0], yy, bx[4], yy, sw=1.1))
    for i, lab in enumerate(("CBD3", "CBD2", "CBD1")):
        cx = (bx[i] + bx[i + 1]) / 2.0
        o.append(_rect(cx - 17, by[2] + 6, 34, by[3] - by[2] - 12,
                       fill="#5d6d7e", sw=0.8))
        o.append(T(cx, by[2] + (by[3] - by[2]) / 2.0 + 2, lab, 6.0,
                   color="#ffffff"))
    _ground(o, bx[0] - 10, bx[4] + 10, by[-1])
    for i in range(4):
        mx = (bx[i] + bx[i + 1]) / 2.0
        o.append(T(mx, 214, "700", 6.2, color=GREY))
        o.append(_line(bx[i], 204, bx[i], 209, sw=0.7, color=GREY))
        o.append(_line(bx[i + 1], 204, bx[i + 1], 209, sw=0.7, color=GREY))
    for j in range(4):
        o.append(T(540, (by[j] + by[j + 1]) / 2.0 + 2, "600", 6.2,
                   color=GREY, anchor="start"))
    o.append(T(495, 232, "dimensions in mm", 6.6, color=GREY))
    return _mk(2, o, "Shaking-table test model and dimensions",
               "Mô hình thử nghiệm bàn rung và kích thước",
               "Shaking-table test model and dimensions",
               "(a) Mô hình bê tông bốn tầng tỉ lệ 1:30 trên bàn rung. (b) Mặt đứng có kích thước: nhịp 700 mm, tầng 600 mm; CBD1–CBD3 ở tầng ba.",
               "(a) 1:30 four-storey reinforced-concrete model on the shaking table. (b) Dimensioned elevation: 700 mm bays, 600 mm storeys, CBD1-CBD3 at the third storey.")


# ------------------------------------------------------------------- fig 3
@_reg
def fig_f03():
    o = [_defs()]
    o.append(T(340, 14, "Main vibration control mode of the structure",
               9.0, color=INK, weight="600"))
    fr, mx, my = _frame(120, 52, 420, 168, (0.0, 1.2), (0.0, 4.0),
                        [(0.0, "0"), (0.2, "0.2"), (0.4, "0.4"), (0.6, "0.6"),
                         (0.8, "0.8"), (1.0, "1.0"), (1.2, "1.2")],
                        [(0, "0"), (1, "1"), (2, "2"), (3, "3"), (4, "4")],
                        "Displacement", "Story")
    o.append(fr)
    pts = [(0.0, 0.0), (0.1, 1.0), (0.30, 2.0), (0.45, 3.0), (1.0, 4.0)]
    o.append(_series(pts, mx, my, BLUE, dot=0))
    for px, py in pts:
        _tri(o, mx(px), my(py), 3.4, BLUE)
    o.append(T(250, 96, "CBD layer (3rd storey)", 6.8, color=GREY))
    o.append(_line(250, 100, mx(0.45), my(3.0), sw=0.8, color=GREY, dash="3 2"))
    for i, lab in enumerate(("η₁ = 1523", "ξ₁ = 0.05", "M₁ = 1000 kg",
                             "K₁ = 411.5 kN/m", "ω₁ = 20.29 rad/s",
                             "T₁ = 0.31 s")):
        o.append(T(370, 72 + i * 16, lab, 7.2, color=INK, anchor="start"))
    return _mk(3, o, "Main vibration control mode",
               "Chế độ dao động kiểm soát chính",
               "Main vibration control mode",
               "Dạng dao động thuần nhất thứ nhất; độ dịch chuyển lớn nhất tại tầng ba là vị trí lắp ba CBD.",
               "First-mode deformation; the largest displacement occurs at the third storey, where the three CBDs are installed.")


# ------------------------------------------------------------------- fig 4
def _tf0(f):
    r = f / 19.2 - 19.2 / f if f > 0 else -99.0
    return 0.0032 + 0.0340 / math.sqrt(1.0 + (7.5 * r) ** 2)


def _tf1(f):
    base = _tf0(f)
    env = math.exp(-((f - 19.6) / 2.9) ** 6)
    twin = (0.0128 + 0.0044 * math.exp(-((f - 17.4) / 1.2) ** 2)
            + 0.0038 * math.exp(-((f - 21.4) / 1.2) ** 2))
    return base * (1.0 - env) + twin * env


@_reg
def fig_f04():
    o = [_defs()]
    o.append(T(340, 14, "Transfer function with and without optimal CBDs",
               9.0, color=INK, weight="600"))
    fr, mx, my = _frame(80, 50, 440, 165, (0.0, 40.0), (0.0, 0.04),
                        [(0, "0"), (5, "5"), (10, "10"), (15, "15"),
                         (20, "20"), (25, "25"), (30, "30"), (35, "35"),
                         (40, "40")],
                        [(0.0, "0"), (0.01, "0.01"), (0.02, "0.02"),
                         (0.03, "0.03"), (0.04, "0.04")],
                        "Frequency (Hz)", "")
    o.append(fr)
    o.append(T(96, 46, "Amplitude", 6.6, color=INK, anchor="start"))
    o.append(_rect(mx(17.715), 50, mx(22.065) - mx(17.715), 165,
                   fill="#e8e8e8", sw=0))
    fs = [0.5 + i * 0.25 for i in range(158)]
    o.append(_series([(f, _tf0(f)) for f in fs], mx, my, GREY, dot=0, dash="4 3"))
    o.append(_series([(f, _tf1(f)) for f in fs], mx, my, BLUE, dot=0))
    for f, lab, dx in ((16.5, "P", -9), (23.4, "Q", 4)):
        px, py = mx(f), my(_tf0(f))
        o.append(_circle(px, py, 2.6, fill=RED, sw=0))
        o.append(T(px + dx, py - 9, lab, 7.4, color=RED))
    o.append(T(mx(19.9), 62, "Operating range", 6.6, color=GREY))
    o.append(_legend([(GREY, "Without CBDs"), (BLUE, "With CBDs")], 468, 66,
                     w=98, size=7.0))
    return _mk(4, o, "Transfer function with and without optimal CBDs",
               "Hàm truyền khi có và không có CBD tối ưu",
               "Transfer function with and without optimal CBDs",
               "Đường đứt nét (không CBD) có đỉnh cộng hưởng cao; đường liền (có CBD tối ưu) có hai đỉnh thấp hơn, cắt nhau tại P và Q trong dải 17,715–22,065 Hz.",
               "Dashed curve (no CBDs) keeps a high resonance peak; the solid curve (optimal CBDs) splits into two lower peaks, crossing at P and Q inside the 17.715-22.065 Hz band.")


# ------------------------------------------------------------------- fig 5
_SURF_COLORS = ["#1f5f8b", "#2a6fa8", "#3b82b8", "#5b9bc4", "#8fb6cc",
                "#c4cbd0", "#d9a86a", "#d98416", "#b03a2e"]


def _surf_pt(u, v):
    z = min(1.0, 0.52 + 0.42 * ((u - 0.12) / 0.22) ** 2
            + 0.18 * ((v - 0.05) / 0.15) ** 2)
    return (50 + (u + 0.1) * 360 + v * 120,
            190 - (z - 0.5) * 200 - (u + 0.1) * 35 - v * 60)


@_reg
def fig_f05():
    o = [_defs()]
    o.append(T(340, 14, "Objective function versus frequency deviation and damping ratio",
               9.0, color=INK, weight="600"))

    # (a) three-dimensional surface, drawn as a projected wireframe mesh
    o.append(T(130, 32, "βopt = 0.2", 6.6, color=INK))
    o.append(T(130, 44, "Δopt = 0.12", 6.6, color=INK))
    o.append(T(130, 56, "ξdopt = 0.05", 6.6, color=INK))
    for k in range(9):
        v = 0.025 * k
        pts = [_surf_pt(-0.1 + 0.4 * i / 12.0, v) for i in range(13)]
        o.append(_poly(pts, sw=1.0, color=_SURF_COLORS[k]))
    for i in range(13):
        u = -0.1 + 0.4 * i / 12.0
        pts = [_surf_pt(u, 0.025 * k) for k in range(9)]
        o.append(_poly(pts, sw=0.6, color="#4a4a4a"))
    o.append(_line(45, 205, 200, 205, sw=1.0))
    o.append(_ar(45, 205, 45, 62, color=INK, sw=1.0))
    for u, lab in ((-0.1, "−0.1"), (0.0, "0"), (0.1, "0.1"),
                   (0.2, "0.2"), (0.3, "0.3")):
        o.append(T(50 + (u + 0.1) * 360, 214, lab, 6.0, color=GREY))
    o.append(T(122, 228, "Δ", 7.2, color=INK))
    o.append(T(38, 58, "F", 7.2, color=INK))
    o.append(T(39, 186, "0.6", 6.0, color=GREY, anchor="end"))
    o.append(T(39, 102, "1.0", 6.0, color=GREY, anchor="end"))
    o.append(T(221, 195, "ξd", 7.2, color=INK))
    o.append(T(216, 180, "0.2", 6.0, color=GREY))
    o.append(T(203, 208, "0", 6.0, color=GREY))
    o.append(T(128, 246, "(a) Surface F(Δ, ξd)", 7.4, color=INK))

    # (b) sections at fixed Delta
    fr, mx, my = _frame(268, 50, 178, 150, (0.0, 0.2), (0.5, 1.0),
                        [(0.0, "0"), (0.05, "0.05"), (0.1, "0.1"),
                         (0.15, "0.15"), (0.2, "0.2")],
                        [(0.5, "0.5"), (0.6, "0.6"), (0.7, "0.7"),
                         (0.8, "0.8"), (0.9, "0.9"), (1.0, "1")],
                        "ξd", "F value")
    o.append(fr)
    secs = [
        (0.83, 0.30, 0.78, BLUE, "", "Δ = −0.1", 297, 66),
        (0.66, 0.16, 0.70, GREEN, "", "Δ = 0", 303, 132),
        (0.74, 0.16, 0.66, "#d98416", "", "Δ = 0.2", 348, 152),
        (0.67, 0.14, 0.64, GREY, "4 3", "Δopt = 0.12", 362, 184),
    ]
    for a, b, c, col, dash, lab, tx, ty in secs:
        pts = []
        for i in range(41):
            x = 0.2 * i / 40.0
            y = min(1.0, max(0.5, a - b * math.exp(-((x - 0.05) / c) ** 2)
                             + 0.30 * x * x))
            pts.append((x, y))
        o.append(_series(pts, mx, my, col, dot=0, dash=dash))
        o.append(T(tx, ty, lab, 6.2, color=col))
    o.append(T(398, 62, "β = βopt = 0.2", 6.4, color=INK))
    o.append(T(356, 246, "(b) Sections versus ξd", 7.4, color=INK))

    # (c) sections at fixed damping ratio
    fr, mx, my = _frame(502, 50, 150, 150, (-0.1, 0.3), (0.5, 1.0),
                        [(-0.1, "−0.1"), (0.0, "0"), (0.1, "0.1"),
                         (0.2, "0.2"), (0.3, "0.3")],
                        [(0.5, "0.5"), (0.6, "0.6"), (0.7, "0.7"),
                         (0.8, "0.8"), (0.9, "0.9"), (1.0, "1")],
                        "Δ", "F value")
    o.append(fr)
    secs = [
        (0.66, 0.34, 0.13, BLUE, "", "ξd = 0.01", 540, 72),
        (0.58, 0.30, 0.13, GREEN, "", "ξd = 0.02", 544, 102),
        (0.53, 0.27, 0.13, "#d98416", "", "ξd = 0.1", 558, 132),
        (0.52, 0.26, 0.13, GREY, "4 3", "ξdopt = 0.05", 568, 174),
    ]
    for base, amp, cen, col, dash, lab, tx, ty in secs:
        pts = []
        for i in range(41):
            x = -0.1 + 0.4 * i / 40.0
            y = min(1.0, max(0.5, base + amp * ((x - cen) / 0.30) ** 2))
            pts.append((x, y))
        o.append(_series(pts, mx, my, col, dot=0, dash=dash))
        o.append(T(tx, ty, lab, 6.2, color=col))
    o.append(T(585, 62, "β = βopt = 0.2", 6.4, color=INK))
    o.append(T(576, 246, "(c) Sections versus Δ", 7.4, color=INK))
    return _mk(5, o, "Objective function at optimal coverage",
               "Hàm mục tiêu ở tỉ lệ phủ tối ưu",
               "Objective function at optimal coverage",
               "(a) Mặt hàm mục tiêu theo Δ và ξd. (b) Cắt theo ξd ứng với các Δ. (c) Cắt theo Δ ứng với các ξd; βopt = 0,2, Δopt = 0,12, ξdopt = 0,05.",
               "(a) Objective surface over Delta and xi_d. (b) Sections versus xi_d for several Delta. (c) Sections versus Delta for several xi_d; beta_opt = 0.2, Delta_opt = 0.12, xi_dopt = 0.05.")


# ------------------------------------------------------------------- fig 6
@_reg
def fig_f06():
    o = [_defs()]
    o.append(T(340, 14, "Schematic diagram of a coal bucket damper",
               9.0, color=INK, weight="600"))
    # four supporting columns
    for cx in (205, 260, 385, 440):
        o.append(_rect(cx - 6, 78, 12, 152, fill=STEEL, sw=0.8))
    # upper red beams and coal-bucket beam
    o.append(_poly([(199, 78), (259, 64), (446, 64), (386, 78)],
                   fill="#c0392b", sw=0.9, color=INK, close=True))
    o.append(_poly([(199, 88), (259, 74), (446, 74), (386, 88)],
                   fill="#922b21", sw=0.9, color=INK, close=True))
    o.append(_poly([(304, 70), (322, 70), (356, 108), (338, 108)],
                   fill="#e74c3c", sw=0.8, color=INK, close=True))
    # hanger rods
    for x1, x2 in ((232, 262), (262, 290), (350, 380), (380, 408)):
        o.append(_line(x1, 86, x2, 130, sw=3.0, color=ROD))
    # green coal bucket
    o.append(_poly([(268, 130), (400, 130), (382, 190), (286, 190)],
                   fill=BUCKET, sw=1.0, color=INK, close=True))
    o.append(_poly([(268, 130), (286, 122), (414, 122), (400, 130)],
                   fill="#27ae60", sw=0.9, color=INK, close=True))
    # elastic elements and dampers at the bucket base
    for cx in (292, 376):
        _spring(o, cx - 14, cx + 14, 200, turns=3, amp=5, color=ELAST)
    o.append(_rect(316, 194, 36, 12, fill="#f5b041", sw=0.9))
    o.append(_line(324, 194, 324, 206, sw=0.9, color=RED))
    o.append(_line(344, 194, 344, 206, sw=0.9, color=RED))
    # connectors at the column feet
    for cx in (260, 385):
        o.append(_rect(cx - 14, 216, 28, 10, fill="#2980b9", sw=0.8))
    # leaders and labels
    for tx, ty, lx, ly, lab in (
            (110, 62, 210, 76, "Beam"),
            (330, 48, 330, 68, "Coal-bucket beam"),
            (505, 86, 420, 96, "Hanger rod"),
            (505, 132, 396, 140, "Coal bucket"),
            (505, 167, 392, 172, "Damper"),
            (505, 202, 392, 200, "Elastic element"),
            (130, 226, 250, 221, "Connector"),
            (130, 256, 205, 228, "Column")):
        o.append(T(tx, ty, lab, 7.0, color=INK))
        o.append(_line(tx + (26 if tx < 300 else -26), ty - 2, lx, ly,
                       sw=0.7, color=GREY))
    return _mk(6, o, "Coal bucket damper schematic",
               "Sơ đồ bộ giảm chấn phễu than",
               "Coal bucket damper schematic",
               "CBD gồm thanh treo, phễu thép, dầm đàn hồi, bộ giảm chấn và đầu nối; thanh treo vừa chịu tải vừa tạo độ cứng dao động.",
               "A CBD comprises hanger rods, a steel bucket, an elastic beam, dampers and connectors; the rods carry weight and supply swinging stiffness.")


# ------------------------------------------------------------------- fig 7
@_reg
def fig_f07():
    o = [_defs()]
    o.append(T(340, 14, "Coal bucket dampers in the shaking-table test model",
               9.0, color=INK, weight="600"))

    # (a) simplified mechanical model
    o.append(T(120, 32, "(a) Simplified mechanical model", 7.4, color=INK))
    o.append(_line(32, 60, 128, 60, sw=1.2))
    for x in range(34, 128, 8):
        o.append(_line(x, 60, x + 6, 54, sw=0.6, color=GREY))
    o.append(_circle(80, 60, 2.0, fill=INK, sw=0))
    o.append(_line(80, 60, 80, 172, sw=1.2))
    o.append(_line(80, 60, 106, 168, sw=0.9, color=GREY, dash="4 3"))
    o.append(_path("M88 68 Q84 63 80 60", sw=0.8, color=INK))
    o.append(T(91, 75, "θ", 7.4, color=INK))
    o.append(_circle(74, 178, 10, fill="#2a2a2a", sw=0))
    o.append(_circle(94, 178, 10, fill="#2a2a2a", sw=0))
    o.append(T(84, 204, "m", 7.4, color=INK))
    o.append(_line(45, 60, 45, 178, sw=0.8, color=GREY))
    o.append(_line(41, 60, 49, 60, sw=0.8, color=GREY))
    o.append(_line(41, 178, 49, 178, sw=0.8, color=GREY))
    o.append(T(38, 122, "h", 7.4, color=INK, anchor="end"))
    # simply supported elastic beam
    o.append(_line(178, 104, 178, 210, sw=2.0, color=STEEL))
    o.append(_poly([(170, 96), (186, 96), (178, 104)], fill="#ffffff",
                   sw=0.9, color=INK, close=True))
    o.append(_circle(178, 212, 4, fill="#ffffff", sw=0.9))
    o.append(_path("M178 104 Q170 156 178 210", sw=0.9,
                   color=GREY, dash="4 3"))
    o.append(T(154, 158, "E, I", 7.0, color=INK))
    o.append(_line(198, 104, 198, 210, sw=0.8, color=GREY))
    o.append(_line(194, 104, 202, 104, sw=0.8, color=GREY))
    o.append(_line(194, 210, 202, 210, sw=0.8, color=GREY))
    o.append(T(207, 160, "l", 7.4, color=INK))
    o.append(T(120, 248, "(a) Pendulum and beam model", 7.0, color=INK))

    # (b) detailed construction
    o.append(T(354, 32, "(b) Detailed structure", 7.4, color=INK))
    o.append(_rect(258, 96, 14, 132, fill=STEEL, sw=0.8))
    o.append(_rect(438, 96, 14, 132, fill=STEEL, sw=0.8))
    o.append(_rect(272, 96, 166, 8, fill="#c0392b", sw=0.8))
    o.append(_line(300, 104, 300, 142, sw=2.6, color=ROD))
    o.append(_line(410, 104, 410, 142, sw=2.6, color=ROD))
    o.append(_rect(300, 142, 110, 52, fill="#5d6d7e", sw=1.0))
    o.append(_rect(276, 202, 158, 12, fill="#aab7b8", sw=0.9))
    o.append(_rect(272, 196, 26, 8, fill="#2980b9", sw=0.8))
    o.append(_rect(412, 196, 26, 8, fill="#2980b9", sw=0.8))
    # inset connector plate with hole types
    o.append(_rect(250, 48, 82, 38, fill="#ffffff", sw=0.9))
    o.append(_rect(258, 70, 66, 8, fill="#7f8c8d", sw=0.6))
    o.append(_circle(268, 74, 2.4, fill="none", sw=0.8))
    o.append(_circle(278, 74, 2.4, fill="none", sw=0.8))
    o.append(_rect(290, 72, 12, 4, fill="none", sw=0.8))
    o.append(_rect(306, 72, 12, 4, fill="none", sw=0.8))
    o.append(T(292, 61, "Fixed / slotted holes", 6.2, color=INK))
    o.append(T(292, 95, "Connector detail", 6.2, color=GREY))
    for tx, ty, lab in (
            (470, 118, "Hanger rod"),
            (470, 152, "Coal bucket"),
            (470, 186, "Steel plate"),
            (300, 228, "Riveting"),
            (420, 228, "Hinged")):
        o.append(T(tx, ty, lab, 6.6, color=INK))
    o.append(_line(464, 116, 412, 122, sw=0.7, color=GREY))
    o.append(_line(464, 150, 408, 168, sw=0.7, color=GREY))
    o.append(_line(464, 184, 430, 206, sw=0.7, color=GREY))
    o.append(T(354, 248, "(b) Bucket and connectors", 7.0, color=INK))

    # (c) layout in the test model
    o.append(T(568, 32, "(c) Layout in test model", 7.4, color=INK))
    gx = [492, 526, 560, 594, 628]
    gy = [62, 97, 132, 167, 202]
    for xx in gx:
        o.append(_line(xx, gy[0], xx, gy[-1], sw=1.2))
    for yy in gy:
        o.append(_line(gx[0], yy, gx[-1], yy, sw=1.0))
    for i, lab in enumerate(("CBD3", "CBD2", "CBD1")):
        cx = (gx[i] + gx[i + 1]) / 2.0
        o.append(_rect(cx - 14, gy[2] + 5, 28, gy[3] - gy[2] - 10,
                       fill="#5d6d7e", sw=0.8))
        o.append(T(cx, gy[2] + (gy[3] - gy[2]) / 2.0 + 2, lab, 5.8,
                   color="#ffffff"))
    o.append(_line(gx[0], gy[2] - 6, gx[3], gy[2] - 6, sw=0.8,
                   color=RED, dash="3 2"))
    o.append(T(560, 115, "CBD storey", 6.4, color=RED))
    _ground(o, gx[0] - 8, gx[-1] + 8, gy[-1])
    o.append(T(568, 248, "(c) Three CBDs at third storey", 7.0, color=INK))
    return _mk(7, o, "Coal bucket dampers in the test model",
               "Các bộ giảm chấn phễu than trong mô hình thử nghiệm",
               "Coal bucket dampers in the test model",
               "(a) Mô hình con lắc và dầm đàn hồi. (b) Cấu tạo phễu, thanh treo, tấm thép và đầu nối. (c) Bố trí CBD1–CBD3 tại tầng ba của mô hình.",
               "(a) Pendulum and elastic-beam model. (b) Bucket, hanger rods, steel plate and connectors. (c) CBD1-CBD3 installed at the third storey of the test frame.")
