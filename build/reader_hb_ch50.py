# -*- coding: utf-8 -*-
"""Handbook Chapter 50 — Inductance Measurement (Đo điện cảm).
Run:  python build/reader_hb_ch50.py
"""
import os
import hb_common as C
from hb_common import p, h2, h3, eq, table

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSLUG = "ch50-inductance-measurement"
CH_NO = 50
TITLE_EN = "Inductance Measurement"
TITLE_VI = "Đo điện cảm"
BYLINE = "John G. Webster (chủ biên) · CRC Press, 1999"
FIGS = {}


def body_vi():
    b = []
    b.append(p(
        "Điện cảm (inductance) L = Φ/I = N·Φ/I, đơn vị henry (H). Với cuộn có lõi, L phụ thuộc độ từ thẩm và "
        "hình học. Đo L dùng để kiểm tra cuộn cảm, biến áp, cảm biến vị trí (LVDT) và linh kiện."))
    b.append(p(
        "Thực tế, mọi cuộn đều có điện trở dây dẫn R_s (tổn hao) và điện dung rò rải rác, nên đo L phải tách "
        "biệt thành phần phản kháng khỏi tổn hao."))

    b.append(h2("50.1 Cầu Maxwell, Hay và Anderson", "Maxwell, Hay and Anderson Bridges"))
    b.append(p(
        "Các cầu này cân bằng một cuộn cảm L_x (nối tiếp R_x) với tụ chuẩn C_s và trở. <b>Cầu Maxwell</b> "
        "(hay cầu Maxwell-Wien) dùng một nhánh RC song song đối với nhánh L_x, cân bằng độc lập tần số ở tần số "
        "điện lưới. <b>Cầu Hay</b> dùng nhánh RL chuẩn. <b>Cầu Anderson</b> chính xác hơn, dùng thêm trở phụ để "
        "triệt sai số do tụ rò."))
    b.append(eq("L_x = R₁·R₃·C_s   (Maxwell, với R₁,R₃ là hai nhánh cầu)"))

    b.append(h2("50.2 Cộng hưởng và LCR meter", "Resonance and LCR Meter"))
    b.append(p(
        "Đưa cuộn vào mạch cộng hưởng LC: tần số cộng hưởng f₀ = 1/(2π√L·C). Biết C chuẩn, đo f₀ suy ra L. "
        "Cách này đặc biệt tốt ở tần số cao. <b>LCR meter</b> tự động đo L, R, Q, D trên dải 20 Hz–2 MHz bằng "
        "cầu tự cân bằng hoặc chuyển đổi I–V phức, báo trực tiếp L ở tần số test chọn trước."))

    b.append(h2("50.3 Hệ số phẩm chất Q", "Quality Factor Q"))
    b.append(p(
        "Cuộn có Q = ωL/R_s; Q cao nghĩa là tổn hao nhỏ. Máy đo Q (Q-meter) dùng phương pháp cộng hưởng biến "
        "tần: đặt điện áp cố định vào mạch LC, đo điện áp trên tụ chuẩn V_C = Q·V_in, từ đó Q = V_C/V_in và "
        "L = 1/((2πf)²C)."))

    b.append(h2("50.4 Thông số", "Specifications"))
    b.append(table(
        ["Phương pháp", "Dải", "Tần số", "Ghi chú"],
        [["Cầu Maxwell", "mH–H", "Âm thanh", "Cân bằng tần số"],
         ["Cầu Anderson", "µH–H", "Âm thanh", "Chính xác cao"],
         ["Cộng hưởng LC", "nH–mH", "RF", "Tốt tần số cao"],
         ["LCR meter", "nH–H", "20 Hz–2 MHz", "Tự động, đa năng"],
         ["Q-meter", "µH–mH", "kHz–MHz", "Đo Q kèm"]],
        "Bảng 50.1 · Các phương pháp đo điện cảm."))

    b.append(h2("Tóm tắt", "Summary"))
    b.append(p(
        "Điện cảm L = Φ/I. Cầu Maxwell/Hay/Anderson cân bằng L_x (với R_x tổn hao) qua tụ chuẩn: L_x = R₁R₃C_s "
        "(Maxwell). Cộng hưởng LC: L = 1/((2πf)²C). LCR meter tự động đo L, R, Q. Q = ωL/R_s; Q-meter đo qua "
        "V_C = Q·V_in."))
    b.append('<div class="chapter-nav">'
             '<a href="%s"><span class="k">← Mục lục</span>Sổ tay</a>'
             '<a href="%s" style="text-align:right;"><span class="k">Mục lục →</span>Sổ tay</a></div>'
             % (C.BASE_VI, C.BASE_VI))
    return "".join(b)


def body_en():
    b = []
    b.append(p(
        "Companion to the Vietnamese translation of Chapter 50. Equations and table of the source are "
        "reproduced below; the prose is not repeated."))
    b.append(p(
        "Inductance L = Φ/I = NΦ/I (henry). Every real coil also has series resistance R_s (loss) and stray "
        "capacitance, so measurement must separate the reactive part. Bridges balance the coil (L_x in series "
        "with R_x) against a standard capacitor: the Maxwell bridge uses a parallel RC arm giving a frequency-"
        "independent balance at line frequency with L_x = R₁R₃C_s; the Hay bridge uses an RL standard arm; the "
        "Anderson bridge adds resistors to cancel stray-capacitance error and is the most accurate. Resonance "
        "methods use f₀ = 1/(2π√LC) to back out L from a known C — good at high frequency. LCR meters automate "
        "L, R, Q, D over 20 Hz–2 MHz via auto-balancing or complex I–V. The Q-meter sweeps a series-LC resonator "
        "at fixed V_in and reads V_C = Q·V_in across the standard capacitor, giving Q = V_C/V_in and L = 1/((2πf)²C); "
        "Q = ωL/R_s."))
    b.append(table(
        ["Method", "Range", "Frequency", "Note"],
        [["Maxwell", "mH–H", "Audio", "Freq.-indep."],
         ["Anderson", "µH–H", "Audio", "Most accurate"],
         ["LC resonance", "nH–mH", "RF", "Good HF"],
         ["LCR meter", "nH–H", "20 Hz–2 MHz", "Auto, versatile"],
         ["Q-meter", "µH–mH", "kHz–MHz", "Gives Q"]],
        "Table 50.1 · Inductance-measurement methods."))
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
