# -*- coding: utf-8 -*-
"""Table 6.2 aggregator for McMillan Chapter 6.

The two landscape printed pages (printed pp. 152-153; PDF pp. 173-174) carry
one table.  The rows are assembled from three source-order transcription
modules; only headers, caption and the printed-conventions note are localized.
"""
import mcmillan_tbl62_a as _a
import mcmillan_tbl62_b as _b
import mcmillan_tbl62_c as _c

HEAD_EN = [
    "Dust",
    "&lt;500<br>µm",
    "&lt;125<br>µm",
    "&lt;71<br>µm",
    "&lt;32<br>µm",
    "&lt;20<br>µm",
    "Median<br>µm",
    "Ignition temp.<br>of cloud<br>°C",
    "Ignition temp.<br>of layer<br>°C",
    "Cloud Ign.<br>energy<br>mj",
    "Min Explosive<br>conc.<br>g/l",
]

HEAD_VI = [
    "Bụi",
    "&lt;500<br>µm",
    "&lt;125<br>µm",
    "&lt;71<br>µm",
    "&lt;32<br>µm",
    "&lt;20<br>µm",
    "Trung vị<br>µm",
    "Nhiệt độ bắt lửa<br>đám mây<br>°C",
    "Nhiệt độ bắt lửa<br>lớp bụi<br>°C",
    "Năng lượng bắt lửa<br>đám mây<br>mj",
    "Nồng độ nổ tối thiểu<br>g/l",
]

ROWS = _a.ROWS + _b.ROWS + _c.ROWS

CAPTION_EN = ("Table 6.2 Properties of Combustible dusts (part from BS 6467, "
              "Part 2 (1988)) — printed pp. 152-153; PDF pp. 173-174.")
CAPTION_VI = ("Bảng 6.2 Tính chất của bụi cháy được (một phần từ BS 6467, "
              "Phần 2 (1988)) — trang in 152-153; PDF 173-174.")

NOTE_EN = ("<b>Printed conventions retained.</b> The particle-size columns are "
           "percentages by mass. The ignition-energy unit is printed in lower "
           "case as 'mj'; minimum explosive concentration is printed in g/l, "
           "while the prose on printed p.158 gives 50-100 g of dust per m³ of "
           "air. Blank median cells, 'Melts', 'No glowing to ... °C', and the "
           "two near-duplicate polyacrylonitrile rows are preserved exactly "
           "as printed rather than silently reconciled.")
NOTE_VI = ("<b>Quy ước in được giữ nguyên.</b> Các cột kích thước hạt là phần "
           "trăm theo khối lượng. Đơn vị năng lượng bắt lửa được in thường là "
           "'mj'; nồng độ nổ tối thiểu được in bằng g/l, trong khi thân văn bản "
           "trang in 158 nêu 50-100 g bụi cho mỗi m³ không khí. Các ô trung vị "
           "để trống, mục 'Melts', mục 'No glowing to ... °C' và hai dòng "
           "polyacrylonitrile gần trùng được giữ đúng như bản in, không hiệu "
           "chỉnh lặng lẽ.")
