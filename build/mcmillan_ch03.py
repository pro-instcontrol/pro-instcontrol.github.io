# -*- coding: utf-8 -*-
"""Chapter 3 - Area classification practice for gases, vapours and mists
in freely ventilated situations / Thuc hanh phan loai khu vuc (EN/VI).

Unofficial bilingual study reader of Alan McMillan, *Electrical Installations
in Hazardous Areas* (Butterworth-Heinemann, 1998), printed pp. 43-86
(PDF pp. 64-107). All eleven printed sections (3.1-3.4.11), four recoverable
tables and sixteen recoverable vector figures are included. Eight source
pages are literal "MISSING PAGE" placeholders in the supplied PDF and are
flagged in both languages; the missing material is not invented.

Prose is assembled from five sequential source-order modules; figures are
redrawn in four `mcmillanfig03_*` supplier modules.
"""
from mcmillan_common import note, p, refs

import mcmillan_ch03a as _a
import mcmillan_ch03b as _b
import mcmillan_ch03c as _c
import mcmillan_ch03d as _d
import mcmillan_ch03e as _e

PAGES_SRC = 44
BYLINE = "Alan McMillan · Electrical Installations in Hazardous Areas (Butterworth-Heinemann, 1998)"
TITLE_EN = "Area classification practice for gases, vapours and mists in freely ventilated situations"
TITLE_VI = "Thực hành phân loại khu vực đối với khí, hơi và sương mù trong tình huống thông gió tự nhiên"

_SECTIONS = (_a, _b, _c, _d, _e)

_REFS = [
    "BS 5345. Selection, Installation and Maintenance of Electrical Apparatus for use in "
    "Potentially Explosive Atmospheres (other than mining operations or explosives "
    "processing and manufacture). Part 2 (1983). Classification of hazardous areas.",
    "RoSPA/ICI Engineering Codes and Regulations, Electrical Installations in Flammable "
    "Atmospheres (1973). Group C (Electrical), Volume 1.5.",
    "Institute of Petroleum. Model Code of Safe Practice in the Petroleum Industry (1990). "
    "Part 15. Area Classification Code for Petroleum Installations.",
    "HS (G) 50. Health and Safety Executive Booklet. The Storage of Flammable Liquids in "
    "Fixed Tanks (up to 10 000 m³ total capacity) (1996).",
    "The Dangerous Substances (conveyance by road in road tankers and tank containers) "
    "Regulations 1981. HMSO (SI 1981/1059).",
    "EH 40. Guidance Note from the Health and Safety Executive, Occupational Exposure "
    "Limits. (Regularly updated.)",
]


def note_terms(lang):
    if lang == "vi":
        return ("<b>Thuật ngữ chương 3.</b> phân loại khu vực · nguồn nguy hiểm · nguồn phát "
                "thải · phát thải đồng thời · phương pháp tổng quát · phương pháp nguồn nguy "
                "hiểm · Vùng 0 / Vùng 1 / Vùng 2 · bầu khí quyển nổ · thông gió tự nhiên · "
                "thông gió hạn chế · điểm cháy · điểm sôi · giới hạn nổ dưới (LEL) · tỷ trọng "
                "tương đối · sương mù chất lỏng · gioăng CAF · gioăng gia cố xoắn ốc · vòng "
                "đệm O · mối nối ép (olive) · bể chứa (bund) · van xả áp · đĩa vỡ · mương/rãnh "
                "hở · phễu hứng · điểm lấy mẫu · BS 5345 phần 2 · RoSPA/ICI · Institute of "
                "Petroleum · HS(G)50 · EH 40")
    return ("<b>Key terms in Chapter 3.</b> area classification · source of hazard · "
            "source of release · simultaneous release · generalized method · source-of-hazard "
            "method · Zones 0, 1 and 2 · explosive atmosphere · freely ventilated · "
            "restricted ventilation · flashpoint · boiling point · lower explosive limit "
            "(LEL) · relative density · mist · CAF gasket · spirally supported gasket · "
            "'O' ring · compression (olive) joint · bund · pressure relief valve · bursting "
            "disc · open drain · tundish · sampling point · BS 5345 Part 2 · RoSPA/ICI · "
            "Institute of Petroleum · HS(G)50 · EH 40")


def _source_note(lang):
    if lang == "vi":
        return ("<b>Đặc điểm của nguyên bản.</b> Chương gồm 44 trang in (43–86; in = PDF − 21). "
                "Tám trang PDF 80–87 (trang in 59–66) là các trang chữ <i>MISSING PAGE</i> "
                "ngay trong tệp PDF được cung cấp: phần cuối của 3.3.3, toàn bộ 3.3.4, phần "
                "lớn 3.3.5, các hình 3.6–3.8 và các bảng 3.5–3.10 không thể khôi phục. "
                "Bản dịch đánh dấu khoảng trống đó và không bịa thêm nội dung. Mười sáu hình "
                "còn lại được vẽ lại dạng vector theo đúng chú thích in; bốn bảng còn lại "
                "được chép lại kèm số liệu gốc. Một số lỗi OCR và lỗi in được giữ nguyên và "
                "ghi chú: 'value stems' trong chú thích Hình 3.16 (ý là valve stems), lời "
                "dẫn đến 'các mục 3.5.1 và 3.5.2' (không tồn tại), tiêu đề trang in '40' "
                "thực chất là trang 48, và chú thích Hình 3.11 ghi C = 7 m trong khi văn bản "
                "nói 10 m (3 m + 7 m). Đơn vị áp suất N/m² và tốc độ gió m/sec được giữ như "
                "trong nguyên bản.")
    return ("<b>Source quirks.</b> The chapter spans 44 printed pages (43-86; printed = "
            "PDF - 21). Eight PDF pages 80-87 (printed 59-66) are literal <i>MISSING PAGE</i> "
            "placeholders in the supplied PDF: the tail of 3.3.3, all of 3.3.4, most of 3.3.5, "
            "Figures 3.6-3.8 and Tables 3.5-3.10 cannot be recovered. The translation flags "
            "the gap and invents no material. The sixteen surviving figures are redrawn as "
            "vectors under their printed captions, and the four surviving tables retain the "
            "printed values. Some OCR and printed quirks are retained and flagged: \"value "
            "stems\" in the Fig. 3.16 note (meaning valve stems), the cross-reference to "
            "\"sections 3.5.1 and 3.5.2\" (which do not exist), the printed header \"40\" that "
            "is actually page 48, and the Fig. 3.11 caption giving C = 7 m where the text "
            "says 10 m (3 m + 7 m). Pressure in N/m² and wind speed in m/sec follow the source.")


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
