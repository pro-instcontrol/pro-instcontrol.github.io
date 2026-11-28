# -*- coding: utf-8 -*-
"""Tables 15.1 and 15.2 of McMillan Chapter 15, bilingual EN/VI.

Transcribed from the authoritative page renders:
  - PDF p.481 / printed p.460 -> Table 15.1 and its ¹ predominance note
  - PDF p.488 / printed p.467 -> Table 15.2 (no printed footnote)

Cross-checked against work/mcmillan_ch15_survey_a.md §5 and
work/mcmillan_ch15_survey_b.md §4. The OCR text layer is garbled in places;
the page images govern throughout.

Structure follows mcmillan_tbl14_1_3.py: HEAD is one cell per column, ROWS is
a list of equal-length cell lists, CAPTION and NOTE are localized. The four
stacked header rows of 15.1 are carried into the CAPTION lines (over-headers
'Minimum acceptable dust ignition temperature', 'Protection concepts' /
'Type of protection', and their 'd/e/i/m/o/p/q' and 'N(n)' subheaders), so
the flat HEAD keeps only the five final columns.

Table 15.1 prints pure values plus superscripts, so its rows are shared.
Table 15.2 prints connector words in its second column, so it exports
genuine language-specific ROWS152_VI / ROWS152_EN (with ROWS152 as the
English canonical rows).

Printed quirks retained deliberately:
  * 15.1 non-numeric row order T1, T4, T2, T3, T5, T6;
  * the doubled parentheses in 'N(’n’)';
  * superscript ¹ on the individual predominating values and in the note;
  * inconsistent spacing around °C in the printed values;
  * the operator spacing in '≤16', '>16 but ≤35', '>35'.
"""

# ---------------------------------------------------------------------------
# Table 15.1 — printed p.460 (PDF p.481)
# ---------------------------------------------------------------------------

CAPTION151_EN = (
    "Table 15.1 Equivalent minimum dust ignition temperature for gas/vapour temperature classifications"
    "<br>Minimum acceptable dust ignition temperature"
    "<br>Protection concepts / Type of protection"
    "<br>‘d’ ‘e’ ‘i’ ‘m’ ‘o’ ‘p’ and ‘q’ / ‘N(’n’)’ — Cloud / Layer / Cloud / Layer"
)
CAPTION151_VI = (
    "Bảng 15.1 Nhiệt độ đánh lửa bụi tối thiểu tương đương cho các cấp nhiệt độ của khí/hơi"
    "<br>Nhiệt độ đánh lửa bụi tối thiểu chấp nhận được"
    "<br>Khái niệm bảo vệ / Loại hình bảo vệ"
    "<br>‘d’ ‘e’ ‘i’ ‘m’ ‘o’ ‘p’ và ‘q’ / ‘N(’n’)’ — Đám mây / Lớp bụi / Đám mây / Lớp bụi"
)

HEAD151_EN = [
    "Temperature classification",
    "Protection concepts — Cloud",
    "Protection concepts — Layer",
    "Type of protection ‘N(’n’)’ — Cloud",
    "Type of protection ‘N(’n’)’ — Layer",
]
HEAD151_VI = [
    "Phân loại nhiệt độ",
    "Khái niệm bảo vệ — Đám mây",
    "Khái niệm bảo vệ — Lớp bụi",
    "Loại hình bảo vệ ‘N(’n’)’ — Đám mây",
    "Loại hình bảo vệ ‘N(’n’)’ — Lớp bụi",
]

# 5 cells per row: classification plus four dust ignition temperatures.
# Every cell is a printed value or a superscript mark, so rows are shared.
ROWS151 = [
    ["T1 (450°C)", "675 °C¹", "525 °C", "685°C¹", "535 °C"],
    ["T4 (125°C)", "195 °C", "205 °C¹", "203 °C", "210°C¹"],
    ["T2 (300°C)", "450 °C¹", "375 °C", "465 °C¹", "385 °C"],
    ["T3 (200°C)", "308 °C¹", "280 °C", "315 °C¹", "285 °C"],
    ["T5 (100°C)", "158°C", "180 °C¹", "165 °C", "185 °C¹"],
    ["T6 (85°C)", "135°C", "165°C¹", "143°C", "170 °C¹"],
]
ROWS151_EN = ROWS151
ROWS151_VI = ROWS151

NOTE151_EN = (
    "<p>Notes: ¹As a dust cloud cannot practically exist without dust layers "
    "forming, and dust layers are a result of dust clouds, this figure is "
    "predominant in the apparatus selection procedure and should always be used.</p>"
    "<p>Translator note: the printed non-numeric row order T1, T4, T2, T3, "
    "T5, T6 is preserved, as is the superscript ¹ on each predominating "
    "value (the cloud value for T1/T2/T3 and the layer value for T4/T5/T6). "
    "The four stacked header rows are carried into the caption lines; the "
    "flat header keeps the five final columns. The doubled parentheses in "
    "'N(’n’)’' and the inconsistent spacing around °C in the printed "
    "'675 °C¹' versus '685°C¹', '158°C' versus '180 °C¹' are retained.</p>"
)

NOTE151_VI = (
    "<p>Ghi chú: ¹Vì đám mây bụi trên thực tế không thể tồn tại mà không có "
    "lớp bụi hình thành, và lớp bụi lại là kết quả của đám mây bụi, giá trị "
    "này là giá trị chủ đạo trong quy trình lựa chọn thiết bị và phải luôn "
    "được sử dụng.</p>"
    "<p>Ghi chú của người dịch: thứ tự hàng không theo số của bản in "
    "T1, T4, T2, T3, T5, T6 được giữ nguyên, cũng như chỉ số trên ¹ trên "
    "từng giá trị chủ đạo (giá trị đám mây đối với T1/T2/T3 và giá trị lớp "
    "bụi đối với T4/T5/T6). Bốn hàng tiêu đề xếp chồng được đưa vào các "
    "dòng nhan đề; tiêu đề phẳng chỉ giữ năm cột cuối. Dấu ngoặc đơn đôi "
    "trong 'N(’n’)’' và cách viết khoảng cách không nhất quán quanh °C "
    "trong '675 °C¹' so với '685°C¹', '158°C' so với '180 °C¹' đều được "
    "bảo lưu.</p>"
)

# ---------------------------------------------------------------------------
# Table 15.2 — printed p.467 (PDF p.488)
# ---------------------------------------------------------------------------

CAPTION152_EN = "Table 15.2 Required protective conductor cross-sectional area relative to phase conductors"
CAPTION152_VI = "Bảng 15.2 Tiết diện tối thiểu của dây dẫn bảo vệ tương ứng với dây dẫn pha"

HEAD152_EN = [
    "Phase conductor cross-sectional area<br>(mm²)",
    "Minimum cross-section required for protective conductor<br>(mm²)",
]
HEAD152_VI = [
    "Tiết diện dây dẫn pha<br>(mm²)",
    "Tiết diện tối thiểu yêu cầu của dây dẫn bảo vệ<br>(mm²)",
]

# 2 cells per row. The second column contains connector words, so the rows
# are genuinely language-specific.
ROWS152 = [
    ["≤16", "As the phase conductor"],
    [">16 but ≤35", "16"],
    [">35", "Half of the phase conductor area"],
]
ROWS152_EN = ROWS152
ROWS152_VI = [
    ["≤16", "Bằng tiết diện dây dẫn pha"],
    [">16 nhưng ≤35", "16"],
    [">35", "Một nửa tiết diện dây dẫn pha"],
]

NOTE152_EN = ""
NOTE152_VI = ""
