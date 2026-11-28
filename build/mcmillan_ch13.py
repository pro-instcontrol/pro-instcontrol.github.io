# -*- coding: utf-8 -*-
"""Chapter 13 — Apparatus and systems using protection concept intrinsic safety 'i'.

Unofficial bilingual study reader of Alan McMillan, *Electrical Installations
in Hazardous Areas* (Butterworth-Heinemann, 1998), printed pp. 331-426
(PDF pp. 352-447). The chapter contains forty-five printed figures, twelve
printed tables and seventeen references.

Prose is assembled from six sequential source-order modules A-F. The shell
owns the chapter h2, the seventeen printed references, the glossary, the
source-quirk note and the copyright line.
"""
from mcmillan_common import h2, note, p, refs

import mcmillan_ch13a as _a
import mcmillan_ch13b as _b
import mcmillan_ch13c as _c
import mcmillan_ch13d as _d
import mcmillan_ch13e as _e
import mcmillan_ch13f as _f

PAGES_SRC = 96
BYLINE = "Alan McMillan · Electrical Installations in Hazardous Areas (Butterworth-Heinemann, 1998)"
TITLE_EN = "Apparatus and systems using protection concept intrinsic safety 'i'"
TITLE_VI = "Thiết bị và hệ thống theo nguyên lý an toàn nội tại 'i'"

_SECTIONS = (_a, _b, _c, _d, _e, _f)

_REFS = [
    "BS 1259 (1958) — Intrinsically Safe Electrical Apparatus and Circuits for use in "
    "Explosive Atmospheres.",
    "EECS/BASEEFA — Health and Safety Executive, Electrical Equipment Certification Service. "
    "British Approval Service for Electrical Equipment in Flammable Atmospheres.",
    "SFA 3012 (1972) — BASEEFA Certification Standard Intrinsic Safety.",
    "BS 5501 — Electrical Apparatus for Potentially Explosive Atmospheres. Part 7 (1977). "
    "Intrinsic Safety 'i'.",
    "EN 50020 (1977) — Electrical Apparatus for Potentially Explosive Atmospheres. "
    "Intrinsic Safety 'i'.",
    "PTB — Physikalisch Technische Bundesanstalt.",
    "IEC — International Electrotechnical Commission.",
    "IEC 79-11 — Electrical Apparatus for Explosive Gas Atmospheres. Part 11 (1984). "
    "Construction and Test of Intrinsically Safe and Associated Apparatus.",
    "CENELEC — Comité Européen de Normalisation Électrique.",
    "BS/EN 50020 (1995) — Electrical apparatus for Potentially Explosive Atmospheres. "
    "Intrinsic Safety 'i'.",
    "BS 5501 — Electrical Apparatus for Potentially Explosive Atmospheres. Part 9 (1982). "
    "Intrinsically Safe Systems 'i'.",
    "BS 5501 — Electrical Apparatus for Potentially Explosive Atmospheres. Part 1 (1977). "
    "General Requirements.",
    "BS/EN 60127 (1991) — Miniature Fuses. Part 1, Definitions for miniature fuses and general "
    "requirements for miniature fuse links. Part 2, Specification for Cartridge Fuse Links. "
    "Part 3, Specification for Sub-Miniature Fuse Links.",
    "HSE GS43 (1987) — Lithium Batteries.",
    "BS/EN 60529 (1991) — Specification for Degrees of Protection Provided by Enclosures (IP).",
    "BS 5901 (1980) — Method of Test for Determining the Comparative and the Proof Tracking "
    "Indices of Solid Insulating Materials Under moist Conditions.",
    "BS/EN 50019 (1985) — Electrical Apparatus for Potentially Explosive Atmospheres. "
    "Increased Safety 'e'.",
]


def note_terms(lang):
    if lang == "vi":
        return ("<b>Thuật ngữ chính của chương.</b> an toàn nội tại 'i' · thiết bị an toàn nội tại "
                "· thiết bị liên kết · hệ thống an toàn nội tại · mạch an toàn nội tại · "
                "thiết bị đơn giản · category 'ia' / 'ib' · hỏng hóc đếm được / không đếm được · "
                "thử tia lửa · dòng và năng lượng đánh lửa · hệ số an toàn · bề mặt nóng · "
                "linh kiện không thể hỏng · rào diode zener · thông số vào/ra · cáp liên kết · "
                "BS/EN 50020 · BS 5501 Part 9 · IEC 79-11")
    return ("<b>Key terms in Chapter 13.</b> intrinsic safety 'i' · intrinsically safe apparatus "
            "· associated apparatus · intrinsically safe system · intrinsically safe circuit · "
            "simple apparatus · category 'ia' / 'ib' · countable and non-countable faults · "
            "spark test apparatus · ignition current and energy · safety factors · hot surfaces · "
            "infallible components · zener diode safety barriers · input and output parameters · "
            "interconnecting cables · BS/EN 50020 · BS 5501 Part 9 · IEC 79-11")


def _source_note(lang):
    if lang == "vi":
        return ("<b>Đặc điểm của nguyên bản.</b> Chương gồm 96 trang in (331-426; in = PDF − 21), "
                "không có trang <i>MISSING PAGE</i> nào, và gồm 45 hình (13.1-13.45), 12 bảng "
                "(13.1-13.12) và 17 tài liệu tham khảo. Mọi nhãn hình, ô bảng, dòng điện, năng "
                "lượng, điện áp, nhiệt độ, ký hiệu tiêu chuẩn và năm được đối chiếu từ trang render "
                "vì lớp văn bản PDF bị xáo trộn (ví dụ 'Fig. 13.1 1', 'Table 13.1 2', '20 FJ', "
                "'25pH/Q', 'BSIEN 50020' và '13.70.4'). Nhiều chi tiết in được giữ nguyên kèm "
                "ghi chú. Không lỗi in nào được sửa lặng lẽ.")
    return ("<b>Source quirks.</b> The chapter spans 96 printed pages (331-426; printed = "
            "PDF − 21), contains no <i>MISSING PAGE</i> placeholders, and has 45 figures "
            "(13.1-13.45), 12 tables (13.1-13.12) and 17 references. Every figure label, table "
            "cell, current, energy, voltage, temperature, standard designation and date was "
            "checked against the page renders because the PDF text layer is garbled (for example "
            "'Fig. 13.1 1', 'Table 13.1 2', '20 FJ', '25pH/Q', 'BSIEN 50020' and '13.70.4'). "
            "Several printed details are retained with notes. No printed error is silently "
            "corrected.")


def body_vi():
    b = [h2("13 — Thiết bị và hệ thống theo nguyên lý an toàn nội tại 'i'",
            "13 — Apparatus and systems using protection concept intrinsic safety 'i'")]
    for m in _SECTIONS:
        b.append(m.body_vi())
    b.append(refs(_REFS))
    b.append(note(_source_note("vi")))
    b.append(p("<i>Đây là bản dịch không chính thức để học tập. Nội dung gốc © 1998 Reed "
               "Educational and Professional Publishing Ltd.</i>"))
    return "".join(b)


def body_en():
    b = [h2("13 — Apparatus and systems using protection concept intrinsic safety 'i'",
            "13 — Apparatus and systems using protection concept intrinsic safety 'i'")]
    for m in _SECTIONS:
        b.append(m.body_en())
    b.append(refs(_REFS))
    b.append(note(_source_note("en")))
    b.append(p("<i>This is an unofficial translation for study purposes. Original content "
               "© 1998 Reed Educational and Professional Publishing Ltd.</i>"))
    return "".join(b)
