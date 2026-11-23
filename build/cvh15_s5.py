# -*- coding: utf-8 -*-
"""Sections 15.13-15.15 — API/Baume gravity / Useful conversions / Metric prefixes."""
from cvh15_common import T, H, P, LEAD, B, N, TB

# ---------------------------------------------------------------------------
# 15.13 — API and Baumé Gravity Tables and Weight Factors
#
# Printed as TWO side-by-side 5-column blocks (API Gravity / Baumé Gravity /
# Specific Gravity / Lb per U.S. Gal / U.S. Gal per Lb); the OCR interleaves the
# two blocks and even splits one printed row across two lines (0 ... then
# 31 ...).  All 101 five-value groups (API 0..100) are kept intact and listed
# here in ascending API order.  Quirks from the source (e.g. Baumé 50.61 at
# API 47) are preserved verbatim.
_GRAVITY_ROWS = [
    ("0",   "10.247", "1.0760", "8.962", "0.1116"),
    ("1",   "9.223",  "1.0679", "8.895", "0.1124"),
    ("2",   "8.198",  "1.0599", "8.828", "0.1133"),
    ("3",   "7.173",  "1.0520", "8.762", "0.1141"),
    ("4",   "6.148",  "1.0443", "8.698", "0.1150"),
    ("5",   "5.124",  "1.0366", "8.634", "0.1158"),
    ("6",   "4.099",  "1.0291", "8.571", "0.1167"),
    ("7",   "3.074",  "1.0217", "8.509", "0.1175"),
    ("8",   "2.049",  "1.0143", "8.448", "0.1184"),
    ("9",   "1.025",  "1.0071", "8.388", "0.1192"),
    ("10",  "10.00",  "1.0000", "8.328", "0.1201"),
    ("11",  "10.99",  "0.9930", "8.270", "0.1209"),
    ("12",  "11.98",  "0.9861", "8.212", "0.1218"),
    ("13",  "12.97",  "0.9792", "8.155", "0.1226"),
    ("14",  "13.96",  "0.9725", "8.099", "0.1235"),
    ("15",  "14.95",  "0.9659", "8.044", "0.1243"),
    ("16",  "15.94",  "0.9593", "7.989", "0.1252"),
    ("17",  "16.93",  "0.9529", "7.935", "0.1260"),
    ("18",  "17.92",  "0.9465", "7.882", "0.1269"),
    ("19",  "18.90",  "0.9402", "7.830", "0.1277"),
    ("20",  "19.89",  "0.9340", "7.778", "0.1286"),
    ("21",  "20.88",  "0.9279", "7.727", "0.1294"),
    ("22",  "21.87",  "0.9218", "7.676", "0.1303"),
    ("23",  "22.86",  "0.9159", "7.627", "0.1311"),
    ("24",  "23.85",  "0.9100", "7.578", "0.1320"),
    ("25",  "24.84",  "0.9042", "7.529", "0.1328"),
    ("26",  "25.83",  "0.8984", "7.481", "0.1337"),
    ("27",  "26.82",  "0.8927", "7.434", "0.1345"),
    ("28",  "27.81",  "0.8871", "7.387", "0.1354"),
    ("29",  "28.80",  "0.8816", "7.341", "0.1362"),
    ("30",  "29.79",  "0.8762", "7.296", "0.1371"),
    ("31",  "30.78",  "0.8708", "7.251", "0.1379"),
    ("32",  "31.77",  "0.8654", "7.206", "0.1388"),
    ("33",  "32.76",  "0.8602", "7.163", "0.1396"),
    ("34",  "33.75",  "0.8550", "7.119", "0.1405"),
    ("35",  "34.73",  "0.8498", "7.076", "0.1413"),
    ("36",  "35.72",  "0.8448", "7.034", "0.1422"),
    ("37",  "36.71",  "0.8398", "6.993", "0.1430"),
    ("38",  "37.70",  "0.8348", "6.951", "0.1439"),
    ("39",  "38.69",  "0.8299", "6.910", "0.1447"),
    ("40",  "39.68",  "0.8251", "6.870", "0.1456"),
    ("41",  "40.67",  "0.8203", "6.830", "0.1464"),
    ("42",  "41.66",  "0.8155", "6.790", "0.1473"),
    ("43",  "42.65",  "0.8109", "6.752", "0.1481"),
    ("44",  "43.64",  "0.8063", "6.713", "0.1490"),
    ("45",  "44.63",  "0.8017", "6.675", "0.1498"),
    ("46",  "45.62",  "0.7972", "6.637", "0.1507"),
    ("47",  "50.61",  "0.7927", "6.600", "0.1515"),
    ("48",  "50.60",  "0.7883", "6.563", "0.1524"),
    ("49",  "50.59",  "0.7839", "6.526", "0.1532"),
    ("50",  "50.58",  "0.7796", "6.490", "0.1541"),
    ("51",  "50.57",  "0.7753", "6.455", "0.1549"),
    ("52",  "51.55",  "0.7711", "6.420", "0.1558"),
    ("53",  "52.54",  "0.7669", "6.385", "0.1566"),
    ("54",  "53.53",  "0.7628", "6.350", "0.1575"),
    ("55",  "54.52",  "0.7587", "6.316", "0.1583"),
    ("56",  "55.51",  "0.7547", "6.283", "0.1592"),
    ("57",  "56.50",  "0.7507", "6.249", "0.1600"),
    ("58",  "57.49",  "0.7467", "6.216", "0.1609"),
    ("59",  "58.48",  "0.7428", "6.184", "0.1617"),
    ("60",  "59.47",  "0.7389", "6.151", "0.1626"),
    ("61",  "60.46",  "0.7351", "6.119", "0.1634"),
    ("62",  "61.45",  "0.7313", "6.087", "0.1643"),
    ("63",  "62.44",  "0.7275", "6.056", "0.1651"),
    ("64",  "63.43",  "0.7238", "6.025", "0.1660"),
    ("65",  "64.42",  "0.7201", "5.994", "0.1668"),
    ("66",  "65.41",  "0.7165", "5.964", "0.1677"),
    ("67",  "66.40",  "0.7128", "5.934", "0.1685"),
    ("68",  "67.39",  "0.7093", "5.904", "0.1694"),
    ("69",  "68.37",  "0.7057", "5.874", "0.1702"),
    ("70",  "69.36",  "0.7022", "5.845", "0.1711"),
    ("71",  "70.35",  "0.6988", "5.817", "0.1719"),
    ("72",  "71.34",  "0.6953", "5.788", "0.1728"),
    ("73",  "72.33",  "0.6919", "5.759", "0.1736"),
    ("74",  "73.32",  "0.6886", "5.731", "0.1745"),
    ("75",  "74.31",  "0.6852", "5.703", "0.1753"),
    ("76",  "75.30",  "0.6819", "5.676", "0.1762"),
    ("77",  "76.29",  "0.6787", "5.649", "0.1770"),
    ("78",  "77.28",  "0.6754", "5.622", "0.1779"),
    ("79",  "78.27",  "0.6722", "5.595", "0.1787"),
    ("80",  "79.26",  "0.6690", "5.568", "0.1796"),
    ("81",  "80.25",  "0.6659", "5.542", "0.1804"),
    ("82",  "81.24",  "0.6628", "5.516", "0.1813"),
    ("83",  "82.23",  "0.6597", "5.491", "0.1821"),
    ("84",  "83.22",  "0.6566", "5.465", "0.1830"),
    ("85",  "84.20",  "0.6536", "5.440", "0.1838"),
    ("86",  "85.19",  "0.6506", "5.415", "0.1847"),
    ("87",  "86.18",  "0.6476", "5.390", "0.1855"),
    ("88",  "87.17",  "0.6446", "5.365", "0.1864"),
    ("89",  "88.16",  "0.6417", "5.341", "0.1872"),
    ("90",  "89.15",  "0.6388", "5.316", "0.1881"),
    ("91",  "90.14",  "0.6360", "5.293", "0.1889"),
    ("92",  "91.13",  "0.6331", "5.269", "0.1898"),
    ("93",  "92.12",  "0.6303", "5.246", "0.1906"),
    ("94",  "93.11",  "0.6275", "5.222", "0.1915"),
    ("95",  "94.10",  "0.6247", "5.199", "0.1924"),
    ("96",  "95.09",  "0.6220", "5.176", "0.1932"),
    ("97",  "96.08",  "0.6193", "5.154", "0.1940"),
    ("98",  "97.07",  "0.6166", "5.131", "0.1949"),
    ("99",  "98.06",  "0.6139", "5.109", "0.1957"),
    ("100", "99.05",  "0.6112", "5.086", "0.1966"),
]
_GRAVITY_HDR_VI = ["Độ API", "Độ Baumé", "Tỷ trọng", "Lb/gallon (Mỹ)",
                   "Gallon (Mỹ)/lb"]
_GRAVITY_HDR_EN = ["API Gravity", "Baumé Gravity", "Specific Gravity",
                   "Lb per U.S. Gal", "U.S. Gal per Lb"]

# Formula list — the numeric/formula content is kept verbatim; only the
# descriptive label words are localized.
_FORMULA_LIGHT_VI = [
    "Độ Baumé = 140/G − 130 , G = 140/(130 + Độ Baumé)",
    "Độ A.P.I. = 141.5/G − 131.5 , G = 141.5/(131.5 + Độ A.P.I.)",
]
_FORMULA_LIGHT_EN = [
    "Degrees Baumé = 140/G − 130 , G = 140/(130 + Degrees Baumé)",
    "Degrees A.P.I. = 141.5/G − 131.5 , G = 141.5/(131.5 + Degrees A.P.I.)",
]
_FORMULA_HEAVY_VI = ["Độ Baumé = 145/G − 145 , G = 145/(145 − Độ Baumé)"]
_FORMULA_HEAVY_EN = ["Degrees Baumé = 145/G − 145 , G = 145/(145 − Degrees Baumé)"]
_MIX_VI = [
    "D = (m·d1 + n·d2)/(m + n)",
    "D = Tỷ trọng của hỗn hợp",
    "m = Tỷ lệ của dầu có tỷ trọng d1",
    "n = Tỷ lệ của dầu có tỷ trọng d2",
    "d1 = Tỷ trọng của dầu m",
    "d2 = Tỷ trọng của dầu n",
]
_MIX_EN = [
    "D = (m·d1 + n·d2)/(m + n)",
    "D = Density or Specific Gravity of mixture",
    "m = Proportion of oil of d1 density",
    "n = Proportion of oil of d2 density",
    "d1 = Specific Gravity of m oil",
    "d2 = Specific Gravity of n oil",
]

# ---------------------------------------------------------------------------
# 15.14 — Other Useful Conversions
# Source header reads "To Covert From" (OCR typo); corrected here.  All unit
# strings and substitute factors (including .41793/...) are kept verbatim.
_CONVERT_ROWS = [
    ("Cu Ft (Methane)",               "B.T.U.",            "1000 (approx.)"),
    ("Cu Ft of Water",                "Lbs of Water",      "62.4"),
    ("Degrees",                       "Radians",           "0.01745"),
    ("Gals",                          "Lbs of Water",      "8.336"),
    ("Grams",                         "Ounces",            "0.0352"),
    ("Horsepower (mech.)",            "Ft Lbs per Min",    "33,000"),
    ("Horsepower (elec.)",            "Watts",             "746"),
    ("Kg",                            "Lbs",               "2.205"),
    ("Kg per Cu Meter",              "Lbs per Cu Ft",     "0.06243"),
    ("Kilowatts",                     "Horsepower",        "1.341"),
    ("Lbs",                           "Kg",                "0.4536"),
    ("Lbs of Air (14.7 psia and 60°F)", "Cu Ft of Air",    "13.1"),
    ("Lbs per Cu Ft",                 "Kg per Cu Meter",   "16.0184"),
    ("Lbs per Hr (Gas)",              "Std Cu Ft per Hr",  "13.1/Specific Gravity"),
    ("Lbs per Hr (Water)",            "Gals per Min",      "0.002"),
    ("Lbs per Sec (Gas)",             "Std Cu Ft per Hr",  ".41793/Specific Gravity"),
    ("Radians",                       "Degrees",           "57.3"),
    ("Scfh Air",                      "Scfh Propane",      "0.81"),
    ("Scfh Air",                      "Scfh Butane",       "0.71"),
    ("Scfh Air",                      "Scfh 0.6 Natural Gas", "1.29"),
    ("Scfh",                          "Cu Meters per Hr",  "0.028317"),
]
_CONVERT_HDR_VI = ["Chuyển đổi từ", "Sang", "Thay vào công thức"]
_CONVERT_HDR_EN = ["To Convert From", "To", "Substitute in Formula"]

# ---------------------------------------------------------------------------
# 15.15 — Metric Prefixes and Suffixes
# Source prints powers with superscript digits (10^18 written as "1018");
# they are rendered here with a caret, which is XML-safe.  Prefix names and
# symbols stay verbatim; header/caption/note are localized.
_PREFIX_ROWS = [
    ("1 000 000 000 000 000 000 = 10^18", "exa",   "E"),
    ("1 000 000 000 000 000 = 10^15",      "peta",  "P"),
    ("1 000 000 000 000 = 10^12",          "tera",  "T"),
    ("1 000 000 000 = 10^9",               "giga",  "G"),
    ("1 000 000 = 10^6",                   "mega",  "M"),
    ("1 000 = 10^3",                       "kilo",  "k"),
    ("100 = 10^2",                         "hecto", "h"),
    ("10 = 10^1",                          "deka",  "da"),
    ("0.1 = 10^-1",                        "deci",  "d"),
    ("0.01 = 10^-2",                       "centi", "c"),
    ("0.001 = 10^-3",                      "milli", "m"),
    ("0.000 001 = 10^-6",                  "micro", "µ"),
    ("0.000 000 001 = 10^-9",              "nano",  "n"),
    ("0.000 000 000 001 = 10^-12",         "pico",  "p"),
    ("0.000 000 000 000 001 = 10^-15",     "femto", "f"),
    ("0.000 000 000 000 000 001 = 10^-18", "atto",  "a"),
]
_PREFIX_HDR_VI = ["Hệ số nhân", "Tiền tố", "Ký hiệu"]
_PREFIX_HDR_EN = ["Multiplication Factor", "Prefix", "Symbol"]


def section(lang):
    b = []

    # ---- 15.13 -----------------------------------------------------------
    b.append(H("15.13 Bảng trọng lực API và Baumé cùng hệ số trọng lượng",
               "15.13 API and Baumé Gravity Tables and Weight Factors",
               lang))
    b.append(LEAD("Bảng dưới đây cho biết mối quan hệ giữa độ API, độ Baumé, "
                  "tỷ trọng và trọng lượng trên mỗi gallon (Mỹ).",
                  "The table below relates degrees API, degrees Baumé, specific "
                  "gravity and weight per U.S. gallon.",
                  lang))
    b.append(TB(_GRAVITY_HDR_VI, _GRAVITY_HDR_EN, _GRAVITY_ROWS, lang,
                cap_vi="Bảng 15.1 · Trọng lực API và Baumé, tỷ trọng, số pound "
                       "mỗi gallon (Mỹ) và số gallon (Mỹ) mỗi pound.",
                cap_en="Table 15.1 · API and Baumé gravity, specific gravity, "
                       "pounds per U.S. gallon and U.S. gallons per pound."))
    b.append(N("Trong bản gốc, bảng được in thành hai nhóm cột xếp cạnh nhau và "
               "có dòng bị gãy giữa chừng; các dòng ở đây được gộp lại và sắp "
               "theo độ API tăng dần.",
               "In the source the table is printed as two side-by-side column "
               "groups, with one row split across lines; the rows here are "
               "combined and ordered by ascending API gravity.",
               lang))
    b.append(P("Mối quan hệ giữa độ Baumé hoặc độ A.P.I. với tỷ trọng được biểu "
               "thị bằng các công thức sau:",
               "The relation of degrees Baumé or A.P.I. to specific gravity is "
               "expressed by the following formulas:",
               lang))
    b.append(P("Đối với chất lỏng nhẹ hơn nước:",
               "For liquids lighter than water:", lang))
    b.append(B(_FORMULA_LIGHT_VI, _FORMULA_LIGHT_EN, lang))
    b.append(P("Đối với chất lỏng nặng hơn nước:",
               "For liquids heavier than water:", lang))
    b.append(B(_FORMULA_HEAVY_VI, _FORMULA_HEAVY_EN, lang))
    b.append(P("G = Tỷ trọng = tỷ số giữa trọng lượng của một thể tích dầu nhất "
               "định ở 15.5°C (60°F) và trọng lượng của cùng một thể tích nước ở "
               "15.5°C (60°F).",
               "G = Specific Gravity = ratio of the weight of a given volume of "
               "oil at 15.5°C (60°F) to the weight of the same volume of water "
               "at 15.5°C (60°F).",
               lang))
    b.append(P("Các bảng trên dựa trên trọng lượng của 1 gallon (Mỹ) dầu có thể "
               "tích 231 inch khối ở 15.5°C (60°F), trong không khí ở áp suất "
               "760 mm và độ ẩm 50%. Giả định trọng lượng của 1 gallon nước ở "
               "15.5°C (60°F) trong không khí là 8.32828 pound.",
               "The previous tables are based on the weight of 1 gallon (U.S.) "
               "of oil with a volume of 231 cubic inches at 15.5°C (60°F) in air "
               "at 760 mm pressure and 50% humidity. Assumed weight of 1 gallon "
               "of water at 15.5°C (60°F) in air is 8.32828 pounds.",
               lang))
    b.append(P("Để xác định tỷ trọng thu được khi trộn các loại dầu có tỷ trọng "
               "khác nhau:",
               "To determine the resulting gravity by mixing oils of different "
               "gravities:",
               lang))
    b.append(B(_MIX_VI, _MIX_EN, lang))

    # ---- 15.14 -----------------------------------------------------------
    b.append(H("15.14 Các phép chuyển đổi hữu ích khác",
               "15.14 Other Useful Conversions", lang))
    b.append(TB(_CONVERT_HDR_VI, _CONVERT_HDR_EN, _CONVERT_ROWS, lang,
                cap_vi="Bảng 15.2 · Các phép chuyển đổi hữu ích khác.",
                cap_en="Table 15.2 · Other useful conversions."))

    # ---- 15.15 -----------------------------------------------------------
    b.append(H("15.15 Tiền tố và hậu tố hệ mét",
               "15.15 Metric Prefixes and Suffixes", lang))
    b.append(TB(_PREFIX_HDR_VI, _PREFIX_HDR_EN, _PREFIX_ROWS, lang,
                cap_vi="Bảng 15.3 · Tiền tố hệ mét và hệ số nhân tương ứng.",
                cap_en="Table 15.3 · Metric prefixes and their multiplication "
                       "factors."))
    b.append(N("Chữ số mũ trong bản gốc được in ở dạng mũ; ở đây được viết bằng "
               "dấu ^ (ví dụ: 10^18).",
               "Superscript digits in the source are rendered here with a caret "
               "(for example 10^18).",
               lang))

    return "".join(b)
