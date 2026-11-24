# -*- coding: utf-8 -*-
"""Chapter 3, "Transducers - III" (EN/VI bilingual).

Source: Prasad, Jayaswal & Priye, *Instrumentation and Process Control*
(I.K. International, 2019), PDF pp. 136-215, printed pp. 124-203.
PAGES_SRC = 80 counts this whole source span.

The chapter contains four numbered sections, 72 numbered figures, three
numbered tables and 45 numbered equations.  Every figure is redrawn as a
vector in the four `ipcfig3_*` supplier modules; the prose is assembled from
nine source-order section modules.
"""
import ipc_common as C          # noqa: F401  (page shell, used by C.build)
from ipc_common import h3, note, p
import ipc_ch03_a as _a        # noqa: E402
import ipc_ch03_b as _b        # noqa: E402
import ipc_ch03_c as _c        # noqa: E402
import ipc_ch03_d as _d        # noqa: E402
import ipc_ch03_e as _e        # noqa: E402
import ipc_ch03_f as _f        # noqa: E402
import ipc_ch03_g as _g        # noqa: E402
import ipc_ch03_h as _h        # noqa: E402
import ipc_ch03_i as _i        # noqa: E402

PAGES_SRC = 80
BYLINE = ("Janardan Prasad · M. N. Jayaswal · Vishnu Priye · "
          "Instrumentation and Process Control (I.K. International, 2019)")
TITLE_EN = "Transducers – III"
TITLE_VI = "Bộ chuyển đổi – III"

_SECTIONS = (_a, _b, _c, _d, _e, _f, _g, _h, _i)


def note_terms(lang):
    if lang == "vi":
        return ("<b>Thuật ngữ chính.</b> nhiệt độ · nhiệt kế thủy ngân · nhiệt kế khí · nhiệt trở "
                "(RTD) · cặp nhiệt điện (thermocouple) · điểm nóng / điểm lạnh · bù điểm lạnh · "
                "đường cong hiệu chuẩn · lưu lượng · phương trình lưu lượng · phần tử sơ cấp · "
                "tấm lỗ (orifice) · vòi phun · venturi · hệ số Cv · độ nhớt · số Reynolds · mức "
                "chất lỏng · đo mức liên tục · đo mức rời rạc · phao · báo mức · radar · "
                "siêu âm · áp suất tĩnh · đầu dò · hiệu chuẩn · ISO · IEC.")
    return ("<b>Key terms.</b> temperature · mercury-in-glass thermometer · gas thermometer · "
            "RTD · thermocouple · hot junction · cold junction · cold-junction compensation · "
            "calibration curve · flow · universal flow formula · primary element · orifice plate · "
            "nozzle · venturi · flow coefficient · viscosity · Reynolds number · level · "
            "continuous level · discrete level · float · level switch · radar · ultrasonic · "
            "static pressure · probe · calibration · ISO · IEC.")


def source_notes(lang):
    if lang == "vi":
        return ("<b>Đặc điểm của nguyên bản.</b> PDF lưu phần lớn văn bản dưới dạng mã glyph "
                "(/Gnn); bản giải mã work/ipc_decoded.txt đổi mỗi mã thành ký tự tương ứng nhưng "
                "vẫn giữ nhiều lỗi OCR, ký hiệu bị rời rạc và lỗi chính tả. Các phương trình in "
                "được viết lại bằng ký hiệu toán học chuẩn tại chỗ; thứ tự hệ số được chọn theo "
                "nghĩa vật lý hợp lý nhất. Hình trong PDF là ảnh, chỉ nhãn và chú thích còn lại "
                "trong lớp văn bản, vì vậy mọi hình được vẽ lại dạng vector rút gọn. Các bảng "
                "hiệu chuẩn nhiệt độ dài được chép lại từ trang in với số liệu và dung sai giữ "
                "nguyên. Một số lỗi của nguyên bản được giữ trong bản Anh, còn bản Việt dùng "
                "nghĩa đúng.")
    return ("<b>Source quirks.</b> The PDF stores most body text as glyph codes (/Gnn); the decoded "
            "file work/ipc_decoded.txt converts each code to its character but retains OCR "
            "artifacts, scattered symbols and typos. Printed equations are rendered with standard "
            "mathematical notation in place, with coefficient order following the most plausible "
            "physical meaning. Figures are images in the PDF and only their printed labels and "
            "captions survive in the text layer, so every figure is redrawn in simplified vector "
            "form. The long thermocouple calibration tables are transcribed from the printed "
            "pages with their values and tolerances unchanged. A few source quirks are kept in the "
            "English text while the Vietnamese uses the intended meaning.")


def _body(lang):
    vi = lang == "vi"
    b = [C.lead(
        "Chương này trình bày phép đo nhiệt độ bằng nhiệt kế, nhiệt trở và cặp nhiệt điện cùng "
        "các vấn đề về điểm lạnh và độ chính xác; sau đó là phương trình lưu lượng và các phần tử "
        "sơ cấp; cuối cùng là các phương pháp đo mức liên tục và rời rạc."
        if vi else
        "This chapter covers temperature measurement by thermometers, RTDs and thermocouples "
        "together with cold-junction and accuracy questions; it then derives the universal flow "
        "formula and surveys primary flow elements; it closes with continuous and discrete level "
        "measurement methods.")]
    for module in _SECTIONS:
        b.extend(module.section(lang))

    b.append(h3("Về nguồn tài liệu" if vi else "About the source"))
    b.append(p(
        "Chương 3 chiếm PDF tr. 136–215, tương ứng tr. 124–203 của bản in; PAGES_SRC = 80 đếm "
        "toàn bộ phân đoạn nguồn này. Nguyên bản gồm bốn mục: Transducers and Measurement of "
        "Temperature, Other Considerations, Measurement of Flow và Measurement of Level. Có 72 "
        "hình đánh số Figure 3.1 – Figure 3.72, ba bảng Table 3.2 – Table 3.4 và 45 phương trình "
        "đánh số (3.1) – (3.45); tất cả được dựng lại dạng vector hoặc chép lại từ trang in."
        if vi else
        "Chapter 3 occupies PDF pp. 136-215, corresponding to printed pp. 124-203; PAGES_SRC = 80 "
        "counts this whole source span. Its four sections are Transducers and Measurement of "
        "Temperature, Other Considerations, Measurement of Flow and Measurement of Level. The "
        "source contains 72 numbered figures (Figure 3.1 - Figure 3.72), three numbered tables "
        "(Table 3.2 - Table 3.4) and 45 numbered equations (3.1) - (3.45); all are redrawn as "
        "vectors or transcribed from the printed pages here."))
    b.append(note(source_notes(lang)))
    b.append(p(
        "<i>Đây là bản dịch không chính thức, dùng cho mục đích học tập. Nội dung gốc © 2019 I.K. "
        "International; các chương của sách phát hành theo giấy phép Creative Commons.</i>"
        if vi else
        "<i>This is an unofficial translation for study purposes. Original content © 2019 I.K. "
        "International; the individual chapters are released under Creative Commons.</i>"))
    return "".join(b)


def body_vi():
    return _body("vi")


def body_en():
    return _body("en")
