# -*- coding: utf-8 -*-
"""Chapter 8, section 8.2 "Interface System Techniques" with 8.2.1
(Interfacing of Instrumentation Units) and the start of 8.2.2 (PIA operation).

Source: Prasad, Jayaswal and Priye, *Instrumentation and Process Control*
(I.K. International, 2019), PDF pp. 355-359, printed pp. 343-347, decoded
text lines 13718-13929. Figures 8.3-8.6 are embedded in printed order.

The `ipcfig8_a` supplier registers fig_f01 ... fig_f09.  Small genuine
non-overwriting fallbacks are installed only for the four figures this
section embeds, in case that supplier is still being written in parallel.
"""

import ipcfig8 as F
from ipc_ch06_lib import H, P, L, E, FIG, TBL, NOTE, REFS


# ----------------------------------------------------------------- figures
def _stub(n):
    """Minimal valid 5-tuple fallback for one printed diagram."""
    svg = ('<svg viewBox="0 0 680 250" xmlns="http://www.w3.org/2000/svg">'
           '<text x="340" y="120" text-anchor="middle" font-size="12">'
           'Figure 8.%d</text></svg>' % n)
    return (svg,
            "Hình 8.%d · Sơ đồ giao tiếp" % n,
            "Figure 8.%d · Interface diagram" % n,
            "Sơ đồ minh họa giao tiếp số tương tự và giải mã địa chỉ",
            "Schematic of the digital interface and address decoding")


for _n in (3, 4, 5, 6):
    if not hasattr(F, "fig_f%02d" % _n):
        setattr(F, "fig_f%02d" % _n, (lambda _n=_n: _stub(_n)))


# ------------------------------------------------------------------- prose
def section(lang):
    b = []

    # ---------------------------------------------------------------- 8.2
    H(b, lang, "8.2 Kỹ thuật giao tiếp hệ thống",
      "8.2 Interface System Techniques")

    P(b, lang,
      "Để một vi xử lý hoạt động thực tế một cách phối hợp, nhiều thiết bị "
      "hoặc công cụ hỗ trợ gọi là ngoại vi cần được giao tiếp. Yêu cầu về bộ "
      "nhớ ngoài phần được tích hợp trong chính vi xử lý (dưới dạng các thanh "
      "ghi) và các ngoại vi tương tự khác (bàn phím, màn hình, v.v.) giúp vi "
      "xử lý nói chung có thể hoạt động hữu ích không được xem xét ở đây. Ở "
      "đây chúng ta chủ yếu quan tâm đến việc giao tiếp các thiết bị đo biến "
      "số công nghệ. Trước khi đi vào điểm giao tiếp thực tế của I/O công "
      "nghệ, chúng ta sẽ xem xét khái niệm cơ bản của kỹ thuật giao tiếp.",
      "To make a microprocessor work practically in a co-ordinated manner, "
      "many supporting equipment or devices called peripherals are to be "
      "interfaced. Memory requirement other than that integrated with the "
      "microprocessor itself (in the form of registers) and similar other "
      "peripherals (keyboard, monitor, etc.) which makes the microprocessor "
      "generally operable in useful ways are not being considered here for "
      "discussion. Here we are mainly interested in interfacing the process "
      "variable instrumentation units. Before we come to the point of actual "
      "interfacing of process I/O, we shall see the basic concept of "
      "interfacing techniques.")

    P(b, lang,
      "Khái niệm cơ bản trong việc giao tiếp bất kỳ thiết bị I/O nào với vi "
      "xử lý phụ thuộc vào tập lệnh được dùng cho các phép truyền dữ liệu. "
      "Việc giao tiếp thiết bị I/O có thể là ánh xạ I/O hoặc ánh xạ bộ nhớ. "
      "Nhìn chung, sơ đồ ánh xạ I/O vượt trội hơn sơ đồ ánh xạ bộ nhớ. Sơ đồ "
      "ánh xạ I/O dùng địa chỉ 8 bit để nhận diện thiết bị cụ thể và chỉ hai "
      "lệnh được dùng cho phép truyền dữ liệu, đó là IN và OUT. Phần cứng cần "
      "thiết cho cách triển khai này ít hơn. Mặt khác, giao tiếp I/O ánh xạ "
      "bộ nhớ dùng địa chỉ 16 bit để nhận diện thiết bị và nhiều lệnh được "
      "yêu cầu để thực hiện hoạt động truyền dữ liệu. Độ phức tạp phần cứng "
      "lớn hơn trong hệ thống này. Ưu điểm duy nhất của sơ đồ này là các phép "
      "toán toán học cũng như logic có thể được thực hiện trực tiếp trên dữ "
      "liệu I/O. Tuy nhiên, đặc tính này không có trong sơ đồ ánh xạ I/O do "
      "số lượng phần cứng hạn chế.",
      "Basic concept behind interfacing any I/O device with a microprocessor "
      "depends upon the set of instructions that have been used for data "
      "transfer operations. Interfacing of I/O devices can be I/O mapped or "
      "memory mapped. In general, I/O mapped scheme is superior to that of "
      "memory mapped. The I/O mapped scheme has 8 bit address to identify the "
      "particular device and only two instructions are used for data transfer "
      "operation, i.e. IN and OUT. Less hardware is required for carrying out "
      "such an implementation. On the other hand, memory-mapped I/O "
      "interfacing uses 16 bits address for identifying the device and many "
      "instructions are required for effecting the data transfer activity. "
      "Hardware complications are more in this system. Only advantage with "
      "this scheme is that the mathematical as well as logical operations can "
      "be done directly on the I/O data. This feature, however, is not "
      "available with I/O mapped scheme due to limited number of hardware.")

    P(b, lang,
      "Nhìn chung, trong hệ thống đo, tất cả thiết bị I/O đều được giao tiếp "
      "với vi xử lý theo kỹ thuật ánh xạ I/O. Lệnh IN đưa dữ liệu từ thiết bị "
      "vào bộ tích lũy. Lệnh OUT gửi nội dung của bộ tích lũy ra khỏi vi xử lý "
      "để xử lý tiếp. Tập lệnh hai byte dùng trong thao tác này cho cả IN lẫn "
      "OUT gồm một byte mã lệnh và byte còn lại là địa chỉ cổng.",
      "In general, in instrumentation system all I/O devices are interfaced "
      "with the microprocessor on I/O mapped techniques. The IN instruction "
      "inputs the data from input devices into the accumulator. The OUT "
      "instruction sends the contents of the accumulator out of the "
      "microprocessor for further processing. The two byte instruction set "
      "used in this operation for IN as well as OUT comprises one byte of "
      "opcode and the other byte for port address.")

    P(b, lang,
      "Giao tiếp I/O trước hết yêu cầu giải mã địa chỉ. Nhiều phương pháp có "
      "thể dùng cho mục đích này, nhưng phương pháp phổ biến nhất là giải mã "
      "bằng bộ giải mã 3 trên 8 như thể hiện trong Hình 8.3.",
      "I/O interfacing requires first decoding of the address. Many methods "
      "are available for this purpose, but the most popular method is "
      "decoding by 3-to-8 decoder as shown in Figure 8.3.")
    FIG(b, 3, F.fig_f03(), lang)

    P(b, lang,
      "Ở đây, 3 trong 8 đường địa chỉ A2 A1 A0 được đưa vào mạch giải mã, "
      "trong khi 5 đường còn lại A7A6A5A4A3 là tín hiệu cho phép của bộ giải "
      "mã. Chúng có thể tạo địa chỉ cho 8 thiết bị I/O khác nhau. Trong sơ "
      "đồ, O6 (11111110) với sự trợ giúp của đường điều khiển IOW chọn cổng ra "
      "chốt, còn O7 (11111111) với sự trợ giúp của IOR chọn cổng vào đệm.",
      "Here 3 out of 8 address lines A2 A1 A0 are input to the decoder circuit "
      "whereas remaining A7A6A5A4A3 (5 numbers) are enabling signals for the "
      "decoder. These can generate address for 8 different I/O devices. In the "
      "diagram, O6 (11111110) with the help of IOW control line selects output "
      "latching port and O7 (11111111) with the help of IOR select input "
      "buffer port.")

    # -------------------------------------------------------------- 8.2.1
    H(b, lang, "8.2.1 Giao tiếp các thiết bị đo",
      "8.2.1 Interfacing of Instrumentation Units", level=3)

    H(b, lang, "(i) Giao tiếp bộ chuyển đổi",
      "(i) Interfacing of transducers", level=4)

    P(b, lang,
      "Một bộ chuyển đổi trong sơ đồ đo có thể chỉ có tín hiệu tương tự làm "
      "đầu ra, hoặc có cả tín hiệu tương tự lẫn tín hiệu số chồng lên nhau "
      "cùng chạy trên một dây. Việc tạo ra đầu ra tín hiệu kép như vậy là có "
      "thể với các bộ chuyển đổi thông minh. Vì các ứng dụng vi xử lý chỉ "
      "chấp nhận tín hiệu số, tín hiệu kép cung cấp tín hiệu đo ở dạng đầu ra "
      "số trực tiếp và do đó có thể giao tiếp khá thuận tiện với vi xử lý. "
      "Tuy nhiên, các bộ chuyển đổi chỉ tạo tín hiệu đầu ra dạng tương tự "
      "không thể giao tiếp trực tiếp. Việc giao tiếp này phải được thực hiện "
      "thông qua bộ chuyển đổi tương tự sang số (ADC). Ngoài ra, một bộ "
      "chuyển đổi có thể có nhiều dạng mức tín hiệu biến số công nghệ khác, "
      "ví dụ: 0 đến 10 volt; 0,25 đến 1,25 volt; 4 đến 20 mA; milivolt từ cặp "
      "nhiệt điện hoặc đầu dò nhiệt độ điện trở (RTD); miliampe từ nhiệt trở, "
      "milivolt hoặc microvolt từ máy phân tích công nghệ và một số dạng "
      "khác. Để đưa tất cả các dạng tín hiệu đo biến số công nghệ nêu trên về "
      "dạng điện áp nhằm tương thích với việc nối vào cổng vào của ADC, có "
      "thể cần dùng bộ khuếch đại phù hợp. Riêng tín hiệu 4 đến 20 mA (là tín "
      "hiệu biến số công nghệ tiêu chuẩn công nghiệp) có thể chuyển đổi rất "
      "dễ dàng thành tín hiệu điện áp 0,25 đến 1,25 volt bằng cách cho dòng "
      "điện đi qua điện trở chính xác 62,5 ohm.",
      "A transducer under an instrumentation scheme can have analog signal "
      "alone as output or analog as well as digital signals both superimposed "
      "upon each other running upon the same wire. Generation of such dual "
      "signal output is possible with application of smart transducers. Since "
      "the microprocessor applications accept digital signal only, dual "
      "signalling provides measurement signal in the form of digital output "
      "directly and therefore, can be interfaced quite conveniently to the "
      "microprocessors. But the transducers generating output signals in the "
      "form of analog only cannot be interfaced directly. This interfacing "
      "shall be done, however, through an analog-to-digital converter (ADC). "
      "In addition to this, a transducer can have varieties of other process "
      "variable signal levels e.g., 0 to 10 volt; 0.25 to 1.25 volt; 4 to 20 "
      "mAmps; millivolt from Thermocouples or resistance temperature detectors "
      "(RTD); milliampere from thermistors, millivolt or microvolt from process "
      "analyzers and several others. To put all the above forms of process "
      "variable instrumentation signals into voltage form for making them "
      "compatible for connection to input port of an ADC, suitable amplifiers "
      "may also have to be used. As far as 4 to 20 mAmps signal is concerned "
      "(which constitutes industry standard process variable signal), it can "
      "be converted into voltage signal very easily in the form of 0.25 to "
      "1.25 volt by passing the current signal through a 62.5 ohm precision "
      "resistor.")

    P(b, lang,
      "Giao tiếp của ADC thực chất rất quan trọng và có thể được triển khai "
      "theo hai cách khác nhau:",
      "Interfacing of an ADC in fact is important and can be implemented in "
      "two different ways:")
    L(b, lang,
      ["Giao tiếp dùng thăm dò", "Giao tiếp dùng ngắt"],
      ["Interfacing using polling", "Interfacing using interrupts"],
      ordered=True)

    P(b, lang,
      "Sơ đồ đơn giản hóa trong Hình 8.4 cho thấy kỹ thuật giao tiếp ADC theo "
      "phương pháp thăm dò. ADC có một đường vào tương tự và 8 đường ra cho "
      "đầu ra số được nối tới vi xử lý. Tín hiệu vào tương tự có dạng điện áp. "
      "Có hai đường điều khiển: tín hiệu khởi động (ST) và tín hiệu sẵn sàng "
      "dữ liệu (DR). Quá trình chuyển đổi được khởi động bằng cách phát xung "
      "ST và vô hiệu hóa bộ đệm đầu ra ba trạng thái. Việc hoàn tất chuyển "
      "đổi được kiểm tra bằng thăm dò. Khi quá trình chuyển đổi hoàn tất, DR "
      "trở nên hoạt động.",
      "The simplified diagram on Figure 8.4 shows an interfacing technique "
      "for ADC using polling method. The ADC has one analog input line and 8 "
      "output lines for digital output to be connected to the microprocessor. "
      "The analog input signal is in the form of voltage. There are two "
      "control lines: START (ST) and DATA READY DR. Conversion is started by "
      "initiating the START pulse and disabling the tri-state output buffer. "
      "Completion of conversion is verified by polling. When the conversion "
      "is completed, DATA READY comes alive.")

    P(b, lang,
      "Bộ giải mã địa chỉ tạo ra ba địa chỉ 1, 2 và 3. Đường địa chỉ 3 phát "
      "xung ST. Khi chuyển đổi bắt đầu, đường DR, tức là tín hiệu sẵn sàng dữ "
      "liệu, được theo dõi qua một trong các đầu ra số D0 thông qua bộ đệm ba "
      "trạng thái và đường địa chỉ 1 như trong sơ đồ. Khi DR được kích hoạt, "
      "dữ liệu được đưa ra đường đầu ra và vi xử lý có thể đọc dữ liệu bằng "
      "cách kích hoạt đường địa chỉ 2.",
      "The address decoder creates three addresses 1, 2 and 3. The address "
      "line 3 sends START pulse. When the conversion starts, DR, i.e. DATA "
      "READY line is monitored by one of the digital outputs D0 through a "
      "tri-state buffer and address line 1 as shown on the diagram. When the "
      "DR is activated, the data is put on the output line and microprocessor "
      "can read the data by the activation of address line 2.")
    FIG(b, 4, F.fig_f04(), lang)

    P(b, lang,
      "Kỹ thuật giao tiếp ADC dùng ngắt đã được thể hiện trong sơ đồ đơn giản "
      "hóa của Hình 8.5.",
      "Interfacing technique for ADC using interrupt has been shown on the "
      "simplified diagram in Figure 8.5.")

    P(b, lang,
      "Trong trường hợp này, tín hiệu vào tương tự cũng có dạng điện áp với "
      "các nối thông thường. ADC được điều khiển bằng xung nhịp trong khoảng "
      "100 KHz đến 800 KHz, có thể là ngoài hoặc trong. Có ba tín hiệu điều "
      "khiển tích hợp sẵn, ví dụ WR (ghi); RD (đọc) và CS (chọn chip).",
      "In this case also, the analog input signal is in the form of voltage "
      "having usual connections. The ADC is clock driven between 100 KHz and "
      "800 KHz which can be any of the two: external or internal. There are "
      "three numbers of built-in control signals, e.g. WR (Write); RD (Read) "
      "and CS (Chip select).")
    FIG(b, 5, F.fig_f05(), lang)

    P(b, lang,
      "Khi WR lên mức cao, quá trình chuyển đổi bắt đầu. Khi chuyển đổi hoàn "
      "tất, tín hiệu ngắt xuống mức thấp và dữ liệu có sẵn trên đường đầu ra. "
      "Đường ngắt đi tới vi xử lý để khởi phát ngắt, cho phép vi xử lý đọc dữ "
      "liệu.",
      "When WR goes high, conversion starts. On completion of conversion "
      "interrupt goes low and the data becomes available at the output line. "
      "The interrupt line goes to microprocessor to initiate the interruption "
      "for enabling the microprocessor to read the data.")

    # -------------------------------------------------------------- 8.2.2
    H(b, lang, "8.2.2 Hoạt động của PIA (Bộ giao tiếp song song)",
      "8.2.2 PIA (Parallel Interface Adaptors) Operation", level=3)

    P(b, lang,
      "Như đã thảo luận ở phần trước, trong đo dựa trên vi xử lý, giao tiếp "
      "số nói chung là ánh xạ I/O, phương pháp giao tiếp kia là ánh xạ bộ nhớ "
      "nhưng không được dùng phổ biến. Trong sơ đồ đo công nghệ, thiết bị I/O "
      "có thể là một trong ba loại hoặc tổ hợp của cả ba, ví dụ chuyên dùng "
      "cho vào và/hoặc ra riêng biệt hoặc có thể cấu hình cho cả hai. Ví dụ "
      "về thiết bị vào chuyên dụng là cặp nhiệt điện, công cụ đo biến dạng, "
      "đầu dò nhiệt độ điện trở (RTD), nhiệt trở, đầu vào tiếp điểm hở hoặc "
      "đóng, v.v. Sự xuống cấp hoặc hỏng hóc của chúng có thể được biết ngay "
      "qua tình trạng đầu ra không đủ hoặc mạch hở hoặc mạch đóng. Ví dụ về "
      "thiết bị ra chuyên dụng là các tiếp điểm trường hở để cắt thiết bị "
      "điện hoặc bất kỳ phần tử điều khiển cuối nào khác, ví dụ van điều khiển "
      "khí nén do cơ cấu điện từ vận hành; thiết bị do động cơ bước vận hành "
      "và các thiết bị liên quan đến an toàn khác. Ví dụ về thiết bị I/O có "
      "thể cấu hình cho cả hai là bộ chuyển đổi thông minh và phần tử điều "
      "khiển cuối ghép lại với nhau. Các thiết bị này được cấu hình từ phòng "
      "điều khiển trung tâm bằng hệ thống cấu hình dựa trên PC, cũng như từ "
      "bộ cấu hình cầm tay (phổ dụng hoặc chuyên dụng) để sắp xếp lại, kiểm "
      "tra hiệu chuẩn lại và thậm chí khắc phục sự cố. Một sơ đồ đơn giản của "
      "hệ thống như vậy đã được thể hiện trong Hình 8.6.",
      "As we have discussed earlier, in microprocessor based instrumentation, "
      "the digital interfacing is in general I/O mapped, the other interfacing "
      "method being memory mapped but not in common use. In process "
      "instrumentation scheme, I/O devices can be any one or a combination of "
      "all three e.g. dedicated to input and/or output separately or "
      "configurable to both. Examples of dedicated input devices are "
      "thermocouples, strain gages, resistance temperature detectors (RTD), "
      "thermistors, open or close contact inputs, etc. Their deterioration or "
      "failure can at once be known in terms of insufficient output or open "
      "circuit or closed circuit conditions. Examples of dedicated output "
      "devices are open field contacts to TRIP the electrical equipment or any "
      "other final control elements, e.g. solenoid operated pneumatic control "
      "valves; stepper motor operated equipment and other safety related "
      "equipment. Examples of I/O devices which can be configured for both "
      "are smart transducers and final control elements put together. These "
      "instruments are configured from central control room by means of a "
      "PC-based configurable system as well as from hand-held configuration "
      "(Universal or Dedicated) for rearranging, recalibration checking and "
      "even troubleshooting. A simple scheme of such system has been shown in "
      "Figure 8.6.")
    FIG(b, 6, F.fig_f06(), lang)

    P(b, lang,
      "Điều này bổ sung cho các đầu vào đến từ hiện trường, bao gồm các tín "
      "hiệu biến số công nghệ cũng như các thông số khác liên quan đến tình "
      "trạng hoạt động của chính các thiết bị (tình trạng của bộ phát, một "
      "thiết bị vào, cũng như tình trạng của phần tử điều khiển cuối, một "
      "thiết bị ra).",
      "This is in addition to the inputs, which are coming from the field that "
      "includes process variable signals as well as other parameters related "
      "to health of the instruments themselves (Health of transmitter, an "
      "input device as well as health of final control element, an output "
      "device).")

    P(b, lang,
      "PIA gồm sự kết hợp của các thanh ghi lệnh/trạng thái cũng như các "
      "thanh ghi dữ liệu. Đây là một giao tiếp quan trọng giữa bộ xử lý chủ và "
      "thẻ giao tiếp I/O, thực chất là một bộ xử lý phụ do bộ xử lý chủ điều "
      "khiển. Sơ đồ đã được thể hiện trong Hình 8.7. Hoạt động của các thanh "
      "ghi dữ liệu phụ thuộc vào chế độ hoạt động của PIA (làm thiết bị vào "
      "hay thiết bị ra). Tín hiệu lệnh từ máy tính chủ được các thanh ghi "
      "lệnh/trạng thái nhận và trạng thái của PIA được giám sát bởi cùng nhóm "
      "thanh ghi đó. Để truyền dữ liệu, bộ xử lý chủ đưa lệnh tới các thanh "
      "ghi lệnh/trạng thái để cấu hình PIA thành thiết bị ra, sau đó truyền "
      "dữ liệu tới các thanh ghi dữ liệu trong khi giám sát trạng thái xem dữ "
      "liệu đã được chấp nhận hay chưa. Mặt khác, để đọc dữ liệu, bộ xử lý "
      "chủ đưa lệnh tới các thanh ghi lệnh/trạng thái để cấu hình PIA thành "
      "thiết bị vào, rồi kiểm tra trạng thái sẵn có của dữ liệu và cuối cùng "
      "khởi phát thao tác đọc.",
      "The PIA is consisting of a combination of command/status registers as "
      "well as data registers. This is an important interface between the host "
      "processor and the I/O interface card which is in fact a slave processor "
      "controlled by the host processor. The scheme has been shown in Figure "
      "8.7. The working of data registers depend upon the mode of operation of "
      "PIA (whether operating as input device or output device). Command "
      "signals from the host computer are received by the command/status "
      "registers and the status of the PIA is monitored by the same group of "
      "registers. For transferring data the host processor gives command to "
      "command/status registers to configure PIA as output device and then "
      "transfers data to the data registers while monitoring the status as to "
      "whether the data has been accepted or not. On the other hand, for "
      "reading the data, the host processor gives command to command/status "
      "registers to configure the PIA as input device and then checks the "
      "status of availability of data and finally initiates read operation.")

    P(b, lang,
      "Trong Hình 8.7, bộ xử lý chủ được nối bằng bus tới giao tiếp PIA và tới "
      "thẻ giao tiếp I/O rời rạc và tương tự; thẻ này lại nối tới các đường "
      "I/O rời rạc và I/O tương tự.",
      "In Figure 8.7, the host processor is linked by a bus to the PIA "
      "interface and to the discrete and analog I/O interface card, which in "
      "turn connects to the discrete I/O and analog I/O lines.")

    return b
