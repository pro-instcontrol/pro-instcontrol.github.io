# -*- coding: utf-8 -*-
"""Figures for Handbook Chapter 19 — Frequency Measurement (Michael A. Lombardi, NIST).

Source has 15 figures (19.1–19.15). FIGS is a 15-figure set.
"""
import math as _m

from hbfig import GOLD, INK, MUTED, TXT, _f, svg, _fig

E = "#2a2a2a"
G = "#b45309"
S = "#888888"
P = "#ffffff"


def _lbl(x, y, txt, cls="t", anchor="start"):
    return '<text class="%s" x="%s" y="%s" text-anchor="%s">%s</text>' % (
        cls, _f(x), _f(y), anchor, txt)


def _defs():
    return ('<defs>'
            '<marker id="ah19" markerWidth="9" markerHeight="9" refX="7" refY="3" '
            'orient="auto"><path d="M0,0 L7,3 L0,6 z" fill="%s"/></marker>'
            '<marker id="ah19g" markerWidth="9" markerHeight="9" refX="7" refY="3" '
            'orient="auto"><path d="M0,0 L7,3 L0,6 z" fill="%s"/></marker>'
            '</defs>' % (E, G))


def _arr(x1, y1, x2, y2, col=E, marker="ah19", sw=1.4):
    return ('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="%s" '
            'marker-end="url(#%s)"/>' % (_f(x1), _f(y1), _f(x2), _f(y2), col, sw, marker))


def _box(x, y, w, h, t, col=E, fill="#ffffff", fs=12):
    o = ['<rect x="%s" y="%s" width="%s" height="%s" rx="6" fill="%s" stroke="%s" stroke-width="1.4"/>'
         % (_f(x), _f(y), _f(w), _f(h), fill, col)]
    lines = t.split("\n")
    for i, ln in enumerate(lines):
        yy = y + h / 2.0 + (i - (len(lines) - 1) / 2.0) * (fs + 3) + fs * 0.35
        o.append(_lbl(x + w / 2.0, yy, ln, "tb", "middle"))
    return "".join(o)


def _frame(x0, y0, x1, y1):
    return '<rect x="%s" y="%s" width="%s" height="%s" fill="#fff" stroke="%s" stroke-width="1"/>' % (
        _f(x0), _f(y0), _f(x1 - x0), _f(y1 - y0), E)


# ---------------------------------------------------------------- 19.1
def fig_19_1():
    o = [_defs()]
    # top panel: perfectly linear phase
    o.append(_frame(60, 44, 620, 116))
    o.append('<line x1="72" y1="108" x2="608" y2="54" stroke="%s" stroke-width="2"/>' % G)
    o.append(_lbl(60, 34, "a) Không thấy biến thiên phi tuyến → TUR ≥ 10:1", "ts"))
    o.append(_lbl(340, 132, "thời gian", "ts", "middle"))
    o.append(_lbl(24, 84, "pha", "ts"))
    # bottom panel: small variation
    o.append(_frame(60, 156, 620, 228))
    pts = []
    for i in range(0, 101):
        x = 72 + 536 * i / 100.0
        y = 220 - 66 * i / 100.0 + 2.4 * _m.sin(i * 0.85)
        pts.append((x, y))
    o.append('<path d="M' + " L".join("%s %s" % p for p in pts) + '" fill="none" stroke="%s" stroke-width="2"/>' % G)
    o.append(_lbl(60, 146, "b) Biến thiên nhỏ → TUR &lt; 10:1 (sai số do chuẩn)", "ts"))
    o.append(_lbl(340, 244, "thời gian", "ts", "middle"))
    return _fig(
        svg(680, 256, "".join(o), "Hai đồ thị so sánh pha đơn giản"),
        "Hình 19.1 · Hai đồ thị so sánh pha đơn giản giữa thiết bị cần hiệu chuẩn và tần số chuẩn. "
        "Độ lệch tần số là một hàm tuyến tính; đồ thị trên không thấy biến thiên phi tuyến (TUR ≥ 10:1), "
        "đồ thị dưới có biến thiên nhỏ cho thấy TUR &lt; 10:1 và một phần không đảm bảo do chuẩn đóng góp.",
        "Figure 19.1 · Two simple phase-comparison graphs between a DUT and a reference. Frequency "
        "offset is linear; the top graph shows no discernible nonlinearity (TUR ≥ 10:1), the bottom "
        "shows a small variation indicating TUR &lt; 10:1 with some uncertainty from the reference.",
        "Hai đồ thị pha: trên tuyến tính hoàn hảo, dưới có dao động nhỏ",
        "Two phase graphs: top perfectly linear, bottom slightly wavy")


# ---------------------------------------------------------------- 19.2
def fig_19_2():
    o = [_defs()]
    # t1,t2,t3 vertical guides
    for tx, lab in ((120, "t₁"), (330, "t₂"), (560, "t₃")):
        o.append('<line x1="%d" y1="40" x2="%d" y2="220" stroke="%s" stroke-width="1" stroke-dasharray="4 4"/>' % (tx, tx, S))
        o.append(_lbl(tx, 34, lab, "ts", "middle"))
    # signal 1 (unstable after t2)
    pts = []
    for i in range(0, 221):
        x = 60 + 500 * i / 220.0
        t = i / 220.0
        if t < 0.5:
            f = 7.0
        else:
            f = 7.0 + 26.0 * (t - 0.5)
        y = 95 - 26 * _m.sin(2 * _m.pi * f * t)
        pts.append((x, y))
    o.append('<path d="M' + " L".join("%s %s" % p for p in pts) + '" fill="none" stroke="%s" stroke-width="1.8"/>' % G)
    o.append(_lbl(64, 60, "Tín hiệu 1: không ổn định (tần số dao động sau t₂)", "ts"))
    # signal 2 (stable)
    pts = []
    for i in range(0, 221):
        x = 60 + 500 * i / 220.0
        t = i / 220.0
        y = 185 - 26 * _m.sin(2 * _m.pi * 7.0 * t)
        pts.append((x, y))
    o.append('<path d="M' + " L".join("%s %s" % p for p in pts) + '" fill="none" stroke="%s" stroke-width="1.8"/>' % E)
    o.append(_lbl(64, 150, "Tín hiệu 2: ổn định (cùng tần số suốt)", "ts"))
    return _fig(
        svg(680, 232, "".join(o), "So sánh tần số không ổn định và ổn định"),
        "Hình 19.2 · So sánh tần số không ổn định và ổn định. Hai tín hiệu có cùng tần số giữa t₁ và t₂, "
        "nhưng tín hiệu 1 dao động tần số giữa t₂ và t₃ trong khi tín hiệu 2 giữ nguyên.",
        "Figure 19.2 · Comparison of unstable and stable frequencies. Both signals share the same "
        "frequency between t₁ and t₂, but signal 1 fluctuates between t₂ and t₃ while signal 2 does not.",
        "Hai dạng sóng: tín hiệu 1 đổi tần số sau t₂, tín hiệu 2 ổn định",
        "Two waveforms: signal 1 changes frequency after t₂, signal 2 stays stable")


# ---------------------------------------------------------------- 19.3
def fig_19_3():
    o = [_defs()]
    x0, y0, x1, y1 = 80, 200, 620, 44
    o.append(_frame(x0, y1, x1, y0))

    def X(tau):
        return x0 + (x1 - x0) * (_m.log10(tau) / 5.0)

    def Y(sig):
        return y0 - (y0 - y1) * ((_m.log10(sig) + 12.0) / 2.0)

    # decade gridlines
    for k in range(0, 6):
        xx = X(10 ** k)
        o.append('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="#eee" stroke-width="1"/>' % (_f(xx), _f(y1), _f(xx), _f(y0)))
        o.append(_lbl(xx, y0 + 14, "10^%d" % k, "ts", "middle"))
    for k in range(0, 3):
        yy = Y(10 ** (-12 + k))
        o.append('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="#eee" stroke-width="1"/>' % (_f(x0), _f(yy), _f(x1), _f(yy)))
        o.append(_lbl(x0 - 6, yy + 3, "1e-%d" % (12 - k), "ts", "end"))
    pts = []
    for i in range(0, 121):
        tau = 10 ** (5 * i / 120.0)
        sig = 5e-12 * (1 + _m.sqrt(100.0 / tau))
        pts.append((X(tau), Y(sig)))
    o.append('<path d="M' + " L".join("%s %s" % p for p in pts) + '" fill="none" stroke="%s" stroke-width="2.2"/>' % G)
    # flicker floor
    yf = Y(5e-12)
    o.append('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="1.4" stroke-dasharray="5 4"/>' % (_f(X(10)), _f(yf), _f(x1), _f(yf), E))
    o.append(_lbl(X(10) + 6, yf - 5, "sàn nhấp nháy ≈ 5 × 10⁻¹²", "ts"))
    o.append(_lbl((x0 + x1) / 2, 226, "thời gian lấy trung bình τ (s, thang log)", "ts", "middle"))
    o.append(_lbl(20, 60, "σ_y(τ)", "ts"))
    return _fig(
        svg(680, 236, "".join(o), "Đồ thị Allan deviation mẫu"),
        "Hình 19.3 · Đồ thị Allan deviation mẫu: độ ổn định cải thiện khi thời gian lấy trung bình dài hơn, "
        "cho tới khi đạt sàn nhấp nháy (flicker floor) — ở đây khoảng 5 × 10⁻¹² tại 100 s đối với một bộ "
        "dao động thạch anh.",
        "Figure 19.3 · A sample Allan-deviation graph: stability improves as the averaging time grows, "
        "until the flicker floor is reached — here about 5 × 10⁻¹² at 100 s for a quartz oscillator.",
        "Đồ thị Allan deviation giảm dần rồi chạm sàn nhấp nháy",
        "Allan deviation graph falling then flattening at the flicker floor")


# ---------------------------------------------------------------- 19.4
def fig_19_4():
    o = [_defs()]
    x0, y0, x1, y1 = 90, 210, 620, 50
    o.append(_frame(x0, y1, x1, y0))
    o.append(_arr(x0, y0, x1, y0, E, "ah19", 1.4))
    o.append(_arr(x0, y0, x0, y1, E, "ah19", 1.4))
    o.append(_lbl((x0 + x1) / 2, 232, "độ lệch tần số (độ chính xác) →", "ts", "middle"))
    o.append(_lbl(24, 70, "độ ổn định", "ts"))
    pts = [("ổn định +\nchính xác", 470, 92), ("chính xác nhưng\nkém ổn định", 470, 176),
           ("ổn định nhưng\nlệch tần số", 150, 92), ("kém cả hai", 150, 176)]
    for lab, px, py in pts:
        o.append('<circle cx="%d" cy="%d" r="5" fill="%s"/>' % (px, py, G))
        o.append(_lbl(px + 9, py + 4, lab.replace("\n", " "), "ts"))
    return _fig(
        svg(680, 246, "".join(o), "Quan hệ giữa độ không đảm bảo tần số và độ ổn định"),
        "Hình 19.4 · Quan hệ giữa độ không đảm bảo tần số (độ chính xác) và độ ổn định. Độ lệch tần số "
        "cho biết tần số đúng tới đâu; độ ổn định cho biết tần số có giữ nguyên hay không — hai đại lượng "
        "độc lập.",
        "Figure 19.4 · The relationship between frequency uncertainty (accuracy) and stability. Frequency "
        "offset says how close the frequency is to nominal; stability says whether it stays the same — "
        "the two are independent.",
        "Biểu đồ hai trục: độ lệch tần số và độ ổn định, với bốn điểm ví dụ",
        "Two-axis chart of frequency offset versus stability with four example points")


# ---------------------------------------------------------------- 19.5
def fig_19_5():
    o = [_defs()]
    # amplifier triangle
    o.append('<polygon points="150,70 150,150 240,110" fill="#fff" stroke="%s" stroke-width="1.6"/>' % E)
    o.append(_lbl(160, 114, "bộ khuếch đại", "ts"))
    # crystal box
    o.append(_box(360, 84, 110, 52, "tinh thể\nthạch anh"))
    # forward path
    o.append(_arr(240, 110, 360, 110, G, "ah19g", 1.6))
    # feedback loop (bottom)
    o.append('<path d="M470 136 L470 190 L150 190 L150 150" fill="none" stroke="%s" stroke-width="1.6" marker-end="url(#ah19)"/>' % E)
    o.append(_lbl(300, 206, "hồi tiếp: tinh thể tạo điện áp dao động (hiệu ứng áp điện)", "ts", "middle"))
    o.append(_arr(150, 110, 150, 70, E, "ah19", 1.2))
    return _fig(
        svg(680, 220, "".join(o), "Sơ đồ khối bộ dao động thạch anh"),
        "Hình 19.5 · Sơ đồ khối bộ dao động thạch anh. Bộ khuếch đại cung cấp năng lượng để duy trì dao "
        "động; tinh thể thạch anh trong vòng hồi tiếp tạo điện áp dao động nhờ hiệu ứng áp điện.",
        "Figure 19.5 · Block diagram of a quartz oscillator. The amplifier supplies the energy to sustain "
        "oscillation; the quartz crystal in the feedback loop produces the oscillating voltage via the "
        "piezoelectric effect.",
        "Sơ đồ khối: bộ khuếch đại và tinh thể thạch anh trong vòng hồi tiếp",
        "Block diagram: amplifier and quartz crystal in a feedback loop")


# ---------------------------------------------------------------- 19.6
def fig_19_6():
    o = [_defs()]
    x0, y0, x1, y1 = 80, 190, 620, 50
    o.append(_frame(x0, y1, x1, y0))
    mid = (y0 + y1) / 2.0
    o.append('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="#ccc" stroke-width="1"/>' % (_f(x0), _f(mid), _f(x1), _f(mid)))
    pts = []
    for i in range(0, 301):
        x = x0 + (x1 - x0) * i / 300.0
        n = 26 * _m.sin(i * 1.9) + 14 * _m.sin(i * 0.53 + 1.0) + 8 * _m.sin(i * 4.1 + 2.0)
        pts.append((x, mid - n))
    o.append('<path d="M' + " L".join("%s %s" % p for p in pts) + '" fill="none" stroke="%s" stroke-width="1.2"/>' % G)
    o.append(_lbl(x0, y0 + 14, "0", "ts"))
    o.append(_lbl(x1, y0 + 14, "100 s", "ts", "end"))
    o.append(_lbl(24, 84, "pha (ns)", "ts"))
    o.append(_lbl((x0 + x1) / 2, 208, "nhiễu đường truyền ≈ ±200 ns", "ts", "middle"))
    return _fig(
        svg(680, 220, "".join(o), "Biến thiên đường truyền LORAN-C trong 100 s"),
        "Hình 19.6 · Biến thiên đường truyền LORAN-C trong khoảng đo 100 s (chuỗi 8970 thu tại Boulder, CO). "
        "Biên độ nhiễu đường truyền khoảng 200 ns.",
        "Figure 19.6 · LORAN-C path variations over a 100 s measurement (chain 8970 received in Boulder, "
        "CO). The path-noise range is about 200 ns.",
        "Dải nhiễu ngang khoảng 200 ns của đường LORAN-C",
        "Horizontal noise band of about 200 ns for the LORAN-C path")


# ---------------------------------------------------------------- 19.7
def fig_19_7():
    o = [_defs()]
    x0, y0, x1, y1 = 80, 200, 620, 44
    o.append(_frame(x0, y1, x1, y0))
    pts = []
    for i in range(0, 301):
        x = x0 + (x1 - x0) * i / 300.0
        base = (y0 - 20) - (y0 - y1 - 40) * (i / 300.0)  # downward slope
        n = 10 * _m.sin(i * 1.3) + 7 * _m.sin(i * 0.47 + 1.0)
        pts.append((x, base - n))
    o.append('<path d="M' + " L".join("%s %s" % p for p in pts) + '" fill="none" stroke="%s" stroke-width="1.1"/>' % G)
    # least-squares line
    o.append('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="2.4"/>'
             % (_f(x0 + 8), _f(y0 - 22), _f(x1 - 8), _f(y0 - 22 - (y0 - y1 - 40) * (300 - 16) / 300.0), E))
    o.append(_lbl(x0, y0 + 14, "0", "ts"))
    o.append(_lbl(x1, y0 + 14, "96 h", "ts", "end"))
    o.append(_lbl(24, 90, "pha (ns)", "ts"))
    o.append(_lbl((x0 + x1) / 2, 218, "đường hồi quy bình phương nhỏ nhất: tần số thấp hơn ≈ 3,4 × 10⁻¹²", "ts", "middle"))
    return _fig(
        svg(680, 230, "".join(o), "So sánh LORAN-C với bộ dao động xêzi trong 96 giờ"),
        "Hình 19.7 · So sánh LORAN-C với một bộ dao động xêzi trong khoảng 96 giờ. Đường đậm là ước lượng "
        "bình phương nhỏ nhất của độ lệch tần số; độ dốc cho thấy bộ xêzi thấp tần số khoảng 3,4 × 10⁻¹².",
        "Figure 19.7 · LORAN-C compared with a cesium oscillator over 96 h. The thick line is the "
        "least-squares estimate of the frequency offset; its slope shows the cesium is low by about "
        "3.4 × 10⁻¹².",
        "Dữ liệu nhiễu với đường hồi quy dốc xuống trong 96 giờ",
        "Noisy data with a downward regression line over 96 h")


# ---------------------------------------------------------------- 19.8
def fig_19_8():
    o = [_defs()]
    x0, y0, x1, y1 = 80, 180, 620, 60
    o.append(_frame(x0, y1, x1, y0))
    mid = (y0 + y1) / 2.0
    o.append('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="#ccc" stroke-width="1"/>' % (_f(x0), _f(mid), _f(x1), _f(mid)))
    pts = []
    for i in range(0, 301):
        x = x0 + (x1 - x0) * i / 300.0
        n = 12 * _m.sin(i * 2.1) + 7 * _m.sin(i * 0.61 + 1.0) + 4 * _m.sin(i * 4.7 + 2.0)
        pts.append((x, mid - n))
    o.append('<path d="M' + " L".join("%s %s" % p for p in pts) + '" fill="none" stroke="%s" stroke-width="1.1"/>' % G)
    o.append(_lbl(x0, y0 + 14, "0", "ts"))
    o.append(_lbl(x1, y0 + 14, "100 s", "ts", "end"))
    o.append(_lbl(24, 84, "pha (ns)", "ts"))
    o.append(_lbl((x0 + x1) / 2, 198, "nhiễu do biến thiên đường GPS và SA; tổng dịch pha &lt; 1 ns", "ts", "middle"))
    return _fig(
        svg(680, 210, "".join(o), "So sánh GPS với bộ dao động xêzi trong 100 s"),
        "Hình 19.8 · So sánh GPS với một bộ dao động xêzi trong khoảng 100 s. Bộ xêzi có độ lệch tần số "
        "khoảng 1 × 10⁻¹³ nên dịch pha tích luỹ dưới 1 ns; nhiễu trên đồ thị là do biến thiên đường GPS và SA.",
        "Figure 19.8 · GPS compared with a cesium oscillator over 100 s. The cesium offset is about "
        "1 × 10⁻¹³, so accumulated phase is under 1 ns; the noise is from GPS path variations and SA.",
        "Dải nhiễu GPS dưới 1 ns trong 100 giây",
        "GPS noise band under 1 ns over 100 s")


# ---------------------------------------------------------------- 19.9
def fig_19_9():
    o = [_defs()]
    x0, y0, x1, y1 = 80, 200, 620, 44
    o.append(_frame(x0, y1, x1, y0))
    pts = []
    for i in range(0, 301):
        x = x0 + (x1 - x0) * i / 300.0
        base = (y0 - 24) - (y0 - y1 - 40) * (i / 300.0)
        n = 12 * _m.sin(i * 1.1) + 8 * _m.sin(i * 0.43 + 1.0)
        pts.append((x, base - n))
    o.append('<path d="M' + " L".join("%s %s" % p for p in pts) + '" fill="none" stroke="%s" stroke-width="1.1"/>' % G)
    o.append('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="2.4"/>'
             % (_f(x0 + 8), _f(y0 - 26), _f(x1 - 8), _f(y0 - 26 - (y0 - y1 - 40) * (284) / 300.0), E))
    o.append(_lbl(x0, y0 + 14, "0", "ts"))
    o.append(_lbl(x1, y0 + 14, "1 tuần", "ts", "end"))
    o.append(_lbl(24, 90, "pha (ns)", "ts"))
    o.append(_lbl((x0 + x1) / 2, 218, "biên độ dữ liệu 550 ns; xu hướng tuyến tính: xêzi thấp ≈ 5 × 10⁻¹³", "ts", "middle"))
    return _fig(
        svg(680, 230, "".join(o), "So sánh GPS với bộ dao động xêzi trong 1 tuần"),
        "Hình 19.9 · So sánh GPS với cùng bộ dao động xêzi trong 1 tuần. Biên độ dữ liệu 550 ns; đường "
        "hồi quy cho thấy xu hướng tuyến tính do độ lệch tần số của xêzi, tức bộ xêzi thấp khoảng 5 × 10⁻¹³.",
        "Figure 19.9 · GPS compared with the same cesium oscillator over one week. The data range is "
        "550 ns; the regression line shows the linear trend of the cesium offset — the cesium is low by "
        "about 5 × 10⁻¹³.",
        "Dữ liệu nhiễu biên độ 550 ns với xu hướng tuyến tính trong 1 tuần",
        "Noisy 550 ns data with a linear trend over one week")


# ---------------------------------------------------------------- 19.10
def fig_19_10():
    o = [_defs()]
    # supply dashed lines
    for yv in (50, 210):
        o.append('<line x1="60" y1="%d" x2="620" y2="%d" stroke="%s" stroke-width="1" stroke-dasharray="6 4"/>' % (yv, yv, S))
    o.append(_lbl(624, 54, "nguồn (5–15 V)", "ts"))
    # four waveform panels
    base = 130
    # 1 sine
    pts = [(60 + 130 * i / 60.0, base - 34 * _m.sin(2 * _m.pi * i / 60.0)) for i in range(0, 61)]
    o.append('<path d="M' + " L".join("%s %s" % p for p in pts) + '" fill="none" stroke="%s" stroke-width="1.8"/>' % G)
    # 2 square
    pts = []
    for i in range(0, 61):
        x = 200 + 130 * i / 60.0
        y = base - 34 if (i // 10) % 2 == 0 else base + 34
        pts.append((x, y))
    o.append('<path d="M' + " L".join("%s %s" % p for p in pts) + '" fill="none" stroke="%s" stroke-width="1.8"/>' % E)
    # 3 pulse
    pts = []
    for i in range(0, 61):
        x = 340 + 130 * i / 60.0
        on = (i % 20) < 4
        y = base - 34 if on else base + 34
        pts.append((x, y))
    o.append('<path d="M' + " L".join("%s %s" % p for p in pts) + '" fill="none" stroke="%s" stroke-width="1.8"/>' % G)
    # 4 clipped sine
    pts = []
    for i in range(0, 61):
        x = 480 + 130 * i / 60.0
        v = 52 * _m.sin(2 * _m.pi * i / 60.0)
        v = max(-34, min(34, v))
        pts.append((x, base - v))
    o.append('<path d="M' + " L".join("%s %s" % p for p in pts) + '" fill="none" stroke="%s" stroke-width="1.8"/>' % E)
    for x, lab in ((60, "sin"), (200, "vuông"), (340, "xung"), (480, "sin cắt")):
        o.append(_lbl(x, 232, lab, "ts"))
    return _fig(
        svg(680, 244, "".join(o), "Các dạng đầu ra của bộ dao động"),
        "Hình 19.10 · Các dạng tín hiệu đầu ra của bộ dao động: sin, sóng vuông, xung và sin bị cắt. "
        "Đường đứt nét là điện áp nguồn (5–15 V với CMOS), đường đậm là điện áp ra.",
        "Figure 19.10 · Oscillator output waveforms: sine, square, pulse and clipped sine. Dashed lines "
        "are the supply rails (5–15 V for CMOS), bold lines the output voltage.",
        "Bốn dạng sóng đầu ra: sin, vuông, xung, sin cắt, giữa hai mức nguồn",
        "Four output waveforms — sine, square, pulse, clipped sine — between supply rails")


# ---------------------------------------------------------------- 19.11
def fig_19_11():
    o = [_defs()]
    o.append('<line x1="60" y1="120" x2="620" y2="120" stroke="#ccc" stroke-width="1"/>')
    pts = [(80 + 500 * i / 120.0, 120 - 60 * _m.sin(2 * _m.pi * i / 120.0)) for i in range(0, 121)]
    o.append('<path d="M' + " L".join("%s %s" % p for p in pts) + '" fill="none" stroke="%s" stroke-width="2"/>' % G)
    o.append(_arr(80, 120, 580, 120, E, "ah19", 1.2))
    o.append(_lbl(590, 124, "t", "ts"))
    # period marker
    o.append('<line x1="80" y1="150" x2="580" y2="150" stroke="%s" stroke-width="1" stroke-dasharray="4 3"/>' % S)
    o.append(_lbl(330, 166, "một chu kỳ = 2π rad pha = T", "ts", "middle"))
    return _fig(
        svg(680, 180, "".join(o), "Một tín hiệu dao động hình sin"),
        "Hình 19.11 · Một tín hiệu dao động hình sin: trong một chu kỳ T, tín hiệu hoàn thành một vòng "
        "(2π radian pha).",
        "Figure 19.11 · An oscillating sine signal: in one period T the signal completes one cycle "
        "(2π radians of phase).",
        "Sóng sin một chu kỳ với chú thích chu kỳ T và 2π pha",
        "One-cycle sine wave annotated with period T and 2π phase")


# ---------------------------------------------------------------- 19.12
def fig_19_12():
    o = [_defs()]
    # DUT sine (top)
    p1 = [(70 + 520 * i / 240.0, 80 - 30 * _m.sin(2 * _m.pi * i / 60.0)) for i in range(0, 241)]
    o.append('<path d="M' + " L".join("%s %s" % p for p in p1) + '" fill="none" stroke="%s" stroke-width="1.8"/>' % G)
    o.append(_lbl(72, 46, "DUT", "ts"))
    # reference sine (bottom), slightly different frequency
    p2 = [(70 + 520 * i / 240.0, 160 - 30 * _m.sin(2 * _m.pi * i / 58.0)) for i in range(0, 241)]
    o.append('<path d="M' + " L".join("%s %s" % p for p in p2) + '" fill="none" stroke="%s" stroke-width="1.8"/>' % E)
    o.append(_lbl(72, 126, "chuẩn", "ts"))
    # phase bars widening
    for k in range(0, 6):
        x = 110 + k * 78
        w = 4 + k * 7
        o.append('<rect x="%d" y="204" width="%d" height="12" fill="%s"/>' % (x, w, G))
    o.append(_lbl(70, 232, "hiệu pha giữa hai tín hiệu tăng dần → DUT lệch tần số", "ts"))
    return _fig(
        svg(680, 244, "".join(o), "Hai tín hiệu có quan hệ pha thay đổi"),
        "Hình 19.12 · Hai tín hiệu có quan hệ pha thay đổi: sóng trên từ DUT, sóng dưới từ chuẩn. Các "
        "“cột” hiệu pha ở dưới rộng dần, cho thấy DUT có độ lệch tần số không đổi so với chuẩn.",
        "Figure 19.12 · Two signals with a changing phase relationship: the top wave is the DUT, the "
        "bottom the reference. The phase-difference bars widen, showing the DUT has a constant frequency "
        "offset.",
        "Hai sóng sin lệch tần số với các cột hiệu pha rộng dần",
        "Two sine waves of different frequency with widening phase-difference bars")


# ---------------------------------------------------------------- 19.13
def fig_19_13():
    o = [_defs()]
    # start pulse A
    o.append('<line x1="60" y1="60" x2="150" y2="60" stroke="%s" stroke-width="2"/>' % E)
    o.append('<line x1="150" y1="60" x2="150" y2="120" stroke="%s" stroke-width="2"/>' % E)
    o.append('<line x1="150" y1="120" x2="620" y2="120" stroke="%s" stroke-width="2"/>' % E)
    o.append(_lbl(60, 52, "A: xung khởi động", "ts"))
    # stop pulse B
    o.append('<line x1="60" y1="150" x2="360" y2="150" stroke="%s" stroke-width="2"/>' % G)
    o.append('<line x1="360" y1="150" x2="360" y2="210" stroke="%s" stroke-width="2"/>' % G)
    o.append('<line x1="360" y1="210" x2="620" y2="210" stroke="%s" stroke-width="2"/>' % G)
    o.append(_lbl(60, 142, "B: xung dừng", "ts"))
    # gate region
    o.append('<line x1="150" y1="228" x2="360" y2="228" stroke="%s" stroke-width="1.4" stroke-dasharray="4 3"/>' % S)
    o.append(_lbl(255, 244, "khoảng thời gian đo (đếm chu kỳ timebase)", "ts", "middle"))
    o.append('<line x1="150" y1="236" x2="150" y2="222" stroke="%s"/>' % S)
    o.append('<line x1="360" y1="236" x2="360" y2="222" stroke="%s"/>' % S)
    return _fig(
        svg(680, 254, "".join(o), "Đo khoảng thời gian bằng bộ đếm khoảng thời gian"),
        "Hình 19.13 · Đo khoảng thời gian: bộ đếm (TIC) bắt đầu đo khi tín hiệu khởi động A đạt mức "
        "trigger và dừng khi tín hiệu dừng B đạt mức trigger; khoảng thời gian được đo bằng cách đếm chu "
        "kỳ của timebase.",
        "Figure 19.13 · Measuring a time interval: the TIC starts when start signal A reaches its trigger "
        "level and stops when stop signal B does; the interval is measured by counting timebase cycles.",
        "Hai xung khởi động và dừng với khoảng đo được đánh dấu",
        "Start and stop pulses with the measured interval marked")


# ---------------------------------------------------------------- 19.14
def fig_19_14():
    o = [_defs()]
    o.append(_box(40, 50, 120, 50, "DUT"))
    o.append(_box(40, 150, 120, 50, "Chuẩn"))
    o.append(_box(240, 50, 120, 50, "chia tần"))
    o.append(_box(240, 150, 120, 50, "chia tần"))
    o.append(_box(430, 96, 120, 60, "TIC"))
    o.append(_box(590, 96, 80, 60, "máy\ntính"))
    o.append(_arr(160, 75, 240, 75, G, "ah19g", 1.4))
    o.append(_arr(160, 175, 240, 175, G, "ah19g", 1.4))
    o.append(_arr(360, 75, 430, 115, G, "ah19g", 1.4))
    o.append(_arr(360, 175, 430, 137, E, "ah19", 1.4))
    o.append(_arr(550, 126, 590, 126, E, "ah19", 1.4))
    o.append(_lbl(245, 90, "1 Hz", "ts"))
    return _fig(
        svg(680, 230, "".join(o), "Hệ đo khoảng thời gian"),
        "Hình 19.14 · Hệ đo khoảng thời gian: DUT và tần số chuẩn được chia xuống tần số thấp (thường 1 Hz) "
        "rồi đưa vào bộ đếm khoảng thời gian (TIC) để đo và ghi lại hiệu giữa hai tín hiệu.",
        "Figure 19.14 · A time-interval system: the DUT and reference are divided down to a low frequency "
        "(typically 1 Hz) and fed to a time-interval counter (TIC) that measures and records the difference.",
        "Sơ đồ hệ đo khoảng thời gian: DUT và chuẩn qua bộ chia tới TIC rồi máy tính",
        "Time-interval system: DUT and reference through dividers to a TIC and computer")


# ---------------------------------------------------------------- 19.15
def fig_19_15():
    o = [_defs()]
    o.append(_box(40, 40, 130, 50, "Chuẩn"))
    o.append(_box(40, 170, 130, 50, "DUT"))
    o.append(_box(250, 40, 140, 50, "bộ tổng hợp\ntần số"))
    o.append(_box(250, 96, 110, 50, "trộn 1"))
    o.append(_box(250, 176, 110, 50, "trộn 2"))
    o.append(_box(430, 96, 130, 70, "dò điểm\nkhông"))
    o.append(_box(430, 186, 130, 40, "bộ đếm sự kiện"))
    o.append(_box(590, 116, 80, 60, "máy\ntính"))
    o.append(_arr(170, 65, 250, 65, G, "ah19g", 1.3))
    o.append(_arr(170, 195, 250, 200, G, "ah19g", 1.3))
    o.append(_arr(320, 90, 305, 96, E, "ah19", 1.2))
    o.append(_arr(320, 90, 305, 176, E, "ah19", 1.2))
    o.append(_arr(360, 121, 430, 121, G, "ah19g", 1.3))
    o.append(_arr(360, 201, 430, 201, E, "ah19", 1.3))
    o.append(_arr(495, 166, 495, 186, E, "ah19", 1.3))
    o.append(_arr(560, 140, 590, 140, E, "ah19", 1.3))
    o.append(_lbl(240, 156, "trộn với cả hai", "ts"))
    return _fig(
        svg(680, 240, "".join(o), "Hệ dual mixer time difference"),
        "Hình 19.15 · Hệ Dual Mixer Time Difference (DMTD): bộ tổng hợp tần số khoá theo chuẩn tạo tần số "
        "thấp hơn DUT; tần số này được trộn với cả chuẩn lẫn DUT để tạo hai tần số phách lệch pha tỉ lệ "
        "với chênh lệch thời gian. Bộ dò điểm không và bộ đếm sự kiện đo pha thô, TIC đo phần lẻ, cho phép "
        "đo độ ổn định ngắn hạn tốt hơn nhiều so với hệ đo khoảng thời gian.",
        "Figure 19.15 · The Dual Mixer Time Difference (DMTD) system: a synthesizer locked to the reference "
        "produces a frequency below the DUT; mixing it with both reference and DUT yields two beat "
        "frequencies out of phase by an amount proportional to the time difference. A zero-crossing "
        "detector and event counter measure coarse phase, a TIC the fractional part, giving far better "
        "short-term stability measurement than a time-interval system.",
        "Sơ đồ DMTD: chuẩn và DUT trộn với bộ tổng hợp, qua bộ dò điểm không và bộ đếm tới máy tính",
        "DMTD diagram: reference and DUT mixed with a synthesizer, through zero-crossing detector and counter to computer")


FIGS = [fig_19_1, fig_19_2, fig_19_3, fig_19_4, fig_19_5, fig_19_6, fig_19_7, fig_19_8,
        fig_19_9, fig_19_10, fig_19_11, fig_19_12, fig_19_13, fig_19_14, fig_19_15]


def fig(n):
    return FIGS[n - 1]()
