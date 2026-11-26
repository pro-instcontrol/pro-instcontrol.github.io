# -*- coding: utf-8 -*-
"""Book 7, Chapter 22, Section B — worked ABC example and Table 22-1
(EN/VI bilingual).

Source: Baumann, *Control Valve Primer*, 5th ed. (ISA / Wiley), PDF p. 139,
printed p. 140. Covers the complete 4-inch rotary plug valve worked example
and a verbatim transcription of Table 22-1: 18 data rows, 12 printed columns,
all ditto marks (″) and printed quirks (371, 18,6, 028) checked against the
page render work/cvp22_pages/p139.png. No figures; no numbered equation.
"""
from cvp_common import p, h2, h3, eq, ul, table

PAGES_SRC = 1
BYLINE = "Hans D. Baumann · Control Valve Primer, 5th ed. (ISA / Wiley)"
TITLE_EN = "Graphical Estimation of Noise Produced by Turbulence and Cavitation of Liquids"
TITLE_VI = "Ước tính đồ thị tiếng ồn do nhiễu loạn và xâm thực chất lỏng"


# Table 22-1, transcribed verbatim from the printed page (PDF p. 139).
# Every numeric cell, ditto mark and printed quirk is preserved exactly.
_HEADER = [
    "Size in Inches", "Valve Type", "P<sub>1</sub> psia", "X", "C<sub>v</sub>",
    "X<sub>Fz</sub> / F<sub>L</sub>", "A", "B", "C", "Estimate dBA",
    "Test dBA", "Offset",
]

_ROWS = [
    ["4", "Rotary Plug",    "145", "0.7",  "18",   "0.3 / 0.9", "9.4",  "40.6", "41.5", "91.5",  "92",   "−0.5"],
    ["4", "″",              "″",   "0.2",  "″",    "″",         "″",    "″",    "9.6",  "59.6",  "61.5", "−1.9"],
    ["3", "Rotary Sleeve",  "145", "0.5",  "114",  "0.3/0.55",  "21",   "40.6", "27.6", "89.2",  "89",   "+0.2"],
    ["3", "″",              "″",   "0.2",  "″",    "″",         "″",    "″",    "9",    "67.3",  "61.5", "+5.8"],
    ["4", "Rotary Plug",    "145", "0.1",  "100",  "0.1/0.7",   "18.4", "40.6", "1.3",  "60.3",  "62",   "−1.7"],
    ["4", "″",              "″",   "0.55", "100",  "″",         "″",    "″",    "65",   "123.9", "129",  "−5.1"],
    ["2", "Globe Valve",    "145", "0.5",  "2",    "0.3/0.85",  "2.8",  "40.6", "35.1", "78.5",  "80",   "−1.5"],
    ["2", "″",              "″",   "0.3",  "2",    "″",         "″",    "″",    "15.7", "59.1",  "60",   "−0.9"],
    ["3", "Rotary Plug",    "130", "0.25", "117",  "028/0.87",  "21.2", "39",   "11.8", "72",    "77.5", "−5.5"],
    ["3", "″",              "130", "0.5",  "117",  "″",         "″",    "″",    "36.1", "96.3",  "103",  "−6.7"],
    ["6", "Butterfly",      "115", "0.25", "180",  "0.3 /0.8",  "18.6", "371",  "12.1", "67.8",  "66.5", "+1.3"],
    ["6", "″",              "″",   "0.65", "″",    "″",         "″",    "″",    "44.1", "99.8",  "100",  "−0.2"],
    ["6", "Butterfly",      "145", "0.9",  "180",  "0.3/0.6",   "18,6", "40.6", "24.2", "73.4",  "74",   "−0.6"],
    ["6", "Butterfly",      "145", "0.45", "826",  "0.4/0.66",  "26.6", "40.6", "18.1", "85.3",  "85",   "+0.3"],
    ["6", "″",              "″",   "0.65", "″",    "″",         "″",    "″",    "31.8", "99",    "95",   "+4"],
    ["2", "V-Port Globe",   "145", "0.6",  "3.5",  "0.53/0.95", "5.7",  "40.6", "24.6", "72.9",  "70.5", "+2.4"],
    ["2", "″",              "″",   "0.8",  "″",    "″",         "″",    "″",    "33.7", "80",    "83",   "−3"],
    ["3", "Rotary Sleeve",  "145", "0.5",  "63.5", "0.3/0.5",   "18",   "40.6", "35.6", "83.7",  "86",   "−2.3"],
]

_CAP_EN = "Table 22-1. Tabulation of ABC prediction versus actual test data."
_CAP_VI = "Bảng 22-1. Bảng so sánh dự đoán ABC với dữ liệu thử nghiệm thực tế."


def body_vi():
    b = []
    b.append(h3("Ví dụ minh họa"))
    b.append(p("Sau đây là một ví dụ: mức âm thanh lớn nhất của van nút xoay "
               "4 inch có C<sub>v</sub> bằng 18, F<sub>L</sub> bằng 0.8 và "
               "X<sub>Fz</sub> bằng 0.3 khi giảm áp nước từ 145 psia xuống các "
               "áp suất hạ lưu khác nhau trong ống hạ lưu 4 inch, schedule 40, "
               "là bao nhiêu?"))
    b.append(p("Trong ví dụ này, giả sử P<sub>2</sub> = 65 psia. Khi đó X = 0.55."))
    b.append(p("Trước hết, tính C<sub>v</sub>/D²; ta được 18/4² = 1.13. Từ Hình "
               "22-1, xác định hệ số A bằng 10 tại giao điểm của ống 4 inch và "
               "C<sub>v</sub> = 5 × D². Tiếp theo, dùng Hình 22-2 xác định hệ số "
               "B bằng 40.5 dBA."))
    b.append(eq("C<sub>v</sub>/D² = 18/4² = 1.13"))
    b.append(p("Dùng Hình 22-3 để xác định mức âm. Bắt đầu tại 10X = 5.5 và "
               "nhìn tới đường cong có nhãn X<sub>Fz</sub> = 0.3; mức âm sẽ là "
               "36.5 dB. Khi đó tổng các hệ số cho kết quả đánh giá như sau:"))
    b.append(eq("L<sub>Ae,1m</sub> = A + B + C = 10 + 40.5 + 36 = 86.6 dBA"))
    b.append(p("Ba giá trị đọc từ đồ thị được tóm tắt như sau:"))
    b.append(ul([
        "Đồ thị A (Hình 22-1): A = 10 tại D = 4 in và C<sub>v</sub>/D² = 1.13.",
        "Đồ thị B (Hình 22-2): B = 40.5 dBA tại P<sub>1</sub> = 145 psia.",
        "Đồ thị C (Hình 22-3): C ≈ 36 dBA tại 10X = 5.5 với X<sub>Fz</sub> = 0.3.",
    ]))
    b.append(p("So sánh kết quả này với số liệu thử nghiệm 89 dBA từ Hình 22-4. "
               "Khá gần khi dùng phương pháp đồ thị."))
    b.append(table(_HEADER, [list(r) for r in _ROWS], _CAP_VI))
    return "".join(b)


def body_en():
    b = []
    b.append(h3("Worked Example"))
    b.append(p("Here is an example: What is the maximum sound level of a 4-inch "
               "rotary plug valve having a C<sub>v</sub> of 18, F<sub>L</sub> of "
               "0.8, and X<sub>Fz</sub> of 0.3, reducing water from 145 psia to "
               "various downstream pressures in a 4-inch, schedule 40 downstream "
               "pipe?"))
    b.append(p("For our example, assume that P<sub>2</sub> = 65 psia. This makes "
               "X = 0.55."))
    b.append(p("To start, calculate C<sub>v</sub>/D²; this is 18/4² = 1.13. From "
               "Figure 22-1, we identify an A factor of 10 at the intersection "
               "of a 4-inch pipe and C<sub>v</sub> = 5 × D². Next, using Figure "
               "22-2 we identify a B factor of 40.5 dBA."))
    b.append(eq("C<sub>v</sub>/D² = 18/4² = 1.13"))
    b.append(p("Use Figure 22-3 to determine the sound level. Start at 10X = 5.5 "
               "and look toward the curve reading X<sub>Fz</sub> = 0.3; the sound "
               "level will be 36.5 dB. Now, the printed solution reads:"))
    b.append(eq("A + B = C = 10 + 40.5 + 36 = 86.6 dBA"))
    b.append(p("The three graph readings are summarized below:"))
    b.append(ul([
        "Graph A (Figure 22-1): A = 10 at D = 4 in and C<sub>v</sub>/D² = 1.13.",
        "Graph B (Figure 22-2): B = 40.5 dBA at P<sub>1</sub> = 145 psia.",
        "Graph C (Figure 22-3): C ≈ 36 dBA at 10X = 5.5 for X<sub>Fz</sub> = 0.3.",
    ]))
    b.append(p("Compare this solution with the test data of 89 dBA from Figure "
               "22-4. Fairly close for a graphical method."))
    b.append(table(_HEADER, [list(r) for r in _ROWS], _CAP_EN))
    return "".join(b)
