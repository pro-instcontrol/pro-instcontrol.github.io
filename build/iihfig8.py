# -*- coding: utf-8 -*-
"""Vector figures for Chapter 8 "Control Valves" of 3G E-learning,
*Illustrated Handbook of Industrial Instrumentation and Control* (2018),
PDF pp. 303-344 (printed pp. 289-330).

The eight source items are schematics, cut-away photographs and a curve
chart with short captions (only the first three are captioned in the
source).  They are redrawn here as simplified bilingual vector figures.
Every function returns the standard 5-tuple
``(svg, caption_vi, caption_en, aria_vi, aria_en)`` through ``_finish()``.
All SVG text is XML-escaped with ``esc()`` and kept romanized (unaccented)
Vietnamese; the bilingual captions use full Vietnamese diacritics.
Source figure order 1 through 8 is preserved.
"""
import math
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from vfig import (BLUE, GREEN, GREY, INK, RED,  # noqa: E402
                  _arrow, _circle, _defs, _ellipse, _fig, _line, _path, _poly,
                  _rect, _txt, svg)

FIGS = {}


def _reg(f):
    figs = f()
    FIGS[f.__name__] = figs
    return f


def esc(s):
    """Escape SVG text while preserving entities already present in the data."""
    s = str(s)
    s = re.sub(r"\x26(?!amp;|lt;|gt;|quot;|apos;|#\d+;)", "&amp;", s)
    return s.replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")


def T(x, y, s, size=8.5, **kw):
    """XML-safe text label."""
    return _txt(x, y, esc(s), size=size, **kw)


def _bl(x, y, vi, en, size=7.4, color=INK, anchor="start", dy=11):
    """Two-line bilingual label (Vietnamese over English)."""
    return (T(x, y, vi, size, color=color, anchor=anchor)
            + T(x, y + dy, en, size - 0.7, color=GREY, anchor=anchor))


def _num(cx, cy, n):
    """A numbered callout bubble."""
    return (_circle(cx, cy, 8, fill="#fdf3e6", sw=1.1, color=INK)
            + T(cx, cy + 3, str(n), 8.0, color=INK, weight="600"))


def _legend(items, x, y, lh=15, size=7.6):
    """Numbered parts list rendered as plain text lines."""
    return "".join(T(x, y + i * lh, "%d. %s" % (i + 1, lab), size,
                     anchor="start") for i, lab in enumerate(items))


def _callouts(items):
    """Draw connector lines and numbered bubbles from (lx,ly) to (tx,ty)."""
    o = []
    for i, (lx, ly, tx, ty) in enumerate(items):
        o.append(_line(lx, ly, tx, ty, sw=0.8, color=GREY))
        dy = 12 if ly < 200 else -12
        o.append(_num(lx, ly + dy, i + 1))
    return "".join(o)


def _foot(w, y, text):
    # Auto-shrink long bilingual notes so they stay inside the canvas.
    size = min(7.6, max(4.4, 640.0 / (len(text) * 0.52)))
    return T(w / 2.0, y, text, size, color=GREY)


def _panel(x, y, w, h, label):
    o = [_rect(x, y, w, h, fill="#fbfaf7", sw=1.3, stroke=GREY)]
    o.append(T(x + w / 2.0, y + 16, label, 8.6, color=INK, weight="600"))
    return "".join(o)


def _finish(o, w, h, title, cap_vi, cap_en, aria_vi, aria_en):
    s = svg(w, h, "".join(o), esc(title))
    return _fig(s, cap_vi, cap_en, aria_vi, aria_en)


# ---------------------------------------------------------------------------
@_reg
def fig_f01():
    """Figure 1a: distributed control with analog control calculations."""
    w, h = 680, 380
    o = [_defs()]
    o.append(T(340, 24, "Dieu khien phan tan - tinh toan tuong tu / "
                        "Distributed control with analog calculations", 8.6,
               color=INK, weight="600"))
    # Field and control-room panels.
    o.append(_panel(28, 78, 196, 244, "Truong thiet bi / Field"))
    o.append(_panel(456, 78, 196, 244, "Phong dieu khien / Control room"))
    # Field sensor and transmitter.
    o.append(_circle(70, 146, 14, fill="#eef3fb", sw=1.4))
    o.append(T(70, 150, "S", 9.0, color=BLUE, weight="600"))
    o.append(T(70, 178, "Cam bien / Sensor", 6.8, color=INK))
    o.append(_rect(120, 130, 82, 34, fill="#fdf3e6", sw=1.3))
    o.append(T(161, 143, "May phat xa", 7.0, color=INK))
    o.append(T(161, 154, "Transmitter", 6.4, color=GREY))
    o.append(_arrow(84, 146, 120, 146, sw=1.3, color=BLUE))
    # Field actuator and valve.
    o.append(_rect(120, 236, 82, 34, fill="#f6e6c8", sw=1.3))
    o.append(T(161, 249, "Co chap hanh", 7.0, color=INK))
    o.append(T(161, 260, "Actuator", 6.4, color=GREY))
    o.append(_poly([(56, 274), (56, 250), (104, 250), (104, 274)],
                   sw=1.4, color=INK))
    o.append(_poly([(56, 250), (104, 274)], sw=1.2, color=BLUE))
    o.append(T(80, 292, "Van / Valve", 6.8, color=INK))
    # Control-room instruments.
    o.append(_rect(486, 108, 136, 32, fill="#eef3fb", sw=1.3))
    o.append(T(554, 121, "Hien thi / Display", 7.2, color=INK))
    o.append(_rect(486, 164, 136, 40, fill="#fdf3e6", sw=1.4))
    o.append(T(554, 178, "Bo dieu khien tuong tu", 7.2, color=INK))
    o.append(T(554, 190, "Analog controller", 6.6, color=GREY))
    o.append(_rect(486, 234, 136, 32, fill="#f6e6c8", sw=1.3))
    o.append(T(554, 247, "May ghi / Recorder", 7.2, color=INK))
    # Analog signal paths.
    o.append(_arrow(202, 147, 486, 147, sw=1.8, color=BLUE))
    o.append(T(344, 138, "Tin hieu do 4-20 mA / 4-20 mA signal", 7.0,
               color=BLUE))
    o.append(_path("M554,204 L554,282 L202,282", sw=1.8, color=GREEN))
    o.append(_arrow(230, 282, 202, 282, sw=1.8, color=GREEN))
    o.append(T(344, 300, "Tin hieu dieu khien 4-20 mA / 4-20 mA control",
               7.0, color=GREEN))
    o.append(_arrow(554, 140, 554, 164, sw=1.2, color=GREY))
    o.append(_arrow(554, 204, 554, 234, sw=1.2, color=GREY))
    o.append(_foot(680, 344, "Gia tri bien do duoc truyen bang dong dien tuong tu; "
                             "phep tinh toan va hien thi tap trung tai phong dieu khien / "
                             "Measured values travel as analog currents; calculations and displays are centralized"))
    o.append(_foot(680, 366, "Tin hieu dieu khien quay tro lai van de thay doi vi tri than van va luong chay / "
                             "The control signal returns to the valve to change stem position and flow rate"))
    return _finish(o, w, h, "Distributed control with analog calculations",
        "Hình 8.1 · Điều khiển phân tán với các phép tính điều khiển tương tự: tín hiệu đo 4–20 mA từ cảm biến và "
        "máy phát đi tới phòng điều khiển trung tâm, nơi bộ điều khiển tương tự và máy ghi xử lý; tín hiệu điều "
        "khiển sau đó quay lại bộ chấp hành và van tại hiện trường.",
        "Figure 8.1 · Distributed control with analog control calculations: a 4–20 mA measurement signal travels "
        "from the field sensor and transmitter to the central control room, where an analog controller and "
        "recorder process it; the control signal then returns to the actuator and valve in the field.",
        "Sơ đồ điều khiển phân tán dùng tín hiệu tương tự 4 đến 20 mA",
        "Distributed control schematic using analog 4 to 20 mA signals")


# ---------------------------------------------------------------------------
@_reg
def fig_f02():
    """Figure 1b: distributed control with digital control calculations."""
    w, h = 680, 380
    o = [_defs()]
    o.append(T(340, 24, "Dieu khien phan tan - tinh toan so / "
                        "Distributed control with digital calculations", 8.6,
               color=INK, weight="600"))
    o.append(_panel(28, 78, 196, 244, "Truong thiet bi / Field"))
    o.append(_panel(456, 78, 196, 244, "Phong dieu khien / Control room"))
    # Smart field transmitter.
    o.append(_circle(70, 146, 14, fill="#eef3fb", sw=1.4))
    o.append(T(70, 150, "S", 9.0, color=BLUE, weight="600"))
    o.append(T(70, 178, "Cam bien / Sensor", 6.8, color=INK))
    o.append(_rect(120, 130, 82, 34, fill="#fdf3e6", sw=1.3))
    o.append(T(161, 143, "Phat xa thong minh", 6.6, color=INK))
    o.append(T(161, 154, "Smart transmitter", 6.4, color=GREY))
    o.append(_arrow(84, 146, 120, 146, sw=1.3, color=BLUE))
    # Smart actuator and valve.
    o.append(_rect(120, 236, 82, 34, fill="#f6e6c8", sw=1.3))
    o.append(T(161, 249, "Co chap hanh so", 6.8, color=INK))
    o.append(T(161, 260, "Smart actuator", 6.4, color=GREY))
    o.append(_poly([(56, 274), (56, 250), (104, 250), (104, 274)],
                   sw=1.4, color=INK))
    o.append(_poly([(56, 250), (104, 274)], sw=1.2, color=BLUE))
    o.append(T(80, 292, "Van / Valve", 6.8, color=INK))
    # Digital control-room instruments.
    o.append(_rect(486, 108, 136, 32, fill="#eef3fb", sw=1.3))
    o.append(T(554, 121, "Hien thi / Display", 7.2, color=INK))
    o.append(_rect(486, 164, 136, 40, fill="#fdf3e6", sw=1.4))
    o.append(T(554, 178, "Bo dieu khien so", 7.2, color=INK))
    o.append(T(554, 190, "Digital controller", 6.6, color=GREY))
    o.append(_rect(486, 234, 136, 32, fill="#f6e6c8", sw=1.3))
    o.append(T(554, 247, "Luu tru / Database", 7.2, color=INK))
    # Two-way digital communication bus.
    o.append(_arrow(202, 143, 486, 143, sw=1.7, color=BLUE))
    o.append(_arrow(486, 152, 202, 152, sw=1.4, color=GREEN, dash="5 3"))
    o.append(T(344, 133, "Truyen thong so / Digital bus", 7.0, color=BLUE))
    o.append(T(344, 167, "HART / Fieldbus / Modbus", 6.6, color=GREY))
    o.append(_path("M554,204 L554,282 L202,282", sw=1.8, color=GREEN))
    o.append(_arrow(230, 282, 202, 282, sw=1.8, color=GREEN))
    o.append(T(344, 300, "Lenh so den co chap hanh / Digital command to actuator",
               6.8, color=GREEN))
    o.append(_arrow(554, 140, 554, 164, sw=1.2, color=GREY))
    o.append(_arrow(554, 204, 554, 234, sw=1.2, color=GREY))
    o.append(_foot(680, 344, "Bo vi xu ly thuc hien phep tinh toan dieu khien; tin hieu so cho phep truyen "
                             "hai chieu va chuan doa cao / A microprocessor performs the control calculation "
                             "and digital signals allow two-way, high-accuracy communication"))
    o.append(_foot(680, 366, "May phat xa thong minh va co chap hanh so trao doi du lieu tren cung mot duong "
                             "truyen / Smart transmitters and smart actuators exchange data over one wire"))
    return _finish(o, w, h, "Distributed control with digital calculations",
        "Hình 8.2 · Điều khiển phân tán với các phép tính điều khiển số: máy phát thông minh gửi giá trị đo tới "
        "bộ điều khiển số qua đường truyền kỹ thuật số hai chiều (HART, Fieldbus). Bộ vi xử lý tính toán và gửi "
        "lệnh tới cơ chấp hành thông minh để định vị van.",
        "Figure 8.2 · Distributed control with digital control calculations: a smart transmitter sends measured "
        "values to a digital controller over a two-way digital bus (HART, Fieldbus). The microprocessor computes "
        "the output and sends a digital command to the smart actuator to position the valve.",
        "Sơ đồ điều khiển phân tán dùng truyền thông số hai chiều",
        "Distributed control schematic using two-way digital communication")


# ---------------------------------------------------------------------------
@_reg
def fig_f03():
    """Figure 2: key elements required for monitoring and control."""
    w, h = 680, 400
    o = [_defs()]
    o.append(T(340, 24, "Cac phan tu chinh cua vong dieu khien / "
                        "Key elements of a monitoring and control loop", 8.6,
               color=INK, weight="600"))
    o.append(_panel(24, 110, 116, 96, "Qua trinh / Process"))
    o.append(_panel(158, 110, 116, 96, "Phat xa / Transmitter"))
    o.append(_panel(292, 110, 116, 96, "Dieu khien / Controller"))
    o.append(_panel(426, 110, 116, 96, "Chuyen doi / I-P"))
    o.append(_panel(560, 110, 96, 96, "Van / Valve"))
    # Process vessel and sensor.
    o.append(_rect(48, 150, 68, 38, fill="#eef3fb", sw=1.3))
    o.append(_line(48, 164, 116, 164, sw=1.2, color=BLUE))
    o.append(_line(82, 150, 82, 140, sw=1.3, color=INK))
    o.append(T(82, 196, "Cam bien / Sensor", 6.4, color=INK))
    # Transmitter output.
    o.append(_rect(176, 146, 80, 36, fill="#fdf3e6", sw=1.3))
    o.append(T(216, 162, "4-20 mA", 7.4, color=INK, weight="600"))
    o.append(T(216, 175, "tin hieu / signal", 6.4, color=GREY))
    # Controller computation.
    o.append(_rect(310, 146, 80, 36, fill="#eef3fb", sw=1.3))
    o.append(T(350, 162, "Tinh toan / Compute", 6.8, color=INK))
    o.append(T(350, 175, "PID", 7.0, color=BLUE, weight="600"))
    # Current-to-pressure converter.
    o.append(_rect(444, 146, 80, 36, fill="#f6e6c8", sw=1.3))
    o.append(T(484, 162, "3-15 PSI", 7.4, color=INK, weight="600"))
    o.append(T(484, 175, "khi / air", 6.4, color=GREY))
    # Pneumatic actuator and valve.
    o.append(_circle(608, 150, 12, fill="#eef3fb", sw=1.4))
    o.append(T(608, 154, "A", 8.0, color=BLUE, weight="600"))
    o.append(_line(608, 162, 608, 178, sw=1.5, color=INK))
    o.append(_poly([(590, 178), (608, 190), (626, 178), (608, 190)],
                   sw=1.4, color=INK))
    # Forward signal path.
    for x1, x2 in ((140, 158), (274, 292), (408, 426), (542, 560)):
        o.append(_arrow(x1, 158, x2, 158, sw=1.6, color=BLUE))
    o.append(T(149, 98, "do luong / PV", 6.6, color=GREY))
    o.append(T(283, 98, "4-20 mA", 6.6, color=GREY))
    o.append(T(417, 98, "dieu khien / CO", 6.6, color=GREY))
    o.append(T(551, 98, "3-15 PSI / air", 6.6, color=GREY))
    # Return process line closes the loop.
    o.append(_path("M608,206 L608,270 L82,270 L82,206", sw=2.0, color=BLUE))
    o.append(_arrow(300, 270, 250, 270, sw=1.8, color=BLUE))
    o.append(T(340, 262, "Dong chay tro lai / Return flow", 7.0, color=BLUE))
    o.append(_foot(680, 330, "Gia tri do duoc chuyen thanh tin hieu 4-20 mA; bo dieu khien tinh toan va gui lenh "
                             "den final element / The measurement becomes a 4-20 mA signal and the controller "
                             "drives the final element"))
    o.append(_foot(680, 354, "Tai van, bo chuyen doi I/P doi dong dien thanh ap suat khi 3-15 PSI de dieu "
                             "khien co chap hanh / At the valve an I-P converter changes current to 3-15 PSI "
                             "air pressure"))
    o.append(_foot(680, 378, "Chuyen dong cua than van lam thay do do can va luong chay; dong chay quay ve qua "
                             "trinh de lap lai chu trinh / Stem motion changes resistance and flow, which "
                             "returns to the process to close the loop"))
    return _finish(o, w, h, "Key elements of a monitoring and control loop",
        "Hình 8.3 · Sơ đồ các phần tử cần thiết để giám sát và điều khiển: phép đo từ cảm biến được máy phát đổi "
        "thành tín hiệu 4–20 mA, bộ điều khiển tính toán đầu ra và gửi tới cơ chấp hành. Tại van, bộ chuyển đổi "
        "I/P đổi dòng điện thành áp suất khí 3–15 PSI để dịch chuyển thân van và điều tiết lưu lượng.",
        "Figure 8.3 · Schematic of the key elements required for monitoring and control: a sensor measurement is "
        "converted by the transmitter to a 4–20 mA signal, and the controller computes an output for the final "
        "element. At the valve an I/P converter changes current into 3–15 PSI air pressure to move the stem and "
        "throttle the flow.",
        "Sơ đồ vòng đo và điều khiển gồm cảm biến, máy phát, bộ điều khiển và van",
        "Control loop schematic with sensor, transmitter, controller and valve")


# ---------------------------------------------------------------------------
@_reg
def fig_f04():
    """Cut-away globe valve body in three positions (source photographs)."""
    w, h = 680, 380
    o = [_defs()]
    o.append(T(340, 24, "Than van cau mat cat - ba vi tri / "
                        "Cut-away globe valve body - three positions", 8.6,
               color=INK, weight="600"))
    stages = ((125, "Dong / Closed", 156),
              (340, "Mo mot nua / Half open", 144),
              (555, "Mo toan / Fully open", 128))
    for cx, label, py in stages:
        o.append(_panel(cx - 104, 70, 208, 236, label))
        # Inlet and outlet stubs.
        o.append(_rect(cx - 98, 152, 28, 26, fill="#eef3fb", sw=1.4))
        o.append(_rect(cx + 70, 152, 28, 26, fill="#eef3fb", sw=1.4))
        # Valve body and flow channel.
        o.append(_rect(cx - 72, 130, 144, 86, fill="#fbfaf7", sw=1.6,
                       stroke=GREY))
        o.append(_poly([(cx - 98, 165), (cx - 26, 165), (cx - 26, 158),
                        (cx + 26, 158), (cx + 26, 165), (cx + 98, 165)],
                       sw=1.8, color=BLUE))
        # Seat ring with central port.
        o.append(_line(cx - 28, 158, cx - 11, 158, sw=2.6, color=INK))
        o.append(_line(cx + 11, 158, cx + 28, 158, sw=2.6, color=INK))
        # Bonnet, stem, handwheel and guided plug.
        o.append(_rect(cx - 22, 104, 44, 36, fill="#fbfaf7", sw=1.3,
                       stroke=GREY))
        o.append(_line(cx, 106, cx, py, sw=2.0, color=INK))
        o.append(_ellipse(cx, 104, 20, 5, fill="#eef3fb", sw=1.4))
        o.append(_poly([(cx - 18, py), (cx + 18, py), (cx + 11, py + 14),
                        (cx - 11, py + 14)], fill="#f6e6c8", sw=1.4,
                       color=INK, close=True))
        if label.startswith("Dong"):
            o.append(_arrow(cx - 76, 165, cx - 40, 165, sw=1.2, color=BLUE))
        else:
            o.append(_arrow(cx - 76, 165, cx - 40, 165, sw=1.6, color=BLUE))
            o.append(_arrow(cx + 40, 165, cx + 76, 165, sw=1.6, color=BLUE))
        o.append(T(cx, 236, "Nut va ghe / Plug and seat", 6.6, color=GREY))
    o.append(_legend(["Than van / Body", "Nut dan bang than / Stem-guided plug",
                      "Ghe va cong / Seat and port"], 48, 326, lh=14, size=7.0))
    o.append(_foot(680, 366, "Nut van luon thang hang voi tam ghe vi no duoc dan bang than: kieu nay goi la van "
                             "cau dan bang than / The plug stays aligned with the seat because the stem guides "
                             "it, hence the name stem-guided globe valve"))
    return _finish(o, w, h, "Cut-away globe valve body in three positions",
        "Hình 8.4 · Ảnh cắt bỏ thân van cầu dạng điều khiển ở ba vị trí: đóng hoàn toàn, mở một nửa và mở hoàn "
        "toàn. Nút van được thân dẫn hướng nên luôn thẳng hàng với tâm ghe; khoảng cách giữa nút và ghe quyết "
        "định mức độ tiết lưu.",
        "Figure 8.4 · A cut-away globe valve body in three positions: fully closed, half open and fully open. "
        "The plug is guided by the stem so it always aligns with the seat centreline; the gap between plug and "
        "seat sets the degree of throttling.",
        "Ảnh cắt bỏ thân van cầu ở ba vị trí đóng, mở một nửa và mở hoàn toàn",
        "Cut-away globe valve shown closed, half open and fully open")


# ---------------------------------------------------------------------------
@_reg
def fig_f05():
    """Needle valve in three positions (source photographs)."""
    w, h = 680, 380
    o = [_defs()]
    o.append(T(340, 24, "Van kim - ba vi tri / Needle valve - three positions",
               8.6, color=INK, weight="600"))
    stages = ((125, "Dong / Closed", 140),
              (340, "Mo mot nua / Mid-open", 132),
              (555, "Mo toan / Fully open", 120))
    for cx, label, py in stages:
        o.append(_panel(cx - 104, 70, 208, 236, label))
        o.append(_rect(cx - 98, 152, 28, 26, fill="#eef3fb", sw=1.4))
        o.append(_rect(cx + 70, 152, 28, 26, fill="#eef3fb", sw=1.4))
        o.append(_rect(cx - 72, 130, 144, 86, fill="#fbfaf7", sw=1.6,
                       stroke=GREY))
        o.append(_poly([(cx - 98, 165), (cx - 14, 165), (cx - 14, 158),
                        (cx + 14, 158), (cx + 14, 165), (cx + 98, 165)],
                       sw=1.8, color=BLUE))
        # Seat hole: a small V-shaped ring.
        o.append(_poly([(cx - 12, 157), (cx - 5, 175), (cx + 5, 175),
                        (cx + 12, 157)], sw=1.6, color=INK))
        o.append(_rect(cx - 18, 104, 36, 34, fill="#fbfaf7", sw=1.3,
                       stroke=GREY))
        o.append(_line(cx, 106, cx, py, sw=1.8, color=INK))
        o.append(_ellipse(cx, 104, 18, 5, fill="#eef3fb", sw=1.4))
        # Tapered needle with its tip at the seat.
        o.append(_poly([(cx - 8, py), (cx + 8, py), (cx, py + 30)],
                       fill="#f6e6c8", sw=1.4, color=RED, close=True))
        if label.startswith("Dong"):
            o.append(_arrow(cx - 76, 165, cx - 30, 165, sw=1.0, color=BLUE))
        else:
            o.append(_arrow(cx - 76, 165, cx - 30, 165, sw=1.6, color=BLUE))
            o.append(_arrow(cx + 30, 165, cx + 76, 165, sw=1.6, color=BLUE))
        o.append(T(cx, 236, "Kim nho / Fine needle", 6.6, color=GREY))
    o.append(_legend(["Than van / Body", "Kim / Needle", "Lo ghe / Seat hole"],
                     48, 326, lh=14, size=7.0))
    o.append(_foot(680, 366, "Van kim la bien doi cua van cau: nut rat nho va lop vao lo ghe, dung dieu chinh "
                             "luong chat long hoa khi nho bang tay / A needle valve varies a globe valve with "
                             "a very small plug that fits the seat, used for manual low-flow control of air or oil"))
    return _finish(o, w, h, "Needle valve in three positions",
        "Hình 8.5 · Van kim ở ba vị trí từ trái sang phải: đóng hoàn toàn, mở một nửa và mở hoàn toàn. Nút hình "
        "kim nhỏ lọt sâu vào lỗ ghe, thích hợp điều chỉnh bằng tay các lưu lượng nhỏ của không khí hoặc dầu.",
        "Figure 8.5 · A needle valve in three positions from left to right: fully closed, mid-open and fully "
        "open. Its very small tapered plug fits down into the seat hole, making it suitable for manual control "
        "of low flow rates of air or oil.",
        "Van kim ở ba vị trí đóng, mở một nửa và mở hoàn toàn",
        "Needle valve shown closed, mid-open and fully open")


# ---------------------------------------------------------------------------
@_reg
def fig_f06():
    """Characterized ball valve in successive stages of opening."""
    w, h = 680, 380
    o = [_defs()]
    o.append(T(340, 24, "Van bong co khe V - cac giai doan mo / "
                        "V-notch ball valve - stages of opening", 8.6,
               color=INK, weight="600"))
    stages = ((92, "Dong 0% / Closed", 90),
              (264, "Mo 30% / Open", 58),
              (436, "Mo 60% / Open", 32),
              (608, "Mo 90% / Open", 4))
    for cx, label, deg in stages:
        o.append(_panel(cx - 80, 70, 160, 236, label))
        o.append(_rect(cx - 74, 148, 24, 26, fill="#eef3fb", sw=1.4))
        o.append(_rect(cx + 50, 148, 24, 26, fill="#eef3fb", sw=1.4))
        o.append(_rect(cx - 56, 128, 112, 84, fill="#fbfaf7", sw=1.6,
                       stroke=GREY))
        o.append(_circle(cx, 170, 32, fill="#eef3fb", sw=1.6))
        # Rotated through-bore of the ball.
        a = math.radians(deg)
        pts = []
        for dx, dy in ((-30, -7), (30, -7), (30, 7), (-30, 7)):
            px = cx + dx * math.cos(a) - dy * math.sin(a)
            py = 170 + dx * math.sin(a) + dy * math.cos(a)
            pts.append((px, py))
        o.append(_poly(pts, fill="#ffffff", sw=1.4, color=BLUE, close=True))
        # Shaft and handle above the ball.
        o.append(_line(cx, 138, cx, 104, sw=1.6, color=INK))
        o.append(_ellipse(cx, 104, 17, 4, fill="#eef3fb", sw=1.3))
        o.append(_line(cx - 20 * math.cos(a), 104 - 6 * math.sin(a),
                       cx + 20 * math.cos(a), 104 + 6 * math.sin(a),
                       sw=1.8, color=INK))
        if deg >= 58:
            o.append(_arrow(cx - 72, 161, cx - 42, 161, sw=1.3, color=BLUE))
        if deg <= 32:
            o.append(_arrow(cx + 42, 161, cx + 72, 161, sw=1.6, color=BLUE))
        o.append(T(cx, 236, "Luong chay / Flow", 6.6, color=GREY))
    o.append(_legend(["Than van / Body", "Bong co lo / Bored ball",
                      "Khe V / V-notch"], 48, 326, lh=14, size=7.0))
    o.append(_foot(680, 366, "Khe V o mep lo cho dien tich chay nho khi mo it, dieu khien chinh xac hon van "
                             "bong lo tron; van bong lo day thich hop cho dong/ngat / The V-notch gives a "
                             "small flow area at low angles and finer control than a full-bore ball valve"))
    return _finish(o, w, h, "V-notch ball valve in stages of opening",
        "Hình 8.6 · Van bi định hình có khe V ở các giai đoạn mở liên tiếp, từ gần đóng tới gần mở hoàn toàn. "
        "Khe V tạo diện tích dòng chảy nhỏ khi góc mở thấp, cho khả năng tiết lưu chính xác hơn van bi lỗ tròn "
        "thường dùng cho đóng/ngắt.",
        "Figure 8.6 · A characterized ball valve with a V-notch shown in successive stages of opening, from "
        "nearly closed to nearly wide open. The notch narrows the flow area at low opening angles and gives "
        "more precise throttling than a plain full-bore ball valve suited to on/off service.",
        "Van bi có khe V ở các giai đoạn mở khác nhau",
        "V-notch ball valve at successive stages of opening")


# ---------------------------------------------------------------------------
@_reg
def fig_f07():
    """Six inherent control valve flow characteristics (source chart)."""
    w, h = 680, 400
    o = [_defs()]
    o.append(T(340, 24, "Dac tinh dong chay von co cua van dieu khien / "
                        "Inherent control valve flow characteristics", 8.4,
               color=INK, weight="600"))
    x0, y0, gw, gh = 80, 70, 400, 250
    o.append(_poly([(x0, y0), (x0, y0 + gh), (x0 + gw, y0 + gh),
                    (x0 + gw, y0)], sw=1.2, color=GREY))
    for v in (0.25, 0.5, 0.75):
        o.append(_line(x0 + v * gw, y0, x0 + v * gw, y0 + gh,
                       sw=0.6, color="#d8d8d8"))
        o.append(_line(x0, y0 + gh - v * gh, x0 + gw, y0 + gh - v * gh,
                       sw=0.6, color="#d8d8d8"))
    o.append(_arrow(x0, y0 + gh, x0 + gw + 12, y0 + gh, sw=1.1))
    o.append(_arrow(x0, y0 + gh, x0, y0 - 10, sw=1.1))
    o.append(T(x0 + gw, y0 - 16, "Mo van % / Stem opening %", 7.4,
               anchor="end", color=GREY))
    o.append(T(x0 + 5, y0 - 14, "Luong chay % / Flow %", 7.6,
               anchor="start", color=GREY))
    for v, lab in ((0, "0"), (0.25, "25"), (0.5, "50"), (0.75, "75"),
                   (1, "100")):
        o.append(T(x0 + v * gw, y0 + gh + 13, lab, 6.8, color=GREY))
        o.append(T(x0 - 6, y0 + gh - v * gh + 2.4, lab, 6.8,
                   anchor="end", color=GREY))
    # Six curves plotted from their governing relations.
    curves = (
        (lambda t: t ** 0.5, RED, ""),
        (lambda t: t, BLUE, ""),
        (lambda t: 0.3 * t + 0.7 * t * t, GREEN, ""),
        (lambda t: (50 ** t - 1.0) / 49.0, INK, ""),
        (lambda t: math.log(1 + 9 * t) / math.log(10), RED, "4 3"),
        (lambda t: t ** 3, GREY, "4 3"),
    )
    for fn, col, dash in curves:
        pts = []
        for i in range(121):
            t = i / 120.0
            pts.append((x0 + t * gw, y0 + gh - fn(t) * gh))
        o.append(_poly(pts, sw=1.7, color=col, dash=dash))
    o.append(_legend(["Mo nhanh / Quick opening", "Tuyen tinh / Linear",
                      "Parabol chinh sua / Modified parabolic",
                      "Ty le bang / Equal percentage",
                      "Ban log / Semi-log", "Bac ba / Cubic"],
                     490, 86, lh=32, size=6.8))
    o.append(_foot(680, 360, "Bieu do luc luong chay 0 den 100 phan tram theo do mo than van, gia dinh ap suat "
                             "khong doi; ba dac tinh thong dung la tuyen tinh, ty le bang va parabol chinh sua / "
                             "Flow versus stem travel at constant pressure drop; the three most common are "
                             "linear, equal percentage and modified parabolic"))
    o.append(_foot(680, 384, "Ty le bang tang nhanh o cuoi hanh trinh, phu hop hoi; tuyen tinh phu hop nuoc / "
                             "Equal percentage rises steeply near full travel and suits steam service"))
    return _finish(o, w, h, "Inherent control valve flow characteristics",
        "Hình 8.7 · Đồ thị sáu đặc tính dòng chảy vốn có của van điều khiển: phần trăm lưu lượng theo phần trăm độ "
        "mở thân van với giả thiết áp suất giảm không đổi. Ba đặc tính thường dùng là tuyến tính, tỷ lệ bằng và "
        "parabol chỉnh sửa; tỷ lệ bằng hợp hơi, tuyến tính hợp nước.",
        "Figure 8.7 · Graph of six inherent control valve flow characteristics: flow percentage versus stem "
        "opening at constant pressure drop. The three most common are linear, equal percentage and modified "
        "parabolic; equal percentage suits steam and linear suits water systems.",
        "Đồ thị sáu đặc tính dòng chảy vốn có của van điều khiển",
        "Chart of six inherent control valve flow characteristics")


# ---------------------------------------------------------------------------
@_reg
def fig_f08():
    """Fisher E-plug control valve body with the disk partly open."""
    w, h = 680, 380
    o = [_defs()]
    o.append(T(340, 24, "Van Fisher E-plug voi dia mo mot phan / "
                        "Fisher E-plug valve with disk partly open", 8.6,
               color=INK, weight="600"))
    # Body, flanges and flow passage.
    o.append(_rect(40, 166, 60, 48, fill="#eef3fb", sw=1.5))
    o.append(_rect(380, 166, 60, 48, fill="#eef3fb", sw=1.5))
    o.append(_ellipse(240, 190, 120, 96, fill="#fbfaf7", sw=1.8,
                      color=GREY))
    o.append(_poly([(100, 190), (170, 190)], sw=3.0, color=BLUE))
    o.append(_poly([(310, 190), (380, 190)], sw=3.0, color=BLUE))
    # Seat ring and shaft.
    o.append(_ellipse(240, 190, 40, 58, fill="none", sw=2.2, color=INK))
    o.append(_line(240, 96, 240, 284, sw=1.5, color=INK, dash="4 3"))
    # Eccentric disk, rotated to show the partly open position.
    a = math.radians(38)
    pts = []
    for dx, dy in ((-52, -7), (52, -7), (52, 7), (-52, 7)):
        px = 240 + dx * math.cos(a) - dy * math.sin(a)
        py = 190 + dx * math.sin(a) + dy * math.cos(a)
        pts.append((px, py))
    o.append(_poly(pts, fill="#f6e6c8", sw=1.8, color=RED, close=True))
    o.append(_circle(240, 190, 6, fill="#eef3fb", sw=1.3))
    # Cam-action indicator and caption.
    o.append(_arrow(196, 150, 284, 150, sw=1.3, color=GREEN))
    o.append(T(240, 314, "Dia mo mot phan / Disk partly open", 7.0,
               color=INK))
    o.append(_callouts([(600, 120, 330, 140),
                        (600, 162, 282, 176),
                        (600, 204, 240, 244),
                        (600, 246, 268, 156),
                        (600, 288, 240, 116)]))
    o.append(_legend(["Than van / Body", "Dia lech / Eccentric disk",
                      "Ghe / Seat", "Tac dong cam / Cam action",
                      "Truc quay / Shaft"], 470, 108, lh=30, size=7.0))
    o.append(_foot(680, 344, "Tam dia lech khoi tam truc nen dia cham ghe voi tac dong cam, tao ap luc ep "
                             "lon / The disk centre is offset from the shaft so the disk meets the seat with "
                             "cam action and high seating pressure"))
    o.append(_foot(680, 366, "Nho vay co the dong kin bang ghe kim loai ma khong can lot mem, van van hanh tot "
                             "trong dich vu tiet luu / This permits tight metal-to-metal shut-off without a "
                             "soft lining, even in throttling service"))
    return _finish(o, w, h, "Fisher E-plug valve with disk partly open",
        "Hình 8.8 · Thân van Fisher E-plug với đĩa mở một phần. Tâm đĩa lệch khỏi trục quay nên đĩa tiếp cận ghe "
        "theo chuyển động cam, tạo áp lực ép lớn; nhờ đó đóng kín được bằng ghe kim loại mà không cần đệm mềm.",
        "Figure 8.8 · The body of a Fisher E-plug control valve with the disk partly open. The disk centre is "
        "offset from the shaft centreline, so the disk approaches the seat with a cam action that produces high "
        "seating pressure and tight metal-seat shut-off without a soft lining.",
        "Thân van Fisher E-plug có đĩa lệch mở một phần",
        "Fisher E-plug valve body with partly open eccentric disk")
