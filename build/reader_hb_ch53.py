# -*- coding: utf-8 -*-
"""Handbook Chapter 53 — Distortion Measurement (Đo méo).
Run:  python build/reader_hb_ch53.py
"""
import os
import hb_common as C
from hb_common import p, h2, h3, eq, table

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSLUG = "ch53-distortion-measurement"
CH_NO = 53
TITLE_EN = "Distortion Measurement"
TITLE_VI = "Đo méo"
BYLINE = "John G. Webster (chủ biên) · CRC Press, 1999"
FIGS = {}


def body_vi():
    b = []
    b.append(p(
        "<b>Méo</b> (distortion) là sự biến dạng tín hiệu khi qua thiết bị không lý tưởng. Các loại chính: méo "
        "hài (harmonic, do phi tuyến), méo giao điều (intermodulation, IM), méo biên độ/pha. Đo méo đánh giá "
        "chất lượng khuếch đại, bộ phát và kênh truyền."))

    b.append(h2("53.1 Méo hài tổng (THD)", "Total Harmonic Distortion (THD)"))
    b.append(p(
        "Với tín hiệu hình sine có điện áp cơ bản V₁ và các họ hài Vₙ (n ≥ 2), THD là tỉ số căn bậc hai tổng "
        "công suất hài trên cơ bản:"))
    b.append(eq("THD = √(V₂² + V₃² + … ) / V₁   (thường tính bằng %)"))
    b.append(p(
        "Bộ <b>đo méo (distortion analyzer)</b> dùng bộ lọc loại bỏ hoàn toàn thành phần cơ bản (notch filter "
        "hoặc khóa đồng bộ), để lại phần dư chứa hài, rồi đo điện áp phần dư bằng true-RMS. Kết quả so với V₁ "
        "cho THD. Phương pháp FFT/DSP hiện đại tính trực tiếp phổ và THD từ mẫu số."))

    b.append(h2("53.2 Méo giao điều (IMD)", "Intermodulation Distortion (IMD)"))
    b.append(p(
        "Bơm hai tín hiệu tần số f₁, f₂ (cách nhau vài kHz) vào thiết bị; méo phi tuyến sinh ra các tần số "
        "giao điều 2f₁−f₂, 2f₂−f₁ (sản phẩm bậc ba) và f₁+f₂, |f₁−f₂|. Đo biên độ các sản phẩm này so với tín "
        "hiệu gốc cho IMD (thường dBc). IMD quan trọng trong âm thanh và RF vì tai/nhận rất nhạy với nó."))

    b.append(h2("53.3 Các chỉ tiêu khác", "Other Metrics"))
    b.append(p(
        "Ngoài THD và IMD, còn có <b>SMPTE/DIN IMD</b> (tín hiệu cao tần mang tín hiệu thấp tần), <b>méo xuyến "
        "vòng</b> (CCIF), và tỉ số tín hiệu trên nhiễu cộng méo (SINAD). Đo thực tế dùng bộ phân tích âm thanh "
        "hoặc vector signal analyzer."))

    b.append(h2("53.4 Thông số", "Specifications"))
    b.append(table(
        ["Chỉ tiêu", "Định nghĩa", "Điển hình"],
        [["THD", "√(ΣVₙ²)/V₁", "< 0,01% (âm thanh tốt)"],
         ["IMD (3rd)", "2f₁−f₂ / tín hiệu", "−60 đến −90 dBc"],
         ["SINAD", "S/(N+D)", "> 70 dB (radio)"],
         ["CCIF IMD", "Sản phẩm xuyến vòng", "Âm thanh Hi-Fi"]],
        "Bảng 53.1 · Các chỉ tiêu méo."))

    b.append(h2("Tóm tắt", "Summary"))
    b.append(p(
        "Méo do phi tuyến/biến dạng. THD = √(ΣVₙ²)/V₁, đo bằng cách lọc bỏ cơ bản rồi true-RMS phần dư, hoặc "
        "FFT. IMD đo sản phẩm giao điều 2f₁−f₂ từ hai tín hiệu f₁,f₂. Các chỉ tiêu SINAD, CCIF đánh giá tổng "
        "thể. Méo thấp (<0,01% THD) là yêu cầu âm thanh/RF chất lượng cao."))
    b.append('<div class="chapter-nav">'
             '<a href="%s"><span class="k">← Mục lục</span>Sổ tay</a>'
             '<a href="%s" style="text-align:right;"><span class="k">Mục lục →</span>Sổ tay</a></div>'
             % (C.BASE_VI, C.BASE_VI))
    return "".join(b)


def body_en():
    b = []
    b.append(p(
        "Companion to the Vietnamese translation of Chapter 53. Equations and table of the source are "
        "reproduced below; the prose is not repeated."))
    b.append(p(
        "Distortion is signal deformation through a non-ideal device: harmonic (nonlinearity), intermodulation, "
        "and amplitude/phase distortion. Total harmonic distortion THD = √(V₂²+V₃²+…)/V₁ (%). A distortion "
        "analyzer nulls the fundamental with a notch/synchronous filter, leaving the residual harmonics, which a "
        "true-RMS meter reads; the ratio to V₁ is THD. DSP/FFT computes the spectrum and THD directly. "
        "Intermodulation distortion (IMD) drives two tones f₁, f₂ and measures the intermodulation products "
        "2f₁−f₂, 2f₂−f₁ (third-order) and f₁+f₂, |f₁−f₂| relative to the originals (dBc) — critical in audio "
        "and RF because the ear/receiver is very sensitive to it. Other metrics: SMPTE/DIN IMD (HF carrier "
        "modulated by LF), CCIF difference-tone, and SINAD = S/(N+D). High-quality audio/RF targets THD "
        "< 0.01%."))
    b.append(table(
        ["Metric", "Definition", "Typical"],
        [["THD", "√(ΣVₙ²)/V₁", "< 0.01% (good audio)"],
         ["IMD (3rd)", "2f₁−f₂ / signal", "−60 to −90 dBc"],
         ["SINAD", "S/(N+D)", "> 70 dB (radio)"],
         ["CCIF IMD", "Difference product", "Hi-Fi audio"]],
        "Table 53.1 · Distortion metrics."))
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
