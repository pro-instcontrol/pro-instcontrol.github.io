# -*- coding: utf-8 -*-
"""Book 9, Chapter 3 (part A) — Study of Control Strategy of the Converter in
Solar Photovoltaic Power System (EN/VI bilingual).

Source: Jin Liu and Yigong Zhang, in L. N. Jalali (ed.), *Handbook on Power
Plant Instrumentation and Control* (Bibliotex, 2019), PDF pp. 55–57, printed
pp. 39–41: ABSTRACT, KEYWORDS, INTRODUCTION and STRUCTURE OF THE SYSTEM.
Figure 1 is redrawn as a vector in `ppicfig3.py`; its caption comes from there.
Figures 2–8 belong to the other section modules of Chapter 3.
"""

from ppic_common import h2, h3, p, fig, note  # noqa: F401
import ppicfig3 as F


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

    # ------------------------------------------------------------------ ABSTRACT
    H("TÓM TẮT", "ABSTRACT")
    P(
        "Năng lượng mặt trời quang điện (PV) là một trong những nguồn năng lượng "
        "tái tạo quan trọng nhất, đồng thời cũng là một nguồn năng lượng xanh. "
        "Việc vận hành và điều khiển hệ thống phát điện mặt trời quang điện có "
        "tầm quan trọng đối với ứng dụng của nó. Bài báo này nghiên cứu chiến "
        "lược điều khiển của bộ chuyển đổi dùng trong phát điện quang điện (PV) "
        "năng lượng mặt trời, có khả năng đấu nối với lưới điện. Mô hình mô phỏng "
        "của hệ thống phát điện PV được xây dựng để kiểm chứng tính khả thi của "
        "chiến lược điều khiển. Một số thí nghiệm đã được thực hiện trên bộ thiết "
        "bị thí nghiệm năng lượng tái tạo của Công ty TI.",
        "Solar photovoltaic (PV) generation is one of the most important "
        "renewable energy resources, which is a green energy too. The operation "
        "and control of the solar PV generation system are important for its "
        "application. This paper studies the control strategy of the converter "
        "used in solar energy photovoltaic (PV) power generation, which can "
        "connect with the power grid. The simulation model of the PV generation "
        "system is set up to verify the feasibility of the control strategy. And "
        "some experiments have been done in the renewable experiment kit of TI "
        "Company."
    )

    # ----------------------------------------------------------------- KEYWORDS
    P(
        "<b>Từ khóa:</b> Converter, DSP, MATLAB, Control, Power",
        "<b>Keywords:</b> Converter, DSP, MATLAB, Control, Power"
    )

    # -------------------------------------------------------------- INTRODUCTION
    H("GIỚI THIỆU", "INTRODUCTION")
    P(
        "Khi nhu cầu năng lượng tăng lên, nhiều nguồn năng lượng tái tạo như gió "
        "và năng lượng mặt trời được nghiên cứu để phát điện. Và phát điện quang "
        "điện năng lượng mặt trời sẽ được sử dụng rộng rãi, vì điện năng xanh có "
        "thể được cung cấp bởi nó.",
        "With the demand of the energy increases, many renewable energy sources "
        "such as wind and solar energy are studied to generate electric power. "
        "And solar energy photovoltaic power generation will be widely used, "
        "because of the green electric power can be supplied by it."
    )
    P(
        "Thuật toán điều khiển của bộ chuyển đổi là một trong những điểm quan "
        "trọng nhất đối với việc sử dụng phát điện quang điện. Và hệ thống phát "
        "điện mặt trời quang điện có thể cung cấp điện cho người tiêu dùng trong "
        "hệ thống phát điện phân tán (distributed generation - DG) hoặc cho tải "
        "cô lập của người tiêu dùng, chẳng hạn như đèn đường. Thuật toán điều "
        "khiển khác nhau đối với hệ thống cô lập và hệ thống đấu nối với lưới "
        "điện [1].",
        "The control algorithm of the converter is one of the most important "
        "points for the use of photovoltaic power generation. And the solar PV "
        "generation system can supply power to the custom in a distributed "
        "generation (DG) system or to the isolated custom's load, such as street "
        "lamp. The control algorithm is different for the isolated system and "
        "the system connected with the power grid [1]."
    )
    P(
        "Bài báo này nghiên cứu chiến lược điều khiển của bộ chuyển đổi dùng "
        "trong phát điện quang điện (PV) năng lượng mặt trời, có khả năng đấu nối "
        "với lưới điện. Mô hình mô phỏng của hệ thống phát điện PV, được xây dựng "
        "với MATLAB/Simulink, được thiết lập để kiểm chứng tính khả thi của "
        "chiến lược điều khiển [2].",
        "This paper studies the control strategy of the converter used in solar "
        "energy photovoltaic (PV) power generation, which can connect with grid. "
        "The simulation model of the PV generation system, which is built with "
        "MATLAB/Simulink, is set up to verify the feasibility of the control "
        "strategy [2]."
    )
    P(
        "Bộ thiết bị phát triển hệ thống phát điện quang điện năng lượng mặt "
        "trời của Công ty TI được sử dụng để thực hiện các thí nghiệm điều "
        "khiển, và chiến lược điều khiển đấu nối lưới được triển khai trên nền "
        "tảng thí nghiệm [3].",
        "Solar energy PV power generation system development kit of TI Company "
        "is used to do the control experiments, and the grid connection control "
        "strategy is realized in the experiment plat [3]."
    )

    # ------------------------------------------------------ STRUCTURE OF THE SYSTEM
    H("CẤU TRÚC CỦA HỆ THỐNG", "STRUCTURE OF THE SYSTEM")
    P(
        "Hệ thống phát điện mặt trời quang điện được cấu thành từ mảng quang "
        "điện, mạch tăng áp DC/DC, bộ nghịch lưu công suất, bộ lọc, mạch PLL và "
        "các phần khác [4]. Cấu trúc của hệ thống phát điện mặt trời quang điện "
        "được thể hiện trong Hình 1.",
        "The solar photovoltaic power generation system is consisted of "
        "photovoltaic array, DC/DC boost circuit, power inverter, filter, PLL "
        "circuit and other parts [4]. The structure of solar photovoltaic power "
        "generation system is shown in Figure 1."
    )
    FIG(1)
    P(
        "Mảng quang điện mặt trời tạo ra dòng điện một chiều (DC). Và bộ chuyển "
        "đổi của hệ thống phát điện PV biến đổi công suất DC thành công suất "
        "xoay chiều (AC) một pha hoặc ba pha (220/380 V, 50 Hz), để cấp cho tải "
        "AC hoặc đấu nối với lưới điện.",
        "The solar photovoltaic array produces direct current (DC) power. And "
        "the PV generation system converter the DC power into single phase or "
        "three phase alternating current (AC) power (220/380 V, 50 Hz), and to "
        "supply for the AC load or connect with the power grid."
    )
    P(
        "Cấp bộ chuyển đổi tăng áp DC-DC có thể tăng điện áp DC đầu vào lên một "
        "giá trị điện áp yêu cầu, là đầu vào tiếp theo của bộ nghịch lưu. Cấp "
        "này cũng cung cấp điều khiển ổn áp trên bus DC trung gian mà không có ở "
        "các đầu nguồn, có thể điều chỉnh điện áp DC về giá trị yêu cầu [5].",
        "The DC-DC boost converter stage could step up the input DC voltage to a "
        "required voltage value, which is the next input of the inverter. This "
        "stage also provides voltage regulation control on the intermediate DC "
        "bus that is not available at the source terminals, which can regulate "
        "the DC voltage into the required value [5]."
    )
    P(
        "Chức năng của mạch PLL (Phase Locking Loop - vòng khóa pha) là theo dõi "
        "điện áp đường dây AC của lưới điện và đưa ra điện áp tham chiếu cho "
        "điện áp đầu ra của bộ nghịch lưu, điện áp này phải được đồng bộ với "
        "điện áp đường dây, nếu bộ chuyển đổi được đấu nối với lưới điện.",
        "The function of PLL (Phase Locking Loop) circuit is to trace the AC "
        "line voltage of the power grid and give the reference voltage for the "
        "inverter output voltage which has to be synchronized with the line "
        "voltage, if the converter is connected with the power grid."
    )
    P(
        "Bộ nghịch lưu biến đổi điện áp DC thành điện áp AC một pha hoặc 3 pha, "
        "dựa trên cấu trúc bộ nghịch lưu và thuật toán điều khiển. Thuật toán "
        "điều khiển SPWM (Sine Pulse Width Modulation - điều chế độ rộng xung "
        "hình sin) được sử dụng trong điều khiển bộ nghịch lưu và các tín hiệu "
        "điều khiển được tính toán bởi bộ vi điều khiển với một số tín hiệu phản "
        "hồi từ mạch, như điện áp bus DC, điện áp đầu ra của bộ nghịch lưu và "
        "tín hiệu PLL.",
        "The inverter converts the DC voltage into single phase or 3-phase AC "
        "voltage, which is based on the inverter structure and the control "
        "algorithm. SPWM control algorithm (Sine Pulse Width Modulation) is used "
        "in the inverter control and the control signals are calculated by the "
        "Micro-controller with some feedback signals from the circuit, such the "
        "DC Bus voltage, the inverter output voltage and the PLL signal."
    )
    P(
        "Và toàn bộ hệ thống điều khiển là một vòng lặp kín với điều chỉnh điện "
        "áp [6]. Để có điện áp AC đầu ra chất lượng cao, có một mạch lọc ở đầu ra "
        "của bộ nghịch lưu, có thể lọc các hài bậc cao do bộ nghịch lưu tạo ra, "
        "mặc dù THD (Total Harmonic Distortion - độ méo hài tổng) của điện áp rất "
        "nhỏ với thuật toán điều khiển SPWM.",
        "And the whole control system is a close loop with voltage regulation "
        "[6]. In order to get high quality output AC voltage, there is a filter "
        "circuit at the terminal of the output of the inverter, which can filter "
        "the high numbers harmonics produced by the inverter, even though the "
        "voltage THD (Total Harmonic Distortion) is very small with SPWM control "
        "algorithm."
    )
    P(
        "Có một giao diện người–máy trên PC, giao tiếp với thẻ điều khiển thông "
        "qua SCI (Serial Communication Interface - giao diện truyền thông nối "
        "tiếp) và được lập trình bằng ngôn ngữ C#. Các chức năng của phần mềm "
        "giao diện là khởi tạo và thiết lập các thông số điều khiển của hệ "
        "thống; thiết lập các mô hình điều khiển; giám sát các thông số nhận "
        "được từ thẻ điều khiển và đưa ra dạng sóng hình sin của điện áp lưới, "
        "dạng sóng điện áp đầu ra của bộ nghịch lưu [7].",
        "There is a human-machine Interface in PC, which is communicated with "
        "the controller card through SCI (Serial Communication Interface) and "
        "programmed with C# language. The functions of the interface software "
        "are to initialize and set the control parameters of the control system; "
        "setup the control models; monitor the parameters get from controller "
        "card and give out the sine waveform of the power grid voltage, voltage "
        "waveform of the output of the inverter [7]."
    )
    P(
        "Với giao diện này, việc thay đổi các thông số điều khiển và quan sát các "
        "kết quả khác nhau do các thông số khác nhau gây ra trở nên thuận tiện. "
        "Và việc sử dụng phần mềm giao diện có thể giúp bắt đầu nhanh chóng việc "
        "nghiên cứu thuật toán điều khiển và hiểu nguyên lý hoạt động của hệ "
        "thống phát điện PV dễ dàng hơn. Đây là một trợ thủ tốt để điều khiển và "
        "giám sát hoạt động của mạch tăng áp DC-DC, mạch PLL và mạch nghịch lưu, "
        "đồng thời có thể lưu trữ dữ liệu hoạt động trên PC [8].",
        "With the interface, it is convenience to change the parameters of "
        "control and observe the different results caused by different "
        "parameters. And using the interface software can give quickly starting "
        "to study the control algorithm and understand the operation principle "
        "of PV power generation system more easily. It is a good assistant to "
        "control and monitor the operation of the DC-DC Boost circuit, PLL "
        "circuit and the inverter circuit, and can store the data of operation "
        "in the PC [8]."
    )

    return b
