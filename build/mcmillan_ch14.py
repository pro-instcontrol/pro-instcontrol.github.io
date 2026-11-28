# -*- coding: utf-8 -*-
"""Chapter 14 — Apparatus using protection concept 'N' ('n').

Unofficial bilingual study reader of Alan McMillan, *Electrical Installations
in Hazardous Areas* (Butterworth-Heinemann, 1998), printed pp. 427-455
(PDF pp. 448-476). The chapter contains five printed figures, seven printed
tables and twenty-eight references, with no numbered equations.

Prose is assembled from three sequential source-order modules A-C. The shell
owns the chapter h2, the twenty-eight printed references, the glossary, the
source-quirk note and the copyright line.
"""
from mcmillan_common import h2, note, p, refs

import mcmillan_ch14a as _a
import mcmillan_ch14b as _b
import mcmillan_ch14c as _c

PAGES_SRC = 29
BYLINE = "Alan McMillan · Electrical Installations in Hazardous Areas (Butterworth-Heinemann, 1998)"
TITLE_EN = "Apparatus using protection concept 'N' ('n')"
TITLE_VI = "Thiết bị theo nguyên lý 'N' ('n')"

_SECTIONS = (_a, _b, _c)

_REFS = [
    "BS/CP 1003 (1967) — Part 3. Division 2 Areas.",
    "BS 4137 (1967) — Guide to the Selection of Electrical Equipment for Use in Division 2 Areas.",
    "BS 5345 — Installation and Maintenance of Electrical Apparatus for Use in Potentially "
    "Explosive Atmospheres. Part 1 (1976). Basic Requirements for All Parts of the Code.",
    "76/117/EEC (1975) — Council Directive on the Approximation of the Laws of Member States "
    "Concerning electrical Equipment for Use in Potentially Explosive Atmospheres. 18th December.",
    "94/9/EC (1994) — Directive of the European Parliament and Council on the Approximation of "
    "the Laws of Member States Concerning Electrical Equipment for Use in Potentially "
    "Explosive Atmospheres. 23rd March.",
    "BS 4683 — Electrical Apparatus for Explosive Atmospheres. Part 3 (1972). Type of Protection N.",
    "IEC — International Electrotechnical Commission.",
    "BS 6941 (1988) — Electrical Apparatus for Explosive Atmospheres with Type of Protection N.",
    "BS 5000 — Specification for Rotating Electrical Machines of Particular Types for Particular "
    "Applications. Part 16 (1972). Rotating Electrical Machines with Type of Protection N.",
    "BS 4533 (1976) — Luminaires: Part 101, Specification for General Requirements and Tests; "
    "Part 102 Particular Requirements: (Section 51) Specification for Luminaires with Type of "
    "Protection N.",
    "IEC 79–15 — Electrical Apparatus for Explosive Gas Atmospheres. Part 15 (1987). "
    "Electrical Apparatus With Type of Protection n.",
    "CENELEC — Comite Europeen de Normalisation Electrique.",
    "BS/EN 60529 (1988) — Specification for Classification of Degrees of Protection Provided by "
    "Enclosures (replaced BS 5490).",
    "BS 4999 — General Requirements for Rotating Electrical Machines. Part 105 (1988). "
    "Classification of Types of Enclosure.",
    "BS 5901 (1980) — Method of Test for Determining the Comparative and Proof Tracking Indices "
    "of Solid Insulating Materials under Moist Conditions.",
    "BS 5917 (1988) (withdrawn) — Specification for Conformal Coating Material for Use on Printed "
    "Circuit Assemblies. This Standard has been replaced by the following: BS/EN 61086-1 (1995); "
    "BS/EN 61086-2 (1995); BS/EN 60086-3 (1995).",
    "IEC 34 — Rotating Electrical Machines. Part 5 (1991). Classification of degrees of "
    "protection provided by the enclosures of rotating machines.",
    "BS 5042 (1987) — Specification for Lampholders and Starter Holders.",
    "BS 6776 (1990) (withdrawn) — Specification for Edison Screw Lampholders: this Standard has "
    "been replaced by BS/EN 60238 (1992).",
    "BS 6702 (1991) (withdrawn) — Specification for Lampholders for Tubular Fluorescent Lamps "
    "and Starter Holders: this Standard has been replaced by BS/EN 60400 (1992).",
    "BS 3772 (1980) — Specific for Starters for Fluorescent Lamps.",
    "BS 2818 (withdrawn) — Ballasts for Tubular Fluorescent Lamps. This standard has been "
    "replaced by the following: BS/EN 60920 (1991); BS/EN 60921 (1991).",
    "BS 4782 (1971) (withdrawn) — Specification for Ballasts for Discharge Lamps (Excluding "
    "Ballasts for Tubular Fluorescent Lamps). This standard has been replaced by the following: "
    "BS/EN 60922 (1991); BS/EN 60923 (1991).",
    "IEC 61 (1969) — Lamp Caps and Holders Together with Gauges for Control of "
    "Interchangeability and Safety.",
    "IEC 238 (1982) — Edison Screw Lampholders",
    "IEC 400 (1982) — Lampholders for Tubular Fluorescent Lamps and Starter Holders.",
    "IEC 262 (1969) — Ballasts for High Pressure Mercury Vapour Lamps.",
    "IEC 598–1 — Luminaires. Part 1 (1979). General Requirements and Tests.",
]


def note_terms(lang):
    if lang == "vi":
        return ("<b>Thuật ngữ chính của chương.</b> nguyên lý bảo vệ 'N' / 'n' · khu vực Zone 2 "
                "· thiết bị không phát tia lửa trong điều kiện làm việc bình thường · thiết bị đóng cắt kín "
                "· linh kiện không gây cháy · ngăn chặn truyền ngọn lửa · vỏ hở kín hạn chế hô hấp "
                "· mạch năng lượng hạn chế · hệ số hô hấp hạn chế S · điện trở đường dây · "
                "khoảng cách rò (creepage) · khoảng hở và khoảng cách phân tách · CTI · "
                "BS 6941 · IEC 79-15 · BS/EN 50019")
    return ("<b>Key terms in Chapter 14.</b> protection concept 'N' / 'n' · Zone 2 · non-sparking "
            "apparatus in normal operation · enclosed break device · non-incendive component · "
            "flame transmission · restricted breathing enclosure · energy limited circuit · "
            "restricted breathing factor S · L/R ratio · creepage · clearance and separation · "
            "CTI · BS 6941 · IEC 79-15 · BS/EN 50019")


def _source_note(lang):
    if lang == "vi":
        return ("<b>Đặc điểm của nguyên bản.</b> Chương gồm 29 trang in (427-455; in = PDF − 21), "
                "không có trang <i>MISSING PAGE</i> nào, và gồm 5 hình (14.1-14.5), 7 bảng "
                "(14.1-14.7) và 28 tài liệu tham khảo. Không có phương trình được đánh số hay "
                "phương trình trình bày riêng; công thức trong chú thích Bảng 14.2 và các điện áp "
                "thử được giữ dạng văn bản. Mọi nhãn hình, ô bảng, điện áp, dòng điện, nhiệt độ, "
                "khoảng cách, ký hiệu tiêu chuẩn và năm được đối chiếu từ trang render vì lớp văn "
                "bản PDF bị xáo trộn (ví dụ '74.5.1' thay vì 14.5.1, '±' bị đọc sai thành các ký "
                "tự khác, và '0.97 x lo5'). Nhiều chi tiết in được giữ nguyên kèm ghi chú, gồm "
                "'L/R ration', 'Notwithstanding ths', 'less then 40 °C', 'Specific for Starters' "
                "và mục 25 không có dấu chấm cuối. Không lỗi in nào được sửa lặng lẽ.")
    return ("<b>Source quirks.</b> The chapter spans 29 printed pages (427-455; printed = "
            "PDF − 21), contains no <i>MISSING PAGE</i> placeholders, and has 5 figures "
            "(14.1-14.5), 7 tables (14.1-14.7) and 28 references. There are no numbered or "
            "displayed equations; the Table 14.2 formula and the test voltages remain inline "
            "text. Every figure label, table cell, voltage, current, temperature, distance, "
            "standard designation and date was checked against the page renders because the PDF "
            "text layer is garbled (for example '74.5.1' for 14.5.1, '±' read as other stray "
            "characters, and '0.97 x lo5'). Many printed details are retained with notes, "
            "including 'L/R ration', "
            "'Notwithstanding ths', 'less then 40 °C', 'Specific for Starters' and the missing "
            "full stop in reference 25. No printed error is silently corrected.")


def body_vi():
    b = [h2("14 — Thiết bị theo nguyên lý 'N' ('n')",
            "14 — Apparatus using protection concept 'N' ('n')")]
    for m in _SECTIONS:
        b.append(m.body_vi())
    b.append(refs(_REFS))
    b.append(note(_source_note("vi")))
    b.append(p("<i>Đây là bản dịch không chính thức để học tập. Nội dung gốc © 1998 Reed "
               "Educational and Professional Publishing Ltd.</i>"))
    return "".join(b)


def body_en():
    b = [h2("14 — Apparatus using protection concept 'N' ('n')",
            "14 — Apparatus using protection concept 'N' ('n')")]
    for m in _SECTIONS:
        b.append(m.body_en())
    b.append(refs(_REFS))
    b.append(note(_source_note("en")))
    b.append(p("<i>This is an unofficial translation for study purposes. Original content "
               "© 1998 Reed Educational and Professional Publishing Ltd.</i>"))
    return "".join(b)
