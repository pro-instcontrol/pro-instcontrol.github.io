# -*- coding: utf-8 -*-
"""Handbook Chapter 31 — Surface Tension Measurement
(David B. Thiessen and Kin F. Man — California Institute of Technology)

Three sections, 14 source pages, 5 figures, 2 tables and 13 numbered equations.

Run:  python build/reader_hb_ch31.py
"""
import os

import hb31fig as F
from reader_handbook import SLUG, head, header, footer
from chapter_nav import nav as chapter_nav

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSLUG = "ch31-surface-tension-measurement"
TITLE_EN = "Surface Tension Measurement"
TITLE_VI = "Đo sức căng bề mặt"
BYLINE = ("David B. Thiessen (California Institute of Technology) · "
          "Kin F. Man (California Institute of Technology)")
BASE_EN = "/books/read/%s/" % SLUG
BASE_VI = "/vi/books/read/%s/" % SLUG
PREV_EN = "ch30-viscosity-measurement"
PREV_VI = "ch30-viscosity-measurement"
PREV_T_EN = "Viscosity Measurement"
PREV_T_VI = "Đo độ nhớt"


def fig(num, key, lang="vi"):
    svg, cap_vi, cap_en, aria_vi, aria_en = key
    if lang == "vi":
        cap = cap_vi
    else:
        cap = cap_en
        # The <svg> tag is built once, in hb31fig, with a Vietnamese aria-label
        # baked in by hbfig.svg(). Swap it for the English one, otherwise a
        # screen reader on this page announces Vietnamese.
        k = svg.find('aria-label="')
        if k >= 0:
            a = k + len('aria-label="')
            b = svg.find('"', a)
            svg = svg[:a] + (aria_en or aria_vi) + svg[b:]
    return ('<figure class="figure" id="fig-31-%d">%s<figcaption class="figcap">%s</figcaption></figure>'
            % (num, svg, cap))


def p(t):
    return "<p>%s</p>" % t


def h2(t, en=""):
    if en == t:
        en = ""
    sid = ""
    if t.startswith("31."):
        head_ = t[3:].split(" ", 1)[0]
        if head_.isdigit():
            sid = ' id="s31-%s"' % head_
    return '<h2%s>%s%s</h2>' % (sid, t, (' <span class="en">%s</span>' % en) if en else "")


def h3(t, en="", anchor=None):
    if en == t:
        en = ""
    a = ' id="%s"' % anchor if anchor else ""
    return '<h3%s>%s%s</h3>' % (a, t, (' <span class="en">%s</span>' % en) if en else "")


def eq(body, num=""):
    if not num:
        return '<div class="eq">%s</div>' % body
    return '<div class="eq"><span class="n">(%s)</span>%s</div>' % (num, body)


def note(t):
    return '<div class="note">%s</div>' % t


def wl(items):
    return ('<p style="font-size:.92rem;color:#333;line-height:1.8;margin:-.3rem 0 1.2rem">'
            + "<br>".join(items) + "</p>")


def ul(items):
    return ('<ul style="margin:-.2rem 0 1.3rem">%s</ul>'
            % "".join("<li>%s</li>" % i for i in items))


def table(hd, rows, cap, cls="tbl", widths=None):
    body = "".join("<tr>%s</tr>" % "".join("<td>%s</td>" % c for c in r) for r in rows)
    ths = "".join('<th%s>%s</th>' % ((' style="width:%s"' % widths[i]) if widths else "", h)
                  for i, h in enumerate(hd))
    return ('<div class="table-wrap"><table class="%s"><thead><tr>%s</tr></thead><tbody>%s</tbody></table></div>'
            '<p style="font-size:.84rem;color:#888;font-style:italic">%s</p>'
            % (cls, ths, body, cap))


def defs(items):
    """Defining-terms block, rendered as a two-column table so it inherits the
    reader's .tbl styling — there is no .deflist rule in library.css."""
    rows = "".join('<tr><th scope="row" style="text-align:left;width:30%%">%s</th><td>%s</td></tr>'
                   % (k, v) for k, v in items)
    return ('<div class="table-wrap"><table class="tbl"><tbody>%s</tbody></table></div>' % rows)


# ================================================================ table data

def _t311(lang):
    """Table 31.1 — nine instrument types. Prices are the 1999 figures the
    source prints; they are left as printed rather than updated."""
    vi = lang == "vi"
    hd = (["Phương pháp", "Loại thiết bị", "Hãng / tên sản phẩm", "Giá xấp xỉ (khoảng)"]
          if vi else
          ["Method", "Instrument type", "Manufacturer / product name", "Approximate price (range)"])
    rows = [
        ("Mao dẫn dâng" if vi else "Capillary rise",
         "Thủ công" if vi else "Manual",
         "Fisher", "$79"),
        ("Bản Wilhelmy / vòng du Noüy" if vi else "Wilhelmy plate / du Noüy ring",
         "Thủ công, cân cơ" if vi else "Manual, mechanical balance",
         "CSC, Fisher, Kahl", "$2000–$4000"),
        ("Bản Wilhelmy / vòng du Noüy" if vi else "Wilhelmy plate / du Noüy ring",
         "Thủ công, cân điện tử" if vi else "Manual, electrobalance",
         "KSV, Lauda, NIMA", "$4000–$11,000"),
        ("Bản Wilhelmy / vòng du Noüy" if vi else "Wilhelmy plate / du Noüy ring",
         "Tự động, cân điện tử" if vi else "Automatic, electrobalance",
         "Cahn, Krüss, KSV, NIMA", "$9000–$24,000"),
        ("Áp suất bọt cực đại" if vi else "Maximum bubble pressure",
         "Tự động" if vi else "Automatic",
         "Krüss, Lauda, Sensa Dyne", "$5000–$23,000"),
        ("Giọt treo / giọt nằm" if vi else "Pendant / sessile drop",
         "Thủ công" if vi else "Manual",
         "Krüss, Rame-Hart", "$7000–$10,000"),
        ("Giọt treo / giọt nằm" if vi else "Pendant / sessile drop",
         "Tự động" if vi else "Automatic",
         "ADSA, AST, FTA, Krüss, Rame-Hart, Temco", "$10,000–$100,000"),
        ("Trọng lượng / thể tích giọt" if vi else "Drop weight / volume",
         "Tự động" if vi else "Automatic",
         "Krüss, Lauda", "$16,000–$21,000"),
        ("Giọt quay" if vi else "Spinning drop",
         "Thủ công" if vi else "Manual",
         "Krüss", "$20,100"),
    ]
    cap = ("Bảng 31.1 · Các thiết bị đo sức căng bề mặt bán trên thị trường. Khoảng giá phản ánh "
           "mức độ tự động hoá, số phụ kiện kèm theo và chênh lệch giữa các hãng."
           if vi else
           "Table 31.1 · Commercially available instruments. Price ranges reflect differences in "
           "degree of automation, the number of accessories included, or variation in price "
           "between manufacturers.")
    return table(hd, rows, cap, widths=["22%", "22%", "34%", "22%"])


def _t312(lang):
    """Table 31.2 — fourteen suppliers, laid out two per row exactly as the
    source prints it. There is no header row, so this is built by hand rather
    than through table()."""
    vi = lang == "vi"
    entries = [
        ("AST Products", ["9 Linnell Circle", "Billerica, MA 01821-3902", "Tel: (508) 663-7652"]),
        ("Fisher Scientific", ["711 Forbes Ave.", "Pittsburgh, PA 15219-4785", "Tel: (800) 766-7000"]),
        ("Applied Surface Thermodynamics Research Associates (ASTRA)",
         ["P.O. Box 1166", "(distributor of ADSA instrumentation)",
          "15 Brendan Rd.", "Toronto, Ontario, Canada, M4G 2W9", "Tel: (416) 978-3601"]),
        ("Kahl Scientific Instrument Corp.",
         ["P.O. Box 1166", "El Cajon, CA 92022-1166", "Tel: (619) 444-2158"]),
        ("Brinkmann Instruments, Inc.",
         ["(distributor for Lauda tensiometers)", "One Catiaque Road", "P.O. Box 1019",
          "Westbury, NY 11590-0207", "Tel: (800) 645-3050"]),
        ("Krüss U.S.A.", ["9305-B Monroe Road", "Charlotte, NC 28270-1488", "Tel: (704) 847-8933"]),
        ("Cahn Instruments", ["5225 Verona Rd., Bldg. 1", "Madison, WI 53711", "Tel: (800) 244-6305"]),
        ("KSV Instruments U.S.A.", ["P.O. Box 192", "Monroe, CT 06468", "Tel: (800) 280-6216"]),
        ("CSC Scientific Company, Inc.", ["8315 Lee Highway", "Fairfax, VA 22031", "Tel: (800) 458-2558"]),
        ("Rame-Hart, Inc.", ["8 Morris Ave.", "Mountain Lakes, NJ 07046", "Tel: (201) 335-0560"]),
        ("CTC Technologies, Inc.",
         ["(distributor for NIMA tensiometers)", "7925-A North Oracle Road, Suite 364",
          "Tucson, AZ 85704-6356", "Tel: (800) 282-8325"]),
        ("Sensa Dyne Instrument Div.",
         ["Chem-Dyne Research Corp.", "P.O. Box 30430", "Mesa, AZ 85275-0430", "Tel: (602) 924-1744"]),
        ("First Ten Angstroms (FTA)",
         ["465 Dinwiddie Street", "Portsmouth, VA 23704", "Tel: (800) 949-4110"]),
        ("Temco, Inc.", ["4616 North Mingo", "Tulsa, OK 74117-5901", "Tel: (918) 834-2337"]),
    ]

    def cell(e):
        name, lines = e
        body = "<br>".join(lines)
        return ('<b>%s</b><br><span style="font-size:.86rem;color:#444">%s</span>' % (name, body))

    rows = []
    for i in range(0, len(entries), 2):
        pair = entries[i:i + 2]
        left = cell(pair[0])
        right = cell(pair[1]) if len(pair) > 1 else ""
        rows.append("<tr><td>%s</td><td>%s</td></tr>" % (left, right))
    cap = ("Bảng 31.2 · Các hãng sản xuất và nhà cung cấp thiết bị đo sức căng bề mặt."
           if vi else
           "Table 31.2 · Manufacturers and suppliers of instruments for surface tension measurement.")
    return ('<div class="table-wrap"><table class="tbl"><tbody>%s</tbody></table></div>'
            '<p style="font-size:.84rem;color:#888;font-style:italic">%s</p>'
            % ("".join(rows), cap))


# ================================================================ references

def _refs31(lang):
    """The source prints 35 references. The numbers live inside the strings, so
    they are rendered with wl() — passing them to ol() would number them twice."""
    refs = [
        "A. W. Adamson, <i>Physical Chemistry of Surfaces</i>, 5th ed., New York: John Wiley &amp; Sons, 1990.",
        "A. E. Alexander and J. B. Hayter, Determination of surface and interfacial tension, in "
        "A. Weissberger and B. W. Rossiter (eds.), <i>Physical Methods of Chemistry, Part V</i>, "
        "4th ed., New York: John Wiley &amp; Sons, 1971.",
        "A. Couper, Surface tension and its measurement, in B. W. Rossiter and R. C. Baetzold (eds.), "
        "<i>Physical Methods of Chemistry</i>, Vol. 9A, 2nd ed., New York: John Wiley &amp; Sons, 1993.",
        "J. F. Padday, Surface tension. II. The measurement of surface tension, in E. Matijevic (ed.), "
        "<i>Surface and Colloid Science</i>, Vol. 1, New York: John Wiley &amp; Sons, 1969.",
        "S. Sugden, The determination of surface tension from the maximum pressure in bubbles. Part II, "
        "<i>J. Chem. Soc.</i>, 125, 27–31, 1924.",
        "ASTM Standard D3825-90, Standard test method for dynamic surface tension by the fast-bubble "
        "technique, <i>1996 Annual Book of ASTM Standards</i>, Vol. 05.02, West Conshohocken, PA: "
        "ASTM, 1996, 575–579.",
        "D. S. Ambwani and T. Fort, Jr., Pendant drop technique for measuring liquid boundary "
        "tensions, in R. J. Good and R. R. Stromberg (eds.), <i>Surface and Colloid Science</i>, "
        "Vol. 11, New York: Plenum Press, 1979.",
        "Y. Rotenberg, L. Boruvka, and A. W. Neumann, Determination of surface tension and contact "
        "angle from the shapes of axisymmetric fluid interfaces, <i>J. Colloid Interface Sci.</i>, "
        "93, 169–183, 1983.",
        "P. Cheng, D. Li, L. Boruvka, Y. Rotenberg, and A. W. Neumann, Automation of axisymmetric drop "
        "shape analysis for measurements of interfacial tensions and contact angles, "
        "<i>Colloids Surf.</i>, 43, 151–167, 1990.",
        "D. B. Thiessen, D. J. Chione, C. B. McCreary, and W. B. Krantz, Robust digital image analysis "
        "of pendant drop shapes, <i>J. Colloid Interface Sci.</i>, 177, 658–665, 1996.",
        "S. Lin, K. McKeigue, and C. Maldarelli, Diffusion-controlled surfactant adsorption studied by "
        "pendant drop digitization, <i>AIChE J.</i>, 36, 1785–1795, 1990.",
        "D. Y. Kwok, D. Vollhardt, R. Miller, D. Li, and A. W. Neumann, Axisymmetric drop shape "
        "analysis as a film balance, <i>Colloids Surf., A</i>, 88, 51–58, 1994.",
        "W. M. Schoel, S. Schurch, and J. Goerke, The captive bubble method for the evaluation of "
        "pulmonary surfactant: surface tension, area, and volume calculations, "
        "<i>Biochim. Biophys. Acta</i>, 1200, 281–290, 1994.",
        "S. Lahooti, O. I. Del Rio, P. Cheng, and A. W. Neumann, Axisymmetric drop shape analysis "
        "(ADSA), in A. W. Neumann and J. K. Spelt (eds.), <i>Applied Surface Thermodynamics</i>, "
        "New York: Marcel Dekker, 1996.",
        "M. L. Alexander and M. J. Matteson, The automation of an interfacial tensiometer, "
        "<i>Colloids Surf.</i>, 27, 201–217, 1987.",
        "J. C. Slattery and J. Chen, Alternative solution for spinning drop interfacial tensiometer, "
        "<i>J. Colloid Interface Sci.</i>, 64, 371–373, 1978.",
        "D. Y. Kwok, M. A. Cabrerizo-Vilchez, Y. Gomez, S. S. Susnar, O. Del Rio, D. Vollhardt, "
        "R. Miller, and A. W. Neumann, Axisymmetric drop shape analysis as a method to study dynamic "
        "interfacial tensions, in V. Pillai and D. O. Shah (eds.), <i>Dynamic Properties of Interfaces "
        "and Association Structures</i>, Champaign, IL: AOCS Press, 1996.",
        "W. D. E. Thomas and L. Potter, Solution/air interfaces. I. An oscillating jet relative method "
        "for determining dynamic surface tensions, <i>J. Colloid Interface Sci.</i>, 50, 397–412, 1975.",
        "V. B. Fainerman and R. Miller, Dynamic surface tension measurements in the sub-millisecond "
        "range, <i>J. Colloid Interface Sci.</i>, 175, 118–121, 1995.",
        "G. L. Gaines Jr., <i>Insoluble Monolayers at Liquid-Gas Interfaces</i>, New York: John Wiley "
        "&amp; Sons, 1966, 44.",
        "R. Miller, R. Sedev, K.-H. Schano, C. Ng, and A. W. Neumann, Relaxation of adsorption layers "
        "at solution/air interfaces using axisymmetric drop-shape analysis, <i>Colloids Surf.</i>, "
        "69, 209–216, 1993.",
        "D. O. Johnson and K. J. Stebe, Oscillating bubble tensiometry: a method for measuring the "
        "surfactant adsorptive-desorptive kinetics and the surface dilatational viscosity, "
        "<i>J. Colloid Interface Sci.</i>, 168, 21–31, 1994.",
        "D. O. Johnson and K. J. Stebe, Experimental confirmation of the oscillating bubble technique "
        "with comparison to the pendant bubble method: the adsorption dynamics of 1-decanol, "
        "<i>J. Colloid Interface Sci.</i>, 182, 526–538, 1996.",
        "D. A. Edwards, H. Brenner, and D. T. Wasan, <i>Interfacial Transport Processes and "
        "Rheology</i>, Boston: Butterworth-Heinemann, 1991.",
        "C. Garcia-Cordovilla, E. Louis, and A. Pamies, The surface tension of liquid pure aluminium "
        "and aluminium-magnesium alloy, <i>J. Mater. Sci.</i>, 21, 2787–2792, 1986.",
        "B. C. Allen, The surface tension of liquid transition metals at their melting points, "
        "<i>Trans. Metall. Soc. AIME</i>, 227, 1175–1183, 1963.",
        "D. B. Thiessen and K. F. Man, A quasi-containerless pendant drop method for surface tension "
        "measurements on molten metals and alloys, <i>Int. J. Thermophys.</i>, 16, 245–255, 1995.",
        "S. C. Hardy, The surface tension of liquid silicon, <i>J. Cryst. Growth</i>, 69, 456–460, 1984.",
        "V. Schoettle and H. Y. Jennings, Jr., High-pressure high-temperature visual cell for "
        "interfacial tension measurement, <i>Rev. Sci. Instrum.</i>, 39, 386–388, 1968.",
        "R. Simon and R. L. Schmidt, A system for determining fluid properties up to 136 MPa and "
        "473 K, <i>Fluid Phase Equilib.</i>, 10, 233–248, 1983.",
        "K. Hool and B. Schuchardt, A new instrument for the measurement of liquid-liquid interfacial "
        "tension and the dynamics of interfacial tension reduction, <i>Meas. Sci. Technol.</i>, "
        "3, 451–457, 1992.",
        "A. Passerone, L. Liggieri, N. Rando, F. Ravera, and E. Ricci, A new experimental method for "
        "the measurement of the interfacial tension between immiscible fluids at zero Bond number, "
        "<i>J. Colloid Interface Sci.</i>, 146, 152–162, 1991.",
        "G. Pétré and G. Wozniak, Measurement of the variation of interfacial tension with temperature "
        "between immiscible liquids of equal density, <i>Acta Astronaut.</i>, 13, 669–672, 1986.",
        "D. Chatenay, D. Langevin, J. Meunier, D. Bourbon, P. Lalanne, and A. M. Bellocq, Measurement "
        "of low interfacial tension, comparison between a light scattering technique and the spinning "
        "drop technique, <i>J. Dispersion Sci. Technol.</i>, 3, 245–260, 1982.",
        "D. Y. Kwok, P. Chiefalo, B. Khorshiddoust, S. Lahooti, M. A. Cabrerizo-Vilchez, O. Del Rio, "
        "and A. W. Neumann, Determination of ultralow interfacial tension by axisymmetric drop shape "
        "analysis, in R. Sharma (ed.), <i>Surfactant Adsorption and Surface Solubilization</i> "
        "(ACS Symp. Ser. 615), Washington, D.C.: ACS, 1995, 374–386.",
    ]
    return ["%d. %s" % (i + 1, r) for i, r in enumerate(refs)]


# ================================================================ 31.1

def sec_31_1_vi():
    b = [h2("31.1 Cơ học của mặt chất lưu", "Mechanics of Fluid Surfaces")]
    b.append(p(
        "Tác dụng của sức căng bề mặt có thể thấy trong nhiều tình huống hằng ngày. Một vòi nước "
        "rỉ chậm nhỏ giọt vì lực sức căng bề mặt giữ nước bám lại cho đến khi khối lượng nước đủ "
        "lớn để thoát ra. Sức căng bề mặt có thể khiến một chiếc kim thép “nổi” trên mặt nước dù "
        "khối lượng riêng của nó lớn hơn nước rất nhiều. Có thể hình dung bề mặt chất lỏng như có "
        "một lớp da đang bị kéo căng. Một giọt chất lỏng phần nào giống một quả bóng bay chứa đầy "
        "không khí: lớp da đàn hồi của bóng giữ không khí bên trong ở áp suất cao hơn không khí "
        "xung quanh, và bề mặt giọt chất lỏng cũng vậy — nó giữ chất lỏng bên trong ở áp suất hơi "
        "cao hơn áp suất môi trường."))
    b.append(p(
        "Tuy nhiên, một mặt chất lỏng sạch không đàn hồi như da cao su. Sức căng trong một miếng "
        "cao su tăng lên khi bị kéo giãn và cuối cùng sẽ đứt; còn mặt chất lỏng sạch có thể mở rộng "
        "vô hạn mà sức căng bề mặt không đổi."))

    b.append(h3("Mô hình cơ học và năng lượng bề mặt",
                "The mechanical model and surface energy", "t31-mohinh"))
    b.append(p(
        "Mô hình cơ học của mặt chất lỏng là một lớp da đang chịu kéo. Một mảnh bề mặt bất kỳ vì "
        "thế chịu một lực hướng ra ngoài, tiếp tuyến với bề mặt, tại mọi điểm trên chu vi của nó. "
        "Lực trên một đơn vị dài chu vi, tác dụng vuông góc với chu vi, được định nghĩa là "
        "<b>sức căng bề mặt</b> γ."))
    b.append(p(
        "Các phân tử trong vùng liên bề mặt có thế năng cao hơn phân tử trong lòng các pha, do sự "
        "mất cân bằng của lực hút giữa các phân tử. Kết quả là có một năng lượng tự do dư trên một "
        "đơn vị diện tích gắn với bề mặt, và về trị số nó bằng sức căng bề mặt. Xét một mảnh mặt "
        "phân cách phẳng hình chữ nhật rộng <i>W</i> và dài <i>L</i>. Để kéo dài thêm Δ<i>L</i>, "
        "phải thực hiện một công γ<i>W</i>Δ<i>L</i> ở biên. Tích <i>W</i>Δ<i>L</i> chính là độ biến "
        "thiên diện tích Δ<i>A</i> của bề mặt. Vậy công để tăng diện tích là γΔ<i>A</i>, đúng bằng "
        "độ tăng năng lượng tự do bề mặt. Do đó sức căng bề mặt γ tương đương với năng lượng tự do "
        "bề mặt trên một đơn vị diện tích."))
    b.append(p(
        "Các chất lỏng hữu cơ ở nhiệt độ phòng thường có sức căng bề mặt trong khoảng "
        "20 mN m<sup>–1</sup> đến 40 mN m<sup>–1</sup>, còn nước tinh khiết là "
        "72 mN m<sup>–1</sup> ở 25 °C. Mặt phân cách giữa hai chất lỏng không trộn lẫn, như dầu và "
        "nước, cũng có một sức căng gắn với nó, thường được gọi là <b>sức căng liên bề mặt</b>."))

    b.append(h3("Hình dạng và chất hoạt động bề mặt",
                "Shape, and surface-active agents", "t31-hinhdang"))
    b.append(p(
        "Khái niệm năng lượng bề mặt rất hữu ích để hiểu hình dạng mà mặt chất lỏng chấp nhận. Một "
        "hệ cô lập ở trạng thái cân bằng là hệ có năng lượng tự do cực tiểu. Vì năng lượng tự do bề "
        "mặt góp vào năng lượng tự do toàn phần của hệ nhiều pha, nó bị cực tiểu hoá ở cân bằng với "
        "những ràng buộc nhất định; và do năng lượng tự do bề mặt tỉ lệ trực tiếp với diện tích bề "
        "mặt nên diện tích bề mặt cũng bị cực tiểu hoá. Không có trọng lực, một giọt chất lỏng tự "
        "do sẽ có dạng cầu, vì với một thể tích cho trước, hình cầu có diện tích bề mặt nhỏ nhất. "
        "Nhưng một giọt treo ở đầu kim trên Trái Đất không thành hình cầu hoàn hảo: cấu hình năng "
        "lượng tự do cực tiểu ở đây là sự thoả hiệp giữa việc giảm năng lượng bề mặt và việc giảm "
        "thế năng trọng trường. Giọt dài ra để hạ thấp thế năng trọng trường của nó."))
    b.append(p(
        "Khái niệm năng lượng bề mặt cũng giúp hiểu hành vi của các chất hoạt động bề mặt. Một hỗn "
        "hợp hai thành phần ở cân bằng nhiệt động sẽ hấp phụ ưu tiên một thành phần ở bề mặt nếu "
        "việc hấp phụ đó làm giảm năng lượng bề mặt. Thuật ngữ <i>chất hoạt động bề mặt</i> dành "
        "cho những phân tử hấp phụ mạnh ở bề mặt ngay cả khi nồng độ của chúng trong lòng chất lỏng "
        "rất thấp. Chất hoạt động bề mặt có mặt phổ biến trong nước tự nhiên và đóng vai trò rất "
        "quan trọng trong nhiều quá trình sinh học và công nghiệp."))

    b.append(h3("Đường tiếp xúc và góc tiếp xúc",
                "The contact line and the contact angle", "t31-tiepxuc"))
    b.append(p(
        "Mặt phân cách giữa chất rắn và chất lưu cũng có năng lượng tự do bề mặt. Hình 31.1(a) cho "
        "thấy một giọt chất lỏng nằm yên trên mặt rắn trong không khí. Hệ này có ba loại mặt phân "
        "cách: rắn–khí, rắn–lỏng và lỏng–khí, mỗi loại có một năng lượng tự do bề mặt riêng trên "
        "một đơn vị diện tích. Trạng thái năng lượng tự do cực tiểu của hệ vì thế là sự thoả hiệp "
        "về diện tích bề mặt của các mặt phân cách khác nhau. Vùng tiếp xúc giữa khí, lỏng và rắn "
        "được gọi là <b>đường tiếp xúc</b>. Mặt lỏng–khí gặp mặt rắn dưới một góc θ đo qua pha "
        "lỏng, gọi là <b>góc tiếp xúc</b>. Góc tiếp xúc nhận giá trị làm cực tiểu hoá năng lượng tự "
        "do của hệ, và do đó là một đặc trưng của từng hệ rắn–lỏng–khí."))
    b.append(fig(1, F.fig(1), "vi"))
    b.append(p(
        "Hệ ở Hình 31.1(a) có góc tiếp xúc nhỏ hơn hệ ở Hình 31.1(b). Góc tiếp xúc càng nhỏ thì "
        "càng nói chất lỏng làm ướt bề mặt rắn tốt hơn. Khi θ = 0, chất lỏng được gọi là làm ướt "
        "hoàn toàn."))
    b.append(p(
        "Đo sức căng bề mặt quan trọng trong nhiều lĩnh vực khoa học, kỹ thuật cũng như trong y học. "
        "Có nhiều phương pháp chuẩn để đo nó. Trong nhiều hệ khảo sát, sức căng bề mặt thay đổi theo "
        "thời gian, chẳng hạn do hấp phụ chất hoạt động bề mặt. Một số phương pháp chuẩn dùng được "
        "để đo sức căng bề mặt động khi nó biến đổi chậm; với những hệ biến đổi rất nhanh, phải "
        "dùng những kỹ thuật riêng."))

    b.append(h3("Cân bằng tại đường tiếp xúc",
                "Equilibrium at the contact line", "t31-canhbang"))
    b.append(p(
        "Một số phương pháp đo sức căng bề mặt dựa vào cơ học tại đường tiếp xúc giữa rắn, lỏng và "
        "khí. Khi hệ ở cân bằng cơ học tĩnh, đường tiếp xúc đứng yên, nghĩa là hợp lực tác dụng lên "
        "nó bằng không. Các lực tác dụng lên đường tiếp xúc sinh ra từ sức căng của ba mặt phân "
        "cách hội tụ tại đó — rắn–khí, rắn–lỏng và lỏng–khí — ký hiệu lần lượt là γ<sub>SG</sub>, "
        "γ<sub>SL</sub> và γ<sub>LG</sub> (Hình 31.2). Điều kiện hợp lực theo phương tiếp tuyến với "
        "mặt rắn bằng không cho quan hệ sau giữa các sức căng bề mặt và góc tiếp xúc θ:"))
    b.append(eq("γ<sub>SG</sub> = γ<sub>SL</sub> + γ<sub>LG</sub> cos θ", "31.1"))
    b.append(p(
        "Đây là <b>phương trình Young</b>. Góc tiếp xúc vì thế phụ thuộc vào sức căng bề mặt giữa "
        "các pha có mặt trong hệ, và do đó là một thuộc tính nội tại của hệ."))
    b.append(fig(2, F.fig(2), "vi"))

    b.append(h3("Mặt cong và áp suất Laplace",
                "Curved surfaces and the Laplace pressure", "t31-laplace"))
    b.append(p(
        "Như đã nói ở phần mở đầu, sức căng bề mặt của một giọt làm áp suất bên trong giọt tăng "
        "lên. Có thể hiểu điều này bằng cách xét các lực tác dụng lên một mảnh mặt cong, như minh "
        "hoạ ở Hình 31.3(a). Do độ cong, các lực sức căng bề mặt kéo bề mặt về phía lõm. Để cân "
        "bằng cơ học, áp suất ở phía lõm vì thế phải lớn hơn. Hình 31.3(b) cho thấy một mảnh mặt "
        "dạng yên ngựa, ở đó các lực sức căng bề mặt đối kháng nhau và vì thế làm giảm hoặc triệt "
        "tiêu chênh lệch áp suất cần có qua mặt."))
    b.append(p(
        "Độ cong trung bình của một mặt hai chiều được xác định qua hai bán kính cong chính "
        "<i>R</i><sub>1</sub> và <i>R</i><sub>2</sub>, đo theo hai phương vuông góc. Phân tích cơ "
        "học chi tiết mặt chịu kéo cho thấy độ biến thiên áp suất qua mặt tỉ lệ trực tiếp với sức "
        "căng bề mặt và với độ cong trung bình của mặt:"))
    b.append(eq("P<sub>A</sub> − P<sub>B</sub> = γ (1/<i>R</i><sub>1</sub> + 1/<i>R</i><sub>2</sub>)",
                "31.2"))
    b.append(p(
        "trong đó γ là sức căng bề mặt và đại lượng trong ngoặc là hai lần độ cong trung bình. Bán "
        "kính cong được lấy dấu dương nếu tâm cong nằm trong pha A và âm nếu nằm trong pha B. "
        "Phương trình 31.2 được gọi là <b>phương trình Young–Laplace</b>, và độ biến thiên áp suất "
        "qua mặt phân cách được gọi là <b>áp suất Laplace</b>. Đo áp suất Laplace trên một mặt đã "
        "biết độ cong cho phép xác định sức căng bề mặt."))
    b.append(fig(3, F.fig(3), "vi"))

    b.append(h3("Giọt và bọt đối xứng trục",
                "Axisymmetric drops and bubbles", "t31-giot"))
    b.append(p(
        "Một số phương pháp đo sức căng bề mặt dựa trên việc đo hình dạng tĩnh của một giọt hay bọt "
        "đối xứng trục, hoặc dựa trên điểm bất ổn định cơ học của chúng. Trong trường trọng lực, "
        "một giọt hay bọt gắn vào giá đỡ rắn sẽ có dạng không cầu. Hình 31.4(a) cho thấy dạng của "
        "một giọt treo, còn Hình 31.4(b) là một giọt nằm. Bọt khí đối xứng trục trong nước có cùng "
        "dạng với giọt nước trong không khí, chỉ khác là bị lật ngược: bọt được đỡ từ phía dưới gọi "
        "là bọt treo, còn bọt được đỡ từ phía trên gọi là bọt giam hay bọt nằm."))
    b.append(p(
        "Lý do hình dạng lệch khỏi hình cầu có thể hiểu từ phương trình 31.2. Áp suất thuỷ tĩnh "
        "biến đổi theo độ sâu nhanh hơn nhiều trong chất lỏng so với trong chất khí. Vì thế chênh "
        "lệch áp suất qua mặt một giọt treo trong không khí tăng dần từ trên xuống dưới, đòi hỏi độ "
        "cong trung bình của mặt phải tăng theo phương trình 31.2. Giọt ở Hình 31.4(a) có một cổ ở "
        "phía trên, nghĩa là hai bán kính cong chính trái dấu và triệt tiêu nhau phần nào; ở đáy "
        "giọt, hai bán kính cong cùng dấu nên độ cong trung bình lớn hơn."))
    b.append(p(
        "Với một mặt đối xứng trục trong trường trọng lực, phương trình Young–Laplace có thể viết "
        "thành hệ phương trình vi phân cấp một ghép cặp theo các toạ độ của mặt phân cách:"))
    b.append(eq(
        "d<i>x</i>/d<i>s</i> = cos φ&nbsp;&nbsp;&nbsp;&nbsp; d<i>z</i>/d<i>s</i> = sin φ"
        "&nbsp;&nbsp;&nbsp;&nbsp; dφ/d<i>s</i> = 2/<i>b</i> + (Δρ<i>g</i>/γ) <i>z</i> − sin φ/<i>x</i>"
        "<br><span style=\"font-size:.86rem;color:#666\">"
        "<i>x</i>(0) = <i>z</i>(0) = φ(0) = 0</span>", "31.3"))
    b.append(p(
        "trong đó <i>x</i> và <i>z</i> là toạ độ ngang và thẳng đứng, gốc đặt tại đỉnh giọt; "
        "<i>s</i> là chiều dài cung dọc theo mặt giọt, đo từ đỉnh; và φ là góc giữa tiếp tuyến mặt "
        "và phương ngang (Hình 31.4a). Tham số <i>b</i> là bán kính cong tại đỉnh giọt hay bọt, Δρ "
        "là chênh lệch khối lượng riêng giữa hai pha lưu, và <i>g</i> là gia tốc trọng trường."))
    b.append(fig(4, F.fig(4), "vi"))
    b.append(p(
        "Tích phân số phương trình 31.3 cho phép tính hình dạng của một mặt chất lưu đối xứng trục. "
        "So sánh hình tính được với hình đo được của giọt hay bọt là một cách hữu ích để đo sức "
        "căng bề mặt. Nếu mọi độ dài trong phương trình 31.3 được làm vô thứ nguyên bằng cách chia "
        "cho <i>b</i>, phương trình thu được chỉ còn một tham số, "
        "β = Δρ<i>g</i><i>b</i><sup>2</sup>/γ, gọi là <b>số Bond</b> (hay hệ số hình dạng). Hình "
        "dạng của một giọt, bọt hay mặt khum đối xứng trục chỉ phụ thuộc vào một tham số vô thứ "
        "nguyên này. Số Bond cũng có thể viết là β = 2<i>b</i><sup>2</sup>/<i>a</i><sup>2</sup>, "
        "trong đó <i>a</i> = √(2γ/Δρ<i>g</i>) được gọi là <b>hằng số mao quản</b> và có thứ nguyên "
        "độ dài."))
    b.append(note(
        "<b>Lưu ý về ký hiệu.</b> Nguyên bản dùng <i>b</i> cho bán kính cong tại đỉnh giọt và β "
        "(beta) cho số Bond. Hai ký hiệu này rất dễ lẫn khi đọc lướt, nhất là trong phương trình "
        "31.8, nơi cả hai xuất hiện cạnh nhau."))

    b.append(h3("Sóng mao quản", "Capillary waves", "t31-song"))
    b.append(p(
        "Một số phương pháp động để đo sức căng bề mặt dựa trên sóng mao quản. Sóng mao quản sinh "
        "ra từ dao động của mặt chất lỏng mà ở đó sức căng bề mặt đóng vai trò lực phục hồi; do đó "
        "tần số dao động của mặt phụ thuộc vào sức căng bề mặt và bước sóng. Những sóng mao quản "
        "biên độ rất nhỏ với dải tần rộng luôn tồn tại trên mặt chất lỏng do thăng giáng nhiệt. Sóng "
        "mao quản biên độ lớn hơn có thể được kích thích bằng cách nhiễu loạn mặt một cách có chủ ý."))
    return "".join(b)


def sec_31_1_en():
    b = [h2("31.1 Mechanics of Fluid Surfaces", "")]
    b.append(p(
        "The effect of surface tension is observed in many everyday situations. A slowly leaking "
        "faucet drips because the force of surface tension lets the water cling to it until a "
        "sufficient mass has accumulated to break free. Surface tension can make a steel needle "
        "“float” on the surface of water although its density is much higher than that of water. "
        "The surface of a liquid can be thought of as having a skin under tension. A liquid droplet "
        "is somewhat analogous to a balloon filled with air: the elastic skin of the balloon holds "
        "the air inside at a pressure slightly above the surrounding air, and the surface of a "
        "liquid droplet likewise holds the liquid inside at a pressure slightly above ambient."))
    b.append(p(
        "A clean liquid surface, however, is not elastic like a rubber skin. The tension in a piece "
        "of rubber increases as it is stretched and will eventually rupture; a clean liquid surface "
        "can be expanded indefinitely without changing the surface tension."))

    b.append(h3("The mechanical model and surface energy", "", "t31-mohinh"))
    b.append(p(
        "The mechanical model of the liquid surface is that of a skin under tension. Any given "
        "patch of the surface thus experiences an outward force tangential to the surface "
        "everywhere on the perimeter. The force per unit length of the perimeter acting "
        "perpendicular to the perimeter is defined as the <b>surface tension</b>, γ."))
    b.append(p(
        "Molecules in the interfacial region have a higher potential energy than molecules in the "
        "bulk phases because of an imbalance of intermolecular attractive forces. This results in "
        "an excess free energy per unit area associated with the surface that is numerically "
        "equivalent to the surface tension. Consider a flat rectangular patch of fluid interface of "
        "width <i>W</i> and length <i>L</i>. In order to expand the length to <i>L</i> + Δ<i>L</i>, "
        "an amount of work γ<i>W</i>Δ<i>L</i> must be done at the boundary. The product "
        "<i>W</i>Δ<i>L</i> is just the change in area Δ<i>A</i> of the surface. The work done to "
        "increase the area is thus γΔ<i>A</i>, which corresponds to the increase in surface free "
        "energy. Thus the surface tension γ is seen to be equivalent to the surface free energy per "
        "unit area."))
    b.append(p(
        "Room-temperature organic liquids typically have surface tensions in the range of "
        "20 mN m<sup>–1</sup> to 40 mN m<sup>–1</sup>, while pure water has a value of "
        "72 mN m<sup>–1</sup> at 25 °C. The interface between two immiscible liquids, such as oil "
        "and water, also has a tension associated with it, generally referred to as the "
        "<b>interfacial tension</b>."))

    b.append(h3("Shape, and surface-active agents", "", "t31-hinhdang"))
    b.append(p(
        "The surface energy concept is useful for understanding the shapes adopted by liquid "
        "surfaces. An isolated system in equilibrium is in a state of minimum free energy. Because "
        "the surface free energy contributes to the total free energy of a multiphase system, the "
        "surface free energy is minimized at equilibrium subject to certain constraints; and "
        "because the surface free energy is directly proportional to the surface area, surface area "
        "is also minimized. In the absence of gravity, a free-floating liquid droplet assumes a "
        "spherical shape because, for a given volume of liquid, the sphere has the least surface "
        "area. However, a droplet suspended from a needle tip on Earth does not form a perfect "
        "sphere, because the minimum free energy configuration involves a trade-off between a "
        "reduction of the surface energy and a reduction of the gravitational potential. The "
        "droplet elongates to reduce its gravitational potential energy."))
    b.append(p(
        "The surface energy concept is also useful for understanding the behaviour of so-called "
        "surface active agents or <i>surfactants</i>. A two-component liquid mixture in "
        "thermodynamic equilibrium exhibits preferential adsorption of one component at the surface "
        "if the adsorption causes a decrease in the surface energy. The term surfactant is reserved "
        "for molecular species that strongly adsorb at the surface even when their concentration in "
        "the bulk liquid is very low. Surfactants are common in natural waters and are very "
        "important in many biological and industrial processes."))

    b.append(h3("The contact line and the contact angle", "", "t31-tiepxuc"))
    b.append(p(
        "The interface between a solid and a fluid also has a surface free energy associated with "
        "it. Figure 31.1(a) shows a liquid droplet at rest on a solid surface surrounded by air. "
        "This system contains three different types of interface: solid–gas, solid–liquid and "
        "liquid–gas, each with a characteristic surface free energy per unit area. The state of "
        "minimum free energy for the system then involves trade-offs in the surface area for the "
        "various interfaces. The region of contact between the gas, liquid and solid is termed the "
        "<b>contact line</b>. The liquid–gas surface meets the solid surface with an angle θ "
        "measured through the liquid, known as the <b>contact angle</b>. The contact angle attains a "
        "value that minimizes the free energy of the system and is thus a characteristic of a "
        "particular solid–liquid–gas system."))
    b.append(fig(1, F.fig(1), "en"))
    b.append(p(
        "The system shown in Figure 31.1(a) has a smaller contact angle than that shown in "
        "Figure 31.1(b). The smaller the contact angle, the better the liquid is said to wet the "
        "solid surface. For θ = 0, the liquid is said to be perfectly wetting."))
    b.append(p(
        "Measurement of surface tension is important in many fields of science and engineering, as "
        "well as in medicine. A number of standard methods exist for its measurement. In many "
        "systems of interest the surface tension changes with time, perhaps because of adsorption of "
        "surfactants. Several standard methods can be used to measure dynamic surface tension if it "
        "changes slowly with time. Special techniques have been developed to measure dynamic surface "
        "tensions for systems that evolve very rapidly."))

    b.append(h3("Equilibrium at the contact line", "", "t31-canhbang"))
    b.append(p(
        "Some methods of measuring surface tension depend on the mechanics at the line of contact "
        "between a solid, liquid and gas. When the system is in static mechanical equilibrium the "
        "contact line is motionless, meaning that the net force on the line is zero. Forces acting "
        "on the contact line arise from the surface tensions of the converging solid–gas, "
        "solid–liquid and liquid–gas interfaces, denoted by γ<sub>SG</sub>, γ<sub>SL</sub> and "
        "γ<sub>LG</sub> respectively (Figure 31.2). The condition of zero net force along the "
        "direction tangent to the solid surface gives the following relationship between the surface "
        "tensions and contact angle θ:"))
    b.append(eq("γ<sub>SG</sub> = γ<sub>SL</sub> + γ<sub>LG</sub> cos θ", "31.1"))
    b.append(p(
        "This is known as <b>Young’s equation</b>. The contact angle is thus seen to be dependent on "
        "the surface tensions between the various phases present in the system, and is therefore an "
        "intrinsic property of the system."))
    b.append(fig(2, F.fig(2), "en"))

    b.append(h3("Curved surfaces and the Laplace pressure", "", "t31-laplace"))
    b.append(p(
        "As discussed in the introduction, the surface tension of a droplet causes an increase in "
        "pressure in the droplet. This can be understood by considering the forces acting on a "
        "curved section of surface as illustrated in Figure 31.3(a). Because of the curvature, the "
        "surface tension forces pull the surface toward the concave side. For mechanical "
        "equilibrium, the pressure must then be greater on the concave side of the surface. "
        "Figure 31.3(b) shows a saddle-shaped section of surface in which surface tension forces "
        "oppose each other, thus reducing or eliminating the required pressure difference across "
        "the surface."))
    b.append(p(
        "The mean curvature of a two-dimensional surface is specified in terms of the two principal "
        "radii of curvature, <i>R</i><sub>1</sub> and <i>R</i><sub>2</sub>, which are measured in "
        "perpendicular directions. A detailed mechanical analysis of curved tensile surfaces shows "
        "that the pressure change across the surface is directly proportional to the surface tension "
        "and to the mean curvature of the surface:"))
    b.append(eq("P<sub>A</sub> − P<sub>B</sub> = γ (1/<i>R</i><sub>1</sub> + 1/<i>R</i><sub>2</sub>)",
                "31.2"))
    b.append(p(
        "where γ is the surface tension, and the quantity in brackets is twice the mean curvature. "
        "The sign of the radius of curvature is positive if its centre of curvature lies in phase A "
        "and negative if it lies in phase B. Equation 31.2 is known as the "
        "<b>Young–Laplace equation</b>, and the pressure change across the interface is termed the "
        "<b>Laplace pressure</b>. Measurement of the Laplace pressure for a surface of known "
        "curvature then allows a determination of the surface tension."))
    b.append(fig(3, F.fig(3), "en"))

    b.append(h3("Axisymmetric drops and bubbles", "", "t31-giot"))
    b.append(p(
        "Several methods of surface tension measurement are based on the measurement of the static "
        "shape of an axisymmetric drop or bubble, or on the point of mechanical instability of such "
        "drops or bubbles. In a gravitational field a drop or bubble attached to a solid support "
        "assumes a nonspherical shape. Figure 31.4(a) shows the shape of a hanging droplet, also "
        "known as a pendant drop, and Figure 31.4(b) shows a so-called sessile drop. Axisymmetric "
        "air bubbles in water attain the same shapes as water drops in air, except that they are "
        "inverted: a bubble supported from below is called a hanging or pendant bubble, and a "
        "bubble supported from above is called a captive or sessile bubble."))
    b.append(p(
        "The reason for the deviation of the shape from that of a sphere can be understood from "
        "Equation 31.2. The hydrostatic pressure changes with depth more rapidly in a liquid than in "
        "a gas. The pressure difference across the surface of a pendant drop in air therefore "
        "increases from top to bottom, requiring an increase in the mean curvature of the surface "
        "according to Equation 31.2. The drop in Figure 31.4(a) has a neck at the top, which means "
        "that the two principal radii of curvature have opposite signs and cancel to some extent. At "
        "the bottom of the drop the radii of curvature have the same sign, thus making the mean "
        "curvature larger."))
    b.append(p(
        "For an axisymmetric surface in a gravitational field, the Young–Laplace equation can be "
        "written as coupled first-order differential equations in terms of the coordinates of the "
        "interface:"))
    b.append(eq(
        "d<i>x</i>/d<i>s</i> = cos φ&nbsp;&nbsp;&nbsp;&nbsp; d<i>z</i>/d<i>s</i> = sin φ"
        "&nbsp;&nbsp;&nbsp;&nbsp; dφ/d<i>s</i> = 2/<i>b</i> + (Δρ<i>g</i>/γ) <i>z</i> − sin φ/<i>x</i>"
        "<br><span style=\"font-size:.86rem;color:#666\">"
        "<i>x</i>(0) = <i>z</i>(0) = φ(0) = 0</span>", "31.3"))
    b.append(p(
        "where <i>x</i> and <i>z</i> are the horizontal and vertical coordinates, with the origin at "
        "the drop apex; <i>s</i> is the arc length along the drop surface measured from the drop "
        "apex; and φ is the angle between the surface tangent and the horizontal "
        "(Figure 31.4a). The parameter <i>b</i> is the radius of curvature at the apex of the drop "
        "or bubble, Δρ is the density difference between the two fluid phases, and <i>g</i> is the "
        "acceleration of gravity."))
    b.append(fig(4, F.fig(4), "en"))
    b.append(p(
        "Numerical integration of Equation 31.3 allows one to compute the shape of an axisymmetric "
        "fluid interface. Comparison of computed shapes with experimentally measured shapes of drops "
        "or bubbles is a useful method of measuring surface tension. If all lengths in Equation 31.3 "
        "are made dimensionless by dividing them by <i>b</i>, the resulting equation contains only "
        "one parameter, β = Δρ<i>g</i><i>b</i><sup>2</sup>/γ, which is called the <b>Bond number</b> "
        "(or shape factor). The shape of an axisymmetric drop, bubble or meniscus depends only on "
        "this one dimensionless parameter. The Bond number can also be written as "
        "β = 2<i>b</i><sup>2</sup>/<i>a</i><sup>2</sup>, where <i>a</i> = √(2γ/Δρ<i>g</i>) is known "
        "as the <b>capillary constant</b> and has units of length."))
    b.append(note(
        "<b>A note on the symbols.</b> The source uses <i>b</i> for the radius of curvature at the "
        "drop apex and β (beta) for the Bond number. The two are easy to confuse when reading "
        "quickly, especially in Equation 31.8, where both appear side by side."))

    b.append(h3("Capillary waves", "", "t31-song"))
    b.append(p(
        "Several dynamic methods of measuring surface tension are based on capillary waves. "
        "Capillary waves result from oscillations of the liquid surface for which surface tension is "
        "the restoring force. The frequency of the surface oscillation is thus dependent on the "
        "surface tension and wavelength. Very low amplitude capillary waves with a broad range of "
        "frequencies are always present on liquid surfaces owing to thermal fluctuations. Larger "
        "amplitude capillary waves can be excited by purposely perturbing the surface."))
    return "".join(b)


# ================================================================ 31.2

def sec_31_2_vi():
    b = [h2("31.2 Các phương pháp và thiết bị chuẩn", "Standard Methods and Instrumentation")]
    b.append(p(
        "Có nhiều phương pháp đo sức căng bề mặt thông dụng. Việc chọn phương pháp phụ thuộc vào "
        "hệ cần khảo sát, độ chính xác yêu cầu và cả khả năng tự động hoá phép đo. Trong phần dưới, "
        "các phương pháp được nhóm theo loại thiết bị dùng để đo. Vì thông tin cho mỗi phương pháp "
        "buộc phải ngắn gọn, bạn đọc muốn tự chế tạo thiết bị nên tham khảo các chuyên khảo chi tiết "
        "hơn trong [1–4]. Bảng 31.1 liệt kê các thiết bị bán trên thị trường cùng tên hãng và giá "
        "xấp xỉ; địa chỉ liên hệ của các hãng ở Bảng 31.2."))
    b.append(_t311("vi"))
    b.append(_t312("vi"))

    b.append(h3("Phương pháp mao dẫn dâng", "Capillary rise method", "t31-maodan"))
    b.append(p(
        "Nếu nhúng một ống mao quản thuỷ tinh vào mặt chất lỏng, và nếu chất lỏng làm ướt thuỷ "
        "tinh với góc tiếp xúc nhỏ hơn 90°, thì chất lỏng bị hút dâng lên trong ống như ở Hình "
        "31.5(a). Sức căng bề mặt tỉ lệ trực tiếp với chiều cao dâng <i>h</i> của chất lỏng trong "
        "ống so với mặt phẳng của chất lỏng trong bình lớn. Áp dụng phương trình 31.2 cho mặt khum "
        "trong ống mao quản cho quan hệ sau:"))
    b.append(eq("Δρ<i>g</i><i>h</i> = 2γ/<i>b</i>", "31.4"))
    b.append(p(
        "trong đó <i>b</i> là bán kính cong tại tâm mặt khum và Δρ là chênh lệch khối lượng riêng "
        "giữa lỏng và khí. Với ống mao quản nhỏ, <i>b</i> được xấp xỉ tốt bằng bán kính của chính "
        "ống, với giả thiết góc tiếp xúc của chất lỏng trên thành ống bằng không. Với ống lớn hơn "
        "hoặc khi cần độ chính xác cao hơn, giá trị của <i>b</i> phải được hiệu chỉnh cho biến dạng "
        "của mặt khum dưới tác dụng của trọng lực (tr. 12 của [1])."))
    b.append(fig(5, F.fig(5), "vi"))
    b.append(p(
        "Để có kết quả chính xác bằng phương pháp mao dẫn dâng, phải dùng ống mao quản thuỷ tinh "
        "sạch hoàn toàn với đường kính rất đều và nhỏ hơn 1 mm. Bình chứa chất lỏng phải có đường "
        "kính ít nhất 8 cm, và chất lỏng phải làm ướt ống mao quản với góc tiếp xúc bằng không. "
        "Phương pháp này chủ yếu dùng cho chất lỏng tinh khiết và có thể đạt độ chính xác cao với "
        "chi phí tương đối thấp."))

    b.append(h3("Phương pháp bản Wilhelmy và vòng du Noüy",
                "Wilhelmy plate and du Noüy ring methods", "t31-wilhelmy"))
    b.append(p(
        "Đo lực kéo của mặt chất lỏng tác dụng trực tiếp lên một vật rắn là cơ sở của hai trong số "
        "các phương pháp chuẩn ở đây. Trong phương pháp bản Wilhelmy, vật rắn là một bản phẳng, mỏng "
        "mà chất lỏng cần đo phải làm ướt với góc tiếp xúc bằng không. Bản được treo thẳng đứng trên "
        "một cân nhạy, cân được đặt về không khi bản còn treo trong không khí. Đưa chất lỏng cần đo "
        "tiếp xúc với mép dưới của bản; sức căng bề mặt kéo bản xuống vào chất lỏng. Sau đó tăng lực "
        "tác dụng từ phía trên để đưa mép dưới của bản ngang bằng với mặt phẳng của chất lỏng (Hình "
        "31.5b). Cách này tránh được việc phải hiệu chỉnh lực đẩy Archimedes cho phép đo."))
    b.append(p("Sức căng bề mặt được tính từ lực đo được <i>f</i> theo:"))
    b.append(eq("γ = <i>f</i> cos θ / [2(<i>l</i> + <i>t</i>)]", "31.5"))
    b.append(p(
        "trong đó <i>l</i> là chiều dài bản và <i>t</i> là độ dày. Góc tiếp xúc θ thường được giả "
        "định bằng không với các chất lỏng thông dụng trên bản thuỷ tinh hay bạch kim sạch, nhưng "
        "cần lưu ý sai số do góc tiếp xúc khác không gây ra. Phương pháp này không cần hệ số hiệu "
        "chỉnh nào khác và không cần biết khối lượng riêng của chất lưu."))
    b.append(p(
        "Phương pháp vòng du Noüy là một phương pháp lực kéo cực đại, có nhiều biến thể. Kỹ thuật "
        "là cho một chiếc vòng tiếp xúc với mặt chất lỏng rồi đo lực liên tục trong khi hạ mặt xuống "
        "cho đến khi ghi được lực cực đại <i>f</i><sub>max</sub>. Lực cực đại thường xuất hiện ngay "
        "trước khi vòng tách khỏi mặt. Sức căng bề mặt thu được từ công thức:"))
    b.append(eq(
        "γ = (<i>f</i><sub>max</sub>/4π<i>R</i>) · F(<i>R</i><sup>3</sup>/<i>V</i>, "
        "<i>R</i>/<i>r</i>)", "31.6"))
    b.append(p(
        "trong đó <i>R</i> và <i>r</i> lần lượt là bán kính của vòng và của dây, như chỉ ra ở Hình "
        "31.5(c), <i>V</i> là thể tích chất lỏng bị vòng kéo lên, và F là hệ số hiệu chỉnh (F được "
        "lập bảng ở Bảng 5, tr. 132 của [4]). Phương pháp vòng du Noüy đòi hỏi biết khối lượng riêng "
        "của chất lỏng ρ<sub>L</sub> để xác định <i>V</i> từ "
        "<i>V</i> = <i>f</i><sub>max</sub>/ρ<sub>L</sub>. Phương pháp này yêu cầu chất lỏng làm ướt "
        "vòng với góc tiếp xúc bằng không và không thích hợp cho các dung dịch đạt cân bằng bề mặt "
        "chậm."))
    b.append(p(
        "Một thiết bị thường có thể thực hiện được cả phép đo bằng bản Wilhelmy lẫn vòng du Noüy. "
        "Một số thiết bị bán trên thị trường có thể tự động thực hiện toàn bộ quy trình đo. Ghép máy "
        "tính với thiết bị bản Wilhelmy cho phép ghi dữ liệu tự động, dùng để theo dõi sự thay đổi "
        "sức căng bề mặt theo thời gian trong các dung dịch chất hoạt động bề mặt."))

    b.append(h3("Phương pháp áp suất bọt cực đại",
                "Maximum bubble pressure method", "t31-bot"))
    b.append(p(
        "Phương pháp áp suất bọt cực đại (MBPM) đo trực tiếp áp suất trong một bọt để xác định sức "
        "căng bề mặt. Một ống được hạ xuống độ sâu <i>t</i> trong chất lỏng cần đo và khí được bơm "
        "vào để tạo một bọt có chiều cao <i>Z</i><sub>B</sub> ở đầu ống, như ở Hình 31.5(d). Độ tăng "
        "áp suất trong bọt <i>P</i><sub>b</sub> so với áp suất môi trường <i>P</i><sub>a</sub>, do "
        "mặt phân cách gây ra, bằng tổng của áp suất thuỷ tĩnh và áp suất Laplace:"))
    b.append(eq(
        "δ<i>p</i> = <i>P</i><sub>b</sub> − <i>P</i><sub>a</sub> − Δρ<i>gt</i> = "
        "Δρ<i>gZ</i><sub>B</sub> + 2γ/<i>b</i>", "31.7"))
    b.append(p(
        "Khi một bọt mới bắt đầu hình thành, <i>Z</i><sub>B</sub> tăng trong khi <i>b</i> — bán "
        "kính cong tại đỉnh bọt — giảm, làm áp suất trong bọt tăng. Cuối cùng <i>b</i> lại tăng khi "
        "bọt lớn lên, do đó áp suất giảm. Vậy áp suất trong bọt đạt cực đại khi δ<i>p</i> đạt cực "
        "đại, và đại lượng này có thể liên hệ về mặt lý thuyết với sức căng bề mặt. Với "
        "δ<i>p</i> = δ<i>p</i><sub>max</sub>, phương trình 31.7 có thể viết lại ở dạng vô thứ nguyên "
        "như sau:"))
    b.append(eq(
        "<i>r</i>/<i>X</i> = <i>r</i>/<i>b</i> + (<i>r</i>/<i>a</i>)(<i>Z</i><sub>B</sub>/<i>b</i>)"
        "(β/2)<sup>1/2</sup>", "31.8"))
    b.append(p(
        "trong đó <i>r</i> là bán kính ống, <i>X</i> là một độ dài xác định bởi "
        "<i>X</i> = 2γ/δ<i>p</i><sub>max</sub>, <i>a</i> là hằng số mao quản, và β là số Bond. Đại "
        "lượng vô thứ nguyên <i>r</i>/<i>X</i> chỉ phụ thuộc vào <i>r</i>/<i>a</i>; quan hệ này được "
        "xác định từ phương trình 31.8 kết hợp với nghiệm số của phương trình 31.3. Các bảng của "
        "quan hệ này được dùng để tính sức căng bề mặt bằng một thủ tục lặp (tr. 18 của [1]). MBPM "
        "chuẩn đòi hỏi biết khối lượng riêng của chất lưu, bán kính ống và độ sâu nhúng của ống."))
    b.append(p(
        "Một MBPM vi sai dùng hai ống có đường kính khác nhau nhúng ở cùng một độ sâu. Người ta đo "
        "hiệu áp suất bọt cực đại giữa hai ống, Δ<i>P</i>; nhờ vậy không cần biết độ sâu nhúng và "
        "phép đo bớt nhạy với sai số về khối lượng riêng chất lỏng. Với MBPM vi sai, sức căng bề mặt "
        "được tính từ (xem [5]):"))
    b.append(eq(
        "γ = <i>A</i>Δ<i>P</i> [1 + (0,69 <i>r</i><sub>2</sub>ρ<sub>L</sub>/Δ<i>P</i>)]", "31.9"))
    b.append(note(
        "<b>Lưu ý của người dịch.</b> Ở phương trình 31.9, tử số của số hạng hiệu chỉnh in là "
        "0,69 <i>r</i><sub>2</sub>ρ<sub>L</sub>, không có <i>g</i>. Số hạng này phải có thứ nguyên "
        "của áp suất để cộng được với Δ<i>P</i>, nên trên thực tế phải là "
        "0,69 <i>r</i><sub>2</sub>ρ<sub>L</sub><i>g</i>. Bản dịch giữ nguyên như nguyên bản in và "
        "ghi chú điều này ở đây."))
    b.append(p(
        "trong đó <i>r</i><sub>2</sub> là bán kính của ống lớn hơn, ρ<sub>L</sub> là khối lượng riêng "
        "của chất lỏng, và <i>A</i> là một hằng số phụ thuộc thiết bị, xác định bằng hiệu chuẩn với "
        "một số chất lỏng chuẩn [6]. Các thiết bị MBPM tự động có bán trên thị trường (xem Bảng "
        "31.1). Sensa Dyne chế tạo thiết bị MBPM vi sai cho phép đo trực tuyến trong quá trình sản "
        "xuất ở điều kiện nhiệt độ và áp suất thay đổi."))

    b.append(h3("Phương pháp giọt treo và giọt nằm",
                "Pendant drop and sessile drop methods", "t31-giotdo"))
    b.append(p(
        "Hình dạng của một giọt treo hay giọt nằm đối xứng trục (Hình 31.4) chỉ phụ thuộc vào một "
        "tham số duy nhất là số Bond, như đã bàn ở trên. Số Bond đo mức độ quan trọng tương đối của "
        "trọng lực so với sức căng bề mặt trong việc quyết định hình dạng giọt. Với số Bond gần "
        "không, sức căng bề mặt chiếm ưu thế và giọt gần như hình cầu. Với số Bond lớn hơn, giọt bị "
        "trọng lực làm biến dạng đáng kể. Về nguyên tắc, phương pháp gồm việc thu ảnh của giọt rồi "
        "so sánh hình dạng và kích thước của nó với các prôfin lý thuyết thu được bằng cách tích "
        "phân phương trình 31.3 với nhiều giá trị β và <i>b</i> khác nhau. Khi đã xác định được β và "
        "<i>b</i> từ việc so sánh hình dạng và kích thước, sức căng bề mặt được tính từ:"))
    b.append(eq("γ = Δρ<i>g</i><i>b</i><sup>2</sup>/β", "31.10"))
    b.append(p(
        "Trong thực tế, hình dạng và kích thước giọt trước đây thường được xác định bằng cách đo tay "
        "một số kích thước đặc trưng (xem Hình 31.4) trên ảnh chụp. Với giọt treo, tỉ số "
        "<i>d</i><sub>s</sub>/<i>d</i><sub>e</sub> được tương quan với một hệ số hình dạng <i>H</i>, "
        "từ đó tính sức căng bề mặt (tr. 27 của [3], [7]) theo:"))
    b.append(eq("γ = Δρ<i>g</i><i>d</i><sub>e</sub><sup>2</sup>/<i>H</i>", "31.11"))
    b.append(p(
        "Với giọt nằm, có nhiều công thức giải tích để tính trực tiếp sức căng bề mặt từ các kích "
        "thước đặc trưng (tr. 36 của [3]). Các phương pháp dựa trên kích thước đặc trưng đòi hỏi đo "
        "kích thước rất chính xác mới có kết quả tốt. Để có kết quả chính xác hơn, nên dùng các "
        "phương pháp khớp toàn bộ đường viền của giọt với phương trình Laplace."))
    b.append(p(
        "Những năm gần đây, toàn bộ quy trình đã được tự động hoá nhờ ảnh số và phân tích ảnh bằng "
        "máy tính [8, 9]. Thông thường, vài trăm toạ độ trên đường viền giọt được xác định với độ "
        "phân giải dưới điểm ảnh bằng phân tích ảnh số. Kích thước, hình dạng và độ lệch ngang, dọc "
        "của prôfin lý thuyết cho bởi phương trình 31.3 được thay đổi thông qua bốn tham số: β, "
        "<i>b</i>, và toạ độ điểm ảnh của đỉnh giọt <i>x</i><sub>0</sub> và <i>z</i><sub>0</sub>. "
        "Khớp tốt nhất giữa prôfin lý thuyết và các toạ độ đường viền đo được thu được bằng cách cực "
        "tiểu hoá một hàm mục tiêu. Một ảnh số của giọt treo có thể được phân tích để tìm sức căng bề "
        "mặt trên máy tính để bàn trong 1 hoặc 2 giây [10]. Tốc độ của các thuật toán phân tích giọt "
        "treo trên máy tính hiện đại đã cho phép dùng phương pháp này để theo dõi sự thay đổi sức "
        "căng bề mặt của các bề mặt phủ chất hoạt động bề mặt, bằng cách phân tích một chuỗi ảnh. "
        "Các thuật toán có thể đồng thời theo dõi diện tích bề mặt và thể tích của giọt hay bọt."))
    b.append(p(
        "Cả chất hoạt động bề mặt tan và không tan đều đã được nghiên cứu bằng các cấu hình giọt "
        "treo, giọt nằm, bọt treo và bọt giam [11–13]. Bảng 31.1 liệt kê một số hãng cung cấp phần "
        "mềm phân tích tự động sức căng bề mặt từ giọt hay bọt ở cấu hình treo hoặc nằm. Độ chính "
        "xác và tính đơn giản tăng lên của quy trình giọt treo tự động khiến nó trở thành một phương "
        "pháp rất linh hoạt, đã được áp dụng để đo sức căng liên bề mặt cực thấp, sự phụ thuộc của "
        "sức căng liên bề mặt vào áp suất, nhiệt độ và thời gian, sự hồi phục của các lớp hấp phụ, "
        "đo sức căng đường, và các phép đo cân màng [14]."))

    b.append(h3("Phương pháp trọng lượng hoặc thể tích giọt",
                "Drop weight or volume method", "t31-trongluong"))
    b.append(p(
        "Một giọt treo sẽ trở nên bất ổn định và tách khỏi giá đỡ nếu lớn quá. Trọng lượng của phần "
        "tách ra liên hệ với sức căng bề mặt của chất lưu bởi:"))
    b.append(eq("γ = (<i>mg</i>/<i>r</i>) · F(<i>r</i>/<i>V</i><sup>1/3</sup>)", "31.12"))
    b.append(p(
        "trong đó <i>mg</i> là trọng lượng của giọt tách ra, <i>r</i> là bán kính của đầu ống mà "
        "giọt treo vào, và <i>V</i> là thể tích của giọt tách ra. Một hệ số hiệu chỉnh thực nghiệm F "
        "được lập bảng theo <i>r</i>/<i>V</i><sup>1/3</sup> (tr. 50 của [3]). Để áp dụng được phương "
        "trình 31.12, giọt phải được tạo thành chậm. Phép đo thường gồm việc cân lượng chất lỏng "
        "tích lại từ một số lớn giọt để xác định trọng lượng trung bình mỗi giọt. Phải biết khối "
        "lượng riêng của chất lưu để xác định thể tích giọt rồi từ đó lấy hệ số F. Một cách khác là "
        "đo lưu lượng thể tích chất lỏng tới đầu ống trong khi đếm số giọt; khi đó phải biết khối "
        "lượng riêng của chất lưu để xác định trọng lượng giọt. Cách sau cho phép tự động hoá phép "
        "đo [15]."))

    b.append(h3("Phương pháp giọt quay", "Spinning drop method", "t31-quay"))
    b.append(p(
        "Phương pháp giọt quay là một phương pháp đo hình dạng, tương tự phương pháp giọt treo và "
        "giọt nằm. Tuy nhiên ở đây giọt bị biến dạng bởi gradient áp suất hướng tâm trong một ống "
        "quay nhanh. Phương pháp này thường dùng để đo sức căng liên bề mặt giữa các chất lỏng không "
        "trộn lẫn. Một ống thuỷ tinh nằm ngang bịt kín hai đầu được nạp chất lỏng đậm đặc hơn qua "
        "một cửa nạp. Sau đó ống được quay quanh trục của nó trong khi một giọt chất lỏng nhẹ hơn "
        "được bơm vào ống. Do chuyển động quay, áp suất trong chất lỏng bên ngoài tăng từ tâm ống ra "
        "thành ống. Gradient áp suất đẩy giọt về tâm ống và làm nó dài ra, trong khi sức căng bề mặt "
        "chống lại sự dài ra đó. Đo đường kính lớn nhất của giọt 2<i>r</i><sub>max</sub> và chiều dài "
        "2<i>h</i><sub>max</sub>, cùng với vận tốc góc Ω, cho phép tính sức căng bề mặt theo:"))
    b.append(eq(
        "γ = ½ (<i>r</i><sub>max</sub>/<i>r</i><sup>*</sup><sub>max</sub>)<sup>3</sup> ΔρΩ<sup>2</sup>",
        "31.13"))
    b.append(p(
        "trong đó <i>r</i><sup>*</sup><sub>max</sub> tương quan với tỉ số dạng "
        "<i>r</i><sub>max</sub>/<i>h</i><sub>max</sub> [16]. Phương pháp giọt quay đặc biệt thích "
        "hợp để đo sức căng liên bề mặt cực thấp (10<sup>–2</sup> mN m<sup>–1</sup> đến "
        "10<sup>–4</sup> mN m<sup>–1</sup>)."))
    return "".join(b)


def sec_31_2_en():
    b = [h2("31.2 Standard Methods and Instrumentation", "")]
    b.append(p(
        "A number of commonly used methods of measuring surface tension exist. The choice of a "
        "method depends on the system to be studied, the degree of accuracy required, and possibly "
        "on the ability to automate the measurements. In the discussion that follows, these methods "
        "are grouped according to the kind of instruments used in the measurements. Because the "
        "information presented for each method is necessarily brief, readers who are interested in "
        "constructing their own apparatus should consult the more detailed treatises in [1–4]. A "
        "list of commercially available instruments is given in Table 31.1, together with "
        "manufacturer names and approximate prices. Vendors can be contacted at the addresses given "
        "in Table 31.2."))
    b.append(_t311("en"))
    b.append(_t312("en"))

    b.append(h3("Capillary rise method", "", "t31-maodan"))
    b.append(p(
        "If a glass capillary tube is brought into contact with a liquid surface, and if the liquid "
        "wets the glass with a contact angle of less than 90°, then the liquid is drawn up into the "
        "tube as shown in Figure 31.5(a). The surface tension is directly proportional to the height "
        "of rise, <i>h</i>, of the liquid in the tube relative to the flat liquid surface in the "
        "larger container. By applying Equation 31.2 to the meniscus in the capillary tube, the "
        "following relationship is obtained:"))
    b.append(eq("Δρ<i>g</i><i>h</i> = 2γ/<i>b</i>", "31.4"))
    b.append(p(
        "where <i>b</i> is the radius of curvature at the centre of the meniscus and Δρ is the "
        "density difference between liquid and gas. For small capillary tubes, <i>b</i> is well "
        "approximated by the radius of the tube itself, assuming that the contact angle of the "
        "liquid on the tube is zero. For larger tubes or for increased accuracy, the value of "
        "<i>b</i> must be corrected for gravitational deformation of the meniscus (p. 12 of [1])."))
    b.append(fig(5, F.fig(5), "en"))
    b.append(p(
        "Obtaining accurate results with the capillary rise method requires using a thoroughly "
        "clean glass capillary tube with a very uniform diameter of less than 1 mm. The container "
        "for the liquid should be at least 8 cm in diameter, and the liquid must wet the capillary "
        "tube with a contact angle of zero. This method is primarily useful for pure liquids and is "
        "capable of high accuracy at relatively low cost."))

    b.append(h3("Wilhelmy plate and du Noüy ring methods", "", "t31-wilhelmy"))
    b.append(p(
        "Measurement of the pull of a liquid surface directly on a solid object is the basis for "
        "two of the standard methods discussed here. In the Wilhelmy plate method, the solid object "
        "is a flat, thin plate that the test liquid should wet with a zero contact angle. The plate "
        "is suspended vertically from a delicate balance that is zeroed with the plate suspended in "
        "air. The test liquid is brought into contact with the bottom of the plate, causing the "
        "plate to be pulled down into the liquid by the surface tension force. The force applied to "
        "the plate from above is then increased to bring the bottom edge of the plate level with the "
        "flat surface of the liquid (Figure 31.5b). This avoids the necessity to make buoyancy "
        "corrections to the measurement."))
    b.append(p("The surface tension is computed from the force measurement, <i>f</i>, using:"))
    b.append(eq("γ = <i>f</i> cos θ / [2(<i>l</i> + <i>t</i>)]", "31.5"))
    b.append(p(
        "where <i>l</i> is the length of the plate and <i>t</i> is its thickness. The contact angle "
        "θ is often assumed to be zero for common liquids on clean glass or platinum plates, but one "
        "should be aware of the error caused by a non-zero contact angle. No other correction "
        "factors are necessary for this method and the fluid density does not need to be known."))
    b.append(p(
        "The du Noüy ring method is known as a maximum pull method, of which there are several "
        "variations. The technique is to contact the liquid surface with a ring and then measure the "
        "force continuously as the surface is lowered until a maximum force, "
        "<i>f</i><sub>max</sub>, is recorded. The maximum force typically occurs just before the "
        "ring detaches from the surface. The surface tension is obtained from the formula:"))
    b.append(eq(
        "γ = (<i>f</i><sub>max</sub>/4π<i>R</i>) · F(<i>R</i><sup>3</sup>/<i>V</i>, "
        "<i>R</i>/<i>r</i>)", "31.6"))
    b.append(p(
        "where <i>R</i> and <i>r</i> are the radii of the ring and wire, respectively, as indicated "
        "in Figure 31.5(c), <i>V</i> is the volume of liquid raised by the ring, and F is a "
        "correction factor (F is tabulated in Table 5, p. 132 of [4]). The du Noüy ring method "
        "requires knowledge of the liquid density, ρ<sub>L</sub>, in order to determine <i>V</i> "
        "from <i>V</i> = <i>f</i><sub>max</sub>/ρ<sub>L</sub>. This method requires the liquid to "
        "wet the ring with zero contact angle and is not suitable for solutions that attain surface "
        "equilibrium slowly."))
    b.append(p(
        "A single instrument is normally capable of performing either Wilhelmy plate or du Noüy ring "
        "measurements. Some commercially available instruments can perform the complete measurement "
        "procedure automatically. Computer interfacing with a Wilhelmy plate instrument allows "
        "automatic data logging, which can be used to follow changes in surface tension with time in "
        "surfactant solutions."))

    b.append(h3("Maximum bubble pressure method", "", "t31-bot"))
    b.append(p(
        "The maximum bubble pressure method (MBPM) involves direct measurement of the pressure in a "
        "bubble to determine the surface tension. A tube is lowered to a depth <i>t</i> in the test "
        "liquid and gas is injected to form a bubble of height <i>Z</i><sub>B</sub> at the tip of the "
        "tube as shown in Figure 31.5(d). The increase in bubble pressure, <i>P</i><sub>b</sub>, "
        "over ambient pressure, <i>P</i><sub>a</sub>, arising from the interface is given by the sum "
        "of a hydrostatic pressure and Laplace pressure:"))
    b.append(eq(
        "δ<i>p</i> = <i>P</i><sub>b</sub> − <i>P</i><sub>a</sub> − Δρ<i>gt</i> = "
        "Δρ<i>gZ</i><sub>B</sub> + 2γ/<i>b</i>", "31.7"))
    b.append(p(
        "As a new bubble begins to form, <i>Z</i><sub>B</sub> increases while <i>b</i>, the radius "
        "of curvature at the bubble apex, decreases, resulting in an increase in pressure in the "
        "bubble. Ultimately, <i>b</i> increases as the bubble grows larger, thus reducing the "
        "pressure. The pressure in the bubble thus reaches a maximum when δ<i>p</i> reaches a "
        "maximum, which in turn can be theoretically related to the surface tension. For "
        "δ<i>p</i> = δ<i>p</i><sub>max</sub>, Equation 31.7 can be rewritten in dimensionless form "
        "as follows:"))
    b.append(eq(
        "<i>r</i>/<i>X</i> = <i>r</i>/<i>b</i> + (<i>r</i>/<i>a</i>)(<i>Z</i><sub>B</sub>/<i>b</i>)"
        "(β/2)<sup>1/2</sup>", "31.8"))
    b.append(p(
        "where <i>r</i> is the tube radius, <i>X</i> is a length defined as "
        "<i>X</i> = 2γ/δ<i>p</i><sub>max</sub>, <i>a</i> is the capillary constant, and β is the "
        "Bond number. The dimensionless quantity <i>r</i>/<i>X</i> depends only on "
        "<i>r</i>/<i>a</i>, the relationship being determined by Equation 31.8 combined with "
        "numerical solutions of Equation 31.3. Tabulations of this relationship are used to "
        "calculate the surface tension by an iterative procedure (p. 18 of [1]). The standard MBPM "
        "requires a knowledge of the fluid densities, tube radius, and depth of immersion of the "
        "tube."))
    b.append(p(
        "A differential MBPM uses two tubes of different diameters immersed to the same depth. The "
        "difference in the maximum bubble pressure for the two tubes, Δ<i>P</i>, is measured, "
        "eliminating the need to know the immersion depth and making the method less sensitive to "
        "errors in the knowledge of the liquid density. For the differential MBPM, surface tension "
        "is computed from (see [5]):"))
    b.append(eq(
        "γ = <i>A</i>Δ<i>P</i> [1 + (0.69 <i>r</i><sub>2</sub>ρ<sub>L</sub>/Δ<i>P</i>)]", "31.9"))
    b.append(note(
        "<b>Translator’s note.</b> In Equation 31.9 the numerator of the correction term is printed "
        "as 0.69 <i>r</i><sub>2</sub>ρ<sub>L</sub>, with no <i>g</i>. That term has to carry the "
        "dimensions of a pressure in order to be added to Δ<i>P</i>, so it should read "
        "0.69 <i>r</i><sub>2</sub>ρ<sub>L</sub><i>g</i>. The translation keeps the printed form and "
        "records the discrepancy here."))
    b.append(p(
        "where <i>r</i><sub>2</sub> is the radius of the larger tube, ρ<sub>L</sub> is the liquid "
        "density, and <i>A</i> is an apparatus-dependent constant that is determined by calibration "
        "with several standard liquids [6]. Automated MBPM units are commercially available (see "
        "Table 31.1). Sensa Dyne manufactures differential MBPM units that allow for on-line process "
        "measurements under conditions of varying temperature and pressure."))

    b.append(h3("Pendant drop and sessile drop methods", "", "t31-giotdo"))
    b.append(p(
        "The shape of an axisymmetric pendant or sessile drop (Figure 31.4) depends on only a single "
        "parameter, the Bond number, as discussed above. The Bond number is a measure of the "
        "relative importance of gravity to surface tension in determining the shape of the drop. For "
        "Bond numbers near zero, surface tension dominates and the drop is nearly spherical. For "
        "larger Bond numbers, the drop becomes significantly deformed by gravity. In principle, the "
        "method involves obtaining an image of the drop and comparing its shape and size to "
        "theoretical profiles obtained by integrating Equation 31.3 for various values of β and "
        "<i>b</i>. Once β and <i>b</i> have been determined from shape and size comparison, the "
        "surface tension is calculated from:"))
    b.append(eq("γ = Δρ<i>g</i><i>b</i><sup>2</sup>/β", "31.10"))
    b.append(p(
        "In practice, the drop shape and size has traditionally been determined by the manual "
        "measurement of several characteristic dimensions (see Figure 31.4) of the drop from a "
        "photographic print. For pendant drops, the ratio "
        "<i>d</i><sub>s</sub>/<i>d</i><sub>e</sub> is correlated to a shape factor <i>H</i> from "
        "which surface tension is calculated (p. 27 of [3], [7]) according to:"))
    b.append(eq("γ = Δρ<i>g</i><i>d</i><sub>e</sub><sup>2</sup>/<i>H</i>", "31.11"))
    b.append(p(
        "For sessile drops, various analytical formulae are available for computation of surface "
        "tension directly from the characteristic dimensions (p. 36 of [3]). Drop shape methods "
        "based on characteristic dimensions require very accurate measurement of the dimensions for "
        "good results. For more accurate results, methods that fit the entire shape of the edge of "
        "the drop to the Laplace equation are recommended."))
    b.append(p(
        "In recent years, the entire procedure has been automated using digital imaging and computer "
        "image analysis [8, 9]. Typically, several hundred coordinates on the edge of the drop are "
        "located with subpixel resolution by computer analysis of the digital image. The size, "
        "shape, and horizontal and vertical offsets of the theoretical profile given by Equation "
        "31.3 are varied by varying four parameters: β, <i>b</i>, and the pixel coordinates of the "
        "drop apex, <i>x</i><sub>0</sub> and <i>z</i><sub>0</sub>. A best fit of the theoretical "
        "profile to the measured edge coordinates is obtained by minimizing an objective function. A "
        "digital image of a pendant drop can be analyzed for surface tension on a desktop computer "
        "in 1 or 2 s [10]. The speed of algorithms for pendant drop analysis on modern desktop "
        "computers has allowed this method to be used to track changes in surface tension for "
        "surfactant-covered surfaces by analyzing a sequence of images. The algorithms can "
        "simultaneously track the surface area and volume of the drop or bubble."))
    b.append(p(
        "Both soluble and insoluble surfactants have been studied using the pendant drop, sessile "
        "drop, pendant bubble, and captive bubble configurations [11–13]. Table 31.1 lists several "
        "manufacturers that can provide software for automated analysis of surface tension from "
        "drops or bubbles in pendant or sessile configurations. The increased accuracy and "
        "simplicity of the automated pendant drop procedure makes it a very flexible method that has "
        "been applied to measure ultralow interfacial tensions, pressure, temperature and time "
        "dependence of interfacial tension, relaxation of adsorption layers, measurement of line "
        "tensions, and film-balance measurements [14]."))

    b.append(h3("Drop weight or volume method", "", "t31-trongluong"))
    b.append(p(
        "A pendant drop will become unstable and detach from its support if it grows too large. The "
        "weight of the detached portion is related to the surface tension of the fluid by:"))
    b.append(eq("γ = (<i>mg</i>/<i>r</i>) · F(<i>r</i>/<i>V</i><sup>1/3</sup>)", "31.12"))
    b.append(p(
        "where <i>mg</i> is the weight of the detached drop, <i>r</i> is the radius of the tip from "
        "which the drop hangs, and <i>V</i> is the volume of the detached drop. An empirical "
        "correction factor, F, is tabulated as a function of "
        "<i>r</i>/<i>V</i><sup>1/3</sup> (p. 50 of [3]). For Equation 31.12 to apply, drops must be "
        "formed slowly. Measurements typically involve weighing the accumulated liquid from a large "
        "number of drops to determine the average weight per drop. The density of the fluid must be "
        "known in order to determine the drop volume and then obtain the factor F. Another method "
        "involves measuring the volumetric flow rate of liquid to the tip while counting the drops; "
        "the density of the fluid must then be known in order to determine the drop weight. The "
        "latter method allows for automation of measurements [15]."))

    b.append(h3("Spinning drop method", "", "t31-quay"))
    b.append(p(
        "The spinning drop method is a shape-measurement method similar to the pendant and sessile "
        "drop methods. However, the deformation of the drop in this case is caused by radial "
        "pressure gradients in a rapidly spinning tube. This method is normally used for measuring "
        "interfacial tensions between immiscible liquids. A horizontal glass tube with sealed ends "
        "is filled with the more dense liquid through a filling port. The tube is then spun about "
        "its axis while a drop of the lower density liquid is injected into the tube. The pressure "
        "in the outer liquid increases from the centre of the tube toward the walls as a result of "
        "the spinning motion. The pressure gradient forces the drop to move to the centre of the "
        "tube and causes it to elongate, while surface tension opposes elongation. Measurement of "
        "the maximum drop diameter, 2<i>r</i><sub>max</sub>, and length, "
        "2<i>h</i><sub>max</sub>, together with the angular velocity of rotation, Ω, allows for "
        "calculation of the surface tension according to:"))
    b.append(eq(
        "γ = ½ (<i>r</i><sub>max</sub>/<i>r</i><sup>*</sup><sub>max</sub>)<sup>3</sup> ΔρΩ<sup>2</sup>",
        "31.13"))
    b.append(p(
        "where <i>r</i><sup>*</sup><sub>max</sub> is correlated to the aspect ratio "
        "<i>r</i><sub>max</sub>/<i>h</i><sub>max</sub> [16]. The spinning drop method is "
        "particularly suited for measuring ultralow interfacial tensions "
        "(10<sup>–2</sup> mN m<sup>–1</sup> to 10<sup>–4</sup> mN m<sup>–1</sup>)."))
    return "".join(b)


# ================================================================ 31.3

def sec_31_3_vi():
    b = [h2("31.3 Các phương pháp chuyên dụng", "Specialized Methods")]

    b.append(h3("Sức căng bề mặt động", "Dynamic surface tension", "t31-dong"))
    b.append(p(
        "Trong dung dịch nước của một chất hoạt động bề mặt tan, sức căng bề mặt giảm sau khi một "
        "diện tích bề mặt mới được tạo ra, do sự hấp phụ của các phân tử chất hoạt động bề mặt. Động "
        "học hấp phụ của chất hoạt động bề mặt có thể được nghiên cứu bằng cách đo sự thay đổi sức "
        "căng bề mặt theo thời gian. Với dung dịch loãng, tốc độ thay đổi sức căng bề mặt thường đủ "
        "chậm để có thể dùng các phiên bản tự động của những phương pháp tĩnh như bản Wilhelmy hay "
        "giọt treo [17] để theo dõi sự thay đổi đó. Với dung dịch đậm đặc, nơi sức căng bề mặt có thể "
        "thay đổi lớn chỉ trong một phần nhỏ giây sau khi bề mặt được tạo ra, phải dùng phương pháp "
        "động. Một tia chất lỏng phun ra từ lỗ hình elip có những sóng dừng trên bề mặt, với bước "
        "sóng liên hệ với sức căng bề mặt. Phương pháp tia dao động đã được dùng để đo sức căng bề "
        "mặt ở tuổi bề mặt thấp tới 0,6 ms [18]. Một phiên bản động của phương pháp áp suất bọt cực "
        "đại đã được dùng để đo sức căng bề mặt động ở tuổi bề mặt xuống tới 0,1 ms [19]."))

    b.append(h3("Nhớt đàn hồi bề mặt", "Surface viscoelasticity", "t31-nhotdanhoi"))
    b.append(p(
        "Một mặt chất lỏng phủ một đơn lớp chất hoạt động bề mặt thể hiện hành vi nhớt đàn hồi. "
        "Ngoài sức căng bề mặt, lưu biến bề mặt còn được đặc trưng bằng độ đàn hồi dãn và độ đàn hồi "
        "trượt, cũng như độ nhớt dãn và độ nhớt trượt. Các tính chất dãn đặc biệt quan trọng trong "
        "nhiều tình huống, từ độ ổn định của bọt đến hoạt động của phổi người. Mô đun dãn bề mặt tỉ "
        "lệ với độ biến thiên sức căng bề mặt ứng với một độ biến thiên diện tích bề mặt cho trước. "
        "Mô đun này phụ thuộc vào tốc độ biến thiên diện tích bề mặt, với cả đơn lớp chất hoạt động "
        "bề mặt tan và không tan, điều đó cho thấy các quá trình hồi phục đang hoạt động. Những quá "
        "trình hồi phục này sinh ra độ nhớt dãn bề mặt. Với chất hoạt động bề mặt tan, một trong các "
        "quá trình hồi phục là sự hấp phụ hoặc giải hấp các phân tử ở bề mặt. Độ đàn hồi dãn cân bằng "
        "của một đơn lớp không tan có thể đo bằng cách dãn hoặc nén chậm đơn lớp trong một máng "
        "Langmuir, đồng thời theo dõi sức căng bề mặt bằng thiết bị bản Wilhelmy [20]. Nghiên cứu lưu "
        "biến bề mặt ở tốc độ dãn hoặc nén bề mặt cao cũng được quan tâm với cả chất hoạt động bề "
        "mặt tan và không tan."))
    b.append(p(
        "Sự hồi phục sức căng bề mặt sau khi bề mặt bị dãn hoặc nén đột ngột, với một chất hoạt động "
        "bề mặt tan, đã được nghiên cứu bằng phương pháp giọt treo tự động [21]. Một phương pháp gọi "
        "là đo sức căng bằng bọt dao động đã được áp dụng để đo động học hấp phụ và giải hấp của "
        "chất hoạt động bề mặt tan [22, 23]. Các phương pháp khác để nghiên cứu tính chất nhớt đàn "
        "hồi dãn động được tổng quan trong [24], gồm phương pháp sóng mao quản ngang và dọc, một "
        "phương pháp áp suất bọt cực đại cải tiến, và phương pháp bọt dao động."))

    b.append(h3("Đo ở nhiệt độ và áp suất cực đoan",
                "Measurements at extremes of temperature and pressure", "t31-cucdoan"))
    b.append(p(
        "Một số phương pháp chuẩn mô tả trong chương này có thể được thích nghi để đo sức căng bề "
        "mặt hoặc sức căng liên bề mặt ở nhiệt độ và/hoặc áp suất cực đoan. Các phương pháp phổ biến "
        "nhất để đo sức căng bề mặt của kim loại nóng chảy, hợp kim và chất bán dẫn ở nhiệt độ cao là "
        "phương pháp áp suất bọt cực đại [25] và phương pháp giọt treo hay giọt nằm [26–28]. Đo sức "
        "căng liên bề mặt giữa dầu và một pha không trộn lẫn thứ hai ở áp suất cao và nhiệt độ cao "
        "được quan tâm để hiểu một số khía cạnh của thu hồi dầu tăng cường. Phương pháp giọt treo đã "
        "được áp dụng ở áp suất 82 MPa và 449 K [29], còn phương pháp sóng mao quản đã được áp dụng "
        "ở 136 MPa và 473 K [30]. Temco Inc. (Bảng 31.2) có bán một thiết bị giọt treo cho phép đo "
        "tới 10.000 psi (69 MPa) và 350 °F (450 K)."))

    b.append(h3("Sức căng liên bề mặt", "Interfacial tension", "t31-lienbe"))
    b.append(p(
        "Đo sức căng liên bề mặt giữa hai chất lỏng không trộn lẫn có thể gặp những khó khăn riêng. "
        "Đo bằng phương pháp mao dẫn dâng, vòng du Noüy hay bản Wilhelmy là có vấn đề, vì góc tiếp "
        "xúc thường khác không. Phương pháp giọt treo [7] và trọng lượng giọt [31] đều có thể áp "
        "dụng được, miễn là khối lượng riêng của hai chất lỏng đủ khác nhau. Phương pháp giọt treo "
        "đặc biệt được dùng rộng rãi để đo sức căng liên bề mặt. Sức căng liên bề mặt có thể đo bằng "
        "một phương pháp áp suất bọt cực đại cải tiến, trong đó người ta đo áp suất cực đại trong "
        "một giọt chất lỏng bơm vào một chất lỏng không trộn lẫn thứ hai [32]. Phương pháp áp suất "
        "bọt cực đại cải tiến [32] và một phương pháp cầu chất lỏng [33] đã được dùng để đo sức căng "
        "liên bề mặt giữa hai chất lỏng có khối lượng riêng bằng nhau. Sức căng liên bề mặt cực thấp "
        "có thể đo bằng phương pháp giọt quay [34], giọt treo [35] và sóng mao quản [34]."))
    return "".join(b)


def sec_31_3_en():
    b = [h2("31.3 Specialized Methods", "")]

    b.append(h3("Dynamic surface tension", "", "t31-dong"))
    b.append(p(
        "In an aqueous solution of soluble surfactant, the surface tension decreases following "
        "creation of new surface area because of adsorption of surfactant molecules. Surfactant "
        "adsorption kinetics can be studied by measuring the change in surface tension with time. "
        "For a dilute solution, the rate of change of surface tension is often slow enough that "
        "automated versions of static methods such as the Wilhelmy plate or pendant drop [17] "
        "methods can be used to follow the changes in surface tension. In concentrated solutions in "
        "which large changes in surface tension can occur within a fraction of a second following "
        "surface creation, a dynamic method must be used. A liquid jet emerging from an elliptical "
        "orifice has stationary waves on its surface, the wavelengths of which are related to the "
        "surface tension. The oscillating jet method has been used to measure surface tension for "
        "surface ages as low as 0.6 ms [18]. A dynamic version of the maximum bubble pressure "
        "method has been used to measure dynamic surface tension at surface ages down to 0.1 ms "
        "[19]."))

    b.append(h3("Surface viscoelasticity", "", "t31-nhotdanhoi"))
    b.append(p(
        "A liquid surface covered by a monolayer of surfactant exhibits viscoelastic behaviour. In "
        "addition to surface tension, the surface rheology is characterized in terms of dilatational "
        "and shear elasticities as well as dilatational and shear viscosities. The dilatational "
        "properties in particular are important in a variety of situations, from foam stability to "
        "the functioning of the human lung. The surface dilatational modulus is proportional to the "
        "change in surface tension for a given change in surface area. This modulus depends on the "
        "rate of change of surface area for both soluble and insoluble surfactant monolayers, which "
        "indicates that relaxation processes are active. These relaxation processes give rise to the "
        "surface dilatational viscosity. For the case of soluble surfactants, one of the relaxation "
        "processes is the adsorption or desorption of molecules at the surface. The equilibrium "
        "dilatational elasticity of an insoluble monolayer can be measured by slowly expanding or "
        "compressing the monolayer in a Langmuir trough while monitoring the surface tension with a "
        "Wilhelmy plate apparatus [20]. Studies of surface rheology at high rates of surface "
        "expansion or compression are of interest for both soluble and insoluble surfactants."))
    b.append(p(
        "Surface tension relaxation following sudden expansion or compression of the surface for a "
        "soluble surfactant has been studied by the automated pendant drop method [21]. A method "
        "known as oscillating bubble tensiometry has been applied to measure the kinetics of "
        "adsorption and desorption for soluble surfactants [22, 23]. Other methods for studying "
        "dynamic dilatational viscoelastic properties are reviewed in [24], including transverse and "
        "longitudinal capillary wave methods, a modified maximum bubble pressure method, and an "
        "oscillating bubble method."))

    b.append(h3("Measurements at extremes of temperature and pressure", "", "t31-cucdoan"))
    b.append(p(
        "Several of the standard methods described in this chapter can be adapted to make surface or "
        "interfacial tension measurements at extreme temperatures and/or pressures. The most common "
        "methods used to measure the surface tension of high-temperature molten metals, alloys and "
        "semiconductors are the maximum bubble pressure method [25] and the pendant or sessile drop "
        "method [26–28]. Measurement of the interfacial tension between oil and a second immiscible "
        "phase at high pressure and elevated temperature is of interest for understanding aspects of "
        "enhanced oil recovery. The pendant drop method has been applied under pressures of 82 MPa at "
        "449 K [29], while a capillary wave method has been applied at 136 MPa and 473 K [30]. A "
        "pendant drop apparatus capable of measurements to 10,000 psi (69 MPa) and 350 °F (450 K) is "
        "commercially available from Temco Inc. (Table 31.2)."))

    b.append(h3("Interfacial tension", "", "t31-lienbe"))
    b.append(p(
        "Measurement of the interfacial tension between two immiscible liquids can present special "
        "difficulties. Measurement by the capillary rise, du Noüy ring or Wilhelmy plate method is "
        "problematic in that the contact angle is often non-zero. The pendant drop [7] and drop "
        "weight [31] methods can both be applied, provided the densities of the two liquids are "
        "sufficiently different. The pendant drop method, in particular, is widely used for "
        "interfacial tension measurement. Interfacial tension can be measured by a modified maximum "
        "bubble pressure method in which one measures the maximum pressure in a liquid drop injected "
        "into a second immiscible liquid [32]. The modified maximum bubble pressure method [32] and "
        "a liquid bridge method [33] have been used to measure interfacial tension between two "
        "liquids of equal density. Ultralow values of interfacial tension can be measured by the "
        "spinning drop [34], pendant drop [35] and capillary wave methods [34]."))
    return "".join(b)


# ================================================================ back matter

def back_vi():
    b = [h3("Định nghĩa các thuật ngữ", "Defining Terms", "t31-thuatngu")]
    b.append(defs([
        ("Sức căng bề mặt",
         "Lực trên một đơn vị dài, tác dụng tiếp tuyến với mặt chất lỏng và vuông góc với mọi đường "
         "nằm trong mặt đó."),
        ("Năng lượng bề mặt",
         "Năng lượng tự do dư trên một đơn vị diện tích gắn với mặt phân cách giữa hai pha. Với mặt "
         "lỏng–lưu, năng lượng bề mặt có trị số bằng sức căng bề mặt."),
    ]))
    b.append(h3("Lời cảm ơn", "Acknowledgments", "t31-camon"))
    b.append(p(
        "Trong thời gian chuẩn bị chương này, một trong các tác giả (DBT) được hỗ trợ một phần bởi "
        "Cơ quan Hàng không và Vũ trụ Quốc gia Hoa Kỳ (NASA) và Văn phòng Nghiên cứu Hải quân. Công "
        "trình của một trong các tác giả (KFM) được thực hiện tại Phòng Thí nghiệm Sức đẩy Phản lực, "
        "Viện Công nghệ California, theo hợp đồng với NASA."))
    b.append(h3("Tài liệu tham khảo", "References", "t31-tltk"))
    b.append(wl(_refs31("vi")))
    return "".join(b)


def back_en():
    b = [h3("Defining Terms", "", "t31-thuatngu")]
    b.append(defs([
        ("Surface tension",
         "A force per unit length that acts tangential to a liquid surface and perpendicular to any "
         "line that lies within the surface."),
        ("Surface energy",
         "The excess free energy per unit area associated with a surface between two phases. For a "
         "liquid–fluid surface, the surface energy is numerically equivalent to the surface "
         "tension."),
    ]))
    b.append(h3("Acknowledgments", "", "t31-camon"))
    b.append(p(
        "During the preparation of this chapter, one of us (DBT) was supported in part by the "
        "National Aeronautics and Space Administration (NASA) and by the Office of Naval Research. "
        "The work by one of us (KFM) was performed at the Jet Propulsion Laboratory, California "
        "Institute of Technology, under contract with NASA."))
    b.append(h3("References", "", "t31-tltk"))
    b.append(wl(_refs31("en")))
    return "".join(b)


SECTIONS_VI = [sec_31_1_vi, sec_31_2_vi, sec_31_3_vi]
SECTIONS_EN = [sec_31_1_en, sec_31_2_en, sec_31_3_en]

# The source numbers three sections and gives the methods under §31.2 and §31.3 as
# named sub-topics with no numbers of their own. The index lists the three sections
# with their numbers and hangs the sub-topics under them unnumbered.
INDEX = [
    ("31.1", "Cơ học của mặt chất lưu", "Mechanics of Fluid Surfaces", "s31-1", [
        ("Mô hình cơ học và năng lượng bề mặt", "The mechanical model and surface energy", "t31-mohinh"),
        ("Hình dạng và chất hoạt động bề mặt", "Shape, and surface-active agents", "t31-hinhdang"),
        ("Đường tiếp xúc và góc tiếp xúc", "The contact line and the contact angle", "t31-tiepxuc"),
        ("Cân bằng tại đường tiếp xúc", "Equilibrium at the contact line", "t31-canhbang"),
        ("Mặt cong và áp suất Laplace", "Curved surfaces and the Laplace pressure", "t31-laplace"),
        ("Giọt và bọt đối xứng trục", "Axisymmetric drops and bubbles", "t31-giot"),
        ("Sóng mao quản", "Capillary waves", "t31-song"),
    ]),
    ("31.2", "Các phương pháp và thiết bị chuẩn", "Standard Methods and Instrumentation", "s31-2", [
        ("Phương pháp mao dẫn dâng", "Capillary rise method", "t31-maodan"),
        ("Bản Wilhelmy và vòng du Noüy", "Wilhelmy plate and du Noüy ring methods", "t31-wilhelmy"),
        ("Áp suất bọt cực đại", "Maximum bubble pressure method", "t31-bot"),
        ("Giọt treo và giọt nằm", "Pendant drop and sessile drop methods", "t31-giotdo"),
        ("Trọng lượng hoặc thể tích giọt", "Drop weight or volume method", "t31-trongluong"),
        ("Giọt quay", "Spinning drop method", "t31-quay"),
    ]),
    ("31.3", "Các phương pháp chuyên dụng", "Specialized Methods", "s31-3", [
        ("Sức căng bề mặt động", "Dynamic surface tension", "t31-dong"),
        ("Nhớt đàn hồi bề mặt", "Surface viscoelasticity", "t31-nhotdanhoi"),
        ("Đo ở nhiệt độ và áp suất cực đoan", "Measurements at extremes of temperature and pressure",
         "t31-cucdoan"),
        ("Sức căng liên bề mặt", "Interfacial tension", "t31-lienbe"),
    ]),
]


def sec_index(lang):
    """The in-page jump index: three numbered sections with their sub-topics hung
    underneath, indented and unnumbered, since the source gives them no numbers."""
    vi = lang == "vi"
    li = []
    for num, tvi, ten, anchor, subs in INDEX:
        li.append('<li><span class="n">%s</span><span class="t"><a href="#%s">%s</a></span></li>'
                  % (num, anchor, tvi if vi else ten))
        for stvi, sten, sanchor in subs:
            li.append('<li style="margin-left:2.4rem;font-size:.9rem;padding:.15rem 0">'
                      '<span class="t"><a href="#%s">%s</a></span></li>'
                      % (sanchor, stvi if vi else sten))
    return ('<ul class="toc-list sec-index" aria-label="%s">%s</ul>'
            % ("Mục lục trong chương" if vi else "Contents of this chapter", "".join(li)))


def body_vi():
    out = ['<p class="lede">Sức căng bề mặt là lực trên một đơn vị dài kéo căng mặt thoáng của chất '
           'lỏng — thứ làm giọt nước căng tròn, cho chiếc kim thép nổi trên mặt nước và khiến vòi '
           'nước rỉ nhỏ giọt. Chương này đi từ cơ học của mặt chất lưu, qua mười ba công thức đo, '
           'đến các thiết bị thương mại dùng cho từng phương pháp.</p>',
           sec_index("vi")]
    for f in SECTIONS_VI:
        out.append(f())
    out.append(back_vi())
    return "".join(out)


def body_en():
    out = ['<p class="lede">Surface tension is the force per unit length that holds a liquid surface '
           'taut — it rounds a droplet, floats a steel needle, and makes a leaking tap drip. This '
           'chapter runs from the mechanics of fluid surfaces, through the thirteen working '
           'equations of measurement, to the commercial instruments that implement each method.</p>',
           sec_index("en")]
    for f in SECTIONS_EN:
        out.append(f())
    out.append(back_en())
    return "".join(out)


def build(lang):
    vi = lang == "vi"
    switch = ("%s%s/" % (BASE_EN, CSLUG)) if vi else ("%s%s/" % (BASE_VI, CSLUG))
    title = ("Chương 31 — %s · Sổ tay Đo lường, Thiết bị đo và Cảm biến" % TITLE_VI if vi
             else "Chapter 31 — %s · Measurement, Instrumentation and Sensors Handbook" % TITLE_EN)
    desc = ("Bản dịch tiếng Việt Chương 31 “Đo sức căng bề mặt” của David B. Thiessen và Kin F. Man — "
            "cơ học mặt chất lưu, phương trình Young–Laplace, và mười ba công thức đo sức căng bề "
            "mặt cùng thiết bị cho từng phương pháp." if vi
            else
            "Companion to Chapter 31 of the CRC Measurement Handbook — the mechanics of fluid "
            "surfaces, the Young–Laplace equation, and thirteen working equations for measuring "
            "surface tension, with the instruments that implement each one.")
    crumb = ('<a href="/vi/books/">Sách</a> · <a href="%s">Sổ tay Đo lường, Thiết bị đo và Cảm biến</a> · '
             'Chương 31' % BASE_VI if vi else
             '<a href="/books/">Books</a> · <a href="%s">Measurement, Instrumentation and Sensors '
             'Handbook</a> · Chapter 31' % BASE_EN)
    # Recount these whenever a section is added: the meta line is the only place
    # the reader is told how big the chapter is, and a stale count is the kind of
    # error nobody notices until they have read the whole thing.
    meta = ("Chương 31 · theo Ch31.pdf (CRC Press, 1999) · 5 hình, 13 phương trình, 2 bảng" if vi else
            "Chapter 31 · 5 figures, 13 equations, 2 tables")
    body = ('<main><article class="intranet-content reader"><div class="reader-hero">'
            '<div class="breadcrumb">%s</div><h1>%s</h1><p class="byline">%s</p>'
            '<div class="meta-line">%s</div></div><div class="prose">%s</div>%s</article></main>'
            % (crumb, TITLE_VI if vi else TITLE_EN, BYLINE, meta,
               body_vi() if vi else body_en(), chapter_nav(lang, 31)))
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
