# -*- coding: utf-8 -*-
"""Chapter 6, "Process Control" (EN/VI).

Source: Prasad, Jayaswal & Priye, *Instrumentation and Process Control*
(I.K. International, 2019), PDF pp. 284-328, printed pp. 272-316.
PAGES_SRC = 45 counts this whole source span.

The chapter covers open-loop and closed-loop control, ON-OFF, proportional,
integral, derivative, PI and PID actions, integral windup, electronic and
pneumatic controllers, control-action selection, three-element feed-forward
control, thirteen worked examples and a fourteen-question exercise. All 26
printed figures are redrawn as vectors by the three `ipcfig6_*` suppliers;
the prose is assembled from nine source-order section modules.
"""
import ipc_common as C          # noqa: F401  (page shell, used by C.build)
from ipc_common import h3, note, p
import ipc_ch06a as _a          # noqa: E402
import ipc_ch06b as _b          # noqa: E402
import ipc_ch06c as _c          # noqa: E402
import ipc_ch06d as _d          # noqa: E402
import ipc_ch06e as _e          # noqa: E402
import ipc_ch06f as _f          # noqa: E402
import ipc_ch06g as _g          # noqa: E402
import ipc_ch06h as _h          # noqa: E402
import ipc_ch06i as _i          # noqa: E402

PAGES_SRC = 45
BYLINE = ("Janardan Prasad · M. N. Jayaswal · Vishnu Priye · "
          "Instrumentation and Process Control (I.K. International, 2019)")
TITLE_EN = "Process Control"
TITLE_VI = "Điều khiển quá trình"

_SECTIONS = (_a, _b, _c, _d, _e, _f, _g, _h, _i)


def note_terms(lang):
    if lang == "vi":
        return ("<b>Thuật ngữ chính.</b> hệ thống hở · hệ thống kín · phản hồi · phản hồi âm · "
                "điều khiển ON-OFF · dải tỷ lệ (PB) · độ lợi · độ lệch · suy giảm biên độ một phần "
                "tư · hành động tỷ lệ · hành động tích phân · hành động vi phân · tốc độ tích phân "
                "· PI · PID · tích phân bão hòa (integral windup) · mạch giới hạn · bộ điều khiển "
                "điện tử · bộ điều khiển khí nén · bộ phát hiện sai số · vòi phun và cánh flap · "
                "buồng khí · trạm nạp tay · lựa chọn phương pháp điều khiển · điều khiển xếp tầng "
                "· điều khiển ba phần tử · điều khiển đón đầu (feed forward) · mức trống nồi hơi.")
    return ("<b>Key terms.</b> open-loop system · closed-loop system · feedback · negative "
            "feedback · ON-OFF control · proportional band (PB) · gain · offset · quarter "
            "amplitude decay · proportional action · integral action · derivative action · "
            "integral rate · PI control · PID control · integral windup · limiter circuit · "
            "electronic controller · pneumatic controller · error detector · flapper-nozzle · "
            "bellows · manual loading station · selection of control technique · cascade control · "
            "three-element control · feed forward · boiler drum level.")


def source_notes(lang):
    if lang == "vi":
        return ("<b>Đặc điểm của nguyên bản.</b> PDF lưu phần lớn văn bản dưới dạng mã glyph /Gnn; "
                "work/ipc_decoded.txt giải mã từng mã nhưng vẫn giữ nhiều lỗi OCR, ký hiệu bị "
                "rời rạc và lỗi chính tả. Bốn phương trình được đánh số (6.1)–(6.4) và các "
                "công thức trong ví dụ được viết lại bằng ký hiệu toán học chuẩn sau khi đối "
                "chiếu trang in; các lỗi tính toán của nguyên bản vẫn được giữ trong bản Anh. "
                "Hình là ảnh trong PDF, chỉ nhãn và chú thích còn trong lớp văn bản, nên mọi "
                "hình được vẽ lại dạng vector rút gọn giữ cấu trúc mạch, đường cong và nhãn "
                "chính. Nguyên bản không có bảng và không có danh mục tài liệu tham khảo ở "
                "cuối chương.")
    return ("<b>Source quirks.</b> The PDF stores most body text as glyph codes (/Gnn); "
            "work/ipc_decoded.txt decodes each code but retains OCR artifacts, scattered "
            "symbols and typos. The four numbered equations (6.1)-(6.4) and the formulas in "
            "the worked examples were rewritten with standard mathematical notation after "
            "checking the printed pages; arithmetic quirks in the examples are retained in "
            "the English text. Figures are images in the PDF and only their labels and "
            "captions survive in the text layer, so every figure is redrawn as a simplified "
            "vector retaining circuit topology, curves and principal labels. The printed "
            "chapter has no tables and no end-of-chapter reference list.")


def _body(lang):
    vi = lang == "vi"
    b = [C.lead(
        "Chương này trình bày các chế độ điều khiển quá trình: hệ thống hở và kín, điều khiển "
        "ON-OFF, tỷ lệ, tích phân, vi phân, PI và PID, hiện tượng tích phân bão hòa, cấu trúc "
        "bộ điều khiển điện tử và khí nén, cách chọn chế độ điều khiển, điều khiển ba phần tử "
        "với đón đầu, cùng 13 ví dụ và 14 câu hỏi ôn tập."
        if vi else
        "This chapter presents the modes of process control: open and closed loops, ON-OFF, "
        "proportional, integral, derivative, PI and PID actions, integral windup, electronic "
        "and pneumatic controller designs, the selection of a control technique, three-element "
        "feed-forward control, plus thirteen worked examples and a fourteen-question exercise.")]
    for module in _SECTIONS:
        b.extend(module.section(lang))

    b.append(h3("Về nguồn tài liệu" if vi else "About the source"))
    b.append(p(
        "Chương 6 chiếm PDF tr. 284–328, tương ứng tr. 272–316 của bản in; PAGES_SRC = 45 đếm "
        "toàn bộ phân đoạn nguồn này. Nguyên bản gồm Mở đầu, các chế độ điều khiển ON-OFF, tỷ lệ, "
        "tích phân, vi phân, PI và PID, tích phân bão hòa, bộ điều khiển điện tử và khí nén, lựa "
        "chọn kỹ thuật điều khiển, điều khiển ba phần tử, 13 ví dụ và 14 câu hỏi ôn tập, cùng "
        "26 hình đánh số Figure 6.1 – Figure 6.26 và bốn phương trình (6.1)–(6.4)."
        if vi else
        "Chapter 6 occupies PDF pp. 284-328, corresponding to printed pp. 272-316; PAGES_SRC = 45 "
        "counts this whole source span. Its sections cover the Introduction, ON-OFF, "
        "proportional, integral, derivative, PI and PID actions, integral windup, electronic and "
        "pneumatic controllers, the selection of a control technique, three-element control, "
        "thirteen examples and a fourteen-question exercise, together with 26 numbered figures "
        "(Figure 6.1 - Figure 6.26) and four numbered equations (6.1)-(6.4)."))
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
