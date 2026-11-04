# -*- coding: utf-8 -*-
"""Handbook Chapter 69 — Dosimetry Measurement (Đo liều bức xạ).
Run:  python build/reader_hb_ch69.py
"""
import os
import hb_common as C
from hb_common import p, h2, h3, eq, table

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSLUG = "ch69-dosimetry-measurement"
CH_NO = 69
TITLE_EN = "Dosimetry Measurement"
TITLE_VI = "Đo liều bức xạ"
BYLINE = "John G. Webster (chủ biên) · CRC Press, 1999"
FIGS = {}


def body_vi():
    b = []
    b.append(p(
        "<b>Liều hấp thụ</b> (absorbed dose) D là năng lượng bức xạ hấp thụ trên đơn vị khối lượng: D = dE/dm, "
        "đơn vị gray (Gy = J/kg). <b>Liều tương đương</b> (equivalent dose) H = D·w_R tính theo sievert (Sv), "
        "với w_R là hệ số trọng số bức xạ (γ, β: 1; proton: 2; α: 20). <b>Liều hiệu dụng</b> E = Σ w_T·H_T cộng "
        "theo độ nhạy từng cơ quan w_T."))
    b.append(p(
        "Đo liều dùng để bảo vệ người lao động (nhân viên xạ), kiểm soát liều bệnh nhân trong xạ trị/chẩn đoán "
        "hình ảnh, và quan trắc môi trường."))

    b.append(h2("69.1 Buồng ion và máy đo liều", "Ion Chambers and Survey Meters"))
    b.append(p(
        "Buồng ion đo dòng ion hóa, tuyến tính theo <b>tốc độ liều</b> (µSv/h, mGy/min), là thiết bị chuẩn của "
        "phòng đo liều. Máy đo liều cầm tay (survey meter) dùng buồng ion hoặc GM, hiệu chuẩn theo tốc độ liều "
        "tương đương với hệ số năng lượng. Thạch đo liều (phantom) mô phỏng mô người để hiệu chuẩn xạ trị."))

    b.append(h2("69.2 Dosimeter thụ động", "Passive Dosimeters"))
    b.append(p(
        "<b>TLD</b> (thermoluminescent dosimeter, LiF): electron bị bắt giữ trong bẫy khi chiếu xạ; khi nung lên "
        "chúng phát sáng, cường độ ∝ liều. <b>OSL</b> (optically stimulated, Al₂O₃:C) đọc bằng laser — nhạy hơn, "
        "đọc lại được, là chuẩn hiện nay của badge nhân viên. <b>Phim</b> (film badge) cổ điển, còn dùng để ghi "
        "chứng. <b>Nuclear track</b> (CR-39) cho α và nơ tron."))

    b.append(h2("69.3 Dosimeter chủ động", "Active/Electronic Dosimeters"))
    b.append(p(
        "Dosimeter điện tử dùng bán dẫn (Si diode, MOSFET) hoặc buồng ion nhỏ, đọc tức thời, có báo động ngưỡng "
        "— dùng cho nhân viên vào vùng bức xạ và cho xạ trị (in-vivo dosimetry với diode gắn trên bệnh nhân)."))

    b.append(h2("69.4 Thông số", "Specifications"))
    b.append(table(
        ["Dosimeter", "Dải liều", "Độ chính xác", "Ứng dụng"],
        [["Buồng ion", "nGy–Gy", "±2%–5%", "Chuẩn, phòng đo"],
         ["TLD (LiF)", "10 µSv–10 Sv", "±5%–10%", "Badge nhân viên"],
         ["OSL", "10 µSv–10 Sv", "±5%", "Badge hiện đại"],
         ["Phim", "0,1 mSv–10 Sv", "±10%–20%", "Ghi chứng"],
         ["Si diode / MOSFET", "µGy–Gy", "±3%–5%", "Xạ trị, tức thời"],
         ["CR-39", "α, n track", "±15%", "α, nơ tron"]],
        "Bảng 69.1 · Các dosimeter."))

    b.append(h2("Tóm tắt", "Summary"))
    b.append(p(
        "Liều hấp thụ D (Gy = J/kg); H = D·w_R (Sv); liều hiệu dụng E = Σ w_T·H_T. Buồng ion đo tốc độ liều "
        "(chuẩn); TLD/OSL là badge thụ động nhân viên; film badge ghi chứng; CR-39 cho α/nơ tron; dosimeter "
        "điện tử (diode/MOSFET) đọc tức thời, dùng xạ trị và báo động."))
    b.append('<div class="chapter-nav">'
             '<a href="%s"><span class="k">← Mục lục</span>Sổ tay</a>'
             '<a href="%s" style="text-align:right;"><span class="k">Mục lục →</span>Sổ tay</a></div>'
             % (C.BASE_VI, C.BASE_VI))
    return "".join(b)


def body_en():
    b = []
    b.append(p(
        "Companion to the Vietnamese translation of Chapter 69. Equations and table of the source are "
        "reproduced below; the prose is not repeated."))
    b.append(p(
        "Absorbed dose D = dE/dm in gray (Gy = J/kg); equivalent dose H = D·w_R in sievert (Sv) with radiation "
        "weighting w_R (γ, β: 1; protons: 2; α: 20); effective dose E = Σ w_T·H_T weights organs. Ion chambers "
        "measure dose rate linearly (µSv/h, mGy/min) — the standards-laboratory instrument; survey meters use "
        "ion chambers or GM tubes energy-compensated for H*(10); phantoms calibrate radiotherapy. Passive "
        "dosimeters: TLD (LiF — traps release light when heated, ∝ dose), OSL (Al₂O₃:C, laser-read, re-readable, "
        "the modern personnel-badge standard), film badges (legacy record), and CR-39 nuclear-track for α/neutron. "
        "Active dosimeters use Si diodes/MOSFETs or small ion chambers for real-time readout with alarm thresholds "
        "(entry-control, in-vivo radiotherapy dosimetry)."))
    b.append(table(
        ["Dosimeter", "Dose range", "Accuracy", "Use"],
        [["Ion chamber", "nGy–Gy", "±2%–5%", "Standard, lab"],
         ["TLD (LiF)", "10 µSv–10 Sv", "±5%–10%", "Personnel badge"],
         ["OSL", "10 µSv–10 Sv", "±5%", "Modern badge"],
         ["Film", "0.1 mSv–10 Sv", "±10%–20%", "Record"],
         ["Si diode / MOSFET", "µGy–Gy", "±3%–5%", "RT, real-time"],
         ["CR-39", "α, n tracks", "±15%", "Alpha, neutron"]],
        "Table 69.1 · Dosimeters."))
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
