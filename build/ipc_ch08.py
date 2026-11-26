# -*- coding: utf-8 -*-
"""Chapter 8, "Microprocessor Based Instrumentation System" (EN/VI).

Source: Prasad, Jayaswal & Priye, *Instrumentation and Process Control*
(I.K. International, 2019), PDF pp. 353-396, printed pp. 341-384.
PAGES_SRC = 44 counts this whole source span.

The chapter covers the stored-program/microprocessor concept, interfacing
techniques (PIA, isolation, masking, ADC/DAC), the system bus, interrupts and
communication protocols (Modbus, ABDH, ARCNET, IEEE 1118, PROFIBUS, FIP), the
PLC (components, operation cycle, ladder programming) and the DCS (architecture,
data highway, controllers and operator stations), plus a thirty-question
exercise. All 34 printed figures are redrawn as vectors by four `ipcfig8_*`
suppliers; the prose is assembled from six source-order section modules.
"""
import ipc_common as C          # noqa: F401  (page shell, used by C.build)
from ipc_common import h3, note, p
import ipc_ch08a as _a          # noqa: E402
import ipc_ch08b as _b          # noqa: E402
import ipc_ch08c as _c          # noqa: E402
import ipc_ch08d as _d          # noqa: E402
import ipc_ch08e as _e          # noqa: E402
import ipc_ch08f as _f          # noqa: E402

PAGES_SRC = 44
BYLINE = ("Janardan Prasad · M. N. Jayaswal · Vishnu Priye · "
          "Instrumentation and Process Control (I.K. International, 2019)")
TITLE_EN = "Microprocessor Based Instrumentation System"
TITLE_VI = "Hệ thống thiết bị đo dựa trên vi xử lý"

_SECTIONS = (_a, _b, _c, _d, _e, _f)


def note_terms(lang):
    if lang == "vi":
        return ("<b>Thuật ngữ chính.</b> hệ thống thiết bị đo dựa trên vi xử lý · kiến trúc Von "
                "Neumann · chương trình lưu trữ · giao tiếp · bộ chuyển đổi tương tự-số (ADC) · "
                "bộ chuyển đổi số-tương tự (DAC) · bộ thích ứng giao tiếp song song (PIA) · "
                "cách ly quang · che lọc · xe buýt hệ thống · ngắt · giao thức truyền thông · "
                "Modbus · PROFIBUS · ARCNET · FIP · điểm-điểm · cấu trúc mạng bus/vòng/sao · "
                "bộ điều khiển logic lập trình (PLC) · logic bậc thang · chu kỳ quét · "
                "hệ thống điều khiển phân tán (DCS) · đường truyền dữ liệu nhà máy · trạm người "
                "vận hành · bộ điều khiển đa chức năng.")
    return ("<b>Key terms.</b> microprocessor-based instrumentation system · Von Neumann "
            "architecture · stored program · interfacing · analog-to-digital converter (ADC) · "
            "digital-to-analog converter (DAC) · parallel interface adaptor (PIA) · optical "
            "isolation · masking · system bus · interrupt · communication protocol · Modbus · "
            "PROFIBUS · ARCNET · FIP · point-to-point link · bus/ring/star topology · "
            "programmable logic controller (PLC) · ladder logic · scan cycle · distributed "
            "control system (DCS) · plant data highway · operator station · multifunction "
            "controller.")


def source_notes(lang):
    if lang == "vi":
        return ("<b>Đặc điểm của nguyên bản.</b> PDF lưu phần lớn văn bản dưới dạng mã glyph /Gnn; "
                "work/ipc_decoded.txt giải mã từng mã nhưng vẫn giữ nhiều lỗi OCR, ký hiệu bị "
                "rời rạc và lỗi chính tả. Các nhãn trên hình chỉ tồn tại rời rác trong lớp văn "
                "bản, nên 34 hình trong chương được vẽ lại dạng vector rút gọn sau khi đối chiếu "
                "trang in, giữ cấu trúc mạch, topology mạng và các nhãn chính. Nguyên bản không "
                "có bảng, không có phương trình được đánh số và không có danh mục tài liệu tham "
                "khảo cuối chương; 30 câu hỏi ôn tập được giữ nguyên. Một số lỗi chính tả và cách "
                "viết cũ của nguyên bản vẫn được giữ trong bản Anh.")
    return ("<b>Source quirks.</b> The PDF stores most body text as glyph codes (/Gnn); "
            "work/ipc_decoded.txt decodes each code but retains OCR artifacts, scattered "
            "symbols and typos. Figure labels survive only as scattered fragments in the text "
            "layer, so all 34 figures were redrawn as simplified vectors after checking the "
            "printed pages, preserving circuit topology, network layout and principal labels. "
            "The printed chapter has no tables, no numbered equations and no end-of-chapter "
            "reference list; its thirty exercise questions are retained. Some source typos and "
            "older spellings are kept in the English text.")


def _body(lang):
    vi = lang == "vi"
    b = [C.lead(
        "Chương cuối này trình bày các hệ thống thiết bị đo dựa trên vi xử lý: khái niệm chương "
        "trình lưu trữ và vi xử lý, kỹ thuật giao tiếp, xe buýt hệ thống và ngắt, các giao thức "
        "truyền thông công nghiệp, bộ điều khiển logic lập trình (PLC), hệ thống điều khiển phân "
        "tán (DCS), cùng 30 câu hỏi ôn tập."
        if vi else
        "This final chapter presents microprocessor-based instrumentation systems: the stored-"
        "program and microprocessor concept, interfacing techniques, the system bus and "
        "interrupts, industrial communication protocols, programmable logic controllers (PLCs), "
        "distributed control systems (DCSs), and a thirty-question exercise.")]
    for module in _SECTIONS:
        b.extend(module.section(lang))

    b.append(h3("Về nguồn tài liệu" if vi else "About the source"))
    b.append(p(
        "Chương 8 chiếm PDF tr. 353–396, tương ứng tr. 341–384 của bản in; PAGES_SRC = 44 đếm "
        "toàn bộ phân đoạn nguồn này. Nguyên bản gồm các mục 8.1 Giới thiệu, 8.2 Kỹ thuật giao "
        "tiếp, 8.3 Bộ điều khiển lập trình dựa trên vi xử lý, 8.4 Xe buýt hệ thống, dịch vụ ngắt "
        "và giao thức truyền thông, 8.5 PLC và 8.6 DCS, cùng 34 hình đánh số Figure 8.1 – "
        "Figure 8.34 và 30 câu hỏi ôn tập."
        if vi else
        "Chapter 8 occupies PDF pp. 353-396, corresponding to printed pp. 341-384; PAGES_SRC = 44 "
        "counts this whole source span. Its sections cover Introduction (8.1), Interface System "
        "Techniques (8.2), Microprocessor Based Programmable Controller (8.3), Bus System, "
        "Interrupt Services and Communication Protocols (8.4), PLC (8.5) and DCS (8.6), together "
        "with 34 numbered figures (Figure 8.1 - Figure 8.34) and a thirty-question exercise."))
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
