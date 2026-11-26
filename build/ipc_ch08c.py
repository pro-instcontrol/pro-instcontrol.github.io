# -*- coding: utf-8 -*-
"""Chapter 8, section 8.2.2 (continued) through 8.3 (EN/VI bilingual).

Source: Prasad, Jayaswal and Priye, *Instrumentation and Process Control*
(I.K. International, 2019), PDF pp. 359-363, printed pp. 347-351, decoded
text lines 13900-14166. Covers the tail of 8.2.2 PIA operation, all of
8.2.3 Isolation and Masking and 8.3 Microprocessor Based Programmable
Controller. Figures 8.7-8.14 are embedded in source order.

Printed wording anomalies ("Red Time Clock", "hexagonal address scheme",
"parellely") are retained verbatim in the English stream; the Vietnamese
stream follows the intended meaning. The `ipcfig8_b` supplier is authored
in parallel; until it is importable, non-overwriting fallbacks are installed
for figures 8.10-8.14.
"""

import ipcfig8 as F
from ipc_ch06_lib import H, P, L, E, FIG, TBL, NOTE, REFS


# ----------------------------------------------------------------- figures
def _stub_fig(n, en, vi):
    """Minimal labelled placeholder used only while the supplier is absent."""
    mid = "ipc8c%02d" % n
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
        'fill="#9aa7b8">Hinh 8.%d   ·   Figure 8.%d</text>'
        '</svg>' % (defs, en, n, n))
    return (svg,
            "Hình 8.%d · %s" % (n, vi),
            "Figure 8.%d · %s" % (n, en),
            vi, en)


for _n, _en, _vi in (
    (10, "High-voltage leakage minimization for thermocouple input",
     "Giam thieu don ro dien ap cao cho dau vao cap nhiet dien"),
    (11, "Process analyzer signal tapped from display instrument",
     "Tin hieu phan tich qua trinh duoc lay song song tu thiet bi hien thi"),
    (12, "4 to 20 mA current input through 62.5 ohm precision resistor",
     "Dong dau vao 4 den 20 mA qua dien tro chinh xac 62,5 om"),
    (13, "Seven-segment LED display with address decoder and output latch",
     "Man hinh LED bay doan voi bo giai ma dia chi va chot dau ra"),
    (14, "DAC interface to electro-pneumatic converter and control valve",
     "Giao tiep DAC voi bo chuyen doi dien-khi nen va van dieu khien"),
):
    if not hasattr(F, "fig_f%02d" % _n):
        setattr(F, "fig_f%02d" % _n,
                (lambda _n=_n, _en=_en, _vi=_vi: _stub_fig(_n, _en, _vi)))


# ------------------------------------------------------------------- prose
def section(lang):
    b = []

    # -------------------------------- 8.2.2 PIA operation (continued)
    P(b, lang,
      "Điều này bổ sung cho các tín hiệu đầu vào đến từ hiện trường, bao gồm "
      "cả tín hiệu biến quá trình lẫn các thông số khác liên quan đến tình "
      "trạng của chính các thiết bị (tình trạng của bộ phát, một thiết bị đầu "
      "vào, và tình trạng của phần tử điều khiển cuối, một thiết bị đầu ra).",
      "This is in addition to the inputs, which are coming from the field that "
      "includes process variable signals as well as other parameters related "
      "to health of the instruments themselves (Health of transmitter, an "
      "input device as well as health of final control element, an output "
      "device).")

    P(b, lang,
      "PIA là sự kết hợp giữa các thanh ghi lệnh/trạng thái và các thanh ghi "
      "dữ liệu. Đây là giao diện quan trọng giữa bộ xử lý chủ và thẻ giao "
      "diện I/O, thực chất là một bộ xử lý phụ do bộ xử lý chủ điều khiển. Sơ "
      "đồ được trình bày trong Hình 8.7. Hoạt động của các thanh ghi dữ liệu "
      "phụ thuộc vào chế độ hoạt động của PIA (đóng vai trò thiết bị đầu vào "
      "hay thiết bị đầu ra). Các tín hiệu lệnh từ máy tính chủ được các thanh "
      "ghi lệnh/trạng thái tiếp nhận, và trạng thái của PIA cũng được giám "
      "sát qua chính nhóm thanh ghi này. Để truyền dữ liệu, bộ xử lý chủ gửi "
      "lệnh tới các thanh ghi lệnh/trạng thái nhằm cấu hình PIA thành thiết "
      "bị đầu ra, sau đó truyền dữ liệu tới các thanh ghi dữ liệu trong khi "
      "theo dõi trạng thái xem dữ liệu đã được chấp nhận hay chưa. Mặt khác, "
      "để đọc dữ liệu, bộ xử lý chủ gửi lệnh tới các thanh ghi lệnh/trạng "
      "thái nhằm cấu hình PIA thành thiết bị đầu vào, rồi kiểm tra trạng thái "
      "sẵn có của dữ liệu và cuối cùng khởi lệnh đọc.",
      "The PIA is consisting of a combination of command/status registers as "
      "well as data registers. This is an important interface between the "
      "host processor and the I/O interface card which is in fact a slave "
      "processor controlled by the host processor. The scheme has been shown "
      "in Figure 8.7. The working of data registers depend upon the mode of "
      "operation of PIA (whether operating as input device or output device). "
      "Command signals from the host computer are received by the "
      "command/status registers and the status of the PIA is monitored by the "
      "same group of registers. For transferring data the host processor gives "
      "command to command/status registers to configure PIA as output device "
      "and then transfers data to the data registers while monitoring the "
      "status as to whether the data has been accepted or not. On the other "
      "hand, for reading the data, the host processor gives command to "
      "command/status registers to configure the PIA as input device and then "
      "checks the status of availability of data and finally initiates read "
      "operation.")

    FIG(b, 7, F.fig_f07(), lang)

    # ------------------------------------------------------------- 8.2.3
    H(b, lang, "8.2.3 Cô lập và che lọc",
      "8.2.3 Isolation and Masking")

    P(b, lang,
      "Tín hiệu số được dùng để điều khiển các cuộn điện từ mức thấp nhằm tạo "
      "ra các thao tác đóng cắt. Đồng thời, chúng cũng cần được cách ly với "
      "nhau do sự khác biệt về mức điện áp hoạt động. Điều này có thể thực "
      "hiện bằng cách dùng hệ thống rơ le dạng từ tính hoặc dạng quang. Cuộn "
      "điện từ mức thấp hoạt động tốt hơn khi dùng cách ly quang như trình "
      "bày trong Hình 8.8. Cách hoạt động rất đơn giản.",
      "Digital signals are used to operate low level solenoids for generating "
      "switching operations. At the same time, it needs isolation also, from "
      "each other because of difference in operating voltage level. This can "
      "be done by use of a relay system being of magnetic type or optical "
      "type. Low level solenoid is better operated by optical isolation as "
      "shown in Figure 8.8. The operation is simple.")

    P(b, lang,
      "Đầu vào số (DI) điều khiển điốt phát quang (điốt phát sáng hồng ngoại "
      "bằng arsenua gali), phát sáng ở tầng đầu vào và điều khiển bộ transitor "
      "quang N-P-N bằng silicon ở tầng đầu ra. Dòng nguồn đặt giữa cực thu và "
      "cực bazơ của hệ thống cảm biến được dùng để tạo dòng nhờ các tia tới "
      "chiếu vào bazơ. Dòng bazơ tỷ lệ trực tiếp với bức xạ phát ra từ điốt.",
      "The digital input (DI) drives the LED (Gallium Arsenide infrared light "
      "emitting diode) which emits light from it at input stage and operates "
      "the silicon N-P-N photo transistor at the output stage. The source "
      "current applied between collector and the base of the sensing system "
      "is used to generate current by incident rays on the base. The base "
      "current is directly proportional to the emitted radiation from the "
      "diode.")

    FIG(b, 8, F.fig_f08(), lang)

    P(b, lang,
      "Khi quá trình đang vận hành, một số cổng số của PIA có thể không còn "
      "liên quan và do đó cần được giữ ở trạng thái cách ly. Sự cách ly này "
      "chỉ mang tính tạm thời và được gọi là che lọc. Che lọc được thực hiện "
      "bằng cổng logic AND như trình bày trong Hình 8.9. Ở đây, bit dữ liệu "
      "được đưa qua phép AND với bit che lọc. Khi bit che lọc bằng 0, đầu ra "
      "sẽ bằng 0 hoặc có thể giữ giá trị trước đó theo như đã lập trình.",
      "While the process is in operation some digital ports of a PIA may not "
      "be relevant and therefore, are required to be kept isolated. Such "
      "isolation is of temporary nature and is called masking. Masking is "
      "implemented by means of AND logic gate as shown in Figure 8.9. Here "
      "the data bit is ANDed with the masking bit. When the masking bit is 0, "
      "the output becomes 0 or can otherwise retain its last value as "
      "programmed.")

    FIG(b, 9, F.fig_f09(), lang)

    H(b, lang, "(i) Giao tiếp với tín hiệu tương tự mức thấp",
      "(i) Interfacing of low-level analog signals", level=3)

    P(b, lang,
      "Các tín hiệu tương tự biến quá trình mức thấp gồm đầu ra milli-vôn của "
      "cặp nhiệt điện, các tổ hợp cầu đo của cảm biến biến dạng và RTD, cũng "
      "như tín hiệu từ các máy phân tích quá trình. Chúng ta sẽ thảo luận ở "
      "đây cả tín hiệu cặp nhiệt điện lẫn tín hiệu của máy phân tích.",
      "Low level process variable analog signals are comprising of millivolt "
      "output from thermocouples, strain gages RTD-bridge combinations and "
      "signals from process analysers as well. We shall discuss here "
      "thermocouple signals as well as analyzer signals.")

    P(b, lang,
      "Vì cặp nhiệt điện được lắp đặt vật lý trong vùng nhiệt độ cao, giá đỡ "
      "lắp đặt có thể trở nên dẫn điện ở nhiệt độ nâng cao. Ngoài ra còn có "
      "khả năng dò rò điện áp cao có thể truyền suốt đến giao diện ADC. Một "
      "sắp xếp gồm bộ lọc và điốt (đấu ngược chiều) như trình bày trong Hình "
      "8.10 giúp giảm thiểu sự dò rò điện áp cao và cải thiện chất lượng tín "
      "hiệu.",
      "Thermocouples, being installed physically in high temperature zone, "
      "the installation supports may become conductive at elevated "
      "temperature. Also there is possibility of high voltage leakage which "
      "can be transmitted all the way to ADC interfacing. A filter-cum-diode "
      "(oppositely connected) arrangement as shown in Figure 8.10 minimizes "
      "the high voltage leakage and improves the signal quality.")

    FIG(b, 10, F.fig_f10(), lang)

    P(b, lang,
      "Có thể thực hiện sắp xếp tương tự cho tín hiệu của máy phân tích quá "
      "trình, nhưng cách kết nối sẽ hơi khác. Đầu ra của máy phân tích không "
      "được nối trực tiếp mà được lấy song song từ hệ thống hiển thị hiện "
      "có. Phần còn lại của hệ thống vẫn giữ nguyên cách kết nối. Sắp xếp này "
      "được trình bày trong Hình 8.11. Việc này nhằm giảm thiểu ảnh hưởng của "
      "tải cảm biến do trở kháng nguồn rất cao của các máy phân tích.",
      "A similar arrangement can be done for process analyzer signal also but "
      "the system of connection shall be slightly different. The analyzer "
      "output shall not be connected directly but it will be tapped parallely "
      "from the existing display system. Rest of the system connection is "
      "same. The arrangement has been shown in Figure 8.11. This is done to "
      "minimize the effect of sensor loading due to very high source "
      "impedance of the analyzers.")

    FIG(b, 11, F.fig_f11(), lang)

    P(b, lang,
      "Tín hiệu đầu vào biến quá trình đo lường cũng như tín hiệu đầu ra điều "
      "khiển đều là tín hiệu mức thấp theo tiêu chuẩn dòng một chiều 4 đến 20 "
      "mA. Để giao tiếp các tín hiệu này với ADC hoặc với bộ vi điều khiển "
      "lập trình một trạm, chúng phải được chuyển sang dạng tín hiệu điện áp. "
      "Việc này được thực hiện bằng cách cho dòng tín hiệu đi qua điện trở "
      "chính xác 62,5 ôm như trình bày trong Hình 8.12.",
      "Process measurement variable input as well as control output signals "
      "are also low level signals comprising of 4 to 20 mAmps. D.C. standard. "
      "For interfacing these to ADC or to single station programmable "
      "microcontroller, these have to be converted to voltage signal form. "
      "This is done by passing the current signal through 62.5 ohm precision "
      "resistor as shown in Figure 8.12.")

    FIG(b, 12, F.fig_f12(), lang)

    H(b, lang, "(ii) Giao tiếp với hệ thống hiển thị",
      "(ii) Interfacing of display system", level=3)

    P(b, lang,
      "Như đã mô tả trước đó, giao tiếp với hệ thống hiển thị có thể thực "
      "hiện qua một cổng đầu ra có chốt kết hợp với bộ giải mã địa chỉ. Ở đây "
      "chúng ta xét một ví dụ đơn giản về giao tiếp với hệ thống hiển thị LED "
      "bảy đoạn như trình bày trong Hình 8.13.",
      "As described earlier, interfacing of display system can be made through "
      "an output latching port in combination with an address decoder. Here "
      "we consider a simple example of interfacing a seven segment LED display "
      "system as shown in Figure 8.13.")

    FIG(b, 13, F.fig_f13(), lang)

    P(b, lang,
      "Màn hình LED bảy đoạn cực dương chung được nối qua điện trở chính xác "
      "hạn dòng như trình bày trên hình. Trong hầu hết các trường hợp, dấu "
      "thập phân cũng được yêu cầu và có thể nối vào cổng D7; nếu không cần "
      "thì để hở. Trong kỹ thuật này, A0A1A2 là 3 trong số 8 đường địa chỉ, và "
      "5 đường còn lại (không thể hiện trong sơ đồ) là các đường kích hoạt "
      "khác. Địa chỉ giải mã đầu ra 11111110 được kết hợp với tín hiệu điều "
      "khiển IOW để tạo tín hiệu chọn I/O cần thiết.",
      "The common anode seven segment LED display has been connected through "
      "current limiting precision resistor as shown. In majority of the cases "
      "the decimal point is also required which can be connected to D7 port "
      "but if not required, it is left open. In this technique also A0A1A2 are "
      "3 out of 8 address lines and remaining 5 lines (not shown in the "
      "diagram) are different enabling lines. The decoded address output "
      "11111110 is combined with control signal IOW and the required I/O "
      "select signal is generated.")

    H(b, lang, "(iii) Giao tiếp đầu ra điều khiển với phần tử điều khiển cuối",
      "(iii) Interfacing of control output to final control elements", level=3)

    P(b, lang,
      "Giao tiếp đầu ra điều khiển với phần tử điều khiển cuối được thực hiện "
      "qua nhiều giai đoạn. Đầu ra điều khiển từ bộ điều khiển dựa trên vi xử "
      "lý về cơ bản ở dạng số. Trước hết, tín hiệu số này phải được chuyển đổi "
      "sang tín hiệu tương tự bằng bộ chuyển đổi số-tương tự (DAC). Đầu ra của "
      "DAC có thể ở dạng dòng điện hoặc dạng điện áp. Vì tín hiệu thiết bị đo "
      "yêu cầu ở dạng đầu ra dòng điện (4 đến 20 mA), DAC có đầu ra dòng điện "
      "có thể nối trực tiếp với bộ chuyển đổi điện-khí nén. Bộ chuyển đổi "
      "điện-khí nén biến dòng điện thành tín hiệu khí nén 0,2 đến 1,0 kg/cm² "
      "để vận hành phần tử điều khiển cuối (các van điều khiển khí nén) lắp "
      "trên đường ống dẫn quá trình. Mặt khác, nếu đầu ra của DAC ở dạng điện "
      "áp, cần dùng thêm một thiết bị khác gọi là bộ chuyển đổi điện áp-dòng "
      "điện. Sơ đồ chi tiết được trình bày trong Hình 8.14.",
      "Interfacing of control output to final control element is carried out "
      "through several stages. The control output from a microprocessor based "
      "controller is essentially in digital form. First of all, this digital "
      "signal has to be converted to analog signal output by means of "
      "digital-to-analog converter (DAC). The DAC output can be in current "
      "form as well as in voltage form. Since the instrumentation signal "
      "required is of current output form (4 to 20 mAmps), the DAC having "
      "current output can be directly connected to electro-pneumatic "
      "converter. The electro-pneumatic converter converts the current into "
      "0.2 to 1.0 kg/cm² pneumatic signal for operation of final control "
      "element (the pneumatically operated control valves) installed in the "
      "process flow line. If, on the other hand, the DAC output happens to be "
      "in voltage form, another instrument called voltage to current converter "
      "also is to be employed. The detailed diagram has been shown in Figure "
      "8.14.")

    P(b, lang,
      "Đầu ra của bộ giải mã địa chỉ kết hợp với đường điều khiển IOW sẽ kích "
      "hoạt khối chốt. Các bit dữ liệu đi tới DAC và sau khi chuyển đổi (xét "
      "đầu ra dòng điện từ DAC), dòng đầu ra được gửi tới bộ chuyển đổi "
      "điện-khí nén. Bộ này biến dòng điện thành dạng khí nén (0,2 đến 1,0 "
      "kg/cm²), cuối cùng vận hành van điều khiển khí nén (phần tử điều khiển "
      "cuối) lắp trên đường ống dẫn quá trình.",
      "The output of address decoder in combination with IOW control line "
      "enables the latch unit. The data bits go to DAC and after conversion "
      "(considering current output from the DAC) the current output is sent to "
      "electro-pneumatic converter. The electro-pneumatic converter converts "
      "the current into pneumatic form (0.2 to 1.0 kg/cm²) which ultimately "
      "operates the pneumatic control valve (the final control element) "
      "installed in the process flow line.")

    FIG(b, 14, F.fig_f14(), lang)

    # --------------------------------------------------------------- 8.3
    H(b, lang, "8.3 Bộ điều khiển lập trình dựa trên vi xử lý",
      "8.3 MICROPROCESSOR BASED PROGRAMMABLE CONTROLLER")

    P(b, lang,
      "Thiết bị này nói ngắn gọn cũng được gọi là bộ vi điều khiển, vì được "
      "cấu hình quanh vi xử lý 8 bit và được tích hợp bộ nhớ cùng hệ thống I/O "
      "trên cùng một chip mạch tích hợp. Bộ vi điều khiển liên lạc qua bàn phím "
      "ASCII (thiết bị đầu vào) cũng như qua thiết bị hiển thị LCD (thiết bị "
      "đầu ra). Ngoài ra, nó còn có thể được nối với PC (máy tính cá nhân) để "
      "nạp hoặc tải chương trình và cho các chức năng truyền thông khác. Các "
      "phần cứng sau đây có thể thấy trong hầu hết mọi bộ vi điều khiển:",
      "This equipment in short is called microcontroller as well because it "
      "has been configured around 8-bit microprocessor and has been "
      "integrated with memory and I/O system on the same IC chip. The "
      "microcontroller communicates through ASCII keyboard (input unit) as "
      "well as through LCD display device (output unit). In addition to the "
      "above, it can also be connected to PC (personal computer) for uploading "
      "or downloading of programs and also for other communication functions. "
      "The following hardware can be found in almost all micro-controllers:")

    L(b, lang,
      ["CPU 8 bit (mạch dao động và mạch xung nhịp ngay trên vi mạch)",
       "EPROM 64 byte (cũng có thể mở rộng thêm)",
       "RAM 8 đến 32 kbyte",
       "48 đường I/O",
       "Cổng nối tiếp EIA RS-232C",
       "Bộ đếm thời gian/đếm sự kiện 16 bit (ba bộ)",
       "Giao diện đồng hồ thời gian thực",
       "ADC và DAC",
       "Rơ le có tiếp điểm NO và NC",
       "Hệ thống đầu vào cách ly quang (nếu cần)",
       "Hệ thống hiển thị LCD",
       "Bàn phím ASCII đa năng",
       "Hệ thống nguồn"],
      ["8-bit CPU (oscillator and clock circuit on chip)",
       "64 bytes EPROM (further expandable as well)",
       "8 to 32 kbytes RAM",
       "48 I/O lines",
       "Serial Port EIA RS-232C",
       "16 bits timer/counters (three in numbers)",
       "Real Time clock interface",
       "ADC and DAC",
       "Relay having NO and NC contacts",
       "Optically isolated input system (if required)",
       "LCD Display system",
       "General purpose ASCII keyboard",
       "Power supply system"])

    P(b, lang,
      "Bộ vi điều khiển thường vận hành ở tần số thạch anh 20 MHz, với mạch "
      "dao động và mạch xung nhịp ngay trên vi mạch. Vi mạch vi điều khiển có "
      "khả năng định địa chỉ ít nhất 64 Kbyte bộ nhớ dữ liệu và bộ nhớ chương "
      "trình bên ngoài, mỗi loại như vậy. Mạch xung nhịp cũng nằm trên vi mạch "
      "và được vận hành bằng đầu vào thạch anh 20 MHz. Xung nhịp cho phần còn "
      "lại của mạch điều khiển được cung cấp bởi một mạch hai thao tác. Bộ nhớ "
      "sẵn có cho vi điều khiển ở dạng EPROM và RAM. Một phần của RAM (theo sơ "
      "đồ địa chỉ thập lục phân do nhà sản xuất cung cấp) cũng được dự phòng "
      "bằng pin để lưu chương trình khi mất điện.",
      "The microcontroller normally operates at crystal frequency of 20 MHz "
      "having on chip oscillator and clock circuitry. The microcontroller IC "
      "chip is capable of addressing at least 64 Kbytes of external data as "
      "well as program memory each. The clock circuit is also on chip and is "
      "operated by crystal input at 20 MHz. Clock pulse for rest of the "
      "controller circuitry is provided by a two-operation circuit. Memory "
      "available for the microcontroller is in EPROM and RAM form. A portion "
      "of the RAM (hexagonal address scheme to be provided by the "
      "manufacturer) is battery backed as well in order to save the program "
      "in the event of power failure.")

    P(b, lang,
      "Một thành phần I/O lập trình đa năng dùng để giao tiếp thiết bị ngoại "
      "vi với bus hệ thống, gọi là Giao diện ngoại vi lập trình (PPI), cung "
      "cấp khả năng lập trình cần thiết cho bộ vi điều khiển. Chức năng của "
      "PPI được lập trình bằng phần mềm hệ thống, do đó không cần thiết bị "
      "logic bên ngoài. Tuy nhiên, nó có thể dùng với bất kỳ loại bộ điều "
      "khiển dựa trên vi xử lý nào. PPI có ba cổng I/O, mỗi cổng 8 đường (cổng "
      "A, cổng B và cổng C). Cổng C được chia thành hai cổng con, mỗi cổng 4 "
      "đường (gọi là Cu và Cl). Bất kỳ tổ hợp I/O nào của cổng A, B, Cu, Cl "
      "cũng có thể được cấu hình bằng lệnh phần mềm. Địa chỉ cổng phải do nhà "
      "sản xuất cung cấp. Ngoài ra, PPI còn có thể dùng để giao tiếp ADC và "
      "thiết bị hiển thị LED bảy đoạn. Thực tế, kỹ thuật giao tiếp dùng PPI "
      "được xem là vượt trội hơn các phương pháp đã nêu trước đó trong chương "
      "này.",
      "A general-purpose programmable I/O component for interfacing, the "
      "peripheral equipment to the system bus, called Programmable Peripheral "
      "Interface (PPI) provides the necessary programmability to the "
      "microcontroller. The functionality of PPI is system-software programmed "
      "and therefore, no external logic device is required. This can be used "
      "with any type of microprocessor based controller however. This is "
      "having three I/O ports of 8 lines each (port A, port B and port C). "
      "Port C is grouped into two sub-ports having 4 lines each (named Cu and "
      "Cl). Any I/O combination of port A, B, Cu, Cl can be configured by the "
      "software command. The port addresses have to be supplied by the "
      "manufacturer. In addition to the above, the PPI can be used for "
      "interfacing ADC and seven segment LED display devices as well. In fact "
      "the interfacing technique using PPI is considered to be superior to "
      "the methods suggested earlier in this chapter.")

    P(b, lang,
      "Bộ đếm thời gian/khoảng lập trình PIT/C là một thiết bị quan trọng "
      "khác, đặc biệt được dùng cho các chức năng điều khiển quá trình. Ví "
      "dụ, các chức năng trễ thời gian, tạo tốc độ, đếm sự kiện, nhân tốc độ ở "
      "định dạng nhị phân, v.v. được thực hiện rất hiệu quả thông qua điều "
      "khiển phần mềm nhờ PIT/C.",
      "The programmable interval timer/counter PIT/C is another important "
      "equipment which is used for process control functions especially. For "
      "instance, implementation of time delay functions, rate generation, "
      "event counting, rate multiplication in binary format, etc. are done "
      "through software control very effectively by means of PIT/C.")

    P(b, lang,
      "Việc nạp chương trình từ bộ điều khiển lên hệ thống hỗ trợ/sao lưu bổ "
      "sung dựa trên PC, hoặc tải bất kỳ chương trình nào từ PC xuống bộ điều "
      "khiển, được thực hiện bằng cách nối PC qua giao diện nối tiếp EIA "
      "RS-232C sẵn có thông qua lệnh phần mềm thích hợp đi kèm hệ thống. Giao "
      "diện EIA RS-232C được hiện thực qua UART (Bộ thu/phát không đồng bộ đa "
      "năng). Đây là giao diện truyền thông lập trình được, dùng làm thiết bị "
      "ngoại vi để thực hiện lệnh. Thiết bị này biến dữ liệu song song từ CPU "
      "thành dạng nối tiếp để truyền đi, đồng thời chuyển dữ liệu nối tiếp "
      "nhận được thành dữ liệu song song để CPU tiếp nhận. Tuy nhiên, kết nối "
      "PC như vậy phải thực hiện qua phần mềm giả lập thiết bị đầu cuối, ví dụ "
      "XTALK có sẵn trên thị trường. Việc cài đặt gói XTALK được tiến hành "
      "theo thủ tục cài đặt thông thường.",
      "Uploading of a program from the controller to an additional PC-based "
      "support/back-up system or downloading of any program from the PC to the "
      "controller is done by connecting the PC by means of available serial "
      "interface EIA RS-232C through appropriate software command available "
      "with the system. The EIA RS-232C interface is implemented through UART "
      "(Universal Asynchronous Receiver/Transmitter). This is a programmable "
      "communication interface used as peripheral device for command execution "
      "as well. This device transforms the parallel data from CPU to serial "
      "form for transmission and also transfers the received serial data into "
      "parallel data to be accepted by the CPU. Such connection of PC is, "
      "however, to be done through a terminal emulator software, e.g. XTALK "
      "which is easily available. The installation of XTALK package is done "
      "through usual installation procedure.")

    P(b, lang,
      "Một bộ điều khiển quá trình cần hiển thị ngày và giờ trên bảng mặt "
      "trước cùng với số thẻ, giá trị quá trình và giá trị cài đặt. Những điều "
      "này được thực hiện nhờ Đồng hồ thời gian thực (RTC) hoạt động bằng mạch "
      "dao động thạch anh ở tần số cụ thể giữa 32 và 33 KHz. RTC cũng có tính "
      "năng ngắt, nhờ đó có thể thực hiện rất hiệu quả việc xử lý hoặc giám "
      "sát một dữ liệu điều khiển cụ thể trong các thao tác điều khiển quá "
      "trình.",
      "A process controller needs date and time also to be displayed on the "
      "front panel alongwith tag number, process value and set value figures. "
      "These are accomplished by a Red Time Clock (RTC) which is operated by a "
      "crystal oscillator at a particular frequency between 32 and 33 KHz. "
      "Interrupt facility is also available with the RTC by the help of which "
      "a particular control data processing or monitoring can be accomplished "
      "very effectively in process control operations.")

    P(b, lang,
      "Bộ chuyển đổi ADC tám kênh (dựa trên CMOS đơn khối, thời gian chuyển đổi "
      "đến 100 microgiây) có đầu ra 8 bit được giao tiếp phù hợp qua bộ giải "
      "mã địa chỉ. Thông qua ADC, bộ điều khiển được nối trực tiếp với Cổng "
      "tín hiệu đầu vào tương tự. Một DAC 8 bit có đầu ra dòng điện với thời "
      "gian ổn định 100 nanogiây được nối với đầu ra của bộ điều khiển. Do đó, "
      "bộ điều khiển cho ra trực tiếp đầu ra điều khiển ở dạng dòng tương tự "
      "để vận hành phần tử điều khiển cuối. Vì giao tiếp DAC được ánh xạ bộ "
      "nhớ, bất kỳ phép toán toán học hoặc logic nào cũng có thể thực hiện "
      "trực tiếp trên dữ liệu đầu ra. Các phép toán đó gồm hành động điều "
      "khiển tách (để vận hành hai phần tử điều khiển cuối nối song song), "
      "nhân tín hiệu đầu ra tương tự với một hằng số (để vận hành van đóng-ngắt "
      "tác động nhanh công suất lớn được thiết kế riêng). Bất kỳ kiểu xử lý "
      "nào khác trên tín hiệu đầu ra cũng có thể thực hiện rất hiệu quả và "
      "thuận tiện.",
      "An eight-channel ADC (monolithic CMOS based, conversion time upto 100 "
      "microsecond) having eight-bit output is suitably interfaced through "
      "address decoder. Through the ADC, the controller is directly connected "
      "to Analog Input Signal Port. An eight-bit DAC, having current output "
      "with settling time of 100 nanosecond is connected to the controller "
      "output. Therefore, the controller gives out control output directly in "
      "analog current form for operation of final control element. Since the "
      "DAC interfacing is memory mapped, any mathematical or logical operation "
      "can be performed directly on the output data. Such operations include "
      "split control action (for operating two parellely connected final "
      "control elements), multiplication of analog output signal by a constant "
      "(for operation of especially designed high capacity quick-acting "
      "ON-OFF valve). Any other type of manipulation on the output signal can "
      "also be carried out very effectively and conveniently.")

    P(b, lang,
      "Đối với các thao tác báo động dựa trên sự bất thường của biến quá trình, "
      "hai tiếp điểm NO/NC, một tiếp điểm thường mở và tiếp điểm kia thường "
      "đóng, được bố trí trên bo mạch đầu ra của bộ điều khiển. Hệ thống "
      "còi/báo động hiện có cũng có thể được nối với các tiếp điểm đầu ra rơ "
      "le sẵn có nếu cần.",
      "For alarm operations which are based on abnormalities on process "
      "variables, two NO/NC contacts, one normally open and the other one "
      "normally closed are provided on the controller output board. The "
      "existing alarm/hooter system can also be hooked up with the available "
      "relay output contacts if so desired.")

    return b
