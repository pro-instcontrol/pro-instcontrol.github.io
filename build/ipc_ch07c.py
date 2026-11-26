# -*- coding: utf-8 -*-
"""Chapter 7, section 7.2 (continued) through 7.3.1 opening (EN/VI bilingual).

Source: Prasad, Jayaswal and Priye, *Instrumentation and Process Control*
(I.K. International, 2019), PDF pp. 337-341, printed pp. 325-329, decoded
text lines 13051-13256. Covers the tail of the X-Y plotter discussion,
7.2.1 Multifunction Programmable Recorder, 7.2.2 Modern Ink-Pen-Chart
Recorder, 7.2.3 Paperless Recording System, and the opening of 7.3 with
Figure 7.16. Printed wording anomalies ("especialty", "softwave",
"with respective to") are retained verbatim in the English stream.

Figures 7.12-7.16 are embedded in source order. The `ipcfig7_b` supplier
is authored in parallel; until it is importable, small non-overwriting
fallbacks are installed for exactly those five figures.
"""

import ipcfig7 as F
from ipc_ch06_lib import H, P, L, E, FIG, TBL, NOTE, REFS


# ----------------------------------------------------------------- figures
def _stub_fig(n, en, vi):
    """Minimal labelled placeholder used only while the supplier is absent."""
    mid = "ipc7c%02d" % n
    defs = ('<defs><marker id="%s" viewBox="0 0 8 8" refX="7" refY="4" '
            'markerWidth="6" markerHeight="6" orient="auto">'
            '<path d="M0 0 L8 4 L0 8 z" fill="#1f3a5f"/></marker></defs>' % mid)
    svg = (
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 680 250" '
        'width="680" height="250">%s'
        '<rect x="90" y="65" width="500" height="120" fill="#eef3fb" '
        'stroke="#1f3a5f" stroke-width="1.2"/>'
        '<path d="M90 100 L590 100 M90 150 L590 150" fill="none" '
        'stroke="#c8d4e4" stroke-width="0.8"/>'
        '<text x="340" y="136" text-anchor="middle" font-size="11" '
        'fill="#1f3a5f">%s</text>'
        '<text x="340" y="244" text-anchor="middle" font-size="6.4" '
        'fill="#9aa7b8">Hinh 7.%d   ·   Figure 7.%d</text>'
        '</svg>' % (defs, en, n, n))
    return (svg,
            "Hình 7.%d · %s" % (n, vi),
            "Figure 7.%d · %s" % (n, en),
            vi, en)


for _n, _en, _vi in (
    (12, "Multifunction programmable recorder", "Máy ghi lập trình đa năng"),
    (13, "Ultrasonic pen-position sensing", "Cảm biến vị trí bút siêu âm"),
    (14, "High-voltage solid-state input scanner", "Bộ quét đầu vào trạng thái rắn cao áp"),
    (15, "Paperless recording system", "Hệ thống ghi không dùng giấy"),
    (16, "Measurement, display and control devices", "Thiết bị đo, hiển thị và điều khiển"),
):
    if not hasattr(F, "fig_f%02d" % _n):
        setattr(F, "fig_f%02d" % _n,
                (lambda _n=_n, _en=_en, _vi=_vi: _stub_fig(_n, _en, _vi)))


# ------------------------------------------------------------------- prose
def section(lang):
    b = []

    # ------------------------------------------- X-Y plotter (continued)
    P(b, lang,
      "Sau khi được điều chỉnh điều kiện thích hợp, cả hai đầu vào được đưa "
      "đến các mạch cân bằng tương ứng, tại đây một điện áp sai số được tạo ra "
      "khi so sánh tín hiệu đầu vào với nguồn chuẩn được cấp riêng tới mạch cân "
      "bằng như hình vẽ. Các tín hiệu đầu ra thu được từ hệ thống cân bằng "
      "được chuyển sang dòng xoay chiều (A.C.), rồi sau khi khuếch đại được "
      "đưa tới các động cơ servo tương ứng; các động cơ này cuối cùng điều "
      "khiển hoạt động của máy ghi đồng thời cân bằng cả hệ thống. Các đầu vào "
      "tương ứng được ghi đồng thời trên giấy biểu đồ miễn là còn có sự biến "
      "đổi của các đầu vào; nhờ đó thu được bản ghi của một biến theo biến kia. "
      "Độ chính xác và độ nhạy của máy vẽ X-Y lần lượt là ± 0,3% và "
      "10 microvolt/milimet.",
      "Both the input after proper conditioning are fed to their respective "
      "balancing circuits where an error voltage is generated on comparison of "
      "input signal with respect to the standard supply fed separately to the "
      "balancing circuit as shown. The output signals obtained from balancing "
      "system are converted to A.C. and then after amplification are fed to the "
      "respective servomotors which ultimately control the recorder functioning "
      "and balancing of the system as well. The respective input are recorded on "
      "the chart paper simultaneously as long as there are variations in the "
      "inputs and thus a record of one variable with respective to another "
      "variable is obtained. The accuracy and sensitivity of X-Y plotter are "
      "± 0.3% and 10 microvolt/millimetre respectively.")

    P(b, lang,
      "Máy ghi này cũng được dùng để xác định quan hệ ứng suất-biến dạng khi "
      "thử nghiệm độ bền của vật liệu trong phòng thí nghiệm cơ khí. Nó cũng "
      "được dùng để vẽ đồ thị sự thay đổi điện trở theo sự thay đổi của nhiệt "
      "độ trong phòng thí nghiệm đo lường, hoặc thậm chí để vẽ đồ thị sự thay "
      "đổi điện áp đầu ra tính bằng milli-vôn của cặp nhiệt điện theo sự thay "
      "đổi nhiệt độ.",
      "This recorder is utilized for obtaining of stress-strain relationship as "
      "well while testing strength of material in mechanical laboratory. Also "
      "this is utilized for obtaining a graph of change in resistance versus "
      "change in temperature in instrumentation laboratory or even for obtaining "
      "a graph of change in milli-volt output of thermocouple with respect to "
      "change in temperature.")

    # --------------------------------------------------------------- 7.2.1
    H(b, lang, "7.2.1 Máy ghi lập trình đa năng",
      "7.2.1 Multifunction Programmable Recorder")

    P(b, lang,
      "Từ khi ra đời, các máy ghi công nghiệp truyền thống chủ yếu được dùng "
      "để giám sát và ghi lại dữ liệu quá trình thu được từ các cảm biến tại "
      "hiện trường.",
      "Conventional industrial recorders since their inception have been used "
      "primarily for monitoring and recording process data obtained from the "
      "field transducers.")

    P(b, lang,
      "Để khai thác thêm thông tin mà nếu thiếu có thể trở nên quan trọng và "
      "có giá trị, các máy ghi dữ liệu cần phải thông minh, phải có khả năng "
      "xử lý thông tin tiên tiến và hỗ trợ các giao thức truyền thông dữ liệu "
      "phù hợp. Điều này đòi hỏi một mạng dữ liệu liền mạch giữa các địa điểm "
      "đo lường và điều khiển khác nhau, ví dụ: hiện trường (nơi lắp đặt cảm "
      "biến), trạm điều khiển cục bộ (nơi đặt các điểm đầu cuối I/O), phòng "
      "điều khiển trung tâm (nơi lắp đặt máy ghi, thiết bị tạo tín hiệu điều "
      "khiển và các trạm người vận hành dựa trên PC), cũng như các văn phòng "
      "MIS (Hệ thống Thông tin Quản lý) khác nhau nơi đưa ra các quyết định "
      "quản lý.",
      "In order to extract more information that may otherwise prove to be "
      "critical and valuable, data recorders need to be intelligent, should "
      "have advanced information processing capabilities and should support "
      "appropriate data communication protocols. This requires seamless data "
      "networking amongst various instrumentation sites, e.g. field (where "
      "transducers are installed), local control station (where I/O termination "
      "points are located), central control room (where recorders and control "
      "generation instruments as well as PC-based operator stations are "
      "installed) and the various MIS (Management Information System) offices "
      "where management decisions are taken.")

    P(b, lang,
      "Hệ thống ghi dữ liệu cho phép truy cập các bản ghi từ bất kỳ nơi nào "
      "trên thế giới qua internet. Dạng ghi có thể là ghi bằng bút mực trên "
      "giấy biểu đồ hoặc ghi không dùng giấy. Cả hai loại máy ghi đều có khả "
      "năng hiển thị xu hướng theo thời gian thực, giá trị tức thời dưới dạng "
      "số và xu hướng dưới dạng biểu đồ cột. Ngoài ra, các máy ghi này còn "
      "hiển thị dữ liệu, thời gian, số kênh, trạng thái các điểm báo động, v.v. "
      "Một hệ thống hoàn chỉnh được trình bày trong Hình 7.12.",
      "Data recording system allows accessing of records from anywhere in the "
      "world through internet. The type of recording can be either on "
      "ink-pen-chart recording or a paperless recording. Both the recorders are "
      "capable of displaying real time trend, instantaneous value in digital "
      "form, trend in bar-graph form. In addition to these, these recorders "
      "display data, time, channel number, alarm points status, etc. A complete "
      "system has been shown in Figure 7.12.")

    FIG(b, 12, F.fig_f12(), lang)

    # --------------------------------------------------------------- 7.2.2
    H(b, lang, "7.2.2 Máy ghi giấy biểu đồ bằng bút mực hiện đại",
      "7.2.2 Modern Ink-Pen-Chart Recorder")

    P(b, lang,
      "So với các dạng máy ghi giấy biểu đồ bằng bút mực khác, máy ghi hiện "
      "đại có nhiều tính năng đặc biệt. Ngoài việc cung cấp đồng thời màn hình "
      "hiển thị tương tự và số, máy có thể được lập trình cho bất kỳ đầu vào "
      "nào (dải đầu vào phổ dụng) và cho bất kỳ bốn cấu hình tạo báo động nào "
      "trong số sáu cấu hình sẵn có của hệ thống (thấp, cao, rất thấp, rất "
      "cao, tốc độ thay đổi thấp và tốc độ thay đổi cao). Thẻ nhớ được lắp để "
      "lưu dữ liệu hiệu chuẩn và các dữ liệu thiết lập khác đã nhập vào hệ "
      "thống. Các phép toán toán học theo thời gian thực cũng được thực hiện "
      "cho mọi tính toán liên quan, và kết quả được ghi lại theo các khoảng "
      "được lập trình sẵn hoặc được truyền đến các địa điểm đã quy định thông "
      "qua kết nối mạng.",
      "In comparison to other forms of ink-pen-chart recorders, the modern "
      "recorders have many special features. In addition to provide "
      "simultaneous analog and digital displays, it can be programmed for any "
      "input (universal input ranging) and for any four-alarm generating "
      "settings out of six being available in the system (low, high, very low, "
      "very high, low rate of change and high rate of change). Memory cards are "
      "attached to save calibration data and other set-up data entered into the "
      "system. Real time mathematical operations also are done for any related "
      "calculations and results are recorded at programmed intervals or are "
      "communicated to described locations through network connectivity.")

    P(b, lang,
      "Hầu hết các tính năng đặc biệt của máy ghi hiện đại đều là thế mạnh "
      "riêng của từng nhà sản xuất, dựa trên công nghệ ASIC (mạch tích hợp "
      "chuyên dụng). Ví dụ, bộ khuếch đại với khả năng lập trình hệ số khuếch "
      "đại và bộ chuyển đổi tương tự-số được kết hợp trên cùng một chip. Ngoài "
      "ra, các tiếp điểm dây trượt được thay bằng thiết bị cảm biến vị trí bút "
      "siêu âm. Trong hệ thống này, vị trí của bút ghi được cảm biến thông qua "
      "hệ thống định thời xung siêu âm. Một bộ chuyển đổi áp điện thông qua "
      "phần tử từ giảo thực hiện nhiệm vụ đó, như trình bày đơn giản trong "
      "Hình 7.13.",
      "Most of the special features of a modern recorder are the especialty of "
      "the manufacturers, based on their ASIC (application specific integrated "
      "circuits) technology. For example, the amplifier unit with gain "
      "programming facilities and analog-to-digital converter are combined "
      "together on a single chip. Also the slide-wire contacts are replaced by "
      "ultrasonic pen position sensing device. In this system, the position of "
      "recorder pen is sensed through ultrasonic pulse timing system. A "
      "piezoelectric transducer through a magnetostrictive element do the job "
      "as shown in Figure 7.13 in a simplified way.")

    FIG(b, 13, F.fig_f13(), lang)

    P(b, lang,
      "Một đặc điểm nữa là thiết kế động cơ servo một chiều (D.C.) không chổi "
      "than. Sự trượt liên tục của giá bút gây mòn cơ học, dẫn đến hỏng động "
      "cơ servo. Tuy nhiên, trong thiết kế không chổi than, các cuộn dây được "
      "cố định và nam châm được phép quay, còn việc đóng cắt dòng điện qua "
      "cuộn dây được thực hiện bằng điện tử; trong khi đó, ở máy ghi truyền "
      "thống, nguồn dòng cần thiết được cấp qua chổi than.",
      "Another feature is the design of brushless D.C. servomotor. Sliding of "
      "pen carriage continuously creates mechanical wear resulting in "
      "servomotor failure. In the brushless design, however, the coils are "
      "fixed and the magnets are allowed to turn and switching of current "
      "through the coil is carried out electronically whereas the required "
      "current supply is done through brushes in conventional recorders.")

    P(b, lang,
      "Trong máy ghi hiện đại, việc quét đầu vào để ghi được thực hiện thông "
      "qua rơ le bán dẫn thiết kế đặc biệt. Việc quét đầu vào cho hệ thống máy "
      "ghi đa điểm thực sự đòi hỏi kỹ thuật riêng. Ở máy ghi truyền thống, "
      "điều này được thực hiện bằng công tắc vi mô chọn tín hiệu do một động "
      "cơ chọn tín hiệu vận hành liên tục. Khi công tắc vi mô này được tác "
      "động bởi một đầu vào cụ thể, toàn bộ cơ chế chấm điểm và in được cấp "
      "điện, dẫn đến việc ghi lại đầu vào đó. Tuy nhiên, ở máy ghi hiện đại, "
      "người ta dùng bộ quét trạng thái rắn chuyên dụng cao áp. Một bộ ghép "
      "quang có đầu ra dạng điện áp và một MOSFET hoạt động ở điện áp cao "
      "(vài kilovôn, với dòng rò cỡ vài nanoampe) kết hợp với nhau để đóng "
      "vai trò bộ quét đầu vào, như trình bày đơn giản trong Hình 7.14.",
      "In modern recorder scanning of input for recording is carried out "
      "through especially designed semiconductor relay. Scanning of input for "
      "a multi-point recorder system really needs techniques. In conventional "
      "recorder, it is done through signal selector microswitch operated "
      "continuously by a signal selector motor. When this micro-switch is "
      "operated upon by a particular input, entire dotting and printing "
      "mechanism is energized resulting in recording of that particular input. "
      "In modern recorder, however, application specific high voltage "
      "solid-state scanner is used. A photo coupler having output in voltage "
      "form and a high voltage operated MOSFET (a few kilovolt and leakage "
      "current of the order of a few nanoampere) combine together to work as "
      "input scanner as shown in Figure 7.14 in a simplified way.")

    FIG(b, 14, F.fig_f14(), lang)

    # --------------------------------------------------------------- 7.2.3
    H(b, lang, "7.2.3 Hệ thống ghi không dùng giấy",
      "7.2.3 Paperless Recording System")

    P(b, lang,
      "Các hệ thống ghi không dùng giấy không sử dụng giấy biểu đồ. Thực tế, "
      "toàn bộ bản ghi đều có sẵn trên màn hình giám sát. Các kênh đầu vào đi "
      "qua các mạch điều chỉnh tín hiệu thông thường, gồm bộ khuếch đại và bộ "
      "chuyển đổi tương tự-số, sau đó được ghi vào ngân hàng nhớ. Hệ thống "
      "được điều khiển bởi mạch điều khiển ghi như trình bày trong Hình 7.15. "
      "Toàn bộ ngân hàng nhớ được dùng để ghi các đầu vào đa kênh. Các đầu vào "
      "tương tự, thường ở dạng điện áp, được lấy mẫu với tốc độ rất cao để "
      "khớp với khoảng cách của dạng sóng của các biến công nghệ cần ghi. Dạng "
      "sóng của từng biến công nghệ được lấy mẫu theo cách này được lưu nguyên "
      "vẹn trong ngân hàng nhớ, sau đó có thể sao chép sang các thiết bị khác. "
      "Một thiết bị điều khiển đầu ra được bổ sung vào hệ thống để chọn loại "
      "đầu ra (tương tự hoặc số) thông qua bộ chuyển đổi thích hợp.",
      "The paperless recording systems do not use chart. In fact the entire "
      "records are available on the monitor screen. The input channels are "
      "passed through usual signal conditioners including amplifiers and "
      "analog-to-digital converters and then are recorded on memory bank. The "
      "system is controlled by recording control circuit as shown in Figure "
      "7.15. The entire memory bank are used for multi-channel input recording. "
      "The analog inputs usually in the form of voltage are sampled at very "
      "high sampling rate to match the interval of waveshape of the process "
      "variables to be recorded. The waveshape of the individual process "
      "variables sampled in this way is stored as it is in the memory bank and "
      "then can be copied to other instruments. An output controlling device "
      "is added to the system to select the type of output (analog or digital) "
      "through appropriate converter.")

    FIG(b, 15, F.fig_f15(), lang)

    P(b, lang,
      "Màn hình giám sát và các hệ thống truyền thông kết nối không được thể "
      "hiện trên sơ đồ. Màn hình là loại màn hình thông thường, có khả năng "
      "tạo ra các hình ảnh và đồ họa chân thực với sự trợ giúp của các gói "
      "phần mềm được thiết kế riêng cho mục đích này. Để xây dựng màn hình "
      "giám sát, có thể dễ dàng dùng phần mềm tạo dựng (chạy trên Microsoft "
      "Power Point). Ở chiều ngược lại, phần mềm thời gian chạy sẽ hiển thị "
      "tất cả đồ họa và các nội dung khác khi được khởi động. Đầu nối Ethernet "
      "được sử dụng thuận tiện cho hệ thống này.",
      "Monitor and the connected communication systems have not been shown on "
      "the diagram. The monitor is a conventional monitor having capability of "
      "creating realistic images and graphics with the help of especially "
      "designed software packages for the purpose. To construct the monitoring "
      "screen a builder softwave (which runs on Microsoft Power Point) can be "
      "easily used. The runtime software, on the other hand, shall display all "
      "the graphics and others when it is started. Ethernet connectors are used "
      "for this system easily.")

    # ------------------------------------------------- 7.3 / 7.3.1 opening
    H(b, lang, "7.3 Thiết bị hiển thị dữ liệu số",
      "7.3 DIGITAL DATA DISPLAY DEVICES")

    H(b, lang, "7.3.1 Giới thiệu", "7.3.1 Introduction", level=3)

    P(b, lang,
      "Chúng ta biết rằng một hệ thống đo lường kín về cơ bản gồm các thiết bị "
      "đo, thiết bị hiển thị và thiết bị điều khiển, như thể hiện trong sơ đồ "
      "khối của Hình 7.16. Phạm vi của thiết bị hiển thị khá rộng; tuy nhiên, "
      "trong phần thảo luận này chúng ta chỉ quan tâm đến các hệ thống hiển "
      "thị số. Điều đó có nghĩa là các dạng hiển thị khác, chẳng hạn thiết bị "
      "chỉ thị tương tự và máy ghi, tạm thời nằm ngoài phạm vi thảo luận. Dù "
      "vậy, trong thảo luận này chúng ta đã thấy thiết bị hiển thị đa năng và "
      "rất nhiều hệ thống ghi khác nhau.",
      "We are aware that a closed instrumentation system is consisting of "
      "essentially measurement devices, display devices and control devices as "
      "indicated in the block diagram presentation of Figure 7.16. The scope of "
      "display devices is fairly large, however, in the present discussion we "
      "are concerned with digital display systems only. That means other forms "
      "of display systems such as analog indicators, recorders shall remain out "
      "of discussion for the time being. In this discussion, however, we have "
      "already seen the versatile display device and a great number of "
      "different recording systems.")

    FIG(b, 16, F.fig_f16(), lang)

    return b
