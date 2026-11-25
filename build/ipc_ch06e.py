# -*- coding: utf-8 -*-
"""Chapter 6, section 6.5 "Proportional-cum-Integral Control (PI control)".

Source: Prasad, Jayaswal and Priye, *Instrumentation and Process Control*
(I.K. International, 2019), PDF pp. 297-300, printed pp. 285-288, decoded
text lines 11446-11537.  Covers the PI response, the printed gain settings
for flow, level and pressure loops, the integral-rate setting, the electronic
circuit and the pneumatic implementation.  Figures 6.14 and 6.15 are inserted
where the prose refers to them; their labels were checked against the page
renders work/ipc6_pages/p298.png and p299.png.  There are no numbered
equations, tables or references in this span, so none are invented.

The figure suppliers are authored in parallel.  Until they are importable the
two small vector redraws below are installed with non-overwriting hasattr
guards, so a real supplier callable is never replaced.
"""

import math

import ipcfig6 as F
from ipc_ch06_lib import H, P, L, FIG

INK = "#1f3a5f"
GREY = "#777777"


# --------------------------------------------------------------- SVG helpers
def _t(x, y, s, size=7.0, anchor="middle", color=INK):
    return ('<text x="%s" y="%s" text-anchor="%s" style="font:%spx '
            'Inter,Helvetica,sans-serif;fill:%s">%s</text>'
            % (x, y, anchor, size, color, s))


def _ln(x1, y1, x2, y2, color=INK, sw=1.2, dash=""):
    d = ' stroke-dasharray="%s"' % dash if dash else ""
    return ('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" '
            'stroke-width="%s"%s/>' % (x1, y1, x2, y2, color, sw, d))


def _poly(pts, color=INK, sw=1.6, dash=""):
    d = ' stroke-dasharray="%s"' % dash if dash else ""
    p = " ".join("%.1f,%.1f" % (x, y) for x, y in pts)
    return ('<polyline points="%s" fill="none" stroke="%s" '
            'stroke-width="%s"%s/>' % (p, color, sw, d))


def _rect(x, y, w, h, fill="#ffffff", color=INK, sw=1.2):
    return ('<rect x="%s" y="%s" width="%s" height="%s" fill="%s" '
            'stroke="%s" stroke-width="%s"/>' % (x, y, w, h, fill, color, sw))


def _defs(mid):
    return ('<defs><marker id="%s" viewBox="0 0 8 8" refX="7" refY="4" '
            'markerWidth="6" markerHeight="6" orient="auto">'
            '<path d="M0 0 L8 4 L0 8 z" fill="%s"/></marker></defs>' % (mid, INK))


def _ar(x1, y1, x2, y2, mid, sw=1.2, color=INK):
    return ('<path d="M%s %s L%s %s" fill="none" stroke="%s" '
            'stroke-width="%s" marker-end="url(#%s)"/>'
            % (x1, y1, x2, y2, color, sw, mid))


def _cap(n):
    return _t(340, 245, "Hinh 6.%d   ·   Figure 6.%d" % (n, n),
              6.4, color=GREY)


# --------------------------------------------------------- fallback figures
def _fig14():
    """PI response: set value, proportional step, PI ramp and rate-time drop."""
    mid = "ipc6e14"
    o = [_defs(mid)]

    # Panel A - process variable and set-value step.
    o += [_ar(72, 78, 72, 24, mid), _ar(72, 78, 332, 78, mid),
          _t(64, 30, "Process", 7.0, anchor="end"),
          _t(64, 39, "variable", 7.0, anchor="end"),
          _t(336, 81, "Time", 7.0, anchor="start"),
          _ln(80, 66, 108, 66), _ln(108, 66, 108, 38), _ln(108, 38, 300, 38),
          _t(304, 41, "Set value", 7.0, anchor="start")]

    # Panel B - output: proportional step, error band and the PI ramp.
    o += [_ar(72, 150, 72, 86, mid), _ar(72, 150, 332, 150, mid),
          _t(64, 95, "Output", 7.0, anchor="end"),
          _ln(80, 140, 108, 140), _ln(108, 140, 108, 106), _ln(108, 106, 300, 106),
          _t(304, 109, "Proportional action", 7.0, anchor="start"),
          _ln(108, 132, 300, 132, color=GREY, sw=1.0, dash="5,4"),
          _poly([(108, 132), (300, 92)], color=INK, sw=1.8),
          _t(304, 122, "PI action", 7.0, anchor="start"),
          _ar(150, 132, 150, 140, mid, sw=0.9),
          _t(150, 136, "Es", 7.0),
          _ln(108, 146, 288, 146, color=GREY, sw=0.9),
          _ln(108, 143, 108, 149, color=GREY, sw=0.9),
          _ln(288, 143, 288, 149, color=GREY, sw=0.9),
          _t(198, 157, "Time for one repeat", 7.0)]

    # Panel C - exponential drop used to define the rate time.
    pts = []
    for i in range(81):
        t = i / 80.0
        pts.append((92 + 208 * t, 205 - 33 * math.exp(-4.0 * t)))
    o += [_ar(72, 215, 72, 162, mid), _ar(72, 215, 332, 215, mid),
          _t(64, 170, "Output", 7.0, anchor="end"),
          _poly(pts, color=INK, sw=1.8),
          _ln(92, 181, 150, 181, color=GREY, sw=1.0, dash="5,4"),
          _t(96, 178, "63.2% of drop", 6.6, anchor="start"),
          _ln(92, 208, 122, 208, color=GREY, sw=0.9),
          _ln(92, 205, 92, 211, color=GREY, sw=0.9),
          _ln(122, 205, 122, 211, color=GREY, sw=0.9),
          _t(150, 206, "Rate time", 7.0, anchor="start"),
          _t(336, 218, "Time", 7.0, anchor="start"),
          _cap(14)]

    svg = ('<svg xmlns="http://www.w3.org/2000/svg" width="680" height="250" '
           'viewBox="0 0 680 250"><rect width="680" height="250" '
           'fill="#ffffff"/>%s</svg>' % "".join(o))
    return (svg,
            "Hinh 6.14 · Dap ung dieu khien PI",
            "Figure 6.14 · PI control action response",
            "Do thi dap ung PI voi thoi gian lap lai va thoi gian toc do",
            "PI response graph with repeat time and rate time")


def _fig15():
    """Electronic PI controller: op-amp, input network and two adjustments."""
    mid = "ipc6e15"
    o = [_defs(mid)]

    # Error signal and input network.
    o += [_ar(70, 160, 70, 110, mid),
          _t(60, 138, "Ein", 7.0, anchor="end"),
          _ln(70, 110, 108, 110), _rect(108, 106, 30, 8),
          _t(123, 102, "R1", 7.0),
          _ln(138, 110, 196, 110),
          _ln(196, 110, 196, 116), _ln(196, 124, 196, 124),
          _ln(196, 124, 300, 124),
          _t(200, 98, "Cin", 7.0)]

    # Amplifier and output.
    o += [('<polygon points="300,92 300,178 396,135" fill="#eef3fb" '
           'stroke="%s" stroke-width="1.2"/>' % INK),
          _t(336, 140, "OA", 7.0),
          _ar(396, 135, 560, 135, mid),
          _t(566, 139, "E0", 7.0, anchor="start")]

    # Integral adjustment Ri to ground.
    o += [_ln(196, 170, 250, 170), _rect(250, 166, 30, 8),
          _t(265, 162, "Ri", 7.0),
          _ln(280, 170, 280, 196),
          _ln(268, 196, 292, 196), _ln(271, 200, 289, 200),
          _ln(274, 204, 286, 204),
          _t(170, 196, "Integral adjustment", 7.0)]

    # Feedback capacitor Cfb around the amplifier.
    o += [_ln(396, 135, 396, 72), _ln(396, 72, 210, 72),
          _ln(210, 72, 210, 78), _ln(210, 86, 210, 86),
          _ln(210, 86, 210, 124),
          _t(210, 66, "Cfb", 7.0)]

    # Proportional band adjustment Rp across the output.
    o += [_ln(440, 135, 440, 176), _rect(432, 152, 8, 26),
          _t(450, 155, "Rp", 7.0, anchor="start"),
          _ar(440, 170, 516, 170, mid, sw=0.9, color=GREY),
          _ln(440, 176, 516, 176),
          _t(512, 196, "Proportional band adjustment", 7.0),
          _cap(15)]

    svg = ('<svg xmlns="http://www.w3.org/2000/svg" width="680" height="250" '
           'viewBox="0 0 680 250"><rect width="680" height="250" '
           'fill="#ffffff"/>%s</svg>' % "".join(o))
    return (svg,
            "Hinh 6.15 · Mach dieu khien PI dien tu",
            "Figure 6.15 · Electronic PI controller circuit",
            "So do mach PI voi chinh dai ty le va chinh toc do tich phan",
            "PI circuit with proportional band and integral rate adjustments")


for _n, _fn in ((14, _fig14), (15, _fig15)):
    if not hasattr(F, "fig_f%02d" % _n):
        setattr(F, "fig_f%02d" % _n, _fn)


# --------------------------------------------------------------------- prose
def section(lang):
    b = []

    H(b, lang,
      "6.5 Điều khiển tỷ lệ cộng tích phân (điều khiển PI)",
      "6.5 Proportional-cum-Integral Control (PI Control)")

    P(b, lang,
      "Đã được chứng minh rằng điều khiển tích phân có khả năng loại bỏ độ lệch "
      "tĩnh do điều khiển tỷ lệ tạo ra. Vì vậy, sự kết hợp giữa hành động điều "
      "khiển tỷ lệ và tích phân có khả năng hiệu chỉnh chính xác trong các vòng "
      "điều khiển thực tế cho mọi điều kiện tải. Ở đây, tốc độ tích phân, được "
      "biểu thị bằng số lần lặp mỗi phút, thực chất là số lần trong mỗi phút mà "
      "đầu ra do hành động tỷ lệ tạo ra được lặp lại bởi hành động tích phân. "
      "Hiệu ứng của nó là cứ tiếp tục cộng thêm sự hiệu chỉnh vào biến quá "
      "trình chừng nào còn độ lệch. Điều này về thực chất giống như dịch dần "
      "điểm chỉnh giá trị cài đặt, buộc hành động điều khiển phải đi theo cho "
      "đến khi đạt lại giá trị cài đặt cũ. Khi tải thay đổi, phản ứng tức thời "
      "đến từ hành động tỷ lệ, sau đó được hành động tích phân tăng lên với tốc "
      "độ cố định. Điều này đôi khi có thể gây chu trình dao động kéo dài nếu "
      "tải thay đổi nhanh.",
      "It has already been shown that integral control can eliminate the offset "
      "created by proportional control acting alone. A combination of "
      "proportional and integral control action can therefore provide exact "
      "correction in practical control loops for all load conditions. Here the "
      "integral rate, expressed in repeats per minute, is actually the number "
      "of times per minute that the output produced by proportional action is "
      "repeated by the integral action. Its effect is to go on adding correction "
      "to the process variable for as long as the deviation exists. In effect "
      "this is the same as gradually shifting the set-value adjustment, forcing "
      "the control action to follow until the previous set value is reached. On "
      "a load change the immediate response comes from proportional action, "
      "which is then increased at a fixed rate by the integral action. This can "
      "sometimes cause prolonged cycling if the load change is rapid.")

    P(b, lang,
      "Hành động điều khiển PI phù hợp với các quá trình có hằng số thời gian "
      "nhỏ và độ trễ nhỏ đến trung bình. Đối với việc điều khiển các biến quá "
      "trình như lưu lượng, mức chất lỏng hoặc áp suất, điều khiển PI được áp "
      "dụng gần như không ngoại lệ. Khi biến quá trình trở về đúng giá trị cài "
      "đặt ban đầu, hành động tích phân lập tức ngừng.",
      "PI control action is suitable for processes having a small time constant "
      "and small to medium dead times. For the control of process variables such "
      "as flow, level or pressure, PI control is applied almost invariably. When "
      "the process variable is returned to the original set value, the integral "
      "action ceases immediately.")

    P(b, lang,
      "Chế độ điều khiển PI là chế độ điều khiển đa dụng nhất, có khả năng xử lý "
      "khá tốt hầu hết các tổ hợp đặc tính quá trình. Các đặc tính quá trình "
      "cùng với cài đặt độ lợi thực tế cần thiết cho các vòng điều khiển lưu "
      "lượng, mức và áp suất được nêu dưới đây:",
      "The PI mode of control is the most versatile mode of control action, "
      "capable of handling most combinations of process characteristics quite "
      "satisfactorily. The process characteristics together with the most "
      "required practical gain settings for flow, level and pressure control "
      "loops are given below:")

    L(b, lang,
      ["Vòng lưu lượng: dung lượng = không đáng kể; độ trễ truyền = nhỏ; "
       "độ trễ = nhỏ; cài đặt độ lợi = 0,2 đến 10.",
       "Vòng mức chất lỏng: dung lượng = một dung lượng đơn nhỏ hoặc trung "
       "bình; độ trễ truyền = nhỏ hoặc trung bình; độ trễ = nhỏ; cài đặt độ lợi "
       "= 2 đến 10.",
       "Vòng áp suất: dung lượng = một dung lượng đơn nhỏ hoặc trung bình; "
       "truyền = rất nhỏ; độ trễ = nhỏ; cài đặt độ lợi = 5 đến 50 đối với "
       "áp suất chất lỏng; cài đặt độ lợi = 20 đến 50 đối với áp suất khí."],
      ["Flow control loop: capacitance = negligible; transfer lag = small; "
       "dead time = small; gain setting = 0.2 to 10.",
       "Level control loop: capacitance = small or medium single capacitance; "
       "transfer lag = small or medium; dead time = small; gain setting = 2 to 10.",
       "Pressure control loop: capacitance = small or medium single capacitance; "
       "transfer = very small; dead time = small; gain setting = 5 to 50 for "
       "liquid pressure control; gain setting = 20 to 50 for gas pressure control."])

    P(b, lang,
      "Về cài đặt tốc độ tích phân, dung lượng nhỏ cho phép tốc độ tích phân "
      "cao hơn; độ trễ truyền và độ trễ đòi hỏi tốc độ tích phân thấp hơn. Tốc "
      "độ tích phân cao hơn khử độ lệch nhanh hơn, trong khi tốc độ thấp hơn "
      "tránh dao động quá mức của biến quá trình. Hình 6.14 cho thấy đồ thị "
      "chi tiết của hành động điều khiển PI.",
      "As far as the integral rate setting is concerned, a small capacitance "
      "allows a higher integral rate, while transfer lag and dead time require "
      "a lower integral rate. A higher integral rate counteracts the offset more "
      "quickly, whereas a lower integral rate avoids excessive cycling of the "
      "process variable. Figure 6.14 shows a detailed graph of PI control action.")
    FIG(b, 14, F.fig_f14(), lang)

    P(b, lang,
      "Giới hạn của điều khiển PI là chu kỳ dao động lớn, do đó đáp ứng chậm "
      "khi độ trễ đáng kể. Nếu thiết bị đo nhạy, độ trễ truyền không phải là "
      "giới hạn; ngược lại, nếu thiết bị đo chậm, độ trễ truyền sẽ chuyển "
      "thành độ trễ.",
      "The limitation of PI control is a large period of cycling and hence a "
      "slow response with appreciable dead time. If the measuring device is "
      "sensitive, transfer lag is not a limitation; if, on the other hand, the "
      "measuring device is sluggish, transfer lag is converted into dead time.")

    P(b, lang,
      "Hình 6.15 cho thấy cách thực hiện điện tử của điều khiển PI, thực chất "
      "là sự biến đổi nhẹ so với sơ đồ trên Hình 6.8. Rp và Ri lần lượt là "
      "chiết áp chỉnh dải tỷ lệ và chỉnh tốc độ tích phân. Dải tỷ lệ đưa phản "
      "hồi âm vào để ổn định hệ thống, còn tốc độ tích phân tạo phản hồi dương "
      "trễ để bù tác động của phản hồi âm và thu hẹp dải tỷ lệ nhằm loại bỏ độ "
      "lệch.",
      "Figure 6.15 shows the electronic implementation of PI control, which is "
      "actually a slight modification of the diagram given in Figure 6.8. Rp "
      "and Ri are the proportional band and integral rate adjustments "
      "respectively. The proportional band introduces negative feedback to "
      "stabilize the system, while the integral rate provides a delayed positive "
      "feedback to compensate the effect of the negative feedback and reduces "
      "the proportional band in order to remove the offset.")
    FIG(b, 15, F.fig_f15(), lang)

    P(b, lang,
      "Cách thực hiện khí nén của hành động PI đã được trình bày trên Hình "
      "6.10 trong thảo luận trước đó. Trong thực tế, giới hạn cho hành động "
      "tích phân thể hiện ở đây được tạo bằng một van kim nhỏ, thân van được "
      "dùng để chỉnh tốc độ trong cách thực hiện khí nén.",
      "The pneumatic implementation of PI action was shown in Figure 6.10 "
      "during the earlier discussion. In practice the restriction for integral "
      "action shown there is provided by a small needle valve, whose stem is "
      "used for rate adjustment in the pneumatic implementation.")

    return b
