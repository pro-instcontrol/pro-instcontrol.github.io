# -*- coding: utf-8 -*-
"""Handbook Chapter 71 — pH Measurement (Đo pH).
Run:  python build/reader_hb_ch71.py
"""
import os
import hb_common as C
from hb_common import p, h2, h3, eq, table

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSLUG = "ch71-ph-measurement"
CH_NO = 71
TITLE_EN = "pH Measurement"
TITLE_VI = "Đo pH"
BYLINE = "John G. Webster (chủ biên) · CRC Press, 1999"
FIGS = {}


def body_vi():
    b = []
    b.append(p(
        "<b>pH</b> là số đo độ hoạt động của ion hydro: pH = −log₁₀(a_H⁺), thang 0–14 ở 25 °C (7 trung tính). "
        "pH quan trọng trong hóa học, xử lý nước, thực phẩm, dược và sinh học."))
    b.append(p(
        "Đo pH bằng <b>electrode thuỷ tinh</b> (glass electrode): màng thuỷ tinh nhạy với a_H⁺ sinh hiệu điện "
        "thế theo phương trình Nernst:"))
    b.append(eq("E = E₀ − (2,303·R·T/F)·pH = E₀ − 0,0592·pH  (V, ở 25 °C)"))
    b.append(p(
        "Do đó một đơn vị pH tương ứng ~59,2 mV ở 25 °C; hệ số này đổi theo nhiệt độ nên máy đo phải <b>bù nhiệt "
        "độ</b> (ATC). Electrode so sánh (reference, Ag/AgCl hoặc calomel) cung cấp điện thế chuẩn ổn định."))

    b.append(h2("71.1 Hiệu chuẩn", "Calibration"))
    b.append(p(
        "Hiệu chuẩn bằng dung dịch đệm chuẩn (buffer) 4,01; 7,00; 10,01 (hoặc 1,68; 12,45). Thực hiện hai/three "
        "điểm, kèm bù nhiệt độ của buffer. Độ dốc (slope) electrode giảm theo tuổi — khi slope < ~95% lý thuyết "
        "hoặc thời gian đáp ứng dài thì thay electrode. Nên hiệu chuẩn hằng ngày hoặc trước mỗi chuỗi đo."))

    b.append(h2("71.2 Các electrode và ứng dụng", "Electrodes and Applications"))
    b.append(p(
        "Electrode kết hợp (combination) gộp thuỷ tinh + so sánh trong một thân — phổ biến nhất. Electrode phẳng "
        "cho bề mặt (da, gel), micro-electrode cho mẫu nhỏ, electrode chống nhiễm bẩn (tfidf double junction) cho "
        "dung dịch chứa sulfide/protein. Ứng dụng: xử lý nước/thải, thực phẩm (sữa, thịt), dược (GMP), nuôi cấy "
        "vi sinh (bioreactor), và soil/ môi trường."))

    b.append(h2("71.3 Thông số", "Specifications"))
    b.append(table(
        ["Thông số", "Giá trị điển hình", "Ghi chú"],
        [["Dải pH", "−2 đến 16", "Tùy electrode"],
         ["Độ chính xác", "±0,01–0,05 pH", "Với hiệu chuẩn chuẩn"],
         ["Độ phân giải", "0,001 pH", "Máy đo"],
         ["Nhiệt độ", "0–100 °C", "Tùy electrode"],
         ["Thời gian đáp ứng", "vài giây", "Tùy mẫu"],
         ["Tuổi thọ electrode", "6–24 tháng", "Tùy dùng"]],
        "Bảng 71.1 · Thông số máy đo pH."))

    b.append(h2("Tóm tắt", "Summary"))
    b.append(p(
        "pH = −log₁₀(a_H⁺). Electrode thuỷ tinh cho E = E₀ − 0,0592·pH (25 °C) theo Nernst; máy phải bù nhiệt "
        "độ. Hiệu chuẩn bằng buffer 4/7/10; slope thấp là dấu hiệu electrode yếu. Ứng dụng rộng: nước, thực "
        "phẩm, dược, sinh học."))
    b.append('<div class="chapter-nav">'
             '<a href="%s"><span class="k">← Mục lục</span>Sổ tay</a>'
             '<a href="%s" style="text-align:right;"><span class="k">Mục lục →</span>Sổ tay</a></div>'
             % (C.BASE_VI, C.BASE_VI))
    return "".join(b)


def body_en():
    b = []
    b.append(p(
        "Companion to the Vietnamese translation of Chapter 71. Equations and table of the source are "
        "reproduced below; the prose is not repeated."))
    b.append(p(
        "pH = −log₁₀(a_H⁺) on a 0–14 scale at 25 °C (7 neutral). The glass electrode develops a potential across "
        "its H⁺-sensitive membrane following Nernst: E = E₀ − (2.303RT/F)·pH = E₀ − 0.0592·pH at 25 °C, so one "
        "pH unit ≈ 59.2 mV; the slope is temperature-dependent, hence automatic temperature compensation (ATC). "
        "A reference electrode (Ag/AgCl or calomel) provides the stable potential. Calibration uses standard "
        "buffers (4.01, 7.00, 10.01) at two or three points with buffer-temperature compensation; electrode slope "
        "decays with age (replace below ~95% of theoretical or when response slows); calibrate daily or before "
        "each series. Combination electrodes (glass + reference in one body) are most common; flat, micro and "
        "double-junction variants suit surfaces, small samples and dirty media. Applications: water/wastewater, "
        "food, pharma (GMP), bioreactors, soil."))
    b.append(table(
        ["Parameter", "Typical", "Note"],
        [["Range", "−2 to 16", "Electrode-dependent"],
         ["Accuracy", "±0.01–0.05 pH", "With calibration"],
         ["Resolution", "0.001 pH", "Meter"],
         ["Temperature", "0–100 °C", "Electrode-dependent"],
         ["Response time", "Seconds", "Sample-dependent"],
         ["Electrode life", "6–24 months", "Usage-dependent"]],
        "Table 71.1 · pH-meter specifications."))
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
