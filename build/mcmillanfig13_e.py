# -*- coding: utf-8 -*-
"""Vector redraws of Figures 13.28-13.35 in A. McMillan, *Electrical
Installations in Hazardous Areas*, Chapter 13 "Intrinsic safety 'i'".

All eight drawings are simplified vector redraws of the rendered pages
p421, p424, p425, p426, p429, p430 and p431.  The printed English
captions, including the two printed Notes of Fig. 13.30, are reproduced
verbatim behind a bilingual prefix; every part label, equation, axis
mark and threshold printed in the figures is transcribed onto the
drawings.  Printed quirks are retained: the two identical "Copper
plating extends through hole" labels of Fig. 13.28, the terminal comma
on the V_F note of Fig. 13.29, the V1/V2 graph marks of Fig. 13.30,
the two different Note 1 texts and the R1 subscript of Fig. 13.32,
"Cable capacity" in the Fig. 13.34 key, and the missing word "ratio" in
the Fig. 13.35 caption.  Each public callable returns the standard
five-tuple through ``vfig._fig()`` and is registered in ``FIGS`` by the
``_reg`` decorator.
"""
import sys
import os

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

from vfig import (BLUE, GREEN, GREY, INK, PAPER, RED, _arrow, _circle,
                  _defs, _ellipse, _f, _fig, _line, _path, _poly, _rect,
                  _txt, svg)

FIGS = {}


def _reg(f):
    FIGS[f.__name__] = f()
    return f


def esc(s):
    """Every displayed string is literal Unicode with raw ampersands escaped."""
    return str(s).replace("&", "&amp;")


def T(x, y, s, size=8.0, **kw):
    """Plain text: escape first, then delegate to vfig._txt()."""
    return _txt(x, y, esc(s), size, **kw)


# ------------------------------------------------------------------ helpers

def _title(o, n, vi, en, size=7.2):
    o.append(T(340, 15, "Hình 13.%d · %s / Figure 13.%d · %s" % (n, vi, n, en),
               size, color=INK, weight="600"))


def _sub(o, s, size=6.8):
    """All displayed type stays within the 6.8-9.5 px contract."""
    o.append(T(340, 29, s, max(6.8, size), color=GREY))


def _bi(o, x, y, vi, en, size=6.8, weight=""):
    """Vietnamese label first, printed English term in parentheses below."""
    size = max(6.8, size)
    o.append(T(x, y, vi, size, color=INK, weight=weight))
    o.append(T(x, y + size + 1.4, "(" + en + ")", size, color=GREY))


def _lead(x1, y1, x2, y2, sw=0.8):
    return _arrow(x1, y1, x2, y2, sw=sw, color=INK, head="a7")


def _res_h(x1, x2, y, sw=1.1):
    pts = [(x1, y)]
    step = (x2 - x1) / 6.0
    for i in range(1, 6):
        pts.append((x1 + step * i, y + (-5 if i % 2 else 5)))
    pts.append((x2, y))
    return _poly(pts, fill="none", sw=sw)


def _res_v(x, y1, y2, sw=1.1):
    pts = [(x, y1)]
    step = (y2 - y1) / 6.0
    for i in range(1, 6):
        pts.append((x + (-5 if i % 2 else 5), y1 + step * i))
    pts.append((x, y2))
    return _poly(pts, fill="none", sw=sw)


def _coil_h(x, y, w=40, n=4, r=4.5):
    step = w / float(n)
    d = "M%s %s" % (_f(x), _f(y))
    for i in range(n):
        d += " A%s %s 0 0 1 %s %s" % (_f(r), _f(r),
                                      _f(x + step * (i + 1)), _f(y))
    return _path(d, fill="none", sw=1.1)


def _coil_v(x, y1, y2, n=3, r=4.0):
    step = (y2 - y1) / float(n)
    d = "M%s %s" % (_f(x), _f(y1))
    for i in range(n):
        d += " A%s %s 0 0 0 %s %s" % (_f(r), _f(r), _f(x),
                                      _f(y1 + step * (i + 1)))
    return _path(d, fill="none", sw=1.1)


def _fuse_h(x, y, w=22):
    return (_rect(x, y - 5, w, 10, fill="#ffffff", sw=1.0)
            + _line(x + 2, y + 4, x + w - 2, y - 4, sw=1.0))


def _zener_v(x, y_top, y_bot, label=None):
    """Vertical zener: cathode bar above a filled triangle."""
    span = y_bot - y_top
    th = min(12.0, span * 0.38)
    apex = y_top + span * 0.56 - th
    bar = y_top + span * 0.56 + th * 0.18
    o = [_line(x, y_top, x, apex, sw=1.1),
         _poly([(x - 8, bar), (x, apex), (x + 8, bar)],
               fill="#2a2a2a", sw=1.0, close=True),
         _line(x - 10, bar, x + 10, bar, sw=1.3),
         _line(x, bar, x, y_bot, sw=1.1)]
    if label:
        o.append(T(x, y_bot + 9, label, 6.8))
    return "".join(o)


def _diode_left(x, y):
    """In-line diode pointing left, as printed in Fig. 13.32 diagram 4."""
    return (_poly([(x + 8, y - 6), (x - 6, y), (x + 8, y + 6)],
                  fill="#2a2a2a", sw=1.0, close=True)
            + _line(x - 8, y - 7, x - 8, y + 7, sw=1.3))


def _earth(x, y):
    return (_line(x - 9, y, x + 9, y, sw=1.2)
            + _line(x - 6, y + 4, x + 6, y + 4, sw=1.0)
            + _line(x - 3, y + 8, x + 3, y + 8, sw=0.9))


# ------------------------------------------------------------------ 13.28

@_reg
def fig_f1328():
    """Figure 13.28 - two infallible soldered joints, machine and manual."""
    w, h = 680, 300
    o = [_defs(), _rect(0, 0, w, h, fill=PAPER, sw=0)]
    _title(o, 28, "Mối hàn không hỏng", "Infallible soldered joints", 7.2)
    _sub(o, "Hai mối hàn trên cùng một bảng mạch · mối hàn máy (trái) và mối hàn tay (phải) / "
            "Two joints on a common board · machine and manual joints")

    for cx, bent in ((170, False), (510, True)):
        # Common hatched board with a plated-through hole at the centre.
        o.append(_rect(cx - 90, 170, 180, 12, fill="url(#h6)", sw=1.0))
        o.append(_line(cx - 90, 182, cx + 90, 182, sw=0.9))
        o.append(_rect(cx - 12, 168, 3, 20, fill="#8a8a8a", sw=0.8))
        o.append(_rect(cx + 9, 168, 3, 20, fill="#8a8a8a", sw=0.8))
        # Wire and its insulation.
        o.append(_rect(cx - 9, 108, 18, 82, fill="#cfcfcf", sw=1.0))
        o.append(_rect(cx - 9, 66, 18, 52, fill="#bdbdbd", sw=1.0))
        if bent:
            o.append(_poly([(cx - 9, 72), (cx + 2, 62), (cx + 16, 68),
                            (cx + 18, 84), (cx + 11, 90), (cx + 9, 78),
                            (cx + 2, 74), (cx - 9, 82)],
                           fill="#bdbdbd", sw=1.0, close=True))
        # Solder fillet under the board and around the hole.
        o.append(_ellipse(cx, 186, 30, 10, fill="#dedede", sw=1.0))
        o.append(_poly([(cx - 26, 184), (cx - 14, 194), (cx, 198),
                        (cx + 14, 194), (cx + 26, 184)],
                       fill="none", sw=1.0))

    # Left-hand (machine) call-outs.
    o.append(T(42, 92, "Copper plating", 6.8, anchor="start"))
    o.append(T(42, 101, "extends through hole", 6.8, anchor="start"))
    o.append(_lead(142, 98, 160, 169))
    o.append(T(226, 100, "Wire insulation", 6.8, anchor="start"))
    o.append(_lead(224, 104, 183, 116))
    o.append(T(42, 212, "Machine applied", 6.8, anchor="start"))
    o.append(T(42, 221, "solder", 6.8, anchor="start"))
    o.append(_lead(128, 209, 152, 190))
    o.append(T(232, 212, "Wire left", 6.8, anchor="start"))
    o.append(T(232, 221, "straight", 6.8, anchor="start"))
    o.append(_lead(230, 208, 179, 158))
    o.append(T(170, 250, "Machine joint", 7.6, color=INK, weight="600"))

    # Right-hand (manual) call-outs.
    o.append(T(610, 84, "Wire", 6.8, anchor="end"))
    o.append(_lead(604, 87, 516, 108))
    o.append(T(404, 100, "Insulation", 6.8, anchor="end"))
    o.append(_lead(406, 104, 503, 96))
    o.append(T(638, 120, "Copper plating", 6.8, anchor="end"))
    o.append(T(638, 129, "extends through hole", 6.8, anchor="end"))
    o.append(_lead(564, 126, 523, 169))
    o.append(T(412, 212, "Manually", 6.8, anchor="start"))
    o.append(T(412, 221, "applied solder", 6.8, anchor="start"))
    o.append(_lead(458, 209, 490, 190))
    o.append(T(638, 212, "Wire bent", 6.8, anchor="end"))
    o.append(T(638, 221, "over", 6.8, anchor="end"))
    o.append(_lead(608, 208, 527, 152))
    o.append(T(510, 250, "Manual joint", 7.6, color=INK, weight="600"))

    o.append(T(340, 278, "Hai mối hàn cùng xuyên qua lỗ mạ đồng · dây để thẳng ở mối hàn máy, "
                "dây bẻ cong ở mối hàn tay", 6.8, color=GREY))

    return _fig(svg(w, h, "".join(o), esc("Fig. 13.28")),
                "Hình 13.28 · Mối hàn không hỏng",
                "Figure 13.28 · Infallible soldered joints",
                "Hai mối hàn cắt ngang trên cùng một đường bảng mạch gạch chéo. Bên trái là mối "
                "hàn máy: dây dẫn để thẳng xuyên qua lỗ mạ đồng, phần đầu dây có lớp cách điện, "
                "lớp thiếc chảy máy bao quanh mặt dưới bảng, nhãn ghi Machine joint. Bên phải là "
                "mối hàn tay: dây dẫn được bẻ cong lại qua lỗ mạ đồng, thiếc được bôi thủ công, "
                "nhãn ghi Manual joint. Cả hai hình đều có nhãn Copper plating extends through "
                "hole giống hệt nhau, cùng các nhãn Wire, Insulation, Wire insulation, Machine "
                "applied solder và Manually applied solder",
                "Two soldered-joint cross-sections on one common hatched board line. On the left "
                "a machine joint shows a straight wire passing through a plated-through hole, "
                "its insulated upper end, machine-applied solder under the board and the label "
                "Machine joint. On the right a manual joint shows the wire bent over at the hole, "
                "manually applied solder and the label Manual joint. Both views repeat the "
                "identical label Copper plating extends through hole; the other leaders read "
                "Wire, Insulation, Wire insulation, Machine applied solder and Manually applied "
                "solder")


# ------------------------------------------------------------------ 13.29

@_reg
def fig_f1329():
    """Figure 13.29 - typical zener (avalanche) diode characteristics."""
    w, h = 680, 300
    o = [_defs(), _rect(0, 0, w, h, fill=PAPER, sw=0)]
    _title(o, 29, "Đặc tính điển hình của diode zener (sụp đổ thác lũ)",
           "Typical zener (avalanche) diode characteristics", 7.0)
    _sub(o, "Đồ thị dòng theo áp · nhánh thuận và nhánh zener / Current-voltage graph · forward and "
            "zener branches")

    # Axes cross at the origin; current is positive upwards.
    o.append(_arrow(80, 165, 606, 165, sw=1.1))
    o.append(_arrow(340, 258, 340, 60, sw=1.1))
    o.append(_line(340, 160, 340, 170, sw=1.0))

    # Forward branch: near-zero current until V_F, then a steep rise.
    o.append(_poly([(340, 165), (348, 165), (352, 161), (362, 132),
                    (372, 96), (378, 68)], fill="none", sw=1.8, color=BLUE))
    # Zener branch: near-zero current to the left, then breakdown at V_Z.
    o.append(_poly([(338, 165), (300, 164), (260, 163), (250, 161),
                    (250, 196), (250, 232)], fill="none", sw=1.8, color=RED))
    o.append(_line(250, 120, 250, 158, sw=0.8, dash="3 3", color=GREY))

    o.append(T(356, 70, "Current", 6.8, anchor="start"))
    o.append(T(332, 84, "I", 6.8, anchor="end"))
    o.append(T(332, 252, "−I", 6.8, anchor="end"))
    o.append(T(398, 97, "Diode", 6.8, anchor="start"))
    o.append(T(398, 106, "current", 6.8, anchor="start"))
    o.append(_lead(392, 110, 370, 104))
    o.append(T(100, 148, "Zener", 6.8, anchor="start"))
    o.append(T(100, 157, "direction", 6.8, anchor="start"))
    o.append(T(104, 181, "−V", 6.8, anchor="start"))
    o.append(T(244, 114, "V<sub>Z</sub>", 6.8, anchor="end"))
    o.append(T(212, 216, "Zener current", 6.8, anchor="start"))
    o.append(_lead(288, 212, 251, 214))
    o.append(T(438, 148, "Diode", 6.8, anchor="start"))
    o.append(T(438, 157, "direction", 6.8, anchor="start"))
    o.append(T(596, 181, "V", 6.8, anchor="end"))
    o.append(T(556, 184, "Voltage", 6.8, anchor="end"))
    o.append(T(356, 181, "V<sub>F</sub>", 6.8, anchor="start"))

    o.append(T(340, 272, "V<sub>F</sub> = Forward diode voltage (usually 0.5–0.8 V),", 6.8, color=INK))
    o.append(T(340, 284, "V<sub>Z</sub> = Zener or avalanche breakdown voltage (3–100 + V)", 6.8, color=INK))

    return _fig(svg(w, h, "".join(o), esc("Fig. 13.29")),
                "Hình 13.29 · Đặc tính điển hình của diode zener (sụp đổ thác lũ)",
                "Figure 13.29 · Typical zener (avalanche) diode characteristics",
                "Đồ thị dòng I theo điện áp V với hai trục cắt nhau tại gốc tọa độ. Nhánh thuận "
                "nằm sát trục hoành từ gốc tới ngưỡng V_F rồi dựng đứng lên phía trên, được ghi "
                "là Diode current; nhánh zener nằm sát trục hoành sang trái tới ngưỡng V_Z rồi "
                "đổ thẳng xuống dưới, được ghi là Zener current. Cạnh trái của đồ thị mang nhãn "
                "Zener direction và mốc −V, cạnh phải mang nhãn Diode direction, V và Voltage; "
                "trục dọc có mốc I ở trên và −I ở dưới. Hai dòng chú thích dưới cùng định nghĩa "
                "V_F là điện áp diode thuận, thường 0,5–0,8 V và kết thúc bằng dấu phẩy, còn V_Z "
                "là điện áp phá hủy zener hoặc thác lũ, 3–100 + V",
                "Current I against voltage V with the axes crossing at the origin. The forward "
                "branch follows the horizontal axis to the V_F threshold and then rises steeply "
                "upward, labelled Diode current; the zener branch follows the axis to the left "
                "to V_Z and then drops vertically downward, labelled Zener current. The left "
                "side is marked Zener direction and −V, the right side Diode direction, V and "
                "Voltage, while the vertical axis carries I above and −I below. Two footnotes "
                "define V_F as the forward diode voltage, usually 0.5–0.8 V and ending with a "
                "comma, and V_Z as the zener or avalanche breakdown voltage, 3–100 + V")


# ------------------------------------------------------------------ 13.30

@_reg
def fig_f1330():
    """Figure 13.30 - zener barrier circuit and its output characteristic."""
    w, h = 680, 360
    o = [_defs(), _rect(0, 0, w, h, fill=PAPER, sw=0)]
    _title(o, 30, "Cấu hình hàng rào zener điển hình",
           "Typical zener barrier configuration", 7.2)
    _sub(o, "Sơ đồ mạch và đặc tính đầu ra · Z1, Z2, F1, R1, R2 / Circuit and barrier output "
            "characteristic")

    # ---- circuit
    o.append(_line(150, 75, 530, 75, sw=1.2))
    o.append(_line(150, 145, 530, 145, sw=1.2))
    for yy in (75, 145):
        o.append(_circle(150, yy, 3.2, fill="#ffffff", sw=1.1))
        o.append(_circle(530, yy, 3.2, fill="#ffffff", sw=1.1))

    o.append(_fuse_h(190, 75))
    o.append(T(200, 60, "Protective", 6.8))
    o.append(T(200, 69, "fuse", 6.8))
    o.append(T(200, 90, "F1", 6.8))

    o.append(_res_h(250, 300, 75))
    o.append(T(275, 50, "Current limiting", 6.8))
    o.append(T(275, 59, "resistor", 6.8))
    o.append(T(275, 90, "R1", 6.8))

    o.append(_res_h(392, 442, 75))
    o.append(T(417, 50, "Current limiting", 6.8))
    o.append(T(417, 59, "resistor", 6.8))
    o.append(T(417, 90, "R2", 6.8))

    o.append(_zener_v(232, 75, 145))
    o.append(_zener_v(350, 75, 145))
    o.append(T(291, 116, "Zener", 6.8))
    o.append(T(291, 125, "diodes", 6.8))
    o.append(T(232, 163, "Z1 (Note 1)", 6.8))
    o.append(T(350, 163, "Z2 (Note 1)", 6.8))
    o.append(_earth(300, 145))

    o.append(T(36, 96, "Non-hazardous", 6.8, anchor="start"))
    o.append(T(36, 105, "area circuit", 6.8, anchor="start"))
    o.append(T(36, 114, "terminals", 6.8, anchor="start"))
    o.append(T(546, 96, "Intrinsically", 6.8, anchor="start"))
    o.append(T(546, 105, "safe circuit", 6.8, anchor="start"))
    o.append(T(546, 114, "terminals", 6.8, anchor="start"))
    o.append(T(300, 179, "Single infallible or 2 separate", 6.8))
    o.append(T(300, 188, "earth connections (Note 2)", 6.8))

    # ---- barrier output characteristic
    o.append(_arrow(150, 288, 500, 288, sw=1.1))
    o.append(_arrow(150, 288, 150, 214, sw=1.1))
    o.append(T(150, 207, "V", 6.8))
    o.append(_rect(150, 224, 280, 64, fill="url(#h6)", sw=1.1))
    o.append(T(140, 228, "V<sub>2</sub>", 6.8, anchor="end"))
    o.append(T(140, 266, "V<sub>1</sub>", 6.8, anchor="end"))
    o.append(T(140, 291, "0", 6.8, anchor="end"))
    o.append(T(290, 304, "Barrier output characteristic", 6.8, color=INK))
    o.append(T(290, 319, "V<sub>2</sub> = Maximum zener voltage of Z1 or Z2, whichever is greater", 6.8))

    return _fig(svg(w, h, "".join(o), esc("Fig. 13.30")),
                "Hình 13.30 · Cấu hình hàng rào zener điển hình. Ghi chú: (1) Cả Z1 và Z2 đều được "
                "chọn sao cho không bị hư hỏng trong thời gian trước khi cầu chì cắt khi có điện áp "
                "vào lớn nhất (điện lưới). (2) Nếu nối đất là dây thì tiết diện dẫn phải ít nhất "
                "4 mm²",
                "Figure 13.30 · Typical zener barrier configuration. Notes: (1) Both Z1 and Z2 are "
                "chosen so that they will not suffer damage during fuse pre-arcing period when "
                "maximum (mains) input voltage is applied. (2) If earth connection is a wire it "
                "must be of at least 4 mm² conductor cross section",
                "Nửa trên là sơ đồ mạch: từ cặp cực đầu vào vùng không nguy hiểm, dây dẫn qua cầu "
                "chì F1, điện trở R1 và R2 tới cặp cực mạch an toàn nội tại. Hai diode zener Z1 và "
                "Z2 mắc song song từ dây trên xuống dây dưới, dây dưới nối đất bằng một nối đất "
                "không hỏng hoặc hai nối đất riêng. Nửa dưới là đồ thị đặc tính đầu ra có trục "
                "điện áp V và vùng bị giới hạn giữa hai mức V1 và V2, với chú thích V2 là điện áp "
                "zener cực đại của Z1 hoặc Z2, whichever is greater. Caption in gốc có hai ghi chú "
                "về chọn zener chịu được thời gian trước khi cầu chì cắt và tiết diện dây nối đất "
                "tối thiểu 4 mm²",
                "The upper half is the circuit: from the non-hazardous input terminals the top "
                "conductor runs through protective fuse F1, resistor R1 and resistor R2 to the "
                "intrinsically safe terminals. Two zener diodes Z1 and Z2 shunt the top conductor "
                "to the lower earth conductor, which is connected by a single infallible or two "
                "separate earth connections. The lower half is the barrier output characteristic: "
                "a voltage axis V with a hatched output region bounded by V1 and V2, and the note "
                "that V2 is the maximum zener voltage of Z1 or Z2, whichever is greater. The "
                "printed caption carries two Notes about choosing both zeners to survive fuse "
                "pre-arcing and about a minimum 4 mm² earth wire")


# ------------------------------------------------------------------ 13.31

@_reg
def fig_f1331():
    """Figure 13.31 - typical barrier mounting system on an earth bar."""
    w, h = 680, 300
    o = [_defs(), _rect(0, 0, w, h, fill=PAPER, sw=0)]
    _title(o, 31, "Hệ thống lắp đặt hàng rào điển hình", "Typical barrier mounting system", 7.2)
    _sub(o, "Lắp lệch một đầu vào thanh nối đất / Asymmetric mounting on the earth bar")

    # Barrier body and its two ascending cables.
    o.append(_rect(120, 122, 450, 42, fill="#eef3fb", sw=1.3))
    o.append(T(345, 148, "Barrier device", 7.6, color=INK, weight="600"))
    o.append(_path("M338 122 C326 96 354 92 346 68", fill="none", sw=1.2))
    o.append(_path("M386 122 C374 94 402 90 394 64", fill="none", sw=1.2))
    o.append(_line(342, 68, 350, 68, sw=1.2))
    o.append(_line(390, 64, 398, 64, sw=1.2))

    # Earth bar below the barrier.
    o.append(_rect(80, 178, 520, 18, fill="url(#h6)", sw=1.1))
    o.append(_line(80, 196, 600, 196, sw=1.0))
    o.append(T(88, 214, "Earth bar", 6.8, anchor="start"))
    o.append(_lead(126, 210, 112, 188))

    # Asymmetric bolt plate at the left-hand end.
    o.append(_poly([(142, 164), (196, 164), (182, 214), (128, 214)],
                   fill="#dedede", sw=1.1, close=True))
    for xx, yy in ((152, 172), (178, 172), (146, 204), (172, 204)):
        o.append(_circle(xx, yy, 3, fill="#ffffff", sw=0.9))
    o.append(T(250, 230, "Bolts fixing barrier asymmetrically", 6.8))
    o.append(T(250, 240, "to earth bar and forming infallible", 6.8))
    o.append(T(250, 250, "earth connection", 6.8))
    o.append(_lead(246, 224, 180, 184))

    # Terminal cluster at the right-hand end.
    for yy in (134, 148):
        o.append(_circle(574, yy, 3, fill="#ffffff", sw=1.0))
    o.append(T(462, 220, "Circuit connection", 6.8, anchor="start"))
    o.append(T(462, 230, "terminals (one may be", 6.8, anchor="start"))
    o.append(T(462, 240, "an earth terminal)", 6.8, anchor="start"))
    o.append(_lead(558, 215, 574, 152))

    o.append(T(340, 274, "Lắp lệch giúp không thể lặp ngược hàng rào lên thanh nối đất", 6.8, color=GREY))

    return _fig(svg(w, h, "".join(o), esc("Fig. 13.31")),
                "Hình 13.31 · Hệ thống lắp đặt hàng rào điển hình",
                "Figure 13.31 · Typical barrier mounting system",
                "Một thiết bị hàng rào dạng hộp dài nằm ngang trên thanh nối đất gạch chéo. Hai "
                "dây cáp đi lên từ mặt trên của hộp. Ở đầu trái, một tấm bắt vít lệch tâm với bốn "
                "vít gắn hộp vào thanh nối đất, tạo nối đất không hỏng; nhãn ở dưới ghi Bolts "
                "fixing barrier asymmetrically to earth bar and forming infallible earth "
                "connection. Ở đầu phải có cụm cực nối dây gồm hai điểm, được ghi là Circuit "
                "connection terminals (one may be an earth terminal). Nhãn Earth bar chỉ vào tấm "
                "lắp bên trái, và nhãn Barrier device nằm giữa thân hộp",
                "A long rectangular barrier device sits horizontally on a hatched earth bar with "
                "two cables rising from its top. At the left end an asymmetric bolted plate with "
                "four bolts fixes the barrier to the earth bar and forms the infallible earth "
                "connection, captioned Bolts fixing barrier asymmetrically to earth bar and "
                "forming infallible earth connection. At the right end a cluster of two circuit "
                "terminals is labelled Circuit connection terminals (one may be an earth "
                "terminal). The label Earth bar points to the left mounting plate and Barrier "
                "device is centred on the body")


# ------------------------------------------------------------------ 13.32

@_reg
def fig_f1332():
    """Figure 13.32 - four typical zener barrier configurations."""
    w, h = 680, 600
    o = [_defs(), _rect(0, 0, w, h, fill=PAPER, sw=0)]
    _title(o, 32, "Các cấu hình hàng rào zener điển hình", "Typical zener barrier configurations", 7.2)
    _sub(o, "Bốn cấu hình kênh đơn, hai kênh và chuỗi diode · phương trình đầu ra ở bên phải / "
            "Four configurations with output equations")

    # ---- diagram 1: single channel
    o.append(T(40, 48, "(1)", 6.8, anchor="start", color=GREY))
    o.append(_line(48, 70, 352, 70, sw=1.1))
    o.append(_line(48, 135, 352, 135, sw=1.1))
    o.append(T(40, 74, "+", 6.8, anchor="end"))
    o.append(T(40, 139, "−", 6.8, anchor="end"))
    o.append(_fuse_h(72, 70, 18))
    o.append(T(81, 62, "F1", 6.8))
    o.append(_res_h(140, 185, 70))
    o.append(T(162, 62, "R1", 6.8))
    o.append(_res_h(255, 300, 70))
    o.append(T(277, 62, "R2", 6.8))
    o.append(_zener_v(112, 70, 135))
    o.append(T(112, 155, "Z1", 6.8))
    o.append(_zener_v(222, 70, 135))
    o.append(T(222, 155, "Z2", 6.8))
    o.append(_earth(222, 135))
    o.append(T(362, 100, "V<sub>O/C</sub>", 6.8, anchor="start"))
    o.append(T(362, 125, "I<sub>S/C</sub>", 6.8, anchor="start"))

    o.append(T(400, 72, "V<sub>O/C</sub> = +V<sub>Z</sub>", 6.8, anchor="start"))
    o.append(T(400, 84, "or −V<sub>DIODE</sub>", 6.8, anchor="start"))
    o.append(T(400, 102, "I<sub>S/C</sub> = +V<sub>Z</sub>/R", 6.8, anchor="start"))
    o.append(T(400, 114, "or −V<sub>DIODE</sub>/R", 6.8, anchor="start"))

    # ---- diagram 2: dual channel, four zeners per side
    o.append(T(40, 168, "(2)", 6.8, anchor="start", color=GREY))
    o.append(_line(48, 184, 352, 184, sw=1.1))
    o.append(_line(48, 278, 352, 278, sw=1.1))
    o.append(_circle(48, 184, 3, fill="#ffffff", sw=1.0))
    o.append(_circle(48, 278, 3, fill="#ffffff", sw=1.0))
    o.append(_fuse_h(62, 184, 16))
    o.append(_fuse_h(62, 278, 16))
    o.append(T(70, 174, "F1/1", 6.8))
    o.append(T(70, 296, "F1/2", 6.8))
    o.append(_res_h(112, 154, 184))
    o.append(_res_h(112, 154, 278))
    o.append(T(133, 174, "R1/1", 6.8))
    o.append(T(133, 296, "R1/2", 6.8))
    o.append(_res_h(266, 308, 184))
    o.append(_res_h(266, 308, 278))
    o.append(T(287, 174, "R2/1", 6.8))
    o.append(T(287, 296, "R2/2", 6.8))
    for i in range(4):
        y0 = 184 + i * 21
        y1 = 205 + i * 21
        o.append(_zener_v(180, y0, y1))
        o.append(T(180, y1 + 7, "Z1/%d" % (i + 1), 6.8))
        o.append(_zener_v(228, y0, y1))
        o.append(T(228, y1 + 7, "Z2/%d" % (i + 1), 6.8))
    o.append(_earth(204, 278))
    o.append(T(350, 224, "V<sub>E</sub>", 6.8, anchor="start"))
    o.append(T(350, 240, "I<sub>E</sub>", 6.8, anchor="start"))
    o.append(T(350, 264, "V<sub>O/C</sub>", 6.8, anchor="start"))
    o.append(T(350, 280, "I<sub>S/C</sub>", 6.8, anchor="start"))

    o.append(T(400, 187, "V<sub>O/C</sub> = 2V<sub>Z</sub> + 2V<sub>DIODE</sub>", 6.8, anchor="start"))
    o.append(T(400, 199, "V<sub>E</sub> = ±V<sub>Z</sub> + V<sub>DIODE</sub>", 6.8, anchor="start"))
    o.append(T(400, 217, "I<sub>S/C</sub> = 2V<sub>Z</sub> + 2V<sub>DIODE</sub>/ 2 R₂", 6.8, anchor="start"))
    o.append(T(400, 235, "I<sub>E</sub> = ±V<sub>Z</sub> + V<sub>DIODE</sub>/ R₂", 6.8, anchor="start"))
    o.append(T(400, 247, "or ± 2(V<sub>Z</sub> + V<sub>DIODE</sub>)/R₂", 6.8, anchor="start"))
    o.append(T(400, 259, "(Note 1)", 6.8, anchor="start"))
    o.append(T(356, 311, "Note 1: Both channels can feed current to earth in parallel if field wiring is s/c",
              6.8, anchor="start"))

    # ---- diagram 3: dual channel, cross-connected diodes
    o.append(T(40, 332, "(3)", 6.8, anchor="start", color=GREY))
    o.append(_line(48, 348, 352, 348, sw=1.1))
    o.append(_line(48, 442, 352, 442, sw=1.1))
    o.append(_circle(48, 348, 3, fill="#ffffff", sw=1.0))
    o.append(_circle(48, 442, 3, fill="#ffffff", sw=1.0))
    o.append(_fuse_h(62, 348, 16))
    o.append(_fuse_h(62, 442, 16))
    o.append(_res_h(120, 160, 348))
    o.append(_res_h(250, 290, 442))
    o.append(T(140, 338, "R1/1", 6.8))
    o.append(T(270, 460, "R2/2", 6.8))
    o.append(_zener_v(120, 348, 390))
    o.append(_zener_v(120, 400, 442))
    o.append(T(120, 404, "Z1/1", 6.8))
    o.append(T(120, 455, "Z1/3", 6.8))
    o.append(_zener_v(250, 348, 390))
    o.append(_zener_v(250, 400, 442))
    o.append(T(250, 404, "Z2/1", 6.8))
    o.append(T(250, 455, "Z2/3", 6.8))
    o.append(_line(120, 392, 250, 392, sw=1.0))
    o.append(_diode_left(168, 392))
    o.append(_diode_left(208, 392))
    o.append(T(168, 414, "Z1/2", 6.8))
    o.append(T(208, 414, "Z2/2", 6.8))
    o.append(_earth(185, 442))
    o.append(T(350, 386, "V<sub>E</sub>", 6.8, anchor="start"))
    o.append(T(350, 402, "I<sub>E</sub>", 6.8, anchor="start"))
    o.append(T(350, 428, "V<sub>O/C</sub>", 6.8, anchor="start"))
    o.append(T(350, 444, "I<sub>S/C</sub>", 6.8, anchor="start"))

    o.append(T(400, 351, "V<sub>E</sub> = V<sub>O/C</sub> = ±V<sub>Z</sub> + V<sub>DIODE</sub>", 6.8, anchor="start"))
    o.append(T(400, 369, "I<sub>S/C</sub> = ±V<sub>Z</sub> + V<sub>DIODE</sub>/ 2 R₂", 6.8, anchor="start"))
    o.append(T(400, 387, "I<sub>E</sub> = V<sub>Z</sub> + V<sub>DIODE</sub>/ R₂", 6.8, anchor="start"))
    o.append(T(400, 399, "or 2(V<sub>Z</sub> + V<sub>DIODE</sub>/R₁)", 6.8, anchor="start"))
    o.append(T(400, 411, "(Note 1)", 6.8, anchor="start"))
    o.append(T(356, 473, "Note 1: Both channels can feed current to earth in parallel if field wiring",
              6.8, anchor="start"))
    o.append(T(356, 483, "is short circuit.", 6.8, anchor="start"))

    # ---- diagram 4: series diode string
    o.append(T(40, 508, "(4)", 6.8, anchor="start", color=GREY))
    o.append(_line(48, 524, 352, 524, sw=1.1))
    o.append(_line(48, 590, 352, 590, sw=1.1))
    o.append(_circle(48, 524, 3, fill="#ffffff", sw=1.0))
    o.append(_circle(48, 590, 3, fill="#ffffff", sw=1.0))
    for xx in (92, 132):
        o.append(_fuse_h(xx, 524, 16))
    o.append(_res_h(176, 214, 524))
    for xx in (258, 288, 318):
        o.append(_diode_left(xx, 524))
    o.append(_zener_v(132, 524, 590))
    o.append(_zener_v(214, 524, 590))
    o.append(_earth(214, 590))
    o.append(T(362, 552, "V<sub>O/C</sub>", 6.8, anchor="start"))
    o.append(T(362, 576, "I<sub>S/C</sub>", 6.8, anchor="start"))

    o.append(T(400, 533, "V<sub>O/C</sub> = V<sub>Z</sub> or V<sub>DIODE</sub>", 6.8, anchor="start"))
    o.append(T(400, 551, "I<sub>S/C</sub> = 0 (Effectively)", 6.8, anchor="start"))

    return _fig(svg(w, h, "".join(o), esc("Fig. 13.32")),
                "Hình 13.32 · Các cấu hình hàng rào zener điển hình",
                "Figure 13.32 · Typical zener barrier configurations",
                "Bốn sơ đồ hàng rào xếp dọc. (1) Một kênh có cầu chì F1, các điện trở R1, R2 và "
                "hai zener Z1, Z2, với V_O/C bằng +V_Z hoặc −V_DIODE và I_S/C bằng +V_Z/R hoặc "
                "−V_DIODE/R. (2) Hai kênh, mỗi bên bốn zener Z1/1 đến Z1/4 và Z2/1 đến Z2/4, "
                "các phương trình cho điện áp đầu ra 2V_Z + 2V_DIODE và dòng ngắn mạch chia cho "
                "2 R₂, kèm Note 1 kết thúc bằng s/c. (3) Hai kênh, mỗi bên hai zener được nối chéo "
                "qua hai diode Z1/2 và Z2/2, V_E bằng V_O/C, và phương trình cuối in R₁ thay vì "
                "R₂, kèm Note 1 kết thúc bằng short circuit. (4) Chuỗi ba diode mắc nối tiếp "
                "sau các zener, V_O/C bằng V_Z hoặc V_DIODE và I_S/C bằng 0 (Effectively)",
                "Four barrier circuits stacked vertically. (1) A single channel with fuse F1, "
                "resistors R1 and R2 and zeners Z1 and Z2, giving V_O/C of +V_Z or −V_DIODE and "
                "I_S/C of +V_Z/R or −V_DIODE/R. (2) A dual channel with four zeners per side, "
                "Z1/1 to Z1/4 and Z2/1 to Z2/4, output voltage 2V_Z + 2V_DIODE and short-circuit "
                "current divided by 2 R₂, followed by Note 1 ending in s/c. (3) A dual channel "
                "with two zeners per side cross-connected by diodes Z1/2 and Z2/2, V_E equal to "
                "V_O/C, and a last equation printing R₁ instead of R₂, followed by Note 1 ending "
                "in short circuit. (4) A string of three series diodes after the zeners, with "
                "V_O/C equal to V_Z or V_DIODE and I_S/C equal to 0 (Effectively)")


# ------------------------------------------------------------------ 13.33

@_reg
def fig_f1333():
    """Figure 13.33 - cable stored energy characteristic."""
    w, h = 680, 400
    o = [_defs(), _rect(0, 0, w, h, fill=PAPER, sw=0)]
    _title(o, 33, "Đặc tính năng lượng tích trữ của cáp", "Cable stored energy characteristic", 7.2)
    _sub(o, "Nguồn, cáp và đồ thị năng lượng theo điện trở cáp / Source, external circuit and energy curve")

    # ---- circuit
    o.append(_line(90, 76, 500, 76, sw=1.2))
    o.append(_line(90, 146, 500, 146, sw=1.2))
    o.append(_line(90, 76, 90, 103, sw=1.2))
    o.append(_line(90, 119, 90, 146, sw=1.2))
    o.append(_line(80, 103, 100, 103, sw=1.6))
    o.append(_line(84, 119, 96, 119, sw=1.6))
    o.append(T(76, 116, "V", 6.8, anchor="end"))
    o.append(_res_h(138, 178, 76))
    o.append(T(158, 66, "R", 6.8))
    o.append(_line(210, 60, 210, 152, sw=0.9, dash="4 4", color=GREY))
    o.append(_coil_h(300, 76, 40))
    o.append(T(320, 66, "L<sub>0</sub>", 6.8))
    o.append(_res_h(390, 430, 76))
    o.append(T(410, 66, "R<sub>0</sub>", 6.8))
    o.append(T(150, 158, "Source", 6.8))
    o.append(T(350, 158, "External circuit", 6.8))

    o.append(T(340, 184, "Stored energy for any cable length = 1/2 L (V/(R + R<sub>0</sub>))²", 6.8, color=INK))

    # ---- energy curve: E is proportional to R0/(R+R0)^2 and peaks at R0 = R
    x0, y0, W, H = 140, 335, 360, 100
    o.append(_arrow(x0, y0, x0 + W + 16, y0, sw=1.1))
    o.append(_arrow(x0, y0, x0, y0 - H - 12, sw=1.1))
    pts = []
    xpeak, ypeak = 0.0, 0.0
    for i in range(81):
        xv = 2.2 * i / 80.0
        val = 4.0 * xv / ((1.0 + xv) ** 2)
        px = x0 + xv / 2.2 * W
        py = y0 - val / 1.05 * H
        pts.append((px, py))
        if abs(xv - 1.0) < 0.02:
            xpeak, ypeak = px, py
    o.append(_poly(pts, fill="none", sw=1.8, color=BLUE))
    o.append(_line(x0, ypeak, xpeak + 20, ypeak, sw=0.9, dash="4 3", color=GREY))
    o.append(_line(xpeak, ypeak, xpeak, y0 + 4, sw=0.9, dash="4 3", color=GREY))
    o.append(T(132, 211, "1/2 L (V/(R + R<sub>0</sub>))²", 6.8, anchor="end"))
    o.append(T(344, 238, "Maximum external circuit", 6.8, anchor="start"))
    o.append(T(344, 248, "stored energy", 6.8, anchor="start"))
    o.append(T(132, 339, "0", 6.8, anchor="end"))
    o.append(T(xpeak, 350, "R<sub>0</sub> = R", 6.8))
    o.append(T(512, 350, "R<sub>c</sub>", 6.8, anchor="end"))

    return _fig(svg(w, h, "".join(o), esc("Fig. 13.33")),
                "Hình 13.33 · Đặc tính năng lượng tích trữ của cáp",
                "Figure 13.33 · Cable stored energy characteristic",
                "Nửa trên là mạch nối tiếp gồm nguồn V và điện trở R ở phía nguồn, sau một đường "
                "chia đứt nét là phần mạch ngoài với cuộn cảm L0 và điện trở cáp R0. Dòng công "
                "thức giữa hình ghi năng lượng tích trữ của mọi chiều dài cáp bằng 1/2 L nhân "
                "bình phương của V chia cho R + R0. Đồ thị dưới có trục hoành Rc và trục tung là "
                "1/2 L (V/(R + R0))²; đường cong đi lên từ gốc tọa độ tới đỉnh tại Rc bằng R rồi "
                "đi xuống, với đường ngang đứt nét đánh dấu năng lượng tích trữ cực đại của mạch "
                "ngoài và đường đứng đứt nét tại R0 = R",
                "The upper circuit is a series loop: source V and resistor R on the source side, "
                "then past a dashed divider the external circuit with inductance L0 and cable "
                "resistance R0. The centred formula states that the stored energy for any cable "
                "length is 1/2 L (V/(R + R0)) squared. The lower graph has a horizontal Rc axis "
                "and a vertical 1/2 L (V/(R + R0)) squared axis; the curve rises from the origin "
                "to a peak at Rc equal to R and then falls, with a dashed horizontal line marking "
                "the maximum external circuit stored energy and a dashed vertical line at R0 = R")


# ------------------------------------------------------------------ 13.34

@_reg
def fig_f1334():
    """Figure 13.34 - calculation of the L/R ratio for source, cable and receptor."""
    w, h = 680, 330
    o = [_defs(), _rect(0, 0, w, h, fill=PAPER, sw=0)]
    _title(o, 34, "Tính tỉ số L/R", "Calculation of L/R ratio", 7.2)
    _sub(o, "Nguồn, cáp và thiết bị nhận · các thông số tập trung và phân bố / Source, cable and "
            "receptor parameters")

    # ---- series loop
    o.append(_line(70, 92, 600, 92, sw=1.2))
    o.append(_line(70, 170, 600, 170, sw=1.2))
    o.append(_line(70, 92, 70, 104, sw=1.2))
    o.append(_line(70, 158, 70, 170, sw=1.2))
    o.append(_circle(70, 104, 3.2, fill="#ffffff", sw=1.1))
    o.append(_circle(70, 158, 3.2, fill="#ffffff", sw=1.1))
    o.append(T(58, 136, "V", 6.8, anchor="end"))
    o.append(_line(250, 70, 250, 188, sw=0.9, dash="4 4", color=GREY))
    o.append(_line(450, 70, 450, 188, sw=0.9, dash="4 4", color=GREY))

    o.append(_coil_h(100, 92, 40))
    o.append(T(120, 82, "L<sub>s</sub>", 6.8))
    o.append(_res_h(158, 198, 92))
    o.append(T(178, 82, "R<sub>s</sub>", 6.8))
    o.append(_coil_h(300, 92, 40))
    o.append(T(320, 82, "L<sub>0</sub>", 6.8))
    o.append(_res_h(370, 410, 92))
    o.append(T(390, 82, "R<sub>0</sub>", 6.8))
    o.append(_line(600, 92, 600, 116, sw=1.2))
    o.append(_coil_v(600, 116, 140))
    o.append(T(614, 130, "L<sub>1</sub>", 6.8, anchor="start"))
    o.append(_res_v(600, 140, 164))
    o.append(T(614, 158, "R<sub>1</sub>", 6.8, anchor="start"))
    o.append(_line(600, 164, 600, 170, sw=1.2))

    o.append(T(160, 202, "Source", 6.8))
    o.append(T(160, 211, "(associated", 6.8))
    o.append(T(160, 220, "apparatus)", 6.8))
    o.append(T(350, 202, "Cable", 6.8))
    o.append(T(530, 202, "Receptor", 6.8))
    o.append(T(530, 211, "(intrinsically", 6.8))
    o.append(T(530, 220, "safe apparatus)", 6.8))

    key = ["L<sub>s</sub> = Source lumped inductance (fixed)",
           "L<sub>i</sub> = Reception lumped inductance (fixed)",
           "L<sub>0</sub> = Cable capacity (varies with length)",
           "R<sub>s</sub> = Source resistance (fixed)",
           "R<sub>i</sub> = Reception resistance (fixed)",
           "R<sub>0</sub> = Cable resistance (varies with length)",
           "V = Source voltage"]
    for i, line in enumerate(key):
        o.append(T(60, 242 + i * 11, line, 6.8, anchor="start"))

    return _fig(svg(w, h, "".join(o), esc("Fig. 13.34")),
                "Hình 13.34 · Tính tỉ số L/R",
                "Figure 13.34 · Calculation of L/R ratio",
                "Sơ đồ mạch một vòng gồm nguồn V ở bên trái, cuộn cảm Ls và điện trở Rs cố định "
                "trong thiết bị nguồn, cuộn cảm L0 và điện trở R0 thay đổi theo chiều dài trong "
                "đoạn cáp, và cuộn cảm L1 cùng điện trở R1 ở thiết bị nhận bên phải. Hai đường đứt "
                "nét chia sơ đồ thành ba vùng có nhãn Source, Cable và Receptor. Bảng chú giải bảy "
                "dòng dưới hình định nghĩa lần lượt Ls, Li, L0, Rs, Ri, R0 và V; dòng thứ ba in "
                "nguyên văn Cable capacity (varies with length), dù ký hiệu là L0, và các chỉ số "
                "của thiết bị nhận trong chú giải là chữ i",
                "A single series loop with source voltage V on the left, fixed inductance Ls and "
                "resistance Rs in the associated apparatus, cable inductance L0 and resistance "
                "R0 that vary with length, and inductance L1 with resistance R1 in the receptor "
                "on the right. Two dashed dividers separate the regions labelled Source, Cable "
                "and Receptor. A seven-line key defines Ls, Li, L0, Rs, Ri, R0 and V; line three "
                "prints Cable capacity (varies with length) even though the symbol is L0, and "
                "the receptor subscripts in the key are the letter i")


# ------------------------------------------------------------------ 13.35

@_reg
def fig_f1335():
    """Figure 13.35 - L/R for a constant current voltage limited supply."""
    w, h = 680, 390
    o = [_defs(), _rect(0, 0, w, h, fill=PAPER, sw=0)]
    _title(o, 35, "Tính L/R cho nguồn điện dòng không đổi, giới hạn điện áp",
           "Calculation of L/R for constant current voltage limited power supply", 6.8)

    # ---- supply envelope graph
    x0, y0 = 140, 215
    o.append(_arrow(x0, y0, 566, y0, sw=1.1))
    o.append(_arrow(x0, y0, x0, 62, sw=1.1))
    o.append(_line(140, 120, 370, 120, sw=1.0))
    o.append(_line(370, 120, 370, 215, sw=1.0))
    o.append(_rect(140, 120, 230, 95, fill="url(#h6)", sw=1.1))
    o.append(_line(140, 75, 555, 215, sw=1.0, dash="5 4", color=GREY))

    o.append(T(132, 124, "I", 6.8, anchor="end"))
    o.append(T(132, 79, "2I", 6.8, anchor="end"))
    o.append(T(132, 219, "0", 6.8, anchor="end"))
    o.append(T(370, 232, "V", 6.8))
    o.append(T(555, 232, "2V", 6.8))
    o.append(T(400, 112, "Equivalent load line", 6.8, anchor="start"))
    o.append(T(400, 122, "for L/R calculation", 6.8, anchor="start"))
    o.append(_lead(452, 126, 452, 157))
    o.append(T(44, 163, "Envelope of", 6.8, anchor="start"))
    o.append(T(44, 172, "power supply", 6.8, anchor="start"))
    o.append(_lead(124, 168, 144, 166))
    o.append(T(232, 234, "Power supply", 6.8, anchor="start"))
    o.append(T(232, 244, "characteristic", 6.8, anchor="start"))
    o.append(_lead(288, 230, 290, 214))

    # ---- equivalent circuit
    o.append(T(385, 278, "Equivalent circuit", 6.8))
    o.append(_circle(300, 298, 3.2, fill="#ffffff", sw=1.1))
    o.append(_circle(300, 342, 3.2, fill="#ffffff", sw=1.1))
    o.append(T(284, 320, "2V", 6.8, anchor="end"))
    o.append(_line(300, 298, 370, 298, sw=1.1))
    o.append(_res_h(370, 420, 298))
    o.append(_line(420, 298, 470, 298, sw=1.1))
    o.append(_circle(470, 298, 3.2, fill="#ffffff", sw=1.1))
    o.append(_line(300, 342, 470, 342, sw=1.1))
    o.append(_circle(470, 342, 3.2, fill="#ffffff", sw=1.1))
    o.append(T(395, 288, "V", 6.8))
    o.append(T(395, 310, "I", 6.8))
    o.append(T(385, 358, "Equivalent circuit used for L/R calculations", 6.8, color=INK))
    o.append(T(340, 378, "Đường tải tương đương tiếp xúc bao của nguồn tại góc trên của vùng V, I",
              6.8, color=GREY))

    return _fig(svg(w, h, "".join(o), esc("Fig. 13.35")),
                "Hình 13.35 · Tính L/R cho nguồn điện áp không đổi, dòng không đổi",
                "Figure 13.35 · Calculation of L/R for constant current voltage limited power supply",
                "Đồ thị trên có trục điện áp đến V và 2V, trục dòng đến I và 2I. Một hình chữ nhật "
                "gạch chéo từ gốc tới V và I là bao của nguồn, có nhãn Envelope of power supply "
                "ở cạnh trái và Power supply characteristic ở cạnh dưới. Đường đứt nét từ 2I trên "
                "trục dọc tới 2V trên trục hoành là đường tải tương đương dùng tính L/R, chạm "
                "vào góc trên bên phải của vùng gạch chéo. Bên dưới là mạch tương đương gồm nguồn "
                "2V và một điện trở mang nhãn V trên I giữa hai cực hở, với dòng ghi Equivalent "
                "circuit used for L/R calculations",
                "The upper graph has a voltage axis reaching V and 2V and a current axis reaching "
                "I and 2I. A hatched rectangle from the origin to V and I is the envelope of the "
                "power supply, with Envelope of power supply at its left edge and Power supply "
                "characteristic along its lower edge. A dashed line from 2I on the vertical axis "
                "to 2V on the horizontal axis is the equivalent load line used for the L/R "
                "calculation, tangent to the upper right corner of the hatched region. Below, an "
                "equivalent circuit shows a 2V source with a resistor marked V over I between "
                "two open terminals, captioned Equivalent circuit used for L/R calculations")
