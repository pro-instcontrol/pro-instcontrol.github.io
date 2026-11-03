# -*- coding: utf-8 -*-
"""Handbook Chapter 32 — Temperature (Robert J. Sandberg, ed.)

The chapter is 163 source pages and eleven sections, each contributed by a
different author. Sections are being written in order; §32.1 is complete.

  §32.1  Bimaterials Thermometers            p3-14    6 figs  19 eqs  5 tables
  §32.2  Resistive Thermometers              p14-25
  §32.3  Thermistor Thermometers             p26-41
  §32.4  Thermocouple Thermometers           p42-74
  §32.5  Semiconductor Junction Thermometers p75-87
  §32.6  Infrared Thermometers               p88-109
  §32.7  Pyroelectric Thermometers           p110-117
  §32.8  Liquid-in-Glass Thermometers        p118-129
  §32.9  Manometric Thermometers             p130-136
  §32.10 Temperature Indicators              p137-152
  §32.11 Fiber-Optic Thermometers            p153-163

Run:  python build/reader_hb_ch32.py            (writes the two pages)
      python build/reader_hb_ch32.py <path>     (writes a preview elsewhere)
"""
import os
import sys

import hb32fig as F
from reader_handbook import SLUG, head, header, footer
from chapter_nav import nav as chapter_nav

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSLUG = "ch32-temperature"
TITLE_EN = "Temperature"
TITLE_VI = "Đo nhiệt độ"
BYLINE = "Robert J. Sandberg"
BASE_EN = "/books/read/%s/" % SLUG
BASE_VI = "/vi/books/read/%s/" % SLUG
PREV_EN = "ch31-surface-tension-measurement"
PREV_VI = "ch31-surface-tension-measurement"
PREV_T_EN = "Surface Tension Measurement"
PREV_T_VI = "Đo sức căng bề mặt"


# ------------------------------------------------------------------ helpers
def fig(num, key, lang="vi"):
    svg, cap_vi, cap_en, aria_vi, aria_en = key
    if lang == "vi":
        cap = cap_vi
    else:
        cap = cap_en
        # The <svg> tag is built once, in hb32fig, with a Vietnamese aria-label
        # baked in by hbfig.svg(). Swap it for the English one, otherwise a
        # screen reader on the English page announces Vietnamese.
        k = svg.find('aria-label="')
        if k >= 0:
            a = k + len('aria-label="')
            b = svg.find('"', a)
            svg = svg[:a] + (aria_en or aria_vi) + svg[b:]
    return ('<figure class="figure" id="fig-32-%d">%s'
            '<figcaption class="figcap">%s</figcaption></figure>' % (num, svg, cap))


def p(t):
    return "<p>%s</p>" % t


def h2(t, en="", anchor=None):
    if en == t:
        en = ""
    sid = ""
    if anchor:
        sid = ' id="%s"' % anchor
    elif t.startswith("32."):
        head_ = t[3:].split(" ", 1)[0]
        if head_.isdigit():
            sid = ' id="s32-%s"' % head_
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


def table(hd, rows, cap, cls="tbl", widths=None, small=False):
    """rows may contain, besides lists of cells, a bare string: that becomes a
    full-width group heading. Without the colspan the heading sits in the first
    column and leaves the rest of the row looking like a hole."""
    out = []
    for r in rows:
        if isinstance(r, str):
            out.append('<tr><td colspan="%d">%s</td></tr>' % (len(hd), r))
        else:
            out.append("<tr>%s</tr>" % "".join("<td>%s</td>" % c for c in r))
    body = "".join(out)
    ths = "".join('<th%s>%s</th>' % ((' style="width:%s"' % widths[i]) if widths else "", h)
                  for i, h in enumerate(hd))
    style = ' style="font-size:.84rem"' if small else ""
    return ('<div class="table-wrap"><table class="%s"%s><thead><tr>%s</tr></thead><tbody>%s</tbody>'
            '</table></div><p style="font-size:.84rem;color:#888;font-style:italic">%s</p>'
            % (cls, style, ths, body, cap))


def defs(items):
    """Defining-terms block, rendered as a two-column table so it inherits the
    reader's .tbl styling — there is no .deflist rule in library.css."""
    rows = "".join('<tr><th scope="row" style="text-align:left;width:30%%">%s</th><td>%s</td></tr>'
                   % (k, v) for k, v in items)
    return ('<div class="table-wrap"><table class="tbl"><tbody>%s</tbody></table></div>' % rows)


def authors(vi, en):
    return ('<p class="byline" style="font-size:.92rem;margin:-.2rem 0 1.6rem">%s</p>'
            % (vi if vi else en))


# ================================================================ table data

def _t321(lang):
    """Table 32.1 — properties of the materials used in bimaterial elements.
    Some rows carry two sets of figures, one from each source; both are kept,
    because the difference between them is larger than the rounding."""
    vi = lang == "vi"
    hd = (["Vật liệu", "Khối lượng riêng ρ<br>(kg m⁻³)", "Môđun Young E<br>(GPa)",
           "Nhiệt dung C<br>(J kg⁻¹ K⁻¹)", "Giãn nở nhiệt<br>(10⁻⁶ K⁻¹)",
           "Dẫn nhiệt<br>(W m⁻¹ K⁻¹)"] if vi else
          ["Material", "Density ρ<br>(kg m⁻³)", "Young's modulus E<br>(GPa)",
           "Heat capacity C<br>(J kg⁻¹ K⁻¹)", "Thermal expansion<br>(10⁻⁶ K⁻¹)",
           "Thermal conductivity<br>(W m⁻¹ K⁻¹)"])
    rows = [
        ("Al", "2700ᶜ", "61–71ᵇ", "896ᵃ", "24ᵇ", "237ᶜ"),
        ("", "2707ᵃ", "70.6ᶜ", "900ᶜ", "23.5ᶜ", "204ᵃ"),
        ("Cu", "8954ᵃ", "129.8ᶜ", "383.1ᵃ", "17.0ᶜ", "386ᵃ"),
        ("", "8960ᶜ", "—", "385ᶜ", "—", "401ᶜ"),
        ("Cr", "7100ᶜ", "279ᶜ", "518ᶜ", "6.5ᶜ", "94ᶜ"),
        ("Au", "19300ᵇ,ᶜ", "78.5ᵇ,ᶜ", "129ᵇ,ᶜ", "14.1ᵇ,ᶜ", "318ᵇ,ᶜ"),
        ("Fe", "7870ᶜ", "211.4ᶜ", "444ᶜ", "12.1ᶜ", "80.4ᶜ"),
        ("Ni", "8906ᵃ", "199.5ᶜ", "446ᵃ", "13.3ᶜ", "90ᵃ"),
        ("", "8900ᶜ", "—", "444ᶜ", "—", "90.9ᶜ"),
        ("Ag", "10524ᵃ", "82.7ᶜ", "234.0ᵃ", "19.1ᶜ", "419ᵃ"),
        ("", "10500ᶜ", "—", "237ᶜ", "—", "429ᶜ"),
        ("Sn", "7304ᵃ", "49.9ᶜ", "226.5ᵃ", "23.5ᶜ", "64ᵃ"),
        ("", "7280ᶜ", "—", "213ᶜ", "—", "66.8ᶜ"),
        ("Ti", "4500ᶜ", "120.2ᶜ", "523ᶜ", "8.9ᶜ", "21.9ᶜ"),
        ("W", "19350ᵃ", "411ᶜ", "134.4ᵃ", "4.5ᶜ", "163ᵃ"),
        ("", "19300ᶜ", "—", "133ᶜ", "—", "173ᶜ"),
        ("Invar (Fe64/Ni36)", "8000ᶜ", "140–150ᶜ", "—", "1.7–2.0ᶜ", "13ᶜ"),
        ("Si", "2340ᶜ", "113ᶜ", "703ᶜ", "4.7–7.6ᶜ", "80–150ᶜ"),
        ("n-Si", "2328ᵇ", "130–190ᵇ", "700ᵇ", "2.6ᵇ", "150ᵇ"),
        ("p-Si", "2300ᵇ", "150–170ᵇ", "770ᵇ", "—", "30ᵇ"),
        ("Si₃N₄", "3100ᵃ", "304ᵇ", "600–800ᵇ", "3.0ᵇ", "9–30ᵇ"),
        ("SiO₂", "2200ᵇ", "57–85ᵇ", "730ᵇ", "0.50ᵇ", "1.4ᵇ"),
    ]
    cap = ("Bảng 32.1 · Tính chất của một số vật liệu dùng trong phần tử lưỡng kim. ᵃ Từ tài liệu "
           "[13], Bảng A1 ở 20 °C. ᵇ Từ tài liệu [13], Bảng A2 ở 300 K. ᶜ Từ catalogue Goodfellow "
           "1995/1996 [14]." if vi else
           "Table 32.1 · Properties of selected materials used in bimaterial elements. ᵃ From "
           "Reference [13], Table A1 at 20 °C. ᵇ From Reference [13], Table A2 at 300 K. ᶜ From "
           "Goodfellow catalog 1995/1996 [14].")
    return table(hd, rows, cap, widths=["20%", "16%", "16%", "16%", "16%", "16%"], small=True)


def _t322(lang):
    """Table 32.2 — ASTM thermostatic elements. Each element lists flexivity at
    two reference ranges, hence the two-row groups."""
    vi = lang == "vi"
    hd = (["Loại (ASTM)", "Độ uốn 10⁻⁶ (°C⁻¹)", "Dải nhiệt độ ứng suất cực đại (°C)",
           "Nhiệt độ làm việc cực đại (°C)", "Môđun Young (GPa)"] if vi else
          ["Type (ASTM)", "Flexivity 10⁻⁶ (°C⁻¹)", "Max. sensitivity temp. range (°C)",
           "Max. operating temp. (°C)", "Young's modulus (GPa)"])
    rows = [
        ("TM1", "27.0 ± 5%ᵃ<br>26.3 ± 5%ᵇ", "−18–149", "538", "17.2"),
        ("TM2", "38.7 ± 5%ᵃ<br>38.0 ± 5%ᵇ", "−18–204", "260", "13.8"),
        ("TM5", "11.3 ± 6%ᵃ<br>11.5 ± 6%ᵇ", "149–454", "538", "17.6"),
        ("TM10", "23.6 ± 6%ᵃ<br>22.9 ± 6%ᵇ", "−18–149", "482", "17.9"),
        ("TM15", "26.6 ± 5.5%ᵃ<br>25.9 ± 5.5%ᵇ", "−18–149", "482", "17.2"),
        ("TM20", "25.0 ± 5%ᵃ<br>25.0 ± 5%ᵇ", "−18–149", "482", "17.2"),
    ]
    cap = ("Bảng 32.2 · Một số phần tử nhiệt lưỡng kim ASTM bán trên thị trường. ᵃ 10–93 °C. "
           "ᵇ 38–149 °C. Cả hai theo ASTM Designation B 388 [15]." if vi else
           "Table 32.2 · Selected industrially available ASTM thermostatic elements. ᵃ 10–93 °C. "
           "ᵇ 38–149 °C. Both from ASTM Designation B 388 [15].")
    return table(hd, rows, cap, widths=["14%", "26%", "24%", "20%", "16%"], small=True)


def _t323(lang):
    """Table 32.3 — composition of the ASTM elements in Table 32.2."""
    vi = lang == "vi"
    hd = (["", "Nguyên tố", "TM1", "TM2", "TM5", "TM10", "TM15", "TM20"] if vi else
          ["", "Element", "TM1", "TM2", "TM5", "TM10", "TM15", "TM20"])
    rows = [
        ("<b>Thành phần lớp giãn nở mạnh (% khối lượng)</b>" if vi else
         "<b>High-expansive material, chemical composition (% weight)</b>"),
        ("", "Niken" if vi else "Nickel", "22", "10", "25", "22", "22", "18"),
        ("", "Crom" if vi else "Chromium", "3", "72", "8.5", "3", "3", "11.5"),
        ("", "Mangan" if vi else "Manganese", "—", "18", "—", "—", "—", "—"),
        ("", "Đồng" if vi else "Copper", "—", "—", "—", "—", "—", "—"),
        ("", "Sắt" if vi else "Iron", "75", "—", "66.5", "75", "75", "70.5"),
        ("", "Nhôm" if vi else "Aluminum", "—", "—", "—", "—", "—", "—"),
        ("", "Cacbon" if vi else "Carbon", "—", "—", "—", "—", "—", "—"),
        ("<b>Lớp niken trung gian</b>" if vi else "<b>Intermediate nickel layer</b>",
         "", "Không" if vi else "No", "Không" if vi else "No", "Không" if vi else "No",
         "Có" if vi else "Yes", "Có" if vi else "Yes", "Không" if vi else "No"),
        ("<b>Thành phần lớp giãn nở yếu (% khối lượng)</b>" if vi else
         "<b>Low-expansive material, chemical composition (% weight)</b>"),
        ("", "Niken" if vi else "Nickel", "36", "36", "50", "36", "36", "36"),
        ("", "Sắt" if vi else "Iron", "64", "64", "50", "64", "64", "64"),
        ("", "Coban" if vi else "Cobalt", "—", "—", "—", "—", "—", "—"),
        ("<b>Tỉ lệ thành phần (% chiều dày)</b>" if vi else
         "<b>Component ratio (% of thickness)</b>"),
        ("", "Lớp giãn nở mạnh" if vi else "High", "50", "53", "50", "34", "47", "50"),
        ("", "Lớp trung gian" if vi else "Intermediate", "—", "—", "—", "32", "6", "—"),
        ("", "Lớp giãn nở yếu" if vi else "Low", "50", "47", "50", "34", "47", "50"),
    ]
    cap = ("Bảng 32.3 · Thành phần của các phần tử nhiệt ASTM trong Bảng 32.2. Theo ASTM "
           "Designation B 388 [15]." if vi else
           "Table 32.3 · Composition of the ASTM thermostatic elements given in Table 32.2. "
           "From ASTM Designation B 388 [15].")
    return table(hd, rows, cap, widths=["34%", "16%", "8.3%", "8.3%", "8.3%", "8.3%", "8.3%", "8.3%"],
                 small=True)


def _t324(lang):
    """Table 32.4 — DIN thermostatic elements."""
    vi = lang == "vi"
    hd = (["Loại (DIN)", "Độ võng riêng (10⁻⁶ K⁻¹)", "Độ cong riêng (10⁻⁶ K⁻¹) ± 5%",
           "Dải tuyến tính (°C)", "Nhiệt độ làm việc cực đại (°C)"] if vi else
          ["Type (DIN)", "Specific deflection (10⁻⁶ K⁻¹)", "Specific curvature (10⁻⁶ K⁻¹) ± 5%",
           "Linear range (°C)", "Max. operating temperature (°C)"])
    rows = [
        ("TB0965", "9.8", "18.6", "−20–425", "450"),
        ("TB1075", "10.8", "20.0", "−20–200", "550"),
        ("TB1170A", "11.7", "22.0", "−20–380", "450"),
        ("TB1577A", "15.5", "28.5", "−20–200", "450"),
        ("TB20110", "20.8", "39.0", "−20–200", "350"),
    ]
    cap = ("Bảng 32.4 · Một số phần tử nhiệt lưỡng kim DIN bán trên thị trường. Theo tiêu chuẩn "
           "DIN 1715 [4]. Độ võng riêng và độ cong riêng ứng với khoảng 20 °C đến 130 °C." if vi else
           "Table 32.4 · Selected industrially available DIN thermostatic elements. From DIN 1715 "
           "[4]. Specific deflection and curvature are for the range 20 °C to 130 °C.")
    return table(hd, rows, cap, widths=["16%", "22%", "24%", "18%", "20%"], small=True)


def _t325(lang):
    """Table 32.5 — composition of the DIN elements in Table 32.4."""
    vi = lang == "vi"
    hd = (["", "Nguyên tố", "TB0965", "TB1075", "TB1170A", "TB1577A", "TB20110"] if vi else
          ["", "Element", "TB0965", "TB1075", "TB1170A", "TB1577A", "TB20110"])
    rem = "Còn lại" if vi else "Remainder"
    rows = [
        ("<b>Thành phần lớp giãn nở mạnh (% khối lượng)</b>" if vi else
         "<b>High-expansive chemical composition (% mass)</b>"),
        ("", "Niken" if vi else "Nickel", "20", "16", "20", "20", "10–16"),
        ("", "Crom" if vi else "Chromium", "—", "11", "—", "—", "—"),
        ("", "Mangan" if vi else "Manganese", "6", "—", "6", "6", rem),
        ("", "Đồng" if vi else "Copper", "—", "—", "—", "—", "18–10"),
        ("", "Sắt" if vi else "Iron", rem, rem, rem, rem, "0.5"),
        ("", "Cacbon" if vi else "Carbon", "—", "—", "—", "—", "—"),
        ("<b>Thành phần lớp giãn nở yếu (% khối lượng)</b>" if vi else
         "<b>Low-expansive chemical composition (% mass)</b>"),
        ("", "Niken" if vi else "Nickel", "46", "20", "42", "36", "36"),
        ("", "Sắt" if vi else "Iron", rem, rem, rem, rem, rem),
        ("", "Coban" if vi else "Cobalt", "—", "26", "—", "—", "—"),
        ("", "Crom" if vi else "Chromium", "—", "8", "—", "—", "—"),
    ]
    cap = ("Bảng 32.5 · Thành phần của các phần tử nhiệt DIN trong Bảng 32.4. Theo tiêu chuẩn "
           "DIN 1715 [4]." if vi else
           "Table 32.5 · Composition of the DIN thermostatic elements given in Table 32.4. From "
           "DIN 1715 Standard [4].")
    return table(hd, rows, cap, widths=["34%", "16%", "10%", "10%", "10%", "10%", "10%"], small=True)


# ================================================================ §32.1
def sec_32_1_vi():
    b = [h2("32.1 Đo nhiệt độ bằng lưỡng kim", "Bimaterials Thermometers", anchor="s32-1")]
    b.append(authors("Robert J. Stephenson, Armelle M. Moulin và Mark E. Welland", ""))

    b.append(p(
        "Lần đầu tiên người ta dùng sự giãn nở nhiệt khác nhau của kim loại trong một cơ cấu máy "
        "là vào năm 1735, với thợ đồng hồ người Anh John Harrison. Harrison ghép hai kim loại khác "
        "nhau trong bộ thoát của đồng hồ để bù lại sự thay đổi nhiệt độ trên tàu. Chiếc đồng hồ hải "
        "hành đầu tiên ấy dùng một lưới (gridiron) hai kim loại làm thay đổi chu kỳ của bánh đà chỉ "
        "bằng một dịch chuyển đơn giản. Chính tác động cơ học sinh ra từ độ giãn nở nhiệt khác nhau "
        "của hai kim loại tiếp xúc nhau ấy là cơ sở cho mọi phần tử lưỡng kim ngày nay."))
    b.append(p(
        "Hiệu ứng lưỡng kim hiện được dùng trong vô số ứng dụng, từ thiết bị gia dụng đến bù trừ "
        "trên vệ tinh. Có hai cách dùng: hoặc như một cơ cấu chấp hành, hoặc như một hệ đo nhiệt độ. "
        "Một cơ cấu chấp hành lưỡng kim thiết yếu gồm hai dải kim loại gắn chặt vào nhau. Nếu hai "
        "kim loại có độ giãn nở khác nhau thì khi nhiệt độ thay đổi, một lớp giãn nhiều hơn lớp kia "
        "và làm thiết bị cong ra khỏi mặt phẳng. Độ cong cơ học này có thể dùng để đóng mở một công "
        "tắc điện cơ, hoặc chính nó là một phần của mạch điện, sao cho khi phần tử lưỡng kim chạm "
        "vào một điện cực thì mạch được nối. Tuy dạng đơn giản nhất chỉ là hai miếng kim loại phẳng, "
        "trong thực tế người ta dùng rất nhiều hình dạng khác nhau để đạt được độ dịch chuyển lớn "
        "nhất hoặc lực lớn nhất trong một chu trình nhiệt."))
    b.append(p(
        "Khi dùng làm thiết bị đo nhiệt độ, phần tử lưỡng kim — thiết kế giống cơ cấu chấp hành nói "
        "trên — có thể xác định nhiệt độ môi trường nếu đo được độ cong. Ưu điểm của hệ này là độ "
        "cong có thể khuếch đại bằng cơ khí để tạo ra một dịch chuyển lớn và vì thế dễ đo. Hình 32.1 "
        "trình bày nguyên lý cơ bản của một cơ cấu chấp hành lưỡng kim: hai dải kim loại có độ giãn "
        "nở nhiệt khác nhau được gắn chặt với nhau. Khi nhiệt độ của cụm thay đổi, nếu không có "
        "ngoại lực, cơ cấu sẽ có dạng một cung tròn. Tổng dịch chuyển ra khỏi mặt phẳng của hai dải "
        "lớn hơn nhiều so với độ giãn riêng của từng kim loại."))
    b.append(fig(1, F.fig(1), "vi"))
    b.append(p(
        "Để độ cong là lớn nhất, người ta thường chọn hai kim loại hay hợp kim có hệ số giãn nở "
        "nhiệt rất khác nhau. Kim loại có độ giãn nở lớn hơn gọi là <b>phần tử hoạt động</b>, kim "
        "loại có hệ số nhỏ hơn gọi là <b>phần tử thụ động</b>. Để có tác động cực đại, phần tử thụ "
        "động thường là hợp kim sắt–niken Invar, gần như không giãn nở nhiệt (thực tế từ 0,1 đến "
        "1 × 10⁻⁶ K⁻¹ tùy thành phần). Phần tử hoạt động khi đó được chọn sao cho độ giãn nở nhiệt "
        "là lớn nhất trong giới hạn của môi trường làm việc và giá thành."))
    b.append(p(
        "Ngoài việc tối đa hóa độ dịch chuyển, người ta còn đặt ra các ràng buộc về độ dẫn điện và "
        "độ dẫn nhiệt. Khi đó người ta đưa vào một lớp kim loại thứ ba bằng đồng hoặc niken, kẹp "
        "giữa lớp hoạt động và lớp thụ động, để tăng cả độ dẫn điện lẫn độ dẫn nhiệt của cơ cấu. "
        "Điều này đặc biệt quan trọng khi cơ cấu là một phần của mạch điện và phải cho dòng điện đi "
        "qua, ngoài chức năng cảm biến nhiệt độ."))

    # ---------------------------------------------------------- Basic Equations
    b.append(h3("Dải lưỡng kim thẳng", "Linear Bimaterial Strip"))
    b.append(h3("Các phương trình cơ bản", "Basic Equations"))
    b.append(p(
        "Việc phân tích phân bố ứng suất và độ võng của một dải lưỡng kim lý tưởng được Timoshenko "
        "đưa ra đầu tiên [1], bằng một cách dẫn đơn giản từ lý thuyết đàn hồi. Hình 32.2 trình bày "
        "các nội lực và mômen gây uốn trong dải, cùng phân bố ứng suất lý tưởng trong dầm. Lý "
        "thuyết này xây dựng cho dải lưỡng kim, nhưng áp dụng được như nhau cho dải hai vật liệu "
        "bất kỳ."))
    b.append(p(
        "Phương trình tổng quát cho bán kính cong của một dải lưỡng kim được nung nóng đều từ "
        "<i>T</i>₀ đến <i>T</i>, trong điều kiện không có ngoại lực, là [1]:"))
    b.append(eq("1/<i>R</i> − 1/<i>R</i><sub>0</sub> = "
                "6(1+<i>m</i>)²(α<sub>2</sub> − α<sub>1</sub>)(<i>T</i> − <i>T</i><sub>0</sub>) / "
                "{<i>t</i>[3(1+<i>m</i>)² + (1+<i>mn</i>)(<i>m</i>² + 1/(<i>mn</i>))]}", "32.1"))
    b.append(wl([
        "1/<i>R</i><sub>0</sub> = độ cong ban đầu của dải ở nhiệt độ <i>T</i><sub>0</sub>",
        "α<sub>1</sub> và α<sub>2</sub> = hệ số giãn nở của hai lớp: (1) vật liệu giãn nở yếu và "
        "(2) vật liệu giãn nở mạnh",
        "<i>n</i> = <i>E</i><sub>1</sub>/<i>E</i><sub>2</sub>, với <i>E</i><sub>1</sub> và "
        "<i>E</i><sub>2</sub> là môđun Young tương ứng",
        "<i>m</i> = <i>t</i><sub>1</sub>/<i>t</i><sub>2</sub>, với <i>t</i><sub>1</sub> và "
        "<i>t</i><sub>2</sub> là chiều dày tương ứng",
        "<i>t</i> = <i>t</i><sub>1</sub> + <i>t</i><sub>2</sub> là chiều dày của dải",
    ]))
    b.append(p("Chiều rộng của dải được lấy bằng đơn vị."))
    b.append(p(
        "Phương trình 32.1 áp dụng cho nhiều cấu hình dải khác nhau, kể cả dải gối tựa đơn giản và "
        "dải kẹp chặt một đầu (tức côngxôn). Với một cấu hình cho trước, độ võng xác định được từ "
        "quan hệ hình học của nó với độ cong 1/<i>R</i>."))
    b.append(fig(2, F.fig(2), "vi"))
    b.append(p(
        "Một ví dụ tính độ võng là dải lưỡng kim gối tựa đơn giản ở hai đầu. Độ cong ban đầu "
        "1/<i>R</i><sub>0</sub> được giả thiết bằng không. Hình 32.3 cho quan hệ hình học giữa bán "
        "kính <i>R</i> của dải và độ võng <i>d</i> ở giữa nhịp:"))
    b.append(eq("(<i>R</i> − <i>t</i><sub>2</sub>)² = "
                "(<i>R</i> − <i>d</i> − <i>t</i><sub>2</sub>)² + (<i>L</i>/2)²", "32.2"))
    b.append(p("Suy ra:"))
    b.append(eq("1/<i>R</i> = 8<i>d</i> / (<i>L</i>² + 4<i>d</i>² + 8<i>dt</i><sub>2</sub>)", "32.3"))
    b.append(p(
        "Nếu giả thiết độ võng và chiều dày đều nhỏ hơn 10% chiều dài dải — điều đúng trong hầu hết "
        "các trường hợp thực tế — thì các số hạng 8<i>dt</i><sub>2</sub> và 4<i>d</i>² là không đáng "
        "kể và biểu thức rút gọn thành:"))
    b.append(eq("<i>d</i> = <i>L</i>² / (8<i>R</i>)", "32.4"))
    b.append(p("Kết hợp với Phương trình 32.1 ta được:"))
    b.append(eq("<i>d</i> = <i>L</i>² · 3(1+<i>m</i>)² / "
                "{4<i>t</i>[3(1+<i>m</i>)² + (1+<i>mn</i>)(<i>m</i>² + 1/(<i>mn</i>))]} · "
                "(α<sub>2</sub> − α<sub>1</sub>)(<i>T</i> − <i>T</i><sub>0</sub>)", "32.5"))
    b.append(p(
        "Với một dải dài 100 mm gồm hai lớp dày bằng nhau (0,5 mm), lớp giãn nở mạnh bằng sắt "
        "(theo Bảng 32.1, <i>E</i><sub>2</sub> = 211 GPa và α<sub>2</sub> = 12,1 × 10⁻⁶ K⁻¹), lớp "
        "giãn nở yếu bằng Invar (<i>E</i><sub>1</sub> = 140 GPa và α<sub>1</sub> = 1,7 × 10⁻⁶ K⁻¹), "
        "và nhiệt độ tăng từ 20 °C lên 120 °C, độ võng lý thuyết ở giữa dải sẽ là 1,92 mm."))
    b.append(p(
        "Ví dụ thứ hai xét độ võng ở đầu tự do của một dải côngxôn lưỡng kim như Hình 32.4. Khi đó "
        "quan hệ hình học là:"))
    b.append(eq("(<i>R</i> + <i>t</i><sub>1</sub>)² = "
                "(<i>R</i> + <i>t</i><sub>1</sub> − <i>d</i>)² + <i>L</i>²", "32.6a"))
    b.append(p("hay"))
    b.append(eq("1/<i>R</i> = 2<i>d</i> / (<i>L</i>² + <i>d</i>² − 2<i>dt</i><sub>1</sub>)", "32.6b"))
    b.append(p(
        "Với cùng các giả thiết như trên, tức <i>d</i>² « <i>L</i>² và <i>dt</i><sub>1</sub> « "
        "<i>L</i>², độ võng ở đầu tự do là:"))
    b.append(eq("<i>d</i> = <i>L</i>² / (8<i>R</i>)", "32.7"))
    b.append(fig(3, F.fig(3), "vi"))
    b.append(fig(4, F.fig(4), "vi"))
    b.append(p("Kết hợp với Phương trình 32.1 cho:"))
    b.append(eq("<i>d</i> = <i>L</i>² · 3(1+<i>m</i>)² / "
                "{<i>t</i>[3(1+<i>m</i>)² + (1+<i>mn</i>)(<i>m</i>² + 1/(<i>mn</i>))]} · "
                "(α<sub>2</sub> − α<sub>1</sub>)(<i>T</i> − <i>T</i><sub>0</sub>)", "32.8"))
    b.append(p(
        "Nếu xét một côngxôn vi mô hai vật liệu nhôm và nitrua silic dùng trong nghiên cứu cảm biến "
        "[2], với <i>L</i> = 200 µm, <i>t</i><sub>1</sub> = 0,6 µm, <i>t</i><sub>2</sub> = 0,05 µm, "
        "<i>E</i><sub>1</sub> = 300 GPa, <i>E</i><sub>2</sub> = 70 GPa, α<sub>1</sub> = 3 × 10⁻⁶ K⁻¹ "
        "và α<sub>2</sub> = 24 × 10⁻⁶ K⁻¹ (xem Bảng 32.1), thì một chênh lệch nhiệt độ 1 °C cho độ "
        "võng lý thuyết của côngxôn là 0,103 µm."))

    # ------------------------------------------------- Terminology and Simplifications
    b.append(h3("Thuật ngữ và đơn giản hóa", "Terminology and Simplifications"))
    b.append(p(
        "Trong công nghiệp, dải và tấm lưỡng kim nhiệt tĩnh tuân theo một tiêu chuẩn: ASTM [3] ở "
        "Mỹ và DIN [4] ở châu Âu. Các thông số quan trọng của tiêu chuẩn này được suy trực tiếp từ "
        "các phương trình trên, với những đơn giản hóa dựa trên ứng dụng thông thường."))
    b.append(p(
        "Có thể thấy tỉ số <i>E</i><sub>1</sub>/<i>E</i><sub>2</sub> = <i>n</i> hầu như không ảnh "
        "hưởng đáng kể đến độ cong của dải: lấy <i>n</i> = 1 chỉ gây sai số dưới 3%. Cũng giả thiết "
        "độ cong ban đầu bằng không, Phương trình 32.1 rút gọn thành:"))
    b.append(eq("1/<i>R</i> = 6<i>m</i> / [<i>t</i>(<i>m</i>+1)²] · "
                "(α<sub>2</sub> − α<sub>1</sub>)(<i>T</i> − <i>T</i><sub>0</sub>)", "32.9"))
    b.append(_t321("vi"))
    b.append(p(
        "Trong hầu hết ứng dụng công nghiệp của phần tử lưỡng kim, chiều dày hai lớp được lấy bằng "
        "nhau (<i>m</i> = 1), khi đó Phương trình 32.6 trở thành:"))
    b.append(eq("1/<i>R</i> = (3/2) · (α<sub>2</sub> − α<sub>1</sub>)(<i>T</i> − <i>T</i><sub>0</sub>) "
                "/ <i>t</i>", "32.10"))
    b.append(p(
        "Hằng số (α<sub>2</sub> − α<sub>1</sub>) mang tên <b>độ uốn</b> (flexivity) ở Mỹ và <b>độ "
        "cong riêng</b> (specific curvature) ở châu Âu. Đưa độ uốn <i>k</i> vào và sắp xếp lại "
        "Phương trình 32.10 ta được:"))
    b.append(eq("<i>k</i> = (<i>t</i>/<i>R</i>) / (<i>T</i> − <i>T</i><sub>0</sub>)", "32.11"))
    b.append(p(
        "Độ uốn được định nghĩa là “độ thay đổi độ cong của một dải lưỡng kim trên một đơn vị thay "
        "đổi nhiệt độ, nhân với chiều dày” [5]. Việc xác định thực nghiệm độ uốn của từng dải phải "
        "theo các tiêu chuẩn thử ASTM B388 [3] và DIN 1715 [4]. Phương pháp gồm đo độ võng ở điểm "
        "giữa của dải khi dải được gối tựa đơn giản ở hai đầu. Dùng Phương trình 32.4 ở trên và kết "
        "hợp với Phương trình 32.11 cho:"))
    b.append(eq("<i>k</i> = 8<i>dt</i> / [(<i>T</i> − <i>T</i><sub>0</sub>)<i>L</i>²]", "32.12"))
    b.append(p(
        "Trở lại ví dụ thứ hai về độ võng của côngxôn, dùng Phương trình 32.10 và cùng các giả "
        "thiết (<i>m</i> = <i>n</i> = 1), Phương trình 32.7 trở thành:"))
    b.append(eq("<i>d</i> = (<i>k</i>/2) · (<i>L</i>²/<i>t</i>) · "
                "(<i>T</i> − <i>T</i><sub>0</sub>)", "32.13"))
    b.append(p(
        "Ở châu Âu, hằng số <i>a</i> = <i>dt</i>/[(<i>T</i> − <i>T</i><sub>0</sub>)<i>L</i>²] (về lý "
        "thuyết bằng <i>k</i>/2) được gọi là <b>độ võng riêng</b> và được đo theo tiêu chuẩn DIN từ "
        "độ cong của một dải côngxôn. Cần lưu ý giá trị thực nghiệm khác giá trị lý thuyết vì nó "
        "kể đến ảnh hưởng của các ngoại lực triệt tiêu độ cong ngang tại chỗ kẹp: lý thuyết giả "
        "thiết độ cong bằng nhau dọc suốt dải, trong khi thực tế chỗ kẹp làm bán kính bằng vô cùng "
        "ở đầu cố định."))
    b.append(p(
        "Bảng 32.2 và Bảng 32.4 lần lượt giới thiệu một số phần tử lưỡng kim theo tiêu chuẩn ASTM "
        "và DIN. Các bảng cho độ uốn (hay độ cong riêng), dải nhiệt độ tuyến tính, nhiệt độ làm việc "
        "cực đại và — riêng DIN — độ võng riêng. Thành phần hóa học chi tiết của các phần tử này "
        "được cho trong Bảng 32.3 và Bảng 32.5."))
    b.append(_t322("vi"))
    b.append(_t323("vi"))
    b.append(_t324("vi"))
    b.append(_t325("vi"))

    # ---------------------------------------------------------- Industrial Applications
    b.append(h3("Ứng dụng công nghiệp", "Industrial Applications"))
    b.append(p(
        "Rơle nhiệt cơ khí được dùng rất rộng rãi để điều khiển nhiệt độ trong các quá trình công "
        "nghiệp và trong đời sống hằng ngày. Sự phổ biến ấy có được nhờ việc phát hiện ra Invar — "
        "hợp kim chứa 36% niken với hệ số giãn nở nhiệt rất nhỏ, được đặt tên theo tính chất “bất "
        "biến” của nó [6]."))
    b.append(p(
        "Dựa trên cách chuyển động khi nhiệt độ thay đổi, có hai lớp phần tử lưỡng kim. Phần tử "
        "<b>tác động tức thời</b> (snap-action) bật từ vị trí này sang vị trí khác tại một nhiệt độ "
        "xác định, tùy thiết kế và kết cấu. Có vô số hình dạng và kích thước phần tử tác động tức "
        "thời, và chúng thường là cơ cấu chấp hành ON/OFF. Lớp còn lại, phần tử <b>bò</b> (creep), "
        "thay đổi hình dạng dần dần theo nhiệt độ và được dùng trong nhiệt kế kiểu đồng hồ cùng các "
        "ứng dụng cần chuyển động êm. Ta xét phần tử lưỡng kim chuyển động liên tục trước. Cấu hình "
        "thẳng đã được trình bày ở trên, nên phần này tập trung vào phần tử dạng cuộn."))

    b.append(h3("Cấu hình cuộn xoắn ốc và lò xo", "Spiral and Helical Coil Configurations"))
    b.append(p(
        "Với đo lường công nghiệp hoặc thương mại, cấu hình cuộn xoắn ốc hay xoắn lò xo rất hữu ích "
        "để làm quay kim trên mặt đồng hồ, vì độ võng nhiệt là tuyến tính trong một dải làm việc cho "
        "trước. “Tuyến tính” ở đây nghĩa là độ võng không thay đổi quá 5% so với giá trị tính từ độ "
        "uốn [4]. Các ý tưởng cơ bản về hai vật liệu vẫn giữ nguyên, chỉ thêm vài phương trình liên "
        "hệ chuyển động của cuộn với sự thay đổi nhiệt độ. Như phần trước, các phương pháp chuẩn để "
        "thử tốc độ võng của cuộn xoắn ốc và cuộn lò xo được nêu trong [7]. Các phương trình sau "
        "được lấy từ Sổ tay lưỡng kim nhiệt tĩnh Kanthal [8], có đổi đôi chút ký hiệu. Góc quay của "
        "một cuộn lưỡng kim là (xem Hình 32.5):"))
    b.append(eq("θ = (1/<i>R</i> − 1/<i>R</i><sub>0</sub>) · <i>L</i>", "32.14"))
    b.append(wl([
        "<i>L</i> = chiều dài của dải",
        "<i>R</i><sub>0</sub> và <i>R</i> = bán kính uốn ban đầu và cuối (giả thiết không đổi dọc "
        "theo dải)",
    ]))
    b.append(fig(5, F.fig(5), "vi"))
    b.append(p("Theo độ võng riêng <i>a</i>, biểu thức này được viết thành:"))
    b.append(eq("θ = (2<i>aL</i>/<i>t</i>)(<i>T</i> − <i>T</i><sub>0</sub>) · (360/2π)", "32.15"))
    b.append(wl([
        "<i>t</i> = chiều dày của thiết bị",
        "<i>T</i><sub>0</sub> và <i>T</i> = nhiệt độ ban đầu và cuối",
    ]))
    b.append(p(
        "Một ví dụ là cuộn lưỡng kim hình lò xo đặt trong ống thép, một đầu cuộn gắn vào đầu ống "
        "còn đầu kia nối với kim chỉ. Độ chính xác của một sản phẩm thương mại điển hình là 1% đến "
        "2% toàn thang đo, với dải làm việc 0 °C đến 600 °C [9]."))
    b.append(p(
        "Nếu cần thay đổi nhiệt độ vừa để làm quay kim vừa để sinh lực dẫn động thì góc quay bị "
        "giảm, và được cho bởi:"))
    b.append(eq("θ = [(2<i>a</i>(<i>T</i> − <i>T</i><sub>0</sub>)<i>L</i>)/<i>t</i> − "
                "12(<i>F</i> − <i>F</i><sub>0</sub>)<i>Lr</i>/(<i>wt</i>³<i>E</i>)] · (360/2π)", "32.16"))
    b.append(wl([
        "<i>w</i> = chiều rộng của phần tử",
        "<i>r</i> = khoảng cách từ tâm cuộn đến điểm đặt lực <i>F</i>",
    ]))
    b.append(p("Biểu thức này có thể viết lại thành:"))
    b.append(eq("<i>T</i> − <i>T</i><sub>0</sub> = (θ<i>t</i>/2<i>aL</i>)(2π/360) + "
                "6(<i>F</i> − <i>F</i><sub>0</sub>)<i>r</i>/(<i>wt</i>²<i>Ea</i>)", "32.17"))
    b.append(p(
        "trong đó số hạng thứ nhất là nhiệt độ gắn với góc quay của dải, số hạng thứ hai là nhiệt độ "
        "gắn với lực do dải sinh ra. Nói chung dải được thiết kế sao cho hai số hạng bằng nhau, vì "
        "khi đó thể tích dải là nhỏ nhất, kéo theo khối lượng và giá thành thiết bị nhỏ nhất."))
    b.append(p("Cuối cùng, nếu cuộn bị giữ không cho chuyển động thì độ thay đổi mômen là:"))
    b.append(eq("(<i>F</i> − <i>F</i><sub>0</sub>)<i>r</i> = "
                "(1/6)<i>wt</i>²<i>Ea</i>(<i>T</i> − <i>T</i><sub>0</sub>)", "32.18"))
    b.append(note(
        "<b>Ví dụ.</b> Xét một phần tử lưỡng kim đo nhiệt độ thay đổi từ 20 °C đến 100 °C và làm "
        "dịch chuyển một cần cách 50 mm với lực 1 N. Cần dải đọc trên mặt đồng hồ là 180°. Chọn "
        "lưỡng kim nhiệt tĩnh TM2 vì cho độ võng lớn nhất trên mỗi độ thay đổi nhiệt độ và thỏa mãn "
        "yêu cầu nhiệt độ làm việc. Ở đây có cả lực và chuyển động, nên dùng Phương trình 32.7. Lấy "
        "mỗi số hạng bằng nửa độ thay đổi nhiệt độ cho thể tích dải nhỏ nhất:"))
    b.append(eq("(1/2)(<i>T</i> − <i>T</i><sub>0</sub>) = (θ<i>t</i>/2<i>aL</i>)(2π/360) + "
                "6(<i>F</i> − <i>F</i><sub>0</sub>)<i>r</i>/(<i>wt</i>²<i>Ea</i>)", "32.19"))
    b.append(p(
        "Chọn chiều dày 1,0 mm và dùng độ võng riêng 19 × 10⁻⁶ °C⁻¹ (<i>a</i> = <i>k</i>/2 theo "
        "Bảng 32.2) cho chiều rộng 29 mm. Tương tự, chiều dài dải lưỡng kim nhận được từ số hạng "
        "thứ hai của đẳng thức, cho <i>L</i> = 2,1 m."))

    b.append(h3("Cấu hình tác động tức thời", "Snap-Action Configurations"))
    b.append(p(
        "Phần tử lưỡng kim tác động tức thời được dùng ở nơi cần một hành động tại nhiệt độ ngưỡng. "
        "Vì vậy chúng không phải thiết bị đo nhiệt độ mà là thiết bị được nhiệt độ kích hoạt. Độ "
        "thay đổi nhiệt độ điển hình để kích hoạt một thiết bị tác động tức thời là vài độ và do "
        "hình học của thiết bị quyết định (Hình 32.6). Khi phần tử tác động, một mối nối thường được "
        "đóng hoặc mở, và trong quá trình đó tồn tại một khe hở giữa hai tiếp điểm trong một khoảng "
        "thời gian. Với hệ cơ khí điều đó không thành vấn đề; nhưng với hệ điện, khe hở có thể sinh "
        "tia lửa, làm thiết bị lão hóa sớm và ăn mòn. Biên độ và thời gian phóng tia lửa giảm đi nếu "
        "công tắc tác động nhanh — đó chính là lý do dùng phần tử tác động tức thời."))
    b.append(fig(6, F.fig(6), "vi"))
    b.append(p(
        "Phần tử tác động tức thời cũng đưa vào hệ một lượng trễ nhất định, rất có ích cho những ứng "
        "dụng mà nếu không sẽ dao động quanh điểm đặt. Tuy vậy cần lưu ý rằng thiết kế đặc biệt của "
        "lưỡng kim bò cũng có thể cho các điểm ON/OFF khác nhau, như trường hợp lưỡng kim hàn chồng "
        "ngược (reverse lap-welded) [8]."))

    b.append(h3("Độ nhạy và độ chính xác", "Sensitivity and Accuracy"))
    b.append(p(
        "Khi đo nhiệt độ, các kỹ thuật hiện đại tỏ ra hữu ích hơn về độ nhạy và độ chính xác; nhưng "
        "lưỡng kim vẫn được dùng trong điều khiển nhiệt độ thương mại và công nghiệp ở nơi cần một "
        "hành động mà không cần kết nối bên ngoài. Rõ ràng hình học là quan trọng với các hệ lưỡng "
        "kim, vì độ nhạy do thiết kế quyết định và có thể dùng lợi thế cơ học để có dịch chuyển lớn "
        "trên mỗi độ thay đổi nhiệt độ. Huston [10] đã trình diễn độ nhạy bằng một cuộn lò xo, đạt "
        "6 in. (15,2 cm) dịch chuyển trên mỗi độ trong hệ đo của ông — tương ứng độ nhạy 0,01 °F "
        "trên 1/16 in. (0,0035 °C mm⁻¹). Huston cũng cho thấy độ chính xác lặp lại 0,05 °F "
        "(0,027 °C) khi dùng một thiết bị hiệu chuẩn có độ chính xác 0,1 °F (0,056 °C)."))
    b.append(p(
        "Dải làm việc của nhiều loại lưỡng kim khá rộng; tuy vậy có một vùng mà độ nhạy là cực đại. "
        "Phần tử lưỡng kim thường được chọn để làm việc trong vùng này, và các chi tiết cụ thể do "
        "nhà sản xuất cung cấp trong catalogue. Đáng chú ý là, dù bị chu trình nhiệt kéo dài, dải "
        "lưỡng kim vẫn trở về đúng vị trí cũ ở một nhiệt độ cho trước (tức không có trễ) và rất bền, "
        "miễn là không bị đưa ra ngoài dải nhiệt độ làm việc quy định."))

    # ---------------------------------------------------------- Advanced Applications
    b.append(h3("Ứng dụng tiên tiến", "Advanced Applications"))
    b.append(p(
        "Van nhiệt tĩnh là một cách đo nhiệt độ và điều khiển gia nhiệt, làm lạnh sẵn có và bền bỉ "
        "trong môi trường công nghiệp. Các thiết kế cơ bản đã tồn tại nhiều năm và là trụ cột của "
        "nhiều hệ điều khiển nhiệt độ thương mại. Những ứng dụng mới của vật liệu hai lớp đang xuất "
        "hiện trong vi cơ cấu chấp hành và vi cảm biến."))
    b.append(p(
        "Ngoài chức năng dụng cụ đo nhiệt độ, thiết bị hai lớp còn dùng được cho nhiều ứng dụng "
        "trong đó nhiệt độ là hiện tượng điều khiển hay kích hoạt, hoặc trong đó người ta suy ra các "
        "tính chất khác của vật liệu từ đáp ứng nhiệt. Một ví dụ là cơ cấu chấp hành niken–silic do "
        "các kỹ sư phòng thí nghiệm HP ở Palo Alto, CA phát triển: cơ cấu hoạt động bằng cách nung "
        "một điện trở niken mỏng trên mặt silic của một thiết bị hai lớp [11]. Cả lớp silic và lớp "
        "niken đều giãn ra khi bị nung; nhưng lớp niken giãn nhiều hơn, làm thiết bị cong đi và mở "
        "một van rất nhỏ. Thiết bị điều khiển được lưu lượng khí từ 0,1 đến 600 cm³ tiêu chuẩn mỗi "
        "phút với áp suất từ 5 psi đến 200 psi (34,5 kPa đến 1379 kPa)."))
    b.append(p(
        "Việc dùng các cảm biến nhiệt chế tạo bằng vi gia công, tương thích với công nghệ chế tạo "
        "mạch tích hợp silic hiện đại, gần đây nhận được nhiều chú ý. Một cách đạt được phép đo "
        "nhiệt có độ nhạy cao là dùng côngxôn lưỡng kim vi cơ và đo độ võng do dao động nhiệt gây "
        "ra. Côngxôn chữ nhật hoặc tam giác, thường dài 100 µm, làm bằng silic hoặc nitrua silic, "
        "được phủ một lớp kim loại mỏng giãn nở mạnh (ví dụ nhôm hoặc vàng). Độ võng ở đầu côngxôn "
        "được đo chính xác bằng một sơ đồ cảm quang thường dùng trong kính hiển vi lực nguyên tử. "
        "Bản chất vi cơ của cảm biến côngxôn đem lại ưu thế lớn về độ nhạy tuyệt đối: thiết bị có "
        "thể đo nhiệt độ, nhiệt lượng và công suất với độ phân giải lần lượt 10⁻⁵ K, 150 fJ và "
        "100 pW [2]. Ngoài vai trò cảm biến nhiệt, hệ côngxôn lưỡng kim còn được dùng để khảo sát "
        "các hiện tượng vật lý trong đó nhiệt sinh ra từ mẫu. Ví dụ gồm phổ quang nhiệt của silic vô "
        "định hình [2] và quan sát dao động trong phản ứng xúc tác của hydro và oxy trên bạch kim "
        "[12]. Như vậy cảm biến hai vật liệu đang trở thành một hướng phát triển ngày càng quan "
        "trọng."))

    # ---------------------------------------------------------- Defining Terms
    b.append(h3("Định nghĩa thuật ngữ", "Defining Terms"))
    b.append(defs([
        ("<b>Hệ số giãn nở nhiệt dài</b>",
         "Độ thay đổi chiều dài của một vật liệu trên mỗi độ thay đổi nhiệt độ, biểu diễn theo "
         "phân số của tổng chiều dài (Δ<i>L</i>/<i>L</i>)."),
        ("<b>Độ uốn</b> (flexivity)",
         "Độ thay đổi bán kính cong của một phần tử hai vật liệu trên mỗi độ thay đổi nhiệt độ, "
         "nhân với chiều rộng của phần tử (xem Phương trình 32.11)."),
        ("<b>Độ cong riêng</b>",
         "Thuật ngữ châu Âu chỉ độ uốn."),
        ("<b>Độ võng riêng</b>",
         "Về lý thuyết bằng nửa độ uốn. Độ võng riêng được đo bằng cách gắn phần tử thử như một "
         "côngxôn — kẹp một đầu, đầu kia tự do."),
    ]))
    return "".join(b)


def sec_32_1_en():
    b = [h2("32.1 Bimaterials Thermometers", anchor="s32-1")]
    b.append(authors("", "Robert J. Stephenson, Armelle M. Moulin, and Mark E. Welland"))

    b.append(p(
        "The first known use of differential thermal expansion of metals in a mechanical device was "
        "that of the English clockmaker John Harrison in 1735. Harrison used two dissimilar metals "
        "in a clock escapement to account for the changes in temperature on board a ship. This first "
        "marine chronometer used a gridiron of two metals that altered the flywheel period of the "
        "clock through a simple displacement. This mechanical actuation, resulting from the "
        "different thermal expansivities of two metals in contact, is the basis for all bimetallic "
        "actuators used today."))
    b.append(p(
        "The bimetallic effect is now used in numerous applications ranging from domestic appliances "
        "to compensation in satellites. The effect can be used in two ways: either as an actuator or "
        "as a temperature measuring system. A bimetallic actuator essentially consists of two metal "
        "strips fixed together. If the two metals have different expansivities, then as the "
        "temperature of the actuator changes, one element will expand more than the other, causing "
        "the device to bend out of the plane. This mechanical bending can then be used to actuate an "
        "electromechanical switch or be part of an electrical circuit itself, so that contact of the "
        "bimetallic device with an electrode causes a circuit to be made. Although in its simplest "
        "form a bimetallic actuator can be constructed from two flat pieces of metal, in practical "
        "terms a whole range of shapes are used to provide maximum actuation or maximum force during "
        "thermal cycling."))
    b.append(p(
        "As a temperature measuring device, the bimetallic element — similar in design to the "
        "actuator above — can be used to determine the ambient temperature if the degree of bending "
        "can be measured. The advantage of such a system is that the amount of bending can be "
        "mechanically amplified to produce a large and hence easily measurable displacement. Figure "
        "32.1 shows the basic principle of a bimetallic actuator: two metal strips of differing "
        "thermal expansion are bonded together. When the temperature of the assembly is changed, in "
        "the absence of external forces, the bimetallic actuator takes the shape of an arc. The total "
        "displacement of the actuator out of the plane of the metal strips is much greater than the "
        "individual expansions of the metallic elements."))
    b.append(fig(1, F.fig(1), "en"))
    b.append(p(
        "To maximize the bending of the actuator, metals or alloys with greatly differing "
        "coefficients of thermal expansion are normally selected. The metal having the largest "
        "thermal expansivity is known as the <b>active element</b>, while the metal having the "
        "smaller coefficient of expansion is known as the <b>passive element</b>. For maximum "
        "actuation, the passive element is often an iron–nickel alloy, Invar, having an almost zero "
        "thermal expansivity (actually between 0.1 and 1 × 10⁻⁶ K⁻¹, depending on the composition). "
        "The active element is then chosen to have maximum thermal expansivity given the constraints "
        "of operating environment and cost."))
    b.append(p(
        "In addition to maximizing the actuation of the bimetallic element, other constraints such as "
        "electrical and thermal conductivity can be imposed. In such cases a third metallic layer is "
        "introduced, consisting of either copper or nickel sandwiched between the active and passive "
        "elements so as to increase both the electrical and thermal conductivity of the actuator. "
        "This is especially important where the actuator is part of an electrical circuit and needs "
        "to pass current in addition to being a temperature sensor."))

    b.append(h3("Linear Bimaterial Strip"))
    b.append(h3("Basic Equations"))
    b.append(p(
        "The analysis of the stress distribution and the deflection of an ideal bimetallic strip was "
        "first deduced by Timoshenko [1], who produced a simple derivation from the theory of "
        "elasticity. Figure 32.2 shows the internal forces and moments that induce bending in a "
        "bimetallic strip, followed by the ideal stress distribution in the beam. This theory is "
        "derived for bimetallic strips but is equally applicable to bimaterial strips."))
    b.append(p(
        "The general equation for the curvature radius of a bimetallic strip uniformly heated from "
        "<i>T</i>₀ to <i>T</i> in the absence of external forces is given by [1]:"))
    b.append(eq("1/<i>R</i> − 1/<i>R</i><sub>0</sub> = "
                "6(1+<i>m</i>)²(α<sub>2</sub> − α<sub>1</sub>)(<i>T</i> − <i>T</i><sub>0</sub>) / "
                "{<i>t</i>[3(1+<i>m</i>)² + (1+<i>mn</i>)(<i>m</i>² + 1/(<i>mn</i>))]}", "32.1"))
    b.append(wl([
        "1/<i>R</i><sub>0</sub> = initial curvature of the strip at temperature <i>T</i><sub>0</sub>",
        "α<sub>1</sub> and α<sub>2</sub> = coefficients of expansion of the two elements: (1) low "
        "expansive material and (2) high expansive material",
        "<i>n</i> = <i>E</i><sub>1</sub>/<i>E</i><sub>2</sub>, with <i>E</i><sub>1</sub> and "
        "<i>E</i><sub>2</sub> their respective Young's moduli",
        "<i>m</i> = <i>t</i><sub>1</sub>/<i>t</i><sub>2</sub>, with <i>t</i><sub>1</sub> and "
        "<i>t</i><sub>2</sub> their respective thicknesses",
        "<i>t</i> = <i>t</i><sub>1</sub> + <i>t</i><sub>2</sub>, the thickness of the strip",
    ]))
    b.append(p("The width of the strip is taken as equal to unity."))
    b.append(p(
        "Equation 32.1 applies for several strip configurations, including the simply supported strip "
        "and a strip clamped at one end (i.e., a cantilever). For a given configuration, the "
        "deflection of a strip can be determined by its relationship with curvature, 1/<i>R</i>."))
    b.append(fig(2, F.fig(2), "en"))
    b.append(p(
        "An example of a calculation of deflection is a bimetallic strip simply supported at its two "
        "ends. The initial curvature 1/<i>R</i><sub>0</sub> is assumed to be zero. Figure 32.3 shows "
        "the geometrical relationship between the radius <i>R</i> of the strip and the deflection "
        "<i>d</i> at its mid-point:"))
    b.append(eq("(<i>R</i> − <i>t</i><sub>2</sub>)² = "
                "(<i>R</i> − <i>d</i> − <i>t</i><sub>2</sub>)² + (<i>L</i>/2)²", "32.2"))
    b.append(p("Hence,"))
    b.append(eq("1/<i>R</i> = 8<i>d</i> / (<i>L</i>² + 4<i>d</i>² + 8<i>dt</i><sub>2</sub>)", "32.3"))
    b.append(p(
        "Making the assumption that the deflection and the thickness are less than 10% of the length "
        "of the strip (which is true in most practical cases) means the terms 8<i>dt</i><sub>2</sub> "
        "and 4<i>d</i>² are negligible and the expression reduces to:"))
    b.append(eq("<i>d</i> = <i>L</i>² / (8<i>R</i>)", "32.4"))
    b.append(p("Combining this with Equation 32.1 yields:"))
    b.append(eq("<i>d</i> = <i>L</i>² · 3(1+<i>m</i>)² / "
                "{4<i>t</i>[3(1+<i>m</i>)² + (1+<i>mn</i>)(<i>m</i>² + 1/(<i>mn</i>))]} · "
                "(α<sub>2</sub> − α<sub>1</sub>)(<i>T</i> − <i>T</i><sub>0</sub>)", "32.5"))
    b.append(p(
        "If a 100-mm strip is composed of two layers of the same thickness (0.5 mm) with the "
        "high-expansive layer made of iron (from Table 32.1, <i>E</i><sub>2</sub> = 211 GPa and "
        "α<sub>2</sub> = 12.1 × 10⁻⁶ K⁻¹), the low-expansive layer made of Invar (<i>E</i><sub>1</sub> "
        "= 140 GPa and α<sub>1</sub> = 1.7 × 10⁻⁶ K⁻¹), and the temperature increases from 20 °C to "
        "120 °C, then the theoretical bending at the middle of the strip will be 1.92 mm."))
    b.append(p(
        "As a second example, consider the calculation of the deflection of the free end of a "
        "bimetallic cantilever strip as illustrated in Figure 32.4. In this case the geometrical "
        "relation is:"))
    b.append(eq("(<i>R</i> + <i>t</i><sub>1</sub>)² = "
                "(<i>R</i> + <i>t</i><sub>1</sub> − <i>d</i>)² + <i>L</i>²", "32.6a"))
    b.append(p("or"))
    b.append(eq("1/<i>R</i> = 2<i>d</i> / (<i>L</i>² + <i>d</i>² − 2<i>dt</i><sub>1</sub>)", "32.6b"))
    b.append(p(
        "Making the same assumptions as before, that is, <i>d</i>² « <i>L</i>² and "
        "<i>dt</i><sub>1</sub> « <i>L</i>², then the deflection of the free end is given by:"))
    b.append(eq("<i>d</i> = <i>L</i>² / (8<i>R</i>)", "32.7"))
    b.append(fig(3, F.fig(3), "en"))
    b.append(fig(4, F.fig(4), "en"))
    b.append(p("and combining this with Equation 32.1 yields:"))
    b.append(eq("<i>d</i> = <i>L</i>² · 3(1+<i>m</i>)² / "
                "{<i>t</i>[3(1+<i>m</i>)² + (1+<i>mn</i>)(<i>m</i>² + 1/(<i>mn</i>))]} · "
                "(α<sub>2</sub> − α<sub>1</sub>)(<i>T</i> − <i>T</i><sub>0</sub>)", "32.8"))
    b.append(p(
        "If an aluminum and silicon nitride bimaterial microcantilever as used for sensor research "
        "[2] is considered, then <i>L</i> = 200 µm, <i>t</i><sub>1</sub> = 0.6 µm, "
        "<i>t</i><sub>2</sub> = 0.05 µm, <i>E</i><sub>1</sub> = 300 GPa, <i>E</i><sub>2</sub> = 70 GPa, "
        "α<sub>1</sub> = 3 × 10⁻⁶ K⁻¹ and α<sub>2</sub> = 24 × 10⁻⁶ K⁻¹ (see Table 32.1). In this "
        "situation, a temperature difference of 1 °C gives a theoretical deflection of the "
        "cantilever of 0.103 µm."))

    b.append(h3("Terminology and Simplifications"))
    b.append(p(
        "For industrial purposes, bimetallic thermostatic strips and sheets follow a standard "
        "specification — ASTM [3] in the U.S. and DIN [4] in Europe. Important parameters involved in "
        "this specification are derived directly from the previous equations, in which "
        "simplifications are made based on common applications."))
    b.append(p(
        "It can be seen that the magnitude of the ratio <i>E</i><sub>1</sub>/<i>E</i><sub>2</sub> = "
        "<i>n</i> has no substantial effect on the curvature of the strip, and taking <i>n</i> = 1 "
        "implies an error less than 3%. Assuming again that the initial curvature is zero, Equation "
        "32.1 can be simplified to:"))
    b.append(eq("1/<i>R</i> = 6<i>m</i> / [<i>t</i>(<i>m</i>+1)²] · "
                "(α<sub>2</sub> − α<sub>1</sub>)(<i>T</i> − <i>T</i><sub>0</sub>)", "32.9"))
    b.append(_t321("en"))
    b.append(p(
        "In most industrial applications involving bimetallic elements, the thicknesses of the two "
        "component layers are taken to be equal (<i>m</i> = 1), thus Equation 32.6 becomes:"))
    b.append(eq("1/<i>R</i> = (3/2) · (α<sub>2</sub> − α<sub>1</sub>)(<i>T</i> − <i>T</i><sub>0</sub>) "
                "/ <i>t</i>", "32.10"))
    b.append(p(
        "The constant (α<sub>2</sub> − α<sub>1</sub>) is known as <b>flexivity</b> in the U.S. and as "
        "<b>specific curvature</b> in Europe. Introducing the flexivity <i>k</i> and rearranging "
        "Equation 32.10 gives:"))
    b.append(eq("<i>k</i> = (<i>t</i>/<i>R</i>) / (<i>T</i> − <i>T</i><sub>0</sub>)", "32.11"))
    b.append(p(
        "Flexivity can be defined as “the change of curvature of a bimetal strip per unit of "
        "temperature change times thickness” [5]. The experimental determination of the flexivity "
        "for each bimetallic strip has to follow the test specifications ASTM B388 [3] and DIN 1715 "
        "[4]. The method consists of measuring the deflection of the midpoint of the strip when it is "
        "simply supported at its ends. Using Equation 32.4 derived above and combining with Equation "
        "32.11 gives:"))
    b.append(eq("<i>k</i> = 8<i>dt</i> / [(<i>T</i> − <i>T</i><sub>0</sub>)<i>L</i>²]", "32.12"))
    b.append(p(
        "Coming back to the second example of the calculation of the deflection (cantilever case), "
        "using Equation 32.10 and the same assumptions (<i>m</i> = <i>n</i> = 1), Equation 32.7 "
        "becomes:"))
    b.append(eq("<i>d</i> = (<i>k</i>/2) · (<i>L</i>²/<i>t</i>) · "
                "(<i>T</i> − <i>T</i><sub>0</sub>)", "32.13"))
    b.append(p(
        "In Europe, the constant <i>a</i> = <i>dt</i>/[(<i>T</i> − <i>T</i><sub>0</sub>)<i>L</i>²] "
        "(theoretically equal to <i>k</i>/2) is called <b>specific deflection</b> and is measured "
        "following the DIN test specification from the bending of a cantilever strip. It can be noted "
        "that the experimental value differs from the theoretical value as it takes into account the "
        "effect of the external forces suppressing the cross-curvature where the strip is fastened "
        "(i.e., the theory assumes that the curvature is equal along the strip, whereas in reality "
        "the fact that the strip is fastened implies that the radius is infinite at its fixed end)."))
    b.append(p(
        "Tables 32.2 and 32.4 present a selection of bimetallic elements following ASTM and DIN "
        "standards, respectively. Flexivity (or specific curvature), linear temperature range, "
        "maximum operating temperature and specific deflection (DIN only) are given. The details of "
        "the chemical composition of these elements are specified in Tables 32.3 and 32.5."))
    b.append(_t322("en"))
    b.append(_t323("en"))
    b.append(_t324("en"))
    b.append(_t325("en"))

    b.append(h3("Industrial Applications"))
    b.append(p(
        "The mechanical thermostat finds a wide range of applications in temperature control in "
        "industrial processes and everyday life. This widespread use of thermostats is due to the "
        "discovery of Invar, a 36% nickel alloy that has a very low thermal expansion coefficient, "
        "and was so named because of its property of invariability [6]."))
    b.append(p(
        "There are two general classes of bimetallic elements based on their movement in response to "
        "temperature changes. <b>Snap-action</b> devices jump from one position to another at a "
        "specific temperature depending on their design and construction. There are numerous "
        "different shapes and sizes of snap-action elements and they are typically ON/OFF actuators. "
        "The other class of elements, <b>creep</b> elements, exhibit a gradual change in shape in "
        "response to a change in temperature and are employed in temperature gauges and other smooth "
        "movement applications. Continuous movement bimetals will be considered first. A linear "
        "configuration was covered previously, so the discussion will focus on coiled bimetallic "
        "elements."))

    b.append(h3("Spiral and Helical Coil Configurations"))
    b.append(p(
        "For industrial or commercial measurements, a spiral or helical coil configuration is useful "
        "for actuating a pointer on a dial as the thermal deflection is linear within a given "
        "operating range. Linearity in this case means that the deflection does not vary by more than "
        "5% of the deflection, as calculated from the flexivity [4]. The basic bimaterial ideas from "
        "the previous section still apply, with some additional equations relating the movement of a "
        "bimetal coil to a change in temperature. As in the previous section, standard methods for "
        "testing the deflection rate of spiral and helical coils exist and can be found in [7]. The "
        "following equations have been taken from the Kanthal Thermostatic Bimetal Handbook [8], with "
        "some change in notation. The angular rotation of a bimetal coil is given by (see Figure "
        "32.5):"))
    b.append(eq("θ = (1/<i>R</i> − 1/<i>R</i><sub>0</sub>) · <i>L</i>", "32.14"))
    b.append(wl([
        "<i>L</i> = length of the strip",
        "<i>R</i><sub>0</sub> and <i>R</i> = initial and final bending radii (assumed to be constant "
        "along the strip), respectively",
    ]))
    b.append(fig(5, F.fig(5), "en"))
    b.append(p("In terms of the specific deflection <i>a</i>, this can be written as:"))
    b.append(eq("θ = (2<i>aL</i>/<i>t</i>)(<i>T</i> − <i>T</i><sub>0</sub>) · (360/2π)", "32.15"))
    b.append(wl([
        "<i>t</i> = thickness of the device",
        "<i>T</i><sub>0</sub> and <i>T</i> = initial and final temperatures, respectively",
    ]))
    b.append(p(
        "An example would be a helical bimetal coil inside a steel tube with one end of the coil "
        "fixed to the end of the tube and the other connected to a pointer. The accuracy of a typical "
        "commercial product is 1% to 2% of full-scale deflection with an operating range of 0 °C to "
        "600 °C [9]."))
    b.append(p(
        "If a change in temperature is required both to move a pointer and to produce a driving "
        "force, then the angular rotation is reduced and is given by:"))
    b.append(eq("θ = [(2<i>a</i>(<i>T</i> − <i>T</i><sub>0</sub>)<i>L</i>)/<i>t</i> − "
                "12(<i>F</i> − <i>F</i><sub>0</sub>)<i>Lr</i>/(<i>wt</i>³<i>E</i>)] · (360/2π)", "32.16"))
    b.append(wl([
        "<i>w</i> = width of the element",
        "<i>r</i> = distance from the center of the coil to the point of applied force, <i>F</i>",
    ]))
    b.append(p("This can be rewritten as:"))
    b.append(eq("<i>T</i> − <i>T</i><sub>0</sub> = (θ<i>t</i>/2<i>aL</i>)(2π/360) + "
                "6(<i>F</i> − <i>F</i><sub>0</sub>)<i>r</i>/(<i>wt</i>²<i>Ea</i>)", "32.17"))
    b.append(p(
        "where the first term represents the temperature associated with the angular rotation of the "
        "strip and the second term represents the temperature associated with the force generated by "
        "the strip. In general, the strip is designed so that the two are equal, as this leads to the "
        "minimum volume for the strip and consequently less weight and cost for the device."))
    b.append(p(
        "Finally, if the coil is prevented from moving then the change in torque is given by:"))
    b.append(eq("(<i>F</i> − <i>F</i><sub>0</sub>)<i>r</i> = "
                "(1/6)<i>wt</i>²<i>Ea</i>(<i>T</i> − <i>T</i><sub>0</sub>)", "32.18"))
    b.append(note(
        "<b>Example.</b> Consider a bimetal element that measures a temperature change from 20 °C to "
        "100 °C and moves a lever 50 mm away with a force of 1 N. A dial reading range of 180° is "
        "required. Choosing thermostatic bimetal TM2 gives the largest deflection per degree "
        "temperature change and TM2 meets the operating temperature requirements. Both a force and a "
        "movement are involved, so use Equation 32.7. Choosing each term equal to half the "
        "temperature change gives the minimum volume for the strip as:"))
    b.append(eq("(1/2)(<i>T</i> − <i>T</i><sub>0</sub>) = (θ<i>t</i>/2<i>aL</i>)(2π/360) + "
                "6(<i>F</i> − <i>F</i><sub>0</sub>)<i>r</i>/(<i>wt</i>²<i>Ea</i>)", "32.19"))
    b.append(p(
        "Selecting a thickness of 1.0 mm and using a specific deflection of 19 × 10⁻⁶ °C⁻¹ "
        "(<i>a</i> = <i>k</i>/2 from Table 32.2) gives a width of 29 mm. Similarly, the length of the "
        "bimetal strip is obtained from the second term in the equality, giving <i>L</i> = 2.1 m."))

    b.append(h3("Snap-Action Configurations"))
    b.append(p(
        "Snap-action bimetal elements are used in applications where an action is required at a "
        "threshold temperature. As such, they are not temperature measuring devices, but rather "
        "temperature-activated devices. The typical temperature change to activate a snap-action "
        "device is several degrees and is determined by the geometry of the device (Figure 32.6). "
        "When the element activates, a connection is generally made or broken and in doing so, a gap "
        "between the two contacts exists for a period of time. For a mechanical system there is no "
        "problem; however, for an electrical system the gap can result in a spark that can lead to "
        "premature aging and corrosion of the device. The amount and duration of spark is reduced by "
        "having the switch activate quickly, hence the use of snap-action devices."))
    b.append(fig(6, F.fig(6), "en"))
    b.append(p(
        "Snap-action elements also incorporate a certain amount of hysteresis into the system, which "
        "is useful in applications that would otherwise result in an oscillation about the set-point. "
        "It should be noted, however, that special design of creep action bimetals can also lead to "
        "different ON/OFF points, such as in the reverse lap-welded bimetal [8]."))

    b.append(h3("Sensitivity and Accuracy"))
    b.append(p(
        "Modern techniques are more useful where sensitivity and accuracy are concerned for making a "
        "temperature measurement; however, bimetals find application in commercial and industrial "
        "temperature control where an action is required without external connections. Evidently, "
        "geometry is important for bimetal systems as the sensitivity is determined by the design, "
        "and a mechanical advantage can be used to yield a large movement per degree temperature "
        "change. A demonstration of sensitivity using a helical coil was made by Huston [10] that "
        "gave 6 in. (15.2 cm) deflection per degree in their measurement system — yielding a "
        "sensitivity of 0.01 °F per 1/16 in. (0.0035 °C mm⁻¹). Huston also demonstrated a repeatable "
        "accuracy of 0.05 °F (0.027 °C) based on the use of a 0.1 °F (0.056 °C) accuracy calibration "
        "instrument."))
    b.append(p(
        "The operating range for many bimetals is quite large; however, there is a range over which "
        "the sensitivity is a maximum. A bimetal element is generally chosen to operate in this range "
        "and specific details are provided by manufacturers in their product catalogs. Of particular "
        "note is that, despite extended thermal cycling, bimetal strips reliably return to the same "
        "position (i.e., show no hysteresis) at a given temperature and are very robust as long as "
        "they are not subjected to temperatures outside their specified operating range."))

    b.append(h3("Advanced Applications"))
    b.append(p(
        "Thermostatic valves are a ready and robust means of measuring temperature and controlling "
        "heating and cooling in industrial settings. The basic designs have been around for many "
        "years and are the mainstay of many commercial temperature-control systems. New applications "
        "of bimaterials are being found in microactuators and microsensors."))
    b.append(p(
        "Besides operating as temperature-measuring instruments, bimaterial devices can be used for a "
        "variety of applications where temperature is the controlling or triggering phenomenon, or "
        "indeed, other material properties are inferred from the temperature response. One such "
        "example is a nickel–silicon actuator developed by engineers at HP labs in Palo Alto, CA; the "
        "actuator operates by heating a thin nickel resistor on the silicon side of a bilayer device "
        "[11]. Both the silicon and nickel layers expand due to heating; however, the nickel layer "
        "expands more, thereby curling the device, which leads to the actuation of a tiny valve. The "
        "device can control gas flow rates from 0.1 to 600 standard cm³ per minute with pressures "
        "ranging from 5 psi to 200 psi (34.5 kPa to 1379 kPa)."))
    b.append(p(
        "The use of micromachined thermal sensors compatible with modern silicon integrated circuit "
        "fabrication methods has recently received significant attention. One way of achieving highly "
        "sensitive thermal measurements is by using micromechanical bimetallic cantilevers and "
        "measuring the deflection as a result of thermal fluctuations. Rectangular or triangular "
        "cantilevers, typically 100 µm long made of silicon or silicon nitride, are coated with a "
        "thin high-expansive metallic layer (e.g., aluminum or gold). Precise measurement of the "
        "deflection of the end of the cantilever is achieved using an optical sensing arrangement "
        "commonly used in atomic force microscopes. The micromechanical nature of the cantilever-based "
        "sensor leads to significant advantages in the absolute sensitivity achievable. In this way "
        "the device is capable of measuring temperature, heat and power variations of 10⁻⁵ K, 150 fJ "
        "and 100 pW, respectively [2]. In addition to their use as thermal sensors, the bimetallic "
        "cantilever systems have been used to investigate physical phenomena where heat is produced "
        "by the sample. Examples include photothermal spectroscopy studies of amorphous silicon [2] "
        "and the observation of oscillations in the catalyzed reaction of hydrogen and oxygen on "
        "platinum [12]. Thus, bimaterial sensors are becoming an increasingly important area of "
        "development."))

    b.append(h3("Defining Terms"))
    b.append(defs([
        ("<b>Linear coefficient of thermal expansion</b>",
         "The change in length of a material per degree change in temperature, expressed as a "
         "fraction of the total length (Δ<i>L</i>/<i>L</i>)."),
        ("<b>Flexivity</b>",
         "The change in radius of curvature of a bimaterial per degree change in temperature times "
         "the width of the element (see Equation 32.11)."),
        ("<b>Specific curvature</b>",
         "The European term for flexivity."),
        ("<b>Specific deflection</b>",
         "Theoretically equal to half the flexivity. Specific deflection is measured by mounting the "
         "test element as a cantilever — supported at one end and free to move at the other."),
    ]))
    return "".join(b)


# ================================================================ back matter
def _refs(lang):
    vi = lang == "vi"
    items = [
        "1. S.P. Timoshenko, <i>The Collected Papers</i>, New York: McGraw-Hill, 1953.",
        "2. J.R. Barnes, R.J. Stephenson, M.E. Welland, C. Gerber, and J.K. Gimzewski, Photothermal "
        "spectroscopy with femtojoule sensitivity using a micromechanical device, <i>Nature</i>, "
        "372, 79–81, 1994.",
        "3. ASTM Designation B 388.",
        "4. DIN 1715, Part 1, <i>Thermostat Metals</i>, 1983.",
        "5. ASTM Designation B 106.",
        "6. M. Kutz, <i>Temperature Control</i>, New York: John Wiley &amp; Sons, 1968.",
        "7. ASTM Designation B 389.",
        "8. <i>The Kanthal Thermostatic Bimetal Handbook</i>, Box 502, S-73401 Hallstammar, Sweden, "
        "1987.",
        "9. Bourdon Sedeme, F-41103 Vendôme Cedex, France.",
        "10. W.D. Huston, The accuracy and reliability of bimetallic temperature measuring elements, "
        "in C.M. Herzfeld and A.I. Dahl (eds.), <i>Temperature — Its Measurement and Control in "
        "Science and Industry</i>, New York: Reinhold, 1962.",
        "11. L. O'Connor, A bimetallic silicon microvalve, <i>Mechanical Engineering</i>, 117(1), 1, "
        "1995.",
        "12. J.K. Gimzewski, C. Gerber, E. Meyer, and R. Schlittler, Observation of a chemical "
        "reaction using a micromechanical sensor, <i>Chem. Phys. Lett.</i> 217, 589–594, 1994.",
        "13. G.C.M. Meijer and A.W. van Herwaarden, <i>Thermal Sensors</i>, Bristol, U.K.: Institute "
        "of Physics Publishing, 1994.",
        "14. Goodfellow Cambridge Limited, Cambridge Science Park, U.K. CB4 4DJ.",
        "15. American Society for Testing and Materials, <i>Annual Book of ASTM Standards</i>, "
        "Philadelphia, 1991.",
    ]
    head_ = "<h3 id=\"t32-tltk\">Tài liệu tham khảo</h3>" if vi else \
            "<h3 id=\"t32-tltk\">References</h3>"
    return head_ + wl(items)


def back_vi():
    b = [_refs("vi")]
    b.append(h3("Thông tin thêm", "Further Information"))
    b.append(wl([
        "V.C. Miles, <i>Thermostatic Control — Principles and Practice</i>, London: Newnes-Butterworth.",
        "Kanthal Thermostatic Bimetal Handbook (xem [8]) — dữ liệu thiết kế cho cuộn xoắn ốc và "
        "lò xo, kèm bảng độ uốn của từng loại lưỡng kim.",
    ]))
    return "".join(b)


def back_en():
    b = [_refs("en")]
    b.append(h3("Further Information", "Thông tin thêm"))
    b.append(wl([
        "V.C. Miles, <i>Thermostatic Control — Principles and Practice</i>, London: Newnes-Butterworth.",
        "Kanthal Thermostatic Bimetal Handbook (see [8]) — design data for spiral and helical coils, "
        "with flexivity tables for each bimetal type.",
    ]))
    return "".join(b)


# ================================================================ index
INDEX = [
    ("32.1", "Bimaterials Thermometers", "Đo nhiệt độ bằng lưỡng kim", [
        ("Linear Bimaterial Strip", "Dải lưỡng kim thẳng"),
        ("Basic Equations", "Các phương trình cơ bản"),
        ("Terminology and Simplifications", "Thuật ngữ và đơn giản hóa"),
        ("Industrial Applications", "Ứng dụng công nghiệp"),
        ("Spiral and Helical Coil Configurations", "Cấu hình cuộn xoắn ốc và lò xo"),
        ("Snap-Action Configurations", "Cấu hình tác động tức thời"),
        ("Sensitivity and Accuracy", "Độ nhạy và độ chính xác"),
        ("Advanced Applications", "Ứng dụng tiên tiến"),
        ("Defining Terms", "Định nghĩa thuật ngữ"),
    ]),
]


def sec_index(vi):
    out = ['<ol class="toc-list">']
    for num, en, vn, subs in INDEX:
        title = vn if vi else en
        out.append('<li><span class="n">%s</span><a class="t" href="#s32-%s">%s</a></li>'
                   % (num, num.split(".")[1], title))
        for sub_en, sub_vi in subs:
            out.append('<li style="margin-left:2.4rem;font-size:.9rem;padding:.15rem 0">'
                       '<a class="t" href="#s32-%s">%s</a></li>'
                       % (num.split(".")[1], sub_vi if vi else sub_en))
    out.append("</ol>")
    return "".join(out)


def body_vi():
    lede = (
        "Nhiệt độ là đại lượng được đo nhiều nhất trong công nghiệp, và cũng là đại lượng có nhiều "
        "họ nguyên lý chuyển đổi nhất. Chương này đi qua mười một họ dụng cụ — từ dải lưỡng kim, "
        "nhiệt điện trở, cặp nhiệt điện đến hồng ngoại và sợi quang — với phương trình, hình vẽ và "
        "bảng dữ liệu của từng loại.")
    return (p(lede) + sec_index(True) + sec_32_1_vi() + back_vi())


def body_en():
    lede = (
        "Temperature is the most widely measured quantity in industry, and the one with the largest "
        "number of transducer families. This chapter works through eleven of them — bimetallic "
        "strips, resistance thermometers, thermistors, thermocouples, semiconductor junctions, "
        "infrared, pyroelectric, liquid-in-glass, manometric, indicators and fiber-optic probes — "
        "with the equations, figures and data tables for each.")
    return (p(lede) + sec_index(False) + sec_32_1_en() + back_en())


def build(lang):
    vi = lang == "vi"
    title = TITLE_VI if vi else TITLE_EN
    desc = ("Bản dịch tiếng Việt chương 32 của The Measurement, Instrumentation and Sensors "
            "Handbook — Đo nhiệt độ." if vi else
            "Bilingual companion to Chapter 32 of The Measurement, Instrumentation and Sensors "
            "Handbook — Temperature.")
    switch = (BASE_EN if vi else BASE_VI)
    crumb = ('<a href="/vi/books/">Sách</a> · <a href="%s">Sổ tay Đo lường, Thiết bị đo và Cảm biến'
             '</a> · Chương 32' % BASE_VI if vi else
             '<a href="/books/">Books</a> · <a href="%s">Measurement, Instrumentation and Sensors '
             'Handbook</a> · Chapter 32' % BASE_EN)
    meta = ("Chương 32 · theo Ch32.pdf (CRC Press, 1999) · §32.1/11 · 6 hình, 19 phương trình, 5 bảng"
            if vi else
            "Chapter 32 · §32.1 of 11 · 6 figures, 19 equations, 5 tables")
    body = ('<main><article class="intranet-content reader"><div class="reader-hero">'
            '<div class="breadcrumb">%s</div><h1>%s</h1><p class="byline">%s</p>'
            '<div class="meta-line">%s</div></div><div class="prose">%s</div>%s</article></main>'
            % (crumb, title, BYLINE, meta,
               body_vi() if vi else body_en(), chapter_nav(lang, 32)))
    return head(lang, title, desc) + header(lang, switch) + body + footer(lang)


def main():
    if len(sys.argv) > 1:
        path = sys.argv[1]
        page = build("vi")
        os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
        open(path, "w", encoding="utf-8").write(page)
        print("wrote preview %s  %d kB" % (path, len(page) // 1024))
        return
    pairs = [("en", os.path.join(ROOT, "books", "read", SLUG, CSLUG, "index.html")),
             ("vi", os.path.join(ROOT, "vi", "books", "read", SLUG, CSLUG, "index.html"))]
    for lang, path in pairs:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        page = build(lang)
        open(path, "w", encoding="utf-8").write(page)
        print("wrote %s  %d kB" % (path, len(page) // 1024))


if __name__ == "__main__":
    main()
