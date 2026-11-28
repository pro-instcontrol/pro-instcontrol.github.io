# -*- coding: utf-8 -*-
"""Tables 13.5 to 13.8 of McMillan Chapter 13, bilingual EN/VI.

Transcribed from the authoritative page renders:
  - PDF p.376 / printed p.355 -> Table 13.5 + source line, A/B/C legend and 5 Notes
  - PDF p.383 / printed p.362 -> Table 13.6 + source line and 2 Notes
  - PDF p.391 / printed p.370 -> Table 13.7 + legend and 3 Notes
  - PDF p.400 / printed p.379 -> Table 13.8 + legend and 2 Notes

Cross-checked against work/ch13_survey_b.md (Table 13.5 and 13.6),
work/ch13_survey_c.md (Table 13.7) and work/ch13_survey_d.md (Table 13.8).
The text layer is garbled in all four tables; the page images govern.

Structure follows mcmillan_tbl12_1_4.py: HEAD is one cell per column, ROWS is a
list of equal-length cell lists, CAPTION and NOTE are localized. Spanning
over-headers are carried as extra lines of CAPTION so the flat HEAD/ROWS shape
stays intact.

Table 13.5 has only numeric row cells, so its VI rows share the printed rows.
Tables 13.6, 13.7 and 13.8 contain connector words or printed word labels in
their row cells, so genuine Vietnamese row lists are exported alongside the
printed English rows.

Printed quirks retained deliberately (with bilingual translator notes):

  * 13.5 folds the spanning over-header 'Maximum permissible current for
    temperature classification shown (Amps)' into the caption; the T4/T5/T6
    groups and A/B/C sub-columns are flattened into paired HEAD cells;
  * 13.5 prints '01.3' (row 0.3, T6 A), '195.0' (row 0.3, T6 B, decimal point
    misplaced), '4.02' (row 1.5, T6 A, out of sequence) and '117.0' (row 3.0,
    T5 C, superfluous leading 1). Note 5 cross-references 'Table 13.2',
    which is a source cross-reference error (this is Table 13.5);
  * 13.6 prints its caption over two lines with a hyphenated line-break split
    ('evalua-tion') and uses en-dashes between cell-type names; the IEC codes
    for five rows print an en dash; the Zinc-Manganese-Dioxide entry spans two
    rows, the second parenthesised;
  * 13.7 prints literal 'Note 2' / 'Note 3' in place of CTI numbers and 'N/A'
    at the four highest voltages; the first column is plain numbers up to
    1575 and then '3.3 kV' ... '15.6 kV' with a space;
  * 13.8 prints the first-column voltages with a suffixed 'V' or 'KV' and no
    space ('10V' ... '15.6KV'); its legend abbreviates CTG as 'Coating' where
    Table 13.7 prints 'Conformal coating'; literal 'Note 1' / 'Note 2' and
    'N/A' occupy the CTI cells.
"""

# ---------------------------------------------------------------------------
# Table 13.5 — printed p.355 (PDF p.376)
# ---------------------------------------------------------------------------

CAPTION135_EN = (
    "Table 13.5 Minimum printed wiring widths for copper conductors of "
    "various thicknesses on insulating boards"
    "<br>Maximum permissible current for temperature classification shown "
    "(Amps)"
)
CAPTION135_VI = (
    "Bảng 13.5 Chiều rộng nhỏ nhất của đường dẫn in cho dây dẫn đồng có độ "
    "dày khác nhau trên bản mạch cách điện"
    "<br>Dòng điện tối đa cho phép theo phân loại nhiệt độ đã chỉ ra (Amps)"
)

HEAD135_EN = [
    "Minimum<br>track width<br>(mm)",
    "T4 A", "T4 B", "T4 C",
    "T5 A", "T5 B", "T5 C",
    "T6 A", "T6 B", "T6 C",
]
HEAD135_VI = [
    "Chiều rộng<br>đường mạch<br>(mm)",
    "T4 A", "T4 B", "T4 C",
    "T5 A", "T5 B", "T5 C",
    "T6 A", "T6 B", "T6 C",
]

# 10 cells per row: minimum track width + three temperature classes, each
# with A/B/C copper-thickness sub-columns. Every cell is numeric.
ROWS135 = [
    ["0.15", "0.8", "1.2", "1.56", "0.67", "1.0", "1.3", "0.6", "0.9", "1.1"],
    ["0.2", "1.2", "1.8", "2.3", "0.97", "1.45", "1.88", "0.87", "1.3", "1.69"],
    ["0.3", "1.87", "2.8", "3.64", "1.5", "2.25", "2.92", "01.3", "195.0", "2.53"],
    ["0.4", "2.4", "3.6", "4.68", "1.94", "2.9", "3.77", "1.67", "2.5", "3.25"],
    ["0.5", "2.94", "4.4", "5.72", "2.34", "3.5", "4.55", "2.01", "3.0", "3.9"],
    ["0.7", "3.81", "5.7", "7.41", "3.08", "4.6", "5.98", "2.74", "4.1", "5.33"],
    ["1.0", "5.02", "7.5", "9.75", "4.05", "6.05", "7.86", "3.61", "5.4", "7.02"],
    ["1.5", "6.56", "9.8", "12.7", "5.42", "8.1", "10.5", "4.02", "6.9", "8.97"],
    ["2.0", "8.04", "12.0", "15.6", "6.49", "9.7", "12.6", "5.62", "8.4", "10.9"],
    ["2.5", "9.04", "13.5", "17.5", "7.7", "11.5", "14.9", "6.43", "9.6", "12.4"],
    ["3.0", "10.7", "16.1", "20.9", "8.77", "13.1", "117.0", "7.7", "11.5", "14.9"],
    ["4.0", "13.0", "19.5", "25.3", "10.7", "16.1", "20.9", "9.58", "14.3", "18.5"],
    ["5.0", "15.2", "22.7", "29.5", "12.6", "18.9", "24.5", "11.1", "16.6", "21.5"],
    ["6.0", "17.2", "25.8", "33.5", "14.6", "21.8", "28.3", "12.6", "18.9", "24.5"],
]
ROWS135_EN = ROWS135
# Every cell is a width or a current figure: no connector words to translate.
ROWS135_VI = ROWS135

NOTE135_EN = (
    "<p>(from BS/EN 50020)</p>"
    "<p>A = 18µm copper tracks</p>"
    "<p>B = 35µm copper tracks</p>"
    "<p>C = 70µm copper tracks</p>"
    "<p>Notes:</p>"
    "<p>1 Where the pcb is at least 0.5mm and is less than 1.6mm thickness "
    "divide the above current figures by a factor of 1.2.</p>"
    "<p>2 Where the board is double-sided, divide the figures in the table by "
    "a factor of 1.5 and where the board is also of the lower thickness of "
    "Note 1, divide the figures in the Table by a factor of 1.8 instead of "
    "1.5.</p>"
    "<p>3 Where the board is a multilayer board divide the figures in the "
    "Table by a factor of 2 and the board layers also have a lower thickness "
    "as described in Note 1, divide the figures in the Table by 2.4 instead "
    "of 2.</p>"
    "<p>4 Divide the result of applying the Table and Notes 1,2 and 3 by a "
    "further factor of 1.5 where the printed circuit track passes under a "
    "component dissipating 0.25 watts or more.</p>"
    "<p>5 Divide the result of applying the Table and Notes 1, 2, 3 and 4 by "
    "a further factor of 2 if the track is additionally used to terminate a "
    "component dissipating 0.25 watts or more. Alternatively, widen the track "
    "at the point of termination and up to 1 mm from that point to 3 times "
    "that determined from Table 13.2 after the application of Notes 1, 2, 3 "
    "and 4 as appropriate.</p>"
    "<p>Translator note: the spanning over-header 'Maximum permissible current "
    "for temperature classification shown (Amps)' covers the nine current "
    "columns and is carried in the caption (second line). The T4, T5 and T6 "
    "group heads each split into A, B and C sub-columns and are flattened "
    "into paired HEAD cells; A/B/C are defined by the italic legend lines "
    "below the table.</p>"
    "<p>Translator note: four printed numeric anomalies are preserved verbatim "
    "and are confirmed in the render, not OCR noise: '01.3' with a leading "
    "zero (row 0.3, T6 A), '195.0' with a misplaced decimal point (row 0.3, "
    "T6 B), '4.02' out of sequence (row 1.5, T6 A) and '117.0' with a "
    "superfluous leading 1 (row 3.0, T5 C).</p>"
    "<p>Translator note: Note 5 cross-references 'Table 13.2'; this is a "
    "source cross-reference error because the applicable table is Table "
    "13.5. The source line and the 'Notes:' heading are italicised in print, "
    "and Note 1 prints '0.5mm' and '1.6mm' without spaces while Note 4 prints "
    "'1,2 and 3' without a space after the comma.</p>"
)

NOTE135_VI = (
    "<p>(theo BS/EN 50020)</p>"
    "<p>A = đường đồng 18µm</p>"
    "<p>B = đường đồng 35µm</p>"
    "<p>C = đường đồng 70µm</p>"
    "<p>Ghi chú:</p>"
    "<p>1 Khi pcb dày ít nhất 0,5mm và mỏng hơn 1,6mm, chia các số dòng điện "
    "trên cho hệ số 1,2.</p>"
    "<p>2 Khi bản mạch hai mặt, chia các số trong bảng cho hệ số 1,5; và khi "
    "bản mạch lại có độ dày thấp hơn như ở Ghi chú 1, chia các số trong Bảng "
    "cho hệ số 1,8 thay vì 1,5.</p>"
    "<p>3 Khi bản mạch nhiều lớp, chia các số trong Bảng cho hệ số 2; và nếu "
    "các lớp bản mạch cũng có độ dày thấp hơn như mô tả ở Ghi chú 1, chia các "
    "số trong Bảng cho 2,4 thay vì 2.</p>"
    "<p>4 Chia kết quả sau khi áp dụng Bảng và các Ghi chú 1,2 và 3 cho thêm "
    "hệ số 1,5 khi đường mạch in đi bên dưới linh kiện tiêu thụ công suất "
    "0,25 watt trở lên.</p>"
    "<p>5 Chia kết quả sau khi áp dụng Bảng và các Ghi chú 1, 2, 3 và 4 cho "
    "thêm hệ số 2 nếu đường dẫn còn được dùng để nối đầu vào của linh kiện "
    "tiêu thụ công suất 0,25 watt trở lên. Hoặc mở rộng đường dẫn tại điểm "
    "nối và trong khoảng tới 1 mm từ điểm đó lên 3 lần giá trị xác định từ "
    "Bảng 13.2 sau khi áp dụng phù hợp các Ghi chú 1, 2, 3 và 4.</p>"
    "<p>Ghi chú của người dịch: tiêu đề trải rộng 'Maximum permissible current "
    "for temperature classification shown (Amps)' phủ chín cột dòng điện "
    "được đưa vào dòng thứ hai của CAPTION. Các nhóm T4, T5, T6 mỗi nhóm "
    "chia thành các cột con A, B, C được gộp thành các ô HEAD ghép đôi; A/B/C "
    "được định nghĩa bởi các dòng chú thích in nghiêng bên dưới bảng.</p>"
    "<p>Ghi chú của người dịch: bốn bất thường số liệu trong bản in được giữ "
    "nguyên và đã được xác nhận trên ảnh trang, không phải nhiễu OCR: '01.3' "
    "có số 0 đứng đầu (hàng 0.3, T6 A), '195.0' với dấu thập phân bị lệch "
    "(hàng 0.3, T6 B), '4.02' nằm ngoài trình tự (hàng 1.5, T6 A) và '117.0' "
    "với chữ số 1 thừa ở đầu (hàng 3.0, T5 C).</p>"
    "<p>Ghi chú của người dịch: Ghi chú 5 dẫn đến 'Bảng 13.2'; đây là lỗi "
    "dẫn chiếu của tài liệu gốc vì bảng áp dụng là Bảng 13.5. Dòng nguồn và "
    "nhan đề 'Ghi chú:' được in nghiêng; Ghi chú 1 in '0.5mm' và '1.6mm' "
    "không có dấu cách, còn Ghi chú 4 in '1,2 và 3' không có dấu cách sau "
    "dấu phẩy.</p>"
)

# ---------------------------------------------------------------------------
# Table 13.6 — printed p.362 (PDF p.383)
# ---------------------------------------------------------------------------

CAPTION136_EN = (
    "Table 13.6 Output voltages of cells of various types to be used for "
    "evaluation of circuits using batteries"
)
CAPTION136_VI = (
    "Bảng 13.6 Điện áp đầu ra của các loại pin được dùng để đánh giá mạch "
    "sử dụng bộ pin"
)

HEAD136_EN = [
    "IEC type<br>Code",
    "Cell type<br>(chemical)",
    "Peak o/c voltage<br>for spark<br>ignition<br>(V)",
    "Nominal voltage<br>for hot surface<br>ignition<br>(V)",
]
HEAD136_VI = [
    "Mã loại<br>IEC",
    "Loại pin<br>(hóa học)",
    "Điện áp đỉnh mạch hở<br>để đánh lửa<br>bằng tia lửa<br>(V)",
    "Điện áp danh định<br>để đánh lửa bằng<br>bề mặt nóng<br>(V)",
]

# 4 cells per row: IEC code, cell type, peak o/c voltage, nominal voltage.
ROWS136_EN = [
    ["K", "Nickel Cadmium", "1.5", "1.3"],
    ["–", "Lead Acid (Wet)", "2.67", "2.2"],
    ["–", "Lead Acid (Dry) (See Note 1)", "2.35", "2.2"],
    ["L", "Alkaline – Manganese", "1.65", "1.5"],
    ["M", "Mercury – Zinc", "1.37", "1.35"],
    ["N", "Mercury – Manganese Dioxide – Zinc", "1.63", "1.4"],
    ["S", "Silver – Zinc", "1.6", "1.55"],
    ["A", "Zinc – Air", "1.55", "1.4"],
    ["C", "Lithium – Manganese Dioxide", "3.7", "3.0"],
    ["–", "Zinc – Manganese Dioxide", "1.735", "1.5"],
    ["–", "(Zinc – Carbon Leclanche)", "1.725", "1.5"],
    ["–", "Nickel – Hydride", "1.6", "1.3"],
]
ROWS136 = ROWS136_EN
ROWS136_VI = [
    ["K", "Niken cadmi", "1.5", "1.3"],
    ["–", "Chì axit (ướt)", "2.67", "2.2"],
    ["–", "Chì axit (khô) (Xem Ghi chú 1)", "2.35", "2.2"],
    ["L", "Kiềm – Mangan", "1.65", "1.5"],
    ["M", "Thủy ngân – Kẽm", "1.37", "1.35"],
    ["N", "Thủy ngân – Mangan dioxide – Kẽm", "1.63", "1.4"],
    ["S", "Bạc – Kẽm", "1.6", "1.55"],
    ["A", "Kẽm – Không khí", "1.55", "1.4"],
    ["C", "Lithium – Mangan dioxide", "3.7", "3.0"],
    ["–", "Kẽm – Mangan dioxide", "1.735", "1.5"],
    ["–", "(Kẽm – Carbon Leclanche)", "1.725", "1.5"],
    ["–", "Niken – Hydrua", "1.6", "1.3"],
]

NOTE136_EN = (
    "<p>(from BS/EN 50020)</p>"
    "<p>Notes:</p>"
    "<p>1 Dry Lead/acid cells are those with paste electrolytes which do not "
    "need electrolyte addition during their lives.</p>"
    "<p>2 Rechargeable cells such as nickel/cadmium or lead/acid may not "
    "achieve their maximum voltages on initial charge and thus may not "
    "achieve these voltages. They will, however, after two or three charges, "
    "and so if tests are carried out the cells should be cycled first.</p>"
    "<p>Translator note: the caption prints over two centred lines with a "
    "hyphenated line-break split ('evalua-tion'); the unhyphenated wording is "
    "given as one string. The header 'Peak o/c voltage for spark ignition "
    "(V)' abbreviates 'open circuit' as 'o/c' exactly as printed.</p>"
    "<p>Translator note: the cell-type names are separated by en dashes in "
    "print, except 'Nickel Cadmium', 'Lead Acid (Wet)' and 'Lead Acid (Dry) "
    "(See Note 1)'. Five IEC codes print an en dash. The Zinc – Manganese "
    "Dioxide entry spans two rows, the second parenthesised as '(Zinc – "
    "Carbon Leclanche)'. The source line and the 'Notes:' heading are "
    "italicised in print.</p>"
)

NOTE136_VI = (
    "<p>(theo BS/EN 50020)</p>"
    "<p>Ghi chú:</p>"
    "<p>1 Pin chì/axit khô là loại có chất điện giải dạng bột, không cần bổ "
    "sung chất điện giải trong suốt thời gian sử dụng.</p>"
    "<p>2 Các pin có thể sạc lại như niken/cadmi hoặc chì/axit có thể đạt "
    "điện áp cực đại ngay khi sạc lần đầu và do đó có thể không đạt được các "
    "điện áp này. Tuy nhiên chúng sẽ đạt sau hai hoặc ba lần sạc, vì vậy nếu "
    "tiến hành thử nghiệm thì trước hết phải cho pin chu trình sạc xả.</p>"
    "<p>Ghi chú của người dịch: nhan đề được in thành hai dòng căn giữa có "
    "gạch nối khi xuống dòng ('evalua-tion'); toàn bộ câu được ghi không "
    "ngắt và không gạch nối. Tiêu đề 'Peak o/c voltage for spark ignition "
    "(V)' viết tắt 'open circuit' thành 'o/c' đúng như bản in.</p>"
    "<p>Ghi chú của người dịch: các tên loại pin được ngăn cách bằng dấu "
    "gạch ngang kiểu en-dash trong bản in, trừ 'Nickel Cadmium', 'Lead Acid "
    "(Wet)' và 'Lead Acid (Dry) (See Note 1)'. Năm mã IEC in dấu gạch ngang. "
    "Mục Kẽm – Mangan dioxide trải trên hai hàng, hàng thứ hai đặt trong "
    "ngoặc đơn '(Zinc – Carbon Leclanche)'. Dòng nguồn và nhan đề 'Ghi chú:' "
    "được in nghiêng.</p>"
)

# ---------------------------------------------------------------------------
# Table 13.7 — printed p.370 (PDF p.391)
# ---------------------------------------------------------------------------

CAPTION137_EN = (
    "Table 13.7 Creepages, clearances and separations considered as not "
    "subject to fault (infallible)"
    "<br>Creepages, clearances and separations (mm)"
    "<br>CTI values<br>Note 1"
)
CAPTION137_VI = (
    "Bảng 13.7 Khoảng cách bò, khoảng hở và khoảng tách được coi là không "
    "chịu sự cố (không thể hỏng)"
    "<br>Khoảng cách bò, khoảng hở và khoảng tách (mm)"
    "<br>Giá trị CTI<br>Ghi chú 1"
)

HEAD137_EN = [
    "Maximum<br>peak<br>(V)",
    "Clearance",
    "Creepage<br>Air",
    "Creepage<br>CTG",
    "Separation<br>CC",
    "Separation<br>SI",
    "‘ia’",
    "‘ib’",
]
HEAD137_VI = [
    "Đỉnh cực đại<br>(V)",
    "Khoảng hở",
    "Khoảng bò<br>Không khí",
    "Khoảng bò<br>CTG",
    "Khoảng tách<br>CC",
    "Khoảng tách<br>SI",
    "‘ia’",
    "‘ib’",
]

# 8 cells per row: peak voltage, clearance, two creepages, two separations
# and the two CTI categories. The printed word labels are translated in VI.
ROWS137_EN = [
    ["10", "1.5", "1.5", "0.5", "0.5", "0.5", "Note 2", "Note 2"],
    ["30", "2.0", "2.0", "0.7", "0.7", "0.5", "100", "100"],
    ["60", "3.0", "3.0", "1.0", "1.0", "0.5", "100", "100"],
    ["90", "4.0", "4.0", "1.3", "1.3", "0.7", "100", "100"],
    ["190", "5.0", "8.0", "2.6", "1.7", "0.8", "175", "175"],
    ["375", "6.0", "10.0", "3.3", "2.0", "1.0", "175", "175"],
    ["550", "7.0", "15.0", "5.0", "2.4", "1.2", "275", "175"],
    ["750", "8.0", "18.0", "6.0", "2.7", "1.4", "275", "175"],
    ["1000", "10.0", "25.0", "8.3", "3.3", "1.7", "275", "175"],
    ["1300", "14.0", "36.0", "12.0", "4.6", "2.3", "275", "175"],
    ["1575", "16.0", "49.0", "13.3", "5.3", "2.7", "275", "175"],
    ["3.3 kV", "Note 3", "Note 3", "Note 3", "9.0", "4.5", "N/A", "N/A"],
    ["4.7 kV", "Note 3", "Note 3", "Note 3", "12.0", "6.9", "N/A", "N/A"],
    ["9.5 kV", "Note 3", "Note 3", "Note 3", "20.0", "10.0", "N/A", "N/A"],
    ["15.6 kV", "Note 3", "Note 3", "Note 3", "33.0", "16.5", "N/A", "N/A"],
]
ROWS137 = ROWS137_EN
ROWS137_VI = [
    ["10", "1.5", "1.5", "0.5", "0.5", "0.5", "Ghi chú 2", "Ghi chú 2"],
    ["30", "2.0", "2.0", "0.7", "0.7", "0.5", "100", "100"],
    ["60", "3.0", "3.0", "1.0", "1.0", "0.5", "100", "100"],
    ["90", "4.0", "4.0", "1.3", "1.3", "0.7", "100", "100"],
    ["190", "5.0", "8.0", "2.6", "1.7", "0.8", "175", "175"],
    ["375", "6.0", "10.0", "3.3", "2.0", "1.0", "175", "175"],
    ["550", "7.0", "15.0", "5.0", "2.4", "1.2", "275", "175"],
    ["750", "8.0", "18.0", "6.0", "2.7", "1.4", "275", "175"],
    ["1000", "10.0", "25.0", "8.3", "3.3", "1.7", "275", "175"],
    ["1300", "14.0", "36.0", "12.0", "4.6", "2.3", "275", "175"],
    ["1575", "16.0", "49.0", "13.3", "5.3", "2.7", "275", "175"],
    ["3.3 kV", "Ghi chú 3", "Ghi chú 3", "Ghi chú 3", "9.0", "4.5", "N/A", "N/A"],
    ["4.7 kV", "Ghi chú 3", "Ghi chú 3", "Ghi chú 3", "12.0", "6.9", "N/A", "N/A"],
    ["9.5 kV", "Ghi chú 3", "Ghi chú 3", "Ghi chú 3", "20.0", "10.0", "N/A", "N/A"],
    ["15.6 kV", "Ghi chú 3", "Ghi chú 3", "Ghi chú 3", "33.0", "16.5", "N/A", "N/A"],
]

NOTE137_EN = (
    "<p>(from BS/EN 50020)</p>"
    "<p>CTG = Conformal coating</p>"
    "<p>CC = Casting compound</p>"
    "<p>SI = Solid insulation</p>"
    "<p>Notes:</p>"
    "<p>1 CTI refers only to quality of insulation providing the creepage path "
    "in air.</p>"
    "<p>2 CTI is not considered as important at these low voltages.</p>"
    "<p>3 No values are given for these voltages and thus it is considered "
    "that separation by creepages or clearances alone is not sufficient.</p>"
    "<p>Translator note: the spanning over-header 'Creepages, clearances and "
    "separations (mm)' covers the five distance columns and the over-header "
    "'CTI values Note 1' covers the two ‘ia’/‘ib’ columns; both are carried "
    "in the caption. The Creepage and Separation group heads with their Air/CTG "
    "and CC/SI sub-columns are flattened into paired HEAD cells.</p>"
    "<p>Translator note: the CTI cells print the literal words 'Note 2' in the "
    "10 V row and 'Note 3' in the four highest-voltage rows instead of "
    "numbers, and 'N/A' in both CTI columns of those four rows. The first "
    "column prints plain numbers up to 1575 and then '3.3 kV', '4.7 kV', "
    "'9.5 kV' and '15.6 kV' with a space; the VI rows translate the printed "
    "word labels to 'Ghi chú 2' / 'Ghi chú 3' while keeping 'N/A'.</p>"
    "<p>Translator note: Note 3 reads 'by creepages or clearances', whereas "
    "the corresponding Note 2 of Table 13.8 reads 'by clearance or creepage'; "
    "the difference and the singular/plural forms are preserved in both "
    "languages. The source line and the 'Notes:' heading are italicised in "
    "print.</p>"
)

NOTE137_VI = (
    "<p>(theo BS/EN 50020)</p>"
    "<p>CTG = Lớp phủ bảo vệ</p>"
    "<p>CC = Hợp chất đổ khuôn</p>"
    "<p>SI = Cách điện rắn</p>"
    "<p>Ghi chú:</p>"
    "<p>1 CTI chỉ liên quan đến chất lượng của lớp cách điện tạo nên đường "
    "bò trong không khí.</p>"
    "<p>2 CTI không được coi là quan trọng ở các điện áp thấp này.</p>"
    "<p>3 Không cho giá trị nào cho các điện áp này, vì vậy người ta cho rằng "
    "riêng sự tách bằng khoảng cách bò hoặc khoảng hở là chưa đủ.</p>"
    "<p>Ghi chú của người dịch: tiêu đề trải rộng 'Creepages, clearances and "
    "separations (mm)' phủ năm cột khoảng cách và tiêu đề 'CTI values Note 1' "
    "phủ hai cột ‘ia’/‘ib’; cả hai được đưa vào CAPTION. Các nhóm Creepage và "
    "Separation cùng các cột con Air/CTG và CC/SI được gộp thành các ô HEAD "
    "ghép đôi.</p>"
    "<p>Ghi chú của người dịch: các ô CTI in literal là các từ 'Note 2' ở "
    "hàng 10 V và 'Note 3' ở bốn hàng điện áp cao nhất thay vì số, đồng thời "
    "in 'N/A' ở cả hai cột CTI của bốn hàng đó. Cột đầu in các số thuần túy "
    "đến 1575 rồi đến '3.3 kV', '4.7 kV', '9.5 kV' và '15.6 kV' có dấu cách; "
    "các hàng tiếng Việt dịch nhãn chữ sang 'Ghi chú 2' / 'Ghi chú 3' nhưng "
    "giữ 'N/A'.</p>"
    "<p>Ghi chú của người dịch: Ghi chú 3 viết 'bằng khoảng cách bò hoặc "
    "khoảng hở', trong khi Ghi chú 2 tương ứng của Bảng 13.8 viết 'bằng khoảng "
    "hở hoặc khoảng cách bò'; sự khác biệt và hình thức số nhiều/số ít được "
    "giữ nguyên ở cả hai ngôn ngữ. Dòng nguồn và nhan đề 'Ghi chú:' được in "
    "nghiêng.</p>"
)

# ---------------------------------------------------------------------------
# Table 13.8 — printed p.379 (PDF p.400)
# ---------------------------------------------------------------------------

CAPTION138_EN = (
    "Table 13.8 Creepages, clearances and separations (countable faults)"
    "<br>Clearances, creepages and separations (mm)"
    "<br>CTI value<br>Category"
)
CAPTION138_VI = (
    "Bảng 13.8 Khoảng cách bò, khoảng hở và khoảng tách (lỗi có thể đếm được)"
    "<br>Khoảng hở, khoảng bò và khoảng tách (mm)"
    "<br>Giá trị CTI<br>Danh mục"
)

HEAD138_EN = [
    "Maximum<br>peak<br>(V)",
    "Clearance",
    "Creepage<br>Air",
    "Creepage<br>CTG",
    "Separation<br>CC",
    "Separation<br>SI",
    "‘ia’",
    "‘ib’",
]
HEAD138_VI = [
    "Đỉnh cực đại<br>(V)",
    "Khoảng hở",
    "Khoảng bò<br>Không khí",
    "Khoảng bò<br>CTG",
    "Khoảng tách<br>CC",
    "Khoảng tách<br>SI",
    "‘ia’",
    "‘ib’",
]

# 8 cells per row: peak voltage, clearance, two creepages, two separations
# and the two CTI categories. Voltage cells keep the printed suffixed V/KV.
ROWS138_EN = [
    ["10V", "0.5", "0.5", "0.17", "0.17", "0.17", "Note 1", "Note 1"],
    ["30V", "0.67", "0.67", "0.24", "0.24", "0.17", "100", "100"],
    ["60V", "1.0", "1.0", "0.34", "0.34", "0.17", "100", "100"],
    ["90V", "1.34", "1.34", "0.44", "0.44", "0.24", "100", "100"],
    ["190V", "1.67", "2.67", "0.87", "0.57", "0.27", "175", "175"],
    ["375V", "2.0", "3.34", "1.1", "0.67", "0.34", "175", "175"],
    ["550V", "2.34", "5.0", "1.67", "0.8", "0.4", "275", "175"],
    ["750V", "2.67", "6.0", "2.0", "0.9", "0.47", "275", "175"],
    ["1000V", "3.34", "8.34", "2.77", "1.1", "0.57", "275", "175"],
    ["1300V", "4.67", "12.0", "4.0", "1.54", "0.77", "275", "175"],
    ["1575V", "5.34", "16.34", "4.44", "1.77", "0.9", "275", "175"],
    ["3.3KV", "Note 2", "Note 2", "Note 2", "3.0", "1.5", "N/A", "N/A"],
    ["4.7KV", "Note 2", "Note 2", "Note 2", "4.0", "2.0", "N/A", "N/A"],
    ["9.5KV", "Note 2", "Note 2", "Note 2", "6.67", "3.34", "N/A", "N/A"],
    ["15.6KV", "Note 2", "Note 2", "Note 2", "11.0", "5.34", "N/A", "N/A"],
]
ROWS138 = ROWS138_EN
ROWS138_VI = [
    ["10V", "0.5", "0.5", "0.17", "0.17", "0.17", "Ghi chú 1", "Ghi chú 1"],
    ["30V", "0.67", "0.67", "0.24", "0.24", "0.17", "100", "100"],
    ["60V", "1.0", "1.0", "0.34", "0.34", "0.17", "100", "100"],
    ["90V", "1.34", "1.34", "0.44", "0.44", "0.24", "100", "100"],
    ["190V", "1.67", "2.67", "0.87", "0.57", "0.27", "175", "175"],
    ["375V", "2.0", "3.34", "1.1", "0.67", "0.34", "175", "175"],
    ["550V", "2.34", "5.0", "1.67", "0.8", "0.4", "275", "175"],
    ["750V", "2.67", "6.0", "2.0", "0.9", "0.47", "275", "175"],
    ["1000V", "3.34", "8.34", "2.77", "1.1", "0.57", "275", "175"],
    ["1300V", "4.67", "12.0", "4.0", "1.54", "0.77", "275", "175"],
    ["1575V", "5.34", "16.34", "4.44", "1.77", "0.9", "275", "175"],
    ["3.3KV", "Ghi chú 2", "Ghi chú 2", "Ghi chú 2", "3.0", "1.5", "N/A", "N/A"],
    ["4.7KV", "Ghi chú 2", "Ghi chú 2", "Ghi chú 2", "4.0", "2.0", "N/A", "N/A"],
    ["9.5KV", "Ghi chú 2", "Ghi chú 2", "Ghi chú 2", "6.67", "3.34", "N/A", "N/A"],
    ["15.6KV", "Ghi chú 2", "Ghi chú 2", "Ghi chú 2", "11.0", "5.34", "N/A", "N/A"],
]

NOTE138_EN = (
    "<p>CTG = Coating</p>"
    "<p>CC = Casting compound</p>"
    "<p>SI = Solid insulation</p>"
    "<p>Notes:</p>"
    "<p>1 CTI is not considered as important at these low voltages.</p>"
    "<p>2 No values are given for these voltages and thus it is considered "
    "that separation by clearance or creepage is not sufficient in such "
    "circumstances.</p>"
    "<p>Translator note: the spanning over-header 'Clearances, creepages and "
    "separations (mm)' covers the five distance columns and 'CTI value' over "
    "'Category' covers the two ‘ia’/‘ib’ columns; both are carried in the "
    "caption. The Creepage and Separation group heads with their Air/CTG and "
    "CC/SI sub-columns are flattened into paired HEAD cells.</p>"
    "<p>Translator note: the first column prints every voltage with a suffixed "
    "'V' or 'KV' and no space ('10V' ... '15.6KV'), with a capital K in the "
    "last four rows, unlike Table 13.7 which prints plain numbers and '3.3 kV' "
    "with a space. The CTI cells print the literal words 'Note 1' in the 10V "
    "row and 'Note 2' in the four highest-voltage rows, and 'N/A' in both CTI "
    "columns of those rows; the VI rows translate the printed word labels "
    "while keeping 'N/A'.</p>"
    "<p>Translator note: the legend prints 'CTG = Coating' here but 'CTG = "
    "Conformal coating' under Table 13.7; the abbreviation is preserved. Note "
    "2 here reads 'by clearance or creepage ... in such circumstances', "
    "whereas Table 13.7 Note 3 reads 'by creepages or clearances alone'; both "
    "wordings are retained. The 'Notes:' heading is italicised in print.</p>"
)

NOTE138_VI = (
    "<p>CTG = Lớp phủ</p>"
    "<p>CC = Hợp chất đổ khuôn</p>"
    "<p>SI = Cách điện rắn</p>"
    "<p>Ghi chú:</p>"
    "<p>1 CTI không được coi là quan trọng ở các điện áp thấp này.</p>"
    "<p>2 Không cho giá trị nào cho các điện áp này, vì vậy người ta cho rằng "
    "trong những trường hợp đó, sự tách bằng khoảng hở hoặc khoảng cách bò "
    "là chưa đủ.</p>"
    "<p>Ghi chú của người dịch: tiêu đề trải rộng 'Clearances, creepages and "
    "separations (mm)' phủ năm cột khoảng cách và 'CTI value' phủ 'Category' "
    "trên hai cột ‘ia’/‘ib’; cả hai được đưa vào CAPTION. Các nhóm Creepage và "
    "Separation cùng các cột con Air/CTG và CC/SI được gộp thành các ô HEAD "
    "ghép đôi.</p>"
    "<p>Ghi chú của người dịch: cột đầu in mọi điện áp với chữ 'V' hoặc 'KV' "
    "ngay sau số và không có dấu cách ('10V' ... '15.6KV'), với chữ K viết "
    "hoa ở bốn hàng cuối, khác với Bảng 13.7 in số thuần túy và '3.3 kV' có "
    "dấu cách. Các ô CTI in literal là các từ 'Note 1' ở hàng 10V và 'Note 2' "
    "ở bốn hàng điện áp cao nhất, đồng thời in 'N/A' ở cả hai cột CTI của "
    "những hàng đó; các hàng tiếng Việt dịch nhãn chữ nhưng giữ 'N/A'.</p>"
    "<p>Ghi chú của người dịch: chú thích in 'CTG = Coating' ở đây nhưng 'CTG "
    "= Conformal coating' dưới Bảng 13.7; cách viết tắt được giữ nguyên. Ghi "
    "chú 2 ở đây viết 'bằng khoảng hở hoặc khoảng cách bò ... trong những "
    "trường hợp đó', trong khi Ghi chú 3 của Bảng 13.7 viết 'riêng bằng khoảng "
    "cách bò hoặc khoảng hở'; cả hai cách diễn đạt đều được giữ. Nhan đề "
    "'Ghi chú:' được in nghiêng.</p>"
)
