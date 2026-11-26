# -*- coding: utf-8 -*-
"""Book 7, Chapter 22 - Graphical Estimation of Noise Produced by Turbulence
and Cavitation of Liquids (EN/VI bilingual).

Source: Baumann, *Control Valve Primer*, 5th ed. (ISA / Wiley), printed pp.
137-143 (PDF pp. 136-142; printed = PDF + 1). Seven source pages, five
computed vector graphs, one 11-column comparison table (Table 22-1, 17 rows),
Equation 22-1 plus many unnumbered formulas, four worked examples and the
pipe-schedule modifier list. Printed p.144 is absent from this e-book; the
next chapter begins on printed p.145.

The OCR text layer garbles every printed equation and the table's numeric
cells; all of them were transcribed from pypdfium2 page renders. The prose
is assembled from three source-order section modules.
"""
import cvp_ch22a as _a
import cvp_ch22b as _b
import cvp_ch22c as _c
from cvp_common import note, p

PAGES_SRC = 7
BYLINE = "Hans D. Baumann · Control Valve Primer, 5th ed. (ISA / Wiley)"
TITLE_EN = "Graphical Estimation of Noise Produced by Turbulence and Cavitation of Liquids"
TITLE_VI = "Ước tính đồ thị tiếng ồn do nhiễu loạn và xâm thực chất lỏng"


def note_terms(lang):
    """One-line bilingual glossary box."""
    if lang == "vi":
        return ("<b>Thuật ngữ chương 22.</b> phương pháp ABC dạng đồ thị · đồ thị A/B/C · "
                "tiếng ồn rối (turbulent noise) · xâm thực (cavitation) · hóa hơi (flashing) "
                "· hệ số bắt đầu xâm thực X<sub>Fz</sub> · hệ số phục hồi áp suất F<sub>L</sub> "
                "· hệ số lưu lượng C<sub>v</sub> · đường kính ống hạ lưu D · tỷ số C<sub>v</sub>/D² "
                "· áp suất đầu vào tuyệt đối P₁ (psia) · tỷ số áp suất X · 10X · A = mức cơ sở · "
                "B = hiệu chỉnh áp suất đầu vào · C = hệ số giảm áp · r<sub>w</sub> = hệ số kiểu van "
                "· mức áp suất âm thanh L<sub>Ae,1m</sub> (dBA tại 1 m) · cấp ống 40/80/160 · "
                "bộ lót chống xâm thực (anticavitation trim) · lót nhiều cấp tăng diện tích "
                "· lót điện trở một cấp · tỷ số diện tích AR · áp suất cấp đầu vào P₁s · "
                "tốc độ âm chất lỏng cᵢ · khối lượng riêng ρ · inch (in) · psi tuyệt đối (psia)")
    return ("<b>Key terms.</b> graphical ABC method · Graphs A, B and C · turbulent noise · "
            "cavitation · flashing · coefficient of incipient cavitation X<sub>Fz</sub> · "
            "pressure recovery factor F<sub>L</sub> · flow coefficient C<sub>v</sub> · "
            "downstream pipe diameter D · C<sub>v</sub>/D² ratio · absolute inlet pressure P₁ "
            "(psia) · pressure ratio X · 10X · A base level · B inlet-pressure adjustment · "
            "C pressure-drop factor · r<sub>w</sub> valve-type modifier · sound pressure level "
            "L<sub>Ae,1m</sub> (dBA at 1 m) · pipe schedule 40/80/160 · anticavitation trim · "
            "multistep trim with increasing flow areas · single-stage resistance trim · area "
            "ratio AR · first-stage inlet pressure P₁s · liquid speed of sound cᵢ · density ρ")


def _source_notes(lang):
    if lang == "vi":
        return ("<b>Đặc điểm của nguyên bản.</b> Lớp văn bản OCR làm sai toàn bộ phương trình in "
                "và nhiều ô số trong Table 22-1; các công thức và số liệu trong bản này được "
                "đọc lại từ ảnh trang in. Năm đồ thị gốc là ảnh trong PDF, được vẽ lại dạng "
                "vector với trục, lưới, họ đường cong và chú thích tương ứng. Một số lỗi in "
                "và lỗi tính toán của nguyên bản (A = 10.13 so với 10.31, log(156) so với "
                "log(1.56), 371, 18,6, 028) vẫn được giữ trong bản Anh; bản Việt dùng giá "
                "trị đúng theo ý đồ của nguyên bản. Trang in 144 không có trong bản e-book "
                "này: chương 22 kết thúc ở trang 143 và chương 23 bắt đầu ở trang 145.")
    return ("<b>Source quirks.</b> The OCR text layer garbles every printed equation and many "
            "cells of Table 22-1; all formulas and table values here were re-read from the "
            "rendered pages. The five source graphs are raster images and were redrawn as "
            "vectors with matching axes, grids, curve families and legends. Several printed "
            "typos and arithmetic slips (A = 10.13 vs 10.31, log(156) vs log(1.56), 371, "
            "18,6, 028) are retained in the English text; the Vietnamese follows the intended "
            "meaning. Printed page 144 is absent from this e-book: Chapter 22 ends on p.143 "
            "and Chapter 23 begins on p.145.")


def _body(lang):
    parts = [
        _a.body_vi() if lang == "vi" else _a.body_en(),
        _b.body_vi() if lang == "vi" else _b.body_en(),
        _c.body_vi() if lang == "vi" else _c.body_en(),
    ]
    return "".join(parts) + note(_source_notes(lang)) + p(
        "<i>Đây là bản dịch không chính thức, dùng cho mục đích học tập. Nội dung gốc © 2011 "
        "Hans D. Baumann, xuất bản bởi ISA / John Wiley &amp; Sons.</i>"
        if lang == "vi" else
        "<i>This is an unofficial translation for study purposes. Original content © 2011 "
        "Hans D. Baumann, published by ISA / John Wiley &amp; Sons.</i>")


def body_vi():
    return _body("vi")


def body_en():
    return _body("en")
