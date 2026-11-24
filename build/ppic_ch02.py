# -*- coding: utf-8 -*-
"""Book 9, Chapter 2 - Advanced Measuring (Instrumentation) Methods for
Nuclear Installations: A Review (EN/VI bilingual).

Source: L. N. Jalali (ed.), *Handbook on Power Plant Instrumentation and
Control* (Bibliotex, 2019), PDF pp. 29-54, printed pp. 13-38. Twenty-six
source pages, seven vector figures, no tables and 76 numbered references.
The prose is split into three section modules (`ppic_ch02a/b/c.py`) and the
figures into `ppicfig2.py`.
"""
import ppic_common as C  # noqa: F401  (page shell, used by C.build)
import ppic_ch02a as A
import ppic_ch02b as B
import ppic_ch02c as Cc
from ppic_common import h3, note, p

PAGES_SRC = 26
BYLINE = ("Wang Qiu-kuan · Lin Chang-hua · Yang Yan · "
          "Handbook on Power Plant Instrumentation and Control (Bibliotex, 2019)")
TITLE_EN = "Advanced Measuring (Instrumentation) Methods for Nuclear Installations: A Review"
TITLE_VI = "Phương pháp đo tiên tiến cho các cơ sở hạt nhân: Tổng quan"


def note_terms(lang):
    """One-line bilingual glossary box."""
    if lang == "vi":
        return ("<b>Thuật ngữ chính.</b> phương pháp đo tiên tiến · cơ sở hạt nhân · lò phản ứng "
                "nghiên cứu · lò ATR · detector MMGAS · nhiệt kế nhiễu (noise thermometer) · "
                "buồng đếm tỷ lệ mô mô (tissue equivalent proportional counter) · quang phổ kế "
                "đa cầu (multisphere spectrometer) · buồng phân hạch urani / plutoni · detector "
                "neutron tự cấp (self-powered neutron detector) · detector gamma tự cấp · "
                "antineutrino lò phản ứng · detector scintillator chất lỏng pha Gadolinium · "
                "cảm biến sợi quang (OFS) · giao thoa kế quét bước sóng (SWI) · chu trình nhiên "
                "liệu hạt nhân · đầu / giữa / cuối chu trình · nhiên liệu đã chiếu xạ · lò phản "
                "ứng công suất · an toàn và an ninh hạt nhân · kiểm kê vật liệu (materials "
                "accountancy) · kiểm soát bao chứa (containment verification) · kiểm tra "
                "không phá hủy (NDA) · IAEA · bảo vệ và an ninh nội địa · tai nạn hạt nhân · "
                "mất nước làm mát (LOCA) · mất toàn bộ nước cấp (TLOFW) · đứt ống SGTR · mất "
                "điện trạm (SBO) · SVC · GMDH · SVM · SVR · PNN · BPNA · AFDS · GS · AMS · "
                "SSNTD · sản phẩm phân hạch (FP) · quang phổ gamma · phản xạ miền thời gian "
                "(TDR) · ESMADP · MPBR · đầu dò Cherenkov nước áp lực.")
    return ("<b>Key terms.</b> advanced measuring methods · nuclear installation · research "
            "reactor · Advanced Test Reactor (ATR) · MMGAS detector · noise thermometer · "
            "tissue equivalent proportional counter · multisphere spectrometer · uranium and "
            "plutonium fission chambers · self-powered neutron detector · self-powered gamma "
            "detector · reactor antineutrino · Gd-doped liquid scintillator · optical fiber "
            "sensor (OFS) · swept wavelength interferometry (SWI) · nuclear fuel cycle · front "
            "end, service period and back end · spent fuel · safeguards and homeland security · "
            "nondestructive assay (NDA) · IAEA · materials accountancy · containment "
            "verification · nuclear accident · loss of coolant accident (LOCA) · total loss of "
            "feedwater (TLOFW) · steam generator tube rupture (SGTR) · station blackout (SBO) · "
            "SVC · GMDH · SVM · SVR · PNN · BPNA · AFDS · GS · AMS · SSNTD · fission products "
            "(FP) · gamma spectrometry · time domain reflectometry (TDR) · ESMADP · MPBR · "
            "pressurized water Cherenkov detector.")


def _body(lang):
    vi = lang == "vi"
    b = []
    b.extend(A.section(lang))
    b.extend(B.section(lang))
    b.extend(Cc.section(lang))

    b.append(h3("Về nguồn tài liệu", "About the source"))
    b.append(p(
        "Chương 2 chiếm PDF tr. 29–54, tương ứng tr. 13–38 của bản in; PAGES_SRC = 26 đếm toàn "
        "bộ phân đoạn nguồn này. Các mục theo mục lục là Abstract, Introduction, Nuclear Power "
        "Reactors, Nuclear Fuel Cycle, Safeguards and Homeland Security, Nuclear Accident, After "
        "Action, and Analysis, Conclusions, Acknowledgments và References. Nguyên bản có đúng "
        "bảy hình đánh số Figure 1 – Figure 7, không có bảng, và 76 tài liệu tham khảo đánh số "
        "1–76; tất cả được giữ lại ở đây."
        if vi else
        "Chapter 2 occupies PDF pp. 29-54, corresponding to printed pp. 13-38; PAGES_SRC = 26 "
        "counts this whole source span. Its sections are Abstract, Introduction, Nuclear Power "
        "Reactors, Nuclear Fuel Cycle, Safeguards and Homeland Security, Nuclear Accident, After "
        "Action, and Analysis, Conclusions, Acknowledgments and References. The source contains "
        "exactly seven numbered figures, Figure 1 - Figure 7, no tables and 76 numbered "
        "references (1-76); all are retained here."))

    b.append(note(
        ("<b>Đặc điểm của nguyên bản.</b> Lớp văn bản OCR có các dấu gạch nối khi xuống dòng "
         "(«Self-Powered», «ANALY-SIS», «nondestructive assay» bị tách dòng); bản dịch ghép lại "
         "thành từ hoàn chỉnh. Các tiêu đề in viết hoa toàn bộ được giữ dạng viết hoa trong bản "
         "Anh và dịch sang chữ thường có nhấn trọng âm trong bản Việt. Nhiều câu trong nguyên "
         "bản mang đặc điểm ngôn ngữ của tác giả không phải bản ngữ Anh (ví dụ «in last decade», "
         "«instrumentations to measuring», «the technology which persisted nearly unchanged», "
         "«there is a possibility of application … in condition of NPP»); bản Anh giữ nguyên các "
         "cấu trúc đó, bản Việt dùng nghĩa đúng tự nhiên. Ký hiệu đồng vị và đơn vị được trình "
         "bày dạng văn bản thuần (ví dụ 131I, 134Cs, 137Cs, ut Bq/m3) để tránh lỗi HTML. "
         "Tham chiếu [3] của nguồn có ký hiệu «[55]» ngay trong nhan đề; bản dịch giữ nguyên. "
         "Hình 2.4 giữ hướng mũi tên như bản in. Cả bảy hình là bản vẽ lại vector đã đơn giản "
         "hóa, không phải ảnh gốc."
         if vi else
         "<b>Source quirks.</b> The OCR text contains line-break hyphenations (for example "
         "«Self-Powered», «ANALY-SIS» and split «nondestructive assay»); these have been "
         "rejoined. Printed all-capital headings are kept in capitals in the English text and "
         "rendered with normal Vietnamese diacritics in the translation. Many sentences retain "
         "the non-native English phrasing of the source (for example 'in last decade', "
         "'instrumentations to measuring', 'the technology which persisted nearly unchanged', "
         "'there is a possibility of application ... in condition of NPP'); the English text "
         "keeps those structures while the Vietnamese uses the intended meaning. Isotope symbols "
         "and units are rendered as plain text (e.g. 131I, 134Cs, 137Cs, ut Bq/m3) to avoid "
         "HTML errors. Source reference [3] prints a stray '[55]' inside its title; it is kept. "
         "Figure 2.4 follows the arrow directions of the printed original. All seven figures "
         "are simplified vector redrawings, not scans of the original artwork.")))

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
