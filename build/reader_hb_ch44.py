# -*- coding: utf-8 -*-
"""Handbook Chapter 44 — Charge Measurement (Đo điện tích).
Run:  python build/reader_hb_ch44.py
"""
import os
import hb_common as C
from hb_common import p, h2, h3, eq, table

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSLUG = "ch44-charge-measurement"
CH_NO = 44
TITLE_EN = "Charge Measurement"
TITLE_VI = "Đo điện tích"
BYLINE = "John G. Webster (chủ biên) · CRC Press, 1999"
FIGS = {}


def body_vi():
    b = []
    b.append(p(
        "Điện tích (charge) Q là đại lượng cơ bản, liên hệ với dòng và điện áp qua Q = ∫ i dt = C·V. Đơn vị "
        "là coulomb (C); trong vật lý hạt, điện tích nguyên tố e ≈ 1,602·10⁻¹⁹ C. Đo điện tích dùng để xác "
        "định dòng cực nhỏ tích luỹ theo thời gian, điện tích bề mặt, và là nguyên lý của nhiều cảm biến "
        "(quang điện, bức xạ, hạt tích điện)."))
    b.append(p(
        "Vì điện tích cực nhỏ (pC–nC) dễ rò rỉ qua trở cách điện và bị nhiễu, đo điện tích đòi hỏi đầu vào "
        "cách điện cực cao (electrometer, FET), vỏ che chắn và guard."))

    b.append(h2("44.1 Electrometer tụ hồi tiếp", "Feedback Electrometer"))
    b.append(p(
        "Cách chính xác nhất: dùng bộ khuếch đại thuật toán có tụ hồi tiếp C_f. Điện tích đầu vào Q_in tích "
        "lũy trên C_f, và điện áp đầu ra:"))
    b.append(eq("V_out = −Q_in / C_f"))
    b.append(p(
        "Vì đầu vào ảo địa (virtual ground), hầu như không dòng rò; độ nhạy đạt được 10⁻¹⁵–10⁻¹⁶ C. Đây là "
        "công cụ chuẩn trong đo dòng cực nhỏ và điện tích bức xạ."))

    b.append(h2("44.2 Phương pháp qV (charge–voltage)", "Charge–Voltage (qV) Method"))
    b.append(p(
        "Điện tích chưa biết Q trên một tụ mẫu C_x được chuyển sang tụ chuẩn C_f qua công tắc; đo điện áp "
        "trên C_f rồi tính Q = C_f·V_f. Lặp lại nhiều lần (phương pháp dither) tăng độ phân giải. Dùng trong "
        "cảm biến áp điện (piezoelectric) và đo điện tích bề mặt (Kelvin probe)."))

    b.append(h2("44.3 Ứng dụng", "Applications"))
    b.append(p(
        "Đo điện tích gắn liền với: (1) <b>cảm biến áp điện</b> — lực/gia tốc tạo điện tích Q = d·F (d là "
        "hằng số áp điện); (2) <b>quang điện</b> — đếm electron sinh ra; (3) <b>bức xạ/hạt</b> — detector "
        "tích điện tích do hạt gây ra; (4) <b>điện tích bề mặt</b> (Kelvin probe) đo thế công tác (work "
        "function); (5) <b>định lượng Coulometry</b> trong hóa học — Q = n·F (F = hằng số Faraday) cho biết "
        "số mol phản ứng."))

    b.append(h2("44.4 Thông số", "Specifications"))
    b.append(table(
        ["Phương pháp", "Dải", "Độ nhạy", "Ghi chú"],
        [["Electrometer hồi tiếp", "10⁻¹⁶ – 10⁻⁶ C", "10⁻¹⁶ C", "Chuẩn, cách ly tốt"],
         ["qV / dither", "10⁻¹² – 10⁻⁶ C", "10⁻¹³ C", "Cảm biến áp điện"],
         ["Coulometry", "mC – C", "µC", "Hóa học/định lượng"],
         ["Tụ chuẩn", "pC – µC", "tùy C_f", "Cần leakage thấp"]],
        "Bảng 44.1 · Các phương pháp đo điện tích."))

    b.append(h2("Tóm tắt", "Summary"))
    b.append(p(
        "Điện tích Q = ∫i dt = C·V. Electrometer tụ hồi tiếp cho V_out = −Q_in/C_f với độ nhạy 10⁻¹⁶ C nhờ "
        "đầu vào ảo địa và che chắn. Phương pháp qV chuyển Q sang tụ chuẩn để đo điện áp. Ứng dụng: cảm biến "
        "áp điện (Q = d·F), quang điện, detector bức xạ, Kelvin probe và Coulometry (Q = nF)."))
    b.append('<div class="chapter-nav">'
             '<a href="%s"><span class="k">← Mục lục</span>Sổ tay</a>'
             '<a href="%s" style="text-align:right;"><span class="k">Mục lục →</span>Sổ tay</a></div>'
             % (C.BASE_VI, C.BASE_VI))
    return "".join(b)


def body_en():
    b = []
    b.append(p(
        "Companion to the Vietnamese translation of Chapter 44. Equations and table of the source are "
        "reproduced below; the prose is not repeated."))
    b.append(p(
        "Charge Q = ∫ i dt = C·V (coulomb; elementary charge e ≈ 1.602×10⁻¹⁹ C). Because charges of interest "
        "(pC–nC) easily leak through insulation resistance and pick up noise, measurement needs very high-input-"
        "impedance electrometers, shielding and guarding. The feedback electrometer integrates Q_in on a "
        "feedback capacitor C_f giving V_out = −Q_in/C_f; the virtual ground keeps leakage negligible, reaching "
        "10⁻¹⁵–10⁻¹⁶ C sensitivity — the standard for tiny currents and radiation charge. The charge–voltage "
        "(qV) method transfers unknown Q from sample capacitor C_x to a standard C_f and reads V_f (Q = C_f·V_f); "
        "dithering repeats to improve resolution (piezoelectric sensors). Applications: piezoelectric Q = d·F; "
        "photoelectric/radiation charge counting; Kelvin-probe surface charge (work function); coulometry where "
        "Q = nF (Faraday constant) gives moles reacted."))
    b.append(table(
        ["Method", "Range", "Sensitivity", "Note"],
        [["Feedback electrometer", "10⁻¹⁶ – 10⁻⁶ C", "10⁻¹⁶ C", "Standard, isolated"],
         ["qV / dither", "10⁻¹² – 10⁻⁶ C", "10⁻¹³ C", "Piezoelectric"],
         ["Coulometry", "mC – C", "µC", "Chemistry/quant."],
         ["Std capacitor", "pC – µC", "depends", "Low leakage needed"]],
        "Table 44.1 · Charge-measurement methods."))
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
