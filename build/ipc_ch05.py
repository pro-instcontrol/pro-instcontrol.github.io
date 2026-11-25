# -*- coding: utf-8 -*-
"""Chapter 5, "Signal Conditioning and Data Acquisition System" (EN/VI).

Source: Prasad, Jayaswal & Priye, *Instrumentation and Process Control*
(I.K. International, 2019), PDF pp. 241-283, printed pp. 229-271.
PAGES_SRC = 43 counts this whole source span.

The chapter covers signal conditioning hardware, multiplexing, sample-and-hold,
ADC/DAC conversion, meter resolution and accuracy, aperture time, PC-based
acquisition, industrial communication protocols, eleven worked examples and an
18-question exercise. It has 43 numbered figures and many unnumbered printed
formulas; every figure is redrawn as a vector in the four `ipcfig5_*` supplier
modules and the prose is assembled from eight source-order section modules.
"""
import ipc_common as C          # noqa: F401  (page shell, used by C.build)
from ipc_common import h3, note, p
import ipc_ch05a as _a          # noqa: E402
import ipc_ch05b as _b          # noqa: E402
import ipc_ch05c as _c          # noqa: E402
import ipc_ch05d as _d          # noqa: E402
import ipc_ch05e as _e          # noqa: E402
import ipc_ch05f as _f          # noqa: E402
import ipc_ch05g as _g          # noqa: E402
import ipc_ch05h as _h          # noqa: E402

PAGES_SRC = 43
BYLINE = ("Janardan Prasad · M. N. Jayaswal · Vishnu Priye · "
          "Instrumentation and Process Control (I.K. International, 2019)")
TITLE_EN = "Signal Conditioning and Data Acquisition System"
TITLE_VI = "Điều hòa tín hiệu và Hệ thống thu thập dữ liệu"

_SECTIONS = (_a, _b, _c, _d, _e, _f, _g, _h)


def note_terms(lang):
    if lang == "vi":
        return ("<b>Thuật ngữ chính.</b> hệ thống thu thập dữ liệu (DAS) · bộ điều hòa tín hiệu "
                "· nguồn nuôi · bộ khuếch đại · bộ lọc · máy so sánh · bộ cộng / bộ trừ · "
                "mạch tích phân · vi sai · ghép kênh (multiplexer) · lấy mẫu · giữ mẫu (sample "
                "and hold) · thời gian cửa sổ (aperture time) · chuyển đổi A/D và D/A · "
                "bộ so sánh liên tiếp · bộ chuyển đổi ramp · V/T · V/F · độ phân giải · "
                "chữ số bán phần (half digit) · độ chính xác · lỗi · bus GPIB · RS-422 · "
                "RS-485 · Ethernet · CAN · ISO-OSI · PLC · SCADA · phần mềm ứng dụng.")
    return ("<b>Key terms.</b> data acquisition system (DAS) · signal conditioning · power pack "
            "· amplifier · filter · comparator · summing and subtracting amplifier · integrator · "
            "differentiator · multiplexer · sampling · sample and hold · aperture time · "
            "A/D and D/A conversion · successive approximation · ramp converter · voltage-to-time "
            "and voltage-to-frequency conversion · resolution · half digit · accuracy · error · "
            "GPIB bus · RS-422 · RS-485 · Ethernet · CAN · ISO-OSI · PLC · SCADA · application "
            "software.")


def source_notes(lang):
    if lang == "vi":
        return ("<b>Đặc điểm của nguyên bản.</b> PDF lưu phần lớn văn bản dưới dạng mã glyph /Gnn; "
                "work/ipc_decoded.txt giải mã từng mã nhưng vẫn giữ nhiều lỗi OCR, ký hiệu bị "
                "rời rạc và lỗi chính tả. Công thức trong nguyên bản hầu như không đánh số và "
                "bị xáo trộn trong lớp văn bản, nên được viết lại bằng ký hiệu toán học chuẩn "
                "sau khi đối chiếu trang in. Hình là ảnh trong PDF, chỉ nhãn và chú thích còn "
                "trong lớp văn bản, vì vậy mọi hình được vẽ lại dạng vector rút gọn giữ cấu "
                "trúc mạch và nhãn chính. Một số lỗi tính toán trong ví dụ được giữ nguyên bản "
                "Anh, còn bản Việt dùng cách diễn đạt rõ nghĩa hơn.")
    return ("<b>Source quirks.</b> The PDF stores most body text as glyph codes (/Gnn); "
            "work/ipc_decoded.txt decodes each code but retains OCR artifacts, scattered "
            "symbols and typos. The printed formulas are mostly unnumbered and scrambled in "
            "the text layer, so they were rewritten with standard mathematical notation after "
            "checking the printed pages. Figures are images in the PDF and only their labels "
            "and captions survive in the text layer; every figure is redrawn as a simplified "
            "vector retaining circuit topology and principal labels. A few arithmetic quirks "
            "in the worked examples are retained in the English text while Vietnamese uses "
            "the clearer reading.")


def _body(lang):
    vi = lang == "vi"
    b = [C.lead(
        "Chương này trình bày cách đưa tín hiệu đo về dạng chuẩn trước khi số hóa: nguồn nuôi, "
        "khuếch đại và lọc, ghép kênh, mạch giữ mẫu, bộ chuyển đổi A/D và D/A, độ phân giải và "
        "độ chính xác của đồng hồ số, thời gian cửa sổ, hệ thống thu thập trên PC, các chuẩn "
        "truyền thông công nghiệp, cùng 11 ví dụ và 18 câu hỏi ôn tập."
        if vi else
        "This chapter shows how measurement signals are conditioned before digitisation: power "
        "packs, amplification and filtering, multiplexing, sample-and-hold, ADC and DAC "
        "conversion, digital-meter resolution and accuracy, aperture time, PC-based acquisition, "
        "industrial communication standards, plus eleven worked examples and an 18-question "
        "exercise.")]
    for module in _SECTIONS:
        b.extend(module.section(lang))

    b.append(h3("Về nguồn tài liệu" if vi else "About the source"))
    b.append(p(
        "Chương 5 chiếm PDF tr. 241–283, tương ứng tr. 229–271 của bản in; PAGES_SRC = 43 đếm "
        "toàn bộ phân đoạn nguồn này. Nguyên bản gồm Mở đầu, Điều hòa tín hiệu, Ghép kênh, "
        "Độ chính xác của đồng hồ số, Thời gian cửa sổ, Hệ thống thu thập dữ liệu trên PC, "
        "11 ví dụ và 18 câu hỏi ôn tập, cùng 43 hình đánh số Figure 5.1 – Figure 5.43. Các "
        "công thức trong nguyên bản không được đánh số; bản dịch giữ nguyên cách trình bày "
        "đó và dùng ký hiệu toán học chuẩn."
        if vi else
        "Chapter 5 occupies PDF pp. 241-283, corresponding to printed pp. 229-271; PAGES_SRC = 43 "
        "counts this whole source span. Its sections cover Introduction, Signal Conditioning, "
        "Multiplexing, Accuracy of Digital Meter, Aperture Time, PC-based Practical Data "
        "Acquisition System, eleven worked examples and an 18-question exercise, together with "
        "43 numbered figures (Figure 5.1 - Figure 5.43). The printed formulas carry no numbers, "
        "and the translation preserves that convention while using standard mathematical "
        "notation."))
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
