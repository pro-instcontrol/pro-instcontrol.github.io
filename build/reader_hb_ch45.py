# -*- coding: utf-8 -*-
"""Handbook Chapter 45 — Capacitance and Capacitance Measurements (Điện dung và phép đo điện dung).
Run:  python build/reader_hb_ch45.py
"""
import os
import hb_common as C
from hb_common import p, h2, h3, eq, table

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSLUG = "ch45-capacitance-and-capacitance-measurements"
CH_NO = 45
TITLE_EN = "Capacitance and Capacitance Measurements"
TITLE_VI = "Điện dung và phép đo điện dung"
BYLINE = "John G. Webster (chủ biên) · CRC Press, 1999"
FIGS = {}


def body_vi():
    b = []
    b.append(p(
        "Điện dung (capacitance) C = Q/V, đơn vị farad (F). Với tụ phẳng, C = ε·A/d = ε₀·ε_r·A/d. Đo điện "
        "dung được dùng để xác định hằng số điện môi, độ ẩm, vị trí, áp suất (cảm biến điện dung) và kiểm "
        "tra linh kiện."))
    b.append(p(
        "Điện dung điển hình rất nhỏ (pF–µF), nên đo chính xác đòi hỏi triệt tiêu điện dung rò rỉ (stray) "
        "và trở rò, dùng tín hiệu AC tần số cao và điểm zero (null) hoặc chuyển đổi thành đại lượng dễ đo."))

    b.append(h2("45.1 Cầu Wheatstone và Schering", "Bridge Methods"))
    b.append(p(
        "Cầu Wheatstone cân bằng (dùng trở/thành phần phản kháng) đo được C bằng cách so sánh với tụ chuẩn "
        "C_ref. <b>Cầu Schering</b> chuyên đo điện dung và tổn hao điện môi: gồm C_x (mẫu) nối tiếp điện dẫn "
        "G_x (tổn hao), tụ chuẩn C_s và hai trở, cân bằng ở tần số điện lưới. Nó cho trực tiếp C_x và hệ số "
        "tổn hao tan δ."))

    b.append(h2("45.2 Chuyển đổi điện dung", "Capacitance-to-... Conversion"))
    b.append(p(
        "Cách thực tế phổ biến là đưa tụ vào mạch dao động: tần số f = 1/(2π√LC) hoặc hằng số thời gian RC "
        "tỉ lệ với C, rồi đo f hoặc độ rộng xung để suy ra C. Hoặc dùng bộ chuyển đổi C→điện áp (charge "
        "balancing): nạp/xả tụ mẫu ở tần số f cố định, dòng trung bình I = C·V·f ∝ C, đo I qua bộ I–V."))
    b.append(eq("I_avg = C·V·f   ⇒   C = I_avg / (V·f)"))

    b.append(h2("45.3 Sai số và điện dung rò", "Stray Capacitance and Errors"))
    b.append(p(
        "Điện dung rò (stray capacitance) giữa dây dẫn và vỏ, cùng trở cách điện song song, gây sai số. Kỹ "
        "thuật che chắn (guarding) — đặt vòng guard nối potential trung tính bao quanh cực đo — triệt dòng "
        "rò qua trở cách điện, chỉ để lại thành phần C cần đo. Đo trong môi trường được kiểm soát nhiệt độ."))

    b.append(h2("45.4 Thông số", "Specifications"))
    b.append(table(
        ["Phương pháp", "Dải", "Tần số", "Ưu điểm"],
        [["Cầu Wheatstone", "pF–µF", "DC–kHz", "Đơn giản, chính xác"],
         ["Cầu Schering", "pF–µF", "50/60 Hz", "Đo tan δ kèm"],
         ["C→tần số (VCO)", "fF–µF", "kHz–MHz", "Số hoá dễ"],
         ["C→điện áp", "pF–nF", "kHz", "IC tích hợp"],
         ["LCR meter", "mΩ–GΩ, pF–F", "20 Hz–2 MHz", "Đa năng, tự động"]],
        "Bảng 45.1 · Các phương pháp đo điện dung."))

    b.append(h2("Tóm tắt", "Summary"))
    b.append(p(
        "Điện dung C = Q/V = εA/d. Đo bằng cầu Wheatstone/Schering (cân bằng với tụ chuẩn, Schering thêm đo "
        "tanδ) hoặc chuyển đổi C→tần số/C→dòng (I_avg = C·V·f). Che chắn guard triệt điện dung rò và trở rò. "
        "LCR meter tự động đo C, R, L trên dải rộng."))
    b.append('<div class="chapter-nav">'
             '<a href="%s"><span class="k">← Mục lục</span>Sổ tay</a>'
             '<a href="%s" style="text-align:right;"><span class="k">Mục lục →</span>Sổ tay</a></div>'
             % (C.BASE_VI, C.BASE_VI))
    return "".join(b)


def body_en():
    b = []
    b.append(p(
        "Companion to the Vietnamese translation of Chapter 45. Equations and table of the source are "
        "reproduced below; the prose is not repeated."))
    b.append(p(
        "Capacitance C = Q/V (farad); for a parallel plate C = ε₀ε_r A/d. Capacitance (pF–µF) is measured "
        "to derive permittivity, humidity, position and pressure (capacitive sensors) and to test components. "
        "A Wheatstone bridge compares C_x with a standard C_ref; the Schering bridge is specialised for "
        "capacitance and dielectric loss — it yields C_x and the loss tangent tanδ directly. Practical meters "
        "embed C in an oscillator (f = 1/2π√LC) or an RC timer, or use charge-balancing: charging C at a "
        "fixed frequency f gives I_avg = C·V·f, so C = I_avg/(V·f). Stray capacitance and leakage resistance "
        "are suppressed by guarding — a driven guard ring at neutral potential shunts leakage current away. "
        "LCR meters automate C/R/L measurement from mΩ–GΩ and pF–F over 20 Hz–2 MHz."))
    b.append(table(
        ["Method", "Range", "Frequency", "Advantage"],
        [["Wheatstone", "pF–µF", "DC–kHz", "Simple, accurate"],
         ["Schering", "pF–µF", "50/60 Hz", "Gives tanδ"],
         ["C→freq (VCO)", "fF–µF", "kHz–MHz", "Easy digitizing"],
         ["C→voltage", "pF–nF", "kHz", "IC integrated"],
         ["LCR meter", "mΩ–GΩ, pF–F", "20 Hz–2 MHz", "Versatile, auto"]],
        "Table 45.1 · Capacitance-measurement methods."))
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
