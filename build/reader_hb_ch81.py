# -*- coding: utf-8 -*-
"""Handbook Chapter 81 — Modulation (Điều chế).
Run:  python build/reader_hb_ch81.py
"""
import os
import hb_common as C
from hb_common import p, h2, h3, eq, table

CSLUG = 'ch81-modulation'
CH_NO = 81
TITLE_EN = 'Modulation'
TITLE_VI = 'Điều chế'
BYLINE = "John G. Webster (chủ biên) · CRC Press, 1999"
FIGS = {}


def body_vi():
    b = []
    b.append(p('Điều chế dịch phổ tín hiệu đo lên quanh một sóng mang để truyền dẫn xa, ghép kênh, tránh nhiễu 1/f và tách tín hiệu khỏi trôi DC. Trong đo lường, điều chế còn là nền tảng của khuếch đại khoá pha (lock-in), đo cầu xoay chiều và cảm biến điện dung/điện cảm.'))
    b.append(p('Ba biến có thể điều chế là biên độ (AM/ASK), tần số (FM/FSK) và pha (PM/PSK); với tín hiệu số còn có điều chế xung (PAM, PWM, PPM, PCM) và điều chế sigma–delta.'))
    b.append(h2('81.1 Điều chế biên độ và giải điều chế đồng bộ', 'Amplitude Modulation and Synchronous Detection'))
    b.append(p('Tín hiệu AM gồm sóng mang và hai dải biên; chỉ số điều chế m ≤ 1 để tránh quá điều chế. Trong đo lường, AM kết hợp giải điều chế đồng bộ (nhân với tham chiếu cùng pha rồi lọc thông thấp) tạo thành lock-in amplifier: chỉ thành phần cùng tần số và pha được giữ lại, nhiễu ở mọi tần số khác bị loại bỏ bởi hằng số thời gian của bộ lọc.'))
    b.append(eq('s(t) = A_c[1 + m·cos(ω_m t)]·cos(ω_c t) ,   B_AM = 2·f_m', '81.1'))
    b.append(eq('s(t)·2cos(ω_c t) → LPF → A_c·m·cos(ω_m t + φ)   (Q∝cos φ, I∝sin φ)', '81.2'))
    b.append(h2('81.2 Điều chế tần số, pha và quy tắc Carson', "FM, PM and Carson's Rule"))
    b.append(p('FM/PM giữ biên độ không đổi nên chịu nhiễu biên độ và phi tuyến công suất tốt hơn, đổi lấy băng thông rộng hơn. Chỉ số điều chế β = Δf/f_m quyết định số dải biên đáng kể; băng thông ước lượng bằng quy tắc Carson. FM băng hẹp (β < 1) dùng trong telemetry cảm biến, FM băng rộng cho truyền dẫn chất lượng cao.'))
    b.append(eq('s_FM(t) = A_c·cos[ω_c t + β·sin(ω_m t)] ,   β = Δf/f_m ,   B ≈ 2(Δf + f_m)', '81.3'))
    b.append(h2('81.3 Điều chế xung và lấy mẫu', 'Pulse Modulation and Sampling'))
    b.append(p('PAM lấy biên độ mẫu, PWM độ rộng xung, PPM vị trí xung — cả ba vẫn là tương tự. PCM lượng tử hoá và mã hoá thành từ nhị phân, là cầu nối sang ADC. Điều chế sigma–delta dùng lấy mẫu quá tốc độ (oversampling) và định hình nhiễu (noise shaping) để dời nhiễu lượng tử lên tần số cao, rồi lọc số cắt bỏ.'))
    b.append(eq('f_s ≥ 2·f_max (Nyquist) ,   OSR = f_s/(2·f_B) ,   SNR ↑ 3 dB mỗi lần OSR ×2', '81.4'))
    b.append(table(['Kiểu', 'Tham số mang', 'Băng thông', 'Ưu điểm chính'], [['AM / ASK', 'Biên độ', '2f_m', 'Đơn giản, giải điều chế rẻ'], ['FM / FSK', 'Tần số', '2(Δf+f_m)', 'Chịu nhiễu biên độ'], ['PM / PSK', 'Pha', '≈ 2f_m', 'Hiệu suất phổ cao'], ['PWM / PPM', 'Độ rộng / vị trí', 'Rộng', 'Điều khiển công suất'], ['PCM', 'Mã nhị phân', 'N·f_s', 'Chống nhiễu, lưu trữ số'], ['Sigma–delta', 'Mật độ xung', 'f_s ≫ 2f_B', 'Độ phân giải cao']], 'Bảng 81.1 · So sánh các phương pháp điều chế.'))
    b.append(h2("Tóm tắt", "Summary"))
    b.append(p('Điều chế dời tín hiệu lên sóng mang: AM (B = 2f_m) kết hợp giải điều chế đồng bộ tạo lock-in triệt nhiễu; FM/PM đổi băng thông lấy khả năng chống nhiễu (quy tắc Carson B ≈ 2(Δf+f_m)); PWM/PPM/PCM và sigma–delta nối sang miền số. Luôn thoả f_s ≥ 2f_max và lọc chống chồng phổ.'))
    b.append('<div class="chapter-nav">'
             '<a href="%s"><span class="k">← Mục lục</span>Sổ tay</a>'
             '<a href="%s" style="text-align:right;"><span class="k">Mục lục →</span>Sổ tay</a></div>'
             % (C.BASE_VI, C.BASE_VI))
    return "".join(b)


def body_en():
    b = []
    b.append(p('Companion to the Vietnamese translation of Chapter 81. The source prose is not repeated; the governing relations and reference data are summarised below.'))
    b.append(p('Modulation translates a measurement signal to a carrier for transmission, multiplexing and 1/f-noise avoidance. AM (m ≤ 1, B = 2 f_m) with synchronous demodulation is the basis of lock-in detection, where the low-pass time constant sets the equivalent noise bandwidth. FM/PM trade bandwidth (Carson: B ≈ 2(Δf + f_m), beta = Δf/f_m) for amplitude noise immunity. Pulse schemes (PAM, PWM, PPM, PCM) lead to sampling and sigma–delta oversampling with noise shaping; Nyquist f_s ≥ 2 f_max must always be respected with an anti-alias filter.'))
    b.append(eq('s(t) = A_c[1 + m·cos(ω_m t)]·cos(ω_c t) ,   B_AM = 2·f_m', '81.1'))
    b.append(eq('s(t)·2cos(ω_c t) → LPF → A_c·m·cos(ω_m t + φ)   (Q∝cos φ, I∝sin φ)', '81.2'))
    b.append(eq('s_FM(t) = A_c·cos[ω_c t + β·sin(ω_m t)] ,   β = Δf/f_m ,   B ≈ 2(Δf + f_m)', '81.3'))
    b.append(eq('f_s ≥ 2·f_max (Nyquist) ,   OSR = f_s/(2·f_B) ,   SNR ↑ 3 dB mỗi lần OSR ×2', '81.4'))
    b.append(table(['Scheme', 'Carrier parameter', 'Bandwidth', 'Main advantage'], [['AM / ASK', 'Amplitude', '2f_m', 'Simple, cheap demodulation'], ['FM / FSK', 'Frequency', '2(Δf+f_m)', 'Rejects amplitude noise'], ['PM / PSK', 'Phase', '≈ 2f_m', 'Spectral efficiency'], ['PWM / PPM', 'Width / position', 'Wide', 'Power control'], ['PCM', 'Binary code', 'N·f_s', 'Noise immunity, digital storage'], ['Sigma–delta', 'Pulse density', 'f_s ≫ 2f_B', 'High resolution']], 'Table 81.1 · Modulation schemes.'))
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
