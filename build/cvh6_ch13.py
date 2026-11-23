# -*- coding: utf-8 -*-
"""Book 7c, Chapter 13 - Engineering Data (EN/VI bilingual).

Source: Emerson, *Control Valve Handbook*, 6th ed. (2020), printed pp. 260-301.
This chapter is a pure data reference: 42 pages, ZERO figures, almost entirely
numeric property tables (material specifications, hydrocarbon and fluid
constants, specific heat ratios, ammonia, water, and saturated/superheated
steam).  The nine sections are supplied by six modules cvh13_s1..s6; table
DATA is language-neutral and shared verbatim, while headings, prose, headers
and captions are localized through the cvh13_common helpers.
"""

import cvh6_common as C  # noqa: F401
from cvh6_common import lead, note, p
from cvh13_common import T
import cvh13_s1, cvh13_s2, cvh13_s3, cvh13_s4, cvh13_s5, cvh13_s6

PAGES_SRC = 42         # source printed pp. 260-301 inclusive
BYLINE = "Emerson Flow Controls · Control Valve Handbook, 6th ed. (2020)"
TITLE_EN = "Engineering Data"
TITLE_VI = "Dữ liệu kỹ thuật"

SECTIONS = (cvh13_s1, cvh13_s2, cvh13_s3, cvh13_s4, cvh13_s5, cvh13_s6)


def note_terms(lang):
    """A one-line glossary box of the chapter's key data/terms."""
    if lang == "vi":
        return (
            "<b>Thuật ngữ chính của chương.</b> material specification — quy cách vật liệu · "
            "pressure-retaining — chịu áp · composition — thành phần · temperature range — dải "
            "nhiệt độ · molecular weight — khối lượng phân tử · boiling point — điểm sôi · "
            "freezing point — điểm đông · vapor pressure — áp suất hơi · critical constants — "
            "hằng số tới hạn · specific gravity — tỷ trọng riêng · specific heat ratio (k) — tỷ "
            "số nhiệt dung riêng · density — mật độ · enthalpy — entanpi · saturated vapor — hơi "
            "bão hòa · saturated liquid — chất lỏng bão hòa · specific volume — thể tích riêng · "
            "latent heat — nhiệt ẩn · absolute pressure — áp suất tuyệt đối · gauge pressure — "
            "áp suất đo · vacuum — chân không · BTU/lb. — BTU trên pound · °F — độ Fahrenheit · "
            "psia — pound trên inch vuông tuyệt đối · superheated steam — hơi quá nhiệt · "
            "saturated steam — hơi bão hòa")
    return (
        "<b>Key terms in this chapter.</b> material specification · pressure-retaining · "
        "composition · temperature range · molecular weight · boiling point · freezing point · "
        "vapor pressure · critical constants · specific gravity · specific heat ratio (k) · "
        "density · enthalpy · saturated vapor · saturated liquid · specific volume · latent heat "
        "· absolute pressure · gauge pressure · vacuum · BTU/lb. · °F · psia · superheated steam "
        "· saturated steam")


def source_notes(lang):
    """Data-fidelity and source-quirk notes for this reference chapter."""
    if lang == "vi":
        return (
            "<b>Ghi chú về nguồn.</b> (1) Đây là chương dữ liệu: 42 trang in (260–301), không có "
            "hình; gần như toàn bộ nội dung là bảng thông số kỹ thuật. Dữ liệu bảng (số, công thức "
            "hóa học, ký hiệu, đơn vị) được giữ nguyên và dùng chung cho cả hai bản ngôn ngữ; chỉ "
            "tiêu đề, văn bản và chú thích bảng được dịch. (2) Các dòng «=== PAGE N ===», tiêu đề "
            "chạy và số trang được bỏ qua; các dòng «...continued...» được gộp vào cùng một bảng "
            "có một hàng tiêu đề duy nhất. (3) Ký tự bullet «» của PDF được OCR sai được thay "
            "bằng danh sách gạch đầu dòng bình thường. (4) Nhiều lỗi OCR và lỗi chính tả được giữ "
            "nguyên ở bản Anh: «Isolpentane», «Phsyical Constants», «Mangesium Chloride», công thức "
            "như «NH4CI», «CCI4», «CI2», «C12H22011», các số có dấu chấm hoặc dấu trừ lẻ như "
            "«332.», «-119.(6)», «14.0 (9.7E4)», «07967», «1233.», «1266.90». (5) Các ký hiệu "
            "chỉ số chân (footnote) như (1), (2), (5), (7), (8) và các ô trống «- - -» được giữ "
            "nguyên vì chúng mang ý nghĩa trong bảng gốc. (6) Dấu trừ Unicode (U+2212, U+2013) "
            "trong một số giá trị và dấu `ʋ` (thể tích riêng) được giữ nguyên từ bản in. (7) Với "
            "bảng hơi quá nhiệt, các nhóm nhiệt độ được tách thành hai bảng theo số cột; các dấu "
            "«- - -» biểu thị giá trị không áp dụng ở áp suất đó. (8) Không có phương trình hay "
            "hình minh họa nào được thêm vào; mọi nội dung đều được chuyển từ bảng của nguồn.")
    return (
        "<b>Source notes.</b> (1) This is a data chapter: 42 printed pages (260-301), ZERO "
        "figures; almost all content is engineering property tables. Table DATA (numbers, "
        "chemical formulas, symbols, units) is kept verbatim and shared between the two "
        "languages; only headings, prose, headers and captions are translated. (2) The "
        "`=== PAGE N ===` markers, running headers and bare page numbers are skipped; "
        "`...continued...` pages are merged into one table with a single header row. (3) The "
        "PDF's mis-OCR'd bullet glyph «» is rendered as a normal bulleted list. (4) Many OCR "
        "and spelling quirks are retained in English: «Isolpentane», «Phsyical Constants», "
        "«Mangesium Chloride», formulas such as «NH4CI», «CCI4», «CI2», «C12H22011», and odd "
        "figures such as «332.», «-119.(6)», «14.0 (9.7E4)», «07967», «1233.», «1266.90». "
        "(5) Footnote markers (1), (2), (5), (7), (8) and the «- - -» missing-value cells are "
        "retained because they carry meaning in the source tables. (6) Unicode minus signs "
        "(U+2212, U+2013) in some values and the `ʋ` (specific volume) glyph are preserved from "
        "the print. (7) For the superheated-steam table, temperature blocks are split into two "
        "tables by column count; «- - -» marks values not applicable at that pressure. (8) No "
        "equations or figures are introduced; all content is transcribed from the source tables.")


def _body(lang):
    b = []
    vi = lang == "vi"

    b.append(lead(
        "Chương này tổng hợp các dữ liệu kỹ thuật dùng trong thiết kế và lựa chọn van: quy cách "
        "vật liệu chịu áp, hằng số vật lý của hydrocarbon và các chất lỏng, tỷ số nhiệt dung "
        "riêng, tính chất của amonia, nước, hơi bão hòa và hơi quá nhiệt. Các bảng dữ liệu được "
        "chuyển nguyên vẹn từ bản in; số liệu, công thức và đơn vị được giữ như trong nguồn."
        if vi else
        "This chapter collects the engineering data used in valve design and selection: "
        "pressure-retaining material specifications, physical constants of hydrocarbons and "
        "various fluids, specific heat ratios, and the properties of ammonia, water, saturated "
        "steam and superheated steam. The data tables are reproduced from the printed source; "
        "figures, formulas and units are kept as printed."))
    b.append(note(note_terms("vi") if vi else note_terms("en")))

    # Nine source sections supplied by six section modules, in source order.
    for mod in SECTIONS:
        b.append(mod.section(lang))

    # ------------------------------------------------------------ source notes
    b.append((
        "<h3>%s</h3>" % ("Ghi chú về nguồn" if vi else "Source notes")))
    b.append(note(source_notes("vi") if vi else source_notes("en")))

    b.append(p(
        "Chương 13 chiếm các trang in 260–301 của Emerson, Control Valve Handbook, ấn bản 6 "
        "(2020), gồm chín mục 13.1–13.9. Toàn bộ nội dung là bảng dữ liệu; không có hình minh "
        "họa nào trong nguồn để vẽ lại."
        if vi else
        "Chapter 13 occupies printed pp. 260-301 (42 pages) of Emerson, Control Valve Handbook, "
        "6th edition (2020), covering nine sections, 13.1-13.9. The content is entirely data "
        "tables; the source contains no figures to redraw."))
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
