# -*- coding: utf-8 -*-
"""Chapter 8 — General requirements for explosion protected apparatus
(gas, vapour and mist risks).

Unofficial bilingual study reader of Alan McMillan, *Electrical Installations
in Hazardous Areas* (Butterworth-Heinemann, 1998), printed pp. 178-208
(PDF pp. 199-229). The chapter contains nine printed figures, six printed
tables, no numbered equations and no worked examples.

Prose is assembled from six sequential source-order modules W1-W6. Figures
and tables are emitted by the modules that own them in brief `work/mcmillan_ch08_brief.md`.
The shell owns the chapter h2, the 19 printed references and end matter.
"""
from mcmillan_common import h2, note, p, refs

import mcmillan_ch08a as _a
import mcmillan_ch08b as _b
import mcmillan_ch08c as _c
import mcmillan_ch08d as _d
import mcmillan_ch08e as _e
import mcmillan_ch08f as _f

PAGES_SRC = 31
BYLINE = "Alan McMillan · Electrical Installations in Hazardous Areas (Butterworth-Heinemann, 1998)"
TITLE_EN = "General requirements for explosion protected apparatus (gas, vapour and mist risks)"
TITLE_VI = "Yêu cầu chung cho thiết bị bảo vệ chống nổ (nguy cơ khí, hơi và sương mù)"

_SECTIONS = (_a, _b, _c, _d, _e, _f)

_REFS = [
    "BS/EN 50014 (1993) Electrical Equipment for Potentially Explosive "
    "Atmospheres General Requirements.",
    "BS/EN 60529 (1991) Specification for Degrees of Protection Provided by "
    "Enclosures (IP Code).",
    "IS0 — The International Standards Organization (the non-electrical "
    "equivalent of CENELEC).",
    "IEC 216-1 — Guide for the determination of thermal endurance properties "
    "of electrical insulating materials. Part 1 (1987) General Guide-lines "
    "for Ageing and Evaluation of Test Results.",
    "IEC 216-2 (1974) — Guide for the Determination of Thermal Endurance "
    "Properties of Electrical Insulating Materials.",
    "BS 2782 (1975) — Methods of Testing Plastics. (IS0 178 (1975)) Part 3. "
    "Mechanical Properties.",
    "IEC R527 (1966) — Plastics — Determination of Tensile Properties.",
    "BS 3643 (1981) — Metric Screw Threads. IS0 262 (1973) Part 1. Principles "
    "and Basic Data.",
    "BS 3643 (1981) — Metric Screw Threads. (IS0 965-1 (1980)) Part 1. "
    "Principles and Basic Data. General Purpose Metric Screw Threads — "
    "tolerances. IS0 965-2 (1980) Part 2. Limits of Sizes for General Purpose "
    "Bolt and Nut Threads, Medium Quality.",
    "IS0 4014 (1988) — Hexagon Head Bolts — Product Grades A and B.",
    "IS0 4017 (1988) — Hexagon Head Screws — Product Grades A and B.",
    "IS0 4032 (1986) — Hexagon Nuts, Style 1 — Product Grades A and B.",
    "BS 4168 (1981) — Hexagon Socket Screws and Wrench Keys — Metric Sizes. "
    "(IS0 4762 (1989)) Part 1. Specification for Hexagon Socket Head Cap Screws.",
    "BS 4168 (1981) — Hexagon Socket Screws and Wrench Keys — Metric Sizes "
    "(IS0 4026 (1977)). Part 2. Specification for Hexagon Socket Set Screws "
    "with Flat Point.",
    "BS 4168 (1981) — Hexagon Socket Screws and Wrench Keys — metric Sizes. "
    "(IS0 4027 (1977)) Part 3. Specifications for Hexagon Socket Set Screws "
    "with Cone Point.",
    "BS 4168 (1981) — Hexagon Socket Screws and Wrench Keys — Metric Sizes. "
    "(IS0 4028 (1977)) Part 4. Specification for Hexagon Socket Set Screws "
    "with Dog Point.",
    "BS 4168 (1981) — Hexagon Socket Screws and Wrench Keys — Metric Sizes. "
    "(IS0 4029 (1977)) Part 5. Specification for Hexagon Socket Set Screws "
    "with Cup Point.",
    "BS 4500 (1990) — IS0 Limits and Fits. (IS0 286-2 (1988)) Part 1. "
    "General tolerances and Deviations. Section 1.2,1990 Tables of Commonly "
    "Used Tolerances and Grades and Limit Deviations for Holes and Shafts.",
    "BS 4999 (1988) — General Requirements for Rotating Electrical Machines. "
    "Part 105 Classification of Degrees of Protection Provided by Enclosures "
    "for Rotating Machines.",
]


def note_terms(lang):
    if lang == "vi":
        return ("<b>Thuật ngữ chương 8.</b> yêu cầu chung · thiết bị bảo vệ chống nổ · "
                "tiêu chuẩn BS/EN 50014 · điều khoản bắt buộc / khuyến nghị · định nghĩa · "
                "nhóm thiết bị I / II · phân nhóm IIA / IIB / IIC · năng lượng bắt lửa tối "
                "thiểu · tỷ lệ MIC · khe hở an toàn tối đa MESG · cấp nhiệt độ T1–T6 · "
                "nhiệt độ bề mặt · nhiệt độ tự nóng · vỏ bọc · thử va đập · thử rơi · "
                "mức bảo vệ IP · điện tích dư · vật liệu nhựa · chỉ số nhiệt độ · điện trở "
                "bề mặt · kim loại nhẹ · magiê · ốc vít · khóa liên động · bạc lót · mỡ "
                "chống lỏng · đầu nối · dây dẫn bảo vệ · cổng vào cáp · đấu nối cáp · "
                "thiết bị quay · cầu dao · cầu chì · phích cắm · đèn · bộ phận Ex · "
                "ký hiệu EEx · mã bảo vệ · điều kiện sử dụng đặc biệt 'X' · bộ phận 'U' · "
                "nhiệt độ môi trường Ta / Tamb · tốc độ thổi sạch")
    return ("<b>Key terms in Chapter 8.</b> general requirements · explosion protected "
            "apparatus · BS/EN 50014 · shall / should / must · definitions · Group I / II · "
            "sub-groups IIA / IIB / IIC · minimum ignition energy · MIC ratio · maximum "
            "experimental safe gap (MESG) · temperature classes T1–T6 · surface temperature "
            "· self-heating · enclosure · impact test · drop test · IP code · residual "
            "charge · plastics · temperature index · surface resistance · light metal · "
            "magnesium · fasteners · interlocking devices · bushings · cements · connection "
            "facilities · protective conductor · cable gland · conduit entry · rotating "
            "machine · switchgear · fuse · plug and socket · luminaire · Ex component · "
            "EEx code · protection concept symbol · special condition 'X' · component 'U' · "
            "ambient temperature Ta / Tamb · purge rate")


def _source_note(lang):
    if lang == "vi":
        return ("<b>Đặc điểm của nguyên bản.</b> Chương gồm 31 trang in (178-208; in = "
                "PDF − 21), không có trang <i>MISSING PAGE</i> nào, và gồm chín hình "
                "(8.1-8.9), sáu bảng (8.1-8.6), không phương trình được đánh số cũng "
                "không ví dụ tính toán; danh mục 19 tài liệu tham khảo nằm trên các "
                "trang in 207-208. Mọi ô bảng, chú thích hình, giá trị số, ký hiệu "
                "tiêu chuẩn và năm được đối chiếu từ trang render vì lớp văn bản PDF "
                "bị xáo trộn (ví dụ 'IS0' viết bằng số không, 'II' thành '11', 'IP10' "
                "thành 'IPlO', '1OOmm', 'Mi0', dấu độ bị mất). Nhiều chi tiết in được "
                "giữ nguyên kèm ghi chú: tiêu đề mục '8.7.4' in nhầm cho phần ốc vít; "
                "'1450 °C' in nhầm cho giới hạn T1; 'european' viết thường trong "
                "tiêu đề Bảng 8.1; Bảng 8.3 xáo trộn thứ tự dòng trong lớp văn bản "
                "(dòng 6 thực sự là 2/1 J theo trang in); các ký hiệu lớp US lịch sử "
                "và số La mã Đức trong Bảng 8.1; '3n'; nhận xét 'see Section 8.5.1' "
                "không khớp cấu trúc chương; và các dạng 'Exm' / 'Ex m'. Không lỗi "
                "in nào được sửa lặng lẽ.")
    return ("<b>Source quirks.</b> The chapter spans 31 printed pages (178-208; printed = "
            "PDF − 21), contains no <i>MISSING PAGE</i> placeholders, and has nine "
            "figures (8.1-8.9), six tables (8.1-8.6), no numbered equations and no worked "
            "examples; the 19 printed references are on printed pp.207-208. Every table "
            "cell, figure caption, numeric value, standard designation and date was "
            "checked against the page renders because the PDF text layer is garbled "
            "(for example 'IS0' with a zero, 'II' for '11', 'IP10' for 'IPlO', '1OOmm', "
            "'Mi0' and lost degree signs). Several printed details are retained with "
            "notes: the heading '8.7.4' printed for the fasteners section; '1450 °C' "
            "printed for the T1 limit; lower-case 'european' in the Table 8.1 caption; "
            "the text-layer row-order artifact in Table 8.3 (row 6 is 2/1 J on the "
            "printed page); the historic US class marks and German Roman numerals in "
            "Table 8.1; '3n'; the cross-reference 'see Section 8.5.1' that does not "
            "match the chapter structure; and both 'Exm' and 'Ex m'. No printed error "
            "is silently corrected.")


def body_vi():
    b = [h2("8 — Yêu cầu chung cho thiết bị bảo vệ chống nổ (nguy cơ khí, hơi và sương mù)",
            "8 — General requirements for explosion protected apparatus (gas, vapour and mist risks)")]
    for m in _SECTIONS:
        b.append(m.body_vi())
    b.append(refs(_REFS))
    b.append(note(_source_note("vi")))
    b.append(p("<i>Đây là bản dịch không chính thức để học tập. Nội dung gốc © 1998 Reed "
               "Educational and Professional Publishing Ltd.</i>"))
    return "".join(b)


def body_en():
    b = [h2("8 — General requirements for explosion protected apparatus (gas, vapour and mist risks)",
            "8 — General requirements for explosion protected apparatus (gas, vapour and mist risks)")]
    for m in _SECTIONS:
        b.append(m.body_en())
    b.append(refs(_REFS))
    b.append(note(_source_note("en")))
    b.append(p("<i>This is an unofficial translation for study purposes. Original content "
               "© 1998 Reed Educational and Professional Publishing Ltd.</i>"))
    return "".join(b)
