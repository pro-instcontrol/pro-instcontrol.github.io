# -*- coding: utf-8 -*-
"""Chapter 5, section 5.5.1 (EN/VI bilingual).

Source: Prasad, Jayaswal and Priye, *Instrumentation and Process Control*
(I.K. International, 2019), PDF pp. 266-275, printed pp. 254-263, decoded
text lines 10175-10580.  Covers the tail of section 5.5 (the two printed
R-2R ladder current-output expressions) followed by 5.5.1 "PC-based
Practical Data Acquisition System": hardware, software, communication
standards (RS-232, RS-422, RS-485, Ethernet, GPIB, CAN), the TransNet
design, application software packages and the distributed system, with
Figures 5.35-5.42.

The printed figures are images in the PDF and the text layer around them is
scrambled, so the page renders were consulted to confirm each figure's real
subject.  The `ipcfig5_d` supplier is authored in parallel; simple but
valid 5-tuple fallbacks are installed below only for figure numbers that are
not yet registered, and never replace a real supplier callable.
"""

# -*- coding: utf-8 -*-
import ipcfig5 as F
from ipc_ch05_lib import H, P, L, E, FIG, TBL, NOTE, REFS


# ----------------------------------------------------------------- figures
_STUB_LABELS = {
    35: ("PC-based DAQ architecture",
         "Kiến trúc hệ thống thu thập dữ liệu dựa trên PC"),
    36: ("RS-232 interface connector",
         "Đầu nối giao diện RS-232"),
    37: ("RS-422 four-wire connection",
         "Kết nối bốn dây RS-422"),
    38: ("RS-485 standard bus link",
         "Liên kết bus chuẩn RS-485"),
    39: ("Ethernet packet format",
         "Định dạng gói tin Ethernet"),
    40: ("CAN message frame",
         "Khung thông điệp CAN"),
    41: ("Twin-axial distributed DAQ network",
         "Mạng thu thập dữ liệu phân tán dùng cáp twin axial"),
    42: ("Two-wire RS-485 network with repeaters",
         "Mạng RS-485 hai dây có bộ lặp"),
}


def _stub(n):
    en, vi = _STUB_LABELS[n]
    svg = (
        '<svg xmlns="http://www.w3.org/2000/svg" width="680" height="250" '
        'viewBox="0 0 680 250"><rect width="680" height="250" '
        'fill="#ffffff"/><rect x="130" y="85" width="420" height="80" '
        'fill="#eef3fb" stroke="#1f3a5f" stroke-width="1.2"/>'
        '<text x="340" y="116" text-anchor="middle" font-size="13" '
        'fill="#1f3a5f">Figure 5.%d</text>'
        '<text x="340" y="141" text-anchor="middle" font-size="11" '
        'fill="#1f3a5f">%s</text>'
        '<text x="340" y="225" text-anchor="middle" font-size="8" '
        'fill="#888888">Hinh 5.%d / Figure 5.%d</text></svg>'
        % (n, en, n, n))
    return (svg,
            "Hình 5.%d · %s" % (n, vi),
            "Figure 5.%d · %s" % (n, en),
            vi, en)


for _n in range(35, 43):
    if not hasattr(F, "fig_f%02d" % _n):
        setattr(F, "fig_f%02d" % _n, (lambda _n=_n: _stub(_n)))


# ------------------------------------------------------------------- prose
def section(lang):
    b = []

    # ------------------------------------------- tail of section 5.5 (R-2R)
    H(b, lang, "Phần tiếp theo của 5.5: các biểu thức dòng đầu ra",
      "Continuation of 5.5: the output-current expressions")

    P(b, lang,
      "Các nút của mạng thang R-2R có thể chia một dòng tham chiếu thành các "
      "mức nhị phân có trọng số. Hình 5.34 trình bày cách bố trí đó, với dòng "
      "tham chiếu 2 mA được áp vào và cho sự phân bố dòng như thể hiện trên "
      "hình. Với hệ thống chuyển đổi 4 bit, dòng đầu ra Iout được cho bởi:",
      "The nodes of the R-2R ladder can divide a reference current into "
      "weighted binary levels. Figure 5.34 shows such an arrangement, in "
      "which a reference current of 2 milliamperes is applied, resulting in "
      "the current distribution indicated in the diagram. For the four-bit "
      "conversion system, the current output Iout is given by:")

    E(b, lang, "Iout = (Iref/2)[D₃ + 2⁻¹D₂ + 2⁻²D₁ + 2⁻³D₀]",
      "Iout = (Iref/2)[D₃ + 2⁻¹D₂ + 2⁻²D₁ + 2⁻³D₀]", num="")

    P(b, lang,
      "Biểu thức tổng quát cho dòng đầu ra Iout có thể được mở rộng thành:",
      "The general expression for the output current Iout can be extended as:")

    E(b, lang, "Iout = (Iref/2)[Dₙ₋₁ + 2⁻¹Dₙ₋₂ + … + 2⁻⁽ⁿ⁻¹⁾D₀]",
      "Iout = (Iref/2)[Dₙ₋₁ + 2⁻¹Dₙ₋₂ + … + 2⁻⁽ⁿ⁻¹⁾D₀]", num="")

    P(b, lang,
      "Mạch cơ bản có thể được cải tiến bằng cách thêm một bộ khuếch đại "
      "thuật toán, trong đó các công tắc nối đến điện áp tham chiếu khi đầu "
      "vào nhị phân là 1 và nối đến đất khi đầu vào nhị phân là 0. Đầu ra của "
      "bộ khuếch đại ở dạng tương tự.",
      "The basic circuit can be improved by adding an operational amplifier, "
      "in which the switches connect to the reference voltage for a binary "
      "input of 1 and to ground for a binary input of 0. The amplifier output "
      "is in analog form.")

    # -------------------------------------------------------------- 5.5.1
    H(b, lang, "5.5.1 Hệ thống thu thập dữ liệu thực tế dựa trên PC",
      "5.5.1 PC-based Practical Data Acquisition System")

    P(b, lang,
      "Hệ thống thu thập dữ liệu (DAS) thực tế dựa trên PC thực hiện các "
      "thao tác ghi dữ liệu thời gian thực thông qua một giao thức truyền "
      "thông phù hợp như Ethernet, RS-232C, RS-422, RS-485 hoặc GP-IB. "
      "Mô-đun đầu vào phổ dụng hoàn thành các chức năng quét/ghép kênh và "
      "chuyển đổi tương tự-số trong mỗi 500 mili-giây đối với hệ thống 300 "
      "kênh. Tín hiệu đầu vào bao gồm mọi loại tín hiệu có trong bất kỳ ngành "
      "công nghiệp nào. Ngoài ra, mô-đun báo động là tính năng thiết yếu, "
      "phát ra các tín hiệu báo động tiếp điểm theo điều kiện điểm đặt "
      "trước. Việc giám sát hệ thống cấp nguồn cho hệ thống thu thập dữ liệu "
      "được thực hiện bằng cách đo giá trị căn bậc hai trung bình (rms) của "
      "nguồn xoay chiều, công suất tác dụng, công suất biểu kiến, công suất "
      "phản kháng, tần số, hệ số công suất và góc pha. Chu kỳ cập nhật dữ "
      "liệu cho hệ thống cấp nguồn có thể tới 2 giây. Bên cạnh các thành "
      "phần khác, ba phần quan trọng nhất của hệ thống thu thập dữ liệu dựa "
      "trên PC là: (a) phần cứng, (b) phần mềm và (c) liên kết truyền thông.",
      "A practical PC-based data acquisition system (DAS) performs real-time "
      "data logging operations via a suitable communication protocol such as "
      "Ethernet, RS-232C, RS-422, RS-485 or GP-IB. The universal input module "
      "completes its functions of scanning/multiplexing and analog-to-digital "
      "conversion in every 500 milliseconds for a 300-channel system. The "
      "input signals include all types of signals present in any process "
      "industry. In addition, an alarm module is an essential feature, which "
      "outputs contact alarm signals according to a preset point condition. "
      "Monitoring of the power supply system to the data acquisition system "
      "is done by measuring the root mean square (rms) value of the AC supply, "
      "active power, apparent power, reactive power, frequency, power factor "
      "and phase angle. The data update cycle for the power supply system can "
      "be up to 2 seconds. Apart from the others, the three most important "
      "parts of a PC-based data acquisition system are: (a) hardware, "
      "(b) software, and (c) communication link.")

    # ------------------------------------------------------- (a) Hardware
    H(b, lang, "(a) Phần cứng", "(a) Hardware", level=3)

    P(b, lang,
      "Ngày nay, hệ thống thu thập dữ liệu sử dụng các ASIC (mạch tích hợp "
      "chuyên dụng) do chính nhà sản xuất phát triển và trở thành nhãn hiệu "
      "của họ. ASIC mang lại mức độ tích hợp hệ thống cao, giúp hệ thống nhỏ "
      "gọn và nhẹ hơn. Điều này dẫn đến tiêu thụ công suất thấp, sinh nhiệt "
      "ít và do đó nâng cao độ tin cậy của toàn hệ thống. Một cải tiến khác "
      "trong thiết kế là máy biến áp phẳng được dùng trong hệ thống thu thập "
      "dữ liệu. Máy biến áp phẳng khác với máy biến áp quấn dây thông thường; "
      "loại máy biến áp nhỏ và mỏng này gồm các cuộn dây màng mỏng chính xác "
      "nhiều lớp, tăng cường độ bền cách điện đồng thời giảm phát nhiệt và "
      "tiếng ồn. Một cải tiến nữa là các công tắc SSR (rơle thể rắn) có điện "
      "áp đánh thủng cao (khoảng 1500 V một chiều), phù hợp với các tiêu "
      "chuẩn an toàn công nghiệp. Dòng rò rất thấp cỡ 1 nA (một nanoampe) "
      "cho phép đo các tín hiệu điện áp rất nhỏ từ cặp nhiệt điện, pH, độ "
      "dẫn và các thiết bị phân tích khác với độ chính xác cao hơn. Mức "
      "tiêu thụ công suất thấp nhờ hoạt động êm hơn so với các dạng rơle "
      "khác.",
      "Nowadays data acquisition systems use ASICs (application specific "
      "integrated circuits) developed by the particular manufacturer and "
      "becoming their trademark. ASICs bring a high degree of system "
      "integration and make the system smaller and lighter. This altogether "
      "results in low power consumption, low heat generation and thereby "
      "improves the reliability of the overall system. Another improvement "
      "in design is the planar transformer used in the data acquisition "
      "system. A planar transformer differs from a conventional wire-wound "
      "transformer. This small and thin transformer consists of multi-layer "
      "precision thin-film coils that enhance insulation strength while also "
      "reducing heat and noise emission. Still another design improvement is "
      "the SSR switches (solid state relay switches), which have a high "
      "breakdown voltage (nearly 1500 volts DC). This voltage matches "
      "industrial safety norms. Their low leakage current, of the order of "
      "1 nA (one nanoampere), enables very low level voltage signals from "
      "thermocouples, pH, conductivity and other analysis equipment to be "
      "measured with higher accuracy. Power consumption is low owing to "
      "their quiet operation compared with other forms of relays.")

    FIG(b, 35, F.fig_f35(), lang)

    # ------------------------------------------------------- (b) Software
    H(b, lang, "(b) Phần mềm", "(b) Software", level=3)

    P(b, lang,
      "Phần mềm hệ thống thu thập dữ liệu chạy trên mọi nền tảng Windows "
      "(từ 95 trở đi) và trên hệ điều hành Windows 32-bit. Phần mềm chính, "
      "dùng chung cho mọi chức năng thu thập dữ liệu, gồm thiết lập phần "
      "cứng, ghi dữ liệu đơn giản, xem dữ liệu đơn giản, chuyển đổi dữ liệu "
      "qua MS Excel hoặc định dạng ASCII, thiết lập tùy chọn, chẩn đoán hệ "
      "thống và hiệu chuẩn. Một phần mềm khác, gọi là phần mềm thiết lập "
      "tham số, cho phép trao đổi mọi dữ liệu liên quan đến thiết lập, ví dụ "
      "dải đo, thời gian đo, thời điểm bắt đầu đo, tạo báo động, biểu thức "
      "sự kiện/hành động và các hàm tính toán do PC thực hiện.",
      "The data acquisition system software runs on all Windows-based "
      "platforms (95 onwards) and on the 32-bit Windows operating system. "
      "The main software, common to all data acquisition functions, includes "
      "hardware set-up, simplified data logging, simplified data viewing, "
      "data conversion through MS Excel or ASCII format, preference setting, "
      "system diagnosis and calibration functions. Another software, called "
      "parametric setting software, allows the exchange of all set-up related "
      "data items, for example the range of measurement, duration of "
      "measurement, start time of measurement, alarm generation, event/action "
      "expression and computation functions by the PC.")

    P(b, lang,
      "Phần mềm thứ ba, gọi là phần mềm thiết lập hệ thống, chẩn đoán và "
      "hiệu chuẩn, chủ yếu xác định phương pháp truyền thông với bộ chính "
      "và thiết lập một thư mục cho mục đích này. Phần mềm này cũng cho phép "
      "xem dữ liệu hiệu chuẩn chứa trong ROM (bộ nhớ chỉ đọc) và khởi tạo "
      "mọi thiết lập/cấu hình của bộ chính.",
      "The third software, known as system set-up, diagnosis and calibration "
      "software, mainly defines the communication method with the main unit "
      "and also sets up a directory for this purpose. It also allows viewing "
      "the calibration data contained in the ROM (read only memory) and "
      "initializing all the settings/configuration of the main unit.")

    P(b, lang,
      "Phần mềm thứ tư là phần mềm ghi và xem dữ liệu (thông qua thiết lập "
      "thẻ), rất quan trọng đối với người dùng. Phần mềm này hiển thị mọi dữ "
      "liệu đo và tính toán trên thiết bị hiển thị. Các dữ liệu này có thể "
      "được lưu trên thiết bị lưu trữ ngoài nhờ các chức năng thu thập dữ "
      "liệu. Nhiều công cụ đồ họa khác nhau như đường xu hướng tương tự, cửa "
      "sổ hiển thị số và cửa sổ tổng quan báo động cho phép cấu hình màn "
      "hình tối ưu cho từng ứng dụng. Số thẻ cho mỗi kênh có thể được hiển "
      "thị bằng 8 hoặc 16 ký tự nhờ phần mềm thiết lập thẻ.",
      "The fourth software is the data logger and viewing (through tag "
      "setting) software, which is important to the user. It shows all the "
      "measured and computed data on the display unit. These data can be "
      "saved on an external storage unit by the data acquisition functions. "
      "Various graphic tools, such as analog trending waves, digital display "
      "windows and alarm overview windows, enable optimum screen "
      "configuration for every application. Tag numbers for every channel "
      "can be shown by means of the tag setting software in 8 or 16 "
      "characters.")

    # --------------------------------------------- (c) Communication link
    H(b, lang, "(c) Liên kết truyền thông", "(c) Communication link", level=3)

    P(b, lang,
      "Liên kết truyền thông là cần thiết để nối các hệ thống số với nhau "
      "nhằm chia sẻ và tổng hợp thông tin chứa trong các tín hiệu đầu vào "
      "của quá trình. Đây là thành phần quan trọng khác của hệ thống thu "
      "thập dữ liệu đang được thảo luận. Các liên kết vật lý, có thể là dây "
      "xoắn đôi, cáp đồng trục hoặc cáp quang, đã được thảo luận kỹ ở chương "
      "trước. Ở đây chúng ta chỉ giới hạn thảo luận vào các loại chuẩn giao "
      "diện truyền thông, gồm các loại thường gặp sau cho chức năng thu thập "
      "dữ liệu: (i) RS-232 (Recommended Standard), (ii) RS-422, (iii) RS-485, "
      "(iv) Ethernet, (v) GPIB (General Purpose Interface Bus) và (vi) CAN "
      "(Controller Area Network).",
      "Communication links are necessary for interconnecting digital systems "
      "together to share as well as consolidate the information contained in "
      "the process input signals. The communication link is yet another "
      "important component of the data acquisition system under discussion. "
      "The physical links, which may be a twisted pair of wires, a coaxial "
      "cable or a fiber optic cable, have been discussed at length in the "
      "previous chapter. Here we confine our discussion to the types of "
      "communication interface standards, which include the following common "
      "varieties for data acquisition functions: (i) RS-232 (Recommended "
      "Standard), (ii) RS-422, (iii) RS-485, (iv) Ethernet, (v) GPIB "
      "(General Purpose Interface Bus), and (vi) CAN (Controller Area "
      "Network).")

    # ----------------------------------------------------------- (i) RS232
    H(b, lang, "(i) Chuẩn RS-232", "(i) RS-232 Standard", level=4)

    P(b, lang,
      "Chuẩn RS-232 do EIA (Hiệp hội Công nghiệp Điện tử) phát triển là giao "
      "diện truyền thông nối tiếp phổ biến nhất trong công nghiệp. Chuẩn này "
      "được lắp trên mọi máy tính cá nhân (COM1 và COM2) và modem, và quy "
      "định đầu nối 25 chân cho DCE (thiết bị truyền thông dữ liệu) và DTE "
      "(thiết bị đầu cuối dữ liệu). Sơ đồ chi tiết của liên kết RS-232D được "
      "thể hiện ở Hình 5.36. Mức điện áp trong chuẩn RS-232 nằm trong khoảng "
      "±3 V một chiều đến ±25 V một chiều. Mức điện áp từ +3 V đến +25 V "
      "biểu thị bit 0, còn mức từ −3 V đến −25 V biểu thị bit 1 (cả hai mức "
      "đều tính theo chân nối đất tín hiệu). Chuẩn RS-232 không được dùng ở "
      "khoảng cách vượt quá 50 feet và tốc độ dữ liệu trên 20 kbps.",
      "The recommended standard RS-232 was developed by the EIA (Electronic "
      "Industries Association); it is a serial communication interface and "
      "the most popular interface in industry. It is installed on all "
      "personal computers (COM1 and COM2) and modems. The standard specifies "
      "a 25-pin connector for DCE (data communication equipment) and DTE "
      "(data terminal equipment). The detailed drawing of the RS-232D link "
      "is shown in Figure 5.36. The voltage level in the RS-232 standard "
      "ranges from ±3 V DC to ±25 V DC. A voltage level between +3 V and "
      "+25 V represents a 0 bit, and a level between −3 V and −25 V "
      "represents a 1 bit (both levels are with respect to the signal ground "
      "pin). The RS-232 standard is not used beyond 50 feet or at data rates "
      "above 20 kbps.")

    FIG(b, 36, F.fig_f36(), lang)

    # ---------------------------------------------------------- (ii) RS422
    H(b, lang, "(ii) Chuẩn RS-422", "(ii) RS-422 Standard", level=4)

    P(b, lang,
      "Chuẩn RS-422 cần tổng cộng bốn dây (hai dây cho đầu phát và hai dây "
      "cho đầu thu), trong khi RS-232 chỉ cần ba dây. Cả hai cách nối, tức "
      "hệ ba dây cho RS-232 và hệ bốn dây cho RS-422, được thể hiện ở Hình "
      "5.37. Như có thể thấy, RS-422 cân bằng đối với đất nên có thể dùng "
      "cho khoảng cách lớn và tốc độ dữ liệu cao hơn tới 10 mbps. Các cặp "
      "dây xoắn dùng trong RS-422 tăng khả năng chống nhiễu cho toàn hệ "
      "thống truyền thông, vừa là ưu điểm vừa tiết kiệm chi phí. Điện áp tín "
      "hiệu trên liên kết RS-422 nằm giữa ±200 mili-vôn và ±6 V một chiều; "
      "mức từ +200 mV đến +6 V một chiều biểu thị bit 0, còn mức từ −200 mV "
      "đến −6 V một chiều biểu thị bit 1.",
      "The RS-422 standard requires altogether four wires (two each for the "
      "transmit and receive terminals), whereas RS-232 requires only three "
      "wires. Both connection details, that is the three-wire system for "
      "RS-232 and the four-wire system for RS-422, are shown in Figure 5.37. "
      "As can be seen, RS-422 is balanced with respect to ground, so it can "
      "be used over large distances and can operate at the much higher data "
      "rate of 10 Mbps. The twisted wire pairs used in RS-422 enhance the "
      "noise immunity of the whole communication system, which is an added "
      "advantage and also an economy. The signalling voltage on an RS-422 "
      "link ranges between ±200 millivolts and ±6 volts DC. A voltage level "
      "between +200 mV and +6 V DC represents a 0 bit, and a level between "
      "−200 mV and −6 V DC represents a 1 bit.")

    FIG(b, 37, F.fig_f37(), lang)

    # --------------------------------------------------------- (iii) RS485
    H(b, lang, "(iii) Chuẩn RS-485", "(iii) RS-485 Standard", level=4)

    P(b, lang,
      "Chuẩn RS-485 về cấu tạo tương đương RS-422, chỉ khác nhau ở tốc độ dữ "
      "liệu (56 kbps đối với RS-485). Nhưng khác biệt kỹ thuật chính giữa "
      "hai chuẩn là RS-485 được thiết kế cho truyền thông mạng, hoàn toàn "
      "khác với truyền thông điểm-điểm. Trong liên kết điểm-điểm chỉ có hai "
      "thiết bị số được nối với nhau nên không cần giao thức mạng. Trong hệ "
      "thống truyền thông mạng luôn có nhiều hơn hai thiết bị số, do đó "
      "phát sinh vấn đề chia sẻ đường liên kết với các thiết bị khác. Việc "
      "phối hợp truyền dữ liệu giữa các thiết bị số đòi hỏi cấu trúc liên "
      "kết mạng bên cạnh giao thức mạng, vì vậy các chuẩn liên kết truyền "
      "thông khác nhau. Vì trong hệ thống đo lường chỉ dùng mạng hiệu năng "
      "trung bình, ví dụ bộ phát thông minh đa nhánh, RS-485 được thiết kế "
      "phù hợp và là chuẩn liên kết thích hợp nhất cho mục đích này. Liên "
      "kết RS-485 đơn giản và rẻ nhất được lắp cùng cấu trúc dạng bus như "
      "Hình 5.38.",
      "The RS-485 standard is constructional equivalent to RS-422, with the "
      "only difference being the data rate (56 kbps for RS-485). But the "
      "major technical difference between them is that RS-485 has been "
      "designed for network communications, which is completely different "
      "from point-to-point communications. In a point-to-point communication "
      "link only two digital attachments are interconnected, and therefore "
      "they do not require any network protocol at all. In a network "
      "communication system, however, more than two digital attachments are "
      "always present, and therefore the problem of sharing the link with "
      "other devices arises. Coordinating data transfer among the various "
      "digital attachments needs network topology in addition to network "
      "protocol, and therefore the communication link standards differ. "
      "Since instrumentation systems involve only a medium-performance "
      "network, for example multidrop smart transmitters, RS-485 has been "
      "designed accordingly and is the most suitable standard link for the "
      "purpose. The simple and most inexpensive RS-485 link is installed in "
      "combination with bus topology, as shown in Figure 5.38.")

    FIG(b, 38, F.fig_f38(), lang)

    # -------------------------------------------------------- (iv) Ethernet
    H(b, lang, "(iv) Ethernet", "(iv) Ethernet", level=4)

    P(b, lang,
      "Dù Ethernet thường được dùng trong mạng văn phòng, hiện nay việc "
      "liên kết các hoạt động và quản lý đo lường dưới dạng CIM (sản xuất "
      "tích hợp máy tính) đã bắt đầu. Ethernet trở thành chuẩn công nghiệp. "
      "Vì Ethernet cần kết nối với các hệ thống khác nhau, chuẩn này định "
      "nghĩa hai lớp: một lớp liên kết vật lý và một lớp truy cập thông qua "
      "tranh chấp. Lớp vật lý yêu cầu liên kết 10 Mbit, còn phương thức "
      "truy cập mạng là CSMA/CD, tức Truy cập đa phát sóng mang với Phát "
      "hiện va chạm. Thông điệp gửi qua Ethernet có dạng gói tin, với định "
      "dạng thể hiện ở Hình 5.39.",
      "Although Ethernet is commonly used in office networking, "
      "interconnectivity of instrumentation operations and administration "
      "in the form of CIM (computer integrated manufacturing) has now begun. "
      "Ethernet has become an industry standard. Since Ethernet is required "
      "to have connectivity with different systems, it defines two layers: "
      "one is the physical link and the other is access through contention. "
      "The physical layer requires a 10 Mbit link and the network access "
      "method is CSMA/CD, that is Carrier Sense Multiple Access with "
      "Collision Detection. Messages sent through Ethernet are in the form "
      "of packets, whose format is shown in Figure 5.39.")

    FIG(b, 39, F.fig_f39(), lang)

    P(b, lang,
      "Ethernet là kỹ thuật điều khiển truy cập ngẫu nhiên: một trạm muốn "
      "truyền sẽ chờ kiểm tra xem hệ thống có rảnh không; nếu rảnh, trạm bắt "
      "đầu truyền, gọi là truy cập đa phát sóng mang. Trạm cũng theo dõi mạng "
      "để tránh truyền đồng thời. Tình trạng truyền đồng thời gây va chạm có "
      "thể được phát hiện qua tín hiệu sai lệch xuất hiện trên mạng; đây là "
      "phát hiện va chạm. Nếu va chạm xảy ra, các trạm va chạm dừng truyền "
      "trong một thời gian ngắn rồi thử truyền lại. Trong thời gian mạng tải "
      "cao, có thể xảy ra nhiều va chạm. Vì lý do đó, giao thức CSMA/CD có "
      "thể gây vấn đề cho việc thu thập dữ liệu quá trình thời gian thực, vì "
      "một trạm có thể mất một số dữ liệu quan trọng cần thiết cho một điều "
      "kiện công nghệ cụ thể. Do đó khi dùng Ethernet cho hệ thống thu thập "
      "dữ liệu, tải trên mạng được giữ cân bằng để tránh va chạm.",
      "Ethernet is a random access control technique in which a station "
      "wishing to transmit waits to check whether the system is free. If the "
      "system is free, it begins to transmit, which is called carrier sense "
      "multiple access. It also monitors the network to avoid multiple "
      "transmissions. Multiple transmissions resulting in collisions may be "
      "detected by observing the garbled transmission appearing on the "
      "network; this is collision detection. If a collision does occur, the "
      "colliding stations stop transmission for a brief period and then "
      "attempt to retransmit. During periods of higher network load, a "
      "number of collisions can be expected. Therefore the CSMA/CD protocol "
      "may pose problems for real-time process data acquisition, since a "
      "station may lose some critical data that may be absolutely necessary "
      "for a particular process condition. For this reason, when Ethernet is "
      "used for a data acquisition system, the load on the network is kept "
      "balanced so that collisions can be avoided.")

    # ----------------------------------------------------------- (v) GPIB
    H(b, lang, "(v) Hệ thống GPIB", "(v) GPIB System", level=4)

    P(b, lang,
      "Việc liên kết các thiết bị khác nhau để quan sát chung luôn gặp khó "
      "khăn vì mỗi thiết bị có các đặc tính điều khiển và các đặc điểm riêng. "
      "GPIB đã giải quyết vấn đề này rất kinh tế, cho phép liên kết chi phí "
      "thấp tới 15 thiết bị ngay cả khi chúng có tốc độ dữ liệu khác nhau. "
      "GPIB cũng cho phép truyền thông trực tiếp giữa các thiết bị. GPIB gồm "
      "16 đường tín hiệu: các đường 1 đến 8 là đường dữ liệu/lệnh ghép kênh, "
      "các đường 9 đến 11 dùng bắt tay, và các đường 12 đến 16 dành cho các "
      "chức năng quản lý của các thiết bị được nối trong hệ thống. Chiều dài "
      "bus bị giới hạn tới 20 mét và tốc độ truyền dữ liệu tới 3 MB/giây "
      "(thông số thiết kế; giá trị thực tế có thể thấp hơn). Cáp GPIB có đầu "
      "nối giống hệt ở hai đầu và có giá cao. Trong hệ thống GPIB, tại một "
      "thời điểm chỉ một thiết bị ở chế độ truyền, các thiết bị còn lại ở "
      "chế độ nhận. Bộ nhận nhận dữ liệu từ 8 đường (DI01 đến DI08). Các "
      "thao tác truyền dữ liệu được thực hiện qua ba đường tín hiệu: (i) DAV "
      "(dữ liệu hợp lệ trên đường dữ liệu), (ii) NRFD (không có bộ nhận cho "
      "dữ liệu mới) và (iii) NDAC (dữ liệu chưa được mọi bộ nhận chấp nhận).",
      "Interconnection of different instruments for common visualization has "
      "always been a problem because of the various control and other unique "
      "features associated with every instrument. GPIB solved this problem "
      "very economically, making possible low-cost interconnection of up to "
      "15 instruments even with different data rates. GPIB also makes direct "
      "communication between instruments possible. GPIB normally consists of "
      "sixteen different lines. Lines 1 to 8 form the multiplexed data/command "
      "signal lines, lines 9 to 11 are kept for handshaking, and lines 12 to "
      "16 are reserved for management functions of the different equipment "
      "connected in the system. The bus length is restricted to 20 metres and "
      "the data transfer rate is up to 3 MB/second (design figure; the "
      "practical figure may be less). The GPIB cable has identical connectors "
      "at both ends and is costly. In a GPIB system, at one time only one "
      "piece of equipment is in transmission mode while the remaining "
      "interconnected equipment are in receiving mode. The receiver receives "
      "data from the 8 lines (DI01 to DI08). Data transmission operations are "
      "accomplished by means of three signal lines: (i) DAV (data valid on "
      "the data lines), (ii) NRFD (no receiver for new data), and (iii) NDAC "
      "(data not accepted by all the receivers).")

    P(b, lang,
      "Bộ truyền trực tuyến điều khiển đường DAV, trong khi các bộ nhận "
      "điều khiển các đường NRFD và NDAC. Bộ điều khiển hệ thống (IFC), tức "
      "đường số 12, đảm nhận quyền điều khiển hệ thống. Bộ điều khiển hoạt "
      "động (ATN), đường số 13, điều khiển các chức năng ghép kênh của tín "
      "hiệu dữ liệu/lệnh. Đường số 14 (SRQ) là yêu cầu dịch vụ và đóng vai "
      "trò tín hiệu yêu cầu gửi tới bộ điều khiển hoạt động. Đường số 15 "
      "(REN) thực hiện chức năng điều khiển kích hoạt từ xa, và đường số 16 "
      "(EOI) báo hiệu kết thúc một khối dữ liệu.",
      "The on-line transmitter controls the DAV line, whereas the receivers "
      "control the NRFD and NDAC lines. The system controller (IFC), which is "
      "line number 12, takes over control of the system. The active "
      "controller (ATN), which is line number 13, controls the multiplexing "
      "functions of the data/command signals. Line number 14 (SRQ) is the "
      "service request and acts as a request signal for service to the active "
      "controller. Line number 15 (REN) performs remote enabling control "
      "functions, and line number 16 (EOI) indicates the end of a block.")

    # ------------------------------------------------------------ (vi) CAN
    H(b, lang, "(vi) CAN (Mạng khu vực điều khiển)",
      "(vi) CAN (Controller Area Network)", level=4)

    P(b, lang,
      "Giao thức CAN được thiết kế ban đầu cho các ứng dụng ô tô. Khi dùng "
      "một giao thức truyền thông cho mục đích này, có một số đặc điểm cần "
      "lưu ý: giao thức phải cung cấp phản hồi đúng thời gian với độ trễ có "
      "thể dự đoán và nhỏ nhất trước các hành vi động và không đồng bộ của "
      "ô tô. CAN là phiên bản cải tiến của phương thức truy cập CSMA/CD "
      "truyền thống. Giao thức dùng trọng tài từng bit (không phá hủy) để "
      "truyền đồng thời các thông điệp và phân xếp theo độ ưu tiên. Vì nút "
      "điều khiển bus cũng theo dõi để phát hiện xem nó có thua trọng tài hay "
      "không; khi thua, nút quay lại chế độ nhận cho đến khi quá trình truyền "
      "có độ ưu tiên cao hơn kết thúc. Cơ chế xác nhận thông điệp của CAN đặc "
      "biệt ở chỗ các nút biết chính xác trạng thái của thông điệp, cho tính "
      "nhất quán tốt hơn và giảm thời gian phục hồi lỗi xuống dưới 25 "
      "micro-giây ở tốc độ bus 1 megabit/giây.",
      "CAN communication protocol was originally designed for automobile "
      "applications. A few special points have to be taken care of when a "
      "communication protocol is used for this purpose. The protocol should "
      "be able to provide the required timely response with predictable and "
      "minimum latency to the dynamic and asynchronous behaviour of "
      "automobiles. CAN is a modified version of the traditional CSMA/CD "
      "access method. The protocol utilizes bit-to-bit arbitration of a "
      "non-destructive type to transmit messages simultaneously and arbitrate "
      "them priority-wise. Since the node controlling the bus also monitors "
      "to detect whether it has lost arbitration, in that case it returns to "
      "receiving mode until the higher-priority transmission ceases. The "
      "message acknowledgement scheme of CAN is typical in that nodes are "
      "aware of the exact status of the message, resulting in better "
      "consistency and a reduction in error recovery time to less than 25 "
      "microseconds at a bus speed of 1 megabit per second.")

    P(b, lang,
      "Các đặc tính xuất sắc của giao thức CAN như trên cũng thu hút các "
      "ngành công nghiệp tự động hóa quá trình, và giao thức đã được dùng "
      "trong một số sơ đồ thu thập dữ liệu phân tán. CAN dùng định dạng NRZ "
      "cùng cơ chế chèn bit để truyền dữ liệu. Chèn bit duy trì đồng bộ mạng, "
      "vốn sẽ bị mất do chồng chất điện áp nhiễu. Định dạng chuẩn của thông "
      "điệp gồm tám trường như Hình 5.40.",
      "The excellent features of the CAN protocol described above have also "
      "attracted process automation industries, and it has been utilized in "
      "some distributed data acquisition schemes. CAN employs NRZ formatting "
      "along with a bit stuffing scheme for data transmission. Bit stuffing "
      "maintains network synchronization that would otherwise be lost due to "
      "superimposition of noise voltage. The standard format of the message "
      "consists of eight fields, as shown in Figure 5.40.")

    FIG(b, 40, F.fig_f40(), lang)

    P(b, lang,
      "SOF và EOF lần lượt là điểm bắt đầu và kết thúc của khung thông điệp. "
      "ARB và RTR là các trường kết hợp về mặt kỹ thuật: ARB là trường trọng "
      "tài, còn RTR là mã thông điệp cho biết thông điệp có cần phản hồi hay "
      "không. CTRL là trường điều khiển 6 bit, và DATA là trường thông tin "
      "gồm tối đa 8 byte. CRC (Mã kiểm tra dự phòng vòng) là trường kiểm lỗi "
      "16 bit. ACK là trường xác nhận 2 bit gồm khe ACK (1 bit) và dấu phân "
      "cách ACK (1 bit).",
      "SOF and EOF are the start of the message frame and the end of the "
      "message frame, respectively. ARB and RTR are technically combined "
      "fields, where ARB is an arbitration field and RTR is a code message "
      "indicating whether the message shall have a reply or not. CTRL is a "
      "6-bit control field and DATA is the information field consisting of up "
      "to 8 bytes only. CRC (Cyclic Redundancy Code) is a 16-bit error "
      "checking field. ACK is a 2-bit acknowledge field consisting of an ACK "
      "slot (1 bit) and an ACK delimiter (1 bit).")

    # -------------------------------------------------- The TransNet design
    H(b, lang, "Thiết kế TransNet", "The TransNet design")

    P(b, lang,
      "Trong một thiết kế khác của hệ thống thu thập dữ liệu dựa trên PC, "
      "Host PC có thêm hai bộ vi xử lý. Một bộ gọi là bộ xử lý vào/ra (IOP) "
      "để điều khiển dữ liệu vào/ra (I/O), bộ kia gọi là bộ xử lý TransNet để "
      "điều khiển hệ thống truyền thông TransNet. IOP liên tục cập nhật dữ "
      "liệu I/O theo dữ liệu của bộ xử lý TransNet. Hoạt động này hoàn toàn "
      "không do Host PC điều khiển, nhưng Host PC có thể truy cập thông tin "
      "đó. IOP cũng thực hiện kiểm tra tính hợp lệ dữ liệu và duy trì trạng "
      "thái hệ thống. Bộ xử lý TransNet thực chất điều khiển việc trao đổi "
      "dữ liệu giữa Host PC và các mô-đun I/O phổ dụng. Các mô-đun I/O phổ "
      "dụng quét dữ liệu quá trình từ các bộ chuyển đổi và phần tử điều "
      "khiển cuối lắp trong nhà máy, đồng thời tự kiểm tra chẩn đoán để phát "
      "hiện lỗi và sự cố bất thường. Thông tin dữ liệu quá trình được chuyển "
      "tới bộ xử lý TransNet; IOP xử lý dữ liệu và cập nhật RAM. Toàn bộ hệ "
      "thống hoạt động theo nguyên lý xử lý phân tán và song song để nâng "
      "cao hiệu năng.",
      "In another design of a PC-based data acquisition system, the Host PC "
      "incorporates two additional microprocessors. One is called the "
      "input/output processor (IOP), for regulating input/output (I/O) data, "
      "and the other is called the TransNet Processor, for regulating the "
      "TransNet communication system. The IOP continuously updates the I/O "
      "data with respect to the data of the TransNet Processor. This "
      "operation is not controlled by the Host PC at all, but the Host PC can "
      "access this information. Data validation and maintenance of system "
      "status are also performed by the IOP. The TransNet Processor in fact "
      "controls the exchange of data between the Host PC and the universal "
      "I/O modules. These modules scan process data from the transducers and "
      "final control elements installed in the process plants, and also "
      "perform self-diagnostic checks for possible errors and unexpected "
      "faults. The process data information is transferred to the TransNet "
      "processor, the IOP processes the data and updates the RAM. The entire "
      "system works on the principle of distributed and parallel processing "
      "for better system performance.")

    P(b, lang,
      "Hệ thống truyền thông TransNet gồm nhiều bộ vi xử lý nối với nhau "
      "bằng bus nối tiếp tốc độ cao và cũng được nối giao tiếp với Host PC "
      "qua RAM. Thông tin được chuyển tới Host PC qua RAM. Hệ thống quét dữ "
      "liệu I/O và hoặc chuyển thông tin mới tới Host PC qua ngắt, hoặc tiếp "
      "tục quét cho đến khi chính Host PC ngắt. Cách khác là trong lúc hệ "
      "thống tiếp tục quét dữ liệu I/O mà không ngắt Host PC, một cờ bit "
      "được thiết lập để báo cho Host PC biết dữ liệu mới đã tới và sẵn sàng "
      "truy cập trên RAM. Hệ thống truyền thông TransNet hoạt động ở hai chế "
      "độ: chế độ quét bình thường và chế độ ngắt. Ở chế độ quét bình "
      "thường, các mô-đun I/O phổ dụng được IOP quét tuần tự. Các mô-đun lần "
      "lượt đáp ứng theo trạng thái hiện có bắt đầu từ mô-đun số 1 (theo cấu "
      "hình trong bảng) rồi tiếp tục từng mô-đun một. Mỗi mô-đun được cấp "
      "một khe thời gian và phải hoàn thành phản hồi trong khe đó; nếu "
      "không, bộ vi xử lý tạo mã lỗi cho mô-đun tương ứng. Riêng mô-đun đầu "
      "ra mong đợi phản hồi theo lệnh từ Host PC. Nếu các mô-đun không nhận "
      "được phản hồi hợp lệ, chúng trở về điều kiện mặc định. Ở chế độ ngắt, "
      "Host PC ngắt các thao tác quét bình thường để hỏi về biến hệ thống, "
      "trạng thái mô-đun hoặc bất cứ thông tin nào cần biết tại thời điểm "
      "đó.",
      "The communication system of TransNet comprises multiple "
      "microprocessors connected through a high-speed serial bus and "
      "interfaced with the Host PC through RAM as well. Information is "
      "transferred to the Host PC through RAM. The system scans the I/O data "
      "and either transfers new information to the Host PC through an "
      "interrupt, or continues scanning until interrupted by the Host PC "
      "itself. Another way is that while the system continues to scan the "
      "I/O data without interrupting the Host PC, a bit flag is set to let "
      "the Host PC know that new updated data have arrived and are available "
      "for access on the RAM. The TransNet communication system operates in "
      "dual mode: the first mode is called normal scanning mode and the "
      "second is called Interrupt Mode. During normal scanning mode, "
      "universal I/O modules are scanned in sequence by the IOP. The modules "
      "in turn respond according to their existing status, starting from "
      "module number 1 (as configured in the table) and continuing one by "
      "one. Every module is allotted a time slot and has to complete its "
      "response within that slot; if it fails to do so, the processor "
      "generates an error code for that particular module. The output module "
      "in particular expects a response on command from the Host PC. If the "
      "modules do not get a valid response, they revert to default "
      "conditions. During Interrupt Mode, the Host PC interrupts the normal "
      "scanning operations to inquire about system variables, module status "
      "or anything else required to be known at that moment.")

    # -------------------------------------------- Application software list
    H(b, lang, "Phần mềm hệ thống cho thu thập dữ liệu",
      "System software for data acquisition")

    P(b, lang,
      "Về lựa chọn phần mềm hệ thống, có thể chọn bất kỳ phần mềm nào sau "
      "đây tương thích với các thao tác thu thập dữ liệu:",
      "As far as the choice of system software is concerned, any of the "
      "following system software compatible with data acquisition operations "
      "can be selected:")

    L(b, lang,
      ["Intellutions FIX DMACS, ONSPEC và GENIE.",
       "Iconics GENESIS.",
       "Steeplechase Software VLC.",
       "Wonderware IN TOUCH.",
       "Lab View.",
       "NemaSoft Paragon.",
       "Ứng dụng OPC.",
       "DDE và các ứng dụng DDE 32.",
       "Citect.",
       "GE Cimplicity.",
       "Softple."],
      ["Intellutions FIX DMACS, ONSPEC and GENIE.",
       "Iconics GENESIS.",
       "Steeplechase Software VLC.",
       "Wonderware IN TOUCH.",
       "Lab View.",
       "NemaSoft Paragon.",
       "OPC application.",
       "DDE and DDE 32 Applications.",
       "Citect.",
       "GE Cimplicity.",
       "Softple."])

    P(b, lang,
      "Trong số các phần mềm ứng dụng này, Wonderware Intouch và GENIE rất "
      "phổ biến. Wonderware Intouch là chương trình Giao diện Người-Máy "
      "(MMI) đồ họa hướng đối tượng, dành riêng cho tự động hóa quá trình, "
      "điều khiển quá trình công nghiệp và giám sát, bao gồm các môi trường "
      "điều khiển như Hệ thống Điều khiển Phân tán và Hệ thống Giám sát và "
      "Thu thập Dữ liệu. Tính năng quan trọng và hiệu quả nhất của Wonderware "
      "Intouch là các trình hướng dẫn đồ họa được cấu hình sẵn (WIZARDS), "
      "giúp tạo ứng dụng mạnh mẽ nhanh hơn và dễ dàng hơn. Tương tự, GENIE "
      "cung cấp Giao diện Người dùng Đồ họa Hướng đối tượng (OOGUI) mạnh mẽ, "
      "làm cho chiến lược điều khiển cũng như hệ thống hiển thị trở nên đơn "
      "giản nhất. Hệ thống dựa trên Microsoft Windows, gồm việc chọn các "
      "khối biểu tượng từ hộp công cụ, nối chúng và vẽ đối tượng hiển thị "
      "động trực tiếp trên màn hình (không cần lập trình). Các chức năng thu "
      "thập dữ liệu chuẩn của điều khiển quá trình, các chức năng toán học "
      "và hiển thị liên quan có sẵn dưới dạng Thư viện-Khối Chức năng-Biểu "
      "tượng (LFBIs). GENIE còn cung cấp các gói phần mềm bổ sung tích hợp "
      "như Script Designer, Data Center, Task Designer, Screen Designer và "
      "Report Designer, mang lại cách thức giám sát và điều khiển biến quá "
      "trình dễ dàng và linh hoạt hơn.",
      "Of these application software packages, Wonderware Intouch and GENIE "
      "are very popular. Wonderware Intouch is an object-oriented Graphical "
      "Man-Machine Interface (MMI) application program specific to process "
      "automation, industrial process control and supervisory control, "
      "including control environments such as Distributed Control System and "
      "Supervisory Control and Data Acquisition System. The most significant "
      "and effective feature of Wonderware Intouch is its pre-configured "
      "graphic WIZARDS, which make the creation of powerful applications "
      "faster as well as easier. Similarly, GENIE presents a powerful Object "
      "Oriented Graphical User Interface (OOGUI) that makes both the control "
      "strategy and the display systems utterly simple. The system is "
      "Microsoft Windows based and consists of selecting icon blocks from "
      "the toolbox, connecting them and drawing the dynamic display object "
      "physically on the screen (that is, without any programming). Standard "
      "process control data acquisition functions, mathematical and other "
      "related display functions are available in the form of "
      "Library-Function-Block-Icons (LFBIs). GENIE also provides integrated "
      "additional software packages such as Script Designer, Data Center, "
      "Task Designer, Screen Designer and Report Designer, which offer "
      "comparatively easier as well as flexible means for monitoring and "
      "control of process variables.")

    # --------------------------------- Distributed DAQ and fieldbus systems
    H(b, lang, "Hệ thống thu thập dữ liệu điều khiển phân tán",
      "Distributed data acquisition and control system")

    P(b, lang,
      "Hệ thống thu thập dữ liệu đang được thảo luận được thể hiện dưới dạng "
      "sơ đồ khối ở Hình 5.41. Cáp twin axial được dùng làm liên kết vật lý "
      "của hệ thống; loại cáp này gồm một cặp dẫn nằm ở giữa và được bọc che "
      "chắn toàn bộ. Cáp twin axial có khả năng chống nhiễu vượt trội và tốc "
      "độ cao.",
      "The data acquisition system under discussion is shown in a block "
      "diagram view in Figure 5.41. A twin axial cable has been used as the "
      "physical link for the system. A twin axial cable has a pair of "
      "centrally located conductors with an overall shielding. It offers "
      "superior noise immunity and higher speed.")

    FIG(b, 41, F.fig_f41(), lang)

    P(b, lang,
      "Rõ ràng là chúng ta đang xem xét các loại hệ thống thu thập dữ liệu "
      "hiện đại dựa trên công nghệ mạng. Theo hướng đó, một hệ thống khác "
      "đang được đưa vào hoạt động, có thể gọi là hệ thống thu thập dữ liệu "
      "và điều khiển phân tán, trong đó các fieldbus phổ biến trong công "
      "nghiệp như RS-485 và CAN (Controller Area Network) đã được dùng; các "
      "hệ thống này truyền thông với Host PC qua mạng fieldbus đa nhánh như "
      "Hình 5.42. Một đặc điểm khác của hệ thống này là hỗ trợ hệ thống cáp "
      "composite, một liên kết vật lý chế tác riêng gồm mọi loại cáp truyền "
      "thông như cáp xoắn đôi, cáp đồng trục và cáp quang được bọc trong một "
      "vỏ bọc chung.",
      "As is obvious, we are going through different types of modern data "
      "acquisition systems based on networking technology. Along this line, "
      "another system is in operation which may be called a distributed data "
      "acquisition and control system, in which industry-popular field buses "
      "such as RS-485 and CAN (Controller Area Network) have been used, and "
      "the systems communicate with the Host PC over a multidrop fieldbus "
      "network as shown in Figure 5.42. Another peculiarity of this system is "
      "that it supports a composite cable system. A composite cable system is "
      "a custom-made physical link that encapsulates all types of "
      "communication cables, for example twisted pair cable, coaxial cable "
      "and fibre optic cables, in a single overall jacket.")

    FIG(b, 42, F.fig_f42(), lang)

    return b
