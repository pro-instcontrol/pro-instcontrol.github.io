# -*- coding: utf-8 -*-
"""Chapter 4, "Telemetry" (EN/VI bilingual).

Source: Prasad, Jayaswal & Priye, *Instrumentation and Process Control*
(I.K. International, 2019), PDF pp. 216-240, printed pp. 204-228.
PAGES_SRC = 25 counts this whole source span.

The chapter covers hydraulic, pneumatic, cable, fibre-optic, analog, pulse,
digital and RF telemetry, plus telemetry in electrical power systems. It has
30 numbered figures, four numbered equations, four worked examples and a
15-question exercise. Every figure is redrawn as a vector in the two
`ipcfig4_*` supplier modules; the prose is assembled from seven source-order
section modules.
"""
import ipc_common as C          # noqa: F401  (page shell, used by C.build)
from ipc_common import h3, note, p
import ipc_ch04_a as _a        # noqa: E402
import ipc_ch04_b as _b        # noqa: E402
import ipc_ch04_c as _c        # noqa: E402
import ipc_ch04_d as _d        # noqa: E402
import ipc_ch04_e as _e        # noqa: E402
import ipc_ch04_f as _f        # noqa: E402
import ipc_ch04_g as _g        # noqa: E402

PAGES_SRC = 25
BYLINE = ("Janardan Prasad · M. N. Jayaswal · Vishnu Priye · "
          "Instrumentation and Process Control (I.K. International, 2019)")
TITLE_EN = "Telemetry"
TITLE_VI = "Đo từ xa"

_SECTIONS = (_a, _b, _c, _d, _e, _f, _g)


def note_terms(lang):
    if lang == "vi":
        return ("<b>Thuật ngữ chính.</b> đo từ xa · tín hiệu khí nén · tín hiệu thủy lực · "
                "truyền dẫn bằng cáp · cáp xoắn đôi không che chắn (UTP) · cáp xoắn đôi che "
                "chắn (STP) · cáp đồng trục · rào cách ly an toàn nội tại · nhiễu chế độ "
                "thường · nhiễu chế độ chung · sợi quang · lớp lõi · lớp vỏ bọc · chiết suất "
                "· đầu nối quang · điều chế biên độ · điều chế tần số · điều chế pha · điều chế "
                "xung · PAM · PDM/PWM · PPM · PCM · băng thông · tốc độ lấy mẫu · RF · "
                "đường dây nóng · lưới điện · máy biến áp dòng / điện áp.")
    return ("<b>Key terms.</b> telemetry · pneumatic signalling · hydraulic signalling · cable "
            "telemetry · unshielded twisted pair (UTP) · shielded twisted pair (STP) · coaxial "
            "cable · intrinsically safe barrier · normal-mode noise · common-mode noise · "
            "optical fibre · core · cladding · refractive index · optical coupling · amplitude "
            "modulation · frequency modulation · phase modulation · pulse modulation · PAM · "
            "PDM/PWM · PPM · PCM · bandwidth · sampling rate · RF · hot line · grid network · "
            "current and potential transformers.")


def source_notes(lang):
    if lang == "vi":
        return ("<b>Đặc điểm của nguyên bản.</b> PDF lưu phần lớn văn bản dưới dạng mã glyph "
                "/Gnn; tệp work/ipc_decoded.txt đã giải mã từng mã nhưng vẫn giữ nhiều lỗi OCR, "
                "ký hiệu bị rời rạc và lỗi chính tả (ví dụ UPT thay cho UTP). Các phương trình "
                "và kết quả ví dụ được viết lại bằng ký hiệu toán học chuẩn; khi phép tính in "
                "trong nguồn có vẻ không nhất quán, bản Anh vẫn ghi như in và bản Việt dùng "
                "cách diễn đạt rõ nghĩa hơn. Hình trong PDF là ảnh, chỉ nhãn và chú thích còn "
                "trong lớp văn bản, nên mọi hình được vẽ lại dạng vector rút gọn giữ nguyên "
                "cấu trúc mạch và nhãn chính.")
    return ("<b>Source quirks.</b> The PDF stores most body text as glyph codes (/Gnn); "
            "work/ipc_decoded.txt decodes each code but retains OCR artifacts, scattered "
            "symbols and typos (for example UPT for UTP). Printed equations and example "
            "arithmetic are rendered with standard mathematical notation; where the printed "
            "calculation appears inconsistent, the English keeps the printed result and the "
            "Vietnamese uses the clearer reading. Figures are images in the PDF and only their "
            "labels and captions survive in the text layer, so every figure is redrawn as a "
            "simplified vector retaining the original circuit topology and principal labels.")


def _body(lang):
    vi = lang == "vi"
    b = [C.lead(
        "Chương này định nghĩa đo từ xa và trình bày các phương pháp truyền tín hiệu đo từ "
        "địa điểm đo đến nơi quan sát: tín hiệu thủy lực và khí nén, cáp đồng, cáp sợi quang, "
        "điều chế tương tự và xung, PCM, RF và ứng dụng trong lưới điện."
        if vi else
        "This chapter defines telemetry and surveys the ways measurement signals travel from a "
        "remote location to an observer: hydraulic and pneumatic signalling, copper cable, "
        "optical fibre, analog and pulse modulation, PCM, RF, and applications in power grids.")]
    for module in _SECTIONS:
        b.extend(module.section(lang))

    b.append(h3("Về nguồn tài liệu" if vi else "About the source"))
    b.append(p(
        "Chương 4 chiếm PDF tr. 216–240, tương ứng tr. 204–228 của bản in; PAGES_SRC = 25 đếm "
        "toàn bộ phân đoạn nguồn này. Nguyên bản gồm bảy mục từ Introduction đến Telemetry in "
        "Electrical Power System, tiếp theo là bốn ví dụ và 15 câu hỏi ôn tập. Có 30 hình đánh "
        "số Figure 4.1 – Figure 4.30, bốn phương trình (4.1) – (4.4); tất cả được dựng lại "
        "dạng vector hoặc chép lại từ trang in."
        if vi else
        "Chapter 4 occupies PDF pp. 216-240, corresponding to printed pp. 204-228; PAGES_SRC = "
        "25 counts this whole source span. Its seven sections run from Introduction to Telemetry "
        "in Electrical Power System, followed by four worked examples and a 15-question exercise. "
        "The source contains 30 numbered figures (Figure 4.1 - Figure 4.30) and four numbered "
        "equations (4.1) - (4.4); all are redrawn as vectors or transcribed from the printed "
        "pages here."))
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
