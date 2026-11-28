# -*- coding: utf-8 -*-
"""Tables 13.9, 13.10, 13.11 and 13.12 of McMillan Chapter 13, bilingual EN/VI.

Transcribed from the authoritative page renders (the OCR text layer is
garbled for all four tables):
  - PDF p.402 / printed p.381 -> Tables 13.9 and 13.10 + legend/note
  - PDF p.408 / printed p.387 -> Table 13.11 + attribution + Note 1
  - PDF p.413 / printed p.392 -> Table 13.12 + Note

Cross-checked against work/ch13_survey_d.md sections 4.2, 5 and 6.
Structure follows mcmillan_tbl12_5_7.py: HEAD is one cell per column,
ROWS is a list of equal-length cell lists, CAPTION and NOTE are localized.
A plain string in ROWS is a full-width group-header row (bolton_common.table
renders it with colspan), used here for the stacked 'Ref:' block labels of
Tables 13.9 and 13.10. Grouped column titles are carried in the caption so
the flat HEAD/ROWS shape stays intact.

Rows whose cells contain connector words have distinct VI and EN variants.
Table 13.11 is purely numeric/symbolic, so its VI rows share the English list.

Printed quirks retained deliberately (with bilingual translator notes):

  * 13.9 header uses the unit word 'Volts'; 13.10 uses '(V)';
  * 13.9 note prints '1575V' (no space) but '15.6 KV' (space, capital K);
  * 13.9 / 13.10 have three / two stacked 'Ref:' reference blocks;
  * 13.11 caption spans two lines; headers are three tiers deep;
  * 13.11 attribution reads '(from BSEN 50020)' with no slash;
  * 13.11 Note 1 is redundant ('tolerance of up to 10% manufacturing
    tolerance');
  * 13.12 caption hyphenates 'trans-' / 'formers' across two lines;
  * 13.12 capitalises 'Intrinsically Safe' in the third row only;
  * 13.12 rows 2 and 3 end with a full stop; U symbol is subscripted.
"""

# ---------------------------------------------------------------------------
# Table 13.9 — printed p.381 (PDF p.402)
# ---------------------------------------------------------------------------

CAPTION139_EN = (
    "Table 13.9 Multiples used in calculation of composite spacings"
    "<br>Peak voltage (Volts)"
)
CAPTION139_VI = (
    "Bảng 13.9 Các hệ số nhân dùng trong tính toán khoảng cách tổ hợp"
    "<br>Điện áp đỉnh (Volt)"
)

HEAD139_EN = [
    "Type of spacing",
    "0< U ≤10",
    "10< U ≤30",
    "30< U ≤1575",
]
HEAD139_VI = [
    "Loại khoảng cách",
    "0< U ≤10",
    "10< U ≤30",
    "30< U ≤1575",
]

# 4 cells per row; plain strings are full-width 'Ref:' block labels.
ROWS139 = [
    "Ref: Clearance",
    ["Clearance", "1.0", "1.0", "1.0"],
    ["Separation through CC", "3.0", "3.0", "3.0"],
    ["Separation through SI", "3.0", "4.0", "6.0"],
    "Ref: Separation Through CC",
    ["Clearance", "0.33", "0.33", "0.33"],
    ["Separation through CC", "1.0", "1.0", "1.0"],
    ["Separation through SI", "1.0", "1.33", "2.0"],
    "Ref: Separation Through SI",
    ["Clearance", "0.33", "0.33", "0.33"],
    ["Separation through CC", "1.0", "0.75", "0.55"],
    ["Separation through SI", "1.0", "1.0", "1.0"],
]
ROWS139_EN = ROWS139
ROWS139_VI = [
    "Tham chiếu: Khe hở",
    ["Khe hở", "1.0", "1.0", "1.0"],
    ["Ngăn cách qua CC", "3.0", "3.0", "3.0"],
    ["Ngăn cách qua SI", "3.0", "4.0", "6.0"],
    "Tham chiếu: Ngăn cách qua CC",
    ["Khe hở", "0.33", "0.33", "0.33"],
    ["Ngăn cách qua CC", "1.0", "1.0", "1.0"],
    ["Ngăn cách qua SI", "1.0", "1.33", "2.0"],
    "Tham chiếu: Ngăn cách qua SI",
    ["Khe hở", "0.33", "0.33", "0.33"],
    ["Ngăn cách qua CC", "1.0", "0.75", "0.55"],
    ["Ngăn cách qua SI", "1.0", "1.0", "1.0"],
]

NOTE139_EN = (
    "<p>CC = Casting compound</p>"
    "<p>SI = Solid insulation</p>"
    "<p>Note: Clearance alone is not considered as sufficient above 1575V "
    "and thus composite clearances and separations are not possible. "
    "Composite separations through casting compound and solid insulation "
    "are, and the relationships between those two are still valid up to "
    "15.6 KV.</p>"
    "<p>Translator note: the printed header 'Peak voltage (Volts)' spans the "
    "three right-hand columns; it is carried in the caption so the flat "
    "HEAD/ROWS shape stays intact.</p>"
    "<p>Translator note: the three 'Ref: ...' lines are full-width centred "
    "labels separating the stacked reference blocks; they are carried as "
    "group-header rows. The word 'Through' is capitalised in the second "
    "and third block labels but lower case in the row labels; preserved.</p>"
    "<p>Translator note: the unit word 'Volts' is as printed in Table 13.9; "
    "Table 13.10 uses '(V)'. The note prints '1575V' without a space but "
    "'15.6 KV' with a space and capital K; all preserved.</p>"
    "<p>Translator note: the OCR text layer misread the inequality signs as "
    "'o< u 510', '10< U 130' and '30~ U 51575' and dropped the colon in two "
    "'Ref:' labels; the rendered forms govern.</p>"
)

NOTE139_VI = (
    "<p>CC = Hợp chất đúc</p>"
    "<p>SI = Vật liệu cách điện rắn</p>"
    "<p>Ghi chú: Riêng khe hở không được coi là đủ khi điện áp vượt quá "
    "1575V, do đó không thể có khe hở và khoảng cách tổ hợp. Các khoảng cách "
    "tổ hợp qua hợp chất đúc và vật liệu cách điện rắn thì có, và mối quan "
    "hệ giữa hai loại này vẫn còn giá trị đến 15.6 KV.</p>"
    "<p>Ghi chú của người dịch: tiêu đề in 'Peak voltage (Volts)' trải qua "
    "ba cột bên phải; được đưa vào phần tiêu đề phụ của bảng để giữ cấu "
    "trúc HEAD/ROWS dạng phẳng.</p>"
    "<p>Ghi chú của người dịch: ba dòng 'Ref: ...' là các nhãn căn giữa "
    "trải rộng toàn bảng, ngăn cách các khối tham chiếu xếp chồng; được "
    "thể hiện là các hàng tiêu đề nhóm. Chữ 'Through' viết hoa trong nhãn "
    "khối thứ hai và thứ ba nhưng viết thường trong nhãn hàng; giữ nguyên.</p>"
    "<p>Ghi chú của người dịch: bảng 13.9 dùng từ 'Volts' theo bản in; bảng "
    "13.10 dùng '(V)'. Ghi chú in '1575V' không có dấu cách nhưng '15.6 KV' "
    "có dấu cách và chữ K viết hoa; giữ tất cả.</p>"
    "<p>Ghi chú của người dịch: lớp văn bản OCR đọc sai các dấu bất đẳng "
    "thức thành 'o< u 510', '10< U 130' và '30~ U 51575' và bỏ dấu hai "
    "chấm ở hai nhãn 'Ref:'; các dạng trên bản in được giữ.</p>"
)

# ---------------------------------------------------------------------------
# Table 13.10 — printed p.381 (PDF p.402)
# ---------------------------------------------------------------------------

CAPTION1310_EN = (
    "Table 13.10 Multiples used in calculation of composite creepages"
    "<br>Peak voltage (V)"
)
CAPTION1310_VI = (
    "Bảng 13.10 Các hệ số nhân dùng trong tính toán đường rò tổ hợp"
    "<br>Điện áp đỉnh (V)"
)

HEAD1310_EN = [
    "Type of spacing",
    "0< U ≤1575",
]
HEAD1310_VI = [
    "Loại khoảng cách",
    "0< U ≤1575",
]

# 2 cells per row; plain strings are full-width 'Ref:' block labels.
ROWS1310 = [
    "Ref: Creepage Distance in Air",
    ["Creepage in air", "1.0"],
    ["Creepage under conformal coating", "3.0"],
    "Ref: Creepage Under Conformal Coating",
    ["Creepage in air", "0.33"],
    ["Creepage under conformal coating", "1.0"],
]
ROWS1310_EN = ROWS1310
ROWS1310_VI = [
    "Tham chiếu: Chiều dài đường rò trong không khí",
    ["Đường rò trong không khí", "1.0"],
    ["Đường rò dưới lớp phủ bảo vệ", "3.0"],
    "Tham chiếu: Đường rò dưới lớp phủ bảo vệ",
    ["Đường rò trong không khí", "0.33"],
    ["Đường rò dưới lớp phủ bảo vệ", "1.0"],
]

NOTE1310_EN = (
    "<p>Translator note: the printed header 'Peak voltage (V)' spans the "
    "single right-hand column and is carried in the caption so the flat "
    "HEAD/ROWS shape stays intact.</p>"
    "<p>Translator note: the two 'Ref: ...' lines are full-width centred "
    "labels separating the stacked reference blocks; they are carried as "
    "group-header rows.</p>"
    "<p>Translator note: this table prints '(V)' in its header while Table "
    "13.9 uses the unit word 'Volts'; preserved per table.</p>"
    "<p>Translator note: the printed block labels read 'Ref: Creepage "
    "Distance in Air' and 'Ref: Creepage Under Conformal Coating', while "
    "the row labels read 'Creepage in air' and 'Creepage under conformal "
    "coating'; the differing wording is as printed.</p>"
    "<p>Translator note: the OCR text layer misread '0< U ≤1575' as "
    "'O< U 51575'; the rendered inequality governs.</p>"
)

NOTE1310_VI = (
    "<p>Ghi chú của người dịch: tiêu đề in 'Peak voltage (V)' chỉ trải qua "
    "một cột bên phải; được đưa vào phần tiêu đề phụ của bảng để giữ cấu "
    "trúc HEAD/ROWS dạng phẳng.</p>"
    "<p>Ghi chú của người dịch: hai dòng 'Ref: ...' là các nhãn căn giữa "
    "trải rộng toàn bảng, ngăn cách các khối tham chiếu xếp chồng; được "
    "thể hiện là các hàng tiêu đề nhóm.</p>"
    "<p>Ghi chú của người dịch: bảng này in '(V)' ở tiêu đề, trong khi bảng "
    "13.9 dùng từ 'Volts'; giữ nguyên theo từng bảng.</p>"
    "<p>Ghi chú của người dịch: nhãn khối in là 'Ref: Creepage Distance in "
    "Air' và 'Ref: Creepage Under Conformal Coating', còn nhãn hàng là "
    "'Creepage in air' và 'Creepage under conformal coating'; cách dùng từ "
    "khác nhau này là theo bản in.</p>"
    "<p>Ghi chú của người dịch: lớp văn bản OCR đọc sai '0< U ≤1575' thành "
    "'O< U 51575'; dấu bất đẳng thức trên bản in được giữ.</p>"
)

# ---------------------------------------------------------------------------
# Table 13.11 — printed p.387 (PDF p.408)
# ---------------------------------------------------------------------------

CAPTION1311_EN = (
    "Table 13.11 Minimum dimensions for wire or foil used"
    "<br>for transformer screens"
)
CAPTION1311_VI = (
    "Bảng 13.11 Kích thước tối thiểu của dây hoặc lá được dùng"
    "<br>cho màn chắn máy biến áp"
)

HEAD1311_EN = [
    "Rating of protective fuse or circuit breaker<br>Amps",
    "Thickness of foil forming screen<br>(Note 1)<br>mm",
    "Diameter of wire forming layers of screen<br>(Note 1)<br>mm",
]
HEAD1311_VI = [
    "Định mức của cầu chì hoặc cầu dao bảo vệ<br>Amp",
    "Chiều dày của lá tạo màn chắn<br>(Ghi chú 1)<br>mm",
    "Đường kính của dây tạo các lớp màn chắn<br>(Ghi chú 1)<br>mm",
]

# 3 cells per row: fuse rating + foil thickness + wire diameter,
# all purely numeric/symbolic, so the VI rows share the English list.
ROWS1311 = [
    ["0.1", "0.05", "0.2"],
    ["0.5", "0.05", "0.45"],
    ["1.0", "0.075", "0.63"],
    ["2.0", "0.15", "0.9"],
    ["3.0", "0.25", "1.12"],
    ["5.0", "0.3", "1.4"],
]
ROWS1311_EN = ROWS1311
ROWS1311_VI = ROWS1311

NOTE1311_EN = (
    "<p>(from BSEN 50020)</p>"
    "<p>Note: 1 The above figures for wire and foil dimensions are nominal "
    "figures and a tolerance of up to 10% manufacturing tolerance is "
    "permitted provided that in all cases the variation in dimension may "
    "not exceed 0.1 mm.</p>"
    "<p>Translator note: the caption is set on two lines in print; the line "
    "break is reproduced in the English caption.</p>"
    "<p>Translator note: each column header is stacked three tiers deep in "
    "print; the tiers are joined with line breaks inside the header cells.</p>"
    "<p>Translator note: the attribution prints 'BSEN 50020' with no slash, "
    "unlike the 'BS/EN 50020' used in the prose. Preserved as printed.</p>"
    "<p>Translator note: Note 1 is redundant in the original — 'a tolerance "
    "of up to 10% manufacturing tolerance' — and its wording is preserved "
    "verbatim, including the final full stop.</p>"
)

NOTE1311_VI = (
    "<p>(theo BSEN 50020)</p>"
    "<p>Ghi chú: 1 Các số liệu trên về kích thước dây và lá là các số liệu "
    "danh định và cho phép sai số dung sai chế tạo lên tới 10%, với điều "
    "kiện trong mọi trường hợp sự thay đổi kích thước không vượt quá "
    "0.1 mm.</p>"
    "<p>Ghi chú của người dịch: tiêu đề được in trên hai dòng; ngắt dòng "
    "được tái tạo trong tiêu đề tiếng Việt.</p>"
    "<p>Ghi chú của người dịch: mỗi tiêu đề cột được xếp ba tầng trên bản "
    "in; các tầng được nối bằng ngắt dòng bên trong ô tiêu đề.</p>"
    "<p>Ghi chú của người dịch: dòng nguồn in 'BSEN 50020' không có dấu "
    "gạch chéo, khác với 'BS/EN 50020' trong phần văn bản. Giữ nguyên theo "
    "bản in.</p>"
    "<p>Ghi chú của người dịch: Ghi chú 1 bị lặp từ trong nguyên bản — "
    "'sai số dung sai chế tạo lên tới 10%' — và được giữ nguyên từ ngữ, kể "
    "cả dấu chấm cuối.</p>"
)

# ---------------------------------------------------------------------------
# Table 13.12 — printed p.392 (PDF p.413)
# ---------------------------------------------------------------------------

CAPTION1312_EN = (
    "Table 13.12 Routine test voltages for mains trans-"
    "<br>formers"
)
CAPTION1312_VI = (
    "Bảng 13.12 Điện áp thử nghiệm thông thường cho máy biến áp nguồn"
)

HEAD1312_EN = [
    "Application points",
    "rms applied voltages",
]
HEAD1312_VI = [
    "Điểm áp dụng",
    "Điện áp áp dụng rms",
]

# 2 cells per row: application point + rms applied voltage.
ROWS1312 = [
    ["Between the mains input winding and all secondary windings",
     "4 Uₙ or 2000 V rms"],
    ["Between all the windings (both input and secondary) and the transformer core.",
     "2 Uₙ or 1000 V rms"],
    ["Between the Intrinsically Safe circuit winding(s) associated with a "
     "particular intrinsically safe circuit and all other secondary windings.",
     "2 Uₙ + 1000 V rms with a minimum of 1500 V rms"],
]
ROWS1312_EN = ROWS1312
ROWS1312_VI = [
    ["Giữa cuộn dây đầu vào nguồn và tất cả các cuộn dây thứ cấp",
     "4 Uₙ hoặc 2000 V rms"],
    ["Giữa tất cả các cuộn dây (cả đầu vào và thứ cấp) và lõi máy biến áp.",
     "2 Uₙ hoặc 1000 V rms"],
    ["Giữa cuộn dây (các cuộn dây) của mạch An toàn nội tại liên quan đến "
     "một mạch an toàn nội tại cụ thể và tất cả các cuộn dây thứ cấp khác.",
     "2 Uₙ + 1000 V rms với giá trị tối thiểu là 1500 V rms"],
]

NOTE1312_EN = (
    "<p>Note: The criteria for the test is a current of less than 5mA which "
    "is steady or falling during the test which is applied for 60 seconds "
    "the voltage having been raised steadily to the test value in 10 "
    "seconds.</p>"
    "<p>Translator note: the caption is hyphenated across two printed lines "
    "as 'mains trans-' / 'formers'; the printed hyphenation is preserved in "
    "the English caption.</p>"
    "<p>Translator note: 'Intrinsically Safe' is capitalised in the third "
    "application-point cell but lowercase in the surrounding prose; "
    "preserved as printed.</p>"
    "<p>Translator note: the second and third application-point cells end "
    "with a full stop in print; retained.</p>"
    "<p>Translator note: the U symbol is subscripted in print, and the "
    "current '5mA' is printed without a space before the unit; both "
    "preserved.</p>"
)

NOTE1312_VI = (
    "<p>Ghi chú: Tiêu chuẩn của phép thử là dòng điện nhỏ hơn 5mA, ổn định "
    "hoặc giảm trong suốt phép thử được áp dụng trong 60 giây, điện áp được "
    "nâng dần tới giá trị thử trong 10 giây.</p>"
    "<p>Ghi chú của người dịch: tiêu đề bị gãy dòng do căn đều hai bên, "
    "'mains trans-' / 'formers'; dấu gạch nối theo bản in được giữ trong "
    "tiêu đề tiếng Anh.</p>"
    "<p>Ghi chú của người dịch: cụm 'Intrinsically Safe' được viết hoa ở ô "
    "áp dụng thứ ba nhưng viết thường trong văn bản xung quanh; giữ nguyên "
    "theo bản in.</p>"
    "<p>Ghi chú của người dịch: ô áp dụng thứ hai và thứ ba kết thúc bằng "
    "dấu chấm trên bản in; giữ nguyên.</p>"
    "<p>Ghi chú của người dịch: ký hiệu U được in dạng chỉ số dưới và dòng "
    "điện '5mA' được in không có dấu cách trước đơn vị; giữ cả hai.</p>"
)
