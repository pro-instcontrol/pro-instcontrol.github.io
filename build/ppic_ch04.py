# -*- coding: utf-8 -*-
"""Book 9, Chapter 4 — Nuclear Power Plant Instrumentation Fault Detection
Using Fuzzy Logic (EN/VI bilingual).

Source: Keith E. Holbert and Kang Lin, in L. N. Jalali (ed.), *Handbook on
Power Plant Instrumentation and Control* (Bibliotex, 2019), PDF pp. 65–94,
printed pp. 49–78. PAGES_SRC = 30 counts the whole source span.

The chapter has 11 numbered figures, four numbered tables, three printed
equation labels ((1), (2) and (4) — the source omits (3)), and 51 references.
Figures are redrawn in the `ppicfig4_*` suppliers; prose is assembled from
five source-order section modules.
"""
import ppic_common as C          # noqa: F401  (page shell, used by C.build)
from ppic_common import h3, note, p
import ppic_ch04a as _a          # noqa: E402
import ppic_ch04b as _b          # noqa: E402
import ppic_ch04c as _c          # noqa: E402
import ppic_ch04d as _d          # noqa: E402
import ppic_ch04e as _e          # noqa: E402

PAGES_SRC = 30
BYLINE = ("Keith E. Holbert · Kang Lin · School of Electrical, Computer and "
          "Energy Engineering, Arizona State University, USA")
TITLE_EN = "Nuclear Power Plant Instrumentation Fault Detection Using Fuzzy Logic"
TITLE_VI = "Phát hiện lỗi thiết bị đo trong nhà máy điện hạt nhân bằng logic mờ"

_SECTIONS = (_a, _b, _c, _d, _e)


def note_terms(lang):
    if lang == "vi":
        return ("<b>Thuật ngữ chính.</b> bảo trì khắc phục / phòng ngừa / dự đoán · bảo trì "
                "lấy độ tin cậy làm trung tâm (RCM) · quản lý tình trạng thiết bị · giám sát "
                "trực tuyến · logic mờ (fuzzy logic) · tập mờ · hàm thuộc · biến ngôn ngữ · "
                "suy luận mờ · phát hiện và cô lập lỗi (FDI) · tín hiệu dư · kiểm chứng cảm "
                "biến (sensor validation) · độ lệch δ · tần số xuất hiện τ · trạng thái tín "
                "hiệu s · độ lệch chuẩn σ · hiệu chuẩn · giảm hiệu chuẩn · hệ thống cơ sở dữ "
                "liệu dạng cây · ma trận luật · nồi áp · tín hiệu nhiệt độ lõi lò phản ứng · "
                "GLR · SPRT · phân tích thành phần chính · mạng nơ-ron · hệ chuyên gia · "
                "bảo trì dự báo.")
    return ("<b>Key terms.</b> corrective / preventive / predictive maintenance · "
            "reliability-centered maintenance (RCM) · condition monitoring · online "
            "monitoring · fuzzy logic · fuzzy set · membership function · linguistic "
            "variable · fuzzy inference · fault detection and isolation (FDI) · "
            "redundant signals · sensor validation · deviation δ · frequency of "
            "occurrence τ · signal status s · standard deviation σ · calibration · "
            "calibration reduction · tree-structured database · rule matrix · "
            "pressurizer · reactor core exit temperature · GLR · SPRT · principal "
            "component analysis · neural networks · expert systems · predictive maintenance.")


def source_notes(lang):
    if lang == "vi":
        return ("<b>Đặc điểm của nguyên bản.</b> Các hình trong PDF là ảnh raster; bản dịch "
                "vẽ lại dạng vector đơn giản nhưng giữ cấu trúc, đường tín hiệu, trục và nhãn "
                "được in trên trang. Phương trình (1), (2) và (4) được đọc trực tiếp từ trang "
                "in; nguyên bản không in phương trình (3) dù văn bản có nhắc đến ba giá trị tần "
                "suất mờ, nên bản dịch giữ nguyên đánh số (1), (2), (4) thay vì bịa thêm (3). "
                "Bốn bảng dữ liệu được chép lại với giá trị và tiêu đề gốc. Danh mục 51 tài "
                "liệu tham khảo được giữ nguyên thứ tự; một số mục có lỗi chính tả hoặc dấu "
                "ngoặc của nguyên bản được giữ trong bản Anh, còn bản Việt dùng cách viết "
                "chuẩn. Các ký hiệu «·» cuối một số mục tài liệu là dấu phân cách trong bản in.")
        return ("<b>Source quirks.</b> The figures are raster images in the PDF; they are "
                "redrawn as simplified vectors while retaining the printed topology, signal "
                "paths, axes and labels. Equations (1), (2) and (4) were read from the printed "
                "pages; the source does not print an equation (3) even though the prose "
                "mentions three fuzzy frequency values, so the original numbering (1), (2), "
                "(4) is kept rather than inventing a missing equation. The four data tables "
                "are transcribed with their original values and headings. All 51 references "
                "are retained in source order; minor spelling and punctuation quirks remain "
                "in the English text while the Vietnamese uses standard forms. Trailing "
                "middle dots in some reference entries are separators in the printed list.")


def _body(lang):
    vi = lang == "vi"
    b = [C.lead(
        "Bài báo trình bày cách dùng logic mờ để ra quyết định về trạng thái hệ thống và nhu "
        "cầu bảo trì thành phần, áp dụng giám sát chẩn đoán dựa trên logic mờ cho dữ liệu thu "
        "từ thiết bị đo trong các cơ sở đang vận hành."
        if vi else
        "This chapter describes the use of fuzzy logic for decision making about system "
        "status and the possible need for component maintenance, applying fuzzy-logic-based "
        "diagnostic monitoring to data acquired from instrumentation within operating "
        "facilities.")]
    for module in _SECTIONS:
        b.extend(module.section(lang))

    b.append(h3("Về nguồn tài liệu" if vi else "About the source"))
    b.append(p(
        "Chương 4 chiếm PDF tr. 65–94, tương ứng tr. 49–78 của bản in; PAGES_SRC = 30 đếm "
        "toàn bộ phân đoạn nguồn này. Nguyên bản gồm Tóm tắt, Mở đầu, Ứng dụng của logic mờ, "
        "Giám sát chẩn đoán bằng logic mờ, Giám sát hiệu chuẩn thiết bị, Tóm lược và 51 tài "
        "liệu tham khảo, cùng 11 hình (Figure 4.1 – Figure 4.11), bốn bảng (Table 4.1 – "
        "Table 4.4) và các phương trình đánh số (1), (2), (4)."
        if vi else
        "Chapter 4 occupies PDF pp. 65–94, corresponding to printed pp. 49–78; PAGES_SRC = 30 "
        "counts this whole source span. The source contains Abstract, Introduction, "
        "Applications of Fuzzy Logic, Fuzzy Logic Diagnostic Monitoring, Instrument "
        "Calibration Monitoring, Summary and 51 references, together with 11 figures "
        "(Figure 4.1 – Figure 4.11), four tables (Table 4.1 – Table 4.4) and the numbered "
        "equations (1), (2) and (4)."))
    b.append(note(source_notes(lang)))
    b.append(p(
        "<i>Đây là bản dịch không chính thức, dùng cho mục đích học tập. Nội dung gốc © 2019 "
        "Bibliotex; các chương của sách phát hành theo giấy phép Creative Commons.</i>"
        if vi else
        "<i>This is an unofficial translation for study purposes. Original content © 2019 "
        "Bibliotex; the individual chapters are released under Creative Commons.</i>"))
    return "".join(b)


def body_vi():
    return _body("vi")


def body_en():
    return _body("en")
