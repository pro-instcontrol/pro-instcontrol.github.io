# -*- coding: utf-8 -*-
"""Safety Instrumented Systems, Chapter 12 — Functional Testing."""
import math

from vfig import (BLUE, GOLD, GREEN, GREY, INK, PAPER, RED, _arrow, _axes, _box,
                  _circle, _curve, _line, _path, _poly, _rect, _txt)
from pcfig import _finish

DARKRED = "#7f1d1d"
AMBER = "#f6e0b8"
PALE_GREEN = "#dcecdc"
PALE_RED = "#f3d6d2"
PALE_BLUE = "#e8eef6"
PALE_GOLD = "#f7efdd"
EDGE = "#b9b3a4"

# --- model behind figure 12-2 -------------------------------------------
# PFD(TI) = LD * TI / 2 + TD / TI   (undetected failures plus the time the
# unit spends out of service while it is being tested).  The source figure
# carries no parameters, so these are chosen to reproduce its axes.
LD = 5.0e-4          # dangerous failure rate, per year
TD = 1.6e-4          # test duration, years (about 1.4 h)
T_OPT = math.sqrt(2.0 * TD / LD)   # years, PFD minimum


def _pfd(m):
    """PFDavg for a manual test interval of m months."""
    ti = m / 12.0
    return LD * ti / 2.0 + TD / ti


def _valve(x, y):
    """A bow-tie valve body centred on (x, y)."""
    return [_poly([(x - 13, y - 8), (x, y), (x - 13, y + 8)], fill="#fff", sw=1.1, close=True),
            _poly([(x, y), (x + 13, y + 8), (x + 13, y - 8)], fill="#fff", sw=1.1, close=True)]


def _actuator(x, y):
    """Piston actuator above a valve, centred on x with its top at y."""
    return _rect(x - 12, y, 24, 16, "#fff", sw=1.1)


# ---------------------------------------------------------------- 12.1
def fig_12_1():
    """A simple high-pressure SIF: one transmitter, one logic block, one valve."""
    o = [_txt(330, 20, "Một chức năng an toàn áp suất cao: một cảm biến, một bộ logic, một van",
              8.2, weight="600")]

    o.append(_line(50, 200, 612, 200, sw=1.4))
    o.append(_arrow(604, 200, 622, 200, sw=1.4))
    o.append(_txt(54, 190, "dòng quá trình", 5.4, anchor="start", color=GREY))

    # transmitter
    o.append(_line(112, 200, 112, 144, sw=1.0))
    o.append(_circle(112, 122, 22, fill="#fff", sw=1.2))
    o.append(_txt(112, 119, "PT", 6.0, weight="600"))
    o.append(_txt(112, 131, "100", 6.0, weight="600"))

    # logic
    o.append(_rect(200, 96, 130, 48, PALE_BLUE, sw=1.1, stroke=EDGE))
    o.append(_txt(265, 119, "LOGIC RƠ-LE", 6.2, weight="600"))
    o.append(_txt(265, 132, "không tự chẩn đoán", 5.0, color=GREY))
    o.append(_arrow(136, 122, 198, 122, sw=1.0))

    # shutdown valve
    for s in _valve(400, 200):
        o.append(s)
    o.append(_actuator(400, 158))
    o.append(_line(400, 174, 400, 192, sw=1.0))
    o.append(_txt(400, 226, "PV-100", 6.0, weight="600"))
    o.append(_txt(400, 238, "van cắt", 5.0, color=GREY))
    o.append(_line(265, 144, 265, 166, sw=1.0))
    o.append(_line(265, 166, 400, 166, sw=1.0))
    o.append(_arrow(400, 166, 400, 160, sw=1.0))

    # control valve
    for s in _valve(520, 200):
        o.append(s)
    o.append(_actuator(520, 158))
    o.append(_line(520, 174, 520, 192, sw=1.0))
    o.append(_txt(520, 226, "PCV-100", 6.0, weight="600"))
    o.append(_txt(520, 238, "van điều khiển", 5.0, color=GREY))
    o.append(_rect(488, 84, 64, 30, "#fff", sw=1.0, dash="3 2", stroke=GREY))
    o.append(_txt(520, 103, "BPCS", 5.8, weight="600", color=GREY))
    o.append(_arrow(520, 116, 520, 156, sw=1.0, color=GREY))

    o.append(_txt(330, 268, "SIF chỉ gồm PT-100, khối logic và PV-100. Van PCV-100 thuộc BPCS, "
                            "nằm trên cùng tuyến nhưng không tính vào SIL.", 5.6, color=GREY))

    return _finish(o, 660, 284,
                   "Hình 12-1. Một chức năng an toàn áp suất cao đơn giản: cảm biến áp suất PT-100, "
                   "logic rơ-le và một van cắt PV-100, không dự phòng và không tự chẩn đoán. Chính vì "
                   "không có dự phòng nên chỉ cần một hỏng hóc nguy hiểm nằm im là cả chức năng mất tác "
                   "dụng — và chỉ có thử nghiệm định kỳ mới phát hiện được nó.",
                   "Figure 12-1. A simple high-pressure safety instrumented function: pressure "
                   "transmitter PT-100, relay logic and a single shutdown valve PV-100, with no redundancy "
                   "and no automatic diagnostics. Precisely because there is no redundancy, one latent "
                   "dangerous failure disables the whole function — and only periodic testing will find it.",
                   "Sơ đồ vòng đo áp suất cao: cảm biến PT-100 nối tới khối logic rơ-le, khối này điều "
                   "khiển van cắt PV-100 trên tuyến quá trình; van điều khiển PCV-100 của BPCS nằm trên "
                   "cùng tuyến.",
                   "A high-pressure loop: transmitter PT-100 feeds relay logic, which drives shutdown valve "
                   "PV-100 on the process line; the BPCS control valve PCV-100 sits on the same line.")


# ---------------------------------------------------------------- 12.3
def fig_12_2():
    """RRF against manual test interval: there is an optimum, and it is not zero."""
    o = [_txt(330, 20, "Hệ số giảm rủi ro theo chu kỳ thử: có một điểm tối ưu, và nó không phải bằng 0",
              8.2, weight="600")]

    x0, y0, W, H = 118, 62, 462, 186
    xt = [(m / 36.0, str(m)) for m in (0, 6, 12, 18, 24, 30, 36)]
    yt = [((math.log10(v) - 3.0), str(v)) for v in
          (1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000)]
    o.append(_axes(x0, y0, W, H, "chu kỳ thử (tháng)", "RRF", xt, yt))

    def f(m):
        v = 1.0 / _pfd(m)
        lg = math.log10(v)
        if lg < 3.0 or lg > 4.0:
            return None
        return lg

    o.append(_curve(f, x0, y0, W, H, n=400, xr=(1.6, 36.0), yr=(3.0, 4.0),
                    sw=1.9, color="#9b1c1c"))

    # the optimum
    om = T_OPT * 12.0
    ox = x0 + om / 36.0 * W
    oy = y0 + H - (math.log10(1.0 / _pfd(om)) - 3.0) * H
    o.append(_line(ox, oy, ox, y0 + H, sw=0.9, dash="3 2", color=GREY))
    o.append(_circle(ox, oy, 3.2, fill="#9b1c1c", sw=0.6))
    o.append(_txt(ox + 7, oy - 10, "tối ưu ≈ %.1f tháng · RRF ≈ %d"
                  % (om, round(1.0 / _pfd(om))), 5.8, anchor="start",
                  weight="600", color="#9b1c1c"))

    # why the two arms rise — kept outside the plot so they never sit on the line
    o.append(_txt(x0, y0 + H + 30, "thử quá dày: hệ nằm ngoài vận hành quá lâu", 5.2,
                  anchor="start", color=GREY))
    o.append(_txt(x0 + W, y0 + H + 30, "thử quá thưa: hỏng hóc nằm im quá lâu", 5.2,
                  anchor="end", color=GREY))

    return _finish(o, 660, 300,
                   "Hình 12-2. Hệ số giảm rủi ro (RRF) theo chu kỳ thử, thang logarit. Hình gốc không ghi "
                   "tham số, nên đường cong ở đây được tính lại từ mô hình nêu ở mục 8.9.1 — "
                   "PFD = λ<sub>d</sub>·TI/2 + T<sub>thử</sub>/TI — với λ<sub>d</sub> = 5×10⁻⁴/năm và "
                   "thời lượng một lần thử 1,4 giờ. Hai nhánh có hai nguyên nhân khác nhau: thử quá dày "
                   "thì hệ nằm ngoài vận hành quá lâu, thử quá thưa thì hỏng hóc nằm im quá lâu. Điểm tối "
                   "ưu ở đây là khoảng 9,6 tháng, tức RRF cao hơn khoảng 2,5 lần so với thử mỗi tháng một "
                   "lần.",
                   "Figure 12-2. Risk reduction factor against manual test interval, logarithmic scale. The "
                   "source figure gives no parameters, so the curve is recomputed from the model stated in "
                   "section 8.9.1 — PFD = λ<sub>d</sub>·TI/2 + T<sub>test</sub>/TI — with λ<sub>d</sub> = "
                   "5×10⁻⁴/yr and a test duration of 1.4 h. The two arms have different causes: testing too "
                   "often keeps the system out of service too long, testing too rarely leaves failures "
                   "latent too long. The optimum here is about 9.6 months, an RRF roughly 2.5 times that of "
                   "monthly testing.",
                   "Đồ thị RRF theo chu kỳ thử tính bằng tháng, thang logarit từ 1000 đến 10000, đạt cực "
                   "đại khoảng 2500 tại khoảng 9,6 tháng và giảm dần về hai phía.",
                   "A plot of RRF against test interval in months, logarithmic from 1000 to 10000, peaking "
                   "at about 2500 near 9.6 months and falling away on both sides.")


# ---------------------------------------------------------------- 12.5
def fig_12_3():
    """What has to be added before the same loop can be tested online."""
    o = [_txt(330, 20, "Muốn thử trực tuyến cùng vòng đo ấy: thêm van cách ly, van bypass và tiếp điểm hành trình",
              8.0, weight="600")]

    o.append(_line(40, 170, 612, 170, sw=1.4))
    o.append(_arrow(604, 170, 622, 170, sw=1.4))
    o.append(_txt(44, 160, "dòng quá trình", 5.4, anchor="start", color=GREY))

    # transmitter and isolation valve
    o.append(_line(100, 170, 100, 112, sw=1.0))
    o.append(_circle(100, 92, 20, fill="#fff", sw=1.2))
    o.append(_txt(100, 89, "PT", 5.8, weight="600"))
    o.append(_txt(100, 100, "100", 5.8, weight="600"))
    for s in _valve(150, 170):
        o.append(s)
    o.append(_txt(150, 194, "cách ly", 5.0, color=GREY))

    # logic
    o.append(_rect(196, 70, 104, 44, PALE_BLUE, sw=1.1, stroke=EDGE))
    o.append(_txt(248, 96, "LOGIC CẮT", 6.0, weight="600"))
    o.append(_arrow(122, 92, 194, 92, sw=1.0))

    # alarm — kept clear of the title, to the right of everything else
    o.append(_circle(560, 50, 17, fill="#fff", sw=1.1))
    o.append(_txt(560, 47, "ZA", 5.4, weight="600"))
    o.append(_txt(560, 58, "100", 5.4, weight="600"))
    o.append(_line(248, 70, 248, 50, sw=1.0))
    o.append(_arrow(248, 50, 541, 50, sw=1.0))

    # solenoid
    o.append(_rect(340, 76, 68, 32, PALE_GOLD, sw=1.1, stroke=EDGE))
    o.append(_txt(374, 96, "YC-100", 5.8, weight="600"))
    o.append(_arrow(302, 92, 338, 92, sw=1.0))

    # shutdown valve
    for s in _valve(430, 170):
        o.append(s)
    o.append(_actuator(430, 128))
    o.append(_line(430, 144, 430, 162, sw=1.0))
    o.append(_txt(430, 196, "PV-100", 6.0, weight="600"))
    o.append(_path("M 408 92 L 430 92 L 430 126", sw=1.0))
    o.append(_arrow(430, 126, 430, 130, sw=1.0))

    # limit switches
    for cx, tag in ((392, "ZSC-100"), (468, "ZSO-100")):
        o.append(_circle(cx, 216, 14, fill="#fff", sw=1.0, dash="2 2"))
        o.append(_txt(cx, 218, tag.split("-")[0], 4.6, weight="600"))
        o.append(_txt(cx, 240, tag, 4.8, color=GREY))
    o.append(_line(418, 186, 402, 204, sw=0.9, dash="2 2", color=GREY))
    o.append(_line(442, 186, 458, 204, sw=0.9, dash="2 2", color=GREY))

    # bypass loop
    o.append(_line(352, 170, 352, 268, sw=1.1))
    o.append(_line(352, 268, 520, 268, sw=1.1))
    o.append(_line(520, 268, 520, 170, sw=1.1))
    for s in _valve(436, 268):
        o.append(s)
    o.append(_txt(436, 290, "HV-100", 5.8, weight="600"))
    o.append(_txt(436, 301, "van bypass", 4.8, color=GREY))

    o.append(_txt(330, 314, "Mở HV-100 rồi đổi tín hiệu PT-100 để giả tín hiệu cắt: PV-100 phải đóng "
                            "đúng giá trị đặt, và ZSC-100 xác nhận nó đã đóng hết.", 5.4, color=GREY))

    return _finish(o, 660, 328,
                   "Hình 12-3. Cùng vòng đo như Hình 12-1 nhưng đã thêm phương tiện để thử trực tuyến: van "
                   "cách ly cho phép cô lập và tăng áp cảm biến, van bypass HV-100 cho phép dòng quá trình "
                   "đi vòng qua PV-100 trong lúc thử, và hai tiếp điểm hành trình ZSC-100/ZSO-100 xác nhận "
                   "van đã đóng hoặc mở hết. Nhờ vậy việc thử không cần dừng phân xưởng.",
                   "Figure 12-3. The same loop as Figure 12-1 with the facilities needed to test it online: "
                   "an isolation valve so the transmitter can be isolated and pressurised, a bypass valve "
                   "HV-100 so the process can flow around PV-100 during the test, and two limit switches "
                   "ZSC-100/ZSO-100 confirming that the valve really reached its end position. The test no "
                   "longer needs a unit shutdown.",
                   "Sơ đồ thử trực tuyến: cảm biến PT-100 có van cách ly, khối logic cắt điều khiển van "
                   "điện từ YC-100, van cắt PV-100 có hai tiếp điểm hành trình, và một nhánh bypass có van "
                   "HV-100 mắc song song quanh PV-100.",
                   "An online-testing arrangement: transmitter PT-100 with an isolation valve, shutdown "
                   "logic driving solenoid YC-100, shutdown valve PV-100 with two limit switches, and a "
                   "bypass branch with valve HV-100 around PV-100.")


FIGURES = [fig_12_1, fig_12_2, fig_12_3]
