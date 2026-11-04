# -*- coding: utf-8 -*-
"""Handbook Chapter 57 — Densitometry Measurement (Đo mật độ quang).
Run:  python build/reader_hb_ch57.py
"""
import os
import hb_common as C
from hb_common import p, h2, h3, eq, table

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSLUG = "ch57-densitometry-measurement"
CH_NO = 57
TITLE_EN = "Densitometry Measurement"
TITLE_VI = "Đo mật độ quang"
BYLINE = "John G. Webster (chủ biên) · CRC Press, 1999"
FIGS = {}


def body_vi():
    b = []
    b.append(p(
        "<b>Mật độ quang</b> (optical density, OD) là độ mờ của mẫu, định nghĩa OD = log₁₀(I₀/I) với I₀ là "
        "cường độ vào và I là cường độ truyền qua (hoặc phản xạ). OD = 1 nghĩa là chỉ truyền 10%; OD = 2 truyền "
        "1%. Mật độ quang tỉ lệ với nồng độ (định luật Beer–Lambert): A = ε·l·c."))
    b.append(p(
        "<b>Phép đo mật độ quang</b> (densitometry) dùng để đo độ mờ của phim X-quang, mực in, lớp phủ, dung "
        "dịch, và trong y khoa (đo mật độ xương bằng DXA)."))

    b.append(h2("57.1 Densitometer truyền qua và phản xạ", "Transmission and Reflection Densitometers"))
    b.append(p(
        "<b>Densitometer truyền qua</b> chiếu sáng một vùng nhỏ của mẫu (phim) và đo ánh sáng truyền qua bằng "
        "photodiode, so với mẫu trắng chuẩn, hiển thị OD. Dùng cho phim X-quang (0–4 OD), phim chụp ảnh, kính "
        "mặt trời. <b>Densitometer phản xạ</b> đo ánh sáng phản xạ từ bề mặt (giấy in, mẫu tráng), dùng trong "
        "in ấn (mật độ mực)."))
    b.append(p(
        "Đầu dò có vùng lỗ (aperture) 1–3 mm, nguồn sáng ổn định, và bộ lọc phổ (trắng, UV, cyan/magenta/yellow) "
        "tùy ứng dụng in."))

    b.append(h2("57.2 Ứng dụng y sinh và công nghiệp", "Medical and Industrial Applications"))
    b.append(p(
        "Trong y khoa, <b>DXA</b> (dual-energy X-ray absorptiometry) đo mật độ xương bằng hai năng lượng tia X, "
        "quy đổi thành g/cm². Trong hóa học, <b>spectrophotometer</b> đo mật độ quang của dung dịch theo bước "
        "sóng để định lượng (A = εlc). Trong in ấn và chụp ảnh, mật độ mực phải nằm trong khoảng chuẩn để bảo "
        "đảm màu sắc nhất quán."))

    b.append(h2("57.3 Thông số", "Specifications"))
    b.append(table(
        ["Loại", "Dải OD", "Độ chính xác", "Ứng dụng"],
        [["Truyền qua (phim)", "0–4", "±0,02 OD", "X-quang, ảnh"],
         ["Phản xạ (in ấn)", "0–2,5", "±0,02 OD", "Mực in"],
         ["Spectrophotometer", "0–3", "±0,005 OD", "Dung dịch, hóa"],
         ["DXA (xương)", "0–3 g/cm²", "1%–2%", "Loãng xương"]],
        "Bảng 57.1 · Các thiết bị đo mật độ quang."))

    b.append(h2("Tóm tắt", "Summary"))
    b.append(p(
        "Mật độ quang OD = log₁₀(I₀/I), tỉ lệ nồng độ theo Beer–Lambert. Densitometer truyền qua đo phim "
        "(X-quang 0–4 OD), phản xạ đo mực in. Spectrophotometer đo OD dung dịch theo bước sóng; DXA dùng hai "
        "năng lượng tia X để đo mật độ xương. Độ chính xác ±0,02 OD điển hình."))
    b.append('<div class="chapter-nav">'
             '<a href="%s"><span class="k">← Mục lục</span>Sổ tay</a>'
             '<a href="%s" style="text-align:right;"><span class="k">Mục lục →</span>Sổ tay</a></div>'
             % (C.BASE_VI, C.BASE_VI))
    return "".join(b)


def body_en():
    b = []
    b.append(p(
        "Companion to the Vietnamese translation of Chapter 57. Equations and table of the source are "
        "reproduced below; the prose is not repeated."))
    b.append(p(
        "Optical density OD = log₁₀(I₀/I) with I₀ the incident and I the transmitted (or reflected) intensity. "
        "OD 1 = 10% transmission, OD 2 = 1%. Density is proportional to concentration via Beer–Lambert "
        "(A = ε·l·c). Transmission densitometers illuminate a small aperture (1–3 mm) of film (X-ray 0–4 OD) and "
        "read with a photodiode against a white standard; reflection densitometers measure ink density on print. "
        "Spectral filters (visual, UV, CMY) suit print applications. Medical: DXA (dual-energy X-ray "
        "absorptiometry) uses two X-ray energies to report bone mineral density in g/cm² (1%–2%). Chemistry: a "
        "spectrophotometer measures solution OD per wavelength for quantitation (±0.005 OD)."))
    b.append(table(
        ["Type", "OD range", "Accuracy", "Use"],
        [["Transmission (film)", "0–4", "±0.02 OD", "X-ray, photo"],
         ["Reflection (print)", "0–2.5", "±0.02 OD", "Ink density"],
         ["Spectrophotometer", "0–3", "±0.005 OD", "Solutions"],
         ["DXA (bone)", "0–3 g/cm²", "1%–2%", "Osteoporosis"]],
        "Table 57.1 · Densitometry instruments."))
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
