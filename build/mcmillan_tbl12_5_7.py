# -*- coding: utf-8 -*-
"""Tables 12.5, 12.6 and 12.7 of McMillan Chapter 12, bilingual EN/VI.

Transcribed from the authoritative page renders (the OCR text layer is
garbled for all three tables):
  - PDF p.336 / printed p.315 -> Table 12.5 + source line + Note
  - PDF p.337 / printed p.316 -> Table 12.6 + source line
  - PDF p.339 / printed p.318 -> Table 12.7 + spanning heading + 3 notes

Cross-checked against work/mcmillan_ch12_brief.md SURVEY D, sections B/C/E.
Structure follows mcmillan_tbl11_1_2.py: HEAD is one cell per column,
ROWS is a list of equal-length cell lists, CAPTION and NOTE are localized.
Full-width spanning lines that precede the printed columns are carried as a
second line of CAPTION, after the printed caption text.

Every table row carries connector words ('see note', '(note 1)', '(note 2)'),
so language-specific ROWS125_VI / ROWS127_VI are exported in addition to the
shared English rows. Table 12.6 is purely numeric/symbolic, so its VI rows
may share the English list.

Printed quirks retained deliberately (with bilingual translator notes):

  * 12.5 numeric column headings are stacked two/three lines deep;
  * 12.5 insertion-torque cells print '±' (OCR read 'It', 'zt', 'f');
  * 12.5 and 12.6 source lines print '50019' (OCR read '50029');
  * 12.5 printed Note ends with a full stop;
  * 12.6 caption hyphenates 'enve-lope' across justified lines;
  * 12.6 inequality signs '<' / '≤' (OCR read 'O', '5', 't');
  * 12.7 spanning heading over the two right-hand columns;
  * 12.7 Ith / Idyn / Isc are subscripted in print;
  * 12.7 note numbering punctuation is inconsistent (1, 2, 3.).
"""

# ---------------------------------------------------------------------------
# Table 12.5 — printed p.315 (PDF p.336)
# ---------------------------------------------------------------------------

CAPTION125_EN = "Table 12.5 Torque tests for screwed lamps"
CAPTION125_VI = "Bảng 12.5 Thử mô-men xoắn đối với đèn vặn ốc"

HEAD125_EN = [
    "Lamp cap size",
    "Insertion torque<br>Newton Metres",
    "Minimum removal<br>torque<br>Newton Metres",
]
HEAD125_VI = [
    "Kích cỡ đui đèn",
    "Mô-men xoắn khi lắp<br>Newton mét",
    "Mô-men xoắn tháo<br>tối thiểu<br>Newton mét",
]

# 3 cells per row: lamp cap size + insertion torque + minimum removal torque.
ROWS125 = [
    ["E10", "see note", "see note"],
    ["E14", "1.0 ± 0.1", "0.3"],
    ["E27", "1.5 ± 0.1", "0.5"],
    ["E40", "3.0 ± 0.1", "1.0"],
]
ROWS125_EN = ROWS125
ROWS125_VI = [
    ["E10", "xem ghi chú", "xem ghi chú"],
    ["E14", "1.0 ± 0.1", "0.3"],
    ["E27", "1.5 ± 0.1", "0.5"],
    ["E40", "3.0 ± 0.1", "1.0"],
]

NOTE125_EN = (
    "<p>(from BS/EN 50019)</p>"
    "<p>Note: No test is considered as necessary for this small size of lamp.</p>"
    "<p>Translator note: the two numeric column headings are stacked in "
    "print — 'Insertion torque' over 'Newton Metres', and 'Minimum removal' "
    "/ 'torque' over 'Newton Metres'. Line breaks reproduce the stack.</p>"
    "<p>Translator note: the three insertion-torque cells print "
    "'1.0 ± 0.1', '1.5 ± 0.1' and '3.0 ± 0.1'; the OCR text layer read the "
    "sign as 'It', 'zt' and 'f'. The rendered plus/minus sign is retained.</p>"
    "<p>Translator note: the source line prints '50019'; the OCR text "
    "layer read '50029'. Retained as printed.</p>"
    "<p>Translator note: the printed Note ends with a full stop "
    "('...small size of lamp.'); retained.</p>"
)

NOTE125_VI = (
    "<p>(theo BS/EN 50019)</p>"
    "<p>Ghi chú: Không cần thử nghiệm nào cho kích cỡ đèn nhỏ này.</p>"
    "<p>Ghi chú của người dịch: hai tiêu đề cột số được in xếp chồng — "
    "'Mô-men xoắn khi lắp' trên 'Newton mét' và 'Mô-men xoắn tháo' / 'tối "
    "thiểu' trên 'Newton mét'. Ngắt dòng tái tạo cách xếp đó.</p>"
    "<p>Ghi chú của người dịch: ba ô mô-men xoắn khi lắp in '1.0 ± 0.1', "
    "'1.5 ± 0.1' và '3.0 ± 0.1'; lớp văn bản OCR đọc dấu này là 'It', 'zt' "
    "và 'f'. Giữ dấu cộng/trừ theo bản in.</p>"
    "<p>Ghi chú của người dịch: dòng nguồn in '50019'; lớp văn bản OCR "
    "đọc là '50029'. Giữ nguyên theo bản in.</p>"
    "<p>Ghi chú của người dịch: dòng Ghi chú in kết thúc bằng dấu chấm "
    "('...small size of lamp.'); giữ nguyên.</p>"
)

# ---------------------------------------------------------------------------
# Table 12.6 — printed p.316 (PDF p.337)
# ---------------------------------------------------------------------------

CAPTION126_EN = "Table 12.6 Separation between lamp envelope and cover"
CAPTION126_VI = "Bảng 12.6 Khoảng cách giữa bóng đèn và vỏ bọc"

HEAD126_EN = [
    "Lamp power (P) (Watts)",
    "Minimum lamp/cover separation (mm)",
]
HEAD126_VI = [
    "Công suất đèn (P) (Watt)",
    "Khoảng cách tối thiểu giữa đèn/vỏ bọc (mm)",
]

# 2 cells per row: lamp power band + minimum separation. Purely
# numeric/symbolic, so the VI rows share the English list.
ROWS126 = [
    ["0< P <60", "3"],
    ["60≤ P <100", "5"],
    ["100≤ P <200", "10"],
    ["200≤ P <500", "20"],
    ["500< P", "30"],
]
ROWS126_EN = ROWS126
ROWS126_VI = ROWS126

NOTE126_EN = (
    "<p>(from BS/EN 50019)</p>"
    "<p>Translator note: the printed caption breaks 'envelope' across "
    "justified lines as 'enve-' / 'lope'; the word is given whole here.</p>"
    "<p>Translator note: the left bound prints '<' in row 1 and '≤' in "
    "rows 2-4, with a strict '<' on the right in every row, ending in "
    "'500< P'. The OCR text layer read these as 'O<', '605', '1005', "
    "'2005' and 't'; the rendered inequality signs govern. Irregular "
    "printed spacing is normalised in the cells.</p>"
    "<p>Translator note: the source line prints '50019'; the OCR text "
    "layer read '50029'. Retained as printed.</p>"
)

NOTE126_VI = (
    "<p>(theo BS/EN 50019)</p>"
    "<p>Ghi chú của người dịch: tiêu đề in bị gãy dòng do căn đều hai "
    "bên, 'envelope' thành 'enve-' / 'lope'; ở đây viết trọn từ.</p>"
    "<p>Ghi chú của người dịch: cận trái in '<' ở dòng 1 và '≤' ở các "
    "dòng 2-4, cận phải luôn là '<', dòng cuối là '500< P'. Lớp văn bản "
    "OCR đọc là 'O<', '605', '1005', '2005' và 't'; dấu bất đẳng thức "
    "trên bản in được giữ. Khoảng cách in không đều được chuẩn hóa trong ô.</p>"
    "<p>Ghi chú của người dịch: dòng nguồn in '50019'; lớp văn bản OCR "
    "đọc là '50029'. Giữ nguyên theo bản in.</p>"
)

# ---------------------------------------------------------------------------
# Table 12.7 — printed p.318 (PDF p.339)
# ---------------------------------------------------------------------------

CAPTION127_EN = (
    "Table 12.7 Proof against damage by short circuit currents"
    "<br>Safety factors to be used as multipliers for determination of "
    "test current using short circuit current (Isc) as a base"
)
CAPTION127_VI = (
    "Bảng 12.7 Khả năng chống hư hỏng do dòng ngắn mạch"
    "<br>Các hệ số an toàn được dùng làm hệ số nhân để xác định dòng "
    "thử nghiệm dựa trên dòng ngắn mạch (Isc)"
)

HEAD127_EN = [
    "Test current",
    "Basic safety factor",
    "Safety factor for waveform variation",
]
HEAD127_VI = [
    "Dòng thử nghiệm",
    "Hệ số an toàn cơ bản",
    "Hệ số an toàn cho sự biến đổi dạng sóng",
]

# 3 cells per row: test current label + basic factor + waveform factor.
ROWS127 = [
    ["Ith(note 1)", "1.1", "1.0"],
    ["Idyn(note 2)", "1.25", "2.5"],
]
ROWS127_EN = ROWS127
ROWS127_VI = [
    ["Ith(ghi chú 1)", "1.1", "1.0"],
    ["Idyn(ghi chú 2)", "1.25", "2.5"],
]

NOTE127_EN = (
    "<p>1 Ith is the current to be used for temperature rise determination.</p>"
    "<p>2 Idyn is the current to be used for dynamic stress testing.</p>"
    "<p>3. The maximum values of Isc in any waveform configuration are "
    "Ith /1.1 rms and Idyn/1.25 peak.</p>"
    "<p>Translator note: the spanning heading 'Safety factors to be used "
    "as multipliers for determination of test current using short circuit "
    "current (Isc) as a base' covers the two right-hand columns. It is "
    "carried in the caption (second line) so the flat HEAD/ROWS shape "
    "stays intact.</p>"
    "<p>Translator note: Ith, Idyn and Isc are printed with subscripted "
    "'th', 'dyn' and 'sc'. They are written as plain suffixes here because "
    "complete subscript glyphs are unavailable.</p>"
    "<p>Translator note: note numbering punctuation is inconsistent in "
    "print — items 1 and 2 have no full stop after the numeral while item "
    "3 reads '3.'. Preserved as printed.</p>"
    "<p>Translator note: the OCR text layer garbled the row labels "
    "('I*(note 1)', 'I+,(note 2)') and note 3 ('Iu, /1.1 rms and I+/1.25 "
    "peak'); the forms above follow the render.</p>"
)

NOTE127_VI = (
    "<p>1 Ith là dòng được dùng để xác định độ tăng nhiệt độ.</p>"
    "<p>2 Idyn là dòng được dùng để thử ứng suất động.</p>"
    "<p>3. Giá trị lớn nhất của Isc trong bất kỳ cấu hình dạng sóng nào "
    "là Ith /1.1 rms và Idyn/1.25 peak.</p>"
    "<p>Ghi chú của người dịch: tiêu đề trải rộng 'Safety factors to be "
    "used as multipliers for determination of test current using short "
    "circuit current (Isc) as a base' phủ lên hai cột bên phải được đưa "
    "vào dòng thứ hai của CAPTION để giữ cấu trúc HEAD/ROWS dạng phẳng.</p>"
    "<p>Ghi chú của người dịch: Ith, Idyn và Isc được in với các chỉ số "
    "dưới là 'th', 'dyn' và 'sc'. Ở đây viết dạng hậu tố thường vì không "
    "có đầy đủ ký tự chỉ số dưới.</p>"
    "<p>Ghi chú của người dịch: dấu cắt số ghi chú không thống nhất trên "
    "bản in — mục 1 và 2 không có dấu chấm sau số trong khi mục 3 viết "
    "'3.'. Giữ nguyên theo bản in.</p>"
    "<p>Ghi chú của người dịch: lớp văn bản OCR làm sai nhãn hàng "
    "('I*(note 1)', 'I+,(note 2)') và ghi chú 3 ('Iu, /1.1 rms and "
    "I+/1.25 peak'); các dạng trên theo bản in.</p>"
)
