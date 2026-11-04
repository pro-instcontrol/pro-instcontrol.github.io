# -*- coding: utf-8 -*-
"""Handbook Chapter 66 — Radioactivity Measurement, part 2 (Đo phóng xạ, phần 2).
Run:  python build/reader_hb_ch66.py
"""
import os
import hb_common as C
from hb_common import p, h2, h3, eq, table

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSLUG = "ch66-radioactivity-measurement-part-2"
CH_NO = 66
TITLE_EN = "Radioactivity Measurement (part 2)"
TITLE_VI = "Đo phóng xạ (phần 2)"
BYLINE = "John G. Webster (chủ biên) · CRC Press, 1999"
FIGS = {}


def body_vi():
    b = []
    b.append(p(
        "Phần này tập trung vào <b>phổ gamma</b> (gamma spectrometry) và các khía cạnh thực hành của đo phóng "
        "xạ: hiệu chuẩn, nền (background), thống kê đếm và che chắn. Phổ gamma đo bằng HPGe hoặc NaI(Tl) cho "
        "phép định lượng từng đồng vị vì mỗi đồng vị có các vạch năng lượng đặc trưng (ví dụ Cs-137: 662 keV; "
        "Co-60: 1173 và 1332 keV)."))

    b.append(h2("66.1 Hiệu chuẩn năng lượng và hiệu suất", "Energy and Efficiency Calibration"))
    b.append(p(
        "Hiệu chuẩn năng lượng dùng các nguồn chuẩn (Am-241, Cs-137, Co-60, Eu-152) để gán kênh (channel) thành "
        "năng lượng. <b>Hiệu suất</b> (efficiency) tại mỗi năng lượng đo bằng nguồn chuẩn hoạt độ đã biết: "
        "ε(E) = N_counts/(A·t·I_γ). Từ đó tính hoạt độ mẫu:"))
    b.append(eq("A = N_counts / (t · ε(E) · I_γ)"))
    b.append(p(
        "với I_γ là xác suất phát xạ của vạch. Hiệu suất phụ thuộc hình học mẫu (khoảng cách, mật độ, bình chứa) "
        "nên chuẩn mẫu phải cùng hình học."))

    b.append(h2("66.2 Nền và che chắn", "Background and Shielding"))
    b.append(p(
        "Nền tự nhiên (cosmic, K-40, U/Th trong đất, tia X máy) là giới hạn chính của độ nhạy. Che chắn bằng chì "
        "10–15 cm (có lớp đồng/thép trong để hấp thụ X-đặc trưng của chì), và dùng <b>hệ thống chống trùng phùng</b> "
        "(anticoincidence) hoặc detector Shield (guard) để triệt nhiễu vũ trụ. Đo nền riêng và trừ đi."))

    b.append(h2("66.3 Thống kê đếm", "Counting Statistics"))
    b.append(p(
        "Phân rã là quá trình Poisson: nếu đếm N, sai số chuẩn là σ = √N. Sai số tương đối = 1/√N, nên để giảm "
        "sai số 10 lần phải đếm gấp 100 lần thời gian. Kết quả báo kèm độ tin cậy (±1σ, ±2σ)."))
    b.append(eq("N = A·t·ε(E)·I_γ ,   σ_A/A ≈ 1/√N"))

    b.append(h2("66.4 Thông số", "Specifications"))
    b.append(table(
        ["Đại lượng", "Định nghĩa", "Điển hình"],
        [["Hiệu suất ε(E)", "Counts / (A·t·Iγ)", "HPGe ~1%–30%, NaI ~10%–40%"],
         ["Phân giải FWHM", "662 keV", "HPGe 1,8 keV; NaI 40–50 keV"],
         ["Nền", "cps trong vùng quan tâm", "0,01–1 cps"],
         ["Giới hạn phát hiện", "MDA", "mBq–Bq tùy thời gian đếm"],
         ["Sai số thống kê", "1/√N", "1%–10%"]],
        "Bảng 66.1 · Các đại lượng phổ gamma."))

    b.append(h2("Tóm tắt", "Summary"))
    b.append(p(
        "Phổ gamma định lượng đồng vị qua vạch đặc trưng. Hiệu chuẩn năng lượng + hiệu suất ε(E) = N/(A·t·Iγ) "
        "cho A = N/(t·ε·Iγ). Nền (cosmic, K-40, U/Th) hạn chế độ nhạy — giảm bằng che chì + lớp Cu và chống "
        "trùng phùng. Thống kê Poisson: σ = √N, sai số tương đối 1/√N."))
    b.append('<div class="chapter-nav">'
             '<a href="%s"><span class="k">← Mục lục</span>Sổ tay</a>'
             '<a href="%s" style="text-align:right;"><span class="k">Mục lục →</span>Sổ tay</a></div>'
             % (C.BASE_VI, C.BASE_VI))
    return "".join(b)


def body_en():
    b = []
    b.append(p(
        "Companion to the Vietnamese translation of Chapter 66. Equations and table of the source are "
        "reproduced below; the prose is not repeated."))
    b.append(p(
        "Gamma spectrometry quantifies each isotope via its characteristic lines (Cs-137: 662 keV; Co-60: 1173 "
        "and 1332 keV). Energy calibration with standard sources (Am-241, Cs-137, Co-60, Eu-152) maps channels to "
        "energy; efficiency calibration with a known-activity source gives ε(E) = N_counts/(A·t·I_γ), and sample "
        "activity follows A = N_counts/(t·ε(E)·I_γ). Efficiency depends on sample geometry (distance, density, "
        "container), so standards must match. Natural background (cosmic, K-40, U/Th in soil, machine X-rays) "
        "limits sensitivity; shielding is 10–15 cm lead with an inner copper/steel layer to absorb lead "
        "characteristic X-rays, plus anticoincidence/guard detectors for cosmic rejection; background is measured "
        "separately and subtracted. Decay is Poisson: σ = √N, relative error 1/√N — a 10× error reduction needs "
        "100× the counting time."))
    b.append(table(
        ["Quantity", "Definition", "Typical"],
        [["Efficiency ε(E)", "Counts/(A·t·Iγ)", "HPGe 1%–30%; NaI 10%–40%"],
         ["FWHM resolution", "at 662 keV", "HPGe 1.8 keV; NaI 40–50 keV"],
         ["Background", "cps in ROI", "0.01–1 cps"],
         ["Detection limit", "MDA", "mBq–Bq (count-time dependent)"],
         ["Statistical error", "1/√N", "1%–10%"]],
        "Table 66.1 · Gamma-spectrometry quantities."))
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
