# -*- coding: utf-8 -*-
"""Handbook Chapter 43 — Electrical Conductivity and Resistivity (Độ dẫn điện và điện trở suất).
Run:  python build/reader_hb_ch43.py
"""
import os
import hb_common as C
from hb_common import p, h2, h3, eq, table

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSLUG = "ch43-electrical-conductivity-and-resistivity"
CH_NO = 43
TITLE_EN = "Electrical Conductivity and Resistivity"
TITLE_VI = "Độ dẫn điện và điện trở suất"
BYLINE = "John G. Webster (chủ biên) · CRC Press, 1999"
FIGS = {}


def body_vi():
    b = []
    b.append(p(
        "<b>Điện trở suất</b> (resistivity) ρ là đặc trưng của vật liệu, định nghĩa ρ = R·A/l, đơn vị ôm·mét "
        "(Ω·m). <b>Độ dẫn điện</b> (conductivity) σ = 1/ρ, đơn vị siemens/mét (S/m). Đo ρ và σ là cơ sở để "
        "phân loại vật liệu (kim loại, bán dẫn, điện môi), kiểm soát chất lượng và đo nồng độ dung dịch."))
    b.append(p(
        "Với vật liệu đồng nhất, điện trở đo được R = ρ·l/A. Do đó biết hình học (l, A) và đo R sẽ suy ra ρ. "
        "Thực tế, các phương pháp đo dùng điện cực tiếp xúc hoặc trường bốn điểm để loại bỏ ảnh hưởng của điện "
        "tiếp xúc."))

    b.append(h2("43.1 Cầu Wheatstone và đo trở hai điểm", "Two-Terminal and Wheatstone Bridge"))
    b.append(p(
        "Với mẫu có trở lớn (MΩ–GΩ), đo trực tiếp bằng vôn kế/ampe kế (R = V/I) hoặc cầu Wheatstone cân bằng. "
        "Tuy nhiên, với mẫu trở thấp, điện trở dây dẫn và tiếp xúc gây sai số lớn, nên dùng phương pháp bốn "
        "điểm."))

    b.append(h2("43.2 Phương pháp bốn điểm (four-point probe)", "Four-Point Probe"))
    b.append(p(
        "Bốn kim dò thẳng hàng, cách đều s, tiếp xúc với bề mặt mẫu. Dòng I chạy qua hai kim ngoài, và điện "
        "áp V đo giữa hai kim trong. Với mẫu bán cản nửa không gian (semi-infinite), điện trở suất bề mặt "
        "sheet resistance R_s và ρ liên hệ:"))
    b.append(eq("ρ = 2π·s·(V/I)   (mẫu dày) ;   R_s = (π/ln 2)·(V/I) ≈ 4,53·(V/I)   (màng mỏng)"))
    b.append(p(
        "Phương pháp này loại bỏ điện trở tiếp xúc vì dòng và áp đo ở các kim khác nhau. Dùng rộng rãi cho "
        "wafer bán dẫn và màng mỏng."))

    b.append(h2("43.3 Phương pháp Van der Pauw", "Van der Pauw Method"))
    b.append(p(
        "Với mẫu dạng đĩa/màng mỏng bất kỳ (miễn không có lỗ), đặt bốn tiếp điểm ở rìa, đo hai cặp điện trở "
        "R_AB,CD và R_BC,DA rồi giải:"))
    b.append(eq("exp(−π·R_AB,CD/R_s) + exp(−π·R_BC,DA/R_s) = 1   ⇒   R_s, từ đó ρ = R_s·t (t = độ dày)"))
    b.append(p(
        "Van der Pauw cho độ chính xác cao mà không cần biết hình dạng mẫu, rất phổ biến trong vật lý bán dẫn."))

    b.append(h2("43.4 Đo độ dẫn dung dịch (conductivity cell)", "Solution Conductivity"))
    b.append(p(
        "Độ dẫn điện của dung dịch đo bằng <b>cell dẫn điện</b>: hai điện cực trong mẫu, điện trở đo được "
        "R = K/σ với <b>hằng số cell</b> K = l/A (m⁻¹). Do đó σ = K/R. K được xác định bằng hiệu chuẩn với "
        "dung dịch chuẩn (KCl). Đo dùng cầu hoặc oscillator AC (tránh phân cực điện cực), thường ở 1–10 kHz."))
    b.append(p(
        "Độ dẫn phụ thuộc nhiệt độ mạnh (hệ số ~2%/°C cho nước), nên máy đo tích hợp đầu dò nhiệt để bù, quy "
        "về 25 °C. Ứng dụng: kiểm soát nước thải, nước tinh khiết, nồng độ acid/base, môi trường nuôi cấy."))

    b.append(h2("43.5 Thông số", "Specifications"))
    b.append(table(
        ["Phương pháp", "Vật liệu", "Dải", "Độ chính xác"],
        [["Cầu Wheatstone", "Điện trở tổng", "Ω–MΩ", "0,1%"],
         ["Bốn điểm", "Bán dẫn, màng", "10⁻⁴–10³ Ω·□", "1%–5%"],
         ["Van der Pauw", "Màng mỏng bất kỳ", "10⁻⁴–10⁴ Ω·□", "1%–2%"],
         ["Cell dẫn điện", "Dung dịch", "µS–S/cm", "0,5%–2%"],
         ["Electrometer", "Cách điện cực cao", "10¹²–10¹⁸ Ω·m", "phụ thuộc"]],
        "Bảng 43.1 · Các phương pháp đo ρ, σ."))

    b.append(h2("Tóm tắt", "Summary"))
    b.append(p(
        "Điện trở suất ρ = R·A/l, độ dẫn σ = 1/ρ. Mẫu trở thấp/trung bình dùng bốn điểm (ρ = 2πs·V/I) hoặc "
        "Van der Pauw để loại bỏ điện trở tiếp xúc. Dung dịch đo bằng cell dẫn điện với σ = K/R (K là hằng "
        "số cell), dùng AC tránh phân cực và bù nhiệt độ. Các phương pháp này phân biệt vật liệu và đo nồng "
        "độ dung dịch."))
    b.append('<div class="chapter-nav">'
             '<a href="%s"><span class="k">← Mục lục</span>Sổ tay</a>'
             '<a href="%s" style="text-align:right;"><span class="k">Mục lục →</span>Sổ tay</a></div>'
             % (C.BASE_VI, C.BASE_VI))
    return "".join(b)


def body_en():
    b = []
    b.append(p(
        "Companion to the Vietnamese translation of Chapter 43. Equations and table of the source are "
        "reproduced below; the prose is not repeated."))
    b.append(p(
        "Resistivity ρ = R·A/l (Ω·m); conductivity σ = 1/ρ (S/m). For uniform samples R = ρ·l/A. Low-resistance "
        "materials need contact-resistance-free methods. The four-point probe passes current I through the two "
        "outer of four collinear equidistant probes (spacing s) and measures V across the inner pair: for a "
        "semi-infinite sample ρ = 2πs(V/I), and for a thin film the sheet resistance R_s ≈ 4.53·(V/I). Van der "
        "Pauw measures two resistance pairs on any arbitrarily-shaped thin sample (no holes) and solves "
        "exp(−πR₁/R_s)+exp(−πR₂/R_s)=1 for R_s, then ρ = R_s·t — shape-independent, widely used in "
        "semiconductor physics. Solution conductivity uses a conductivity cell where R = K/σ, K = l/A the cell "
        "constant, so σ = K/R; measured with an AC bridge/oscillator (1–10 kHz) to avoid electrode "
        "polarization and temperature-compensated (≈2%/°C)."))
    b.append(table(
        ["Method", "Material", "Range", "Accuracy"],
        [["Wheatstone", "General R", "Ω–MΩ", "0.1%"],
         ["Four-point", "Semi., film", "10⁻⁴–10³ Ω/□", "1%–5%"],
         ["Van der Pauw", "Any thin film", "10⁻⁴–10⁴ Ω/□", "1%–2%"],
         ["Cond. cell", "Solution", "µS–S/cm", "0.5%–2%"],
         ["Electrometer", "High-insul.", "10¹²–10¹⁸ Ω·m", "varies"]],
        "Table 43.1 · Resistivity/conductivity methods."))
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
