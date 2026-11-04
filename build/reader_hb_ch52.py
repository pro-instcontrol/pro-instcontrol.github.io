# -*- coding: utf-8 -*-
"""Handbook Chapter 52 — Q Factor Measurement (Đo hệ số Q).
Run:  python build/reader_hb_ch52.py
"""
import os
import hb_common as C
from hb_common import p, h2, h3, eq, table

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSLUG = "ch52-q-factor-measurement"
CH_NO = 52
TITLE_EN = "Q Factor Measurement"
TITLE_VI = "Đo hệ số Q"
BYLINE = "John G. Webster (chủ biên) · CRC Press, 1999"
FIGS = {}


def body_vi():
    b = []
    b.append(p(
        "<b>Hệ số phẩm chất</b> (quality factor) Q đặc trưng cho độ “sắc” của mạch cộng hưởng hoặc linh kiện "
        "phản kháng: Q = ωL/R = 1/(ωCR) = f₀/(B) với B là băng thông −3 dB. Q càng cao, tổn hao càng nhỏ và "
        "đường cộng hưởng càng hẹp. Q của cuộn cảm thường 10–300, của tụ chất lượng cao 500–10000, của thạch "
        "anh hàng vạn."))
    b.append(p(
        "Đo Q có ý nghĩa trong lọc điện, ăng-ten, dao động và cảm biến."))

    b.append(h2("52.1 Q-meter (cộng hưởng biến tần)", "Q-Meter Method"))
    b.append(p(
        "Máy đo Q (Q-meter) mắc nối tiếp cuộn L_x cần đo với tụ chuẩn C qua nguồn áp V_in. Khi cộng hưởng, "
        "điện áp trên tụ V_C = Q·V_in. Đo V_C và V_in cho:"))
    b.append(eq("Q = V_C / V_in   ;   L_x = 1 / ((2πf₀)²·C)"))
    b.append(p(
        "Quét tần số đến cộng hưởng f₀, máy chỉ thị Q trực tiếp. Đây là phương pháp kinh điển, chính xác với "
        "cuộn cảm ở kHz–MHz."))

    b.append(h2("52.2 Phương pháp băng thông", "Bandwidth Method"))
    b.append(p(
        "Kích động mạch cộng hưởng bằng nguồn rộng băng, đo đáp ứng tần số và xác định hai tần số f₁, f₂ tại "
        "điểm −3 dB (0,707 amplitude). Khi đó:"))
    b.append(eq("Q = f₀ / (f₂ − f₁) = f₀ / B"))
    b.append(p(
        "Phương pháp này miễn nhiễm với độ lợi tuyệt đối của thiết bị đo, chỉ cần đo tỉ số tần số. Dùng rộng "
        "rãi với network analyzer."))

    b.append(h2("52.3 Phương pháp suy giảm (decay)", "Decay Method"))
    b.append(p(
        "Kích mạch cộng hưởng rồi ngắt nguồn; biên độ dao động tắt dần theo e^(−t/τ) với thời hằng τ = Q/(πf₀). "
        "Đo độ suy giảm theo thời gian:"))
    b.append(eq("Q = π·f₀·τ"))
    b.append(p(
        "Hữu ích cho cộng hưởng cơ (thạch anh, tinh thể áp điện) và hốc cộng hưởng, nơi Q rất cao."))

    b.append(h2("52.4 Thông số", "Specifications"))
    b.append(table(
        ["Phương pháp", "Dải Q", "Tần số", "Ghi chú"],
        [["Q-meter", "10–1000", "kHz–MHz", "Chỉ thị trực tiếp"],
         ["Băng thông", "1–10⁶", "DC–GHz", "Miễn độ lợi"],
         ["Suy giảm", "10³–10⁶", "Âm thanh–RF", "Q rất cao"],
         ["Cầu", "1–1000", "Âm thanh", "Dùng chung LCR"]],
        "Bảng 52.1 · Các phương pháp đo Q."))

    b.append(h2("Tóm tắt", "Summary"))
    b.append(p(
        "Hệ số Q = ωL/R = f₀/B = V_C/V_in (Q-meter) = πf₀τ (suy giảm). Q-meter đo V_C = Q·V_in tại cộng hưởng; "
        "phương pháp băng thông dùng Q = f₀/(f₂−f₁); suy giảm dùng Q = πf₀τ. Q cao ⇔ tổn hao thấp, đường cộng "
        "hưởng hẹp."))
    b.append('<div class="chapter-nav">'
             '<a href="%s"><span class="k">← Mục lục</span>Sổ tay</a>'
             '<a href="%s" style="text-align:right;"><span class="k">Mục lục →</span>Sổ tay</a></div>'
             % (C.BASE_VI, C.BASE_VI))
    return "".join(b)


def body_en():
    b = []
    b.append(p(
        "Companion to the Vietnamese translation of Chapter 52. Equations and table of the source are "
        "reproduced below; the prose is not repeated."))
    b.append(p(
        "Quality factor Q = ωL/R = 1/(ωCR) = f₀/B (B = −3 dB bandwidth) characterizes resonance sharpness; "
        "higher Q means lower loss and a narrower resonance. The Q-meter drives the unknown L_x in series with "
        "a standard C at V_in and, at resonance, reads the capacitor voltage V_C = Q·V_in, so Q = V_C/V_in and "
        "L_x = 1/((2πf₀)²C) — direct reading at kHz–MHz. The bandwidth method excites the resonator broadband "
        "and finds the −3 dB frequencies f₁, f₂, giving Q = f₀/(f₂−f₁); it is immune to absolute gain. The decay "
        "method rings the resonator then disconnects the source; amplitude decays as e^(−t/τ) with τ = Q/(πf₀), "
        "so Q = πf₀τ — ideal for very high-Q mechanical/resonator elements. Typical Q: coils 10–300, good caps "
        "500–10⁴, quartz 10⁴–10⁶."))
    b.append(table(
        ["Method", "Q range", "Frequency", "Note"],
        [["Q-meter", "10–1000", "kHz–MHz", "Direct reading"],
         ["Bandwidth", "1–10⁶", "DC–GHz", "Gain-immune"],
         ["Decay", "10³–10⁶", "Audio–RF", "Very high Q"],
         ["Bridge", "1–1000", "Audio", "With LCR"]],
        "Table 52.1 · Q-measurement methods."))
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
