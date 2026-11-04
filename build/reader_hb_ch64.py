# -*- coding: utf-8 -*-
"""Handbook Chapter 64 — Vision and Image Sensors (Cảm biến thị giác và hình ảnh).
Run:  python build/reader_hb_ch64.py
"""
import os
import hb_common as C
from hb_common import p, h2, h3, eq, table

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSLUG = "ch64-vision-and-image-sensors"
CH_NO = 64
TITLE_EN = "Vision and Image Sensors"
TITLE_VI = "Cảm biến thị giác và hình ảnh"
BYLINE = "John G. Webster (chủ biên) · CRC Press, 1999"
FIGS = {}


def body_vi():
    b = []
    b.append(p(
        "Cảm biến hình ảnh (CCD, CMOS) chuyển đổi ánh sáng thành mảng điện tích/điện áp. Mỗi <b>pixel</b> có "
        "<b>sức chứa đầy</b> (full well, e⁻), <b>hiệu suất lượng tử</b> (QE = electron sinh/photon tới), dòng tối "
        "(dark current, e⁻/s) và <b>nhiễu đọc</b> (read noise, e⁻). Chất lượng ảnh quyết định bởi SNR:"))
    b.append(eq("SNR = S / √(S + N_dark + N_read²)   (S: tín hiệu, e⁻)"))
    b.append(p(
        "Dải động = full well / read noise, tính theo stop (log₂)."))

    b.append(h2("64.1 CCD và CMOS", "CCD and CMOS"))
    b.append(p(
        "<b>CCD</b> chuyển điện tích từ pixel qua thanh ghi tới một đầu đọc — đồng nhất, nhiễu thấp, QE cao "
        "(> 90% với CCD back-illuminated), dùng trong khoa học, thiên văn, y khoa. <b>CMOS</b> có khuếch đại và "
        "ADC ngay tại mỗi pixel — nhanh, điện năng thấp, tích hợp, chủ đạo trong máy ảnh/điện thoại, thị giác "
        "máy (machine vision) và ô tô. Nhược điểm CMOS: noise cố định theo mẫu (FPN) lớn hơn, phải hiệu chỉnh."))

    b.append(h2("64.2 Các đại lượng đo", "Measured Quantities"))
    b.append(p(
        "<b>Hiệu suất lượng tử</b> (QE): đo bằng nguồn sáng đã hiệu chuẩn, đếm photon. <b>Dòng tối</b>: đo khi "
        "che kín, theo thời gian và nhiệt độ (tăng gấp đôi mỗi ~6–8 °C). <b>Nhiễu đọc</b>: đo từ hai ảnh chiếu "
        "sáng không (phương pháp photon transfer). <b>MTF</b> (modulation transfer function): đo đáp ứng không "
        "gian của cảm biến qua vạch/mép. <b>FPN</b>: sai lệch giữa các pixel, hiệu chỉnh bằng bản đen/trắng."))

    b.append(h2("64.3 Ứng dụng", "Applications"))
    b.append(p(
        "Máy ảnh số, camera giám sát, thị giác máy công nghiệp (kiểm tra sản phẩm), viễn thám, kính hiển vi và "
        "thiên văn (CCD khoa học), camera ô tô và y khoa (nội soi, X-quang số)."))

    b.append(h2("64.4 Thông số", "Specifications"))
    b.append(table(
        ["Đại lượng", "Định nghĩa", "Điển hình"],
        [["Full well", "e⁻ chứa tối đa mỗi pixel", "10 000 – 200 000 e⁻"],
         ["Read noise", "Nhiễu đọc một lần", "1–10 e⁻"],
         ["Dark current", "e⁻/s ở 25 °C", "0,001–10 e⁻/s/pixel"],
         ["QE tối đa", "Photon→electron", "40%–95%"],
         ["Dải động", "Full well / read noise", "60–90 dB (10–15 stop)"],
         ["Tốc độ", "Khung hình/giây", "30 fps – hàng nghìn fps"]],
        "Bảng 64.1 · Đặc tính cảm biến hình ảnh."))

    b.append(h2("Tóm tắt", "Summary"))
    b.append(p(
        "Cảm biến CCD/CMOS: full well, QE, dark current, read noise, SNR = S/√(S+N_dark+N_read²), dải động = "
        "full well/read noise. CCD: nhiễu thấp, QE cao, dùng khoa học. CMOS: nhanh, thấp điện năng, dùng chủ "
        "đạo, nhưng có FPN. Đo QE, dark, read noise, MTF và FPN bằng nguồn chuẩn và photon transfer."))
    b.append('<div class="chapter-nav">'
             '<a href="%s"><span class="k">← Mục lục</span>Sổ tay</a>'
             '<a href="%s" style="text-align:right;"><span class="k">Mục lục →</span>Sổ tay</a></div>'
             % (C.BASE_VI, C.BASE_VI))
    return "".join(b)


def body_en():
    b = []
    b.append(p(
        "Companion to the Vietnamese translation of Chapter 64. Equations and table of the source are "
        "reproduced below; the prose is not repeated."))
    b.append(p(
        "Image sensors (CCD, CMOS) convert light into a charge/voltage array. Per pixel: full well capacity "
        "(e⁻), quantum efficiency QE = electrons/photon, dark current (e⁻/s), read noise (e⁻); image quality is "
        "set by SNR = S/√(S + N_dark + N_read²) and dynamic range = full well / read noise (stops = log₂). CCDs "
        "shift charge to one readout node — uniform, low noise, QE > 90% (back-illuminated) — used in science, "
        "astronomy and medical imaging. CMOS integrates an amplifier and ADC per pixel — fast, low power, "
        "integrable — dominant in cameras, machine vision and automotive, but with more fixed-pattern noise "
        "(FPN) requiring calibration. Measured quantities: QE with calibrated sources, dark current vs time/"
        "temperature (doubles every ~6–8 °C), read noise via the photon-transfer method (two dark frames), MTF "
        "(spatial response via slanted edge), FPN via dark/flat calibration. Applications: digital cameras, "
        "surveillance, industrial inspection, remote sensing, microscopy, astronomy, automotive and medical."))
    b.append(table(
        ["Quantity", "Definition", "Typical"],
        [["Full well", "Max e⁻ per pixel", "10 000 – 200 000 e⁻"],
         ["Read noise", "Noise per read", "1–10 e⁻"],
         ["Dark current", "e⁻/s at 25 °C", "0.001–10 e⁻/s/px"],
         ["Peak QE", "Photon→electron", "40%–95%"],
         ["Dynamic range", "Full well / read", "60–90 dB"],
         ["Speed", "Frames/s", "30 – thousands fps"]],
        "Table 64.1 · Image-sensor characteristics."))
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
