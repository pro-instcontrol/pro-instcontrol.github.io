# -*- coding: utf-8 -*-
"""Vector redraws of Figures 12.9-12.12 in A. McMillan, *Electrical
Installations in Hazardous Areas*, Chapter 12 "Protection concept increased
safety 'e'".

Every drawing is a simplified vector redraw of the authoritative rendered
pages p332, p333, p335 and p341.  Printed English captions (including the
Notes of Figs 12.10 and 12.11) are reproduced verbatim in the returned
English captions/ARIA text and drawn bilingually on the canvas.  Each public
callable returns the standard five-tuple through ``vfig._fig()`` on a
680-wide canvas and is registered in ``FIGS`` by the ``_reg`` decorator.
"""
import sys
import os

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

from vfig import (_defs, _fig, _line, _rect, _txt, _arrow, _circle, _poly, svg,
                  GREY, INK, PAPER, BLUE, RED, GREEN)

FIGS = {}


def _reg(f):
    FIGS[f.__name__] = f()
    return f


def esc(s):
    """Every displayed string is literal Unicode with XML metacharacters escaped."""
    return (str(s).replace("&", "&amp;").replace("<", "&lt;")
            .replace(">", "&gt;"))


def T(x, y, s, size=6.8, **kw):
    """Plain text: vet first, then delegate to vfig._txt()."""
    return _txt(x, y, esc(s), size, **kw)


# ------------------------------------------------------------------ helpers

CREEP = RED
CLEAR = BLUE
INSFILL = "#f3ead6"


def _title(o, n, vi, en):
    o.append(T(340, 14, "Hình 12.%d · %s" % (n, vi), 7.8, weight="600"))
    o.append(T(340, 24, "Figure 12.%d · %s" % (n, en), 7.0, color=GREY))


def _hatch(x, y, w, h, step=7, color="#9a9a9a", sw=0.6):
    """Explicit diagonal hatch strokes clipped to a rectangle."""
    o = []
    n = int((w + h) / step) + 1
    for i in range(n + 1):
        x1 = x + i * step
        xa, xb = max(x, x1 - h), min(x + w, x1)
        if xb > xa:
            o.append(_line(xb, y, xa, y + h, sw=sw, color=color))
    return "".join(o)


def _dimh(x1, x2, y, label, color=INK, size=6.8):
    """Double-headed horizontal dimension arrow with an explicit label."""
    return (_line(x1, y - 5, x1, y + 5, sw=0.7, color=color)
            + _line(x2, y - 5, x2, y + 5, sw=0.7, color=color)
            + _arrow(x1 + 2, y, x2 - 2, y, sw=0.8, color=color, head="a7")
            + _arrow(x2 - 2, y, x1 + 2, y, sw=0.8, color=color, head="a7")
            + T((x1 + x2) / 2.0, y - 6, label, size, color=color))


def _lab(tx, ty, ax, ay, s, size=6.8, side="middle", color=INK):
    """Bilingual label with a thin grey leader to a feature."""
    return (T(tx, ty, s, size, anchor=side, color=color)
            + _arrow(tx, ty + 2, ax, ay, sw=0.7, color=GREY, head="a7"))


def _two(tx, ty, vi, en, side="middle", size=6.8, color=INK):
    """Two-line bilingual label: Vietnamese above English."""
    return (T(tx, ty, vi, size, anchor=side, color=color)
            + T(tx, ty + 9, en, size, anchor=side, color=color))


# ------------------------------------------------------------------ 12.9

@_reg
def fig_f1209():
    """Figure 12.9 - isolated conductors and creepage/clearance geometry."""
    w, h = 680, 350
    o = [_defs(), _rect(0, 0, w, h, fill=PAPER, sw=0)]
    _title(o, 9, "Ảnh hưởng của dây dẫn cô lập đến chiều dài rò và khoảng hở",
           "Effect of isolated conductors on creepage distances and clearances")

    # Cross-section of the solid insulating material.
    o.append(_rect(120, 112, 440, 58, fill=INSFILL, sw=1.1))
    o.append(_hatch(121, 113, 438, 56, step=8))
    o.append(_line(120, 112, 560, 112, sw=1.3))
    o.append(_line(120, 170, 560, 170, sw=1.1))

    # Three conductors sitting on the insulating surface.
    o.append(_rect(180, 105, 34, 7, fill=INK, sw=0.8))
    o.append(_rect(322, 105, 20, 7, fill=INK, sw=0.8))
    o.append(_rect(452, 105, 34, 7, fill=INK, sw=0.8))

    # D and d: the two isolated-conductor distances.
    o.append(_dimh(214, 322, 88, "D"))
    o.append(_dimh(342, 452, 88, "d"))

    # Creepage follows the surface; clearance spans the air gap.
    o.append(_line(214, 110, 322, 110, sw=1.6, color=CREEP, dash="1 2"))
    o.append(_line(342, 110, 452, 110, sw=1.6, color=CREEP, dash="1 2"))
    o.append(_line(214, 98, 452, 98, sw=1.3, color=CLEAR, dash="5 3"))

    # Printed callouts, bilingual.
    o.append(_lab(197, 66, 197, 104, "Dây dẫn mạch (Circuit conductor)", 6.8))
    o.append(_lab(332, 50, 332, 104, "Dây dẫn cô lập (Isolated conductor)", 6.8))
    o.append(_lab(469, 66, 469, 104, "Dây dẫn mạch (Circuit conductor)", 6.8))
    o.append(_lab(268, 204, 268, 111, "Chiều dài rò (Creepage distance)", 6.8))
    o.append(_lab(474, 204, 440, 106, "Khoảng hở (Clearance)", 6.8))

    # The printed equations and the creepage caveat.
    o.append(T(340, 228, "Khoảng hở = D + d, · Clearance = D + d,", 6.8))
    o.append(T(340, 244, "Chiều dài rò = D + d (Mọi chiều dài rò (d hoặc D) dưới 2,5 mm", 6.8))
    o.append(T(340, 258, "(1,5 mm nếu tổng chiều dài rò yêu cầu dưới 3 mm) được coi là", 6.8))
    o.append(T(340, 272, "đứt xuống và dẫn điện trong điều kiện làm việc bình thường).", 6.8))
    o.append(T(340, 288, "Creepage distance = D + d (Any creepage distance (d or D) of less", 6.8))
    o.append(T(340, 302, "than 2.5 mm (1.5 mm if total creepage distance required is less", 6.8))
    o.append(T(340, 316, "than 3 mm) is assumed to breakdown and conduct in normal service)", 6.8))

    return _fig(svg(w, h, "".join(o), esc("Fig 12.9")),
                "Hình 12.9 · Ảnh hưởng của dây dẫn cô lập đến chiều dài rò và khoảng hở",
                "Figure 12.9 · Effect of isolated conductors on creepage distances and clearances",
                "Mặt cắt chất cách điện có ba dây dẫn: hai dây dẫn mạch ở ngoài và một "
                "dây dẫn cô lập ở giữa. Hai kích thước D và d đo từ dây cô lập đến hai "
                "dây dẫn mạch. Đường chấm đỏ sát mặt chất cách điện là chiều dài rò; "
                "đường gạch xanh ngang qua không khí là khoảng hở. Các nhãn Dây dẫn "
                "mạch (Circuit conductor), Dây dẫn cô lập (Isolated conductor), Chiều "
                "dài rò (Creepage distance) và Khoảng hở (Clearance). Ghi công thức "
                "Clearance = D + d và Creepage distance = D + d kèm điều kiện: mọi "
                "chiều dài rò dưới 2,5 mm, hoặc 1,5 mm nếu tổng chiều dài rò yêu cầu "
                "dưới 3 mm, được coi là đứt xuống và dẫn điện khi làm việc bình thường",
                "Cross-section of insulating material with three conductors: two "
                "circuit conductors outside and one isolated conductor between them. "
                "Dimensions D and d measure from the isolated conductor to the two "
                "circuit conductors. The dotted red line hugging the surface is the "
                "creepage path; the dashed blue line through air is the clearance. "
                "Labelled Circuit conductor, Isolated conductor, Creepage distance "
                "and Clearance. The printed equations give Clearance = D + d and "
                "Creepage distance = D + d, with the caveat that any creepage "
                "distance under 2.5 mm, or 1.5 mm where the total required creepage "
                "is under 3 mm, is assumed to breakdown and conduct in normal service")


# ------------------------------------------------------------------ 12.10

@_reg
def fig_f1210():
    """Figure 12.10 - series temperature measurement in a terminal enclosure."""
    w, h = 680, 340
    o = [_defs(), _rect(0, 0, w, h, fill=PAPER, sw=0)]
    _title(o, 10, "Bố trí đo nhiệt độ trong vỏ đầu nối",
           "Arrangement for temperature measurement in terminal enclosures.")

    # The connection box and its label.
    o.append(_rect(230, 74, 220, 206, fill="#f7f9fb", sw=1.3))
    o.append(T(340, 62, "Hộp đầu nối (cao (H) × rộng (W)) / Connection box (height (H) x width (W))",
               6.8))
    o.append(_arrow(340, 64, 340, 73, sw=0.7, color=GREY, head="a7"))

    # The terminal strip: two columns of six screw terminals.
    o.append(_rect(312, 122, 56, 130, fill="#e8eef5", sw=1.1))
    for r in range(6):
        for c in range(2):
            cx, cy = 326 + c * 28, 134 + r * 20
            o.append(_circle(cx, cy, 6.2, fill="#ffffff", sw=1.0))
            o.append(_line(cx - 3.5, cy, cx + 3.5, cy, sw=0.9))
            o.append(_line(cx, cy - 3.5, cx, cy + 3.5, sw=0.9))

    # The two looms of six conductors, looped over the terminal strip.
    for i in range(6):
        dx = i * 2.2
        o.append(_poly([(266 + dx, 280), (266 + dx, 106), (270 + dx, 98),
                        (278 + dx, 94), (288 + dx, 96), (294 + dx, 104),
                        (294 + dx, 130), (312 + dx, 130)],
                       fill="none", sw=0.8, color=INK))
        o.append(_poly([(414 - dx, 280), (414 - dx, 106), (410 - dx, 98),
                        (402 - dx, 94), (392 - dx, 96), (386 - dx, 104),
                        (386 - dx, 130), (368 - dx, 130)],
                       fill="none", sw=0.8, color=INK))

    o.append(_lab(180, 174, 266, 174, "Bó 6 dây dẫn (Loom of 6 conductors)",
                  6.8, side="end"))
    o.append(_lab(500, 174, 414, 174, "Bó 6 dây dẫn (Loom of 6 conductors)",
                  6.8, side="start"))
    o.append(_lab(340, 106, 340, 128, "Các đầu nối (Terminals)", 6.8))

    # Printed note under the figure.
    o.append(T(340, 300,
               "Lưu ý: Chiều dài mỗi dây dẫn bằng một nửa đường chéo hộp (√(H² + W²)) bên trong hộp",
               6.8))
    o.append(T(340, 314,
               "Note: Length of each conductor is half of diagonal box dimension (√(H² + W²)) inside the box",
               6.8))

    return _fig(svg(w, h, "".join(o), esc("Fig 12.10")),
                "Hình 12.10 · Bố trí đo nhiệt độ trong vỏ đầu nối. "
                "Lưu ý: Chiều dài mỗi dây dẫn bằng một nửa đường chéo hộp bên trong hộp",
                "Figure 12.10 · Arrangement for temperature measurement in terminal "
                "enclosures. Note: Length of each conductor is half of diagonal box "
                "dimension (√(H² + W²)) inside the box",
                "Hộp đầu nối hình chữ nhật có kích thước cao H và rộng W. Bên trong là "
                "dải đầu nối gồm hai cột, mỗi cột sáu đầu nối vít, được nối tiếp bởi "
                "hai bó dẫn gồm sáu dây, vòng qua đầu dải rồi đi ra dưới đáy hộp. "
                "Nhãn Hộp đầu nối (Connection box), Các đầu nối (Terminals) và Bó 6 "
                "dây dẫn (Loom of 6 conductors). Ghi chú in: chiều dài mỗi dây dẫn "
                "bằng một nửa đường chéo hộp √(H² + W²) bên trong hộp",
                "Rectangular connection box of height H and width W. Inside it a "
                "terminal strip of two columns of six screw terminals is wired in "
                "series by two looms of six conductors which loop over the strip and "
                "leave through the bottom of the box. Labelled Connection box "
                "(height (H) x width (W)), Terminals and Loom of 6 conductors. "
                "Printed note: length of each conductor is half of diagonal box "
                "dimension (√(H² + W²)) inside the box")


# ------------------------------------------------------------------ 12.11

@_reg
def fig_f1211():
    """Figure 12.11 - indirect lamp isolation via a flameproof enclosure."""
    w, h = 680, 360
    o = [_defs(), _rect(0, 0, w, h, fill=PAPER, sw=0)]
    _title(o, 11, "Ví dụ về cách ly đèn gián tiếp",
           "Example of indirect lamp isolation.")
    o.append(T(340, 34,
               "Lưu ý: Nếu nối cuối vào nguồn ngoài không nằm trong vỏ chống cháy nổ thì phải đặt trong vỏ an toàn tăng cường bổ sung",
               6.8, color=GREY))
    o.append(T(340, 45,
               "Note: If final connection to external supply is not within flameproof enclosure then it should be in an additional increased safety enclosure",
               6.8, color=GREY))

    # Flameproof enclosure surrounding the break contacts.
    o.append(_rect(304, 74, 72, 78, fill="#efe6d3", sw=1.4))
    o.append(_hatch(305, 75, 70, 76, step=7))
    o.append(_rect(334, 82, 12, 12, fill="#dbe7f0", sw=1.0))
    o.append(_rect(334, 126, 12, 10, fill="#dbe7f0", sw=1.0))
    o.append(_line(340, 94, 340, 122, sw=1.2, color=INK, dash="3 2"))
    o.append(_rect(337, 56, 6, 104, fill="#d7dce2", sw=1.0))

    # Two flameproof bushings around the operating rod.
    o.append(_rect(330, 74, 20, 9, fill="#e7ddc8", sw=1.0))
    o.append(_hatch(331, 75, 18, 7, step=5))
    o.append(_rect(330, 130, 20, 9, fill="#e7ddc8", sw=1.0))
    o.append(_hatch(331, 131, 18, 7, step=5))

    # Cylindrical joint on the left and flange joint on the right.
    o.append(_rect(232, 100, 76, 8, fill="#d7dce2", sw=1.0))
    o.append(_rect(292, 100, 16, 8, fill="#efe6d3", sw=1.0))
    o.append(_hatch(293, 101, 14, 6, step=5))
    o.append(_rect(376, 100, 96, 8, fill="#d7dce2", sw=1.0))
    o.append(_rect(376, 96, 14, 16, fill="#efe6d3", sw=1.0))
    o.append(_hatch(377, 97, 12, 14, step=5))

    # Spring, threaded lamp cap and bulb.
    o.append(_poly([(330, 118), (350, 121), (330, 124), (350, 127), (330, 130)],
                   fill="none", sw=1.0, color=INK))
    o.append(_rect(326, 152, 28, 16, fill="#e9edf2", sw=1.0))
    for i in range(5):
        yy = 154 + i * 3.2
        o.append(_line(322, yy, 358, yy + 1.6, sw=0.9))
    o.append(_poly([(322, 170), (358, 170), (350, 178), (330, 178)],
                   fill="#dfe5ec", sw=1.0, close=True))
    o.append(_circle(340, 240, 64, fill="#f9fcff", sw=1.4))
    o.append(T(340, 244, "Đèn (Lamp)", 7.2))

    # Printed labels, bilingual, with leaders.
    o.append(_two(206, 80, "Mối nối trụ (thanh tác động)",
                  "Cylindrical joint (operating rod)", side="end"))
    o.append(_arrow(207, 91, 292, 104, sw=0.7, color=GREY, head="a7"))
    o.append(_two(206, 138, "Bushing chống cháy nổ",
                  "Flameproof bushing", side="end"))
    o.append(_arrow(207, 149, 304, 134, sw=0.7, color=GREY, head="a7"))
    o.append(_two(474, 60, "Bushing chống cháy nổ",
                  "Flameproof bushing", side="start"))
    o.append(_arrow(473, 71, 348, 78, sw=0.7, color=GREY, head="a7"))
    o.append(_two(474, 82, "Vỏ chống cháy nổ",
                  "Flameproof enclosure", side="start"))
    o.append(_arrow(473, 93, 376, 100, sw=0.7, color=GREY, head="a7"))
    o.append(_two(500, 110, "Mối nối bích", "Flange joint", side="start"))
    o.append(_arrow(499, 121, 468, 104, sw=0.7, color=GREY, head="a7"))
    o.append(_two(500, 136, "Thanh tác động", "Operating rod", side="start"))
    o.append(_arrow(499, 147, 344, 136, sw=0.7, color=GREY, head="a7"))
    o.append(_two(500, 162, "Lò xo", "Spring", side="start"))
    o.append(_arrow(499, 173, 350, 127, sw=0.7, color=GREY, head="a7"))

    return _fig(svg(w, h, "".join(o), esc("Fig 12.11")),
                "Hình 12.11 · Ví dụ về cách ly đèn gián tiếp. "
                "Lưu ý: Nếu nối cuối vào nguồn ngoài không nằm trong vỏ chống cháy nổ "
                "thì phải đặt trong một vỏ an toàn tăng cường bổ sung",
                "Figure 12.11 · Example of indirect lamp isolation. Note: If final "
                "connection to external supply is not within flameproof enclosure "
                "then it should be in an additional increased safety enclosure",
                "Mặt cắt đui đèn: thanh tác động đi qua mối nối trụ bên trái và mối "
                "nối bích bên phải; tiếp điểm bị ngắt bên trong vỏ chống cháy nổ "
                "có gạch chéo, với hai bushing chống cháy nổ và lò xo. Đầu dưới là "
                "núm vặn có ren và bóng đèn tròn nhãn Đèn (Lamp). Các nhãn in "
                "Cylindrical joint (operating rod), Flameproof enclosure, Flange "
                "joint, Operating rod, Spring và Flameproof bushing. Ghi chú: nếu "
                "nối cuối vào nguồn ngoài không nằm trong vỏ chống cháy nổ thì phải "
                "đặt trong một vỏ an toàn tăng cường bổ sung",
                "Lamp-holder cross-section: the operating rod passes through a "
                "cylindrical joint on the left and a flange joint on the right; the "
                "contacts break inside the hatched flameproof enclosure, with two "
                "flameproof bushings and a spring. Below is the threaded screw cap "
                "and the round bulb labelled Lamp. Printed labels include "
                "Cylindrical joint (operating rod), Flameproof enclosure, Flange "
                "joint, Operating rod, Spring and Flameproof bushing. Note: if the "
                "final connection to the external supply is not within the "
                "flameproof enclosure then it should be in an additional increased "
                "safety enclosure")


# ------------------------------------------------------------------ 12.12

@_reg
def fig_f1212():
    """Figure 12.12 - typical increased-safety cell construction."""
    w, h = 680, 350
    o = [_defs(), _rect(0, 0, w, h, fill=PAPER, sw=0)]
    _title(o, 12, "Cấu tạo điển hình của cell an toàn tăng cường",
           "Typical increased safety cell construction")

    # Cell container, insulated lining and sealed lid.
    o.append(_rect(240, 72, 200, 248, fill="#f5f8fa", sw=1.4))
    o.append(_rect(246, 78, 188, 236, fill="#fbfdff", sw=1.0))
    o.append(_hatch(240, 72, 6, 248, step=6))
    o.append(_hatch(434, 72, 6, 248, step=6))
    o.append(_hatch(240, 312, 200, 8, step=6))
    o.append(_rect(234, 66, 212, 12, fill="#e6ecf2", sw=1.3))

    # Electrolyte, expansion space and the two printed level marks.
    o.append(_rect(248, 100, 184, 212, fill="#eef6fa", sw=0))
    o.append(_line(248, 100, 432, 100, sw=1.0, color=BLUE, dash="6 3"))
    o.append(_line(248, 112, 432, 112, sw=1.0, color=BLUE, dash="6 3"))

    # Terminal posts, their encapsulation and the intercell connector.
    for cx in (286, 394):
        o.append(_rect(cx - 6, 48, 12, 26, fill="#d9dee4", sw=1.0))
        o.append(_rect(cx - 11, 58, 22, 16, fill="#efe6d3", sw=1.0))
        o.append(_hatch(cx - 10, 59, 20, 14, step=5))
    o.append(_rect(398, 40, 96, 8, fill="#d9dee4", sw=1.0))
    o.append(_circle(486, 44, 3, fill=INK, sw=0))
    o.append(_rect(258, 50, 22, 18, fill="#e6ecf2", sw=1.0))
    o.append(_rect(262, 44, 14, 6, fill="#d9dee4", sw=1.0))

    # Plate group connection bar, connection lug, plates and separators.
    o.append(_rect(268, 128, 144, 8, fill="#d9dee4", sw=1.0))
    o.append(_rect(392, 136, 10, 14, fill="#c8d2dd", sw=1.0))
    for px in (276, 306, 336, 366, 396):
        o.append(_rect(px, 150, 8, 142, fill="#dfe7ef", sw=1.0))
        o.append(_hatch(px + 1, 151, 6, 140, step=6))
    for px in (291, 321, 351, 381):
        o.append(_rect(px, 150, 6, 142, fill="#f3f6f9", sw=0.8, dash="3 2"))

    # Left-hand printed labels.
    o.append(_two(214, 50, "Núm rót chống tràn", "Spillproof fill and vent plug",
                  side="end"))
    o.append(_arrow(215, 61, 258, 56, sw=0.7, color=GREY, head="a7"))
    o.append(_two(214, 76, "Nắp kín", "Sealed lid", side="end"))
    o.append(_arrow(215, 87, 234, 72, sw=0.7, color=GREY, head="a7"))
    o.append(_two(214, 98, "Khoảng giãn nở dung dịch", "Electrolyte expansion space",
                  side="end"))
    o.append(_arrow(215, 109, 248, 90, sw=0.7, color=GREY, head="a7"))
    o.append(_two(214, 126, "Mức dung dịch tối đa / tối thiểu",
                  "Maximum and minimum electrolyte levels", side="end"))
    o.append(_arrow(215, 137, 248, 104, sw=0.7, color=GREY, head="a7"))
    o.append(_two(214, 198, "Vách ngăn bản cực", "Plate separators", side="end"))
    o.append(_arrow(215, 209, 291, 200, sw=0.7, color=GREY, head="a7"))
    o.append(_two(214, 244, "Vỏ cell", "Cell container", side="end"))
    o.append(_arrow(215, 255, 240, 244, sw=0.7, color=GREY, head="a7"))

    # Right-hand printed labels.
    o.append(T(470, 50, "Vỏ cách điện cọc (Post insulation/encapsulation)", 6.8,
               anchor="start"))
    o.append(_arrow(469, 52, 404, 62, sw=0.7, color=GREY, head="a7"))
    o.append(T(470, 64, "Đầu nối liên cell (Intercell connector)", 6.8,
               anchor="start"))
    o.append(_arrow(469, 66, 470, 44, sw=0.7, color=GREY, head="a7"))
    o.append(T(470, 78, "Cọc đầu cuối/nắp (Terminal post/lid)", 6.8,
               anchor="start"))
    o.append(_arrow(469, 80, 394, 66, sw=0.7, color=GREY, head="a7"))
    o.append(T(470, 92, "Gioăng kín dung dịch (Electrolyte proof seal)", 6.8,
               anchor="start"))
    o.append(_arrow(469, 94, 394, 72, sw=0.7, color=GREY, head="a7"))
    o.append(T(470, 106, "Cọc đầu cuối (Terminal post)", 6.8, anchor="start"))
    o.append(_arrow(469, 108, 388, 50, sw=0.7, color=GREY, head="a7"))
    o.append(T(470, 134, "Thanh nối nhóm bản cực (Plate group connection bar)",
               6.8, anchor="start"))
    o.append(_arrow(469, 136, 412, 132, sw=0.7, color=GREY, head="a7"))
    o.append(T(470, 150, "Tai nối bản cực (Plate connection lug)", 6.8,
               anchor="start"))
    o.append(_arrow(469, 152, 402, 142, sw=0.7, color=GREY, head="a7"))
    o.append(T(470, 220, "Bản cực (Plate)", 6.8, anchor="start"))
    o.append(_arrow(469, 222, 400, 220, sw=0.7, color=GREY, head="a7"))
    o.append(T(470, 306, "Khoảng bùn lắng đầy đủ (Adequate slurry space)", 6.8,
               anchor="start"))
    o.append(_arrow(469, 308, 410, 306, sw=0.7, color=GREY, head="a7"))

    return _fig(svg(w, h, "".join(o), esc("Fig 12.12")),
                "Hình 12.12 · Cấu tạo điển hình của cell an toàn tăng cường",
                "Figure 12.12 · Typical increased safety cell construction",
                "Mặt cắt cell ắc quy: vỏ cell có lớp lót cách điện và nắp kín, núm "
                "rót chống tràn, khoảng giãn nở dung dịch với hai mức tối đa và tối "
                "thiểu. Hai cọc đầu cuối được bọc cách điện và nối bằng đầu nối liên "
                "cell. Bên trong là thanh nối nhóm bản cực, tai nối bản cực, các bản "
                "cực và vách ngăn, phần đáy chừa khoảng bùn lắng. Các nhãn in gồm "
                "Post insulation/encapsulation, Intercell connector, Terminal "
                "post/lid, Electrolyte proof seal, Terminal post, Plate group "
                "connection bar, Plate connection lug, Plate, Plate separators, "
                "Cell container, Sealed lid, Spillproof fill and vent plug và "
                "Adequate slurry space",
                "Cross-section of a battery cell: the container has an insulated "
                "lining and a sealed lid, a spillproof fill and vent plug, an "
                "electrolyte expansion space with maximum and minimum levels. Two "
                "terminal posts are encapsulated and joined by an intercell "
                "connector. Inside are the plate group connection bar, the plate "
                "connection lug, plates and separators, with an adequate slurry "
                "space at the bottom. Printed labels include Post insulation/"
                "encapsulation, Intercell connector, Terminal post/lid, Electrolyte "
                "proof seal, Terminal post, Plate group connection bar, Plate "
                "connection lug, Plate, Plate separators, Cell container, Sealed "
                "lid, Spillproof fill and vent plug and Adequate slurry space")
