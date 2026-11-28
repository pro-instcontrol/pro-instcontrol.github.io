# -*- coding: utf-8 -*-
"""Vector redraws of Figures 12.1-12.4 in A. McMillan, *Electrical
Installations in Hazardous Areas*, Chapter 12 "Apparatus with protection
concept increased safety 'e'".

All four drawings are simplified vector redraws of the rendered pages
p321 and p322.  The printed English captions, including their Note lines,
are reproduced verbatim with a bilingual prefix; printed part labels and
the A-F legend of Fig. 12.3 are transcribed onto the drawings.  Printed
quirks are retained and noted: the Fig. 12.2 caption omits its number in
print and Fig. 12.3 prints 'spade/eylet'.  Each public callable returns the
standard five-tuple through ``vfig._fig()`` and is registered in ``FIGS``
by the ``_reg`` decorator.
"""
import sys
import os

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

from vfig import (BLUE, GREEN, GREY, INK, PAPER, RED, _arrow, _circle,
                  _defs, _fig, _line, _poly, _rect, _txt, svg)

FIGS = {}


def _reg(f):
    FIGS[f.__name__] = f()
    return f


def esc(s):
    """Every displayed string is literal Unicode with raw ampersands escaped."""
    return str(s).replace("&", "&amp;")


def T(x, y, s, size=8.0, **kw):
    """Plain text: vet first, then delegate to vfig._txt()."""
    return _txt(x, y, esc(s), size, **kw)


# ------------------------------------------------------------------ helpers

def _title(o, n, vi, en, size=7.2):
    o.append(T(340, 15, "Hình 12.%d · %s / Figure 12.%d · %s" % (n, vi, n, en),
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


def _badge(o, cx, cy, letter):
    o.append(_circle(cx, cy, 7, fill="#ffffff", sw=1.0))
    o.append(T(cx, cy + 2.6, letter, 7.4, color=INK, weight="600"))


def _thread(o, cx, y0, y1, step=8):
    for yy in range(y0, y1, step):
        o.append(_line(cx - 5, yy, cx + 5, yy - 3, sw=0.6, color=GREY))


def _single_view(o, cx, cross=False):
    """One cross-section of a single-conductor terminal."""
    x0, w = cx - 44, 88
    o.append(_rect(x0, 76, w, 146, fill="#ffffff", sw=1.2))
    o.append(_rect(x0, 76, 9, 146, fill="url(#h6)", sw=0.9))
    o.append(_rect(x0 + w - 9, 76, 9, 146, fill="url(#h6)", sw=0.9))
    o.append(_rect(x0, 214, 20, 8, fill="url(#h6)", sw=0.9))
    o.append(_rect(x0 + w - 20, 214, 20, 8, fill="url(#h6)", sw=0.9))
    o.append(_rect(cx - 17, 62, 34, 14, fill="#dedede", sw=1.1))
    o.append(_line(cx - 12, 69, cx + 12, 69, sw=0.9))
    if cross:
        o.append(_line(cx, 64, cx, 74, sw=0.7))
    o.append(_poly([(cx - 9, 80), (cx + 9, 84), (cx - 9, 88),
                    (cx + 9, 92), (cx - 9, 96)], fill="none", sw=1.0))
    o.append(_rect(cx - 5, 96, 10, 88, fill="#cfcfcf", sw=1.0))
    _thread(o, cx, 104, 184, 8)
    o.append(_rect(cx - 28, 188, 56, 10, fill="url(#h7)", sw=1.0))
    o.append(_circle(cx, 211, 13, fill="#bdbdbd", sw=1.2))
    o.append(_circle(cx, 211, 7, fill="#f2f2f2", sw=0.8))


def _multi_view(o, cx, cross=False):
    """One cross-section of a multi-conductor terminal."""
    x0, w = cx - 46, 92
    o.append(_rect(x0, 82, w, 146, fill="#ffffff", sw=1.2))
    o.append(_rect(x0, 82, 11, 146, fill="url(#h6)", sw=0.9))
    o.append(_rect(x0 + w - 11, 82, 11, 146, fill="url(#h6)", sw=0.9))
    o.append(_rect(x0, 220, 20, 8, fill="url(#h6)", sw=0.9))
    o.append(_rect(x0 + w - 20, 220, 20, 8, fill="url(#h6)", sw=0.9))
    o.append(_rect(cx - 18, 66, 36, 16, fill="#dedede", sw=1.1))
    o.append(_line(cx - 12, 74, cx + 12, 74, sw=0.9))
    if cross:
        o.append(_line(cx, 68, cx, 80, sw=0.7))
    o.append(_rect(x0 + 11, 88, 14, 10, fill="url(#h7)", sw=0.9))
    o.append(_rect(x0 + w - 25, 88, 14, 10, fill="url(#h7)", sw=0.9))
    o.append(_rect(cx - 5, 102, 10, 92, fill="#cfcfcf", sw=1.0))
    _thread(o, cx, 110, 194, 8)
    o.append(_rect(cx - 27, 198, 54, 10, fill="url(#h7)", sw=1.0))
    for dx in (-20, 0, 20):
        o.append(_circle(cx + dx, 219, 9, fill="#bdbdbd", sw=1.0))


# ------------------------------------------------------------------ 12.1

@_reg
def fig_f1201():
    """Figure 12.1 - typical single conductor terminal, two sections."""
    w, h = 680, 300
    o = [_defs(), _rect(0, 0, w, h, fill=PAPER, sw=0)]
    _title(o, 1, "Cầu nối một dây dẫn điển hình", "Typical single conductor terminal", 7.2)
    _sub(o, "Mặt cắt · đầu vít, lò xo khóa, miếng đệm áp và dây dẫn / "
            "Cross-sections · screw head, spring lock, pressure pad, conductor", 5.5)

    _single_view(o, 170)
    _single_view(o, 510, cross=True)

    _bi(o, 340, 78, "Đầu vít", "Screw head", 6.4)
    _bi(o, 340, 102, "Lò xo khóa", "Spring locking arrangement", 6.2)
    _bi(o, 340, 140, "Vít", "Screw", 6.2)
    _bi(o, 340, 178, "Miếng đệm áp", "Pressure pad", 6.2)
    _bi(o, 340, 224, "Dây dẫn", "Conductor", 6.4)

    o.append(_lead(292, 80, 202, 69))
    o.append(_lead(388, 80, 478, 69))
    o.append(_lead(288, 106, 204, 88))
    o.append(_lead(392, 106, 476, 88))
    o.append(_lead(300, 143, 204, 143))
    o.append(_lead(380, 143, 476, 143))
    o.append(_lead(292, 182, 206, 192))
    o.append(_lead(388, 182, 474, 192))
    o.append(_lead(300, 228, 200, 214))
    o.append(_lead(380, 228, 480, 214))

    o.append(T(170, 244, "(a) Mặt cắt / Section", 6.8, color=GREY))
    o.append(T(510, 244, "(b) Mặt cắt quay / Rotated section", 6.8, color=GREY))
    o.append(T(340, 272, "Lưu ý: Không cần miếng đệm áp nếu dây dẫn được ép trong ống ferrule phù hợp",
      6.8, color=INK))
    o.append(T(340, 282, "Note: The pressure pad is not necessary if the conductor is crimped "
                "in a suitable ferrule", 6.8, color=INK))

    return _fig(svg(w, h, "".join(o), esc("Fig 12.1")),
                "Hình 12.1 · Cầu nối một dây dẫn điển hình. Lưu ý: Không cần miếng đệm áp "
                "nếu dây dẫn được ép trong ống ferrule phù hợp",
                "Figure 12.1 · Typical single conductor terminal. Note: The pressure pad "
                "is not necessary if the conductor is crimped in a suitable ferrule",
                "Hai mặt cắt cầu nối một dây dẫn. Ở mỗi mặt cắt, đầu vít và lò xo khóa "
                "nằm phía trên vít có ren, vít ép vào miếng đệm áp gạch chéo, dây dẫn "
                "tròn nằm ở đáy thân cầu nối có thành gạch chéo. Các nhãn giữa hình chỉ "
                "Đầu vít (Screw head), Lò xo khóa (Spring locking arrangement), Vít "
                "(Screw), Miếng đệm áp (Pressure pad) và Dây dẫn (Conductor). Dòng "
                "Lưu ý/Note in ở cuối hình nói không cần miếng đệm áp nếu dây dẫn được "
                "ép trong ống ferrule phù hợp",
                "Two cross-sections of a single-conductor terminal. Each shows a slotted "
                "screw head and a spring locking arrangement above the threaded screw, "
                "which bears on a hatched pressure pad with a round conductor at the "
                "bottom of the hatched terminal body. Central leaders name Screw head, "
                "Spring locking arrangement, Screw, Pressure pad and Conductor. The "
                "printed Note says the pressure pad is not necessary if the conductor "
                "is crimped in a suitable ferrule")


# ------------------------------------------------------------------ 12.2

@_reg
def fig_f1202():
    """Figure 12.2 - typical multi-conductor terminal, two sections."""
    w, h = 680, 300
    o = [_defs(), _rect(0, 0, w, h, fill=PAPER, sw=0)]
    _title(o, 2, "Cầu nối nhiều dây dẫn điển hình", "Typical multi-conductor terminal", 7.0)
    _sub(o, "Mặt cắt · đầu vít, vòng giữ, thân cầu nối, miếng đệm áp và các dây dẫn / "
            "Cross-sections · screw head, retaining ring, body, pressure pad, conductors", 5.4)

    _multi_view(o, 170)
    _multi_view(o, 510, cross=True)

    _bi(o, 340, 70, "Đầu vít", "Screwhead", 6.2)
    _bi(o, 340, 100, "Vòng giữ", "Retaining ring", 6.2)
    _bi(o, 340, 136, "Vít", "Screw", 6.2)
    _bi(o, 340, 166, "Thân cầu nối", "Terminal body", 6.2)
    _bi(o, 340, 196, "Miếng đệm áp", "Pressure pad", 6.2)
    _bi(o, 340, 238, "Dây dẫn", "Conductor", 6.2)

    o.append(_lead(288, 72, 204, 74))
    o.append(_lead(392, 72, 476, 74))
    o.append(_lead(288, 104, 206, 93))
    o.append(_lead(392, 104, 474, 93))
    o.append(_lead(298, 139, 204, 139))
    o.append(_lead(382, 139, 476, 139))
    o.append(_lead(288, 170, 206, 170))
    o.append(_lead(392, 170, 474, 170))
    o.append(_lead(290, 199, 206, 203))
    o.append(_lead(390, 199, 474, 203))
    o.append(_lead(298, 242, 196, 222))
    o.append(_lead(382, 242, 484, 222))

    o.append(T(170, 250, "(a) Mặt cắt / Section", 6.8, color=GREY))
    o.append(T(510, 250, "(b) Mặt cắt quay / Rotated section", 6.8, color=GREY))
    o.append(T(340, 270, "Lưu ý: Không cần miếng đệm áp nếu các dây dẫn được ép riêng vào ống ferrule phù hợp",
      6.8, color=INK))
    o.append(T(340, 280, "Note: The pressure pad is not necessary if the conductors are individually "
                "crimped into suitable ferrules", 6.8, color=INK))

    return _fig(svg(w, h, "".join(o), esc("Fig 12.2")),
                "Hình 12.2 · Cầu nối nhiều dây dẫn điển hình. Lưu ý: Không cần miếng đệm áp "
                "nếu các dây dẫn được ép riêng vào ống ferrule phù hợp",
                "Figure 12.2 · Typical multi-conductor terminal. Note: The pressure pad "
                "is not necessary if the conductors are individually crimped into suitable ferrules",
                "Hai mặt cắt cầu nối nhiều dây dẫn. Mỗi mặt cắt có đầu vít, vòng giữ ở "
                "hai bên, vít ren dài, thân cầu nối gạch chéo, miếng đệm áp và ba dây "
                "dẫn tròn ở đáy. Các nhãn giữa hình là Đầu vít (Screwhead), Vòng giữ "
                "(Retaining ring), Vít (Screw), Thân cầu nối (Terminal body), Miếng đệm "
                "áp (Pressure pad) và Dây dẫn (Conductor). Chú thích in gốc chỉ ghi "
                "'Fig. Typical multi-conductor terminal' và thiếu số hình; số 12.2 được "
                "khôi phục ở đây. Lưu ý/Note in nói không cần miếng đệm áp nếu các dây "
                "dẫn được ép riêng vào ống ferrule phù hợp",
                "Two cross-sections of a multi-conductor terminal. Each shows a screw "
                "head, retaining rings at the sides, a long threaded screw, a hatched "
                "terminal body, a pressure pad and three round conductors at the bottom. "
                "Central leaders name Screwhead, Retaining ring, Screw, Terminal body, "
                "Pressure pad and Conductor. The printed caption reads 'Fig. Typical "
                "multi-conductor terminal' and omits its number; Figure 12.2 is restored "
                "here. The printed Note says the pressure pad is not necessary if the "
                "conductors are individually crimped into suitable ferrules")


# ------------------------------------------------------------------ 12.3

@_reg
def fig_f1203():
    """Figure 12.3 - typical spade/eylet termination with the A-F legend."""
    w, h = 680, 300
    o = [_defs(), _rect(0, 0, w, h, fill=PAPER, sw=0)]
    _title(o, 3, "Đầu nối spade/eylet điển hình", "Typical spade/eylet termination", 7.2)
    _sub(o, "Mặt cắt · A = bộ phận dẫn điện, B = vít, C = đầu nối, D = dây dẫn, "
            "E = vòng lò xo, F = vòng sao / Cross-section · A-F legend", 5.5)

    o.append(T(340, 60, "Mặt cắt đầu nối / Termination cross-section", 6.8, color=INK))

    # Stacked joint: conductor and spade above, hatched apparatus plate below.
    o.append(_rect(160, 132, 330, 26, fill="url(#h6)", sw=1.2))
    o.append(_rect(320, 126, 72, 6, fill="url(#h7)", sw=0.9))
    o.append(_poly([(322, 124), (332, 120), (342, 124), (352, 120),
                    (362, 124), (372, 120), (382, 124), (390, 120)],
                   fill="none", sw=1.0))
    o.append(_rect(300, 112, 170, 8, fill="#cfcfcf", sw=1.1))
    o.append(_rect(348, 112, 14, 8, fill="#ffffff", sw=0.9))
    o.append(_rect(470, 113, 116, 6, fill="#bdbdbd", sw=1.0))
    o.append(_rect(356, 158, 10, 34, fill="#cfcfcf", sw=1.0))
    _thread(o, 361, 162, 190, 6)
    o.append(_rect(334, 192, 46, 22, fill="#dedede", sw=1.1))
    for xx in (340, 348, 356, 364, 372):
        o.append(_line(xx, 194, xx, 212, sw=0.6, color=GREY))

    # Letter call-outs on the printed component locations.
    _badge(o, 190, 146, "A")
    _badge(o, 410, 204, "B")
    _badge(o, 430, 102, "C")
    _badge(o, 530, 102, "D")
    _badge(o, 402, 124, "E")
    _badge(o, 306, 130, "F")
    o.append(_lead(403, 204, 380, 204))

    # Printed A-F legend, translated with the printed English in parentheses.
    o.append(T(36, 236, "A = Bộ phận dẫn điện (Conducting part of apparatus)", 6.8, anchor="start"))
    o.append(T(36, 250, "B = Vít nối (Connection screw)", 6.8, anchor="start"))
    o.append(T(36, 264, "C = Đầu nối spade/eylet (Spade or eylet termination or similar)",
      6.8, anchor="start"))
    o.append(T(344, 236, "D = Dây dẫn ép/hàn (Conductor crimped, soldered, welded or brazed to termination)",
      6.8, anchor="start"))
    o.append(T(344, 250, "E = Vòng đệm lò xo (Spring washer to prevent loosening)",
      6.8, anchor="start"))
    o.append(T(344, 264, "F = Vòng đệm sao (Star washer, if necessary to ensure good electrical connection)",
      6.8, anchor="start"))
    o.append(T(340, 284, "Thứ tự lắp: đầu nối, vòng đệm sao, vòng đệm lò xo, vít nối · "
                "Stack: termination, star washer, spring washer, screw", 6.8, color=GREY))

    return _fig(svg(w, h, "".join(o), esc("Fig 12.3")),
                "Hình 12.3 · Đầu nối spade/eylet điển hình",
                "Figure 12.3 · Typical spade/eylet termination",
                "Mặt cắt đầu nối có vít nối đi lên qua thân thiết bị gạch chéo, vòng đệm "
                "sao và vòng đệm lò xo, đầu nối spade/eylet dẹt và dây dẫn phía trên "
                "bên phải. Các ký hiệu A-F trên hình và bảng chú thích liệt kê A = bộ "
                "phận dẫn điện, B = vít nối, C = đầu nối spade hoặc eylet, D = dây dẫn "
                "được ép/hàn/khâu, E = vòng đệm lò xo chống lỏng, F = vòng đệm sao. "
                "Chính tả 'spade/eylet' của bản in được giữ nguyên",
                "Cross-section of a termination with a connection screw rising through "
                "the hatched apparatus part, a star washer and a spring washer, then a "
                "flat spade/eylet termination and its conductor to the upper right. "
                "Call-outs A-F and the legend list A = conducting part of apparatus, "
                "B = connection screw, C = spade or eylet termination or similar, "
                "D = conductor crimped, soldered, welded or brazed to termination, "
                "E = spring washer to prevent loosening, F = star washer if necessary "
                "to ensure good electrical connection. The printed spelling "
                "'spade/eylet' is retained")


# ------------------------------------------------------------------ 12.4

@_reg
def fig_f1204():
    """Figure 12.4 - typical crimped connections, terminal and through crimp."""
    w, h = 680, 300
    o = [_defs(), _rect(0, 0, w, h, fill=PAPER, sw=0)]
    _title(o, 4, "Mối nối ép điển hình", "Typical crimped connections", 7.2)
    _sub(o, "Hai kiểu ép · mối ép đầu và ép xuyên / Two forms · terminal crimp and through crimp", 5.8)

    # (a) spade/eylet terminal with a ferrule crimped onto the wire.
    o.append(T(340, 52, "(a) Đầu nối spade/eylet có ống ép / Spade/eylet terminal with ferrule",
      6.8, color=INK))
    o.append(_poly([(110, 106), (196, 106), (210, 113), (196, 120), (110, 120)],
                   fill="#cfcfcf", sw=1.1, close=True))
    o.append(_rect(206, 104, 110, 18, fill="#dedede", sw=1.1))
    o.append(_rect(360, 105, 110, 14, fill="#eeeeee", sw=0.9))
    o.append(_rect(316, 109, 180, 8, fill="#bdbdbd", sw=1.0))
    o.append(_rect(226, 104, 7, 18, fill="#8a8a8a", sw=0))
    o.append(_rect(262, 104, 7, 18, fill="#8a8a8a", sw=0))
    o.append(T(110, 82, "Đầu spade/eylet (Spade/eylet terminal)", 6.8, anchor="start"))
    o.append(T(470, 82, "Dây dẫn (Wire)", 6.8, anchor="end"))
    o.append(_lead(160, 86, 158, 106))
    o.append(_lead(446, 86, 440, 109))
    o.append(T(200, 142, "Ống ferrule (Ferrule)", 6.8))
    o.append(T(320, 142, "Các vết ép (Crimps)", 6.8))
    o.append(T(470, 142, "Ép đầu (Terminal crimp)", 6.8))
    o.append(_lead(210, 136, 240, 122))
    o.append(_lead(310, 136, 266, 122))

    o.append(_line(50, 166, 630, 166, sw=0.8, color=GREY))

    # (b) through crimp: ferrule joining two wires with crimps at each end.
    o.append(T(340, 186, "(b) Ép xuyên / Through crimp", 6.8, color=INK))
    o.append(_rect(110, 214, 130, 10, fill="#bdbdbd", sw=1.0))
    o.append(_rect(440, 214, 130, 10, fill="#bdbdbd", sw=1.0))
    o.append(_rect(240, 206, 200, 26, fill="#dedede", sw=1.1))
    for xx in (250, 330, 420):
        o.append(_rect(xx, 206, 8, 26, fill="#8a8a8a", sw=0))
    o.append(T(200, 200, "Ép đầu (Terminal crimp)", 6.8))
    o.append(T(330, 200, "Ống ferrule (Ferrule)", 6.8))
    o.append(T(500, 200, "Dây dẫn (Wires)", 6.8))
    o.append(_lead(210, 204, 254, 207))
    o.append(_lead(330, 204, 330, 206))
    o.append(_lead(500, 204, 500, 214))
    o.append(T(330, 250, "Các vết ép (Crimps)", 6.8))
    o.append(_lead(330, 255, 334, 232))
    o.append(T(340, 270, "Ép xuyên (Through crimp)", 6.8, color=INK, weight="600"))
    o.append(T(340, 286, "Dây dẫn được cố định trong ống ferrule bằng một hoặc nhiều vết ép · "
                "Conductors are secured in the ferrule by single or multiple crimping actions",
      6.8, color=GREY))

    return _fig(svg(w, h, "".join(o), esc("Fig 12.4")),
                "Hình 12.4 · Mối nối ép điển hình",
                "Figure 12.4 · Typical crimped connections",
                "Hai mối nối ép. Hình trên: đầu nối spade/eylet dẹt nối với dây dẫn qua "
                "ống ferrule có hai vết ép, các nhãn Spade/eylet terminal, Wire, Ferrule, "
                "Crimps và Terminal crimp. Hình dưới: ống ferrule nối hai dây dẫn, ép "
                "ở nhiều vị trí, các nhãn Terminal crimp, Ferrule, Wires, Crimps và "
                "Through crimp",
                "Two crimped connections. Upper: a flat spade/eylet terminal joined to "
                "a wire through a ferrule with two crimp bands, labelled Spade/eylet "
                "terminal, Wire, Ferrule, Crimps and Terminal crimp. Lower: a ferrule "
                "joining two wires with crimps at several positions, labelled Terminal "
                "crimp, Ferrule, Wires, Crimps and Through crimp")
