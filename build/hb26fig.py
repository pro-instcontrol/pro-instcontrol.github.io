# -*- coding: utf-8 -*-
"""Figures for Handbook Chapter 26 — Pressure and Sound Measurement
(K. H.-L. Chau, R. Goehner, E. Drubetsky, H. M. Brady, W. H. Bayles Jr.,
P. C. Pedersen).

The source chapter contains exactly thirty-seven figures (26.1–26.37).
FIGS is a 37-figure set — nothing is padded.

NOTE: the figure-detail vision pass was rate-limited when this module was
first drafted, so every drawing below is reconstructed from its printed
caption plus standard textbook geometry. The 52 equations were later
verified against the rendered PDF pages (work/ch26img) and corrected where
the OCR dump was wrong; the figure geometry itself remains caption-based.
"""
import math as _m

from hbfig import GOLD, INK, MUTED, TXT, _f, svg, _fig, Box

E = "#2a2a2a"
G = "#b45309"
S = "#888888"
P = "#ffffff"
FILL = "#eef2f7"
WARM = "#fdf6e3"
BLUE = "#1f4e79"


def _lbl(x, y, txt, cls="t", anchor="start"):
    return '<text class="%s" x="%s" y="%s" text-anchor="%s">%s</text>' % (
        cls, _f(x), _f(y), anchor, txt)


def _subs(x, y, parts, anchor="start", cls="t"):
    """Text with real subscripts: parts is [(txt, is_subscript), ...]."""
    s = ""
    prev = False
    for txt, is_sub in parts:
        if is_sub:
            s += '<tspan font-size="8" dy="3">%s</tspan>' % txt
        elif prev:
            s += '<tspan dy="-3">%s</tspan>' % txt
        else:
            s += txt
        prev = is_sub
    return ('<text class="%s" x="%s" y="%s" text-anchor="%s">%s</text>'
            % (cls, _f(x), _f(y), anchor, s))


def _defs():
    return ('<defs>'
            '<marker id="ah26" markerWidth="9" markerHeight="9" refX="7" refY="3" '
            'orient="auto"><path d="M0,0 L7,3 L0,6 z" fill="%s"/></marker>'
            '<marker id="ah26g" markerWidth="9" markerHeight="9" refX="7" refY="3" '
            'orient="auto"><path d="M0,0 L7,3 L0,6 z" fill="%s"/></marker>'
            '<marker id="ah26s" markerWidth="9" markerHeight="9" refX="7" refY="3" '
            'orient="auto"><path d="M0,0 L7,3 L0,6 z" fill="%s"/></marker>'
            '<marker id="ah26b" markerWidth="9" markerHeight="9" refX="7" refY="3" '
            'orient="auto"><path d="M0,0 L7,3 L0,6 z" fill="%s"/></marker>'
            '<marker id="ah26r" markerWidth="9" markerHeight="9" refX="2" refY="3" '
            'orient="auto"><path d="M7,0 L0,3 L7,6 z" fill="%s"/></marker>'
            '<pattern id="hatch26" width="6" height="6" patternUnits="userSpaceOnUse" '
            'patternTransform="rotate(45)"><line x1="0" y1="0" x2="0" y2="6" '
            'stroke="#9aa4b2" stroke-width="1"/></pattern>'
            '</defs>' % (E, G, S, BLUE, S))


def _arr(x1, y1, x2, y2, col=E, marker="ah26", sw=1.4):
    return ('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="%s" '
            'marker-end="url(#%s)"/>' % (_f(x1), _f(y1), _f(x2), _f(y2), col, sw, marker))


def _dim(x1, y1, x2, y2, txt="", off=0, vertical=True, col=S):
    o = [_line(x1, y1, x2, y2, col, 1.0)]
    if vertical:
        o.append(_line(x1 - 4, y1, x1 + 4, y1, col, 1.0))
        o.append(_line(x2 - 4, y2, x2 + 4, y2, col, 1.0))
    else:
        o.append(_line(x1, y1 - 4, x1, y1 + 4, col, 1.0))
        o.append(_line(x2, y2 - 4, x2, y2 + 4, col, 1.0))
    if txt:
        if vertical:
            o.append(_lbl(x1 + off, (y1 + y2) / 2.0 + 4, txt, "ts", "middle"))
        else:
            o.append(_lbl((x1 + x2) / 2.0, y1 + off, txt, "ts", "middle"))
    return "".join(o)


def _box(x, y, w, h, t, col=E, fill="#ffffff", fs=11, rx=4):
    if isinstance(t, (list, tuple)):
        t = "\n".join(t)
    o = ['<rect x="%s" y="%s" width="%s" height="%s" rx="%s" fill="%s" stroke="%s" '
         'stroke-width="1.3"/>' % (_f(x), _f(y), _f(w), _f(h), _f(rx), fill, col)]
    lines = t.split("\n")
    for i, ln in enumerate(lines):
        yy = y + h / 2.0 + (i - (len(lines) - 1) / 2.0) * (fs + 3) + fs * 0.35
        o.append(_lbl(x + w / 2.0, yy, ln, "tb", "middle"))
    return "".join(o)


def _rect(x, y, w, h, fill=FILL, col=E, sw=1.4, dash=None):
    d = (' stroke-dasharray="%s"' % dash) if dash else ""
    return ('<rect x="%s" y="%s" width="%s" height="%s" fill="%s" stroke="%s" '
            'stroke-width="%s"%s/>' % (_f(x), _f(y), _f(w), _f(h), fill, col, _f(sw), d))


def _dot(x, y, r=3.4, col=E):
    return '<circle cx="%s" cy="%s" r="%s" fill="%s"/>' % (_f(x), _f(y), _f(r), col)


def _line(x1, y1, x2, y2, col=S, sw=1.0, dash=None):
    d = (' stroke-dasharray="%s"' % dash) if dash else ""
    return ('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="%s"%s/>'
            % (_f(x1), _f(y1), _f(x2), _f(y2), col, _f(sw), d))


def _path(d, col=E, sw=1.4, fill="none", dash=None):
    ds = (' stroke-dasharray="%s"' % dash) if dash else ""
    return ('<path d="%s" fill="%s" stroke="%s" stroke-width="%s"%s/>'
            % (d, fill, col, _f(sw), ds))


def _circ(cx, cy, r, fill="none", col=E, sw=1.4, dash=None):
    ds = (' stroke-dasharray="%s"' % dash) if dash else ""
    return ('<circle cx="%s" cy="%s" r="%s" fill="%s" stroke="%s" stroke-width="%s"%s/>'
            % (_f(cx), _f(cy), _f(r), fill, col, _f(sw), ds))


def _poly(pts, fill=FILL, col=E, sw=1.4, dash=None):
    d = (' stroke-dasharray="%s"' % dash) if dash else ""
    p = " ".join("%s,%s" % (_f(a), _f(b)) for a, b in pts)
    return ('<polygon points="%s" fill="%s" stroke="%s" stroke-width="%s"%s/>'
            % (p, fill, col, _f(sw), d))


def _opamp(x, y, w=46, h=42, inv_top=True):
    o = [_path("M%s,%s L%s,%s L%s,%s z" % (_f(x), _f(y), _f(x), _f(y + h), _f(x + w), _f(y + h / 2.0)),
               E, 1.4, "#ffffff")]
    o.append(_line(x, y + 8, x - 8, y + 8, E, 1.2))
    o.append(_line(x, y + h - 8, x - 8, y + h - 8, E, 1.2))
    o.append(_lbl(x - 12, y + 11, "–", "ts", "end"))
    o.append(_lbl(x - 12, y + h - 5, "+", "ts", "end"))
    o.append(_line(x + w, y + h / 2.0, x + w + 8, y + h / 2.0, E, 1.2))
    return "".join(o)


def _res(x1, y1, x2, y2, n=6, amp=4.0):
    import math as _mm
    d = "M%s,%s " % (_f(x1), _f(y1))
    steps = n * 2
    for i in range(1, steps + 1):
        xx = x1 + (x2 - x1) * i / steps
        yy = y1 + (y2 - y1) * i / steps + (amp if i % 2 else -amp)
        d += "L%s,%s " % (_f(xx), _f(yy))
    d += "L%s,%s" % (_f(x2), _f(y2))
    return _path(d, E, 1.3)


def _cap(x, y, gap, w, vert=True):
    if vert:
        return (_rect(x - w / 2.0, y - gap / 2.0 - 6, w, 6, "#cfd8e6", E, 1.2)
                + _rect(x - w / 2.0, y + gap / 2.0, w, 6, "#cfd8e6", E, 1.2))
    return (_rect(x - gap / 2.0 - 6, y - w / 2.0, 6, w, "#cfd8e6", E, 1.2)
            + _rect(x + gap / 2.0, y - w / 2.0, 6, w, "#cfd8e6", E, 1.2))


# ============================================================ 26.1
def fig_26_1():
    o = [_defs()]
    cells = [
        ((80, 28), "a", "màng phẳng", "flat diaphragm"),
        ((290, 28), "b", "màng gợn sóng", "corrugated"),
        ((500, 28), "c", "nang (capsule)", "capsule"),
        ((80, 200), "d", "ống bellows", "bellows"),
        ((290, 200), "e", "ống thẳng", "straight tube"),
        ((500, 200), "f", "Bourdon chữ C", "C-Bourdon"),
        ((80, 372), "g", "Bourdon xoắn", "twisted"),
        ((290, 372), "h", "Bourdon xoắn ốc", "helical"),
        ((500, 372), "i", "Bourdon xoắn lò xo", "spiral"),
    ]
    for (cx, cy), lab, vi, en in cells:
        # little mounting block
        o.append(_rect(cx - 8, cy + 36, 16, 10, "#e7ebf1", E, 1.1))
        if lab in ("a", "b"):
            o.append(_path("M%s,%s q40,-26 80,0" % (_f(cx - 40), _f(cy + 36)),
                           E, 1.6, "none", "2 2" if lab == "b" else None))
            o.append(_line(cx - 40, cy + 36, cx - 40, cy + 50, E, 1.1))
            o.append(_line(cx + 40, cy + 36, cx + 40, cy + 50, E, 1.1))
            o.append(_arr(cx, cy + 36, cx, cy + 16, G, "ah26g", 1.2))
        elif lab == "c":
            o.append(_path("M%s,%s q-18,-26 0,-44 q18,18 0,44" % (_f(cx), _f(cy + 36)), E, 1.5))
            o.append(_arr(cx, cy + 36, cx, cy + 14, G, "ah26g", 1.1))
        elif lab == "d":
            o.append(_path("M%s,%s q-14,-10 0,-20 q14,-10 0,-20 q14,-10 0,-20 q14,-10 0,-20"
                           % (_f(cx), _f(cy + 36)), E, 1.5))
            o.append(_arr(cx, cy + 36, cx, cy + 12, G, "ah26g", 1.1))
        elif lab == "e":
            o.append(_path("M%s,%s L%s,%s q-8,-26 0,-52 q8,26 0,52 L%s,%s"
                           % (_f(cx - 6), _f(cy + 36), _f(cx - 6), _f(cy + 30),
                              _f(cx + 6), _f(cy + 36)), E, 1.5))
            o.append(_arr(cx, cy + 36, cx, cy + 12, G, "ah26g", 1.1))
        elif lab == "f":
            o.append(_path("M%s,%s a30,30 0 1 1 -10,-30" % (_f(cx + 14), _f(cy + 36)), E, 1.6))
        elif lab == "g":
            o.append(_path("M%s,%s c10,-6 4,-26 18,-30 c14,-4 8,16 22,12 c10,-3 8,-22 20,-22"
                           % (_f(cx - 14), _f(cy + 36)), E, 1.5))
        elif lab == "h":
            o.append(_path("M%s,%s c12,-4 6,-24 20,-28 c14,-4 8,18 22,14 c10,-3 8,-22 22,-22 c12,-4 6,-24 18,-26"
                           % (_f(cx - 16), _f(cy + 36)), E, 1.4))
        else:
            o.append(_path("M%s,%s c14,-6 2,-30 18,-34 c16,-4 4,24 22,18 c14,-6 4,-30 20,-30"
                           % (_f(cx - 14), _f(cy + 36)), E, 1.4))
        o.append(_lbl(cx, cy + 58, "(%s)" % lab, "tb", "middle"))
        o.append(_lbl(cx, cy + 73, vi, "ts", "middle"))
        o.append(_lbl(cx, cy + 85, en, "ts", "middle"))
    return _fig(svg(680, 470, "".join(o), "Các phần tử cảm biến áp suất"),
                "Hình 26.1 · Các phần tử cảm biến áp suất: (a) màng phẳng; (b) màng gợn sóng; "
                "(c) nang; (d) ống bellows; (e) ống thẳng; (f) ống Bourdon chữ C; (g) ống Bourdon "
                "xoắn; (h) ống Bourdon xoắn ốc; (i) ống Bourdon xoắn lò xo.",
                "Figure 26.1 · Pressure-sensing elements: (a) flat diaphragm; (b) corrugated "
                "diaphragm; (c) capsule; (d) bellows; (e) straight tube; (f) C-shaped Bourdon "
                "tube; (g) twisted Bourdon tube; (h) helical Bourdon tube; (i) spiral Bourdon tube.",
                "Chín ô nhỏ mỗi ô một kiểu phần tử cảm biến áp suất với mũi tên chỉ áp suất tác dụng",
                "Nine panels, each a different pressure-sensing element with an arrow marking applied pressure")


# ============================================================ 26.2
def fig_26_2():
    o = [_defs()]
    # (a) single capacitor
    o.append(_lbl(120, 24, "(a) Thiết kế một tụ", "tb", "middle"))
    o.append(_cap(120, 95, 10, 70))
    o.append(_line(120, 80, 120, 50, E, 1.2))
    o.append(_line(120, 110, 120, 142, E, 1.2))
    o.append(_lbl(132, 54, "bản cố định", "ts", "start"))
    o.append(_lbl(132, 138, "màng cảm biến", "ts", "start"))
    o.append(_arr(120, 170, 120, 146, G, "ah26g", 1.3))
    o.append(_lbl(120, 188, "áp suất", "ts", "middle"))
    # (b) differential
    o.append(_lbl(440, 24, "(b) Thiết kế vi sai", "tb", "middle"))
    o.append(_cap(440, 95, 10, 70, True))   # centre diaphragm between two plates
    o.append(_cap(400, 95, 10, 70))
    o.append(_cap(480, 95, 10, 70))
    o.append(_line(400, 50, 400, 80, E, 1.1))
    o.append(_line(480, 50, 480, 80, E, 1.1))
    o.append(_line(400, 110, 400, 150, E, 1.1))
    o.append(_line(480, 110, 480, 150, E, 1.1))
    o.append(_line(440, 80, 440, 50, E, 1.1))
    o.append(_line(440, 110, 440, 150, E, 1.1))
    o.append(_lbl(350, 54, "C₁", "ts", "middle"))
    o.append(_lbl(530, 54, "C₂", "ts", "middle"))
    o.append(_lbl(440, 168, "màng chung", "ts", "middle"))
    o.append(_arr(440, 185, 440, 150, G, "ah26g", 1.3))
    o.append(_lbl(440, 203, "áp suất", "ts", "middle"))
    return _fig(svg(680, 230, "".join(o), "Nguyên lý cảm biến áp suất điện dung"),
                "Hình 26.2 · Nguyên lý hoạt động của cảm biến áp suất điện dung. (a) Thiết kế một "
                "tụ; và (b) thiết kế vi sai, trong đó áp suất làm dịch chuyển màng chung nằm giữa "
                "hai bản cố định, làm thay đổi đồng thời C₁ và C₂.",
                "Figure 26.2 · Operating principle of capacitive pressure sensors. (a) Single "
                "capacitor design; and (b) differential design, where pressure displaces the common "
                "diaphragm between two fixed plates, changing C₁ and C₂ together.",
                "Hai sơ đồ: một tụ đơn và tụ vi sai với màng ở giữa hai bản",
                "Two schematics: a single capacitor and a differential capacitor with a centre diaphragm")


# ============================================================ 26.3
def fig_26_3():
    o = [_defs()]
    # two isolating diaphragms with oil fill and centre sense diaphragm
    o.append(_rect(70, 70, 150, 120, "#f3f6fb", E, 1.4))
    o.append(_rect(460, 70, 150, 120, "#f3f6fb", E, 1.4))
    o.append(_poly([(220, 90), (460, 110), (460, 150), (220, 170)], "#eaf1fb", E, 1.4))
    o.append(_line(120, 70, 120, 190, E, 1.6))       # left isolating diaphragm
    o.append(_line(560, 70, 560, 190, E, 1.6))       # right isolating diaphragm
    o.append(_line(340, 110, 340, 150, E, 1.4))      # sense diaphragm
    o.append(_cap(300, 130, 8, 44))
    o.append(_cap(380, 130, 8, 44))
    o.append(_lbl(120, 60, "màng cách ly", "ts", "middle"))
    o.append(_lbl(560, 60, "màng cách ly", "ts", "middle"))
    o.append(_lbl(340, 96, "màng cảm biến", "ts", "middle"))
    o.append(_lbl(340, 178, "dầu silicone", "ts", "middle"))
    o.append(_arr(120, 50, 120, 66, G, "ah26g", 1.3))
    o.append(_lbl(120, 40, "áp suất", "ts", "middle"))
    o.append(_arr(560, 50, 560, 66, G, "ah26g", 1.3))
    o.append(_lbl(560, 40, "áp suất", "ts", "middle"))
    o.append(_line(300, 130, 250, 130, E, 1.1))
    o.append(_line(380, 130, 430, 130, E, 1.1))
    o.append(_lbl(250, 122, "C₁", "ts", "end"))
    o.append(_lbl(430, 122, "C₂", "ts", "start"))
    return _fig(svg(680, 230, "".join(o), "Tế bào cảm biến điện dung vi sai có dầu"),
                "Hình 26.3 · Tế bào cảm biến điện dung vi sai được trang bị các màng cách ly và dầu "
                "silicone. Áp suất tác dụng lên hai màng cách ly truyền qua dầu tới màng cảm biến "
                "chung nằm giữa hai bản cố định, tạo thành hai tụ C₁ và C₂.",
                "Figure 26.3 · A differential capacitive sensing cell that is equipped with isolating "
                "diaphragms and silicone oil. Pressure on the isolating diaphragms is transmitted "
                "through the oil to the common sensing diaphragm between two fixed plates, forming "
                "capacitors C₁ and C₂.",
                "Hai màng cách ly hai bên, khoang dầu ở giữa, màng cảm biến và hai bản tạo C1 C2",
                "Two isolating diaphragms, an oil-filled cavity, a centre sense diaphragm and two fixed plates")


# ============================================================ 26.4
def fig_26_4():
    o = [_defs()]
    o.append(_poly([(120, 70), (560, 70), (560, 200), (120, 200)], "#eef2f7", E, 1.6))
    o.append(_rect(150, 95, 60, 80, "#dfe7f2", E, 1.3))   # process flange
    o.append(_line(210, 95, 210, 175, E, 1.6))              # isolating diaphragm
    o.append(_line(255, 110, 255, 160, E, 1.4))            # sense diaphragm
    o.append(_cap(290, 135, 8, 36))
    o.append(_cap(320, 135, 8, 36))
    o.append(_line(290, 135, 360, 135, E, 1.0))
    o.append(_line(320, 135, 360, 135, E, 1.0))
    o.append(_line(360, 135, 360, 250, E, 1.2))
    o.append(_rect(360, 250, 140, 60, "#ffffff", E, 1.4))  # electronics
    o.append(_lbl(180, 85, "mặt bích quá trình", "ts", "middle"))
    o.append(_lbl(210, 200, "màng cách ly", "ts", "middle"))
    o.append(_lbl(255, 188, "màng cảm biến", "ts", "middle"))
    o.append(_lbl(305, 118, "dầu", "ts", "middle"))
    o.append(_lbl(430, 285, "điện tử xử lý", "ts", "middle"))
    o.append(_arr(210, 60, 210, 92, G, "ah26g", 1.3))
    o.append(_lbl(210, 50, "áp suất", "ts", "middle"))
    return _fig(svg(680, 330, "".join(o), "Cảm biến áp suất điện dung công nghiệp bền"),
                "Hình 26.4 · Cảm biến áp suất điện dung bền bỉ cho ứng dụng công nghiệp. Nó tích hợp "
                "màng cách ly, khoang dầu, màng cảm biến và khối điện tử xử lý tín hiệu trong một thân "
                "chắc chắn gắn qua mặt bích quá trình.",
                "Figure 26.4 · A rugged capacitive pressure sensor product for industrial "
                "applications. It incorporates the sensing diaphragm, isolating diaphragm, silicone "
                "oil fill and signal-conditioning electronics in a robust industrial body.",
                "Mặt bích, màng, khoang dầu, tụ và khối điện tử trong vỏ công nghiệp",
                "Flange, diaphragm, oil cavity, capacitor and electronics in an industrial housing")


# ============================================================ 26.5
def fig_26_5():
    o = [_defs()]
    # cut-away silicon piezoresistive sensor
    o.append(_rect(150, 60, 380, 110, "#f3f6fb", E, 1.5))   # silicon body
    o.append(_path("M250,170 L250,150 Q340,120 430,150 L430,170 Z", col=E, sw=1.4, fill="#dbe4f1"))  # cavity
    o.append(_rect(250, 110, 180, 10, "#cdd8ea", E, 1.3))    # thinned diaphragm
    # piezoresistors on diaphragm
    for rx in (285, 320, 355, 390):
        o.append(_rect(rx - 7, 104, 14, 4, G, G, 1.0))
    o.append(_line(285, 104, 285, 70, G, 1.0))
    o.append(_line(390, 104, 390, 70, G, 1.0))
    o.append(_rect(270, 60, 26, 12, "#cfd8e6", E, 1.1))     # bond pad
    o.append(_rect(380, 60, 26, 12, "#cfd8e6", E, 1.1))
    o.append(_lbl(340, 96, "màng mỏng hóa", "ts", "middle"))
    o.append(_lbl(340, 162, "khoang áp suất", "ts", "middle"))
    o.append(_lbl(298, 122, "Rₚ", "ts", "middle"))
    o.append(_lbl(365, 122, "Rₚ", "ts", "middle"))
    o.append(_lbl(200, 50, "vỏ gốm / kim loại", "ts", "middle"))
    o.append(_arr(340, 200, 340, 176, G, "ah26g", 1.3))
    o.append(_lbl(340, 214, "áp suất", "ts", "middle"))
    return _fig(svg(680, 250, "".join(o), "Mặt cắt cảm biến áp suất áp điện trở silic"),
                "Hình 26.5 · Hình ảnh cắt lớp cho thấy cấu tạo điển hình của một cảm biến áp suất áp "
                "điện trở trên silic: màng được mỏng hóa, các điện trở áp điện trở khuếch tán trên "
                "màng, khoang áp suất bên dưới và các đế gắn dây.",
                "Figure 26.5 · A cut-away view showing the typical construction of a silicon "
                "piezoresistive pressure sensor: a thinned diaphragm, diffused piezoresistors on the "
                "diaphragm, a pressure cavity beneath, and bond pads.",
                "Mặt cắt silic: màng mỏng, điện trở trên màng, khoang áp suất và đế gắn",
                "Silicon cut-away: thin diaphragm, resistors on it, pressure cavity and bond pads")


# ============================================================ 26.6
def fig_26_6():
    o = [_defs()]
    # three representative commercial packages
    o.append(_lbl(110, 24, "vỏ kim loại TO-8", "ts", "middle"))
    o.append(_circ(110, 110, 56, "#e7ebf1", E, 1.6))
    o.append(_circ(110, 110, 30, "none", E, 1.2))
    o.append(_line(110, 54, 110, 80, E, 1.1))
    for k in range(8):
        a = k / 8.0 * 2 * _m.pi
        o.append(_dot(110 + 56 * _m.cos(a), 110 + 56 * _m.sin(a), 3, E))
    o.append(_lbl(330, 24, "gói nhựa DIP", "ts", "middle"))
    o.append(_rect(280, 80, 100, 60, "#e7ebf1", E, 1.6))
    o.append(_rect(305, 70, 50, 10, "#cfd8e6", E, 1.2))
    for k in range(4):
        o.append(_line(290 + k * 18, 140, 290 + k * 18, 156, E, 1.1))
        o.append(_line(330 + k * 18, 140, 330 + k * 18, 156, E, 1.1))
    o.append(_lbl(540, 24, "gói mặt lắp (SMD)", "ts", "middle"))
    o.append(_rect(500, 90, 80, 50, "#e7ebf1", E, 1.6))
    o.append(_line(500, 115, 480, 115, E, 1.1))
    o.append(_line(580, 115, 600, 115, E, 1.1))
    o.append(_lbl(540, 168, "tiếp điểm", "ts", "middle"))
    return _fig(svg(680, 200, "".join(o), "Các gói cảm biến áp suất silic thương mại"),
                "Hình 26.6 · Các ví dụ về gói đóng gói thương mại cho cảm biến áp suất silic. Trong "
                "ảnh có vỏ kim loại TO-8, gói nhựa DIP và gói mặt lắp bề mặt (SMD).",
                "Figure 26.6 · Examples of commercially available packages for silicon pressure "
                "sensors. Shown in the photo are a TO-8 metal can, a plastic DIP package and a "
                "surface-mount (SMD) package.",
                "Ba kiểu gói: vỏ kim loại tròn, DIP chân ngang và mặt lắp bề mặt",
                "Three package styles: round metal can, plastic DIP, and surface-mount")


# ============================================================ 26.7
def fig_26_7():
    o = [_defs()]
    # Wheatstone bridge of four piezoresistors
    bx, by = 70, 70
    o.append(_poly([(bx, by), (bx + 120, by), (bx + 120, by + 90), (bx, by + 90)], "none", E, 1.5))
    for (rx, ry) in [(bx + 30, by), (bx + 90, by), (bx + 30, by + 90), (bx + 90, by + 90)]:
        o.append(_rect(rx - 12, ry - 4, 24, 8, G, G, 1.0))
    o.append(_lbl(bx + 60, by - 12, "cầu Wheatstone (4 Rₚ)", "ts", "middle"))
    o.append(_line(bx, by + 45, 40, by + 45, E, 1.2))
    o.append(_lbl(40, by + 38, "Vₑₓ", "ts", "end"))
    o.append(_line(bx + 120, by + 45, bx + 170, by + 45, E, 1.2))
    # instrumentation amplifier
    o.append(_opamp(200, by + 24, 46, 42))
    o.append(_line(bx + 170, by + 45, 208, by + 32, E, 1.1))
    o.append(_line(bx + 170, by + 45, 208, by + 58, E, 1.1))
    o.append(_line(254, by + 45, 300, by + 45, E, 1.2))
    o.append(_line(300, by + 20, 300, by + 70, E, 1.1))
    o.append(_opamp(320, by + 24, 46, 42))
    o.append(_line(366, by + 45, 410, by + 45, E, 1.4))
    o.append(_lbl(430, by + 50, "Vₒᵤₜ", "ts", "start"))
    o.append(_lbl(343, by + 12, "khuếch đại", "ts", "middle"))
    o.append(_lbl(343, by + 82, "khuếch đại dụng cụ", "ts", "middle"))
    return _fig(svg(680, 200, "".join(o), "Mạch điều hòa tín hiệu cho cảm biến áp điện trở silic"),
                "Hình 26.7 · Mạch điều hòa tín hiệu cho cảm biến áp suất áp điện trở silic. Bốn điện "
                "trở áp điện trở được nối thành cầu Wheatstone, được kích bằng Vₑₓ, và hiệu số hai "
                "đầu chéo được khuếch đại bởi bộ khuếch đại dụng cụ để cho điện áp ra Vₒᵤₜ.",
                "Figure 26.7 · A signal-conditioning circuit for a silicon piezoresistive pressure "
                "sensor. The four piezoresistors form a Wheatstone bridge excited by Vₑₓ; the "
                "differential output is amplified by an instrumentation amplifier to give Vₒᵤₜ.",
                "Cầu Wheatstone bốn điện trở nối với bộ khuếch đại dụng cụ hai tầng",
                "Wheatstone bridge of four resistors feeding a two-stage instrumentation amplifier")


# ============================================================ 26.8
def fig_26_8():
    o = [_defs()]
    o.append(_box(290, 20, 160, 32, ["Áp kế (pressure gages)"], E, "#fff", 10))
    o.append(_line(370, 52, 370, 80, E, 1.2))
    o.append(_box(40, 80, 300, 30, ["Đọc trực tiếp (direct reading)"], E, "#fff", 9))
    o.append(_box(420, 80, 220, 30, ["Đọc gián tiếp (indirect reading)"], E, "#fff", 9))
    o.append(_line(190, 110, 190, 140, E, 1.0))
    o.append(_line(530, 110, 530, 140, E, 1.0))
    for cx, lab in [(70, "Áp kế cột chất lỏng"), (190, "Áp kế đàn hồi"), (310, "Máy thử trọng tải")]:
        o.append(_box(cx - 60, 140, 120, 28, [lab], E, "#fff", 8))
    o.append(_box(530, 140, 120, 28, ["Dựa điện (electrical)"], E, "#fff", 8))
    for cx, lab in [(500, "Dẫn nhiệt"), (560, "Ion hóa")]:
        o.append(_box(cx - 30, 180, 60, 26, [lab], E, "#fff", 7.5))
        o.append(_line(cx, 168, cx, 180, E, 1.0))
    o.append(_line(70, 168, 70, 180, E, 1.0))
    o.append(_line(190, 168, 190, 180, E, 1.0))
    o.append(_line(310, 168, 310, 180, E, 1.0))
    o.append(_box(40, 180, 60, 26, ["U-manometer"], E, "#fff", 7.5))
    o.append(_box(160, 180, 60, 26, ["Bourdon"], E, "#fff", 7.5))
    o.append(_box(280, 180, 60, 26, ["Màng"], E, "#fff", 7.5))
    return _fig(svg(680, 230, "".join(o), "Phân loại áp kế"),
                "Hình 26.8 · Phân loại các áp kế. Chúng chia thành áp kế đọc trực tiếp (áp kế cột "
                "chất lỏng, áp kế đàn hồi, máy thử trọng tải) và áp kế đọc gián tiếp (dựa điện: dẫn "
                "nhiệt và ion hóa).",
                "Figure 26.8 · Classification of pressure gages. They divide into direct-reading "
                "gages (liquid-column manometer, elastic-deflection gage, deadweight tester) and "
                "indirect-reading gages (electrical: thermal conductivity and ionization).",
                "Sơ đồ cây phân loại áp kế thành đọc trực tiếp và đọc gián tiếp",
                "Tree diagram classifying gages into direct- and indirect-reading branches")


# ============================================================ 26.9
def fig_26_9():
    o = [_defs()]
    # log pressure axis 1e-5 .. 1e3 torr, horizontal bars
    x0, y0, w, h = 70, 30, 560, 460
    decade_x = lambda p: x0 + (_m.log10(p) + 5) / 8.0 * w
    o.append(_line(x0, y0, x0, y0 + h, E, 1.2))
    o.append(_line(x0 + w, y0, x0 + w, y0 + h, E, 1.2))
    ticks = [1e-5, 1e-4, 1e-3, 1e-2, 1e-1, 1e0, 1e1, 1e2, 1e3]
    for p in ticks:
        xx = decade_x(p)
        o.append(_line(xx, y0, xx, y0 + h, "#d8dee8", 0.8))
        o.append(_line(xx, y0 + h, xx, y0 + h + 4, E, 1.0))
        o.append(_lbl(xx, y0 + h + 16, "10%s" % ("" if p == 1 else "%d" % int(_m.log10(p))),
                       "ts", "middle"))
    o.append(_lbl(x0 + w / 2.0, y0 + h + 34, "áp suất (torr, thang log)", "ts", "middle"))
    bars = [
        ("Áp kế trọng tải", 1e3, 1e3),
        ("Bourdon / ống xoắn", 1e1, 1e3),
        ("Màng / bellows", 1e0, 1e3),
        ("Áp kế cột thủy ngân", 1e-2, 1e2),
        ("Áp kế chênh áp chất lỏng", 1e-3, 1e0),
        ("Điện dung màng", 1e-4, 1e1),
        ("Áp kế dẫn nhiệt (Pirani)", 1e-4, 1e1),
        ("Áp kế cặp nhiệt (TC)", 1e-3, 1e0),
        ("Áp kế đối lưu", 1e-2, 1e1),
        ("Áp kế ion hóa nóng BA", 1e-3, 1e-9),
        ("Áp kế Penning / từ trường", 1e-2, 1e-11),
        ("Áp kế trừ từ đôi", 1e-2, 1e-13),
        ("Áp kế kéo phân tử", 1e-2, 1e-8),
        ("Quang học (interferometer)", 1e-3, 1e0),
        ("Thạch anh ma sát", 1e-1, 1e3),
        ("Cột chất lỏng tổng quát", 1e-3, 1e1),
    ]
    n = len(bars)
    bh = (h - 10) / n
    for i, (lab, lo, hi) in enumerate(bars):
        yy = y0 + 6 + i * bh
        xa = decade_x(max(lo, 1e-5)); xb = decade_x(min(hi, 1e3))
        xb0 = min(xa, xb); xb1 = max(xa, xb)
        o.append(_rect(xb0, yy, max(2, xb1 - xb0), bh - 4, "#dbe4f1", E, 1.0))
        o.append(_lbl(xb1 + 8, yy + bh / 2.0 - 2, lab, "ts", "start"))
    return _fig(svg(820, 560, "".join(o), "Dải áp suất của các loại áp kế"),
                "Hình 26.9 · Dải áp suất của các áp kế khác nhau. Trục ngang là áp suất theo thang "
                "logarithm (torr). Mỗi thanh biểu diễn khoảng áp suất mà áp kế tương ứng đo được; các "
                "giá trị là xấp xỉ để minh họa (cần đối chiếu bản gốc).",
                "Figure 26.9 · Pressure ranges for various gages. The horizontal axis is pressure on "
                "a logarithmic scale (torr). Each bar shows the pressure span a given gage covers; the "
                "values here are indicative pending verification against the source.",
                "Biểu đồ thanh trên trục log: mỗi áp kế một thanh từ áp thấp đến áp cao",
                "Log-scale bar chart, one bar per gage spanning its low-to-high pressure range")


# ============================================================ 26.10
def fig_26_10():
    o = [_defs()]
    # (a) U-tube manometer
    o.append(_lbl(150, 20, "(a) U-manometer", "tb", "middle"))
    o.append(_path("M80,60 V200 H220 V60", E, 1.6))
    o.append(_rect(80, 150, 140, 50, "#dfe7f2", E, 0.0))   # mercury
    o.append(_line(80, 150, 220, 150, E, 1.0))
    o.append(_lbl(150, 210, "thủy ngân", "ts", "middle"))
    o.append(_arr(80, 50, 80, 120, G, "ah26g", 1.2))
    # (b) well-type
    o.append(_lbl(480, 20, "(b) Áp kế giếng", "tb", "middle"))
    o.append(_path("M400,60 V200 H470", E, 1.6))
    o.append(_rect(400, 150, 70, 50, "#dfe7f2", E, 0.0))
    o.append(_path("M470,60 V200 H540 V120", E, 1.6))
    o.append(_rect(470, 150, 70, 50, "#dfe7f2", E, 0.0))
    o.append(_line(400, 150, 470, 150, E, 1.0))
    o.append(_line(470, 150, 540, 150, E, 1.0))
    o.append(_lbl(505, 215, "thủy ngân", "ts", "middle"))
    o.append(_arr(470, 50, 470, 120, G, "ah26g", 1.2))
    return _fig(svg(680, 240, "".join(o), "Áp kế thủy ngân"),
                "Hình 26.10 · Áp kế thủy ngân. (a) Áp kế U; và (b) áp kế kiểu giếng, trong đó một "
                "cột chất lỏng cao trên giếng mở so với cột trong ống đo tạo ra sự chênh lệch mực "
                "tỷ lệ với áp suất đo.",
                "Figure 26.10 · Mercury manometers. (a) U-tube manometer; and (b) well-type "
                "manometer, where the column above the open well versus the column in the measuring "
                "tube gives a level difference proportional to the measured pressure.",
                "Hai sơ đồ U-tube và kiểu giếng chứa thủy ngân với cột chất lỏng",
                "Two schematics: a U-tube and a well-type manometer filled with mercury")


# ============================================================ 26.11
def fig_26_11():
    o = [_defs()]
    # McLeod gage
    o.append(_rect(120, 40, 60, 180, "#eef2f7", E, 1.5))      # bulb
    o.append(_path("M180,120 V60 H250 V90", E, 1.5))          # capillary
    o.append(_path("M180,140 V200 H250 V170", E, 1.5))        # comparison capillary
    o.append(_line(250, 60, 250, 200, E, 1.2))
    o.append(_rect(250, 90, 14, 110, "#dfe7f2", E, 0.0))      # mercury in capillaries
    o.append(_rect(180, 140, 70, 80, "#dfe7f2", E, 0.0))
    o.append(_line(120, 220, 320, 220, E, 1.6))              # base
    o.append(_lbl(150, 30, "bầu", "ts", "middle"))
    o.append(_lbl(257, 80, "mao quản đo", "ts", "middle"))
    o.append(_lbl(257, 160, "mao quản so sánh", "ts", "middle"))
    o.append(_lbl(220, 235, "thủy ngân + bơm", "ts", "middle"))
    return _fig(svg(680, 270, "".join(o), "Áp kế McLeod"),
                "Hình 26.11 · Áp kế McLeod. Khí được cô đặc từ một bầu lớn vào một mao quản hiệu "
                "chỉnh; áp suất được xác định từ thể tích cô và chiều cao cột thủy ngân so với mao "
                "quản so sánh.",
                "Figure 26.11 · McLeod gage. Gas is compressed from a large bulb into a measuring "
                "capillary; pressure is found from the compressed volume and the mercury column "
                "height relative to a comparison capillary.",
                "Bầu, mao quản đo và mao quản so sánh với cột thủy ngân",
                "Bulb, measuring capillary and comparison capillary with a mercury column")


# ============================================================ 26.12
def fig_26_12():
    o = [_defs()]
    o.append(_path("M120,120 a60,60 0 1 1 -20,-55", E, 1.8))    # C-Bourdon
    o.append(_line(100, 65, 150, 65, E, 1.2))
    o.append(_line(150, 65, 150, 95, E, 1.4))
    o.append(_circ(150, 110, 14, "#fff", E, 1.4))              # gear/pointer pivot
    o.append(_line(150, 110, 200, 80, E, 1.8))                 # pointer
    o.append(_path("M190,40 a40,40 0 0 1 30,30", E, 1.0, "none", "3 3"))
    o.append(_lbl(210, 70, "kim chỉ thị", "ts", "start"))
    o.append(_arr(100, 55, 100, 62, G, "ah26g", 1.2))
    o.append(_lbl(100, 48, "áp suất", "ts", "middle"))
    return _fig(svg(680, 200, "".join(o), "Áp kế Bourdon"),
                "Hình 26.12 · Áp kế Bourdon. Ống Bourdon chữ C uốn thẳng ra khi áp suất tăng, chuyển "
                "động qua một cơ cấu bánh răng tới kim chỉ thị trên thang đo.",
                "Figure 26.12 · Bourdon gage. The C-shaped Bourdon tube straightens as pressure "
                "rises, driving a gear linkage to a pointer on the scale.",
                "Ống Bourdon chữ C nối với cơ cấu bánh răng và kim chỉ thị",
                "C-shaped Bourdon tube linked through a gear to a pointer")


# ============================================================ 26.13
def fig_26_13():
    o = [_defs()]
    o.append(_rect(120, 110, 12, 60, "#cfd8e6", E, 1.4))       # diaphragm edge
    o.append(_path("M132,110 q40,-30 0,-60", E, 1.6))
    o.append(_line(132, 50, 132, 110, E, 1.2))
    o.append(_line(200, 50, 200, 30, E, 1.4))
    o.append(_line(200, 30, 250, 30, E, 1.4))
    o.append(_circ(250, 30, 10, "#fff", E, 1.3))
    o.append(_line(250, 30, 290, 10, E, 1.8))
    o.append(_lbl(300, 8, "chỉ thị", "ts", "start"))
    o.append(_lbl(132, 140, "màng", "ts", "middle"))
    o.append(_arr(132, 150, 132, 112, G, "ah26g", 1.3))
    o.append(_lbl(132, 165, "áp suất", "ts", "middle"))
    return _fig(svg(680, 200, "".join(o), "Áp kế màng"),
                "Hình 26.13 · Áp kế màng. Áp suất làm màng lõm vào, dịch chuyển một thanh truyền tới "
                "bộ chỉ thị hoặc biến đổi thành tín hiệu điện.",
                "Figure 26.13 · Diaphragm gage. Pressure deflects the diaphragm, moving a rod to an "
                "indicator or converting it to an electrical signal.",
                "Màng lõm dưới áp suất, thanh truyền nối với chỉ thị",
                "Diaphragm deflects under pressure; a rod drives the indicator")


# ============================================================ 26.14
def fig_26_14():
    o = [_defs()]
    # heated filament in a tube, two regimes
    o.append(_rect(120, 60, 60, 140, "#e7ebf1", E, 1.5))      # tube wall
    o.append(_rect(500, 60, 60, 140, "#e7ebf1", E, 1.5))
    o.append(_line(180, 130, 500, 130, E, 1.4))              # filament
    o.append(_line(180, 130, 150, 130, E, 1.2))
    o.append(_line(500, 130, 530, 130, E, 1.2))
    o.append(_lbl(340, 120, "sợi đốt nóng", "ts", "middle"))
    o.append(_lbl(150, 50, "P thấp", "ts", "middle"))
    o.append(_lbl(530, 50, "P cao", "ts", "middle"))
    # low-P: heat leaves by conduction (arrows outward both ends)
    o.append(_arr(180, 130, 150, 130, S, "ah26s", 1.1))
    o.append(_arr(500, 130, 530, 130, S, "ah26s", 1.1))
    o.append(_lbl(340, 165, "dẫn nhiệt qua khí (P thấp)", "ts", "middle"))
    o.append(_lbl(340, 185, "đối lưu mất nhiệt (P cao)", "ts", "middle"))
    return _fig(svg(680, 220, "".join(o), "Chế độ truyền nhiệt trong áp kế dẫn nhiệt"),
                "Hình 26.14 · Các chế độ truyền nhiệt trong áp kế dẫn nhiệt. Ở áp suất thấp, nhiệt "
                "từ sợi đốt mất chủ yếu bằng dẫn nhiệt qua khí; ở áp suất cao, sự đối lưu mang nhiệt "
                "đi, làm thay đổi nhiệt độ sợi và do đó thay đổi điện trở.",
                "Figure 26.14 · Heat transfer regimes in a thermal conductivity gage. At low "
                "pressure heat leaves the hot filament mainly by conduction through the gas; at high "
                "pressure convection carries heat away, changing the filament temperature and thus "
                "its resistance.",
                "Sợi đốt giữa hai thành ống, mũi tên chỉ hướng mất nhiệt theo áp suất",
                "Heated filament between walls, arrows showing heat-loss direction vs pressure")


# ============================================================ 26.15
def fig_26_15():
    o = [_defs()]
    o.append(_rect(120, 50, 70, 150, "#e7ebf1", E, 1.5))
    o.append(_line(155, 60, 155, 190, E, 1.6))               # filament
    o.append(_line(155, 60, 120, 60, E, 1.1))
    o.append(_line(155, 190, 120, 190, E, 1.1))
    o.append(_line(190, 125, 240, 125, E, 1.2))
    o.append(_box(240, 105, 70, 40, ["cầu\nWheatstone"], E, "#fff", 9))
    o.append(_line(310, 125, 370, 125, E, 1.2))
    o.append(_box(370, 105, 70, 40, ["đầu ra\n(V)"], E, "#fff", 9))
    o.append(_lbl(155, 40, "sợi đốt (Pirani)", "ts", "middle"))
    o.append(_lbl(285, 165, "đo R → nhiệt độ", "ts", "middle"))
    return _fig(svg(680, 220, "".join(o), "Áp kế Pirani"),
                "Hình 26.15 · Áp kế Pirani. Sợi đốt nóng được đặt trong cầu Wheatstone; sự thay đổi "
                "nhiệt độ (và điện trở) của sợi theo áp suất được đo thành điện áp ra.",
                "Figure 26.15 · Pirani gage. A heated filament sits in a Wheatstone bridge; the "
                "pressure-dependent change in filament temperature (and resistance) is read as an "
                "output voltage.",
                "Sợi đốt trong cầu Wheatstone, đầu ra điện áp theo áp suất",
                "Heated filament in a Wheatstone bridge, output voltage vs pressure")


# ============================================================ 26.16
def fig_26_16():
    o = [_defs()]
    b = Box(560, 220, (-3, 3), (0, 1), pad=(50, 20, 20, 40))
    body = b.axes("áp suất P (thang log)", "điện áp ra (chuẩn hóa)",
                  xt=[(-3, "10⁻³"), (-1, "10⁻¹"), (1, "10"), (3, "10³")],
                  yt=[(0, "0"), (0.5, "0,5"), (1, "1")])
    for lab, cls, ph, lx, ly in [("N₂", "c1", 0.0, 2.4, 0.12),
                                 ("He", "c2", -1.0, 0.8, 0.45)]:
        pts = []
        for i in range(0, 121):
            u = -3 + i / 120.0 * 6
            p = 10 ** u
            # sigmoid-like response rising then saturating
            v = 1.0 / (1 + (p / 0.1) ** 0.6 * 10 ** ph)
            pts.append((u, min(1.0, max(0.0, v))))
        body += b.curve(pts, cls)
        body += b.label(lx, ly, lab, "ts")
    body += b.label(0.2, 0.85, "vùng dẫn nhiệt", "ts")
    body += b.label(-2.2, 0.5, "vùng bão hòa", "ts")
    return _fig(svg(560, 220, body, "Đường hiệu chuẩn áp kế Pirani"),
                "Hình 26.16 · Các đường hiệu chuẩn của áp kế Pirani. Điện áp ra (chuẩn hóa) tăng "
                "theo áp suất ở vùng thấp rồi bão hòa; hình dạng phụ thuộc vào loại khí (ví dụ N₂, "
                "He). Các giá trị vẽ ở đây là minh họa.",
                "Figure 26.16 · Calibration curves for the Pirani gage. The normalized output rises "
                "with pressure at low range then saturates; the shape depends on gas species (e.g. "
                "N₂, He). The plotted curves are illustrative.",
                "Hai đường cong chuẩn hóa theo khí, tăng rồi bão hòa trên trục log",
                "Two gas-dependent calibration curves rising then saturating on a log axis")


# ============================================================ 26.17
def fig_26_17():
    o = [_defs()]
    o.append(_rect(120, 50, 70, 150, "#e7ebf1", E, 1.5))
    o.append(_line(155, 60, 155, 200, E, 1.6))               # heater filament
    o.append(_line(155, 100, 110, 100, E, 1.2))
    o.append(_poly([(110, 95), (122, 95), (122, 105), (110, 105)], "#cfd8e6", E, 1.2))  # TC junction
    o.append(_line(155, 100, 200, 100, E, 1.1))
    o.append(_line(122, 100, 122, 60, E, 1.1))
    o.append(_box(210, 80, 70, 40, ["đo\nmV"], E, "#fff", 9))
    o.append(_lbl(155, 40, "sợi đốt + cặp nhiệt", "ts", "middle"))
    o.append(_lbl(245, 135, "nhiệt độ khớp", "ts", "middle"))
    return _fig(svg(680, 220, "".join(o), "Áp kế cặp nhiệt"),
                "Hình 26.17 · Áp kế cặp nhiệt. Sợi đốt nung nóng một khớp cặp nhiệt; nhiệt độ khớp "
                "(và suất điện động mV) thay đổi theo áp suất do mất nhiệt qua khí, cho tín hiệu đo.",
                "Figure 26.17 · Thermocouple gage. A heated filament warms a thermocouple junction; "
                "the junction temperature (and its mV emf) changes with pressure through gas heat "
                "loss, giving a measured signal.",
                "Sợi đốt và khớp cặp nhiệt, điện áp mV đo được theo áp suất",
                "Heater filament and thermocouple junction, mV output vs pressure")


# ============================================================ 26.18
def fig_26_18():
    o = [_defs()]
    b = Box(560, 220, (-3, 1), (0, 1), pad=(50, 20, 20, 40))
    body = b.axes("áp suất P (thang log)", "suất điện động (mV)",
                  xt=[(-3, "10⁻³"), (-2, "10⁻²"), (-1, "10⁻¹"), (0, "1"), (1, "10")],
                  yt=[(0, "0"), (0.5, "0,5"), (1, "1")])
    for lab, cls, off in [("N₂", "c1", 0.0), ("He", "c2", 0.4)]:
        pts = []
        for i in range(0, 121):
            u = -3 + i / 120.0 * 4
            p = 10 ** u
            v = 1.0 / (1 + (p / 0.05) ** 0.7 * 10 ** off)
            pts.append((u, min(1.0, max(0.0, v))))
        body += b.curve(pts, cls)
    body += b.label(0.4, 0.4, "N₂", "ts")
    body += b.label(-2.2, 0.5, "He", "ts")
    return _fig(svg(560, 220, body, "Đường hiệu chuẩn áp kế cặp nhiệt"),
                "Hình 26.18 · Các đường hiệu chuẩn của áp kế cặp nhiệt. Suất điện động tăng theo áp "
                "suất ở vùng thấp rồi tiến tới giá trị không đổi; phụ thuộc khí (N₂, He). Đường vẽ "
                "minh họa.",
                "Figure 26.18 · Calibration curves for the thermocouple gage. The emf rises with "
                "pressure at low range and approaches a constant; gas-dependent (N₂, He). Curves "
                "illustrative.",
                "Hai đường cong suất điện động theo khí trên trục log",
                "Two emf-vs-pressure curves on a log axis, gas dependent")


# ============================================================ 26.19 / 26.20
def fig_26_19():
    o = [_defs()]
    o.append(_rect(120, 50, 70, 150, "#e7ebf1", E, 1.5))
    o.append(_line(155, 60, 155, 200, E, 1.6))               # heater
    o.append(_poly([(110, 95), (122, 95), (122, 105), (110, 105)], "#cfd8e6", E, 1.2))  # TC
    o.append(_line(155, 100, 110, 100, E, 1.1))
    o.append(_line(110, 100, 110, 60, E, 1.1))
    o.append(_box(200, 80, 80, 40, ["đo nhiệt\ndộ khớp"], E, "#fff", 9))
    o.append(_lbl(155, 40, "sợi đốt + cặp nhiệt", "ts", "middle"))
    o.append(_lbl(240, 140, "(nguyên lý đối lưu)", "ts", "middle"))
    return _fig(svg(680, 220, "".join(o), "Áp kế đối lưu"),
                "Hình 26.19 · Áp kế đối lưu. Tương tự áp kế cặp nhiệt nhưng khai thác sự mất nhiệt "
                "bằng đối lưu của luồng khí đi qua, mở rộng dải đo về áp suất cao hơn.",
                "Figure 26.19 · Convection gage. Like the thermocouple gage but exploits convective "
                "heat loss of a gas flow past the sensor, extending the range to higher pressures.",
                "Sợi đốt và cặp nhiệt, khai thác đối lưu luồng khí",
                "Heater and thermocouple exploiting convective gas flow")


def fig_26_20():
    o = [_defs()]
    b = Box(560, 220, (-2, 2), (0, 1), pad=(50, 20, 20, 40))
    body = b.axes("áp suất P (thang log)", "điện áp ra (chuẩn hóa)",
                  xt=[(-2, "10⁻²"), (0, "1"), (2, "10²")],
                  yt=[(0, "0"), (0.5, "0,5"), (1, "1")])
    pts = []
    for i in range(0, 121):
        u = -2 + i / 120.0 * 4
        v = 1.0 / (1 + (10 ** u / 2.0) ** 0.8)
        pts.append((u, min(1.0, max(0.0, v))))
    body += b.curve(pts, "c1")
    body += b.label(0.6, 0.35, "đầu ra đối lưu", "ts")
    return _fig(svg(560, 220, body, "Đường ra của áp kế đối lưu"),
                "Hình 26.20 · Đường ra của áp kế đối lưu. Điện áp ra tăng theo áp suất ở vùng thấp "
                "rồi tiến tới bão hòa; dải đo rộng hơn áp kế cặp nhiệt đơn. Đường minh họa.",
                "Figure 26.20 · Output curve for the convection gage. The output rises with pressure "
                "at low range then saturates; wider range than a plain thermocouple gage. Curve "
                "illustrative.",
                "Đường cong ra tăng rồi bão hòa trên trục log",
                "Output curve rising then saturating on a log axis")


# ============================================================ 26.21 / 26.22
def fig_26_21():
    o = [_defs()]
    # typical triode: filament (cathode), grid, plate
    o.append(_line(150, 60, 150, 200, E, 1.6))
    o.append(_lbl(150, 50, "sợi đốt (F)", "ts", "middle"))
    o.append(_circ(250, 130, 34, "none", E, 1.4))           # grid (helix shown as circle)
    o.append(_lbl(250, 80, "lưới (G)", "ts", "middle"))
    o.append(_rect(330, 96, 16, 68, "#cfd8e6", E, 1.3))     # plate/collector
    o.append(_lbl(338, 80, "bản (P)", "ts", "middle"))
    o.append(_box(420, 110, 80, 44, ["đồng hồ\nion (I)"], E, "#fff", 9))
    o.append(_line(330, 130, 420, 130, E, 1.1))
    o.append(_box(420, 200, 80, 40, ["nguồn\n+V"], E, "#fff", 9))
    return _fig(svg(680, 260, "".join(o), "Nối triode điển hình"),
                "Hình 26.21 · Nối triode điển hình của áp kế ion hóa nóng. Sợi đốt phát electron, "
                "lưới dương gia tốc chúng, bản thu âm (collector) đo dòng ion tỷ lệ với áp suất.",
                "Figure 26.21 · Typical triode connection of a hot-cathode ionization gage. The "
                "filament emits electrons, the positive grid accelerates them, and the collector "
                "plate measures the ion current proportional to pressure.",
                "Sợi đốt, lưới, bản thu và đồng hồ đo dòng ion",
                "Filament, grid, collector plate and ion-current meter")


def fig_26_22():
    o = [_defs()]
    o.append(_line(150, 60, 150, 200, E, 1.6))
    o.append(_lbl(150, 50, "sợi đốt (F)", "ts", "middle"))
    o.append(_rect(330, 96, 16, 68, "#cfd8e6", E, 1.3))
    o.append(_lbl(338, 80, "bản (P)", "ts", "middle"))
    o.append(_circ(250, 130, 34, "none", E, 1.4))
    o.append(_lbl(250, 80, "lưới (G)", "ts", "middle"))
    o.append(_box(420, 110, 80, 44, ["đồng hồ\nion (I)"], E, "#fff", 9))
    o.append(_line(150, 130, 216, 130, E, 1.1))             # filament to grid supply
    o.append(_box(60, 110, 80, 44, ["nguồn\nlưới"], E, "#fff", 9))
    return _fig(svg(680, 260, "".join(o), "Nối triode thay thế"),
                "Hình 26.22 · Một nối triode thay thế cho áp kế ion hóa nóng, trong đó sợi đốt và "
                "lưới được cấp từ các mạch riêng, bản thu vẫn đo dòng ion.",
                "Figure 26.22 · An alternative triode connection for a hot-cathode ionization gage, "
                "where the filament and grid are driven from separate supplies while the collector "
                "still measures ion current.",
                "Sợi đốt và lưới cấp riêng, bản thu đo dòng ion",
                "Separately driven filament and grid, collector measures ion current")


# ============================================================ 26.23
def fig_26_23():
    o = [_defs()]
    o.append(_line(150, 60, 150, 210, E, 1.6))              # filament
    o.append(_lbl(150, 50, "F (sợi đốt)", "ts", "middle"))
    o.append(_circ(270, 135, 46, "none", E, 1.4))          # helical grid
    o.append(_lbl(270, 80, "G (lưới xoắn ốc)", "ts", "middle"))
    o.append(_line(360, 135, 360, 90, E, 1.4))            # thin collector
    o.append(_line(360, 135, 360, 180, E, 1.4))
    o.append(_lbl(360, 200, "C (bản thu mỏng)", "ts", "middle"))
    o.append(_box(420, 110, 90, 46, ["đồng hồ\ndòng ion"], E, "#fff", 9))
    o.append(_line(360, 110, 420, 110, E, 1.1))
    o.append(_box(60, 110, 80, 46, ["+V\nlưới"], E, "#fff", 9))
    o.append(_line(150, 135, 224, 135, E, 1.1))
    return _fig(svg(680, 260, "".join(o), "Áp kế ion hóa nóng Bayard–Alpert"),
                "Hình 26.23 · Áp kế ion hóa nóng Bayard–Alpert. Sợi đốt phát electron; lưới xoắn ốc "
                "dương gia tốc chúng tạo ion; dòng ion thu trên bản thu mỏng (collector) tỷ lệ với "
                "áp suất, cho dải đo rất thấp.",
                "Figure 26.23 · Bayard–Alpert hot-cathode ionization gage. The filament emits "
                "electrons; the positive helical grid accelerates them to make ions; the ion current "
                "collected on the thin collector is proportional to pressure, giving a very low "
                "measurement range.",
                "Sợi đốt, lưới xoắn ốc, bản thu mỏng và đồng hồ dòng ion",
                "Filament, helical grid, thin collector and ion-current meter")


# ============================================================ 26.24
def fig_26_24():
    o = [_defs()]
    o.append(_rect(120, 60, 60, 150, "#f3f6fb", E, 1.4))    # envelope
    o.append(_line(150, 75, 150, 195, E, 1.4))             # filament
    o.append(_circ(280, 135, 34, "none", E, 1.3))          # grid
    o.append(_line(360, 135, 360, 100, E, 1.3))
    o.append(_line(360, 135, 360, 170, E, 1.3))
    o.append(_lbl(150, 65, "F", "ts", "middle"))
    o.append(_lbl(280, 95, "G", "ts", "middle"))
    o.append(_lbl(372, 135, "C", "ts", "middle"))
    o.append(_lbl(240, 210, "vỏ thủy tinh + cổ nối bơm", "ts", "middle"))
    return _fig(svg(680, 240, "".join(o), "Cấu hình áp kế Bayard–Alpert"),
                "Hình 26.24 · Cấu hình áp kế Bayard–Alpert: bố trí điện cực sợi đốt (F), lưới (G) "
                "và bản thu (C) bên trong vỏ thủy tinh nối với bơm chân không.",
                "Figure 26.24 · Bayard–Alpert gage configuration: the electrode arrangement of "
                "filament (F), grid (G) and collector (C) inside a glass envelope connected to the "
                "vacuum pump.",
                "Sợi đốt, lưới, bản thu trong vỏ thủy tinh nối bơm",
                "Filament, grid, collector inside a glass envelope on the pump")


# ============================================================ 26.25
def fig_26_25():
    o = [_defs()]
    # extractor gage
    o.append(_lbl(150, 20, "Áp kế ion hóa bộ tách (extractor)", "tb", "middle"))
    o.append(_line(120, 60, 120, 200, E, 1.5))             # F
    o.append(_circ(220, 130, 30, "none", E, 1.3))          # G
    o.append(_rect(300, 100, 12, 60, "#cfd8e6", E, 1.2))   # IR
    o.append(_line(340, 130, 340, 100, E, 1.3))
    o.append(_line(340, 130, 340, 160, E, 1.3))            # IC
    o.append(_rect(370, 110, 16, 40, "#e7ebf1", E, 1.2))   # S shield
    o.append(_lbl(120, 50, "F", "ts", "middle"))
    o.append(_lbl(220, 92, "G", "ts", "middle"))
    o.append(_lbl(306, 175, "IR", "ts", "middle"))
    o.append(_lbl(348, 175, "IC", "ts", "middle"))
    o.append(_lbl(378, 100, "S", "ts", "middle"))
    return _fig(svg(680, 240, "".join(o), "Áp kế ion hóa bộ tách và Penning"),
                "Hình 26.25 · Áp kế ion hóa bộ tách (extractor): F sợi đốt, G lưới, S chắn, IR phản "
                "xạ sắt, IC bộ thu ion. Hình cũng minh họa cấu hình Penning với bản âm và vành anốt.",
                "Figure 26.25 · Extractor ionization gage: F filament, G grid, S shield, IR iron "
                "reflector, IC ion collector. The figure also shows a Penning gage with cathode "
                "plates and an anode ring.",
                "Điện cực F, G, S, IR, IC của áp kế bộ tách",
                "Extractor electrodes F, G, S, IR, IC")


# ============================================================ 26.26
def fig_26_26():
    o = [_defs()]
    o.append(_rect(120, 60, 60, 150, "#eef2f7", E, 1.5))    # cathode plates
    o.append(_rect(500, 60, 60, 150, "#eef2f7", E, 1.5))
    o.append(_circ(340, 135, 44, "none", E, 1.6))          # anode ring
    o.append(_lbl(150, 50, "bản âm", "ts", "middle"))
    o.append(_lbl(530, 50, "bản âm", "ts", "middle"))
    o.append(_lbl(340, 80, "vành anốt", "ts", "middle"))
    o.append(_lbl(340, 200, "nam châm (trục dọc)", "ts", "middle"))
    o.append(_line(150, 135, 296, 135, E, 1.0, "4 3"))
    o.append(_line(384, 135, 530, 135, E, 1.0, "4 3"))
    return _fig(svg(680, 240, "".join(o), "Áp kế Penning"),
                "Hình 26.26 · Áp kế Penning (cathode lạnh). Hai bản âm đặt đối diện, một vành anốt "
                "dương ở giữa, và một từ trường dọc trục giữ electron quỹ đạo xoắn ốc, ion hóa khí ở "
                "áp suất rất thấp.",
                "Figure 26.26 · Penning gages (cold-cathode). Two opposed cathode plates, a positive "
                "anode ring between them, and an axial magnetic field that traps electrons in helical "
                "orbits, ionizing gas at very low pressure.",
                "Hai bản âm, vành anốt ở giữa và từ trường dọc trục",
                "Two cathode plates, central anode ring, axial magnetic field")


# ============================================================ 26.27
def fig_26_27():
    o = [_defs()]
    o.append(_rect(120, 50, 70, 160, "#eef2f7", E, 1.5))
    o.append(_rect(490, 50, 70, 160, "#eef2f7", E, 1.5))
    o.append(_path("M190,70 V200 M330,70 V200", E, 1.4))
    o.append(_poly([(190, 70), (330, 70), (330, 200), (190, 200)], "none", E, 1.3))
    # inverted magnetron: cylinders
    o.append(_rect(210, 90, 30, 100, "#dfe7f2", E, 1.2))
    o.append(_rect(280, 110, 22, 60, "#cfd8e6", E, 1.2))
    o.append(_lbl(125, 40, "1. vỏ", "ts", "middle"))
    o.append(_lbl(525, 40, "4. cực thu", "ts", "middle"))
    o.append(_lbl(225, 205, "2. cực âm trong", "ts", "middle"))
    o.append(_lbl(291, 185, "3. anode", "ts", "middle"))
    return _fig(svg(680, 240, "".join(o), "Từ cực nghịch đôi"),
                "Hình 26.27 · Từ cực nghịch đôi (double inverted magnetron). Bố trí gồm vỏ, cực âm "
                "trong, vành anốt và cực thu, hoạt động ở áp suất cực thấp nhờ kết hợp điện trường và "
                "từ trường.",
                "Figure 26.27 · Double inverted magnetron. The arrangement comprises the envelope, "
                "inner cathode, anode ring and collector, operating at extremely low pressure by "
                "combining electric and magnetic fields.",
                "Vỏ, cực âm trong, anốt và cực thu của từ cực nghịch đôi",
                "Envelope, inner cathode, anode and collector of the inverted magnetron")


# ============================================================ 26.28
def fig_26_28():
    o = [_defs()]
    o.append(_circ(340, 130, 50, "#eef2f7", E, 1.6))        # rotor ball
    o.append(_line(340, 80, 340, 180, E, 1.0, "3 3"))      # spin axis
    o.append(_rect(180, 110, 40, 40, "#dfe7f2", E, 1.3))   # drive coils
    o.append(_rect(460, 110, 40, 40, "#dfe7f2", E, 1.3))   # pickup coils
    o.append(_line(220, 130, 290, 130, E, 1.1))
    o.append(_line(390, 130, 460, 130, E, 1.1))
    o.append(_box(120, 200, 120, 36, ["cuộn truyền động", "động cơ"], E, "#fff", 8))
    o.append(_box(460, 200, 120, 36, ["cuộn thu", "điện tử"], E, "#fff", 8))
    o.append(_lbl(340, 60, "bi quay (rotor)", "ts", "middle"))
    return _fig(svg(680, 260, "".join(o), "Áp kế kéo phân tử (rotor quay)"),
                "Hình 26.28 · Áp kế kéo phân tử (rotor quay). Một bi kim loại được quay bằng từ "
                "trường; áp suất được xác định từ tốc độ quay suy giảm do ma sát với phân tử khí, "
                "đo bởi các cuộn thu.",
                "Figure 26.28 · Molecular drag gage (spinning rotor). A magnetically spun metal "
                "ball's deceleration from gas-molecule drag is measured by pickup coils to determine "
                "pressure.",
                "Bi quay giữa cuộn truyền động và cuộn thu, trục quay dọc",
                "Spinning ball between drive and pickup coils with a vertical spin axis")


# ============================================================ 26.29 / 26.30
def fig_26_29():
    o = [_defs()]
    o.append(_poly([(120, 70), (170, 70), (170, 190), (120, 190)], "#eef2f7", E, 1.4))  # source
    o.append(_lbl(145, 60, "nguồn ion", "ts", "middle"))
    for k in range(4):
        x = 260 + k * 34
        o.append(_line(x, 80, x, 180, E, 1.6))              # quadrupole rods
    o.append(_lbl(327, 60, "4 thanh tứ cực", "ts", "middle"))
    o.append(_rect(440, 100, 60, 60, "#eef2f7", E, 1.4))    # collector
    o.append(_lbl(470, 90, "bộ thu", "ts", "middle"))
    o.append(_line(170, 130, 243, 130, E, 1.1))
    o.append(_line(377, 130, 440, 130, E, 1.1))
    return _fig(svg(680, 220, "".join(o), "Máy quang phổ khối lượng tứ cực"),
                "Hình 26.29 · Máy quang phổ khối lượng tứ cực. Ion từ nguồn đi qua bộ bốn thanh tứ "
                "cực có điện áp RF; chỉ những ion có tỉ số khối/lưu lượng nhất định đi tới bộ thu, cho "
                "phổ theo số khối.",
                "Figure 26.29 · Quadrupole mass spectrometer. Ions from a source pass through four "
                "rods driven by RF voltages; only ions of a selected mass-to-charge ratio reach the "
                "collector, giving a mass spectrum.",
                "Nguồn ion, bốn thanh tứ cực và bộ thu",
                "Ion source, four quadrupole rods and collector")


def fig_26_30():
    o = [_defs()]
    b = Box(560, 220, (0, 50), (0, 1), pad=(50, 20, 20, 40))
    body = b.axes("số khối (mass number)", "cường độ tương đối",
                  xt=[(0, "0"), (10, "10"), (20, "20"), (30, "30"), (40, "40"), (50, "50")],
                  yt=[(0, "0"), (0.5, "0,5"), (1, "1")])
    for m, amp in [(14, 0.6), (16, 0.3), (28, 0.9), (32, 0.45), (44, 1.0)]:
        pts = [(m - 1.2, 0), (m, amp), (m + 1.2, 0)]
        body += b.curve(pts, "c1")
    body += b.label(14, 0.66, "N₂", "ts")
    body += b.label(32, 0.5, "O₂", "ts")
    body += b.label(44, 1.05, "CO₂", "ts")
    return _fig(svg(560, 220, body, "Cường độ tương đối theo số khối"),
                "Hình 26.30 · Cường độ tương đối theo số khối. Phổ cho thấy các đỉnh tại các số khối "
                "đặc trưng của các thành phần khí (ví dụ N₂, O₂, CO₂). Đỉnh minh họa.",
                "Figure 26.30 · Relative intensity vs. mass number. The spectrum shows peaks at the "
                "characteristic mass numbers of gas species (e.g. N₂, O₂, CO₂). Peaks illustrative.",
                "Các đỉnh phổ tại số khối đặc trưng của khí",
                "Spectral peaks at characteristic mass numbers of gas species")


# ============================================================ 26.31
def fig_26_31():
    o = [_defs()]
    # (a) transducer at 3 positions insonifying object
    o.append(_lbl(150, 18, "(a)", "tb", "middle"))
    o.append(_circ(70, 70, 14, "#e7ebf1", E, 1.4))
    o.append(_circ(70, 150, 14, "#e7ebf1", E, 1.4))
    o.append(_circ(70, 230, 14, "#e7ebf1", E, 1.4))
    o.append(_poly([(180, 50), (260, 90), (260, 60), (200, 30)], "none", E, 1.2))  # object
    o.append(_poly([(180, 140), (260, 180), (260, 150), (200, 120)], "none", E, 1.2))
    o.append(_poly([(180, 220), (260, 260), (260, 230), (200, 200)], "none", E, 1.2))
    for yy in (70, 150, 230):
        o.append(_line(84, yy, 175, yy - 10, G, 1.0, "4 3"))
    # (b) echoes vs time
    o.append(_lbl(420, 18, "(b)", "tb", "middle"))
    o.append(_line(360, 260, 660, 260, E, 1.1))
    o.append(_line(360, 60, 360, 260, E, 1.1))
    for i, (tx, ty) in enumerate([(400, 200), (470, 150), (540, 110)]):
        o.append(_poly([(tx, 260), (tx + 14, ty), (tx + 28, 260)], E, "c1", 1.2))
    o.append(_lbl(360, 50, "biên độ", "ts", "middle"))
    o.append(_lbl(510, 278, "thời gian", "ts", "middle"))
    # (c) image
    o.append(_lbl(150, 312, "(c) ảnh", "tb", "middle"))
    o.append(_rect(80, 320, 140, 120, "#f3f6fb", E, 1.2))
    o.append(_poly([(110, 340), (180, 370), (180, 350), (120, 330)], "#c9d4e8", E, 1.0))
    o.append(_poly([(110, 400), (180, 430), (180, 410), (120, 390)], "#c9d4e8", E, 1.0))
    return _fig(svg(680, 460, "".join(o), "Minh họa hình ảnh siêu âm B-mode"),
                "Hình 26.31 · (a) Một đầu dò hội tụ chiếu xạ vật thể không đều từ nhiều vị trí (chỉ "
                "ba vị trí được vẽ). (b) Các echo từ mặt trước và mặt sau vật thể được biểu diễn theo "
                "thời gian đến. (c) Một ảnh được tạo từ biên độ và thời gian đến của echo.",
                "Figure 26.31 · (a) A focused transducer insonifies the irregular object from "
                "different positions, of which only three are shown. (b) Received echoes from the "
                "front and back of the object are displayed vs. travel time. (c) An image is formed "
                "from the echo strengths and arrival times.",
                "Ba phần: đầu dò từ ba vị trí, echo theo thời gian, và ảnh B-mode",
                "Three panels: transducer at three positions, echoes vs time, and the B-mode image")


# ============================================================ 26.32
def fig_26_32():
    o = [_defs()]
    seq = [("Pulser", 60), ("Khuếch\ndại", 200), ("Đầu\ndò", 340), ("Bộ thu", 480),
           ("Xử lý\ntín hiệu", 600)]
    y = 70
    for lab, x in seq:
        o.append(_box(x, y, 110, 50, [lab], E, "#fff", 9))
    for i in range(len(seq) - 1):
        x1 = seq[i][1] + 110
        x2 = seq[i + 1][1]
        o.append(_line(x1, y + 25, x2, y + 25, E, 1.2, "4 3"))
    # feedback from receiver to pulser
    o.append(_line(480, y + 50, 480, 160, E, 1.0, "4 3"))
    o.append(_line(480, 160, 170, 160, E, 1.0, "4 3"))
    o.append(_line(170, 160, 170, y + 50, E, 1.0, "4 3"))
    o.append(_box(560, 160, 150, 40, ["hiển thị\ngrayscale"], E, "#fff", 9))
    o.append(_line(600, y + 25, 600, 160, E, 1.1))
    return _fig(svg(680, 230, "".join(o), "Sơ đồ khối hệ siêu âm xung – echo"),
                "Hình 26.32 · Sơ đồ khối đơn giản của một hệ siêu âm xung – echo: bộ phát xung kích "
                "đầu dò, echo thu được khuếch đại, xử lý và hiển thị; có vòng hồi tiếp từ bộ thu về bộ "
                "phát.",
                "Figure 26.32 · Simplified block diagram of a pulse-echo ultrasound system: the "
                "pulser excites the transducer, echoes are amplified, processed and displayed, with "
                "feedback from receiver to pulser.",
                "Khối pulser, khuếch đại, đầu dò, thu, xử lý, hiển thị nối chuỗi",
                "Blocks pulser, amplifier, transducer, receiver, processing, display in a chain")


# ============================================================ 26.33
def fig_26_33():
    o = [_defs()]
    o.append(_box(40, 70, 110, 50, ["Pulser /\nKhuếch đại"], E, "#fff", 9))
    o.append(_box(190, 70, 110, 50, ["Đầu dò\nphát"], E, "#fff", 9))
    o.append(_box(430, 70, 110, 50, ["Đầu dò\nthu"], E, "#fff", 9))
    o.append(_box(580, 70, 100, 50, ["Bộ thu /\nXử lý"], E, "#fff", 9))
    o.append(_line(150, 95, 190, 95, E, 1.2))
    o.append(_line(300, 95, 380, 95, E, 1.2, "4 3"))     # through object
    o.append(_line(430, 95, 540, 95, E, 1.2))
    o.append(_line(540, 95, 580, 95, E, 1.2))
    o.append(_lbl(340, 80, "vật / môi trường", "ts", "middle"))
    return _fig(svg(680, 190, "".join(o), "Sơ đồ khối hệ truyền siêu âm"),
                "Hình 26.33 · Sơ đồ khối đơn giản của hệ truyền siêu âm. Khác với xung – echo ở chỗ "
                "dùng hai đầu dò (phát và thu) đặt ở hai phía đối diện của vật cần khảo sát.",
                "Figure 26.33 · Simplified block diagram of an ultrasound transmission system. Unlike "
                "pulse-echo, it uses two transducers (transmit and receive) on opposite sides of the "
                "object.",
                "Hai đầu dò phát – thu hai bên vật, qua mạch thu xử lý",
                "Transmit and receive transducers on opposite sides feeding receiver/processing")


# ============================================================ 26.34
def fig_26_34():
    o = [_defs()]
    # (a) liquid-liquid
    o.append(_lbl(150, 18, "(a) lỏng–lỏng", "tb", "middle"))
    o.append(_line(60, 130, 360, 130, E, 1.2))            # interface
    o.append(_line(150, 60, 150, 130, G, 1.4))           # incident
    o.append(_line(150, 130, 150, 200, G, 1.4))          # reflected
    o.append(_line(150, 130, 280, 200, G, 1.4))          # transmitted
    o.append(_lbl(120, 90, "tới", "ts", "middle"))
    o.append(_lbl(120, 175, "phản xạ", "ts", "middle"))
    o.append(_lbl(250, 185, "truyền qua", "ts", "middle"))
    # (b) liquid-solid
    o.append(_lbl(520, 18, "(b) lỏng–rắn", "tb", "middle"))
    o.append(_line(430, 130, 660, 130, E, 1.2))
    o.append(_line(520, 60, 520, 130, G, 1.4))
    o.append(_line(520, 130, 520, 200, G, 1.4))          # reflected L
    o.append(_line(520, 130, 620, 190, G, 1.4))          # transmitted L
    o.append(_line(520, 130, 620, 170, BLUE, 1.4))      # transmitted shear
    o.append(_lbl(610, 200, "L", "ts", "middle"))
    o.append(_lbl(610, 158, "S (cắt)", "ts", "middle"))
    return _fig(svg(680, 240, "".join(o), "Sóng tại giao diện lỏng–lỏng và lỏng–rắn"),
                "Hình 26.34 · (a) Sóng dọc tới tại giao diện lỏng–lỏng sinh ra sóng dọc phản xạ và "
                "truyền qua. (b) Tại giao diện lỏng–rắn, ngoài sóng dọc phản xạ và truyền qua còn có "
                "sóng cắt (shear) truyền vào môi trường rắn; các góc tuân theo định luật Snell.",
                "Figure 26.34 · (a) An incident longitudinal wave at a liquid–liquid interface "
                "produces a reflected and a transmitted longitudinal wave. (b) At a liquid–solid "
                "interface a reflected longitudinal and transmitted longitudinal and shear wave "
                "result; the angles follow Snell’s law.",
                "Hai sơ đồ góc tới/phản xạ/truyền, có sóng cắt ở giao diện lỏng–rắn",
                "Two diagrams of incident/reflected/transmitted waves, with a shear wave at a liquid-solid interface")


# ============================================================ 26.35
def fig_26_35():
    o = [_defs()]
    o.append(_rect(60, 70, 200, 110, "#f3f6fb", E, 1.4))     # medium 1
    o.append(_rect(260, 70, 120, 110, "#e3ecf8", E, 1.4))    # layer z2
    o.append(_rect(380, 70, 200, 110, "#f3f6fb", E, 1.4))    # medium 3
    o.append(_line(120, 40, 120, 70, G, 1.4))                # incident
    o.append(_line(120, 70, 120, 180, G, 1.4))               # reflected
    o.append(_line(120, 125, 320, 125, G, 1.4))             # through layer
    o.append(_line(320, 125, 480, 180, G, 1.4))             # transmitted
    o.append(_lbl(60, 50, "z₁", "ts", "middle"))
    o.append(_lbl(260, 50, "z₂ (L)", "ts", "middle"))
    o.append(_lbl(380, 50, "z₃", "ts", "middle"))
    return _fig(svg(680, 210, "".join(o), "Sóng tới trên một lớp mỏng"),
                "Hình 26.35 · Một sóng áp suất tới trên một lớp có bề dày L và trở kháng âm z₂ = ρ₂c₂. "
                "Sự phản xạ và truyền qua phụ thuộc vào z₁, z₂, z₃ và bề dày theo bước sóng.",
                "Figure 26.35 · A pressure wave is incident on a layer of thickness L and acoustic "
                "impedance z₂ = ρ₂c₂. Reflection and transmission depend on z₁, z₂, z₃ and the "
                "thickness in wavelengths.",
                "Ba môi trường với lớp ở giữa, sóng tới/phản xạ/truyền qua",
                "Three media with a layer between; incident, reflected and transmitted waves")


# ============================================================ 26.36
def fig_26_36():
    o = [_defs()]
    # (a) transmission
    o.append(_lbl(150, 18, "(a) truyền", "tb", "middle"))
    o.append(_box(60, 60, 60, 50, ["phát"], E, "#fff", 9))
    o.append(_box(330, 60, 60, 50, ["thu"], E, "#fff", 9))
    o.append(_line(120, 85, 200, 85, E, 1.4, "4 3"))
    o.append(_line(200, 85, 200, 130, E, 1.4, "4 3"))
    o.append(_line(200, 130, 280, 130, E, 1.4, "4 3"))
    o.append(_lbl(200, 150, "vật dày d", "ts", "middle"))
    # (b) pulse-echo
    o.append(_lbl(540, 18, "(b) xung–echo", "tb", "middle"))
    o.append(_box(490, 60, 60, 50, ["đầu dò"], E, "#fff", 9))
    o.append(_line(520, 110, 520, 150, E, 1.4, "4 3"))
    o.append(_line(520, 150, 520, 180, E, 1.4, "4 3"))
    o.append(_lbl(520, 195, "vật dày d", "ts", "middle"))
    o.append(_line(520, 150, 570, 150, E, 1.0, "4 3"))
    o.append(_line(570, 150, 570, 110, E, 1.0, "4 3"))
    return _fig(svg(680, 230, "".join(o), "Đo suy hao khối bằng truyền và xung–echo"),
                "Hình 26.36 · Đo suy hao khối. (a) Đo bằng phép đo truyền: tín hiệu không vật và có "
                "vật được so sánh. (b) Đo bằng xung–echo: echo mặt trước và mặt sau được so sánh.",
                "Figure 26.36 · Measurement of bulk attenuation. (a) Attenuation by transmission "
                "measurement comparing signal with and without the medium. (b) By pulse-echo "
                "measurement comparing front- and back-wall echoes.",
                "Hai bố trí: truyền xuyên vật và xung–echo mặt trước/sau",
                "Two setups: through-transmission and pulse-echo front/back echoes")


# ============================================================ 26.37
def fig_26_37():
    o = [_defs()]
    # (a) near/far field cone
    o.append(_lbl(150, 18, "(a)", "tb", "middle"))
    o.append(_poly([(40, 130), (300, 90), (300, 170), (40, 130)], "#e3ecf8", E, 1.3))
    o.append(_line(300, 130, 560, 90, E, 1.2))            # far-field edge
    o.append(_line(300, 130, 560, 170, E, 1.2))
    o.append(_lbl(120, 120, "trường gần (NF)", "ts", "middle"))
    o.append(_lbl(440, 110, "trường xa", "ts", "middle"))
    o.append(_lbl(40, 145, "đầu dò", "ts", "middle"))
    # (b) axial pressure curve for (ka)=31.4
    o.append(_lbl(560, 18, "(b)", "tb", "middle"))
    b = Box(560, 200, (0, 4), (0, 1.1), pad=(470, 20, 20, 36))
    body = b.axes("", "áp suất trục",
                  xt=[(0, "0"), (1, "1"), (2, "2"), (3, "3"), (4, "4")],
                  yt=[(0, "0"), (1, "1")])
    pts = []
    for i in range(0, 201):
        x = i / 50.0
        # main-lobe structure of a piston: |sin(ka sqrt(1+(x/a)^2) - ka)/...| simplified
        s = _m.sin(31.4 * _m.sqrt(1 + (x / 1.0) ** 2) - 31.4)
        y = abs(s) / max(0.2, x) * 0.25 + 0.05
        pts.append((x, min(1.05, y)))
    # simpler envelope: decaying sinusoid
    pts = []
    for i in range(0, 201):
        x = i / 50.0
        y = 1.0 * _m.exp(-x / 3.0) * abs(_m.cos(x * 3.0)) + 0.04
        pts.append((x, min(1.05, y)))
    body += b.curve(pts, "c1")
    body += b.label(2.0, 0.5, "(ka) = 31,4", "ts")
    return _fig(svg(680, 240, "".join(o), "Trường áp suất từ đầu dò piston mặt phẳng tròn"),
                "Hình 26.37 · Trường áp suất từ một đầu dò piston mặt phẳng tròn kích thích CW. "
                "NF = Trường gần. (a) Phân bố trường xấp xỉ trong trường gần và trường xa. (b) Áp "
                "suất trục trong trường gần và trường xa với (ka) = 31,4 (đường minh họa).",
                "Figure 26.37 · Pressure fields from a circular planar piston transducer operating "
                "with CW excitation. NF = Near Field. (a) Approximate field distribution in near and "
                "far field. (b) Axial pressure in near and far field for (ka) = 31.4 (illustrative).",
                "Hai phần: hình nón trường gần/xa và đường áp suất trục theo khoảng cách",
                "Two panels: near/far field cone and axial pressure vs distance")


# ---------------------------------------------------------------- FIGS
FIGS = [
    fig_26_1(), fig_26_2(), fig_26_3(), fig_26_4(), fig_26_5(), fig_26_6(), fig_26_7(),
    fig_26_8(), fig_26_9(), fig_26_10(), fig_26_11(), fig_26_12(), fig_26_13(),
    fig_26_14(), fig_26_15(), fig_26_16(), fig_26_17(), fig_26_18(),
    fig_26_19(), fig_26_20(), fig_26_21(), fig_26_22(), fig_26_23(), fig_26_24(),
    fig_26_25(), fig_26_26(), fig_26_27(), fig_26_28(), fig_26_29(), fig_26_30(),
    fig_26_31(), fig_26_32(), fig_26_33(), fig_26_34(), fig_26_35(), fig_26_36(),
    fig_26_37(),
]


def fig(n):
    return FIGS[n - 1]
