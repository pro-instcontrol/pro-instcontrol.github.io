# -*- coding: utf-8 -*-
"""Chapter 11 — Apparatus using protection concept pressurization 'p'.

Unofficial bilingual study reader of Alan McMillan, *Electrical Installations
in Hazardous Areas* (Butterworth-Heinemann, 1998), printed pp. 275-296
(PDF pp. 296-317). The chapter contains eight printed figures, two printed
tables, ten references, no numbered equations and no worked examples.

Prose is assembled from five sequential source-order modules W1-W5. The shell
owns the chapter h2, the ten printed references, the glossary, the source-quirk
note and the copyright line.
"""
from mcmillan_common import h2, note, p, refs

import mcmillan_ch11a as _a
import mcmillan_ch11b as _b
import mcmillan_ch11c as _c
import mcmillan_ch11d as _d
import mcmillan_ch11e as _e

PAGES_SRC = 22
BYLINE = "Alan McMillan · Electrical Installations in Hazardous Areas (Butterworth-Heinemann, 1998)"
TITLE_EN = "Apparatus using protection concept pressurization 'p'"
TITLE_VI = "Thiết bị theo nguyên lý tạo áp 'p'"

_SECTIONS = (_a, _b, _c, _d, _e)

_REFS = [
    "CP 1003 — Electrical Apparatus and Associated Equipment for use in Explosive Atmospheres "
    "of Gas or Vapour Other Than Mining operations. Part 2 (1966). Methods of Meeting the "
    "Explosion Hazard Other Than by the Use of Flameproof and Intrinsically Safe Equipment.",
    "NEC 70 (1990) — National Electrical Code (USA). Article 500, hazardous (Classified) Locations.",
    "76/117/EEC (1975) — Council Directive on the Approximation of the Laws of Member States "
    "Concerning Electrical Equipment for Use in Potentially Explosive Atmospheres. December.",
    "CENELEC — Centre Européen de Normalisation Électrique.",
    "BS 5501 — Electrical Apparatus for Potentially Explosive Atmospheres. Part 3 (1977). "
    "Pressurized Apparatus 'p'.",
    "BS/EN 50016 (1996) — Electrical Apparatus for Potentially Explosive Atmospheres. "
    "Pressurized Apparatus 'p'.",
    "BS/EN 50014 (1993) — Electrical Apparatus for Potentially Explosive Atmospheres. "
    "General Requirements.",
    "BS/EN 60529 (1991) — Specification for Degrees of Protection Provided by Enclosures "
    "(IP Code).",
    "BS 4999 — General Requirements for Rotating Electrical Machines. Part 105 (1988). "
    "Specification for Degrees of Protection Provided by Enclosures for rotating Machinery.",
    "EN 954 — Safety of Machinery – Safety Related Parts of Control Systems (in Preparation).",
]


def note_terms(lang):
    if lang == "vi":
        return ("<b>Thuật ngữ chính của chương.</b> nguyên lý tạo áp 'p' · áp suất bảo vệ · "
                "áp suất dương · làm sạch (purge) · pha loãng · khí bảo vệ · không khí · khí trơ · "
                "buồng kín · ống dẫn · cửa/ nắp · còi báo và khóa liên động · ngắt nguồn điện · "
                "vùng nguy hiểm · Vùng 0/1/2 · thiết bị đánh lửa · tia lửa và hạt nóng · "
                "bộ bắt tia lửa · labyrinth · len thép · BS/EN 50016 · BS/EN 50014 · "
                "BS/EN 60529 · EN 954")
    return ("<b>Key terms in Chapter 11.</b> pressurization 'p' · protective pressure · "
            "positive pressure · purge · dilution · protective gas · air · inert gas · "
            "enclosure · ducting · door or cover · pressure switch and interlock · "
            "disconnection of electrical supplies · hazardous area · Zone 0/1/2 · "
            "ignition-capable apparatus · incandescent sparks and particles · spark and "
            "particle barrier · labyrinth · steel wool · BS/EN 50016 · BS/EN 50014 · "
            "BS/EN 60529 · EN 954")


def _source_note(lang):
    if lang == "vi":
        return ("<b>Đặc điểm của nguyên bản.</b> Chương gồm 22 trang in (275-296; in = PDF − 21), "
                "không có trang <i>MISSING PAGE</i> nào, và gồm 8 hình (11.1-11.8), 2 bảng "
                "(11.1-11.2), 10 tài liệu tham khảo, không phương trình được đánh số cũng không "
                "ví dụ tính toán. Mọi nhãn hình, ô bảng, áp suất, thời gian, ký hiệu tiêu chuẩn "
                "và năm được đối chiếu từ trang render vì lớp văn bản PDF bị xáo trộn (ví dụ "
                "'17.2.7', '610 per cent', 'chromotographs', 'BS/EN 500147' và 'BSEN 5001 6'). "
                "Nhiều chi tiết in được giữ nguyên kèm ghi chú, gồm tiêu đề ghi 'BS/EN 50016 "
                "(1995)' nhưng thân bài ghi '(1996)⁶', cụm 'as described in Chapter 11' ngay "
                "trong Chương 11, 'per cent' và '%' dùng lẫn lộn, dấu phẩy trong 'made,?', "
                "'gasflow' viết liền, và dấu ngoặc đơn cuối trong 'worn BSEN 50026)'. Không lỗi "
                "in nào được sửa lặng lẽ.")
    return ("<b>Source quirks.</b> The chapter spans 22 printed pages (275-296; printed = "
            "PDF − 21), contains no <i>MISSING PAGE</i> placeholders, and has 8 figures "
            "(11.1-11.8), 2 tables (11.1-11.2), 10 references, no numbered equations and no "
            "worked examples. Every figure label, table cell, pressure, time, standard "
            "designation and date was checked against the page renders because the PDF text "
            "layer is garbled (for example '17.2.7', '610 per cent', 'chromotographs', "
            "'BS/EN 500147' and 'BSEN 5001 6'). Several printed details are retained with "
            "notes: the title's 'BS/EN 50016 (1995)' against the body's '(1996)⁶', the "
            "self-referential 'as described in Chapter 11' inside Chapter 11, mixed 'per cent' "
            "and '%', the comma in 'made,?', the compound 'gasflow', and the unclosed "
            "parenthesis in 'worn BSEN 50026)'. No printed error is silently corrected.")


def body_vi():
    b = [h2("11 — Thiết bị theo nguyên lý tạo áp 'p'",
            "11 — Apparatus using protection concept pressurization 'p'")]
    for m in _SECTIONS:
        b.append(m.body_vi())
    b.append(refs(_REFS))
    b.append(note(_source_note("vi")))
    b.append(p("<i>Đây là bản dịch không chính thức để học tập. Nội dung gốc © 1998 Reed "
               "Educational and Professional Publishing Ltd.</i>"))
    return "".join(b)


def body_en():
    b = [h2("11 — Apparatus using protection concept pressurization 'p'",
            "11 — Apparatus using protection concept pressurization 'p'")]
    for m in _SECTIONS:
        b.append(m.body_en())
    b.append(refs(_REFS))
    b.append(note(_source_note("en")))
    b.append(p("<i>This is an unofficial translation for study purposes. Original content "
               "© 1998 Reed Educational and Professional Publishing Ltd.</i>"))
    return "".join(b)
