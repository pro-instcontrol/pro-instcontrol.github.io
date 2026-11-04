# -*- coding: utf-8 -*-
"""Handbook Chapter 54 — Noise Measurement (Đo nhiễu).
Run:  python build/reader_hb_ch54.py
"""
import os
import hb_common as C
from hb_common import p, h2, h3, eq, table

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSLUG = "ch54-noise-measurement"
CH_NO = 54
TITLE_EN = "Noise Measurement"
TITLE_VI = "Đo nhiễu"
BYLINE = "John G. Webster (chủ biên) · CRC Press, 1999"
FIGS = {}


def body_vi():
    b = []
    b.append(p(
        "<b>Nhiễu</b> (noise) là tín hiệu ngẫu nhiên giới hạn độ nhỏ nhất có thể đo được. Các nguồn chính: nhiễu "
        "nhiệt (Johnson–Nyquist), nhiễu shot (hạt), nhiễu 1/f (flicker), nhiễu phát xạ. Đo nhiễu xác định giới "
        "hạn thiết bị, tỉ số tín hiệu trên nhiễu (SNR) và hệ số nhiễu (noise figure)."))

    b.append(h2("54.1 Nhiễu nhiệt và mật độ phổ", "Thermal Noise and Spectral Density"))
    b.append(p(
        "Nhiễu nhiệt trên điện trở R ở nhiệt độ T có mật độ phổ điện áp:"))
    b.append(eq("S_V(f) = 4·k·T·R   (V²/Hz) ,   V_n,rms = √(4·k·T·R·B)"))
    b.append(p(
        "với k = 1,38·10⁻²³ J/K, B là băng thông (Hz). Nhiễu là trắng (phẳng theo tần số). Đo nhiễu thường "
        "tính theo mật độ phổ (nV/√Hz) hoặc điện áp rms trên băng B xác định."))

    b.append(h2("54.2 Hệ số nhiễu (noise figure, NF)", "Noise Figure"))
    b.append(p(
        "NF so sánh SNR tại vào và ra của thiết bị; NF = 1 (0 dB) nghĩa là không thêm nhiễu:"))
    b.append(eq("NF = (SNR_in / SNR_out) ,   NF_dB = 10·log₁₀(SNR_in/SNR_out)"))
    b.append(p(
        "Đo NF bằng <b>phương pháp Y-factor</b>: so sánh đầu ra khi nguồn nóng (T_h, load nhiệt) và lạnh "
        "(T_c), qua bộ suy hao chính xác. Hoặc dùng nguồn nhiễu chuẩn (noise source) có mật độ biết trước."))

    b.append(h2("54.3 Phương pháp đo", "Measurement Methods"))
    b.append(p(
        "• <b>True-RMS trên băng</b>: khuếch đại nhiễu qua băng thông B biết trước, đo V_rms rồi quy về mật độ. "
        "• <b>Phân tích phổ</b> (spectrum/FFT): vẽ S(f), tách nhiễu trắng và 1/f. "
        "• <b>So sánh thay thế</b> (substitution): thay nguồn nhiễu chuẩn vào, so sánh chỉ thị. "
        "• <b>Nhiễu tương đương đầu vào</b> (equivalent input noise): đo nhiễu ra chia cho độ lợi để chuẩn hóa."))

    b.append(h2("54.4 Thông số", "Specifications"))
    b.append(table(
        ["Đại lượng", "Công thức", "Đơn vị"],
        [["Mật độ nhiệt", "√(4kTR)", "nV/√Hz"],
         ["Nhiễu rms", "√(4kTRB)", "V (rms)"],
         ["Hệ số nhiễu", "SNR_in/SNR_out", "dB"],
         ["Nhiễu t.đầu vào", "V_out/rms ÷ gain", "V/√Hz"],
         ["SNR", "10·log₁₀(P_s/P_n)", "dB"]],
        "Bảng 54.1 · Các đại lượng đo nhiễu."))

    b.append(h2("Tóm tắt", "Summary"))
    b.append(p(
        "Nhiễu nhiệt V_n = √(4kTRB), mật độ √(4kTR) (nV/√Hz). Hệ số nhiễu NF = SNR_in/SNR_out đo bằng Y-factor "
        "(nguồn nóng/lạnh) hoặc nguồn nhiễu chuẩn. Đo bằng true-RMS trên băng, phân tích phổ (FFT), hoặc so "
        "sánh thay thế. Nhiễu tương đương đầu vào chuẩn hóa theo độ lợi."))
    b.append('<div class="chapter-nav">'
             '<a href="%s"><span class="k">← Mục lục</span>Sổ tay</a>'
             '<a href="%s" style="text-align:right;"><span class="k">Mục lục →</span>Sổ tay</a></div>'
             % (C.BASE_VI, C.BASE_VI))
    return "".join(b)


def body_en():
    b = []
    b.append(p(
        "Companion to the Vietnamese translation of Chapter 54. Equations and table of the source are "
        "reproduced below; the prose is not repeated."))
    b.append(p(
        "Noise is random signal that sets the smallest measurable limit. Principal sources: thermal "
        "(Johnson–Nyquist), shot, flicker (1/f) and emission noise. Thermal noise on resistance R at "
        "temperature T has spectral density S_V(f) = 4kTR (V²/Hz) so V_n,rms = √(4kTRB) with B the bandwidth "
        "— white (flat) noise. Noise is usually stated as spectral density (nV/√Hz). The noise figure NF = "
        "SNR_in/SNR_out (dB = 10log₁₀) measures added noise; NF is found by the Y-factor method comparing output "
        "with a hot (T_h) vs cold (T_c) source through a known attenuator, or with a calibrated noise source. "
        "Measurement methods: true-RMS over a known band (back out density), spectrum/FFT analysis (separates "
        "white and 1/f), substitution against a standard noise source, and equivalent-input-noise (output noise "
        "/ gain). SNR = 10log₁₀(P_s/P_n)."))
    b.append(table(
        ["Quantity", "Formula", "Unit"],
        [["Thermal density", "√(4kTR)", "nV/√Hz"],
         ["Noise rms", "√(4kTRB)", "V (rms)"],
         ["Noise figure", "SNR_in/SNR_out", "dB"],
         ["Equiv. input", "V_out/rms ÷ gain", "V/√Hz"],
         ["SNR", "10log₁₀(P_s/P_n)", "dB"]],
        "Table 54.1 · Noise quantities."))
    b.append('<div class="chapter-nav">'
             '<a href="%s"><span class="k">← Contents</span>Handbook</a>'
             '<a href="%s" style="text-align:right;"><span class="k">Contents →</span>Handbook</a></div>'
             % (C.BASE_EN, C.BASE_EN))
    return "".join(b)


def main():
    for path in C.write_chapter(CH_NO, CSLUG, TITLE_EN, TITLE_VI, BYLINE, body_vi(), body_en(), FIGS):
        print("wrote %s  %d kB" % (path, os.path.getsize(path) // 1024))


if __name__ == "__main__":
    main()
