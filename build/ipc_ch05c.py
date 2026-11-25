# -*- coding: utf-8 -*-
"""Chapter 5, sections 5.3 and 5.3.1 (EN/VI bilingual).

Source: Prasad, Jayaswal and Priye, *Instrumentation and Process Control*
(I.K. International, 2019), PDF pp. 251-254, printed pp. 239-242, decoded
text lines 9563-9686.  Covers 5.3 "Multiplexing" and 5.3.1 "Sample and
Hold Unit" with Figures 5.13-5.18.  This portion of the text carries no
printed equations and no tables, so none are invented here.

The printed diagrams are images in the PDF; the formulas in the text layer
around them are scrambled.  The `ipcfig5_b` supplier is authored in
parallel with this prose module.  When it is not yet importable, simple
but genuine vector redraws of the six printed diagrams are installed as
non-overwriting fallbacks; as soon as the real supplier registers
`fig_f13` .. `fig_f18`, those callables win.
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


_MID = "ipc5c"


def _defs():
    return ('<defs><marker id="%s" viewBox="0 0 8 8" refX="7" refY="4" '
            'markerWidth="6" markerHeight="6" orient="auto">'
            '<path d="M0 0 L8 4 L0 8 z" fill="#1f3a5f"/></marker></defs>'
            % _MID)


def _w(pts, arrow=False, dash=False):
    d = "M" + " L".join("%g %g" % p for p in pts)
    m = ' marker-end="url(#%s)"' % _MID if arrow else ""
    da = ' stroke-dasharray="3 2"' if dash else ""
    return ('<path d="%s" fill="none" stroke="#1f3a5f" '
            'stroke-width="1.1"%s%s/>' % (d, da, m))


def _node(x, y):
    return '<circle cx="%d" cy="%d" r="2.2" fill="#1f3a5f"/>' % (x, y)


def _and(x, y, w=30, h=20):
    """D-shaped AND gate with its left edge at x and centre line at y."""
    r = h / 2.0
    return ('<path d="M%d %g L%g %g A %g %g 0 0 1 %g %g L%d %g z" '
            'fill="#ffffff" stroke="#1f3a5f" stroke-width="1.1"/>'
            % (x, y - r, x + w - r, y - r, r, r, x + w - r, y + r,
               x, y + r))


def _or(x, y, w=45, h=84):
    """OR gate with its left edge at x and centre line at y."""
    a, b = h / 2.0, w / 2.0
    return ('<path d="M%d %g Q %g %g %g %g Q %g %g %d %g '
            'Q %g %g %d %g z" fill="#ffffff" stroke="#1f3a5f" '
            'stroke-width="1.1"/>'
            % (x, y - a, x + b, y - a, x + w, y,
               x + b, y + a, x, y + a,
               x + b * 0.8, y, x, y - a))


def _cap(x, y_top, y_bot):
    m = (y_top + y_bot) / 2.0
    return (_w([(x, y_top), (x, m - 4)]) +
            _w([(x - 12, m - 4), (x + 12, m - 4)]) +
            _w([(x - 12, m + 4), (x + 12, m + 4)]) +
            _w([(x, m + 4), (x, y_bot)]))


def _gnd(x, y):
    return ('<path d="M%d %d L%d %d M%d %d L%d %d M%d %d L%d %d" '
            'fill="none" stroke="#1f3a5f" stroke-width="1"/>'
            % (x - 9, y, x + 9, y, x - 6, y + 4, x + 6, y + 4,
               x - 3, y + 8, x + 3, y + 8))


_FIG_TEXT = {
    13: ("Sơ đồ khối ghép kênh", "Multiplexing block diagram",
         "Tín hiệu từ bộ điều hòa đi qua mạch lấy mẫu-giữ mẫu, bộ ghép kênh "
         "tương tự và ADC trước khi tới đầu ra; máy tính tạo đường địa chỉ "
         "và bộ giải mã để chọn kênh",
         "Signals from the conditioner pass through a sample and hold unit, "
         "an analog multiplexer and an ADC on their way to the output; "
         "computer-generated address lines and a decoder select the channel"),
    14: ("Bộ giải mã 2 sang 4", "Two-to-four decoder",
         "Bốn cổng kết hợp dùng các tín hiệu x, x̄, y, ȳ tạo bốn đầu ra 0, 1, 2, 3",
         "Four AND gates driven by x, x̄, y and ȳ give the four outputs "
         "0, 1, 2 and 3"),
    15: ("Bộ ghép kênh tương tự bốn kênh", "Four-channel analog multiplexer",
         "Đường địa chỉ từ máy tính điều khiển bộ giải mã chọn một trong bốn "
         "công tắc FET để nối một đầu vào tương tự ra đường ra",
         "Computer-generated address lines drive a decoder that selects one "
         "of four FET switches to connect an analog input to the output line"),
    16: ("Bộ ghép kênh số 4 sang 1", "Four-to-one digital multiplexer",
         "Bốn đầu vào được đưa qua bốn cổng kết hợp và một cổng tuyển; các đường "
         "chọn x, x̄, y, ȳ quyết định đầu ra",
         "Four inputs pass through four AND gates and one OR gate; the "
         "select lines x, x̄, y and ȳ determine the output"),
    17: ("Mạch lấy mẫu-giữ mẫu dùng rơle", "Relay-operated sample and hold circuit",
         "Công tắc do rơle vận hành nạp tụ giữ mẫu Ch từ Vin và giữ điện áp "
         "sau khi tiếp điểm mở",
         "A relay-operated switch charges the holding capacitor Ch from Vin "
         "and retains the voltage after the contact opens"),
    18: ("Mạch lấy mẫu-giữ mẫu dùng FET", "FET sample and hold circuit",
         "Công tắc FET điều khiển bằng xung nạp tụ Ch; bộ theo điện áp có trở "
         "kháng lớn hạn chế sự phóng điện của tụ",
         "A pulse-driven FET switch charges capacitor Ch; a high-impedance "
         "voltage follower limits the discharge of the capacitor"),
}


def _standalone_fig(n):
    o = [_defs()]

    if n == 13:
        o += [_r(20, 70, 110, 130),
              _t(75, 90, "Signal", 7.2),
              _t(75, 103, "conditioning", 7.0),
              _t(75, 116, "unit", 7.2),
              _r(160, 70, 100, 130),
              _t(210, 90, "Sample and", 7.2),
              _t(210, 103, "hold unit", 7.2),
              _r(300, 70, 110, 130),
              _t(355, 120, "Analog", 7.2),
              _t(355, 133, "multiplexing", 7.0),
              _t(355, 146, "unit", 7.2)]
        for y, lab in zip((140, 154, 168, 182, 196),
                          ("1", "2", "3", "…", "n")):
            o += [_t(75, y + 3, lab, 7.2),
                  _t(210, y + 3, lab, 7.2),
                  _w([(130, y), (160, y)], True),
                  _w([(260, y), (300, y)], True)]
        o += [_w([(410, 121), (445, 121)], True),
              _r(445, 105, 50, 32),
              _t(470, 125, "ADC", 8.0),
              _w([(495, 121), (515, 121)], True),
              _t(520, 118, "Output", 7.2, anchor="start"),
              _t(520, 131, "1, 2, 3 ... n", 7.0, anchor="start"),
              _r(430, 18, 235, 50),
              _t(548, 36, "Computer generated", 7.2),
              _t(548, 50, "address lines/decoder", 7.0),
              _t(548, 63, "1, 2, 3 ... n", 7.0),
              _w([(470, 68), (470, 78), (410, 78)], True),
              _w([(570, 68), (570, 88), (410, 88)], True),
              _r(445, 160, 120, 36),
              _t(505, 182, "Control unit", 7.5),
              _w([(445, 178), (410, 178)], True),
              _w([(470, 160), (470, 137)], True)]

    elif n == 14:
        o += [_t(130, 42, "x", 8.0),
              _t(210, 42, "x̄", 8.0),
              _t(290, 42, "y", 8.0),
              _t(370, 42, "ȳ", 8.0)]
        for xx in (130, 210, 290, 370):
            o.append(_w([(xx, 50), (xx, 195)]))
        for gy, a, b, out in ((70, 210, 370, "0"),
                              (105, 210, 290, "1"),
                              (140, 130, 370, "2"),
                              (175, 130, 290, "3")):
            o += [_w([(a, gy - 5), (440, gy - 5)]),
                  _w([(b, gy + 5), (440, gy + 5)]),
                  _node(a, gy - 5), _node(b, gy + 5),
                  _and(440, gy),
                  _w([(470, gy), (505, gy)], True),
                  _t(516, gy + 3, out, 8.0, anchor="start")]

    elif n == 15:
        o += [_t(85, 48, "Computer generated", 7.0),
              _t(85, 61, "address lines", 7.0),
              _w([(85, 68), (85, 100)], True),
              _r(35, 100, 90, 85),
              _t(80, 145, "Decoder", 7.5),
              _r(560, 25, 100, 28),
              _t(610, 43, "Analog inputs", 7.2),
              _w([(610, 53), (610, 70)], True),
              _w([(205, 70), (610, 70)])]
        for cx, lab in ((205, "FETS 1"), (305, "FETS 2"),
                        (405, "FETS 3"), (505, "FETS 4")):
            o += [_w([(cx, 70), (cx, 95)], True),
                  _r(cx - 35, 95, 70, 34),
                  _t(cx, 116, lab, 7.2),
                  _w([(cx + 25, 129), (cx + 25, 145)]),
                  _node(cx + 25, 145)]
        for sy, cx in ((145, 190), (158, 290), (171, 390), (184, 490)):
            o += [_w([(125, sy), (cx, sy)]),
                  _w([(cx, sy), (cx, 129)], True),
                  _node(cx, sy)]
        o += [_w([(230, 145), (600, 145)], True),
              _t(605, 148, "Analog output", 7.2, anchor="start")]

    elif n == 16:
        o += [_t(40, 70, "Input lines", 7.0, anchor="start"),
              _w([(95, 74), (110, 80)], True),
              _t(400, 38, "Select lines", 7.0, anchor="end"),
              _w([(398, 42), (385, 48)], True)]
        for xx, lab in ((130, "x"), (210, "x̄"),
                        (290, "y"), (370, "ȳ")):
            o += [_t(xx, 56, lab, 8.0),
                  _w([(xx, 62), (xx, 175)])]
        for yy, lab in ((85, "0"), (110, "1"),
                        (135, "2"), (160, "3")):
            o += [_w([(40, yy), (400, yy)]),
                  _t(35, yy + 3, lab, 8.0, anchor="end"),
                  _node(130, yy), _node(210, yy),
                  _node(290, yy), _node(370, yy),
                  _and(400, yy, 30, 20),
                  _w([(430, yy), (470, yy)]),
                  _t(442, yy - 10, lab, 6.8)]
        o += [_or(470, 122),
              _w([(515, 122), (545, 122)], True),
              _t(550, 126, "Output", 7.5, anchor="start")]

    elif n == 17:
        o += [_t(40, 58, "Vin", 7.5, anchor="start"),
              _node(60, 70),
              _w([(60, 70), (205, 70)]),
              _w([(222, 70), (540, 70)]),
              _node(540, 70),
              _t(545, 58, "Vout", 7.5, anchor="start"),
              _t(240, 58, "Contact", 7.2, anchor="start"),
              '<circle cx="205" cy="70" r="3" fill="#ffffff" '
              'stroke="#1f3a5f" stroke-width="1.1"/>',
              '<circle cx="222" cy="70" r="3" fill="#ffffff" '
              'stroke="#1f3a5f" stroke-width="1.1"/>',
              _w([(205, 68), (219, 61)]),
              _cap(450, 70, 135),
              _gnd(450, 135),
              _t(468, 110, "Ch", 7.5, anchor="start")]
        coil = ['<path d="M%d %d ' % (210, 96)]
        for k in range(5):
            y0 = 96 + k * 9
            coil.append('a 7 4.5 0 0 1 0 9 ')
        coil.append('" fill="none" stroke="#1f3a5f" stroke-width="1.1"/>')
        o.append("".join(coil))
        o += [_w([(210, 96), (212, 66)], dash=True),
              _t(258, 122, "Relay coil", 7.2, anchor="start"),
              '<circle cx="140" cy="165" r="2.2" fill="#ffffff" '
              'stroke="#1f3a5f" stroke-width="1.1"/>',
              '<circle cx="180" cy="165" r="2.2" fill="#ffffff" '
              'stroke="#1f3a5f" stroke-width="1.1"/>',
              _w([(140, 165), (140, 145), (203, 145)]),
              _w([(180, 165), (180, 150), (217, 150)]),
              _t(160, 180, "Switching pulses", 7.0)]

    else:  # n == 18
        o += [_t(40, 72, "Vin", 7.5, anchor="start"),
              _node(50, 85),
              _w([(50, 85), (148, 85)]),
              '<circle cx="170" cy="85" r="22" fill="#ffffff" '
              'stroke="#1f3a5f" stroke-width="1.1"/>',
              _w([(170, 67), (170, 103)]),
              _w([(156, 78), (156, 92)]),
              _t(170, 50, "FET switch", 7.5),
              _w([(170, 145), (170, 107)], True),
              _t(170, 162, "Driver pulse", 7.0),
              _w([(192, 85), (250, 85)]),
              _node(250, 85),
              _cap(250, 85, 142),
              _gnd(250, 142),
              _t(266, 114, "Ch", 7.5, anchor="start"),
              _w([(250, 85), (350, 100)]),
              '<polygon points="350,55 350,115 420,85" fill="#ffffff" '
              'stroke="#1f3a5f" stroke-width="1.2"/>',
              _t(362, 72, "−", 10),
              _t(362, 105, "+", 10),
              _w([(430, 85), (385, 85), (385, 70), (350, 70)]),
              _w([(420, 85), (530, 85)]),
              _node(530, 85),
              _t(535, 72, "Vout", 7.5, anchor="start"),
              _t(392, 46, "+", 9.0),
              _t(392, 128, "−", 9.0),
              _w([(470, 125), (412, 96)], True),
              _t(478, 132, "Voltage follower", 7.2, anchor="start")]

    cvi, cen, avi, aen = _FIG_TEXT[n]
    o.append(_t(340, 242, "Hình 5.%d   ·   Figure 5.%d" % (n, n),
                6.4, color="#888888"))
    svg = ('<svg xmlns="http://www.w3.org/2000/svg" width="680" height="250" '
           'viewBox="0 0 680 250"><rect width="680" height="250" '
           'fill="#ffffff"/>%s</svg>' % "".join(o))
    return (svg, "Hình 5.%d · %s" % (n, cvi),
            "Figure 5.%d · %s" % (n, cen), avi, aen)


for _n in range(13, 19):
    if not hasattr(F, "fig_f%02d" % _n):
        setattr(F, "fig_f%02d" % _n, (lambda _n=_n: _standalone_fig(_n)))


# ------------------------------------------------------------------- prose
def section(lang):
    b = []

    # ---------------------------------------------------------------- 5.3
    H(b, lang, "5.3 Ghép kênh", "5.3 Multiplexing")

    P(b, lang,
      "Khi cần truyền một số biến công nghệ chỉ trên một kênh duy nhất, người "
      "ta dùng phương pháp đo và truyền dùng chung thời gian, gọi là ghép "
      "kênh. Để hệ thống thu thập dữ liệu dựa trên PC (máy tính cá nhân) hoạt "
      "động đúng đắn, các tín hiệu tương tự từ các bộ chuyển đổi lắp tại hiện "
      "trường được quét qua bộ quét và được truyền qua bộ ghép kênh. Trong "
      "cách bố trí này, mạch lấy mẫu-giữ mẫu được thêm vào trước bộ ghép kênh "
      "và bộ chuyển đổi tương tự-số (ADC) được lắp sau bộ ghép kênh như Hình "
      "5.13. Theo cách này, các đầu vào tương tự được ghép theo từng kênh với "
      "hệ thống truyền thông để truyền và xử lý tiếp.",
      "When a number of process variables are required to be transmitted on "
      "one channel only, the time shared method of measurement and "
      "transmission is employed and is known as multiplexing. For a PC "
      "(Personal Computer) based data acquisition system to operate "
      "properly, the analog signals available from the field mounted "
      "transducers are scanned through a scanner and transmitted through a "
      "multiplexing unit. In this arrangement, a sample and hold circuit is "
      "added before the multiplexer unit and an analog-to-digital converter "
      "(ADC) is installed after the multiplexer unit, as shown in Figure "
      "5.13. In this way, the analog inputs are multiplexed channel-wise "
      "with the communication system for further transmission and "
      "processing.")

    FIG(b, 13, F.fig_f13(), lang)

    P(b, lang,
      "Các đường địa chỉ do máy tính tạo ra chọn từng kênh tương tự một qua "
      "bộ giải mã để lấy mẫu. Một bộ giải mã đơn giản 2 sang 4 được trình "
      "bày ở Hình 5.14. Bộ giải mã bậc cao hơn có thể xây dựng dễ dàng dựa "
      "trên bộ này. Như quan sát thấy, có bốn cổng kết hợp được dùng cho bộ "
      "giải mã 2 sang 4. Tương tự như vậy, đối với bộ giải mã 4 sang 16 sẽ "
      "cần mười sáu cổng kết hợp.",
      "The computer generated address lines select an analog channel through "
      "the decoder one by one for sampling. A simple two-to-four decoder is "
      "presented in Figure 5.14. A higher order decoder can be manipulated "
      "easily on the basis of this one. As is observed, there are four AND "
      "gates used for a two-to-four decoder. In a similar way, for a "
      "four-to-sixteen decoder, sixteen AND gates will be required.")

    FIG(b, 14, F.fig_f14(), lang)

    P(b, lang,
      "Theo cách tương tự, Hình 5.15 trình bày một bộ ghép kênh tương tự đơn "
      "giản bốn kênh. Tùy theo trạng thái của các đường địa chỉ, bộ giải mã "
      "chọn một công tắc FET cụ thể và đầu vào tương tự thích hợp từ bộ "
      "chuyển đổi được nối vào đường ra tương tự. Các bộ ghép kênh bậc cao "
      "hơn có thể được thiết kế theo cách tương tự.",
      "On a similar pattern, a simple four-channel analog multiplexing unit "
      "is presented in Figure 5.15. Depending upon the status of the address "
      "lines, the decoder selects a particular FET switch and the appropriate "
      "analog input from the transducer is connected to the analog output "
      "line. A higher order multiplexing unit can be designed on a similar "
      "pattern.")

    FIG(b, 15, F.fig_f15(), lang)

    P(b, lang,
      "Hình 5.16 cho thấy một bộ ghép kênh số đơn giản kiểu bốn vào – một ra.",
      "Figure 5.16 shows a simple four-to-one digital type of multiplexer "
      "unit.")

    FIG(b, 16, F.fig_f16(), lang)

    # ------------------------------------------------------------ 5.3.1
    H(b, lang, "5.3.1 Mạch lấy mẫu-giữ mẫu",
      "5.3.1 Sample and Hold Unit")

    P(b, lang,
      "Như đã chỉ ra ở Hình 5.13, mạch lấy mẫu-giữ mẫu đưa các tín hiệu từ bộ "
      "chuyển đổi vào bộ ghép kênh tương tự một cách có hệ thống. Hoạt động "
      "của mạch lấy mẫu-giữ mẫu rất đơn giản và được thể hiện ở Hình 5.17. "
      "Thực chất, đây là sự kết hợp giữa một công tắc (do rơle vận hành) và "
      "một tụ giữ mẫu Ch như minh họa. Điện áp trên tụ giữ mẫu Ch theo dõi Vin "
      "(tín hiệu vào) trong giai đoạn lấy mẫu khi xung đóng cắt làm đóng tiếp "
      "điểm công tắc, và giữ điện tích trên tụ trong giai đoạn giữ mẫu. Khi "
      "tiếp điểm công tắc đóng, tụ giữ mẫu được nạp đến mức điện áp bằng với "
      "mức điện áp đầu vào. Khi tiếp điểm công tắc mở, tụ tiếp tục giữ điện "
      "áp đã thu được trong giai đoạn lấy mẫu. Khoảng thời gian mà tụ giữ "
      "điện áp đó được gọi là thời gian giữ mẫu.",
      "As indicated by Figure 5.13, the sample and hold unit feeds the "
      "transducer signals systematically to the analog multiplexer unit. The "
      "operation of a sample and hold unit is simple and is shown in Figure "
      "5.17. It is in fact a combination of a switch (operated by a relay) "
      "and a holding capacitor Ch, as shown. The voltage across the holding "
      "capacitor Ch follows Vin (the input signal) during the sampling "
      "period, when the switching pulse closes the switch contact, and holds "
      "the charge at the capacitor during the hold period. When the switch "
      "contact closes, the holding capacitor is charged to a voltage equal "
      "to the input voltage level. When the switch contact opens, the "
      "capacitor continues to hold the voltage acquired during sampling. The "
      "period for which the capacitor holds the voltage is called the "
      "holding time.")

    FIG(b, 17, F.fig_f17(), lang)

    P(b, lang,
      "Trong thiết kế hiện đại như Hình 5.18, một công tắc FET điều khiển "
      "bằng xung tác động lên tín hiệu vào và tụ giữ mẫu Ch chỉ đơn giản theo "
      "dõi các tín hiệu vào. Tụ giữ mẫu Ch được nối vào đường ra qua một phần "
      "tử theo điện áp có trở kháng đầu vào rất cao, nhờ đó sự phóng điện của "
      "tụ Ch bị hạn chế ở mức được kiểm soát.",
      "In the modern design shown in Figure 5.18, a pulse driven FET switch "
      "operates upon the input signal and the holding capacitor Ch just "
      "follows the input signals. The holding capacitor Ch is connected to "
      "the output line through a voltage follower element having very high "
      "input impedance, which ultimately restricts the discharge of "
      "capacitor Ch to a controlled amount only.")

    FIG(b, 18, F.fig_f18(), lang)

    return b
