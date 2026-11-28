# -*- coding: utf-8 -*-
"""Tables 12.1 to 12.4 of McMillan Chapter 12, bilingual EN/VI.

Transcribed from the authoritative page renders:
  - PDF p.323 / printed p.302 -> Table 12.1 + its source line and 3 footnotes
  - PDF p.329 / printed p.308 -> Table 12.2 + source line and Note
  - PDF p.330 / printed p.309 -> Table 12.3
  - PDF p.331 / printed p.310 -> Table 12.4 + its 3 printed Notes

Cross-checked against work/mcmillan_ch12_brief.md, SURVEYS B and C. The text
layer is materially garbled in all four tables; the page images govern. Survey
C places Table 12.3 on PDF p.330, not p.329; the render confirms p.330.

Structure follows mcmillan_tbl11_1_2.py: HEAD is one cell per column, ROWS is a
list of equal-length cell lists, CAPTION and NOTE are localized. Spanning
over-headers are carried as extra lines of CAPTION so the flat HEAD/ROWS shape
stays intact.

Tables 12.1 and 12.2 have only numeric/symbolic row cells, so their VI rows may
share the printed rows. Tables 12.3 and 12.4 contain connector words in their
row labels, so genuine Vietnamese row lists are exported alongside the printed
English rows.

Printed quirks retained deliberately (with bilingual translator notes):

  * 12.1 'Minimum creepage distance (mm)' spans the three material-group
    columns; group heads print superscript footnote digits I¹ II² IIIa³;
    the final column prints lowercase 'minimum clearance (mm)';
  * 12.1 footnote source prints '(from BS/EN 50019)' with a slash, although
    Survey B transcribed '(from BS EN 50019)'; all voltage ranges print a
    strict '<' and a '≤';
  * 12.2 caption prints '≤600' and wraps over four hyphenated print lines;
    the note prints '250 V' with a space;
  * 12.3 prints 'e.g.,' with a comma, lowercase brand names, en-dash ranges
    and '+' suffixes on '200–700+' and '700+';
  * 12.4 '(note 3)' sits under the Method column, 'Thermal material insulation
    class (notes 1 and 2)' spans the five class columns, the machine row
    prints a subscript e in 'tₑ', and Note 3 has no terminal full stop.
"""

# ---------------------------------------------------------------------------
# Table 12.1 — printed p.302 (PDF p.323)
# ---------------------------------------------------------------------------

CAPTION121_EN = (
    "Table 12.1 Minimum creepage and clearance distances"
    "<br>Minimum creepage distance (mm)"
)
CAPTION121_VI = (
    "Bảng 12.1 Khoảng cách bò và khoảng hở nhỏ nhất"
    "<br>Khoảng cách bò nhỏ nhất (mm)"
)

HEAD121_EN = [
    "Working<br>voltage U<br>(rms)",
    "Material<br>Group I¹",
    "Material<br>Group II²",
    "Material<br>Group IIIa³",
    "minimum<br>clearance<br>(mm)",
]
HEAD121_VI = [
    "Điện áp làm việc U<br>(rms)",
    "Vật liệu<br>Nhóm I¹",
    "Vật liệu<br>Nhóm II²",
    "Vật liệu<br>Nhóm IIIa³",
    "khoảng hở<br>nhỏ nhất<br>(mm)",
]

# 5 cells per row: voltage range + three material-group distances + clearance.
ROWS121 = [
    ["0< U ≤15", "1.6", "1.6", "1.6", "1.6"],
    ["15< U ≤30", "1.8", "1.8", "1.8", "1.8"],
    ["30< U ≤60", "2.1", "2.6", "3.4", "2.1"],
    ["60< U ≤110", "2.5", "3.2", "4.0", "2.5"],
    ["110< U ≤175", "3.2", "4.0", "5.0", "3.2"],
    ["175< U ≤275", "5.0", "6.3", "8.0", "5.0"],
    ["275< U ≤420", "8.0", "10.0", "12.5", "6.0"],
    ["420< U ≤550", "10.0", "12.5", "16.0", "8.0"],
    ["550< U ≤750", "12.0", "16.0", "20.0", "10.0"],
    ["750< U ≤1100", "20.0", "25.0", "32.0", "14.0"],
    ["1100< U ≤2200", "32.0", "36.0", "40.0", "30.0"],
    ["2200< U ≤3300", "40.0", "45.0", "50.0", "36.0"],
    ["3300< U ≤4200", "50.0", "56.0", "63.0", "44.0"],
    ["4200< U ≤5500", "63.0", "71.0", "80.0", "50.0"],
    ["5500< U ≤6600", "80.0", "90.0", "100.0", "60.0"],
    ["6600< U ≤8300", "100.0", "110.0", "125.0", "80.0"],
    ["8300< U ≤11000", "125.0", "140.0", "160.0", "100.0"],
]
ROWS121_EN = ROWS121
# Every cell is a voltage symbol or a number: no connector words to translate.
ROWS121_VI = ROWS121

NOTE121_EN = (
    "<p>(from BS/EN 50019)</p>"
    "<p>1 = Material Group I has a CTI of at least 600</p>"
    "<p>2 = Material Group II has a CTI of at least 400</p>"
    "<p>3 = Material Group IIIa has a CTI of at least 175</p>"
    "<p>Translator note: the spanning over-header 'Minimum creepage distance "
    "(mm)' covers the three material-group columns and is carried in the "
    "caption (second line). The sub-heads print 'Material Group I¹', "
    "'Material Group II²' and 'Material Group IIIa³' with superscript "
    "footnote digits, while the last column prints lowercase 'minimum "
    "clearance (mm)'.</p>"
    "<p>Translator note: every voltage range was corrupted in the OCR text "
    "layer (e.g. '0< U (15', '550~ U5750', '7501 U ill00', '42001 U 55500'); "
    "the page render shows a strict '<' on the left and a '≤' on the right "
    "and governs here.</p>"
    "<p>Translator note: the italic source line prints '(from BS/EN 50019)' "
    "with a slash; Survey B of work/mcmillan_ch12_brief.md transcribed '(from "
    "BS EN 50019)' without it. The render governs, and the slash form also "
    "matches the Table 12.2 source line.</p>"
)

NOTE121_VI = (
    "<p>(theo BS/EN 50019)</p>"
    "<p>1 = Vật liệu Nhóm I có CTI ít nhất 600</p>"
    "<p>2 = Vật liệu Nhóm II có CTI ít nhất 400</p>"
    "<p>3 = Vật liệu Nhóm IIIa có CTI ít nhất 175</p>"
    "<p>Ghi chú của người dịch: tiêu đề phía trên 'Minimum creepage distance "
    "(mm)' trải rộng trên ba cột nhóm vật liệu được đưa vào dòng thứ hai của "
    "CAPTION. Các tiêu đề phụ in 'Material Group I¹', 'Material Group II²' và "
    "'Material Group IIIa³' với các chỉ số trên là số ghi chú; cột cuối in "
    "thường 'minimum clearance (mm)'.</p>"
    "<p>Ghi chú của người dịch: mọi khoảng điện áp đều bị hỏng trong lớp văn "
    "bản OCR (ví dụ '0< U (15', '550~ U5750', '7501 U ill00', '42001 U "
    "55500'); ảnh trang in '<' nghiêm ngặt bên trái và '≤' bên phải và là "
    "nguồn quyết định.</p>"
    "<p>Ghi chú của người dịch: dòng nguồn in nghiêng '(from BS/EN 50019)' có "
    "dấu gạch chéo; Survey B trong work/mcmillan_ch12_brief.md chép là '(from "
    "BS EN 50019)' không có dấu này. Ảnh trang in là nguồn quyết định và dạng "
    "có gạch chéo cũng khớp với dòng nguồn của Bảng 12.2.</p>"
)

# ---------------------------------------------------------------------------
# Table 12.2 — printed p.308 (PDF p.329)
# ---------------------------------------------------------------------------

CAPTION122_EN = (
    "Table 12.2 Creepage and clearance distances for screw lampcaps and "
    "lampholders with insulation having a CTI of ≤600"
)
CAPTION122_VI = (
    "Bảng 12.2 Khoảng cách bò và khoảng hở cho đầu đèn ren và giá đèn có "
    "lớp cách điện có CTI ≤600"
)

HEAD122_EN = [
    "Working voltage<br>V (rms)",
    "Creepage distance<br>and clearance<br>(mm)",
]
HEAD122_VI = [
    "Điện áp làm việc<br>V (rms)",
    "Khoảng cách bò<br>và khoảng hở<br>(mm)",
]

# 2 cells per row: voltage range + the single distance value.
ROWS122 = [
    ["0< U ≤60", "2"],
    ["60< U ≤250", "3"],
]
ROWS122_EN = ROWS122
# Both cells of each row are purely symbolic/numeric.
ROWS122_VI = ROWS122

NOTE122_EN = (
    "<p>(from BS/EN 50019)</p>"
    "<p>Note: For lamps of over 250 V Table 12.1 applies</p>"
    "<p>Translator note: the caption prints '≤600' and wraps over four "
    "centred print lines with hyphenated line-break splits ('dis-tances', "
    "'insu-lation'); the unhyphenated wording is given as one string. The OCR "
    "text layer read the '≤' in the caption as '('.</p>"
    "<p>Translator note: both voltage ranges print a strict '<' on the left "
    "and a '≤' on the right (the OCR text layer read '0< U 160' and '60< U "
    "5250'); the printed Note spaces '250 V'. The source line and the Note "
    "are italicised in print.</p>"
)

NOTE122_VI = (
    "<p>(theo BS/EN 50019)</p>"
    "<p>Ghi chú: Đối với đèn có điện áp trên 250 V, áp dụng Bảng 12.1</p>"
    "<p>Ghi chú của người dịch: nhan đề in '≤600' và được ngắt thành bốn dòng "
    "in căn giữa có gạch nối khi xuống dòng ('dis-tances', 'insu-lation'); "
    "toàn bộ câu được ghi không ngắt và không gạch nối. Lớp văn bản OCR đọc "
    "dấu '≤' trong nhan đề là '('.</p>"
    "<p>Ghi chú của người dịch: cả hai khoảng điện áp đều in '<' nghiêm ngặt "
    "bên trái và '≤' bên phải (lớp văn bản OCR đọc là '0< U 160' và '60< U "
    "5250'); dòng Ghi chú in '250 V' có dấu cách. Dòng nguồn và dòng Ghi chú "
    "được in nghiêng.</p>"
)

# ---------------------------------------------------------------------------
# Table 12.3 — printed p.309 (PDF p.330)
# ---------------------------------------------------------------------------

CAPTION123_EN = "Table 12.3 Typical CTI values for material families"
CAPTION123_VI = "Bảng 12.3 Giá trị CTI điển hình cho các họ vật liệu"

HEAD123_EN = [
    "Family of material",
    "Approximate<br>CTI limits",
]
HEAD123_VI = [
    "Họ vật liệu",
    "Giới hạn CTI<br>xấp xỉ",
]

# 2 cells per row: material family with its example + CTI limits.
ROWS123 = [
    ["Polycarbonate (e.g., makrolon)", "80–100"],
    ["Phenolic laminates (e.g., tufnol)", "80–150"],
    ["Resin bonded materials (e.g., fibreglass)", "100–140"],
    ["Epoxides (e.g., PCB material)", "150–300"],
    ["Nylon (e.g., maranyl)", "200–600"],
    ["Polyvinyl Chloride (PVC)", "300"],
    ["Polystyrene", "250–300"],
    ["Polyesters (e.g., permaglass)", "200–700+"],
    ["Polyethylene", "700+"],
]
ROWS123_EN = ROWS123
ROWS123_VI = [
    ["Policarbonat (ví dụ: makrolon)", "80–100"],
    ["Vật liệu dán ép phenolic (ví dụ: tufnol)", "80–150"],
    ["Vật liệu kết dính bằng nhựa (ví dụ: sợi thủy tinh)", "100–140"],
    ["Epoxy (ví dụ: vật liệu PCB)", "150–300"],
    ["Nylon (ví dụ: maranyl)", "200–600"],
    ["Polyvinyl clorua (PVC)", "300"],
    ["Polystyren", "250–300"],
    ["Polyester (ví dụ: permaglass)", "200–700+"],
    ["Polyethylen", "700+"],
]

NOTE123_EN = (
    "<p>Translator note: every parenthesised example prints 'e.g.,' with a "
    "comma; the brand names makrolon, tufnol, maranyl and permaglass are "
    "lowercase in print, while 'Polyvinyl Chloride' has a capital C. The "
    "ranges use an en-dash-like dash and the last two carry a plus suffix "
    "('200–700+', '700+'). The OCR text layer garbled 'tufnol' as 'tuhol' and "
    "dropped the comma in 'e.g.,'; the render governs.</p>"
)

NOTE123_VI = (
    "<p>Ghi chú của người dịch: mọi ví dụ trong ngoặc đơn đều in 'e.g.,' có "
    "dấu phẩy; các tên thương hiệu makrolon, tufnol, maranyl và permaglass "
    "được in thường, còn 'Polyvinyl Chloride' có chữ C hoa. Các khoảng giá "
    "trị dùng dấu gạch ngang kiểu en-dash và hai khoảng cuối có dấu cộng "
    "('200–700+', '700+'). Lớp văn bản OCR đọc sai 'tufnol' thành 'tuhol' và "
    "bỏ dấu phẩy trong 'e.g.,'; ảnh trang in là nguồn quyết định.</p>"
)

# ---------------------------------------------------------------------------
# Table 12.4 — printed p.310 (PDF p.331)
# ---------------------------------------------------------------------------

CAPTION124_EN = (
    "Table 12.4 Limiting temperatures for windings"
    "<br>Maximum winding temperature (°C)"
    "<br>Thermal material insulation class (notes 1 and 2)"
)
CAPTION124_VI = (
    "Bảng 12.4 Nhiệt độ giới hạn cho cuộn dây"
    "<br>Nhiệt độ cuộn dây tối đa (°C)"
    "<br>Cấp cách điện vật liệu (ghi chú 1 và 2)"
)

HEAD124_EN = [
    "Criteria and winding<br>type measurement",
    "Method of<br>temperature<br>measurement<br>(note 3)",
    "A",
    "B",
    "E",
    "F",
    "H",
]
HEAD124_VI = [
    "Tiêu chí và loại cuộn dây<br>đo lường",
    "Phương pháp<br>đo nhiệt độ<br>(ghi chú 3)",
    "A",
    "B",
    "E",
    "F",
    "H",
]

# 7 cells per row: criteria, method, and five insulation-class temperatures.
ROWS124 = [
    ["Single layer windings. (maximum temp)",
     "R or T", "95", "110", "120", "130", "155"],
    ["Other windings (maximum temp)",
     "R", "90", "105", "110", "130", "155"],
    ["", "T", "80", "95", "100", "115", "135"],
    ["Rotating machines (temp at tₑ time)",
     "R", "160", "175", "185", "210", "235"],
    ["", "T", "N/P", "N/P", "N/P", "N/P", "N/P"],
]
ROWS124_EN = ROWS124
ROWS124_VI = [
    ["Cuộn dây một lớp. (nhiệt độ cực đại)",
     "R hoặc T", "95", "110", "120", "130", "155"],
    ["Các cuộn dây khác (nhiệt độ cực đại)",
     "R", "90", "105", "110", "130", "155"],
    ["", "T", "80", "95", "100", "115", "135"],
    ["Máy quay (nhiệt độ tại thời điểm tₑ)",
     "R", "160", "175", "185", "210", "235"],
    ["", "T", "N/P", "N/P", "N/P", "N/P", "N/P"],
]

NOTE124_EN = (
    "<p>Notes:</p>"
    "<p>1 Insulation classes in accordance with BS 2757.</p>"
    "<p>2 These figures are included on a temporary basis pending the "
    "inclusion of figures in BS 2757.</p>"
    "<p>3 R indicates measurement by the resistance thermometer method and T "
    "by the thermometer method. The thermometer method is not acceptable "
    "where the resistance thermometer method is usable and never for "
    "rotating machines</p>"
    "<p>Translator note: Note 3 ends without a full stop in print and the "
    "'Notes:' heading is italicised. The machine row prints a subscript e in "
    "'tₑ', whose meaning is not defined in the chapter, and 'temp' is "
    "lowercase in all printed row labels. The OCR text layer read 'tₑ' as "
    "'te'; the render governs.</p>"
    "<p>Translator note: the two spanning header lines 'Maximum winding "
    "temperature (°C)' and 'Thermal material insulation class (notes 1 and "
    "2)' cover the five class columns and are carried in the caption; "
    "'(note 3)' prints under the Method column and is folded into that HEAD "
    "cell, leaving the flat HEAD/ROWS shape intact. 'N/P' is retained as "
    "printed, and Note 2's 1980s 'temporary basis' wording is translated "
    "literally.</p>"
)

NOTE124_VI = (
    "<p>Ghi chú:</p>"
    "<p>1 Cấp cách điện theo BS 2757.</p>"
    "<p>2 Các số liệu này được đưa vào trên cơ sở tạm thời cho đến khi đưa "
    "số liệu vào BS 2757.</p>"
    "<p>3 R chỉ phép đo bằng phương pháp nhiệt kế điện trở và T bằng phương "
    "pháp nhiệt kế. Không được dùng phương pháp nhiệt kế khi có thể dùng "
    "phương pháp nhiệt kế điện trở và không bao giờ dùng cho máy quay</p>"
    "<p>Ghi chú của người dịch: Ghi chú 3 kết thúc không có dấu chấm trong "
    "bản in và nhan đề 'Ghi chú:' được in nghiêng. Dòng máy quay in chỉ số "
    "dưới e trong 'tₑ', nghĩa của nó không được định nghĩa trong chương, và "
    "'nhiệt độ' được viết thường trong tất cả nhãn hàng in. Lớp văn bản OCR "
    "đọc 'tₑ' là 'te'; ảnh trang in là nguồn quyết định.</p>"
    "<p>Ghi chú của người dịch: hai dòng tiêu đề trải rộng 'Maximum winding "
    "temperature (°C)' và 'Thermal material insulation class (notes 1 and "
    "2)' phủ năm cột cấp và được đưa vào nhan đề; '(note 3)' in dưới cột "
    "Phương pháp được gộp vào ô HEAD đó, giữ cấu trúc HEAD/ROWS dạng phẳng. "
    "'N/P' được giữ nguyên theo bản in và cách diễn đạt 'tạm thời' của Ghi "
    "chú 2 được dịch sát nghĩa.</p>"
)
