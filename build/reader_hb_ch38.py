# -*- coding: utf-8 -*-
"""Handbook Chapter 38 — Current Measurement (Đo dòng điện).

Writes the full Vietnamese translation and the English companion.
Run:  python build/reader_hb_ch38.py
"""
import os
import hb_common as C
from hb_common import p, h2, h3, eq, table

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSLUG = "ch38-current-measurement"
CH_NO = 38
TITLE_EN = "Current Measurement"
TITLE_VI = "Đo dòng điện"
BYLINE = "John G. Webster (chủ biên) · CRC Press, 1999"


def _svg_series():
    return ('<svg viewBox="0 0 520 180" role="img" aria-label="Ampe ke noi tiep">'
            '<style>.w{stroke:#2a2a2a;stroke-width:2;fill:none}'
            '.t{font:12px Inter,Helvetica,sans-serif;fill:#111}'
            '.d{stroke:#b45309;stroke-width:2;fill:none}</style>'
            '<circle cx="70" cy="90" r="26" class="w"/><text x="70" y="95" text-anchor="middle" class="t">E</text>'
            '<line x1="96" y1="90" x2="200" y2="90" class="w"/>'
            '<circle cx="260" cy="90" r="30" class="w"/><text x="260" y="95" text-anchor="middle" class="t">A</text>'
            '<line x1="290" y1="90" x2="420" y2="90" class="w"/>'
            '<line x1="420" y1="90" x2="450" y2="90" class="w"/>'
            '<circle cx="450" cy="90" r="26" class="w"/><text x="450" y="95" text-anchor="middle" class="t">−</text>'
            '<line x1="200" y1="90" x2="200" y2="150" class="d"/><line x1="420" y1="90" x2="420" y2="150" class="d"/>'
            '<line x1="200" y1="150" x2="420" y2="150" class="d"/>'
            '<text x="310" y="172" text-anchor="middle" class="t">Rʟ (tải)</text>'
            '<text x="260" y="55" text-anchor="middle" class="t">Ampe kế nối tiếp (Rₐ nhỏ)</text>'
            '</svg>')


FIGS = {
    1: (_svg_series(),
        "Hình 38.1 · Ampe kế nối tiếp với tải; trở ampe kế gây sụt áp (burden voltage).",
        "Figure 38.1 · An ammeter in series with the load; its resistance causes a voltage burden.",
        "Ampe kế nối tiếp", "Ammeter in series"),
}


fig = C.make_fig(FIGS, CH_NO)


def body_vi():
    b = []
    b.append(p(
        "Dòng điện (current) là tốc độ dịch chuyển điện tích qua một tiết diện, I = dQ/dt, đơn vị ampere "
        "(A) — một ampere bằng một coulomb trên giây. Các thang đo trải từ picoampere (pA, trong rò rỉ và "
        "quang điện) đến kiloampere (kA, trong điện lực). Phép đo dòng là cơ sở của đo công suất, đo điện "
        "năng và nhiều phép đo không điện (cảm biến dòng)."))
    b.append(p(
        "Khác với vôn kế (nối song song), ampe kế (ammeter) phải nối <b>tiếp nối</b> (series) vào mạch để "
        "toàn bộ dòng cần đo chảy qua nó. Vì vậy trở của ampe kế phải nhỏ để không làm thay đổi đáng kể dòng "
        "trong mạch — sai số do <b>gánh áp</b> (burden voltage) là đặc trưng của phép đo dòng."))

    b.append(h2("38.1 Ampe kế kiểu động cơ và mạch chia (shunt)", "Moving-Coil Meters and Shunts"))
    b.append(p(
        "Ampe kế động cơ (D'Arsonval) có cuộn cảm có trở R_a và dòng full-scale I_fs. Để đo dòng lớn hơn, "
        "người ta nối song song một <b>shunt</b> (điện trở chia dòng) R_sh sao cho phần lớn dòng chảy qua "
        "shunt, chỉ I_fs chảy qua đồng hồ:"))
    b.append(eq("R_sh = R_a · I_fs / (I − I_fs)"))
    b.append(p(
        "Shunt thường làm bằng hợp kim manganin (Mn-Cu-Ni) có hệ số nhiệt thấp để giữ độ chính xác theo "
        "nhiệt độ. Sụt áp trên ampe kế là V_burden = I·R_a (hoặc I·R_sh với shunt). Để giảm sai số, ampe "
        "kế chuẩn có gánh áp vài milivôn tới dưới 1 V."))
    b.append(fig(1))

    b.append(h2("38.2 Ampe kế điện tử", "Electronic Ammeters"))
    b.append(p(
        "Ampe kế điện tử dùng bộ khuếch đại thuật toán cấu hình <b>transresistance</b> (I–V converter): dòng "
        "đầu vào chảy qua điện trở hồi tiếp R_f, và điện áp đầu ra V_out = −I_in·R_f. Nhờ có hồi tiếp, đầu "
        "vào几乎 không sụt áp (ảo địa, virtual ground), nên gánh áp cực nhỏ (µV) và dải đo trải từ fA đến "
        "A. Bộ <b>feedback picoammeter/electrometer</b> đo được 10⁻¹⁶ A với trở đầu vào 10¹⁶ Ω."))
    b.append(p(
        "Đối với dòng xoay chiều, đầu ra I–V được chỉnh lưu hoặc đưa vào mạch true-RMS để chỉ thị giá trị "
        "hiệu dụng. Đo dòng một chiều lớn (hàng chục/ampere đến kA) thường dùng shunt có giá trị nhỏ (mΩ) "
        "và đo sụt áp qua nó, hoặc dùng cảm biến dòng (current transducer) cách ly."))

    b.append(h2("38.3 Đo dòng xoay chiều không tiếp xúc", "AC Current: Transformer, Rogowski, Hall"))
    b.append(p(
        "Đo dòng điện lực (AC) thường dùng <b>biến dòng (current transformer, CT)</b>: dây dẫn mang dòng "
        "làm dây sơ cấp một vòng, cuộn thứ cấp có N vòng cho dòng tỉ lệ I_s = I_p/N, cách ly an toàn khỏi "
        "điện áp cao. CT chỉ dùng cho AC và bị bão hòa, méo trên tần số thấp hoặc dòng một chiều."))
    b.append(p(
        "Cuộn <b>Rogowski</b> là một vòng dây mềm quấn quanh dây dẫn; điện áp cảm ứng tỉ lệ với đạo hàm dòng, "
        "và mạch tích phân trả về dòng thực. Nó nhẹ, không bão hòa, đo được xung lớn và dải tần rộng. "
        "Cảm biến hiệu ứng <b>Hall</b> đo được cả DC và AC (dựa trên lực Lorentz lên hạt tải trong từ "
        "trường), là lõi của các <b>ampe kế kẹp (clamp meter)</b> hiện đại."))

    b.append(h2("38.4 Đo dòng nhỏ và dòng lớn", "Low- and High-Current Measurement"))
    b.append(p(
        "<b>Dòng nhỏ (pA–µA):</b> nhiễu rò rỉ và tích điện thống trị. Kỹ thuật: che chắn (guard ring) triệt "
        "dòng qua trở cách điện, vỏ kín nối guard, lấy trung bình nhiều lần, và electrometer đầu vào FET. "
        "<b>Dòng lớn (kA):</b> dùng shunt manganin giá trị rất nhỏ (µΩ) hoặc biến dòng kiểu Hall/quang cách "
        "ly; đo sụt áp hoặc dòng thứ cấp qua ADC."))

    b.append(h2("38.5 Thông số ampe kế", "Ammeter Specifications"))
    b.append(table(
        ["Thông số", "Ý nghĩa", "Điển hình"],
        [["Gánh áp (burden)", "Sụt áp do ampe kế", "< 1 V (chuẩn), µV (điện tử)"],
         ["Trở vào", "Ảnh hưởng mạch đo", "Rất thấp (mV drop)"],
         ["Dải đo", "Từ fA đến kA", "tùy kiểu (shunt / CT / Hall)"],
         ["Độ chính xác", "Sai số full-scale", "0,1% – 1%"],
         ["Băng thông", "Giới hạn tần số", "DC – vài MHz (Rogowski/Hall)"],
         ["Cách ly", "An toàn điện lực", "CT / Hall / quang"]],
        "Bảng 38.1 · Các thông số chính của ampe kế."))

    b.append(h2("Tóm tắt", "Summary"))
    b.append(p(
        "Đo dòng điện nối ampe kế tiếp xúc với mạch; trở ampe kế phải nhỏ để hạn chế gánh áp. Mở rộng dải "
        "bằng shunt (R_sh = R_a·I_fs/(I−I_fs)). Ampe kế điện tử dùng bộ I–V (transresistance) cho gánh áp "
        "µV và dải fA–A. AC dùng biến dòng, Rogowski hoặc Hall; kẹp (clamp) đo không tiếp xúc. Dòng nhỏ "
        "cần electrometer và guard; dòng lớn dùng shunt manganin hoặc transducer cách ly."))
    b.append('<div class="chapter-nav">'
             '<a href="%s"><span class="k">← Mục lục</span>Sổ tay</a>'
             '<a href="%s" style="text-align:right;"><span class="k">Mục lục →</span>Sổ tay</a></div>'
             % (C.BASE_VI, C.BASE_VI))
    return "".join(b)


def body_en():
    b = []
    b.append(p(
        "Companion to the Vietnamese translation of Chapter 38. Figures and tables of the source are "
        "reproduced below; the prose is not repeated."))
    b.append(p(
        "Current I = dQ/dt (ampere = coulomb/second) spans pA (leakage, photo-current) to kA (power). An "
        "ammeter must be in <i>series</i> with the circuit so the full current flows through it, so its "
        "resistance must be small — the <i>voltage burden</i> V_burden = I·R_a is the characteristic error."))
    b.append(fig(1, "en"))
    b.append(p(
        "A moving-coil meter of resistance R_a and full-scale current I_fs is extended with a shunt "
        "R_sh = R_a·I_fs/(I−I_fs) (manganin, low tempco). Electronic ammeters use an op-amp transresistance "
        "converter: V_out = −I_in·R_f, with a virtual ground giving µV burden and a range from fA to A; "
        "feedback picoammeters/electrometers reach 10⁻¹⁶ A. AC current is measured with a current "
        "transformer (CT, AC only, isolated, saturating), a Rogowski coil (flexible, non-saturating, wide "
        "bandwidth, integrated output) or a Hall-effect sensor (DC+AC, the basis of clamp meters)."))
    b.append(p(
        "Low current (pA–µA) needs guarding, shielding and electrometer FET inputs; high current (kA) uses "
        "manganin shunts (µΩ) or isolated Hall/optical transducers. Burden voltage, insertion effect, "
        "frequency response and CMRR are the key error sources."))
    b.append(table(
        ["Parameter", "Meaning", "Typical"],
        [["Burden voltage", "Drop caused by meter", "< 1 V (std), µV (electronic)"],
         ["Input resistance", "Circuit disturbance", "Very low (mV drop)"],
         ["Range", "fA to kA", "shunt / CT / Hall"],
         ["Accuracy", "Error FS", "0.1%–1%"],
         ["Bandwidth", "Freq. limit", "DC – MHz (Rogowski/Hall)"],
         ["Isolation", "Power-safety", "CT / Hall / optical"]],
        "Table 38.1 · Key ammeter specifications."))
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
