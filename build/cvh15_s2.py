# -*- coding: utf-8 -*-
"""Sections 15.5-15.7 — Area / Volume / Volume Rate equivalents."""
from cvh15_common import T, H, P, LEAD, B, N, TB

# ---------------------------------------------------------------------------
# 15.5 — Area Equivalents
#
# Multiplier matrix.  The multiplier at the intersection of a row and a column
# converts the ROW unit into the COLUMN unit.  Source prints a blank top-left
# corner; it is kept blank in both header lists.  Row labels are unit names and
# are transcribed verbatim (including the printed "Square Killometers" typo).
_AREA_ROWS = [
    ("Square Meters",      "1",         "1549.99",   "10.7639",  "3.861 x 10−7",  "1 x 10−6"),
    ("Square Inches",      "0.0006452", "1",         "6.944 x 10−3", "2.491 x 10−10", "6.452 x 10−10"),
    ("Square Feet",        "0.0929",    "144",       "1",        "3.587x 10−8",   "9.29 x 10−8"),
    ("Square Miles",       "2,589,999", "---",       "27,878,400", "1",           "2.59"),
    ("Square Killometers", "1,000,000", "---",       "10,763,867", "0.3861",      "1"),
]

_AREA_HDR_VI = ["", "Mét vuông", "Inch vuông", "Foot vuông", "Dặm vuông", "Km vuông"]
_AREA_HDR_EN = ["", "Square Meters", "Square Inches", "Square Feet",
                "Square Miles", "Square Kilometers"]

_AREA_NOTES_VI = [
    "1 mét vuông = 10,000 cm vuông.",
    "1 mm vuông = 0.01 cm vuông = 0.00155 inch vuông.",
]
_AREA_NOTES_EN = [
    "1 square meter = 10,000 square centimeters.",
    "1 square millimeter = 0.01 square centimeter = 0.00155 square inches.",
]

# ---------------------------------------------------------------------------
# 15.6 — Volume Equivalents
#
# Multiplier matrix; column order as printed:
#   Cubic Decimeters (Liters) | Cubic Inches | Cubic Feet | U.S. Quart |
#   U.S. Gallon | Imperial Gallon | U.S. Barrel (Petroleum)
_VOLUME_ROWS = [
    ("Cubic Decimeters (Liters)", "1",        "61.0234", "0.03531",  "1.05668",  "0.264178", "0.220083", "0.00629"),
    ("Cubic Inches",              "0.01639",  "1",       "5.787 x 10−4", "0.01732", "0.004329", "0.003606", "0.000103"),
    ("Cubic Feet",                "28.317",   "1728",    "1",        "29.9221",  "7.48055",  "6.22888",  "0.1781"),
    ("U.S. Quart",                "0.94636",  "57.75",   "0.03342",  "1",        "0.25",     "0.2082",   "0.00595"),
    ("U.S. Gallon",               "3.78543",  "231",     "0.13368",  "4",        "1",        "0.833",    "0.02381"),
    ("Imperial Gallon",           "4.54374",  "277.274", "0.16054",  "4.80128",  "1.20032",  "1",        "0.02877"),
    ("U.S. Barrel (Petroleum)",   "158.98",   "9702",    "5.6146",   "168",      "42",       "34.973",   "1"),
]

_VOLUME_HDR_VI = ["", "Decimét khối (Lít)", "Inch khối", "Foot khối",
                  "Quart Mỹ", "Gallon Mỹ", "Gallon Anh", "Thùng Mỹ (Dầu mỏ)"]
_VOLUME_HDR_EN = ["", "Cubic Decimeters (Liters)", "Cubic Inches", "Cubic Feet",
                  "U.S. Quart", "U.S. Gallon", "Imperial Gallon", "U.S. Barrel (Petroleum)"]

_VOLUME_NOTES_VI = [
    "1 mét khối = 1,000,000 cm khối.",
    "1 lít = 1000 mililít = 1000 cm khối.",
]
_VOLUME_NOTES_EN = [
    "1 cubic meter = 1,000,000 cubic centimeters.",
    "1 liter = 1000 milliliters = 1000 cubic centimeters.",
]

# ---------------------------------------------------------------------------
# 15.7 — Volume Rate Equivalents
#
# Multiplier matrix; column order as printed:
#   Liters Per Minute | Cubic Meters Per Hour | Cubic Feet Per Hour |
#   Liters Per Hour | U.S. Gallon Per Minute | U.S. Barrel Per Day
_RATE_ROWS = [
    ("Liters Per Minute",      "1",        "0.06",     "2.1189",  "60",     "0.264178", "9.057"),
    ("Cubic Meters Per Hour",  "16.667",   "1",        "35.314",  "1000",   "4.403",    "151"),
    ("Cubic Feet Per Hour",    "0.4719",   "0.028317", "1",       "28.317", "0.1247",   "4.2746"),
    ("Liters Per Hour",        "0.016667", "0.001",    "0.035314", "1",     "0.004403", "0.151"),
    ("U.S. Gallon Per Minute", "3.785",    "0.2273",   "8.0208",  "227.3",  "1",        "34.28"),
    ("U.S. Barrel Per Day",    "0.1104",   "0.006624", "0.23394", "6.624",  "0.02917",  "1"),
]

_RATE_HDR_VI = ["", "Lít trên phút", "Mét khối trên giờ", "Foot khối trên giờ",
                "Lít trên giờ", "Gallon Mỹ trên phút", "Thùng Mỹ trên ngày"]
_RATE_HDR_EN = ["", "Liters Per Minute", "Cubic Meters Per Hour", "Cubic Feet Per Hour",
                "Liters Per Hour", "U.S. Gallon Per Minute", "U.S. Barrel Per Day"]


def section(lang):
    b = []

    # ---- 15.5 ------------------------------------------------------------
    b.append(H("15.5 Hệ số quy đổi diện tích",
               "15.5 Area Equivalents",
               lang))
    b.append(N("Lưu ý: Dùng hệ số nhân tại giao điểm của hàng và cột.",
               "Note: Use multiplier at convergence of row and column.",
               lang))
    b.append(TB(_AREA_HDR_VI, _AREA_HDR_EN, _AREA_ROWS, lang,
                cap_vi="Bảng 15.5 · Hệ số quy đổi diện tích (bảng hệ số nhân).",
                cap_en="Table 15.5 · Area equivalents (multiplier matrix)."))
    b.append(B(_AREA_NOTES_VI, _AREA_NOTES_EN, lang))

    # ---- 15.6 ------------------------------------------------------------
    b.append(H("15.6 Hệ số quy đổi thể tích",
               "15.6 Volume Equivalents",
               lang))
    b.append(N("Lưu ý: Dùng hệ số nhân tại giao điểm của hàng và cột.",
               "Note: Use multiplier at convergence of row and column.",
               lang))
    b.append(TB(_VOLUME_HDR_VI, _VOLUME_HDR_EN, _VOLUME_ROWS, lang,
                cap_vi="Bảng 15.6 · Hệ số quy đổi thể tích (bảng hệ số nhân).",
                cap_en="Table 15.6 · Volume equivalents (multiplier matrix)."))
    b.append(B(_VOLUME_NOTES_VI, _VOLUME_NOTES_EN, lang))

    # ---- 15.7 ------------------------------------------------------------
    b.append(H("15.7 Hệ số quy đổi lưu lượng thể tích",
               "15.7 Volume Rate Equivalents",
               lang))
    b.append(N("Lưu ý: Dùng hệ số nhân tại giao điểm của hàng và cột.",
               "Note: Use multiplier at convergence of row and column.",
               lang))
    b.append(TB(_RATE_HDR_VI, _RATE_HDR_EN, _RATE_ROWS, lang,
                cap_vi="Bảng 15.7 · Hệ số quy đổi lưu lượng thể tích (bảng hệ số nhân).",
                cap_en="Table 15.7 · Volume rate equivalents (multiplier matrix)."))

    return "".join(b)
