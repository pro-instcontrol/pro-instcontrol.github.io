# -*- coding: utf-8 -*-
"""Vector redraws of Figures 4.1-4.3 in A. McMillan, *Electrical Installations
in Hazardous Areas*, Chapter 4 "Calculation of release rates and extents".

Fig. 4.1 is a log-log chart of the extent of a hazardous area relative to
wind dispersion against release differential pressure; Fig. 4.2 is an
unhatched geometry sketch of a gas release and its hazardous envelope;
Fig. 4.3 plots R^0.2 against pool area.  All plotted curves are smooth
monotone redraws of the printed shapes, not claims about source data.

Architecture mirrors `mcmillanfig03_a.py` and `mcmillanfig02_a.py`: every
figure returns the standard five-tuple through `vfig._fig()` and is
registered in `FIGS` by the `_reg` decorator.
"""
import sys
import os
import math

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

from vfig import (GREY, INK, PAPER, _arrow, _circle, _defs, _fig, _line,
                  _path, _poly, _rect, _txt, svg)

FIGS = {}


def _reg(f):
    FIGS[f.__name__] = f()
    return f


def esc(s):
    """Escape XML-significant characters in displayed text."""
    return (str(s).replace("&", "&amp;").replace("<", "&lt;")
            .replace(">", "&gt;").replace('"', "&quot;"))


def T(x, y, s, size=8.0, **kw):
    """Plain text: escape first, then delegate to vfig._txt()."""
    return _txt(x, y, esc(s), size, **kw)


def TM(x, y, s, size=8.0, **kw):
    """Markup text: allow <sup>/<sub> tags, escape bare ampersands."""
    return _txt(x, y, str(s).replace("&", "&amp;"), size, **kw)


def _pchip(pts):
    """Monotone cubic Hermite interpolant through (x, y) anchor pairs."""
    xs = [p[0] for p in pts]
    ys = [p[1] for p in pts]
    n = len(xs)
    h = [xs[i + 1] - xs[i] for i in range(n - 1)]
    d = [(ys[i + 1] - ys[i]) / h[i] for i in range(n - 1)]
    m = [0.0] * n
    m[0], m[-1] = d[0], d[-1]
    for i in range(1, n - 1):
        if d[i - 1] * d[i] <= 0.0:
            m[i] = 0.0
        else:
            w1, w2 = 2.0 * h[i] + h[i - 1], h[i] + 2.0 * h[i - 1]
            m[i] = (w1 + w2) / (w1 / d[i - 1] + w2 / d[i])

    def f(x):
        if x <= xs[0]:
            return ys[0]
        if x >= xs[-1]:
            return ys[-1]
        i = 0
        while i < n - 2 and x > xs[i + 1]:
            i += 1
        t = (x - xs[i]) / h[i]
        t2, t3 = t * t, t * t * t
        return ((2 * t3 - 3 * t2 + 1) * ys[i]
                + (t3 - 2 * t2 + t) * h[i] * m[i]
                + (-2 * t3 + 3 * t2) * ys[i + 1]
                + (t3 - t2) * h[i] * m[i + 1])
    return f


@_reg
def fig_f401():
    """Figure 4.1 - Extent of hazardous area versus differential pressure."""
    w, h = 680, 470
    o = [_defs(), _rect(0, 0, w, h, fill=PAPER, sw=0)]
    o.append(T(340, 18,
               "Hình 4.1 · Phạm vi vùng nguy hiểm theo áp suất chênh lệch / "
               "Figure 4.1 · Extent of hazardous area versus differential pressure",
               8.8, color=INK, weight="600"))
    o.append(T(340, 32,
               "Đồ thị log-log; chú thích in trên hình là mục xác thực / "
               "Log-log chart; the printed legend is authoritative",
               6.6, color=GREY))

    x0, ytop, W, H = 84.0, 52.0, 532.0, 308.0
    ybot = ytop + H
    lx0, lx1 = math.log10(2.0e3), 7.0

    def X(lp):
        return x0 + (lp - lx0) / (lx1 - lx0) * W

    def Y(v):
        return ytop + (1.0 - math.log10(v)) / 3.0 * H

    ylabels = [(10, "10"), (7, "7"), (5, "5"), (3, "3"), (2, "2"),
               (1, "1"), (0.7, "0.7"), (0.5, "0.5"), (0.3, "0.3"),
               (0.2, "0.2"), (0.1, "0.1"), (0.07, "0.07"), (0.05, "0.05"),
               (0.03, "0.03"), (0.02, "0.02"), (0.01, "0.01")]
    for v, lab in ylabels:
        yy = Y(v)
        o.append(_line(x0, yy, x0 + W, yy, sw=0.5, color="#d6d1c5"))
        o.append(_line(x0 - 3, yy, x0, yy, sw=0.8, color=INK))
        o.append(T(x0 - 6, yy + 2.1, lab, 6.4, anchor="end", color=GREY))

    xlabels = []
    for decade in range(3, 7):
        prefix = "10<sup>%d</sup>" % decade
        for mant in (2, 3, 5, 7):
            xlabels.append((mant * 10.0 ** decade,
                            "%s×%s" % (mant, prefix)))
        xlabels.append((10.0 ** decade, prefix))
    xlabels.append((1.0e7, "10<sup>7</sup>"))
    xlabels.sort(key=lambda p: p[0])
    for val, lab in xlabels:
        xx = X(math.log10(val))
        o.append(_line(xx, ytop, xx, ybot, sw=0.5, color="#d6d1c5"))
        o.append(_line(xx, ybot, xx, ybot + 3, sw=0.8, color=INK))
        o.append(TM(xx, ybot + 12, lab, 5.6, color=GREY))

    o.append(_line(x0, ytop, x0, ybot, sw=1.1, color=INK))
    o.append(_line(x0, ybot, x0 + W, ybot, sw=1.1, color=INK))

    # Printed ordinate key, reproduced as a small box inside the plot.
    key = [T(x0 + 7, 64, "x = Extent of hazardous area", 6.2, anchor="start"),
           T(x0 + 7, 73, "as a fraction of that", 6.2, anchor="start"),
           T(x0 + 7, 82, "produced by wind dispersion at", 6.2, anchor="start"),
           T(x0 + 7, 91, "a release differential pressure", 6.2, anchor="start"),
           TM(x0 + 7, 100, "of 10<sup>5</sup> N/m<sup>2</sup>", 6.2,
              anchor="start")]
    o.extend(key)

    # Smooth monotone redraws; the printed curves are not tabulated data.
    curves = [
        ([(3.301, 0.35), (4.0, 0.40), (5.0, 0.65), (5.7, 1.15),
          (6.3, 2.4), (7.0, 7.0)], "1"),
        ([(3.301, 0.33), (4.0, 0.38), (5.0, 0.58), (5.7, 0.95),
          (6.3, 1.85), (7.0, 5.0)], "2"),
        ([(3.301, 0.30), (4.0, 0.35), (5.0, 0.52), (5.7, 0.80),
          (6.3, 1.45), (7.0, 3.7)], "3"),
        ([(3.301, 0.27), (4.0, 0.27), (5.0, 0.27), (5.7, 0.27),
          (6.0, 0.33), (6.5, 0.95), (7.0, 2.0)], "4"),
    ]
    for anchors, num in curves:
        f = _pchip(anchors)
        pts = [(X(lx0 + (lx1 - lx0) * i / 240.0),
                Y(f(lx0 + (lx1 - lx0) * i / 240.0))) for i in range(241)]
        o.append(_poly(pts, fill="none", sw=1.7, color=INK))
        vend = f(lx1)
        o.append(T(X(lx1) - 11, Y(vend) - 5, num, 8.2,
                   anchor="end", color=INK, weight="600"))

    # Verbatim four-line printed legend (superscript markup renders as printed).
    legend = [
        "1 - Curve for wind dispersion at all pressures",
        "2 - Curve for total jet dispersion above 10<sup>5</sup> N/m<sup>2</sup> - molecular wt = 1",
        "3 - Curve for total jet dispersion above 10<sup>5</sup> N/m<sup>2</sup> - molecular wt = 10",
        "4 - Curve for total jet dispersion above 10<sup>5</sup> N/m<sup>2</sup> - molecular wt = 100",
    ]
    for i, line in enumerate(legend):
        o.append(TM(140, 292 + i * 11, line, 6.0, anchor="start", color=INK))

    o.append(TM(x0 + W, 388, "Differential pressure", 7.2,
                anchor="end", color=INK))
    o.append(TM(x0 + W, 399, "(P<sub>e</sub> − P<sub>a</sub>)", 7.2,
                anchor="end", color=INK))
    o.append(T(340, 431,
               "Văn bản in đảo nhầm đường 2 và 3; chú thích trên hình là mục xác thực / "
               "Printed prose swaps curves 2 and 3; the legend is authoritative",
               6.4, color=GREY))
    o.append(T(340, 454,
               "Hình 4.1 · Mức độ phơi nhiễm / "
               "Figure 4.1 · Extent of hazardous area",
               7.0, color=INK))

    return _fig(svg(w, h, "".join(o),
                    esc("Đồ thị log-log: mức độ phơi nhiễm theo áp suất chênh lệch "
                        "với bốn đường tăng dần được đánh số 1 đến 4 và chú thích bốn dòng")),
                "Hình 4.1 · Phạm vi vùng nguy hiểm theo áp suất chênh lệch. "
                "Văn bản in trên trang 102 đảo nhầm đường 2 và 3; chú thích in trên "
                "hình là mục xác thực.",
                "Figure 4.1 · Extent of hazardous area relative to wind dispersion "
                "versus differential pressure. The printed prose swaps curves 2 and 3; "
                "the printed four-line legend is authoritative.",
                "Đồ thị log-log có bốn đường tăng dần, đánh số 1 đến 4 ở đầu phải; "
                "trục tung từ 0,01 đến 10, trục hoành từ 2×10^3 đến 10^7 N/m²; "
                "chú thích bốn dòng nằm trong phần dưới của đồ thị.",
                "Log-log chart with four rising curves numbered 1 to 4 at their right "
                "ends; ordinate 0.01 to 10, abscissa 2×10^3 to 10^7 N/m²; a four-line "
                "legend sits in the lower part of the plot.")


@_reg
def fig_f402():
    """Figure 4.2 - Geometry of gas release formed hazardous area."""
    w, h = 680, 420
    o = [_defs(), _rect(0, 0, w, h, fill=PAPER, sw=0)]
    o.append(T(340, 18,
               "Hình 4.2 · Hình học vùng nguy hiểm do phát thải khí / "
               "Figure 4.2 · Geometry of gas release formed hazardous area",
               8.8, color=INK, weight="600"))
    o.append(T(340, 32,
               "Bản vẽ đường nét, không gạch chéo; các số 1, 2, 3 là chú giải / "
               "Unhatched line drawing; numbers 1, 2, 3 are the printed callouts",
               6.6, color=GREY))

    # Dimension 3: witness lines at the source and the far arc.
    o.append(_line(166, 62, 166, 98, sw=0.8, color=GREY))
    o.append(_line(600, 62, 600, 98, sw=0.8, color=GREY))
    o.append(_arrow(169, 75, 597, 75, sw=0.9, color=GREY, head="a7"))
    o.append(_arrow(597, 75, 169, 75, sw=0.9, color=GREY, head="a7"))
    o.append(T(383, 67, "3", 8.6, color=INK, weight="600"))

    # Diverging wedge closed by a convex arc.
    o.append(_line(166, 206, 556, 112, sw=1.3, color=INK))
    o.append(_line(166, 238, 556, 332, sw=1.3, color=INK))
    o.append(_path("M 556 112 C 620 150, 620 294, 556 332",
                   fill="none", sw=1.3, color=INK))

    # Two inner lines bounding the turbulent-mixing envelope.
    o.append(_line(168, 215, 592, 196, sw=1.0, color=INK))
    o.append(_line(168, 230, 592, 250, sw=1.0, color=INK))

    # Pipe cross-section: unhatched double circle.
    o.append(_circle(150, 222, 17, fill=PAPER, sw=1.2))
    o.append(_circle(150, 222, 10, fill="none", sw=1.0))

    # Leaders and callout 1.
    o.append(T(62, 178, "Pipe or", 7.0, anchor="start", color=INK))
    o.append(T(62, 187, "similar", 7.0, anchor="start", color=INK))
    o.append(_arrow(112, 183, 137, 210, sw=0.9, color=GREY, head="a7"))
    o.append(T(62, 252, "Source of release", 7.0, anchor="start", color=INK))
    o.append(_arrow(118, 249, 146, 229, sw=0.9, color=GREY, head="a7"))
    o.append(T(118, 128, "1", 8.6, color=INK, weight="600"))
    o.append(_arrow(122, 134, 140, 207, sw=0.9, color=GREY, head="a7"))

    # Callout 2 points to both inner mixing-envelope lines.
    o.append(T(366, 104, "2", 8.6, color=INK, weight="600"))
    o.append(_arrow(366, 110, 370, 205, sw=0.9, color=GREY, head="a7"))
    o.append(_arrow(366, 110, 366, 236, sw=0.9, color=GREY, head="a7"))

    o.append(T(340, 380,
               "Hình 4.2 · Hình học vùng nguy hiểm do phát thải khí / "
               "Figure 4.2 · Geometry of gas release formed hazardous area",
               7.2, color=INK))
    o.append(T(340, 399,
               "(1) Giãn nở · (2) Vùng trộn rối · (3) Phạm vi vùng nguy hiểm / "
               "(1) Expansion · (2) Mixing envelope · (3) Extent of hazardous area",
               6.4, color=GREY))

    return _fig(svg(w, h, "".join(o),
                    esc("Bản vẽ đường nét: mặt cắt ống hai vòng tròn ở bên trái, "
                        "hình nêm mở rộng sang phải được đóng bằng cung lồi, hai đường "
                        "bao trộn bên trong và các số gọi 1, 2, 3")),
                "Hình 4.2 · Hình học của vùng nguy hiểm do phát thải khí. "
                "(1) Giãn nở nhanh của hơi khí khi giải phóng áp suất. "
                "(2) Bao vùng có khí dễ nổ trong quá trình trộn rối với không khí. "
                "(3) Phạm vi vùng nguy hiểm (thường được cộng thêm vào bán kính của ống "
                "hoặc vật tương tự để cho bán kính hình cầu do hướng rò rỉ thay đổi).",
                "Figure 4.2 · Geometry of gas release formed hazardous area. "
                "(1) Rapid gas vapour expansion on release of pressure. "
                "(2) Envelope within which explosive atmosphere exists during "
                "turbulent mixing with air. "
                "(3) Extent of hazardous area (normally added to pipe or similar "
                "radius to give sphere radius due to varying orientation of leak)",
                "Mặt cắt ống gồm hai vòng tròn ở bên trái có hai đường chỉ dẫn "
                "\"Pipe or similar\" và \"Source of release\". Từ miệng rò rỉ, một hình "
                "nêm mở rộng sang phải và được đóng bằng một cung lồi; hai đường bên "
                "trong tạo thành bao vùng trộn rối. Số 1 chỉ nguồn, số 2 chỉ hai đường "
                "bên trong, số 3 nằm trên đường kích thích thước ngang phía trên.",
                "A small double-circle pipe cross-section at left with leaders "
                "\"Pipe or similar\" and \"Source of release\". A wedge expands right "
                "and is closed by a convex arc; two inner lines bound the mixing "
                "envelope. Callout 1 points to the source, 2 to the two inner lines, "
                "and 3 to the horizontal dimension line above the wedge.")


@_reg
def fig_f403():
    """Figure 4.3 - Reynolds Number R^0.2 against pool area."""
    w, h = 680, 515
    o = [_defs(), _rect(0, 0, w, h, fill=PAPER, sw=0)]
    o.append(TM(340, 18,
                "Hình 4.3 · Số Reynolds R<sup>0.2</sup> theo diện tích vũng / "
                "Figure 4.3 · Reynolds Number R<sup>0.2</sup> against pool area",
                8.8, color=INK, weight="600"))
    o.append(T(340, 32,
               "Trục hoành logarit, trục tung tuyến tính 0 đến 40 / "
               "Logarithmic abscissa, linear ordinate 0 to 40",
               6.6, color=GREY))

    x0, x1, ytop, ybot = 84.0, 616.0, 60.0, 420.0
    W, H = x1 - x0, ybot - ytop

    def X(loga):
        return x0 + (loga + 1.0) / 5.0 * W

    def Y(v):
        return ybot - v / 40.0 * H

    for v in range(0, 41):
        yy = Y(v)
        major = (v % 10 == 0)
        o.append(_line(x0, yy, x1, yy,
                       sw=0.8 if major else 0.4,
                       color="#b9b4a8" if major else "#dcd8ce"))
        if major:
            o.append(T(x0 - 6, yy + 2.4, str(v), 6.8,
                       anchor="end", color=GREY))

    ticks = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 1, 2, 3, 4, 5, 6,
             10, 100, 1000, 10000]
    for a in ticks:
        xx = X(math.log10(a))
        o.append(_line(xx, ytop, xx, ybot, sw=0.7, color="#b9b4a8"))
        o.append(_line(xx, ybot, xx, ybot + 3, sw=0.8, color=INK))
        o.append(T(xx, ybot + 13, str(a), 6.6, color=GREY))
    for dec in range(-1, 4):
        for mant in range(2, 10):
            xx = X(math.log10(mant * 10.0 ** dec))
            o.append(_line(xx, ytop, xx, ybot, sw=0.4, color="#dedacf"))

    o.append(_line(x0, ytop, x0, ybot, sw=1.1, color=INK))
    o.append(_line(x0, ybot, x1, ybot, sw=1.1, color=INK))
    o.append(TM(x0 + 6, 50, "R<sup>0.2</sup>", 9.0, anchor="start", color=INK))
    o.append(TM(x1, 458, "Pool size (m<sup>2</sup>)", 8.0,
                anchor="end", color=INK))

    # Smooth monotone redraw of the single printed curve.
    anchors = [(-1.0, 8.0), (0.0, 10.0), (1.0, 14.0), (2.0, 19.0),
               (2.3, 20.0), (3.0, 24.0), (4.0, 29.0)]
    f = _pchip(anchors)
    pts = [(X(-1.0 + 5.0 * i / 300.0), Y(f(-1.0 + 5.0 * i / 300.0)))
           for i in range(301)]
    o.append(_poly(pts, fill="none", sw=1.8, color=INK))
    for a in (1, 2, 3):
        xx = X(math.log10(a))
        o.append(_line(xx, Y(f(math.log10(a))) - 2, xx, ybot - 4,
                       sw=0.6, dash="3 3", color="#b5b0a4"))

    o.append(TM(340, 485,
                "Hình 4.3 · Số Reynolds R<sup>0.2</sup> theo diện tích vũng / "
                "Figure 4.3 · Reynolds Number R<sup>0.2</sup> against pool area",
                7.0, color=INK))
    o.append(T(340, 503,
               "Đường đơn điệu tăng từ khoảng 8 đến 29 / "
               "Single rising curve from about 8 to 29",
               6.4, color=GREY))

    return _fig(svg(w, h, "".join(o),
                    esc("Đồ thị R mũ 0,2 theo diện tích vũng: trục tung tuyến tính "
                        "0 đến 40, trục hoành logarit 0,1 đến 10000, một đường tăng dần")),
                "Hình 4.3 · Số Reynolds R^0.2 theo diện tích vũng (m²). "
                "Một đường tăng dần từ khoảng 8 tại 0,1 m² đến khoảng 29 tại 10^4 m².",
                "Figure 4.3 · Reynolds Number R^0.2 against pool area (m²). "
                "A single rising curve from about 8 at 0.1 m² to about 29 at 10^4 m².",
                "Đồ thị có lưới dày: trục tung tuyến tính từ 0 đến 40 với các mốc "
                "0, 10, 20, 30, 40; trục hoành logarit từ 0,1 đến 10000 m²; một đường "
                "cong tăng dần duy nhất, có vài nét đứt mờ gần 1 đến 5 m².",
                "Dense grid chart: linear ordinate 0 to 40 with labels 0, 10, 20, "
                "30, 40; logarithmic abscissa 0.1 to 10000 m²; one smooth rising "
                "curve with a few faint dashed marks near 1 to 5 m².")
