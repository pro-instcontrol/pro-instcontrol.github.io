# -*- coding: utf-8 -*-
"""Sections 13.2 and 13.3 — Valve Material Properties; Physical Constants of Hydrocarbons."""
from cvh13_common import T, H, P, LEAD, B, N, TB

# ---------------------------------------------------------------------------
# 13.2 — Valve Material Properties for Pressure-Containing Components
#
# Printed column order (the "Minimum Mechanical Properties" super-heading
# spans the Tensile / Yield / Elongation / Reduction columns):
#   Material Code | Tensile ksi (MPa) | Yield ksi (MPa) |
#   Elongation in 2-inch (50 mm) | Reduction in Area (%) |
#   Modulus of Elasticity at 21 C psi (MPa) | Typical Brinell Hardness
_MATERIAL_ROWS = [
    ("1",     "70-95 (485- 655)",   "40 (275)",          "22",        "35",  "27.9E6 (19.2E4)", "137-187"),
    ("2",     "70-95 (485- 655)",   "40 (275)",          "22",        "35",  "27.9E6 (19.2E4)", "137-187"),
    ("3",     "57 (390) typical",   "42 (290) typical",  "37 typical", "67 typical", "30.0E6 (20.7E4)", "111"),
    ("4",     "79 (545) typical",   "71 (490) typical",  "16 typical", "52 typical", "30.0E6 (20.7E4)", "163"),
    ("5(1)",  "125 (860)",          "105 (725) typical", "16",        "50",  "29.9E6 (20.6E4)", "258"),
    ("6",     "70-95 (485- 655)",   "40 (275)",          "24",        "35",  "27.9E6 (19.2E4)", "140-190"),
    ("7",     "70-95 (485- 655)",   "40 (275)",          "20",        "35",  "29.9E6 (20.6E4)", "147-200"),
    ("8",     "70-95 (485- 655)",   "40 (275)",          "20",        "35",  "29.9E6 (20.6E4)", "147-200"),
    ("9",     "75-100 (515- 690)",  "45(310)",           "19",        "40",  "29.9E6 (20.6E4)", "156-207 required"),
    ("10",    "90-115 (620- 795)",  "60 (415)",          "18",        "35",  "27.4E6 (19.0E4)", "176-255"),
    ("11",    "75 (515)",           "30 (205)",          "30",        "40",  "28.3E6 (19.3E4)", "150"),
    ("12",    "70 (485)",           "25 (170)",          "30",        "40",  "29.0E6 (20.0E4)", "150"),
    ("13",    "70 (485)",           "30 (205)",          "35",        "- - -", "29.0E6 (20.0E4)", "150"),
    ("14",    "70 (485)",           "25 (170)",          "40",        "50",  "28.3E6 (19.3E4)", "150-170"),
    ("15(2)", "75 (515)",           "30 (205)",          "30",        "40",  "28.3E6 (19.5E4)", "150"),
    ("16",    "70 (485)",           "30 (205)",          "30",        "- - -", "28.3E6 (19.5E4)", "163"),
    ("17",    "75 (515)",           "30 (205)",          "30",        "40",  "28.3E6 (19.5E4)", "170"),
    ("18",    "75 (515)",           "35 (240)",          "25",        "- - -", "28.3E6 (19.5E4)", "170"),
    ("19(3)", "70 (480)",           "40 (275)",          "20",        "45",  "29.2E6 (20.1E4)", "241"),
    ("20(4)", "145 (1000)",         "125 (860)",         "13",        "45",  "29E6 (20.0E4)",   "311 min"),
    ("21",    "95 (665)",           "45 (310)",          "35",        "50",  "29.0E6 (20.0E4)", "90 HRB"),
    ("22",    "80 (550)",           "38 (260)",          "35",        "- - -", "29.0E6 (20.0E4)", "82 HRB"),
    ("23",    "90 (620)",           "65 (450)",          "25",        "- - -", "30.5E6 (21.0E4)", "290 max"),
    ("24",    "90 (620)",           "65 (450)",          "25",        "- - -", "30.5E6 (21.0E4)", "98 HRB"),
    ("25(5)", "31 (214)",           "- - -",             "- - -",     "- - -", "13.4E6 (9.2E4)", "160-220"),
    ("26(6)", "41 (282)",           "- - -",             "- - -",     "- - -", "13.4E6 (9.2E4)", "230"),
    ("27",    "60 (415)",           "40 (276)",          "18",        "- - -", "23E6 (16E4)",    "143-187"),
    ("28",    "58 (400)",           "30 (205)",          "8",         "- - -", "- - -",           "139-202"),
    ("29",    "34 (234)",           "16 (110)",          "24",        "- - -", "14.0E6 (9.7E4)", "65"),
    ("30",    "40 (275)",           "18 (124)",          "20",        "- - -", "14.0 (9.7E4)",   "75"),
    ("31",    "65 (448)",           "25 (172)",          "20",        "- - -", "15.3E6 (10.5E4)", "97"),
    ("32",    "75 (515)",           "30 (205)",          "12",        "- - -", "16E6 (11.0E4)",  "150 min"),
    ("33",    "85 (585)",           "35 (240)",          "15",        "- - -", "16E6 (11.0E4)",  "159"),
    ("34",    "55 (380)",           "25 (170)",          "10",        "- - -", "14E6 (9.6E4)",   "55-75 HRB required"),
    ("35",    "60 (415)",           "27 (185)",          "25",        "- - -", "15.0E6 (10.3E4)", "131-142"),
    ("36",    "42 (290)",           "35 (241)",          "10",        "- - -", "9.9E6 (6.8E4)",  "95"),
    ("37(7)", "154 (1060) typical", "93 (638) typical",  "17 typical", "- - -", "30E6 (21E4)",   "37 HRC"),
    ("38",    "140 (965)",          "100 (690)",         "20",        "- - -", "26E6 (17.9E4)",  "265-325"),
    ("39",    "65 (450)",           "25 (170)",          "25",        "- - -", "23E6 (15.8E4)",  "110-150"),
    ("40",    "100 (689)",          "41 (283)",          "40",        "- - -", "29.8E6 (20.5E4)", "210"),
    ("41",    "72 (496)",           "40 (275)",          "20",        "- - -", "30.8E6 (21.2E4)", "150-185"),
    ("42",    "110 (760)",          "51 (350)",          "40",        "- - -", "31.4E6 (21.7E4)", "238"),
    ("43",    "76 (525)",           "40 (275)",          "20",        "- - -", "28.5E6 (19.7E4)", "180"),
]

_MATERIAL_HDR_VI = [
    "Mã vật liệu",
    "Độ bền kéo ksi (MPa)",
    "Giới hạn chảy ksi (MPa)",
    "Độ giãn dài trong 2 inch (50 mm)",
    "Độ co diện tích (%)",
    "Mô đun đàn hồi ở 21°C (70°F), psi (MPa)",
    "Độ cứng Brinell điển hình",
]
_MATERIAL_HDR_EN = [
    "Material Code",
    "Tensile Strength ksi (MPa)",
    "Yield Strength ksi (MPa)",
    "Elongation in 2-inch (50 mm)",
    "Reduction in Area (%)",
    "Modulus of Elasticity at 21°C (70°F) psi (MPa)",
    "Typical Brinell Hardness",
]
_MATERIAL_NOTES_VI = [
    "1. Luyện tôi lại ở 650°C (1200°F).",
    "2. Ủ mềm.",
    "3. ASTM A479, tình trạng ủ mềm",
    "4. ASTM A564 cấp 630, tình trạng H1075",
    "5. A126 Cl.B, thanh tròn đường kính 1.125 in. (95 mm).",
    "6. A126 Cl.C, thanh tròn đường kính 1.125 in. (95 mm).",
    "7. Rèn nóng.",
]
_MATERIAL_NOTES_EN = [
    "1. Tempered 650°C (1200°F).",
    "2. Annealed.",
    "3. ASTM A479 Annealed Condition",
    "4. ASTM A564 Grade 630 Condition H1075",
    "5. A126 Cl.B 1.125 in. (95 mm) dia bar.",
    "6. A126 Cl.C 1.125 in. (95 mm) dia bar.",
    "7. Wrought.",
]

# ---------------------------------------------------------------------------
# 13.3 — Physical Constants of Hydrocarbons
#
# Table A: No. / Compound / Formula / Molecular Weight / Boiling Point /
#          Vapor Pressure at 100 F / Freezing Point  (rows 1-49, all pages)
# Table B: No. / Compound / Formula / Critical Temp / Critical Pressure /
#          Specific Gravity liquid / gas              (rows 1-49, all pages)
_HYDROCARBON_ROWS = [
    ("1",  "Methane",           "CH4",   "16.043", "-258.69", "(5000)(2)", "-296.46(5)"),
    ("2",  "Ethane",            "C2H6",  "30.070", "-127.48", "(800)(2)",  "-297.89(5)"),
    ("3",  "Propane",           "C3H8",  "44.097", "-43.67",  "190",       "-305.84(5)"),
    ("4",  "n–Butane",          "C4H10", "58.124", "31.10",   "51.6",      "-217.05"),
    ("5",  "Isobutane",         "C4H10", "58.124", "10.90",   "72.2",      "-255.29"),
    ("6",  "n–Pentane",         "C5H12", "72.151", "96.92",   "15.570",    "-201.51"),
    ("7",  "Isolpentane",       "C5H12", "72.151", "82.12",   "20.44",     "-255.83"),
    ("8",  "Neopentane",        "C5H12", "72.151", "49.10",   "35.90",     "2.17"),
    ("9",  "n−Hexane",          "C6H14", "86.178", "155.72",  "4.956",     "-139.58"),
    ("10", "2−Methylpentane",   "C6H14", "86.178", "140.47",  "6.767",     "-244.63"),
    ("11", "3−Methylpentane",   "C6H14", "86.178", "145.89",  "6.098",     "- - -"),
    ("12", "Neohexane",         "C6H14", "86.178", "121.52",  "9.856",     "-147.72"),
    ("13", "2,3−Dimethylbutane","C6H14", "86.178", "136.36",  "7.404",     "-199.38"),
    ("14", "n−Heptane",         "C7H16", "100.205","209.17",  "1.620",     "-131.05"),
    ("15", "2−Methylhexane",    "C7H16", "100.205","194.09",  "2.271",     "-180.89"),
    ("16", "3−Methylhexane",    "C7H16", "100.205","197.32",  "2.130",     "- - -"),
    ("17", "3−Ethylpentane",    "C7H16", "100.205","200.25",  "2.012",     "-181.48"),
    ("18", "2,2−Dimethylpentane","C7H16","100.205","174.54",  "3.492",     "-190.86"),
    ("19", "2,4−Dimethylpentane","C7H16","100.205","176.89",  "3.292",     "-182.63"),
    ("20", "3,3−Dimethylpentane","C7H16","100.205","186.91",  "2.773",     "-210.01"),
    ("21", "Triptane",          "C7H16", "100.205","177.58",  "3.374",     "-12.82"),
    ("22", "n−Octane",          "C8H18", "114.232","258.22",  "0.537",     "-70.18"),
    ("23", "Diisobutyl",        "C8H18", "114.232","228.39",  "1.101",     "-132.07"),
    ("24", "Isooctane",         "C8H18", "114.232","210.63",  "1.708",     "-161.27"),
    ("25", "n−Nonane",          "C9H20", "128.259","303.47",  "0.179",     "-64.28"),
    ("26", "n−Decane",          "C10H22","142.286","345.48",  "0.0597",    "-21.36"),
    ("27", "Cyclopentane",      "C5H10", "70.135", "120.65",  "9.914",     "-136.91"),
    ("28", "Methylcyclopentane","C6H12", "84.162", "161.25",  "4.503",     "-224.44"),
    ("29", "Cyclohexane",       "C6H12", "84.162", "177.29",  "3.264",     "43.77"),
    ("30", "Methylcyclohexane", "C7H14", "98.189", "213.68",  "1.609",     "-195.87"),
    ("31", "Ethylene",          "C2H4",  "28.054", "-154.62", "- - -",     "-272.45(5)"),
    ("32", "Propene",           "C3H6",  "42.081", "-53.90",  "226.4",     "-301.45(5)"),
    ("33", "1−Butene",          "C4H8",  "56.108", "20.75",   "63.05",     "-301.63(5)"),
    ("34", "Cis−2−Butene",      "C4H8",  "56.108", "38.69",   "45.54",     "-218.06"),
    ("35", "Trans−2−Butene",    "C4H8",  "56.108", "33.58",   "49.80",     "-157.96"),
    ("36", "Isobutene",         "C4H8",  "56.108", "19.59",   "63.40",     "-220.61"),
    ("37", "1−Pentene",         "C5H10", "70.135", "85.93",   "19.115",    "-265.39"),
    ("38", "1,2−Butadiene",     "C4H6",  "54.092", "51.53",   "(20.)(2)",  "-213.16"),
    ("39", "1,3−Butadiene",     "C4H6",  "54.092", "24.06",   "(60.)(2)",  "-164.02"),
    ("40", "Isoprene",          "C5H8",  "68.119", "93.30",   "16.672",    "-230.74"),
    ("41", "Acetylene",         "C2H2",  "26.038", "-119.(6)","- - -",     "-114(5)"),
    ("42", "Benzene",           "C6H6",  "78.114", "176.17",  "3.224",     "41.96"),
    ("43", "Toluene",           "C7H8",  "92.141", "231.13",  "1.032",     "-138.94"),
    ("44", "Ethylbenzene",      "C8H10", "106.168","277.16",  "0.371",     "-138.91"),
    ("45", "o−Xylene",          "C8H10", "106.168","291.97",  "0.264",     "-13.30"),
    ("46", "m−Xylene",          "C8H10", "106.168","282.41",  "0.326",     "-54.12"),
    ("47", "p−Xylene",          "C8H10", "106.168","281.05",  "0.342",     "55.86"),
    ("48", "Styrene",           "C8H8",  "104.152","293.29",  "(0.24)(2)", "-23.10"),
    ("49", "Isopropylbenzene",  "C9H12", "120.195","306.34",  "0.188",     "-140.82"),
]

_CRITICAL_ROWS = [
    ("1",  "Methane",           "CH4",   "-116.63", "667.8", "0.3(8)",     "0.5539"),
    ("2",  "Ethane",            "C2H6",  "90.09",   "707.8", "0.3564(7)",  "1.0382"),
    ("3",  "Propane",           "C3H8",  "206.01",  "616.3", "0.5077(7)",  "1.5225"),
    ("4",  "n–Butane",          "C4H10", "305.65",  "550.7", "0.5844(7)",  "2.0068"),
    ("5",  "Isobutane",         "C4H10", "274.98",  "529.1", "0.5631(7)",  "2.0068"),
    ("6",  "n–Pentane",         "C5H12", "385.7",   "488.6", "0.6310",     "2.4911"),
    ("7",  "Isolpentane",       "C5H12", "369.10",  "490.4", "0.6247",     "2.4911"),
    ("8",  "Neopentane",        "C5H12", "321.13",  "464.0", "0.5967(7)",  "2.4911"),
    ("9",  "n−Hexane",          "C6H14", "453.7",   "436.9", "0.6640",     "2.9753"),
    ("10", "2−Methylpentane",   "C6H14", "435.83",  "436.6", "0.6579",     "2.9753"),
    ("11", "3−Methylpentane",   "C6H14", "448.3",   "453.1", "0.6689",     "2.9753"),
    ("12", "Neohexane",         "C6H14", "420.13",  "446.8", "0.6540",     "2.9753"),
    ("13", "2,3−Dimethylbutane","C6H14", "440.29",  "453.5", "0.6664",     "2.9753"),
    ("14", "n−Heptane",         "C7H16", "512.8",   "396.8", "0.6882",     "3.4596"),
    ("15", "2−Methylhexane",    "C7H16", "495.00",  "396.5", "0.6830",     "3.4596"),
    ("16", "3−Methylhexane",    "C7H16", "503.78",  "408.1", "0.6917",     "3.4596"),
    ("17", "3−Ethylpentane",    "C7H16", "513.48",  "419.3", "0.7028",     "3.4596"),
    ("18", "2,2−Dimethylpentane","C7H16","477.23",  "402.2", "0.6782",     "3.4596"),
    ("19", "2,4−Dimethylpentane","C7H16","475.95",  "396.9", "0.6773",     "3.4596"),
    ("20", "3,3−Dimethylpentane","C7H16","505.85",  "427.2", "0.6976",     "3.4596"),
    ("21", "Triptane",          "C7H16", "496.44",  "428.4", "0.6946",     "3.4596"),
    ("22", "n−Octane",          "C8H18", "564.22",  "360.6", "0.7068",     "3.9439"),
    ("23", "Diisobutyl",        "C8H18", "530.44",  "360.6", "0.6979",     "3.9439"),
    ("24", "Isooctane",         "C8H18", "519.46",  "372.4", "0.6962",     "3.9439"),
    ("25", "n−Nonane",          "C9H20", "610.68",  "332.",  "0.7217",     "4.4282"),
    ("26", "n−Decane",          "C10H22","652.1",   "304.",  "0.7342",     "4.9125"),
    ("27", "Cyclopentane",      "C5H10", "461.5",   "653.8", "0.7504",     "2.4215"),
    ("28", "Methylcyclopentane","C6H12", "499.35",  "548.9", "0.7536",     "2.9057"),
    ("29", "Cyclohexane",       "C6H12", "536.7",   "591.",  "0.7834",     "2.9057"),
    ("30", "Methylcyclohexane", "C7H14", "570.27",  "503.5", "0.7740",     "3.3900"),
    ("31", "Ethylene",          "C2H4",  "48.58",   "729.8", "- - -",      "0.9686"),
    ("32", "Propene",           "C3H6",  "196.9",   "669.",  "0.5220(7)",  "1.4529"),
    ("33", "1−Butene",          "C4H8",  "295.6",   "583.",  "0.6013(7)",  "1.9372"),
    ("34", "Cis−2−Butene",      "C4H8",  "324.37",  "610.",  "0.6271(7)",  "1.9372"),
    ("35", "Trans−2−Butene",    "C4H8",  "311.86",  "595.",  "0.6100(7)",  "1.9372"),
    ("36", "Isobutene",         "C4H8",  "292.55",  "580.",  "0.6004(7)",  "1.9372"),
    ("37", "1−Pentene",         "C5H10", "376.93",  "590.",  "0.6457",     "2.4215"),
    ("38", "1,2−Butadiene",     "C4H6",  "(339.)(2)","(653.)(2)","0.6587", "1.8676"),
    ("39", "1,3−Butadiene",     "C4H6",  "306.",    "628.",  "0.6272(7)",  "1.8676"),
    ("40", "Isoprene",          "C5H8",  "(412.)(2)","(558.4)(2)","0.6861", "2.3519"),
    ("41", "Acetylene",         "C2H2",  "95.31",   "890.4", "0.615(9)",   "0.8990"),
    ("42", "Benzene",           "C6H6",  "552.22",  "710.4", "0.8844",     "2.6969"),
    ("43", "Toluene",           "C7H8",  "605.55",  "595.9", "0.8718",     "3.1812"),
    ("44", "Ethylbenzene",      "C8H10", "651.24",  "523.5", "0.8718",     "3.6655"),
    ("45", "o−Xylene",          "C8H10", "675.0",   "541.4", "0.8848",     "3.6655"),
    ("46", "m−Xylene",          "C8H10", "651.02",  "513.6", "0.8687",     "3.6655"),
    ("47", "p−Xylene",          "C8H10", "649.6",   "509.2", "0.8657",     "3.6655"),
    ("48", "Styrene",           "C8H8",  "706.0",   "580.",  "0.9110",     "3.5959"),
    ("49", "Isopropylbenzene",  "C9H12", "676.4",   "465.4", "0.8663",     "4.1498"),
]

_HYDRO_HDR_VI = [
    "Số", "Hợp chất", "Công thức", "Khối lượng phân tử",
    "Điểm sôi ở 14.696 psia (°F)",
    "Áp suất hơi ở 100°F (psia)",
    "Điểm đông đặc ở 14.696 psia (°F)",
]
_HYDRO_HDR_EN = [
    "No.", "Compound", "Formula", "Molecular Weight",
    "Boiling Point at 14.696 psia (°F)",
    "Vapor Pressure at 100°F (psia)",
    "Freezing Point at 14.696 psia (°F)",
]
_CRIT_HDR_VI = [
    "Số", "Hợp chất", "Công thức",
    "Nhiệt độ tới hạn (°F)",
    "Áp suất tới hạn (psia)",
    "Lỏng(3)(4) 60°F/60°F",
    "Khí ở 60°F (Không khí=1)(1)",
]
_CRIT_HDR_EN = [
    "No.", "Compound", "Formula",
    "Critical Temp. (°F)",
    "Critical Pressure (psia)",
    "Liquid(3)(4) 60°F/60°F",
    "Gas at 60°F (Air=1)(1)",
]
_HYDRO_NOTES_VI = [
    "1. Giá trị tính toán.",
    "2. (   )−Giá trị ước tính.",
    "3. Hydrocarbon bão hòa không khí.",
    "4. Giá trị tuyệt đối từ cân nặng trong chân không.",
    "5. Ở áp suất bão hòa (điểm ba).",
    "6. Điểm thăng hoa.",
    "7. Áp suất bão hòa và 15.5°C (60°F).",
    "8. Giá trị biểu kiến của methane ở 15.5°C (60°F).",
    "9. Tỷ trọng, 119°F/60°F (điểm thăng hoa).",
]
_HYDRO_NOTES_EN = [
    "1. Calculated values.",
    "2. (   )−Estimated values.",
    "3. Air saturated hydrocarbons.",
    "4. Absolute values from weights in vacuum.",
    "5. At saturation pressure (triple point).",
    "6. Sublimation point.",
    "7. Saturation pressure and 15.5°C (60°F).",
    "8. Apparent value for methane at 15.5°C (60°F).",
    "9. Specific gravity, 119°F/60°F (sublimation point).",
]


def section(lang):
    b = []

    # ---- 13.2 ------------------------------------------------------------
    b.append(H("13.2 Tính chất của vật liệu làm bộ phận chịu áp suất",
               "13.2 Valve Material Properties for Pressure-Containing Components",
               lang))
    b.append(LEAD("Các mã vật liệu trong bảng này tương ứng với danh mục Đặc tả tiêu chuẩn "
                  "cho vật liệu van được liệt kê ở mục 13.1.",
                  "The material codes in this table correspond to the Standard "
                  "Specifications for Valve Materials listings in section 13.1.",
                  lang))
    b.append(TB(_MATERIAL_HDR_VI, _MATERIAL_HDR_EN, _MATERIAL_ROWS, lang,
                cap_vi="Bảng 13.2 · Tính chất cơ học tối thiểu của vật liệu chế tạo bộ phận "
                       "chịu áp suất.",
                cap_en="Table 13.2 · Minimum mechanical properties of materials for "
                       "pressure-containing components."))
    b.append(P("Ghi chú:", "Notes:", lang))
    b.append(B(_MATERIAL_NOTES_VI, _MATERIAL_NOTES_EN, lang))

    # ---- 13.3 ------------------------------------------------------------
    b.append(H("13.3 Hằng số vật lý của hydrocarbon",
               "13.3 Physical Constants of Hydrocarbons",
               lang))
    b.append(TB(_HYDRO_HDR_VI, _HYDRO_HDR_EN, _HYDROCARBON_ROWS, lang,
                cap_vi="Bảng 13.3 · Hằng số vật lý của hydrocarbon: điểm sôi, áp suất hơi "
                       "ở 100°F và điểm đông đặc.",
                cap_en="Table 13.3 · Physical constants of hydrocarbons: boiling point, "
                       "vapor pressure at 100°F and freezing point."))
    b.append(TB(_CRIT_HDR_VI, _CRIT_HDR_EN, _CRITICAL_ROWS, lang,
                cap_vi="Bảng 13.4 · Hằng số tới hạn và tỷ trọng của hydrocarbon.",
                cap_en="Table 13.4 · Critical constants and specific gravity of hydrocarbons."))
    b.append(P("Ghi chú:", "Notes:", lang))
    b.append(B(_HYDRO_NOTES_VI, _HYDRO_NOTES_EN, lang))

    return "".join(b)
