# -*- coding: utf-8 -*-
"""Chapter 5, tail of 5.3.2 plus sections 5.3.3 and 5.4 (EN/VI bilingual).

Source: Prasad, Jayaswal and Priye, *Instrumentation and Process Control*
(I.K. International, 2019), PDF pp. 259-262, printed pp. 247-250, decoded
text lines 9864-10010.  Covers the successive-approximation ADC conversion
with Figures 5.25 and 5.26, "Resolution of Digital Meters", "Sensitivity of
digital meter" and "Accuracy of Digital Meter" with Figure 5.27 (the
quantization-error waveform).  The printed formulas are reproduced as
unnumbered equations: 1/10^n, 1/10^4 = 0.0001 = 0.01 per cent,
S = lowest full scale value x resolution, and Ce = C/(2 sqrt(3)).

The printed diagrams are images in the PDF and their text layer is
scrambled; the `ipcfig5_c` supplier is authored in parallel.  Simple
non-overwriting stand-ins are installed below only when a real supplier is
not yet available, so the genuine vector redraws always take precedence.
"""

import ipcfig5 as F
from ipc_ch05_lib import H, P, L, E, FIG, TBL, NOTE, REFS


# ----------------------------------------------------------------- figures
def _standalone_fig(n, title_vi, title_en, alt_vi, alt_en):
    """A minimal valid five-tuple, used only when no supplier is present."""
    svg = (
        '<svg xmlns="http://www.w3.org/2000/svg" width="680" height="250" '
        'viewBox="0 0 680 250"><rect width="680" height="250" '
        'fill="#ffffff"/><rect x="140" y="70" width="400" height="95" '
        'fill="#eef3fb" stroke="#1f3a5f" stroke-width="1.2"/>'
        '<text x="340" y="118" text-anchor="middle" font-size="13" '
        'fill="#1f3a5f">%s</text>'
        '<text x="340" y="200" text-anchor="middle" font-size="11" '
        'fill="#888888">Hinh 5.%d / Figure 5.%d</text></svg>'
        % (title_en, n, n)
    )
    return (svg, "Hình 5.%d · %s" % (n, title_vi),
            "Figure 5.%d · %s" % (n, title_en), alt_vi, alt_en)


def _ensure(n, title_vi, title_en, alt_vi, alt_en):
    name = "fig_f%02d" % n
    if not hasattr(F, name):
        setattr(F, name,
                (lambda n=n, v=title_vi, e=title_en, av=alt_vi, ae=alt_en:
                 _standalone_fig(n, v, e, av, ae)))


_ensure(25, "Cây so sánh xấp xỉ liên tiếp",
        "Successive-approximation comparison tree",
        "Sơ đồ cây so sánh: các giá trị nhị phân từ 000 đến 111 ứng với các "
        "phân số của Er từ 1/8 đến 7/8 qua bốn lần so sánh liên tiếp",
        "Comparison tree: binary values 000 to 111 mapped to fractions of "
        "Er from 1/8 to 7/8 over four successive comparisons")

_ensure(26, "Trình tự khởi động và flip-flop",
        "Start and flip-flop conversion sequence",
        "Sơ đồ khối hệ thống ADC xấp xỉ liên tiếp với bộ so sánh, DAC, "
        "thanh ghi điều khiển, thanh ghi phân phối, mạch trễ và flip-flop "
        "start/stop",
        "Block diagram of the successive-approximation ADC with comparator, "
        "DAC, control and distribution registers, time delay and start/stop "
        "flip-flop")

_ensure(27, "Minh họa sai số lượng tử hóa",
        "Quantization error illustration",
        "Đồ thị sai số lượng tử hóa dạng răng cưa dao động từ -C/2 đến +C/2 "
        "với giá trị đỉnh-đỉnh C",
        "Sawtooth quantization-error waveform swinging from -C/2 to +C/2 "
        "with a peak-to-peak value C")


# ------------------------------------------------------------------- prose
def section(lang):
    b = []

    # ------------------------------------------- tail of 5.3.2 (balancing ADC)
    P(b, lang,
      "Các hệ thống hiển thị số khác cũng có thể được sử dụng. Rõ ràng là ở "
      "đây không dùng nguyên lý lấy mẫu mà dùng nguyên lý cân bằng.",
      "Other systems of digital display can also be used. As is evident, "
      "here the principle of balancing, and not sampling, has been used.")

    H(b, lang, "4. Chuyển đổi ADC kiểu xấp xỉ liên tiếp",
      "4. Successive approximation type ADC conversion", level=3)

    P(b, lang,
      "Nguyên lý xấp xỉ liên tiếp so sánh một điện áp đầu vào dạng tương tự "
      "với điện áp tham chiếu của một bộ DAC (bộ đếm lắp ráp giải mã), được "
      "chia liên tiếp thành từng nửa. Như thấy trong Hình 5.25, một số nhị "
      "phân bốn chữ số 1000, biểu diễn Er (điện áp tham chiếu đầy đủ), được "
      "chia đôi thành số nhị phân tương đương 100, tương ứng với điện áp "
      "1/2 Er. Điện áp tham chiếu 1/2 Er này được so sánh với điện áp tương "
      "tự. Nếu phép so sánh cho thấy xấp xỉ thứ nhất quá nhỏ (tức là 1/2 Er "
      "< đầu vào tương tự), thì phép so sánh tiếp theo được thực hiện với "
      "3/4 Er (số nhị phân tương đương là 110). Nếu phép so sánh này cho "
      "thấy xấp xỉ thứ nhất quá lớn (tức là 1/2 Er > đầu vào tương tự), thì "
      "phép so sánh tiếp theo được thực hiện với 1/4 Er (số nhị phân tương "
      "đương là 010). Sau bốn lần xấp xỉ liên tiếp, số nhị phân cần tìm "
      "được xác lập. Một số tám chữ số sẽ được xác lập sau tám lần xấp xỉ "
      "liên tiếp.",
      "The principle of successive approximation compares an input voltage "
      "in analog form to the reference voltage of a DAC (Decode Assembly "
      "Counter), which is divided repeatedly into half. As seen in Figure "
      "5.25, a four-digit binary number 1000, representing Er (full reference "
      "voltage), is divided into half (the equivalent binary number is 100) "
      "to give the corresponding voltage 1/2 Er. This reference voltage "
      "1/2 Er is compared to the analog voltage. If the comparison indicates "
      "that the first approximation is too small (that is, 1/2 Er < analog "
      "input), then the next comparison is made with respect to 3/4 Er (the "
      "equivalent binary number is 110). If this comparison indicates that "
      "the first approximation was too large (that is, 1/2 Er > analog "
      "input), then the next comparison is made with respect to 1/4 Er (the "
      "equivalent binary number is 010). After four successive "
      "approximations, the required digital number is resolved. An "
      "eight-digit number will be resolved in eight successive "
      "approximations.")

    FIG(b, 25, F.fig_f25(), lang)

    P(b, lang,
      "Hình 5.26 trình bày một hệ thống chuyển đổi ADC dùng phương pháp xấp "
      "xỉ liên tiếp. Điện áp đầu vào tương tự được đưa tới mạch so sánh; tín "
      "hiệu kia tới bộ so sánh là điện áp tham chiếu do bộ chuyển đổi "
      "số-tương tự (DAC) cung cấp. Như chỉ ra trong sơ đồ khối, lúc bắt đầu, "
      "thanh ghi điều khiển và thanh ghi phân phối được đặt với một bit 1 ở "
      "vị trí có ý nghĩa nhất (MSB) và số 0 ở tất cả các bit có ý nghĩa nhỏ "
      "nhất còn lại (LSB). Vì vậy thanh ghi phân phối cho thấy chu trình "
      "chuyển đổi tín hiệu vào tương tự đã bắt đầu và đang ở giai đoạn thứ "
      "nhất. Thanh ghi điều khiển cho giá trị 1000, làm cho mạch D/A đưa ra "
      "điện áp có trị số khoảng 1/2 điện áp tham chiếu. Cùng lúc, một xung "
      "đi vào mạch trễ thời gian.",
      "Figure 5.26 shows an ADC conversion system employing the successive "
      "approximation method. The analog input voltage is applied to the "
      "comparison circuit; the other signal to the comparator is a reference "
      "voltage applied through a digital-to-analog (D/A) converter (DAC). As "
      "indicated by the block diagram, at start the control register and the "
      "distribution register are set with a 1 in the MSB (most significant "
      "bit) and a 0 in all the remaining LSB (least significant bit) "
      "positions. So the distribution register indicates that the conversion "
      "cycle of the analog input signal has started and is at its first "
      "stage. The control register indicates 1000 and this brings an output "
      "voltage from the D/A converter circuit of the order of 1/2 of the "
      "reference voltage. At the same instant, a pulse enters the time delay "
      "circuit.")

    FIG(b, 26, F.fig_f26(), lang)

    P(b, lang,
      "Khi bộ chuyển đổi D/A và mạch so sánh đã ổn định, xung trễ sau mạch "
      "trễ thời gian được đưa qua đầu ra của bộ so sánh. Khi bit MSB tiếp "
      "theo được đặt trong thanh ghi điều khiển bởi mạch định thời, bit MSB "
      "hiện tại giữ nguyên giá trị 1 hoặc được đặt lại về 0, tùy theo đầu ra "
      "của mạch so sánh. Trạng thái 1 của thanh ghi phân phối được dịch sang "
      "vị trí kế tiếp và theo dõi phép so sánh tiếp theo. Quá trình được lặp "
      "lại cho đến khi kết thúc phép xấp xỉ cuối cùng, và sự kết thúc chuyển "
      "đổi được thanh ghi phân phối báo cáo.",
      "By the time the D/A converter and comparator circuit have settled, "
      "the delayed pulse, after the time delay, is gated through the "
      "comparator output. When the next MSB is set in the control register "
      "circuit by the timing circuit, the present MSB remains at 1 or is "
      "reset to 0, based on the output of the comparator circuit. The state "
      "1 of the distribution register is shifted to the next nearby position "
      "and keeps track of the next comparison. The procedure is repeated "
      "until the end of the last approximation operation, and finally the "
      "end of conversion is reported by the distribution register.")

    P(b, lang,
      "Để tránh bất kỳ sự thay đổi nào của điện áp vào tương tự trong thời "
      "gian chuyển đổi (từ dạng tương tự sang dạng số), điện áp vào tương tự "
      "được đưa qua mạch lấy mẫu-giữ mẫu. Mạch này lấy mẫu điện áp vào tương "
      "tự trong một thời gian rất ngắn và giữ nó ở cùng giá trị đó cho đến "
      "khi quá trình chuyển đổi từ tương tự sang số hoàn tất.",
      "In order to avoid any change in the analog voltage input taking place "
      "during the conversion period (from analog to digital form), the "
      "analog voltage input is taken through a sample and hold circuit. The "
      "circuit takes a sample of the analog voltage input in a very short "
      "time and holds it at the same value until the conversion from analog "
      "to digital is completed.")

    # --------------------------------------------------------------- 5.3.3
    H(b, lang, "5.3.3 Độ phân giải của đồng hồ số",
      "5.3.3 Resolution of Digital Meters")

    P(b, lang,
      "Số chữ số dùng trong đồng hồ số quyết định độ phân giải. Điều này có "
      "nghĩa là một đồng hồ số ba chữ số có thang đo từ 0 đến 1 vôn sẽ có "
      "thể chỉ thị từ 0 đến 999 milivôn với độ phân giải 1 milivôn. Tuy "
      "nhiên, để dùng trong công nghiệp, một chữ số thứ tư, nếu đặt bên trái "
      "chữ số có tác dụng, có thể chỉ thị số 0 hoặc số 1. Như vậy, giá trị "
      "999 nói trên sẽ vượt lên trên 999 tới 1999, tạo ra sự quá tải giữa "
      "các thang đo. Đây được gọi là hiện tượng quá dải. Kiểu màn hình này "
      "được gọi là màn hình 3½ chữ số. Tuy nhiên, độ phân giải của một đồng "
      "hồ số dạng bảng chỉ được xác định bởi số chữ số đầy đủ có tác dụng.",
      "The number of digits used in a digital meter decides the resolution. "
      "This means a three-digit digital meter of range 0 to 1 volt shall be "
      "capable of indicating 0 to 999 millivolts with a resolution of 1 "
      "millivolt. However, for industrial use, a fourth digit, if placed on "
      "the left of the active digit, is capable of indicating either a zero "
      "or a one. Thus, the value 999 as described above will go above 999 up "
      "to 1999, which gives overloading between ranges. This is called "
      "over-ranging. This type of display shall be called a 3½-digit "
      "display. However, the resolution of a digital panel meter is "
      "determined by the number of full active digits only.")

    P(b, lang,
      "Nếu n là số chữ số đầy đủ có tác dụng, thì độ phân giải được định "
      "nghĩa là:",
      "If n is the number of full active digits, then the resolution is "
      "defined as:")

    E(b, lang, "Độ phân giải = 1/10ⁿ", "Resolution = 1/10ⁿ", num="")

    P(b, lang,
      "Như vậy, một màn hình bốn chữ số sẽ có độ phân giải bằng:",
      "Thus, a four-digit display will have a resolution of:")

    E(b, lang, "1/10⁴ = 0.0001 = 0.01 %", "1/10⁴ = 0.0001 = 0.01 %", num="")

    P(b, lang,
      "Giá trị này cũng được gọi là độ phân giải 1 trên 10.000.",
      "This is also called resolution at 1 in 10,000.")

    H(b, lang, "Độ nhạy của đồng hồ số", "Sensitivity of digital meter",
      level=3)

    P(b, lang,
      "Độ nhạy được định nghĩa là sự thay đổi nhỏ nhất của tín hiệu đầu vào "
      "mà đồng hồ số có thể phát hiện được. Về mặt toán học, độ nhạy S được "
      "cho bởi biểu thức:",
      "Sensitivity is defined as the smallest change in signal input which a "
      "digital meter is capable of detecting. Mathematically, sensitivity S "
      "is given by the relation:")

    E(b, lang, "S = giá trị toàn thang nhỏ nhất × độ phân giải",
      "S = lowest full scale value × resolution", num="")

    # --------------------------------------------------------------- 5.4
    H(b, lang, "5.4 Độ chính xác của đồng hồ số",
      "5.4 Accuracy of Digital Meter")

    P(b, lang,
      "Độ chính xác của đồng hồ số được biểu thị bằng phần trăm của giá trị "
      "đọc cộng với phần trăm của chữ số có ý nghĩa nhỏ nhất (LSD). Ví dụ, "
      "độ chính xác ± 0,2 % của giá trị đọc ± 2 chữ số có nghĩa là 0,2 % "
      "nhân với giá trị chỉ thị là một phần của sai số và phần trăm của LSD, "
      "tức 2 chữ số tương ứng với 0,02 %, được cộng vào phần sai số thứ "
      "nhất.",
      "Accuracy of a digital meter is expressed in terms of percentage of "
      "the reading plus a percentage of the LSD (least significant digit). "
      "For instance, accuracy of ± 0.2 per cent of reading ± 2-digit "
      "indicates that 0.2 per cent multiplied by the indicated value is one "
      "part of the error and the percentage of LSD, that is 2-digit, which "
      "comes to 0.02 per cent, is to be added to the first part of the error.")

    P(b, lang,
      "Mức sai số chấp nhận được trong quá trình lượng tử hóa được gọi là "
      "sai số lượng tử hóa và phụ thuộc vào số mức lượng tử hóa. Mức lượng "
      "tử hóa là một chỉ số của độ phân giải của thiết bị. Sai số lượng tử "
      "hóa được minh họa trong Hình 5.27. Giá trị đỉnh-đỉnh là C. Biểu thức "
      "thực nghiệm cho giá trị hiệu dụng (rms) của sai số lượng tử hóa Ce "
      "được cho bởi:",
      "The acceptance level of error during the quantization process is "
      "known as quantization error and is dependent on the number of "
      "quantization levels. The quantization level is an index of the "
      "resolution of the instrument. The quantization error is shown in "
      "Figure 5.27. The peak-to-peak value is C. The empirical relation for "
      "the rms value of the quantization error Ce is given by:")

    E(b, lang, "Ce = C / (2√3)", "Ce = C / (2√3)", num="")

    FIG(b, 27, F.fig_f27(), lang)

    return b
