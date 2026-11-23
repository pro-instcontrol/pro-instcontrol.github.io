# -*- coding: utf-8 -*-
"""Sections 15.8-15.10 — Mass / Pressure equivalents / psi-to-bar."""
from cvh15_common import T, H, P, LEAD, B, N, TB

# ---------------------------------------------------------------------------
# 15.8 — Mass Conversion: Pounds to Kilograms
#
# Lookup grid: columns are the units digit 0-9 pounds, rows are the tens digit
# 0,10,...90 pounds. The value at each intersection is kilograms. Column
# header digits and row labels are printed verbatim; values are kept exactly
# as printed (two decimals, including trailing zeros).
# ---------------------------------------------------------------------------
_MASS_ROWS = [
    ("0",  "0.00",  "0.45",  "0.91",  "1.36",  "1.81",  "2.27",  "2.72",  "3.18",  "3.63",  "4.08"),
    ("10", "4.54",  "4.99",  "5.44",  "5.90",  "6.35",  "6.80",  "7.26",  "7.71",  "8.16",  "8.62"),
    ("20", "9.07",  "9.53",  "9.98",  "10.43", "10.89", "11.34", "11.79", "12.25", "12.70", "13.15"),
    ("30", "13.61", "14.06", "14.52", "14.97", "15.42", "15.88", "16.33", "16.78", "17.24", "17.69"),
    ("40", "18.14", "18.60", "19.05", "19.50", "19.96", "20.41", "20.87", "21.32", "21.77", "22.23"),
    ("50", "22.68", "23.13", "23.59", "24.04", "24.49", "24.95", "25.40", "25.86", "26.31", "26.76"),
    ("60", "27.22", "27.67", "28.12", "28.58", "29.03", "29.48", "29.94", "30.39", "30.84", "31.30"),
    ("70", "31.75", "32.21", "32.66", "33.11", "33.57", "34.02", "34.47", "34.93", "35.38", "35.83"),
    ("80", "36.29", "36.74", "37.20", "37.65", "38.10", "38.56", "39.01", "39.46", "39.92", "40.37"),
    ("90", "40.82", "41.28", "41.73", "42.18", "42.64", "43.09", "43.55", "44.00", "44.45", "44.91"),
]
_MASS_HDR_VI = ["Pound / Kilôgam", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
_MASS_HDR_EN = ["Pound / Kilogram", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

# ---------------------------------------------------------------------------
# 15.9 — Pressure Equivalents
#
# Square multiplier matrix. Row labels (unit names) and every factor are kept
# language-neutral and verbatim in the shared rows; only the eight column
# headers are localized. The corner cell indicates row=From, column=To.
# ---------------------------------------------------------------------------
_PRESSURE_ROWS = [
    ("Kg. Per Sq. Cm.", "1",        "14.22",   "0.9678",   "0.98067", "28.96",  "98.067",  "394.05", "32.84"),
    ("Lb. Per Sq. In.", "0.07031",  "1",       "0.06804",  "0.06895", "2.036",  "6.895",   "27.7",   "2.309"),
    ("Atm.",            "1.0332",   "14.696",  "1",        "1.01325", "29.92",  "101.325", "407.14", "33.93"),
    ("Bar",             "1.01972",  "14.5038", "0.98692",  "1",       "29.53",  "100",     "402.156","33.513"),
    ("In. of Hg.",      "0.03453",  "0.4912",  "0.03342",  "0.033864","1",      "3.3864",  "13.61",  "11.134"),
    ("Kilopascals",     "0.0101972","0.145038","0.0098696","0.01",    "0.2953", "1",       "4.02156","0.33513"),
    ("In. of Water",    "0.002538", "0.0361",  "0.002456", "0.00249", "0.07349","0.249",   "1",      "0.0833"),
    ("Ft. of Water",    "0.03045",  "0.4332",  "0.02947",  "0.029839","0.8819", "2.9839",  "12",     "1"),
]
_PRESSURE_HDR_VI = ["Từ / Đến", "Kg. trên cm²", "Lb. trên in²", "Atm.", "Bar",
                    "In. của Hg.", "Kilopascal", "In. của nước", "Ft. của nước"]
_PRESSURE_HDR_EN = ["From / To", "Kg. Per Sq. Cm.", "Lb. Per Sq. In.", "Atm.", "Bar",
                    "In. of Hg.", "Kilopascals", "In. of Water", "Ft. of Water"]

# ---------------------------------------------------------------------------
# 15.10 — Pressure Conversion: Pounds Per Square Inch to Bar
#
# Printed as two side-by-side halves split by a page break (columns 0-4 and
# columns 5-9); both halves are reproduced as separate tables. Rows are psi
# tens 0..100, column digits are psi units, values are bar printed to six
# decimals. The two notes are repeated after each half in the source.
# ---------------------------------------------------------------------------
_PSI_BAR_A_ROWS = [
    ("0",   "0.000000", "0.068948", "0.137895", "0.206843", "0.275790"),
    ("10",  "0.689476", "0.758423", "0.827371", "0.896318", "0.965266"),
    ("20",  "1.378951", "1.447899", "1.516847", "1.585794", "1.654742"),
    ("30",  "2.068427", "2.137375", "2.206322", "2.275270", "2.344217"),
    ("40",  "2.757903", "2.826850", "2.895798", "2.964746", "3.033693"),
    ("50",  "3.447379", "3.516326", "3.585274", "3.654221", "3.723169"),
    ("60",  "4.136854", "4.205802", "4.274750", "4.343697", "4.412645"),
    ("70",  "4.826330", "4.895278", "4.964225", "5.033173", "5.102120"),
    ("80",  "5.515806", "5.584753", "5.653701", "5.722649", "5.791596"),
    ("90",  "6.205282", "6.274229", "6.343177", "6.412124", "6.481072"),
    ("100", "6.894757", "6.963705", "7.032652", "7.101600", "7.170548"),
]
_PSI_BAR_B_ROWS = [
    ("0",   "0.344738", "0.413685", "0.482633", "0.551581", "0.620528"),
    ("10",  "1.034214", "1.103161", "1.172109", "1.241056", "1.310004"),
    ("20",  "1.723689", "1.792637", "1.861584", "1.930532", "1.999480"),
    ("30",  "2.413165", "2.482113", "2.551060", "2.620008", "2.688955"),
    ("40",  "3.102641", "3.171588", "3.240536", "3.309484", "3.378431"),
    ("50",  "3.792117", "3.861064", "3.930012", "3.998959", "4.067907"),
    ("60",  "4.481592", "4.550540", "4.619487", "4.688435", "4.757383"),
    ("70",  "5.171068", "5.240016", "5.308963", "5.377911", "5.446858"),
    ("80",  "5.860544", "5.929491", "5.998439", "6.067386", "6.136334"),
    ("90",  "6.550019", "6.618967", "6.687915", "6.756862", "6.825810"),
    ("100", "7.239495", "7.308443", "7.377390", "7.446338", "7.515285"),
]
_PSI_HDR_VI_A = ["psi / Bar", "0", "1", "2", "3", "4"]
_PSI_HDR_EN_A = ["psi / Bar", "0", "1", "2", "3", "4"]
_PSI_HDR_VI_B = ["psi / Bar", "5", "6", "7", "8", "9"]
_PSI_HDR_EN_B = ["psi / Bar", "5", "6", "7", "8", "9"]

_PSI_NOTE1_VI = ("Lưu ý: Để đổi sang kilopascal, dời dấu thập phân hai vị trí sang phải; "
                 "để đổi sang Megapascal, dời dấu thập phân một vị trí sang trái. "
                 "Ví dụ, 30 psi = 2.068427 bar = 206.8427 kPa = 0.2068427 MPa.")
_PSI_NOTE1_EN = ("Note: To convert to kilopascals, move decimal point two positions to right; "
                 "to convert to Megapascals, move decimal point one position to left. "
                 "For example, 30 psi = 2.068427 bar = 206.8427 kPa = 0.2068427 MPa.")
_PSI_NOTE2_VI = "Lưu ý: Làm tròn các chữ số thập phân để độ chính xác không vượt quá mức mong muốn."
_PSI_NOTE2_EN = "Note: Round off decimal points to provide no more than the desired degree of accuracy."


def section(lang):
    b = []

    # ---- 15.8 ------------------------------------------------------------
    b.append(H("15.8 Chuyển đổi khối lượng — Pound sang Kilôgam",
               "15.8 Mass Conversion–Pounds to Kilograms", lang))
    b.append(LEAD("Hàng và cột được tính theo pound (hàng: chục pound, cột: đơn vị pound); "
                  "giá trị tại giao điểm là kilôgam.",
                  "Rows and columns are in pounds (rows: tens of pounds, columns: units of "
                  "pounds); the value at the intersection is kilograms.",
                  lang))
    b.append(TB(_MASS_HDR_VI, _MASS_HDR_EN, _MASS_ROWS, lang,
                cap_vi="Bảng 15.8 · Chuyển đổi khối lượng từ pound sang kilôgam.",
                cap_en="Table 15.8 · Mass conversion from pounds to kilograms."))

    # ---- 15.9 ------------------------------------------------------------
    b.append(H("15.9 Đương lượng áp suất", "15.9 Pressure Equivalents", lang))
    b.append(N("Lưu ý: Dùng hệ số nhân tại giao điểm của hàng và cột.",
               "Note: Use the multiplier at the convergence of the row and column.", lang))
    b.append(TB(_PRESSURE_HDR_VI, _PRESSURE_HDR_EN, _PRESSURE_ROWS, lang,
                cap_vi="Bảng 15.9 · Bảng hệ số nhân đương lượng áp suất.",
                cap_en="Table 15.9 · Pressure equivalents multiplier matrix."))
    b.append(N("1 ounce/sq. inch = 0.0625 lbs./sq. inch",
               "1 ounce/sq. inch = 0.0625 lbs./sq. inch", lang))

    # ---- 15.10 -----------------------------------------------------------
    b.append(H("15.10 Chuyển đổi áp suất — Pound trên inch vuông sang Bar",
               "15.10 Pressure Conversion–Pounds Per Square Inch to Bar", lang))
    b.append(LEAD("Hàng và cột tính theo pound trên inch vuông (psi); giá trị tại giao điểm là bar.",
                  "Rows and columns are in pounds per square inch (psi); the value at the "
                  "intersection is bar.", lang))
    b.append(TB(_PSI_HDR_VI_A, _PSI_HDR_EN_A, _PSI_BAR_A_ROWS, lang,
                cap_vi="Bảng 15.10 · Chuyển đổi psi sang bar (cột 0–4).",
                cap_en="Table 15.10 · psi-to-bar conversion (columns 0–4)."))
    b.append(N(_PSI_NOTE1_VI, _PSI_NOTE1_EN, lang))
    b.append(N(_PSI_NOTE2_VI, _PSI_NOTE2_EN, lang))
    b.append(P("(tiếp theo)", "(continued)", lang))
    b.append(TB(_PSI_HDR_VI_B, _PSI_HDR_EN_B, _PSI_BAR_B_ROWS, lang,
                cap_vi="Bảng 15.10 (tiếp theo) · Chuyển đổi psi sang bar (cột 5–9).",
                cap_en="Table 15.10 (continued) · psi-to-bar conversion (columns 5–9)."))
    b.append(N(_PSI_NOTE1_VI, _PSI_NOTE1_EN, lang))
    b.append(N(_PSI_NOTE2_VI, _PSI_NOTE2_EN, lang))

    return "".join(b)
