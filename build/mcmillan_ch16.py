# -*- coding: utf-8 -*-
"""Chapter 16 — Other methods of protection and future apparatus requirements.

Unofficial bilingual study reader of Alan McMillan, *Electrical Installations
in Hazardous Areas* (Butterworth-Heinemann, 1998), printed pp. 474-481
(PDF pp. 495-502). The chapter contains two printed figures, no printed
tables and four references, with no numbered equations.

Prose is assembled from three sequential source-order modules A-C. The shell
owns the chapter h2, the four printed references, the glossary, the source-quirk
note and the copyright line.
"""
from mcmillan_common import h2, note, p, refs

import mcmillan_ch16a as _a
import mcmillan_ch16b as _b
import mcmillan_ch16c as _c

PAGES_SRC = 8
BYLINE = "Alan McMillan · Electrical Installations in Hazardous Areas (Butterworth-Heinemann, 1998)"
TITLE_EN = "Other methods of protection and future apparatus requirements"
TITLE_VI = "Phương pháp bảo vệ khác và yêu cầu thiết bị trong tương lai"

_SECTIONS = (_a, _b, _c)

_REFS = [
    "76/117/EEC (1975) — Council Directive on the Approximation of the Laws of Member States "
    "Concerning Equipment for Use in Potentially Explosive Atmospheres. 18 December.",
    "94/9/EC (1994) — European Parliament and Council Directive on the approximation of the "
    "Laws of Member States Concerning Equipment and Protective Systems for Use in Potentially "
    "Explosive Atmospheres. 23 March.",
    "EU Journal — The Journal of the European communities.",
    "CENELEC — Centre Européen de Normalization Electriques.",
]


def note_terms(lang):
    if lang == "vi":
        return ("<b>Thuật ngữ chính của chương.</b> Chỉ thị 76/117/EEC · Chỉ thị 94/9/EC · "
                "yêu cầu thiết yếu · cơ quan được thông báo · Giấy chứng nhận hợp quy · "
                "Giấy chứng nhận kiểm tra · Dấu cộng đồng (CE) · Dấu bảo vệ chống nổ (Ex) · "
                "dấu G / dấu D · hệ thống bảo vệ · an toàn nội tại ‘ia’ · Vùng 0 / 20 / 1 / 21 / "
                "2 / 22 · CENELEC · Tạp chí EU")
    return ("<b>Key terms in Chapter 16.</b> Directive 76/117/EEC · Directive 94/9/EC · "
            "essential requirements · notified body · Certificate of Conformity · Inspection "
            "Certificate · Community Mark (CE) · Explosion Protection Mark (Ex) · G mark / D "
            "mark · protective system · intrinsic safety ‘ia’ · Zone 0 / 20 / 1 / 21 / 2 / 22 "
            "· CENELEC · EU Journal")


def _source_note(lang):
    if lang == "vi":
        return ("<b>Đặc điểm của nguyên bản.</b> Chương gồm 8 trang in (474-481; in = PDF − 21), "
                "không có trang <i>MISSING PAGE</i> nào, và gồm 2 hình (16.1-16.2), không có "
                "bảng nào và 4 tài liệu tham khảo. Không có phương trình được đánh số hay "
                "phương trình trình bày riêng; mọi số Chỉ thị, tên Tiêu chuẩn và ngày tháng "
                "đều nằm trong văn bản. Mọi nhãn hình và chi tiết in được đối chiếu từ trang "
                "render vì lớp văn bản PDF bị xáo trộn, ví dụ OCR đọc chữ ‘q’ thành ‘4’, đọc "
                "‘16.2.2’ thành ‘76.2.2’, đọc số trang ‘481’ thành ‘48 1’, và đảo thứ tự cột "
                "của tài liệu tham khảo 3 và 4. Nhiều chi tiết in được giữ nguyên kèm ghi chú, "
                "gồm ‘Zone 0 and 1’, ‘not withstanding’, ‘formed by is own release’, "
                "‘in much the same vane’, ‘not has been’, ‘chapter 15’ viết thường và "
                "‘Chapters 9,10,11,12,13 and 15’ không có dấu cách sau dấu phẩy. Không lỗi in "
                "nào được sửa lặng lẽ.")
    return ("<b>Source quirks.</b> The chapter spans 8 printed pages (474-481; printed = "
            "PDF − 21), contains no <i>MISSING PAGE</i> placeholders, and has 2 figures "
            "(16.1-16.2), no printed tables and 4 references. There are no numbered or "
            "displayed equations; every Directive number, Standard designation and date "
            "remains inline in prose. Every figure label and printed detail was checked "
            "against the page renders because the PDF text layer is garbled: the OCR reads "
            "‘q’ as ‘4’, ‘16.2.2’ as ‘76.2.2’, the folio ‘481’ as ‘48 1’, and reorders the "
            "two columns of references 3 and 4. Many printed details are retained with "
            "notes, including ‘Zone 0 and 1’, ‘not withstanding’, ‘formed by is own release’, "
            "‘in much the same vane’, ‘not has been’, lowercase ‘chapter 15’ and "
            "‘Chapters 9,10,11,12,13 and 15’ without spaces after the commas. No printed "
            "error is silently corrected.")


def body_vi():
    b = [h2("16 — Phương pháp bảo vệ khác và yêu cầu thiết bị trong tương lai",
            "16 — Other methods of protection and future apparatus requirements")]
    for m in _SECTIONS:
        b.append(m.body_vi())
    b.append(refs(_REFS))
    b.append(note(_source_note("vi")))
    b.append(p("<i>Đây là bản dịch không chính thức để học tập. Nội dung gốc © 1998 Reed "
               "Educational and Professional Publishing Ltd.</i>"))
    return "".join(b)


def body_en():
    b = [h2("16 — Other methods of protection and future apparatus requirements",
            "16 — Other methods of protection and future apparatus requirements")]
    for m in _SECTIONS:
        b.append(m.body_en())
    b.append(refs(_REFS))
    b.append(note(_source_note("en")))
    b.append(p("<i>This is an unofficial translation for study purposes. Original content "
               "© 1998 Reed Educational and Professional Publishing Ltd.</i>"))
    return "".join(b)
