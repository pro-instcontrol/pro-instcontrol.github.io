# -*- coding: utf-8 -*-
"""Handbook Chapter 92 — Liquid Crystal Displays (Kalluri R. Sarma, Honeywell).

Writes the full Vietnamese translation and the English companion.
Figures: hb92fig.py (92.1–92.6), hb92figb.py (92.7–92.12), hb92figc.py (92.13–92.16).
Run:  python build/reader_hb_ch92.py
"""
import os

import hb92fig as A
import hb92figb as B
import hb92figc as C
from reader_handbook import SLUG, head, header, footer
from chapter_nav import nav as chapter_nav

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSLUG = "ch92-liquid-crystal-displays"
TITLE_EN = "Liquid Crystal Displays"
TITLE_VI = "Màn hình tinh thể lỏng"
BYLINE = "Kalluri R. Sarma — Honeywell, Inc."
BYLINE_EN = "Kalluri R. Sarma, Honeywell, Inc."
BASE_EN = "/books/read/%s/" % SLUG
BASE_VI = "/vi/books/read/%s/" % SLUG

FIGS = {n: getattr(A, "fig_92_%d" % n) for n in range(1, 7)}
FIGS.update({n: getattr(B, "fig_92_%d" % n) for n in range(7, 13)})
FIGS.update({n: getattr(C, "fig_92_%d" % n) for n in range(13, 17)})


def fig(num, lang="vi"):
    svg, cap_vi, cap_en, _av, _ae = FIGS[num]()
    return ('<figure class="figure" id="fig-92-%d">%s<figcaption class="figcap">%s</figcaption>'
            '</figure>' % (num, svg, cap_vi if lang == "vi" else cap_en))


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


def refs(items):
    return '<ol class="ref-list">%s</ol>' % "".join("<li>%s</li>" % i for i in items)


# ================================================================ EQUATIONS
_EQ = {
    "92.1": ("<i>S</i> = ½⟨3cos²θ − 1⟩"),
    "92.2": ("<i>S</i> = (1 − <i>T</i>/<i>T</i><sub>c</sub>)<sup>β</sup>"),
    "92.3": ("Δε = ε<sub>∥</sub> − ε<sub>⊥</sub>"),
    "92.4": ("Δ<i>n</i> = <i>n</i><sub>∥</sub> − <i>n</i><sub>⊥</sub> = "
             "<i>n</i><sub>e</sub> − <i>n</i><sub>o</sub>"),
    "92.5": ("<i>n</i><sub>o,e</sub> = <i>n</i><sub>∞</sub> + α/λ²"),
    "92.6": ("<i>F</i> = ½[<i>K</i><sub>11</sub>(∇·<b>n</b>)² + "
             "<i>K</i><sub>22</sub>(<b>n</b>·∇×<b>n</b>)² + "
             "<i>K</i><sub>33</sub>(<b>n</b>×∇×<b>n</b>)²]"),
    "92.7": ("<i>K</i><sub>ii</sub> ∝ <i>S</i>²"),
    "92.8": ("<i>f</i><sub>e</sub> = −½ε<sub>⊥</sub><i>E</i>² − "
             "½Δε(<b>n</b>·<b>E</b>)²"),
    "92.9": ("<i>E</i><sub>c</sub> = (π/<i>d</i>)√[<i>K</i><sub>ii</sub>/"
             "(ε<sub>0</sub>Δε)]"),
    "92.10": ("<i>V</i><sub>th</sub> = <i>E</i><sub>c</sub><i>d</i> = "
              "π√[<i>K</i><sub>ii</sub>/(ε<sub>0</sub>Δε)]"),
    "92.11": ("<i>V</i><sub>th</sub> = π√[<i>K</i><sub>ii</sub>/(ε<sub>0</sub>Δε)], "
              "<i>K</i><sub>ii</sub> = <i>K</i><sub>11</sub> + "
              "(<i>K</i><sub>33</sub> − 2<i>K</i><sub>22</sub>)/4"),
    "92.12": ("τ<sub>r</sub> = γ<i>d</i>²/[ε<sub>0</sub>Δε(<i>V</i>² − "
              "<i>V</i><sub>th</sub>²)]"),
    "92.13": ("τ<sub>d</sub> = γ<i>d</i>²/[ε<sub>0</sub>Δε<i>V</i><sub>th</sub>²]"),
    "92.14": ("<i>V</i><sub>on</sub>/<i>V</i><sub>off</sub> = "
              "(√<i>N</i> + 1)/(√<i>N</i> − 1)"),
    "92.15": ("<i>I</i> = <i>I</i><sub>0</sub> sin²(2φ)·sin²[π<i>d</i>Δ<i>n</i>(<i>V</i>)/λ]"),
    "92.16": ("Δ<i>V</i><sub>p</sub> = [<i>C</i><sub>gd</sub>/(<i>C</i><sub>gd</sub> + "
              "<i>C</i><sub>LC</sub> + <i>C</i><sub>S</sub>)]·Δ<i>V</i><sub>g</sub>"),
}


def _eq(num):
    return _EQ[num]


# ================================================================ REFERENCES
_REFS = [
    "P.J. Collings, <i>Liquid Crystals: Nature's Delicate Phase Matter</i>, Princeton University "
    "Press, Princeton, NJ, 1990.",
    "L.M. Blinov and V.G. Chigrinov, <i>Electro-optical Effects in Liquid Crystal Materials</i>, "
    "Springer, New York, 1996.",
    "P.G. De Gennes and J. Prost, <i>The Physics of Liquid Crystals</i>, 2nd ed., Clarendon Press, "
    "Oxford, 1993.",
    "B. Bahadur, Ed., <i>Liquid Crystals: Applications and Uses</i>, World Scientific, Singapore, "
    "1990.",
    "E. Kaneko, <i>Liquid Crystal TV Displays: Principles and Applications of Liquid Crystal "
    "Displays</i>, D. Reidel Publishing, Boston, 1987.",
    "T. Tsukada, <i>TFT/LCD: Liquid Crystal Display Addressed by Thin Film Transistors</i>, Gordon "
    "and Breach, Canada, 1996.",
    "E. Lueder, Fundamentals of passive and active addressed liquid crystal displays, Short Course "
    "S-1, SID Conference, San Diego, CA, May 12, 1996.",
    "P.W. Ross, L.K.M. Chan, and P.W. Surguy, Ferroelectric LCD: simplicity and versatility, "
    "<i>SID '94 Digest</i>, 147–150, 1996.",
    "J.W. Doane, D.K. Yang, and Z. Yaniv, Front-lit flat panel display for polymer stabilized "
    "cholesteric textures, <i>Proc. 12th International Display Conference, Japan Display '92</i>, "
    "Oct. 12–14, 73–76, 1992.",
    "J.C. Rowell, W.D. Phillips, L.R. Melby, and M. Panar, NMR studies of some liquid crystal "
    "systems, <i>J. Chem. Phys.</i>, 43, 3442–3454, 1965.",
    "L. Pohl and E. Merck, Physical properties of liquid crystals, in <i>Liquid Crystals: "
    "Applications and Uses</i>, B. Bahadur, Ed., World Scientific, Singapore, 1990, 139–170.",
    "P.R. Kishore, N.V.S. Rao, P.B.K. Sarma, T.F.S. Raj, M.N. Avadhanlu, and C.R.K. Murty, Field "
    "and frequency effects in nematic mixtures of negative and positive dielectric anisotropy, "
    "<i>Mol. Cryst. Liq. Cryst.</i>, 45, 3/4, 231–241, 1978.",
    "D. Lippens, J.P. Parneix, and A. Chapoton, Study of 4-heptyl 4′-cyanobiphenyl using the "
    "analysis of its dielectric properties, <i>J. Phys.</i>, 38, 1465, 1977.",
    "F.C. Frank, On the theory of liquid crystals, <i>Discuss. Faraday Soc.</i>, 25, 19, 1958.",
    "W.H. de Jeu, <i>Physical Properties of Liquid Crystalline Materials</i>, Gordon and Breach, "
    "New York, 1980.",
    "J.J. Wysocki, A. Adams, and W. Haas, Electric-field-induced phase change in cholesteric liquid "
    "crystals, <i>Phys. Rev. Lett.</i>, 20, 1024, 1968.",
    "G.H. Heilmeier, L.A. Zanoni, and L.A. Barton, Dynamic scattering: a new electro-optic effect "
    "in certain classes of nematic liquid crystals, <i>Proc. IEEE</i>, 56, 1162, 1968.",
    "G.H. Heilmeier and L.A. Zanoni, Guest-host interaction in nematic liquid crystal — a new "
    "electro-optic effect, <i>Appl. Phys. Lett.</i>, 13, 91, 1968.",
    "M. Schadt and W. Helfrich, Voltage-dependent optical activity of a twisted nematic liquid "
    "crystal, <i>Appl. Phys. Lett.</i>, 18, 127, 1971.",
    "M.F. Schiekel and K. Fahrenschon, Deformation of nematic liquid crystal with vertical "
    "orientation in electric fields, <i>Appl. Phys. Lett.</i>, 19, 391, 1971.",
    "M. Hareng, G. Assouline, and E. Leiba, Liquid crystal matrix display by electrically "
    "controlled birefringence, <i>Proc. IEEE</i>, 60, 913, 1972.",
    "C.H. Gooch and H.A. Tarry, The optical properties of twisted nematic liquid crystal "
    "structures with twist angles ≤ 90°, <i>J. Phys. D: Appl. Phys.</i>, 8, 1575–1584, 1975.",
    "E. Jakeman and E.P. Raynes, Electro-optical response times in liquid crystals, <i>Phys. "
    "Lett.</i>, 39A, 69–70, 1972.",
    "P.M. Alt and P. Pleshko, Scanning limitations of liquid-crystal displays, <i>IEEE Trans. "
    "Electron Dev.</i>, ED-21, 146, 1974.",
    "T.J. Scheffer and J. Nerring, A new highly multiplexable liquid crystal display, <i>Appl. "
    "Phys. Lett.</i>, 45, 1021, 1984.",
    "T.J. Scheffer, Super Twisted Nematic (STN) LCDs, <i>SID '95 Seminar Notes</i>, Vol. I, M-2, "
    "1995.",
    "M. Oh-e, M. Ohta, S. Aratani, and K. Kondo, Principles and characteristics of electro-optical "
    "behavior of in-plane switching mode, <i>Proc. 15th International Display Research Conf., Asia "
    "Display '95</i>, 577–580, 1995.",
    "T. Scheffer and B. Clifton, Active addressing method for high-contrast video-rate STN "
    "displays, <i>SID '92 Digest</i>, 228, 1992.",
    "H. Muraji et al., A 9.4-in. color VGA F-STN display with fast response time and high contrast "
    "ratio by using MLS method, <i>SID '94 Dig.</i>, 61, 1994.",
    "Higashi et al., A 1.8-in. poly-Si TFT-LCD for HDTV projectors with 5 V fully integrated "
    "driver, <i>SID '95 Dig.</i>, 81, 1995.",
]


# ================================================================ VIETNAMESE
def body_vi():
    b = []

    b.append(note(
        "<b>Ghi chú của người dịch.</b> Bản in gốc (CRC Press, 1999) có vài lỗi đã được sửa "
        "trong bản dịch này. Khe cell được in là “5 đến 10 mm” và bề dày kính lọc màu là “2 mm”, "
        "nhưng theo ngữ cảnh phải là µm; các chỗ này đã đổi sang µm. Thời gian đáp ứng được in là "
        "“tr, tf” trong khi văn bản nói tới thời gian tăng và thời gian giảm; ký hiệu đúng là "
        "τ<sub>r</sub> và τ<sub>d</sub>, và phương trình 92.13 là của τ<sub>d</sub>. Các phương "
        "trình 92.9–92.13 bị OCR làm hỏng và đã được khôi phục về dạng Freedericksz và "
        "Jakeman–Raynes chuẩn. Chú thích Hình 92.3 in “P = azoxy anisole (PPA)” trong khi văn bản "
        "dùng PAA (p-azoxyanisole)."))

    # ------------------------------------------------------------ 92.1
    b.append(h2("92.1 Giới thiệu", "Introduction"))
    b.append(p(
        "Tinh thể lỏng (LC) là một lớp vật liệu quan trọng, được dùng từ thiết bị hiển thị, thiết "
        "bị quang điện tử, cảm biến cho tới vật liệu sinh học và vật liệu kết cấu. Chương này chỉ "
        "bàn tới LC cho ứng dụng hiển thị. Nói chung, hầu hết các chất có một điểm nóng chảy duy "
        "nhất: một chất rắn có trật tự vị trí và trật tự định hướng, khi nóng chảy thì chuyển thành "
        "chất lỏng đẳng hướng không có cả trật tự vị trí lẫn trật tự định hướng. Tuy vậy, một số "
        "vật liệu khi nóng chảy từ trạng thái rắn lại chuyển thành một chất lỏng đục, có trật tự "
        "định hướng, ở một nhiệt độ nào đó; nếu tiếp tục nung nóng, chúng chuyển thành chất lỏng "
        "đẳng hướng không còn trật tự, như trên Hình 92.1."))
    b.append(fig(1))
    b.append(p(
        "Như vậy, LC là một pha trung gian (mesophase) tồn tại giữa nhiệt độ nóng chảy "
        "<i>T</i><sub>m</sub> của pha tinh thể và điểm trong <i>T</i><sub>c</sub> của pha lỏng: "
        "dưới <i>T</i><sub>m</sub> vật liệu ở pha tinh thể, trên <i>T</i><sub>c</sub> ở pha lỏng "
        "(đẳng hướng), còn giữa <i>T</i><sub>m</sub> và <i>T</i><sub>c</sub> thì ở pha tinh thể "
        "lỏng. Loại LC có pha trung gian được xác định bởi nhiệt độ như vậy gọi là LC nhiệt biến "
        "(thermotropic). Khi pha trung gian được xác định bởi nồng độ dung môi, người ta gọi là LC "
        "dung biến (lyotropic). LC dùng cho hiển thị là loại nhiệt biến. Trật tự định hướng trong "
        "vật liệu LC tạo ra những tính chất vật lý quan trọng, chẳng hạn lưỡng chiết, khiến vật "
        "liệu này hữu ích cho thiết bị hiển thị."))
    b.append(p(
        "Nhờ các đặc tính điện áp điều khiển thấp, công suất tiêu thụ thấp, dạng mỏng (màn hình "
        "phẳng), khối lượng nhẹ, màu đầy đủ, thang xám với dải động rộng, video chuyển động đầy "
        "đủ, chất lượng hình ảnh cao và độ tin cậy cao, màn hình tinh thể lỏng (LCD) là lựa chọn "
        "hàng đầu cho các ứng dụng chạy pin (xách tay), từ mặt đồng hồ, TV cầm tay đến màn hình "
        "máy tính xách tay. LCD cũng đang thay thế ống tia cathode (CRT) trong một số ứng dụng như "
        "màn hình hàng không, nhờ độ chói cao và khả năng đọc tốt dưới ánh sáng mặt trời."))
    b.append(p(
        "LC còn được dùng trong thiết bị hiển thị chiếu, cho màn hình gắn đầu (HMD) và cho màn hình "
        "lớn. Phần tiếp theo sẽ trình bày các loại vật liệu LC, tính chất của chúng, vật liệu và "
        "quy trình chế tạo LCD, các chế độ hiển thị LCD và các phương pháp quét địa chỉ. Có nhiều "
        "tài liệu tham khảo tốt, chẳng hạn các tài liệu 1–7, về LC và LCD. Vào thời điểm viết, "
        "công nghệ LCD đang tiến rất nhanh về góc nhìn, chất lượng hình ảnh, công suất tiêu thụ và "
        "kích thước màn hình. Tuy vậy, mục đích của chương này là trình bày các nguyên lý và công "
        "nghệ LCD cơ bản, chứ không phải điểm lại trình độ tiên tiến nhất."))

    # ------------------------------------------------------------ 92.2
    b.append(h2("92.2 Các loại vật liệu tinh thể lỏng", "Types of Liquid Crystal Materials"))
    b.append(p(
        "Phần lớn vật liệu LC là hợp chất hữu cơ gồm các phân tử hình que hoặc hình đĩa. Cho ứng "
        "dụng hiển thị, vật liệu LC có phân tử hình que được dùng phổ biến nhất. Theo trật tự phân "
        "tử, vật liệu LC được chia thành ba loại (pha) — smectic, nematic và cholesteric — như trên "
        "Hình 92.2. Trong tinh thể lỏng smectic, các phân tử hình que xếp thành lớp, các phân tử "
        "song song với nhau. Có nhiều pha smectic khác nhau, nhưng smectic A và smectic C là phổ "
        "biến nhất. Ở smectic A, trục phân tử (director) vuông góc với các lớp (Hình 92.2a); ở "
        "smectic C, trục này nghiêng một góc so với pháp tuyến của lớp (Hình 92.2b)."))
    b.append(fig(2))
    b.append(p(
        "Ở LC nematic, các phân tử hình que song song với nhau nhưng từng phân tử có thể chuyển "
        "động tương đối dễ dàng theo hướng trục của chúng, không có cấu trúc lớp (Hình 92.2c). Ở "
        "LC cholesteric, các phân tử xếp thành lớp như smectic, nhưng trục phân tử nằm trong mặt "
        "phẳng của mỗi lớp (Hình 92.2d); ngoài ra LC cholesteric có cấu trúc xoắn, trong đó "
        "director <b>n</b> đổi hướng từ lớp này sang lớp khác. Cùng một vật liệu LC có thể có các "
        "pha khác nhau ở các nhiệt độ khác nhau: chẳng hạn ở nhiệt độ thấp hơn nó có pha smectic "
        "C, khi tăng nhiệt độ chuyển sang smectic A rồi nematic, trước khi thành chất lỏng đẳng "
        "hướng ở <i>T</i><sub>c</sub>."))
    b.append(p(
        "LC nematic là nền tảng của phần lớn LCD ma trận chủ động dùng nematic xoắn (TN) và LCD "
        "ma trận thụ động dùng nematic xoắn siêu cao (STN) được dùng rộng rãi. Một ví dụ của màn "
        "hình dùng LC smectic C là LCD sắt điện quét địa chỉ ma trận thụ động [8]. Một ví dụ của "
        "màn hình cholesteric là màn hình cấu trúc cholesteric ổn định (SCT) quét địa chỉ ma trận "
        "thụ động, có tính lưỡng ổn [9]. Một ví dụ kinh điển của vật liệu LC nematic là "
        "p-azoxyanisole (PAA), có pha nematic trong khoảng 117 đến 136 °C."))
    b.append(p(
        "Trong PAA, hai vòng benzen gần như đồng phẳng, thanh cứng dài khoảng 20 Å và rộng 5 Å. "
        "Một ví dụ lịch sử khác của LC nematic là N-(p-methoxybenzylidene-p-butylaniline) (MBBA), "
        "có pha nematic trong khoảng 22 đến 47 °C."))
    b.append(p(
        "MBBA có một nhóm trung tâm nối chặt hai lõi dạng vòng và giữ cho toàn bộ phân tử LC thẳng. "
        "Các nhóm tận cùng và các liên kết liên hợp trong lõi chịu trách nhiệm chính cho tính chất "
        "điện môi, quang học và các tính chất dị hướng khác của vật liệu. Các hợp chất azoxy và "
        "base Schiff thuộc nhóm vật liệu được dùng sớm nhất trong LCD. Vì vấn đề ổn định môi "
        "trường, chúng được thay bằng vật liệu biphenyl. Gần đây, các hợp chất phenylcyclohexane, "
        "bicyclohexane và estercyclohexane được phát triển để đáp ứng yêu cầu làm việc ở dải nhiệt "
        "độ rộng và tính chất quang điện tốt hơn. Vật liệu LC dùng trong LCD hiện nay là hỗn hợp "
        "tinh luyện của nhiều hợp chất, được điều chỉnh để đạt độ ổn định môi trường, dải nhiệt độ "
        "làm việc rộng, đáp ứng thích hợp với điện trường đặt vào, điện trở suất cao cho quét địa "
        "chỉ ma trận và thời gian đáp ứng nhanh."))
    b.append(p(
        "Mức độ trật tự trong LC là một thông số quan trọng, được xác định bởi thông số trật tự "
        "<i>S</i>:"))
    b.append(eq(_eq("92.1"), "92.1"))
    b.append(p(
        "trong đó θ là góc giữa trục phân tử và hướng phân tử ưu tiên <b>n</b>. Ký hiệu ⟨ ⟩ là lấy "
        "trung bình trên toàn không gian. Hướng phân tử ưu tiên, gọi là director <b>n</b> của LC, "
        "được định nghĩa là hướng sắp xếp trung bình của trục dài phân tử. Với trật tự định hướng "
        "hoàn hảo — mọi phân tử song song với director, như trong tinh thể hoàn hảo — θ = 0 và do "
        "đó <i>S</i> = 1. Với trật tự định hướng bằng không — hướng phân tử hoàn toàn ngẫu nhiên, "
        "như trong chất lỏng đẳng hướng — <i>S</i> = 0. Ở LC nematic điển hình, <i>S</i> nằm trong "
        "khoảng 0,3 đến 0,7; ở LC smectic điển hình, <i>S</i> trong khoảng 0,7 đến 0,8, với giá trị "
        "cao hơn ở nhiệt độ thấp hơn. Hình 92.3 cho thấy sự phụ thuộc nhiệt độ của <i>S</i> đối "
        "với vật liệu LC PAA [10]. Thông số trật tự giảm nhanh tới khoảng 0,3 khi gần điểm trong "
        "<i>T</i><sub>c</sub>, và bằng không ở trạng thái đẳng hướng."))
    b.append(fig(3))
    b.append(p(
        "Sự phụ thuộc chính xác của <i>S</i> vào nhiệt độ <i>T</i> tuỳ thuộc loại phân tử; tuy "
        "vậy, biểu thức giải tích sau đây, rút ra từ lý thuyết, tỏ ra hữu ích [11]:"))
    b.append(eq(_eq("92.2"), "92.2"))
    b.append(p(
        "trong đó <i>T</i><sub>c</sub> ứng với chuyển pha nematic–đẳng hướng, β là số mũ trong "
        "khoảng 0,13 đến 0,18 tuỳ vật liệu. (Bản in còn đưa vào một hệ số γ cỡ 0,98; dạng chuẩn "
        "của Haller được dùng ở đây.)"))

    # ------------------------------------------------------------ 92.3
    b.append(h2("92.3 Tính chất vật lý của tinh thể lỏng",
                "Physical Properties of Liquid Crystals"))
    b.append(p(
        "Do cấu trúc trật tự với các phân tử sắp xếp theo trục dài song song với nhau, phân tử LC "
        "thể hiện tính chất dị hướng: nhiều đại lượng vật lý như hằng số điện môi ε, chiết suất "
        "<i>n</i>, độ từ cảm χ, độ dẫn điện σ và độ nhớt η có giá trị khác nhau theo hướng song "
        "song (∥) và vuông góc (⊥) với trục phân tử. Tính dị hướng này, cùng với khả năng điều "
        "khiển dễ dàng hướng ban đầu (điều kiện biên) bằng định hướng bề mặt và khả năng định "
        "hướng lại trục phân tử bằng điện áp đặt vào, là cơ sở để dùng LC cho hiển thị. Phần này "
        "bàn về dị hướng của hằng số điện môi và chiết suất, các hằng số đàn hồi và đặc trưng "
        "quang điện — những yếu tố quan trọng khi dùng LC cho hiển thị."))

    b.append(h3("Dị hướng điện môi", "Dielectric Anisotropy"))
    b.append(p(
        "Phân tử LC thể hiện dị hướng điện môi do các lưỡng cực vĩnh cửu và cảm ứng. Dị hướng điện "
        "môi Δε được biểu diễn:"))
    b.append(eq(_eq("92.3"), "92.3"))
    b.append(p(
        "trong đó ε<sub>∥</sub> và ε<sub>⊥</sub> là hằng số điện môi đo theo hướng song song và "
        "vuông góc với director. Vật liệu có dị hướng điện môi dương (Δε > 0) gọi là vật liệu "
        "p-type; vật liệu có dị hướng điện môi âm (Δε < 0) gọi là n-type. LC p-type có xu hướng "
        "sắp trục phân tử song song với điện trường đặt vào, còn LC n-type sắp trục phân tử vuông "
        "góc với điện trường."))
    b.append(p(
        "Nói chung, hằng số điện môi ε<sub>∥</sub> giảm khi tần số tăng [12] do hiện tượng hồi "
        "phục (relaxation); trong khi ε<sub>⊥</sub> không phụ thuộc tần số trên một dải tần rộng. "
        "Ở tần số giao thoa <i>f</i><sub>c</sub>, nơi ε<sub>∥</sub> = ε<sub>⊥</sub>, vật liệu LC "
        "trở nên đẳng hướng. Tuỳ vật liệu, <i>f</i><sub>c</sub> nằm trong khoảng 100 kHz đến hơn "
        "1 MHz. Các hằng số điện môi cũng thay đổi theo nhiệt độ [13], như trên Hình 92.4 đối với "
        "LC nematic cyanobiphenyl. Hai hằng số điện môi hội tụ nhanh khi nhiệt độ tiến tới "
        "<i>T</i><sub>c</sub>, nơi ε<sub>∥</sub> = ε<sub>⊥</sub> = ε<sub>đẳng hướng</sub>."))
    b.append(fig(4))

    b.append(h3("Dị hướng chiết suất", "Refractive Index Anisotropy"))
    b.append(p(
        "LC là vật liệu lưỡng chiết với chiết suất dị hướng. Nó có hai chiết suất chính "
        "<i>n</i><sub>o</sub> và <i>n</i><sub>e</sub>, như trên Hình 92.5. Với chiết suất thường "
        "<i>n</i><sub>o</sub>, vectơ điện trường của chùm sáng dao động vuông góc với trục quang; "
        "với chiết suất dị thường <i>n</i><sub>e</sub>, vectơ điện trường dao động song song với "
        "trục quang. Ở LC nematic và smectic, hướng của director <b>n</b> là trục quang của tinh "
        "thể đơn trục, nên chiết suất cho tia sáng dao động theo hướng song song và vuông góc với "
        "director lần lượt là <i>n</i><sub>∥</sub> và <i>n</i><sub>⊥</sub>, tức "
        "<i>n</i><sub>o</sub> = <i>n</i><sub>⊥</sub>, <i>n</i><sub>e</sub> = "
        "<i>n</i><sub>∥</sub>, và dị hướng quang hay lưỡng chiết Δ<i>n</i> là:"))
    b.append(eq(_eq("92.4"), "92.4"))
    b.append(fig(5))
    b.append(p(
        "Hình 92.6a và b cho thấy sự phụ thuộc nhiệt độ [2] và phụ thuộc bước sóng [2] của chiết "
        "suất ở các vật liệu LC điển hình. Sự phụ thuộc của chiết suất vào bước sóng λ thường được "
        "biểu diễn bằng phương trình Cauchy:"))
    b.append(eq(_eq("92.5"), "92.5"))
    b.append(p(
        "trong đó <i>n</i><sub>∞</sub> là chiết suất ngoại suy tới bước sóng vô hạn và α là hệ số "
        "đặc trưng cho vật liệu."))
    b.append(fig(6))

    b.append(h3("Hằng số đàn hồi", "Elastic Constants"))
    b.append(p(
        "Ở LC đơn trục, hướng ưu tiên (cân bằng) của phân tử LC được cho bởi director <b>n</b>, có "
        "thể do xử lý bề mặt ở điều kiện biên hoặc do trường ngoài áp đặt. Khi LC bị nhiễu khỏi "
        "trạng thái cân bằng do đặt vào hoặc gỡ bỏ trường ngoài, lực đàn hồi và lực điện quyết "
        "định dạng biến dạng tĩnh của LC. Sự chuyển hướng của director từ hướng này sang hướng "
        "khác gây ra biến dạng uốn trong môi trường. Frank [14] chỉ ra rằng một trạng thái biến "
        "dạng bất kỳ có thể xem là tổ hợp của ba phép cơ bản: splay (toả), twist (xoắn) và bend "
        "(uốn), với các hằng số đàn hồi <i>K</i><sub>11</sub>, <i>K</i><sub>22</sub>, "
        "<i>K</i><sub>33</sub> theo ký hiệu của lý thuyết Oseen–Frank. Hình 92.7 minh hoạ ba kiểu "
        "biến dạng này. Phần đàn hồi của năng lượng tự do bên trong <i>F</i> của tinh thể lỏng bị "
        "nhiễu được cho bởi:"))
    b.append(eq(_eq("92.6"), "92.6"))
    b.append(p(
        "Như vậy mật độ năng lượng tự do là hàm bậc hai của các biến dạng uốn, với các hằng số "
        "đàn hồi đóng vai trò hệ số tỉ lệ. Các hằng số đàn hồi phụ thuộc nhiệt độ và giảm khi "
        "nhiệt độ tăng. Độ lớn của chúng có thể xấp xỉ [15] bởi:"))
    b.append(eq(_eq("92.7"), "92.7"))
    b.append(fig(7))

    b.append(h3("Đặc trưng quang điện", "Electro-Optical Characteristics"))
    b.append(p(
        "Khi đặt điện trường vào LC có hướng phân tử (director) ban đầu, hướng này sẽ chuyển sang "
        "một hướng mới do dị hướng điện môi (Δε = ε<sub>∥</sub> − ε<sub>⊥</sub>) của LC. Sự thay "
        "đổi hướng phân tử này kéo theo sự thay đổi đặc trưng truyền/phản xạ quang của LC — cơ sở "
        "của LCD. Hiện tượng điều biến quang bằng điện này gọi là hiệu ứng quang điện của LC. Khi "
        "đặt điện trường <b>E</b> vào LC, nó sinh ra năng lượng điện <i>f</i><sub>e</sub>:"))
    b.append(eq(_eq("92.8"), "92.8"))
    b.append(p(
        "Hướng phân tử ban đầu (điều kiện biên đạt được bằng định hướng bề mặt) của phân tử LC "
        "(director <b>n</b>) hoặc song song (với Δε > 0) hoặc vuông góc (với Δε < 0) với mặt phẳng "
        "hai điện cực song song của màn hình. Khi đặt trường giữa hai điện cực song song có LC ở "
        "giữa, director <b>n</b> định hướng song song với điện trường <b>E</b> ở vật liệu Δε "
        "dương, và vuông góc với trường ở vật liệu Δε âm. Năng lượng tự do tổng <i>F</i> của LC "
        "khi hướng phân tử ban đầu chưa biến dạng bị biến dạng do trường đặt vào bằng tổng năng "
        "lượng điện <i>f</i><sub>e</sub> và năng lượng đàn hồi. Sự chuyển từ trạng thái chưa biến "
        "dạng này, gọi là chuyển pha Freedericksz, xảy ra khi trường tăng tới trường tới hạn "
        "<i>E</i><sub>c</sub>. Chuyển pha Freedericksz chỉ là sự chuyển từ một cấu hình director "
        "đồng nhất sang một cấu hình director bị biến dạng; tức là tại mọi điểm trong LC, trật tự "
        "tương đối giữa các phân tử vẫn giữ nguyên. Trường tới hạn <i>E</i><sub>c</sub> được tính "
        "bằng kỹ thuật cực tiểu hoá năng lượng tự do [3]:"))
    b.append(eq(_eq("92.9"), "92.9"))
    b.append(p("Do đó điện áp ngưỡng <i>V</i><sub>th</sub> của hiệu ứng quang điện LC là:"))
    b.append(eq(_eq("92.10"), "92.10"))
    b.append(p(
        "Trong các phương trình 92.9 và 92.10, <i>d</i> là bề dày lớp LC và "
        "<i>K</i><sub>ii</sub> là hằng số đàn hồi thích hợp. Khi trường vuông góc với hướng ban "
        "đầu đồng nhất của director, <i>K</i><sub>ii</sub> = <i>K</i><sub>11</sub> hoặc "
        "<i>K</i><sub>22</sub>. Khi trường song song với hướng ban đầu đồng nhất, "
        "<i>K</i><sub>ii</sub> = <i>K</i><sub>33</sub>. Với hướng xoắn, "
        "<i>K</i><sub>ii</sub> = <i>K</i><sub>11</sub> + (<i>K</i><sub>33</sub> − "
        "2<i>K</i><sub>22</sub>)/4."))

    # ------------------------------------------------------------ 92.4
    b.append(h2("92.4 Vật liệu và quy trình chế tạo LCD",
                "LCD Materials and Fabrication Processes"))
    b.append(p(
        "Có nhiều loại LCD dùng vật liệu LC và chế độ hiển thị khác nhau, sẽ bàn ở phần sau. Tuy "
        "vậy, quy trình lắp ráp và vật liệu chung của màn hình rất giống nhau ở mọi chế độ LCD. "
        "Hình 92.8a và b cho thấy mặt bằng và mặt cắt của một LCD quét địa chỉ ma trận thụ động. "
        "Việc chế tạo màn hình có thể chia thành ba phần: (1) quy trình chế tạo kính dưới và kính "
        "trên, (2) quy trình lắp ráp cell, và (3) gắn phin phân cực, driver và lắp ráp mô-đun, như "
        "minh hoạ trên Hình 92.9. Phần tiếp theo mô tả các vật liệu và quy trình lắp ráp."))
    b.append(fig(8))
    b.append(fig(9))

    b.append(h3("Đế kính", "Glass Substrate"))
    b.append(p(
        "Chất lượng đế kính quan trọng ở các mặt: tương thích hoá học với vật liệu LC, độ phẳng "
        "bề mặt, khuyết tật và độ ổn định kích thước dưới nhiệt độ chế tạo của các bước khác nhau. "
        "Với khe cell LCD điển hình 5 đến 10 µm, tầm quan trọng của độ phẳng và chất lượng bề mặt "
        "kính là rõ ràng. Khuyết tật đế kính như rỗ, xước, vệt và hạt bám có thể gây lỗi điện cực "
        "và cản trở việc giữ khe cell LC đồng đều. Vì vậy, tuỳ loại màn hình, đế kính đôi khi được "
        "đánh bóng để đạt chất lượng bề mặt yêu cầu. Vật liệu kính hiển thị điển hình gồm "
        "borosilicate (ví dụ Corning 7059) và aluminosilicate (ví dụ Corning 1737), dày 0,7 hoặc "
        "1,1 mm."))

    b.append(h3("Kính lọc màu", "Color Filters"))
    b.append(p(
        "Ở LCD màu đầy đủ, màu thường được tạo bằng kính lọc màu đỏ, lục, lam (R, G, B) chế tạo "
        "tại mỗi điểm ảnh, như trên Hình 92.8b, dùng hệ đèn nền trắng. Yêu cầu với kính lọc màu "
        "gồm đặc trưng truyền phổ thích hợp và độ ổn định hoá học, nhiệt và kích thước. Gam màu "
        "của màn hình là hàm của đặc trưng phổ đèn nền và đặc trưng truyền của kính lọc màu. Bằng "
        "cách chọn các thông số này thích hợp, LCD có thể đạt gam màu tương đương CRT chất lượng "
        "cao. Tuy vậy, đôi khi phải đánh đổi giữa độ tinh khiết màu và độ truyền (độ chói) của "
        "LCD. Bề dày kính lọc màu điển hình khoảng 2 µm. Vật liệu kính lọc màu gồm polyimide và "
        "photoresist phân tán thuốc nhuộm và sắc tố. Vật liệu được phủ lên kính bằng nhiều quy "
        "trình như quay phủ, in, điện phân lắng và quang khắc. Đầu tiên phủ vật liệu màu thứ nhất "
        "rồi tạo hình bằng quang khắc; sau đó xử lý màu thứ hai rồi màu thứ ba. Một vật liệu ma "
        "trận đen cũng được phủ và tạo hình giữa các kính lọc màu để chặn ánh sáng truyền qua vùng "
        "giữa các điểm ảnh. Trong một số trường hợp, một lớp thụ động như điện môi SiO<sub>2</sub> "
        "nhiệt độ thấp được lắng trên kính lọc màu để làm rào cản tạp chất và tạo bề mặt nhẵn cho "
        "bước lắng điện cực trong suốt tiếp theo."))

    b.append(h3("Điện cực trong suốt", "Transparent Electrodes"))
    b.append(p(
        "Thông thường, oxit indium thiếc (ITO) với nồng độ điển hình 90% In<sub>2</sub>O<sub>3</sub> "
        "và 10% SnO<sub>2</sub> được dùng làm vật liệu điện cực dẫn trong suốt. Độ truyền điển hình "
        "của ITO khoảng 90%. ITO thường được lắng bằng bay hơi chùm tia điện tử hoặc phún xạ trong "
        "khí quyển chứa oxy. Bề dày màng điển hình 50 đến 300 nm tuỳ điện trở tấm và độ truyền yêu "
        "cầu. Điện trở suất điển hình trong khoảng 2 × 10<sup>−4</sup> Ω·cm. Độ truyền sáng qua "
        "ITO không tỉ lệ tuyến tính với bề dày màng vì có giao thoa ánh sáng."))

    b.append(h3("Vật liệu và kỹ thuật định hướng", "Alignment Materials and Techniques"))
    b.append(p(
        "Sau khi tạo hình điện cực trong suốt, một lớp phủ định hướng LC được áp dụng. Tuỳ chế độ "
        "hiển thị, người ta đạt được định hướng đồng nhất (song song), nghiêng hoặc thẳng đứng "
        "(homeotropic) bằng vật liệu và quy trình thích hợp. LCD kiểu TN phổ biến nhất cần định "
        "hướng nghiêng để loại bỏ khuyết tật nghiêng ngược. Màng vô cơ như SiO bay hơi xiên, cũng "
        "như vật liệu hữu cơ như polyimide, có thể dùng làm vật liệu định hướng. Polyimide được "
        "dùng phổ biến nhất làm lớp định hướng: nó được quay phủ hoặc in để đạt bề dày khoảng 50 "
        "nm, rồi đóng rắn ở khoảng 150 đến 200 °C. Sau đó lớp này được chà (rubbing) bằng con lăn "
        "bọc vải cotton hoặc vải tổng hợp. Với LCD TN, quy trình định hướng được chọn để đạt góc "
        "nghiêng sẵn khoảng 2 đến 5°."))

    b.append(h3("Khoảng cách và hàn kín cell", "Cell Spacing and Sealing"))
    b.append(p(
        "Quy trình lắp ráp cell bắt đầu sau khi hai đế đã được xử lý lớp định hướng bằng chà xát. "
        "Để kiểm soát chính xác khe cell LC (bề dày), vật liệu đệm được đưa vào vùng hoạt động của "
        "màn hình cũng như vùng keo viền ngoại vi, nơi hai đế kính được hàn kín. Vật liệu đệm điển "
        "hình gồm sợi (trụ) hoặc hạt (cầu) thuỷ tinh hay nhựa, với phân bố kích thước (đường kính) "
        "được kiểm soát chặt. Sau đó một keo hàn kín như epoxy được phủ ở vùng viền, chừa một lỗ "
        "(lỗ nạp) để bơm vật liệu LC sau khi hàn kín. Keo viền điển hình rộng 1 đến 3 mm và cách "
        "vùng hiển thị hoạt động vài milimét. Yêu cầu với vật liệu hàn kín là không phản ứng hoá "
        "học với (không làm nhiễm bẩn) vật liệu LC và phải là rào cản với hơi ẩm và tạp chất từ "
        "bên ngoài. Sau khi đặt hạt đệm và keo viền lên đế thứ nhất (đế hoạt động), đế này được "
        "căn chính xác với đế thứ hai (đế kính lọc màu), và keo viền được đóng rắn bằng cách nung "
        "tới nhiệt độ cao hơn, điển hình 100 đến 150 °C, hoặc bằng chiếu tia tử ngoại tuỳ loại "
        "epoxy."))

    b.append(h3("Nạp vật liệu LC", "LC Material Filling"))
    b.append(p(
        "Sau khi chế tạo cell rỗng, cell được nạp vật liệu LC. Vì bề dày cell (khe) nhỏ (khoảng 5 "
        "đến 10 µm), việc nạp phải dùng kỹ thuật đặc biệt. Phương pháp phổ biến nhất là hút chân "
        "không cell trong buồng chân không, nhúng lỗ nạp vào bình chứa vật liệu LC rồi tăng áp "
        "suất trong buồng. Khi áp suất buồng tăng, cell được nạp nhờ mao dẫn. Sau khi cell đầy "
        "hoàn toàn, lỗ nạp được bịt bằng keo epoxy tương thích hoá học với vật liệu LC."))

    b.append(h3("Linh kiện ngoài", "External Components"))
    b.append(p(
        "Linh kiện ngoài của LCD gồm phin phân cực, gương phản xạ, driver màn hình và bộ đèn nền. "
        "LCD phản xạ dùng gương phản xạ ở mặt sau, làm việc bằng cách điều biến ánh sáng môi "
        "trường và không cần đèn nền. Ở LCD TN chế độ truyền qua phổ biến nhất, phin phân cực được "
        "gắn ở cả mặt trước và mặt sau của LCD sau khi lắp ráp cell. Ở chế độ thường trắng (NW) "
        "phổ biến nhất, các phin phân cực được gắn với trục phân cực vuông góc nhau và dọc theo "
        "hướng chà của lớp định hướng. Phin phân cực là màng ghép ba lớp: màng phân cực "
        "polyvinyl alcohol (PVA) pha iod kéo giãn ở giữa, và hai màng triacetyl cellulose (TAC) "
        "bên ngoài bảo vệ màng PVA khỏi điều kiện môi trường (hơi ẩm, nhiệt độ, môi trường khắc "
        "nghiệt). Độ truyền điển hình của phin phân cực 41 đến 45%, với hiệu suất phân cực 99,9 "
        "đến 99,99%."))
    b.append(p(
        "Các IC driver hàng và cột của màn hình được gắn vào pad hàng và cột của màn hình bằng "
        "TAB (tape-automated bonding) dùng keo dẫn dị hướng (ACA), hoặc bằng phương pháp chip on "
        "glass (COG). Với LCD truyền qua cần đèn nền, thường dùng đèn huỳnh quang. Phổ phát xạ R, "
        "G, B của đèn nền và phổ truyền của kính lọc màu R, G, B được chỉnh cùng nhau để đạt toạ "
        "độ màu mong muốn cho các màu cơ bản. Một bộ khuếch tán cũng được dùng để đèn nền chiếu "
        "đều. Hệ đèn nền có thể dùng thêm màng tăng độ chói để điều chỉnh phân bố cường độ sáng "
        "trong nón nhìn. Ngoài các linh kiện trên, LCD cho ứng dụng đặc biệt cần hiệu năng cao có "
        "thể dùng kính bảo vệ có phủ chống nhiễu điện từ và chống phản xạ ở mặt trước, và kính "
        "gia nhiệt ở mặt sau (giữa đèn nền và LCD) để làm việc ở nhiệt độ thấp."))

    # ------------------------------------------------------------ 92.5
    b.append(h2("92.5 Các chế độ hiển thị tinh thể lỏng",
                "Liquid Crystal Display Modes"))
    b.append(p(
        "Nhiều chế độ hoạt động khác nhau của màn hình LC đã được phát triển. Về lịch sử, hiệu ứng "
        "chuyển pha (PC) được Wysoki và cộng sự phát hiện đầu tiên năm 1968 [16]. Cùng năm đó, "
        "chế độ tán xạ động (DS) [17] và chế độ khách–chủ (GH) [18] được Heilmeier và cộng sự "
        "công bố. Năm 1971, chế độ TN [19] được Schadt và Helfrich báo cáo, còn lưỡng chiết điều "
        "khiển bằng điện (ECB) được Schiekel và Fahrenschon [20] cùng Hareng và cộng sự [21] báo "
        "cáo. Các hiệu ứng vật lý và chế độ hiển thị dựa trên chúng gồm:"))
    b.append(p(
        "<b>Hiệu ứng dòng:</b> • hiệu ứng DS<br>"
        "<b>Hiệu ứng điện trường:</b> • hiệu ứng TN • hiệu ứng STN • ECB • hiệu ứng GH • hiệu ứng "
        "chuyển pha<br>"
        "<b>Hiệu ứng nhiệt:</b> • hiệu ứng smectic"))
    b.append(p(
        "Hiệu ứng DS dựa trên dị hướng độ dẫn điện. Vì làm việc ở điện áp cao hơn và tiêu thụ công "
        "suất lớn hơn, chế độ DS hiện không còn được dùng. Hiệu ứng TN và STN được dùng rộng rãi "
        "nhất trong mọi LCD. Phần tiếp theo bàn về các chế độ hiển thị."))

    b.append(h3("Hiệu ứng nematic xoắn", "Twisted Nematic Effect"))
    b.append(p(
        "Hình 92.10 là sơ đồ một màn hình dựa trên hiệu ứng TN. Nó gồm vật liệu LC nematic có dị "
        "hướng điện môi dương (Δε > 0), bề dày lớp khoảng 5 µm, kẹp giữa hai đế trong suốt có điện "
        "cực trong suốt. Bề mặt các điện cực được phủ lớp định hướng polyimide và chà xát để định "
        "hướng phân tử LC ở bề mặt đế theo hướng chà, với góc nghiêng sẵn nhỏ (khoảng 3°). Phân tử "
        "trên hai đế được định hướng lệch nhau 90°, như trên Hình 92.10a; tức là trục phân tử LC "
        "quay (xoắn) liên tục 90° từ đế thứ nhất sang đế thứ hai. Màn hình TN có thể được chế tạo "
        "để làm việc ở chế độ thường đen (NB) hoặc thường trắng (NW) tuỳ cách gắn phin phân cực "
        "lên mặt ngoài hai đế kính. Hình 92.10a và b cho thấy trạng thái bật và tắt của LCD TN chế "
        "độ NW với các phin phân cực vuông góc, có hướng phân cực song song với hướng director LC "
        "trên đế đó."))
    b.append(fig(10))
    b.append(p(
        "Vì bước xoắn đủ lớn so với bước sóng ánh sáng nhìn thấy, hướng phân cực của ánh sáng "
        "phân cực thẳng tới vuông góc với một mặt màn hình quay 90° do độ xoắn của phân tử LC khi "
        "truyền qua cell, rồi ló ra qua phin phân cực thứ hai. Khi đặt điện áp vào cell TN, các "
        "phân tử sắp song song với hướng trường như trên Hình 92.10b, và khả năng quay quang 90° "
        "bị mất. Do đó ánh sáng phân cực tới từ phin thứ nhất không bị quay khi qua cell LC và bị "
        "phin ra vuông góc chặn lại."))
    b.append(p(
        "Hình 92.10c cho thấy đặc trưng điện áp–truyền qua của cell TN ở chế độ NB và NW. Với chế "
        "độ NW, khi đặt điện áp đủ cao, phân tử LC sắp thẳng đứng (song song với trường) và không "
        "còn quay vectơ điện trường của ánh sáng phân cực. Kết quả là độ truyền bị triệt tiêu hoàn "
        "toàn, bất kể bước sóng ánh sáng. Tuy vậy, độ truyền ở trạng thái bật lại phụ thuộc bước "
        "sóng; điều này không ảnh hưởng đáng kể tới tỉ số tương phản, dù có thể ảnh hưởng cân bằng "
        "màu. Ở chế độ NB, độ truyền chỉ bị triệt tiêu về không [22] ở trạng thái tắt đối với ánh "
        "sáng đơn sắc có một bước sóng nhất định. Vì vậy, trong màn hình thực tế dùng đèn nền phổ "
        "rộng, có một lượng nhỏ ánh sáng rò, làm giảm tỉ số tương phản. Ở màn hình màu, khe cell "
        "cho các điểm ảnh R, G, B có thể được tối ưu để loại bỏ rò sáng và tăng tương phản [22]."))
    b.append(p("Điện áp ngưỡng của LCD chế độ TN là:"))
    b.append(eq(_eq("92.11"), "92.11"))
    b.append(p(
        "<i>V</i><sub>th</sub> phụ thuộc dị hướng điện môi và các hằng số đàn hồi, thường trong "
        "khoảng 2 đến 3 V, với điện áp làm việc cực đại 5 đến 8 V. Việc điều khiển ở điện áp thấp "
        "này, cùng với dòng nhỏ do điện trở suất cao của vật liệu LC, góp phần vào công suất tiêu "
        "thụ rất thấp (khoảng 1 mW/cm²) của LCD. Thời gian đáp ứng, đo bằng thời gian tăng và thời "
        "gian giảm của màn hình, được cho bởi [23]:"))
    b.append(eq(_eq("92.12"), "92.12"))
    b.append(eq(_eq("92.13"), "92.13"))
    b.append(p(
        "trong đó γ là hệ số nhớt quay. Các phương trình trên cho thấy thời gian tăng có thể cải "
        "thiện bằng cách dùng khe cell <i>d</i> mỏng hơn, Δε lớn hơn và điện áp điều khiển <i>V</i> "
        "cao hơn. Tương tự, thời gian giảm có thể cải thiện bằng cách giảm khe cell. Thời gian bật "
        "τ<sub>r</sub> thường ngắn hơn thời gian tắt τ<sub>d</sub>. Ở nhiệt độ phòng, các thời gian "
        "này cỡ 10 ms, đủ cho nhiều ứng dụng thông dụng như màn hình máy tính và TV. Trong LCD TN, "
        "thang xám được tạo bằng cách thay đổi điện áp theo đường cong quang điện trên Hình "
        "92.10c. Độ dốc thoải của đường cong này phù hợp để tạo thang xám trong màn hình quét địa "
        "chỉ ma trận chủ động (xem phần sau). Tuy vậy, với quét địa chỉ ma trận thụ động, độ dốc "
        "thoải làm giảm mạnh khả năng ghép kênh (số hàng có thể định địa chỉ) của màn hình, dẫn "
        "tới sự ra đời của hiệu ứng STN."))

    b.append(h3("Hiệu ứng STN", "STN Effect"))
    b.append(p(
        "Trong màn hình quét địa chỉ ma trận thụ động, khả năng định địa chỉ hay số hàng tối đa "
        "có thể định địa chỉ <i>N</i> được cho bởi giới hạn Alt và Pleshko [24]:"))
    b.append(eq(_eq("92.14"), "92.14"))
    b.append(p(
        "trong đó <i>V</i><sub>on</sub> và <i>V</i><sub>off</sub> là điện áp hiệu dụng tại điểm ảnh "
        "được chọn và không được chọn. Phương trình 92.14 cho thấy khi <i>N</i> tăng, "
        "<i>V</i><sub>off</sub> tiến tới <i>V</i><sub>on</sub> và tỉ số tương phản tiến tới 1, làm "
        "màn hình không còn xem được. Với <i>N</i> = 100, <i>V</i><sub>on</sub> = 1,11 "
        "<i>V</i><sub>off</sub>; tức là điện áp chọn chỉ cao hơn điện áp không chọn 11%. Điều này "
        "sẽ cho tỉ số tương phản rất thấp nếu dùng chế độ TN với đường cong bật thoải (Hình "
        "92.10c)."))
    b.append(p(
        "Màn hình STN được phát triển [25, 26] để đạt đường cong quang điện dốc, cho phép ghép kênh "
        "nhiều hàng. Hiệu ứng STN dùng góc xoắn 180° đến khoảng 270° với góc nghiêng sẵn tương đối "
        "cao. Hình 92.11 [25] minh hoạ hiệu ứng STN: sự phụ thuộc điện áp của góc nghiêng director "
        "ở mặt giữa của một lớp nematic chiral có góc nghiêng sẵn 28° ở cả hai đế. Tính lưỡng ổn "
        "đạt được khi dùng góc xoắn Φ lớn hơn 245°. Trong màn hình ghép kênh cao, người ta thường "
        "dùng góc xoắn 240° đến 275° và góc nghiêng 5° đến 30°. Góc nghiêng sẵn cao bảo đảm loại "
        "bỏ cấu trúc biến dạng cạnh tranh có độ xoắn ít hơn 180°. Với góc xoắn trái 270°, kết quả "
        "tối ưu đạt được khi phin phân cực trước có trục phân cực hợp với director LC một góc 30° "
        "và phin phân cực sau hợp với hình chiếu của director trên đế sau một góc 60°. Do giao "
        "thoa của các mode quang chuẩn truyền trong lớp LC, màn hình có màu lưỡng chiết vàng ở "
        "trạng thái không chọn (chế độ vàng). Quay một trong hai phin phân cực đi 90° cho ảnh bổ "
        "sung với trạng thái sáng không màu và trạng thái không chọn màu lam (chế độ lam). Màn "
        "hình STN chế độ trắng được làm bằng màng bù pha. Thời gian đáp ứng của STN điển hình cỡ "
        "150 ms. Các màn hình này thường có tỉ số tương phản thấp hơn và góc nhìn hẹp."))
    b.append(fig(11))

    b.append(h3("Lưỡng chiết điều khiển bằng điện (ECB)",
                "Electrically Controlled Birefringence (ECB)"))
    b.append(p(
        "Kỹ thuật hiển thị này dựa trên việc điều khiển lưỡng chiết của cell LC bằng điện trường. "
        "Có nhiều loại màn hình kiểu này tuỳ hướng phân tử của cell LC, ví dụ kiểu DAP, kiểu đồng "
        "nhất, kiểu HAN (hybrid aligned nematic) và kiểu IPS (in-plane switching). Kiểu DAP (định "
        "hướng thẳng đứng) được làm bằng LC có Δε âm, kẹp giữa hai đế điện cực trong suốt và đặt "
        "giữa hai phin phân cực vuông góc, như trên Hình 92.12. Ở trạng thái tắt (không có điện "
        "trường), ánh sáng phân cực tới không thấy lưỡng chiết khi qua cell nên bị phin ra vuông "
        "góc chặn lại. Ở trạng thái bật (khi đặt điện áp), trục phân tử LC nghiêng một góc θ (như "
        "trên Hình 92.12), nên ánh sáng phân cực thẳng trở thành phân cực elip khi qua cell do "
        "lưỡng chiết. Do đó một phần ánh sáng lọt qua phin ra vuông góc; cường độ <i>I</i> của "
        "ánh sáng truyền qua cell được cho bởi [20]:"))
    b.append(eq(_eq("92.15"), "92.15"))
    b.append(fig(12))
    b.append(p(
        "trong đó <i>I</i><sub>0</sub> là cường độ ánh sáng tới, φ là góc giữa hướng phân cực của "
        "ánh sáng tới và hướng dao động của ánh sáng thường trong cell, <i>d</i> là khe cell, "
        "Δ<i>n</i>(<i>V</i>) là lưỡng chiết của cell, <i>d</i>Δ<i>n</i> là hiệu pha quang, và λ là "
        "bước sóng ánh sáng tới. Phương trình cho thấy <i>I</i> phụ thuộc điện áp đặt vào và λ."))
    b.append(p(
        "Với kỹ thuật đồng nhất, cell LC dùng vật liệu dương với định hướng đồng nhất. Ở phương "
        "pháp này, điện áp ngưỡng nhận được bằng cách thay hằng số đàn hồi uốn <i>K</i><sub>33</sub> "
        "bằng hằng số đàn hồi toả <i>K</i><sub>11</sub>. Cell HAN có định hướng hybrid: phân tử "
        "vuông góc với một đế nhưng song song với đế kia. Ở chế độ này có thể dùng cả vật liệu Δε "
        "dương và âm, và vì không có điện áp ngưỡng rõ ràng nên nó có ưu điểm là điện áp điều "
        "khiển rất thấp. Gần đây, một chế độ ECB dựa trên kiểu IPS đã được phát triển để tạo LCD có "
        "góc nhìn cực rộng. Ở màn hình IPS, LC được định hướng đồng nhất và chuyển giữa trạng thái "
        "bật và tắt bằng các điện cực đan răng lược chế tạo trên một trong hai đế [27]. Màn hình "
        "IPS dùng chế độ NB với vật liệu LC Δε dương hoặc âm."))

    b.append(h3("Kiểu khách–chủ", "Guest–Host Type"))
    b.append(p(
        "Một số thuốc nhuộm hữu cơ thể hiện dị hướng hấp thụ ánh sáng: chúng hấp thụ nhiều hơn "
        "trong một dải bước sóng nhất định khi vectơ <b>E</b> của ánh sáng song song với trục "
        "quang của phân tử thuốc nhuộm so với khi vuông góc. LCD dựa trên nguyên lý này gọi là "
        "màn hình khách–chủ (GH). Trong đó, một lượng nhỏ thuốc nhuộm lưỡng sắc (khách) được trộn "
        "vào vật liệu LC (chủ). Các phân tử thuốc nhuộm sắp theo phân tử LC, nên có thể đổi hướng "
        "(bằng cách đổi hướng phân tử LC) khi đặt điện trường. Khi dùng vật liệu LC có Δε dương, "
        "ở trạng thái tắt vectơ <b>E</b> của ánh sáng phân cực trùng với trục hấp thụ của thuốc "
        "nhuộm lưỡng sắc; do đó ánh sáng bị hấp thụ và ánh sáng truyền qua có màu. Khi đặt điện "
        "áp cho trạng thái bật, vectơ <b>E</b> vuông góc với trục hấp thụ của thuốc nhuộm; do đó "
        "không có hấp thụ và ánh sáng truyền qua không có màu (trắng). LCD GH chỉ cần một phin "
        "phân cực. Hơn nữa, vì hiệu ứng quang dựa trên hấp thụ, màn hình cho góc nhìn tốt hơn LCD "
        "chế độ TN."))

    b.append(h3("Kiểu chuyển pha", "Phase-Change Type"))
    b.append(p(
        "Màn hình kiểu chuyển pha dựa trên sự thay đổi hướng phân tử từ pha cholesteric xoắn sang "
        "pha nematic thẳng đứng và ngược lại. Kỹ thuật này dùng LC cholesteric có bước xoắn dài, "
        "với Δε dương hoặc âm. Màn hình này không dùng phin phân cực. Ở trạng thái tắt, ánh sáng "
        "tới qua cell cholesteric có định hướng focal conic bị tán xạ quang học, nên cell trông "
        "đục. Tuy vậy, khi đặt điện áp, cấu trúc xoắn của pha cholesteric chuyển thành pha nematic "
        "định hướng thẳng đứng và cell trở nên trong suốt."))

    b.append(h3("Hiệu ứng nhiệt", "Thermal Effects"))
    b.append(p(
        "Hiệu ứng nhiệt dựa trên sự thay đổi hành vi quang điện do thay đổi hướng phân tử của LC "
        "khi bị nung nóng hoặc làm lạnh. Hiệu ứng này được dùng với LC smectic định hướng thẳng "
        "đứng. Khi nung cell tới pha đẳng hướng rồi làm lạnh, nếu làm lạnh đột ngột cell trở nên "
        "đục, còn nếu làm lạnh từ từ cell trở nên trong suốt. Hai trạng thái đục và trong tương "
        "ứng với định hướng focal conic và thẳng đứng của LC smectic A. Hiệu ứng này được dùng cho "
        "màn hình loại bộ nhớ khổ lớn, trong đó tia laser được dùng để ghi hình bằng nhiệt. Việc "
        "nung nóng cũng có thể thực hiện bằng một trong hai điện cực trong suốt, còn điện cực kia "
        "làm điện cực tín hiệu."))

    # ------------------------------------------------------------ 92.6
    b.append(h2("92.6 Quét địa chỉ màn hình", "Display Addressing"))
    b.append(p(
        "Kỹ thuật quét địa chỉ (điều khiển) ảnh hưởng lớn tới chất lượng hình ảnh LCD. Có thể chia "
        "thành ba loại chính: quét trực tiếp (tĩnh), quét địa chỉ ma trận thụ động và quét địa chỉ "
        "ma trận chủ động. Với màn hình ít thông tin như hiển thị số, biểu đồ thanh và các màn "
        "hình mẫu cố định dùng điện cực phân đoạn, người ta dùng quét trực tiếp. Ví dụ phổ biến của "
        "màn hình quét trực tiếp là hiển thị số dùng bảy điện cực phân đoạn cho mỗi chữ số. Mỗi "
        "điện cực phân đoạn trên đế trước và điện cực chung trên đế sau được nối trực tiếp với "
        "tín hiệu điều khiển. Điện áp được đặt chọn lọc lên từng phân đoạn để hiển thị bất kỳ chữ "
        "số nào từ 0 đến 9. Với màn hình nhiều thông tin, cách này trở nên không thực tế vì số "
        "đường nối quá lớn, nên người ta dùng quét địa chỉ ma trận thụ động hoặc chủ động."))

    b.append(h3("Quét địa chỉ ma trận thụ động", "Passive Matrix Addressing"))
    b.append(p(
        "Màn hình ma trận thụ động (PM) gồm LC giữa một ma trận điện cực hàng và cột dẫn điện "
        "trong suốt (Hình 92.8) là loại LCD quét địa chỉ ma trận đơn giản nhất và rẻ nhất để chế "
        "tạo. Một ví dụ của LCD PM là màn hình VGA màu (R, G, B) dùng hiệu ứng STN, với định dạng "
        "điểm ảnh 640 (× 3 = 1920) ngang × 480 dọc, tức 1920 cột và 480 hàng, tổng cộng 2400 đường "
        "nối dùng để định địa chỉ cho màn hình chứa 921.600 điểm ảnh. Trong quét địa chỉ PM, điện "
        "áp hàng được quét lần lượt với điện áp <i>V</i><sub>r</sub>, trong khi mọi cột trong một "
        "hàng được điều khiển song song, trong thời gian hàng, với điện áp ±<i>V</i><sub>c</sub> "
        "tuỳ điểm ảnh được chọn bật hay tắt. Như đã bàn ở phần hiệu ứng STN, tỉ số tương phản của "
        "LCD PM chịu ảnh hưởng của giới hạn định địa chỉ Alt–Pleshko [24]. Để tăng biên làm việc "
        "nhằm cải thiện tương phản, người ta dùng cấu hình DSTN (dual-scan STN) trong màn hình "
        "nhiều thông tin hơn. Ở DSTN, màn hình được chia làm hai nửa, các hàng trong mỗi nửa được "
        "quét đồng thời và đồng bộ, về cơ bản nhân đôi tỉ số nhiệm vụ của điểm ảnh bật để tăng "
        "tương phản. Một nhược điểm lớn của màn hình STN quét địa chỉ ma trận thụ động là thời gian "
        "đáp ứng chậm của LC, cỡ 150 ms. Thời gian này không đủ cho ứng dụng video và chỉ vừa đủ "
        "cho giao diện đồ hoạ của máy tính. Thời gian đáp ứng của LCD STN có thể cải thiện bằng kỹ "
        "thuật quét địa chỉ chủ động hoặc quét nhiều dòng [28, 29]. Các kỹ thuật này định địa chỉ "
        "đồng thời nhiều hàng để khắc phục vấn đề đáp ứng khung của LCD STN thông thường."))

    b.append(h3("Quét địa chỉ ma trận chủ động", "Active Matrix Addressing"))
    b.append(p(
        "Quét địa chỉ ma trận chủ động (AM) loại bỏ giới hạn ghép kênh [24] của LCD PM bằng cách "
        "đưa một phần tử điều khiển phi tuyến nối tiếp với mỗi điểm ảnh, và cung cấp tỉ số nhiệm "
        "vụ 100% cho điểm ảnh nhờ điện tích tích trữ tại điểm ảnh trong thời gian quét hàng. Hình "
        "92.13a minh hoạ một mảng ma trận chủ động với các driver hàng và cột cùng điện tử mô-đun "
        "màn hình đi kèm. Hình 92.13b là ảnh phóng to mảng ma trận chủ động trong panel LCD. Trong "
        "hình, <i>C</i><sub>LC</sub> và <i>C</i><sub>S</sub> là điện dung điểm ảnh và điện dung "
        "tích trữ của điểm ảnh. Thông thường một tụ tích trữ <i>C</i><sub>S</sub> được đưa vào mỗi "
        "điểm ảnh để giảm độ lệch điện áp điểm ảnh (xem phương trình 92.16) và để làm việc ở dải "
        "nhiệt độ rộng. Hình 92.14 là mặt cắt qua một LCD AM, minh hoạ các thành phần của màn "
        "hình. Hình 92.15 là một điểm ảnh AM LCD điển hình, cho thấy các bus cổng và dữ liệu, "
        "transistor màng mỏng (TFT), điện cực điểm ảnh ITO và tụ tích trữ."))
    b.append(fig(13))
    b.append(fig(14))
    b.append(fig(15))
    b.append(p(
        "Chế tạo đế ma trận chủ động là một trong những khía cạnh chính của sản xuất LCD AM. Cả "
        "linh kiện hai cực như diode nối tiếp ngược và diode kim loại–cách điện–kim loại (MIM), "
        "lẫn TFT ba cực đều được phát triển cho quét địa chỉ ma trận chủ động. Linh kiện hai cực dễ "
        "chế tạo và rẻ hơn, nhưng hạn chế ở chỗ hiệu năng không đồng đều (điện áp đánh thủng/ngưỡng) "
        "trên diện tích màn hình lớn và không cách ly hoàn toàn điểm ảnh khi các điểm ảnh lân cận "
        "được định địa chỉ. Để có chất lượng hình ảnh tốt hơn, LCD AM dùng TFT làm linh kiện ma "
        "trận chủ động, vì TFT cách ly hoàn toàn điểm ảnh khỏi các điểm ảnh lân cận. LCD AM diện "
        "tích lớn dùng TFT silic vô định hình (a-Si) [6], còn TFT polysilicon tích hợp driver hàng "
        "và cột được dùng trong LCD nhỏ, độ phân giải cao [30]."))
    b.append(p(
        "Hình 92.16 cho thấy mạch tương đương của một điểm ảnh TFT-LCD, dạng sóng điều khiển màn "
        "hình và điện áp điểm ảnh thu được. Như ở hầu hết màn hình quét địa chỉ ma trận kiểu quét "
        "từng dòng, các hàng (cổng) được quét bằng một xung cổng chọn <i>V</i><sub>g,sel</sub> "
        "trong thời gian khung <i>t</i><sub>f</sub>, trong khi mọi điểm ảnh trong một hàng được "
        "định địa chỉ đồng thời bằng điện áp dữ liệu ±<i>V</i><sub>d</sub> trong thời gian hàng "
        "<i>t</i><sub>r</sub> (= <i>t</i><sub>f</sub>/<i>N</i>). Trong thời gian hàng, điện áp "
        "cổng chọn <i>V</i><sub>g,sel</sub> “bật” TFT và nạp điểm ảnh cùng tụ tích trữ tới điện áp "
        "dữ liệu <i>V</i><sub>d</sub>. Sau thời gian hàng, TFT bị “tắt” bằng điện áp cổng không "
        "chọn <i>V</i><sub>g,non-sel</sub>; do đó điện áp (điện tích) tại điểm ảnh này được cách "
        "ly khỏi phần còn lại của cấu trúc ma trận cho tới khi tới lúc nạp lại điểm ảnh trong "
        "khung kế tiếp. Lưu ý rằng điểm ảnh LC phải được điều khiển kiểu xoay chiều với +<i>V</i>"
        "<sub>d</sub> và −<i>V</i><sub>d</sub> trong các khung xen kẽ, sao cho không có điện áp "
        "một chiều ròng trên điểm ảnh. Điện áp một chiều ròng trên điểm ảnh gây nhấp nháy và hiện "
        "tượng dính ảnh [33], do độ dẫn điện của LC. Điện áp một chiều lớn và kéo dài còn làm "
        "hỏng vật liệu LC do điện phân. Độ dịch điện áp điểm ảnh Δ<i>V</i><sub>p</sub> trên Hình "
        "92.16, ở cuối thời gian hàng, là do điện dung ký sinh cổng–máng <i>C</i><sub>gd</sub> "
        "của TFT."))
    b.append(fig(16))
    b.append(p(
        "Khi điện áp cổng chuyển mạch, sự phân bố lại điện tích từ lớp điện môi cổng của TFT gây "
        "ra độ dịch điện áp điểm ảnh Δ<i>V</i><sub>p</sub>:"))
    b.append(eq(_eq("92.16"), "92.16"))
    b.append(p(
        "Với TFT a-Si kênh n kiểu tăng cường, độ dịch Δ<i>V</i><sub>p</sub> này âm ở cả khung "
        "dương lẫn khung âm; do đó nó giúp nạp điểm ảnh ở khung âm và cản trở ở khung dương. Hơn "
        "nữa, do phân cực cổng tăng trong khung âm, điểm ảnh đạt điện áp dữ liệu nhanh hơn nhiều "
        "trong thời gian định địa chỉ. Vì vậy TFT được thiết kế cho điều kiện khung dương xấu "
        "nhất. Δ<i>V</i><sub>p</sub> được giảm bằng cách giảm thiểu <i>C</i><sub>gd</sub> nhờ giảm "
        "diện tích chồng lấn nguồn–máng của TFT và bằng cách dùng tụ tích trữ. Hơn nữa, "
        "Δ<i>V</i><sub>p</sub> được bù bằng cách chỉnh điện áp điện cực chung <i>V</i><sub>com</sub> "
        "như trên Hình 92.16. Lưu ý rằng <i>C</i><sub>lc</sub> là hàm của <i>V</i><sub>p</sub> "
        "(<i>V</i><sub>lc</sub>) do dị hướng điện môi của LC; vì vậy chỉ chỉnh <i>V</i><sub>com</sub> "
        "không loại bỏ được điện áp một chiều cho mọi mức xám, và cần sửa đổi điện áp thang xám "
        "để bù dị hướng điện môi của LC."))

    b.append(h3("Điện tử mô-đun màn hình", "Display Module Electronics"))
    b.append(p(
        "Hình 92.13 là sơ đồ khối điện tử của một mô-đun LCD AM. Khối điều khiển và bộ tạo nguồn "
        "được gắn riêng trên một bảng mạch in và nối với các driver hàng và cột của LCD ở một phía "
        "và với bộ điều khiển chủ ở phía kia. Khối điều khiển có thể gồm bộ dịch mức, bộ tạo thời "
        "gian và trong một số trường hợp cả các chức năng tương tự; khối này nhận dữ liệu số từ hệ "
        "chủ, thường là chip điều khiển đồ hoạ, và chuyển thành thời gian cùng mức tín hiệu mà "
        "driver hàng và cột yêu cầu. Kiến trúc và thiết kế điện tử mô-đun bao gồm driver hàng và "
        "cột ảnh hưởng đáng kể không chỉ tới chi phí hệ thống hiển thị và công suất tiêu thụ mà "
        "còn tới chất lượng hình ảnh. Vật liệu LC thường cần khoảng 5 V để đạt bão hoà quang (xem "
        "Hình 92.10c). Xét nhu cầu điều khiển xoay chiều, biên độ điện áp cần trên vật liệu LC "
        "khoảng 10 V. Để đạt biên 10 V này trên vật liệu LC, driver cột thường dùng nguồn 12 V. Có "
        "thể giảm điện áp driver cột bằng phương pháp điều khiển điều biến <i>V</i><sub>com</sub>. "
        "Trong phương pháp này, nút <i>V</i><sub>com</sub> (nối với mọi điểm ảnh trong màn hình) "
        "được điều khiển lên trên và xuống dưới dải 5 V của driver cột. Mỗi thời gian hàng, nút "
        "<i>V</i><sub>com</sub> được đảo giữa một điện áp trên và một điện áp dưới dải đầu ra 5 V "
        "của driver cột. Như vậy đạt 10 V trên vật liệu LC mà chỉ dùng driver cột 5 V. Phương pháp "
        "này cần thêm linh kiện và tiêu thụ thêm công suất do dao động của nút <i>V</i><sub>com</sub>. "
        "Ngoài ra, để tránh vấn đề tiêm điện dung, driver hàng thường có nguồn âm được điều biến "
        "cùng tần số với nút <i>V</i><sub>com</sub>. Tuy vậy, so với driver cột 10 V, driver cột 5 V "
        "tiêu thụ ít công suất hơn và dễ thiết kế, chế tạo hơn bằng CMOS kích thước nhỏ. Phương "
        "pháp điều biến <i>V</i><sub>com</sub> chỉ dùng được với sơ đồ đảo cực theo hàng (để loại "
        "nhấp nháy điểm ảnh), kéo theo một ít nhiễu xuyên âm ngang. Tuy vậy, sơ đồ đảo cực theo cột "
        "và theo điểm ảnh cho chất lượng hình ảnh tốt hơn với nhiễu xuyên âm giảm nhiều, nhưng "
        "không dùng được với điều khiển điều biến <i>V</i><sub>com</sub>."))

    b.append(h2("Tài liệu tham khảo", "References"))
    b.append(refs(_REFS))
    return "".join(b)


# ================================================================ ENGLISH
def body_en():
    b = []

    b.append(note(
        "<b>Translator's note.</b> The printed source (CRC Press, 1999) contains several defects "
        "that are corrected here. The cell gap is printed as “5 to 10 mm” and the colour-filter "
        "thickness as “2 mm”, but the context requires micrometres; both have been changed to µm. "
        "The response times are printed as “tr, tf” although the text refers to rise and decay "
        "times; the correct symbols are τ<sub>r</sub> and τ<sub>d</sub>, and Eq. 92.13 is for "
        "τ<sub>d</sub>. Equations 92.9–92.13 were corrupted by OCR and have been restored to the "
        "standard Freedericksz and Jakeman–Raynes forms. The caption of Fig. 92.3 prints “P = "
        "azoxy anisole (PPA)” while the text uses PAA (p-azoxyanisole)."))

    b.append(h2("92.1 Introduction"))
    b.append(p(
        "Liquid crystals (LC) are an important class of materials with applications ranging from "
        "display devices, optoelectronic devices and sensors to biological and structural "
        "materials. This chapter focuses on LCs for display applications. In general, most "
        "substances have a single melting point, where a solid possessing positional and "
        "orientational order changes upon melting to an isotropic liquid that has neither. "
        "However, some materials, when melted from the solid state, change into a cloudy liquid "
        "with orientational order at one temperature and, upon further heating, into an isotropic "
        "liquid with no order, as shown in Fig. 92.1."))
    b.append(fig(1, "en"))
    b.append(p(
        "An LC is therefore a mesophase existing between the melting temperature "
        "<i>T</i><sub>m</sub> of a crystalline phase and the clearing point "
        "<i>T</i><sub>c</sub> of the liquid phase: below <i>T</i><sub>m</sub> the material is "
        "crystalline, above <i>T</i><sub>c</sub> it is a liquid (isotropic), and between the two "
        "it is a liquid crystal. An LC whose mesophase is defined by temperature is called "
        "thermotropic; when the mesophase is defined by solvent concentration it is called "
        "lyotropic. Display LCs are thermotropic. The orientational order of LC materials "
        "produces important physical properties, such as birefringence, that make them useful for "
        "displays."))
    b.append(p(
        "Because LCs offer low drive voltage, low power consumption, a thin form factor (flat "
        "panels), light weight, full colour, grey scale with a wide dynamic range, full motion "
        "video, superior image quality and high reliability, LC displays (LCDs) are the preferred "
        "approach for battery-powered (portable) applications ranging from wristwatch displays "
        "and handheld TVs to laptop computer displays. They are also replacing cathode ray tubes "
        "(CRTs) in select applications such as avionic displays because of their high brightness "
        "and readability in sunlight."))
    b.append(p(
        "LCs are also used in projection displays for head-mounted displays (HMD) and for "
        "large-screen applications. The following sections discuss the various types of LC "
        "materials, their properties, LCD materials and fabrication processes, the various LCD "
        "modes, and display addressing methods. Many good general references exist (for example "
        "References 1 through 7). At the time of writing, LCD technology is advancing very "
        "rapidly in viewing angle, image quality, power consumption and display size. The purpose "
        "of this chapter, however, is to present basic LCD principles and technologies rather "
        "than to review the state of the art."))

    b.append(h2("92.2 Types of Liquid Crystal Materials"))
    b.append(p(
        "Most LC materials are organic compounds consisting of rod-shaped or disk-shaped "
        "molecules. For displays, rod-shaped LCs are the most commonly used. According to their "
        "molecular order, LC materials are broadly classified into three types (phases) — "
        "smectic, nematic and cholesteric — as shown in Fig. 92.2. In a smectic liquid crystal "
        "the rod-shaped molecules are arranged in layers with the molecules parallel to each "
        "other. There are many smectic phases, but smectic A and smectic C are the most common. "
        "In smectic A the molecular axis (director) is perpendicular to the layers (Fig. 92.2a); "
        "in smectic C it is tilted from the layer normal (Fig. 92.2b)."))
    b.append(fig(2, "en"))
    b.append(p(
        "In a nematic LC the rod-shaped molecules are parallel to each other, but individual "
        "molecules move relatively easily along their axis without a layer structure (Fig. "
        "92.2c). In a cholesteric LC the molecules are arranged in layers as in a smectic, but "
        "the molecular axis lies in the plane of each layer (Fig. 92.2d); moreover, the "
        "cholesteric has a helical structure in which the director <b>n</b> changes from layer to "
        "layer. The same material may show different phases at different temperatures — for "
        "example smectic C at low temperature, then smectic A, then nematic, before becoming "
        "isotropic at <i>T</i><sub>c</sub>."))
    b.append(p(
        "The nematic LC is the basis of most widely used active-matrix-addressed twisted nematic "
        "(TN) LCDs and passive-matrix-addressed supertwisted nematic (STN) LCDs. An example of a "
        "smectic C display is the passive-matrix-addressed ferroelectric LCD [8]. An example of a "
        "cholesteric display is the passive-matrix-addressed stabilised cholesteric texture (SCT) "
        "display with bistability [9]. A classic nematic material is p-azoxyanisole (PAA), "
        "nematic from 117 to 136 °C."))
    b.append(p(
        "In PAA the two benzene rings are nearly coplanar and the rigid rod is about 20 Å long and "
        "5 Å wide. Another historical nematic is N-(p-methoxybenzylidene-p-butylaniline) (MBBA), "
        "nematic from 22 to 47 °C."))
    b.append(p(
        "MBBA has a central group that firmly connects the two ring cores and keeps the whole "
        "molecule linear. The terminal groups and conjugated bonds in the core are largely "
        "responsible for the dielectric, optical and other anisotropic properties. Azoxy and "
        "Schiff's-base compounds were among the earliest LCD materials. Because of environmental "
        "stability problems they were replaced by biphenyl materials. More recently "
        "phenylcyclohexane, bicyclohexane and estercyclohexane compounds were developed to meet "
        "the requirements of broad temperature operation and enhanced electro-optical "
        "characteristics. The LCs used in current LCDs are highly developed mixtures tailored for "
        "environmental stability, a wide operating temperature range, proper response to the "
        "applied field, high resistivity for matrix addressing and fast response."))
    b.append(p(
        "The degree of order is an important parameter, defined by the order parameter "
        "<i>S</i>:"))
    b.append(eq(_eq("92.1"), "92.1"))
    b.append(p(
        "where θ is the angle between the molecular axis and the predominant molecular "
        "orientation <b>n</b>; ⟨ ⟩ denotes an average over all space. The predominant orientation, "
        "known as the LC director <b>n</b>, is the average alignment direction of the long "
        "molecular axis. For perfect orientational order — all molecules parallel to the director, "
        "as in a perfect crystal — θ = 0 and <i>S</i> = 1. For no orientational order — a "
        "completely random orientation, as in an isotropic liquid — <i>S</i> = 0. In a typical "
        "nematic, <i>S</i> lies between 0.3 and 0.7; in a typical smectic, between 0.7 and 0.8, "
        "with higher values at lower temperatures. Fig. 92.3 shows the temperature dependence of "
        "<i>S</i> for PAA [10]. The order parameter falls rapidly to about 0.3 near the clearing "
        "point <i>T</i><sub>c</sub> and becomes zero in the isotropic state."))
    b.append(fig(3, "en"))
    b.append(p(
        "The exact dependence of <i>S</i> on <i>T</i> depends on the molecules, but the following "
        "analytical expression derived from theory is useful [11]:"))
    b.append(eq(_eq("92.2"), "92.2"))
    b.append(p(
        "where <i>T</i><sub>c</sub> is the nematic–isotropic transition and β is an exponent "
        "between 0.13 and 0.18 depending on the material. (The printed source also includes a "
        "coefficient γ of order 0.98; the standard Haller form is used here.)"))

    b.append(h2("92.3 Physical Properties of Liquid Crystals"))
    b.append(p(
        "Because of their ordered structure, with molecules aligned with their long axes parallel, "
        "LC molecules exhibit anisotropic properties: the dielectric constant ε, refractive index "
        "<i>n</i>, magnetic susceptibility χ, conductivity σ and viscosity η all differ parallel "
        "(∥) and perpendicular (⊥) to the molecular axis. This anisotropy, together with the ease "
        "of setting the initial orientation (boundary condition) by surface alignment and of "
        "reorienting the molecular axis by an applied voltage, is the basis of LC displays. This "
        "section discusses dielectric and refractive-index anisotropy, the elastic constants and "
        "the electro-optical characteristics."))

    b.append(h3("Dielectric Anisotropy"))
    b.append(p(
        "LC molecules exhibit dielectric anisotropy because of their permanent and induced "
        "dipoles. The dielectric anisotropy Δε is:"))
    b.append(eq(_eq("92.3"), "92.3"))
    b.append(p(
        "where ε<sub>∥</sub> and ε<sub>⊥</sub> are measured parallel and perpendicular to the "
        "director. Materials with Δε > 0 are called p-type, those with Δε < 0 n-type. p-type LCs "
        "tend to align their molecular axis parallel to the applied field; n-type LCs align "
        "perpendicular to it."))
    b.append(p(
        "Generally ε<sub>∥</sub> decreases with increasing frequency [12] because of dielectric "
        "relaxation, whereas ε<sub>⊥</sub> is frequency independent over a wide range. At the "
        "crossover frequency <i>f</i><sub>c</sub>, where ε<sub>∥</sub> = ε<sub>⊥</sub>, the "
        "material becomes isotropic. Depending on the material, <i>f</i><sub>c</sub> lies between "
        "100 kHz and more than 1 MHz. The dielectric constants also change with temperature [13], "
        "as shown in Fig. 92.4 for the nematic cyanobiphenyl. The two constants converge rapidly "
        "as the temperature approaches <i>T</i><sub>c</sub>, where ε<sub>∥</sub> = ε<sub>⊥</sub> "
        "= ε<sub>isotropic</sub>."))
    b.append(fig(4, "en"))

    b.append(h3("Refractive Index Anisotropy"))
    b.append(p(
        "An LC is birefringent, with anisotropic refractive indices. It has two principal indices, "
        "<i>n</i><sub>o</sub> and <i>n</i><sub>e</sub>, as shown in Fig. 92.5. For the ordinary "
        "index <i>n</i><sub>o</sub> the electric vector oscillates perpendicular to the optic "
        "axis; for the extraordinary index <i>n</i><sub>e</sub> it oscillates parallel to the "
        "optic axis. In nematic and smectic LCs the director <b>n</b> is the optic axis of the "
        "uniaxial crystal, so the indices for oscillations parallel and perpendicular to the "
        "director are <i>n</i><sub>∥</sub> and <i>n</i><sub>⊥</sub> respectively: "
        "<i>n</i><sub>o</sub> = <i>n</i><sub>⊥</sub>, <i>n</i><sub>e</sub> = "
        "<i>n</i><sub>∥</sub>. The optical anisotropy, or birefringence, is:"))
    b.append(eq(_eq("92.4"), "92.4"))
    b.append(fig(5, "en"))
    b.append(p(
        "Fig. 92.6a and b show the temperature [2] and wavelength [2] dependence of the indices "
        "for typical LCs. The wavelength dependence λ is usually expressed by the Cauchy equation:"))
    b.append(eq(_eq("92.5"), "92.5"))
    b.append(p(
        "where <i>n</i><sub>∞</sub> is the index extrapolated to infinite wavelength and α is a "
        "material-specific coefficient."))
    b.append(fig(6, "en"))

    b.append(h3("Elastic Constants"))
    b.append(p(
        "In uniaxial LCs the preferred (equilibrium) orientation is given by the director "
        "<b>n</b>, imposed by surface treatment at the boundaries or by an external field. When "
        "the LC is perturbed from equilibrium by applying or removing a field, elastic and "
        "electrical forces determine the static deformation pattern. The transition of the "
        "director from one direction to another induces curvature strain. Frank [14] showed that "
        "an arbitrary deformation can be seen as a combination of three basic operations — splay, "
        "twist and bend — with elastic constants <i>K</i><sub>11</sub>, <i>K</i><sub>22</sub> and "
        "<i>K</i><sub>33</sub> in the notation of Oseen–Frank theory. Fig. 92.7 illustrates the "
        "three. The elastic part of the internal free energy <i>F</i> is:"))
    b.append(eq(_eq("92.6"), "92.6"))
    b.append(p(
        "The free-energy density is thus quadratic in the curvature strains, with the elastic "
        "constants as coefficients of proportionality. The constants are temperature dependent "
        "and decrease as temperature rises. Their magnitudes can be approximated [15] by:"))
    b.append(eq(_eq("92.7"), "92.7"))
    b.append(fig(7, "en"))

    b.append(h3("Electro-Optical Characteristics"))
    b.append(p(
        "When a field is applied to an LC with an initial director orientation, the director "
        "changes to a new orientation because of the dielectric anisotropy (Δε = ε<sub>∥</sub> − "
        "ε<sub>⊥</sub>). This change is accompanied by a change in the optical transmission or "
        "reflection of the LC, which is the basis of LCDs. This electrically driven optical "
        "modulation is the electro-optic effect. A field <b>E</b> produces an electric energy "
        "<i>f</i><sub>e</sub>:"))
    b.append(eq(_eq("92.8"), "92.8"))
    b.append(p(
        "The initial orientation of the director is either parallel (Δε > 0) or perpendicular "
        "(Δε < 0) to the plane of the two parallel electrodes. When a field is applied, the "
        "director orients parallel to <b>E</b> for Δε > 0 and perpendicular for Δε < 0. The total "
        "free energy <i>F</i> of the deformed LC is the sum of the electric energy "
        "<i>f</i><sub>e</sub> and the elastic energy. The transition from the undeformed state, "
        "the Freedericksz transition, occurs when the field reaches a critical value "
        "<i>E</i><sub>c</sub>. It is simply a transition from a uniform director configuration to "
        "a deformed one: at every point the relative order of the molecules is unchanged. The "
        "threshold field is obtained by free-energy minimisation [3]:"))
    b.append(eq(_eq("92.9"), "92.9"))
    b.append(p("The threshold voltage <i>V</i><sub>th</sub> is therefore:"))
    b.append(eq(_eq("92.10"), "92.10"))
    b.append(p(
        "In Eqs. 92.9 and 92.10, <i>d</i> is the LC thickness and <i>K</i><sub>ii</sub> the "
        "appropriate elastic constant. When the field is perpendicular to an initially "
        "homogeneous director, <i>K</i><sub>ii</sub> = <i>K</i><sub>11</sub> or "
        "<i>K</i><sub>22</sub>; when parallel, <i>K</i><sub>ii</sub> = <i>K</i><sub>33</sub>. For "
        "a twisted orientation, <i>K</i><sub>ii</sub> = <i>K</i><sub>11</sub> + "
        "(<i>K</i><sub>33</sub> − 2<i>K</i><sub>22</sub>)/4."))

    b.append(h2("92.4 LCD Materials and Fabrication Processes"))
    b.append(p(
        "There are several types of LCD using different LC materials and modes, discussed in the "
        "next section. However, the general assembly processes and materials are very similar for "
        "all modes. Fig. 92.8a and b show the plan and cross-section of a passive-matrix-addressed "
        "LCD. Display fabrication can be divided into three parts: (1) lower and upper glass "
        "fabrication, (2) cell assembly, and (3) polarizer and driver attachment and module "
        "assembly, as illustrated in Fig. 92.9. The following describes the materials and "
        "processes."))
    b.append(fig(8, "en"))
    b.append(fig(9, "en"))

    b.append(h3("Glass Substrate"))
    b.append(p(
        "Glass quality matters for chemical compatibility with the LC, surface flatness, defects "
        "and dimensional stability under the processing temperatures of the various fabrication "
        "steps. With a typical cell gap of 5 to 10 µm, the importance of flatness and surface "
        "quality is clear. Defects such as voids, scratches, streaks and attached particles cause "
        "electrode defects and hinder uniform cell spacing. Depending on the display type, "
        "substrates are sometimes polished. Typical glasses include borosilicate (e.g. Corning "
        "7059) and aluminosilicate (e.g. Corning 1737), 0.7 or 1.1 mm thick."))

    b.append(h3("Color Filters"))
    b.append(p(
        "In full-colour LCDs, colour is usually generated by red, green and blue (R, G, B) colour "
        "filters at each pixel, as shown in Fig. 92.8b, using a white backlight. The filters must "
        "have suitable spectral transmission and chemical, thermal and dimensional stability. The "
        "colour gamut is a function of the backlight spectrum and the filter transmission; with a "
        "suitable choice an LCD can match a high-quality CRT, though colour purity and "
        "transmission (brightness) are sometimes traded off. Typical filter thickness is about "
        "2 µm. Materials include dye- and pigment-dispersed polyimides and photoresists, applied "
        "by spin coating, printing, electrodeposition or photolithography. The first colour is "
        "applied and patterned, then the second, then the third. A black matrix is applied and "
        "patterned between the filters to block light from the interpixel regions. Sometimes a "
        "passivation layer such as low-temperature SiO<sub>2</sub> is deposited to act as an "
        "impurity barrier and to smooth the surface for the subsequent transparent electrode."))

    b.append(h3("Transparent Electrodes"))
    b.append(p(
        "Indium tin oxide (ITO), typically 90% In<sub>2</sub>O<sub>3</sub> and 10% "
        "SnO<sub>2</sub>, is the usual transparent conductor. Its typical transmission is about "
        "90%. It is deposited by e-beam evaporation or sputtering in an oxygen-containing "
        "atmosphere. The film is typically 50 to 300 nm thick, depending on the required sheet "
        "resistance and transmission. Typical resistivity is about 2 × 10<sup>−4</sup> Ω·cm. "
        "Transmission is not linear in thickness because of optical interference."))

    b.append(h3("Alignment Materials and Techniques"))
    b.append(p(
        "After the transparent electrodes are patterned, an alignment coating is applied. "
        "Depending on the mode, a homogeneous (parallel), tilted or homeotropic (vertical) "
        "alignment is achieved. The common TN LCD requires a tilted alignment to eliminate reverse "
        "tilt disclinations. Inorganic films such as obliquely evaporated SiO and organic "
        "materials such as polyimide can be used. Polyimide is the most common: it is "
        "spin-coated or printed to about 50 nm, cured at 150 to 200 °C, then buffed (rubbed) with "
        "a roller covered in cotton or synthetic fabric. For TN LCDs the process is chosen to give "
        "a pretilt of about 2 to 5°."))

    b.append(h3("Cell Spacing and Sealing"))
    b.append(p(
        "Cell assembly starts after both substrates have been rubbed. To control the cell gap "
        "accurately, spacers are applied in the active area and in the peripheral seal area. "
        "Typical spacers are glass or plastic fibres (cylinders) or spheres (balls) with a tightly "
        "controlled size distribution. A sealing adhesive such as epoxy is applied at the seal "
        "area, leaving a fill hole for LC injection. The seal is typically 1 to 3 mm wide and a "
        "few millimetres from the active area. It must not react with (contaminate) the LC and "
        "must bar moisture and contamination. After spacers and seal are applied to the first "
        "(active) substrate, it is aligned to the second (colour-filter) substrate and the seal is "
        "cured by heating, typically to 100 to 150 °C, or by ultraviolet exposure."))

    b.append(h3("LC Material Filling"))
    b.append(p(
        "The empty cell is then filled. Because the gap is small (about 5 to 10 µm), special "
        "techniques are needed. The most popular is to evacuate the cell in a vacuum chamber, dip "
        "the fill hole into a vessel of LC and raise the chamber pressure; capillary action fills "
        "the cell. The fill hole is then capped with an epoxy compatible with the LC."))

    b.append(h3("External Components"))
    b.append(p(
        "External components include polarizers, reflectors, drivers and a backlight. A reflective "
        "LCD uses a reflector at the back, modulates ambient light and needs no backlight. In the "
        "common transmissive TN LCD, a polarizer is attached to both faces after cell assembly. In "
        "the common normally white (NW) mode the polarizers are crossed and aligned with the "
        "rubbing directions. A polarizer is a three-layer film: a stretched iodine-doped polyvinyl "
        "alcohol (PVA) film in the centre, with two outer triacetyl cellulose (TAC) films "
        "protecting it from moisture, temperature and harsh environments. Typical transmission is "
        "41 to 45%, with a polarization efficiency of 99.9 to 99.99%."))
    b.append(p(
        "The row and column IC drivers are attached to the row and column bond pads by TAB "
        "(tape-automated bonding) with an anisotropic conductive adhesive (ACA), or by chip on "
        "glass (COG). For transmissive LCDs a fluorescent lamp is generally used. The R, G, B "
        "emission of the backlight and the transmission of the R, G, B filters are tuned together "
        "to obtain the desired primary colour coordinates. A diffuser provides uniform "
        "backlighting, and brightness-enhancement films may tailor the intensity distribution in "
        "the viewing cone. Specialised LCDs may add a cover glass with EMI and antireflection "
        "coatings at the front and a heater glass at the back (between backlight and LCD) for "
        "low-temperature operation."))

    b.append(h2("92.5 Liquid Crystal Display Modes"))
    b.append(p(
        "Many modes of operation have been developed. Historically the phase-change (PC) effect "
        "was discovered first, in 1968, by Wysocki et al. [16]. The same year, the dynamic "
        "scattering (DS) mode [17] and the guest–host (GH) mode [18] were announced by Heilmeier "
        "et al. In 1971 the TN mode [19] was reported by Schadt and Helfrich, and electrically "
        "controlled birefringence (ECB) by Schiekel and Fahrenschon [20] and Hareng et al. [21]. "
        "The physical effects and the modes based on them include:"))
    b.append(p(
        "<b>Current effects:</b> • DS effect<br>"
        "<b>Electric-field effects:</b> • TN effect • STN effect • ECB • GH effect • phase-change "
        "effect<br>"
        "<b>Thermal effects:</b> • smectic effect"))
    b.append(p(
        "The DS effect relies on conductivity anisotropy. Because of higher voltage and power it is "
        "no longer used. The TN and STN effects are the most widely used of all LCDs. The "
        "following discusses the various modes."))

    b.append(h3("Twisted Nematic Effect"))
    b.append(p(
        "Fig. 92.10 is a schematic of a TN display. It consists of a nematic LC with positive "
        "dielectric anisotropy (Δε > 0), about 5 µm thick, sandwiched between two transparent "
        "substrates with transparent electrodes. The electrode surfaces are coated with a "
        "polyimide alignment layer and rubbed to orient the molecules along the rubbing direction "
        "with a small (~3°) pretilt. The molecules on the two substrates are oriented 90° from "
        "each other (Fig. 92.10a); the molecular axis twists continuously through 90° from the "
        "first substrate to the second. A TN display can be made normally black (NB) or normally "
        "white (NW) depending on how the polarizers are attached. Fig. 92.10a and b show the on "
        "and off states of an NW-mode TN LCD with crossed polarizers, their polarization "
        "directions parallel to the LC director on that substrate."))
    b.append(fig(10, "en"))
    b.append(p(
        "Because the twist pitch is large compared with the visible wavelength, the polarization "
        "direction of linearly polarized light incident normally on one surface rotates through "
        "90° as it propagates through the cell and exits through the second polarizer. When a "
        "voltage is applied, the molecules align parallel to the field (Fig. 92.10b) and the 90° "
        "optical rotatory power disappears. The polarized light is then not rotated and is blocked "
        "by the crossed exit polarizer."))
    b.append(p(
        "Fig. 92.10c shows the voltage–transmission characteristics for NB and NW modes. In NW, a "
        "sufficiently high voltage aligns the molecules homeotropically and there is no rotation "
        "of the electric vector, so transmission is completely suppressed regardless of "
        "wavelength. The on-state transmission is wavelength dependent, which does not "
        "significantly affect contrast but can influence colour balance. In NB the transmission is "
        "suppressed to zero [22] in the off state only for monochromatic light of a particular "
        "wavelength. In a practical display with a broadband backlight there is therefore some "
        "light leakage that lowers contrast. In a colour display the cell gaps for the R, G, B "
        "pixels can be optimised to eliminate the leakage [22]."))
    b.append(p("The threshold voltage of a TN LCD is:"))
    b.append(eq(_eq("92.11"), "92.11"))
    b.append(p(
        "<i>V</i><sub>th</sub> depends on the dielectric anisotropy and elastic constants and is "
        "generally 2 to 3 V, with a maximum operating voltage of 5 to 8 V. This low-voltage "
        "driving, together with the low current due to the high resistivity of LCs, gives the very "
        "low power consumption (~1 mW/cm²) of LCDs. The response times, measured as the rise and "
        "decay times of the display, are [23]:"))
    b.append(eq(_eq("92.12"), "92.12"))
    b.append(eq(_eq("92.13"), "92.13"))
    b.append(p(
        "where γ is the rotational viscosity. The rise time improves with a thinner cell gap "
        "<i>d</i>, a higher Δε and a higher drive voltage <i>V</i>; the decay time improves with a "
        "smaller gap. The turn-on time τ<sub>r</sub> is usually shorter than the turn-off time "
        "τ<sub>d</sub>. At room temperature these times are of order 10 ms, adequate for many "
        "common applications such as computer and TV displays. In a TN LCD, grey scale is "
        "generated by varying the voltage along the electro-optic curve of Fig. 92.10c. The "
        "shallow slope works well for grey scale in active-matrix displays (next section), but in "
        "passive-matrix addressing it greatly limits the multiplexibility (number of addressable "
        "rows), which led to the STN effect."))

    b.append(h3("STN Effect"))
    b.append(p(
        "In a passive-matrix display the addressability, or maximum number of addressable rows "
        "<i>N</i>, is given by the Alt and Pleshko [24] limit:"))
    b.append(eq(_eq("92.14"), "92.14"))
    b.append(p(
        "where <i>V</i><sub>on</sub> and <i>V</i><sub>off</sub> are the rms voltages at selected "
        "and non-selected pixels. As <i>N</i> increases, <i>V</i><sub>off</sub> approaches "
        "<i>V</i><sub>on</sub> and the contrast ratio approaches 1, making the display unviewable. "
        "For <i>N</i> = 100, <i>V</i><sub>on</sub> = 1.11 <i>V</i><sub>off</sub>: the select "
        "voltage is only 11% above the non-select voltage. This gives a very low contrast ratio "
        "with a TN mode whose turn-on curve is shallow (Fig. 92.10c)."))
    b.append(p(
        "STN displays were developed [25, 26] to achieve a steep electro-optic curve so that many "
        "rows can be multiplexed. The STN effect uses a twist of 180° to about 270° with a "
        "relatively high pretilt. Fig. 92.11 [25] shows the voltage dependence of the midplane "
        "director tilt of a chiral nematic layer with a pretilt of 28° at both substrates. "
        "Bistability is achieved for a twist Φ greater than 245°. In highly multiplexed displays "
        "twist angles of 240° to 275° and tilt angles of 5° to 30° are generally used. High "
        "pretilts eliminate a competing distortion with 180° less twist. For a 270° left-handed "
        "twist, optimum results are obtained when the front polarizer axis makes 30° with the LC "
        "director and the rear polarizer makes 60° with the projection of the director on the rear "
        "substrate. Because of interference of the normal optical modes, the display has a yellow "
        "birefringence colour in the non-select state (yellow mode). Rotating one polarizer by 90° "
        "gives a complementary image with a bright colourless state and a blue non-select state "
        "(blue mode). White-mode STN displays use retardation films. The response time of a "
        "typical STN display is about 150 ms; these displays generally have lower contrast and a "
        "narrower viewing angle."))
    b.append(fig(11, "en"))

    b.append(h3("Electrically Controlled Birefringence (ECB)"))
    b.append(p(
        "This technique controls the birefringence of the cell with an electric field. There are "
        "several types depending on the molecular orientation: DAP, homogeneous, HAN (hybrid "
        "aligned nematic) and IPS (in-plane switching). A DAP cell (homeotropic) uses an LC with "
        "negative Δε between transparent electrode substrates and crossed polarizers, as in Fig. "
        "92.12. In the off state (no field) the incident polarized light sees no birefringence and "
        "is blocked by the crossed exit polarizer. In the on state the molecular axis is inclined "
        "at θ (Fig. 92.12), so the linearly polarized light becomes elliptically polarized and "
        "part of it passes the crossed polarizer; the transmitted intensity <i>I</i> is [20]:"))
    b.append(eq(_eq("92.15"), "92.15"))
    b.append(fig(12, "en"))
    b.append(p(
        "where <i>I</i><sub>0</sub> is the incident intensity, φ the angle between the incident "
        "polarization and the oscillation direction of the ordinary light in the cell, <i>d</i> "
        "the cell gap, Δ<i>n</i>(<i>V</i>) the birefringence, <i>d</i>Δ<i>n</i> the optical phase "
        "difference and λ the wavelength. <i>I</i> thus depends on the applied voltage and λ."))
    b.append(p(
        "In the homogeneous technique the cell uses a positive material with homogeneous "
        "orientation; the threshold voltage is obtained by replacing the bend constant "
        "<i>K</i><sub>33</sub> with the splay constant <i>K</i><sub>11</sub>. The HAN cell has a "
        "hybrid orientation: molecules perpendicular to one substrate but parallel to the other. "
        "Both positive and negative Δε materials can be used, and since there is no clear "
        "threshold it has the advantage of a very low drive voltage. Recently an IPS-based ECB "
        "mode has been developed for extremely wide viewing angles. In IPS the LC is homogeneously "
        "aligned and switched by interdigitated electrodes on one substrate [27], using an NB mode "
        "with positive or negative Δε."))

    b.append(h3("Guest–Host Type"))
    b.append(p(
        "Some organic dyes show anisotropic absorption: they absorb more in a given wavelength "
        "band when the light's <b>E</b> vector is parallel to the dye's optic axis than when it is "
        "perpendicular. Displays based on this are called guest–host (GH). A small amount of a "
        "dichroic dye (guest) is mixed into the LC (host); the dye aligns with the LC, so its "
        "orientation can be changed by an applied field. With a positive-Δε LC, in the off state "
        "the <b>E</b> vector coincides with the dye absorption axis, so light is absorbed and the "
        "transmitted light is coloured. In the on state the <b>E</b> vector is orthogonal to the "
        "absorption axis, so there is no absorption and the transmitted light is white. A GH LCD "
        "needs only one polarizer and, because the effect is absorptive, gives a better viewing "
        "angle than a TN LCD."))

    b.append(h3("Phase-Change Type"))
    b.append(p(
        "The phase-change display relies on a change from a helical cholesteric phase to a "
        "homeotropic nematic phase and back. It uses a cholesteric LC with a long pitch and "
        "positive or negative Δε, and no polarizers. In the off state the incident light passing "
        "through the focal-conic cholesteric cell is optically scattered, so the cell looks "
        "cloudy. When a voltage is applied the helical structure changes to a homeotropic nematic "
        "phase and the cell becomes transparent."))

    b.append(h3("Thermal Effects"))
    b.append(p(
        "Thermal effects rely on a change in electro-optical behaviour when the LC is heated or "
        "cooled, and are used with homeotropically aligned smectic LCs. When the cell is heated to "
        "the isotropic phase and cooled, sudden cooling makes it cloudy while gradual cooling "
        "makes it transparent. The cloudy and transparent states correspond to the focal-conic and "
        "homeotropic orientations of smectic A. The effect is used for large memory-type displays "
        "in which a laser writes the image thermally. Heating can also be done by one transparent "
        "electrode, with the other acting as the signal electrode."))

    b.append(h2("92.6 Display Addressing"))
    b.append(p(
        "Addressing (driving) techniques strongly influence LCD image quality. They fall into "
        "three types: direct (static), passive matrix and active matrix. For low-information "
        "displays such as numeric displays, bar graphs and other fixed patterns using segmented "
        "electrodes, direct addressing is used. A common example is a numeric display with seven "
        "segments per digit; each segment on the front substrate and the common electrode on the "
        "back are connected directly to drive signals, and a voltage is selectively applied to "
        "each segment to show any digit from 0 to 9. For high-information displays this becomes "
        "impractical because of the huge number of interconnects, so passive or active matrix "
        "addressing is used."))

    b.append(h3("Passive Matrix Addressing"))
    b.append(p(
        "A passive matrix (PM) display — an LC between a matrix of transparent row and column "
        "electrodes (Fig. 92.8) — is the simplest and least expensive matrix-addressed LCD to "
        "manufacture. An example is a colour (R, G, B) VGA display using the STN effect, with a "
        "pixel format of 640 (× 3 = 1920) H × 480 V, i.e. 1920 columns and 480 rows, for 2400 "
        "interconnects addressing 921,600 pixels. In PM addressing the row voltages are scanned in "
        "succession with <i>V</i><sub>r</sub>, while all columns in a row are driven in parallel "
        "during the row time with ±<i>V</i><sub>c</sub> depending on whether the pixel is selected "
        "on or off. As discussed under the STN effect, the contrast of PM LCDs is limited by the "
        "Alt–Pleshko addressability limit [24]. To improve the operating margin, DSTN (dual-scan "
        "STN) is used in higher-information displays: the display is split into two halves whose "
        "rows are scanned simultaneously and synchronously, essentially doubling the duty ratio of "
        "the on pixels. A major shortcoming of the passive-matrix STN display is the slow LC "
        "response, of order 150 ms — inadequate for video and barely fast enough for a computer's "
        "graphical interface. It can be improved by active addressing or multiline addressing "
        "[28, 29], which address several rows simultaneously to suppress the frame response of "
        "conventional STN LCDs."))

    b.append(h3("Active Matrix Addressing"))
    b.append(p(
        "Active matrix (AM) addressing removes the multiplexing limitations [24] of PM LCDs by "
        "placing a nonlinear control element in series with each pixel, providing a 100% duty "
        "ratio from the charge stored at the pixel during the row time. Fig. 92.13a illustrates an "
        "active matrix array with row and column drivers and the associated module electronics; "
        "Fig. 92.13b is a magnified view of the array. In the figure <i>C</i><sub>LC</sub> and "
        "<i>C</i><sub>S</sub> are the pixel capacitance and the pixel storage capacitance. A "
        "storage capacitor <i>C</i><sub>S</sub> is usually incorporated at each pixel to reduce the "
        "pixel voltage offset (Eq. 92.16) and for broad temperature operation. Fig. 92.14 shows a "
        "cross-section through an AM LCD; Fig. 92.15 shows a typical pixel with the gate and data "
        "buses, the thin-film transistor (TFT), the ITO pixel electrode and the storage "
        "capacitor."))
    b.append(fig(13, "en"))
    b.append(fig(14, "en"))
    b.append(fig(15, "en"))
    b.append(p(
        "Fabrication of the active matrix substrate is a major aspect of AM LCD manufacturing. "
        "Both two-terminal devices (back-to-back diodes and metal–insulator–metal, MIM, diodes) and "
        "three-terminal TFTs have been developed. Two-terminal devices are simple and cheap but "
        "suffer from non-uniform performance (breakdown/threshold voltage) over a large area and "
        "from incomplete isolation of the pixel when neighbours are addressed. For superior image "
        "quality, AM LCDs use a TFT, which isolates the pixel completely. Large-area AM LCDs use "
        "amorphous silicon (a-Si) TFTs [6], while polysilicon TFTs with integrated row and column "
        "drivers are used in small high-resolution LCDs [30]."))
    b.append(p(
        "Fig. 92.16 shows the equivalent circuit of a TFT-LCD pixel, the drive waveforms and the "
        "resulting pixel voltage. As in most line-at-a-time matrix displays, the rows (gates) are "
        "scanned with a select pulse <i>V</i><sub>g,sel</sub> during the frame time "
        "<i>t</i><sub>f</sub>, while all pixels in a row are addressed simultaneously with the data "
        "voltage ±<i>V</i><sub>d</sub> during the row time <i>t</i><sub>r</sub> (= "
        "<i>t</i><sub>f</sub>/<i>N</i>). During the row time the select gate voltage turns the TFT "
        "on and charges the pixel and storage capacitor to <i>V</i><sub>d</sub>. After the row "
        "time the TFT is switched off by the non-select gate voltage "
        "<i>V</i><sub>g,non-sel</sub>, isolating the pixel charge until the next frame. The LC "
        "pixel must be driven in an ac fashion with +<i>V</i><sub>d</sub> and −<i>V</i><sub>d</sub> "
        "on alternate frames, with no net dc across the pixel; a net dc causes flicker and image "
        "sticking [33] due to LC conductivity, and large sustained dc voltages degrade the LC by "
        "electrolysis. The pixel-voltage shift Δ<i>V</i><sub>p</sub> at the end of the row time is "
        "due to the parasitic gate-to-drain capacitance <i>C</i><sub>gd</sub> of the TFT."))
    b.append(fig(16, "en"))
    b.append(p(
        "When the gate voltage switches, the redistribution of charge from the gate dielectric "
        "gives the pixel-voltage shift Δ<i>V</i><sub>p</sub>:"))
    b.append(eq(_eq("92.16"), "92.16"))
    b.append(p(
        "For an n-channel enhancement-mode a-Si TFT this shift is negative in both the positive "
        "and negative frames; it therefore helps pixel charging in the negative frame and hinders "
        "it in the positive frame. Moreover, the increased gate bias during the negative frame "
        "lets the pixel reach the data voltage much faster, so the TFT is designed for the "
        "worst-case positive frame. Δ<i>V</i><sub>p</sub> is reduced by minimising "
        "<i>C</i><sub>gd</sub> (a smaller source–drain overlap) and by using a storage capacitor, "
        "and is compensated by adjusting the common electrode voltage <i>V</i><sub>com</sub> as "
        "shown in Fig. 92.16. Since <i>C</i><sub>lc</sub> is a function of <i>V</i><sub>p</sub> "
        "(<i>V</i><sub>lc</sub>) through the dielectric anisotropy, adjusting "
        "<i>V</i><sub>com</sub> alone does not eliminate dc for all grey levels, and the grey-scale "
        "voltages must be modified to compensate."))

    b.append(h3("Display Module Electronics"))
    b.append(p(
        "Fig. 92.13 is a block diagram of the electronics of an AM LCD module. The control block "
        "and the power-supply generation are mounted separately on a printed-circuit board and "
        "connected to the row and column drivers on one side and to the host controller on the "
        "other. The control block may include level shifters, timing generators and, in some "
        "cases, analog functions; it takes digital data from the host system (typically a graphics "
        "controller chip) and converts it into the timing and signal levels required by the "
        "drivers. The architecture and design of the module electronics, including the drivers, "
        "strongly affect not only system cost and power consumption but also image quality. The LC "
        "material typically needs about 5 V for optical saturation (Fig. 92.10c); with ac drive "
        "the required swing across the LC is about 10 V. To achieve this, column drivers typically "
        "use 12 V supplies. The column-driver voltage can be reduced by <i>V</i><sub>com</sub> "
        "modulation: the <i>V</i><sub>com</sub> node (connected to all pixels) is driven above and "
        "below the 5 V range of the column drivers, alternating every row time, so that 10 V is "
        "obtained across the LC with 5 V drivers. This needs extra components and power because of "
        "the oscillation, and to avoid capacitive injection the row drivers usually have their "
        "negative supply modulated at the same frequency. Compared with 10 V column drivers, 5 V "
        "drivers consume less power and are simpler to design and fabricate in small-geometry "
        "CMOS. The <i>V</i><sub>com</sub> modulation method can be used only with row (polarity) "
        "inversion, which results in some horizontal cross-talk; column and pixel inversion give "
        "better image quality with much-reduced cross-talk but cannot be used with "
        "<i>V</i><sub>com</sub> modulation."))

    b.append(h2("References"))
    b.append(refs(_REFS))
    return "".join(b)


def build(lang):
    vi = lang == "vi"
    switch = ("%s%s/" % (BASE_EN, CSLUG)) if vi else ("%s%s/" % (BASE_VI, CSLUG))
    title = ("Chương 92 — %s · Sổ tay Đo lường, Thiết bị đo và Cảm biến" % TITLE_VI if vi
             else "Chapter 92 — %s · Measurement, Instrumentation and Sensors Handbook" % TITLE_EN)
    desc = ("Bản dịch tiếng Việt Chương 92 “Màn hình tinh thể lỏng” của Kalluri R. Sarma — các "
            "loại vật liệu tinh thể lỏng, dị hướng điện môi và chiết suất, hằng số đàn hồi, đặc "
            "trưng quang điện, vật liệu và quy trình chế tạo LCD, các chế độ hiển thị TN/STN/ECB/"
            "GH/chuyển pha/nhiệt và các phương pháp quét địa chỉ ma trận thụ động và chủ động, "
            "với 16 hình, 16 phương trình và 30 tài liệu tham khảo." if vi
            else
            "Companion to Chapter 92 of the CRC Measurement Handbook — liquid crystal materials, "
            "dielectric and refractive-index anisotropy, elastic constants, electro-optical "
            "characteristics, LCD materials and fabrication, the TN/STN/ECB/GH/phase-change/"
            "thermal modes, and passive and active matrix addressing, with 16 figures, 16 "
            "equations and 30 references.")
    crumb = ('<a href="/vi/books/">Sách</a> · <a href="%s">Sổ tay Đo lường, Thiết bị đo và Cảm biến</a> · '
             'Chương 92' % BASE_VI if vi else
             '<a href="/books/">Books</a> · <a href="%s">Measurement, Instrumentation and Sensors '
             'Handbook</a> · Chapter 92' % BASE_EN)
    meta = ("Chương 92 · theo Ch92.pdf (CRC Press, 1999) · 16 hình, 16 phương trình" if vi
            else "Chapter 92 · 16 figures, 16 equations")
    body = ('<main><article class="intranet-content reader"><div class="reader-hero">'
            '<div class="breadcrumb">%s</div><h1>%s</h1><p class="byline">%s</p>'
            '<div class="meta-line">%s</div></div><div class="prose">%s</div>%s</article></main>'
            % (crumb, TITLE_VI if vi else TITLE_EN, BYLINE if vi else BYLINE_EN, meta,
               body_vi() if vi else body_en(), chapter_nav(lang, 92)))
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
