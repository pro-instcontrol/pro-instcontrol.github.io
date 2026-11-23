# -*- coding: utf-8 -*-
"""Sections 13.4 and 13.5 — Specific Heat Ratio (k); Physical Constants of Various Fluids."""
from cvh13_common import T, H, P, LEAD, B, N, TB

# ---------------------------------------------------------------------------
# 13.4 — four Gas / k column pairs.  The source table prints four repeated
# "Gas / Specific Heat Ratio (k)" header blocks; rows below follow the exact
# reading order of the raw text.  The stray "0.6" is kept verbatim (OCR quirk).
# ---------------------------------------------------------------------------
_SH_HDR_VI = ["Khí", "k", "Khí", "k", "Khí", "k", "Khí", "k"]
_SH_HDR_EN = ["Gas", "k", "Gas", "k", "Gas", "k", "Gas", "k"]
_SH_ROWS = [
    ["Acetylene", "1.38", "Carbon Dioxide", "1.29", "", "0.6", "Natural Gas", "1.32"],
    ["Steam(1)", "1.33", "", "", "", "", "", ""],
    ["Air", "1.40", "Ethane", "1.25", "", "", "Nitrogen", "1.40"],
    ["Argon", "1.67", "Helium", "1.66", "", "", "Oxygen", "1.40"],
    ["Butane", "1.17", "Hydrogen", "1.40", "", "", "Propane", "1.21"],
    ["Carbon Monoxide", "1.40", "Methane", "1.26", "", "", "Propylene", "1.15"],
]

# ---------------------------------------------------------------------------
# 13.5 — one merged table: the same nine-column header set appears on three
# consecutive printed pages (274-276) with "continued..." captions.  All 64
# data rows are kept in one table.  Data cells are language-neutral and
# transcribed verbatim, including "- - -" missing-value markers, footnote
# markers and OCR spellings of formulas/names.
# ---------------------------------------------------------------------------
_PHYS_HDR_VI = [
    "Chất lỏng", "Công thức", "Khối lượng phân tử",
    "Điểm sôi (°F, 14,696 psia)", "Áp suất hơi 70°F (psig)",
    "Nhiệt độ tới hạn (°F)", "Áp suất tới hạn (psia)",
    "Trọng lực riêng lỏng (60/60°F)", "Trọng lực riêng khí",
]
_PHYS_HDR_EN = [
    "Fluid", "Formula", "Molecular Weight",
    "Boiling Point (°F, 14.696 psia)", "Vapor Pressure 70°F (psig)",
    "Critical Temp (°F)", "Critical Pressure (psia)",
    "Specific Gravity, Liquid (60/60°F)", "Specific Gravity, Gas",
]
_PHYS_ROWS = [
    # page 274
    ["Acetic Acid", "HC2H3O2", "60.05", "245", "- - -", "- - -", "- - -", "1.05", "- - -"],
    ["Acetone", "C3H6O", "58.08", "133", "- - -", "455", "691", "0.79", "2.01"],
    ["Air", "N2O2", "28.97", "-317", "- - -", "-221", "547", "0.86(3)", "1.0"],
    ["Alcohol, Ethyl", "C2H6O", "46.07", "173", "2.3(2)", "470", "925", "0.794", "1.59"],
    ["Alcohol, Methyl", "CH4O", "32.04", "148", "4.63(2)", "463", "1174", "0.796", "1.11"],
    ["Ammonia", "NH3", "17.03", "-28", "114", "270", "1636", "0.62", "0.59"],
    ["Ammonium Chloride(1)", "NH4CI", "- - -", "- - -", "- - -", "- - -", "- - -", "1.07", "- - -"],
    ["Ammonium Hydroxide(1)", "NH4OH", "- - -", "- - -", "- - -", "- - -", "- - -", "0.91", "- - -"],
    ["Ammonium Sulfate(1)", "(NH4)2SO4", "- - -", "- - -", "- - -", "- - -", "- - -", "1.15", "- - -"],
    ["Aniline", "C6H7N", "93.12", "365", "- - -", "798", "770", "1.02", "- - -"],
    ["Argon", "A", "39.94", "-302", "- - -", "-188", "705", "1.65", "1.38"],
    ["Beer", "- - -", "- - -", "- - -", "- - -", "- - -", "- - -", "1.01", "- - -"],
    ["Bromine", "Br2", "159.84", "138", "- - -", "575", "- - -", "2.93", "5.52"],
    ["Calcium Chloride(1)", "CaCI2", "- - -", "- - -", "- - -", "- - -", "- - -", "1.23", "- - -"],
    ["Carbon Dioxide", "CO2", "44.01", "-109", "839", "88", "1072", "0.801(3)", "1.52"],
    ["Carbon Disulfide", "CS2", "76.1", "115", "- - -", "- - -", "- - -", "1.29", "2.63"],
    ["Carbon Monoxide", "CO", "28.01", "-314", "- - -", "-220", "507", "0.80", "0.97"],
    ["Carbon Tetrachloride", "CCI4", "153.84", "170", "- - -", "542", "661", "1.59", "5.31"],
    ["Chlorine", "CI2", "70.91", "-30", "85", "291", "1119", "1.42", "2.45"],
    ["Chromic Acid", "H2CrO4", "118.03", "- - -", "- - -", "- - -", "- - -", "1.21", "- - -"],
    ["Citric Acid", "C6H8O7", "192.12", "- - -", "- - -", "- - -", "- - -", "1.54", "- - -"],
    ["Copper Sulfate(1)", "CuSO4", "- - -", "- - -", "- - -", "- - -", "- - -", "1.17", "- - -"],
    ["Ether", "(C2H5)2O", "74.12", "34", "- - -", "- - -", "- - -", "0.74", "2.55"],
    ["Ferric Chloride(1)", "FeCI3", "- - -", "- - -", "- - -", "- - -", "- - -", "1.23", "- - -"],
    ["Fluorine", "F2", "38.00", "-305", "300", "1200", "809", "1.11", "1.31"],
    ["Formaldehyde", "H2CO", "30.03", "-6", "- - -", "- - -", "- - -", "0.82", "1.08"],
    ["Formic Acid", "HCO2H", "46.03", "214", "- - -", "- - -", "- - -", "1.23", "- - -"],
    ["Furfural", "C5H4O2", "96.08", "324", "- - -", "- - -", "- - -", "1.16", "- - -"],
    ["Glycerine", "C3H8O3", "92.09", "554", "- - -", "- - -", "- - -", "1.26", "- - -"],
    ["Glycol", "C2H6O2", "62.07", "387", "- - -", "- - -", "- - -", "1.11", "- - -"],
    # page 275 (continued)
    ["Helium", "He", "4.003", "-454", "- - -", "-450", "33", "0.18", "0.14"],
    ["Hydrochloric Acid", "HCI", "36.47", "-115", "- - -", "- - -", "- - -", "1.64", "- - -"],
    ["Hydrofluoric Acid", "HF", "20.01", "66", "0.9", "446", "- - -", "0.92", "- - -"],
    ["Hydrogen", "H2", "2.016", "-422", "- - -", "-400", "188", "0.07(3)", "0.07"],
    ["Hydrogen Chloride", "HCI", "36.47", "-115", "613", "125", "1198", "0.86", "1.26"],
    ["Hydrogen Sulfide", "H2S", "34.07", "-76", "252", "213", "1307", "0.79", "1.17"],
    ["Isopropyl Alcohol", "C3H8O", "60.09", "180", "- - -", "- - -", "- - -", "0.78", "2.08"],
    ["Linseed Oil", "- - -", "- - -", "538", "- - -", "- - -", "- - -", "0.93", "- - -"],
    ["Mangesium Chloride(1)", "MgCI2", "- - -", "- - -", "- - -", "- - -", "- - -", "1.22", "- - -"],
    ["Mercury", "Hg", "200.61", "670", "- - -", "- - -", "- - -", "13.6", "6.93"],
    ["Methyl Bromide", "CH3Br", "94.95", "38", "13", "376", "", "1.73", "3.27"],
    ["Methyl Chloride", "CH3CI", "50.49", "-11", "59", "290", "969", "0.99", "1.74"],
    ["Naphthalene", "C10H8", "128.16", "424", "- - -", "- - -", "- - -", "1.14", "4.43"],
    ["Nitric Acid", "HNO3", "63.02", "187", "- - -", "- - -", "- - -", "1.5", "- - -"],
    ["Nitrogen", "N2", "28.02", "-320", "- - -", "-233", "493", "0.81(3)", "0.97"],
    ["Oil, Vegetable", "- - -", "- - -", "- - -", "- - -", "- - -", "- - -", "0.91- 0.94", "- - -"],
    ["Oxygen", "O2", "32", "-297", "- - -", "-181", "737", "1.14(3)", "1.105"],
    ["Phosgene", "COCI2", "98.92", "47", "10.7", "360", "823", "1.39", "3.42"],
    ["Phosphoric Acid", "H3PO4", "98.00", "415", "- - -", "- - -", "- - -", "1.83", "- - -"],
    ["Potassium Carbonate(1)", "K2CO3", "- - -", "- - -", "- - -", "- - -", "- - -", "1.24", "- - -"],
    ["Potassium Chloride(1)", "KCI", "- - -", "- - -", "- - -", "- - -", "- - -", "1.16", "- - -"],
    ["Potassium Hydroxide(1)", "KOH", "- - -", "- - -", "- - -", "- - -", "- - -", "1.24", "- - -"],
    ["Sodium Chloride(1)", "NaCI", "- - -", "- - -", "- - -", "- - -", "- - -", "1.19", "- - -"],
    ["Sodium Hydroxide(1)", "NaOH", "- - -", "- - -", "- - -", "- - -", "- - -", "1.27", "- - -"],
    ["Sodium Sulfate(1)", "Na2SO4", "- - -", "- - -", "- - -", "- - -", "- - -", "1.24", "- - -"],
    ["Sodium Thiosulfate(1)", "Na2S2O3", "- - -", "- - -", "- - -", "- - -", "- - -", "1.23", "- - -"],
    # page 276 (continued)
    ["Starch", "(C6H10O5)x", "- - -", "- - -", "- - -", "- - -", "- - -", "1.50", "- - -"],
    ["Sugar Solutions(1)", "C12H22011", "- - -", "- - -", "- - -", "- - -", "- - -", "1.10", "- - -"],
    ["Sulfuric Acid", "H2SO4", "98.08", "626", "- - -", "- - -", "- - -", "1.83", "- - -"],
    ["Sulfur Dioxide", "SO2", "64.6", "14", "34.4", "316", "1145", "1.39", "2.21"],
    ["Turpentine", "- - -", "- - -", "320", "- - -", "- - -", "- - -", "0.87", "- - -"],
    ["Water", "H2O", "18.016", "212", "0.9492(2)", "706", "3208", "1.00", "0.62"],
    ["Zinc Chloride(1)", "ZnCI2", "- - -", "- - -", "- - -", "- - -", "- - -", "1.24", "- - -"],
    ["Zinc Sulfate(1)", "ZnSO4", "- - -", "- - -", "- - -", "- - -", "- - -", "1.31", "- - -"],
]


def section(lang):
    b = []

    # ---- 13.4 -------------------------------------------------------------
    b.append(H("13.4 Tỷ lệ nhiệt dung riêng (k)",
               "13.4 Specific Heat Ratio (k)", lang))
    b.append(LEAD(
        "Bảng dưới đây liệt kê tỷ lệ nhiệt dung riêng (k) của các chất khí "
        "thường gặp trong tính toán van điều khiển.",
        "The table below lists the specific heat ratio (k) of gases commonly "
        "encountered in control-valve calculations.", lang))
    b.append(TB(_SH_HDR_VI, _SH_HDR_EN, _SH_ROWS, lang,
                cap_vi="Bảng 13.4 — Tỷ lệ nhiệt dung riêng (k) của các chất khí.",
                cap_en="Table 13.4 — Specific Heat Ratio (k) of gases."))
    b.append(B(
        ["1. Sử dụng bảng thuộc tính nếu có để đạt độ chính xác cao hơn."],
        ["1. Use property tables if available for greater accuracy."], lang))
    b.append(N(
        "Ghi chú về nguồn: giá trị “0.6” xuất hiện trong dòng dữ liệu đầu tiên "
        "mà không có tên chất khí tương ứng; giá trị này được giữ nguyên để "
        "bảo toàn dữ liệu gốc.",
        "Source note: the value “0.6” appears in the first data row with no "
        "matching gas name; it is retained verbatim for data fidelity.", lang))

    # ---- 13.5 -------------------------------------------------------------
    b.append(H("13.5 Các hằng số vật lý của các chất lỏng khác nhau",
               "13.5 Physical Constants of Various Fluids", lang))
    b.append(LEAD(
        "Bảng tổng hợp các hằng số vật lý của nhiều chất lỏng và chất khí, "
        "gồm điểm sôi, áp suất hơi, thông số tới hạn và trọng lực riêng. "
        "Dữ liệu từ ba trang liên tiếp của nguồn được gộp thành một bảng.",
        "A consolidated table of physical constants for a wide range of "
        "fluids, including boiling point, vapor pressure, critical properties "
        "and specific gravity. Data from three consecutive source pages are "
        "merged into one table.", lang))
    b.append(TB(_PHYS_HDR_VI, _PHYS_HDR_EN, _PHYS_ROWS, lang,
                cap_vi="Bảng 13.5 — Các hằng số vật lý của các chất lỏng khác nhau "
                       "(tiếp theo, các trang 274–276).",
                cap_en="Table 13.5 — Physical Constants of Various Fluids "
                       "(continued, pages 274–276)."))
    b.append(B(
        ["1. Dung dịch nước − 25% theo khối lượng hợp chất.",
         "2. Áp suất hơi tính bằng psia ở 39°C (100°F).",
         "3. Áp suất hơi tính bằng psia."],
        ["1. Aqueous Solution − 25% by weight of compound.",
         "2. Vapor pressure in psia at 39°C (100°F).",
         "3. Vapor pressure in psia."], lang))
    b.append(N(
        "Ghi chú về nguồn: “- - -” biểu thị giá trị không được liệt kê. Một số "
        "công thức giữ nguyên lỗi OCR (NH4CI, CCI4, C12H22011, v.v.) và tên "
        "“Mangesium Chloride(1)” được giữ như bản gốc. Dòng Methyl Bromide "
        "thiếu một giá trị áp suất tới hạn trong nguồn.",
        "Source note: “- - -” marks values not listed. Some formulas retain "
        "OCR spellings (NH4CI, CCI4, C12H22011, etc.) and the name “Mangesium "
        "Chloride(1)” is kept as printed. The Methyl Bromide row lacks a "
        "critical-pressure value in the source.", lang))

    return "".join(b)
