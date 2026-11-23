# -*- coding: utf-8 -*-
"""Vector figures for Chapter 7 "Gas and Liquid Sampling Techniques in
Process Industry" of 3G E-learning, *Illustrated Handbook of Industrial
Instrumentation and Control* (2018), PDF pp. 257-302 (printed pp. 243-288).

The nineteen source figures are photographs, line drawings and process
charts with short numbered captions.  They are redrawn here as simplified
bilingual vector schematics.  Every function returns the standard 5-tuple
``(svg, caption_vi, caption_en, aria_vi, aria_en)`` through ``_finish()``.
All SVG text is XML-escaped with ``esc()`` and kept romanized (unaccented)
Vietnamese; the bilingual captions use full Vietnamese diacritics.  Source
figure order 1 through 19 is preserved.
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
    """Gas chromatograph (source Figure 1)."""
    w, h = 680, 380
    o = [_defs()]
    o.append(T(340, 24, "May sac khi / Gas chromatograph", 9.0,
               color=INK, weight="600"))
    # Carrier-gas cylinder and regulator.
    o.append(_rect(44, 116, 32, 80, fill="#eef3fb", sw=1.6))
    o.append(_ellipse(60, 116, 16, 6, fill="#dbe4ea", sw=1.2))
    o.append(T(60, 104, "Khi mang / Carrier gas", 7.0, color=BLUE))
    o.append(_rect(92, 140, 44, 32, fill="#f6e6c8", sw=1.2))
    o.append(_circle(114, 156, 8, fill="#fdf3e6", sw=1.0))
    # Injection port with septum.
    o.append(_rect(158, 140, 62, 32, fill="#fdf3e6", sw=1.4))
    o.append(_line(170, 140, 170, 172, sw=1.0, color=GREY))
    o.append(T(189, 128, "Tiem mau / Injector", 6.8, color=INK))
    # Oven with a coiled packed or capillary column.
    o.append(_rect(238, 112, 182, 88, fill="#fbfaf7", sw=1.4, stroke=GREY))
    o.append(_poly([(258, 150), (276, 138), (294, 162), (312, 138),
                    (330, 162), (348, 138), (366, 162), (384, 138),
                    (402, 150)], sw=1.6, color=BLUE))
    o.append(T(329, 104, "Cot trong lo / Column in oven", 7.0, color=BLUE))
    # Detector and chart recorder.
    o.append(_rect(438, 140, 72, 32, fill="#f6e6c8", sw=1.4))
    o.append(T(474, 128, "May do / Detector", 6.8, color=INK))
    o.append(_rect(528, 128, 108, 56, fill="#fbfaf7", sw=1.4))
    o.append(_poly([(538, 170), (556, 170), (562, 146), (568, 170),
                    (582, 170), (590, 152), (598, 170), (628, 170)],
                   sw=1.4, color=RED))
    o.append(T(582, 116, "May ghi / Recorder", 6.8, color=INK))
    # Flow path.
    o.append(_arrow(88, 156, 158, 156, sw=1.8, color=BLUE))
    o.append(_arrow(220, 156, 238, 156, sw=1.8, color=BLUE))
    o.append(_arrow(420, 156, 438, 156, sw=1.8, color=BLUE))
    o.append(_arrow(510, 156, 528, 156, sw=1.8, color=BLUE))
    o.append(T(329, 220, "Nhiet do cot: thoi gian rua 2-30 phut / "
                         "Column temperature sets elution in 2-30 min",
               6.8, color=GREY))
    o.append(_foot(680, 264, "Khi mang tro thanh pham qua cot; cac cau tu tach ra roi di qua detector / "
                             "Carrier gas sweeps the sample through the column and the separated compounds reach the detector"))
    o.append(_foot(680, 288, "Detector co the khong chon loc hoac chon loc; tin hieu duoc ghi thanh sac do / "
                             "Detectors may be non-selective or specific; the signal is drawn as a chromatogram"))
    o.append(_foot(680, 312, "Mau duoc tiem bang microkim qua vat lieu septum / "
                             "The sample is injected with a microsyringe through a rubber septum"))
    return _finish(o, w, h, "Gas chromatograph",
        "Hình 7.1 · Máy sắc ký khí: khí mang đi qua bộ điều chỉnh và cổng tiêm mẫu, mang mẫu vào cột đặt trong "
        "lò có nhiệt độ kiểm soát. Các cấu tử tách ra lần lượt đi tới đầu dò và tín hiệu được máy ghi thành sắc "
        "đồ; thời gian rửa giải thường từ 2 đến 30 phút.",
        "Figure 7.1 · A gas chromatograph: carrier gas passes through a regulator and an injection port, carrying "
        "the sample into a column held in a temperature-controlled oven. Separated compounds reach the detector "
        "and the signal is drawn as a chromatogram; elution times are typically 2 to 30 minutes.",
        "Sơ đồ máy sắc ký khí với cột trong lò và đầu dò",
        "Schematic of a gas chromatograph with oven column and detector")


# ---------------------------------------------------------------------------
@_reg
def fig_f02():
    """Dispersive IR analyzer (source Figure 2)."""
    w, h = 680, 380
    o = [_defs()]
    o.append(T(340, 24, "May phan tich IR tan sac / Dispersive IR analyzer", 8.8,
               color=INK, weight="600"))
    # Infrared source.
    o.append(_rect(66, 130, 46, 44, fill="#fdf3e6", sw=1.4))
    o.append(_circle(89, 152, 11, fill="#f6d9a0", sw=1.0, color=RED))
    o.append(T(89, 116, "Nguon IR / IR source", 7.0, color=RED))
    # Sample chamber.
    o.append(_rect(138, 132, 122, 40, fill="#eef3fb", sw=1.4))
    o.append(T(199, 116, "Buong mau / Sample cell", 7.0, color=BLUE))
    # Dispersive element (prism) inside a monochromator.
    o.append(_rect(286, 110, 142, 84, fill="#fbfaf7", sw=1.4, stroke=GREY))
    o.append(_poly([(306, 174), (330, 128), (354, 174)], fill="#dfeaf4",
                   sw=1.2, close=True))
    o.append(T(357, 104, "Don sac ke / Monochromator", 7.0, color=INK))
    # Detector and readout.
    o.append(_rect(456, 132, 62, 40, fill="#f6e6c8", sw=1.4))
    o.append(T(487, 116, "Dau do / Detector", 7.0, color=INK))
    o.append(_rect(544, 124, 100, 56, fill="#fbfaf7", sw=1.4))
    o.append(_line(560, 164, 628, 164, sw=1.0, color=GREY))
    o.append(T(594, 116, "Dong ho / Readout", 7.0, color=INK))
    # Optical path: white light in, separated wavelengths around the prism.
    o.append(_line(112, 152, 138, 152, sw=1.8, color=RED))
    o.append(_line(260, 152, 306, 152, sw=1.8, color=RED))
    o.append(_path("M330,152 L466,152", sw=1.4, color=GREEN))
    o.append(_path("M330,152 L466,168", sw=0.9, color=GREY, dash="4 3"))
    o.append(_path("M330,152 L466,136", sw=0.9, color=GREY, dash="4 3"))
    o.append(_line(518, 152, 544, 152, sw=1.4, color=GREEN))
    o.append(T(400, 198, "buoc song chon / selected wavelength", 6.6, color=GREEN))
    o.append(_foot(680, 248, "Phan tu hap thu buoc song dac trung; cuong do anh sang giam cho biet nong do / "
                             "Molecules absorb a characteristic wavelength; the loss of light gives the concentration"))
    o.append(_foot(680, 272, "Thiet bi tan sac dung prisma hoac cach tu de tach cac buoc song truoc khi do / "
                             "A dispersive instrument uses a prism or grating to separate wavelengths before detection"))
    o.append(_foot(680, 296, "Nguon IR duoc ngat nhip de loai bo tin hieu nen nhiet / "
                             "The IR source is chopped so that thermal background signals can be offset"))
    return _finish(o, w, h, "Dispersive IR analyzer",
        "Hình 7.2 · Máy phân tích hồng ngoại tán sắc: nguồn IR chiếu qua buồng mẫu rồi tới bộ đơn sắc chứa lăng "
        "kính. Bộ đơn sắc tách các bước sóng, chỉ bước sóng đặc trưng đi tới đầu dò và cường độ suy giảm cho "
        "biết nồng độ chất cần đo.",
        "Figure 7.2 · A dispersive infrared analyzer: an IR source shines through a sample cell into a "
        "monochromator containing a prism. The monochromator separates wavelengths, only the characteristic "
        "wavelength reaches the detector, and the attenuation gives the gas concentration.",
        "Sơ đồ máy phân tích IR tán sắc có lăng kính và đầu dò",
        "Dispersive IR analyzer with prism monochromator and detector")


# ---------------------------------------------------------------------------
@_reg
def fig_f03():
    """Non-dispersive IR technique (source Figure 3)."""
    w, h = 680, 380
    o = [_defs()]
    o.append(T(340, 24, "Ky thuat IR khong tan sac / Non-dispersive IR technique", 8.6,
               color=INK, weight="600"))
    # IR lamp feeding two parallel cells.
    o.append(_rect(46, 140, 44, 40, fill="#fdf3e6", sw=1.4))
    o.append(_circle(68, 160, 10, fill="#f6d9a0", sw=1.0, color=RED))
    o.append(T(68, 128, "Nguon IR / IR source", 7.0, color=RED))
    o.append(_rect(148, 118, 152, 36, fill="#eef3fb", sw=1.4))
    o.append(_rect(148, 182, 152, 36, fill="#fbfaf7", sw=1.4, stroke=GREY))
    o.append(T(224, 106, "Buong mau / Sample cell", 7.0, color=BLUE))
    o.append(T(224, 238, "Buong tham chieu / Reference cell (N2)", 6.8, color=GREY))
    o.append(_path("M90,160 L148,136", sw=1.4, color=RED))
    o.append(_path("M90,160 L148,200", sw=1.4, color=RED, dash="4 3"))
    # Optical filter and detector.
    o.append(_rect(330, 140, 52, 40, fill="#f6e6c8", sw=1.4))
    o.append(T(356, 128, "Loc quang / Optical filter", 7.0, color=INK))
    o.append(_rect(414, 142, 62, 36, fill="#fdf3e6", sw=1.4))
    o.append(T(445, 128, "Dau do / Detector", 7.0, color=INK))
    o.append(_rect(508, 140, 96, 40, fill="#fbfaf7", sw=1.4))
    o.append(T(556, 128, "Tin hieu / Signal", 7.0, color=INK))
    o.append(_path("M300,136 L330,152 L330,168 L300,200", sw=1.2, color=GREY))
    o.append(_line(382, 160, 414, 160, sw=1.6, color=GREEN))
    o.append(_line(476, 160, 508, 160, sw=1.6, color=GREEN))
    o.append(T(340, 202, "chi mot buoc song / one selected band only", 6.6, color=GREEN))
    o.append(_foot(680, 274, "Bo loc chi cho qua buoc song ma khi can do hap thu; cac buoc song khac bi chan / "
                             "The filter passes only the wavelength absorbed by the target gas and blocks the rest"))
    o.append(_foot(680, 298, "Nguon duoc ngat nhip de tru cac tin hieu nen nhiet va on dinh dong doc / "
                             "The source is chopped to remove thermal background and stabilise the reading"))
    o.append(_foot(680, 322, "Buong tham chieu chua khi tro; dung de so sanh voi buong mau / "
                             "The reference cell holds an inert gas for comparison with the sample cell"))
    return _finish(o, w, h, "Non-dispersive IR technique",
        "Hình 7.3 · Kỹ thuật hồng ngoại không tán sắc: chùm sáng IR đi song song qua buồng mẫu và buồng tham "
        "chiếu chứa khí trơ, sau đó qua bộ lọc quang chỉ truyền bước sóng đặc trưng tới đầu dò. Nguồn được ngắt "
        "nhịp để triệt tiêu tín hiệu nền nhiệt.",
        "Figure 7.3 · The non-dispersive infrared technique: an IR beam passes in parallel through a sample "
        "cell and a reference cell filled with inert gas, then through an optical filter that transmits only the "
        "characteristic wavelength. The source is chopped to cancel thermal background signals.",
        "Sơ đồ kỹ thuật IR không tán sắc với buồng mẫu và buồng tham chiếu",
        "NDIR layout with sample cell, reference cell and optical filter")


# ---------------------------------------------------------------------------
@_reg
def fig_f04():
    """Wheatstone bridge of the thermal conductivity detector (source Figure 4)."""
    w, h = 680, 380
    o = [_defs()]
    o.append(T(340, 24, "Cau Wheatstone cua dau do dan nhiet / "
                        "Wheatstone bridge of the thermal conductivity detector", 8.4,
               color=INK, weight="600"))
    # Diamond bridge and its four arms.
    o.append(_poly([(340, 90), (470, 190), (340, 290), (210, 190)],
                   sw=1.8, close=True))
    o.append(_line(340, 70, 340, 90, sw=1.6, color=INK))
    o.append(_line(210, 190, 160, 190, sw=1.6, color=RED))
    o.append(_line(470, 190, 520, 190, sw=1.6, color=GREY))
    for cx, cy in ((275, 140), (405, 140), (275, 240), (405, 240)):
        o.append(_rect(cx - 17, cy - 9, 34, 18, fill="#f6e6c8", sw=1.2))
    o.append(T(405, 144, "R1", 8.0, color=INK, weight="600"))
    o.append(T(405, 244, "R2", 8.0, color=INK, weight="600"))
    o.append(T(275, 244, "R3", 8.0, color=INK, weight="600"))
    o.append(T(275, 144, "R4", 8.0, color=INK, weight="600"))
    o.append(T(340, 62, "V vao / Vin", 7.0, color=INK))
    o.append(T(128, 190, "V ra / Vout", 7.0, color=RED))
    o.append(T(405, 168, "tham chieu / reference", 6.6, color=GREY))
    o.append(T(275, 168, "tham chieu / reference", 6.6, color=GREY))
    o.append(T(405, 268, "mau / sample", 6.6, color=GREY))
    o.append(T(275, 268, "mau / sample", 6.6, color=GREY))
    o.append(_foot(680, 320, "Khi ca bon dien tro bang nhau, V ra bang khong va cau duoc can bang / "
                             "When all four resistances are equal, Vout is zero and the bridge is balanced"))
    o.append(_foot(680, 344, "Khi mau chay qua mot nua cau, dien tro doi va gia tri V ra tuong ung / "
                             "Passing sample gas over half the bridge changes its resistances and Vout"))
    o.append(_foot(680, 368, "Quan he giua tin hieu va ham luong mau la phi tuyen / "
                             "The relation between signal and sample content is non-linear"))
    return _finish(o, w, h, "Wheatstone bridge of the thermal conductivity detector",
        "Hình 7.4 · Cầu Wheatstone của đầu dò dẫn nhiệt gồm bốn điện trở mắc thành hình thoi. Khi cả bốn điện trở "
        "bằng nhau (đặt khí tham chiếu), điện áp ra bằng không; khi khí mẫu chảy qua nửa cầu, điện trở thay đổi "
        "và điện áp ra tương ứng với hàm lượng khí mẫu.",
        "Figure 7.4 · The Wheatstone bridge of a thermal conductivity detector has four resistors in a diamond. "
        "With all resistances equal under reference gas the output is zero; when sample gas flows over half the "
        "bridge the resistances change and the output voltage corresponds to the sample content.",
        "Cầu Wheatstone bốn điện trở của đầu dò dẫn nhiệt",
        "Four-resistor Wheatstone bridge of a thermal conductivity detector")


# ---------------------------------------------------------------------------
@_reg
def fig_f05():
    """Cut-away view of the thermal conductivity sensor (source Figure 5)."""
    w, h = 680, 380
    o = [_defs()]
    o.append(T(340, 24, "Mat cat cam bien dan nhiet / "
                        "Cut-away view of the thermal conductivity sensor", 8.4,
               color=INK, weight="600"))
    # Sensor block, cut away to show four gas channels.
    o.append(_rect(110, 110, 460, 170, fill="#fbfaf7", sw=1.6, stroke=GREY))
    for x in (150, 370):
        o.append(_rect(x, 132, 160, 46, fill="#eef3fb", sw=1.2))
        o.append(_rect(x, 210, 160, 46, fill="#fdf3e6", sw=1.2))
        for cy in (155, 233):
            o.append(_poly([(x + 22, cy), (x + 42, cy - 8), (x + 62, cy + 8),
                            (x + 82, cy - 8), (x + 102, cy + 8), (x + 122, cy)],
                           sw=1.8, color=RED))
        o.append(_arrow(x + 10, 155, x + 52, 155, sw=1.0, color=BLUE))
        o.append(_arrow(x + 10, 233, x + 52, 233, sw=1.0, color=BLUE))
    o.append(T(230, 124, "Khi tham chieu / Reference gas", 7.0, color=BLUE))
    o.append(T(450, 124, "Khi tham chieu / Reference gas", 7.0, color=BLUE))
    o.append(T(230, 280, "Khi mau / Sample gas", 7.0, color=INK))
    o.append(T(450, 280, "Khi mau / Sample gas", 7.0, color=INK))
    o.append(T(340, 198, "Bon day dot that / Four matched filaments", 6.6, color=GREY))
    o.append(_foot(680, 308, "Hai phan tu nam trong khi tham chieu, hai phan tu nam trong khi mau / "
                             "Two elements sit in reference gas and two elements sit in the sample stream"))
    o.append(_foot(680, 332, "Dong dien khong doi chay qua cau de lam nong cac day dot / "
                             "A constant current passes through the bridge and heats the filaments"))
    o.append(_foot(680, 356, "Nhiet do va dien tro thay doi theo dan nhiet cua khi di qua / "
                             "Temperature and resistance change with the thermal conductivity of the gas"))
    return _finish(o, w, h, "Cut-away view of the thermal conductivity sensor",
        "Hình 7.5 · Mặt cắt đầu dò dẫn nhiệt dạng katharometer bốn phần tử: hai phần tử đặt trong dòng khí tham "
        "chiếu và hai phần tử đặt trong dòng khí mẫu. Dòng điện không đổi làm nóng các dây đốt; nhiệt độ và điện "
        "trở của từng dây thay đổi theo độ dẫn nhiệt của khí bao quanh.",
        "Figure 7.5 · A cut-away view of a four-element katharometer thermal conductivity sensor: two elements "
        "sit in reference gas and two in the sample gas stream. A constant current heats the filaments; their "
        "temperature and resistance follow the thermal conductivity of the surrounding gas.",
        "Mặt cắt cảm biến dẫn nhiệt bốn phần tử",
        "Cut-away of a four-element thermal conductivity sensor")


# ---------------------------------------------------------------------------
@_reg
def fig_f06():
    """Electrical diagram of the thermal conductivity sensor (source Figure 6)."""
    w, h = 680, 380
    o = [_defs()]
    o.append(T(340, 24, "So do dien cam bien dan nhiet / "
                        "Electrical diagram of the thermal conductivity sensor", 8.4,
               color=INK, weight="600"))
    # Constant-current supply and bridge diamond.
    o.append(_circle(340, 62, 14, fill="#fdf3e6", sw=1.3))
    o.append(_arrow(334, 62, 346, 62, sw=1.0, color=RED))
    o.append(T(340, 40, "Nguon dong / Constant current", 7.0, color=INK))
    o.append(_poly([(340, 96), (470, 196), (340, 296), (210, 196)],
                   sw=1.8, close=True))
    o.append(_line(340, 76, 340, 96, sw=1.6, color=INK))
    o.append(_circle(340, 196, 16, fill="#fbfaf7", sw=1.3))
    o.append(T(340, 200, "G", 9.0, color=INK, weight="600"))
    o.append(T(340, 176, "V ra / Vout", 7.0, color=RED))
    for cx, cy in ((275, 146), (405, 146), (275, 246), (405, 246)):
        o.append(_poly([(cx - 14, cy + 6), (cx - 8, cy - 6), (cx - 2, cy + 6),
                        (cx + 4, cy - 6), (cx + 10, cy + 6), (cx + 14, cy - 6)],
                       sw=1.4, color=BLUE))
    o.append(T(405, 148, "R1", 7.6, color=INK, weight="600"))
    o.append(T(275, 148, "R4", 7.6, color=INK, weight="600"))
    o.append(T(405, 248, "R2", 7.6, color=INK, weight="600"))
    o.append(T(275, 248, "R3", 7.6, color=INK, weight="600"))
    o.append(T(405, 170, "mau / sample", 6.6, color=GREY))
    o.append(T(275, 170, "mau / sample", 6.6, color=GREY))
    o.append(T(405, 270, "tham chieu / reference", 6.6, color=GREY))
    o.append(T(275, 270, "tham chieu / reference", 6.6, color=GREY))
    o.append(_foot(680, 320, "Bon day dot duoc dau noi thanh cau Wheatstone va duoc cap dong khong doi / "
                             "The four filaments are wired as a Wheatstone bridge fed by a constant current"))
    o.append(_foot(680, 344, "Khi tat ca day dot o cung mot khi, dien tro bang nhau va V ra bang khong / "
                             "With every filament in the same gas the resistances match and Vout is zero"))
    o.append(_foot(680, 368, "Khi dan nhiet khac nhau, hai day dot mat nhiet nhanh hon va cau mat can bang / "
                             "Different conductivity cools two filaments faster and unbalances the bridge"))
    return _finish(o, w, h, "Electrical diagram of the thermal conductivity sensor",
        "Hình 7.6 · Sơ đồ điện của cảm biến dẫn nhiệt: bốn dây đốt được nối thành cầu Wheatstone, cấp dòng "
        "không đổi và có đồng hồ đo điện áp ở đường chéo. Khi các dây ở cùng loại khí, cầu cân bằng và điện áp "
        "ra bằng không; khí mẫu có độ dẫn nhiệt khác làm cầu mất cân bằng.",
        "Figure 7.6 · Electrical diagram of the thermal conductivity sensor: four filaments are wired into a "
        "Wheatstone bridge fed by a constant current, with a meter across the diagonal. Identical gas balances "
        "the bridge at zero output; a sample of different conductivity unbalances it.",
        "Sơ đồ mạch cầu của cảm biến dẫn nhiệt",
        "Bridge circuit diagram of the thermal conductivity sensor")


# ---------------------------------------------------------------------------
@_reg
def fig_f07():
    """Paramagnetic gas analyzer (source Figure 7)."""
    w, h = 680, 380
    o = [_defs()]
    o.append(T(340, 24, "May phan tich khi thuan tu / Paramagnetic gas analyzer", 9.0,
               color=INK, weight="600"))
    # Pole pieces producing a non-uniform magnetic field.
    o.append(_poly([(150, 132), (186, 132), (186, 188), (150, 188)],
                   fill="#dfeaf4", sw=1.2, close=True))
    o.append(_poly([(494, 132), (530, 132), (530, 188), (494, 188)],
                   fill="#dfeaf4", sw=1.2, close=True))
    o.append(T(168, 204, "Nam chau / Magnet", 6.8, color=INK))
    o.append(T(512, 204, "Nam chau / Magnet", 6.8, color=INK))
    # Suspended nitrogen-filled dumbbell.
    o.append(_line(340, 96, 340, 138, sw=1.2, color=GREY))
    o.append(T(340, 88, "Soi treo / Suspension", 6.8, color=GREY))
    o.append(_line(250, 160, 430, 160, sw=3.0, color=INK))
    o.append(_circle(250, 160, 28, fill="#eef3fb", sw=1.6))
    o.append(_circle(430, 160, 28, fill="#eef3fb", sw=1.6))
    o.append(_circle(340, 160, 8, fill="#f6e6c8", sw=1.2))
    o.append(T(250, 124, "Qua cau N2 / N2 sphere", 6.8, color=BLUE))
    o.append(T(430, 124, "Qua cau N2 / N2 sphere", 6.8, color=BLUE))
    # Optical lever: lamp, mirror and light receiver.
    o.append(_circle(200, 244, 10, fill="#fdf3e6", sw=1.2))
    o.append(_circle(480, 244, 10, fill="#f6e6c8", sw=1.2))
    o.append(_path("M200,244 L340,162 L480,244", sw=1.0, color=RED, dash="4 3"))
    o.append(T(200, 272, "Nguon sang / Light source", 6.8, color=RED))
    o.append(T(480, 272, "Dau doc anh / Light detector", 6.8, color=INK))
    o.append(T(340, 286, "Guong / Mirror", 6.6, color=GREY))
    o.append(_foot(680, 312, "Oxy bi hut vao vung tu truong manh lam quay qua cau / "
                             "Oxygen is pulled into the stronger field and turns the suspended dumbbell"))
    o.append(_foot(680, 336, "Dong phan hoi duaqua cau ve vi tri can bang ban dau / "
                             "A feedback current returns the dumbbell to its original balanced position"))
    o.append(_foot(680, 360, "Dong phan hoi ti le voi nong do oxy / "
                             "That feedback current is proportional to the oxygen concentration"))
    return _finish(o, w, h, "Paramagnetic gas analyzer",
        "Hình 7.7 · Máy phân tích khí thân từ kiểu quả tạ: hai quả cầu thủy tinh chứa nitơ được treo trong từ "
        "trường không đồng nhất. Oxy có độ từ cảm lớn bị hút vào vùng từ mạnh làm lệch quả tạ; gương và nguồn "
        "sáng phát hiện độ lệch, dòng phân hồi đưa quả tạ về vị trí cân bằng và tỉ lệ với nồng độ oxy.",
        "Figure 7.7 · A dumbbell-type paramagnetic oxygen analyzer: two nitrogen-filled glass spheres hang in a "
        "non-uniform magnetic field. Oxygen, with high magnetic susceptibility, is pulled into the stronger field "
        "and deflects the dumbbell; a mirror and light source sense the deflection and a feedback current restores "
        "balance in proportion to the oxygen concentration.",
        "Máy phân tích oxy thân từ kiểu quả tạ treo",
        "Suspended-dumbbell paramagnetic oxygen analyzer")


# ---------------------------------------------------------------------------
@_reg
def fig_f08():
    """ORSAT apparatus (source Figure 8)."""
    w, h = 680, 380
    o = [_defs()]
    o.append(T(340, 24, "Bo ORSAT / ORSAT apparatus", 9.0, color=INK, weight="600"))
    # Wooden case and capillary manifold.
    o.append(_rect(60, 78, 560, 236, fill="#fbfaf7", sw=1.6, stroke=GREY))
    o.append(_line(130, 110, 560, 110, sw=1.4, color=INK))
    # Water-jacketed gas burette with graduations.
    o.append(_rect(168, 118, 26, 166, fill="#eef3fb", sw=1.4))
    for k in range(7):
        yy = 130 + k * 22
        o.append(_line(168, yy, 178 if k % 2 else 182, yy, sw=0.8, color=GREY))
    o.append(T(181, 106, "Buret do / Gas burette", 7.0, color=INK))
    # Leveling bottle.
    o.append(_poly([(86, 246), (128, 246), (122, 286), (92, 286)],
                   fill="#dfeaf4", sw=1.2, close=True))
    o.append(_line(107, 246, 107, 206, sw=1.2, color=GREY))
    o.append(T(107, 302, "Binh can bang / Leveling bottle", 6.6, color=GREY))
    # Three absorption pipettes.
    for cx in (300, 400, 500):
        o.append(_line(cx, 110, cx, 146, sw=1.2, color=GREY))
        o.append(_poly([(cx - 30, 146), (cx, 190), (cx + 30, 146)],
                       fill="#fdf3e6", sw=1.2, close=True))
        o.append(_circle(cx, 190, 12, fill="#f6e6c8", sw=1.0))
    o.append(T(300, 216, "KOH / Caustic potash", 6.6, color=INK))
    o.append(T(400, 216, "Pyrogallol / O2", 6.6, color=INK))
    o.append(T(500, 216, "CuCl / CO", 6.6, color=INK))
    o.append(_foot(680, 336, "Khi duoc hut vao buret roi day lan luot qua cac pipet de hap thu CO2, O2 va CO / "
                             "Gas is drawn into the burette and passed through pipettes that absorb CO2, O2 and CO"))
    o.append(_foot(680, 360, "Binh can bang giu ap suat khong doi; the tich khi con lai cho biet thanh phan / "
                             "The leveling bottle keeps constant pressure and the residual volume gives each component"))
    return _finish(o, w, h, "ORSAT apparatus",
        "Hình 7.8 · Bộ ORSAT gồm buret đo khí có áo nước nối bằng ống mao dẫn tới ba pipet hấp thụ chứa KOH, "
        "pyrogallol kiềm và đồng clorua amoniac, cùng bình cân bằng. Khí mẫu được hút vào buret và đẩy lần lượt "
        "qua từng pipet; thể tích còn lại cho biết hàm lượng CO2, O2 và CO.",
        "Figure 7.8 · The ORSAT apparatus has a water-jacketed gas burette connected by capillary tubing to three "
        "absorption pipettes containing potassium hydroxide, alkaline pyrogallol and ammoniacal cuprous chloride, "
        "plus a leveling bottle. The gas is passed through each pipette in turn and the residual volume gives CO2, "
        "O2 and CO.",
        "Bộ ORSAT với buret đo khí và ba pipet hấp thụ",
        "ORSAT apparatus with gas burette and three absorption pipettes")


# ---------------------------------------------------------------------------
@_reg
def fig_f09():
    """Gravimetric method of gas analysis (source Figure 9)."""
    w, h = 680, 380
    o = [_defs()]
    o.append(T(340, 24, "Phap phan tich khi trong luong / Gravimetric method of gas analysis", 8.6,
               color=INK, weight="600"))
    # Dry oxygen feed and combustion tube.
    o.append(_rect(48, 134, 46, 40, fill="#eef3fb", sw=1.4))
    o.append(T(71, 124, "O2 kho / Dry O2", 7.0, color=BLUE))
    o.append(_rect(120, 132, 134, 44, fill="#fbfaf7", sw=1.4, stroke=GREY))
    o.append(_poly([(150, 168), (166, 148), (182, 168), (198, 148), (214, 168)],
                   sw=1.4, color=RED))
    o.append(T(187, 124, "Mau + xuc tac / Sample + catalyst", 6.8, color=RED))
    # Three weighed absorption tubes in series.
    for cx, fill in ((370, "#eef3fb"), (500, "#fdf3e6"), (610, "#fbfaf7")):
        o.append(_rect(cx - 26, 132, 52, 44, fill=fill, sw=1.4))
        o.append(_line(cx - 26, 154, cx + 26, 154, sw=0.8, color=GREY))
    o.append(T(370, 124, "P2O5: giu H2O / traps water", 6.6, color=INK))
    o.append(T(500, 124, "Ascarite: giu CO2 / traps CO2", 6.6, color=INK))
    o.append(T(610, 124, "Ong bao ve / Guard tube", 6.6, color=INK))
    for x1, x2 in ((94, 120), (254, 344), (396, 474), (526, 584)):
        o.append(_arrow(x1, 154, x2, 154, sw=1.4, color=BLUE))
    o.append(T(340, 226, "Can cac ong sau khi chay de xac dinh H va C / "
                         "Weigh the tubes after combustion to determine H and C", 6.8, color=INK))
    o.append(_foot(680, 274, "Mau chay trong O2 kho voi xuc tac kim loai; CO2 va H2O duoc tao thanh hoan toan / "
                             "The sample burns in dry oxygen with a metal catalyst; CO2 and H2O form completely"))
    o.append(_foot(680, 298, "P2O5 hap thu nuoc, ascarite hap thu CO2; ong thu ba chan nguoc am va CO2 / "
                             "P2O5 traps water and ascarite traps CO2; the third tube guards against backflow"))
    o.append(_foot(680, 322, "Do tang khoi luong cua cac ong ma tinh cacbon va hidro / "
                             "The increase in tube mass gives carbon and hydrogen"))
    return _finish(o, w, h, "Gravimetric method of gas analysis",
        "Hình 7.9 · Pháp phân tích khí trọng lượng: mẫu cháy hoàn toàn trong oxy khô có chất xúc tác, tạo CO2 và "
        "H2O. Ống P2O5 giữ nước, ống ascarite giữ CO2, ống thứ ba bảo vệ khí ẩm và CO2 từ ngoài tràn ngược. Cân "
        "độ tăng khối lượng các ống để xác định hydro và carbon.",
        "Figure 7.9 · Gravimetric gas analysis: the sample burns completely in dry oxygen with a catalyst, "
        "forming CO2 and H2O. A P2O5 tube traps water, an ascarite tube traps CO2 and a guard tube prevents "
        "backflow of atmospheric moisture and CO2. Weighing the tubes gives hydrogen and carbon.",
        "Sơ đồ các ống hấp thụ trong phân tích trọng lượng",
        "Absorption train for gravimetric gas analysis")


# ---------------------------------------------------------------------------
@_reg
def fig_f10():
    """Methane gas detector with a cap alarm (source Figure 10)."""
    w, h = 680, 380
    o = [_defs()]
    o.append(T(340, 24, "May do methane co bao dong tren mu / "
                        "Methane gas detector with a cap alarm", 8.6,
               color=INK, weight="600"))
    # Miner's helmet and cap lamp.
    o.append(_path("M196,232 Q196,130 340,130 Q484,130 484,232 Z",
                   fill="#eef3fb", sw=1.8))
    o.append(_line(186, 232, 494, 232, sw=3.0, color=INK))
    o.append(_circle(340, 158, 16, fill="#fdf3e6", sw=1.4))
    o.append(T(340, 110, "Den mu / Cap lamp", 7.0, color=INK))
    # Methane molecules rising toward the helmet.
    for cx, cy in ((206, 214), (230, 196), (250, 212), (268, 190)):
        o.append(_circle(cx, cy, 3.2, fill=RED, sw=0))
    o.append(T(200, 252, "Khi methane / Methane gas", 6.8, color=RED))
    # Detector module with lamp and buzzer.
    o.append(_rect(398, 176, 84, 52, fill="#fbfaf7", sw=1.4))
    o.append(_circle(416, 194, 7, fill="#f6d9a0", sw=1.0, color=RED))
    o.append(_circle(442, 194, 7, fill="#f6e6c8", sw=1.0))
    o.append(_line(410, 214, 470, 214, sw=1.0, color=GREY))
    o.append(T(440, 252, "Cam bien CH4 / CH4 sensor", 6.8, color=INK))
    o.append(T(440, 286, "Bao dong / Alarm", 6.8, color=RED))
    o.append(_foot(680, 318, "Bao dong bang anh sang va am thanh khi methane vuot nguong dat truoc / "
                             "Visual and audible alarms operate when methane exceeds a preset limit"))
    o.append(_foot(680, 342, "Khoi chay trong khong khi khi CH4 chiem 5 den 15 phan tram / "
                             "Methane in air can ignite at 5 to 15 percent by volume"))
    o.append(_foot(680, 366, "May duoc pin cua den mu cap nguon va deo tren mu thao tac / "
                             "The detector is powered by the cap-lamp battery and worn on the helmet"))
    return _finish(o, w, h, "Methane gas detector with a cap alarm",
        "Hình 7.10 · Máy dò khí methane gắn trên mũ thợ mỏ, dùng chung pin với đèn đội đầu. Cảm biến cảnh báo "
        "bằng đèn và còi khi nồng độ methane vượt ngưỡng cài đặt; hỗn hợp methane trong không khí có thể cháy ở "
        "nồng độ từ 5 đến 15 phần trăm thể tích.",
        "Figure 7.10 · A methane detector mounted on a miner's helmet and powered by the cap-lamp battery. The "
        "sensor gives visual and audible alarms when methane exceeds a set limit; methane in air is ignitable at "
        "5 to 15 percent by volume.",
        "Máy dò methane gắn trên mũ có đèn và còi báo động",
        "Helmet-mounted methane detector with light and audible alarm")


# ---------------------------------------------------------------------------
@_reg
def fig_f11():
    """Segments and variety of combustion processes (source Figure 11)."""
    w, h = 680, 380
    o = [_defs()]
    o.append(T(340, 24, "Cac doan va dang day chay / "
                        "Segments and variety of combustion processes", 8.6,
               color=INK, weight="600"))
    top = [(30, 100, "Nhien lieu", "Fuel"),
           (150, 100, "Khong khi chay", "Combustion air"),
           (270, 100, "Lo / Furnace", ""),
           (390, 100, "Chay / Combustion", ""),
           (510, 120, "Khi thai / Flue gas", "")]
    for x, bw, lab, sub in top:
        o.append(_rect(x, 130, bw, 60, fill="#eef3fb", sw=1.4))
        o.append(T(x + bw / 2.0, 158, lab, 7.0, color=INK))
        if sub:
            o.append(T(x + bw / 2.0, 173, sub, 6.4, color=GREY))
    for x1, x2 in ((130, 150), (250, 270), (370, 390), (490, 510)):
        o.append(_arrow(x1, 160, x2, 160, sw=1.4, color=BLUE))
    # Downstream processes fed from combustion.
    low = [(270, 100, "Qua trinh phu", "Connected processes"),
           (390, 100, "Lam sach khi thai", "Flue gas cleaning"),
           (510, 120, "Kiem soat khai thac", "Emission control")]
    for x, bw, lab, sub in low:
        o.append(_rect(x, 252, bw, 60, fill="#fbfaf7", sw=1.4, stroke=GREY))
        o.append(T(x + bw / 2.0, 280, lab, 7.0, color=INK))
        o.append(T(x + bw / 2.0, 295, sub, 6.4, color=GREY))
    o.append(_arrow(440, 190, 320, 252, sw=1.2, color=GREY))
    o.append(_arrow(440, 190, 440, 252, sw=1.2, color=GREY))
    o.append(_arrow(560, 190, 560, 252, sw=1.2, color=GREY))
    o.append(_foot(680, 336, "Phan tich khí o moi doan: nhien lieu, khong khi, chay va khi thai / "
                             "Gas analysis applies at each segment: fuel, air, combustion and flue gas"))
    o.append(_foot(680, 360, "Toi uu chay, kiem soat phat thai va van hanh on dinh / "
                             "Combustion optimisation, emission control and stable operation"))
    return _finish(o, w, h, "Segments and variety of combustion processes",
        "Hình 7.11 · Các đoạn của quá trình cháy: nhiên liệu và không khí cháy vào lò, diễn ra quá trình cháy "
        "và các quá trình liên quan, sau đó khí thải được làm sạch và kiểm soát phát thải. Phân tích khí tại "
        "mỗi đoạn giúp tối ưu cháy, kiểm soát khí thải và vận hành ổn định.",
        "Figure 7.11 · The segments of a combustion process: fuel and combustion air enter the furnace, "
        "combustion and connected processes take place, then flue gas is cleaned and emissions are controlled. "
        "Gas analysis at each segment supports optimisation, emission control and stable operation.",
        "Sơ đồ các đoạn của quá trình cháy công nghiệp",
        "Flow of the segments of an industrial combustion process")


# ---------------------------------------------------------------------------
@_reg
def fig_f12():
    """Combustion diagram (source Figure 12)."""
    w, h = 680, 380
    o = [_defs()]
    o.append(T(340, 24, "Bieu do chay / Combustion diagram", 9.0,
               color=INK, weight="600"))
    x0, x1, yt, yb = 90, 590, 90, 300

    def px(lam):
        return x0 + (lam - 0.8) / 0.8 * (x1 - x0)

    def py(val):
        return yb - val / 21.0 * (yb - yt)

    o.append(_line(x0, yb, x1 + 10, yb, sw=1.4))
    o.append(_line(x0, yb, x0, yt - 10, sw=1.4))
    for lam in (0.8, 1.0, 1.2, 1.4, 1.6):
        x = px(lam)
        o.append(_line(x, yb, x, yb + 4, sw=0.9))
        o.append(T(x, yb + 18, "%.1f" % lam, 6.8, color=GREY))
    for val in (0, 5, 10, 15, 20):
        y = py(val)
        o.append(_line(x0 - 4, y, x0, y, sw=0.9))
        o.append(T(x0 - 10, y + 2.4, "%d" % val, 6.8, color=GREY,
                   anchor="end"))
    o.append(_line(px(1.0), yt, px(1.0), yb, sw=1.0, color=GREY, dash="5 4"))
    o.append(T(px(1.0), 78, "can bang / stoichiometric", 7.0, color=GREY))
    o.append(T(90, 72, "Nong do % / Concentration %", 7.2, color=INK))
    # CO falls to zero just above lambda = 1.
    co = [(0.8, 8.0), (0.85, 6.6), (0.9, 4.8), (0.95, 2.4),
          (1.0, 0.6), (1.05, 0.0), (1.2, 0.0), (1.4, 0.0), (1.6, 0.0)]
    o.append(_poly([(px(a), py(b)) for a, b in co], sw=2.0, color=RED))
    # CO2 peaks at stoichiometric then is diluted by excess air.
    co2 = [(0.8, 7.0), (0.85, 9.0), (0.9, 11.5), (0.95, 13.8),
           (1.0, 15.0), (1.05, 14.6), (1.2, 12.8), (1.4, 10.8), (1.6, 9.2)]
    o.append(_poly([(px(a), py(b)) for a, b in co2], sw=2.0, color=GREEN))
    # O2 stays near zero until stoichiometric then rises.
    o2 = [(0.8, 0.0), (0.95, 0.0), (1.0, 0.3), (1.05, 1.2),
          (1.2, 3.6), (1.4, 6.2), (1.6, 8.5)]
    o.append(_poly([(px(a), py(b)) for a, b in o2], sw=2.0, color=BLUE))
    o.append(T(120, 222, "CO", 7.0, color=RED, weight="600"))
    o.append(T(368, 138, "CO2", 7.0, color=GREEN, weight="600"))
    o.append(T(560, 222, "O2", 7.0, color=BLUE, weight="600"))
    o.append(T(340, 340, "Gia tri khong khi du / Excess air value", 7.4,
               color=INK))
    o.append(_foot(680, 364, "Trai: thieu khi lam CO tang. Phai: du khi lam O2 tang va CO2 bi loang / "
                             "Left: air deficiency raises CO. Right: excess air raises O2 and dilutes CO2"))
    return _finish(o, w, h, "Combustion diagram",
        "Hình 7.12 · Biểu đồ cháy biểu diễn nồng độ CO, CO2 và O2 theo giá trị không khí dư. Bên trái (thiếu "
        "khí) CO tăng dần về không khi tiến tới điểm cân bằng; CO2 đạt cực đại tại điểm đó. Bên phải (dư khí) "
        "O2 tăng còn CO2 giảm do pha loãng.",
        "Figure 7.12 · The combustion diagram shows CO, CO2 and O2 concentrations against excess air value. "
        "On the left (air deficiency) CO falls to zero approaching stoichiometric and CO2 peaks there. On the "
        "right (excess air) O2 rises while CO2 falls through dilution.",
        "Biểu đồ nồng độ CO, CO2 và O2 theo không khí dư",
        "Plot of CO, CO2 and O2 concentrations versus excess air")


# ---------------------------------------------------------------------------
@_reg
def fig_f13():
    """Process flow chart of a solid fuel furnace (source Figure 13)."""
    w, h = 680, 380
    o = [_defs()]
    o.append(T(340, 24, "So do chay lo dot nhien lieu ran / "
                        "Process flow chart of a solid fuel furnace", 8.4,
               color=INK, weight="600"))
    boxes = [(30, 80, "Nhien lieu", "ran / solid"),
             (130, 70, "May nghien", "Mill"),
             (220, 70, "Dot / Burner", ""),
             (310, 90, "Lo / Furnace", ""),
             (430, 90, "Trao nhiet", "Heat exchanger"),
             (550, 90, "Khi thai", "Stack")]
    for x, bw, lab, sub in boxes:
        o.append(_rect(x, 150, bw, 56, fill="#eef3fb", sw=1.4))
        o.append(T(x + bw / 2.0, 176, lab, 7.0, color=INK))
        if sub:
            o.append(T(x + bw / 2.0, 191, sub, 6.4, color=GREY))
    for x1, x2 in ((110, 130), (200, 220), (290, 310), (400, 430), (520, 550)):
        o.append(_arrow(x1, 178, x2, 178, sw=1.4, color=BLUE))
    o.append(_line(410, 150, 410, 126, sw=0.9, color=GREY))
    o.append(_num(410, 118, 1))
    o.append(_line(595, 150, 595, 126, sw=0.9, color=GREY))
    o.append(_num(595, 118, 2))
    o.append(T(355, 232, "MP 1: dau ra lo / furnace outlet", 6.8, color=GREY))
    o.append(T(595, 232, "MP 2: cong khoi / stack", 6.8, color=GREY))
    o.append(_foot(680, 278, "MP 1: dieu chinh dot, tim CO va dam bao on dinh van hanh / "
                             "MP 1: burner tuning, CO pockets and reliable plant operation"))
    o.append(_foot(680, 302, "MP 2: giam sat phat thai o cong khoi / "
                             "MP 2: emission monitoring in the clean gas at the stack"))
    o.append(_foot(680, 326, "Phan tich khi toi uu nhien lieu, lap can bang nang luong va kiem soat khai thac / "
                             "Gas analysis optimises fuel, provides the energy balance and controls emissions"))
    return _finish(o, w, h, "Process flow chart of a solid fuel furnace with measuring points",
        "Hình 7.13 · Sơ đồ dây chuyền lò đốt nhiên liệu rắn: nhiên liệu nghiền đi qua đầu đốt vào lò, trao đổi "
        "nhiệt rồi thải qua cống khói. Điểm đo MP 1 tại đầu ra lò dùng chỉnh đốt và phát hiện CO; MP 2 tại cống "
        "khói dùng giám sát phát thải.",
        "Figure 7.13 · Process flow chart of a solid-fuel furnace: crushed fuel passes a burner into the furnace, "
        "then through a heat exchanger to the stack. Measuring point MP 1 at the furnace outlet tunes the burner "
        "and finds CO pockets; MP 2 at the stack monitors emissions.",
        "Sơ đồ lò đốt nhiên liệu rắn với hai điểm đo",
        "Solid-fuel furnace flow chart with two measuring points")


# ---------------------------------------------------------------------------
@_reg
def fig_f14():
    """Process flow chart of a gas fired furnace (source Figure 14)."""
    w, h = 680, 380
    o = [_defs()]
    o.append(T(340, 24, "So do chay lo dot khi / "
                        "Process flow chart of a gas fired furnace", 8.6,
               color=INK, weight="600"))
    boxes = [(30, 90, "Khi dot / Fuel gas", ""),
             (140, 90, "Quat gio / Air fan", ""),
             (250, 80, "Dot / Burner", ""),
             (350, 90, "Lo / Furnace", ""),
             (460, 90, "Trao nhiet", "Heat exchanger"),
             (570, 80, "Cong khoi", "Stack")]
    for x, bw, lab, sub in boxes:
        o.append(_rect(x, 150, bw, 56, fill="#eef3fb", sw=1.4))
        o.append(T(x + bw / 2.0, 176, lab, 7.0, color=INK))
        if sub:
            o.append(T(x + bw / 2.0, 191, sub, 6.4, color=GREY))
    for x1, x2 in ((120, 140), (230, 250), (330, 350), (440, 460), (550, 570)):
        o.append(_arrow(x1, 178, x2, 178, sw=1.4, color=BLUE))
    o.append(_line(395, 150, 395, 126, sw=0.9, color=GREY))
    o.append(_num(395, 118, 1))
    o.append(_line(610, 150, 610, 126, sw=0.9, color=GREY))
    o.append(_num(610, 118, 2))
    o.append(T(340, 232, "MP 1: dau ra lo / furnace outlet", 6.8, color=GREY))
    o.append(T(610, 232, "MP 2: cong khoi / stack", 6.8, color=GREY))
    o.append(_foot(680, 278, "MP 1: dieu chinh dot toi uu, giam chi phi nhien lieu / "
                             "MP 1: optimum burner adjustment and reduced fuel cost"))
    o.append(_foot(680, 302, "MP 2: giam sat phat thai o cong khoi / "
                             "MP 2: emission monitoring at the stack"))
    o.append(_foot(680, 326, "Khi dot duoc cap bang van hoac vot ap cao; chay gan nhu sach va it tro / "
                             "Fuel gas is fed by vents or high-pressure burners with almost no residues"))
    return _finish(o, w, h, "Process flow chart of a gas fired furnace with measuring points",
        "Hình 7.14 · Sơ đồ dây chuyền lò đốt khí: khí nhiên liệu và không khí cháy qua đầu đốt vào lò, trao đổi "
        "nhiệt rồi ra cống khói. MP 1 tại đầu ra lò dùng chỉnh đốt tối ưu và giảm chi phí nhiên liệu; MP 2 tại "
        "cống khói dùng giám sát phát thải.",
        "Figure 7.14 · Process flow chart of a gas-fired furnace: fuel gas and combustion air pass a burner into "
        "the furnace, then a heat exchanger and the stack. MP 1 at the furnace outlet gives optimum burner "
        "adjustment and lower fuel cost; MP 2 at the stack monitors emissions.",
        "Sơ đồ lò đốt khí với hai điểm đo",
        "Gas-fired furnace flow chart with two measuring points")


# ---------------------------------------------------------------------------
@_reg
def fig_f15():
    """Process flow chart of a gas turbine plant (source Figure 15)."""
    w, h = 680, 380
    o = [_defs()]
    o.append(T(340, 24, "So do chay nha may tua bin khi / "
                        "Process flow chart of a gas turbine plant", 8.4,
               color=INK, weight="600"))
    boxes = [(30, 80, "Khong khi", "Air"),
             (130, 100, "May nen", "Compressor"),
             (250, 100, "Buong dot", "Combustor"),
             (370, 80, "Tua bin", "Turbine"),
             (470, 80, "May phat", "Generator"),
             (570, 80, "Cong khoi", "Stack")]
    for x, bw, lab, sub in boxes:
        o.append(_rect(x, 150, bw, 56, fill="#eef3fb", sw=1.4))
        o.append(T(x + bw / 2.0, 176, lab, 7.0, color=INK))
        o.append(T(x + bw / 2.0, 191, sub, 6.4, color=GREY))
    for x1, x2 in ((110, 130), (230, 250), (350, 370), (450, 470), (550, 570)):
        o.append(_arrow(x1, 178, x2, 178, sw=1.4, color=BLUE))
    o.append(_line(410, 150, 410, 126, sw=0.9, color=GREY))
    o.append(_num(410, 118, 1))
    o.append(_line(610, 150, 610, 126, sw=0.9, color=GREY))
    o.append(_num(610, 118, 2))
    o.append(T(410, 232, "MP 1: dau ra tua bin / turbine outlet", 6.8, color=GREY))
    o.append(T(610, 232, "MP 2: cong khoi / stack", 6.8, color=GREY))
    o.append(_foot(680, 278, "MP 1: giam sat khi thai tua bin de van hanh toi uu / "
                             "MP 1: monitor turbine emissions for optimum operation"))
    o.append(_foot(680, 302, "MP 2: giam sat phat thai o cong khoi / "
                             "MP 2: emission monitoring at the stack"))
    o.append(_foot(680, 326, "Thanh phan khi thai giong lo dot khi; nhien lieu co the la khi tu nhien hoac khi bai / "
                             "Exhaust resembles a gas furnace; fuel may be natural gas, landfill gas or biogas"))
    return _finish(o, w, h, "Process flow chart of a gas turbine plant with measuring points",
        "Hình 7.15 · Sơ đồ dây chuyền nhà máy tua bin khí: không khí qua máy nén vào buồng đốt, khí nóng quay "
        "tua bin dẫn động máy phát rồi thải ra cống khói. MP 1 tại đầu ra tua bin giám sát phát thải để vận hành "
        "tối ưu; MP 2 tại cống khói giám sát phát thải theo quy định.",
        "Figure 7.15 · Process flow chart of a gas turbine plant: air passes a compressor into a combustor, hot "
        "gas spins the turbine driving a generator and leaves through the stack. MP 1 at the turbine outlet "
        "monitors emissions for optimum operation; MP 2 at the stack checks regulatory compliance.",
        "Sơ đồ nhà máy tua bin khí với hai điểm đo",
        "Gas turbine plant flow chart with two measuring points")


# ---------------------------------------------------------------------------
@_reg
def fig_f16():
    """Process flow chart of an oil-fired furnace (source Figure 16)."""
    w, h = 680, 380
    o = [_defs()]
    o.append(T(340, 24, "So do chay lo dot dau / "
                        "Process flow chart of an oil-fired furnace", 8.8,
               color=INK, weight="600"))
    boxes = [(30, 80, "Dau / Oil", ""),
             (130, 80, "Bom / Pump", ""),
             (230, 100, "Dot / Burner", "oil and air spray"),
             (350, 90, "Lo / Furnace", ""),
             (460, 90, "Trao nhiet", "Heat exchanger"),
             (570, 80, "Cong khoi", "Stack")]
    for x, bw, lab, sub in boxes:
        o.append(_rect(x, 150, bw, 56, fill="#eef3fb", sw=1.4))
        o.append(T(x + bw / 2.0, 176, lab, 7.0, color=INK))
        if sub:
            o.append(T(x + bw / 2.0, 191, sub, 6.2, color=GREY))
    for x1, x2 in ((110, 130), (210, 230), (330, 350), (440, 460), (550, 570)):
        o.append(_arrow(x1, 178, x2, 178, sw=1.4, color=BLUE))
    o.append(_line(395, 150, 395, 126, sw=0.9, color=GREY))
    o.append(_num(395, 118, 1))
    o.append(_line(610, 150, 610, 126, sw=0.9, color=GREY))
    o.append(_num(610, 118, 2))
    o.append(T(340, 232, "MP 1: dau ra lo / furnace outlet", 6.8, color=GREY))
    o.append(T(610, 232, "MP 2: cong khoi / stack", 6.8, color=GREY))
    o.append(_foot(680, 278, "MP 1: dieu chinh dot, giam chi phi va lap can bang nang luong / "
                             "MP 1: burner adjustment, fuel cost reduction and energy balance"))
    o.append(_foot(680, 302, "MP 2: giam sat phat thai o cong khoi / "
                             "MP 2: emission monitoring at the stack"))
    o.append(_foot(680, 326, "Dau va khong khi chay duoc phun thanh hon hop vao buong dot; it tro va it bui / "
                             "Oil and air are sprayed as a mixture into the chamber, with little residue or dust"))
    return _finish(o, w, h, "Process flow chart of an oil-fired furnace with measuring points",
        "Hình 7.16 · Sơ đồ dây chuyền lò đốt dầu: dầu qua bơm được phun cùng không khí tại đầu đốt vào lò, trao "
        "đổi nhiệt rồi thải qua cống khói. MP 1 tại đầu ra lò dùng chỉnh đốt, giảm chi phí và lập cân bằng năng "
        "lượng; MP 2 tại cống khói dùng giám sát phát thải.",
        "Figure 7.16 · Process flow chart of an oil-fired furnace: oil is pumped and sprayed with combustion air "
        "at the burner into the furnace, then through a heat exchanger to the stack. MP 1 at the furnace outlet "
        "supports burner adjustment, fuel saving and energy balance; MP 2 monitors emissions at the stack.",
        "Sơ đồ lò đốt dầu với hai điểm đo",
        "Oil-fired furnace flow chart with two measuring points")


# ---------------------------------------------------------------------------
@_reg
def fig_f17():
    """Process flow chart of a coal-fired power station (source Figure 17)."""
    w, h = 680, 400
    o = [_defs()]
    o.append(T(340, 24, "So do chay nha may dien than / "
                        "Process flow chart of a coal-fired power station", 8.4,
               color=INK, weight="600"))
    boxes = [(20, 74, "Than / Coal", ""),
             (108, 74, "Nghien / Mill", ""),
             (196, 94, "Lo hoi / Boiler", ""),
             (304, 80, "Tua bin", "Turbine"),
             (398, 80, "May phat", "Generator"),
             (492, 100, "Xu ly khi", "Gas cleaning"),
             (606, 56, "Cong khoi", "Stack")]
    for x, bw, lab, sub in boxes:
        o.append(_rect(x, 154, bw, 52, fill="#eef3fb", sw=1.4))
        o.append(T(x + bw / 2.0, 177, lab, 6.8, color=INK))
        if sub:
            o.append(T(x + bw / 2.0, 192, sub, 6.2, color=GREY))
    for x1, x2 in ((94, 108), (182, 196), (290, 304), (384, 398),
                   (478, 492), (592, 606)):
        o.append(_arrow(x1, 180, x2, 180, sw=1.3, color=BLUE))
    o.append(_line(243, 154, 243, 128, sw=0.9, color=GREY))
    o.append(_num(243, 120, 1))
    o.append(_line(292, 206, 292, 232, sw=0.9, color=GREY))
    o.append(_num(292, 240, 2))
    o.append(_line(542, 154, 542, 128, sw=0.9, color=GREY))
    o.append(_num(542, 120, 3))
    o.append(_line(634, 206, 634, 232, sw=0.9, color=GREY))
    o.append(_num(634, 240, 4))
    o.append(T(340, 278, "1. Lo: chay on dinh, phat hien CO / Furnace: stable fire, CO detection", 6.6, color=GREY))
    o.append(T(340, 300, "2. Dau ra lo: toi uu chay / Furnace outlet: combustion optimisation", 6.6, color=GREY))
    o.append(T(340, 322, "3. Khu NOx: kiem tra hieu suat / Denitrification: performance control", 6.6, color=GREY))
    o.append(T(340, 344, "4. Cong khoi: giam sat phat thai / Stack: emission monitoring", 6.6, color=GREY))
    o.append(_foot(680, 374, "Hoi ap cao tu lo hoi quay tua bin; khi thai qua cac thiet bi loc va chuyen hoa / "
                             "High-pressure steam from the boiler drives the turbine; flue gas passes scrubbers"))
    return _finish(o, w, h, "Process flow chart of a coal-fired power station with measuring points",
        "Hình 7.17 · Sơ đồ dây chuyền nhà máy điện than: than nghiền vào lò hơi, hơi quay tua bin phát điện; khí "
        "thải đi qua hệ thống khử NOx, lọc bụi và thiết bị làm sạch rồi ra cống khói. MP 1 tại lò, MP 2 tại đầu "
        "ra lò, MP 3 tại khử NOx và MP 4 tại cống khói.",
        "Figure 7.17 · Process flow chart of a coal-fired power station: ground coal enters the boiler and steam "
        "drives a generator; flue gas passes denitrification, dust filtration and gas cleaning to the stack. "
        "MP 1 is at the furnace, MP 2 at the furnace outlet, MP 3 at denitrification and MP 4 at the stack.",
        "Sơ đồ nhà máy điện than với bốn điểm đo",
        "Coal-fired power station flow chart with four measuring points")


# ---------------------------------------------------------------------------
@_reg
def fig_f18():
    """Process flow chart of a block-type power station (source Figure 18)."""
    w, h = 680, 380
    o = [_defs()]
    o.append(T(340, 24, "So do chay tram dien kieu khoi / "
                        "Process flow chart of a block-type power station", 8.4,
               color=INK, weight="600"))
    # Generator driven by the gas engine above the main gas line.
    o.append(_rect(170, 76, 120, 46, fill="#fbfaf7", sw=1.4, stroke=GREY))
    o.append(T(230, 98, "May phat / Generator", 7.0, color=INK))
    o.append(_line(230, 122, 230, 150, sw=1.2, color=GREY))
    boxes = [(40, 90, "Khi dot / Fuel gas", ""),
             (170, 120, "Dong co / Engine", ""),
             (330, 120, "Chat xuc tac", "Catalyst"),
             (480, 100, "Thu hoi nhiet", "Heat recovery"),
             (600, 60, "Cong khoi", "Stack")]
    for x, bw, lab, sub in boxes:
        o.append(_rect(x, 150, bw, 56, fill="#eef3fb", sw=1.4))
        o.append(T(x + bw / 2.0, 176, lab, 7.0, color=INK))
        if sub:
            o.append(T(x + bw / 2.0, 191, sub, 6.4, color=GREY))
    for x1, x2 in ((130, 170), (290, 330), (450, 480), (580, 600)):
        o.append(_arrow(x1, 178, x2, 178, sw=1.4, color=BLUE))
    o.append(_line(310, 150, 310, 128, sw=0.9, color=GREY))
    o.append(_num(310, 120, 1))
    o.append(_line(465, 150, 465, 128, sw=0.9, color=GREY))
    o.append(_num(465, 120, 2))
    o.append(T(340, 232, "MP 1: truoc chat xuc tac / before catalyst", 6.8, color=GREY))
    o.append(T(530, 232, "MP 2: sau chat xuc tac / behind catalyst", 6.8, color=GREY))
    o.append(_foot(680, 278, "MP 1: giua dong co va chat xuc tac, dieu chinh may va kiem tra hieu suat / "
                             "MP 1: between engine and catalyst for engine setting and efficiency control"))
    o.append(_foot(680, 302, "MP 2: sau chat xuc tac, kiem tra hieu suat va giam sat phat thai / "
                             "MP 2: behind the catalyst for efficiency control and emission monitoring"))
    o.append(_foot(680, 326, "Dien va nhiet duoc san xuat dong thoi tu nhien lieu khi hoac dau diesel / "
                             "Electricity and heat are produced together from natural gas or diesel fuel"))
    return _finish(o, w, h, "Process flow chart of a block-type power station with measuring points",
        "Hình 7.18 · Sơ đồ dây chuyền trạm điện kiểu khối: động cơ đốt khí dẫn động máy phát, khí thải qua chất "
        "xúc tác và bộ thu hồi nhiệt rồi ra cống khói. MP 1 nằm giữa động cơ và chất xúc tác để chỉnh máy và "
        "kiểm tra hiệu suất; MP 2 nằm sau chất xúc tác để giám sát phát thải.",
        "Figure 7.18 · Process flow chart of a block-type power station: a gas engine drives a generator, and "
        "exhaust passes a catalyst and heat recovery before the stack. MP 1 lies between engine and catalyst for "
        "engine setting and efficiency control; MP 2 is behind the catalyst for emission monitoring.",
        "Sơ đồ trạm điện kiểu khối với hai điểm đo",
        "Block-type combined heat and power flow chart with two measuring points")


# ---------------------------------------------------------------------------
@_reg
def fig_f19():
    """Process flow chart of a gas and steam power station (source Figure 19)."""
    w, h = 680, 400
    o = [_defs()]
    o.append(T(340, 24, "So do chay nha may dien khi va hoi / "
                        "Process flow chart of a gas and steam power station", 8.4,
               color=INK, weight="600"))
    # Gas path.
    boxes = [(20, 80, "Khi dot / Fuel", ""),
             (120, 110, "Buong dot", "Burner"),
             (250, 110, "Tua bin khi", "Gas turbine"),
             (380, 120, "SNPH hoi", "Heat recovery"),
             (520, 90, "Cong khoi", "Stack")]
    for x, bw, lab, sub in boxes:
        o.append(_rect(x, 138, bw, 54, fill="#eef3fb", sw=1.4))
        o.append(T(x + bw / 2.0, 162, lab, 7.0, color=INK))
        o.append(T(x + bw / 2.0, 177, sub, 6.2, color=GREY))
    for x1, x2 in ((100, 120), (230, 250), (360, 380), (500, 520)):
        o.append(_arrow(x1, 165, x2, 165, sw=1.4, color=BLUE))
    # Steam loop below the heat-recovery boiler.
    o.append(_rect(380, 262, 120, 52, fill="#fbfaf7", sw=1.4, stroke=GREY))
    o.append(T(440, 284, "Tua bin hoi / Steam turbine", 6.8, color=INK))
    o.append(_rect(520, 262, 110, 52, fill="#fbfaf7", sw=1.4, stroke=GREY))
    o.append(T(575, 284, "May phat / Generator", 6.8, color=INK))
    o.append(_rect(250, 262, 110, 52, fill="#fbfaf7", sw=1.4, stroke=GREY))
    o.append(T(305, 284, "Nuoc cap / Feedwater", 6.8, color=INK))
    o.append(_arrow(440, 192, 440, 262, sw=1.3, color=GREEN))
    o.append(_arrow(500, 288, 520, 288, sw=1.3, color=GREEN))
    o.append(_path("M520,300 L360,300", sw=1.1, color=GREY, dash="5 4"))
    o.append(_arrow(305, 262, 305, 192, sw=1.3, color=GREY, dash="5 4"))
    # Measurement points.
    o.append(_line(230, 138, 230, 114, sw=0.9, color=GREY))
    o.append(_num(230, 106, 1))
    o.append(_line(565, 138, 565, 114, sw=0.9, color=GREY))
    o.append(_num(565, 106, 2))
    o.append(_foot(680, 340, "MP 1: dau ra buong dot, toi uu chay va phat thai / "
                             "MP 1: burner outlet for combustion and emission optimisation"))
    o.append(_foot(680, 364, "MP 2: cong khoi, giam sat phat thai / "
                             "MP 2: stack for emission monitoring and regulatory compliance"))
    o.append(T(340, 226, "Khi nong tua bin khi tao hoi ap cao cho tua bin hoi / "
                         "Hot gas-turbine exhaust raises high-pressure steam", 6.8, color=GREY))
    return _finish(o, w, h, "Process flow chart of a gas and steam power station with measuring points",
        "Hình 7.19 · Sơ đồ dây chuyền nhà máy điện kết hợp khí và hơi: khí nhiên liệu cháy quay tua bin khí, khí "
        "nóng đi qua lò thu hồi nhiệt tạo hơi áp lực cao cho tua bin hơi và máy phát. MP 1 tại đầu ra buồng đốt "
        "tối ưu cháy và phát thải; MP 2 tại cống khói giám sát phát thải.",
        "Figure 7.19 · Process flow chart of a combined gas and steam power station: fuel burns to drive a gas "
        "turbine, and hot exhaust passes a heat-recovery boiler that raises high-pressure steam for a steam "
        "turbine and generator. MP 1 at the burner outlet optimises combustion and emissions; MP 2 at the stack "
        "monitors emissions.",
        "Sơ đồ nhà máy điện kết hợp khí và hơi với hai điểm đo",
        "Combined gas and steam power station flow chart with two measuring points")
