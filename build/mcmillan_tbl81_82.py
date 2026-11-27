# -*- coding: utf-8 -*-
"""Tables 8.1 and 8.2 from McMillan Chapter 8.

Transcribed from the authoritative page renders:
  - printed p.185 / PDF p.206 -> Table 8.1
  - printed p.187 / PDF p.208 -> Table 8.2

The PDF text layer garbles Roman numerals, class marks, degree signs and degree
Fahrenheit values, so the page images govern every cell below. Printed quirks
are preserved deliberately (not silently corrected):

  * Table 8.1 US column prints "Class I" with a raised 2 in all four allocated
    rows; the text layer/OCR variously reads this as "Class I2", "Class I*" and
    "Class I'". The image shows the same raised 2 in every row, so "Class I²"
    is transcribed uniformly.
  * Historic UK FLP/GRP column prints Roman numerals II, III, IV, IV¹, IV¹.
  * "3n" in the German class column of the "All gases" row is printed as-is.
  * Lower-case "european" in the Table 8.1 caption is printed as-is.
  * Table 8.2 has no G6 and no note marker on the "Temperature system" column.
  * Printed Note 4 of Table 8.2 has no punctuation between "536 °F" and
    "Group C"; this is retained.
"""

# ---------------------------------------------------------------------------
# Table 8.1 — Current european grouping system
# ---------------------------------------------------------------------------

HEAD81_EN = [
    "Test gases",
    "European grouping",
    "Historic UK groups and classes<br>FLP/GRP and IS/CLS",
    "German class",
    "US groups and classes",
]

HEAD81_VI = [
    "Khí thử",
    "Phân nhóm châu Âu",
    "Nhóm và cấp theo hệ thống Anh lịch sử<br>FLP/GRP và IS/CLS",
    "Cấp theo hệ thống Đức",
    "Nhóm và cấp theo hệ thống Mỹ",
]

ROWS81 = [
    ["Propane", "IIA", "II / 2c", "1", "Class I²<br>Group D"],
    ["Ethylene", "IIB", "III / 2d", "2", "Class I²<br>Group C"],
    ["Hydrogen", "IIC", "IV / 2e", "3a", "Class I²<br>Group B"],
    ["Acetylene", "IIC", "IV¹ / 2f", "3c", "Class I²<br>Group A"],
    ["Carbon disulphide", "IIC", "IV¹ / 2f", "3b", "Not specifically allocated"],
    ["All gases", "", "", "3n", ""],
]

CAPTION81_EN = (
    "Current european grouping system showing relationship to historic German "
    "and UK systems and current USA system"
)

CAPTION81_VI = (
    "Hệ thống phân nhóm châu Âu hiện hành, thể hiện mối liên hệ với các hệ thống "
    "Đức và Anh lịch sử cùng hệ thống Mỹ hiện hành"
)

NOTE81_EN = (
    "<p>1 Although Group IV was allocated for these gases the Standard appropriate "
    "at the time (BS 229) excluded construction requirements for these gases and "
    "thus no equipment exists.</p>"
    "<p>2 Class I in the USA National Electrical Code was for gases, vapours and "
    "mists only. Dusts were Class II, and fibres and flyings Class III.</p>"
)

NOTE81_VI = (
    "<p>1 Mặc dù Nhóm IV đã được phân bổ cho các khí này, Tiêu chuẩn phù hợp tại "
    "thời điểm đó (BS 229) lại loại trừ các yêu cầu kết cấu đối với các khí này, "
    "vì vậy không có thiết bị nào tồn tại.</p>"
    "<p>2 Class I trong Bộ luật Điện Quốc gia Hoa Kỳ chỉ áp dụng cho khí, hơi và "
    "sương mù. Bụi thuộc Class II, còn sợi và mảnh bay thuộc Class III.</p>"
)

# ---------------------------------------------------------------------------
# Table 8.2 — European temperature classification system
# ---------------------------------------------------------------------------

HEAD82_EN = [
    "Temperature system",
    "European system (Note 1)",
    "Historic German system (Note 2)",
    "US systems – Current (Note 3)",
    "US systems – Historic (Notes 3 and 4)",
]

HEAD82_VI = [
    "Hệ thống nhiệt độ",
    "Hệ thống châu Âu (Ghi chú 1)",
    "Hệ thống Đức lịch sử (Ghi chú 2)",
    "Hệ thống Mỹ – Hiện hành (Ghi chú 3)",
    "Hệ thống Mỹ – Lịch sử (Ghi chú 3 và 4)",
]

ROWS82 = [
    ["450 °C", "T1", "G1", "T1 (842 °F)", "Groups A, B, C and D"],
    ["300 °C", "T2", "G2", "T2 (572 °F)", "Groups A, B, C and D"],
    ["", "", "", "T2A (536 °F)", "Groups A, B, C and D"],
    ["", "", "", "T2B (500 °F)", "Group C"],
    ["", "", "", "T2C (446 °F)", "Group C"],
    ["", "", "", "T2D (419 °F)", "Group C"],
    ["200 °C", "T3", "G3", "T3 (392 °F)", "Group C"],
    ["", "", "", "T3A (356 °F)", "Group C"],
    ["", "", "", "T3B (329 °F)", "–"],
    ["", "", "", "T3C (320 °F)", "–"],
    ["135 °C", "T4", "G4", "T4 (275 °F)", "–"],
    ["", "", "", "T4A (248 °F)", "–"],
    ["100 °C", "T5", "G5", "T5 (212 °F)", "–"],
    ["85 °C", "T6", "", "T6 (185 °F)", "–"],
]

CAPTION82_EN = (
    "European temperature classification system and its relationship with German "
    "and US systems"
)

CAPTION82_VI = (
    "Hệ thống phân loại nhiệt độ châu Âu và mối liên hệ với các hệ thống Đức và Mỹ"
)

NOTE82_EN = (
    "<p>1 The UK did not have a temperature classification system prior to the "
    "introduction of the European system.</p>"
    "<p>2 The historic German system did not have the equivalent of T6.</p>"
    "<p>3 The USA works on the Fahrenheit scale but the basic T classes are "
    "equivalent.</p>"
    "<p>4 The original US temperature classification was associated with its "
    "grouping system whereby the following was the case: Groups A and B were "
    "associated with a maximum temperature of 536 °F Group C was associated with "
    "a maximum temperature of 356 °F.</p>"
)

NOTE82_VI = (
    "<p>1 Anh Quốc không có hệ thống phân loại nhiệt độ trước khi hệ thống châu Âu "
    "được đưa vào sử dụng.</p>"
    "<p>2 Hệ thống Đức lịch sử không có cấp tương đương với T6.</p>"
    "<p>3 Hoa Kỳ sử dụng thang Fahrenheit nhưng các cấp T cơ bản là tương đương.</p>"
    "<p>4 Hệ thống phân loại nhiệt độ ban đầu của Hoa Kỳ gắn với hệ thống phân nhóm, "
    "cụ thể như sau: Các nhóm A và B liên quan đến nhiệt độ tối đa 536 °F; nhóm C "
    "liên quan đến nhiệt độ tối đa 356 °F.</p>"
)
