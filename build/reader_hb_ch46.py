# -*- coding: utf-8 -*-
"""Handbook Chapter 46 — Permittivity Measurement (Đo hằng số điện môi).
Run:  python build/reader_hb_ch46.py
"""
import os
import hb_common as C
from hb_common import p, h2, h3, eq, table

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSLUG = "ch46-permittivity-measurement"
CH_NO = 46
TITLE_EN = "Permittivity Measurement"
TITLE_VI = "Đo hằng số điện môi"
BYLINE = "John G. Webster (chủ biên) · CRC Press, 1999"
FIGS = {}


def body_vi():
    b = []
    b.append(p(
        "<b>Hằng số điện môi</b> (permittivity) ε = ε₀·ε_r mô tả khả năng phân cực của vật liệu dưới điện "
        "trường; ε_r là hằng số điện môi tương đối (không thứ nguyên), ε₀ ≈ 8,854·10⁻¹² F/m. Đo ε_r cho "
        "biết tính chất vật liệu, dùng trong thiết kế tụ, radar, truyền sóng và cảm biến."))
    b.append(p(
        "Đo ε_r thường đi kèm với <b>hệ số tổn hao</b> tan δ (loss tangent) — tỉ số phần dẫn điện mất mát trên "
        "phần phản kháng: tan δ = G/(ωC). Vật liệu tốt có tan δ nhỏ (10⁻⁴–10⁻²)."))

    b.append(h2("46.1 Tụ bản song song (parallel-plate cell)", "Parallel-Plate Cell"))
    b.append(p(
        "Với tụ hai bản phẳng điện cực diện tích A, cách nhau d, chứa mẫu:"))
    b.append(eq("ε_r = C·d / (ε₀·A)"))
    b.append(p(
        "Đo C bằng cầu (Schering/Wheatstone) hoặc LCR meter ở tần số thấp–trung. Phải hiệu chỉnh điện dung "
        "rò rỉ cạnh (fringing) và độ dày chính xác. Phương pháp này dùng cho rắn, lỏng, tần số âm thanh–RF "
        "thấp."))

    b.append(h2("46.2 Cầu Schering và đo tan δ", "Schering Bridge and tan δ"))
    b.append(p(
        "Cầu Schering cân bằng để lấy C_x và G_x của mẫu, từ đó ε_r và tan δ. Nó đặc biệt quan trọng trong "
        "kiểm tra cách điện (transformer oil, cáp) vì tan δ nhạy với sự lão hoá, ẩm và tạp chất."))

    b.append(h2("46.3 Tần số cao: cộng hưởng và không gian tự do", "High-Frequency: Resonant and Free-Space"))
    b.append(p(
        "Ở RF/vi ba, dùng <b>cộng hưởng khe hốc</b> (re-entrant cavity) hoặc <b>hốc cộng hưởng</b> (resonant "
        "cavity): đặt mẫu vào hốc, dịch tần số cộng hưởng f và hệ số phẩm chất Q để suy ε_r, tan δ. Độ chính "
        "xác cao nhưng chỉ đo được mẫu nhỏ. Ở tần số vi ba trở lên, phương pháp <b>không gian tự do</b> "
        "(free-space) chiếu sóng qua mẫu và đo hệ số truyền/suy hao và dịch pha để tính ε_r."))

    b.append(h2("46.4 Thông số", "Specifications"))
    b.append(table(
        ["Phương pháp", "Tần số", "Loại mẫu", "Đo tan δ"],
        [["Tụ bản song song", "DC–MHz", "Rắn, lỏng", "Có (qua LCR)"],
         ["Cầu Schering", "50 Hz–kHz", "Cách điện", "Có, nhạy"],
         ["Hốc cộng hưởng", "MHz–GHz", "Mẫu nhỏ", "Có (từ Q)"],
         ["Không gian tự do", "GHz", "Tấm, lớp", "Có"],
         ["Cầu coaxial", "kHz–MHz", "Lỏng, bột", "Có"]],
        "Bảng 46.1 · Các phương pháp đo ε_r."))

    b.append(h2("Tóm tắt", "Summary"))
    b.append(p(
        "Hằng số điện môi ε_r = C·d/(ε₀·A) với tụ bản song song; đo C bằng cầu/LCR. Cầu Schering cho cả tanδ "
        "= G/(ωC), nhạy với lão hoá cách điện. Tần số cao dùng hốc cộng hưởng (dịch f, Q) hoặc chiếu không "
        "gian tự do qua mẫu. ε_r và tanδ là đặc trưng then chốt của vật liệu điện môi."))
    b.append('<div class="chapter-nav">'
             '<a href="%s"><span class="k">← Mục lục</span>Sổ tay</a>'
             '<a href="%s" style="text-align:right;"><span class="k">Mục lục →</span>Sổ tay</a></div>'
             % (C.BASE_VI, C.BASE_VI))
    return "".join(b)


def body_en():
    b = []
    b.append(p(
        "Companion to the Vietnamese translation of Chapter 46. Equations and table of the source are "
        "reproduced below; the prose is not repeated."))
    b.append(p(
        "Permittivity ε = ε₀ε_r (ε₀ ≈ 8.854×10⁻¹² F/m); ε_r is the relative permittivity. Measurement is "
        "usually paired with the loss tangent tanδ = G/(ωC), a sensitivity indicator for ageing, moisture "
        "and contamination in dielectrics. A parallel-plate cell gives ε_r = C·d/(ε₀·A), measured by bridge "
        "or LCR meter at low-to-mid frequency (corrections for fringing and thickness needed). The Schering "
        "bridge yields C_x and G_x simultaneously, hence ε_r and tanδ — central to insulation testing "
        "(transformer oil, cables). At RF/microwave, a re-entrant or resonant cavity holding the sample "
        "shifts the resonance frequency f and quality factor Q, from which ε_r and tanδ are derived; free-space "
        "methods transmit a wave through the sample and infer ε_r from attenuation and phase shift."))
    b.append(table(
        ["Method", "Frequency", "Sample", "tanδ"],
        [["Parallel-plate", "DC–MHz", "Solid, liquid", "Yes (LCR)"],
         ["Schering", "50 Hz–kHz", "Insulation", "Yes, sensitive"],
         ["Cavity", "MHz–GHz", "Small", "Yes (from Q)"],
         ["Free-space", "GHz", "Slab/layer", "Yes"],
         ["Coaxial", "kHz–MHz", "Liquid, powder", "Yes"]],
        "Table 46.1 · Permittivity-measurement methods."))
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
