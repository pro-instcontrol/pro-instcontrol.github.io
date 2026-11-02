# -*- coding: utf-8 -*-
"""Handbook Chapter 90 — Human Factors in Displays.

Steven A. Murray (SPAWAR Systems Center) and Barrett S. Caldwell
(University of Wisconsin — Madison).

Writes the full Vietnamese translation and the English companion.
Figure: hb90fig.py (90.1). Equations 90.1–90.6 were all garbled in the text
extract and were re-read off the printed page — see the translator's note.
Run:  python build/reader_hb_ch90.py
"""
import os

import hb90fig as F90
from reader_handbook import SLUG, head, header, footer
from chapter_nav import nav as chapter_nav

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSLUG = "ch90-human-factors-in-displays"
TITLE_EN = "Human Factors in Displays"
TITLE_VI = "Yếu tố con người trong hiển thị"
BYLINE = "Steven A. Murray và Barrett S. Caldwell"
BYLINE_EN = "Steven A. Murray and Barrett S. Caldwell"
BASE_EN = "/books/read/%s/" % SLUG
BASE_VI = "/vi/books/read/%s/" % SLUG

FIGS = {1: F90.fig_90_1}


def fig(num, lang="vi"):
    svg, cap_vi, cap_en, _av, _ae = FIGS[num]()
    return ('<figure class="figure" id="fig-90-%d">%s<figcaption class="figcap">%s</figcaption>'
            '</figure>' % (num, svg, cap_vi if lang == "vi" else cap_en))


def p(t):
    return "<p>%s</p>" % t


def h2(t, en=""):
    return '<h2>%s%s</h2>' % (t, (' <span class="en">%s</span>' % en) if en else "")


def h3(t, en=""):
    return '<h3>%s%s</h3>' % (t, (' <span class="en">%s</span>' % en) if en else "")


def note(t):
    return '<div class="note">%s</div>' % t


def eq(body, num=""):
    if not num:
        return '<div class="eq">%s</div>' % body
    return '<div class="eq"><span class="n">(%s)</span>%s</div>' % (num, body)


def refs(items):
    return '<ol class="ref-list">%s</ol>' % "".join("<li>%s</li>" % i for i in items)


def ul(items):
    return "<ul>%s</ul>" % "".join("<li>%s</li>" % i for i in items)


def _frac(num, den, size="0.86em"):
    """A stacked fraction built from two inline-blocks.

    The book sets 90.1, 90.2, 90.3 and 90.5 as true two-line fractions, so a
    slash would misrepresent them. No `.frac` class exists in library.css and
    adding one would touch every reader page, so the styling stays inline.
    """
    return ('<span style="display:inline-block;vertical-align:middle;text-align:center;'
            'max-width:100%%;font-size:%s;line-height:1.25;margin:0 0.2em">'
            '<span style="display:block;border-bottom:1.2px solid currentColor;'
            'padding:0 0.4em 2px">%s</span>'
            '<span style="display:block;padding:2px 0.4em 0">%s</span></span>'
            % (size, num, den))


# ================================================================ EQUATIONS
# Re-read from the printed page: the text extract lost the pi-times sign in
# 90.1 ("R =p´"), the delta in 90.2 ("DI"), the fraction bars in 90.3 and
# 90.5, and both sub/superscripts in 90.4 ("EE = m cos4 q") and 90.6
# ("CFF a L b =+ log a").
_EQ_VI = {
    "90.1": "<i>R</i> = π × " + _frac("độ chói", "độ rọi"),
    "90.2": "<i>K</i> = " + _frac("Δ<i>I</i>", "<i>I</i>"),
    "90.3": "VA = " + _frac("3438<i>H</i>", "<i>D</i>"),
    "90.4": "<i>E</i> = <i>E</i><sub>m</sub> cos<sup>4</sup> θ",
    "90.5": ("<i>C</i><sub>R</sub> = "
             + _frac("độ chói của vật sáng hơn − độ chói của vật tối hơn",
                     "độ chói của vật sáng hơn", "0.82em")),
    "90.6": "CFF = <i>a</i> log <i>L</i><sub>a</sub> + <i>b</i>",
}

_EQ_EN = {
    "90.1": "<i>R</i> = π × " + _frac("luminance", "illuminance"),
    "90.2": "<i>K</i> = " + _frac("Δ<i>I</i>", "<i>I</i>"),
    "90.3": "VA = " + _frac("3438<i>H</i>", "<i>D</i>"),
    "90.4": "<i>E</i> = <i>E</i><sub>m</sub> cos<sup>4</sup> θ",
    "90.5": ("<i>C</i><sub>R</sub> = "
             + _frac("luminance of brighter object − luminance of darker object",
                     "luminance of brighter object", "0.82em")),
    "90.6": "CFF = <i>a</i> log <i>L</i><sub>a</sub> + <i>b</i>",
}


# ================================================================ GLOSSARY
_GLOSS_VI = [
    ("Thời gian suy giảm",
     "Thời gian cần để độ chói đỉnh của một huỳnh quang giảm xuống một phần xác định của độ chói "
     "đỉnh; một thước đo cho biết huỳnh quang còn phát sáng bao lâu sau khi được chùm điện tử kích "
     "thích."),
    ("Hệ số chu kỳ nhiệm vụ",
     "Thời gian dành cho việc địa chỉ hoá mỗi điểm ảnh trong một chu kỳ làm tươi; tỉ lệ nghịch với "
     "số điểm ảnh."),
    ("Phông chữ",
     "Chỉ hình thức mà chữ-số và các ký hiệu được tạo ra."),
    ("Kích thước đốm sáng",
     "Kích thước của đốm sáng phát ra từ chùm điện tử; giới hạn kích thước của dòng mành."),
    ("Chiếu sáng xuyên",
     "Chiếu sáng từ phía sau bề mặt màn hình, để làm nổi bật thông tin trên chính bề mặt đó; ví dụ "
     "chiếu sáng cho đồng hồ đo trên ô tô hoặc máy bay."),
    ("Xoá trắng",
     "Sự mất độ tương phản (tức giảm dải động) ở LED khi ánh sáng môi trường phản xạ từ nền của bề "
     "mặt màn hình tiến gần mức ánh sáng của vùng hoạt động."),
]

_GLOSS_EN = [
    ("Decay time",
     "The time required for the peak brightness of a phosphor to drop to a defined fraction of peak "
     "luminance; a measure of how long the phosphor remains illuminated after being energized by the "
     "electron beam."),
    ("Duty cycle",
     "The time spent addressing each pixel during a refresh cycle; inversely proportional to the "
     "number of pixels."),
    ("Font",
     "Refers to the form in which alphanumerics and symbols are produced."),
    ("Spot size",
     "The size of the illuminated spot from the electron beam; limits the size of the raster line."),
    ("Transillumination",
     "Illumination from the side of a display surface, to highlight information on the surface "
     "itself; e.g., lighting for automobile or aircraft instruments."),
    ("Wash out",
     "The loss of contrast (i.e., reduction in dynamic range) in an LED as the ambient light "
     "reflected off the background of the display surface approaches the light level of the active "
     "area."),
]


def _glossary(items):
    o = ['<dl class="glossary">']
    for term, body in items:
        o.append("<dt>%s</dt><dd>%s</dd>" % (term, body))
    o.append("</dl>")
    return "".join(o)


# ================================================================ REFERENCES
_REFS = [
    "S. Sherr, <i>Electronic Displays</i>, 2nd ed. New York: John Wiley &amp; Sons, 1993.",
    "M.S. Sanders and E.J. McCormick, <i>Human Factors in Engineering and Design</i>, 6th ed. "
    "New York: McGraw-Hill, 1987.",
    "E. Grandjean, Design of VDT workstations, in G. Salvendy, Ed., <i>Handbook of Human "
    "Factors</i>, New York: John Wiley &amp; Sons, 1987.",
    "D.G. Payne, V.A. Lang, and J.M. Blackwell, Mixed vs. pure display format in integration and "
    "nonintegration visual display monitoring tasks, <i>Human Factors</i>, 37(3), 507–527, 1995.",
    "N.H. Lehrer, The challenge of the cathode-ray tube, in L.E. Tannas, Jr., Ed., <i>Flat-Panel "
    "Displays and CRTs</i>, New York: Van Nostrand Reinhold, 1985.",
    "M. Hartney, ARPA display program and the national flat panel display initiative, in "
    "<i>Proc. 2nd Int. Workshop on Active Matrix Liquid Crystal Displays</i>, IEEE, 8–15, 1995.",
    "T. Morita, An overview of active matrix LCDs in business and technology, in <i>Proc. 2nd Int. "
    "Workshop on Active Matrix Liquid Crystal Displays</i>, IEEE, 1–7, 1995.",
    "I-W. Wu, High-definition displays and technology trends in TFT-LCDs, <i>J. Soc. Inf. "
    "Display</i>, 2(1), 1–14, 1991.",
    "L. Weber, Plasma displays, in L.E. Tannas, Jr., Ed., <i>Flat-Panel Displays and CRTs</i>, "
    "New York: Van Nostrand Reinhold, 1985.",
    "Y. Amano, A new hybrid ac–dc plasma display panel, <i>J. Soc. Inf. Display</i>, 2(1), 57–58, "
    "1994.",
]

_FURTHER = [
    "E. Grandjean, <i>Ergonomics in Computerized Offices</i>, London: Taylor &amp; Francis, 1987, is "
    "an excellent all-around treatise on the principles of effective VDT selection and use. "
    "Summarizes a wide range of research literature. If this volume is difficult to obtain, a "
    "chapter by the same author is also included in the <i>Handbook of Human Factors</i> "
    "(Reference 2).",
    "M.G. Helander, Design of visual displays, in G. Salvendy, Ed., <i>Handbook of Human "
    "Factors</i>, New York: John Wiley &amp; Sons, 1987, is an excellent and concise review of "
    "major human factors principles for display design and use. Includes a critical review of the "
    "foundation literature in this area.",
    "S. Sherr, <i>Electronic Displays</i>, 2nd ed., New York: John Wiley &amp; Sons, 1993, offers "
    "clear presentations of all important display technologies, together with a good summary of "
    "performance measurement methods for display systems. Well illustrated with a variety of "
    "commercial products.",
    "L.E. Tannas, Jr., Ed., <i>Flat-Panel Displays and CRTs</i>, New York: Van Nostrand Reinhold, "
    "1985, provides a thorough, yet highly readable examination of the physical principles behind "
    "essentially every major display technology. Although the technology capabilities have become "
    "dated since publication, this is well worth review.",
]


# ================================================================ BODY — VI
def body_vi():
    b = []
    b.append(note(
        "<b>Ghi chú của người dịch.</b> Bản gốc in năm 1999 bị lỗi chế bản ở cả sáu công thức, "
        "nên cả sáu đã được đọc lại trực tiếp từ trang in chứ không lấy theo bản trích văn bản. "
        "(90.1) in là <i>R</i> = π × độ chói/độ rọi, nhưng bản trích làm hỏng dấu π × thành “p´”. "
        "(90.2) in là <i>K</i> = Δ<i>I</i>/<i>I</i>; bản trích mất chữ Δ nên thành “DI”. (90.3) in "
        "là một phân số 3438<i>H</i>/<i>D</i>. (90.4) in là <i>E</i> = <i>E</i><sub>m</sub> "
        "cos<sup>4</sup> θ; bản trích thành “EE = m cos4 q”. (90.5) in là một phân số với tử là "
        "hiệu hai độ chói và mẫu là độ chói của vật sáng hơn. (90.6) in là CFF = <i>a</i> log "
        "<i>L</i><sub>a</sub> + <i>b</i>; bản trích đảo thành “CFF a L b =+ log a”. "
        "Các lỗi ký tự khác: “»0.02” là <b>≈</b>0,02; “2 ´ 10–7 lx” là 2 × 10<sup>−7</sup> lx; "
        "“cd/m2” thực ra được in đúng là cd/m², chỉ bị mất chỉ số trên khi trích xuất. Trong định "
        "nghĩa <i>Transillumination</i>, bản gốc in “surface itself;, e.g.” với một dấu chấm phẩy "
        "thừa trước dấu phẩy. Ở mục 90.5, bản gốc in “displays which do no flicker” (đúng là <i>do "
        "not flicker</i>) và “an excellent summaries” (đúng là <i>excellent summaries</i>); ở mục "
        "90.11 in “graceful degrades” (đúng là <i>graceful degradation</i>). Ở mục 90.6, câu “the "
        "interested reader is referred to Helander (1987) and Grandjean [3])” có một dấu ngoặc "
        "đóng thừa; Helander (1987) cũng không có trong danh mục tài liệu tham khảo mà chỉ xuất "
        "hiện ở mục “Thông tin thêm”. Ở mục 90.7, danh sách ưu điểm được đánh số (1)–(6) nhưng "
        "mục (2) lại gộp ba đặc tính khác nhau. Câu “two of the primary colors — red, blue, and "
        "green” nói “hai” nhưng liệt kê ba màu. Mục “Thông tin thêm” dẫn “Handbook of Human "
        "Factors (Reference 2)” cho chương của Grandjean, nhưng chương đó là tài liệu số 3; tài "
        "liệu số 2 là Sanders và McCormick. Ba điểm cần lưu ý về nội dung: định nghĩa hệ số phản xạ "
        "trong 90.2 nói tỉ số giữa lượng ánh sáng <i>đập vào</i> bề mặt và lượng ánh sáng <i>rời "
        "khỏi</i> nó, tức ngược với chính công thức (độ chói/độ rọi = ánh sáng ra/ánh sáng tới); "
        "tên cơ quan được in là “International Lighting Commission (CIE)”, trong khi tên chính thức "
        "là <i>International Commission on Illumination</i>; và các đỉnh phổ của ba loại tế bào nón "
        "được in là 670, 470 và 400 nm, trong khi các giá trị thường được dẫn là khoảng 564, 534 "
        "và 420 nm. Hình 90.1 được in nhãn “16-segment font” nhưng chỉ vẽ mười bốn vị trí đoạn; "
        "nhãn in được giữ nguyên."))

    # ------------------------------------------------------------ 90.1
    b.append(h2("90.1 Giới thiệu", "Introduction"))
    b.append(p(
        "Hệ thống hiển thị là mắt xích cuối cùng giữa quá trình đo lường và người dùng. Nếu màn "
        "hình không dễ nhìn và dễ hiểu thì chính quá trình đó bị ảnh hưởng. Vì vậy, cả năng lực "
        "cảm giác và các đặc điểm nhận thức của người dùng đều phải được tính đến khi lựa chọn hệ "
        "thống hiển thị. Hơn nữa, các công nghệ hiển thị và năng lực hiệu năng của chúng dễ đánh "
        "giá hơn khi đặt trong bối cảnh ứng dụng dự kiến. Việc xem xét những vấn đề sau có thể thu "
        "hẹp phạm vi tìm kiếm các hệ thống ứng viên và tránh được những thất vọng không cần thiết "
        "trong quá trình sử dụng hệ thống:"))
    b.append(ul([
        "<b>Môi trường.</b> Màn hình sẽ được vận hành dưới ánh nắng hay ban đêm?",
        "<b>Ứng dụng.</b> Màn hình sẽ trình bày dữ liệu chữ-số, hình ảnh video, đồ hoạ, hay một "
        "tổ hợp nào đó?",
        "<b>Kịch bản nhiệm vụ.</b> Có yêu cầu về tính di động, vận hành cầm tay hay xem theo nhóm "
        "không?",
        "<b>Đặc tính hệ thống.</b> Khối lượng, thể tích, công suất, bảo trì, chi phí, v.v.",
    ]))
    b.append(p(
        "Chương này bắt đầu bằng những nội dung cơ bản về ánh sáng và thị giác. Sau đó chuyển sang "
        "bàn về các năng lực thị giác và những đặc tính hiển thị phải được ghép tương ứng với "
        "chúng."))

    # ------------------------------------------------------------ 90.2
    b.append(h2("90.2 Cơ sở của phép đo ánh sáng", "Fundamentals of Light Measurement"))
    b.append(p(
        "Đại lượng nền tảng của ánh sáng là quang thông, tức tốc độ mà năng lượng ánh sáng được "
        "phát ra từ một nguồn, biểu thị bằng lumen (lm). Cường độ sáng là quang thông trên một đơn "
        "vị góc khối, đơn vị đo là candela (cd). Đại lượng này phân biệt với độ rọi, hay độ chiếu "
        "sáng, đơn giản là quang thông trên một đơn vị diện tích, biểu thị bằng lux (lx). Độ chói "
        "là đại lượng đo độ sáng, tức lượng ánh sáng trên một đơn vị diện tích, do một bề mặt phát "
        "ra hoặc phản xạ lại. Đơn vị đo độ chói là candela trên mét vuông (cd/m²) hoặc nit. Cuối "
        "cùng, hệ số phản xạ là một tỉ số không thứ nguyên giữa lượng ánh sáng đập vào một bề mặt "
        "và lượng ánh sáng rời khỏi nó:"))
    b.append(eq(_EQ_VI["90.1"], "90.1"))
    b.append(p("Hệ số phản xạ cao có thể gây loá, làm giảm mạnh năng lực thị giác."))

    # ------------------------------------------------------------ 90.3
    b.append(h2("90.3 Cơ sở của thị giác", "Fundamentals of Vision"))
    b.append(p(
        "Mắt hoạt động rất giống một máy ảnh thông thường. Ánh sáng vào mắt qua một giác mạc trong "
        "suốt và được điều biến bởi đồng tử, một khẩu độ thay đổi được điều khiển bởi các cơ của "
        "mống mắt. Đồng tử mở rộng trong môi trường tối và thu nhỏ trong môi trường sáng để điều "
        "chỉnh dải cường độ ánh sáng đi vào mắt. Các tia sáng sau đó bị khúc xạ bởi một thấu kính "
        "điều chỉnh được và được hội tụ trên võng mạc, nơi bắt đầu quá trình tạo ảnh thần kinh. "
        "Võng mạc chứa cả tế bào nón và tế bào que, hai loại tế bào cảm thụ ánh sáng hoàn toàn "
        "khác nhau. Tế bào nón tập trung gần điểm vàng, tức 2° trung tâm của trường nhìn, và giảm "
        "nhanh theo khoảng cách từ vùng này. Ngược lại, tế bào que hầu như không có ở điểm vàng và "
        "tăng mật độ theo khoảng cách."))
    b.append(p(
        "Mắt nhạy cảm với ba đặc tính của bức xạ điện từ: (1) độ sáng (cường độ của ánh sáng môi "
        "trường hoặc ánh sáng tới, đo bằng lux), (2) sắc màu (bước sóng ánh sáng, đo bằng nm), và "
        "(3) độ bão hoà (nồng độ tương đối của những sắc màu cụ thể trong ánh sáng, đo bằng một tỉ "
        "số không thứ nguyên từ 0 đến 1). Tế bào nón nhạy cảm khác nhau với bước sóng, tức sắc màu, "
        "và có khả năng phân giải cao hơn tế bào que nhờ ánh xạ một-một lên các dây thần kinh thị "
        "giác. Tế bào nón lại được chia thành ba loại, mỗi loại nhạy cảm nhất với một phần khác "
        "nhau của phổ ánh sáng khả kiến: (1) đỏ (đỉnh 670 nm), (2) lục (đỉnh 470 nm), và (3) lam "
        "(đỉnh 400 nm). Tế bào que nhạy cảm với ánh sáng hơn tế bào nón và có các kết nối nhiều-một "
        "với những dây thần kinh đi ra khỏi mắt, một đặc điểm cho phép tổng hợp thần kinh các tín "
        "hiệu ánh sáng yếu. Khả năng của con người phân biệt những khác biệt về mức độ chói, độ "
        "bão hoà hay sắc màu được chi phối bởi một hàm tâm-vật lý gọi là định luật Weber:"))
    b.append(eq(_EQ_VI["90.2"], "90.2"))
    b.append(p(
        "trong đó Δ<i>I</i> là độ chênh lệch, hay độ thay đổi, cường độ; <i>I</i> là cường độ ban "
        "đầu; và <i>K</i> là phân số Weber. Các giá trị của <i>K</i> đã được xác định bằng thực "
        "nghiệm cho độ chói (0,079), độ bão hoà (0,019 với màu đỏ) và sắc màu (≈0,02 đến 0,04, tuỳ "
        "vùng của phổ khả kiến)."))
    b.append(p(
        "Thị giác ban ngày (<i>photopic</i>) xuất hiện ở những mức ánh sáng mà cả tế bào que và tế "
        "bào nón đều nhạy cảm. Cường độ ánh sáng tối thiểu cần cho thị giác ban ngày là khoảng "
        "2 lx; màu sắc được nhìn thấy trong vùng này. Khi độ chói giảm, một quá trình chuyển tiếp "
        "từ thị giác ban ngày sang thị giác ban đêm (<i>scotopic</i>) diễn ra và cảm nhận màu sắc "
        "mất dần, một hiện tượng có thể ảnh hưởng đến việc diễn giải thông tin mã hoá bằng màu "
        "trong ánh sáng yếu. Cảm nhận về lam và đỏ mất trước, rồi đến lam lục và vàng cam, và cuối "
        "cùng là lục, tức những bước sóng mà mắt nhạy cảm nhất. Mắt trở nên nhạy cảm nhất với bước "
        "sóng khoảng 550 nm (lục) ở gần giới hạn của thị giác ban ngày. Thị giác ban đêm xuất hiện "
        "ở những mức ánh sáng thấp (2 × 10<sup>−7</sup> lx đến 2 lx) và chủ yếu liên quan đến tế "
        "bào que; chỉ nhìn thấy các sắc độ xám không màu. Quá trình chuyển từ thị giác ban ngày "
        "sang ban đêm diễn ra chậm, cần khoảng 30 phút để điều chỉnh hoàn toàn từ độ nhạy thị giác "
        "ban ngày sang độ nhạy thị giác ban đêm."))

    # ------------------------------------------------------------ 90.4
    b.append(h2("90.4 Năng lực thị giác", "Visual Performance"))
    b.append(p(
        "Độ tinh mắt là khả năng phân biệt chi tiết. Tác động của thấu kính nhằm thay đổi tiêu cự "
        "cho những vật ở khoảng cách khác nhau gọi là điều tiết. Độ tinh mắt phân ly tối thiểu, "
        "thước đo phổ biến nhất của khả năng phân biệt, được xác định bởi chi tiết nhỏ nhất mà mắt "
        "có thể phát hiện, và được đo bằng nghịch đảo của góc thị giác mà chi tiết đó chắn tại "
        "mắt. Góc thị giác, tính bằng phút cung, được tính như sau"))
    b.append(eq(_EQ_VI["90.3"], "90.3"))
    b.append(p(
        "trong đó <i>H</i> là chiều cao của vật và <i>D</i> (cùng đơn vị) là khoảng cách từ người "
        "quan sát. Khả năng phân biệt một vật với môi trường xung quanh gọi là độ nhìn thấy. Thuật "
        "ngữ này liên quan đến độ tinh mắt, nhưng kết hợp một cách ngầm định các yếu tố kích thước "
        "vật, độ tương phản (tức bao gồm cả những khác biệt về sắc màu và độ bão hoà) và độ chói — "
        "tất cả tương tác để quyết định hiệu năng phát hiện thị giác thực sự. Ở mức chức năng hơn, "
        "khả năng đọc hay tính dễ đọc mô tả khả năng phân biệt các nhóm vật có nghĩa (ví dụ những "
        "từ tách ra từ một nhóm chữ cái trên màn hình)."))
    b.append(p(
        "Những tham số khác ảnh hưởng đến năng lực thị giác gồm góc nhìn và khoảng cách nhìn. Góc "
        "nhìn tại mắt được đo từ một đường đi qua trục thị giác đến điểm đang được nhìn, và quyết "
        "định vị trí vật sẽ được ghi nhận trên võng mạc. Độ phân giải hình ảnh tốt nhất xảy ra ở "
        "điểm vàng, ngay trên đường nhìn, và độ tinh mắt giảm khi góc lệch khỏi trục này tăng. Góc "
        "nhìn tại màn hình là góc, tính bằng độ, giữa đường pháp tuyến với mặt màn hình và trục thị "
        "giác của người dùng. Góc nhìn tốt nhất dĩ nhiên là trên trục thị giác và vuông góc với mặt "
        "màn hình, vì độ chói giảm ở hầu hết các màn hình khi góc lệch khỏi pháp tuyến tăng. Độ "
        "giảm độ chói theo góc nhìn có thể tính như sau"))
    b.append(eq(_EQ_VI["90.4"], "90.4"))
    b.append(p(
        "trong đó <i>E</i><sub>m</sub> là độ rọi tại tâm màn hình và θ là góc nhìn. Lưu ý rằng đã "
        "định nghĩa hai góc nhìn — tại mắt và tại màn hình. Khoảng cách nhìn được quyết định chủ "
        "yếu bởi yêu cầu về kích thước tối thiểu (tức góc thị giác) cho những vật mà người dùng "
        "phải nhìn. Khoảng cách đọc thông thường là khoảng 71 cm, mặc dù các thiết bị hiển thị video "
        "(VDT) thường được đọc ở 46 cm. Hầu hết các tiêu chí thiết kế giả định khoảng cách nhìn từ "
        "50 đến 70 cm."))
    b.append(p(
        "Mỏi mắt là một thuật ngữ không chính xác nhưng được dùng phổ biến, chỉ sự khó chịu, bực "
        "bội hay không thoải mái gắn với những nhiệm vụ thị giác được thực hiện trong điều kiện kém "
        "hoặc trong thời gian dài. Một nguyên nhân phổ biến của mỏi mắt là loá, có thể do tổ hợp của "
        "độ chói cao, hệ số phản xạ cao và các phản xạ gương (như gương) khiến ánh sáng nguồn phản "
        "chiếu trực tiếp vào mắt. Giảm thiểu hoặc loại bỏ loá là điều thiết yếu để có hiệu năng "
        "hiển thị tốt, và thường bao gồm việc đặt màn hình một cách có suy tính, bố trí đèn trong "
        "phòng hợp lý, kiểm soát ánh sáng môi trường (ví dụ rèm cửa) hoặc dùng các tấm che màn "
        "hình."))

    # ------------------------------------------------------------ 90.5
    b.append(h2("90.5 Các yếu tố cần xét về hiệu năng hiển thị",
                "Display Performance Considerations"))
    b.append(p(
        "Độ phân giải là thước đo vật nhỏ nhất có thể phân giải trên một màn hình, biểu thị bằng số "
        "dòng hiển thị trên milimét hoặc trên xentimét. Mặc dù độ nét, và ngược lại là độ nhoè, "
        "thường được định nghĩa bằng phản ứng chủ quan của người dùng màn hình, độ nét đã được đo "
        "một cách hình thức bằng tỉ số giữa vùng biên bị nhoè của chữ cái và độ rộng nét của chúng "
        "[3]. Tính dễ đọc liên quan đến chất lượng ký tự, hay khả năng đọc, và phụ thuộc vào độ nét "
        "của các ký tự."))
    b.append(p(
        "Độ tương phản, hay tỉ số tương phản, là thước đo chênh lệch độ chói giữa một vật và nền "
        "của nó. Dù trong tài liệu tồn tại nhiều định nghĩa khác nhau, độ tương phản độ chói được Uỷ "
        "ban Chiếu sáng Quốc tế (CIE) thông qua được cho như sau"))
    b.append(eq(_EQ_VI["90.5"], "90.5"))
    b.append(p(
        "Những màn hình có độ chói thấp hơn cần độ tương phản lớn hơn để đạt được cùng độ nhìn thấy "
        "của vật. Độ tương phản, hay tỉ số độ chói, giữa hai bề mặt trong trường nhìn trung tâm (ví "
        "dụ một màn hình và mặt bàn đặt nó) nên vào khoảng 3:1, trong khi tỉ số giữa trường trung "
        "tâm và những bề mặt xa hơn (ví dụ quanh phòng) có thể lên tới 10:1. Tỉ số lớn hơn mức này "
        "có thể gây loá. Những phương pháp đơn giản nhất để tăng cường độ tương phản là dùng tấm che "
        "kiểu mui hoặc màn hình có thể nghiêng ra khỏi nguồn sáng gây hại. Tuy vậy, các bộ lọc tăng "
        "tương phản có thể hiệu quả hơn. Mọi bộ lọc đều liên quan đến việc giảm lượng ánh sáng môi "
        "trường phản xạ trở lại người dùng, trong khi giữ cho ánh sáng phát ra từ nội dung hiển thị "
        "càng không đổi càng tốt. Có nhiều chiến lược lọc khác nhau, gồm khắc mờ hoặc làm nhám bề "
        "mặt màn hình để tách và tán xạ các phản xạ gương. Bộ lọc mật độ trung tính tăng độ tương "
        "phản bằng cách giảm lượng ánh sáng đi qua chúng; ánh sáng môi trường phải đi qua hai lần "
        "trước khi đến mắt người dùng, trong khi nội dung hiển thị chỉ phải đi qua một lần. Bộ lọc "
        "lưới vi mô đặt trên bề mặt màn hình hạn chế sự xuyên qua của ánh sáng để chỉ những tia rơi "
        "vuông góc với lưới mới có thể xuyên qua; điều này chặn cả phản xạ gương và phản xạ khuếch "
        "tán, và tăng độ tương phản. Kính phân cực tròn là những bộ lọc mật độ trung tính làm phân "
        "cực ánh sáng tới, rồi ánh sáng đó bị ngăn không cho quay trở lại qua bộ lọc. Các lớp phủ "
        "màng mỏng một phần tư bước sóng giao thoa với cả phản xạ gương và phản xạ khuếch tán."))
    b.append(p(
        "Thang độ xám chỉ số mức độ chói, hay số sắc độ xám, có sẵn trong một màn hình. Định nghĩa "
        "phổ biến là tỉ số độ chói 1,4 giữa các mức, mặc dù mắt có thể phân biệt những thay đổi nhỏ "
        "tới 1,03 (giá trị <i>K</i> của Weber là 0,03). Số sắc độ xám hữu ích để đánh giá khả năng "
        "của một màn hình trong việc thể hiện thông tin hình ảnh hoặc dải mức độ chói có thể dùng "
        "để mã hoá. Mức chói cao nhất do năng lực của màn hình quyết định, nhưng mức thấp nhất do "
        "độ chói của bề mặt màn hình khi không có tín hiệu quyết định. Ánh sáng mạnh chiếu vào màn "
        "hình có thể nâng mức tối thiểu này lên và làm giảm số sắc độ xám dùng được."))
    b.append(p(
        "Nhấp nháy là thuật ngữ chỉ những thay đổi phát hiện được của độ chói màn hình, và xảy ra "
        "khi tần số của những thay đổi đó thấp hơn khả năng tích hợp của mắt. Tần số tối thiểu mà "
        "tại đó điều này xảy ra là tần số hợp nhất nhấp nháy tới hạn, hay CFF, phụ thuộc vào mức độ "
        "chói của hình ảnh; nghĩa là những màn hình không nhấp nháy ở mức chói cao vẫn có thể nhấp "
        "nháy ở mức thấp. CFF được tính như sau"))
    b.append(eq(_EQ_VI["90.6"], "90.6"))
    b.append(p(
        "trong đó <i>a</i> = 12,5 cho mức ánh sáng môi trường cao (ban ngày) và 1,5 cho mức thấp "
        "(ban đêm), <i>L</i><sub>a</sub> là độ chói trung bình của hình ảnh tính bằng cd/m² hoặc "
        "nit, và <i>b</i> = 37. Đây là một công thức thực nghiệm, và các giá trị của <i>a</i> và "
        "<i>b</i> chỉ là gần đúng. Vì mắt không thể thích nghi với nhấp nháy đủ nhanh để điều khiển "
        "ánh sáng trên võng mạc, sự khó chịu thị giác thường xuất hiện khi có nhấp nháy."))
    b.append(p(
        "Nhiều tham số hiển thị được phát biểu theo điểm ảnh, hay phần tử hình. Điểm ảnh là phần tử "
        "địa chỉ hoá được nhỏ nhất trong một màn hình điện tử, hoặc là phần tử thông tin phân giải "
        "được nhỏ nhất mà người dùng nhìn thấy. Tốc độ làm tươi là tần số mà các điểm ảnh của màn "
        "hình được chiếu sáng lại. Tốc độ làm tươi dưới 50 đến 80 Hz có thể gây ra nhấp nháy cảm "
        "nhận được. Tốc độ cập nhật là tần số mà nội dung thông tin của màn hình được thay đổi."))
    b.append(p(
        "Tính tuyến tính là độ lệch của một đường thẳng so với dạng chính xác của nó, biểu thị bằng "
        "phần trăm tổng chiều dài đường. Méo hình mẫu là độ lệch của bất kỳ phần tử nào của một hình "
        "mẫu (ví dụ một lưới) so với vị trí chính xác của nó, biểu thị theo kích thước của toàn hình "
        "mẫu. Dù không có giới hạn cụ thể nào gắn với những tham số này, việc diễn giải dữ liệu đo "
        "rõ ràng có thể bị ảnh hưởng nếu quan sát thấy phi tuyến trên màn hình."))
    b.append(p(
        "Đã có nhiều mô hình toán học được xây dựng để định lượng chất lượng hình ảnh hiển thị thành "
        "một “chỉ số phẩm chất” duy nhất. Những mô hình này tuy hữu ích nhưng quá phức tạp để trình "
        "bày ở đây, và bạn đọc được giới thiệu đến những bản tổng quan xuất sắc trong tài liệu [1] "
        "để biết thêm."))

    # ------------------------------------------------------------ 90.6
    b.append(h2("90.6 Các yếu tố cần xét về nội dung hiển thị",
                "Display Content Considerations"))
    b.append(p(
        "Những gói phần mềm cấu hình được dành cho đo lường khoa học (ví dụ LabView™) cho phép rất "
        "nhiều linh hoạt trong thiết kế định dạng hiển thị. Vì vậy, các nguyên tắc yếu tố con người "
        "cho nội dung hiển thị quan trọng đối với việc đo lường hiệu quả không kém gì các đặc tính "
        "điện tử của bản thân màn hình. Những nguyên tắc sau là phần giới thiệu về các loại vấn đề "
        "phải xem xét khi thiết kế nội dung hiển thị. Bạn đọc quan tâm được giới thiệu đến Helander "
        "(1987) và Grandjean [3] để biết thông tin về yếu tố con người và các hướng dẫn thiết kế "
        "ngoài những gì được trình bày ở đây."))

    b.append(h3("Hiển thị chữ-số", "Alphanumeric Displays"))
    b.append(p(
        "Kích thước của một chữ cái là cỡ chữ (<i>pitch</i>) của nó. Một khuyến nghị chung là các "
        "ký tự phải chắn một góc tối thiểu khoảng 12 phút cung ở những khoảng cách đọc thông "
        "thường. Màn hình chữ-số thường được cấu tạo từ các mảng điểm ảnh hoặc các thanh phân đoạn "
        "(Hình 90.1). Mảng điểm ảnh 5 × 7 được coi là mức tối thiểu cần thiết để biểu diễn bộ ký tự "
        "ASCII. Nhiều điểm ảnh hơn có thể tăng tính dễ đọc nhưng với chi phí cao hơn cho mạch điều "
        "khiển. Ma trận thanh bảy đoạn cũng là một thiết kế phổ biến và có hiệu năng tốt, nhưng các "
        "mảng tới 16 đoạn đã có sẵn để có diện mạo đẹp hơn."))
    b.append(fig(1))
    b.append(p(
        "Độ rộng nét là tỉ số giữa độ dày nét và chiều cao chữ cái. Những khuyến nghị cho tính dễ "
        "đọc là 1:6 đến 1:8, hoặc 1:8 đến 1:10 [2]. Khi độ chiếu sáng giảm, chữ đậm dễ đọc hơn chữ "
        "mảnh. Với độ chiếu sáng thấp và độ tương phản thấp, chữ nên là kiểu đậm với tỉ số độ rộng "
        "nét trên chiều cao thấp (ví dụ 1:5)."))

    b.append(h3("Hiển thị định lượng và hiển thị trạng thái",
                "Quantitative and Status Displays"))
    b.append(p(
        "Dù màn hình đọc số dễ triển khai bằng phần mềm, màn hình kim tương tự lại tỏ ra có lợi thế "
        "khi điều quan trọng là quan sát hướng hoặc tốc độ thay đổi của các giá trị được trình bày "
        "[4]. Nếu ứng dụng đo lường liên quan đến những cách hiểu “nhiều hơn hay ít hơn” hoặc “lên "
        "hay xuống”, thì thang thẳng hoặc thang nhiệt kế được ưa thích vì nó cho thấy phép đo trong "
        "tương quan với số không. Kim động truyền đạt được những thay đổi nhỏ trong số đọc tốt hơn "
        "kim cố định hay màn hình đọc số. Các vạch chia độ phải phản ánh độ dài của đơn vị nhỏ nhất "
        "cần đọc. Nên có một vạch đánh dấu cho mỗi đơn vị, để không phải nội suy."))
    b.append(p(
        "Các chỉ thị kiểm tra đọc được dùng để xác định xem một điều kiện có “bình thường” hay "
        "không. Vì vậy, điểm tiêu chí bình thường phải được mã hoá rõ ràng. Nếu nhiều chỉ thị được "
        "nhóm lại với nhau, chúng phải được sắp xếp sao cho số đọc lệch trở nên nổi bật (ví dụ bằng "
        "cách chỉ ra chiều cao cột hoặc góc kim khác đi, v.v.)."))
    b.append(p(
        "Màu sắc là một phương pháp tuyệt vời để tổ chức thông tin trên màn hình và để định vị vật "
        "thể nhanh chóng. Dù người dùng màn hình có thể phân biệt được nhiều màu khác nhau, họ "
        "thường không nhớ được quá bảy đến mười màu, nên số màu phải được hạn chế nếu dùng màu như "
        "một chiều mã hoá."))

    b.append(h3("Tóm tắt", "Summary"))
    b.append(p(
        "Những mục tiếp theo bàn về các công nghệ hiển thị khác nhau dưới ánh sáng của những nguyên "
        "tắc đã thảo luận ở đây. Dù hướng dẫn hiển thị có sẵn cho hầu như bất kỳ tham số nào, điều "
        "quan trọng cần nhớ là cảm nhận thị giác là một quá trình tích hợp. Không một hướng dẫn đơn "
        "lẻ nào hoạt động một mình, và chất lượng hiển thị thường là kết quả của những nhu cầu và "
        "sự đánh đổi tương tác lẫn nhau."))

    # ------------------------------------------------------------ 90.7
    b.append(h2("90.7 Hiển thị ống tia điện tử", "Cathode Ray Tube Displays"))
    b.append(p(
        "Ống tia điện tử (CRT, xem Chương 91) cho đến nay là công nghệ hiển thị phổ biến nhất đang "
        "được dùng, và việc nó được sử dụng rộng rãi trong tivi và màn hình máy tính phải bảo đảm sự "
        "hiện diện tiếp tục của nó trong tương lai gần. Những ưu điểm của màn hình dùng CRT gồm (1) "
        "tính linh hoạt (cùng một CRT có thể dùng cho chữ-số, hình ảnh hoặc đồ hoạ), (2) khả năng độ "
        "phân giải cao và hiệu suất phát sáng cao, đáp ứng động cực nhanh (điều có thể quan trọng "
        "với những tín hiệu thay đổi nhanh), (3) sẵn có rộng rãi trên thị trường (ví dụ 2,5 đến "
        "64 cm theo đường chéo), (4) độ tin cậy cao, (5) tuổi thọ dài, và (6) chi phí tương đối "
        "thấp. Màn hình CRT có thể hoạt động tốt trong ánh sáng môi trường mạnh nếu dùng bộ lọc. "
        "Những nhược điểm tiềm tàng của màn hình CRT là cồng kềnh (độ sâu của ống CRT thông thường "
        "có thể bằng hoặc vượt kích thước đường chéo của nó, dù đã có CRT phẳng) và dễ bị ảnh hưởng "
        "bởi phản xạ môi trường và độ chiếu sáng cao. Ánh sáng rơi trên bề mặt nhẵn của màn hình có "
        "thể tạo ra một độ rọi màn che làm xoá mất độ tương phản của màn hình và làm giảm số màu có "
        "thể cảm nhận được."))

    b.append(h3("Hiệu năng của CRT", "CRT Performance"))
    b.append(p(
        "Nhiều đặc tính của màn hình CRT phụ thuộc vào loại huỳnh quang được chọn cho thiết kế. Vật "
        "liệu huỳnh quang rất khác nhau về hiệu suất phát sáng, màu sắc và thời gian suy giảm. Thời "
        "gian suy giảm tương tác với tốc độ làm tươi của màn hình; một huỳnh quang có thời gian suy "
        "giảm ngắn sẽ cần tốc độ làm tươi cao hơn để tránh những hiệu ứng nhấp nháy quan sát được. "
        "Chọn một CRT có thời gian suy giảm huỳnh quang cao cũng dẫn đến việc chọn một ống có độ "
        "chói trung bình cao. Độ phân giải phụ thuộc vào kích thước đốm sáng của huỳnh quang được "
        "kích thích (mà thực chất là độ dày của dòng mành). Kích thước đốm sáng cũng phụ thuộc vào "
        "điện áp gia tốc và dòng chùm tia của súng catôt, nên phải ghi nhận dữ liệu của nhà sản xuất "
        "theo điện áp và dòng mà tại đó các phép đo được thực hiện, rồi so sánh với điều kiện vận "
        "hành dự kiến. Độ phân giải CRT được đo theo hai cách. Dòng truyền hình là số những dòng "
        "phân biệt được, xếp sát nhau nhất, có thể phân biệt trên một biểu đồ thử EIA (Hiệp hội "
        "Công nghiệp Điện tử). Những dòng mành co lại liên quan đến một quá trình giảm khoảng cách "
        "giữa các dòng của một hình mẫu thử cho đến khi không còn thấy dòng nào. Điểm này sau đó "
        "được biểu thị bằng số dòng trên xentimét, và là một thước đo tốt hơn cho các ứng dụng hiển "
        "thị đo lường. Số dòng quét tăng lên cải thiện tính dễ đọc của ký hiệu và chất lượng hình "
        "ảnh. Hầu hết các màn hình CRT thông thường có 525 dòng quét, nhưng đã có những hệ thống "
        "tới 5000 dòng [5]. Phương pháp chính để có màn hình CRT màu là dùng một hoặc nhiều chùm "
        "điện tử để kích thích huỳnh quang cho ba màu cơ bản — đỏ, lam và lục. Một dải màu đầy đủ "
        "đạt được bằng cách kích thích chọn lọc những tổ hợp thích hợp của ba loại huỳnh quang cơ "
        "bản này. Hiệu suất chùm tia bị giảm trong quá trình này, nghĩa là màn hình CRT màu không "
        "sáng bằng các hệ thống CRT đơn sắc. Tỉ số tương phản bị giảm bởi mức ánh sáng môi trường "
        "cao, và thường phải thoả hiệp giữa yêu cầu ánh sáng cho nhiệm vụ công việc và mức ánh sáng "
        "cho độ nhìn CRT tối ưu. Trong điều kiện ánh sáng môi trường thấp, tỉ số tương phản CRT "
        "10:1 thường đạt được. Tỉ số 25:1 có thể đạt được với các bộ lọc tăng tương phản, nhưng "
        "phải đánh đổi bằng độ chói."))

    b.append(h3("Các loại màn hình CRT", "Types of CRT Displays"))
    b.append(p(
        "Ngoài những CRT quét mành thông thường dùng cho màn hình máy tính và trạm làm việc, cần "
        "nêu hai biến thể của công nghệ CRT: CRT lưu trữ nhìn trực tiếp và CRT phẳng. CRT lưu trữ "
        "nhìn trực tiếp được thiết kế để tránh nhu cầu làm tươi huỳnh quang liên tục. Các hệ thống "
        "nhìn trực tiếp thường thêm một lớp tích điện bổ sung — phần tử lưu trữ — ở đâu đó phía sau "
        "lớp huỳnh quang, và thêm một súng điện tử để duy trì điện tích này. Thông tin được hiển thị "
        "được giữ lại cho đến khi bị xoá một cách chủ động. CRT phẳng được phát triển để đáp ứng nhu "
        "cầu về hiệu năng CRT trong một kết cấu vật lý nhỏ hơn. Kỹ thuật thiết kế cơ bản đặt súng "
        "điện tử vuông góc với màn hình và, thông qua mạch hội tụ bổ sung hoặc một màn huỳnh quang "
        "hơi nghiêng, ghi hình mẫu mành ở một góc lớn. Có thể tìm thêm chi tiết về những thiết kế "
        "CRT này và các thiết kế khác trong Sherr [1]."))

    # ------------------------------------------------------------ 90.8
    b.append(h2("90.8 Hiển thị tinh thể lỏng", "Liquid Crystal Displays"))
    b.append(p(
        "Màn hình tinh thể lỏng (LCD, xem Chương 92) thuộc nhóm công nghệ không phát xạ, tức những "
        "màn hình không tự tạo ra ánh sáng mà điều khiển sự truyền qua hoặc phản xạ của một nguồn "
        "sáng bên ngoài. LCD thay đổi đường quang của ánh sáng khi một điện trường được đặt ngang "
        "qua vật liệu tinh thể lỏng (LC)."))
    b.append(p(
        "Những ưu điểm chính của LCD gồm (1) tiêu thụ công suất rất thấp (quan trọng với các hệ "
        "thống chạy pin và di động như máy tính bỏ túi), (2) kết cấu phẳng, (3) chi phí vật liệu cơ "
        "bản thấp, và (4) độ tương phản xuất sắc trong ánh sáng môi trường mạnh. Tuy vậy, một số "
        "LCD có đáp ứng động chậm (tức việc bật và tắt các phần tử hiển thị); ví dụ thời gian lên "
        "100 đến 500 ms là nhận thấy được bằng mắt và những hệ thống như vậy có thể không chấp nhận "
        "được cho các ứng dụng đo lường. Độ chói thấp là một nhược điểm khác, và có thể làm màn hình "
        "khó đọc trong điều kiện ánh sáng yếu nếu không có nguồn sáng bên ngoài. Ngoài ra, góc nhìn "
        "bị hạn chế bởi những đặc tính nội tại của LC, và thường nhỏ hơn 45° nếu không có thiết kế "
        "đặc biệt. Nhiều đặc tính của LCD, như ngưỡng chuyển mạch và thời gian đáp ứng, phụ thuộc "
        "nhiệt độ."))

    b.append(h3("Hiệu năng của LCD", "LCD Performance"))
    b.append(p(
        "Có đủ dải năng lực phân giải, từ những màn hình chữ-số đơn giản đến những hệ thống có 63 "
        "triệu điểm ảnh và độ phân giải 47 dòng/cm [6]. LCD chủ yếu được dùng trong các ứng dụng "
        "hiển thị nhỏ (ví dụ máy tính bỏ túi, đồng hồ, v.v.), dù đã có những màn hình đường chéo "
        "53 cm có khả năng video toàn màu [7]."))
    b.append(p(
        "Độ tương phản trong các hệ phân cực được quyết định bởi tỉ số tắt của kính phân cực, tức "
        "tỉ số giữa ánh sáng truyền qua ở hướng phân cực song song và ánh sáng truyền qua ở hướng "
        "phân cực chéo. Tuy vậy, những kính phân cực có tỉ số tắt tốt cũng chịu tổn thất ánh sáng "
        "cao ở hướng truyền qua, nên độ sáng cực đại bị đánh đổi lấy độ tương phản. Đã đạt được "
        "những tỉ số tương phản tới 50:1 [6], dù 20:1 phổ biến hơn."))
    b.append(p(
        "Màn hình màu có thể đạt được bằng cách đặt một khảm màu lên trên LCD và chuyển các ô phía "
        "sau những tổ hợp lỗ khảm thích hợp sang trạng thái truyền qua. Tuy nhiên, phương pháp này "
        "làm giảm độ phân giải và độ sáng, vì các điểm ảnh có sẵn phải được phân bổ cho mỗi một "
        "trong ba màu cơ bản. Việc dùng transistor màng mỏng (TFT) làm công nghệ chuyển mạch cho LCD "
        "là cách tiếp cận mới nhất để tạo ra những màn hình lớn, độ phân giải cao, và là đối tượng "
        "của nghiên cứu kỹ thuật rộng rãi [8]."))

    # ------------------------------------------------------------ 90.9
    b.append(h2("90.9 Hiển thị plasma", "Plasma Displays"))
    b.append(p(
        "Tính đơn giản và độ bền của màn hình plasma (xem Chương 93) khiến công nghệ này trở thành "
        "một ứng viên hấp dẫn cho nhiều nhu cầu đo lường khác nhau, đặc biệt ở những nơi dự kiến có "
        "môi trường khắc nghiệt. Ngoài ra, những đặc tính chuyển mạch của khí plasma vẫn chưa được "
        "khai thác hết, và công nghệ này có tiềm năng xuất sắc cho những cải tiến kỹ thuật trong "
        "tương lai. Các phương pháp plasma được dùng rộng rãi cho màn hình chữ-số trong máy tính "
        "xách tay, máy tính di động và cầm tay, và cho việc hiển thị hình ảnh video."))
    b.append(p(
        "Những ưu điểm của màn hình plasma gồm khả năng lưu trữ được tăng cường, độ chói và hiệu "
        "suất phát sáng. Cũng có thể giữ các điểm ảnh ở trạng thái bật mà không cần tín hiệu làm "
        "tươi liên tục, nghĩa là có thể đạt độ chói cao hơn với cùng công suất và mạch lái. Ưu điểm "
        "này cũng cho phép có tỉ số tương phản xuất sắc trong ánh sáng môi trường mạnh."))
    b.append(p(
        "Màn hình plasma cũng có tuổi thọ hiển thị dài và độ chắc chắn cao. Không hiếm khi màn hình "
        "sống lâu hơn tuổi thọ của sản phẩm mà nó được lắp trong đó, và kết cấu tấm nền tương đối "
        "đơn giản có thể chịu được môi trường sốc và rung mạnh, hoặc nhiệt độ cực đoan. Một số "
        "nhược điểm của màn hình plasma gồm chi phí cao (so với CRT) và yêu cầu công suất cao (so "
        "với LCD). Những công nghệ khác có thể cạnh tranh hiệu quả với thiết bị plasma cho các màn "
        "hình chữ-số nhỏ trong điều kiện thuận lợi."))

    b.append(h3("Hiệu năng của màn hình plasma", "Plasma Display Performance"))
    b.append(p(
        "Màn hình plasma thương mại có sẵn với độ phân giải 40 dòng/cm, và những hệ thống gần "
        "50 dòng/cm đang được phát triển. Đã chế tạo được những hệ thống 2 triệu điểm ảnh [9]. Thang "
        "độ xám đạt được với màn hình dc bằng cách điều chỉnh dòng phóng điện trong mỗi ô. Màn hình "
        "dùng điện áp ac có thể đánh đổi độ phân giải lấy thang độ xám bằng các phương pháp điều "
        "biến không gian, tức bằng cách điều khiển số lượng và vị trí các điểm ảnh được kích hoạt, "
        "thay vì mức chiếu sáng của điểm ảnh. Dù màn hình plasma có thang độ xám tốt, độ chói của "
        "chúng chưa tương đương với CRT. Màn hình plasma thể hiện màu của khí bị ion hoá, thường là "
        "cam (tức nơi dùng neon), dù những hỗn hợp khí hoặc huỳnh quang khác đã được dùng thành "
        "công để mở rộng dải màu. Màn hình lai ac-dc được thiết kế để kết hợp khả năng lưu trữ của "
        "hệ ac với mạch ma trận hiệu quả của thiết bị dc [10]. Màn hình dùng cả hai loại dòng để "
        "tạo phóng điện khí; thành phần dc điều khiển việc địa chỉ hoá điểm ảnh, trong khi thành "
        "phần ac điều khiển các trạng thái lưu trữ của các ô. Màn hình lai plasma–CRT cố gắng dùng "
        "hiệu ứng phóng điện khí của tấm plasma như một nguồn điện tử địa chỉ hoá được bằng ma trận "
        "cho CRT. Kết quả là một hệ thống toàn màu có độ chói cao và hiệu suất phát sáng tốt."))

    # ------------------------------------------------------------ 90.10
    b.append(h2("90.10 Hiển thị điện phát quang", "Electroluminescent Displays"))
    b.append(p(
        "Trừ diode phát quang (LED, xem Chương 95), các công nghệ điện phát quang (EL, xem Chương "
        "94) không nổi bật trên thương trường như những loại hệ thống hiển thị khác. Vật liệu EL "
        "phức tạp (tức được điều khiển và kiểm soát bởi những quá trình liên quan đến vật lý bán "
        "dẫn thể rắn) và khó làm việc hơn các vật liệu hiển thị khác. Tuy vậy, chúng có tiềm năng "
        "lớn về độ chói cao và chi phí thấp, đáng được xem xét, đặc biệt khi những thiết kế mới trở "
        "nên sẵn có. Địa chỉ hoá ma trận được dùng để điều khiển các ứng dụng hiển thị thông tin. "
        "Vật liệu EL được ứng dụng ở hai dạng — bột (PEL) và màng mỏng (TFEL) — và được điều khiển "
        "bằng cả điện áp ac và dc, tạo ra bốn cách tiếp cận thiết kế cơ bản. Một số ưu điểm của màn "
        "hình EL là (1) hiệu suất phát sáng cao (trừ các thiết kế bột ac), (2) đọc được dưới ánh "
        "nắng, (3) có khả năng màu, (4) thiết kế tấm phẳng, gọn, và (5) tiềm năng đáng kể cho việc "
        "chế tạo chi phí thấp. Một nhược điểm của màn hình EL là các hệ thống bột ac (ACPEL) có độ "
        "chói và tỉ số tương phản thấp. Ngoài ra, huỳnh quang trong các thiết kế bột tán xạ và phản "
        "xạ ánh sáng môi trường, làm giảm độ tương phản của chúng."))

    b.append(h3("Hiệu năng của màn hình EL", "EL Display Performance"))
    b.append(p(
        "Đã chứng minh được những tỉ số tương phản 50 đến 150:1 với các hệ thống màng mỏng đơn sắc "
        "(ACTFEL), trong khi đạt 15 đến 20:1 với các thiết kế dc. Thiết kế ACTFEL cũng cho độ chói "
        "xuất sắc, với những mức chói đã chứng minh trên 157 cd/m² (đơn sắc) và 26 cd/m² (màu). Các "
        "thiết kế DCPEL, đại diện cho công nghệ mới hơn, đã đạt trên 100 cd/m² với các thiết kế đơn "
        "sắc, nhưng có thể sớm đạt hoặc vượt những giá trị dựa trên ac. Độ phân giải của màn hình "
        "EL bị hạn chế bởi hệ số chu kỳ nhiệm vụ của việc địa chỉ hoá ma trận; cần một khoảng thời "
        "gian hữu hạn để kích thích mỗi dòng, và cần một mức chói tối thiểu để có hiệu năng hiển "
        "thị đầy đủ, nên biến số còn lại trở thành số dòng địa chỉ hoá được. Một màn hình ACTFEL đã "
        "chứng minh với 640 × 400 phần tử, sáu màu và độ phân giải 27 dòng/cm, là điển hình cho "
        "công nghệ này."))

    # ------------------------------------------------------------ 90.11
    b.append(h2("90.11 Hiển thị diode phát quang", "Light-Emitting Diode Displays"))
    b.append(p(
        "Màn hình diode phát quang (LED, xem Chương 95) liên quan đến những vật liệu huỳnh quang đơn "
        "tinh thể, điều phân biệt chúng với vật liệu EL đa tinh thể đã bàn ở mục trước. Tuy vậy, vật "
        "lý cơ bản đằng sau hoạt động của chúng khá tương tự. Màn hình LED rất linh hoạt và thích "
        "hợp cho nhiều ứng dụng đo lường. Những ưu điểm của màn hình LED gồm độ tin cậy cao và sự "
        "suy giảm êm; từng phần tử LED riêng lẻ có thể hỏng mà không ảnh hưởng đến hiệu năng chung "
        "của màn hình. LED chắc chắn, để vận hành trong môi trường khắc nghiệt, và chịu được nhiệt "
        "độ cực đoan tốt hơn các công nghệ khác. LED cho góc nhìn tốt hơn LCD, và độ chói xuất sắc "
        "để nhìn thấy dưới ánh nắng. Đáng tiếc, màn hình LED cũng tiêu thụ công suất cao khi được "
        "đóng gói thành những màn hình phẳng lớn, và chi phí cao cho việc lắp ráp phức tạp. Có thể "
        "xảy ra nhiễu quang giữa các phần tử mảng nếu dùng đế trong suốt. LED là loại hạn chế nhất "
        "về dải màu (ví dụ không có thiết bị lam nào bán trên thị trường)."))

    b.append(h3("Hiệu năng của màn hình LED", "LED Display Performance"))
    b.append(p(
        "Thiết bị LED có độ chói xuất sắc, nhưng vì độ chói của màn hình cũng là một hàm của các bộ "
        "lọc hoặc thấu kính phóng đại được dùng trên các phần tử LED, nên độ chói của thiết bị tự "
        "nó không phải là thước đo đáng tin cậy cho hiệu năng tổng thể của hệ thống. Màn hình LED "
        "cũng cho độ tương phản độ chói rất tốt. Tuy vậy, độ tương phản sắc độ — khác biệt màu giữa "
        "LED và nền của nó — là một yếu tố khi đánh giá hiệu năng LED mà không thấy ở các công nghệ "
        "khác. Độ tương phản sắc độ có ý nghĩa vì độ bão hoà cao của hầu hết huỳnh quang LED. Nó bị "
        "ảnh hưởng bởi các bộ lọc hiển thị, và có thể có ảnh hưởng đến hiệu năng hiển thị lớn hơn "
        "đáng kể so với độ tương phản độ chói."))
    b.append(p(
        "Đã chế tạo được những màn hình LED với độ phân giải 20 đến 25 dòng/cm. Cũng đã chứng minh "
        "được những màn hình phẳng 38.400 phần tử rời với mức chói khoảng 137 cd/m² (tăng lên "
        "240 cd/m² khi giảm độ phân giải), và ít nhất một màn hình máy bay với 49.000 phần tử đã "
        "được chế tạo. Những màn hình tương đương CRT với 600 × 400 phần tử cũng đã được hiện thực "
        "hoá bằng các mẫu phát triển kỹ thuật."))

    # ------------------------------------------------------------ glossary
    b.append(h2("Định nghĩa các thuật ngữ", "Defining Terms"))
    b.append(_glossary(_GLOSS_VI))

    b.append(h2("Tài liệu tham khảo", "References"))
    b.append(refs(_REFS))

    b.append(h2("Thông tin thêm", "Further Information"))
    b.append('<ul class="ref-list">%s</ul>' % "".join("<li>%s</li>" % i for i in _FURTHER))
    return "".join(b)


# ================================================================ BODY — EN
def body_en():
    b = []
    b.append(note(
        "<b>Translator's note.</b> All six equations are mis-set in the 1999 printed edition as "
        "captured by the text extract, so each was re-read from the page image. (90.1) is printed "
        "<i>R</i> = π × luminance/illuminance, but the extract turns the pi-times sign into "
        "&ldquo;p´&rdquo;. (90.2) is printed <i>K</i> = Δ<i>I</i>/<i>I</i>; the extract drops the "
        "delta and gives &ldquo;DI&rdquo;. (90.3) is printed as the fraction 3438<i>H</i>/<i>D</i>. "
        "(90.4) is printed <i>E</i> = <i>E</i><sub>m</sub> cos<sup>4</sup> θ; the extract gives "
        "&ldquo;EE = m cos4 q&rdquo;. (90.5) is printed as a fraction whose numerator is the "
        "difference of two luminances and whose denominator is the luminance of the brighter "
        "object. (90.6) is printed CFF = <i>a</i> log <i>L</i><sub>a</sub> + <i>b</i>; the extract "
        "scrambles it into &ldquo;CFF a L b =+ log a&rdquo;. Other character defects: "
        "&ldquo;»0.02&rdquo; is <b>≈</b>0.02; &ldquo;2 ´ 10–7 lx&rdquo; is 2 × "
        "10<sup>−7</sup> lx; &ldquo;cd/m2&rdquo; is in fact printed cd/m² and only loses its "
        "superscript in extraction. In the <i>Transillumination</i> definition the original prints "
        "&ldquo;surface itself;, e.g.&rdquo; with a stray semicolon before the comma. In 90.5 the "
        "original prints &ldquo;displays which do no flicker&rdquo; (read: <i>do not flicker</i>) "
        "and &ldquo;an excellent summaries&rdquo; (read: <i>excellent summaries</i>); 90.11 prints "
        "&ldquo;graceful degrades&rdquo; (read: <i>graceful degradation</i>). In 90.6 the sentence "
        "&ldquo;the interested reader is referred to Helander (1987) and Grandjean [3])&rdquo; "
        "carries an extra closing parenthesis, and Helander (1987) appears nowhere in the reference "
        "list — only in Further Information. In 90.7 the advantages are numbered (1)–(6) but item "
        "(2) bundles three separate properties. &ldquo;Two of the primary colors — red, blue, and "
        "green&rdquo; says two and then lists three. Further Information cites &ldquo;Handbook of "
        "Human Factors (Reference 2)&rdquo; for Grandjean's chapter, but that chapter is reference "
        "3; reference 2 is Sanders and McCormick. Three substantive points: the definition of "
        "reflectance in 90.2 describes the ratio of light <i>striking</i> a surface to light "
        "<i>leaving</i> it, which is the reverse of the equation itself (luminance/illuminance = "
        "leaving/incident); the body is named &ldquo;International Lighting Commission (CIE)&rdquo; "
        "where the official name is the <i>International Commission on Illumination</i>; and the "
        "cone peaks are printed as 670, 470 and 400 nm, where the values usually quoted are about "
        "564, 534 and 420 nm. Figure 90.1 is labelled &ldquo;16-segment font&rdquo; although only "
        "fourteen segment positions are drawn; the printed label is kept."))

    # ------------------------------------------------------------ 90.1
    b.append(h2("90.1 Introduction"))
    b.append(p(
        "The display system is the final link between the measuring process and the user. If the "
        "display is not easy to see and easy to understand, then that process is compromised. The "
        "user's sensory capabilities and cognitive characteristics, therefore, must both be "
        "addressed in display system selection. Furthermore, display technologies and performance "
        "capabilities are easier to evaluate in the context of their intended application. "
        "Consideration of the following issues can narrow the search for candidate systems, and can "
        "prevent needless frustration during system use:"))
    b.append(ul([
        "<b>Environment.</b> Will the display be operated in sunlight or at night?",
        "<b>Application.</b> Will the display present alphanumeric data, video images, graphics, or "
        "some combination?",
        "<b>Task scenario.</b> Are portability, handheld operation, or group viewing required?",
        "<b>System characteristics.</b> Weight, volume, power, maintenance, cost, etc.",
    ]))
    b.append(p(
        "This chapter begins with basic treatments of light and vision. It then proceeds to "
        "discussions of visual capabilities and the display characteristics that must be matched to "
        "them."))

    # ------------------------------------------------------------ 90.2
    b.append(h2("90.2 Fundamentals of Light Measurement"))
    b.append(p(
        "The foundation metric of light is luminous flux, which is the rate at which light energy is "
        "emitted from a source, and is expressed in lumens (lm). Luminous intensity is luminous flux "
        "per unit solid angle, and its unit of measurement is the candela (cd). This is "
        "distinguished from illuminance, or illumination, which is simply luminous flux per unit "
        "area, expressed as lux (lx). Luminance is a measure of the brightness, i.e., the amount of "
        "light, per unit area, either emitted by or reflected from a surface. Units of luminance "
        "measurement are candelas per square meter (cd/m²) or nits. Finally, reflectance is a "
        "unitless ratio of the amount of light striking a surface to the amount of light leaving "
        "it:"))
    b.append(eq(_EQ_EN["90.1"], "90.1"))
    b.append(p("High reflectance can create glare, dramatically reducing visual performance."))

    # ------------------------------------------------------------ 90.3
    b.append(h2("90.3 Fundamentals of Vision"))
    b.append(p(
        "The eye functions very much like a conventional camera. Light enters the eye through a "
        "transparent cornea and is modulated by the pupil, a variable aperture opening controlled by "
        "muscles of the iris. The pupil grows larger in dark surroundings and smaller in bright "
        "surroundings to control the range of light intensity to the eye. Light rays are then "
        "refracted by an adjustable lens and brought into focus on the retina, where neural imaging "
        "begins. The retina contains both cones and rods, two distinctly different types of "
        "photoreceptors. Cones are concentrated near the fovea, or the central 2° of the visual "
        "field, and decrease rapidly with distance from this region. In contrast, rods are "
        "essentially absent in the fovea and increase in density with distance."))
    b.append(p(
        "The eye is sensitive to three characteristics of electromagnetic radiation: (1) brightness "
        "(the intensity of ambient or incident light, measured in lux), (2) hue (the wavelength of "
        "light, measured in nm), and (3) saturation (relative concentration of specific hues in "
        "light, measured as a dimensionless ratio from 0 to 1). Cones are differentially sensitive "
        "to wavelength, i.e., hue, and have greater resolving power than rods because of their "
        "one-to-one mapping onto visual nerves. Cones can be further divided into three types, each "
        "maximally sensitive to a different portion of the visible light spectrum: (1) red (670 nm "
        "peak), (2) green (470 nm peak), and (3) blue (400 nm peak). Rods are more sensitive to "
        "light than cones and have many-to-one connections with the nerves that exit the eye, a "
        "feature that permits neural summation of low light signals. Human ability to discriminate "
        "differences in levels of brightness, saturation, or hue is governed by a psychophysical "
        "function known as Weber's law:"))
    b.append(eq(_EQ_EN["90.2"], "90.2"))
    b.append(p(
        "where Δ<i>I</i> is the difference, or change, in intensity, <i>I</i> is the initial "
        "intensity, and <i>K</i> is the Weber fraction. Values of <i>K</i> have been experimentally "
        "determined for brightness (0.079), saturation (0.019 for red), and hue (≈0.02 to 0.04, "
        "depending on the region of the visible spectrum)."))
    b.append(p(
        "<i>Photopic vision</i> occurs at light levels where both rods and cones are sensitive. The "
        "minimum light intensity required for photopic vision is approximately 2 lx; colors are seen "
        "in this region. As brightness decreases, a transition from photopic to scotopic vision "
        "takes place and color perception drops out gradually, a phenomenon that can impact the "
        "interpretation of color-coded information in poor light. Perception of blues and reds is "
        "lost first, then cyan and yellow-orange, and finally green, i.e., the wavelengths where the "
        "eye is most sensitive. The eye becomes most sensitive to wavelengths of about 550 nm "
        "(green) near the limit of photopic vision. Scotopic vision occurs at low light levels "
        "(2 × 10<sup>−7</sup> lx to 2 lx) and primarily involves the rods; only achromatic shades of "
        "gray are seen. The transition from photopic to scotopic vision occurs slowly, requiring "
        "approximately 30 min for complete adjustment from photopic to scotopic visual sensitivity."))

    # ------------------------------------------------------------ 90.4
    b.append(h2("90.4 Visual Performance"))
    b.append(p(
        "Visual acuity is the ability to discriminate detail. The action of the lens, to change "
        "focus for objects at different distances, is called accommodation. Minimum separable "
        "acuity, the most common measure of discrimination, is determined by the smallest feature "
        "that the eye can detect, and is measured in terms of the reciprocal of the visual angle "
        "subtended at the eye by that feature. Visual angle, in minutes of arc, is calculated as"))
    b.append(eq(_EQ_EN["90.3"], "90.3"))
    b.append(p(
        "where <i>H</i> is the height of the object and <i>D</i> (in the same units) is the distance "
        "from the observer. The ability to distinguish an object from its surroundings is known as "
        "visibility. The term is related to visual acuity, but implicitly combines factors of object "
        "size, contrast (i.e., including differences in hue and saturation), and brightness that all "
        "interact to determine true visual detection performance. On a more functional level, "
        "readability or legibility describe the ability to distinguish meaningful groups of objects "
        "(e.g., words extracted from groups of letters on a display)."))
    b.append(p(
        "Other parameters affecting visual performance include viewing angle and viewing distance. "
        "Viewing angle at the eye is measured from a line through the visual axis to the point being "
        "viewed, and determines where an object will register on the retina. The best image "
        "resolution occurs at the fovea, directly on the line of gaze, and visual acuity degrades "
        "with increasing angle away from this axis. Viewing angle at the display is the angle, in "
        "degrees, between a line normal to the display surface and the user's visual axis. The best "
        "viewing angle is, of course, on the visual axis and normal to the display surface, as "
        "luminance falls off for most displays as the angle from normal increases. Luminance "
        "reduction with viewing angle can be calculated as"))
    b.append(eq(_EQ_EN["90.4"], "90.4"))
    b.append(p(
        "where <i>E</i><sub>m</sub> is the illuminance at the center of the display and θ is the "
        "viewing angle. Note that two viewing angles — at the eye and at the display — have been "
        "defined. Viewing distance is determined primarily by the minimum size requirements (i.e., "
        "visual angle) for objects that the user must see. A conventional reading distance is about "
        "71 cm, although VDTs are frequently read at 46 cm. Most design criteria assume a viewing "
        "distance of between 50 and 70 cm."))
    b.append(p(
        "Visual fatigue is an imprecise term, but one in common use, referring to the annoyance, "
        "irritation, or discomfort associated with visual tasks performed under poor conditions or "
        "for extended periods of time. A common cause of visual fatigue is glare, which can be due "
        "to a combination of high brightness, high reflectance, and specular (mirrorlike) "
        "reflections causing source light to reflect directly into the eye. Minimizing or eliminating "
        "glare is essential for effective display performance, and usually involves a thoughtful "
        "placement of the display, proper positioning of room lights, control of ambient light "
        "(e.g., window shades), or the use of display hoods."))

    # ------------------------------------------------------------ 90.5
    b.append(h2("90.5 Display Performance Considerations"))
    b.append(p(
        "Resolution is a measure of the smallest resolvable object on a display, and is expressed as "
        "display lines per millimeter or centimeter. Although sharpness, and its converse blur, are "
        "normally defined by the subjective reaction of the display user, sharpness has been "
        "formally measured as the ratio of the blurred border zone of letters to their stroke width "
        "[3]. Legibility is related to character quality, or readability, and depends on the "
        "sharpness of characters."))
    b.append(p(
        "Contrast, or contrast ratio, is the measure of the luminance difference between an object "
        "and its background. While different definitions exist in the literature, luminance "
        "contrast as adopted by the International Lighting Commission (CIE) is given as"))
    b.append(eq(_EQ_EN["90.5"], "90.5"))
    b.append(p(
        "Lower luminance displays require greater contrast to achieve the same visibility of "
        "objects. The contrast, or luminance ratio between two surfaces in the central field of "
        "vision (e.g., a display and the desk on which it rests) should be around 3:1, while the "
        "ratio between the central field and surfaces farther away (e.g., around a room) can be as "
        "high as 10:1. Ratios greater than this can induce glare. The simplest methods for contrast "
        "enhancement are the use of hooded shades or displays that can be tilted away from the "
        "offending light. Contrast-enhancing filters, however, can be more effective. All filters "
        "involve reducing the amount of ambient light reflected back to the user, while leaving the "
        "emitted light from the display content as unchanged as possible. Several strategies for "
        "filtering exist, including etching or frosting the display surface to break up and scatter "
        "specular reflections. Neutral density filters increase contrast by reducing the amount of "
        "light passing through them; ambient light must pass through twice before reaching the "
        "user's eye, while display content must only pass through once. Micromesh filters placed on "
        "the display surface limit light penetration so only rays falling perpendicular to the mesh "
        "can penetrate; this stops both specular and diffuse reflections and increases contrast. "
        "Circular polarizers are neutral density filters that polarize incident light, which is then "
        "prevented from returning through the filter. Quarter-wave thin film coatings interfere with "
        "both specular and diffuse reflections."))
    b.append(p(
        "Gray scale refers to the number of luminance levels, or shades of gray, available in a "
        "display. The common definition is a luminance ratio of 1.4 between levels, although the eye "
        "can discriminate changes as small as 1.03 (a Weber's <i>K</i> value of 0.03). The number of "
        "gray shades is useful for evaluating the capability of a display to render pictorial "
        "information or the range of luminance levels that can be used for coding. The highest "
        "luminance level is determined by display capabilities, but the lowest level is determined "
        "by the luminance of the display surface when no signal is present. Bright light incident on "
        "the display can elevate this minimum level and reduce the number of usable gray shades."))
    b.append(p(
        "Flicker is the term for detectable changes in display luminance, and occurs when the "
        "frequency of those changes is below the integrating capability of the eye. The minimum "
        "frequency at which this occurs is the critical flicker fusion frequency, or CFF, which "
        "depends on the luminance level of the image; i.e., displays which do not flicker at high "
        "luminance levels may still flicker at low levels. The CFF is calculated as"))
    b.append(eq(_EQ_EN["90.6"], "90.6"))
    b.append(p(
        "where <i>a</i> = 12.5 for high (photopic) ambient light levels and 1.5 for low (scotopic) "
        "levels, <i>L</i><sub>a</sub> is the average luminance of the image in cd/m², or nits, and "
        "<i>b</i> = 37. This is an empirical formula, and the values for <i>a</i> and <i>b</i> are "
        "only approximate. Because the eye cannot adapt to flicker fast enough to control the light "
        "on the retina, visual irritation usually occurs where flicker is present."))
    b.append(p(
        "Many display parameters are stated in terms of the pixel, or picture element. The pixel is "
        "the smallest addressable element in an electronic display, or the smallest resolvable "
        "information element seen by the user. Refresh rate is the frequency with which display "
        "pixels are reilluminated. Refresh rates below 50 to 80 Hz may induce perceptible flicker. "
        "The update rate is the frequency with which the information content of display is changed."))
    b.append(p(
        "Linearity is the deviation of a straight line from its exact form, expressed as a "
        "percentage of total line length. Pattern distortion is the deviation of any element of a "
        "pattern (e.g., a grid) from its exact location, expressed in dimensions of the total "
        "pattern. While no specific limits are associated with these parameters, interpretation of "
        "measurement data can obviously be affected if nonlinearities are observable on the "
        "display."))
    b.append(p(
        "Several mathematical models have been developed to quantify display image quality as single "
        "&ldquo;figures of merit.&rdquo; These models, while useful, are too involved for treatment "
        "here and the reader is referred to excellent summaries in the literature [1] for further "
        "information."))

    # ------------------------------------------------------------ 90.6
    b.append(h2("90.6 Display Content Considerations"))
    b.append(p(
        "Configurable software packages for scientific measurement (e.g., LabView™) allow great "
        "flexibility in the design of display formats. Human factors principles for display content, "
        "therefore, are as important to effective measurement as the electronic characteristics of "
        "the display itself. The following principles are an introduction to the kinds of issues "
        "that must be considered when designing display content. The interested reader is referred "
        "to Helander (1987) and Grandjean [3] for information on human factors and design guidelines "
        "beyond those presented here."))

    b.append(h3("Alphanumeric Displays"))
    b.append(p(
        "The size of a letter is its pitch. A general recommendation is that characters should "
        "subtend a minimum of about 12 min of arc at common reading distances. Alphanumeric displays "
        "are usually constructed of pixel arrays or segmented bars (Figure 90.1). A 5 × 7 pixel "
        "array is considered the minimum necessary to represent the ASCII character set. More pixels "
        "can increase legibility, but at higher cost for the control electronics. The seven-segment "
        "bar matrix is also a common design and has good performance, but up to 16-segment arrays "
        "are available for better appearance."))
    b.append(fig(1, "en"))
    b.append(p(
        "Stroke width is the ratio of the thickness of the stroke to the height of the letter. "
        "Recommendations for legibility are 1:6 to 8 or 1:8 to 10 [2]. As illumination is reduced, "
        "thick letters are easier to read than thin ones. With low illumination and low contrast, "
        "letters should be boldface type with low stroke width–height ratios (e.g., 1:5)."))

    b.append(h3("Quantitative and Status Displays"))
    b.append(p(
        "While numeric readout displays are easy to implement in software, analog pointer displays "
        "show an advantage when it is important to observe the direction or rate of change of the "
        "values presented [4]. If the measurement application involves &ldquo;more or less&rdquo; or "
        "&ldquo;up or down&rdquo; interpretations, a straight-line or thermometer scale is preferred "
        "because it shows the measurement in relation to zero. Moving pointers are better able to "
        "convey minor changes in readings than fixed pointers or numeric readouts. Scale markings "
        "should reflect the length of the smallest unit to be read. It is desirable to have a marker "
        "for each unit, so that no interpolation is required."))
    b.append(p(
        "Check reading indicators are used to determine whether a condition is &ldquo;normal.&rdquo; "
        "The normal criterion point, therefore, should be clearly coded. If several indicators are "
        "grouped together, they should be arranged so that the deviant reading stands out (e.g., by "
        "indicating a different column height or dial angle, etc.)."))
    b.append(p(
        "Color is an excellent method for organizing information on a display and for locating "
        "objects rapidly. Although display users can distinguish between many different colors, they "
        "usually cannot remember more than seven to ten of them, so the number should be limited if "
        "color is going to be used as a coding dimension."))

    b.append(h3("Summary"))
    b.append(p(
        "The next sections address different display technologies in light of the principles "
        "discussed here. While display guidelines are available for essentially any parameter, it is "
        "important to remember that visual perception is an integrative process. No single guideline "
        "functions alone, and display quality is usually a product of interacting needs and "
        "trade-offs."))

    # ------------------------------------------------------------ 90.7
    b.append(h2("90.7 Cathode Ray Tube Displays"))
    b.append(p(
        "The cathode ray tube (CRT, see Chapter 91) is by far the most common display technology in "
        "use today, and its widespread use in televisions and computer monitors should guarantee its "
        "continued presence throughout the foreseeable future. Advantages of CRT-based displays "
        "include (1) versatility (the same CRT can be used for alphanumerics, pictures, or graphics), "
        "(2) high-resolution capability and high luminous efficiency, extremely fast dynamic "
        "response (which can be important for rapidly changing signals), (3) extensive commercial "
        "availability (e.g., 2.5 to 64 cm, diagonally), (4) high reliability, (5) long life, and (6) "
        "relatively low cost. CRT displays can function well in high ambient illumination if "
        "filtering is used. Potential disadvantages of CRT displays are bulk (the depth of "
        "conventional CRT tubes can match or exceed their diagonal dimension, although flat CRTs are "
        "available), and vulnerability to ambient reflections and high illumination. Light falling on "
        "the smooth display surface can produce a veiling illuminance that washes out screen "
        "contrast and reduces the number of colors that can be perceived."))

    b.append(h3("CRT Performance"))
    b.append(p(
        "Many characteristics of CRT displays depend on the type of phosphor selected for the design. "
        "Phosphor materials vary widely in their luminous efficiency, their color, and their decay "
        "time. Decay time interacts with display refresh rate; a phosphor with a short decay time "
        "will require a higher refresh rate to avoid observable flicker effects. Selecting a CRT "
        "with a high phosphor decay time will also result in selecting a tube with a high average "
        "luminance. Resolution depends on the spot size of the energized phosphor (which is "
        "effectively the thickness of the raster line). Spot size will also depend on the "
        "acceleration voltage and beam current of the cathode gun, so manufacturer's data must be "
        "noted for the voltage and current where the measurements were recorded, and compared with "
        "expected operating conditions. CRT resolution is measured in two ways. Television lines are "
        "the number of the most closely spaced, discernible lines that can be distinguished on an "
        "EIA (Electronic Industries Association) test chart. Shrinking raster lines involve a process "
        "of reducing the spacing between lines of a test pattern until no lines can be seen. This "
        "point is then expressed as the number of lines per centimeter, and is a better metric for "
        "measurement display applications. Increasing numbers of scan lines improve symbol legibility "
        "and image quality. Most conventional CRT monitors have 525 scan lines, but up to 5000-line "
        "systems are available [5]. The primary method for achieving color CRT displays is the use of "
        "single or multiple electron beams to energize phosphors for three primary colors — red, "
        "blue, and green. A complete range of colors is obtained by selectively energizing "
        "appropriate combinations of these three basic phosphors. Beam efficiency is reduced in this "
        "process, which means that color CRT displays are not as bright as monochrome CRT systems. "
        "Contrast ratio is diminished by high ambient light levels, and it is often necessary to "
        "compromise between light requirements for work tasks and light levels for optimum CRT "
        "visibility. In low ambient lighting conditions, a CRT contrast ratio of 10:1 is usually "
        "attainable. A ratio of 25:1 can be achieved with contrast-enhancing filters, but at the "
        "expense of brightness."))

    b.append(h3("Types of CRT Displays"))
    b.append(p(
        "In addition to the conventional, raster-scanned CRTs used for computer monitors and "
        "workstations, two variants of CRT technology should be mentioned, the direct-view storage "
        "CRT and the flat CRT. Direct-view storage CRTs have been designed to get around the need to "
        "refresh phosphors constantly. Direct-view systems usually add an additional, electrically "
        "charged layer — the storage element — somewhere behind the phosphor layer and an additional "
        "electron gun to maintain this charge. Displayed information is retained until it is actively "
        "erased. Flat CRTs have been developed to answer the need for CRT performance in a smaller "
        "physical package. The basic design technique places the electron gun at right angles to the "
        "screen and, through additional focusing circuitry or a slightly angled phosphor screen, "
        "writes the raster pattern at a high angle. Additional detail on these and other CRT designs "
        "can be found in Sherr [1]."))

    # ------------------------------------------------------------ 90.8
    b.append(h2("90.8 Liquid Crystal Displays"))
    b.append(p(
        "Liquid crystal displays (LCDs, see Chapter 92) belong to the class of nonemissive "
        "technologies, i.e., displays that do not generate light of their own but control the "
        "transmission or reflection of an external light source. LCDs alter the optical path of light "
        "when an electric field is placed across the liquid crystal (LC) material."))
    b.append(p(
        "The principal advantages of LCDs include (1) very low power consumption (important for "
        "battery-operated and portable systems such as calculators), (2) a flat display package, (3) "
        "low cost of the basic materials, and (4) excellent contrast in high ambient illumination. "
        "Some LCDs, however, have slow dynamic response (i.e., for switching display elements on and "
        "off); 100 to 500 ms rise times, for example, are visually noticeable and such systems may be "
        "unacceptable for measurement applications. Low luminance is another drawback, and can make "
        "the display difficult to read in low-light conditions without an external light source. In "
        "addition, viewing angle is limited by inherent LC characteristics, and is usually less than "
        "45° without special designs. Many LCD features, such as switching thresholds and response "
        "times, are temperature dependent."))

    b.append(h3("LCD Performance"))
    b.append(p(
        "A full range of resolution capabilities is available, from simple alphanumeric displays to "
        "systems with 63 million pixels and resolutions of 47 lines/cm [6]. LCDs are primarily used "
        "in small display applications (e.g., calculators, watches, etc.), although 53 cm diagonal, "
        "full-color video-capable displays have been developed [7]."))
    b.append(p(
        "Contrast in polarized systems is determined by the extinction ratio of the polarizer, i.e., "
        "the ratio of light transmitted in the parallel polarizing orientation to light transmitted "
        "in the cross-polarizing orientation. Polarizers with good extinction ratios, however, also "
        "suffer high loss of light in the transmitting orientation, so maximum brightness is traded "
        "for contrast. Contrast ratios of up to 50:1 [6] have been achieved, although 20:1 is more "
        "common."))
    b.append(p(
        "Color displays can be achieved by placing a color mosaic over the LCD and switching the "
        "cells behind the proper combinations of mosaic holes into their transmission states. This "
        "method reduces resolution and brightness, however, as the available pixels must be assigned "
        "to each of the three primary colors. The use of thin-film transistors (TFT) as a switching "
        "technology for LCDs is the latest approach to generating large, high-resolution displays and "
        "is the subject of extensive engineering research [8]."))

    # ------------------------------------------------------------ 90.9
    b.append(h2("90.9 Plasma Displays"))
    b.append(p(
        "The simplicity and durability of plasma displays (see Chapter 93) makes this technology an "
        "attractive candidate for diverse measurement needs, especially where harsh environments are "
        "expected. In addition, the switching characteristics of plasma gases have not yet been fully "
        "exploited, and this technology offers excellent potential for future engineering "
        "improvements. Plasma methods are used extensively for alphanumeric displays in portable, "
        "laptop, and handheld computers, and for the display of video imagery."))
    b.append(p(
        "Advantages of plasma displays include enhanced memory capability, brightness, and luminous "
        "efficiency. It is also possible to retain pixels in the on state without continuous refresh "
        "signals, which means that increased brightness can be obtained for the same power and "
        "driving circuitry. This advantage also allows for excellent contrast ratios in high ambient "
        "illumination."))
    b.append(p(
        "Plasma displays also exhibit long display life and ruggedness. It is not unusual for the "
        "display to outlast the life of the product in which it is installed, and the relatively "
        "simple panel construction can tolerate high shock and vibration environments, or extremes of "
        "temperature. Some disadvantages of plasma displays include high cost (relative to CRTs) and "
        "high power requirements (relative to LCDs). Other technologies can compete effectively with "
        "plasma devices for small alphanumeric displays in benign conditions."))

    b.append(h3("Plasma Display Performance"))
    b.append(p(
        "Commercial plasma displays are available with resolutions of 40 lines/cm, and systems with "
        "almost 50 lines/cm are under development. Systems of 2 million pixels have been constructed "
        "[9]. Gray scale is achieved with dc displays by adjusting the discharge current in each "
        "cell. Displays using ac voltage can trade resolution for gray scale with spatial modulation "
        "methods, i.e., by controlling the number and location of activated pixels, rather than the "
        "level of pixel illumination. While plasma displays have good gray scale, their brightness is "
        "not yet equivalent to that of CRTs. Plasma displays show the color of the ionized gas, "
        "usually orange (i.e., where neon is used), although different gas mixtures or phosphors have "
        "been successfully used to expand the range of colors. The hybrid ac-dc display was designed "
        "to combine the memory capability of ac systems with the efficient matrix circuitry of dc "
        "devices [10]. The display uses both types of current to generate gas discharge; the dc "
        "component controls the pixel addressing, while the ac component controls the memory states "
        "of the cells. The hybrid plasma–CRT display attempts to use the gas discharge effect of the "
        "plasma panel as a matrix-addressable source of electrons for the CRT. The result is a "
        "full-color system with high brightness and good luminous efficiency."))

    # ------------------------------------------------------------ 90.10
    b.append(h2("90.10 Electroluminescent Displays"))
    b.append(p(
        "With the exception of light-emitting diodes (LEDs, see Chapter 95), electroluminescent (EL, "
        "see Chapter 94) technologies are not as prominent in the commercial arena as other types of "
        "display systems. EL materials are complex (i.e., driven and controlled by processes related "
        "to solid-state semiconductor physics) and are more difficult to work with than other display "
        "materials. Nevertheless, they offer great potential for high brightness and low cost that "
        "deserves consideration, especially as new designs become available. Matrix addressing is "
        "used for control of information display applications. EL materials are applied in two forms "
        "— powders (PEL) and thin films (TFEL) — and are controlled by both ac and dc voltages, "
        "generating four basic design approaches. Some advantages of EL displays are (1) high "
        "luminous efficiency (except ac powder designs), (2) readability in sunlight, (3) color "
        "capability, (4) compact, flat panel designs, and (5) significant potential for low-cost "
        "manufacture. A disadvantage of EL displays is that ac powder (ACPEL) systems have low "
        "luminance and contrast ratio. In addition, phosphors in powder designs scatter and reflect "
        "ambient light, reducing their contrast."))

    b.append(h3("EL Display Performance"))
    b.append(p(
        "Contrast ratios of 50 to 150:1 have been demonstrated with monochrome thin-film (ACTFEL) "
        "systems, while 15 to 20:1 have been achieved with dc designs. ACTFEL designs also show "
        "excellent brightness, with demonstrated luminance levels of over 157 cd/m² (monochrome) and "
        "26 cd/m² (color). DCPEL designs, representing newer technologies, have achieved over "
        "100 cd/m² with monochrome designs, but may soon meet or exceed ac-based values. Resolution "
        "of EL displays is limited by the duty factor of matrix addressing; a finite amount of time "
        "is needed to energize each row, and a minimum luminance level is needed for adequate display "
        "performance, so the remaining variable becomes the number of addressable lines. A "
        "demonstrated ACTFEL display with 640 × 400 elements, with six colors and a resolution of "
        "27 lines/cm, is typical of this technology."))

    # ------------------------------------------------------------ 90.11
    b.append(h2("90.11 Light-Emitting Diode Displays"))
    b.append(p(
        "Light-emitting diode (LED) displays (see Chapter 95) involve single-crystal phosphor "
        "materials, which distinguishes them from the polycrystal EL materials discussed in the "
        "previous section. The basic physics behind their operation is, however, quite similar. LED "
        "displays are highly versatile and well suited to a variety of measurement applications. "
        "Advantages of LED displays include high reliability and graceful degradation; individual LED "
        "elements can fail without affecting overall display performance. LEDs are rugged, for "
        "operation in harsh environments, and they are more tolerant of temperature extremes than "
        "other technologies. LEDs demonstrate better viewing angles than LCDs, and excellent "
        "brightness for visibility in sunlight. Unfortunately, LED displays also have high power "
        "consumption when packaged in large, flat panel displays, and the cost is high for the complex "
        "assembly. Optical cross talk between array elements can occur if transparent substrates are "
        "used. LEDs are the most-restricted display in terms of color range (e.g., no blue device is "
        "commercially available)."))

    b.append(h3("LED Display Performance"))
    b.append(p(
        "LED devices have excellent brightness, but because display brightness is also a function of "
        "the filters or magnification lenses used over the LED elements, device luminance is not, by "
        "itself, a reliable measure of overall system performance. LED displays also show very good "
        "luminance contrast. Chrominance contrast, however — the color difference between the LED and "
        "its background — is a factor in evaluating LED performance that is not found in other "
        "technologies. Chrominance contrast is significant because of the high saturation of most LED "
        "phosphors. It is affected by display filters, and can have significantly more influence on "
        "display performance than luminance contrast."))
    b.append(p(
        "LED displays with resolutions of 20 to 25 lines/cm have been constructed. Flat panel "
        "displays of 38,400 discrete elements have also been demonstrated with luminance levels of "
        "around 137 cd/m² (increasing to 240 cd/m² with reduced resolution), and at least one "
        "aircraft display with 49,000 elements has been built. CRT-equivalent displays with 640 × 400 "
        "elements have also been realized with engineering development models."))

    # ------------------------------------------------------------ glossary
    b.append(h2("Defining Terms"))
    b.append(_glossary(_GLOSS_EN))

    b.append(h2("References"))
    b.append(refs(_REFS))

    b.append(h2("Further Information"))
    b.append('<ul class="ref-list">%s</ul>' % "".join("<li>%s</li>" % i for i in _FURTHER))
    return "".join(b)


# ================================================================ PAGE
def build(lang):
    vi = lang == "vi"
    switch = ("%s%s/" % (BASE_EN, CSLUG)) if vi else ("%s%s/" % (BASE_VI, CSLUG))
    title = ("Chương 90 — %s · Sổ tay Đo lường, Thiết bị đo và Cảm biến" % TITLE_VI if vi
             else "Chapter 90 — %s · Measurement, Instrumentation and Sensors Handbook"
                  % TITLE_EN)
    desc = ("Bản dịch tiếng Việt Chương 90 “Yếu tố con người trong hiển thị” của Steven A. Murray "
            "và Barrett S. Caldwell — cơ sở đo ánh sáng và thị giác, năng lực thị giác, các yếu tố "
            "hiệu năng và nội dung hiển thị, rồi năm công nghệ hiển thị (CRT, LCD, plasma, điện "
            "phát quang, LED) cùng định nghĩa thuật ngữ, với 1 hình, 6 công thức và 10 tài liệu "
            "tham khảo." if vi
            else
            "Companion to Chapter 90 of the CRC Measurement Handbook — light measurement and vision, "
            "visual performance, display performance and display content, then five display "
            "technologies (CRT, LCD, plasma, EL and LED) with a glossary, 1 figure, 6 equations and "
            "10 references.")
    crumb = ('<a href="/vi/books/">Sách</a> · <a href="%s">Sổ tay Đo lường, Thiết bị đo và Cảm '
             'biến</a> · Chương 90' % BASE_VI if vi else
             '<a href="/books/">Books</a> · <a href="%s">Measurement, Instrumentation and Sensors '
             'Handbook</a> · Chapter 90' % BASE_EN)
    meta = ("Chương 90 · theo Ch90.pdf (CRC Press, 1999) · 1 hình, 6 công thức" if vi
            else "Chapter 90 · 1 figure, 6 equations")
    body = ('<main><article class="intranet-content reader"><div class="reader-hero">'
            '<div class="breadcrumb">%s</div><h1>%s</h1><p class="byline">%s</p>'
            '<div class="meta-line">%s</div></div><div class="prose">%s</div>%s</article></main>'
            % (crumb, TITLE_VI if vi else TITLE_EN, BYLINE if vi else BYLINE_EN, meta,
               body_vi() if vi else body_en(), chapter_nav(lang, 90)))
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
