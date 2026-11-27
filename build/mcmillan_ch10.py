# -*- coding: utf-8 -*-
"""Chapter 10 — Apparatus using protection concept flameproof enclosure 'd'.

Unofficial bilingual study reader of Alan McMillan, *Electrical Installations
in Hazardous Areas* (Butterworth-Heinemann, 1998), printed pp. 226-274
(PDF pp. 247-295). The chapter contains 29 printed figures, 15 printed
tables, 17 references, no numbered equations and no worked examples.

Prose is assembled from nine sequential source-order modules W1-W9. The shell
owns the chapter h2, the 17 printed references, the glossary, the source-quirk
note and the copyright line.
"""
from mcmillan_common import h2, note, p, refs

import mcmillan_ch10a as _a
import mcmillan_ch10b as _b
import mcmillan_ch10c as _c
import mcmillan_ch10d as _d
import mcmillan_ch10e as _e
import mcmillan_ch10f as _f
import mcmillan_ch10g as _g
import mcmillan_ch10h as _h
import mcmillan_ch10i as _i

PAGES_SRC = 49
BYLINE = "Alan McMillan · Electrical Installations in Hazardous Areas (Butterworth-Heinemann, 1998)"
TITLE_EN = "Apparatus using protection concept flameproof enclosure 'd'"
TITLE_VI = "Thiết bị theo nguyên lý vỏ chống cháy 'd'"

_SECTIONS = (_a, _b, _c, _d, _e, _f, _g, _h, _i)

_REFS = [
    "Phillips, H. (1971) (SMRE) Institution of Electrical Engineers conference, "
    "'Electrical Safety in Hazardous Environments'. The Basic Theory of the Flameproof Enclosure.",
    "BS 229 (1959) Flameproof Enclosure of Electrical Apparatus. (First published in 1926 and "
    "revised in 1929, 1940, 1946, 1957 and 1959).",
    "BS 4683 Electrical Apparatus for Explosive Atmospheres. Part 2 (1971). The Construction and "
    "Testing of Flameproof Enclosures of Electrical Apparatus.",
    "CENELEC Centre Européen de Normalization Electrique.",
    "BS 5501 Electrical Apparatus for Potentially Explosive Atmospheres. Part 5 (1977). "
    "Flameproof Enclosure 'd'.",
    "BS/EN 50018 (1995) Electrical Apparatus for Potentially Explosive Atmospheres. "
    "Flameproof Enclosure 'd'.",
    "IEC 79-1A (1975) Electrical Apparatus for Explosive Atmospheres. Part 1. Construction and "
    "Test of Flameproof Enclosures of Electrical Apparatus. Appendix D, Method of Test for "
    "Ascertainment of Maximum Experimental Safe Gap.",
    "IEC International Electrotechnical Commission.",
    "BS/EN 50019 (1994) Electrical Apparatus for Potentially Explosive Atmospheres. "
    "Increased Safety 'e'.",
    "ISO 468 (1982) Surface Roughness, Parameters, Their Values and General Rules for "
    "Specifying Requirements.",
    "BS 4500 (1990) ISO Limits and Fits. Part 1. General Tolerances and Deviations. Section 1.2, "
    "Tables of Commonly Used Tolerances and Grades and Limits Deviations for Holes and Shafts.",
    "BS/EN 50014 (1992) Electrical Apparatus for Potentially Explosive Atmospheres. "
    "General Requirements.",
    "ISO 6892 (1984) Metallic Materials, Tensile Testing.",
    "ISO 185 (1988) Grey Cast Iron, Classification.",
    "BS 5901:1980 Method of Test for Determining the Comparative and the Proof Tracking "
    "Indices for Solid Insulating Materials Under Moist Conditions.",
    "BS 5600: (1979) (1988) Powder Metallurgical Material and Products. Part 3. Methods of "
    "Testing Sintered Materials and Products, Excluding Hard Materials. Section 3.2, "
    "Determination of Density, Oil Content and Open Porosity. Section 3.5, Determination of "
    "Bubble Test Pore Size for Permeable Sintered Metal Materials. Section 3.6, Determination "
    "of Fluid Permeability.",
    "BS 5101 (1975) Specification for Lamp Caps and Holders Together with Gauges for the "
    "Control of Interchangeability and Safety. Part 1. Lamp Caps. Part 2. Lamp holders.",
]


def note_terms(lang):
    if lang == "vi":
        return ("<b>Thuật ngữ chính của chương.</b> vỏ chống cháy 'd' · nguyên lý bảo vệ · "
                "MESG · khe hở ngọn lửa · mối nối mặt bích · mối nối ren · mối nối xi măng · "
                "mối nối mở rộng · mối nối labyrinth · ổ bi · khe hở tối đa · chiều dài mối nối · "
                "thể tích vỏ bọc · nhóm IIA/IIB/IIC · áp suất thử · pressure piling · "
                "đầu vào trực tiếp/gián tiếp · cáp · đệm kín · chốt · giá đỡ chống cháy · "
                "BS/EN 50018 · BS 5501 · BS/EN 50014 · IEC 79-1A")
    return ("<b>Key terms in Chapter 10.</b> flameproof enclosure 'd' · protection concept · "
            "MESG · flamepath · flanged joint · threaded joint · cemented joint · spigot joint · "
            "labyrinth joint · sleeve and rolling-element bearings · maximum gap · joint length · "
            "enclosure volume · sub-groups IIA/IIB/IIC · test pressure · pressure piling · "
            "direct and indirect entry · cable gland · gasket · fastener · freestanding "
            "flameproof component · BS/EN 50018 · BS 5501 · BS/EN 50014 · IEC 79-1A")


def _source_note(lang):
    if lang == "vi":
        return ("<b>Đặc điểm của nguyên bản.</b> Chương gồm 49 trang in (226-274; in = PDF − 21), "
                "không có trang <i>MISSING PAGE</i> nào, và gồm 29 hình (10.1-10.29), 15 bảng "
                "(10.1-10.15), 17 tài liệu tham khảo, không phương trình được đánh số cũng không "
                "ví dụ tính toán. Mọi ô bảng, chú thích hình, khe hở, áp suất, ký hiệu tiêu chuẩn "
                "và năm được đối chiếu từ trang render vì lớp văn bản PDF bị xáo trộn (ví dụ "
                "'10.1 1', 'shaffs', 'IS0', '50018' bị đọc sai). Nhiều chi tiết in được giữ nguyên "
                "kèm ghi chú, gồm các ô không có dấu ≤ hoặc đóng ngoặc trong Bảng 10.8/10.10, "
                "cách viết 'neither … or', 'data sheet Fab of IEC 61', 'The point must comply', "
                "và chú thích BS 5101 mang số tham khảo 16 dù danh mục ghi 17. Không lỗi in nào "
                "được sửa lặng lẽ.")
    return ("<b>Source quirks.</b> The chapter spans 49 printed pages (226-274; printed = PDF − "
            "21), contains no <i>MISSING PAGE</i> placeholders, and has 29 figures (10.1-10.29), "
            "15 tables (10.1-10.15), 17 references, no numbered equations and no worked "
            "examples. Every table cell, figure caption, gap, pressure, standard designation and "
            "date was checked against the page renders because the PDF text layer is garbled "
            "(for example 'Fig. 10.1 1', 'shaffs', 'IS0' and misread '50018'). Several printed "
            "details are retained with notes: the missing '≤' sign in a Table 10.10 header, the "
            "unclosed parenthesis in Table 10.8, the 'neither … or' idiom, 'data sheet Fab of "
            "IEC 61', 'The point must comply' in the Fig. 10.29 caption, and a BS 5101 prose "
            "marker pointing to reference 16 although BS 5101 is reference 17. No printed error "
            "is silently corrected.")


def body_vi():
    b = [h2("10 — Thiết bị theo nguyên lý vỏ chống cháy 'd'",
            "10 — Apparatus using protection concept flameproof enclosure 'd'")]
    for m in _SECTIONS:
        b.append(m.body_vi())
    b.append(refs(_REFS))
    b.append(note(_source_note("vi")))
    b.append(p("<i>Đây là bản dịch không chính thức để học tập. Nội dung gốc © 1998 Reed "
               "Educational and Professional Publishing Ltd.</i>"))
    return "".join(b)


def body_en():
    b = [h2("10 — Apparatus using protection concept flameproof enclosure 'd'",
            "10 — Apparatus using protection concept flameproof enclosure 'd'")]
    for m in _SECTIONS:
        b.append(m.body_en())
    b.append(refs(_REFS))
    b.append(note(_source_note("en")))
    b.append(p("<i>This is an unofficial translation for study purposes. Original content "
               "© 1998 Reed Educational and Professional Publishing Ltd.</i>"))
    return "".join(b)
