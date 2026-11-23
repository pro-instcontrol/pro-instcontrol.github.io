# -*- coding: utf-8 -*-
"""Section 14.3 — American Pipe Flange Dimensions."""
from cvh14_common import T, H, P, LEAD, B, N, TB

# ---------------------------------------------------------------------------
# 14.3.1 — Diameter of Bolt Circles (inches, ASME B16.1 / B16.5 / B16.24)
# Columns: Nominal Pipe Size | Class 125(CI)/150(STL) | Class 250(CI)/300(STL)
#          | Class 600 | Class 900 | Class 1500 | Class 2500
# NPS strings in this subsection use the ASCII hyphen (1-1/4).
_BOLT_CIRCLE_ROWS = [
    ("1",     "3.12",  "3.50",  "3.50",  "4.00",  "4.00",  "4.25"),
    ("1-1/4", "3.50",  "3.88",  "3.88",  "4.38",  "4.38",  "5.12"),
    ("1-1/2", "3.88",  "4.50",  "4.50",  "4.88",  "4.88",  "5.75"),
    ("2",     "4.75",  "5.00",  "5.00",  "6.50",  "6.50",  "6.75"),
    ("2-1/2", "5.50",  "5.88",  "5.88",  "7.50",  "7.50",  "7.75"),
    ("3",     "6.00",  "6.62",  "6.62",  "7.50",  "8.00",  "9.00"),
    ("4",     "7.50",  "7.88",  "8.50",  "9.25",  "9.50",  "10.75"),
    ("5",     "8.50",  "9.25",  "10.50", "11.00", "11.50", "12.75"),
    ("6",     "9.50",  "10.62", "11.50", "12.50", "12.50", "14.50"),
    ("8",     "11.75", "13.00", "13.75", "15.50", "15.50", "17.25"),
    ("10",    "14.25", "15.25", "17.00", "18.50", "19.00", "21.75"),
    ("12",    "17.00", "17.75", "19.25", "21.00", "22.50", "24.38"),
    ("14",    "18.75", "20.25", "20.75", "22.00", "25.00", "- - -"),
    ("16",    "21.25", "22.50", "23.75", "24.25", "27.75", "- - -"),
    ("18",    "22.75", "24.75", "25.75", "27.00", "30.50", "- - -"),
    ("20",    "25.00", "27.00", "28.50", "29.50", "32.75", "- - -"),
    ("24",    "29.50", "32.00", "33.00", "35.50", "39.00", "- - -"),
    ("30",    "36.00", "39.25", "- - -", "- - -", "- - -", "- - -"),
    ("36",    "42.75", "46.00", "- - -", "- - -", "- - -", "- - -"),
    ("42",    "49.50", "52.75", "- - -", "- - -", "- - -", "- - -"),
    ("48",    "56.00", "60.75", "- - -", "- - -", "- - -", "- - -"),
]

_BOLT_HDR_VI = [
    "Kích thước ống danh nghĩa",
    "Class(1) 125 (Gang đúc)(2) hoặc Class 150 (Thép)",
    "Class(3) 250 (Gang đúc)(2) hoặc Class 300 (Thép)",
    "Class 600", "Class 900", "Class 1500", "Class 2500",
]
_BOLT_HDR_EN = [
    "Nominal Pipe Size",
    "Class(1) 125 (Cast Iron)(2) or Class 150 (Steel)",
    "Class(3) 250 (Cast Iron)(2) or Class 300 (Steel)",
    "Class 600", "Class 900", "Class 1500", "Class 2500",
]
_BOLT_NOTES_VI = [
    "1. Kích thước ống danh nghĩa từ 1 đến 12 cũng áp dụng cho mặt bích hợp kim đồng đúc Class 150.",
    "2. Các đường kính này áp dụng cho van thép với kích thước ống danh nghĩa từ 1 đến 24.",
    "3. Kích thước ống danh nghĩa từ 1 đến 8 cũng áp dụng cho mặt bích hợp kim đồng đúc Class 300.",
]
_BOLT_NOTES_EN = [
    "1. Nominal pipe sizes 1 through 12 also apply to Class 150 cast copper alloy flanges.",
    "2. These diameters apply to steel valves for nominal pipe sizes 1 through 24.",
    "3. Nominal pipe sizes 1 thorough 8 also apply to Class 300 cast copper alloy flanges.",
]

# ---------------------------------------------------------------------------
# 14.3.2 — Number of Stud Bolts and Diameter (inches, ASME B16.1/16.5/16.24)
# Each class contributes two columns: No. (count) then Dia. (diameter).
# NPS strings in this subsection use U+2212 MINUS SIGN (1−1/4).
_STUD_ROWS = [
    ("1",     "4", "0.50", "4", "0.62", "4", "0.62", "4", "0.88", "4", "0.88", "4", "0.88"),
    ("1−1/4", "4", "0.50", "4", "0.62", "4", "0.62", "4", "0.88", "4", "0.88", "4", "1.00"),
    ("1−1/2", "4", "0.50", "4", "0.75", "4", "0.75", "4", "1.00", "4", "1.00", "4", "1.12"),
    ("2",     "4", "0.62", "8", "0.62", "8", "0.62", "8", "0.88", "8", "0.88", "8", "1.00"),
    ("2−1/2", "4", "0.62", "8", "0.75", "8", "0.75", "8", "1.00", "8", "1.00", "8", "1.12"),
    ("3",     "4", "0.62", "8", "0.75", "8", "0.75", "8", "0.88", "8", "1.12", "8", "1.25"),
    ("4",     "8", "0.62", "8", "0.75", "8", "0.88", "8", "1.12", "8", "1.25", "8", "1.50"),
    ("5",     "8", "0.75", "8", "0.75", "8", "1.00", "8", "1.25", "8", "1.50", "8", "1.75"),
    ("6",     "8", "0.75", "12","0.75", "12","1.00", "12","1.12", "12","1.38", "8", "2.00"),
    ("8",     "8", "0.75", "12","0.88", "12","1.12", "12","1.38", "12","1.62", "12","2.00"),
    ("10",    "12","0.88", "16","1.00", "16","1.25", "16","1.38", "12","1.88", "12","2.50"),
    ("12",    "12","0.88", "16","1.12", "20","1.25", "20","1.38", "16","2.00", "12","2.75"),
    ("14",    "12","1.00", "20","1.12", "20","1.38", "20","1.50", "16","2.25", "- - -", "- - -"),
    ("16",    "16","1.00", "20","1.25", "20","1.50", "20","1.62", "16","2.50", "- - -", "- - -"),
    ("18",    "16","1.12", "24","1.25", "20","1.62", "20","1.88", "16","2.75", "- - -", "- - -"),
    ("20",    "20","1.12", "24","1.25", "24","1.62", "20","2.00", "16","3.00", "- - -", "- - -"),
    ("24",    "20","1.25", "24","1.50", "24","1.88", "20","2.50", "16","3.50", "- - -", "- - -"),
    ("30",    "28","1.25", "28","1.75", "- - -", "- - -", "- - -", "- - -", "- - -", "- - -", "- - -", "- - -"),
    ("36",    "32","1.50", "32","2.00", "- - -", "- - -", "- - -", "- - -", "- - -", "- - -", "- - -", "- - -"),
    ("42",    "36","1.50", "36","2.00", "- - -", "- - -", "- - -", "- - -", "- - -", "- - -", "- - -", "- - -"),
    ("48",    "44","1.50", "40","2.00", "- - -", "- - -", "- - -", "- - -", "- - -", "- - -", "- - -", "- - -"),
]

_STUD_HDR_VI = [
    "Kích thước ống danh nghĩa",
    "Class(1) 125 (Gang đúc)(2) hoặc Class 150 (Thép) — Số lượng",
    "Class(1) 125 (Gang đúc)(2) hoặc Class 150 (Thép) — Đường kính",
    "Class(3) 250 (Gang đúc)(2) hoặc Class 300 (Thép) — Số lượng",
    "Class(3) 250 (Gang đúc)(2) hoặc Class 300 (Thép) — Đường kính",
    "Class 600 — Số lượng", "Class 600 — Đường kính",
    "Class 900 — Số lượng", "Class 900 — Đường kính",
    "Class 1500 — Số lượng", "Class 1500 — Đường kính",
    "Class 2500 — Số lượng", "Class 2500 — Đường kính",
]
_STUD_HDR_EN = [
    "Nominal Pipe Size",
    "Class(1) 125 (Cast Iron)(2) or Class 150 (Steel) — No.",
    "Class(1) 125 (Cast Iron)(2) or Class 150 (Steel) — Dia.",
    "Class(3) 250 (Cast Iron)(2) or Class 300 (Steel) — No.",
    "Class(3) 250 (Cast Iron)(2) or Class 300 (Steel) — Dia.",
    "Class 600 — No.", "Class 600 — Dia.",
    "Class 900 — No.", "Class 900 — Dia.",
    "Class 1500 — No.", "Class 1500 — Dia.",
    "Class 2500 — No.", "Class 2500 — Dia.",
]
_STUD_NOTES_VI = [
    "1. Kích thước ống danh nghĩa từ 1 đến 12 cũng áp dụng cho mặt bích hợp kim đồng đúc Class 150.",
    "2. Các đường kính này áp dụng cho van thép với kích thước ống danh nghĩa từ 1 đến 24.",
    "3. Kích thước ống danh nghĩa từ 1 đến 8 cũng áp dụng cho mặt bích hợp kim đồng đúc Class 300.",
]
_STUD_NOTES_EN = [
    "1. Nominal pipe sizes 1 through 12 also apply to Class 150 cast copper alloy flanges.",
    "2. These diameters apply to steel valves for nominal pipe sizes 1 through 24.",
    "3. Nominal pipe sizes 1 through 8 also apply to Class 300 cast copper alloy flanges.",
]

# ---------------------------------------------------------------------------
# 14.3.3 — Flange Diameter (inches, ASME B16.1 / B16.5 / B16.24)
_FLANGE_DIA_ROWS = [
    ("1",     "4.25",  "4.88",  "4.88",  "5.88",  "5.88",  "6.25"),
    ("1−1/4", "4.62",  "5.25",  "5.25",  "6.25",  "6.25",  "7.25"),
    ("1−1/2", "5.00",  "6.12",  "6.12",  "7.00",  "7.00",  "8.00"),
    ("2",     "6.00",  "6.50",  "6.50",  "8.50",  "8.50",  "9.25"),
    ("2−1/2", "7.00",  "7.50",  "7.50",  "9.62",  "9.62",  "10.50"),
    ("3",     "7.50",  "8.25",  "8.25",  "9.50",  "10.50", "12.00"),
    ("4",     "9.00",  "10.00", "10.75", "11.50", "12.25", "14.00"),
    ("5",     "10.00", "11.00", "13.00", "13.75", "14.75", "16.50"),
    ("6",     "11.00", "12.50", "14.00", "15.00", "15.50", "19.00"),
    ("8",     "13.50", "15.00", "16.50", "18.50", "19.00", "21.75"),
    ("10",    "16.00", "17.50", "20.00", "21.50", "23.00", "26.50"),
    ("12",    "19.00", "20.50", "22.00", "24.00", "26.50", "30.00"),
    ("14",    "21.00", "23.00", "23.75", "25.25", "29.50", "- - -"),
    ("16",    "23.50", "25.50", "27.00", "27.75", "32.50", "- - -"),
    ("18",    "25.00", "28.00", "29.25", "31.00", "36.00", "- - -"),
    ("20",    "27.50", "30.50", "32.00", "33.75", "38.75", "- - -"),
    ("24",    "32.00", "36.00", "37.00", "41.00", "46.00", "- - -"),
    ("30",    "38.75", "43.00", "- - -", "- - -", "- - -", "- - -"),
    ("36",    "46.00", "50.00", "- - -", "- - -", "- - -", "- - -"),
    ("42",    "53.00", "57.00", "- - -", "- - -", "- - -", "- - -"),
    ("48",    "59.50", "65.00", "- - -", "- - -", "- - -", "- - -"),
]

_FLANGE_DIA_HDR_VI = [
    "Kích thước ống danh nghĩa",
    "Class(1) 125 (Gang đúc)(2) hoặc Class 150 (Thép)",
    "Class(3) 250 (Gang đúc)(2) hoặc Class 300 (Thép)",
    "Class 600", "Class 900", "Class 1500", "Class 2500",
]
_FLANGE_DIA_HDR_EN = [
    "Nominal Pipe Size",
    "Class(1) 125 (Cast Iron)(2) or Class 150 (Steel)",
    "Class(3) 250 (Cast Iron)(2) or Class 300 (Steel)",
    "Class 600", "Class 900", "Class 1500", "Class 2500",
]
_FLANGE_DIA_NOTES_VI = [
    "1. Kích thước ống danh nghĩa từ 1 đến 12 cũng áp dụng cho mặt bích hợp kim đồng đúc Class 150.",
    "2. Kích thước ống danh nghĩa từ 1 đến 8 cũng áp dụng cho mặt bích hợp kim đồng đúc Class 300.",
]
_FLANGE_DIA_NOTES_EN = [
    "1. Nominal pipe sizes 1 through 12 also apply to Class 150 cast copper alloy flanges.",
    "2. Nominal pipe sizes 1 through 8 also apply to Class 300 cast copper alloy flanges.",
]

# ---------------------------------------------------------------------------
# 14.3.4 — Flange Thickness for Flange Fittings (inches, ASME B16.1/16.5/16.24)
# The printed page stacks two sub-tables (each repeated on the continued page):
#   Part A: Class 150 / 250 / 300 -> size + 6 values (RF(2), RTJ, Cast Copper
#           Alloy; RF, RTJ, Cast Copper Alloy).
#   Part B: Class 600 / 900 / 1500 / 2500 -> size + 8 values (RF, RTJ per class).
# They are kept in ONE table with language-neutral class-label band rows.
_FLANGE_THICK_ROWS = [
    "Class 150 / Class 250 / Class 300",
    ("1",     "0.50", "0.75", "0.38", "0.62", "0.87", "0.59"),
    ("1−1/4", "0.56", "0.81", "0.41", "0.69", "0.94", "0.62"),
    ("1−1/2", "0.62", "0.87", "0.44", "0.75", "1.00", "0.69"),
    ("2",     "0.69", "0.94", "0.50", "0.81", "1.12", "0.75"),
    ("2−1/2", "0.81", "1.06", "0.56", "0.94", "1.25", "0.81"),
    ("3",     "0.88", "1.13", "0.62", "1.06", "1.37", "0.91"),
    ("4",     "0.88", "1.13", "0.69", "1.19", "1.50", "1.06"),
    ("5",     "0.88", "1.13", "0.75", "1.31", "1.62", "1.12"),
    ("6",     "0.94", "1.19", "0.81", "1.38", "1.69", "1.19"),
    ("8",     "1.06", "1.31", "0.94", "1.56", "1.87", "1.38"),
    ("10",    "1.12", "1.37", "1.00", "1.81", "2.12", "- - -"),
    ("12",    "1.19", "1.44", "1.06", "1.94", "2.25", "- - -"),
    ("14",    "1.31", "1.56", "- - -", "2.06", "2.37", "- - -"),
    ("16",    "1.38", "1.63", "- - -", "2.19", "2.50", "- - -"),
    ("18",    "1.50", "1.75", "- - -", "2.31", "2.62", "- - -"),
    ("20",    "1.62", "1.87", "- - -", "2.44", "2.82", "- - -"),
    ("24",    "1.81", "2.06", "- - -", "2.69", "3.13", "- - -"),
    "Class 600 / Class 900 / Class 1500 / Class 2500",
    ("1",     "0.69", "0.94", "1.12", "1.37", "1.12", "1.37", "1.38", "1.63"),
    ("1−1/4", "0.81", "1.06", "1.12", "1.37", "1.12", "1.37", "1.50", "1.81"),
    ("1−1/2", "0.88", "1.13", "1.25", "1.50", "1.25", "1.50", "1.75", "2.06"),
    ("2",     "1.00", "1.31", "1.50", "1.81", "1.50", "1.81", "2.00", "2.31"),
    ("2−1/2", "1.12", "1.43", "1.62", "1.93", "1.62", "1.93", "2.25", "2.62"),
    ("3",     "1.25", "1.56", "1.50", "1.81", "1.88", "2.43", "2.62", "3.00"),
    ("4",     "1.50", "1.81", "1.75", "2.06", "2.12", "2.43", "3.00", "3.44"),
    ("5",     "1.75", "2.06", "2.00", "2.31", "2.88", "3.19", "3.62", "4.12"),
    ("6",     "1.88", "2.19", "2.19", "2.50", "3.25", "3.62", "4.25", "4.75"),
    ("8",     "2.19", "2.50", "2.50", "2.81", "3.62", "4.06", "5.00", "5.56"),
    ("10",    "2.50", "2.81", "2.75", "3.06", "4.25", "4.69", "6.50", "7.19"),
    ("12",    "2.62", "2.93", "3.12", "3.43", "4.88", "5.44", "7.25", "7.94"),
    ("14",    "2.75", "3.06", "3.38", "3.82", "5.25", "5.88", "- - -", "- - -"),
    ("16",    "3.00", "3.31", "3.50", "3.94", "5.75", "6.44", "- - -", "- - -"),
    ("18",    "3.25", "3.56", "4.00", "4.50", "6.38", "7.07", "- - -", "- - -"),
    ("20",    "3.50", "3.88", "4.25", "4.75", "7.00", "7.69", "- - -", "- - -"),
    ("24",    "4.00", "4.44", "5.50", "6.12", "8.00", "8.81", "- - -", "- - -"),
]

_FLANGE_THICK_HDR_VI = [
    "Kích thước ống danh nghĩa",
    "Class 150 (CI) FF và STL — RF(2)",
    "Class 150 (CI) FF và STL — RTJ",
    "Class 150 STL — Hợp kim đồng đúc",
    "Class 250 (CI) và Class 300 STL(1) — RF",
    "Class 250 (CI) và Class 300 STL(1) — RTJ",
    "Class 300 STL CL 300 — Hợp kim đồng đúc",
    "Class 600 / 900 / 1500 / 2500 — RF",
    "Class 600 / 900 / 1500 / 2500 — RTJ",
]
_FLANGE_THICK_HDR_EN = [
    "Nominal Pipe Size",
    "Class 150 (CI) FF and STL — RF(2)",
    "Class 150 (CI) FF and STL — RTJ",
    "Class 150 STL — Cast Copper Alloy",
    "Class 250 (CI) and Class 300 STL(1) — RF",
    "Class 250 (CI) and Class 300 STL(1) — RTJ",
    "Class 300 STL CL 300 — Cast Copper Alloy",
    "Class 600 / 900 / 1500 / 2500 — RF",
    "Class 600 / 900 / 1500 / 2500 — RTJ",
]
_FLANGE_THICK_NOTES_VI = [
    "1. Các kích thước này áp dụng cho van thép với kích thước ống danh nghĩa từ 1 đến 24.",
    "2. Kích thước mặt bích minh họa là cho bề mặt lồi (raised face) 0,06 in. được cung cấp thông thường.",
]
_FLANGE_THICK_NOTES_EN = [
    "1. These dimensions apply to steel valves for nominal pipe sizes 1 through 24.",
    "2. The flange dimensions illustrated are for regularly furnished 0.06-in. raised face.",
]

_IN_VI = "Tính bằng inch theo ASME B16.1, B16.5 và B16.24."
_IN_EN = "In inches per ASME B16.1, B16.5, and B16.24."


def section(lang):
    b = []

    # ---- 14.3.1 -----------------------------------------------------------
    b.append(H("14.3.1 Đường kính vòng bulông",
               "14.3.1 Diameter of Bolt Circles", lang))
    b.append(LEAD(_IN_VI, _IN_EN, lang))
    b.append(TB(_BOLT_HDR_VI, _BOLT_HDR_EN, _BOLT_CIRCLE_ROWS, lang,
                cap_vi="Bảng 14.3.1 · Đường kính vòng bulông (inch) theo ASME B16.1, B16.5 và B16.24.",
                cap_en="Table 14.3.1 · Diameter of bolt circles (inches) per ASME B16.1, B16.5, and B16.24."))
    b.append(P("Ghi chú:", "Notes:", lang))
    b.append(B(_BOLT_NOTES_VI, _BOLT_NOTES_EN, lang))

    # ---- 14.3.2 -----------------------------------------------------------
    b.append(H("14.3.2 Số lượng và đường kính bulông chốt",
               "14.3.2 Number of Stud Bolts and Diameter", lang))
    b.append(LEAD(_IN_VI, "In Inches per ASME B16.1, B16.5, and B16.24.", lang))
    b.append(TB(_STUD_HDR_VI, _STUD_HDR_EN, _STUD_ROWS, lang,
                cap_vi="Bảng 14.3.2 · Số lượng và đường kính bulông chốt (inch) theo ASME B16.1, B16.5 và B16.24.",
                cap_en="Table 14.3.2 · Number and diameter of stud bolts (inches) per ASME B16.1, B16.5, and B16.24."))
    b.append(P("Ghi chú:", "Notes:", lang))
    b.append(B(_STUD_NOTES_VI, _STUD_NOTES_EN, lang))

    # ---- 14.3.3 -----------------------------------------------------------
    b.append(H("14.3.3 Đường kính mặt bích",
               "14.3.3 Flange Diameter", lang))
    b.append(LEAD(_IN_VI, "In Inches per ASME B16.1, B16.5, and B16.24.", lang))
    b.append(TB(_FLANGE_DIA_HDR_VI, _FLANGE_DIA_HDR_EN, _FLANGE_DIA_ROWS, lang,
                cap_vi="Bảng 14.3.3 · Đường kính mặt bích (inch) theo ASME B16.1, B16.5 và B16.24.",
                cap_en="Table 14.3.3 · Flange diameter (inches) per ASME B16.1, B16.5, and B16.24."))
    b.append(P("Ghi chú:", "Notes:", lang))
    b.append(B(_FLANGE_DIA_NOTES_VI, _FLANGE_DIA_NOTES_EN, lang))

    # ---- 14.3.4 -----------------------------------------------------------
    b.append(H("14.3.4 Chiều dày mặt bích cho phụ kiện mặt bích",
               "14.3.4 Flange Thickness for Flange Fittings", lang))
    b.append(LEAD(_IN_VI, "In Inches per ASME B16.1, B16.5, and B16.24.", lang))
    b.append(TB(_FLANGE_THICK_HDR_VI, _FLANGE_THICK_HDR_EN, _FLANGE_THICK_ROWS, lang,
                cap_vi="Bảng 14.3.4 · Chiều dày mặt bích cho phụ kiện mặt bích (inch) theo ASME B16.1, B16.5 và B16.24. "
                       "RF = bề mặt lồi, RTJ = rãnh chặn kiểu vòng, CI = gang đúc, STL = thép.",
                cap_en="Table 14.3.4 · Flange thickness for flange fittings (inches) per ASME B16.1, B16.5, and B16.24. "
                       "RF = raised face, RTJ = ring-type joint, CI = cast iron, STL = steel."))
    b.append(P("Ghi chú:", "Notes:", lang))
    b.append(B(_FLANGE_THICK_NOTES_VI, _FLANGE_THICK_NOTES_EN, lang))

    return "".join(b)
