# -*- coding: utf-8 -*-
"""Chapter 8, section 8.5: PLC (Programmable Logic Controller).

Source: Prasad, Jayaswal and Priye, *Instrumentation and Process Control*
(I.K. International, 2019), PDF pp. 376-384, printed pp. 364-372, decoded
text lines 14623-15025.  Figures 8.21-8.31 are inserted in source order;
their labels were checked against work/ipc8_pages/p376.png ... p383.png.

The vector suppliers are authored in parallel.  Until they are importable the
eleven small redraws below are installed with non-overwriting ``hasattr``
guards, so a real supplier callable is never replaced.
"""

import math

import ipcfig8 as F
from ipc_ch06_lib import H, P, L, E, FIG, TBL, NOTE, REFS

INK = "#1f3a5f"
GREY = "#777777"


# --------------------------------------------------------------- SVG helpers
def _t(x, y, s, size=7.2, anchor="middle", color=INK):
    return ('<text x="%s" y="%s" text-anchor="%s" style="font:%spx '
            'Inter,Helvetica,sans-serif;fill:%s">%s</text>'
            % (x, y, anchor, size, color, s))


def _ln(x1, y1, x2, y2, color=INK, sw=1.1):
    return ('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" '
            'stroke-width="%s"/>' % (x1, y1, x2, y2, color, sw))


def _ar(x1, y1, x2, y2, color=INK):
    ang = math.atan2(y2 - y1, x2 - x1)
    a = 6.0
    pts = "%s,%s %s,%s %s,%s" % (
        x2, y2,
        x2 - a * math.cos(ang - 0.5), y2 - a * math.sin(ang - 0.5),
        x2 - a * math.cos(ang + 0.5), y2 - a * math.sin(ang + 0.5))
    return (_ln(x1, y1, x2, y2, color) +
            '<polygon points="%s" fill="%s"/>' % (pts, color))


def _box(x, y, w, h, label, fill="#eef3fb", size=7.0):
    o = ['<rect x="%s" y="%s" width="%s" height="%s" fill="%s" '
         'stroke="%s" stroke-width="1"/>' % (x, y, w, h, fill, INK)]
    lines = str(label).split("\n")
    y0 = y + h / 2.0 - (len(lines) - 1) * size * 0.6 + size * 0.35
    for i, ln in enumerate(lines):
        o.append(_t(x + w / 2.0, y0 + i * size * 1.15, ln, size))
    return "".join(o)


def _coil(x, y, label, size=6.8):
    o = [_ln(x - 26, y, x + 26, y)]
    o.append('<ellipse cx="%s" cy="%s" rx="20" ry="9" fill="#ffffff" '
             'stroke="%s" stroke-width="1"/>' % (x, y, INK))
    o.append(_t(x, y + 2.6, label, size))
    return "".join(o)


def _contact(x, y, label, nc=False, size=6.8):
    o = [_ln(x - 26, y, x - 12, y), _ln(x + 12, y, x + 26, y)]
    o.append(_ln(x - 12, y, x + 12, y - 8 if not nc else y))
    if nc:
        o.append(_ln(x - 10, y + 7, x + 13, y - 9))
    o.append(_t(x, y - 13, label, size))
    return "".join(o)


def _mk(n, o, cvi, cen, avi, aen):
    o.append(_ln(30, 224, 650, 224, GREY, 0.6))
    o.append(_t(340, 238, "Hình 8.%d   ·   Figure 8.%d" % (n, n),
                6.4, color=GREY))
    svg = ('<svg xmlns="http://www.w3.org/2000/svg" width="680" height="250" '
           'viewBox="0 0 680 250"><rect width="680" height="250" '
           'fill="#ffffff"/>%s</svg>' % "".join(o))
    return (svg, "Hình 8.%d · %s" % (n, cvi),
            "Figure 8.%d · %s" % (n, cen), avi, aen)


# --------------------------------------------------------- fallback figures
def _fig21():
    o = [_t(340, 30, "Overhead sanitary water tank - process drawing", 8.0)]
    o.append(_box(255, 55, 170, 135, "Sanitary\nwater tank"))
    o.append(_ln(255, 105, 425, 105, "#2a6fbb", 1.2))
    o.append(_t(245, 108, "80%", 6.5, anchor="end"))
    o.append(_ln(255, 158, 425, 158, "#2a6fbb", 1.2))
    o.append(_t(245, 161, "20%", 6.5, anchor="end"))
    o.append(_box(120, 55, 100, 30, "HLS (1,4)", size=6.8))
    o.append(_box(120, 158, 100, 30, "LLS (1,3)", size=6.8))
    o.append(_box(470, 55, 130, 34, "SV1 - inlet (7,2)", size=6.6))
    o.append(_box(470, 158, 130, 34, "SV2 - outlet (5,2)", size=6.6))
    o.append(_ar(425, 120, 470, 72))
    o.append(_ar(470, 175, 425, 165))
    o.append(_t(340, 212, "110 V D.C. control supply / Instrument air", 6.8))
    return _mk(21, o, "Sơ đồ bồn nước sinh hoạt trên cao",
               "Overhead sanitary water tank, process drawing",
               "Sơ đồ công nghệ bồn nước sinh hoạt trên cao với công tắc mức và van",
               "Process drawing of an overhead sanitary water tank with level switches and valves")


def _fig22():
    o = [_t(340, 28, "Interlock drawing - terminal details", 8.0)]
    o.append(_ln(180, 45, 180, 200))
    o.append(_ln(500, 45, 500, 200))
    for y in (65, 105, 145, 185):
        o.append(_ln(180, y, 500, y))
    o.append(_contact(250, 65, "LLS"))
    o.append(_contact(400, 65, "HLS"))
    o.append(_coil(340, 105, "R1"))
    o.append(_coil(340, 145, "R2"))
    o.append(_coil(400, 185, "SV1"))
    o.append(_t(340, 214, "1,2 supply | 1,3 LLS | 1,4 HLS | 3,2 R1 | 4,2 R2 | 5,2 SV2 | 7,2 SV1", 6.0))
    return _mk(22, o, "Sơ đồ liên khóa bồn nước",
               "Interlock drawing for overhead tank level",
               "Sơ đồ liên khóa điều khiển mức bồn với tiếp điểm LLS, HLS và cuộn R1, R2, SV1, SV2",
               "Interlock ladder for tank level with LLS/HLS contacts and R1/R2/SV1/SV2 coils")


def _fig23():
    o = [_t(340, 32, "Digital-logic interlock - second level", 8.0)]
    o.append(_box(55, 80, 150, 90, "Input terminal\nstrip\nLLS / HLS", size=6.8))
    o.append(_box(265, 80, 150, 90, "Logic gates\nVCC", size=7.0))
    o.append(_box(475, 80, 150, 90, "Output terminal\nstrip\nSV1 / SV2", size=6.8))
    o.append(_ar(205, 125, 265, 125))
    o.append(_ar(415, 125, 475, 125))
    o.append(_t(340, 195, "110 volt D.C. - electronic gates replace electromechanical relays", 6.6))
    return _mk(23, o, "Liên khóa bằng cổng logic số",
               "Relay interlock replaced by digital logic gates",
               "Mức liên khóa thứ hai dùng cổng logic số thay rơ le cơ điện",
               "Second interlock level using digital logic gates in place of relays")


def _fig24():
    o = [_t(340, 30, "PLC based interlock - simplified diagram", 8.0)]
    o.append(_box(60, 75, 150, 95, "Input circuit\nterminal\nLLS / HLS", size=6.8))
    o.append(_box(265, 75, 150, 95, "PLC\ncontrol program", fill="#e6f0dc", size=7.2))
    o.append(_box(470, 75, 150, 95, "Output circuit\nterminal\nSV1 / SV2", size=6.8))
    o.append(_ar(210, 122, 265, 122))
    o.append(_ar(415, 122, 470, 122))
    o.append(_t(160, 195, "110 volt D.C.", 6.6))
    o.append(_t(340, 195, "24 volt D.C.", 6.6))
    return _mk(24, o, "Hệ thống liên khóa dùng PLC",
               "PLC based interlock system block layout",
               "Sơ đồ hệ thống liên khóa dùng PLC với mạch đầu vào, đầu ra và chương trình",
               "Simplified PLC interlock layout with input circuit, program and output circuit")


def _fig25():
    o = [_t(340, 28, "Components of a PLC", 8.0)]
    for x, lab in ((55, "Power supply\nNguồn"), (180, "Microprocessor\nVi xử lý"),
                   (305, "Memory\nBộ nhớ"), (430, "I/O system\nHệ I/O"),
                   (555, "Programmer\nBộ lập trình")):
        o.append(_box(x, 80, 105, 70, lab, size=6.6))
    for x in (160, 285, 410, 535):
        o.append(_ln(x, 115, x + 20, 115))
    o.append(_t(340, 185, "Microprocessor + memory + I/O + programming device + power supply", 6.6))
    o.append(_t(340, 205, "Input -> program -> Output", 6.6))
    return _mk(25, o, "Các thành phần của PLC",
               "Combined components of a PLC",
               "Sơ đồ hợp nhất các thành phần PLC: nguồn, vi xử lý, bộ nhớ, I/O và bộ lập trình",
               "Combined PLC components: power supply, CPU, memory, I/O and programmer")


def _fig26():
    o = [_t(340, 28, "PLC operation cycle in one scan", 8.0)]
    o.append(_box(60, 80, 150, 70, "Input scan\nQuét đầu vào", fill="#eef3fb", size=7.0))
    o.append(_box(265, 80, 150, 70, "Program scan\nQuét chương trình", fill="#e6f0dc", size=7.0))
    o.append(_box(470, 80, 150, 70, "Output scan\nQuét đầu ra", fill="#fbf0e0", size=7.0))
    o.append(_ar(210, 115, 265, 115))
    o.append(_ar(415, 115, 470, 115))
    o.append(_ar(545, 160, 135, 160))
    o.append(_t(340, 200, "Input image table -> program -> output image table", 6.6))
    return _mk(26, o, "Chu kỳ hoạt động của PLC",
               "PLC operation cycle: input, program, output scan",
               "Chu kỳ quét của PLC gồm quét đầu vào, quét chương trình và quét đầu ra",
               "PLC scan cycle with input scan, program scan and output scan")


def _fig27():
    o = [_t(340, 30, "Packaged PLC (micro PLC) - example interlock", 8.0)]
    o.append(_box(180, 60, 320, 120, "Micro PLC\n(packaged unit)", fill="#e6f0dc", size=8.0))
    o.append(_box(60, 65, 105, 45, "230 V A.C.\nsupply", size=6.6))
    o.append(_ar(165, 88, 180, 88))
    o.append(_box(60, 140, 105, 40, "0-0 / 0-1 / 0-2", size=6.4))
    o.append(_ar(165, 160, 180, 160))
    o.append(_box(530, 65, 110, 40, "SV1", size=7.0))
    o.append(_box(530, 135, 110, 40, "SV2", size=7.0))
    o.append(_ar(500, 85, 530, 85))
    o.append(_ar(500, 155, 530, 155))
    o.append(_t(340, 205, "All I/O housed in one package", 6.6))
    return _mk(27, o, "PLC dạng gói khối",
               "Packaged (micro) PLC unit",
               "PLC dạng gói khối cho hệ thống liên khóa ví dụ",
               "Packaged micro PLC for the example interlock system")


def _fig28():
    o = [_t(340, 28, "Modular PLC in a rack", 8.0)]
    o.append(_box(50, 80, 100, 75, "Power\nsupply\nmodule", size=6.4))
    o.append(_box(160, 80, 100, 75, "Microprocessor\nunit", fill="#e6f0dc", size=6.4))
    for i in range(8):
        o.append(_box(270 + i * 45, 80, 42, 75, "I/O\n%d" % i, size=6.2))
    o.append(_ln(50, 170, 630, 170))
    o.append(_t(340, 190, "230 volt A.C. - modules interconnected, any I/O PCB in any slot", 6.4))
    return _mk(28, o, "PLC dạng mô-đun",
               "Modular PLC with interconnected modules",
               "PLC dạng mô-đun gồm nguồn, CPU và các mô-đun I/O từ 0 đến 7 trên giá",
               "Modular PLC with power module, CPU and I/O modules 0 to 7 on a rack")


def _fig29():
    o = [_t(340, 28, "PC based programming unit", 8.0)]
    o.append(_box(55, 115, 110, 60, "Power\nsupply PCB", size=6.6))
    o.append(_box(175, 115, 120, 60, "Microprocessor\nPCB", fill="#e6f0dc", size=6.6))
    o.append(_box(305, 115, 130, 60, "I/O modules PCB", size=6.6))
    o.append(_ar(435, 130, 500, 75))
    o.append(_box(490, 40, 150, 55, "Personal computer\nwith keyboard", size=6.6))
    o.append(_box(490, 100, 150, 40, "Monitor", size=6.8))
    o.append(_t(340, 205, "Connected only for programming, start up and troubleshooting", 6.4))
    return _mk(29, o, "Bộ lập trình dùng PC",
               "PC based programming unit with monitor",
               "Bộ lập trình dựa trên PC gồm bản nguồn, bản vi xử lý, bản I/O, máy tính và màn hình",
               "PC based programmer with power, CPU and I/O PCBs, personal computer and monitor")


def _fig30():
    o = [_t(340, 26, "Relay ladder - overhead tank level interlock", 8.0)]
    o.append(_ln(200, 42, 200, 205))
    o.append(_ln(490, 42, 490, 205))
    for y in (62, 100, 145, 185):
        o.append(_ln(200, y, 490, y))
    o.append(_contact(250, 62, "LLS 1"))
    o.append(_contact(400, 62, "HLS 1"))
    o.append(_coil(345, 100, "R1"))
    o.append(_coil(345, 145, "R2"))
    o.append(_contact(270, 185, "1R1 6"))
    o.append(_contact(360, 185, "2R2 7", nc=True))
    o.append(_coil(450, 185, "SV1 2"))
    o.append(_t(340, 220, "1R2 -> SV2 ; decimal digit = terminal wiring number", 6.0))
    return _mk(30, o, "Sơ đồ logic thang rơ le",
               "Relay ladder diagram of the example interlock",
               "Sơ đồ logic thang rơ le điều khiển mức bồn với LLS, HLS, R1, R2, SV1, SV2",
               "Relay ladder of the overhead tank level interlock with LLS/HLS, R1/R2 and SV1/SV2")


def _fig31():
    o = [_t(340, 26, "Equivalent PLC ladder program", 8.0)]
    o.append(_ln(200, 45, 200, 205))
    o.append(_ln(490, 45, 490, 205))
    for y, r in ((68, 1), (105, 2), (150, 3), (190, 4)):
        o.append(_ln(200, y, 490, y))
        o.append(_t(175, y + 2.5, "rung %d" % r, 6.0, anchor="end"))
    o.append(_contact(270, 68, "I:000/00"))
    o.append(_contact(390, 68, "I:001/00"))
    o.append(_coil(430, 68, "0:000/00"))
    o.append(_contact(270, 105, "I:001/00"))
    o.append(_coil(430, 105, "0:001/00"))
    o.append(_contact(270, 150, "I:000/00"))
    o.append(_contact(350, 150, "0:001/01", nc=True))
    o.append(_coil(430, 150, "0:002/00"))
    o.append(_contact(270, 190, "0:001/02"))
    o.append(_coil(430, 190, "0:003/00"))
    o.append(_t(340, 222, "I = input condition ; O = output condition ; digits = word and bit", 6.0))
    return _mk(31, o, "Chương trình thang PLC tương đương",
               "Equivalent PLC ladder program with rungs 1-4",
               "Chương trình logic thang PLC tương đương với các rung 1-4 và địa chỉ I/O",
               "Equivalent PLC ladder program with rungs 1-4 and I/O reference addresses")


for _n, _fn in ((21, _fig21), (22, _fig22), (23, _fig23), (24, _fig24),
                (25, _fig25), (26, _fig26), (27, _fig27), (28, _fig28),
                (29, _fig29), (30, _fig30), (31, _fig31)):
    if not hasattr(F, "fig_f%02d" % _n):
        setattr(F, "fig_f%02d" % _n, _fn)


# --------------------------------------------------------------------- prose
def section(lang):
    b = []

    H(b, lang, "8.5 PLC (Bộ điều khiển logic lập trình được)",
      "8.5 PLC (Programmable Logic Controller)", level=2)
    P(b, lang,
      "Về cơ bản, PLC là cấp thứ ba của hệ thống điều khiển liên khóa điện. "
      "Đầu tiên trong dòng hệ thống này là sơ đồ điều khiển truyền thống dựa trên "
      "rơ le cơ điện, thông qua đó các tác động điều khiển BẬT–TẮT, hệ thống "
      "khởi động–dừng–cắt hoặc sơ đồ dừng khẩn cấp từng được triển khai trong "
      "các ngành công nghiệp chế biến. Một hệ thống liên khóa BẬT–TẮT dùng nguồn "
      "điều khiển 110 V một chiều để điều khiển mức nước của một bồn chứa nước "
      "sinh hoạt đặt trên cao được thể hiện trong Hình 8.21 (sơ đồ công nghệ) "
      "và Hình 8.22 (sơ đồ liên khóa).",
      "Basically, PLC is a third level of electrical interlock control system. "
      "First in its line have been conventional electromechanical relay based "
      "control scheme through which ON-OFF control actions or start-stop-trip "
      "systems or emergency shut-down schemes were used to be implemented in "
      "the process industries. A 110 volt D.C. control supply operated ON-OFF "
      "interlock system to control the level of an overhead sanitary water tank "
      "has been shown in Figures 8.21 (process drawing) and 8.22 (interlock "
      "drawing).")
    FIG(b, 21, F.fig_f21(), lang)

    P(b, lang,
      "Sơ đồ liên khóa trong Hình 8.22 dùng nguồn điều khiển 110 V một chiều. "
      "Các cực đấu dây của sơ đồ được liệt kê dưới đây.",
      "The interlock drawing of Figure 8.22 uses a 110 volt D.C. control supply. "
      "Its terminal details are listed below.")
    FIG(b, 22, F.fig_f22(), lang)
    P(b, lang, "Chi tiết các cực đấu dây (Terminal Details) như sau:",
      "The terminal details are as follows:")
    L(b, lang,
      ["1,2 : Nguồn điều khiển 110 V một chiều,",
       "1,3 : Tiếp điểm công tắc mức thấp (LLS),",
       "1,4 : Tiếp điểm công tắc mức cao (HLS),",
       "1,5 : Tiếp điểm thường mở của rơ le R2,",
       "1,6 : Tiếp điểm thường mở của rơ le R1,",
       "1,7 : Tiếp điểm thường đóng của rơ le R2,",
       "3,2 : Cuộn rơ le R1,",
       "4,2 : Cuộn rơ le R2,",
       "5,2 : Van điện từ SV2",
       "7,2 : Van điện từ SV1"],
      ["1,2 : 110 Volt D.C. Control Supply,",
       "1,3 : Low Level Switch (LLS) contact,",
       "1,4 : High Level Switch (HLS) contact,",
       "1,5 : Normally open contact of Relay R2,",
       "1,6 : Normally open contact of Relay R1,",
       "1,7 : Normally close contact of Relay R2,",
       "3,2 : Relay coil R1,",
       "4,2 : Relay coil R2,",
       "5,2 : Solenoid valve SV2",
       "7,2 : Solenoid valve SV1"])

    P(b, lang,
      "Sơ đồ điều khiển BẬT–TẮT nêu trên hoạt động trong khoảng mức từ 20% đến "
      "80%, nghĩa là khi bồn đạt mức 20% thì công tắc mức thấp LLS tác động và "
      "mở van cấp nước đầu vào thông qua van điện từ SV1. Trong điều kiện bất "
      "thường khi nước không được sử dụng, nếu mức nước lên tới 80% thì công tắc "
      "mức cao HLS sẽ tác động và mở van xả đầu ra thông qua van điện từ SV2.",
      "The above ON-OFF control scheme operates between 20% and 80% of level "
      "which means when the tank attains a level of 20% the LLS (Low Level "
      "Switch) operates and opens the inlet filling valve through solenoid "
      "valve SV1. In an abnormal condition when water is not used, then if the "
      "level goes to 80%, the HLS (High Level Switch) gets operational and "
      "opens outlet drain valve through solenoid valve SV2.")

    P(b, lang,
      "Sơ đồ điều khiển liên khóa tương tự cũng có thể được triển khai bằng cách "
      "dùng các cổng logic số điện tử thay cho rơ le cơ điện; cách này tạo thành "
      "cấp thứ hai trong dòng hệ thống liên khóa, như thể hiện trong Hình 8.23.",
      "The same interlock control scheme can also be implemented by utilizing "
      "electronic digital logic gates in place of electromechanical relays "
      "which shall constitute second level of the interlock system in the line "
      "as shown in Figure 8.23.")
    FIG(b, 23, F.fig_f23(), lang)

    P(b, lang,
      "Như ta có thể thấy, các phần tử của hệ thống liên khóa dựa trên những "
      "khái niệm cơ bản nêu trên bị phân tán và được đấu nối bằng các cáp điều "
      "khiển mềm. Nhược điểm nằm ở chỗ các hệ thống như vậy dễ hỏng linh kiện. "
      "Việc thay thế linh kiện và đấu dây lại tốn một lượng thời gian đáng kể, "
      "làm tăng thời gian ngừng máy của các nhà máy chế biến. Tuy nhiên, "
      "nhược điểm này đã được khắc phục bằng cách thiết kế cấp thứ ba của hệ "
      "thống liên khóa, đó là PLC, như thể hiện trong sơ đồ đơn giản của "
      "Hình 8.24.",
      "As we can observe, the interlock system elements based on the above "
      "basic concepts are scattered and are wired through flexible control "
      "cables. The disadvantage lies with the fact that such systems are prone "
      "to component failure. The component replacement and rewiring takes "
      "appreciable amount of time, which increases the downtime of the process "
      "plants. This disadvantage, however, was removed by designing third level "
      "of interlock system that is PLC as shown in the simplified diagram of "
      "Figure 8.24.")
    FIG(b, 24, F.fig_f24(), lang)

    P(b, lang,
      "PLC là một bộ điều khiển logic nhỏ gọn, phức tạp, được đấu cứng. Chỉ có "
      "các giao diện I/O được bố trí bên ngoài hệ thống. Khi hoạt động, PLC "
      "kiểm tra trạng thái đầu vào tại cổng vào và tạo ra các tác động điều "
      "khiển cho các quá trình hoặc máy móc mà nó được kết nối. Các tác động "
      "điều khiển xuất hiện dưới dạng đầu ra tại cổng ra. Toàn bộ thao tác được "
      "thực hiện bởi một chương trình điều khiển lưu trong bộ nhớ. Một thiết bị "
      "lập trình được dùng để nạp chương trình điều khiển vào hệ thống. Chương "
      "trình điều khiển này được vi xử lý quét theo lịch trình một cách tuần "
      "tự. Thời gian để kiểm tra đầu vào, thực hiện các logic điều khiển và "
      "thực thi đầu ra được gọi là thời gian quét.",
      "PLC is a complex, hard-wired compact logic control units. Only I/O "
      "interfacings are located outside the system. In operation, it examines "
      "the status of input at input port and generates control actions for "
      "processes or machines to which it is tied up. The control actions appear "
      "as output on the output port. The entire operation is carried out by a "
      "control program which is stored in memory. A programmable device is used "
      "to upload the control program into the system. This control program is "
      "scanned by the microprocessor on a scheduled basis in sequential manner. "
      "The time taken in examining the input, performing the control logics and "
      "executing the output is called SCAN time.")
    P(b, lang,
      "Sơ đồ đơn giản trong Hình 8.24 thể hiện mạch điều khiển liên khóa ví dụ "
      "đã mô tả ở trên, trong đó các công tắc mức thấp và mức cao (LLS và HLS) "
      "được đấu vào cực mạch đầu vào, còn các cực mạch đầu ra điều khiển các van "
      "điện từ SV1 và SV2. Các mạch đầu vào và đầu ra được điều khiển bởi chương "
      "trình của PLC.",
      "The simplified diagram in Figure 8.24 represents the example interlock "
      "control circuit described above wherein the low and high level switches "
      "(LLS and HLS) are wired to the input circuit terminal and the output "
      "circuit terminals drive the solenoid valves SV1 and SV2. The input and "
      "output circuits are controlled by the program of the PLC.")

    H(b, lang, "8.5.1 Các thành phần của PLC", "8.5.1 Components of PLC", level=3)
    P(b, lang,
      "Mọi loại PLC đều có các thành phần cơ bản giống nhau, ví dụ vi xử lý, "
      "hệ thống I/O, một bộ nhớ, một thiết bị lập trình và một hệ thống nguồn. "
      "Các thành phần này được thể hiện hợp nhất trong Hình 8.25.",
      "All types of PLCs have the same basic components, e.g. microprocessor, "
      "an I/O system, a memory unit, a programming device and a power supply "
      "system. These components have been shown in combined way in Figure 8.25")
    FIG(b, 25, F.fig_f25(), lang)

    H(b, lang, "(i) Bộ vi xử lý", "(i) Microprocessor unit", level=4)
    P(b, lang,
      "Vi xử lý thường được chế tạo theo yêu cầu riêng và thực hiện các chức "
      "năng toán học, logic và liên quan đến bộ nhớ. Nó đọc trạng thái đầu vào "
      "rồi thực hiện các hàm toán học và logic dựa trên các chương trình ứng "
      "dụng đã được nạp. Cuối cùng, nó tạo ra đầu ra theo logic đó. Chương trình "
      "ứng dụng và dữ liệu được lưu trong bộ nhớ. Chương trình ứng dụng gồm các "
      "tệp chương trình chi tiết, tệp chương trình con và tệp lỗi. Dữ liệu gồm "
      "các dữ liệu liên quan đến chương trình điều khiển, ví dụ trạng thái I/O, "
      "giá trị điều chỉnh bộ đếm và bộ định thời cùng các hằng số và biến khác. "
      "Ngoài ra, vi xử lý còn có bộ nhớ hệ thống để thực thi chương trình điều "
      "khiển, quét đầu vào và cập nhật đầu ra. Loại bộ nhớ trước thuộc về người "
      "dùng và có thể được người dùng truy cập, còn loại bộ nhớ sau do nhà sản "
      "xuất quy định nên không thể được người dùng truy cập.",
      "The microprocessor is normally custom made and performs the "
      "mathematical, logical and memory related functions. It reads the input "
      "status and then executes the mathematical and logical functions based on "
      "the application programs loaded. Finally it generates output according "
      "to the logic. The application program and the data are stored in the "
      "memory. The application program consists of detailed program files, "
      "subroutine files and error files. The data consists of control program "
      "related data, e.g. I/O status, counter and timer adjustment valves and "
      "other constants and variables. In addition to these, the microprocessor "
      "has system memory as well for execution of control program, scanning of "
      "input and updating of outputs. The former memory is user based and can "
      "be accessed by the user but the later memory is manufacturer based and "
      "therefore, cannot be accessed by the user.")
    P(b, lang,
      "Một chu kỳ hoạt động hoàn chỉnh trong một lần quét gồm Quét đầu vào, Quét "
      "chương trình và cuối cùng là Quét đầu ra, như thể hiện trong Hình 8.26.",
      "The complete operation cycle in one scan consists of Input Scan, "
      "Program Scan and finally Output Scan as shown in Figure 8.26.")
    FIG(b, 26, F.fig_f26(), lang)
    P(b, lang,
      "Trong lần quét đầu vào, PLC quét tuần tự các thiết bị đầu vào để phát "
      "hiện sự hiện diện của tín hiệu (trạng thái BẬT hoặc TẮT ở thời điểm ban "
      "đầu) và trạng thái đầu vào thu được được lưu trong bộ nhớ dưới dạng bảng "
      "gọi là bảng ảnh đầu vào. Trong lần quét chương trình, PLC quét các tập "
      "lệnh của chương trình điều khiển và dựa trên trạng thái đầu vào để tạo "
      "ra các đầu ra cần thiết. Đầu ra được tạo ra lại được ghi dưới dạng bảng "
      "gọi là bảng ảnh đầu ra. Các thiết bị bên ngoài được PLC điều khiển dựa "
      "trên dữ liệu có trong bảng ảnh đầu ra. Thời gian chu kỳ hoạt động của một "
      "hệ thống PLC điển hình nằm trong khoảng từ 1 đến 25 mili giây.",
      "In the input scan, the PLC scans input devices sequentially for a signal "
      "presence (ON or OFF state in the first instant) and the status of input "
      "so obtained are stored in memory in tabular form called input image "
      "table. In the program scan, the PLC scans the instruction sets of the "
      "control program and with respect to input status, generates the required "
      "outputs. The generated output is recorded again in a tabular form called "
      "output image table. External devices are controlled by the PLC, based on "
      "the data available on the output image table. Operation cycle time of a "
      "typical PLC system ranges between 1 and 25 milliseconds.")
    P(b, lang,
      "Có một dòng bộ định thời canh gác (WDT) do chính nhà sản xuất lập trình "
      "(người dùng không thể thay đổi) để giám sát hoạt động đúng đắn của hệ "
      "thống PLC. Nấc WDT là sự kết hợp của một vài tiếp điểm NC (thường đóng) "
      "nối tiếp nhau và tự tham chiếu đến chính nó. Nấc WDT ở trạng thái BẬT "
      "trong một lần quét, ở trạng thái TẮT trong lần quét tiếp theo. Nghĩa là "
      "phải mất hai lần quét để WDT hoàn thành một chu kỳ đầy đủ. Vi xử lý giám "
      "sát nấc WDT và được thiết kế sao cho nếu WDT không thay đổi trạng thái "
      "đều đặn như thiết kế, PLC sẽ bị buộc chuyển sang trạng thái ngừng (đầu ra "
      "TẮT; đèn Run TẮT). Điều này đảm bảo rằng nếu xảy ra lỗi phần cứng và PLC "
      "không thể giải một nấc cụ thể hoặc dừng quét, một trạng thái đã biết sẽ "
      "được thiết lập với tất cả đầu ra ở mức TẮT và đèn RUN tắt.",
      "There is a Watchdog Timer (WDT) line programmed by the manufacturers "
      "themselves (cannot be altered by the user) to monitor the proper "
      "functioning of the PLC system. The WDT rung is a combination of a few NC "
      "(Normally closed) contacts connected in series and referenced to itself. "
      "The WDT rung is ON for one scan, OFF for the next scan. That means, it "
      "takes two scans for the WDT to complete a full cycle operation. The "
      "microprocessor monitors the WDT rung and is designed in such a way that "
      "if the WDT does not change its state regularly as designed, the PLC shall "
      "be forced to go into shutdown state (output OFF; Run Light OFF). This "
      "ensures that if there is a hardware failure and the PLC cannot solve a "
      "specific rung or stops scanning, a known state shall be reached with all "
      "outputs OFF and the RUN light extinguished.")

    H(b, lang, "(ii) Bộ I/O", "(ii) I/O unit", level=4)
    P(b, lang,
      "Bộ I/O nối PLC với các biến công nghệ ở một đầu và với các phần tử điều "
      "khiển cuối cùng ở đầu kia. Đầu vào nhận được từ bộ chuyển đổi hoặc bộ "
      "phát trường dưới dạng tiếp điểm vật lý (mô phỏng điều kiện BẬT/TẮT, tức "
      "đầu vào rời rạc); milivôn từ cặp nhiệt điện, RTD và cảm biến biến dạng; "
      "miliampe từ bộ phát biến công nghệ; microvon hoặc milivôn từ thiết bị "
      "phân tích. Các tín hiệu này đi qua các bộ điều hòa tín hiệu phù hợp trước "
      "khi vào PLC. Tương tự, đầu ra từ PLC dưới dạng rời rạc tác động các phần "
      "tử điều khiển cuối cùng thông qua các thiết bị điều khiển thích hợp hoạt "
      "động ở điện áp điều khiển của PLC. Mức điện áp hoạt động của các phần tử "
      "điều khiển cuối cùng cao hơn điện áp điều khiển của PLC. Các mô-đun I/O "
      "gồm mô-đun I/O tương tự (chứa tín hiệu bộ phát dạng 4 đến 20 mA), mô-đun "
      "I/O rời rạc (chứa tiếp điểm BẬT/TẮT) và các mô-đun I/O đặc biệt chứa cặp "
      "nhiệt điện, RTD, máy phân tích, mô-đun truyền thông đặc biệt để liên lạc "
      "với hệ thống điều khiển phân tán (DCS) và các hệ thống PLC khác, giao "
      "diện triển khai phần mềm SCADA và các hệ thống điều khiển bằng máy tính "
      "khác.",
      "I/O unit connects the PLC to the process variables on one end and to the "
      "final control elements on the other end. Input one received from the "
      "field transducer/transmitter in the form of physical contacts "
      "(simulating ON/OFF condition i.e. discrete input); millivolt from "
      "thermocouples, RTD and strain gages; milliampere from process variable "
      "transmitters; microvolt/millivolt from analysis instruments. These "
      "signals pass through appropriate signal conditioners before entering the "
      "PLC. Similarly, output from the PLC in discrete form actuates the final "
      "control elements through suitable control devices which operate at PLC "
      "control voltage. The operating voltage level of final control elements "
      "is higher than the PLC control voltage. The I/O modules together are in "
      "the form of Analog I/O module (containing transmitter signals in the form "
      "of 4 to 20 mAmps), Discrete I/O module (containing ON/OFF contacts) and "
      "special I/O modules which contain thermocouples, RTD, analysers, special "
      "communication module to communicate with distributed control system "
      "(DCS) and other PLC systems, interface for SCADA software implementation "
      "and for any other computer control systems.")
    P(b, lang,
      "Chính số lượng I/O quyết định độ phức tạp của cấu trúc PLC. Bắt đầu từ 32 "
      "I/O cho PLC siêu nhỏ, phạm vi này lên tới cấu trúc PLC lớn có hơn 1024 "
      "I/O. Giữa hai dạng này có thể có thêm các biến thể khác, ví dụ PLC trung "
      "bình có tới 1024 I/O và PLC nhỏ có tới 256 I/O. PLC siêu nhỏ có dạng gói "
      "khối, còn các loại kia có dạng mô-đun. Trong PLC dạng mô-đun, tất cả các "
      "mô-đun được liên kết với nhau. Hình 8.27 cho thấy hệ thống điều khiển "
      "liên khóa ví dụ đã mô tả trong chương này, biểu diễn một PLC dạng gói "
      "khối, trong khi Hình 8.28 thể hiện một PLC dạng mô-đun.",
      "It is the number of I/O counts that decides the complexity of a PLC "
      "structure. Starting from 32 I/O for micro PLC, it ranges upto large PLC "
      "structure having more than 1024 I/O. In between the two more varieties "
      "can be accommodated e.g. medium PLC having upto 1024 I/O and small PLC "
      "having upto 256 I/O. The micro PLC comes in package form and the rest "
      "come in modular form. In modular PLC, all modules are interconnected "
      "together. Figure 8.27, which shows the example interlock control system "
      "described in this chapter, indicates a packaged PLC whereas Figure 8.28 "
      "shows a modular PLC unit.")
    FIG(b, 27, F.fig_f27(), lang)
    FIG(b, 28, F.fig_f28(), lang)
    P(b, lang,
      "Các mô-đun I/O được chế tạo trên bản mạch PCB và được lắp trên giá "
      "đỡ như thể hiện trong sơ đồ dạng mô-đun. Các bản mạch này có thể được "
      "tháo ra để bảo trì khi cần mà không làm gián đoạn nguồn điện. Vỏ dạng "
      "mô-đun được chế tạo theo kiểu phổ dụng để bất kỳ bản mạch I/O nào cũng "
      "có thể lắp vào bất kỳ khe nào. Phía sau vỏ mô-đun được bố trí sẵn chỗ để "
      "liên kết các hệ thống truyền thông dữ liệu.",
      "I/O modules are constructed on PCB (printed circuit board) and are "
      "installed on racks as shown on the modular diagram. These PCBs can be "
      "removed for maintenance work as and when required without interrupting "
      "the power supply. The modular housing is constructed universal type so "
      "that any I/O PCB can be installed on any slot. The back of the modular "
      "housing makes provision for interconnection of data communication "
      "systems.")

    H(b, lang, "(iii) Bộ nhớ", "(iii) Memory unit", level=4)
    P(b, lang,
      "Bộ nhớ của hệ thống PLC gồm hai phần: bộ nhớ Hệ điều hành (O.S.) và bộ "
      "nhớ ứng dụng. Bộ nhớ O.S. do người thiết kế hoặc nhà sản xuất hệ thống "
      "tạo ra và cần thiết để thực hiện các thao tác khác nhau của bộ PLC, ví dụ "
      "thực thi chương trình điều khiển, liên kết truyền thông với các thiết bị "
      "I/O và các chức năng tương tự. Bộ nhớ ứng dụng chứa chương trình điều "
      "khiển, dữ liệu và các bảng ảnh I/O.",
      "Memory unit of a PLC system is two-fold: Operating System (O.S.) memory "
      "and application memory. The O.S. memory is generated by the system "
      "designer or manufacturer and is required for performing various "
      "operations of the PLC unit, e.g. control program execution, communication "
      "linkage with I/O devices and similar other functions. The application "
      "memory contains control program, data and I/O image tables.")
    P(b, lang,
      "Các bảng ảnh I/O là các bit trong mảng dùng để lưu đầu vào nhận được từ "
      "quá trình cũng như để điều khiển các thiết bị đầu ra. Số bit tối đa trong "
      "các bảng ảnh I/O được phân chia riêng giữa thiết bị đầu vào của quá trình "
      "và thiết bị đầu ra. Ví dụ, với số lượng I/O là 1024, có thể phân bổ đều "
      "hoặc theo cách khác, nhưng tổng số bit tối đa chỉ là 1024.",
      "The I/O image tables are bits in arrays for storing the input available "
      "from process as well as for controlling the output devices. The maximum "
      "number of bits in I/O image tables shall be separately divided between "
      "process input and output devices. For instance, an I/O counts of 1024 can "
      "be distributed equally or otherwise into maximum number of bits of 1024 "
      "only.")
    P(b, lang,
      "Nội dung của bộ nhớ O.S. hoàn toàn không thể được người dùng truy cập và "
      "cũng không cần thiết phải truy cập. Nhưng bộ nhớ ứng dụng thì người dùng "
      "có thể truy cập. Bộ nhớ này mang lại khả năng lập trình cho người dùng, "
      "tại đây người dùng thực hiện mọi thao tác lập trình để làm cho PLC phù "
      "hợp với một ứng dụng cụ thể.",
      "The content of O.S. memory cannot be accessed by the user at all and is "
      "not required also. But the application memory is user accessible. This "
      "memory gives programmability to the user where the user performs all "
      "programming for making the PLC usable for a particular application.")
    P(b, lang,
      "Dung lượng bộ nhớ liên quan đến số lượng I/O cũng như độ phức tạp của "
      "chương trình điều khiển. Dung lượng bộ nhớ thường là 64 K trở lên. Yêu "
      "cầu về bộ nhớ trước hết (thường) được tính theo kinh nghiệm bằng 10 lần "
      "số lượng I/O, rồi con số này được nhân thêm 40% (một con số dựa trên "
      "kinh nghiệm thực tế).",
      "Memory capacity is related to I/O counts as well as complexities of "
      "control program. Capacity of memory unit is generally 64 K or more. "
      "Requirement of memory is first (generally) calculated empirically as 10 "
      "times of the number of I/O counts and this figure is multiplied by 40% "
      "more (a figure which is based on practical experience).")

    H(b, lang, "(iv) Bộ lập trình", "(iv) Programming unit", level=4)
    P(b, lang,
      "Bộ lập trình được dùng để thực hiện các công việc liên quan đến lập "
      "trình trên PLC; lập trình bao gồm việc nạp phần mềm PLC. Bộ lập trình có "
      "thể là một thiết bị chuyên dụng hoặc hệ thống dựa trên PC. Khi PLC đang "
      "hoạt động, bộ lập trình được giữ ngắt kết nối. Nó chỉ được nối với bộ PLC "
      "trong quá trình lập trình, khởi động và xử lý sự cố. Bộ lập trình chuyên "
      "dụng thường chỉ dùng cho bộ PLC nhỏ. Đối với các bộ khác, hệ thống dựa "
      "trên PC được sử dụng như thể hiện trong Hình 8.29.",
      "The programming unit is used to perform the programming related works on "
      "the PLC, programming constitutes loading of PLC software. Programming "
      "unit can be a dedicated unit or a PC based system. While PLC is in "
      "operation the programming unit is kept disconnected. It is connected to "
      "the PLC unit only during programming, start up and troubleshooting "
      "operation. A dedicated programming unit is normally used for smaller PLC "
      "unit only. For other units PC based system is employed as shown in Figure "
      "8.29.")
    FIG(b, 29, F.fig_f29(), lang)
    P(b, lang,
      "Khi hệ thống dựa trên PC được chọn cho một ứng dụng công nghệ cụ thể, "
      "phần mềm SCADA (giám sát điều khiển và thu thập dữ liệu) cũng có thể được "
      "triển khai để vận hành PLC từ vị trí từ xa, ví dụ phòng điều khiển trung "
      "tâm. Ưu điểm của phần mềm SCADA là ngoài việc hỗ trợ vận hành PLC từ xa, "
      "nó còn trình bày các màn hình đồ họa chi tiết dưới dạng bảng đồ họa cho "
      "quá trình trên màn hình. Phần mềm SCADA cho ứng dụng cụ thể đó phải được "
      "nạp vào máy tính cá nhân để triển khai.",
      "When a PC based system is selected for a particular process application, "
      "the software SCADA (supervisory control and data acquisition) can also "
      "be implemented for operating the PLC from remote location say central "
      "control room. The advantage of the SCADA software is that in addition to "
      "offering assistance in operating the PLC from remote location, it "
      "presents detailed graphic displays in the form of graphic panel for the "
      "process on the monitor. The SCADA software for the particular application "
      "have to be loaded on the personal computer for its implementation.")

    H(b, lang, "(v) Bộ nguồn", "(v) Power supply unit", level=4)
    P(b, lang,
      "Bộ nguồn được lắp dưới dạng bản mạch lấy 230 V xoay chiều từ lưới điện "
      "và chuyển đổi sang các mức điện áp phù hợp bên trong cho hoạt động của "
      "PLC. Nhìn chung, cần ba loại mức điện áp cho việc triển khai PLC. 24 V "
      "một chiều dùng cho hoạt động của mạch đầu vào, 5 V một chiều dùng cho "
      "hoạt động của các mạch logic bên trong PLC và 110 V một chiều dùng cho "
      "hoạt động của các thiết bị đầu ra, ví dụ van điện từ, bộ khởi động v.v.",
      "Power supply unit is installed in the form of PCB which takes 230 volt "
      "A.C. from the mains and converts it to appropriate voltage levels "
      "internally which are required for the operation of PLC. In general, three "
      "types of voltage level is required for the PLC implementation. 24 volt "
      "D.C. is used for input circuit operation, 5 volt D.C. is used for the "
      "operation of logic circuits inside the PLC and a 110 volt D.C. is used "
      "for output devices operation, e.g. solenoid valves, starters etc.")
    P(b, lang,
      "Bộ nguồn được thiết kế để loại bỏ hoặc giảm thiểu mọi loại nhiễu do đường "
      "dây điện xoay chiều hoặc thiết bị khác tạo ra. Chúng chịu được những "
      "thay đổi nhiệt độ khí quyển khắc nghiệt trong khu vực nhà máy cũng như "
      "ảnh hưởng của môi trường ẩm ướt phổ biến trong hầu hết các cơ sở công "
      "nghiệp.",
      "Power supply unit is designed to eliminate or minimize all sorts of "
      "noise generated by the A.C. power lines or by other equipment. They "
      "withstand severe atmospheric temperature changes inside the plant areas "
      "as well as the effect of humid environments prevailing inside most of "
      "the industrial establishments.")

    H(b, lang, "8.5.2 Lập trình PLC", "8.5.2 Programming of PLC", level=3)
    P(b, lang,
      "Giao tiếp đúng cách với PLC đòi hỏi phải lập trình PLC đúng cách. Việc "
      "lập trình PLC sử dụng một ngôn ngữ lập trình cụ thể. Chương trình điều "
      "khiển mô tả các tập lệnh được sắp xếp tuần tự để điều khiển các biến công "
      "nghệ nhằm duy trì hoạt động đúng đắn của nhà máy.",
      "Proper communication with the PLC requires proper programming of the "
      "PLC. Programming of PLC employs a particular programming language. The "
      "control program describes instruction sets which are sequentially "
      "arranged for controlling the process variables for maintaining proper "
      "operation of the plant.")
    P(b, lang,
      "Có nhiều ngôn ngữ lập trình để lập trình PLC nhưng logic thang là ngôn "
      "ngữ cơ bản và phổ biến nhất cho triển khai PLC đa dụng. Sơ đồ logic thang "
      "giống với hệ thống liên khóa dựa trên rơ le cơ điện, do đó dễ hiểu đối "
      "với mọi kỹ sư và kỹ thuật viên thiết bị đo.",
      "There are many programming languages for programming the PLC but Ladder "
      "Logic is the basic and the most popular programming language for general "
      "purpose PLC implementation. Ladder logic diagram resembles to "
      "electro-mechanical relay based interlock system and therefore, is easily "
      "understandable to every instrument engineer and technician.")
    P(b, lang,
      "Sơ đồ logic thang về cơ bản gồm một số ký hiệu đại diện cho thiết bị được "
      "nối với nhau bằng các đường thẳng biểu thị dòng chảy qua các thiết bị "
      "được nối. Nguồn điện tạo thành hai bên của sơ đồ logic thang và các đường "
      "mà dòng chảy đi qua được gọi là các nấc của sơ đồ. Thực tế, sơ đồ logic "
      "thang biểu thị mạch cần thiết cho hoạt động cơ bản của hệ thống điều "
      "khiển liên khóa điện, còn sơ đồ đấu dây kèm theo biểu thị kết nối vật lý "
      "của các thiết bị điều khiển cuối cùng. Sơ đồ logic thang cho hệ thống "
      "liên khóa ví dụ điều khiển mức bồn trên cao được thể hiện trong "
      "Hình 8.30. Các công tắc điều khiển mức thấp và mức cao (LLS và HLS) lần "
      "lượt điều khiển hoạt động của các rơ le cơ điện R1 và R2,",
      "The ladder logic diagram consists essentially of a number of instruments "
      "representative symbols interconnected by straight lines indicating "
      "current flow through the connected devices. The power source forms the "
      "sideways of the ladder logic diagram and the lines through which current "
      "flows are called rungs of ladder logic diagram. In fact, the ladder logic "
      "diagram indicates the required circuit for basic operation of electrical "
      "interlock control system and the associated wiring diagram indicates "
      "physical connection of the final control devices. The ladder logic "
      "diagram for the example interlock system for overhead tank level control "
      "has been shown in Figure 8.30. The low level and high-level control "
      "switches (LLS and HLS) control the operation of the electro-mechanical "
      "relays R1 and R2 respectively,")
    FIG(b, 30, F.fig_f30(), lang)
    P(b, lang,
      "và tương tự, tiếp điểm NO (thường mở) 1R1 kết hợp logic với tiếp điểm NC "
      "(thường đóng) 2R2 điều khiển van điện từ SV1, còn tiếp điểm NO 1R2 điều "
      "khiển van điện từ SV2. Chữ số thập phân biểu thị số đấu dây của cực trên "
      "sơ đồ. Một sơ đồ logic thang điển hình để lập trình PLC được thể hiện "
      "trong Hình 8.31.",
      "and similarly the NO (normally open) contact 1R1 in logical combination "
      "of NC (normally closed) contact 2R2 controls the solenoid valve SV1 and "
      "the NO contact 1R2 control the solenoid valve SV2. The decimal digit "
      "indicates the terminal wiring number of the diagram. A typical ladder "
      "logic diagram for PLC programming has been shown in Figure 8.31.")
    FIG(b, 31, F.fig_f31(), lang)

    P(b, lang,
      "Yêu cầu cơ bản của lập trình logic thang là với điều kiện đầu vào logic "
      "đã cho, điều kiện đầu ra logic yêu cầu chỉ được đáp ứng khi có tính liên "
      "tục logic để cấp điện cho các thiết bị đầu ra. Trong lập trình logic "
      "thang cũng dùng ba lệnh thông thường để triển khai chương trình: lệnh NO, "
      "lệnh NC và lệnh OTE (cấp điện cho cuộn đầu ra). Lệnh NO yêu cầu vi xử lý "
      "kiểm tra vị trí bit được gán của nó trong bộ nhớ chương trình. Nếu bit ở "
      "trạng thái BẬT (biểu thị bằng logic 1), lệnh đúng về mặt logic, tạo ra "
      "tính liên tục logic qua nấc thang. Mặt khác, nếu bit biểu thị TẮT (biểu "
      "thị bằng logic 0), không thể xác lập tính liên tục logic trên nấc thang.",
      "The basic requirement of the ladder logic programming is that with the "
      "given logical input condition, the required logical output condition "
      "should meet only when there is a logical continuity for energizing the "
      "output devices. In the ladder logic programming also, the usual three "
      "instructions are employed for implementing the program: NO instruction, "
      "NC instruction and OTE (output coil energized) instruction. The NO "
      "instruction asks the microprocessor to examine its assigned bit location "
      "in the program memory. If the bit is ON (indicated by logic 1), the "
      "instruction is logically true resulting in logical continuity through "
      "the ladder rung. On the other hand, if the bit indicates OFF (indicated "
      "by logic O), no logical continuity can be ascertained on the ladder rung.")
    P(b, lang,
      "Tương tự, lệnh NC trong sơ đồ logic thang thực chất là lệnh kiểm tra "
      "điều kiện TẮT. Lệnh này yêu cầu vi xử lý kiểm tra sự tồn tại của điều "
      "kiện TẮT. Nếu bit biểu thị TẮT, lệnh đúng về mặt logic, tạo ra tính liên "
      "tục logic qua nấc thang. Mặt khác, nếu bit biểu thị BẬT, lệnh NC sai và "
      "không thể xác lập tính liên tục logic trên nấc thang. Lệnh OTE tương "
      "đương với cuộn rơ le, yêu cầu vi xử lý đặt một vị trí nhớ cụ thể thành "
      "BẬT (bit logic 1) nếu tồn tại tính liên tục logic ở bất kỳ nấc logic nào "
      "trước đó. Trong trường hợp ngược lại, vi xử lý đặt bit lệnh cuộn đầu ra "
      "thành TẮT (logic 0).",
      "Similarly, the NC instruction from the ladder logic diagram is in fact "
      "to examine OFF instruction. This instructs the microprocessor to examine "
      "the existence of OFF condition. If the bit indicates OFF, the instruction "
      "is logically true resulting in logical continuity through the ladder "
      "rung. On the other hand, if the bit indicates ON, the NC instruction is "
      "false and no logical continuity can be ascertained on the ladder rung. "
      "The OTE instruction is just equivalent to relay coil which instructs the "
      "microprocessor to set a particular memory location to ON (logical bit 1), "
      "if a logic continuity exists in any logic rung preceding it. In case the "
      "situation is otherwise, the microprocessor sets the output coil "
      "instruction bit to OFF (logical O).")
    P(b, lang,
      "Trong Hình 8.31, I và O biểu thị điều kiện đầu vào và đầu ra. Ba chữ số "
      "đi với I hoặc O biểu thị số từ, còn hai chữ số còn lại biểu thị các bit "
      "logic. Tất cả cùng nhau biểu thị địa chỉ tham chiếu trong bộ nhớ nơi "
      "phép toán logic được thực hiện. Trong hệ thống liên khóa ví dụ của chúng "
      "ta, tính liên tục logic ở nấc 3 mở van điều khiển nước đầu vào, còn tính "
      "liên tục logic ở nấc 4 đóng van đầu vào và mở van đầu ra.",
      "In Figure 8.31, I and O represent input and output condition. The three "
      "digits associated with I or O represent word number and the rest two "
      "digits represent logic bits. These altogether represent reference address "
      "in the memory where the logic operation shall be implemented. In our "
      "example interlock control system, the logical continuity in rung 3 opens "
      "inlet water control valve whereas the logical continuity in rung 4 closes "
      "the inlet valve and opens the outlet valve.")

    P(b, lang,
      "Trong lập trình logic thang còn có các loại lệnh khác. Đó là lệnh cuộn "
      "chốt (LI); lệnh cuộn mở chốt (UI); lệnh đầu vào một lần (ONS); lệnh định "
      "thời trễ BẬT (TON) và lệnh định thời trễ TẮT (TOF) cùng một số lệnh khác. "
      "Cần lập trình LI cho một đầu ra cụ thể nếu đầu ra đó phải tiếp tục được "
      "cấp điện ngay cả khi điều kiện khởi động đã thay đổi trạng thái. Mặt "
      "khác, cần lập trình UI để đặt lại một đầu ra đã được chốt có cùng địa chỉ "
      "tham chiếu. Lệnh ONS là lệnh chỉ hoạt động trong một lần quét của vi xử "
      "lý khi có sự thay đổi điều kiện, ví dụ từ sai sang đúng. Thông thường các "
      "tác động kích hoạt được triển khai bằng lệnh ONS. Các lệnh TON và TOF "
      "được lập trình để tạo hành động trễ thời gian. TON dùng để bắt đầu hành "
      "động định thời, còn TOF dùng để dừng hành động định thời. Mạch định thời "
      "có bố trí để điều chỉnh thời gian. Sau khi thời gian cài đặt trôi qua, "
      "mạch được nối sẽ chuyển sang BẬT hoặc TẮT tùy theo yêu cầu của sơ đồ "
      "điều khiển liên khóa.",
      "There are other types of instructions as well in the ladder logic "
      "programming. They are Latch coil instruction (LI); Unlatch coil "
      "instruction (UI); One shot input instruction (ONS); Timer ON delay "
      "instruction (TON) and Timer OFF delay instruction (TOF) and several "
      "others. The programming of LI for a specific output is required if that "
      "output is to remain energized even if the initiating condition has "
      "changed its status. On the other hand, the programming of UI is required "
      "for resetting a latched output of the same address reference. ONS "
      "instruction is such instruction that is active for one micro-processor "
      "scan only when there is change in condition, e.g. false to true. "
      "Normally triggering actions are implemented by ONS instruction. The TON "
      "and TOF instructions are programmed to create time delay action. TON is "
      "for starting the timer action and TOF is for stopping the timer action. "
      "Arrangement is provided in the timer circuit for adjustment of time. "
      "After the preset time elapses, the connected circuit is made ON or OFF "
      "depending upon the requirement of the interlock control scheme.")
    P(b, lang,
      "Các lệnh nêu trên đủ cho bốn chức năng điều khiển cơ bản của PLC, ví dụ "
      "điều khiển BẬT/TẮT; xử lý dữ liệu; định thời và đếm. Để PLC thực hiện các "
      "chức năng điều khiển tiên tiến hơn, cần triển khai các kỹ thuật lập trình "
      "tiên tiến hơn. Các kỹ thuật như lệnh khối chức năng (FB); ngôn ngữ văn "
      "bản cấu trúc (ST); sơ đồ chức năng tuần tự (SFC) v.v. có khả năng lập "
      "trình PLC thực hiện các tác động điều khiển tương tự, thao tác tệp phức "
      "tạp, tuần tự hóa và chức năng báo cáo v.v.",
      "The instructions outlined above are sufficient for four basic control "
      "functions of a PLC, e.g. ON/OFF control; data manipulation; timing and "
      "counting. For making the PLC perform more advanced control functions, "
      "more advanced programming techniques are required to be implemented. "
      "Advanced programming techniques like Function Block (FB) instruction; "
      "Structural Text (ST) language; Sequential Function Chart (SFC), etc. are "
      "capable of programming the PLC for performing analog control actions, "
      "complex file operation, sequencing and reporting function etc.")

    return b
