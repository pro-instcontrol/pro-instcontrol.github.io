# -*- coding: utf-8 -*-
"""Chapter 9 — Apparatus using protection concepts encapsulation 'm',
oil immersion 'o' and powder filling 'q'.

Unofficial bilingual study reader of Alan McMillan, *Electrical Installations
in Hazardous Areas* (Butterworth-Heinemann, 1998), printed pp. 209-225
(PDF pp. 230-246). The chapter contains two printed figures, three printed
tables, no numbered equations and no worked examples.

Prose is assembled from five sequential source-order modules W1-W5. The shell
owns the chapter h2, the 29 printed references plus the unnumbered BS 5784
line, the glossary, the source-quirk note and the copyright line.
"""
from mcmillan_common import h2, note, p, refs

import mcmillan_ch09a as _a
import mcmillan_ch09b as _b
import mcmillan_ch09c as _c
import mcmillan_ch09d as _d
import mcmillan_ch09e as _e

PAGES_SRC = 17
BYLINE = "Alan McMillan · Electrical Installations in Hazardous Areas (Butterworth-Heinemann, 1998)"
TITLE_EN = ("Apparatus using protection concepts encapsulation 'm', oil immersion 'o' "
            "and powder filling 'q'")
TITLE_VI = "Thiết bị theo nguyên lý bọc kín 'm', ngâm dầu 'o' và nhồi bột 'q'"

_SECTIONS = (_a, _b, _c, _d, _e)

_REFS = [
    "76/117/EEC Council Directive of 18 December 1975 on the approximation of the "
    "laws of the Member States concerning electrical equipment for use in potentially "
    "explosive atmospheres.",
    "94/9/EC Directive of the European Parliament and Council of 23 March 1994 on the "
    "approximation of the laws of Member States concerning equipment and protective "
    "systems intended for use in potentially explosive atmospheres.",
    "BS 5501 Electrical Apparatus for Potentially Explosive Atmospheres. Part 8 (1988). "
    "Encapsulation 'm'.",
    "BS 5501 Electrical Apparatus for Potentially Explosive Atmospheres. Part 1 (1977). "
    "General Requirements.",
    "BS/EN 50014 Electrical Apparatus for Potentially Explosive Atmospheres. Part 1 (1993). "
    "General Requirements.",
    "BS 5501 Electrical Apparatus for Potentially Explosive Atmospheres. Part 7 (1977). "
    "Intrinsic Safety 'i'.",
    "BS/EN 50020 (1994) Electrical Apparatus for Potentially Explosive Atmospheres. "
    "Intrinsic Safety 'i'.",
    "BS/EN 60127 (1991) Miniature Fuses. Part 1 Definitions for miniature fuses general "
    "requirements for miniature fuse-links. Part 2 Specification for cartridge fuse-links. "
    "Part 3 Specification for sub-miniature fuse-links.",
    "BS 5501 Electrical Apparatus for Potentially Explosive Atmospheres. Part 6 (1977). "
    "Increased Safety 'e'.",
    "BS/EN 50019 (1994) Electrical Equipment for Potentially Explosive Atmospheres. "
    "Increased Safety 'e'.",
    "BS 4265 (1977) (1984) Specification for Cartridge Fuse links for Miniature Fuses.",
    "IEC 269 Series of Standards for low voltage fuses.",
    "BS/EN 50015 (1994) Electrical Apparatus for Potentially Explosive Atmospheres. "
    "Oil Immersion 'o'.",
    "BS 5501 Electrical Apparatus for Potentially Explosive Atmospheres. Part 2 (1977). "
    "Oil Immersion 'o'.",
    "IEC 79-15 Electrical Apparatus for Explosive Gas Atmospheres. Part 15 (1987). "
    "Electrical Apparatus with Type of Protection 'n'.",
    "BS 6941 (1988) Electrical Apparatus for Explosive Atmospheres with Type of Protection 'n'.",
    "BS/EN 60529 (1991) Specification for Degrees of Protection provided by Enclosures (IP Code).",
    "IEC 296 (1969) Specification for New Insulating Oils for Transformers and Switchgear.",
    "IEC 296 (1982) Specification for Unused Mineral Insulating Oils for Transformers and Switchgear.",
    "IEC 836 (1988) Specifications for Silicone Liquids for Electrical Purposes.",
    "ISO 3104 (1976) Petroleum Products – Transparent and Opaque Liquids – Determination of "
    "Kinematic viscosity and Calculation of Dynamic Viscosity.",
    "BS 6664 Flashpoint of Petroleum Related Products. Part 5 (1990). Method for determination "
    "of flashpoint by Pensky-Martens closed tester.",
    "BS 5737 (1979) Method for Measurement of Relative Permittivity, Dielectric Dissipation "
    "Factor and dc Resistivity of Insulating Oils.",
    "BS 2000 Methods of Test for Petroleum and its Products. Part 15 (1993). Determination "
    "of Pour Point.",
    "IEC 588-2 Askarels for Transformers and Capacitors. Part 2 (1978). Test Methods.",
    "BS/EN 50017 (1994) Electrical Equipment for Potentially Explosive Atmospheres. "
    "Powder Filling 'q'.",
    "ISO 565 (1990) Test Sieves – Metal Wire Cloth, Perforated Metal Plate and Electro/Formed "
    "Sheet – Nominal Size of Openings.",
    "BS 2782 (1992) Methods of Testing Plastics. Method 140A – Determination of the Burning "
    "Behaviour of Horizontal and Vertical Specimens in contact with a Small-Flame Ignition Source.",
    "BS 5501 Electrical Apparatus for Potentially Explosive Atmospheres. Part 4 (1977). "
    "Powder Filling 'q'.",
    "BS 5784 Method for Determination of Electrical Strength of Insulating Oils (1980) "
    "(printed without a reference number).",
]


def note_terms(lang):
    if lang == "vi":
        return ("<b>Thuật ngữ chương 9.</b> bọc kín 'm' · ngâm dầu 'o' · nhồi bột 'q' · bảo vệ "
                "chống nổ · khái niệm bảo vệ · hợp chất đóng gói · chất lỏng bảo vệ · mức dầu · "
                "thiết bị thở · chất hút ẩm · van thông hơi · khe hở · điện áp đỉnh · khoảng cách "
                "rò · chỉ số CTI · vật liệu điền đầy · điện cực · cách ly · điện áp danh định · "
                "quá tải · dòng cầu chì · thử nhiệt độ · chu trình nhiệt · cells và bình ắc quy · "
                "đầu nối bên ngoài · mức bảo vệ IP · tiêu chuẩn BS/EN 50014 · BS/EN 50015 · "
                "BS/EN 50017 · BS 5501")
    return ("<b>Key terms in Chapter 9.</b> encapsulation 'm' · oil immersion 'o' · powder filling "
            "'q' · explosion protection · protection concept · encapsulating compound · "
            "protective fluid · oil level · breathing device · desiccant · vent · separation · "
            "peak voltage · creepage distance · CTI · filling material · electrode · insulation · "
            "rated voltage · overload · fuse current · temperature testing · temperature cycling · "
            "cells and batteries · external connections · IP code · BS/EN 50014 · BS/EN 50015 · "
            "BS/EN 50017 · BS 5501")


def _source_note(lang):
    if lang == "vi":
        return ("<b>Đặc điểm của nguyên bản.</b> Chương gồm 17 trang in (209-225; in = PDF − 21), "
                "không có trang <i>MISSING PAGE</i> nào, và gồm hai hình (9.1-9.2), ba bảng "
                "(9.1-9.3), không phương trình được đánh số cũng không ví dụ tính toán; danh mục "
                "29 tài liệu tham khảo cộng một dòng BS 5784 không đánh số nằm trên các trang in "
                "224-225. Mọi ô bảng, chú thích hình, giá trị điện áp/khoảng cách, ký hiệu tiêu "
                "chuẩn và năm được đối chiếu từ trang render vì lớp văn bản PDF bị xáo trộn (ví "
                "dụ '1OOOV dc', 'BS 550 1', '9.1. 1', '5001 5'). Nhiều chi tiết in được giữ nguyên "
                "kèm ghi chú: tiêu đề '9.7.7' cho mục thử nghiệm của 9.1 (nhiều khả năng là 9.1.7) "
                "và '9.2.7' cho mục kết cấu của 9.2 (nhiều khả năng là 9.2.1); 'BS 5501 part 8 "
                "(1998)' ở phần mở đầu so với (1988) ở tài liệu tham khảo 3; 'BS/EN 50019 (1993)' "
                "trong thân văn bản so với (1994) ở tài liệu tham khảo 10; 'BS 2782²⁸' trong thân "
                "văn bản; viết hoa 'Desiccant Holder' và 'exclude Water' trong chú thích Hình 9.1; "
                "và 'N/A⁶' trong Bảng 9.3. Không lỗi in nào được sửa lặng lẽ.")
    return ("<b>Source quirks.</b> The chapter spans 17 printed pages (209-225; printed = PDF − 21), "
            "contains no <i>MISSING PAGE</i> placeholders, and has two figures (9.1-9.2), three "
            "tables (9.1-9.3), no numbered equations and no worked examples; the 29 numbered "
            "references plus an unnumbered BS 5784 line are on printed pp.224-225. Every table "
            "cell, figure caption, voltage/separation value, standard designation and date was "
            "checked against the page renders because the PDF text layer is garbled (for example "
            "'1OOOV dc', 'BS 550 1', '9.1. 1' and '5001 5'). Several printed details are retained "
            "with notes: the heading '9.7.7' for the 9.1 type-testing section (almost certainly "
            "9.1.7) and '9.2.7' for the 9.2 construction section (almost certainly 9.2.1); "
            "'BS 5501 part 8 (1998)' in the opener against (1988) in reference 3; 'BS/EN 50019 "
            "(1993)' in prose against (1994) in reference 10; 'BS 2782²⁸' in prose; the "
            "'Desiccant Holder' and 'exclude Water' capitalisation in the Fig. 9.1 caption; and "
            "'N/A⁶' in Table 9.3. No printed error is silently corrected.")


def body_vi():
    b = [h2("9 — Thiết bị theo nguyên lý bọc kín 'm', ngâm dầu 'o' và nhồi bột 'q'",
            "9 — Apparatus using protection concepts encapsulation 'm', oil immersion 'o' "
            "and powder filling 'q'")]
    for m in _SECTIONS:
        b.append(m.body_vi())
    b.append(refs(_REFS))
    b.append(note(_source_note("vi")))
    b.append(p("<i>Đây là bản dịch không chính thức để học tập. Nội dung gốc © 1998 Reed "
               "Educational and Professional Publishing Ltd.</i>"))
    return "".join(b)


def body_en():
    b = [h2("9 — Apparatus using protection concepts encapsulation 'm', oil immersion 'o' "
            "and powder filling 'q'",
            "9 — Apparatus using protection concepts encapsulation 'm', oil immersion 'o' "
            "and powder filling 'q'")]
    for m in _SECTIONS:
        b.append(m.body_en())
    b.append(refs(_REFS))
    b.append(note(_source_note("en")))
    b.append(p("<i>This is an unofficial translation for study purposes. Original content "
               "© 1998 Reed Educational and Professional Publishing Ltd.</i>"))
    return "".join(b)
