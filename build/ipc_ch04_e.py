# -*- coding: utf-8 -*-
"""Chapter 4, "Telemetry", section 4.4 "Pulse Telemetry" (EN/VI bilingual).

Source: Prasad, Jayaswal & Priye, *Instrumentation and Process Control*
(I.K. International, 2019), PDF pp. 233-235, printed pp. 221-223, decoded text
lines 8852-8906.  Covered here are pulse amplitude modulation (PAM), pulse
duration/width modulation (PDM/PWM) and pulse position modulation (PPM),
together with the power-versus-bandwidth trade-off of the last technique.
The three waveforms (Figures 4.24-4.26) are redrawn as vectors in the
`ipcfig4_b` supplier module and placed where the text refers to them.
"""

import ipcfig4 as F
from ipc_ch04_lib import H, P, L, E, FIG, TBL, NOTE


def section(lang):
    b = []

    # ---------------------------------------------------------------- 4.4
    H(b, lang,
      "4.4 Đo từ xa xung",
      "4.4 Pulse Telemetry")

    P(b, lang,
      "Cho đến nay chúng ta mới chỉ xét dạng sóng tín hiệu cùng loại với sóng "
      "mang, tức là dạng sin. Cách xử lý sẽ hoàn toàn khác nếu ta coi dạng sóng "
      "tín hiệu gồm một chuỗi các xung (có dạng chữ nhật). Kỹ thuật điều chế vì "
      "thế cũng thay đổi tương ứng và được trình bày dưới đây.",
      "Till now we have considered the signal waveform to be of the same type "
      "as the carrier wave, i.e. sinusoidal in form. The treatment will be "
      "entirely different if we consider the signal waveform to consist of a "
      "train of pulses (of rectangular shape). The modulation technique will "
      "also change accordingly and is described below.")

    # ------------------------------------------------------------ 4.4.1 PAM
    H(b, lang,
      "Điều chế biên độ xung (PAM)",
      "Pulse Amplitude Modulation (PAM)", level=3)

    P(b, lang,
      "Trong kỹ thuật điều chế này, chuỗi xung (tức dạng sóng tín hiệu thực tế) "
      "có tần số không đổi. Sóng mang được điều chế sao cho chiều cao, tức biên "
      "độ của sóng thu được, mang giá trị tín hiệu thực tế như thể hiện ở Hình "
      "4.24.",
      "In this modulation technique, the trains of pulses (the actual signal "
      "waveform) have constant frequency. The carrier waveform is modulated in "
      "such a way that the heights, i.e. the amplitude of the resultant wave, "
      "carry the actual signal value, as shown in Figure 4.24.")
    FIG(b, 24, F.fig_f24(), lang)

    # ------------------------------------------------------------ 4.4.2 PDM
    H(b, lang,
      "Điều chế độ dài xung (PDM)",
      "Pulse Duration Modulation (PDM)", level=3)

    P(b, lang,
      "Trong biến thể này của kỹ thuật điều chế, biên độ của xung được giữ "
      "không đổi và sự thay đổi độ dài của xung biểu thị giá trị của sóng tín "
      "hiệu. Kỹ thuật này còn được gọi là điều chế độ rộng xung (PWM). Độ rộng "
      "hay độ dài của xung biểu thị giá trị cường độ tín hiệu như thể hiện ở "
      "Hình 4.25.",
      "In this variation of the modulation technique, the amplitude of the "
      "pulse is kept constant and a change in the duration of a pulse signifies "
      "the value of the signal wave. This is also known as pulse width "
      "modulation (PWM). The width or duration of the pulse represents the "
      "value of the signal strength, as shown in Figure 4.25.")
    FIG(b, 25, F.fig_f25(), lang)

    NOTE(b, lang,
      "t₁, t₂ và t₃ là các độ dài xung; w₁, w₂ và w₃ là các độ rộng xung.",
      "t₁, t₂ and t₃ are durations; w₁, w₂ and w₃ are widths.")

    P(b, lang,
      "Kỹ thuật PDM hoặc PWM có thể được biến đổi bằng cách thay xung hiện có "
      "bằng một xung có độ dài ngắn như thể hiện ở Hình 4.26.",
      "The technique of PDM or PWM can be modified by replacing the existing "
      "pulse with a pulse of short duration, as shown in Figure 4.26.")
    FIG(b, 26, F.fig_f26(), lang)

    P(b, lang,
      "Đây được gọi là điều chế vị trí xung (PPM). Ưu điểm của PPM là dùng ít "
      "công suất hơn so với PDM hoặc PWM, nhưng nhược điểm là cần băng thông "
      "lớn hơn để truyền tải.",
      "This is called pulse position modulation (PPM). Its advantage is that "
      "PPM uses less power with respect to PDM or PWM, but the disadvantage is "
      "that it needs a larger bandwidth for transmission.")

    return b
