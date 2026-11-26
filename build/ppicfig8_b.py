# -*- coding: utf-8 -*-
"""Vector figures 8-14 for PPIC Chapter 8 (coal-bucket dampers).

All seven figures are genuine vector redraws of the raster charts printed on
PDF pages p185-p196.  Figure 12 is rendered as the four line-and-marker panels
actually printed (RMS / peak by frequent / moderate excitation), not as bars.
Every figure returns the standard 5-tuple built by ``_mk`` and is registered
in ``FIGS`` by ``@_reg``.
"""
import math

from ppicfig8_common import (BLUE, GREEN, GREY, INK, RED, H, W, T, _ar, _b,
                             _circle, _defs, _ellipse, _fig, _frame, _legend,
                             _line, _path, _poly, _rect, _mk, _series,
                             _wavey, make_registry)

FIGS, _reg = make_registry()

AM = chr(38)


# ----------------------------------------------------------------- helpers
def _clamp(v, lo, hi):
    return lo if v < lo else (hi if v > hi else v)


def _rot_ylabel(x, y, s, size=7.2, color=INK):
    """Rotated axis title (same convention as _frame)."""
    return ('<text x="%s" y="%s" transform="rotate(-90 %s %s)" '
            'style="font:%spx Inter,Helvetica,sans-serif;fill:%s">%s</text>'
            % (x, y, x, y, size, color, s))


def _diamond(cx, cy, r, color):
    return _poly([(cx, cy - r), (cx + r, cy), (cx, cy + r), (cx - r, cy)],
                 fill=color, sw=0.7, color=color, close=True)


def _tri(cx, cy, r, color):
    return _poly([(cx, cy - r), (cx + r * 0.9, cy + r * 0.7),
                  (cx - r * 0.9, cy + r * 0.7)],
                 fill=color, sw=0.7, color=color, close=True)


def _damped(t, amp, freq, decay, phase):
    return amp * math.exp(-decay * t) * math.cos(2 * math.pi * freq * t + phase)


def _quake(t, f1, f2, decay, spikes=()):
    """Deterministic acceleration signal bounded to [-1, 1]."""
    v = (0.60 * math.sin(2 * math.pi * f1 * t + 0.4)
         + 0.28 * math.sin(2 * math.pi * f2 * t - 0.9)
         + 0.12 * math.sin(2 * math.pi * (f1 + f2) * t + 1.7))
    for tc, a, wd in spikes:
        v += a * math.exp(-((t - tc) / wd) ** 2) * math.sin(
            2 * math.pi * f1 * (t - tc))
    return _clamp(math.exp(-t / decay) * v, -1.0, 1.0)


def _spectrum(T_, amp, tp, tail):
    x = T_ / tp
    return amp * x * math.exp(1.0 - x) + tail * math.exp(-T_ / 3.0)


def _lorentz(f, a, fp, g):
    return a / (1.0 + ((f - fp) / g) ** 2)


def _hist_mini(x, y, w, h, tmax, color, name, f1, f2, decay, spikes=()):
    """One small acceleration time-history plot for Figure 10(a)."""
    o = [_rect(x, y, w, h, fill="#fbfaf7", sw=0.8)]
    z = y + h / 2.0
    o.append(_line(x, z, x + w, z, sw=0.5, color="#cfcfcf"))
    for i in range(1, 5):
        v = i * tmax / 5.0
        px = x + v / tmax * w
        o.append(_line(px, y, px, y + h, sw=0.4, color="#e8e8e8"))
        o.append(T(px, y + h + 9, "%g" % v, 5.6, color=GREY))
    for v in (0.5, 0.0, -0.5):
        py = z - v * h
        o.append(T(x - 4, py + 2, "%g" % v, 5.6, anchor="end", color=GREY))
    pts = []
    for i in range(181):
        t = tmax * i / 180.0
        pts.append((x + t / tmax * w, z - 0.46 * _quake(t, f1, f2, decay, spikes) * h))
    o.append(_poly(pts, sw=1.0, color=color))
    o.append(T(x + w - 4, y + 8, name, 6.2, anchor="end", color=color))
    return "".join(o)


# ------------------------------------------------------------------- 8.8
@_reg
def fig_f08():
    """Figure 8 - free-vibration attenuation curves for CBD1, CBD2 and CBD3."""
    o = [T(340, 12, "Free-vibration attenuation of the three CBDs",
           8.6, color=INK, weight="600")]
    fr, mx, my = _frame(70, 24, 560, 202, (0.0, 3.0), (-0.35, 0.35),
                        [(v, "%g" % v) for v in (0, 0.5, 1, 1.5, 2, 2.5, 3)],
                        [(v, "%g" % v) for v in (-0.3, -0.2, -0.1, 0, 0.1, 0.2, 0.3)],
                        "Time (s)", "Acceleration (g)")
    o.append(fr)
    for col, amp, fq, dc, ph in (
            (RED, 0.34, 2.4, 1.10, -0.70),
            (BLUE, 0.33, 2.2, 0.90, -1.10),
            (GREY, 0.32, 2.7, 1.30, -0.40)):
        o.append(_poly([(mx(t), my(_damped(t, amp, fq, dc, ph)))
                        for t in [3.0 * i / 300.0 for i in range(301)]],
                       sw=1.3, color=col))
    o.append(_legend([(RED, "CBD1"), (BLUE, "CBD2"), (GREY, "CBD3")],
                     512, 36, w=82, lh=13))
    return _mk(8, o, "Free-vibration attenuation curve for CBD1-3",
               "Đường suy giảm dao động tự do của CBD1, CBD2 và CBD3",
               "Free-vibration attenuation curves for CBD1-3",
               "Ba đường gia tốc suy giảm dần theo thời gian cho CBD1, CBD2 và CBD3.",
               "Three acceleration traces decaying with time for CBD1, CBD2 and CBD3.")


# ------------------------------------------------------------------- 8.9
@_reg
def fig_f09():
    """Figure 9 - displacement and acceleration sensor placement."""
    o = [T(340, 13, "A: acceleration sensor     U: displacement sensor",
           7.6, color=INK)]

    def _tower(x0, x1, ytop, ybot, n, pre):
        z = []
        xc = (x0 + x1) / 2.0
        z.append(_rect(x0, ytop, x1 - x0, ybot - ytop, fill="#ffffff", sw=1.0))
        z.append(_line(xc, ytop, xc, ybot, sw=0.8, color=GREY))
        lv = [ybot - k * (ybot - ytop) / n for k in range(n + 1)]
        for y in lv[1:-1]:
            z.append(_line(x0, y, x1, y, sw=0.8))
        for k in range(n):
            yb, yt = lv[k], lv[k + 1]
            z.append(_line(x0, yb, x1, yt, sw=0.7, color=GREY, dash="3,3"))
            z.append(_poly([(x0, yb - 3.5), (x0 + 3.5, yb),
                            (x0, yb + 3.5), (x0 - 3.5, yb)],
                           fill=INK, sw=0.6, color=INK, close=True))
            z.append(T(x0 - 7, yb + 2.4, "%s-%d" % (pre, k + 1),
                       6.6, anchor="end", color=INK))
            z.append(_poly([(xc, yt - 5), (xc + 4.2, yt + 2),
                            (xc - 4.2, yt + 2)],
                           fill=RED, sw=0.6, color=RED, close=True))
            z.append(T(xc + 8, yt + 2.4, "A%d-%d" % (1 if pre == "U1" else 5, k + 1),
                       6.6, anchor="start", color=RED))
        for i in range(int((x1 - x0 + 20) / 11)):
            gx = x0 - 10 + i * 11
            z.append(_line(gx, ybot, gx - 6, ybot - 6, sw=0.7, color=INK))
        z.append(_line(x0 - 12, ybot, x1 + 12, ybot, sw=1.1))
        z.append(T((x0 + x1) / 2.0, ybot + 27,
                   "Axis 1" if pre == "U1" else "Axis 5", 7.8, color=INK))
        return "".join(z)

    o.append(_tower(70, 270, 42, 232, 3, "U1"))
    o.append(_tower(410, 610, 42, 232, 4, "U5"))
    o.append(T(340, 272,
               "U sensors span each storey; A sensors sit at storey tops",
               6.8, color=GREY))
    return _mk(9, o, "Sensor placement",
               "Bố trí cảm biến",
               "Sensor placement",
               "Mặt đứng trục 1 và trục 5: cảm biến chuyển vị U1, U5 và cảm biến gia tốc A1, A5.",
               "Elevations along axes 1 and 5 with displacement sensors U1, U5 and accelerometers A1, A5.")


# ------------------------------------------------------------------ 8.10
@_reg
def fig_f10():
    """Figure 10 - acceleration time histories and response spectra."""
    o = [T(340, 12, "Seismic acceleration: time histories and response spectrum",
           8.6, color=INK, weight="600")]
    y0s = (32, 102, 172)
    for y, tmax, col, name, f1, f2, dc, sp in (
            (y0s[0], 50, BLUE, "RGB", 2.3, 5.1, 19.0, ()),
            (y0s[1], 60, BLUE, "El Centro", 2.8, 6.3, 15.0, ()),
            (y0s[2], 40, BLUE, "Impvall", 3.4, 7.5, 11.0,
             ((9.0, 1.5, 0.45), (11.0, 1.3, 0.40), (13.0, 1.1, 0.55)))):
        o.append(_hist_mini(70, y, 280, 52, tmax, col, name, f1, f2, dc, sp))
    o.append(_rot_ylabel(58, 132, "Acceleration (g)", 6.8, INK))
    o.append(T(210, 244, "Time (s)", 7.0, color=INK))
    o.append(T(210, 260, "(a)", 7.2, color=INK, weight="600"))

    fr, mx, my = _frame(420, 32, 220, 190, (0.0, 6.0), (0.0, 0.3),
                        [(v, "%g" % v) for v in range(7)],
                        [(v, "%g" % v) for v in (0, 0.1, 0.2, 0.3)],
                        "T (s)", "Acceleration (g)")
    o.append(fr)
    for col, dash, a, tp, tail in (
            (BLUE, "", 0.160, 0.32, 0.035),
            (GREY, "5,3", 0.255, 0.18, 0.040),
            (RED, "4,3", 0.225, 0.16, 0.030)):
        o.append(_poly([(mx(t), my(_spectrum(t, a, tp, tail)))
                        for t in [6.0 * i / 240.0 for i in range(241)]],
                       sw=1.3, color=col, dash=dash))
    o.append(_legend([(BLUE, "RGB [30]"), (GREY, "El Centro"), (RED, "Impvall")],
                     465, 166, w=98, lh=13))
    o.append(T(530, 260, "(b)", 7.2, color=INK, weight="600"))
    return _mk(10, o,
               "Time history of seismic acceleration and response spectrum",
               "Lịch sử thời gian và phổ phản ứng của gia tốc địa chấn",
               "Time history and response spectrum of seismic acceleration",
               "Ba bản ghi El Centro, Impvall và RGB: lịch sử thời gian và phổ phản ứng gia tốc.",
               "Three records El Centro, Impvall and RGB: acceleration time histories and response spectra.")


# ------------------------------------------------------------------ 8.11
@_reg
def fig_f11():
    """Figure 11 - white-noise transfer function with natural-frequency marks."""
    o = [T(340, 12, "Acceleration transfer function under white-noise input",
           8.6, color=INK, weight="600")]
    fr, mx, my = _frame(70, 28, 560, 190, (0.0, 35.0), (0.0, 1.0),
                        [(v, "%g" % v) for v in range(0, 36, 5)],
                        [(v / 10.0, "%g" % (v / 10.0)) for v in range(0, 11)],
                        "Frequency (Hz)", "Transfer function")
    o.append(fr)
    for fq in (3.16, 13.2, 21.5):
        o.append(_line(mx(fq), 28, mx(fq), 218, sw=0.9, color=BLUE, dash="4,3"))
    w1 = [(0.90, 3.16, 0.50), (0.22, 13.2, 0.95),
          (0.14, 21.5, 0.80), (0.05, 28.5, 0.90)]
    w4 = [(0.94, 3.30, 0.42), (0.57, 13.2, 0.75),
          (0.47, 21.5, 0.70), (0.22, 28.5, 0.95)]
    fs = [35.0 * i / 420.0 for i in range(421)]
    o.append(_poly([(mx(f), my(min(1.0, 0.015 + sum(_lorentz(f, a, p, g)
                                                    for a, p, g in w1)))) for f in fs],
                   sw=1.3, color=INK))
    o.append(_poly([(mx(f), my(min(1.0, 0.020 + sum(_lorentz(f, a, p, g)
                                                    for a, p, g in w4)))) for f in fs],
                   sw=1.3, color=RED, dash="5,3"))
    o.append(T(150, 44, "No. 1 NF", 7.0, color=INK))
    o.append(_ar(145, 47, 127, 36, color=INK, sw=0.9))
    o.append(T(150, 58, chr(937) + "1 = 3.16 Hz", 6.6, color=INK))
    o.append(T(300, 88, "No. 2 NF", 7.0, color=INK))
    o.append(_ar(295, 91, 288, 101, color=INK, sw=0.9))
    o.append(T(436, 118, "No. 3 NF", 7.0, color=INK))
    o.append(_ar(431, 121, 420, 129, color=INK, sw=0.9))
    o.append(_legend([(INK, "W1"), (RED, "W4")], 88, 246, w=78, lh=13))
    return _mk(11, o, "Transfer function of model under white-noise input",
               "Hàm truyền của mô hình khi kích thích ngẫu nhiên",
               "Transfer function of model under white-noise input",
               "Hàm truyền gia tốc W1 và W4 theo tần số, với ba tần số tự nhiên; tần số đầu là 3,16 Hz.",
               "Acceleration transfer functions W1 and W4 versus frequency with three natural-frequency marks; the first is 3.16 Hz.")


# ------------------------------------------------------------------ 8.12
@_reg
def fig_f12():
    """Figure 12 - RMS and peak displacement reduction rates, four panels."""
    o = [T(340, 12, "Displacement reduction rates under applied seismic conditions",
           8.4, color=INK, weight="600")]
    panels = [
        (70, 34, "(a) RMS, frequent",
         [29.0, 26.5, 28.5, 20.5], [16.7, 18.3, 14.5, 12.2], [12.3, 9.3, 10.2, 14.5]),
        (380, 34, "(b) Peak, frequent",
         [30.0, 21.0, 28.5, 9.0], [8.0, 8.0, 3.0, -11.5], [15.0, 12.5, 9.8, 0.0]),
        (70, 150, "(c) RMS, moderate",
         [32.0, 28.0, 26.0, 32.5], [19.5, 19.0, 17.0, 28.0], [14.7, 14.0, 13.9, 30.0]),
        (380, 150, "(d) Peak, moderate",
         [23.0, 18.0, 20.0, 18.0], [3.0, 7.5, 2.0, -1.5], [21.5, 25.0, 18.3, 16.0]),
    ]
    for px, py, title, e, im, rg in panels:
        pw, ph = 230.0, 78.0
        o.append(T(px, py - 7, title, 7.2, color=INK, weight="600"))
        o.append(_rect(px, py, pw, ph, fill="#fbfaf7", sw=0.9))
        for v in (-10, 0, 10, 20, 30):
            yy = py + ph - (v + 15.0) / 50.0 * ph
            o.append(_line(px, yy, px + pw, yy, sw=0.45, color="#dedede"))
            o.append(T(px - 5, yy + 2, "%g" % v, 5.9, anchor="end", color=GREY))
        for i in range(4):
            xx = px + i * pw / 3.0
            o.append(_line(xx, py + ph, xx, py + ph + 3, sw=0.6))
            o.append(T(xx, py + ph + 11, "%d" % (i + 1), 6.0, color=GREY))
        if py > 100:
            o.append(T(px + pw / 2.0, py + ph + 22, "Story", 6.8, color=INK))
        xs = [px + i * pw / 3.0 for i in range(4)]

        def yy(v):
            return py + ph - (v + 15.0) / 50.0 * ph

        for col, data, mk in ((INK, e, "d"), (BLUE, im, "t"), (RED, rg, "c")):
            o.append(_poly([(xs[i], yy(data[i])) for i in range(4)],
                           sw=1.2, color=col))
            for i in range(4):
                cx, cy = xs[i], yy(data[i])
                if mk == "d":
                    o.append(_diamond(cx, cy, 2.8, col))
                elif mk == "t":
                    o.append(_tri(cx, cy, 3.0, col))
                else:
                    o.append(_circle(cx, cy, 2.6, fill=col, sw=0.6, color=col))
    o.append(_line(185, 260, 199, 260, sw=2.0, color=INK))
    o.append(T(203, 263, "El Centro", 6.8, anchor="start"))
    o.append(_line(295, 260, 309, 260, sw=2.0, color=BLUE))
    o.append(T(313, 263, "Impvall", 6.8, anchor="start"))
    o.append(_line(395, 260, 409, 260, sw=2.0, color=RED))
    o.append(T(413, 263, "RGB", 6.8, anchor="start"))
    return _mk(12, o,
               "Displacement reduction rates under applied seismic conditions",
               "Tỷ lệ giảm chuyển vị dưới các điều kiện địa chấn",
               "Displacement reduction rates under applied seismic conditions",
               "Tỷ lệ giảm chuyển vị RMS và đỉnh theo tầng cho động đất thường xuyên và trung bình.",
               "RMS and peak interstory displacement reduction rates by story under frequent and moderate earthquakes.")


def _disp_trace(t, amp, freq, decay, phase, t0):
    if t <= t0:
        return 0.010 * math.sin(2 * math.pi * 4.5 * t)
    u = t - t0
    return amp * math.exp(-decay * u) * math.sin(2 * math.pi * freq * u + phase)


def _three_panel_disp(o, moderate):
    """Draw the common 3 x 2 panel time-history grid for Figures 13 and 14."""
    lim = 2.0 if moderate else 1.0
    kinds = (
        ("(a) El Centro", 1.25, 2.6, 1.10, 0.42),
        ("(b) Impvall", 1.05, 3.1, 1.25, 0.50),
        ("(c) RGB", 0.85, 2.2, 0.95, 0.38),
    )
    scale = 2.15 if moderate else 1.0
    for px, (name, t0, fq, d_on, d_off) in zip((55, 265, 475), kinds):
        w = 185.0
        for py, story, a_on, a_off in ((30, "Story-2", 0.88, 0.98),
                                       (122, "Story-4", 0.92, 1.00)):
            h = 68.0
            o.append(_rect(px, py, w, h, fill="#fbfaf7", sw=0.8))
            z = py + h / 2.0
            o.append(_line(px, z, px + w, z, sw=0.5, color="#cfcfcf"))
            for v in (-lim, -lim / 2.0, lim / 2.0, lim):
                yy = z - v / lim * (h / 2.0)
                o.append(_line(px, yy, px + w, yy, sw=0.4, color="#e8e8e8"))
                o.append(T(px - 4, yy + 2, "%g" % v, 5.6,
                           anchor="end", color=GREY))
            for i in range(1, 5):
                xx = px + i * w / 5.0
                o.append(_line(xx, py, xx, py + h, sw=0.4, color="#e8e8e8"))
                o.append(T(xx, py + h + 9, "%d" % i, 5.6, color=GREY))
            for col, dash, decay, phase, amp in (
                    (RED, "", d_on, 0.3, a_on),
                    (BLUE, "4,3", d_off, 0.6, a_off)):
                pts = []
                for i in range(181):
                    t = 5.0 * i / 180.0
                    v = _disp_trace(t, amp * scale, fq, decay, phase, t0)
                    pts.append((px + t / 5.0 * w,
                                z - _clamp(v, -lim, lim) / lim * (h / 2.0)))
                o.append(_poly(pts, sw=1.0, color=col, dash=dash))
            o.append(T(px + 5, py + 9, story, 6.2, color=RED))
        o.append(T(px + w / 2.0, 218, name, 7.2, color=INK, weight="600"))
    o.append(_rot_ylabel(42, 110, "Displacement (mm)", 6.8, INK))
    o.append(_line(255, 248, 269, 248, sw=1.8, color=RED))
    o.append(T(273, 251, "With CBDs", 6.8, anchor="start"))
    o.append(_line(380, 248, 394, 248, sw=1.8, color=BLUE, dash="4,3"))
    o.append(T(398, 251, "Without CBDs", 6.8, anchor="start"))
    return o


# ------------------------------------------------------------------ 8.13
@_reg
def fig_f13():
    """Figure 13 - interstory displacement histories, frequent earthquakes."""
    o = [T(340, 12, "Interstory displacements under frequent-intensity earthquakes",
           8.6, color=INK, weight="600")]
    o = _three_panel_disp(o, False)
    return _mk(13, o,
               "Time-history comparison of interstory displacements under frequent-intensity earthquakes",
               "So sánh lịch sử thời gian chuyển vị giữa các tầng dưới động đất mức thường xuyên",
               "Time-history comparison of interstory displacements under frequent-intensity earthquakes",
               "Lịch sử chuyển vị tầng 2 và tầng 4 có và không có CBD cho El Centro, Impvall và RGB.",
               "Story-2 and story-4 displacements with and without CBDs for El Centro, Impvall and RGB.")


# ------------------------------------------------------------------ 8.14
@_reg
def fig_f14():
    """Figure 14 - interstory displacement histories, moderate earthquakes."""
    o = [T(340, 12, "Interstory displacements under moderate-intensity earthquakes",
           8.6, color=INK, weight="600")]
    o = _three_panel_disp(o, True)
    return _mk(14, o,
               "Time-history comparison of interstory displacements under moderate-intensity earthquakes",
               "So sánh lịch sử thời gian chuyển vị giữa các tầng dưới động đất mức trung bình",
               "Time-history comparison of interstory displacements under moderate-intensity earthquakes",
               "Lịch sử chuyển vị tầng 2 và tầng 4 có và không có CBD cho El Centro, Impvall và RGB.",
               "Story-2 and story-4 displacements with and without CBDs for El Centro, Impvall and RGB.")
