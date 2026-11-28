# -*- coding: utf-8 -*-
"""Tables 14.4 and 14.5 of McMillan Chapter 14, bilingual EN/VI.

Transcribed from the authoritative page renders:
  - PDF p.460 / printed p.439 -> Table 14.4 + source line + printed Note
  - PDF p.465 / printed p.444 -> Table 14.5 + source line
Cross-checked against work/mcmillan_ch14_survey_b.md §4 (read in full).
The OCR text layer garbles the '±' signs in both tables; the render governs.

Structure follows build/mcmillan_tbl13_1_4.py: HEAD is one cell per column,
ROWS is a list of equal-length cell lists, CAPTION and NOTE are localized.
Multi-line headers and the three-line caption of Table 14.5 are carried with
'<br>' so the flat HEAD/ROWS shape stays intact.

Table 14.4 prints the word 'Note' in both numeric columns of the E10 row, and
Table 14.5 carries the connector words 'in air' and 'in nitrogen'; both tables
therefore export genuine language-specific ROWS lists. ROWS144 / ROWS145 hold
the printed English values; the VI bodies must use ROWS144_VI / ROWS145_VI.
"""

# ---------------------------------------------------------------------------
# Table 14.4 — printed p.439 (PDF p.460)
# ---------------------------------------------------------------------------

CAPTION144_EN = "Table 14.4 Torque tests for screw lampholders"
CAPTION144_VI = "Bảng 14.4 Thử nghiệm mô-men xoắn cho đui đèn kiểu vặn"

HEAD144_EN = [
    "Lamp cap size",
    "Insertion torque<br>Nm",
    "Minimum removal<br>torque<br>Nm",
]
HEAD144_VI = [
    "Cỡ đui đèn",
    "Mô-men xoắn khi lắp<br>Nm",
    "Mô-men xoắn tháo ra<br>tối thiểu<br>Nm",
]

# 3 cells per row: lamp cap size + insertion torque + minimum removal torque.
ROWS144 = [
    ["E10", "Note", "Note"],
    ["E14", "1.0 ± 0.1", "0.3"],
    ["E27", "1.5 ± 0.1", "0.5"],
    ["E40", "3.0 ± 0.1", "1.0"],
]
ROWS144_EN = [
    ["E10", "Note", "Note"],
    ["E14", "1.0 ± 0.1", "0.3"],
    ["E27", "1.5 ± 0.1", "0.5"],
    ["E40", "3.0 ± 0.1", "1.0"],
]
# The E10 cells print the English word 'Note' (a cross-reference to the
# footnote), so the VI rows are exported separately; all other cells are
# numeric or symbolic and stay unchanged.
ROWS144_VI = [
    ["E10", "Ghi chú", "Ghi chú"],
    ["E14", "1.0 ± 0.1", "0.3"],
    ["E27", "1.5 ± 0.1", "0.5"],
    ["E40", "3.0 ± 0.1", "1.0"],
]

NOTE144_EN = (
    "<p>(from BS/EN 50019)</p>"
    "<p>Note: No test is considered as necessary for this small size of lamp.</p>"
    "<p>Translator note: the second header prints 'Insertion torque' with "
    "'Nm' on a second line; the third prints 'Minimum removal torque' over "
    "three lines with 'Nm' last. The E10 row prints the word 'Note' in both "
    "numeric columns, referring to the printed Note below the rule. The "
    "source line and the Note are italicised in print.</p>"
)
NOTE144_VI = (
    "<p>(theo BS/EN 50019)</p>"
    "<p>Ghi chú: Không cần thực hiện thử nghiệm nào cho cỡ đèn nhỏ này.</p>"
    "<p>Ghi chú của người dịch: tiêu đề thứ hai in 'Insertion torque' với "
    "'Nm' ở dòng thứ hai; tiêu đề thứ ba in 'Minimum removal torque' trên "
    "ba dòng, với 'Nm' ở dòng cuối. Hàng E10 in chữ 'Note' ở cả hai cột số, "
    "viện dẫn đến dòng Ghi chú in bên dưới vạch kẻ. Dòng nguồn và dòng Ghi "
    "chú được in nghiêng.</p>"
)

# ---------------------------------------------------------------------------
# Table 14.5 — printed p.444 (PDF p.465)
# ---------------------------------------------------------------------------

# The caption is printed on three lines; the line breaks are kept with '<br>'.
CAPTION145_EN = (
    "Table 14.5 Test mixtures for flame transmission in"
    "<br>enclosed break devices and non-incendive"
    "<br>components"
)
CAPTION145_VI = (
    "Bảng 14.5 Hỗn hợp thử truyền ngọn lửa trong"
    "<br>thiết bị ngắt kín và linh kiện"
    "<br>không gây cháy"
)

HEAD145_EN = [
    "Sub-group",
    "Test gas mixture",
]
HEAD145_VI = [
    "Phân nhóm",
    "Hỗn hợp khí thử",
]

# 2 cells per row: sub-group + test gas mixture. Connector words in the
# second cell require genuine language-specific rows.
ROWS145 = [
    ["IIA", "6.5 ± 0.5% ethylene in air"],
    ["IIB", "28.2 ± 2% hydrogen in air"],
    ["IIC", "34 ± 2% hydrogen/17 ± 1% oxygen in nitrogen"],
]
ROWS145_EN = [
    ["IIA", "6.5 ± 0.5% ethylene in air"],
    ["IIB", "28.2 ± 2% hydrogen in air"],
    ["IIC", "34 ± 2% hydrogen/17 ± 1% oxygen in nitrogen"],
]
ROWS145_VI = [
    ["IIA", "6.5 ± 0.5% etylen trong không khí"],
    ["IIB", "28.2 ± 2% hydro trong không khí"],
    ["IIC", "34 ± 2% hydro/17 ± 1% oxy trong nitơ"],
]

NOTE145_EN = (
    "<p>(from BS 6941)</p>"
    "<p>Translator note: the caption is printed on three lines "
    "('transmission in' / 'non-incendive' / 'components'); the unbroken "
    "wording is preserved across the '<br>' breaks. The gas-mixture cells "
    "retain the printed '±' tolerances, '%' signs and the '/' separator in "
    "the IIC row. No Note is printed beneath this table; the source line is "
    "italicised in print.</p>"
)
NOTE145_VI = (
    "<p>(theo BS 6941)</p>"
    "<p>Ghi chú của người dịch: nhan đề được in trên ba dòng "
    "('transmission in' / 'non-incendive' / 'components'); cách viết liền "
    "được giữ nguyên qua các ngắt dòng '<br>'. Các ô hỗn hợp khí giữ nguyên "
    "dung sai '±', dấu '%' và dấu '/' trong hàng IIC. Không có dòng Ghi chú "
    "nào được in bên dưới bảng này; dòng nguồn được in nghiêng.</p>"
)
