# -*- coding: utf-8 -*-
"""Section 14.4.6-14.4.10 — Cast Steel Flange Standards for PN 100, 160, 250, 320, 400."""
from cvh14_common import T, H, P, LEAD, B, N, TB

# ---------------------------------------------------------------------------
# 14.4.6 - 14.4.10 — Cast Steel Flange Standards, PN classes 100/160/250/
# 320/400.  Printed column order:
#   DN | Outside Diameter | Thickness | Bolt Circle Diameter |
#   Number of Bolts | Threads | Bolt Hole Diameter
# ("Flange Bolting" is the super-heading spanning the six right-hand columns;
# it is carried by the table captions.  All dimensions in mm.)
#
# Table DATA is language-neutral and shared verbatim between EN and VI.
# ---------------------------------------------------------------------------

_FLANGE_HDR_VI = [
    "DN",
    "Đường kính ngoài",
    "Chiều dày",
    "Đường kính vòng bulông",
    "Số bulông",
    "Ren",
    "Đường kính lỗ bulông",
]
_FLANGE_HDR_EN = [
    "DN",
    "Outside Diameter",
    "Thickness",
    "Bolt Circle Diameter",
    "Number of Bolts",
    "Threads",
    "Bolt Hole Diameter",
]

# 14.4.6 PN 100 — DN 10 to DN 350 (15 rows).
_PN100_ROWS = [
    ("10",  "100", "20", "70",  "4",  "M12", "14"),
    ("15",  "105", "20", "75",  "4",  "M12", "14"),
    ("25",  "140", "24", "100", "4",  "M16", "18"),
    ("32",  "155", "24", "110", "4",  "M20", "22"),
    ("40",  "170", "28", "125", "4",  "M20", "22"),
    ("50",  "195", "30", "145", "4",  "M24", "26"),
    ("65",  "220", "34", "170", "8",  "M24", "26"),
    ("80",  "230", "36", "180", "8",  "M24", "26"),
    ("100", "265", "40", "210", "8",  "M27", "30"),
    ("125", "315", "40", "250", "8",  "M30", "33"),
    ("150", "355", "44", "290", "12", "M30", "33"),
    ("200", "430", "52", "360", "12", "M33", "36"),
    ("250", "505", "60", "430", "12", "M36", "39"),
    ("300", "585", "68", "500", "16", "M39", "42"),
    ("350", "655", "74", "560", "16", "M45", "48"),
]

# 14.4.7 PN 160 — DN 10 to DN 300 (13 rows).
_PN160_ROWS = [
    ("10",  "100", "20", "70",  "4",  "M12", "14"),
    ("15",  "105", "20", "75",  "4",  "M12", "14"),
    ("25",  "140", "24", "100", "4",  "M16", "18"),
    ("40",  "170", "28", "125", "4",  "M20", "22"),
    ("50",  "195", "30", "145", "4",  "M24", "26"),
    ("65",  "220", "34", "170", "8",  "M24", "26"),
    ("80",  "230", "36", "180", "8",  "M24", "26"),
    ("100", "265", "40", "210", "8",  "M27", "30"),
    ("125", "315", "44", "250", "8",  "M30", "33"),
    ("150", "355", "50", "290", "12", "M30", "33"),
    ("200", "430", "60", "360", "12", "M33", "36"),
    ("250", "515", "68", "430", "12", "M39", "42"),
    ("300", "585", "78", "500", "16", "M39", "42"),
]

# 14.4.8 PN 250 — DN 10 to DN 300 (13 rows).
_PN250_ROWS = [
    ("10",  "125", "24", "85",  "4",  "M16", "18"),
    ("15",  "130", "26", "90",  "4",  "M16", "18"),
    ("25",  "150", "28", "105", "4",  "M20", "22"),
    ("40",  "185", "34", "135", "4",  "M24", "26"),
    ("50",  "200", "38", "150", "8",  "M24", "26"),
    ("65",  "230", "42", "180", "8",  "M24", "26"),
    ("80",  "255", "46", "200", "8",  "M27", "30"),
    ("100", "300", "54", "235", "8",  "M30", "33"),
    ("125", "340", "60", "275", "12", "M30", "33"),
    ("150", "390", "68", "320", "12", "M33", "36"),
    ("200", "485", "82", "400", "12", "M39", "42"),
    ("250", "585", "100", "490", "16", "M45", "48"),
    ("300", "690", "120", "590", "16", "M48", "52"),
]

# 14.4.9 PN 320 — DN 10 to DN 250 (12 rows).
_PN320_ROWS = [
    ("10",  "125", "24", "85",  "4",  "M16", "18"),
    ("15",  "130", "26", "90",  "4",  "M16", "18"),
    ("25",  "160", "34", "115", "4",  "M20", "22"),
    ("40",  "195", "38", "145", "4",  "M24", "26"),
    ("50",  "210", "42", "160", "8",  "M24", "26"),
    ("65",  "255", "51", "200", "8",  "M27", "30"),
    ("80",  "275", "55", "220", "8",  "M27", "30"),
    ("100", "335", "65", "265", "8",  "M33", "36"),
    ("125", "380", "75", "310", "12", "M33", "36"),
    ("150", "425", "84", "350", "12", "M36", "39"),
    ("200", "525", "103", "440", "16", "M39", "42"),
    ("250", "640", "125", "540", "16", "M48", "52"),
]

# 14.4.10 PN 400 — DN 10 to DN 200 (11 rows).
_PN400_ROWS = [
    ("10",  "125", "28", "85",  "4",  "M16", "18"),
    ("15",  "145", "30", "100", "4",  "M20", "22"),
    ("25",  "180", "38", "130", "4",  "M24", "26"),
    ("40",  "220", "48", "165", "4",  "M27", "30"),
    ("50",  "235", "52", "180", "8",  "M27", "30"),
    ("65",  "290", "64", "225", "8",  "M30", "33"),
    ("80",  "305", "68", "240", "8",  "M30", "33"),
    ("100", "370", "80", "295", "8",  "M36", "39"),
    ("125", "415", "92", "340", "12", "M36", "39"),
    ("150", "475", "105", "390", "12", "M39", "42"),
    ("200", "585", "130", "490", "16", "M45", "48"),
]

_NOTE_VI = "Tất cả kích thước được cho tính bằng mm."
_NOTE_EN = "All dimensions are given in mm."


def section(lang):
    b = []

    # ---- 14.4.6 ----------------------------------------------------------
    b.append(H("14.4.6 Tiêu chuẩn mặt bích thép đúc cho PN 100",
               "14.4.6 Cast Steel Flange Standard for PN 100", lang, lvl=3))
    b.append(P(_NOTE_VI, _NOTE_EN, lang))
    b.append(TB(_FLANGE_HDR_VI, _FLANGE_HDR_EN, _PN100_ROWS, lang,
                cap_vi="Bảng 14.4.6 — Tiêu chuẩn mặt bích thép đúc PN 100 "
                       "(thông số bulông mặt bích).",
                cap_en="Table 14.4.6 — Cast steel flange standard for PN 100 "
                       "(flange bolting dimensions)."))

    # ---- 14.4.7 ----------------------------------------------------------
    b.append(H("14.4.7 Tiêu chuẩn mặt bích thép đúc cho PN 160",
               "14.4.7 Cast Steel Flange Standard for PN 160", lang, lvl=3))
    b.append(P(_NOTE_VI, _NOTE_EN, lang))
    b.append(TB(_FLANGE_HDR_VI, _FLANGE_HDR_EN, _PN160_ROWS, lang,
                cap_vi="Bảng 14.4.7 — Tiêu chuẩn mặt bích thép đúc PN 160 "
                       "(thông số bulông mặt bích).",
                cap_en="Table 14.4.7 — Cast steel flange standard for PN 160 "
                       "(flange bolting dimensions)."))

    # ---- 14.4.8 ----------------------------------------------------------
    b.append(H("14.4.8 Tiêu chuẩn mặt bích thép đúc cho PN 250",
               "14.4.8 Cast Steel Flange Standard for PN 250", lang, lvl=3))
    b.append(P(_NOTE_VI, _NOTE_EN, lang))
    b.append(TB(_FLANGE_HDR_VI, _FLANGE_HDR_EN, _PN250_ROWS, lang,
                cap_vi="Bảng 14.4.8 — Tiêu chuẩn mặt bích thép đúc PN 250 "
                       "(thông số bulông mặt bích).",
                cap_en="Table 14.4.8 — Cast steel flange standard for PN 250 "
                       "(flange bolting dimensions)."))

    # ---- 14.4.9 ----------------------------------------------------------
    b.append(H("14.4.9 Tiêu chuẩn mặt bích thép đúc cho PN 320",
               "14.4.9 Cast Steel Flange Standard for PN 320", lang, lvl=3))
    b.append(P(_NOTE_VI, _NOTE_EN, lang))
    b.append(TB(_FLANGE_HDR_VI, _FLANGE_HDR_EN, _PN320_ROWS, lang,
                cap_vi="Bảng 14.4.9 — Tiêu chuẩn mặt bích thép đúc PN 320 "
                       "(thông số bulông mặt bích).",
                cap_en="Table 14.4.9 — Cast steel flange standard for PN 320 "
                       "(flange bolting dimensions)."))

    # ---- 14.4.10 ---------------------------------------------------------
    b.append(H("14.4.10 Tiêu chuẩn mặt bích thép đúc cho PN 400",
               "14.4.10 Cast Steel Flange Standard for PN 400", lang, lvl=3))
    b.append(P(_NOTE_VI, _NOTE_EN, lang))
    b.append(TB(_FLANGE_HDR_VI, _FLANGE_HDR_EN, _PN400_ROWS, lang,
                cap_vi="Bảng 14.4.10 — Tiêu chuẩn mặt bích thép đúc PN 400 "
                       "(thông số bulông mặt bích).",
                cap_en="Table 14.4.10 — Cast steel flange standard for PN 400 "
                       "(flange bolting dimensions)."))

    return "".join(b)
