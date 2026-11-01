# -*- coding: utf-8 -*-
"""Figures for Handbook Chapter 101 — Measurement and Identification of Brush,
Brushless, and dc Stepping Motors (S. Schweid, R. Lofthus, J. McInroy).

The source chapter contains exactly five figures (101.1–101.5); the set below
is those five, nothing padded.
"""
from hbfig import _f, svg, _fig, Box

E = "#2a2a2a"
S = "#888888"


def _lbl(x, y, txt, cls="t", anchor="start"):
    return ('<text class="%s" x="%s" y="%s" text-anchor="%s">%s</text>'
            % (cls, _f(x), _f(y), anchor, txt))


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
            '<marker id="a101" markerWidth="9" markerHeight="9" refX="7" refY="3" '
            'orient="auto"><path d="M0,0 L7,3 L0,6 z" fill="%s"/></marker>'
            '</defs>' % E)


def _arr(x1, y1, x2, y2, sw=1.4):
    return ('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="%s" '
            'marker-end="url(#a101)"/>'
            % (_f(x1), _f(y1), _f(x2), _f(y2), E, sw))


def _line(x1, y1, x2, y2, sw=1.4, col=E, dash=""):
    d = ' stroke-dasharray="%s"' % dash if dash else ""
    return ('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="%s"%s/>'
            % (_f(x1), _f(y1), _f(x2), _f(y2), col, sw, d))


def _rect(x, y, w, h, sw=1.4, dash=""):
    d = ' stroke-dasharray="%s"' % dash if dash else ""
    return ('<rect x="%s" y="%s" width="%s" height="%s" fill="#fff" stroke="%s" '
            'stroke-width="%s"%s/>' % (_f(x), _f(y), _f(w), _f(h), E, sw, d))


def _block(x, y, w, h, parts):
    """A block whose label is (parts, anchor-y-offset) with real subscripts."""
    return _rect(x, y, w, h) + _subs(x + w / 2.0, y + h / 2.0 + 4, parts, "middle")


def _sum(cx, cy, r=12, minus=False):
    o = ['<circle cx="%s" cy="%s" r="%s" fill="#fff" stroke="%s" stroke-width="1.4"/>'
         % (_f(cx), _f(cy), _f(r), E)]
    o.append(_lbl(cx - 8, cy - 1, "+", "ts"))
    if minus:
        o.append(_lbl(cx - 8, cy + 13, "−", "ts"))
    return "".join(o)


def _out(x, yc, txt):
    return _lbl(x, yc - 10, txt, "ts")


# ---------------------------------------------------------------- 101.1
def fig_101_1():
    """Torque–speed curve on a log speed axis, roll-off fitted to the print."""
    b = Box(560, 250, (0, 4), (0, 1.0), pad=(64, 30, 22, 44))
    body = b.axes("bước trên giây (thang log)", "mômen (Nm)",
                  xt=[(0, "10⁰"), (1, "10¹"), (2, "10²"), (3, "10³"), (4, "10⁴")],
                  yt=[(0, "0"), (0.2, "0,2"), (0.4, "0,4"), (0.6, "0,6"),
                      (0.8, "0,8"), (1.0, "1")])
    # T(f) = 1 / (1 + (f/fc)^n), fc = 348 steps/s, n = 0.887 — fitted to the
    # printed curve (≈0,75 at 10², ≈0,28 at 10³, ≈0,05 at 10⁴)
    pts = []
    for i in range(0, 241):
        lg = i / 240.0 * 4.0
        f = 10 ** lg
        pts.append((lg, 1.0 / (1.0 + (f / 348.0) ** 0.887)))
    body += b.curve(pts)
    body += _lbl(112, 22, "Đường đặc tính mômen – tốc độ của động cơ bước lai", "ts")
    return _fig(svg(560, 250, _defs() + body,
                    "Đường cong mômen theo tốc độ của động cơ bước lai, giảm dần khi tốc độ tăng"),
                "Hình 101.1 · Đường đặc tính mômen – tốc độ điển hình. Mômen khả dụng gần như không "
                "đổi ở tốc độ thấp rồi giảm nhanh khi số bước trên giây tăng; động cơ chỉ được chọn "
                "khi đường này nằm trên mômen yêu cầu ở mọi tốc độ.",
                "Figure 101.1 · Typical torque–speed curve. The available torque is nearly flat at low "
                "speed and falls away as the step rate rises; a motor is adequate only where this "
                "curve stays above the torque the load demands at every speed.",
                "Đồ thị mômen theo số bước trên giây: đường cong phẳng ở tốc độ thấp rồi giảm dần",
                "Torque against steps per second: flat at low speed then falling")


# ---------------------------------------------------------------- 101.2
def _switch_pair(cx, cy, hw=14, hh=12):
    """Two devices in parallel between two bars — one switch position."""
    o = [_line(cx - hw, cy - hh, cx + hw, cy - hh, 1.2),
         _line(cx - hw, cy + hh, cx + hw, cy + hh, 1.2)]
    for dx in (-hw, 1):
        o.append(_rect(cx + dx, cy - hh, 13, 2 * hh, 1.2))
    return "".join(o)


def fig_101_2():
    """H-bridge fed from a single 24 V rail, driven by a 75 % duty logic signal."""
    o = [_defs()]
    top, bot, ymid = 48, 176, 108
    xl, xr = 180, 380
    o.append(_line(xl, top, xr, top, 1.6))
    o.append(_line(xl, bot, xr, bot, 1.6))
    o.append(_lbl((xl + xr) / 2.0, top - 10, "24 V", "t", "middle"))
    for x in (xl, xr):
        o.append(_line(x, top, x, 66))
        o.append(_switch_pair(x, 78))
        o.append(_line(x, 90, x, 126))
        o.append(_switch_pair(x, 138))
        o.append(_line(x, 150, x, bot))
    # motor between the two midpoints
    o.append(_line(xl, ymid, 248, ymid))
    o.append(_rect(248, ymid - 22, 64, 44))
    o.append(_lbl(280, ymid + 4, "Motor", "t", "middle"))
    o.append(_line(312, ymid, xr, ymid))
    # ground
    o.append(_line((xl + xr) / 2.0, bot, (xl + xr) / 2.0, bot + 14))
    for i, w in enumerate((20, 12, 5)):
        o.append(_line((xl + xr) / 2.0 - w / 2.0, bot + 14 + i * 4,
                       (xl + xr) / 2.0 + w / 2.0, bot + 14 + i * 4))
    # 75 % duty logic signal driving the bridge
    o.append(_arr(152, 236, 152, bot + 2))
    o.append(_lbl(144, 256, "V", "t", "end"))
    o.append(_subs(144, 259, [("logic", True)], "end"))
    lo, hi, x0, P, HI = 270, 246, 176, 76, 57
    pts = [(x0, lo)]
    x = x0
    for _ in range(3):
        pts += [(x, hi), (x + HI, hi), (x + HI, lo), (x + P, lo)]
        x += P
    pts += [(x, hi), (x + HI, hi)]
    d = "M" + " L".join("%s %s" % (_f(a), _f(b)) for a, b in pts)
    o.append('<path d="%s" fill="none" stroke="%s" stroke-width="1.6"/>' % (d, E))
    o.append(_lbl(x0 + 112, lo + 22, "chu kỳ làm việc 75 %", "ts", "middle"))
    return _fig(svg(560, 300, "".join(o),
                    "Cầu H bốn nhánh nuôi từ một nguồn 24 V, điều khiển bằng tín hiệu số có chu kỳ làm việc 75 phần trăm"),
                "Hình 101.2 · Bộ khuếch đại PWM được đặt để cấp 12 V cho động cơ. Cầu H chỉ có thể nối "
                "động cơ với +24 V, với −24 V hoặc để hở; điện áp trung bình 12 V có được nhờ chu kỳ "
                "làm việc 75 % của tín hiệu logic.",
                "Figure 101.2 · PWM amplifier set to deliver 12 V to the motor. The H-bridge can only "
                "connect the motor to +24 V, to −24 V, or leave it open; the 12 V average comes from "
                "the 75 % duty cycle of the logic signal.",
                "Sơ đồ cầu H: bốn nhánh khóa, động cơ ở giữa, nguồn 24 V và dạng xung chu kỳ 75 phần trăm",
                "H-bridge: four switch positions around the motor, 24 V rail, 75 percent duty waveform")


# ---------------------------------------------------------------- 101.3
def fig_101_3():
    o = [_defs()]
    yc, bh = 88, 54
    by = yc - bh / 2.0
    o.append(_lbl(14, yc + 4, "Tham chiếu", "t"))
    o.append(_arr(80, yc, 92, yc))
    o.append(_sum(106, yc, minus=True))
    o.append(_arr(118, yc, 148, yc))
    o.append(_block(148, by, 110, bh, [("Controller", False)]))
    o.append(_subs(203, yc + 15, [("G", False), ("c", True)], "middle"))
    o.append(_arr(258, yc, 318, yc))
    o.append(_block(318, by, 100, bh, [("Amp", False)]))
    o.append(_subs(368, yc + 15, [("K", False), ("AMP", True)], "middle"))
    o.append(_arr(418, yc, 468, yc))
    o.append(_block(468, by, 100, bh, [("System", False)]))
    o.append(_subs(518, yc + 15, [("G", False), ("m", True)], "middle"))
    o.append(_arr(568, yc, 648, yc))
    o.append(_out(598, yc, "Đầu ra"))
    o.append(_arr(518, 20, 518, by - 2))
    o.append(_subs(526, 32, [("T", False), ("ext", True)]))
    o.append(_line(612, yc, 612, 154))
    o.append(_line(612, 154, 106, 154))
    o.append(_arr(106, 154, 106, yc + 13))
    return _fig(svg(660, 186, "".join(o),
                    "Sơ đồ khối vòng kín: tham chiếu, bộ điều khiển, bộ khuếch đại, đối tượng và mạch phản hồi"),
                "Hình 101.3 · Hệ vòng kín điển hình. Ngõ ra được đưa ngược về bộ cộng; mômen ngoài "
                "T<sub>ext</sub> tác động trực tiếp lên đối tượng và không đo được.",
                "Figure 101.3 · Typical closed-loop system. The output is fed back to the summing "
                "junction; the external torque T<sub>ext</sub> acts directly on the plant and cannot "
                "be measured.",
                "Sơ đồ khối vòng kín với bốn khối và đường phản hồi từ đầu ra về bộ cộng",
                "Closed-loop block diagram: four blocks with a feedback path to the summing junction")


# ---------------------------------------------------------------- 101.4
def fig_101_4():
    o = [_defs()]
    yc, bh = 88, 54
    by = yc - bh / 2.0
    o.append(_lbl(14, yc + 4, "Tham chiếu", "t"))
    o.append(_arr(80, yc, 92, yc))
    o.append(_sum(106, yc, minus=True))
    o.append(_arr(118, yc, 148, yc))
    o.append(_block(148, by, 100, bh, [("Controller", False)]))
    o.append(_subs(198, yc + 15, [("G", False), ("c", True)], "middle"))
    o.append(_arr(248, yc, 258, yc))
    o.append(_lbl(250, yc - 14, "Y", "tb"))
    o.append(_sum(272, yc))
    o.append(_arr(284, yc, 316, yc))
    o.append(_lbl(294, yc - 14, "X", "tb"))
    o.append(_block(316, by, 94, bh, [("Amp", False)]))
    o.append(_subs(363, yc + 15, [("K", False), ("AMP", True)], "middle"))
    o.append(_arr(410, yc, 456, yc))
    o.append(_block(456, by, 94, bh, [("System", False)]))
    o.append(_subs(503, yc + 15, [("G", False), ("m", True)], "middle"))
    o.append(_arr(550, yc, 648, yc))
    o.append(_out(588, yc, "Đầu ra"))
    o.append(_arr(272, 18, 272, yc - 14))
    o.append(_lbl(280, 32, "z", "tb"))
    o.append(_arr(503, 20, 503, by - 2))
    o.append(_subs(511, 32, [("T", False), ("ext", True)]))
    o.append(_line(612, yc, 612, 154))
    o.append(_line(612, 154, 106, 154))
    o.append(_arr(106, 154, 106, yc + 13))
    return _fig(svg(660, 186, "".join(o),
                    "Sơ đồ khối có thêm bộ cộng giữa bộ điều khiển và bộ khuếch đại, với tín hiệu kích thích z"),
                "Hình 101.4 · Bộ cộng đặt thêm vào hệ. Ưu điểm là nó có thể chèn ở bất kỳ điểm nào "
                "thuận tiện cho việc đo, không còn bị giới hạn ở ngõ vào hay ngõ ra nguyên thuỷ của hệ.",
                "Figure 101.4 · The summing junction placed in the system. Its advantage is that it can "
                "be inserted at any point convenient for measurement — it is no longer limited to the "
                "unaugmented inputs or outputs of the system.",
                "Sơ đồ khối có bộ cộng thứ hai, tín hiệu z đi vào từ trên, nhãn Y và X hai bên",
                "Block diagram with a second summing junction fed by z, labelled Y and X")


# ---------------------------------------------------------------- 101.5
def fig_101_5():
    o = [_defs()]
    yc, bh = 124, 52
    by = yc - bh / 2.0
    o.append(_rect(118, 78, 172, 96, 1.2, "5 4"))
    o.append(_lbl(204, 190, "Microprocessor", "ts", "middle"))
    o.append(_lbl(8, yc + 4, "Tham chiếu", "t"))
    o.append(_arr(74, yc, 86, yc))
    o.append(_sum(99, yc, minus=True))
    o.append(_arr(111, yc, 133, yc))
    o.append(_block(133, by, 78, bh, [("Controller", False)]))
    o.append(_subs(172, yc + 15, [("G", False), ("c", True)], "middle"))
    o.append(_arr(211, yc, 241, yc))
    o.append(_lbl(218, yc - 14, "Y", "tb"))
    o.append(_sum(253, yc))
    o.append(_arr(265, yc, 296, yc))
    o.append(_lbl(272, yc - 14, "X", "tb"))
    o.append(_block(296, by, 60, bh, []))
    o.append(_subs(326, yc + 4, [("S", False), ("H", True)], "middle"))
    o.append(_arr(356, yc, 396, yc))
    o.append(_block(396, by, 78, bh, [("Amp", False)]))
    o.append(_subs(435, yc + 15, [("K", False), ("AMP", True)], "middle"))
    o.append(_arr(474, yc, 512, yc))
    o.append(_block(512, by, 90, bh, [("System", False)]))
    o.append(_subs(557, yc + 15, [("G", False), ("m", True)], "middle"))
    o.append(_arr(602, yc, 686, yc))
    o.append(_out(632, yc, "Đầu ra"))
    # Zm -> A_f -> the internal summing junction
    o.append(_subs(210, 18, [("Z", False), ("m", True)], "middle"))
    o.append(_arr(210, 24, 210, 34))
    o.append(_block(178, 34, 64, 30, []))
    o.append(_subs(210, 54, [("A", False), ("f", True)], "middle"))
    o.append(_arr(210, 64, 210, yc - 14))
    # P_f tapping the output line, up to X_e
    o.append(_line(450, yc, 450, 66))
    o.append(_block(418, 34, 64, 30, []))
    o.append(_subs(450, 54, [("P", False), ("f", True)], "middle"))
    o.append(_arr(450, 34, 450, 16))
    o.append(_subs(458, 20, [("X", False), ("e", True)]))
    # external torque
    o.append(_arr(566, 42, 566, by - 2))
    o.append(_subs(574, 54, [("T", False), ("ext", True)]))
    # feedback
    o.append(_line(656, yc, 656, 202))
    o.append(_line(656, 202, 99, 202))
    o.append(_arr(99, 202, 99, yc + 13))
    return _fig(svg(700, 216, "".join(o),
                    "Sơ đồ khối hệ điều khiển bằng vi xử lý, có khối chuyển đổi A f và bộ lọc P f"),
                "Hình 101.5 · Hệ điều khiển bằng vi xử lý. Bộ cộng được thực hiện ngay bên trong vi xử "
                "lý bằng một lệnh cộng; A<sub>f</sub> đại diện cho quá trình chuyển đổi tương tự – số "
                "và P<sub>f</sub> cho bộ lọc thông thấp ở ngõ ra.",
                "Figure 101.5 · A microprocessor-controlled system. The summing junction is implemented "
                "inside the microprocessor by an add instruction; A<sub>f</sub> represents the "
                "analog-to-digital conversion and P<sub>f</sub> the low-pass filter on the output.",
                "Sơ đồ khối vi xử lý với khối A f trên đường Z m, khối P f lấy tín hiệu X e và đường phản hồi",
                "Microprocessor block diagram with A f on Z m, P f tapping X e, and a feedback path")


FIGS = [fig_101_1, fig_101_2, fig_101_3, fig_101_4, fig_101_5]


def fig(n):
    return FIGS[n - 1]()
