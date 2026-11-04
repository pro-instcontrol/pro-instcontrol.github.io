# -*- coding: utf-8 -*-
"""Handbook Chapter 75 — Blood Pressure Measurement (Đo huyết áp).
Run:  python build/reader_hb_ch75.py
"""
import os
import hb_common as C
from hb_common import p, h2, h3, eq, table

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSLUG = "ch75-blood-pressure-measurement"
CH_NO = 75
TITLE_EN = "Blood Pressure Measurement"
TITLE_VI = "Đo huyết áp"
BYLINE = "John G. Webster (chủ biên) · CRC Press, 1999"
FIGS = {}


def body_vi():
    b = []
    b.append(p(
        "Huyết áp được biểu thị bằng hai giá trị: <b>tâm thu</b> (systolic) và <b>tâm trương</b> (diastolic), "
        "đơn vị mmHg (1 mmHg = 133,3 Pa). Bình thường ~120/80 mmHg. Đo gồm phương pháp <b>không xâm nhập</b> "
        "(cuff) và <b>xâm nhập</b> (catheter)."))

    b.append(h2("75.1 Phương pháp băng quấn (cuff)", "Cuff-Based Methods"))
    b.append(p(
        "<b>Korotkoff/auscultatory</b>: bơm cuff vượt tâm thu, xả từ từ; nghe tiếng Korotkoff bằng ống nghe — "
        "tiếng xuất hiện = tâm thu, biến mất = tâm trương. Đây là chuẩn lâm sàng. <b>Oscillometric</b>: đo dao "
        "động áp trong cuff bằng cảm biến áp; biên độ dao động cực đại ứng áp trung bình (MAP), và thuật toán suy "
        "ra tâm thu/tâm trương — nguyên lý của máy đo tự động và monitor bệnh viện."))

    b.append(h2("75.2 Đo xâm nhập", "Invasive Measurement"))
    b.append(p(
        "Thông (catheter) nối với <b>cảm biến áp</b> (strain-gauge, áp trở) đặt trong động mạch; đo sóng áp liên "
        "tục, chính xác nhất, dùng ICU và phẫu thuật. Cần hệ truyền đầy nước (fluid-filled) hoặc cảm biến đầu "
        "sợi (tip transducer), hiệu chuẩn bằng mức tham chiếu tim (phlebostatic axis)."))

    b.append(h2("75.3 Các phương pháp khác", "Other Methods"))
    b.append(p(
        "<b>Doppler siêu âm</b>: đo tiếng phun máu qua động mạch dưới cuff — dùng trẻ em, sốc. <b>Tonometry áp</b> "
        "(áp lên động mạch nông) theo dõi liên tục không cuff. <b>Applanation tonometry</b> đo huyết áp trung tâm. "
        "Huyết áp tâm của mắt (tonometry mắt) đo bằng Goldmann áp phẳng."))

    b.append(h2("75.4 Thông số", "Specifications"))
    b.append(table(
        ["Phương pháp", "Độ chính xác", "Đặc điểm"],
        [["Korotkoff (thủ công)", "±2–3 mmHg", "Chuẩn lâm sàng"],
         ["Oscillometric (tự động)", "±3–5 mmHg", "Máy đo, monitor"],
         ["Xâm nhập (catheter)", "±1–2 mmHg", "Liên tục, ICU"],
         ["Doppler", "±5 mmHg", "Trẻ em, sốc"],
         ["Tonometry", "±5 mmHg", "Liên tục không cuff"]],
        "Bảng 75.1 · Các phương pháp đo huyết áp."))

    b.append(h2("Tóm tắt", "Summary"))
    b.append(p(
        "Huyết áp mmHg (1 mmHg = 133,3 Pa). Cuff: Korotkoff (chuẩn lâm sàng) hoặc oscillometric (biên độ dao động "
        "→ MAP → suy thu/trương) cho máy tự động. Xâm nhập: catheter + strain-gauge, chính xác nhất, ICU. Doppler "
        "cho trẻ em/sốc; tonometry theo dõi liên tục."))
    b.append('<div class="chapter-nav">'
             '<a href="%s"><span class="k">← Mục lục</span>Sổ tay</a>'
             '<a href="%s" style="text-align:right;"><span class="k">Mục lục →</span>Sổ tay</a></div>'
             % (C.BASE_VI, C.BASE_VI))
    return "".join(b)


def body_en():
    b = []
    b.append(p(
        "Companion to the Vietnamese translation of Chapter 75. The table of the source is reproduced below; "
        "the prose is not repeated."))
    b.append(p(
        "Blood pressure is reported as systolic/diastolic in mmHg (1 mmHg = 133.3 Pa); normal ≈ 120/80. "
        "Noninvasive cuff methods: Korotkoff/auscultatory (inflate above systolic, deflate slowly; appearance of "
        "Korotkoff sounds = systolic, disappearance = diastolic) — the clinical standard; oscillometric measures "
        "cuff-pressure oscillations with a pressure sensor — maximum oscillation amplitude corresponds to mean "
        "arterial pressure (MAP) and algorithms derive systolic/diastolic; the basis of automated home devices "
        "and bedside monitors. Invasive measurement uses an arterial catheter coupled to a strain-gauge pressure "
        "transducer (fluid-filled or catheter-tip) for continuous, most-accurate waveform in ICU/surgery, "
        "referenced to the phlebostatic axis. Doppler ultrasound (children, shock), arterial tonometry "
        "(cuffless continuous), and applanation tonometry for central pressure are alternatives."))
    b.append(table(
        ["Method", "Accuracy", "Notes"],
        [["Korotkoff (manual)", "±2–3 mmHg", "Clinical standard"],
         ["Oscillometric", "±3–5 mmHg", "Automated, monitors"],
         ["Invasive (catheter)", "±1–2 mmHg", "Continuous, ICU"],
         ["Doppler", "±5 mmHg", "Children, shock"],
         ["Tonometry", "±5 mmHg", "Cuffless continuous"]],
        "Table 75.1 · Blood-pressure methods."))
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
