# -*- coding: utf-8 -*-
"""Handbook Chapter 40 — Power Factor Measurement (Đo hệ số công suất).
Run:  python build/reader_hb_ch40.py
"""
import os
import hb_common as C
from hb_common import p, h2, h3, eq, table

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSLUG = "ch40-power-factor-measurement"
CH_NO = 40
TITLE_EN = "Power Factor Measurement"
TITLE_VI = "Đo hệ số công suất"
BYLINE = "John G. Webster (chủ biên) · CRC Press, 1999"
FIGS = {}


def body_vi():
    b = []
    b.append(p(
        "<b>Hệ số công suất</b> (power factor, PF) là tỉ số giữa công suất tác dụng và công suất biểu kiến: "
        "λ = P / S = cos φ, với φ là góc lệch pha giữa điện áp và dòng điện ở tần số cơ bản. Hệ số công suất "
        "càng thấp, dòng điện cần thiết để truyền cùng công suất càng lớn, gây tổn thất đường dây và giảm "
        "hiệu quả. Đo hệ số công suất là bước then chốt trong quản lý chất lượng điện năng."))
    b.append(p(
        "Cần phân biệt hai khái niệm: <b>hệ số công suất dịch chuyển</b> (displacement PF) chỉ xét thành "
        "phần cơ bản cos φ₁, và <b>hệ số công suất thực</b> (true PF) = P/S bao gồm cả méo dạng sóng do "
        "sóng hài: true PF = (cos φ₁)·(I₁/I_rms), trong đó I₁/I_rms là hệ số méo dòng (distortion factor)."))

    b.append(h2("40.1 Phương pháp watt – vôn – ampe", "Watt-Volt-Ammeter Method"))
    b.append(p(
        "Cách trực tiếp nhất: đo P bằng watt kế, V bằng vôn kế và I bằng ampe kế, rồi tính λ = P/(V·I). "
        "Phương pháp này cho true PF nếu watt kế đo đúng công suất thực, nhưng đòi hộp thiết bị và hiệu "
        "chuẩn nhiều đồng hồ."))

    b.append(h2("40.2 Phương pháp ba vôn kế", "Three-Voltmeter Method"))
    b.append(p(
        "Mắc nối tiếp một trở thuần R (không pha) với phần tử cần đo (Z), cấp điện áp xoay chiều. Gọi V₁ là "
        "điện áp trên R, V₂ trên Z, và V₃ là điện áp nguồn (tổng hai nhánh). Áp dụng định luật Kirchhoff "
        "cho tam giác điện áp:"))
    b.append(eq("V₃² = V₁² + V₂² + 2·V₁·V₂·cos φ   ⇒   cos φ = (V₃² − V₁² − V₂²) / (2·V₁·V₂)"))
    b.append(p(
        "Từ cos φ suy ra hệ số công suất. Phương pháp chỉ cần ba phép đo điện áp, thuận tiện khi không có "
        "sẵn watt kế. Tương tự có <b>phương pháp ba ampe kế</b> (three-ammeter method) dùng ba nhánh dòng."))

    b.append(h2("40.3 Pha kế và mạch điện tử", "Phase Meters and Electronic Methods"))
    b.append(p(
        "Pha kế (phase meter) đo trực tiếp góc φ giữa hai tín hiệu cùng tần số, thường dựa trên chuyển đổi "
        "thời gian–điện áp: một cổng logic (XOR hoặc flip-flop) tạo xung có độ rộng Δt tỉ lệ với φ; trung "
        "bình xung đó hoặc đếm Δt cho điện áp ∝ φ, từ đó λ = cos φ. Các vi mạch đo công suất (ADE7xxx) tính "
        "luôn PF, P, Q, S theo thời gian thực từ tích v·i tức thời."))
    b.append(p(
        "Với mạng có sóng hài, phương pháp dựa trên φ cơ bản (ba vôn kế, pha kế tần số cơ bản) chỉ cho "
        "displacement PF; muốn true PF phải dùng watt kế điện tử nhân tức thời."))

    b.append(h2("40.4 Thông số", "Specifications"))
    b.append(table(
        ["Phương pháp", "Ưu điểm", "Nhược điểm"],
        [["Watt–V–A", "Cho true PF trực tiếp", "Cần 3 thiết bị, hiệu chuẩn"],
         ["Ba vôn kế", "Chỉ đo V, đơn giản", "Sai số do trở chuẩn"],
         ["Ba ampe kế", "Chỉ đo I", "Cần trở chuẩn chính xác"],
         ["Pha kế", "Đọc φ trực tiếp", "Thường chỉ cơ bản (cos φ₁)"],
         ["IC đo công suất", "P,Q,S,PF thời gian thực", "Cần giao tiếp/hiệu chuẩn"]],
        "Bảng 40.1 · Các phương pháp đo hệ số công suất."))

    b.append(h2("Tóm tắt", "Summary"))
    b.append(p(
        "Hệ số công suất λ = P/S = cos φ. Đo trực tiếp bằng watt–vôn–ampe (λ = P/(V·I)); bằng ba vôn kế "
        "qua cosφ = (V₃²−V₁²−V₂²)/(2V₁V₂); hoặc bằng pha kế đo φ rồi lấy cosφ. Phân biệt displacement PF "
        "(cosφ₁) và true PF = cosφ₁·(I₁/I_rms) khi có sóng hài — true PF chỉ có được từ watt kế nhân tức "
        "thời."))
    b.append('<div class="chapter-nav">'
             '<a href="%s"><span class="k">← Mục lục</span>Sổ tay</a>'
             '<a href="%s" style="text-align:right;"><span class="k">Mục lục →</span>Sổ tay</a></div>'
             % (C.BASE_VI, C.BASE_VI))
    return "".join(b)


def body_en():
    b = []
    b.append(p(
        "Companion to the Vietnamese translation of Chapter 40. Equations and table of the source are "
        "reproduced below; the prose is not repeated."))
    b.append(p(
        "Power factor λ = P/S = cos φ, where φ is the phase angle between voltage and current at the "
        "fundamental frequency. Distinguish the displacement PF (cos φ₁, fundamental only) from the true "
        "PF = P/S which includes waveform distortion: true PF = cos φ₁ · (I₁/I_rms), where I₁/I_rms is the "
        "current distortion factor."))
    b.append(p(
        "The watt–volt–ammeter method measures P, V, I and computes λ = P/(V·I) — a true PF if the "
        "wattmeter is accurate. The three-voltmeter method places a non-inductive resistor R in series "
        "with the load Z; with V₁ across R, V₂ across Z and V₃ the source, Kirchhoff gives "
        "V₃² = V₁²+V₂²+2V₁V₂cosφ ⇒ cosφ = (V₃²−V₁²−V₂²)/(2V₁V₂). A three-ammeter method is analogous. "
        "Phase meters convert the time delay Δt (∝φ) via a logic gate to a voltage ∝φ; power-metering ICs "
        "compute PF, P, Q, S in real time from instantaneous v·i. Only the instantaneous-multiplier approach "
        "yields true PF when harmonics are present."))
    b.append(table(
        ["Method", "Advantage", "Drawback"],
        [["Watt–V–A", "Direct true PF", "3 instruments, calibration"],
         ["3-voltmeter", "Voltage only, simple", "Error from std resistor"],
         ["3-ammeter", "Current only", "Needs accurate std resistor"],
         ["Phase meter", "Reads φ directly", "Often fundamental only"],
         ["IC metering", "Real-time P,Q,S,PF", "Needs interface/calibration"]],
        "Table 40.1 · Power-factor measurement methods."))
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
