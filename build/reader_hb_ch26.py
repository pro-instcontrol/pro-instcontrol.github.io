# -*- coding: utf-8 -*-
"""Handbook Chapter 26 — Pressure and Sound Measurement
(K. H.-L. Chau — Analog Devices; R. Goehner, E. Drubetsky, H. M. Brady,
W. H. Bayles Jr. — The Fredericks Company; P. C. Pedersen — WPI).

Writes the full Vietnamese translation and the English companion.
Run:  python build/reader_hb_ch26.py
"""
import os

import hb26fig as F
from reader_handbook import SLUG, head, header, footer

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSLUG = "ch26-pressure-and-sound-measurement"
TITLE_EN = "Pressure and Sound Measurement"
TITLE_VI = "Đo áp suất và âm thanh"
BYLINE = ("K. H.-L. Chau (Analog Devices) · R. Goehner · E. Drubetsky · "
          "H. M. Brady · W. H. Bayles Jr. (The Fredericks Company) · "
          "P. C. Pedersen (Worcester Polytechnic Institute)")
BASE_EN = "/books/read/%s/" % SLUG
BASE_VI = "/vi/books/read/%s/" % SLUG
PREV_EN = "ch25-tactile-sensing"
PREV_VI = "ch25-tactile-sensing"
PREV_T_EN = "Tactile Sensing"
PREV_T_VI = "Cảm biến xúc giác"


def fig(num, key, lang="vi"):
    svg, cap_vi, cap_en, _av, _ae = key
    cap = cap_vi if lang == "vi" else cap_en
    return ('<figure class="figure" id="fig-26-%d">%s<figcaption class="figcap">%s</figcaption></figure>'
            % (num, svg, cap))


def p(t):
    return "<p>%s</p>" % t


def h2(t, en=""):
    return '<h2>%s%s</h2>' % (t, (' <span class="en">%s</span>' % en) if en else "")


def h3(t, en=""):
    return '<h3>%s%s</h3>' % (t, (' <span class="en">%s</span>' % en) if en else "")


def eq(body, num=""):
    if not num:
        return '<div class="eq">%s</div>' % body
    return '<div class="eq"><span class="n">(%s)</span>%s</div>' % (num, body)


def note(t):
    return '<div class="note">%s</div>' % t


def wl(items):
    return ('<p style="font-size:.92rem;color:#333;line-height:1.8;margin:-.3rem 0 1.2rem">'
            + "<br>".join(items) + "</p>")


def ol(items):
    return ('<ol style="margin:-.3rem 0 1.2rem 1.3rem;line-height:1.85;font-size:.95rem">'
            + "".join("<li>%s</li>" % i for i in items) + "</ol>")


def table(hd, rows, cap):
    body = "".join("<tr>%s</tr>" % "".join("<td>%s</td>" % c for c in r) for r in rows)
    return ('<div class="table-wrap"><table class="tbl"><thead><tr>%s</tr></thead><tbody>%s</tbody></table></div>'
            '<p style="font-size:.84rem;color:#888;font-style:italic">%s</p>'
            % ("".join("<th>%s</th>" % h for h in hd), body, cap))


# ================================================================ tables data

def _t261(lang):
    if lang == "vi":
        hd = ("Đơn vị", "Pa", "bar", "atm", "Torr", "psi", "mm H₂O")
        cap = ("Bảng 26.1 · Bảng chuyển đổi đơn vị áp suất. Hệ số cho biết 1 đơn vị ở dòng tương ứng "
               "bằng bao nhiêu đơn vị ở cột. (Các giá trị là tiêu chuẩn, làm tròn.)")
    else:
        hd = ("Unit", "Pa", "bar", "atm", "Torr", "psi", "mm H₂O")
        cap = ("Table 26.1 · Pressure unit conversion table. Entry at row U, column V gives how many "
               "units V equal one unit U. (Standard, rounded values.)")
    rows = [
        ["Pa", "1", "1.0×10⁻⁵", "9.869×10⁻⁶", "7.501×10⁻³", "1.450×10⁻⁴", "0.10197"],
        ["bar", "1.0×10⁵", "1", "0.9869", "750.06", "14.504", "1.0197×10⁴"],
        ["atm", "1.01325×10⁵", "1.01325", "1", "760.0", "14.696", "1.0332×10⁴"],
        ["Torr", "133.32", "1.333×10⁻³", "1.316×10⁻³", "1", "1.934×10⁻²", "13.595"],
        ["psi", "6.895×10³", "6.895×10⁻²", "6.805×10⁻²", "51.715", "1", "7.027×10²"],
        ["mm H₂O", "9.80665", "9.807×10⁻⁵", "9.678×10⁻⁵", "7.356×10⁻²", "1.422×10⁻³", "1"],
    ]
    return hd, rows, cap


def _t262(lang):
    if lang == "vi":
        hd = ("Loại cảm biến", "Hãng tiêu biểu", "Ghi chú")
        cap = ("Bảng 26.2 · Một số hãng chế tạo cảm biến áp suất và hệ thống hiệu chuẩn áp suất "
               "(danh sách đại diện; xem văn bản gốc để có địa chỉ đầy đủ).")
        rows = [
            ["Áp kế vi cơ (silicon)", "Analog Devices, Honeywell, Motorola/Sensym, Foxboro", "Công nghệ vi cơ (micromachined)"],
            ["Áp kế điện dung", "Rosemount, Setra Systems, Druck", "Độ chính xác cao, ổn định"],
            ["Áp kế strain-gage liên kết", "Kulite, Endevco, PCB Piezotronics, Entran", "Áp suất động / xung"],
            ["Hệ thống hiệu chuẩn", "Druck, DH Instruments, Fluke / Ruska", "Chuẩn chính/phụ áp suất"],
        ]
    else:
        hd = ("Sensor type", "Representative makers", "Note")
        cap = ("Table 26.2 · Selected companies that make pressure sensors and pressure calibration "
               "systems (representative list; see the source for full addresses).")
        rows = [
            ["Micromachined (silicon)", "Analog Devices, Honeywell, Motorola/Sensym, Foxboro", "Micromachined technology"],
            ["Capacitive", "Rosemount, Setra Systems, Druck", "High accuracy, stable"],
            ["Bonded strain-gage", "Kulite, Endevco, PCB Piezotronics, Entran", "Dynamic / impulse pressure"],
            ["Calibration systems", "Druck, DH Instruments, Fluke / Ruska", "Primary/secondary pressure standards"],
        ]
    return hd, rows, cap


def _t263(lang):
    if lang == "vi":
        hd = ("Thông số", "BaTiO₃", "PZT-5", "PbNb₂O₆", "PVDF")
        cap = ("Bảng 26.3 · Các thông số áp điện quan trọng của vật liệu áp điện thông dụng. "
               "d₃₃ (10⁻¹² m/V), g₃₃ (10⁻³ V·m/N), hệ số ghép k₃₃, k_T, cơ khí Q_m.")
        rows = [
            ["d₃₃", "149", "374", "75", "22"],
            ["g₃₃", "14", "25", "35", "339"],
            ["k₃₃", "0.50", "0.70", "0.38", "k₃₁ = 0.12"],
            ["k_T", "0.38", "0.68", "0.40", "0.11"],
            ["Q_m", "600", "75", "5", "19"],
        ]
    else:
        hd = ("Parameter", "BaTiO₃", "PZT-5", "PbNb₂O₆", "PVDF")
        cap = ("Table 26.3 · Most significant piezoelectric parameters for common piezoelectric "
               "materials. d₃₃ (10⁻¹² m/V), g₃₃ (10⁻³ V·m/N), coupling k₃₃, k_T, mechanical Q_m.")
        rows = [
            ["d₃₃", "149", "374", "75", "22"],
            ["g₃₃", "14", "25", "35", "339"],
            ["k₃₃", "0.50", "0.70", "0.38", "k₃₁ = 0.12"],
            ["k_T", "0.38", "0.68", "0.40", "0.11"],
            ["Q_m", "600", "75", "5", "19"],
        ]
    return hd, rows, cap


def _t264(lang):
    if lang == "vi":
        hd = ("Loại sản phẩm", "Hãng sản xuất")
        cap = ("Bảng 26.4 · Các sản phẩm và hãng sản xuất thiết bị đo siêu âm tiêu biểu.")
        rows = [
            ["Đầu dò siêu âm", "Panametrics; Krautkramer Branson"],
            ["Đo cự ly trong không khí", "Polaroid (Ultrasonics Components Group)"],
            ["Pulser-receiver", "Panametrics; JSR Ultrasonics; Ritec"],
            ["Bộ khuếch đại công suất", "Amplifier Research; Ritec"],
            ["Thiết bị NDE", "Panametrics; Krautkramer Branson"],
            ["Kính hiển vi âm học", "Sonoscan"],
            ["Hình ảnh y tế", "HP; ATL; Diasonics; Siemens Ultrasound"],
            ["Hình ảnh trường âm (Schlieren)", "Optison"],
            ["Hình ảnh trường âm (quang học)", "UltraOptec"],
        ]
    else:
        hd = ("Product type", "Manufacturer")
        cap = ("Table 26.4 · Representative list of ultrasound equipment and manufacturers.")
        rows = [
            ["Ultrasound transducers", "Panametrics; Krautkramer Branson"],
            ["Air range measurement", "Polaroid (Ultrasonics Components Group)"],
            ["Pulser-receivers", "Panametrics; JSR Ultrasonics; Ritec"],
            ["Power amplifiers", "Amplifier Research; Ritec"],
            ["NDE instrumentation", "Panametrics; Krautkramer Branson"],
            ["Acoustic microscopy", "Sonoscan"],
            ["Medical imaging", "HP; ATL; Diasonics; Siemens Ultrasound"],
            ["Schlieren acoustic-field imaging", "Optison"],
            ["Optical acoustic-field imaging", "UltraOptec"],
        ]
    return hd, rows, cap


# ================================================================ Vietnamese

def body_vi():
    b = []
    b.append(p(
        "Chương này trình bày các nguyên lý đo áp suất và đo âm thanh (siêu âm). Phần 26.1 mô tả các "
        "phần tử cảm biến áp suất, các phương pháp phát hiện (điện dung, áp điện trở) và cảm biến áp "
        "suất vi cơ bằng silicon cùng những hạn chế của chúng. Phần 26.2 đề cập đo chân không — từ các "
        "áp kế đọc trực tiếp (thủy ngân, Bourdon, màng) đến các áp kế đọc gián tiếp (dẫn nhiệt, ion hóa, "
        "kéo phân tử, phổ kế khối). Phần 26.3 giới thiệu các tham số cơ bản của siêu âm, lan truyền sóng, "
        "phản xạ/khúc xạ ở giao diện, trường bức xạ của đầu dò, đo suy hao, đầu dò áp điện, Doppler và "
        "các tích phân nhiễu xạ."))

    # -------------------------------------------------------- 26.1
    b.append(h2("26.1 Đo áp suất", "Pressure Measurement"))
    b.append(p(
        "Áp suất được định nghĩa là lực pháp tuyến tác dụng trên một đơn vị diện tích do một chất lưu "
        "(lỏng hoặc khí) gây ra lên bất kỳ bề mặt nào. Áp suất tuyệt đối, áp suất tương đối (gage) và áp "
        "suất chênh lệch thường được ký hiệu lần lượt là psia, psig và psid; trong các hệ đơn vị khác, "
        "sự phân biệt này thường không được chỉ rõ. Một lớp đơn vị khác biểu diễn áp suất qua chiều cao "
        "cột chất lỏng tĩnh, ví dụ milimét thủy ngân ở 0 °C (mm Hg, còn gọi là torr) hay inch nước ở 4 °C."))
    b.append(p(
        "Áp suất p tương ứng với áp suất sinh ra tại đáy cột chất lỏng do trọng lượng của nó được cho "
        "bởi phương trình sau:"))
    b.append(eq("p = ρ g h", "26.1"))
    b.append(p(
        "trong đó ρ là mật độ chất lỏng, g là gia tốc trọng trường và h là chiều cao cột chất lỏng. Một "
        "bảng chuyển đổi cho các đơn vị áp suất phổ biến nhất được cung cấp ở Bảng 26.1."))
    b.append(table(*_t261("vi")))

    b.append(h3("26.1.1 Các nguyên lý cảm biến", "Sensing Principles"))
    b.append(h3("Các phần tử cảm biến", "Sensing Elements"))
    b.append(p(
        "Vì áp suất là lực trên một diện tích, cách trực tiếp nhất để đo áp suất là cô lập một diện tích "
        "trên một phần tử cơ học đàn hồi để lực tác dụng lên đó. Sự biến dạng của phần tử cảm biến sinh "
        "ra chuyển vị và biến dạng có thể đo chính xác để hiệu chuẩn áp suất. Đây là cơ sở của hầu hết "
        "các cảm biến áp suất thương mại hiện nay. Các phần tử có thể chia thành màng (diaphragm), nang "
        "(capsule), ống bellows và ống (tube), như minh họa ở Hình 26.1."))
    b.append(fig(1, F.fig(1), "vi"))
    b.append(p(
        "Màng phẳng và màng gợn sóng biến dạng dưới áp suất; nang là hai màng hàn lại; ống bellows mở "
        "rộng theo trục; các ống Bourdon (chữ C, xoắn, xoắn ốc, xoắn lò xo) biến áp suất thành chuyển "
        "động đầu tự do. Độ cứng và hành trình của các phần tử này quyết định dải đo và độ nhạy."))

    b.append(h3("Các phương pháp phát hiện", "Detection Methods"))
    b.append(h3("Cảm biến áp suất điện dung", "Capacitive Pressure Sensors"))
    b.append(p(
        "Trong cảm biến điện dung, một màng kim loại hoặc silicon đóng vai trò phần tử cảm biến áp suất "
        "đồng thời là một bản cực của tụ điện; áp suất làm màng lõm vào, thay đổi khoảng cách giữa hai "
        "bản và do đó làm thay đổi điện dung. Hình 26.2 minh họa nguyên lý hoạt động với thiết kế một tụ "
        "đơn và thiết kế vi sai. Thiết kế vi sai giúp triệt tiêu các ảnh hưởng chế độ chung (nhiệt độ, "
        "áp suất tham chiếu)."))
    b.append(fig(2, F.fig(2), "vi"))
    b.append(p(
        "Hình 26.3 shows một tế bào cảm biến điện dung vi sai thực tế trang bị màng cách ly và dầu silicon "
        "truyền áp suất. Hình 26.4 là một cảm biến điện dung công nghiệp bền vững dựa trên tế bào này, "
        "với điện tử đọc tích hợp trong vỏ."))
    b.append(fig(3, F.fig(3), "vi"))
    b.append(fig(4, F.fig(4), "vi"))

    b.append(h3("Cảm biến áp điện trở", "Piezoresistive Pressure Sensors"))
    b.append(p(
        "Cảm biến áp điện trở (còn gọi là cảm biến strain-gage) là loại phổ biến nhất hiện nay. Hiệu ứng "
        "áp điện trở là sự thay đổi điện trở của vật liệu khi có ứng suất hay biến dạng. Độ nhạy của một "
        "strain-gage được biểu diễn bằng hệ số gage, định nghĩa là tỉ lệ thay đổi điện trở ΔR/R trên một "
        "đơn vị biến dạng:"))
    b.append(eq("G = (ΔR ⁄ R) ⁄ ε", "26.2"))
    b.append(p(
        "với biến dạng ε = ΔL/L. Cần phân biệt hai trường hợp: (1) biến dạng song song với hướng dòng "
        "điện (hệ số gage dọc) và (2) biến dạng vuông góc với hướng dòng điện (hệ số gage ngang). Hình "
        "26.5 shows kết cấu điển hình của cảm biến áp điện trở silicon: một mảng các điện trở khu vực "
        "(piezoresistor) khuếch tán trên màng."))
    b.append(fig(5, F.fig(5), "vi"))
    b.append(p(
        "Nhiều kiểu gói hàng thương mại phù hợp lắp trên mạch in hoặc có màng cách ly trong vỏ thép "
        "không gỉ, như ở Hình 26.6."))
    b.append(fig(6, F.fig(6), "vi"))
    b.append(p(
        "Mạch điều khiển tín hiệu điển hình dùng cầu phân áp (Hình 26.7) để chuyển đổi thay đổi điện trở "
        "thành điện áp. Vì hệ số gage của silicon luôn âm, có thể bù nhiệt bằng mạch phân áp thích hợp."))
    b.append(fig(7, F.fig(7), "vi"))

    b.append(h3("Cảm biến áp suất vi cơ bằng silicon", "Silicon Micromachined Pressure Sensors"))
    b.append(p(
        "Cảm biến áp suất vi cơ (micromachined) dùng công nghệ vi điện tử để chế tạo màng silicon và các "
        "điện trở/khối điện dung trên cùng một chip, cho kích thước nhỏ, giá thấp và có khả năng tích "
        "hợp điện tử. Chúng phù hợp rộng rãi cho đo áp suất công nghiệp và ô tô."))

    b.append(h3("Các hạn chế", "Limitations"))
    b.append(p(
        "Cảm biến áp điện trở silicon chịu hai ảnh hưởng nhiệt đáng kể: (1) hệ số nhiệt của điện trở "
        "(từ 0,06 %/°C đến 0,24 %/°C); và (2) hệ số nhiệt của hệ số gage (từ –0,06 %/°C đến –0,24 %/°C), "
        "làm giảm độ nhạy áp suất khi nhiệt độ tăng. Cần bù nhiệt (bằng mạch hoặc thuật toán) để duy trì "
        "độ chính xác trên dải nhiệt độ làm việc."))
    b.append(p(
        "Bảng 26.2 cung cấp thông tin liên hệ của một số hãng chọn lọc chế tạo cảm biến áp suất và hệ "
        "thống hiệu chuẩn áp suất."))
    b.append(table(*_t262("vi")))

    # -------------------------------------------------------- 26.2
    b.append(h2("26.2 Đo chân không", "Vacuum Measurement"))
    b.append(h3("Lịch sử và nền tảng", "Background and History of Vacuum Gages"))
    b.append(p(
        "Đo chân không đo áp suất thấp (dưới áp suất khí quyển). Các áp kế chân không thường được phân "
        "thành hai loại: đọc trực tiếp (bằng cơ học hoặc thủy ngân) và đọc gián tiếp (thường là điện tử). "
        "Hình 26.8 phân loại các áp kế đang dùng; Hình 26.9 shows dải áp suất làm việc của các áp kế khác "
        "nhau trên thang log."))
    b.append(fig(8, F.fig(8), "vi"))
    b.append(fig(9, F.fig(9), "vi"))

    b.append(h3("Các áp kế đọc trực tiếp", "Direct Reading Gages"))
    b.append(p(
        "Áp kế thủy ngân (manometer) đo chênh lệch cột thủy ngân. Hình 26.10 shows các kiểu manometer "
        "thủy ngân; ống thẳng đơn giản đo chênh lệch đến vài nghìn psi. Áp kế McLeod (Hình 26.11) nén "
        "thể tích khí trước khi đo, dùng làm chuẩn chính khi có bẫy nitơ lỏng, đo được tới ~10⁻⁶ torr. "
        "Áp kế Bourdon (Hình 26.12) dùng ống Bourdon chỉ áp suất trên khí quyển đến hàng nghìn psi. Áp "
        "kế màng (Hình 26.13) dùng màng đàn hồi làm một bản cực tụ (điện dung) hoặc gắn strain-gage."))
    b.append(fig(10, F.fig(10), "vi"))
    b.append(fig(11, F.fig(11), "vi"))
    b.append(fig(12, F.fig(12), "vi"))
    b.append(fig(13, F.fig(13), "vi"))

    b.append(h3("Các áp kế đọc gián tiếp", "Indirect Reading Gages"))
    b.append(p(
        "Áp kế dẫn nhiệt (thermal conductivity) đo sự mất nhiệt của dây nóng vào khí; hệ số truyền nhiệt "
        "phụ thuộc số Knudsen. Hình 26.14 shows các chế độ truyền nhiệt; Hình 26.15 là áp kế Pirani; Hình "
        "26.16 là đường hiệu chuẩn của áp kế Pirani (phụ thuộc khí). Tuyến tính giữa mật độ phân tử và "
        "dòng ion cho phép định nghĩa hệ số nhạy S:"))
    b.append(eq("I_i = S · I_e · P", "26.3"))
    b.append(p(
        "với I_i dòng ion (A), I_e dòng electron (A), P áp suất và S hệ số nhạy (nghịch đảo áp suất). "
        "Áp kế cặp nhiệt (Hình 26.17, 26.18) và áp kế đối lưu (Hình 26.19, 26.20) cũng khai thác mất "
        "nhiệt, với dải đo rộng hơn nhờ đối lưu."))
    b.append(fig(14, F.fig(14), "vi"))
    b.append(fig(15, F.fig(15), "vi"))
    b.append(fig(16, F.fig(16), "vi"))
    b.append(fig(17, F.fig(17), "vi"))
    b.append(fig(18, F.fig(18), "vi"))
    b.append(fig(19, F.fig(19), "vi"))
    b.append(fig(20, F.fig(20), "vi"))
    b.append(p(
        "Áp kế ion hóa dùng dòng electron ion hóa khí; dòng ion thu được tỉ lệ với áp suất. Áp kế triode "
        "(Hình 26.21, 26.22) nối sợi đốt, lưới và bản thu. Áp kế ion hóa nóng Bayard–Alpert (Hình 26.23, "
        "26.24) dùng bản thu mỏng để đạt dải rất thấp (~10⁻¹¹ torr). Áp kế bộ tách (extractor, Hình 26.25) "
        "và Penning (Hình 26.26) cùng áp kế từ trường kéo phân tử (Hình 26.27, 26.28) mở rộng xuống vùng "
        "siêu cao chân không (UHV)."))
    b.append(fig(21, F.fig(21), "vi"))
    b.append(fig(22, F.fig(22), "vi"))
    b.append(fig(23, F.fig(23), "vi"))
    b.append(fig(24, F.fig(24), "vi"))
    b.append(fig(25, F.fig(25), "vi"))
    b.append(fig(26, F.fig(26), "vi"))
    b.append(fig(27, F.fig(27), "vi"))
    b.append(p(
        "Trong vùng chảy phân tử, áp suất vùng gần đúng bởi (áp kế kéo phân tử / rô-to quay):"))
    b.append(eq("P = (π ρ a c̄ ⁄ (10 σ_eff)) · ((−ω′ − RD − 2αT′) ⁄ ω)", "26.4"))
    b.append(p(
        "với ρ mật độ rô-to, a bán kính rô-to, c̄ vận tốc phân tử khí trung bình, σ_eff hệ số thích ứng "
        "hiệu dụng, α hệ số giãn nở của bi, T′ tốc độ biến thiên nhiệt độ của bi và RD lực cản dư không "
        "phụ thuộc áp suất."))
    b.append(fig(28, F.fig(28), "vi"))
    b.append(p(
        "Đo áp suất riêng phần dùng phổ kế khối (quadrupole, Hình 26.29, 26.30), cho phổ cường độ theo "
        "số khối."))
    b.append(fig(29, F.fig(29), "vi"))
    b.append(fig(30, F.fig(30), "vi"))

    # -------------------------------------------------------- 26.3
    b.append(h2("26.3 Đo siêu âm", "Ultrasound Measurement"))
    b.append(h3("Các ứng dụng của siêu âm", "Applications of Ultrasound"))
    b.append(p(
        "Siêu âm (tần số trên 20 kHz) được dùng trong NDE (kiểm tra không phá hủy), đo lưu lượng, hình "
        "ảnh y tế (tim, bụng), khoảng cách/độ dày, làm sạch, hàn và tán sỏi (lithotripsy). Khả năng xuyên "
        "qua chất lỏng/rắn và phản xạ tại giao diện làm nó đặc biệt hữu ích cho đo lường."))

    b.append(h3("Định nghĩa các tham số siêu âm cơ bản", "Definition of Basic Ultrasound Parameters"))
    b.append(p(
        "Sóng âm là dao động cơ học, cần môi trường để truyền (không tồn tại trong chân không). Với sóng "
        "đơn tần (continuous wave, CW), quan hệ giữa tần số f, tốc độ âm c₀ và bước sóng λ là:"))
    b.append(eq("λ = c₀ ⁄ f", "26.5"))
    b.append(p(
        "Trở kháng âm đặc trưng z của môi trường không tổn hao:"))
    b.append(eq("z = ρ₀ c₀", "26.6"))
    b.append(p(
        "với ρ₀ mật độ (kg/m³). Trở kháng này liên hệ vận tốc hạt u với áp suất âm p:"))
    b.append(eq("z = p ⁄ u", "26.7"))
    b.append(p(
        "Tại giao diện giữa hai môi trường có trở kháng z_i và z_t, hệ số phản xạ áp suất và cường độ, "
        "R_p và R_I:"))
    b.append(eq("R_p = (z_i − z_t) ⁄ (z_i + z_t);  R_I = 4 z_i z_t ⁄ (z_i + z_t)²", "26.8"))
    b.append(p("Các hệ số truyền tương ứng T_p và T_I:"))
    b.append(eq("T_p = 2 z_t ⁄ (z_i + z_t);  T_I = 4 z_i z_t ⁄ (z_i + z_t)²", "26.9"))

    b.append(h3("Mô tả khái niệm của hình ảnh siêu âm", "Conceptual Description"))
    b.append(p(
        "Hình ảnh siêu âm được tạo bằng cách chiếu một chùm siêu âm hội tụ vào vật thể và ghi lại các "
        "echo phản xạ từ mặt trước và mặt sau của vật thể theo thời gian đến (Hình 26.31). Biên độ echo "
        "và thời gian đến được dùng để dựng ảnh (B-mode)."))
    b.append(fig(31, F.fig(31), "vi"))
    b.append(p(
        "Hệ siêu âm xung–echo (Hình 26.32) gồm bộ phát xung (pulser), bộ khuếch đại, đầu dò, bộ thu và "
        "khối xử lý/hiển thị. Hệ truyền (transmission, Hình 26.33) dùng hai đầu dò phát và thu đặt ở hai "
        "phía đối diện của vật cần khảo sát."))
    b.append(fig(32, F.fig(32), "vi"))
    b.append(fig(33, F.fig(33), "vi"))
    b.append(h3("Vận tốc âm", "Sound Velocity"))
    b.append(p("Với khí lý tưởng:"))
    b.append(eq("c₀ = √(γ P₀ ⁄ ρ₀) = √(γ r T_K)", "26.10"))
    b.append(p("với γ = C_P/C_V; ở 0 °C, không khí c₀ ≈ 331,6 m/s. Phụ thuộc nhiệt độ:"))
    b.append(eq("c₀ = c_ref √(1 + T ⁄ 273)", "26.11"))
    b.append(p("Với chất lỏng, dùng môđun nén đoạn nhiệt K_s:"))
    b.append(eq("c₀ = √(K_s ⁄ ρ₀)", "26.12"))
    b.append(p(
        "Với nước tinh khiết, tốc độ âm theo nhiệt độ và áp suất (xấp xỉ, vùng 1–100 atm):"))
    b.append(eq("c_H₂O = 1402,4 + 5,01 T − 0,055 T² + 0,00022 T³ + 1,6×10⁻⁶ P₀", "26.13"))
    b.append(p(
        "với T tính bằng °C và P₀ là áp suất tĩnh (N m⁻²); công thức đúng trong khoảng 1–100 atm."))
    b.append(p("Với sóng dọc trong rắn (hằng đàn hồi Lamé λ, μ):"))
    b.append(eq("c_L = √(c₁₁ ⁄ ρ₀) = √((λ + 2μ) ⁄ ρ₀)", "26.14"))

    b.append(h3("Lan truyền sóng trong môi trường đồng nhất", "Wave Propagation in Homogeneous Media"))
    b.append(p("Phương trình sóng tổng quát:"))
    b.append(eq("∇² p = (1 ⁄ c₀²) ∂²p ⁄ ∂t²", "26.15"))
    b.append(p("Nghiệm sóng phẳng điều hòa đơn tần:"))
    b.append(eq("p(r,t) = A e^{j(ω t − k·r)} + B e^{j(ω t + k·r)}", "26.16"))
    b.append(p("với số sóng:"))
    b.append(eq("k = ω ⁄ c₀ = 2π ⁄ λ", "26.17"))
    b.append(eq("k = k_x x̂ + k_y ŷ + k_z ẑ", "26.18"))
    b.append(eq("k_z = √(k² − k_x² − k_y²)", "26.19"))
    b.append(p("Sóng phẳng theo hướng +k:"))
    b.append(eq("p(r,t) = A e^{j(ω t − k·r)}", "26.20"))
    b.append(p("Sóng cầu từ nguồn tại gốc tọa độ:"))
    b.append(eq("p(r,t) = (A ⁄ r) e^{j(ω t − k r)} + (B ⁄ r) e^{j(ω t + k r)}", "26.21"))
    b.append(eq("p(r,t) = (A ⁄ r) exp[j(ωt − kr)],  r > a", "26.22"))
    b.append(h3("Cường độ âm và mức âm", "Acoustic Intensity and Sound Levels"))
    b.append(p("Cường độ âm I (trung bình công suất trên đơn vị diện tích):"))
    b.append(eq("I = (1 ⁄ T) ∫<sub>0</sub><sup>T</sup> p(t) u(t) dt", "26.23"))
    b.append(eq("I = P² ⁄ (2 ρ₀ c₀) = ½ P U", "26.24"))
    b.append(eq("SPL = 20 log₁₀(P_e ⁄ P_ref)  [dB]", "26.25"))
    b.append(eq("IL = 10 log₁₀(I ⁄ I_ref)  [dB]", "26.26"))

    b.append(h3("Phản xạ và khúc xạ tại giao diện", "Reflection and Refraction at Boundaries"))
    b.append(p("Điều kiện biên dẫn đến (định luật Snell):"))
    b.append(eq("sin θ_i = sin θ_r ;  sin θ_i ⁄ c₁ = sin θ_t ⁄ c₂", "26.27"))
    b.append(eq("θ_i = θ_r ;  θ_t = arcsin((c₂ ⁄ c₁) sin θ_i)", "26.28"))
    b.append(p("Góc tới tới hạn (chỉ khi c₁ < c₂):"))
    b.append(eq("sin θ_c = c₁ ⁄ c₂", "26.29"))
    b.append(p("Hệ số phản xạ Rayleigh (góc tới):"))
    b.append(eq("R(θ_i) = ((z₂ ⁄ z₁) − (cos θ_i ⁄ cos θ_t)) ⁄ ((z₂ ⁄ z₁) + (cos θ_i ⁄ cos θ_t))", "26.30"))
    b.append(p("với cos θ_t = √(1 − (c₂ ⁄ c₁)² sin²θ_i)."))
    b.append(p("Truyền qua một lớp đơn dưới góc tới chuẩn:"))
    b.append(eq("R = P_r ⁄ P_i = [(1 − z₁ ⁄ z₃) cos k₂L + j(z₂ ⁄ z₃ − z₁ ⁄ z₂) sin k₂L] ⁄ [(1 + z₁ ⁄ z₃) cos k₂L + j(z₂ ⁄ z₃ + z₁ ⁄ z₂) sin k₂L]", "26.31"))
    b.append(eq("T = P_t ⁄ P_i = 2 ⁄ [(1 + z₁ ⁄ z₃) cos k₂L + j(z₂ ⁄ z₃ + z₁ ⁄ z₂) sin k₂L]", "26.32"))
    b.append(p(
        "Các trường hợp đặc biệt: khi z₁ = z₃ tử số đơn giản hoá; khi k₂L ≪ 1 thì cos k₂L ≈ 1 và "
        "sin k₂L ≈ k₂L."))
    b.append(p("Truyền 100 % năng lượng (R = 0) khi:"))
    b.append(eq("k₂L = π ⁄ 2 + nπ ;  z₂ = √(z₁ z₃)", "26.33"))
    b.append(fig(34, F.fig(34), "vi"))
    b.append(fig(35, F.fig(35), "vi"))

    b.append(h3("Đo suy hao", "Attenuation Measurement"))
    b.append(p("Suy hao (dB/cm) đo bằng phương pháp truyền qua hoặc xung–vang (pulse-echo):"))
    b.append(eq("Att [dB/cm] = (1 ⁄ d) 10 log₁₀(∫<sub>0</sub><sup>∞</sup> |v₁(t)|² dt ⁄ ∫<sub>0</sub><sup>∞</sup> |v₂(t)|² dt) − 20 log₁₀(4 z₁ z₂ ⁄ (z₁ + z₂)²)", "26.34"))
    b.append(eq("Att [dB/cm] = (1 ⁄ 2d) 10 log₁₀(∫<sub>0</sub><sup>ΔT</sup> |v_f(t)|² dt ⁄ ∫<sub>0</sub><sup>ΔT</sup> |v_b(t)|² dt) ≅ (1 ⁄ 2d) 20 log₁₀(peak v_f ⁄ peak v_b)", "26.35"))
    b.append(p(
        "với d là bề dày mẫu; số hạng thứ hai ở 26.34 hiệu chỉnh tổn hao truyền qua và có thể bỏ qua "
        "bằng cách đo suy hao gia tăng theo độ dày."))
    b.append(fig(36, F.fig(36), "vi"))

    b.append(h3("Trường CW từ nguồn piston phẳng", "CW Fields from Planar Piston Sources"))
    b.append(p(
        "Trường từ đầu dò piston phẳng chia thành vùng gần (near field) và vùng xa (far field). Độ dài "
        "vùng gần:"))
    b.append(eq("NF = a² ⁄ λ", "26.36"))
    b.append(p("Góc phân kỳ xấp xỉ:"))
    b.append(eq("θ = arcsin(0,61 λ ⁄ a)", "26.37"))
    b.append(p("Áp suất trục (baffled piston):"))
    b.append(eq("P_ax(x) = 2 ρ₀ c₀ U₀ |sin((ka ⁄ 2)[√(x² ⁄ a² + 1) − (x ⁄ a)])|", "26.38"))
    b.append(eq("P(r,θ) = (ρ₀ c₀ U₀ ⁄ 2)(ka)(a ⁄ r)[2 J₁(ka sinθ) ⁄ (ka sinθ)]", "26.39"))
    b.append(p(
        "với U₀ là biên độ vận tốc trên bề mặt đầu dò và J₁ là hàm Bessel bậc một."))
    b.append(p("Hướng tính (directivity):"))
    b.append(eq("D(x) = I_ax(x) [given] ⁄ I_ax(x) [simple]", "26.40"))
    b.append(eq("D = (ka)³ ⁄ (ka − J₁(2ka))", "26.41"))
    b.append(fig(37, F.fig(37), "vi"))

    b.append(h3("Đầu dò đơn và mảng", "Single-Element / Array Transducers"))
    b.append(p(
        "Đầu dò siêu âm dùng hiệu ứng áp điện để chuyển điện–cơ và ngược lại. Các hằng số vật liệu quan "
        "trọng được liệt kê ở Bảng 26.3. Hằng số truyền d₃₃ cho biến dạng cơ khi đặt điện trường E₃:"))
    b.append(eq("S₃ = d₃₃ E₃ = d₃₃ V_appl ⁄ l", "26.42"))
    b.append(eq("Δl = d₃₃ V_appl", "26.43"))
    b.append(p("Hằng số thu g₃₃ cho điện áp ra khi chịu ứng suất T₃:"))
    b.append(eq("V_out = g₃₃ T₃ l", "26.44"))
    b.append(table(*_t263("vi")))
    b.append(p(
        "Các vật liệu áp điện thông dụng: gốm titanat bari (BaTiO₃), PZT-5, chì meta-niobat (PbNb₂O₆) và "
        "polyme PVDF. Vật liệu từ giảo (magnetostrictive) như nickel, alfenol co/giãn dưới từ trường "
        "(Joule, 1847), cũng dùng làm đầu dò."))

    b.append(h3("Tiêu chí chọn tần số", "Selection Criteria for Ultrasound Frequencies"))
    b.append(p(
        "Tần số càng cao thì phân giải không gian càng tốt nhưng suy hao càng lớn và dải truyền càng ngắn. "
        "Tần số thấp dùng cho đo khoảng cách xa hoặc qua vật liệu tổn hao lớn; tần số cao dùng cho hình "
        "ảnh chi tiết nông."))

    b.append(h3("Các tham số cơ bản trong đo siêu âm", "Basic Parameters in Ultrasound Measurements"))
    b.append(p(
        "Các tham số đo lường gồm: tốc độ âm, suy hao, trở kháng âm, hệ số phản xạ, băng thông, hướng "
        "tính và độ phân giải trục/ngang. Chúng được xác định từ các phương trình trên kết hợp với đặc "
        "tính đầu dò."))

    b.append(h3("Lý thuyết và ứng dụng", "Theory and Applications"))
    b.append(p(
        "Hiệu ứng Doppler: tần số Doppler f_d do chất phân tán chuyển động với vận tốc v, góc θ so với "
        "chùm tia:"))
    b.append(eq("f_d = 2 v cos θ ⁄ c₀", "26.45"))
    b.append(p(
        "Hệ thống CW Doppler đo tần số nhưng không đo cự ly; hệ thống xung (PW Doppler) đo cả vận tốc và "
        "cự ly, chịu ảnh hưởng ráp (aliasing). Phổ Doppler thu được bằng FFT khi có phân bố vận tốc."))
    b.append(p("Nhiễu xạ Fresnel (xấp xỉ paraxial):"))
    b.append(eq("p(x₀,y₀,z,ω) = (A₀ ⁄ (jλz)) ∫∫_S u(x,y,ω) exp[−jk (x²+y²) ⁄ (2z)] exp[jk (x₀x + y₀y) ⁄ z] dx dy", "26.46"))
    b.append(p("Xấp xỉ Fraunhofer (vùng xa):"))
    b.append(eq("p(x₀,y₀,z,ω) = (A₀ ⁄ (jλz)) ∫∫_S u(x,y,ω) exp[jk (x₀x + y₀y) ⁄ z] dx dy", "26.47"))
    b.append(p("Tích phân Rayleigh (kỹ thuật xung):"))
    b.append(eq("h(r,t) = (1 ⁄ (2π)) ∫∫_S (δ(t − r′ ⁄ c) ⁄ r′) dS", "26.48"))
    b.append(eq("φ(r,t) = h(r,t) ⊗ u(t)", "26.49"))
    b.append(eq("u(r,t) = ∇ φ(r,t)", "26.50"))
    b.append(eq("p(r,t) = − ρ₀ ∂φ(r,t) ⁄ ∂t", "26.51"))
    b.append(p("Vận tốc thu được từ mặt phản xạ có trở kháng lớn:"))
    b.append(eq("d v(r,t) = A₀ ρ₀ (cos[ψ(r)] ⁄ c₀) [h(r,t) ⊗ h(r,t) ⊗ ∂²u(t) ⁄ ∂t²] dA", "26.52"))
    b.append(p(
        "trong đó S là bề mặt đầu dò, A₀ là hằng số, r′ là khoảng cách từ dS tới điểm trường và ⊗ là "
        "tích chập theo thời gian."))

    b.append(h3("Tổng quan ứng dụng", "Review of Applications"))
    b.append(p(
        "Siêu âm đo được: độ dày, khoảng cách, vận tốc lưu chất (Doppler), mô đun đàn hồi, khuyết tật "
        "(NDE), và hình ảnh y tế/tế bào. Kính hiển vi âm học (SAM) quan sát cấu trúc vi mô không phá hủy."))

    b.append(h3("Các hãng sản xuất siêu âm tiêu biểu", "Selected Manufacturers of Ultrasound Products"))
    b.append(table(*_t264("vi")))

    b.append(h3("Các chủ đề nâng cao", "Advanced Topics"))
    b.append(p(
        "Các chủ đề nâng cao gồm: mô hình đầu dò (Mason, KLM, Redwood) gần cộng hưởng; mảng pha (phased "
        "array) để quét chùm tia điện tử; thấu kính âm và hội tụ; ảnh ba chiều; và phổ kế khối cho áp "
        "suất riêng phần trong chân không kết hợp siêu âm trong khí."))
    return "".join(b)


# ================================================================ English

def body_en():
    b = []
    b.append(p(
        "This chapter presents the principles of pressure and sound (ultrasound) measurement. Section "
        "26.1 describes pressure-sensing elements, detection methods (capacitive, piezoresistive) and "
        "silicon micromachined pressure sensors together with their limitations. Section 26.2 covers "
        "vacuum measurement — from direct-reading gages (mercury, Bourdon, diaphragm) to indirect-reading "
        "gages (thermal conductivity, ionization, molecular drag, mass spectrometry). Section 26.3 "
        "introduces basic ultrasound parameters, wave propagation, reflection/refraction at interfaces, "
        "transducer radiation fields, attenuation measurement, piezoelectric transducers, Doppler and the "
        "diffraction integrals."))

    # -------------------------------------------------------- 26.1
    b.append(h2("26.1 Pressure Measurement", "Đo áp suất"))
    b.append(p(
        "Pressure is defined as the normal force per unit area exerted by a fluid (liquid or gas) on any "
        "surface. Absolute, gage and differential pressures are often written psia, psig and psid; in "
        "other unit systems this distinction is usually not made. A second class of units expresses "
        "pressure through the height of a static liquid column, e.g. the millimetre of mercury at 0 °C "
        "(mm Hg, also the torr) or the inch of water at 4 °C."))
    b.append(p(
        "The pressure p developed at the base of a liquid column by its weight is:"))
    b.append(eq("p = ρ g h", "26.1"))
    b.append(p(
        "where ρ is the liquid density, g is the acceleration of gravity and h is the column height. A "
        "conversion table for the most popular pressure units is given in Table 26.1."))
    b.append(table(*_t261("en")))

    b.append(h3("26.1.1 Sensing Principles", "Các nguyên lý cảm biến"))
    b.append(h3("Sensing Elements", "Các phần tử cảm biến"))
    b.append(p(
        "Because pressure is force per area, the most direct way to measure it is to isolate an area on "
        "an elastic element for the force to act on. The deformation of the sensing element produces "
        "displacements and strains that are sensed to give a calibrated pressure reading; this underlies "
        "essentially all commercial pressure sensors today. The elements group into diaphragms, "
        "capsules, bellows and tubes, as shown in Figure 26.1."))
    b.append(fig(1, F.fig(1), "en"))
    b.append(p(
        "Flat and corrugated diaphragms deflect under pressure; a capsule joins two diaphragms; a bellows "
        "extends axially; Bourdon tubes (C-shaped, twisted, helical, spiral) convert pressure into free-"
        "end motion. Their stiffness and travel set the range and sensitivity."))

    b.append(h3("Detection Methods", "Các phương pháp phát hiện"))
    b.append(h3("Capacitive Pressure Sensors", "Cảm biến áp suất điện dung"))
    b.append(p(
        "In a capacitive sensor a metal or silicon diaphragm is both the pressure-sensing element and one "
        "plate of a capacitor; pressure deflects the diaphragm, changing the plate spacing and hence the "
        "capacitance. Figure 26.2 shows the single-capacitor and differential designs. The differential "
        "design rejects common-mode effects such as temperature and reference pressure."))
    b.append(fig(2, F.fig(2), "en"))
    b.append(p(
        "Figure 26.3 shows a practical differential capacitive sensing cell with isolating diaphragms "
        "and silicone oil; Figure 26.4 is a rugged industrial capacitive sensor built on that cell with "
        "readout electronics in the housing."))
    b.append(fig(3, F.fig(3), "en"))
    b.append(fig(4, F.fig(4), "en"))

    b.append(h3("Piezoresistive Pressure Sensors", "Cảm biến áp điện trở"))
    b.append(p(
        "Piezoresistive (strain-gage) sensors are the most common type in use. The piezoresistive effect "
        "is a change in electrical resistance of a material under stress or strain. The gage factor G "
        "expresses the sensitivity — the fractional change in resistance ΔR/R per unit strain:"))
    b.append(eq("G = (ΔR ⁄ R) ⁄ ε", "26.2"))
    b.append(p(
        "with strain ε = ΔL/L. Two cases are distinguished: strain parallel to the current (longitudinal "
        "gage factor) and strain perpendicular to it (transverse gage factor). Figure 26.5 shows a typical "
        "silicon piezoresistive sensor: an array of diffused piezo-resistors on a diaphragm."))
    b.append(fig(5, F.fig(5), "en"))
    b.append(p(
        "Many commercial packages suit printed-circuit-board mounting or have isolating diaphragms in "
        "stainless-steel housings, as in Figure 26.6."))
    b.append(fig(6, F.fig(6), "en"))
    b.append(p(
        "A typical signal-conditioning circuit uses a voltage-divider bridge (Figure 26.7) to convert "
        "the resistance change into a voltage. Because the silicon gage factor is always negative, "
        "temperature compensation can be arranged in the bridge."))
    b.append(fig(7, F.fig(7), "en"))

    b.append(h3("Silicon Micromachined Pressure Sensors", "Cảm biến áp suất vi cơ bằng silicon"))
    b.append(p(
        "Micromachined silicon sensors use microelectronic fabrication to build the diaphragm and the "
        "resistors or capacitor plates on one chip, giving small size, low cost and integrated "
        "electronics. They are widely used in industrial and automotive pressure measurement."))

    b.append(h3("Limitations", "Các hạn chế"))
    b.append(p(
        "Silicon piezoresistive sensors suffer two notable thermal effects: (1) the temperature "
        "coefficient of resistance (0.06 %/°C to 0.24 %/°C); and (2) the temperature coefficient of the "
        "gage factor (–0.06 %/°C to –0.24 %/°C), which lowers pressure sensitivity as temperature rises. "
        "Thermal compensation (circuit or algorithm) is needed to hold accuracy over the operating range."))
    b.append(p(
        "Table 26.2 lists selected companies that make pressure sensors and pressure calibration "
        "systems."))
    b.append(table(*_t262("en")))

    # -------------------------------------------------------- 26.2
    b.append(h2("26.2 Vacuum Measurement", "Đo chân không"))
    b.append(h3("Background and History of Vacuum Gages", "Lịch sử và nền tảng"))
    b.append(p(
        "Vacuum measurement covers pressures below atmospheric. Vacuum gages are broadly direct-reading "
        "(mechanical or mercury) or indirect-reading (usually electronic). Figure 26.8 classifies the "
        "gages in current use; Figure 26.9 shows their operating-pressure ranges on a log scale."))
    b.append(fig(8, F.fig(8), "en"))
    b.append(fig(9, F.fig(9), "en"))

    b.append(h3("Direct Reading Gages", "Các áp kế đọc trực tiếp"))
    b.append(p(
        "Mercury manometers measure a column difference (Figure 26.10); the straight-tube manometer "
        "covers up to several thousand psi. The McLeod gage (Figure 26.11) compresses the gas before "
        "measurement and serves as a primary standard with a liquid-nitrogen trap, down to ~10⁻⁶ torr. "
        "The Bourdon gage (Figure 26.12) reads above atmospheric to thousands of psi. The diaphragm gage "
        "(Figure 26.13) uses an elastic diaphragm as one capacitor plate (capacitive) or with a strain "
        "gage."))
    b.append(fig(10, F.fig(10), "en"))
    b.append(fig(11, F.fig(11), "en"))
    b.append(fig(12, F.fig(12), "en"))
    b.append(fig(13, F.fig(13), "en"))

    b.append(h3("Indirect Reading Gages", "Các áp kế đọc gián tiếp"))
    b.append(p(
        "Thermal-conductivity gages measure the heat lost from a hot wire to the gas; the heat-transfer "
        "coefficient depends on the Knudsen number. Figure 26.14 shows the regimes; Figure 26.15 the "
        "Pirani gage; Figure 26.16 its calibration curves (gas dependent). A linear relation between "
        "molecular density and ion current defines a sensitivity factor S:"))
    b.append(eq("I_i = S · I_e · P", "26.3"))
    b.append(p(
        "with I_i the ion current (A), I_e the electron current (A), P the pressure and S the sensitivity "
        "(reciprocal pressure). The thermocouple gage (Figures 26.17, 26.18) and convection gage "
        "(Figures 26.19, 26.20) also exploit heat loss, the latter extending the range via convection."))
    b.append(fig(14, F.fig(14), "en"))
    b.append(fig(15, F.fig(15), "en"))
    b.append(fig(16, F.fig(16), "en"))
    b.append(fig(17, F.fig(17), "en"))
    b.append(fig(18, F.fig(18), "en"))
    b.append(fig(19, F.fig(19), "en"))
    b.append(fig(20, F.fig(20), "en"))
    b.append(p(
        "Ionization gages ionize the gas with electrons; the collected ion current is proportional to "
        "pressure. The triode gage (Figures 26.21, 26.22) connects filament, grid and collector. The "
        "hot-cathode Bayard–Alpert gage (Figures 26.23, 26.24) uses a thin collector for very low ranges "
        "(~10⁻¹¹ torr). The extractor (Figure 26.25) and Penning (Figure 26.26) gages and the magnetic "
        "drag/magnetron types (Figures 26.27, 26.28) extend into the UHV region."))
    b.append(fig(21, F.fig(21), "en"))
    b.append(fig(22, F.fig(22), "en"))
    b.append(fig(23, F.fig(23), "en"))
    b.append(fig(24, F.fig(24), "en"))
    b.append(fig(25, F.fig(25), "en"))
    b.append(fig(26, F.fig(26), "en"))
    b.append(fig(27, F.fig(27), "en"))
    b.append(p(
        "In the molecular-flow region the pressure is given approximately by the spinning-rotor (molecular "
        "drag) gage relation:"))
    b.append(eq("P = (π ρ a c̄ ⁄ (10 σ_eff)) · ((−ω′ − RD − 2αT′) ⁄ ω)", "26.4"))
    b.append(fig(28, F.fig(28), "en"))
    b.append(p(
        "Partial-pressure measurement uses a quadrupole mass spectrometer (Figures 26.29, 26.30), giving "
        "a spectrum of intensity versus mass number."))
    b.append(fig(29, F.fig(29), "en"))
    b.append(fig(30, F.fig(30), "en"))

    # -------------------------------------------------------- 26.3
    b.append(h2("26.3 Ultrasound Measurement", "Đo siêu âm"))
    b.append(h3("Applications of Ultrasound", "Các ứng dụng của siêu âm"))
    b.append(p(
        "Ultrasound (above 20 kHz) is used in NDE, flow metering, medical imaging (cardiac, abdominal), "
        "thickness/level gauging, cleaning, welding and lithotripsy. Its ability to penetrate liquids and "
        "solids and reflect at interfaces makes it especially useful for measurement."))

    b.append(h3("Definition of Basic Ultrasound Parameters", "Định nghĩa các tham số siêu âm cơ bản"))
    b.append(p(
        "Acoustic waves are mechanical vibrations and need a medium (they cannot exist in vacuum). For a "
        "single-frequency (continuous-wave, CW) sound, the relation among frequency f, sound speed c₀ and "
        "wavelength λ is:"))
    b.append(eq("λ = c₀ ⁄ f", "26.5"))
    b.append(p("The specific acoustic impedance z of a lossless medium:"))
    b.append(eq("z = ρ₀ c₀", "26.6"))
    b.append(p("with ρ₀ the density (kg/m³). Acoustic impedance links particle velocity u to acoustic "
               "pressure p:"))
    b.append(eq("z = p ⁄ u", "26.7"))
    b.append(p(
        "At an interface between media of acoustic impedances z_i and z_t, the pressure and intensity "
        "reflection coefficients R_p and R_I are:"))
    b.append(eq("R_p = (z_i − z_t) ⁄ (z_i + z_t);  R_I = 4 z_i z_t ⁄ (z_i + z_t)²", "26.8"))
    b.append(p("The corresponding pressure and intensity transmission coefficients T_p and T_I:"))
    b.append(eq("T_p = 2 z_t ⁄ (z_i + z_t);  T_I = 4 z_i z_t ⁄ (z_i + z_t)²", "26.9"))

    b.append(h3("Conceptual Description", "Mô tả khái niệm"))
    b.append(p(
        "Ultrasound imaging is formed by insonifying an object with a focused beam and recording the "
        "echoes reflected from its front and back surfaces versus arrival time (Figure 26.31). Echo "
        "strength and arrival time are used to build a B-mode image."))
    b.append(fig(31, F.fig(31), "en"))
    b.append(p(
        "A pulse-echo ultrasound system (Figure 26.32) comprises a pulser, amplifier, transducer, "
        "receiver and processing/display block. A transmission system (Figure 26.33) uses separate "
        "transmit and receive transducers on opposite sides of the object."))
    b.append(fig(32, F.fig(32), "en"))
    b.append(fig(33, F.fig(33), "en"))
    b.append(h3("Sound Velocity", "Vận tốc âm"))
    b.append(p("For an ideal gas:"))
    b.append(eq("c₀ = √(γ P₀ ⁄ ρ₀) = √(γ r T_K)", "26.10"))
    b.append(p("with γ = C_P/C_V; for air at 0 °C, c₀ ≈ 331.6 m/s. Its temperature dependence:"))
    b.append(eq("c₀ = c_ref √(1 + T ⁄ 273)", "26.11"))
    b.append(p("For liquids, using the adiabatic bulk modulus K_s:"))
    b.append(eq("c₀ = √(K_s ⁄ ρ₀)", "26.12"))
    b.append(p("For pure water, the sound speed as a function of temperature and pressure "
               "(approximate, 1–100 atm):"))
    b.append(eq("c_H₂O = 1402.4 + 5.01 T − 0.055 T² + 0.00022 T³ + 1.6×10⁻⁶ P₀", "26.13"))
    b.append(p("For longitudinal waves in a solid (Lamé constants λ, μ):"))
    b.append(eq("c_L = √(c₁₁ ⁄ ρ₀) = √((λ + 2μ) ⁄ ρ₀)", "26.14"))

    b.append(h3("Wave Propagation in Homogeneous Media", "Lan truyền sóng trong môi trường đồng nhất"))
    b.append(p("The general wave equation:"))
    b.append(eq("∇² p = (1 ⁄ c₀²) ∂²p ⁄ ∂t²", "26.15"))
    b.append(p("The harmonic plane-wave solution:"))
    b.append(eq("p(r,t) = A e^{j(ω t − k·r)} + B e^{j(ω t + k·r)}", "26.16"))
    b.append(p("with wavenumber:"))
    b.append(eq("k = ω ⁄ c₀ = 2π ⁄ λ", "26.17"))
    b.append(eq("k = k_x x̂ + k_y ŷ + k_z ẑ", "26.18"))
    b.append(eq("k_z = √(k² − k_x² − k_y²)", "26.19"))
    b.append(p("Plane wave in the +k direction:"))
    b.append(eq("p(r,t) = A e^{j(ω t − k·r)}", "26.20"))
    b.append(p("Spherical waves from a source at the origin:"))
    b.append(eq("p(r,t) = (A ⁄ r) e^{j(ω t − k r)} + (B ⁄ r) e^{j(ω t + k r)}", "26.21"))
    b.append(eq("p(r,t) = (A ⁄ r) exp[j(ωt − kr)],  r > a", "26.22"))
    b.append(h3("Acoustic Intensity and Sound Levels", "Cường độ âm và mức âm"))
    b.append(p("The acoustic intensity I (mean power per unit area):"))
    b.append(eq("I = (1 ⁄ T) ∫<sub>0</sub><sup>T</sup> p(t) u(t) dt", "26.23"))
    b.append(eq("I = P² ⁄ (2 ρ₀ c₀) = ½ P U", "26.24"))
    b.append(eq("SPL = 20 log₁₀(P_e ⁄ P_ref)  [dB]", "26.25"))
    b.append(eq("IL = 10 log₁₀(I ⁄ I_ref)  [dB]", "26.26"))

    b.append(h3("Reflection and Refraction at Boundaries", "Phản xạ và khúc xạ tại giao diện"))
    b.append(p("The boundary conditions give Snell's law:"))
    b.append(eq("sin θ_i = sin θ_r ;  sin θ_i ⁄ c₁ = sin θ_t ⁄ c₂", "26.27"))
    b.append(eq("θ_i = θ_r ;  θ_t = arcsin((c₂ ⁄ c₁) sin θ_i)", "26.28"))
    b.append(p("The critical incident angle (only when c₁ < c₂):"))
    b.append(eq("sin θ_c = c₁ ⁄ c₂", "26.29"))
    b.append(p("The Rayleigh reflection coefficient (at angle):"))
    b.append(eq("R(θ_i) = ((z₂ ⁄ z₁) − (cos θ_i ⁄ cos θ_t)) ⁄ ((z₂ ⁄ z₁) + (cos θ_i ⁄ cos θ_t))", "26.30"))
    b.append(p("Transmission through a single layer under normal incidence:"))
    b.append(eq("R = P_r ⁄ P_i = [(1 − z₁ ⁄ z₃) cos k₂L + j(z₂ ⁄ z₃ − z₁ ⁄ z₂) sin k₂L] ⁄ [(1 + z₁ ⁄ z₃) cos k₂L + j(z₂ ⁄ z₃ + z₁ ⁄ z₂) sin k₂L]", "26.31"))
    b.append(eq("T = P_t ⁄ P_i = 2 ⁄ [(1 + z₁ ⁄ z₃) cos k₂L + j(z₂ ⁄ z₃ + z₁ ⁄ z₂) sin k₂L]", "26.32"))
    b.append(p("100 % energy transmission (R = 0) requires:"))
    b.append(eq("k₂L = π ⁄ 2 + nπ ;  z₂ = √(z₁ z₃)", "26.33"))
    b.append(fig(34, F.fig(34), "en"))
    b.append(fig(35, F.fig(35), "en"))

    b.append(h3("Attenuation Measurement", "Đo suy hao"))
    b.append(p("Attenuation (dB/cm) is measured by transmission or pulse-echo:"))
    b.append(eq("Att [dB/cm] = (1 ⁄ d) 10 log₁₀(∫<sub>0</sub><sup>∞</sup> |v₁(t)|² dt ⁄ ∫<sub>0</sub><sup>∞</sup> |v₂(t)|² dt) − 20 log₁₀(4 z₁ z₂ ⁄ (z₁ + z₂)²)", "26.34"))
    b.append(eq("Att [dB/cm] = (1 ⁄ 2d) 10 log₁₀(∫<sub>0</sub><sup>ΔT</sup> |v_f(t)|² dt ⁄ ∫<sub>0</sub><sup>ΔT</sup> |v_b(t)|² dt) ≅ (1 ⁄ 2d) 20 log₁₀(peak v_f ⁄ peak v_b)", "26.35"))
    b.append(fig(36, F.fig(36), "en"))

    b.append(h3("CW Fields from Planar Piston Sources", "Trường CW từ nguồn piston phẳng"))
    b.append(p(
        "The field of a planar piston transducer splits into a near field and a far field. The near-field "
        "length:"))
    b.append(eq("NF = a² ⁄ λ", "26.36"))
    b.append(p("The divergence angle approximately:"))
    b.append(eq("θ = arcsin(0.61 λ ⁄ a)", "26.37"))
    b.append(p("The axial pressure (baffled piston):"))
    b.append(eq("P_ax(x) = 2 ρ₀ c₀ U₀ |sin((ka ⁄ 2)[√(x² ⁄ a² + 1) − (x ⁄ a)])|", "26.38"))
    b.append(eq("P(r,θ) = (ρ₀ c₀ U₀ ⁄ 2)(ka)(a ⁄ r)[2 J₁(ka sinθ) ⁄ (ka sinθ)]", "26.39"))
    b.append(p("The directivity D:"))
    b.append(eq("D(x) = I_ax(x) [given] ⁄ I_ax(x) [simple]", "26.40"))
    b.append(eq("D = (ka)³ ⁄ (ka − J₁(2ka))", "26.41"))
    b.append(fig(37, F.fig(37), "en"))

    b.append(h3("Single-Element / Array Transducers", "Đầu dò đơn và mảng"))
    b.append(p(
        "Ultrasound transducers use the piezoelectric effect to convert electrical-to-mechanical and back. "
        "The key material constants are listed in Table 26.3. The transmission constant d₃₃ gives the "
        "mechanical strain under an applied field E₃:"))
    b.append(eq("S₃ = d₃₃ E₃ = d₃₃ V_appl ⁄ l", "26.42"))
    b.append(eq("Δl = d₃₃ V_appl", "26.43"))
    b.append(p("The receiving constant g₃₃ gives the output voltage under an applied stress T₃:"))
    b.append(eq("V_out = g₃₃ T₃ l", "26.44"))
    b.append(table(*_t263("en")))
    b.append(p(
        "Common piezoelectric materials are barium titanate (BaTiO₃), PZT-5, lead meta-niobate "
        "(PbNb₂O₆) and the polymer PVDF. Magnetostrictive materials such as nickel and alfenol "
        "contract or expand under a magnetic field (Joule, 1847) and also serve as transducers."))

    b.append(h3("Selection Criteria for Ultrasound Frequencies", "Tiêu chí chọn tần số"))
    b.append(p(
        "Higher frequency gives better spatial resolution but greater attenuation and shorter range. Low "
        "frequencies suit long range or lossy media; high frequencies suit detailed shallow imaging."))

    b.append(h3("Basic Parameters in Ultrasound Measurements", "Các tham số cơ bản trong đo siêu âm"))
    b.append(p(
        "Measured parameters include sound speed, attenuation, acoustic impedance, reflection "
        "coefficient, bandwidth, directivity and axial/lateral resolution — determined from the equations "
        "above together with transducer characteristics."))

    b.append(h3("Theory and Applications", "Lý thuyết và ứng dụng"))
    b.append(p(
        "The Doppler effect: the Doppler frequency f_d for scatterers moving at velocity v, at angle θ to "
        "the beam:"))
    b.append(eq("f_d = 2 v cos θ ⁄ c₀", "26.45"))
    b.append(p(
        "CW Doppler measures frequency but not range; pulsed-wave (PW) Doppler measures both velocity "
        "and range and is subject to aliasing. A Doppler spectrum (via FFT) arises with a velocity "
        "distribution. The Fresnel diffraction integral (paraxial):"))
    b.append(eq("p(x₀,y₀,z,ω) = (A₀ ⁄ (jλz)) ∫∫_S u(x,y,ω) exp[−jk (x²+y²) ⁄ (2z)] exp[jk (x₀x + y₀y) ⁄ z] dx dy", "26.46"))
    b.append(p("The Fraunhofer (far-field) approximation:"))
    b.append(eq("p(x₀,y₀,z,ω) = (A₀ ⁄ (jλz)) ∫∫_S u(x,y,ω) exp[jk (x₀x + y₀y) ⁄ z] dx dy", "26.47"))
    b.append(p("The Rayleigh integral (impulse technique):"))
    b.append(eq("h(r,t) = (1 ⁄ (2π)) ∫∫_S (δ(t − r′ ⁄ c) ⁄ r′) dS", "26.48"))
    b.append(eq("φ(r,t) = h(r,t) ⊗ u(t)", "26.49"))
    b.append(eq("u(r,t) = ∇ φ(r,t)", "26.50"))
    b.append(eq("p(r,t) = − ρ₀ ∂φ(r,t) ⁄ ∂t", "26.51"))
    b.append(p("The received velocity from a high-impedance reflector:"))
    b.append(eq("d v(r,t) = A₀ ρ₀ (cos[ψ(r)] ⁄ c₀) [h(r,t) ⊗ h(r,t) ⊗ ∂²u(t) ⁄ ∂t²] dA", "26.52"))

    b.append(h3("Review of Applications", "Tổng quan ứng dụng"))
    b.append(p(
        "Ultrasound measures thickness, distance, fluid velocity (Doppler), elastic modulus, defects "
        "(NDE) and medical/tissue images. Acoustic microscopy (SAM) inspects microstructure "
        "non-destructively."))

    b.append(h3("Selected Manufacturers of Ultrasound Products", "Các hãng sản xuất siêu âm tiêu biểu"))
    b.append(table(*_t264("en")))

    b.append(h3("Advanced Topics", "Các chủ đề nâng cao"))
    b.append(p(
        "Advanced topics include transducer models near resonance (Mason, KLM, Redwood), phased arrays "
        "for electronic beam steering, acoustic lenses and focusing, three-dimensional imaging, and mass "
        "spectrometry for partial-pressure measurement in vacuum combined with gas-borne ultrasound."))
    return "".join(b)


# ================================================================ build

def build(lang):
    vi = lang == "vi"
    switch = ("%s%s/" % (BASE_EN, CSLUG)) if vi else ("%s%s/" % (BASE_VI, CSLUG))
    title = ("Chương 26 — %s · Sổ tay Đo lường, Thiết bị đo và Cảm biến" % TITLE_VI if vi
             else "Chapter 26 — %s · Measurement, Instrumentation and Sensors Handbook" % TITLE_EN)
    desc = ("Bản dịch tiếng Việt Chương 26 “Đo áp suất và âm thanh” của K. H.-L. Chau, R. Goehner, "
            "E. Drubetsky, H. M. Brady, W. H. Bayles Jr. và P. C. Pedersen — đo áp suất (phần tử cảm "
            "biến, điện dung, áp điện trở, vi cơ silicon), đo chân không (áp kế trực tiếp/gián tiếp, "
            "ion hóa, kéo phân tử, phổ kế khối) và đo siêu âm (thông số, lan truyền sóng, phản xạ, "
            "trường đầu dò, Doppler, nhiễu xạ), với 37 hình, 52 phương trình và 4 bảng." if vi
            else
            "Companion to Chapter 26 of the CRC Measurement Handbook — pressure measurement "
            "(sensing elements, capacitive, piezoresistive, silicon micromachined), vacuum measurement "
            "(direct/indirect gages, ionization, molecular drag, mass spectrometry) and ultrasound "
            "measurement (parameters, wave propagation, reflection, transducer fields, Doppler, "
            "diffraction), with 37 figures, 52 equations and 4 tables.")
    crumb = ('<a href="/vi/books/">Sách</a> · <a href="%s">Sổ tay Đo lường, Thiết bị đo và Cảm biến</a> · '
             'Chương 26' % BASE_VI if vi else
             '<a href="/books/">Books</a> · <a href="%s">Measurement, Instrumentation and Sensors '
             'Handbook</a> · Chapter 26' % BASE_EN)
    meta = ("Chương 26 · theo Ch26.pdf (CRC Press, 1999) · 37 hình, 52 phương trình, 4 bảng" if vi else
            "Chapter 26 · 37 figures, 52 equations, 4 tables")
    body = ('<main><article class="intranet-content reader"><div class="reader-hero">'
            '<div class="breadcrumb">%s</div><h1>%s</h1><p class="byline">%s</p>'
            '<div class="meta-line">%s</div></div><div class="prose">%s</div></article></main>'
            % (crumb, TITLE_VI if vi else TITLE_EN, BYLINE, meta,
               body_vi() if vi else body_en()))
    return head(lang, title, desc) + header(lang, switch) + body + footer(lang)


def main():
    pairs = [("en", os.path.join(ROOT, "books", "read", SLUG, CSLUG, "index.html")),
             ("vi", os.path.join(ROOT, "vi", "books", "read", SLUG, CSLUG, "index.html"))]
    for lang, path in pairs:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        page = build(lang)
        open(path, "w", encoding="utf-8").write(page)
        print("wrote %s  %d kB" % (path, len(page) // 1024))


if __name__ == "__main__":
    main()
