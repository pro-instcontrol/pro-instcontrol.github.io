# -*- coding: utf-8 -*-
"""Vector redraw of the NEC 505 marking breakdown (printed A9, PDF p10).

Figure 5-1 reproduces the leader-line diagram for the typical North American
marking ``Class I, Zone 1, AEx de IIC T6``.  It is drawn entirely with ``vfig``
primitives--no raster--and every callout carries a bilingual VI/EN label.
Architecture mirrors ``cvpfig26.py``: ``FIGS`` registry, ``@_reg`` and the
standard five-tuple returned by ``vfig._fig()``.
"""
from vfig import (BLUE, GREEN, GREY, INK, PAPER, RED, _arrow, _circle, _defs,
                  _fig, _line, _path, _poly, _rect, _txt, svg)

FIGS = {}


def _reg(f):
    FIGS[f.__name__] = f()
    return f


def esc(s):
    return (str(s).replace("&", "&amp;").replace("<", "&lt;")
            .replace(">", "&gt;").replace('"', "&quot;"))


def T(x, y, s, size=7.6, **kw):
    return _txt(x, y, esc(s), size, **kw)


def _leader(o, sx, ty):
    """Drop a leader from a mark segment, then run it right to the text."""
    o.append(_line(sx, 54, sx, ty, sw=0.9, color=GREY))
    o.append(_line(sx, ty, 372, ty, sw=0.9, color=GREY))
    o.append(_circle(sx, 54, 1.6, fill=INK, sw=0))


@_reg
def fig_f501():
    """Figure 5-1 -- NEC 505 marking, 'Class I, Zone 1, AEx de IIC T6'."""
    w, h = 680, 560
    o = [_defs()]
    o.append(T(340, 18,
               "Hình 5-1 · Ký hiệu Bắc Mỹ theo NEC 505 / "
               "Figure 5-1 · Typical North American marking to NEC 505",
               8.8, color=INK, weight="600"))

    # ---- the marking itself, drawn as six underlined segments -------------
    o.append(_line(30, 54, 376, 54, sw=1.2, color=INK))
    for bx in (90, 166, 228, 282, 334):
        o.append(_line(bx, 45, bx, 54, sw=0.8, color=GREY))
    segs = [(58, "Class I,"), (132, "Zone 1,"), (200, "AEx"),
            (256, "de"), (308, "IIC"), (360, "T6")]
    for sx, label in segs:
        o.append(T(sx, 43, label, 8.4, color=INK, weight="600"))

    # ---- leader lines (a small grid, as on the printed page) --------------
    for sx, ty in ((58, 82), (132, 110), (200, 256),
                   (256, 282), (308, 306), (360, 384)):
        _leader(o, sx, ty)

    # ---- definitions, right-hand column ----------------------------------
    x = 380
    o.append(T(x, 82, "Class I (khí và hơi) / Class I (Gases and Vapors)",
               7.0, color=BLUE, weight="600"))

    # The three Zone definitions share one bracket off the "Zone 1," leader.
    o.append(_line(372, 110, 372, 238, sw=0.9, color=GREY))
    for by in (110, 154, 208):
        o.append(_line(372, by, 380, by, sw=0.9, color=GREY))

    o.append(T(x, 110, "Vùng 0 / Zone 0", 7.0, color=BLUE, weight="600"))
    o.append(T(x, 120, "Môi trường khí nổ hiện diện liên tục hoặc trong thời gian dài", 6.6))
    o.append(T(x, 130, "Areas where explosive gas atmosphere is continuously present", 6.6))
    o.append(T(x, 140, "or present for long periods of time", 6.6))

    o.append(T(x, 154, "Vùng 1 / Zone 1", 7.0, color=BLUE, weight="600"))
    o.append(T(x, 164, "Môi trường khí nổ có khả năng xuất hiện trong vận hành bình thường", 6.6))
    o.append(T(x, 174, "hoặc dự kiến hiện diện thường xuyên", 6.6))
    o.append(T(x, 184, "Areas where explosive gas atmosphere is likely to occur in normal", 6.6))
    o.append(T(x, 194, "operation or can be expected to be present frequently", 6.6))

    o.append(T(x, 208, "Vùng 2 / Zone 2", 7.0, color=BLUE, weight="600"))
    o.append(T(x, 218, "Môi trường khí nổ ít có khả năng xuất hiện; nếu có thì chỉ tồn tại trong thời gian ngắn", 6.6))
    o.append(T(x, 228, "Area where explosive gas atmosphere is not likely to occur and if it", 6.6))
    o.append(T(x, 238, "does, it will only exist for a short period of time", 6.6))

    o.append(T(x, 256, "AEx chỉ thiết kế theo tiêu chuẩn ANSI của Hoa Kỳ", 6.6))
    o.append(T(x, 266, "AEx designates built to a US ANSI standard", 6.6))

    o.append(T(x, 282, "Phương pháp bảo vệ: d, e, p, i, o, q, m, n", 6.6))
    o.append(T(x, 292, "Methods of protection, d, e, p, i, o, q, m, n", 6.6))

    o.append(T(x, 306, "Nhóm thiết bị / Apparatus Group", 7.0, color=BLUE, weight="600"))
    o.append(T(x, 316, "I Khai khoáng – dưới lòng đất (mêtan); II Công nghiệp trên mặt đất", 6.6))
    o.append(T(x, 326, "I Mining – Underground (methane); II Surface Industries", 6.6))
    o.append(T(x, 338, "A (propan), B (etylen), C (hydro)", 6.6))
    o.append(T(x, 348, "A (propane), B (ethylene), C (hydrogen)", 6.6))

    o.append(T(x, 384, "Cấp nhiệt độ / Temperature class", 7.0, color=BLUE, weight="600"))
    for i, s in enumerate(("T1 450° C", "T2 300° C", "T3 200° C",
                           "T4 135° C", "T5 100°C", "T6 85° C")):
        o.append(T(x, 396 + i * 10, s, 6.8, color=RED))
    o.append(T(x, 460, "Nhiệt độ bề mặt tối đa / Maximum surface temperature",
               6.4, color=GREY))

    # ---- in-SVG caption strip --------------------------------------------
    o.append(T(340, 524,
               "Hình 5-1 · Ký hiệu NEC 505: Class I, Zone 1, AEx de IIC T6",
               6.8, color=INK))
    o.append(T(340, 538,
               "Figure 5-1 · NEC 505 marking: Class I, Zone 1, AEx de IIC T6",
               6.8, color=GREY))
    return _fig(svg(w, h, "".join(o),
                    esc("Sơ đồ phân tích ký hiệu NEC 505: Class I, Zone 1, AEx de IIC T6")),
                "Hình 5-1 · Ký hiệu điển hình của Bắc Mỹ theo NEC 505: Class I, Zone 1, AEx de IIC T6, với các chú thích dẫn giải từng thành phần",
                "Figure 5-1 · Typical North American marking to NEC 505: Class I, Zone 1, AEx de IIC T6, with leader-line definitions of every element of the mark.",
                "Sơ đồ ký hiệu NEC 505 với đường dẫn từ Class I, Zone 1, AEx, de, IIC và T6 tới các định nghĩa về vùng, phương pháp bảo vệ, nhóm thiết bị và cấp nhiệt độ",
                "NEC 505 marking diagram with leaders from Class I, Zone 1, AEx, de, IIC and T6 to definitions of zones, protection methods, apparatus groups and temperature classes")
