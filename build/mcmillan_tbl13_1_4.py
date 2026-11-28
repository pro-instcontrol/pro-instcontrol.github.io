# -*- coding: utf-8 -*-
"""Tables 13.1 to 13.4 of McMillan Chapter 13, bilingual EN/VI.

Transcribed from the authoritative page renders:
  - PDF p.363 / printed p.342 -> Table 13.1 + italic source line
  - PDF p.365 / printed p.344 -> Table 13.2 + source line + Note
  - PDF p.375 / printed p.354 -> Table 13.3
  - PDF p.375 / printed p.354 -> Table 13.4 + source line + Note

Cross-checked against work/ch13_survey_a.md §4 and work/ch13_survey_b.md §4.
The text layer is materially garbled in all four tables (e.g. '±' read as 'f'
or 'i', '(% V/V)' as '(Yo W)', '≥' as 't', '(mm²)' as '(m2)'); the page images
govern throughout.

Structure follows mcmillan_tbl12_1_4.py: HEAD is one cell per column, ROWS is
a list of equal-length cell lists, CAPTION and NOTE are localized. Spanning
over-headers are carried as extra lines of CAPTION so the flat HEAD/ROWS shape
stays intact:
  * 13.1 / 13.2: 'Calibration' spans the two calibration sub-columns;
  * 13.4: 'Maximum permissible rms wire current ... (Amps)' spans T4–T6.

Rows are shared only where every cell is numeric/symbolic (13.1 uses 'N/A',
13.4 is entirely numeric). Table 13.2 prints the word 'None' and Table 13.3
prints connector words, so both export genuine Vietnamese row lists.

Printed quirks retained deliberately (with bilingual translator notes):

  * 13.1 title uses an en dash before 'with electrical safety factors'; the
    sub-heads print lowercase 'current' and 'energy';
  * 13.2 sub-heads instead print 'Current' and 'Energy' with capitals; each
    sub-group occupies two rows and absent gases print 'None', not 'N/A';
  * 13.3 row 3 repeats '≥20 mm²' (the lower bound of row 2), and the four
    'at ... Ambient' lines are separate lines in the final cell;
  * 13.4 caption is hyphenated 'relation- / ship' and 'temper- / ature' over
    three print lines, '40°C' prints without a space, and the 0.5 mm row has
    T6 (6.7) lower than T5 (6.9).
"""

# ---------------------------------------------------------------------------
# Table 13.1 — printed p.342 (PDF p.363)
# ---------------------------------------------------------------------------

CAPTION131_EN = (
    "Table 13.1 Test mixtures and ignition currents/energies "
    "(normal tests – with electrical safety factors)"
    "<br>Calibration"
)
CAPTION131_VI = (
    "Bảng 13.1 Hỗn hợp thử và dòng/năng lượng đánh lửa "
    "(thử nghiệm thường – có hệ số an toàn điện)"
    "<br>Hiệu chuẩn"
)

HEAD131_EN = [
    "Sub-group",
    "Hydrogen<br>(% V/V)",
    "Ethylene<br>(% V/V)",
    "Propane<br>(% V/V)",
    "current<br>(mA)",
    "energy<br>(μJ)",
]
HEAD131_VI = [
    "Phân nhóm",
    "Hydro<br>(% V/V)",
    "Ethylene<br>(% V/V)",
    "Propane<br>(% V/V)",
    "dòng điện<br>(mA)",
    "năng lượng<br>(μJ)",
]

# 6 cells per row: sub-group + three gas mixtures + calibration current/energy.
ROWS131 = [
    ["IIA", "N/A", "N/A", "5.25 ± 0.25", "100", "475"],
    ["IIB", "N/A", "7.8 ± 0.5", "N/A", "65", "201"],
    ["IIC", "21 ± 2", "N/A", "N/A", "30", "43"],
]
ROWS131_EN = ROWS131
# Sub-group codes, 'N/A' and numbers are symbolic; no connector words.
ROWS131_VI = ROWS131

NOTE131_EN = (
    "<p>(from BS/EN 50020)</p>"
    "<p>Translator note: the spanning over-header 'Calibration' covers the "
    "'current (mA)' and 'energy (μJ)' sub-columns and is carried in the "
    "caption (second line); each of the three gas columns carries '(% V/V)' "
    "on a second header line. The title wraps after 'normal tests –' and "
    "prints an en dash before 'with electrical safety factors'.</p>"
    "<p>Translator note: the sub-heads print lowercase 'current' and "
    "'energy', unlike Table 13.2 which prints 'Current' and 'Energy' with "
    "initial capitals; the energy unit prints the Greek letter mu in 'μJ'. "
    "'N/A' is printed in the IIA and IIB rows as shown. The OCR text layer "
    "read '±' as a stray 'f' and '(% V/V)' as '(Yo W)'; the render governs.</p>"
)

NOTE131_VI = (
    "<p>(theo BS/EN 50020)</p>"
    "<p>Ghi chú của người dịch: tiêu đề phía trên 'Calibration' trải rộng "
    "trên hai cột con 'current (mA)' và 'energy (μJ)' và được đưa vào dòng "
    "thứ hai của nhan đề; cả ba cột khí đều có '(% V/V)' ở dòng tiêu đề thứ "
    "hai. Nhan đề được ngắt dòng sau 'normal tests –' và in dấu gạch ngang "
    "kiểu en dash trước 'with electrical safety factors'.</p>"
    "<p>Ghi chú của người dịch: các tiêu đề phụ in thường 'current' và "
    "'energy', trái với Bảng 13.2 in 'Current' và 'Energy' với chữ cái đầu "
    "viết hoa; đơn vị năng lượng in chữ cái Hy Lạp mu trong 'μJ'. 'N/A' được "
    "in trong các hàng IIA và IIB như đã hiển thị. Lớp văn bản OCR đọc '±' "
    "thành một ký tự 'f' lạc đề và '(% V/V)' thành '(Yo W)'; ảnh trang in là "
    "nguồn quyết định.</p>"
)

# ---------------------------------------------------------------------------
# Table 13.2 — printed p.344 (PDF p.365)
# ---------------------------------------------------------------------------

CAPTION132_EN = (
    "Table 13.2 Test mixtures and ignition currents/energies "
    "(gas mixtures providing safety factors)"
    "<br>Calibration"
)
CAPTION132_VI = (
    "Bảng 13.2 Hỗn hợp thử và dòng/năng lượng đánh lửa "
    "(hỗn hợp khí tạo hệ số an toàn)"
    "<br>Hiệu chuẩn"
)

HEAD132_EN = [
    "Sub-group",
    "Hydrogen<br>(% V/V)",
    "Oxygen<br>(% V/V)",
    "Air<br>(% V/V)",
    "Current<br>(mA)",
    "Energy<br>(μJ)",
]
HEAD132_VI = [
    "Phân nhóm",
    "Hydro<br>(% V/V)",
    "Oxy<br>(% V/V)",
    "Không khí<br>(% V/V)",
    "Dòng điện<br>(mA)",
    "Năng lượng<br>(μJ)",
]

# 6 cells per row: sub-group + three gas mixtures + calibration current/energy.
ROWS132 = [
    ["IIA", "48 ± 2", "None", "52 ± 2", "67", "211"],
    ["IIA", "85 ± 2", "15 ± 2", "None", "67", "211"],
    ["IIB", "38 ± 2", "None", "62 ± 2", "43", "89"],
    ["IIB", "75 ± 2", "25 ± 2", "None", "43", "89"],
    ["IIC", "30 ± 2", "17 ± 2", "53 ± 2", "20", "19"],
    ["IIC", "60 ± 2", "None", "40 ± 2", "20", "19"],
]
ROWS132_EN = ROWS132
# 'None' is a printed English word: the VI rows carry its meaning.
ROWS132_VI = [
    ["IIA", "48 ± 2", "Không có", "52 ± 2", "67", "211"],
    ["IIA", "85 ± 2", "15 ± 2", "Không có", "67", "211"],
    ["IIB", "38 ± 2", "Không có", "62 ± 2", "43", "89"],
    ["IIB", "75 ± 2", "25 ± 2", "Không có", "43", "89"],
    ["IIC", "30 ± 2", "17 ± 2", "53 ± 2", "20", "19"],
    ["IIC", "60 ± 2", "Không có", "40 ± 2", "20", "19"],
]

NOTE132_EN = (
    "<p>(gas mixtures from BS/EN 50020)</p>"
    "<p>Note: These mixtures provide safety factors equivalent to a 1.5 "
    "safety factor on current or voltage.</p>"
    "<p>Translator note: the spanning over-header 'Calibration' covers the "
    "'Current (mA)' and 'Energy (μJ)' sub-columns and is carried in the "
    "caption (second line). Unlike Table 13.1, the sub-heads print 'Current' "
    "and 'Energy' with initial capitals. Each sub-group IIA, IIB and IIC is "
    "printed on two consecutive rows, and absent gases are marked 'None' "
    "rather than 'N/A'.</p>"
    "<p>Translator note: the OCR text layer read '±' as 'i' or 'f'; the "
    "render governs. The prose on printed p.343 cites 'Table 13.6 on page "
    "362' in this safety-factor context, but no Table 13.6 appears on "
    "printed p.362 (PDF p.363 carries Table 13.1); the erroneous citation "
    "is preserved in the prose.</p>"
)

NOTE132_VI = (
    "<p>(hỗn hợp khí theo BS/EN 50020)</p>"
    "<p>Ghi chú: Các hỗn hợp này cung cấp hệ số an toàn tương đương với hệ "
    "số an toàn 1.5 về dòng điện hoặc điện áp.</p>"
    "<p>Ghi chú của người dịch: tiêu đề phía trên 'Calibration' trải rộng "
    "trên hai cột con 'Current (mA)' và 'Energy (μJ)' và được đưa vào dòng "
    "thứ hai của nhan đề. Khác với Bảng 13.1, các tiêu đề phụ in 'Current' "
    "và 'Energy' với chữ cái đầu viết hoa. Mỗi phân nhóm IIA, IIB và IIC "
    "được in trên hai hàng liên tiếp và khí không có mặt được đánh dấu "
    "'None' thay vì 'N/A'.</p>"
    "<p>Ghi chú của người dịch: lớp văn bản OCR đọc '±' thành 'i' hoặc 'f'; "
    "ảnh trang in là nguồn quyết định. Phần văn bản trên trang in 343 trích "
    "dẫn 'Table 13.6 on page 362' trong ngữ cảnh hệ số an toàn này, nhưng "
    "không có Bảng 13.6 nào trên trang in 362 (PDF 363 có Bảng 13.1); "
    "trích dẫn sai này được giữ nguyên trong phần văn bản.</p>"
)

# ---------------------------------------------------------------------------
# Table 13.3 — printed p.354 (PDF p.375)
# ---------------------------------------------------------------------------

CAPTION133_EN = "Table 13.3 Temperature relaxations for small components and wiring"
CAPTION133_VI = "Bảng 13.3 Nới lỏng nhiệt độ cho linh kiện nhỏ và dây dẫn"

HEAD133_EN = [
    "Total surface area<br>(excluding wires)",
    "Requirement for T4 rating",
]
HEAD133_VI = [
    "Tổng diện tích bề mặt<br>(không tính dây)",
    "Yêu cầu đối với xếp hạng T4",
]

# 2 cells per row: surface area + requirement (with four line breaks in row 3).
ROWS133 = [
    ["<20 mm²", "Maximum permitted surface temperature = 275 °C"],
    ["≥20 mm² – < 10 cm²", "Maximum permitted surface temperature = 200 °C"],
    ["≥20 mm²",
     "Maximum power dissipation:"
     "<br>– at 40 °C Ambient = 1.3 watts"
     "<br>– at 60 °C Ambient = 1.2 watts"
     "<br>– at 80 °C Ambient = 1.0 watts"],
]
ROWS133_EN = ROWS133
ROWS133_VI = [
    ["<20 mm²", "Nhiệt độ bề mặt tối đa cho phép = 275 °C"],
    ["≥20 mm² – < 10 cm²", "Nhiệt độ bề mặt tối đa cho phép = 200 °C"],
    ["≥20 mm²",
     "Công suất tiêu tán tối đa:"
     "<br>– ở nhiệt độ môi trường 40 °C = 1.3 watts"
     "<br>– ở nhiệt độ môi trường 60 °C = 1.2 watts"
     "<br>– ở nhiệt độ môi trường 80 °C = 1.0 watts"],
]

NOTE133_EN = (
    "<p>Translator note: the third row prints '≥20 mm²', identical to the "
    "lower bound of the second row; '≥10 cm²' is the likely intended "
    "reading, but the printed anomaly is preserved. The four 'at ... "
    "Ambient' lines are separate lines inside the last cell of that row "
    "and are joined here with line breaks.</p>"
    "<p>Translator note: the second row boundary prints '≥20 mm² – < 10 "
    "cm²' with an en dash and spaces, and the temperature values print a "
    "space before '°C' (e.g. '275 °C'), while the power figures print "
    "'watts' in lowercase. The OCR text layer read '≥' as 't'; the render "
    "governs. No source line is printed beneath this table.</p>"
)

NOTE133_VI = (
    "<p>Ghi chú của người dịch: hàng thứ ba in '≥20 mm²', trùng với cận "
    "dưới của hàng thứ hai; '≥10 cm²' là cách đọc có thể định, nhưng "
    "bất thường trong bản in được giữ nguyên. Bốn dòng 'at ... Ambient' "
    "là các dòng riêng trong ô cuối của hàng đó và được nối bằng các ngắt "
    "dòng ở đây.</p>"
    "<p>Ghi chú của người dịch: ranh giới ở hàng thứ hai in '≥20 mm² – < "
    "10 cm²' với dấu gạch ngang kiểu en dash và các dấu cách, và các giá "
    "trị nhiệt độ in có dấu cách trước '°C' (ví dụ '275 °C'), còn công "
    "suất in 'watts' viết thường. Lớp văn bản OCR đọc '≥' thành 't'; ảnh "
    "trang in là nguồn quyết định. Không có dòng nguồn nào được in bên "
    "dưới bảng này.</p>"
)

# ---------------------------------------------------------------------------
# Table 13.4 — printed p.354 (PDF p.375)
# ---------------------------------------------------------------------------

CAPTION134_EN = (
    "Table 13.4 Current/temperature classification relationship for copper "
    "wire at 40°C ambient temperature"
    "<br>Maximum permissible rms wire current for temperature classification "
    "at 40°C ambient (Amps)"
)
CAPTION134_VI = (
    "Bảng 13.4 Mối quan hệ phân loại dòng điện/nhiệt độ cho dây đồng ở "
    "nhiệt độ môi trường 40°C"
    "<br>Dòng rms tối đa cho phép trong dây để phân loại nhiệt độ ở nhiệt "
    "độ môi trường 40°C (Amps)"
)

HEAD134_EN = [
    "Diameter of circular<br>wire (mm)",
    "Cross-sectional<br>area of any wire<br>(mm²)",
    "T4",
    "T5",
    "T6",
]
HEAD134_VI = [
    "Đường kính của dây tròn<br>(mm)",
    "Tiết diện của mọi dây<br>(mm²)",
    "T4",
    "T5",
    "T6",
]

# 5 cells per row: diameter + cross-sectional area + three class currents.
ROWS134 = [
    ["0.035", "0.000962", "0.53", "0.48", "0.43"],
    ["0.05", "0.00196", "1.04", "0.93", "0.84"],
    ["0.1", "0.00785", "2.1", "1.9", "1.7"],
    ["0.2", "0.0314", "3.7", "3.3", "3.0"],
    ["0.35", "0.0962", "6.4", "5.6", "5.0"],
    ["0.5", "0.196", "7.7", "6.9", "6.7"],
]
ROWS134_EN = ROWS134
# Every cell is numeric or a class code: no connector words to translate.
ROWS134_VI = ROWS134

NOTE134_EN = (
    "<p>(from BS/EN 50020)</p>"
    "<p>Note: While the diameter of the wire only refers to circular solid "
    "wires the cross-sectional areas apply to wire of any cross-section form "
    "including stranded and flat conductors. They do not apply, however, to "
    "printed circuit tracks and similar situations.</p>"
    "<p>Translator note: the caption is printed over three lines, hyphenated "
    "as 'relation- / ship' and 'temper- / ature'; the unhyphenated wording is "
    "given as one string. The spanning over-header 'Maximum permissible rms "
    "wire current for temperature classification at 40°C ambient (Amps)' "
    "covers the T4, T5 and T6 columns and is carried in the caption (second "
    "line); '40°C' prints without a space in both the caption and that "
    "over-header.</p>"
    "<p>Translator note: in the 0.5 mm row the printed T6 value (6.7) is "
    "lower than the T5 value (6.9) — a source anomaly preserved here. The "
    "OCR text layer garbled 'relationship' as 'relation ship' and read the "
    "header unit as '(m2)'; the render shows '(mm²)' and governs. The source "
    "line and the Note are italicised in print.</p>"
)

NOTE134_VI = (
    "<p>(theo BS/EN 50020)</p>"
    "<p>Ghi chú: Trong khi đường kính của dây chỉ áp dụng cho dây đặc rắn "
    "tròn, tiết diện áp dụng cho dây có mọi hình dạng tiết diện, kể cả dây "
    "bện và dây dẹt. Tuy nhiên, chúng không áp dụng cho các đường mạch in "
    "và các tình huống tương tự.</p>"
    "<p>Ghi chú của người dịch: nhan đề được in trên ba dòng, ngắt gạch nối "
    "thành 'relation- / ship' và 'temper- / ature'; cách viết không ngắt "
    "gạch nối được đưa thành một chuỗi. Tiêu đề phía trên 'Maximum "
    "permissible rms wire current for temperature classification at 40°C "
    "ambient (Amps)' trải rộng trên các cột T4, T5 và T6 và được đưa vào "
    "nhan đề (dòng thứ hai); '40°C' được in không có dấu cách cả trong "
    "nhan đề và trong tiêu đề đó.</p>"
    "<p>Ghi chú của người dịch: trong hàng 0.5 mm, giá trị T6 in là 6.7 "
    "thấp hơn giá trị T5 là 6.9 — bất thường trong bản in được giữ nguyên. "
    "Lớp văn bản OCR làm hỏng 'relationship' thành 'relation ship' và đọc "
    "đơn vị tiêu đề là '(m2)'; ảnh trang in cho '(mm²)' và là nguồn quyết "
    "định. Dòng nguồn và dòng Ghi chú được in nghiêng.</p>"
)
