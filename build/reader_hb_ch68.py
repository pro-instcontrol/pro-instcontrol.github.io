# -*- coding: utf-8 -*-
"""Handbook Chapter 68 — Neutron Measurement (Đo nơ tron).
Run:  python build/reader_hb_ch68.py
"""
import os
import hb_common as C
from hb_common import p, h2, h3, eq, table

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSLUG = "ch68-neutron-measurement"
CH_NO = 68
TITLE_EN = "Neutron Measurement"
TITLE_VI = "Đo nơ tron"
BYLINE = "John G. Webster (chủ biên) · CRC Press, 1999"
FIGS = {}


def body_vi():
    b = []
    b.append(p(
        "Nơ tron không tích điện, không ion hóa trực tiếp, nên đo gián tiếp qua <b>phản ứng hạt nhân</b> sinh "
        "hạt tích điện. Phổ năng lượng chia: <b>nhiệt</b> (thermal, <0,5 eV), <b>trung gian</b> (0,5 eV–0,1 "
        "MeV), <b>nhanh</b> (>0,1 MeV). Nguồn: lò phản ứng, máy gia tốc, nguồn đồng vị (Am-Be, Cf-252)."))

    b.append(h2("68.1 Counter BF₃, ³He và Li-6", "BF₃, ³He and Li-6 Counters"))
    b.append(p(
        "<b>BF₃ counter</b> dùng khí boron trifluoride giàu ¹⁰B: phản ứng ¹⁰B(n,α)⁷Li sinh hạt α và ⁷Li tích "
        "điện, ion hóa khí, tạo xung lớn — đo nơ tron nhiệt chuẩn, giá rẻ. <b>³He counter</b> dùng phản ứng "
        "³He(n,p)³H — hiệu suất cao hơn, an toàn hơn (khí không độc), phổ biến nhất hiện nay. <b>Li-6 scintillator</b> "
        "(¹⁴⁶Li glass hoặc ⁶LiI) phản ứng ⁶Li(n,α)³H, cho xung sáng; có thể phân biệt gamma bằng phân tích "
        "hình dạng xung (PSD)."))

    b.append(h2("68.2 Nơ tron nhanh: proton recoil và fission chamber", "Fast Neutrons: Proton Recoil and Fission"))
    b.append(p(
        "Nơ tron nhanh đo bằng <b>proton recoil</b>: tán xạ đàn hồi trên hydro (plastique scintillator, H quanh "
        "môi trường) sinh proton tích điện, xung ∝ năng lượng nơ tron. <b>Fission chamber</b> dùng ²³⁵U hoặc "
        "²³⁸U: phản ứng phân hạch sinh fragment năng lượng lớn — xung rất lớn, dễ tách gamma, dùng trong lò "
        "phản ứng."))

    b.append(h2("68.3 Đo phổ nơ tron", "Neutron Spectrometry"))
    b.append(p(
        "<b>Quả cầu Bonner</b> (Bonner sphere): một ³He counter cỡ nhỏ đặt trong các quả cầu polyethylene đường "
        "kính khác nhau; mỗi quả cầu nhạy với một dải năng lượng, giải tục (unfolding) cho phổ. <b>Time-of-flight</b> "
        "(TOF): đo thời gian bay trên quãng đường L, E = ½m(L/t)², phân giải cao nhưng cần xung và khoảng cách lớn. "
        "<b>Proton recoil telescope</b> cho phổ nơ tron nhanh chính xác."))

    b.append(h2("68.4 Thông số", "Specifications"))
    b.append(table(
        ["Detector", "Phản ứng", "Dải năng lượng", "Ứng dụng"],
        [["BF₃ counter", "¹⁰B(n,α)⁷Li", "Nhiệt", "Môi trường, lò"],
         ["³He counter", "³He(n,p)³H", "Nhiệt (với moderator)", "Chuẩn, phổ rộng"],
         ["Li-6 scint.", "⁶Li(n,α)³H", "Nhiệt–trung gian", "PSD, phổ"],
         ["Proton recoil", "H(n,n)H", "Nhanh (>0,1 MeV)", "Phổ nhanh"],
         ["Fission chamber", "²³⁵U(n,f)", "Mọi dải", "Lò phản ứng"],
         ["Bonner sphere", "³He + moderator", "Phổ đầy đủ", "Unfolding phổ"]],
        "Bảng 68.1 · Các detector nơ tron."))

    b.append(h2("Tóm tắt", "Summary"))
    b.append(p(
        "Nơ tron đo gián tiếp: ¹⁰B(n,α) (BF₃), ³He(n,p), ⁶Li(n,α) cho nhiệt; proton recoil và fission chamber "
        "cho nhanh. Phổ đo bằng Bonner sphere (unfolding) hoặc TOF. Hiệu suất phụ thuộc moderator; gamma tách "
        "bằng PSD hoặc ngưỡng xung."))
    b.append('<div class="chapter-nav">'
             '<a href="%s"><span class="k">← Mục lục</span>Sổ tay</a>'
             '<a href="%s" style="text-align:right;"><span class="k">Mục lục →</span>Sổ tay</a></div>'
             % (C.BASE_VI, C.BASE_VI))
    return "".join(b)


def body_en():
    b = []
    b.append(p(
        "Companion to the Vietnamese translation of Chapter 68. The table of the source is reproduced below; "
        "the prose is not repeated."))
    b.append(p(
        "Neutrons carry no charge and must be detected indirectly via nuclear reactions producing charged "
        "particles. Energy classes: thermal (<0.5 eV), intermediate (0.5 eV–0.1 MeV), fast (>0.1 MeV); sources "
        "include reactors, accelerators and isotopes (Am-Be, Cf-252). The BF₃ counter uses ¹⁰B-rich gas: the "
        "¹⁰B(n,α)⁷Li reaction ionizes the gas with a large pulse — the classic cheap thermal-neutron standard. "
        "The ³He counter (³He(n,p)³H) offers higher efficiency and is now the most common. ⁶Li scintillators "
        "(Li glass, ⁶LiI) via ⁶Li(n,α)³H support pulse-shape discrimination (PSD) against gammas. Fast neutrons "
        "are measured by proton recoil (elastic scattering on hydrogen in plastic scintillator, pulse ∝ energy) "
        "or fission chambers (²³⁵U/²³⁸U — very large fragments, easy gamma rejection, reactor use). "
        "Spectrometry: Bonner spheres (a small ³He counter inside polyethylene spheres of graded size; unfolding "
        "gives the spectrum), time-of-flight (E = ½m(L/t)²), and recoil telescopes."))
    b.append(table(
        ["Detector", "Reaction", "Energy range", "Use"],
        [["BF₃ counter", "¹⁰B(n,α)⁷Li", "Thermal", "Survey, reactor"],
         ["³He counter", "³He(n,p)³H", "Thermal (+moderator)", "Standard, broad"],
         ["Li-6 scint.", "⁶Li(n,α)³H", "Thermal–interm.", "PSD, spectro."],
         ["Proton recoil", "H(n,n)H", "Fast (>0.1 MeV)", "Fast spectra"],
         ["Fission chamber", "²³⁵U(n,f)", "All", "Reactors"],
         ["Bonner sphere", "³He + moderator", "Full spectrum", "Unfolding"]],
        "Table 68.1 · Neutron detectors."))
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
