# -*- coding: utf-8 -*-
"""Book 9, Chapter 7 - Spatial Aspects of Environmental Impact of Power Plants (EN/VI).

Source: Boško Josimović and Saša Milijić, in L. N. Jalali (ed.), *Handbook on
Power Plant Instrumentation and Control* (Bibliotex, 2019), PDF pp. 141-167,
printed pp. 125-151 (printed = PDF - 16). PAGES_SRC = 27 counts the whole span.

The chapter studies Strategic Environmental Assessment (SEA) and multi-criteria
evaluation for power plants in Serbia's Energy Sector Development Strategy.
It has two figures, six tables and 59 references, with no numbered equations.
Figures are redrawn as vectors in `ppicfig7`; the prose is assembled from seven
source-order section modules.
"""
import ppic_common as C          # noqa: F401  (page shell, used by C.build)
import bolton_common as _B       # noqa: F401  (figure-caption language state)
from ppic_common import h3, note, p
import ppic_ch07a as _a          # noqa: E402
import ppic_ch07b as _b          # noqa: E402
import ppic_ch07c as _c          # noqa: E402
import ppic_ch07d as _d          # noqa: E402
import ppic_ch07e as _e          # noqa: E402
import ppic_ch07f as _f          # noqa: E402
import ppic_ch07g as _g          # noqa: E402

try:
    import ppicfig7 as F
except ImportError:                       # supplier not written yet
    class _SupplierNamespace(object):
        pass
    F = _SupplierNamespace()


def _stub_tuple(n):
    """A minimal valid 5-tuple used only while the supplier is unavailable."""
    svg = (
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 680 60" '
        'role="img"><rect x="1" y="1" width="678" height="58" '
        'fill="#f4f6fa" stroke="#9aa7bd"/>'
        '<text x="340" y="35" text-anchor="middle" '
        'style="font:14px Helvetica,sans-serif;fill:#24364f">'
        'Figure 7.%d</text></svg>' % n
    )
    return (svg,
            "Hình 7.%d · Hình minh họa." % n,
            "Figure 7.%d · Illustration." % n,
            "Hình 7.%d" % n,
            "Figure 7.%d" % n)


if not hasattr(F, "fig_f71"):
    F.fig_f71 = lambda: _stub_tuple(1)
if not hasattr(F, "fig_f72"):
    F.fig_f72 = lambda: _stub_tuple(2)

PAGES_SRC = 27
BYLINE = ("Boško Josimović · Saša Milijić · Institute of Architecture and Urban "
          "&amp; Spatial Planning of Serbia, Belgrade, Serbia")
TITLE_EN = "Spatial Aspects of Environmental Impact of Power Plants"
TITLE_VI = "Khía cạnh không gian của tác động môi trường của nhà máy điện"

_SECTIONS = (_a, _b, _c, _d, _e, _f, _g)


def note_terms(lang):
    if lang == "vi":
        return ("<b>Thuật ngữ chính.</b> đánh giá môi trường chiến lược (SEA) · Chỉ thị "
                "2001/42/EC · phát triển bền vững · quy hoạch năng lượng · đánh giá đa tiêu "
                "chí (MCE) · ra quyết định đa tiêu chí (MCDM) · hỗ trợ ra quyết định đa tiêu "
                "chí (MCDA) · MCE có sự tham gia (PMCE) · MCE xã hội (SMCE) · chỉ số phát "
                "triển bền vững · mục tiêu SEA · tiêu chí đánh giá · cường độ tác động · kích "
                "thước không gian · xác suất tác động · tác động xuyên biên giới · ma trận tác "
                "động · ưu tiên chiến lược · nhà máy nhiệt điện · năng lượng tái tạo · vùng "
                "bảo tồn · Công ước Århus · báo cáo SEA · giám sát · sự tham gia của cộng đồng.")
    return ("<b>Key terms.</b> strategic environmental assessment (SEA) · Directive 2001/42/EC "
            "· sustainable development · energy-sector planning · multi-criteria evaluation "
            "(MCE) · multi-criteria decision-making (MCDM) · multi-criteria decision aid "
            "(MCDA) · participatory multi-criteria evaluation (PMCE) · social multi-criteria "
            "evaluation (SMCE) · sustainable development indicators · SEA objectives · "
            "evaluation criteria · impact magnitude · spatial dimension · impact probability · "
            "transboundary impacts · impact matrices · strategic priorities · thermal power "
            "plants · renewable energy sources · protected areas · Århus Convention · SEA "
            "report · monitoring · public participation.")


def source_notes(lang):
    if lang == "vi":
        return ("<b>Đặc điểm của nguyên bản.</b> Văn bản in gồm 27 trang PDF (tr. in 125–151, "
                "tr. in = PDF − 16). Cả hai hình và tất cả sáu bảng đều là ảnh raster trong PDF, "
                "nên bản dịch vẽ lại hai hình dạng vector rút gọn và chép lại toàn bộ dữ liệu "
                "bảng từ ảnh trang in; nhãn và con số được giữ nguyên, kể cả dấu trừ và dấu "
                "phần trăm. Nguyên bản không có phương trình đánh số. Danh mục 59 tài liệu "
                "tham khảo được giữ đúng thứ tự in, bao gồm tên tác giả, năm, nơi xuất bản và "
                "DOI; dấu và trong tên tác giả được mã hóa để hiển thị đúng.")
    return ("<b>Source quirks.</b> The printed chapter occupies 27 PDF pages (printed pp. "
            "125-151, printed = PDF - 16). Both figures and all six tables are raster images "
            "in the PDF; the two figures are redrawn here as simplified vectors and every "
            "table value is transcribed from the page renders with its original signs and "
            "percentages retained. The source has no numbered equations. All 59 references "
            "are kept in printed order with author initials, years, venues and DOIs; "
            "ampersands in author lists are encoded so they render as printed.")


def _body(lang):
    vi = lang == "vi"
    b = [C.lead(
        "Chương này trình bày cách đánh giá môi trường chiến lược (SEA) và phương pháp đánh giá "
        "đa tiêu chí (MCE) cho các nhà máy điện trong Chiến lược phát triển ngành năng lượng của "
        "Cộng hòa Serbia: khung phương pháp, mục tiêu và chỉ số, các nhóm tiêu chí, ma trận tác "
        "động không gian, bảng xếp hạng các tác động có ý nghĩa chiến lược và kết luận chính "
        "sách, kèm 59 tài liệu tham khảo."
        if vi else
        "This chapter presents strategic environmental assessment (SEA) and multi-criteria "
        "evaluation (MCE) for power plants in Serbia's Energy Sector Development Strategy: the "
        "methodological framework, objectives and indicators, criterion sets, spatial-impact "
        "matrices, a ranking of strategically significant impacts and policy conclusions, with "
        "59 references.")]
    for module in _SECTIONS:
        b.extend(module.section(lang))

    b.append(h3("Về nguồn tài liệu" if vi else "About the source"))
    b.append(p(
        "Chương 7 chiếm PDF tr. 141–167, tương ứng tr. in 125–151 (tr. in = PDF − 16); "
        "PAGES_SRC = 27 đếm toàn bộ phân đoạn này. Nguyên bản gồm Tóm tắt, Mở đầu, Khung "
        "phương pháp, Các nhà máy điện trong Chiến lược, Thảo luận và kết luận, Lời cảm ơn và "
        "59 tài liệu tham khảo, cùng Hình 7.1, Hình 7.2 và Bảng 7.1–Bảng 7.6. Không có phương "
        "trình đánh số trong chương này."
        if vi else
        "Chapter 7 occupies PDF pp. 141-167, corresponding to printed pp. 125-151 (printed = "
        "PDF - 16); PAGES_SRC = 27 counts this whole span. Its sections cover the Abstract, "
        "Introduction, Methodological Framework, Power Plants in the Strategy, Discussion and "
        "Conclusions, Acknowledgements and 59 references, together with Figure 7.1, Figure 7.2 "
        "and Tables 7.1-7.6. There are no numbered equations."))
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
