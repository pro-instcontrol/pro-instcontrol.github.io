# -*- coding: utf-8 -*-
"""Handbook Chapter 74 — Biopotentials and Electrophysiology Measurement (Đo điện thế sinh học và điện sinh lý).
Run:  python build/reader_hb_ch74.py
"""
import os
import hb_common as C
from hb_common import p, h2, h3, eq, table

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSLUG = "ch74-biopotentials-and-electrophysiology-measurement"
CH_NO = 74
TITLE_EN = "Biopotentials and Electrophysiology Measurement"
TITLE_VI = "Đo điện thế sinh học và điện sinh lý"
BYLINE = "John G. Webster (chủ biên) · CRC Press, 1999"
FIGS = {}


def body_vi():
    b = []
    b.append(p(
        "Tế bào excitable (tim, cơ, thần kinh) sinh hiệu điện thế màng. Đo tại bề mặt da cho <b>ECG</b> (tim, "
        "0,05–100 Hz, 0,1–5 mV), <b>EEG</b> (não, 0,5–100 Hz, 10–100 µV), <b>EMG</b> (cơ, 20–2000 Hz, 50 µV–5 "
        "mV), <b>EOG</b> (mắt), <b>EGG</b> (dạ dày). Vì tín hiệu rất nhỏ và trở kháng nguồn cao (kΩ–MΩ), đo "
        "cần khuếch đại chuyên dụng."))
    b.append(p(
        "<b>Khuếch đại dụng cụ</b> (instrumentation amplifier) có trở vào rất cao (>100 MΩ), <b>CMRR</b> cao "
        "(>100 dB để triệt nhiễu điện lưới chung) và độ lợi 500–1000×. Đầu vào cách ly (isolation, quang hoặc "
        "biến áp) để bảo vệ bệnh nhân theo chuẩn IEC 60601."))

    b.append(h2("74.1 Electrode", "Electrodes"))
    b.append(p(
        "<b>Electrode Ag/AgCl</b> với gel dẫn là chuẩn vì trở tiếp xúc thấp, ổn định và ít trôi. Các loại: đĩa "
        "dán (disposable), kẹp tay, kim (cho EMG), electrode khô (không gel, cho thiết bị mặc). Trở tiếp xúc "
        "phải thấp (<10 kΩ) — chuẩn bị da (cạo, chà nhẹ, gel) là then chốt để giảm nhiễu."))

    b.append(h2("74.2 Nhiễu và lọc", "Noise and Filtering"))
    b.append(p(
        "Nhiễu chính: điện lưới 50/60 Hz (mode chung và mode vi phân), trôi điện cực (baseline drift), nhiễu cơ "
        "(EMG lẫn vào EEG). Kỹ thuật: dây dẫn che chắn, bệnh nhân cách ly đất, lọc thông cao 0,05–0,5 Hz, thông "
        "thấp theo băng tin hiệu, và <b>notch 50/60 Hz</b>. ECG lọc chẩn đoán 0,05–150 Hz; monitor 0,5–40 Hz."))

    b.append(h2("74.3 Thông số", "Specifications"))
    b.append(table(
        ["Tín hiệu", "Biên độ", "Băng tần", "Ứng dụng"],
        [["ECG", "0,1–5 mV", "0,05–150 Hz", "Tim mạch"],
         ["EEG", "10–100 µV", "0,5–100 Hz", "Thần kinh, giấc ngủ"],
         ["EMG", "50 µV–5 mV", "20–2000 Hz", "Cơ, phục hồi"],
         ["EOG", "50 µV–3 mV", "DC–100 Hz", "Mắt, giấc ngủ"],
         ["Điện thế đơn tế bào", "mV", "DC–10 kHz", "Khoa học cơ bản"]],
        "Bảng 74.1 · Các tín hiệu sinh điện."))

    b.append(h2("Tóm tắt", "Summary"))
    b.append(p(
        "Biopotential rất nhỏ (µV–mV), trở nguồn cao: cần khuếch đại dụng cụ (CMRR >100 dB, cách ly IEC 60601), "
        "electrode Ag/AgCl với chuẩn bị da tốt, lọc cao/thấp theo băng và notch 50/60 Hz. ECG 0,05–150 Hz; EEG "
        "10–100 µV; EMG 20–2000 Hz."))
    b.append('<div class="chapter-nav">'
             '<a href="%s"><span class="k">← Mục lục</span>Sổ tay</a>'
             '<a href="%s" style="text-align:right;"><span class="k">Mục lục →</span>Sổ tay</a></div>'
             % (C.BASE_VI, C.BASE_VI))
    return "".join(b)


def body_en():
    b = []
    b.append(p(
        "Companion to the Vietnamese translation of Chapter 74. The table of the source is reproduced below; "
        "the prose is not repeated."))
    b.append(p(
        "Excitable cells (cardiac, muscle, neural) generate membrane potentials. Surface measurements: ECG "
        "(0.1–5 mV, 0.05–100 Hz), EEG (10–100 µV, 0.5–100 Hz), EMG (50 µV–5 mV, 20–2000 Hz), EOG, EGG. Signals "
        "are tiny with high source impedance (kΩ–MΩ), so an instrumentation amplifier with very high input Z "
        "(>100 MΩ), high CMRR (>100 dB to reject line common-mode) and 500–1000× gain is required; patient "
        "isolation (optical/transformer) per IEC 60601. Ag/AgCl electrodes with conductive gel are the standard "
        "(low, stable contact potential); skin preparation keeps contact impedance <10 kΩ. Main noise: 50/60 Hz "
        "line (common and differential mode), electrode drift, motion; mitigations: shielded leads, patient "
        "isolation from ground, high-pass 0.05–0.5 Hz, band-limited low-pass, 50/60 Hz notch; ECG diagnostic "
        "band 0.05–150 Hz vs monitoring 0.5–40 Hz."))
    b.append(table(
        ["Signal", "Amplitude", "Band", "Use"],
        [["ECG", "0.1–5 mV", "0.05–150 Hz", "Cardiology"],
         ["EEG", "10–100 µV", "0.5–100 Hz", "Neuro, sleep"],
         ["EMG", "50 µV–5 mV", "20–2000 Hz", "Muscle, rehab"],
         ["EOG", "50 µV–3 mV", "DC–100 Hz", "Eye, sleep"],
         ["Single-cell", "mV", "DC–10 kHz", "Basic science"]],
        "Table 74.1 · Biopotential signals."))
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
