# -*- coding: utf-8 -*-
"""Handbook Chapter 59 — Optical Loss (Tổn hao quang).
Run:  python build/reader_hb_ch59.py
"""
import os
import hb_common as C
from hb_common import p, h2, h3, eq, table

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSLUG = "ch59-optical-loss"
CH_NO = 59
TITLE_EN = "Optical Loss"
TITLE_VI = "Tổn hao quang"
BYLINE = "John G. Webster (chủ biên) · CRC Press, 1999"
FIGS = {}


def body_vi():
    b = []
    b.append(p(
        "<b>Tổn hao quang</b> (optical loss) là phần công suất quang mất đi khi truyền qua một phần tử hoặc "
        "một đoạn sợi, biểu thị theo decibel:"))
    b.append(eq("Loss (dB) = −10·log₁₀(P_out / P_in)"))
    b.append(p(
        "Trong sợi quang, hệ số suy hao α (dB/km) đặc trưng tổn hao trên mỗi km. Các nguồn tổn hao: hấp thụ "
        "(OH⁻, vi tạp), tán xạ Rayleigh, tán xạ phi tuyến, và tổn hao do uốn (bend loss). Giới hạn lý thuyết "
        "của silica ~0,2 dB/km ở 1550 nm."))

    b.append(h2("59.1 Phương pháp cut-back", "Cut-Back Method"))
    b.append(p(
        "Đo công suất ra P_out của sợi chiều dài L, sau đó cắt ngắn một đoạn (một phần) và đo lại P₂. Suy hao "
        "α = (10/(L−L₂))·log₁₀(P₂/P_out) — chính xác, dùng làm chuẩn phòng thí nghiệm."))

    b.append(h2("59.2 OTDR (đo từ xa)", "Optical Time-Domain Reflectometry (OTDR)"))
    b.append(p(
        "Bơm xung ánh sáng vào sợi và đo ánh sáng tán xạ ngược (backscatter) quay lại theo thời gian. Từ delay "
        "t suy ra vị trí z = c·t/(2n). Đồ thị này cho biết suy hao theo km, vị trí và độ lớn của nối hàn, đầu "
        "nối, và điểm gãy. Đây là công cụ bảo trì mạng sợi chủ đạo."))

    b.append(h2("59.3 Tổn hao nối và hệ số phản xạ", "Connector/Splice Loss and Return Loss"))
    b.append(p(
        "Tổn hao đầu nối (connector loss) do lệch tâm, khe hở, góc mạt, và khác biệt giữa hai sợi; điển hình "
        "0,1–0,5 dB mỗi nối. <b>Return loss</b> đo công suất phản xạ ngược: RL = −10log₁₀(P_ref/P_in), giá trị "
        "cao (50–60 dB) là tốt. <b>Insertion loss</b> đo tổn hao chèn của một phần tử (bộ lọc, khuếch đại quang) "
        "trong hệ."))

    b.append(h2("59.4 Thông số", "Specifications"))
    b.append(table(
        ["Phép đo", "Phương pháp", "Độ chính xác", "Ứng dụng"],
        [["Suy hao sợi (dB/km)", "Cut-back, OTDR", "±0,01 dB/km", "Cáp quang"],
         ["Tổn hao đầu nối", "Power meter", "±0,02 dB", "Mạng sợi"],
         ["Return loss", "Coupler, OTDR", "±0,5 dB", "Chất lượng nối"],
         ["Vị trí lỗi", "OTDR", "±(0,5–2) m", "Bảo trì, sửa chữa"],
         ["Suy hao phần tử", "Insertion loss", "±0,05 dB", "Bộ lọc, WDM"]],
        "Bảng 59.1 · Các phép đo tổn hao quang."))

    b.append(h2("Tóm tắt", "Summary"))
    b.append(p(
        "Tổn hao quang Loss = −10log₁₀(P_out/P_in); suy hao sợi α (dB/km) từ hấp thụ, tán xạ Rayleigh, uốn. "
        "Cut-back đo chuẩn phòng thí nghiệm; OTDR dùng backscatter để đo suy hao theo km và vị trí lỗi. Tổn hao "
        "nối 0,1–0,5 dB; return loss cao là tốt; insertion loss đo phần tử chèn."))
    b.append('<div class="chapter-nav">'
             '<a href="%s"><span class="k">← Mục lục</span>Sổ tay</a>'
             '<a href="%s" style="text-align:right;"><span class="k">Mục lục →</span>Sổ tay</a></div>'
             % (C.BASE_VI, C.BASE_VI))
    return "".join(b)


def body_en():
    b = []
    b.append(p(
        "Companion to the Vietnamese translation of Chapter 59. Equations and table of the source are "
        "reproduced below; the prose is not repeated."))
    b.append(p(
        "Optical loss Loss (dB) = −10·log₁₀(P_out/P_in); fiber attenuation α (dB/km) comes from absorption "
        "(OH⁻, impurities), Rayleigh scattering, nonlinearity and bend loss (silica floor ≈0.2 dB/km at "
        "1550 nm). The cut-back method measures P_out over length L, trims the fiber and measures again to get "
        "α = (10/(L−L₂))·log₁₀(P₂/P_out) — the laboratory reference. An OTDR injects a pulse and measures "
        "backscatter vs time, locating features at z = c·t/(2n): attenuation profile, splices, connectors and "
        "breaks — the field-maintenance tool. Connector loss (0.1–0.5 dB) arises from offset, gap and end-face "
        "angle; return loss RL = −10log₁₀(P_ref/P_in) (50–60 dB is good); insertion loss characterizes inserted "
        "elements such as filters and WDM devices."))
    b.append(table(
        ["Measurement", "Method", "Accuracy", "Use"],
        [["Fiber α (dB/km)", "Cut-back, OTDR", "±0.01 dB/km", "Cable"],
         ["Connector loss", "Power meter", "±0.02 dB", "Fiber networks"],
         ["Return loss", "Coupler, OTDR", "±0.5 dB", "Joint quality"],
         ["Fault location", "OTDR", "±(0.5–2) m", "Repair"],
         ["Element loss", "Insertion", "±0.05 dB", "Filters, WDM"]],
        "Table 59.1 · Optical-loss measurements."))
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
