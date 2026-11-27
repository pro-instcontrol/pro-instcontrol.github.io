# -*- coding: utf-8 -*-
"""Tables 9.1, 9.2 and 9.3 from McMillan Chapter 9.

Transcribed from the authoritative page renders:
  - printed p.214 / PDF p.235 -> Table 9.1
  - printed p.221 / PDF p.242 -> Table 9.2
  - printed p.222 / PDF p.243 -> Table 9.3

Printed quirks are preserved deliberately, not silently corrected:

  * Table 9.1 has a full-width scope line between its caption and column
    headers ("Minimum distances between bare live parts ..."). It is carried
    in CAPTION91_* (second line) so the two-column HEAD/ROWS structure stays
    intact and the line remains localized in both languages.
  * Table 9.2 printed header reads "taking account of supply voltage
    variations"; the brief omitted "of", the page image governs here.
  * Table 9.3 note 3 prints an unmatched parenthesis in "(see BS 5901
    (1980). Method of Test ...)" - retained verbatim. The N/A cell carries
    its printed superscript 6.
  * All non-ASCII characters (µ, ·, ×, °, superscripts) are literal Unicode.
"""

# ---------------------------------------------------------------------------
# Table 9.1 - Separation between live parts through encapsulant
# ---------------------------------------------------------------------------

HEAD91_EN = [
    "Maximum voltage between live parts at maximum rated supply voltage "
    "taking account of faults and recognized overloads¹<br>(Volts rms)",
    "Minimum permissible separation²<br>(mm)",
]

HEAD91_VI = [
    "Điện áp tối đa giữa các bộ phận mang điện tại điện áp nguồn định mức "
    "tối đa, có tính đến sự cố và quá tải được thừa nhận¹<br>(Vôn RMS)",
    "Khoảng cách tối thiểu cho phép²<br>(mm)",
]

# Eight 2-cell data rows in printed order. Verified against p235.png.
ROWS91 = [
    ["380", "1.0"],
    ["500", "1.5"],
    ["660", "2.0"],
    ["1000", "2.5"],
    ["1500", "4.0"],
    ["3000", "7.0"],
    ["6000", "12.0"],
    ["10000", "20.0"],
]

CAPTION91_EN = (
    "Separation between live parts through encapsulant<br>"
    "Minimum distances between bare live parts of the same circuit, "
    "different circuits and any circuit and earthed metallic parts"
)

CAPTION91_VI = (
    "Phân tách các bộ phận mang điện qua vật liệu bọc kín<br>"
    "Khoảng cách tối thiểu giữa các bộ phận mang điện trần của cùng một mạch, "
    "giữa các mạch khác nhau và giữa bất kỳ mạch nào với các bộ phận kim loại "
    "nối đất"
)

NOTE91_EN = (
    "<p>(From BS 5501, Part 8³)</p>"
    "<p>1 The voltage in practice may exceed the values above by up to 10% "
    "without the necessity to move to the next highest figure.</p>"
    "<p>2 Where the separation is between two live parts via an interposing "
    "isolated conducting part the separation required will be formed by the "
    "total of the separations of the two live parts and the interposing "
    "part.</p>"
)

NOTE91_VI = (
    "<p>(Theo BS 5501, phần 8³)</p>"
    "<p>1 Trên thực tế, điện áp có thể vượt quá các giá trị nêu trên tới 10% "
    "mà không cần chuyển sang giá trị cao hơn tiếp theo.</p>"
    "<p>2 Trường hợp khoảng cách nằm giữa hai bộ phận mang điện thông qua "
    "một bộ phận dẫn điện trung gian được cách ly, khoảng cách yêu cầu sẽ "
    "bằng tổng của hai khoảng cách giữa các bộ phận mang điện và bộ phận "
    "trung gian đó.</p>"
)

# ---------------------------------------------------------------------------
# Table 9.2 - Separations between conducting parts and insulating parts
#             and/or the enclosure through the filling material
# ---------------------------------------------------------------------------

HEAD92_EN = [
    "Maximum voltage taking account of supply voltage variations, "
    "recognized overloads and faults¹<br>(Volts rms ac/dc)",
    "Minimum separation²<br>(mm)",
]

HEAD92_VI = [
    "Điện áp tối đa có tính đến sự thay đổi của điện áp nguồn, quá tải được "
    "thừa nhận và sự cố¹<br>(Vôn RMS xoay chiều/một chiều)",
    "Khoảng cách tối thiểu²<br>(mm)",
]

# Eight 2-cell data rows in printed order. Verified against p242.png.
ROWS92 = [
    ["0 to 275", "5"],
    ["276 to 420", "6"],
    ["421 to 550", "8"],
    ["551 to 750", "10"],
    ["751 to 1000", "14"],
    ["1001 to 3000", "36"],
    ["3001 to 6000", "60"],
    ["6001 to 10000", "100"],
]

CAPTION92_EN = (
    "Separations between conducting parts and insulating parts and/or the "
    "enclosure through the filling material"
)

CAPTION92_VI = (
    "Phân tách giữa các bộ phận dẫn điện và các bộ phận cách điện và/hoặc vỏ "
    "bọc thông qua vật liệu điền đầy"
)

NOTE92_EN = (
    "<p>(from BS/EN 50017)</p>"
    "<p>1 This is the voltage through the filling between electrically "
    "conducting parts and insulating parts and/or the inner surface of the "
    "enclosure.</p>"
    "<p>2 This separation applies even when the electrically conducting part "
    "is isolated.</p>"
)

NOTE92_VI = (
    "<p>(theo BS/EN 50017)</p>"
    "<p>1 Đây là điện áp xuyên qua vật liệu điền đầy giữa các bộ phận dẫn "
    "điện và các bộ phận cách điện và/hoặc bề mặt bên trong của vỏ bọc.</p>"
    "<p>2 Khoảng cách này được áp dụng ngay cả khi bộ phận dẫn điện được "
    "cách ly.</p>"
)

# ---------------------------------------------------------------------------
# Table 9.3 - Separations of conducting parts within the filling
# ---------------------------------------------------------------------------

HEAD93_EN = [
    "Peak Voltage¹<br>(Volts)",
    "Creepage distance²<br>(mm)",
    "Minimum CTI value³",
    "Creepage distance under coating⁴<br>(mm)",
    "Distance through filling material⁵<br>(mm)",
]

HEAD93_VI = [
    "Điện áp đỉnh¹<br>(Vôn)",
    "Chiều dài đường rò bề mặt²<br>(mm)",
    "Giá trị CTI tối thiểu³",
    "Chiều dài đường rò bề mặt dưới lớp phủ⁴<br>(mm)",
    "Khoảng cách xuyên qua vật liệu điền đầy⁵<br>(mm)",
]

# Eleven 5-cell data rows in printed order. Verified against p243.png;
# the first CTI cell retains its printed superscript 6 in "N/A⁶".
ROWS93 = [
    ["10", "1.5", "N/A⁶", "0.6", "1.5"],
    ["30", "2.0", "100", "0.7", "1.5"],
    ["60", "3.0", "100", "1.0", "1.5"],
    ["90", "4.0", "100", "1.3", "2.0"],
    ["190", "8.0", "175", "2.6", "3.0"],
    ["375", "10.0", "175", "3.3", "3.0"],
    ["550", "15.0", "175", "5.0", "3.0"],
    ["750", "18.0", "175", "6.0", "5.0"],
    ["1000", "25.0", "175", "8.3", "5.0"],
    ["1300", "36.0", "175", "12.0", "10.0"],
    ["1575", "49.0", "175", "13.3", "10.0"],
]

CAPTION93_EN = "Separations of conducting parts within the filling"

CAPTION93_VI = "Phân tách các bộ phận dẫn điện bên trong vật liệu điền đầy"

NOTE93_EN = (
    "<p>(from BS/EN 50017)</p>"
    "<p>1 This is the maximum peak voltage between any two live parts at "
    "maximum rated voltage with recognized overloads and faults. Where "
    "energized parts do not have a common reference the sum of the two "
    "voltages concerned will be used.</p>"
    "<p>2 This is the minimum distance along an insulating surface within "
    "the filling.</p>"
    "<p>3 Comparative Tracking Index (CTI) is a measure of the quality of "
    "insulation against breakdown by contamination (see BS 5901 (1980). "
    "Method of Test for Determining the Comparative and proof Tracking "
    "indices of Solid Insulating Materials Under Moist Conditions).</p>"
    "<p>4 The conformal coating must be such as to totally cover the "
    "conducting parts, adhere to both the conducting parts and the "
    "insulation, and effectively exclude moisture.</p>"
    "<p>5 The shortest direct distance through the filling material between "
    "two conducting parts.</p>"
    "<p>6 CTI is not considered relevant below 10 V.</p>"
    "<p>7 Where voltages between conducting parts are in excess of 1575 V "
    "failure is always considered.</p>"
)

NOTE93_VI = (
    "<p>(theo BS/EN 50017)</p>"
    "<p>1 Đây là điện áp đỉnh tối đa giữa bất kỳ hai bộ phận mang điện nào "
    "tại điện áp định mức tối đa, có tính đến quá tải và sự cố được thừa "
    "nhận. Trường hợp các bộ phận được cấp điện không có điểm tham chiếu "
    "chung, sẽ dùng tổng của hai điện áp liên quan.</p>"
    "<p>2 Đây là khoảng cách nhỏ nhất dọc theo bề mặt cách điện bên trong "
    "vật liệu điền đầy.</p>"
    "<p>3 Chỉ số theo dõi so sánh (CTI) là thước đo chất lượng cách điện "
    "chống sự phá hủy do nhiễm bẩn (xem BS 5901 (1980). Phương pháp thử để "
    "xác định chỉ số theo dõi so sánh và chỉ số theo dõi chứng minh của vật "
    "liệu cách điện rắn trong điều kiện ẩm).</p>"
    "<p>4 Lớp phủ bảo vệ phải bao phủ hoàn toàn các bộ phận dẫn điện, bám "
    "chắc vào cả các bộ phận dẫn điện lẫn lớp cách điện và ngăn ẩm hiệu "
    "quả.</p>"
    "<p>5 Khoảng cách trực tiếp ngắn nhất xuyên qua vật liệu điền đầy giữa "
    "hai bộ phận dẫn điện.</p>"
    "<p>6 CTI không được coi là có liên quan dưới 10 V.</p>"
    "<p>7 Trường hợp điện áp giữa các bộ phận dẫn điện vượt quá 1575 V thì "
    "luôn luôn coi là hư hỏng.</p>"
)
