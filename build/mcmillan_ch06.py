# -*- coding: utf-8 -*-
"""Chapter 6 — Area classification practice for dusts.

Unofficial bilingual study reader of Alan McMillan, *Electrical Installations
in Hazardous Areas* (Butterworth-Heinemann, 1998), printed pp. 149-163
(PDF pp. 170-184).  The chapter contains three printed figures, three printed
tables, no numbered equations and no worked examples.

Prose is assembled from four sequential source-order modules.  Table 6.1 is
owned by module A, Table 6.3 by module B, and the three figures by module C;
the two-page Table 6.2 insert is added here between modules A and B, matching
the printed page order.
"""
from mcmillan_common import note, p, refs, table

import mcmillan_ch06a as _a
import mcmillan_ch06b as _b
import mcmillan_ch06c as _c
import mcmillan_ch06d as _d
import mcmillan_tbl62 as _T62

PAGES_SRC = 15
BYLINE = "Alan McMillan · Electrical Installations in Hazardous Areas (Butterworth-Heinemann, 1998)"
TITLE_EN = "Area classification practice for dusts"
TITLE_VI = "Thực hành phân loại khu vực cho bụi"

_REFS = [
    "The Factories Act 1961.",
    "BS 6467 — Electrical Apparatus With Protection by Enclosure for Use in "
    "the Presence of Combustible Dust. Part 2 (1988). Guide to Selection, "
    "Installation and Maintenance.",
    "IEC 1241–3 — Electrical Apparatus for Use in the Presence of Combustible "
    "Dust. Part 3. Classification of Areas Where Combustible Dusts are or may "
    "be Present. (Draft 1994) (BS 94/213454 DC).",
    "IEC 1241–2 — Electrical Apparatus for Use in the Presence of Combustible "
    "Dust. Part 2, Test Methods: Section 1 (1994). Method for the "
    "Determination of the Minimum Ignition Temperature of Dust; Section 2 "
    "(1993). Method for the Determination of the Ignition Temperature of "
    "Dust in Layers; Section 3 (1993). Method for Determination of Minimum "
    "Ignition Energy for Dust/Air Mixtures.",
]


def note_terms(lang):
    if lang == "vi":
        return ("<b>Thuật ngữ chương 6.</b> bụi cháy được · bụi dễ cháy · đám mây bụi · "
                "lớp bụi lắng · dọn dẹp / vệ sinh công nghiệp · sự tích tụ · che chắn / bao "
                "kín · nguồn phát thải · khu vực nguy hiểm · phạm vi khu vực nguy hiểm · "
                "Vùng 20 / Vùng 21 / Vùng 22 · cấp phát thải liên tục / chính / phụ · "
                "nhiệt độ bắt lửa đám mây / lớp bụi · năng lượng bắt lửa · âm ỉ cháy · "
                "phân bố kích thước hạt · trung vị · độ ẩm · bụi dẫn điện · cyclone · túi "
                "lọc bụi · phễu chứa sản phẩm · khớp nối kín khí · thùng thu bụi · phễu / "
                "cửa nạp liệu · thổi khí vào trong · thông gió hút · thùng chứa kín · mặt "
                "bệ / cột chống · nồng độ nổ tối thiểu")
    return ("<b>Key terms in Chapter 6.</b> combustible dust · flammable dust · dust cloud · "
            "dust layer · housekeeping · accumulation · containment · source of release · "
            "hazardous area · hazardous area extent · Zones 20, 21 and 22 · continuous / "
            "primary / secondary grade source · cloud and layer ignition temperature · "
            "ignition energy · smouldering · particle size distribution · median · moisture "
            "content · conducting dust · cyclone · bag filter · product hopper · air sealed "
            "joint · dust collection drum · hopper / manhole · air purge inwards · extract "
            "ventilation · air sealed receptacle · ledges and stanchions · minimum explosive "
            "concentration")


def _source_note(lang):
    if lang == "vi":
        return ("<b>Đặc điểm của nguyên bản.</b> Chương gồm 15 trang in (149-163; "
                "in = PDF − 21), không có trang <i>MISSING PAGE</i> nào, và gồm ba "
                "hình (6.1-6.3), ba bảng (6.1-6.3), không phương trình được đánh số "
                "cũng không ví dụ tính toán. Mọi ô bảng, chú thích hình, kích thước và "
                "ký hiệu tiêu chuẩn được đối chiếu từ trang render vì lớp văn bản PDF "
                "bị xáo trộn (ví dụ 6.7.7 thành 6.1.1, IEC 1241-Z4 thành IEC 1241 – "
                "2⁴, BS/94/213454 LX4 thành BS/94/213454 DC⁴). Nhiều chi tiết in được "
                "giữ nguyên kèm ghi chú: cụm 'have historically been been classified', "
                "'and, is in definition, synonymous', số nhiều 'Factories Acts' trong "
                "thân văn bản so với tiêu đề tham khảo số một, các cách viết khác nhau "
                "của IEC 1241–2 / IEC 1241 – 2⁴, ghi chú (3) của Hình 6.2 ghi 'Zone 2', "
                "cách viết hoa trộn lẫn của x/y/z và X/y, các cụm '50-100' và '1-1.5' "
                "dùng dấu gạch nối, và câu bắt đầu bằng 'once again' thường thường. "
                "Bảng 6.2 giữ đơn vị 'mj' in thường, nồng độ g/l, các ô trống, mục "
                "'Melts' / 'No glowing to ... °C' và hai dòng polyacrylonitrile gần "
                "trùng. Không lỗi in nào được sửa lặng lẽ.")
    return ("<b>Source quirks.</b> The chapter spans 15 printed pages (149-163; "
            "printed = PDF − 21), contains no <i>MISSING PAGE</i> placeholders, and "
            "prints three figures (6.1-6.3), three tables (6.1-6.3), no numbered "
            "equations and no worked examples. Every table cell, caption, dimension "
            "and standard designation was checked against the page renders because "
            "the PDF text layer is garbled (for example 6.7.7 for 6.1.1, IEC 1241-Z4 "
            "for IEC 1241 – 2⁴, and BS/94/213454 LX4 for BS/94/213454 DC⁴). Several "
            "printed details are retained with notes: \"have historically been been "
            "classified\"; \"and, is in definition, synonymous\"; plural \"Factories "
            "Acts\" in the body against the singular reference title; the IEC "
            "1241–2 / IEC 1241 – 2⁴ variants; Figure 6.2 note (3) printing \"Zone "
            "2\"; the mixed case of x/y/z and X/y; the hyphens in \"50-100\" and "
            "\"1-1.5\"; and the sentence beginning lowercase \"once again\". Table "
            "6.2 keeps lowercase \"mj\", g/l units, blank cells, \"Melts\", \"No "
            "glowing to ... °C\", and two near-duplicate polyacrylonitrile rows. "
            "No printed error is silently corrected.")


def body_vi():
    b = [_a.body_vi()]
    b.append(table(_T62.HEAD_VI, _T62.ROWS, _T62.CAPTION_VI))
    b.append(note(_T62.NOTE_VI))
    b.append(_b.body_vi())
    b.append(_c.body_vi())
    b.append(_d.body_vi())
    b.append(refs(_REFS))
    b.append(note(_source_note("vi")))
    b.append(p("<i>Đây là bản dịch không chính thức để học tập. Nội dung gốc © 1998 Reed "
               "Educational and Professional Publishing Ltd.</i>"))
    return "".join(b)


def body_en():
    b = [_a.body_en()]
    b.append(table(_T62.HEAD_EN, _T62.ROWS, _T62.CAPTION_EN))
    b.append(note(_T62.NOTE_EN))
    b.append(_b.body_en())
    b.append(_c.body_en())
    b.append(_d.body_en())
    b.append(refs(_REFS))
    b.append(note(_source_note("en")))
    b.append(p("<i>This is an unofficial translation for study purposes. Original content "
               "© 1998 Reed Educational and Professional Publishing Ltd.</i>"))
    return "".join(b)
