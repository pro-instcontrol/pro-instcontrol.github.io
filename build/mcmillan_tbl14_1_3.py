# -*- coding: utf-8 -*-
"""Tables 14.1 to 14.3 of McMillan Chapter 14, bilingual EN/VI.

Transcribed from the authoritative page renders:
  - PDF p.452 / printed p.431 -> Table 14.1 + italic source line
  - PDF p.453 / printed p.432 -> Table 14.2 + source line + Note
  - PDF p.455 / printed p.434 -> Table 14.3 + source line + Notes 1-5

Cross-checked against work/mcmillan_ch14_survey_a.md §4. The OCR text layer
is garbled in all three tables ('ffrorn' for 'from', '1 .o' for '1.0', 'nns'
for 'rms', 'cncapsulant' for 'encapsulant', 'BS 5901,15' for 'BS 5901,¹⁵');
the page images govern throughout.

Structure follows mcmillan_tbl13_1_4.py: HEAD is one cell per column, ROWS is
a list of equal-length cell lists, CAPTION and NOTE are localized. Spanning
over-headers are carried as extra lines of CAPTION so the flat HEAD/ROWS shape
stays intact:
  * 14.1: 'Impact energy (J)' spans the two damage-risk sub-columns;
  * 14.3: three spanning over-headers cover the ac/dc pair, the three
    separation columns and the four CTI columns.

Rows are shared only where every cell is numeric/symbolic (14.2 and 14.3,
including 'N/A'). Table 14.1 prints connector words in its first-column
labels, so it exports genuine ROWS141_VI / ROWS141_EN.

Printed quirks retained deliberately (with bilingual translator notes):

  * 14.1 first row is a run-on label which repeats the phrase 'which are
    guarded (These are tested with their guards removed)' found in row 3;
  * 14.2 mass unit prints as '(K)', not 'kg', and the Note uses gₙ with
    10m/s² versus 9.81 m/s²;
  * 14.3 prints mixed-case 'coated' and 'Encapsulated' sub-heads, retains
    'BS 5901,¹⁵' in Note 5 and omits that Note's terminal full stop.
"""

# ---------------------------------------------------------------------------
# Table 14.1 — printed p.431 (PDF p.452)
# ---------------------------------------------------------------------------

CAPTION141_EN = (
    "Table 14.1 Impact testing of enclosure parts"
    "<br>Impact energy (J)"
)
CAPTION141_VI = (
    "Bảng 14.1 Thử va đập các bộ phận của vỏ bọc"
    "<br>Năng lượng va đập (J)"
)

HEAD141_EN = [
    "Part of apparatus",
    "Normal damage<br>risk",
    "Low damage<br>risk",
]
HEAD141_VI = [
    "Bộ phận của thiết bị",
    "Nguy cơ hư hỏng<br>bình thường",
    "Nguy cơ hư hỏng<br>thấp",
]

# 3 cells per row: apparatus part + normal-risk energy + low-risk energy.
ROWS141 = [
    ["All parts of enclosures including guards and fan hoods, excluding "
     "light transmitting parts which do not have a guard which are guarded "
     "(These are tested with their guards removed)", "3.5", "2.0"],
    ["Light transmitting parts", "2.0", "1.0"],
    ["Light transmitting parts which are guarded (These are tested with "
     "their guards removed)", "1.0", "0.5"],
]
ROWS141_EN = ROWS141
ROWS141_VI = [
    ["Tất cả các bộ phận của vỏ bọc, kể cả tấm che và mũ quạt, không tính "
     "các bộ phận truyền sáng không có tấm che và những bộ phận được che "
     "(Các bộ phận này được thử khi đã tháo bỏ tấm che)", "3.5", "2.0"],
    ["Các bộ phận truyền sáng", "2.0", "1.0"],
    ["Các bộ phận truyền sáng có tấm che (Các bộ phận này được thử khi đã "
     "tháo bỏ tấm che)", "1.0", "0.5"],
]

NOTE141_EN = (
    "<p>(from BS 6941)</p>"
    "<p>Translator note: the spanning over-header 'Impact energy (J)' covers "
    "the 'Normal damage risk' and 'Low damage risk' sub-columns and is "
    "carried in the caption (second line). The first row label is a run-on "
    "in the print and repeats the phrase 'which are guarded (These are "
    "tested with their guards removed)' that also appears in the third "
    "row; both occurrences are preserved verbatim.</p>"
    "<p>Translator note: the source line is italicised in print. The OCR "
    "text layer read 'from' as 'ffrorn' and '1.0' as '1 .o'; the render "
    "governs.</p>"
)

NOTE141_VI = (
    "<p>(theo BS 6941)</p>"
    "<p>Ghi chú của người dịch: tiêu đề phía trên 'Impact energy (J)' trải "
    "rộng trên hai cột con 'Normal damage risk' và 'Low damage risk' và "
    "được đưa vào nhan đề (dòng thứ hai). Nhãn của hàng đầu tiên bị nối dài "
    "trong bản in và lặp lại cụm từ 'which are guarded (These are tested "
    "with their guards removed)' vốn cũng xuất hiện ở hàng thứ ba; cả hai "
    "lần xuất hiện đều được giữ nguyên.</p>"
    "<p>Ghi chú của người dịch: dòng nguồn được in nghiêng. Lớp văn bản OCR "
    "đọc 'from' thành 'ffrorn' và '1.0' thành '1 .o'; ảnh trang in là nguồn "
    "quyết định.</p>"
)

# ---------------------------------------------------------------------------
# Table 14.2 — printed p.432 (PDF p.453)
# ---------------------------------------------------------------------------

CAPTION142_EN = "Table 14.2 Use of smaller impact tester masses for testing"
CAPTION142_VI = (
    "Bảng 14.2 Sử dụng đầu thử va đập có khối lượng nhỏ hơn để thử nghiệm"
)

HEAD142_EN = [
    "Impact energy<br>(J)",
    "Impact test mass<br>(K)",
    "Impact test height<br>(m)",
]
HEAD142_VI = [
    "Năng lượng va đập<br>(J)",
    "Khối lượng đầu thử va đập<br>(K)",
    "Độ cao thử va đập<br>(m)",
]

# 3 cells per row: energy + test mass + test height. All cells numeric.
ROWS142 = [
    ["3.5", "1.0", "0.35"],
    ["2.0", "0.25", "0.8"],
    ["1.0", "0.25", "0.4"],
    ["0.5", "0.25", "0.2"],
]
ROWS142_EN = ROWS142
ROWS142_VI = ROWS142

NOTE142_EN = (
    "<p>(from BS 6941)</p>"
    "<p>Note: For the purposes of this Table, gₙ (the acceleration due to "
    "gravity) in the formula, height of fall = energy (mass × gₙ), is taken "
    "as 10m/s² for convenience, rather than the more accurate figure of "
    "9.81 m/s².</p>"
    "<p>Translator note: the mass unit prints as '(K)' in the second "
    "header, not 'kg'; the printed form is retained here and in the VI "
    "header. The caption is printed over two lines. The subscript in gₙ "
    "and the superscripts in 'm/s²' were restored from the render, where "
    "the OCR text layer garbled them.</p>"
)

NOTE142_VI = (
    "<p>(theo BS 6941)</p>"
    "<p>Ghi chú: Đối với mục đích của Bảng này, gₙ (gia tốc do trọng lực) "
    "trong công thức, độ cao rơi = năng lượng (khối lượng × gₙ), được lấy "
    "là 10m/s² để tiện lợi, thay vì giá trị chính xác hơn là 9.81 m/s².</p>"
    "<p>Ghi chú của người dịch: đơn vị khối lượng được in là '(K)' trong "
    "tiêu đề thứ hai, không phải 'kg'; hình thức in này được giữ nguyên ở "
    "đây và trong tiêu đề tiếng Việt. Nhan đề được in trên hai dòng. Chỉ số "
    "dưới trong gₙ và chỉ số trên trong 'm/s²' được khôi phục từ ảnh trang "
    "in, vì lớp văn bản OCR đã làm hỏng chúng.</p>"
)

# ---------------------------------------------------------------------------
# Table 14.3 — printed p.434 (PDF p.455)
# ---------------------------------------------------------------------------

CAPTION143_EN = (
    "Table 14.3 Minimum creepage distances, clearances and separations "
    "between conductors"
    "<br>Nominal rms supply voltage (Un) or nominal rms voltage between "
    "conductive parts (Notes 1 and 2) — ac / dc (V)"
    "<br>Minimum separations in air, under coating (Notes 3 and 4) — "
    "In air / coated / Encapsulated (mm)"
    "<br>Minimum creepage distances in air at various CTI values (Note 5) — "
    "CTI 125 / CTI 175 / CTI 250 / CTI 500 (mm)"
)
CAPTION143_VI = (
    "Bảng 14.3 Khoảng cách rò, khoảng hở và khoảng cách phân tách tối thiểu "
    "giữa các dây dẫn"
    "<br>Điện áp nguồn rms danh định (Un) hoặc điện áp rms danh định giữa "
    "các bộ phận dẫn điện (Ghi chú 1 và 2) — ac / dc (V)"
    "<br>Khoảng cách phân tách tối thiểu trong không khí, dưới lớp phủ "
    "(Ghi chú 3 và 4) — Trong không khí / phủ / Đóng gói (mm)"
    "<br>Khoảng cách rò tối thiểu trong không khí ở các giá trị CTI khác "
    "nhau (Ghi chú 5) — CTI 125 / CTI 175 / CTI 250 / CTI 500 (mm)"
)

HEAD143_EN = [
    "ac<br>(V)",
    "dc<br>(V)",
    "In air<br>(mm)",
    "coated<br>(mm)",
    "Encapsulated<br>(mm)",
    "CTI 125<br>(mm)",
    "CTI 175<br>(mm)",
    "CTI 250<br>(mm)",
    "CTI 500<br>(mm)",
]
HEAD143_VI = [
    "ac<br>(V)",
    "dc<br>(V)",
    "Trong không khí<br>(mm)",
    "phủ<br>(mm)",
    "Đóng gói<br>(mm)",
    "CTI 125<br>(mm)",
    "CTI 175<br>(mm)",
    "CTI 250<br>(mm)",
    "CTI 500<br>(mm)",
]

# 9 cells per row: ac, dc, three separations, four creepage/CTI columns.
# Every cell is numeric or symbolic ('N/A'), so the rows are shared.
ROWS143 = [
    ["12", "15", "0.4", "0.3", "0.13", "1.0", "1.0", "1.0", "1.0"],
    ["30", "36", "0.8", "0.3", "0.26", "1.0", "1.0", "1.0", "1.0"],
    ["60", "75", "1.3", "0.43", "0.43", "1.3", "1.3", "1.3", "1.3"],
    ["130", "160", "2.0", "1.0", "0.66", "2.5", "2.0", "1.7", "1.4"],
    ["250", "300", "2.0", "1.7", "0.66", "4.0", "3.4", "2.8", "2.3"],
    ["380", "500", "2.8", "2.6", "0.73", "6.7", "5.1", "4.3", "3.7"],
    ["500", "600", "3.4", "3.0", "0.9", "7.1", "6.0", "5.1", "4.4"],
    ["660", "900", "5.0", "4.4", "1.1", "11.0", "9.0", "7.5", "6.5"],
    ["1000", "1200", "6.8", "5.8", "1.7", "14.0", "12.0", "10.0", "8.6"],
    ["3000", "N/A", "23.0", "N/A", "N/A", "60.0", "42.0", "35.0", "28.0"],
    ["6000", "N/A", "45.0", "N/A", "N/A", "N/A", "85.0", "70.0", "55.0"],
    ["10,000", "N/A", "75.0", "N/A", "N/A", "N/A", "N/A", "100.0", "80.0"],
]
ROWS143_EN = ROWS143
ROWS143_VI = ROWS143

NOTE143_EN = (
    "<p>(from BS 6941)</p>"
    "<p>Notes :</p>"
    "<p>1 The highest voltage which can appear between any conductive parts "
    "will be used even if, at some points due to voltage multiplication, "
    "this can exceed the nominal supply voltage.</p>"
    "<p>2 Actual voltage may exceed nominal values by up to 10% without any "
    "necessary increase in the voltage used to apply the table.</p>"
    "<p>3 Sealed values apply to conducting parts covered by a conformal "
    "coating. Where they emerge from the conformal coating creepage "
    "distances apply, and the coating must have the required CTI in addition "
    "to any supporting insulation.</p>"
    "<p>4 Encapsulated values apply where the conductive parts are surrounded "
    "with encapsulant to a depth of at least 0.4mm. Where any conductive "
    "parts exit the encapsulation the creepage distance in the table apply "
    "and the encapsulant must have the required CTI in addition to any "
    "support insulation.</p>"
    "<p>5 The CTI is determined in accordance with BS 5901,¹⁵ notwithstanding "
    "the fact that the voltages increase to values exceeding those to which "
    "that standard applies</p>"
    "<p>Translator note: the three spanning over-headers cover the ac/dc "
    "pair, the In air/coated/Encapsulated trio and the four CTI columns; "
    "they are carried as extra caption lines. The printed mixed-case "
    "'coated' and 'Encapsulated' sub-heads are retained. Note 5 prints "
    "'BS 5901,¹⁵' with a superscript reference numeral and has no terminal "
    "full stop in the source; both are preserved. '0.4mm', '10%', 'CTI' and "
    "the 'N/A' cells are printed forms retained verbatim.</p>"
    "<p>Translator note: the source line and the Notes are italicised in "
    "print. The OCR text layer read 'rms' as 'nns', 'encapsulant' as "
    "'cncapsulant' and 'BS 5901,¹⁵' as 'BS 5901,15'; the render governs.</p>"
)

NOTE143_VI = (
    "<p>(theo BS 6941)</p>"
    "<p>Ghi chú :</p>"
    "<p>1 Điện áp cao nhất có thể xuất hiện giữa bất kỳ bộ phận dẫn điện "
    "nào sẽ được dùng, ngay cả khi ở một số điểm, do nhân điện áp, giá trị "
    "này có thể vượt quá điện áp nguồn danh định.</p>"
    "<p>2 Điện áp thực tế có thể vượt quá giá trị danh định tới 10% mà "
    "không cần tăng điện áp dùng để áp dụng bảng.</p>"
    "<p>3 Giá trị 'phủ' áp dụng cho các bộ phận dẫn điện được phủ một lớp "
    "phủ bảo vệ đồng hình. Khi các bộ phận đó nhô ra khỏi lớp phủ bảo vệ, "
    "khoảng cách rò được áp dụng và lớp phủ phải có CTI yêu cầu ngoài "
    "lớp cách điện nâng đỡ.</p>"
    "<p>4 Giá trị 'đóng gói' áp dụng khi các bộ phận dẫn điện được bao "
    "quanh bởi vật liệu đóng gói với độ sâu ít nhất 0.4mm. Khi bất kỳ bộ "
    "phận dẫn điện nào thoát ra khỏi lớp đóng gói, khoảng cách rò trong "
    "bảng được áp dụng và vật liệu đóng gói phải có CTI yêu cầu ngoài "
    "lớp cách điện nâng đỡ.</p>"
    "<p>5 CTI được xác định theo BS 5901,¹⁵, mặc dù thực tế điện áp tăng "
    "lên các giá trị vượt quá những giá trị mà tiêu chuẩn đó áp dụng</p>"
    "<p>Ghi chú của người dịch: ba tiêu đề phía trên trải rộng trên cặp "
    "cột ac/dc, bộ ba cột Trong không khí/phủ/Đóng gói và bốn cột CTI; "
    "chúng được đưa thành các dòng nhan đề bổ sung. Các tiêu đề phụ "
    "'coated' và 'Encapsulated' viết hoa hỗn hợp được giữ nguyên. Ghi chú 5 "
    "in 'BS 5901,¹⁵' với số tham chiếu dạng chỉ số trên và không có dấu "
    "chấm cuối câu trong bản gốc; cả hai đều được bảo lưu. '0.4mm', '10%', "
    "'CTI' và các ô 'N/A' là hình thức in được giữ nguyên từng chữ.</p>"
    "<p>Ghi chú của người dịch: dòng nguồn và các Ghi chú được in nghiêng. "
    "Lớp văn bản OCR đọc 'rms' thành 'nns', 'encapsulant' thành "
    "'cncapsulant' và 'BS 5901,¹⁵' thành 'BS 5901,15'; ảnh trang in là "
    "nguồn quyết định.</p>"
)
