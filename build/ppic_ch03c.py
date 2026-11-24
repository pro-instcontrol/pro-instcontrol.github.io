# -*- coding: utf-8 -*-
"""Book 9, Chapter 3 (part C) - Experiments, Conclusions and References
(EN/VI bilingual).

Source: Jin Liu and Yigong Zhang, in L. N. Jalali (ed.), *Handbook on Power
Plant Instrumentation and Control* (Bibliotex, 2019), PDF pp. 61-64, printed
pp. 45-48: EXPERIMENTS; CONCLUSIONS; REFERENCES. Figures 6, 7 and 8 are
redrawn as vectors in `ppicfig3.py`; captions come from there.
"""

from ppic_common import h2, h3, p, fig, note, refs, ul  # noqa: F401
import ppicfig3 as F


_REFS = [
    "L. Jin and Y. S. Niu, “Research on the Universal Power Electronic "
    "Control Platform Based on Real Time Operation System,” Presented "
    "at 2009 International Conference on Sustainable Power Generation "
    "and Supply, SUPERGEN 2009, Nanjing, China, 2009.",
    "J. L. Alqueres and J. C. Praca, “Power-Electronic Systems for the "
    "Grid Integration of Renewable Energy Sources: A Survey,” in IEEE "
    "Transactions on Industrial Electronics, Vol. 53, No. 4, 2006.",
    "S. B. Kjear, K. P. John and F. Blaabjerg, “A Review of Single-"
    "Phase Grid-Connected Inverters for Photovoltaic Modules,” IEEE "
    "Transactions on Industry Applications, Vol. 41, No. 5, 2005.",
    "X. Y. Wang and M. Kazerani, “A Multicarrier Modular Photovoltaic "
    "Grid-connected Inverter with a New Phase-shift Rule,” Electric "
    "Power Systems Research, Vol. 77, No. 7, 2007, pp. 754-760. "
    "doi:10.1016/j.epsr.2006.06.010",
    "J. C. Jia, J. Liu and Y. G. Zhang, “Novel Reactive Power "
    "Optimization Control Strategy for Doubly Fed Induction Wind "
    "Power Generation System,” Proceedings of the Chinese Society of "
    "Electrical Engineering, Vol. 30, No. 30, 2010, pp. 87-92.",
    "Al-Amoudi and A. L. Zhang, “Optional Control of a Grid- Connected "
    "PV System for Maximum Power Point Tracking and Unity Power "
    "Factor,” Power Electronics and Variable Speed Drives, 1998, pp. "
    "21-23.",
    "S. B. Kjear, K. P. John and F. Blaabjerg, “A Review of Single-"
    "Phase Grid-Connected Inverters for Photovoltaic Modules,” IEEE "
    "Transactions on Industry Applications, Vol. 41, No. 5, 2005.",
    "Timothy, C. Y. Wang, Z. H. Ye, G. Sinha, et al., “Output Filter "
    "Design for a Grid-interconnected Three-phase Inverter,” Power "
    "Electronics Specialist Conference, IEEE 34th Annual, No. 2, 2003, "
    "pp. 779-784.",
    "X. Y. Wang and M. Kazerani, “A Multicarrier Modular Photovoltaic "
    "Grid-connected Inverter with a New Phase-shift Rule,” Electric "
    "Power Systems Research, Vol. 77, No. 7, 2007, pp. 754-760. "
    "doi:10.1016/j.epsr.2006.06.010",
    "Implementing a Digitally Controlled Renewable Energy.",
    "DSP TMS320F28035, Datasheet: http://www.ti.com.",
    "F28xxx User’s Guides. http://www.ti.com/f28xuserguide",
    "TMS320, “Fixed-Point DSP Assembly Language Tools User’s "
    "Guide,” Texas Instruments,1991, pp. 78-123.",
]


def section(lang):
    """Return the bilingual HTML chunks for this part of Chapter 3."""
    vi = lang == "vi"
    b = []

    def P(v, e):
        b.append(p(v if vi else e))

    def H(v, e, lvl=h2):
        b.append(lvl(v if vi else e))

    def FIG(n):
        b.append(fig(n, getattr(F, "fig_f3%d" % n)()))

    # -------------------------------------------------------------- EXPERIMENTS
    H("THÍ NGHIỆM", "EXPERIMENTS")
    P(
        "Nền tảng thí nghiệm của hệ thống phát điện mặt trời quang điện là "
        "bộ phát triển hệ thống điện PV của công ty TI. Hệ thống này chủ yếu "
        "được cấu thành bởi mảng PV, mạch DC/DC (Boost), các mạch nghịch lưu, "
        "mạch lọc, mạch lấy mẫu, bộ điều khiển TMS320F28035, v.v. [10].",
        "Solar photovoltaic power generation systems experiment platform is "
        "the TI company PV power system development package. This system is "
        "mainly composed by the PV array, DC/DC (Boost) circuit, inverter "
        "circuits, filter circuit, the sampling circuit, TMS320F28035 "
        "controller etc [10]."
    )
    P(
        "Bộ điều khiển TMS320F28035 là một CPU 32-bit hiệu suất cao "
        "(TMS320C28x™) của công ty TI. Thiết bị này chỉ dùng một nguồn cấp "
        "3,3 V duy nhất và có tần số 60 MHz. Nó có hai bộ dao động nội bộ "
        "Zero-pin, tới 45 chân GPIO đa năng và ba bộ định thời CPU 32-bit "
        "[11].",
        "TMS320F28035 controller is a high-efficiency 32-Bit CPU "
        "(TMS320C28x™) of TI Company. It is only single 3.3V supply and "
        "60MHz device. It has two internal Zero-pin Oscillators and up to 45 "
        "Multiplexed GPIO Pins and three 32-Bit CPU Timers [11]."
    )
    P(
        "Một bộ điều chỉnh điện áp nội bộ cho phép hoạt động với một đường "
        "nguồn duy nhất. Các bộ so sánh tương tự với tham chiếu 10-bit nội "
        "bộ đã được bổ sung và có thể được định tuyến trực tiếp để điều "
        "khiển các đầu ra PWM. ADC chuyển đổi trong thang đo toàn phần cố "
        "định từ 0 đến 3,3 V và hỗ trợ các tham chiếu VREFHI/VREFLO tỷ lệ. "
        "Giao diện ADC được tối ưu hóa để giảm chi phí và độ trễ.",
        "An internal voltage regulator allows for single rail operation. "
        "Analogy comparators with internal10-bit references have been added "
        "and can be routed directly to control the PWM outputs. The ADC "
        "converts from 0 to 3.3-V fixed full scale range and supports "
        "ratio-metric VREFHI/VREFLO references. The ADC interface has been "
        "optimized for low overhead/latency."
    )
    P(
        "Thẻ điều khiển của bộ điều khiển TMS320F28035 được thể hiện trong "
        "Hình 6. Thẻ này liên lạc với PC thông qua SCI. Thuật toán điều "
        "khiển được triển khai trên thẻ điều khiển, và các tín hiệu điều "
        "khiển (xung SPWM) được gửi tới mạch chính để điều khiển bộ nghịch "
        "lưu chuyển đổi điện áp một chiều thành điện áp xoay chiều yêu cầu.",
        "The control card of TMS320F28035 controller is showed in Figure 6. "
        "And it communicates with the PC through SCI. The control algorithm "
        "is progressed in the control card, and the control signals (SPWM "
        "pulses) are sent to the main circuit to drive the inverter to "
        "converter the DC voltage into the required AC voltage."
    )
    FIG(6)
    P(
        "Tần số chuyển mạch của các công tắc nghịch lưu là 25 kHz. Bốn xung "
        "điều khiển SPWM của hai nhánh của bộ nghịch lưu được thể hiện "
        "trong Hình 7. Mỗi hai xung là bổ sung cho nhau, và có một vùng "
        "thời gian chết được thiết lập giữa hai xung này để ngăn ngừa hiện "
        "tượng ngắn mạch xảy ra ở một nhánh của bộ nghịch lưu. Và vùng thời "
        "gian chết có thể được thay đổi thông qua phần mềm giao diện "
        "người–máy trên PC, hoặc được thay đổi trong chương trình điều "
        "khiển theo yêu cầu của quá trình điều khiển [12].",
        "The frequency of the inverter switches is 25 kHz. And the four "
        "SPWM control pulses of the two arms of the inverter are showed in "
        "Figure 7. Each two pulses are complemented, and there is dead time "
        "zone setup between these two pulses to prevent the short circuit "
        "happened in the one arm of the inverter. And the dead time zone can "
        "be changed through the human-machine interface software in the PC, "
        "or be changed in the control program according to the requirement "
        "of control [12]."
    )
    FIG(7)
    P(
        "Các thí nghiệm về mạch tăng áp DC/DC và thuật toán điều khiển SPWM "
        "của bộ nghịch lưu một pha đã được hoàn thành trên nền tảng thí "
        "nghiệm. Các dạng sóng đầu ra của thí nghiệm được thể hiện trong "
        "Hình 8 bên dưới. Đường màu vàng là điện áp bus một chiều, đường "
        "màu xanh lam là điện áp lưới điện, đường màu xanh lục là dạng sóng "
        "điện áp đầu ra của bộ nghịch lưu, và đường màu tím là dạng sóng "
        "dòng điện đầu ra của bộ nghịch lưu, với tải là một điện trở. Điện "
        "áp đầu ra của bộ nghịch lưu cùng pha và cùng tần số với điện áp "
        "lưới điện. Sự đồng bộ giữa điện áp đầu ra và điện áp lưới điện "
        "được thực hiện bằng mạch PLL và điều khiển vòng lặp kín [13].",
        "The experiments of DC/DC booster circuit and single phase inverter "
        "SPWM control algorithm are finished in the experimental platform. "
        "The experiment output waveforms are showed in Figure 8 below. The "
        "yellow line is the DC Bus voltage, the blue line is the power grid "
        "voltage, the green line is the output voltage waveform of the "
        "inverter, and the purple line is the output current waveform of the "
        "inverter, which load is a resister. And the output voltage of the "
        "inverter is same phase and same frequency with the power grid "
        "voltage. And the synchronization between the output voltage and the "
        "power grid voltage is realized by the PLL circuit and the close "
        "loop control [13]."
    )
    FIG(8)

    # ------------------------------------------------------------- CONCLUSIONS
    H("KẾT LUẬN", "CONCLUSIONS")
    P(
        "Hệ thống điều khiển của bộ chuyển đổi điện năng là một trong những "
        "phần quan trọng nhất của hệ thống phát điện mặt trời quang điện. "
        "Bài báo này hoàn thành mô phỏng hệ thống điều khiển và hiện thực "
        "hóa chiến lược điều khiển trong hệ thống thí nghiệm. Bài báo đưa ra "
        "việc kiểm tra và xác minh thuật toán điều khiển mô phỏng trên nền "
        "tảng thí nghiệm, và có thể phát triển thêm các thí nghiệm nghiên "
        "cứu chi tiết hơn trên nền tảng này.",
        "The control system of power converter is one of the most important "
        "parts of the solar photovoltaic power generation system. This paper "
        "completes the simulation of the control system and realized the "
        "control strategy in experiment system. It gives the test and verify "
        "of the simulation control algorithm in the experiment platform, and "
        "more detail research experiments can be development in the platform."
    )

    # --------------------------------------------------------------- REFERENCES
    H("TÀI LIỆU THAM KHẢO", "REFERENCES")
    b.append(refs(_REFS))

    return b
