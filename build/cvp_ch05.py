# -*- coding: utf-8 -*-
"""Book 7, Chapter 5 - Valve Sizing Made Easy (EN/VI bilingual).

Source: Baumann, *Control Valve Primer*, 5th ed. (ISA / Wiley), printed pp.
24-46 (PDF pp. 31-53).  The chapter is assembled from three section
modules: cvp_ch05a (opening through Other Methods), cvp_ch05b (Pipe
Reducers through Figure 5-2) and cvp_ch05c (Small Flow Valve Sizing
through Additional Reading).  Figures 5-1 and 5-2 are redrawn as vectors
in cvpfig5.py; all five source tables and equations (5-1) through (5-18)
are retained.
"""
from cvp_common import note

import cvp_ch05a as A
import cvp_ch05b as B
import cvp_ch05c as C

PAGES_SRC = 23
BYLINE = "Hans D. Baumann · Control Valve Primer, 5th ed. (ISA / Wiley)"
TITLE_EN = "Valve Sizing Made Easy"
TITLE_VI = "Định cỡ van dễ dàng"


def note_terms(lang):
    if lang == "vi":
        return ("<b>Thuật ngữ chương 5.</b> định cỡ van (valve sizing) · hệ số lưu lượng "
                "C<sub>v</sub> · hệ số phục hồi áp suất F<sub>L</sub> · hệ số hình học "
                "đường ống F<sub>p</sub> · F<sub>Lp</sub> khi lắp giữa hai đoạn thu nhỏ · "
                "chảy dưới tới hạn / chảy tới hạn (subcritical / choked flow) · chênh áp ΔP · "
                "áp suất hơi P<sub>v</sub> · áp suất tới hạn P<sub>c</sub> · ΔP<sub>s</sub> · "
                "tỷ lệ sụt áp X<sub>T</sub> · hệ số giãn nở Y · hệ số tỷ lệ nhiệt dung F<sub>k</sub> · "
                "đoạn thu nhỏ đường ống (pipe reducer) · số Reynolds van Re<sub>v</sub> · "
                "hệ số Reynolds van F<sub>R</sub> · hệ số F<sub>d</sub> · độ nhớt động học "
                "(centistoke, cSt) · độ nhớt động (centipoise, cP) · giây Saybolt (SSU) · "
                "van lưu lượng nhỏ · đế van / bệ van / mặt tựa của van (seat) · "
                "xâm thực (cavitation) · hóa hơi (flashing) · hành trình van · dải điều tiết.")
    return ("<b>Key terms.</b> valve sizing · flow coefficient C<sub>v</sub> · liquid pressure "
            "recovery factor F<sub>L</sub> · piping geometry factor F<sub>p</sub> · "
            "F<sub>Lp</sub> for valves between reducers · subcritical / choked flow · pressure "
            "drop ΔP · vapor pressure P<sub>v</sub> · critical pressure P<sub>c</sub> · "
            "ΔP<sub>s</sub> · pressure-drop ratio X<sub>T</sub> · expansion factor Y · "
            "specific-heat-ratio factor F<sub>k</sub> · pipe reducers · valve Reynolds number "
            "Re<sub>v</sub> · valve Reynolds number factor F<sub>R</sub> · F<sub>d</sub> factor "
            "· kinematic viscosity (centistokes, cSt) · dynamic viscosity (centipoise, cP) · "
            "Saybolt seconds (SSU) · small-flow valve · seat · cavitation · flashing · valve "
            "travel · rangeability.")


def _source_note(lang):
    if lang == "vi":
        return (
            "<b>Ghi chú về nguồn.</b> (1) Bản PDF lưu các phương trình dưới dạng ký tự bị lệch, "
            "nên các công thức (5-1)–(5-18) được trình bày lại bằng ký hiệu chuẩn (q, C<sub>v</sub>, "
            "F<sub>L</sub>, F<sub>p</sub>, ΔP, P<sub>v</sub>, P<sub>c</sub>, X<sub>T</sub>, Y, "
            "F<sub>k</sub>, Re<sub>v</sub>, F<sub>R</sub>, F<sub>d</sub>…), giữ nguyên số hiệu "
            "và hệ số in; đây không phải bản sao chụp lại từ bản in. (2) Bảng dạng hai cột "
            "「dòng dưới tới hạn / dòng tới hạn」 trong nguyên bản được trải thành các dòng "
            "tuần tự. (3) Một số kết quả ví dụ không khớp hoàn toàn với công thức tái dựng "
            "(ví dụ các giá trị 64 và 83,7 ở ví dụ độ nhớt, hay F<sub>L</sub> = 0,4/0,89 = 0,42); "
            "giữ nguyên theo bản in. (4) Giữ nguyên lỗi chính tả và in ấn của nguồn như "
            "“process date”, “Napthalene”, “March1993” và trị số 85 trong dòng van cắm lệch "
            "tâm (rõ ràng là 0,85). (5) Nguyên bản viện dẫn “Table 5-4” cho các lựa chọn thực "
            "tế lấy từ Bảng 5-5; giữ nguyên cách viện dẫn. (6) Chú thích Hình 5-1 nằm giữa "
            "câu trong lớp văn bản; bản dịch giữ nguyên câu và đặt hình đúng vị trí chú thích. "
            "(7) Theo thống nhất thuật ngữ của dự án, seat được dịch là đế van / bệ van / "
            "mặt tựa của van, cavitation là xâm thực và flashing là hóa hơi.")
        return (
            "<b>Source notes.</b> (1) The PDF stores its equations as damaged glyph sequences, "
            "so equations (5-1)–(5-18) are presented as symbolic equivalents (q, C<sub>v</sub>, "
            "F<sub>L</sub>, F<sub>p</sub>, ΔP, P<sub>v</sub>, P<sub>c</sub>, X<sub>T</sub>, Y, "
            "F<sub>k</sub>, Re<sub>v</sub>, F<sub>R</sub>, F<sub>d</sub>…), keeping the original "
            "numbers and constants; these are not facsimile copies of the printed formulae. "
            "(2) The two-column subcritical/critical layouts in the source are flattened into "
            "sequential entries. (3) A few worked-example values do not reconcile with the "
            "reconstructed equations (e.g. 64 and 83.7 in the viscosity example, or "
            "F<sub>L</sub> = 0.4/0.89 = 0.42); they are retained as printed. (4) Source typos "
            "and print quirks are kept: “process date”, “Napthalene”, “March1993” and the "
            "value 85 in the eccentric rotary plug row (evidently 0.85). (5) The text cites "
            "“Table 5-4” for choices actually drawn from Table 5-5; the citation is retained. "
            "(6) The Figure 5-1 caption interrupts a sentence in the text layer; the sentence "
            "is kept whole and the figure is placed at the caption point. (7) Project "
            "terminology standardizes the Vietnamese renderings of <i>seat</i>, "
            "<i>cavitation</i> and <i>flashing</i> across the site.")


def _body(lang):
    b = []
    b.append(A.body_vi() if lang == "vi" else A.body_en())
    b.append(B.body_vi() if lang == "vi" else B.body_en())
    b.append(C.body_vi() if lang == "vi" else C.body_en())
    b.append(note(_source_note(lang)))
    return "".join(b)


def body_vi():
    return _body("vi")


def body_en():
    return _body("en")
