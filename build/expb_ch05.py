# -*- coding: utf-8 -*-
"""Unit 5 - North American Equipment Certification /
Chứng nhận thiết bị Bắc Mỹ (EN/VI bilingual).

Source: R. STAHL, *Basics of Explosion Protection*, printed A9-A10 (PDF pp.
10-11): equipment certification by an accredited third party, follow-up
inspection, field-installed conduit/cable entries, the NEC 500 marking lines,
and the full NEC 505 marking with every leader definition.  One vector
figure (5-1), no tables.
"""
from expb_common import p, lead, h2, h3, h4, ul, ol, note, table, fig, refs

import expbfig05 as F

PAGES_SRC = 2
BYLINE = "R. STAHL · Basics of Explosion Protection (Innovative Explosion Protection)"
TITLE_EN = "North American Equipment Certification"
TITLE_VI = "Chứng nhận thiết bị Bắc Mỹ"

_NEC500 = [
    "Class I, Divisions 1 or 2, Groups A, B, C &amp; D, T4 (T-Code)",
    "Class II, Divisions 1 or 2, Groups E, F &amp; G, T4 (T-Code)",
    "Class III,",
    "Enclosure type 3, 4, 4X",
]

_NEC505_HEAD = "Class I, Zone 1, AEx de IIC T6"

_TEMP = "T1 450° C · T2 300° C · T3 200° C · T4 135° C · T5 100°C · T6 85° C"

_ZONES_VI = [
    "Vùng 0 — Môi trường khí nổ hiện diện liên tục hoặc trong thời gian dài.",
    "Vùng 1 — Môi trường khí nổ có khả năng xuất hiện trong vận hành bình thường "
    "hoặc dự kiến hiện diện thường xuyên.",
    "Vùng 2 — Môi trường khí nổ ít có khả năng xuất hiện; nếu có thì chỉ tồn tại "
    "trong thời gian ngắn.",
]

_ZONES_EN = [
    "Zone 0 — Areas where explosive gas atmosphere is continuously present or "
    "present for long periods of time.",
    "Zone 1 — Areas where explosive gas atmosphere is likely to occur in normal "
    "operation or can be expected to be present frequently.",
    "Zone 2 — Area where explosive gas atmosphere is not likely to occur and if "
    "it does, it will only exist for a short period of time.",
]


def note_terms(lang):
    if lang == "vi":
        return ("<b>Thuật ngữ chương 5.</b> chứng nhận thiết bị (equipment certification) · "
                "tiêu chuẩn quốc gia (National Standard) · tổ chức thử nghiệm bên thứ ba được "
                "công nhận (accredited third party testing organization) · kiểm tra theo dõi "
                "(follow-up inspection) · nhiều ký hiệu cho nhiều quốc gia · UL · FM · CSA · "
                "lắp tại hiện trường (field installed) · ống dẫn (conduit) · đầu vào cáp "
                "(cable entries) · bonding và grounding · NEC 500 · NEC 505 · T-Code · "
                "Class I, Zone 1, AEx de IIC T6 · AEx (tiêu chuẩn ANSI của Hoa Kỳ) · "
                "Vùng 0 / 1 / 2 · phương pháp bảo vệ d, e, p, i, o, q, m, n · "
                "nhóm thiết bị I / II · A (propan) / B (etylen) / C (hydro) · "
                "cấp nhiệt độ T1 đến T6")
    return ("<b>Key terms.</b> equipment certification · National Standard · accredited "
            "third party testing organization · follow-up inspection · multiple markings "
            "for multiple countries · UL · FM · CSA · field installed · conduit · cable "
            "entries · bonding and grounding · NEC 500 · NEC 505 · T-Code · "
            "Class I, Zone 1, AEx de IIC T6 · AEx (built to a US ANSI standard) · "
            "Zone 0 / 1 / 2 · methods of protection d, e, p, i, o, q, m, n · "
            "apparatus groups I / II · A (propane) / B (ethylene) / C (hydrogen) · "
            "temperature classes T1 through T6")


def body_vi():
    b = []
    b.append(h2(TITLE_VI, TITLE_EN))
    b.append(lead("Thiết bị dùng ở vị trí nguy hiểm phải được chứng nhận theo một Tiêu chuẩn "
                  "Quốc gia phù hợp và được tổ chức thử nghiệm bên thứ ba được công nhận gắn "
                  "ký hiệu tương ứng. Kiểm tra theo dõi để bảo đảm sự phù hợp là một phần của "
                  "chương trình chứng nhận."))
    b.append(p("Sản phẩm có thể mang nhiều ký hiệu cho nhiều quốc gia. Sau đây là mô tả tóm tắt "
               "về các yêu cầu quốc gia."))
    b.append(h3("Thông tin quan trọng về lập danh mục", "Important Listing Information"))
    b.append(p("Các yêu cầu cụ thể cho việc chứng nhận sản phẩm khác nhau giữa các quốc gia. "
               "Dù UL, FM và CSA có cách tiếp cận tương tự, vẫn tồn tại những khác biệt nhỏ."))
    b.append(p("Chứng nhận Bắc Mỹ cho phép lắp đầu vào ống dẫn hoặc cáp tại hiện trường, miễn "
               "là tuân thủ các yêu cầu thích hợp về bonding và grounding."))

    b.append(h3("Ký hiệu", "Marking"))
    b.append(h4("Ký hiệu điển hình của Bắc Mỹ theo NEC 500",
                "Typical North American Marking to NEC 500"))
    b.append(p("Các dòng ký hiệu điển hình theo NEC 500:"))
    b.append(ul(_NEC500))

    b.append(h4("Ký hiệu điển hình của Bắc Mỹ theo NEC 505",
                "Typical North American Marking to NEC 505"))
    b.append(p("Ký hiệu đầy đủ: " + _NEC505_HEAD + "."))
    b.append(fig(1, F.fig_f501()))

    b.append(h3("Giải thích ký hiệu NEC 505", "Reading the NEC 505 marking"))
    b.append(p("Ký hiệu " + _NEC505_HEAD + " được chia thành các phần, mỗi phần được giải "
               "nghĩa bằng một đường dẫn trong Hình 5-1:"))
    b.append(ul([
        "Class I (khí và hơi).",
    ] + _ZONES_VI + [
        "AEx chỉ thiết kế theo tiêu chuẩn ANSI của Hoa Kỳ.",
        "Phương pháp bảo vệ: d, e, p, i, o, q, m, n.",
        "Nhóm thiết bị: I Khai khoáng – dưới lòng đất (mêtan); II Công nghiệp trên mặt đất.",
        "A (propane), B (ethylene), C (hydrogen).",
        "Cấp nhiệt độ: " + _TEMP + ".",
    ]))
    b.append(note("<b>Đặc điểm của nguyên bản.</b> Chương gồm hai trang in (A9–A10; trang in "
                  "= trang PDF − 1), có một hình vector và không có bảng. Mọi ký hiệu và giá "
                  "trị gốc được giữ nguyên: các dòng ký hiệu NEC 500 và NEC 505, cách diễn đạt "
                  "Vùng 0/1/2, phương pháp bảo vệ d, e, p, i, o, q, m, n, nhóm thiết bị I/II "
                  "và A/B/C, cùng các cấp nhiệt độ T1 450° C đến T6 85° C."))
    b.append(p("<i>Đây là bản dịch không chính thức, dùng cho mục đích học tập. Nội dung "
               "gốc © R. STAHL, Basics of Explosion Protection.</i>"))
    return "".join(b)


def body_en():
    b = []
    b.append(h2(TITLE_EN, TITLE_EN))
    b.append(lead("Equipment for use in hazardous locations must be certified to an "
                  "appropriate National Standard and marked as such by an accredited third "
                  "party testing organization. Follow-up inspection to ensure conformance "
                  "is part of the program."))
    b.append(p("Products may carry multiple markings for multiple countries. The following "
               "is a brief description of the National Requirements."))
    b.append(h3("Important Listing Information"))
    b.append(p("The specific requirements for product certification vary from country to "
               "country. While UL, FM and CSA are similar in their approach, subtle "
               "differences still exist."))
    b.append(p("North American certifications permit conduit or cable entries to be field "
               "installed provided appropriate bonding and grounding requirements are "
               "followed."))

    b.append(h3("Marking"))
    b.append(h4("Typical North American Marking to NEC 500"))
    b.append(p("The typical North American marking to NEC 500:"))
    b.append(ul(_NEC500))

    b.append(h4("Typical North American Marking to NEC 505"))
    b.append(p("The full marking is " + _NEC505_HEAD + "."))
    b.append(fig(1, F.fig_f501()))

    b.append(h3("Reading the NEC 505 marking"))
    b.append(p("The marking " + _NEC505_HEAD + " is divided into elements, each explained by "
               "a leader line in Figure 5-1:"))
    b.append(ul([
        "Class I (Gases and Vapors).",
    ] + _ZONES_EN + [
        "AEx designates built to a US ANSI standard.",
        "Methods of protection, d, e, p, i, o, q, m, n.",
        "Apparatus Group: I Mining – Underground (methane); II Surface Industries.",
        "A (propane), B (ethylene), C (hydrogen).",
        "Temperature class: " + _TEMP + ".",
    ]))
    b.append(note("<b>Source quirks.</b> The unit spans two printed pages (A9-A10; printed = "
                  "PDF page - 1), with one vector figure and no tables. All original codes "
                  "and values are retained: the NEC 500 and NEC 505 marking lines, the Zone "
                  "0/1/2 wording, protection methods d, e, p, i, o, q, m, n, apparatus groups "
                  "I/II and A/B/C, and temperature classes T1 450° C through T6 85° C."))
    b.append(p("<i>This is an unofficial translation for study purposes. Original content "
               "© R. STAHL, Basics of Explosion Protection.</i>"))
    return "".join(b)
