# -*- coding: utf-8 -*-
"""Tables 10.6–10.10 of McMillan Chapter 10, bilingual EN/VI.

Transcribed from the authoritative page renders (printed p.241 / PDF p.262;
printed p.247 / PDF p.268; printed p.249 / PDF p.270; printed p.251 / PDF
p.272), cross-checked against work/ch10_survey_b.md and ch10_survey_c.md.
Printed p.252 / PDF p.273 (Table 10.11) was inspected for the scope note
that bears on Table 10.10's caption.

Structure follows mcmillan_common.table(): HEAD is one cell per column,
ROWS is a list of equal-length cell lists (shared by both languages, as in
the other McMillan table suppliers), CAPTION and NOTE are localized.
Full-width centred/spanning lines that precede the printed columns are
carried as a second line of CAPTION, after the printed caption text.

Printed quirks retained deliberately (with bilingual translator notes):

  * 10.6 caption prints capital 'Maximum' (10.5 prints 'maximum');
  * 10.6 row labels use the '≥' sign, misread as '1' by the OCR layer;
  * 10.6 row ≥ 12.5 / ≤ 100 cm³ / IIB prints '0.02' (sic; likely 0.2);
  * 10.6 last cell prints '0.2' while neighbours print '0.20';
  * 10.8 first row prints 'At least 0.9 mm (see notes 1 and 2' with no
    closing parenthesis;
  * 10.9 caption is set over four lines in print;
  * 10.10 second volume header prints 'Volume 500 cm³' with no '<=' sign;
  * 10.10 decimal places vary cell by cell (0.3 / 0.30 / 0.2 / 0.20);
  * 10.10 source line is '(BS/EN 50018)' without 'from';
  * 10.10 note prints 'subgroup IIC' (no hyphen), 10.11 'this sub-group'.
"""

# ---------------------------------------------------------------------------
# Table 10.6 — printed p.241 (PDF p.262)
# ---------------------------------------------------------------------------

CAPTION106_EN = (
    "Table 10.6 Maximum permitted gaps for simple spigot joints of various widths"
    "<br>Permissible maximum gaps for given enclosure volumes and sub-groups (mm)"
)
CAPTION106_VI = (
    "Bảng 10.6 Khe hở tối đa cho phép đối với mối nối dạng chốt lồng đơn giản "
    "có các chiều rộng khác nhau"
    "<br>Khe hở tối đa cho phép theo thể tích vỏ bọc và nhóm con đã cho (mm)"
)

HEAD106_EN = [
    "Joint width<br>(L)<br>(mm)",
    "Volume ≤ 100 cm³<br>IIA", "IIB", "IIC",
    "Volume ≤ 500 cm³<br>IIA", "IIB", "IIC",
    "Volume ≤ 2000 cm³<br>IIA", "IIB", "IIC",
    "Volume > 2000 cm³<br>IIA", "IIB", "IIC",
]
HEAD106_VI = [
    "Chiều rộng mối nối<br>(L)<br>(mm)",
    "Thể tích ≤ 100 cm³<br>IIA", "IIB", "IIC",
    "Thể tích ≤ 500 cm³<br>IIA", "IIB", "IIC",
    "Thể tích ≤ 2000 cm³<br>IIA", "IIB", "IIC",
    "Thể tích > 2000 cm³<br>IIA", "IIB", "IIC",
]

# 13 cells per row: joint width plus 4 volume groups x 3 sub-groups.
ROWS106 = [
    ["≥ 6.0", "0.3", "0.2", "0.10", "N/P", "N/P", "0.10",
     "N/P", "N/P", "N/P", "N/P", "N/P", "N/P"],
    ["≥ 9.5", "0.3", "0.2", "0.10", "0.3", "0.2", "0.10",
     "N/P", "N/P", "N/P", "N/P", "N/P", "N/P"],
    ["≥ 12.5", "0.3", "0.02", "0.15", "0.3", "0.2", "0.15",
     "0.3", "0.2", "0.15", "0.2", "0.15", "N/P"],
    ["≥ 25.0", "0.4", "0.2", "0.15", "0.4", "0.2", "0.15",
     "0.4", "0.2", "0.15", "0.4", "0.20", "0.15"],
    ["≥ 40.0", "0.4", "0.2", "0.20", "0.4", "0.2", "0.20",
     "0.4", "0.2", "0.20", "0.4", "0.20", "0.2"],
]

NOTE106_EN = (
    "<p>(from BS/EN 50018)</p>"
    "<p>N/P = Spigot joints are not permitted for enclosures of this volume "
    "in this sub-group</p>"
    "<p>Translator note: the caption prints 'Maximum' with a capital M; the "
    "Table 10.5 caption on printed p.238 prints 'maximum' with a lower-case m. "
    "Reproduced as printed.</p>"
    "<p>Translator note: the row labels print the '≥' sign; the OCR text layer "
    "misreads it as the digit '1'.</p>"
    "<p>Translator note: the cell at row ≥ 12.5, Volume ≤ 100 cm³, sub-group "
    "IIB prints '0.02' (sic; likely 0.2). Retained as printed.</p>"
    "<p>Translator note: the final cell (row ≥ 40.0, Volume > 2000 cm³, IIC) "
    "prints '0.2' while neighbouring cells print '0.20'; decimal places are "
    "retained cell by cell.</p>"
)
NOTE106_VI = (
    "<p>(theo BS/EN 50018)</p>"
    "<p>N/P = Không cho phép dùng mối nối dạng chốt lồng cho vỏ bọc có thể tích "
    "này trong nhóm con này</p>"
    "<p>Ghi chú của người dịch: tiêu đề in 'Maximum' với chữ M hoa; tiêu đề "
    "Bảng 10.5 ở trang in 238 in 'maximum' với chữ m thường. Giữ nguyên theo "
    "bản in.</p>"
    "<p>Ghi chú của người dịch: nhãn các hàng in dấu '≥'; lớp văn bản OCR đọc "
    "nhầm thành chữ số '1'.</p>"
    "<p>Ghi chú của người dịch: ô tại hàng ≥ 12.5, Thể tích ≤ 100 cm³, nhóm con "
    "IIB in '0.02' (có thể là lỗi in, đáng lẽ 0,2). Giữ nguyên theo bản in.</p>"
    "<p>Ghi chú của người dịch: ô cuối cùng (hàng ≥ 40.0, Thể tích > 2000 cm³, "
    "IIC) in '0.2' trong khi các ô kề bên in '0.20'; giữ nguyên số chữ số thập "
    "phân của từng ô.</p>"
)

# ---------------------------------------------------------------------------
# Table 10.7 — printed p.247 (PDF p.268)
# ---------------------------------------------------------------------------

CAPTION107_EN = (
    "Table 10.7 Thread requirements for cylindrical (parallel) threaded joints"
    "<br>Cylindrical (parallel) threaded joints"
)
CAPTION107_VI = (
    "Bảng 10.7 Yêu cầu về ren đối với mối nối ren trụ (song song)"
    "<br>Mối nối ren trụ (song song)"
)

# The printed table has no column-heading row; its centred heading is carried
# in CAPTION, so the two header cells are deliberately empty.
HEAD107_EN = ["", ""]
HEAD107_VI = ["", ""]

ROWS107 = [
    ["Thread pitch", "0.7 mm min to 2 mm max (see note)"],
    ["Thread form and fit quality according to ISO 965/1 and ISO 965/3",
     "Medium or fine tolerance"],
    ["No. of threads engaged", "Minimum 5"],
    ["Depth of engagement in", ""],
    ["Enclosure wall:", ""],
    ["Enclosure Volume ≤ 100 cm³", "At least 5 mm"],
    ["Enclosure Volume >100 cm³", "At least 8 mm"],
]

NOTE107_EN = (
    "<p>(from BS/EN 50018)</p>"
    "<p>Note: If this pitch is exceeded then requirements in addition to this "
    "table may be necessary (see text).</p>"
)
NOTE107_VI = (
    "<p>(theo BS/EN 50018)</p>"
    "<p>Ghi chú: Nếu vượt quá bước ren này thì có thể cần các yêu cầu bổ sung "
    "ngoài bảng này (xem nội dung chính).</p>"
)

# ---------------------------------------------------------------------------
# Table 10.8 — printed p.247 (PDF p.268)
# ---------------------------------------------------------------------------

CAPTION108_EN = (
    "Table 10.8 Cylindrical (taper) threaded joints"
    "<br>Cylindrical (taper) threaded joints"
)
CAPTION108_VI = (
    "Bảng 10.8 Mối nối ren trụ (côn)"
    "<br>Mối nối ren trụ (côn)"
)

HEAD108_EN = ["", ""]
HEAD108_VI = ["", ""]

ROWS108 = [
    ["Pitch", "At least 0.9 mm (see notes 1 and 2"],  # no closing ')' in print
    ["Threads engaged", "5 Nominal (see note 3)"],
    ["Threads provided on each part", "At least 6"],
]

NOTE108_EN = (
    "<p>(from BS/EN 50018)</p>"
    "<p>1 There is no maximum pitch in this case as the joint is tight fitting.</p>"
    "<p>2 The cone angle on the taper shall be the same for both parts of the "
    "threaded joint.</p>"
    "<p>3 It is accepted that at the limit of tolerance less than 5 threads may "
    "be engaged because the tightness of fit will allow the flameproof "
    "properties of the joint to be maintained even in such cases.</p>"
    "<p>Translator note: the first row prints 'At least 0.9 mm (see notes 1 and 2' "
    "with no closing parenthesis; retained verbatim, not repaired.</p>"
)
NOTE108_VI = (
    "<p>(theo BS/EN 50018)</p>"
    "<p>1 Trong trường hợp này không có bước ren tối đa vì mối nối lắp khít.</p>"
    "<p>2 Góc côn của phần ren côn phải như nhau ở cả hai chi tiết của mối nối ren.</p>"
    "<p>3 Chấp nhận rằng ở giới hạn dung sai có thể chỉ có chưa đầy 5 ren ăn khớp, "
    "vì độ khít của lắp ghép vẫn duy trì được đặc tính chống cháy nổ của mối nối "
    "trong những trường hợp đó.</p>"
    "<p>Ghi chú của người dịch: hàng đầu in 'At least 0.9 mm (see notes 1 and 2' "
    "mà thiếu dấu ngoặc đóng; giữ nguyên theo bản in, không sửa lại.</p>"
)

# ---------------------------------------------------------------------------
# Table 10.9 — printed p.249 (PDF p.270)
# ---------------------------------------------------------------------------

CAPTION109_EN = (
    "Table 10.9 Minimum lengths of cemented joints not complying with joint "
    "requirements in the absence of cement"
    "<br>Length of cemented joints"
)
CAPTION109_VI = (
    "Bảng 10.9 Chiều dài tối thiểu của mối nối xi măng không đáp ứng các yêu cầu "
    "về mối nối khi không có xi măng"
    "<br>Chiều dài của mối nối xi măng"
)

HEAD109_EN = ["Enclosure volume<br>cm³", "Joint length<br>mm"]
HEAD109_VI = ["Thể tích vỏ bọc<br>cm³", "Chiều dài mối nối<br>mm"]

ROWS109 = [
    ["Less than 10", "At least 3"],
    ["Over 10 and up to 100", "At least 6"],
    ["Over 100", "At least 10"],
]

NOTE109_EN = (
    "<p>(from BS/EN 50018)</p>"
    "<p>Translator note: the printed caption is set over four lines; the line "
    "breaks are a layout feature of the source and the wording is reproduced "
    "verbatim.</p>"
)
NOTE109_VI = (
    "<p>(theo BS/EN 50018)</p>"
    "<p>Ghi chú của người dịch: tiêu đề bản in được xếp trên bốn dòng; ngắt dòng "
    "chỉ là đặc điểm trình bày của bản gốc, nội dung được giữ nguyên.</p>"
)

# ---------------------------------------------------------------------------
# Table 10.10 — printed p.251 (PDF p.272)
# ---------------------------------------------------------------------------

CAPTION1010_EN = (
    "Table 10.10 Maximum permissible gaps for cylindrical joints of operating "
    "rods and shafts of rotating machines with sleeve bearings"
    "<br>Permissible maximum gaps for given enclosure volumes"
)
CAPTION1010_VI = (
    "Bảng 10.10 Khe hở tối đa cho phép đối với mối nối trụ của thanh truyền động "
    "và trục của máy quay có ổ bi dạng bạc"
    "<br>Khe hở tối đa cho phép theo thể tích vỏ bọc đã cho"
)

# The second volume header prints 'Volume 500 cm³' with NO inequality sign.
HEAD1010_EN = [
    "Joint width<br>(L)<br>(mm)",
    "Volume ≤ 100 cm³<br>IIA", "IIB", "IIC",
    "Volume 500 cm³<br>IIA", "IIB", "IIC",
    "Volume ≤ 2000 cm³<br>IIA", "IIB", "IIC",
    "Volume >2000 cm³<br>IIA", "IIB", "IIC",
]
HEAD1010_VI = [
    "Chiều rộng mối nối<br>(L)<br>(mm)",
    "Thể tích ≤ 100 cm³<br>IIA", "IIB", "IIC",
    "Thể tích 500 cm³<br>IIA", "IIB", "IIC",
    "Thể tích ≤ 2000 cm³<br>IIA", "IIB", "IIC",
    "Thể tích >2000 cm³<br>IIA", "IIB", "IIC",
]

# 13 cells per row; decimal places preserved exactly as printed.
ROWS1010 = [
    ["≥6.0", "0.30", "0.20", "0.10", "N/P", "N/P", "N/P",
     "N/P", "N/P", "N/P", "N/P", "N/P", "N/P"],
    ["≥9.5", "0.30", "0.20", "0.10", "0.3", "0.20", "0.10",
     "N/P", "N/P", "N/P", "N/P", "N/P", "N/P"],
    ["≥12.5", "0.35", "0.25", "0.15", "0.3", "0.20", "0.15",
     "0.3", "0.20", "0.15", "0.2", "N/P", "N/P"],
    ["≥25.0", "0.40", "0.30", "0.15", "0.4", "0.25", "0.15",
     "0.4", "0.25", "0.15", "0.4", "0.20", "0.15"],
    ["≥40.0", "0.50", "0.40", "0.20", "0.5", "0.30", "0.20",
     "0.5", "0.30", "0.20", "0.5", "0.25", "0.20"],
]

NOTE1010_EN = (
    "<p>(BS/EN 50018)</p>"
    "<p>N/P = Joints of this width and/or this sub-group are not permitted when "
    "sleeve bearings are used.</p>"
    "<p>Note: Sleeve bearings are not permitted for subgroup IIC rotating "
    "electrical machines.</p>"
    "<p>Translator note: the second volume header prints 'Volume 500 cm³' with "
    "no inequality sign, unlike the other three columns; as printed; logically "
    "≤ 500 cm³. Retained verbatim.</p>"
    "<p>Translator note: decimal places vary cell by cell (0.3 / 0.30 / 0.2 / "
    "0.20) in nominally identical columns; retained verbatim.</p>"
    "<p>Translator note: the source line prints '(BS/EN 50018)' without 'from', "
    "whereas Tables 10.7–10.9 print '(from BS/EN 50018)'; retained as printed.</p>"
    "<p>Translator note: this note prints 'subgroup IIC' with no hyphen, while "
    "Table 10.11 prints 'this sub-group'; retained as printed.</p>"
    "<p>Translator note: Table 10.11 on printed p.252 states that it is not "
    "valid for shafts and rotating machines, while Table 10.10's caption covers "
    "both operating rods and shafts of rotating machines with sleeve bearings. "
    "Retain the scope distinction: Table 10.11 = operating rods only; Table "
    "10.12 = shafts and rotating machines.</p>"
)
NOTE1010_VI = (
    "<p>(BS/EN 50018)</p>"
    "<p>N/P = Không cho phép dùng mối nối có chiều rộng và/hoặc nhóm con này khi "
    "sử dụng ổ bi dạng bạc.</p>"
    "<p>Ghi chú: Không cho phép dùng ổ bi dạng bạc cho máy điện quay thuộc nhóm "
    "con IIC.</p>"
    "<p>Ghi chú của người dịch: tiêu đề thể tích thứ hai in 'Volume 500 cm³' mà "
    "không có dấu bất đẳng thức, khác với ba cột còn lại; ghi theo bản gốc; về "
    "logic là ≤ 500 cm³. Giữ nguyên theo bản in.</p>"
    "<p>Ghi chú của người dịch: số chữ số thập phân thay đổi từng ô (0.3 / 0.30 / "
    "0.2 / 0.20) ở các cột về danh nghĩa giống nhau; giữ nguyên theo bản in.</p>"
    "<p>Ghi chú của người dịch: dòng nguồn in '(BS/EN 50018)' mà không có 'from', "
    "trong khi các Bảng 10.7–10.9 in '(from BS/EN 50018)'; giữ nguyên theo bản in.</p>"
    "<p>Ghi chú của người dịch: ghi chú này in 'subgroup IIC' không có dấu gạch "
    "nối, còn Bảng 10.11 in 'this sub-group'; giữ nguyên theo bản in.</p>"
    "<p>Ghi chú của người dịch: Bảng 10.11 ở trang in 252 nêu rõ bảng đó không "
    "áp dụng cho trục và máy quay, trong khi tiêu đề Bảng 10.10 bao gồm cả thanh "
    "truyền động lẫn trục của máy quay có ổ bi dạng bạc. Giữ nguyên sự phân biệt "
    "phạm vi: Bảng 10.11 chỉ cho thanh truyền động; Bảng 10.12 cho trục và máy "
    "quay.</p>"
)
