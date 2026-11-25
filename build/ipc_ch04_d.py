# -*- coding: utf-8 -*-
"""Chapter 4, "Telemetry", section 4.3 "Analog Telemetry" (EN/VI bilingual).

Source: Janardan Prasad, M. N. Jayaswal and Vishnu Priye, *Instrumentation and
Process Control* (I.K. International, 2019), PDF pp. 231-233, printed pp.
219-221, decoded text lines 8758-8851.  Covered here are the carrier/signal
notion, amplitude, frequency and phase modulation, sidebands and FM bandwidth.
The nine source figures (4.15-4.23) are redrawn as vectors in the `ipcfig4_a`
supplier module and placed where the text refers to them.  Equation (4.1) uses
literal Unicode notation; the English body follows the source wording, the
Vietnamese body uses the accepted technical reading.
"""

import ipcfig4 as F
from ipc_ch04_lib import H, P, L, E, FIG, TBL, NOTE


def section(lang):
    b = []

    # ---------------------------------------------------------------- 4.3
    H(b, lang,
      "4.3 Đo từ xa tương tự",
      "4.3 Analog Telemetry")

    P(b, lang,
      "Đo từ xa tương tự có thể được coi là một phần của cả đo từ xa bằng cáp "
      "lẫn đo từ xa RF, nhưng vẫn cần một thảo luận riêng, dù ngắn gọn, vì hệ "
      "thống truyền dẫn xoay chiều gặp nhiều sai số mà đã có sẵn những giải "
      "pháp điện tử rất tốt.",
      "Analog telemetry can be considered a part of both cable telemetry and RF "
      "telemetry, but a separate discussion, though brief, is needed because "
      "an AC transmission system encounters many errors for which excellent "
      "electronic solutions are available.")

    P(b, lang,
      "Thật không may, truyền tín hiệu tương tự qua đường dây cố định cũng như "
      "qua tín hiệu RF đều bị suy giảm cường độ do suy hao tự nhiên dọc theo "
      "đường truyền, do méo trễ của tín hiệu nhận được và do tỷ số tín hiệu trên "
      "nhiễu kém gây ra bởi nhiễu. Điều tệ nhất là các ảnh hưởng này phần lớn "
      "phụ thuộc vào tần số. Có thể dễ dàng nghiên cứu phân tích qua phổ quen "
      "thuộc của các thành phần Fourier.",
      "This is very unfortunate that analog transmission through land lines as "
      "well as through RF signalling suffers loss of signal strength due to "
      "the natural characteristic of attenuation along the path, delay "
      "distortion of the received signal and poor signal-to-noise ratio due to "
      "interference. The worst part of the problem is that these effects are "
      "largely frequency dependent. The analysis can be studied easily through "
      "the well-known spectrum of Fourier components.")

    P(b, lang,
      "Có thể khắc phục tình trạng mất tín hiệu bằng các kỹ thuật điều chế. "
      "Điều chế thực sự làm thay đổi hoàn toàn tín hiệu tương tự nhưng vẫn giữ "
      "nguyên chất lượng của nó, để ở đầu thu có thể dùng biện pháp điện tử "
      "chuyển tín hiệu trở về dạng ban đầu. Muốn vậy, người ta đưa vào một dạng "
      "sóng sin chuẩn gọi là sóng mang. Chức năng của sóng mang có thể so sánh "
      "với chức năng của một chuyến tàu hỏa chở khách: tàu chạy từ ga này tới "
      "ga kia, chở nhiều hành khách và hành lý. Thực ra, chính con tàu là thứ "
      "đi hết hành trình; khi hành khách và hành lý được đưa lên tàu thì chúng "
      "cũng đến được đích. Tương tự, trong kỹ thuật điều chế, tín hiệu được đặt "
      "lên sóng mang, và ở đầu thu tín hiệu được tách khỏi sóng mang — kỹ thuật "
      "gọi là giải điều chế, ngược với điều chế. Nhờ cách đó, đầu thu nhận được "
      "tín hiệu gần như nguyên dạng ban đầu.",
      "The problem of loss of signal can be dealt with by applying modulation "
      "techniques. Modulation in fact modifies the analog signal completely "
      "while leaving the quality of the signal intact, so that it can be "
      "converted into its original form by electronic means at the receiving "
      "end. The introduction of a standard sinusoidal waveform called the "
      "carrier wave does the job. The function of the carrier wave can be "
      "compared with the function of a passenger railway train. A passenger "
      "train runs from one destination to the other carrying a number of "
      "persons and luggage. Here, the persons and the luggage do not actually "
      "travel; it is the passenger train that travels all along. When the "
      "persons and the luggage are put on the train, they also reach the "
      "destination. In modulation techniques similarly, the signal is put on "
      "the carrier wave and at the receiving end the signal is stripped off "
      "the carrier, which is known as demodulation (the opposite of "
      "modulation). In this way the receiving end gets the signal in nearly "
      "original form.")

    P(b, lang,
      "Vì dạng sóng sin của sóng mang có ba biến số — biên độ, tần số và pha — "
      "nên các kỹ thuật điều chế được phân loại thành điều chế biên độ (AM), "
      "điều chế tần số (FM) và điều chế pha (PM). Điều chế là một chủ đề rất "
      "rộng, cần trình bày chi tiết để mô tả đầy đủ; nhưng ở đây phần trình "
      "bày chỉ giới hạn ở các nguyên lý cơ bản áp dụng cho đo từ xa bằng đường "
      "dây cố định và RF.",
      "Since there are three variables in a carrier sinusoidal waveform, e.g., "
      "amplitude, frequency and phase, modulation techniques can be classified "
      "as amplitude modulation (AM), frequency modulation (FM) and phase "
      "modulation (PM). Modulation is in fact a vast topic, which requires a "
      "detailed description for its complete treatment. But here the "
      "description shall be restricted to the basic principles applicable to "
      "land-line and RF telemetry only.")

    # ------------------------------------------------------------ 4.3 AM
    H(b, lang,
      "Điều chế biên độ (AM)",
      "Amplitude modulation (AM)", level=3)

    P(b, lang,
      "Trong kỹ thuật điều chế biên độ, biên độ của dạng sóng mang được thay "
      "đổi theo giá trị tức thời thực tế của tín hiệu cần truyền. Giả sử dạng "
      "sóng mang ở tần số f₁ có dạng sin (trường hợp thường gặp nhất), như "
      "Hình 4.15, và dạng sóng của tín hiệu tương tự ở tần số f₂ cũng thường "
      "có dạng sin, như Hình 4.16. Khi biên độ của sóng mang được cho đi theo "
      "dạng sóng tín hiệu, dạng sóng thu được của tín hiệu điều chế biên độ "
      "như Hình 4.17.",
      "In the amplitude modulation technique, the amplitude of the carrier "
      "waveform is modified with respect to the actual instantaneous value of "
      "the signal to be transmitted. Let us suppose the carrier waveform at "
      "frequency f₁ to be sinusoidal (the most usual case), as shown in Figure "
      "4.15, and the wave-shape of the analog signal of frequency f₂, which is "
      "also usually in sinusoidal form, as shown in Figure 4.16. When the "
      "amplitude of the carrier is added to the signal wave, the resulting "
      "waveshape of the amplitude modulated signal is shown in Figure 4.17.")
    FIG(b, 15, F.fig_f15(), lang)
    FIG(b, 16, F.fig_f16(), lang)
    FIG(b, 17, F.fig_f17(), lang)

    P(b, lang,
      "Như thấy, dạng sóng thu được có thêm hai dạng tần số hữu hiệu bên cạnh "
      "tần số gốc f₁ của sóng mang. Hai tần số tổng hợp (f₁ + f₂) và (f₁ − f₂) "
      "làm cho toàn bộ băng tần của tín hiệu là 2f₂. Chúng được gọi là các "
      "băng tần biên.",
      "As is seen, the resulting waveform has another two effective frequency "
      "patterns in addition to the original frequency f₁ of the carrier "
      "waveform. The combined frequencies consisting of (f₁ + f₂) and (f₁ − "
      "f₂) make the overall frequency band of the signal 2f₂. These are called "
      "sidebands.")

    P(b, lang,
      "Chất lượng của điều chế biên độ bị ảnh hưởng bởi trở kháng cáp lớn và "
      "nhiễu từ các trường tản, vì vậy có thể không nên dùng cho đo từ xa bằng "
      "đường dây cố định ở những khoảng cách đáng kể.",
      "The quality of amplitude modulation is affected by high cable impedance "
      "and the stray field interferences and therefore may not be advisable to "
      "be used for landline telemetry of substantial distances.")

    # ------------------------------------------------------------ 4.3 FM
    H(b, lang,
      "Điều chế tần số (FM)",
      "Frequency modulation (FM)", level=3)

    P(b, lang,
      "Trong điều chế tần số, sự điều chế chỉ thực hiện bằng thay đổi tần số, "
      "biên độ và pha nhất thiết giữ nguyên. Ở đây cũng giả sử dạng sóng tín "
      "hiệu tương tự có dạng sin. Khi tần số được điều chế, dạng sóng điều chế "
      "thu được thể hiện ở Hình 4.20 cùng với dạng sóng mang (Hình 4.18) và "
      "dạng sóng tín hiệu (Hình 4.19).",
      "In case of frequency modulation, the modulation is affected by frequency "
      "change only, the amplitude and phase necessarily remaining the same. "
      "Here also it is assumed that the analog signal wave is of sinusoidal "
      "type. When frequency is modulated, the resulting modulated waveshape is "
      "seen in Figure 4.20 along with the carrier waveform (Figure 4.18) and "
      "the signal waveform (Figure 4.19).")
    FIG(b, 18, F.fig_f18(), lang)
    FIG(b, 19, F.fig_f19(), lang)
    FIG(b, 20, F.fig_f20(), lang)

    P(b, lang,
      "Độ lớn của sự thay đổi tần số được xác định bởi biên độ của sóng mang, "
      "trong khi tốc độ thay đổi được xác định bởi tần số của sóng mang. Khác "
      "với kỹ thuật AM, trong kỹ thuật FM có nhiều băng tần biên được hình "
      "thành, nhưng cường độ của chúng giảm dần từ băng tần biên này sang "
      "băng tần biên khác. Sự giảm này trở nên rất rõ chỉ sau vài băng tần "
      "biên, và các băng tần biên cũng hội tụ rất nhanh.",
      "The magnitude of variation in frequency is determined by the amplitude "
      "of the carrier wave whereas rate of variation is found by frequency of "
      "the carrier wave. Unlike AM technique, in case of FM, a number of "
      "sidebands are formed, but their intensity goes on decreasing for one "
      "sideband to the other. This decrease is quite effective after a few "
      "sidebands itself and converge also very rapidly.")

    P(b, lang,
      "Ngoài ra, kỹ thuật điều chế tần số có tính chọn lọc băng thông, vì một "
      "phần của dải băng thông gây méo dạng trong tín hiệu đầu ra. Dải băng "
      "thông BW được cho bởi biểu thức:",
      "Also the frequency modulation technique is bandwidth selective because "
      "some of the range of bandwidth creates distortion in the output signal. "
      "The range of bandwidth BW is given by the expression:")
    E(b, lang, "BW = 2(dₘ + f₀)", "BW = 2(dₘ + f₀)", num="4.1")

    P(b, lang,
      "trong đó dₘ là độ lệch cực đại của sóng mang so với tần số tín hiệu đầu "
      "ra, còn f₀ là tần số cực đại của tín hiệu đầu ra.",
      "where dₘ is the maximum deviation of the carrier with respect to output "
      "signal frequency and f₀ is the maximum frequency of the output signal.")

    # ------------------------------------------------------------ 4.3 PM
    H(b, lang,
      "Điều chế pha (PM)",
      "Phase modulation (PM)", level=3)

    P(b, lang,
      "Cuối cùng, điều chế pha được thực hiện bằng cách thay đổi góc pha của "
      "sóng mang theo giá trị tức thời của sóng mang. Độ dịch pha chỉ được xác "
      "định bởi giá trị biên độ của sóng mang; tần số của sóng mang không đóng "
      "vai trò gì trong điều chế pha. Kỹ thuật PM hoàn toàn không phổ biến "
      "trong công việc đo từ xa, vì thế chỉ có ý nghĩa học thuật. Các Hình "
      "4.21, 4.22 và 4.23 lần lượt cho thấy sóng mang, tín hiệu và dạng sóng "
      "đã điều chế.",
      "Lastly the phase modulation is effected by changing the phase angle of "
      "the carrier wave with respect to the instantaneous value of the carrier "
      "wave. The shift in phase is characterized by the value of amplitude of "
      "the carrier wave only. The frequency of the carrier wave does not play "
      "any role in phase modulation. The PM technique is not at all popular in "
      "telemetry work and therefore, is of academic interest only. Figures "
      "4.21, 4.22 and 4.23 show the carrier, the signal and the modulated "
      "waveshape respectively.")
    FIG(b, 21, F.fig_f21(), lang)
    FIG(b, 22, F.fig_f22(), lang)
    FIG(b, 23, F.fig_f23(), lang)

    return b
