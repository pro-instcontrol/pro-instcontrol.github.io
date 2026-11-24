# -*- coding: utf-8 -*-
"""Book 9, Chapter 3 — Study of Control Strategy of the Converter in Solar
Photovoltaic Power System (EN/VI bilingual).

Source: Jin Liu and Yigong Zhang, in L. N. Jalali (ed.), *Handbook on Power
Plant Instrumentation and Control* (Bibliotex, 2019), PDF pp. 55–64, printed
pp. 39–48. PAGES_SRC = 10 counts this whole source span.

The chapter has eight numbered figures, no tables, no numbered equations and
13 numbered references. Figures are redrawn in `ppicfig3.py`; the prose is
assembled from three source-order section modules.
"""
import ppic_common as C          # noqa: F401  (page shell, used by C.build)
from ppic_common import h3, note, p
import ppic_ch03a as _a          # noqa: E402
import ppic_ch03b as _b          # noqa: E402
import ppic_ch03c as _c          # noqa: E402

PAGES_SRC = 10
BYLINE = ("Jin Liu · Yigong Zhang · School of Electric and Electronics Engineering, "
          "North China Electric Power University, China, Beijing")
TITLE_EN = "Study of Control Strategy of the Converter in Solar Photovoltaic Power System"
TITLE_VI = "Nghiên cứu chiến lược điều khiển bộ chuyển đổi trong hệ thống điện mặt trời quang điện"

_SECTIONS = (_a, _b, _c)


def note_terms(lang):
    if lang == "vi":
        return ("<b>Thuật ngữ chính.</b> hệ thống điện mặt trời quang điện (PV) · bộ chuyển đổi · "
                "bộ tăng áp DC/DC · bộ nghịch lưu (inverter) · mạng lưới điện · bộ lọc LCL · "
                "PLL (vòng khóa pha) · SPWM (điều chế độ rộng xung hình sin) · bus một chiều · "
                "THD (độ méo hài tổng) · MATLAB/Simulink · DSP TMS320F28035 · SCI · IGBT · "
                "thời gian chết (dead time) · MPPT · hệ số công suất · điều khiển vòng lặp kín · "
                "giao diện người–máy · C#.")
    return ("<b>Key terms.</b> solar photovoltaic (PV) system · converter · DC/DC boost · "
            "inverter · power grid · LCL filter · PLL · SPWM · DC bus · THD · MATLAB/Simulink · "
            "DSP TMS320F28035 · SCI · IGBT · dead time · MPPT · power factor · closed-loop "
            "control · human–machine interface · C#.")


def source_notes(lang):
    if lang == "vi":
        return ("<b>Đặc điểm của nguyên bản.</b> Văn bản in có nhiều câu thiếu chủ ngữ hoặc sai "
                "chia động từ («is consisted of», «the converter the DC power into», «voltage "
                "should great than», «with the interface, it is convenience»); bản Anh giữ những "
                "đặc điểm này, còn bản Việt dùng cách diễn đạt kỹ thuật đúng. Các chú thích hình "
                "trong bản gốc chỉ là dòng tiêu đề ngắn, vì vậy mọi hình được vẽ lại dạng vector "
                "rút gọn theo đúng cấu trúc khối, đường tín hiệu và nhãn hiển thị trên trang in. "
                "Thông số kỹ thuật của TMS320F28035 (32 bit, 3,3 V, 60 MHz, 45 GPIO, ADC 10 bit, "
                "tần số chuyển mạch 25 kHz) được giữ nguyên. Tài liệu tham khảo 3 và 9 trùng nhau "
                "trong bản in; cả hai vẫn được giữ nguyên đánh số.")
    return ("<b>Source quirks.</b> The printed prose often lacks subjects or uses non-standard "
            "verb agreement («is consisted of», «the converter the DC power into», «voltage "
            "should great than», «with the interface, it is convenience»); those phrases are kept "
            "in the English text while the Vietnamese uses correct technical meaning. Source "
            "figure captions are only short title lines, so every figure is redrawn in simplified "
            "vector form consistent with the printed block topology, signal paths and labels. "
            "The printed TMS320F28035 specifications (32-bit, 3.3 V, 60 MHz, 45 GPIO, 10-bit ADC, "
            "25 kHz switching frequency) are retained. References 3 and 9 are duplicates in the "
            "source; both are retained with their original numbering.")


def _body(lang):
    vi = lang == "vi"
    b = [C.lead(
        "Bài báo nghiên cứu chiến lược điều khiển bộ chuyển đổi trong hệ thống điện mặt trời "
        "quang điện có khả năng đấu nối lưới, xây dựng mô phỏng MATLAB/Simulink để kiểm chứng và "
        "thực hiện thử nghiệm trên bộ thiết bị phát triển năng lượng tái tạo của Texas Instruments."
        if vi else
        "This paper studies the control strategy of the converter used in a solar photovoltaic "
        "power generation system that can connect with the power grid, builds a MATLAB/Simulink "
        "simulation model to verify the strategy, and carries out experiments on a TI renewable "
        "energy development kit.")]
    for module in _SECTIONS:
        b.extend(module.section(lang))

    b.append(h3("Về nguồn tài liệu" if vi else "About the source"))
    b.append(p(
        "Chương 3 chiếm PDF tr. 55–64, tương ứng tr. 39–48 của bản in; PAGES_SRC = 10 đếm toàn "
        "bộ phân đoạn nguồn này. Nguyên bản gồm Tóm tắt, Mở đầu, Cấu trúc hệ thống, Mô hình mô "
        "phỏng, Thí nghiệm, Kết luận và 13 tài liệu tham khảo, cùng tám hình đánh số Figure 1 – "
        "Figure 8; không có bảng hay phương trình đánh số."
        if vi else
        "Chapter 3 occupies PDF pp. 55–64, corresponding to printed pp. 39–48; PAGES_SRC = 10 "
        "counts this whole source span. The source has Abstract, Introduction, Structure of the "
        "System, Simulation Model, Experiments, Conclusions and 13 references, together with eight "
        "numbered figures (Figure 1 – Figure 8); there are no tables or numbered equations."))
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
