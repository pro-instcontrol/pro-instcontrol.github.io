# -*- coding: utf-8 -*-
"""Book 7c, Chapter 14 - Pipe Data (EN/VI bilingual).

Source: Emerson, *Control Valve Handbook*, 6th ed. (2020), printed pp. 302-324.
Like Chapter 13, this is a pure data reference: 22 printed pages, ZERO figures,
almost entirely numeric pipe and flange dimension tables (pipe engagement,
carbon/alloy/stainless pipe schedules, American flange dimensions, and cast
steel flange standards PN 10 through PN 400).  The four sections are supplied
by modules cvh14_s1..s4; table DATA is language-neutral and shared verbatim,
while headings, prose, headers and captions are localized through cvh14_common.
"""

import cvh6_common as C  # noqa: F401
from cvh6_common import lead, note, p
from cvh13_common import T
import cvh14_s1, cvh14_s2, cvh14_s3, cvh14_s4

PAGES_SRC = 22         # source printed pp. 302-324 inclusive
BYLINE = "Emerson Flow Controls · Control Valve Handbook, 6th ed. (2020)"
TITLE_EN = "Pipe Data"
TITLE_VI = "Dữ liệu về ống"

SECTIONS = (cvh14_s1, cvh14_s2, cvh14_s3, cvh14_s4)


def note_terms(lang):
    """A one-line glossary box of the chapter's key terms."""
    if lang == "vi":
        return (
            "<b>Thuật ngữ chính của chương.</b> pipe engagement — chiều dài ren lắp ống · "
            "nominal pipe size (NPS) — cỡ ống danh nghĩa · nominal diameter (DN) — đường kính "
            "danh nghĩa · wall thickness — độ dày thành ống · schedule number — số cấp độ dày "
            "(SCH) · Std/XS/XXS — tiêu chuẩn / siêu dày / siêu dày đôi · outside diameter — đường "
            "kính ngoài · inside diameter — đường kính trong · transverse internal area — diện "
            "tích mặt cắt trong · bolt circle — vòng tròn bulông · stud bolt — bulông chốt · "
            "flange — mặt bích · flange thickness — chiều dày mặt bích · bolt hole — lỗ bulông · "
            "class — cấp áp lực · cast iron — gang đúc · steel — thép · carbon steel — thép các-bon "
            "· alloy steel — thép hợp kim · stainless steel — thép không gỉ · PN — áp suất danh "
            "nghĩa · raised face — mặt lồi · dimension — kích thước · mm — milimet")
    return (
        "<b>Key terms in this chapter.</b> pipe engagement · nominal pipe size (NPS) · nominal "
        "diameter (DN) · wall thickness · schedule number · Std/XS/XXS · outside diameter · inside "
        "diameter · transverse internal area · bolt circle · stud bolt · flange · flange thickness "
        "· bolt hole · class · cast iron · steel · carbon steel · alloy steel · stainless steel · "
        "PN · raised face · dimension · mm")


def source_notes(lang):
    """Data-fidelity and source-quirk notes for this reference chapter."""
    if lang == "vi":
        return (
            "<b>Ghi chú về nguồn.</b> (1) Đây là chương dữ liệu: 22 trang in (302–324), không có "
            "hình; gần như toàn bộ nội dung là bảng kích thước ống và mặt bích. Dữ liệu bảng (số, "
            "cỡ NPS/DN, cấp áp lực, ký hiệu ren M12…M56, đơn vị) được giữ nguyên và dùng chung cho "
            "cả hai bản ngôn ngữ; chỉ tiêu đề, văn bản, tiêu đề và chú thích bảng được dịch. "
            "(2) Các dòng «=== PAGE N ===», tiêu đề chạy, số trang và dòng «See Additional "
            "Resources »» được bỏ qua; các trang «...continued...» được gộp vào cùng một bảng có "
            "một hàng tiêu đề. (3) Bảng 14.2 rất rộng; mỗi cỡ ống (NPS/DN/OD) được trình bày như "
            "một nhóm, với các dòng cấp độ dày con bên dưới, để giữ nguyên cấu trúc nhiều dòng "
            "của bản in mà không làm mất giá trị nào. (4) Các ký hiệu «- - -» (giá trị không áp "
            "dụng), ghi chú chân (1)(2)(3), STD/XS/XXS và số SCH được giữ nguyên. (5) Một số quy "
            "ước in được giữ như đã in: NPS 16 có đường kính ngoài in là «1600» (có lẽ là 16.000); "
            "PN 63 bỏ qua DN 20; dấu gạch ngang ASCII và U+2212 trộn lẫn giữa các bảng. "
            "(6) Lỗi chính tả «1 thorough 8» trong ghi chú chân được giữ ở bản Anh. (7) Không có "
            "phương trình hay hình minh họa nào được thêm; mọi nội dung đều được chuyển từ bảng "
            "của nguồn.")
    return (
        "<b>Source notes.</b> (1) This is a data chapter: 22 printed pages (302-324), ZERO figures; "
        "almost all content is pipe and flange dimension tables. Table DATA (numbers, NPS/DN "
        "designations, class labels, thread designations M12...M56, units) is kept verbatim and "
        "shared between the two languages; only headings, prose, table headers and captions are "
        "translated. (2) The `=== PAGE N ===` markers, running headers, bare page numbers and "
        "`See Additional Resources »` boilerplate are skipped; `...continued...` pages are merged "
        "into one table with a single header row. (3) The very wide 14.2 table is presented with "
        "each pipe size (NPS/DN/OD) as a group band and its schedule sub-rows beneath, preserving "
        "the print's multi-line structure without dropping any value. (4) The `- - -` markers (not "
        "applicable), footnotes (1)(2)(3), STD/XS/XXS and SCH numbers are retained. (5) Several "
        "printed quirks are kept as-is: NPS 16 outside diameter prints as «1600» (likely 16.000); "
        "PN 63 omits DN 20; ASCII and U+2212 hyphens are mixed across tables. (6) The typo "
        "`1 thorough 8` in a footnote is retained in English. (7) No equations or figures are "
        "introduced; all content is transcribed from the source tables.")


def _body(lang):
    b = []
    vi = lang == "vi"

    b.append(lead(
        "Chương này tổng hợp dữ liệu kích thước ống và mặt bích dùng trong thiết kế đường ống: "
        "chiều dài ren lắp ống, thông số ống thép các-bon, thép hợp kim và thép không gỉ theo ASME "
        "B36.10M/B36.19M, kích thước mặt bích kiểu Mỹ theo ASME B16.1/B16.5/B16.24, và tiêu chuẩn "
        "mặt bích thép đúc từ PN 10 đến PN 400. Các bảng dữ liệu được chuyển nguyên vẹn từ bản in."
        if vi else
        "This chapter collects the pipe and flange dimension data used in piping design: pipe "
        "engagement thread lengths, carbon/alloy/stainless steel pipe schedules per ASME "
        "B36.10M/B36.19M, American flange dimensions per ASME B16.1/B16.5/B16.24, and cast steel "
        "flange standards from PN 10 through PN 400. The data tables are reproduced from the "
        "printed source."))
    b.append(note(note_terms("vi") if vi else note_terms("en")))

    for mod in SECTIONS:
        b.append(mod.section(lang))

    b.append("<h3>%s</h3>" % ("Ghi chú về nguồn" if vi else "Source notes"))
    b.append(note(source_notes("vi") if vi else source_notes("en")))

    b.append(p(
        "Chương 14 chiếm các trang in 302–324 của Emerson, Control Valve Handbook, ấn bản 6 "
        "(2020), gồm bốn mục 14.1–14.4 với nhiều bảng kích thước. Không có hình minh họa nào "
        "trong nguồn để vẽ lại."
        if vi else
        "Chapter 14 occupies printed pp. 302-324 (22 pages) of Emerson, Control Valve Handbook, "
        "6th edition (2020), covering four sections, 14.1-14.4, with numerous dimension tables. "
        "The source contains no figures to redraw."))
    b.append(p(
        "<i>Đây là bản dịch không chính thức, dùng cho mục đích học tập. Nội dung gốc © 2020 "
        "Emerson Flow Controls.</i>"
        if vi else
        "<i>This is an unofficial translation for study purposes. Original content © 2020 "
        "Emerson Flow Controls.</i>"))
    return "".join(b)


def body_vi():
    return _body("vi")


def body_en():
    return _body("en")
