# -*- coding: utf-8 -*-
"""Handbook Chapter 47 — Electric Field Strength (Cường độ điện trường).
Run:  python build/reader_hb_ch47.py
"""
import os
import hb_common as C
from hb_common import p, h2, h3, eq, table

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSLUG = "ch47-electric-field-strength"
CH_NO = 47
TITLE_EN = "Electric Field Strength"
TITLE_VI = "Cường độ điện trường"
BYLINE = "John G. Webster (chủ biên) · CRC Press, 1999"
FIGS = {}


def body_vi():
    b = []
    b.append(p(
        "<b>Cường độ điện trường</b> (electric field strength) E có đơn vị vôn trên mét (V/m). Nó mô tả lực "
        "tác dụng lên một điện tích thử: F = q·E. Đo E quan trọng trong an toàn điện (tiếp xúc gần đường dây "
        "cao áp), điện khí quyển, điện từ trường (EMF) và thiết kế cảm biến."))
    b.append(p(
        "Dải đo trải từ vài mV/m (trường nền) đến hàng MV/m (gần sét, thiết bị cao áp). Đo chính xác khó vì "
        "điện trường bị nhiễu bởi vật dẫn xung quanh và do bản thân đầu dò làm biến dạng trường."))

    b.append(h2("47.1 Cảm biến dipole và cuộn dây nhỏ", "Dipole and Small-Loop Sensors"))
    b.append(p(
        "Một dipole ngắn (hai điện cực cách nhau l) trong trường E sinh điện áp V = E·l·cosθ (θ là góc giữa "
        "dipole và E). Đo V bằng vôn kế trở cao hoặc bộ khuếch đại. Tương tự, một vòng dây nhỏ đo thành phần "
        "từ trường của sóng điện từ. Các cảm biến này dùng trong máy đo trường EM (field strength meter) cầm "
        "tay và trạm quan trắc."))

    b.append(h2("47.2 Field mill (cối xay từ trường)", "Field Mill"))
    b.append(p(
        "Để đo điện trường tĩnh (DC, ví dụ gần đường dây cao áp), dùng <b>field mill</b>: một đĩa quay có các "
        "sector kim loại xen kẽ che/mở các điện cực cố định. Khi quay, điện tích cảm ứng trên điện cực bị điều "
        "chế thành xung AC có biên độ tỉ lệ với E. Bộ lọc đồng bộ (lock-in) tách tín hiệu, cho phép đo E tĩnh "
        "ổn định mà không cần vật dẫn tiếp xúc."))

    b.append(h2("47.3 Phương pháp quang học (Kerr, Pockels)", "Optical: Kerr and Pockels"))
    b.append(p(
        "Hiệu ứng Kerr (chất lỏng/ khí không đối xứng) và Pockels (tinh thể áp điện) làm thay đổi chiết suất "
        "kép tỉ lệ với E² hoặc E. Chiếu sáng qua môi trường và đo sự quay phân cực/trễ pha suy ra E. Ưu điểm: "
        "cảm biến không kim loại, cách ly hoàn toàn, đo được trường rất lớn (MV/m) trong máy biến áp, cầu dao."))

    b.append(h2("47.4 Thông số", "Specifications"))
    b.append(table(
        ["Phương pháp", "Dải", "Loại trường", "Ưu điểm"],
        [["Dipole ngắn", "mV/m – kV/m", "AC", "Đơn giản, rẻ"],
         ["Field mill", "V/m – kV/m", "DC + AC", "Đo tĩnh, không tiếp xúc"],
         ["Kerr / Pockels", "kV/m – MV/m", "DC + AC", "Cách ly, trường lớn"],
         ["Vòng dây nhỏ", "µT – mT", "Từ trường AC", "Đo thành phần B"]],
        "Bảng 47.1 · Các phương pháp đo cường độ điện trường."))

    b.append(h2("Tóm tắt", "Summary"))
    b.append(p(
        "Cường độ điện trường E (V/m), F = qE. Dipole ngắn cho V = E·l·cosθ; field mill điều chế điện tích "
        "cảm ứng thành AC để đo trường tĩnh không tiếp xúc; hiệu ứng Kerr/Pockels đo trường lớn cách ly qua sự "
        "thay đổi chiết suất. Dải từ mV/m đến MV/m; nhiễu do vật dẫn xung quanh là sai số chủ yếu."))
    b.append('<div class="chapter-nav">'
             '<a href="%s"><span class="k">← Mục lục</span>Sổ tay</a>'
             '<a href="%s" style="text-align:right;"><span class="k">Mục lục →</span>Sổ tay</a></div>'
             % (C.BASE_VI, C.BASE_VI))
    return "".join(b)


def body_en():
    b = []
    b.append(p(
        "Companion to the Vietnamese translation of Chapter 47. Equations and table of the source are "
        "reproduced below; the prose is not repeated."))
    b.append(p(
        "Electric field strength E (V/m) is the force per unit charge, F = qE. It spans mV/m (ambient) to "
        "MV/m (lightning, HV equipment); the probe itself distorts the field, and nearby conductors add error. "
        "A short dipole of length l in field E develops V = E·l·cosθ (θ between dipole and E), read by a "
        "high-impedance voltmeter; a small loop senses the magnetic component of an EM wave. For static (DC) "
        "fields — e.g. near HV lines — a field mill rotates shielded sectors over fixed electrodes, modulating "
        "the induced charge into an AC whose amplitude ∝ E; a lock-in amplifier extracts it, giving a contactless "
        "DC measurement. Optical methods use the Kerr (liquids/gases) or Pockels (piezo-optic crystals) effect: "
        "the field changes birefringence ∝ E² or E, read via polarization rotation/retardation — fully isolated, "
        "metal-free sensors for MV/m fields in breakers and transformers."))
    b.append(table(
        ["Method", "Range", "Field type", "Advantage"],
        [["Short dipole", "mV/m–kV/m", "AC", "Simple, cheap"],
         ["Field mill", "V/m–kV/m", "DC+AC", "Static, contactless"],
         ["Kerr/Pockels", "kV/m–MV/m", "DC+AC", "Isolated, large field"],
         ["Small loop", "µT–mT", "AC magnetic", "Senses B"]],
        "Table 47.1 · Electric-field measurement methods."))
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
