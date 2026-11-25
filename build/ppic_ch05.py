# -*- coding: utf-8 -*-
"""Book 9, Chapter 5 — Analysis of the Spatial Separation Effects of
Thorium/Uranium Fuels in Block-Type HTRs (EN/VI bilingual).

Source: Ming Ding and Jie Huang, in L. N. Jalali (ed.), *Handbook on Power
Plant Instrumentation and Control* (Bibliotex, 2019), PDF pp. 95–121,
printed pp. 79–105. PAGES_SRC = 27 counts this whole source span.

The chapter has 17 numbered figures, five numbered tables, five printed
equations (1)–(5) and 18 references. Figures are redrawn in the three
`ppicfig5_*` supplier modules; prose is assembled from seven source-order
section modules.
"""
import ppic_common as C          # noqa: F401  (page shell, used by C.build)
from ppic_common import h3, note, p
import ppic_ch05a as _a          # noqa: E402
import ppic_ch05b as _b          # noqa: E402
import ppic_ch05c as _c          # noqa: E402
import ppic_ch05d as _d          # noqa: E402
import ppic_ch05e as _e          # noqa: E402
import ppic_ch05f as _f          # noqa: E402
import ppic_ch05g as _g          # noqa: E402

PAGES_SRC = 27
BYLINE = ("Ming Ding · Jie Huang · Harbin Engineering University, Harbin, China · "
          "China Nuclear Power Technology Research Institute, Shenzhen, China")
TITLE_EN = "Analysis of the Spatial Separation Effects of Thorium/Uranium Fuels in Block-Type HTRs"
TITLE_VI = "Phân tích ảnh hưởng của sự tách không gian giữa nhiên liệu thori/urani trong lò HTR dạng khối"

_SECTIONS = (_a, _b, _c, _d, _e, _f, _g)


def note_terms(lang):
    if lang == "vi":
        return ("<b>Thuật ngữ chính.</b> lò phản ứng nhiệt độ cao kiểu khối (HTR) · nhiên liệu "
                "thori/urani · tách không gian · không tách · tách ở cấp TRISO · tách ở cấp "
                "kênh · tách ở cấp khối · chu trình nhiên liệu · hạt nhiên liệu TRISO · "
                "compact nhiên liệu · khối nhiên liệu · làm giàu hiệu dụng của U‐235 · "
                "tồn kho ban đầu của U‐235 · hệ số nhân hiệu dụng ban đầu k_eff · tỷ lệ "
                "chuyển đổi trung bình (ACR) · sơ đồ tính toán hai bước · phương pháp năm "
                "hệ số · chi phí chu trình nhiên liệu · chi phí vòng đời san đều (levelized "
                "lifetime cost) · EFPD · MOX · SBT · SBU · WASB · Th‐232 · U‐233 · U‐235 · "
                "U‐238 · phân tán neutron.")
    return ("<b>Key terms.</b> block-type high-temperature gas-cooled reactor (HTR) · "
            "thorium/uranium fuel · spatial separation · no separation · TRISO-level "
            "separation · channel-level separation · block-level separation · fuel cycle · "
            "TRISO particle · fuel compact · fuel block · initial effective enrichment of "
            "U-235 · initial inventory of U-235 · initial effective multiplication factor "
            "k_eff · average conversion ratio (ACR) · two-step calculation scheme · "
            "five-factor formula · fuel cycle cost · levelized lifetime cost · EFPD · MOX · "
            "SBT · SBU · WASB · Th-232 · U-233 · U-235 · U-238 · neutron diffusion.")


def source_notes(lang):
    if lang == "vi":
        return ("<b>Đặc điểm của nguyên bản.</b> Lớp văn bản của PDF giữ lại tiêu đề hình, bảng "
                "và phần lớn văn bản nhưng xáo trộn công thức toán học; các phương trình (1)–(5) "
                "được đọc lại từ trang in và viết bằng ký hiệu chuẩn. Năm bảng số liệu được chép "
                "lại từ bản in với giá trị và phần trăm giữ nguyên. Hình trong PDF là ảnh màu "
                "của lõi lò, cấu hình nhiên liệu và đồ thị đường cong; mọi hình được vẽ lại dạng "
                "vector rút gọn với nhãn và chú thích tương ứng. Một số ký hiệu in (ví dụ k_eff "
                "và chỉ số dạng U5, Th2) được chuẩn hóa cho dễ đọc.")
    return ("<b>Source quirks.</b> The PDF text layer preserves figure and table captions and "
            "most prose but scrambles mathematical expressions; equations (1)–(5) were read from "
            "the printed pages and rendered with standard notation. All five numeric tables are "
            "transcribed with their printed values and percentages. Figures are colour images of "
            "reactor cores, fuel configurations and curves; every figure is redrawn as a "
            "simplified vector with matching labels and captions. A few printed symbols (for "
            "example k_eff and U5/Th2 subscripts) are normalized for readability.")


def _body(lang):
    vi = lang == "vi"
    b = [C.lead(
        "Bài báo so sánh bốn mức tách không gian của nhiên liệu thori/urani trong lò HTR dạng "
        "khối — không tách, tách ở cấp TRISO, cấp kênh và cấp khối — bằng sơ đồ tính toán hai "
        "bước, rồi đối chiếu làm giàu ban đầu của U‐235, hệ số nhân, tỷ lệ chuyển đổi và chi "
        "phí chu trình nhiên liệu theo hàm lượng thori."
        if vi else
        "This chapter compares four spatial separation levels of thorium/uranium fuel in "
        "block-type HTRs — no separation, TRISO level, channel level and block level — using a "
        "two-step calculation scheme, then compares the initial U-235 enrichment, multiplication "
        "factor, conversion ratio and fuel cycle cost as functions of thorium content.")]
    for module in _SECTIONS:
        b.extend(module.section(lang))

    b.append(h3("Về nguồn tài liệu" if vi else "About the source"))
    b.append(p(
        "Chương 5 chiếm PDF tr. 95–121, tương ứng tr. 79–105 của bản in; PAGES_SRC = 27 đếm "
        "toàn bộ phân đoạn nguồn này. Nguyên bản gồm Tóm tắt, Mở đầu, Hình học và phương pháp "
        "tính toán, Kết quả và thảo luận, Kết luận, Lời cảm ơn và 18 tài liệu tham khảo, cùng "
        "17 hình (Figure 5.1 – Figure 5.17), năm bảng (Table 5.1 – Table 5.5) và các phương "
        "trình đánh số (1)–(5)."
        if vi else
        "Chapter 5 occupies PDF pp. 95–121, corresponding to printed pp. 79–105; PAGES_SRC = 27 "
        "counts this whole source span. The source contains Abstract, Introduction, block-type "
        "HTR geometry and calculation methodologies, Results and Discussion, Conclusions, "
        "Acknowledgements and 18 references, together with 17 figures (Figure 5.1 - Figure "
        "5.17), five tables (Table 5.1 - Table 5.5) and numbered equations (1) - (5)."))
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
