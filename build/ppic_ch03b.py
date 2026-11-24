# -*- coding: utf-8 -*-
"""Book 9, Chapter 3 (part B) - Simulation Model (EN/VI bilingual).

Source: Jin Liu and Yigong Zhang, in L. N. Jalali (ed.), *Handbook on Power
Plant Instrumentation and Control* (Bibliotex, 2019), PDF pp. 58-61, printed
pp. 42-45: SIMULATION MODEL. Figures 2, 3, 4 and 5 are redrawn as vectors in
`ppicfig3.py`; captions come from there. The Figure 5 prose is split across
the printed page break in the source and is rejoined here into one paragraph.
"""

from ppic_common import h2, h3, p, fig, note  # noqa: F401
import ppicfig3 as F


def section(lang):
    """Return the bilingual HTML chunks for the Simulation Model section."""
    vi = lang == "vi"
    b = []

    def P(v, e):
        b.append(p(v if vi else e))

    def H(v, e, lvl=h2):
        b.append(lvl(v if vi else e))

    def FIG(n):
        b.append(fig(n, getattr(F, "fig_f3%d" % n)()))

    # ------------------------------------------------------- SIMULATION MODEL
    H("MÔ HÌNH MÔ PHỎNG", "SIMULATION MODEL")

    P(
        "Mô hình mô phỏng hệ thống phát điện mặt trời quang điện được xây dựng "
        "trong MATLAB/Simulink. Cấu trúc của mô hình mô phỏng được thể hiện "
        "trong Hình 2.",
        "The solar photovoltaic power generation system simulation model is "
        "established with the MATLAB/Simulink. The simulation model structure "
        "is shown in Figure 2."
    )
    FIG(2)
    P(
        "Mảng quang điện (PV) tạo ra điện áp một chiều thay đổi theo ánh sáng "
        "mặt trời và nhiệt độ.",
        "The PV array produces variable DC voltage according to the sun light "
        "and temperature."
    )
    P(
        "Khối DC/DC Boost tăng điện áp một chiều lên mức điện áp bus DC cần "
        "thiết, chính là điện áp trên tụ điện trong Hình 2. Để công suất tác "
        "dụng được truyền từ phía DC sang phía AC, điện áp bus DC phải lớn hơn "
        "giá trị đỉnh của điện áp phía AC [9].",
        "The DC/DC Boost block step up the DC voltage into a required DC Bus "
        "voltage, which is the voltage of the capacitor in Figure 2. And the "
        "DC Bus voltage should great than the peak value of the AC side voltage "
        "if the active power wants to be transmitted from the DC side to the "
        "AC side [9]."
    )
    P(
        "Khối con hệ thống điều khiển điều chỉnh điện áp bus DC được thể hiện "
        "trong Hình 3. Khối này gồm khối PLL, khối biến đổi abc sang dq0, khối "
        "bộ điều khiển PI, khối biến đổi dq0 sang abc và khối tạo xung PWM.",
        "The DC Bus voltage regulation control subsystem block is showed in "
        "Figure 3. It is consisted of PLL block, abc to dq0 converter block, PI "
        "controller block, dq0 to abc inverter block and the PWM pulses "
        "generator block."
    )
    FIG(3)
    P(
        "Mạch nghịch lưu là bộ chuyển đổi nguồn áp toàn cầu ba pha, dùng IGBT "
        "làm phần tử đóng cắt và có các diode được mắc song song ngược với các "
        "IGBT. Chức năng của các diode là tạo đường dẫn cho công suất phản "
        "kháng chảy từ phía AC về phía DC. Mô hình điều khiển SPWM được dùng "
        "để tạo các xung PWM điều khiển các phần tử đóng cắt của bộ nghịch lưu "
        "và chuyển đổi điện áp một chiều thành điện áp xoay chiều.",
        "The inverter circuit is a three phase full bridge voltage source "
        "converter, which uses the IGBT as switches, and there are Diodes "
        "reverse parallel connected with the IGBTs. The function of Diodes is "
        "to provide the flow path for the reactive power flowing from the AC "
        "side to the DC side. SPWM control model is used to generate the PWM "
        "pulses to drive the switches of the inverter and converter the DC "
        "voltage into AC voltage."
    )
    P(
        "Các xung điều khiển SPWM cho IGBT1 và IGBT2 được thể hiện trong Hình "
        "4. Độ rộng của xung thay đổi theo dạng sóng sin. Các xung của IGBT1 và "
        "IGBT2 ngược nhau vì chúng được mắc trên cùng một nhánh cầu. Thời gian "
        "chết của các IGBT không được xét trong mô hình mô phỏng, nhưng được "
        "tính đến trong hệ thống điều khiển thực tế.",
        "The SPWM control pulses for IGBT1 and IGBT2 are showed in Figure 4. "
        "The width of pulse is changed as a sinusoidal waveform. And the "
        "pulses of IGBT1 and IGBT2 are opposite because they are connected in "
        "one bridge arm. The dead time of the IGBTs is not considered in the "
        "simulation model, which is considered in the reality control system."
    )
    FIG(4)
    P(
        "Vì bộ nghịch lưu là tải phi tuyến nên nó có thể sinh ra các sóng hài "
        "bậc cao có tần số là bội số nguyên của tần số đóng cắt. Do đó, ở đầu ra "
        "của bộ nghịch lưu có một mạch lọc có chức năng lọc bỏ các sóng hài. "
        "Bộ lọc được chọn là bộ lọc LCL, có đặc tính tốt hơn bộ lọc LC.",
        "Because the inverter is non-linear load and it can produce high number "
        "harmonics, which frequency are integer times of the switches' "
        "frequency. So, there is a filter circuit at the output of the "
        "inverter, which function is to filter the harmonics. And the filter "
        "is the LCL filter, which has better character than LC filter."
    )
    P(
        "Dạng sóng đầu ra của mô phỏng được thể hiện trong Hình 5. Đường phía "
        "trên là dạng sóng điện áp đầu ra của bộ nghịch lưu khi dùng điều "
        "khiển SPWM, được gọi là dạng sóng SPWM, gồm thành phần sóng ở tần số "
        "đường dây và các thành phần sóng hài bậc cao. Hai dạng sóng bên dưới "
        "là dạng sóng điện áp và dòng điện của tải, trong đó các thành phần "
        "sóng hài bậc cao đã được mạch lọc loại bỏ. Nhờ đó có thể cung cấp "
        "dạng sóng điện áp đầu ra của bộ nghịch lưu có chất lượng cao.",
        "The simulation output waveform is showed in Figure 5. And the above "
        "line is the output voltage waveform of inverter with SPWM control, and "
        "is called as SPWM waveform, which is consist of the line frequency "
        "waveform and high numbers harmonics waveform. The under two waveforms "
        "are the voltage and current waveform of the load, and the high numbers "
        "are filtered by the filter circuit. It can provide high quality "
        "inverter output voltage waveform."
    )
    FIG(5)

    return b
