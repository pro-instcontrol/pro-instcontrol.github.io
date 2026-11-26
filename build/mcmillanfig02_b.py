# -*- coding: utf-8 -*-
"""Vector redraws of Figures 2.2 to 2.4 in A. McMillan, *Electrical
Installations in Hazardous Areas*, Chapter 2 "Area Classification".

Fig. 2.2 is a blank form for collection of information on gases, vapours
and mists, Fig. 2.3 the matching form for dusts and Fig. 2.4 the LEAC
(List of Equipment for Area Classification) schedule. All are simplified
bilingual VI/EN SVG vectors, no raster art. Architecture mirrors
`mcmillanfig01_b.py`: each function returns the standard five-tuple
through `vfig._fig()` and is registered in `FIGS` by `_reg`.
"""
import sys
import os

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

from vfig import (GREY, INK, PAPER, _defs, _fig, _line, _rect, _txt, svg)

FIGS = {}


def _reg(f):
    FIGS[f.__name__] = f()
    return f


def esc(s):
    return (str(s).replace("&", "&amp;").replace("<", "&lt;")
            .replace(">", "&gt;").replace('"', "&quot;"))


def T(x, y, s, size=8.2, **kw):
    return _txt(x, y, esc(s), size, **kw)


def _title(o, vi, en):
    """Bilingual group heading above a form, Vietnamese first."""
    o.append(T(340, 26, vi, 9.6, color=INK, weight="600"))
    o.append(T(340, 42, en, 7.0, color=GREY))


def _foot(o, h, vi, en):
    """Printed figure caption below the ruled table."""
    o.append(T(340, h - 34, vi, 6.4, color=GREY))
    o.append(T(340, h - 18, en, 6.2, color=GREY))


def _grid(o, x, y, widths, header_h, row_h, nrows):
    """Draw the table frame, vertical column rules and empty row rules."""
    total = sum(widths)
    bottom = y + header_h + row_h * nrows
    o.append(_rect(x, y, total, header_h + row_h * nrows,
                   fill=PAPER, sw=1.2, stroke=INK))
    bx = x
    for wd in widths[:-1]:
        bx += wd
        o.append(_line(bx, y, bx, bottom, sw=0.6, color="#9a9a9a"))
    for i in range(nrows + 1):
        yy = y + header_h + i * row_h
        o.append(_line(x, yy, x + total, yy, sw=0.6,
                       color=INK if i == 0 else "#9a9a9a"))
    return bottom


def _heads(o, x, y, widths, heads, size=7.0, lh=8.4, pad=7):
    """Centre the wrapped Vietnamese/English heading in each column."""
    bx = x
    for wd, lines in zip(widths, heads):
        cx = bx + wd / 2.0
        yy = y + pad + size
        for line in lines:
            o.append(T(cx, yy, line, size, color=INK))
            yy += lh
        bx += wd


@_reg
def fig_f202():
    """Figure 2.2 - Blank gas/vapour/mist information form."""
    w, h = 680, 440
    o = [_defs()]
    _title(o,
           "Tính chất của vật liệu dễ cháy — Khí/Hơi/Lỏng",
           "Properties of flammable materials — Gas/Vapour/Liquid")

    widths = [76, 52, 54, 54, 62, 57, 55, 46, 57, 57, 66]
    heads = [
        ["Mô tả vật liệu", "(Description of", "Material)"],
        ["Điểm cháy °C", "(Flash point", "°C)"],
        ["Điểm sôi ban", "đầu °C", "(Initial", "Boiling Point", "°C)"],
        ["Nhiệt độ tự", "cháy °C", "(Auto-Ignition", "Temp °C)"],
        ["Tỷ trọng khí/hơi", "Không khí = 1", "(Gas/Vapour", "Density Air = 1)"],
        ["Tỷ trọng", "khí/hơi", "(Gas/Vapour", "Density)"],
        ["Giới hạn cháy", "% vol", "(Flamm Range", "% Vol)"],
        ["Khối lượng", "phân tử", "(Mol. Wt.)"],
        ["Nhiệt ẩn hơi", "KJ/Kg", "(Lt. Ht. of", "Vap. KJ/Kg)"],
        ["Nhiệt dung", "KJ/Kg/K", "(Heat. Cap.", "KJ/Kg/K)"],
        ["Nhóm/Cấp T", "BS 5345", "(Group/T Class", "BS 5345)"],
    ]
    _grid(o, 22, 64, widths, 76, 40, 6)
    _heads(o, 22, 64, widths, heads)

    _foot(o, h,
          "Hình 2.2 · Mẫu thu thập thông tin về khí, hơi và sương mù.",
          "Figure 2.2 · Form for collection of information on gases, vapours and mists.")
    return _fig(svg(w, h, "".join(o),
                    esc("Bảng trống gồm mười một cột về tính chất khí, hơi và sương mù với sáu dòng trống")),
                "Hình 2-2 · Mẫu thu thập thông tin về khí, hơi và sương mù.",
                "Figure 2-2 · Form for collection of information on gases, vapours and mists.",
                "Bảng trống với các cột: Mô tả vật liệu; Điểm cháy; Điểm sôi ban đầu; Nhiệt độ tự cháy; "
                "Tỷ trọng khí/hơi và tỷ trọng so với không khí; Giới hạn cháy; Khối lượng phân tử; "
                "Nhiệt ẩn hơi; Nhiệt dung; Nhóm và cấp nhiệt độ BS 5345, kèm sáu dòng trống.",
                "Blank form with columns: Description of Material; Flash point; Initial Boiling Point; "
                "Auto-Ignition Temp; Gas/Vapour Density and density relative to air; Flammability Range; "
                "Molecular Weight; Latent Heat of Vapour; Heat Capacity; Group and T Class BS 5345, "
                "with six empty rows.")


@_reg
def fig_f203():
    """Figure 2.3 - Blank dust information form."""
    w, h = 680, 436
    o = [_defs()]
    _title(o,
           "Tính chất của vật liệu dễ cháy — Bụi",
           "Properties of flammable materials — Dust")

    widths = [86, 128, 82, 82, 104, 78, 76]
    heads = [
        ["Mô tả vật liệu", "(Description of", "Materials)"],
        ["Bụi dễ cháy ở", "nhiệt độ <110 °C", "và >110 °C",
         "(Is Dust Cloud", "Flammable at", "<110 °C and", ">110 °C)"],
        ["Nhiệt độ cháy", "đám bụi °C", "(Dust Cloud", "Ignition Temp °C)"],
        ["Nhiệt độ cháy", "lớp bụi °C", "(Dust Layer", "Ignition Temp °C)"],
        ["Có sinh hơi dễ", "cháy khi phân hủy", "(Are Flammable",
         "Vapours Evolved", "During", "Decomposition)"],
        ["Bụi có dẫn điện", "(Is Dust Conducting)"],
        ["Cấp nhiệt độ", "thiết bị T1–T6", "(Apparatus Temp.",
         "Class T1–T6)"],
    ]
    _grid(o, 22, 64, widths, 78, 38, 6)
    _heads(o, 22, 64, widths, heads)

    _foot(o, h,
          "Hình 2.3 · Mẫu thu thập thông tin về bụi.",
          "Figure 2.3 · Form for collection of information on dusts.")
    return _fig(svg(w, h, "".join(o),
                    esc("Bảng trống gồm bảy cột về tính chất dễ cháy của bụi với sáu dòng trống")),
                "Hình 2-3 · Mẫu thu thập thông tin về bụi.",
                "Figure 2-3 · Form for collection of information on dusts.",
                "Bảng trống với các cột: Mô tả vật liệu; Bụi có dễ cháy ở nhiệt độ dưới và trên 110 °C; "
                "Nhiệt độ cháy của đám bụi; Nhiệt độ cháy của lớp bụi; Hơi dễ cháy sinh ra khi phân hủy; "
                "Bụi có dẫn điện; Cấp nhiệt độ thiết bị T1 đến T6, kèm sáu dòng trống.",
                "Blank form with columns: Description of Materials; dust cloud flammability below and "
                "above 110 °C; Dust Cloud Ignition Temp; Dust Layer Ignition Temp; flammable vapours "
                "evolved during decomposition; Is Dust Conducting; Apparatus Temp Class T1 to T6, "
                "with six empty rows.")


@_reg
def fig_f204():
    """Figure 2.4 - Blank LEAC equipment schedule."""
    w, h = 680, 432
    o = [_defs()]
    _title(o,
           "Danh mục thiết bị để phân loại khu vực (LEAC)",
           "List of Equipment for Area Classification (LEAC)")

    widths = [48, 44, 46, 66, 66, 106, 70, 82, 58, 50]
    heads = [
        ["Số thiết bị", "(Equipment", "No.)"],
        ["Tên", "(Title)"],
        ["Vị trí", "(Location)"],
        ["Vật liệu công", "nghệ xử lý", "(Process", "Materials", "Handled)"],
        ["Điều kiện:", "Nhiệt độ &", "Áp suất", "(Conditions", "Temp & Pressure)"],
        ["Mô tả sự chứa", "đựng vật liệu", "công nghệ", "(Description of",
         "Process Material", "Containment)"],
        ["Nguồn nguy hiểm", "SH0/SH1/SH2", "hoặc phi NH",
         "(Source of Hazard", "SH0/SH1/SH2", "or Non-Haz)"],
        ["Khoảng cách ngang", "đến ranh giới", "Vùng 1 / Vùng 2",
         "(Horizontal Dist.", "to Zone 1 /", "Zone 2 boundary)"],
        ["Nhóm/Cấp", "nhiệt độ TB", "(Apparatus", "Group/Temp", "Class)"],
        ["Ghi chú", "(Remarks)"],
    ]
    _grid(o, 22, 64, widths, 76, 38, 6)
    _heads(o, 22, 64, widths, heads)

    _foot(o, h,
          "Hình 2.4 · Danh mục thiết bị để phân loại khu vực (LEAC).",
          "Figure 2.4 · List of equipment for area classification (LEAC).")
    return _fig(svg(w, h, "".join(o),
                    esc("Bảng danh mục thiết bị LEAC trống gồm mười cột và sáu dòng trống")),
                "Hình 2-4 · Danh mục thiết bị để phân loại khu vực (LEAC).",
                "Figure 2-4 · List of equipment for area classification (LEAC).",
                "Bảng trống với các cột: Số thiết bị; Tên; Vị trí; Vật liệu công nghệ xử lý; Điều kiện "
                "nhiệt độ và áp suất; Mô tả sự chứa đựng vật liệu; Nguồn nguy hiểm SH0, SH1, SH2 hoặc "
                "không nguy hiểm; Khoảng cách ngang đến ranh giới Vùng 1 hoặc Vùng 2; Nhóm và cấp nhiệt "
                "độ thiết bị; Ghi chú, kèm sáu dòng trống.",
                "Blank LEAC schedule with columns: Equipment No; Title; Location; Process Materials "
                "Handled; Conditions of temperature and pressure; Description of Process Material "
                "Containment; Source of Hazard SH0, SH1, SH2 or Non-Haz; Horizontal Distance to Zone 1 "
                "or Zone 2 boundary; Apparatus Group and Temp Class; Remarks, with six empty rows.")
