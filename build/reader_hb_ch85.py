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
    b.append(p('ADC là cầu nối giữa miền tương tự liên tục và miền số rời rạc, gồm ba bước: lấy mẫu theo thời gian (sample-and-hold), lượng tử hoá biên độ và mã hoá thành từ N bit. Mọi sai số tại đây đều không thể sửa ở hạ nguồn.'))
    b.append(p('Chọn ADC là cân bằng giữa tốc độ, độ phân giải, độ tuyến tính, công suất và chi phí: SAR cho đo đa kênh trung tốc, sigma–delta cho độ phân giải cao, flash cho băng siêu rộng, dual-slope cho đồng hồ đo chống nhiễu lưới.'))
    b.append(h2('85.1 Lấy mẫu, Nyquist và chồng phổ', 'Sampling, Nyquist and Aliasing'))
    b.append(p('Tín hiệu có băng f_max phải lấy mẫu ở f_s > 2f_max; nếu không, thành phần trên f_s/2 gập về dải nền (alias) và không thể phân biệt với tín hiệu thật. Vì bộ lọc chống chồng phổ thực tế có dải chuyển tiếp hữu hạn, thường chọn f_s = 2,5–10 lần f_max kèm lọc thông thấp bậc cao.'))
    b.append(eq('f_s > 2·f_max ,   f_alias = |f_in − k·f_s| ,   q = V_FS/2^N   (LSB)', '85.1'))
    b.append(h2('85.2 Lượng tử hoá, SNR lý tưởng và ENOB', 'Quantisation, Ideal SNR and ENOB'))
    b.append(p('Lượng tử hoá thêm nhiễu trải đều trong ±q/2 với công suất q²/12. Với tín hiểu hình sin toàn thang, tỉ lệ tín hiệu trên nhiễu lượng tử là SNR = 6,02N + 1,76 dB. Thực tế méo hài, nhiễu nhiệt, jitter xung đồng hồ và phi tuyến làm giảm SINAD, từ đó ENOB luôn nhỏ hơn số bit danh định.'))
    b.append(eq('SNR_ideal = 6,02·N + 1,76 dB ,   SINAD = 20·log₁₀(S/(N+D)) ,   ENOB = (SINAD − 1,76)/6,02', '85.2'))
    b.append(h2('85.3 Kiến trúc và sai số tĩnh', 'Architectures and Static Errors'))
    b.append(p('Flash so sánh song song 2^N − 1 ngưỡng, nhanh nhất (GS·s⁻¹) nhưng tốn diện tích và công suất; SAR dùng tìm kiếm nhị phân với một DAC điện dung, cân bằng tốt ở 8–18 bit, 0,1–10 MS·s⁻¹; sigma–delta lấy mẫu quá tốc độ kèm định hình nhiễu, đạt 16–24 bit ở tốc độ thấp; dual-slope/integrating tích phân trong đúng chu kỳ lưới để triệt nhiễu 50/60 Hz. Sai số tĩnh gồm offset, gain, DNL, INL và các mã bị mất.'))
    b.append(table(['Kiến trúc', 'Độ phân giải', 'Tốc độ', 'Ưu điểm'], [['Flash', '6–8 bit', '0,1–10 GS·s⁻¹', 'Độ trễ cực thấp'], ['Pipeline', '10–16 bit', '10–500 MS·s⁻¹', 'Băng rộng'], ['SAR', '8–18 bit', '0,1–10 MS·s⁻¹', 'Không độ trễ ống, tiết kiệm'], ['Sigma–delta', '16–24 bit', '1 S·s⁻¹ – 10 MS·s⁻¹', 'ENOB cao, lọc số sẵn'], ['Dual-slope', '12–20 bit', 'Vài S·s⁻¹', 'Triệt nhiễu lưới, rẻ']], 'Bảng 85.1 · So sánh kiến trúc ADC.'))
    b.append(h2('85.4 Mạch giữ mẫu, tham chiếu và hiệu chuẩn', 'Sample-and-Hold, Reference and Calibration'))
    b.append(p('Mạch S/H phải ổn định trong thời gian chuyển đổi; jitter đồng hồ gây sai số SNR_jitter = −20·log₁₀(2π·f_in·σ_t). Độ ổn định và nhiễu của điện áp tham chiếu V_ref cộng trực tiếp vào kết quả, nên dùng tham chiếu có trôi thấp, tách decoupling và bố trí mặt đất tương tự riêng. Hiệu chuẩn offset/gain hai điểm và bù nhiệt độ là bắt buộc với phép đo chính xác.'))
    b.append(eq('SNR_jitter = −20·log₁₀(2π·f_in·σ_t) ,   V_in = (D/2^N)·V_ref', '85.3'))
    b.append(h2("Tóm tắt", "Summary"))
    b.append(p('Ba bước: lấy mẫu (f_s > 2f_max + lọc chống chồng phổ), lượng tử hoá (q = V_FS/2^N), mã hoá. SNR lý tưởng = 6,02N + 1,76 dB; ENOB = (SINAD − 1,76)/6,02 phản ánh hiệu năng thực. Chọn flash/pipeline cho tốc độ, SAR cho đa kênh, sigma–delta cho độ phân giải, dual-slope cho đồng hồ đo; V_ref, jitter và INL/DNL là sai số then chốt.'))
    b.append('<div class="chapter-nav">'
             '<a href="%s"><span class="k">← Mục lục</span>Sổ tay</a>'
             '<a href="%s" style="text-align:right;"><span class="k">Mục lục →</span>Sổ tay</a></div>'
             % (C.BASE_VI, C.BASE_VI))
    return "".join(b)


def body_en():
    b = []
    b.append(p('Companion to the Vietnamese translation of Chapter 85. The source prose is not repeated; the governing relations and reference data are summarised below.'))
    b.append(p('An ADC samples, quantises and codes: f_s > 2 f_max with an anti-alias filter, q = V_FS/2^N, and ideal SNR = 6.02N + 1.76 dB for a full-scale sine. Real performance is captured by SINAD and ENOB = (SINAD − 1.76)/6.02, degraded by thermal noise, clock jitter (SNR = −20 log(2π f_in σ_t)), DNL/INL and reference drift. Flash/pipeline suit multi-GS/s capture, SAR suits multiplexed medium-speed measurements, sigma–delta oversampling with noise shaping reaches 16–24 bit, and dual-slope integrating converters reject 50/60 Hz line noise in DMMs. Two-point offset/gain calibration and a quiet, decoupled V_ref are mandatory for accurate work.'))
    b.append(eq('f_s > 2·f_max ,   f_alias = |f_in − k·f_s| ,   q = V_FS/2^N   (LSB)', '85.1'))
    b.append(eq('SNR_ideal = 6,02·N + 1,76 dB ,   SINAD = 20·log₁₀(S/(N+D)) ,   ENOB = (SINAD − 1,76)/6,02', '85.2'))
    b.append(table(['Architecture', 'Resolution', 'Speed', 'Advantage'], [['Flash', '6–8 bit', '0.1–10 GS·s⁻¹', 'Minimum latency'], ['Pipeline', '10–16 bit', '10–500 MS·s⁻¹', 'Wide bandwidth'], ['SAR', '8–18 bit', '0.1–10 MS·s⁻¹', 'No pipeline delay, low power'], ['Sigma–delta', '16–24 bit', '1 S·s⁻¹ – 10 MS·s⁻¹', 'High ENOB, digital filter'], ['Dual-slope', '12–20 bit', 'A few S·s⁻¹', 'Line rejection, low cost']], 'Table 85.1 · ADC architecture comparison.'))
    b.append(eq('SNR_jitter = −20·log₁₀(2π·f_in·σ_t) ,   V_in = (D/2^N)·V_ref', '85.3'))
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
