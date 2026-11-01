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
