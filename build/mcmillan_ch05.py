# -*- coding: utf-8 -*-
"""Chapter 5 - Area classification practice for gases, vapours and mists
in areas which are not freely ventilated.

Unofficial bilingual study reader of Alan McMillan, *Electrical Installations
in Hazardous Areas* (Butterworth-Heinemann, 1998), printed pp. 125-148
(PDF pp. 146-169). All sections 5.1-5.7, fifteen vector redraws and the
single worked example are included. No table or numbered equation is
printed in this chapter; the example reuses Eqs. 4.7, 4.31 and 4.32.

Prose is assembled from five sequential source-order modules; figures are
redrawn in `mcmillanfig05_a.py` and `mcmillanfig05_b.py`. Unlike Chapter 3,
this source span contains no MISSING PAGE placeholders.
"""
from mcmillan_common import note, p, refs

import mcmillan_ch05a as _a
import mcmillan_ch05b as _b
import mcmillan_ch05c as _c
import mcmillan_ch05d as _d
import mcmillan_ch05e as _e

PAGES_SRC = 24
BYLINE = "Alan McMillan · Electrical Installations in Hazardous Areas (Butterworth-Heinemann, 1998)"
TITLE_EN = "Area classification practice for gases, vapours and mists in areas which are not freely ventilated"
TITLE_VI = "Thực hành phân loại khu vực cho khí, hơi và sương mù ở nơi không thông gió tự do"

_SECTIONS = (_a, _b, _c, _d, _e)

_REFS = [
    "BS 5345. Selection, Installation and Maintenance of Electrical Apparatus in "
    "Potentially Explosive Atmospheres (other than mining applications or explosive "
    "processing or manufacture). Part 2 (1983). Classification of hazardous areas.",
    "Directorate of Labour (Netherlands) (1980). Guide to the Classification of "
    "hazardous areas in Zones in Relation to the Gas Explosion Hazard and to the "
    "Installation and Selection of Electrical Apparatus. First Edition.",
    "BS/EN 60079-10 (1996). Electrical Apparatus for Explosive Atmospheres. "
    "Classification of hazardous areas.",
    "HSE Guidance Note PM 25. Vehicle Finishing Units: Fire and Explosion Hazards.",
]


def note_terms(lang):
    if lang == "vi":
        return ("<b>Thuật ngữ chương 5.</b> phân loại khu vực nguy hiểm · thông gió hạn chế · "
                "thông gió kém · thông gió tự do · nguồn phát thải · khu vực nguy hiểm · phạm vi "
                "khu vực nguy hiểm · Vùng 0 / Vùng 1 / Vùng 2 · nguồn phát thải cấp liên tục / "
                "cấp chính / cấp phụ · thời gian tồn lưu · thông gió cưỡng bức · thông gió hút · "
                "thông gió tại chỗ · thông gió chung · thông gió độ tin cậy cao · hiệu quả thông "
                "gió · số lần thay không khí mỗi giây · cửa chớp (louvre) · lỗ/cửa thông hơi · "
                "cửa vào khí · ống dẫn · quạt · chụp hút · vách ngăn / màn che · buồng đệm · kín "
                "khí · tự đóng · tiếp giáp · ảnh hưởng của một / hai / ba bức tường · mái phẳng · "
                "mái hồi (kiểu chuồng Hà Lan) · lỗ thông hơi ở đỉnh mái · phủ qua đầu tường · "
                "khu vực hở · buồng phun sơn · lò sấy sơn · lưới · dung môi · sương mù chất lỏng · "
                "hơi · giới hạn nổ dưới (LEL) · thể tích hỗn hợp có khả năng nổ · xả sạch trước "
                "khi cấp điện")
    return ("<b>Key terms in Chapter 5.</b> area classification · restricted ventilation · "
            "poorly ventilated · freely ventilated · source of release · hazardous area · "
            "hazardous area extent · Zones 0, 1 and 2 · continuous / primary / secondary grade "
            "source of release · retention time · forced ventilation · extract ventilation · "
            "local ventilation · general ventilation · high integrity ventilation · ventilation "
            "effectiveness · air changes per second · louvre · vent · air inlet · ducting · fan · "
            "hood · divider / curtain · airlock · gas-tight · self-closing · abut · single / two / "
            "three-wall effect · flat roof · hipped (dutch-barn) roof · apex vent · wrap-around · "
            "open area · paint-spray booth · paint drying oven · grid/mesh · solvent · mist · "
            "vapour · lower explosive limit (LEL) · volume of explosive atmosphere · pre-purge")


def _source_note(lang):
    if lang == "vi":
        return ("<b>Đặc điểm của nguyên bản.</b> Chương gồm 24 trang in (125–148; "
                "in = PDF − 21) và, khác với Chương 3, không có trang <i>MISSING PAGE</i> "
                "nào. Nguyên bản in mười lăm hình (5.1–5.15), không có bảng nào và không "
                "đánh số phương trình mới; ví dụ duy nhất dùng lại Phương trình 4.7, 4.31 "
                "và 4.32. Nhiều chi tiết in được giữ nguyên kèm ghi chú: hai tiêu đề liên "
                "tiếp đều ghi 5.3.2 (tiêu đề thứ hai về logic là 5.3.3); mục 5.1.3 viện "
                "dẫn “Bảng 4.2” như một bảng thông gió không tồn tại; chú thích Hình 5.8 "
                "định nghĩa V nhưng lại dùng Y/y trong `a = E − Y` và `b = 2y − 2a`; ghi "
                "chú (3) của Hình 5.14 thiếu một từ (“is restricted Table 3.2”); và "
                "Hình 5.15 viết “eveness”. Ví dụ giữ nguyên `10 − 03` bị suy thoái, `2952` "
                "thay cho 295², các dấu `/` mờ, lỗi “Equation 4.32 from we have”, khối "
                "lượng không ghi đơn vị và ký hiệu Q dùng sai cho V<sub>m</sub>. Các "
                "tham chiếu tới Hình 3.3–3.5 và Bảng 3.1/3.2/3.8/3.10 được giữ nguyên "
                "số in, không tạo ra bảng hay hình mới.")
    return ("<b>Source quirks.</b> The chapter spans 24 printed pages (125-148; printed = "
            "PDF - 21) and, unlike Chapter 3, contains no <i>MISSING PAGE</i> placeholders. "
            "The source prints fifteen figures (5.1-5.15), no tables and no new numbered "
            "equations; the single worked example reuses Eqs. 4.7, 4.31 and 4.32. Several "
            "printed details are retained with notes: two consecutive headings are both "
            "numbered 5.3.2 (the second is logically 5.3.3); Section 5.1.3 cites \"Table 4.2\" "
            "as a ventilation table that does not exist; the Fig. 5.8 legend defines V but "
            "then uses Y/y in `a = E − Y` and `b = 2y − 2a`; Fig. 5.14 note (3) is missing a "
            "word (\"is restricted Table 3.2\"); and Fig. 5.15 prints \"eveness\". The worked "
            "example keeps the degraded `10 − 03`, `2952` for 295², ambiguous division "
            "grouping, the \"Equation 4.32 from we have\" typo, the missing mass unit and Q "
            "where Eq. 4.32 has V<sub>m</sub>. References to Figs. 3.3-3.5 and Tables "
            "3.1/3.2/3.8/3.10 retain their printed numbers; no new table or figure is invented.")


def body_vi():
    b = []
    for m in _SECTIONS:
        b.append(m.body_vi())
    b.append(refs(_REFS))
    b.append(note(_source_note("vi")))
    b.append(p("<i>Đây là bản dịch không chính thức để học tập. Nội dung gốc © 1998 Reed "
               "Educational and Professional Publishing Ltd.</i>"))
    return "".join(b)


def body_en():
    b = []
    for m in _SECTIONS:
        b.append(m.body_en())
    b.append(refs(_REFS))
    b.append(note(_source_note("en")))
    b.append(p("<i>This is an unofficial translation for study purposes. Original content "
               "© 1998 Reed Educational and Professional Publishing Ltd.</i>"))
    return "".join(b)
