# -*- coding: utf-8 -*-
"""Figures for Handbook Chapter 96 — Reading/Recording Devices
(Herman Vermarien, Edward McConnell, Yufeng Li).

Part 1: figures 96.1–96.12, all from section 96.2 (Data Acquisition Systems).

NOTE: never emit <sub>/<sup> inside <svg> text — both are on the HTML parser's
breakout list and eject the parser from SVG foreign content. Subscripts use
<tspan dy=...> via _rich().
"""
import math

from hbfig import _f, svg, _fig

E = "#2a2a2a"
S = "#8a8a8a"
GRID = "#e2e2e2"
GOLD = "#b45309"
BLUE = "#1d4ed8"
TEAL = "#0f766e"


# ---------------------------------------------------------------- helpers
def _lbl(x, y, txt, cls="tm", anchor="start"):
    return ('<text class="%s" x="%s" y="%s" text-anchor="%s">%s</text>'
            % (cls, _f(x), _f(y), anchor, txt))


def _rich(x, y, parts, anchor="start", cls="tm"):
    s, prev = "", False
    for txt, is_sub in parts:
        if is_sub:
            s += '<tspan font-size="7.6" dy="2.2">%s</tspan>' % txt
        elif prev:
            s += '<tspan dy="-2.2">%s</tspan>' % txt
        else:
            s += txt
        prev = is_sub
    return ('<text class="%s" x="%s" y="%s" text-anchor="%s">%s</text>'
            % (cls, _f(x), _f(y), anchor, s))


def _vlab(x, y, txt, cls="ts"):
    return ('<text class="%s" x="%s" y="%s" text-anchor="middle" '
            'transform="rotate(-90 %s %s)">%s</text>'
            % (cls, _f(x), _f(y), _f(x), _f(y), txt))


def _defs(tag):
    return ('<defs>'
            '<marker id="a%s" markerWidth="9" markerHeight="9" refX="7" refY="3" '
            'orient="auto"><path d="M0,0 L7,3 L0,6 z" fill="%s"/></marker>'
            '<marker id="h%s" markerWidth="7" markerHeight="7" refX="5" refY="2.4" '
            'orient="auto"><path d="M0,0 L5,2.4 L0,4.8 z" fill="%s"/></marker>'
            '<style>.ts{font:9.5px Inter,Helvetica,sans-serif;fill:#666}'
            '.tm{font:9.5px Inter,Helvetica,sans-serif;fill:#222}'
            '.tf{font:11px "Cambria Math",Georgia,serif;fill:#111}'
            '.tb{font:9.5px Inter,Helvetica,sans-serif;fill:#111;font-weight:700}'
            '.tcap{font:9px Inter,Helvetica,sans-serif;fill:#555}'
            '</style></defs>' % (tag, E, tag, E))


def _line(x1, y1, x2, y2, sw=1.2, col=E, dash=""):
    d = ' stroke-dasharray="%s"' % dash if dash else ""
    return ('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="%s"%s/>'
            % (_f(x1), _f(y1), _f(x2), _f(y2), col, sw, d))


def _arr(x1, y1, x2, y2, tag="961", sw=1.15, col=E, head="a"):
    return ('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="%s" '
            'marker-end="url(#%s%s)"/>'
            % (_f(x1), _f(y1), _f(x2), _f(y2), col, sw, head, tag))


def _rect(x, y, w, h, sw=1.2, fill="#fff", dash=""):
    d = ' stroke-dasharray="%s"' % dash if dash else ""
    return ('<rect x="%s" y="%s" width="%s" height="%s" fill="%s" stroke="%s" '
            'stroke-width="%s"%s/>'
            % (_f(x), _f(y), _f(w), _f(h), fill, E, sw, d))


def _blk(x, y, w, h, parts, cls="tm"):
    o = [_rect(x, y, w, h)]
    n = len(parts)
    for i, ln in enumerate(parts):
        cy = y + h / 2.0 + (i - (n - 1) / 2.0) * 12 + 3.4
        if isinstance(ln, list):
            o.append(_rich(x + w / 2.0, cy, ln, "middle", cls))
        else:
            o.append(_lbl(x + w / 2.0, cy, ln, cls, "middle"))
    return "".join(o)


def _tri(x, y, w, h, d="l"):
    """Amplifier triangle; d='l' points left, 'r' points right."""
    if d == "l":
        pts = "%s,%s %s,%s %s,%s" % (_f(x + w), _f(y), _f(x + w), _f(y + h),
                                     _f(x), _f(y + h / 2.0))
    else:
        pts = "%s,%s %s,%s %s,%s" % (_f(x), _f(y), _f(x), _f(y + h),
                                     _f(x + w), _f(y + h / 2.0))
    return '<polygon points="%s" fill="#fff" stroke="%s" stroke-width="1.2"/>' % (pts, E)


def _frame(x, y, w, h, xt=(), yt=(), xlab="", ylab=""):
    """L-shaped axes with inward ticks and optional labels."""
    o = [_line(x, y + h, x + w, y + h, 1.2),
         _line(x, y, x, y + h, 1.2)]
    for px, lab in xt:
        o.append(_line(px, y + h, px, y + h - 4, 1.1))
        if lab:
            o.append(_lbl(px, y + h + 13, lab, "ts", "middle"))
    for py, lab in yt:
        o.append(_line(x, py, x + 4, py, 1.1))
        if lab:
            o.append(_lbl(x - 6, py + 3.2, lab, "ts", "end"))
    if xlab:
        o.append(_lbl(x + w + 6, y + h + 3, xlab, "ts", "start"))
    if ylab:
        o.append(_vlab(x - 30, y + h / 2.0, ylab, "ts"))
    return "".join(o)


def _path(pts, sw=1.5, col=E, dash=""):
    d = ' stroke-dasharray="%s"' % dash if dash else ""
    s = "M" + " L".join("%s %s" % (_f(a), _f(b)) for a, b in pts)
    return ('<path d="%s" fill="none" stroke="%s" stroke-width="%s"%s/>'
            % (s, col, sw, d))


# ---------------------------------------------------------------- 96.1
def fig_96_1():
    tag = "961"
    o = [_defs(tag)]
    y, h = 74, 56
    for x, w, lines in [(26, 92, ["Transducers"]),
                        (158, 118, ["Signal", "Conditioning"]),
                        (318, 150, ["Data Acquisition", "and Analysis", "Hardware"]),
                        (512, 110, ["Personal", "Computer"])]:
        o.append(_blk(x, y, w, h, lines))
    ym = y + h / 2.0
    o.append(_arr(120, ym, 154, ym, tag))
    o.append(_arr(278, ym, 314, ym, tag))
    o.append(_arr(470, ym, 508, ym, tag))
    o.append(_line(567, y + h, 567, y + h + 24, 1.1, S, "3 3"))
    o.append(_lbl(567, y + h + 40, "Software", "tm", "middle"))
    return _fig(svg(700, 190, "".join(o),
                    "Các thành phần của một hệ thống thu thập dữ liệu"),
                "Các thành phần của một hệ thống thu thập dữ liệu.",
                "Components of a DAQ system.",
                "Sơ đồ khối hệ thống thu thập dữ liệu: cảm biến, điều hoà tín hiệu, "
                "phần cứng thu thập và phân tích dữ liệu, máy tính cá nhân, phần mềm",
                "Block diagram of a DAQ system: transducers, signal conditioning, "
                "data acquisition and analysis hardware, personal computer, software")


# ---------------------------------------------------------------- 96.2
def _inset(x, y, w, h, kind, tag):
    """Small inset sketch of a signal class."""
    o = [_line(x, y + h, x + w, y + h, 1.1),
         _line(x, y, x, y + h, 1.1)]
    xl = x + w + 5
    if kind == "onoff":
        xm = x + w * 0.42
        o.append(_path([(x + 4, y + h * 0.74), (xm, y + h * 0.74),
                        (xm, y + h * 0.24), (x + w - 6, y + h * 0.24)]))
        o.append(_lbl(x + 7, y + h * 0.24 - 4, "on", "ts"))
        o.append(_lbl(x + 7, y + h * 0.74 - 4, "off", "ts"))
        o.append(_lbl(xl, y + h + 3, "t", "tf"))
    elif kind == "pulse":
        pts, xc = [(x + 4, y + h * 0.78)], x + 4
        for _ in range(3):
            pts.append((xc + w * 0.08, y + h * 0.78))
            pts.append((xc + w * 0.08, y + h * 0.22))
            pts.append((xc + w * 0.17, y + h * 0.22))
            pts.append((xc + w * 0.17, y + h * 0.78))
            pts.append((xc + w * 0.25, y + h * 0.78))
            xc += w * 0.25
        o.append(_path(pts))
        o.append(_lbl(x + 6, y + h * 0.24 - 3, "1", "ts"))
        o.append(_lbl(x + 6, y + h * 0.78 - 3, "0", "ts"))
        o.append(_lbl(xl, y + h + 3, "t", "tf"))
    elif kind == "dc":
        pts = [(x + 4 + i * (w - 10) / 12.0,
                y + h * 0.40 + 3 * math.sin(i / 2.6) + i * 0.35) for i in range(13)]
        o.append(_path(pts))
        cx, cy = pts[-3]
        o.append('<circle cx="%s" cy="%s" r="2" fill="#fff" stroke="%s" '
                 'stroke-width="1.2"/>' % (_f(cx), _f(cy), E))
        o.append(_lbl(cx - 4, cy - 7, "0.995", "ts", "end"))
        o.append(_lbl(xl, y + h + 3, "t", "tf"))
    elif kind == "time":
        pts = [(x + 4 + i * (w - 10) / 40.0,
                y + h * 0.5 - (math.sin(i / 3.1) + 0.55 * math.sin(i / 1.3 + 1)
                               + 0.3 * math.sin(i / 0.7)) * h * 0.16)
               for i in range(41)]
        o.append(_path(pts))
        o.append(_lbl(xl, y + h + 3, "t", "tf"))
    else:  # freq
        base = y + h - 4
        for fx, fh in ((0.10, 0.55), (0.24, 0.85), (0.40, 0.42),
                       (0.56, 0.72), (0.74, 0.30)):
            px = x + 4 + fx * (w - 12)
            o.append(_line(px, base, px, base - fh * (h - 8), 1.5))
        o.append(_lbl(xl, y + h + 3, "f", "tf"))
    return "".join(o)


def fig_96_2():
    tag = "962"
    o = [_defs(tag)]
    o.append(_lbl(28, 226, "Signals", "tf"))
    o.append(_line(88, 222, 148, 222, 1.2))
    o.append(_line(148, 108, 148, 316, 1.2))

    o.append(_lbl(158, 100, "Digital", "tm"))
    o.append(_line(148, 108, 232, 108, 1.2))
    o.append(_line(232, 66, 232, 152, 1.2))
    o.append(_line(232, 66, 424, 66, 1.2))
    o.append(_line(232, 152, 424, 152, 1.2))

    o.append(_lbl(158, 308, "Analog", "tm"))
    o.append(_line(148, 316, 232, 316, 1.2))
    o.append(_line(232, 252, 232, 404, 1.2))
    for yy in (252, 316, 404):
        o.append(_line(232, yy, 424, yy, 1.2))

    for yy, kind in ((66, "onoff"), (152, "pulse"),
                     (252, "dc"), (316, "time"), (404, "freq")):
        o.append(_rect(424, yy - 26, 196, 52, 1.1, "#fff"))
        o.append(_inset(434, yy - 19, 168, 36, kind, tag))

    for yy, lab in ((66, "On-Off"), (152, "Pulse-Train"), (252, "DC"),
                    (316, "Time Domain"), (404, "Frequency Domain")):
        o.append(_lbl(420, yy - 7, lab, "tm", "end"))

    return _fig(svg(700, 450, "".join(o), "Phân loại tín hiệu"),
                "Phân loại tín hiệu.",
                "Classes of signals.",
                "Cây phân loại tín hiệu: tín hiệu số gồm on-off và chuỗi xung; "
                "tín hiệu tương tự gồm DC, miền thời gian và miền tần số",
                "Signal classification tree: digital signals split into on-off and "
                "pulse-train, analog signals into dc, time domain and frequency domain")


# ---------------------------------------------------------------- 96.3
def fig_96_3():
    tag = "963"
    o = [_defs(tag)]
    ym, bh = 100, 52

    o.append(_rect(646, 44, 20, 132, 1.2))
    o.append(_lbl(656, 34, "I/O Connector", "ts", "middle"))

    o.append(_blk(536, ym - bh / 2, 84, bh, ["Analog", "Mux"]))
    o.append(_tri(462, ym - bh / 2, 54, bh, "l"))
    o.append(_lbl(489, ym + bh / 2 + 14, "Inst. Amp", "ts", "middle"))
    o.append(_tri(388, ym - bh / 2, 54, bh, "l"))
    o.append(_lbl(415, ym + bh / 2 + 14, "S/H", "ts", "middle"))
    o.append(_blk(302, ym - bh / 2, 66, bh, ["ADC"]))
    o.append(_blk(212, ym - bh / 2, 66, bh, ["FIFO"]))
    o.append(_blk(104, ym - bh / 2, 88, bh, ["PC Interface", "Circuitry"]))
    o.append(_rect(46, 44, 20, 132, 1.2))
    o.append(_lbl(56, 34, "PC Bus", "ts", "middle"))

    for x1, x2 in ((646, 622), (536, 518), (462, 444), (388, 370),
                   (302, 280), (212, 194), (104, 68)):
        o.append(_arr(x1, ym, x2, ym, tag))

    return _fig(svg(700, 200, "".join(o),
                    "Phần vào tương tự của một bo mạch thu thập dữ liệu cắm trong"),
                "Phần vào tương tự của một bo mạch thu thập dữ liệu cắm trong. "
                "Ghi chú: FIFO = bộ đệm vào trước ra trước, S/H = mẫu và giữ, "
                "Inst. Amp = khuếch đại đo lường, Mux = bộ dồn kênh tương tự.",
                "Analog input section of a plug-in DAQ board. Note: FIFO = first-in "
                "first-out buffer, S/H = sample-and-hold, Inst. Amp = instrumentation "
                "amplifier, and Mux = analog multiplexer.",
                "Sơ đồ khối phần vào tương tự: đầu nối vào ra, bộ dồn kênh tương tự, "
                "khuếch đại đo lường, mạch mẫu và giữ, chuyển đổi tương tự sang số, "
                "bộ đệm FIFO, mạch giao tiếp PC và búy PC",
                "Analog input chain: I/O connector, analog multiplexer, instrumentation "
                "amplifier, sample-and-hold, ADC, FIFO, PC interface circuitry, PC bus")


# ---------------------------------------------------------------- 96.4
def _wave(t):
    return (math.sin(2 * math.pi * 0.9 * t)
            + 0.55 * math.sin(2 * math.pi * 2.3 * t + 0.8)
            + 0.28 * math.sin(2 * math.pi * 4.1 * t + 2.1))


def fig_96_4():
    tag = "964"
    o = [_defs(tag)]
    x0, w = 118, 424
    T = 4.0
    N = 240

    # --- input signal
    o.append(_lbl(10, 62, "Input", "tm"))
    o.append(_lbl(10, 74, "Signal", "tm"))
    o.append(_frame(x0, 24, w, 62, xt=(), yt=(), xlab="Time", ylab="Amplitude"))
    pts = [(x0 + i * w / float(N), 55 - _wave(i * T / N) * 17) for i in range(N + 1)]
    o.append(_path(pts))

    # --- sample clock
    o.append(_lbl(10, 132, "Sample", "tm"))
    o.append(_lbl(10, 144, "Clock", "tm"))
    cy = 138
    o.append(_line(x0, cy, x0 + w, cy, 1.1))
    K = 26
    for i in range(K + 1):
        px = x0 + i * w / float(K)
        o.append(_line(px, cy - 9, px, cy, 1.1))

    # --- digitized signal
    o.append(_lbl(10, 216, "Digitized", "tm"))
    o.append(_lbl(10, 228, "Signal", "tm"))
    o.append(_frame(x0, 182, w, 62, xt=(), yt=(), xlab="Time", ylab="Amplitude"))
    spts = [(x0 + i * w / float(K), 213 - _wave(i * T / K) * 17) for i in range(K + 1)]
    o.append(_path(spts, 1.2, E, "2 3"))
    for px, py in spts:
        o.append('<circle cx="%s" cy="%s" r="1.7" fill="%s"/>' % (_f(px), _f(py), E))

    return _fig(svg(640, 268, "".join(o),
                    "Các mẫu rời rạc liên tiếp tái tạo lại tín hiệu vào"),
                "Các mẫu rời rạc liên tiếp tái tạo lại tín hiệu vào.",
                "Consecutive discrete samples recreate the input signal.",
                "Ba dải tín hiệu: tín hiệu vào liên tục, xung nhịp lấy mẫu và tín hiệu "
                "đã số hoá gồm các điểm rời rạc nối bằng nét gạch",
                "Three traces: continuous input signal, sample clock, and digitized "
                "signal drawn as discrete dots joined by a dashed line")


# ---------------------------------------------------------------- 96.5 / 96.6
def _spectrum(tag, aliases):
    o = [_defs(tag)]
    ay = 158
    o.append(_line(74, ay, 560, ay, 1.3))

    # axis break between the low-frequency cluster and the 500 Hz region
    o.append(_line(380, ay - 6, 390, ay + 6, 1.2))
    o.append(_line(394, ay - 6, 404, ay + 6, 1.2))

    for x, lab in ((80, "0"), (500, "500")):
        o.append(_line(x, ay, x, ay + 5, 1.1))
        o.append(_lbl(x, ay + 18, lab, "ts", "middle"))
    for x in (164, 249):
        o.append(_line(x, ay, x, ay + 5, 1.1))

    o.append(_rich(164, ay + 18, [("f", False), ("s", True), ("/2=50", False)],
                   "middle", "ts"))
    o.append(_lbl(164, ay + 32, "Nyquist Frequency", "ts", "middle"))
    o.append(_rich(249, ay + 18, [("f", False), ("s", True), ("=100", False)],
                   "middle", "ts"))
    o.append(_lbl(249, ay + 47, "Sampling Frequency", "ts", "middle"))

    peaks = [(122, 25, "F1", 58), (198, 70, "F2", 62),
             (350, 160, "F3", 44), (520, 510, "F4", 58)]
    for x, f, name, hh in peaks:
        o.append(_line(x, ay - 1, x, ay - 1 - hh, 1.5))
        o.append(_arr(x, ay - 1 - hh + 6, x, ay - 1 - hh - 1, tag, 1.5))
        o.append(_lbl(x, ay - 1 - hh - 21, name, "tm", "middle"))
        o.append(_lbl(x, ay - 1 - hh - 10, "%d Hz" % f, "ts", "middle"))

    if aliases:
        o.append(_lbl(78, 30, "Solid Arrows \u2013 Actual Frequency", "ts"))
        o.append(_lbl(78, 44, "Dashed Arrows \u2013 Alias", "ts"))
        o.append(_lbl(78, 62, "F2 \u2192 30 Hz  \u00b7  F3 \u2192 40 Hz  \u00b7  F4 \u2192 10 Hz",
                      "ts"))
        for x in (97, 131, 147):
            o.append(_line(x, ay - 1, x, ay - 34, 1.3, S, "4 3"))
            o.append(_arr(x, ay - 34, x, ay - 42, tag, 1.3, S, "h"))
    return "".join(o), ay


def fig_96_5():
    body, ay = _spectrum("965", False)
    return _fig(svg(640, 225, body, "Phổ của tín hiệu có nhiều tần số"),
                "Phổ của tín hiệu có nhiều tần số.",
                "Spectral of signal with multiple frequencies.",
                "Phổ vạch của tín hiệu gồm các thành phần 25, 70, 160 và 510 Hz, "
                "đánh dấu tần số Nyquist 50 Hz và tần số lấy mẫu 100 Hz",
                "Line spectrum showing components at 25, 70, 160 and 510 Hz, with the "
                "Nyquist frequency of 50 Hz and sampling frequency of 100 Hz marked")


def fig_96_6():
    body, ay = _spectrum("966", True)
    return _fig(svg(640, 235, body,
                    "Phổ của tín hiệu có nhiều tần số sau khi lấy mẫu"),
                "Phổ của tín hiệu có nhiều tần số sau khi lấy mẫu ở f\u209b = 100 Hz.",
                "Spectral of signal with multiple frequencies after sampling at "
                "fs = 100 Hz.",
                "Phổ sau khi lấy mẫu: các vạch thực 25, 70, 160, 510 Hz và các vạch "
                "chồng phổ tương ứng 30, 40, 10 Hz",
                "Post-sampling spectrum: real lines at 25, 70, 160 and 510 Hz plus "
                "alias lines at 30, 40 and 10 Hz")


# ---------------------------------------------------------------- 96.7
def fig_96_7():
    tag = "967"
    o = [_defs(tag)]
    x0, y0, w, h = 92, 26, 470, 250
    # grid
    for i in range(0, 11):
        px = x0 + i * w / 10.0
        o.append(_line(px, y0, px, y0 + h, 0.9, GRID))
        o.append(_line(px, y0 + h, px, y0 + h + 4, 1.1))
        o.append(_lbl(px, y0 + h + 16, "%.2f" % (i / 10.0), "ts", "middle"))
    for j in range(0, 11):
        py = y0 + j * h / 10.0
        o.append(_line(x0, py, x0 + w, py, 0.9, GRID))
        o.append(_line(x0, py, x0 - 4, py, 1.1))
        o.append(_lbl(x0 - 7, py + 3.2, "%d" % (-10 * j), "ts", "end"))
    o.append(_line(x0, y0, x0, y0 + h, 1.3))
    o.append(_line(x0, y0 + h, x0 + w, y0 + h, 1.3))
    o.append(_lbl(x0 + w / 2.0, y0 + h + 32, "Frequency / Sample Rate", "ts", "middle"))
    o.append(_vlab(46, y0 + h / 2.0, "Magnitude (dB)", "ts"))

    def yy(db):
        return y0 + (-db) * h / 100.0

    # passband flat, steep roll-off, then noise floor
    pts = [(x0, yy(0))]
    for i in range(0, 41):
        fr = i / 100.0
        pts.append((x0 + fr * w, yy(0.15 * math.sin(fr * 9))))
    for fr, db in ((0.42, -0.5), (0.44, -6), (0.455, -22), (0.468, -48),
                   (0.478, -70), (0.487, -82), (0.497, -86), (0.51, -84)):
        pts.append((x0 + fr * w, yy(db)))
    for i in range(0, 50):
        fr = 0.51 + i * 0.0098
        pts.append((x0 + fr * w, yy(-(83.5 + 1.8 * math.sin(i * 1.7)
                                      + 0.9 * math.sin(i * 4.3)))))
    o.append(_path(pts, 1.7))

    return _fig(svg(640, 320, "".join(o),
                    "Phần độ lớn hàm truyền của bộ lọc chống chồng phổ"),
                "Phần độ lớn của hàm truyền của một bộ lọc chống chồng phổ.",
                "Magnitude portion of transfer function of an antialiasing filter.",
                "Đồ thị độ lớn theo tỉ số tần số trên tần số lấy mẫu: băng thông phẳng "
                "0 dB tới khoảng 0,42 rồi sụt rất dốc xuống −85 dB và nằm ở mức nhiễu",
                "Magnitude versus frequency-to-sample-rate ratio: flat 0 dB passband to "
                "about 0.42, a very steep roll-off to -85 dB, then the noise floor")


# ---------------------------------------------------------------- 96.8
def fig_96_8():
    tag = "968"
    o = [_defs(tag)]
    x0, y0, w, h = 122, 34, 448, 130
    o.append(_line(x0, y0 + h, x0 + w, y0 + h, 1.2))
    o.append(_line(x0, y0, x0, y0 + h, 1.2))

    def yy(v):          # volts, range -5..17
        return y0 + h - (v + 5) * h / 22.0

    for v, lab in ((0, "0 V"), (5, "5 V"), (10, "+10 V")):
        o.append(_line(x0 - 5, yy(v), x0, yy(v), 1.1))
        o.append(_lbl(x0 - 8, yy(v) + 3.2, lab, "ts", "end"))
        o.append(_line(x0, yy(v), x0 + w, yy(v), 0.9, GRID))

    pts = []
    N = 300
    for i in range(N + 1):
        t = i * 30.0 / N
        pts.append((x0 + i * w / float(N),
                    yy(10 * math.sin(2 * math.pi * t / 10.0) + 5)))
    o.append(_path(pts, 1.6))

    xp = x0 + w * 2.5 / 30.0          # first peak
    xa, xb = xp - 8, xp + 8
    top = yy(17.2)
    o.append(_line(xa, yy(5), xa, top, 1.05, E, "3 3"))
    o.append(_line(xb, yy(5), xb, top, 1.05, E, "3 3"))
    o.append(_line(xa, top, xb, top, 1.05, E, "3 3"))
    o.append(_lbl(xp, top - 8, "5 \u00b5s", "ts", "middle"))
    o.append(_lbl(xa - 4, yy(5) + 13, "t", "tf", "end"))
    o.append(_rich(xa - 2, yy(5) + 17, [("1", True)], "end", "ts"))
    o.append(_lbl(xb + 4, yy(5) + 13, "t", "tf"))
    o.append(_rich(xb + 6, yy(5) + 17, [("2", True)], "start", "ts"))

    xd = xb + 20
    o.append(_arr(xd, yy(5) - 2, xd, yy(9.4), tag, 1.05))
    o.append(_arr(xd, yy(9.4), xd, yy(5) - 2, tag, 1.05))
    o.append(_lbl(xd + 6, yy(7.0), "\u0394V", "tf", "start"))

    for t, lab in ((10, "10 ms"), (20, "20 ms")):
        px = x0 + w * t / 30.0
        o.append(_line(px, y0 + h, px, y0 + h + 5, 1.1))
        o.append(_lbl(px, y0 + h + 17, lab, "ts", "middle"))
    o.append(_lbl(x0 + w + 6, y0 + h + 3, "Time", "ts"))

    o.append(_lbl(x0 + w - 176, y0 + h + 42,
                  "V(t) = 10sin(2\u03c0 \u00d7 100 \u00d7 t) + 5", "ts"))

    return _fig(svg(640, 250, "".join(o),
                    "Jitter làm giảm độ chính xác hiệu dụng"),
                "Jitter làm giảm độ chính xác hiệu dụng của bo mạch thu thập dữ liệu.",
                "Jitter reduces the effective accuracy of the DAQ board.",
                "Đường sin 100 Hz với cửa sổ 5 micro giây ở đỉnh, cho thấy sai số "
                "điện áp \u0394V do thời điểm lấy mẫu dao động",
                "A 100 Hz sine with a 5 microsecond window at its peak, showing the "
                "voltage error delta V caused by uncertain sample timing")


# ---------------------------------------------------------------- 96.9
def fig_96_9():
    tag = "969"
    o = [_defs(tag)]
    x0, w = 108, 470

    def panel(y0, h, lab):
        o.append(_line(x0, y0 + h, x0 + w, y0 + h, 1.2))
        o.append(_line(x0, y0, x0, y0 + h, 1.2))
        for v, s in ((5, "+5 V"), (0, "0"), (-5, "\u22125 V")):
            py = y0 + h - (v + 5) * h / 10.0
            o.append(_line(x0 - 5, py, x0, py, 1.1))
            o.append(_lbl(x0 - 8, py + 3.2, s, "ts", "end"))
        o.append(_lbl(x0 - 78, y0 + h / 2.0 + 3, lab, "tm"))

    T = 10.0
    # CH0
    y0, h = 34, 78
    panel(y0, h, "CH0")
    pts = []
    N = 260
    for i in range(N + 1):
        t = i * 20.0 / N
        pts.append((x0 + i * w / float(N), y0 + h - (5 * math.sin(2 * math.pi * t / T) + 5) * h / 10.0))
    o.append(_path(pts, 1.5))
    o.append(_lbl(x0 - 78, y0 - 8, "Continuous", "ts"))
    o.append(_lbl(x0 - 78, y0 + 4, "Sampling", "ts"))

    # CH1 (phase shifted)
    y1 = 140
    panel(y1, h, "CH1")
    pts = []
    for i in range(N + 1):
        t = i * 20.0 / N
        pts.append((x0 + i * w / float(N),
                    y1 + h - (5 * math.sin(2 * math.pi * t / T + 1.05) + 5) * h / 10.0))
    o.append(_path(pts, 1.5))

    # sample instants, alternating channels
    xs, sums = [], []
    K = 16
    for k in range(K + 1):
        t = k * 20.0 / K
        px = x0 + k * w / float(K)
        ch = 0 if k % 2 == 0 else 1
        val = 5 * math.sin(2 * math.pi * t / T + (0 if ch == 0 else 1.05))
        o.append(_line(px, y0, px, y1 + h, 1.0, S, "4 4"))
        o.append(_lbl(px, y1 + h + 14, str(ch + 1), "ts", "middle"))
        xs.append(px)
        sums.append(val)

    # resulting waveform
    y2 = 262
    o.append(_line(x0, y2 + 74, x0 + w, y2 + 74, 1.2))
    o.append(_line(x0, y2, x0, y2 + 74, 1.2))
    for v, s in ((5, "+5 V"), (0, "0"), (-5, "\u22125 V")):
        py = y2 + 74 - (v + 5) * 74 / 10.0
        o.append(_line(x0 - 5, py, x0, py, 1.1))
        o.append(_lbl(x0 - 8, py + 3.2, s, "ts", "end"))
    o.append(_lbl(x0 - 86, y2 + 22, "Resulting", "ts"))
    o.append(_lbl(x0 - 86, y2 + 34, "Waveform", "ts"))
    o.append(_lbl(x0 - 86, y2 + 46, "CH0+CH1", "ts"))

    def yv(v):
        return y2 + 74 - (v + 5) * 74 / 10.0

    vals = [5 if k % 2 == 0 else -5 for k in range(K + 1)]
    rpts = [(xs[k], yv(vals[k])) for k in range(K + 1)]
    o.append(_path(rpts, 1.5))
    for k in (1, 2):
        o.append(_lbl(xs[k] + 5, yv(vals[k]) + (3.4 if vals[k] > 0 else -4),
                      "+5+0" if vals[k] > 0 else "\u22125+0", "ts"))

    o.append(_lbl(x0 + w + 6, y1 + h + 3, "Time", "ts"))

    return _fig(svg(660, 360, "".join(o),
                    "Độ lệch kênh gây kết luận sai"),
                "Nếu độ lệch kênh lớn so với tín hiệu thì có thể dẫn tới những kết "
                "luận sai.",
                "If the channel skew is large compared with the signal, then erroneous "
                "conclusions may result.",
                "Hai kênh sin lệch pha được lấy mẫu xen kẽ, tạo ra dạng sóng tổng hợp "
                "hình răng cưa thay vì bằng không",
                "Two phase-shifted sine channels sampled alternately, producing a "
                "sawtooth sum instead of the expected zero")


# ---------------------------------------------------------------- 96.10
def fig_96_10():
    tag = "9610"
    o = [_defs(tag)]
    bh = 34
    for i, yy in enumerate((46, 108)):
        o.append(_lbl(34, yy + 20, "Channel %d" % (i + 1), "tm"))
        o.append(_arr(96, yy + 14, 126, yy + 14, tag))
        o.append(_tri(126, yy - 3, 44, bh, "r"))
        o.append(_lbl(148, yy + 44, "Inst", "ts", "middle"))
        o.append(_lbl(148, yy + 54, "Amp", "ts", "middle"))
        o.append(_arr(170, yy + 14, 196, yy + 14, tag))
        o.append(_tri(196, yy - 3, 44, bh, "r"))
        o.append(_lbl(218, yy + 44, "S/H", "ts", "middle"))
        o.append(_arr(240, yy + 14, 282, yy + 14, tag))
    o.append(_blk(286, 48, 74, 86, ["Analog", "Mux"]))
    o.append(_arr(360, 92, 404, 92, tag))
    o.append(_blk(404, 72, 60, 40, ["ADC"]))

    # waveforms with aligned sample marks
    x0, w = 150, 380
    for i, (yy, ph) in enumerate(((196, 0.0), (256, 1.6))):
        o.append(_lbl(78, yy + 18, "Channel %d" % (i + 1), "tm"))
        o.append(_line(x0, yy + 34, x0 + w, yy + 34, 1.1))
        pts = []
        N = 200
        for j in range(N + 1):
            t = j * 6.0 / N
            pts.append((x0 + j * w / float(N), yy + 17 - 13 * math.sin(2 * math.pi * t / 2.0 + ph)))
        o.append(_path(pts, 1.4))
        for k in range(9):
            px = x0 + k * w / 8.0
            o.append(_line(px, yy, px, yy + 34, 1.0, S, "3 3"))

    return _fig(svg(660, 310, "".join(o),
                    "Sơ đồ khối lấy mẫu nhiều kênh đồng thời"),
                "Sơ đồ khối các thành phần thu thập dữ liệu dùng để lấy mẫu nhiều kênh "
                "đồng thời.",
                "Block diagram of DAQ components used to sample multiple channels "
                "simultaneously.",
                "Mỗi kênh có khuếch đại đo lường và mạch mẫu giữ riêng, sau đó dồn "
                "kênh vào một bộ chuyển đổi tương tự sang số duy nhất",
                "Each channel has its own instrumentation amplifier and sample-and-hold, "
                "then a multiplexer feeds a single ADC")


# ---------------------------------------------------------------- 96.11
def fig_96_11():
    tag = "9611"
    o = [_defs(tag)]

    def group(x0, skew, note1, note2):
        w = 150
        o.append(_line(x0, 40, x0, 190, 1.2))
        for i in range(4):
            yy = 62 + i * 32
            o.append(_lbl(x0 - 6, yy + 3, "Channel %d" % (i + 1), "ts", "end"))
            pts = []
            N = 90
            for j in range(N + 1):
                t = j * 4.0 / N
                pts.append((x0 + j * w / float(N),
                            yy - 11 * math.sin(2 * math.pi * t / 2.0 + i * 0.62)))
            o.append(_path(pts, 1.3))
            # sample marks
            for k in range(4):
                px = x0 + 12 + k * 38 + (skew * i)
                o.append(_line(px, yy - 16, px, yy + 16, 1.0, S, "3 3"))
        o.append(_lbl(x0 + w / 2.0, 214, note1, "ts", "middle"))
        o.append(_lbl(x0 + w / 2.0, 228, note2, "ts", "middle"))

    group(96, 4.0, "5 \u00b5sec between sample", "270\u00b0 phase shift between Ch1 and Ch4")
    group(420, 0.0, "5 nanosec interchannel skew", "0.09\u00b0 phase shift between Ch1 and Ch4")

    return _fig(svg(660, 250, "".join(o),
                    "So sánh quét liên tục và lấy mẫu đồng thời"),
                "So sánh quét liên tục và lấy mẫu đồng thời.",
                "Comparison of continuous scanning and simultaneous sampling.",
                "Hai bên: quét liên tục tạo độ lệch 5 micro giây giữa các kênh, còn "
                "lấy mẫu đồng thời chỉ lệch 5 nano giây",
                "Two panels: continuous scanning gives a 5 microsecond channel skew, "
                "simultaneous sampling only 5 nanoseconds")


# ---------------------------------------------------------------- 96.12
def fig_96_12():
    tag = "9612"
    o = [_defs(tag)]
    x0, w = 116, 400
    for i in range(10):
        yy = 40 + i * 22
        lab = "Channel %d" % (i + 1) if i < 2 else ("Channel 10" if i == 9 else None)
        if i == 2:
            o.append(_lbl(x0 - 8, yy - 2, "\u22ee", "tm", "end"))
        if lab:
            o.append(_lbl(x0 - 8, yy + 3, lab, "ts", "end"))
        o.append(_line(x0, yy, x0 + w, yy, 1.0, "#c9c9c9"))

    # scan burst: ten samples within 50 us
    for i in range(10):
        yy = 40 + i * 22
        px = x0 + 22 + i * 4.2
        o.append('<circle cx="%s" cy="%s" r="2" fill="%s"/>' % (_f(px), _f(yy), E))
    o.append(_line(132, 266, 132, 280, 1.1))
    o.append(_line(180, 266, 180, 280, 1.1))
    o.append(_arr(133, 273, 179, 273, tag))
    o.append(_arr(179, 273, 133, 273, tag))
    o.append(_lbl(156, 294, "50 \u00b5s", "ts", "middle"))

    # second scan, one second later
    px2 = x0 + 330
    for i in range(10):
        yy = 40 + i * 22
        o.append('<circle cx="%s" cy="%s" r="2" fill="%s"/>'
                 % (_f(px2 + i * 4.2), _f(yy), E))
    o.append(_line(132, 318, 132, 332, 1.1))
    o.append(_line(px2 + 2, 318, px2 + 2, 332, 1.1))
    o.append(_arr(133, 325, px2, 325, tag))
    o.append(_arr(px2, 325, 133, 325, tag))
    o.append(_lbl((133 + px2) / 2.0, 346, "1 s", "ts", "middle"))

    return _fig(svg(640, 362, "".join(o),
                    "Quét theo khoảng trên mười kênh"),
                "Quét theo khoảng — cả mười kênh được quét trong 45 \u00b5s; con số này "
                "không đáng kể so với tốc độ thu thập tổng thể 1 S/s.",
                "Interval scanning \u2014 all ten channels are scanned within 45 \u00b5s; "
                "this is insignificant relative to the overall acquisition rate of 1 S/s.",
                "Mười kênh được quét dồn trong khoảng 50 micro giây rồi lặp lại mỗi giây",
                "Ten channels scanned in a 50 microsecond burst, then repeated once "
                "per second")


# ---------------------------------------------------------------- dispatch
_FIGS = {
    1: fig_96_1, 2: fig_96_2, 3: fig_96_3, 4: fig_96_4,
    5: fig_96_5, 6: fig_96_6, 7: fig_96_7, 8: fig_96_8,
    9: fig_96_9, 10: fig_96_10, 11: fig_96_11, 12: fig_96_12,
}


def fig(n):
    return _FIGS[n]()


# ---------------------------------------------------------------- 96.13
def fig_96_13():
    tag = "9613"
    o = [_defs(tag)]

    # ---- (a) head / medium cross-section
    o.append(_rect(70, 206, 550, 40, 1.1, "#ececec"))
    o.append(_lbl(84, 262, "Magnetic medium", "ts"))

    mx = 118
    for k in range(8):
        d = 1 if k % 2 == 0 else -1
        x = mx + k * 62
        o.append(_arr(x - 22 * d, 226, x + 22 * d, 226, tag, 1.1))

    o.append('<path d="M376,190 L320,190 L320,112 L440,112 L440,190 L384,190" '
             'fill="none" stroke="%s" stroke-width="26" stroke-linejoin="round" '
             'stroke-linecap="butt"/>' % E)
    o.append(_lbl(380, 168, "Gap", "ts", "middle"))
    o.append(_arr(380, 172, 380, 196, tag, 1.0))
    o.append(_lbl(400, 220, "\u03c6", "tf"))

    for k in range(6):
        o.append('<ellipse cx="%s" cy="112" rx="5.5" ry="13" fill="#ffffff" '
                 'stroke="%s" stroke-width="1.1"/>' % (_f(344 + k * 14), E))
    o.append(_lbl(438, 92, "Coil", "ts"))

    o.append(_arr(300, 74, 300, 96, tag, 1.1))
    o.append(_lbl(292, 68, "i", "tf", "end"))
    o.append(_arr(462, 96, 462, 74, tag, 1.1))
    o.append(_lbl(470, 68, "i", "tf"))

    o.append(_arr(556, 186, 600, 186, tag, 1.2))
    o.append(_lbl(606, 190, "V", "tf"))

    o.append(_line(430, 250, 430, 262, 1.0))
    o.append(_line(560, 250, 560, 262, 1.0))
    o.append(_arr(431, 256, 559, 256, tag, 1.0))
    o.append(_arr(559, 256, 431, 256, tag, 1.0))
    o.append(_lbl(495, 278, "B", "tf", "middle"))

    o.append(_lbl(380, 44, "(a)", "ts", "middle"))

    # ---- (b) write / read timing
    x0, x1 = 190, 600
    cells = 6
    cw = (x1 - x0) / float(cells)
    bits = [1, 0, 1, 0, 0, 1]

    o.append(_lbl(96, 320, "Encoded data", "ts"))
    for k, b in enumerate(bits):
        o.append(_lbl(x0 + cw * (k + 0.5), 320, str(b), "tm", "middle"))

    # current i
    yi = 350
    o.append(_lbl(96, yi + 4, "i", "tf"))
    o.append(_line(x0, yi, x1, yi, 1.0, S, "4 3"))
    cur = [1, -1, 1, -1, 1, -1]
    for k, c in enumerate(cur):
        xa, xb = x0 + cw * k, x0 + cw * (k + 1)
        yy = yi - 13 if c > 0 else yi + 13
        o.append(_line(xa, yy, xb, yy, 1.6))
        if k:
            o.append(_line(xa, yy, xa, yi - 13 if cur[k - 1] > 0 else yi + 13, 1.6))
    o.append(_lbl(164, yi - 12, "+", "ts", "middle"))
    o.append(_lbl(164, yi + 16, "\u2212", "ts", "middle"))

    # magnetization M
    ym = 396
    o.append(_lbl(96, ym + 4, "M", "tf"))
    o.append(_line(x0, ym, x1, ym, 1.1))
    for k, b in enumerate(bits):
        if not b:
            continue
        xa, xb = x0 + cw * k + 6, x0 + cw * (k + 1) - 6
        d = 1 if k % 4 == 0 else -1
        xm = (xa + xb) / 2.0
        o.append(_arr(xm - 14 * d, ym, xm + 14 * d, ym, tag, 1.1))

    # reproducing voltage v
    yv = 442
    o.append(_lbl(96, yv + 4, "v", "tf"))
    o.append(_line(x0, yv, x1, yv, 1.0, S, "4 3"))
    for k, b in enumerate(bits):
        if not b:
            continue
        xm = x0 + cw * (k + 0.5)
        d = -1 if k % 4 == 0 else 1
        pts = [(xm - 20, yv), (xm - 8, yv + 16 * d), (xm + 4, yv),
               (xm + 14, yv - 6 * d), (xm + 22, yv)]
        o.append(_path(pts, 1.5))

    # output pulse
    yp = 486
    o.append(_lbl(96, yp + 4, "Output pulse", "ts"))
    o.append(_line(x0, yp, x1, yp, 1.1))
    for k, b in enumerate(bits):
        if not b:
            continue
        xa, xb = x0 + cw * k + 10, x0 + cw * (k + 1) - 10
        o.append(_path([(xa, yp), (xa, yp - 20), (xb, yp - 20), (xb, yp)], 1.5))

    # process brackets
    o.append(_line(632, 338, 632, 410, 1.1))
    o.append(_lbl(640, 378, "Write process", "ts"))
    o.append(_line(632, 428, 632, 492, 1.1))
    o.append(_lbl(640, 464, "Read process", "ts"))

    return _fig(svg(700, 510, "".join(o),
                    "Nguyên lý ghi từ và quá trình ghi/đọc"),
                "Sơ đồ khái niệm minh hoạ nguyên lý ghi từ (a), và quá trình ghi/đọc "
                "lại (b).",
                "Conceptual diagrams illustrating the magnetic recording principle (a), "
                "and recording/reproducing process (b).",
                "Phần (a) là mặt cắt đầu từ hình vành khuyên với khe hở và cuộn dây trên "
                "môi trường từ; phần (b) là các dạng sóng dòng điện, từ độ, điện áp và "
                "xung ra khi ghi rồi đọc lại",
                "Part (a) is a cross-section of a ring head with gap and coil above the "
                "medium; part (b) shows the current, magnetization, voltage and output "
                "pulse waveforms for writing then reading")


# ---------------------------------------------------------------- 96.14
def fig_96_14():
    tag = "9614"
    o = [_defs(tag)]
    cx, cy = 250, 160
    sx, sy = 78.0, 96.0

    o.append(_line(cx - 200, cy, cx + 200, cy, 1.2))
    o.append(_arr(cx + 186, cy, cx + 202, cy, tag, 1.2))
    o.append(_line(cx, cy + 120, cx, cy - 120, 1.2))
    o.append(_arr(cx, cy - 106, cx, cy - 122, tag, 1.2))
    o.append(_lbl(cx + 208, cy + 4, "H", "tf"))
    o.append(_lbl(cx + 6, cy - 126, "M", "tf"))

    Ms, Hc, k = 1.0, 0.40, 0.32
    Mr = Ms * math.tanh(Hc / k)   # remanence: ascending branch at H = 0

    def branch(shift):
        pts = []
        N = 160
        for i in range(N + 1):
            h = -2.4 + i * 4.8 / N
            m = Ms * math.tanh((h + shift) / k)
            pts.append((cx + h * sx, cy - m * sy))
        return pts

    o.append(_path(branch(Hc), 1.6))     # ascending (H increasing)
    o.append(_path(branch(-Hc), 1.6))    # descending

    for v, lab in ((Ms, "M"), (Mr, "M")):
        pass
    o.append(_lbl(cx - 8, cy - Ms * sy + 4, "M", "tf", "end"))
    o.append(_rich(cx - 6, cy - Ms * sy + 7, [("s", True)], "end", "ts"))
    o.append(_lbl(cx - 8, cy - Mr * sy + 4, "M", "tf", "end"))
    o.append(_rich(cx - 6, cy - Mr * sy + 7, [("r", True)], "end", "ts"))
    o.append(_line(cx - 4, cy - Ms * sy, cx + 4, cy - Ms * sy, 1.1, S, "3 3"))
    o.append(_line(cx - 4, cy - Mr * sy, cx + 4, cy - Mr * sy, 1.1, S, "3 3"))

    o.append(_lbl(cx + Hc * sx + 2, cy + 18, "H", "tf", "middle"))
    o.append(_rich(cx + Hc * sx + 5, cy + 22, [("c", True)], "middle", "ts"))
    o.append(_line(cx + Hc * sx, cy - 3, cx + Hc * sx, cy + 3, 1.1))

    return _fig(svg(560, 330, "".join(o),
                    "Vòng từ trễ của vật liệu từ"),
                "Vòng từ trễ của một vật liệu từ, thể hiện quan hệ phi tuyến giữa M và H "
                "tạo nên khả năng nhớ từ.",
                "Hysteresis loop of a magnetic material shows the nonlinear relationship "
                "between M and H which results in magnetic memory.",
                "Đường cong từ trễ với từ độ bão hoà Ms, từ dư Mr và lực kháng từ Hc",
                "A hysteresis loop showing saturation magnetization Ms, remanence Mr and "
                "coercivity Hc")


# ---------------------------------------------------------------- 96.15
def fig_96_15():
    tag = "9615"
    o = [_defs(tag)]
    x0, w = 120, 200

    # --- particulate tape
    o.append(_rect(x0, 62, w, 34, 1.0, "#dcdcdc"))
    for r in range(2):
        for c in range(7):
            cx0 = x0 + 14 + c * 26 + (13 if r % 2 else 0)
            cy0 = 72 + r * 14
            o.append('<path d="M%s,%s L%s,%s L%s,%s L%s,%s z" fill="#2a2a2a"/>'
                     % (_f(cx0 - 8), _f(cy0), _f(cx0), _f(cy0 - 5),
                        _f(cx0 + 8), _f(cy0), _f(cx0), _f(cy0 + 5)))
    o.append(_rect(x0, 96, w, 54, 1.0, "#f6f6f6"))
    o.append(_rect(x0, 150, w, 18, 1.0, "#dcdcdc"))

    o.append(_lbl(x0 + w + 12, 82, "Magnetic coat (2 \u2013 5 \u00b5m)", "ts"))
    o.append(_lbl(x0 + w + 12, 127, "Substrate (10 \u2013 20 \u00b5m)", "ts"))
    o.append(_lbl(x0 + w + 12, 163, "Back coat (1 \u2013 3 \u00b5m)", "ts"))

    o.append(_lbl(40, 52, "Magnetic", "ts"))
    o.append(_lbl(40, 64, "particle", "ts"))
    o.append(_arr(92, 56, 118, 74, tag, 1.0))
    o.append(_lbl(196, 50, "Binder", "ts"))
    o.append(_arr(198, 54, 176, 70, tag, 1.0))

    # --- thin film disk
    y = 208
    layers = [("Lubricant (1 \u2013 3 nm)", 9, "#e8e8e8"),
              ("Overcoat (8 \u2013 15 nm)", 14, "#cfcfcf"),
              ("Magnetic film (15 \u2013 50 nm)", 18, "#8f8f8f"),
              ("Underlayer (20 \u2013 100 nm)", 26, "#dedede"),
              ("Undercoat (10 \u2013 20 \u00b5m)", 28, "#f2f2f2"),
              ("Substrate (0.4 \u2013 1.5 mm)", 52, "#b8b8b8")]
    for name, hh, col in layers:
        o.append(_rect(x0, y, w, hh, 1.0, col))
        o.append(_lbl(x0 + w + 12, y + hh / 2.0 + 3.4, name, "ts"))
        y += hh

    return _fig(svg(620, 400, "".join(o),
                    "Mặt cắt băng từ dạng hạt và đĩa cứng màng mỏng"),
                "Mặt cắt của một băng từ dạng hạt (trên) và của một đĩa cứng màng mỏng "
                "(dưới).",
                "Cross-sectional views of a particulate magnetic tape (top) and a thin "
                "film hard disk (bottom).",
                "Hai chồng lớp: băng từ gồm lớp từ, đế và lớp phủ sau; đĩa cứng màng "
                "mỏng gồm chất bôi trơn, lớp phủ, màng từ, lớp đệm, lớp lót và đế",
                "Two layer stacks: tape with magnetic coat, substrate and back coat; "
                "thin film disk with lubricant, overcoat, magnetic film, underlayer, "
                "undercoat and substrate")


# ---------------------------------------------------------------- 96.16
def fig_96_16():
    tag = "9616"
    o = [_defs(tag)]

    # (a) laminated head
    for k in range(5):
        off = k * 5
        o.append('<path d="M%s,%s L%s,%s L%s,%s L%s,%s" fill="none" stroke="%s" '
                 'stroke-width="3.2" stroke-linejoin="round"/>'
                 % (_f(72 + off), _f(196), _f(72 + off), _f(74 + off),
                    _f(196 - off), _f(74 + off), _f(196 - off), _f(196), E))
    o.append(_lbl(120, 60, "Gap", "ts"))
    o.append(_arr(128, 64, 134, 72, tag, 1.0))
    o.append(_lbl(206, 66, "Laminations", "ts"))
    for k in range(5):
        o.append(_arr(214, 72, 178, 76 + k * 5, tag, 0.9))
    for k in range(6):
        o.append('<ellipse cx="%s" cy="130" rx="5" ry="8" fill="none" stroke="%s" '
                 'stroke-width="1.1"/>' % (_f(196 + k * 11), E))
    o.append(_lbl(268, 116, "coil", "ts"))
    o.append(_lbl(134, 226, "(a)", "ts", "middle"))

    # (b) MIG head
    o.append('<path d="M404,196 L404,96 L446,58 L474,58 L516,96 L516,196" '
             'fill="none" stroke="%s" stroke-width="2" stroke-linejoin="round"/>' % E)
    o.append(_rect(444, 46, 10, 22, 1.0, "#cfcfcf"))
    o.append(_rect(466, 46, 10, 22, 1.0, "#cfcfcf"))
    o.append(_lbl(430, 38, "Gap", "ts", "middle"))
    o.append(_rich(486, 38, [("High B", False), ("s", True)], "start", "ts"))
    o.append(_lbl(486, 50, "films", "ts"))
    o.append('<path d="M446,68 L474,68 L488,110 L432,110 z" fill="#efefef" stroke="%s" '
             'stroke-width="1"/>' % E)
    o.append(_lbl(460, 128, "Bonding", "ts", "middle"))
    for k in range(6):
        o.append('<ellipse cx="%s" cy="150" rx="5" ry="8" fill="none" stroke="%s" '
                 'stroke-width="1.1"/>' % (_f(522 + k * 10), E))
    o.append(_lbl(556, 136, "Coil", "ts"))
    o.append(_lbl(416, 176, "Ferrite core", "ts"))
    o.append(_lbl(460, 226, "(b)", "ts", "middle"))

    # (c) thin film head
    o.append(_rect(60, 268, 44, 150, 1.0, "#e4e4e4"))
    o.append(_lbl(62, 264, "Substrate", "ts"))
    o.append(_rect(104, 268, 26, 150, 1.0, "#f4f4f4"))
    o.append(_lbl(100, 452, "Undercoat", "ts"))
    o.append(_rect(130, 268, 74, 150, 1.0, "#fbfbfb"))
    o.append(_rect(186, 268, 74, 150, 1.0, "#fbfbfb"))
    o.append('<path d="M150,292 L214,292 L214,336 L196,336 L196,306 L168,306 L168,336 '
             'L150,336 z" fill="#d9d9d9" stroke="%s" stroke-width="1.2"/>' % E)
    o.append(_lbl(214, 286, "Core", "ts"))
    o.append(_lbl(160, 276, "Gap", "ts"))
    for r in range(4):
        for c in range(2):
            o.append(_rect(226 + c * 16, 300 + r * 18, 11, 11, 1.0, "#fff"))
    o.append(_lbl(268, 330, "Coil", "ts"))
    o.append(_rect(130, 418, 130, 14, 1.0, "#ececec"))
    o.append(_lbl(262, 430, "Overcoat", "ts"))
    o.append(_lbl(160, 478, "(c)", "ts", "middle"))

    # (d) MR sensor
    o.append(_rect(420, 292, 150, 96, 1.2, "#f7f7f7"))
    o.append(_rect(400, 292, 20, 96, 1.1, "#dcdcdc"))
    o.append(_rect(570, 292, 20, 96, 1.1, "#dcdcdc"))
    o.append(_lbl(430, 286, "MRE", "ts"))
    o.append(_lbl(478, 402, "Leads", "ts"))
    o.append(_line(404, 300, 586, 300, 1.0, S, "3 3"))
    o.append(_line(440, 292, 440, 388, 1.0))
    o.append(_arr(440, 384, 440, 292, tag, 1.0))
    o.append(_lbl(434, 344, "h", "tf", "end"))
    o.append(_line(420, 366, 570, 366, 1.0))
    o.append(_arr(566, 366, 420, 366, tag, 1.0))
    o.append(_lbl(495, 380, "w", "tf", "middle"))
    o.append(_lbl(524, 302, "t", "tf"))
    o.append(_arr(498, 350, 540, 318, tag, 1.4))
    o.append(_lbl(546, 314, "M", "tf"))
    o.append('<path d="M498,350 A 40,40 0 0 0 522,342" fill="none" stroke="%s" '
             'stroke-width="1"/>' % E)
    o.append(_lbl(512, 340, "\u03b8", "tf"))
    o.append(_arr(470, 352, 520, 352, tag, 1.1))
    o.append(_lbl(526, 356, "J", "tf"))
    o.append(_lbl(495, 478, "(d)", "ts", "middle"))

    return _fig(svg(700, 496, "".join(o),
                    "Bốn kiểu đầu từ: lá thép, MIG, màng mỏng và cảm biến từ trở"),
                "Sơ đồ minh hoạ (a) đầu từ lá thép, (b) mặt cắt đầu từ MIG, (c) mặt cắt "
                "đầu từ màng mỏng, và (d) cảm biến từ trở có các điện cực.",
                "Schematic illustrations of (a) a laminated head, (b) cross-section of a "
                "MIG head, (c) cross-section of a thin film head, and (d) an MR sensor "
                "with leads.",
                "Bốn pa-nô: đầu từ lá thép có khe hở và cuộn dây, đầu từ MIG với màng "
                "từ tính cao ở khe, đầu từ màng mỏng nhiều lớp, và cảm biến từ trở có "
                "chiều cao h, chiều rộng w, vectơ từ độ M lệch góc theta",
                "Four panels: laminated head with gap and coil, MIG head with high-Bs "
                "films at the gap, multilayer thin film head, and an MR sensor of height "
                "h and width w with magnetization M at angle theta")


_FIGS.update({13: fig_96_13, 14: fig_96_14, 15: fig_96_15, 16: fig_96_16})


# ---------------------------------------------------------------- 96.17
def fig_96_17():
    tag = "9617"
    o = [_defs(tag)]
    o.append('<defs><clipPath id="cp%s"><rect x="40" y="40" width="560" height="210"/>'
             '</clipPath></defs>' % tag)

    for r in range(20, 130, 14):
        for cx in (290, 330):
            o.append('<circle cx="%s" cy="250" r="%s" fill="none" stroke="%s" '
                     'stroke-width="0.9" clip-path="url(#cp%s)"/>'
                     % (_f(cx), _f(r), "#8a8a8a", tag))

    o.append(_rect(120, 250, 170, 62, 1.1, "#dcdcdc"))
    o.append(_rect(330, 250, 170, 62, 1.1, "#dcdcdc"))
    o.append(_lbl(205, 288, "Head core", "ts", "middle"))
    o.append(_lbl(415, 288, "Head core", "ts", "middle"))
    o.append(_lbl(310, 288, "Gap", "ts", "middle"))
    o.append(_lbl(310, 234, "g", "tf", "middle"))

    o.append(_rect(60, 176, 500, 34, 1.1, "#f2f2f2"))
    for k in range(7):
        o.append(_arr(96 + k * 66, 193, 140 + k * 66, 193, tag, 1.1))
    o.append(_lbl(66, 168, "M", "tf"))
    o.append(_lbl(548, 168, "M", "tf"))

    o.append(_line(48, 176, 48, 210, 1.0))
    o.append(_lbl(38, 196, "\u03b4", "tf", "middle"))
    o.append(_line(48, 210, 48, 250, 1.0))
    o.append(_lbl(38, 234, "d", "tf", "middle"))
    o.append(_line(48, 176, 60, 176, 0.9))
    o.append(_line(48, 210, 60, 210, 0.9))

    o.append(_lbl(330, 118, "H", "tf"))
    o.append(_rich(338, 121, [("2", True)], "start", "ts"))
    o.append(_lbl(388, 140, "H", "tf"))
    o.append(_rich(396, 143, [("c", True)], "start", "ts"))
    o.append(_lbl(446, 166, "H", "tf"))
    o.append(_rich(454, 169, [("1", True)], "start", "ts"))

    o.append(_arr(520, 150, 570, 150, tag, 1.2))
    o.append(_lbl(576, 154, "V", "tf"))
    o.append(_line(60, 240, 600, 240, 1.0, S, "3 3"))
    o.append(_lbl(604, 244, "x", "tf"))
    o.append(_arr(310, 150, 310, 100, tag, 1.0))
    o.append(_lbl(318, 104, "y", "tf"))

    return _fig(svg(640, 330, "".join(o),
                    "Xấp xỉ Karlqvist: các đường trường ngang không đổi"),
                "Các đường trường ngang không đổi của xấp xỉ Karlqvist là những vòng tròn "
                "tựa trên hai góc khe hở của đầu từ, và từ độ trong môi trường biến đổi "
                "dần.",
                "The constant horizontal fields of Karlqvist approximation are circles "
                "resting on the gap corners of a head, and the change of magnetization in "
                "the medium is gradual.",
                "Các vòng tròn đồng mức từ trường quanh hai góc khe hở, phía trên là môi "
                "trường có các mũi tên từ độ hướng sang phải",
                "Contours of constant field as circles about the two gap corners, with the "
                "medium above carrying rightward magnetization arrows")


# ---------------------------------------------------------------- 96.18
def fig_96_18():
    tag = "9618"
    o = [_defs(tag)]
    cx, cy, sx, sy = 270, 160, 52.0, 74.0

    o.append(_line(cx - 190, cy, cx + 190, cy, 1.2))
    o.append(_arr(cx + 176, cy, cx + 192, cy, tag, 1.2))
    o.append(_line(cx, cy + 110, cx, cy - 110, 1.2))
    o.append(_arr(cx, cy - 96, cx, cy - 112, tag, 1.2))
    o.append(_lbl(cx + 198, cy + 4, "x/a", "tf"))
    o.append(_lbl(cx + 8, cy - 116, "M", "tf"))
    o.append(_rich(cx + 16, cy - 113, [("r", True)], "start", "ts"))

    for v in (-3, -2, -1, 1, 2, 3):
        o.append(_line(cx + v * sx, cy - 3, cx + v * sx, cy + 3, 1.0))
        o.append(_lbl(cx + v * sx, cy + 16, str(v), "ts", "middle"))
    for v in (-1, -0.5, 0.5, 1):
        o.append(_line(cx - 3, cy - v * sy, cx + 3, cy - v * sy, 1.0))
        o.append(_lbl(cx - 8, cy - v * sy + 3.2, ("%.1f" % v).replace("-", "\u2212"),
                      "ts", "end"))
    o.append(_line(cx - 170, cy - sy, cx + 170, cy - sy, 1.0, S, "3 3"))
    o.append(_line(cx - 170, cy + sy, cx + 170, cy + sy, 1.0, S, "3 3"))

    pts = []
    N = 220
    for i in range(N + 1):
        u = -3.4 + i * 6.8 / N
        pts.append((cx + u * sx, cy - (2.0 / math.pi) * math.atan(u) * sy))
    o.append(_path(pts, 1.8))

    return _fig(svg(560, 320, "".join(o),
                    "Chuyển tiếp từ độ dạng arctang cô lập"),
                "Một chuyển tiếp từ độ dạng arctang cô lập, từ \u2212M\u1d63 sang "
                "+M\u1d63.",
                "An isolated arctangent magnetization transition from negative Mr to "
                "positive Mr.",
                "Đường cong arctang của từ độ chuẩn hoá theo khoảng cách chuẩn hoá, đi từ "
                "trừ Mr tới cộng Mr",
                "An arctangent curve of normalized magnetization versus normalized "
                "distance, running from minus Mr to plus Mr")


# ---------------------------------------------------------------- 96.19
def fig_96_19():
    tag = "9619"
    o = [_defs(tag)]
    x0, y0, w, h = 90, 40, 400, 230

    for j in range(0, 5):
        py = y0 + h - j * h / 4.0
        o.append(_line(x0, py, x0 + w, py, 0.9, GRID))
        o.append(_line(x0, py, x0 - 4, py, 1.1))
        o.append(_lbl(x0 - 7, py + 3.2, str(j * 100), "ts", "end"))
    for i in range(5):
        px = x0 + i * w / 4.0
        o.append(_line(px, y0 + h, px, y0 + h + 4, 1.1))
        o.append(_lbl(px, y0 + h + 16,
                      ("\u22121" if i == 0 else
                       ("0" if i == 2 else ("1" if i == 4 else
                        ("\u22120.5" if i == 1 else "0.5")))), "ts", "middle"))
    o.append(_line(x0, y0, x0, y0 + h, 1.2))
    o.append(_line(x0, y0 + h, x0 + w, y0 + h, 1.2))
    o.append(_lbl(x0 + w / 2.0, y0 + h + 34, "x (\u00b5m)", "ts", "middle"))
    o.append(_vlab(46, y0 + h / 2.0, "Readback voltage (\u00b5V)", "ts"))

    fam = [(0.115, 372, 0.0), (0.145, 352, 0.0), (0.175, 332, 0.0),
           (0.205, 316, 0.0)]
    for sig, amp, _ in fam:
        pts = []
        N = 200
        for i in range(N + 1):
            xv = -1.0 + i * 2.0 / N
            v = amp * math.exp(-(xv / sig) ** 2)
            pts.append((x0 + (xv + 1) * w / 2.0, y0 + h - v * h / 400.0))
        o.append(_path(pts, 1.4))

    o.append(_lbl(x0 + 6, y0 + 34, "g = 0.2 \u00b5m", "ts"))
    for k, lab in enumerate(("0.3", "0.4")):
        o.append(_arr(x0 + 62, y0 + 40 + k * 12, x0 + 150 + k * 26,
                      y0 + 62 + k * 20, tag, 0.9))
        o.append(_lbl(x0 + 66, y0 + 44 + k * 12, lab, "ts"))

    o.append(_lbl(x0 + 214, y0 + 34, "a+d = 0.10 \u00b5m", "ts"))
    for k, lab in enumerate(("0.15", "0.20")):
        o.append(_arr(x0 + 268, y0 + 40 + k * 12, x0 + 250 + k * 30,
                      y0 + 78 + k * 22, tag, 0.9))
        o.append(_lbl(x0 + 272, y0 + 44 + k * 12, lab, "ts"))

    return _fig(svg(600, 330, "".join(o),
                    "Điện áp đọc lại của đầu từ điện cảm"),
                "Điện áp đọc lại của một đầu từ điện cảm trên một chuyển tiếp arctang "
                "cô lập, cho thấy ảnh hưởng của chiều dài khe hở g, tham số a và khoảng "
                "cách đầu từ/môi trường d.",
                "The reproducing voltage of an inductive head over an isolated arctangent "
                "transition shows the effects of gap length g, parameter a, and "
                "head/medium separation d.",
                "Họ đường cong điện áp đọc lại theo vị trí, hẹp và cao hơn khi g nhỏ, "
                "rộng và thấp hơn khi a cộng d lớn",
                "A family of readback voltage curves versus position, narrower and taller "
                "for small g, broader and lower as a plus d grows")


# ---------------------------------------------------------------- 96.20
def fig_96_20():
    tag = "9620"
    o = [_defs(tag)]
    o.append(_rect(60, 250, 460, 40, 1.1, "#ececec"))
    o.append(_lbl(70, 300, "Medium", "ts"))
    for k in range(7):
        o.append(_arr(90 + k * 62, 270, 130 + k * 62, 270, tag, 1.1))

    o.append(_rect(140, 120, 70, 110, 1.1, "#d8d8d8"))
    o.append(_rect(370, 120, 70, 110, 1.1, "#d8d8d8"))
    o.append(_lbl(175, 176, "Shield", "ts", "middle"))
    o.append(_lbl(405, 176, "Shield", "ts", "middle"))
    o.append(_rect(258, 110, 18, 130, 1.1, "#ffffff"))
    o.append(_lbl(267, 100, "MRE", "ts", "middle"))

    o.append(_lbl(246, 190, "g", "tf", "middle"))
    o.append(_lbl(290, 190, "g", "tf", "middle"))
    o.append(_line(240, 200, 256, 200, 1.0))
    o.append(_line(278, 200, 294, 200, 1.0))

    o.append(_line(300, 118, 300, 234, 1.0))
    o.append(_arr(300, 230, 300, 118, tag, 1.0))
    o.append(_lbl(306, 176, "h", "tf"))
    o.append(_lbl(268, 108, "t", "tf", "middle"))

    o.append(_arr(250, 150, 292, 132, tag, 1.3))
    o.append(_lbl(298, 128, "M", "tf"))
    o.append('<path d="M250,150 A 30,30 0 0 1 268,138" fill="none" stroke="%s" '
             'stroke-width="1"/>' % E)
    o.append(_lbl(258, 146, "\u03b8", "tf"))
    o.append(_arr(232, 158, 280, 158, tag, 1.1))
    o.append(_lbl(286, 162, "J", "tf"))

    o.append(_line(120, 250, 120, 238, 1.0))
    o.append(_lbl(108, 246, "d", "tf", "middle"))
    o.append(_arr(500, 230, 540, 230, tag, 1.2))
    o.append(_lbl(546, 234, "x", "tf"))

    return _fig(svg(580, 330, "".join(o),
                    "Đầu từ từ trở có vỏ bọc"),
                "Sơ đồ đầu từ từ trở có vỏ bọc, với khoảng cách từ vỏ tới phần tử từ trở "
                "là g.",
                "Schematic diagram of a shielded MR head with a shield to MRE distance g.",
                "Mặt cắt đầu từ từ trở: phần tử từ trở mỏng kẹp giữa hai vỏ bọc từ, phía "
                "trên môi trường có các mũi tên từ độ",
                "Cross-section of an MR head: a thin magnetoresistive element between two "
                "magnetic shields, above the medium")


# ---------------------------------------------------------------- 96.21
def fig_96_21():
    tag = "9621"
    o = [_defs(tag)]
    x0, y0, w, h = 96, 40, 360, 230
    import math as _m

    def lx(v):
        return x0 + (_m.log10(v) + 2.0) / 2.0 * w

    for j in range(0, 6):
        py = y0 + j * h / 5.0
        o.append(_line(x0, py, x0 + w, py, 0.9, GRID))
        o.append(_line(x0, py, x0 - 4, py, 1.1))
        o.append(_lbl(x0 - 7, py + 3.2, "%d" % (-5 * j), "ts", "end"))
        o.append(_line(x0 + w, py, x0 + w + 4, py, 1.1))
        o.append(_lbl(x0 + w + 7, py + 3.2, "%d" % (-10 * j), "ts"))
    for v, lab in ((0.01, "0.01"), (0.1, "0.1"), (1.0, "1")):
        o.append(_line(lx(v), y0 + h, lx(v), y0 + h + 4, 1.1))
        o.append(_lbl(lx(v), y0 + h + 16, lab, "ts", "middle"))
        o.append(_line(lx(v), y0, lx(v), y0 + h, 0.9, GRID))
    o.append(_line(x0, y0, x0, y0 + h, 1.2))
    o.append(_line(x0, y0 + h, x0 + w, y0 + h, 1.2))
    o.append(_line(x0 + w, y0, x0 + w, y0 + h, 1.2))
    o.append(_vlab(48, y0 + h / 2.0, "Thickness loss (dB)", "ts"))
    o.append(_vlab(524, y0 + h / 2.0, "Spacing and gap losses (dB)", "ts"))
    o.append(_lbl(x0 + w / 2.0, y0 + h + 34,
                  "\u03b4/\u03bb , d/\u03bb , and g/\u03bb", "ts", "middle"))

    # thickness loss, referenced to the left axis
    pts = []
    for i in range(120):
        r = 0.01 * (100 ** (i / 119.0))
        db = 20 * _m.log10(max(1e-3, 1 - _m.exp(-2 * _m.pi * r)))
        pts.append((lx(r), y0 + (-db) * h / 25.0))
    o.append(_path(pts, 1.7))

    # spacing loss, right axis (0 at top, -50 at bottom)
    pts = []
    for i in range(120):
        r = 0.01 * (100 ** (i / 119.0))
        db = -54.6 * r
        pts.append((lx(r), y0 + (-db) * h / 50.0))
    o.append(_path(pts, 1.5, E, "6 3"))

    # gap loss
    pts = []
    for i in range(160):
        r = 0.01 * (100 ** (i / 159.0))
        arg = _m.pi * r
        s = 1.0 if abs(arg) < 1e-9 else abs(_m.sin(arg) / arg)
        db = 20 * _m.log10(max(1e-3, s))
        pts.append((lx(r), y0 + (-db) * h / 50.0))
    o.append(_path(pts, 1.4, E, "2 3"))

    ly = y0 + h - 74
    for k, (lab, dash, sw) in enumerate((("Thickness loss", "", 1.7),
                                         ("Spacing loss", "6 3", 1.5),
                                         ("Gap loss", "2 3", 1.4))):
        yy = ly + k * 16
        o.append(_line(x0 + 118, yy, x0 + 150, yy, sw, E, dash))
        o.append(_lbl(x0 + 158, yy + 3.4, lab, "ts"))

    return _fig(svg(600, 340, "".join(o),
                    "Tổn hao khoảng cách, bề dày và khe hở"),
                "Tổn hao khoảng cách, bề dày và khe hở của một đầu từ điện cảm theo tần "
                "số, khi đọc lại từ độ dạng sin của môi trường.",
                "Spacing, thickness, and gap losses of an inductive head vs. frequency for "
                "the reproducing of a sinusoidal medium magnetization.",
                "Ba đường tổn hao theo bước sóng chuẩn hoá: tổn hao bề dày giảm chậm, tổn "
                "hao khoảng cách giảm tuyến tính, tổn hao khe hở có điểm không",
                "Three loss curves versus normalized wavelength: thickness loss falls "
                "slowly, spacing loss falls linearly, gap loss has a null")


_FIGS.update({17: fig_96_17, 18: fig_96_18, 19: fig_96_19,
              20: fig_96_20, 21: fig_96_21})


# ---------------------------------------------------------------- 96.22
def fig_96_22():
    tag = "9622"
    o = [_defs(tag)]
    x0, y0, w, h = 96, 46, 300, 232

    for k in range(9):
        py = y0 + h - k * h / 8.0
        o.append(_line(x0, py, x0 + w, py, 0.8, GRID))
    o.append(_line(x0, y0, x0, y0 + h, 1.2))
    o.append(_line(x0, y0 + h, x0 + w, y0 + h, 1.2))
    o.append(_lbl(x0 - 10, y0 + 4, "1.0", "ts", "end"))
    o.append(_lbl(x0 - 10, y0 + h / 2.0 + 3, "0.5", "ts", "end"))
    o.append(_lbl(x0 - 10, y0 + h + 3, "0", "ts", "end"))
    o.append(_lbl(x0 - 24, y0 - 10, "V", "tf"))
    o.append(_arr(x0, y0 + 12, x0, y0 - 8, tag, 1.1))

    pts = []
    N = 200
    for i in range(N + 1):
        t = i * 6.0 / N
        v = (math.exp(0.55 * t) - 1) / (math.exp(3.3) - 1)
        pts.append((x0 + t * w / 6.0, y0 + h - v * h))
    o.append(_path(pts, 1.8))

    codes = ["000", "001", "010", "011", "100", "111"]
    for k in range(1, 7):
        px = x0 + k * w / 6.0
        o.append(_line(px, y0 + h, px, y0 + h + 4, 1.0))
        o.append(_lbl(px - w / 12.0, y0 + h + 17, str(k), "ts", "middle"))
        o.append(_lbl(px - w / 12.0, y0 + h + 33, codes[k - 1], "ts", "middle"))
    o.append(_lbl(x0 + w + 8, y0 + h + 3, "t", "tf"))
    o.append(_arr(x0 + 16, y0 + h + 48, x0 + w / 6.0 - 4, y0 + h + 48, tag, 1.0))
    o.append(_lbl(x0 + 4, y0 + h + 52, "MSB", "ts", "end"))
    o.append(_arr(x0 + w - 40, y0 + h + 48, x0 + w - 8, y0 + h + 48, tag, 1.0))
    o.append(_lbl(x0 + w - 44, y0 + h + 52, "LSB", "ts", "end"))

    # bit table
    tx = x0 + w + 34
    o.append(_lbl(tx + 14, y0 - 4, "Bit", "ts", "middle"))
    for i, lab in enumerate(("1", "2", "3")):
        o.append(_lbl(tx + i * 16, y0 + 12, lab, "ts", "middle"))
    rows = ["111", "110", "101", "100", "011", "010", "001", "000"]
    for r, row in enumerate(rows):
        for i, ch in enumerate(row):
            o.append(_lbl(tx + i * 16, y0 + 30 + r * 18, ch, "ts", "middle"))

    o.append(_arr(x0 + 132, y0 + 30, x0 + 132, y0 + 4, tag, 1.0))
    o.append(_arr(x0 + 132, y0 + 4, x0 + 132, y0 + 30, tag, 1.0))
    o.append(_lbl(x0 + 126, y0 + 18, "\u0394V", "tf", "end"))

    return _fig(svg(560, 380, "".join(o),
                    "Lượng tử hoá tín hiệu liên tục thành ba bit"),
                "Sơ đồ minh hoạ việc lượng tử hoá một tín hiệu liên tục thành ba bit.",
                "Schematic illustration of the quantization of a continuous signal to "
                "three bits.",
                "Tín hiệu liên tục tăng dần được rời rạc hoá thành tám mức, mỗi mức ứng "
                "với một mã nhị phân ba bit, kèm bảng bit bên phải",
                "A rising continuous signal quantized into eight levels, each labelled with "
                "a three-bit code, with the bit table at the right")


# ---------------------------------------------------------------- 96.23
def fig_96_23():
    tag = "9623"
    o = [_defs(tag)]
    cx, cy, sx, sy = 250, 150, 66.0, 78.0

    o.append(_line(cx - 180, cy, cx + 180, cy, 1.2))
    o.append(_arr(cx + 166, cy, cx + 182, cy, tag, 1.2))
    o.append(_line(cx, cy + 100, cx, cy - 100, 1.2))
    o.append(_arr(cx, cy - 86, cx, cy - 102, tag, 1.2))
    o.append(_lbl(cx + 190, cy + 4, "H", "tf"))
    o.append(_rich(cx + 198, cy + 7, [("u", True)], "start", "ts"))
    o.append(_lbl(cx + 8, cy - 106, "M", "tf"))
    o.append(_rich(cx + 16, cy - 103, [("r", True)], "start", "ts"))

    o.append(_line(cx - 130, cy + 74, cx + 130, cy - 74, 1.0, S, "4 3"))
    o.append(_line(cx - 130, cy - 74, cx + 130, cy + 74, 1.0, S, "4 3"))

    pts = []
    N = 180
    for i in range(N + 1):
        u = -2.2 + i * 4.4 / N
        pts.append((cx + u * sx, cy - math.tanh(u * 0.95) * sy))
    o.append(_path(pts, 1.8))

    return _fig(svg(520, 300, "".join(o),
                    "Từ độ dư không trễ"),
                "Từ độ dư không trễ thể hiện quan hệ gần như tuyến tính với từ trường một "
                "chiều đặt vào, cho tới một mức H\u1d64 nào đó.",
                "An anhysteretic remanent magnetization shows a pseudo-linear relationship "
                "with the applied unidirectional magnetic field to some Hu level.",
                "Đường cong từ độ dư không trễ với đoạn gần tuyến tính được đánh dấu bằng "
                "hai đường chấm chéo",
                "An anhysteretic remanence curve with its pseudo-linear region marked by two "
                "dotted lines")


# ---------------------------------------------------------------- 96.24
def fig_96_24():
    tag = "9624"
    o = [_defs(tag)]
    x0, x1 = 150, 600
    bits = [1, 0, 1, 0, 0, 0, 1, 1, 1]
    cw = (x1 - x0) / float(len(bits))

    o.append(_lbl(56, 62, "Data", "ts"))
    for k, b in enumerate(bits):
        xa = x0 + cw * k
        o.append(_line(xa, 40, xa, 74, 0.9, GRID))
        o.append(_lbl(xa + cw / 2.0, 66, str(b), "tm", "middle"))
    o.append(_line(x1, 40, x1, 74, 0.9, GRID))

    # RZ
    y = 110
    o.append(_lbl(56, y + 4, "RZ", "ts"))
    o.append(_line(x0, y, x1, y, 1.0, S, "3 3"))
    for k, b in enumerate(bits):
        xa, xb = x0 + cw * k, x0 + cw * (k + 1)
        yy = y - 18 if b else y + 18
        o.append(_path([(xa, y), (xa + cw * 0.15, yy), (xa + cw * 0.6, yy),
                        (xa + cw * 0.75, y), (xb, y)], 1.4))

    # NRZI
    y = 176
    o.append(_lbl(56, y + 4, "NRZI", "ts"))
    lvl = 1
    o.append(_path([(x0, y - lvl * 18)], 1.4))
    for k, b in enumerate(bits):
        xa, xb = x0 + cw * k, x0 + cw * (k + 1)
        if b:
            o.append(_line(xa, y - lvl * 18, xa, y + lvl * 18, 1.4))
            lvl = -lvl
        o.append(_line(xa, y - lvl * 18, xb, y - lvl * 18, 1.4))

    # FM
    y = 246
    o.append(_lbl(56, y + 4, "FM", "ts"))
    lvl = 1
    o.append(_path([(x0, y - 18)], 1.4))
    for k, b in enumerate(bits):
        xa, xb = x0 + cw * k, x0 + cw * (k + 1)
        xm = (xa + xb) / 2.0
        o.append(_line(xa, y - lvl * 18, xa, y + lvl * 18, 1.4))
        lvl = -lvl
        o.append(_line(xa, y - lvl * 18, xm, y - lvl * 18, 1.4))
        if b:
            o.append(_line(xm, y - lvl * 18, xm, y + lvl * 18, 1.4))
            lvl = -lvl
        o.append(_line(xm, y - lvl * 18, xb, y - lvl * 18, 1.4))

    return _fig(svg(640, 300, "".join(o),
                    "So sánh một số mã ghi sớm"),
                "So sánh một số mã được phát triển sớm.",
                "Comparison of some early developed codes.",
                "Bốn dạng sóng cho cùng chuỗi dữ liệu 1 0 1 0 0 0 1 1 1: mã RZ, NRZI và FM",
                "Four waveforms for the same data string 1 0 1 0 0 0 1 1 1: RZ, NRZI and FM "
                "codes")


# ---------------------------------------------------------------- 96.25
def _slider(o, ox, oy, sap, tag):
    def P(i, j, z=0):
        return (ox + (i - j) * 26, oy + (i + j) * 15 - z)
    for j in range(3):
        for i in range(3):
            a, b, c, d = P(i, j), P(i + 1, j), P(i + 1, j + 1), P(i, j + 1)
            o.append('<polygon points="%s,%s %s,%s %s,%s %s,%s" fill="#f4f4f4" '
                     'stroke="%s" stroke-width="0.9"/>'
                     % (_f(a[0]), _f(a[1]), _f(b[0]), _f(b[1]), _f(c[0]), _f(c[1]),
                        _f(d[0]), _f(d[1]), E))
    o.append(_rect(ox + 26, oy + 30, 78, 12, 1.0, "#ffffff"))

    def top(i0, j0, i1, j1, hatch=True):
        a, b, c, d = P(i0, j0, 6), P(i1, j0, 6), P(i1, j1, 6), P(i0, j1, 6)
        o.append('<polygon points="%s,%s %s,%s %s,%s %s,%s" fill="%s" stroke="%s" '
                 'stroke-width="1"/>'
                 % (_f(a[0]), _f(a[1]), _f(b[0]), _f(b[1]), _f(c[0]), _f(c[1]),
                    _f(d[0]), _f(d[1]), "#c9c9c9" if hatch else "#ffffff", E))

    top(0.15, 0.15, 0.6, 0.42)
    top(0.15, 0.6, 0.6, 0.85)
    if not sap:
        top(0.65, 0.42, 0.9, 0.6, False)
    else:
        top(0.65, 0.2, 0.92, 0.4)
        top(0.65, 0.62, 0.92, 0.82)


def fig_96_25():
    tag = "9625"
    o = [_defs(tag)]
    _slider(o, 90, 40, False, tag)
    o.append(_lbl(150, 30, "Tapers", "ts"))
    o.append(_arr(178, 34, 120, 52, tag, 0.9))
    o.append(_lbl(210, 74, "ABS", "ts"))
    o.append(_arr(232, 78, 186, 86, tag, 0.9))
    o.append(_lbl(250, 44, "Pad", "ts"))
    o.append(_arr(272, 48, 250, 56, tag, 0.9))
    o.append(_lbl(316, 40, "Gap", "ts"))
    o.append(_arr(312, 44, 268, 52, tag, 0.9))
    o.append(_lbl(190, 190, "(a)", "ts", "middle"))

    _slider(o, 90, 220, True, tag)
    o.append(_lbl(120, 210, "Tapers", "ts"))
    o.append(_arr(150, 214, 118, 236, tag, 0.9))
    o.append(_lbl(168, 254, "ABS", "ts"))
    o.append(_arr(190, 258, 158, 268, tag, 0.9))
    o.append(_lbl(236, 224, "Cavity", "ts"))
    o.append(_arr(258, 228, 232, 246, tag, 0.9))
    o.append(_lbl(322, 222, "Gap", "ts"))
    o.append(_arr(318, 226, 292, 244, tag, 0.9))
    o.append(_lbl(190, 380, "(b)", "ts", "middle"))

    return _fig(svg(560, 400, "".join(o),
                    "Mặt tựa khí của con trượt ba đệm và con trượt SAP"),
                "Mặt tựa khí (ABS) của (a) con trượt ba đệm dùng cho ghi gần tiếp xúc và "
                "(b) con trượt SAP dùng cho ghi bay thông thường.",
                "The ABS of (a) a tri-pad slider for pseudo-contact recording and (b) a SAP "
                "slider for conventional flying recording.",
                "Hai con trượt dạng khối: loại ba đệm có hai đường trượt và một đệm sau, "
                "loại SAP có thêm khoang giảm áp ở giữa",
                "Two slider blocks: the tri-pad type with two rails and a rear pad, the SAP "
                "type with a sub-ambient cavity in the middle")


# ---------------------------------------------------------------- 96.26
def fig_96_26():
    tag = "9626"
    o = [_defs(tag)]
    cx = 240
    o.append(_line(60, 210, 420, 210, 1.4))
    o.append('<path d="M140,210 A 100,100 0 0 1 340,210" fill="none" stroke="%s" '
             'stroke-width="1.6"/>' % E)
    o.append('<path d="M170,210 C 186,178 206,168 240,166 C 274,168 294,178 310,210" '
             'fill="#e8e8e8" stroke="%s" stroke-width="1.1"/>' % E)
    o.append(_lbl(120, 190, "h", "tf"))
    o.append(_line(146, 210, 146, 168, 1.0))
    o.append(_arr(146, 206, 146, 170, tag, 0.9))
    o.append(_lbl(176, 186, "y", "tf"))
    o.append(_line(196, 210, 196, 172, 1.0))
    o.append(_arr(196, 206, 196, 174, tag, 0.9))
    o.append(_lbl(240, 110, "R", "tf"))
    o.append(_line(240, 166, 300, 96, 1.0, S, "3 3"))
    o.append(_arr(cx, 150, cx, 200, tag, 1.3))
    o.append(_lbl(cx + 6, 176, "F", "tf"))
    o.append(_rich(cx + 14, 179, [("m", True)], "start", "ts"))
    o.append(_lbl(150, 228, "\u03b8", "tf"))
    o.append('<path d="M146,210 A 22,22 0 0 1 166,200" fill="none" stroke="%s" '
             'stroke-width="1"/>' % E)
    o.append(_lbl(320, 230, "\u03b8", "tf"))
    o.append('<path d="M310,210 A 20,20 0 0 1 292,198" fill="none" stroke="%s" '
             'stroke-width="1"/>' % E)

    return _fig(svg(480, 280, "".join(o),
                    "Hình thành mặt khum giữa đầu cầu và mặt phẳng"),
                "Sự hình thành mặt khum giữa một đầu cầu và một mặt phẳng.",
                "Formation of meniscus between a sphere tip and a flat surface.",
                "Mặt cầu đặt trên mặt phẳng có lớp bôi trơn, tạo mặt khum với bán kính R, "
                "khoảng cách y, bề dày h và góc tiếp xúc theta",
                "A sphere above a flat surface with a lubricant film, forming a meniscus of "
                "radius R with distance y, thickness h and contact angle theta")


_FIGS.update({22: fig_96_22, 23: fig_96_23, 24: fig_96_24,
              25: fig_96_25, 26: fig_96_26})


# ---------------------------------------------------------------- 96.27
def _surf(o, ox, oy, nx, ny, cw, ch, hf, hscale):
    cells = []
    for i in range(nx):
        for j in range(ny):
            h00, h10 = hf(i, j), hf(i + 1, j)
            h11, h01 = hf(i + 1, j + 1), hf(i, j + 1)
            p = [(ox + (i - j) * cw, oy + (i + j) * ch - h00 * hscale),
                 (ox + (i + 1 - j) * cw, oy + (i + 1 + j) * ch - h10 * hscale),
                 (ox + (i - j) * cw, oy + (i + 1 + j) * ch - h11 * hscale),
                 (ox + (i - j - 1) * cw, oy + (i + j + 1) * ch - h01 * hscale)]
            gx = (h10 - h00) + (h11 - h01)
            gy = (h01 - h00) + (h11 - h10)
            lit = 0.62 - 1.55 * gx - 1.15 * gy
            lit = max(0.0, min(1.0, lit))
            g = int(96 + 138 * lit)
            cells.append((i + j, p, "#%02x%02x%02x" % (g, g, g)))
    cells.sort(key=lambda c: c[0])
    for _, p, col in cells:
        o.append('<polygon points="%s,%s %s,%s %s,%s %s,%s" fill="%s" '
                 'stroke="#666" stroke-width="0.35"/>'
                 % (_f(p[0][0]), _f(p[0][1]), _f(p[1][0]), _f(p[1][1]),
                    _f(p[2][0]), _f(p[2][1]), _f(p[3][0]), _f(p[3][1]), col))


def fig_96_27():
    tag = "9627"
    o = [_defs(tag)]

    def rough(i, j):
        v = (0.50 + 0.17 * math.sin(i * 1.15 + j * 0.45)
             + 0.13 * math.sin(i * 0.55 - j * 0.95)
             + 0.09 * math.sin(i * 1.95 + j * 1.45)
             + 0.06 * math.cos(i * 2.65 - j * 2.05))
        return max(0.0, min(1.0, v))

    def rings(i, j):
        h = 0.0
        for (ci, cj) in ((4.5, 3.5), (11, 3), (7.5, 7), (14, 7.5), (3.5, 9),
                         (10, 11)):
            r = math.hypot(i - ci, j - cj)
            h += math.exp(-((r - 2.0) ** 2) / 0.75)
        return max(0.0, min(1.0, 0.16 + 0.84 * min(1.0, h)))

    def panel(oy, hf, hs, tag_letter, zlab):
        _surf(o, 196, oy, 18, 13, 9, 5.5, hf, hs)
        o.append(_lbl(196, oy - 14, tag_letter, "ts", "middle"))
        o.append(_lbl(392, oy + 58, "X  10.000 \u00b5m/div", "ts"))
        o.append(_lbl(392, oy + 72, zlab, "ts"))
        o.append(_lbl(392, oy + 86, "50 \u00b5m", "ts"))

    panel(56, rough, 12, "(a)", "Z  50.000 nm/div")
    panel(288, rings, 11, "(b)", "Z  75.000 nm/div")

    return _fig(svg(560, 470, "".join(o),
                    "\u1ea2nh hi\u1ec3n vi l\u1ef1c nguy\u00ean t\u1eed c\u1ee7a "
                    "b\u1ec1 m\u1eb7t c\u01a1 h\u1ecdc v\u00e0 b\u1ec1 m\u1eb7t laser"),
                "\u1ea2nh hi\u1ec3n vi l\u1ef1c nguy\u00ean t\u1eed (AFM) c\u1ee7a (a) "
                "m\u1ed9t b\u1ec1 m\u1eb7t gia c\u00f4ng c\u01a1 v\u00e0 (b) m\u1ed9t "
                "b\u1ec1 m\u1eb7t t\u1ea1o b\u1eb1ng laser (\u1ea3nh do J. Xuan cung "
                "c\u1ea5p).",
                "AFM images of (a) a mechanical texture and (b) a laser texture (Courtesy of "
                "J. Xuan).",
                "Hai \u1ea3nh b\u1ec1 m\u1eb7t ba chi\u1ec1u: b\u1ec1 m\u1eb7t gia "
                "c\u00f4ng c\u01a1 c\u00f3 gai nh\u00e1m ng\u1eabu nhi\u00ean, b\u1ec1 "
                "m\u1eb7t laser c\u00f3 c\u00e1c v\u00f2ng l\u00f5m tr\u00f2n \u0111\u1ec1u "
                "\u0111\u1eb7n",
                "Two 3-D surface maps: a mechanically textured surface with random roughness "
                "spikes, and a laser-textured surface with regular circular ring craters")


# ---------------------------------------------------------------- 96.28
def fig_96_28():
    tag = "9628"
    o = [_defs(tag)]
    cx = 240

    o.append('<polygon points="190,54 290,54 262,92 218,92" fill="#f2f2f2" '
             'stroke="%s" stroke-width="1.2"/>' % E)
    o.append(_line(190, 40, 290, 40, 1.0))
    o.append(_arr(192, 44, 190, 40, tag, 0.9))
    o.append(_arr(288, 44, 290, 40, tag, 0.9))
    o.append(_lbl(240, 34, "D", "tf", "middle"))

    o.append(_rect(110, 130, 260, 74, 1.1, "#e6e6e6"))
    for k in range(14):
        o.append(_line(112 + k * 19, 130, 96 + k * 19, 204, 0.7, "#b9b9b9"))
    o.append(_lbl(116, 148, "Substrate", "ts"))
    o.append(_lbl(116, 162, "n = 1.5", "ts"))

    o.append(_line(218, 92, cx - 8, 214, 1.0))
    o.append(_line(262, 92, cx + 8, 214, 1.0))
    o.append(_lbl(268, 118, "\u03b8", "tf"))
    o.append('<path d="M262,100 A 26,26 0 0 1 258,112" fill="none" stroke="%s" '
             'stroke-width="1"/>' % E)

    o.append(_line(240, 92, 240, 130, 1.0))
    o.append(_lbl(246, 114, "h", "tf"))
    o.append(_rich(252, 117, [("3", True)], "start", "ts"))
    o.append(_line(240, 130, 240, 204, 1.0))
    o.append(_lbl(246, 172, "h", "tf"))
    o.append(_rich(252, 175, [("2", True)], "start", "ts"))

    o.append(_line(196, 130, 196, 142, 1.0))
    o.append(_line(284, 130, 284, 142, 1.0))
    o.append(_arr(197, 136, 283, 136, tag, 0.9))
    o.append(_arr(283, 136, 197, 136, tag, 0.9))
    o.append(_lbl(240, 128, "d", "tf", "middle"))
    o.append(_rich(246, 131, [("2", True)], "start", "ts"))

    o.append(_line(224, 204, 224, 216, 1.0))
    o.append(_line(256, 204, 256, 216, 1.0))
    o.append(_arr(225, 210, 255, 210, tag, 0.9))
    o.append(_arr(255, 210, 225, 210, tag, 0.9))
    o.append(_lbl(240, 226, "d", "tf", "middle"))
    o.append(_rich(246, 229, [("1", True)], "start", "ts"))

    for k in range(6):
        xa = 128 + k * 44
        o.append(_rect(xa, 204, 16, 8, 0.9, "#8f8f8f"))
    o.append(_lbl(392, 218, "Land", "ts"))

    o.append(_line(400, 60, 400, 240, 1.0, S, "3 3"))
    o.append(_rect(414, 96, 96, 84, 1.0, "#ffffff"))
    o.append(_path([(424, 156), (424, 132), (452, 132), (452, 118), (486, 118),
                    (486, 132), (500, 132), (500, 156)], 1.4))
    o.append(_lbl(430, 128, "I", "tf"))
    o.append(_rich(437, 131, [("1", True)], "start", "ts"))
    o.append(_lbl(478, 114, "I", "tf"))
    o.append(_rich(485, 117, [("2", True)], "start", "ts"))
    o.append(_lbl(508, 150, "h", "tf"))
    o.append(_rich(514, 153, [("1", True)], "start", "ts"))
    o.append(_line(504, 132, 504, 118, 1.0))

    return _fig(svg(560, 340, "".join(o),
                    "Nguyên lý đọc đĩa CD-ROM"),
                "Sơ đồ biểu diễn nguyên lý đọc lại của đĩa CD-ROM.",
                "Schematic representation of the CD-ROM reproducing principle.",
                "Thấu kính hội tụ chùm tia qua lớp nền tới mặt phản xạ có các hố và vùng "
                "phẳng, kèm đồ thị cường độ sáng I1 và I2 ở góc phải",
                "A lens focuses a beam through the substrate onto a reflective surface with "
                "pits and lands, with the I1 and I2 intensity profile at the right")


# ---------------------------------------------------------------- 96.29
def fig_96_29():
    tag = "9629"
    o = [_defs(tag)]

    # (a) MO recording
    o.append('<polygon points="90,52 190,52 162,96 118,96" fill="#f2f2f2" '
             'stroke="%s" stroke-width="1.2"/>' % E)
    o.append(_lbl(96, 84, "Laser", "ts"))
    o.append(_line(140, 96, 140, 150, 1.0, S, "3 3"))
    o.append(_rect(60, 150, 220, 26, 1.1, "#ededed"))
    o.append(_lbl(70, 146, "Medium", "ts"))
    for k in range(7):
        x = 78 + k * 30
        d = -1 if k % 2 else 1
        o.append(_arr(x, 172, x, 172 - 16 * d, tag, 1.0))
    o.append(_arr(300, 130, 340, 130, tag, 1.1))
    o.append(_lbl(346, 134, "V", "tf"))
    for k in range(5):
        o.append('<ellipse cx="%s" cy="192" rx="16" ry="4.5" fill="none" stroke="%s" '
                 'stroke-width="1"/>' % (_f(96 + k * 32), E))
    o.append(_lbl(264, 200, "coil", "ts"))
    o.append(_lbl(140, 236, "(a)", "ts", "middle"))

    # (b) quadrilayer stack
    x0, w = 400, 150
    y = 62
    layers = [("Substrate", 30, "#f4f4f4"), ("Overlayer", 24, "#e2e2e2"),
              ("MO layer", 12, "#9a9a9a"), ("Underlayer", 20, "#e2e2e2"),
              ("Reflector", 26, "#c9c9c9")]
    for name, hh, col in layers:
        o.append(_rect(x0, y, w, hh, 1.0, col))
        o.append(_lbl(x0 + w + 8, y + hh / 2.0 + 3.4, name, "ts"))
        y += hh

    o.append(_line(430, 50, 430, 62, 1.0))
    o.append(_arr(430, 58, 430, 44, tag, 1.0))
    o.append(_line(470, 50, 470, 62, 1.0))
    o.append(_arr(470, 58, 470, 44, tag, 1.0))
    o.append(_lbl(392, 40, "Out of phase", "ts", "end"))
    o.append(_line(506, 62, 506, 50, 1.0))
    o.append(_arr(506, 54, 506, 40, tag, 1.0))
    o.append(_line(534, 62, 534, 50, 1.0))
    o.append(_arr(534, 54, 534, 40, tag, 1.0))
    o.append(_lbl(548, 46, "In phase", "ts"))
    o.append(_lbl(475, 236, "(b)", "ts", "middle"))

    return _fig(svg(620, 260, "".join(o),
                    "Ghi từ quang và mặt cắt môi trường bốn lớp"),
                "Sơ đồ minh hoạ (a) quá trình ghi/đọc từ quang và (b) mặt cắt môi trường "
                "bốn lớp.",
                "Schematic illustrations of (a) MO recording/reproducing and (b) quadrilayer "
                "medium cross section.",
                "Phần (a): thấu kính hội tụ tia laser lên môi trường từ có các đômen ngược "
                "chiều, cuộn dây tạo từ trường bên dưới. Phần (b): chồng năm lớp với tia "
                "phản xạ lệch pha và cùng pha",
                "Part (a): a lens focuses a laser onto a magnetic medium with opposing "
                "domains, with a coil below. Part (b): the five-layer stack showing "
                "out-of-phase and in-phase reflected rays")


_FIGS.update({27: fig_96_27, 28: fig_96_28, 29: fig_96_29})
