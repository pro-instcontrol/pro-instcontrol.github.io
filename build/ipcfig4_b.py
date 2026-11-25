# -*- coding: utf-8 -*-
"""Figures 4.16-4.30 for IPC Chapter 4 (Telemetry).

Supplier module ``_b``: amplitude / frequency / phase modulation sketches,
pulse telemetry (PAM, PDM/PWM, PPM), digital bit-pattern modulation and the
SDS block diagram of an electrical power system.  Every figure is a
simplified vector redraw of the printed original; all text stays inside the
680 x 250 canvas and above y = 232 (the bilingual 4.n strip sits at y = 245).
"""
import math

from ipcfig4_common import (BLUE, GREEN, GREY, INK, RED, H, W, T, _ar, _b,
                            _circle, _defs, _ellipse, _fig, _frame, _legend,
                            _line, _path, _poly, _rect, _mk, _series,
                            _wavey, make_registry)

FIGS, _reg = make_registry()

_TWO_PI = 2.0 * math.pi


# ----------------------------------------------------------------- helpers
def _sine(x0, x1, cy, amp, cycles, phase=0.0, color=BLUE, sw=1.7, n=200,
          taper=None):
    """Sinusoid (optionally amplitude-tapered) between two x positions."""
    pts = []
    for i in range(n + 1):
        t = i / float(n)
        a = amp * (taper(t) if taper else 1.0)
        pts.append((x0 + (x1 - x0) * t,
                    cy - a * math.sin(_TWO_PI * cycles * t + phase)))
    return _poly(pts, sw=sw, color=color)


def _wave_axes(xa=64, yc=112, xr=470, ytop=54, ybot=172):
    """Vertical zero axis and horizontal centre line of a waveform sketch."""
    return (_line(xa, ytop, xa, ybot, sw=1.2)
            + _line(xa, yc, xr, yc, sw=0.9, color=GREY))


def _side_label(text, y=112, lx1=524, lx2=484, tx=658):
    """Short right-hand callout with a left-pointing arrow, as printed."""
    return _ar(lx1, y, lx2, y, sw=1.3, color=INK) + T(tx, y + 4, text, 7.8,
                                                      anchor="end")


def _am_wave(x0, x1, cy, amp, fc=9.0, fm=1.25, m=0.72, n=280):
    """Carrier whose amplitude follows a slow sinusoidal signal (AM)."""
    up, dn, pts = [], [], []
    for i in range(n + 1):
        t = i / float(n)
        env = amp * (1.0 + m * math.sin(_TWO_PI * fm * t))
        x = x0 + (x1 - x0) * t
        up.append((x, cy - env))
        dn.append((x, cy + env))
        pts.append((x, cy - env * math.sin(_TWO_PI * fc * t)))
    return (_poly(up, sw=1.0, color=GREY, dash="4,3")
            + _poly(dn, sw=1.0, color=GREY, dash="4,3")
            + _poly(pts, sw=1.5, color=BLUE))


def _fm_wave(x0, x1, cy, amp, fc=8.0, fm=1.0, beta=2.4, n=300):
    """Constant-amplitude carrier with signal-dependent frequency (FM)."""
    pts = []
    for i in range(n + 1):
        t = i / float(n)
        ph = _TWO_PI * fc * t + beta * math.sin(_TWO_PI * fm * t)
        pts.append((x0 + (x1 - x0) * t, cy - amp * math.sin(ph)))
    return _poly(pts, sw=1.6, color=BLUE)


def _pm_wave(x0, x1, cy, amp, cycles=4.6, flips=(0.22, 0.46, 0.72), n=300):
    """Carrier with abrupt 180 degree phase reversals (PM)."""
    pts = []
    for i in range(n + 1):
        t = i / float(n)
        step = sum(math.pi for f in flips if t >= f)
        y = cy - amp * math.sin(_TWO_PI * cycles * t + step)
        pts.append((x0 + (x1 - x0) * t, y))
    return _poly(pts, sw=1.6, color=BLUE)


def _pulse_axes(x0, base, x1, top, ylab, xlab):
    """Arrowed value/time axes for the pulse-telemetry sketches."""
    return (_line(x0, base, x0, top, sw=1.2)
            + _poly([(x0 - 4, top + 7), (x0, top), (x0 + 4, top + 7)],
                    sw=1.1)
            + _line(x0, base, x1, base, sw=1.2)
            + _poly([(x1 - 8, base - 4), (x1, base), (x1 - 8, base + 4)],
                    sw=1.1)
            + T(x0, top - 9, ylab, 7.4)
            + T(x1 + 7, base + 4, xlab, 7.4, anchor="start"))


def _dim(xa, xb, y, lab, ly, size=7.0):
    """A horizontal dimension bracket with end ticks and a short label."""
    return (_line(xa, y, xb, y, sw=0.9, color=GREY)
            + _line(xa, y - 4, xa, y + 4, sw=0.9, color=GREY)
            + _line(xb, y - 4, xb, y + 4, sw=0.9, color=GREY)
            + T((xa + xb) / 2.0, ly, lab, size))


def _bit_grid(bits, x0, cw, ytop, ybot):
    """Dashed cell boundaries for a digital bit-pattern diagram."""
    o = []
    for i in range(len(bits) + 1):
        xx = x0 + i * cw
        o.append(_line(xx, ytop, xx, ybot, sw=0.8, color="#cccccc",
                       dash="3,3"))
    return "".join(o)


def _bit_wave(bits, x0, cw, yhi, ylo):
    """Square-wave drawing of the bit sequence."""
    pts = []
    for i, b in enumerate(bits):
        ya = yhi if b == "1" else ylo
        xa = x0 + i * cw
        pts.extend([(xa, ya), (xa + cw, ya)])
    return _poly(pts, sw=1.4, color=INK)


def _mod_carrier(bits, x0, cw, yc, amp, mode):
    """Carrier trace for digital AM / FM / PM, drawn one bit cell at a time."""
    o = []
    for i, b in enumerate(bits):
        xa = x0 + i * cw
        if mode == "am":
            a = amp if b == "1" else amp * 0.22
            cycles, ph = 2.5, 0.0
        elif mode == "fm":
            a = amp
            cycles, ph = (4 if b == "1" else 2), 0.0
        else:
            a = amp
            cycles, ph = 2.5, (0.0 if b == "0" else math.pi)
        pts = []
        for k in range(41):
            t = k / 40.0
            pts.append((xa + cw * t,
                        yc - a * math.sin(_TWO_PI * cycles * t + ph)))
        o.append(_poly(pts, sw=1.4, color=BLUE))
    return "".join(o)


def _coil_h(cx, ys, color=INK):
    """Small zigzag reactance symbol crossing horizontal phase lines."""
    y0, y1 = min(ys), max(ys)
    pts = []
    for i in range(9):
        t = i / 8.0
        pts.append((cx + (4 if i % 2 else -4), y0 - 4 + (y1 - y0 + 8) * t))
    return _poly(pts, sw=1.0, color=color)


def _coil_v(cy, xs, color=INK):
    """Small zigzag reactance symbol crossing vertical phase lines."""
    x0, x1 = min(xs), max(xs)
    pts = []
    for i in range(9):
        t = i / 8.0
        pts.append((x0 - 4 + (x1 - x0 + 8) * t, cy + (4 if i % 2 else -4)))
    return _poly(pts, sw=1.0, color=color)


# ---------------------------------------------------------------- 4.16
@_reg
def fig_f16():
    """Fig. 4.16 - low-frequency signal waveform used for AM."""
    o = [_wave_axes()]
    o.append(_sine(66, 466, 112, 26, 1.25))
    o.append(_side_label("Signal waveform"))
    return _mk(16, o, "Signal waveform for amplitude modulation",
               "Dạng tín hiệu analog tần số thấp dùng làm tín hiệu điều chế biên độ",
               "Low-frequency sinusoidal signal used for amplitude modulation",
               "Đồ thị dạng sóng tín hiệu: một đường sin tần số thấp dao động quanh trục giữa, bắt đầu từ trục rồi đi lên, dùng làm tín hiệu điều chế cho sóng mang.",
               "Plot of the signal waveform: a low-frequency sinusoid oscillating about the centre line, starting at the axis and rising, used to modulate the carrier.")


# ---------------------------------------------------------------- 4.17
@_reg
def fig_f17():
    """Fig. 4.17 - amplitude-modulated waveshape with envelope."""
    o = [_wave_axes()]
    o.append(_am_wave(66, 466, 112, 17))
    o.append(_side_label("Amplitude-modulated wave"))
    return _mk(17, o, "Amplitude-modulated waveshape",
               "Dạng sóng điều chế biên độ: sóng mang tần số cao có đường bao theo tín hiệu",
               "Amplitude-modulated wave: a high-frequency carrier with an envelope set by the signal",
               "Đồ thị điều chế biên độ: sóng mang tần số cao dao động trong một đường bao dạng sin chậm; hai đường đứt nét cho thấy biên độ tăng và giảm theo tín hiệu.",
               "Amplitude-modulation sketch: a high-frequency carrier oscillating inside a slowly varying sinusoidal envelope; two dashed curves show the amplitude rising and falling with the signal.")


# ---------------------------------------------------------------- 4.18
@_reg
def fig_f18():
    """Fig. 4.18 - carrier waveform for frequency modulation."""
    o = [_wave_axes()]
    o.append(_sine(66, 466, 112, 26, 7.0))
    o.append(_side_label("Carrier waveform"))
    return _mk(18, o, "Carrier waveform for frequency modulation",
               "Dạng sóng mang sinusoidal tần số cao, biên độ không đổi, dùng cho điều chế tần số",
               "High-frequency constant-amplitude sinusoidal carrier used for frequency modulation",
               "Đồ thị sóng mang: đường sin tần số cao với biên độ không đổi, có khoảng bảy chu kỳ, dùng làm sóng mang cho điều chế tần số.",
               "Carrier waveform diagram: a high-frequency sinusoid of constant amplitude with about seven cycles, used as the carrier for frequency modulation.")


# ---------------------------------------------------------------- 4.19
@_reg
def fig_f19():
    """Fig. 4.19 - signal waveform for frequency modulation."""
    o = [_wave_axes()]
    o.append(_sine(66, 466, 112, 26, 1.0))
    o.append(_side_label("Signal waveform"))
    return _mk(19, o, "Signal waveform for frequency modulation",
               "Dạng tín hiệu điều chế một chu kỳ gồm một bán sóng dương và một bán sóng âm",
               "Single-cycle modulating signal with one positive and one negative half wave",
               "Đồ thị tín hiệu điều chế: một chu kỳ sin hoàn chỉnh gồm một bán sóng dương rồi một bán sóng âm, xác định sự thay đổi tần số của sóng mang.",
               "Modulating signal plot: one complete sine cycle with a positive half wave followed by a negative half wave, determining the carrier frequency variation.")


# ---------------------------------------------------------------- 4.20
@_reg
def fig_f20():
    """Fig. 4.20 - frequency-modulated waveform."""
    o = [_wave_axes()]
    o.append(_fm_wave(66, 466, 112, 22))
    o.append(_side_label("Frequency-modulated wave"))
    return _mk(20, o, "Frequency-modulated waveform",
               "Dạng sóng điều chế tần số: biên độ không đổi nhưng khoảng cách các chu kỳ thay đổi",
               "Frequency-modulated waveform with constant amplitude and varying cycle spacing",
               "Đồ thị điều chế tần số: sóng mang giữ nguyên biên độ nhưng các chu kỳ bị nén và giãn theo tín hiệu; tần số tức thời thay đổi còn biên độ và pha không đổi.",
               "Frequency-modulation plot: the carrier keeps a constant amplitude while its cycles are compressed and stretched by the signal; the instantaneous frequency changes while amplitude and phase stay fixed.")


# ---------------------------------------------------------------- 4.21
@_reg
def fig_f21():
    """Fig. 4.21 - carrier wave for phase modulation (damped drawing)."""
    o = [_wave_axes()]
    o.append(_sine(66, 466, 112, 27, 4.6, taper=lambda t: (1.0 - t) ** 0.9))
    o.append(_side_label("Carrier wave"))
    return _mk(21, o, "Carrier wave for phase modulation",
               "Dạng sóng mang tần số cao có biên độ giảm dần về phía cuối như bản in",
               "High-frequency carrier wave whose amplitude tapers towards the end, as printed",
               "Đồ thị sóng mang trong điều chế pha: một chuỗi dao động tần số cao có biên độ giảm dần và kết thúc trên trục giữa.",
               "Carrier wave sketch for phase modulation: a train of high-frequency oscillations with gradually decreasing amplitude, ending at the centre line.")


# ---------------------------------------------------------------- 4.22
@_reg
def fig_f22():
    """Fig. 4.22 - signal wave for phase modulation."""
    o = [_wave_axes()]
    o.append(_sine(66, 466, 112, 26, 1.0))
    o.append(_side_label("Signal wave"))
    return _mk(22, o, "Signal wave for phase modulation",
               "Dạng tín hiệu điều chế một chu kỳ dùng để làm lệch pha sóng mang",
               "Single-cycle signal used to shift the phase of the carrier",
               "Đồ thị tín hiệu điều chế pha: một chu kỳ sin gồm nửa sóng dương và nửa sóng âm, giá trị tức thời của nó quyết định độ lệch pha.",
               "Phase-modulation signal plot: one sine cycle with positive and negative half waves; its instantaneous value decides the phase shift of the carrier.")


# ---------------------------------------------------------------- 4.23
@_reg
def fig_f23():
    """Fig. 4.23 - phase-modulated wave with phase reversals."""
    o = [_wave_axes()]
    o.append(_pm_wave(66, 466, 112, 27))
    o.append(_side_label("Modulated wave"))
    return _mk(23, o, "Phase-modulated waveshape",
               "Dạng sóng điều chế pha: sóng mang bị đảo pha đột ngột tại các vị trí xác định",
               "Phase-modulated wave with abrupt carrier phase reversals at set points",
               "Đồ thị điều chế pha: sóng mang bị đảo pha một nửa chu kỳ tại ba vị trí, tạo thành các vòng nối đặc trưng; biên độ và tần số được giữ nguyên.",
               "Phase-modulation sketch: the carrier reverses phase by half a cycle at three points, forming the characteristic loops; amplitude and frequency remain unchanged.")


# ---------------------------------------------------------------- 4.24
@_reg
def fig_f24():
    """Fig. 4.24 - pulse amplitude modulation (PAM)."""
    o = [_pulse_axes(110, 178, 470, 58, "Output", "Time")]
    xs = [134 + i * 16 for i in range(19)]
    peak = 286

    def env(x):
        return 66.0 * max(0.0, 1.0 - abs(x - peak) / 172.0)

    for x in xs:
        h = env(x)
        o.append(_line(x, 178, x, 178 - h, sw=1.6, color=BLUE))
        o.append(_line(x - 2, 178 - h, x + 2, 178 - h, sw=0.8, color=BLUE))
    o.append(_poly([(x, 178 - env(x)) for x in xs], sw=1.0, color=GREY,
                   dash="4,3"))
    o.append(_line(xs[-1], 178 - env(xs[-1]), 462, 168, sw=1.0, color=GREY,
                   dash="4,3"))
    o.append(_line(134, 193, 166, 193, sw=0.9, color=GREY))
    o.append(_line(134, 189, 134, 197, sw=0.9, color=GREY))
    o.append(_line(166, 189, 166, 197, sw=0.9, color=GREY))
    o.append(T(150, 208, "Time period", 6.5))
    return _mk(24, o, "Pulse amplitude modulation (PAM)",
               "Điều chế biên độ xung: các xung có chiều cao thay đổi theo tín hiệu",
               "Pulse amplitude modulation: pulse heights follow the signal value",
               "Đồ thị PAM: một dãy xung hẹp có tần số không đổi; chiều cao của từng xung nằm theo một đường bao hình tam giác tăng rồi giảm, biểu thị giá trị tín hiệu.",
               "PAM plot: a train of narrow pulses at constant frequency; each pulse height follows a triangular envelope that rises and falls, representing the signal value.")


# ---------------------------------------------------------------- 4.25
@_reg
def fig_f25():
    """Fig. 4.25 - pulse duration / width modulation (PDM/PWM)."""
    o = [_pulse_axes(100, 180, 490, 62, "Value", "Time")]
    pulses = [(160, 196), (270, 330), (400, 428)]
    for xa, xb in pulses:
        o.append(_rect(xa, 112, xb - xa, 68, fill="#eef3fb", sw=1.3))
    o.append(_dim(160, 270, 98, "t1", 92))
    o.append(_dim(270, 400, 98, "t2", 92))
    o.append(_dim(400, 490, 98, "t3", 92))
    o.append(_dim(160, 196, 195, "w1", 211))
    o.append(_dim(270, 330, 195, "w2", 211))
    o.append(_dim(400, 428, 195, "w3", 211))
    o.append(T(300, 226, "t1, t2, t3: duration    w1, w2, w3: width", 6.2))
    return _mk(25, o, "Pulse duration modulation (PDM/PWM)",
               "Điều chế độ rộng xung: biên độ không đổi, độ dài xung thể hiện giá trị tín hiệu",
               "Pulse duration modulation: constant amplitude, pulse width carries the signal value",
               "Đồ thị PDM hay PWM: ba xung có cùng biên độ nhưng độ rộng w1, w2, w3 khác nhau; khoảng thời gian t1, t2, t3 giữa các xung biểu thị giá trị tín hiệu.",
               "PDM or PWM plot: three pulses of equal amplitude but different widths w1, w2 and w3; the durations t1, t2 and t3 between pulses represent the signal value.")


# ---------------------------------------------------------------- 4.26
@_reg
def fig_f26():
    """Fig. 4.26 - pulse position modulation (PPM)."""
    o = [_pulse_axes(100, 180, 520, 62, "Value", "Time")]
    for x in (190, 320, 450):
        pts = [(x, 180), (x, 112)]
        for k in range(1, 31):
            t = k / 30.0
            pts.append((x + 26.0 * t, 180 - 68.0 * math.exp(-4.0 * t)))
        o.append(_poly(pts, sw=1.5, color=BLUE))
    o.append(_dim(170, 300, 98, "t1", 92))
    o.append(_dim(300, 430, 98, "t2", 92))
    o.append(_dim(430, 520, 98, "t3", 92))
    o.append(_dim(190, 216, 195, "w1", 211))
    o.append(_dim(320, 346, 195, "w2", 211))
    o.append(_dim(450, 476, 195, "w3", 211))
    o.append(T(310, 226, "w1, w2, w3: pulse width (constant)", 6.2))
    return _mk(26, o, "Pulse position modulation (PPM)",
               "Điều chế vị trí xung: các xung ngắn không đổi độ rộng được dời vị trí theo tín hiệu",
               "Pulse position modulation: short fixed-width pulses shifted in time by the signal",
               "Đồ thị PPM: ba xung ngắn có độ rộng không đổi, mỗi xung bắt đầu tại một vị trí t1, t2, t3 khác nhau trên trục thời gian; dạng xung có đuôi giảm dần như bản in.",
               "PPM plot: three short pulses of constant width, each starting at a different position t1, t2 and t3 on the time axis; each pulse has a decaying tail as in the printed figure.")


# ---------------------------------------------------------------- 4.27
@_reg
def fig_f27():
    """Fig. 4.27 - digital amplitude modulation, bits 01100101."""
    bits = "01100101"
    o = [_bit_grid(bits, 100, 55, 48, 174)]
    o.append(_bit_wave(bits, 100, 55, 64, 88))
    for i, b in enumerate(bits):
        o.append(T(100 + i * 55 + 27.5, 56, b, 7.2))
    o.append(_mod_carrier(bits, 100, 55, 140, 22, "am"))
    o.append(_ar(570, 142, 548, 142, sw=1.3))
    o.append(T(658, 146, "Amplitude modulation", 7.6, anchor="end"))
    return _mk(27, o, "Digital amplitude modulation",
               "Điều chế biên độ số cho chuỗi bit 01100101: biên độ sóng mang theo từng bit",
               "Digital amplitude modulation of bit pattern 01100101: carrier amplitude follows each bit",
               "Sơ đồ điều chế biên độ số cho chuỗi bit 01100101: hàng trên là dạng bit nhị phân, hàng dưới là sóng mang có biên độ lớn khi bit bằng 1 và nhỏ khi bit bằng 0.",
               "Digital amplitude-modulation diagram for bit pattern 01100101: the upper row is the binary bit stream, the lower row is a carrier with large amplitude for bit 1 and small amplitude for bit 0.")


# ---------------------------------------------------------------- 4.28
@_reg
def fig_f28():
    """Fig. 4.28 - digital frequency modulation, bits 01101001."""
    bits = "01101001"
    o = [_bit_grid(bits, 100, 55, 48, 174)]
    o.append(_bit_wave(bits, 100, 55, 64, 88))
    for i, b in enumerate(bits):
        o.append(T(100 + i * 55 + 27.5, 56, b, 7.2))
    o.append(_mod_carrier(bits, 100, 55, 140, 22, "fm"))
    o.append(_ar(570, 142, 548, 142, sw=1.3))
    o.append(T(658, 146, "Frequency modulation", 7.6, anchor="end"))
    return _mk(28, o, "Digital frequency modulation",
               "Điều chế tần số số cho chuỗi bit 01101001: tần số sóng mang theo từng bit",
               "Digital frequency modulation of bit pattern 01101001: carrier frequency follows each bit",
               "Sơ đồ điều chế tần số số cho chuỗi bit 01101001: hàng trên là dãy bit, hàng dưới là sóng mang giữ nguyên biên độ nhưng có nhiều chu kỳ hơn khi bit bằng 1 và ít hơn khi bit bằng 0.",
               "Digital frequency-modulation diagram for bit pattern 01101001: the upper row is the bit stream, the lower row is a carrier of constant amplitude with more cycles for bit 1 and fewer for bit 0.")


# ---------------------------------------------------------------- 4.29
@_reg
def fig_f29():
    """Fig. 4.29 - digital phase modulation, bits 1010011010."""
    bits = "1010011010"
    o = [_bit_grid(bits, 100, 44, 48, 174)]
    o.append(_bit_wave(bits, 100, 44, 64, 88))
    for i, b in enumerate(bits):
        o.append(T(100 + i * 44 + 22, 56, b, 7.2))
    o.append(_mod_carrier(bits, 100, 44, 140, 22, "pm"))
    o.append(_ar(570, 142, 548, 142, sw=1.3))
    o.append(T(658, 146, "Phase modulation", 7.6, anchor="end"))
    return _mk(29, o, "Digital phase modulation",
               "Điều chế pha số cho chuỗi bit 1010011010: pha sóng mang đảo theo từng bit",
               "Digital phase modulation of bit pattern 1010011010: carrier phase reverses per bit",
               "Sơ đồ điều chế pha số cho chuỗi bit 1010011010: hàng trên là dãy bit, hàng dưới là sóng mang có tần số và biên độ không đổi nhưng bị đảo pha khi giá trị bit thay đổi.",
               "Digital phase-modulation diagram for bit pattern 1010011010: the upper row is the bit stream, the lower row is a carrier of constant frequency and amplitude whose phase reverses when the bit value changes.")


# ---------------------------------------------------------------- 4.30
@_reg
def fig_f30():
    """Fig. 4.30 - SDS telemetry block diagram of a power system."""
    o = []
    # Power plant with three generating units
    o.append(_rect(40, 74, 120, 126, fill="#ffffff", sw=1.3))
    for i, lab in enumerate(("GU-1", "GU-2", "GU-3")):
        o.append(_b(50, 84 + i * 28, 100, 22, lab, fill="#eef3fb", size=8.0))
    o.append(_line(100, 162, 100, 176, sw=1.1))
    o.append(T(100, 190, "Power Plant", 7.5))
    o.append(_ar(160, 131, 192, 131, sw=1.4))
    # Step-up substation
    o.append(_b(192, 108, 68, 46, "SUS\n11/132\nKV", fill="#eef3fb",
                size=7.3))
    # Three-phase line from SUS to the receiving-end grid station
    ys = (122, 131, 140)
    for y in ys:
        o.append(_line(260, y, 374, y, sw=0.9))
    o.append(_coil_h(315, ys))
    # Two grid stations
    o.append(_b(374, 104, 86, 54, "GS\nReceiving\nend", fill="#eef3fb",
                size=7.3))
    o.append(_b(460, 104, 86, 54, "GS\nSending\nend", fill="#eef3fb",
                size=7.3))
    # Outgoing three-phase line
    for y in ys:
        o.append(_line(546, y, 636, y, sw=0.9))
    o.append(_coil_h(592, ys))
    # Upward feeders above the two grid stations
    for xs in ((388, 417, 446), (474, 503, 532)):
        for x in xs:
            o.append(_line(x, 104, x, 48, sw=0.9))
        o.append(_coil_v(76, xs))
    # Downward feeders: the left one reaches the step-down substation
    for xs, yb in (((388, 417, 446), 182), ((474, 503, 532), 186)):
        for x in xs:
            o.append(_line(x, 158, x, yb, sw=0.9))
        o.append(_coil_v(170, xs))
    o.append(_b(388, 182, 58, 40, "SDS\n132/11\nKV", fill="#eef3fb",
                size=7.0))
    return _mk(30, o, "SDS in electrical power system telemetry",
               "Sơ đồ khối hệ thống điện: nhà máy phát điện, trạm tăng áp SUS, hai trạm lưới GS và trạm giảm áp SDS",
               "Power-system block diagram: generating plant, step-up station SUS, two grid stations GS and step-down station SDS",
               "Sơ đồ khối telemetry trong hệ thống điện: ba tổ máy GU-1 đến GU-3 trong nhà máy phát điện nối qua trạm tăng áp SUS 11/132 KV tới hai trạm lưới GS đầu thu và đầu phát bằng đường dây ba pha; trạm lưới đầu thu nối xuống trạm giảm áp SDS 132/11 KV.",
               "Telemetry block diagram of an electrical power system: three generating units GU-1 to GU-3 in the power plant feed the step-up station SUS 11/132 KV; three-phase lines connect to the receiving-end and sending-end grid stations GS, and the receiving end feeds the step-down substation SDS 132/11 KV.")
