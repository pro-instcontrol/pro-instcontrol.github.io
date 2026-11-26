# -*- coding: utf-8 -*-
"""Chapter 7, "Display Devices and Recorders" (EN/VI).

Source: Prasad, Jayaswal & Priye, *Instrumentation and Process Control*
(I.K. International, 2019), PDF pp. 329-352, printed pp. 317-340.
PAGES_SRC = 24 counts this whole source span.

The chapter covers potentiometric, circular-chart, strip-chart, fanfold,
magnetic and digital recorders, X-Y plotters, programmable and paperless
recorders, LED and LCD display technologies, gas-discharge and liquid-vapour
displays, electrophoretic display and an eleven-question exercise. All 32
printed figures are redrawn as vectors by three `ipcfig7_*` suppliers;
the prose is assembled from five source-order section modules.
"""
import ipc_common as C          # noqa: F401  (page shell, used by C.build)
from ipc_common import h3, note, p
import ipc_ch07a as _a          # noqa: E402
import ipc_ch07b as _b          # noqa: E402
import ipc_ch07c as _c          # noqa: E402
import ipc_ch07d as _d          # noqa: E402
import ipc_ch07e as _e          # noqa: E402

PAGES_SRC = 24
BYLINE = ("Janardan Prasad · M. N. Jayaswal · Vishnu Priye · "
          "Instrumentation and Process Control (I.K. International, 2019)")
TITLE_EN = "Display Devices and Recorders"
TITLE_VI = "Thiết bị hiển thị và Máy ghi"

_SECTIONS = (_a, _b, _c, _d, _e)


def note_terms(lang):
    if lang == "vi":
        return ("<b>Thuật ngữ chính.</b> máy ghi · máy ghi thế kế cân bằng · biểu đồ tròn · "
                "biểu đồ dải · biểu đồ xếp nếp · ghi từ tính · ghi từ tính số · ghi tăng lượng · "
                "ghi đồng bộ · máy vẽ X-Y · máy ghi lập trình đa chức năng · máy ghi không giấy · "
                "màn hình hiển thị · đèn LED · màn hình tinh thể lỏng (LCD) · tán xạ động · "
                "hiệu ứng trường · smectic · nematic · cholesteric · hiển thị bảy đoạn · ma trận "
                "điểm · biểu đồ cột LED · đèn Nixie · phóng điện khí · hiển thị lỏng-hơi (LVD) · "
                "hiển thị điện di (EPI) · hạt màu trong dung dịch.")
    return ("<b>Key terms.</b> recorder · self-balancing potentiometric recorder · circular "
            "chart · strip chart · fanfold chart · magnetic recording · digital magnetic "
            "recording · incremental recording · synchronous recording · X-Y plotter · "
            "multifunction programmable recorder · paperless recorder · display device · LED · "
            "liquid crystal display (LCD) · dynamic scattering · field effect · smectic · "
            "nematic · cholesteric · seven-segment display · dot-matrix display · LED bar graph · "
            "Nixie tube · gas-discharge display · liquid-vapour display (LVD) · electrophoretic "
            "(EPI) display · electrophoresis.")


def source_notes(lang):
    if lang == "vi":
        return ("<b>Đặc điểm của nguyên bản.</b> PDF lưu phần lớn văn bản dưới dạng mã glyph /Gnn; "
                "work/ipc_decoded.txt giải mã từng mã nhưng vẫn giữ nhiều lỗi OCR, ký hiệu bị "
                "rời rạc và lỗi chính tả. Các nhãn trên hình chỉ tồn tại rời rạc trong lớp văn "
                "bản, nên 32 hình trong chương được vẽ lại dạng vector rút gọn sau khi đối chiếu "
                "trang in, giữ cấu trúc mạch, đường đi giấy và nhãn chính. Nguyên bản không có "
                "bảng, không có phương trình được đánh số và không có danh mục tài liệu tham "
                "khảo cuối chương; 11 câu hỏi ôn tập được giữ nguyên. Một số lỗi chính tả và "
                "cách viết cũ của nguyên bản vẫn được giữ trong bản Anh.")
    return ("<b>Source quirks.</b> The PDF stores most body text as glyph codes (/Gnn); "
            "work/ipc_decoded.txt decodes each code but retains OCR artifacts, scattered "
            "symbols and typos. Figure labels survive only as scattered fragments in the text "
            "layer, so all 32 figures were redrawn as simplified vectors after checking the "
            "printed pages, preserving circuit topology, paper paths and principal labels. The "
            "printed chapter has no tables, no numbered equations and no end-of-chapter "
            "reference list; its eleven exercise questions are retained. Some source typos and "
            "older spellings are kept in the English text.")


def _body(lang):
    vi = lang == "vi"
    b = [C.lead(
        "Chương này trình bày các hệ thống ghi và hiển thị dùng trong thiết bị đo công nghiệp: "
        "máy ghi thế kế tự cân bằng, biểu đồ tròn, dải và xếp nếp, ghi từ tính và ghi số, máy vẽ "
        "X-Y, máy ghi lập trình và máy ghi không giấy, cùng các công nghệ hiển thị LED, LCD, "
        "đèn Nixie, màn hình lỏng-hơi và màn hình điện di, kèm 11 câu hỏi ôn tập."
        if vi else
        "This chapter presents the recording and display systems used in industrial "
        "instrumentation: self-balancing potentiometric recorders, circular, strip and fanfold "
        "charts, magnetic and digital recording, X-Y plotters, programmable and paperless "
        "recorders, and the LED, LCD, Nixie, liquid-vapour and electrophoretic display "
        "technologies, followed by an eleven-question exercise.")]
    for module in _SECTIONS:
        b.extend(module.section(lang))

    b.append(h3("Về nguồn tài liệu" if vi else "About the source"))
    b.append(p(
        "Chương 7 chiếm PDF tr. 329–352, tương ứng tr. 317–340 của bản in; PAGES_SRC = 24 đếm "
        "toàn bộ phân đoạn nguồn này. Nguyên bản gồm các mục Máy ghi (7.1), Máy vẽ X-Y (7.2) và "
        "Thiết bị hiển thị số (7.3), cùng 32 hình đánh số Figure 7.1 – Figure 7.32 và "
        "11 câu hỏi ôn tập."
        if vi else
        "Chapter 7 occupies PDF pp. 329-352, corresponding to printed pp. 317-340; PAGES_SRC = 24 "
        "counts this whole source span. Its sections cover Recorders (7.1), X-Y Plotter (7.2) "
        "and Digital Data Display Devices (7.3), together with 32 numbered figures "
        "(Figure 7.1 - Figure 7.32) and an eleven-question exercise."))
    b.append(note(source_notes(lang)))
    b.append(p(
        "<i>Đây là bản dịch không chính thức, dùng cho mục đích học tập. Nội dung gốc © 2019 I.K. "
        "International; các chương của sách phát hành theo giấy phép Creative Commons.</i>"
        if vi else
        "<i>This is an unofficial translation for study purposes. Original content © 2019 I.K. "
        "International; the individual chapters are released under Creative Commons.</i>"))
    return "".join(b)


def body_vi():
    return _body("vi")


def body_en():
    return _body("en")
