# -*- coding: utf-8 -*-
"""Practical Process Control, Chapter 13 — Fuzzy Logic and Neural Networks."""
import math

from vfig import (BLUE, GOLD, GREEN, GREY, INK, PAPER, RED, _arrow, _axes, _box,
                  _circle, _curve, _ellipse, _line, _node, _path, _poly, _rect,
                  _txt)
from pcfig import _finish, _legend, _legend_h

PURPLE = "#6b3f6b"
SET5 = [BLUE, GREEN, GOLD, RED, PURPLE]


# ---------------------------------------------------------------- helpers
def _prect(x, y, w, h, fill, op=0.16, sw=1.1, stroke=None, dash=""):
    """A filled rectangle with a separate fill-opacity (vfig._rect has none)."""
    d = (' stroke-dasharray="%s"' % dash) if dash else ""
    return ('<rect x="%s" y="%s" width="%s" height="%s" fill="%s" fill-opacity="%s" '
            'stroke="%s" stroke-width="%s"%s/>'
            % (_f2(x), _f2(y), _f2(w), _f2(h), fill, op, stroke or fill, sw, d))


def _f2(v):
    return ("%.2f" % v).rstrip("0").rstrip(".")


def _mk(x0, y0, W, H, xr, yr):
    """Two mappers from data space to page space for one plotting box."""
    def X(v):
        return x0 + (v - xr[0]) / float(xr[1] - xr[0]) * W

    def Y(v):
        return y0 + H - (v - yr[0]) / float(yr[1] - yr[0]) * H
    return X, Y


def _tri(x, c, w):
    """A symmetric triangular membership function, peak 1 at c, zero at c ± w."""
    if x <= c - w or x >= c + w:
        return 0.0
    return 1.0 - abs(x - c) / w


# ---------------------------------------------------------------- 13.1
def fig_13_1():
    """A crisp set against a fuzzy set, on the same membership axis."""
    o = []
    for x0, kind in ((58, "crisp"), (378, "fuzzy")):
        X, Y = _mk(x0, 48, 226, 104, (0.0, 1.0), (0.0, 1.15))
        o.append(_axes(x0, 48, 226, 104, "nhiệt độ", "μ",
                       xt=[(0.0, ""), (1.0, "")],
                       yt=[(0.0, "0"), (1.0 / 1.15, "1")]))
        o.append(_line(x0, Y(0.5), x0 + 226, Y(0.5), sw=0.7, dash="3 3", color="#d0cbc0"))
        if kind == "crisp":
            pts = [(X(0.0), Y(0)), (X(0.32), Y(0)), (X(0.32), Y(1)),
                   (X(0.68), Y(1)), (X(0.68), Y(0)), (X(1.0), Y(0))]
            o.append(_poly(pts, sw=2.0, color=BLUE))
            o.append(_prect(X(0.32), Y(1), X(0.68) - X(0.32), Y(0) - Y(1), BLUE, 0.10))
            o.append(_txt(x0 + 113, 182, "Tập hợp chuẩn: thuộc hoặc không", 7.6, weight="600"))
            o.append(_txt(x0 + 113, 194, "luật bài trung của Aristotle", 6.8, color=GREY))
        else:
            pts = [(X(0.14), Y(0)), (X(0.36), Y(1)), (X(0.62), Y(1)), (X(0.86), Y(0))]
            area = [(X(0.14), Y(0))] + pts[1:] + [(X(0.86), Y(0))]
            o.append(_poly(area, fill="#f5e7cf", sw=0.0, color="#f5e7cf", close=True))
            o.append(_poly(pts, sw=2.0, color=GOLD))
            o.append(_arrow(X(0.66), Y(0.44), X(0.76), Y(0.80), sw=0.9, color=GREY))
            o.append(_txt(X(0.78), Y(0.84), "biên mờ dần", 6.6, anchor="start", color=GREY))
            o.append(_txt(x0 + 113, 182, "Tập hợp mờ: thuộc một phần", 7.6, weight="600"))
            o.append(_txt(x0 + 113, 194, "có thể thuộc nhiều tập cùng lúc", 6.8, color=GREY))
    o.append(_txt(330, 24, "Cùng một trục độ phụ thuộc, hai cách định nghĩa tập", 8.6, weight="600"))
    return _finish(o, 660, 214,
                   "Hình 13-1. Tập hợp chuẩn chỉ có hai mức phụ thuộc 0 và 1, biên là một bước nhảy "
                   "thẳng đứng. Tập hợp mờ cho phép mọi giá trị giữa 0 và 1, biên thoải dần nên một "
                   "phần tử có thể vừa thuộc vừa không thuộc.",
                   "Figure 13-1. A crisp set allows only the two membership levels 0 and 1, and its "
                   "boundary is a vertical step. A fuzzy set allows every value between 0 and 1, and "
                   "its boundary tapers, so one element can partly belong and partly not.",
                   "Hai đồ thị cạnh nhau. Bên trái, tập hợp chuẩn có dạng bậc thang vuông từ 0 lên 1. "
                   "Bên phải, tập hợp mờ có dạng hình thang với hai sườn thoải.",
                   "Two side-by-side plots. On the left the crisp set is a square step from 0 to 1; "
                   "on the right the fuzzy set is a trapezoid with two sloping shoulders.")


# ---------------------------------------------------------------- 13.2
def fig_13_2():
    """The five rule patches of the air-conditioner example."""
    T0, W, H = 68, 452, 132
    xr, yr = (56.0, 82.0), (0.0, 100.0)
    X, Y = _mk(T0, 52, W, H, xr, yr)
    o = [_axes(T0, 52, W, H, "nhiệt độ (°F)", "tốc độ động cơ (%)",
               xt=[((v - 56) / 26.0, str(v)) for v in (56, 64, 72, 80)],
               yt=[(0.0, "0"), (0.5, "50"), (1.0, "100")])]

    # the five temperature centres are set so that 68 °F reads 20 % cool and
    # 70 % just right, exactly the membership values the chapter quotes
    rules = [(60.4, 10, "RẤT CHẬM"), (64.8, 30, "CHẬM"), (69.2, 50, "VỪA"),
             (73.6, 70, "NHANH"), (78.0, 90, "TỐI ĐA")]
    hw, hh = 4.4, 20.0
    for i, (cx, cy, _lab) in enumerate(rules):
        x1, x2 = max(xr[0], cx - hw), min(xr[1], cx + hw)
        y1, y2 = max(yr[0], cy - hh), min(yr[1], cy + hh)
        o.append(_prect(X(x1), Y(y2), X(x2) - X(x1), Y(y1) - Y(y2), SET5[i], 0.15))
    for i, (cx, cy, lab) in enumerate(rules):
        x1, x2 = max(xr[0], cx - hw), min(xr[1], cx + hw)
        y1, y2 = max(yr[0], cy - hh), min(yr[1], cy + hh)
        o.append(_rect(X(x1), Y(y2), X(x2) - X(x1), Y(y1) - Y(y2), "none", sw=1.0,
                       stroke=SET5[i]))
        wlab = 4.7 * len(lab) + 7
        o.append(_rect(X(cx) - wlab / 2.0, Y(cy) - 7.4, wlab, 11.2, PAPER, sw=0,
                       stroke=PAPER))
        o.append(_txt(X(cx), Y(cy) + 2.2, lab, 6.2, color=SET5[i], weight="600"))

    o.append(_line(X(68), Y(0), X(68), Y(100), sw=0.8, dash="2 3", color=INK))
    o.append(_txt(X(68), Y(0) + 9, "68 °F", 6.4, color=INK))
    o.append(_txt(X(58.6), Y(96), "năm mảng luật phủ kín", 6.2, anchor="start", color=GREY))
    o.append(_txt(X(58.6), Y(88), "toàn dải nhiệt độ", 6.2, anchor="start", color=GREY))
    return _finish(o, 660, 246,
                   "Hình 13-2. Năm luật của một máy điều hoà, mỗi luật là một mảng chữ nhật trong mặt "
                   "phẳng nhiệt độ – tốc độ. Các mảng chồng lên nhau nên một nhiệt độ bất kỳ luôn "
                   "đánh thức từ hai luật trở lên, mỗi luật chỉ ở một mức độ nhất định.",
                   "Figure 13-2. The five rules of an air conditioner, each a rectangular patch in the "
                   "temperature–speed plane. The patches overlap, so any temperature fires at least two "
                   "rules, each only to some degree.",
                   "Đồ thị nhiệt độ theo tốc độ động cơ với năm hình chữ nhật chồng nhau chạy dọc theo "
                   "đường chéo, mỗi hình mang tên một tập tốc độ.",
                   "A temperature-versus-motor-speed plot with five overlapping rectangles stepping up "
                   "along the diagonal, each labelled with one speed set.")


# ---------------------------------------------------------------- 13.3
def fig_13_3():
    """The two α-cuts and the aggregated output curve."""
    x0, y0, W, H = 68, 48, 470, 130
    X, Y = _mk(x0, y0, W, H, (0.0, 100.0), (0.0, 1.0))
    o = [_axes(x0, y0, W, H, "tốc độ động cơ (% thang)", "μ",
               xt=[(0.0, "0"), (0.5, "50"), (1.0, "100")],
               yt=[(0.0, "0"), (0.2, "0,2"), (0.5, "0,5"), (0.7, "0,7"), (1.0, "1")])]

    centres = [10.0, 30.0, 50.0, 70.0, 90.0]
    for c in centres:
        o.append(_poly([(X(v), Y(_tri(v, c, 20.0)))
                        for v in [c - 20.0 + 0.5 * i for i in range(81)]],
                       sw=0.8, color="#cfc9bd"))

    def clipped(v, c, a):
        return min(_tri(v, c, 20.0), a)

    def agg(v):
        return max(clipped(v, 30.0, 0.20), clipped(v, 50.0, 0.70))

    # the SLOW set cut at 0.20 and the MEDIUM set cut at 0.70
    for c, a, col, pale in ((30.0, 0.20, BLUE, "#cfdde9"), (50.0, 0.70, GOLD, "#f0dfc4")):
        pts = [(X(v), Y(clipped(v, c, a))) for v in [c - 20.0 + 0.5 * i for i in range(81)]]
        o.append(_poly(pts + [(X(c + 20.0), Y(0)), (X(c - 20.0), Y(0))],
                       fill=pale, sw=0.0, color=pale, close=True))
        o.append(_poly(pts, sw=1.5, color=col, dash="4 2"))

    o.append(_poly([(X(v), Y(agg(v))) for v in [0.0 + 0.25 * i for i in range(401)]],
                   sw=2.2, color=RED))

    o.append(_arrow(X(22), Y(0.30), X(26), Y(0.205), sw=0.9, color=BLUE))
    o.append(_txt(X(21), Y(0.34), "CHẬM cắt tại 0,20", 6.2, anchor="end", color=BLUE))
    o.append(_arrow(X(58), Y(0.83), X(56), Y(0.705), sw=0.9, color=GOLD))
    o.append(_txt(X(59), Y(0.88), "VỪA cắt tại 0,70", 6.2, anchor="start", color=GOLD))
    o.append(_arrow(X(74), Y(0.60), X(66), Y(0.66), sw=0.9, color=RED))
    o.append(_txt(X(75), Y(0.64), "hợp của hai lát cắt", 6.2, anchor="start", color=RED))
    o.append(_legend_h(x0 + 4, y0 + H + 34,
                       [(BLUE, "tập CHẬM bị cắt", ""),
                        (GOLD, "tập VỪA bị cắt", ""),
                        (RED, "tập đầu ra hợp thành", "")], gap=14))
    return _finish(o, 660, 240,
                   "Hình 13-3. Hai luật cùng đánh thức: tập CHẬM bị cắt xuống còn 0,20 chiều cao, tập "
                   "VỪA còn 0,70. Lấy hợp của hai lát cắt theo từng điểm ta được đường cong đầu ra "
                   "của tập mờ.",
                   "Figure 13-3. Two rules fire together: the SLOW set is clipped to 0.20 of its "
                   "height and the MEDIUM set to 0.70. Taking the point-by-point union of the two "
                   "clipped slices gives the output curve of the fuzzy set.",
                   "Đồ thị độ phụ thuộc theo tốc độ: hai hình thang bị cắt ngang ở mức 0,2 và 0,7, "
                   "đường bao ngoài cùng màu đỏ là tập đầu ra hợp thành.",
                   "A membership-versus-speed plot: two triangles cut flat at 0.2 and 0.7, with the "
                   "outer envelope drawn in red as the aggregated output set.")


# ---------------------------------------------------------------- 13.4
def fig_13_4():
    """Defuzzification: the centroid of the aggregated curve."""
    x0, y0, W, H = 68, 48, 470, 130
    X, Y = _mk(x0, y0, W, H, (0.0, 100.0), (0.0, 1.0))
    o = [_axes(x0, y0, W, H, "tốc độ động cơ (% thang)", "μ",
               xt=[(0.0, "0"), (0.5, "50"), (1.0, "100")],
               yt=[(0.0, "0"), (0.5, "0,5"), (1.0, "1")])]

    def clipped(v, c, a):
        return min(_tri(v, c, 20.0), a)

    def agg(v):
        return max(clipped(v, 30.0, 0.20), clipped(v, 50.0, 0.70))

    vs = [0.25 * i for i in range(401)]
    num = den = 0.0
    for v in vs:
        m = agg(v)
        num += m * v
        den += m
    centroid = num / den

    pts = [(X(v), Y(agg(v))) for v in vs]
    o.append(_poly([(X(0.0), Y(0.0))] + pts + [(X(100.0), Y(0.0))],
                   fill="#f3ded8", sw=0.0, color="#f3ded8", close=True))
    o.append(_poly(pts, sw=2.0, color=RED))

    o.append(_line(X(centroid), Y(0.0), X(centroid), Y(0.86), sw=1.6, color=INK))
    o.append(_circle(X(centroid), Y(0.0), 3.2, fill=INK, sw=0))
    o.append(_txt(X(centroid) - 5, Y(0.90), "trọng tâm ≈ %.0f" % centroid, 7.0,
                  anchor="end", color=INK, weight="600"))
    o.append(_line(X(47), Y(0.0), X(47), Y(0.34), sw=1.0, dash="3 3", color=GREY))
    o.append(_txt(X(47) + 5, Y(0.30), "sách nêu 47", 6.2, anchor="start", color=GREY))
    return _finish(o, 660, 226,
                   "Hình 13-4. Giải mờ: lấy hoành độ trọng tâm của diện tích dưới đường cong hợp "
                   "thành, ta được một con số duy nhất — ở đây khoảng 45 % thang tốc độ. Sách nêu "
                   "47 rpm cho cùng ví dụ; xem ghi chú của người dịch.",
                   "Figure 13-4. Defuzzification: taking the abscissa of the centroid of the area "
                   "under the aggregated curve yields a single number — here about 45 % of the speed "
                   "scale. The book quotes 47 rpm for the same example; see the translator's note.",
                   "Đồ thị tập đầu ra hợp thành tô hồng, một đường thẳng đứng đánh dấu trọng tâm ở "
                   "khoảng 45 trên trục tốc độ.",
                   "The aggregated output set shaded pink, with a vertical line marking the centroid "
                   "at about 45 on the speed axis.")


# ---------------------------------------------------------------- 13.5
def fig_13_5():
    """A three-layer back-propagation network, fully connected."""
    o = []
    ins = [(96, 66), (96, 118), (96, 170)]
    hid = [(322, 42), (322, 94), (322, 146), (322, 198)]
    out = [(552, 120)]

    for a in ins:
        for b in hid:
            o.append(_line(a[0], a[1], b[0], b[1], sw=0.7, color="#c3bdb0"))
    for a in hid:
        for b in out:
            o.append(_line(a[0], a[1], b[0], b[1], sw=0.7, color="#c3bdb0"))

    for i, (cx, cy) in enumerate(ins):
        o.append(_node(cx, cy, "X%d" % (i + 1), fill="#e8eef6", r=15, size=7.6))
    for cx, cy in hid:
        o.append(_node(cx, cy, "", fill="#f6ecd8", r=15))
    for cx, cy in out:
        o.append(_node(cx, cy, "Y", fill="#e6f0e8", r=15, size=8.4))

    o.append(_txt(322, 226, "lớp ẩn", 7.4, color=GREY))
    o.append(_txt(96, 210, "lớp vào", 7.4, color=GREY))
    o.append(_txt(552, 158, "lớp ra", 7.4, color=GREY))

    o.append(_circle(209, 54, 9.5, fill="#fff", sw=0.9, color=INK))
    o.append(_txt(209, 56.6, "w", 6.4))
    o.append(_txt(330, 22, "ba lớp, mỗi nơ-ron nối tới mọi nơ-ron của lớp sau", 8.0, weight="600"))
    return _finish(o, 660, 246,
                   "Hình 13-5. Một mạng nơ-ron ba lớp điển hình: lớp vào, một lớp ẩn và lớp ra. Mọi "
                   "nơ-ron của một lớp đều nối tới mọi nơ-ron của lớp kế tiếp, và mỗi đường nối mang "
                   "một trọng số w.",
                   "Figure 13-5. A typical three-layer neural network: an input layer, one hidden layer "
                   "and an output layer. Every neuron in a layer connects to every neuron in the next, "
                   "and each connection carries a weight w.",
                   "Sơ đồ mạng nơ-ron: ba nút bên trái nối đầy đủ tới bốn nút ở giữa, bốn nút giữa nối "
                   "đầy đủ tới một nút bên phải.",
                   "A neural-network diagram: three nodes on the left fully connected to four nodes in "
                   "the middle, which are fully connected to a single node on the right.")


# ---------------------------------------------------------------- 13.6
def fig_13_6():
    """What happens inside one neuron."""
    o = []
    ys = [36, 66, 96, 126]
    for i, y in enumerate(ys):
        o.append(_txt(62, y + 2.6, "X%d" % (i + 1), 7.4, anchor="end"))
        o.append(_arrow(70, y, 268, y, sw=0.9, color=INK))
        o.append(_circle(176, y, 9.5, fill="#fff", sw=0.9, color=INK))
        o.append(_txt(176, y + 2.4, "w%d" % (i + 1), 6.0))

    o.append(_circle(292, 81, 20, fill="#f6ecd8", sw=1.3))
    o.append(_txt(292, 88, "Σ", 13))
    o.append(_arrow(292, 20, 292, 59, sw=1.0, color=GREEN))
    o.append(_txt(300, 26, "B<sub>j</sub>", 7.2, anchor="start", color=GREEN))

    o.append(_box(356, 53, 104, 56, "f ( I )", fill="#e8eef6", size=8.4, sub="hàm kích hoạt"))
    o.append(_arrow(312, 81, 354, 81, sw=1.1))
    o.append(_arrow(462, 81, 520, 81, sw=1.1))
    o.append(_txt(540, 84, "Y", 9.0, anchor="start", weight="600"))

    o.append(_txt(330, 146, "I<sub>j</sub> = Σ W<sub>ji</sub> X<sub>i</sub> + B<sub>j</sub>",
                  9.0))
    o.append(_txt(330, 166, "Y<sub>j</sub> = f ( I<sub>j</sub> )", 9.0))
    o.append(_txt(330, 186, "trọng số là chỗ duy nhất mạng có thể thay đổi", 7.0, color=GREY))
    return _finish(o, 660, 202,
                   "Hình 13-6. Bên trong một nơ-ron: các đầu vào X đi qua trọng số w, cộng lại thành "
                   "tổng có trọng số I, cộng thêm một ngưỡng B, rồi được bẻ cong bởi hàm kích hoạt f "
                   "để cho ra Y. Muốn đổi hành vi của nơ-ron thì chỉ có cách đổi các trọng số.",
                   "Figure 13-6. Inside one neuron: the inputs X pass through the weights w and are "
                   "summed into the weighted total I, a bias B is added, and the result is bent by the "
                   "activation function f to give Y. The only way to change the neuron's behaviour is "
                   "to change the weights.",
                   "Sơ đồ một nơ-ron: bốn mũi tên đầu vào X1 tới X4 đi qua bốn vòng tròn trọng số, "
                   "hội tụ vào một nút tổng, rồi qua hộp hàm kích hoạt ra đầu ra Y.",
                   "A single-neuron diagram: four input arrows X1 to X4 pass through four weight "
                   "circles, meet at a summation node, then pass through an activation-function box "
                   "to the output Y.")


# ---------------------------------------------------------------- 13.7
def fig_13_7():
    """The sigmoidal activation function at two thresholds."""
    x0, y0, W, H = 74, 44, 458, 126
    X, Y = _mk(x0, y0, W, H, (-6.0, 6.0), (-0.05, 1.05))
    o = [_axes(x0, y0, W, H, "tổng đầu vào I", "f ( I )",
               xt=[(0.0, "−6"), (0.5, "0"), ((2 - -6) / 12.0, "2"), (1.0, "6")],
               yt=[((0.0 + 0.05) / 1.1, "0"), ((0.5 + 0.05) / 1.1, "0,5"),
                   ((1.0 + 0.05) / 1.1, "1")])]
    o.append(_line(x0, Y(0.0), x0 + W, Y(0.0), sw=0.8, dash="4 3", color=GREY))
    o.append(_line(x0, Y(1.0), x0 + W, Y(1.0), sw=0.8, dash="4 3", color=GREY))
    o.append(_txt(x0 + 4, Y(1.0) - 5, "trần +1", 6.2, anchor="start", color=GREY))
    o.append(_txt(x0 + W - 6, Y(0.0) - 5, "sàn 0", 6.2, anchor="end", color=GREY))

    for T, col in ((0.0, BLUE), (2.0, GOLD)):
        o.append(_curve(lambda I, T=T: 1.0 / (1.0 + math.exp(-(I - T))),
                        x0, y0, W, H, n=241, xr=(-6.0, 6.0), yr=(-0.05, 1.05),
                        sw=2.1, color=col))
        o.append(_circle(X(T), Y(0.5), 3.0, fill=col, sw=0))
        o.append(_line(X(T), Y(0.0), X(T), Y(0.5), sw=0.8, dash="2 3", color=col))

    o.append(_txt(X(0.0) - 6, Y(0.36), "T = 0", 6.6, anchor="end", color=BLUE))
    o.append(_txt(X(2.0) + 7, Y(0.36), "T = 2", 6.6, anchor="start", color=GOLD))
    o.append(_txt(X(-3.4), Y(0.16), "dốc đuôi dài", 6.2, anchor="start", color=GREY))
    return _finish(o, 660, 208,
                   "Hình 13-7. Hàm kích hoạt sigmoid f(I) = 1 / (1 + e<sup>−(I−T)</sup>). Đường cong "
                   "liên tục, hình chữ S, tăng đơn điệu và tiệm cận hai giá trị cố định khi I tiến ra "
                   "±∞. Đổi ngưỡng T chỉ làm đường cong trượt ngang; độ dốc và hình dạng S mới là điều "
                   "quan trọng, không phải công thức chính xác.",
                   "Figure 13-7. The sigmoidal activation function f(I) = 1 / (1 + e<sup>−(I−T)</sup>). "
                   "The curve is continuous, S-shaped, monotonically increasing and asymptotic to two "
                   "fixed values as I goes to ±∞. Changing the threshold T only slides the curve "
                   "sideways; the slope and the S shape matter, not the exact formula.",
                   "Đồ thị hai đường cong chữ S: đường xanh đi qua điểm giữa tại I bằng 0, đường vàng "
                   "dịch sang phải đi qua điểm giữa tại I bằng 2, cả hai tiệm cận 0 và 1.",
                   "A plot of two S-curves: the blue one crosses its midpoint at I = 0, the gold one is "
                   "shifted right to cross at I = 2, both asymptotic to 0 and 1.")


# ---------------------------------------------------------------- 13.8
def fig_13_8():
    """Gradient descent on a bowl-shaped error surface."""
    a, b, eta = 0.15, 3.0, 0.45
    x0, y0, W, H = 96, 44, 380, 132
    xr, yr = (-1.15, 1.15), (-0.30, 0.30)
    X, Y = _mk(x0, y0, W, H, xr, yr)
    o = [_axes(x0, y0, W, H, "w₁", "w₂",
               xt=[(0.5, "0"), (1.0, "")],
               yt=[(0.5, "0"), (1.0, "")])]

    for c in (0.008, 0.025, 0.05, 0.08, 0.11):
        o.append(_ellipse(X(0.0), Y(0.0),
                          math.sqrt(2 * c / a) / (xr[1] - xr[0]) * W,
                          math.sqrt(2 * c / b) / (yr[1] - yr[0]) * H,
                          fill="none", sw=0.8, color="#cfc9bd"))

    w, path = [1.0, 0.22], [(1.0, 0.22)]
    for _ in range(12):
        w[0] -= eta * a * w[0]
        w[1] -= eta * b * w[1]
        path.append((w[0], w[1]))

    o.append(_poly([(X(u), Y(v)) for u, v in path], sw=1.6, color=BLUE))
    for u, v in path[:-1]:
        o.append(_circle(X(u), Y(v), 2.1, fill=BLUE, sw=0))
    o.append(_circle(X(path[-1][0]), Y(path[-1][1]), 3.0, fill=BLUE, sw=0))

    o.append(_circle(X(0.0), Y(0.0), 3.2, fill=RED, sw=0))
    o.append(_txt(X(-0.08), Y(0.09), "cực tiểu: sai số bằng 0", 6.2, anchor="end",
                  color=RED))
    o.append(_txt(X(0.97), Y(0.20), "xuất phát", 6.2, anchor="end", color=INK))
    o.append(_arrow(X(0.63), Y(0.17), X(0.88), Y(0.03), sw=0.9, color=GREY))
    o.append(_txt(X(0.62), Y(0.20), "dao động tắt nhanh", 6.2, anchor="end", color=GREY))
    o.append(_arrow(X(0.31), Y(-0.17), X(0.50), Y(-0.01), sw=0.9, color=GREY))
    o.append(_txt(X(0.30), Y(-0.19), "bò chậm theo trục thoải", 6.2, anchor="end", color=GREY))
    return _finish(o, 660, 226,
                   "Hình 13-8. Mặt sai số dạng cái bát, vẽ bằng các đường đồng mức, mỗi đường là một "
                   "mức sai số như nhau. Hạ theo gradient thì dao động ngang qua trục dốc w₂ tắt rất "
                   "nhanh, nhưng dọc theo trục thoải w₁ mạng vẫn bò rất chậm — đó chính là lý do người "
                   "ta thêm số hạng quán tính α để tăng tốc theo phương chậm.",
                   "Figure 13-8. A bowl-shaped error surface drawn as contours, each contour a level of "
                   "equal error. Gradient descent damps the wobble across the steep axis w₂ almost at "
                   "once, but along the shallow axis w₁ the network still crawls — which is exactly why "
                   "a momentum term α is added to speed up the slow direction.",
                   "Đồ thị đường đồng mức hình bầu dục lồng nhau, một đường gấp khúc màu xanh từ góc "
                   "trên bên phải dao động mạnh theo phương đứng vài bước rồi bò dần theo phương ngang "
                   "về chấm đỏ ở giữa.",
                   "A contour plot of nested ellipses with a blue path from the upper right that "
                   "wobbles vertically for a few steps then crawls horizontally toward the red dot at "
                   "the centre.")


FIGURES = [fig_13_1, fig_13_2, fig_13_3, fig_13_4,
           fig_13_5, fig_13_6, fig_13_7, fig_13_8]
