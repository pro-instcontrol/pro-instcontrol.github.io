# -*- coding: utf-8 -*-
"""Chapter 15 — Protection concepts for apparatus for dust risks.

Unofficial bilingual study reader of Alan McMillan, *Electrical Installations
in Hazardous Areas* (Butterworth-Heinemann, 1998), printed pp. 456-473
(PDF pp. 477-494). The chapter contains two printed figures, two printed
tables and ten references, with no numbered equations.

Prose is assembled from three sequential source-order modules A-C. The shell
owns the chapter h2, the ten printed references, the glossary, the source-quirk
note and the copyright line.
"""
from mcmillan_common import h2, note, p, refs

import mcmillan_ch15a as _a
import mcmillan_ch15b as _b
import mcmillan_ch15c as _c

PAGES_SRC = 18
BYLINE = "Alan McMillan · Electrical Installations in Hazardous Areas (Butterworth-Heinemann, 1998)"
TITLE_EN = "Protection concepts for apparatus for dust risks"
TITLE_VI = "Nguyên lý bảo vệ thiết bị cho nguy cơ bụi"

_SECTIONS = (_a, _b, _c)

_REFS = [
    "BS 6467 — Electrical Apparatus with Protection by Enclosure for Use in the Presence of "
    "Combustible Dust. Part 1, (1985). Specification for Apparatus. Part 2 (1988). Guide to "
    "Selection, Installation and Maintenance.",
    "BS 7535 (1992) — Guide to the Selection of Apparatus Complying with BS 5501 or BS 6941 in "
    "the Presence of Combustible Dust.",
    "RoSPA/ICI — Engineering Codes and Regulations, Electrical Equipment in Flammable "
    "Atmospheres (1973). Group C (Electrical), Volume 1.5.",
    "BS/EN 60529 (1991) — Specification for Degrees of Protection Provided by Enclosure.",
    "BS 5490 (1977) (withdrawn) — Specification for Degrees of Protection Provided by Enclosure. "
    "This Standard has been replaced by BS/EN 60529 (1992).",
    "BS 5420 (1977) (withdrawn) — Specification for Degrees of Enclosure of Switchgear and "
    "Control Gear for Voltages up to and including 1000V ac and 1200V dc. This Standard has been "
    "replaced by BS/EN 60947-1 (1992).",
    "EN 60034 — General Requirements for Rotating Electrical Machines. Part 5 (1986). "
    "Classification of Degrees of Protection Provided by Enclosures for Rotating Machinery.",
    "BS 4999 — General Requirements for Rotating Electrical machines. Part 105 (1988). "
    "Classification of Degrees of Protection Provided by Enclosures for Rotating Machinery.",
    "BS/EN 50014 (1993) — Electrical Apparatus for Potentially Explosive Atmospheres. "
    "General Requirements.",
    "BS 6941 (1988) — Electrical Apparatus for Explosive Atmospheres with Type of "
    "Protection N.",
]


def note_terms(lang):
    if lang == "vi":
        return ("<b>Thuật ngữ chính của chương.</b> bụi dễ cháy · khu vực Zone 20 / 21 / 22 · "
                "vỏ kín bụi · vỏ chống bụi · IP5X / IP6X · nhiệt độ tự bắt cháy của bụi · "
                "đám mây bụi / lớp bụi · mối nối không có gioăng · mối nối bán cố định · "
                "vòng ‘o’ · tiết diện dẫn bảo vệ · BS 6467 · BS 7535 · BS/EN 60529 · BS 6941")
    return ("<b>Key terms in Chapter 15.</b> combustible dust · Zone 20 / 21 / 22 · dust tight "
            "enclosure · dust-protected enclosure · IP5X / IP6X · dust ignition temperature · "
            "dust cloud / dust layer · ungasketted joint · semi-permanent joint · ‘o’ ring · "
            "protective conductor cross-section · BS 6467 · BS 7535 · BS/EN 60529 · BS 6941")


def _source_note(lang):
    if lang == "vi":
        return ("<b>Đặc điểm của nguyên bản.</b> Chương gồm 18 trang in (456-473; in = PDF − 21), "
                "không có trang <i>MISSING PAGE</i> nào, và gồm 2 hình (15.1-15.2), 2 bảng "
                "(15.1-15.2) và 10 tài liệu tham khảo. Không có phương trình được đánh số hay "
                "phương trình trình bày riêng; mọi công thức và giá trị nhiệt độ đều nằm trong "
                "văn bản, bảng hoặc nhãn hình. Mọi nhãn hình, ô bảng, nhiệt độ, kích thước, ký "
                "hiệu tiêu chuẩn và năm được đối chiếu từ trang render vì lớp văn bản PDF bị "
                "xáo trộn (ví dụ OCR đọc ≥ thành ký tự sai, bỏ mất μm trong '6.3μm', đọc '‘o’ ring' "
                "thành số 0, và đảo thứ tự cột của tài liệu tham khảo). Nhiều chi tiết in được "
                "giữ nguyên kèm ghi chú, gồm '{[280 × 2/3] − 10)', quy tắc 85 °C nhưng phép tính "
                "'225 − 75 − 10', thứ tự hàng T1/T4/T2/T3/T5/T6 và dấu ngoặc kép '‘N(’n’)’'. "
                "Không lỗi in nào được sửa lặng lẽ.")
    return ("<b>Source quirks.</b> The chapter spans 18 printed pages (456-473; printed = "
            "PDF − 21), contains no <i>MISSING PAGE</i> placeholders, and has 2 figures "
            "(15.1-15.2), 2 tables (15.1-15.2) and 10 references. There are no numbered or "
            "displayed equations; every formula and temperature value remains inline in prose, "
            "tables or figure labels. Every figure label, table cell, temperature, dimension, "
            "standard designation and date was checked against the page renders because the PDF "
            "text layer is garbled (for example the OCR flattens ≥, drops the μm in '6.3μm', "
            "reads '‘o’ ring' as a zero, and reorders the two reference columns). Many printed "
            "details are retained with notes, including '{[280 × 2/3] − 10)', the 85 °C rule "
            "against the '225 − 75 − 10' arithmetic, the T1/T4/T2/T3/T5/T6 row order and the "
            "doubled brackets in '‘N(’n’)’'. No printed error is silently corrected.")


def body_vi():
    b = [h2("15 — Nguyên lý bảo vệ thiết bị cho nguy cơ bụi",
            "15 — Protection concepts for apparatus for dust risks")]
    for m in _SECTIONS:
        b.append(m.body_vi())
    b.append(refs(_REFS))
    b.append(note(_source_note("vi")))
    b.append(p("<i>Đây là bản dịch không chính thức để học tập. Nội dung gốc © 1998 Reed "
               "Educational and Professional Publishing Ltd.</i>"))
    return "".join(b)


def body_en():
    b = [h2("15 — Protection concepts for apparatus for dust risks",
            "15 — Protection concepts for apparatus for dust risks")]
    for m in _SECTIONS:
        b.append(m.body_en())
    b.append(refs(_REFS))
    b.append(note(_source_note("en")))
    b.append(p("<i>This is an unofficial translation for study purposes. Original content "
               "© 1998 Reed Educational and Professional Publishing Ltd.</i>"))
    return "".join(b)
