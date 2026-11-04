# -*- coding: utf-8 -*-
"""Handbook Chapter 48 — Magnetic Field Measurement (Đo từ trường).
Run:  python build/reader_hb_ch48.py
"""
import os
import hb_common as C
from hb_common import p, h2, h3, eq, table

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSLUG = "ch48-magnetic-field-measurement"
CH_NO = 48
TITLE_EN = "Magnetic Field Measurement"
TITLE_VI = "Đo từ trường"
BYLINE = "John G. Webster (chủ biên) · CRC Press, 1999"
FIGS = {}


def body_vi():
    b = []
    b.append(p(
        "Từ trường được mô tả bằng mật độ từ thông B (tesla, T) và cường độ từ trường H (A/m), liên hệ B = μ·H "
        "= μ₀μ_r·H. Đo từ trường dùng trong la bàn kỹ thuật số, cảm biến vị trí/tốc độ, y sinh (từ tim đồ), "
        "địa vật lý và nghiên cứu vật liệu."))

    b.append(h2("48.1 Cuộn dây tìm kiếm (search coil)", "Search Coil"))
    b.append(p(
        "Một cuộn N vòng diện tích A quay hoặc dịch chuyển trong từ trường sinh sức điện động cảm ứng:"
    ))
    b.append(eq("e = −N·dΦ/dt = −N·A·dB/dt"))
    b.append(p(
        "Tích phân e theo thời gian cho từ thông Φ, từ đó B. Phương pháp này đo Biến thiên từ trường (AC) rất "
        "tốt, nhưng với từ trường tĩnh cần cuộn quay cơ học để tạo dΦ/dt."))

    b.append(h2("48.2 Hiệu ứng Hall", "Hall Effect"))
    b.append(p(
        "Dải mỏng mang dòng I trong mặt phẳng, đặt vuông góc với B, sinh hiệu điện thế Hall ngang qua bản:"
    ))
    b.append(eq("V_H = (I·B) / (n·q·t)   (n: mật độ hạt tải, t: độ dày, q: điện tích)"))
    b.append(p(
        "Cảm biến Hall đo được cả DC và AC, không tiếp xúc, rẻ, dùng rộng rãi trong đo dòng (qua từ trường vòng "
        "dây), cảm biến vị trí và ô tô. Nhược điểm: nhạy nhiệt độ, cần bù."))

    b.append(h2("48.3 Từ trở (fluxgate) và SQUID", "Fluxgate and SQUID"))
    b.append(p(
        "<b>Fluxgate</b> dùng lõi từ bão hoà tuần hoàn; từ trường ngoài làm lệch dạng sóng từ thông, sinh họa "
        "sóng hài chẵn tỉ lệ với H. Độ nhạy rất cao (nT–pT), dùng đo từ trường Trái Đất và khảo cổ từ. "
        "<b>SQUID</b> (Superconducting Quantum Interference Device) dựa trên hiệu ứng lượng tử Josephson, nhạy "
        "nhất thế giới (fT = 10⁻¹⁵ T), dùng trong não từ đồ (MEG), tim từ đồ (MCG) và vật lý cơ bản."))

    b.append(h2("48.4 Cảm biến từ trở tỉ lệ (MR) và NMR", "Magnetoresistive and NMR"))
    b.append(p(
        "Cảm biến AMR/GMR/TMR thay đổi điện trở theo góc giữa từ trường và dòng, nhỏ, rẻ, dùng trong ổ cứng và "
        "cảm biến góc. <b>NMR (cộng hưởng từ hạt nhân)</b> đo B cực chính xác qua tần số Larmor f = γ·B (γ là "
        "tỉ số giro), là chuẩn hiệu chuẩn máy đo từ trường."))

    b.append(h2("48.5 Thông số", "Specifications"))
    b.append(table(
        ["Cảm biến", "Dải", "Độ nhạy", "Ứng dụng"],
        [["Search coil", "µT–T (AC)", "Tốt với AC", "Đo B biến thiên"],
         ["Hall", "mT–T (DC+AC)", "Trung bình", "Dòng, vị trí, ô tô"],
         ["Fluxgate", "pT–mT", "Rất cao", "Địa từ, khảo cổ"],
         ["SQUID", "fT–nT", "Cao nhất", "MEG, MCG, vật lý"],
         ["AMR/GMR", "nT–mT", "Cao", "Góc, ổ cứng"],
         ["NMR", "mT–T", "Chuẩn xác", "Hiệu chuẩn"]],
        "Bảng 48.1 · Các phương pháp đo từ trường."))

    b.append(h2("Tóm tắt", "Summary"))
    b.append(p(
        "Từ trường B (T) / H (A/m). Search coil: e = −N·A·dB/dt (AC tốt). Hall: V_H = I·B/(nqt), đo DC+AC, rẻ. "
        "Fluxgate nhạy pT–nT (địa từ); SQUID nhạy nhất (fT) cho MEG/MCG. AMR/GMR đo góc; NMR chuẩn hoá qua "
        "f = γB. Chọn cảm biến theo dải và độ nhạy cần thiết."))
    b.append('<div class="chapter-nav">'
             '<a href="%s"><span class="k">← Mục lục</span>Sổ tay</a>'
             '<a href="%s" style="text-align:right;"><span class="k">Mục lục →</span>Sổ tay</a></div>'
             % (C.BASE_VI, C.BASE_VI))
    return "".join(b)


def body_en():
    b = []
    b.append(p(
        "Companion to the Vietnamese translation of Chapter 48. Equations and table of the source are "
        "reproduced below; the prose is not repeated."))
    b.append(p(
        "Magnetic field: B (tesla) and H (A/m), with B = μ₀μ_r H. A search coil of N turns, area A, gives an "
        "induced emf e = −N·dΦ/dt = −N·A·dB/dt; integrating yields Φ and B — excellent for AC fields, but a "
        "static field needs mechanical rotation to create dΦ/dt. The Hall effect gives a transverse voltage "
        "V_H = I·B/(n·q·t) (n carrier density, t thickness), measuring DC and AC contactlessly and cheaply — "
        "ubiquitous in current sensing and position sensors, though temperature-compensated. A fluxgate uses a "
        "periodically saturated core; the external field distorts the flux waveform, producing even harmonics "
        "∝ H, reaching pT–nT sensitivity for geomagnetics. The SQUID (Josephson quantum interference) is the "
        "most sensitive (fT = 10⁻¹⁵ T) for MEG/MCG. AMR/GMR/TMR sensors change resistance with field angle "
        "(disk drives, angle sensors); NMR measures B via the Larmor frequency f = γB and serves as the "
        "calibration standard."))
    b.append(table(
        ["Sensor", "Range", "Sensitivity", "Use"],
        [["Search coil", "µT–T (AC)", "Good AC", "Varying B"],
         ["Hall", "mT–T (DC+AC)", "Medium", "Current, position, auto"],
         ["Fluxgate", "pT–mT", "Very high", "Geomagnetic, archaeo."],
         ["SQUID", "fT–nT", "Highest", "MEG, MCG, physics"],
         ["AMR/GMR", "nT–mT", "High", "Angle, disks"],
         ["NMR", "mT–T", "Absolute", "Calibration"]],
        "Table 48.1 · Magnetic-field measurement methods."))
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
