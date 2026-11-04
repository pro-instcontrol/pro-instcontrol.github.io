# -*- coding: utf-8 -*-
"""Handbook Chapter 42 — Energy Measurement (Đo điện năng).
Run:  python build/reader_hb_ch42.py
"""
import os
import hb_common as C
from hb_common import p, h2, h3, eq, table

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSLUG = "ch42-energy-measurement"
CH_NO = 42
TITLE_EN = "Energy Measurement"
TITLE_VI = "Đo điện năng"
BYLINE = "John G. Webster (chủ biên) · CRC Press, 1999"
FIGS = {}


def body_vi():
    b = []
    b.append(p(
        "Điện năng (energy) là tích phân của công suất theo thời gian: E = ∫ p(t) dt. Đơn vị là watt-giờ "
        "(Wh), kilôwatt-giờ (kWh) và megawatt-giờ (MWh) — 1 kWh = 3,6·10⁶ J. Đo điện năng là nền tảng của "
        "hóa đơn tiền điện, kiểm toán năng lượng và quản lý tải."))
    b.append(p(
        "Với công suất không đổi, E = P·t. Với AC, E = ∫ V_rms(t)·I_rms(t)·cosφ(t) dt — do đó công tơ phải "
        "nhân tức thời v(t)·i(t) rồi tích phân theo thời gian."))

    b.append(h2("42.1 Công tơ đĩa quay (cơ điện)", "Induction (Disk) Meter"))
    b.append(p(
        "Công tơ điện năng kiểu cảm ứng (kWh meter) dùng đĩa nhôm quay trong từ trường sinh bởi cuộn dòng "
        "và cuộn áp. Mômen quay tỉ lệ với công suất tức thời trung bình (P), và tốc độ quay tỉ lệ với P. "
        "Một bộ đếm cơ học đếm số vòng quay; hằng số công tơ (rev/kWh) quy đổi vòng quay sang năng lượng. "
        "Loại này bền, rẻ, nhưng chỉ đo được năng lượng tác dụng và chịu ảnh hưởng nhiệt độ, từ trường ngoài."))

    b.append(h2("42.2 Công tơ điện tử và công tơ thông minh", "Electronic and Smart Meters"))
    b.append(p(
        "Công tơ điện tử nhân tức thời v(t)·i(t) bằng mạch analog hoặc ADC, tích phân số (đếm xung tỉ lệ "
        "năng lượng) để ra giá trị kWh. Vi mạch chuyên dụng (họ ADE7xxx) tích hợp bộ nhân, ADC đa kênh, "
        "bộ xử lý tính P, Q, S, năng lượng tác dụng/phản kháng và hệ số công suất."))
    b.append(p(
        "<b>Công tơ thông minh</b> (smart meter) thêm giao tiếp (PLC, RF, Zigbee) để truyền dữ liệu hai "
        "chiều, đo theo phiên (time-of-use), phát hiện mất điện và hỗ trợ lưới thông minh (smart grid). "
        "Chúng đo được cả năng lượng có sóng hài nhờ nhân tức thời."))

    b.append(h2("42.3 Đo năng lượng ba pha", "Three-Phase Energy"))
    b.append(p(
        "Năng lượng ba pha tổng cộng là tổng năng lượng các pha. Công tơ ba pha dùng hai hoặc ba phần tử "
        "đo (tương ứng hai/ba watt kế), tích phân tổng hợp để ra kWh tổng ngay cả khi tải không cân bằng. "
        "Sai số chuẩn công bố thường ở mức 0,2%–2% tùy cấp chính xác (class 0,2 … class 2)."))

    b.append(h2("42.4 Thông số", "Specifications"))
    b.append(table(
        ["Thông số", "Công tơ cảm ứng", "Công tơ điện tử"],
        [["Độ chính xác", "1%–2% (class 1–2)", "0,2%–0,5% (class 0,2–0,5)"],
         ["Đo hài", "Không", "Có (nhân tức thời)"],
         ["Giao tiếp", "Cơ học (đĩa)", "PLC/RF/Zigbee"],
         ["Năng lượng phản kháng", "Hạn chế", "Đầy đủ (kvarh)"],
         ["Tuổi thọ", "Rất cao", "Cao (điện tử)"]],
        "Bảng 42.1 · So sánh công tơ điện năng."))

    b.append(h2("Tóm tắt", "Summary"))
    b.append(p(
        "Điện năng E = ∫p(t)dt, đơn vị kWh (1 kWh = 3,6 MJ). Công tơ cảm ứng dùng đĩa nhôm quay với tốc độ "
        "∝ P, đếm vòng qua hằng số rev/kWh. Công tơ điện tử nhân tức thời v·i rồi tích phân số, đo đúng cả "
        "năng lượng có hài; công tơ thông minh thêm giao tiếp hai chiều cho lưới thông minh. Ba pha tổng hợp "
        "từ hai/ba phần tử đo."))
    b.append('<div class="chapter-nav">'
             '<a href="%s"><span class="k">← Mục lục</span>Sổ tay</a>'
             '<a href="%s" style="text-align:right;"><span class="k">Mục lục →</span>Sổ tay</a></div>'
             % (C.BASE_VI, C.BASE_VI))
    return "".join(b)


def body_en():
    b = []
    b.append(p(
        "Companion to the Vietnamese translation of Chapter 42. The table of the source is reproduced "
        "below; the prose is not repeated."))
    b.append(p(
        "Energy E = ∫ p(t)dt, in watt-hours (1 kWh = 3.6 MJ). An induction (disk) meter spins an aluminum "
        "disk at a speed ∝ P; a mechanical counter counts revolutions and a meter constant (rev/kWh) converts "
        "them to energy — robust and cheap, but records only real energy and is affected by temperature and "
        "stray fields. Electronic meters multiply v(t)·i(t) instantaneously and integrate digitally to a pulse "
        "count ∝ energy; ADE7xxx-class ICs compute P, Q, S, active/reactive energy and PF. Smart meters add "
        "two-way communication (PLC/RF) for time-of-use billing and grid monitoring, and measure harmonic "
        "energy via the instantaneous multiplier. Three-phase energy totals the phases via two/three "
        "measurement elements; accuracy classes run 0.2%–2%."))
    b.append(table(
        ["Parameter", "Induction meter", "Electronic meter"],
        [["Accuracy", "1%–2% (class 1–2)", "0.2%–0.5% (class 0.2–0.5)"],
         ["Harmonics", "No", "Yes (instant. mult.)"],
         ["Comms", "Mechanical", "PLC/RF/Zigbee"],
         ["Reactive energy", "Limited", "Full (kvarh)"],
         ["Life", "Very high", "High (electronic)"]],
        "Table 42.1 · Energy-meter comparison."))
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
