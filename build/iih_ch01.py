# -*- coding: utf-8 -*-
"""Book 8, Chapter 1 - Measurement of Temperature (EN/VI bilingual).

Source: 3G E-learning LLC, *Illustrated Handbook of Industrial Instrumentation
& Control* (2018), PDF pp. 15-59 (45 pages of text, plus one blank p. 60),
printed pp. 1-45.  PAGES_SRC counts the 46 source pages 15-60 inclusive.

The chapter covers temperature scales, thermometers, probes, non-contact
devices, control system outputs, transmitters/readouts and application
considerations.  Its six numbered source figures (Figure 1 - Figure 6) are
redrawn as vectors in `iihfig.py` and placed where the source captions occur.
Prose is translated in full; image-only tables and equations that the text
layer does not contain are recorded as source quirks at the end.
"""

import iih_common as C
import iihfig as F
from iih_common import (eq, fig, h2, h3, h4, lead, note, ol, p, refs, table, ul)

PAGES_SRC = 46          # PDF pp. 15-60 inclusive (printed pp. 1-45, p. 60 blank)
BYLINE = "3G E-learning LLC · Illustrated Handbook of Industrial Instrumentation & Control (2018)"
TITLE_EN = "Measurement of Temperature"
TITLE_VI = "Đo nhiệt độ"


# ---------------------------------------------------------------------------
# Reference list (source pp. 41-45).  Citation text is kept as printed.
# ---------------------------------------------------------------------------
_REFS = [
    "http://www.physicsclassroom.com/class/thermalP/Lesson-1/Temperature-and-Thermometers",
    "https://doc.lagout.org/electronics/Fundamentals%20of%20Industrial%20Instrumentation%20"
    "and%20Process%20Control%20%5Bby%20William%20Dunn%5D.pdf",
    "http://myprojectforu.weebly.com/uploads/6/3/6/7/6367594/"
    "introduction_instrumentationsensors_controlsystems.pdf",
    "https://web.mst.edu/~cottrell/ME240/Resources/Temperature/Temperature.pdf",
    "http://nptel.ac.in/courses/108105063/pdf/L-04(SS)(IA&amp;C)%20((EE)NPTEL).pdf",
    "http://www.jma.go.jp/jma/jma-eng/jma-center/ric/Our%20activities/"
    "International/CP2-Temperature.pdf",
    "http://www.npl.co.uk/educate-explore/factsheets/temperature/",
    "Comptes rendus, Conference Generale des Poids et Mesures, 94 (1927). See also: Hall J.A, "
    "“The Early history of the International Practical Scale of Temperature”, Metrologia, 1967, "
    "3, (1), 25-28; and Hall J.A, Barber C.R. “The Evolution of the International Practical "
    "Temperature Scale”, Metrologia, 1967, 3 (3), 78-86.",
    "Dewitt D.P. and Nutter G.D. (1988). Theory and Practice of Radiation Thermometry. 1138 pp; "
    "John Wiley and Sons, Inc. New York.",
    "Fahrenheit G.D. (1724). Experimenta &amp; Observations De Congelatione Aquae in Vacuo Factae "
    "a D G Fahrenheit R.S.S. Philoshophical Transactions (1683-1775), Vol 33. (1724-1725, "
    "pp.78-84.",
    "Guilliaume C.E. (1899). Traite practique de la Thermometric de precision. Paris: "
    "Gauthier-Villars et Fil.",
    "Mathews, D., “Choosing and Using a Temperature Sensor,” Sensors Magazine, Vol. 17, No. 1, "
    "January 2000.",
    "Krysciar, T., “Low Temperature Measurements with Thin Film Platinum Resistance Elements,” "
    "Sensors Magazine, Vol. 16, No. 1, January 1999.",
    "Lavenuth, G., “Negative Temperature Coefficient Thermistors,” Sensors Magazine, Vol. 14, "
    "No. 5, May 1997.",
    "Humphries, J. T., and L. P. Sheets, Industrial Electronics, 4th ed., Delmar, 1993, "
    "pp. 320-323.",
    "Klopfenstien, Jr., R., “Linearization of a Thermocouple,” Sensors Magazine, Vol. 14, "
    "No. 12, December 1997.",
    "Bedrossian, Jr., J., “Infrared Noncontact Temperature Measurement,” Proceedings Sensor "
    "Expo, 1994, pp. 597-602.",
    "Barron, W. R., “Infrared Thermometry—Today,” Proceedings Sensor Expo, 1993, pp. 1-12.",
    "DeWitt, D. P., “Infrared Thermometry—Tomorrow,” Proceedings Sensor Expo, 1993, pp. 13-16.",
    "Ristic, L., Sensor Technology and Devices, Artech House 1994, pp. 287-315.",
    "Scolio, J., “Temperature Sensor IC's Simplify Designs,” Sensors Magazine, Vol. 17, No. 1, "
    "January 2000.",
    "Maxwell, D., and R. Williamson, “Wireless Temperature Monitoring in Remote Systems,” "
    "Sensors Magazine, Vol. 19, No. 10, October 2002.",
    "Desmarais, R., and J. Breuer, “How to Select the Right Temperature Sensor,” Sensors "
    "Magazine, Vol. 18, No. 1, January 2001.",
    "Johnson, C. D., Process Control Instrumentation Technology, 7th ed., Prentice Hall, 2003, "
    "pp. 36-38.",
    "Paluch, R., “Field Installation of Thermocouple &amp; RTD Temperature Sensor Assemblies,” "
    "Sensors Magazine, Vol. 19, No. 8, August 2002.",
    "Stokes J., and G. Palmer, “A Fiber Optic Temperature Sensor,” Sensors Magazine, Vol. 19, "
    "No. 8, August 2002.",
    "Harrison T.R. (1960). Radiation Pyrometry and Its Underlying Principles of Heat Transfer. "
    "234 pages, John Wiley and Sons, Inc., New York.",
    "Hudson R.P. (1982). Temperature scales, the IPTS, and its future development. Temperature, "
    "Its Measurement and Control in Science and Industry (ed. J.F Schooley). Pages 1-7, Vol. 5 "
    "Part 1, American Institute of Physics, New York.",
    "Knowles W.E. (1966). A History of the Thermometer. 249 pp. Johns Hopkins Press, Baltimore.",
    "M. Planck, (1900). “Ueber irreversible Strahlungsvorgange.” (Concerning Irreversible "
    "Radiation Processes.) Annals der Physik (Leipzig) 1, 69.",
    "Mangum B.W. and Furukawa G.T. (1990). Guidelines for Realizing the International "
    "Temperature Scale of 1990 (ITS-90). NIST Technical Note 1265. 199 pp. Washington, D.C.: "
    "National Institute of Standards and Technology (NIST), Superintendent of Documents, US "
    "Government Printing Office.",
    "McGee T.D. (1988). Principles and Methods of Temperature Measurement. 581 pages, John "
    "Wiley and Sons, New York.",
    "Nicholas, J.R. and White, D.R., (2001) “Traceable Temperatures, an Introduction to "
    "Temperature Measurement and Calibration”, 2nd Ed., John Wiley and Sons Ltd., Chichester, "
    "England, 421 pages.",
    "Callendar H.L. (1887). On the practical measurement of temperature: experiments made in the "
    "Cavendish Laboratory, Cambridge. Philosophical Transactions of the Royal Society of "
    "London A 178, 161.",
    "Ohte A., Yamagata M., and Akiyama K. (1982). Precision silicon transistor thermometer. "
    "Temperature, Its Measurement and Control in Science and Industry (ed. J.F. Schooley), "
    "American Institute of Physics, New York, pp. 1197-1203.",
    "Preston-Thomas H. (1990). The International Temperature Scale of 1990 (ITS-90). Metrologia "
    "27, 3-10.",
    "Ripples, D.C. (2003), “Temperature Its Measurement and Control in Science and Industry”, "
    "Vol 7, Part 1, pp. 1 to 552 and Part 2, pp. 553 to 1132, American Institute of Phisics, "
    "Melville, N.Y.",
    "Rusby R.L., Hudson-Thomas R.P., Durieux M., Schooley J.F., Steur P.P.M., and Swenson "
    "C.A. (1991). Thermodynamic basis of the ITS-90. Metropologia 28, 9-18.",
    "Seebeck T.J. (1822/1823). Evidence for the thermal current from a combination Bi-Cu by its "
    "action on a magnetic needle. Abhandlungen der Physicalische Klasse der Koniglichen "
    "Akademie der Wissenschaften zu Berlin aus den Jahren 1822-1823, pages 265-373.",
    "Thomson W. (1847). Theory of thermoelectricity. Transactions of the Royal Society of "
    "Edinburgh 21, 153.",
    "W. Thomson (1848) “On an Absolute Thermodynamic Scale of Temperature founded on Carnot's "
    "Theory of the Motive Power of Heat” Philosophical Magazine [3] 33, 313-317.",
    "Hawley, S. A., J. E. Breyer, and F. Dunn, Fabrication of miniature thermocouples for uhf "
    "acoustic detectors, Rev. Sci. Instr. 33, 1118 (Oct.).",
    "Heyne, W., Precision measurements in examining the relation between thermal e.m.f. and "
    "temperature of Pt-Rh/Pt thermocouples by comparison with a normal thermocouple, "
    "Feingeratetech. 11, 400 (Sept.).",
    "Jackson, P. L., Use of a large thermocouple junction to locate temperature disturbances. "
    "Rev. Sci. Instr. 33, 334 (Mar.).",
    "Kislyi, P. S., Prospects of utilizing refractory compounds for high temperature "
    "thermocouples, Poroshkovaya Met., Akad. Nauk SSSR 2, No. 4, 50.",
    "Lachman, J. C, Ck)axial thermocouple viewed as im-provement, Abstract: S.A.E. J. 70, 128 "
    "(July).",
    "Lachman, J. C, High temperatures thermocouples using tungsten-rhenium alloy tubing, S.A.E. "
    "Paper 524D, Abstract: S.A.E. J. 70, 102 (Sept.).",
    "Lachman, J. C, New developments in W/W-RE (tungsten/tungsten rhenium) thermocouples, ISA "
    "Trans. 1, 340.",
    "Ling, F. F., and T. E. Simkins, Measurement of point-wise junction condition of temperature "
    "at the interface of two-bodies in sliding contact, ASTIA AD-283 932.",
    "MacKenzie, D. J., and M. D. Scadron, Selection of thermocouples for high gas temperature "
    "measurement, S.A.E. Paper 524B, Abstract: S.A.E. J. 70, 102 (Sept.).",
    "Olsen, L. O., Catalytic effects of thermocouple materials, ASD-TDR-62-304; ASTIA AD-284 "
    "880; S.A.E. Paper 524G, Abstract: S.A.E. J. 70, 94 (May).",
    "Patzke, H., A new vacuum-thermocouple made by VEB Carl Zeiss Jena, Jena Rev. No. 1, 32.",
    "Stewart, P. J., Study of temperature distribution with rhodium-platinum thermocouple "
    "probes, Platinum Metals Rev. 6, 126 (Oct.).",
    "Walker, B. E., C. T. Ewing, and R. R. Miller, Thermoelectric instability of some noble "
    "metal thermocouples at high temperatures, Rev. Sci. Instr. 33, 1029 (Oct.).",
    "Walker, B. E., C. T. Ewing, and R. R. Miller, Thermoelectric instability of some noble "
    "metal thermocouples at high temperatures, U.S. Naval Res. Lab., Washington, D.C., Rept. "
    "5792 (June 29); ASTIA AD-282 154.",
    "White, F. J., Accuracy of thermocouples in radiant-heat testing, Exp. Mech. 2, 204 (July).",
    "Wolfe, R., and J. H. Wernick, Thermoelectric devices and materials. Bell Lab., Record 40, "
    "190 (June).",
    "Wormser, A. F., and R. A. Pfuntner, Thermocouple tells temperature above its melting point, "
    "S.A.E. J. 70, 56 (May).",
    "Zenin, A. A., Errors in the readings of thermocouples passed through flames, Inzh. Fiz. "
    "Zh. 5, 68 (May).",
    "A rhodium-platinum thermocouple for high temperature, Platinum Metals Rev. 6, 96 (July).",
    "Ambler, E., and H. Plumb, Use of carbon resistors as low temperature thermometers in the "
    "presence of stray r.f. (radio frequency) fields. Rev. Sci. Instr. 31, 656.",
    "Belinskii, L. I., and A. I. Pilorskii, Semiconductor thermometer, Instr. Construct. No. 10, "
    "25 (Oct.). Christiansen, W. H., The use of fine unheated wires in shock tubes, Phys. "
    "Fluids 3, 1027.",
    "Gniewek, J. J., and R. J. Corruccini, Carbon resistance thermometry with mixed dc and rf "
    "currents. Rev. Sci. Instr. 31, 899.",
    "Herr, A. C, H. G. Terbeck, and M. W. Tiefermann, Suitability of carbon resistors for field "
    "measurements of temperatures in the range of 35 to 100 degree R, NASA Tech. Note D-264 "
    "(Feb.).",
    "Kostryukov, V. N., Platinum thermometer for calorimetric work, Instr. Exp. Tech. No. 6, "
    "978 (Sept.).",
    "Leslie, W. H. P., J. J. Hunter, and D. Robb, Precision temperature measurement outside the "
    "laboratory. Research 13, 250 (July).",
    "Lockett, O. J., A clinical thermometer. Lancet 1, 1391.",
    "Lowenthal, G. C, and A. F. A. Harper, Resistance-temperature relationship of platinum at "
    "low temperatures and its influence on precision thermometry, Brit. J. Appl. Phys. 205 "
    "(May).",
    "Norton, H. N., Resistance elements for missile temperatures, Instr. Control Systems 33, "
    "922 (June).",
    "Obrowski, W., Platinum resistance thermometer for high temperatures, Platinum Metals Rev. "
    "4, 102.",
    "Pavlova, I. A., The use of semiconductor thermometers for measuring low temperatures, Proc. "
    "Intern. Congr. Refrig., 10th, Copenhagen 1959, 1, 410.",
    "Perelshina, A. P., The results of an experimental investigation of thermoelectromotive "
    "force in thermistors, Inzh. Fiz. Zh. 3, 119 (Apr.).",
    "Rogers, G. B., and F. A. Raal, Semiconducting diamonds as thermistors. Rev. Sci. Instr. 31, "
    "663.",
    "Sharven, Yu. V., Anthracite coal thermometers for various temperature ranges, Instr. Exp. "
    "Tech. No. 1, 153 (Jan.).",
    "Smith, R. W., An evaluation of thermistors: thermally sensitive semiconductors. General "
    "Motors Eng. J. 7, 14 (Oct.).",
    "Sterling, P. H., and H. Ho, Modern trends in resistance thermometry, Ind. Eng. Chem. 52, "
    "59A (July). Blue diamonds make rugged thermistors. Electronics 33, 78 (Aug.).",
    "Resistance thermometer claimed accurate to 1560 degree F, Prod. Eng. 31, 9 (Aug. 29).",
]


# ---------------------------------------------------------------------------
# Table 3 (source p. 38) - the only table whose data is present in the text layer
# ---------------------------------------------------------------------------
_TBL3_VI = [
    ["Lá kép", "Tốt", "Chi phí thấp, chắc chắn, dải rộng",
     "Chỉ đo tại chỗ hoặc đóng/ngắt On/Off"],
    ["Áp suất", "Trung bình", "Chính xác, dải rộng",
     "Cần bù nhiệt độ, hơi chất lỏng phi tuyến"],
    ["Điện trở", "Rất tốt", "Ổn định, dải rộng, chính xác",
     "Đáp ứng chậm, độ nhạy thấp, đắt, tự nóng, dải hẹp"],
    ["Thermistor", "Kém", "Chi phí thấp, nhỏ, độ nhạy cao, đáp ứng nhanh",
     "Phi tuyến, dải hẹp, tự nóng"],
    ["Cặp nhiệt điện", "Tốt", "Chi phí thấp, chắc chắn, dải rất rộng",
     "Độ nhạy thấp, cần điểm tham chiếu"],
    ["Bán dẫn", "Xuất sắc", "Chi phí thấp, nhạy, dễ giao tiếp",
     "Tự nóng, đáp ứng chậm, dải hẹp, cần nguồn cấp"],
]
_TBL3_EN = [
    ["Bimetallic", "Good", "Low cost, rugged, wide range",
     "Local measurement, or for On/Off switching only"],
    ["Pressure", "Medium", "Accurate, wide range",
     "Needs temperature compensation, vapor is nonlinear"],
    ["Resistance", "Very good", "Stable, wide range, accurate",
     "Slow response, low sensitivity, expensive, self-heating, range"],
    ["Thermistor", "Poor", "Low cost, small, high sensitivity, fast response",
     "Nonlinear, range, self-heating"],
    ["Thermocouple", "Good", "Low cost, rugged, very wide range",
     "Low sensitivity, reference needed"],
    ["Semiconductor", "Excellent", "Low cost, sensitive, easy to interface",
     "Self-heating, slow response, range, power source"],
]


def note_terms(lang):
    if lang == "vi":
        return ("<b>Thuật ngữ chính.</b> nhiệt kế — thermometer · đầu dò — probe · "
                "cặp nhiệt điện — thermocouple · RTD — Resistance Temperature Detector · "
                "thermistor — điện trở nhiệt · giê-cheo-nhiệt — thermowell · "
                "thanh hai kim loại — bimetal strip · thermopile — cặp nhiệt điện chồng · "
                "độ phát xạ — emissivity · hằng số thời gian nhiệt — thermal time constant · "
                "điểm đặt — set point · vòng lặp dòng — current loop · SSR — rơ le bán dẫn · "
                "điều chế độ rộng xung — PWM.")
    return ("<b>Key terms.</b> thermometer · probe · thermocouple · RTD · thermistor · "
            "thermowell · bimetal strip · thermopile · emissivity · thermal time constant · "
            "set point · current loop · SSR · PWM.")


# ===========================================================================
def _body(lang):
    vi = lang == "vi"
    b = []

    def P(v, e):
        b.append(p(v if vi else e))

    def H(v, e, lvl=h2):
        b.append(lvl(v if vi else e))

    def U(v, e):
        b.append(ul(v if vi else e))

    def FIG(n, fn):
        b.append(fig(n, fn))

    def EQ(body):
        b.append(eq(body))

    # ---------------------------------------------------------------- lead
    b.append(lead(
        "Chương này khảo sát phép đo nhiệt độ trong công nghiệp — từ nhiệt kế chất lỏng và "
        "thanh hai kim loại đến đầu dò điện, thiết bị không tiếp xúc, đầu ra hệ thống điều "
        "khiển, bộ phát và màn hình đọc, cùng các lưu ý khi lựa chọn và lắp đặt."
        if vi else
        "This chapter surveys temperature measurement in industry - from liquid-in-glass and "
        "bimetal thermometers to electrical probes, non-contact devices, control system "
        "outputs, transmitters and readouts, and considerations for selection and "
        "installation."))

    # ---------------------------------------------------------------- 1.1
    H("1.1 Giới thiệu", "1.1 Introduction")
    P("Nhiệt độ là thước đo trạng thái năng lượng nhiệt bên trong của một chất. Nó biểu thị "
      "năng lượng dao động chứa trong các phân tử của chất lỏng hoặc chất rắn, hay năng lượng "
      "tịnh tiến (tốc độ chuyển động) của các phân tử trong chất khí. Có nhiều thang nhiệt độ "
      "khác nhau để đo nhiệt độ. Thang được giới khoa học sử dụng là thang Kelvin. Zero tuyệt "
      "đối (0 K) biểu thị một chất không chứa năng lượng nhiệt nào, một điểm không thể đạt "
      "được. Điểm đóng băng của nước là 273,15 K và điểm sôi của nước là 373,15 K. Thang "
      "Celsius thực chất là thang Kelvin được dịch đi 273,15, tức lấy điểm đóng băng của nước "
      "làm gốc (273,15 K = 0 độ C). Trên thang Fahrenheit, nước đóng băng ở 32 độ F, sôi ở "
      "212 độ F, và zero tuyệt đối là -459,67 độ F.",
      "Temperature is a measure of the internal thermal energy state of a substance. It "
      "represents how much vibrational energy exists in the molecules of a liquid or solid, "
      "or the translational energy (speed of movement) of molecules in a gas. There are "
      "various temperature scales for measuring temperature. The one used by scientists is "
      "the Kelvin scale. Absolute zero (0 K) represents absolutely no thermal energy "
      "contained by a substance, a point which is impossible to achieve. The freezing point "
      "of water is at 273.15 K, and the boiling point of water is 373.15 K. The Celsius scale "
      "of temperature is just the Kelvin scale with an offset of 273.15, that is, referenced "
      "to the freezing point of water (273.15 K = 0 deg. C). On the Fahrenheit scale, the "
      "freezing point of water is 32 deg F, the boiling point of water is 212 deg. F, and "
      "absolute zero is at -459.67 deg. F.")
    P("Hiểu nhiệt độ cũng cần hiểu năng lượng. Nhiệt độ của một chất thay đổi tùy theo tốc độ "
      "nhận và mất năng lượng. Nhìn chung, tốc độ mất năng lượng phụ thuộc rất nhiều vào nhiệt "
      "độ. Một khi vật có nhiệt độ cao hơn môi trường xung quanh, nó mất năng lượng ra môi "
      "trường với tốc độ tăng dần theo hiệu nhiệt độ. Nhiệt độ không đổi thường có nghĩa là "
      "đang có cân bằng năng lượng, với tốc độ nhận và mất năng lượng bằng nhau.",
      "Understanding temperature requires understanding energy as well. The temperature of a "
      "substance will change depending upon the rates of energy gain and energy loss. "
      "Generally speaking, the rate of energy loss is very temperature dependent. Once "
      "something reaches a higher temperature than its surroundings, it loses energy to its "
      "surroundings at a rate that increases with that temperature difference. A constant "
      "temperature usually means there is energy equilibrium, with equal rates of energy gain "
      "and energy loss.")
    P("Đo nhiệt độ trong môi trường công nghiệp ngày nay bao hàm nhiều nhu cầu và ứng dụng "
      "rất đa dạng. Để đáp ứng hàng loạt nhu cầu đó, ngành điều khiển quá trình đã phát triển "
      "nhiều cảm biến và thiết bị. Nhiệt độ là biến rất quan trọng và được đo rộng rãi đối với "
      "hầu hết kỹ sư cơ khí. Nhiều quá trình phải có nhiệt độ được giám sát hoặc điều khiển. "
      "Phạm vi đó có thể từ việc giám sát đơn giản nhiệt độ nước của động cơ hoặc thiết bị tải, "
      "đến phức tạp như nhiệt độ của mối hàn trong ứng dụng hàn laser. Các phép đo khó hơn có "
      "thể kể đến nhiệt độ khí thải ống khói từ nhà máy phát điện hoặc lò cao, hay khí thải "
      "của tên lửa, có thể cần được giám sát. Phổ biến hơn nhiều là nhiệt độ của chất lỏng "
      "trong quá trình hoặc trong các ứng dụng phụ trợ, hoặc nhiệt độ của vật rắn như tấm kim "
      "loại, ổ bi và trục trong một cỗ máy.",
      "Temperature measurement in today's industrial environment encompasses a wide variety "
      "of needs and applications. To meet this wide array of needs the process controls "
      "industry has developed a large number of sensors and devices to handle this demand. "
      "Temperature is a very critical and widely measured variable for most mechanical "
      "engineers. Many processes must have either a monitored or controlled temperature. This "
      "can range from the simple monitoring of the water temperature of an engine or load "
      "device, or as complex as the temperature of a weld in a laser welding application. More "
      "difficult measurements such as the temperature of smoke stack gas from a power "
      "generating station or blast furnace or the exhaust gas of a rocket may be need to be "
      "monitored. Much more common are the temperatures of fluids in processes or process "
      "support applications, or the temperature of solid objects such as metal plates, "
      "bearings and shafts in a piece of machinery.")

    # ---------------------------------------------------------------- 1.2
    H("1.2 Lịch sử đo nhiệt độ", "1.2 The History of Temperature Measurement")
    P("Hiện nay có nhiều loại đầu dò đo nhiệt độ khác nhau, tùy vào đối tượng cần đo, độ chính "
      "xác yêu cầu, việc dùng để điều khiển hay chỉ để quan sát, và việc có thể chạm tới đối "
      "tượng hay không. Phép đo nhiệt độ có thể chia thành một số nhóm chung:",
      "There are a wide variety of temperature measurement probes in use today depending on "
      "what you are trying to measure, how accurately you need to measure it, if you need to "
      "use it for control or just man monitoring, or if you can even touch what you are trying "
      "to monitor. Temperature measurement can be classified into a few general categories:")
    U(["Nhiệt kế", "Đầu dò", "Không tiếp xúc"],
      ["Thermometers", "Probes", "Non-contact"])
    P("Nhiệt kế là nhóm cổ nhất. Nhu cầu đo và định lượng nhiệt độ của một vật bắt đầu vào khoảng "
      "năm 150 sau Công nguyên, khi Galen xác định “tính chất” (complexion) của một người dựa "
      "trên bốn đại lượng quan sát được. Khoa học “đo nhiệt” (thermometry) thực sự chỉ phát "
      "triển khi các ngành khoa học bùng lên vào những năm 1500; nhiệt kế đầu tiên là một "
      "air-thermoscope được mô tả trong Natural Magic (1558, 1589). Thiết bị này là tiền thân "
      "của dòng nhiệt kế thủy tinh hiện nay. Đến năm 1841 vẫn có 18 thang nhiệt độ khác nhau "
      "được sử dụng. Một thợ chế tạo dụng cụ, Daniel Gabriel Fahrenheit, đã học cách hiệu "
      "chuẩn nhiệt kế từ Ole Romer, một nhà thiên văn người Đan Mạch. Trong giai đoạn 1708 "
      "đến 1724 Fahrenheit bắt đầu chế tạo nhiệt kế theo thang của Romer, sau đó sửa đổi thành "
      "thang Fahrenheit mà ta biết hiện nay. Fahrenheit đã cải tiến nhiệt kế rất nhiều bằng "
      "cách đổi bình chứa thành dạng hình trụ và thay chất lỏng dùng trong các thiết bị ban đầu "
      "bằng thủy ngân, vì thủy ngân có tốc độ giãn nở nhiệt gần như tuyến tính. Kỹ thuật hiệu "
      "chuẩn của ông là bí mật thương mại, nhưng người ta biết ông dùng một hỗn hợp gồm điểm "
      "nóng chảy của muối biển, đá và nước, cùng nhiệt độ nách của một người khỏe mạnh làm các "
      "điểm hiệu chuẩn. Khi thang này được Anh Quốc chấp nhận, nhiệt độ 212 được định nghĩa là "
      "điểm sôi của nước. Điểm này cùng điểm nóng chảy của đá thường được dùng làm hai điểm "
      "hiệu chuẩn đã biết. Khoảng năm 1740 Anders Celsius đề xuất thang centigrade. Không rõ "
      "ai là người phát minh ra thang này, nhưng nó chia khoảng từ điểm nóng chảy của đá (100) "
      "đến điểm hơi của nước (0) thành 100 phần, vì thế gọi là “centigrade”. Linnaeus đảo ngược "
      "thang lại để 0 là điểm đá và 100 là điểm hơi. Năm 1948 tên thang centigrade được đổi "
      "thành Celsius.",
      "Thermometers are the oldest of the group. The need to measure and quantify the "
      "temperature of something started around 150 A.D. when Galen determined the "
      "'complexion' of someone based on four observable quantities. The actual science of "
      "'thermometry' did not evolve until the growth of the sciences in the 1500's the first "
      "actual thermometer was an air-thermoscope described in Natural Magic (1558, 1589). "
      "This device was the fore runner of the current class of glass thermometers. Up to 1841 "
      "there were 18 different temperature scales in use. An instrument maker, Daniel Gabriel "
      "Fahrenheit learned to calibrate thermometers from Ole Romer, a Danish astronomer. "
      "Between 1708 and 1724 Fahrenheit began producing thermometers using Romer's scale and "
      "then modified that to what we know to day as the Fahrenheit scale. Fahrenheit greatly "
      "improved the thermometer by changing the reservoir to a cylinder and replaced the "
      "spirits used in the early devices with mercury. This was done because it had a nearly "
      "linear rate of thermal expansion. His calibration techniques were a trade secret, but "
      "it was known that he used a certain mixture of the melting point of a mixture of sea "
      "salt, ice and water and the armpit temperature of a healthy man as calibration points. "
      "When the scale was adopted by Great Britain the temperature of 212 was defined as the "
      "boiling point of water. This point as well as the melting point of plain ice were used "
      "as two known calibration points. About 1740 Anders Celsius proposed the centigrade "
      "scale. It is not clear who invented the scale, but it divided the range of the melting "
      "point of ice (100) to the steam point of water (0) into 100 parts, hence 'centigrade'. "
      "Linnaeus inverted the scale so that 0 was the ice point and 100 was the steam point. In "
      "1948 the name of the centigrade scale was changed to Celsius.")
    P("Vào khoảng thời gian Fahrenheit thử nghiệm các thiết bị chứa chất lỏng, Jaspeh L. "
      "Gay-Lussac lại làm việc với các ống chứa khí. Ông kết luận rằng ở áp suất không đổi, "
      "thể tích khí giãn ra với một tỷ lệ nhất định cho mỗi độ tăng nhiệt độ, đó là 1/267 cho "
      "mỗi độ. Năm 1874 Victor Regnault thu được kết quả thử nghiệm tốt hơn, cho thấy con số "
      "đó là 1/273, và kết luận áp suất sẽ tiến về zero ở 1/273,15 độ C. Điều này dẫn đến định "
      "nghĩa áp suất zero tại -273,15 độ C, hay thang tuyệt đối mà ta biết hiện nay.",
      "About the time that Fahrenheit was experimenting with his liquid filled devices, "
      "Jaspeh L. Gay-Lussac was working with gas filled tubes. He concluded that at a "
      "constant pressure, the volume of the gas would expand at a particular rate for each "
      "degree of temperature rise, that being 1/267 per degree. In 1874 Victor Regnault "
      "obtained better experimental results, showing this number to be 1/273 and concluded "
      "that the pressure would approach zero at 1/273.15 degrees C. This lead to the "
      "definition of zero pressure at -273.15 degrees C, or what we now know as the absolute "
      "scale.")

    # ---------------------------------------------------------------- 1.3
    H("1.3 Nhiệt kế", "1.3 Thermometers")
    P("Nhiệt kế là dụng cụ dùng để đo nhiệt độ. Nhiệt kế analog gồm một ống được bịt kín, trên "
      "đó có các vạch chia. Các vạch này biểu thị nhiệt độ tăng dần theo Celsius hoặc "
      "Fahrenheit. Vạch chia trên nhiệt kế y tế và nhiệt kế thời tiết thì khác nhau, nhưng "
      "nguyên lý hoạt động giống nhau.",
      "A thermometer is an instrument we can use to measure temperature. An analog thermometer "
      "consists of a sealed tube with markings on it. These markings are increasing "
      "temperatures in Celsius or Fahrenheit. The markings on a clinical and weather "
      "thermometer are different, but they work in the same way.")

    H("Nhiệt kế ống thủy tinh", "Glass Tube Thermometers", h3)
    P("Hiện nay có rất nhiều loại nhiệt kế trên thị trường. Một số phép đo có độ chính xác rất "
      "cao vẫn được thực hiện bằng nhiệt kế thủy tinh. Vì tính chất của chất lỏng, đặc biệt là "
      "thủy ngân, đã được biết rõ, giới hạn duy nhất về độ chính xác và độ phân giải nằm ở "
      "khả năng chế tạo ống thủy tinh có lỗ khoan chính xác đến đâu. Một số nhà sản xuất đã "
      "chế tạo nhiệt kế có thang chia thay đổi cho các mục đích riêng. Một ví dụ là quá trình "
      "gọi là độ nhớt ướt (wet viscosity). Trong quá trình này, việc biết chính xác nhiệt độ "
      "của bể nước là rất quan trọng. Nhiệt kế thủy tinh vẫn được dùng vì khả năng lặp lại cực "
      "cao. Những nhiệt kế chuyên dụng này có lỗ khoan thu hẹp tại một điểm nhất định. Nhờ "
      "cách đó, một dải nhiệt độ rộng hai độ ở giữa thang có thể được kéo dài tới khoảng hai "
      "inch, cho phép đọc đến một phần mười độ C.",
      "There are a wide variety of thermometers available on the market today. Some highly "
      "precise measurements are still done with glass thermometers. Since the properties of "
      "fluids, and in particular, mercury are well known, the only limitation to accuracy and "
      "resolution come in the form of how well you can manufacture a glass tube with a "
      "precision bore. Some manufacturers have made thermometers that have variable scales for "
      "specific uses. One such use is a process called wet viscosity. In this process it is "
      "important to know the precise temperature of the water bath. The glass thermometer is "
      "still used because of it extreme repeatability. These specialized thermometers have a "
      "bore that narrows at a particular point. In this way it can expand a two degree "
      "temperature range in the middle of its scale to approximately two inches long, allowing "
      "readings down to a fraction of a tenth of a degree C.")
    P("Nhiều nhiệt kế hiện nay dùng chất lỏng khác thủy ngân vì nguy cơ thủy ngân bị đổ. Các "
      "thiết bị mới này dùng những chất lỏng được chế tạo để có tốc độ giãn nở riêng. Nhược "
      "điểm của các chất lỏng này là chúng thường không có khả năng chịu nhiệt độ cao như thủy "
      "ngân. Một nhược điểm lớn của nhiệt kế thủy tinh là khả năng chịu áp của thủy tinh có "
      "hạn. Ngoài ra, việc đưa bình cảm biến thủy tinh vào chất lỏng hoặc buồng có áp suất làm "
      "độ chính xác của nhiệt kế bị suy giảm. Điều này dẫn đến việc dùng “giê-cheo-nhiệt” "
      "(thermowell).",
      "Many of today's thermometers use fluids other than mercury due to the hazards of spilled "
      "mercury. These newer devices use other fluids that have been engineered to have "
      "specific rates of expansion. The drawback to these fluids is that they typically do not "
      "have the high temperature capabilities that mercury does. One major drawback of the "
      "glass thermometer is the limited pressure capacity of the glass. Also inserting the "
      "glass bulb into a pressurized fluid or chamber caused the accuracy of the thermometer "
      "to suffer. This led to the use of 'thermowells'.")
    FIG(1, F.fig_f01())
    P("Giê-cheo-nhiệt là một ống kim loại bịt kín một đầu, nhô vào trong buồng hoặc chất lỏng; "
      "nhiệt kế nằm trong ống này và tiếp xúc với thành ống.",
      "A thermowell is a closed end metal tube that sticks into the chamber or fluid, and the "
      "thermometer sits in this well, making contact with its sides.")

    H("Dải đo và độ chính xác", "Ranges and Accuracy", h4)
    P("Dải đo và độ chính xác khi đọc của nhiệt kế phụ thuộc vào kích thước lỗ khoan, chiều dài "
      "ống và loại chất lỏng bên trong. Nhìn chung, vạch chia càng nhỏ thì dải đo càng hẹp. Ví "
      "dụ, một nhiệt kế thủy ngân có độ chính xác 0,1 °C và dải đo 100 °C thường dài khoảng "
      "600 mm. Giới hạn nằm ở khả năng chế tạo thang đọc dễ nhìn của nhà sản xuất. Để tăng khả "
      "năng đọc, một số nhà sản xuất dùng thân nhiệt kế không tròn; góc bo tròn ở mặt đọc hoạt "
      "động như kính phóng đại, làm cột chất lỏng hiện rộng hơn và dễ đọc hơn. Nhiệt kế tròn "
      "vẫn là dạng tiêu chuẩn, với nhiều loại giá đỡ và vòng đệm phù hợp. Có cả ống bọc giáp "
      "bảo vệ để lắp nhiệt kế vào, cho phép sử dụng nhưng giảm nguy cơ vỡ.",
      "The range of a thermometer and it reading accuracy is dependent on the size of the hole, "
      "the length of the tube and the fluid in the thermometer. Typically the smaller the "
      "reading increment, the less range it will have. As an example, a 0.1° C accuracy mercury "
      "thermometer with a range of 100°C will typically be about 600 mm long. The restrictions "
      "rest with how well the maker can fabricate a readable scale. To increase readability "
      "some manufacturers have moved to non-round thermometer bodies, the rounded corner on the "
      "reading side acts as a magnifying glass, making the liquid column show up wider, and "
      "easier to read. The round thermometer is still the standard and there are a variety of "
      "holders and seals to fit them. There are also armored sleeves to put them in that allow "
      "them to be used, but reduce the chance of breakage.")
    P("Biểu đồ dưới đây liệt kê một số nhiệt kế có sẵn trên thị trường. Rõ ràng đây không phải "
      "tất cả nhiệt kế hiện có, mà chỉ là một lựa chọn hạn chế để bạn có ý tưởng về một số kích "
      "cỡ và dải đo phổ biến.",
      "The chart below lists some thermometers commercially available. These are clearly not "
      "all the thermometers available, but a limited selection to give you some idea of what "
      "some more standard sizes and ranges are.")
    P("Độ chính xác của nhiệt kế phụ thuộc rất nhiều vào quá trình chế tạo, nhưng cũng có thể bị "
      "ảnh hưởng bởi cách sử dụng. Như đã nêu ở trên, áp suất tác dụng lên bình cảm biến có thể "
      "ảnh hưởng đến kết đọc ở một mức độ nhất định. Mạnh hơn cả là mức độ nhúng vào chất lỏng "
      "có ảnh hưởng lớn đến độ chính xác. Hầu hết nhiệt kế thương mại đều có vạch khắc sẵn để "
      "cho biết độ sâu nhúng đã được hiệu chuẩn. Nhúng không đủ sâu sẽ cho kết đọc thấp, trong "
      "khi nhúng quá sâu sẽ cho kết đọc cao một cách giả tạo. Nhiệt kế không được thiết kế để "
      "nhúng hoàn toàn vào chất lỏng đang đo.",
      "The accuracy of a thermometer is greatly dependent on the manufacturing process, but "
      "also can be affected by usage. As stated earlier, the pressure exerted on the "
      "thermometer bulb can affect the reading to a certain degree. Even more so the amount of "
      "immersion in the fluid will have a drastic effect on the accuracy. Most commercial "
      "thermometers have lines etched in them to show you the calibrated depth of immersion. "
      "Failure to immerse the thermometer in deep enough will cause low readings, while putting "
      "it in too deeply will cause the readings to be artificially high. Thermometers are not "
      "designed to be totally immersed in the fluid they are measuring.")

    H("Điều khiển", "Controls", h4)
    P("Có thể dùng nhiệt kế ống thủy tinh để tạo một phần tử điều khiển. Bằng cách đặt một phần "
      "tử dẫn điện bên trong ống sao cho thủy ngân chạm vào nó ở điểm vận hành mong muốn, và "
      "đặt một tiếp điểm thứ hai trong thủy ngân ở đáy, bạn có một công tắc điện. Đã có thời "
      "gian những thiết bị này là thiết bị điều khiển chủ yếu, nhưng với sự ra đời của phần tử "
      "cảm biến điện tử chúng bị đẩy vào các kệ sau và góc bụi. Vẫn còn một số ứng dụng trong "
      "hóa học mà ở đó chúng hữu ích, vì phần tiếp xúc với vật liệu được đo — phần ngâm — chỉ "
      "là thủy tinh.",
      "It is possible to use the glass tube thermometer to create a control element. By placing "
      "a conductive element inside the glass tube, such that the mercury touches it at the "
      "desired operating point, and a second contact in the mercury at the bottom, you can "
      "create an electrical switch. There was a time when these were the predominant control "
      "device, but with the advent of electronic sensing elements these have been relegated to "
      "back shelves and dusty corners. There are still some applications in chemistry where "
      "these are useful, since the wetted portion, or portion that contacts the measured "
      "material, is only glass.")

    H("Nhiệt kế lá kép", "Bimetal Thermometers", h3)
    P("Nhiệt kế lá kép được thiết kế để kém chính xác hơn nhưng bền chắc hơn nhiệt kế thủy "
      "tinh. Trong nhiều ứng dụng công nghiệp vẫn có những nơi cần biết nhiệt độ của chất lỏng "
      "hoặc thiết bị, nhưng không đáng để tốn chi phí cho một đầu dò và màn hình đọc đắt hơn. "
      "Ví dụ là các vòng nước làm mát, bếp nướng gas, lò nung và lò sấy. Nhìn chung người dùng "
      "muốn kiểm tra nhanh nhiệt độ xấp xỉ, nhưng không cần biết đến hàng phần mười độ. Với "
      "hầu hết ứng dụng, sai số vài độ là hơn đủ. Nhiệt kế lá kép được cấu tạo từ một thanh cảm "
      "biến kim loại dẫn nhiệt tới phần tử nhiệt, bản thân phần tử nhiệt, và một thang đọc.",
      "The Bimetal thermometer was designed to be a less accurate, but more rugged measuring "
      "device than the glass thermometer. In many industrial applications there are still "
      "locations where it is desirable to know what the temperature of a fluid or device is, "
      "but it is not worth the cost of a more expensive probe and readout. Some examples of "
      "this are cooling water loops, gas grills, furnaces and ovens. In general the user would "
      "like a quick check to see what the approximate temperature is, but don't need to know to "
      "the tenth of a degree. Probably within a few degrees is more than enough for most of "
      "the applications. Bimetal thermometers are constructed of a metal sensing rod, which "
      "conducts the temperature to the thermal element, the thermal element and a scale.")
    P("Phần tử cảm biến lá kép gồm một kim loại được tạo dạng như một lò xo phẳng. Phần tử này là "
      "hai vật liệu kim loại khác nhau được ép với nhau. Khi phần tử cảm nhận nhiệt độ, các "
      "thành phần kim loại muốn giãn nở. Vì là những vật liệu khác nhau và giãn nở với tốc độ "
      "khác nhau, một ứng suất được tạo ra trong cuộn vật liệu. Ứng suất này làm phần tử cố quấn "
      "tròn quanh chính nó. Kim chỉ thị được gắn vào đầu của phần tử, hoặc trực tiếp hoặc qua "
      "cơ cấu. Chuyển động của vật liệu dạng lò xo làm kim chỉ thị dịch chuyển. Trước khi có "
      "bộ điều chỉnh nhiệt điện, công dụng phổ biến nhất của loại nhiệt kế này là trong hệ "
      "thống sưởi ấm gia đình. Bộ điều chỉnh nhiệt gồm một lò xo lá kép như dùng trong nhiệt kế "
      "kiểu đồng hồ và một công tắc, thường là công tắc thủy ngân. Khi lò xo quấn và mở theo "
      "thay đổi nhiệt độ, góc của công tắc thủy ngân thay đổi, đóng hoặc ngắt tiếp điểm. Nhiều "
      "ngôi nhà hiện nay vẫn dùng thiết bị này. Một vị trí điển hình khác để gặp loại nhiệt kế "
      "này là bếp nướng tại gia, hoặc nhiệt kế đặt trong lò sấy mà bạn mua. Nhiều loại có phần "
      "tử hở để bạn có thể nhìn và xem cấu tạo của chúng.",
      "The bimetal sensing element consists of a metal element shaped like a flat spring. This "
      "element is two different metallic materials sandwiched together. When a temperature is "
      "sensed by the element, the metallic components want to expand. Since they are different "
      "materials and expand at different rates, a stress in generated in the coil of material. "
      "This stress causes the element to try to wrap around itself. The indicator needle is "
      "attached to the end of this either directly or by mechanism. The motion of the spring "
      "shaped material moves the indicator. Prior to the advent of electrical thermostats, the "
      "most common use of these thermometers was in home heating systems. The thermostat "
      "consisted of a bimetallic spring such as used in the gage type thermometer and a switch, "
      "usually a mercury level switch. As the spring wound and unwound with temperature change, "
      "the angle of the mercury switch would change, closing or opening the contacts. These are "
      "still used in many homes today. Another typical location that you may find this type of "
      "thermometer is your home grill, or if you have purchased an in-oven thermometer. Many of "
      "these have exposed elements such that you can look and see how they are constructed.")

    H("Dải đo và độ chính xác", "Ranges and Accuracy", h4)
    P("Nhìn chung phần tử lá kép có thể rất chính xác. Chẳng hạn, bộ điều chỉnh nhiệt trong nhà "
      "thường chính xác đến khoảng một độ. Nhiệt kế kiểu mặt tròn hiện nay có nhiều kích cỡ, "
      "dải nhiệt và độ chính xác khác nhau. Một nhiệt kế bỏ túi nhỏ để kiểm tra hệ thống điều "
      "hòa không khí hoặc nấu ăn có mặt tròn đường kính khoảng một inch và dải nhiệt 0 đến 220 "
      "độ F. Chúng thường được chia theo bước hai độ. Các loại lớn hơn với mặt tròn 2, 3 thậm "
      "chí 5 inch thường chính xác đến 1% của dải đo. Có loại dải tới 1000 °F, nhưng dải quanh "
      "500 °F phổ biến hơn.",
      "In general the bimetallic element can be extremely accurate. Home thermostats, for "
      "instance, were typically accurate to one degree or so. Today's dial type come in a wide "
      "range of sizes, temperature ranges and accuracies. A small pocket thermometer for "
      "testing air conditioning systems or cooking has a dial about an inch in diameter and a "
      "temperature range of 0 to 220 degrees F. These are generally marked off in two degree "
      "increments. Larger units with 2, 3 or even 5” dial faces will typically be accurate to "
      "1% of the span of the unit. Ranges as high as 1000° F are available, however ranges "
      "around the 500° F value are more common.")
    P("Cũng như nhiệt kế thủy tinh, các thiết bị này cần một độ sâu nhúng nhất định vào môi "
      "trường được đo. Có một số “cấp” (grades) độ chính xác tiêu chuẩn được định nghĩa cho "
      "nhiệt kế lá kép. Bạn sẽ tìm thấy bản sao các tiêu chuẩn độ chính xác của nhiệt kế "
      "Ashcroft® trong phụ lục.",
      "As with glass thermometers, these devices expect a certain depth of immersion into the "
      "measured medium. There are a number of standard 'grades' of accuracy that are defined "
      "for bimetal thermometers. You will find a copy of the accuracy standards for Ashcroft® "
      "Thermometers included in the appendix.")

    H("Điều khiển", "Controls", h4)
    P("Hệ thống điều khiển sớm nhất dùng phần tử lá kép là các công tắc đơn giản. Chúng vẫn được "
      "dùng ở nhiều nơi cho đến nay, một số có thể khiến bạn bất ngờ. Bằng cách đặt phần tử lá "
      "kép ở vị trí mà chuyển động của nó có thể đóng hoặc ngắt một tiếp điểm, rồi nối dây vào "
      "cả phần tử lẫn tiếp điểm, bạn có một công tắc nhiệt đơn giản. Hình dưới đây cho thấy "
      "cấu hình đơn giản đó.",
      "The earliest control systems using bimetallic elements were simple switches. These are "
      "still in use today in many places, some of which may surprise you. By placing a "
      "bimetallic element in a location where its motion can make cause a contact to be made or "
      "broken, and attaching a wire to the element as well as the contact, you can create a "
      "simple temperature switch. The figure below shows this simple configuration.")
    FIG(2, F.fig_f02())
    P("Dễ thấy công tắc đơn giản như vậy có thể có nhiều ứng dụng. Về cơ bản đây là hệ vẫn được "
      "dùng hiện nay trong hầu hết máy điều hòa nhỏ và lò nướng gia đình. Bằng cách thay đổi khe "
      "hở tới tiếp điểm, có thể thay đổi nhiệt độ đặt để tiếp điểm đóng. Công tắc đơn giản mà "
      "hiệu quả này đã được dùng nhiều năm. Những nơi khác từng dùng rộng rãi và vẫn dùng là rơ "
      "le đèn báo rẽ ô tô và cầu dao điện. Việc bổ sung một phần tử gia nhiệt nhỏ quanh thanh lá "
      "kép và tạo cho nó một độ cong nhẹ để tác động là đóng “bật” thay vì đóng chậm, đã tạo ra "
      "một rơ le thời gian đơn giản mà hiệu quả. Lượng dòng chạy qua thanh lá kép quyết định "
      "nó nóng lên nhanh đến đâu và tác động nhanh đến đâu. Chính vì lý do này mà các xe đời cũ "
      "có đèn báo rẽ nhấp nháy nhanh hơn khi móc đoàn lôi hơn là khi không có. Thực ra đó là một "
      "tính năng an toàn được thiết kế có chủ đích. Nếu dòng chạy không đủ, tiếp điểm sẽ không "
      "bao giờ ngắt, làm đèn báo rẽ không hoạt động. Lý do phổ biến nhất gây thiếu dòng là một "
      "trong các bóng đèn bị cháy. Việc đèn báo rẽ không nháy là tín hiệu báo người lái cần bảo "
      "trì hệ thống đèn báo rẽ. Nhiều xe vẫn dùng hệ thống này, nhưng ở xe mới chúng đang bị "
      "thay bằng các đơn vị điện tử.",
      "It is easy to see how such a simple switch could have many applications. This system is "
      "basically what is still in use today in most small air conditioners and home ovens. By "
      "changing the gap to the contact, the set temperature at which it will make contact can "
      "be changed. This simple and effective switch has been used for years. Other locations "
      "where this has been used extensively, and still is, are automotive turn signal relays "
      "and electrical circuit breakers. The addition of a small heating element around the "
      "bimetal strip and forming it with a slight curve so the action is a 'snap' closure rather "
      "than a slow closure, a simple and effective timing relay was created. The amount of "
      "current flowing thru the bimetal strip controlled how quickly it heated and how fast it "
      "would trip. It is for this reason that earlier model cars had turn signals that flashed "
      "faster with trailers attached than without. This was actually a safety feature that was "
      "designed in. If there were inadequate current flow the contact would never break, "
      "preventing the 'blinkers' from functioning. The most common reason there was inadequate "
      "current flow was that one of the lamps was burned out. The lack of the turn signals "
      "blinking was an indicator for the operator to have the turn signals serviced. Many "
      "vehicles still use this system, however they are being with electronic units in newer "
      "vehicles.")
    P("Một vị trí khác mà thanh lá kép được dùng nhiều là cầu dao điện (circuit breaker). Cầu "
      "dao gồm hai phần: một nam châm điện để phát hiện quá tải nghiêm trọng và ngắt tải ngay "
      "lập tức, và một thanh lá kép để xử lý quá tải dòng nhỏ. Khi dòng chạy qua thanh, thanh bị "
      "uốn cong, nhả thanh giữ và cho cầu dao ngắt dòng. Cách này cũng được dùng tương tự trong "
      "nhiều hệ thống điều khiển motor.",
      "Another location that the bimetal strip is heavily incorporated is the electrical "
      "circuit breaker. The circuit breaker consists of two portions. An electromagnet to "
      "detect severe overloads and disconnect the load immediately and a bimetal strip to "
      "handle small current overloads. As current flows thru the strip it deflects, releasing "
      "the holding bar and allowing the breaker to interrupt the current flow. This is also "
      "used in many motor control systems in a similar fashion.")

    # ---------------------------------------------------------------- 1.4
    H("1.4 Đầu dò", "1.4 Probes")
    P("Sau sự phát triển của nhiệt kế, bước tiếp theo trong tiến hóa của phép đo nhiệt độ là "
      "sự phát triển của đầu dò nhiệt độ. Năm 1826 một nhà phát minh tên Becquerel đã dùng cặp "
      "nhiệt điện platinum-palladium đầu tiên. Trước thời điểm đó, mọi phép đo nhiệt độ đều "
      "dùng nhiệt kế chứa chất lỏng hoặc khí. Phát minh cặp nhiệt điện đã mở ra một làn sóng "
      "phát triển hoàn toàn mới, dẫn tới cái mà ngày nay ta gọi là nhiệt kế thực hành. Phần tử "
      "điện trở đó là thiết bị đầu tiên trong chuỗi các thiết bị không được xếp vào đầu dò hay "
      "bộ chuyển đổi. Chúng rơi vào ba nhóm chung:",
      "Following the development of the thermometer, the next step in the evolution of "
      "temperature measurement was the development of the temperature probe. In 1826 an "
      "inventor named Becquerel used the first platinum-vs-palladium thermocouple. Prior to "
      "this time all temperature measurement was done with liquid or gas filled thermometers. "
      "The invention of the thermocouple ushered in a whole new wave of development, "
      "culminating in what we know today as practical thermometry. This resistance element was "
      "the first in a series of devices that are not classified as probes or transducers. These "
      "fall into three general categories:")
    U(["Phần tử điện trở", "Cặp nhiệt điện chồng (thermopile)", "Bán dẫn"],
      ["Resistance elements", "Thermopiles", "Semiconductor"])
    P("Nhóm phần tử thứ nhất là lớp các phần tử điện trở. Thiết bị mà Becquerel dùng thực chất "
      "là một phần tử điện trở. Ngày nay thuật ngữ cặp nhiệt điện được dùng để mô tả các thiết "
      "bị sinh điện áp trong nhóm thermopile. Toàn bộ nhóm đầu dò này có khả năng đo nhiệt độ, "
      "nhưng chúng cũng cần thiết bị đo hoặc mạch bổ sung để đưa phép đo đó tới người dùng. "
      "Mạch bổ sung này có thể là các unit hiển thị được thiết kế riêng, thiết bị phòng thí "
      "nghiệm thông dụng, máy ghi dữ liệu hoặc hệ thống thu thập dữ liệu máy tính. Nhìn chung "
      "các thiết bị này đều mang tính điện tử, và kết đọc sẽ ở dạng điện trở, điện áp hoặc "
      "dòng, sau đó được tỷ lệ hóa và hiển thị bởi thiết bị đọc đầu dò.",
      "The first category of elements is the class of resistance elements. The device "
      "Becquerel used was actually a resistance element. Today the term thermocouple is used "
      "to describe the voltage creating devices in the thermopile classification. This whole "
      "classification of probes are capable of measuring temperature, but they also require "
      "additional instrumentation or circuitry to make that measurement available to a user. "
      "This additional circuitry can come in the form of specially designed display units, "
      "generic laboratory equipment, data loggers or computer data acquisition systems. In "
      "general these devices are all electronic in nature and the display will be in the form "
      "of a resistance, voltage, or current that is then scaled and displayed by the device "
      "reading the probe.")
    P("Hầu hết thiết bị có bảng hoặc đường cong hiệu chuẩn tiêu chuẩn để người dùng tra cứu "
      "nhiệt độ đã đo từ kết đọc điện mà đầu dò tạo ra.",
      "Most devices have standard tables or calibration curves that allow a user to look up "
      "the measured temperature given the electrical reading that the probe produces.")

    H("Phần tử điện trở", "Resistance Elements", h3)
    P("Phần tử điện trở là những đầu dò xuất hiện sớm nhất. Các nhà phát minh ban đầu đã hiểu "
      "mối quan hệ giữa nhiệt độ và điện trở của các vật liệu khác nhau. Điều này dẫn tới một "
      "chuỗi phần tử gọi là thermistor. Thermistor là một phần tử điện trở nhiệt thay đổi điện "
      "trở theo nhiệt độ. Độ thay đổi điện trở được xác định bởi ∆R = k∆T, trong đó ∆R là độ "
      "thay đổi điện trở, k là hệ số điện trở bậc nhất của vật liệu và ∆T là độ thay đổi nhiệt "
      "độ. Nhiệt độ được đo bằng cách cho một dòng một chiều nhỏ chạy qua thiết bị và đo sụt áp "
      "tạo ra.",
      "Resistance elements were the first probes that came into being. Early inventors understood "
      "the relationship between temperature and the resistance of different elements. This gave "
      "rise to a series of elements called thermistors. The thermistor is a thermal resistance "
      "element that changes resistance with temperature. The amount of resistance change is "
      "defined by ∆R = k∆T where ∆R is the resistance change, k is the first order coefficient "
      "of resistance of the material and ∆T is the temperature change. The temperature is "
      "measured by passing a small DC current thru the device and measuring the voltage drop "
      "produced.")
    EQ("&#916;R = k&#916;T")
    P("Loại thiết bị thứ hai trong nhóm này là RTD hay Resistance Temperature Detector (đầu dò "
      "nhiệt độ điện trở). RTD được phát triển sau thermistor để có độ chính xác cao hơn. "
      "Ngày nay RTD là một trong những thiết bị đo chính xác nhất hiện có. Thiết bị hoạt động "
      "dựa trên sự thay đổi điện trở của kim loại tinh khiết. RTD platinum là tiêu chuẩn cho "
      "các phần tử đo có độ chính xác cao. Những thiết bị này tuyến tính và chính xác hơn nhiều "
      "so với cặp nhiệt điện, nhưng đáp ứng chậm hơn và đắt hơn nhiều.",
      "The second type of device in this class is the RTD or Resistance Temperature Detector. "
      "The RTD was developed after the thermistor to obtain greater accuracy. Today the RTD is "
      "one of the most accurate measuring devices available. The device operates on the basis "
      "of changes of resistance of pure metals. The Platinum RTD is the standard for high "
      "accuracy measurement elements. These devices are much more linear and accurate than "
      "thermocouples, but they respond much slower and are much more costly.")

    H("Thermistor", "Thermistors", h3)
    P("Thermistor là điện trở nhạy nhiệt có chức năng chính là tạo ra sự thay đổi lớn, có thể "
      "dự đoán và chính xác về điện trở khi thân của nó thay đổi nhiệt độ tương ứng. Thermistor "
      "hệ số nhiệt âm (NTC) giảm điện trở khi nhiệt độ thân tăng, còn thermistor hệ số nhiệt "
      "dương (PTC) tăng điện trở khi nhiệt độ thân tăng. U.S. Sensor chế tạo thermistor có thể "
      "hoạt động trong dải nhiệt từ -100° đến trên +600° Fahrenheit. Nhờ đặc tính rất dễ dự "
      "đoán và độ ổn định lâu dài xuất sắc, thermistor được công nhận là cảm biến có lợi thế "
      "nhất cho nhiều ứng dụng, kể cả đo và điều khiển nhiệt độ.",
      "Thermistors are thermally sensitive resistors whose prime function is to exhibit a "
      "large, predictable and precise change in electrical resistance when subjected to a "
      "corresponding change in body temperature. Negative Temperature Coefficient (NTC) "
      "thermistors exhibit a decrease in electrical resistance when subjected to an increase "
      "in body temperature and Positive Temperature Coefficient (PTC) thermistors exhibit an "
      "increase in electrical resistance when subjected to an increase in body temperature. "
      "U.S. Sensor produces thermistors capable of operating over the temperature range of "
      "-100° to over +600° Fahrenheit. Because of their very predictable characteristics and "
      "their excellent long term stability, thermistors are generally accepted to be the most "
      "advantageous sensor for many applications including temperature measurement and "
      "control.")
    P("Từ khi Michael Faraday lần đầu quan sát thấy hệ số nhiệt âm của bạc sunfua vào năm 1833, "
      "công nghệ thermistor đã được cải tiến liên tục. Đặc tính quan trọng nhất của thermistor "
      "không gì khác là hệ số điện trở theo nhiệt độ cực lớn. Công nghệ thermistor hiện đại "
      "cho ra các thiết bị có đặc tính điện trở theo nhiệt độ cực kỳ chính xác, làm chúng trở "
      "thành cảm biến có lợi thế nhất cho nhiều ứng dụng.",
      "Since the negative temperature coefficient of silver sulphide was first observed by "
      "Michael Faraday in 1833, there has been a continual improvement in thermistor "
      "technology. The most important characteristic of a thermistor is, without question, its "
      "extremely high temperature coefficient of resistance. Modern thermistor technology "
      "results in the production of devices with extremely precise resistance versus "
      "temperature characteristics, making them the most advantageous sensor for a wide "
      "variety of applications.")
    P("Sự thay đổi điện trở của thermistor do nhiệt độ tương ứng thay đổi thể hiện rõ dù thân "
      "thermistor thay đổi nhiệt độ do dẫn hoặc bức xạ từ môi trường xung quanh, hay do “tự "
      "nóng” (self heating) gây ra bởi công suất tiêu tán bên trong thiết bị.",
      "A thermistor's change in electrical resistance due to a corresponding temperature "
      "change is evident whether the thermistor's body temperature is changed as a result of "
      "conduction or radiation from the surrounding environment or due to 'self heating' "
      "brought about by power dissipation within the device.")
    P("Khi thermistor được dùng trong mạch mà công suất tiêu tán bên trong thiết bị không đủ "
      "gây “tự nóng”, nhiệt độ thân thermistor sẽ theo nhiệt độ môi trường. Thermistor không bị "
      "“tự nóng” khi dùng cho các ứng dụng như đo nhiệt độ, điều khiển nhiệt độ hoặc bù nhiệt độ.",
      "When a thermistor is used in a circuit where the power dissipated within the device is "
      "not sufficient to cause 'self heating', the thermistor's body temperature will follow "
      "that of the environment. Thermistors are not 'self heated' for use in applications such "
      "as temperature measurement, temperature control or temperature compensation.")
    P("Khi thermistor được dùng trong mạch mà công suất tiêu tán bên trong thiết bị đủ gây “tự "
      "nóng”, nhiệt độ thân thermistor sẽ phụ thuộc vào độ dẫn nhiệt của môi trường cũng như "
      "nhiệt độ của nó. Thermistor được “tự nóng” cho các ứng dụng như phát hiện mức chất lỏng, "
      "phát hiện lưu lượng không khí và đo độ dẫn nhiệt.",
      "When a thermistor is used in a circuit where the power dissipated within the device is "
      "sufficient to cause 'self heating', the thermistor's body temperature will be dependent "
      "upon the thermal conductivity of its environment as well as its temperature. Thermistors "
      "are 'self heated' for use in application such as liquid level detection, air flow "
      "detection and thermal conductivity measurement.")

    H("Các loại thermistor", "Types of Thermistors", h4)
    P("Thermistor được chia thành hai loại dựa trên cách chúng phản ứng với sự thay đổi nhiệt "
      "độ:",
      "Thermistors are classified into two types based on how they behave with the change in "
      "temperature:")
    U(["Thermistor hệ số nhiệt âm (NTC)", "Thermistor hệ số nhiệt dương (PTC)",
       "Thermistor hệ số nhiệt âm (NTC)"],
      ["Negative Temperature Co-efficient (NTC) thermistors",
       "Positive Temperature Co-efficient (PTC) thermistors",
       "Negative Temperature Co-efficient (NTC) thermistors"])
    P("Điện trở của thermistor NTC giảm khi nhiệt độ tăng. Nói cách khác, dòng điện chạy qua "
      "thermistor NTC tăng khi nhiệt độ tăng.",
      "The resistance of the NTC (Negative Temperature Co-efficient) thermistors decreases "
      "with increasing temperature. In other words, the electric current flow through the NTC "
      "(Negative Temperature Co-efficient) thermistors increases with the increase in "
      "temperature.")
    P("Hầu hết thermistor NTC được làm từ một đĩa ép, thanh hoặc chip đúc từ vật liệu bán dẫn "
      "như oxit kim loại thiêu kết.",
      "Most of the NTC thermistors are made from a pressed disc, rod or cast chip of "
      "semiconductor material such as sintered metal oxides.")
    P("Ở thermistor NTC, các hạt mang điện được tạo ra nhờ quá trình pha tạp (doping). Nhờ quá "
      "trình pha tạp này mà một số lượng lớn hạt mang điện được tạo ra.",
      "In NTC thermistors, charge carriers are generated by doping process. Because of this "
      "doping process, a large number of charge carriers are generated.")
    P("Nếu nhiệt độ tăng nhẹ, một lượng lớn hạt mang điện (electron tự do) va vào electron hóa "
      "trị của các nguyên tử khác và cung cấp cho chúng đủ năng lượng. Electron hóa trị nhận đủ "
      "năng lượng sẽ phá vỡ liên kết với nguyên tử mẹ và di chuyển tự do từ chỗ này sang chỗ "
      "khác. Những electron di chuyển tự do như vậy được gọi là electron tự do. Chúng mang "
      "dòng điện khi di chuyển. Electron hóa trị trở thành electron tự do lại va vào các electron "
      "hóa trị khác và làm chúng trở thành tự do.",
      "If the temperature is slightly increased, a large number of charge carriers (free "
      "electrons) collides with the valence electrons of other atoms and provides them "
      "sufficient energy. The valence electrons which gains sufficient energy will breaks the "
      "bonding with the parent atom and moves freely from one place to another place. The "
      "electrons that move freely from one place to another place are called free electrons. "
      "These electrons carry the electric current while moving from one place to another place. "
      "The valence electron, which becomes a free electron will again collide with the other "
      "valence electrons and makes them free.")
    P("Cũng vì thế, chỉ một sự tăng nhẹ nhiệt độ cũng tạo ra hàng triệu electron tự do. Càng "
      "nhiều electron tự do hay hạt mang điện thì dòng điện càng lớn. Như vậy, một sự tăng nhẹ "
      "nhiệt độ sẽ làm giảm nhanh điện trở của thermistor NTC và cho phép một lượng lớn dòng "
      "điện chạy qua.",
      "Likewise, a small increase in temperature produces millions of free electrons. More "
      "free electrons or charge carriers means more electric current. Thus, a small increase "
      "in temperature will rapidly decrease the resistance of NTC thermistor and allows a "
      "large amount of electric current.")
    P("Điện trở của thermistor hệ số nhiệt dương (PTC) tăng khi nhiệt độ tăng. Hầu hết thermistor "
      "PTC được làm từ gốm đa tinh thể được pha tạp. Thermistor PTC còn được gọi là posistor.",
      "The resistance of Positive Temperature Co-efficient (PTC) thermistors increases with "
      "increase in temperature. Most of the Positive Temperature Co-efficient (PTC) "
      "thermistors are made from doped polycrystalline ceramic. Thermistors with Positive "
      "Temperature Co-efficient (PTC) are also called posistors.")

    H("Lịch sử thermistor", "History of Thermistors", h4)
    P("Thermistor NTC (Negative Temperature Co-efficient) đầu tiên được Michael Faraday phát "
      "hiện vào năm 1833. Ông quan sát thấy điện trở của bạc sunfua giảm nhanh khi nhiệt độ tăng.",
      "The first NTC (Negative Temperature Co-efficient) thermistor was discovered by Michael "
      "Faraday in1833. Michael Faraday observed that the resistance of silver sulfide decreased "
      "rapidly when the temperature is increased.")

    H("Dải đo và độ chính xác", "Range and Accuracy", h4)
    P("Như đã nêu, thermistor có thể có độ chính xác rất cao. Độ chính xác này bị giới hạn và "
      "ảnh hưởng bởi nhiều yếu tố. Thứ nhất là cấu trúc thực tế của vật liệu điện trở. "
      "Thermistor có thể là phần tử cảm biến chính xác nhất trên thị trường hiện nay. Dung "
      "sai chế tạo có thể tạo ra thermistor có độ chính xác và khả năng lặp lại thấp tới 0,1 °C "
      "hoặc cao tới 5 °C. Thường thì giá càng thấp thì độ chính xác càng kém. Một yếu tố lớn "
      "khác là lựa chọn mạch đọc thiết bị. Nếu dòng chạy qua thiết bị không đủ, nhiễu ngoài sẽ "
      "là vấn đề vì mức tín hiệu rất thấp. Nếu dòng quá cao, đầu dò bắt đầu tỏa nhiệt, làm dịch "
      "kết đọc nhiệt độ một cách giả tạo. Yếu tố quan trọng thứ ba là sự tuyến tính hóa của "
      "đồng hồ. Vì thermistor không phải thiết bị tuyến tính, hầu hết đồng hồ dùng một dạng "
      "thuật toán khớp đường cong đa thức để tạo công thức hiệu chuẩn nhiệt độ theo điện trở. "
      "Công thức này phụ thuộc rất nhiều vào việc hiệu chuẩn tại hiện trường. Một số đồng hồ "
      "cho phép bạn nhập vài điểm, từ đó máy tính toán giá trị đường cong. Dù thermistor là lựa "
      "chọn tốt cho các phép đo nhỏ không yêu cầu độ chính xác cao, được thực hiện với bộ xử lý "
      "nhỏ và điện tử chuyên dụng, nó không còn được coi là tiêu chuẩn trong đo nhiệt độ điện "
      "tử như trước. Dải nhiệt của thermistor thường chạy từ khoảng -80 °C đến +150 °C. Có một "
      "số thiết bị chuyên dụng có dải thấp hơn và cao hơn những giá trị này. Dải sử dụng của "
      "thermistor phụ thuộc vào khả năng tạo ra sự thay đổi điện trở hợp lý trên dải nhiệt rộng. "
      "Ví dụ, giá trị điện trở của đầu dò Omega 30KΩ dao động từ 884KΩ ở -40 °C tới thấp nhất "
      "500Ω ở +150 °C trên cùng một đầu dò. Đầu dò 3KΩ có dải từ 2,211MΩ ở -80 °C đến 55Ω ở "
      "+150 °C. Chắc bạn có thể tưởng tượng khó khăn thế nào khi tạo một hệ thống đo để đọc "
      "một dải giá trị rộng đến vậy mà vẫn tuân thủ giới hạn công suất tiêu tán. Vì lý do đó, "
      "hầu hết thermistor chỉ dùng trong dải rộng khoảng 100 °C. Cả hai thiết bị đều có độ chính "
      "xác ± 0,1 °C, nhưng con số này trở thành ± 0,2 °C với nhiệt độ trên 100 °C. Biểu đồ dưới "
      "đây cho thấy đường cong điện trở của đầu dò 3K.",
      "As stated earlier, thermistors can have very high accuracy. This accuracy is limited and "
      "influenced by a number of factors. The first is the actual construction of the resistor "
      "material. A thermistor can be the most accurate sensing element that is on the market "
      "today. The manufacturing tolerances can create thermistors with accuracy and "
      "repeatability as low as 0.1°C or as high as 5°C. Typically the lower cost the worse the "
      "accuracy. Another major factor is the selection of the circuitry to read the device. If "
      "insufficient current is flowed thru the device, external noise will be a problem because "
      "the signal levels will be very low. If the current is too high, the probe will start "
      "dissipating heat, artificially shifting the temperature reading. The third significant "
      "factor is the linearization of the meter. Since the thermistor is not a linear device, "
      "most meters will use some type of polynomial curve fit algorithm to create a calibrated "
      "formula of temperature vs resistance. This formula is highly dependent on the "
      "calibration done in the field. Some meters will allow you to enter several points, from "
      "which it will calculate its curve value. While the thermistor is a good choice for small "
      "measurements that do not require high precision, being done with a small processor and "
      "dedicated electronics, it is no longer considered the standard in electronic temperature "
      "measurement it once was. Temperature ranges for thermistors typically run from around "
      "-80°C to +150°C. There are some specialty units that have ranges down below and above "
      "these. The usable range for a thermistor is dependent on its ability to give reasonable "
      "resistance changes over a wide temperature change. As an example the values of "
      "resistance for the Omega 30KΩ probe range from 884KΩ at -40°C. to as low as 500Ω at "
      "+150°C on the same probe. The 3KΩ probe has a range of 2.211MΩ at -80°C to 55Ω at +150°C. "
      "I am sure you can imagine how difficult it would be to create a measurement system to "
      "read such a wide range of values, while still holding to the power dissipation "
      "limitations. For this reason most thermistors are used within a span of only about "
      "100°C. Both of these units are ± 0.1°C, however this changes to ± 0.2°C for temperatures "
      "above 100°C. The chart below shows the resistance curve for the 3K probe.")
    P("Thermistor đặc biệt hữu ích trong môi trường có sự thay đổi nhiệt độ nhỏ. Ví dụ, nếu bạn "
      "cần điều khiển một quá trình với dung sai rất chặt trong một dải nhiệt rất hẹp, chẳng "
      "hạn ± 10 °C, thermistor có thể là lựa chọn tốt nhất, nhất là ở dải nhiệt thấp. Dải nhiệt "
      "sử dụng thực tế của bất kỳ thermistor nào phụ thuộc vào cách chất nền bán dẫn của nó được "
      "tạo ra và mối quan hệ điện trở của nó như thế nào. Có thể cần đánh giá một số thiết bị "
      "để tìm loại có đặc tính mong muốn.",
      "The thermistor is particularly useful in small temperature change environments. As an "
      "example, if you need to control a process to a very tight tolerance over a very narrow "
      "temperature range, say ± 10°C, a thermistor may be your best choice, especially in lower "
      "temperature ranges. The actual usable temperature range of any thermistor is dependent "
      "on how its semiconductor substrate was created and what it resistance relationship is. A "
      "number of units may need to be evaluated to find one that has the desired "
      "characteristics.")

    H("Đầu dò nhiệt độ điện trở (RTD)", "Resistance Temperature Detector", h3)
    P("RTD hoặc là một màng kim loại lắng đọng trên một khung, hoặc là điện trở quấn dây, sau đó "
      "được bịt kín trong vật liệu composite gốm-thủy tinh. Hình 3 cho thấy RTD ba dây được bọc "
      "trong vỏ thép không gỉ để bảo vệ. Cuộn dây được quấn không cảm ứng. Khe hở giữa phần tử "
      "và vỏ được lấp bằng bột gốm để dẫn nhiệt tốt. Phần tử có ba dây dẫn, nhờ đó có thể hiệu "
      "chỉnh sụt áp trên dây dẫn. Điện trở của kim loại tinh khiết là dương, tăng tuyến tính theo "
      "nhiệt độ. Bảng 1 cho hệ số điện trở theo nhiệt độ của một số kim loại thường dùng trong "
      "nhiệt kế điện trở. Platinum là lựa chọn hàng đầu, tiếp theo là niken. Những thiết bị này "
      "rất chính xác — có thể đo được sự thay đổi nhiệt độ chỉ một phần nhỏ của độ. RTD có thể "
      "đo nhiệt độ từ −300° đến +1.400°F (−170° đến +780°C). Thời gian đáp ứng thường nằm giữa "
      "0,5 và 5 giây.",
      "RTDs are either a metal film deposited on a form or are wire-wound resistors, which are "
      "then sealed in a glass-ceramic composite material. Figure 3 shows a three-wire RTD "
      "encased in a stainless steel sheath for protection. The coil is wound to be "
      "non-inductive. The space between the element and the case is filled with a ceramic power "
      "for good thermal conduction. The element has three leads, so that correction can be made "
      "for voltage drops in the lead wires. The electrical resistance of pure metals is "
      "positive, increasing linearly with temperature. Table 1 gives the temperature "
      "coefficient of resistance of some common metals used in resistance thermometers. "
      "Platinum is the first choice, followed by nickel. These devices are accurate—temperature "
      "changes of a fraction of a degree can be measured. The RTD can be used to measure "
      "temperatures from −300° to +1,400°F (−170° to +780°C). The response time is typically "
      "between 0.5 and 5 seconds.")
    FIG(3, F.fig_f03())
    P("<b>Bảng 1.</b> Hệ số điện trở theo nhiệt độ của một số kim loại thường gặp (bảng gốc trong "
      "nguồn là hình ảnh, không có dữ liệu trong lớp văn bản).",
      "<b>Table 1.</b> Temperature Coefficient of Resistance of Some Common Metals (the source "
      "table is an image; its data is not present in the text layer).")
    P("Trong nhiệt kế điện trở, sự thay đổi điện trở theo nhiệt độ được cho bởi:",
      "In a resistance thermometer, the variation of resistance with temperature is given by:")
    EQ("R<sub>T2</sub> = R<sub>T1</sub> [1 + Coeff. (T<sub>2</sub> − T<sub>1</sub>)]")
    P("trong đó R<sub>T2</sub> là điện trở tại nhiệt độ T<sub>2</sub>, và R<sub>T1</sub> là điện "
      "trở tại nhiệt độ T<sub>1</sub>.",
      "where RT2 is the resistance at temperature T2, and RT1 is the resistance at temperature "
      "T1.")

    H("Thermopile (cặp nhiệt điện chồng)", "Thermopiles", h3)
    P("Thermopile là thiết bị nhiệt điện gồm một dãy các cặp nhiệt điện mắc nối tiếp. Nó được dùng "
      "rộng rãi trong các ứng dụng đo nhiệt độ không tiếp xúc và hệ thống giám sát nhiệt độ. "
      "Thermopile phát hiện nhiệt độ của một vật bằng cách hấp thụ bức xạ hồng ngoại (IR) phát ra "
      "từ bề mặt vật. Hầu hết đầu dò của thiết bị được trang bị bề mặt vật đen để hấp thụ bức xạ "
      "IR hiệu quả.",
      "A thermopile is a thermoelectric device that consists of an array of thermocouples "
      "connected in series. It is widely used in non-contact temperature measurement "
      "applications and temperature monitoring systems. Thermopiles detect the temperature of "
      "an object by absorbing the infrared(IR) radiation that emits from the object's surface. "
      "Most of the device's detectors are equipped with a black body surface for effectively "
      "absorbing the IR radiation.")
    P("Các cặp nhiệt điện tạo nên thermopile gồm hai dải kim loại khác nhau được hàn ở một đầu. Mỗi "
      "cặp nhiệt điện sinh một điện áp tỉ lệ với hiệu nhiệt độ giữa đầu “nóng” và đầu “lạnh”, "
      "được gọi là hiệu ứng Seebeck. Tuy nhiên, tổng điện áp đầu ra của thiết bị này cao hơn "
      "đáng kể so với một cặp nhiệt điện đơn.",
      "The thermocouples that make up a thermopile consist of two strips of different metals "
      "welded at one end. Each thermocouple produces a voltage that is proportional to the "
      "temperature difference between the «hot» and «cold» ends, which is known as the Seebeck "
      "effect. The total output voltage of one of these devices is considerably higher than "
      "that of a thermocouple, however.")
    P("Trong đầu dò thermopile, các “mối nối nóng” của cặp nhiệt điện hướng về phía bức xạ IR tới "
      "từ vật, trong khi các “mối nối lạnh” nối vào bộ tản nhiệt, thường là một đế silica. Khi "
      "đầu dò hướng về phía vật, nhiệt chảy từ vật sang thermopile. Dòng nhiệt này tạo ra hiệu "
      "nhiệt độ đáng kể giữa mối nối nóng và lạnh, góp phần tăng tín hiệu điện đầu ra của "
      "thermopile. Để đo dễ dàng tín hiệu đầu ra này, có thể dùng bộ khuếch đại đầu ra không nhiễu.",
      "In a thermopile detector, the 'hot junctions' of the thermocouples face the incident IR "
      "radiation from the object, whereas the 'cold junctions' are connected to a heat sink, "
      "which is usually a silica substrate. Once the detector is pointed toward the object, "
      "heat flows from the object to the thermopile. This heat flow creates a significant "
      "temperature difference between the hot and cold junctions, and this contributes to an "
      "increase in the output electric signal of the thermopile. In order to easily measure "
      "this output signal, a noise-free output amplifier can be used.")
    P("Trong cảm biến nhiệt, khi bức xạ IR từ vật bị cảm biến thermopile hấp thụ, các điện áp riêng "
      "của từng cặp nhiệt điện cộng lại tạo thành điện áp đầu ra cao. Hầu hết thermopile đều có "
      "thermistor tích hợp. Lý do là tín hiệu đầu ra tỉ lệ với hiệu nhiệt độ giữa vật và "
      "thermopile, và thermistor giúp ghi nhận nhiệt độ đó.",
      "In heat sensors, when the IR radiation from an object is absorbed by the thermopile "
      "sensor, the individual voltages of the thermocouples add up to generate a high output "
      "voltage. Most thermopiles have built-in thermistors. This is because the output signal "
      "is proportional to the temperature difference between the object and the thermopile, and "
      "a thermistor helps in registering the temperature.")
    P("Sự ra đời của công nghệ vi gia công trên nền silicon đã làm các đầu dò thermopile tiết "
      "kiệm chi phí trở nên dễ dàng có được. Chúng được dùng rộng rãi trong nhiều ngành. Trong "
      "số các ứng dụng có thể kể đến y tế như nhiệt kế tai, ứng dụng cảm nhận nhiệt như lò vi "
      "sóng và máy sấy tóc, và ứng dụng phát hiện khí như cảm biến CO2.",
      "The advent of silicon-based micromachining technology has lead to the easy availability "
      "of cost-effective thermopile detectors. These are widely used in a range of industries. "
      "Among other uses, they are used in medical applications such as ear thermometers, heat "
      "sensing applications such as microwave ovens and hair driers, and gas detection "
      "applications such as CO2 sensors.")
    FIG(4, F.fig_f04())
    P("Máy dò khí dùng thermopile để đo nồng độ khí trong không khí bằng hấp thụ IR. Chẳng hạn, "
      "cảm biến CO2 được dùng trong ứng dụng sưởi ấm, thông gió và điều hòa không khí (HVAC) để "
      "kiểm tra chất lượng không khí trong nhà (IAQ), hỗ trợ thông gió theo nhu cầu (DCV). Các "
      "máy dò khí này có nhiều ứng dụng công nghiệp, như phát hiện rò rỉ khí, đo hàm lượng CO2 "
      "trong bãi rác, giám sát hàm lượng CO2 trong hơi thở của bệnh nhân và ứng dụng báo cháy.",
      "Gas detectors employ thermopiles for measuring the concentration of gases in the "
      "atmosphere by IR absorption. For instance, CO2 sensors are employed in heating, "
      "ventilation, and air conditioning (HVAC) applications that check the indoor air quality "
      "(IAQ), facilitating demand controlled ventilation (DCV). These gas detectors have a "
      "broad range of industrial applications, such as detecting gas leaks, measuring the CO2 "
      "content of landfills, monitoring CO2 content in exhalation breath of patients, and fire "
      "alarm applications.")
    FIG(5, F.fig_f05())

    H("Cặp nhiệt điện", "Thermocouples", h3)
    P("Cặp nhiệt điện là cảm biến dùng để đo nhiệt độ. Cảm biến này gồm hai dây kim loại khác "
      "nhau, nối với nhau ở một đầu và nối tới nhiệt kế cặp nhiệt điện hoặc thiết bị khác có "
      "khả năng đo cặp nhiệt điện ở đầu kia. Khi được cấu hình đúng, cặp nhiệt điện có thể cho "
      "phép đo nhiệt độ trên dải rất rộng.",
      "A thermocouple is a sensor for measuring temperature. This sensor consists of two "
      "dissimilar metal wires, joined at one end, and connected to a thermocouple thermometer "
      "or other thermocouple-capable device at the other end. When properly configured, "
      "thermocouples can provide temperature measurements over wide range of temperatures.")
    P("Cặp nhiệt điện nổi tiếng về tính đa dụng như cảm biến nhiệt độ, nên được dùng trong nhiều "
      "ứng dụng — từ cặp nhiệt điện công nghiệp đến cặp nhiệt điện thông thường trong tiện ích "
      "và thiết bị gia dụng. Vì có nhiều mẫu mã và thông số kỹ thuật, điều cực kỳ quan trọng là "
      "phải hiểu cấu trúc cơ bản, nguyên lý hoạt động và dải đo để xác định đúng loại và vật "
      "liệu cặp nhiệt điện cho ứng dụng của bạn.",
      "Thermocouples are known for their versatility as temperature sensors therefore commonly "
      "used on a wide range of applications - from an industrial usage thermocouple to a "
      "regular thermocouple found on utilities and regular appliances. Due to their wide range "
      "of models and technical specifications, it is extremely important to understand its "
      "basic structure, how it works, its ranges as to better determine what is the right type "
      "and material of thermocouple for your application.")
    FIG(6, F.fig_f06())

    H("Nguyên lý hoạt động", "Working Principle", h4)
    P("Nguyên lý hoạt động của cặp nhiệt điện dựa trên ba hiệu ứng do Seebeck, Peltier và Thomson "
      "phát hiện. Đó là:",
      "The working principle of thermocouple is based on three effects, discovered by Seebeck, "
      "Peltier and Thomson. They are as follows:")
    U([
        "<b>Hiệu ứng Seebeck:</b> Khi hai kim loại khác nhau được nối tại hai mối nối, một "
        "suất điện động (emf) được sinh ra tại hai mối nối đó. Lượng emf sinh ra khác nhau "
        "với mỗi tổ hợp kim loại.",
        "<b>Hiệu ứng Peltier:</b> Khi hai kim loại khác nhau được nối để tạo hai mối nối, emf "
        "được sinh ra trong mạch do nhiệt độ khác nhau của hai mối nối.",
        "<b>Hiệu ứng Thomson:</b> Khi hai kim loại khác nhau được nối tạo thành hai mối nối, "
        "tồn tại điện thế trong mạch do gradient nhiệt độ dọc theo toàn bộ chiều dài của dây "
        "dẫn trong mạch.",
    ], [
        "<b>Seebeck effect:</b> The Seebeck effect states that when two different or unlike "
        "metals are joined together at two junctions, an electromotive force (emf) is generated "
        "at the two junctions. The amount of emf generated is different for different "
        "combinations of the metals.",
        "<b>Peltier effect:</b> As per the Peltier effect, when two dissimilar metals are joined "
        "together to form two junctions, emf is generated within the circuit due to the "
        "different temperatures of the two junctions of the circuit.",
        "<b>Thomson effect:</b> As per the Thomson effect, when two unlike metals are joined "
        "together forming two junctions, the potential exists within the circuit due to "
        "temperature gradient along the entire length of the conductors within the circuit.",
    ])
    P("Trong hầu hết trường hợp, emf do hiệu ứng Thomson sinh ra rất nhỏ và có thể bỏ qua bằng "
      "cách lựa chọn kim loại phù hợp. Hiệu ứng Peltier đóng vai trò nổi bật trong nguyên lý hoạt "
      "động của cặp nhiệt điện.",
      "In most of the cases the emf suggested by the Thomson effect is very small and it can be "
      "neglected by making proper selection of the metals. The Peltier effect plays a prominent "
      "role in the working principle of the thermocouple.")

    H("Cách hoạt động", "How it Works", h4)
    P("Khi hai dây gồm những kim loại khác nhau được nối ở cả hai đầu và một đầu bị nóng lên, có "
      "một dòng điện liên tục chạy trong mạch nhiệt điện. Nếu mạch bị cắt ở giữa, điện áp mạch hở "
      "ròng (điện áp Seebeck) là hàm của nhiệt độ mối nối và thành phần của hai kim loại. Nghĩa là "
      "khi mối nối của hai kim loại được nóng lên hoặc làm lạnh đi thì một điện áp được sinh ra "
      "có thể đối chiếu ngược lại với nhiệt độ.",
      "When two wires composed of dissimilar metals are joined at both ends and one of the ends "
      "is heated, there is a continuous current which flows in the thermoelectric circuit. If "
      "this circuit is broken at the center, the net open circuit voltage (the Seebeck voltage) "
      "is a function of the junction temperature and the composition of the two metals. Which "
      "means that when the junction of the two metals is heated or cooled a voltage is produced "
      "that can be correlated back to the temperature.")

    H("Các loại cặp nhiệt điện", "Thermocouple Types", h4)
    P("Cặp nhiệt điện có sẵn ở nhiều tổ hợp kim loại hay kiểu hiệu chuẩn khác nhau. Phổ biến nhất "
      "là các cặp nhiệt điện “kim loại cơ bản” (Base Metal) gọi là Loại J, K, T, E và N. Cũng có "
      "các kiểu hiệu chuẩn nhiệt độ cao — gọi là cặp nhiệt điện kim loại quý (Noble Metal) — Loại "
      "R, S, C và GB.",
      "Thermocouples are available in different combinations of metals or calibrations. The most "
      "common are the 'Base Metal' thermocouples known as Types J, K, T, E and N. There are also "
      "high temperature calibrations - also known as Noble Metal thermocouples - Types R, S, C "
      "and GB.")
    P("Mỗi kiểu hiệu chuẩn có dải nhiệt và môi trường riêng, dù nhiệt độ tối đa cũng thay đổi theo "
      "đường kính dây được dùng trong cặp nhiệt điện.",
      "Each calibration has a different temperature range and environment, although the maximum "
      "temperature varies with the diameter of the wire used in the thermocouple.")
    P("Dù kiểu hiệu chuẩn quyết định dải nhiệt, dải tối đa cũng bị giới hạn bởi đường kính dây. "
      "Nói cách khác, một cặp nhiệt điện rất mảnh có thể không đạt tới toàn bộ dải nhiệt.",
      "Although the thermocouple calibration dictates the temperature range, the maximum range "
      "is also limited by the diameter of the thermocouple wire. That is, a very thin "
      "thermocouple may not reach the full temperature range.")
    P("Cặp nhiệt điện Loại K được biết đến như cặp nhiệt điện đa dụng nhờ chi phí thấp và dải "
      "nhiệt của nó.",
      "K Type Thermocouples are known as general purpose thermocouple due to its low cost and "
      "temperature range.")

    H("Đầu dò bán dẫn", "Semiconductor Probes", h3)
    P("Đầu dò bán dẫn là nhóm chính thứ ba của đầu dò. Giống đầu dò điện trở, chúng cần nguồn "
      "dòng (hoặc điện áp) để tạo kết đọc. Điểm tương đồng chỉ dừng lại ở đó. Đầu dò bán dẫn được "
      "chế tạo từ một tấm bán dẫn chứa nhiều mạch tích cực. Có lẽ phổ biến nhất trong số này là "
      "thiết bị AD590 của Analog Devices. Mạch thực tế của thiết bị được cho thấy bên dưới.",
      "Semiconductor probes are the third main category of probe. Like a resistance probe, they "
      "require a current (or voltage) supply to create a reading. This is where the similarity "
      "ends. Semiconductor probes are created from a semiconductor wafer that contains a number "
      "of active circuits. Probably the most common of these are the Analog Devices AD590 "
      "Device. The actual circuit that the device consists of is shown below.")
    P("Về bản chất thiết bị này là phần tử có điện trở thay đổi theo nhiệt độ, sau đó chuyển sự "
      "thay đổi điện trở thành sự thay đổi dòng điện. Ở thiết bị cụ thể này, dòng đầu ra được "
      "điều khiển bằng 1µA/°K. Các thiết bị này thường không có độ chính xác như RTD do dung sai "
      "chế tạo, nhưng lại cực kỳ tiết kiệm chi phí cho ứng dụng số lượng lớn. Chúng có dung sai "
      "ban đầu hay độ lệch tuyệt đối tương đối lớn, nhưng điều đó được bù lại bằng độ lặp lại rất "
      "cao. Ví dụ, AD590K có thể sai tới ±2,5 °C ở 25 °C, nhưng một khi bạn biết độ lệch đó và "
      "hiệu chỉnh, thiết bị sẽ đo lặp lại trong vòng 0,1 °C. Nó làm được điều đó với chi phí "
      "8,95 USD (một linh kiện và 6,50 USD / 1000), và gần như không cần mạch khác trước khi tín "
      "hiệu nhiệt độ có thể dùng trong một mạch lớn hơn. MAX7500 của Dallas Semiconductor là "
      "phiên bản số hoàn toàn với sai số ±2 °C và đầu ra số 2 dây sẵn sàng giao tiếp với vi xử lý "
      "nhỏ. Thiết bị này còn rẻ hơn ở mức 0,65 USD (cho 1000 chiếc).",
      "This device is essentially a temperature variable resistance device, which then converts "
      "the change in resistance to a change in current. In this particular device, the "
      "controlled current output is equal to 1µA/°K. These devices do not typically have the "
      "accuracy that an RTD would due to the manufacturing tolerances, however they are "
      "extremely cost effective for large volume applications. The devices have a relatively "
      "large initial tolerance or absolute offset, but this is countered by a very high level of "
      "repeatability. As an example, an AD590K will vary as much as ±2.5°C at 25°C, but once you "
      "know what this offset is, you can adjust for it and the device will be able to make "
      "measurements that are repeatable to within 0.1°C. It will do this for a cost of $8.95 "
      "(Single part and $6.50 / 1000), and require virtually no other circuitry before the "
      "temperature signal can be used in a larger circuit. The Dallas semiconductor MAX7500 is "
      "a fully digital implementation with a ±2°C error, and a 2 wire digital output ready to "
      "interface to small microprocessors. This devise is even less expensive at $0.65 (per "
      "1000).")
    P("Ngoài AD590, thực sự có hàng trăm thiết bị bán dẫn xuất dữ liệu dưới dạng dòng, điện áp, "
      "thậm chí chuỗi bit số. National Semiconductor liệt kê 12 sản phẩm hiện hành, còn Dallas "
      "Semiconductor liệt kê 99 thiết bị. Hầu hết dựa trên cùng lý thuyết như AD590, nhưng ở nhiều "
      "dải nhiệt và loại đầu ra khác nhau. Tính đơn giản của thiết bị làm nó rất hữu ích cho các "
      "dụng cụ bù điểm đóng băng điện tử. Dù các thiết bị này nhìn chung hữu ích, cần cẩn thận "
      "trong thiết kế mạch để tránh phá hủy ngoài ý muốn thiết bị hoặc một phần hệ thống của bạn. "
      "Nhìn chung tốt nhất là nên lôi kéo kỹ sư điện yêu thích của bạn vào khi dùng thiết bị như "
      "vậy. Tuy nhiên, một người thử nghiệm tại nhà có thể dễ dàng dùng một cái cho hệ thống "
      "không quan trọng ở nhà, vì có nhiều ghi chú ứng dụng trên web hướng dẫn dùng chúng làm "
      "nhiệt kế gia đình và các thiết bị tương tự.",
      "In addition to the AD590, there are literally hundreds of semiconductor devices that "
      "output their data as either a current, a voltage or even a digital bit stream. National "
      "semiconductor shows 12 current products, and Dallas Semiconductor shows 99 devices. Most "
      "of these are based on the same theory as the AD590, but in a variety of temperature ranges "
      "and output types. The simplicity of this device makes it extremely useful for electronic "
      "ice point compensation devices. While these devices are generally useful, one should take "
      "care in designing the circuitry to prevent accidental destruction of the device or some "
      "section of your system. In general it is best to get your favorite Electrical Engineer "
      "involved when using a device like this. However, a backyard experimenter can easily use "
      "one for non-critical systems at home, as there are a wide variety of application notes "
      "available on the web, showing how to use these for home thermometers and such.")

    # ---------------------------------------------------------------- 1.5
    H("1.5 Thiết bị không tiếp xúc", "1.5 Non-Contact Devices")
    P("Nhóm cảm biến nhiệt độ không tiếp xúc gồm nhiều thiết bị chủ yếu là quang học. Tất cả đều "
      "hoạt động dựa trên một dạng đo truyền nhiệt bức xạ. Nhìn chung, mọi vật đều bức xạ nhiệt. "
      "Nhiệt này có thể được phát hiện dưới dạng bức xạ từ thiết bị. Bằng cách đo bức xạ đó, bạn "
      "xác định được nhiệt độ của thiết bị, không chỉ ở khoảng cách vài milimet mà còn ở khoảng "
      "cách hàng triệu năm ánh sáng. Dù hầu hết kỹ sư cơ khí không mấy quan tâm đến nhiệt độ của "
      "một ngôi sao cụ thể trong thiên hà khác, họ rất có thể muốn biết nhiệt độ của một miếng "
      "thép ra khỏi lò tôi. Chạy tới chạm vào miếng kim loại gần nóng chảy từng là phương pháp "
      "chính để đo nhiệt độ của nó. Ngày nay ta nhìn vào đặc trưng bức xạ của nó và xác định "
      "nhiệt độ.",
      "The non-contact temperature sensor category includes a wide variety of primarily optical "
      "devices. These all operate on some form of radiative heat transfer measurement. In "
      "general, all things radiate heat. This heat can be detected as a radiation from the "
      "device. By measuring this radiation, you can determine the temperature of the device, not "
      "only from a distance of a few millimeters, but also from millions of light years distant. "
      "While most mechanical engineers won't really care what the temperature of a particular "
      "star in another galaxy may be, they very well may want to know what the temperature of a "
      "piece of steel emerging from a heat treat furnace may be. Running up and touching the "
      "piece of nearly molten metal was once the primary method of measuring its temperature. "
      "Today we look at its radiation signature and determine the temperature.")

    H("Thiết bị đọc một điểm", "Single Reading Devices", h3)
    P("Nếu bạn muốn đo tiết kiệm nhiệt độ của một miếng thép ra khỏi lò, có lẽ bạn không quan tâm "
      "đến nhiệt độ chính xác của toàn bộ bề mặt. Một nhiệt độ chung của cả khối là đủ. Với mục "
      "đích này ta dùng thiết bị đọc một điểm. Thiết bị dạng này hoạt động bằng cách cho bức xạ "
      "chiếu tới một phần tử nhạy hồng ngoại. Bức xạ được hướng tới phần tử này qua một hệ thống "
      "thấu kính đơn giản. Các thấu kính này có thể tập trung bức xạ từ một điểm nhỏ cách hàng "
      "trăm feet hoặc một vùng lớn ngay sát. Những hệ thống này đòi hỏi bạn có hiểu biết nhất "
      "định về vật liệu đang cảm nhận. Độ phát xạ (emissivity) của vật liệu là một số giữa 0 và "
      "1, tính đến bước sóng, dải sóng, độ phản xạ, độ truyền qua, độ hấp thụ, hệ số hấp thụ "
      "v.v. Nó không giống với Tổng độ phát xạ (Total Emissivity). Độ phát xạ này được gọi là độ "
      "phát xạ quang phổ. Để có kết đọc chính xác với nhiệt kế bức xạ nhiệt, bạn cần có giá trị "
      "này. Cách dễ nhất là tra từ bảng. Phép đo bằng Nhiệt kế Bức xạ Hồng ngoại với hiệu chỉnh "
      "độ phát xạ gần như luôn cần thiết khi gặp hai điều kiện đơn giản sau:",
      "If you are looking to cost effectively measure the temperature of a piece of steel "
      "emerging from a furnace, you probably don't care what the exact temperature of the entire "
      "surface is. A general temperature of the chunk will probably be adequate. For this we use "
      "a single point reading device. This type of device works by allowing the radiation to "
      "strike an infrared sensitive element. The radiation is directed to this element by a "
      "simple system of lenses. These lenses can focus the radiation from a small spot hundreds "
      "of feet away or a large area from very close. These systems require that you have a "
      "certain knowledge of the material you are sensing. The emissivity of the material is a "
      "number between 0 and 1 that takes into account wavelength, waveband, reflectivity, "
      "transmissivity, absorptivity, absorption coefficient etc. This is not the same thing as "
      "Total Emissivity. This emissivity is referred to as spectral emissivity. In order to get "
      "an accurate reading with a thermal radiation thermometer you will need to have this "
      "value. They are most easily obtained from tables. An Infrared Radiation Thermometer "
      "measurement with an emissivity correction is almost always required when one meets two "
      "simple conditions:")
    U(["đối tượng quan tâm được dự kiến nóng hơn đáng kể so với môi trường xung quanh (và không "
       "có nguồn bức xạ IR khác phản xạ từ vật vào nhiệt kế, như ánh sáng mặt trời, đèn hồ quang "
       "hay đèn thạch anh); và",
       "khi bạn đủ tin rằng mình biết giá trị độ phát xạ quang phổ của vật (tất nhiên là nằm "
       "trong dải đáp ứng của nhiệt kế)."],
      ["the object of interest is expected to be significantly hotter than its surroundings "
       "(and there's no other source of IR radiation which can reflect off the object into the "
       "Thermometer, like sunlight, arc lamp or quartz lamp radiation etc.) and,",
       "when you are reasonably confident that you know the value of the spectral emissivity of "
       "the object (of course within the response waveband of the Thermometer)."])
    P("Bức xạ nhiệt từ môi trường sẽ được phản xạ từ vật đo, trừ những điều kiện rất đặc biệt, "
      "vào Nhiệt kế IR. Điều đó làm cảm biến đọc nhiệt độ cao giả tạo (độ lớn của sai số phụ thuộc "
      "vào nhiều yếu tố, trong đó có độ phản xạ của vật và sự khác biệt nhiệt độ giữa vật và môi "
      "trường xung quanh).",
      "The thermal radiation from the surroundings will be reflected from the object of "
      "measurement, except under the most unusual conditions, into the IR Thermometer. That "
      "results in the sensor reading a falsely high temperature (the magnitude of the error "
      "depends on several factors, not the least of which is the reflectivity of the object and "
      "the difference in temperature between the object and its surroundings).")
    P("Nếu bạn ở vị trí có thể dùng kiểu đo này, hãy dành thời gian đọc tài liệu hiện hành về độ "
      "phát xạ quang phổ để chắc rằng bạn hiểu cách cài đặt thiết bị, nếu không bạn chắc chắn sẽ "
      "nhận được những nhiệt độ ít hoặc không có giá trị.",
      "If you are in a position to use this type of measurement, spend a long time reading the "
      "current literature on spectral emissivity to be sure you understand how to set your "
      "instrument or you will most certainly get temperatures that are of little or no value.")

    H("Thiết bị dạng camera", "Camera Field Devices", h3)
    P("Thị trường hiện nay có nhiều thiết bị thuộc nhóm dạng camera. Những thiết bị này “nhìn” "
      "vào vật và hiển thị các nhiệt độ khác nhau mà nó thấy dưới dạng một hình ảnh. Chúng là "
      "biến thể của đầu dò tìm nhiệt (heat seeker) ban đầu được chế tạo cho mục đích tên lửa quân "
      "sự. Hãy nghĩ về thiết bị như một máy ảnh số, tương tự cái bạn có thể mua ở cửa hàng giảm "
      "giá địa phương. Phần tử CCD “nhìn” ánh sáng ở nhiều bước sóng khả kiến và trả kết quả về "
      "màn hình hoặc thẻ nhớ. Những bước sóng gần 700nm được trả về thành đỏ và cam, còn những "
      "bước sóng gần 450nm thành xanh dương và tím. Tâm trí ta nhìn những kết quả đó và nhận ra "
      "màu sắc. Thiết bị dạng camera nhiệt làm điều tương tự, nhưng ở dải bước sóng hồng ngoại "
      "(giữa 1mm và 750nm). Các hệ thống khác nhau làm việc ở dải khác nhau. Có hai dải thiết bị "
      "IR: IR xa (thường là những bước sóng dài hơn 1000nm) và IR gần (những bước sóng gần dải "
      "khả kiến hơn 1000nm). Cả hai loại đều hoạt động cùng cách, nhưng dùng thiết kế đầu dò hơi "
      "khác để thu thông tin ở bước sóng mong muốn.",
      "Today's market has a wide variety of devices that fall into the camera field area. These "
      "devices 'look' at objects and display the varying temperatures that it sees as an image. "
      "These devices are an adaptation of heat seeker heads originally created for military "
      "missile use. Think of the device as a digital camera, similar to what you might buy at "
      "your local discount store. The CCD element 'sees' light in a variety of visible "
      "wavelengths and returns the results of these findings to a display or memory card. Those "
      "wavelengths that are close to 700nm are returned as red's and oranges, and those closer "
      "to 450nm are returned as blues and violets. Our mind sees these results and recognizes "
      "these colors. The thermal camera style device does the same thing, but in the infrared "
      "wavelength range (between 1mm and 750nm). Different systems work in different ranges. Two "
      "ranges of IR device exist, far IR (typically those wavelengths longer than 1000nm) and "
      "near IR (those wavelengths closer to the visible range than 1000nm). Both of these "
      "devices work the same way, but use slightly different detector designs in order to "
      "obtain information in the desired wavelength.")
    P("Nguyên lý cơ bản giống như máy ảnh số, chỉ khác ở chỗ con chip máy tính nhìn vào tín hiệu "
      "từ ma trận đầu dò và chuyển nó thành tín hiệu mà mắt người hiểu được. Nhờ vậy ta có thể "
      "“nhìn” vào một hình ảnh về bức xạ hồng ngoại do các vật trong trường hình phát ra, với các "
      "bước sóng (nhiệt độ) khác nhau được hiển thị thành các cường độ hoặc màu sắc khác nhau.",
      "The basic principle is the same as the digital camera, with the single difference that "
      "the computer chip looks at the signal from the detector grid, and converts it to a signal "
      "that the human eye can understand. In this way we can 'look' at a picture of the infrared "
      "radiation being emitted by the bodies in the image field, with different wavelengths "
      "(temperatures) being displayed as different intensities or colors.")

    # ---------------------------------------------------------------- 1.6
    H("1.6 Đầu ra hệ thống điều khiển", "1.6 Control System Outputs")
    P("Thị trường hiện nay có hàng trăm tổ hợp màn hình đọc và bộ điều khiển nhiệt độ, từ bộ điều "
      "khiển bật/tắt một đầu vào đơn giản đến bộ điều khiển PWM nhiều kênh cao cấp. Việc chọn "
      "bộ điều khiển hoặc màn hình đọc phù hợp có thể là một nhiệm vụ đáng nản, càng khó hơn vì "
      "sự đa dạng của thuật ngữ và chức năng điều khiển. Danh sách dưới đây gồm những lựa chọn "
      "phổ biến nhất.",
      "Today's market has hundreds of combinations of temperature readouts and controllers, "
      "ranging from simple single input on/off controllers to high end multiple channel PWM "
      "controllers. Selecting the appropriate controller or readout can be a daunting task, "
      "made worse by the wide variety of terminology and control functions available. The list "
      "below includes the most common selections.")

    H("Điều khiển Bật/Tắt", "ON/OFF Control", h3)
    P("Đây là phương pháp điều khiển cơ bản nhất. Đầu ra của điều khiển đơn giản là được bật hoặc "
      "tắt khi cần để điều khiển quá trình. Thường thì thời gian đóng cắt dài hơn một giây. Quyết "
      "định khi nào bật hay tắt dựa trên thuật toán điều khiển trong bộ điều khiển. Đó có thể là "
      "bộ điều khiển tỉ lệ đơn giản, P/D (Tỉ lệ / Vi phân) hoặc PID (Tỉ lệ / Tích phân / Vi phân). "
      "Phần tử đầu ra thực tế thường là tiếp điểm rơ le đơn giản, đầu ra xung một chiều hoặc SSR "
      "(rơ le trạng thái rắn). Có thể dùng các lựa chọn khác như Triac hoặc SCR, nhưng thường "
      "chỉ các dân điện tử dùng đến.",
      "This method of control is the most basic control method. The output of the control is "
      "simply switched on or off as needed to control the process. Typically the switching "
      "duration will be longer than one second. The decision on when to turn on or off is based "
      "on the control algorithm in the controller. This can be a simple proportional controller, "
      "P/D (Proportional / Derivative) or PID (Proportional / Integral / Derivative) type. The "
      "actual output element would normally be either a simple relay contact, DC pulse output or "
      "SSR (Solid state relay). Other choices can be gotten such as a Triac or SCR, but normally "
      "these are only used by EE types.")

    H("Điều khiển PWM", "PWM Control", h3)
    P("Điều khiển PWM hay Điều chế độ rộng xung (Pulse Width Modulation) được dùng để điều khiển "
      "các thiết bị cao cấp. Tín hiệu PWM là đầu ra sóng vuông có tần số cố định, thay đổi thời "
      "gian bật của tín hiệu hay chu kỳ làm việc (duty cycle). Tín hiệu này thường là điện áp một "
      "chiều mức thấp trong dải 0 đến 5 volt hoặc 0 đến 24 volt. Cũng có thể dùng đầu ra dòng, "
      "chẳng hạn 4 đến 20 miliampe. Trong mỗi trường hợp, giá trị nhỏ nhất biểu thị trạng thái tắt "
      "và giá trị cao biểu thị trạng thái bật. Loại tín hiệu này thường dùng để điều khiển van "
      "hoặc bộ định vị.",
      "The PWM or Pulse Width Modulation control is used to control higher end devices. The PWM "
      "signal is a square wave output of a fixed frequency that varies the on duration of the "
      "signal or the duty cycle. This signal is typically a low level DC voltage signal in the "
      "rage of 0 to 5 volts or 0 to 24 volts. It can also be done in a current output such as 4 "
      "to 20 milliamps. In each of these cases the minimum value represents the off state and "
      "the high value represents the on state of the signal. This type of a signal is normally "
      "used to control valves or positioners.")
    P("Thường thì tần số cơ bản của kiểu điều khiển này nằm trong dải vài trăm hertz, nhưng có thể "
      "cao tới mười hoặc hai mươi nghìn hertz. Tần số này phụ thuộc vào bộ điều khiển cụ thể và "
      "nhu cầu của thiết bị được điều khiển. Tỷ lệ phần trăm bật của tín hiệu PWM tạo ra độ mở, "
      "độ đóng hoặc vị trí van mong muốn.",
      "Typically the base frequency of this type of control is in the range of a few hundred "
      "hertz, but can be as high as ten or twenty thousand hertz. This frequency is dependent "
      "on the particular controller and the needs of the device under control. The on percentage "
      "of the PWM signal generates the desired valve opening, closing or position.")

    H("Đầu ra tương tự", "Analog Output", h3)
    P("Phương pháp điều khiển đầu ra tương tự dùng một tín hiệu tương tự thay đổi, chẳng hạn 0-10 "
      "volt một chiều, tín hiệu -10 đến +10 volt hoặc tín hiệu dòng (0 đến 20 ma hoặc 4 đến 20 "
      "ma), làm đầu ra điều khiển. Tín hiệu này do bộ điều khiển tạo ra và, giống điều khiển PWM, "
      "mức tín hiệu tỉ lệ với lệnh của bộ điều khiển. Ví dụ, nếu bộ điều khiển tạo tín hiệu 0 đến "
      "10 volt, đầu ra 25% sẽ là 2,5 volt và đầu ra 50% là 5 volt. Tín hiệu này rất thường được "
      "dùng ở cấu hình đầu ra 4-20 miliampe, vì tín hiệu dưới 4 miliampe cho thấy đứt dây và có "
      "thể thực hiện một tác động điều khiển xác định để đưa hệ thống về trạng thái an toàn "
      "(fail-safe). Tín hiệu đầu ra này luôn là tín hiệu công suất rất thấp và cần khuếch đại "
      "công suất bổ sung ở đầu thiết bị điều khiển để tạo ra một tác động điều khiển thực tế.",
      "The analog output control method uses a variable analog signal, such as a 0-10 volt DC, "
      "-10 to +10 volt signal or current signal (0 to 20 ma or 4 to 20 ma) as the control output. "
      "This signal is generated by the controller, and similar to the PWM control the level is "
      "proportional to the controllers command signal. As an example, if the control was "
      "generating a 0 to 10 volt control signal, a 25% output would be 2.5volts, and a 50% "
      "control output would be 5 volts. This signal is very commonly used in a 4-20 milliamp "
      "output configuration since a signal below 4 milliamps indicates a line failure and a "
      "definite control action can be taken to put the system in a failed safe mode. This signal "
      "output is always a very low power signal and additional power amplification is required "
      "at the control device end to make an actual control move.")

    H("Đầu ra rơ le", "Relay Output", h3)
    P("Đầu ra điều khiển rơ le nói chung gồm tiếp điểm rơ le dạng C hoặc dạng A. Tiếp điểm rơ le "
      "thường có định mức dòng mười ampe trở xuống, và nhiều khi dưới một ampe. Kiểu điều khiển "
      "này là rẻ nhất trong các đầu ra điều khiển và chỉ hữu ích trong bộ điều khiển Bật/Tắt. "
      "Thời gian chu kỳ từ Bật sang Tắt thường cần dài hơn năm giây để tránh hỏng sớm rơ le. Có "
      "hai cách thể hiện tiếp điểm rơ le. Hình dưới cho thấy cả hai cách cho tiếp điểm dạng A và "
      "dạng C.",
      "The relay output control generally consists of a form C or form A relay contact. The "
      "relay contact generally has a current rating of ten amps or less, and many times less "
      "than one amp. This type of control is the least expensive of the control outputs and is "
      "only useful in and ON/OFF controller. The cycle time from ON to OFF usually needs to be "
      "something longer than five seconds to prevent premature failure of the relay. There are "
      "two ways in which the relay contact can be shown. The graphic below shows both methods "
      "for both a form A and form C contact.")

    H("Đầu ra xung một chiều", "DC Pulse Output", h3)
    P("Phương pháp đầu ra điều khiển này tạo một tín hiệu một chiều công suất thấp. Tín hiệu công "
      "suất thấp này được đưa tới một thiết bị điều khiển có khả năng biến tín hiệu đóng cắt công "
      "suất thấp thành tín hiệu công suất cao hoặc thành một giá trị điều khiển thực tế. Ví dụ, "
      "dùng tín hiệu đầu ra xung cho điều khiển bật/tắt, nối đến rơ le trạng thái rắn, có thể cho "
      "một bộ điều khiển đơn điều khiển hàng trăm nghìn watt công suất gia nhiệt. Nếu cùng tín hiệu đó "
      "được dùng trong hệ PWM, nó có thể điều khiển vị trí của những van có kích cỡ bằng xe hơi "
      "nhỏ. Bản thân tín hiệu nói cho thiết bị điều khiển biết phải làm gì, và thiết bị dùng "
      "thêm công suất để khuếch đại tín hiệu thành một thay đổi vật lý.",
      "This method of control output generates a DC signal that is of low power. The low power "
      "signal is fed to a control device that has the ability to turn the low power switching "
      "signal into either a high power signal or into an actual control value. For instance, "
      "using a pulse output signal for an on off control, wired to a solid state relay can allow "
      "a single controller to drive hundreds of thousands of watts of heating capacity. If this "
      "same signal is used in a PWM system, it can be used to control the position of valves the "
      "size of small cars. The signal itself tells the control device what to do, and the control "
      "device uses additional power to amplify this signal to a physical change.")

    H("Đầu ra SSR", "SSR Output", h3)
    P("Đầu ra rơ le trạng thái rắn (SSR) là phiên bản bán dẫn xoay chiều của tiếp điểm dạng A. Tức "
      "là nó hoặc bật hoặc tắt. Đầu ra SSR chỉ đóng cắt tải xoay chiều và thường bị giới hạn ở "
      "dòng tối đa 5 ampe. Nếu cần dòng lớn hơn, nên dùng SSR ngoài. Cần lưu ý một điểm: rơ le "
      "trạng thái rắn chỉ đóng cắt tải xoay chiều và chỉ tắt khi điện áp ở phía đường dây của rơ "
      "le đi qua zero. Điều này chỉ xảy ra hai lần trong mỗi chu kỳ. Vì lý do đó, việc cài thời "
      "gian bật/tắt ngắn hơn 1/60 giây sẽ cho kết quả không mong đợi. Điều đó cũng có nghĩa là "
      "nếu bạn chọn thời gian dài hơn và dùng phương pháp điều khiển PWM, thời gian độ rộng xung "
      "(T2) sẽ luôn ở bội của 16 mili giây. Điều này đúng ngay cả khi bạn dùng hệ điều chế độ rộng "
      "xung một chiều để điều khiển SSR ngoài. Nhìn chung nên đặt thời gian T1 của bất kỳ hệ PWM "
      "hoặc Bật/Tắt nào điều khiển SSR không nhỏ hơn một giây.",
      "The solid state relay output is an AC semiconductor version of a form A contact. That "
      "being it is either on or off. The solid state relay output will switch ONLY alternating "
      "current loads and will typically be limited to a maximum current of 5 amps. If larger "
      "currents are required, an external SSR is recommended. One caution to note. Solid state "
      "relays will switch only an alternating current load, and will only turn off as the voltage "
      "on the line side of the relay crosses zero. This only happens twice in each cycle. For "
      "this reason, setting an on/off time of less than 1/60th of a second will produce "
      "unexpected results. It also means that if you select a longer time and are using a PWM "
      "method of control the pulse width time (T2) will always be in 16 millisecond increments. "
      "This holds even if you are using a DC pulse width system to control an external SSR. In "
      "general it is a good idea to set your T1 time of any PWM or ON/OFF system driving an SSR "
      "to not less than one second.")

    H("Điều khiển tỉ lệ", "Proportional Control", h3)
    P("Thuật toán điều khiển cơ bản nhất cho bất kỳ thiết bị nào là đo một tín hiệu lệnh rồi trừ "
      "đi một tín hiệu phản hồi, tạo ra tín hiệu sai số. Tín hiệu sai số này được khuếch đại một "
      "lượng nhất định. Lượng đó gọi là HỆ SỐ KHUẾCH ĐẠI (GAIN). Khi tín hiệu phản hồi lệch xa "
      "tín hiệu lệnh hơn, tín hiệu sai số nhân GAIN lớn dần theo tỉ lệ. Đó là tín hiệu tạo ra đầu "
      "ra điều khiển. Trong điều khiển Bật/Tắt, khi tín hiệu tỉ lệ vượt quá một giới hạn quy định "
      "thì đầu ra bị tắt; khi tín hiệu nhỏ hơn một mức nhất định thì đầu ra được bật. Đây là "
      "phương pháp điều khiển điển hình cho hệ gia nhiệt. Dùng điều khiển tỉ lệ với tín hiệu PWM "
      "hoặc tín hiệu tương tự tạo hệ thống hiệu quả hơn. Trong chế độ này, mức độ lệch khỏi điểm "
      "đặt làm thay đổi độ rộng xung hoặc đầu ra tương tự. Sai số càng lớn thì đầu ra thay đổi "
      "càng nhiều. Đó là bản chất của điều khiển tỉ lệ: đầu ra thay đổi tỉ lệ với tín hiệu sai số.",
      "The most basic control algorithm for control of any device, is to measure a command "
      "signal and subtract a feedback signal from it, creating an error signal. This error "
      "signal is amplified by a certain amount. This amount is known as GAIN. As the feedback "
      "signal varies farther from the command signal, the error x GAIN signal grows "
      "proportionally larger. This is the signal that generates the control output. In the case "
      "of ON/OFF control, when the proportional signal grows higher than a specified limit, the "
      "output is turned off. When the signal grows smaller than a certain amount, it turns the "
      "output on. This is a typical control method for a heater system. Using a Proportional "
      "control with a PWM or analog signal makes a more efficient system. In this control mode "
      "the amount of deviation from the set point changes the pulse width or analog output. The "
      "higher the error signal, the more the output signal is changed. This is the essence of "
      "proportional control. The output is changed proportionally to the error signal.")

    H("PD (Điều khiển Tỉ lệ – Vi phân)", "PD (Proportional – Derivative Control)", h3)
    P("Nếu bạn muốn thay đổi nhanh tín hiệu đầu ra với một sự thay đổi nhỏ hơn của tín hiệu sai "
      "số, hệ thống sẽ giữ nhiệt độ tốt hơn đôi chút. Vấn đề là trong phương pháp này điều khiển "
      "có xu hướng vượt quá (overshoot), hay nâng nhiệt độ cao hơn mong đợi vì nó nóng nhanh hơn "
      "để tới điểm đặt nhanh hơn. Tốc độ thay đổi của tín hiệu phản hồi được gọi là đạo hàm của "
      "tín hiệu. Nếu tín hiệu phản hồi lệch quá nhanh, có nguy cơ vượt quá giá trị mong muốn. Bằng "
      "cách tính đến tốc độ thay đổi của tín hiệu, ta biết cần làm chậm đầu ra điều khiển để giảm "
      "hiện tượng đó. Đạo hàm của phản hồi được trừ vào sai số để giảm thiểu điều này. Thuật toán "
      "điều khiển mới sẽ có dạng đại loại:",
      "If you want to change the output signal quickly with a smaller change in the error signal "
      "you will get the system to hold the temperature somewhat better. The problem is that in "
      "this method the control has a tendency to overshoot, or raise the temperature higher than "
      "desired because it is heating faster to get to the set point faster. The rate of change "
      "of the feedback signal is known as the derivative of the signal. If the feedback signal "
      "deviates too quickly, there is a chance we will overshoot the desired value. By taking "
      "the rate of change of the signal into account we know we need to slow down the control "
      "output some to reduce this. The derivative of the feedback is subtracted from the error "
      "to minimize this. The new control algorithm would look something like:")
    EQ("(Lệnh − phản hồi) × PropGain − Đạo hàm(phản hồi) × DGain")
    P("(Command – feedback) × PropGain – Derivative (feedback) × DGain",
      "(Command – feedback) × PropGain – Derivative (feedback) × DGain")

    H("PID (Tỉ lệ – Tích phân – Vi phân)", "PID (Proportional – Integral – Derivative)", h3)
    P("Điều khiển PID đẩy điều khiển PD đi xa hơn một bước. Vì bộ điều khiển PD thực sự có thể ổn "
      "định ở điểm đặt khác với điểm đặt mong muốn, do tác động vi phân nếu hệ số khuếch đại tỉ "
      "lệ quá thấp, ta cần thêm một phần tử nữa để chắc rằng nó tới được điểm đó. Tác động vi "
      "phân chỉ hoạt động khi phản hồi đang thay đổi. Nếu hệ số khuếch đại tỉ lệ không đủ cao, hệ "
      "thống sẽ vui vẻ ổn định ở đâu đó gần nhưng không phải ở điểm điều khiển mong muốn. Tích "
      "phân là một tổng theo thời gian. Trong trường hợp này, đó là tổng của các sai số trong một "
      "khoảng thời gian. Nếu hệ thống ổn định ở điểm thấp hơn điểm đặt, chẳng hạn, sẽ vẫn còn tín "
      "hiệu sai số (lệnh – phản hồi). Dù sai số nhỏ, vì tích phân là tổng theo thời gian, giá trị "
      "tích phân bắt đầu tích lũy và lớn dần theo thời gian. Nếu thêm số hạng mới này vào thuật "
      "toán điều khiển hiện có, ta sẽ thấy đại loại như sau:",
      "The PID control takes the PD control one step farther. Since the PD controller can "
      "actually settle at a set point different than the desired set point, due to the "
      "derivative action if the proportional gain is too low, we need to add an additional "
      "element to make sure that it gets there. The derivative action only works while the "
      "feedback is changing. If the proportional gain is not high enough the system will "
      "happily settle some place near, but not at, the desired control point. An integral is a "
      "sum over time. In this case it is the sum of the errors over a period of time. If the "
      "system has settled at a point below the set point, for instance, there will be some "
      "remaining error signal (command – feedback). Even if this error is small, since the "
      "integral is a sum over time, the integral value will begin building, and over time grow "
      "larger. If one were to add this new term to the existing control algorithm we would see "
      "something like the following:")
    P("Theo thời gian, tổng sai số tăng cho đến khi đầu ra bị ép phải dịch chuyển, lại huy động số hạng "
      "vi phân. Giá trị tích phân thường được nhập dưới dạng một giá trị thời gian để tích lũy. "
      "Con số này thường nhỏ, vài giây hoặc ngắn hơn tùy quá trình.",
      "As time passes the sum of the error grows until the output is forced to move, calling "
      "into play the derivative term once again. The integral value is generally entered as a "
      "time value for it to sum over. This number is usually small, some number of seconds or "
      "shorter depending on the process.")

    # ---------------------------------------------------------------- 1.7
    H("1.7 Bộ phát và màn hình đọc", "1.7 Transmitters and Readouts")
    P("Ngoài các bộ điều khiển, còn có nhiều thiết bị thuộc nhóm bộ phát và màn hình đọc. Những "
      "thiết bị này được đặt gần bộ chuyển đổi (transducer), và một tín hiệu được đưa ra có thể "
      "sử dụng ở các khoảng cách khác nhau từ bộ chuyển đổi. Ba loại đầu ra bộ phát phổ biến "
      "nhất là:",
      "In addition to controllers, there are a wide variety of devices that fall in the category "
      "of transmitters and readouts. These devices are placed in close proximity to the "
      "transducer and an signal is output that is capable of being used at varying distances "
      "from the transducer. The three most common transmitter outputs are:")
    U(["Số (Digital)", "Vòng dòng (Current loop)", "Điện áp (Voltage output)"],
      ["Digital", "Current loop", "Voltage output"])
    P("Mỗi đầu ra có ưu và nhược điểm riêng. Khi chọn bộ phát phù hợp, hai tiêu chí chính cần "
      "xem xét là khoảng cách và môi trường phải đi qua, và loại thiết bị nhận dữ liệu ở đầu kia "
      "của đường dây.",
      "Each of these outputs have their advantages and disadvantages. When selecting an "
      "appropriate transmitter the two main criteria that need to be considered are the distance "
      "and environment being traversed, and the type of device receiving the data on the other "
      "end of the line.")

    H("Bộ phát đầu ra số", "Digital Output Transmitters", h3)
    P("Bộ phát đầu ra số là nhóm thiết bị đọc tín hiệu tương tự từ bộ chuyển đổi và chuyển nó "
      "thành tín hiệu dữ liệu số có thể gửi qua dây truyền dữ liệu tới hệ thống từ xa. Chúng khác "
      "nhau rất nhiều về độ phức tạp và cũng về chi phí. Dù là loại đắt nhất trong dòng bộ phát, "
      "chúng cũng là loại linh hoạt nhất. Hai giao thức truyền chính là multi-drop và Ethernet. "
      "Trong cả hai trường hợp, dữ liệu tương tự phải được chuyển sang dạng số. Việc này thường "
      "được thực hiện bằng một hệ vi xử lý nhúng nhỏ và chip chuyển đổi tương tự-số. Ở một số hệ "
      "thống, chip A/D cũng được nhúng luôn trong chip xử lý. Cả hai hệ thống đều cần đáng kể "
      "mạch bổ sung cho truyền thông, làm giá cao hơn đáng kể so với các phương pháp khác.",
      "Digital output transmitters are a class of devices that read the analog signal from a "
      "transducer and convert it to a digital data signal that can be sent over a data "
      "transmission wire to a remote system. These vary greatly in complexity and also cost. "
      "While these are the most expensive of the transmitter series, they are also the most "
      "flexible. The two primary transmission protocols are multi-drop and Ethernet. In either "
      "case the analog data must be converted to a digital format. This is typically done with "
      "a small embedded processor system and an analog-to-digital conversion chip. In some "
      "systems this A/D chip is embedded in the processor chip as well. Both of these systems "
      "require a significant overhead in additional circuitry for the communications, causing "
      "the price to be significantly higher than other methods.")

    H("Multi-Drop", "Multi-Drop", h4)
    P("Hệ truyền multi-drop dùng một bộ dây có khả năng nối nhiều hơn một bộ phát cùng lúc. Sơ đồ "
      "dưới cho thấy một hệ multi-drop đơn giản với ba thiết bị nhiệt độ và bộ phát cùng một máy "
      "tính điều khiển duy nhất.",
      "Multi-drop transmission systems use a set of wires that are capable of connecting more "
      "than one transmitter at a time. The diagram below shows a simple multi-drop system with "
      "three temperature devices and transmitters and a single control computer.")
    P("Trong sơ đồ này, bạn dễ thấy máy tính điều khiển có thể nói chuyện và lấy dữ liệu từ nhiều "
      "thiết bị. Dù về lý thuyết bạn có thể có bất kỳ số thiết bị nào trên đường dây, giới hạn thực "
      "tế là 128 thiết bị. Các thiết bị giao tiếp với máy tính ở dạng điện áp vi sai để giảm ảnh "
      "hưởng của nhiễu trên đường truyền. Hai định dạng phổ biến nhất là RS-422 (cáp 4 dây) và "
      "RS-485 (cáp 2 dây). Không nên nhầm lẫn cả hai với RS-232, cổng truyền thông điểm-điểm đơn "
      "lẻ có trên hầu hết máy tính. Cả RS-422 và RS-485 đều cần một card hoặc bộ chuyển đổi đặc "
      "biệt để máy tính làm việc được.",
      "In this diagram you can easily see that the control computer can talk to and take data "
      "from a number of devices. While in theory you can have any number of devices on the line, "
      "the practical limit is 128 devices. The devices communicate with the computer in a "
      "differential voltage mode format to reduce the effects of noise on the communications "
      "lines. The two most common formats for this are RS-422 (4 wire cable) and RS-485 (2 wire "
      "cable). Neither of these should be confused with RS-232, which is the single point to "
      "point communications port found on most computers. Both RS-422 and RS-485 communications "
      "require a special card or converter for the computer to work with it.")
    P("Hai dạng này cũng có giới hạn chiều dài thực tế. Có thể dùng tới 4000 feet cáp với tốc độ "
      "truyền dữ liệu tối đa 56 kilobyte mỗi giây. Với tốc độ cao hơn, nên dùng chiều dài dưới "
      "1500 feet. Cả hai định dạng đều được coi là dạng thăm dò (polled). Điều này có nghĩa là "
      "máy tính phải hỏi từng thiết bị “kết đọc của bạn là bao nhiêu” và thiết bị trả lời “kết "
      "đọc hiện tại của tôi là xxx”. Một số thiết bị thông minh hơn có thể được lập trình để lưu "
      "kết đọc theo một khoảng nhất định, chẳng hạn một lần mỗi giây. Máy tính sau đó có thể yêu "
      "cầu toàn bộ dữ liệu, rồi xóa đi để dành chỗ lưu thêm. Một thiết bị đọc đơn RS-422 điển "
      "hình có giá khoảng 300 USD.",
      "There are practical length limits to both of these forms as well. It is possible to use "
      "up to 4000 feet of cable with a maximum data rate of 56 kilobytes per second data "
      "transfer rate. For higher data rates lengths of less than 1500 feet are recommended. "
      "Both formats are considered a polled format. This means that the computer must ask each "
      "device 'what is your reading' and the device will return 'my current reading is xxx'. "
      "Some smarter devices can be programmed to save readings at a particular interval, say "
      "once each second. The computer can then ask for all of its data, which it then can erase "
      "to make room to save more. A typical RS-422 single reading device will cost around $300.")

    H("Thiết bị Ethernet", "Ethernet Devices", h4)
    P("Người mới vào thị trường là nhóm thiết bị Ethernet. Việc đưa điện toán phân tán vào đã mở "
      "đường cho hệ điều khiển phân tán trong nhà máy và xưởng sản xuất. Khả năng của Ethernet "
      "hỗ trợ hàng nghìn thiết bị, cùng mức độ thông minh đáng kể tại các vị trí điều khiển, làm "
      "cho nó thành công nghệ rất hữu ích cho nhà máy quy mô lớn. Sơ đồ dưới cho thấy một hệ mạng "
      "Ethernet đơn giản.",
      "The newest entry into the market is the class of Ethernet devices. The incorporation of "
      "distributed computing has opened the door to distributed control systems in process "
      "plants and factories. The ability of Ethernet to support thousands of devices, and to "
      "have a significant amount of intelligence at the control locations, make this a very "
      "useful technology for large scale plants. The diagram below shows a simple Ethernet "
      "network system.")
    P("Trong hệ Ethernet, máy tính có thể từ xa lấy dữ liệu từ nhiều loại phần tử cảm biến và "
      "điều khiển nhiều loại phần tử tương đương. Một số bộ phát tương đối không thông minh, chỉ "
      "trả lời vài lệnh đơn giản và trả dữ liệu của mình, trong khi số khác có thể được lập trình "
      "với các vòng điều khiển và quy trình phân tích phức tạp trước khi chuyển dữ liệu về hệ "
      "máy tính điều khiển chính. Tính linh hoạt lớn này cho phép nhiều lựa chọn, nhưng kèm chi "
      "phí. Một hệ National Instruments Compact Rio với 4 đầu vào cặp nhiệt điện, 4 đầu vào RTD "
      "và 4 tín hiệu điều khiển đầu ra dòng sẽ có giá gần 3500 USD.",
      "In the Ethernet system the computer can remotely take data from a wide array of sensing "
      "elements, and control an equally wide variety of elements. Some transmitters will be "
      "relatively unintelligent, just responding to a few simple commands and returning its "
      "data, while other can be programmed with control loops and complex analysis routines "
      "before ever passing their data back to the main control computer system. This vast "
      "flexibility allows for a wide variety of options, but at a cost. A National Instruments "
      "Compact Rio system with 4 thermocouple inputs, 4 RTD inputs and 4 current output control "
      "signals will cost nearly $3500.")

    H("Bộ phát đầu ra dòng", "Current Output Transmitters", h3)
    P("Bộ phát tương tự phổ biến nhất là thiết bị đầu ra dòng. Thiết bị này chuyển tín hiệu từ đầu "
      "dò thành một đầu ra đã tỷ lệ hóa được truyền trên đầu ra 4 đến 20 miliampe. Trong một hệ "
      "bộ phát điển hình, bộ phát đọc đầu vào của thiết bị và tính đầu ra tỷ lệ phù hợp. Ví dụ, "
      "đầu vào nhiệt độ 0 đến 500°F được tỷ lệ hóa thành 4 đến 20 ma. Điều này có nghĩa là đầu "
      "vào 100°F được truyền dọc dây như một dòng 7,2 ma.",
      "The most common analog style transmitter is the current output device. This device will "
      "convert the signal from the probe into a scaled output that is transmitted on a 4 to 20 "
      "milliamp output. In a typical transmitter system, the transmitter reads the device input "
      "and calculates what the appropriate scaled output should be. As an example, a 0 to 500°F "
      "Temperature input would be scaled from 4 to 20 ma. This means that a temperature input of "
      "100°F would be transmitted down the wires as a current of 7.2ma.")
    P("Hệ vòng dòng hoạt động trên đường dây dài tới 10.000 feet và khá miễn nhiễm với nhiễu cảm "
      "ứng trên dây. Chúng cũng khá kinh tế. Một bộ phát dòng tuyến tính đơn giản của Omega có "
      "giá khoảng 100 USD mỗi cái.",
      "Current loop systems work over long wire runs, up to 10,000 feet, and are fairly immune "
      "to noise induced on the wires. They are also fairly economical. A simple linear current "
      "transmitter from Omega will cost around $100 each.")
    P("Ở đầu nhận, máy tính phải chuyển tín hiệu này về dạng nó dùng được. Cách phổ biến nhất là "
      "cho dòng chạy qua một điện trở chính xác và đo điện áp sinh ra trên điện trở bằng một thẻ "
      "thu thập dữ liệu.",
      "On the receiving end the computer must convert this signal back into something it can "
      "use. The most common method is to flow the current thru a precision resistor and measure "
      "the voltage generated across the resistor with a data acquisition card.")

    H("Bộ phát đầu ra điện áp", "Voltage Output Transmitters", h3)
    P("Hầu hết bộ phát đầu ra điện áp được dùng cho khoảng cách khá ngắn. Đường dây rất dễ bị "
      "nhiễu và chỉ hữu ích trên quãng ngắn. Công dụng phổ biến nhất của loại bộ phát này là từ "
      "màn hình đọc trong phòng điều khiển tới máy tính ghi dữ liệu. Điều này cung cấp cho người "
      "vận hành một kết đọc nhiệt độ trực quan, đồng thời cung cấp đầu ra đã tỷ lệ hóa cho máy "
      "tính xử lý. Ở một số lắp đặt, máy tính là thiết bị duy nhất nhìn thấy dữ liệu, và dựa trên "
      "dữ liệu đó sẽ hiển thị thông báo hoặc giá trị cho người vận hành. Những bộ phát và màn "
      "hình đọc này hữu ích, có giá từ hơn một trăm đến vài trăm USD. Bộ phát và đầu ra chế độ "
      "điện áp cực kỳ nhạy với nhiễu cảm ứng và chỉ nên dùng trong ứng dụng điện yên tĩnh và "
      "ngắn (dưới 50 feet).",
      "Most voltage output transmitters are intended for fairly short distance use. The lines "
      "are very susceptible to noise and are useful only over short distances. The most common "
      "use for these types of transmitters are from a readout in a control room environment to "
      "a data logging computer. This provides the operator with a visual reading of the "
      "temperature, as well as providing a scaled output to the computer for processing. In some "
      "installations, the computer is the only device seeing the data, and based on that data, "
      "will display messages or values to the operator. These transmitters and readouts are "
      "useful and range from a little over a hundred dollars to several hundred dollars. "
      "Voltage mode transmitters and outputs are extremely susceptible to induced noise, and "
      "should only be used in electrically quiet and short distance (less than 50 feet) "
      "applications.")

    # ---------------------------------------------------------------- 1.8
    H("1.8 Lưu ý khi ứng dụng", "1.8 Application Considerations")
    P("Có nhiều thiết bị để đo nhiệt độ. Việc lựa chọn thiết bị do nhu cầu của ứng dụng quyết "
      "định. Một sự so sánh các đặc tính của thiết bị đo nhiệt độ được đưa ra. Các vấn đề về hằng "
      "số thời gian nhiệt, lắp đặt, hiệu chuẩn và bảo vệ cũng được thảo luận.",
      "Many devices are available for temperature measurement. The selection of a device will be "
      "determined by the needs of the application. A comparison of the characteristics of "
      "temperature-measuring devices is given. Thermal time constant considerations, "
      "installation calibration, and protection also are discussed.")

    H("Lựa chọn", "Selection", h3)
    P("Trong điều khiển quá trình có nhiều lựa chọn cảm biến nhiệt độ. Tuy nhiên, dải đo, tính "
      "tuyến tính và độ chính xác yêu cầu có thể thu hẹp lựa chọn. Khi quyết định cuối cùng về cảm "
      "biến, có thể phải xét thêm các yếu tố khác như chỉ thị từ xa, hiệu chỉnh sai số, hiệu "
      "chuẩn, nhạy rung, kích thước, thời gian đáp ứng, tuổi thọ, yêu cầu bảo trì và chi phí. "
      "Không nên làm giảm chất lượng lựa chọn thiết bị trong instrumentation chỉ vì lý do chi "
      "phí. Điều khiển quá trình chỉ tốt bằng chính các phần tử giám sát của nó.",
      "In process control, a wide selection of temperature sensors is available. However, the "
      "required range, linearity, and accuracy can limit the selection. In the final selection "
      "of a sensor, other factors may have to be taken into consideration, such as remote "
      "indication, error correction, calibration, vibration sensitivity, size, response time, "
      "longevity, maintenance requirements, and cost. The choice of sensor devices in "
      "instrumentation should not be degraded from a cost standpoint. Process control is only "
      "as good as the monitoring elements.")

    H("Dải đo và độ chính xác", "Range and Accuracy", h3)
    P("Bảng 2 cho dải nhiệt và độ chính xác của các cảm biến nhiệt độ; độ chính xác thể hiện ở đây "
      "là khi hiệu chỉnh sai số ở mức tối thiểu. Trong một số trường hợp dải có thể được mở rộng "
      "nhờ dùng vật liệu mới. Bảng 3 tóm tắt các đặc tính của cảm biến nhiệt độ.",
      "Table 2 gives the temperature ranges and accuracies of temperature sensors, the "
      "accuracies shown are with minimal error correction. The ranges in some cases can be "
      "extended with the use of new materials. Table 3 gives a summary of temperature sensor "
      "characteristics.")
    P("<b>Bảng 2.</b> Dải nhiệt và độ chính xác của cảm biến nhiệt độ (bảng gốc là hình ảnh, không "
      "có dữ liệu trong lớp văn bản).",
      "<b>Table 2.</b> Temperature Range and Accuracy of Temperature Sensors (the source table "
      "is an image; its data is not present in the text layer).")
    P("<b>Bảng 3.</b> Tóm tắt đặc tính cảm biến.",
      "<b>Table 3.</b> Summary of Sensor Characteristics.")
    b.append(table(["Loại", "Tuyến tính", "Ưu điểm", "Nhược điểm"] if vi else
                   ["Type", "Linearity", "Advantages", "Disadvantages"],
                   _TBL3_VI if vi else _TBL3_EN))

    H("Hằng số thời gian nhiệt", "Thermal Time Constant", h3)
    P("Đầu dò nhiệt không phản ứng ngay với sự thay đổi nhiệt độ. Thời gian phản ứng của cảm biến, "
      "hay hằng số thời gian nhiệt, là thước đo thời gian để cảm biến ổn định bên trong theo sự "
      "thay đổi nhiệt độ bên ngoài, và được xác định bởi khối lượng nhiệt và điện trở dẫn nhiệt "
      "của thiết bị. Kích thước bình cảm biến, kích thước đầu dò hoặc giế-cheo-nhiệt bảo vệ đều "
      "có thể ảnh hưởng đến thời gian đáp ứng của kết đọc. Ví dụ, bình lớn chứa nhiều chất lỏng "
      "hơn để độ nhạy tốt hơn, nhưng điều đó làm tăng hằng số thời gian để đáp ứng đầy đủ một sự "
      "thay đổi nhiệt độ.",
      "A temperature detector does not react immediately to a change in temperature. The "
      "reaction time of the sensor, or thermal time constant, is a measure of the time it takes "
      "for the sensor to stabilize internally to the external temperature change, and is "
      "determined by the thermal mass and thermal conduction resistance of the device. "
      "Thermometer bulb size, probe size, or protection well can affect the response time of "
      "the reading. For example, a large bulb contains more liquid for better sensitivity, but "
      "this will increase the time constant to fully respond to a temperature change.")
    P("Các phương trình của nguồn tại chỗ này chỉ tồn tại dưới dạng hình ảnh nên không có trong "
      "bản chép văn bản; các ký hiệu được giải thích trong nguyên bản như sau: t<sub>c</sub> là "
      "hằng số thời gian nhiệt, m là khối lượng, c là nhiệt dung riêng, k là hệ số truyền nhiệt "
      "và A là diện tích tiếp xúc nhiệt.",
      "The equations at this point in the source exist only as images and are absent from the "
      "text layer; their symbols are explained in the original as follows: t c is the thermal "
      "time constant, m is the mass, c is the specific heat, k is the heat transfer "
      "coefficient, and A is the area of thermal contact.")
    P("Khi nhiệt độ thay đổi nhanh, kết đọc nhiệt độ của cảm biến nhiệt được cho bởi một biểu "
      "thức (cũng là hình ảnh trong nguồn) với T là nhiệt độ đọc, T<sub>1</sub> là nhiệt độ ban "
      "đầu, T<sub>2</sub> là nhiệt độ thực của hệ thống và t là thời gian kể từ khi sự thay đổi "
      "xảy ra.",
      "When temperature changes rapidly, the temperature output reading of a thermal sensor is "
      "given by an expression (also an image in the source) where T is the temperature reading, "
      "T1 is the initial temperature, T2 is the true system temperature, and t is the time from "
      "when the change occurred.")
    P("Hằng số thời gian của một hệ t<sub>c</sub> được định nghĩa là thời gian để hệ đạt 63,2% "
      "giá trị nhiệt độ cuối cùng sau một sự thay đổi nhiệt độ. Ví dụ, một khối đồng được giữ "
      "trong bể nước đá cho đến khi nhiệt độ ổn định ở 0 °C. Sau đó lấy ra và đặt vào bể hơi "
      "100 °C. Nhiệt độ của khối đồng không lập tức lên 100 °C mà tăng theo đường cong hàm mũ "
      "khi hấp thụ năng lượng từ hơi, cho đến sau một khoảng thời gian nhất định (tức hằng số "
      "thời gian của nó) sẽ đạt 63,2 °C, rồi cuối cùng tới 100 °C. Trong hằng số thời gian thứ "
      "hai, đồng tăng thêm 63,2% của phần nhiệt độ còn lại để tới cân bằng. Tức là (100 − 63,2) "
      "× 63,2% = 23,3 °C, hay vào cuối hai chu kỳ hằng số thời gian, nhiệt độ của đồng là "
      "86,5 °C. Cuối ba chu kỳ là 95 °C, v.v. Khi cần thời gian đáp ứng nhanh, hằng số thời gian "
      "nhiệt có thể là vấn đề nghiêm trọng. Trong một số trường hợp, hằng số có thể kéo dài "
      "vài giây và có thể phải áp dụng hiệu chỉnh điện tử cho kết đọc đầu ra để có đáp ứng "
      "nhanh hơn. Có thể làm điều này bằng cách đo tốc độ tăng của nhiệt độ do cảm biến chỉ thị "
      "và ngoại suy nhiệt độ mục tiêu thực tế. Hằng số thời gian nhiệt của một vật tương tự như "
      "hằng số thời gian điện.",
      "The time constant of a system t c is defined as the time it takes for the system to "
      "reach 63.2% of its final temperature value after a temperature change. As an example, a "
      "copper block is held in an ice-water bath until its temperature has stabilized at 0°C. "
      "It is then removed and placed in a 100°C steam bath. The temperature of the copper block "
      "will not immediately go to 100°C, but its temperature will rise on an exponential curve "
      "as it absorbs energy from the steam, until after some time period (i.e., its time "
      "constant), it will reach 63.2°C, eventually reaching 100°C. During the second time "
      "constant, the copper will rise another 63.2% of the remaining temperature to get to "
      "equilibrium. That is, (100 − 63.2) × 63.2% = 23.3°C, or at the end of two time constant "
      "periods, the temperature of the copper will be 86.5°C. At the end of three periods, the "
      "temperature will be 95°C, and so on. Where a fast response time is required, thermal "
      "time constants can be a serious problem. In some cases, the constants can be several "
      "seconds in duration, and a correction may have to be electronically applied to the output "
      "reading to obtain a faster response. Measuring the rate of rise of the temperature "
      "indicated by the sensor and extrapolating the actual aiming temperature can do this. The "
      "thermal time constant of a body is similar to an electrical time constant.")

    H("Lắp đặt", "Installation", h3)
    P("Cần cẩn thận khi xác định vị trí phần cảm biến của cảm biến nhiệt độ. Phần này phải được "
      "bao phủ hoàn toàn bởi môi trường đang đo và không được chạm vào thành bình. Nếu cần, cảm "
      "biến phải được che khỏi nhiệt bức xạ và nhiệt phản xạ. Cảm biến cũng nên được đặt ở hạ "
      "lưu của chất lỏng đang được trộn, để bảo đảm nhiệt độ đã ổn định, nhưng càng gần điểm trộn "
      "càng tốt để có phép đo nhiệt độ nhanh nhất nhằm điều khiển tốt. Cần có hằng số thời gian "
      "nhiệt thấp trong cảm biến để đáp ứng nhanh.",
      "Care must be taken in locating the sensing portion of the temperature sensor. It should "
      "be fully encompassed by the medium whose temperature is being measured, and not be in "
      "contact with the walls of the container. The sensor should be screened from reflected "
      "and radiant heat, if necessary. The sensor also should be placed downstream from fluids "
      "being mixed, to ensure that the temperature has stabilized, but as close as possible to "
      "the point of mixing, to give as fast as possible temperature measurement for good "
      "control. A low thermal time constant in the sensor is necessary for a quick response.")
    P("Có thể cần bù và hiệu chuẩn khi dùng thiết bị lò xo áp suất có ống dài, nhất là khi cần "
      "kết đọc chính xác.",
      "Compensation and calibration may be necessary when using pressure-spring devices with "
      "long tubes, especially when accurate readings are required.")

    H("Hiệu chuẩn", "Calibration", h3)
    P("Có thể hiệu chuẩn nhiệt độ cho hầu hết thiết bị cảm biến nhiệt độ bằng cách nhúng chúng vào "
      "chuẩn nhiệt độ đã biết, đó là các điểm cân bằng của hỗn hợp rắn/lỏng hoặc lỏng/khí (còn "
      "gọi là điểm ba - triple point). Một số chuẩn như vậy được cho trong Bảng 4. Hầu hết thiết "
      "bị cảm biến nhiệt độ đều bền và tin cậy, nhưng có thể bị lệch khỏi hiệu chuẩn do rò rỉ "
      "trong quá trình sử dụng hoặc nhiễm bẩn trong lúc chế tạo, vì vậy nên kiểm tra định kỳ.",
      "Temperature calibration can be performed on most temperature sensing devices by immersing "
      "them in known temperature standards, which are the equilibrium points of solid/liquid or "
      "liquid/gas mixtures (also known as the triple point). Some of these standards are given "
      "in Table 4. Most temperature-sensing devices are rugged and reliable, but they can go out "
      "of calibration, due to leakage during use or contamination during manufacture, and "
      "therefore should be checked on a regular basis.")
    P("<b>Bảng 4.</b> Các điểm hiệu chuẩn của thang nhiệt độ (bảng gốc là hình ảnh, không có dữ "
      "liệu trong lớp văn bản).",
      "<b>Table 4.</b> Temperature Scale Calibration Points (the source table is an image; its "
      "data is not present in the text layer).")

    H("Bảo vệ", "Protection", h3)
    P("Trong một số ứng dụng, thiết bị cảm biến nhiệt độ được đặt trong giê-cheo-nhiệt hoặc vỏ "
      "bọc để tránh hư hỏng cơ khí hoặc để dễ thay thế. Kiểu bảo vệ này có thể làm tăng đáng kể "
      "thời gian đáp ứng của hệ thống, trong một số trường hợp là không chấp nhận được. Cảm biến "
      "cũng có thể cần được bảo vệ khỏi quá nhiệt, do đó có thể cần một thiết bị thứ hai bền hơn "
      "để bảo vệ thiết bị cảm biến chính. Thiết bị bán dẫn có thể có sẵn bảo vệ quá nhiệt. Cơ chế "
      "an toàn khi mất nguồn (fail-safe) cũng có thể được tích hợp để tắt hệ thống khi xử lý vật "
      "liệu dễ bay hơi hoặc ăn mòn.",
      "In some applications, temperature-sensing devices are placed in thermowells or enclosures, "
      "to prevent mechanical damage or for ease of replacement. This kind of protection can "
      "greatly increase the system response time, which in some circumstances may be "
      "unacceptable. Sensors also may need to be protected from over temperature, so that a "
      "second, more rugged device may be needed to protect the main sensing device. "
      "Semiconductor devices may have built-in over temperature protection. A fail-safe "
      "mechanism also may be incorporated for system shutdown, when processing volatile or "
      "corrosive materials.")
    P("Nhiệt độ là thông số vật lý quan trọng nhất, vì mọi thông số vật lý khác đều phụ thuộc vào "
      "nhiệt độ. Nhiệt độ có thể đo bằng Celsius hoặc Kelvin trong hệ đơn vị SI, và Fahrenheit "
      "hoặc Rankine trong hệ đơn vị Anh. Chương này đã mô tả mối quan hệ giữa các đơn vị và giới "
      "thiệu khái niệm cơ bản rằng nhiệt độ là thước đo năng lượng nhiệt chứa trong một vật hay "
      "biên độ dao động phân tử. Biên độ dao động và lực hút phân tử quyết định pha của vật liệu. "
      "Năng lượng nhiệt có thể đo bằng đơn vị nhiệt Anh (British thermal unit) hoặc joule, và "
      "có thể truyền giữa các vật bằng dẫn nhiệt, đối lưu hoặc bức xạ. Cơ chế truyền nhiệt đã "
      "được mô tả.",
      "Temperature is the most important physical parameter, because all other physical "
      "parameters are temperature-dependent. Temperature can be measured using Celsius or "
      "Kelvin, in the SI system of units, and Fahrenheit or Rankine in the English system of "
      "units. This chapter described the relations between the units and introduced the basic "
      "concept that temperature is a measure of the heat energy contained in a body or the "
      "amplitude of molecular vibration. The vibration amplitude and molecular attraction "
      "determines the phase of the material. Heat energy can be measured in British thermal "
      "units or joules, and can be transferred between bodies either by conduction, convection, "
      "or radiation. The mechanics of heat transfer was described.")
    P("Có rất nhiều thiết bị để đo nhiệt độ. Việc chọn thiết bị do yêu cầu của ứng dụng quyết "
      "định. Những đổi mới mới, như nhiệt kế số bán dẫn, đã làm nhiệt kế thủy ngân bị loại bỏ. "
      "Các ứng dụng Bật/Tắt giá rẻ từng dùng thiết bị lá kép, nhưng chúng cũng đang bị thay bằng "
      "thiết bị bán dẫn. Các ứng dụng dải nhiệt rộng thường dùng cặp nhiệt điện, còn thiết bị độ "
      "chính xác cao là RTD. Một số thiết bị có thời gian ổn định dài do hằng số thời gian nhiệt "
      "của chúng, điều này có thể được bù bằng điện tử.",
      "A large number of instruments is available for temperature measurement. The choice of "
      "instrument is determined by the requirements of the application. New innovations, such as "
      "the semiconductor digital thermometer, have brought about the demise of the mercury "
      "thermometer. Inexpensive On/Off applications used bimetallic devices, but these are also "
      "being replaced by semiconductor devices. Wide temperature range applications typically "
      "use thermocouples, and high accuracy devices are RTDs. Some devices have long settling "
      "times due to their thermal time constant, which can be compensated for electronically.")

    # ---------------------------------------------------------------- 1.9
    H("1.9 Tài liệu tham khảo", "1.9 References")
    b.append(refs(_REFS))

    # ---------------------------------------------------------------- about
    H("Về nguồn tài liệu", "About the source", h3)
    P("Chương 1 chiếm PDF tr. 15-59 (45 trang có chữ; PDF tr. 60 để trống), tương ứng tr. 1-45 "
      "của bản in; PAGES_SRC = 46 đếm cả PDF tr. 15-60. Các mục theo mục lục là Introduction, "
      "The History of Temperature Measurement, Thermometers, Probes, Non-Contact Devices, "
      "Control System Outputs, Transmitters and Readouts, Application Considerations và "
      "References. Nguyên bản có đúng sáu hình đánh số Figure 1 - Figure 6; tất cả được vẽ lại "
      "dạng vector trong iihfig.py với nhãn và số gọi chi tiết.",
      "Chapter 1 occupies PDF pp. 15-59 (45 pages of text; PDF p. 60 is blank), corresponding "
      "to printed pp. 1-45; PAGES_SRC = 46 counts PDF pp. 15-60. Its sections are Introduction, "
      "The History of Temperature Measurement, Thermometers, Probes, Non-Contact Devices, "
      "Control System Outputs, Transmitters and Readouts, Application Considerations and "
      "References. The source contains exactly six numbered figures, Figure 1 - Figure 6; all "
      "are redrawn as vectors in iihfig.py with their labels and callouts.")
    b.append(note(
        ("<b>Đặc điểm của nguyên bản.</b> Các dòng “Citation:” trong nguồn là ghi chú nguồn ảnh, "
        "không phải prose, nên không được dịch. Bảng 1, 2 và 4 chỉ có tiêu đề trong lớp văn bản "
        "(dữ liệu là hình ảnh); Bảng 3 được chép đầy đủ. Ba phương trình trong mục Hằng số thời "
        "gian nhiệt và phương trình PID cũng là hình ảnh nên chỉ được mô tả bằng ký hiệu. Nguồn "
        "có một số lỗi chính tả và lỗi OCR được giữ nguyên trong bản Anh (ví dụ “man monitoring”, "
        "“Jaspeh L. Gay-Lussac”, “this lead to”, “in the rage of”, “they are being with electronic "
        "units”, “Ck)axial”, “Metropologia”, “Phisics”), trong khi bản Việt dùng nghĩa đúng. Mục "
        "Types of Thermistors liệt kê mục NTC hai lần như trong nguyên bản.")
        if vi else
        "<b>Source quirks.</b> The 'Citation:' lines in the source are image credits, not prose, "
        "and are not translated. Tables 1, 2 and 4 have only their captions in the text layer "
        "(the data are images); Table 3 is reproduced in full. Three equations in the Thermal "
        "Time Constant section and the PID equation are also images and are therefore described "
        "by their symbols. A number of source typos and OCR artifacts are kept in the English "
        "text (e.g. 'man monitoring', 'Jaspeh L. Gay-Lussac', 'this lead to', 'in the rage of', "
        "'they are being with electronic units', 'Ck)axial', 'Metropologia', 'Phisics'), while "
        "the Vietnamese uses the intended meaning. The 'Types of Thermistors' list repeats the "
        "NTC entry, as in the original."))
    P("<i>Đây là bản dịch không chính thức, dùng cho mục đích học tập. Nội dung gốc © 2018 "
      "3G E-learning LLC.</i>",
      "<i>This is an unofficial translation for study purposes. Original content © 2018 "
      "3G E-learning LLC.</i>")
    return "".join(b)


def body_vi():
    return _body("vi")


def body_en():
    return _body("en")
