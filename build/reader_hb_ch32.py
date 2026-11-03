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


def _frac(num, den, size="0.84em"):
    """A stacked fraction from two inline-blocks. library.css has no .frac rule
    and adding one would touch every reader page, so the styling stays inline.
    §32.3 needs a dozen of these — the whole polynomial discussion is fractions."""
    return ('<span style="display:inline-block;vertical-align:middle;text-align:center;'
            'max-width:100%%;font-size:%s;line-height:1.22;margin:0 0.18em">'
            '<span style="display:block;border-bottom:1.2px solid currentColor;'
            'padding:0 0.35em 2px">%s</span>'
            '<span style="display:block;padding:2px 0.35em 0">%s</span></span>'
            % (size, num, den))


def _sq(inner):
    """A square root: radical sign plus an overlined radicand. The radicand is a
    flex item rather than an inline span, because a stacked fraction is itself an
    inline-block and overflows above an inline box's border — that is how the bar
    came to run straight through the numerator of 32.69 instead of over it. The
    flex line also centres the radical sign against the tall fraction."""
    return ('<span style="display:inline-flex;align-items:center;vertical-align:middle">'
            '<span style="font-size:1.32em;line-height:1">√</span>'
            '<span style="border-top:1.2px solid currentColor;padding:.14em .12em 0">%s</span>'
            '</span>' % inner)


def _big(t, k=1.9):
    """Large round delimiters around a stacked fraction. The book's typesetter used
    stretchy brackets here; the plain character leaves a fraction sticking out of
    both ends of a one-em parenthesis, so the glyph is scaled on the vertical axis
    and the two are centred on the fraction with a flex line."""
    p = ("display:inline-block;transform:scaleY(%s);line-height:1;margin:0 -.05em" % k)
    return ('<span style="display:inline-flex;align-items:center;vertical-align:middle">'
            '<span style="%s">(</span>%s<span style="%s">)</span></span>' % (p, t, p))


def h4(t, en=""):
    """A sub-sub-heading. The source nests the three electrical characteristics
    under "Electrical Properties", and the three circuit techniques under
    "Linearization"; flattening both to h3 would lose that."""
    if en == t:
        en = ""
    a = ""
    if _CUR[0]:
        base = (en or t) if _LANG[0] == "vi" else t
        a = ' id="s32-%s-%s"' % (_CUR[0], _slug(base))
    return ('<h4%s style="font-size:1rem;font-weight:700;margin:1.7rem 0 .5rem">%s%s</h4>'
            % (a, t, (' <span class="en">%s</span>' % en) if en else ""))


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


def _tbl2(h1, h2, rows, cap):
    """A table with a two-row header. Tables 32.8 and 32.9 both group two
    dissipation columns and two time-constant columns under single headings, and
    the single-row helper cannot express that — the second row would land in the
    wrong columns."""
    top = "".join(('<th rowspan="2">%s</th>' % t) if s == 0
                  else ('<th colspan="%d">%s</th>' % (s, t)) for t, s in h1)
    sub = "".join("<th>%s</th>" % t for t in h2)
    body = "".join("<tr>%s</tr>" % "".join("<td>%s</td>" % c for c in r) for r in rows)
    return ('<div class="table-wrap"><table class="tbl" style="font-size:.84rem">'
            '<thead><tr>%s</tr><tr>%s</tr></thead><tbody>%s</tbody></table></div>'
            '<p style="font-size:.84rem;color:#888;font-style:italic">%s</p>'
            % (top, sub, body, cap))


def _t328(lang):
    vi = lang == "vi"
    h1 = [("Kiểu", 0), ("Đường kính (mm)", 0),
          ("Hằng số tiêu tán (mW °C⁻¹)", 2), ("Hằng số thời gian (s)", 2)] if vi else \
         [("Style", 0), ("Diameter (mm)", 0),
          ("Dissipation constant (mW °C⁻¹)", 2), ("Time constant (s)", 2)]
    h2 = ("Trong không khí", "Trong nước", "Trong không khí", "Khi nhúng nước") if vi else \
         ("Still air", "Still water", "Still air", "Water plunge")
    rows = [
        ("Hạt phủ thủy tinh", "0,13", "0,045", "0,45", "0,12", "0,005"),
        ("Hạt phủ thủy tinh", "0,25", "0,09", "0,9", "0,5", "0,010"),
        ("Hạt phủ thủy tinh", "0,36", "0,10", "0,98", "1,0", "0,015"),
        ("Hạt gia cố", "0,41", "0,12", "1,1", "1,2", "0,016"),
        ("Đầu dò thủy tinh", "0,63", "0,19", "1,75", "1,9", "0,020"),
        ("Hạt phủ thủy tinh", "0,89", "0,35", "3,8", "4,5", "0,10"),
        ("Hạt phủ thủy tinh", "1,1", "0,40", "4,0", "5,5", "0,14"),
        ("Hạt gia cố", "1,4", "0,51", "4,3", "7,0", "0,20"),
        ("Đầu dò thủy tinh", "1,5", "0,72", "4,4", "12,0", "0,30"),
        ("Đầu dò thủy tinh", "2,16", "0,90", "4,5", "16,0", "0,40"),
        ("Đầu dò thủy tinh", "2,5", "1,0", "4,5", "22,0", "0,65"),
    ] if vi else [
        ("Glass-coated bead", "0.13", "0.045", "0.45", "0.12", "0.005"),
        ("Glass-coated bead", "0.25", "0.09", "0.9", "0.5", "0.010"),
        ("Glass-coated bead", "0.36", "0.10", "0.98", "1.0", "0.015"),
        ("Ruggedized bead", "0.41", "0.12", "1.1", "1.2", "0.016"),
        ("Glass probe", "0.63", "0.19", "1.75", "1.9", "0.020"),
        ("Glass-coated bead", "0.89", "0.35", "3.8", "4.5", "0.10"),
        ("Glass-coated bead", "1.1", "0.40", "4.0", "5.5", "0.14"),
        ("Ruggedized bead", "1.4", "0.51", "4.3", "7.0", "0.20"),
        ("Glass probe", "1.5", "0.72", "4.4", "12.0", "0.30"),
        ("Glass probe", "2.16", "0.90", "4.5", "16.0", "0.40"),
        ("Glass probe", "2.5", "1.0", "4.5", "22.0", "0.65"),
    ]
    cap = ("Bảng 32.8 · Tính chất nhiệt của hạt và đầu dò hàn kín. Theo Tài liệu tham khảo [1]."
           if vi else
           "Table 32.8 · Thermal properties of hermetically sealed beads and probes. From "
           "Reference [1].")
    return _tbl2(h1, h2, rows, cap)


def _t329(lang):
    vi = lang == "vi"
    hd = ("Kiểu", "Đường kính (mm)", "Hằng số tiêu tán (mW °C⁻¹)",
          "Hằng số thời gian (s)") if vi else \
         ("Style", "Diameter (mm)", "Dissipation constant (mW °C⁻¹)", "Time constant (s)")
    rows = [
        ("Chip hoặc đĩa trong vỏ điốt thủy tinh", "2", "2–3", "7–8"),
        ("Chip hoặc đĩa phủ epoxy loại lắp lẫn được", "2,4", "1", "10"),
        ("Đĩa có dây dẫn hướng kính hoặc hướng trục", "2,5", "3–4", "8–15"),
        ("Đĩa có dây dẫn hướng kính hoặc hướng trục", "5,1", "4–8", "13–50"),
        ("Đĩa có dây dẫn hướng kính hoặc hướng trục", "7,6", "7–9", "35–85"),
        ("Đĩa có dây dẫn hướng kính hoặc hướng trục", "10,2", "8–11", "28–150"),
        ("Đĩa có dây dẫn hướng kính hoặc hướng trục", "12,7", "5–16", "50–175"),
        ("Đĩa có dây dẫn hướng kính hoặc hướng trục", "19,6", "15–20", "90–300"),
        ("Đĩa có dây dẫn hướng kính hoặc hướng trục", "25,4", "24–40", "110–230"),
        ("Đĩa có dây dẫn hướng kính hoặc hướng trục", "1,3", "2,5–3", "16–20"),
        ("Thanh có dây dẫn hướng kính hoặc hướng trục", "1,8", "4–10", "35–90"),
        ("Thanh có dây dẫn hướng kính hoặc hướng trục", "4,4", "8–24", "80–125"),
    ] if vi else [
        ("Chip or disk in glass diode package", "2", "2–3", "7–8"),
        ("Interchangeable epoxy coated chip or disk", "2.4", "1", "10"),
        ("Disk with radial or axial leads", "2.5", "3–4", "8–15"),
        ("Disk with radial or axial leads", "5.1", "4–8", "13–50"),
        ("Disk with radial or axial leads", "7.6", "7–9", "35–85"),
        ("Disk with radial or axial leads", "10.2", "8–11", "28–150"),
        ("Disk with radial or axial leads", "12.7", "5–16", "50–175"),
        ("Disk with radial or axial leads", "19.6", "15–20", "90–300"),
        ("Disk with radial or axial leads", "25.4", "24–40", "110–230"),
        ("Disk with radial or axial leads", "1.3", "2.5–3", "16–20"),
        ("Rod with radial or axial leads", "1.8", "4–10", "35–90"),
        ("Rod with radial or axial leads", "4.4", "8–24", "80–125"),
    ]
    cap = ("Bảng 32.9 · Tính chất nhiệt của nhiệt điện trở có điện cực bề mặt kim loại hóa. Theo "
           "các Tài liệu tham khảo [1, 6, 9, 10]." if vi else
           "Table 32.9 · Thermal properties of thermistors with metallized surface electrodes. "
           "From References [1, 6, 9, 10].")
    return table(hd, rows, cap, widths=["40%", "16%", "24%", "20%"], small=True)


def _t3210(lang):
    """Table 32.10 is four numbered groups of bulleted applications. As a table
    it has one column and eleven rows, which reads worse than one cell per group
    with the bullets broken by <br>."""
    vi = lang == "vi"
    groups = [
        ("1. Thay đổi hằng số tiêu tán (đường tải cố định trên một họ đường cong)",
         ["Áp kế chân không", "Máy đo gió, lưu lượng kế, vận tốc chất lưu",
          "Phân tích độ dẫn nhiệt, máy dò khí, sắc ký khí",
          "Đo, điều khiển và báo động mức chất lỏng"]),
        ("2. Thay đổi tham số mạch (đường tải quay và/hoặc dịch trên một đường cong E–I cố định)",
         ["Điều chỉnh biên độ và/hoặc tần số dao động",
          "Ổn định và cân bằng độ lợi hoặc mức tín hiệu", "Hạn chế âm lượng",
          "Nén và giãn điện áp", "Linh kiện chuyển mạch"]),
        ("3. Thay đổi nhiệt độ môi trường (đường tải cố định hoặc thay đổi trên một họ đường cong)",
         ["Điều khiển hoặc báo động nhiệt độ"]),
        ("4. Đo công suất vi ba", ["Bolometer"]),
    ] if vi else [
        ("1. Variation in dissipation constant (fixed load line on a family of curves)",
         ["Vacuum manometers", "Anemometers, flowmeters, fluid velocity",
          "Thermal conductivity analysis, gas detectors, gas chromatography",
          "Liquid level measurement, control, and alarm"]),
        ("2. Variation in circuit parameters (rotation and/or translation of load line on a "
         "fixed E–I curve)",
         ["Oscillator amplitude and/or frequency regulation",
          "Gain or level stabilization and equalization", "Volume limiters",
          "Voltage compression and expansion", "Switching devices"]),
        ("3. Variation in ambient temperature (fixed or variable load line on a family of curves)",
         ["Temperature control or alarm"]),
        ("4. Microwave power measurement", ["Bolometers"]),
    ]
    rows = []
    for head_, items in groups:
        rows.append("<b>%s</b><br>%s" % (head_, "<br>".join("• " + i for i in items)))
    body = "".join("<tr><td>%s</td></tr>" % r for r in rows)
    hd = "Ứng dụng dựa trên đặc tính dòng – áp của nhiệt điện trở" if vi else \
         "Applications Based on the Voltage–Current Characteristic of Thermistors"
    cap = ("Bảng 32.10 · Ứng dụng dựa trên đặc tính dòng – áp của nhiệt điện trở. Theo các Tài "
           "liệu tham khảo [1, 14]." if vi else
           "Table 32.10 · Applications based on the voltage–current characteristic of thermistors. "
           "From References [1, 14].")
    return ('<div class="table-wrap"><table class="tbl" style="font-size:.86rem">'
            '<thead><tr><th>%s</th></tr></thead><tbody>%s</tbody></table></div>'
            '<p style="font-size:.84rem;color:#888;font-style:italic">%s</p>'
            % (hd, body, cap))


def _t3211(lang):
    vi = lang == "vi"
    hd = ("Dải nhiệt độ (°C)", "Dải nhiệt độ khảo sát (°C)", "Sai số nội suy (°C)") if vi else \
         ("Temperature range (°C)", "Temperature span (°C)", "Interpolation error (°C)")
    rows = [
        ("−80 đến 0", "50", "0,002–0,01"),
        ("0 đến 200", "50", "0,001–0,003"),
        ("−80 đến 0", "100", "0,02–0,03"),
        ("0 đến 200", "100", "0,01"),
        ("−60 đến 90", "150", "0,1"),
        ("0 đến 150", "150", "0,045"),
        ("50 đến 200", "150", "0,015"),
        ("0 đến 200", "200", "0,08"),
    ] if vi else [
        ("–80 to 0", "50", "0.002–0.01"),
        ("0 to 200", "50", "0.001–0.003"),
        ("–80 to 0", "100", "0.02–0.03"),
        ("0 to 200", "100", "0.01"),
        ("–60 to 90", "150", "0.1"),
        ("0 to 150", "150", "0.045"),
        ("50 to 200", "150", "0.015"),
        ("0 to 200", "200", "0.08"),
    ]
    cap = ("Bảng 32.11 · Sai số nội suy của ln <i>R</i><sub>T</sub> = <i>C</i><sub>0</sub> + "
           "<i>C</i><sub>1</sub>/<i>T</i> + <i>C</i><sub>3</sub>/<i>T</i><sup>3</sup>." if vi else
           "Table 32.11 · Interpolation errors for ln <i>R</i><sub>T</sub> = <i>C</i><sub>0</sub> + "
           "<i>C</i><sub>1</sub>/<i>T</i> + <i>C</i><sub>3</sub>/<i>T</i><sup>3</sup>.")
    return table(hd, rows, cap, widths=["34%", "33%", "33%"], small=True)


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
# ================================================================ §32.3
def sec_32_3_vi():
    b = [h2("32.3 Nhiệt kế nhiệt điện trở", "Thermistor Thermometers")]
    b.append(authors("Meyer Sapoff", ""))

    b.append(p(
        "Nhiệt điện trở là một điện trở nhạy nhiệt, có chức năng chính là thể hiện sự thay đổi "
        "điện trở khi nhiệt độ của thân nó thay đổi. Khác với cảm biến nhiệt điện trở (RTD) kiểu "
        "quấn dây hay kiểu màng kim loại, nhiệt điện trở là một chất bán dẫn gốm. RTD có hệ số "
        "nhiệt độ của điện trở tương đối nhỏ, cỡ 0,4 đến 0,5% °C⁻¹. Tùy theo hệ vật liệu dùng, "
        "nhiệt điện trở có thể có hệ số nhiệt độ của điện trở dương lớn (linh kiện PTC) hoặc âm "
        "lớn (linh kiện NTC)."))
    b.append(p(
        "Có hai loại nhiệt điện trở PTC. Nhiệt điện trở PTC silic dựa trên tính chất khối của "
        "silic pha tạp và có đặc tính điện trở – nhiệt độ gần như tuyến tính. Chúng có hệ số nhiệt "
        "độ của điện trở khoảng 0,7 đến 0,8% °C⁻¹. Ứng dụng phổ biến nhất của nhiệt điện trở PTC "
        "silic là bù cho các linh kiện và mạch bán dẫn silic [1]. Vật liệu dùng cho nhiệt điện trở "
        "PTC kiểu chuyển mạch là các hợp chất titanat bari, chì và stronti. Hình 32.16 cho thấy "
        "đặc tính điện trở – nhiệt độ của một nhiệt điện trở PTC kiểu chuyển mạch thông dụng [2]. "
        "Ở nhiệt độ thấp, từ dưới 0 °C đến <i>R</i><sub>min</sub>, giá trị điện trở nhỏ và "
        "<i>R</i><sub>T</sub> theo <i>T</i> có hệ số nhiệt độ của điện trở âm nhỏ, cỡ −1% °C⁻¹. "
        "Khi nhiệt độ tăng, hệ số nhiệt độ của điện trở trở thành dương và điện trở bắt đầu tăng. "
        "Tại một nhiệt độ ngưỡng hay nhiệt độ chuyển mạch, tốc độ tăng trở nên rất nhanh và đặc "
        "tính PTC trở nên rất dốc. Trong dải chuyển mạch của nó, hệ số nhiệt độ của điện trở có "
        "thể lên tới 100% °C⁻¹ và linh kiện có giá trị điện trở cao. Ở nhiệt độ trên dải chuyển "
        "mạch, điện trở đạt giá trị cực đại, vượt qua đó hệ số nhiệt độ lại trở thành âm. Có thể "
        "thay đổi nhiệt độ chuyển mạch trong khoảng 80 °C đến 240 °C bằng cách thay đổi thành phần "
        "hóa học của gốm. Ứng dụng điển hình của nhiệt điện trở PTC kiểu chuyển mạch là bảo vệ quá "
        "nhiệt, hạn chế dòng và tự điều chỉnh nhiệt. Hệ số nhiệt độ của điện trở của một linh kiện "
        "dùng làm phần tử gia nhiệt thường khoảng 25% °C⁻¹ ở nhiệt độ chuyển mạch 240 °C [1, 2]."))
    b.append(fig(16, F.fig(16), "vi"))
    b.append(p(
        "Nhiệt điện trở NTC gồm các oxit kim loại như oxit của crom, coban, đồng, sắt, mangan, "
        "niken và titan. Những linh kiện này có điện trở giảm đơn điệu khi nhiệt độ tăng. Đặc tính "
        "điện trở – nhiệt độ của nhiệt điện trở NTC là phi tuyến và xấp xỉ đặc tính của chất bán "
        "dẫn nội tại, ở đó sự phụ thuộc nhiệt độ của điện trở là do kích thích hạt tải vượt qua "
        "một khe năng lượng. Do đó, logarit của điện trở nhiệt điện trở NTC gần như là một hàm "
        "tuyến tính của nghịch đảo nhiệt độ tuyệt đối. Dưới nhiệt độ phòng, độ dốc của hàm giảm và "
        "nhiệt điện trở hành xử giống chất bán dẫn ngoại lai hơn. Cơ chế dẫn thực tế tương đương "
        "cơ chế “nhảy” quan sát thấy ở ferit và manganit có cấu trúc tinh thể spinel. Sự dẫn xảy "
        "ra khi hạt tải điện nhảy từ một vị trí ion trong mạng spinel sang một vị trí kề bên. Kiểu "
        "nhảy này xảy ra được khi các ion của cùng một nguyên tố, có hóa trị khác nhau 1, cùng nằm "
        "trên những vị trí mạng tương đương."))
    b.append(p(
        "Do đặc tính điện trở – nhiệt độ phi tuyến, hệ số nhiệt độ của điện trở của nhiệt điện trở "
        "NTC thay đổi theo nhiệt độ. Tùy hệ vật liệu, hệ số này ở 25 °C thường nằm trong khoảng −3 "
        "đến −5% °C⁻¹. Ở −60 °C, nó nằm trong khoảng −6,4 đến −11,3% °C⁻¹; còn ở 100 °C, nó biến "
        "thiên từ −2,1 đến −3,7% °C⁻¹. Tỉ số điện trở tương ứng so với 25 °C, "
        "<i>R</i><sub>T</sub>/<i>R</i><sub>25</sub>, là 41 đến 228 ở −60 °C và 0,13 đến 0,03 ở "
        "100 °C. Độ dốc của đặc tính log <i>R</i> theo 1/<i>T</i>, ký hiệu β, tương đối ổn định. "
        "Các hệ vật liệu nêu số liệu trên có giá trị β từ 2930 đến 5135 K trong khoảng 25 đến "
        "125 °C [1]."))
    b.append(p(
        "Dù đặc tính điện trở – nhiệt độ của nhiệt điện trở NTC là phi tuyến, vẫn có thể đạt độ "
        "tuyến tính tốt cho đặc tính điện dẫn – nhiệt độ và điện trở – nhiệt độ bằng các mạng "
        "nhiệt điện trở – điện trở. Mắc một điện trở nối tiếp với nhiệt điện trở cho ta một mạng "
        "điện dẫn tuyến tính, ví dụ một cầu phân áp. Dòng điện thu được khi đặt một điện áp lên "
        "mạng là tuyến tính theo nhiệt độ. Do đó, đầu ra của cầu phân áp (điện áp trên điện trở) là "
        "tuyến tính theo nhiệt độ. Tổ hợp song song của một điện trở và một nhiệt điện trở là một "
        "mạng điện trở tuyến tính. Có các kỹ thuật tối ưu hóa độ tuyến tính của mạng một nhiệt "
        "điện trở [3, 4]."))
    b.append(p(
        "Những mạng như vậy có đường cong hình chữ S cho đặc tính điện áp – nhiệt độ hoặc điện trở "
        "– nhiệt độ. Với dải nhiệt độ 20 °C đến 30 °C, độ lệch cực đại giữa một điểm bất kỳ trên "
        "đường cong và đường thẳng xấp xỉ tốt nhất là nhỏ. Khi dải vượt quá 30 °C, độ lệch tuyến "
        "tính cực đại tăng nhanh, từ khoảng 0,15 °C với dải 30 °C lên 0,7 °C với dải 50 °C. Dùng "
        "mạng hai nhiệt điện trở có thể đạt độ lệch tuyến tính cực đại 0,22 °C trên dải 0 °C đến "
        "100 °C, so với 2 °C khi dùng mạng một nhiệt điện trở [5]. Ứng dụng của nhiệt điện trở NTC "
        "gồm đo, điều khiển và bù nhiệt độ."))
    b.append(p(
        "Khi có dòng điện chạy qua nhiệt điện trở, xuất hiện hiệu ứng tự đốt nóng do công suất tiêu "
        "tán trong nó. Nhiệt độ nhiệt điện trở tăng cho đến khi tốc độ thất thoát nhiệt từ nhiệt "
        "điện trở ra môi trường xung quanh bằng công suất tiêu tán. Ở điều kiện cân bằng nhiệt "
        "này, độ tăng nhiệt tỉ lệ thuận với công suất tiêu tán trong nhiệt điện trở. Hằng số tỉ lệ "
        "δ là hằng số tiêu tán của nhiệt điện trở. Theo định nghĩa, δ là tỉ số — ở một nhiệt độ môi "
        "trường, điều kiện lắp đặt và môi trường xác định — giữa mức thay đổi công suất tiêu tán "
        "trong nhiệt điện trở và mức thay đổi nhiệt độ thân tương ứng. Các yếu tố ảnh hưởng đến "
        "hằng số tiêu tán là diện tích bề mặt nhiệt điện trở, độ dẫn nhiệt và tốc độ chuyển động "
        "tương đối của môi trường quanh nhiệt điện trở, thất thoát nhiệt do đối lưu tự nhiên trong "
        "môi trường đứng yên, truyền nhiệt giữa nhiệt điện trở và giá lắp qua dây dẫn, và thất "
        "thoát nhiệt do bức xạ (đáng kể với chất khí ở áp suất thấp). Vì độ dẫn nhiệt của chất lưu "
        "thay đổi theo nhiệt độ và đối lưu tự nhiên phụ thuộc chênh lệch nhiệt độ giữa nhiệt điện "
        "trở và môi trường, δ không phải là một hằng số đúng nghĩa. Đặc biệt với chất khí, hằng số "
        "tiêu tán thay đổi theo cả nhiệt độ thân nhiệt điện trở lẫn mức tự đốt nóng."))
    b.append(p(
        "Hằng số thời gian nhiệt τ là đáp ứng 63,2% khi nhiệt độ nhiệt điện trở thay đổi theo hàm "
        "bậc thang, trong điều kiện công suất tiêu tán trong nhiệt điện trở không đáng kể. Hằng số "
        "thời gian nhiệt chỉ có ý nghĩa khi đáp ứng là một hàm mũ đơn. Trong trường hợp đó, một "
        "khoảng thời gian τ cho mức thay đổi 63,2% giữa nhiệt độ đầu và nhiệt độ xác lập cuối, còn "
        "khoảng thời gian 5τ cho mức thay đổi 99,3%. Với một cấu trúc phức tạp hơn, chẳng hạn nhiệt "
        "điện trở được bao trong vỏ cảm biến, có thể tồn tại nhiều hàm mũ và không thể đoán rằng "
        "đáp ứng 99% sẽ đến sau năm hằng số thời gian. Cũng như hằng số tiêu tán, hằng số thời gian "
        "nhiệt phụ thuộc tốc độ truyền nhiệt giữa nhiệt điện trở và môi trường. Do đó, mọi yếu tố "
        "làm tăng hằng số tiêu tán đều làm giảm hằng số thời gian."))
    b.append(p(
        "Các kiểu linh kiện PTC silic thông dụng nhất là vỏ điốt thủy tinh có đường kính 1,8 mm "
        "đến 2,5 mm và chiều dài 3,8 mm đến 7,5 mm, và vỏ epoxy đúc có đường kính 3,6 mm đến "
        "6,0 mm và chiều dài 10,4 mm đến 15,0 mm. Những linh kiện này có dây dẫn hướng trục. Cũng "
        "có loại chip và đĩa phủ epoxy với dây dẫn hướng kính, đường kính khoảng 3 mm. Nhiệt điện "
        "trở PTC silic tuân theo MIL-T-23648 có dải nhiệt độ làm việc −55 °C đến 125 °C. Loại "
        "thương mại có thể có dải −65 °C đến 150 °C [6]."))
    b.append(p(
        "Cấu hình thông dụng nhất của nhiệt điện trở PTC kiểu chuyển mạch là đĩa có dây dẫn hướng "
        "kính, có hoặc không có lớp phủ cách điện. Linh kiện loại này có đường kính 4 mm đến "
        "26 mm. Chiều dày nằm trong khoảng 0,5 mm đến 6,5 mm. Chúng cũng có loại gắn trên bề mặt, "
        "loại đĩa không dây dẫn và loại vỏ điốt thủy tinh. Đĩa PTC kiểu chuyển mạch có dải nhiệt độ "
        "bảo quản −25 °C đến 155 °C và dải làm việc 0 °C đến 55 °C [1]."))
    b.append(p(
        "Trọng tâm của phần này là nhiệt điện trở NTC. Hầu hết ứng dụng nhiệt điện trở dùng loại "
        "này. Nhiệt điện trở NTC có hai nhóm chính. Nhiệt điện trở kiểu hạt có dây dẫn bằng hợp kim "
        "bạch kim được thiêu kết vào thân gốm. Nhiệt điện trở kiểu chip, đĩa, gắn bề mặt, mảnh và "
        "thanh có điện cực bề mặt kim loại hóa. Nhóm sau bao gồm vỏ điốt thủy tinh, trong đó dây "
        "dumet được liên kết áp vào đĩa hoặc chip."))
    b.append(p(
        "Hạt phủ thủy tinh có cả cấu hình dây dẫn kề bên và đối diện, đường kính 0,125 mm đến "
        "1,5 mm. Đầu dò thủy tinh có đường kính 0,4 mm đến 2,5 mm, chiều dài từ 1,5 mm đến "
        "6,35 mm. Đầu dò đường kính 1,5 mm đến 2,5 mm có chiều dài 3 mm đến 12,7 mm, còn đầu dò lớn "
        "hơn với đường kính 2 mm đến 2,5 mm có chiều dài tới 50 mm. Thanh thủy tinh thường dài "
        "6,3 mm với đường kính 1,5 mm đến 2,5 mm. Đầu dò thủy tinh gồm một nhiệt điện trở kiểu hạt "
        "trần được hàn kín ở đầu một thanh thủy tinh đặc, cùng dây dẫn dumet hướng kính. So sánh "
        "thì thanh thủy tinh có hạt được hàn kín ở giữa một thanh thủy tinh đặc và dây dẫn dumet "
        "hướng trục. Dải nhiệt độ quy định trong MIL-T-23648 là −55 °C đến 200 °C với hạt phủ thủy "
        "tinh và −55 °C đến 275 °C với đầu dò và thanh thủy tinh. Loại thương mại của các linh kiện "
        "bọc thủy tinh này thường có dải −80 °C đến 300 °C. Một số linh kiện được định mức làm việc "
        "gián đoạn ở 600 °C, còn các linh kiện đông lạnh đặc biệt được định mức làm việc trong "
        "khoảng −196 °C đến 25 °C."))
    b.append(p(
        "Nhiệt điện trở chip có dây dẫn hướng kính có tiết diện 0,25 mm × 0,25 mm đến 13 mm × "
        "13 mm và chiều dày 0,175 mm đến 1,5 mm. Đĩa đường kính 1 mm đến 25 mm có cả loại dây dẫn "
        "hướng kính và hướng trục, chiều dày 0,25 mm đến 6,35 mm. Chip và đĩa cũng có loại vỏ điốt "
        "thủy tinh với dây dẫn dumet hướng trục. Chip gắn bề mặt có kích thước dài 2 mm đến "
        "3,2 mm × rộng 1,1 mm đến 1,6 mm × dày 0,36 mm đến 1,3 mm. Nhiệt điện trở kiểu mảnh, có cả "
        "dây dẫn kề bên và đối diện, có chiều dày 0,025 mm đến 0,125 mm với tiết diện 0,5 mm × "
        "0,5 mm đến 3 mm × 3 mm. Dải nhiệt độ quy định cho chip, đĩa, thanh và vỏ điốt thủy tinh "
        "trong MIL-T-23648 là −55 °C đến 125 °C. Chip và đĩa thương mại có dải nhiệt độ làm việc "
        "−80 °C đến 155 °C [1]. Thanh có loại dùng trong dải −60 °C đến 150 °C [7], và vỏ điốt "
        "thủy tinh có dải làm việc −60 °C đến 300 °C [8]."))

    # ------------------------------------------------------------ thermal
    b.append(h3("Tính chất nhiệt của nhiệt điện trở NTC", "Thermal Properties of NTC Thermistors"))
    b.append(p(
        "Năng lượng tiêu tán dưới dạng nhiệt trong một nhiệt điện trở mắc vào mạch điện làm nhiệt "
        "độ thân nhiệt điện trở tăng lên trên nhiệt độ môi trường của nó. Tại mọi thời điểm, "
        "phương trình truyền nhiệt áp dụng được là:"))
    b.append(eq(_frac("d<i>H</i>", "d<i>t</i>") +
                " = <i>P</i> = <i>E</i><sub>T</sub><i>I</i><sub>T</sub> = δ(<i>T</i> − "
                "<i>T</i><sub>a</sub>) + <i>cm</i> " + _frac("d<i>T</i>", "d<i>t</i>"), "32.26"))
    b.append(wl([
        "<i>dH</i>/<i>dt</i> = <i>P</i> = <i>E</i><sub>T</sub><i>I</i><sub>T</sub> = tốc độ cấp "
        "năng lượng nhiệt hay nhiệt lượng cho nhiệt điện trở",
        "δ = hằng số tiêu tán",
        "<i>T</i><sub>a</sub> = nhiệt độ môi trường",
        "δ(<i>T</i> − <i>T</i><sub>a</sub>) = tốc độ thất thoát nhiệt ra môi trường xung quanh",
        "<i>c</i> và <i>m</i> = tương ứng nhiệt dung riêng và khối lượng của nhiệt điện trở",
        "<i>cm</i>(<i>dT</i>/<i>dt</i>) = tốc độ hấp thụ nhiệt của nhiệt điện trở",
    ]))
    b.append(p("Nghiệm của Phương trình 32.26 khi <i>P</i> không đổi là:"))
    b.append(eq("<i>T</i> = <i>T</i><sub>a</sub> + " + _frac("<i>P</i>", "δ") +
                "[1 − exp(−" + _frac("δ", "<i>cm</i>") + "<i>t</i>)]", "32.27"))
    b.append(p(
        "Nghiệm quá độ của Phương trình 32.27 là cơ sở cho đặc tính dòng – thời gian của nhiệt "
        "điện trở. Khi <i>t</i> ≫ <i>cm</i>/δ thì <i>dT</i>/<i>dt</i> → 0, và nghiệm xác lập của "
        "Phương trình 32.27 trở thành:"))
    b.append(eq("<i>P</i> = <i>E</i><sub>T</sub><i>I</i><sub>T</sub> = δ(<i>T</i> − "
                "<i>T</i><sub>a</sub>)", "32.28"))
    b.append(p(
        "trong đó <i>E</i><sub>T</sub> và <i>I</i><sub>T</sub> tương ứng là điện áp và dòng điện "
        "xác lập của nhiệt điện trở. Phương trình 32.28 là cơ sở cho đặc tính dòng – áp của nhiệt "
        "điện trở."))
    b.append(p(
        "Bằng cách giảm công suất của nhiệt điện trở xuống mức tự đốt nóng không đáng kể, "
        "<i>P</i> → 0, Phương trình 32.26 trở thành:"))
    b.append(eq(_frac("d<i>T</i>", "d<i>t</i>") + " = −" + _frac("δ", "<i>cm</i>") +
                "(<i>T</i> − <i>T</i><sub>a</sub>)", "32.29"))
    b.append(p(
        "Phương trình 32.29 là phát biểu toán học của định luật làm nguội Newton và có nghiệm:"))
    b.append(eq("<i>T</i> = <i>T</i><sub>a</sub> + (<i>T</i><sub>i</sub> − <i>T</i><sub>a</sub>) "
                "exp(−<i>t</i>/τ)"))
    b.append(wl([
        "<i>T</i><sub>i</sub> = nhiệt độ thân ban đầu của nhiệt điện trở",
        "<i>T</i><sub>a</sub> = nhiệt độ môi trường",
        "τ = <i>cm</i>/δ = hằng số thời gian nhiệt",
    ]))
    b.append(p(
        "Bảng 32.8 cho số liệu hằng số tiêu tán và hằng số thời gian của hạt phủ thủy tinh, đầu dò "
        "thủy tinh và thanh thủy tinh. Bảng 32.9 liệt kê số liệu tương tự cho nhiệt điện trở kiểu "
        "chip, đĩa và thanh có tiếp xúc bề mặt kim loại hóa. Số liệu hằng số tiêu tán và hằng số "
        "thời gian là của nhiệt điện trở treo bằng dây dẫn ở 25 °C, theo quy trình quy định trong "
        "MIL-T-23648A. Độ tăng nhiệt dùng để tính hằng số tiêu tán là kết quả của việc tự đốt nóng "
        "nhiệt điện trở lên 75 °C từ môi trường 25 °C. Số liệu hằng số thời gian là kết quả của "
        "việc để nhiệt điện trở nguội từ 75 °C xuống môi trường 25 °C. Số liệu hằng số thời gian "
        "khi nhúng nước là kết quả của việc nhúng nhanh nhiệt điện trở từ không khí ở nhiệt độ "
        "phòng vào nước đứng yên. Thời gian chuyển không đáng kể. Nhiệt độ không khí khoảng 25 °C "
        "và nhiệt độ nước khoảng 5 °C. Đường kính ghi cho các linh kiện phủ epoxy lắp lẫn được là "
        "đường kính cực đại. Để minh họa ảnh hưởng của môi trường đến tính chất nhiệt của các linh "
        "kiện này, hằng số tiêu tán và hằng số thời gian là 8 mW °C⁻¹ và 1 s khi thử trong dầu "
        "khuấy, so với 1 mW °C⁻¹ và 10 s khi thử trong không khí đứng yên. Hằng số tiêu tán và hằng "
        "số thời gian của đĩa phụ thuộc chiều dày đĩa, đường kính dây dẫn, lượng thiếc hàn dùng để "
        "gắn dây, khoảng cách giữa thân nhiệt điện trở và giá lắp, và vật liệu nhiệt điện trở. Hằng "
        "số tiêu tán và hằng số thời gian của thanh phụ thuộc chiều dài thanh cùng các biến số đã "
        "nêu cho đĩa."))
    b.append(_t328("vi"))
    b.append(_t329("vi"))

    # ------------------------------------------------------------ electrical
    b.append(h3("Tính chất điện của nhiệt điện trở NTC", "Electrical Properties of NTC Thermistors"))
    b.append(p(
        "Ứng dụng của nhiệt điện trở phụ thuộc ba đặc tính điện cơ bản. Đó là đặc tính dòng – áp, "
        "đặc tính dòng – thời gian và đặc tính điện trở – nhiệt độ."))

    b.append(h4("Đặc tính dòng – áp", "Voltage–Current Characteristics"))
    b.append(p(
        "Hình 32.17 cho thấy một đường cong dòng – áp điển hình. Ở dòng nhỏ, công suất tiêu tán "
        "nhỏ so với hằng số tiêu tán và hiệu ứng tự đốt nóng không đáng kể. Trong điều kiện đó, "
        "điện trở là hằng số, không phụ thuộc dòng điện, và điện áp tỉ lệ với dòng điện. Do đó, ở "
        "dòng nhỏ, đường đặc tính tiếp tuyến với một đường điện trở không đổi bằng điện trở ở công "
        "suất không của nhiệt điện trở. Khi dòng tăng, hiệu ứng tự đốt nóng trở nên rõ hơn; nhiệt "
        "độ nhiệt điện trở tăng và điện trở bắt đầu giảm. Với mỗi mức tăng thêm của dòng điện đều "
        "có một mức giảm tương ứng của điện trở. Vì vậy, độ dốc của đặc tính dòng – áp giảm khi "
        "dòng tăng. Điều này tiếp diễn cho đến khi dòng đạt giá trị mà tại đó độ dốc bằng không. "
        "Vượt qua điểm này, nơi điện áp đạt cực đại, độ dốc tiếp tục giảm và nhiệt điện trở thể "
        "hiện đặc tính điện trở âm. Nhiệt độ, điện áp và dòng điện tương ứng với đỉnh đường cong "
        "là:"))
    b.append(eq("<i>T</i><sub>p</sub> = " +
                _frac("β − " + _sq("β<sup>2</sup> − 4β<i>T</i><sub>a</sub>"), "2"), "32.30"))
    b.append(eq("<i>E</i><sub>p</sub> = " +
                _sq("<i>R</i><sub>p</sub> δ(<i>T</i><sub>p</sub> − <i>T</i><sub>a</sub>)"), "32.31"))
    b.append(eq("<i>I</i><sub>p</sub> = " +
                _sq(_frac("δ(<i>T</i><sub>p</sub> − <i>T</i><sub>a</sub>)",
                          "<i>R</i><sub>p</sub>")), "32.32"))
    b.append(wl([
        "<i>T</i><sub>p</sub> = nhiệt độ tuyệt đối (K) tại đó đỉnh xuất hiện",
        "<i>T</i><sub>a</sub> = nhiệt độ môi trường tuyệt đối (K)",
        "<i>R</i><sub>p</sub> = điện trở của nhiệt điện trở tại <i>T</i><sub>p</sub>",
    ]))
    b.append(p(
        "Các ứng dụng dựa trên đặc tính dòng – áp liên quan đến sự thay đổi điểm làm việc trên một "
        "đường cong hoặc một họ đường cong. Những thay đổi đó là do thay đổi điều kiện môi trường "
        "hoặc do biến thiên tham số mạch. Hình 32.17 cho một lời giải đồ thị để tìm điểm làm việc. "
        "Đường cong biểu diễn quan hệ phi tuyến giữa điện áp và dòng điện của nhiệt điện trở. Mạch "
        "tương đương Thevenin nhìn từ hai cực của nhiệt điện trở cho quan hệ nêu trong Phương trình "
        "32.33."))
    b.append(eq("<i>E</i><sub>T</sub> = <i>E</i><sub>THEV</sub> − "
                "<i>I</i><sub>T</sub><i>R</i><sub>THEV</sub>", "32.33"))
    b.append(p(
        "trong đó <i>E</i><sub>T</sub> và <i>I</i><sub>T</sub> tương ứng là điện áp và dòng điện "
        "của nhiệt điện trở. Quan hệ tuyến tính của Phương trình 32.33 là đường tải của nhiệt điện "
        "trở tự đốt nóng. Giao điểm của nó với đặc tính dòng – áp là điểm làm việc. Bảng 32.10 phân "
        "các ứng dụng quen thuộc hơn thành bốn nhóm, phân biệt theo dạng kích thích nhiệt điện trở "
        "[1, 14]."))
    b.append(_t3210("vi"))
    b.append(fig(17, F.fig(17), "vi"))

    b.append(h4("Đặc tính dòng – thời gian", "Current–Time Characteristics"))
    b.append(p(
        "Đặc tính dòng – áp trình bày ở trên nói về một nhiệt điện trở tự đốt nóng làm việc ở điều "
        "kiện xác lập. Điều kiện này — trong đó điện trở của nhiệt điện trở giảm do một dòng điện "
        "đủ lớn gây tự đốt nóng — không xảy ra tức thời. Trong mạch nhiệt điện trở tồn tại một "
        "trạng thái quá độ kể từ lúc bắt đầu cấp nguồn (<i>t</i> = 0) cho đến khi đạt cân bằng "
        "nhiệt (<i>t</i> ≫ τ). Quan hệ giữa dòng điện của nhiệt điện trở và thời gian cần để đạt "
        "cân bằng nhiệt là đặc tính dòng – thời gian. Nói chung, kích thích là một hàm bậc thang "
        "điện áp qua một nguồn tương đương Thevenin. Hình 32.18 cho thấy đặc tính dòng – thời gian "
        "của một số đĩa nhiệt điện trở và nguồn điện áp. Với một đặc tính cho trước, điện áp nguồn, "
        "điện trở nguồn và điện trở ở công suất không của nhiệt điện trở quyết định dòng điện ban "
        "đầu. Điện áp nguồn, điện trở nguồn và đặc tính dòng – áp quyết định giá trị cân bằng cuối "
        "cùng. Đường cong giữa giá trị ban đầu và giá trị cuối phụ thuộc các tham số thiết kế "
        "mạch, cũng như hằng số tiêu tán và nhiệt dung của nhiệt điện trở. Việc chọn đúng nhiệt "
        "điện trở và thiết kế mạch đúng cho thời gian quá độ trong khoảng vài mili giây đến vài "
        "phút."))
    b.append(fig(18, F.fig(18), "vi"))
    b.append(p(
        "Các ứng dụng dựa trên đặc tính dòng – thời gian là trễ thời gian, chống xung, bảo vệ dây "
        "tóc, bảo vệ quá tải và chuyển mạch tuần tự."))

    b.append(h4("Đặc tính điện trở – nhiệt độ", "Resistance–Temperature Characteristics"))
    b.append(p(
        "Thuật ngữ điện trở ở công suất không áp dụng cho nhiệt điện trở làm việc với mức tự đốt "
        "nóng không đáng kể. Đặc tính này mô tả quan hệ giữa điện trở ở công suất không của một "
        "nhiệt điện trở và nhiệt độ môi trường của nó. Trên những dải nhiệt độ nhỏ, quan hệ gần "
        "tuyến tính giữa logarit của điện trở và nghịch đảo nhiệt độ tuyệt đối được cho bởi:"))
    b.append(eq("ln <i>R</i><sub>T</sub> ≡ <i>A</i> + " + _frac("β", "<i>T</i>"), "32.34"))
    b.append(wl([
        "<i>T</i> = nhiệt độ tuyệt đối (K)",
        "β = hằng số vật liệu của nhiệt điện trở",
    ]))
    b.append(p(
        "Nếu đặt <i>R</i><sub>T</sub> = <i>R</i><sub>T0</sub> tại nhiệt độ chuẩn <i>T</i> = "
        "<i>T</i><sub>0</sub> và giải ra <i>R</i><sub>T</sub>, ta được:"))
    b.append(eq("<i>R</i><sub>T</sub> ≅ <i>R</i><sub>T0</sub> exp[ " +
                _frac("β(<i>T</i><sub>0</sub> − <i>T</i>)", "<i>TT</i><sub>0</sub>") + " ]", "32.35"))
    b.append(p("Hệ số nhiệt độ của điện trở α được định nghĩa là:"))
    b.append(eq("α ≡ " + _frac("1", "<i>R</i><sub>T</sub>") + " " +
                _frac("d<i>R</i><sub>T</sub>", "d<i>T</i>"), "32.36"))
    b.append(p("Giải Phương trình 32.34 theo α ta được:"))
    b.append(eq("α = − " + _frac("β", "<i>T</i><sup>2</sup>"), "32.37"))
    b.append(p(
        "Trong Phương trình 32.34, độ lệch khỏi tuyến tính gây ra sai số nhiệt độ 0,01 °C, 0,1 °C "
        "và 0,3 °C tương ứng với các dải nhiệt độ 10 °C, 30 °C và 50 °C, trong khoảng 0 °C đến "
        "50 °C. Dùng một đa thức cho ln <i>R</i><sub>T</sub> theo 1/<i>T</i> làm giảm sai số đáng "
        "kể. Bậc của đa thức cần thiết phụ thuộc dải nhiệt độ và hệ vật liệu dùng. Đa thức bậc ba "
        "là đủ cho hầu hết ứng dụng. Vì vậy, các biểu thức chính xác hơn cho đặc tính điện trở – "
        "nhiệt độ là:"))
    b.append(eq("ln <i>R</i><sub>T</sub> = <i>A</i><sub>0</sub> + " +
                _frac("<i>A</i><sub>1</sub>", "<i>T</i>") + " + " +
                _frac("<i>A</i><sub>2</sub>", "<i>T</i><sup>2</sup>") + " + " +
                _frac("<i>A</i><sub>3</sub>", "<i>T</i><sup>3</sup>"), "32.38a"))
    b.append(eq("ln <i>R</i><sub>T</sub> = <i>A</i><sub>0</sub> + " +
                _frac("<i>A</i><sub>1</sub>", "<i>T</i>") + " + " +
                _frac("<i>A</i><sub>2</sub>", "<i>T</i><sup>2</sup>") + " + " +
                _frac("<i>A</i><sub>3</sub>", "<i>T</i><sup>3</sup>"), "32.38b"))
    b.append(note(
        "Trong bản gốc, Phương trình 32.38a và 32.38b được in giống hệt nhau. Bản dịch giữ nguyên "
        "như đã in thay vì tự sửa, để người đọc đối chiếu được với sách."))
    b.append(eq(_frac("1", "<i>T</i>") + " = α<sub>0</sub> + α<sub>1</sub> ln " +
                "<i>R</i><sub>T</sub> + α<sub>2</sub>(ln <i>R</i><sub>T</sub>)<sup>2</sup> + "
                "α<sub>3</sub>(ln <i>R</i><sub>T</sub>)<sup>3</sup>", "32.39"))
    b.append(p(
        "Steinhart và Hart đề nghị dùng Phương trình 32.39 cho dải hải dương học −2 °C đến 30 °C "
        "[11]. Phân tích của họ cho thấy không mất độ chính xác đáng kể khi bỏ số hạng bình "
        "phương α<sub>2</sub>(ln <i>R</i><sub>T</sub>)<sup>2</sup>. Vì vậy, họ đề nghị dùng "
        "Phương trình 32.40."))
    b.append(eq(_frac("1", "<i>T</i>") + " = <i>b</i><sub>0</sub> + <i>b</i><sub>1</sub> ln " +
                "<i>R</i><sub>T</sub> + <i>b</i><sub>3</sub>(ln <i>R</i><sub>T</sub>)"
                "<sup>3</sup>", "32.40"))
    b.append(p(
        "Mangum báo cáo rằng dùng Phương trình 32.40 cho sai số nội suy khoảng 0,001 °C trên dải "
        "0 °C đến 70 °C [12]."))
    b.append(p(
        "Nhóm kỹ thuật của Thermometrics, Inc. đã đánh giá Phương trình 32.38 trên dải −80 °C đến "
        "260 °C với 17 vật liệu nhiệt điện trở khác nhau. Các đầu dò thủy tinh được khảo sát trải "
        "trên một dải điện trở suất từ 2 Ω cm đến 300 kΩ cm và một dải điện trở ở 25 °C từ 10 Ω đến "
        "2 MΩ. Kết quả được trình bày tại Hội nghị Quốc tế lần thứ sáu về Nhiệt độ và cho thấy sai "
        "số nội suy không vượt quá tổng độ không đảm bảo đo. Với các dải nhiệt độ 100 °C trong "
        "khoảng −80 °C đến 260 °C, 150 °C trong khoảng −60 °C đến 260 °C, và 150 °C đến 200 °C "
        "trong khoảng 0 °C đến 260 °C, sai số nội suy là 0,005 °C đến 0,01 °C [13]. Giảm dải nhiệt "
        "độ xuống 50 °C trong khoảng 0 °C đến 260 °C làm sai số nội suy giảm còn 0,001 °C đến "
        "0,003 °C."))
    b.append(p(
        "Sapoff và Siwek [14] đánh giá độ chính xác bị mất khi bỏ số hạng bậc hai trong Phương "
        "trình 32.38. Trong điều kiện đó, Phương trình 32.38 rút gọn thành Phương trình 32.41."))
    b.append(eq("ln <i>R</i><sub>T</sub> = <i>C</i><sub>0</sub> + " +
                _frac("<i>C</i><sub>1</sub>", "<i>T</i>") + " + " +
                _frac("<i>C</i><sub>3</sub>", "<i>T</i><sup>3</sup>"), "32.41"))
    b.append(p(
        "Sai số nội suy do Phương trình 32.40 và 32.41 gây ra phụ thuộc hệ vật liệu, dải nhiệt độ "
        "(độ phi tuyến tăng ở nhiệt độ thấp) và dải nhiệt độ được khảo sát. Bảng 32.11 tóm tắt sai "
        "số gắn với việc dùng Phương trình 32.41 cho các dải và khoảng nhiệt độ khác nhau."))
    b.append(_t3211("vi"))
    b.append(p("Có thể viết lại các Phương trình 32.38 đến 32.41 thành:"))
    b.append(eq("<i>R</i><sub>T</sub> = exp( <i>A</i><sub>0</sub> + " +
                _frac("<i>A</i><sub>1</sub>", "<i>T</i>") + " + " +
                _frac("<i>A</i><sub>2</sub>", "<i>T</i><sup>2</sup>") + " + " +
                _frac("<i>A</i><sub>3</sub>", "<i>T</i><sup>3</sup>") + " )", "32.42"))
    b.append(eq("<i>T</i> = [ <i>a</i><sub>0</sub> + <i>a</i><sub>1</sub> ln "
                "<i>R</i><sub>T</sub> + <i>a</i><sub>2</sub>(ln <i>R</i><sub>T</sub>)"
                "<sup>2</sup> + <i>a</i><sub>3</sub>(ln <i>R</i><sub>T</sub>)<sup>3</sup> ]"
                "<sup>−1</sup>", "32.43"))
    b.append(eq("<i>T</i> = [ <i>b</i><sub>0</sub> + <i>b</i><sub>1</sub> ln "
                "<i>R</i><sub>T</sub> + <i>b</i><sub>3</sub>(ln <i>R</i><sub>T</sub>)"
                "<sup>3</sup> ]<sup>−1</sup>", "32.44"))
    b.append(eq("<i>R</i><sub>T</sub> = exp( <i>C</i><sub>0</sub> + " +
                _frac("<i>C</i><sub>1</sub>", "<i>T</i>") + " + " +
                _frac("<i>C</i><sub>3</sub>", "<i>T</i><sup>3</sup>") + " )", "32.45"))
    b.append(p(
        "Nghiệm của các Phương trình 32.38, 32.39, 32.42 và 32.43 cần bốn điểm hiệu chuẩn và phải "
        "giải hệ phương trình đồng thời. Tương tự, nghiệm của các Phương trình 32.40, 32.41, 32.44 "
        "và 32.45 cần ba điểm hiệu chuẩn. Dùng phân tích hồi quy đa thức với thêm điểm hiệu chuẩn "
        "có thể giảm thiểu ảnh hưởng của độ không đảm bảo đo khi hiệu chuẩn."))
    b.append(p(
        "Các ứng dụng phụ thuộc đặc tính điện trở – nhiệt độ là đo, điều khiển và bù nhiệt độ. Cũng "
        "có những ứng dụng trong đó nhiệt độ của nhiệt điện trở phụ thuộc một hiện tượng vật lý "
        "khác. Ví dụ, cao kế là dụng cụ trong đó nhiệt độ của một chất lỏng sôi cho biết áp suất hơi "
        "của chất lỏng đó. Một ví dụ khác là dùng ống thông tim kiểu nhiệt điện trở để phân tích "
        "pha loãng nhiệt. Một thể tích dung dịch nước muối hoặc dextroza đã biết, ở nhiệt độ đã "
        "biết, được bơm vào dòng máu qua một lòng của ống thông. Dung dịch trộn với máu làm loãng "
        "dung dịch và làm giảm nhiệt độ của máu khi máu chảy xuôi qua một nhiệt điện trở nằm trên "
        "bề mặt một lòng khác của ống thông. Cung lượng tim tính từ dữ liệu đáp ứng nhiệt độ – thời "
        "gian do nhiệt điện trở đo được cho biết hiệu suất bơm của tim."))

    # ------------------------------------------------------------ linearization
    b.append(h3("Kỹ thuật tuyến tính hóa và điều chế tín hiệu",
                "Linearization and Signal Conditioning Techniques"))
    b.append(p(
        "Điện trở đo được và các hằng số tính từ Phương trình 32.43 và 32.44 có thể dùng với máy "
        "tính để xác định nhiệt độ mà không cần mạng tuyến tính. Cách này hữu ích khi cần độ chính "
        "xác cao trên dải nhiệt độ tương đối rộng. Tuy vậy, hầu hết ứng dụng dựa trên đặc tính điện "
        "trở – nhiệt độ của nhiệt điện trở đều dùng một dạng tuyến tính hóa hoặc điều chế tín hiệu "
        "nào đó. Dùng một nguồn dòng không đổi với một mạng điện trở tuyến tính cho đầu ra điện áp "
        "tuyến tính theo nhiệt độ. Với tổ hợp đúng của dòng điện và mức điện trở, một vôn kế số mắc "
        "qua mạng sẽ hiển thị trực tiếp nhiệt độ. Dùng một nguồn áp không đổi cho một mạng điện dẫn "
        "tuyến tính với dòng điện tuyến tính theo nhiệt độ."))

    b.append(h4("Mạng dẫn tuyến tính", "Linear Conductance Networks"))
    b.append(p(
        "Cầu phân áp, mạch ôm kế và mạch cầu Wheatstone là những mạng dẫn tuyến tính. Xét mạch "
        "phân áp ở Hình 32.19. Dùng điện trở cố định làm lối ra sẽ loại bỏ ảnh hưởng của điện trở "
        "tải. Để tiện phân tích, điện trở ký hiệu <i>R</i> là tổ hợp song song của điện trở tải và "
        "điện trở phân áp cố định. Một ưu điểm nữa là với cách bố trí này, điện áp ra tăng theo "
        "nhiệt độ. Tỉ số giữa điện áp ra và điện áp vào được cho bởi:"))
    b.append(eq(_frac("<i>e</i><sub>0</sub>", "<i>e</i><sub>s</sub>") + " = " +
                _frac("<i>R</i>", "<i>R</i> + <i>R</i><sub>T</sub>") + " = " +
                _frac("1", "1 + <i>R</i><sub>T</sub>/<i>R</i>"), "32.46"))
    b.append(wl([
        "<i>e</i><sub>0</sub> = điện áp ra",
        "<i>e</i><sub>s</sub> = điện áp nguồn",
        "<i>R</i> = tổ hợp song song của điện trở tải và điện trở cố định",
        "<i>R</i><sub>T</sub> = điện trở của nhiệt điện trở tại nhiệt độ xác định <i>T</i>",
    ]))
    b.append(fig(19, F.fig(19), "vi"))
    b.append(p(
        "Nếu chuẩn hóa điện trở của nhiệt điện trở theo giá trị của nó tại nhiệt độ chuẩn xác định "
        "<i>T</i><sub>0</sub>, ta có:"))
    b.append(eq("<i>r</i><sub>T</sub> = " + _frac("<i>R</i><sub>T</sub>",
                                                 "<i>R</i><sub>T0</sub>"), "32.47"))
    b.append(wl([
        "<i>R</i><sub>T0</sub> = điện trở của nhiệt điện trở tại <i>T</i><sub>0</sub>",
        "<i>r</i><sub>T</sub> = tỉ số điện trở",
    ]))
    b.append(p(
        "Các nhà sản xuất nhiệt điện trở thường cung cấp đặc tính tỉ số điện trở – nhiệt độ trong "
        "catalog của họ. Thay Phương trình 32.47 vào Phương trình 32.46 ta được:"))
    b.append(eq(_frac("<i>e</i><sub>0</sub>", "<i>e</i><sub>s</sub>") + " = " +
                _frac("1", "1 + <i>r</i><sub>T</sub><i>R</i><sub>T0</sub>/<i>R</i>"), "32.48"))
    b.append(p(
        "Nếu hằng số mạch σ = <i>R</i><sub>T0</sub>/<i>R</i> thì Phương trình 32.48 trở thành:"))
    b.append(eq("<i>F</i>(<i>T</i>) = " + _frac("<i>e</i><sub>0</sub>", "<i>e</i><sub>s</sub>") +
                " = " + _frac("1", "1 + <i>r</i><sub>T</sub>σ"), "32.49"))
    b.append(p(
        "Đầu ra của cầu phân áp ở Hình 32.19a là đường cong hình chữ S như trên Hình 32.19b. Giá "
        "trị của hằng số mạch σ quyết định dải nhiệt độ mà trong đó tồn tại độ tuyến tính tốt giữa "
        "<i>e</i><sub>0</sub> và <i>T</i>. Tài liệu [3, 4] đưa ra các họ đường cong hình chữ S trên "
        "dải 0,01 ≤ σ ≤ 20,0 cho ba hệ vật liệu cơ bản của MIL-T-23648. Một tiêu chí tốt để đạt độ "
        "tuyến tính tối ưu là cho độ dốc của hàm <i>F</i>(<i>T</i>) tại hai đầu mút của dải nhiệt "
        "độ xác định bằng nhau, <i>T</i><sub>L</sub> ≤ σ ≤ <i>T</i><sub>H</sub>. Đặt "
        "<i>dF</i>(<i>T</i><sub>L</sub>)/<i>dT</i> = <i>dF</i>(<i>T</i><sub>H</sub>)/<i>dT</i> cho "
        "kết quả sau:"))
    b.append(eq("σ = " + _frac("<i>X</i> − <i>Y</i>",
                               "<i>Yr</i><sub>TL</sub> − <i>Xr</i><sub>TH</sub>"), "32.50"))
    b.append(p(
        "trong đó <i>X</i> và <i>Y</i> được xác định bởi các điều kiện ở hai đầu mút và các hằng số "
        "của phương trình ln <i>R</i><sub>T</sub> theo <i>T</i>. Khi dùng Phương trình 32.41, "
        "<i>X</i> và <i>Y</i> được cho bởi:"))
    b.append(eq("<i>X</i> = <i>T</i><sub>H</sub> " +
                _sq("<i>r</i><sub>TL</sub>(<i>C</i><sub>1</sub> + 3" +
                    _frac("<i>C</i><sub>3</sub>", "<i>T</i><sub>H</sub><sup>2</sup>") + ")"), "32.51"))
    b.append(eq("<i>Y</i> = <i>T</i><sub>L</sub> " +
                _sq("<i>r</i><sub>TH</sub>(<i>C</i><sub>1</sub> + 3" +
                    _frac("<i>C</i><sub>3</sub>", "<i>T</i><sub>L</sub><sup>2</sup>") + ")"), "32.52"))
    b.append(p("Khi dùng Phương trình 32.38, <i>X</i> và <i>Y</i> được cho bởi:"))
    b.append(eq("<i>X</i> = <i>T</i><sub>H</sub> " +
                _sq("<i>r</i><sub>TL</sub>(<i>A</i><sub>1</sub> + 2" +
                    _frac("<i>A</i><sub>2</sub>", "<i>T</i><sub>L</sub>") + " + 3" +
                    _frac("<i>A</i><sub>3</sub>", "<i>T</i><sub>L</sub><sup>2</sup>") + ")"), "32.53"))
    b.append(eq("<i>Y</i> = <i>T</i><sub>L</sub> " +
                _sq("<i>r</i><sub>TH</sub>(<i>A</i><sub>1</sub> + 2" +
                    _frac("<i>A</i><sub>2</sub>", "<i>T</i><sub>H</sub>") + " + 3" +
                    _frac("<i>A</i><sub>3</sub>", "<i>T</i><sub>H</sub><sup>2</sup>") + ")"), "32.54"))
    b.append(p(
        "Cho phép <i>e</i><sub>s</sub> và <i>R</i> là điện áp và điện trở tương đương Thevenin nhìn "
        "từ hai cực của nhiệt điện trở, phép phân tích cầu phân áp áp dụng được cho bất kỳ mạch "
        "phức tạp hơn nào, ví dụ cầu Wheatstone [3, 4]."))
    b.append(p(
        "Ràng buộc về tự đốt nóng của nhiệt điện trở thường dẫn đến những nguồn điện áp không "
        "chuẩn trong thiết kế mạch nhiệt kế. Các mạch phân áp biến đổi ở Hình 32.20 cho những mạch "
        "tương đương dùng nguồn điện áp chuẩn. Ở Hình 32.20a chỉ một phần điện áp ra khả dụng xuất "
        "hiện trên bộ phát hiện lối ra. Các nhiệt kế kiểu ôm kế dùng những mạch như vậy. Mạch ở "
        "Hình 32.20a cho toàn bộ điện áp ra khả dụng. Tuy nhiên, việc biến đổi tạo ra một điện áp "
        "phân cực mắc nối tiếp với đầu ra. Các nhiệt kế kiểu mạch cầu dùng mạch ở Hình 32.20b. Các "
        "phương trình biến đổi áp dụng cho Hình 32.20a là:"))
    b.append(eq("<i>K</i> = " + _frac("<i>R</i><sub>1</sub>",
                                      "<i>R</i><sub>1</sub> + <i>R</i><sub>2</sub>") +
                " = " + _frac("<i>E</i><sub>1</sub>", "<i>E</i><sub>2</sub>") +
                " = " + _frac("<i>R</i><sub>4</sub>", "<i>R</i><sub>2</sub>"), "32.55"))
    b.append(fig(20, F.fig(20), "vi"))
    b.append(eq("<i>R</i> = <i>R</i><sub>3</sub> + <i>R</i><sub>4</sub> = "
                "<i>R</i><sub>3</sub> + " +
                _frac("<i>R</i><sub>1</sub><i>R</i><sub>2</sub>",
                      "<i>R</i><sub>1</sub> + <i>R</i><sub>2</sub>"), "32.56"))
    b.append(eq("<i>E</i><sub>2</sub> = nguồn điện áp mong muốn", "32.57"))
    b.append(eq("<i>R</i><sub>2</sub> = " + _frac("<i>R</i><sub>4</sub>", "<i>K</i>"), "32.58"))
    b.append(eq("<i>R</i><sub>1</sub> = " +
                _frac("<i>R</i><sub>2</sub><i>R</i><sub>4</sub>",
                      "<i>R</i><sub>2</sub> − <i>R</i><sub>4</sub>"), "32.59"))
    b.append(eq(_big(_frac("<i>R</i><sub>3</sub>",
                            "<i>R</i><sub>3</sub> + <i>R</i><sub>4</sub>")) +
                " <i>F</i>(<i>T</i>)", "32.60"))
    b.append(p("Các phương trình biến đổi áp dụng cho Hình 32.20b là:"))
    b.append(eq("<i>K</i> = " + _frac("<i>R</i><sub>2</sub>",
                                      "<i>R</i><sub>1</sub> + <i>R</i><sub>2</sub>") +
                " = " + _frac("<i>E</i><sub>1</sub>", "<i>E</i><sub>2</sub>") +
                " = " + _frac("<i>R</i>", "<i>R</i><sub>1</sub>"), "32.61"))
    b.append(eq("<i>R</i> = " + _frac("<i>R</i><sub>1</sub><i>R</i><sub>2</sub>",
                                      "<i>R</i><sub>1</sub> + <i>R</i><sub>2</sub>"), "32.62"))
    b.append(eq("<i>E</i><sub>2</sub> = nguồn điện áp mong muốn", "32.63"))
    b.append(eq("<i>R</i><sub>1</sub> = " + _frac("<i>R</i>", "<i>K</i>"), "32.64"))
    b.append(eq("<i>R</i><sub>2</sub> = " +
                _frac("<i>RR</i><sub>1</sub>", "<i>R</i><sub>1</sub> − <i>R</i>"), "32.65"))
    b.append(eq("<i>e</i><sub>02</sub> = (<i>E</i><sub>2</sub> − <i>E</i><sub>1</sub>) + "
                "<i>e</i><sub>01</sub>", "32.66"))
    b.append(p("Tài liệu [15] có các ví dụ thiết kế dùng những phương trình biến đổi này."))

    b.append(h4("Bộ điều khiển nhiệt độ", "Temperature Controllers"))
    b.append(p(
        "Các bộ điều khiển nhiệt độ dùng nhiệt điện trở thường dùng mạch phân áp và mạch cầu. Dùng "
        "nhiệt điện trở trong một mạch như vậy cho độ nhạy cao hơn nhiều so với cặp nhiệt điện hoặc "
        "RTD. Các cặp nhiệt điện chuẩn nhạy nhất có độ dốc điện áp ra 50 đến 55 µV °C⁻¹ trong dải "
        "0 °C đến 300 °C. Cầu phân áp dùng nhiệt điện trở thường có độ dốc đầu ra khoảng 8 đến "
        "10 mV °C⁻¹ trên mỗi vôn đặt vào cầu. Vì đầu vào của một cầu phân áp nhiệt điện trở thường "
        "nằm trong khoảng 1 đến 5 V, nhiệt điện trở cho độ nhạy lớn hơn cặp nhiệt điện khoảng 200 "
        "đến 1000 lần. Hệ số nhiệt độ của điện trở của nhiệt điện trở lớn hơn của RTD khoảng 10 "
        "lần. Tuy nhiên, dải nhiệt độ quanh điểm điều khiển của một bộ điều khiển nhiệt điện trở "
        "nhỏ so với dải mà cặp nhiệt điện hoặc RTD có được."))
    b.append(p(
        "Tài liệu [1] có một số bộ điều khiển nhiệt độ nhiệt điện trở giá rẻ điển hình. Có những "
        "bộ điều khiển nhiệt độ nhiệt điện trở của Hart Scientific, Inc. cho độ ổn định điều khiển "
        "tốt hơn 0,001 °C [16]."))

    b.append(h4("Mạng điện trở tuyến tính", "Linear Resistance Networks"))
    b.append(p(
        "Một kỹ thuật phổ biến khi thiết kế mạch nhiệt kế là đặt một nguồn dòng không đổi vào một "
        "mạng điện trở tuyến tính. Kết quả là một điện áp trên mạng tuyến tính theo nhiệt độ. Bù "
        "nhiệt cho những thay đổi điện trở xảy ra trong cuộn dây, dụng cụ, rơ le, động cơ và máy "
        "phát cũng dùng những mạng như vậy. Ví dụ, một cuộn dây đồng có hệ số nhiệt độ của điện trở "
        "dương khoảng 0,39% °C⁻¹. Mạng nhiệt điện trở có hệ số nhiệt độ âm. Bộ bù được thiết kế để "
        "cho độ dốc có cùng độ lớn nhưng ngược dấu với độ dốc của cuộn đồng. Vì vậy, độ dốc Ω theo "
        "°C của bộ bù bằng mức thay đổi Ω/°C của cuộn dây. Kết quả là dòng điện qua cuộn dây không "
        "phụ thuộc nhiệt độ. Các ứng dụng khác gồm bù trôi trong cảm biến biến dạng silic, máy dò "
        "hồng ngoại, và các mạch chứa cả linh kiện thụ động lẫn tích cực."))
    b.append(p("Với mạng điện trở tuyến tính cơ bản ở Hình 32.21a:"))
    b.append(eq("<i>R</i><sub>12</sub> = <i>R</i><sub>C</sub> = " +
                _frac("<i>RR</i><sub>T</sub>", "<i>R</i> + <i>R</i><sub>T</sub>") +
                " = <i>R</i>(1 − " + _frac("1", "1 + <i>R</i><sub>T</sub>/<i>R</i>") + ")", "32.67"))
    b.append(p(
        "Chuẩn hóa theo <i>R</i> và thay <i>r</i><sub>T</sub> = <i>R</i><sub>T</sub>/"
        "<i>R</i><sub>T0</sub> cùng <i>R</i><sub>T0</sub>/<i>R</i> = σ vào Phương trình 32.67 ta "
        "được:"))
    b.append(eq("<i>R</i><sub>n</sub> = " +
                _frac("<i>R</i><sub>C</sub>", "<i>R</i>") + " = 1 − " +
                _frac("1", "1 + <i>r</i><sub>T</sub>σ") + " = 1 − <i>F</i>(<i>T</i>)", "32.68"))
    b.append(p(
        "Do đó, những kỹ thuật dùng để tối ưu độ tuyến tính của cầu phân áp cũng áp dụng được cho "
        "mạng điện trở tuyến tính. Dùng điện trở nối tiếp <i>R</i><sub>1</sub> ở Hình 32.21b sẽ "
        "dịch đường cong lên một mức điện trở cao hơn và không ảnh hưởng đến đầu ra Ω/°C."))
    b.append(fig(21, F.fig(21), "vi"))
    b.append(p(
        "Thường thì việc thiết kế một bộ bù cho đầu ra Ω/°C mong muốn dẫn đến một nhiệt điện trở có "
        "giá trị <i>R</i><sub>T0</sub> không chuẩn. Mạch biến đổi ở Hình 32.21c cho phép dùng một "
        "giá trị <i>R</i><sub>T0</sub> chuẩn. Các phương trình biến đổi như sau:"))
    b.append(eq("<i>K</i><sub>1</sub> = " +
                _sq(_frac("<i>R</i>′<sub>T0</sub>", "<i>R</i><sub>T0</sub>")), "32.69"))
    b.append(eq("<i>R</i><sub>E</sub> = <i>R</i><sub>1</sub> − <i>R</i>(<i>K</i><sub>1</sub> − 1)",
                "32.70"))
    b.append(eq("<i>R</i><sub>A</sub> = <i>RK</i><sub>1</sub>(<i>K</i><sub>1</sub> − 1)", "32.71"))
    b.append(eq("<i>R</i><sub>B</sub> = <i>RK</i><sub>1</sub>", "32.72"))
    b.append(p(
        "trong đó <i>R</i><sub>T0</sub> là giá trị không chuẩn và <i>R</i>′<sub>T0</sub> là giá trị "
        "chuẩn. Yêu cầu là cả hai nhiệt điện trở phải có cùng đặc tính tỉ số điện trở – nhiệt độ. "
        "Đặt <i>R</i><sub>1</sub> = <i>R</i>(<i>K</i><sub>1</sub> − 1) ở Hình 32.21b cho "
        "<i>R</i><sub>E</sub> = 0 ở Hình 32.21c. Do đó, việc chuyển từ Hình 32.21a sang Hình 32.21c "
        "đòi hỏi dùng điện trở chèn tối thiểu <i>R</i><sub>1</sub> = <i>R</i>(<i>K</i><sub>1</sub> "
        "− 1)."))
    b.append(p(
        "Mạng này cho độ tuyến tính tốt với những dải nhiệt độ nhỏ 10 °C đến 30 °C. Tuy nhiên, sai "
        "số tăng nhanh từ khoảng 0,15 °C với dải 30 °C lên 0,7 °C với dải 50 °C (0 °C đến 50 °C). "
        "Dùng mạng hai nhiệt điện trở ở Hình 32.22 cho sai số tuyến tính cực đại 0,22 °C trên dải "
        "0 °C đến 100 °C, còn mạng ba nhiệt điện trở cũng ở hình đó giảm sai số xuống 0,04 °C trên "
        "cùng dải 0 °C đến 100 °C [5]. Các mạng ở Hình 32.22 là cầu phân áp tuyến tính. Mắc điện "
        "trở <i>R</i><sub>1</sub> qua hai cực ra 3–4 sẽ biến các mạng này thành mạng điện trở tuyến "
        "tính. Nhiều nhà sản xuất bán một nhiệt điện trở kép ba dây lắp lẫn được, phù hợp cho mạch "
        "hai nhiệt điện trở ở Hình 32.22."))
    b.append(fig(22, F.fig(22), "vi"))
    b.append(p(
        "Nhiệt điện trở lắp lẫn được và các kỹ thuật tuyến tính hóa mô tả ở trên đã có từ nhiều "
        "năm. Ngoài ra, độ ổn định của nhiệt điện trở NTC tốt hơn của cặp nhiệt điện và thường tốt "
        "hơn hoặc bằng của RTD thương mại [17]. Tuy vậy, đặc tính điện trở – nhiệt độ phi tuyến của "
        "nhiệt điện trở vẫn tiếp tục hạn chế việc dùng chúng trong đo và điều khiển nhiệt độ công "
        "nghiệp. Sự sẵn có của các bộ vi xử lý giá rẻ đã loại bỏ hạn chế này. Những linh kiện đó có "
        "thể dùng các hằng số của Phương trình 32.38 hoặc 32.39 để tính và hiển thị nhiệt độ trực "
        "tiếp. Chúng cũng có thể được dùng để tính bảng tra, cho độ không đảm bảo đo khi nội suy "
        "trong khoảng 0,001 °C đến 0,01 °C. Có những dụng cụ mô tả trong tài liệu dùng các chip vi "
        "xử lý như vậy [18, 19]. Thermometrics, Inc. bán một dụng cụ thương mại đọc các hằng số "
        "phương trình từ một chip trong đầu nối của từng đầu dò cung cấp kèm dụng cụ [1]. Việc dùng "
        "nhiệt điện trở cho ứng dụng công nghiệp sẽ tiếp tục tăng khi giá chip vi xử lý tiếp tục "
        "giảm."))

    b.append(_refs323("vi"))
    return "".join(b)


def sec_32_3_en():
    b = [h2("32.3 Thermistor Thermometers", "Nhiệt kế nhiệt điện trở")]
    b.append(authors("Meyer Sapoff", ""))

    b.append(p(
        "A thermistor is a thermally sensitive resistor whose primary function is to exhibit a "
        "change in electric resistance with a change in body temperature. Unlike a wirewound or "
        "metal film resistance temperature detector (RTD), a thermistor is a ceramic "
        "semiconductor. An RTD exhibits a comparatively low temperature coefficient of resistance "
        "on the order of 0.4 to 0.5% °C⁻¹. Depending on the type of material system used, a "
        "thermistor can have either a large positive temperature coefficient of resistance (PTC "
        "device) or a large negative temperature coefficient of resistance (NTC device)."))
    b.append(p(
        "Two types of PTC thermistors are available. Silicon PTC thermistors rely on the bulk "
        "properties of doped silicon and exhibit resistance–temperature characteristics that are "
        "approximately linear. They have temperature coefficients of resistance of about 0.7 to "
        "0.8% °C⁻¹. The most common application of silicon PTC thermistors is compensation of "
        "silicon semiconductor devices and circuits [1]. The materials used for switching-type PTC "
        "thermistors are compounds of barium, lead, and strontium titanates. Figure 32.16 shows the "
        "resistance–temperature characteristic of a typical switching-type PTC thermistor [2]. At "
        "low temperatures, from below 0 °C to <i>R</i><sub>min</sub>, the resistance value is low, "
        "and <i>R</i><sub>T</sub> vs. <i>T</i> exhibits a small negative temperature coefficient of "
        "resistance on the order of −1% °C⁻¹. As the temperature increases, the temperature "
        "coefficient of resistance becomes positive and the resistance begins to rise. At a "
        "threshold or switching temperature, the rate of rise becomes very rapid and the PTC "
        "characteristic becomes very steep. Within its switching range, the temperature coefficient "
        "of resistance can be as high as 100% °C⁻¹ and the device exhibits a high resistance value. "
        "At temperatures above the switching range, the resistance reaches a maximum value beyond "
        "which the temperature coefficient becomes negative again. The switching temperature can be "
        "varied between 80 °C and 240 °C by altering the chemical composition of the ceramic. "
        "Typical applications for switching-type PTC thermistors are over-temperature protection, "
        "current limiting, and self-regulated heating. The temperature coefficient of resistance of "
        "a unit used as a heating element typically is about 25% °C⁻¹ at a switching temperature of "
        "240 °C [1, 2]."))
    b.append(fig(16, F.fig(16), "en"))
    b.append(p(
        "NTC thermistors consist of metal oxides such as the oxides of chromium, cobalt, copper, "
        "iron, manganese, nickel, and titanium. Such units exhibit a monotonic decrease in electric "
        "resistance with an increase in temperature. The resistance–temperature characteristics of "
        "NTC thermistors are nonlinear and approximate the characteristics exhibited by intrinsic "
        "semiconductors for which the temperature dependence of resistance is due to the excitation "
        "of carriers across a single energy gap. As such, the logarithm of resistance of an NTC "
        "thermistor is approximately a linear function of its inverse absolute temperature. Below "
        "room temperature, the slope of the function decreases and the thermistor behaves more like "
        "an extrinsic semiconductor. The actual conduction mechanism is comparable to the “hopping” "
        "mechanism observed in ferrites and manganites that have a spinel crystal structure. "
        "Conduction occurs when charge carriers hop from one ionic site in the spinel lattice to an "
        "adjacent site. Such hopping can occur when ions of the same element, with valences "
        "differing by 1, are present on equivalent lattice sites."))
    b.append(p(
        "Because of its nonlinear resistance–temperature characteristic, the temperature "
        "coefficient of resistance of an NTC thermistor changes with temperature. Depending on the "
        "material system used, the temperature coefficient at 25 °C typically is in the range of −3 "
        "to −5% °C⁻¹. At −60 °C, it is in the range of −6.4 to −11.3% °C⁻¹; and at 100 °C, it "
        "varies between −2.1 and −3.7% °C⁻¹. The corresponding resistance ratios with respect to "
        "25 °C, <i>R</i><sub>T</sub>/<i>R</i><sub>25</sub>, are 41 to 228 at −60 °C and 0.13 to "
        "0.03 at 100 °C. The slope of the log <i>R</i> vs. 1/<i>T</i> characteristic β is "
        "relatively constant. The material systems for which the above data are presented exhibit "
        "β values of 2930 to 5135 K over the range of 25 to 125 °C [1]."))
    b.append(p(
        "Although the resistance–temperature characteristic of an NTC thermistor is nonlinear, it "
        "is possible to achieve good linearity of the conductance–temperature and "
        "resistance–temperature characteristics using thermistor–resistor networks. The use of a "
        "resistor in series with a thermistor results in a linear conductance network, such as a "
        "voltage divider. The current obtained in response to a voltage applied to the network is "
        "linear with temperature. Consequently, the output of the voltage divider (voltage across "
        "the resistor) is linear with temperature. The parallel combination of a resistor and "
        "thermistor is a linear resistance network. Techniques exist for optimizing the linearity "
        "of single thermistor networks [3, 4]."))
    b.append(p(
        "Such networks exhibit S-shaped curves for their voltage–temperature or "
        "resistance–temperature characteristics. For temperature spans of 20 °C to 30 °C, the "
        "maximum deviation is small between any point on the curve and the best straight-line "
        "approximation of the curve. As the span increases beyond 30 °C, the maximum deviation from "
        "linearity increases rapidly from about 0.15 °C for a 30 °C span to 0.7 °C for a 50 °C "
        "span. Using a two-thermistor network, a maximum linearity deviation of 0.22 °C can be "
        "obtained over a range of 0 °C to 100 °C, as compared with a 2 °C deviation obtained with a "
        "single-thermistor network [5]. Applications for NTC thermistors include temperature "
        "measurement, control, and compensation."))
    b.append(p(
        "When current flows through a thermistor, there is a self-heating effect caused by the "
        "power dissipated in it. The thermistor temperature rises until the rate of heat loss from "
        "the thermistor to its surrounding environment equals the power dissipated. For this "
        "condition of thermal equilibrium, the temperature rise is directly proportional to the "
        "power dissipated in the thermistor. The constant of proportionality δ is the dissipation "
        "constant of the thermistor. By definition, δ is the ratio — at a specified ambient "
        "temperature, mounting condition, and environment — of the change in power dissipation in a "
        "thermistor to the resultant body temperature change. Factors that affect the dissipation "
        "constant are the thermistor surface area, the thermal conductivity and relative rate of "
        "motion of the medium surrounding the thermistor, the heat loss due to free convection in a "
        "still medium, the heat transfer between the thermistor and its mount through the thermistor "
        "lead wires, and heat loss due to radiation (significant for gases at low pressure). Because "
        "the thermal conductivities of fluids vary with temperature and free convection depends on "
        "the temperature difference between the thermistor and its ambient, δ is not a true "
        "constant. For gases in particular, the dissipation constant varies both with the "
        "thermistor body temperature and the amount of self-heating."))
    b.append(p(
        "The thermal time constant τ is the 63.2% response to a step-function change in the "
        "thermistor temperature when the power dissipated in the thermistor is negligible. The "
        "thermal time constant only has meaning when there is a single exponential response. In "
        "such a case, an elapsed time of τ results in a 63.2% change between the initial and final "
        "steady-state temperatures, while an elapsed time of 5τ results in a 99.3% change. For a "
        "more complex structure, such as a thermistor encapsulated in a sensor housing, multiple "
        "exponentials can exist and one cannot predict that the 99% response will occur after an "
        "interval of five time constants. As with the dissipation constant, the thermal time "
        "constant is dependent on the rate of heat transfer between the thermistor and its "
        "environment. Consequently, all of the factors that increase the dissipation constant "
        "decrease the time constant."))
    b.append(p(
        "The most common types of silicon PTC devices are the glass diode package having diameters "
        "of 1.8 mm to 2.5 mm and lengths of 3.8 mm to 7.5 mm, and the molded epoxy package with "
        "diameters of 3.6 mm to 6.0 mm and lengths of 10.4 mm to 15.0 mm. Such units have axial "
        "leads. Epoxy-coated chips and disks with radial leads also are available, with diameters of "
        "approximately 3 mm. Silicon PTC thermistors that comply with MIL-T-23648 have an operating "
        "temperature range of −55 °C to 125 °C. Commercial versions can be obtained with a range of "
        "−65 °C to 150 °C [6]."))
    b.append(p(
        "The most common configuration for switching-type PTC thermistors is the radial lead disk, "
        "with and without an insulating coating. Such units are available in diameters of 4 mm to "
        "26 mm. The thickness dimension is in the range between 0.5 mm to 6.5 mm. They also are "
        "available as surface-mount devices, disks without leads, and in glass diode packages. "
        "Switching-type PTC disks have a storage temperature range of −25 °C to 155 °C and an "
        "operating range of 0 °C to 55 °C [1]."))
    b.append(p(
        "The emphasis of this text will be on NTC thermistors. Most thermistor applications use "
        "such devices. Two major categories of NTC thermistors exist. Bead-type thermistors have "
        "platinum alloy lead wires sintered into the body of the ceramic. Chip, disk, surface-mount, "
        "flake, and rod-type thermistors have metallized surface electrodes. The latter category "
        "includes glass diode packages in which dumet leads are compression-bonded to disks or "
        "chips."))
    b.append(p(
        "Glass-coated beads include both adjacent and opposite lead configurations with diameters "
        "of 0.125 mm to 1.5 mm. Glass probes with diameters of 0.4 mm to 2.5 mm have lengths ranging "
        "from 1.5 mm to 6.35 mm. Probes with diameters of 1.5 mm to 2.5 mm have lengths of 3 mm to "
        "12.7 mm, while larger probes with diameters of 2 mm to 2.5 mm have lengths of up to 50 mm. "
        "Glass rods typically are 6.3 mm long with diameters of 1.5 mm to 2.5 mm. A glass probe "
        "consists of a bare-bead-type thermistor sealed at the tip of a solid glass rod and radial "
        "dumet leads. A glass rod, by comparison, has its bead sealed in the center of a solid glass "
        "rod and has axial dumet leads. The temperature range specified in MIL-T-23648 is −55 °C to "
        "200 °C for glass-coated beads and −55 °C to 275 °C for glass probes and glass rods. "
        "Commercial versions of such glass-enclosed devices typically have a range of −80 °C to "
        "300 °C. Some units are rated for intermittent operation at 600 °C, while special cryogenic "
        "devices are rated for operation in the range of −196 °C to 25 °C."))
    b.append(p(
        "Chip thermistors with radial leads are available with cross-sections of 0.25 mm × 0.25 mm "
        "to 13 mm × 13 mm and a thickness range of 0.175 mm to 1.5 mm. Disks having diameters of "
        "1 mm to 25 mm are available in both radial and axial lead configurations, with a thickness "
        "range of 0.25 mm to 6.35 mm. Chips and disks also are available in glass diode packages "
        "with axial dumet leads. Surface-mount chips are available in sizes ranging from 2 mm to "
        "3.2 mm long × 1.1 mm to 1.6 mm wide × 0.36 mm to 1.3 mm thick. Flake thermistors with both "
        "adjacent and opposite leads are available in a thickness range of 0.025 mm to 0.125 mm, "
        "with cross-sections of 0.5 mm × 0.5 mm to 3 mm × 3 mm. The temperature range specified for "
        "chips, disks, rods, and glass diode packages in MIL-T-23648 is −55 °C to 125 °C. Commercial "
        "chips and disks are available with an operating temperature range of −80 °C to 155 °C [1]. "
        "Rods are available for use over the range of −60 °C to 150 °C [7], and glass diode packages "
        "are available with an operating range of −60 °C to 300 °C [8]."))

    # ------------------------------------------------------------ thermal
    b.append(h3("Thermal Properties of NTC Thermistors", "Tính chất nhiệt của nhiệt điện trở NTC"))
    b.append(p(
        "The energy dissipated as heat in a thermistor connected to an electric circuit causes the "
        "thermistor body temperature to rise above the ambient temperature of its environment. At "
        "any instant, the applicable heat transfer equation is:"))
    b.append(eq(_frac("d<i>H</i>", "d<i>t</i>") +
                " = <i>P</i> = <i>E</i><sub>T</sub><i>I</i><sub>T</sub> = δ(<i>T</i> − "
                "<i>T</i><sub>a</sub>) + <i>cm</i> " + _frac("d<i>T</i>", "d<i>t</i>"), "32.26"))
    b.append(wl([
        "<i>dH</i>/<i>dt</i> = <i>P</i> = <i>E</i><sub>T</sub><i>I</i><sub>T</sub> = rate of "
        "thermal energy or heat supplied to the thermistor",
        "δ = dissipation constant",
        "<i>T</i><sub>a</sub> = ambient temperature",
        "δ(<i>T</i> − <i>T</i><sub>a</sub>) = rate of heat loss to the surrounding environment",
        "<i>c</i> and <i>m</i> = respectively, specific heat and mass of the thermistor",
        "<i>cm</i>(<i>dT</i>/<i>dt</i>) = rate of heat absorbed by the thermistor",
    ]))
    b.append(p("The solution of Equation 32.26 when <i>P</i> is constant is:"))
    b.append(eq("<i>T</i> = <i>T</i><sub>a</sub> + " + _frac("<i>P</i>", "δ") +
                "[1 − exp(−" + _frac("δ", "<i>cm</i>") + "<i>t</i>)]", "32.27"))
    b.append(p(
        "The transient solution of Equation 32.27 is the basis for the current–time characteristic "
        "of a thermistor. When <i>t</i> ≫ <i>cm</i>/δ, then <i>dT</i>/<i>dt</i> → 0, and the steady "
        "state solution of Equation 32.27 becomes:"))
    b.append(eq("<i>P</i> = <i>E</i><sub>T</sub><i>I</i><sub>T</sub> = δ(<i>T</i> − "
                "<i>T</i><sub>a</sub>)", "32.28"))
    b.append(p(
        "where <i>E</i><sub>T</sub> and <i>I</i><sub>T</sub> are the steady-state thermistor "
        "voltage and current, respectively. Equation 32.28 is the basis for the voltage–current "
        "characteristic of a thermistor."))
    b.append(p(
        "By reducing the thermistor power to a value that results in negligible self-heating, "
        "<i>P</i> → 0, Equation 32.26 becomes:"))
    b.append(eq(_frac("d<i>T</i>", "d<i>t</i>") + " = −" + _frac("δ", "<i>cm</i>") +
                "(<i>T</i> − <i>T</i><sub>a</sub>)", "32.29"))
    b.append(p(
        "Equation 32.29 is a mathematical statement of Newton’s law of cooling and has the "
        "solution:"))
    b.append(eq("<i>T</i> = <i>T</i><sub>a</sub> + (<i>T</i><sub>i</sub> − <i>T</i><sub>a</sub>) "
                "exp(−<i>t</i>/τ)"))
    b.append(wl([
        "<i>T</i><sub>i</sub> = initial thermistor body temperature",
        "<i>T</i><sub>a</sub> = ambient temperature",
        "τ = <i>cm</i>/δ = thermal time constant",
    ]))
    b.append(p(
        "Table 32.8 gives dissipation and time constant data for glass-coated beads, glass probes, "
        "and glass rods. Table 32.9 lists similar data for chip, disk, and rod-type thermistors with "
        "metallized surface contacts. Data for the dissipation and time constants are for the "
        "thermistor suspended by its leads at 25 °C using the procedure specified in MIL-T-23648A. "
        "The temperature increment used for computing the dissipation constant results from "
        "self-heating the thermistors to 75 °C from an ambient of 25 °C. The time constant data "
        "result from allowing the thermistors to cool from 75 °C to an ambient of 25 °C. The "
        "water-plunge time constant data result from rapidly immersing the thermistors from room "
        "temperature air into still water. The transit time was negligible. The air temperature was "
        "approximately 25 °C and the water temperature was about 5 °C. The diameters specified for "
        "epoxy-coated interchangeable units are maximum diameters. To illustrate the effect of the "
        "environment on the thermal properties of these units, the dissipation and time constants "
        "are 8 mW °C⁻¹ and 1 s, respectively, when tested in stirred oil, as compared with "
        "1 mW °C⁻¹ and 10 s, respectively, when tested in still air. The dissipation and time "
        "constants for disks depend on the disk thickness, lead wire diameter, quantity of solder "
        "used for lead attachment, distance between the thermistor body and its mount, and the "
        "thermistor material. The dissipation and time constants for rods depend on the rod length "
        "as well as the variables specified above for disks."))
    b.append(_t328("en"))
    b.append(_t329("en"))

    # ------------------------------------------------------------ electrical
    b.append(h3("Electrical Properties of NTC Thermistors",
                "Tính chất điện của nhiệt điện trở NTC"))
    b.append(p(
        "Thermistor applications depend on three fundamental electrical characteristics. These are "
        "the voltage–current characteristic, the current–time characteristic, and the "
        "resistance–temperature characteristic."))

    b.append(h4("Voltage–Current Characteristics", "Đặc tính dòng – áp"))
    b.append(p(
        "Figure 32.17 shows a typical voltage–current curve. At low currents, the power dissipated "
        "is small compared with the dissipation constant and the self-heating effect is negligible. "
        "Under these conditions, the resistance is constant, independent of the current, and the "
        "voltage is proportional to the current. Consequently, at low currents, the characteristic "
        "curve is tangent to a constant resistance line equal to the zero-power resistance of the "
        "thermistor. As the current increases, the effects of self-heating become more evident; the "
        "thermistor temperature rises, and its resistance begins to decrease. For each subsequent "
        "incremental increase in current, there is a corresponding decrease in resistance. Hence, "
        "the slope of the voltage–current characteristic decreases with increasing current. This "
        "continues until the current reaches a value at which the slope becomes zero. Beyond this "
        "point, at which the voltage exhibits its maximum value, the slope continues to decrease and "
        "the thermistor exhibits a negative resistance characteristic. The temperature, voltage, and "
        "current corresponding to the peak of the curve are:"))
    b.append(eq("<i>T</i><sub>p</sub> = " +
                _frac("β − " + _sq("β<sup>2</sup> − 4β<i>T</i><sub>a</sub>"), "2"), "32.30"))
    b.append(eq("<i>E</i><sub>p</sub> = " +
                _sq("<i>R</i><sub>p</sub> δ(<i>T</i><sub>p</sub> − <i>T</i><sub>a</sub>)"), "32.31"))
    b.append(eq("<i>I</i><sub>p</sub> = " +
                _sq(_frac("δ(<i>T</i><sub>p</sub> − <i>T</i><sub>a</sub>)",
                          "<i>R</i><sub>p</sub>")), "32.32"))
    b.append(wl([
        "<i>T</i><sub>p</sub> = absolute temperature (in K) at which the peak occurs",
        "<i>T</i><sub>a</sub> = absolute ambient temperature (in K)",
        "<i>R</i><sub>p</sub> = thermistor resistance at <i>T</i><sub>p</sub>",
    ]))
    b.append(p(
        "Applications based on the voltage–current characteristics involve changes in the "
        "operating point on a single curve or family of curves. Such changes result from changes in "
        "the environmental conditions or variations in circuit parameters. Figure 32.17 shows a "
        "graphical solution for obtaining the operating point. The curve represents a nonlinear "
        "relationship between the thermistor voltage and current. The Thevenin equivalent circuit "
        "with respect to the thermistor terminals provides the relationship given by Equation "
        "32.33."))
    b.append(eq("<i>E</i><sub>T</sub> = <i>E</i><sub>THEV</sub> − "
                "<i>I</i><sub>T</sub><i>R</i><sub>THEV</sub>", "32.33"))
    b.append(p(
        "where <i>E</i><sub>T</sub> and <i>I</i><sub>T</sub> are the thermistor voltage and "
        "current, respectively. The straight-line relationship of Equation 32.33 is the load line of "
        "the self-heated thermistor. Its intersection with the voltage–current characteristic is the "
        "operating point. Table 32.10 categorizes the more familiar applications into four groups "
        "distinguished by the form of thermistor excitation [1, 14]."))
    b.append(_t3210("en"))
    b.append(fig(17, F.fig(17), "en"))

    b.append(h4("Current–Time Characteristics", "Đặc tính dòng – thời gian"))
    b.append(p(
        "The voltage–current characteristic discussed above deals with a self-heated thermistor "
        "operated under steady-state conditions. This condition, for which a decrease in thermistor "
        "resistance results from a current sufficiently high to cause self-heating, does not occur "
        "instantaneously. A transient condition exists in a thermistor circuit from the time at "
        "which power is first applied (<i>t</i> = 0) until the time equilibrium occurs "
        "(<i>t</i> ≫ τ). The relationship between the thermistor current and the time required to "
        "reach thermal equilibrium is the current–time characteristic. Generally, the excitation is "
        "a step function in voltage through a Thevenin equivalent source. Figure 32.18 shows the "
        "current–time characteristics for several thermistor disks and voltage sources. For any "
        "given characteristic, the source voltage, source resistance, and thermistor zero-power "
        "resistance determine the initial current. The source voltage, source resistance, and "
        "voltage–current characteristic determine the final equilibrium value. The curve between the "
        "initial and final values depends on the circuit design parameters, as well as the "
        "dissipation constant and heat capacity of the thermistor. The proper choice of thermistor "
        "and circuit design results in a transient time range of a few milliseconds to several "
        "minutes."))
    b.append(fig(18, F.fig(18), "en"))
    b.append(p(
        "Applications based on the current–time characteristic are time delay, surge suppression, "
        "filament protection, overload protection, and sequential switching."))

    b.append(h4("Resistance–Temperature Characteristics", "Đặc tính điện trở – nhiệt độ"))
    b.append(p(
        "The term zero-power resistance applies to thermistors operated with negligible "
        "self-heating. This characteristic describes the relationship between the zero-power "
        "resistance of a thermistor and its ambient temperature. Over small temperature spans, the "
        "approximately linear relationship between the logarithm of resistance and inverse absolute "
        "temperature is given by:"))
    b.append(eq("ln <i>R</i><sub>T</sub> ≡ <i>A</i> + " + _frac("β", "<i>T</i>"), "32.34"))
    b.append(wl([
        "<i>T</i> = absolute temperature (K)",
        "β = material constant of the thermistor",
    ]))
    b.append(p(
        "If one lets <i>R</i><sub>T</sub> = <i>R</i><sub>T0</sub> at a reference temperature "
        "<i>T</i> = <i>T</i><sub>0</sub> and solves for <i>R</i><sub>T</sub>, one obtains:"))
    b.append(eq("<i>R</i><sub>T</sub> ≅ <i>R</i><sub>T0</sub> exp[ " +
                _frac("β(<i>T</i><sub>0</sub> − <i>T</i>)", "<i>TT</i><sub>0</sub>") + " ]", "32.35"))
    b.append(p("The temperature coefficient of resistance α is defined as:"))
    b.append(eq("α ≡ " + _frac("1", "<i>R</i><sub>T</sub>") + " " +
                _frac("d<i>R</i><sub>T</sub>", "d<i>T</i>"), "32.36"))
    b.append(p("Solving Equation 32.34 for α yields:"))
    b.append(eq("α = − " + _frac("β", "<i>T</i><sup>2</sup>"), "32.37"))
    b.append(p(
        "In Equation 32.34, the deviation from linearity results in temperature errors of 0.01 °C, "
        "0.1 °C, and 0.3 °C for temperature spans of 10 °C, 30 °C, and 50 °C, respectively, within "
        "the range of 0 °C to 50 °C. Using a polynomial for ln <i>R</i><sub>T</sub> vs. "
        "1/<i>T</i> reduces the error considerably. The degree of the polynomial required depends on "
        "the temperature range and material system used. The use of a third-degree polynomial is "
        "adequate for most applications. Hence, more accurate expressions for the "
        "resistance–temperature characteristic are:"))
    b.append(eq("ln <i>R</i><sub>T</sub> = <i>A</i><sub>0</sub> + " +
                _frac("<i>A</i><sub>1</sub>", "<i>T</i>") + " + " +
                _frac("<i>A</i><sub>2</sub>", "<i>T</i><sup>2</sup>") + " + " +
                _frac("<i>A</i><sub>3</sub>", "<i>T</i><sup>3</sup>"), "32.38a"))
    b.append(eq("ln <i>R</i><sub>T</sub> = <i>A</i><sub>0</sub> + " +
                _frac("<i>A</i><sub>1</sub>", "<i>T</i>") + " + " +
                _frac("<i>A</i><sub>2</sub>", "<i>T</i><sup>2</sup>") + " + " +
                _frac("<i>A</i><sub>3</sub>", "<i>T</i><sup>3</sup>"), "32.38b"))
    b.append(note(
        "Equations 32.38a and 32.38b are printed identically in the source. The translation keeps "
        "them as printed rather than silently correcting one, so the reader can check against the "
        "book."))
    b.append(eq(_frac("1", "<i>T</i>") + " = α<sub>0</sub> + α<sub>1</sub> ln " +
                "<i>R</i><sub>T</sub> + α<sub>2</sub>(ln <i>R</i><sub>T</sub>)<sup>2</sup> + "
                "α<sub>3</sub>(ln <i>R</i><sub>T</sub>)<sup>3</sup>", "32.39"))
    b.append(p(
        "Steinhart and Hart proposed the use of Equation 32.39 for the oceanographic range of "
        "−2 °C to 30 °C [11]. Their analysis showed that no significant loss in accuracy occurred by "
        "eliminating the square term α<sub>2</sub>(ln <i>R</i><sub>T</sub>)<sup>2</sup>. "
        "Consequently, they proposed the use of Equation 32.40."))
    b.append(eq(_frac("1", "<i>T</i>") + " = <i>b</i><sub>0</sub> + <i>b</i><sub>1</sub> ln " +
                "<i>R</i><sub>T</sub> + <i>b</i><sub>3</sub>(ln <i>R</i><sub>T</sub>)"
                "<sup>3</sup>", "32.40"))
    b.append(p(
        "Mangum reported that the use of Equation 32.40 resulted in interpolation errors of "
        "approximately 0.001 °C over the range of 0 °C to 70 °C [12]."))
    b.append(p(
        "The technical staff at Thermometrics, Inc. evaluated Equation 32.38 over the range of "
        "−80 °C to 260 °C using 17 different thermistor materials. The glass probes investigated "
        "encompassed a span of specific resistance values of 2 Ω cm to 300 kΩ cm and a resistance "
        "range at 25 °C of 10 Ω to 2 MΩ. The results were presented at the Sixth International "
        "Symposium on Temperature and show that the interpolation errors do not exceed the total "
        "measurement uncertainties. For temperature spans of 100 °C within the range of −80 °C to "
        "260 °C, 150 °C within the range of −60 °C to 260 °C, and 150 °C to 200 °C within the range "
        "of 0 °C to 260 °C, the interpolation errors are 0.005 °C to 0.01 °C [13]. Lowering the "
        "temperature span to 50 °C within the range of 0 °C to 260 °C reduces the interpolation "
        "error to 0.001 °C to 0.003 °C."))
    b.append(p(
        "Sapoff and Siwek [14] evaluated the loss in accuracy introduced by eliminating the "
        "quadratic term in Equation 32.38. For this condition, Equation 32.38 reduces to Equation "
        "32.41."))
    b.append(eq("ln <i>R</i><sub>T</sub> = <i>C</i><sub>0</sub> + " +
                _frac("<i>C</i><sub>1</sub>", "<i>T</i>") + " + " +
                _frac("<i>C</i><sub>3</sub>", "<i>T</i><sup>3</sup>"), "32.41"))
    b.append(p(
        "The interpolation errors introduced by Equations 32.40 and 32.41 depend on the material "
        "system, temperature range (nonlinearity increases at low temperatures), and the "
        "temperature span considered. Table 32.11 summarizes the errors associated with the use of "
        "Equation 32.41 for various temperature spans and ranges."))
    b.append(_t3211("en"))
    b.append(p("Equations 32.38 through 32.41 can be rewritten as:"))
    b.append(eq("<i>R</i><sub>T</sub> = exp( <i>A</i><sub>0</sub> + " +
                _frac("<i>A</i><sub>1</sub>", "<i>T</i>") + " + " +
                _frac("<i>A</i><sub>2</sub>", "<i>T</i><sup>2</sup>") + " + " +
                _frac("<i>A</i><sub>3</sub>", "<i>T</i><sup>3</sup>") + " )", "32.42"))
    b.append(eq("<i>T</i> = [ <i>a</i><sub>0</sub> + <i>a</i><sub>1</sub> ln "
                "<i>R</i><sub>T</sub> + <i>a</i><sub>2</sub>(ln <i>R</i><sub>T</sub>)"
                "<sup>2</sup> + <i>a</i><sub>3</sub>(ln <i>R</i><sub>T</sub>)<sup>3</sup> ]"
                "<sup>−1</sup>", "32.43"))
    b.append(eq("<i>T</i> = [ <i>b</i><sub>0</sub> + <i>b</i><sub>1</sub> ln "
                "<i>R</i><sub>T</sub> + <i>b</i><sub>3</sub>(ln <i>R</i><sub>T</sub>)"
                "<sup>3</sup> ]<sup>−1</sup>", "32.44"))
    b.append(eq("<i>R</i><sub>T</sub> = exp( <i>C</i><sub>0</sub> + " +
                _frac("<i>C</i><sub>1</sub>", "<i>T</i>") + " + " +
                _frac("<i>C</i><sub>3</sub>", "<i>T</i><sup>3</sup>") + " )", "32.45"))
    b.append(p(
        "The solutions for Equations 32.38, 32.39, 32.42, and 32.43 require four calibration "
        "points and the use of simultaneous equations. Similarly, the solutions for Equations 32.40, "
        "32.41, 32.44, and 32.45 require three calibration points. The use of a polynomial "
        "regression analysis involving additional calibration points can minimize the effects of "
        "calibration uncertainties."))
    b.append(p(
        "Applications that depend on the resistance–temperature characteristic are temperature "
        "measurement, control, and compensation. There also are applications for which the "
        "thermistor temperature depends on some other physical phenomenon. For example, a hypsometer "
        "is an instrument in which the temperature of a boiling liquid provides an indication of "
        "the liquid vapor pressure. Another example involves the use of thermistor-type cardiac "
        "catheters for thermodilution analysis. A saline or dextrose solution of known volume and "
        "temperature is injected into the bloodstream through one of the catheter lumens. The mixing "
        "of the solution with the blood dilutes the solution and decreases the temperature of the "
        "blood as it flows downstream past a thermistor located at the surface of another lumen in "
        "the catheter. The cardiac output computed from the temperature–time response data measured "
        "by the thermistor provides an indication of the heart pump efficiency."))

    # ------------------------------------------------------------ linearization
    b.append(h3("Linearization and Signal Conditioning Techniques",
                "Kỹ thuật tuyến tính hóa và điều chế tín hiệu"))
    b.append(p(
        "The measured resistance and computed constants for Equations 32.43 and 32.44 can be used "
        "with a computer to determine temperature without the need for a linear network. This is "
        "useful for obtaining high accuracy over relatively wide temperature ranges. Most "
        "applications based on the resistance–temperature characteristics of thermistors, however, "
        "use some form of linearization or signal conditioning. The use of a constant current source "
        "and a linear resistance network provides a voltage output that is linear with temperature. "
        "By using the proper combination of current and resistance level, a digital voltmeter "
        "connected across the network provides a direct display of temperature. The use of a "
        "constant voltage source results in a linear conductance network with a current that is "
        "linear with temperature."))

    b.append(h4("Linear Conductance Networks", "Mạng dẫn tuyến tính"))
    b.append(p(
        "Voltage dividers, ohmmeter circuits and Wheatstone bridge circuits are linear conductance "
        "networks. Consider the voltage divider circuit shown in Figure 32.19. Using the fixed "
        "resistor for the output eliminates the effect of the load resistance. For the purpose of "
        "analysis, the resistor denoted by <i>R</i> is the parallel combination of the load and "
        "fixed divider resistors. Another advantage is that the output voltage increases with "
        "temperature with this arrangement. The ratio of output voltage to input voltage is given "
        "by:"))
    b.append(eq(_frac("<i>e</i><sub>0</sub>", "<i>e</i><sub>s</sub>") + " = " +
                _frac("<i>R</i>", "<i>R</i> + <i>R</i><sub>T</sub>") + " = " +
                _frac("1", "1 + <i>R</i><sub>T</sub>/<i>R</i>"), "32.46"))
    b.append(wl([
        "<i>e</i><sub>0</sub> = output voltage",
        "<i>e</i><sub>s</sub> = source voltage",
        "<i>R</i> = parallel combination of the load and fixed resistors",
        "<i>R</i><sub>T</sub> = thermistor resistance at a specified temperature <i>T</i>",
    ]))
    b.append(fig(19, F.fig(19), "en"))
    b.append(p(
        "If one normalizes the thermistor resistance with respect to its value at a specified "
        "reference temperature <i>T</i><sub>0</sub>, then:"))
    b.append(eq("<i>r</i><sub>T</sub> = " + _frac("<i>R</i><sub>T</sub>",
                                                 "<i>R</i><sub>T0</sub>"), "32.47"))
    b.append(wl([
        "<i>R</i><sub>T0</sub> = thermistor resistance at <i>T</i><sub>0</sub>",
        "<i>r</i><sub>T</sub> = resistance ratio",
    ]))
    b.append(p(
        "Thermistor manufacturers typically supply resistance ratio–temperature characteristics in "
        "their catalogs. Substituting Equation 32.47 in Equation 32.46 yields:"))
    b.append(eq(_frac("<i>e</i><sub>0</sub>", "<i>e</i><sub>s</sub>") + " = " +
                _frac("1", "1 + <i>r</i><sub>T</sub><i>R</i><sub>T0</sub>/<i>R</i>"), "32.48"))
    b.append(p(
        "If the circuit constant σ = <i>R</i><sub>T0</sub>/<i>R</i>, then Equation 32.48 becomes:"))
    b.append(eq("<i>F</i>(<i>T</i>) = " + _frac("<i>e</i><sub>0</sub>", "<i>e</i><sub>s</sub>") +
                " = " + _frac("1", "1 + <i>r</i><sub>T</sub>σ"), "32.49"))
    b.append(p(
        "The output for the voltage divider of Figure 32.19a is the S-shaped curve shown in Figure "
        "32.19b. The value of the circuit constant σ determines the temperature range for which "
        "good linearity exists between <i>e</i><sub>0</sub> and <i>T</i>. References [3, 4] include "
        "families of S-shaped curves over the range 0.01 ≤ σ ≤ 20.0 for the three basic material "
        "systems of MIL-T-23648. A good criterion for achieving optimum linearity is to equate the "
        "slopes of the function <i>F</i>(<i>T</i>) at the end-points of the specified temperature "
        "range <i>T</i><sub>L</sub> ≤ σ ≤ <i>T</i><sub>H</sub>. Specifying that "
        "<i>dF</i>(<i>T</i><sub>L</sub>)/<i>dT</i> = <i>dF</i>(<i>T</i><sub>H</sub>)/<i>dT</i> "
        "results in the following:"))
    b.append(eq("σ = " + _frac("<i>X</i> − <i>Y</i>",
                               "<i>Yr</i><sub>TL</sub> − <i>Xr</i><sub>TH</sub>"), "32.50"))
    b.append(p(
        "where <i>X</i> and <i>Y</i> are determined by the end-point conditions and the equation "
        "constants for ln <i>R</i><sub>T</sub> vs. <i>T</i>. When Equation 32.41 is used, <i>X</i> "
        "and <i>Y</i> are given by:"))
    b.append(eq("<i>X</i> = <i>T</i><sub>H</sub> " +
                _sq("<i>r</i><sub>TL</sub>(<i>C</i><sub>1</sub> + 3" +
                    _frac("<i>C</i><sub>3</sub>", "<i>T</i><sub>H</sub><sup>2</sup>") + ")"), "32.51"))
    b.append(eq("<i>Y</i> = <i>T</i><sub>L</sub> " +
                _sq("<i>r</i><sub>TH</sub>(<i>C</i><sub>1</sub> + 3" +
                    _frac("<i>C</i><sub>3</sub>", "<i>T</i><sub>L</sub><sup>2</sup>") + ")"), "32.52"))
    b.append(p("When Equation 32.38 is used, <i>X</i> and <i>Y</i> are given by:"))
    b.append(eq("<i>X</i> = <i>T</i><sub>H</sub> " +
                _sq("<i>r</i><sub>TL</sub>(<i>A</i><sub>1</sub> + 2" +
                    _frac("<i>A</i><sub>2</sub>", "<i>T</i><sub>L</sub>") + " + 3" +
                    _frac("<i>A</i><sub>3</sub>", "<i>T</i><sub>L</sub><sup>2</sup>") + ")"), "32.53"))
    b.append(eq("<i>Y</i> = <i>T</i><sub>L</sub> " +
                _sq("<i>r</i><sub>TH</sub>(<i>A</i><sub>1</sub> + 2" +
                    _frac("<i>A</i><sub>2</sub>", "<i>T</i><sub>H</sub>") + " + 3" +
                    _frac("<i>A</i><sub>3</sub>", "<i>T</i><sub>H</sub><sup>2</sup>") + ")"), "32.54"))
    b.append(p(
        "By allowing <i>e</i><sub>s</sub> and <i>R</i> to be the Thevenin equivalent voltage and "
        "resistance with respect to the thermistor terminals, respectively, the voltage divider "
        "analysis applies to any more complex circuit such as a Wheatstone bridge [3, 4]."))
    b.append(p(
        "Thermistor self-heating constraints typically result in nonstandard voltage sources for "
        "thermometer circuit designs. The modified divider circuits of Figure 32.20 provide "
        "equivalent circuits with standard voltage sources. Only a portion of the available output "
        "voltage appears across the output detector in Figure 32.20a. Ohmmeter-type thermometers use "
        "such circuits. The circuit of Figure 32.20a provides the full available output voltage. "
        "However, the conversion results in a bias voltage in series with the output. Bridge "
        "circuit-type thermometers use the circuit of Figure 32.20b. The conversion equations "
        "applicable to Figure 32.20a are:"))
    b.append(eq("<i>K</i> = " + _frac("<i>R</i><sub>1</sub>",
                                      "<i>R</i><sub>1</sub> + <i>R</i><sub>2</sub>") +
                " = " + _frac("<i>E</i><sub>1</sub>", "<i>E</i><sub>2</sub>") +
                " = " + _frac("<i>R</i><sub>4</sub>", "<i>R</i><sub>2</sub>"), "32.55"))
    b.append(fig(20, F.fig(20), "en"))
    b.append(eq("<i>R</i> = <i>R</i><sub>3</sub> + <i>R</i><sub>4</sub> = "
                "<i>R</i><sub>3</sub> + " +
                _frac("<i>R</i><sub>1</sub><i>R</i><sub>2</sub>",
                      "<i>R</i><sub>1</sub> + <i>R</i><sub>2</sub>"), "32.56"))
    b.append(eq("<i>E</i><sub>2</sub> = Desired source voltage", "32.57"))
    b.append(eq("<i>R</i><sub>2</sub> = " + _frac("<i>R</i><sub>4</sub>", "<i>K</i>"), "32.58"))
    b.append(eq("<i>R</i><sub>1</sub> = " +
                _frac("<i>R</i><sub>2</sub><i>R</i><sub>4</sub>",
                      "<i>R</i><sub>2</sub> − <i>R</i><sub>4</sub>"), "32.59"))
    b.append(eq(_big(_frac("<i>R</i><sub>3</sub>",
                            "<i>R</i><sub>3</sub> + <i>R</i><sub>4</sub>")) +
                " <i>F</i>(<i>T</i>)", "32.60"))
    b.append(p("The conversion equations applicable to Figure 32.20b are:"))
    b.append(eq("<i>K</i> = " + _frac("<i>R</i><sub>2</sub>",
                                      "<i>R</i><sub>1</sub> + <i>R</i><sub>2</sub>") +
                " = " + _frac("<i>E</i><sub>1</sub>", "<i>E</i><sub>2</sub>") +
                " = " + _frac("<i>R</i>", "<i>R</i><sub>1</sub>"), "32.61"))
    b.append(eq("<i>R</i> = " + _frac("<i>R</i><sub>1</sub><i>R</i><sub>2</sub>",
                                      "<i>R</i><sub>1</sub> + <i>R</i><sub>2</sub>"), "32.62"))
    b.append(eq("<i>E</i><sub>2</sub> = Desired source voltage", "32.63"))
    b.append(eq("<i>R</i><sub>1</sub> = " + _frac("<i>R</i>", "<i>K</i>"), "32.64"))
    b.append(eq("<i>R</i><sub>2</sub> = " +
                _frac("<i>RR</i><sub>1</sub>", "<i>R</i><sub>1</sub> − <i>R</i>"), "32.65"))
    b.append(eq("<i>e</i><sub>02</sub> = (<i>E</i><sub>2</sub> − <i>E</i><sub>1</sub>) + "
                "<i>e</i><sub>01</sub>", "32.66"))
    b.append(p("Reference [15] includes design examples that use these conversion equations."))

    b.append(h4("Temperature Controllers", "Bộ điều khiển nhiệt độ"))
    b.append(p(
        "Thermistor temperature controllers frequently use voltage divider and bridge circuits. "
        "The use of a thermistor in such a circuit results in much higher sensitivity than that "
        "obtainable with a thermocouple or RTD. The most sensitive standard thermocouples exhibit "
        "output voltage slopes of 50 to 55 µV °C⁻¹ in the range of 0 °C to 300 °C. Thermistor "
        "voltage dividers typically exhibit output slopes of about 8 to 10 mV °C⁻¹ per volt applied "
        "to the divider. Since the input to a thermistor voltage divider typically is in the range "
        "of 1 to 5 V, a thermistor provides about 200 to 1000 times the sensitivity of a "
        "thermocouple. The temperature coefficient of resistance of a thermistor is about 10 times "
        "that of an RTD. However, the temperature span about the control point of a thermistor "
        "controller is small compared with that available with a thermocouple or RTD."))
    b.append(p(
        "Reference [1] includes some typical low-cost thermistor temperature controllers. Thermistor "
        "temperature controllers are available from Hart Scientific, Inc. that provide control "
        "stabilities of better than 0.001 °C [16]."))

    b.append(h4("Linear Resistance Networks", "Mạng điện trở tuyến tính"))
    b.append(p(
        "A common technique for designing a thermometer circuit is to apply a constant-current "
        "source to a linear resistance network. This results in a voltage across the network that is "
        "linear with temperature. Temperature compensation for resistance changes that occur in coil "
        "windings, instruments, relays, motors, and generators also use such networks. For example, "
        "a copper coil has a positive temperature coefficient of resistance of approximately "
        "0.39% °C⁻¹. The thermistor network has a negative temperature coefficient. The compensator "
        "is designed to provide a slope that is equal in magnitude, but opposite in sign to that of "
        "the copper coil. Hence, the Ω vs. °C slope of the compensator is equal to the Ω/°C change "
        "of the coil. This results in a current through the coil that is independent of temperature. "
        "Additional applications include compensation of drift in silicon strain gages, infrared "
        "detectors, and circuits that contain both passive and active components."))
    b.append(p("For the basic linear resistance network of Figure 32.21a:"))
    b.append(eq("<i>R</i><sub>12</sub> = <i>R</i><sub>C</sub> = " +
                _frac("<i>RR</i><sub>T</sub>", "<i>R</i> + <i>R</i><sub>T</sub>") +
                " = <i>R</i>(1 − " + _frac("1", "1 + <i>R</i><sub>T</sub>/<i>R</i>") + ")", "32.67"))
    b.append(p(
        "Normalizing with respect to <i>R</i> and substituting <i>r</i><sub>T</sub> = "
        "<i>R</i><sub>T</sub>/<i>R</i><sub>T0</sub> and <i>R</i><sub>T0</sub>/<i>R</i> = σ in "
        "Equation 32.67 yields:"))
    b.append(eq("<i>R</i><sub>n</sub> = " +
                _frac("<i>R</i><sub>C</sub>", "<i>R</i>") + " = 1 − " +
                _frac("1", "1 + <i>r</i><sub>T</sub>σ") + " = 1 − <i>F</i>(<i>T</i>)", "32.68"))
    b.append(p(
        "Consequently, the techniques used for optimizing the linearity of voltage dividers also "
        "apply to linear resistance networks. The use of the series resistor <i>R</i><sub>1</sub> in "
        "Figure 32.21b translates the curve to a higher resistance level and does not affect the "
        "Ω/°C output."))
    b.append(fig(21, F.fig(21), "en"))
    b.append(p(
        "Frequently, the design of a compensator that provides the desired Ω/°C output results in a "
        "thermistor that has a nonstandard <i>R</i><sub>T0</sub> value. The conversion circuit of "
        "Figure 32.21c permits the use of a standard <i>R</i><sub>T0</sub> value. The conversion "
        "equations are as follows:"))
    b.append(eq("<i>K</i><sub>1</sub> = " +
                _sq(_frac("<i>R</i>′<sub>T0</sub>", "<i>R</i><sub>T0</sub>")), "32.69"))
    b.append(eq("<i>R</i><sub>E</sub> = <i>R</i><sub>1</sub> − <i>R</i>(<i>K</i><sub>1</sub> − 1)",
                "32.70"))
    b.append(eq("<i>R</i><sub>A</sub> = <i>RK</i><sub>1</sub>(<i>K</i><sub>1</sub> − 1)", "32.71"))
    b.append(eq("<i>R</i><sub>B</sub> = <i>RK</i><sub>1</sub>", "32.72"))
    b.append(p(
        "where <i>R</i><sub>T0</sub> is the nonstandard value and <i>R</i>′<sub>T0</sub> is the "
        "standard value. A requirement is that both thermistors have the same resistance "
        "ratio–temperature characteristic. Setting <i>R</i><sub>1</sub> = <i>R</i>(<i>K</i><sub>1"
        "></sub> − 1) in Figure 32.21b results in <i>R</i><sub>E</sub> = 0 for Figure 32.21c. "
        "Consequently, the conversion of Figure 32.21a to that of Figure 32.21c requires the use of "
        "the minimum insertion resistance <i>R</i><sub>1</sub> = <i>R</i>(<i>K</i><sub>1</sub> − 1)."))
    b.append(p(
        "The network provides good linearity for small temperature spans of 10 °C to 30 °C. "
        "However, the error increases rapidly from about 0.15 °C for a 30 °C span to 0.7 °C for a "
        "50 °C span (0 °C to 50 °C). The use of the two-thermistor network shown in Figure 32.22 "
        "results in a maximum linearity error of 0.22 °C over the range of 0 °C to 100 °C, while the "
        "three-thermistor network shown reduces the error to 0.04 °C for the same 0 °C to 100 °C "
        "range [5]. The networks shown in Figure 32.22 are linear voltage dividers. Placing the "
        "resistor <i>R</i><sub>1</sub> across the output terminals 3–4 converts these networks to "
        "linear resistance networks. Many manufacturers sell an interchangeable, three-wire, dual "
        "thermistor that is suitable for use in the two-thermistor circuit of Figure 32.22."))
    b.append(fig(22, F.fig(22), "en"))
    b.append(p(
        "Interchangeable thermistors and the linearization techniques described above have been "
        "available for many years. In addition, the stability of NTC thermistors is better than that "
        "of thermocouples and frequently better than or equal to that of commercial RTDs [17]. "
        "However, the nonlinear resistance–temperature characteristics of thermistors continue to "
        "limit their use in industrial temperature measurement and control applications. The "
        "availability of low-cost microprocessors has eliminated this limitation. Such devices can "
        "use the equation constants of Equations 32.38 or 32.39 to compute and display temperature "
        "directly. They also can be used to compute lookup tables to provide interpolation "
        "uncertainties in the range of 0.001 °C to 0.01 °C. There are instruments described in the "
        "literature that utilize such microprocessor chips [18, 19]. Thermometrics, Inc. sells a "
        "commercial instrument that reads the equation constants from a chip in the connector of "
        "each probe supplied for use with the instrument [1]. The use of thermistors for industrial "
        "applications will continue to increase as the cost of microprocessor chips continues to "
        "fall."))

    b.append(_refs323("en"))
    return "".join(b)


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


def _refs323(lang):
    """§32.3 has nineteen references of its own, numbered 1–19 within the section."""
    vi = lang == "vi"
    items = [
        "1. Thermometrics, Inc., <i>Thermometrics NTC &amp; PTC Thermistors</i>, Edison, NJ, 1993.",
        "2. J. Fabien, Heating with PTC thermistors, <i>EDN Products Edition</i>, 41(12A), 10, "
        "1996.",
        "3. M. Sapoff and R. M. Oppenheim, The design of linear thermistor networks, <i>IEEE "
        "International Convention Record</i>, Part 8, 12, 1964.",
        "4. M. Sapoff, Thermistors: Part 4, Optimum linearity techniques, <i>Measurements &amp; "
        "Control</i>, 14(10), 1980.",
        "5. C. D. Kimball and R. W. Harruff, Thermistor thermometry design for biological systems, "
        "<i>Temperature, Its Measurement and Control in Science and Industry</i>, Vol. 4, "
        "Pittsburgh, PA: Instrument Society of America, 1972, Part 2.",
        "6. Ketema, Rodan Division, <i>Thermistor Product Guide</i>, Anaheim, CA, 1995.",
        "7. Cesiwid Inc., <i>Alphalite® Bulk Ceramic NTC Thermistors</i>, Niagara Falls, NY, 1996.",
        "8. Fenwal Electronics, Inc., <i>Standard Products Catalog</i>, Milford, MA, 1994.",
        "9. Fenwal Electronics, Inc., <i>Thermistor Manual</i>, Milford, MA, 1974.",
        "10. Victory Engineering Corporation, <i>Technical Corporation of Thermistors &amp; "
        "Varistors</i>, Springfield, NJ, 1962.",
        "11. J. S. Steinhart and S. R. Hart, Calibration curves for thermistors, <i>Deep Sea "
        "Research</i>, 15, 497, 1968.",
        "12. B. W. Mangum, The triple point of succinonitrile and its use in the calibration of "
        "thermistor thermometers, <i>Rev. Sci. Instrum.</i>, 54(12), 1687, 1983.",
        "13. M. Sapoff, W. R. Siwek, H. C. Johnson, J. Slepian, and S. Weber, The exactness of fit "
        "of resistance–temperature data of thermistors with third-degree polynomials, in J. F. "
        "Schooley (ed.), <i>Temperature, Its Measurement and Control in Science and Industry</i>, "
        "Vol. 5, New York, NY: American Institute of Physics, 1982, 875.",
        "14. M. Sapoff and R. M. Oppenheim, Theory and application of self-heated thermistors, "
        "<i>Proc. IEEE</i>, 51, 1292, 1963.",
        "15. M. Sapoff, Thermistors: Part 5, Applications, <i>Measurements &amp; Control</i>, "
        "14(12), 1980.",
        "16. Hart Scientific, Inc., <i>Hart Scientific Calibration Equipment</i>, Pleasant Grove, "
        "UT, 1995.",
        "17. W. R. Siwek, M. Sapoff, A. Goldberg, H. C. Johnson, M. Botting, R. Lonsdorf, and S. "
        "Weber, Stability of NTC thermistors, in J. F. Schooley (ed.), <i>Temperature, Its "
        "Measurement and Control in Science and Industry</i>, Vol. 6, New York, NY: American "
        "Institute of Physics, 1992, 497.",
        "18. R. L. Berger, T. Clem, C. Gibson, W. Siwek, and M. Sapoff, A digitally linearized "
        "thermistor thermometer referenced to IPTS—26(13), 68, 1980.",
        "19. W. R. Siwek, M. Sapoff, A. Goldberg, H. C. Johnson, M. Botting, R. Lonsdorf, and S. "
        "Weber, A precision temperature standard based on the exactness of fit of thermistor "
        "resistance–temperature data using third degree polynomials, in J. F. Schooley (ed.), "
        "<i>Temperature, Its Measurement and Control in Science and Industry</i>, Vol. 6, New York, "
        "NY: American Institute of Physics, 1992, 491.",
    ]
    head_ = "<h3 id=\"t32-tltk-3\">Tài liệu tham khảo</h3>" if vi else \
            "<h3 id=\"t32-tltk-3\">References</h3>"
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
    ("32.3", "Thermistor Thermometers", "Nhiệt kế nhiệt điện trở", [
        ("Thermal Properties of NTC Thermistors", "Tính chất nhiệt của nhiệt điện trở NTC"),
        ("Electrical Properties of NTC Thermistors", "Tính chất điện của nhiệt điện trở NTC"),
        ("Voltage–Current Characteristics", "Đặc tính dòng – áp", 1),
        ("Current–Time Characteristics", "Đặc tính dòng – thời gian", 1),
        ("Resistance–Temperature Characteristics", "Đặc tính điện trở – nhiệt độ", 1),
        ("Linearization and Signal Conditioning Techniques",
         "Kỹ thuật tuyến tính hóa và điều chế tín hiệu"),
        ("Linear Conductance Networks", "Mạng dẫn tuyến tính", 1),
        ("Temperature Controllers", "Bộ điều khiển nhiệt độ", 1),
        ("Linear Resistance Networks", "Mạng điện trở tuyến tính", 1),
    ]),
]


def sec_index(vi):
    out = ['<ol class="toc-list">']
    for num, en, vn, subs in INDEX:
        title = vn if vi else en
        out.append('<li><span class="n">%s</span><a class="t" href="#s32-%s">%s</a></li>'
                   % (num, num.split(".")[1], title))
        for item in subs:
            sub_en, sub_vi = item[0], item[1]
            # a third element means the entry is one level down: the three
            # characteristics nest under "Electrical Properties", the three
            # circuit techniques under "Linearization"
            deep = len(item) > 2
            out.append('<li style="margin-left:%s;font-size:%s;padding:.15rem 0">'
                       '<a class="t" href="#s32-%s-%s">%s</a></li>'
                       % ("4.2rem" if deep else "2.4rem",
                          ".86rem" if deep else ".9rem",
                          num.split(".")[1], _slug(sub_en),
                          sub_vi if vi else sub_en))
    out.append("</ol>")
    return "".join(out)


def body_vi():
    lede = (
        "Nhiệt độ là đại lượng được đo nhiều nhất trong công nghiệp, và cũng là đại lượng có nhiều "
        "họ nguyên lý chuyển đổi nhất. Chương này đi qua mười một họ dụng cụ — từ dải lưỡng kim, "
        "nhiệt điện trở, cặp nhiệt điện đến hồng ngoại và sợi quang — với phương trình, hình vẽ và "
        "bảng dữ liệu của từng loại.")
    return (p(lede) + sec_index(True) + sec_32_1_vi() + back_vi() + sec_32_2_vi()
            + sec_32_3_vi())


def body_en():
    lede = (
        "Temperature is the most widely measured quantity in industry, and the one with the largest "
        "number of transducer families. This chapter works through eleven of them — bimetallic "
        "strips, resistance thermometers, thermistors, thermocouples, semiconductor junctions, "
        "infrared, pyroelectric, liquid-in-glass, manometric, indicators and fiber-optic probes — "
        "with the equations, figures and data tables for each.")
    return (p(lede) + sec_index(False) + sec_32_1_en() + back_en() + sec_32_2_en()
            + sec_32_3_en())


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
    meta = ("Chương 32 · theo Ch32.pdf (CRC Press, 1999) · §32.1–32.3/11 · 22 hình, 72 phương "
            "trình, 11 bảng" if vi else
            "Chapter 32 · §32.1–32.3 of 11 · 22 figures, 72 equations, 11 tables")
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
