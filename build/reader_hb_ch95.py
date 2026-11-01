# -*- coding: utf-8 -*-
"""Handbook Chapter 95 — Light-Emitting Diode Displays
(Mohammad A. Karim, University of Tennessee, Knoxville).

Writes the full Vietnamese translation and the English companion.
Run:  python build/reader_hb_ch95.py
"""
import os

import hb95fig as F
from reader_handbook import SLUG, head, header, footer
from chapter_nav import nav as chapter_nav

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSLUG = "ch95-light-emitting-diode-displays"
TITLE_EN = "Light-Emitting Diode Displays"
TITLE_VI = "Hiển thị LED"
BYLINE = "Mohammad A. Karim · University of Tennessee, Knoxville"
BASE_EN = "/books/read/%s/" % SLUG
BASE_VI = "/vi/books/read/%s/" % SLUG


def fig(num, key, lang="vi"):
    svg, cap_vi, cap_en, _av, _ae = key
    return ('<figure class="figure" id="fig-95-%d">%s<figcaption class="figcap">%s</figcaption>'
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


def table(hd, rows, cap, cls=""):
    body = "".join("<tr>%s</tr>" % "".join("<td>%s</td>" % c for c in r) for r in rows)
    return ('<div class="table-wrap"><table class="tbl%s"><thead><tr>%s</tr></thead><tbody>%s'
            '</tbody></table></div><p style="font-size:.84rem;color:#888;font-style:italic">%s</p>'
            % (cls, "".join("<th>%s</th>" % h for h in hd), body, cap))


# ================================================================ EQUATIONS
# One shared dictionary so the Vietnamese and English pages cannot drift.
_EQ = {
    "95.1": "d<i>n</i>/d<i>t</i> = <i>B</i><sub>r</sub><i>np</i>",
    "95.3": "η = <i>R</i><sub>r</sub> / (<i>R</i><sub>r</sub> + <i>R</i><sub>nr</sub>)",
    "95.4": "Δ<i>p</i> = Δ<i>n</i> = Δ<i>n</i><sub>0</sub><i>e</i><sup>−<i>t</i>/τ</sup>",
    "95.5": "(1/τ) = (1/τ<sub>r</sub>) + (1/τ<sub>nr</sub>)",
    "95.6": ("∂Δ<i>n</i><sub>p</sub>/∂<i>t</i> = <i>D</i><sub>n</sub>"
             "∂<sup>2</sup>Δ<i>n</i><sub>p</sub>/∂<i>x</i><sup>2</sup> "
             "− Δ<i>n</i><sub>p</sub>/τ"),
    "95.7": ("Δ<i>n</i><sub>p</sub>(<i>x</i>,<i>t</i>) = ⟨Δ<i>n</i><sub>p</sub>(<i>x</i>)⟩ "
             "+ <i>n</i>′<sub>p</sub>(<i>x</i>)<i>e</i><sup>jω<i>t</i></sup>"),
    "95.8a": ("∂<sup>2</sup>/∂<i>x</i><sup>2</sup>⟨Δ<i>n</i><sub>p</sub>(<i>x</i>)⟩ = "
              "⟨Δ<i>n</i><sub>p</sub>(<i>x</i>)⟩/(<i>L</i><sub>n</sub>)<sup>2</sup>"),
    "95.8b": ("∂<sup>2</sup>/∂<i>x</i><sup>2</sup>[Δ<i>n</i>′<sub>p</sub>(<i>x</i>)] = "
              "Δ<i>n</i>′<sub>p</sub>(<i>x</i>)/[<i>L</i><sup>*</sup><sub>n</sub>]<sup>2</sup>"),
    "95.9a": "<i>L</i><sup>*</sup><sub>n</sub> = <i>L</i><sub>n</sub>/(1 + jωτ)<sup>1/2</sup>",
    "95.9b": "<i>L</i><sub>n</sub> = (<i>D</i><sub>n</sub>τ)<sup>1/2</sup>",
    "95.10": ("Δ<i>n</i>′<sub>p</sub>(<i>x</i>) = Δ<i>n</i>′<sub>p</sub>(0)"
              "<i>e</i><sup>−<i>x</i>/<i>L</i>*</sup>"),
    "95.11": ("<i>I</i>(ω) = |<i>eAD</i><sub>n</sub> d<i>n</i>′<sub>p</sub>(<i>x</i>)"
              "/d<i>x</i>|<sub><i>x</i>=0</sub> = <i>I</i>(0)/(1 + ω<sup>2</sup>τ<sup>2</sup>)"
              "<sup>1/2</sup>"),
    "95.12": "Δω = 1/τ<sub>r</sub>",
    "95.13": ("<i>R</i><sub>nr</sub> = [<i>B</i><sub>r</sub>(<i>n</i><sub>0</sub> + Δ<i>n</i>)"
              "(<i>p</i><sub>0</sub> + Δ<i>p</i>) − <i>B</i><sub>r</sub><i>n</i><sub>0</sub>"
              "<i>p</i><sub>0</sub>] = <i>B</i><sub>r</sub>(<i>n</i><sub>0</sub> + "
              "<i>p</i><sub>0</sub> + Δ<i>n</i>)Δ<i>n</i>"),
    "95.14": ("τ<sub>r</sub> = Δ<i>n</i>/<i>R</i><sub>nr</sub> = [<i>B</i><sub>r</sub>"
              "(<i>n</i><sub>0</sub> + <i>p</i><sub>0</sub> + Δ<i>n</i>)]<sup>−1</sup>"),
    "95.15": "Δ<i>n</i> = <i>J</i>τ<sub>r</sub>/<i>ed</i>",
    "95.16": ("τ<sub>r</sub> = [{(<i>n</i><sub>0</sub> + <i>p</i><sub>0</sub>)<sup>2</sup> + "
              "(4<i>J</i>/<i>B</i><sub>r</sub><i>ed</i>)}<sup>1/2</sup> − "
              "(<i>n</i><sub>0</sub> + <i>p</i><sub>0</sub>)]/(2<i>J</i>/<i>ed</i>)"),
    "95.17a": "τ<sub>r</sub> ≈ [<i>B</i><sub>r</sub>(<i>n</i><sub>0</sub> + "
              "<i>p</i><sub>0</sub>)]<sup>1/2</sup>",
    "95.17b": "τ<sub>r</sub> ≈ (<i>ed</i>/<i>JB</i><sub>r</sub>)<sup>1/2</sup>",
    "95.18": "θ<sub>c</sub> = sin<sup>−1</sup>(<i>n</i><sub>2</sub>/<i>n</i><sub>1</sub>)",
    "95.19": ("<i>T</i> = 1 − {(<i>n</i><sub>1</sub> − <i>n</i><sub>2</sub>)/"
              "(<i>n</i><sub>1</sub> + <i>n</i><sub>2</sub>)}<sup>2</sup>"),
}

# Equation 95.2 carries the decimal separator, so it is built per language.
_EQ2 = "λ = <i>hc</i>/<i>E</i><sub>g</sub> = %s<i>E</i><sub>g</sub> (eV)"

# Equation 95.20 is a four-line chain; only the first line is language-bearing.
_EQ20_L1 = {
    "vi": ("η<sub>LED</sub> = <i>T</i>[(góc khối trong nón)/(4π)]"),
    "en": ("η<sub>LED</sub> = <i>T</i>[(solid angle within the cone)/(4π)]"),
}
_EQ20_TAIL = [
    "(<i>T</i>/2)(1 − cos θ<sub>c</sub>)",
    "(<i>T</i>/4)sin<sup>2</sup>θ<sub>c</sub>",
    ("(1/4)(<i>n</i><sub>2</sub>/<i>n</i><sub>1</sub>)<sup>2</sup>"
     "[1 − {(<i>n</i><sub>1</sub> − <i>n</i><sub>2</sub>)/"
     "(<i>n</i><sub>1</sub> + <i>n</i><sub>2</sub>)}<sup>2</sup>]"),
]


def _eq(lang, num):
    if num == "95.2":
        return _EQ2 % ("1,24/" if lang == "vi" else "1.24/")
    return _EQ[num]


def _eq20(lang):
    lines = [_EQ20_L1[lang]] + _EQ20_TAIL
    return '<div class="eq"><span class="n">(95.20)</span>%s</div>' % (
        "<br>".join("%s%s" % ("" if i == 0 else "&nbsp;=&nbsp;", ln)
                    for i, ln in enumerate(lines)))


# ================================================================ TABLE 95.1
_T1 = [
    ("III–V", "GaN", "3,5", "UV"),
    ("II–VI", "ZnS", "3,8", "UV"),
    ("II–VI", "SnO<sub>2</sub>", "3,5", "UV"),
    ("II–VI", "ZnO", "3,2", "UV"),
    ("III–VII", "CuCl", "3,1", "UV"),
    ("II–VI", "BeTe", "2,8", "UV"),
    ("III–VII", "CuBr", "2,9", "UV — khả kiến"),
    ("II–VI", "ZnSe", "2,7", "Khả kiến"),
    ("III–VI", "In<sub>2</sub>O<sub>3</sub>", "2,7", "Khả kiến"),
    ("II–VI", "CdS", "2,52", "Khả kiến"),
    ("II–VI", "ZnTe", "2,3", "Khả kiến"),
    ("III–V", "GaAs", "1,45", "IR"),
    ("II–VI", "CdSe", "1,75", "IR — khả kiến"),
    ("II–VI", "CdTe", "1,5", "IR"),
    ("III–VI", "GaSe", "2,1", "Khả kiến"),
]

_T1_EN = [
    ("III–V", "GaN", "3.5", "UV"),
    ("II–VI", "ZnS", "3.8", "UV"),
    ("II–VI", "SnO<sub>2</sub>", "3.5", "UV"),
    ("II–VI", "ZnO", "3.2", "UV"),
    ("III–VII", "CuCl", "3.1", "UV"),
    ("II–VI", "BeTe", "2.8", "UV"),
    ("III–VII", "CuBr", "2.9", "UV — visible"),
    ("II–VI", "ZnSe", "2.7", "Visible"),
    ("III–VI", "In<sub>2</sub>O<sub>3</sub>", "2.7", "Visible"),
    ("II–VI", "CdS", "2.52", "Visible"),
    ("II–VI", "ZnTe", "2.3", "Visible"),
    ("III–V", "GaAs", "1.45", "IR"),
    ("II–VI", "CdSe", "1.75", "IR — visible"),
    ("II–VI", "CdTe", "1.5", "IR"),
    ("III–VI", "GaSe", "2.1", "Visible"),
]


def _table1(lang):
    hd = (["Nhóm", "Vật liệu", "<i>E</i><sub>g</sub> (eV)", "Kiểu phát xạ"] if lang == "vi"
          else ["Group", "Material", "<i>E</i><sub>g</sub> (eV)", "Emission type"])
    cap = ("Bảng 95.1 · Các chất bán dẫn hai nguyên thích hợp để chế tạo LED."
           if lang == "vi" else
           "TABLE 95.1 · Binary semiconductors suitable for LED fabrication.")
    return hd, (_T1 if lang == "vi" else _T1_EN), cap, ""


# ================================================================ REFERENCES
_REFS = [
    "M.A. Karim, <i>Electro-Optical Devices and Systems</i>, Boston: PWS-Kent Publishing, 1990.",
    "M.A. Karim (ed.), <i>Electro-Optical Displays</i>, New York: Marcel Dekker, 1992.",
    "L.E. Tannas, Jr. (ed.), <i>Flat-Panel Displays and CRTs</i>, New York: Van Nostrand Reinhold, 1985.",
    "T. Uchida, Multicolored Liquid Crystal Displays, <i>Opt. Eng.</i>, 23, 247–252, 1984.",
    "J. Wilson and J.F.B. Hawkes, <i>Optoelectronics: An Introduction</i>, Englewood Cliffs, NJ: "
    "Prentice-Hall International, 1985.",
]


# ================================================================ VIETNAMESE
def body_vi():
    b = []

    b.append(p(
        "Điốt phát quang (LED) là một điốt chuyển tiếp <i>p–n</i> bán dẫn đặc biệt phát ra ánh sáng "
        "khi được phân cực thuận. Quá trình phát sáng ở đây là điện phát quang, gắn với bước sóng "
        "phát xạ nằm trong vùng khả kiến và hồng ngoại của phổ. Khi đặt phân cực thuận lên chuyển "
        "tiếp <i>p–n</i>, các hạt tải được bơm vào vùng nghèo với mật độ lớn. Do ở gần nhau về mặt "
        "không gian, các cặp điện tử–lỗ trống tái hợp, và sự tái hợp này gắn với việc phát xạ năng "
        "lượng. Tuỳ theo đặc trưng vùng cấm của chất bán dẫn, năng lượng phát xạ có thể ở dạng nhiệt "
        "(phonon) hoặc ánh sáng (photon)."))
    b.append(p(
        "Nghiệm phương trình Schrödinger cho một tinh thể điển hình cho thấy tồn tại các vùng "
        "Brillouin. Đồ thị năng lượng <i>E</i> của một điện tử trong chất rắn theo vectơ sóng "
        "<i>k</i> biểu diễn các vùng năng lượng được phép. Có thể nhận thấy mạng tinh thể ảnh hưởng "
        "tới chuyển động của điện tử khi <i>k</i> gần <i>n</i>π/<i>l</i> (trong đó <i>n</i> là số "
        "nguyên bất kỳ và <i>l</i> là chu kỳ tinh thể); hệ quả của ràng buộc này là xuất hiện một "
        "khe năng lượng giữa các vùng năng lượng được phép. Hình 95.1a trình bày một phần hai "
        "đường <i>E</i> theo <i>k</i> của các vùng lân cận trong phạm vi <i>k</i> = π/<i>l</i> và "
        "<i>k</i> = −π/<i>l</i> (còn gọi là vùng rút gọn)."))

    b.append(fig(1, F.fig(1)))

    b.append(p(
        "Trong khi nhánh trên của Hình 95.1a biểu diễn năng lượng của các điện tử vùng dẫn, độ cong "
        "của nhánh dưới có thể gắn với các điện tử có khối lượng hiệu dụng âm. Khái niệm khối lượng "
        "hiệu dụng âm có thể nhận diện được nhờ khái niệm lỗ trống trong vùng hoá trị. Trong khi "
        "phần lớn điện tử được đồng nhất với các cực tiểu của đường <i>E–k</i> phía trên, phần lớn "
        "lỗ trống được đồng nhất với các cực đại của đường <i>E–k</i> phía dưới. Cực tiểu của năng "
        "lượng vùng dẫn và cực đại của năng lượng vùng hoá trị trong Hình 95.1a cùng có giá trị "
        "<i>k</i> như nhau. Chất bán dẫn có đặc trưng như vậy được gọi là có vùng cấm trực tiếp, và "
        "sự tái hợp gắn với nó được gọi là tái hợp trực tiếp."))
    b.append(p(
        "Tái hợp trực tiếp của một cặp điện tử–lỗ trống luôn dẫn tới phát xạ một photon. Trong chất "
        "bán dẫn vùng cấm trực tiếp, photon phát xạ không gắn với thay đổi xung lượng nào (cho bởi "
        "<i>hk</i>/2π), do đó Δ<i>k</i> = 0. Tuy nhiên, với một số vật liệu bán dẫn, đường <i>E</i> "
        "theo <i>k</i> có thể khác đi, như trên Hình 95.1b: năng lượng cực tiểu của vùng dẫn có thể "
        "ứng với <i>k</i> khác không, còn năng lượng cực đại của vùng hoá trị ứng với <i>k</i> = 0. "
        "Tái hợp điện tử–lỗ trống trong chất bán dẫn như vậy được gọi là gián tiếp."))
    b.append(p(
        "Tái hợp gián tiếp bao gồm một điều chỉnh xung lượng. Phần lớn năng lượng phát xạ bị tiêu "
        "tán dưới dạng nhiệt (phonon). Rất ít năng lượng còn lại cho việc phát xạ photon, mà trong "
        "hầu hết các trường hợp là một quá trình rất chậm. Hơn nữa, vì cả phonon và photon đều tham "
        "gia vào trao đổi năng lượng này, những chuyển mức như vậy ít có khả năng xảy ra. Tốc độ "
        "tái hợp giữa các vùng về cơ bản được cho bởi"))

    b.append(eq(_eq("vi", "95.1"), "95.1"))

    b.append(p(
        "trong đó <i>B</i><sub>r</sub> là một hằng số phụ thuộc tái hợp; với chất bán dẫn vùng cấm "
        "trực tiếp, hằng số này lớn hơn khoảng 10<sup>6</sup> lần so với chất bán dẫn vùng cấm gián "
        "tiếp. Với tái hợp trực tiếp, giá trị <i>B</i><sub>r</sub> nằm trong khoảng 0,46 × "
        "10<sup>−10</sup> đến 7,2 × 10<sup>−10</sup> cm<sup>3</sup>/s."))
    b.append(p(
        "Tất cả các tinh thể bán dẫn đơn chất đều giống nhau, chỉ khác nhau ở đặc trưng vùng cấm. Si "
        "và Ge đều có chuyển mức vùng gián tiếp, trong khi GaAs là chất bán dẫn có chuyển mức vùng "
        "trực tiếp. Do đó, Si và Ge thích hợp để chế tạo transistor và mạch tích hợp, còn GaAs thích "
        "hợp để chế tạo LED."))
    b.append(p(
        "Tái hợp trực tiếp (khi <i>k</i> = hằng số) cho phát xạ photon có bước sóng (tính bằng "
        "micrômét) là"))

    b.append(eq(_eq("vi", "95.2"), "95.2"))

    b.append(p(
        "trong đó <i>E</i><sub>g</sub> là năng lượng vùng cấm. Khi được phân cực thuận thích hợp, "
        "LED có thể hoạt động trong vùng tử ngoại, khả kiến và hồng ngoại. Tuy nhiên, với vùng khả "
        "kiến, cần quan tâm tới các đường cong hiệu quả sáng phổ của Hình 95.2, vì chúng phản ánh "
        "thực tế rằng đáp ứng thị giác với bất kỳ bước sóng phát xạ nào là một hàm của bước sóng. "
        "Đáng tiếc là không có một chất bán dẫn đơn chất nào thích hợp để chế tạo LED, nhưng có "
        "nhiều hợp chất hai nguyên và ba nguyên có thể dùng cho mục đích này. Bảng 95.1 liệt kê một "
        "số chất bán dẫn hai nguyên như vậy. Các chất bán dẫn ba nguyên gồm GaAlAs, CdGeP<sub>2</sub> "
        "và ZnGeP<sub>2</sub> cho hoạt động trong vùng hồng ngoại, CuGaS<sub>2</sub> và "
        "AgInS<sub>2</sub> cho vùng khả kiến, còn CuAlS<sub>2</sub> cho vùng tử ngoại. Các chất bán "
        "dẫn ba nguyên được dùng vì năng lượng vùng cấm của chúng có thể được điều chỉnh tới bước "
        "sóng phát xạ mong muốn bằng cách chọn thành phần thích hợp."))

    b.append(fig(2, F.fig(2)))
    b.append(table(*_table1("vi")))

    b.append(p(
        "Một ví dụ về hợp chất ba nguyên là gali asen-photpho (viết là "
        "GaAs<sub>1−<i>x</i></sub>P<sub><i>x</i></sub>), vốn là sự kết hợp cơ bản của hai chất bán "
        "dẫn hai nguyên, cụ thể là GaAs và GaP. Năng lượng vùng cấm tương ứng của chất bán dẫn có "
        "thể được thay đổi bằng cách thay đổi giá trị của <i>x</i>. Ví dụ, khi <i>x</i> = 0, "
        "<i>E</i><sub>g</sub> = 1,43 eV. <i>E</i><sub>g</sub> tăng khi <i>x</i> tăng cho tới "
        "<i>x</i> = 0,44 và <i>E</i><sub>g</sub> = 1,977 eV, như trên Hình 95.3. Tuy nhiên, với "
        "<i>x</i> ≥ 0,45, vùng cấm là gián tiếp. Thành phần phổ biến nhất của "
        "GaAs<sub>1−<i>x</i></sub>P<sub><i>x</i></sub> dùng trong LED là <i>x</i> = 0,4 và "
        "<i>E</i><sub>g</sub> ≈ 1,3 eV. Năng lượng vùng cấm này ứng với phát xạ màu đỏ. Máy tính và "
        "đồng hồ thường dùng thành phần đặc biệt này của GaAs<sub>1−<i>x</i></sub>P<sub><i>x</i></sub>."))

    b.append(fig(3, F.fig(3)))

    b.append(p(
        "Điều thú vị là chất bán dẫn GaAs<sub>1−<i>x</i></sub>P<sub><i>x</i></sub> gián tiếp (với "
        "1 ≥ <i>x</i> ≥ 0,45) có thể được dùng để phát sáng trong dải từ vàng qua lục nếu được pha "
        "tạp các tạp chất như nitơ. Các chất pha tạp đưa vào chất bán dẫn sẽ thay thế các nguyên tử "
        "photpho, từ đó tạo ra các mức bẫy điện tử nằm rất gần vùng dẫn. Ví dụ, với <i>x</i> = 0,5, "
        "pha tạp nitơ làm tăng hiệu suất của LED từ 0,01 lên 1%, như trên Hình 95.4. Tuy nhiên, cần "
        "lưu ý rằng pha tạp nitơ làm dịch bước sóng đỉnh phát xạ về phía đỏ. Độ dịch tương đối lớn "
        "hơn tại và quanh <i>x</i> = 0,5 so với <i>x</i> = 1,0. Phát xạ năng lượng trong các linh "
        "kiện GaAs<sub>1−<i>x</i></sub>P<sub><i>x</i></sub> pha tạp nitơ là một hàm của cả <i>x</i> "
        "và nồng độ nitơ."))

    b.append(fig(4, F.fig(4)))

    b.append(p(
        "Nitơ là một loại tạp chất khác với những tạp chất thường gặp trong chất bán dẫn ngoại lai. "
        "Nitơ, giống như asen và photpho, có năm điện tử hoá trị, nhưng nó không đưa thêm hạt tải "
        "điện tích nào vào mạng tinh thể. Nó tạo ra các tâm tái hợp bức xạ hoạt động trong các vật "
        "liệu có vùng cấm gián tiếp. Với một điện tử, một tâm tái hợp là một trạng thái trống trong "
        "khe năng lượng mà điện tử rơi vào, và sau đó rơi vào vùng hoá trị bằng cách tái hợp với "
        "một lỗ trống. Ví dụ, trong khi LED GaP phát ra ánh sáng lục (2,23 eV), LED GaP pha tạp nitơ "
        "phát ra ánh sáng lục hơi vàng (2,19 eV), và LED GaP pha tạp nitơ mạnh phát ra ánh sáng "
        "vàng (2,1 eV)."))

    b.append(h2("Hiệu suất lượng tử nội", "Internal quantum efficiency"))

    b.append(p(
        "Các hạt tải dư được bơm vào chất bán dẫn có thể tái hợp hoặc bức xạ hoặc không bức xạ. "
        "Trong khi tái hợp không bức xạ sinh ra phonon, tái hợp bức xạ sinh ra photon. Do đó, hiệu "
        "suất lượng tử nội η, định nghĩa là tỉ số giữa tốc độ tái hợp bức xạ <i>R</i><sub>r</sub> "
        "và tốc độ tái hợp tổng cộng, được cho bởi"))

    b.append(eq(_eq("vi", "95.3"), "95.3"))

    b.append(p(
        "trong đó <i>R</i><sub>nr</sub> là tốc độ tái hợp không bức xạ. Tuy nhiên, các mật độ hạt "
        "tải dư được bơm vào trở về giá trị của chúng theo hàm mũ như"))

    b.append(eq(_eq("vi", "95.4"), "95.4"))

    b.append(p(
        "trong đó τ là thời gian sống của hạt tải và Δ<i>n</i><sub>0</sub> là mật độ điện tử dư ở "
        "trạng thái cân bằng. Vì Δ<i>n</i>/<i>R</i><sub>r</sub> và Δ<i>n</i>/<i>R</i><sub>nr</sub> "
        "tương ứng với thời gian sống tái hợp bức xạ τ<sub>r</sub> và thời gian sống tái hợp không "
        "bức xạ τ<sub>nr</sub>, ta có thể thu được thời gian sống tái hợp khối hiệu dụng của hạt "
        "tải thiểu số τ như"))

    b.append(eq(_eq("vi", "95.5"), "95.5"))

    b.append(p(
        "sao cho η = τ/τ<sub>r</sub>. Lý do khiến thời gian tái hợp nhanh là then chốt nằm ở chỗ: "
        "hạt tải càng lưu lại lâu ở trạng thái kích thích thì xác suất nó nhả năng lượng theo cách "
        "không bức xạ càng lớn. Để hiệu suất lượng tử nội cao, thời gian sống bức xạ τ<sub>r</sub> "
        "cần nhỏ. Với chất bán dẫn vùng cấm gián tiếp, τ<sub>r</sub> ≫ τ<sub>nr</sub> nên rất ít "
        "ánh sáng được tạo ra; còn với chất bán dẫn vùng cấm trực tiếp, τ<sub>r</sub> tăng theo "
        "nhiệt độ, do đó hiệu suất lượng tử nội giảm đi khi nhiệt độ tăng."))

    b.append(h2("Đặc trưng đáp ứng và băng thông điều chế",
                "Response characteristics and modulation bandwidth"))

    b.append(p(
        "Vì LED được dùng làm thiết bị hiển thị, đặc trưng đáp ứng tần số không quan trọng lắm. Tuy "
        "nhiên, LED cũng được dùng cho mục đích thông tin quang, và với những ứng dụng đó cần khảo "
        "sát đặc trưng đáp ứng thời gian của chúng. Ví dụ, một LED có thể được dùng cùng với một "
        "photodiode để truyền thông tin quang giữa hai điểm. Đầu ra ánh sáng của LED có thể được "
        "điều chế để mang thông tin quang bằng cách thay đổi dòng điốt. Thông thường, việc truyền "
        "tín hiệu quang được thuận lợi hoá bằng cách đưa một sợi quang vào giữa LED và photodiode."))
    b.append(p(
        "Có hai loại điện dung trong điốt có thể ảnh hưởng tới hành vi của hạt tải thiểu số. Một là "
        "điện dung chuyển tiếp, gây ra bởi sự thay đổi điện tích đa số trong vùng nghèo. Trong khi "
        "nó tỉ lệ nghịch với căn bậc hai của điện áp phân cực trong trường hợp chuyển tiếp đột ngột, "
        "nó lại tỉ lệ nghịch với căn bậc ba của điện áp phân cực trong trường hợp chuyển tiếp biến "
        "đổi tuyến tính. Loại điện dung thứ hai, gọi là điện dung khuếch tán, gây ra bởi các hạt "
        "tải thiểu số."))
    b.append(p(
        "Xét một LED được phân cực thuận bằng một điện áp một chiều. Xét thêm rằng phân cực này bị "
        "nhiễu loạn bởi một tín hiệu hình sin nhỏ. Khi phân cực bị rút bớt hoặc giảm đi, điện tích "
        "bắt đầu khuếch tán ra khỏi chuyển tiếp do tái hợp cho tới khi đạt được điều kiện cân bằng. "
        "Do đó, như một đáp ứng với tín hiệu điện áp, sự phân bố hạt tải thiểu số đóng góp vào một "
        "dòng tín hiệu."))
    b.append(p(
        "Xét một vật liệu bán dẫn loại <i>p</i> một chiều có tiết diện <i>A</i>, mà mật độ hạt tải "
        "thiểu số dư của nó được cho bởi"))

    b.append(eq(_eq("vi", "95.6"), "95.6"))

    b.append(p(
        "Như một hệ quả trực tiếp của tín hiệu hình sin đặt vào, phân bố điện tử dư dao động quanh "
        "giá trị một chiều của nó. Thực tế, ta có thể giả thiết mật độ hạt tải thiểu số dư có một "
        "thành phần biến thiên theo thời gian như"))

    b.append(eq(_eq("vi", "95.7"), "95.7"))

    b.append(p(
        "trong đó ⟨Δ<i>n</i><sub>p</sub>(<i>x</i>)⟩ là một đại lượng không đổi theo thời gian. Thay "
        "phương trình 95.7 vào phương trình 95.6, ta được hai phương trình vi phân riêng biệt:"))

    b.append(eq(_eq("vi", "95.8a"), "95.8a"))
    b.append(p("và"))
    b.append(eq(_eq("vi", "95.8b"), "95.8b"))
    b.append(p("trong đó"))
    b.append(eq(_eq("vi", "95.9a"), "95.9a"))
    b.append(p("và"))
    b.append(eq(_eq("vi", "95.9b"), "95.9b"))

    b.append(p(
        "Nghiệm một chiều của phương trình 95.8a đã được biết. Một lần nữa, dạng của phương trình "
        "95.8b lại tương tự như của phương trình 95.8a, và do đó nghiệm của nó được cho bởi"))

    b.append(eq(_eq("vi", "95.10"), "95.10"))

    b.append(p(
        "Vì dòng phụ thuộc tần số <i>I</i>(ω) đơn giản là tích của <i>eAD</i><sub>n</sub> và gradient "
        "nồng độ, ta thấy"))

    b.append(eq(_eq("vi", "95.11"), "95.11"))

    b.append(p(
        "trong đó <i>I</i>(0) là cường độ phát xạ ở tần số điều chế bằng không. Tiếp theo ta có thể "
        "xác định dẫn nạp bằng cách chia dòng cho điện áp nhiễu loạn. Phần thực của dẫn nạp, trong "
        "trường hợp này, sẽ tương đương với độ dẫn của điốt, còn phần ảo của nó sẽ tương ứng với "
        "điện dung khuếch tán."))
    b.append(p(
        "Đáp ứng điều chế cho bởi phương trình 95.11, tuy nhiên, bị giới hạn bởi thời gian tái hợp "
        "của hạt tải. LED thường được đặc trưng bởi băng thông điều chế của nó, định nghĩa là băng "
        "tần mà trên đó công suất tín hiệu (tỉ lệ với <i>I</i><sup>2</sup>(ω)) bằng một nửa giá trị "
        "của nó tại ω = 0. Dùng phương trình 95.11, băng thông điều chế 3 dB được cho bởi"))

    b.append(eq(_eq("vi", "95.12"), "95.12"))

    b.append(p(
        "trong đó thời gian sống khối đã được xấp xỉ bằng thời gian sống bức xạ. Đôi khi băng thông "
        "3 dB của LED được cho bởi <i>I</i>(ω) = <i>I</i>(0)/√2, nhưng sự đơn giản hoá này góp phần "
        "làm băng thông tăng sai đi một hệ số 1,732."))

    b.append(h2("Thời gian sống tái hợp bức xạ", "Radiative recombination lifetime"))

    b.append(p(
        "Dưới điều kiện cân bằng nhiệt, tốc độ tái hợp tỉ lệ với tích của các nồng độ hạt tải ban "
        "đầu, <i>n</i><sub>0</sub> và <i>p</i><sub>0</sub>. Khi đó, dưới điều kiện không cân bằng, "
        "các hạt tải bổ sung Δ<i>n</i> = Δ<i>p</i> được bơm vào vật liệu. Do đó, tốc độ tái hợp của "
        "các mật độ hạt tải dư được bơm vào được cho bởi các nồng độ hạt tải ban đầu và các mật độ "
        "hạt tải được bơm vào như"))

    b.append(eq(_eq("vi", "95.13"), "95.13"))

    b.append(p(
        "trong đó <i>B</i><sub>r</sub> là cùng hằng số đã đưa ra trong phương trình 95.1. Ví dụ với "
        "GaAs loại <i>p</i>, <i>B</i><sub>r</sub> = 1,7 × 10<sup>−10</sup> cm<sup>3</sup>/s khi "
        "<i>p</i><sub>0</sub> = 2,4 × 10<sup>18</sup> lỗ trống/cm<sup>3</sup>. Phương trình 95.13 "
        "được dùng để định nghĩa thời gian sống tái hợp bức xạ của hạt tải bằng"))

    b.append(eq(_eq("vi", "95.14"), "95.14"))

    b.append(p(
        "Trong điều kiện dừng, mật độ hạt tải dư có thể được tính theo độ rộng <i>d</i> của vùng "
        "hoạt động bằng"))

    b.append(eq(_eq("vi", "95.15"), "95.15"))

    b.append(p("trong đó <i>J</i> là mật độ dòng bơm."))
    b.append(p(
        "Thời gian sống tái hợp bức xạ được tìm bằng cách giải phương trình 95.14 sau khi đã khử "
        "Δ<i>n</i> khỏi nó nhờ phương trình 95.15:"))

    b.append(eq(_eq("vi", "95.16"), "95.16"))

    b.append(p(
        "Do đó, với bơm hạt tải thấp (tức <i>n</i><sub>0</sub> + <i>p</i><sub>0</sub> ≫ Δ<i>n</i>), "
        "phương trình 95.16 rút gọn thành"))

    b.append(eq(_eq("vi", "95.17a"), "95.17a"))

    b.append(p(
        "với bơm hạt tải cao (tức <i>n</i><sub>0</sub> + <i>p</i><sub>0</sub> ≪ Δ<i>n</i>), nó rút "
        "gọn thành"))

    b.append(eq(_eq("vi", "95.17b"), "95.17b"))

    b.append(p(
        "Phương trình 95.17a cho thấy trong chất bán dẫn pha tạp mạnh, τ<sub>r</sub> nhỏ. Nhưng quá "
        "trình pha tạp có vấn đề riêng của nó, vì trong nhiều hợp chất LED hai nguyên, pha tạp mạnh "
        "hơn có thể đưa vào các bẫy không bức xạ ngay bên dưới vùng dẫn, do đó vô hiệu hoá phương "
        "trình 95.12. So với phương trình 95.17a, phương trình 95.17b đưa ra một lựa chọn thay thế "
        "tốt hơn, theo đó τ<sub>r</sub> có thể được giảm bằng cách giảm độ rộng vùng hoạt động hoặc "
        "bằng cách tăng mật độ dòng. Với trường hợp GaAs loại <i>p</i>, thời gian sống bức xạ biến "
        "thiên trong khoảng 2,6 đến 0,35 ns, tương ứng, khi <i>p</i><sub>0</sub> biến thiên trong "
        "khoảng 1,0 × 10<sup>18</sup> lỗ trống/cm<sup>3</sup> đến 1,5 × 10<sup>19</sup> lỗ "
        "trống/cm<sup>3</sup>."))
    b.append(p(
        "Thông thường, LED hoạt động ở dòng thấp (≈10 mA) và điện áp thấp (≈1,5 V), và chúng có thể "
        "được bật và tắt trong khoảng 10 ns. Ngoài ra, vì kích thước nhỏ, chúng có thể được coi một "
        "cách hợp lý như những nguồn điểm. Do đó không có gì đáng ngạc nhiên khi chúng được ưa "
        "chuộng hơn các nguồn sáng khác cho các ứng dụng trong đường truyền dữ liệu sợi quang."))

    b.append(h2("Kết cấu phát xạ mặt và phát xạ cạnh",
                "Surface emitters and edge emitters"))

    b.append(p(
        "Hai kết cấu LED đặc biệt phổ biến là bộ phát xạ mặt và bộ phát xạ cạnh. Chúng được trình "
        "bày trên Hình 95.5. Ở kết cấu thứ nhất, hướng phát xạ chính vuông góc với mặt phẳng của "
        "vùng hoạt động; ở kết cấu thứ hai, hướng phát xạ chính nằm trong mặt phẳng của vùng hoạt "
        "động. Đồ thị phát xạ của bộ phát xạ mặt rất đẳng hướng, còn đồ thị phát xạ của bộ phát xạ "
        "cạnh thì rất định hướng."))

    b.append(fig(5, F.fig(5)))

    b.append(p(
        "Khi ánh sáng của LED đi từ một môi trường có chiết suất <i>n</i><sub>1</sub> sang một môi "
        "trường khác có chiết suất <i>n</i><sub>2</sub> (<i>n</i><sub>2</sub> &lt; "
        "<i>n</i><sub>1</sub>), chỉ một phần ánh sáng tới được truyền qua. Cụ thể, phần ánh sáng "
        "phát xạ chỉ tương ứng với phần xuất phát từ bên trong một nón có nửa góc đỉnh "
        "θ<sub>c</sub>, sao cho"))

    b.append(eq(_eq("vi", "95.18"), "95.18"))

    b.append(p(
        "Trong trường hợp LED, <i>n</i><sub>1</sub> tương ứng với chiết suất của môi trường LED và "
        "<i>n</i><sub>2</sub> tương ứng với chiết suất của không khí (hoặc chân không). Ánh sáng "
        "xuất phát từ <i>bên ngoài</i> góc θ<sub>c</sub> bị phản xạ toàn phần. Tuy nhiên, ánh sáng "
        "hướng từ <i>bên trong</i> nón có nửa góc đỉnh θ<sub>c</sub> sẽ chịu tổn hao Fresnel. Do đó, "
        "độ truyền qua tổng cộng <i>T</i> được cho bởi"))

    b.append(eq(_eq("vi", "95.19"), "95.19"))

    b.append(p("Theo đó, hiệu suất chuyển đổi điện–quang tổng cộng trong LED được cho bởi"))

    b.append(_eq20("vi"))

    b.append(p(
        "Chỉ có hai sơ đồ làm tăng hiệu suất chuyển đổi điện–quang trong LED. Kỹ thuật thứ nhất bao "
        "gồm việc bảo đảm rằng phần lớn các tia tới đập vào mặt phân cách bán dẫn–không khí ở góc "
        "nhỏ hơn θ<sub>c</sub>. Điều này đạt được bằng cách làm mặt phân cách bán dẫn–không khí có "
        "dạng bán cầu. Phương pháp thứ hai bao gồm những sơ đồ trong đó LED được bọc trong một môi "
        "trường gần như trong suốt có chiết suất cao. Cách thứ hai thường ít tốn kém hơn. Nếu dùng "
        "thuỷ tinh có chiết suất 1,5 để bọc, hiệu suất của LED có thể tăng lên một hệ số 3. Hai "
        "trong số các cách bố trí vỏ bọc khả dĩ và các đồ thị phát xạ tương ứng được minh hoạ trên "
        "Hình 95.6."))

    b.append(fig(6, F.fig(6)))

    b.append(h2("Bộ ghép quang", "Optocouplers"))

    b.append(p(
        "LED thường được dùng cùng với một phototransistor để làm việc như một bộ ghép quang. Các bộ "
        "ghép quang được dùng trong những trường hợp cần truyền tín hiệu giữa các mạch cách ly về "
        "điện. Chúng được dùng để đạt được cách ly nhiễu bằng cách loại bỏ nhu cầu có một điểm đất "
        "chung giữa hai hệ thống. Tuỳ theo loại vật liệu ghép, các linh kiện thu nhỏ này có thể vừa "
        "cách ly nhiễu vừa cách ly điện áp cao. Hình 95.7 trình bày một trường hợp điển hình trong "
        "đó hai bộ ghép quang được dùng để tạo nên một mạch cắt tín hiệu. Hai bộ ghép quang cắt "
        "phần dương hoặc phần âm của tín hiệu vào với tần số bằng một nửa tần số của tín hiệu điều "
        "khiển được đưa vào trigơ <i>T</i>. Bộ khuếch đại thuật toán cung cấp một phiên bản đã được "
        "khuếch đại của dạng sóng đã cắt. So sánh với một mạch cắt dùng transistor lưỡng cực đơn "
        "giản, mạch cắt dùng bộ ghép quang tạo ra các xung nhiễu ở đầu ra do điện dung ghép nội tại "
        "của nó."))

    b.append(fig(7, F.fig(7)))

    b.append(h2("Hiển thị LED", "LED displays"))

    b.append(p(
        "Các LED khả kiến được biết đến nhiều nhất với công dụng trong màn hiển thị và đèn chỉ báo. "
        "Trong những ứng dụng cần nhiều hơn một nguồn sáng, có thể dùng một dãy LED. Dãy LED là một "
        "linh kiện gồm một hàng các LED rời được nối với nhau, có hoặc không có một hốc phản xạ "
        "chung. Hình 95.8a trình bày các cách bố trí LED khác nhau để hiển thị ký tự số thập lục "
        "phân và chữ-số, còn Hình 95.8b trình bày, ví dụ, các ký tự chữ-số khả dĩ dùng màn 16 đoạn. "
        "Trong các hệ thống số, mã nhị phân tương đương với các ký tự này thường được giải mã, và do "
        "đó, một tổ hợp cụ thể các đoạn LED được bật lên để hiển thị ký tự chữ-số mong muốn."))

    b.append(fig(8, F.fig(8)))

    b.append(p(
        "Màn hiển thị ma trận điểm cung cấp phông hiển thị dễ đọc nhất. Nó cho độ linh hoạt lớn hơn "
        "trong việc tạo hình ký tự và có xác suất bị hiểu sai thấp hơn trong trường hợp một phần tử "
        "hiển thị bị hỏng. Tuy nhiên, các màn hiển thị này cần một số lượng lớn dây dẫn và làm tăng "
        "độ phức tạp của mạch. Nói chung, màn hiển thị LED có góc nhìn tuyệt vời, tốc độ đáp ứng cao "
        "(≈10 ns), tuổi thọ dài, và khả năng giao tiếp ưu việt với các mạch điện tử, gần như không "
        "bị giới hạn chu trình làm việc. LED phát xạ xanh dương không có sẵn trên thị trường. Khi so "
        "sánh với màn hiển thị thụ động, màn hiển thị LED tiêu thụ nhiều công suất hơn và cần một "
        "hệ thống dây dẫn phức tạp với ít nhất một dây cho mỗi phần tử hiển thị."))

    b.append(h2("Tài liệu tham khảo", "References"))
    b.append(refs(_REFS))

    b.append(note(
        "<b>Ghi chú của người dịch.</b> "
        "(1) Bảng 95.1 xếp SnO<sub>2</sub> vào nhóm II–VI, nhưng thiếc thuộc nhóm IV nên "
        "SnO<sub>2</sub> không phải là hợp chất II–VI theo nghĩa chặt; bảng được giữ nguyên như bản "
        "gốc. Thứ tự các dòng trong bảng cũng không tăng dần theo <i>E</i><sub>g</sub> (CuBr 2,9 eV "
        "đứng sau BeTe 2,8 eV) — cũng giữ nguyên như bản gốc. "
        "(2) Bản gốc in “<i>x</i> = 0.05” trong câu so sánh độ dịch bước sóng đỉnh; xét theo ngữ "
        "cảnh (điểm chuyển từ vùng cấm trực tiếp sang gián tiếp nằm ở <i>x</i> ≈ 0,45) thì giá trị "
        "đúng phải là <i>x</i> = 0,5. Bản dịch dùng 0,5 và ghi lại điểm này. "
        "(3) Phương trình 95.17a được in với số mũ 1/2, nhưng theo phương trình 95.14 thì khi "
        "Δ<i>n</i> → 0 phải thu được τ<sub>r</sub> = [<i>B</i><sub>r</sub>(<i>n</i><sub>0</sub> + "
        "<i>p</i><sub>0</sub>)]<sup>−1</sup>; số mũ 1/2 không đúng về thứ nguyên. Bản dịch giữ "
        "nguyên như bản in và ghi chú tại đây. "
        "(4) Bản gốc dùng ký hiệu δ<sup>2</sup>/δ<i>x</i><sup>2</sup> trong các phương trình 95.8a "
        "và 95.8b; bản dịch chuẩn hoá thành ∂<sup>2</sup>/∂<i>x</i><sup>2</sup> cho thống nhất với "
        "phương trình 95.6. "
        "(5) Ký hiệu <i>R</i><sub>nr</sub> trong phương trình 95.13 và 95.14 thực chất là tốc độ tái "
        "hợp thực của hạt tải dư, không phải tốc độ tái hợp không bức xạ, dù chỉ số “nr” thường mang "
        "nghĩa sau; ký hiệu được giữ nguyên như bản gốc."))

    return "".join(b)


# ================================================================ ENGLISH
def body_en():
    b = []

    b.append(p(
        "A light-emitting diode (LED) is a particular solid-state <i>p–n</i> junction diode that gives "
        "out light upon the application of a bias voltage. The luminescence process in this case is "
        "electroluminescence, which is associated with emission wavelengths in the visible and "
        "infrared regions of the spectrum. When a forward bias is applied to the <i>p–n</i> junction "
        "diode, carriers are injected into the depletion region in large numbers. Because of their "
        "physical proximity, the electron–hole pairs undergo a recombination that is associated with "
        "the emission of energy. Depending on the semiconductor band-gap characteristics, this "
        "emitted energy can be in the form of heat (as phonons) or light (as photons)."))
    b.append(p(
        "The solution of the Schrödinger equation for a typical crystal reveals the existence of "
        "Brillouin zones. A plot between the energy <i>E</i> of an electron in a solid and its wave "
        "vector <i>k</i> represents the allowed energy bands. It may be noted that the lattice "
        "structure affects the motion of an electron when <i>k</i> is close to <i>n</i>π/<i>l</i> "
        "(where <i>n</i> is any integer and <i>l</i> is the crystal periodicity) and the effect of "
        "this constraint is to introduce an energy band gap between the allowed energy bands. Figure "
        "95.1a shows portions of two <i>E</i> vs. <i>k</i> curves for neighboring energy bands within "
        "the regions <i>k</i> = π/<i>l</i> and <i>k</i> = −π/<i>l</i> (also known as the reduced "
        "zone)."))

    b.append(fig(1, F.fig(1), "en"))

    b.append(p(
        "While the upper band of Fig. 95.1a represents the energy of conduction band electrons, the "
        "curvature of the lower band can be associated with electrons having negative effective mass. "
        "The concept of negative effective mass can readily be identified with the concept of holes "
        "in the valence band. While the majority of the electrons are identified with the minima of "
        "the upper <i>E–k</i> curve, the majority of the holes are identified with the maxima of the "
        "lower <i>E–k</i> curve. The minimum value of the conduction band and the maximum value of "
        "the valence band in Fig. 95.1a both have identical <i>k</i> values. A semiconductor having "
        "such a characteristic is said to have a direct band gap, and the associated recombination in "
        "such a semiconductor is referred to as direct."))
    b.append(p(
        "The <i>direct recombination</i> of an electron–hole pair always results in the emission of a "
        "photon. In a direct band-gap semiconductor, the emitted photon is not associated with any "
        "change in momentum (given by <i>hk</i>/2π) since Δ<i>k</i> = 0. However, for some "
        "semiconducting materials, the <i>E</i> vs. <i>k</i> curve may be somewhat different, as "
        "shown in Fig. 95.1b, while the minimum conduction band energy can have a nonzero <i>k</i>, "
        "the maximum valence band energy can have <i>k</i> = 0. The electron–hole recombination in "
        "such a semiconductor is referred to as indirect."))
    b.append(p(
        "An <i>indirect recombination</i> involves a momentum adjustment. Most of the emission energy "
        "is thus expended in the form of heat (as phonons). Very little energy is left for the purpose "
        "of photon emission, which in most cases is a very slow process. Furthermore, since both "
        "photons and phonons are involved in this energy exchange, such transitions are less likely "
        "to occur. The interband recombination rate is basically given by"))

    b.append(eq(_eq("en", "95.1"), "95.1"))

    b.append(p(
        "where <i>B</i><sub>r</sub> is a recombination-dependent constant which for a direct band-gap "
        "semiconductor is ~10<sup>6</sup> times larger than that for an indirect band-gap "
        "semiconductor. For direct recombination, <i>B</i><sub>r</sub> value ranges from 0.46 × "
        "10<sup>−10</sup> to 7.2 × 10<sup>−10</sup> cm<sup>3</sup>/s."))
    b.append(p(
        "All semiconductor crystal lattices are alike, being dissimilar only in terms of their band "
        "characteristics. Si and Ge both have indirect band transitions, whereas GaAs, for example, "
        "is a semiconductor that has a direct band transition. Thus, while Si and Ge are preferred "
        "for fabrication of transistors and integrated circuits, GaAs is preferred for the "
        "fabrication of LEDs."))
    b.append(p(
        "The direct recombination (when <i>k</i> = constant) results in a photon emission whose "
        "wavelength (in micrometers) is given by"))

    b.append(eq(_eq("en", "95.2"), "95.2"))

    b.append(p(
        "where <i>E</i><sub>g</sub> is the band-gap energy. The LEDs under proper forward-biased "
        "conditions can operate in the ultraviolet, visible, and infrared regions. For the visible "
        "region, however, the spectral luminous efficiency curves of Fig. 95.2, which account for the "
        "fact that the visual response to any emission is a function of wavelength, should be of "
        "concern. It is unfortunate that there is not a single-element semiconductor suitable for "
        "fabrication of LEDs, but there are many binary and ternary compounds that can be used for "
        "fabrication of LEDs. Table 95.1 lists some of these binary semiconductor materials. The "
        "ternary semiconductors include GaAlAs, CdGeP<sub>2</sub>, and ZnGeP<sub>2</sub> for infrared "
        "region operation, CuGaS<sub>2</sub> and AgInS<sub>2</sub> for visible region operation, and "
        "CuAlS<sub>2</sub> for ultraviolet region operation. Ternary semiconductors are used because "
        "their energy gaps can be tuned to a desired emission wavelength by picking appropriate "
        "composition."))

    b.append(fig(2, F.fig(2), "en"))
    b.append(table(*_table1("en")))

    b.append(p(
        "Of the ternary compounds, gallium arsenide–phosphide (written as "
        "GaAs<sub>1−<i>x</i></sub>P<sub><i>x</i></sub>) is an example that is basically a combination "
        "of two binary semiconductors, namely, GaAs and GaP. The corresponding band-gap energy of the "
        "semiconductor can be varied by changing the value of <i>x</i>. For example, when <i>x</i> = "
        "0, <i>E</i><sub>g</sub> = 1.43 eV. <i>E</i><sub>g</sub> increases with increasing <i>x</i> "
        "until <i>x</i> = 0.44 and <i>E</i><sub>g</sub> = 1.977 eV, as shown in Fig. 95.3. However, "
        "for <i>x</i> ≥ 0.45, the band gap is indirect. The most common composition of "
        "GaAs<sub>1−<i>x</i></sub>P<sub><i>x</i></sub> used in LEDs has <i>x</i> = 0.4 and "
        "<i>E</i><sub>g</sub> ≈ 1.3 eV. This band-gap energy corresponds to an emission of red light. "
        "Calculators and watches often use this particular composition of "
        "GaAs<sub>1−<i>x</i></sub>P<sub><i>x</i></sub>."))

    b.append(fig(3, F.fig(3), "en"))

    b.append(p(
        "Interestingly, the indirect band gap of GaAs<sub>1−<i>x</i></sub>P<sub><i>x</i></sub> (with "
        "1 ≥ <i>x</i> ≥ 0.45) can be used to output light ranging from yellow through green provided "
        "the semiconductor is doped with impurities such as nitrogen. The dopants introduced in the "
        "semiconductor replace phosphorus atoms which, in turn, introduce electron trap levels very "
        "near the conduction band. For example, <i>x</i> = 0.5, the doping of nitrogen increases the "
        "LED efficiency form 0.01 to 1%, as shown in Fig. 95.4. It must be noted, however, that "
        "nitrogen doping shifts the peak emission wavelength toward the red. The shift is "
        "comparatively larger at and around <i>x</i> = 0.5 than <i>x</i> = 1.0. The energy emission "
        "in nitrogen-doped GaAs<sub>1−<i>x</i></sub>P<sub><i>x</i></sub> devices is a function of both "
        "<i>x</i> and the nitrogen concentration."))

    b.append(fig(4, F.fig(4), "en"))

    b.append(p(
        "Nitrogen is a different type of impurity from those commonly encountered in extrinsic "
        "semiconductors. Nitrogen, like arsenic and phosphorus, has five valence electrons, but it "
        "introduces no net charge carriers in the lattice. It provides active radiative recombination "
        "centers in the indirect band-gap materials. For an electron, a recombination center is an "
        "empty state in the band gap into which an electron falls and, then, thereafter, falls into "
        "the valence band by recombining with a hole. For example, while a GaP LED emits green light "
        "(2.23 eV), a nitrogen-doped GaP LED emits yellowish green light (2.19 eV), and a heavily "
        "nitrogen-doped GaP LED emits yellow light (2.1 eV)."))

    b.append(h2("Internal quantum efficiency"))

    b.append(p(
        "The injected excess carriers in a semiconductor may recombine either radiatively or "
        "nonradiatively. Whereas nonradiative recombination generates phonons, radiative "
        "recombination produces photons. Consequently, the internal quantum efficiency η, defined as "
        "the ratio of the radiative recombination rate <i>R</i><sub>r</sub> to the total "
        "recombination rate, is given by"))

    b.append(eq(_eq("en", "95.3"), "95.3"))

    b.append(p(
        "where <i>R</i><sub>nr</sub> is the nonradiative recombination rate. However, the injected "
        "excess carrier densities return to their value exponentially as"))

    b.append(eq(_eq("en", "95.4"), "95.4"))

    b.append(p(
        "where τ is the carrier lifetime and Δ<i>n</i><sub>0</sub> is the excess electron density at "
        "equilibrium. Since Δ<i>n</i>/<i>R</i><sub>r</sub> and Δ<i>n</i>/<i>R</i><sub>nr</sub> are, "
        "respectively, equivalent to the radiative recombination lifetime τ<sub>r</sub> and the "
        "nonradiative recombination lifetime τ<sub>nr</sub>, we can obtain the effective minority "
        "carrier bulk recombination time τ as"))

    b.append(eq(_eq("en", "95.5"), "95.5"))

    b.append(p(
        "such that η = τ/τ<sub>r</sub>. The reason that a fast recombination time is crucial is that "
        "the longer the carrier remains in an excited state, the larger the probability that it will "
        "give out energy nonradiatively. In order for the internal quantum efficiency to be high, the "
        "radiative lifetime τ<sub>r</sub> needs to be small. For indirect band-gap semiconductors, "
        "τ<sub>r</sub> ≫ τ<sub>nr</sub> so that very little light is generated, and for direct "
        "band-gap semiconductors, τ<sub>r</sub> increases with temperature so that the internal "
        "quantum efficiency deteriorates with the temperature."))

    b.append(h2("Response characteristics and modulation bandwidth"))

    b.append(p(
        "As long as the LEDs are used as display devices, it is not too important to have fast "
        "response characteristics. However, LEDs are also used for the purpose of optical "
        "communications, and for those applications it is appropriate to study their time response "
        "characteristics. For example, an LED can be used in conjunction with a photodetector for "
        "transmitting optical information between two points. The LED light output can be modulated "
        "to convey optical information by varying the diode current. Most often, the transmission of "
        "optical signals is facilitated by introducing an optical fiber between the LED and the "
        "photodetector."))
    b.append(p(
        "There can be two different types of capacitances in diodes that can influence the behavior of "
        "the minority carriers. One of these is the <i>junction capacitance</i>, which is caused by "
        "the variation of majority charge in the depletion layer. While it is inversely proportional "
        "to the square root of bias voltage in the case of an abrupt junction, it is inversely "
        "proportional to the cube root of bias voltage in the case of a linearly graded junction. The "
        "second type of capacitance, known as the <i>diffusion capacitance</i>, is caused by the "
        "minority carriers."))
    b.append(p(
        "Consider an LED that is forward biased with a dc voltage. Consider further that the bias is "
        "perturbed by a small sinusoidal signal. When the bias is withdrawn or reduced, charge begins "
        "to diffuse from the junction as a result of recombination until an equilibrium condition is "
        "achieved. Consequently, as a response to the signal voltage, the minority carrier "
        "distribution contributes to a signal current."))
    b.append(p(
        "Consider a one-dimensional <i>p</i>-type semiconducting material of cross-sectional area "
        "<i>A</i> whose excess minority carrier density is given by"))

    b.append(eq(_eq("en", "95.6"), "95.6"))

    b.append(p(
        "As a direct consequence of the applied sinusoidal signal, the excess electron distribution "
        "fluctuates about its dc value. In fact, we may assume excess minority carrier density to "
        "have a time-varying component as described by"))

    b.append(eq(_eq("en", "95.7"), "95.7"))

    b.append(p(
        "where ⟨Δ<i>n</i><sub>p</sub>(<i>x</i>)⟩ is a time-invariant quantity. By introducing Eq. "
        "95.7 into Eq. 95.6, we get two separate differential equations:"))

    b.append(eq(_eq("en", "95.8a"), "95.8a"))
    b.append(p("and"))
    b.append(eq(_eq("en", "95.8b"), "95.8b"))
    b.append(p("where"))
    b.append(eq(_eq("en", "95.9a"), "95.9a"))
    b.append(p("and"))
    b.append(eq(_eq("en", "95.9b"), "95.9b"))

    b.append(p(
        "The dc solution of Eq. 95.8a is well known. Again, the form of Eq. 95.8b is similar to that "
        "of Eq. 95.8a and, therefore, its solution is given by"))

    b.append(eq(_eq("en", "95.10"), "95.10"))

    b.append(p(
        "Since the frequency-dependent current <i>I</i>(ω) is simply a product of "
        "<i>eAD</i><sub>n</sub> and the concentration gradient, we find that"))

    b.append(eq(_eq("en", "95.11"), "95.11"))

    b.append(p(
        "where <i>I</i>(0) is the intensity emitted at zero modulation frequency. We can determine the "
        "admittance next by dividing the current by the perturbing voltage. The real part of the "
        "admittance, in this case, will be equivalent to the diode conductance, whereas its imaginary "
        "part will correspond to the diffusion capacitance susceptance."))
    b.append(p(
        "The modulation response as given by Eq. 95.11 is, however, limited by the carrier "
        "recombination time. Often an LED is characterized by its modulation bandwidth, which is "
        "defined as the frequency band over which signal power (proportional to <i>I</i><sup>2</sup>"
        "(ω)) is half of that at ω = 0. Using Eq. 95.11, the 3-dB modulation bandwidth is given by"))

    b.append(eq(_eq("en", "95.12"), "95.12"))

    b.append(p(
        "where the bulk lifetime has been approximated by the radiative lifetime. Some times the 3-dB "
        "bandwidth of the LED is given by <i>I</i>(ω) = <i>I</i>(0)/√2, but this simplification "
        "contributes to an erroneous increase in the bandwidth by a factor of 1.732."))

    b.append(h2("Radiative recombination lifetime"))

    b.append(p(
        "Under conditions of thermal equilibrium, the recombination rate is proportional to the "
        "product of initial carrier concentrations, <i>n</i><sub>0</sub> and <i>p</i><sub>0</sub>. "
        "Then, under nonequilibrium conditions, additional carriers Δ<i>n</i> = Δ<i>p</i> are injected "
        "into the material. Consequently, the recombination rate of injected excess carrier densities "
        "is given by initial carrier concentrations and injected carrier densities as"))

    b.append(eq(_eq("en", "95.13"), "95.13"))

    b.append(p(
        "where <i>B</i><sub>r</sub> is the same constant introduced in Eq. 95.1. For <i>p</i>-type "
        "GaAs, for example, <i>B</i><sub>r</sub> = 1.7 × 10<sup>−10</sup> cm<sup>3</sup>/s when "
        "<i>p</i><sub>0</sub> = 2.4 × 10<sup>18</sup> holes/cm<sup>3</sup>. Equation 95.13 is used to "
        "define the radiative carrier recombination lifetime by"))

    b.append(eq(_eq("en", "95.14"), "95.14"))

    b.append(p(
        "In the steady-state condition, the excess carrier density can be calculated in terms of the "
        "active region width <i>d</i> by"))

    b.append(eq(_eq("en", "95.15"), "95.15"))

    b.append(p("where <i>J</i> is the injection current density."))
    b.append(p(
        "The radiative recombination lifetime is found by solving Eq. 95.14 after having eliminated "
        "Δ<i>n</i> from it using Eq. 95.15:"))

    b.append(eq(_eq("en", "95.16"), "95.16"))

    b.append(p(
        "Thus, while for the low carrier injection (i.e., <i>n</i><sub>0</sub> + <i>p</i><sub>0</sub> "
        "≫ Δ<i>n</i>), Eq. 95.16 reduces to"))

    b.append(eq(_eq("en", "95.17a"), "95.17a"))

    b.append(p(
        "for the high carrier injection (i.e., <i>n</i><sub>0</sub> + <i>p</i><sub>0</sub> ≪ "
        "Δ<i>n</i>), it reduces to"))

    b.append(eq(_eq("en", "95.17b"), "95.17b"))

    b.append(p(
        "Equation 95.17a indicates that in highly doped semiconductors, τ<sub>r</sub> is small. But "
        "the doping process has its own problem, since in many of the binary LED compounds higher "
        "doping may introduce nonradiative traps just below the conduction band, thus nullifying Eq. "
        "95.12. In comparison to Eq. 95.17a, Eq. 95.17b provides a better alternative whereby "
        "τ<sub>r</sub> can be reduced by decreasing the active region width or by increasing the "
        "current density. For the case of <i>p</i>-type GaAs, the radiative lifetimes vary between "
        "2.6 and 0.35 ns, respectively, when <i>p</i><sub>0</sub> varies between 1.0 × "
        "10<sup>18</sup> holes/cm<sup>3</sup> and 1.5 × 10<sup>19</sup> holes/cm<sup>3</sup>."))
    b.append(p(
        "Usually, LEDs are operated at low current (≈10 mA) and low voltages (≈1.5 V), and they can be "
        "switched on and off in the order of 10 ns. In addition, because of their small sizes, they "
        "can be reasonably treated as point sources. It is, therefore, not surprising that they are "
        "highly preferred over other light sources for applications in fiber-optic data links."))

    b.append(h2("Surface emitters and edge emitters"))

    b.append(p(
        "Two particular LED designs are popular: <i>surface emitters</i> and <i>edge emitters</i>. "
        "They are shown in Fig. 95.5. In the former, the direction of major emission is normal to the "
        "plane of the active region, whereas in the latter the direction of major emission is in the "
        "plane of the active region. The emission pattern of the surface emitters is very much "
        "isotropic, whereas that of the edge emitters is highly directional."))

    b.append(fig(5, F.fig(5), "en"))

    b.append(p(
        "As the LED light originating from a medium of refractive index <i>n</i><sub>1</sub> goes to "
        "another medium of refractive index <i>n</i><sub>2</sub> (<i>n</i><sub>2</sub> &lt; "
        "<i>n</i><sub>1</sub>), only a portion of incident light is transmitted. In particular, the "
        "portion of the emitted light corresponds to only that which originates from within a cone of "
        "semiapex angle θ<sub>c</sub>, such that"))

    b.append(eq(_eq("en", "95.18"), "95.18"))

    b.append(p(
        "In the case of an LED, <i>n</i><sub>1</sub> corresponds to the refractive index of the LED "
        "medium and <i>n</i><sub>2</sub> corresponds to that of air (or vacuum). Light originating "
        "from <i>beyond</i> angle θ<sub>c</sub> undergoes a total internal reflection. However, the "
        "light directed from <i>within</i> the cone of the semiapex angle θ<sub>c</sub> will be "
        "subjected to Fresnels loss. Thus, the overall transmittance <i>T</i> is given by"))

    b.append(eq(_eq("en", "95.19"), "95.19"))

    b.append(p(
        "Accordingly, the total electrical-to-optical conversion efficiency in LEDs is given by"))

    b.append(_eq20("en"))

    b.append(p(
        "Only two schemes increase the electrical-to-optical conversion efficiency in an LED. The "
        "first technique involves guaranteeing that most of the incident rays strike the "
        "glass-to-air interface at angles less than θ<sub>c</sub>. It is accomplished by making the "
        "semiconductor–air interface hemispherical. The second method involves schemes whereby the "
        "LED is encapsulated in an almost transparent medium of high refractive index. The latter "
        "means is comparatively less expensive. If a glass of refractive index 1.5 is used for "
        "encapsulation, the LED efficiency can be increased by a factor of 3. Two of the possible "
        "encapsulation arrangements and the corresponding radiation patterns are illustrated in Fig. "
        "95.6."))

    b.append(fig(6, F.fig(6), "en"))

    b.append(h2("Optocouplers"))

    b.append(p(
        "LEDs are often used in conjunction with a phototransistor to function as an optocoupler. The "
        "optocouplers are used in circumstances when it is desirable to have a transmission of "
        "signals between electrically isolated circuits. They are used to achieve noise separation by "
        "eliminating the necessity of having a common ground between the two systems. Depending on "
        "the type of coupling material, these miniature devices can provide both noise isolation as "
        "well as high voltage isolation. Figure 95.7 shows a typical case where two optocouplers are "
        "used to attain a chopper circuit. The two optocouplers chop either the positive or the "
        "negative portion of the input signals with a frequency of one half of that of the control "
        "signal that is introduced at the <i>T</i> flip-flop. The operational amplifier provides an "
        "amplified version of the chopped output waveform. In comparison, a chopper circuit that uses "
        "simple bipolar transistors produces noise spikes in the output because of its inherent "
        "capacitive coupling."))

    b.append(fig(7, F.fig(7), "en"))

    b.append(h2("LED displays"))

    b.append(p(
        "The visible LEDs are best known for their uses in displays and indicator lamps. In "
        "applications where more than a single source of light is required, an LED array can be "
        "utilized. An LED array is a device consisting of a row of discrete LEDs connected together "
        "within or without a common reflector cavity. Figure 95.8a shows different LED arrangements "
        "for displaying hexadecimal numeric and alphanumeric characters, whereas Fig. 95.8b shows, "
        "for example, the possible alphanumeric characters using 16-segment displays. In digital "
        "systems, the binary codes equivalent to these characters are usually decoded and, "
        "consequently, a specific combination of LED segments are turned on to display the desired "
        "alphanumeric character."))

    b.append(fig(8, F.fig(8), "en"))

    b.append(p(
        "The dot matrix display provides the most desirable display font. It gives more flexibility "
        "in shaping characters and has a lower probability of being misinterpreted in case of a "
        "display failure. However, these displays involve a large number of wires and increased "
        "circuit complexity. LED displays, in general, have an excellent viewing angle, high "
        "resonance speed (≈10 ns), long life, and superior interface capability with electronics with "
        "almost no duty cycle limitation. LEDs with blue emission are not available commercially. "
        "When compared with passive displays, LED displays consume more power and involve complicated "
        "wiring with at least one wire per display element."))

    b.append(h2("References"))
    b.append(refs(_REFS))

    return "".join(b)


# ================================================================ BUILD
def build(lang):
    vi = lang == "vi"
    switch = ("%s%s/" % (BASE_EN, CSLUG)) if vi else ("%s%s/" % (BASE_VI, CSLUG))
    title = ("Chương 95 — %s · Sổ tay Đo lường, Thiết bị đo và Cảm biến" % TITLE_VI if vi
             else "Chapter 95 — %s · Measurement, Instrumentation and Sensors Handbook" % TITLE_EN)
    desc = ("Bản dịch tiếng Việt Chương 95 “Hiển thị LED” của Mohammad A. Karim — cơ chế "
            "điện phát quang, vùng cấm trực tiếp và gián tiếp, vật liệu bán dẫn, hiệu suất lượng tử "
            "nội, băng thông điều chế, bộ ghép quang và màn hiển thị LED, với 8 hình, 1 bảng và 20 "
            "phương trình." if vi
            else
            "Companion to Chapter 95 of the CRC Measurement Handbook — electroluminescence, direct "
            "and indirect band gaps, LED materials, internal quantum efficiency, modulation "
            "bandwidth, optocouplers and LED displays, with 8 figures, 1 table and 20 equations.")
    crumb = ('<a href="/vi/books/">Sách</a> · <a href="%s">Sổ tay Đo lường, Thiết bị đo và Cảm biến</a> · '
             'Chương 95' % BASE_VI if vi else
             '<a href="/books/">Books</a> · <a href="%s">Measurement, Instrumentation and Sensors '
             'Handbook</a> · Chapter 95' % BASE_EN)
    meta = ("Chương 95 · theo Ch95.pdf (CRC Press, 1999) · 8 hình, 1 bảng, 20 phương trình" if vi else
            "Chapter 95 · 8 figures, 1 table, 20 equations")
    body = ('<main><article class="intranet-content reader"><div class="reader-hero">'
            '<div class="breadcrumb">%s</div><h1>%s</h1><p class="byline">%s</p>'
            '<div class="meta-line">%s</div></div><div class="prose">%s</div>%s</article></main>'
            % (crumb, TITLE_VI if vi else TITLE_EN, BYLINE, meta,
               body_vi() if vi else body_en(), chapter_nav(lang, 95)))
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
