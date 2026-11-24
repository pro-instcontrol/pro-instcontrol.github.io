# -*- coding: utf-8 -*-
"""Chapter 2, "Transducers - II" (EN/VI bilingual).

Source: Janardan Prasad, M. N. Jayaswal and Vishnu Priye, *Instrumentation and
Process Control* (I.K. International, 2019), PDF pp. 75-135, printed pp. 63-123.
PAGES_SRC = 61 counts the whole assigned source span.

The source chapter has three numbered sections, 58 numbered figures, one
numbered table, twenty numbered equations, twelve worked examples and an
eleven-question exercise.  Every figure is redrawn as a vector in the three
`ipcfig2_*` supplier modules; the prose is assembled from six section modules
that follow the source order.
"""
import ipc_common as C          # noqa: F401  (page shell, used by C.build)
from ipc_common import lead, note, p
import ipc_ch02_a as _a  # noqa: E402
import ipc_ch02_b as _b  # noqa: E402
import ipc_ch02_c as _c  # noqa: E402
import ipc_ch02_d as _d  # noqa: E402
import ipc_ch02_e as _e  # noqa: E402
import ipc_ch02_f as _f  # noqa: E402

PAGES_SRC = 61
BYLINE = ("Janardan Prasad · M. N. Jayaswal · Vishnu Priye · "
          "Instrumentation and Process Control (I.K. International, 2019)")
TITLE_EN = "Transducers – II"
TITLE_VI = "Bộ chuyển đổi – II"

_SECTIONS = (_a, _b, _c, _d, _e, _f)


def note_terms(lang):
    if lang == "vi":
        return ("<b>Thuật ngữ chính.</b> hệ thống thiết bị đo — instrumentation system · bộ phát — "
                "transmitter · bộ thu — receiver · bộ điều khiển — controller · phần tử điều khiển "
                "cuối — final control element · áp suất — pressure · áp kế — pressure gage · "
                "manomet — manometer · ống Bourdon — Bourdon tube · màng — diaphragm · bộ khuếch đại "
                "khí nén — pneumatic relay · chuyển vị — displacement · vận tốc — velocity · gia tốc "
                "— acceleration · mô-men xoắn — torque · LVDT — LVDT · cảm biến địa chấn — seismic "
                "pick-up · hiệu điện thế — voltage · tần số — frequency.")
    return ("<b>Key terms.</b> instrumentation system · transmitter · receiver · controller · "
            "final control element · pressure · pressure gage · manometer · Bourdon tube · "
            "diaphragm · pneumatic relay · displacement · velocity · acceleration · torque · "
            "LVDT · seismic pick-up · voltage · frequency.")


def source_notes(lang):
    if lang == "vi":
        return ("<b>Đặc điểm của nguyên bản.</b> PDF lưu phần lớn văn bản dưới dạng mã glyph "
                "(/Gnn); bản giải mã work/ipc_decoded.txt đổi mỗi mã thành ký tự tương ứng nhưng vẫn "
                "giữ nhiều lỗi OCR, ký hiệu bị rời rạc và lỗi chính tả. Các phương trình in bị vỡ "
                "thành từng ký tự nên được viết lại bằng ký hiệu toán học chuẩn tại chỗ; thứ tự hệ "
                "số được chọn theo nghĩa vật lý hợp lý nhất. Hình trong PDF là ảnh, chỉ nhãn và chú "
                "thích còn lại trong lớp văn bản, vì vậy mọi hình được vẽ lại dạng vector rút gọn "
                "theo đúng cấu trúc và nhãn của bản in. Một số lỗi của nguyên bản được giữ nguyên "
                "trong bản Anh (ví dụ 'instruments are eyes of any processing plant', "
                "'manometer liquid of density', 'usual value of do'), còn bản Việt dùng nghĩa đúng.")
    return ("<b>Source quirks.</b> The PDF stores most body text as glyph codes (/Gnn); the decoded "
            "file work/ipc_decoded.txt converts each code to its character but retains many OCR "
            "artifacts, scattered symbols and typos. Printed equations survive as disjoint glyphs "
            "and are rendered with standard mathematical notation in place; coefficient order "
            "follows the most plausible physical meaning. The figures are images in the PDF and "
            "only their printed labels and captions remain in the text layer, so every figure is "
            "redrawn in simplified vector form consistent with the original topology. A few source "
            "quirks are kept in the English text (e.g. 'instruments are eyes of any processing "
            "plant', 'manometer liquid of density', 'usual value of do'), while the Vietnamese "
            "uses the intended meaning.")


def _body(lang):
    vi = lang == "vi"
    b = []
    b.append(lead(
        "Chương này mô tả các phần tử của hệ thống thiết bị đo, rồi trình bày bộ chuyển đổi và "
        "phép đo áp suất từ manomet, áp kế cơ khí đến bộ phát khí nén, điện tử và thông minh; cuối "
        "cùng là các phép đo chuyển vị, vận tốc, gia tốc và mô-men xoắn kèm mười hai ví dụ tính toán."
        if vi else
        "This chapter describes the elements of an instrumentation system, then covers transducers "
        "and pressure measurement from manometers and mechanical gages to pneumatic, electronic "
        "and smart transmitters; it closes with displacement, velocity, acceleration and torque "
        "measurement and twelve worked examples."))

    for module in _SECTIONS:
        b.append(module.section(lang))

    # ---------------------------------------------------------------- about
    H = C.h3
    b.append(H("Về nguồn tài liệu" if vi else "About the source"))
    b.append(p(
        "Chương 2 chiếm PDF tr. 75-135, tương ứng tr. 63-123 của bản in; PAGES_SRC = 61 đếm toàn "
        "bộ phân đoạn nguồn này. Các mục theo mục lục là Elements of Instrumentation System, "
        "Transducers and Measurement of Pressure, và Measurement of Displacement, Velocity, "
        "Acceleration and Torque. Nguyên bản có 58 hình đánh số Fig. 2.1 - Fig. 2.58, một bảng "
        "Table 2.1, 20 phương trình đánh số (2.1) - (2.20), 12 ví dụ và 11 câu hỏi; tất cả được "
        "dựng lại dạng vector hoặc chép lại từ trang in ở đây."
        if vi else
        "Chapter 2 occupies PDF pp. 75-135, corresponding to printed pp. 63-123; PAGES_SRC = 61 "
        "counts this whole source span. Its sections are Elements of Instrumentation System, "
        "Transducers and Measurement of Pressure, and Measurement of Displacement, Velocity, "
        "Acceleration and Torque. The source contains 58 numbered figures (Fig. 2.1 - Fig. 2.58), "
        "one numbered table (Table 2.1), 20 numbered equations (2.1) - (2.20), 12 worked examples "
        "and 11 exercise questions; all are redrawn as vectors or transcribed from the printed "
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
