# -*- coding: utf-8 -*-
"""Handbook Chapter 49 — Permeability and Hysteresis Measurement (Đo độ từ thẩm và hiện tượng trễ).
Run:  python build/reader_hb_ch49.py
"""
import os
import hb_common as C
from hb_common import p, h2, h3, eq, table

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSLUG = "ch49-permeability-and-hysteresis-measurement"
CH_NO = 49
TITLE_EN = "Permeability and Hysteresis Measurement"
TITLE_VI = "Đo độ từ thẩm và hiện tượng trễ"
BYLINE = "John G. Webster (chủ biên) · CRC Press, 1999"
FIGS = {}


def body_vi():
    b = []
    b.append(p(
        "<b>Độ từ thẩm</b> (permeability) μ_r = μ/μ₀ = B/(μ₀H) mô tả khả năng từ hoá của vật liệu. Đo μ_r và "
        "vẽ đường cong <b>từ trễ</b> (B–H hysteresis loop) là then chốt để đánh giá thép điện, ferit, vật "
        "liệu lõi máy biến áp và từ ghi âm."))
    b.append(p(
        "Đường cong từ trễ cho biết từ dư B_r (remnant), lực kháng từ H_c (coercivity), độ từ thẩm ban đầu μ_i "
        "và độ từ thẩm cực đại μ_max. Diện tích vòng trễ tỉ lệ với năng lượng tiêu tán mỗi chu kỳ (tổn hao lõi)."))

    b.append(h2("49.1 Mẫu vòng (toroid) và đo B–H", "Toroidal Sample and B–H Tracing"))
    b.append(p(
        "Dùng mẫu dạng vòng (ring) bão hoà từ kín để tránh từ rò. Quấn N₁ vòng sơ cấp mang dòng I sinh H = "
        "N₁·I/l (l là chu vi vòng), và N₂ vòng thứ cấp để đo sức điện động cảm ứng e = −N₂·A·dB/dt. Tích phân "
        "e theo thời gian cho B; tích phân đồng thời H sinh đường B–H:"))
    b.append(eq("H = N₁·I / l ,   B(t) = (1/(N₂·A)) ∫ e(t) dt"))
    b.append(p(
        "Hai bộ tích phân (integrator) theo dõi B và H theo thời gian, vẽ trực tiếp vòng từ trễ trên "
        "oscilloscope hoặc thu số."))

    b.append(h2("49.2 Cầu từ (Maxwell, Anderson)", "Magnetic Bridges"))
    b.append(p(
        "Độ từ thẩm và tổn hao lõi có thể đo bằng cầu tương tự cầu điện: cuộn cảm mẫu nối với lõi từ được mô "
        "tả bằng điện cảm L_x nối tiếp điện trở tổn hao R_x. Cầu Maxwell, Hay hoặc Anderson cân bằng để lấy "
        "L_x, R_x, từ đó μ_r và hệ số tổn hao."))

    b.append(h2("49.3 Thông số", "Specifications"))
    b.append(table(
        ["Đại lượng", "Ý nghĩa", "Đo bằng"],
        [["μ_r (độ từ thẩm)", "B/(μ₀H)", "Vòng toroid + tích phân"],
         ["B_r (từ dư)", "B tại H = 0", "Vòng trễ"],
         ["H_c (lực kháng từ)", "H đảo ngược từ hoá", "Vòng trễ"],
         ["Tổn hao lõi", "Diện tích vòng × f", "Tích phân công suất"],
         ["μ_i / μ_max", "Từ thẩm ban đầu / cực đại", "Đo điểm làm việc"]],
        "Bảng 49.1 · Các đại lượng đo của vật liệu từ."))

    b.append(h2("Tóm tắt", "Summary"))
    b.append(p(
        "Độ từ thẩm μ_r = B/(μ₀H). Mẫu vòng toroid đo H = N₁I/l và B qua tích phân e = −N₂A·dB/dt, vẽ đường "
        "B–H (từ trễ) cho B_r, H_c, μ_i, μ_max. Diện tích vòng trễ = năng lượng tiêu tán/chu kỳ. Cầu Maxwell/"
        "Anderson đo L_x, R_x của cuộn có lõi để suy μ_r."))
    b.append('<div class="chapter-nav">'
             '<a href="%s"><span class="k">← Mục lục</span>Sổ tay</a>'
             '<a href="%s" style="text-align:right;"><span class="k">Mục lục →</span>Sổ tay</a></div>'
             % (C.BASE_VI, C.BASE_VI))
    return "".join(b)


def body_en():
    b = []
    b.append(p(
        "Companion to the Vietnamese translation of Chapter 49. Equations and table of the source are "
        "reproduced below; the prose is not repeated."))
    b.append(p(
        "Permeability μ_r = μ/μ₀ = B/(μ₀H). The B–H hysteresis loop reveals the remanence B_r, coercivity H_c, "
        "initial permeability μ_i and maximum permeability μ_max; the loop area is the energy dissipated per "
        "cycle (core loss). A closed toroidal sample avoids flux leakage: N₁ primary turns carry I giving "
        "H = N₁I/l (l = circumference), and an N₂ secondary senses e = −N₂A·dB/dt; integrating e yields B(t), "
        "so two integrators trace the B–H loop on a scope or digitizer. Magnetic bridges (Maxwell, Hay, "
        "Anderson) model the cored coil as L_x in series with loss R_x and balance to give L_x, R_x, hence "
        "μ_r and the loss factor. Core loss = loop area × frequency."))
    b.append(table(
        ["Quantity", "Meaning", "Measured by"],
        [["μ_r", "B/(μ₀H)", "Toroid + integrator"],
         ["B_r", "B at H=0", "Loop intercept"],
         ["H_c", "Reverse coerc. field", "Loop intercept"],
         ["Core loss", "Loop area × f", "Power integral"],
         ["μ_i / μ_max", "Init./max perm.", "Operating point"]],
        "Table 49.1 · Magnetic-material quantities."))
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
