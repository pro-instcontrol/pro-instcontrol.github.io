# -*- coding: utf-8 -*-
"""Book 9, Chapter 9 - Predictive Maintenance Based on Control Charts Applied
at Thermoelectric Power Plant / Bảo trì dự báo dựa trên biểu đồ kiểm soát
(EN/VI bilingual).

Source: Kisić, Đurović and Petrović, in L. N. Jalali (ed.), *Handbook on Power
Plant Instrumentation and Control* (Bibliotex, 2019), PDF pp. 215-244, printed
pp. 199-228 (printed = PDF - 16). PAGES_SRC = 30 counts this span. The chapter
has 11 figures, 2 tables, 40 references and unnumbered equations; all figures
are redrawn as vectors by three `ppicfig9_*` suppliers and the prose is
assembled from five source-order section modules.
"""
import ppic_common as C          # noqa: F401  (page shell, used by C.build)
import bolton_common as _B       # noqa: F401  (figure-caption language state)
from ppic_common import h3, note, p
import ppic_ch09a as _a          # noqa: E402
import ppic_ch09b as _b          # noqa: E402
import ppic_ch09c as _c          # noqa: E402
import ppic_ch09d as _d          # noqa: E402
import ppic_ch09e as _e          # noqa: E402

PAGES_SRC = 30
BYLINE = ("Emilija Kisić · Željko Đurović · Vera Petrović · "
          "Handbook on Power Plant Instrumentation and Control (Bibliotex, 2019)")
TITLE_EN = ("Predictive Maintenance Based on Control Charts Applied at "
            "Thermoelectric Power Plant")
TITLE_VI = "Bảo trì dự đoán dựa trên biểu đồ kiểm soát áp dụng tại nhà máy nhiệt điện"

_SECTIONS = (_a, _b, _c, _d, _e)


def note_terms(lang):
    if lang == "vi":
        return ("<b>Thuật ngữ chương 9.</b> bảo trì dự báo (predictive maintenance) · "
                "bảo trì theo thời gian (time-based maintenance) · bảo trì theo tình "
                "trạng (condition-based maintenance) · chẩn đoán · dự báo · tuổi thọ "
                "còn lại (RUL) · hệ thống nghiền than · bàn nghiền (grinding table) · "
                "tín hiệu âm thanh · phổ tần số (spectrogram) · biểu đồ kiểm soát "
                "Hotelling T² · giới hạn kiểm soát trên (UCL) · mô hình Markov ẩn "
                "(HMM) · trạng thái ẩn · ma trận chuyển trạng thái · ma trận quan sát "
                "· thuật toán Baum–Welch · phân phối xác suất · Q-Q plot · nhà máy "
                "nhiệt điện TEKO, Kostolac")
    return ("<b>Key terms.</b> predictive maintenance · time-based maintenance · "
            "condition-based maintenance · diagnostics · prognostics · remaining "
            "useful life (RUL) · coal-grinding subsystem · grinding table · acoustic "
            "signal · spectrogram · Hotelling T² control chart · upper control limit "
            "(UCL) · hidden Markov model (HMM) · hidden state · transition matrix · "
            "emission matrix · Baum–Welch algorithm · probability density function · "
            "Q-Q plot · TEKO thermoelectric power plant, Kostolac")


def source_notes(lang):
    if lang == "vi":
        return ("<b>Đặc điểm của nguyên bản.</b> Lớp văn bản PDF rời rạc các ký "
                "hiệu toán học; mọi phương trình trong bản này được đọc lại từ ảnh "
                "trang in. Mười một hình gốc là ảnh (sơ đồ hệ thống, phổ, biểu đồ "
                "T² và trạng thái HMM) được vẽ lại dạng vector, giữ trục, nhãn và "
                "đặc trưng chính. Hai bảng và 40 tài liệu tham khảo được giữ nguyên "
                "số hiệu. Một số lỗi chính tả và lỗi in của nguyên bản vẫn được giữ "
                "trong bản Anh.")
    return ("<b>Source quirks.</b> The PDF text layer scatters mathematical symbols; "
            "all equations here were re-read from the rendered printed pages. The "
            "eleven source figures are raster images (system layout, spectrogram, "
            "T² charts and HMM states) and were redrawn as vectors with their axes, "
            "labels and principal features. Both tables and all forty references "
            "retain their printed numbering. Some source typos and printing quirks "
            "are kept in the English text.")


def _body(lang):
    b = [C.lead(
        "Chương này trình bày kỹ thuật bảo trì dự báo dựa trên tín hiệu âm thanh, biểu "
        "đồ kiểm soát Hotelling T² và mô hình Markov ẩn, áp dụng cho bàn nghiền của "
        "máy nghiền than tại nhà máy nhiệt điện TEKO (Kostolac, Serbia)."
        if lang == "vi" else
        "This chapter presents a predictive-maintenance technique combining acoustic "
        "signals, Hotelling T² control charts and a hidden Markov model, applied to "
        "the grinding tables of a coal mill at the TEKO thermoelectric power plant "
        "(Kostolac, Serbia).")]
    for module in _SECTIONS:
        b.extend(module.section(lang))
    b.append(h3("Về nguồn tài liệu" if lang == "vi" else "About the source"))
    b.append(p(
        "Chương 9 chiếm PDF tr. 215–244, tương ứng tr. 199–228 của bản in; PAGES_SRC "
        "= 30 đếm toàn bộ phân đoạn này. Nguyên bản gồm 11 hình, 2 bảng và 40 tài "
        "liệu tham khảo."
        if lang == "vi" else
        "Chapter 9 occupies PDF pp. 215-244, corresponding to printed pp. 199-228; "
        "PAGES_SRC = 30 counts this whole span. The printed chapter has 11 figures, "
        "2 tables and 40 references."))
    b.append(note(source_notes(lang)))
    b.append(p(
        "<i>Đây là bản dịch không chính thức, dùng cho mục đích học tập. Nội dung gốc "
        "© 2019 Emilija Kisić, Željko Đurović và Vera Petrović, xuất bản bởi InTech "
        "theo giấy phép Creative Commons.</i>"
        if lang == "vi" else
        "<i>This is an unofficial translation for study purposes. Original content "
        "© 2019 Emilija Kisić, Željko Đurović and Vera Petrović, published by InTech "
        "under a Creative Commons licence.</i>"))
    return "".join(b)


def body_vi():
    return _body("vi")


def body_en():
    return _body("en")
