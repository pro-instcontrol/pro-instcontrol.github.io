# -*- coding: utf-8 -*-
"""Tables 10.1–10.5 of McMillan Chapter 10, bilingual EN/VI.

Transcribed from the authoritative page renders (PDF p.252 / printed p.231,
PDF p.256 / printed p.235, PDF p.257 / printed p.236, PDF p.259 / printed
p.238), cross-checked against work/ch10_survey_a.md, ch10_survey_b.md and
work/mcmillan_ch10_brief.md. PDF p.251 / printed p.230 was inspected as the
page preceding Table 10.1; it carries no table.

Structure follows mcmillan_common.table(): HEAD is one cell per column,
ROWS is a list of equal-length cell lists (shared by both languages, as in
the other McMillan table suppliers), CAPTION and NOTE are localized.
Full-width centred/spanning lines that precede the printed columns are
carried as a second line of CAPTION, after the printed caption text.

Printed quirks retained deliberately (with bilingual translator notes):

  * 10.1 volume headers print '≤'; the OCR layer read the sign as '5';
  * 10.1 row labels print '≥'; the OCR layer read the sign as '2';
  * 10.1 source line prints '(from BS/EN 50018)', not 'BS/€N 50028';
  * 10.1 the >2000 cm³ group prints 0.15 / 0.20 / 0.20 in sub-group IIB;
  * 10.2 row labels print '< 12.5', '≥12.5 < 25' and '≥ 25' with unequal
    spacing around the inequality signs;
  * 10.3 every thread-size cell prints a space, including 'M 4' to 'M 8';
  * 10.4 right header prints a capital '(T)' (OCR gave '(0'); the note
    prints '10 mm' with a space (OCR gave '10mm');
  * 10.5 caption prints lower-case 'maximum' (10.6 prints 'Maximum');
  * 10.5 left header carries a superscript 1 on L, printed as 'L¹';
  * 10.5 decimal places vary cell by cell (0.2 versus 0.20).
"""

# ---------------------------------------------------------------------------
# Table 10.1 — printed p.231 (PDF p.252)
# ---------------------------------------------------------------------------

CAPTION101_EN = (
    "Table 10.1 Maximum permitted gaps for flanged joints of various widths"
    "<br>Permissible maximum gaps for given enclosure volumes and sub-groups (mm)"
)
CAPTION101_VI = (
    "Bảng 10.1 Khe hở tối đa cho phép đối với mối nối mặt bích có các chiều "
    "rộng khác nhau"
    "<br>Khe hở tối đa cho phép theo thể tích vỏ bọc và nhóm con đã cho (mm)"
)

HEAD101_EN = [
    "Joint width<br>(L)<br>(mm)",
    "Volume ≤ 100 cm³<br>IIA", "IIB", "IIC",
    "Volume ≤ 500 cm³<br>IIA", "IIB", "IIC",
    "Volume ≤ 2000 cm³<br>IIA", "IIB", "IIC",
    "Volume >2000 cm³<br>IIA", "IIB", "IIC",
]
HEAD101_VI = [
    "Chiều rộng mối nối<br>(L)<br>(mm)",
    "Thể tích ≤ 100 cm³<br>IIA", "IIB", "IIC",
    "Thể tích ≤ 500 cm³<br>IIA", "IIB", "IIC",
    "Thể tích ≤ 2000 cm³<br>IIA", "IIB", "IIC",
    "Thể tích >2000 cm³<br>IIA", "IIB", "IIC",
]

# 13 cells per row: joint width plus 4 volume groups x 3 sub-groups.
ROWS101 = [
    ["≥6.0", "0.3", "0.2", "0.1", "N/P", "N/P", "N/P",
     "N/P", "N/P", "N/P", "N/P", "N/P", "N/P"],
    ["≥9.5", "0.3", "0.2", "0.1", "0.3", "0.2", "N/P",
     "N/P", "N/P", "N/P", "N/P", "N/P", "N/P"],
    ["≥12.5", "0.3", "0.2", "0.1", "0.3", "0.2", "0.1",
     "0.3", "0.2", "N/P", "0.2", "0.15", "N/P"],
    ["≥25.0", "0.4", "0.2", "0.1", "0.4", "0.2", "0.1",
     "0.4", "0.2", "N/P", "0.4", "0.20", "N/P"],
    ["≥40.0", "0.4", "0.2", "0.1", "0.4", "0.2", "0.1",
     "0.4", "0.2", "N/P", "0.4", "0.20", "N/P"],
]

NOTE101_EN = (
    "<p>(from BS/EN 50018)</p>"
    "<p>N/P = Flanged joints are not permitted for this volume of enclosure "
    "and this sub-group</p>"
    "<p>Translator note: the volume headers print the '≤' sign and the row "
    "labels print the '≥' sign; the OCR text layer misread them as '5' and "
    "'2' respectively.</p>"
    "<p>Translator note: the source line prints '(from BS/EN 50018)'; the "
    "OCR text layer read '(from BS/€N 50028)'.</p>"
    "<p>Translator note: in the >2000 cm³ group sub-group IIB prints 0.15 "
    "at row ≥12.5 and 0.20 at rows ≥25.0 and ≥40.0; retained cell by cell.</p>"
)
NOTE101_VI = (
    "<p>(theo BS/EN 50018)</p>"
    "<p>N/P = Không cho phép dùng mối nối mặt bích cho thể tích vỏ bọc và "
    "nhóm con này</p>"
    "<p>Ghi chú của người dịch: các tiêu đề thể tích in dấu '≤' và nhãn các "
    "hàng in dấu '≥'; lớp văn bản OCR đọc nhầm lần lượt thành '5' và '2'.</p>"
    "<p>Ghi chú của người dịch: dòng nguồn in '(from BS/EN 50018)'; lớp văn "
    "bản OCR đọc là '(from BS/€N 50028)'.</p>"
    "<p>Ghi chú của người dịch: trong nhóm >2000 cm³, nhóm con IIB in 0.15 "
    "ở hàng ≥12.5 và 0.20 ở các hàng ≥25.0, ≥40.0; giữ nguyên từng ô.</p>"
)

# ---------------------------------------------------------------------------
# Table 10.2 — printed p.235 (PDF p.256)
# ---------------------------------------------------------------------------

CAPTION102_EN = (
    "Table 10.2 Geometry of joint where bolts pass through it"
)
CAPTION102_VI = (
    "Bảng 10.2 Hình học của mối nối nơi bulông đi xuyên qua"
)

HEAD102_EN = [
    "Joint width<br>(L)<br>(mm)",
    "Length of flamepath between<br>enclosure and exterior<br>(l)<br>(mm)",
]
HEAD102_VI = [
    "Chiều rộng mối nối<br>(L)<br>(mm)",
    "Chiều dài đường cháy lan giữa<br>vỏ bọc và môi trường ngoài<br>(l)<br>(mm)",
]

ROWS102 = [
    ["< 12.5", "6"],
    ["≥12.5 < 25", "8"],
    ["≥ 25", "9"],
]

NOTE102_EN = (
    "<p>See Fig. 10.4 to see geometry of reduced joint width where bolts "
    "pass through the flamepath.</p>"
    "<p>Translator note: the three row labels print '< 12.5', '≥12.5 < 25' "
    "and '≥ 25', with unequal spacing around the inequality signs; the "
    "second label has no space after '≥'. Retained verbatim.</p>"
)
NOTE102_VI = (
    "<p>Xem Hình 10.4 để thấy hình học của chiều rộng mối nối được giảm "
    "ở những chỗ bulông đi xuyên qua đường cháy lan.</p>"
    "<p>Ghi chú của người dịch: ba nhãn hàng in '< 12.5', '≥12.5 < 25' và "
    "'≥ 25', với khoảng cách không đều quanh các dấu bất đẳng thức; nhãn "
    "thứ hai không có dấu cách sau '≥'. Giữ nguyên theo bản in.</p>"
)

# ---------------------------------------------------------------------------
# Table 10.3 — printed p.235 (PDF p.256)
# ---------------------------------------------------------------------------

CAPTION103_EN = (
    "Table 10.3 Bolt clearance holes which penetrate enclosure flange flamepath"
)
CAPTION103_VI = (
    "Bảng 10.3 Lỗ lọt bulông xuyên qua đường cháy lan của mặt bích vỏ bọc"
)

HEAD103_EN = [
    "Thread size<br>(mm)",
    "Diameter of clearance<br>hole (nominal)<br>(mm)",
]
HEAD103_VI = [
    "Kích thước ren<br>(mm)",
    "Đường kính lỗ lọt<br>(danh nghĩa)<br>(mm)",
]

ROWS103 = [
    ["M 4", "4.5"],
    ["M 5", "5.5"],
    ["M 6", "6.6"],
    ["M 8", "9.0"],
    ["M 10", "11.0"],
    ["M 12", "14.0"],
    ["M 14", "16.0"],
    ["M 16", "18.0"],
    ["M 20", "22.0"],
    ["M 24", "26.0"],
]

NOTE103_EN = (
    "<p>(from BS/EN 50014)</p>"
    "<p>Note: For other sizes clearance holes should be in accordance with "
    "not worse than a medium tolerance fit of H13 in accordance with "
    "BS 4500 (1990).</p>"
    "<p>Translator note: every thread-size cell prints a space between 'M' "
    "and the number, including 'M 4', 'M 5', 'M 6' and 'M 8'; the OCR text "
    "layer dropped those four spaces.</p>"
)
NOTE103_VI = (
    "<p>(theo BS/EN 50014)</p>"
    "<p>Ghi chú: Đối với các kích thước khác, lỗ lọt phải phù hợp với dung "
    "sai không kém hơn mức trung bình H13 theo BS 4500 (1990).</p>"
    "<p>Ghi chú của người dịch: mỗi ô kích thước ren đều in dấu cách giữa "
    "'M' và chữ số, kể cả 'M 4', 'M 5', 'M 6', 'M 8'; lớp văn bản OCR đã "
    "bỏ bốn dấu cách đó.</p>"
)

# ---------------------------------------------------------------------------
# Table 10.4 — printed p.236 (PDF p.257)
# ---------------------------------------------------------------------------

CAPTION104_EN = (
    "Table 10.4 Minimum thickness of wall between thread and interior of enclosure"
)
CAPTION104_VI = (
    "Bảng 10.4 Chiều dày tối thiểu của thành giữa ren và bên trong vỏ bọc"
)

HEAD104_EN = [
    "Thread size<br>(mm)",
    "Minimum thickness of wall<br>(T)<br>(mm)",
]
HEAD104_VI = [
    "Kích thước ren<br>(mm)",
    "Chiều dày tối thiểu của thành<br>(T)<br>(mm)",
]

ROWS104 = [
    ["M 4", "3.0"],
    ["M 5", "3.0"],
    ["M 6", "3.0"],
    ["M 8", "3.0"],
    ["M 10", "3.4"],
    ["M 12", "4.0"],
    ["M 14", "4.7"],
    ["M 16", "5.4"],
    ["M 20", "6.7"],
    ["M 24", "8.0"],
]

NOTE104_EN = (
    "<p>Note: For other diameters above 10 mm use one third of thread "
    "diameter for minimum thickness.</p>"
    "<p>Translator note: the right header prints a capital '(T)' (the OCR "
    "text layer read '(0'); the note prints '10 mm' with a space (the OCR "
    "text layer read '10mm').</p>"
)
NOTE104_VI = (
    "<p>Ghi chú: Đối với các đường kính khác trên 10 mm, lấy một phần ba "
    "đường kính ren làm chiều dày tối thiểu.</p>"
    "<p>Ghi chú của người dịch: tiêu đề bên phải in chữ hoa '(T)' (lớp văn "
    "bản OCR đọc là '(0'); ghi chú in '10 mm' có dấu cách (lớp văn bản OCR "
    "đọc là '10mm').</p>"
)

# ---------------------------------------------------------------------------
# Table 10.5 — printed p.238 (PDF p.259)
# ---------------------------------------------------------------------------

CAPTION105_EN = (
    "Table 10.5 maximum permitted gaps for composite spigot joints of "
    "various widths"
    "<br>Permissible maximum gaps for given enclosure volumes and sub-groups (mm)"
)
CAPTION105_VI = (
    "Bảng 10.5 khe hở tối đa cho phép đối với mối nối dạng chốt lồng ghép "
    "có các chiều rộng khác nhau"
    "<br>Khe hở tối đa cho phép theo thể tích vỏ bọc và nhóm con đã cho (mm)"
)

HEAD105_EN = [
    "Joint width<br>L¹<br>(mm)",
    "Volume ≤ 100 cm³<br>IIA", "IIB", "IIC",
    "Volume ≤ 500 cm³<br>IIA", "IIB", "IIC",
    "Volume ≤ 2000 cm³<br>IIA", "IIB", "IIC",
    "Volume > 2000 cm³<br>IIA", "IIB", "IIC",
]
HEAD105_VI = [
    "Chiều rộng mối nối<br>L¹<br>(mm)",
    "Thể tích ≤ 100 cm³<br>IIA", "IIB", "IIC",
    "Thể tích ≤ 500 cm³<br>IIA", "IIB", "IIC",
    "Thể tích ≤ 2000 cm³<br>IIA", "IIB", "IIC",
    "Thể tích > 2000 cm³<br>IIA", "IIB", "IIC",
]

# 13 cells per row: joint width plus 4 volume groups x 3 sub-groups.
ROWS105 = [
    ["≥ 6.0", "0.3", "0.2", "N/P", "N/P", "N/P", "N/P",
     "N/P", "N/P", "N/P", "N/P", "N/P", "N/P"],
    ["≥ 9.5", "0.3", "0.2", "N/P", "0.3", "0.2", "N/P",
     "N/P", "N/P", "N/P", "N/P", "N/P", "N/P"],
    ["≥ 12.5", "0.3", "0.2", "0.15", "0.3", "0.2", "0.15",
     "0.3", "0.2", "0.15", "0.2", "0.15", "N/P"],
    ["≥ 25.0", "0.4", "0.2", "0.18", "0.4", "0.2", "0.18",
     "0.4", "0.2", "0.18", "0.4", "0.20", "0.18"],
    ["≥ 40.0", "0.4", "0.2", "0.20", "0.4", "0.2", "0.20",
     "0.4", "0.2", "0.20", "0.4", "0.2", "0.20"],
]

NOTE105_EN = (
    "<p>(from BS/EN 50018)</p>"
    "<p>N/P = Spigot joints are not permitted for this enclosure volume "
    "and this sub-group.</p>"
    "<p>Translator note: the caption prints 'maximum' with a lower-case m; "
    "the Table 10.6 caption on printed p.241 prints 'Maximum' with a "
    "capital M. Reproduced as printed.</p>"
    "<p>Translator note: the left header carries a superscript 1 on L "
    "(L¹); the OCR text layer read it as L'.</p>"
    "<p>Translator note: decimal places vary cell by cell, for example "
    "'0.2' beside '0.20' in the > 2000 cm³ group; retained as printed.</p>"
)
NOTE105_VI = (
    "<p>(theo BS/EN 50018)</p>"
    "<p>N/P = Không cho phép dùng mối nối dạng chốt lồng cho thể tích vỏ "
    "bọc và nhóm con này.</p>"
    "<p>Ghi chú của người dịch: tiêu đề in 'maximum' với chữ m thường; "
    "tiêu đề Bảng 10.6 ở trang in 241 in 'Maximum' với chữ M hoa. Giữ "
    "nguyên theo bản in.</p>"
    "<p>Ghi chú của người dịch: tiêu đề bên trái có chỉ số trên 1 trên L "
    "(L¹); lớp văn bản OCR đọc là L'.</p>"
    "<p>Ghi chú của người dịch: số chữ số thập phân thay đổi từng ô, ví dụ "
    "'0.2' cạnh '0.20' trong nhóm > 2000 cm³; giữ nguyên theo bản in.</p>"
)
