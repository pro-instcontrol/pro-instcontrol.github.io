# -*- coding: utf-8 -*-
"""Chapter 4, "Telemetry", section 4.5 "Digital Telemetry" (EN/VI bilingual).

Source: Prasad, Jayaswal & Priye, *Instrumentation and Process Control*
(I.K. International, 2019), PDF pp. 235-236, printed pp. 223-224, decoded text
lines 8907-8955.  Covered here are amplitude, frequency and phase modulation
of digital bit streams (Figures 4.27-4.29), pulse code modulation (PCM) and
quantization error, the Nyquist sampling rule, channel bandwidth (4.2) and the
PCM transmission rate in terms of signal-to-noise ratio (4.3, 4.4).  Equations
use literal Unicode notation; the English body follows the source wording and
the Vietnamese body uses the accepted technical reading.
"""

import ipcfig4 as F
from ipc_ch04_lib import H, P, L, E, FIG, TBL, NOTE


def section(lang):
    b = []

    # ---------------------------------------------------------------- 4.5
    H(b, lang,
      "4.5 Đo từ xa số",
      "4.5 Digital Telemetry")

    P(b, lang,
      "Trong dạng đo từ xa này, tín hiệu số gồm sự kết hợp của các bit 0 và 1 "
      "được truyền qua đường dây cáp hoặc bằng phương tiện khác. Ở đây cũng áp "
      "dụng các kỹ thuật điều chế đã được thiết lập cho tín hiệu cần truyền, "
      "khi đó tín hiệu đã ở dạng số. Các kỹ thuật cơ bản tương tự như những kỹ "
      "thuật đã mô tả trong hệ thống tương tự. Cả ba kỹ thuật điều chế đều được "
      "áp dụng và trình bày trong các Hình 4.27, 4.28 và 4.29 cho ba tín hiệu "
      "số khác nhau lần lượt là 01100101, 01101001 và 1010011010. Sóng mang ở "
      "đây cũng chính là sóng sin, và do đó các tín hiệu số đã điều chế được "
      "thể hiện trong cùng các hình đó.",
      "In this form of telemetry, a digital signal consisting of a combination "
      "of 0s and 1s is transmitted via a cable link or by other means. Here too "
      "the well-established modulation techniques are applied to the signal to "
      "be transmitted, which is now available in digital form. The basic "
      "techniques are similar to those described for analog systems. All three "
      "modulation techniques have been applied and are shown in Figures 4.27, "
      "4.28 and 4.29 for three different digital signals, 01100101, 01101001 "
      "and 1010011010 respectively. The carrier wave here is also the "
      "sinusoidal wave itself, and accordingly the modulated digital signals "
      "have been shown in the same figures.")

    FIG(b, 27, F.fig_f27(), lang)
    FIG(b, 28, F.fig_f28(), lang)
    FIG(b, 29, F.fig_f29(), lang)

    NOTE(b, lang,
      "Các chuỗi bit trong Hình 4.27, 4.28 và 4.29 lần lượt là 01100101, "
      "01101001 và 1010011010.",
      "The bit strings in Figures 4.27, 4.28 and 4.29 are 01100101, 01101001 "
      "and 1010011010 respectively.")

    # --------------------------------------------------------------- PCM
    P(b, lang,
      "Tuy nhiên, kỹ thuật điều chế phổ biến nhất cho dạng đo từ xa số là điều "
      "chế mã xung (PCM). Tạo sóng PCM rất dễ dàng: người ta chỉ cần lượng tử "
      "hóa sóng điều chế biên độ xung. Hệ thống PCM chọn, như thường lệ, giá "
      "trị gần nhất trong một tập hợp các số rời rạc, tức là số nhị phân. Ví "
      "dụ, nếu một hệ thống tín hiệu tương tự nhận giá trị trong khoảng 0 đến "
      "5 V (mức chuẩn thường dùng) và giá trị tức thời là 4,4 V thì giá trị số "
      "tương ứng là 0100 khi biểu diễn bằng 4 chữ số. Khi đó sai số là 0,4 V "
      "và được gọi là sai số lượng tử hóa. Nếu tăng số chữ số ở mức mã số thì "
      "có thể thu được nhiều chi tiết hơn từ PCM. Mức biểu diễn được cho bởi "
      "R_l = 2^N, trong đó N là số chữ số trong tín hiệu PCM.",
      "The most popular modulation technique for the digital form of telemetry, "
      "however, is that of pulse code modulation (PCM). It is very easy to "
      "obtain a PCM wave: it is produced simply by quantizing the pulse "
      "amplitude modulated wave. The PCM system selects, as usual, the nearest "
      "approximation with respect to a set of discrete numbers, i.e. binary "
      "numbers. For instance, if an analog signal system assumes values between "
      "0 and 5 volts (a standard value used in most equivalent systems) and the "
      "instantaneous value is 4.4 volts, then its digital value is 0100 over a "
      "4-digit level of representation. The error here comes to 0.4 volt and "
      "is called the quantization error. If the number of digits is increased "
      "at the digital code level, more details can be obtained from the PCM. "
      "The representation level is given by R_l = 2^N, where N is the number "
      "of digits in the PCM signal.")

    # ------------------------------------------- Nyquist / channel bandwidth
    P(b, lang,
      "Trong kỹ thuật PCM, băng thông của tín hiệu thực tế quyết định việc lựa "
      "chọn băng thông cho PCM. Định lý Nyquist xác định cách thức lấy mẫu "
      "được quyết định trong hệ thống PCM. Tốc độ lấy mẫu là tối ưu khi nó bằng "
      "hai lần băng thông của dạng sóng tín hiệu gốc. Băng thông của một kênh "
      "được cho bởi:",
      "In the PCM technique, the bandwidth of the actual signal directs the "
      "selection of bandwidth of the PCM. Nyquist theorem defines the way "
      "sampling is decided with the PCM system. The sampling rate is optimum "
      "when it is twice the bandwidth of the original signal wave. The "
      "bandwidth of a particular channel is given by:")
    E(b, lang, "BW = Nf₀", "BW = Nf₀", num="4.2")

    P(b, lang,
      "trong đó f₀ là tần số cực đại của tín hiệu đầu ra.",
      "where f₀ is the maximum frequency of the output signal.")

    # -------------------------------------------------- transmission rate
    P(b, lang,
      "Tốc độ truyền Trp qua PCM có thể được biểu diễn theo tỷ số tín hiệu trên "
      "nhiễu, và được cho bởi:",
      "Rate of transmission Trp through PCM can be expressed in terms of the "
      "signal-to-noise ratio and is given by:")
    E(b, lang, "Trp = f_b log₂[1 + P₁/P₂]", "Trp = f_b log₂[1 + P₁/P₂]",
      num="4.3")

    P(b, lang, "hoặc", "or")

    E(b, lang, "Trp = 2f_b log₂[1 + V₁/V₂]", "Trp = 2f_b log₂[1 + V₁/V₂]",
      num="4.4")

    P(b, lang,
      "trong đó P₁ và V₁ là cường độ tín hiệu dưới dạng công suất và điện áp, "
      "còn P₂ và V₂ là cường độ nhiễu dưới dạng công suất và điện áp.",
      "where P₁ and V₁ are signal strengths in the form of power and voltage "
      "and similarly P₂ and V₂ are the noise strength in terms of power and "
      "voltage.")

    return b
