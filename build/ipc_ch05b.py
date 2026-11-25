# -*- coding: utf-8 -*-
"""Chapter 5, section 5.2 "Signal Conditioning" (EN/VI bilingual).

Source: Prasad, Jayaswal and Priye, *Instrumentation and Process Control*
(I.K. International, 2019), PDF pp. 244-251, printed pp. 232-239, decoded
text lines 9259-9562.  Covers 5.2.1 Power Pack Unit and 5.2.2 Amplifier
Unit (rectifier/filter/regulator, inverter, adder, subtractor, integrator,
differentiator, instrumentation amplifier) with Figures 5.3-5.12.

The printed formulas are unnumbered and badly scrambled in the text layer;
each one below was transcribed from the page renders (p247-p251).  The
`ipcfig5_a` / `ipcfig5_b` suppliers are authored in parallel with this prose
module.  When they are not yet importable, simple but genuine vector redraws
of the printed diagrams are installed as non-overwriting fallbacks; as soon
as the real suppliers register `fig_f03` .. `fig_f12`, those callables win.
"""

import ipcfig5 as F
from ipc_ch05_lib import H, P, L, E, FIG, TBL, NOTE, REFS


# ----------------------------------------------------------------- figures
def _t(x, y, s, size=7.5, anchor="middle", color="#1f3a5f"):
    return ('<text x="%s" y="%s" text-anchor="%s" font-size="%s" '
            'fill="%s">%s</text>' % (x, y, anchor, size, color, s))


def _r(x, y, w, h, fill="#eef3fb"):
    return ('<rect x="%d" y="%d" width="%d" height="%d" fill="%s" '
            'stroke="#1f3a5f" stroke-width="1.1"/>' % (x, y, w, h, fill))


_MID = "ipc5b"


def _defs():
    return ('<defs><marker id="%s" viewBox="0 0 8 8" refX="7" refY="4" '
            'markerWidth="6" markerHeight="6" orient="auto">'
            '<path d="M0 0 L8 4 L0 8 z" fill="#1f3a5f"/></marker></defs>'
            % _MID)


def _w(pts, arrow=False):
    d = "M" + " L".join("%g %g" % p for p in pts)
    m = ' marker-end="url(#%s)"' % _MID if arrow else ""
    return ('<path d="%s" fill="none" stroke="#1f3a5f" '
            'stroke-width="1.1"%s/>' % (d, m))


def _res(x1, x2, y):
    seg = (x2 - x1) / 8.0
    pts = [(x1, y)]
    for k in range(1, 7):
        pts.append((x1 + k * seg, y + (-6 if k % 2 else 6)))
    pts.append((x2, y))
    return _w(pts)


def _cap(x, y1, y2):
    m = (y1 + y2) / 2.0
    return (_w([(x, y1), (x, m - 5)]) +
            _w([(x - 9, m - 5), (x + 9, m - 5)]) +
            _w([(x - 9, m + 5), (x + 9, m + 5)]) +
            _w([(x, m + 5), (x, y2)]))


def _gnd(x, y):
    return (_w([(x, y), (x, y + 8)]) +
            '<path d="M%d %d L%d %d M%d %d L%d %d M%d %d L%d %d" '
            'fill="none" stroke="#1f3a5f" stroke-width="1"/>'
            % (x - 8, y + 8, x + 8, y + 8, x - 5, y + 12, x + 5, y + 12,
               x - 2, y + 16, x + 2, y + 16))


def _node(x, y):
    return '<circle cx="%d" cy="%d" r="2.2" fill="#1f3a5f"/>' % (x, y)


def _oa(cx, cy, label="OA"):
    o = ['<polygon points="%d,%d %d,%d %d,%d" fill="#ffffff" '
         'stroke="#1f3a5f" stroke-width="1.2"/>'
         % (cx - 42, cy - 32, cx - 42, cy + 32, cx + 48, cy)]
    o.append(_t(cx + 6, cy + 4, label, 7.5))
    o.append(_t(cx - 26, cy - 16, "−", 10))
    o.append(_t(cx - 26, cy + 22, "+", 10))
    return o, (cx - 42, cy - 16), (cx - 42, cy + 16), (cx + 48, cy)


_FIG_TEXT = {
    3: ("Sơ đồ khối bộ nguồn", "Power pack unit block diagram",
        "Sơ đồ khối ứng dụng của bộ nguồn trong mạch đo và bộ khuếch đại",
        "Block diagram of the power pack unit feeding a measurement circuit "
        "and an instrumentation amplifier"),
    4: ("Mạch nguồn chỉnh lưu cầu", "Transformer, bridge rectifier and filter",
        "Mạch nguồn dùng máy biến áp, cầu diode, tụ lọc và transistor cho "
        "điện áp từ +Vx đến −Vx",
        "Power supply with transformer, diode bridge, filter capacitor and "
        "transistors giving a voltage from +Vx to −Vx"),
    5: ("Bộ khuếch đại điều chế chopper", "Chopper-modulated instrument amplifier",
        "Tín hiệu một chiều được chopper biến thành xoay chiều, khuếch đại "
        "rồi chỉnh lưu trở lại thành một chiều",
        "A D.C. signal is chopped to A.C., amplified and then rectified back "
        "to D.C."),
    6: ("Dạng cơ bản của bộ khuếch đại thuật toán", "Basic operational amplifier",
        "Bộ khuếch đại thuật toán với điện trở đầu vào Ri và điện trở "
        "phản hồi R0",
        "Operational amplifier with input resistor Ri and feedback resistor R0"),
    7: ("Bộ đảo dùng bộ khuếch đại thuật toán", "Inverting amplifier",
        "Mạch đảo pha với điện trở đầu vào và điện trở phản hồi đều bằng R",
        "Phase-inverting circuit with equal input and feedback resistors R"),
    8: ("Bộ cộng dùng bộ khuếch đại thuật toán", "Summing amplifier (adder)",
        "Hai tín hiệu e_1 và e_2 được cộng tại đầu vào đảo",
        "Two signals e_1 and e_2 are summed at the inverting input"),
    9: ("Bộ trừ dùng bộ khuếch đại thuật toán", "Subtracting amplifier (subtractor)",
        "Hai bộ khuếch đại thuật toán thực hiện phép trừ e_2 − e_1",
        "Two operational amplifiers perform the subtraction e_2 − e_1"),
    10: ("Bộ tích phân dùng bộ khuếch đại thuật toán", "Operational integrator",
         "Điện trở đầu vào R và tụ phản hồi C tạo thành phép tích phân",
         "Input resistor R and feedback capacitor C form the integrator"),
    11: ("Bộ vi phân dùng bộ khuếch đại thuật toán", "Operational differentiator",
         "Tụ đầu vào C và điện trở phản hồi R tạo thành phép vi phân",
         "Input capacitor C and feedback resistor R form the differentiator"),
    12: ("Bộ khuếch đại đo lường", "Instrumentation amplifier",
         "Ba bộ khuếch đại thuật toán với R_1, R_2 và điện trở biến đổi R_x",
         "Three operational amplifiers with R_1, R_2 and the variable "
         "resistor R_x"),
}


def _standalone_fig(n):
    o = [_defs()]
    if n == 3:
        o += [_r(20, 92, 100, 40), _t(70, 116, "Sensor signal", 7.2),
              _w([(120, 112), (160, 112)], True),
              _r(160, 88, 116, 48), _t(218, 106, "Power pack", 7.5),
              _t(218, 119, "unit", 7.5),
              _w([(276, 100), (320, 70)], True),
              _r(320, 46, 150, 38), _t(395, 69, "Measurement circuit", 7.2),
              _w([(276, 124), (320, 139)], True),
              _r(320, 120, 150, 38),
              _t(395, 143, "Instrumentation amplifier", 7.0),
              _w([(470, 139), (510, 139)], True),
              _r(510, 120, 70, 38), _t(545, 143, "Filter", 7.5),
              _w([(580, 139), (612, 139)], True),
              _t(616, 143, "Output", 7.5, anchor="start"),
              _r(160, 170, 150, 34),
              _t(235, 191, "Calibration adjustment", 7.0),
              _w([(218, 136), (218, 170)], True),
              _w([(310, 187), (320, 158)], True)]
    elif n == 4:
        o += [_t(40, 70, "A.C. supply", 7.5),
              _w([(40, 80), (80, 80)], True),
              _r(80, 60, 90, 40), _t(125, 84, "Transformer", 7.2),
              _w([(170, 80), (210, 80)], True)]
        for x, y, lab in ((245, 55, "D1"), (315, 55, "D2"),
                          (245, 125, "D3"), (315, 125, "D4")):
            o += [_r(x - 18, y - 11, 36, 22, "#ffffff"), _t(x, y + 3, lab, 7.0)]
        o += [_w([(210, 80), (227, 80), (227, 55), (227, 55)]),
              _w([(227, 55), (245, 55)]),
              _w([(210, 90), (227, 90), (227, 125), (245, 125)]),
              _w([(281, 55), (315, 55)]), _w([(281, 125), (315, 125)]),
              _w([(333, 55), (360, 55), (360, 80)]),
              _w([(333, 125), (360, 125), (360, 80)]),
              _w([(360, 80), (380, 80), (380, 50), (400, 50)]),
              _w([(380, 80), (380, 130), (400, 130)]),
              _w([(400, 50), (560, 50)]), _w([(400, 130), (560, 130)]),
              _cap(420, 50, 130), _t(440, 94, "C", 7.0, anchor="start"),
              _r(455, 36, 44, 26, "#ffffff"), _t(477, 53, "Q1", 7.0),
              _r(455, 118, 44, 26, "#ffffff"), _t(477, 135, "Q2", 7.0),
              _res(510, 552, 50), _res(510, 552, 130),
              _t(566, 54, "+Vx", 7.5, anchor="start"),
              _t(566, 134, "−Vx", 7.5, anchor="start")]
    elif n == 5:
        o += [_r(20, 50, 120, 36), _t(80, 72, "Input signal", 7.2),
              _t(80, 82, "in D.C.", 7.2),
              _w([(140, 68), (180, 68)], True),
              _r(180, 50, 80, 36), _t(220, 72, "Chopper", 7.2),
              _w([(260, 68), (300, 68)], True),
              _r(300, 50, 140, 36),
              _t(370, 65, "Low power", 7.0), _t(370, 78, "transformer", 7.0),
              _w([(440, 68), (560, 68), (560, 130)], True),
              _r(520, 130, 80, 36), _t(560, 152, "A.C. output", 7.2),
              _w([(520, 148), (500, 148)], True),
              _r(370, 130, 130, 36), _t(435, 145, "Rectifier", 7.2),
              _t(435, 157, "and filter", 7.2),
              _w([(370, 148), (320, 148)], True),
              _r(220, 130, 100, 36), _t(270, 152, "D.C. output", 7.2),
              _w([(220, 148), (196, 148)], True),
              _t(190, 152, "A.C. input", 7.0, anchor="end")]
    elif n in (6, 7, 8, 10, 11):
        parts, inv, ig, out = _oa(400, 110, "OA" if n == 6 else "")
        o += parts
        o += [_w([(out[0], out[1]), (510, 110)]),
              _t(518, 114, "e_o", 7.5, anchor="start"),
              _node(out[0] - 1, 110),
              _w([(ig[0], ig[1]), (ig[0], 168)]), _gnd(ig[0], 168),
              _node(inv[0], inv[1])]
        if n == 10:
            o += [_w([(190, 94), (inv[0], 94)]),
                  _res(230, 320, 94), _t(210, 88, "e_i", 7.5, anchor="end"),
                  _t(275, 88, "R", 7.0),
                  _w([(inv[0], inv[1]), (inv[0], 58)]),
                  _cap(inv[0] + 56, 58, 110),
                  _w([(inv[0] + 56, 58), (inv[0], 58)]),
                  _w([(inv[0] + 56, 110), (out[0] - 1, 110)]),
                  _t(inv[0] + 74, 88, "C", 7.0, anchor="start")]
        elif n == 11:
            o += [_w([(190, 94), (inv[0], 94)]),
                  _cap(240, 94, 148),
                  _w([(190, 94), (190, 94 + 54), (240, 148)]),
                  _t(170, 88, "e_i", 7.5, anchor="end"),
                  _t(258, 88, "C", 7.0, anchor="start"),
                  _w([(inv[0], inv[1]), (inv[0], 58)]),
                  _res(inv[0], 470, 58),
                  _w([(470, 58), (470, 110), (out[0] - 1, 110)]),
                  _t(430, 52, "R", 7.0)]
        else:
            o += [_w([(190, 94), (inv[0], 94)]),
                  _res(230, 320, 94), _t(210, 88, "e_i", 7.5, anchor="end"),
                  _w([(inv[0], inv[1]), (inv[0], 58)]),
                  _res(inv[0], 470, 58),
                  _w([(470, 58), (470, 110), (out[0] - 1, 110)]),
                  _t(430, 52, "R0" if n == 6 else "R", 7.0)]
            if n == 6:
                o += [_t(275, 88, "Ri", 7.0),
                      _w([(200, 94), (232, 94)], True),
                      _t(200, 114, "I", 7.5)]
            if n == 8:
                o += [_w([(190, 136), (inv[0], 136), (inv[0], 94)]),
                      _res(230, 320, 136),
                      _t(210, 130, "e_1", 7.5, anchor="end"),
                      _t(210, 158, "e_2", 7.5, anchor="end"),
                      _w([(190, 136), (190, 148), (190, 148)])]
            if n == 7:
                o += [_t(275, 88, "R", 7.0)]
    elif n == 9:
        pa, ia, ga, oa1 = _oa(220, 90, "OA1")
        pb, ib, gb, oa2 = _oa(470, 110, "OA2")
        o += pa + pb
        o += [_w([(40, 74), (ia[0], 74)]), _res(80, 170, 74),
              _t(60, 68, "e_2", 7.5, anchor="end"),
              _w([(ia[0], ia[1]), (ia[0], 50)]),
              _res(ia[0], oa1[0], 50),
              _w([(oa1[0], 50), (oa1[0], oa1[1])]),
              _node(ia[0], ia[1]),
              _w([(ga[0], ga[1]), (ga[0], 140)]), _gnd(ga[0], 140),
              _w([(oa1[0], oa1[1]), (340, 90), (340, 94)]),
              _res(340, ib[0], 94), _t(365, 88, "R", 7.0),
              _w([(40, 158), (ib[0], 158), (ib[0], ib[1])]),
              _res(80, 170, 158),
              _t(60, 152, "e_1", 7.5, anchor="end"),
              _node(ib[0], ib[1]), _t(360, 152, "−e_2", 7.0),
              _w([(gb[0], gb[1]), (gb[0], 190)]), _gnd(gb[0], 190),
              _w([(ib[0], ib[1]), (ib[0], 56)]),
              _res(ib[0], 550, 56),
              _w([(550, 56), (550, 110), (oa2[0], 110)]),
              _w([(oa2[0], oa2[1]), (590, 110)]),
              _t(598, 114, "e_o", 7.5, anchor="start")]
    else:  # n == 12
        pa, ia, ga, oa1 = _oa(190, 78, "OA1")
        pb, ib, gb, oa2 = _oa(190, 168, "OA2")
        pc, ic, gc, oa3 = _oa(480, 123, "OA3")
        o += pa + pb + pc
        o += [_w([(40, 62), (ia[0], 62)]),
              _t(34, 66, "(e_n + e_1)", 7.0, anchor="end"),
              _w([(40, 152), (ib[0], 152)]),
              _t(34, 156, "(e_n + e_2)", 7.0, anchor="end"),
              _w([(oa1[0], oa1[1]), (270, 78), (270, 62)]),
              _r(262, 62, 16, 32, "#ffffff"),
              _t(270, 83, "R_1", 6.8),
              _w([(oa2[0], oa2[1]), (270, 168), (270, 94)]),
              _r(262, 94, 16, 32, "#ffffff"),
              _t(270, 115, "R_2", 6.8),
              _r(266, 66, 8, 24, "#ffffff"),
              _w([(260, 92), (280, 66)], True),
              _t(288, 84, "R_x", 7.0, anchor="start"),
              _w([(270, 78), (ic[0], 107)]),
              _res(310, 400, 107), _t(355, 101, "R", 7.0),
              _w([(270, 168), (ic[0], 139)]),
              _res(310, 400, 139), _t(355, 133, "R", 7.0),
              _w([(ic[0], ic[1]), (ic[0], 72)]),
              _res(ic[0], 560, 72),
              _w([(560, 72), (560, 123), (oa3[0], 123)]),
              _t(520, 66, "R", 7.0),
              _w([(oa3[0], oa3[1]), (600, 123)]),
              _t(608, 127, "e_o", 7.5, anchor="start")]
    cvi, cen, avi, aen = _FIG_TEXT[n]
    o.append(_t(340, 242, "Hình 5.%d   ·   Figure 5.%d" % (n, n),
                6.4, color="#888888"))
    svg = ('<svg xmlns="http://www.w3.org/2000/svg" width="680" height="250" '
           'viewBox="0 0 680 250"><rect width="680" height="250" '
           'fill="#ffffff"/>%s</svg>' % "".join(o))
    return (svg, "Hình 5.%d · %s" % (n, cvi),
            "Figure 5.%d · %s" % (n, cen), avi, aen)


for _n in range(3, 13):
    if not hasattr(F, "fig_f%02d" % _n):
        setattr(F, "fig_f%02d" % _n, (lambda _n=_n: _standalone_fig(_n)))


# ------------------------------------------------------------------- prose
def section(lang):
    b = []

    # ---------------------------------------------------------------- 5.2
    H(b, lang, "5.2 Điều hòa tín hiệu", "5.2 Signal Conditioning")

    P(b, lang,
      "Như đã thảo luận ở phần trước, tín hiệu đầu vào đầy đủ của một phép đo "
      "nói chung đi qua hai giai đoạn: bộ chuyển đổi sơ cấp và bộ chuyển đổi "
      "thứ cấp. Bộ chuyển đổi sơ cấp về cơ bản gồm các phần tử sơ cấp tiếp "
      "xúc trực tiếp với quá trình; ta cũng có thể gọi các phần tử này là "
      "cảm biến. Thường thì tín hiệu cảm biến không ở dạng chuẩn (dạng tín "
      "hiệu điện chuẩn của chúng ta là 4 đến 20 mA một chiều). Các cảm biến "
      "hay phần tử sơ cấp có thể cho kết quả đo dưới dạng các phần tử mạch, "
      "tức là sự thay đổi của điện trở, độ tự cảm hay điện dung, hoặc dưới "
      "dạng điện áp rất thấp, tức là milivôn hay microvôn. Những tín hiệu "
      "này không thể dùng cho các công việc tiếp theo, tức là để chỉ thị, "
      "ghi chép hoặc điều khiển. Chính phần thứ cấp của bộ chuyển đổi có "
      "nhiệm vụ điều hòa các tín hiệu này, giữ nguyên dạng ban đầu, để biến "
      "chúng về dạng chuẩn, tức là dạng 4 đến 20 mA một chiều hoặc 0,25 đến "
      "1,25 vôn.",
      "As we have discussed earlier, the complete measurement input signal "
      "comes out of two stages in general: the primary transducer and the "
      "secondary transducer. The primary transducer essentially consists of "
      "primary elements that are in physical contact with the process; "
      "these elements may also be called sensors. Usually the sensor signals "
      "are not available in standard form (our standard form of electrical "
      "signal is 4 to 20 mA D.C.). Sensors or primary elements may give the "
      "result of measurement in the form of circuit elements, that is, a "
      "change in resistance, inductance or capacitance, or in the form of "
      "extremely low voltages, that is, millivolts or microvolts. Such "
      "signals cannot be used for further work, namely for indicating, "
      "recording or controlling. It is the job of the secondary part of the "
      "transducer to condition these signals, in their original form, and "
      "convert them into standard form, that is, into 4 to 20 mA D.C. or "
      "0.25 to 1.25 V.")

    P(b, lang,
      "Đôi khi điều hòa còn có nghĩa là nhiều hơn thế. Ví dụ, ở các máy phân "
      "tích, mẫu được lấy từ quá trình ở dạng thô để phân tích các thành "
      "phần khác nhau trong đó. Mẫu thô này có thể được làm nguội (nếu nó ở "
      "dạng nóng), lọc, làm sạch và các công đoạn khác. Mẫu phải đi qua một "
      "buồng kín để tiến hành làm nguội, lọc, làm sạch, v.v. Đối với máy phân "
      "tích, các thao tác này cũng thuộc phạm vi điều hòa. Máy phân tích NOx "
      "và SOx có các bộ điều hòa tín hiệu dạng này.",
      "Sometimes conditioning means more than this. For instance, in "
      "analysis instruments the sample is drawn from the process in raw "
      "form for the analysis of its different contents. This raw sample may "
      "be cooled (if it is in heated form), filtered, cleaned and so on. It "
      "has to pass through a closed chamber for carrying out cooling, "
      "filtering, cleaning, etc. In the case of analysis instruments these "
      "operations also come under conditioning. NOx and SOx analyzers have "
      "such signal conditioner units.")

    P(b, lang,
      "Tiếp theo, hệ thống nguồn nuôi — tức là nguồn kích thích trong trường "
      "hợp bộ chuyển đổi thụ động — và sau đó là sự khuếch đại tín hiệu mức "
      "thấp cũng được xét trong bộ điều hòa tín hiệu. Đôi khi một vài thành "
      "phần chính của hệ thống thu thập dữ liệu, ví dụ mạch lấy mẫu-giữ mẫu, "
      "bộ ghép kênh, bộ chuyển đổi, v.v., cũng được nghiên cứu trong bộ điều "
      "hòa tín hiệu. Vì vậy, phạm vi nghiên cứu của bộ điều hòa tín hiệu rộng "
      "hơn nhiều.",
      "Next, the power supply system, that is, excitation in the case of a "
      "passive transducer system, and then the amplification of the "
      "low-level signal are also considered part of the signal conditioning "
      "unit. Sometimes a few main components of the data acquisition system, "
      "for example the sample-and-hold circuit, multiplexer, converter, etc., "
      "are also studied under the signal conditioning unit. We therefore "
      "observe that the scope of study of the signal conditioner is much "
      "larger.")

    P(b, lang,
      "Về bộ điều hòa ở dạng bộ chuyển đổi thứ cấp, chúng ta đã thảo luận rất "
      "kỹ ở chương trước, vì thế không cần bàn thêm ở đây. Tương tự, chúng "
      "ta sẽ không đi vào chi tiết bộ điều hòa tín hiệu dùng cho máy phân "
      "tích, vì điều này vượt quá phạm vi thảo luận hiện tại. Do đó, chúng "
      "ta sẽ bắt đầu đề tài này từ nguồn kích thích hay bộ nguồn.",
      "As far as the conditioning unit in the form of a secondary transducer "
      "is concerned, we have already discussed it at great length in the "
      "previous chapter, so no further discussion is needed here. Similarly, "
      "we shall not discuss the details of the signal conditioning unit "
      "applicable to analysis instruments, because this is beyond the scope "
      "of the present discussion. We shall therefore start our discussion "
      "of the topic with the excitation unit, or power pack unit.")

    # ------------------------------------------------------------- 5.2.1
    H(b, lang, "5.2.1 Bộ nguồn", "5.2.1 Power Pack Unit", level=3)

    P(b, lang,
      "Bộ nguồn hay nguồn kích thích về cơ bản là một hệ thống cấp điện "
      "được thiết kế để cung cấp một mức điện áp cụ thể hoặc sự kết hợp của "
      "nhiều mức điện áp khác nhau theo yêu cầu của mạch đo cũng như của bộ "
      "khuếch đại. Vì sự kết hợp giữa hệ thống đo và hệ thống khuếch đại có "
      "thể thuộc loại xoay chiều hoặc một chiều, bộ nguồn cũng có thể được "
      "thiết kế để cấp điện xoay chiều hoặc một chiều. Cả hai loại nguồn đều "
      "nhất thiết có chung một máy biến áp. Sơ đồ khối chung thể hiện ứng "
      "dụng của bộ nguồn được cho trong Hình 5.3.",
      "A power pack unit or excitation unit is essentially a power supply "
      "system designed to supply a particular level of voltage or a "
      "combination of more than one voltage level, as required by the "
      "measurement circuit as well as by the amplifier unit. Since the "
      "combination of the measurement and amplification systems may be of "
      "A.C. type or D.C. type, the power pack unit can also be designed to "
      "supply A.C. or D.C. Both types of supply unit essentially have a "
      "transformer in common. A general block diagram showing the "
      "application of the power pack unit is given in Figure 5.3.")

    FIG(b, 3, F.fig_f03(), lang)

    P(b, lang,
      "Hình 5.4 cho thấy sơ đồ mạch điển hình nhưng thực tế của một bộ nguồn "
      "dùng để cấp điện áp từ +Vx đến −Vx cho bộ khuếch đại cần loại nguồn "
      "đó. Trong mạch này đã dùng ba loại diode, một loại tụ điện, một loại "
      "điện trở và một loại transistor. Sự giống nhau về ký hiệu giữa các "
      "phần tử mạch cho thấy sự tương đồng về đặc tính. Mạch nguyên bản "
      "hoặc phiên bản cải tiến của nó được dùng trong nhiều ứng dụng liên "
      "quan đến thiết bị đo.",
      "Figure 5.4 shows a typical but practical circuit diagram of a power "
      "pack unit supplying a voltage from +Vx to −Vx for the amplifier unit "
      "that needs such a supply. In this circuit three types of diode, one "
      "type of capacitor, one type of resistor and one type of transistor "
      "have been used. Similarity of nomenclature for a circuit element "
      "indicates similarity of characteristic. The circuit, in its original "
      "or an improved version, is used in many instrumentation applications.")

    FIG(b, 4, F.fig_f04(), lang)

    # ------------------------------------------------------------- 5.2.2
    H(b, lang, "5.2.2 Bộ khuếch đại", "5.2.2 Amplifier Unit", level=3)

    P(b, lang,
      "Tín hiệu đầu vào mức thấp nhận được từ cảm biến cần được khuếch đại, "
      "tức là nâng mức của nó lên, để có thể xử lý tiếp nhằm thu được tín "
      "hiệu điều khiển các thiết bị chỉ thị, máy ghi hoặc bộ điều khiển. Bộ "
      "khuếch đại đo lường gần như luôn được dùng để thực hiện việc khuếch "
      "đại này. Trong các hệ thống đo lường trước đây, khi khuếch đại xoay "
      "chiều còn phổ biến, bộ khuếch đại đo lường được gọi là bộ khuếch đại "
      "đo lường điều chế chopper. Tín hiệu đầu vào nhận ở dạng một chiều "
      "trước hết được biến đổi sang xoay chiều nhờ một chopper cơ khí kết "
      "hợp với máy biến áp công suất thấp, như Hình 5.5. Đầu ra của chopper "
      "ở dạng xoay chiều được khuếch đại rồi chỉnh lưu để thu lại tín hiệu "
      "đầu vào ban đầu ở dạng một chiều. Có những thao tác đo lường không "
      "cần tín hiệu ở dạng một chiều, do đó đầu ra của bộ khuếch đại có thể "
      "được giữ nguyên. Ví dụ, trong các ứng dụng máy ghi nhiệt độ dùng "
      "động cơ servo xoay chiều để thực hiện các thao tác ghi và in.",
      "The low-level input signal obtained from the sensor has to be "
      "amplified, that is, its level has to be enhanced, so that further "
      "processing becomes possible for obtaining signals to drive "
      "indicators, recorders or controllers. Instrumentation amplifiers are "
      "almost invariably used to carry out the amplification. In earlier "
      "instrumentation systems, when A.C. amplification was popular, the "
      "instrumentation amplifier was called a chopper-modulated instrument "
      "amplifier. The input signal received in D.C. form was first converted "
      "into A.C. by means of a mechanically operated chopper in combination "
      "with low-power transformers, as shown in Figure 5.5. The output of "
      "the chopper in A.C. form is amplified and then rectified to recover "
      "the original input signal in D.C. form. There are instrumentation "
      "operations where a signal in D.C. form may not be required, so the "
      "amplifier output may be allowed to remain as it is. For example, in "
      "temperature recorder applications an A.C. servomotor is employed to "
      "operate the recording-cum-printing operations.")

    FIG(b, 5, F.fig_f05(), lang)

    P(b, lang,
      "Trong những trường hợp thiết kế bộ khuếch đại xoay chiều thuộc dạng "
      "phổ biến (đa số trường hợp đều như vậy), chopper có thể được thiết "
      "kế theo nhiều kiểu. Một số kiểu là chopper cơ điện do dao động điều "
      "khiển (kiểu thiết kế phổ biến trong các máy ghi nhiệt độ ngày "
      "trước), chopper dùng transistor, chopper quang điện, v.v.",
      "In situations where the design of the A.C. amplifier is of the common "
      "type (as is the case in most instances), the chopper can be of many "
      "designs. Some of these are the oscillator-driven electromechanical "
      "type (a popular design in earlier temperature recorders), the "
      "transistor-operated chopper, the photo-optical chopper, and so on.")

    P(b, lang,
      "Tuy nhiên, trong thiết kế hiện đại của bộ khuếch đại đo lường, sự "
      "xuất hiện của bộ khuếch đại thuật toán và khả năng ứng dụng của nó đã "
      "thay đổi hoàn toàn khái niệm thiết kế cơ bản, nhờ đó cải thiện hiệu "
      "năng của bộ khuếch đại đo lường. Dạng cơ bản của bộ khuếch đại thuật "
      "toán được trình bày trong Hình 5.6.",
      "In the modern design of the instrumentation amplifier, however, the "
      "advent of the operational amplifier and its possible applications "
      "has changed the complete basic design concept and has thus improved "
      "the performance of the instrumentation amplifier. The operational "
      "amplifier in its basic form is shown in Figure 5.6.")

    FIG(b, 6, F.fig_f06(), lang)

    P(b, lang,
      "Mạch khuếch đại thuật toán có thể được xem như hai bộ khuếch đại "
      "khác nhau ghép tầng với nhau như một nguồn dòng không đổi. Hệ số "
      "khuếch đại điện áp hở vòng của loại bộ khuếch đại này lớn hơn "
      "100.000. Khi được nối như một bộ đảo, đầu vào không đảo, tức là đầu "
      "vào dương, được nối đất. Tín hiệu đầu vào được đưa vào đầu vào đảo, "
      "ký hiệu âm. Vì hệ số khuếch đại rất cao, một tín hiệu điện áp tương "
      "tự đầu vào (e_i) cỡ microvôn cũng có thể tạo ra đáng kể điện áp đầu "
      "ra (e_o) để điều khiển các thiết bị hiển thị. Bằng cách này, điện áp "
      "đầu vào bằng không cùng với điện trở đầu vào vô hạn làm cho đầu vào "
      "đảo trở thành điểm nối đất ảo (nối đất về điện áp, không phải về "
      "dòng điện). Dù có điện áp bằng không, điểm này không thể hút bất kỳ "
      "dòng điện nào. Đầu vào đảo của bộ khuếch đại thuật toán được nối đất "
      "ảo nghĩa là điện áp bằng không và dòng điện bằng không. Nhờ hệ số "
      "khuếch đại rất cao và điện trở đầu vào lớn, đầu vào đảo được nối đất "
      "ảo, vì thế toàn bộ điện áp đầu vào rơi trên điện trở đầu vào R_i. "
      "Vì không có dòng đầu vào nào chảy vào điểm nối đất ảo, dòng đó phải "
      "chảy qua điện trở đầu ra R_0, do đó dòng đầu ra bằng dòng đầu vào. "
      "Dấu trừ ở đầu ra biểu thị sự đảo pha. Điện trở đầu ra của bộ khuếch "
      "đại rất thấp và khả năng loại bỏ nhiễu chế độ chung cũng rất cao. Bộ "
      "khuếch đại thuật toán có thể thực hiện nhiều phép toán học và các "
      "phép toán khác một cách hiệu quả. Một số phép toán được trình bày ở "
      "đây ngắn gọn nhất có thể.",
      "The operational amplifier circuit can be viewed as two different "
      "amplifiers cascaded together as a constant current source. The "
      "open-loop voltage gain of such an amplifier is more than 100,000. "
      "When it is connected as an inverter, the non-inverting, that is, "
      "positive input is grounded. The input signal voltage is applied to "
      "the inverting input, marked negative. Since the gain is very high, "
      "an analogue input signal voltage (e_i) of the order of a microvolt "
      "can also deliver a considerable output voltage (e_o) to operate "
      "display instruments. In this way, zero input voltage together with "
      "infinite input resistance make the inverting input a virtual ground "
      "(ground for voltage, not for current). Though it has zero voltage, "
      "it cannot sink any current. The inverting input of an operational "
      "amplifier being virtually grounded means zero voltage and zero "
      "current. Because of the very high gain and high input resistance, "
      "the inverting input is virtually grounded, so all the input voltage "
      "appears across the input resistor R_i. Since no input current enters "
      "the virtual ground, it must pass through the output resistor R_0, "
      "and therefore the output current equals the input current. The "
      "minus sign at the output indicates phase inversion. The output "
      "resistance of the amplifier is very low and the common-mode noise "
      "rejection is also high. The operational amplifier can perform many "
      "mathematical and other operations efficiently. Some of these "
      "operations are presented here in the shortest possible way.")

    NOTE(b, lang,
      "Điểm nối đất ảo: điện áp bằng không và dòng điện cũng bằng không; "
      "toàn bộ điện áp đầu vào rơi trên R_i và dòng đầu ra bằng dòng đầu vào.",
      "Virtual ground: zero voltage and zero current; all the input voltage "
      "appears across R_i and the output current equals the input current.")

    # --------------------------------------------------------- Inverter
    H(b, lang, "Bộ đảo", "Inverter", level=3)
    P(b, lang, "Phương trình đầu vào/đầu ra là:",
      "The input/output equation is:")
    E(b, lang, "(e_i − e_g)/R = (e_g − e_o)/R",
      "(e_i − e_g)/R = (e_g − e_o)/R", num="")
    P(b, lang, "Vì −e_o/e_g = A (hệ số khuếch đại), nên e_g = −e_o/A.",
      "Since −e_o/e_g = A (gain), e_g = −e_o/A.")
    FIG(b, 7, F.fig_f07(), lang)
    P(b, lang, "Do đó:", "Hence,")
    E(b, lang, "e_i + e_o/A = −e_o/A − e_o",
      "e_i + e_o/A = −e_o/A − e_o", num="")
    P(b, lang, "hay e_i = −e_o (vì e_o/A không đáng kể).",
      "or e_i = −e_o (since e_o/A is negligible).")

    # ----------------------------------------------------------- Adder
    H(b, lang, "Bộ cộng", "Adder", level=3)
    FIG(b, 8, F.fig_f08(), lang)
    P(b, lang, "Phương trình đầu vào/đầu ra là:",
      "The input/output equation is:")
    E(b, lang, "(e_1 − e_g)/R + (e_2 − e_g)/R = (e_g − e_o)/R",
      "(e_1 − e_g)/R + (e_2 − e_g)/R = (e_g − e_o)/R", num="")
    E(b, lang, "e_1 + e_o/A + e_2 + e_o/A = −e_o/A − e_o",
      "e_1 + e_o/A + e_2 + e_o/A = −e_o/A − e_o", num="")
    P(b, lang, "hay e_1 + e_g = −e_o (vì e_o/A không đáng kể).",
      "or e_1 + e_g = −e_o (since e_o/A is negligible).")
    P(b, lang, "Do đó e_o = −(e_1 + e_2).", "Hence e_o = −(e_1 + e_2).")

    # ------------------------------------------------------- Subtractor
    H(b, lang, "Bộ trừ", "Subtractor", level=3)
    FIG(b, 9, F.fig_f09(), lang)
    P(b, lang, "Phương trình đầu vào/đầu ra là:",
      "The input/output equation is:")
    E(b, lang, "e_o = (e_2 − e_1)", "e_o = (e_2 − e_1)", num="")

    # ------------------------------------------------------- Integrator
    H(b, lang, "Bộ tích phân", "Integrator", level=3)
    FIG(b, 10, F.fig_f10(), lang)
    P(b, lang, "Phương trình đầu vào/đầu ra là:",
      "The input/output equation is:")
    E(b, lang, "(e_i − e_g)/R = C·d(e_g − e_o)/dt",
      "(e_i − e_g)/R = C·d(e_g − e_o)/dt", num="")
    E(b, lang, "(e_i + e_o/A)/R = C·d(e_o/A − e_o)/dt",
      "(e_i + e_o/A)/R = C·d(e_o/A − e_o)/dt", num="")
    E(b, lang, "e_i/R = −C·de_o/dt", "e_i/R = −C·de_o/dt", num="")
    E(b, lang, "de_o/dt = −e_i/(RC)", "de_o/dt = −e_i/(RC)", num="")
    E(b, lang, "e_o = −(1/RC)·∫₀ᵗ e_i·dt",
      "e_o = −(1/RC)·∫₀ᵗ e_i·dt", num="")
    P(b, lang,
      "Nếu trong một điều kiện cụ thể R = 1 MΩ và C = 1 μF, thì:",
      "If for a particular condition R = 1 MΩ and C = 1 μF, then:")
    E(b, lang, "e_o = −∫₀ᵗ e_i·dt", "e_o = −∫₀ᵗ e_i·dt", num="")

    # --------------------------------------------------- Differentiator
    H(b, lang, "Bộ vi phân", "Differentiator", level=3)
    FIG(b, 11, F.fig_f11(), lang)
    P(b, lang, "Phương trình đầu vào/đầu ra là:",
      "The input/output equation is:")
    E(b, lang, "C·d(e_i − e_o)/dt = (e_g − e_o)/R",
      "C·d(e_i − e_o)/dt = (e_g − e_o)/R", num="")
    E(b, lang, "C·d(e_i + e_o/A)/dt = (−e_o/A − e_o)/R",
      "C·d(e_i + e_o/A)/dt = (−e_o/A − e_o)/R", num="")
    E(b, lang, "C·de_i/dt = −e_o/R", "C·de_i/dt = −e_o/R", num="")
    E(b, lang, "e_o = −RC·de_i/dt", "e_o = −RC·de_i/dt", num="")
    P(b, lang,
      "Lại giả sử trong một điều kiện cụ thể R = 1 MΩ và C = 1 μF, thì:",
      "Again, if for a particular condition R = 1 MΩ and C = 1 μF, then:")
    E(b, lang, "e_o = −de_i/dt", "e_o = −de_i/dt", num="")
    P(b, lang,
      "Tương tự, có thể thiết kế các phép toán khác bằng cách dùng bộ "
      "khuếch đại thuật toán.",
      "Similarly, other operations can be designed by employing the "
      "operational amplifier.")

    # -------------------------------------- Instrumentation amplifier
    H(b, lang, "Bộ khuếch đại đo lường", "Instrumentation amplifier", level=3)
    P(b, lang,
      "Bộ khuếch đại đo lường được thiết kế với bộ phản hồi điện trở ổn "
      "định để đạt được hệ số khuếch đại mong muốn với độ chính xác cao "
      "nhất. Đặc tính loại bỏ chế độ chung cao của bộ khuếch đại thuật toán "
      "được khai thác trọn vẹn khi thiết kế bộ khuếch đại đo lường. Hình "
      "5.12 trình bày dạng cơ bản của bộ khuếch đại đo lường. Các nhà sản "
      "xuất thiết bị sửa đổi sơ đồ này đôi chút cho phù hợp với mạch đo cụ "
      "thể của mình và gắn nhãn thương hiệu (TM) riêng. Trong thiết kế này, "
      "các bộ khuếch đại thuật toán OA1 và OA2 có hệ số khuếch đại bằng 1 "
      "đối với tín hiệu nhiễu chế độ chung e_n. Phép tính hệ số khuếch đại "
      "cho tín hiệu vi sai e_1, e_2 được thực hiện theo các phương trình sau "
      "với tham chiếu đến sơ đồ.",
      "The instrumentation amplifier is designed to have such a stable "
      "resistive feedback unit that the desired gain can be obtained with "
      "the highest precision. The characteristic of high common-mode "
      "rejection of the operational amplifier is fully utilized in designing "
      "the instrumentation amplifier. Figure 5.12 shows a basic form of "
      "instrumentation amplifier. Instrument manufacturers modify the system "
      "slightly here and there to suit their particular measurement circuit "
      "and add their own trademark (TM). In this design, the operational "
      "amplifiers OA1 and OA2 have unity gain for the common-mode noise "
      "signal e_n. The calculation of the gain for the differential signals "
      "e_1 and e_2 can be made according to the following equations, with "
      "reference to the diagram.")

    FIG(b, 12, F.fig_f12(), lang)

    E(b, lang, "e_g1 = (1 + R_1/R_x)·e_1 − (R_1/R_x)·(e_n + e_2)",
      "e_g1 = (1 + R_1/R_x)·e_1 − (R_1/R_x)·(e_n + e_2)", num="")
    E(b, lang, "e_g2 = (1 + R_2/R_x)·e_2 − (R_2/R_x)·(e_n + e_1)",
      "e_g2 = (1 + R_2/R_x)·e_2 − (R_2/R_x)·(e_n + e_1)", num="")
    E(b, lang, "e_o = (e_g2 − e_g1)", "e_o = (e_g2 − e_g1)", num="")
    P(b, lang,
      "Nếu trong một điều kiện cụ thể R_1 có thể được làm bằng R_2, thì:",
      "If for a particular condition R_1 can be made equal to R_2, then:")
    E(b, lang, "e_o = (1 + 2R_1/R_x)·(e_2 − e_1)",
      "e_o = (1 + 2R_1/R_x)·(e_2 − e_1)", num="")
    P(b, lang,
      "Vấn đề trôi trong bộ khuếch đại đo lường là điểm thực sự khó khăn, "
      "đòi hỏi tinh chỉnh thiết kế trong các bộ khuếch đại. Hệ số khuếch đại "
      "của bộ khuếch đại đo lường có thể thay đổi bằng cách thay đổi điện "
      "trở biến đổi R_x.",
      "The drift problem in an instrumentation amplifier is the really "
      "troublesome area, where design refinements in amplifier units are "
      "required. The gain of the instrumentation amplifier can be changed "
      "by changing the variable resistance R_x.")

    return b
