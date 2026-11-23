# -*- coding: utf-8 -*-
"""Book 7c, Chapter 15 - Conversions and Equivalents (EN/VI bilingual) — FINAL chapter.

Source: Emerson, *Control Valve Handbook*, 6th ed. (2020), printed pp. 324-355.
Like Chapters 13 and 14, this is a pure data reference: 31 printed pages, ZERO
figures, conversion-factor tables (length, area, volume, mass, pressure,
temperature, gravity, metric prefixes) plus the book's Index and Additional
Resources back matter.  Six section modules cvh15_s1..s6 supply the content;
table DATA is language-neutral and shared verbatim, while headings, prose,
headers and captions are localized through cvh15_common.
"""

import cvh6_common as C  # noqa: F401
from cvh6_common import lead, note, p
from cvh13_common import T
import cvh15_s1, cvh15_s2, cvh15_s3, cvh15_s4, cvh15_s5, cvh15_s6

PAGES_SRC = 31         # source printed pp. 324-355 inclusive (incl. Index + Resources)
BYLINE = "Emerson Flow Controls · Control Valve Handbook, 6th ed. (2020)"
TITLE_EN = "Conversions and Equivalents"
TITLE_VI = "Chuyển đổi và tương đương"

SECTIONS = (cvh15_s1, cvh15_s2, cvh15_s3, cvh15_s4, cvh15_s5, cvh15_s6)


def note_terms(lang):
    """A one-line glossary box of the chapter's key terms."""
    if lang == "vi":
        return (
            "<b>Thuật ngữ chính của chương.</b> conversion — chuyển đổi · equivalent — giá trị "
            "tương đương · multiplier — hệ số nhân · length — chiều dài · area — diện tích · "
            "volume — thể tích · volume rate — lưu lượng thể tích · mass — khối lượng · pressure "
            "— áp suất · temperature — nhiệt độ · Celsius — độ C · Fahrenheit — độ F · Kelvin — "
            "Kelvin · Rankine — Rankine · gravity — tỷ trọng · API gravity — độ API · Baumé "
            "gravity — độ Baumé · specific gravity — tỷ trọng riêng · metric prefix — tiền tố hệ "
            "mét · factor — hệ số · index — chỉ mục · conversion formula — công thức chuyển đổi")
    return (
        "<b>Key terms in this chapter.</b> conversion · equivalent · multiplier · length · area · "
        "volume · volume rate · mass · pressure · temperature · Celsius · Fahrenheit · Kelvin · "
        "Rankine · gravity · API gravity · Baumé gravity · specific gravity · metric prefix · "
        "factor · index · conversion formula")


def source_notes(lang):
    """Data-fidelity and source-quirk notes for this reference chapter."""
    if lang == "vi":
        return (
            "<b>Ghi chú về nguồn.</b> (1) Đây là chương dữ liệu cuối: 31 trang in (324–355), không "
            "có hình; nội dung gồm các bảng hệ số chuyển đổi và phần mục lục chỉ mục (Index) cùng "
            "Tài nguyên bổ sung của cuốn sách. Dữ liệu bảng (số, hệ số, công thức, đơn vị) được giữ "
            "nguyên và dùng chung cho cả hai bản ngôn ngữ; chỉ tiêu đề, văn bản, tiêu đề và chú "
            "thích bảng được dịch. (2) Các dòng «=== PAGE N ===», tiêu đề chạy và số trang được bỏ "
            "qua. (3) Nhiều lỗi OCR/đánh máy được giữ ở bản Anh và hiệu đính ở bản Việt: "
            "«convergemce» → convergence, «Killometers» → Kilometers, «To Covert From» → To Convert "
            "From, «Degrees Rankin»; dấu trừ Unicode (U+2212) và số có dấu phẩy ngàn được giữ "
            "nguyên. (4) Số mũ trong bảng tiền tố hệ mét được in dưới dạng chữ số mũ ("
            "1018 nghĩa là 10^18); ở đây viết lại thành 10^18 cho rõ ràng và ghi chú trong mục "
            "15.15. (5) Bảng nhiệt độ 15.12 gồm ba nhóm cột °C/°F cạnh nhau trên mỗi trang; các "
            "dòng thiếu giá trị được đệm ô trống để giữ đúng vị trí, không bỏ sót giá trị nào. "
            "Giá trị bất thường «787.0» (tr. 334) được giữ nguyên như in. (6) Bảng 15.13 in hai "
            "khối cột cạnh nhau nhưng bị đan xen trong bản dump; ở đây gộp thành một bảng năm cột "
            "theo đúng từng nhóm giá trị. (7) Chỉ mục giữ nguyên thuật ngữ tiếng Anh của bản in "
            "và số trang bản in — các số này là số trang của ấn bản giấy, không phải liên kết web; "
            "xem ghi chú đầu chỉ mục. (8) Không có hình minh họa nào trong nguồn để vẽ lại.")
    return (
        "<b>Source notes.</b> (1) This is the final data chapter: 31 printed pages (324-355), ZERO "
        "figures; content is conversion-factor tables plus the book's Index and Additional "
        "Resources back matter. Table DATA (numbers, factors, formulas, units) is kept verbatim "
        "and shared between the two languages; only headings, prose, table headers and captions "
        "are translated. (2) The `=== PAGE N ===` markers, running headers and bare page numbers "
        "are skipped. (3) Many OCR/typing quirks are kept in English and corrected in Vietnamese: "
        "«convergemce» to convergence, «Killometers» to Kilometers, «To Covert From» to To Convert "
        "From, «Degrees Rankin»; Unicode minus (U+2212) and comma-thousands are retained. (4) "
        "Metric-prefix powers are printed with superscript digits (1018 meaning 10^18); they are "
        "written as 10^18 here and noted in section 15.15. (5) The 15.12 temperature table has "
        "three side-by-side °C/°F column groups per page; short lines are padded with empty cells "
        "to keep positions, dropping no value. The odd value «787.0» (p. 334) is kept as printed. "
        "(6) The 15.13 gravity table prints two side-by-side column blocks that are interleaved in "
        "the dump; they are merged into one five-column table preserving each value group. (7) "
        "The Index retains the source's English terms and printed-edition page numbers — those "
        "numbers reference the paper edition, not web links; see the note at the head of the "
        "index. (8) No figures appear in the source to redraw.")


def _body(lang):
    b = []
    vi = lang == "vi"

    b.append(lead(
        "Chương cuối này tổng hợp các bảng chuyển đổi đơn vị dùng trong kỹ thuật: chiều dài, diện "
        "tích, thể tích, lưu lượng, khối lượng, áp suất, nhiệt độ, độ API/Baumé và tiền tố hệ mét, "
        "kèm công thức chuyển đổi. Sau các bảng là chỉ mục và danh sách tài nguyên bổ sung của "
        "cuốn sách. Số liệu được chuyển nguyên vẹn từ bản in."
        if vi else
        "This final chapter collects the engineering unit-conversion tables: length, area, volume, "
        "volume rate, mass, pressure, temperature, API/Baumé gravity and metric prefixes, with "
        "conversion formulas. The tables are followed by the book's index and additional "
        "resources. All figures are reproduced from the printed source."))
    b.append(note(note_terms("vi") if vi else note_terms("en")))

    # Fifteen conversion sections + Index + Additional Resources, in source order.
    for mod in SECTIONS:
        b.append(mod.section(lang))

    b.append("<h3>%s</h3>" % ("Ghi chú về nguồn" if vi else "Source notes"))
    b.append(note(source_notes("vi") if vi else source_notes("en")))

    b.append(p(
        "Chương 15 chiếm các trang in 324–355 của Emerson, Control Valve Handbook, ấn bản 6 "
        "(2020), gồm mười lăm mục 15.1–15.15 cùng chỉ mục và tài nguyên bổ sung. Đây là chương "
        "cuối của cuốn sách; không có hình minh họa nào trong nguồn để vẽ lại."
        if vi else
        "Chapter 15 occupies printed pp. 324-355 (31 pages) of Emerson, Control Valve Handbook, "
        "6th edition (2020), covering fifteen sections, 15.1-15.15, plus the index and additional "
        "resources. This is the final chapter of the book; the source contains no figures to "
        "redraw."))
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
