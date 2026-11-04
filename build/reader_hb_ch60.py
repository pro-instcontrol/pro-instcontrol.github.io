# -*- coding: utf-8 -*-
"""Handbook Chapter 60 — Polarization Measurement (Đo phân cực).
Run:  python build/reader_hb_ch60.py
"""
import os
import hb_common as C
from hb_common import p, h2, h3, eq, table

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSLUG = "ch60-polarization-measurement"
CH_NO = 60
TITLE_EN = "Polarization Measurement"
TITLE_VI = "Đo phân cực"
BYLINE = "John G. Webster (chủ biên) · CRC Press, 1999"
FIGS = {}


def body_vi():
    b = []
    b.append(p(
        "Ánh sáng có thể phân cực <b>tuyến tính</b>, <b>tròn</b>, hoặc <b>elip</b>. Trạng thái phân cực được "
        "mô tả bằng vector Jones (trường phức) hoặc bốn tham số Stokes (S₀, S₁, S₂, S₃), tất cả đều đo được "
        "bằng kết hợp polarizer và retarder."))
    b.append(p(
        "Đo phân cực dùng để kiểm tra ứng suất (stress birefringence), chất lượng sợi quang (PMD), độ tinh "
        "khiết hóa học (chirality), kính phân cực, màn hình LCD và đo độ trễ của màng mỏng."))

    b.append(h2("60.1 Polarimeter quay (Stokes)", "Rotating Polarizer / Stokes Polarimeter"))
    b.append(p(
        "Quay một polarizer trước đầu dò và đo công suất theo góc: một tín hiệu sine/cosine với biên độ và pha "
        "cho biết S₁, S₂; chèn thêm một retarder (quarter-wave) quay cho S₃ (thành phần tròn/elip). Từ bốn tham "
        "số Stokes suy ra trạng thái phân cực đầy đủ, độ phân cực P = √(S₁²+S₂²+S₃²)/S₀ và góc trục."))

    b.append(h2("60.2 Phân tích pha trễ (retardance)", "Retardance Analysis"))
    b.append(p(
        "Đo độ trễ (retardance) của màng mỏng/tinh thể: đặt mẫu giữa hai polarizer chéo, đo truyền qua theo "
        "bước sóng (bộ phân tích quang phổ) — độ trễ δ = 2π·Δn·d/λ. Dùng trong kiểm tra màn hình LCD, màng "
        "bảo vệ, và tinh thể lỏng."))

    b.append(h2("60.3 Phân cực trong sợi quang", "Polarization in Optical Fiber"))
    b.append(p(
        "Trong sợi, tán xạ chế độ phân cực (PMD) làm tách hai chế độ phân cực trực giao; đo bằng interferometer "
        "hoặc phân tích Stokes theo bước sóng. Độ trễ PMD (ps/√km) hạn chế tốc độ truyền đường dài. Cũng đo "
        "tổn hao phụ thuộc phân cực (PDL) của các phần tử quang."))

    b.append(h2("60.4 Thông số", "Specifications"))
    b.append(table(
        ["Phép đo", "Phương pháp", "Độ chính xác", "Ứng dụng"],
        [["Stokes đầy đủ", "Polarizer + retarder quay", "0,1%–1%", "Polarimeter"],
         ["Độ trễ retardance", "Quang phổ", "0,1 nm", "LCD, màng mỏng"],
         ["Ứng suất (birefring.)", "Phân cực chéo", "10⁻⁶–10⁻⁵", "Kính, wafer"],
         ["PMD sợi", "Interferometer", "fs–ps", "Truyền thông"],
         ["PDL", "Đo theo trạng thái", "0,01 dB", "Phần tử quang"]],
        "Bảng 60.1 · Các phép đo phân cực."))

    b.append(h2("Tóm tắt", "Summary"))
    b.append(p(
        "Trạng thái phân cực được mô tả bằng Jones/Stokes. Polarimeter quay polarizer + retarder cho bốn tham số "
        "Stokes đầy đủ, suy ra độ phân cực và trục. Retardance δ = 2πΔn·d/λ đo bằng phổ giữa polarizer chéo. "
        "Trong sợi, đo PMD (ps/√km) và PDL. Ứng dụng: ứng suất, LCD, chirality, truyền thông."))
    b.append('<div class="chapter-nav">'
             '<a href="%s"><span class="k">← Mục lục</span>Sổ tay</a>'
             '<a href="%s" style="text-align:right;"><span class="k">Mục lục →</span>Sổ tay</a></div>'
             % (C.BASE_VI, C.BASE_VI))
    return "".join(b)


def body_en():
    b = []
    b.append(p(
        "Companion to the Vietnamese translation of Chapter 60. Equations and table of the source are "
        "reproduced below; the prose is not repeated."))
    b.append(p(
        "Light can be linearly, circularly or elliptically polarized; the state is described by the Jones vector "
        "or the four Stokes parameters (S₀–S₃), all measurable with polarizer + retarder combinations. A rotating "
        "polarizer before the detector yields a sine/cosine signal whose amplitude and phase give S₁, S₂; adding "
        "a rotating quarter-wave retarder gives S₃, so the full state, degree of polarization "
        "P = √(S₁²+S₂²+S₃²)/S₀ and axis follow. Retardance of thin films/LCD cells is δ = 2π·Δn·d/λ, measured "
        "spectrally between crossed polarizers. In fiber, polarization-mode dispersion (PMD) splits the two "
        "orthogonal modes — measured by interferometry or swept-wavelength Stokes analysis (ps/√km) — and "
        "polarization-dependent loss (PDL) of components is measured across states. Applications: stress "
        "birefringence, displays, chirality, telecom."))
    b.append(table(
        ["Measurement", "Method", "Accuracy", "Use"],
        [["Full Stokes", "Rotating pol.+ret.", "0.1%–1%", "Polarimetry"],
         ["Retardance", "Spectroscopy", "0.1 nm", "LCD, films"],
         ["Stress birefr.", "Crossed pol.", "10⁻⁶–10⁻⁵", "Glass, wafer"],
         ["Fiber PMD", "Interferometer", "fs–ps", "Telecom"],
         ["PDL", "State sweep", "0.01 dB", "Components"]],
        "Table 60.1 · Polarization measurements."))
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
