# -*- coding: utf-8 -*-
"""Chapter 5, section 5.5: Aperture Time for Sample and Hold Mechanism.

Source: Prasad, Jayaswal and Priye, *Instrumentation and Process Control*
(I.K. International, 2019), PDF pp. 262-265, printed pp. 250-253, decoded
text lines 10011-10174.  Covers the aperture-time relation, Nyquist
sampling, weighted-resistor and R-2R ladder DAC networks, and the DAC
output-current expressions, with Figures 5.28-5.34.

The text layer scrambles the printed formulas; they were recovered from
the page renders and are reproduced here as unnumbered equations with
literal Unicode symbols.  The source prints no equation numbers and no
tables in this portion, so none are invented.  Figure suppliers are
written in parallel; non-overwriting fallbacks are installed below only
when a supplier has not yet been registered.
"""

import ipcfig5 as F
from ipc_ch05_lib import H, P, L, E, FIG, TBL, NOTE, REFS


# ----------------------------------------------------------------- figures
_FIG_STUB_TEXT = {
    28: ("Mạch DAC dùng điện trở có trọng số", "Weighted-resistor DAC circuit"),
    29: ("Mạng điện trở bậc thang R-2R", "R-2R ladder resistor network"),
    30: ("Rút gọn mạng bậc thang, bước một", "Ladder network reduction, first step"),
    31: ("Rút gọn mạng bậc thang, bước hai", "Ladder network reduction, second step"),
    32: ("Rút gọn mạng bậc thang, bước ba", "Ladder network reduction, third step"),
    33: ("Rút gọn mạng bậc thang, bước bốn", "Ladder network reduction, fourth step"),
    34: ("Dòng đầu ra của DAC bốn bit", "Four-bit DAC output currents"),
}


def _stub_fig(n):
    cvi, cen = _FIG_STUB_TEXT[n]
    svg = (
        '<svg xmlns="http://www.w3.org/2000/svg" width="680" height="250" '
        'viewBox="0 0 680 250"><rect width="680" height="250" '
        'fill="#ffffff"/><text x="340" y="120" text-anchor="middle" '
        'font-size="14" fill="#1f3a5f">Figure 5.%d</text></svg>' % n
    )
    return (svg, "Hình 5.%d · %s" % (n, cvi),
            "Figure 5.%d · %s" % (n, cen),
            "Sơ đồ minh họa Hình 5.%d" % n,
            "Illustration for Figure 5.%d" % n)


for _n in range(28, 35):
    if not hasattr(F, "fig_f%02d" % _n):
        setattr(F, "fig_f%02d" % _n, (lambda _n=_n: _stub_fig(_n)))


# ------------------------------------------------------------------- prose
def section(lang):
    b = []

    # ---------------------------------------------------------------- 5.5
    H(b, lang,
      "5.5 Thời gian khẩu độ cho cơ chế lấy mẫu-giữ mẫu",
      "5.5 Aperture Time for Sample and Hold Mechanism")

    P(b, lang,
      "Mạch lấy mẫu-giữ mẫu là một hệ thống phổ biến được dùng trong các mạch "
      "xử lý và truyền dữ liệu, vì thế ở đây ta chỉ đề cập đến khoảng thời gian "
      "mà một tín hiệu tương tự phải được lấy mẫu và giá trị lấy được phải được "
      "giữ nguyên ở mức đó sao cho đạt được mức lượng tử hóa và mã hóa chấp "
      "nhận được. Khoảng thời gian này gọi là thời gian khẩu độ. Công thức thực "
      "nghiệm cho thời gian khẩu độ Ta được cho như sau,",
      "Sample and hold is a general system used in data processing and "
      "transmission circuits, and therefore our discussion is limited to the "
      "duration for which an analog signal must be sampled and the sampled "
      "value held at that particular level so that an acceptable level of "
      "quantization and coding is obtained. This duration is known as the "
      "aperture time. The empirical relation for the aperture time Ta is "
      "given by,")

    E(b, lang, "Ta = ΔE / (2π Em f)", "Ta = ΔE / (2π Em f)", num="")

    P(b, lang,
      "trong đó ΔE là sự thay đổi mức biên độ tại điện áp E, Em là giá trị cực "
      "đại của điện áp hình sin và f là tần số của điện áp. Đối với phép chuyển "
      "đổi xấp xỉ liên tiếp, thời gian khẩu độ bằng đúng thời gian chuyển đổi.",
      "where ΔE is the change in amplitude level at voltage E, Em is the "
      "maximum value of the sinusoidal voltage and f is the frequency of the "
      "voltage. For successive-approximation conversion, the aperture time "
      "equals the conversion time.")

    P(b, lang,
      "Nói chung, việc lấy mẫu phải được thực hiện sao cho không một phần thông "
      "tin nào do tín hiệu mang theo bị mất, đồng thời số lần lấy mẫu được giữ "
      "ở mức nhỏ nhất có thể. Theo lý thuyết do Nyquist đề xuất, tần số lấy mẫu "
      "phải ít nhất gấp đôi tần số của tín hiệu cần lấy mẫu. Nếu fs là tần số "
      "tín hiệu cần lấy mẫu thì tần số lấy mẫu sẽ là 2fs. Tuy nhiên, trên thực "
      "tế người ta lấy 2,5fs để bù cho nhiễu và các hạn chế khác của linh kiện "
      "trong mạch.",
      "In general, sampling must be carried out in such a way that no part of "
      "the information carried by the signal is lost, while keeping the number "
      "of samples as small as possible. The theoretical sampling rate proposed "
      "by Nyquist must be at least twice the frequency of the signal to be "
      "sampled. If fs is the frequency of the signal to be sampled, the "
      "sampling rate will be 2fs. In practice, however, it is taken as 2.5fs "
      "to compensate for noise and other limitations of the circuit "
      "components.")

    # ---------------------------------------------- Digital-to-Analog Conversion
    H(b, lang, "Chuyển đổi số-tương tự (DAC)",
      "Digital-to-Analog Conversion (DAC)", level=3)

    P(b, lang,
      "Hệ thống chuyển đổi số-tương tự dùng các mạng điện trở. Để lưu tạm tín "
      "hiệu số cũng như để dịch mức điện áp, người ta kết hợp thêm các mạch "
      "khác. Có hai kiểu kỹ thuật DAC:",
      "The digital-to-analog conversion system employs resistor networks. "
      "Additional circuits are combined for the temporary storage of the "
      "digital signal as well as for shifting the voltage level. There are "
      "two types of DAC technique:")

    L(b, lang,
      ["Hệ DAC dùng mạng điện trở có trọng số.",
       "Hệ DAC dùng mạng điện trở bậc thang."],
      ["Weighted resistor network DAC system.",
       "Ladder network DAC system."])

    # -------------------------------------------- (a) weighted resistor network
    H(b, lang, "(a) Hệ DAC dùng mạng điện trở có trọng số",
      "(a) Weighted resistor network DAC system", level=3)

    P(b, lang,
      "Trong hệ này có n điện trở đầu vào kết hợp với cùng số công tắc, được "
      "trọng số theo cấp số nhân nhị phân như minh họa ở Hình 5.28. Ở đây n là "
      "số bit được chọn để chuyển đổi. Vref là điện áp chuẩn ổn định và các điện "
      "trở dùng là loại chính xác được chọn để đạt độ chính xác cao nhất có "
      "thể, vì độ chính xác của phép chuyển đổi cũng phụ thuộc vào linh kiện "
      "được dùng. Khuếch đại thuật toán OA đóng vai trò bộ đổi dòng sang áp và "
      "cộng tổng các dòng chạy qua. Từ đó tạo ra điện áp ra V0 làm tín hiệu "
      "tương tự đầu ra, tỉ lệ chính xác với đầu vào số được cung cấp.",
      "In this system there are n input resistors combined with an equal "
      "number of switches weighted in binary progression, as indicated in "
      "Figure 5.28. Here n represents the number of bits selected for "
      "conversion. Vref is a stable reference voltage and the resistors used "
      "are of precision type, chosen for the highest possible accuracy, "
      "because the accuracy of conversion also depends on the components "
      "used. The operational amplifier OA acts as a current-to-voltage "
      "converter and sums the flowing currents. This in turn develops the "
      "output voltage V0 as the analog output signal, exactly proportional to "
      "the digital input supplied.")

    FIG(b, 28, F.fig_f28(), lang)

    P(b, lang,
      "Xét một trường hợp cụ thể khi tất cả các công tắc đều đóng, tức là Dn−1 = "
      "Dn−2 = … = D2 = D1 = D0 = 1, khi đó các dòng điện là:",
      "For a particular condition, when all the switches are closed, Dn−1 = "
      "Dn−2 = … = D2 = D1 = D0 = 1, and the currents are:")

    E(b, lang, "In−1 = Vref / R", "In−1 = Vref / R", num="")
    E(b, lang, "In−2 = Vref / (2 · R)", "In−2 = Vref / (2 · R)", num="")
    E(b, lang, "I2 = Vref / (2^(n−3) · R)",
      "I2 = Vref / (2^(n−3) · R)", num="")
    E(b, lang, "I1 = Vref / (2^(n−2) · R)",
      "I1 = Vref / (2^(n−2) · R)", num="")
    E(b, lang, "I0 = Vref / (2^(n−1) · R)",
      "I0 = Vref / (2^(n−1) · R)", num="")

    P(b, lang,
      "Do đó, đầu ra dưới dạng dòng điện sẽ là:",
      "Hence, the output in the form of current is:")

    E(b, lang, "Iout = In−1 + In−2 + … + I2 + I1 + I0",
      "Iout = In−1 + In−2 + … + I2 + I1 + I0", num="")
    E(b, lang,
      "Iout = (Vref / R) [1 + 1/2 + … + 1/2^(n−3) + 1/2^(n−2) + 1/2^(n−1)]",
      "Iout = (Vref / R) [1 + 1/2 + … + 1/2^(n−3) + 1/2^(n−2) + 1/2^(n−1)]",
      num="")

    P(b, lang,
      "Biểu thức tổng quát cho dòng điện đầu ra được cho như sau:",
      "The general expression for the output current is given by:")

    E(b, lang,
      "Iout = (Vref / R) [Dn−1/1 + Dn−2/2 + Dn−3/2² + … + D1/2^(n−2) + D0/2^(n−1)]",
      "Iout = (Vref / R) [Dn−1/1 + Dn−2/2 + Dn−3/2² + … + D1/2^(n−2) + D0/2^(n−1)]",
      num="")

    P(b, lang,
      "Hạn chế của phương pháp chuyển đổi này nằm ở chỗ rất khó tìm được các "
      "điện trở có giá trị hoàn toàn giống hệt nhau. Mỗi bước của phép chuyển "
      "đổi cần được trọng số đúng cách, điều này không thể thực hiện trọn vẹn "
      "vì không có hai điện trở nào là giống hệt nhau. Hậu quả là xuất hiện sai "
      "số ở đầu ra. Hơn nữa, dải giá trị điện trở cứ tăng lên theo bội hai của "
      "giá trị trước đó, làm cho hệ thống trở nên phức tạp hơn khi số bit tăng.",
      "The limitation of this method of conversion lies in the fact that "
      "resistors of exactly identical value are difficult to find. Each step "
      "of the conversion needs to be weighted properly, which is impossible "
      "to realize because no two resistors are identical. This results in an "
      "error in the output. Also, the range of resistance values keeps "
      "increasing as a multiple of two of the preceding one, and this makes "
      "the system more complicated as the number of bits is increased.")

    # ------------------------------------------------ (b) ladder network DAC
    H(b, lang, "(b) Hệ DAC dùng mạng điện trở bậc thang",
      "(b) Ladder network DAC system", level=3)

    P(b, lang,
      "Trong hệ này chỉ dùng điện trở có hai giá trị khác nhau, vì vậy nó hấp "
      "dẫn hơn kiểu dùng điện trở có trọng số. Hệ này khắc phục tất cả các vấn "
      "đề gặp phải ở hệ dùng điện trở có trọng số.",
      "In this system, resistors of only two different values are used and it "
      "is therefore more attractive than the weighted-resistor type. This "
      "system eliminates all the problems encountered with the weighted "
      "resistor system.")

    P(b, lang,
      "Nếu ta thiết kế một mạng điện trở bậc thang như Hình 5.29 và tính giá "
      "trị điện trở tương đương khi nhìn từ các điểm A, B, C, D về phía trái, "
      "thì giá trị điện trở cuối cùng chỉ còn là R. Quá trình này được thể "
      "hiện lần lượt ở các Hình 5.30, 5.31, 5.32 và 5.33.",
      "If we design a ladder resistor network as shown in Figure 5.29 and "
      "calculate the equivalent resistance looking from points A, B, C and D "
      "towards the left, the final resistance value turns out to be only R. "
      "This has been shown successively in Figures 5.30, 5.31, 5.32 and 5.33.")

    FIG(b, 29, F.fig_f29(), lang)
    FIG(b, 30, F.fig_f30(), lang)
    FIG(b, 31, F.fig_f31(), lang)
    FIG(b, 32, F.fig_f32(), lang)
    FIG(b, 33, F.fig_f33(), lang)

    P(b, lang,
      "Quá trình rút gọn mạng điện trở này cho thấy tất cả các nút đều mang "
      "trọng số nhị phân dương. Vì vậy, nếu áp một từ nhị phân vào các nút A, B, "
      "C, D thì mạng bậc thang có thể chia một dòng chuẩn thành các mức dòng "
      "được trọng số theo nhị phân. Hình 5.34 trình bày một bố trí như vậy: "
      "một dòng chuẩn 2 mA được đưa vào và kết quả phân bố dòng được chỉ ra "
      "ngay trong sơ đồ.",
      "This reduction process of the resistor network indicates that all the "
      "nodes are positive and binary weighted. Therefore, if a binary word is "
      "applied at the nodes A, B, C and D, the ladder can divide a reference "
      "current into binary-weighted levels. Figure 5.34 shows such an "
      "arrangement, where a reference current of 2 milliamperes has been "
      "applied, which results in the distribution of current indicated in the "
      "diagram itself.")

    FIG(b, 34, F.fig_f34(), lang)

    return b
