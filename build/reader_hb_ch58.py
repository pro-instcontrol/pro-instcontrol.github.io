# -*- coding: utf-8 -*-
"""Handbook Chapter 58 — Colorimetry (Đo màu).
Run:  python build/reader_hb_ch58.py
"""
import os
import hb_common as C
from hb_common import p, h2, h3, eq, table

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSLUG = "ch58-colorimetry"
CH_NO = 58
TITLE_EN = "Colorimetry"
TITLE_VI = "Đo màu"
BYLINE = "John G. Webster (chủ biên) · CRC Press, 1999"
FIGS = {}


def body_vi():
    b = []
    b.append(p(
        "Màu sắc được mô tả bằng ba giá trị kích thích (tristimulus) X, Y, Z trong hệ CIE 1931: X, Y, Z là tích "
        "phân phổ của nguồn sáng × vật thể × các hàm khớp màu chuẩn x̄(λ), ȳ(λ), z̄(λ). Tọa độ sắc độ: "
        "x = X/(X+Y+Z), y = Y/(X+Y+Z)."))
    b.append(p(
        "Hệ <b>CIE L*a*b*</b> dễ đánh giá hơn: L* độ sáng, a* xanh lá–đỏ, b* xanh dương–vàng. Sai số màu:"))
    b.append(eq("ΔE*ab = √((ΔL*)² + (Δa*)² + (Δb*)²)"))
    b.append(p(
        "ΔE*ab < 1: mắt khó nhận ra; 1–3: nhận ra nhưng chấp nhận được; > 3: rõ ràng."))

    b.append(h2("58.1 Colorimeter và spectrophotometer", "Colorimeters and Spectrophotometers"))
    b.append(p(
        "<b>Colorimeter</b> dùng ba bộ lọc x̄, ȳ, z̄ để đo trực tiếp X, Y, Z; rẻ, nhanh, dùng kiểm tra sản phẩm "
        "in, sơn, thực phẩm. <b>Spectrophotometer</b> đo toàn phổ phản xạ/truyền (400–700 nm, bước 5–10 nm) rồi "
        "tính tích phân ra tristimulus — chính xác hơn, cho phép chuyển đổi bất kỳ hệ màu nào, dùng làm chuẩn "
        "chất lượng và đo màu phát sáng (màn hình, đèn)."))

    b.append(h2("58.2 Ứng dụng", "Applications"))
    b.append(p(
        "Kiểm soát màu in ấn (ΔE so với mẫu chuẩn), màu sơn/nhựa, thực phẩm và nông sản (màu thịt, trái cây), "
        "màu màn hình (đo gam màu, ΔE màn hình), màu nước/thực phẩm, và trong hóa học (định lượng qua màu)."))

    b.append(h2("58.3 Thông số", "Specifications"))
    b.append(table(
        ["Thiết bị", "Hệ màu", "ΔE*ab", "Ứng dụng"],
        [["Colorimeter cầm tay", "L*a*b*, ΔE", "±0,1", "In, sơn, thực phẩm"],
         ["Spectrophotometer", "Mọi hệ", "±0,02", "Chuẩn, pha màu"],
         ["Display colorimeter", "XYZ, ΔE", "±0,002 (màn)", "Màn hình"],
         ["Sphere/45°-0°", "Đa hình học", "±0,05", "Vật liệu"]],
        "Bảng 58.1 · Thiết bị đo màu."))

    b.append(h2("Tóm tắt", "Summary"))
    b.append(p(
        "Màu được đo bằng tristimulus XYZ (CIE 1931) và L*a*b*; ΔE*ab định lượng sai số màu. Colorimeter dùng "
        "bộ lọc ba kênh, nhanh và rẻ; spectrophotometer đo phổ và tích phân, chính xác (±0,02 ΔE), đa hệ màu. "
        "Ứng dụng: in, sơn, thực phẩm, màn hình, hóa học."))
    b.append('<div class="chapter-nav">'
             '<a href="%s"><span class="k">← Mục lục</span>Sổ tay</a>'
             '<a href="%s" style="text-align:right;"><span class="k">Mục lục →</span>Sổ tay</a></div>'
             % (C.BASE_VI, C.BASE_VI))
    return "".join(b)


def body_en():
    b = []
    b.append(p(
        "Companion to the Vietnamese translation of Chapter 58. Equations and table of the source are "
        "reproduced below; the prose is not repeated."))
    b.append(p(
        "Color is specified by CIE 1931 tristimulus values X, Y, Z — integrals of source × object × standard "
        "matching functions x̄, ȳ, z̄ — with chromaticity coordinates x = X/(X+Y+Z), y = Y/(X+Y+Z). The CIE "
        "L*a*b* space (L* lightness, a* green–red, b* blue–yellow) is more perceptual; color difference is "
        "ΔE*ab = √((ΔL*)²+(Δa*)²+(Δb*)²): <1 imperceptible, 1–3 perceptible but acceptable, >3 obvious. A "
        "colorimeter uses three x̄,ȳ,z̄ filters for direct XYZ — fast and cheap for print, paint, food QC. A "
        "spectrophotometer measures the full reflectance/transmittance spectrum (400–700 nm, 5–10 nm steps) and "
        "integrates to tristimulus — more accurate, any color space, also used for emissive displays and lamps. "
        "Applications: print ΔE vs standard, paint/plastics, food color, display gamut/ΔE, water, and "
        "quantitative colorimetric chemistry."))
    b.append(table(
        ["Instrument", "Color space", "ΔE*ab", "Use"],
        [["Handheld colorimeter", "L*a*b*, ΔE", "±0.1", "Print, paint, food"],
         ["Spectrophotometer", "All", "±0.02", "Reference, matching"],
         ["Display colorimeter", "XYZ, ΔE", "±0.002 (disp.)", "Displays"],
         ["Sphere / 45°-0°", "Multi-geom.", "±0.05", "Materials"]],
        "Table 58.1 · Color-measurement instruments."))
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
