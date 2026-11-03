# -*- coding: utf-8 -*-
"""Handbook Chapter 32 — Temperature (Robert J. Sandberg, ed.)

The chapter is 163 source pages and eleven sections, each contributed by a
different author. Sections are being written in order; §32.1 and §32.2 are
complete.

  §32.1  Bimaterials Thermometers            p3-14    6 figs  19 eqs  5 tables
  §32.2  Resistive Thermometers              p14-26   9 figs   6 eqs  2 tables
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
import re
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


_CUR = [""]
_LANG = [""]


def _slug(t):
    """The anchor for a sub-heading, taken from its English title. Both h3() and
    sec_index() go through here, so a TOC entry can never point at nothing —
    which is what happens if the two sides spell the title differently."""
    s = re.sub(r"<[^>]+>", "", t).lower()
    return re.sub(r"[^a-z0-9]+", "-", s).strip("-")


def h2(t, en="", anchor=None):
    if en == t:
        en = ""
    sid = ""
    if anchor:
        sid = ' id="%s"' % anchor
    if t.startswith("32."):
        head_ = t[3:].split(" ", 1)[0]
        if head_.isdigit():
            _CUR[0] = head_
            if not anchor:
                sid = ' id="s32-%s"' % head_
    return '<h2%s>%s%s</h2>' % (sid, t, (' <span class="en">%s</span>' % en) if en else "")


def h3(t, en="", anchor=None):
    if en == t:
        en = ""
    a = ' id="%s"' % anchor if anchor else ""
    if not a and _CUR[0]:
        # on the Vietnamese page the English title is the second argument; on
        # the English page it is the first
        base = (en or t) if _LANG[0] == "vi" else t
        a = ' id="s32-%s-%s"' % (_CUR[0], _slug(base))
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


def ol(items):
    return ('<ol style="margin:-.2rem 0 1.3rem">%s</ol>'
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


def _t326(lang):
    """Table 32.6 — the three classes of platinum resistance thermometer, with
    what each costs and how much abuse it survives."""
    vi = lang == "vi"
    hd = (["Đầu đo", "Ứng dụng cơ bản", "Nhiệt độ", "Giá", "Kiểu đầu đoᵃ", "Xử lý"]
          if vi else
          ["Probe", "Basic application", "Temperature", "Cost", "Probe styleᵃ", "Handling"])
    rows = [
        ("SPRT", "Hiệu chuẩn SPRT thứ cấp" if vi else "Calibration of Secondary SPRT",
         "−200 đến 1000 °C<br>(−328 đến 1832 °F)", "$5000", "1",
         "Rất dễ vỡ" if vi else "Very fragile"),
        ("SPRT thứ cấp" if vi else "Secondary SPRT", "Dùng trong phòng thí nghiệm" if vi else "Lab use",
         "−200 đến 500 °C<br>(−328 đến 932 °F)", "$700", "1, A",
         "Dễ vỡ" if vi else "Fragile"),
        ("IPRT quấn dây" if vi else "Wirewound IPRT",
         "Dùng hiện trường công nghiệp" if vi else "Industrial field use",
         "−200 đến 648 °C<br>(−328 đến 1200 °F)", "$60–$180", "1, S, A",
         "Bền" if vi else "Rugged"),
        ("IPRT màng mỏng" if vi else "Thin-film IPRT",
         "Dùng hiện trường công nghiệp" if vi else "Industrial field use",
         "−50 đến 260 °C<br>(−200 đến 500 °F)", "$40–$140", "1, S, A",
         "Bền" if vi else "Rugged"),
    ]
    cap = ("Bảng 32.6 · Ba hạng nhiệt kế điện trở bạch kim. ᵃ 1 = ngâm; A = không khí; "
           "S = bề mặt." if vi else
           "Table 32.6 · The three classes of platinum resistance thermometer. ᵃ 1 = immersion; "
           "A = air; S = surface.")
    return table(hd, rows, cap, widths=["17%", "22%", "20%", "11%", "14%", "16%"], small=True)


def _t327(lang):
    """Table 32.7 — the seventeen defining fixed points of ITS-90, in kelvin and
    in degrees Celsius. The two approximate vapour-pressure points are given as
    '≈' in the source and kept that way."""
    vi = lang == "vi"
    hd = (["Chấtᵃ", "Trạng thái cân bằngᵇ", "<i>T</i><sub>90</sub> (K)",
           "<i>t</i><sub>90</sub> (°C)"] if vi else
          ["Materialᵃ", "Equilibrium stateᵇ", "<i>T</i><sub>90</sub> (K)",
           "<i>t</i><sub>90</sub> (°C)"])
    rows = [
        ("He", "VP", "3–5", "−270.15 đến −268.15" if vi else "−270.15 to −268.15"),
        ("e-H₂", "TP", "13.8033", "−259.3467"),
        ("e-H₂ (hoặc He)" if vi else "e-H₂ (or He)", "VP (hoặc GT)" if vi else "VP (or GT)",
         "≈17", "≈−256.16"),
        ("e-H₂ (hoặc He)" if vi else "e-H₂ (or He)", "VP (hoặc GT)" if vi else "VP (or GT)",
         "≈20.3", "≈−252.85"),
        ("Ne", "TP", "24.5561", "−248.5939"),
        ("O₂", "TP", "54.3584", "−218.7916"),
        ("Ar", "TP", "83.8058", "−189.3442"),
        ("Hg", "TP", "234.3156", "−38.8344"),
        ("H₂O", "TP", "273.16", "0.01"),
        ("Ga", "MP", "302.9146", "29.7646"),
        ("In", "FP", "429.7485", "156.5985"),
        ("Sn", "FP", "505.078", "231.928"),
        ("Zn", "FP", "692.677", "419.527"),
        ("Al", "FP", "933.473", "660.323"),
        ("Ag", "FP", "1234.93", "961.78"),
        ("Au", "FP", "1337.33", "1064.18"),
        ("Cu", "FP", "1357.77", "1084.62"),
    ]
    cap = ("Bảng 32.7 · Các điểm cố định định nghĩa của ITS-90. ᵃ e-H₂ chỉ hydro ở trạng thái cân "
           "bằng, nghĩa là hydro có phân bố cân bằng giữa dạng <i>ortho</i> và <i>para</i> ở nhiệt "
           "độ tương ứng. Hydro thường ở nhiệt độ phòng chứa 25% <i>para</i> và 75% <i>ortho</i>. "
           "Thành phần đồng vị của mọi vật liệu là thành phần tự nhiên. ᵇ VP chỉ điểm hay phương "
           "trình áp suất hơi; GT chỉ điểm nhiệt kế khí; TP chỉ điểm ba; FP chỉ điểm đông đặc; "
           "MP chỉ điểm nóng chảy." if vi else
           "Table 32.7 · Defining fixed points of the ITS-90. ᵃ e-H₂ indicates equilibrium hydrogen; "
           "that is, hydrogen with the equilibrium distribution of its <i>ortho</i> and <i>para</i> "
           "forms at the corresponding temperatures. Normal hydrogen at room temperature contains "
           "25% <i>para</i> and 75% <i>ortho</i> hydrogen. The isotopic composition of all materials "
           "is that naturally occurring. ᵇ VP indicates vapour pressure point or equation; GT "
           "indicates gas thermometer point; TP indicates triple point; FP indicates freezing "
           "point; MP indicates melting point.")
    return table(hd, rows, cap, widths=["22%", "26%", "20%", "32%"], small=True)


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


# ================================================================ §32.2
def sec_32_2_vi():
    b = [h2("32.2 Nhiệt kế điện trở", "Resistive Thermometers")]
    b.append(authors("Jim Burns", ""))

    b.append(h3("Giới thiệu về cảm biến nhiệt điện trở",
                "Introduction to Resistance Temperature Detectors"))
    b.append(p(
        "Một cách phổ biến để đo nhiệt độ là dùng cảm biến nhiệt điện trở (Resistive Temperature "
        "Detector — RTD). Những dụng cụ đo điện này cho kết quả đọc nhiệt độ chính xác cao: RTD "
        "công nghiệp đơn giản dùng trong một quy trình chế tạo có độ chính xác ±0,1 °C, còn nhiệt "
        "kế điện trở bạch kim chuẩn (SPRT) chính xác tới ±0,0001 °C."))
    b.append(p(
        "Điện trở của một số kim loại thay đổi theo một quy luật đã biết và dự đoán được, phụ thuộc "
        "vào việc nhiệt độ tăng hay giảm. Khi nhiệt độ tăng, điện trở của kim loại tăng. Khi nhiệt "
        "độ giảm, điện trở giảm. RTD dùng đặc tính này làm cơ sở để đo nhiệt độ."))
    b.append(p(
        "Phần cảm nhận của một RTD, gọi là phần tử, là một cuộn dây đường kính nhỏ, độ tinh khiết "
        "cao, thường làm bằng bạch kim, đồng hoặc niken. Kiểu cấu tạo này được gọi là phần tử quấn "
        "dây. Với phần tử màng mỏng, một màng bạch kim mỏng được lắng lên một đế gốm."))
    b.append(p(
        "Bạch kim là lựa chọn phổ biến cho cảm biến RTD vì nó ổn định lâu dài ở nhiệt độ cao. Bạch "
        "kim tốt hơn đồng và niken vì nó trơ về mặt hóa học, chịu oxy hóa tốt và làm việc được trong "
        "dải nhiệt độ rộng hơn."))
    b.append(p(
        "Khi vận hành, dụng cụ đo cho một dòng điện không đổi chạy qua RTD. Khi nhiệt độ thay đổi, "
        "điện trở thay đổi và điện áp tương ứng cũng thay đổi. Phép đo này sau đó được chuyển thành "
        "giá trị nhiệt độ bằng máy tính. Các phương trình làm khớp đường cong được dùng để xác định "
        "quan hệ điện trở – nhiệt độ này. RTD sau đó có thể dùng để xác định nhiệt độ bất kỳ từ "
        "điện trở đo được."))
    b.append(p(
        "Một kỹ thuật đo điển hình cho nhiệt kế công nghiệp là cho một dòng điện không đổi (0,8 mA "
        "đến 1,0 mA) chạy qua cảm biến, rồi đo điện áp sinh ra trên cảm biến bằng kỹ thuật vôn kế "
        "số. Kỹ thuật này đơn giản và có vài phương pháp hiệu chỉnh sai số được áp dụng."))
    b.append(p(
        "Trong phòng thí nghiệm, khi cần độ chính xác đo từ 10 ppm trở lên, người ta dùng thiết bị "
        "đo chuyên dụng. Các cầu đo và vôn kế số độ chính xác cao có chức năng hiệu chỉnh sai số "
        "đặc biệt được sử dụng. Độ chính xác của thiết bị đo cao cấp có thể đạt 0,1 ppm (phần "
        "triệu). Những dụng cụ này có chức năng bù các sai số như điện áp nhiệt điện và tự đốt nóng "
        "của phần tử."))
    b.append(p(
        "Ngoài nhiệt độ, ứng suất và tạp chất trong dây cũng ảnh hưởng đến đặc tính điện trở – "
        "nhiệt độ của cảm biến. Quy tắc Matthiessen phát biểu rằng điện trở suất (<i>ρ</i>) của một "
        "dây dẫn kim loại phụ thuộc vào nhiệt độ, tạp chất và biến dạng. <i>ρ</i> được đo bằng "
        "(Ω cm):"))
    b.append(eq("<i>ρ</i>(total) = <i>ρ</i>(temperature) + <i>ρ</i>(impurities) + "
                "<i>ρ</i>(deformation)", "32.20"))
    b.append(p(
        "Thiết kế hợp lý và chọn vật liệu cẩn thận sẽ giảm thiểu các ảnh hưởng này, để điện trở "
        "suất chỉ thay đổi khi nhiệt độ thay đổi."))

    b.append(h3("Điện trở của kim loại", "Resistance of Metals"))
    b.append(p(
        "Dù phần tử của RTD được làm bằng bạch kim, đồng hay niken, mỗi loại kim loại có độ nhạy, "
        "độ chính xác và dải nhiệt độ khác nhau. Độ nhạy được định nghĩa là mức thay đổi điện trở "
        "của cảm biến trên mỗi độ thay đổi nhiệt độ. Hình 32.7 cho thấy độ nhạy của các kim loại "
        "thông dụng nhất dùng chế tạo RTD."))
    b.append(fig(7, F.fig(7), "vi"))
    b.append(p(
        "Bạch kim, một kim loại quý, có quan hệ điện trở – nhiệt độ ổn định nhất trên dải nhiệt độ "
        "rộng nhất −184,44 °C (−300 °F) đến 648,88 °C (1200 °F). Phần tử niken có dải nhiệt độ hạn "
        "chế vì mức thay đổi điện trở trên mỗi độ trở nên rất phi tuyến ở nhiệt độ trên 300 °C "
        "(572 °F). Đồng có quan hệ điện trở – nhiệt độ rất tuyến tính. Tuy nhiên, đồng bị oxy hóa ở "
        "nhiệt độ vừa phải và không dùng được trên 150 °C (302 °F)."))
    b.append(p(
        "Bạch kim là kim loại tốt nhất cho phần tử RTD vì ba lý do. Nó tuân theo quan hệ điện trở – "
        "nhiệt độ rất tuyến tính; nó tuân theo quan hệ đó một cách lặp lại được trên toàn dải nhiệt "
        "độ; và nó có dải nhiệt độ rộng nhất trong các kim loại dùng chế tạo RTD. Bạch kim không "
        "phải kim loại nhạy nhất; tuy vậy, nó là kim loại mang lại độ ổn định lâu dài tốt nhất."))
    b.append(p(
        "Độ chính xác của RTD tốt hơn đáng kể so với cặp nhiệt điện trong dải nhiệt độ thông thường "
        "của RTD, −184,44 °C (−300 °F) đến 648,88 °C (1200 °F). RTD cũng được biết đến với độ ổn "
        "định và độ lặp lại cao. Có thể tháo chúng khỏi thiết bị và hiệu chuẩn lại để có độ chính "
        "xác kiểm chứng được, đồng thời kiểm tra xem có trôi không."))

    b.append(h3("Ai dùng RTD? Các cụm lắp và ứng dụng thông dụng",
                "Who Uses RTDs? Common Assemblies and Applications"))
    b.append(p(
        "Các ứng dụng khác nhau cần các loại RTD khác nhau. Một nhiệt kế điện trở bạch kim (PRT) "
        "ngâm trực tiếp cùng một đầu nối có thể dùng cho đường ống vận tốc thấp, bồn chứa hoặc đo "
        "nhiệt độ không khí. Một PRT lò xo nén, đầu nối kiểu nhiệt ngẫu và đầu nối thường được dùng "
        "trong đường ống hoặc bồn chứa. Một cảm biến nhiệt độ kiểu lấy trung bình cảm nhận và đo "
        "nhiệt độ dọc theo toàn bộ vỏ bọc của nó, chiều dài có thể từ 1 đến 20 m. Một cảm biến nhiệt "
        "độ dưới nước hạng nặng được thiết kế để ngâm hoàn toàn dưới sông, ao làm mát hoặc cống. Đây "
        "chỉ là vài ví dụ về cấu hình và ứng dụng RTD."))

    b.append(h3("Tổng quan về RTD bạch kim", "Overview of Platinum RTDs"))
    b.append(p(
        "Có ba hạng chính của nhiệt kế điện trở bạch kim (PRT): nhiệt kế điện trở bạch kim chuẩn "
        "(SPRT), nhiệt kế điện trở bạch kim chuẩn thứ cấp (SPRT thứ cấp) và nhiệt kế điện trở bạch "
        "kim công nghiệp (IPRT). Bảng 32.6 trình bày thông tin về từng loại."))
    b.append(_t326("vi"))

    b.append(h3("Hệ số nhiệt độ của điện trở", "Temperature Coefficient of Resistance"))
    b.append(p(
        "Mỗi kim loại khác nhau dùng làm phần tử cảm nhận (bạch kim, niken, đồng) có mức thay đổi "
        "điện trở tương đối khác nhau trên mỗi đơn vị thay đổi nhiệt độ. Thước đo độ nhạy của nhiệt "
        "kế điện trở là hệ số nhiệt độ của điện trở. Nó được định nghĩa là mức thay đổi điện trở "
        "trên mỗi độ C thay đổi nhiệt độ, trên mỗi ohm điện trở cảm biến, trên dải 0 °C đến 100 °C."))
    b.append(p(
        "Giá trị alpha là mức thay đổi trung bình của điện trở trên mỗi độ C trên mỗi ohm điện trở. "
        "Mức thay đổi thực tế của điện trở trên mỗi độ C trên mỗi ohm là lớn nhất ở −200 °C và giảm "
        "đều khi nhiệt độ sử dụng tăng."))
    b.append(p(
        "Đơn vị của hệ số là Ω/Ω °C⁻¹. Đây được gọi là giá trị alpha và thường được ký hiệu bằng "
        "chữ Hy Lạp <i>α</i>. Hệ số nhiệt độ càng lớn thì mức thay đổi điện trở càng lớn với cùng "
        "một mức thay đổi nhiệt độ. Trong các kim loại RTD thông dụng, niken có hệ số nhiệt độ cao "
        "nhất, 0,00672, còn đồng là 0,00427. Giá trị <i>α</i> của cảm biến được tính bằng phương "
        "trình:"))
    b.append(eq("<i>α</i> = (<i>R</i><sub>100</sub> − <i>R</i><sub>0</sub>) / "
                "(100 °C × <i>R</i><sub>0</sub>)", "32.21"))
    b.append(wl([
        "trong đó <i>R</i><sub>0</sub> = điện trở của cảm biến ở 0 °C",
        "<i>R</i><sub>100</sub> = điện trở của cảm biến ở 100 °C",
    ]))
    b.append(p("Ba hệ số nhiệt độ chính được quy định cho bạch kim:"))
    b.append(ol([
        "ITS-90, thang nhiệt độ chuẩn được quốc tế chấp nhận, yêu cầu hệ số nhiệt độ tối thiểu "
        "0,003925 đối với SPRT. Hệ số này đạt được bằng dây có độ tinh khiết cao (99,9999% hoặc "
        "hơn) được quấn trong một cấu hình không ứng suất.",
        "Với dây bạch kim cấp chuẩn dùng trong phần tử công nghiệp, hệ số nhiệt độ là 0,003902.",
        "IEC 751 [1] và ASTM 1137 [2] đã chuẩn hóa hệ số nhiệt độ của bạch kim là 0,0038500.",
    ]))

    b.append(h3("Cấu tạo RTD", "RTD Construction"))
    b.append(p(
        "Nhiệt kế điện trở bạch kim chuẩn (SPRT), loại nhiệt kế bạch kim chính xác nhất, dễ vỡ và "
        "chỉ dùng trong môi trường phòng thí nghiệm (Hình 32.8). Vật liệu dễ vỡ không đủ độ bền và "
        "khả năng chống rung cho môi trường công nghiệp. SPRT có độ lặp lại cao và độ trôi thấp, "
        "nhưng chúng đắt hơn vì vật liệu và kỹ thuật chế tạo."))
    b.append(fig(8, F.fig(8), "vi"))
    b.append(p(
        "Các phần tử SPRT được quấn từ dây bạch kim độ tinh khiết cao, đường kính lớn. Dây dẫn bên "
        "trong thường làm bằng bạch kim, giá đỡ bên trong làm bằng thạch anh hoặc thủy tinh silica "
        "nóng chảy. SPRT được dùng trên dải nhiệt độ rất rộng, từ −200 °C (−328 °F) đến trên "
        "1000 °C (1832 °F). Với SPRT dùng để đo nhiệt độ tới 660 °C (1220 °F), điện trở ở điểm băng "
        "thường là 25,5 Ω. Với nhiệt kế nhiệt độ cao, điện trở ở điểm băng là 2,5 Ω hoặc 0,25 Ω. Đầu "
        "đo SPRT có thể chính xác tới ±0,001 °C (0,0018 °F) nếu dùng đúng cách."))
    b.append(p(
        "Nhiệt kế điện trở bạch kim chuẩn thứ cấp (SPRT thứ cấp) cũng dành cho môi trường phòng thí "
        "nghiệm (Hình 32.9). Chúng được cấu tạo giống SPRT, nhưng vật liệu rẻ hơn, thường là dây "
        "bạch kim độ tinh khiết cao cấp chuẩn, vỏ kim loại và cách điện gốm. Dây dẫn bên trong "
        "thường là hợp kim gốc niken. Cảm biến thứ cấp bị giới hạn về nhiệt độ trên dải −200 °C "
        "(−328 °F) đến 500 °C (932 °F) — và chính xác tới ±0,03 °C (±0,054 °F) trên dải nhiệt độ "
        "của chúng."))
    b.append(fig(9, F.fig(9), "vi"))
    b.append(p(
        "Nhiệt kế chuẩn thứ cấp chịu được một mức va chạm nhất định, dù vẫn khá nhạy với ứng suất. "
        "Xử lý thô bạo, rung và sốc sẽ làm dịch chuyển điểm hiệu chuẩn. Điện trở danh định ở điểm "
        "băng thường là 100 Ω. Điều này đơn giản hóa quy trình hiệu chuẩn khi hiệu chuẩn các RTD "
        "100 Ω khác. Hệ số nhiệt độ của chuẩn thứ cấp dùng dây bạch kim cấp chuẩn thường là "
        "0,00392 Ω Ω⁻¹ °C⁻¹ hoặc cao hơn."))
    b.append(p(
        "Nhiệt kế điện trở bạch kim công nghiệp (IPRT) được thiết kế để chịu được môi trường công "
        "nghiệp và bền gần như cặp nhiệt điện (Hình 32.10). IEC 751 [1] và ASTM 1137 [2] quy định "
        "các yêu cầu đối với nhiệt kế điện trở bạch kim công nghiệp. Dải nhiệt độ thông dụng nhất là "
        "−200 °C (−328 °F) đến 500 °C (932 °F). Mẫu tiêu chuẩn có thể hoán đổi với độ chính xác "
        "±0,25 °C (±0,45 °F) đến ±2,5 °C (±4,5 °F) trên dải nhiệt độ của chúng."))
    b.append(fig(10, F.fig(10), "vi"))
    b.append(p(
        "Có sẵn nhiều kiểu thiết kế phần tử cho các ứng dụng khác nhau. Một cấu hình phổ biến là "
        "phần tử quấn dây (Hình 32.11). Thiết kế bền này được phát triển để thay thế SPRT dễ vỡ. Dây "
        "cảm nhận bạch kim nhỏ (thường từ 7 đến 50 μm, tức 0,0003 in. đến 0,002 in. đường kính) được "
        "quấn không cảm ứng quanh một lõi gốm hình trụ, và thường được phủ một lớp vật liệu mỏng tạo "
        "cách điện và bảo vệ cơ học. Vì dây cảm nhận được đỡ chắc chắn, nó không thể giãn và co tự "
        "do như dây bạch kim không được đỡ của SPRT. Kiểu phần tử này có độ bền cao hơn SPRT và "
        "chuẩn thứ cấp, cùng độ chính xác rất tốt cho hầu hết ứng dụng công nghiệp."))
    b.append(fig(11, F.fig(11), "vi"))
    b.append(p(
        "Trong một thiết kế quấn dây khác, kiểu treo cuộn dây, một cuộn dây bạch kim mảnh được lắp "
        "vào các lỗ nhỏ trong một lõi gốm hình trụ (Hình 32.12). Các cuộn dây được đỡ bằng bột gốm "
        "hoặc xi măng, và bịt kín ở cả hai đầu. Khi bột gốm được đóng gói lỏng trong các lỗ của lõi, "
        "phần tử có thể giãn và co tự do. Điều này giảm ảnh hưởng của ứng suất lên đặc tính điện "
        "trở, mang lại độ chính xác và độ ổn định rất cao khi dùng cho chuẩn nhiệt độ thứ cấp và "
        "các ứng dụng công nghiệp nhẹ (ít hoặc không rung, sốc). Những cải tiến gần đây về vật liệu "
        "gốm giúp cuộn dây cảm nhận ổn định hơn — nó có thể duy trì độ chính xác 0,03 °C sau hàng "
        "nghìn giờ ở nhiệt độ 500 °C. Các loại bột gốm này đỡ cuộn dây trong lõi và giữ chúng cố "
        "định tại chỗ với ứng suất tối thiểu."))
    b.append(fig(12, F.fig(12), "vi"))
    b.append(p(
        "Phần tử màng mỏng rất nhỏ, thường dưới 1,6 mm (1/16 in.) vuông (Hình 32.13). Chúng được chế "
        "tạo bằng các kỹ thuật tương tự dùng để chế tạo mạch tích hợp. Đầu tiên, một màng bạch kim "
        "mỏng được lắng lên một đế gốm. Một số nhà sản xuất dùng kỹ thuật in quang khắc để khắc "
        "màng bạch kim đã lắng, để lại hình mẫu phần tử trên đế gốm. Sau đó, bề mặt phần tử được phủ "
        "vật liệu thủy tinh để bảo vệ phần tử khỏi độ ẩm và chất nhiễm."))
    b.append(fig(13, F.fig(13), "vi"))
    b.append(p(
        "Dải nhiệt độ của phần tử bạch kim màng mỏng là −50 °C (−58 °F) đến 400 °C (752 °F); độ "
        "chính xác từ 0,5 °C (0,9 °F) đến 2,0 °C (3,6 °F). Phần tử màng mỏng thông dụng nhất có "
        "điện trở điểm băng 100 Ω và hệ số nhiệt độ 0,00385 °C."))
    b.append(p(
        "RTD màng mỏng có thể rất bền khi dây dẫn đường kính nhỏ và màng mỏng được bảo vệ đúng "
        "cách. Độ chính xác và độ ổn định có thể không tốt bằng một số phần tử quấn dây do hiện "
        "tượng trễ, sai số ổn định dài hạn và sai số tự đốt nóng."))

    b.append(h3("Sai số tự đốt nóng", "Self-heating Errors"))
    b.append(p(
        "Dòng điện dùng để đo điện trở cảm biến cũng làm nóng cảm biến. Hiện tượng này được gọi là "
        "đốt nóng I²R hay đốt nóng Joule. Do hiệu ứng này, nhiệt độ chỉ thị của cảm biến cao hơn "
        "nhiệt độ thực một chút. Sự không nhất quán này thường được gọi là sai số tự đốt nóng. Sai "
        "số tự đốt nóng, phụ thuộc vào ứng dụng, có thể từ không đáng kể đến 1 °C. Sai số đốt nóng "
        "lớn nhất xảy ra do truyền nhiệt kém giữa phần tử cảm nhận và ứng dụng, hoặc do dùng dòng "
        "điện quá lớn khi đo điện trở."))
    b.append(p("Các phương pháp sau đây để giảm sai số tự đốt nóng."))
    b.append(ol([
        "Giảm thiểu công suất tiêu tán trong cảm biến. Có sự đánh đổi giữa mức tín hiệu và tự đốt "
        "nóng của cảm biến. Thông thường, dùng dòng 1 mA làm dòng cảm nhận.",
        "Dùng cảm biến có trở nhiệt thấp. Trở nhiệt của cảm biến càng thấp thì cảm biến tản công "
        "suất I²R càng tốt và mức tăng nhiệt trong cảm biến càng thấp. Hằng số thời gian nhỏ cho "
        "thấy cảm biến có trở nhiệt thấp.",
        "Tối đa hóa tiếp xúc nhiệt giữa cảm biến và ứng dụng.",
    ]))

    b.append(h3("Hiệu chuẩn", "Calibration"))
    b.append(p(
        "Các chương trình kiểm tra là thiết yếu để xác minh độ chính xác của PRT. Một số IPRT được "
        "hiệu chuẩn tại nhà máy ở một nhiệt độ như điểm băng, nhưng người dùng PRT có thể muốn hiệu "
        "chuẩn chúng ở các nhiệt độ khác, tùy ứng dụng."))
    b.append(p(
        "Kết quả hiệu chuẩn có thể được so sánh với các lần hiệu chuẩn trước đó của cùng dụng cụ. "
        "Điều này sẽ xác định liệu có cần sửa chữa hoặc thay thế dụng cụ, hay có cần hiệu chuẩn "
        "thường xuyên hơn."))
    b.append(p(
        "Vì sửa chữa và hiệu chuẩn thường xuyên thường tốn kém, người mua và người chỉ định PRT có "
        "thể muốn điều tra các RTD khác nhau trước khi lắp đặt bằng cách tham khảo ASTM Standard "
        "#E1137-95 [2], do American Society for Testing and Materials (ASTM) xuất bản."))
    b.append(p(
        "<i>Tần suất.</i> Độ ổn định của RTD phụ thuộc vào môi trường làm việc. Nhiệt độ cao có thể "
        "gây trôi và nhiễm bẩn dây bạch kim. Nhiệt độ càng cao, trôi xảy ra càng nhanh. Dưới 400 °C, "
        "trôi do nhiệt độ cao không phải vấn đề đáng kể, nhưng nhiệt độ tới 500 °C đến 600 °C là "
        "nguyên nhân chính gây trôi — tới vài độ mỗi năm. Sốc mạnh có thể làm hỏng cảm biến ngay lập "
        "tức và gây hỏng. Va đập, rung và xử lý thô bạo sẽ tạo ứng suất trong dây bạch kim và thay "
        "đổi đặc tính của nó, đồng thời có thể làm hỏng toàn bộ phần tử. Nếu cảm biến không được bịt "
        "kín đúng cách, hơi ẩm có thể vào trong cảm biến và gây ra một số vấn đề với điện trở cách "
        "điện. Vì nước trong hơi ẩm dẫn điện, nó sẽ nằm giữa các dây dẫn và phần tử cảm nhận, và về "
        "cơ bản làm ngắn mạch điện trở của dây phần tử. Trong điều kiện vận hành khắc nghiệt, nên "
        "hiệu chuẩn cảm biến hàng tháng hoặc hai tháng một lần. Nếu hoàn thành năm lần hiệu chuẩn "
        "trở lên mà không có thay đổi đáng kể, thì có thể tăng gấp đôi khoảng thời gian giữa các lần "
        "hiệu chuẩn; tuy nhiên, nên hiệu chuẩn ít nhất mỗi năm một lần."))
    b.append(p(
        "<i>Kỹ thuật.</i> Hai phương pháp hiệu chuẩn thông dụng là phương pháp điểm cố định và "
        "phương pháp so sánh."))
    b.append(p(
        "<i>Hiệu chuẩn bằng điểm cố định</i>, dùng cho độ chính xác cao nhất, dùng điểm ba, điểm "
        "đông đặc hoặc điểm nóng chảy của các chất tinh khiết như nước, kẽm, thiếc và agon để tạo ra "
        "một nhiệt độ đã biết và lặp lại được (Hình 32.14). Các tế bào điểm cố định được bịt kín để "
        "ngăn nhiễm bẩn và ngăn điều kiện khí quyển ảnh hưởng đến nhiệt độ của tế bào. Các tế bào "
        "này cho phép người dùng tái tạo các điều kiện thực tế của thang nhiệt độ ITS-90."))
    b.append(fig(14, F.fig(14), "vi"))
    b.append(p(
        "Hiệu chuẩn bằng điểm cố định mang lại độ chính xác rất cao (trong khoảng ±0,001 °C), nhưng "
        "các tế bào tốn thời gian sử dụng và mỗi lần chỉ chứa được một cảm biến. Vì lý do này, chúng "
        "không được dùng rộng rãi khi hiệu chuẩn cảm biến công nghiệp. Mỗi tế bào điểm cố định có "
        "một quy trình riêng để đạt được điểm cố định."))
    b.append(p("Một quy trình tổng quát để hiệu chuẩn bằng điểm cố định như sau:"))
    b.append(ol([
        "Chuẩn bị tế bào. Có các quy trình khác nhau cho mỗi điểm cố định.",
        "Đưa nhiệt kế cần hiệu chuẩn vào.",
        "Để hệ thống ổn định. Thời gian ổn định phụ thuộc vào nhiệt kế và tế bào điểm cố định. "
        "Thông thường, 15 đến 30 phút là đủ.",
        "Đo điện trở của nhiệt kế. Để có độ chính xác đo cao nhất, dùng cầu đo điện trở chuyên "
        "dụng. Chúng có độ chính xác trong khoảng 10 ppm đến 0,1 ppm.",
    ]))
    b.append(p(
        "Một phương pháp hiệu chuẩn bằng điểm cố định thông dụng cho đầu đo công nghiệp là bể nước "
        "đá. Thiết bị này rẻ, dễ dùng và có thể chứa nhiều cảm biến cùng lúc. Điểm băng được chỉ "
        "định làm chuẩn thứ cấp vì độ chính xác của nó là ±0,005 °C (±0,009 °F), so với ±0,001 °C "
        "(±0,0018 °F) đối với các điểm cố định sơ cấp."))
    b.append(p(
        "Trong <i>hiệu chuẩn so sánh</i>, thường dùng với SPRT thứ cấp và RTD công nghiệp, các nhiệt "
        "kế cần hiệu chuẩn được so sánh với nhiệt kế đã hiệu chuẩn bằng một bể đẳng nhiệt có nhiệt "
        "độ ổn định đồng đều (Hình 32.15). Khác với hiệu chuẩn bằng điểm cố định, phép so sánh có "
        "thể thực hiện ở bất kỳ nhiệt độ nào trong khoảng −100 °C (−148 °F) và 500 °C (932 °F). "
        "Phương pháp này có thể tiết kiệm chi phí hơn vì có thể hiệu chuẩn nhiều cảm biến đồng thời "
        "bằng thiết bị tự động."))
    b.append(fig(15, F.fig(15), "vi"))
    b.append(p(
        "Các bể đẳng nhiệt này, được đốt nóng bằng điện và khuấy đều, dùng dầu silicone làm môi "
        "trường cho nhiệt độ từ −100 °C (−148 °F) đến 200 °C (392 °F), và muối nóng chảy cho nhiệt "
        "độ trên 200 °C (392 °F). Ở nhiệt độ trên 500 °C (932 °F), người ta dùng lò không khí hoặc "
        "tầng sôi, nhưng chúng kém ổn định đồng đều hơn đáng kể."))
    b.append(p("Quy trình hiệu chuẩn so sánh như sau:"))
    b.append(ol([
        "Đưa nhiệt kế chuẩn và các nhiệt kế cần hiệu chuẩn vào bể.",
        "Để bể ổn định.",
        "Đo điện trở của chuẩn để xác định nhiệt độ của bể.",
        "Đo điện trở của từng nhiệt kế đang hiệu chuẩn.",
    ]))
    b.append(p(
        "<i>Suy ra quan hệ điện trở – nhiệt độ của một PRT.</i> Sau khi xác định điện trở của PRT, "
        "có thể xác định các hệ số hiệu chuẩn. Bằng cách thay các giá trị này vào một phương trình, "
        "có thể suy ra nhiệt độ từ bất kỳ điện trở đo được nào. Hai kỹ thuật làm khớp đường cong "
        "thông dụng nhất là phương trình ITS-90 và Callendar–Van Dusen."))
    b.append(p(
        "Ngày 1 tháng 1 năm 1990, Thang Nhiệt độ Quốc tế 1990 (ITS-90) trở thành thang nhiệt độ quốc "
        "tế chính thức [3]. ITS-90 kéo dài lên trên từ 0,65 K (−272,5 °C hay −458,5 °F) và định "
        "nghĩa nhiệt độ từ 0,65 K (0,65 °C trên độ không tuyệt đối) trở lên bằng các điểm cố định "
        "(xem Bảng 32.7)."))
    b.append(_t327("vi"))
    b.append(p(
        "Hai hàm quy chiếu được dùng để định nghĩa hệ số nhiệt độ của một SPRT lý tưởng: một cho "
        "nhiệt độ dưới 0 °C và một cho nhiệt độ trên 0 °C. Khi một PRT được hiệu chuẩn theo ITS-90, "
        "các hệ số xác định trong hiệu chuẩn được dùng để mô tả một hàm độ lệch biểu diễn hiệu giữa "
        "điện trở của PRT chuẩn và hàm quy chiếu ở mọi nhiệt độ trong dải. Dùng các hệ số hiệu chuẩn "
        "và hàm độ lệch, có thể dùng SPRT để xác định nhiệt độ bất kỳ từ điện trở đo được. Vì các "
        "phương trình ITS-90 phức tạp, cần phần mềm máy tính để tính chính xác."))
    b.append(p("ITS-90 ảnh hưởng đến:"))
    b.append(ul([
        "Các phòng thí nghiệm chuẩn và hiệu chuẩn nhiệt độ",
        "Người dùng SPRT chuẩn và chuẩn thứ cấp có liên kết truy xuất tới các phòng thí nghiệm chuẩn",
        "Người dùng hệ thống đo và điều khiển nhiệt độ trong các công ty quan tâm đến quản lý chất "
        "lượng có thể kiểm chứng",
    ]))
    b.append(p(
        "Viện Tiêu chuẩn và Công nghệ Quốc gia (NIST) đã xuất bản Technical Note 1265, "
        "<i>Guidelines for Realizing the International Temperature Scale of 1990 (ITS-90)</i> [4]. "
        "Không phải mọi người dùng PRT đều cần theo các phương trình phức tạp và chương trình máy "
        "tính gắn với ITS-90. Theo nguyên tắc chung: nếu yêu cầu độ không đảm bảo đo tối thiểu nhỏ "
        "hơn 0,1 °C, có lẽ nên dùng ITS-90. Với độ không đảm bảo đo lớn hơn 0,1 °C, ảnh hưởng của "
        "sự thay đổi thang đo là tương đối nhỏ và không bị ảnh hưởng."))
    b.append(p(
        "Các phương trình Callendar–Van Dusen là phương trình nội suy mô tả quan hệ nhiệt độ – điện "
        "trở của PRT công nghiệp. Những phương trình bậc hai và bậc bốn dễ dùng này có thể được lập "
        "trình dễ dàng vào nhiều bộ điều khiển điện tử. Phương trình cho dải nhiệt độ 0 °C (32 °F) "
        "đến 850 °C (1562 °F) là:"))
    b.append(eq("<i>R</i>(<i>t</i>) = <i>R</i><sub>0</sub>(1 + <i>At</i> + <i>Bt</i>²)", "32.22"))
    b.append(p("Cho dải nhiệt độ −200 °C (−392 °F) đến 0 °C (32 °F):"))
    b.append(eq("<i>R</i>(<i>t</i>) = <i>R</i><sub>0</sub>[1 + <i>At</i> + <i>Bt</i>² + "
                "<i>C</i>(<i>t</i> − 100)<i>t</i>³]", "32.23"))
    b.append(wl([
        "trong đó <i>R</i>(<i>t</i>) = điện trở của PRT ở nhiệt độ <i>t</i>",
        "<i>t</i> = nhiệt độ tính bằng °C",
        "<i>R</i><sub>0</sub> = điện trở danh định của PRT ở 0 °C",
        "<i>α</i>, <i>δ</i>, <i>β</i> = các hệ số hiệu chuẩn",
    ]))
    b.append(p(
        "Để xác định nhiệt độ từ một điện trở đo được, cần một bộ phương trình và hệ số hiệu chuẩn "
        "khác. Với nhiệt độ lớn hơn 0 °C (điện trở đo được lớn hơn điện trở điểm băng đã biết của "
        "PRT):"))
    b.append(eq("<i>t</i>(°C) = [(<i>R</i><sub><i>t</i></sub> − <i>R</i><sub>0</sub>) / "
                "(<i>αR</i><sub>0</sub>)] + <i>δ</i>[(<i>t</i>/100) − 1](<i>t</i>/100)", "32.24"))
    b.append(p(
        "Với nhiệt độ nhỏ hơn 0 °C (điện trở đo được nhỏ hơn điện trở điểm băng đã biết của PRT):"))
    b.append(eq("<i>t</i>(°C) = [(<i>R</i><sub><i>t</i></sub> − <i>R</i><sub>0</sub>) / "
                "(<i>αR</i><sub>0</sub>)] + <i>δ</i>[(<i>t</i>/100) − 1](<i>t</i>/100) + "
                "<i>β</i>[(<i>t</i>/100) − 1](<i>t</i>/100)³", "32.25"))
    b.append(wl([
        "trong đó <i>t</i> = nhiệt độ cần tính",
        "<i>R</i>(<i>t</i>) = điện trở đo được ở nhiệt độ chưa biết",
        "<i>R</i><sub>0</sub> = điện trở của cảm biến ở 0 °C",
        "<i>α</i>, <i>δ</i>, <i>β</i> = các hệ số",
    ]))
    b.append(p(
        "Để xác định đúng nhiệt độ từ một điện trở cho trước bằng các phương trình này, phải lặp "
        "các phương trình ít nhất năm lần. Sau mỗi lần tính, giá trị nhiệt độ mới (<i>t</i>) được "
        "thay trở lại vào phương trình. Giá trị nhiệt độ tính được sẽ hội tụ về giá trị thực của nó. "
        "Sau năm lần lặp, nhiệt độ tính được phải nằm trong khoảng ±0,001 °C so với giá trị thực."))
    b.append(p(
        "Với cảm biến công nghiệp, một phương pháp thay thế là dùng các đường khớp bình phương tối "
        "thiểu phi tuyến để tạo ra quan hệ nhiệt độ/điện trở. Tuy nhiên, không nên dùng các phương "
        "pháp này cho nhiệt kế thứ cấp và sơ cấp vì chúng không khớp đủ với thang ITS-90 đã định "
        "nghĩa. Có thể có sai số khớp đường cong tới 0,05 °C."))

    b.append(h3("Sử dụng RTD ngày nay", "Usage of RTDs Today"))
    b.append(p(
        "Trong toàn ngành công nghiệp, việc sử dụng RTD đang tăng lên vì nhiều lý do. Với sự ra đời "
        "của thời đại máy tính, các ngành công nghiệp nhận ra nhu cầu đo nhiệt độ tốt hơn, và một "
        "tín hiệu điện đi kèm với những tiến bộ trong thiết bị đo quá trình được vi tính hóa. RTD "
        "tạo ra tín hiệu điện; và vì điều khiển tự động trong các nhà máy công nghiệp, nó giúp giao "
        "tiếp với bộ điều khiển quá trình trở nên đơn giản và dễ dàng hơn. Với trọng tâm là tái cấu "
        "trúc, các công ty đang tìm cách cải thiện quy trình. Đo và điều khiển nhiệt độ tốt hơn là "
        "một cách tốt để tiết kiệm năng lượng, giảm chất thải vật liệu, giảm chi phí và cải thiện "
        "hiệu quả vận hành tổng thể."))
    b.append(p(
        "Các quy định của chính phủ là một lý do khác khiến RTD ngày càng phổ biến. Trong ngành dược "
        "phẩm, FDA [5] yêu cầu thẩm định; trong đó có việc thẩm định rằng phép đo nhiệt độ là chính "
        "xác. Các quy định mới hiện đang được soạn thảo cho ngành thực phẩm [6]."))
    b.append(p(
        "Sự chấp nhận ngày càng tăng của các tiêu chuẩn ISO 9000 trên toàn thế giới đã buộc các "
        "công ty phải hiệu chuẩn hệ thống và thiết bị đo nhiệt độ của họ. Ngoài ra, việc hiệu chuẩn "
        "phải được ghi thành văn bản và phải truy xuất được tới một chuẩn quốc gia, hợp pháp được "
        "công nhận."))
    b.append(p(
        "RTD an toàn với môi trường. Với nhiệt kế thủy ngân, việc thải bỏ thủy ngân là một vấn đề. "
        "Trong nhiều ngành công nghiệp, chỉ riêng sự hiện diện của nhiệt kế thủy ngân đã là một "
        "rủi ro."))

    b.append(h3("Ví dụ về ứng dụng tiên tiến cho đo nhiệt độ tới hạn",
                "Examples of Advanced Applications for Critical Temperature Measurement"))
    b.append(p(
        "Công nghệ RTD cho phép thiết kế tùy chỉnh trong nhiều ứng dụng và ngành công nghiệp. Trong "
        "nhiều trường hợp, RTD trở thành một phần không thể tách rời của một ứng dụng tiên tiến khi "
        "nhiệt độ là yếu tố tới hạn."))
    b.append(p(
        "Các nhà máy điện dùng cảm biến RTD để theo dõi nhiên liệu và chất làm mát của bộ trao đổi "
        "nhiệt vào và ra. Đo nhiệt độ chính xác cũng rất quan trọng đối với các nhà máy điện hạt "
        "nhân để thực hiện các thử nghiệm rò rỉ áp suất trên bình chứa bao quanh lõi lò phản ứng."))
    b.append(p(
        "Các nhà sản xuất vi xử lý cần kiểm soát nhiệt độ chính xác trong toàn bộ khu vực phòng sạch "
        "của họ. Nhiệt độ không khí là yếu tố tới hạn đối với sản xuất; nhiều điểm đo nhiệt độ phải "
        "chính xác ±0,028 °C (±0,05 °F). Để đạt được điều này, một RTD được hiệu chuẩn với một bộ "
        "phát nhiệt độ. Cặp đôi khớp này đảm bảo mức chính xác cao nhất của hệ thống và loại bỏ sai "
        "số không hoán đổi được của RTD."))

    b.append(h3("Tương lai của công nghệ RTD", "The Future of RTD Technology"))
    b.append(p(
        "Tương lai của công nghệ RTD được thúc đẩy bởi nhu cầu của người dùng cuối và các vấn đề "
        "chưa được giải quyết. Ví dụ, nhu cầu về RTD công nghiệp nhiệt độ cao tồn tại cho các ứng "
        "dụng trên 600 °C (1200 °F). Để hoạt động ở nhiệt độ cao, phần tử bạch kim của RTD phải được "
        "bảo vệ khỏi nhiễm bẩn. Tuy nhiên, vật liệu vỏ có thể là vấn đề vì ở nhiệt độ cao, nó sẽ "
        "phản ứng với oxy trong không khí và sinh ra các hạt kim loại có thể bám vào bạch kim."))
    b.append(p(
        "RTD phải đủ bền về mặt cơ học để chịu được nhiệt độ cao hơn. Một RTD công nghiệp nhiệt độ "
        "cao sẽ cần một vỏ chịu nhiệt, có lẽ là Inconel 600. Ngoài ra, các thành phần cảm biến phải "
        "được thiết kế và chế tạo để chịu được nhiệt độ cực cao. Một số RTD được quy định hoạt động "
        "trên 600 °C (1200 °F), nhưng khi thử nghiệm, chúng không phải lúc nào cũng đáng tin cậy. "
        "Trôi và không lặp lại là những vấn đề cần được quan tâm thêm."))
    b.append(p(
        "Những tiến bộ trong hiệu chuẩn RTD mang lại cải tiến đáng kể cho việc đo và điều khiển "
        "nhiệt độ. Các công nghệ đo mới kết hợp với kỹ thuật tính toán mạnh mẽ đã đơn giản hóa quy "
        "trình hiệu chuẩn và làm cho nó đáng tin cậy hơn."))
    b.append(p(
        "Một lĩnh vực tăng trưởng hiện nay là hiệu chuẩn tại chỗ và bể hiệu chuẩn. Các yêu cầu thẩm "
        "định của chính phủ và tiêu chuẩn ISO 9000 là động lực trong lĩnh vực này. Vì các chương "
        "trình hiệu chuẩn của bên thứ ba tốn kém, các công ty muốn có năng suất cao hơn và hiệu quả "
        "chi phí cao hơn. Wong [7] thảo luận lợi ích của việc thiết lập một phòng hiệu chuẩn tại "
        "chỗ, bên cạnh các khái niệm truy xuất. Truy xuất đề cập đến một chuỗi so sánh không gián "
        "đoạn, liên kết phép đo nhiệt độ với một chuẩn quốc gia, hợp pháp được công nhận. Ở Hoa Kỳ, "
        "chuẩn quốc gia này được duy trì bởi Viện Tiêu chuẩn và Công nghệ Quốc gia (NIST). Tất cả "
        "các nhà sản xuất, phòng thí nghiệm và phòng hiệu chuẩn RTD phải điều chỉnh chuẩn của họ để "
        "đáp ứng chuẩn NIST."))

    b.append(h3("Định nghĩa thuật ngữ", "Defining Terms"))
    b.append(defs([
        ("<b>Accuracy</b> — độ chính xác",
         "Mức độ phù hợp giữa một phép đo thực tế và chuẩn quy chiếu của nó."),
        ("<b>Alpha (<i>α</i>)</b>",
         "Hệ số nhiệt độ của điện trở của một PRT trên dải 0 °C đến 100 °C. Ví dụ, <i>α</i> của một "
         "nhiệt kế điện trở bạch kim chuẩn (SPRT) là 0,003925."),
        ("<b>Calibrate</b> — hiệu chuẩn",
         "Kiểm tra, điều chỉnh hoặc xác định độ chính xác của một RTD bằng cách so sánh với một "
         "chuẩn."),
        ("<b>DIN (Deutsche Industrial Norm)</b>",
         "Một tổ chức của Đức xây dựng các tiêu chuẩn kỹ thuật, khoa học và kích thước được công "
         "nhận trên toàn thế giới."),
        ("<b>Error</b> — sai số",
         "Hiệu giữa giá trị đúng và giá trị đọc thực tế."),
        ("<b>Primary Standard (hay Standard PRT)</b> — chuẩn sơ cấp",
         "Nhiệt kế điện trở bạch kim đáp ứng các yêu cầu để thiết lập hiệu chuẩn theo ITS-90. Dụng "
         "cụ có độ chính xác cao này dành cho môi trường phòng thí nghiệm và chính xác tới 0,001 °C."),
        ("<b>Reliability</b> — độ tin cậy",
         "Được dùng để chỉ độ chính xác xác định trước cho các phép đo thực hiện trong một tập điều "
         "kiện rất hạn chế."),
        ("<b>Repeatability</b> — độ lặp lại",
         "Khả năng cho cùng một kết quả đo trong những điều kiện lặp lại, tương ứng nhau."),
        ("<b>Stability</b> — độ ổn định",
         "Trạng thái chống lại sự thay đổi hoặc xuống cấp."),
        ("<b>Sensitivity</b> — độ nhạy",
         "Mức thay đổi điện trở của cảm biến trên mỗi độ thay đổi nhiệt độ."),
    ]))

    b.append(_refs322("vi"))
    return "".join(b)


def sec_32_2_en():
    b = [h2("32.2 Resistive Thermometers", "Nhiệt kế điện trở")]
    b.append(authors("Jim Burns", ""))

    b.append(h3("Introduction to Resistance Temperature Detectors",
                "Giới thiệu về cảm biến nhiệt điện trở"))
    b.append(p(
        "One common way to measure temperature is by using Resistive Temperature Detectors (RTDs). "
        "These electrical temperature instruments provide highly accurate temperature readings: "
        "simple industrial RTDs used within a manufacturing process are accurate to ±0.1 °C, while "
        "Standard Platinum Resistance Thermometers (SPRTs) are accurate to ±0.0001 °C."))
    b.append(p(
        "The electric resistance of certain metals changes in a known and predictable manner, "
        "depending on the rise or fall in temperature. As temperatures rise, the electric "
        "resistance of the metal increases. As temperatures drop, electric resistance decreases. "
        "RTDs use this characteristic as a basis for measuring temperature."))
    b.append(p(
        "The sensitive portion of an RTD, called an element, is a coil of small-diameter, "
        "high-purity wire, usually constructed of platinum, copper, or nickel. This type of "
        "configuration is called a wire-wound element. With thin-film elements, a thin film of "
        "platinum is deposited onto a ceramic substrate."))
    b.append(p(
        "Platinum is a common choice for RTD sensors because it is known for its long-term "
        "stability over time at high temperatures. Platinum is a better choice than copper or "
        "nickel because it is chemically inert, it withstands oxidation well, and works in a "
        "higher temperature range as well."))
    b.append(p(
        "In operation, the measuring instrument applies a constant current through the RTD. As the "
        "temperature changes, the resistance changes and the corresponding change in voltage is "
        "measured. This measurement is then converted to thermal values by a computer. "
        "Curve-fitting equations are used to define this resistance vs. temperature relationship. "
        "The RTD can then be used to determine any temperature from its measured resistance."))
    b.append(p(
        "A typical measurement technique for industrial thermometers involves sending a constant "
        "current through the sensor (0.8 mA to 1.0 mA), and then measuring the voltage generated "
        "across the sensor using digital voltmeter techniques. The technique is simple and few "
        "error-correcting techniques are applied."))
    b.append(p(
        "In a laboratory where measurement accuracies of 10 ppm or better are required, "
        "specialized measurement equipment is used. High-accuracy bridges and digital voltmeters "
        "with special error-correcting functions are used. Accuracies of high-end measurement "
        "equipment can reach 0.1 ppm (parts per million). These instruments have functions to "
        "compensate for errors such as thermoelectric voltages and element self-heating."))
    b.append(p(
        "In addition to temperature, strain on and impurities in the wire also affect the sensor’s "
        "resistance vs. temperature characteristics. The Matthiessen rule states that the "
        "resistivity (<i>ρ</i>) of a metal conductor depends on temperature, impurities, and "
        "deformation. <i>ρ</i> is measured in (Ω cm):"))
    b.append(eq("<i>ρ</i>(total) = <i>ρ</i>(temperature) + <i>ρ</i>(impurities) + "
                "<i>ρ</i>(deformation)", "32.20"))
    b.append(p(
        "Proper design and careful material selection will minimize these effects so that "
        "resistivity will only vary with a change in temperature."))

    b.append(h3("Resistance of Metals", "Điện trở của kim loại"))
    b.append(p(
        "Whether an RTD’s element is constructed of platinum, copper, or nickel, each type of metal "
        "has a different sensitivity, accuracy, and temperature range. Sensitivity is defined as "
        "the amount of resistance change of the sensor per degree of temperature change. Figure "
        "32.7 shows the sensitivity for the most common metals used to build RTDs."))
    b.append(fig(7, F.fig(7), "en"))
    b.append(p(
        "Platinum, a noble metal, has the most stable resistance-to-temperature relationship over "
        "the largest temperature range — −184.44 °C (−300 °F) to 648.88 °C (1200 °F). Nickel "
        "elements have a limited temperature range because the amount of change in resistance per "
        "degree of change in temperature becomes very nonlinear at temperatures above 300 °C "
        "(572 °F). Copper has a very linear resistance-to-temperature relationship. However, copper "
        "oxidizes at moderate temperatures and cannot be used above 150 °C (302 °F)."))
    b.append(p(
        "Platinum is the best metal for RTD elements for three reasons. It follows a very linear "
        "resistance-to-temperature relationship; it follows its resistance-to-temperature "
        "relationship in a highly repeatable manner over its temperature range; and it has the "
        "widest temperature range among the metals used to make RTDs. Platinum is not the most "
        "sensitive metal; however, it is the metal that offers the best long-term stability."))
    b.append(p(
        "The accuracy of an RTD is significantly better than that of a thermocouple within an "
        "RTD’s normal temperature range of −184.44 °C (−300 °F) to 648.88 °C (1200 °F). RTDs are "
        "also known for high stability and repeatability. They can be removed from service and "
        "recalibrated for verifiable accuracy and checked for any possible drift."))

    b.append(h3("Who Uses RTDs? Common Assemblies and Applications",
                "Ai dùng RTD? Các cụm lắp và ứng dụng thông dụng"))
    b.append(p(
        "Different applications require different types of RTDs. A direct-immersion Platinum "
        "Resistance Thermometer (PRT) and a connection head can be used for low-velocity pipelines, "
        "tanks, or air temperature measurement. A spring-loaded PRT, thermowell, and connection head "
        "are often used in pipelines or storage tanks. An averaging temperature element senses and "
        "measures temperatures along its entire sheath, which can range from 1 to 20 m in length. A "
        "heavy-duty underwater temperature sensor is designed for complete submersion under rivers, "
        "cooling ponds, or sewers. These are just a few examples of RTD configurations and "
        "applications."))

    b.append(h3("Overview of Platinum RTDs", "Tổng quan về RTD bạch kim"))
    b.append(p(
        "There are three main classes of Platinum Resistance Thermometers (PRTs): Standard Platinum "
        "Resistance Thermometers (SPRTs), Secondary Standard Platinum Resistance Thermometers "
        "(Secondary SPRTs), and Industrial Platinum Resistance Thermometers (IPRTs). Table 32.6 "
        "presents information about each."))
    b.append(_t326("en"))

    b.append(h3("Temperature Coefficient of Resistance", "Hệ số nhiệt độ của điện trở"))
    b.append(p(
        "Each of the different metals used for sensing elements (platinum, nickel, copper) has a "
        "different amount of relative change in resistance per unit change in temperature. A "
        "measure of a resistance thermometer’s sensitivity is its temperature coefficient of "
        "resistance. It is defined as the element’s change in resistance per degree C change in "
        "temperature per ohm of sensor resistance over the range of 0 °C to 100 °C."))
    b.append(p(
        "The alpha value is the average change in resistance per degree C per ohm resistance. The "
        "actual change in resistance per degree C per ohm is largest at −200 °C and decreases "
        "steadily as the use temperatures increase."))
    b.append(p(
        "The units for the coefficient are Ω/Ω °C⁻¹. This is called the alpha value and is "
        "commonly denoted by the Greek letter <i>α</i>. The larger the temperature coefficient, the "
        "greater the change in resistance for a given change in temperature. Of the commonly used "
        "RTD metals, nickel has the highest temperature coefficient, 0.00672, while that of copper "
        "is 0.00427. The <i>α</i> value of the sensor is calculated using the equation:"))
    b.append(eq("<i>α</i> = (<i>R</i><sub>100</sub> − <i>R</i><sub>0</sub>) / "
                "(100 °C × <i>R</i><sub>0</sub>)", "32.21"))
    b.append(wl([
        "where <i>R</i><sub>0</sub> = the resistance of the sensor at 0 °C",
        "<i>R</i><sub>100</sub> = the resistance of the sensor at 100 °C",
    ]))
    b.append(p("Three primary temperature coefficients are specified for platinum:"))
    b.append(ol([
        "ITS-90, the internationally accepted temperature scale, requires a minimum temperature "
        "coefficient of 0.003925 for SPRTs. This is achieved using high-purity wire (99.9999% or "
        "better) wound in a strain-free configuration.",
        "With reference-grade platinum wire used in industrial elements, the temperature "
        "coefficient is 0.003902.",
        "IEC 751 [1] and ASTM 1137 [2] have standardized the temperature coefficient of 0.0038500 "
        "for platinum.",
    ]))

    b.append(h3("RTD Construction", "Cấu tạo RTD"))
    b.append(p(
        "Standard Platinum Resistance Thermometers (SPRTs), the highest-accuracy platinum "
        "thermometers, are fragile and used in laboratory environments only (Figure 32.8). Fragile "
        "materials do not provide enough strength and vibration resistance for industrial "
        "environments. SPRTs feature high repeatability and low drift, but they cost more because "
        "of their materials and expensive production techniques."))
    b.append(fig(8, F.fig(8), "en"))
    b.append(p(
        "SPRT elements are wound from large-diameter, high-purity platinum wire. Internal leadwires "
        "are usually made from platinum and internal supports from quartz or fused silica. SPRTs "
        "are used over a very wide range, from −200 °C (−328 °F) to above 1000 °C (1832 °F). For "
        "SPRTs used to measure temperatures up to 660 °C (1220 °F), the ice point resistance is "
        "typically 25.5 Ω. For high-temperature thermometers, the ice point resistance is 2.5 Ω or "
        "0.25 Ω. SPRT probes can be accurate to ±0.001 °C (0.0018 °F) if properly used."))
    b.append(p(
        "Secondary Standard Platinum Resistance Thermometers (Secondary SPRTs) are also intended "
        "for laboratory environments (Figure 32.9). They are constructed like the SPRT, but the "
        "materials are less expensive, typically reference-grade, high-purity platinum wire, metal "
        "sheaths, and ceramic insulators. Internal leadwires are usually a nickel-based alloy. The "
        "secondary grade sensors are limited in temperature range — −200 °C (−328 °F) to 500 °C "
        "(932 °F) — and are accurate to ±0.03 °C (±0.054 °F) over their temperature range."))
    b.append(fig(9, F.fig(9), "en"))
    b.append(p(
        "Secondary standard thermometers can withstand some handling, although they are still quite "
        "strain-free. Rough handling, vibration, and shock will cause a shift in calibration. The "
        "nominal resistance of the ice point is most often 100 Ω. This simplifies calibration "
        "procedures when calibrating other 100-Ω RTDs. The temperature coefficient for secondary "
        "standards using reference-grade platinum wire is usually 0.00392 Ω Ω⁻¹ °C⁻¹ or higher."))
    b.append(p(
        "Industrial Platinum Resistance Thermometers (IPRTs) are designed to withstand industrial "
        "environments and are almost as durable as thermocouples (Figure 32.10). IEC 751 [1] and "
        "ASTM 1137 [2] standards cover the requirements for industrial platinum resistance "
        "thermometers. The most common temperature range is −200 °C (−328 °F) to 500 °C (932 °F). "
        "Standard models are interchangeable to an accuracy of ±0.25 °C (±0.45 °F) to ±2.5 °C "
        "(±4.5 °F) over their temperature range."))
    b.append(fig(10, F.fig(10), "en"))
    b.append(p(
        "Several element designs are available for different applications. One common configuration "
        "is the wirewound element (Figure 32.11). This durable design was developed as a substitute "
        "for the fragile SPRT. The small platinum sensing wire (usually within 7 to 50 μm, i.e. "
        "0.0003 in. to 0.002 in. diameter) is noninductively wound around a cylindrical ceramic "
        "mandrel, and usually covered with a thin layer of material that provides electrical "
        "insulation and mechanical protection. Because the sensing element wire is firmly "
        "supported, it cannot expand and contract as freely as the SPRT’s relatively unsupported "
        "platinum wire. This type of element offers higher durability than SPRTs and secondary "
        "standards, and very good accuracy for most industrial applications."))
    b.append(fig(11, F.fig(11), "en"))
    b.append(p(
        "In another wirewound design, the coil suspension, a coil of fine platinum wire is "
        "assembled into small holes in a cylindrical ceramic mandrel (Figure 32.12). The coils are "
        "supported by ceramic powder or cement, and sealed at both ends. When ceramic powder is "
        "loosely packed in the bores of the mandrel, the element can expand and contract freely. "
        "This reduces the effects of strain on the resistance characteristics, resulting in very "
        "high accuracy and stability for use in secondary temperature standards and docile "
        "industrial applications (with little or no vibration or shock). Recent improvements in "
        "ceramic materials give the sensing coil more stability — it will be capable of maintaining "
        "accuracies of 0.03 °C after thousands of hours at temperatures of 500 °C. These ceramic "
        "powders support the coils in the mandrel bores and hold them firmly in place with minimum "
        "strain."))
    b.append(fig(12, F.fig(12), "en"))
    b.append(p(
        "Thin-film elements are extremely small, often less than 1.6 mm (1/16 in.) square (Figure "
        "32.13). They are manufactured by similar techniques employed to make integrated circuits. "
        "First, a thin film of platinum is deposited onto a ceramic substrate. Some manufacturers "
        "use photolithography to etch the deposited platinum, leaving the element pattern on the "
        "ceramic substrate. Then, the element’s surfaces are covered with glass material to protect "
        "the elements from humidity and contaminants."))
    b.append(fig(13, F.fig(13), "en"))
    b.append(p(
        "The temperature range of thin film platinum elements is −50 °C (−58 °F) to 400 °C (752 °F); "
        "accuracy is from 0.5 °C (0.9 °F) to 2.0 °C (3.6 °F). The most common thin-film element has "
        "a 100-Ω ice point resistance and a temperature coefficient of 0.00385 °C."))
    b.append(p(
        "Thin-film RTDs can be extremely durable if the small-diameter leadwires and the thin "
        "element are properly protected. The accuracy and stability might not be as good as some "
        "wirewound elements due to hysteresis, long-term stability errors, and self-heating "
        "errors."))

    b.append(h3("Self-heating Errors", "Sai số tự đốt nóng"))
    b.append(p(
        "The current that measures sensor resistance also heats the sensor. This is known as "
        "I²R heating or Joule heating. Because of this effect, the sensor’s indicated temperature "
        "is somewhat higher than the actual temperature. This inconsistency is commonly called "
        "self-heating error. Self-heating errors, which are dependent on the application, can range "
        "from negligible values to 1 °C. The greatest heating errors occur because of poor heat "
        "transfer between the sensing element and application, or excessive current used in "
        "measuring resistance."))
    b.append(p("The following are methods for reducing the self-heating error."))
    b.append(ol([
        "Minimize the power dissipation in the sensor. There is a tradeoff between the signal level "
        "and the self-heating of the sensor. Typically, 1 mA of current is used as the sensing "
        "current.",
        "Use a sensor with a low thermal resistance. The lower the thermal resistance of the "
        "sensor, the better the sensor can dissipate the I²R power and the lower the temperature "
        "rise in the sensor. Small time constants indicate a sensor with a low thermal resistance.",
        "Maximize thermal contact between the sensor and the application.",
    ]))

    b.append(h3("Calibration", "Hiệu chuẩn"))
    b.append(p(
        "Testing programs are essential to verify the accuracy of PRTs. Some IPRTs are "
        "factory-calibrated to a temperature such as the ice point, but PRT users might want to "
        "calibrate them at other temperatures, depending on their application."))
    b.append(p(
        "The calibration results can be compared to prior calibrations from the same instrument. "
        "This will determine if it is necessary to repair or replace the instrument, or if "
        "calibration is required more often."))
    b.append(p(
        "Since frequent repairs and recalibration are usually costly, purchasers and specifiers of "
        "PRTs might want to investigate various RTDs before installation by referring to ASTM "
        "Standard #E1137-95 [2], published by The American Society for Testing and Materials "
        "(ASTM)."))
    b.append(p(
        "<i>Frequency.</i> An RTD’s stability depends on its working environment. High temperatures "
        "can cause drift and contamination of the platinum wire. The higher the temperature, the "
        "faster the drift occurs. Below 400 °C, the high-temperature drift is not a significant "
        "problem, but temperatures reaching 500 °C to 600 °C are the most significant causes of "
        "drift — up to several degrees per year. Severe shock can damage a sensor instantly and "
        "cause failure. Shock, vibration, and rough handling will put strains in the platinum wire "
        "and change its characteristics, and potentially damage the entire unit. If a sensor is not "
        "properly sealed, humidity can get into the sensor and cause some problems with the "
        "insulation resistance. Since the water in humidity is conductive, it will get between the "
        "lead wires and the sensing element, and basically shunt off the resistance of the element’s "
        "wires. Under extreme operating conditions, a sensor should be calibrated on a monthly or "
        "bimonthly basis. If five or more calibrations are completed without a significant change, "
        "then the time between calibrations can be doubled; at least once a year is recommended, "
        "however."))
    b.append(p(
        "<i>Techniques.</i> Two common calibration methods are the fixed point method and the "
        "comparison method."))
    b.append(p(
        "<i>Fixed point calibration</i>, used for the highest accuracy calibrations, uses the "
        "triple point, freezing point or melting point of pure substances such as water, zinc, tin, "
        "and argon to generate a known and repeatable temperature (Figure 32.14). The fixed point "
        "cells are sealed to prevent contamination and to prevent atmospheric conditions from "
        "affecting the cell’s temperature. These cells allow the user to reproduce actual conditions "
        "of the ITS-90 temperature scale."))
    b.append(fig(14, F.fig(14), "en"))
    b.append(p(
        "Fixed point calibrations provide extremely accurate calibrations (within ±0.001 °C), but "
        "the cells are time-consuming to use and can only accommodate one sensor at a time. For this "
        "reason, they are not widely used in calibrating industrial sensors. Each fixed point cell "
        "has a unique procedure for achieving the fixed point."))
    b.append(p("A generalized procedure for fixed point calibration is as follows:"))
    b.append(ol([
        "Prepare the cell. Different procedures exist for each fixed point.",
        "Insert the thermometer to be calibrated.",
        "Allow the system to stabilize. Stabilization times depend on thermometer/fixed point "
        "cells. Usually, 15 to 30 min is sufficient.",
        "Measure the resistance of the thermometer. For the highest accuracy measurements, special "
        "resistance bridges are used. They have accuracies in the range of 10 ppm to 0.1 ppm.",
    ]))
    b.append(p(
        "A common fixed point calibration method for industrial-grade probes is the ice bath. The "
        "equipment is inexpensive, easy to use, and can accommodate several sensors at once. The ice "
        "point is designated as a secondary standard because its accuracy is ±0.005 °C "
        "(±0.009 °F), compared to ±0.001 °C (±0.0018 °F) for primary fixed points."))
    b.append(p(
        "In <i>comparison calibrations</i>, commonly used with secondary SPRTs and industrial RTDs, "
        "the thermometers being calibrated are compared to calibrated thermometers by means of an "
        "isothermal bath whose temperature is uniformly stable (Figure 32.15). Unlike fixed point "
        "calibrations, comparisons can be made at any temperature between −100 °C (−148 °F) and "
        "500 °C (932 °F). This method might be more cost-effective since several sensors can be "
        "calibrated simultaneously with automated equipment."))
    b.append(fig(15, F.fig(15), "en"))
    b.append(p(
        "These isothermal baths, electrically heated and well-stirred, use silicone oils as the "
        "medium for temperatures ranging from −100 °C (−148 °F) to 200 °C (392 °F), and molten "
        "salts for temperatures above 200 °C (392 °F). At temperatures above 500 °C (932 °F), air "
        "furnaces or fluidized beds are used, but are significantly less uniformly stable."))
    b.append(p("The procedure for comparison calibration is as follows:"))
    b.append(ol([
        "Insert the standard thermometer and thermometers being calibrated into the bath.",
        "Allow the bath to stabilize.",
        "Measure the resistance of the standard to determine the temperature of the bath.",
        "Measure the resistance of each thermometer under calibration.",
    ]))
    b.append(p(
        "<i>Deriving the resistance vs. temperature relationship of a PRT.</i> After determining "
        "the PRT’s resistance, the calibration coefficients can be determined. By plugging these "
        "values into an equation, temperature from any measured resistance can be derived. The two "
        "most common curve-fitting techniques are the ITS-90 and Callendar–Van Dusen equations."))
    b.append(p(
        "On January 1, 1990, the International Temperature Scale of 1990 (ITS-90) became the "
        "official international temperature scale [3]. ITS-90 extends upward from 0.65 K "
        "(−272.5 °C or −458.5 °F) and defines temperatures of 0.65 K (0.65 °C above absolute zero) "
        "and up by fixed points (see Table 32.7)."))
    b.append(_t327("en"))
    b.append(p(
        "Two reference functions are used to define the temperature coefficient for an ideal SPRT: "
        "one for temperatures below 0 °C and the other for temperatures above 0 °C. When a PRT is "
        "calibrated on the ITS-90, the coefficients determined in the calibration are used to "
        "describe a deviation function that represents the difference between the resistance of the "
        "standard PRT and the reference function at all temperatures within the range. Using the "
        "calibration coefficients and the deviation functions, the SPRT can be used to determine any "
        "temperature from its measured resistance. Because ITS-90 equations are complex, computer "
        "software is necessary for accurate calculations."))
    b.append(p("ITS-90 affects:"))
    b.append(ul([
        "Standards and temperature calibration laboratories",
        "Users of standard and secondary SPRTs with traceability to standards laboratories",
        "Users of temperature measurement and control systems within companies concerned with "
        "verifiable total quality management",
    ]))
    b.append(p(
        "The National Institute for Standards and Technology (NIST) has published Technical Note "
        "1265, <i>Guidelines for Realizing the International Temperature Scale of 1990 (ITS-90)</i> "
        "[4]. Not all PRT users need to follow the complex equations and computer programs "
        "associated with ITS-90. As a rule of thumb: if the minimum required uncertainty of "
        "measurement is less than 0.1 °C, one probably will want to use ITS-90. For uncertainty of "
        "measurements greater than 0.1 °C, the effect of the change in scales is relatively small "
        "and one will not be affected."))
    b.append(p(
        "Callendar–Van Dusen equations are interpolation equations that describe the temperature vs. "
        "resistance relationship of industrial PRTs. These simple-to-use second- and fourth-order "
        "equations can be programmed easily into many electronic controllers. The equation for the "
        "temperature range of 0 °C (32 °F) to 850 °C (1562 °F) is:"))
    b.append(eq("<i>R</i>(<i>t</i>) = <i>R</i><sub>0</sub>(1 + <i>At</i> + <i>Bt</i>²)", "32.22"))
    b.append(p("For the temperature range −200 °C (−392 °F) to 0 °C (32 °F):"))
    b.append(eq("<i>R</i>(<i>t</i>) = <i>R</i><sub>0</sub>[1 + <i>At</i> + <i>Bt</i>² + "
                "<i>C</i>(<i>t</i> − 100)<i>t</i>³]", "32.23"))
    b.append(wl([
        "where <i>R</i>(<i>t</i>) = resistance of the PRT at temperature <i>t</i>",
        "<i>t</i> = temperature in °C",
        "<i>R</i><sub>0</sub> = nominal resistance of the PRT at 0 °C",
        "<i>α</i>, <i>δ</i>, <i>β</i> = calibration coefficients",
    ]))
    b.append(p(
        "To determine the temperature from a measured resistance, a different set of equations and "
        "calibration coefficients is required. For temperatures greater than 0 °C (measured "
        "resistances greater than the known ice point resistance of the PRT):"))
    b.append(eq("<i>t</i>(°C) = [(<i>R</i><sub><i>t</i></sub> − <i>R</i><sub>0</sub>) / "
                "(<i>αR</i><sub>0</sub>)] + <i>δ</i>[(<i>t</i>/100) − 1](<i>t</i>/100)", "32.24"))
    b.append(p(
        "For temperatures less than 0 °C (measured resistances less than the known ice point "
        "resistance of the PRT):"))
    b.append(eq("<i>t</i>(°C) = [(<i>R</i><sub><i>t</i></sub> − <i>R</i><sub>0</sub>) / "
                "(<i>αR</i><sub>0</sub>)] + <i>δ</i>[(<i>t</i>/100) − 1](<i>t</i>/100) + "
                "<i>β</i>[(<i>t</i>/100) − 1](<i>t</i>/100)³", "32.25"))
    b.append(wl([
        "where <i>t</i> = temperature to be calculated",
        "<i>R</i>(<i>t</i>) = measured resistance at unknown temperature",
        "<i>R</i><sub>0</sub> = resistance of the sensor at 0 °C",
        "<i>α</i>, <i>δ</i>, <i>β</i> = coefficients",
    ]))
    b.append(p(
        "To correctly determine the temperature from a given resistance with these equations, one "
        "must iterate the equations a minimum of five times. After each calculation, the new value "
        "of temperature (<i>t</i>) is plugged back into the equations. The calculated temperature "
        "value will converge on its true value. After five iterations, the calculated temperature "
        "should be within ±0.001 °C of the true value."))
    b.append(p(
        "For industrial sensors, an alternative method would be to use nonlinear least squares "
        "curve fits to produce the temperature/resistance relationship. However, these methods "
        "should not be used for secondary and primary level thermometers as they cannot sufficiently "
        "match the defined ITS-90 scale. Curve fitting errors of up to 0.05 °C are possible."))

    b.append(h3("Usage of RTDs Today", "Sử dụng RTD ngày nay"))
    b.append(p(
        "Throughout the industry, usage of RTDs is increasing for many reasons. With the advent of "
        "the computer age, industries recognize the need for better temperature measurement, and an "
        "electrical signal to accompany advances in computerized process instrumentation. RTDs "
        "produce an electrical signal; and because of automatic control in industrial plants, it "
        "makes it simpler and easier to interface with process controllers. With the focus on "
        "reengineering, companies are searching for ways to improve processes. Improved temperature "
        "measurement and control is one good way to save energy, reduce material waste, reduce "
        "expenses and improve overall operating efficiencies."))
    b.append(p(
        "Governmental regulations are another reason why RTDs are gaining popularity. In the "
        "pharmaceutical industry, the FDA [5] requires validation; among them the verification that "
        "temperature measurement is accurate. New regulations are currently being written for the "
        "food industry as well [6]."))
    b.append(p(
        "The growing worldwide acceptance of ISO 9000 standards has forced companies to calibrate "
        "their temperature measurement systems and instrumentation. In addition, the calibration "
        "must be documented, and must be traceable to a recognized national, legal standard."))
    b.append(p(
        "RTDs are safer for the environment. With mercury thermometers, disposal of mercury is a "
        "problem. In many industries, the mere presence of mercury thermometers presents a risk."))

    b.append(h3("Examples of Advanced Applications for Critical Temperature Measurement",
                "Ví dụ về ứng dụng tiên tiến cho đo nhiệt độ tới hạn"))
    b.append(p(
        "RTD technology allows for custom design in a wide range of applications and industries. In "
        "many of these cases, the RTD becomes an integral part of an advanced application when "
        "temperature is critical."))
    b.append(p(
        "Power plants use RTD sensors to monitor fuel and coolant temperatures entering and exiting "
        "heat exchangers. Accurate temperature measurement is also critical for nuclear power plants "
        "to perform pressure leak tests on the containment vessel surrounding the reactor core."))
    b.append(p(
        "Microprocessor manufacturers require precise temperature control throughout their clean "
        "room areas. Air temperature is critical to production; many temperature measurement points "
        "need to be accurate ±0.028 °C (±0.05 °F). To achieve this, an RTD is calibrated with a "
        "temperature transmitter. This matched pair ensures the highest level of system accuracy and "
        "eliminates the interchangeability error of the RTD."))

    b.append(h3("The Future of RTD Technology", "Tương lai của công nghệ RTD"))
    b.append(p(
        "The future of RTD technology is driven by end-user needs and unsolved problems. For "
        "example, the need for high-temperature industrial RTDs exists for applications above "
        "600 °C (1200 °F). In order to function at high temperatures, the RTD’s platinum element "
        "must be protected from contamination. However, the sheath material can be a problem "
        "because, at high temperatures, it will react with the oxygen in the air and give off metal "
        "particles that can attach themselves to the platinum."))
    b.append(p(
        "RTDs must be mechanically strong enough to survive higher temperatures as well. A "
        "high-temperature industrial RTD would require a thermally resistant sheath, perhaps Inconel "
        "600. In addition, sensor components must be designed and manufactured to resist "
        "ultra-high temperatures. Some RTDs are specified to operate above 600 °C (1200 °F), but "
        "when tested, are not always reliable. Drift and nonrepeatability are problem areas that "
        "are in need of further attention."))
    b.append(p(
        "Advances in RTD calibration provide significant improvements for temperature measurement "
        "and control. New measurement technologies combined with powerful computational techniques, "
        "have simplified the calibration process and made it more reliable."))
    b.append(p(
        "Another current area of growth is in-house calibration and calibration baths. Governmental "
        "validation requirements and ISO-9000 standards are the driving forces in this area. Because "
        "third-party calibration services are expensive, companies want to be more productive and "
        "more cost-efficient. Wong [7] discusses the benefits of setting up an in-house calibration "
        "lab in addition to traceability concepts. Traceability refers to an unbroken chain of "
        "comparisons, linking the temperature measurement to a recognized national, legal standard. "
        "In the U.S., this national standard is maintained by the National Institute of Standards "
        "and Technology (NIST). All RTD manufacturers, laboratories, and calibration labs must "
        "adjust their standards to meet NIST standards."))

    b.append(h3("Defining Terms", "Định nghĩa thuật ngữ"))
    b.append(defs([
        ("<b>Accuracy</b>",
         "The degree of agreement between an actual measurement and its reference standard."),
        ("<b>Alpha (<i>α</i>)</b>",
         "The temperature coefficient of resistance of a PRT over the range 0 °C to 100 °C. For "
         "example, <i>α</i> for a standard platinum resistance thermometer (SPRT) is 0.003925."),
        ("<b>Calibrate</b>",
         "To check, adjust or determine an RTD’s accuracy by comparing it to a standard."),
        ("<b>DIN (Deutsche Industrial Norm)</b>",
         "A German organization that develops technical, scientific, and dimensional standards that "
         "are recognized worldwide."),
        ("<b>Error</b>",
         "The difference between a correct value and the actual reading taken."),
        ("<b>Primary Standard (or Standard PRT)</b>",
         "A platinum resistance thermometer that meets the requirements for establishing "
         "calibrations according to the ITS-90. This highly accurate instrument is intended for "
         "laboratory environments and is accurate to 0.001 °C."),
        ("<b>Reliability</b>",
         "Used to designate precision for measurements made within a very restricted set of "
         "conditions."),
        ("<b>Repeatability</b>",
         "The ability to give the same measurement under repeated, matching conditions."),
        ("<b>Stability</b>",
         "The state of being resistant to change or deterioration."),
        ("<b>Sensitivity</b>",
         "The amount of resistance change of the sensor per degree temperature change."),
    ]))

    b.append(_refs322("en"))
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


def _refs322(lang):
    """§32.2 has its own reference list — each section of this chapter does."""
    vi = lang == "vi"
    items = [
        "1. IEC, <i>Industrial platinum resistance thermometer sensors</i>, IEC International "
        "Standard 751.1995-07, Genève, Suisse: Bureau Central de la Commission Electrotechnique "
        "Internationale, 1995.",
        "2. ASTM Standards, <i>Standard Specification for Industrial Platinum Resistance "
        "Thermometers</i>, Standard E 1137-95, 1995.",
        "3. H. Preston-Thomas, The International Temperature Scale of 1990 (ITS-90), "
        "<i>Metrologia</i>, 27(1), 3–10, 1990. For errata, see <i>ibid</i>, 27(2), 107, 1990.",
        "4. NIST Technical Note 1265, <i>Guidelines for Realizing the International Temperature "
        "Scale of 1990 (ITS-90)</i>, National Institute of Standards and Technology, 1990.",
        "5. FDA validation for the pharmaceutical industry.",
        "6. FDA validation for the food industry.",
        "7. W. Wong, Traceability tops in-house calibration, <i>InTech</i>, 41(8), 27–29, 1994.",
    ]
    head_ = "<h3 id=\"t32-tltk-2\">Tài liệu tham khảo</h3>" if vi else \
            "<h3 id=\"t32-tltk-2\">References</h3>"
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
    ("32.2", "Resistive Thermometers", "Nhiệt kế điện trở", [
        ("Introduction to Resistance Temperature Detectors",
         "Giới thiệu về cảm biến nhiệt điện trở"),
        ("Resistance of Metals", "Điện trở của kim loại"),
        ("Who Uses RTDs? Common Assemblies and Applications",
         "Ai dùng RTD? Các cụm lắp và ứng dụng thông dụng"),
        ("Overview of Platinum RTDs", "Tổng quan về RTD bạch kim"),
        ("Temperature Coefficient of Resistance", "Hệ số nhiệt độ của điện trở"),
        ("RTD Construction", "Cấu tạo RTD"),
        ("Self-heating Errors", "Sai số tự đốt nóng"),
        ("Calibration", "Hiệu chuẩn"),
        ("Usage of RTDs Today", "Sử dụng RTD ngày nay"),
        ("Examples of Advanced Applications for Critical Temperature Measurement",
         "Ví dụ về ứng dụng tiên tiến cho đo nhiệt độ tới hạn"),
        ("The Future of RTD Technology", "Tương lai của công nghệ RTD"),
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
                       '<a class="t" href="#s32-%s-%s">%s</a></li>'
                       % (num.split(".")[1], _slug(sub_en), sub_vi if vi else sub_en))
    out.append("</ol>")
    return "".join(out)


def body_vi():
    lede = (
        "Nhiệt độ là đại lượng được đo nhiều nhất trong công nghiệp, và cũng là đại lượng có nhiều "
        "họ nguyên lý chuyển đổi nhất. Chương này đi qua mười một họ dụng cụ — từ dải lưỡng kim, "
        "nhiệt điện trở, cặp nhiệt điện đến hồng ngoại và sợi quang — với phương trình, hình vẽ và "
        "bảng dữ liệu của từng loại.")
    return (p(lede) + sec_index(True) + sec_32_1_vi() + back_vi() + sec_32_2_vi())


def body_en():
    lede = (
        "Temperature is the most widely measured quantity in industry, and the one with the largest "
        "number of transducer families. This chapter works through eleven of them — bimetallic "
        "strips, resistance thermometers, thermistors, thermocouples, semiconductor junctions, "
        "infrared, pyroelectric, liquid-in-glass, manometric, indicators and fiber-optic probes — "
        "with the equations, figures and data tables for each.")
    return (p(lede) + sec_index(False) + sec_32_1_en() + back_en() + sec_32_2_en())


def build(lang):
    vi = lang == "vi"
    _LANG[0] = lang
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
    meta = ("Chương 32 · theo Ch32.pdf (CRC Press, 1999) · §32.1–32.2/11 · 15 hình, 25 phương "
            "trình, 7 bảng" if vi else
            "Chapter 32 · §32.1–32.2 of 11 · 15 figures, 25 equations, 7 tables")
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
