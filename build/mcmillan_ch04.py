# -*- coding: utf-8 -*-
"""Chapter 4 - Calculation of release rates and the extents of hazardous areas.

Unofficial bilingual study reader of Alan McMillan, *Electrical Installations
in Hazardous Areas* (Butterworth-Heinemann, 1998), printed pp. 87-124
(PDF pp. 108-145). All six sections 4.1-4.6, six worked examples, three
vector figures and both printed tables are included; the ten-page Table 4.1
insert is assembled from four transcribed source-order modules.

Prose is assembled from five sequential source-order modules; figures are
redrawn in `mcmillanfig04_a.py`. Unlike Chapter 3, this source span contains
no MISSING PAGE placeholders.
"""
from mcmillan_common import note, p, refs, table

import mcmillan_ch04a as _a
import mcmillan_ch04b as _b
import mcmillan_ch04c as _c
import mcmillan_ch04d as _d
import mcmillan_ch04e as _e
import mcmillan_tbl41 as _T41

PAGES_SRC = 38
BYLINE = "Alan McMillan · Electrical Installations in Hazardous Areas (Butterworth-Heinemann, 1998)"
TITLE_EN = "Calculation of release rates and the extents of hazardous areas"
TITLE_VI = "Tính toán tốc độ thoát và phạm vi khu vực nguy hiểm"

_SECTIONS = (_b, _c, _d, _e)

_REFS = [
    "BS 5345. Selection, Installation and Maintenance of Electrical Apparatus for use in "
    "Potentially Explosive Atmospheres (other than mining applications or explosives "
    "processing or manufacture). Part 2 (1983). Classification of hazardous areas.",
    "RoSPA/ICI. Engineering Codes and Regulations, Electrical Installations in Flammable "
    "Atmospheres (1973). Group C (Electrical), Volume 1.5.",
    "BS/EN 60079-10. Electrical Apparatus for Explosive Atmospheres / Classification of "
    "hazardous areas (1996).",
    "Chemical Engineers Handbook (Editions 1-6). Latest edition. Edition 6 (1984), "
    "R. H. Perry and O. Green.",
    "BSI 79/27013. BSI Committee GEL/114/5 Draft Document produced in preparation of "
    "BS 5345.",
    "Lipincott, S. B. and Lyman, M. L. (1946). Vapour Pressure/Temperature Monographs. "
    "Industrial Engineering and Chemistry (38) 3.",
    "Chartered Institution of Building Services (1970). Natural Infiltration into "
    "Buildings (guide book).",
]


def note_terms(lang):
    if lang == "vi":
        return ("<b>Thuật ngữ chương 4.</b> tốc độ phát thải · lượng phát thải theo khối "
                "lượng · lỗ tiết/đầu phun · diện tích lỗ tiết · tỷ số nhiệt dung riêng · "
                "khối lượng phân tử · áp suất tuyệt đối · áp suất thượng lưu · tỷ số áp "
                "suất tới hạn · thể tích mol · giới hạn nổ dưới (LEL) · phạm vi khu vực "
                "nguy hiểm · phát thải trôi theo gió · tia phun · vật cản · ảnh hưởng của "
                "mặt đất · vũng chất lỏng · sự bay hơi · áp suất riêng phần · hệ số truyền "
                "khối · số Schmidt · số Reynolds · nhiệt ẩn hóa hơi · nhiệt dung riêng · "
                "bay hơi đột thời (flash) · sương mù chất lỏng · thông gió tốt · thông gió "
                "kém · số lần thay không khí mỗi giây · hiệu quả thông gió · thời gian tồn "
                "lưu · Vùng 0 / Vùng 1 / Vùng 2 · cấp nhiệt độ · nhóm thiết bị · BS 5345 · "
                "BS/EN 60079-10")
    return ("<b>Key terms in Chapter 4.</b> release rate · mass release · orifice/nozzle · "
            "orifice area · ratio of specific heats · molecular weight · absolute pressure · "
            "upstream pressure · critical pressure ratio · molar volume · lower explosive "
            "limit (LEL) · hazardous area extent · drift release · jet · obstruction · ground "
            "proximity · pool · vaporization · partial pressure · mass-transfer coefficient · "
            "Schmidt number · Reynolds number · latent heat · heat capacity · flashing-off · "
            "mist · well ventilated · poorly ventilated · air changes per second · "
            "ventilation effectiveness · persistence time · Zones 0, 1 and 2 · temperature "
            "class · apparatus group · BS 5345 · BS/EN 60079-10")


def _source_note(lang):
    if lang == "vi":
        return ("<b>Đặc điểm của nguyên bản.</b> Chương gồm 38 trang in (87–124; "
                "in = PDF − 21) và, khác với Chương 3, không có trang <i>MISSING PAGE</i> "
                "nào. Bảng 4.1 là phần chèn mười trang (trang in 90–99) với 196 dòng "
                "vật liệu dễ cháy, được chép lại từ các trang render vì lớp văn bản PDF "
                "xáo trộn cả mười bốn cột. Ba hình được vẽ lại theo chú thích in. Nhiều "
                "chi tiết in được giữ nguyên kèm ghi chú: Phương trình 4.22 bị bỏ qua "
                "trong dãy số (4.21 → 4.23); các Hình 4.4 và 4.5 không bao giờ được in "
                "dù phần kết luận trích dẫn “Fig. 4.5 from BS 5345 Part 2”; mục 4.5 "
                "trích dẫn “Bảng 4.1” như một bảng thông gió không tồn tại; tiêu đề "
                "4.5.1 in nhầm BS/EN 10079-10 (nguyên bản ở nơi khác ghi 60079-10 và "
                "6079-10). Chú thích Hình 4.1 là chuẩn xác, còn văn bản in trên trang "
                "102 đảo ngược đường cong 2 và 3. Các con số không nhất quán trong sáu "
                "ví dụ, cách gom số mũ mờ của Phương trình 4.3 và 4.31, cùng các lỗi "
                "OCR như <i>kg/s⁴</i> (dấu chú thích 4, không phải số mũ) đều được ghi "
                "nhận rõ ràng chứ không sửa lặng lẽ.")
    return ("<b>Source quirks.</b> The chapter spans 38 printed pages (87-124; printed = "
            "PDF - 21) and, unlike Chapter 3, contains no <i>MISSING PAGE</i> "
            "placeholders. Table 4.1 is a ten-page insert (printed pp. 90-99) with 196 "
            "material rows; it was transcribed from the page renders because the PDF text "
            "layer scrambles all fourteen columns. The three figures are redrawn under "
            "their printed captions. Several printed details are retained with notes: "
            "Equation 4.22 is skipped in the sequence (4.21 to 4.23); Figures 4.4 and 4.5 "
            "are never printed although the conclusion cites \"Fig. 4.5 from BS 5345 Part "
            "2\"; Section 4.5 cites \"Table 4.1\" as a ventilation table that does not "
            "exist; the 4.5.1 heading prints BS/EN 10079-10 (elsewhere the source gives "
            "60079-10 and 6079-10). The printed legend in Fig. 4.1 is authoritative, while "
            "the prose on printed p.102 swaps curves 2 and 3. Internal numerical "
            "inconsistencies in the six worked examples, ambiguous exponent grouping in "
            "Eqs. 4.3 and 4.31, and OCR traps such as <i>kg/s⁴</i> (a footnote marker, not "
            "a power) are all flagged rather than silently corrected.")


def body_vi():
    b = [_a.body_vi()]
    b.append(table(_T41.HEAD_VI, _T41.ROWS,
                   _T41.CAPTION_VI + "<br>" + _T41.FOOTNOTES_VI))
    for m in _SECTIONS:
        b.append(m.body_vi())
    b.append(refs(_REFS))
    b.append(note(_source_note("vi")))
    b.append(p("<i>Đây là bản dịch không chính thức để học tập. Nội dung gốc © 1998 Reed "
               "Educational and Professional Publishing Ltd.</i>"))
    return "".join(b)


def body_en():
    b = [_a.body_en()]
    b.append(table(_T41.HEAD_EN, _T41.ROWS,
                   _T41.CAPTION_EN + "<br>" + _T41.FOOTNOTES_EN))
    for m in _SECTIONS:
        b.append(m.body_en())
    b.append(refs(_REFS))
    b.append(note(_source_note("en")))
    b.append(p("<i>This is an unofficial translation for study purposes. Original content "
               "© 1998 Reed Educational and Professional Publishing Ltd.</i>"))
    return "".join(b)
