# -*- coding: utf-8 -*-
"""Vector redraw of the ATEX/CENELEC marking breakdown (printed A10, PDF p11).

Figure 6-1 reproduces the leader-line diagram for ``II 2G EEx de IIC T6``:
the Ex hexagon, equipment groups and categories, the gas/dust zone
definitions, the CENELEC reference, protection methods, apparatus groups and
temperature classes.  Drawn with ``vfig`` primitives only; bilingual VI/EN
callouts; ``FIGS`` registry + ``@_reg`` and the standard five-tuple via
``vfig._fig()``.
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
    o.append(_line(sx, 52, sx, ty, sw=0.9, color=GREY))
    o.append(_line(sx, ty, 372, ty, sw=0.9, color=GREY))
    o.append(_circle(sx, 52, 1.6, fill=INK, sw=0))


@_reg
def fig_f601():
    """Figure 6-1 -- ATEX/CENELEC marking, 'II 2G EEx de IIC T6'."""
    w, h = 680, 730
    o = [_defs()]
    o.append(T(340, 16,
               "Hình 6-1 · Ký hiệu ATEX/CENELEC / "
               "Figure 6-1 · ATEX/CENELEC marking breakdown",
               8.8, color=INK, weight="600"))

    # ---- the marking itself ----------------------------------------------
    o.append(_line(26, 52, 372, 52, sw=1.2, color=INK))
    for bx in (70, 124, 174, 230, 286, 336):
        o.append(_line(bx, 43, bx, 52, sw=0.8, color=GREY))
    o.append(_poly([(40, 28), (52, 35), (52, 49), (40, 56), (28, 49), (28, 35)],
                   fill=PAPER, sw=1.2, color=BLUE, close=True))
    o.append(T(40, 47, "Ex", 8.0, color=BLUE, weight="600"))
    segs = [(100, "II", BLUE), (146, "2G", BLUE), (200, "EEx", RED),
            (258, "de", RED), (310, "IIC", RED), (360, "T6", RED)]
    for sx, label, color in segs:
        o.append(T(sx, 43, label, 8.4, color=color, weight="600"))

    # ---- leader lines -----------------------------------------------------
    for sx, ty in ((40, 80), (100, 118), (146, 152),
                   (200, 420), (258, 454), (310, 488), (360, 560)):
        _leader(o, sx, ty)

    x = 380

    # Ex hexagon -> approval mark.
    o.append(T(x, 80, "Dấu phê duyệt cho thiết bị được cơ quan thử nghiệm EU chứng nhận", 6.6))
    o.append(T(x, 90, "Approved mark for apparatus certified by EU test authority", 6.6))

    # II -> equipment groups; small bracket for M1/M2 and group II.
    o.append(_line(372, 118, 372, 138, sw=0.9, color=GREY))
    for by in (118, 138):
        o.append(_line(372, by, 380, by, sw=0.9, color=GREY))
    o.append(T(x, 118, "Nhóm thiết bị I (khai khoáng) / Equipment group I (mining)",
               7.0, color=BLUE, weight="600"))
    o.append(T(x, 128, "Category M1 và M2 / Category M1 and M2", 6.6))
    o.append(T(x, 138, "Nhóm thiết bị II (trên mặt đất) / Equipment group II (on surface)",
               6.6, color=GREY))

    # 2G -> categories and their gas/dust zone definitions; single long bracket.
    o.append(_line(372, 152, 372, 372, sw=0.9, color=GREY))
    for by in (152, 196, 250, 294, 328, 362):
        o.append(_line(372, by, 380, by, sw=0.9, color=GREY))

    o.append(T(x, 152, "Category 1G, Vùng 0 / Category 1G, Zone 0", 7.0, color=BLUE, weight="600"))
    o.append(T(x, 162, "Môi trường khí nổ hiện diện liên tục hoặc trong thời gian dài", 6.6))
    o.append(T(x, 172, "Areas where explosive gas atmosphere is continuously present", 6.6))
    o.append(T(x, 182, "or present for long periods of time", 6.6))

    o.append(T(x, 196, "Category 2G, Vùng 1 / Category 2G, Zone 1", 7.0, color=BLUE, weight="600"))
    o.append(T(x, 206, "Môi trường khí nổ có khả năng xuất hiện trong vận hành bình thường", 6.6))
    o.append(T(x, 216, "hoặc dự kiến hiện diện thường xuyên", 6.6))
    o.append(T(x, 226, "Areas where explosive gas atmosphere is likely to occur in normal operation", 6.6))
    o.append(T(x, 236, "or can be expected to be present frequently", 6.6))

    o.append(T(x, 250, "Category 3G, Vùng 2 / Category 3G, Zone 2", 7.0, color=BLUE, weight="600"))
    o.append(T(x, 260, "Môi trường khí nổ ít có khả năng xuất hiện; nếu có thì chỉ tồn tại trong thời gian ngắn", 6.6))
    o.append(T(x, 270, "Area where explosive gas atmosphere is not likely to occur and if it does,", 6.6))
    o.append(T(x, 280, "it will only exist for a short period of time", 6.6))

    o.append(T(x, 294, "Category 1D, Vùng 20 / Category 1D, Zone 20", 7.0, color=BLUE, weight="600"))
    o.append(T(x, 304, "Bụi dễ cháy hiện diện liên tục hoặc thường xuyên", 6.6))
    o.append(T(x, 314, "Area where combustible dust is continuously or frequently present", 6.6))

    o.append(T(x, 328, "Category 2D, Vùng 21 / Category 2D, Zone 21", 7.0, color=BLUE, weight="600"))
    o.append(T(x, 338, "Đám mây bụi dễ cháy có khả năng xuất hiện trong vận hành bình thường", 6.6))
    o.append(T(x, 348, "Area where combustible dust clouds are likely to occur during normal operation", 6.6))

    o.append(T(x, 362, "Category 3D, Vùng 22 / Category 3D, Zone 22", 7.0, color=BLUE, weight="600"))
    o.append(T(x, 372, "Đám mây bụi dễ cháy có thể xuất hiện không thường xuyên trong vận hành bình thường", 6.6))
    o.append(T(x, 382, "Area where combustible dust clouds may occur infrequently during normal operation", 6.6))

    o.append(T(560, 290, "(G cho khí / G for Gas)", 6.2, color=GREY))
    o.append(T(560, 400, "(D cho bụi / D for Dust)", 6.2, color=GREY))

    # EEx, de, IIC, T6.
    o.append(T(x, 420, "Bảo vệ chống nổ theo tiêu chuẩn CENELEC EN 50…", 6.6))
    o.append(T(x, 430, "Explosion protected according to CENELEC standards EN 50…", 6.6))

    o.append(T(x, 454, "Phương pháp bảo vệ: d, e, p, i, o, q, m, n", 6.6))
    o.append(T(x, 464, "Methods of protection, d, e, p, i, o, q, m, n", 6.6))

    o.append(T(x, 488, "Nhóm thiết bị / Apparatus Group", 7.0, color=BLUE, weight="600"))
    o.append(T(x, 498, "I Khai khoáng – dưới lòng đất (mêtan); II Công nghiệp trên mặt đất", 6.6))
    o.append(T(x, 508, "I Mining – Underground (methane); II Surface Industries", 6.6))
    o.append(T(x, 518, "A (propan), B (etylen), C (hydro)", 6.6))
    o.append(T(x, 528, "A (propane), B (ethylene), C (hydrogen)", 6.6))

    o.append(T(x, 560, "Cấp nhiệt độ / Temperature Class", 7.0, color=BLUE, weight="600"))
    for i, s in enumerate(("T1 450° C", "T2 300° C", "T3 200° C",
                           "T4 135° C", "T5 100° C", "T6 85° C")):
        o.append(T(x, 572 + i * 9, s, 6.8, color=RED))

    # ---- in-SVG caption strip --------------------------------------------
    o.append(T(340, 700,
               "Hình 6-1 · Ký hiệu ATEX/CENELEC: II 2G EEx de IIC T6",
               6.8, color=INK))
    o.append(T(340, 714,
               "Figure 6-1 · ATEX/CENELEC marking: II 2G EEx de IIC T6",
               6.8, color=GREY))
    return _fig(svg(w, h, "".join(o),
                    esc("Sơ đồ phân tích ký hiệu ATEX/CENELEC: II 2G EEx de IIC T6")),
                "Hình 6-1 · Ký hiệu ATEX/CENELEC điển hình: II 2G EEx de IIC T6, với các đường dẫn giải thích nhóm thiết bị, danh mục, vùng khí và bụi, phương pháp bảo vệ, nhóm vật liệu và cấp nhiệt độ",
                "Figure 6-1 · Typical European ATEX/CENELEC marking: II 2G EEx de IIC T6, with leader-line definitions of equipment groups, categories, gas and dust zones, protection methods, apparatus groups and temperature classes.",
                "Sơ đồ ký hiệu ATEX/CENELEC với dấu Ex và đường dẫn từ II, 2G, EEx, de, IIC, T6 tới các định nghĩa về nhóm thiết bị, danh mục, vùng, phương pháp bảo vệ và cấp nhiệt độ",
                "ATEX/CENELEC marking diagram with the Ex hexagon and leaders from II, 2G, EEx, de, IIC and T6 to definitions of equipment groups, categories, zones, protection methods and temperature classes")
