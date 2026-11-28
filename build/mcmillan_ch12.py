# -*- coding: utf-8 -*-
"""Chapter 12 — Apparatus with protection concept increased safety 'e'.

Unofficial bilingual study reader of Alan McMillan, *Electrical Installations
in Hazardous Areas* (Butterworth-Heinemann, 1998), printed pp. 296-330
(PDF pp. 317-351). The chapter contains sixteen printed figures, seven printed
tables, sixteen references, no numbered equations and no worked examples.

Prose is assembled from six sequential source-order modules A-F. The shell
owns the chapter h2, the sixteen printed references, the glossary, the
source-quirk note and the copyright line.
"""
from mcmillan_common import h2, note, p, refs

import mcmillan_ch12a as _a
import mcmillan_ch12b as _b
import mcmillan_ch12c as _c
import mcmillan_ch12d as _d
import mcmillan_ch12e as _e
import mcmillan_ch12f as _f

PAGES_SRC = 35
BYLINE = "Alan McMillan · Electrical Installations in Hazardous Areas (Butterworth-Heinemann, 1998)"
TITLE_EN = "Apparatus with protection concept increased safety 'e'"
TITLE_VI = "Thiết bị theo nguyên lý an toàn tăng cường 'e'"

_SECTIONS = (_a, _b, _c, _d, _e, _f)

_REFS = [
    "IEC 79-7 — Electrical Apparatus for Explosive Gas Atmospheres. Part 7 (1969). "
    "Increased Safety.",
    "BS 4683 — Specification for Electrical Apparatus for Explosive Atmospheres. "
    "Part 4 (1973). Type of Protection 'e'.",
    "BS 5501 — Electrical Apparatus for Potentially Explosive Atmospheres. "
    "Part 6 (1977). Increased Safety 'e'.",
    "BS/EN 50019 (1994) — Electrical Apparatus for Potentially Explosive Atmospheres. "
    "Increased Safety 'e'.",
    "BS/EN 60529 (1989) — Specification for Degrees of Protection Provided by Enclosures "
    "(IP Code).",
    "BS 4999 — General Requirements for Rotating Electrical Machines. Part 105 (1988). "
    "Classification of Degrees of Protection Provided by Enclosures for Rotating Machinery.",
    "BS/EN 50014 (1992) — Electrical Apparatus for Potentially Explosive Atmospheres. "
    "General Requirements.",
    "BS/EN 50018 (1995) — Electrical Apparatus for Potentially Explosive Atmospheres. "
    "Flameproof Enclosure 'd'.",
    "BS 2757 (1986) — Method for Determining the Thermal Classification of Electrical "
    "Insulation.",
    "BS 5901 (1980) — Method of Test for Determining the Comparative and Proof Tracking "
    "Indices of Solid Insulating Materials Under Moist Conditions.",
    "HD 555 (1992) — Specification for Particular Types of Winding Wires. Part 3, "
    "Polyester Enamelled Round Copper Wire, Class 155. Part 7, Polyimide Enamelled Round "
    "Copper Wire, Class 200. Part 8, Polyesterimide Enamelled Round Copper Wire, Class 180.",
    "BS 5971 (1988) — Specification for Safety of Tungsten Filament Lamps for Domestic and "
    "Similar General Lighting Purposes.",
    "BS 161 (1990) — Specification for Tungsten Filament Lamps for Domestic and Similar "
    "General Lighting Purposes. Performance Requirements.",
    "EN 60061-1 (1993) — Lamps and Holders Together with Gauges for the Control of "
    "Interchangeability and Safety. Part 1, Lampcaps; Part 2, Lampholders.",
    "92-0474 — The Incendivity of Electrical Discharge Activity in Rotating Electrical "
    "Machines. ERA Report, Bartels, A.L. and Bradford, M.",
    "HSE 498/12 (1992) — High Voltage Types Ex 'N and Ex 'e' Explosion Protected Motors "
    "Operating in Potentially Explosive Atmospheres. HSE Information Document.",
]


def note_terms(lang):
    if lang == "vi":
        return ("<b>Thuật ngữ chính của chương.</b> an toàn tăng cường 'e' · BS/EN 50019 · "
                "vùng 1 · tiếp điểm và đầu nối · chiều dài rò (creepage) · khe hở (clearance) · "
                "chỉ số theo dõi so sánh (CTI) · vật liệu cách điện · dây quấn · nhiệt độ giới hạn · "
                "đèn · cọc nối cáp · pin và ắc quy · thiết bị gia nhiệt · mô quay · "
                "rô-to lồng sóc · thời gian te · tỷ số dòng khởi động · thiết bị bảo vệ quá tải · "
                "IEC 79-7 · BS 5501 · BS/EN 50014 · BS/EN 60529")
    return ("<b>Key terms in Chapter 12.</b> increased safety 'e' · BS/EN 50019 · Zone 1 · "
            "terminals and connection facilities · creepage distance · clearance · comparative "
            "tracking index (CTI) · insulating material · windings · limiting temperature · "
            "luminaires · lampcaps · secondary batteries · heating devices · rotating machines · "
            "squirrel-cage rotor · te time · starting-current ratio · protective devices · "
            "IEC 79-7 · BS 5501 · BS/EN 50014 · BS/EN 60529")


def _source_note(lang):
    if lang == "vi":
        return ("<b>Đặc điểm của nguyên bản.</b> Chương gồm 35 trang in (296-330; in = PDF − 21), "
                "không có trang <i>MISSING PAGE</i> nào, và gồm 16 hình (12.1-12.16), 7 bảng "
                "(12.1-12.7), 16 tài liệu tham khảo, không phương trình được đánh số cũng không "
                "ví dụ tính toán. Mọi nhãn hình, ô bảng, kích thước, điện áp, nhiệt độ, ký hiệu "
                "tiêu chuẩn và năm được đối chiếu từ trang render vì lớp văn bản PDF bị xáo trộn "
                "(ví dụ 'BS/EN 5001 9 (1 994)', 'Fig. 12.1 1', 'IJn', 't, time' và 'IF’ Code'). "
                "Nhiều chi tiết in được giữ nguyên kèm ghi chú, gồm nhãn Hình 12.2 thiếu số "
                "'12.2', chú thích Figure continued trên các trang tiếp theo, các ký hiệu "
                "chân trái/phải của hình, 'spade/eylet', 'Flameoroof', và dấu chấm sau "
                "'BS 2757' và 'BS 5971'. Không lỗi in nào được sửa lặng lẽ.")
    return ("<b>Source quirks.</b> The chapter spans 35 printed pages (296-330; printed = "
            "PDF − 21), contains no <i>MISSING PAGE</i> placeholders, and has 16 figures "
            "(12.1-12.16), 7 tables (12.1-12.7), 16 references, no numbered equations and no "
            "worked examples. Every figure label, table cell, dimension, voltage, temperature, "
            "standard designation and date was checked against the page renders because the "
            "PDF text layer is garbled (for example 'BS/EN 5001 9 (1 994)', 'Fig. 12.1 1', "
            "'IJn', 't, time' and 'IF’ Code'). Several printed details are retained with notes: "
            "the Fig. 12.2 caption omits its number, several figures carry 'Figure continued' "
            "notes on following pages, the left/right legends of the creepage diagrams are "
            "uneven, and the source prints 'spade/eylet', 'Flameoroof' and full stops after "
            "'BS 2757' and 'BS 5971'. No printed error is silently corrected.")


def body_vi():
    b = [h2("12 — Thiết bị theo nguyên lý an toàn tăng cường 'e'",
            "12 — Apparatus with protection concept increased safety 'e'")]
    for m in _SECTIONS:
        b.append(m.body_vi())
    b.append(refs(_REFS))
    b.append(note(_source_note("vi")))
    b.append(p("<i>Đây là bản dịch không chính thức để học tập. Nội dung gốc © 1998 Reed "
               "Educational and Professional Publishing Ltd.</i>"))
    return "".join(b)


def body_en():
    b = [h2("12 — Apparatus with protection concept increased safety 'e'",
            "12 — Apparatus with protection concept increased safety 'e'")]
    for m in _SECTIONS:
        b.append(m.body_en())
    b.append(refs(_REFS))
    b.append(note(_source_note("en")))
    b.append(p("<i>This is an unofficial translation for study purposes. Original content "
               "© 1998 Reed Educational and Professional Publishing Ltd.</i>"))
    return "".join(b)
