# -*- coding: utf-8 -*-
"""Book 9, Chapter 11 - Saturated Adaptive Output-Feedback Power-Level Control
for Modular High Temperature Gas-Cooled Reactors (EN/VI bilingual).

Source: Zhe Dong, in L. N. Jalali (ed.), *Handbook on Power Plant
Instrumentation and Control* (Bibliotex, 2019), PDF pp. 271-299, printed
pp. 255-283 (printed = PDF - 16; PDF p.300 blank). PAGES_SRC = 29. The
chapter has 5 vector figures, 62 numbered equations, no tables, and
24 references.
"""
import ppic_common as C          # noqa: F401  (page shell, used by C.build)
import ppicfig11 as F            # noqa: F401  (figure registry, loaded first)
from ppic_common import h3, note, p
import ppic_ch11a as _a          # noqa: E402
import ppic_ch11b as _b          # noqa: E402
import ppic_ch11c as _c          # noqa: E402
import ppic_ch11d as _d          # noqa: E402
import ppic_ch11e as _e          # noqa: E402

PAGES_SRC = 29
BYLINE = ("Zhe Dong · Institute of Nuclear and New Energy Technology, Tsinghua "
          "University · Handbook on Power Plant Instrumentation and Control "
          "(Bibliotex, 2019)")
TITLE_EN = ("Saturated Adaptive Output-Feedback Power-Level Control for "
            "Modular High Temperature Gas-Cooled Reactors")
TITLE_VI = ("Điều khiển công suất thích ứng bão hòa phản hồi đầu ra cho lò "
            "phản ứng làm mát bằng khí nhiệt độ cao dạng module")

_SECTIONS = (_a, _b, _c, _d, _e)


def note_terms(lang):
    if lang == "vi":
        return ("<b>Thuật ngữ chương 11.</b> lò phản ứng mô-đun nhỏ (SMR) · MHTGR · "
                "NSSM · OTSG · HTR-PM · điều khiển công suất · phi tuyến · bất "
                "định tham số · bão hòa đầu vào điều khiển · phản hồi đầu ra · "
                "điều khiển thích ứng · phần tử bão hòa · bù bão hòa · ổn định "
                "nhờ đầu vào (ISS) · Lyapunov · shifted-ectropy · động học neutron "
                "· nhiệt thủy lực lò phản ứng · tốc độ thanh điều khiển · RFP · "
                "tham số thích ứng trực tuyến")
    return ("<b>Key terms.</b> small modular reactor (SMR) · MHTGR · NSSM · OTSG · "
            "HTR-PM · power-level control · nonlinearity · parameter uncertainty · "
            "control input saturation · output feedback · adaptive control · "
            "saturation element · saturation compensation · input-to-state "
            "stability (ISS) · Lyapunov function · shifted-ectropy · neutron "
            "kinetics · reactor thermal-hydraulics · control-rod speed · RFP · "
            "online parameter adaptation")


def source_notes(lang):
    if lang == "vi":
        return ("<b>Đặc điểm của nguyên bản.</b> Lớp văn bản PDF không chứa 62 "
                "phương trình hiển thị; toàn bộ được đọc lại từ ảnh trang in và "
                "trình bày bằng HTML với số hiệu gốc (1)–(62). Năm hình gốc gồm "
                "sơ đồ NSSM, vi lưới điện, cấu trúc vòng lặp và hai họ sáu đồ thị "
                "mô phỏng được vẽ lại dạng vector. Nguyên bản không có bảng. "
                "Chương có phần lời cảm ơn và 24 tài liệu tham khảo.")
    return ("<b>Source quirks.</b> The PDF text layer omits all 62 displayed "
            "equations; they were re-read from the printed page images and are "
            "presented in HTML with their original numbers (1)-(62). The five "
            "source figures (NSSM layout, micro-grid, closed-loop structure and "
            "two six-panel simulation sets) were redrawn as vectors. The printed "
            "chapter has no tables. It includes an acknowledgments section and "
            "twenty-four references.")


def _body(lang):
    b = [C.lead(
        "Chương này đề xuất bộ điều khiển công suất thích ứng bão hòa, phản hồi "
        "đầu ra cho MHTGR, chứng minh ổn định nhờ đầu vào và thử nghiệm bằng mô "
        "phỏng điều khiển chuyển công suất của HTR-PM."
        if lang == "vi" else
        "This chapter proposes a saturated adaptive output-feedback power-level "
        "controller for MHTGRs, proves input-to-state stability and tests it in "
        "simulations of large power maneuvers for the HTR-PM plant.")]
    for module in _SECTIONS:
        b.extend(module.section(lang))
    b.append(h3("Về nguồn tài liệu" if lang == "vi" else "About the source"))
    b.append(p(
        "Chương 11 chiếm PDF tr. 271–299, tương ứng tr. 255–283 của bản in (PDF "
        "tr. 300 để trống); PAGES_SRC = 29. Nguyên bản gồm năm hình, không có "
        "bảng, 62 phương trình được đánh số và 24 tài liệu tham khảo."
        if lang == "vi" else
        "Chapter 11 occupies PDF pp. 271-299, corresponding to printed pp. "
        "255-283 (PDF p.300 is blank); PAGES_SRC = 29. The printed chapter has "
        "five figures, no tables, 62 numbered equations and twenty-four "
        "references."))
    b.append(note(source_notes(lang)))
    b.append(p(
        "<i>Đây là bản dịch không chính thức, dùng cho mục đích học tập. Nội dung "
        "gốc © 2019 Bibliotex; từng chương © tác giả tương ứng, theo giấy phép "
        "Creative Commons.</i>"
        if lang == "vi" else
        "<i>This is an unofficial translation for study purposes. Original content "
        "© 2019 Bibliotex; individual chapters © their authors, under a Creative "
        "Commons licence.</i>"))
    return "".join(b)


def body_vi():
    return _body("vi")


def body_en():
    return _body("en")
