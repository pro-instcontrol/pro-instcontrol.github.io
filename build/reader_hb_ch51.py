# -*- coding: utf-8 -*-
"""Handbook Chapter 51 — Immittance Measurement (Đo trở kháng phức).
Run:  python build/reader_hb_ch51.py
"""
import os
import hb_common as C
from hb_common import p, h2, h3, eq, table

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSLUG = "ch51-immittance-measurement"
CH_NO = 51
TITLE_EN = "Immittance Measurement"
TITLE_VI = "Đo trở kháng phức"
BYLINE = "John G. Webster (chủ biên) · CRC Press, 1999"
FIGS = {}


def body_vi():
    b = []
    b.append(p(
        "<b>Trở kháng phức</b> (complex impedance) Z = R + jX = |Z|∠θ, với R là phần thực (điện trở), X phần "
        "ảo (cảm kháng/pHản kháng), |Z| độ lớn và θ góc pha. Đo Z (immittance) cho biết đầy đủ đặc tính của "
        "mạch: từ Z suy được R, L, C, tan δ và Q. Thuật ngữ immittance bao gồm cả trở kháng Z, dẫn nạp Y = 1/Z, "
        "kháng A và dẫn kháng B."))
    b.append(p(
        "Tại tần số f, một điện trở R, cuộn L và tụ C có: Z_R = R, Z_L = jωL, Z_C = 1/(jωC) với ω = 2πf."))

    b.append(h2("51.1 Cầu Wheatstone phức", "Complex Bridge Methods"))
    b.append(p(
        "Các cầu (Wheatstone, Maxwell, Hay, Schering, Wien, Owen) cân bằng một nhánh không biết bằng các nhánh "
        "chuẩn. Cân bằng đòi hỏi cả phần thực lẫn phần ảo bằng không, nên mỗi cầu chỉ đo tốt một họ phần tử "
        "(L, C, hoặc mất mát). Ví dụ cầu Wien đo tụ (R_x nối tiếp C_x) qua hai điều chỉnh; cầu Schering đo điện "
        "môi."))

    b.append(h2("51.2 Phương pháp I–V phức (RF-ADC)", "Complex I–V Method"))
    b.append(p(
        "Cách hiện đại: đặt dòng xác định I qua mẫu và đo đồng thời điện áp V phức bằng ADC tốc độ cao, hoặc "
        "dùng bộ chia thế (potential divider) rồi tính:"))
    b.append(eq("Z = V / I ,   Y = 1/Z = G + jB"))
    b.append(p(
        "Bộ <b>tự cân bằng cầu</b> (auto-balancing bridge) trong LCR meter điều khiển dòng sao cho điện áp trên "
        "điện trở chuẩn tỉ lệ với dòng, tự động tách R và X ở mọi tần số test. Độ chính xác cao (0,05%–0,1%)."))

    b.append(h2("51.3 Phân tích mạng (network analyzer) cho tần số cao", "Network Analyzer at RF"))
    b.append(p(
        "Ở RF/vi ba, trở kháng đo bằng phương pháp <b>phản xạ</b>: bơm sóng qua một điện trở chuẩn (cầu định "
        "hướng, directional coupler) và đo hệ số phản xạ Γ = (Z−Z₀)/(Z+Z₀) (Z₀ = 50 Ω). Từ Γ suy Z. Vector "
        "network analyzer (VNA) quét tần số rộng, vẽ |Z(f)|, θ(f), và hấp thụ công suất."))

    b.append(h2("51.4 Ứng dụng và thông số", "Applications and Specs"))
    b.append(table(
        ["Phương pháp", "Dải tần", "Độ chính xác", "Ứng dụng"],
        [["Cầu (Schering…)", "Âm thanh", "0,1%", "L, C, mất mát"],
         ["Tự cân bằng", "20 Hz–2 MHz", "0,05%–0,1%", "Linh kiện tổng quát"],
         ["I–V phức", "DC–MHz", "0,1%–1%", "Vật liệu, cell"],
         ["VNA (phản xạ)", "MHz–GHz", "1%–5%", "RF, ăng-ten, cáp"]],
        "Bảng 51.1 · Các phương pháp đo trở kháng phức."))

    b.append(h2("Tóm tắt", "Summary"))
    b.append(p(
        "Trở kháng phức Z = R+jX = |Z|∠θ, Y = 1/Z. Cầu cân bằng (Wheatstone/Maxwell/Schering/Wien) đo từng họ "
        "phần tử; tự cân bằng cầu và I–V phức (Z = V/I, Y = G+jB) đo đa năng 0,05%–0,1%. Ở RF dùng VNA đo hệ "
        "số phản xạ Γ = (Z−Z₀)/(Z+Z₀) với Z₀ = 50 Ω. Từ Z suy R, L, C, tanδ, Q."))
    b.append('<div class="chapter-nav">'
             '<a href="%s"><span class="k">← Mục lục</span>Sổ tay</a>'
             '<a href="%s" style="text-align:right;"><span class="k">Mục lục →</span>Sổ tay</a></div>'
             % (C.BASE_VI, C.BASE_VI))
    return "".join(b)


def body_en():
    b = []
    b.append(p(
        "Companion to the Vietnamese translation of Chapter 51. Equations and table of the source are "
        "reproduced below; the prose is not repeated."))
    b.append(p(
        "Complex impedance Z = R + jX = |Z|∠θ (R real, X reactive). Immittance generalizes to Z, admittance "
        "Y = 1/Z = G + jB, and the anti-impedances. At frequency f, Z_R = R, Z_L = jωL, Z_C = 1/(jωC). Bridges "
        "(Wheatstone, Maxwell, Hay, Schering, Wien, Owen) balance an unknown arm against standards; balance "
        "requires both real and imaginary parts to vanish, so each bridge best fits a component family. The "
        "modern complex I–V method drives a known current I and measures the complex voltage V (high-speed ADC) "
        "to get Z = V/I, Y = 1/Z = G + jB; an auto-balancing bridge in an LCR meter controls the current so the "
        "voltage across a standard resistor gives it directly, separating R and X at any test frequency with "
        "0.05%–0.1% accuracy. At RF/microwave, reflection methods use a directional coupler to measure the "
        "reflection coefficient Γ = (Z−Z₀)/(Z+Z₀) (Z₀ = 50 Ω) and back out Z; a VNA sweeps frequency to plot "
        "|Z(f)|, θ(f) and power absorption."))
    b.append(table(
        ["Method", "Freq.", "Accuracy", "Use"],
        [["Bridge", "Audio", "0.1%", "L, C, loss"],
         ["Auto-bal.", "20 Hz–2 MHz", "0.05%–0.1%", "General parts"],
         ["Complex I–V", "DC–MHz", "0.1%–1%", "Materials, cells"],
         ["VNA (refl.)", "MHz–GHz", "1%–5%", "RF, antennas, cables"]],
        "Table 51.1 · Complex-impedance methods."))
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
