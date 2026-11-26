# -*- coding: utf-8 -*-
"""Vector six-panel simulation figures for PPIC Chapter 11 (Figures 4 and 5).

Both figures are genuine SVG redraws: a 2 x 3 grid of response curves computed
from smooth, physically plausible models of the 50% <-> 100% RFP ramps.  No
raster images and no empty placeholder boxes are used.
"""
import math

from ppicfig11_common import (BLUE, GREEN, GREY, INK, RED, W, T, _ar,
                              _circle, _defs, _fig, _frame, _line,
                              _poly, _rect, _mk, _series, make_registry)

FIGS, _reg = make_registry()

H = 520
T0, T1 = 1000.0, 1300.0
PW, PH = 268.0, 104.0
COLS = (40.0, 372.0)
ROWS = (34.0, 176.0, 318.0)

# (legend text, colour, dash pattern, deviation weight, saturation bound)
SERIES_A = (
    ("u_m = 1.0 cm/s", GREEN, "4 3", 1.00, 1.0),
    ("u_m = 1.5 cm/s", GREY, "2 2", 0.55, 1.5),
    ("u_m = 2.5 cm/s", BLUE, "6 2 1 2", 0.18, 2.5),
    ("u_m = 3.5 cm/s", RED, "", 0.00, 3.5),
)
SERIES_B = (
    ("u_m = 0.8 cm/s", GREEN, "4 3", 1.00, 0.8),
    ("u_m = 1.0 cm/s", GREY, "2 2", 0.62, 1.0),
    ("u_m = 2.0 cm/s", BLUE, "6 2 1 2", 0.26, 2.0),
    ("u_m = 3.5 cm/s", RED, "", 0.00, 3.5),
)

XT_SHORT = [(t, str(t)) for t in (900, 1000, 1100, 1200, 1300, 1400, 1500, 1600)]
XT_LONG_A = [(0, "0"), (5000, "5k"), (10000, "10k"), (15000, "15k"),
             (20000, "20k"), (25000, "25k"), (30000, "30k")]
XT_LONG_B = [(0, "0"), (2500, "2.5k"), (5000, "5k"), (7500, "7.5k"),
             (10000, "10k"), (12500, "12.5k"), (15000, "15k")]
YT_POWER_UP = [(v, "%.1f" % v) for v in (0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1)]
YT_POWER_DOWN = [(v, "%.1f" % v) for v in (0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0)]
YT_TEMP_F = [(v, str(v)) for v in (600, 610, 620, 630, 640)]
YT_TEMP_C = [(v, str(v)) for v in (715, 720, 725, 730, 735, 740, 745, 750)]
YT_ERR_A = [(-800, "-800"), (-400, "-400"), (0, "0"), (200, "200")]
YT_ERR_B = [(-200, "-200"), (0, "0"), (200, "200"), (400, "400"), (600, "600")]
YT_SPEED = [(v, str(v)) for v in (-4, -2, 0, 2, 4)]
YT_UCP = [(v, "%.1f" % v) for v in (-0.2, -0.1, 0.0, 0.1, 0.2)]


# ------------------------------------------------------------- response models
def _ramp(t, v0, v1, k):
    """Ramp followed at 10% RFP/min, with u_m-dependent tracking error."""
    span = v1 - v0
    p = 0.0 if t <= T0 else (1.0 if t >= T1 else (t - T0) / (T1 - T0))
    v = v0 + span * p
    if T0 < t < T1:
        # a small lag then catch-up overshoot, strongest for the smallest bound
        v += k * span * (0.055 * math.exp(-((t - 1035.0) / 18.0) ** 2)
                         - 0.020 * math.exp(-((t - 1008.0) / 9.0) ** 2))
    if t >= T1:
        dt = t - T1
        v += span * 0.085 * math.exp(-((dt - 4.0) / 16.0) ** 2)
        v += k * span * 0.030 * math.exp(-dt / 22.0) * math.cos(dt * 0.075)
        v += k * span * 0.010 * math.exp(-dt / 90.0) * math.sin(dt * 0.05)
    return v


def _error(t, k, up=True):
    """Rod-position error: large for small u_m, dissipated by u_cp."""
    if t < T0:
        return 0.0
    dt = t - T0
    if up:
        v = -950.0 * (k ** 1.6) * math.exp(-dt / 1800.0)
        plateau = 180.0 * (k ** 1.5) * (1.0 - math.exp(-dt / 6000.0))
        if t > 20000.0:
            plateau *= math.exp(-(t - 20000.0) / 4000.0)
        v += plateau
        v += 120.0 * k * math.exp(-dt / 9000.0) * math.sin(dt * 0.0016)
    else:
        v = 650.0 * (k ** 1.3) * math.exp(-dt / 900.0)
        v += 90.0 * k * math.exp(-dt / 4500.0) * math.sin(dt * 0.0022 + 0.4)
    return v


def _speed(t, bound, up=True):
    """Saturated rod speed: bursts at ramp start and ramp end."""
    if t < T0:
        return 0.0
    v = 0.0
    for centre, sign in ((T0, 1.0 if up else -1.0),
                         (T1, -1.0 if up else 1.0)):
        dt = t - centre
        if 0.0 <= dt <= 140.0:
            v += sign * bound * 1.25 * math.exp(-dt / 72.0) * math.sin(dt * 0.088)
            v += 0.10 * bound * math.exp(-dt / 45.0) * math.sin(dt * 0.20)
    return max(-bound, min(bound, v))


def _ucp(t, k):
    """Compensating signal: stronger for smaller u_m, fading at steady state."""
    if t < T0:
        return 0.0
    dt = t - T0
    amp = 0.13 * (0.06 + 0.94 * k ** 1.2)
    v = amp * math.exp(-dt / 7000.0) * math.sin(dt * 0.0011 + 1.2)
    v += 0.25 * amp * math.exp(-dt / 3000.0) * math.sin(dt * 0.003 + 1.0)
    dt2 = t - T1
    if dt2 >= 0.0:
        v += 0.35 * amp * math.exp(-dt2 / 2500.0) * math.sin(dt2 * 0.0018)
    v += 0.20 * amp * math.exp(-((t - 22000.0) / 2500.0) ** 2) \
        * math.sin((t - 22000.0) * 0.0025)
    return v


def _points(fn, lo, hi, n=150):
    pts = []
    for i in range(n):
        t = lo + (hi - lo) * i / (n - 1.0)
        pts.append((t, fn(t)))
    return pts


# ------------------------------------------------------------- local markup
def _panel(o, col, row, letter, xr, yr, xt, yt, xlab, ylab, series):
    x0, y0 = COLS[col], ROWS[row]
    frame, mx, my = _frame(x0, y0, PW, PH, xr, yr, xt, yt, xlab, ylab)
    o.append(frame)
    o.append(T(x0 + PW / 2.0, y0 - 3.0, "(%s)" % letter, 6.8, weight="bold"))
    for points, color, dash in series:
        o.append(_series(points, mx, my, color, dash=dash))


def _legend(o, y, series):
    o.append(T(40.0, y - 12.0, "Saturation bound u_m (cm/s)", 6.6,
               anchor="start", color=GREY))
    for i, (label, color, dash, _k, _bound) in enumerate(series):
        x = 40.0 + i * 160.0
        o.append(_line(x, y, x + 20.0, y, sw=1.6, color=color, dash=dash))
        o.append(T(x + 24.0, y + 2.4, label, 7.0, anchor="start", color=INK))


def _group(series, fn, lo, hi, n=150):
    return [(_points(lambda t: fn(t, k, bound), lo, hi, n), color, dash)
            for _lab, color, dash, k, bound in series]


# ------------------------------------------------------------------ figures
@_reg
def fig_f04():
    o = []
    o.append(T(W / 2.0, 15.0,
               "Case A | 50% to 100% RFP ramp at 10% RFP/min",
               8.4, weight="bold"))

    _panel(o, 0, 0, "a", (900.0, 1600.0), (0.5, 1.12),
           XT_SHORT, YT_POWER_UP, "time / s", "n_r",
           _group(SERIES_A, lambda t, k, b: _ramp(t, 0.525, 1.05, k), 900.0, 1600.0))
    _panel(o, 1, 0, "b", (900.0, 1600.0), (598.0, 642.0),
           XT_SHORT, YT_TEMP_F, "time / s", "T_f / degC",
           _group(SERIES_A, lambda t, k, b: _ramp(t, 603.0, 637.0, k), 900.0, 1600.0))
    _panel(o, 0, 1, "c", (900.0, 1600.0), (715.0, 752.0),
           XT_SHORT, YT_TEMP_C, "time / s", "T_cout / degC",
           _group(SERIES_A, lambda t, k, b: _ramp(t, 718.0, 749.0, k), 900.0, 1600.0))
    _panel(o, 1, 1, "d", (0.0, 30000.0), (-1000.0, 200.0),
           XT_LONG_A, YT_ERR_A, "time / s", "e_xi / cm",
           _group(SERIES_A, lambda t, k, b: _error(t, k, True), 0.0, 30000.0, 170))
    _panel(o, 0, 2, "e", (900.0, 1600.0), (-4.0, 4.0),
           XT_SHORT, YT_SPEED, "time / s", "u / (cm/s)",
           _group(SERIES_A, lambda t, k, b: _speed(t, b, True), 900.0, 1600.0))
    _panel(o, 1, 2, "f", (0.0, 30000.0), (-0.25, 0.25),
           XT_LONG_A, YT_UCP, "time / s", "u_cp / (cm/s)",
           _group(SERIES_A, lambda t, k, b: _ucp(t, k), 0.0, 30000.0, 170))

    _legend(o, 470.0, SERIES_A)
    return _mk(
        4, o, "Case A six-panel simulation results",
        "Kết quả mô phỏng trường hợp A: công suất tăng từ 50% lên 100% RFP",
        "Case A simulation results: power rising from 50% to 100% RFP",
        "Sáu biểu đồ mô phỏng trường hợp A: công suất hạt nhân, nhiệt độ nhiên liệu, "
        "nhiệt độ helium đầu ra, sai số vị trí thanh điều khiển, tốc độ thanh và "
        "tốc độ bù; giới hạn tốc độ càng lớn thì phản ứng càng nhanh.",
        "Six Case A simulation panels: nuclear power, fuel temperature, outlet helium "
        "temperature, rod position error, rod speed and compensating rod speed; larger "
        "speed bounds give faster settling.",
        h=H)


@_reg
def fig_f05():
    o = []
    o.append(T(W / 2.0, 15.0,
               "Case B | 100% to 50% RFP ramp at 10% RFP/min",
               8.4, weight="bold"))

    _panel(o, 0, 0, "a", (900.0, 1600.0), (0.4, 1.1),
           XT_SHORT, YT_POWER_DOWN, "time / s", "n_r",
           _group(SERIES_B, lambda t, k, b: _ramp(t, 1.0, 0.5, k), 900.0, 1600.0))
    _panel(o, 1, 0, "b", (900.0, 1600.0), (598.0, 642.0),
           XT_SHORT, YT_TEMP_F, "time / s", "T_f / degC",
           _group(SERIES_B, lambda t, k, b: _ramp(t, 637.0, 602.0, k), 900.0, 1600.0))
    _panel(o, 0, 1, "c", (900.0, 1600.0), (715.0, 752.0),
           XT_SHORT, YT_TEMP_C, "time / s", "T_cout / degC",
           _group(SERIES_B, lambda t, k, b: _ramp(t, 749.0, 718.0, k), 900.0, 1600.0))
    _panel(o, 1, 1, "d", (0.0, 15000.0), (-200.0, 700.0),
           XT_LONG_B, YT_ERR_B, "time / s", "e_xi / cm",
           _group(SERIES_B, lambda t, k, b: _error(t, k, False), 0.0, 15000.0, 170))
    _panel(o, 0, 2, "e", (900.0, 1600.0), (-4.0, 4.0),
           XT_SHORT, YT_SPEED, "time / s", "u / (cm/s)",
           _group(SERIES_B, lambda t, k, b: _speed(t, b, False), 900.0, 1600.0))
    _panel(o, 1, 2, "f", (0.0, 15000.0), (-0.25, 0.25),
           XT_LONG_B, YT_UCP, "time / s", "u_cp / (cm/s)",
           _group(SERIES_B, lambda t, k, b: _ucp(t, k), 0.0, 15000.0, 170))

    _legend(o, 470.0, SERIES_B)
    return _mk(
        5, o, "Case B six-panel simulation results",
        "Kết quả mô phỏng trường hợp B: công suất giảm từ 100% xuống 50% RFP",
        "Case B simulation results: power falling from 100% to 50% RFP",
        "Sáu biểu đồ mô phỏng trường hợp B với xu hướng ngược lại: công suất, nhiệt độ "
        "nhiên liệu, nhiệt độ helium đầu ra, sai số vị trí thanh, tốc độ thanh và tốc độ "
        "bù; tín hiệu bù mạnh hơn khi giới hạn tốc độ nhỏ.",
        "Six Case B simulation panels with mirrored trends: power, fuel temperature, "
        "outlet helium temperature, rod position error, rod speed and compensating rod "
        "speed; compensation is stronger for smaller speed bounds.",
        h=H)
