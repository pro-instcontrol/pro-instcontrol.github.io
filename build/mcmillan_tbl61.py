# -*- coding: utf-8 -*-
"""Tables 6.1 and 6.3 from McMillan Chapter 6 (dust area classification).

Transcribed from the verified page renders (printed pp. 150 and 156; PDF
pp. 171 and 177). Rows are shared between languages; only headers, captions
and the source note are localized.
"""

HEAD61_EN = [
    "BS 5345, Part 2 (1983)<br>Zone",
    "BS 6467, Part 2 (1988)<br>Zone",
    "IEC 1241–3 (1994)<br>(Draft)<br>Zone",
]

HEAD61_VI = [
    "BS 5345, Part 2 (1983)<br>Vùng",
    "BS 6467, Part 2 (1988)<br>Vùng",
    "IEC 1241–3 (1994)<br>(Dự thảo)<br>Vùng",
]

ROWS61 = [
    ["0", "", "20"],
    ["1", "Z", "21"],
    ["2", "Y", "22"],
]

CAPTION61_EN = "Table 6.1 Approximate relationship between Zones (Printed p. 150; PDF p. 171)."
CAPTION61_VI = "Bảng 6.1 Mối quan hệ xấp xỉ giữa các Vùng (Trang in 150; PDF 171)."

HEAD63_EN = [
    "Grade of source",
    "Dust clouds",
    "Dust layers<br>Uncontrolled thickness",
    "Dust layers<br>Controlled thickness<br>disturbed often",
    "Dust layers<br>Controlled thickness<br>disturbed rarely",
]

HEAD63_VI = [
    "Cấp nguồn phát thải",
    "Đám mây bụi",
    "Lớp bụi lắng<br>Độ dày không kiểm soát",
    "Lớp bụi lắng<br>Độ dày được kiểm soát<br>bị xáo trộn thường xuyên",
    "Lớp bụi lắng<br>Độ dày được kiểm soát<br>hiếm khi bị xáo trộn",
]

ROWS63 = [
    ["continuous", "20", "20", "21", "22"],
    ["primary", "21", "20", "21", "22"],
    ["secondary", "22", "20", "21", "22"],
]

CAPTION63_EN = "Table 6.3 Grade of release/Zone relationship (including effect of layers)"
CAPTION63_VI = "Bảng 6.3 Mối quan hệ giữa cấp phát thải và Vùng (bao gồm ảnh hưởng của lớp bụi lắng)"

NOTE63_EN = "(From BS/94/213454 DC⁴)"
NOTE63_VI = "(Theo BS/94/213454 DC⁴)"
