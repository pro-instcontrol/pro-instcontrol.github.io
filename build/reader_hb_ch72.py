# -*- coding: utf-8 -*-
"""Handbook Chapter 72 — Humidity and Moisture Measurement (Đo độ ẩm).
Run:  python build/reader_hb_ch72.py
"""
import os
import hb_common as C
from hb_common import p, h2, h3, eq, table

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSLUG = "ch72-humidity-and-moisture-measurement"
CH_NO = 72
TITLE_EN = "Humidity and Moisture Measurement"
TITLE_VI = "Đo độ ẩm"
BYLINE = "John G. Webster (chủ biên) · CRC Press, 1999"
FIGS = {}


def body_vi():
    b = []
    b.append(p(
        "<b>Độ ẩm</b> mô tả lượng hơi nước trong không khí/khí: <b>độ ẩm tuyệt đối</b> (g/m³), <b>độ ẩm tương "
        "đối</b> RH = (p_H₂O/p_sat)·100 (%), và <b>nhiệt độ điểm sương</b> (dew point). Đo độ ẩm quan trọng "
        "trong HVAC, bảo quản, phòng sạch, thực phẩm và khí tượng."))
    b.append(p(
        "Đo ẩm trong chất rắn/bột gọi là <b>đo độ ẩm vật liệu</b> (moisture content), biểu diễn % khối lượng "
        "ướt hoặc khô."))

    b.append(h2("72.1 Cảm biến điện dung polymer", "Capacitive Polymer Sensors"))
    b.append(p(
        "Loại phổ biến nhất: một tụ có lớp điện môi polymer hấp thụ nước, điện dung thay đổi theo RH. Ưu điểm: "
        "nhỏ, rẻ, tuyến tính 0–100% RH, nhiệt độ −40…+180 °C, độ chính xác ±1%–3% RH. Nhược: trôi theo thời "
        "gian, bị nhiễm hoá học."))

    b.append(h2("72.2 Gương làm lạnh (chilled mirror)", "Chilled-Mirror Dew Point"))
    b.append(p(
        "Phương pháp chuẩn chính xác nhất: làm lạnh một gương cho đến khi xuất hiện sương, nhiệt độ đó chính là "
        "điểm sương. Máy dùng LED phát hiện sương và vòng điều khiển PID giữ trạng thái sương mỏng đều. Độ chính "
        "xác ±0,1–0,2 °C điểm sương, dùng hiệu chuẩn các cảm biến khác và khí tượng chuẩn."))

    b.append(h2("72.3 Các phương pháp khác", "Other Methods"))
    b.append(p(
        "<b>Psychrometer</b> (khô/ướt): hai nhiệt kế, một bọc ướt; chênh lệch nhiệt độ cho RH qua bảng/ phương "
        "trình. <b>Điện trở</b> (resistive): vật liệu thay đổi trở theo ẩm — rẻ. <b>NIR/IR hấp thụ</b> và "
        "<b>microwave</b> đo ẩm vật liệu không tiếp xúc (giấy, ngũ cốc, bê tông). <b>Aluminium oxide</b> cho "
        "độ ẩm rất thấp (ppm) trong khí công nghiệp."))

    b.append(h2("72.4 Thông số", "Specifications"))
    b.append(table(
        ["Phương pháp", "Dải", "Độ chính xác", "Ứng dụng"],
        [["Điện dung polymer", "0–100% RH", "±1%–3% RH", "HVAC, chung"],
         ["Gương làm lạnh", "−80…+60 °C dew", "±0,1–0,2 °C", "Chuẩn, khí tượng"],
         ["Psychrometer", "10–100% RH", "±2%–5% RH", "Cổ điển, ngoài trời"],
         ["Al₂O₃", "ppm–%", "±5%", "Khí công nghiệp"],
         ["NIR/microwave (rắn)", "0–40% ẩm", "±0,1%–0,5%", "Giấy, ngũ cốc"]],
        "Bảng 72.1 · Các phương pháp đo độ ẩm."))

    b.append(h2("Tóm tắt", "Summary"))
    b.append(p(
        "RH = p_H₂O/p_sat·100%. Cảm biến polymer điện dung (±1–3% RH) là phổ biến; gương làm lạnh cho điểm sương "
        "±0,1–0,2 °C (chuẩn); psychrometer khô/ướt cổ điển; Al₂O₃ cho ppm; NIR/microwave đo ẩm vật liệu không "
        "tiếp xúc."))
    b.append('<div class="chapter-nav">'
             '<a href="%s"><span class="k">← Mục lục</span>Sổ tay</a>'
             '<a href="%s" style="text-align:right;"><span class="k">Mục lục →</span>Sổ tay</a></div>'
             % (C.BASE_VI, C.BASE_VI))
    return "".join(b)


def body_en():
    b = []
    b.append(p(
        "Companion to the Vietnamese translation of Chapter 72. The table of the source is reproduced below; "
        "the prose is not repeated."))
    b.append(p(
        "Humidity describes water vapor: absolute (g/m³), relative RH = (p_H₂O/p_sat)·100 (%), and dew point. "
        "Moisture content in solids is % wet or dry basis. Capacitive polymer sensors (a water-absorbing polymer "
        "dielectric) are the most common: small, cheap, linear 0–100% RH, −40…+180 °C, ±1%–3% RH, but drift and "
        "chemical contamination affect them. The chilled-mirror dew-point meter is the most accurate: cool a "
        "mirror until condensation forms; that temperature is the dew point (±0.1–0.2 °C, used to calibrate "
        "other sensors). Psychrometers (dry/wet bulbs) derive RH from the temperature difference; resistive "
        "sensors are cheap; NIR/IR absorption and microwave measure material moisture contactlessly (paper, "
        "grain, concrete); aluminium-oxide sensors reach ppm levels in industrial gases."))
    b.append(table(
        ["Method", "Range", "Accuracy", "Use"],
        [["Capacitive polymer", "0–100% RH", "±1%–3% RH", "HVAC, general"],
         ["Chilled mirror", "−80…+60 °C dew", "±0.1–0.2 °C", "Standard, met."],
         ["Psychrometer", "10–100% RH", "±2%–5% RH", "Classic, outdoor"],
         ["Al₂O₃", "ppm–%", "±5%", "Industrial gas"],
         ["NIR/microwave (solid)", "0–40% moist", "±0.1%–0.5%", "Paper, grain"]],
        "Table 72.1 · Humidity/moisture methods."))
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
