# -*- coding: utf-8 -*-
"""Chapter 5, section 5.1 "Introduction" (EN/VI bilingual).

Source: Prasad, Jayaswal and Priye, *Instrumentation and Process Control*
(I.K. International, 2019), PDF pp. 241-244, printed pp. 229-232, decoded
text lines 9128-9258.  Figure 5.1 (DAQ block diagram) and Figure 5.2
(data logging scheme with electronic transmitters) are placed where the
prose refers to them.

The `ipcfig5_a` supplier is authored in parallel with this prose module.
When it is not yet importable, small but genuine vector redraws of the two
printed block diagrams are installed as non-overwriting fallbacks; as soon
as the real supplier registers `fig_f01` / `fig_f02`, those callables win.
"""

import ipcfig5 as F
from ipc_ch05_lib import H, P, L, E, FIG, TBL, NOTE, REFS


# ----------------------------------------------------------------- figures
def _T(x, y, s, size=8.0, anchor="middle", color="#1f3a5f"):
    return ('<text x="%s" y="%s" text-anchor="%s" font-size="%s" '
            'fill="%s">%s</text>' % (x, y, anchor, size, color, s))


def _box(x, y, w, h):
    return ('<rect x="%d" y="%d" width="%d" height="%d" fill="#eef3fb" '
            'stroke="#1f3a5f" stroke-width="1.2"/>' % (x, y, w, h))


def _ar(x1, y1, x2, y2, mid):
    return ('<path d="M%d %d L%d %d" fill="none" stroke="#1f3a5f" '
            'stroke-width="1.2" marker-end="url(#%s)"/>'
            % (x1, y1, x2, y2, mid))


def _wire(pts, mid=""):
    d = "M" + " L".join("%d %d" % p for p in pts)
    m = ' marker-end="url(#%s)"' % mid if mid else ""
    return ('<path d="%s" fill="none" stroke="#1f3a5f" '
            'stroke-width="1.1"%s/>' % (d, m))


def _standalone_fig(n):
    mid = "ipc5a%d" % n
    o = ['<defs><marker id="%s" viewBox="0 0 8 8" refX="7" refY="4" '
         'markerWidth="6" markerHeight="6" orient="auto">'
         '<path d="M0 0 L8 4 L0 8 z" fill="#1f3a5f"/></marker></defs>' % mid]

    if n == 1:
        title = "Data acquisition block diagram"
        cvi = "Sơ đồ khối hệ thống thu thập dữ liệu"
        cen = "Block diagram of a data acquisition system"
        avi = ("Tín hiệu tương tự từ bộ chuyển đổi đi qua bộ điều hòa tín hiệu, "
               "bộ ghép kênh và ADC trước khi tới PC")
        aen = ("Analog transducer signals pass through a conditioner, a "
               "multiplexer and an ADC on their way to a PC")
        o.append(_box(20, 45, 120, 140))
        o.append(_T(80, 60, "Analog signals", 7.2))
        o.append(_T(80, 71, "from", 7.2))
        o.append(_T(80, 82, "transducers", 7.2))
        o.append(_box(170, 45, 120, 140))
        o.append(_T(230, 60, "Signals", 7.2))
        o.append(_T(230, 71, "conditioner unit", 7.0))
        o.append(_box(330, 45, 110, 140))
        o.append(_T(385, 108, "Multi-", 8.0))
        o.append(_T(385, 122, "plexing", 8.0))
        o.append(_T(385, 136, "unit", 8.0))
        for y, lab in zip((102, 120, 138, 156, 174), ("1", "2", "3", "…", "n")):
            o.append(_T(80, y + 3, lab, 7.5))
            o.append(_T(230, y + 3, lab, 7.5))
            o.append(_ar(140, y, 170, y, mid))
            o.append(_ar(290, y, 330, y, mid))
        o.append(_ar(440, 117, 490, 117, mid))
        o.append(_box(490, 100, 54, 34))
        o.append(_T(517, 120, "ADC", 8.0))
        o.append(_ar(544, 117, 606, 117, mid))
        o.append(_T(610, 120, "To PC", 8.0, anchor="start"))
    else:
        title = "Data logging scheme with electronic transmitters"
        cvi = "Sơ đồ ghi dữ liệu dùng bộ phát điện tử"
        cen = "Data logging system using electronic transmitters"
        avi = ("Các bộ phát Tx1 đến Tx5 đưa tín hiệu qua bộ ghép kênh, bộ chuyển "
               "đổi A/D và máy tính để lưu trữ, báo động và in hồ sơ")
        aen = ("Transmitters Tx1 to Tx5 feed a multiplexer, an A/D converter "
               "and a computer for storage, alarms and hard-copy records")
        o.append(_box(255, 26, 170, 36))
        o.append(_T(340, 48, "Unit operation process", 8.0))
        o.append(_box(20, 28, 52, 30))
        o.append(_T(46, 47, "Tx1", 7.5))
        o.append(_box(608, 28, 52, 30))
        o.append(_T(634, 47, "Tx5", 7.5))
        o.append(_ar(255, 44, 72, 44, mid))
        o.append(_ar(425, 44, 608, 44, mid))
        for x, lab in ((250, "Tx2"), (317, "Tx3"), (384, "Tx4")):
            o.append(_box(x, 74, 46, 24))
            o.append(_T(x + 23, 90, lab, 7.5))
            o.append(_ar(x + 23, 62, x + 23, 74, mid))
        o.append(_wire([(46, 58), (46, 104), (176, 104), (176, 112)], mid))
        o.append(_wire([(634, 58), (634, 104), (504, 104), (504, 112)], mid))
        o.append(_box(150, 112, 380, 26))
        o.append(_T(340, 129, "Multiplexing unit", 8.0))
        o.append(_ar(600, 125, 530, 125, mid))
        o.append(_T(604, 122, "Address lines", 6.5, anchor="start"))
        o.append(_ar(340, 138, 340, 148, mid))
        o.append(_box(300, 148, 80, 28))
        o.append(_T(340, 160, "A/D", 7.0))
        o.append(_T(340, 170, "convertor", 6.5))
        o.append(_ar(340, 176, 340, 188, mid))
        o.append(_box(280, 188, 120, 28))
        o.append(_T(340, 205, "Computer system", 7.5))
        o.append(_box(10, 150, 110, 26))
        o.append(_T(65, 160, "Generation of", 7.0))
        o.append(_T(65, 170, "alarms", 7.0))
        o.append(_wire([(280, 196), (240, 196), (240, 163), (120, 163)], mid))
        o.append(_box(560, 150, 110, 26))
        o.append(_T(615, 166, "Hard copier", 7.5))
        o.append(_wire([(400, 196), (440, 196), (440, 163), (560, 163)], mid))
        o.append(_box(10, 190, 110, 26))
        o.append(_T(65, 206, "Auxiliary storage", 7.0))
        o.append(_ar(280, 208, 120, 208, mid))
        o.append(_box(560, 190, 110, 26))
        o.append(_T(615, 206, "Operator station", 7.0))
        o.append(_ar(400, 208, 560, 208, mid))

    o.append(_T(340, 242, "Hình 5.%d   ·   Figure 5.%d" % (n, n), 6.4, color="#888888"))
    svg = ('<svg xmlns="http://www.w3.org/2000/svg" width="680" height="250" '
           'viewBox="0 0 680 250"><rect width="680" height="250" fill="#ffffff"/>'
           '%s</svg>' % "".join(o))
    return (svg,
            "Hình 5.%d · %s" % (n, cvi),
            "Figure 5.%d · %s" % (n, cen),
            avi, aen)


for _n in (1, 2):
    if not hasattr(F, "fig_f%02d" % _n):
        setattr(F, "fig_f%02d" % _n, (lambda _n=_n: _standalone_fig(_n)))


# ------------------------------------------------------------------- prose
def section(lang):
    b = []

    # ---------------------------------------------------------------- 5.1
    H(b, lang, "5.1 Giới thiệu", "5.1 Introduction")

    P(b, lang,
      "Hệ thống thu thập dữ liệu (DAS) thu thập dữ liệu hiện trường lấy trực "
      "tiếp từ các bộ chuyển đổi đo ở dạng tương tự (dòng điện, điện áp, điện "
      "trở, điện dung, tần số, v.v.). Vì tín hiệu trình bày chuẩn cho mọi biến "
      "công nghệ là tín hiệu điện ở mức 4 đến 20 mA một chiều, nên các tín "
      "hiệu đầu ra từ bộ chuyển đổi phải đi qua bộ điều hòa tín hiệu. Bộ điều "
      "hòa tín hiệu biến đổi các tín hiệu đầu vào này về dạng chuẩn nhờ tuyến "
      "tính hóa, lọc, v.v. (các phép toán phi tuyến), và nhờ khuếch đại, các "
      "phép toán đại số, chuyển đổi, v.v. (các phép toán tuyến tính). Vì việc "
      "thu thập dữ liệu về bản chất là thao tác trên máy tính, các tín hiệu "
      "đầu vào ở dạng tương tự chuẩn được biến đổi sang dạng số để tương "
      "thích với máy tính. Dữ liệu này được máy tính lưu trữ để phân tích "
      "thêm khi cần.",
      "A data acquisition system collects field data available directly from "
      "the measurement transducers in analogue form, that is, in current, "
      "voltage, resistance, capacitance, frequency, and so on. Since the "
      "standard representation signal for all the process variables is "
      "electrical, at the level of 4 to 20 mA D.C., the inputs available from "
      "the transducers have to pass through a signal conditioning unit. The "
      "signal conditioning unit transforms these input signals into the "
      "standard form by linearization, filtering, etc. (non-linear "
      "operations) and by amplification, algebraic operations, conversion, "
      "etc. (linear operations). Since data acquisition is essentially a "
      "computer-based operation, the input signals available in standard "
      "analogue form are transformed into digital form to make them "
      "compatible with the computer. These data are stored by the computer "
      "for further analysis as and when required.")

    P(b, lang,
      "Hệ thống đang được thảo luận ở đây về bản chất chỉ giới hạn ở việc thu "
      "thập. Điều này có nghĩa là không có tác động điều khiển thêm các biến "
      "công nghệ từ các thiết bị ngoại vi của máy tính. Nhưng hiện nay thiết "
      "kế hệ thống đã được cải tiến để bao gồm cả các công việc giám sát do "
      "máy tính khởi xướng. Hệ thống mới này được gọi là hệ thống SCADA (giám "
      "sát và thu thập dữ liệu). Tuy nhiên, chúng ta chỉ giới hạn phần trình "
      "bày ở việc thu thập dữ liệu. Hình 5.1 cho thấy các thành phần của hệ "
      "thống thu thập dữ liệu dưới dạng các khối lắp ghép.",
      "The system under discussion is essentially restricted to acquisition "
      "only. This means there is no further action to control the process "
      "variables from the computer peripherals. But nowadays system design "
      "has improved to include the supervisory jobs also to be initiated by "
      "the computer. The new system is named SCADA (supervisory control and "
      "data acquisition). However, we shall restrict our description up to "
      "data acquisition only. Figure 5.1 shows the components of a data "
      "acquisition system in assembled block form.")

    FIG(b, 1, F.fig_f01(), lang)

    P(b, lang,
      "Trước khi đi vào trình bày chi tiết từng thành phần của hệ thống thu "
      "thập dữ liệu hiện có, chúng ta cần xem xét hệ thống dùng cho việc thu "
      "thập dữ liệu từ trước. Thực tế, hệ thống trước đây được gọi là bộ ghi "
      "dữ liệu. Bộ ghi dữ liệu tiếp nhận tín hiệu từ các bộ chuyển đổi điện ở "
      "dạng chuẩn, tín hiệu từ cặp nhiệt điện và tín hiệu từ bộ chuyển đổi "
      "khí nén có dạng 0,2 đến 1,0 kg/cm². Vì phần lớn bộ chuyển đổi hiện "
      "trường thuộc loại khí nén, các tín hiệu khí nén nhận được vì thế phải "
      "được biến đổi về dạng chuẩn, tức là về dạng 4 đến 20 mA một chiều. Để "
      "làm được điều đó, các tín hiệu khí nén này ở dạng ban đầu được cho đi "
      "qua một bộ quét cơ khí (gọi là van scani), chuyển động theo đường tròn, "
      "từng bước một, với khoảng thời gian cố định theo thiết kế. Tất cả các "
      "đầu vào dạng khí nén, sau khi đi qua van scani từng cái một, trước hết "
      "được biến đổi thành tín hiệu điện (4 đến 20 mA một chiều) nhờ bộ "
      "chuyển đổi khí nén – điện. Tín hiệu sau đó được biến đổi sang dạng số "
      "rồi được ghi vào bộ nhớ của bộ xử lý. Trong hệ thống này, khoảng thời "
      "gian cố định cho bước chuyển động của van scani được tính bằng cách "
      "xét thời gian chọn một tín hiệu khí nén cụ thể, thời gian biến đổi "
      "tín hiệu đó sang dạng điện tương đương và sau đó sang dạng số. Chừng "
      "nào toàn bộ thao tác nêu trên chưa hoàn tất thì bước chuyển động tiếp "
      "theo của van scani bị ngăn không cho thực hiện. Trong một trường hợp "
      "cụ thể, nếu một tín hiệu khí nén không có mặt do lỗi ở bộ phát lắp tại "
      "hiện trường, van scani sẽ chuyển sang bước tiếp theo, được khởi động "
      "bởi mạch hẹn giờ. Các đầu vào khác như tín hiệu điện thông thường, tín "
      "hiệu cặp nhiệt điện, tín hiệu RTD, tín hiệu từ máy phân tích đều đến "
      "bộ ghép kênh sau khi đã được điều hòa thích hợp và cũng được ghi vào "
      "bộ nhớ của bộ xử lý.",
      "Before we go into the individual detailing of the different components "
      "of the existing data acquisition system, we must examine the system "
      "available earlier for data acquisition. In fact, the system available "
      "earlier was called a data logger. The data logger unit incorporated "
      "electrical transducer signals in standard form, thermocouple signals "
      "and pneumatic transducer signals in the form of 0.2 to 1.0 kg/cm². "
      "Since the majority of the field transducers were of the pneumatic "
      "type, the pneumatic signals received thus had to be transformed into "
      "the standard form, that is, into 4 to 20 mA D.C. For this, these "
      "pneumatic signals in their original form were passed through a "
      "mechanical scanner (called a scani valve) moving in circular motion "
      "in steps at a fixed interval as per the design. All the inputs "
      "available in pneumatic form, after passing through the scani valve "
      "one by one, were first converted into electrical signals (4 to 20 mA "
      "D.C.) by means of a pneumatic-to-electrical transducer. The signal was "
      "then converted into digital form and logged into the processor "
      "memory. In this system, the fixed interval for the step movement of "
      "the scani valve was calculated by taking into account the time of "
      "selection of one particular pneumatic signal, its conversion to an "
      "equivalent electrical form and then its conversion into digital form. "
      "Unless the entire operation described above was completed, the next "
      "step movement of the scani valve was restricted. In a particular "
      "event, if a pneumatic signal was not available owing to a fault in a "
      "field-mounted transmitter, the scani valve moved to the next step, "
      "initiated by a timer circuit. Other inputs such as normal electrical "
      "signals, thermocouple signals, RTD signals and analyzer signals all "
      "came to the multiplexing unit after proper signal conditioning and "
      "were similarly logged into the processor memory.")

    P(b, lang,
      "Dù thiết kế này có vẻ hơi đặc thù và khó vận hành, khó bảo trì, thiết "
      "bị này lại rất phổ biến trong các ngành công nghiệp quá trình cho đến "
      "năm 1980. Khi các bộ phát điện tử xuất hiện và được lắp đặt thay cho "
      "các bộ phát khí nén, thiết kế van scani trở nên lỗi thời và hệ thống "
      "mới dễ bảo trì hơn. Hệ thống ghi dữ liệu dùng bộ phát điện tử (Tx) "
      "được trình bày trong sơ đồ khối Hình 5.2. Theo sơ đồ này, các bộ phát "
      "lắp tại hiện trường tích hợp bộ điều hòa tín hiệu như một phần không "
      "tách rời, và các tín hiệu tương tự đến bộ ghép kênh đều ở dạng chuẩn. "
      "Sau đó các tín hiệu này được biến đổi sang dạng số nhờ bộ chuyển đổi "
      "A/D và được máy tính xử lý để lưu trữ phụ, để phát sinh các điều kiện "
      "báo động khác nhau và cũng để thu được bản in cứng của các hồ sơ "
      "khác nhau.",
      "Though it seems a rather typical design and difficult to operate and "
      "maintain, this equipment was very popular in process industries up to "
      "1980. Now, when electronic transmitters came into the picture and were "
      "installed in place of pneumatic ones, the scani-valve design became "
      "obsolete and the new system became easier to be maintained. A data "
      "logging system employing electronic transmitters (Tx) is presented in "
      "the block diagram Figure 5.2. In this scheme, the transmitters "
      "installed in the field incorporate the signal conditioning unit as an "
      "integral part and the analog signals received by the multiplexing unit "
      "are all in standard form. These are then converted into digital form "
      "by an A/D converter and then processed by the computer for auxiliary "
      "storage, for the generation of various alarm conditions and also for "
      "obtaining hard copies of different records.")

    FIG(b, 2, F.fig_f02(), lang)

    P(b, lang,
      "Vận hành hiệu quả của bất kỳ ngành công nghiệp nào hay của bất kỳ cơ sở "
      "sản xuất nào cũng liên quan đến nhiều biến công nghệ tác động đến "
      "thiết bị công nghệ theo cách này hay cách khác. Điều này là do các "
      "thiết bị công nghệ cần nhiều vòng điều khiển được thực hiện cẩn thận "
      "để giảm thiểu tương tác trực tiếp giữa các biến. Kiểu tương tác giữa "
      "các biến khác nhau như vậy cuối cùng ảnh hưởng đến độ ổn định của vòng "
      "điều khiển và đôi khi một số vòng điều khiển có thể mất hoàn toàn khả "
      "năng kiểm soát.",
      "The efficient operation of any process industry or any manufacturing "
      "establishment involves a number of process variables affecting the "
      "process unit one way or the other. This is because the process units "
      "need a number of control loops to be implemented carefully so that "
      "the direct interaction amongst variables can be minimized. This type "
      "of interaction amongst different variables ultimately affects the "
      "loop stability and sometimes some of the control loops can go "
      "completely out of control.")

    P(b, lang,
      "Trong hệ thống hiện đại, hệ thống thu thập dữ liệu kết hợp với nhiều "
      "vòng điều khiển độc lập giúp giảm tương tác và nâng cao hiệu năng tổng "
      "thể của quá trình vận hành. Điều này đạt được nhờ dùng máy tính số tốc "
      "độ cao. Hiện nay hầu hết các hệ thống thu thập dữ liệu đều dựa trên "
      "PC.",
      "In a modern system, which incorporates a data acquisition system along "
      "with various independent control loops, interaction is minimized and "
      "the overall performance of the operation is improved. This is achieved "
      "by the use of high-speed digital computers. Nowadays almost all data "
      "acquisition systems are PC based.")

    P(b, lang,
      "Một điểm quan trọng khác trong công nghiệp là sự hiện diện của bầu "
      "không khí nguy hiểm. Trong điều kiện bất thường, khu vực bên trong nhà "
      "máy trở nên nguy hiểm do rò rỉ khí dễ nổ hoặc hỗn hợp khí. Đối với khu "
      "vực như vậy, thực hành lắp đặt đòi hỏi phải có giao diện an toàn nội "
      "tại. Điều này cần dùng thêm rào an toàn điện tử giữa khu vực nguy "
      "hiểm và khu vực an toàn. Về mặt vật lý, các rào này có thể được lắp "
      "giữa các cọc đầu nối của bộ chuyển đổi (nằm trong tủ được lắp tại hiện "
      "trường gần quá trình) và tủ bộ điều hòa tín hiệu đặt bên trong phòng "
      "điều khiển. Nếu các bộ điều hòa tín hiệu là bộ phận tích hợp của tủ bộ "
      "chuyển đổi thì các rào nên được lắp gần bộ ghép kênh. Trong mọi "
      "trường hợp, vị trí của các rào phải nằm bên trong phòng điều khiển, "
      "tức là trong khu vực an toàn.",
      "One more important point in the process industry is the presence of a "
      "hazardous atmosphere. During abnormal conditions the area inside the "
      "process plants becomes hazardous owing to leakage of explosive gases "
      "or mixtures. For such an area, installation practices dictate "
      "provision of intrinsically safe interfacing. This necessitates the "
      "use of electronic safety barriers as well between the hazardous area "
      "and the safe area. Physically, these barriers can be installed between "
      "the transducer terminals, located inside the cabinet installed in the "
      "field near the process, and the signal conditioning unit cabinet "
      "located inside the control room. If the signal conditioning units are "
      "integral to the transducer cabinets, then the barriers should be "
      "installed near the multiplexing unit. In all the cases the location of "
      "the barriers shall be inside the control room, that is, inside the "
      "safe area.")

    P(b, lang,
      "Dựa trên các dữ kiện đã thảo luận, hệ thống thu thập dữ liệu về cơ bản "
      "gồm những thành phần sau:",
      "Based on the facts discussed so far, the data acquisition system "
      "includes essentially the following:")

    L(b, lang,
      ["(a) Các bộ chuyển đổi;",
       "(b) Các bộ điều hòa tín hiệu;",
       "(c) Các bộ ghép kênh;",
       "(d) Chuyển đổi dữ liệu (ADC và DAC);",
       "(e) Thiết bị hiển thị tại chỗ hoặc từ xa, lưu trữ, ghi báo động, v.v."],
      ["(a) Transducers",
       "(b) Signal conditioners",
       "(c) Multiplexers",
       "(d) Data conversion (ADC and DAC)",
       "(e) Local or remote display devices, storage, alarm logging, etc."])

    P(b, lang,
      "Vì phần mô tả về bộ chuyển đổi đã được trình bày trong chương trước, "
      "chúng ta sẽ không thảo luận thêm nữa. Chúng ta sẽ bắt đầu phần trình "
      "bày từ các bộ điều hòa tín hiệu.",
      "Since the description of transducers has been presented in an earlier "
      "chapter, we shall not discuss these any further. We shall start our "
      "description from signal conditioning units.")

    return b
