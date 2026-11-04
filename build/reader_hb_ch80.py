# -*- coding: utf-8 -*-
"""Handbook Chapter 80 — Amplifiers and Signal Conditioners (Bộ khuếch đại và điều hoà tín hiệu).
Run:  python build/reader_hb_ch80.py
"""
import os
import hb_common as C
from hb_common import p, h2, h3, eq, table

CSLUG = 'ch80-amplifiers-and-signal-conditioners'
CH_NO = 80
TITLE_EN = 'Amplifiers and Signal Conditioners'
TITLE_VI = 'Bộ khuếch đại và điều hoà tín hiệu'
BYLINE = "John G. Webster (chủ biên) · CRC Press, 1999"
FIGS = {}


def body_vi():
    b = []
    b.append(p('Tín hiệu cảm biến thường nhỏ (µV–mV), có trở kháng nguồn cao, chồng nhiễu và lệch mức DC. Bộ điều hoà tín hiệu thực hiện khuếch đại, cách ly, lọc, bù offset, kích thích cầu đo và chuẩn hoá về dải vào của ADC (0–5 V, ±10 V hoặc 4–20 mA).'))
    b.append(p('Chất lượng của toàn chuỗi đo thường do tầng đầu quyết định: một khi nhiễu đã lẫn vào tín hiệu ở tầng vào, không tầng khuếch đại hay lọc số nào về sau khôi phục được.'))
    b.append(h2('80.1 Khuếch đại dụng cụ', 'Instrumentation Amplifier'))
    b.append(p('Cấu trúc ba op-amp (hai tầng đệm không đảo + một tầng vi phân) cho trở vào rất cao (>10⁹ Ω), độ lợi đặt bằng một điện trở R_G duy nhất và CMRR cao. Điện trở phải được ghép cặp tinh vi; sai lệch 0,1 % giữa các nhánh có thể kéo CMRR xuống dưới 60 dB. Chọn op-amp có điện áp offset thấp, trôi thấp và nhiễu 1/f nhỏ cho tín hiệu DC.'))
    b.append(eq('G = 1 + 2R/R_G ,   CMRR_dB = 20·log₁₀(A_d/A_cm) ,   V_o = G·(V₂ − V₁) + V_ref', '80.1'))
    b.append(h2('80.2 Cách ly, chopper và điều hoà cầu đo', 'Isolation, Chopper and Bridge Conditioning'))
    b.append(p('Bộ khuếch đại cách ly (quang, biến áp hoặc điện dung) cắt vòng nối đất, chịu điện áp mode chung hàng kV và bảo vệ người/ thiết bị — bắt buộc trong đo y sinh và điện lực. Chopper / auto-zero liên tục đo và trừ offset, đưa trôi xuống dưới 0,1 µV·K⁻¹ nhưng phát sinh nhiễu chuyển mạch. Cầu Wheatstone cần nguồn kích thích ổn định (tỉ lệ với V_ref để triệt trôi nguồn), cảm biến đo xa dùng cấu hình 3 dây/4 dây để bù điện trở dây dẫn.'))
    b.append(eq('V_bridge ≈ V_ex·(ΔR/(4R)) ,   V_o ∝ V_ex·ε·G   (cảm biến biến dạng)', '80.2'))
    b.append(h2('80.3 Nhiễu, lọc và truyền dẫn', 'Noise, Filtering and Transmission'))
    b.append(p('Nguồn nhiễu gồm nhiễu Johnson √(4kTRB), nhiễu dòng/áp của op-amp, nhiễu 1/f và nhiễu mode chung lưới 50/60 Hz. Đặt bộ lọc chống chồng phổ (anti-aliasing) ngay trước ADC, dùng dây xoắn che chắn, nối đất một điểm và tách khối tương tự/khối số. Truyền dẫn đường dài dùng vòng dòng 4–20 mA vì không nhạy sụt áp trên dây và dễ phát hiện đứt dây.'))
    b.append(eq('v_n,rms = √(4kTRB) ,   NF = 10·log₁₀(SNR_in/SNR_out) ,   f_c = 1/(2πRC)', '80.3'))
    b.append(table(['Tầng', 'Chức năng', 'Tham số then chốt'], [['Bảo vệ / EMI', 'Giới hạn quá áp, lọc RC', 'Điện áp đánh thủng'], ['Khuếch đại dụng cụ', 'Độ lợi vi phân', 'CMRR > 100 dB, Z_in > 1 GΩ'], ['Cách ly', 'Cắt vòng đất', '2–5 kV, rò < 1 µA'], ['Lọc', 'Chống chồng phổ', 'Bậc, tần số cắt, pha'], ['Chuẩn hoá', 'V/I, 4–20 mA', 'Độ tuyến tính, tải'], ['Kích thích', 'Nguồn cầu / RTD', 'Ổn định, tỉ lệ V_ref']], 'Bảng 80.1 · Các tầng điển hình của chuỗi điều hoà tín hiệu.'))
    b.append(h2("Tóm tắt", "Summary"))
    b.append(p('Tầng vào quyết định độ tin cậy: khuếch đại dụng cụ (G = 1 + 2R/R_G, CMRR > 100 dB), cách ly an toàn, kích thích cầu tỉ lệ, lọc chống chồng phổ và chuẩn hoá 4–20 mA. Nhiễu Johnson √(4kTRB), offset/trôi và vòng nối đất là ba nguồn sai số cần xử lý trước khi số hoá.'))
    b.append('<div class="chapter-nav">'
             '<a href="%s"><span class="k">← Mục lục</span>Sổ tay</a>'
             '<a href="%s" style="text-align:right;"><span class="k">Mục lục →</span>Sổ tay</a></div>'
             % (C.BASE_VI, C.BASE_VI))
    return "".join(b)


def body_en():
    b = []
    b.append(p('Companion to the Vietnamese translation of Chapter 80. The source prose is not repeated; the governing relations and reference data are summarised below.'))
    b.append(p('Signal conditioning amplifies, isolates, filters and scales µV–mV sensor outputs to the ADC input range. The three-op-amp instrumentation amplifier gives G = 1 + 2R/R_G with very high input impedance and CMRR > 100 dB; resistor matching largely sets the actual CMRR. Isolation amplifiers break ground loops (2–5 kV), chopper/auto-zero stages remove offset drift, ratiometric bridge excitation cancels supply drift, and 3-/4-wire connections compensate lead resistance. Johnson noise sqrt(4kTRB), 1/f noise and 50/60 Hz pickup set the floor; anti-alias filtering and 4–20 mA current loops complete the chain.'))
    b.append(eq('G = 1 + 2R/R_G ,   CMRR_dB = 20·log₁₀(A_d/A_cm) ,   V_o = G·(V₂ − V₁) + V_ref', '80.1'))
    b.append(eq('V_bridge ≈ V_ex·(ΔR/(4R)) ,   V_o ∝ V_ex·ε·G   (cảm biến biến dạng)', '80.2'))
    b.append(eq('v_n,rms = √(4kTRB) ,   NF = 10·log₁₀(SNR_in/SNR_out) ,   f_c = 1/(2πRC)', '80.3'))
    b.append(table(['Stage', 'Function', 'Key parameter'], [['Protection / EMI', 'Overvoltage clamp, RC filter', 'Breakdown voltage'], ['Instrumentation amp', 'Differential gain', 'CMRR > 100 dB, Z_in > 1 GΩ'], ['Isolation', 'Break ground loops', '2–5 kV, leakage < 1 µA'], ['Filtering', 'Anti-aliasing', 'Order, cutoff, phase'], ['Scaling', 'V/I, 4–20 mA', 'Linearity, load'], ['Excitation', 'Bridge / RTD source', 'Stability, ratiometric to V_ref']], 'Table 80.1 · Typical signal-conditioning stages.'))
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
