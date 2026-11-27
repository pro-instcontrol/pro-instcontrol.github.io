# -*- coding: utf-8 -*-
"""Table 4.1 — flammable-materials data from BS 5345 Part 1 (1989).

Reproduced in McMillan, *Electrical Installations in Hazardous Areas*, printed
pp. 90-99 (PDF pp. 111-120). 196 material rows in printed order, transcribed
from the page renders (the PDF text layer scrambles all 14 columns).
"""
import mcmillan_tbl41_a as _a
import mcmillan_tbl41_b as _b
import mcmillan_tbl41_c as _c
import mcmillan_tbl41_d as _d

ROWS = _a.ROWS + _b.ROWS + _c.ROWS + _d.ROWS

_HEAD = [
    "Flammable material", "Formula", "Melting point (°C)", "Boiling point (°C)",
    "Relative vapour density", "Flash point (°C)", "LFL Vol.%", "UFL Vol.%",
    "LFL mg/L", "UFL mg/L", "Ignition temperature (°C)",
    "Minimum igniting current (mA)", "T class of apparatus", "Apparatus group",
]
HEAD_EN = ["<b>%d</b> %s" % (i + 1, h) for i, h in enumerate(_HEAD)]

_VI = [
    "Vật liệu dễ cháy", "Công thức", "Nhiệt độ nóng chảy (°C)",
    "Nhiệt độ sôi (°C)", "Tỷ trọng hơi tương đối", "Điểm cháy (°C)",
    "LFL Vol.%", "UFL Vol.%", "LFL mg/L", "UFL mg/L",
    "Nhiệt độ đánh lửa (°C)", "Dòng đánh lửa nhỏ nhất (mA)",
    "Cấp nhiệt độ T của thiết bị", "Nhóm thiết bị",
]
HEAD_VI = ["<b>%d</b> %s" % (i + 1, h) for i, h in enumerate(_VI)]

CAPTION_EN = ("Table 4.1 · Data for flammable materials for use with electrical equipment "
              "(from BS 5345, Part 1 (1989)). Printed pp. 90-99; row order and all numeric "
              "values follow the source table.")
CAPTION_VI = ("Bảng 4.1 · Dữ liệu vật liệu dễ cháy dùng với thiết bị điện "
              "(theo BS 5345, phần 1 (1989)). Trang in 90-99; thứ tự dòng và mọi giá trị số "
              "theo đúng bảng nguồn.")

_FOOTNOTES_EN = [
    "*Sublimation temperature.",
    "†T class data not available. Seek expert advice.",
    "‡Applicable to both trans and cis forms.",
    "§Data relate only to m-cresol; o- and p- forms are less hazardous.",
    "||Data relate to ortho form. N,N-dimethylaniline is slightly more hazardous (lower flash point).",
    "¶In an enclosed vessel.",
    "**Data relate to the form di-isobutyl carbinol but data for nonan-1-ol are close.",
    "††Data relate to hexan-1-ol. Where data are available for other isomers they are similar.",
    "‡‡Data relate to octan-1-ol. Data for other isomers give higher flash point.",
    "§§Data relate to both ortho and para forms.",
    "Classes in brackets have been derived using non standard means.",
    "Note: The presence of impurities can affect the various properties.",
]
_FOOTNOTES_VI = [
    "*Nhiệt độ thăng hoa.",
    "†Không có dữ liệu cấp nhiệt độ; cần tìm ý kiến chuyên gia.",
    "‡Áp dụng cho cả dạng trans và cis.",
    "§Dữ liệu chỉ cho m-cresol; dạng o- và p- ít nguy hiểm hơn.",
    "||Dữ liệu cho dạng ortho. N,N-dimethylaniline nguy hiểm hơn đôi chút (điểm cháy thấp hơn).",
    "¶Trong bình kín.",
    "**Dữ liệu cho dạng di-isobutyl carbinol nhưng số liệu của nonan-1-ol gần tương tự.",
    "††Dữ liệu cho hexan-1-ol; khi có số liệu của các đồng phân khác thì tương tự.",
    "‡‡Dữ liệu cho octan-1-ol; các đồng phân khác có điểm cháy cao hơn.",
    "§§Dữ liệu cho cả dạng ortho và para.",
    "Cấp trong ngoặc được suy ra bằng phương pháp không chuẩn.",
    "Lưu ý: Tạp chất có thể ảnh hưởng đến các tính chất nêu trên.",
]

FOOTNOTES_EN = "<br>".join(_FOOTNOTES_EN)
FOOTNOTES_VI = "<br>".join(_FOOTNOTES_VI)
