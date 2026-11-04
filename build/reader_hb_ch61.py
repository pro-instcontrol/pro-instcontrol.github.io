# -*- coding: utf-8 -*-
"""Handbook Chapter 61 — Refractive Index Measurement (Đo chiết suất).
Run:  python build/reader_hb_ch61.py
"""
import os
import hb_common as C
from hb_common import p, h2, h3, eq, table

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSLUG = "ch61-refractive-index-measurement"
CH_NO = 61
TITLE_EN = "Refractive Index Measurement"
TITLE_VI = "Đo chiết suất"
BYLINE = "John G. Webster (chủ biên) · CRC Press, 1999"
FIGS = {}


def body_vi():
    b = []
    b.append(p(
        "Chiết suất n = c/v (tốc độ ánh sáng trong chân không / trong môi trường) quyết định khúc xạ, phản xạ "
        "toàn phần và băng thông của quang học. n phụ thuộc bước sóng (tán sắc) và nhiệt độ, nên khi báo giá "
        "phải ghi rõ n_D (đường D natri 589 nm) và nhiệt độ."))
    b.append(p(
        "Đo chiết suất dùng để xác định nồng độ dung dịch (đường — thang Brix, muối, acid), nhận biết đá quý, "
        "kiểm tra màng mỏng và vật liệu quang."))

    b.append(h2("61.1 Khúc xạ kế góc giới hạn (Abbe)", "Critical-Angle (Abbe) Refractometer"))
    b.append(p(
        "Một giọt mẫu đặt trên lăng kính có n cao hơn; ánh sáng chiếu qua mẫu và đo góc giới hạn phản xạ toàn "
        "phần θ_c = arcsin(n_sample/n_prism). Đọc θ_c qua ống ngắm hoặc đầu dò, suy ra n. Khúc xạ kế Abbe cho "
        "n đến 4 chữ số thập phân; kiểu cầm tay đọc trực tiếp qua thang Brix."))

    b.append(h2("61.2 Lăng kính lệch nhỏ nhất", "Minimum-Deviation Prism"))
    b.append(p(
        "Một mẫu dạng lăng kính với góc đỉnh A: đo góc lệch nhỏ nhất δ_min của tia sáng cho"))
    b.append(eq("n = sin((A + δ_min)/2) / sin(A/2)"))
    b.append(p(
        "Đây là phương pháp chuẩn có độ chính xác cao nhất (10⁻⁵–10⁻⁶), dùng hiệu chuẩn khúc xạ kế và đo "
        "vật liệu quang."))

    b.append(h2("61.3 Ellipsometry cho màng mỏng", "Ellipsometry for Thin Films"))
    b.append(p(
        "Chiếu ánh sáng phân cực dưới góc nghiêng và đo sự thay đổi biên độ/phân cực (Ψ, Δ). Từ đó suy ra n, "
        "hệ số hấp thụ k và độ dày lớp màng. Đây là phương pháp chính cho màng mỏng semiconductor và lớp phủ "
        "quang, chính xác tới Å."))

    b.append(h2("61.4 Thông số", "Specifications"))
    b.append(table(
        ["Phương pháp", "Dải n", "Độ chính xác", "Ứng dụng"],
        [["Abbe (góc giới hạn)", "1,30–1,70", "±0,0002", "Dung dịch, dầu"],
         ["Cầm tay (Brix)", "1,33–1,53", "±0,001", "Đường, thực phẩm"],
         ["Lăng kính δ_min", "1,2–2,0", "±0,00001", "Chuẩn, quang học"],
         ["Ellipsometer", "1,0–4,0", "±0,005", "Màng mỏng"],
         ["Interferometer", "1,0–2,0", "±0,00001", "Khí, chất lỏng"]],
        "Bảng 61.1 · Các phương pháp đo chiết suất."))

    b.append(h2("Tóm tắt", "Summary"))
    b.append(p(
        "Chiết suất n = c/v, phụ thuộc bước sóng/nhiệt độ (n_D). Khúc xạ kế Abbe đo góc giới hạn θ_c = "
        "arcsin(n/n_prism) cho dung dịch; kiểu cầm tay đọc Brix. Lăng kính δ_min: n = sin((A+δ_min)/2)/sin(A/2) "
        "— chuẩn, chính xác nhất. Ellipsometry đo Ψ, Δ để suy n, k, độ dày màng mỏng."))
    b.append('<div class="chapter-nav">'
             '<a href="%s"><span class="k">← Mục lục</span>Sổ tay</a>'
             '<a href="%s" style="text-align:right;"><span class="k">Mục lục →</span>Sổ tay</a></div>'
             % (C.BASE_VI, C.BASE_VI))
    return "".join(b)


def body_en():
    b = []
    b.append(p(
        "Companion to the Vietnamese translation of Chapter 61. Equations and table of the source are "
        "reproduced below; the prose is not repeated."))
    b.append(p(
        "Refractive index n = c/v governs refraction, total internal reflection and optical bandwidth; it varies "
        "with wavelength (dispersion) and temperature, hence values are quoted at n_D (589 nm). The critical-angle "
        "(Abbe) refractometer places a sample drop on a higher-index prism and reads θ_c = arcsin(n_sample/n_prism) "
        "through an eyepiece or sensor — four decimal places; handheld versions read Brix for sugar. The "
        "minimum-deviation prism method gives n = sin((A+δ_min)/2)/sin(A/2) with the highest accuracy (10⁻⁵–10⁻⁶) "
        "for calibration and optical materials. Ellipsometry measures polarization changes (Ψ, Δ) at oblique "
        "incidence to derive n, absorption k and film thickness (Å-level) — the thin-film standard for "
        "semiconductors and optical coatings."))
    b.append(table(
        ["Method", "n range", "Accuracy", "Use"],
        [["Abbe (crit. angle)", "1.30–1.70", "±0.0002", "Liquids, oils"],
         ["Handheld (Brix)", "1.33–1.53", "±0.001", "Sugar, food"],
         ["Prism δ_min", "1.2–2.0", "±0.00001", "Reference, optics"],
         ["Ellipsometer", "1.0–4.0", "±0.005", "Thin films"],
         ["Interferometer", "1.0–2.0", "±0.00001", "Gas, liquid"]],
        "Table 61.1 · Refractive-index methods."))
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
