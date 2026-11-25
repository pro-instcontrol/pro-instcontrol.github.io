# -*- coding: utf-8 -*-
"""Vector figures 5.13-5.17 for PPIC chapter 5 (thorium/uranium block HTRs).

Each figure is a simplified vector redraw of the printed figure on PDF pages
112-118: initial U-235 inventory, initial effective multiplication factor and
average conversion ratio, k_eff versus EFPD for two ACR values, fuel cycle cost
of four spatial separation levels, and the cost composition of three typical
cores. Axis ranges, labels and data points are read from the printed plots.
"""
from ppicfig5_common import (BLUE, GREEN, GREY, INK, RED, H, W, T, _ar, _b,
                             _circle, _defs, _ellipse, _fig, _frame, _legend,
                             _line, _path, _poly, _rect, _mk, _series,
                             _tri_membership, make_registry)

FIGS, _reg = make_registry()

ORANGE = "#d98416"
BLACK = "#111111"
PURPLE = "#7b3fa1"
TEAL = "#2a9d9d"
YELLOW = "#e0be2c"

SEP_COLORS = (RED, BLUE, GREEN, ORANGE)
SEP_LABELS = ("Th/U MOX", "SBT", "SBU", "WASB")
SEP_LEGEND = [(c, l) for c, l in zip(SEP_COLORS, SEP_LABELS)]

COST_COLORS = (BLACK, RED, GREEN, BLUE, PURPLE, TEAL, YELLOW)
COST_LABELS = ("Natural uranium purchase", "Enrichment", "Fabrication",
               "Storage", "Conversion", "Thorium purchase", "Disposal")


def _stack_bar(cx, width, values, colors, my, labels):
    """One composition column with segment percentages in the wide bands."""
    o = []
    left = cx - width / 2.0
    cum = 0.0
    for i, (v, col) in enumerate(zip(values, colors)):
        top, bot = my(cum + v), my(cum)
        o.append(_rect(left, top, width, bot - top, col,
                       sw=0.8, stroke="#ffffff"))
        if i < len(labels) and labels[i]:
            o.append(T(cx, (top + bot) / 2.0 + 2.3, labels[i], 6.8,
                       color="#ffffff", weight="600"))
        cum += v
    return "".join(o)


@_reg
def fig_f13():
    """Figure 5.13 - initial U-235 inventory versus thorium content."""
    o = [_defs()]
    o.append(T(340, 14, "Initial U-235 inventory vs thorium content",
               8.8, color=INK, weight="600"))

    xt = [(v, str(v)) for v in range(0, 101, 10)]
    yt = [(700 + 50 * k, str(700 + 50 * k)) for k in range(9)]
    frame, mx, my = _frame(70, 42, 470, 205, (-10, 100), (700, 1100), xt, yt,
                           "Thorium content/%", "Inventory of U-235 / kg")
    o.append(frame)

    data = [
        [(0, 960), (10, 1000), (20, 1033), (30, 1040), (40, 1020),
         (50, 1000), (60, 965), (70, 905), (80, 835), (90, 750)],
        [(10, 960), (20, 965), (30, 935), (40, 920), (50, 890),
         (60, 860), (70, 825), (80, 780), (90, 755)],
        [(17, 898), (32, 850), (43, 828), (56, 818), (70, 795),
         (80, 778), (90, 770)],
        [(19, 890), (30, 838), (43, 822), (56, 812), (65, 792)],
    ]
    for pts, col in zip(data, SEP_COLORS):
        o.append(_series(pts, mx, my, col, dot=2.0))
    o.append(_legend(SEP_LEGEND, 440, 50, w=100, lh=13, size=7.0))

    return _mk(13, o, "Initial U-235 inventory vs thorium content",
               "Trữ lượng U-235 ban đầu theo hàm lượng thori",
               "Initial U-235 inventory vs thorium content",
               "Đồ thị trữ lượng ban đầu của U-235 theo hàm lượng thori với bốn chuỗi "
               "Th/U MOX màu đỏ, SBT màu xanh dương, SBU màu xanh lá và WASB màu cam. "
               "Trục hoành từ -10 đến 100% thori, trục tung từ 700 đến 1100 kg. Chuỗi "
               "MOX tăng từ khoảng 960 kg ở 0% lên đỉnh 1040 kg ở 30% thori rồi giảm "
               "còn 750 kg ở 90%. Chuỗi SBT bắt đầu khoảng 960 kg ở 10% và giảm dần "
               "xuống 755 kg ở 90%. Hai chuỗi SBU và WASB bắt đầu khoảng 890 đến "
               "900 kg ở 17 đến 20% thori, giảm dần và hội tụ gần 770 kg ở 90% thori.",
               "Plot of initial U-235 inventory versus thorium content with four "
               "series: Th/U MOX in red, SBT in blue, SBU in green and WASB in "
               "orange. The horizontal axis runs from -10 to 100% thorium and the "
               "vertical axis from 700 to 1100 kg. The MOX series rises from about "
               "960 kg at 0% to a peak near 1040 kg at 30% thorium, then falls to "
               "750 kg at 90%. The SBT series starts near 960 kg at 10% and declines "
               "steadily to 755 kg at 90%. The SBU and WASB series begin near 890 "
               "to 900 kg at 17 to 20% thorium, decline and converge near 770 kg "
               "at 90% thorium.")


@_reg
def fig_f14():
    """Figure 5.14 - initial k_eff and average conversion ratio."""
    o = [_defs()]
    o.append(T(340, 14, "Initial k_eff and average conversion ratio",
               8.8, color=INK, weight="600"))

    xt = [(v, str(v)) for v in range(0, 101, 10)]
    keff = [
        [(0, 1.270), (10, 1.245), (30, 1.235), (40, 1.205), (50, 1.200),
         (60, 1.195), (70, 1.180), (90, 1.195)],
        [(10, 1.250), (30, 1.245), (40, 1.235), (50, 1.220), (60, 1.205),
         (70, 1.190), (80, 1.195), (90, 1.195)],
        [(10, 1.250), (20, 1.250), (30, 1.245), (40, 1.235), (50, 1.225),
         (60, 1.215), (70, 1.190), (80, 1.185), (90, 1.160)],
        [(0, 1.262), (70, 1.185)],
    ]
    acr = [
        [(10, 0.510), (20, 0.620), (30, 0.680), (50, 0.760), (60, 0.790),
         (70, 0.810), (80, 0.790), (90, 0.740)],
        [(20, 0.630), (40, 0.700), (50, 0.730), (60, 0.750), (70, 0.760),
         (80, 0.740), (90, 0.700)],
        [(20, 0.530), (40, 0.570), (50, 0.600), (60, 0.630), (70, 0.650),
         (80, 0.680), (90, 0.720)],
        [(30, 0.600), (50, 0.680), (65, 0.720), (70, 0.920)],
    ]
    panels = [
        (50, (1.18, 1.28), [(1.18 + 0.01 * k, "%.2f" % (1.18 + 0.01 * k))
                            for k in range(11)],
         "k_eff", "(a) Initial multiplication factor", keff),
        (362, (0.50, 0.95), [(0.50 + 0.05 * k, "%.2f" % (0.50 + 0.05 * k))
                             for k in range(9)],
         "ACR", "(b) Average conversion ratio", acr),
    ]
    for x0, yr, yt, ylab, title, data in panels:
        o.append(T(x0 + 134, 33, title, 6.6, color=INK))
        frame, mx, my = _frame(x0, 48, 268, 185, (0, 100), yr, xt, yt,
                               "Thorium content/%", ylab)
        o.append(frame)
        for pts, col in zip(data, SEP_COLORS):
            o.append(_series(pts, mx, my, col, dot=1.7))
        o.append(_legend(SEP_LEGEND, x0 + 165, 56, w=92, lh=11, size=6.4))

    return _mk(14, o, "Initial k_eff and average conversion ratio",
               "Hệ số nhân hiệu dụng ban đầu và tỷ lệ chuyển đổi trung bình",
               "Initial k_eff and average conversion ratio",
               "Biểu đồ hai ô về hệ số nhân hữu hiệu ban đầu k_eff và tỷ lệ chuyển đổi "
               "trung bình ACR theo hàm lượng thori. Ô trái có trục hoành 0 đến 100% "
               "thori, trục tung 1,18 đến 1,28; ô phải có trục tung 0,50 đến 0,95. "
               "Bốn chuỗi là Th/U MOX màu đỏ, SBT màu xanh dương, SBU màu xanh lá và "
               "WASB màu cam. Ở ô trái k_eff giảm khi tăng hàm lượng thori, chuỗi WASB "
               "giảm mạnh xuống khoảng 1,185 ở 70% thori. Ở ô phải ACR tăng dần với "
               "hàm lượng thori, chuỗi WASB tăng vọt lên khoảng 0,92 ở 70% thori.",
               "Two panels of initial effective multiplication factor k_eff and "
               "average conversion ratio ACR versus thorium content. The left panel "
               "has a horizontal axis from 0 to 100% thorium and a vertical axis from "
               "1.18 to 1.28; the right panel has a vertical axis from 0.50 to 0.95. "
               "Four series are shown: Th/U MOX in red, SBT in blue, SBU in green and "
               "WASB in orange. In the left panel k_eff decreases as thorium content "
               "rises, with the WASB series dropping steeply to about 1.185 at 70% "
               "thorium. In the right panel ACR generally increases with thorium "
               "content, and the WASB series jumps to about 0.92 at 70% thorium.")


@_reg
def fig_f15():
    """Figure 5.15 - k_eff versus EFPD for two average conversion ratios."""
    o = [_defs()]
    o.append(T(340, 14, "k_eff vs EFPD for different ACR values",
               8.8, color=INK, weight="600"))

    xt = [(v, str(v)) for v in range(-100, 801, 100)]
    yt = [(1.00 + 0.02 * k, "%.2f" % (1.00 + 0.02 * k)) for k in range(15)]
    frame, mx, my = _frame(70, 42, 470, 205, (-100, 800), (0.98, 1.28), xt, yt,
                           "t / EFPD", "k_eff")
    o.append(frame)

    high = [(0, 1.160), (20, 1.130), (60, 1.120), (100, 1.110), (150, 1.095),
            (200, 1.080), (250, 1.065), (300, 1.050), (350, 1.040),
            (400, 1.030), (450, 1.020), (500, 1.015), (550, 1.010),
            (600, 1.005), (657, 1.003)]
    low = [(0, 1.225), (20, 1.160), (60, 1.158), (100, 1.145), (150, 1.130),
           (200, 1.115), (250, 1.100), (300, 1.085), (350, 1.070),
           (400, 1.055), (450, 1.040), (500, 1.025), (550, 1.015),
           (600, 1.008), (657, 1.005)]
    o.append(_series(high, mx, my, RED, dot=1.9))
    o.append(_series(low, mx, my, BLUE, dot=1.9))
    o.append(_legend([(RED, "ACR 0.582 (Th/U MOX, 70% Th)"),
                      (BLUE, "ACR 0.535 (SBU, 16% Th)")],
                     350, 48, w=190, lh=13, size=6.8))
    o.append(T(mx(3), my(1.225) - 7, "A1", 6.6, color=BLUE))
    o.append(T(mx(3), my(1.160) - 6, "A2", 6.6, color=RED))
    o.append(T(mx(657) + 11, my(1.005) - 2, "B", 6.6, color=INK))

    return _mk(15, o, "k_eff vs EFPD for different average conversion ratios",
               "k_eff theo EFPD với các tỷ lệ chuyển đổi trung bình khác nhau",
               "k_eff vs EFPD for different average conversion ratios",
               "Đồ thị hệ số nhân hữu hiệu k_eff theo thời gian chiếu xạ t tính bằng "
               "EFPD cho hai chu trình có tỷ lệ chuyển đổi trung bình ACR khác nhau. "
               "Trục hoành từ -100 đến 800 EFPD, trục tung từ 0,98 đến 1,28. Đường đỏ "
               "là ACR bằng 0,582 của Th/U MOX với 70% thori, bắt đầu ở 1,160; đường "
               "xanh dương là ACR bằng 0,535 của SBU với 16% thori, bắt đầu ở 1,225. "
               "Cả hai giảm gần tuyến tính và hội tụ tại điểm B khoảng 657 EFPD, "
               "k_eff bằng 1,005.",
               "Plot of effective multiplication factor k_eff versus irradiation "
               "time t in EFPD for two cycles with different average conversion "
               "ratios ACR. The horizontal axis runs from -100 to 800 EFPD and the "
               "vertical axis from 0.98 to 1.28. The red curve is ACR 0.582 for Th/U "
               "MOX with 70% thorium, starting at 1.160; the blue curve is ACR 0.535 "
               "for SBU with 16% thorium, starting at 1.225. Both decrease almost "
               "linearly and converge at point B near 657 EFPD with k_eff equal "
               "to 1.005.")


@_reg
def fig_f16():
    """Figure 5.16 - fuel cycle cost of four spatial separation levels."""
    o = [_defs()]
    o.append(T(340, 14, "Fuel cycle cost of separation levels",
               8.8, color=INK, weight="600"))

    xt = [(v, str(v)) for v in range(-10, 101, 10)]
    yt = [(16 + k, str(16 + k)) for k in range(7)]
    frame, mx, my = _frame(70, 42, 470, 205, (-10, 100), (16, 22), xt, yt,
                           "Thorium content/%", "Cost / 10^-3 $/kWh")
    o.append(frame)

    data = [
        [(0, 18.0), (10, 18.85), (20, 19.7), (30, 20.0), (40, 20.05),
         (50, 19.9), (60, 19.55), (70, 18.85), (80, 17.95), (90, 16.9)],
        [(10, 18.2), (20, 18.5), (30, 18.4), (40, 18.3), (50, 18.05),
         (60, 17.8), (70, 17.5), (80, 17.15), (90, 16.85)],
        [(15, 17.35), (30, 17.0), (40, 16.8), (50, 16.8), (60, 16.75),
         (70, 16.75), (80, 16.8), (90, 17.3)],
        [(15, 17.2), (30, 16.7), (40, 16.7), (50, 16.6), (60, 16.7),
         (70, 17.0)],
    ]
    for pts, col in zip(data, SEP_COLORS):
        o.append(_series(pts, mx, my, col, dot=2.0))
    o.append(_legend(SEP_LEGEND, 440, 50, w=100, lh=13, size=7.0))

    return _mk(16, o, "Fuel cycle cost of different separation levels",
               "Chi phí chu trình nhiên liệu theo cấp tách ly",
               "Fuel cycle cost of different separation levels",
               "Đồ thị chi phí chu trình nhiên liệu theo hàm lượng thori cho bốn cấp "
               "tách ly. Trục hoành từ -10 đến 100% thori, trục tung từ 16 đến 22 theo "
               "đơn vị 10^-3 $/kWh. Bốn chuỗi là Th/U MOX màu đỏ, SBT màu xanh dương, "
               "SBU màu xanh lá và WASB màu cam. Chuỗi MOX tăng từ 18,0 ở 0% lên đỉnh "
               "20,0 ở 30 đến 40% thori rồi giảm xuống 16,9 ở 90%. Chuỗi SBT đạt "
               "khoảng 18,5 ở 20% rồi giảm xuống 16,9 ở 90%. Hai chuỗi SBU và WASB "
               "nằm thấp hơn, quanh 16,6 đến 17,4.",
               "Plot of fuel cycle cost versus thorium content for four spatial "
               "separation levels. The horizontal axis runs from -10 to 100% thorium "
               "and the vertical axis from 16 to 22 in units of 10^-3 $/kWh. Four "
               "series are shown: Th/U MOX in red, SBT in blue, SBU in green and "
               "WASB in orange. The MOX series rises from 18.0 at 0% to a peak near "
               "20.0 at 30 to 40% thorium, then falls to 16.9 at 90%. The SBT series "
               "peaks near 18.5 at 20% and declines to 16.9 at 90%. The SBU and WASB "
               "series stay lower, between about 16.6 and 17.4.")


@_reg
def fig_f17():
    """Figure 5.17 - composition of fuel cycle cost for typical cores."""
    o = [_defs()]
    o.append(T(340, 14, "Composition of fuel cycle cost",
               8.8, color=INK, weight="600"))

    yt = [(10 * k, str(10 * k)) for k in range(11)]
    frame, mx, my = _frame(70, 38, 470, 160, (0, 4), (0, 100),
                           [(1, "MOX 50% Th"), (2, "SBT 89% Th"),
                            (3, "WASB 55% Th")], yt,
                           "Typical reactor core", "Share of total cost / %")
    o.append(frame)

    columns = [
        (1, [39.7, 35.0, 17.7, 2.4, 2.4, 2.3, 0.5],
         ["39.7%", "35%", "17.7%"]),
        (2, [35.5, 35.1, 20.0, 3.0, 3.0, 2.9, 0.5],
         ["35.5%", "35.1%", "20%"]),
        (3, [37.6, 32.7, 21.0, 2.8, 2.8, 2.6, 0.5],
         ["37.6%", "32.7%", "21%"]),
    ]
    for cat, values, labels in columns:
        o.append(_stack_bar(mx(cat), 88, values, COST_COLORS, my, labels))

    o.append(_legend([(c, l) for c, l in zip(COST_COLORS, COST_LABELS[:4])],
                     110, 240, w=215, lh=12, size=6.8))
    o.append(_legend([(c, l) for c, l in zip(COST_COLORS[4:], COST_LABELS[4:])],
                     350, 240, w=220, lh=12, size=6.8))

    return _mk(17, o, "Composition of fuel cycle cost for typical reactor cores",
               "Thành phần chi phí chu trình nhiên liệu của các lõi điển hình",
               "Composition of fuel cycle cost for typical reactor cores",
               "Biểu đồ cột xếp chồng thể hiện thành phần chi phí chu trình nhiên liệu "
               "cho ba lõi điển hình. Trục hoành gồm ba cột: Th/U MOX với 50% thori, "
               "SBT với 89% thori và WASB với 55% thori; trục tung từ 0 đến 100% tổng "
               "chi phí. Bảy thành phần theo chú giải là mua urani tự nhiên màu đen, "
               "làm giàu màu đỏ, chế tạo màu xanh lá, lưu trữ màu xanh dương, chuyển "
               "đổi màu tím, mua thori màu xanh ngọc và xử lý nhiên liệu đã chiếu màu "
               "vàng. Mua urani tự nhiên chiếm 39,7%, 35,5% và 37,6%; làm giàu chiếm "
               "35%, 35,1% và 32,7%; chế tạo chiếm 17,7%, 20% và 21%.",
               "Stacked bar chart of fuel cycle cost composition for three typical "
               "reactor cores. The horizontal axis has three bars: Th/U MOX with 50% "
               "thorium, SBT with 89% thorium and WASB with 55% thorium; the vertical "
               "axis runs from 0 to 100% of total cost. The seven components in the "
               "legend are natural uranium purchase in black, enrichment in red, "
               "fabrication in green, storage in blue, conversion in purple, thorium "
               "purchase in teal and disposal of spent fuel in yellow. Natural "
               "uranium purchase takes 39.7%, 35.5% and 37.6%; enrichment takes "
               "35%, 35.1% and 32.7%; fabrication takes 17.7%, 20% and 21%.")
