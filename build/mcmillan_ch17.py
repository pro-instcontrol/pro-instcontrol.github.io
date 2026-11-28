# -*- coding: utf-8 -*-
"""Chapter 17 — Selection of power supply, apparatus and interconnecting cabling.

Unofficial bilingual study reader of Alan McMillan, *Electrical Installations
in Hazardous Areas* (Butterworth-Heinemann, 1998), printed pp. 482-502
(PDF pp. 503-523). The chapter contains three printed figures, four
unnumbered display blocks and ten references, with no numbered equations
and no tables.

Prose is assembled from three sequential source-order modules A-C. The shell
owns the chapter h2, the ten printed references, glossary, source-quirk note
and copyright.
"""
from mcmillan_common import h2, note, p, refs

import mcmillan_ch17a as _a
import mcmillan_ch17b as _b
import mcmillan_ch17c as _c

PAGES_SRC = 21
BYLINE = "Alan McMillan · Electrical Installations in Hazardous Areas (Butterworth-Heinemann, 1998)"
TITLE_EN = ("Selection of power supply, apparatus and interconnecting cabling system "
            "for both gas/vapour/mist risks and dust risks")
TITLE_VI = "Lựa chọn nguồn điện, thiết bị và hệ thống cáp liên kết cho cả nguy cơ khí/hơi/sương mù và bụi"

_SECTIONS = (_a, _b, _c)

_REFS = [
    "IEE (1991) — Regulations for Electrical Installations (16th edition).",
    "94/9/EC (1994) — Directive of the European Parliament and Council on the Approximation of "
    "the Laws of Member States concerning Equipment and Protective Systems for Use in "
    "Potentially Explosive Atmospheres 23 March.",
    "BS 5345 — Selection, Installation and Maintenance of electrical Apparatus for Use in "
    "Potentially Explosive Atmospheres (Other than Mining Applications or Explosive Processing "
    "and Manufacture): Part 1 (1989). General Recommendations; Part 4 (1977) Installation and "
    "Maintenance Requirements for Electrical Apparatus with Type of Protection ‘i’. Intrinsically "
    "Safe electrical Apparatus and Systems: Part 7 (1979). Installation and Maintenance "
    "Requirements for Electrical Apparatus with Type of Protection ‘N’.",
    "BS 6467 — Electrical Apparatus with Protection by Enclosure for Use in the Presence of "
    "Combustible Dusts. Part 1 (1985) Specification for Apparatus; Part 2 (1988) Guide to "
    "Selection, installation and maintenance.",
    "BS 7535 (1992) — Guide to the Use of Electrical Apparatus Complying with BS 5501 or BS 6941 "
    "in the Presence of Combustible Dust.",
    "BS/EN 60079 — Electrical Apparatus for Explosive Gas Atmospheres. Part 14 (1997) Electrical "
    "Installations in Explosive Gas Atmospheres.",
    "76/117/EEC (1975) — Council Directive on the Approximation of the Laws of Member States "
    "Concerning Electrical Equipment for Use in Potentially Explosive Atmospheres 18 December.",
    "IEC 332 — Tests on Electric Cables Under Fire Conditions. Part 1 (1993). Test on a Single "
    "Vertical Insulated Cable or Wire.",
    "BS 4568 — Specification for Steel Conduit and Fittings with Metric Threads of ISO Form for "
    "Electrical Installations. Part 1 (1970). Steel Conduit, Bends and Couplers; Part 2 (1970). "
    "Fittings and Components.",
    "BS 731 — Flexible Steel Conduit for Cable Protection and Flexible Steel Tubing to Enclose "
    "Flexible Drives. Part 1 (1952) Flexible Steel Conduit and Adaptors for the Protection of "
    "Electric Cable.",
]


def note_terms(lang):
    if lang == "vi":
        return ("<b>Thuật ngữ chính của chương.</b> hệ thống TN-C-S · hệ thống TN-S · dẫn dẫn "
                "PEN / PE · nối đất · bảo vệ quá dòng · cách ly · MIC · MESG · nhóm thiết bị IIA / "
                "IIB / IIC · cấp nhiệt độ T1–T6 · nhiệt độ môi trường · chứng nhận · Vùng 0 / 1 / "
                "2 · Vùng 20 / 21 / 22 · bọc kín ‘m’ · an toàn tăng cường ‘e’ · an toàn nội tại ‘i’ "
                "· tạo áp ‘p’ · chống cháy ‘d’ · kiểu ‘N’ ('n') · cáp bọc thép · ống dẫn · "
                "rào chắn cát · hộp chặn")
    return ("<b>Key terms in Chapter 17.</b> TN-C-S system · TN-S system · PEN / PE conductor · "
            "earthing · electrical protection · isolation · MIC · MESG · apparatus sub-groups IIA / "
            "IIB / IIC · temperature classes T1–T6 · ambient temperature · certification · Zone 0 / "
            "1 / 2 · Zone 20 / 21 / 22 · encapsulation ‘m’ · increased safety ‘e’ · intrinsic "
            "safety ‘i’ · pressurization ‘p’ · flameproof enclosure ‘d’ · Type ‘N’ ('n') · "
            "armoured cable · conduit · sand barrier · stopper box")


def _source_note(lang):
    if lang == "vi":
        return ("<b>Đặc điểm của nguyên bản.</b> Chương gồm 21 trang in (482-502; in = PDF − 21), "
                "không có trang <i>MISSING PAGE</i> nào, và gồm 3 hình (17.1-17.3), bốn khối trình "
                "bày không đánh số (Ma trận MIC/MESG, danh sách cấp nhiệt độ T6-T1, phương trình "
                "nhiệt độ bề mặt và bốn dòng giải thích ‘where’) cùng 10 tài liệu tham khảo. "
                "Không có bảng nào và không có phương trình được đánh số. Mọi nhãn hình, giá trị "
                "và câu chữ in được đối chiếu từ trang render vì lớp văn bản PDF bị xáo trộn rất "
                "nhiều. Nhiều chi tiết in được giữ nguyên kèm ghi chú, gồm ‘240 V rms’, "
                "‘nuisance rips’, ‘carbon disulphide in not addressed’, ‘exits’ trong Hình 17.3, "
                "giới hạn IIB dường như đảo ngược, danh sách T3-T1 liệt kê giảm dần, ‘94/9/EU’ "
                "trong thân bài, ‘ignition ignition’, ‘enlosures’, ‘raison d’être’, ‘Type ‘s’’, "
                "‘Flameproof enclosures ‘p’’, ‘(See Chapter 15)’, ‘(CSP)’ lặp lại, dấu chấm bị "
                "thiếu sau ‘60 V peak ac or dc’ và thứ tự hai cột của tài liệu tham khảo 6, 8, 9 "
                "bị OCR đảo lộn. Không lỗi in nào được sửa lặng lẽ.")
    return ("<b>Source quirks.</b> The chapter spans 21 printed pages (482-502; printed = "
            "PDF − 21), contains no <i>MISSING PAGE</i> placeholders, and has 3 figures "
            "(17.1-17.3), four unnumbered display blocks (the MIC/MESG inequalities, the T6-T1 "
            "temperature-class list, the surface-temperature equation and its four-line `where` "
            "key) and 10 references. There are no tables and no numbered equations. Every figure "
            "label, value and printed sentence was checked against the page renders because the "
            "PDF text layer is badly garbled. Many printed details are retained with notes, "
            "including ‘240 V rms’, ‘nuisance rips’, ‘carbon disulphide in not addressed’, "
            "‘exits’ in Fig. 17.3, the apparently inverted Sub-group IIB bounds, the descending "
            "T3-T1 list, ‘94/9/EU’ in body text, ‘ignition ignition’, ‘enlosures’, "
            "‘raison d’être’, ‘Type ‘s’’, ‘Flameproof enclosures ‘p’’, ‘(See Chapter 15)’, "
            "the duplicated ‘(CSP)’, the missing full stop after ‘60 V peak ac or dc’, and the "
            "OCR-scrambled two-column order of references 6, 8 and 9. No printed error is silently "
            "corrected.")


def body_vi():
    b = [h2("17 — Lựa chọn nguồn điện, thiết bị và hệ thống cáp liên kết",
            "17 — Selection of power supply, apparatus and interconnecting cabling")]
    for m in _SECTIONS:
        b.append(m.body_vi())
    b.append(refs(_REFS))
    b.append(note(_source_note("vi")))
    b.append(p("<i>Đây là bản dịch không chính thức để học tập. Nội dung gốc © 1998 Reed "
               "Educational and Professional Publishing Ltd.</i>"))
    return "".join(b)


def body_en():
    b = [h2("17 — Selection of power supply, apparatus and interconnecting cabling",
            "17 — Selection of power supply, apparatus and interconnecting cabling")]
    for m in _SECTIONS:
        b.append(m.body_en())
    b.append(refs(_REFS))
    b.append(note(_source_note("en")))
    b.append(p("<i>This is an unofficial translation for study purposes. Original content "
               "© 1998 Reed Educational and Professional Publishing Ltd.</i>"))
    return "".join(b)
