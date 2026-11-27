# -*- coding: utf-8 -*-
"""Tables 10.11–10.15 of McMillan Chapter 10, bilingual EN/VI.

Transcribed from the authoritative page renders:
  - printed p.252 / PDF p.273 -> Table 10.11
  - printed p.254 / PDF p.275 -> Table 10.12 (image-only in the raw text layer)
  - printed p.255 / PDF p.276 -> Table 10.13
  - printed p.258 / PDF p.279 -> Table 10.14
  - printed p.260 / PDF p.281 -> Table 10.15

Cross-checked against work/ch10_survey_c.md and work/ch10_survey_d.md; the
page images govern wherever the OCR layer or a survey line disagrees.

Structure follows the sibling supplier mcmillan_tbl10_6_10.py: HEAD is one
cell per column, ROWS is a list of equal-length cell lists shared by both
languages, and CAPTION / NOTE are localized.  Full-width centred or spanning
lines printed above the columns are carried as a second line of CAPTION,
after the printed caption text.  Where a group header spans three sub-columns
(10.11/10.12) the printed group label sits in the first sub-column header and
the other two carry only their sub-group code, as in Table 10.10 above.

Printed quirks retained deliberately, with bilingual translator notes:

  * 10.11 scope note says the table is not valid for shafts and rotating
    machines; Table 10.10's caption covers shafts with sleeve bearings;
  * 10.12 N/P definition has no final full stop and no 'this' before
    'sub-group' (10.11 prints 'this sub-group' with a full stop);
  * 10.13 definition lines print 'A=', 'B =', 'C=', 'D=' with asymmetric
    spacing and a capital 'P' in 'Pressure';
  * 10.14 caption breaks 'supported' as 'suppor-' / 'ted' across lines (the
    page image governs; survey D's 'support-' / 'ed' is a transcription slip);
  * 10.14 prints the voltage band '4200 < U ≤ 500' (not 5000), with the next
    band starting at 5500;
  * 10.15 has no numbered notes, only the source line; superscripts are
    literal Unicode.

Spacing of '≥' and '≤' against their numbers follows the page image (no
inserted space), as in the printed Table 10.11/10.12 cells and headers.
"""
# ---------------------------------------------------------------------------
# Table 10.11 — printed p.252 (PDF p.273)
# ---------------------------------------------------------------------------

CAPTION1011_EN = (
    "Table 10.11 Maximum permissible gaps for operating rods using rolling "
    "element bearings"
    "<br>Permissible maximum gaps for given enclosure volumes"
)
CAPTION1011_VI = (
    "Bảng 10.11 Khe hở tối đa cho phép đối với thanh truyền động dùng ổ bi lăn"
    "<br>Khe hở tối đa cho phép theo thể tích vỏ bọc đã cho"
)

HEAD1011_EN = [
    "Joint width<br>(L)<br>(mm)",
    "Volume ≤100 cm³<br>IIA", "IIB", "IIC",
    "Volume ≤500 cm³<br>IIA", "IIB", "IIC",
    "Volume ≤2000 cm³<br>IIA", "IIB", "IIC",
    "Volume >2000 cm³<br>IIA", "IIB", "IIC",
]
HEAD1011_VI = [
    "Chiều rộng mối nối<br>(L)<br>(mm)",
    "Thể tích ≤100 cm³<br>IIA", "IIB", "IIC",
    "Thể tích ≤500 cm³<br>IIA", "IIB", "IIC",
    "Thể tích ≤2000 cm³<br>IIA", "IIB", "IIC",
    "Thể tích >2000 cm³<br>IIA", "IIB", "IIC",
]

# 13 cells per row: joint width plus 4 volume groups x 3 sub-groups.
ROWS1011 = [
    ["≥6.0", "0.45", "0.30", "0.15", "N/P", "N/P", "N/P",
     "N/P", "N/P", "N/P", "N/P", "N/P", "N/P"],
    ["≥9.5", "0.45", "0.35", "0.15", "0.40", "0.25", "0.15",
     "N/P", "N/P", "N/P", "N/P", "N/P", "N/P"],
    ["≥12.5", "0.50", "0.40", "0.25", "0.45", "0.30", "0.25",
     "0.45", "0.30", "0.25", "0.30", "0.20", "N/P"],
    ["≥25.0", "0.60", "0.45", "0.25", "0.60", "0.40", "0.25",
     "0.60", "0.40", "0.25", "0.60", "0.30", "0.25"],
    ["≥40.0", "0.75", "0.60", "0.30", "0.75", "0.45", "0.30",
     "0.75", "0.45", "0.30", "0.75", "0.45", "0.30"],
]

NOTE1011_EN = (
    "<p>(from BS/EN 50018)</p>"
    "<p>N/P = Not permitted for joints of this width and/or this sub-group.</p>"
    "<p>Note: This table is not valid for shafts and rotating machines. For "
    "values of gaps for shafts and rotating machines see Table 10.12.</p>"
    "<p>Translator note: the printed scope restriction is retained here. "
    "Table 10.11 applies to operating rods only; shafts of rotating machines "
    "with sleeve bearings are covered by Table 10.10 and referred to Table "
    "10.12 for rolling element bearings.</p>"
)
NOTE1011_VI = (
    "<p>(theo BS/EN 50018)</p>"
    "<p>N/P = Không được phép đối với các mối nối có chiều rộng và/hoặc nhóm "
    "con này.</p>"
    "<p>Ghi chú: Bảng này không áp dụng cho trục và máy quay. Để biết giá trị "
    "khe hở cho trục và máy quay, xem Bảng 10.12.</p>"
    "<p>Ghi chú của người dịch: giữ nguyên phạm vi áp dụng như bản gốc. Bảng "
    "10.11 chỉ áp dụng cho thanh truyền động; trục của máy quay có ổ bi dạng "
    "bạc được qui định tại Bảng 10.10 và được chuyển sang Bảng 10.12 khi dùng "
    "ổ bi lăn.</p>"
)

# ---------------------------------------------------------------------------
# Table 10.12 — printed p.254 (PDF p.275); image-only in the OCR text layer
# ---------------------------------------------------------------------------

CAPTION1012_EN = (
    "Table 10.12 Maximum permissible gaps for shafts and rotating electrical "
    "machines using rolling element bearings"
    "<br>Permissible maximum gaps for given enclosure volumes"
)
CAPTION1012_VI = (
    "Bảng 10.12 Khe hở tối đa cho phép đối với trục và máy điện quay dùng ổ "
    "bi lăn"
    "<br>Khe hở tối đa cho phép theo thể tích vỏ bọc đã cho"
)

HEAD1012_EN = [
    "Joint width<br>(L)<br>(mm)",
    "Volume ≤100 cm³<br>IIA", "IIB", "IIC",
    "Volume ≤500 cm³<br>IIA", "IIB", "IIC",
    "Volume ≤2000 cm³<br>IIA", "IIB", "IIC",
    "Volume >2000 cm³<br>IIA", "IIB", "IIC",
]
HEAD1012_VI = [
    "Chiều rộng mối nối<br>(L)<br>(mm)",
    "Thể tích ≤100 cm³<br>IIA", "IIB", "IIC",
    "Thể tích ≤500 cm³<br>IIA", "IIB", "IIC",
    "Thể tích ≤2000 cm³<br>IIA", "IIB", "IIC",
    "Thể tích >2000 cm³<br>IIA", "IIB", "IIC",
]

# 13 cells per row; decimal places and N/P entries preserved cell by cell.
ROWS1012 = [
    ["≥6.0", "0.30", "0.20", "0.10", "N/P", "N/P", "N/P",
     "N/P", "N/P", "N/P", "N/P", "N/P", "N/P"],
    ["≥9.5", "0.30", "0.23", "0.10", "0.27", "0.17", "0.10",
     "N/P", "N/P", "N/P", "N/P", "N/P", "N/P"],
    ["≥12.5", "0.33", "0.27", "0.17", "0.30", "0.20", "0.17",
     "0.30", "0.20", "0.17", "0.20", "0.13", "N/P"],
    ["≥25.0", "0.40", "0.30", "0.17", "0.40", "0.27", "0.17",
     "0.40", "0.27", "0.17", "0.40", "0.20", "0.17"],
    ["≥40.0", "0.50", "0.40", "0.20", "0.50", "0.30", "0.20",
     "0.50", "0.30", "0.20", "0.50", "0.27", "0.20"],
]

NOTE1012_EN = (
    "<p>(from BS/EN 50018)</p>"
    "<p>N/P = Not permitted for joints of this width and/or sub-group</p>"
    "<p>Translator note: the N/P definition is printed without a final full "
    "stop and without 'this' before 'sub-group', unlike Table 10.11; retained "
    "as printed.</p>"
)
NOTE1012_VI = (
    "<p>(theo BS/EN 50018)</p>"
    "<p>N/P = Không được phép đối với các mối nối có chiều rộng và/hoặc nhóm "
    "con</p>"
    "<p>Ghi chú của người dịch: định nghĩa N/P được in không có dấu chấm cuối "
    "cũng như không có 'this' trước 'sub-group', khác với Bảng 10.11; giữ "
    "nguyên theo bản in.</p>"
)

# ---------------------------------------------------------------------------
# Table 10.13 — printed p.255 (PDF p.276)
# ---------------------------------------------------------------------------

CAPTION1013_EN = (
    "Table 10.13 Reduction in thread length for testing"
    "<br>Reduction in engaged thread length by"
)
CAPTION1013_VI = (
    "Bảng 10.13 Giảm chiều dài ren để thử nghiệm"
    "<br>Mức giảm chiều dài ren ăn khớp"
)

HEAD1013_EN = [
    "Type of threaded joint<br>Test detail",
    "Sub-group IIA and IIB<br>A",
    "Sub-group IIA and IIB<br>B",
    "Sub-group IIC<br>C",
    "Sub-group IIC<br>D",
]
HEAD1013_VI = [
    "Loại mối nối ren<br>Chi tiết thử nghiệm",
    "Nhóm con IIA và IIB<br>A",
    "Nhóm con IIA và IIB<br>B",
    "Nhóm con IIC<br>C",
    "Nhóm con IIC<br>D",
]

ROWS1013 = [
    ["Parallel thread to ISO 965 medium or better fit", "None", "1/3", "1/3", "None"],
    ["Other parallel", "1/3", "1/2", "1/2", "1/3"],
    ["Taper", "None", "1/3", "1/3", "None"],
]

NOTE1013_EN = (
    "<p>(from BS/EN 50018)</p>"
    "<p>A= Tests with enhanced mixtures</p>"
    "<p>B = Tests with enhanced gaps</p>"
    "<p>C= Tests with enhanced gaps</p>"
    "<p>D= Tests at high Pressure</p>"
    "<p>Note: Taper threaded joints are tested with minimum hand tightening "
    "using threads at extremes of tolerance. Length of engaged thread is "
    "achieved by machining off 1/3 engaged threads.</p>"
    "<p>Translator note: the four definition lines print 'A=', 'B =', 'C=' "
    "and 'D=' with inconsistent spacing around the equals sign, and 'D= "
    "Tests at high Pressure' has a capital 'P'; all retained as printed.</p>"
)
NOTE1013_VI = (
    "<p>(theo BS/EN 50018)</p>"
    "<p>A = Thử nghiệm với hỗn hợp tăng cường</p>"
    "<p>B = Thử nghiệm với khe hở tăng cường</p>"
    "<p>C = Thử nghiệm với khe hở tăng cường</p>"
    "<p>D = Thử nghiệm ở áp suất cao</p>"
    "<p>Ghi chú: Mối nối ren côn được thử nghiệm với lực siết tay tối thiểu, "
    "dùng ren ở giới hạn dung sai cực đoan. Chiều dài ren ăn khớp đạt được "
    "bằng cách gia công bỏ 1/3 số ren ăn khớp.</p>"
    "<p>Ghi chú của người dịch: bốn dòng định nghĩa in 'A=', 'B =', 'C=' và "
    "'D=' với khoảng cách không thống nhất quanh dấu bằng, và 'D= Tests at "
    "high Pressure' viết hoa chữ 'P'; giữ nguyên theo bản in.</p>"
)

# ---------------------------------------------------------------------------
# Table 10.14 — printed p.258 (PDF p.279)
# ---------------------------------------------------------------------------

CAPTION1014_EN = (
    "Table 10.14 Creepage distance between bare live parts of flameproof "
    "apparatus suppor-<br>ted by non-metallic enclosure"
    "<br>Minimum creepage distance (mm)"
)
CAPTION1014_VI = (
    "Bảng 10.14 Chiều dài đường rò giữa các bộ phận mang điện trần của thiết "
    "bị chống cháy được nâng đỡ bằng vỏ bọc phi kim loại"
    "<br>Chiều dài đường rò tối thiểu (mm)"
)

HEAD1014_EN = [
    "Maximum rms working voltage<br>(U in volts)",
    "Material Group I",
    "Material Group II",
    "Material Group IIIa",
]
HEAD1014_VI = [
    "Điện áp làm việc RMS tối đa<br>(U tính bằng vôn)",
    "Nhóm vật liệu I",
    "Nhóm vật liệu II",
    "Nhóm vật liệu IIIa",
]

# 17 rows; the '4200 < U ≤ 500' band is printed that way in the original.
ROWS1014 = [
    ["0 < U ≤ 15", "1.6", "1.6", "1.6"],
    ["15 < U ≤ 30", "1.8", "1.8", "1.8"],
    ["30 < U ≤ 60", "2.1", "2.6", "3.4"],
    ["60 < U ≤ 110", "2.5", "3.2", "4.0"],
    ["110 < U ≤ 175", "3.2", "4.0", "5.0"],
    ["175 < U ≤ 275", "5.0", "6.3", "8.0"],
    ["275 < U ≤ 420", "8.0", "10.0", "12.5"],
    ["420 < U ≤ 550", "10.0", "12.5", "16.0"],
    ["550 < U ≤ 750", "12.0", "16.0", "20.0"],
    ["750 < U ≤ 1100", "20.0", "25.0", "32.0"],
    ["1100 < U ≤ 2200", "32.0", "36.0", "40.0"],
    ["2200 < U ≤ 3300", "40.0", "45.0", "50.0"],
    ["3300 < U ≤ 4200", "50.0", "56.0", "63.0"],
    ["4200 < U ≤ 500", "63.0", "71.0", "80.0"],
    ["5500 < U ≤ 6600", "80.0", "90.0", "100.0"],
    ["6600 < U ≤ 8300", "100.0", "110.0", "125.0"],
    ["8300 < U ≤ 11000", "125.0", "140.0", "160.0"],
]

NOTE1014_EN = (
    "<p>(from BS/EN 50019)</p>"
    "<p>Material Group I = Comparative tracking index (CTI) over 600</p>"
    "<p>Material Group II = Comparative tracking index at least 400 but less "
    "than 600</p>"
    "<p>Material Group IIIa = Comparative tracking index at least 175 but "
    "below 400</p>"
    "<p>Note: Comparative tracking index in accordance with BS 5901 (1980).</p>"
    "<p>Translator note: the caption breaks 'supported' as 'suppor-' and "
    "'ted' across two printed lines; retained. The voltage band '4200 < U "
    "≤ 500' is also printed that way (apparently a misprint for 5000) and "
    "the next band starts at 5500; retained verbatim.</p>"
)
NOTE1014_VI = (
    "<p>(theo BS/EN 50019)</p>"
    "<p>Nhóm vật liệu I = Chỉ số theo dõi so sánh (CTI) trên 600</p>"
    "<p>Nhóm vật liệu II = Chỉ số theo dõi so sánh ít nhất 400 nhưng dưới 600</p>"
    "<p>Nhóm vật liệu IIIa = Chỉ số theo dõi so sánh ít nhất 175 nhưng dưới "
    "400</p>"
    "<p>Ghi chú: Chỉ số theo dõi so sánh theo BS 5901 (1980).</p>"
    "<p>Ghi chú của người dịch: tiêu đề in ngắt 'supported' thành 'suppor-' "
    "và 'ted' trên hai dòng; giữ nguyên. Dải điện áp '4200 < U ≤ 500' cũng "
    "được in như vậy (có thể là lỗi in của 5000) và dải tiếp theo bắt đầu từ "
    "5500; giữ nguyên theo bản in.</p>"
)

# ---------------------------------------------------------------------------
# Table 10.15 — printed p.260 (PDF p.281)
# ---------------------------------------------------------------------------

CAPTION1015_EN = (
    "Table 10.15 Test pressure for small enclosures where reference pressure "
    "cannot be measured"
)
CAPTION1015_VI = (
    "Bảng 10.15 Áp suất thử đối với vỏ bọc nhỏ trong đó không thể đo áp suất "
    "tham chiếu"
)

HEAD1015_EN = [
    "Enclosure<br>volume<br>(cm³)",
    "Test pressure<br>(N/m²)<br>Sub-group IIA",
    "Sub-group IIB",
    "Sub-group IIC",
]
HEAD1015_VI = [
    "Thể tích<br>vỏ bọc<br>(cm³)",
    "Áp suất thử<br>(N/m²)<br>Nhóm con IIA",
    "Nhóm con IIB",
    "Nhóm con IIC",
]

ROWS1015 = [
    ["≤10", "1 × 10⁶", "1 × 10⁶", "1 × 10⁶"],
    [">10", "1.5 × 10⁶", "1.5 × 10⁶", "2 × 10⁶"],
]

NOTE1015_EN = "<p>(from BS/EN 50018)</p>"
NOTE1015_VI = "<p>(theo BS/EN 50018)</p>"
