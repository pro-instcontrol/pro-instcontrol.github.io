# -*- coding: utf-8 -*-
"""Book 9, Chapter 10 - Models for the Reliability Analysis of Digital
Instrumentation and Control Systems for Nuclear Power Plants
(EN/VI bilingual).

Source: Pinto, Gomes, Saldanha, Furieri and Frutuoso e Melo, in L. N. Jalali
(ed.), *Handbook on Power Plant Instrumentation and Control* (Bibliotex, 2019),
PDF pp. 245-269, printed pp. 229-253 (printed = PDF - 16; PDF p.270 blank).
PAGES_SRC = 25. The chapter has 5 vector figures, 12 tables, numbered
equations (1)-(8) and 25 references. The prose is assembled from five
source-order section modules and the figures from three vector suppliers.
"""
import ppic_common as C          # noqa: F401  (page shell, used by C.build)
import ppicfig10 as F            # noqa: F401  (figure registry, loaded first)
from ppic_common import h3, note, p
import ppic_ch10a as _a          # noqa: E402
import ppic_ch10b as _b          # noqa: E402
import ppic_ch10c as _c          # noqa: E402
import ppic_ch10d as _d          # noqa: E402
import ppic_ch10e as _e          # noqa: E402

PAGES_SRC = 25
BYLINE = ("Jonathan M. O. Pinto · Ian B. Gomes · Pedro L. C. Saldanha · "
          "Eustério B. Furieri · Paulo F. F. e Melo · "
          "Handbook on Power Plant Instrumentation and Control (Bibliotex, 2019)")
TITLE_EN = ("Models for the Reliability Analysis of Digital Instrumentation "
            "and Control Systems for Nuclear Power Plants")
TITLE_VI = ("Mô hình phân tích độ tin cậy của hệ thống thiết bị đo và điều "
            "khiển số cho nhà máy điện hạt nhân")

_SECTIONS = (_a, _b, _c, _d, _e)


def note_terms(lang):
    if lang == "vi":
        return ("<b>Thuật ngữ chương 10.</b> độ tin cậy · phân tích rủi ro xác suất "
                "(PSA) · hệ thống điều khiển và thiết bị đo số (digital I&amp;C) · DFM "
                "(Dynamic Flowgraph Methodology) · Markov/CCMT · Cell-to-Cell "
                "Mapping Technique · nút quá trình (PN) · nút điều kiện (CN) · hộp "
                "truyền (TB) · hộp chuyển (TT) · bảng quyết định · implicant chính "
                "(prime implicant) · sự kiện đỉnh (top event) · FMEA · CVSS · "
                "phân vùng ô trạng thái · CPU chính và CPU dự phòng · lỗi nguyên "
                "nhân chung (CCF) · SCCF · defence-in-depth · đa dạng (diversity) · "
                "SAPHIRE · DYAMONDA · van nước cấp · mức nước trong bình sinh hơi")
    return ("<b>Key terms.</b> reliability · probabilistic safety assessment (PSA) · "
            "digital instrumentation and control (I&amp;C) · Dynamic Flowgraph "
            "Methodology (DFM) · Markov/CCMT · Cell-to-Cell Mapping Technique · "
            "process node (PN) · condition node (CN) · transfer box (TB) · "
            "transition box (TT) · decision table · prime implicant · top event · "
            "FMEA · CVSS · state-cell partitioning · Main CPU and Backup CPU · "
            "common cause failure (CCF) · software CCF (SCCF) · defence-in-depth · "
            "diversity · SAPHIRE · DYAMONDA · feedwater valve · steam-generator "
            "water level")


def source_notes(lang):
    if lang == "vi":
        return ("<b>Đặc điểm của nguyên bản.</b> Lớp văn bản PDF bỏ sót toàn bộ "
                "phương trình và làm sai một số ký hiệu bảng; tám phương trình "
                "(1)–(8), nhãn các ô trạng thái và các số liệu bảng được đọc lại "
                "từ ảnh trang in. Năm hình gốc (sơ đồ hệ thống, hai sơ đồ Markov "
                "và hai đồ thị) được vẽ lại dạng vector. Bảng 6 có một dòng "
                "“Sprays” bị lặp lại trong bản in; Bảng 10 chuyển đơn vị từ m "
                "sang cm ở hai dòng cuối. Cả hai đặc điểm này được giữ nguyên "
                "và ghi chú, không sửa lặng lẽ. Mười hai bảng và 25 tài liệu "
                "tham khảo giữ nguyên số hiệu in.")
    return ("<b>Source quirks.</b> The PDF text layer omits every equation and "
            "garbles several table symbols; equations (1)-(8), the Markov state "
            "labels and all table numbers were re-read from the rendered printed "
            "pages. The five source figures (system layout, two Markov diagrams "
            "and two charts) were redrawn as vectors. Table 6 repeats a “Sprays” "
            "row in print, and Table 10 changes units from m to cm in its last "
            "two rows; both are preserved and flagged rather than silently fixed. "
            "All twelve tables and twenty-five references keep their printed "
            "numbers.")


def _body(lang):
    b = [C.lead(
        "Chương này so sánh hai phương pháp phân tích độ tin cậy cho hệ thống "
        "điều khiển và thiết bị đo số trong nhà máy điện hạt nhân: DFM và "
        "Markov/CCMT, qua hai nghiên cứu điển hình về bình áp lực và về điều "
        "khiển mức nước bình sinh hơi."
        if lang == "vi" else
        "This chapter compares two approaches to reliability analysis of digital "
        "instrumentation and control systems in nuclear power plants: DFM and "
        "Markov/CCMT, through case studies of a pressurizer and of steam-generator "
        "water-level control.")]
    for module in _SECTIONS:
        b.extend(module.section(lang))
    b.append(h3("Về nguồn tài liệu" if lang == "vi" else "About the source"))
    b.append(p(
        "Chương 10 chiếm PDF tr. 245–269, tương ứng tr. 229–253 của bản in "
        "(PDF tr. 270 để trống); PAGES_SRC = 25. Nguyên bản gồm năm hình, mười "
        "hai bảng, tám phương trình được đánh số và 25 tài liệu tham khảo."
        if lang == "vi" else
        "Chapter 10 occupies PDF pp. 245-269, corresponding to printed pp. 229-253 "
        "(PDF p.270 is blank); PAGES_SRC = 25. The printed chapter has five "
        "figures, twelve tables, eight numbered equations and twenty-five "
        "references."))
    b.append(note(source_notes(lang)))
    b.append(p(
        "<i>Đây là bản dịch không chính thức, dùng cho mục đích học tập. Nội dung "
        "gốc © 2019 Bibliotex; từng chương © tác giả tương ứng, theo giấy phép "
        "Creative Commons.</i>"
        if lang == "vi" else
        "<i>This is an unofficial translation for study purposes. Original content "
        "© 2019 Bibliotex; individual chapters © their authors, under a Creative "
        "Commons licence.</i>"))
    return "".join(b)


def body_vi():
    return _body("vi")


def body_en():
    return _body("en")
