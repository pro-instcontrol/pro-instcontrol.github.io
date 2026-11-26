# -*- coding: utf-8 -*-
"""Book 9, Chapter 8 - Optimization and Damping Performance of a Coal-Fired
Power Plant Building Equipped with Multiple Coal Bucket Dampers (EN/VI).

Source: Ling-Yun Peng, Ying-Jie Kang, Zong-Rui Lai and Yu-Ke Deng, in L. N.
Jalali (ed.), *Handbook on Power Plant Instrumentation and Control* (Bibliotex,
2019), PDF pp. 169-214, printed pp. 153-198 (printed = PDF - 16). PAGES_SRC = 46
counts the whole source span.

The chapter proposes a parameter-optimization design for multiple coal bucket
dampers (CBDs) as a multiple tuned mass damper system, validates it with a
1:30 shaking-table model and finite-element analysis, and studies 53 seismic
excitations. It has 21 figures, 3 tables, 38 references and many numbered
equations. Figures are redrawn as vectors in `ppicfig8`; prose is assembled
from seven source-order section modules.
"""
import ppic_common as C          # noqa: F401  (page shell, used by C.build)
import bolton_common as _B       # noqa: F401  (figure-caption language state)
from ppic_common import h3, note, p
import ppic_ch08a as _a          # noqa: E402
import ppic_ch08b as _b          # noqa: E402
import ppic_ch08c as _c          # noqa: E402
import ppic_ch08d as _d          # noqa: E402
import ppic_ch08e as _e          # noqa: E402
import ppic_ch08f as _f          # noqa: E402
import ppic_ch08g as _g          # noqa: E402

try:
    import ppicfig8 as F
except ImportError:
    class _SupplierNamespace(object):
        pass
    F = _SupplierNamespace()

PAGES_SRC = 46
BYLINE = ("Ling-Yun Peng · Ying-Jie Kang · Zong-Rui Lai · Yu-Ke Deng · "
          "Handbook on Power Plant Instrumentation and Control (Bibliotex, 2019)")
TITLE_EN = ("Optimization and Damping Performance of a Coal-Fired Power Plant "
            "Building Equipped with Multiple Coal Bucket Dampers")
TITLE_VI = ("Tối ưu hóa và hiệu năng giảm chấn của nhà máy điện than có nhiều "
            "bộ giảm chấn phễu than")

_SECTIONS = (_a, _b, _c, _d, _e, _f, _g)


def note_terms(lang):
    if lang == "vi":
        return ("<b>Thuật ngữ chương 8.</b> bộ giảm chấn phễu than (coal bucket damper, CBD) · "
                "bộ giảm chấn khối điều chỉnh nhiều cấp (multiple tuned mass damper, MTMD) · "
                "bộ giảm chấn khối điều chỉnh (TMD) · tối ưu hóa thông số · tần số riêng · "
                "tỷ số tần số · độ lệch tần số Δ · tỷ số cản ξ · tỷ số cản tối ưu ξd · "
                "hệ số bao phủ β · hàm mục tiêu · hàm truyền dịch chuyển · phản ứng động đất · "
                "mô hình cắt (shear model) · phân tích phương thức · bàn rung (shaking table) · "
                "mô hình tỷ lệ 1:30 · hệ số tương tự · phân tích phần tử hữu hạn (FEA) · "
                "SAP2000 · gia tốc nền · phổ phản ứng · dịch chuyển giữa các tầng · "
                "giảm chấn dư vết · động đất trường gần / trường xa · giá trị đỉnh · "
                "giá trị RMS · bài toán kiểm soát rung kết cấu")
    return ("<b>Key terms.</b> coal bucket damper (CBD) · multiple tuned mass damper (MTMD) · "
            "tuned mass damper (TMD) · parameter optimization · natural frequency · frequency "
            "ratio · frequency deviation Δ · damping ratio ξ · optimal damping ratio ξd · "
            "coverage rate β · objective function · displacement response transfer function · "
            "seismic response · shear model · modal decomposition · shaking table · 1:30 scale "
            "model · similarity coefficients · finite-element analysis (FEA) · SAP2000 · ground "
            "acceleration · response spectrum · interstory displacement · residual vibration · "
            "near-field / far-field earthquake · peak value · RMS value · structural vibration "
            "control")


def source_notes(lang):
    if lang == "vi":
        return ("<b>Đặc điểm của nguyên bản.</b> Các hình và bảng trong PDF là ảnh; lớp văn bản "
                "chỉ giữ nhãn rời rạc và nhiều ký hiệu toán học bị lệch. Mọi hình được vẽ lại "
                "dạng vector rút gọn sau khi đối chiếu trang in, còn số liệu bảng và hệ số "
                "trong phương trình được đọc lại từ ảnh trang. Các lỗi OCR và lỗi chính tả "
                "của nguyên bản vẫn được giữ trong bản Anh; bản Việt dùng cách diễn đạt đúng. "
                "Số phương trình được giữ theo bản in (1), (2), …, không đổi thành 8.n.")
    return ("<b>Source quirks.</b> Figures and tables are images in the PDF; the text layer keeps "
            "only scattered labels and often misplaces mathematical symbols. All figures were "
            "redrawn as simplified vectors after checking the printed pages, and table values "
            "and equation coefficients were re-read from page renders. OCR artifacts and source "
            "typos are retained in the English text; the Vietnamese uses the intended meaning. "
            "Equation numbers follow the printed sequence (1), (2), … rather than 8.n.")


def _body(lang):
    b = [C.lead(
        "Chương này trình bày phương pháp tối ưu thông số cho nhiều bộ giảm chấn phễu than "
        "(CBD) dùng làm hệ thống bộ giảm chấn khối điều chỉnh nhiều cấp (MTMD) cho nhà máy điện "
        "than, sau đó kiểm chứng bằng mô hình bàn rung tỷ lệ 1:30 và mô hình phần tử hữu hạn "
        "dưới 53 tác động địa chấn, cùng 38 tài liệu tham khảo."
        if lang == "vi" else
        "This chapter presents a parameter-optimization method for multiple coal bucket dampers "
        "(CBDs) used as a multiple tuned mass damper (MTMD) system in a coal-fired power plant "
        "building, verified by a 1:30 shaking-table model and finite-element analysis under 53 "
        "seismic excitations, with 38 references.")]
    for module in _SECTIONS:
        b.extend(module.section(lang))
    b.append(h3("Về nguồn tài liệu" if lang == "vi" else "About the source"))
    b.append(p(
        "Chương 8 chiếm PDF tr. 169–214, tương ứng tr. 153–198 của bản in; PAGES_SRC = 46 đếm "
        "toàn bộ phân đoạn nguồn này. Nguyên bản gồm 21 hình, 3 bảng, 38 tài liệu tham khảo và "
        "nhiều phương trình được đánh số theo bản in."
        if lang == "vi" else
        "Chapter 8 occupies PDF pp. 169-214, corresponding to printed pp. 153-198; PAGES_SRC = 46 "
        "counts this whole source span. The printed chapter has 21 figures, 3 tables, 38 "
        "references and many equations numbered as in the source."))
    b.append(note(source_notes(lang)))
    b.append(p(
        "<i>Đây là bản dịch không chính thức, dùng cho mục đích học tập. Bản gốc © 2019 Bibliotex; "
        "các chương phát hành theo giấy phép Creative Commons.</i>"
        if lang == "vi" else
        "<i>This is an unofficial translation for study purposes. Original work © 2019 Bibliotex; "
        "the individual chapters are released under Creative Commons.</i>"))
    return "".join(b)


def body_vi():
    return _body("vi")


def body_en():
    return _body("en")
