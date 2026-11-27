# -*- coding: utf-8 -*-
"""Chapter 7 — Design philosophy for electrical apparatus for explosive atmospheres.

Unofficial bilingual study reader of Alan McMillan, *Electrical Installations
in Hazardous Areas* (Butterworth-Heinemann, 1998), printed pp. 164-177
(PDF pp. 185-198).  This is a pure prose chapter: no printed figures, tables,
numbered equations or worked examples.  The seven printed references are
appended by this shell after five sequential source-order prose modules.
"""
from mcmillan_common import note, p, refs

import mcmillan_ch07a as _a
import mcmillan_ch07b as _b
import mcmillan_ch07c as _c
import mcmillan_ch07d as _d
import mcmillan_ch07e as _e

PAGES_SRC = 14
BYLINE = "Alan McMillan · Electrical Installations in Hazardous Areas (Butterworth-Heinemann, 1998)"
TITLE_EN = "Design philosophy for electrical apparatus for explosive atmospheres"
TITLE_VI = "Triết lý thiết kế thiết bị điện dùng trong khí quyển nổ"

_SECTIONS = (_a, _b, _c, _d, _e)

_REFS = [
    "BS 4137 (1967) Guide to the Selection of Electrical Equipment for use in "
    "Division 2 Areas.",
    "76/117/EEC Council Directive of 18 December 1975 (on the approximation of "
    "the laws of Member States concerning electrical equipment for use in "
    "Potentially Explosive Atmospheres)",
    "BS 6467 Electrical Apparatus with Protection by Enclosure for Use in the "
    "Presence of Combustible Dusts. Part 2 (1985) Guide to Selection, "
    "Installation and Maintenance.",
    "RoSPA/ICI Engineering Codes and Regulations, Electrical Installations in "
    "Flammable Atmospheres (1973). Group C (Electrical), Volume 1.5.",
    "94/9/EC Directive of the European Parliament and Council of 23 March 1994 "
    "(on the approximation of the laws of Member States concerning equipment "
    "and protective systems intended for use in Potentially Explosive "
    "Atmospheres)",
    "BS 4683 Electrical Apparatus for Explosive Atmospheres Part 3 (1972). "
    "Type of Protection N.",
    "Official Journal of the European Communities.",
]


def note_terms(lang):
    if lang == "vi":
        return ("<b>Thuật ngữ chương 7.</b> thiết bị bảo vệ chống nổ · bầu khí quyển nổ · "
                "rủi ro tồn dư · khái niệm bảo vệ / loại hình bảo vệ · loại trừ môi trường nổ · "
                "tia lửa có khả năng bắt lửa · quá nóng · dập tắt ngọn lửa · chứa ngăn vụ nổ · "
                "hạn chế năng lượng · ngâm trong dầu ‘o’ · bọc kín ‘m’ · cấp áp khí ‘p’ · an "
                "toàn tăng cường ‘e’ · vỏ chống nổ ‘d’ · lấp đầy bằng bột trơ ‘q’ · an toàn nội "
                "tại ‘i’ · ‘ia’ / ‘ib’ · bảo vệ đặc biệt ‘s’ · loại bảo vệ ‘n’ / ‘N’ · hài hòa "
                "hóa tiêu chuẩn · Chỉ thị EU · yêu cầu thiết yếu · tổ chức chứng nhận được thông "
                "báo · chứng nhận bên thứ ba · Dấu hiệu Cộng đồng đặc trưng · Thư không phản đối "
                "· hạn chế hô hấp · sự lắng đọng bụi · tính dẫn điện · bụi cháy được")
    return ("<b>Key terms in Chapter 7.</b> explosion-protected apparatus · explosive atmosphere "
            "· residual risk · protection concept / type of protection · exclusion of the "
            "explosive atmosphere · incendive spark · excessively hot · quenching · containment "
            "of explosions · energy limitation · oil immersion ‘o’ · encapsulation ‘m’ · "
            "pressurization ‘p’ · increased safety ‘e’ · flameproof enclosure ‘d’ · powder "
            "filling ‘q’ · intrinsic safety ‘i’ · ‘ia’ / ‘ib’ · special protection ‘s’ · type "
            "of protection ‘n’ / ‘N’ · harmonisation of Standards · EU Directive · essential "
            "requirements · notified certification body · third-party certification · "
            "Distinctive Community Mark · Letters of no Objection · restricted breathing · "
            "dust settling · conductivity · combustible dust")


def _source_note(lang):
    if lang == "vi":
        return ("<b>Đặc điểm của nguyên bản.</b> Chương gồm 14 trang in (164-177; in = "
                "PDF − 21), không có trang <i>MISSING PAGE</i> nào và là chương thuần văn "
                "bản: không hình, không bảng, không phương trình và không ví dụ tính toán; "
                "danh mục tham khảo gồm bảy mục trên trang in 177. Mọi ký hiệu bảo vệ, "
                "số tiêu chuẩn, năm, chú thích và dòng tham khảo được đối chiếu từ trang "
                "render vì lớp văn bản PDF bị xáo trộn (ví dụ ‘Id’ thành ‘d’, BS/EN5O "
                "thành BS/EN50, 1970'~~ thành 1970's⁴). Nhiều chi tiết in được giữ nguyên "
                "kèm ghi chú: quy tắc vàng in nghiêng; 'Selected Industrial Apparatus'; "
                "'1970's⁴' với dấu chú thích sau chữ s; 'IEC 79/15' và 'IEC 79–15'; 'IEC "
                "1241 – 1'; 'European Journal⁷' so với tiêu đề mục 7; 'BS 7535' (in nhầm "
                "thành BS 7353); 'BS 5501, Part 2 (1997)' (các phần khác là 1977); tham "
                "chiếu sai 'Section 7.4.1'; 'third editions of These standards'; 'These "
                "was, however, a good reason'; cách viết CENELEC không dấu; và mâu thuẫn "
                "giữa BS 6467 Part 2 (1985) ở đây với (1988) ở Chương 6. Không lỗi in nào "
                "được sửa lặng lẽ.")
    return ("<b>Source quirks.</b> The chapter spans 14 printed pages (164-177; printed = "
            "PDF − 21), contains no <i>MISSING PAGE</i> placeholders and is pure prose: "
            "no figures, tables, equations or worked examples; the seven printed references "
            "are on printed p.177. Every protection symbol, standard number, date, footnote "
            "marker and reference entry was checked against the page renders because the "
            "PDF text layer is garbled (for example ‘Id’ for ‘d’, BS/EN5O for BS/EN50, "
            "and 1970'~~ for 1970's⁴). Several printed details are retained with notes: "
            "the italic golden rule; \"Selected Industrial Apparatus\"; \"1970's⁴\" with "
            "the marker after the s; IEC 79/15 versus IEC 79–15; IEC 1241 – 1; "
            "\"European Journal⁷\" against reference 7's title; \"BS 7535\" where BS 7353 "
            "is intended; \"BS 5501, Part 2 (1997)\" where the other parts are 1977; the "
            "wrong cross-reference \"Section 7.4.1\"; \"third editions of These "
            "standards\"; \"These was, however, a good reason\"; the unaccented CENELEC "
            "expansion; and BS 6467 Part 2 (1985) here against (1988) in Chapter 6. No "
            "printed error is silently corrected.")


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
