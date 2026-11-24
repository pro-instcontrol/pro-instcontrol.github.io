# -*- coding: utf-8 -*-
"""Chapter 2, "Transducers - II" — section module C (EN/VI bilingual).

Source: work/ipc_decoded.txt lines 3519-3973 (PDF pp. 99-109, printed
pp. 87-97): the second half of subsection 2.2.2 "Classification of Pressure
Measurement System", from the tail of the capacitance pressure transmitter
through variable-inductance, resonant-frequency, digital and smart
transmitters, communication, installation and zero suppression/elevation.
Ends immediately before section 2.3. Figures 2.22-2.33 appear in source order.
"""
import ipcfig2 as F
from ipc_ch02_lib import H, P, L, E, FIG, TBL, NOTE


def section(lang):
    b = []

    # ------------------------------------------------ tail of capacitance TX
    P(b, lang,
      "Phần tử cảm biến, về bản chất là một tụ điện thay đổi, phát hiện vị trí của màng cảm biến. "
      "Áp suất quá trình định vị màng cảm biến tương ứng để làm thay đổi điện dung của phần tử cảm "
      "biến. Điện dung ban đầu của phần tử cảm biến thường là 80 picofarad. Bộ dao động ở tần số "
      "thường là 80 kHz và 70 vôn (đỉnh-đỉnh) điều khiển phần tử cảm biến. Đầu ra từ phần tử cảm "
      "biến được chỉnh lưu bởi một bộ giải điều chế gồm mạch chỉnh lưu cầu toàn sóng. Bộ ổn áp "
      "cung cấp nguồn điện áp không đổi 6,4 vôn Một chiều làm chuẩn và 7 vôn Một chiều cho bộ dao "
      "động.",
      "The sensing element which is essentially the variable capacitor detects the position of "
      "the sensing diaphragm. The process pressure positions the sensing diaphragm accordingly "
      "to vary the capacitance of the sensing element. The initial capacitance of the sensing "
      "element is usually 80 picofarad. Oscillator at normally 80 kHz and 70 volts (peak-to-peak) "
      "drives the sensing element. The output from the sensing element is rectified by a "
      "demodulator which consists of a full-wave bridge rectifier circuit. The voltage regulator "
      "provides constant voltage supply of 6.4 volts D.C. for reference and 7 volts D.C. to "
      "oscillator.")
    FIG(b, 22, F.fig_f22(), lang)
    P(b, lang,
      "Bộ khuếch đại điều khiển dòng đưa mức điều khiển tới giá trị sao cho bộ phát hiện phản hồi "
      "một dòng bằng với dòng của cảm biến. Mạch giới hạn dòng ngăn đầu ra vượt quá 35 mADC trong "
      "điều kiện quá dải.",
      "The current controlled amplifier drives the control to a level such that the detector "
      "feeds back a current equal to sensor current. The current limiting circuit prevents the "
      "output from exceeding 35 mADC in an over range condition.")
    P(b, lang,
      "Một ưu điểm của loại bộ phát áp suất điện dung này là khả năng chịu quá dải cao vốn có. "
      "Loại thiết bị này có thành tích đã được chứng minh với thông số kỹ thuật rất tốt. Chúng có "
      "sẵn ở nhiều dải đo và hoạt động trong nhiều điều kiện môi trường khác nhau với độ chính xác "
      "±0,5% của dải hiệu chuẩn.",
      "An advantage of this type of capacitance pressure transmitter is its inherent high over "
      "range capability. This type of instruments have a proven track record with very good "
      "specification. They are available in a number of ranges and operate over a variety of "
      "ambient conditions with an accuracy of ±0.5% of calibrated span.")

    # ------------------------------------------------ (d) variable inductance
    H(b, lang,
      "(d) Bộ phát áp suất cảm ứng biến đổi",
      "(d) Variable inductance pressure transmitter", level=4)
    P(b, lang,
      "Như đã biết, chuyển động tương đối của một lõi so với cuộn dây quấn quanh nó sẽ làm thay đổi "
      "điện cảm của cuộn dây. Bố trí này tạo thành đặc điểm thiết kế cơ bản của bộ phát cảm ứng "
      "biến đổi. Cuộn dây là một phần của mạch dao động Xoay chiều nằm bên trong đơn vị điện tử như "
      "thể hiện trong Hình 2.23. Một chuyển động nhỏ của lõi phát hiện vị trí so với cuộn lực làm "
      "dịch chuyển đầu ra tần số của bộ dao động. Sự dịch chuyển tần số này tạo ra tín hiệu đầu ra "
      "tỉ lệ.",
      "As is known, the relative motion of a core with respect to a coil wound around shall "
      "result in a change in the inductance of the coil. Such arrangement constitutes basic "
      "design feature for the variable inductance transmitter. The coil is part of an A.C. "
      "oscillator circuit located inside the electronic unit as shown in Figure 2.23. A small "
      "amount of movement of the position detector core with respect to the force coil results "
      "in a shift of frequency output of the oscillator. This shift in frequency generates a "
      "proportional output signal.")
    FIG(b, 23, F.fig_f23(), lang)
    P(b, lang,
      "Tín hiệu đầu ra này được phát hiện bởi mạch phân biệt tích hợp trong đơn vị điện tử. Thực "
      "chất, tín hiệu này tỉ lệ với sự thay đổi áp suất đầu vào của phần tử Bourdon. Áp suất đầu "
      "vào tạo ra chuyển động trong lõi phát hiện vị trí của cụm cảm ứng thông qua liên kết vectơ "
      "và liên kết uốn cong chữ T. Đầu ra được tạo ra ở dạng 4 đến 20 mAmps. Một chiều cũng được "
      "đưa vào hệ thống phản hồi, gồm một cuộn từ đặt trên thanh thứ cấp. Bố trí này tạo ra một "
      "lực bằng và ngược chiều trên thanh để cân bằng lực do sự thay đổi của phần tử Bourdon gây "
      "ra bởi áp suất đầu vào đo được. Phản hồi âm này tạo sự ổn định.",
      "This output signal is detected by a discriminator circuit which is incorporated in the "
      "electronic unit. This is in fact proportional to change in pressure input of the bourdon "
      "element. The pressure input produces motion in the position detector core of the inductor "
      "assembly through vector linkage and T flexure link. The generated output which is in the "
      "form of 4 to 20 mAmps. D.C. is also fed to the feedback system, which consists of a "
      "magnetic coil placed on the secondary beam. This arrangement produces an equal and "
      "opposite force on the beam to balance the force created by the change in bourdon element "
      "due to measurement input pressure. This negative feedback provides stabilization.")

    # ------------------------------------------------ (e) resonant frequency
    H(b, lang,
      "(e) Bộ phát tần số cộng hưởng",
      "(e) Resonant frequency transmitter", level=4)
    P(b, lang,
      "Bộ phát loại tần số cộng hưởng hoạt động theo nguyên lý tần số tự nhiên của một vật cơ học "
      "chịu lực căng. Ví dụ, một sợi dây phẳng có tiết diện đáng kể được cho cộng hưởng ở tần số "
      "tự nhiên của nó dưới lực căng; những thay đổi kết quả trong sợi dây làm thay đổi tần số "
      "cộng hưởng của nó. Sợi dây này là một phần không thể tách rời của mạch dao động, làm cho bộ "
      "dao động thay đổi tần số, và cuối cùng tần số này tỉ lệ với áp suất đầu vào của quá trình. "
      "Tần số cộng hưởng fr của sợi dây dưới lực căng tỉ lệ với lực căng tạo ra trong dây bởi áp "
      "suất đầu vào của quá trình được áp dụng. Như vậy, bằng cách thực hiện phép toán điện tử "
      "chính xác trên tín hiệu tần số cộng hưởng, có thể phát triển một tín hiệu đầu ra tỉ lệ với "
      "áp suất chất lỏng áp dụng.",
      "The resonant frequency type transmitter works on the principle of natural frequency of a "
      "mechanical object under tension. For instance, a plane wire of considerable cross-section "
      "is allowed to resonate at its natural frequency under tension, the resulting changes in "
      "the wire change its resonant frequency. This wire being an integral part of an oscillator "
      "circuit causes the oscillator to change the frequency which shall be ultimately "
      "proportional to the process input pressure. Resonant frequency fr of the wire under "
      "tension is proportional to the tension created in the wire by the applied process input "
      "pressure. Thus, by performing exact electronic operation on the resonant frequency signal, "
      "an output signal can be developed which shall be proportional to applied fluid pressure.")
    P(b, lang,
      "Sơ đồ khối của bộ phát áp suất tần số cộng hưởng được thể hiện trong Hình 2.24. Mạch dao "
      "động giữ sợi dây cộng hưởng ở tần số cộng hưởng của nó. Đầu ra của bộ dao động được đưa tới "
      "mạch tạo xung, mạch này tạo ra hai tần số bổ sung cho nhau. Các tần số này được áp dụng cho "
      "hai bộ chuyển đổi tần số, bộ này tạo ra đầu ra 4 đến 20 mAmps. Một chiều tỉ lệ với lực căng "
      "của sợi dây.",
      "The block diagram of a resonant frequency pressure transmitter is shown in Figure 2.24. "
      "The oscillator circuit keeps the resonant wire at its resonant frequency. The output of "
      "the oscillator is fed to a pulse shaper circuit, which produces two complementary "
      "frequencies. These frequencies are applied to two frequency converter, which produces "
      "output as 4 to 20 mAmps D.C. proportional to tension of the wire.")
    FIG(b, 24, F.fig_f24(), lang)
    P(b, lang,
      "Bộ phát cộng hưởng thạch anh hoạt động theo nguyên lý này và có thể đo áp suất tới 2500 "
      "kg/cm². Cảm biến áp suất cộng hưởng thạch anh được thể hiện trong Hình 2.25. Trong cấu hình "
      "bộ phát thực tế, cảm biến được nối với mạch thông qua các mạch dao động và trộn tín hiệu. "
      "Đầu ra của mạch dao động tinh thể áp suất quá trình được trộn với tín hiệu tần số 7,2 MHz "
      "từ tinh thể chuẩn. Hiệu số giữa hai tần số cho ra một tín hiệu áp suất tần số thấp, xấp xỉ "
      "48 Hz cho mỗi lần thay đổi áp suất quá trình 1 kg/cm². Tần số của cảm biến nhiệt độ là 190 "
      "KHz với độ nhạy 8 Hz cho mỗi độ Celsius thay đổi nhiệt độ. Các tín hiệu áp suất và nhiệt độ "
      "dưới dạng tần số cùng với tín hiệu chuẩn 7,2 MHz được đưa tới bộ đếm tần số. Tín hiệu áp "
      "suất đã bù nhiệt thu được có độ chính xác cao. Bộ phát cộng hưởng thạch anh không có hiện "
      "tượng trễ và trôi tới nhiệt độ 175 °C. Độ chính xác rất cao có thể đạt được với thiết bị "
      "này.",
      "Quartz resonant transmitter works on this principle which can measure a pressure upto "
      "2500 kg/cm2. A quartz resonant pressure sensor has been shown in Figure 2.25. In actual "
      "transmitter configuration, the sensor is connected to the circuit through oscillator and "
      "mixer circuits. The output of the process pressure crystal oscillator circuit is mixed "
      "with 7.2 MHz frequency signal from reference crystal. The difference between the two "
      "frequency presents a low frequency pressure signal which is nearly 48 Hz for every "
      "kg/cm2 process pressure change. The temperature sensor frequency is 190 KHz with a "
      "sensitivity of 8 Hz for every degree centigrade of temperature change. The pressure and "
      "temperature signals in terms of frequency along with 7.2 MHz reference signal are fed to "
      "a frequency counter. The temperature compensated pressure signal so obtained has high "
      "degree of precision. The quartz resonant transmitter is free from hysteresis and drifts "
      "upto a temperature of 175C. Very high degree of accuracy can be achieved by it.")
    FIG(b, 25, F.fig_f25(), lang)

    # ------------------------------------------------ (f) digital transmitter
    H(b, lang,
      "(f) Bộ phát áp suất số",
      "(f) Digital pressure transmitter", level=4)
    P(b, lang,
      "Tiêu chí thiết kế cơ bản của bộ phát áp suất số vẫn giống như của bộ phát tương tự đã mô tả "
      "trước đó, ví dụ bộ phát căng kế, bộ phát điện dung hoặc cảm ứng biến đổi, thậm chí cả bộ "
      "phát khí nén. Điểm khác biệt duy nhất nằm ở phần điện tử, nơi thêm một mạch bổ sung gọi là "
      "bộ chuyển đổi tương tự sang số (A/D). Chức năng của bộ chuyển đổi A/D là chuyển tín hiệu "
      "tương tự 4 đến 20 mAmps. Một chiều sang dạng nhị phân số. Tín hiệu nhị phân thu được sau đó "
      "được đưa tới thiết bị chỉ thị số và/hoặc xử lý tiếp. Tuy nhiên, đầu ra của bộ phát khí nén "
      "trước hết được chuyển thành tín hiệu điện, tức là 4 đến 20 mAmps. Một chiều, bằng bộ "
      "chuyển đổi khí nén sang điện. Bộ chuyển đổi khí nén sang điện cùng với bộ chuyển đổi tương "
      "tự sang số đôi khi cũng được gọi là đơn vị điều hòa tín hiệu. Các linh kiện được chọn chứa "
      "trong đơn vị điều hòa tín hiệu phụ thuộc vào yêu cầu của một hệ thống chuyển đổi cụ thể.",
      "The basic design criteria for digital pressure transmitter remains same as that of the "
      "analog transmitter described earlier, e.g. strain gage transmitter, capacitance or "
      "variable inductance transmitter or even pneumatic transmitter. The only difference lies "
      "in the electronic part wherein an additional circuit called analog to digital converter "
      "(A/D) is added. The function of A/D converter is to convert the analog signal of 4 to 20 "
      "mAmps DC to binary digital form. The binary converted signal so obtained is fed to a "
      "digital indicator and/or further processed. The pneumatic transmitter output however is "
      "first converted to electrical signal, i.e. 4 to 20 mAmps. D.C. by means of a pneumatic to "
      "electrical converter. The pneumatic to electrical converter together with analog to "
      "digital converter is also sometimes called signal-conditioning unit. The selected "
      "components contained in the signal-conditioning unit depend upon the requirement of a "
      "particular system of conversion.")

    # ------------------------------------------------ (g) smart transmitter
    H(b, lang,
      "(g) Bộ phát thông minh",
      "(g) Smart transmitter", level=4)
    P(b, lang,
      "Bộ phát quá trình tương tự về cơ bản hoạt động trên công nghệ cảm biến tương tự và cung cấp "
      "tín hiệu đầu ra chuẩn để truyền đi xa bằng đơn vị điều hòa tín hiệu điện tử. Các bộ phát này "
      "đã hoạt động thành công trong một thời gian dài nhưng bị hạn chế về mức độ đa dụng, độ tin "
      "cậy, độ chính xác và độ chuẩn xác cao — những yêu cầu của một hệ thống thiết bị đo hiện "
      "đại. Sai số do trôi trong hành vi của linh kiện cảm biến, đặc tính phi tuyến của phần tử "
      "cảm biến, thay đổi môi trường, áp suất tĩnh và ảnh hưởng nhiệt độ của quá trình là một số "
      "yếu tố phức tạp đến mức rất khó bù trừ.",
      "The analog process transmitter works basically on analog sensor technology and provides "
      "standard output signal for remote transmission employing electronic signal conditioning "
      "unit. These transmitters have been working successfully for a long period of time but "
      "are limited in terms of high degree of versatility, reliability, accuracy and precision "
      "which are the requirements of a modern instrumentation system. Errors due to drift in "
      "sensor-component behaviour, non-linear characteristics of sensing element, environmental "
      "changes, static pressure and temperature effects of the process are some of the factors "
      "that are so complicated that it is very difficult to compensate for.")
    P(b, lang,
      "Tuy nhiên, những sai số này đã được loại bỏ hoàn toàn bằng cách thiết kế một bộ phát thông "
      "minh. Bộ phát thông minh cung cấp tín hiệu đầu ra tuyến tính, không bị ảnh hưởng bởi tất cả "
      "sai số kể trên. Việc sử dụng công nghệ vi xử lý thực hiện công việc này. Ngoài ra, bộ phát "
      "này còn cung cấp khả năng liên lạc hai chiều. Điều này có nghĩa là, ngoài việc nhận tín "
      "hiệu đầu ra tại đầu thu, dữ liệu hiệu chuẩn hoặc bất kỳ thay đổi nào khác có thể được thực "
      "hiện trên bộ phát ngay từ đầu thu.",
      "These, errors however, have completely been eliminated by designing a smart transmitter. "
      "A smart transmitter provides linear output signal free from all the above-mentioned "
      "errors. The use of microprocessor technology does the actual job. In addition, this "
      "transmitter provides facility for two-way communication as well. This means, in addition "
      "to obtaining the output signal at the receiving end, calibration data or any other changes "
      "can be performed on the transmitter from the receiving end itself.")
    P(b, lang,
      "Trong công nghiệp quá trình, có hai loại thiết kế cơ bản cho các bộ phát này đang được sử "
      "dụng. Trong loại thiết kế thứ nhất, nguyên lý cơ bản giống như của hệ thống tương tự được "
      "áp dụng và hệ thống tương tự thu được được chuyển sang dạng số. Tín hiệu đầu ra số này được "
      "đưa tới mạch vi xử lý để thực hiện tất cả các chức năng thông minh. Rõ ràng độ chính xác "
      "của thiết kế này bị giới hạn bởi tiêu chuẩn độ chính xác của kỹ thuật chuyển đổi tương tự "
      "sang số. Độ chính xác đạt được bằng kỹ thuật này luôn nhỏ hơn ±0,25% của dải hiệu chuẩn.",
      "In process industries, two types of basic design for such transmitters are in use. In the "
      "first design type, the same basic principle of analog system is applied and the resulting "
      "analog system is converted to digital form. This digital output signal is fed to a "
      "microprocessor circuit for performing all the smart functions. Obviously the accuracy of "
      "this design shall be limited by the accuracy standard of the analog to digital conversion "
      "techniques. Accuracy obtainable by this technique has always been less than ± 0.25% of "
      "calibrated span.")
    P(b, lang,
      "Hình 2.26 thể hiện loại bộ phát thông minh này dùng phần tử cảm biến điện dung cùng với cảm "
      "biến bù nhiệt độ. Bộ chuyển đổi tương tự sang số cung cấp tín hiệu số tương đương để vi xử "
      "lý xử lý. Trong quá trình đặc trưng hóa phần tử cảm biến tại nhà sản xuất, tất cả các phần "
      "tử cảm biến được cho chạy qua các chu kỳ nhiệt độ và áp suất khác nhau. Dữ liệu từ các thử "
      "nghiệm này được lưu trong một PROM (gọi là PROM tự đặc trưng hóa của bộ phát) để thực hiện "
      "các chức năng hiệu chỉnh tín hiệu trong quá trình hoạt động thực tế. EEPROM lưu trữ dữ liệu "
      "đặc trưng hóa. Các dữ liệu được phần mềm bộ phát thay đổi theo thời gian cũng được lưu "
      "trong EEPROM. Khi phần tử cảm biến, tức bộ chuyển đổi sơ cấp, được thay bằng một cái mới, "
      "các dữ liệu này được xóa. RAM được vi xử lý dùng cho các phép tính tạm thời và không bao "
      "giờ có thể truy cập bởi người dùng. Dữ liệu cấu hình bộ phát cũng như dữ liệu tuyến tính "
      "hóa phần tử cảm biến lưu trong EEPROM được giữ lại khi mất điện.",
      "Figure 2.26 shows this type of smart transmitter using capacitance sensing element, "
      "alongwith temperature compensating sensor. The analog to digital converter provides "
      "equivalent digital signal to be processed by microprocessor. During characterization of "
      "the sensing element at the manufacturing site, all the sensing elements are allowed to "
      "run through different temperature and pressure cycles. Data from these tests are stored "
      "in a PROM (known as self-characterization PROM of the transmitter) to carry out signal "
      "correction functions during actual operation. The EEPROM stores the characterization "
      "data. The data which are changed by the transmitter-software from time-to-time, are also "
      "stored in the EEPROM. When sensing element, i.e. primary transducer is replaced by a new "
      "one, these data are removed. The RAM is used by the microprocessor for temporary "
      "calculations and is never addressable by the user. Transmitter-configuration data as well "
      "as sensing element linearization data stored in EEPROM are retained on power failure.")
    FIG(b, 26, F.fig_f26(), lang)
    P(b, lang,
      "Đầu ra của bộ phát tương thích với giao thức HART (sẽ được mô tả sau). Liên lạc giữa Kỹ sư "
      "Thiết bị và bộ phát được thực hiện bằng một thiết bị đầu cuối từ xa gọi là HHC (được mô tả "
      "sau). Việc cải thiện độ chính xác đạt được bằng bộ phát thông minh luôn quan trọng đối với "
      "các nhà thiết kế. Nếu độ chính xác đo lường được cải thiện, có thể đạt được điều khiển "
      "chặt chẽ hơn quanh giá trị cài đặt của hệ thống điều khiển. Điều này dẫn đến cải thiện "
      "chất lượng sản phẩm, tối ưu hóa sử dụng nguyên liệu thô và tăng lợi nhuận. Trong thiết kế "
      "xét đến thứ hai của bộ phát thông minh, biến quá trình được cảm nhận trực tiếp ở dạng số, "
      "do đó không cần bộ chuyển đổi tương tự sang số. Bằng cách áp dụng kỹ thuật này, độ chính "
      "xác từ 0,075% đến 0,1% của dải hiệu chuẩn có thể đạt được.",
      "The output of the transmitter is compatible with HART protocol (to be described later). "
      "Communication between the Instrument Engineer and the transmitter is done by a remote "
      "terminal called HHC (described later). Improvement in accuracy obtainable by a smart "
      "transmitter has always been important for the designers. If measurement accuracy is "
      "improved, tighter control around the set value of the control system can be achieved. This "
      "will result in improvement in product quality, optimization in use of raw material and "
      "increase in profit. In the other design consideration of smart transmitter, the process "
      "variable is sensed in digital form directly and thus there is no need of an analog to "
      "digital converter as such. By employing this technique, an accuracy from 0.075% to 0.1% "
      "of calibrated span is obtainable.")
    P(b, lang,
      "Có một số kỹ thuật để chuyển đổi trực tiếp biến quá trình sang dạng số, nhưng hai trong số "
      "đó phổ biến hơn:",
      "Several techniques for direct digital conversion of process variable are available, but "
      "two of them are more popular:")
    L(b, lang,
      ["(i) Phần tử cảm biến silicon cộng hưởng",
       "(ii) Phần tử cảm biến cảm ứng kép"],
      ["(i) Resonant silicon sensing element",
       "(ii) Dual inductive sensing element"])

    H(b, lang,
      "(i) Phần tử cảm biến silicon cộng hưởng",
      "(i) Resonant silicon sensing element", level=4)
    P(b, lang,
      "Phần tử cảm biến silicon cộng hưởng được chế tạo từ silicon đơn tinh thể bằng một kỹ thuật "
      "điện tử đặc biệt. Kỹ thuật này được gọi là kỹ thuật vi ghép nối chất bán dẫn 3-D. Nhờ "
      "phương pháp chế tạo này, silicon có được các đặc tính cải tiến, cuối cùng mang lại độ ổn "
      "định và độ lặp lại tốt cho bộ phát với hầu như không có hiện tượng trễ.",
      "The resonant silicon sensing element is fabricated from a single crystal silicon using a "
      "special electronic technique. This technique is called 3-D semiconductor micro-matching "
      "technique. By this fabrication method silicon acquires improved characteristic features "
      "which ultimately provides good stability and repeatability to the transmitter with "
      "almost no hysteresis.")
    P(b, lang,
      "Trong cấu tạo của bộ phát có hai bộ cộng hưởng hình chữ H, cộng hưởng ở tần số tự nhiên "
      "90 KHz như thể hiện trong Hình 2.27.",
      "In the construction of the transmitter there are two H-shaped resonators, which resonate "
      "at their natural frequency of 90 KHz as shown in Figure 2.27.")
    FIG(b, 27, F.fig_f27(), lang)
    P(b, lang,
      "Áp suất quá trình áp dụng ép bộ cộng hưởng ở giữa vào trạng thái căng và bộ cộng hưởng ở "
      "ngoài vào trạng thái nén. Kết quả là tần số cộng hưởng của chúng thay đổi (một tăng dần Fa "
      "và cái kia giảm dần Fb như thể hiện trong Hình 2.28).",
      "The applied process pressure forces the central resonator into tension and the outer "
      "resonator into compression. As a result, their resonating frequencies change (one in "
      "increasing order Fa and the other one in decreasing order Fb as shown in Figure 2.28).")
    FIG(b, 28, F.fig_f28(), lang)
    P(b, lang,
      "Vi xử lý hoạt động sau đó tính toán tần số cộng hưởng vi phân tỉ lệ với áp suất áp dụng. "
      "Hệ thống này hoàn toàn khác với hệ thống đo tương tự thông thường. Đó là lý do không cần "
      "bộ chuyển đổi tương tự sang số. Bộ phát này có độ chính xác 0,075% của dải hiệu chuẩn. Với "
      "một cải tiến nhỏ trong thiết kế, tất nhiên sẽ tốn kém hơn, bộ phát này có khả năng tiệm cận "
      "độ chính xác thậm chí 0,003%.",
      "The active microprocessor then calculates the differential resonant frequency which is "
      "proportional to the applied pressure. This system is completely different from the "
      "conventional analog system of measurement. That is why the analog to digital converter "
      "is not required. This transmitter has the accuracy of 0.075% calibrated span. With slight "
      "improvement in the design, which of course will be costly, this transmitter is capable of "
      "approaching an accuracy of even 0.003%.")

    H(b, lang,
      "(ii) Phần tử cảm biến cảm ứng kép",
      "(ii) Dual inductive sensing element", level=4)
    P(b, lang,
      "Đây là một hệ thống hoàn toàn độc đáo chuyển đổi áp suất áp dụng cùng với nhiệt độ môi "
      "trường đã đo trực tiếp thành đầu ra tín hiệu số chuẩn hóa. Đơn vị đầu ra tín hiệu số chuẩn "
      "hóa hoạt động bằng cách dùng phần tử cảm biến cảm ứng kép, phần tử cảm biến nhiệt độ chính "
      "xác và bộ dao động đa chế độ. Bộ dao động đa chế độ là một mạch tích hợp ứng dụng riêng tạo "
      "ra tín hiệu số chuẩn hóa dựa trên việc chuyển mạch tuần tự của cảm ứng kép và phép đo nhiệt "
      "độ. Thiết kế số dạng này loại bỏ bộ chuyển đổi tương tự sang số. Sai số và độ trôi cũng "
      "được giảm thiểu.",
      "This is completely an unique system which converts the applied pressure along with "
      "measured ambient temperature directly to a standardized digital signal output. The "
      "standardized digital signal output unit functions by using a dual inductive sensing "
      "element, a precision temperature sensing element and a multimode oscillator. The "
      "multimode oscillator unit is an application specific integrated circuit that generates "
      "standardized digital signal based upon the sequential switching of the dual inductance "
      "and the temperature measurement. This type of digital design eliminates the "
      "analog-to-digital converter. Error and drift are also minimized.")
    P(b, lang,
      "Ở đây quá trình sản xuất cũng bao gồm đặc trưng hóa phần tử cảm biến, tức là dữ liệu đáp ứng "
      "áp suất tĩnh và nhiệt độ được lấy trên toàn bộ dải hoạt động và lưu trong EEPROM. Dữ liệu "
      "này xác định cách bộ phát sẽ hoạt động cho một ứng dụng cụ thể khi chịu các ảnh hưởng này. "
      "Phần tử cảm biến sơ cấp được trang bị cùng với các phần tử cảm biến áp suất tĩnh và nhiệt "
      "độ. Trong khi hoạt động, các phép đo môi trường trực tuyến được thực hiện. Vi xử lý so sánh "
      "dữ liệu này với dữ liệu đã đặc trưng hóa và thực hiện hiệu chỉnh. Độ chính xác đạt được bởi "
      "bộ phát này là ±0,1% của dải hiệu chuẩn.",
      "Here also the manufacturing process includes sensing element characterization i.e. the "
      "static pressure and temperature response data are taken over the entire operating range "
      "and stored in EEPROM. This data defines how the transmitter shall behave for a particular "
      "application when exposed to these effects. The primary sensing element is instrumented "
      "alongwith sensing elements for static pressure and temperature as well. While in "
      "operation, online environmental measurements are taken. The microprocessor compares this "
      "data with respect to characterized data and the correction is done. The accuracy obtained "
      "by this transmitter is ± 0.1% of calibrated span.")

    # ------------------------------------------------ communication interface
    H(b, lang,
      "Giao diện liên lạc",
      "Communication Interface", level=4)
    P(b, lang,
      "Vì chúng ta đã thảo luận rằng bộ phát thông minh có đặc tính liên lạc hai chiều, cần dùng "
      "một giao diện đặc biệt để thực hiện điều đó. Tùy chọn truyền tín hiệu 4 đến 20 mAmps. Một "
      "chiều có sẵn từ hiện trường, do đó bộ phát thông minh có thể đáp ứng yêu cầu dữ liệu số cụ "
      "thể từ phòng điều khiển. Các yêu cầu này liên quan đến chẩn đoán, trạng thái dữ liệu quá "
      "trình, thậm chí cả chi tiết thông số kỹ thuật của bộ phát. Các dữ liệu này hỗ trợ kiểm tra "
      "từ xa, chỉnh lại dải đo nếu cần, khắc phục sự cố khi có hỏng hóc, hoặc thậm chí lập tài liệu "
      "quá trình.",
      "Since we have already discussed that the smart transmitter has the especiality of two-way "
      "communication, special interface is required to be used for carrying out the same. The "
      "option of 4 to 20 mAmps. D.C. signal transmission is available from the field, hence smart "
      "transmitter can respond to a request for specific digital data from the control room. "
      "These requests are related to diagnostics, process data status and even transmitter "
      "specification details. These data help in remote checking, re-ranging if need be, "
      "troubleshooting in the event of any failure or even for process documentation.")
    P(b, lang,
      "Liên lạc được thực hiện bằng HHC (Bộ liên lạc cầm tay), có thể kết nối tại bất kỳ điểm nào "
      "trong vòng lặp. Các HHC này thường có hai loại: phổ dụng và/hoặc chuyên dụng. Bộ liên lạc "
      "loại phổ dụng liên lạc được với mọi loại bộ phát thông minh bất kể hãng sản xuất và kiểu "
      "loại, trong khi loại chuyên dụng được thiết kế cho một hãng và kiểu bộ phát cụ thể và "
      "không thể đáp ứng với các bộ phát khác.",
      "Communication is done by means of HHC (Hand-held Communicator), which can be connected at "
      "any point in the loop. These HHCs are normally of two types: universal and/or dedicated. "
      "While universal type communicator shall communicate with all types of smart transmitters "
      "irrespective of make and type, the dedicated one is designed for a particular make and "
      "type of transmitter and cannot respond to other transmitters.")
    P(b, lang,
      "Về giao thức liên lạc, có nhiều giao thức sẵn có để liên lạc với bộ phát. Trong số đó, giao "
      "thức Bell 202 FSK (Frequency Shift Keying – dịch chuyển tần số) phổ biến và được sử dụng "
      "rộng rãi. Tiêu chuẩn này chồng một tín hiệu tần số cao lên tín hiệu 4 đến 20 mAmps. Một "
      "chiều. Các số 1 và 0 được biểu diễn trên các tần số khác nhau. Định dạng này hỗ trợ liên "
      "lạc số cùng với tín hiệu 4 đến 20 m Amps. Một chiều không bị gián đoạn. Việc liên lạc diễn "
      "ra song song với bộ phát thông minh và có thể được khởi tạo từ bất kỳ điểm nào trong vòng "
      "lặp thiết bị đo.",
      "As far as communication protocols are concerned many protocols are available to "
      "communicate with the transmitter. Out of these the Bell 202 FSK (Frequency Shift Keying) "
      "protocol is popular and is in general use. This standard imposes a high frequency signal "
      "onto the 4 to 20 mAmps. D.C. signal. The 1s and 0s are represented on different "
      "frequencies. This format helps in digital communication along with 4 to 20 m Amps. D.C. "
      "signaling uninterrupted. The communication is in parallel with the smart transmitter and "
      "can be initiated from any point in the instrumentation loop.")

    # ------------------------------------------------ outstanding features
    H(b, lang,
      "Các đặc điểm nổi bật của bộ phát thông minh",
      "Outstanding Features of Smart Transmitters", level=4)
    P(b, lang,
      "(i) Các bộ phát thông minh có thể cấu hình từ xa như sau:",
      "(i)  The smart transmitters are remote configurable as indicated below:")
    L(b, lang,
      ["Đầu ra có thể chọn ở dạng 4 đến 20 mAmps. Một chiều hoặc dạng số.",
       "Dải đo tính theo phần trăm hoặc theo đơn vị kỹ thuật.",
       "Lựa chọn dải theo giá trị dưới và giá trị trên.",
       "Chi tiết bộ phát, ví dụ số seri, đầu ra tuyến tính hoặc căn bậc hai, số thẻ (tag number) v.v.",
       "Chi tiết hiệu chuẩn, ví dụ ngày hiệu chuẩn lần cuối, lần hiệu chuẩn tiếp theo đến hạn, "
       "dải hiệu chuẩn.",
       "Chi tiết báo động, ví dụ Thấp, Cao v.v."],
      ["Output is selectable in either 4 to 20 mAmps. D.C. or digital form.",
       "Span in percentage or in Engineering units.",
       "Range selection in lower and upper values.",
       "Transmitter details, e.g. serial number, linear or square root output, tag number etc.",
       "Calibration details, e.g. last calibration data, next calibration due, range of calibration.",
       "Alarm details, e.g. Low, High, etc."])
    L(b, lang,
      ["(ii) Tính năng tự chẩn đoán.",
       "(iii) Có liên lạc hai chiều.",
       "(iv) Độ chính xác tăng tới 0,1% và 0,075% của dải hiệu chuẩn. Độ chính xác bao gồm trễ, "
       "tuyến tính, độ lặp lại và độ trôi.",
       "(v) Ảnh hưởng của quá dải từ dải đo thông thường đến định mức áp suất tối đa là bình thường.",
       "(vi) Không có sai số do rung, độ ẩm, vị trí lắp đặt, ảnh hưởng nhiệt độ, ảnh hưởng môi "
       "trường hoặc ảnh hưởng tĩnh.",
       "(vii) Giảm tiêu thụ năng lượng và giảm chi phí bảo trì."],
      ["(ii) Self-diagnostic features.",
       "(iii) Two-way communication available.",
       "(iv) Increased accuracy upto    0.1% and 0.075% of calibrated span. Accuracy includes "
       "hysteresis, linearity, repeatability and drift.",
       "(v) Over ranging effect from usual span range to maximum pressure rating is normal.",
       "(vi) No error due to vibration, humidity, mounting position, temperature effects, "
       "environemental effects or static effect.",
       "(vii) Reduced power consumption and reduced maintenance cost."])

    # ------------------------------------------------ installation
    H(b, lang,
      "Lắp đặt các thiết bị đo áp suất",
      "Installation of Pressure Measuring Instruments", level=4)
    P(b, lang,
      "Lắp đặt thiết bị là một phần quan trọng của hệ thống đo. Hoạt động tin cậy và đọc chính "
      "xác của mọi hệ thống đo cũng phụ thuộc vào thực hành lắp đặt đúng cách. Các thực hành lắp "
      "đặt được thiết lập theo đặc tính của chất lỏng quá trình đang đo. Chúng ta biết rằng các "
      "phần tử đo áp suất, hay bất kỳ phần tử đo nào, tiếp xúc vật lý với chất lỏng quá trình. Do "
      "đó, luôn có khả năng hư hỏng hoặc các ảnh hưởng bất lợi khác cho phần tử. Các ảnh hưởng này "
      "có thể do tính chất dao động của chất lỏng, sự dao động nhiệt độ quá mức hoặc hiệu ứng độ "
      "nhớt của chất lỏng quá trình và nhiều yếu tố khác. Dù có thể tinh chỉnh thiết kế của chính "
      "phần tử để giảm thiểu các ảnh hưởng này, việc điều chỉnh thực hành lắp đặt cũng có thể giải "
      "quyết những vấn đề này. Bộ giảm dao động (Hình 2.29), cột cân bằng nhiệt độ (Hình 2.30) là "
      "một số phụ kiện được chấp nhận dùng trong lắp đặt công nghiệp gần như luôn luôn để chống "
      "lại các vấn đề kể trên. Ống mao dẫn thường được gọi là pigtail trong công nghiệp, thường có "
      "kích cỡ ½ inch như thể hiện trong Hình 2.29. Để đo áp suất bằng áp kế hoặc bộ phát, đây là "
      "bộ giảm dao động phổ dụng. Ống mao dẫn này đôi khi cũng được gọi là syphon và dùng để đo "
      "áp suất hơi ở nhiệt độ cao. Hiện tượng syphon giúp ngưng tụ hơi, từ đó giữ phần tử đo áp "
      "suất tránh xa hơi nhiệt độ cao.",
      "Installation of instrument is an important part of measurement system. Reliable operation "
      "and accurate reading of any measurement system also depend upon correct installation "
      "practices. The installation practices are laid down according to the characteristics of "
      "process fluids under measurement. We know that the pressure measuring elements or any "
      "measuring element come into physical contact with the process fluid. Due to this, there is "
      "every possibility of damage or other adverse effects to the element. These effects can be "
      "due to pulsating nature of the fluid, excessive temperature fluctuation or viscosity effect "
      "of the process fluid and many others. While design refinements are possible in the element "
      "itself to minimize these effects, modification in installation practices can also remove "
      "these problems. Pulsating dampeners (Figure 2.29) temperature equalizing columns (Figure "
      "2.30) are some of the acceptable auxiliaries employed in the industrial installation almost "
      "invariably for combating above-mentioned problems. The capillary piping popularly known as "
      "pigtail in the industries, are normally of inch size shown on Figure 2.29. For measurement "
      "of pressure by using pressure gages or transmitters, this is the universal pulsating "
      "dampener. This capillary piping is sometimes called syphon also and is used for the "
      "measurement of steam pressure at elevated temperature. The syphoning helps in condensing "
      "the steam and thereby keeping the pressure measuring element away from the high temperature "
      "steam.")
    FIG(b, 29, F.fig_f29(), lang)
    FIG(b, 30, F.fig_f30(), lang)
    P(b, lang,
      "Việc dùng cột cân bằng nhiệt độ giúp đưa nhiệt độ của chất lỏng quá trình về mức bằng nhau "
      "trước khi phép đo diễn ra, do đó các dao động nhiệt độ biến mất. Cột cân bằng nhiệt độ cũng "
      "đưa các chất lỏng về cùng một pha. Bình chắn được dùng để giữ chất lỏng quá trình tránh xa "
      "phần tử đo. Bình chắn không cho phần tử đo tiếp xúc với chất lỏng quá trình. Thực chất, "
      "chính chất lỏng chắn mới tiếp xúc vật lý với chất lỏng đo. Trong công nghiệp, thường dùng "
      "glycerene làm chất lỏng chắn để đo chất lỏng nhớt.",
      "The use of temperature equalizing column helps in bringing the temperature of process "
      "fluid to equal level before measurement takes place and hence the temperature fluctuations "
      "vanish. Temperature equalizing column also brings the fluids at the same phase. Seal pots "
      "are used to keep the process fluid away from the measuring element. Seal pots do not allow "
      "the measuring elements to come into contact of the process fluid. In fact, it is the "
      "sealing liquid, which is in physical contact of the measurement fluid. In industries "
      "usually glycerene is the liquid, which is used as sealing fluid for measurement of viscous "
      "fluid.")
    FIG(b, 31, F.fig_f31(), lang)
    FIG(b, 32, F.fig_f32(), lang)

    # ------------------------------------------------ impulse lines
    H(b, lang,
      "Đường dẫn xung",
      "Impulse Lines", level=4)
    P(b, lang,
      "Đường dẫn xung nối chất lỏng quá trình với thân chính của thiết bị thông qua hệ thống cô lập "
      "và xả phù hợp. Hình 2.33 thể hiện chi tiết lắp đặt điển hình để đo áp suất quá trình. Hai "
      "van cô lập tại điểm lấy mẫu được chọn để đạt được dự phòng 100%. Một đầu của khớp chữ T-1 "
      "đã được bịt kín. Đầu này được mở định kỳ để loại bỏ bọt khí bị kẹt và/hoặc để đổ chất lỏng "
      "chắn nếu cần. Van xả được mở khi cần xả sạch đường dẫn xung để làm sạch. Thiết bị được kẹp "
      "vào giá lắp và được nối với ống dẫn xung qua khớp nối ren và một van cô lập. Van cô lập này "
      "hỗ trợ tháo thiết bị để sửa chữa, hiệu chuẩn lại hoặc đại tu. Đây là bố trí lắp đặt chung, "
      "tuy nhiên có thể có những thay đổi nhỏ tùy theo đặc tính của chất lỏng quá trình đang đo.",
      "The impulse line connects the process fluid to the main body of the instrument through "
      "proper isolation and draining system. Figure 2.33 shows a typical installation details for "
      "measurement of process pressure. The two isolation valves at the tapping point are "
      "selected for obtaining 100% redundancy. One end of the Tee joint-1 has been plugged. This "
      "is opened periodically for removal of entrapped air bubble and/or for pouring in the "
      "sealing fluid if required. The drain valve is opened when it is required for flushing out "
      "the impulse line for cleaning. The instrument is clamped with respect to mounting stand and "
      "is connected to the impulse piping through union joint and an isolation valve. This "
      "isolation valve assists in removal of instrument for repair and recalibration or "
      "overhauling. This is a general installation arrangement, however, slight variations may "
      "be observed depending upon the characteristics of the process fluid under measurement.")
    FIG(b, 33, F.fig_f33(), lang)

    # ------------------------------------------------ zero suppression/elevation
    H(b, lang,
      "Triệt tiêu/Nâng điểm zero",
      "Zero Suppression/Elevation", level=4)
    P(b, lang,
      "Đôi khi hệ thống đo cho một chất lỏng quá trình cụ thể được lắp đặt sao cho một lượng đáng "
      "kể cột áp tĩnh tác dụng lên thiết bị. Cột áp này, gọi là cột áp thủy tĩnh, cộng thêm vào "
      "giá trị áp suất đo được và do đó tạo thành sai số cho tín hiệu đo. Một lò xo triệt tiêu zero "
      "được lắp gần cơ cấu chỉnh zero để bù cho sai số này. Lò xo triệt tiêu zero thêm một hiệu ứng "
      "thiên vị vào hệ thống chỉnh zero. Thực chất, điều này chỉ bổ sung vào lượng chỉnh zero. Lò "
      "xo này cũng đóng vai trò nâng zero bất cứ khi nào cần nâng cao giá trị đọc.",
      "Sometimes the measurement system for a particular process fluid is installed in such a way "
      "that an appreciable amount of static head acts on the instrument. This head which is "
      "called hydrostatic head adds to the value of measured pressure and therefore, constitutes "
      "an error to the measurement signal. A zero suppression spring is installed near the zero "
      "adjustment arrangement for making compensation for this error. The zero suppression spring "
      "adds a biasing effect to the zero adjustment system. In effect this only supplements to the "
      "amount of zero adjustment. This spring acts as zero elevation also whenever it is required "
      "to elevate the reading.")

    return "".join(b)
