# -*- coding: utf-8 -*-
"""Vector figures 5.7-5.12 for PPIC chapter 5 (thorium/uranium block HTRs).

Each figure is a simplified vector redraw of the printed figure on PDF pages
108-111: k_eff curves for five compact configurations at 46% and 91% thorium,
channel-level compact rings, block-level triangular core layouts, initial
effective U-235 enrichment and initial heavy-metal inventory versus thorium
content. Data points, axis ranges and legend labels are taken from the printed
plots.
"""
import math

from ppicfig5_common import (BLUE, GREEN, GREY, INK, RED, H, W, T, _ar, _b,
                             _circle, _defs, _ellipse, _fig, _frame, _legend,
                             _line, _path, _poly, _rect, _mk, _series,
                             _tri_membership, make_registry)

FIGS, _reg = make_registry()

ORANGE = "#d98416"
PURPLE = "#7b3fa1"
REFLECTOR = "#8a8a8a"

SBU_COLORS = ("#111111", RED, BLUE, PURPLE, GREEN)
SBU_LABELS = ("SBU-1#", "SBU-2#", "SBU-3#", "SBU-4#", "SBU-5#")
SEP_COLORS = (RED, BLUE, GREEN, ORANGE)
SEP_LABELS = ("Th/U MOX", "SBT", "SBU", "WASB")


def _hexp(cx, cy, r, fill, sw=0.5, color="#777777"):
    """Point-top hexagon, used for triangular block layouts."""
    pts = [(cx + r * math.cos(math.radians(30 + 60 * k)),
            cy + r * math.sin(math.radians(30 + 60 * k))) for k in range(6)]
    return _poly(pts, fill=fill, sw=sw, color=color, close=True)


def _hexf(cx, cy, r, fill, sw=0.8, color=INK):
    """Flat-top hexagon outline used as a compact-lattice boundary."""
    pts = [(cx + r * math.cos(math.radians(60 * k)),
            cy + r * math.sin(math.radians(60 * k))) for k in range(6)]
    return _poly(pts, fill=fill, sw=sw, color=color, close=True)


def _compact_field(cx, cy, n, s, rad, colour_fn):
    """Honeycomb of small circular compacts in axial coordinates."""
    o = []
    for q in range(-n, n + 1):
        for r in range(-n, n + 1):
            hd = max(abs(q), abs(r), abs(q + r))
            if hd > n:
                continue
            px = cx + s * (q + 0.5 * r)
            py = cy + s * 0.866 * r
            col = REFLECTOR if hd <= 1 else colour_fn(hd, q, r)
            o.append(_circle(px, py, rad, fill=col, sw=0.25, color="#666666"))
    return "".join(o)


def _tri_field(cx, cy, rows, rad, colour_fn):
    """Triangular one-sixth core sector of hexagonal fuel blocks."""
    dx, dy = math.sqrt(3) * rad, 1.5 * rad
    o = []
    for i in range(rows):
        for j in range(i + 1):
            px = cx + (j - i / 2.0) * dx
            py = cy + i * dy
            o.append(_hexp(px, py, rad, colour_fn(i, j), sw=0.45))
    return "".join(o)


KEFF_XT = [(v, str(v)) for v in range(0, 701, 100)]
SBU_LEGEND = [(c, l) for c, l in zip(SBU_COLORS, SBU_LABELS)]


@_reg
def fig_f07():
    """Figure 5.7 - k_eff of five configurations at 46% thorium."""
    o = [_defs()]
    o.append(T(340, 14, "Effective multiplication factor at 46% thorium",
               8.8, color=INK, weight="600"))

    left = [
        [(0, 1.302), (10, 1.270), (40, 1.260), (80, 1.248), (150, 1.234),
         (250, 1.217), (350, 1.199), (450, 1.180), (550, 1.158),
         (650, 1.138), (680, 1.130)],
        [(0, 1.307), (10, 1.271), (40, 1.264), (80, 1.250), (150, 1.238),
         (250, 1.222), (350, 1.205), (450, 1.188), (550, 1.166),
         (650, 1.147), (680, 1.138)],
        [(0, 1.303), (10, 1.268), (40, 1.261), (80, 1.246), (150, 1.232),
         (250, 1.215), (350, 1.197), (450, 1.178), (550, 1.155),
         (650, 1.135), (680, 1.127)],
        [(0, 1.304), (10, 1.269), (40, 1.262), (80, 1.247), (150, 1.233),
         (250, 1.216), (350, 1.198), (450, 1.179), (550, 1.156),
         (650, 1.136), (680, 1.128)],
        [(0, 1.301), (10, 1.267), (40, 1.258), (80, 1.244), (150, 1.230),
         (250, 1.213), (350, 1.195), (450, 1.176), (550, 1.153),
         (650, 1.132), (680, 1.124)],
    ]
    right = [
        [(0, 1.510), (10, 1.508), (40, 1.505), (80, 1.500), (150, 1.494),
         (250, 1.486), (350, 1.477), (450, 1.467), (550, 1.458),
         (650, 1.450), (680, 1.448)],
        [(0, 1.522), (10, 1.518), (40, 1.512), (80, 1.508), (150, 1.502),
         (250, 1.494), (350, 1.485), (450, 1.475), (550, 1.466),
         (650, 1.458), (680, 1.456)],
        [(0, 1.525), (10, 1.520), (40, 1.515), (80, 1.510), (150, 1.505),
         (250, 1.497), (350, 1.488), (450, 1.479), (550, 1.470),
         (650, 1.462), (680, 1.460)],
        [(0, 1.528), (10, 1.522), (40, 1.517), (80, 1.512), (150, 1.507),
         (250, 1.499), (350, 1.490), (450, 1.481), (550, 1.472),
         (650, 1.464), (680, 1.462)],
        [(0, 1.533), (10, 1.526), (40, 1.521), (80, 1.516), (150, 1.511),
         (250, 1.503), (350, 1.494), (450, 1.485), (550, 1.476),
         (650, 1.468), (680, 1.463)],
    ]

    panels = [
        (60, (1.12, 1.32), [(v, "%.2f" % v) for v in
                            [1.12 + 0.02 * k for k in range(11)]],
         "k_eff", "(a) 20% enriched U-235 in uranium rods", left),
        (380, (1.40, 1.60), [(v, "%.2f" % v) for v in
                             [1.40 + 0.02 * k for k in range(11)]],
         "k_eff", "(b) 80% enriched U-235 in uranium rods", right),
    ]
    for x0, yr, yt, ylab, title, data in panels:
        o.append(T(x0 + 125, 33, title, 6.6, color=INK))
        frame, mx, my = _frame(x0, 48, 250, 185, (-100, 700), yr,
                               KEFF_XT, yt, "t / EFPD", ylab)
        o.append(frame)
        for pts, col in zip(data, SBU_COLORS):
            o.append(_series(pts, mx, my, col, dot=1.5))
        o.append(_legend(SBU_LEGEND, x0 + 152, 56, w=92, lh=11, size=6.6))

    return _mk(7, o, "k_eff of five configurations at 46% thorium",
               "k_eff của năm cấu hình ở 46% thori",
               "k_eff of five configurations at 46% thorium",
               "Biểu đồ hai ô về hệ số nhân hữu hiệu k_eff theo thời gian chiếu xạ t "
               "tính bằng EFPD cho năm cấu hình SBU 1 đến SBU 5 ở 46% thori. Ô trái dùng "
               "urani làm giàu 20% có trục tung từ 1,12 đến 1,32; ô phải dùng urani làm "
               "giàu 80% có trục tung từ 1,40 đến 1,60. Cả hai ô có trục hoành từ 0 đến "
               "700 EFPD, năm đường màu đen, đỏ, xanh dương, tím và xanh lá gần như "
               "trùng nhau, giảm nhanh trong năm mươi ngày đầu rồi giảm dần.",
               "Two panels of effective multiplication factor k_eff versus irradiation "
               "time t in EFPD for five configurations SBU-1 to SBU-5 at 46% thorium. "
               "The left panel with 20% enriched uranium has vertical axis from 1.12 "
               "to 1.32; the right panel with 80% enriched uranium spans 1.40 to 1.60. "
               "Both panels show time from 0 to 700 EFPD with five coloured curves in "
               "black, red, blue, purple and green that nearly coincide, dropping "
               "sharply in the first fifty days and then declining gradually.")


@_reg
def fig_f08():
    """Figure 5.8 - k_eff of five configurations at 91% thorium."""
    o = [_defs()]
    o.append(T(340, 14, "Effective multiplication factor at 91% thorium",
               8.8, color=INK, weight="600"))

    left = [
        [(0, 0.800), (10, 0.770), (30, 0.762), (50, 0.770), (100, 0.800),
         (200, 0.818), (300, 0.828), (400, 0.836), (500, 0.842),
         (600, 0.844), (680, 0.844)],
        [(0, 0.830), (10, 0.790), (30, 0.784), (50, 0.790), (100, 0.802),
         (200, 0.817), (300, 0.828), (400, 0.836), (500, 0.842),
         (600, 0.844), (680, 0.843)],
        [(0, 0.835), (10, 0.795), (30, 0.788), (50, 0.795), (100, 0.806),
         (200, 0.820), (300, 0.830), (400, 0.837), (500, 0.843),
         (600, 0.845), (680, 0.844)],
        [(0, 0.838), (10, 0.797), (30, 0.790), (50, 0.797), (100, 0.808),
         (200, 0.821), (300, 0.831), (400, 0.838), (500, 0.844),
         (600, 0.846), (680, 0.845)],
        [(0, 0.843), (10, 0.800), (30, 0.793), (50, 0.800), (100, 0.810),
         (200, 0.822), (300, 0.832), (400, 0.839), (500, 0.845),
         (600, 0.846), (680, 0.845)],
    ]
    right = [
        [(0, 1.180), (10, 1.145), (30, 1.135), (60, 1.135), (150, 1.125),
         (250, 1.115), (350, 1.103), (450, 1.092), (550, 1.082),
         (650, 1.073), (680, 1.072)],
        [(0, 1.245), (10, 1.205), (30, 1.198), (60, 1.195), (150, 1.180),
         (250, 1.165), (350, 1.150), (450, 1.135), (550, 1.120),
         (650, 1.110), (680, 1.108)],
        [(0, 1.260), (10, 1.215), (30, 1.210), (60, 1.208), (150, 1.195),
         (250, 1.182), (350, 1.170), (450, 1.155), (550, 1.140),
         (650, 1.128), (680, 1.125)],
        [(0, 1.265), (10, 1.220), (30, 1.215), (60, 1.212), (150, 1.200),
         (250, 1.188), (350, 1.175), (450, 1.162), (550, 1.148),
         (650, 1.135), (680, 1.132)],
        [(0, 1.268), (10, 1.225), (30, 1.220), (60, 1.218), (150, 1.207),
         (250, 1.195), (350, 1.183), (450, 1.170), (550, 1.155),
         (650, 1.142), (680, 1.138)],
    ]

    panels = [
        (60, (0.74, 0.94), [(v, "%.2f" % v) for v in
                            [0.74 + 0.02 * k for k in range(11)]],
         "k_eff", "(a) 20% enriched U-235 in uranium rods", left),
        (380, (1.06, 1.28), [(v, "%.2f" % v) for v in
                             [1.06 + 0.02 * k for k in range(12)]],
         "k_eff", "(b) 80% enriched U-235 in uranium rods", right),
    ]
    for x0, yr, yt, ylab, title, data in panels:
        o.append(T(x0 + 125, 33, title, 6.6, color=INK))
        frame, mx, my = _frame(x0, 48, 250, 185, (-100, 700), yr,
                               KEFF_XT, yt, "t / EFPD", ylab)
        o.append(frame)
        for pts, col in zip(data, SBU_COLORS):
            o.append(_series(pts, mx, my, col, dot=1.5))
        o.append(_legend(SBU_LEGEND, x0 + 152, 56, w=92, lh=11, size=6.6))

    return _mk(8, o, "k_eff of five configurations at 91% thorium",
               "k_eff của năm cấu hình ở 91% thori",
               "k_eff of five configurations at 91% thorium",
               "Biểu đồ hai ô về k_eff theo thời gian t tính bằng EFPD cho năm cấu hình "
               "SBU 1 đến SBU 5 ở 91% thori. Ô trái dùng urani làm giàu 20% có trục tung "
               "từ 0,74 đến 0,94; ô phải dùng urani làm giàu 80% có trục tung từ 1,06 "
               "đến 1,28. Trục hoành từ 0 đến 700 EFPD. Ở ô trái các đường giảm mạnh rồi "
               "tăng nhẹ và hội tụ gần 0,84; ở ô phải đường đen SBU 1 luôn thấp hơn bốn "
               "đường còn lại.",
               "Two panels of k_eff versus time in EFPD for five configurations SBU-1 "
               "to SBU-5 at 91% thorium. The left panel with 20% enriched uranium has "
               "vertical axis from 0.74 to 0.94; the right panel with 80% enriched "
               "uranium spans 1.06 to 1.28. The time axis runs from 0 to 700 EFPD. In "
               "the left panel the curves drop steeply then rise slightly and converge "
               "near 0.84; in the right panel the black SBU-1 curve stays clearly below "
               "the other four.")


@_reg
def fig_f09():
    """Figure 5.9 - channel-level compact configurations by thorium content."""
    o = [_defs()]
    o.append(T(340, 14, "Channel-level compact configurations",
               8.8, color=INK, weight="600"))

    layouts = [
        (16, 88, 82, lambda hd, q, r: BLUE if q == 0 else RED),
        (32, 256, 82, lambda hd, q, r:
         BLUE if (hd >= 5 or (q == 0 and hd <= 3)) else RED),
        (46, 424, 82, lambda hd, q, r: BLUE if hd >= 4 else RED),
        (60, 592, 82, lambda hd, q, r: BLUE if hd >= 3 else RED),
        (72, 172, 212, lambda hd, q, r: RED if (q + 2 * r) % 7 == 0 else BLUE),
        (81, 340, 212, lambda hd, q, r: RED if (2 * q + 3 * r) % 11 == 0 else BLUE),
        (91, 508, 212, lambda hd, q, r: RED if (3 * q + 5 * r) % 17 == 0 else BLUE),
    ]
    for th, cx, cy, rule in layouts:
        o.append(_hexf(cx, cy, 47, "#dedede", sw=1.0))
        o.append(_compact_field(cx, cy, 5, 8.0, 2.9, rule))
    for k, (th, cx, cy, rule) in enumerate(layouts):
        o.append(T(cx, 138 if k < 4 else 268, "(%s) %d%% thorium" %
                   ("abcdefg"[k], th), 6.4, color=INK))

    o.append(_circle(215, 297, 3.6, fill=RED, sw=0))
    o.append(T(225, 300, "Uranium compact", 6.2, color=INK, anchor="start"))
    o.append(_circle(430, 297, 3.6, fill=BLUE, sw=0))
    o.append(T(440, 300, "Thorium compact", 6.2, color=INK, anchor="start"))

    return _mk(9, o, "Channel-level compact configurations",
               "Cấu hình viên nén theo cấp kênh",
               "Channel-level compact configurations",
               "Bảy lục giác mạng viên nén cho thấy phân bố thori và urani theo cấp "
               "kênh ở các hàm lượng 16, 32, 46, 60, 72, 81 và 91% thori. Vùng giữa xám "
               "là kênh điều khiển; viên nén đỏ là urani, viên nén xanh dương là thori. "
               "Khi tăng hàm lượng thori, vòng đỏ thu hẹp dần và thori xanh chiếm ưu thế.",
               "Seven hexagonal compact lattices show the distribution of thorium and "
               "uranium compacts at channel level for 16, 32, 46, 60, 72, 81 and 91% "
               "thorium. The grey central region marks the control channel; red "
               "compacts are uranium and blue compacts are thorium. As thorium content "
               "rises, the red ring shrinks and blue thorium compacts become dominant.")


@_reg
def fig_f10():
    """Figure 5.10 - block-level triangular core configurations."""
    o = [_defs()]
    o.append(T(340, 14, "Block-level fuel block configurations",
               8.8, color=INK, weight="600"))

    def block_rule(th):
        def colour(i, j):
            if i < 3 or j >= i - 1:
                return REFLECTOR
            score = ((i * 17 + j * 31 + 5) % 100) / 100.0
            return BLUE if score < (th + 6) / 100.0 else RED
        return colour

    layouts = [(20, 118, 42), (31, 340, 42), (43, 562, 42),
               (55, 229, 168), (67, 451, 168)]
    for th, cx, cy in layouts:
        o.append(_tri_field(cx, cy, 9, 6.8, block_rule(th)))
    for k, (th, cx, cy) in enumerate(layouts):
        o.append(T(cx, 143 if k < 3 else 269, "(%s) %d%% thorium" %
                   ("abcde"[k], th), 6.4, color=INK))

    o.append(_hexp(215, 294, 5.4, REFLECTOR, sw=0.5))
    o.append(T(225, 297, "Reflector", 6.2, color=INK, anchor="start"))
    o.append(_hexp(350, 294, 5.4, RED, sw=0.5))
    o.append(T(360, 297, "Uranium block", 6.2, color=INK, anchor="start"))
    o.append(_hexp(505, 294, 5.4, BLUE, sw=0.5))
    o.append(T(515, 297, "Thorium block", 6.2, color=INK, anchor="start"))

    return _mk(10, o, "Block-level fuel block configurations",
               "Cấu hình khối nhiên liệu theo cấp khối",
               "Block-level fuel block configurations",
               "Năm lõi tam giác gồm các khối lục giác cho thấy cấu hình nhiên liệu theo "
               "cấp khối ở 20, 31, 43, 55 và 67% thori. Khối xám là bộ phản xạ; khối đỏ "
               "là urani, khối xanh dương là thori. Số khối thori tăng dần từ trái sang "
               "phải và từ trên xuống dưới.",
               "Five triangular cores of hexagonal blocks show fuel block "
               "configurations at block level for 20, 31, 43, 55 and 67% thorium. Grey "
               "blocks are reflector, red blocks are uranium and blue blocks are "
               "thorium. The number of blue thorium blocks increases steadily across "
               "the five triangles.")


@_reg
def fig_f11():
    """Figure 5.11 - initial effective enrichment versus thorium content."""
    o = [_defs()]
    o.append(T(340, 14, "Initial effective U-235 enrichment vs thorium content",
               8.8, color=INK, weight="600"))

    xt = [(v, str(v)) for v in range(0, 101, 10)]
    yt = [(4.0 + 0.5 * k, "%.1f" % (4.0 + 0.5 * k)) for k in range(7)]
    frame, mx, my = _frame(70, 42, 470, 205, (-10, 100), (4.0, 7.0), xt, yt,
                           "Thorium content/%", "Effective U-235 enrichment / %")
    o.append(frame)

    data = [
        [(2, 5.37), (10, 5.68), (20, 5.98), (30, 6.10), (40, 5.98),
         (50, 5.98), (60, 5.78), (70, 5.48), (80, 5.08), (90, 4.68)],
        [(10, 5.48), (20, 5.58), (30, 5.48), (40, 5.38), (50, 5.28),
         (60, 5.18), (70, 4.98), (80, 4.78), (90, 4.68)],
        [(17, 5.19), (32, 4.98), (43, 4.90), (56, 4.81), (70, 4.68),
         (80, 4.68), (90, 4.78)],
        [(19, 5.08), (30, 4.87), (43, 4.88), (56, 4.78), (68, 4.77),
         (90, 4.68)],
    ]
    for pts, col in zip(data, SEP_COLORS):
        o.append(_series(pts, mx, my, col, dot=2.0))
    o.append(_legend([(c, l) for c, l in zip(SEP_COLORS, SEP_LABELS)],
                     440, 50, w=100, lh=13, size=7.0))

    return _mk(11, o, "Initial effective U-235 enrichment vs thorium content",
               "Độ giàu hiệu dụng ban đầu của U-235 theo hàm lượng thori",
               "Initial effective U-235 enrichment vs thorium content",
               "Đồ thị độ giàu hiệu dụng ban đầu của U-235 theo hàm lượng thori với bốn "
               "chuỗi có nhãn: Th/U MOX màu đỏ, SBT màu xanh dương, SBU màu xanh lá và "
               "WASB màu cam. Trục hoành từ 0 đến 100% thori, trục tung từ 4,0 đến 7,0%. "
               "Chuỗi MOX tăng đến khoảng 6,1% ở 30% thori rồi giảm; ba chuỗi còn lại "
               "giảm dần và gần như hội tụ gần 4,7% ở 90% thori.",
               "Plot of initial effective U-235 enrichment versus thorium content with "
               "four labelled series: Th/U MOX in red, SBT in blue, SBU in green and "
               "WASB in orange. The horizontal axis runs from 0 to 100% thorium and the "
               "vertical axis from 4.0 to 7.0%. The MOX series rises to about 6.1% at "
               "30% thorium then falls; the other three series decline and nearly "
               "converge near 4.7% at 90% thorium.")


@_reg
def fig_f12():
    """Figure 5.12 - initial heavy-metal inventory versus thorium content."""
    o = [_defs()]
    o.append(T(340, 14, "Initial inventories vs thorium content",
               8.8, color=INK, weight="600"))

    x0, y0, w, h = 70, 42, 450, 205
    xt = [(v, str(v)) for v in range(0, 101, 10)]
    yt = [(5000 * k, str(5000 * k)) for k in range(6)]
    frame, mx, my = _frame(x0, y0, w, h, (-10, 100), (0, 25000), xt, yt,
                           "Thorium content/%", "Enriched uranium / kg")
    o.append(frame)

    # Right-hand axis (heavy metal) shares the 0..25000 scale.
    for v, lab in yt:
        py = my(v)
        o.append(_line(x0 + w, py, x0 + w + 3, py, sw=0.7))
        o.append(T(x0 + w + 6, py + 2.3, lab, 6.4, anchor="start", color=RED))
    o.append('<text x="%s" y="%s" transform="rotate(-90 %s %s)" '
             'style="font:7.4px Inter,Helvetica,sans-serif;fill:%s">%s</text>'
             % (x0 + w + 34, y0 + h / 2.0, x0 + w + 34, y0 + h / 2.0,
                RED, "Heavy metal / kg"))

    heavy = [(2, 18000), (10, 17700), (20, 17500), (30, 17300), (40, 17100),
             (50, 16900), (60, 16700), (70, 16500), (80, 16300), (90, 16000)]
    uranium = [(2, 18000), (10, 15600), (20, 13500), (30, 11500), (40, 10000),
               (50, 7800), (60, 6000), (70, 4800), (80, 3200), (90, 1500)]
    offsets = (0.0, -130.0, 110.0, -60.0)
    for col, off in zip(SEP_COLORS, offsets):
        o.append(_series([(a, b + off) for a, b in heavy], mx, my, col, dot=1.6))
        o.append(_series([(a, b + off * 1.2) for a, b in uranium], mx, my,
                         col, dot=1.6))
    o.append(_legend([(c, l) for c, l in zip(SEP_COLORS, SEP_LABELS)],
                     405, 46, w=100, lh=12, size=6.8))

    return _mk(12, o, "Initial heavy-metal inventory vs thorium content",
               "Trữ lượng kim loại nặng ban đầu theo hàm lượng thori",
               "Initial heavy-metal inventory vs thorium content",
               "Đồ thị trữ lượng ban đầu theo hàm lượng thori với bốn chuỗi Th/U MOX, "
               "SBT, SBU và WASB gần như chồng lên nhau. Trục hoành từ 0 đến 100% thori. "
               "Trục trái màu đen cho trữ lượng urani làm giàu từ 0 đến 25000 kg; trục "
               "phải màu đỏ cho trữ lượng kim loại nặng từ 0 đến 25000 kg. Trữ lượng "
               "urani giảm nhanh từ 18000 kg xuống khoảng 1500 kg, còn trữ lượng kim "
               "loại nặng chỉ giảm nhẹ xuống khoảng 16000 kg.",
               "Plot of initial inventories versus thorium content with four series "
               "Th/U MOX, SBT, SBU and WASB nearly overlapping. The horizontal axis runs "
               "from 0 to 100% thorium. The left black axis gives enriched uranium "
               "inventory from 0 to 25000 kg and the right red axis gives heavy metal "
               "inventory from 0 to 25000 kg. Enriched uranium falls steeply from 18000 "
               "kg to about 1500 kg, while heavy metal declines only slightly to about "
               "16000 kg.")
