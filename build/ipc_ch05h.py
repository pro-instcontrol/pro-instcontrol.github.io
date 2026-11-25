# -*- coding: utf-8 -*-
"""Chapter 5, continuation of section 5.5.1 (EN/VI bilingual).

Source: Prasad, Jayaswal and Priye, *Instrumentation and Process Control*
(I.K. International, 2019), PDF pp. 276-283, printed pp. 264-271, decoded
text lines 10581-10907.  Covers the three-level I/O isolation of the
PC-based data acquisition system (Figure 5.43), the eleven worked Examples
5.1-5.11 with their printed arithmetic, and the 18-question exercise.
There are no numbered equations in the source; all formulas are emitted as
unnumbered equations and no tables are invented.

The real supplier ``ipcfig5_d`` normally registers ``fig_f43`` before this
module is imported.  A small non-overwriting fallback is installed only if
that supplier is not present yet.
"""

import ipcfig5 as F
from ipc_ch05_lib import H, P, L, E, FIG, TBL, NOTE, REFS


# ----------------------------------------------------------------- figure
def _stub_box(x, y, w, h, label):
    return ('<rect x="%d" y="%d" width="%d" height="%d" fill="#eef3fb" '
            'stroke="#1f3a5f" stroke-width="1.1"/>'
            '<text x="%d" y="%d" text-anchor="middle" font-size="7.5" '
            'fill="#1f3a5f">%s</text>'
            % (x, y, w, h, x + w / 2, y + h / 2 + 3, label))


def _stub_wire(points, arrow=False):
    d = "M" + " L".join("%g %g" % p for p in points)
    return ('<path d="%s" fill="none" stroke="#1f3a5f" stroke-width="1.1"%s/>'
            % (d, ' marker-end="url(#ipc5h)"' if arrow else ""))


def _stub_f43():
    o = ['<svg xmlns="http://www.w3.org/2000/svg" width="680" height="250" '
         'viewBox="0 0 680 250"><rect width="680" height="250" '
         'fill="#ffffff"/>',
         '<defs><marker id="ipc5h" viewBox="0 0 8 8" refX="7" refY="4" '
         'markerWidth="6" markerHeight="6" orient="auto">'
         '<path d="M0 0 L8 4 L0 8 z" fill="#1f3a5f"/></marker></defs>',
         _stub_box(20, 35, 118, 46, "Universal I/O module"),
         _stub_box(188, 35, 90, 46, "Host PC"),
         _stub_box(330, 35, 100, 46, "Opto-coupler"),
         _stub_box(482, 35, 165, 46, "Communication controller"),
         _stub_wire([(138, 58), (188, 58)], True),
         _stub_wire([(278, 58), (330, 58)], True),
         _stub_wire([(430, 58), (482, 58)], True),
         _stub_wire([(647, 58), (665, 58)], True),
         '<text x="648" y="47" text-anchor="end" font-size="7" '
         'fill="#1f3a5f">Data</text>',
         '<text x="201" y="89" text-anchor="middle" font-size="7" '
         'fill="#1f3a5f">Local bus</text>',
         _stub_box(188, 112, 120, 40, "Watchdog timer"),
         _stub_box(362, 112, 92, 40, "+5 V supply"),
         _stub_box(60, 168, 120, 46, "Rectifier and filter"),
         _stub_box(255, 168, 175, 46, "+10 to +30 V convertor"),
         _stub_wire([(248, 132), (248, 191), (255, 191)], True),
         _stub_wire([(408, 152), (408, 191), (430, 191)], True),
         _stub_wire([(180, 191), (255, 191)]),
         _stub_wire([(180, 191), (248, 191)]),
         _stub_wire([(20, 191), (60, 191)]),
         '<path d="M22 178 l6 -8 l6 16 l6 -16 l6 16 l6 -16 l6 16" '
         'fill="none" stroke="#1f3a5f" stroke-width="1.1"/>',
         '<path d="M22 204 l6 -8 l6 16 l6 -16 l6 16 l6 -16 l6 16" '
         'fill="none" stroke="#1f3a5f" stroke-width="1.1"/>',
         '<text x="340" y="242" text-anchor="middle" font-size="6.4" '
         'fill="#888888">Hinh 5.43   /   Figure 5.43</text>',
         '</svg>']
    svg = "".join(o)
    return (svg,
            "Hình 5.43 · Cách ly I/O ba cấp",
            "Figure 5.43 · Three-level I/O isolation",
            "Sơ đồ cách ly ba cấp: I/O qua bus cục bộ, nguồn qua máy biến "
            "áp và truyền thông qua quang ghép",
            "Three-level isolation: I/O via local bus, power via isolation "
            "transformer and communication via opto-coupling")


if not hasattr(F, "fig_f43"):
    F.fig_f43 = _stub_f43


# ------------------------------------------------------------------- prose
def section(lang):
    b = []

    # ------------------------------------------------ 5.5.1 (continued)
    P(b, lang,
      "Một đặc điểm khác của hệ thống này là nó làm việc với bất kỳ nguồn "
      "cấp không ổn định nào (từ +10 V đến +30 V một chiều). Hệ thống áp "
      "dụng cách ly ba cấp, tức là cách ly I/O qua bus cục bộ, cách ly nguồn "
      "qua máy biến áp cách ly và cách ly bộ điều khiển truyền thông qua "
      "quang ghép, như Hình 5.43. Mức cách ly vào khoảng 3000 V một chiều "
      "đối với các mô-đun I/O và nguồn, trong khi đó là 2500 V một chiều đối "
      "với hệ thống truyền thông. Ngoài ra, hệ thống còn cung cấp tự kiểm tra "
      "phần cứng và tính năng chẩn đoán phần mềm, bên cạnh cơ chế giám sát "
      "tự động.",
      "Yet another peculiarity of this system is that it works on any "
      "unregulated power supply system (between +10 V and +30 V D.C.). The "
      "system has adopted 3-level isolation, i.e. I/O isolation through "
      "local bus, power isolation through isolation transformer and "
      "communication controller isolation through opto-coupling isolation, "
      "as shown in Figure 5.43. The isolation is of the order of 3000 volt "
      "D.C. for I/O modules and power, whereas it is 2500 volt D.C. for the "
      "communication system. The system also provides self-test for the "
      "hardware and diagnostic feature for the software in addition to a "
      "watchdog supervisory scheme.")

    FIG(b, 43, F.fig_f43(), lang)

    P(b, lang,
      "Cơ chế giám sát tự động được thực hiện bằng một bộ định thời, trong "
      "đó có thể qui định một số tiếp điểm thường đóng tham chiếu ngay tới "
      "chính nó. Tín hiệu này ở trạng thái bật trong một chu kỳ quét và tắt "
      "trong chu kỳ quét tiếp theo miễn hệ thống còn hoạt động. Vì vậy bộ "
      "định thời cần hai chu kỳ quét để hoàn thành một chu trình đầy đủ. "
      "Phần cứng trong bộ xử lý giám sát bộ định thời này theo cách rằng nếu "
      "trạng thái của nó không thay đổi trong một khoảng thời gian qui định, "
      "chẳng hạn khoảng 200 mili giây, hệ thống sẽ bị tắt và báo lỗi.",
      "Watchdog supervision is implemented through a watchdog timer in which "
      "there can be a specified number of normally closed contacts "
      "referenced to itself. This is ON for one scan, OFF for the next scan "
      "as long as the system is in operation. Thus, it takes two scans for "
      "the watchdog timer to complete its full cycle. The hardware in the "
      "processor monitors the watchdog timer in such a way that if it does "
      "not change its status every specified time, say 200 millisecond or "
      "so, the system gets shutdown indicating system failure.")

    # --------------------------------------------------------- examples
    H(b, lang, "Các ví dụ", "EXAMPLES")

    # ------------------------------------------------------ Example 5.1
    H(b, lang, "Ví dụ 5.1", "Example 5.1", level=3)
    P(b, lang,
      "(a) Màn hình 3½ chữ số có độ phân giải là bao nhiêu? (b) Nếu thang đo "
      "của đồng hồ số 3½ chữ số là (i) 1 V và (ii) 10 V thì độ phân giải "
      "trong hai trường hợp là bao nhiêu?",
      "(a) What is the resolution of a 3½ digit display? (b) If the range of "
      "a 3½ digit digital meter is (i) 1 volt and (ii) 10 volt, what are the "
      "resolutions in the two cases?")
    H(b, lang, "Lời giải", "Solution", level=4)
    P(b, lang, "(a) Số chữ số đầy đủ có tác dụng = 3.",
      "(a) Number of full active digits = 3.")
    E(b, lang, "∴ Độ phân giải = 1/10³ = 0.001 = 0.1%",
      "∴ Resolution = 1/10³ = 0.001 = 0.1%", num="")
    P(b, lang, "(b)(i) Ở đây số đọc toàn thang = 1.000;",
      "(b)(i) Here full scale reading = 1.000;")
    E(b, lang, "Độ phân giải trên thang 1 V = 1 × 0.001 = 0.001 V",
      "Resolution on 1 volt range = 1 × 0.001 = 0.001 volt", num="")
    P(b, lang, "(ii) Trong trường hợp này số đọc toàn thang = 10.00;",
      "(ii) In this case full scale reading = 10.00;")
    E(b, lang, "Độ phân giải trên thang 10 V = 10 × 0.001 = 0.01 V",
      "Resolution on 10 volt range = 10 × 0.001 = 0.01 volt", num="")

    # ------------------------------------------------------ Example 5.2
    H(b, lang, "Ví dụ 5.2", "Example 5.2", level=3)
    P(b, lang,
      "Một đồng hồ vôn kế số 4½ chữ số được dùng để đo điện áp. (a) Tìm độ "
      "phân giải của nó. (b) 12.75 V được hiển thị thế nào trên thang 10 V? "
      "(c) 0.7525 V được hiển thị thế nào trên thang 1 V? (d) 0.7525 V được "
      "hiển thị thế nào trên thang 10 V?",
      "A 4½ digit digital voltmeter is used for voltage measurement. "
      "(a) Find its resolution. (b) How would 12.75 V be displayed on the "
      "10 V range? (c) How would 0.7525 V be displayed on the 1 V range? "
      "(d) How would 0.7525 V be displayed on the 10 V range?")
    H(b, lang, "Lời giải", "Solution", level=4)
    P(b, lang, "(a) Ở đây số chữ số đầy đủ có tác dụng = 4.",
      "(a) Here number of full active digit = 4.")
    E(b, lang, "∴ Độ phân giải = 1/10⁴ = 0.0001 = 0.01%",
      "∴ Resolution = 1/10⁴ = 0.0001 = 0.01%", num="")
    P(b, lang,
      "(b) Màn hình 4½ chữ số có năm chữ số, nên 12.75 V được hiển thị là "
      "12.750 V trên thang 10 V.",
      "(b) There are five digits on a 4½ digit display, so 12.75 V will be "
      "displayed as 12.750 V on the 10 V scale.")
    P(b, lang, "(c) Trong trường hợp này, độ phân giải trên thang 1 V:",
      "(c) In this case, resolution on the 1 V range:")
    E(b, lang, "1 × 0.0001 = 0.0001 V", "1 × 0.0001 = 0.0001 V", num="")
    P(b, lang,
      "Vì vậy trên thang 1 V, số đọc được hiển thị đến chữ số thập phân thứ "
      "tư và 0.7525 được hiển thị là 0.7525 V.",
      "So on the 1 V range, any reading is displayed up to the 4th decimal "
      "place, and 0.7525 is displayed as 0.7525 volt on the 1 volt range.")
    P(b, lang, "(d) Trong trường hợp này, độ phân giải trên thang 10 V:",
      "(d) In this particular case, resolution on the 10 V range:")
    E(b, lang, "10 × 0.0001 = 0.001 V", "10 × 0.0001 = 0.001 V", num="")
    P(b, lang,
      "Vì vậy trên thang 10 V, số đọc chỉ được hiển thị đến chữ số thập "
      "phân thứ ba và 0.7525 được hiển thị là 0.752 V.",
      "So on the 10 V range, readings are displayed up to the 3rd place "
      "only, and 0.7525 is displayed as 0.752 volt on the 10 volts range.")

    # ------------------------------------------------------ Example 5.3
    H(b, lang, "Ví dụ 5.3", "Example 5.3", level=3)
    P(b, lang,
      "Một đồng hồ vôn kế số 3½ chữ số có độ chính xác ± 0.2% số đọc ± 2 chữ "
      "số. (a) Sai số là bao nhiêu khi đồng hồ đọc 3 V trên thang 10 V? "
      "(b) Sai số là bao nhiêu khi số đọc là 0.10 V trên thang 10 V? "
      "(c) Sai số ở câu (b) chiếm bao nhiêu phần trăm số đọc?",
      "A 3½ digit voltmeter has accuracy of ± 0.2 per cent of reading ± 2 "
      "digits. (a) What shall be the error when the meter reads 3 volts on "
      "the 10 volts range? (b) What shall be the error when the reading is "
      "0.10 volt on the 10 volts range? (c) What percentage of indicated "
      "reading shall be the error in (b)?")
    H(b, lang, "Lời giải", "Solution", level=4)
    P(b, lang, "(a) 0.2% của giá trị chỉ thị là",
      "(a) 0.2 per cent of indicated value is")
    E(b, lang, "0.002 × 3.00 = 0.006 V",
      "0.002 × 3.00 = 0.006 volt", num="")
    P(b, lang,
      "Số hiển thị của 3 V trên thang 10 V của đồng hồ 3½ chữ số là 03.00. "
      "Phần trăm của chữ số có nghĩa nhỏ nhất (LSD) là 0.02 V.",
      "Display for a 3 volts reading on the 10 volts scale of a 3½ digit "
      "meter shall be 03.00. Now the percentage of digit on LSD (Least "
      "Significant Digit) is 0.02 volt.")
    E(b, lang, "Tổng sai số = 0.006 + 0.02 = 0.026 V",
      "Total error = 0.006 + 0.02 = 0.026 volt", num="")
    P(b, lang, "(b) Khi giá trị chỉ thị là 0.10 V trên thang 10 V,",
      "(b) When the indicated value is 0.10 volt on the 10 volts range,")
    E(b, lang, "± 0.2% của số đọc = 0.002 × 0.10 = 0.0002 V",
      "± 0.2 per cent of reading = 0.002 × 0.10 = 0.0002 volt", num="")
    P(b, lang, "± 2 chữ số ở LSD cho sai số ± 0.02 V.",
      "± 2 digits on LSD gives an error of ± 0.02 volt.")
    E(b, lang, "Tổng sai số = 0.0002 + 0.02 = 0.0202 V",
      "Total error = 0.0002 + 0.02 = 0.0202 volt", num="")
    P(b, lang, "(c) Phần trăm sai số ở câu (b):",
      "(c) Percentage error in (b):")
    E(b, lang, "0.0202/0.100 = 0.0202/0.1 × 100 = 20.2%",
      "0.0202/0.100 = 0.0202/0.1 × 100 = 20.2%", num="")

    # ------------------------------------------------------ Example 5.4
    H(b, lang, "Ví dụ 5.4", "Example 5.4", level=3)
    P(b, lang,
      "Một đồng hồ vôn kế số 3½ chữ số được dùng để đo điện áp. (a) Tìm độ "
      "phân giải của bộ chỉ thị. (b) 15.43 V được hiển thị thế nào trên thang "
      "10 V? (c) Số đọc 15.43 V được hiển thị thế nào trên thang 100 V?",
      "A 3½ digit voltmeter is used for measuring voltage. (a) Find the "
      "resolution of the indicator. (b) How would a voltage of 15.43 V be "
      "displayed on the 10 V scale? (c) How would a reading of 15.43 V be "
      "displayed on the 100 V scale?")
    H(b, lang, "Lời giải", "Solution", level=4)
    P(b, lang,
      "(a) Số chữ số đầy đủ có tác dụng trên màn hình 3½ chữ số = 3.",
      "(a) Number of full active digit on a 3½ digit digital display = 3.")
    E(b, lang, "∴ Độ phân giải = 1/10³ = 0.001 = 0.1%",
      "∴ Resolution = 1/10³ = 0.001 = 0.1%", num="")
    P(b, lang,
      "(b) Màn hình 3½ chữ số có bốn chữ số, nên 15.43 V được hiển thị là "
      "15.43 V trên thang 10 V.",
      "(b) There are four digits on a 3½ digit digital display, so 15.43 V "
      "shall be displayed as 15.43 V on the 10 V scale.")
    P(b, lang, "(c) Độ phân giải trên thang 100 V:",
      "(c) Resolution on the 100 V range:")
    E(b, lang, "0.001 × 100 = 0.1 V", "0.001 × 100 = 0.1 V", num="")
    P(b, lang, "Vì vậy 15.43 được hiển thị là 15.4 V.",
      "Hence, 15.43 shall be displayed as 15.4 V.")

    # ------------------------------------------------------ Example 5.5
    H(b, lang, "Ví dụ 5.5", "Example 5.5", level=3)
    P(b, lang,
      "Thang thấp nhất của đồng hồ vôn kế số 4½ chữ số là 10 milivôn toàn "
      "thang. Tìm độ nhạy.",
      "The lower range on a 4½ digit digital voltmeter is 10 millivolt full "
      "scale. Find sensitivity.")
    H(b, lang, "Lời giải", "Solution", level=4)
    P(b, lang,
      "Số chữ số đầy đủ có tác dụng trên màn hình 4½ chữ số = 4.",
      "Number of full active digit on a 4½ digit digital display = 4.")
    E(b, lang, "∴ Độ phân giải = 1/10⁴ = 0.0001",
      "∴ Resolution = 1/10⁴ = 0.0001", num="")
    P(b, lang, "Độ nhạy = giá trị toàn thang thấp nhất × Độ phân giải.",
      "Sensitivity = Lowest full scale value × Resolution.")
    E(b, lang, "10 mV × 0.0001 = 1 × 10⁻⁶ = 1 μV",
      "10 mV × 0.0001 = 1 × 10⁻⁶ = 1 μV", num="")

    # ------------------------------------------------------ Example 5.6
    H(b, lang, "Ví dụ 5.6", "Example 5.6", level=3)
    P(b, lang,
      "Đồng hồ vôn kế số 3½ chữ số có độ chính xác ± 0.5% số đọc ± 2 chữ số. "
      "(a) Sai số là bao nhiêu khi thiết bị đọc 5.00 V trên thang 10 V? "
      "(b) Sai số là bao nhiêu khi thiết bị đọc 0.10 V trên thang 10 V? "
      "(c) Phần trăm sai số ở câu (b) là bao nhiêu?",
      "A 3½ digit digital voltmeter has accuracy ± 0.5% of reading ± 2 "
      "digits. (a) What is the error when the instrument reads 5.00 volt on "
      "its 10 volts range? (b) What is the error when the instrument reads "
      "0.10 volt on its 10 volts range? (c) What is the percentage error "
      "in (b)?")
    H(b, lang, "Lời giải", "Solution", level=4)
    P(b, lang, "(a) 0.5% của giá trị chỉ thị:",
      "(a) 0.5% of indicated value:")
    E(b, lang, "0.005 × 5 = 0.025 V", "0.005 × 5 = 0.025 volt", num="")
    P(b, lang,
      "Số hiển thị của 5.00 V trên thang 10 V là 05.00. Phần trăm trên LSD "
      "là 0.02.",
      "Display for a 5.00 volt reading on the 10 volt scale shall be 05.00. "
      "Now percentage on LSD is 0.02.")
    E(b, lang, "Tổng sai số = 0.025 + 0.02 = 0.045 V",
      "Total error = 0.025 + 0.02 = 0.045 volt", num="")
    P(b, lang, "(b) Khi số đọc là 0.10 V trên thang 10 V:",
      "(b) When the reading is 0.10 volt on the 10 volt range:")
    E(b, lang, "0.005 × 0.10 = 0.0005 V; ± 2 chữ số = 0.02 V",
      "0.005 × 0.10 = 0.0005 volt; ± 2 digits = 0.02 volt", num="")
    E(b, lang, "Tổng sai số = 0.0005 + 0.02 = 0.0205 V",
      "Total error = 0.0005 + 0.02 = 0.0205 volt", num="")
    P(b, lang, "(c) Phần trăm sai số ở câu (b):", "(c) % error in (b):")
    E(b, lang, "0.0205/0.1 × 100 = 20.5%",
      "0.0205/0.1 × 100 = 20.5%", num="")

    # ------------------------------------------------------ Example 5.7
    H(b, lang, "Ví dụ 5.7", "Example 5.7", level=3)
    P(b, lang,
      "Một điện áp tương tự 2.732 cần được đo bằng đồng hồ vôn kế số xấp xỉ "
      "liên tiếp 4 bit. Tìm đầu ra số khi điện áp tham chiếu là 5 V.",
      "An analog voltage 2.732 is to be measured by successive approximation "
      "digital voltmeter of 4 bits. Find the digital output when reference "
      "voltage is 5 volts.")
    H(b, lang, "Lời giải", "Solution", level=4)
    P(b, lang, "(a) Đặt d₃ = 1 trước;", "(a) First set d₃ = 1;")
    E(b, lang, "đầu ra = 5/2¹ = 2.5 V", "output = 5/2¹ = 2.5 volt", num="")
    P(b, lang, "Vì 2.732 > 2.5, d₃ được giữ ở 1.",
      "Since 2.732 > 2.5, d₃ will be set at 1.")
    P(b, lang, "(b) Tiếp theo đặt d₂ = 1;", "(b) Next set d₂ = 1;")
    E(b, lang, "đầu ra = 2.5 + 5/2² = 3.75 V",
      "output = 2.5 + 5/2² = 3.75 volt", num="")
    P(b, lang, "Vì 2.732 < 3.75, d₂ được đặt về O (không).",
      "Since 2.732 < 3.75, d₂ will be set at O.")
    P(b, lang, "(c) Tiếp theo đặt d₁ = 1;", "(c) Next set d₁ = 1;")
    E(b, lang, "đầu ra = 2.5 + 5/2³ = 3.125 V",
      "output = 2.5 + 5/2³ = 3.125 volt", num="")
    P(b, lang, "Vì 3.125 > 2.732, d₁ được giữ ở 1.",
      "Since 3.125 > 2.732, d₁ will be set at 1.")
    P(b, lang, "(d) Tiếp theo đặt d₀ = 1;", "(d) Next set d₀ = 1;")
    E(b, lang, "đầu ra = 3.125 + 5/2⁴ = 3.4375 V",
      "output = 3.125 + 5/2⁴ = 3.4375 volt", num="")
    P(b, lang,
      "Vì 3.4375 > 2.732, d₀ được giữ ở 1. Vì vậy đầu ra số là 1011.",
      "Since 3.4375 > 2.732, d₀ will be set at 1. Thus, digital output = "
      "1011.")

    # ------------------------------------------------------ Example 5.8
    H(b, lang, "Ví dụ 5.8", "Example 5.8", level=3)
    P(b, lang,
      "Một tín hiệu tương tự có thang 0 đến 10 V có thể phân biệt được sự "
      "thay đổi nhỏ nhất là 10 milivôn. Tìm: (a) độ phân giải của nó; (b) để "
      "có cùng độ phân giải dạng số thì chọn bao nhiêu bit cho bộ chuyển đổi "
      "số của đồng hồ vôn kế số; (c) sai số lượng tử hóa.",
      "An analog signal of 0 to 10 volt range is able to distinguish a "
      "minimum change of 10 millivolt. Find (a) its resolution; (b) to have "
      "the same resolution in digital form, what number of bits can be "
      "selected for the digital converter of digital voltmeter; (c) "
      "quantization error.")
    H(b, lang, "Lời giải", "Solution", level=4)
    P(b, lang, "(a) Độ phân giải ở dạng tương tự:",
      "(a) Resolution in analog form:")
    E(b, lang, "10 mV/10 V = 1/1000 = 0.001",
      "10 mV/10 V = 1/1000 = 0.001", num="")
    P(b, lang, "(b) Nếu số bit cần thiết là n thì để có cùng độ phân giải:",
      "(b) If the required number of bits is n, then for the same "
      "resolution:")
    E(b, lang, "1/1000 = 1/2ⁿ, suy ra n = 10 (vì 2¹⁰ = 1024 ≈ 1000)",
      "1/1000 = 1/2ⁿ, so n = 10 (∴ 2¹⁰ = 1024 ≈ 1000)", num="")
    P(b, lang, "(c) Ở đây", "(c) Here")
    E(b, lang, "C = Thang tín hiệu/2ⁿ = 10/2¹⁰ = 10/1024 V ≈ 1 milivôn",
      "C = Signal range/2ⁿ = 10/2¹⁰ = 10/1024 volt ≈ 1 millivolt", num="")
    E(b, lang, "Sai số lượng tử hóa Cₑ = C/(2√3) = (1 × 10⁻³)/(2 × √3) = 0.29 milivôn",
      "Quantization error Cₑ = C/(2√3) = (1 × 10⁻³)/(2 × √3) = 0.29 millivolt",
      num="")

    # ------------------------------------------------------ Example 5.9
    H(b, lang, "Ví dụ 5.9", "Example 5.9", level=3)
    P(b, lang,
      "Cần một đồng hồ vôn kế số có độ phân giải 0.01% để đo tín hiệu tương "
      "tự 0 đến 10 V ở 1 kHz. Tìm: (a) tần số lấy mẫu thực tế nhỏ nhất; "
      "(b) số bit chọn cho đồng hồ vôn kế số; (c) giá trị tương tự của LSB "
      "(bit có nghĩa nhỏ nhất); (d) dải động của phép chuyển đổi số trong "
      "đồng hồ; (e) sai số lượng tử hóa; (f) thời gian khẩu độ.",
      "A digital voltmeter of resolution 0.01% is required to measure an "
      "analog signal of 0 to 10 volt at 1 KHz. Find: (a) Minimum practical "
      "sampling rate; (b) Number of bits selected for the digital voltmeter; "
      "(c) Analog value of LSB (last significant bit); (d) Dynamic range of "
      "digital conversion in digital voltmeter; (e) Quantization error; "
      "(f) Aperture time.")
    H(b, lang, "Lời giải", "Solution", level=4)
    P(b, lang, "(a) Như đã biết, tần số lấy mẫu thực tế phải là",
      "(a) As we know, practical sampling frequency must be")
    E(b, lang, "2.5 × fₓ = 2.5 × 1 = 2.5 kHz",
      "2.5 × fₓ = 2.5 × 1 = 2.5 KHz", num="")
    P(b, lang, "(b) Vì độ phân giải = 0.01% = 0.0001 =",
      "(b) Since resolution = 0.01% = 0.0001 =")
    E(b, lang, "1/10000 = 1/2ⁿ", "1/10000 = 1/2ⁿ", num="")
    P(b, lang,
      "Suy ra n = 14 (vì 2¹⁴ = 16,384 là số có năm chữ số và khi lấy 2¹³ thì "
      "thành 8,192 nhỏ hơn 10,000).",
      "Hence n = 14 (Since 2¹⁴ = 16,384 i.e. 5 decimal number and we take "
      "2¹³ this will become 8,192 which is less than 10,000).")
    P(b, lang, "(c) Giá trị tương đương tương tự của LSB:",
      "(c) Analog equivalent of LSB:")
    E(b, lang, "(1/2ⁿ) × thang đo = (1/2¹⁴) × 10 = 10/16384 = 610.35 μV",
      "(1/2ⁿ) × scale range = (1/2¹⁴) × 10 = 10/16384 = 610.35 μV", num="")
    P(b, lang, "(d) Dải động của phép chuyển đổi số của đồng hồ:",
      "(d) Dynamic range of digital conversion of digital voltmeter is "
      "given by:")
    E(b, lang, "6 × số bit đã chọn = 6 × 14 = 84",
      "6 × number of bits selected = 6 × 14 = 84", num="")
    P(b, lang, "(e) Ở đây", "(e) Here")
    E(b, lang, "C = Thang tín hiệu/2ⁿ = 10/2¹⁴ = 610.35 μV",
      "C = Signal range/2ⁿ = 10/2¹⁴ = 610.35 μV", num="")
    P(b, lang, "và do đó", "and hence")
    E(b, lang, "Cₑ = C/(2√3) = 610.35/(2√3) = 176.2 μV",
      "Cₑ = C/(2√3) = 610.35/(2√3) = 176.2 μV", num="")
    NOTE(b, lang,
      "Lưu ý: ta thấy C tương đương với giá trị tương tự của LSB.",
      "(Note: we see that C is equivalent to analog value of LSB)")
    P(b, lang, "(f) Thời gian khẩu độ:", "(f) Aperture time:")
    E(b, lang,
      "Tₐ = ΔE/(2π fₘₐₓ E) = 1/(2 × 3.14 × 1000 × 16384) = 9.71 × 10⁻⁹ giây",
      "Tₐ = ΔE/(2π fₘₐₓ E) = 1/(2 × 3.14 × 1000 × 16384) = 9.71 × 10⁻⁹ second",
      num="")
    E(b, lang, "Ở đây ΔE/Eₘₐₓ = 1/2¹⁴ = 1/16384",
      "Here ΔE/Eₘₐₓ = 1/2¹⁴ = 1/16384", num="")

    # ----------------------------------------------------- Example 5.10
    H(b, lang, "Ví dụ 5.10", "Example 5.10", level=3)
    P(b, lang,
      "Một điện áp tương tự 10 V cần được đo bằng số. Tìm số bit nhỏ nhất "
      "và độ phân giải thực tế để có độ chính xác tốt hơn 0.01%, cùng với "
      "thời gian chuyển đổi cho tần số xung nhịp 10 kHz, giả sử đồng hồ vôn "
      "kế số kiểu xấp xỉ liên tiếp.",
      "An analog voltage of 10 volts is to be measured digitally. Find the "
      "minimum number of bits and actual resolution to have an accuracy "
      "better than 0.01% and conversion time for a clock frequency of "
      "10 KHz, assuming successive approximation type of DVM.")
    H(b, lang, "Lời giải", "Solution", level=4)
    P(b, lang,
      "(i) Độ chính xác yêu cầu tốt hơn 0.01% = 0.0001. Nghĩa là nếu tín "
      "hiệu 10 V cần được đo thì giá trị nhỏ nhất kỳ vọng là 9.9999 V.",
      "(i) Here required accuracy is better than 0.01% = 0.0001. It means "
      "if a 10 volt signal is to be measured, a minimum value expected "
      "shall be 9.9999 volts.")
    P(b, lang, "Theo phương trình về dải chuyển đổi chính xác:",
      "According to equation of exact range of conversion:")
    E(b, lang,
      "E₀ = E_R[dₙ₋₁ × 2⁻¹ + dₙ₋₂ × 2⁻² + … + d₁ × 2⁻⁽ⁿ⁻¹⁾ + d₀ × 2⁻ⁿ]",
      "E₀ = E_R[dₙ₋₁ × 2⁻¹ + dₙ₋₂ × 2⁻² + … + d₁ × 2⁻⁽ⁿ⁻¹⁾ + d₀ × 2⁻ⁿ]",
      num="")
    P(b, lang,
      "trong đó E_R là điện áp tương tự = 10 trong trường hợp này và E₀ là "
      "đầu ra dự kiến dạng số = 9.9999. Nhìn nhanh vào phương trình trên "
      "cho thấy giá trị 9.9999 có thể đạt được khi chọn tối thiểu 16 bit. "
      "Vì vậy n = 16.",
      "where E_R is the analog voltage = 10 in this case and E₀ is the "
      "expected output in digital form = 9.9999 in this case. A quick look "
      "at the above equation reveals that a value of 9.9999 can be obtained "
      "by selecting minimum 16 bits. Hence, n = 16.")
    P(b, lang, "(ii) Độ phân giải:", "(ii) Resolution:")
    E(b, lang, "1/2ⁿ = 1/2¹⁶ = 1/65536 ≈ 0.0001",
      "1/2ⁿ = 1/2¹⁶ = 1/65536 ≈ 0.0001", num="")
    P(b, lang,
      "(iii) Trong phép chuyển đổi kiểu xấp xỉ liên tiếp, thời gian khẩu độ "
      "Tₐ tương đương với thời gian chuyển đổi T꜀.",
      "(iii) In case of successive approximation type conversion, aperture "
      "time Tₐ is equivalent to conversion time T꜀.")
    E(b, lang,
      "Tₐ = T꜀ = ΔE/(2π fₘₐₓ E) = 1/(2 × 3.14 × 10,000 × 2¹⁶) = 4.1 × 10⁻⁹ giây",
      "Tₐ = T꜀ = ΔE/(2π fₘₐₓ E) = 1/(2 × 3.14 × 10,000 × 2¹⁶) = 4.1 × 10⁻⁹ second",
      num="")
    E(b, lang, "Vì ΔE/Eₘₐₓ = 1/2¹⁶",
      "Since ΔE/Eₘₐₓ = 1/2¹⁶", num="")

    # ----------------------------------------------------- Example 5.11
    H(b, lang, "Ví dụ 5.11", "Example 5.11", level=3)
    P(b, lang,
      "Một đồng hồ vôn kế số kiểu tích phân có tụ tích phân 0.1 μF và điện "
      "trở 100 K. Nếu Eᵢ là 2 V và E₀ không được vượt quá 10 V thì thời gian "
      "lớn nhất mà Eᵢ có thể được tích phân là bao nhiêu?",
      "An integrating type digital voltmeter has an integrating capacitor "
      "of 0.1 μF and a resistance of 100 K. If Eᵢ is 2 volts, and E₀ is not "
      "to exceed 10 volts, what is the maximum time up to which Eᵢ can be "
      "integrated?")
    H(b, lang, "Lời giải", "Solution", level=4)
    P(b, lang, "Như đã biết, đối với đồng hồ vôn kế số kiểu tích phân:",
      "As we know in case of integrating type digital voltmeter:")
    E(b, lang, "E₀ = −Eᵢ × (1/RC) × t", "E₀ = −Eᵢ × (1/RC) × t", num="")
    P(b, lang,
      "Ở đây Eᵢ = 2 V; E₀ = 10 V; R = 100 KΩ; C = 0.1 μF = 0.1 × 10⁻⁶ F. "
      "Thay các giá trị này vào phương trình trên:",
      "Here Eᵢ = 2 V; E₀ = 10 V; R = 100 KΩ; C = 0.1 μF = 0.1 × 10⁻⁶ F. "
      "Putting these values in the above equation:")
    E(b, lang, "10 = (2 × t)/(100 × 1000 × 0.1 × 10⁻⁶)",
      "10 = (2 × t)/(100 × 1000 × 0.1 × 10⁻⁶)", num="")
    P(b, lang, "hay t = 0.05 giây.", "or t = 0.05 second.")

    # -------------------------------------------------------- exercise
    H(b, lang, "Bài tập", "Exercise")
    L(b, lang,
      ["Hệ thống thu thập dữ liệu là gì? Bộ chuyển đổi quan trọng như thế "
       "nào trong hệ thống?",
       "Các thành phần chính của sơ đồ thu thập dữ liệu là gì? Mô tả ngắn "
       "gọn từng thành phần.",
       "Mô tả kỹ thuật số của hệ thống ghép kênh dùng trong mạng thu thập "
       "dữ liệu.",
       "Bộ điều hòa tín hiệu là gì? Các thành phần chính của bộ điều hòa tín "
       "hiệu là gì? Mô tả ngắn gọn.",
       "Nguyên lý cơ bản của hệ thống lấy mẫu-giữ mẫu là gì? Ứng dụng ở đâu? "
       "Mô tả chi tiết.",
       "Các phần mềm ứng dụng khác nhau được dùng trong hệ thống thu thập "
       "dữ liệu và điều khiển hiện đại là gì? Mô tả ngắn gọn hai trong số đó.",
       "Các giao thức truyền thông thường dùng trong dạng tổng quát của hệ "
       "thống thu thập dữ liệu là gì? Mô tả chi tiết GPIB.",
       "Sự khác biệt giữa các hệ thống truyền thông EIA RS-422 và EIA "
       "RS-485 là gì?",
       "Sự khác biệt giữa Ethernet và CAN là gì?",
       "Ethernet và CAN mang lại những ưu điểm bổ sung nào cho tự động hóa "
       "công nghiệp?",
       "Hệ thống thu thập dữ liệu là gì? Các thành phần của hệ thống thu thập "
       "dữ liệu là gì? Mô tả ngắn gọn từng thành phần.",
       "Bộ điều hòa tín hiệu liên quan thế nào đến hệ thống thu thập dữ "
       "liệu? Tầm quan trọng của nó trong thu thập dữ liệu là gì? Một bộ "
       "điều hòa tín hiệu có thể dùng chung cho nhiều bộ chuyển đổi được "
       "không? Thảo luận.",
       "Ghép kênh là gì? Có thể thực hiện ghép kênh bằng điện tử như thế nào "
       "trong hệ thống thu thập dữ liệu?",
       "Bộ chuyển đổi dữ liệu là gì? Tại sao bộ chuyển đổi dữ liệu lại dùng "
       "chung cho nhiều hệ thống đầu vào? Mô tả một phương pháp chuyển đổi "
       "dữ liệu từ số sang tương tự.",
       "Các hệ thống truyền thông khác nhau cho tự động hóa công nghiệp là "
       "gì? Mô tả chi tiết hai trong số đó.",
       "Sự khác biệt giữa Ethernet và CAN là gì? Ban đầu chúng có được "
       "thiết kế cho tự động hóa công nghiệp không? Nếu không, tại sao lại "
       "được áp dụng trong tự động hóa công nghiệp?",
       "Mô tả hệ thống thu thập dữ liệu dựa trên PC. Những đặc điểm đặc "
       "biệt của phần cứng là gì? Mô tả ngắn gọn.",
       "Các gói phần mềm ứng dụng khác nhau cho hệ thống thu thập dữ liệu "
       "phân tán là gì? Mô tả ngắn gọn hai trong số đó."],
      ["What is a data acquisition system? How important is the transducer "
       "in the system?",
       "What are the main components of a data acquisition scheme? Describe "
       "them briefly.",
       "Describe the digital technique of a multiplexing system used in a "
       "data acquisition network.",
       "What is a signal conditioner unit? What are the main components of "
       "a signal conditioner unit? Describe them in brief.",
       "What is the basic principle of a sample and hold system? Where is "
       "it used? Describe in detail.",
       "What are the different application software used in modern data "
       "acquisition system and control? Describe any two of them in brief.",
       "What are the different communication protocols normally used in a "
       "general form of data acquisition system? Describe GPIB in detail.",
       "What is the difference between EIA RS-422 and EIA RS-485 "
       "communication systems?",
       "What is the difference between Ethernet and CAN?",
       "What additional advantages can an Ethernet and a CAN provide for "
       "process automation?",
       "What is a data acquisition system? What are the components of a "
       "data acquisition system? Describe each of them in brief.",
       "What is a signal conditioner in relation to a data acquisition "
       "system? What is its importance in data acquisition? Can a signal "
       "conditioner unit be common to a number of transducers? Discuss.",
       "What is multiplexing? How can it be implemented electronically in "
       "a data acquisition system?",
       "What is a data converter? Why is a data converter common to a "
       "number of input systems? Describe one method of Digital-to-Analog "
       "data converter.",
       "What are the different communication systems for industrial "
       "automation? Describe two of them in detail.",
       "What is the difference between Ethernet and CAN? Have they been "
       "designed for industrial automation originally? If not, why have "
       "they been adopted in industrial automation?",
       "Describe a PC-based data acquisition system. What are the "
       "specialities in its hardware part? Describe in brief.",
       "What are the different application software packages for a "
       "distributed data acquisition system? Describe any two of them in "
       "brief."],
      ordered=True)

    return b
