# -*- coding: utf-8 -*-
"""Handbook Chapter 85 — Analog-to-Digital Converters (Bộ chuyển đổi tương tự – số).
Run:  python build/reader_hb_ch85.py
"""
import os
import hb_common as C
from hb_common import p, h2, h3, eq, table

CSLUG = 'ch85-analog-to-digital-converters'
CH_NO = 85
TITLE_EN = 'Analog-to-Digital Converters'
TITLE_VI = 'Bộ chuyển đổi tương tự – số'
BYLINE = "John G. Webster (chủ biên) · CRC Press, 1999"
FIGS = {}


def body_vi():
    b = []
    b.append(p('Chương 85 do E. B. Loewenstein (National Instruments) biên soạn, trình bày ADC theo đúng trình tự vật lý của phép chuyển đổi: lấy mẫu, lượng tử hoá, thông số kỹ thuật, các kiến trúc ADC, rồi thiết bị và linh kiện thương mại. Đây là chương khép lại khối Xử lý tín hiệu của sổ tay.'))
    b.append(p('Hai ý tưởng cần nắm chắc: lấy mẫu là phép nhân với một chuỗi xung (nên gây chồng phổ nếu thiếu lọc), còn lượng tử hoá là phép làm tròn không đảo ngược (nên đặt sàn nhiễu cho toàn hệ thống). Mọi thông số còn lại của ADC đều là cách định lượng hai sai số này.'))
    b.append(h2('85.1 Mở đầu', '85.1 Introduction'))
    b.append(p('ADC biến một đại lượng tương tự liên tục theo thời gian và biên độ thành một dãy số hữu hạn. Mạch vào thường gồm bộ điều hoà (khuếch đại/lọc), mạch giữ mẫu (S/H), bộ so sánh hoặc DAC nội, mạch logic mã hoá và điện áp tham chiếu V_ref. Chất lượng của cả chuỗi đo bị giới hạn bởi khâu yếu nhất trong các khâu này, không chỉ bởi số bit danh định.'))
    b.append(h2('85.2 Lấy mẫu', '85.2 Sampling'))
    b.append(p('Lấy mẫu chu kỳ T (tần số f_s = 1/T) tạo ra các ảnh phổ lặp tại mọi bội của f_s. Định lý Nyquist–Shannon đòi hỏi f_s > 2f_max để các ảnh không chồng lên dải nền. Khi vi phạm, thành phần f_in > f_s/2 gập về f_alias = |f_in − k·f_s| và không thể phân biệt với một tín hiệu thật ở tần số thấp đó — kể cả bằng xử lý số sau này.'))
    b.append(eq('x_s(t) = x(t)·Σδ(t − kT) ,   f_alias = |f_in − k·f_s| ,   f_s > 2f_max', '85.1'))
    b.append(p('Tác giả dùng ví dụ kinh điển về <b>hiệu ứng bánh xe ngựa</b>: trong phim 24 khung hình/giây, khi nan hoa quay đúng vào vị trí của nan trước đó giữa hai khung hình, bánh xe trông như đứng yên; quay hơi chậm hơn thì trông như quay ngược. Đó chính là alias trong miền thời gian. Cách duy nhất để tránh là lọc thông thấp <b>trước</b> ADC và chọn f_s đủ cao so với dải chuyển tiếp thực tế của bộ lọc.'))
    b.append(p('Mạch giữ mẫu phải nạp tụ giữ đến sai số nhỏ hơn 1 LSB trong thời gian thu (acquisition time); các hiện tượng aperture delay, aperture jitter và droop (tụ xả trong thời gian chuyển đổi) tạo ra sai số biên độ tăng theo tần số tín hiệu.'))
    b.append(h2('85.3 Lượng tử hoá', '85.3 Quantization'))
    b.append(p('Với N bit và thang đầy V_FS, bước lượng tử q = V_FS/2^N (một LSB). Làm tròn sinh sai số e = x_q − x nằm trong ±q/2; nếu coi e là nhiễu trắng đều, công suất nhiễu là q²/12. Với hình sin toàn thang, suy ra giới hạn trên nổi tiếng của tỉ lệ tín hiệu trên nhiễu.'))
    b.append(eq('q = V_FS/2^N ,   P_q = q²/12 ,   SNR_ideal = 6,02·N + 1,76 dB', '85.2'))
    b.append(p('Mỗi bit tăng thêm 6,02 dB SNR nhưng đồng thời đòi hỏi nhiễu tương tự, nhiễu V_ref và jitter đồng hồ phải thấp đi tương ứng. Đây là lý do một ADC 24 bit trên thực tế hiếm khi đạt 24 bit hiệu dụng: các kiến trúc lấy mẫu quá tốc độ (sigma–delta) đạt được độ phân giải cao bằng cách đổi tốc độ lấy mẫu lấy độ chính xác và dời nhiễu lượng tử lên dải cao (noise shaping), rồi lọc số cắt bỏ.'))
    b.append(h2('85.4 Thông số kỹ thuật của ADC', '85.4 ADC Specifications'))
    b.append(h3('Thang và độ phân giải', 'Range and Resolution'))
    b.append(p('Cần phân biệt thang vào (unipolar 0…V_ref, bipolar ±V_ref), độ phân giải (số bit N) và độ phân giải hiệu dụng (ENOB). Độ phân giải danh định chỉ nói kích thước LSB, không nói độ chính xác; ENOB = (SINAD − 1,76)/6,02 mới phản ánh khả năng thật có tính cả nhiễu và méo.'))
    b.append(h3('Quy ước mã hoá', 'Coding Conventions'))
    b.append(p("Các mã thường gặp: nhị phân thẳng (straight binary) cho thang unipolar, bù hai (two's complement) và offset binary cho thang bipolar, BCD trong đồng hồ đo, và mã bù một / sign-magnitude trong một số hệ cũ. Nhầm quy ước mã là lỗi phổ biến khi đọc dữ liệu thô: cùng một từ 0x8000 có thể là điểm giữa thang hoặc là −V_ref."))
    b.append(h3('Sai số tuyến tính và phi tuyến', 'Linear and Nonlinear Errors'))
    b.append(p('Sai số tuyến tính gồm offset (điểm không lệch) và gain (độ dốc lệch), đều sửa được bằng hiệu chuẩn hai điểm. Sai số phi tuyến gồm DNL (độ lệch độ rộng một bước so với q), INL (độ lệch của đặc tính truyền so với đường thẳng lý tưởng) và <b>mã bị mất</b> (missing code, khi DNL ≤ −1 LSB). INL không sửa được bằng hiệu chuẩn hai điểm và là thông số quyết định trong đo tĩnh chính xác.'))
    b.append(h3('Sai số khẩu độ, nhiễu và dải động', 'Aperture, Noise and Dynamic Range'))
    b.append(p('Jitter σ_t của đồng hồ lấy mẫu giới hạn SNR ở tần số cao theo SNR = −20·log₁₀(2π f_in σ_t). Nhiễu tương tự của tầng vào, nhiễu V_ref và nhiễu lượng tử cộng lại; dải động vô tạp âm (SFDR) và tổng méo hài (THD) đặc trưng khả năng phân biệt tín hiệu nhỏ cạnh tín hiệu lớn.'))
    b.append(eq('SINAD = 20·log₁₀(S/(N+D)) ,   ENOB = (SINAD − 1,76)/6,02 ,   SNR_j = −20·log₁₀(2πf_inσ_t)', '85.3'))
    b.append(table(['Nhóm', 'Thông số', 'Sửa bằng hiệu chuẩn?'], [['Thang', 'V_FS, unipolar/bipolar, N bit', 'Không (do thiết kế)'], ['Tuyến tính', 'Offset, gain error', 'Có (2 điểm + bù nhiệt)'], ['Phi tuyến', 'DNL, INL, missing code', 'Không (bản chất kiến trúc)'], ['Thời gian', 'Aperture jitter, droop', 'Một phần (đồng hồ sạch)'], ['Nhiễu', 'SNR, THD, SFDR, SINAD', 'Một phần (lọc, V_ref)'], ['Tổng hợp', 'ENOB', 'Không']], 'Bảng 85.1 · Các nhóm thông số ADC và khả năng hiệu chuẩn.'))
    b.append(h2('85.5 Các kiểu ADC', '85.5 Types of ADCs'))
    b.append(p('<b>Flash</b> so sánh đồng thời với 2^N−1 ngưỡng, cho một chu kỳ chuyển đổi duy nhất (tới GS·s⁻¹) nhưng số comparator tăng luỹ thừa nên thường chỉ 6–8 bit, tiêu thụ nhiều và nhạy sai lệch ngưỡng. <b>SAR</b> dùng DAC điện dung và tìm kiếm nhị phân N chu kỳ: không có độ trễ ống (pipeline delay), tĩnh, tiết kiệm, rất phù hợp đo đa kênh 8–18 bit. <b>Multistage / pipeline</b> chia conversion qua nhiều tầng độ phân giải thấp, đạt tốc độ cao với độ phân giải trung bình nhưng có độ trễ cố định.'))
    b.append(p('<b>Integrating</b> (dual-slope, multi-slope) tích phân tín hiệu trong một khoảng thời gian được chọn là bội số nguyên của chu kỳ điện lưới: nhiễu 50/60 Hz triệt tiêu đúng về không, nên dù chậm (vài mẫu/giây) vẫn là kiến trúc chuẩn của đồng hồ vạn năng 6½ chữ số. <b>Sigma–delta</b> dùng bộ điều chế bậc thấp 1 bit ở tần số rất cao cộng định hình nhiễu và lọc số decimation, đạt 16–24 bit với độ tuyến tính xuất sắc, đổi lấy độ trễ nhóm lớn (không hợp cho điều khiển vòng kín nhanh). <b>V/F</b> biến điện áp thành tần số xung đếm được, truyền xa dễ và có tính tích phân tự nhiên.'))
    b.append(table(['Kiến trúc', 'Độ phân giải', 'Tốc độ', 'Đặc điểm nổi bật'], [['Flash', '6–8 bit', '0,1–10 GS·s⁻¹', 'Độ trễ 1 chu kỳ, tốn diện tích'], ['SAR', '8–18 bit', '0,1–10 MS·s⁻¹', 'Không độ trễ ống, tiết kiệm'], ['Multistage / pipeline', '10–16 bit', '10–500 MS·s⁻¹', 'Băng rộng, có độ trễ cố định'], ['Integrating', '12–20 bit+', 'Vài S·s⁻¹', 'Triệt nhiễu lưới, tuyến tính cao'], ['Sigma–delta', '16–24 bit', '1 S·s⁻¹ – 10 MS·s⁻¹', 'Định hình nhiễu, lọc số sẵn'], ['V/F', '10–16 bit', 'Thấp–trung bình', 'Tích phân, truyền xa chống nhiễu']], 'Bảng 85.2 · So sánh các kiến trúc ADC theo chương 85.'))
    b.append(h2('85.6 Thiết bị và linh kiện', '85.6 Instrumentation and Components'))
    b.append(p('Ở cấp linh kiện cần phối hợp ADC với mạch giữ mẫu, nguồn tham chiếu có hệ số nhiệt thấp, driver ngõ vào đủ băng để nạp tụ lấy mẫu trong thời gian thu, và đồng hồ có jitter nhỏ. Bố trí mạch tách đất tương tự / đất số, decoupling riêng cho V_ref và đường tín hiệu ngắn là bắt buộc nếu muốn đạt ENOB gần số bit danh định.'))
    b.append(p('Ở cấp thiết bị: card thu thập dữ liệu (DAQ) đa kênh thường dùng SAR + multiplexer (cần chú ý chuyển kênh chưa ổn định gây khâu chéo), đồng hồ vạn năng dùng dual-slope, máy hiện sóng số dùng flash/pipeline, và hệ đo động lực học / âm thanh dùng sigma–delta đồng bộ nhiều kênh. Tiêu chí chọn thực tế luôn là bộ bốn: băng thông, độ phân giải hiệu dụng, số kênh đồng thời và độ trễ.'))
    b.append(h2("Tóm tắt", "Summary"))
    b.append(p('Chương 85 đi từ lấy mẫu (f_s > 2f_max, alias không sửa được sau ADC, ví dụ bánh xe ngựa) đến lượng tử hoá (q = V_FS/2^N, SNR = 6,02N + 1,76 dB). Thông số chia thành thang/mã hoá, sai số tuyến tính (sửa được), phi tuyến DNL/INL (không sửa được), aperture jitter, nhiễu và ENOB. Sáu kiến trúc: flash, SAR, pipeline, integrating, sigma–delta và V/F — mỗi kiểu đánh đổi tốc độ lấy độ phân giải hoặc độ trễ. Chọn ADC phải xét đồng thời V_ref, S/H, đồng hồ và bố trí mạch.'))
    b.append('<div class="chapter-nav">'
             '<a href="%s"><span class="k">← Mục lục</span>Sổ tay</a>'
             '<a href="%s" style="text-align:right;"><span class="k">Mục lục →</span>Sổ tay</a></div>'
             % (C.BASE_VI, C.BASE_VI))
    return "".join(b)


def body_en():
    b = []
    b.append(p('Companion to the Vietnamese translation of Chapter 85. The source prose is not repeated; the governing relations and reference data are summarised below.'))
    b.append(p("E. B. Loewenstein (National Instruments), Analog-to-Digital Converters (CRC, 1999). The chapter follows the physical conversion chain: sampling (x_s = x·Σδ(t−kT), Nyquist f_s > 2 f_max, f_alias = |f_in − k f_s|, the wagon-wheel/stroboscopic illustration, sample-and-hold acquisition, aperture delay/jitter and droop); quantisation (q = V_FS/2^N, noise power q²/12, SNR = 6.02N + 1.76 dB, oversampling and noise shaping); ADC specifications (range/resolution, binary/two's-complement/offset-binary/BCD coding, offset and gain errors, DNL/INL/missing codes, aperture errors, noise, SINAD, SFDR, THD, ENOB and SNR_j = −20 log(2π f_in σ_t)); six converter architectures (flash, SAR, multistage/pipeline, integrating/dual-slope, sigma–delta, V/F); and instrumentation: references, S/H drivers, clocks, analogue/digital ground separation, DAQ boards, DMMs, DSOs and synchronous multi-channel sigma–delta systems."))
    b.append(eq('x_s(t) = x(t)·Σδ(t − kT) ,   f_alias = |f_in − k·f_s| ,   f_s > 2f_max', '85.1'))
    b.append(eq('q = V_FS/2^N ,   P_q = q²/12 ,   SNR_ideal = 6,02·N + 1,76 dB', '85.2'))
    b.append(eq('SINAD = 20·log₁₀(S/(N+D)) ,   ENOB = (SINAD − 1,76)/6,02 ,   SNR_j = −20·log₁₀(2πf_inσ_t)', '85.3'))
    b.append(table(['Group', 'Parameter', 'Calibratable?'], [['Range', 'V_FS, unipolar/bipolar, N bits', 'No (design choice)'], ['Linear', 'Offset, gain error', 'Yes (two-point + temp comp)'], ['Nonlinear', 'DNL, INL, missing codes', 'No (architecture limit)'], ['Timing', 'Aperture jitter, droop', 'Partly (clean clock)'], ['Noise', 'SNR, THD, SFDR, SINAD', 'Partly (filtering, V_ref)'], ['Aggregate', 'ENOB', 'No']], 'Table 85.1 · ADC specification groups and correctability.'))
    b.append(table(['Architecture', 'Resolution', 'Speed', 'Distinguishing feature'], [['Flash', '6–8 bit', '0.1–10 GS·s⁻¹', 'One-cycle latency, large die'], ['SAR', '8–18 bit', '0.1–10 MS·s⁻¹', 'No pipeline delay, low power'], ['Multistage / pipeline', '10–16 bit', '10–500 MS·s⁻¹', 'Wideband, fixed latency'], ['Integrating', '12–20 bit+', 'A few S·s⁻¹', 'Line rejection, high linearity'], ['Sigma–delta', '16–24 bit', '1 S·s⁻¹ – 10 MS·s⁻¹', 'Noise shaping, digital filter'], ['V/F', '10–16 bit', 'Low–medium', 'Integrating, noise-immune transmission']], 'Table 85.2 · ADC architectures compared.'))
    b.append('<div class="chapter-nav">'
             '<a href="%s"><span class="k">← Contents</span>Handbook</a>'
             '<a href="%s" style="text-align:right;"><span class="k">Contents →</span>Handbook</a></div>'
             % (C.BASE_EN, C.BASE_EN))
    return "".join(b)


def main():
    for path in C.write_chapter(CH_NO, CSLUG, TITLE_EN, TITLE_VI, BYLINE,
                                body_vi(), body_en(), FIGS):
        print("wrote %s  %d kB" % (path, os.path.getsize(path) // 1024))


if __name__ == "__main__":
    main()
