# -*- coding: utf-8 -*-
"""Handbook Chapter 83 — Spectrum Analysis and Correlation (Phân tích phổ và tương quan).
Run:  python build/reader_hb_ch83.py
"""
import os
import hb_common as C
from hb_common import p, h2, h3, eq, table

CSLUG = 'ch83-spectrum-analysis-and-correlation'
CH_NO = 83
TITLE_EN = 'Spectrum Analysis and Correlation'
TITLE_VI = 'Phân tích phổ và tương quan'
BYLINE = "John G. Webster (chủ biên) · CRC Press, 1999"
FIGS = {}


def body_vi():
    b = []
    b.append(p('Phân tích phổ biểu diễn tín hiệu theo tần số, còn tương quan định lượng sự tự tương đồng theo thời gian và mối liên hệ giữa hai tín hiệu. Hai công cụ này là nền tảng của chẩn đoán rung động máy, nhận dạng mô thanh, đo độ trễ, phân tích méo và ước lượng đáp ứng hệ thống.'))
    b.append(p('Trên thực tế mọi kết quả đều thu được từ một đoạn tín hiệu hữu hạn đã lấy mẫu, nên rò rỉ phổ, độ phân giải tần số và phương pháp trung bình hoá quan trọng không kém chính biến đổi Fourier.'))
    b.append(h2('83.1 Biến đổi Fourier, DFT và FFT', 'Fourier Transform, DFT and FFT'))
    b.append(p('Biến đổi Fourier liên tục cho phổ của tín hiệu lý thuyết; với N mẫu ở tần số f_s, DFT cho N điểm phổ cách nhau Δf = f_s/N = 1/T. FFT chỉ là thuật toán tính DFT hiệu quả (O(N log N)), thường yêu cầu N là luỹ thừa của 2 hoặc tích các thừa số nhỏ. Độ phân giải tần số chỉ cải thiện bằng cách kéo dài thời gian ghi T, không phải bằng zero-padding (zero-padding chỉ nội suy trực quan).'))
    b.append(eq('X(f) = ∫x(t)e^(−i2πft)dt ,   X[k] = Σ x[n]e^(−i2πkn/N) ,   Δf = f_s/N = 1/T', '83.1'))
    b.append(h2('83.2 Cửa sổ, rò rỉ và ước lượng PSD', 'Windows, Leakage and PSD Estimation'))
    b.append(p('Cắt một đoạn hữu hạn tương đương nhân với cửa sổ chữ nhật, gây rò rỉ (sidelobe −13 dB). Cửa sổ Hann/Hamming/Blackman–Harris giảm sidelobe nhưng nới rộng lobe chính, làm giảm độ phân giải và cần hệ số bù biên độ/công suất. PSD ước lượng bằng periodogram; phương pháp Welch chồng lấp các đoạn, cửa sổ hoá rồi trung bình để đổi phương sai lấy độ phân giải.'))
    b.append(eq('S_xx(f) = (1/(T·|U|))·|X(f)|² ,   U = (1/N)Σw²[n]   (bù công suất cửa sổ)', '83.2'))
    b.append(h2('83.3 Tự tương quan, tương quan chéo và độ kết hợp', 'Autocorrelation, Cross-correlation and Coherence'))
    b.append(p('Tự tương quan R_xx(τ) phát hiện tính chu kỳ bị chìm trong nhiễu (đỉnh tại τ = T₀); định lý Wiener–Khinchin liên hệ nó với PSD qua cặp biến đổi Fourier. Tương quan chéo R_xy(τ) cho độ trễ giữa hai cảm biến — cơ sở đo vận tốc dòng chảy, định vị nguồn âm và ước lượng hàm truyền H(f) = S_xy/S_xx. Hàm kết hợp γ²(f) ∈ [0,1] chỉ mức độ liên hệ tuyến tính tại từng tần số, dùng để kiểm tra chất lượng phép đo FRF.'))
    b.append(eq('R_xx(τ) = E[x(t)x(t+τ)] ,   S_xx(f) = ℱ{R_xx(τ)} ,   γ²_xy = |S_xy|²/(S_xx·S_yy)', '83.3'))
    b.append(table(['Công cụ', 'Miền', 'Cho biết', 'Ứng dụng điển hình'], [['FFT / periodogram', 'Tần số', 'Thành phần phổ', 'Méo hài, tần số quay'], ['Welch PSD', 'Tần số', 'Mật độ công suất ổn định', 'Giám sát rung động'], ['Tự tương quan', 'Thời gian', 'Chu kỳ ẩn', 'Phát hiện lỗi vòng bi'], ['Tương quan chéo', 'Thời gian', 'Độ trễ τ', 'Đo lưu lượng, định vị âm'], ['Độ kết hợp γ²', 'Tần số', 'Mức liên hệ tuyến tính', 'Kiểm định FRF'], ['Cepstrum', 'Quefrency', 'Họ hài / echo', 'Chẩn đoán bánh răng']], 'Bảng 83.1 · Các công cụ phổ và tương quan.'))
    b.append(h2("Tóm tắt", "Summary"))
    b.append(p('Δf = f_s/N = 1/T quyết định độ phân giải; cửa sổ Hann/Blackman đổi rò rỉ lấy độ rộng lobe; Welch trung bình periodogram để giảm phương sai. Wiener–Khinchin nối R_xx với S_xx, tương quan chéo cho độ trễ và H(f) = S_xy/S_xx, còn γ² kiểm định độ tin cậy của đáp ứng tần số.'))
    b.append('<div class="chapter-nav">'
             '<a href="%s"><span class="k">← Mục lục</span>Sổ tay</a>'
             '<a href="%s" style="text-align:right;"><span class="k">Mục lục →</span>Sổ tay</a></div>'
             % (C.BASE_VI, C.BASE_VI))
    return "".join(b)


def body_en():
    b = []
    b.append(p('Companion to the Vietnamese translation of Chapter 83. The source prose is not repeated; the governing relations and reference data are summarised below.'))
    b.append(p("Spectral analysis uses the DFT/FFT with bin spacing Δf = f_s/N = 1/T — resolution depends on record length, not zero padding. Windowing (Hann, Hamming, Blackman–Harris) suppresses leakage sidelobes at the cost of main-lobe width and requires power correction. Welch's averaged periodogram trades resolution for variance. The Wiener–Khinchin theorem links autocorrelation to PSD; cross-correlation yields time delay and H(f) = S_xy/S_xx; magnitude-squared coherence γ² validates FRF measurements."))
    b.append(eq('X(f) = ∫x(t)e^(−i2πft)dt ,   X[k] = Σ x[n]e^(−i2πkn/N) ,   Δf = f_s/N = 1/T', '83.1'))
    b.append(eq('S_xx(f) = (1/(T·|U|))·|X(f)|² ,   U = (1/N)Σw²[n]   (bù công suất cửa sổ)', '83.2'))
    b.append(eq('R_xx(τ) = E[x(t)x(t+τ)] ,   S_xx(f) = ℱ{R_xx(τ)} ,   γ²_xy = |S_xy|²/(S_xx·S_yy)', '83.3'))
    b.append(table(['Tool', 'Domain', 'Reveals', 'Typical use'], [['FFT / periodogram', 'Frequency', 'Spectral components', 'Harmonics, shaft speed'], ['Welch PSD', 'Frequency', 'Stable power density', 'Vibration monitoring'], ['Autocorrelation', 'Time', 'Hidden periodicity', 'Bearing fault detection'], ['Cross-correlation', 'Time', 'Delay τ', 'Flow metering, source location'], ['Coherence γ²', 'Frequency', 'Linear coupling', 'FRF validation'], ['Cepstrum', 'Quefrency', 'Harmonic families / echo', 'Gear diagnosis']], 'Table 83.1 · Spectral and correlation tools.'))
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
