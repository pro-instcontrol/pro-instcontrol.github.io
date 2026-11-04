# -*- coding: utf-8 -*-
"""Handbook Chapter 32 — Temperature (Robert J. Sandberg, ed.)

The chapter is 163 source pages and eleven sections, each contributed by a
different author. Sections are being written in order; §32.1–§32.5 are
complete (§32.4 finished in session 51, §32.5 in session 52), §32.6–§32.11
remain.

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


def h5(t, en=""):
    """A fourth-level heading. §32.4 nests twice under "Thermoelectric Effects"
    (Grounding, Balanced Thermocouple Circuits and Filtering live under Noise
    Problems; Static and Transient Thermometry under Thermal Coupling), one
    level deeper than h4 reaches."""
    if en == t:
        en = ""
    a = ""
    if _CUR[0]:
        base = (en or t) if _LANG[0] == "vi" else t
        a = ' id="s32-%s-%s"' % (_CUR[0], _slug(base))
    return ('<h5%s style="font-size:.93rem;font-weight:700;margin:1.35rem 0 .4rem">%s%s</h5>'
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


def _t3212(lang):
    """Table 32.12 — U.S. letter-designated thermocouple characteristics.
    The tolerance columns follow the book's own row placement: the special
    tolerance sits on the pair row (B, E, J...), the normal tolerance on the
    extension row (BX, EX, JX...)."""
    vi = lang == "vi"
    dash = "—"
    hd = ("Loại", "Tên thường", "Mã màu", "N.đ. nóng chảy (°C)",
          "Dải khuyến nghị (°C)", "emf ở 400 °C (mV)",
          "Dung sai đặc biệt", "Dung sai thường", "ρ (µΩ·cm)") if vi else \
         ("Type", "Common name", "Color code", "M.P. (°C)",
          "Recommended range (°C)", "emf at 400 °C (mV)",
          "Special tolerance", "Normal tolerance", "ρ (µΩ·cm)")
    C = {"Brown": ("Nâu", "Brown"), "Gray": ("Xám", "Gray"), "Red": ("Đỏ", "Red"),
         "Purple": ("Tím", "Purple"), "White": ("Trắng", "White"),
         "Yellow": ("Vàng", "Yellow"), "Green": ("Xanh lục", "Green"),
         "Blue": ("Xanh lam", "Blue"), "Orange": ("Cam", "Orange"),
         "Iron": ("Sắt", "Iron"), "Copper": ("Đồng", "Copper")}
    col = lambda k: C[k][0 if vi else 1]
    # values below are already written per-language
    # (type, common, colour, mp, range, emf400, special, normal, rho)
    D = [
        ("B",  "",        "Brown",  "1810", ("870", "1700"),  "0.787",  ("0.25%", ""),            "34.4"),
        ("BX", "",        "Gray",   "",     None,       "",  ("", "0.50%"),            ""),
        ("BP", "Pt30Rh",  "Gray",   "1910", None,       "",  ("", ""),            "18.6"),
        ("BN", "Pt6Rh",   "Red",    "1810", None,       "",  ("", ""),            "15.8"),
        ("E",  "",        "Brown",  "1270", ("-200", "870"),  "28.946", ("1.0°C or 0.40%", ""),  "127"),
        ("EX", "",        "Purple", "",     None,       "",  ("", "1.7°C or 0.50%"),   ""),
        ("EP", "Chromel", "Purple", "1430", None,       "",  ("", ""),            "80"),
        ("EN", "Constantan", "Red", "1270", None,       "",  ("", ""),            "46"),
        ("J",  "",        "Brown",  "1270", ("0", "760"),     "21.848", ("1.1°C or 0.40%", ""),  "56"),
        ("JX", "",        "White",  "",     None,       "",  ("", "2.2°C or 0.75%"),   ""),
        ("JP", "Iron",    "White",  "1536", None,       "",  ("", ""),            "10"),
        ("JN", "Constantan", "Red", "1270", None,       "",  ("", ""),            "46"),
        ("K",  "",        "Brown",  "1400", ("-200", "1260"), "16.397", ("1.1°C or 0.40%", ""), "112"),
        ("KX", "",        "Yellow", "",     None,       "",  ("", "2.2°C or 0.75%"),   ""),
        ("KP", "Chromel", "Yellow", "1430", None,       "",  ("", ""),            "80"),
        ("KN", "Alumel",  "Red",    "1400", None,       "",  ("", ""),            "31"),
        ("N",  "",        "Brown",  "",     ("0", "1260"),    "12.974", ("1.1°C or 0.40%", ""),  ""),
        ("NX", "",        "Orange", "",     None,       "",  ("", "2.2°C or 0.75%"),   ""),
        ("NP", "Nisil",   "Orange", "",     None,       "",  ("", ""),            ""),
        ("NN", "Nicrosil", "Red",   "",     None,       "",  ("", ""),            ""),
        ("R",  "",        "Brown",  "1769", ("0", "1480"),    "3.408",  ("0.6°C or 0.10%", ""),  "29"),
        ("RX", "",        "Green",  "",     None,       "",  ("", "1.5°C or 0.25%"),   ""),
        ("RP", "Pt13Rh",  "Green",  "1840", None,       "",  ("", ""),            "19"),
        ("RN", "Pt",      "Red",    "1769", None,       "",  ("", ""),            "10"),
        ("S",  "",        "Brown",  "1769", ("0", "1480"),    "3.259",  ("0.6°C or 0.10%", ""),  "30"),
        ("SX", "",        "Green",  "",     None,       "",  ("", "1.5°C or 0.25%"),   ""),
        ("SP", "Pt10Rh",  "Green",  "1830", None,       "",  ("", ""),            "20"),
        ("SN", "Pt",      "Red",    "1769", None,       "",  ("", ""),            "10"),
        ("T",  "",        "Brown",  "1083", ("-200", "370"),  "20.810", ("0.5°C or 0.40%", ""),  "48"),
        ("TX", "",        "Blue",   "",     None,       "",  ("", "1.0°C or 0.75%"),   ""),
        ("TP", "Copper",  "Blue",   "1083", None,       "",  ("", ""),            "2"),
        ("TN", "Constantan", "Red", "1270", None,       "",  ("", ""),            "46"),
    ]
    th = lambda s: s.replace(".", ",") if vi else s          # decimal mark
    ti = lambda s: ("{:,}".format(int(s)).replace(",", ".") if vi
                    else s) if s.isdigit() else s            # thousands mark
    tol = lambda t: (t.replace(".", ",").replace("hoặc", "hoặc") if vi else t)
    rows = []
    for ty, name, colour, mp, rng, emf, tolsp, rho in D:
        lo, hi = (rng if rng else ("", ""))
        if vi:
            rtxt = ("%s đến %s" % (ti(lo.lstrip("-")) if lo.isdigit() else lo.replace("-", "−"),
                                   ti(hi))) if rng else dash
            rtxt = rtxt if rng else dash
            if rng and lo.startswith("-"):
                rtxt = "−%s đến %s" % (ti(lo[1:]), ti(hi))
            sp = tolsp[0].replace(" or ", " hoặc ").replace(".", ",") if tolsp[0] else dash
            no = tolsp[1].replace(" or ", " hoặc ").replace(".", ",") if tolsp[1] else dash
        else:
            rtxt = ("%s to %s" % (lo, hi)) if rng else dash
            sp = tolsp[0] if tolsp[0] else dash
            no = tolsp[1] if tolsp[1] else dash
        rows.append((ty, name if name else dash, col(colour) if colour else dash,
                     ti(mp) if mp else dash, rtxt, th(emf) if emf else dash,
                     sp, no, th(rho) if rho else dash))
    cap = ("Bảng 32.12 · Đặc tính của các cặp nhiệt điện ký hiệu chữ cái của Hoa Kỳ "
           "<sup>a–d</sup> (theo Tài liệu tham khảo [1, 4, 9, 10])." if vi else
           "Table 32.12 · Characteristics of U.S. letter-designated thermocouples "
           "<sup>a–d</sup>. From References [1, 4, 9, 10].")
    return table(hd, rows, cap, cls="tbl matrix", small=True)


def _t3214(lang):
    """Table 32.14 — the five corollaries from the Law of Seebeck emf
    (abbreviated from [29]). Rendered as a one-column table: the book's frame
    is a list, not a grid."""
    vi = lang == "vi"
    intro = ("Trong mọi mạch gồm các vật liệu dẫn điện có hệ số Seebeck tuyệt đối "
             "<i>σ</i>(<i>T</i>), mỗi vật liệu đều đẳng hướng nhiệt điện và tuân theo Luật "
             "Seebeck, d<i>E</i>(<i>T</i>) = <i>σ</i>(<i>T</i>)d<i>T</i>:" if vi else
             "In any circuit of electrically conducting materials that have an absolute Seebeck "
             "coefficient <i>σ</i>(<i>T</i>), that are each thermoelectrically homogeneous, and "
             "which follow the Seebeck Law, d<i>E</i>(<i>T</i>) = <i>σ</i>(<i>T</i>)d<i>T</i>:")
    cor = [
        (("1. Hệ quả về vai trò chức năng",
          "Có ba vai trò chức năng nhiệt điện: mối nối, “dây dẫn”, và nguồn suất điện động "
          "Seebeck: • Các mối nối nhiệt điện thực là mặt tiếp xúc ghép ohmic hai vật liệu khác "
          "nhau; • “Dây dẫn” là các đoạn mà, riêng lẻ hay kết hợp, không góp suất điện động "
          "Seebeck thuần; • Mọi đoạn khác đều là nguồn suất điện động Seebeck."),
         ("1. The Corollary of Functional Roles",
          "There are three thermoelectric functional roles: junctions, “conductors,” and Seebeck "
          "emf sources: • Real thermoelectric junctions are interfaces that ohmically couple "
          "dissimilar materials; • “Conductors” are segments that, in effect, individually or in "
          "combination, contribute no net Seebeck emf; • All other segments are sources of "
          "Seebeck emf.")),
        (("2. Hệ quả về tính tất định chức năng",
          "Vai trò nhiệt điện tức thời quanh một mạch không thể ấn định trước bằng kết cấu vật "
          "lý, lựa chọn vật liệu, hay cách bố trí mạch một mình; chúng chi phối bởi sự phân bố "
          "nhiệt độ."),
         ("2. The Corollary of Functional Determinacy",
          "Instantaneous thermoelectric roles around a circuit cannot be predetermined by "
          "physical construction, material choice, or circuit arrangement alone; they are "
          "governed by temperature distribution.")),
        (("3. Hệ quả về tính tất định nhiệt độ",
          "Trong mạch có nhiều mối nối, nhiệt độ của một mối nối duy nhất chỉ có thể xác định "
          "từ suất điện động Seebeck thuần nếu nhiệt độ của mọi mối nối thực khác đã được xác "
          "định."),
         ("3. The Corollary of Temperature Determinacy",
          "In a circuit with multiple junctions, the temperature of a single junction can be "
          "determined from the net Seebeck emf only if the temperatures of all other real "
          "junctions are defined.")),
        (("4. Hệ quả về tính tất định suất điện động",
          "Suất điện động Seebeck chỉ do các thân nhiệt điện sinh ra, nhưng suất điện động "
          "Seebeck thuần lại chịu chi phối bởi nhiệt độ của các mối nối thực."),
         ("4. The Corollary of emf Determinacy",
          "Seebeck emf is produced only by thermoelements, but the net Seebeck emf is governed "
          "by the temperatures only of real junctions.")),
        (("5. Hệ quả về suất điện động Seebeck",
          "Suất điện động Seebeck của bất kỳ đoạn vật liệu M nào, với nhiệt độ điểm cuối "
          "<i>T</i><sub>1</sub> tại <i>X</i><sub>1</sub> và <i>T</i><sub>2</sub> tại "
          "<i>X</i><sub>2</sub>, là độc lập với sự phân bố nhiệt độ, gradient nhiệt độ hay tiết "
          "diện, vì nó được xác định bởi "
          "<i>E</i><sub>M</sub> = ∫<sub><i>X</i>1</sub><sup><i>X</i>2</sup> "
          "<i>σ</i><sub>M</sub>(<i>T</i>)d<i>T</i> = <i>E</i><sub>M</sub>(<i>T</i><sub>2</sub>) "
          "− <i>E</i><sub>M</sub>(<i>T</i><sub>1</sub>)."),
         ("5. The Corollary of Seebeck emf",
          "The Seebeck emf of any segment of material M with end-point temperatures "
          "<i>T</i><sub>1</sub> at segment endpoint <i>X</i><sub>1</sub> and <i>T</i><sub>2</sub> "
          "at segment endpoint <i>X</i><sub>2</sub> is independent of temperature distribution, "
          "temperature gradient, or cross-section as it is determined by "
          "<i>E</i><sub>M</sub> = ∫<sub><i>X</i>1</sub><sup><i>X</i>2</sup> "
          "<i>σ</i><sub>M</sub>(<i>T</i>)d<i>T</i> = <i>E</i><sub>M</sub>(<i>T</i><sub>2</sub>) "
          "− <i>E</i><sub>M</sub>(<i>T</i><sub>1</sub>).")),
    ]
    rows = [intro]
    for title, body in cor:
        rows.append("<b>%s.</b><br>%s" % (title[0 if vi else 1], body[0 if vi else 1]))
    cap = ("Bảng 32.14 · Các hệ quả từ Luật suất điện động Seebeck (rút gọn từ Tài liệu "
           "tham khảo [29])." if vi else
           "Table 32.14 · Corollaries from the Law of Seebeck emf. From References "
           "[1, 7, 29, 30], abbreviated from [29].")
    return table(("<i>σ</i>(<i>T</i>)",), rows, cap, cls="tbl", small=True)


def _t3213(lang):
    """Table 32.13 — international thermocouple color codes (as of 1998)."""
    vi = lang == "vi"
    dash = "—"
    hd = ("Loại", "Mỹ", "IEC", "Anh", "T.Quốc", "Pháp", "Đức", "Nhật", "Nga") if vi else \
         ("Type", "U.S.", "IEC", "England", "China", "France", "Germany", "Japan", "Russia")
    rows = [
        ("B", ("Nâu", "Brown")[not vi], dash, dash, dash, dash, dash, dash, dash, "B"),
        ("BX", ("Xám", "Gray")[not vi], dash, dash, dash, dash, ("Xám", "Gray")[not vi], ("Xám", "Gray")[not vi], dash, "BX"),
        ("BP", ("Xám", "Gray")[not vi], dash, dash, dash, dash, ("Đỏ", "Red")[not vi], ("Đỏ", "Red")[not vi], dash, "BP"),
        ("BN", ("Đỏ", "Red")[not vi], dash, dash, dash, dash, ("Xám", "Gray")[not vi], ("Xám", "Gray")[not vi], dash, "BN"),
        ("E", ("Nâu", "Brown")[not vi], dash, dash, dash, dash, dash, dash, dash, "E"),
        ("EX", ("Tím", "Purple")[not vi], ("Tím", "Purple")[not vi], ("Nâu", "Brown")[not vi], dash, ("Tím", "Purple")[not vi], ("Đen", "Black")[not vi], ("Tím", "Purple")[not vi], dash, "EX"),
        ("EP", ("Tím", "Purple")[not vi], ("Tím", "Purple")[not vi], ("Nâu", "Brown")[not vi], ("Đỏ", "Red")[not vi], ("Vàng", "Yellow")[not vi], ("Đỏ", "Red")[not vi], ("Đỏ", "Red")[not vi], ("Tím hoặc đen", "Purple or black")[not vi], "EP"),
        ("EN", ("Đỏ", "Red")[not vi], ("Trắng", "White")[not vi], ("Xanh lam", "Blue")[not vi], ("Nâu", "Brown")[not vi], ("Tím", "Purple")[not vi], ("Đen", "Black")[not vi], ("Trắng", "White")[not vi], ("Vàng hoặc cam", "Yellow or orange")[not vi], "EN"),
        ("J", ("Nâu", "Brown")[not vi], dash, ("Đỏ", "Red")[not vi], dash, dash, dash, dash, dash, "J"),
        ("JX", ("Đen", "Black")[not vi], ("Đen", "Black")[not vi], ("Đen", "Black")[not vi], dash, ("Đen", "Black")[not vi], ("Xanh lam", "Blue")[not vi], ("Vàng", "Yellow")[not vi], dash, "JX"),
        ("JP", ("Trắng", "White")[not vi], ("Đen", "Black")[not vi], ("Vàng", "Yellow")[not vi], ("Đỏ", "Red")[not vi], ("Vàng", "Yellow")[not vi], ("Đỏ", "Red")[not vi], ("Đỏ", "Red")[not vi], ("Trắng", "White")[not vi], "JP"),
        ("JN", ("Đỏ", "Red")[not vi], ("Trắng", "White")[not vi], ("Xanh lam", "Blue")[not vi], ("Tím", "Purple")[not vi], ("Đen", "Black")[not vi], ("Xanh lam", "Blue")[not vi], ("Trắng", "White")[not vi], ("Vàng hoặc cam", "Yellow or orange")[not vi], "JN"),
        ("K", ("Nâu", "Brown")[not vi], dash, dash, dash, dash, dash, dash, dash, "K"),
        ("KX", ("Vàng", "Yellow")[not vi], ("Xanh lục", "Green")[not vi], ("Đỏ", "Red")[not vi], dash, ("Vàng", "Yellow")[not vi], ("Xanh lục", "Green")[not vi], ("Xanh lam", "Blue")[not vi], dash, "KX"),
        ("KP", ("Vàng", "Yellow")[not vi], ("Xanh lục", "Green")[not vi], ("Nâu", "Brown")[not vi], ("Đỏ", "Red")[not vi], ("Vàng", "Yellow")[not vi], ("Đỏ", "Red")[not vi], ("Đỏ", "Red")[not vi], ("Đỏ", "Red")[not vi], "KP"),
        ("KN", ("Đỏ", "Red")[not vi], ("Trắng", "White")[not vi], ("Xanh lam", "Blue")[not vi], ("Xanh lam", "Blue")[not vi], ("Tím", "Purple")[not vi], ("Xanh lục", "Green")[not vi], ("Trắng", "White")[not vi], ("Nâu", "Brown")[not vi], "KN"),
        ("N", ("Nâu", "Brown")[not vi], dash, dash, dash, dash, dash, dash, dash, "N"),
        ("NX", ("Cam", "Orange")[not vi], dash, dash, dash, dash, dash, dash, dash, "NX"),
        ("NP", ("Cam", "Orange")[not vi], dash, dash, dash, dash, dash, dash, dash, "NP"),
        ("NN", ("Đỏ", "Red")[not vi], dash, dash, dash, dash, dash, dash, dash, "NN"),
        ("R", ("Nâu", "Brown")[not vi], dash, dash, dash, dash, dash, dash, dash, "R"),
        ("RX", ("Đen", "Black")[not vi], ("Cam", "Orange")[not vi], ("Xanh lục", "Green")[not vi], dash, ("Xanh lục", "Green")[not vi], ("Trắng", "White")[not vi], ("Đen", "Black")[not vi], dash, "RX"),
        ("RP", ("Đen", "Black")[not vi], ("Cam", "Orange")[not vi], ("Trắng", "White")[not vi], ("Đỏ", "Red")[not vi], ("Vàng", "Yellow")[not vi], ("Đỏ", "Red")[not vi], ("Đỏ", "Red")[not vi], dash, "RP"),
        ("RN", ("Đỏ", "Red")[not vi], ("Trắng", "White")[not vi], ("Xanh lam", "Blue")[not vi], ("Xanh lục", "Green")[not vi], ("Xanh lục", "Green")[not vi], ("Trắng", "White")[not vi], ("Trắng", "White")[not vi], dash, "RN"),
        ("S", ("Nâu", "Brown")[not vi], dash, dash, dash, dash, dash, dash, dash, "S"),
        ("SX", ("Đen", "Black")[not vi], ("Cam", "Orange")[not vi], ("Xanh lục", "Green")[not vi], dash, ("Xanh lục", "Green")[not vi], ("Trắng", "White")[not vi], ("Đen", "Black")[not vi], dash, "SX"),
        ("SP", ("Đen", "Black")[not vi], ("Cam", "Orange")[not vi], ("Trắng", "White")[not vi], ("Đỏ", "Red")[not vi], ("Vàng", "Yellow")[not vi], ("Đỏ", "Red")[not vi], ("Đỏ", "Red")[not vi], ("Đỏ hoặc hồng", "Red or pink")[not vi], "SP"),
        ("SN", ("Đỏ", "Red")[not vi], ("Trắng", "White")[not vi], ("Xanh lam", "Blue")[not vi], ("Xanh lục", "Green")[not vi], ("Xanh lục", "Green")[not vi], ("Trắng", "White")[not vi], ("Trắng", "White")[not vi], ("Xanh lục", "Green")[not vi], "SN"),
        ("T", ("Nâu", "Brown")[not vi], dash, dash, dash, dash, dash, dash, dash, "T"),
        ("TX", ("Xanh lam", "Blue")[not vi], ("Nâu", "Brown")[not vi], ("Xanh lam", "Blue")[not vi], dash, ("Xanh lam", "Blue")[not vi], ("Nâu", "Brown")[not vi], ("Nâu", "Brown")[not vi], dash, "TX"),
        ("TP", ("Xanh lam", "Blue")[not vi], ("Nâu", "Brown")[not vi], ("Trắng", "White")[not vi], ("Đỏ", "Red")[not vi], ("Vàng", "Yellow")[not vi], ("Đỏ", "Red")[not vi], ("Đỏ", "Red")[not vi], ("Đỏ hoặc hồng", "Red or pink")[not vi], "TP"),
        ("TN", ("Đỏ", "Red")[not vi], ("Trắng", "White")[not vi], ("Xanh lam", "Blue")[not vi], ("Trắng", "White")[not vi], ("Xanh lam", "Blue")[not vi], ("Nâu", "Brown")[not vi], ("Trắng", "White")[not vi], ("Nâu", "Brown")[not vi], "TN"),
        ("*",
         ("Tiêu chuẩn", "Std.")[not vi], ("Tiêu chuẩn", "Std.")[not vi],
         ("Tiêu chuẩn", "Std.")[not vi], ("Tiêu chuẩn", "Std.")[not vi],
         ("Tiêu chuẩn", "Std.")[not vi], ("Tiêu chuẩn", "Std.")[not vi],
         ("Tiêu chuẩn", "Std.")[not vi], ("Tiêu chuẩn", "Std.")[not vi], ("Tiêu chuẩn", "Std.")[not vi]),
        ("*", "MC96.1", "584-3", "1843", "NMI 42-323", "NFC42-43714", "DIN 43714", "JIS 1620", dash, dash),
    ]
    cap = ("Bảng 32.13 · Mã màu cặp nhiệt điện quốc tế (tình trạng năm 1998). Dòng dưới cùng "
           "nêu tiêu chuẩn và số hiệu của từng quốc gia." if vi else
           "Table 32.13 · International thermocouple color codes (as of 1998). The bottom "
           "rows give each nation's standard and its number. From References [1, 4, 9, 10].")
    return table(hd, rows, cap, cls="tbl matrix", small=True)


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


# ================================================================ §32.4
def sec_32_4a_vi():
    b = [h2("32.4 Nhiệt kế cặp nhiệt điện", "Thermocouple Thermometers")]
    b.append(authors("R. P. Reed", ""))

    b.append(h3("Cặp nhiệt điện đơn giản nhất", "The Simplest Thermocouple"))
    b.append(p(
        "Dù các loại cảm biến nhiệt độ ngày càng đa dạng, cặp nhiệt điện tự sinh điện vẫn là cảm "
        "biến được dùng phổ biến nhất cho đo nhiệt độ nhờ tính linh hoạt, tính đơn giản và dễ sử "
        "dụng của nó. Bất kỳ cặp vật liệu nào dẫn điện và khác nhau về tính nhiệt điện, được ghép "
        "với nhau tại một mặt tiếp xúc, đều là một cặp nhiệt điện [1]. Các dây chân là các "
        "<i>thân nhiệt điện</i> (thermoelement). Hiệu ứng Seebeck sinh ra điện áp trong mọi thân "
        "nhiệt điện ở những đoạn không đồng nhất về nhiệt độ. Bất kỳ mặt tiếp xúc điện giữa hai "
        "vật dẫn điện khác nhau đều là một mối nối nhiệt điện thực. Đầu tự do của một thân nhiệt "
        "điện là một đầu mút (terminus), không phải mối nối. Các chỗ ghép giữa hai thân nhiệt điện "
        "giống nhau là mối ghép, không phải mối nối."))
    b.append(p(
        "Chính các thân nhiệt điện quyết định độ nhạy và độ hiệu chuẩn của cặp nhiệt điện; nhưng "
        "chính nhiệt độ của các điểm cuối của thân nhiệt điện (tức nhiệt độ các mối nối) mới quyết "
        "định suất điện động (emf) thuần quan sát được trong đo nhiệt độ. Hiệu ứng Seebeck, vốn "
        "biến nhiệt độ thành điện áp, được dùng cho đo nhiệt độ nhiệt điện, nhưng cũng là một "
        "nguồn nhiễu tần số thấp chính trong mọi mạch điện tử mức thấp [2]."))

    b.append(h3("Đo nhiệt độ bằng cặp nhiệt điện đơn giản", "Simple Thermocouple Thermometry"))
    b.append(p(
        "Trong những ứng dụng đơn giản nhất, việc đo nhiệt độ bằng cặp nhiệt điện hiện nay dễ dùng "
        "ngang với việc dùng đồng hồ vạn năng để đo điện trở. Thực tế, nhiều đồng hồ vạn năng số "
        "hiện nay (ngoài đo áp, dòng và điện trở) còn cung cấp cả đầu dò nhiệt độ cặp nhiệt điện, "
        "và đo nhiệt độ chỉ là một chức năng chọn bằng nút bấm. Những nhiệt kế cặp nhiệt điện này "
        "gồm một bộ chỉ thị hiển thị số nhiệt độ tại đầu làm việc của một đầu dò cặp nhiệt điện "
        "cắm vào (Hình 32.24). Những đồng hồ vạn năng đa năng đơn giản hơn trong số đó có thể mua "
        "với giá dưới 60 đô-la Mỹ [3]. Các đầu dò cặp nhiệt điện thay thế được thuộc nhiều loại "
        "vật liệu cặp nhiệt điện chuẩn khác nhau, với những đầu cảm biến chuyên dụng có thiết kế "
        "rất đa dạng, được thích ứng để đo từ nhiệt độ bề mặt đến nhiệt độ bên trong thực phẩm [4]."))
    b.append(fig(24, F.fig(24), "vi"))
    b.append(p(
        "Với một số đầu dò, có thể chỉ thị nhiệt độ tới 1370 °C chỉ bằng cách (1) bảo đảm loại cặp "
        "nhiệt điện chọn trên bộ chỉ thị và trên đầu dò tương ứng nhau, (2) nhấn nút mở nguồn, và "
        "(3) áp đầu làm việc của đầu dò vào điểm cần đo nhiệt độ. Ngay lập tức, không cần hiệu "
        "chuẩn, nhiệt độ hiện tại của đầu dò được hiển thị số, chọn được theo °C hay °F, thường "
        "với độ phân giải 0,1 °C hoặc 1 °C. Một số tài liệu đặc tả nêu “độ chính xác” 0,3% (4 °C "
        "tại 1370 °C) của số đọc. Một số còn cung cấp khả năng truy nguồn hiệu chuẩn được chứng "
        "nhận tới NIST hoặc phòng chuẩn quốc gia khác."))
    b.append(p(
        "Điện tử số hiện đại đã tạo ra ảo tưởng rằng đo nhiệt độ bằng cặp nhiệt điện thật chính "
        "xác thì không khác gì các phép đo điện thông thường khác. Điều đó khuyến khích nhận định "
        "rằng độ chính xác tinh vi tùy ý bao giờ cũng đạt được bằng hiệu chuẩn và được bảo đảm "
        "bằng chứng nhận. Sự đơn giản hóa đáng kể của dụng cụ — điều nay đã trở nên phổ biến — "
        "cùng với lượng lớn các bài hướng dẫn gây hiểu lầm đã che khuất nhu cầu thực sự phải nắm "
        "vững nguyên lý của mạch cặp nhiệt điện cho bất kỳ phép đo nào không thuộc loại tầm "
        "thường."))
    b.append(p(
        "Nhà sản xuất có thể che chở người dùng khỏi nhiều vấn đề cố hữu trong ứng dụng cặp nhiệt "
        "điện. Đáng tiếc, vẫn còn nhiều cạm bẫy mà nhà sản xuất không thể cách ly người dùng bằng "
        "thiết kế hay kết cấu. Trong các ứng dụng kém đơn giản hơn, người dùng phải tự tránh các "
        "vấn đề bằng cách học kỹ và áp dụng đúng những nguyên lý xác thực của mạch nhiệt điện và "
        "của đo nhiệt độ cặp nhiệt điện. Ngay cả bộ chỉ thị và đầu dò đơn giản nhất cũng có thể "
        "dễ dàng bị dùng sai và tạo ra sai số đáng kể không được nhận biết."))
    b.append(p(
        "Sai số đo nhiệt độ chỉ vài °C, thậm chí nhỏ hơn nhiều, trong các lĩnh vực năng lượng, quá "
        "trình, sản xuất và nghiên cứu mỗi năm gây thiệt hại hàng triệu đô-la do mất năng suất, "
        "tốn nhiên liệu, mất thưởng thành tích, v.v. Hậu quả của sai số còn có thể là diễn giải "
        "dữ liệu sai, không đạt mục tiêu, hư hại thiết bị, thương tích cá nhân, thậm chí tử vong."))
    b.append(p(
        "Những mạch cặp nhiệt điện bất thường, những lắp đặt và ứng dụng đặc biệt thường tạo ra "
        "sai số khó nhận thấy, hoặc những kết quả lạ lùng gây bối rối nếu chưa hiểu một mô hình "
        "đích thực về mạch nhiệt điện. Phần chương này trình bày các nguyên lý xác thực của mạch "
        "nhiệt điện, giúp người dùng dễ dàng ứng dụng cặp nhiệt điện cho những phép đo nhiệt độ "
        "tin cậy và tới hạn, ngay cả trong hoàn cảnh bất thường, với sự tin tưởng có cơ sở. Những "
        "nguyên lý này rất đơn giản, song vẫn đáng nghiên cứu ngay cả với người dùng cặp nhiệt "
        "điện giàu kinh nghiệm, vì mạch nhiệt điện rất thường bị diễn đạt sai hoặc hiểu sai một "
        "cách tinh vi mà tuy không được nhận biết nhưng làm giảm chất lượng đo. Mục đích của phần "
        "chương này là cho phép đo nhiệt độ với mọi sự đơn giản thực tiễn, đồng thời tránh những "
        "sai số đo có thể tốn kém."))
    return "".join(b)


def sec_32_4a_en():
    b = [h2("32.4 Thermocouple Thermometers", "Nhiệt kế cặp nhiệt điện")]
    b.append(authors("R. P. Reed", ""))

    b.append(h3("The Simplest Thermocouple", "Cặp nhiệt điện đơn giản nhất"))
    b.append(p(
        "Despite an increasing variety of temperature sensors, the self-generating thermocouple "
        "remains the most generally used sensor for thermometry because of its versatility, "
        "simplicity, and ease of use. Any pair of electrically conducting and thermoelectrically "
        "dissimilar materials coupled at an interface is a thermocouple [1]. The legs are "
        "<i>thermoelements</i>. The Seebeck effect produces a voltage in all such thermoelements "
        "where they are not at a uniform temperature. Any electric interface between dissimilar "
        "electric conductors is a real thermoelectric junction. A free end of a thermoelement is "
        "a terminus, not a junction. Couplings between identical thermoelements are splices or "
        "joins, not junctions."))
    b.append(p(
        "It is the thermoelements that determine thermocouple sensitivity and calibration; but, it "
        "is the temperatures of the end-points of thermoelements (i.e., junction temperatures) "
        "that determine the net emf observed in thermometry. The Seebeck effect, which converts "
        "temperature to voltage, is used for thermoelectric thermometry but is also a primary "
        "low-frequency noise source in all low-level electronic circuits [2]."))

    b.append(h3("Simple Thermocouple Thermometry", "Đo nhiệt độ bằng cặp nhiệt điện đơn giản"))
    b.append(p(
        "In the simplest applications, thermocouple thermometry now is as easy to use as is a "
        "multimeter to measure resistance. In fact, many present-day digital multimeters (in "
        "addition to voltage, current, and resistance) do provide a thermocouple temperature "
        "probe, and temperature measurement is just another button-selectable function. These "
        "thermocouple thermometers consist of an indicator that digitally displays the temperature "
        "of the tip of a plug-in thermocouple probe (Figure 32.24). The simpler of such versatile "
        "multimeters can be purchased for less than U.S.$60 [3]. Interchangeable thermocouple "
        "probes of different standard thermocouple material types and specialized sensing tips of "
        "widely varying designs are adapted to measurement from surface temperatures to internal "
        "temperatures in foodstuffs [4]."))
    b.append(fig(24, F.fig(24), "en"))
    b.append(p(
        "With some probes, temperatures up to 1370 °C can be indicated merely by (1) ensuring "
        "that the selected thermocouple types of the indicator and probe correspond, (2) pressing "
        "a power-on button, and (3) applying the probe tip at the point where temperature is to "
        "be measured. Promptly, and without calibration, the present temperature of the probe tip "
        "is digitally displayed selectably in °C or °F, usually to a resolution of 0.1 °C or "
        "1 °C. Some specifications claim “accuracy” of 0.3% (4 °C at 1370 °C) of reading. Some "
        "even offer certified calibration traceability to NIST or other national standards "
        "laboratory."))
    b.append(p(
        "Modern digital electronics has created the illusion that very accurate thermocouple "
        "thermometry is no different than other routine electrical measurements. It has encouraged "
        "the perception that arbitrarily fine accuracy can always be accomplished by calibration "
        "and guaranteed by certification. The remarkable simplification of instruments that is now "
        "commonplace and an abundance of misleading tutorials obscure the real need for a sound "
        "understanding of principles of thermocouple circuits for anything other than "
        "inconsequential thermometry."))
    b.append(p(
        "Manufacturers can shelter users from many problems inherent in thermocouple application. "
        "Unfortunately, there are many pitfalls from which the manufacturer cannot isolate the "
        "user by design or construction. In less simple applications, it is necessary for the user "
        "to avoid problems by carefully learning and applying the true principles of "
        "thermoelectric circuits and thermocouple thermometry. Even the simplest indicators and "
        "probes can easily be misused and produce unrecognized substantial error."))
    b.append(p(
        "Thermometry errors of only a few °C or even much less in energy, process, manufacturing, "
        "and research fields annually cost many millions of dollars in lost yield, fuel cost, "
        "performance bonuses, etc. Consequence of error can also be incurred as incorrect "
        "interpretation of data, failure of objective, equipment damage, personal injury, or even "
        "loss of life."))
    b.append(p(
        "Unusual thermocouple circuits, installations, and special applications often produce "
        "inconspicuous error or else peculiar results that are very puzzling if an authentic model "
        "of thermoelectric circuits is not understood. This chapter section presents the factual "
        "principles of thermoelectric circuits that equip the user to easily apply thermocouples "
        "for reliable and critical thermometry, even in unusual circumstances with justified "
        "confidence. These principles are very simple, yet they justify study even by experienced "
        "thermocouple users as thermoelectric circuits are very often misrepresented or "
        "misunderstood in subtle ways that, although unrecognized, degrade measurement. The aim of "
        "the chapter section is to allow thermometry with all practical simplicity while avoiding "
        "possibly costly measurement errors."))
    return "".join(b)


def sec_32_4b_vi():
    b = [h3("Hiệu ứng nhiệt điện", "Thermoelectric Effects")]
    b.append(p(
        "Ba hiện tượng nhiệt điện là các hiệu ứng Seebeck, Peltier và Thomson [1, 2, 5-7]. Trong "
        "số đó, chỉ hiệu ứng Seebeck biến đổi năng lượng nhiệt thành năng lượng điện và cho ra "
        "điện áp cặp nhiệt điện dùng trong đo nhiệt độ. Các hiệu ứng Peltier và Thomson phụ thuộc "
        "dòng điện, không đáng kể trong đo nhiệt độ thực dụng. Chúng không sinh ra điện áp, trái "
        "với những quan niệm sai phổ biến. Các hiệu ứng Peltier và Thomson chỉ vận chuyển nhiệt "
        "bằng dòng điện và phân phối lại nhiệt trong mạch. Đo nhiệt độ bằng cặp nhiệt điện được "
        "tiến hành đúng đắn bằng phép đo hở mạch. Suất điện động Seebeck xuất hiện ngay cả khi "
        "không có dòng điện, trong khi các hiệu ứng Peltier và Thomson tất yếu triệt tiêu. Các "
        "hiệu ứng nhiệt – từ – điện liên quan chỉ có ý nghĩa khi có từ trường lớn và hiếm khi làm "
        "giảm chất lượng của đo nhiệt độ nhiệt điện ứng dụng [2, 5, 6]."))

    b.append(h4("Hiệu ứng Seebeck", "The Seebeck Effect"))
    b.append(p(
        "Hiệu ứng Seebeck là sự xuất hiện của một suất điện động nguồn thuần, tức suất điện động "
        "Seebeck tuyệt đối, giữa các cặp điểm trong bất kỳ một vật liệu dẫn điện riêng lẻ nào, do "
        "có chênh lệch nhiệt độ giữa chúng [1, 2, 5, 7, 8]. Suất điện động Seebeck xuất hiện mà "
        "không cần các vật liệu khác nhau. Nó không phải là hiện tượng tại mối nối, cũng không "
        "liên quan đến điện thế tiếp xúc của Volta."))

    b.append(h4("Các đặc tính Seebeck tuyệt đối", "Absolute Seebeck Properties"))
    b.append(p(
        "Hệ số Seebeck tuyệt đối biểu diễn độ nhạy đo (volt trên một đơn vị nhiệt độ) của hiệu "
        "ứng Seebeck. Nó được xác định trên bất kỳ vùng đồng nhất về nhiệt điện nào của một vật "
        "liệu dẫn điện thanh mảnh riêng lẻ bởi:"))
    b.append(eq("<i>σ</i>(<i>T</i>) = lim<sub>Δ<i>T</i>→0</sub> "
                "Δ<i>E</i>(<i>T</i>) / Δ<i>T</i>", "32.73"))
    b.append(eq("d<i>E</i>(<i>T</i>) = <i>σ</i>(<i>T</i>) d<i>T</i>", "32.74"))
    b.append(p(
        "Hệ số Seebeck là một tính chất vận chuyển của mọi vật liệu dẫn điện. Sau này, Phương "
        "trình 32.74 sẽ được thừa nhận là luật hàm chi phối suất điện động nhiệt điện. Từ Phương "
        "trình 32.74,"))
    b.append(eq("Δ<i>E</i> = ∫<sub><i>T</i>1</sub><sup><i>T</i>2</sup> "
                "<i>σ</i>(<i>T</i>) d<i>T</i> = "
                "<i>E</i>(<i>T</i><sub>2</sub>) − <i>E</i>(<i>T</i><sub>1</sub>)", "32.75"))
    b.append(p(
        "trong đó Δ<i>E</i> là lượng tăng suất điện động giữa một cặp điểm, cách nhau một khoảng "
        "cách bất kỳ, giữa đó có chênh lệch nhiệt độ Δ<i>T</i> = (<i>T</i><sub>2</sub> – "
        "<i>T</i><sub>1</sub>)."))
    b.append(p(
        "Từ Phương trình 32.75, hiệu ứng Seebeck thuần của một vật liệu cụ thể chỉ phụ thuộc nhiệt "
        "độ tại hai điểm, và không phụ thuộc các giá trị của gradient nhiệt độ giữa hai điểm đó. "
        "Hệ số Seebeck là hàm phi tuyến của nhiệt độ. Nó không phải là hằng số. Để đo nhiệt độ "
        "chính xác, hệ số Seebeck phải chỉ phụ thuộc vào nhiệt độ mà thôi. <i>σ</i>(<i>T</i>) "
        "không được thay đổi dọc theo thân nhiệt điện, cũng không được thay đổi đáng kể trong "
        "khoảng thời gian sử dụng. Tuy dễ bị tổn hại bởi các tác nhân môi trường như vậy, để đo "
        "chính xác nó không được phụ thuộc, trong lúc đo, vào các biến môi trường như biến dạng, "
        "áp suất hay từ trường."))
    b.append(p(
        "Hệ số <i>σ</i><sub>M</sub>(<i>T</i>) là hệ số Seebeck tuyệt đối của một vật liệu riêng "
        "lẻ M [1, 2, 7, 8]. Một điện áp nguồn tương ứng trong một vật liệu đơn là suất điện động "
        "Seebeck tuyệt đối, <i>E</i><sub>M</sub>(<i>T</i>). Suất điện động Seebeck tuyệt đối tồn "
        "tại thực nhưng không quan sát được một cách đơn giản. Hệ số Seebeck tuyệt đối có thể xác "
        "định gián tiếp bằng cách đo hệ số Thomson, <i>τ</i>, của vật liệu riêng lẻ và áp dụng "
        "một quan hệ Kelvin,"))
    b.append(eq("<i>σ</i><sub>abs</sub>(<i>T</i>) = (1/<i>T</i>) "
                "∫<sub>0</sub><sup><i>T</i></sup> <i>τ</i><sub>abs</sub> d<i>T</i>", "32.76"))
    b.append(p(
        "để suy ra hệ số Seebeck liên hệ về mặt nhiệt động lực học [1, 2, 5, 7, 8]."))

    b.append(h4("Các đặc tính Seebeck tương đối", "Relative Seebeck Properties"))
    b.append(p(
        "Hiệu của các suất điện động Seebeck của hai thân nhiệt điện, thuộc vật liệu A và B của "
        "một cặp nhiệt điện, với mối nối chung của chúng ở nhiệt độ <i>T</i><sub>m</sub> và cả "
        "hai điểm cuối ở nhiệt độ chuẩn thực <i>T</i><sub>r</sub>, là suất điện động Seebeck "
        "tương đối, <i>E</i><sub>AB</sub>(<i>T</i>), biểu diễn như sau:"))
    b.append(eq("<i>E</i><sub>AB</sub>(<i>T</i><sub>m</sub>,<i>T</i><sub>r</sub>) = "
                "<i>E</i><sub>A</sub>(<i>T</i><sub>m</sub>,<i>T</i><sub>r</sub>) − "
                "<i>E</i><sub>B</sub>(<i>T</i><sub>m</sub>,<i>T</i><sub>r</sub>)", "32.77"))
    b.append(p("Hệ số Seebeck tương đối tương ứng của cặp là:"))
    b.append(eq("<i>σ</i><sub>AB</sub>(<i>T</i><sub>m</sub>,<i>T</i><sub>r</sub>) = "
                "<i>σ</i><sub>A</sub>(<i>T</i><sub>m</sub>,<i>T</i><sub>r</sub>) − "
                "<i>σ</i><sub>B</sub>(<i>T</i><sub>m</sub>,<i>T</i><sub>r</sub>)", "32.78"))
    b.append(p(
        "Chính hệ số Seebeck tương đối này đã từng được gọi bằng thuật ngữ lỗi thời và không "
        "thích hợp “thermopower” [1]. Chính các giá trị tương đối về điện áp hay hệ số này là "
        "những giá trị quan sát trực tiếp được và thường được dùng trong đo nhiệt độ. Những đại "
        "lượng tương đối, được định nghĩa để tiện dùng trong các mạch nối tiếp của đo nhiệt độ, "
        "không có ý nghĩa chung cho các thân nhiệt điện mắc song song về điện [2]. Đây là những "
        "giá trị tương đối được trình bày trong các bảng quen thuộc về suất điện động cặp nhiệt "
        "điện theo nhiệt độ mối nối đo <i>T</i><sub>m</sub>, quy chiếu về nhiệt độ chuẩn quy định "
        "<i>T</i><sub>0</sub> = <i>T</i><sub>r</sub> [1, 4, 9-12]. Để tiện, "
        "<i>T</i><sub>0</sub> thường lấy bằng 0 °C, nhưng giá trị đó là tùy chọn."))

    b.append(h4("Mạch cặp nhiệt điện thực tế", "Realistic Thermocouple Circuits"))
    b.append(p(
        "Cặp nhiệt điện thường được biểu diễn chỉ như một cặp thân nhiệt điện khác nhau nối với "
        "nhau bằng hai mối nối trong một mạch kín. Một mối nối, ở nhiệt độ "
        "<i>T</i><sub>m</sub>, là mối nối đo; mối nối kia, ở nhiệt độ <i>T</i><sub>r</sub>, là "
        "mối nối chuẩn. Suất điện động Seebeck thuần tỉ lệ với chênh lệch nhiệt độ giữa hai mối "
        "nối và với một hệ số tương đối của cặp vật liệu."))
    b.append(p(
        "Hiện tượng Seebeck đã bị mô tả sai là sự xuất hiện dòng điện trong vòng kín. Bản chất "
        "thực của hiện tượng Seebeck là sự xuất hiện một suất điện động nguồn, mà để đo nhiệt độ "
        "chính xác phải đo ở chế độ hở mạch để triệt tiêu dòng điện. Trong đo nhiệt độ thực dụng, "
        "không có mạch cặp nhiệt điện thực tế nào chỉ có hai vật liệu khác nhau. Một số mạch có "
        "nhiều vật liệu và vài trong số đó có thể góp phần tạo ra suất điện động Seebeck. Các "
        "mạch đo nhiệt độ phổ biến nhất có hai mối nối chuẩn tách biệt, chứ không phải một. "
        "Những mạch hợp lệ nhưng hiếm gặp có thể đồng thời có nhiều hơn một nhiệt độ chuẩn [1]."))

    b.append(h4("Nhiệt độ chuẩn", "Reference Temperature"))
    b.append(p(
        "Nhiệt độ chuẩn thực <i>T</i><sub>r</sub> có thể khác với nhiệt độ chuẩn quy định "
        "<i>T</i><sub>0</sub> của quan hệ đặc trưng hóa. Nếu <i>T</i><sub>r</sub> không trùng "
        "với <i>T</i><sub>0</sub> thì, để dùng các hàm tỷ lệ chuẩn, suất điện động cặp nhiệt điện "
        "quan sát được phải được hiệu chỉnh theo chênh lệch nhiệt độ bằng cách cộng thêm một "
        "suất điện động tương đương <i>E</i><sub>AB</sub>(<i>T</i><sub>r</sub>) – "
        "<i>E</i><sub>AB</sub>(<i>T</i><sub>0</sub>) vào suất điện động cặp nhiệt điện quan sát "
        "được [1, 7, 9-12]. Việc này thường thực hiện bằng cách theo dõi "
        "<i>T</i><sub>r</sub> riêng biệt và áp dụng một hiệu chỉnh, theo cách số hoặc theo cách "
        "điện, dùng một quan hệ <i>E</i><sub>AB</sub>(<i>T</i>) cố định chỉ xấp xỉ quan hệ thực "
        "của cặp nhiệt điện và đặc trưng chuẩn hóa trong một khoảng giới hạn quanh "
        "<i>T</i><sub>0</sub> và <i>T</i><sub>r</sub>. Sai số do sự sai khác nhỏ giữa phép xấp "
        "xỉ và <i>E</i><sub>AB</sub>(<i>T</i>) thực tế là nhỏ nếu hai nhiệt độ gần nhau."))
    b.append(p(
        "Trong hầu hết đo nhiệt độ ứng dụng đều dùng các dây nối dài cặp nhiệt điện chuyên dụng. "
        "Nhiều cặp nhiệt điện chính trong công nghiệp được bọc vỏ kim loại cứng [1, 4, 10-12]. "
        "Những cặp khác có thân nhiệt điện trần cách nhau bằng các hạt cách điện. Thường thì "
        "những cụm lắp này được đặt trong ống bảo vệ, có mối nối đo kết cấu phức tạp, hoặc ở xa "
        "dụng cụ theo dõi. Các “đuôi ngắn” (pigtail) và dây nối dài có thể có tiết diện dây to "
        "hơn, điện trở thấp hơn, mềm dẻo hơn và kết cấu cáp bền bỉ khác hẳn so với cặp nhiệt điện "
        "chính (Hình 32.24). Mọi thân nhiệt điện phải được cách điện rất tốt, ngoại trừ tại các "
        "mối nối đo và mối nối chuẩn. Phần lớn đo nhiệt độ hiện đại được tiến hành với các biến "
        "thể của hai mạch cơ bản."))
    b.append(p(
        "<b>Mạch với một mối nối chuẩn đơn.</b> Hình 32.25 vẽ một mạch đo nhiệt độ hiện nay chủ "
        "yếu dùng trong các phòng hiệu chuẩn. Dạng này tiện khi dùng một chuẩn nhiệt độ điểm cố "
        "định như bình đá hay ống điểm ba của nước để áp đặt nhiệt độ chuẩn thực đã biết "
        "<i>T</i><sub>r</sub> [1, 7, 9-12]. Mạch của bộ chỉ thị cặp nhiệt điện giữa a và f chứa "
        "ngầm nhiều vật liệu thừa và mạch phức tạp bên trong dụng cụ. Cần có "
        "<i>T</i><sub>i</sub> = <i>T</i><sub>a</sub> = <i>T</i><sub>f</sub>. Trừ khi nhiệt độ "
        "các bộ phận của dụng cụ không đổi trong suốt phép đo, bất kỳ đoạn không đẳng nhiệt nào "
        "của mạch bên trong dụng cụ đều có thể góp phần tạo thành suất điện động Seebeck như "
        "nhiễu. Suất điện động này chỉ có thể bù đúng nếu nó không đổi."))
    b.append(p(
        "Thường, trong các mạch kiểu Hình 32.25, mối nối đo b của cặp nhiệt điện chính và mối nối "
        "chuẩn e được cung cấp bởi hai cặp nhiệt điện mua riêng a-b-c và d-e-f. Hai cặp này có "
        "thể có độ hiệu chuẩn khác nhau đáng kể dù trên danh nghĩa cùng thuộc một loại vật liệu "
        "cặp nhiệt điện. Với <i>T</i><sub>m</sub> ở 40 °C và <i>T</i><sub>0</sub> ở 0 °C, cặp "
        "nhiệt điện chuẩn d-e-f góp phần khoảng một nửa suất điện động Seebeck."))
    b.append(fig(25, F.fig(25), "vi"))
    b.append(p(
        "Mạch phổ biến này có ít nhất bốn vật liệu thân nhiệt điện phân biệt — A, A′, B và B′ — "
        "mà mỗi vật liệu đều phải đồng nhất. Chúng còn có thể được nối với nhau, như giữa c và d, "
        "bằng một vật liệu liên kết trung gian C chưa hiệu chuẩn (trừ khi "
        "<i>T</i><sub>c</sub> = <i>T</i><sub>d</sub>, vật liệu C sẽ góp một suất điện động "
        "Seebeck không mong muốn). Nếu B và B′ không giống nhau về đặc tính Seebeck thì c (và/hoặc "
        "d) là những mối nối thực. Khi đó, cũng cần có <i>T</i><sub>i</sub> = "
        "<i>T</i><sub>c</sub> = <i>T</i><sub>d</sub>. Các đầu mút a và f, khi nối vào bộ theo "
        "dõi, cũng trở thành những mối nối thực. Chúng phải được kiểm soát để cả hai luôn cùng "
        "nhiệt độ."))
    b.append(p(
        "Trong Hình 32.25, cho mục đích đo nhiệt độ, nhiệt độ chuẩn thực được mong muốn là "
        "<i>T</i><sub>r</sub> = <i>T</i><sub>e</sub>. Tuy vậy, các dụng cụ theo dõi tự bù nhiệt "
        "độ mối nối chuẩn bên trong coi (một cách sai, đối với mạch này) rằng "
        "<i>T</i><sub>r</sub> = <i>T</i><sub>a</sub> = <i>T</i><sub>f</sub>. Vì vậy, mạch một "
        "mối nối chuẩn của Hình 32.25 không thể dùng trực tiếp với các dụng cụ cặp nhiệt điện tự "
        "động áp dụng bù nhiệt độ mối nối chuẩn."))
    b.append(p(
        "<b>Mạch với hai mối nối chuẩn.</b> Trong nhiệt kế cặp nhiệt điện kiểu “hộp đen” đơn giản "
        "(Hình 32.24) cũng như trong phần lớn đo nhiệt độ nhiệt điện ứng dụng, mạch phổ biến nhất "
        "là mạch của Hình 32.26. Mạch này hiện là mạch thông dụng nhất trong đo nhiệt độ cặp nhiệt "
        "điện hiện đại. Cặp nhiệt điện c-d-e, với các thân nhiệt điện nối tại mối nối đo d, là "
        "<i>cặp nhiệt điện chính</i>. Mạch này có thể chỉ có cặp nhiệt điện chính với một phích "
        "và ổ cắm tại đầu vào của bộ chỉ thị. Thường hơn, như trong Hình 32.24, đầu dò cặp nhiệt "
        "điện chính tương đối cứng cũng có các dây nối dài mềm dẻo, cặp C-D, có thể ẩn bên trong "
        "vỏ bộ chỉ thị. Cặp nét đứt A′-B′ biểu diễn sơ đồ việc bù nhiệt độ mối nối chuẩn bên "
        "trong."))
    b.append(fig(26, F.fig(26), "vi"))
    b.append(p(
        "Các mạch kiểu Hình 32.26 có hai mối nối chuẩn tách biệt phải được giữ ở cùng một nhiệt "
        "độ đã biết. Điện áp Seebeck thuần đo ở chế độ hở mạch giữa b và f. Khi các dây cặp nhiệt "
        "điện C và D được nối vào bộ theo dõi, các cực đầu vào b-f có thể được coi là các mối nối "
        "chuẩn. Nếu vậy, nhiệt độ chuẩn của chúng được theo dõi chính xác và áp dụng hiệu chỉnh "
        "suất điện động chuẩn tương ứng với chênh lệch giữa <i>T</i><sub>r</sub> và "
        "<i>T</i><sub>0</sub>. Không thể đo cặp nhiệt điện chính xác bằng các voltmeter thông "
        "thường, nơi nhiệt độ của b và f không được kiểm soát chủ đích cho bằng nhau và đã biết."))

    b.append(h4("Dây nối dài", "Extension Leads"))
    b.append(p(
        "Cặp thân nhiệt điện C và D là các <i>dây nối dài</i> nhiệt điện. Dây nối dài có ba loại: "
        "(1) trung tính, (2) tương đồng (matching), và (3) bù (compensating). Cả ba loại đều có "
        "sẵn dễ dàng; một số là sản phẩm độc quyền. Những mối nối nào trong Hình 32.26 phải là "
        "mối nối chuẩn tùy theo loại dây nối dài. Tùy loại dây nối dài, các vật liệu A, B, C và "
        "D có thể, một cách chủ đích, rất khác nhau."))
    b.append(p(
        "<b>Dây nối dài trung tính.</b> Trong ứng dụng đơn giản nhất của Hình 32.26, các chân C "
        "và D đồng nhất về nhiệt điện và được ghép cặp cẩn thận có cùng hệ số Seebeck "
        "(<i>σ</i><sub>C</sub> = <i>σ</i><sub>D</sub>). Những cặp như vậy là dây nối dài trung "
        "tính. Với điều kiện <i>T</i><sub>c</sub> = <i>T</i><sub>e</sub> và "
        "<i>T</i><sub>b</sub> = <i>T</i><sub>f</sub>, chúng không góp suất điện động Seebeck "
        "thuần, nên cặp giống nhau này thực chất chỉ đóng vai trò dây dẫn “thụ động”. Vì vậy, các "
        "dây nối dài này có thể làm bằng bất kỳ vật liệu dẫn điện nào. Dây nối dài trung tính nên "
        "làm bằng đồng đặc không mạ, vốn có hệ số Seebeck nhỏ và đồng đều."))
    b.append(p(
        "Dây nối dài trung tính đòi hỏi các mối nối c và e phải là mối nối chuẩn ở nhiệt độ "
        "<i>T</i><sub>r</sub> = <i>T</i><sub>s</sub>. Các bộ theo dõi cặp nhiệt điện có bù nhiệt "
        "độ mối nối chuẩn tại các cực đầu vào b và f không thể dùng với dây nối dài trung tính."))
    b.append(p(
        "Nhiệt độ chuẩn có thể khống chế tại cả hai mối nối bằng một chuẩn nhiệt độ vật lý điểm "
        "cố định như bình đá đặt bên ngoài bộ đo điện áp [1, 9-12]. Những bình đá được làm và duy "
        "trì rất cẩn thận có thể đạt đều 0 °C trong khoảng 0,1 °C đến 0,2 °C [9, 11]. Nếu áp dụng "
        "và duy trì cẩu thả, chúng có thể lệch khỏi “nhiệt độ điểm đá” tới 4 °C [10]. Lạnh điện "
        "tử Peltier cũng được dùng. Thường hơn, trong đo nhiệt độ, nhiệt độ chuẩn không bị áp đặt "
        "về mặt vật lý. Thay vào đó, nhiệt độ thực của mối nối chuẩn được đo chính xác và bù "
        "bằng điện (sơ đồ bằng A′-B′) cho chênh lệch giữa <i>T</i><sub>r</sub> và "
        "<i>T</i><sub>0</sub>. Giá trị cụ thể của nhiệt độ tại b và f không quan trọng nếu "
        "<i>T</i><sub>b</sub> = <i>T</i><sub>f</sub> được bù."))
    b.append(p(
        "<b>Dây nối dài bổ trợ.</b> Có hai loại dây nối dài bổ trợ được phép góp phần vào suất "
        "điện động Seebeck của mạch: dây nối dài tương đồng và dây nối dài bù. Các chân C và D "
        "là dây nối dài nhiệt điện thường chưa hiệu chuẩn, và có thể có dải sai số rộng hơn, "
        "thậm chí không biết trước. Người ta mong <i>T</i><sub>s</sub> và "
        "<i>T</i><sub>i</sub> gần giống nhau để phần góp chưa hiệu chuẩn nhỏ và sai số không "
        "đáng kể. Với đo nhiệt độ rất chính xác, giả định này có thể không được bảo đảm."))
    b.append(p(
        "Dây nối dài bổ trợ có thể dùng trực tiếp với các bộ chỉ thị cặp nhiệt điện tự bù bên "
        "trong nhiệt độ mối nối chuẩn cho chênh lệch giữa nhiệt độ mối nối chuẩn thực "
        "<i>T</i><sub>r</sub> và nhiệt độ chuẩn quy định <i>T</i><sub>0</sub>. Với cả dây nối "
        "dài bổ trợ tương đồng lẫn bù, nhiệt độ chuẩn là <i>T</i><sub>r</sub> = "
        "<i>T</i><sub>i</sub> trên vùng chuẩn đẳng nhiệt bao quanh các cực b và f."))
    b.append(p(
        "<b>Dây nối dài tương đồng.</b> Dây nối dài tương đồng có <i>σ</i><sub>C</sub> = "
        "<i>σ</i><sub>A</sub> và cũng <i>σ</i><sub>D</sub> = <i>σ</i><sub>B</sub>. Điều cần "
        "thiết là <i>T</i><sub>b</sub> = <i>T</i><sub>e</sub>, nhưng không bắt buộc (dù mong "
        "muốn) <i>T</i><sub>c</sub> = <i>T</i><sub>e</sub>. Gần nhiệt độ phòng, các thân nhiệt "
        "điện được thiết kế để <i>σ</i><sub>CD</sub>, tính như một cặp, gần bằng "
        "<i>σ</i><sub>AB</sub> trong khoảng nhiệt độ gần <i>T</i><sub>r</sub>. Sai số do hiệu "
        "chuẩn của dây nối dài sai khác nhẹ và chưa được kiểm chứng được giảm thiểu nếu "
        "<i>T</i><sub>s</sub> &gt; <i>T</i><sub>i</sub>. Dây nối dài tương đồng dùng với cặp "
        "nhiệt điện kim loại thường, không dùng với cặp nhiệt điện kim loại chịu lửa hay kim "
        "loại quý."))
    b.append(p(
        "<b>Dây nối dài bù.</b> Biến thể thứ ba của mạch trong Hình 32.26 thường được dùng vì "
        "kinh tế và tiện lợi với các cặp nhiệt điện chính bằng kim loại quý và kim loại chịu lửa "
        "đắt tiền, vốn dùng ở nhiệt độ rất cao và trong môi trường đặc biệt [1, 7, 9-12]. Thường "
        "thì chỉ một phần cặp nhiệt điện chính cần tiếp xúc với môi trường khắc nghiệt. Dây nối "
        "dài C và D chỉ cần tồn tại được trong môi trường lành hơn. Vì vậy, chúng có thể làm "
        "bằng vật liệu rẻ hơn hoặc thuận tiện xử lý hơn, dùng cách điện chịu nhiệt thấp hơn, mềm "
        "dẻo hơn và có điện trở thấp hơn, thêm lớp che chắn cồng kềnh và bảo vệ cơ học, và kéo "
        "dài một quãng xa tới nơi ghi nhận."))
    b.append(p(
        "Dây nối dài bù có <i>σ</i><sub>CD</sub> của cặp C–D, chỉ tính như một cặp, khớp với "
        "<i>σ</i><sub>AB</sub> của cặp A–B. Không cần thiết vật liệu A giống C, cũng không cần C "
        "và D giống nhau. Một mạch thực dụng có thể có bốn vật liệu rất khác nhau. Tuy vậy, để "
        "cho phép điều đó, điều thiết yếu là <i>T</i><sub>c</sub> = <i>T</i><sub>e</sub>. Do đó, "
        "mạch với dây nối dài bù dễ mắc sai số do nhiệt độ các mối nối thừa không khớp hơn so "
        "với khi dùng dây nối dài tương đồng. Nhiệt độ mối nối chuẩn là "
        "<i>T</i><sub>r</sub> = <i>T</i><sub>b</sub> = <i>T</i><sub>f</sub>, và chỉ nhiệt độ này "
        "cần biết độc lập. Bù nhiệt độ mối nối chuẩn tiến hành giống như với dây nối dài tương "
        "đồng."))
    return "".join(b)


def sec_32_4b_en():
    b = [h3("Thermoelectric Effects", "Hiệu ứng nhiệt điện")]
    b.append(p(
        "The three thermoelectric phenomena are the Seebeck, Peltier, and Thomson effects "
        "[1, 2, 5-7]. Of these, only the Seebeck effect converts thermal energy to electric "
        "energy and results in the thermocouple voltage used in thermometry. The "
        "current-dependent Peltier and Thomson effects are insignificant in practical "
        "thermometry. Neither produces a voltage, contrary to common misconceptions. The Peltier "
        "and Thomson effects only transport heat by electric current and redistribute it around a "
        "circuit. Thermocouple thermometry is properly conducted by open-circuit measurement. The "
        "Seebeck emf occurs even without current where Peltier and Thomson effects necessarily "
        "vanish. Related thermo-magneto-electric effects are significant only in the presence of "
        "large magnetic fields and infrequently degrade applied thermoelectric thermometry "
        "[2, 5, 6]."))

    b.append(h4("The Seebeck Effect", "Hiệu ứng Seebeck"))
    b.append(p(
        "The Seebeck effect is the occurrence of a net source emf, the absolute Seebeck emf, "
        "between pairs of points in any individual electrically conducting material due to a "
        "difference of temperature between them [1, 2, 5, 7, 8]. The Seebeck emf occurs without "
        "dissimilar materials. It is not a junction phenomenon, nor is it related to Volta’s "
        "contact potential."))

    b.append(h4("Absolute Seebeck Properties", "Các đặc tính Seebeck tuyệt đối"))
    b.append(p(
        "The absolute Seebeck coefficient expresses the measurement sensitivity (volts per unit "
        "of temperature) of the Seebeck effect. It is defined over any thermoelectrically "
        "homogeneous region of a slender individual conducting material by:"))
    b.append(eq("<i>σ</i>(<i>T</i>) = lim<sub>Δ<i>T</i>→0</sub> "
                "Δ<i>E</i>(<i>T</i>) / Δ<i>T</i>", "32.73"))
    b.append(eq("d<i>E</i>(<i>T</i>) = <i>σ</i>(<i>T</i>) d<i>T</i>", "32.74"))
    b.append(p(
        "The Seebeck coefficient is a transport property of all electrically conducting "
        "materials. Equation 32.74 will be acknowledged later as the functional law that governs "
        "thermoelectric emf. From Equation 32.74,"))
    b.append(eq("Δ<i>E</i> = ∫<sub><i>T</i>1</sub><sup><i>T</i>2</sup> "
                "<i>σ</i>(<i>T</i>) d<i>T</i> = "
                "<i>E</i>(<i>T</i><sub>2</sub>) − <i>E</i>(<i>T</i><sub>1</sub>)", "32.75"))
    b.append(p(
        "where Δ<i>E</i> is the increment of emf between a pair of points, separated by any "
        "distance, between which the temperature difference is Δ<i>T</i> = "
        "(<i>T</i><sub>2</sub> – <i>T</i><sub>1</sub>)."))
    b.append(p(
        "From Equation 32.75, the net Seebeck effect for a particular material depends only on "
        "the temperatures at the two points and not on the values of temperature gradients "
        "between the two points. The Seebeck coefficient is a nonlinear function of temperature. "
        "It is not a constant. For accurate thermometry, the Seebeck coefficient must remain "
        "dependent on temperature alone. <i>σ</i>(<i>T</i>) cannot vary along a thermoelement, "
        "nor can it vary significantly during the time interval of use. Although vulnerable to "
        "such environmental effects, for accurate thermometry it must not depend during "
        "measurement on such environmental variables as strain, pressure, or magnetic field."))
    b.append(p(
        "The coefficient, <i>σ</i><sub>M</sub>(<i>T</i>), is an absolute Seebeck coefficient for "
        "an individual material M [1, 2, 7, 8]. A corresponding source voltage within a single "
        "material is an absolute Seebeck emf, <i>E</i><sub>M</sub>(<i>T</i>). The absolute "
        "Seebeck emf does physically exist but it is not simply observable. The absolute Seebeck "
        "coefficient can be determined indirectly by measuring the Thomson coefficient, "
        "<i>τ</i>, of the individual material and applying a Kelvin relationship,"))
    b.append(eq("<i>σ</i><sub>abs</sub>(<i>T</i>) = (1/<i>T</i>) "
                "∫<sub>0</sub><sup><i>T</i></sup> <i>τ</i><sub>abs</sub> d<i>T</i>", "32.76"))
    b.append(p(
        "to deduce the thermodynamically related Seebeck coefficient [1, 2, 5, 7, 8]."))

    b.append(h4("Relative Seebeck Properties", "Các đặc tính Seebeck tương đối"))
    b.append(p(
        "The difference between the Seebeck emfs of two thermoelements, of materials A and B, of "
        "a thermocouple with their shared junction at temperature <i>T</i><sub>m</sub> and both "
        "their termini at a physical reference temperature <i>T</i><sub>r</sub>, is their "
        "relative Seebeck emf, <i>E</i><sub>AB</sub>(<i>T</i>), expressed as:"))
    b.append(eq("<i>E</i><sub>AB</sub>(<i>T</i><sub>m</sub>,<i>T</i><sub>r</sub>) = "
                "<i>E</i><sub>A</sub>(<i>T</i><sub>m</sub>,<i>T</i><sub>r</sub>) − "
                "<i>E</i><sub>B</sub>(<i>T</i><sub>m</sub>,<i>T</i><sub>r</sub>)", "32.77"))
    b.append(p("The corresponding relative Seebeck coefficient for the pair is:"))
    b.append(eq("<i>σ</i><sub>AB</sub>(<i>T</i><sub>m</sub>,<i>T</i><sub>r</sub>) = "
                "<i>σ</i><sub>A</sub>(<i>T</i><sub>m</sub>,<i>T</i><sub>r</sub>) − "
                "<i>σ</i><sub>B</sub>(<i>T</i><sub>m</sub>,<i>T</i><sub>r</sub>)", "32.78"))
    b.append(p(
        "It is this relative Seebeck coefficient that has been called by the anachronistic and "
        "inept term “thermopower” [1]. It is these relative voltage or coefficient values that "
        "are directly observable and usually used in thermometry. These relative properties, "
        "defined for convenience in the series circuits of thermometry, have no general meaning "
        "for electrically paralleled thermoelements [2]. These are the relative values that are "
        "presented in the familiar tables of thermocouple emf vs. measuring junction temperature, "
        "<i>T</i><sub>m</sub>, referred to as a designated reference temperature "
        "<i>T</i><sub>0</sub> = <i>T</i><sub>r</sub> [1, 4, 9-12]. For convenience, "
        "<i>T</i><sub>0</sub> is usually taken as 0 °C, but the value is arbitrary."))

    b.append(h4("Realistic Thermocouple Circuits", "Mạch cặp nhiệt điện thực tế"))
    b.append(p(
        "The thermocouple is often represented as only a pair of dissimilar thermoelements "
        "joined by two junctions in a closed circuit. One junction, at temperature "
        "<i>T</i><sub>m</sub>, is the measuring junction; the other, at temperature "
        "<i>T</i><sub>r</sub>, is the reference junction. The net Seebeck emf is proportional to "
        "the temperature difference between the two junctions and to a relative coefficient for "
        "the paired materials."))
    b.append(p(
        "The Seebeck phenomenon has wrongly been characterized as the occurrence of current in "
        "the closed loop. The true nature of the Seebeck phenomenon is the occurrence of a source "
        "emf that, for accurate thermometry, must be measured in open-circuit mode that "
        "suppresses current. In practical thermometry, no realistic thermocouple circuit has only "
        "two dissimilar materials. Some have many and several of these can be expected to "
        "contribute some Seebeck emf. The most common thermometry circuits have two separate "
        "reference junctions, not one. Valid, but uncommon, circuits can simultaneously have more "
        "than one reference temperature [1]."))

    b.append(h4("Reference Temperature", "Nhiệt độ chuẩn"))
    b.append(p(
        "The physical reference temperature, <i>T</i><sub>r</sub>, can be different from the "
        "designated reference temperature, <i>T</i><sub>0</sub>, of the characterizing relation. "
        "If <i>T</i><sub>r</sub> is not identical to <i>T</i><sub>0</sub>, then, to use standard "
        "scaling functions, the observed thermocouple emf must be corrected for the temperature "
        "difference by adding an emf equivalent to "
        "<i>E</i><sub>AB</sub>(<i>T</i><sub>r</sub>) – <i>E</i><sub>AB</sub>(<i>T</i><sub>0</sub>) "
        "to the observed thermocouple emf [1, 7, 9-12]. This is often accomplished by separately "
        "monitoring <i>T</i><sub>r</sub> and applying a correction, either numerically or "
        "electrically, using a fixed <i>E</i><sub>AB</sub>(<i>T</i>) relation that only "
        "approximates that of the actual thermocouple and the standardized characteristic over a "
        "limited range in the vicinity of <i>T</i><sub>0</sub> and <i>T</i><sub>r</sub>. The "
        "error due to the slight discrepancy between the approximation and the actual "
        "<i>E</i><sub>AB</sub>(<i>T</i>) is small if the two temperatures are similar."))
    b.append(p(
        "Special thermocouple extension leads are used in most applied thermometry. Many "
        "industrial principal thermocouples are inflexibly metal sheathed [1, 4, 10-12]. Others "
        "have bare thermoelements separated by bead insulators. Often, these kinds of assemblies "
        "are housed in protective wells, have measuring junctions of complex construction, or are "
        "distant from the monitoring instrument. Short “pigtails” and extension leads can be of "
        "larger wire size, lower resistance, greater flexibility, and very different rugged cable "
        "construction than the principal thermocouple (Figure 32.24). All thermoelements must be "
        "very well electrically isolated except at measuring and reference junctions. Most modern "
        "thermometry is conducted with variants of two basic circuits."))
    b.append(p(
        "<b>Circuit with Single Reference Junction.</b> Figure 32.25 shows a thermometry circuit "
        "now used mostly in calibration laboratories. This form is convenient when a fixed point "
        "temperature reference such as an ice point bath or water triple point cell is used to "
        "impose the known physical reference temperature, <i>T</i><sub>r</sub> [1, 7, 9-12]. The "
        "circuit of the thermocouple indicator between a and f inconspicuously includes many "
        "incidental materials and complex circuitry within the instrument. It is necessary that "
        "<i>T</i><sub>i</sub> = <i>T</i><sub>a</sub> = <i>T</i><sub>f</sub>. Unless instrument "
        "temperatures are constant throughout measurement, any nonisothermal portion of the "
        "circuit within the instrument can contribute Seebeck emf as noise. This emf can be "
        "correctly offset only if it is constant."))
    b.append(p(
        "Often, in circuits like Figure 32.25, the measuring junction, b of the principal "
        "thermocouple, and reference junction, e, are provided by separately acquired "
        "thermocouples a-b-c and d-e-f. The two might have significantly different calibrations "
        "although they are nominally of the same thermocouple material type. With "
        "<i>T</i><sub>m</sub> at 40 °C and <i>T</i><sub>0</sub> at 0 °C the reference "
        "thermocouple d-e-f contributes about half the Seebeck emf."))
    b.append(fig(25, F.fig(25), "en"))
    b.append(p(
        "This commonplace circuit has at least four distinct thermoelement materials — A, A′, B, "
        "and B′ — each of which must be homogeneous. Also, they can be joined, as between c and "
        "d, by an intermediate uncalibrated linking material, C (unless <i>T</i><sub>c</sub> = "
        "<i>T</i><sub>d</sub>, material C contributes unwanted Seebeck emf). If B and B′ are not "
        "identical in Seebeck characteristics, then c (and/or d) are real junctions. If so, it is "
        "also necessary that <i>T</i><sub>i</sub> = <i>T</i><sub>c</sub> = "
        "<i>T</i><sub>d</sub>. The termini a and f, when connected to a monitor, also become real "
        "junctions. They must be controlled so that both stay at the same temperature."))
    b.append(p(
        "In Figure 32.25, for thermometry the physical reference temperature is intended to be "
        "<i>T</i><sub>r</sub> = <i>T</i><sub>e</sub>. However, monitoring instruments that "
        "internally compensate for reference junction temperature presume (incorrectly for this "
        "circuit) that <i>T</i><sub>r</sub> = <i>T</i><sub>a</sub> = <i>T</i><sub>f</sub>. "
        "Therefore, the single-reference circuit of Figure 32.25 cannot be used directly with "
        "thermocouple instruments that automatically apply reference junction temperature "
        "compensation."))
    b.append(p(
        "<b>Circuits with Dual Reference Junctions.</b> In the simple “black box” thermocouple "
        "thermometer (Figure 32.24), as well as in most applied thermoelectric thermometry, the "
        "most common circuit is that of Figure 32.26. This circuit is now the most commonly used "
        "in modern thermocouple thermometry. The thermocouple c-d-e with thermoelements joined at "
        "the measuring junction, d, is the <i>principal thermocouple</i>. This circuit might have "
        "only the principal thermocouple with a plug and jack at the indicator input. More often, "
        "as in Figure 32.24, the relatively inflexible principal thermocouple probe also has "
        "flexible extension leads, pair C-D, which can reside unseen within the indicator. Dashed "
        "pair A′-B′ schematically represents internal reference junction temperature "
        "compensation."))
    b.append(fig(26, F.fig(26), "en"))
    b.append(p(
        "Circuits like Figure 32.26 have two separate reference junctions that must be held at "
        "the same known temperature. Net Seebeck terminal voltage is measured in open-circuit "
        "mode between b and f. When thermocouple leads C and D are connected to the monitor, the "
        "input terminals, b-f, might be intended to be reference junctions. If so, their "
        "reference temperature is accurately monitored and emf reference correction corresponding "
        "to the difference between <i>T</i><sub>r</sub> and <i>T</i><sub>0</sub> is applied. "
        "Accurate thermocouple measurements cannot be made with ordinary voltmeters in which the "
        "temperatures of b and f are not deliberately controlled to be equal and known."))

    b.append(h4("Extension Leads", "Dây nối dài"))
    b.append(p(
        "Paired thermoelements C and D are thermoelectric <i>extension leads</i>. Extension leads "
        "are of three kinds: (1) neutral, (2) matching, and (3) compensating. All types are "
        "readily available; some are proprietary. Which of the junctions in Figure 32.26 must be "
        "reference junctions varies with the type of extension. Depending on the extension type, "
        "materials A, B, C, and D might, intentionally, all be of very different materials."))
    b.append(p(
        "<b>Neutral Extension Leads.</b> In the simplest application of Figure 32.26, legs C and "
        "D are thermoelectrically homogeneous and are carefully matched to have the same Seebeck "
        "coefficient (<i>σ</i><sub>C</sub> = <i>σ</i><sub>D</sub>). Such pairs are neutral "
        "extension leads. Provided that <i>T</i><sub>c</sub> = <i>T</i><sub>e</sub> and "
        "<i>T</i><sub>b</sub> = <i>T</i><sub>f</sub>, they contribute no net Seebeck emf, so the "
        "like pair effectively serve only as “passive” leads. Therefore, the leads could be made "
        "of any electrically conducting material. Such extension leads should be made of solid "
        "unplated copper, for which the Seebeck coefficient is small and uniform."))
    b.append(p(
        "Neutral extension leads require that junctions c and e be the reference junctions at "
        "temperature <i>T</i><sub>r</sub> = <i>T</i><sub>s</sub>. Thermocouple monitors that "
        "provide reference junction temperature compensation at input terminals b and f cannot be "
        "used with neutral extension leads."))
    b.append(p(
        "The reference temperature can be controlled on both junctions by a fixed point physical "
        "temperature reference such as an ice bath external to the voltage monitor [1, 9-12]. Ice "
        "baths, very carefully made and maintained, can routinely approximate 0 °C to within "
        "0.1 °C to 0.2 °C [9, 11]. Carelessly applied and maintained, they can deviate from the "
        "“icepoint temperature” by up to 4 °C [10]. Peltier thermoelectric refrigeration is also "
        "used. More often, in thermometry, that reference temperature is not physically imposed. "
        "Instead, the actual temperature of the reference junctions is accurately measured and "
        "electrical compensation is applied (schematically by A′-B′) for the difference between "
        "<i>T</i><sub>r</sub> and <i>T</i><sub>0</sub>. The particular value of the temperature "
        "at b and f does not matter if <i>T</i><sub>b</sub> = <i>T</i><sub>f</sub> is "
        "compensated."))
    b.append(p(
        "<b>Complementary Extension Leads.</b> Two kinds of complementary extension leads are "
        "allowed to contribute to the circuit Seebeck emf: matched and compensating extensions. "
        "The legs C and D are thermoelectric extension leads that are usually uncalibrated, and "
        "possibly are of broader or even unknown tolerance. It is expected that "
        "<i>T</i><sub>s</sub> and <i>T</i><sub>i</sub> are similar so that the uncalibrated "
        "contribution is small and the error is negligible. For very accurate thermometry, this "
        "assumption might not be justified."))
    b.append(p(
        "Complementary extension leads can be used directly with thermocouple indicators that "
        "internally compensate the reference junction temperature for the difference between the "
        "physical reference junction temperature, <i>T</i><sub>r</sub>, and the designated "
        "reference temperature, <i>T</i><sub>0</sub>. For both matched and compensating "
        "complementary extensions, the reference temperature is <i>T</i><sub>r</sub> = "
        "<i>T</i><sub>i</sub> over the isothermal reference zone around the terminals b and f."))
    b.append(p(
        "<b>Matching Extension Leads.</b> Matching leads have <i>σ</i><sub>C</sub> = "
        "<i>σ</i><sub>A</sub> and also <i>σ</i><sub>D</sub> = <i>σ</i><sub>B</sub>. It is "
        "essential that <i>T</i><sub>b</sub> = <i>T</i><sub>e</sub>, but it is not essential "
        "(although it is desirable) that <i>T</i><sub>c</sub> = <i>T</i><sub>e</sub>. Near room "
        "temperature, thermoelements are intended to have <i>σ</i><sub>CD</sub>, as a pair, be "
        "nearly the same as <i>σ</i><sub>AB</sub> for the temperature span near "
        "<i>T</i><sub>r</sub>. Error due to slightly mismatched and unproven calibration of the "
        "extension is minimized if <i>T</i><sub>s</sub> &gt; <i>T</i><sub>i</sub>. Matched "
        "extensions are used with base metal thermocouples, not with refractory or precious metal "
        "thermocouples."))
    b.append(p(
        "<b>Compensating Extension Leads.</b> The third variation of the circuit in Figure 32.26 "
        "is often used for economy and convenience with expensive precious and refractory metal "
        "principal thermocouples that are intended for use at very high temperatures and in "
        "special environments [1, 7, 9-12]. Usually, only a portion of the principal thermocouple "
        "need be exposed to the adverse environment. Extension leads C and D need only survive a "
        "more benign environment. Therefore, they can be made of a less expensive or more "
        "conveniently handled material, use lower temperature insulation, be more flexible and of "
        "lower resistance, add bulky shielding and mechanical protection, and extend a great "
        "distance to a recording facility."))
    b.append(p(
        "Compensating leads have <i>σ</i><sub>CD</sub> of the extension C–D, only as a pair, "
        "match <i>σ</i><sub>AB</sub> of the A–B pair. It is not necessary that material A be like "
        "C, nor that C and D be alike. A practical circuit can have four very dissimilar "
        "materials. However, to allow this, it is essential that <i>T</i><sub>c</sub> = "
        "<i>T</i><sub>e</sub>. Therefore, this circuit with compensating leads is more vulnerable "
        "to error from improperly matched temperatures of incidental junctions than with matching "
        "extension leads. The reference junction temperature is <i>T</i><sub>r</sub> = "
        "<i>T</i><sub>b</sub> = <i>T</i><sub>f</sub>, and only this temperature must be "
        "independently known. Reference junction compensation is the same as for the matching "
        "leads."))
    return "".join(b)


def sec_32_4c_vi():
    b = [h4("Các bộ phận điều chế tín hiệu dạng mô-đun",
            "Modular Signal Conditioning Components")]
    b.append(p(
        "Số lượng các bộ chỉ thị và máy ghi cặp nhiệt điện đa dạng và năng động hiện có trên thị "
        "trường — từ loại đơn giản, rất rẻ đến loại tinh vi, đa năng mà giá vẫn hợp lý — làm cho "
        "phần lớn đo nhiệt độ ứng dụng không cần phải lắp ráp các mạch điều chế tín hiệu đặc "
        "biệt. Một số người, muốn tiết kiệm phần cứng, đã tự dựng các hệ thống riêng. Quá thường "
        "xen, những hệ thống đó không đạt được phép đo chính xác và hóa ra rất đắt, bởi những "
        "điểm khác biệt then chốt giữa mạch nhiệt điện và mạch điện thông thường không được coi "
        "trọng. Với các tình huống đặc biệt cần đưa cặp nhiệt điện vào các bộ phận hay hệ thống "
        "đo hoặc vận hành chuyên dụng, vài nhà sản xuất hiện cung cấp các linh kiện dạng mô-đun "
        "và mạch tích hợp giúp đơn giản hóa ứng dụng đặc biệt và quả thật che chở người thiếu "
        "hiểu biết khỏi một số cạm bẫy [13]."))
    b.append(p(
        "<b>Điều chế tín hiệu cặp nhiệt điện trên một chip.</b> Vì tín hiệu cặp nhiệt điện ở "
        "mức thấp, đôi khi cần khuếch đại chúng để có độ phân giải, ghi nhận hay điều khiển tốt "
        "hơn. Có thể mong muốn đưa cảm biến cặp nhiệt điện vào làm một bộ phận chức năng trong "
        "các hộp dụng cụ khác. Hiện đã có một số mô-đun mạch tích hợp kiểu nhỏ gọn và rẻ tiền "
        "cho cặp nhiệt điện, cung cấp bù nhiệt độ mối nối chuẩn, tuyến tính hóa, cách ly, báo "
        "đầu vào hở, khuếch đại và điều khiển điểm đặt. Áp dụng đúng cách, chúng khiến việc tích "
        "hợp cảm biến cặp nhiệt điện vào các thiết bị khác, chẳng hạn bo thu thập dữ liệu máy "
        "tính, trở nên rất đơn giản [13]."))
    b.append(p(
        "Khi người dùng áp dụng các linh kiện mô-đun như vậy, việc hiểu và áp dụng mô hình mạch "
        "nhiệt điện đích thực và các nguyên lý đã trình bày trong phần “Mô hình chức năng của "
        "mạch nhiệt điện” đặc biệt quan trọng. Một số precaution mà các bộ theo dõi cặp nhiệt "
        "điện thương mại thường có sẵn thì người dùng phải tự cung cấp."))
    b.append(p(
        "<b>Cảm biến nhiệt độ chuẩn.</b> Cặp nhiệt điện tự sinh điện. Với phép đo nhiệt độ và "
        "đo nhiệt độ vi phân gần đúng thông thường, chúng không cần nguồn kích thích cũng như "
        "không cần nhiệt độ chuẩn. Với đo nhiệt độ chính xác, trừ khi nhiệt độ chuẩn đã biết "
        "được áp đặt về mặt vật lý, cần phải đo nhiệt độ mối nối chuẩn chính xác bằng một phương "
        "tiện độc lập. Việc cảm nhận này thường dùng RTD có nguồn cấp, nhiệt điện trở, transistor "
        "hoặc cảm biến mạch tích hợp [1, 4]."))
    b.append(p(
        "<b>Bộ bù nhiệt độ chuẩn.</b> Bù chuẩn đúng đắn đòi hỏi (1) thiết lập một vùng nhiệt độ "
        "đẳng nhiệt gồm cả các cực của cặp nhiệt điện, (2) cảm nhận nhiệt độ của vùng này, và "
        "(3) áp dụng một điện áp bù vật lý hoặc số vào điện áp cực của cặp nhiệt điện trước khi "
        "tỷ lệ hóa tổng điện áp thành nhiệt độ."))
    b.append(p(
        "Phương pháp tương tự đưa cảm biến nhiệt độ vùng trở kháng vào một cầu, điều biến phi "
        "tuyến một điện áp cấp theo một đường cong phi tuyến xấp xỉ của đặc tính "
        "<i>E</i>(<i>T</i>) của cặp nhiệt điện. Phương pháp này chỉ thích hợp để bù cho một loại "
        "cặp nhiệt điện duy nhất. Phương pháp thay thế chuyển đổi bằng số nhiệt độ chuẩn cảm "
        "nhận được thành giá trị điện áp bù thích hợp. Cách tiếp cận số cho phép áp dụng một "
        "điện áp bù riêng cho từng cặp nhiệt điện và cho các loại chuẩn khác nhau. Về nguyên "
        "tắc, để chính xác, điện áp bù bằng số có thể được người dùng lập trình tuân theo độ "
        "hiệu chuẩn cụ thể của từng cặp nhiệt điện, dù thuộc loại chuẩn hóa hay không."))
    b.append(p(
        "Bộ bù nhiệt độ chuẩn nằm bên trong các bộ theo dõi cặp nhiệt điện tiên tiến hơn. Trong "
        "các máy hiện đại, tám đến mười đầu vào cặp nhiệt điện được nhóm trên một cụm cực đẳng "
        "nhiệt tháo rời riêng, để có thể tháo ra hiệu chuẩn cảm biến chuẩn hoặc thay thế. Giống "
        "như cặp nhiệt điện, cảm biến chuẩn thỉnh thoảng trôi, gây sai số nhiệt độ đáng kể. Với "
        "phần lớn loại cặp nhiệt điện, sai số 1° ở nhiệt độ chuẩn tạo ra sai số tương tự ở "
        "nhiệt độ đo. Nhiều loại bộ bù mối nối chuẩn độc lập, cấp bằng pin hay điện lưới, một "
        "hay nhiều kênh, cũng có bán trên thị trường [4, 14]."))

    b.append(h4("Nối đất, che chắn và nhiễu", "Grounding, Shielding, and Noise"))
    b.append(p(
        "Các nguyên lý có cơ sở kỹ thuật vững chắc về kiểm soát nhiễu cho mạch điện cũng áp dụng "
        "cho mạch nhiệt điện [15, 16]. Tuy nhiên, có một số điểm cần cân nhắc thêm riêng cho "
        "mạch cặp nhiệt điện. Một số vấn đề kiểm soát nhiễu bắt nguồn từ bản chất của hiện "
        "tượng nhiệt điện; số khác bắt nguồn từ thông lệ thiết kế cặp nhiệt điện thương mại."))

    b.append(h5("Những vấn đề nhiễu riêng của cặp nhiệt điện",
                "Noise Problems Peculiar to Thermocouples"))
    b.append(p(
        "Việc kiểm soát nhiệt độ của mọi mối nối và linh kiện chủ đích cũng như vô ý, và bản "
        "chất phân bố của nguồn suất điện động Seebeck, không thể bỏ qua mà không phải trả giá "
        "trong ứng dụng cặp nhiệt điện. Những yêu cầu tất yếu của sự kiểm soát đó được trực "
        "quan hóa tốt nhất bằng các phương pháp sẽ nêu sau trong phần “Mô hình chức năng của "
        "mạch nhiệt điện”. Các linh kiện mạch thừa như điện trở cân bằng hoặc hạn dòng, cực "
        "nối xuyên (feedthru), mối ghép và dải cực, vốn không nhằm góp suất điện động Seebeck, "
        "phải được chủ đích duy trì đẳng nhiệt. Các lớp che chắn, tất yếu không đẳng nhiệt, khi "
        "được nối chung điện với cặp nhiệt điện phải được thừa nhận rõ ràng là nguồn tiềm ẩn "
        "của nhiễu một chiều ngẫu nhiên, góp phần tạo suất điện động Seebeck nếu không nối "
        "đúng."))
    b.append(p(
        "<b>Nhiễu điện từ (EM).</b> Trong các đầu dò cặp nhiệt điện kết cấu cách điện khoáng – "
        "vỏ kim loại (MIMS), các cặp nhiệt điện cách điện bằng cúc gốm, và trong một số loại "
        "dây cặp nhiệt điện có vỏ cách điện ghép cặp, các thân nhiệt điện ghép cặp không bị xoán "
        "và cách nhau khá xa. Các đầu dò cặp nhiệt điện dài và đường kính lớn tạo thành một diện "
        "tích vòng mạch đáng kể để ghép các trường nhiễu từ. Ngay cả khi đầu dò được bọc hoàn "
        "toàn bằng kim loại, các vỏ chuẩn hóa rất mỏng và có độ từ thẩm thấp. Chúng gần như "
        "không hiệu quả để che chắn điện từ (EM). Những đặc điểm này ngăn cản việc dùng một số "
        "kỹ thuật cổ điển để khử nhiễu EM [15, 16]. Để giảm nhiễu EM gây khó chịu, đầu dò cặp "
        "nhiệt điện chính nên có đường kính nhỏ nhất thực dụng và chiều dài ngắn nhất. Trong "
        "những trường hợp nguồn EM ở cục bộ và xác định được, có thể sắp xếp hướng của đầu d so "
        "với nguồn để giảm thiểu ghép EM. Để khử nhiễu EM, dây nối dài luôn luôn nên có kết cấu "
        "dây đôi xoán, với bước xoán nhỏ đủ để khử nhiễu tần số cao [15]."))
    b.append(p(
        "<b>Nhiễu tĩnh điện (ES).</b> Nhiễu tĩnh điện dễ khử hơn. Lớp che chắn trở kháng thấp, "
        "dù mỏng, có thể hiệu quả nếu nối đúng [15, 16]. Dây bện đồng mạ thường được dùng và "
        "hiệu quả với nhiễu tần số trung bình. Các lớp che liền mạch, như vỏ MIMS và màng "
        "mylar nhôm hóa, hiệu quả với nhiễu ES tần số thấp và hiệu quả hơn lớp bện đối với "
        "nhiễu tần số rất cao. Lớp che tĩnh điện phải liền mạch (không có khe hở và lỗ như dây "
        "bện) để đạt hiệu quả tối đa. Lợi ích tối ưu từ che chắn đòi hỏi dùng cùng các bộ theo "
        "dõi cặp nhiệt điện có đầu vào ba dây và bộ ghép kênh chuyển cả cặp tín hiệu lẫn dây "
        "che riêng của chúng, riêng cho từng cặp nhiệt điện."))

    b.append(h5("Nối đất", "Grounding"))
    b.append(p(
        "Che chắn chống nhiễu ES và xoán đôi chống nhiễu EM quan trọng để giảm nhiễu tần số "
        "cao. Một lớp che tổng thứ cấp, cách ly với các lớp che trong và nối đất riêng, có thể "
        "cải thiện khả năng khử nhiễu EM. Nối đất mạch thích hợp cũng đặc biệt quan trọng cho "
        "cả khống chế EM lẫn ES tần số cao, nhưng còn có ý nghĩa hơn nữa đối với nhiễu tần số "
        "thấp và nhiễu một chiều, vốn thường nặng nề hơn trong phép đo cặp nhiệt điện. Nối đất "
        "thích hợp trở nên phức tạp khi cần tiếp xúc nhiệt sát sao giữa mối nối đo với vật thể "
        "thử dẫn điện đã nối đất để đo quá độ nhanh hoặc để chính xác khi có gradient nhiệt độ "
        "tĩnh."))
    b.append(p(
        "Hình 32.27 minh họa cách nối đất thích hợp cho một số trong vô số tình huống có thể "
        "xảy ra. Mạch cặp nhiệt điện mức thấp chỉ nên nối đất tại một điểm quy chiếu điện duy "
        "nhất. Vì mối nối đo không phải là một vị trí có nguồn suất điện động tập trung, điểm "
        "nối đất phải được cân nhắc cẩn thận. Không bao giờ được nối đất tại bất kỳ điểm nào "
        "của mạch cặp nhiệt điện ngoài mối nối đo hoặc mối nối chuẩn. Tiếp xúc điện, đặc biệt "
        "là phân lưu hay ngắn mạch, trên một thân nhiệt điện tại bất kỳ điểm nào giữa mối nối "
        "đo và mối nối chuẩn thường đưa vào suất điện động Seebeck giả từ các thân nhiệt điện "
        "thừa không được nhận biết."))
    b.append(fig(27, F.fig(27), "vi"))
    b.append(p(
        "Cách nối đất cho phép có thể do thiết kế nội tại của bộ theo dõi và logger dữ liệu quy "
        "định. Mỗi thiết kế dụng cụ giải quyết kiểm soát nhiễu theo một cách riêng. Các nhiệt "
        "kế cặp nhiệt điện đơn giản, rẻ tiền, cấp điện lưới có thể chỉ có đầu vào đơn cực với "
        "dây âm nối nội bộ vào đất nguồn. Điều đó buộc việc nối đất cảm biến cũng phải quy "
        "chiếu về đất nguồn. Kiểu mối nối nối đất cũng có thể cần cho đo quá độ nhanh. Trong sử "
        "dụng, cặp nhiệt điện vốn cách ly có thể bị ngắn sang vỏ bảo vệ hay vật thể thử. Dù "
        "điều đó làm thay đổi cấu hình nối đất, các sai số do hiệu ứng khác thường khi đó "
        "chiếm ưu thế."))

    b.append(h5("Mạch cặp nhiệt điện cân bằng", "Balanced Thermocouple Circuits"))
    b.append(p(
        "Các hệ thu thập dữ liệu đa kênh tinh vi hơn chuyên cho đo nhiệt độ cặp nhiệt điện "
        "thường có đầu vào cân bằng trở kháng cao để khử tín hiệu chung (common-mode) tốt. Một "
        "số bộ khuếch đại đầu vào vi phân cần điện trở đầu vào đáng kể để ổn định. Phần lớn có "
        "khung nội tại tạo một mặt bảo vệ quy chiếu tín hiệu chung, cách ly tốt với đất nguồn. "
        "Trong vài thiết kế, mặt bảo vệ được kéo điện về một điểm quy chiếu cụ thể. Vì dùng "
        "nhiều biến thể khác nhau, điều khôn ngoan là nghiên cứu và tuân theo các chỉ dẫn nối "
        "đất cụ thể khuyến nghị trong sổ tay sử dụng của dụng cụ. Phần lớn chấp nhận các cách "
        "nối đất thay thế."))
    b.append(p(
        "Trong các đầu dò có vỏ với kích thước MIMS chuẩn, các thân nhiệt điện cùng tiết diện, "
        "song song và cách xa nhau, nằm đối xứng trong vỏ trụ [10]. Nhiễu có xu hướng ghép bằng "
        "nhau vào cặp thân nhiệt điện theo chế độ chung. Tuy vậy, cặp nhiệt điện dài hoặc cỡ "
        "mảnh có các chân có điện trở cao so với mạch đồng. Tỷ lệ giữa điện trở của hai chân "
        "khác nhau có thể tới 25:1. Nhiễu đưa vào theo chế độ chung xấu thay có xu hướng chuyển "
        "thành chế độ bình thường."))
    b.append(p(
        "Ngoài ra, khác với phần lớn nguồn điện áp, suất điện động Seebeck không tập trung tại "
        "mối nối đo (một mặt tiếp xúc vật liệu). Suất điện động có thể phát sinh ở bất kỳ đâu "
        "dọc theo thân nhiệt điện. Trong đo quá độ, nó phát sinh kề cận mối nối đo rồi lan xa "
        "dần. Trong đo tĩnh phổ biến hơn, vị trí nguồn suất điện động thường ở xa mối nối đo."))
    b.append(p(
        "Phần lớn máy ghi cặp nhiệt điện chuyên dụng có bù nhiệt độ chuẩn. Chúng không cho "
        "người dùng truy cập thuận tiện vào mạch phía sau các mối nối chuẩn. Điều đó hạn chế "
        "các phương pháp kiểm soát nhiễu sẵn có cho người dùng. Với cặp nhiệt điện quy chiếu "
        "bên ngoài, một số biến đổi mạch đơn giản mà hiệu quả là khả thi. Hình 32.28 cho thấy "
        "việc thêm ba điện trở, dùng với các bộ theo dõi đầu vào cân bằng, cải thiện khử nhiễu. "
        "Điện trở cân bằng đẳng nhiệt R<sub>c</sub> = R<sub>a</sub> – R<sub>b</sub> được thêm "
        "nối tiếp với thân nhiệt điện có điện trở thấp hơn. Việc làm cho điện trở của hai nhánh "
        "mạch bằng nhau giảm sự chuyển hóa nhiễu không mong muốn từ chế độ chung sang chế độ "
        "bình thường. Cặp điện trở phân lưu khớp nhau R<sub>s</sub> tạo ra một điện trở nguồn "
        "cực tiểu xác định đáng kể cho đầu vào bộ khuếch đại nhằm ổn định, và ghép tín hiệu và "
        "vỏ một cách đối xứng về điểm quy chiếu chung. Các điện trở phải đủ lớn, "
        "R<sub>s</sub> ≥ 1000 (R<sub>a</sub> + R<sub>b</sub>), để tránh sự suy giảm phân lưu "
        "điện trở đáng kể suất điện động Seebeck nguồn của cặp nhiệt điện. Với sự cẩn trọng "
        "giữ các điện trở này nghiêm ngặt đẳng nhiệt, các điện trở cân bằng và phân lưu có thể "
        "đặt ngay tại các cực đầu vào, bên ngoài phần bù nhiệt độ mối nối chuẩn do dụng cụ "
        "cung cấp."))
    b.append(fig(28, F.fig(28), "vi"))

    b.append(h5("Lọc", "Filtering"))
    b.append(p(
        "Với đo nhiệt độ tần số thấp, để bổ sung cho việc khử thụ động nhiễu EM và ES do người "
        "dùng thực hiện bằng nối đất và che chắn đúng, bộ lọc nội tại do nhà sản xuất bộ thu "
        "thập dữ liệu cung cấp có thể khử hiệu quả nhiễu tần số cao. Lọc trước khi ghi nhận là "
        "ưu tiên. Việc khống chế này có thể thực hiện bằng bộ lọc thông thường; nhưng với phép "
        "đo cặp nhiệt điện gần tĩnh, một số thiết kế còn cung cấp các kỹ thuật rất hiệu quả "
        "khác như “tích hợp dốc kép”. Các kỹ thuật này thực chất lấy trung bình tín hiệu qua "
        "vài mẫu đo. Khả năng giảm nhiễu và ổn định trong điều kiện thực tế là đáng nể. Độ "
        "phân giải và độ ổn định thông thường tới 0,1 µV biến thiên trong nhiều ngày đạt được "
        "bởi nhiều logger dữ liệu cặp nhiệt điện hiện đại. Tuy vậy, phương pháp khử nhiễu này "
        "hạn chế tốc độ lấy mẫu, sao cho các mẫu có thể bị giới hạn ở khoảng cách không ngắn "
        "hơn 10 ms đến 20 ms, không thích hợp cho đo quá độ rất nhanh."))

    b.append(h4("Ghép nhiệt", "Thermal Coupling"))
    b.append(p(
        "Đo nhiệt độ chính xác tất yếu đòi hỏi nhiệt độ của các mối nối đo cặp nhiệt điện phải "
        "khớp gần với nhiệt độ cần đo. Trong phép đo tĩnh tại trạng thái cân bằng nhiệt, điều "
        "này thường dễ đạt được. Trong phép đo quá độ nhanh, điều này có thể rất khó."))
    b.append(h5("Đo nhiệt độ tĩnh", "Static Thermometry"))
    b.append(p(
        "Đo nhiệt độ cặp nhiệt điện cho nhiệt độ ổn định hoặc biến thiên chậm đòi hỏi ghép nhiệt "
        "sát sao giữa các mối nối đo với điểm đo. Sự khớp nhiệt độ này tự nhiên xảy ra nhờ cân "
        "bằng nếu điểm đo có thể chọn nằm sâu trong một vùng giữ nhiệt độ đồng nhất trong suốt "
        "phép đo. Ngay cả trong đo nhiệt độ gần tĩnh như vậy, các thân nhiệt điện cũng nên nhỏ "
        "nhất có thể để giảm bất kỳ sự dẫn nhiệt nào dọc theo cặp nhiệt điện có thể ảnh hưởng "
        "đến nhiệt độ đang đo."))
    b.append(p(
        "Tuy nhiên, trong các tình huống điển hình, vùng lân cận điểm đo không đẳng nhiệt và, "
        "ngay cả ở trạng thái ổn định, gradient nhiệt độ tĩnh có thể khiến mối nối đo ở nhiệt "
        "độ khác đáng kể với vật thể [18]. Nguồn sai số này nặng hơn đối với phép đo bề mặt, "
        "chất lỏng và khí so với phép đo trong khối rắn, và trầm trọng hơn khi đo các vật thể "
        "có khối nhiệt thấp. Ghép nhiệt hiệu quả giữa cặp nhiệt điện và vật thể, như trong "
        "Hình 32.27, là thiết yếu."))
    b.append(p(
        "Nhiễu hay an toàn có thể đòi hỏi cách ly điện của cặp nhiệt điện. Các vật liệu cách điện "
        "thông thường đều dẫn nhiệt kém. Hiện đã có các loại mỡ, lớp phủ và vật liệu tấm mỏng "
        "đặc biệt được thiết kế để cung cấp cách điện cao mà vẫn tiếp xúc nhiệt tốt [17]. Khi "
        "cần, chúng có thể cải thiện độ chính xác bằng ghép nhiệt hiệu quả."))
    b.append(h5("Đo nhiệt độ quá độ", "Transient Thermometry"))
    b.append(p(
        "Theo dõi các biến thiên nhiệt độ rất nhanh đạt hiệu quả nhất bằng cặp nhiệt điện nhờ "
        "khối lượng cảm nhận thấp và kích thước nhỏ của mối nối đo mà chúng cho phép. Phản ứng "
        "nhanh đòi hỏi dùng các cấu hình thân nhiệt điện đặc biệt gần mối nối đo, mạch đặc "
        "biệt, dụng cụ theo dõi cặp nhiệt điện đặc biệt, và các phương pháp đặc trưng hóa "
        "[16, 18]. Một số nhà cung cấp chào bán các cặp nhiệt điện lá rất mỏng (dày 10 µm) và "
        "dây mảnh đặc biệt thích hợp cho phép đo như vậy [19, 20]."))
    b.append(p(
        "Một mình cặp nhiệt điện không có thời gian đáp ứng đặc trưng. Hiệu ứng Seebeck xảy ra "
        "với tốc độ điện tử. Suất điện động nguồn của cặp nhiệt điện luôn lập tức tương ứng với "
        "nhiệt độ của mọi mối nối trong mạch. Tuy vậy, đáp ứng nhiệt độ quá độ của một lắp đặt "
        "cặp nhiệt điện chậm hơn nhiều, và chủ yếu do tương tác nhiệt giữa các bộ phận cặp nhiệt "
        "điện kề cận mối nối và khối lượng kề cận của vật thể thử chi phối [18, 22, 23]. Sự "
        "truyền nhiệt dẫn chậm đó bị trì hoãn nhiều lần chỉ bởi một lớp mỏng không khí, chân "
        "không, hay lớp rắn cách nhiệt. Trong đo quá độ nhanh, các tham số điện của cặp nhiệt "
        "điện và mạch liên quan cùng đáp ứng động của hệ ghi nhận có thể làm phản ứng thời gian "
        "xấu thêm."))
    b.append(p(
        "Ghép nhiệt sát sao bằng vật liệu đặc biệt, cần cho phép đo tĩnh trong gradient nhiệt, "
        "còn quan trọng hơn đối với đo quá độ so với đo tĩnh [17]. Ngay cả các vật liệu ghép "
        "đặc biệt cũng làm chậm phản ứng. Chúng nên mỏng nhất có thể. Với đo nhiệt độ rất "
        "nhanh, sự ghép như vậy có thể không chấp nhận được. Có thể cần đặt mối nối đo trần "
        "tiếp xúc điện trực tiếp với vật thể (Hình 32.27)."))
    b.append(p(
        "<b>Cặp nhiệt điện nội tại.</b> Khi vật thể đo là vật dẫn điện, có thể hàn điện hai "
        "thân nhiệt điện riêng biệt lên vật thể thử. Đây là kiểu mối nối cặp nhiệt điện “nội "
        "tại”. Dây mảnh hay lá mỏng hàn điểm lên vật thể cho phép đáp ứng điện – nhiệt nhanh "
        "nhất có thể và giảm ảnh hưởng của cặp nhiệt điện lên nhiệt độ đang đo."))
    b.append(p(
        "Lưu ý hai precaution đặc biệt khi dùng mối nối nội tại. Thứ nhất, hai thân nhiệt điện "
        "nên được hàn lên vật thể cạnh nhau, gần nhau (không đè lên nhau). Với mối nối nội "
        "tại, đoạn cầu nối của vật thể trở thành một phần của mạch nhiệt điện nối tiếp (có hai "
        "mối nối nội tại ghép nối bởi vật liệu vật thể trung gian). Điều này cho phản ứng nhanh "
        "nhất; nhưng trong quá độ rất nhanh, nhiệt độ của hai mối nối có thể trong khoảnh khắc "
        "ngắn hơi khác nhau và vì vậy gây sai số chốc lát, do hệ số Seebeck chưa biết của vật "
        "liệu cầu nối khác với hệ số của một hoặc cả hai thân nhiệt điện chính [21]."))
    b.append(p(
        "Thứ hai, với đo quá độ, các thân nhiệt điện mảnh dẫn tới các mối nối nội tại nên ngắn "
        "và mảnh nhất có thể để giảm tải nhiệt của chúng; tuy vậy, điều này dẫn đến điện trở "
        "dây dẫn tương đối cao. Nên tạo một chuyển tiếp chống ứng suất từ các sợi mảnh sang "
        "các dây dẫn bù vững chắc hơn, điện trở thấp hơn, gần mối nối đo để cải thiện đáp ứng "
        "điện. Hiệu ứng điện của ghép tụ điện của mạch lên đáp ứng quá độ điện cũng phải được "
        "giảm thiểu."))
    b.append(p(
        "<b>Hiệu chỉnh bằng số.</b> Mọi kỹ thuật vật lý khả thi để đạt phản ứng nhiệt độ quá độ "
        "nhanh, khi áp dụng, có thể vẫn chưa đủ cho một phép đo rất nhanh. Đáp ứng quá độ chưa "
        "đạt có thể cải thiện thêm bằng phân tích số [21]. Phải thực hiện thêm hai bước."))
    b.append(p(
        "Thứ nhất, phải thực hiện một đặc trưng hóa đáp ứng quá độ xác thực, bằng thực nghiệm "
        "hoặc mô hình hóa đúng, của toàn hệ thống đo nhiệt độ nhiệt – điện. Các biểu diễn bậc "
        "một đơn giản hóa thường gặp cho đáp ứng cặp nhiệt điện tại chỗ có thể không đủ "
        "[21-23]."))
    b.append(p(
        "Thứ hai, đặc trưng hóa xác thực này phải được áp dụng bằng phép khử tích chập toán học "
        "để ước lượng tốt hơn lịch sử nhiệt độ thực của dữ liệu do một hệ có đáp ứng quá độ vật "
        "lý chưa đạt chỉ ra [16, 19]. Các cải thiện quan trọng và tin cậy của thời gian đáp ứng "
        "hiệu quả gấp bốn lần trở lên thường khả thi. Nếu không hiệu chỉnh, nhiệt độ đỉnh quá độ "
        "chỉ ra có thể sai lệch với phần trăm lớn hơn nhiều so với sai số do hiệu chuẩn tĩnh của "
        "cặp nhiệt điện. Không thể gán một độ không đảm bảo chung cho phép đo quá độ nếu thiếu "
        "đặc trưng hóa phản ứng như vậy."))
    return "".join(b)


def sec_32_4d_vi():
    b = [h3("Vật liệu cặp nhiệt điện", "Thermocouple Materials")]

    b.append(h4("Chuẩn hóa cặp nhiệt điện", "Thermocouple Standardization"))
    b.append(p(
        "Nhiều vật liệu được dùng thường xuyên làm cặp nhiệt điện cho đo nhiệt độ. Một số cặp "
        "được chuẩn hóa; một số thì không. Sự phân biệt này là vấn đề phê duyệt chính thức của "
        "nhóm đồng thuận, do các ủy ban tiêu chuẩn cân bằng gồm người dùng giàu kinh nghiệm, nhà "
        "sản xuất và cán bộ phòng chuẩn biểu quyết [10, 24]. Dữ liệu ứng dụng đầy đủ nhất hiện có "
        "cho các cặp nhiệt điện đã chuẩn hóa. Ở Hoa Kỳ, tám vật liệu hiện được ký hiệu chữ cái "
        "(các loại B, E, J, K, N, R, S và T) [9–12, 24]. Một số đặc tính của chúng được tóm tắt "
        "trong Bảng 32.12. Đặc tính <i>E</i>(<i>T</i>) chuẩn hóa của các loại này nay được xác "
        "định chính xác bằng các hàm đa thức bậc cao thay vì bằng các bảng tra số liệu [1, 9, 10]. "
        "Các thân nhiệt điện nên được dùng theo kiểu do nhà sản xuất ghép chọn lọc, vì các thân "
        "nhiệt điện cùng loại được ghép ngẫu nhiên, dù cùng hay khác nhà sản xuất, không được bảo "
        "đảm tuân theo giá trị hay dung sai của cặp chuẩn [1, 9–12]. Đặc tính của một số cặp phổ "
        "biến khác, như hợp kim kim loại quý và hợp kim chống chịu nhiệt vonfram, cũng đã được "
        "các ủy ban đề xuất, nhưng ký hiệu chữ cái và mã màu chưa được ấn định chính thức [10]. "
        "Thỉnh thoảng, các vật liệu phổ biến khác cũng được xem xét để chuẩn hóa. Thông tin hạn "
        "chế về Seebeck và ứng dụng hiện có cho rất nhiều vật liệu phi chuẩn [25, 26]."))

    b.append(h4("Đo nhiệt độ thấp", "Low Temperature Thermometry"))
    b.append(p(
        "Phần lớn đo nhiệt độ ở nhiệt độ cao. Phép đo cặp nhiệt điện các nhiệt độ dưới điểm đá "
        "đòi hỏi cân nhắc đặc biệt. Đo nhiệt độ sâu lạnh từng được định nghĩa rất đại khái là "
        "phép đo dưới 280 K (7 °C) [1]. Theo nghĩa hẹp hơn, dải sâu lạnh được giới hạn dưới 90 K "
        "(−183 °C, nhiệt độ sôi của oxy lỏng tại 1 atm) [1]. Định nghĩa trước rộng ra và chồng "
        "lấn lên dải nhiệt độ khí quyển (xuống tới −50 °C) dưới điểm đá, vốn thường được đo bằng "
        "một hệ cặp nhiệt điện duy nhất cùng với các nhiệt độ môi trường cao hơn. Định nghĩa sau "
        "thiên về chỉ gọi là sâu lạnh dải nhiệt độ cực thấp mà phép đo ở đó gặp những vấn đề "
        "nghiêm trọng đặc thù và cần các kỹ thuật khác biệt."))
    b.append(p(
        "Hệ số Seebeck của mọi vật dẫn không đáng kể ở 0 K và các vật liệu thông thường giảm dần "
        "độ nhạy nhiệt điện dưới điểm đá. Một số ít thân kim loại siêu dẫn tự nhiên trải qua sự "
        "sụt đột ngột của hệ số Seebeck xuống bằng không tại một ngưỡng siêu dẫn đặc trưng, dưới "
        "10 K với phần lớn siêu dẫn kim loại không hợp kim [27]. Các hợp kim đặc biệt mới đây đã "
        "được phát triển để nâng ngưỡng siêu dẫn lên khoảng 120 K — cao hơn hẳn dải sâu lạnh chính "
        "thức. Các chuyển pha siêu dẫn làm phức tạp thêm phép đo nhiệt điện ở vùng sâu lạnh thấp "
        "nhất [7, 8]."))
    b.append(_t3212("vi"))
    b.append(p(
        "Đặc tính Seebeck chuẩn được xác định cho các loại E, J, K, N và T xuống tới −270 °C. "
        "Đặc tính của loại R và S chỉ kéo xuống tới −50 °C, còn loại B không được đặc trưng hóa "
        "dưới 0 °C. Các đa thức chuẩn xác định đặc tính Seebeck của cặp nhiệt điện ký hiệu chữ "
        "cái và các dung sai sản xuất của vật liệu thương mại khác nhau cho vùng dưới và trên "
        "điểm đá. Vật liệu sản xuất cho đo nhiệt độ cao có thể tuân theo đặc tính sâu lạnh chuẩn "
        "kém hơn các hợp kim cùng loại được cung cấp đặc biệt cho mục đích đó [1]. Vấn đề chất "
        "lượng này nên trao đổi với nhà cung cấp cặp nhiệt điện. Các hợp kim đặc biệt cho đo "
        "nhiệt độ sâu lạnh hiện có bán."))
    b.append(p(
        "Ở dải sâu lạnh thấp hơn, trong số các vật liệu ký hiệu chữ cái, loại E được ưa dùng cho "
        "phép đo xuống tới −233 °C (40 K) nhờ hệ số Seebeck tương đối cao hơn [1]. Loại K và T "
        "kém nhạy hơn cũng được dùng trong dải này. Dưới 40 K, người ta khuyến nghị các tổ hợp "
        "hợp kim đặc biệt, chẳng hạn loại KP với Au/0,07 Fe. Các quan hệ nhiệt điện đặc biệt áp "
        "dụng cho các vật liệu này trong dải sâu lạnh [1]."))
    b.append(p(
        "Nhiệt Peltier tại các mối nối và nhiệt Thomson dọc theo thân nhiệt điện là các hiệu ứng "
        "nhiệt điện phụ thuộc dòng điện; không hiệu ứng nào đáng kể nếu phép đo được tiến hành "
        "đúng đắn ở chế độ hở mạch. Không có hiện tượng tự sinh nhiệt đáng kể của cặp nhiệt điện "
        "như ở nhiệt điện trở."))
    b.append(p(
        "Một số hợp kim thân nhiệt điện trải qua hiện tượng lớn hạt và hình thành sự không đồng "
        "nhất nghiêm trọng khi tiếp xúc kéo dài với nhiệt độ sâu lạnh sâu. Nhạy hơn ở nhiệt độ sâu lạnh "
        "so với nhiệt độ cao, hệ số Seebeck của phần lớn hợp kim cặp nhiệt điện phụ thuộc rất "
        "mạnh vào từ trường. Từ trường mạnh thường hiện diện trong thí nghiệm sâu lạnh, nên các "
        "hiệu ứng nhiệt – từ – điện trở nên đáng kể trong nghiên cứu siêu dẫn [2, 27]."))

    b.append(h4("Độ nhạy", "Sensitivity"))
    b.append(p(
        "Nhu cầu có đầu ra cặp nhiệt điện lớn đã giảm mạnh nhờ độ nhạy, độ ổn định và khả năng "
        "khử nhiễu được cải thiện của các bộ chỉ thị cặp nhiệt điện số bán dẫn hiện đại. Các "
        "dụng cụ này có thể thường xuyên chỉ thị nhiệt độ với độ phân giải và độ ổn định 0,1 °C "
        "cho mọi loại ký hiệu chữ cái. Các cặp chuẩn khác nhau đáng kể về độ nhạy (Bảng 32.12). "
        "Độ nhạy của cặp nhiệt điện loại E gấp 10 lần loại B tại 1000 °C. Vì cặp nhiệt điện loại "
        "B có độ nhạy cực nhỏ quanh nhiệt độ phòng, nó chỉ dùng khi mối nối đo ở trên 870 °C. "
        "Cặp nhiệt điện chuẩn hóa nhạy nhất, loại E, có hệ số Seebeck cực đại 81 µV/°C và, quy "
        "chiếu về 0 °C, suất điện động Seebeck cực đại 76 mV. Dù dung sai ban đầu cho cả vật liệu "
        "cấp thường lẫn cấp đặc biệt đã được chuẩn hóa, chênh lệch giữa cấp thương mại và cấp "
        "cao cấp là nhỏ và, khi sử dụng, vật liệu cấp đặc biệt có thể suy giảm vượt cả dung sai "
        "ban đầu của vật liệu cấp thường."))

    b.append(h4("Ký hiệu chữ cái", "Letter Designations"))
    b.append(p(
        "Ký hiệu chữ cái và mã màu ANSI của Hoa Kỳ cho tám loại cặp nhiệt điện cụ thể (B, E, J, "
        "K, N, R, S và T) lần đầu được ISA ấn định trong Tiêu chuẩn MC-96.1 [28]. Các hiệp hội "
        "tiêu chuẩn ASTM và ANSI cũng theo các quy ước tương tự [10, 24]. Hậu tố đầu tiên của ký "
        "hiệu loại, P hoặc N, như trong KP hay KN, chỉ định thân nhiệt điện dương hoặc âm của "
        "một cặp. Hậu tố cuối “X” chỉ định vật liệu dây nối dài, như KPX là thân nhiệt điện nối "
        "dài dương của loại K. Với các cặp vật liệu chưa chuẩn hóa, nhà sản xuất và nhà bán "
        "thường tự áp dụng ký hiệu chữ cái, mã màu và tên thương mại riêng, không chính thức. "
        "Những định danh thương mại của từng nhà sản xuất này không có ý nghĩa phổ quát."))

    b.append(h4("Mã màu", "Color Codes"))
    b.append(p(
        "Mã màu nhằm tạo thuận lợi cho việc nhận dạng; các tiêu chuẩn của nhiều quốc gia đã ấn "
        "định mã màu cho các loại ký hiệu chữ cái và cho thân nhiệt điện cùng dây nối dài. Vì "
        "từng thân nhiệt điện quyết định cả cực tính lẫn độ nhạy, việc nhận dạng đúng từng chân "
        "rất quan trọng. Mã màu hiện dùng ở Hoa Kỳ nêu trong Bảng 32.12."))
    b.append(p(
        "Mã màu chuẩn hóa của Hoa Kỳ giữ đồng nhất trong vài thập kỷ; vì vậy sự nhầm lẫn mã màu "
        "loại vật liệu ở Hoa Kỳ phần lớn do bất cẩn của người dùng. Các mã màu hiện nay không "
        "đồng nhất toàn cầu có thể gây diễn giải sai tốn kém khi dùng đa quốc gia, đặc biệt bên "
        "ngoài Hoa Kỳ, nơi các nước láng giềng và đối tác thương mại có mã màu khác nhau hoặc "
        "nhiều mã song song. Rõ ràng, một mã màu quốc tế duy nhất được mọi quốc gia chấp nhận "
        "sẽ có lợi. Mã màu quốc tế như vậy đã có trong tiêu chuẩn IEC 584, đang được một số "
        "quốc gia xem xét [28]."))
    b.append(p(
        "Khác với các đặc tính Seebeck chuẩn hóa khá đồng nhất toàn cầu, các mã màu quốc gia "
        "thiếu phối hợp lại rất không nhất quán. Cơn hỗn loạn Babel của các mã màu quốc gia tồn "
        "tại năm 1998 được trình bày trong Bảng 32.13 [1, 4]."))
    b.append(_t3213("vi"))
    b.append(p(
        "Đáng tiếc và độc nhất, trong các tiêu chuẩn cặp nhiệt điện hiện hành của Hoa Kỳ, thân "
        "nhiệt điện âm luôn luôn là màu đỏ — trái với thông lệ điện và dụng cụ của Hoa Kỳ. Điều "
        "này cũng trái với mã màu quốc gia lịch sử của Trung Quốc, Đức và Nhật Bản, nơi màu đỏ "
        "chỉ định thân nhiệt điện dương. Trong tiêu chuẩn Anh, chân âm của mọi loại đều là màu "
        "xanh lam."))
    b.append(p(
        "Ở Pháp, thân nhiệt điện dương luôn được mã màu vàng. Tuy nhiên, chân dương màu vàng "
        "trong tiêu chuẩn Hoa Kỳ lại chỉ định vật liệu loại KP. Dây dẫn của một số kíp nổ điện "
        "ở Hoa Kỳ dùng dây bọc cách điện màu vàng có vạch đỏ song song từng bị nhầm với dây "
        "nối dài cặp nhiệt điện loại KX. Ở Anh, màu vàng chỉ định vật liệu loại JP. Chân dương "
        "trắng và chân âm đen của mã màu ANSI loại J hiện hành của Hoa Kỳ bị hoán đổi trong "
        "tiêu chuẩn quốc tế IEC 584."))
    b.append(p(
        "Bất chấp sự cần thiết rõ ràng của một mã màu thống nhất, vẫn còn một khối lượng khổng "
        "lồ vật liệu với các mã màu khác nhau trong kho và đang sử dụng trên toàn thế giới. Với "
        "bất kỳ quốc gia nào chuyển sang một tiêu chuẩn màu mới, ngay lập tức và trong suốt giai "
        "đoạn chuyển tiếp dài không tránh được sau khi chấp nhận, vật liệu mã màu mới sẽ lẫn "
        "trong khối lượng lớn mã màu cũ không nhất quán. Khả năng nhầm lẫn loại vật liệu sẽ tăng "
        "lên chứ không giảm. Ngoài ra, ngay cả các mã màu hiện hành cũng có thể trở nên nhòe trên "
        "vật liệu lắp đặt lâu năm, màu có thể phai, hoặc màu có thể bị sơn sai ngay từ khâu sản "
        "xuất."))

    b.append(h4("Nhận dạng thân nhiệt điện", "Identifying Thermoelements"))
    b.append(p(
        "Mã màu áp dụng trực tiếp cho dây nối dài và có hiệu lực với dây cặp nhiệt điện chính. "
        "Nhiều thân nhiệt điện chính và cặp nhiệt điện không được mã màu. Người dùng có thể "
        "không nhớ đúng mã màu. Người dùng cẩn trọng sẽ, trước khi dùng, xác nhận nhận dạng loại "
        "vật liệu độc lập với mã màu. Nhận dạng loại chắc chắn phải bằng sự kết hợp các phương "
        "pháp. Bất kỳ phương pháp đơn lẻ nào cũng có thể không dứt khoát, và không phương pháp "
        "nào thích dụng cho mọi vật liệu hay mọi hoàn cảnh."))
    b.append(p(
        "<b>Nhận dạng trực quan.</b> Thân nhiệt điện TP làm bằng đồng nên phân biệt được nhờ màu "
        "đỏ đồng đặc trưng. Thân nhiệt điện JP là sắt, có ánh xám xỉn đặc trưng. Các hợp kim kim "
        "loại nền khác cùng bạch kim và hợp kim của nó, nếu để trần, đều có bề ngoài bạc sáng rất "
        "giống nhau, trừ khi sau khi tách khỏi lớp cách điện khoáng ép, quá trình chế tạo tạo bề "
        "mặt xám xỉn nhám."))
    b.append(p(
        "<b>Nhận dạng từ tính.</b> Loại JP (sắt) hút từ mạnh. Loại KN (Alumel) hút từ nhẹ. Mọi "
        "vật liệu thân nhiệt điện chuẩn khác đều không từ tính. Có thể phân biệt JP và KN với "
        "các vật liệu khác bằng cách thử độ hút của một nam châm nhỏ."))
    b.append(p(
        "<b>Nhận dạng qua điện trở.</b> Điện trở suất của các thân nhiệt điện nêu trong Bảng "
        "32.12. Dù các cặp nhiệt điện lắp ráp có mối nối đo nhìn chung không thể tháo ra để thử, "
        "mối nối trần có thể tiếp cận trực tiếp, hoặc tiếp cận điện tại đầu đầu dò để đo điện trở "
        "từng chân nếu mối nối thuộc loại nối chung với vỏ dẫn điện tại mối nối đo. Các cụm lắp "
        "hay cáp cặp nhiệt điện thường có các cặp thân nhiệt điện cùng chiều dài và cùng tiết "
        "diện. Điện trở của từng chân phân biệt được vật liệu nếu biết cỡ dây và chiều dài. Trong "
        "những trường hợp đó, với hai đầu cáp ở cùng nhiệt độ, điện trở của từng thân nhiệt điện "
        "có thể đo trực tiếp. Tỷ số giữa điện trở chân dương và chân âm giúp xác nhận loại. Với "
        "các cặp nhiệt điện lắp ráp có mối nối đo không tiếp cận được, chỉ có thể đo điện trở "
        "vòng và so sánh với điện trở vòng tính toán."))
    b.append(p(
        "<b>Nhận dạng nhiệt điện.</b> Kém thuận tiện hơn, một cặp có thể được nhận dạng qua đầu "
        "ra ứng với nhiệt độ đã biết của mối nối đo và mối nối chuẩn. Các cáp nối dài bổ sung có "
        "thể nhận dạng bằng nhiệt bằng cách tạm thời tạo một mối nối giữa cặp dây ở một đầu. Có "
        "thể nhận dạng dứt khoát bằng quy trình kém chính xác hơn so với yêu cầu của hiệu chuẩn "
        "chính thức. Để nhận dạng, cả nhiệt độ mối nối chuẩn lẫn mối nối đo đều phải biết hoặc "
        "đo độc lập. Nhiệt độ xấp xỉ của mối nối chuẩn có thể xác định bằng cách ngắn mạch chốc "
        "lát đầu vào ngay tại cực vào của một dụng cụ có bù mối nối chuẩn. Vì vật liệu cặp nhiệt "
        "điện có thể không tương ứng với mức bù được áp dụng, nhiệt độ phải được xác định riêng."))
    b.append(p(
        "Nhiệt độ áp lên mối nối đo để nhận dạng phải ít nhất 200 °C, vì độ không đảm bảo của "
        "hiệu chuẩn cặp nhiệt điện và của nhiệt độ áp vào làm cho sự phân biệt suất điện động "
        "giữa các cặp, như E với J, hay K với N hoặc T, không tin cậy khi chỉ dùng bình nước đá "
        "hoặc nước sôi. Các loại R và S rất giống nhau chỉ phân biệt được tin cậy ở nhiệt độ cao "
        "hơn nhiều hoặc bằng hiệu chuẩn chính thức."))
    return "".join(b)


def sec_32_4e_vi():
    b = [h3("Mô hình chức năng của mạch nhiệt điện",
            "The Functional Model of Thermoelectric Circuits")]
    b.append(p(
        "Vì lý do đơn giản hóa, quan hệ giữa các nhiệt độ mối nối cần thiết cho phép đo chính "
        "xác chỉ được khẳng định trong phần “Mạch cặp nhiệt điện thực tế” mà không giải thích "
        "vật lý nào. Một số vấn đề tinh tế của các mạch nhiệt điện thực tế rất khó hình dung nếu "
        "thiếu một mô hình mạch tường minh. Một mô hình mạch nhiệt điện đơn giản, thực dụng và "
        "đa dụng giờ đây giải thích được vì sao những kết cấu nhiệt độ đó lại thích hợp. Quan "
        "trọng hơn, nó làm rõ hậu quả của việc lệch khỏi các nhiệt độ này. Nó soi sáng những "
        "vấn đề thường gặp của hiệu chuẩn và tính không đồng nhất. Nó giải thích vì sao quan "
        "niệm phổ biến nhưng sai lầm rằng suất điện động Seebeck tập trung tại các mối nối có "
        "thể dẫn đến sai số nghiêm trọng trong các mạch cặp nhiệt điện nói chung."))
    b.append(p(
        "Mạch cặp nhiệt điện thực tế gồm nhiều vật liệu và nhiều mối nối thực phát sinh, thường "
        "nhiều hơn nhiều so với Hình 32.24 hay 32.25. Các vật liệu phát sinh không kiểm soát như "
        "cực nối xuyên (feedthru), cực đấu, mối ghép v.v. có thể không được nhận ra là các phần "
        "tử nguồn, nhưng chúng vẫn có thể, một cách không được nhận thấy, góp vào phép đo những "
        "suất điện động Seebeck không mong muốn đáng kể. Vì vậy, với đo nhiệt độ cặp nhiệt điện "
        "thực dụng, điều thiết yếu là hiểu và dùng một mô hình mạch mô tả đơn giản để áp dụng và "
        "buộc sự chú ý vào những vị trí sai số tiềm ẩn để tránh được các vấn đề."))
    b.append(p(
        "Một mô hình xác thực như vậy, Mô hình chức năng của mạch nhiệt điện [1, 2, 5, 7, "
        "29–31], kết hợp (1) một phần tử mạch nhiệt điện cơ bản, (2) một luật cơ bản duy nhất "
        "mô tả độ nhạy của phần tử đó, (3) một tập các hệ quả thực dụng suy ra từ luật đó nhằm "
        "làm sáng tỏ các hàm ý thực tiễn của nó, và (4) một công cụ đồ họa để trực quan hóa mạch "
        "giúp đơn giản hóa việc phân tích. Mô hình rất đơn giản nhưng phi truyền thống này được "
        "chế tác cho đo nhiệt độ thực dụng và đáng nghiên cứu."))

    b.append(h4("Phần tử mạch nhiệt điện cơ bản",
                "The Basic Thermoelectric Circuit Element"))
    b.append(p(
        "Bất kỳ đoạn vật liệu M dài tùy ý, đẳng hướng nhiệt điện và không đẳng nhiệt, nằm trong "
        "một thân nhiệt điện nào đó đều là một phần tử Seebeck. Mỗi đoạn như vậy, hai đầu có "
        "chênh lệch nhiệt độ thuần (Hình 32.29), là một nguồn áp không lý tưởng có điện trở nội "
        "<i>R</i>(<i>T</i>). Suất điện động nguồn Seebeck phải được quan sát ở chế độ “hở mạch” "
        "(dòng không) để có phép đo nhiệt độ chính xác nhất. Bất kỳ sụt áp <i>iR</i> nào do dòng "
        "điện được phép chạy qua vì điện trở đầu vào thấp của bộ chỉ thị áp đều hạ suất điện động "
        "nguồn Seebeck xuống một điện áp Seebeck cực thấp hơn. Với đo nhiệt độ, chênh áp đó gây "
        "sai số nhiệt độ nếu không được hiệu chỉnh."))
    b.append(fig(29, F.fig(29), "vi"))
    b.append(p(
        "Trong đo nhiệt độ tĩnh, như khi hiệu chuẩn và trong phép đo quá trình thông thường, "
        "mối nối đo và một đoạn đáng kể của các thân nhiệt điện kề cận được nhúng trong một vùng "
        "bất động, gần đẳng nhiệt, nên phần lớn suất điện động Seebeck phát sinh ở xa mối nối "
        "đo, trên các đoạn thân nhiệt điện đi qua những vùng chuyển tiếp nhiệt độ ở xa. Trong đo "
        "nhiệt độ quá độ, vùng chênh lệch nhiệt độ chính lúc đầu kề cận mối nối đo, nên suất "
        "điện động phát sinh trên một vùng lan rộng dần kề cận — nhưng không nằm trong — mối nối "
        "đo (một mặt tiếp xúc vật liệu)."))

    b.append(h4("Luật suất điện động Seebeck", "The Law of Seebeck emf"))
    b.append(p(
        "Phương trình 32.74, d<i>E</i> = <i>σ</i>(<i>T</i>)d<i>T</i>, là luật hàm chi phối suất "
        "điện động của phần tử Seebeck, và vì vậy, chi phối điện áp thuần của những mạch nhiệt "
        "điện phức tạp nhất. Đó là Luật suất điện động Seebeck. Mọi khía cạnh nhiệt điện của hành "
        "vi mạch đều suy ra từ riêng quan hệ đơn giản này. Chi tiết vật lý của quá trình sinh ra "
        "hiệu ứng Seebeck rất phức tạp [5, 6]. Dù vậy, luật đơn giản này hoàn toàn nhất quán với "
        "mọi lý thuyết vật lý và đã được thực nghiệm xác nhận. Nếu quan hệ đơn giản này đúng cho "
        "phần tử Seebeck cơ bản thì phép đo nhiệt độ chính xác là khả thi. Nếu không, phép đo "
        "nhiệt độ nhiệt điện chính xác và tin cậy là không thể."))
    b.append(p(
        "Suất điện động nguồn của một phần tử đơn lẻ làm bằng vật liệu M, theo Phương trình "
        "32.75, là:"))
    b.append(eq("Δ<i>E</i><sub>M</sub>(<i>T</i>) = <i>E</i><sub>M</sub>(<i>T</i><sub>2</sub>) "
                "− <i>E</i><sub>M</sub>(<i>T</i><sub>1</sub>)", "32.79"))
    b.append(p(
        "và, với các đoạn được ghép nhiệt của hai vật liệu A và B mà tại một thời điểm bất kỳ "
        "chia sẻ một cặp nhiệt độ đầu cuối, bất kể vị trí hay khoảng cách của chúng trong mạch:"))
    b.append(eq("Δ<i>E</i><sub>AB</sub>(<i>T</i>) = <i>E</i><sub>AB</sub>(<i>T</i><sub>2</sub>) "
                "− <i>E</i><sub>AB</sub>(<i>T</i><sub>1</sub>)", "32.80"))
    b.append(p(
        "Chúng không cần được nối trực tiếp với nhau tại một mối nối (thực ra cũng không cần được "
        "nối điện). Giá trị của <i>E</i><sub>AB</sub>(<i>T</i>) lấy trực tiếp từ các phương trình "
        "đa thức chuẩn xác định cặp nhiệt điện, từ các biểu diễn đơn giản hơn của các phương "
        "trình đó, từ bảng tra hay đồ thị [1, 9–12]. Đặc tính Seebeck tuyệt đối của nhiều vật "
        "liệu cũng có sẵn, nhưng ít được công bố hơn [1, 5, 7, 8]. Như mô hình này cho thấy, đặc "
        "tính tuyệt đối luôn có thể dùng trong phân tích nhiệt điện. Chúng phải được dùng trong "
        "một số tình huống thực tế mà đặc tính tương đối quy ước trở nên vô nghĩa hoặc chưa được "
        "biết đến."))
    b.append(p(
        "Hệ số Seebeck tuyệt đối, lượng tăng nhiệt độ trên đoạn, hoặc cả hai, đều có thể dương "
        "hoặc âm. Vì vậy, cực tính của một phần tử trong mạch phụ thuộc cả vật liệu lẫn — khác "
        "với phần tử suất điện động điện hóa — chiều của chênh lệch nhiệt độ tức thời trên đoạn. "
        "Cực tính, thậm chí cả chức năng, thay đổi theo sự phân bố nhiệt độ."))

    b.append(h4("Các hệ quả từ Luật Seebeck", "Corollaries from the Seebeck Law"))
    b.append(p(
        "Từ Luật suất điện động Seebeck duy nhất (Phương trình 32.74), năm hệ quả thực dụng đặc "
        "biệt giàu tính dạy bảo đã được nhận ra, giúp ích cho phân tích mạch nhiệt điện. Đó là "
        "các hệ quả về: (1) vai trò chức năng, (2) tính tất định chức năng, (3) tính tất định "
        "nhiệt độ, (4) tính tất định suất điện động, và (5) suất điện động Seebeck [1, 2, 7, "
        "29–31]. Chúng được phát biểu trong Bảng 32.14, rút gọn từ [29]. Những hệ quả giàu "
        "khám phá này gắn trực tiếp với đo nhiệt độ thực dụng hơn ba “luật” cặp nhiệt điện quen "
        "thuộc [32] — thực chất chỉ là những hệ quả thay thế gián tiếp của luật vật lý duy nhất "
        "(Phương trình 32.74)."))
    b.append(_t3214("vi"))

    b.append(h4("Bản phác T/X trực quan hóa", "The T/X Visualization Sketch"))
    b.append(p(
        "Ý nghĩa thực dụng của luật cơ bản và các hệ quả của nó đối với các mạch nhiệt điện thực "
        "tế được bộc lộ bằng một bản phác đồ họa đơn giản (Hình 32.30). Bản phác T/X chỉ dùng để "
        "trực quan hóa và phân tích bằng số. Nó không vẽ theo tỉ lệ và không dùng để giải bằng "
        "đồ thị. Nó soi sáng những sự thực thiết yếu mà sơ đồ điện thông thường hay đồ thị "
        "<i>E</i>(<i>T</i>) không thể hiện rõ. Bản phác T/X cho thấy nhiệt độ của mọi mối nối "
        "thực theo trình tự chúng xuất hiện quanh mạch. Mối nối thực được đánh dấu bằng chấm "
        "đặc. Các mối nối được nối với nhau bởi các thân nhiệt điện. Bản phác không vẽ theo tỉ "
        "lệ, nên độ dốc không biểu diễn gradient nhiệt độ."))
    b.append(fig(30, F.fig(30), "vi"))
    b.append(p(
        "Bản phác T/X bộc lộ rằng các đoạn spanning một khoảng nhiệt độ luôn xuất hiện theo cặp "
        "— nhưng đáng chú ý là chỉ trong mạch nối tiếp. Chính sự thật này cho phép dùng thuận "
        "tiện các đặc tính Seebeck tương đối. Sự đơn giản hóa quy ước này không áp dụng cho các "
        "mạch có nhánh song song [2]. Bản phác T/X, áp vào mạch cặp nhiệt điện của Hình 32.26, "
        "mô tả các phần tử mạch đáng kể (các mối nối và thân nhiệt điện) theo cách tập trung vào "
        "các chức năng nhiệt điện tất yếu của chúng (Hệ quả 1). Hình 32.30 cho thấy một sự phân "
        "bố nhiệt độ mạch với nhiệt độ các mối nối <i>T</i><sub>c</sub> ≠ "
        "<i>T</i><sub>e</sub>, bị cố ý làm khác nhau một cách không đúng để minh họa một nguyên "
        "lý và lợi ích của bản phác."))
    b.append(note(
        "Bản in ghi <i>T</i><sub>b</sub> ≠ <i>T</i><sub>e</sub> tại câu này; nhưng theo lập luận "
        "của phần Ví dụ bên dưới — lỗi ghép cặp nhiệt chỉ nảy sinh khi <i>T</i><sub>c</sub> ≠ "
        "<i>T</i><sub>e</sub> — chữ cái đúng gần như chắc chắn là <i>T</i><sub>c</sub>. Bản dịch "
        "giữ cách diễn giải theo nghĩa và ghi rõ điều này thay vì sửa im lặng."))
    b.append(p(
        "<b>Nhiệt độ của các mối nối phụ.</b> Nhiệt độ các mối nối chuẩn phải được biết chính "
        "xác một cách độc lập để đo. Nhiệt độ chưa biết của mối nối đo phải được suy ra từ điện "
        "áp Seebeck. Nhiệt độ cụ thể của mọi mối nối thực phụ trong mạch rất hiếm khi được biết "
        "chính xác trong thực tế. Để dùng bản phác T/X, giá trị thực của chúng không cần phải "
        "biết chính xác. Tuy vậy, nếu giá trị tương đối của mọi mối nối phụ không được khống chế "
        "đúng như mô tả trong phần “Mạch cặp nhiệt điện thực tế”, và nếu một số nhiệt độ mối nối "
        "thiết yếu không được biết đủ tốt để vẽ bản phác, thì không thể bảo đảm phép đo nhiệt độ "
        "chính xác! Bản phác T/X giàu khám phá này không đòi hỏi nhiều thông tin hơn những gì "
        "thiết yếu cho chính phép đo vật lý."))
    b.append(p(
        "Khi ước lượng hậu quả đo lường và trực quan hóa cách phải khống chế nhiệt độ các mối "
        "nối trong mạch gồm nhiều vật liệu, đủ rồi nếu — cho phân tích định tính — giả định các "
        "mức nhiệt độ tương đối khả dĩ và hậu quả của chúng. Bản phác thường được dùng nhất để "
        "nhìn thấy hậu quả bằng mắt [1, 2, 29–31]. Dù vậy, nó cũng có thể hỗ trợ phân tích định "
        "lượng sai số cho các sự phân bố nhiệt độ khả dĩ."))
    b.append(p(
        "<b>Mối nối ảo và thân nhiệt điện ảo.</b> Trên bản phác T/X, các đường đẳng nhiệt qua "
        "mối nối thực cắt qua một số thân nhiệt điện. Coi các giao điểm này (ví dụ c′ và e′), "
        "mỗi giao điểm đánh dấu bằng một vạch, là các mối nối ảo thì hữu ích cho việc phân tích. "
        "Chúng tiện dụng để ấn định các điểm cuối nhiệt độ tùy ý của các đoạn. Ngoài ra, trên "
        "biểu đồ, các thân nhiệt điện ảo, b–c và f–g, được chỉ bằng nét đứt. Các đoạn này biểu "
        "diễn nguồn nhiệt điện ảo tưởng của suất điện động bù bổ sung, phải được cung cấp để "
        "kéo dài nhiệt độ chuẩn thực <i>T</i><sub>r</sub> tới giá trị nhiệt độ chuẩn ấn định "
        "<i>T</i><sub>0</sub>. Các thân nhiệt điện ảo biểu diễn bù mối nối chuẩn."))
    b.append(p(
        "Bản phác T/X giúp ấn định nhiệt độ biên của từng đoạn, và từ đó ấn định cực tính và "
        "suất điện động cho từng thân nhiệt điện trong mạch. Mạch được đi trên bản phác từ một "
        "cực của dụng cụ, thuận tiện là cực âm, tới cực kia. Sau đó, nếu hệ số Seebeck tuyệt đối "
        "của thân nhiệt điện dương, phần góp suất điện động của đoạn sẽ cộng thêm suất điện động "
        "nếu nhiệt độ tăng khi đi qua đoạn đó từ cực âm về phía cực dương của dụng cụ, v.v. Để "
        "quan sát và phân tích, hiệu quả hơn là coi các đoạn được ghép nhiệt trên một vùng nhiệt "
        "độ bị chặn bởi các đường đẳng nhiệt."))
    b.append(p(
        "<b>Ví dụ.</b> Trên bản phác T/X, hãy xét các suất điện động Seebeck tuyệt đối do bốn "
        "thân nhiệt điện của Hình 32.26 cung cấp. Với cách nối mạch nối tiếp này, đi từ cực âm "
        "tới cực dương, suất điện động Seebeck thuần của mạch thực giữa hai cực b và f là:"))
    b.append(eq("<i>E</i><sub>net</sub> = <i>E</i><sub>C</sub> + <i>E</i><sub>A</sub> + "
                "<i>E</i><sub>B</sub> + <i>E</i><sub>D</sub>", "32.81"))
    b.append(p("trong đó"))
    b.append(eq("<i>E</i><sub>C</sub> = ∫<sub><i>T</i>b</sub><sup><i>T</i>c</sup> "
                "<i>σ</i><sub>C</sub>d<i>T</i> , &nbsp; "
                "<i>E</i><sub>A</sub> = ∫<sub><i>T</i>c</sub><sup><i>T</i>d</sup> "
                "<i>σ</i><sub>A</sub>d<i>T</i> ,<br>"
                "<i>E</i><sub>B</sub> = ∫<sub><i>T</i>d</sub><sup><i>T</i>e</sup> "
                "<i>σ</i><sub>B</sub>d<i>T</i> , &nbsp; "
                "<i>E</i><sub>D</sub> = ∫<sub><i>T</i>e</sub><sup><i>T</i>f</sup> "
                "<i>σ</i><sub>D</sub>d<i>T</i>", "32.82"))
    b.append(p(
        "Hãy nhớ rằng những suất điện động Seebeck riêng lẻ này thực sự tồn tại trong các thân "
        "nhiệt điện dù chúng có được các mối nối nối thành mạch hay không. Chính sự phụ thuộc "
        "nhiệt độ của cả độ lớn lẫn cực tính tức thời của suất điện động là điều phân biệt phân "
        "tích mạch nhiệt điện với phân tích mạch điện thông thường (Hệ quả 5)."))
    b.append(p("Lưu ý rằng suất điện động của thân nhiệt điện A có thể viết lại thành:"))
    b.append(eq("<i>E</i><sub>A</sub> = ∫<sub><i>T</i>c</sub><sup><i>T</i>e′</sup> "
                "<i>σ</i><sub>A</sub>d<i>T</i> + ∫<sub><i>T</i>e′</sub><sup><i>T</i>d</sup> "
                "<i>σ</i><sub>A</sub>d<i>T</i>", "32.83"))
    b.append(p(
        "Cách viết này tùy ý tách thân nhiệt điện A thành hai đoạn nối với nhau tại mối nối ảo "
        "e′. Thân nhiệt điện D cũng có thể tách đoạn tương tự. Bây giờ, trên vùng nhiệt độ được "
        "gạch bóng giữa <i>T</i><sub>c</sub> và <i>T</i><sub>e</sub>, có các đoạn được ghép nhiệt "
        "không đúng là c–e′ và c′–e. Suất điện động thuần từ các đoạn được ghép nhiệt này là:"))
    b.append(eq("<i>E</i><sub>net</sub> = ∫<sub><i>T</i>c</sub><sup><i>T</i>e′</sup> "
                "<i>σ</i><sub>A</sub>d<i>T</i> − ∫<sub><i>T</i>c′</sub><sup><i>T</i>e</sup> "
                "<i>σ</i><sub>D</sub>d<i>T</i>", "32.84"))
    b.append(p(
        "Từ Phương trình 32.75, hãy nhận ra rằng đây chính là suất điện động Seebeck tương đối "
        "của cặp A–D ngoài ý muốn trên vùng nhiệt độ tùy ý đó, dù chúng không được nối trực "
        "tiếp trong mạch. Sự ghép cặp không đúng của các đoạn rõ ràng chỉ tránh được nếu "
        "<i>T</i><sub>c</sub> = <i>T</i><sub>e</sub>, bất kể giá trị nhiệt độ. Trong trường hợp "
        "Hình 32.26 biểu diễn một cặp nhiệt điện chính A–B với các dây nối dài khớp kiểu C–D, "
        "vật liệu A giống C và B giống D. Nếu từng chân của dây nối dài C–D khớp chính xác chân "
        "tương ứng của cặp nhiệt điện AB thì"))
    b.append(eq("∫<sub><i>T</i>c</sub><sup><i>T</i>e</sup> <i>σ</i><sub>CD</sub>d<i>T</i> = "
                "∫<sub><i>T</i>c</sub><sup><i>T</i>e</sup> <i>σ</i><sub>AB</sub>d<i>T</i>", "32.85"))
    b.append(p(
        "và (chỉ với dây nối dài khớp kiểu) sự ghép cặp tình cờ là vô hại."))
    b.append(p(
        "Ngược lại, với dây nối dài kiểu bù (<i>σ</i><sub>A</sub> = <i>σ</i><sub>C</sub> và "
        "<i>σ</i><sub>B</sub> = <i>σ</i><sub>D</sub>), sai số vẫn xảy ra ngay cả khi "
        "<i>σ</i><sub>CD</sub> khớp cặp <i>σ</i><sub>AB</sub> một cách sát sao nhưng không khớp "
        "từng chân riêng lẻ. Trong trường hợp dây nối dài trung hòa, khi C và D giống nhau, suất "
        "điện động thuần của cặp bằng không trên vùng từ <i>T</i><sub>b</sub> tới "
        "<i>T</i><sub>c</sub>. Khi đó, mối nối chuẩn thực được thừa nhận tất yếu là "
        "<i>T</i><sub>r</sub> = <i>T</i><sub>c</sub> = <i>T</i><sub>e</sub>, chứ không phải "
        "<i>T</i><sub>r</sub> = <i>T</i><sub>b</sub> = <i>T</i><sub>f</sub>."))
    b.append(p(
        "Nếu <i>T</i><sub>c</sub> và <i>T</i><sub>e</sub> bị hoán đổi cho nhau, sai số sẽ có độ "
        "lớn khác, chứ không chỉ đơn thuần trái dấu, chỉ vì sự phân bố nhiệt độ (Hệ quả 2). Chỉ "
        "có thể xác định nhiệt độ chưa biết của một mối nối duy nhất; các mối nối khác, kể cả "
        "mối nối phụ, phải được xác định bằng giá trị hoặc, gián tiếp, là đẳng nhiệt (Hệ quả 4)."))
    b.append(p(
        "Lưu ý rằng những phần góp tương đối như vậy (phần góp thuần bằng không từ hai đoạn giống "
        "nhau ngược chiều, hay sự ghép nhiệt sai lệch không mong muốn giữa B và D) lập tức nhìn "
        "thấy ngay bằng mắt trên bản phác T/X phi chính thức, không cần đại số rắc rối. Những "
        "sự thật then chốt của mạch nhiệt điện này không hiện rõ trên sơ đồ điện thông thường "
        "hay trên các đồ thị <i>E</i>(<i>T</i>)."))
    b.append(p(
        "Phần lớn mạch thực gồm nhiều vật liệu phụ chưa hiệu chuẩn như đầu nối, cực đấu, mối "
        "ghép, cực nối xuyên, đuôi dây ngắn hay dây nối dài, mỗi vật liệu đều có các đặc tính "
        "Seebeck riêng (thường là không xác định). Trong một số mạch, một vài thân nhiệt điện có "
        "thể vô tình bị mắc song song. Điều quan trọng là đưa chúng vào bản phác để nhận ra sai "
        "số tiềm ẩn chưa được lưu ý mà các phần tử mạch đó có thể góp vào nếu không được giữ đẳng "
        "nhiệt. Ngoài ra, nhiều phần tử mạch nối dài có thể bị nối sai với cực tính bị đảo. Hậu "
        "quả điện áp hay nhiệt độ cụ thể của các tình huống này dễ dàng tính được cho bất kỳ sự "
        "phân bố nhiệt độ khả dĩ nào. Bản phác T/X được thiết kế riêng để hỗ trợ trực quan hóa "
        "mạch nhằm tránh những vấn đề thực tế rất phổ biến này và để dễ dàng đánh giá tác động "
        "tiềm tàng của chúng."))
    return "".join(b)


def sec_32_4e_en():
    b = [h3("The Functional Model of Thermoelectric Circuits")]

    b.append(p(
        "For simplicity, the relation between junction temperatures required for accurate "
        "measurement was merely asserted in the section on “Practical Thermocouple Circuits,” "
        "without any physical explanation. Some subtle problems of realistic thermoelectric "
        "circuits are difficult to visualize without an explicit circuit model. A simple, "
        "practical, and general-purpose model of thermoelectric circuits now explains why those "
        "temperature structures are appropriate. More significantly, it makes clear the "
        "consequences of deviation from these temperatures. It illuminates the common problems "
        "of calibration and inhomogeneity. It explains why the commonplace misconception that "
        "the Seebeck emf is localized to junctions can lead to serious error in general "
        "thermocouple circuits."))
    b.append(p(
        "Real thermocouple circuits involve several materials and incidental real junctions, "
        "often many more than in Figures 32.24 or 32.25. The incidental uncontrolled materials "
        "of feedthrus, terminals, splices, etc. might not be recognized as source elements, yet "
        "they can, unnoticed, contribute significant unwanted Seebeck emf to the measurement. "
        "Therefore, for practical thermocouple thermometry, it is essential to understand and "
        "use a descriptive circuit model that is simple to apply and that forces the attention "
        "to locations of potential error so that problems can be avoided."))
    b.append(p(
        "One such authentic model, the Functional Model of Thermoelectric Circuits [1, 2, 5, 7, "
        "29–31], combines (1) a basic thermoelectric circuit element, (2) a single fundamental "
        "law that describes the sensitivity of that element, (3) a set of practical corollaries "
        "from that law that illuminate its practical implications, and (4) a graphic tool for "
        "circuit visualization to simplify analysis. This very simple but nontraditional model "
        "is crafted for practical thermometry and is worth studying."))

    b.append(h4("The Basic Thermoelectric Circuit Element"))
    b.append(p(
        "Any thermoelectrically homogeneous nonisothermal segment of arbitrary length of "
        "material M within any thermoelement is a Seebeck cell. Each such segment across which a "
        "net temperature difference exists (Figure 32.29) is a non-ideal voltage source with "
        "internal resistance <i>R</i>(<i>T</i>). The Seebeck source emf must be observed in an "
        "“open-circuit” (null current) mode for the most accurate thermometry. Any <i>iR</i> "
        "voltage drop due to current allowed by a low input resistance of the voltage monitor "
        "reduces the Seebeck source emf to a lower terminal Seebeck voltage. For thermometry, "
        "that voltage difference causes a temperature error unless corrected."))
    b.append(fig(29, F.fig(29), "en"))
    b.append(p(
        "In static thermometry, as in calibration and in typical process measurement, the "
        "measuring junction and a substantial length of the adjacent thermoelements are immersed "
        "in a stationary and somewhat isothermal zone so that most of the Seebeck emf occurs "
        "well apart from the measuring junction in thermoelements where they cross remote "
        "temperature transition regions. In transient thermometry, the zone of principal "
        "temperature difference initially is adjacent to the measuring junction so that the emf "
        "arises across a region of spreading extent adjacent to, but not in, the measuring "
        "junction (a material interface)."))

    b.append(h4("The Law of Seebeck emf"))
    b.append(p(
        "Equation 32.74, d<i>E</i> = <i>σ</i>(<i>T</i>)d<i>T</i>, is the functional law that "
        "governs the emf of the Seebeck cell and, thus, the net voltage of the most complex "
        "thermoelectric circuits. It is the Law of Seebeck emf. Every thermoelectric aspect of "
        "circuit behavior follows from only this simple relation. Physical details of the "
        "process that leads to the Seebeck effect are very complex [5, 6]. Nevertheless, this "
        "one simple law is entirely consistent with all physical theory and is experimentally "
        "confirmed. If this simple relationship does apply to the basic Seebeck cell then "
        "accurate thermometry is possible. If it does not, then accurate and reliable "
        "thermoelectric thermometry is not possible."))
    b.append(p(
        "The source emf of an individual cell of material M, from Equation 32.75, is:"))
    b.append(eq("Δ<i>E</i><sub>M</sub>(<i>T</i>) = <i>E</i><sub>M</sub>(<i>T</i><sub>2</sub>) "
                "− <i>E</i><sub>M</sub>(<i>T</i><sub>1</sub>)", "32.79"))
    b.append(p(
        "and, for thermally paired segments of materials A and B that happen at any instant to "
        "share a pair of end-point temperatures, regardless of their residence or proximity in "
        "a circuit,"))
    b.append(eq("Δ<i>E</i><sub>AB</sub>(<i>T</i>) = <i>E</i><sub>AB</sub>(<i>T</i><sub>2</sub>) "
                "− <i>E</i><sub>AB</sub>(<i>T</i><sub>1</sub>)", "32.80"))
    b.append(p(
        "They need not be directly joined at a junction (nor, indeed, be electrically joined). "
        "The values of <i>E</i><sub>AB</sub>(<i>T</i>) are obtained directly from the standard "
        "thermocouple polynomial defining equations, simpler representations of those equations, "
        "tables, or graphs [1, 9–12]. Absolute Seebeck properties for many materials are also "
        "available, but are less commonly reported [1, 5, 7, 8]. As is evident from this model, "
        "absolute properties could always be used in thermoelectric analysis. They must be used "
        "in some realistic circumstances where the conventional relative properties are "
        "meaningless or where the relative properties are not known."))
    b.append(p(
        "Either the absolute Seebeck coefficient, the temperature increment across the segment, "
        "or both of them, can be either positive or negative. Therefore, the polarity of a cell "
        "within a circuit depends both on the material and, unlike the electrochemical emf cell, "
        "on the momentary sense of temperature difference across the segment. Polarity, and even "
        "function, changes with temperature distribution."))

    b.append(h4("Corollaries from the Seebeck Law"))
    b.append(p(
        "From the single Law of Seebeck emf (Equation 32.74), five particularly instructive "
        "practical corollaries that aid thermoelectric circuit analysis have been recognized. "
        "These are the corollaries of: (1) functional roles, (2) functional determinacy, (3) "
        "temperature determinacy, (4) emf determinacy, and (5) Seebeck emf [1, 2, 7, 29–31]. "
        "These are stated in Table 32.14, abbreviated from [29]. These revealing corollaries "
        "relate more directly to practical thermometry than do the three familiar thermocouple "
        "“laws” [32] that actually are only oblique alternative corollaries to the sole "
        "physical law (Equation 32.74)."))
    b.append(_t3214("en"))

    b.append(h4("The T/X Visualization Sketch"))
    b.append(p(
        "The practical significance of the fundamental law and its corollaries for realistic "
        "thermoelectric circuits is revealed by a simple graphic sketch (Figure 32.30). The T/X "
        "sketch is used for visualization and numerical analysis only. It is not drawn to scale. "
        "It is not used for graphic solution. It illuminates essential facts that are not "
        "obvious from a conventional electrical schematic or <i>E</i>(<i>T</i>) plot. The T/X "
        "sketch shows the temperatures of all real junctions in the sequence in which they "
        "occur around the circuit. Real junctions are indicated by closed circles. Junctions "
        "are joined by thermoelements. The sketch is not drawn to scale, so slopes do not "
        "represent temperature gradients."))
    b.append(fig(30, F.fig(30), "en"))
    b.append(p(
        "The T/X sketch reveals that segments that span a temperature interval always occur in "
        "pairs — but significantly only in series circuits. It is this fact that allows the "
        "convenient use of relative Seebeck properties. This conventional simplification does "
        "not apply to circuits with paralleled branches [2]. The T/X sketch, applied to the "
        "thermocouple circuit of Figure 32.26, depicts the significant circuit elements (the "
        "junctions and thermoelements) in a way that focuses on their unavoidable "
        "thermoelectric functions (Corollary 1). Figure 32.30 shows a circuit temperature "
        "distribution with junction temperatures <i>T</i><sub>b</sub> ≠ <i>T</i><sub>e</sub>, "
        "that were shown (intentionally improperly different) to illustrate a principle and the "
        "benefit of the sketch."))
    b.append(note(
        "The printed text reads <i>T</i><sub>b</sub> ≠ <i>T</i><sub>e</sub> at this sentence; "
        "but from the argument in the Example below — improper thermal pairing arises only when "
        "<i>T</i><sub>c</sub> ≠ <i>T</i><sub>e</sub> — the correct letter is almost certainly "
        "<i>T</i><sub>c</sub>. This translation preserves the sense of the printed text and "
        "notes the discrepancy rather than silently correcting it."))
    b.append(p(
        "<b>Temperatures of Incidental Junctions.</b> The reference junction temperatures must "
        "independently be accurately known for measurement. The unknown temperature of the "
        "measuring junction is to be deduced from the Seebeck voltage. The specific temperatures "
        "of all incidental real junctions of a circuit are rarely known accurately in practice. "
        "For use in the T/X sketch, the actual values need not be accurately known. "
        "Nevertheless, if the relative values of all incidental junctions are not properly "
        "controlled, as described in the section “Practical Thermocouple Circuits,” and if some "
        "essential junction temperatures are not known well enough to draw the sketch, then "
        "accurate thermometry cannot be ensured! The revealing T/X sketch requires no more "
        "information than is essential for the physical measurement."))
    b.append(p(
        "In the estimate of measurement consequences and to visualize how junction temperatures "
        "must be controlled in circuits of many materials, it is sufficient to assume, for "
        "qualitative analysis, plausible relative temperature levels and their consequences. "
        "The sketch is most often used for visualizing consequences by inspection [1, 2, "
        "29–31]. Nevertheless, it also can aid in quantitative analysis of error for plausible "
        "temperature distributions."))
    b.append(p(
        "<b>Virtual Junctions and Thermoelements.</b> On the T/X sketch, isotherms through real "
        "junctions intersect some thermoelements. It is useful for analysis to view these "
        "intercepts (e.g., c′ and e′), each marked by a tic, as virtual junctions. For "
        "inspection and analysis, they conveniently delineate the arbitrary temperature "
        "end-points of segments. Also, on the diagram, virtual thermoelements, b–c and f–g, are "
        "indicated by dashed lines. These segments represent the imaginary thermoelectric source "
        "of complementary emf that must be supplied to extend the physical reference "
        "temperature, <i>T</i><sub>r</sub>, to the designated reference temperature value, "
        "<i>T</i><sub>0</sub>. The virtual thermoelements represent the reference junction "
        "compensation."))
    b.append(p(
        "The T/X sketch aids in assigning segment bounding temperatures and thus a polarity and "
        "an emf to each thermoelement in the circuit. The circuit is traversed on the sketch "
        "from one instrument terminal, conveniently the negative, to the other terminal. Then, "
        "if the absolute Seebeck coefficient of a thermoelement is positive, the emf "
        "contribution of the segment adds emf if the temperature increases in proceeding across "
        "the segment from the negative toward the positive instrument terminal, etc. For "
        "inspection and analysis, it is efficient to consider segments as thermally paired over "
        "a temperature zone bounded by isotherms."))
    b.append(p(
        "<b>Examples.</b> On the T/X sketch, consider the absolute Seebeck emfs supplied by the "
        "four thermoelements of Figure 32.26. As connected in this series circuit, proceeding "
        "from negative to positive terminals, the net Seebeck emf of the physical circuit "
        "between terminals b and f is:"))
    b.append(eq("<i>E</i><sub>net</sub> = <i>E</i><sub>C</sub> + <i>E</i><sub>A</sub> + "
                "<i>E</i><sub>B</sub> + <i>E</i><sub>D</sub>", "32.81"))
    b.append(p("where"))
    b.append(eq("<i>E</i><sub>C</sub> = ∫<sub><i>T</i>b</sub><sup><i>T</i>c</sup> "
                "<i>σ</i><sub>C</sub>d<i>T</i> , &nbsp; "
                "<i>E</i><sub>A</sub> = ∫<sub><i>T</i>c</sub><sup><i>T</i>d</sup> "
                "<i>σ</i><sub>A</sub>d<i>T</i> ,<br>"
                "<i>E</i><sub>B</sub> = ∫<sub><i>T</i>d</sub><sup><i>T</i>e</sup> "
                "<i>σ</i><sub>B</sub>d<i>T</i> , &nbsp; "
                "<i>E</i><sub>D</sub> = ∫<sub><i>T</i>e</sub><sup><i>T</i>f</sup> "
                "<i>σ</i><sub>D</sub>d<i>T</i>", "32.82"))
    b.append(p(
        "Recall that these individual Seebeck emfs do physically exist in the thermoelements "
        "whether or not they are connected by junctions as a circuit. It is the temperature "
        "dependence of both the magnitude and the momentary polarity of emf that distinguishes "
        "thermoelectric from ordinary electric circuit analysis (Corollary 5)."))
    b.append(p("Note that emf from thermoelement A can be rewritten as:"))
    b.append(eq("<i>E</i><sub>A</sub> = ∫<sub><i>T</i>c</sub><sup><i>T</i>e′</sup> "
                "<i>σ</i><sub>A</sub>d<i>T</i> + ∫<sub><i>T</i>e′</sub><sup><i>T</i>d</sup> "
                "<i>σ</i><sub>A</sub>d<i>T</i>", "32.83"))
    b.append(p(
        "This arbitrarily breaks thermoelement A into two segments joined at virtual junction "
        "e′. Thermoelement D can be segmented as well. Now, across the shaded temperature zone "
        "between <i>T</i><sub>c</sub> and <i>T</i><sub>e</sub>, there are improperly thermally "
        "paired segments c–e′ and c′–e. The net emf from these thermally paired segments is:"))
    b.append(eq("<i>E</i><sub>net</sub> = ∫<sub><i>T</i>c</sub><sup><i>T</i>e′</sup> "
                "<i>σ</i><sub>A</sub>d<i>T</i> − ∫<sub><i>T</i>c′</sub><sup><i>T</i>e</sup> "
                "<i>σ</i><sub>D</sub>d<i>T</i>", "32.84"))
    b.append(p(
        "From Equation 32.75, recognize that this is the relative Seebeck emf for the unintended "
        "A–D pair over that arbitrary temperature zone even though they are not directly joined "
        "in the circuit. That improper pairing of segments clearly is avoided only if "
        "<i>T</i><sub>c</sub> = <i>T</i><sub>e</sub>, whatever the temperature. In the instance "
        "that Figure 32.26 represents a principal thermocouple A–B with matching extension "
        "leads C–D, materials A and C are alike and B and D are alike. If the legs of extension "
        "leads C–D each exactly match the corresponding legs of thermocouple AB, then"))
    b.append(eq("∫<sub><i>T</i>c</sub><sup><i>T</i>e</sup> <i>σ</i><sub>CD</sub>d<i>T</i> = "
                "∫<sub><i>T</i>c</sub><sup><i>T</i>e</sup> <i>σ</i><sub>AB</sub>d<i>T</i>", "32.85"))
    b.append(p(
        "and (for matching extension leads only) the accidental pairing is benign."))
    b.append(p(
        "Otherwise, with compensating extension leads (<i>σ</i><sub>A</sub> = "
        "<i>σ</i><sub>C</sub> and <i>σ</i><sub>B</sub> = <i>σ</i><sub>D</sub>), error occurs "
        "even if <i>σ</i><sub>CD</sub> closely matches <i>σ</i><sub>AB</sub> as a pair but not "
        "individually. In the instance of neutral extension leads where C and D are alike, the "
        "net emf from the pair is null over the zone from <i>T</i><sub>b</sub> to "
        "<i>T</i><sub>c</sub>. In this instance, the physical reference junction is recognized "
        "as necessarily <i>T</i><sub>r</sub> = <i>T</i><sub>c</sub> = <i>T</i><sub>e</sub>, "
        "rather than <i>T</i><sub>r</sub> = <i>T</i><sub>b</sub> = <i>T</i><sub>f</sub>."))
    b.append(p(
        "If <i>T</i><sub>c</sub> and <i>T</i><sub>e</sub> were interchanged, the error would be "
        "of different magnitude, not merely of opposite sign, simply because of the "
        "temperature distribution (Corollary 2). The unknown temperature of only one junction "
        "can be determined; the others, including incidental junctions, must be defined by value "
        "or, indirectly, as being isothermal (Corollary 4)."))
    b.append(p(
        "Note that such relative contributions (the null net contribution from two opposed like "
        "segments or the inappropriate thermal mispairing between B and D) are immediately "
        "evident simply by inspection of the informal T/X sketch without tedious algebra. These "
        "critical facts of thermoelectric circuits are not evident from the usual electrical "
        "schematic or from <i>E</i>(<i>T</i>) plots."))
    b.append(p(
        "Most real circuits include several incidental uncalibrated materials such as "
        "connectors, terminals, splices, feedthrus, short pigtails, or extension leads that "
        "each have their own (usually indefinite) Seebeck properties. In some circuits, a few "
        "thermoelements may be inadvertently connected in parallel. It is important to include "
        "them in the sketch to recognize the potential unnoticed error they can contribute if "
        "not held isothermal. Furthermore, many long-lead circuit elements may be misconnected "
        "with reversed polarity. The specific voltage or temperature consequences of such "
        "situations are readily calculated for any plausible temperature distribution. The T/X "
        "sketch is designed specifically to aid circuit visualization to avoid these very "
        "common practical problems and to readily evaluate their potential impact."))
    return "".join(b)


def sec_32_4c_en():
    b = [h4("Modular Signal Conditioning Components",
            "Các bộ phận điều chế tín hiệu dạng mô-đun")]
    b.append(p(
        "The myriad of diverse and capable thermocouple indicators and recorders now commercially "
        "available, ranging from simple and very inexpensive to sophisticated and versatile yet "
        "reasonably priced, makes it unnecessary for most applied thermometry to assemble special "
        "signal conditioning circuits. Some, seeking economy of hardware, have built custom "
        "systems. Too often, these have not achieved accurate measurement and have proved to be "
        "very costly because the critical distinctions between thermoelectric circuits and "
        "ordinary electric circuits were not appreciated. For special situations where "
        "thermocouples are incorporated into special measurement or operational components or "
        "systems, several manufacturers now offer modular and integrated circuit components that "
        "simplify special application and do protect the unaware from some pitfalls [13]."))
    b.append(p(
        "<b>Thermocouple Signal Conditioning on a Chip.</b> As thermocouple signals are low "
        "level, it is sometimes desired to amplify them for improved resolution, recording, or "
        "control. It might be desirable to incorporate thermocouple sensing as a functional "
        "component in other instrumentation packages. There are now several miniature and "
        "inexpensive integrated circuit modules for thermocouples that provide reference junction "
        "compensation, linearization, isolation, open input indication, amplification, and set "
        "point control. Properly applied, these make the integration of thermocouple sensing into "
        "other devices, such as computer data acquisition boards, very simple [13]."))
    b.append(p(
        "When a user applies modular components such as these, it is particularly important to "
        "understand and to apply the authentic thermoelectric circuit model and principles "
        "introduced in the section “The Functional Model of Thermoelectric Circuits.” Some "
        "precautions normally provided in commercial thermocouple monitors must be provided by "
        "the user."))
    b.append(p(
        "<b>Reference Temperature Sensors.</b> Thermocouples are self-generating. For casual "
        "approximate temperature and differential temperature measurement, they require neither "
        "excitation nor reference temperature. For accurate thermometry, unless a known "
        "reference temperature is physically imposed, an accurate measurement of the reference "
        "junction temperature by independent means is necessary. This sensing is usually by "
        "powered resistance temperature detectors, thermistors, transistors, or integrated "
        "circuit sensors [1, 4]."))
    b.append(p(
        "<b>Reference Temperature Compensators.</b> Proper reference compensation requires (1) "
        "the establishment of an isothermal temperature zone that includes the terminals of the "
        "thermocouples, (2) sensing of the temperature of this zone, and (3) application of a "
        "complementary physical or numerical voltage to the thermocouple terminal voltage before "
        "scaling the total voltage to temperature."))
    b.append(p(
        "An analog method includes the resistive zone temperature sensor in a bridge that "
        "nonlinearly modulates a supplied voltage according to an approximated nonlinear curve "
        "of the <i>E</i>(<i>T</i>) characteristic of the thermocouple. This method is adapted to "
        "compensation of only a single thermocouple type. An alternate method numerically "
        "converts the sensed reference temperature to the appropriate compensating voltage "
        "value. The numerical approach allows applying a separate compensating voltage to each "
        "individual thermocouple and for different standard types. In principle, for accuracy, a "
        "numerical compensating voltage could be programmed by the user to conform to the "
        "specific calibration of the individual thermocouple, whether or not of standardized "
        "type."))
    b.append(p(
        "Reference temperature compensators are internal to the more advanced thermocouple "
        "monitors. In advanced units, eight to ten thermocouple inputs are grouped on a "
        "separately removable isothermal terminal assembly so they can be removed for reference "
        "sensor calibration or for replacement. Like thermocouples, reference sensors "
        "occasionally drift, causing significant temperature error. For most thermocouple types, "
        "a 1° error in temperature reference produces a similar error in the measured "
        "temperature. A variety of external battery- or line-powered, single- or multichannel "
        "reference junction compensating units are also commercially available [4, 14]."))

    b.append(h4("Grounding, Shielding, and Noise", "Nối đất, che chắn và nhiễu"))
    b.append(p(
        "The technically well-founded principles of noise control for electric circuits apply "
        "also to thermoelectric circuits [15, 16]. There are, however, some additional "
        "considerations that are necessary for thermocouple circuits. Some noise control "
        "problems stem from the nature of thermoelectricity; others from commercial thermocouple "
        "design practices."))

    b.append(h5("Noise Problems Peculiar to Thermocouples",
                "Những vấn đề nhiễu riêng của cặp nhiệt điện"))
    b.append(p(
        "Temperature control of all deliberate and incidental junctions and components, and the "
        "distributed nature of Seebeck source emf, cannot be ignored with impunity in "
        "thermocouple application. The unavoidable requirements of such control are best "
        "visualized using methods such as given later in “The Functional Model of Thermoelectric "
        "Circuits.” Incidental circuit components such as balancing or swamping resistors, "
        "feedthrus, splices, and terminal strips, not intended to contribute Seebeck emf, must "
        "deliberately be maintained isothermal. Shields, unavoidably nonisothermal, made "
        "electrically common with the thermocouple must be explicitly recognized as latent "
        "sources of random dc noise which contributes Seebeck emf if not properly connected."))
    b.append(p(
        "<b>Electromagnetic (EM) Noise.</b> In thermocouple probes of mineral-insulated "
        "metal-sheathed (MIMS) construction, ceramic-bead-insulated thermocouples, and in some "
        "paired insulated thermocouple wires, the paired thermoelements are not twisted and are "
        "well separated. Lengthy and larger diameter thermocouple probes present a significant "
        "circuit loop area to couple magnetic noise fields. Even if probes are entirely "
        "metal-sheathed, the standardized sheaths are very thin and of low magnetic permeability. "
        "They are scarcely effective for electromagnetic (EM) shielding. These features prevent "
        "the use of some classic techniques for the rejection of EM noise [15, 16]. To reduce "
        "troublesome EM noise, the principal thermocouple probe should be of the smallest "
        "practical diameter, and of minimum length. In instances where the EM source is "
        "localized and identified, the orientation of the probe relative to the source can be "
        "arranged to minimize EM coupling. For rejection of EM noise, extension leads should "
        "always be of twisted-pair construction, with a pitch small enough to reject "
        "high-frequency noise [15]."))
    b.append(p(
        "<b>Electrostatic (ES) Noise.</b> Electrostatic noise is more easily reduced. Shields of "
        "low resistance, though thin, can be effective if properly connected [15, 16]. Plated "
        "copper braid is commonly used and is effective for noise of moderate frequency. "
        "Continuous shields, such as the MIMS sheaths and aluminized mylar film, are effective "
        "for low-frequency ES noise and are more effective than braid shields for "
        "very-high-frequency noise. Electrostatic shields must be continuous (without gaps and "
        "holes as in braid) for maximum effectiveness. Optimum benefits from shielding require "
        "use with thermocouple monitors that provide three-wire input and multiplexers that, "
        "individually for each thermocouple, switch both the signal pair and their separate "
        "shield lead."))

    b.append(h5("Grounding", "Nối đất"))
    b.append(p(
        "Shielding for ES noise and pair twisting for EM noise are important for reduction of "
        "high-frequency noise. A secondary overall shield, isolated from inner shields and "
        "separately grounded, can improve the rejection of EM noise. Appropriate circuit "
        "grounding is also particularly important for both high-frequency EM and ES control, but "
        "it is even more significant for low-frequency and dc noise, which are often more "
        "consequential in thermocouple measurements. Appropriate grounding is complicated where "
        "intimate thermal contact of the measuring junction with an earth-grounded conducting "
        "test subject is needed for rapid transient thermometry or for accuracy in the presence "
        "of static temperature gradients."))
    b.append(p(
        "Figure 32.27 illustrates appropriate grounding for several of many possible "
        "situations. Low-level thermocouple circuits should be grounded only at a single "
        "electric reference point. Because the measuring junction is not a localized site of "
        "source emf, the point of grounding must be carefully considered. Grounding should "
        "never be at any point of the thermocouple circuit other than measuring or reference "
        "junctions. Electric contact, and particularly shunting or shorting, on a thermoelement "
        "at any point between measuring and reference junctions usually introduces spurious "
        "Seebeck emf from incidental unrecognized thermoelements."))
    b.append(fig(27, F.fig(27), "en"))
    b.append(p(
        "Allowable grounding might be dictated by the internal design of monitors and data "
        "loggers. Each instrument design addresses noise control in a distinctive way. Simple "
        "and inexpensive line-powered thermocouple thermometers might have only single-ended "
        "inputs with the negative lead internally connected to the power ground. This forces the "
        "sensor grounding to also refer to power ground. A grounded-junction arrangement might "
        "also be required for fast transient thermometry. In use, initially isolated "
        "thermocouples can short to the protective sheath or test subject. Although this does "
        "change the grounding configuration, resulting errors due to other effects usually are "
        "then predominant."))

    b.append(h5("Balanced Thermocouple Circuits", "Mạch cặp nhiệt điện cân bằng"))
    b.append(p(
        "The more sophisticated multichannel data acquisition systems specialized to "
        "thermocouple thermometry usually have high-resistance balanced inputs for high "
        "common-mode signal rejection. Some differential input amplifiers require significant "
        "input resistance for stability. Most have an internal chassis that provides a common "
        "signal reference guard surface that is well-isolated from power ground. In a few "
        "designs, the guard is electrically driven to a particular reference point. Because many "
        "variations are used, it is prudent to study and follow the specific grounding "
        "instructions recommended in the user’s manual for the instrument. Most accommodate "
        "alternative grounding arrangements."))
    b.append(p(
        "In sheathed thermocouple probes of standard MIMS dimensions, the thermoelements are of "
        "the same cross-section, parallel and well spaced, and located within the cylindrical "
        "sheath symmetrically [10]. Noise tends to be coupled equally to the paired "
        "thermoelements in common mode. However, lengthy or fine gage thermocouples have legs of "
        "high resistance compared to copper circuits. The ratio between the resistances of the "
        "dissimilar legs can be up to 25:1. Noise introduced in common mode adversely tends to "
        "convert to normal mode."))
    b.append(p(
        "In addition, unlike most voltage sources, the Seebeck emf is not localized to the "
        "measuring junction (a material interface). The emf can arise anywhere along the "
        "thermoelements. In transient thermometry, it first occurs adjacent to, and then spreads "
        "away from the measuring junction. In the more commonplace static thermometry, the site "
        "of source emf is usually distant from the measuring junction."))
    b.append(p(
        "Most specialized thermocouple recorders provide reference temperature compensation. "
        "They do not allow convenient user access to the circuit beyond the reference junctions. "
        "This restricts the noise control methods available to the user. For externally "
        "referenced thermocouples, some effective simple circuit modifications are possible. "
        "Figure 32.28 shows the addition of three resistors that, used with monitors of balanced "
        "input, improve noise rejection. Isothermal balancing resistor, "
        "R<sub>c</sub> = R<sub>a</sub> – R<sub>b</sub>, is added in series with the "
        "thermoelement of lower resistance. Making the resistance of the two circuit branches "
        "equal reduces the undesired conversion of noise from common mode to normal mode. The "
        "matched pair of shunting resistors, R<sub>s</sub>, presents a significant definite "
        "minimum source resistance to the amplifier input for stability and symmetrically "
        "couples the signals and sheath to the common reference point. The resistors must be "
        "large enough, R<sub>s</sub> ≥ 1000 (R<sub>a</sub> + R<sub>b</sub>), to avoid "
        "significant shunting resistive attenuation of the thermocouple source Seebeck emf. "
        "With great care to maintain these resistors strictly isothermal, the balancing and "
        "shunt resistors could be placed just at the input terminals external to the "
        "instrument-provided reference junction temperature compensation."))
    b.append(fig(28, F.fig(28), "en"))

    b.append(h5("Filtering", "Lọc"))
    b.append(p(
        "For low-frequency thermometry, to complement the user-provided passive rejection of EM "
        "and ES noise by proper grounding and shielding, internal filtering provided by data "
        "acquisition monitor manufacturers can effectively reject high-frequency noise. "
        "Filtering before recording is preferred. This control can be performed by conventional "
        "filters; but for quasi-static thermocouple measurements, other very effective "
        "techniques such as “double-slope integration” are provided in some designs. These "
        "techniques effectively average the signal over several measured samples. The noise "
        "reduction and stability under real-life conditions is remarkable. Routine resolution "
        "and stability to 0.1 µV variation over a period of days is achieved by many modern "
        "thermocouple data loggers. However, this noise rejection method restricts the sampling "
        "speed so that samples can be limited to intervals no shorter than 10 ms to 20 ms that "
        "are unsuited to very fast transient thermometry."))

    b.append(h4("Thermal Coupling", "Ghép nhiệt"))
    b.append(p(
        "Accurate thermometry obviously requires that the temperature of thermocouple measuring "
        "junctions closely agree with the temperatures to be measured. In static measurements at "
        "thermal equilibrium, this is often easy to accomplish. In fast transient measurements, "
        "it can be very difficult."))
    b.append(h5("Static Thermometry", "Đo nhiệt độ tĩnh"))
    b.append(p(
        "Thermocouple thermometry of steady-state or slowly varying temperatures requires close "
        "thermal coupling of the measuring junctions to the point of measurement. This agreement "
        "of temperatures naturally occurs by equilibration if the point of measurement can be "
        "chosen to be well within a region that stays at uniform temperature during measurement. "
        "Even in such nearly static thermometry, the thermoelements should be as small as "
        "practical to reduce any conduction of heat along the thermocouple that could affect the "
        "temperature being measured."))
    b.append(p(
        "In typical situations, however, the vicinity of the measuring point is not isothermal "
        "and, even at steady state, static temperature gradients can cause the measuring junction "
        "to be at a significantly different temperature from the subject [18]. This source of "
        "error is more severe for surface, liquid, and gas measurements than for internal solid "
        "measurements, and is aggravated for the measurement of subjects of low thermal mass. "
        "Efficient thermal coupling of the thermocouple to the subject, as in Figure 32.27, is "
        "essential."))
    b.append(p(
        "Noise or safety might require electrical isolation of the thermocouple. Commonplace "
        "electrical insulating materials are poor thermal conductors. There are now special "
        "greases, coatings, and thin sheet materials available designed to provide high "
        "electrical isolation, yet good thermal contact [17]. Where needed, they can improve "
        "accuracy by efficient thermal coupling."))
    b.append(h5("Transient Thermometry", "Đo nhiệt độ quá độ"))
    b.append(p(
        "Monitoring very rapid variations of temperature is most effectively accomplished by "
        "thermocouples because of the low sensing mass and small size of measuring junction that "
        "they allow. Fast thermal response requires the use of special thermoelement "
        "configurations in the vicinity of the measuring junction, special circuitry, special "
        "thermocouple monitoring instruments, and characterizing methods [16, 18]. Some "
        "suppliers offer very thin (10 µm thick) foil and fine wire thermocouples that are "
        "especially well adapted to such measurement [19, 20]."))
    b.append(p(
        "A thermocouple alone has no characteristic response time. The Seebeck effect occurs at "
        "electronic speed. The thermocouple source emf always promptly corresponds to the "
        "temperatures of all junctions in the circuit. However, the transient temperature "
        "response of a thermocouple installation is very much slower, and is primarily governed "
        "by the thermal interaction of the thermocouple components adjacent to the junctions and "
        "the adjacent mass of the test subject [18, 22, 23]. That slow conductive heat transfer "
        "is retarded many-fold by even a thin film of air, vacuum, or an insulating solid layer. "
        "In fast transient thermometry, the electrical parameters of the thermocouple and "
        "associated circuitry and dynamic response of the recording system can further degrade "
        "response time."))
    b.append(p(
        "Intimate thermal coupling by special materials required for static measurement in a "
        "thermal gradient is even more critical to transient than to static thermometry [17]. "
        "Even the special coupling materials slow response. They should be as thin as feasible. "
        "For very fast thermometry, such coupling might not be tolerable. It may be necessary to "
        "place the bare measuring junction in direct electric contact with the subject "
        "(Figure 32.27)."))
    b.append(p(
        "<b>Intrinsic Thermocouples.</b> Where the subject of thermometry is an electric "
        "conductor, it is possible to electrically fuse the two thermoelements separately to the "
        "test subject. This is an “intrinsic” thermocouple junction arrangement. Fine wires or "
        "thin foils spot-welded to the subject allow the fastest possible electrothermal "
        "response and reduce the influence of the thermocouple on the temperature being "
        "measured."))
    b.append(p(
        "Observe two special precautions in the use of intrinsic junctions. First, the two "
        "thermoelements should be fused to the subject side-by-side, close together (not one "
        "over the other). With intrinsic junctions, the bridging segment of the subject becomes "
        "a part of the series thermoelectric circuit. (There are two intrinsic junctions coupled "
        "by the intermediate subject material.) This produces the fastest response; but in very "
        "fast transients, the temperatures of the two junctions can very briefly be slightly "
        "different and thus introduce a momentary error, as the unknown Seebeck coefficient of "
        "the bridging subject material is different from that of one or both of the principal "
        "thermoelements [21]."))
    b.append(p(
        "Second, for transient thermometry, the fine thermoelements leading to the intrinsic "
        "junctions should be as short and fine as feasible to reduce their thermal loading; "
        "however, this results in a relatively high electric lead resistance. A strain-relieved "
        "transition from the fine filaments to more substantial low-resistance compensating lead "
        "wires should be made near the measuring junction to enhance electric response. The "
        "electrical effect of capacitive coupling of the circuit on electric transient response "
        "must also be minimized."))
    b.append(p(
        "<b>Numerical Correction.</b> All feasible physical techniques to achieve fast "
        "transient temperature response when applied might not be sufficient for a very fast "
        "measurement. An inadequate transient response can be further enhanced by numerical "
        "analysis [21]. Two additional steps must be taken."))
    b.append(p(
        "First, an authentic experimental or correctly modeled transient response "
        "characterization of the overall thermal-electrical thermometry system must be made. "
        "The usual simplistic first-order representations of in situ thermocouple response might "
        "be inadequate [21-23]."))
    b.append(p(
        "Second, this authentic characterization must be applied by mathematical deconvolution to "
        "better estimate the true temperature history of data indicated by a system that had "
        "inadequate physical transient response [16, 19]. Critical and reliable improvements of "
        "effective response time by factors of four or more are often possible. If uncorrected, "
        "indicated transient peak temperatures can be in error by a much greater percentage "
        "than the error that results from static thermocouple calibration error. No general "
        "uncertainty can be assigned to a transient measurement without such response "
        "characterization."))
    return "".join(b)


def sec_32_4d_en():
    b = [h3("Thermocouple Materials")]

    b.append(h4("Thermocouple Standardization"))
    b.append(p(
        "Many materials are in regular use as thermocouples for thermometry; some pairs are "
        "standardized, some are not. The distinction is a matter of formal consensus approval by "
        "balanced standards committees of experienced users, producers, and standards-laboratory "
        "staff [10, 24]. In the U.S., eight materials are letter-designated (Types B, E, J, K, N, "
        "R, S, and T) [9–12, 24]; some of their properties are summarized in Table 32.12. The "
        "standardized <i>E</i>(<i>T</i>) characteristics are now defined exactly by high-degree "
        "polynomial functions rather than tabulated values [1, 9, 10]. Thermoelements should be "
        "used as selectively paired by the producer: randomly paired elements of the same type, "
        "from the same or different manufacturers, are not assured to conform to the standard "
        "pair values or tolerances [1, 9–12]. Properties of a few other popular pairs, such as "
        "precious-metal and tungsten refractory alloys, have been committee-proposed but carry "
        "no formal letter designations or color codes [10]."))
    b.append(_t3212("en"))
    b.append(h4("Low Temperature Thermometry"))
    b.append(p(
        "Thermocouple measurement below the ice point requires special consideration. Cryogenic "
        "thermometry has been loosely defined as measurement below 280 K (7 °C), or more "
        "restrictively below 90 K (−183 °C, the boiling point of liquid oxygen at 1 atm) [1]. "
        "The Seebeck coefficient of all conductors is insignificant at 0 K, and a few "
        "superconducting metal elements drop abruptly to zero at a threshold below 10 K for most "
        "unalloyed superconductors [27]; special alloys have raised that threshold to about "
        "120 K. Superconducting transitions complicate thermoelectric thermometry at the lowest "
        "cryogenic temperatures [7, 8]."))
    b.append(p(
        "Standard Seebeck characteristics are defined for Types E, J, K, N, and T down to "
        "−270 °C; Types R and S extend only to −50 °C, and Type B is not characterized below "
        "0 °C. Of the letter-designated materials, Type E is preferred for use down to −233 °C "
        "(40 K) for its higher relative Seebeck coefficient [1]. Below 40 K, special alloy "
        "combinations such as Type KP vs. Au/0.07 Fe are recommended [1]. Peltier and Thomson "
        "heating are current-dependent effects, so neither is significant when thermometry is "
        "properly conducted by open-circuit measurement — there is no thermocouple self-heating "
        "as with resistance thermometers. At cryogenic temperatures the Seebeck coefficient of "
        "most alloys is strongly magnetic-field dependent, so thermo-magneto-electric effects "
        "matter in superconductivity studies [2, 27]."))
    b.append(h4("Sensitivity"))
    b.append(p(
        "The need for large thermocouple output has been drastically reduced by modern "
        "solid-state digital indicators, which routinely resolve 0.1 °C for all letter-designated "
        "types. The standard pairs differ significantly in sensitivity (Table 32.12): Type E is "
        "ten times as sensitive as Type B at 1000 °C. Type B, with its very small sensitivity "
        "near room temperature, is intended only for measuring junctions above 870 °C. The most "
        "sensitive standardized type, E, has a maximum Seebeck coefficient of 81 µV/°C and, "
        "referenced to 0 °C, a maximum Seebeck emf of 76 mV. Although initial tolerances for "
        "both normal- and special-grade material are standardized, the gap between commercial "
        "and premium grades is small, and in service special-grade material can degrade beyond "
        "the initial normal-grade tolerance."))
    b.append(h4("Letter Designations"))
    b.append(p(
        "The U.S. ANSI letter designations and color codes were first established by the ISA in "
        "Standard MC-96.1 [28]; ASTM and ANSI follow the same conventions [10, 24]. A first "
        "suffix P or N (as in KP, KN) designates the positive or negative thermoelement of a "
        "pair; a final X designates extension-wire material (KPX). For non-standardized pairs, "
        "producers apply their own unofficial designations and trade names, which have no "
        "universal meaning."))
    b.append(h4("Color Codes"))
    b.append(p(
        "Because each thermoelement determines both polarity and sensitivity, positive "
        "identification of each leg matters. U.S. color codes have been uniform for decades, so "
        "U.S. confusion is mostly carelessness. The globally discordant national codes, "
        "however, cause costly misinterpretation in multinational use. A single international "
        "code is embodied in IEC 584, under consideration by several nations [28]; the 1998 "
        "babel of national codes is shown in Table 32.13 [1, 4]."))
    b.append(_t3213("en"))
    b.append(p(
        "Uniquely among U.S. standards, the negative thermoelement is always red — contrary to "
        "U.S. electrical practice and to the historic codes of China, Germany, and Japan, where "
        "red marks the positive leg. In English standards the negative leg of all types is "
        "blue. In France the positive leg is always yellow, yet a yellow positive leg in the "
        "U.S. standard means Type KP; the yellow-with-red-tracer lead wires of some U.S. "
        "electric blasting caps have been mistaken for Type KX extension wire. In England "
        "yellow denotes Type JP. The white-positive/black-negative U.S. ANSI code for Type J is "
        "transposed in IEC 584. Despite the clear desirability of a uniform code, a huge "
        "quantity of legacy-coded material remains in stock and in service, so a switch to any "
        "new standard would initially increase — not reduce — the possibility of confusion. "
        "Colors also fade or were misapplied at manufacture."))
    b.append(h4("Identifying Thermoelements"))
    b.append(p(
        "The prudent user confirms material type before use, independent of the color code, by "
        "a combination of methods — no single method is definite for all materials or "
        "circumstances. <b>Visual:</b> TP is copper (distinctive reddish color); JP is iron "
        "(matte gray cast); other bare base-metal and platinum alloys look alike. "
        "<b>Magnetic:</b> JP (iron) is strongly magnetic and KN (Alumel) slightly so; all other "
        "standard thermoelements are nonmagnetic. <b>Resistive:</b> with both cable ends at the "
        "same temperature, the resistance of each leg (Table 32.12) identifies the material if "
        "size and length are known; the positive/negative resistance ratio aids confirmation. "
        "For assembled thermocouples with inaccessible junctions, only loop resistance can be "
        "measured and compared with calculated values. <b>Thermoelectric:</b> a pair can be "
        "identified by its output for known measuring- and reference-junction temperatures; "
        "both must be independently known. The imposed measuring-junction temperature must be "
        "at least 200 °C, because calibration and imposed-temperature uncertainty make the emf "
        "distinction between pairs such as E vs. J, or K vs. N and T, unreliable with ice or "
        "boiling-water baths. The very similar Types R and S can be distinguished reliably only "
        "at much higher temperatures or by formal calibration."))
    return "".join(b)


def sec_32_4f_vi():
    b = [h3("Độ không đồng nhất", "Inhomogeneity")]
    b.append(h4("Bản chất của độ không đồng nhất", "The Nature of Inhomogeneity"))
    b.append(p(
        "Một thân nhiệt điện mảnh được gọi là không đồng nhất nếu σ<sub>M</sub>(<i>T</i>) "
        "thay đổi dọc theo chiều dài của nó. Môi trường trong quá trình ứng dụng có thể đưa "
        "vào sự không đồng nhất không đều vào một hoặc cả hai thân nhiệt điện của một cặp. "
        "Hiệu ứng này giống như có một hoặc nhiều vật liệu không đồng nhất bổ sung được thêm "
        "vào mạch."))
    b.append(h4("Tầm quan trọng của độ không đồng nhất", "The Significance of Inhomogeneity"))
    b.append(p(
        "Tính đồng nhất nhiệt điện thỏa đáng là giả định quan trọng nhất của ứng dụng cặp nhiệt "
        "điện. Nó thường được mặc định; hiếm khi được xác nhận. Độ không đồng nhất là một vấn "
        "đề có thật nhưng mang tính “bóng ma”. Nó thường không bị phát hiện ngay cả khi gây ra "
        "sai số đáng kể. Nó hiếm khi bị phát hiện ngay cả bởi sự hiệu chuẩn quy chuẩn cẩn thận "
        "nhất [1, 7, 11, 29–31, 33, 34]. Trong đo nhiệt độ vật lý, trôi cặp nhiệt điện luôn là "
        "triệu chứng của sự tiến triển độ không đồng nhất. Sự thay đổi này mang tính tiến triển, "
        "thường xảo quyệt, và thường bị diễn giải sai [34]. Thay vì được hình dung đúng đắn là "
        "sự suy thoái cục bộ của hệ số Seebeck, trôi thường bị nhìn nhận sai thành sự “hộp đen” "
        "đồng nhất của cặp nhiệt điện thay vì độ không đồng nhất đang tiến triển. Vì lý do này, "
        "nó là một vấn đề phổ biến hơn nhiều so với những gì hầu hết người dùng có kinh nghiệm "
        "nhận ra. Nó có thể xảy ra trong sử dụng, trong chế tạo, hoặc trong hiệu chuẩn do ứng "
        "suất cơ học, biến đổi pha nhiệt, nhiễm bẩn bề mặt, tương tác hóa học giữa các vật liệu, "
        "bay hơi hoặc di chuyển của các thành phần hợp kim, biến đổi dưới bức xạ, và nhiều "
        "nguyên nhân thực tế khác. Sai số do độ không đồng nhất trong cặp nhiệt điện, tính theo "
        "sản xuất, dự kiến được bao phủ bởi các dung sai chuẩn [1, 9, 10, 28]. Độ không đồng "
        "nhất phiền toái phổ biến nhất ở các cặp nhiệt điện đã dùng và bị lạm dụng, nhưng đôi "
        "khi cũng xảy ra ở cặp nhiệt điện mới đã được hiệu chuẩn riêng lẻ ở nhiệt độ cao. Nó có "
        "thể xảy ra bên trong và xuyên qua các vỏ bảo vệ kim loại hoặc giếng nhiệt có vẻ không "
        "thấm, cũng như giữa các chất cách điện hạt. Ví dụ Hình 32.30 minh họa tác động của việc "
        "không kiểm soát đúng nhiệt độ mối nối dẫn đến việc đưa một cách tinh vi suất điện động "
        "Seebeck tương đối từ sự ghép nhiệt không chủ định của các đoạn thân nhiệt điện đồng "
        "nhất. Vấn đề độ không đồng nhất tương tự, được trực quan hóa tốt nhất bằng bản phác "
        "T/X, nảy sinh khi một phần của một hoặc cả hai thân nhiệt điện thay đổi hệ số Seebeck "
        "cục bộ trên một đoạn không đẳng nhiệt của cặp nhiệt điện. Thực chất, điều này đưa vào "
        "các đoạn không đồng nhất “bóng ma” có đặc tính thoải dần không xác định và vị trí không "
        "được nhận ra [35]. Điều này thường xảy ra nhất trên một vùng dài gần mối nối đo, nơi "
        "các thân nhiệt điện tiếp xúc với môi trường gây hại trong lò hoặc quy trình. Sai số tối "
        "đa có thể có của độ không đồng nhất được xác định bởi vị trí và độ lớn của sự lệch lớn "
        "nhất khỏi bình thường của hệ số Seebeck. Sai số thực tế phụ thuộc vào sự phân bố nhiệt "
        "độ tức thời trong quá trình sử dụng. Trong đo nhiệt độ và hiệu chuẩn, sai số có thể do "
        "độ không đồng nhất gây ra được giảm nhẹ. Khi chỉ hiện diện trong vùng đẳng nhiệt, độ "
        "không đồng nhất không gây sai số. Dưới sự phân bố nhiệt độ bất lợi, sai số độ không "
        "đồng nhất có thể cực đoan và dẫn đến các đáp ứng kỳ lạ khó hiểu [34]. Các thay đổi hệ "
        "số Seebeck tương đối trên 60% trong các đoạn dài 25 cm đã được quan sát ở các cặp nhiệt "
        "điện hạng sang Type R MIMS được hiệu chuẩn riêng lẻ, có chứng nhận, dây mảnh, hoàn toàn "
        "nằm trong các vỏ bạch kim còn nguyên vẹn và tiếp xúc với nhiệt độ trong phạm vi nhiệt "
        "độ đã lập bảng [18]."))
    b.append(h4("Kiểm tra độ không đồng nhất", "Testing for Inhomogeneity"))
    b.append(p(
        "Nhiều phép thử nhạy và chính xác xác thực cho độ không đồng nhất nhiệt điện đã được "
        "phát triển, và nhu cầu thực tế của chúng đã được chứng minh; tuy nhiên, chúng hiếm khi "
        "được dùng [33]. Mọi phép thử độ không đồng nhất xác thực đều đòi hỏi di chuyển một bước "
        "nhiệt độ đột ngột tiến dần dọc theo các thân nhiệt điện. Việc áp dụng phổ biến một hình "
        "mẫu nhiệt độ đối xứng rất hẹp là trái ngược với một phép thử độ không đồng nhất. Nó "
        "không phải là phép thử độ không đồng nhất. Việc dùng phổ biến của nó đã đánh lừa nhiều "
        "người phủ nhận độ không đồng nhất như một vấn đề có thật và quan trọng trong đo nhiệt "
        "độ nhiệt điện chính xác. Các phép thử hợp lệ dao động từ các phương pháp đơn giản có độ "
        "phân giải thấp đến các phương pháp tiên tiến có thể phân giải độ không đồng nhất với độ "
        "phân giải không gian vài milimet [21, 33]. Đáng tiếc là, do sai số độ không đồng nhất "
        "thường không được nhận ra, độ không đồng nhất không được thử nghiệm xác thực trong thực "
        "tế thương mại cũng như bởi các phòng thí nghiệm hiệu chuẩn. Dù vậy, chứng nhận NIST "
        "truy nguyên được nhưng không xác thực với độ chính xác cao là có thể trên một cặp nhiệt "
        "điện có thể đo chính xác là cực kỳ không đồng nhất và có độ không đắc định vô hạn "
        "[29–31, 33, 34]."))

    b.append(h3("Hiệu chuẩn", "Calibration"))
    b.append(p(
        "Độ không đắc định đo lường của hầu hết các loại cảm biến có thể giảm bằng hiệu chuẩn "
        "riêng lẻ. Hiệu chuẩn ban đầu, hiệu chuẩn định kỳ lại các cặp nhiệt điện chưa dùng, và "
        "thậm chí của các cặp nhiệt điện cá thể đã suy thoái, mặc dù phổ biến, thường ít có lợi "
        "(hoặc thậm chí có hại) và tốn kém hơn. Việc hiệu chuẩn cặp nhiệt điện thiếu suy nghĩ "
        "như vậy đã bị một số chương trình “bảo đảm chất lượng” ép buộc. Các cuộc khảo sát cho "
        "thấy xu hướng khách hàng đòi độ chính xác ngày càng cao của đo nhiệt độ [36]. Trong một "
        "số ứng dụng, sai số 1°F (0,56°C) giờ đây bị coi là quá lớn, và dung sai 0,1°F có thể "
        "được chỉ định độc lập với mức nhiệt độ. (So sánh với dung sai trong Bảng 32.12.) Có một "
        "vài ứng dụng công nghiệp thực sự đòi hỏi độ chính xác như vậy. Thường hơn, quy định chỉ "
        "đơn giản cho rằng độ chính xác như vậy trong đo nhiệt độ cặp nhiệt điện là đạt được "
        "thường quy chỉ bằng hiệu chuẩn. Hiệu chuẩn là một loại thuốc phiện của bảo đảm chất "
        "lượng. Ảo tưởng về độ chính xác do hiệu chuẩn có chứng nhận NIST truy nguyên và hiệu "
        "chuẩn tại chỗ tự xưng mang lại là phản tác dụng nếu nó không xác thực. Xét đến các chi "
        "tiết của hiệu chuẩn cặp nhiệt điện gợi ý tại sao độ chính xác xác thực ở mức 0,1°C khó "
        "có khả năng trong đo nhiệt độ nhiệt điện công nghiệp. Cách tiếp cận để đạt được hiệu "
        "chuẩn xác thực của độ chính xác hệ thống cặp nhiệt điện (bỏ qua sai số ghép nhiệt và "
        "đáp ứng quá độ) được minh họa trong Hình 32.31. Hình 32.31(a) biểu diễn hệ thống cặp "
        "nhiệt điện cần hiệu chuẩn. Hiệu chuẩn cho đo nhiệt độ nhiệt điện phải phân biệt ba "
        "thành phần hệ thống: (1) mạch cặp nhiệt điện, (2) bộ bù nhiệt độ mối nối chuẩn, và (3) "
        "dụng cụ theo dõi. Mỗi thành phần riêng biệt ảnh hưởng đến độ không đắc định nhiệt độ."))
    b.append(fig(31, F.fig(31), "vi"))
    b.append(h4("Cặp nhiệt điện chính", "The Principal Thermocouple"))
    b.append(p(
        "Hiệu chuẩn cặp nhiệt điện chính được thực hiện bằng cách nhúng vùng lân cận mối nối đo "
        "vào vùng đẳng nhiệt của bể hoặc lò [37]. Một vài bộ hiệu chuẩn giếng khô nhỏ gọn hiện "
        "có rất tiện lợi để hiệu chuẩn tại hiện trường [38]. Các ô điểm cố định, bể chất lỏng, "
        "và giường rắn lưu hóa bằng chất lưu có thể chính xác hơn và được dùng rộng rãi trong "
        "phòng thí nghiệm hiệu chuẩn [39]. Độ sâu nhúng đủ vào vùng hiệu chuẩn đẳng nhiệt, thường "
        "ít nhất 10 đến 20 lần đường kính đầu dò, bảo đảm rằng sự dẫn nhiệt dọc theo cặp nhiệt "
        "điện từ môi trường không ảnh hưởng đến nhiệt độ mối nối. Sự quan tâm thích đáng đến tác "
        "động của dẫn nhiệt dọc trục lên nhiệt độ mối nối đo đã dẫn đến sự hiểu lầm rằng chính "
        "mối nối đang được hiệu chuẩn [30]. Rõ ràng, hiệu chuẩn cặp nhiệt điện không phải của "
        "mối nối đo; nó là của các đoạn thân nhiệt điện không xác định, ở xa mối nối đo, chỉ tại "
        "nơi chúng đi vào vùng hiệu chuẩn đẳng nhiệt qua một chuyển tiếp nhiệt độ. Các đoạn độ "
        "không đồng nhất do sử dụng đưa vào, vốn làm suy giảm nghiêm trọng độ chính xác đo, "
        "thường được đặt, trong quá trình cố gắng hiệu chuẩn lại không thành công, bên trong "
        "vùng đẳng nhiệt nơi chúng không đóng góp suất điện động Seebeck nào, nên độ không đồng "
        "nhất không bị phát hiện. Hành động hiệu chuẩn ở nhiệt độ trên 400°C thực sự có thể gây "
        "ra độ không đồng nhất và làm suy giảm độ chính xác [9, 10]. Ngay cả việc hiệu chuẩn và "
        "chứng nhận “NIST-truy nguyên” tốn kém bởi các phòng thí nghiệm hiệu chuẩn có năng lực, "
        "nếu không có sự bảo đảm riêng biệt về tính đồng nhất, cũng không phải là sự bảo đảm độ "
        "chính xác ở bất kỳ mức nào."))
    b.append(h4("Dung sai thương mại", "Commercial Tolerances"))
    b.append(p(
        "Các dung sai chuẩn hóa cho vật liệu cặp nhiệt điện mới được thiết lập bởi sự phán quyết "
        "đồng thuận chính thức của nhiều nhà sản xuất, người dùng, và nhân viên phòng thí nghiệm "
        "chuẩn hiệu chuẩn có kinh nghiệm [10, 24, 28]. Các dung sai bao gồm không chỉ độ lệch so "
        "với các đặc tính Seebeck tổng thể, mà còn bao phủ độ không đắc định không thể tránh "
        "khỏi từ độ không đồng nhất và các độ lệch không đều so với đặc tính chuẩn hóa làm trơn "
        "trên các khoảng nhỏ của nhiệt độ. Chúng áp dụng cho vật liệu khi được giao và chưa tiếp "
        "xúc với nhiệt độ quá mức. Các dung sai bảo thủ cho các kiểu cặp nhiệt điện ký hiệu chữ "
        "cái chuẩn, khi được giao, thường đáng tin cậy cho đến khi các cặp nhiệt điện tiếp xúc "
        "quá lâu với nhiệt độ quá mức hoặc môi trường bất lợi. Hiệu chuẩn lại các cặp nhiệt điện "
        "đã dùng mà không có sự bảo đảm riêng biệt về tính đồng nhất có thể gây hiểu lầm [31]. "
        "Để giải quyết các vấn đề hiệu chuẩn do độ không đồng nhất không được phát hiện, hai cách "
        "làm phổ biến. Đối với cặp nhiệt điện kim loại cơ bản giá rẻ, người ta mặc định rằng các "
        "cặp nhiệt điện chưa dùng là đồng nhất và đồng đều trong các dung sai chuẩn hóa. Đặc "
        "tính Seebeck điển hình của một lô sản xuất được nhà sản xuất hoặc người dùng đặc trưng "
        "hóa bằng cách hiệu chuẩn một hoặc nhiều mẫu đại diện thay thế đã tiêu hao. Chúng bị loại "
        "bỏ sau khi hiệu chuẩn. Lần hiệu chuẩn chu trình đầu của chúng được lấy làm đại diện cho "
        "các cặp nhiệt điện khác cùng lô. Các cặp nhiệt điện chính đã dùng có trôi được loại bỏ. "
        "Cách tiếp cận phổ biến thứ hai là hiệu chuẩn lại. Điều này thường là để đáp ứng trôi "
        "quan sát được trong sử dụng. Trôi báo hiệu độ không đồng nhất đang tiến triển. Ngoại trừ "
        "một sàng lọc độ không đồng nhất xác thực trước, không khuyến nghị hiệu chuẩn lại. Ngay "
        "cả việc hiệu chuẩn lại tại chỗ được quảng bá rộng rãi của các cặp nhiệt điện đã suy thoái "
        "cũng không có hiệu quả nếu sự phân bố nhiệt độ sẽ thay đổi trong sử dụng [31]. Dây cặp "
        "nhiệt điện bạch kim có thể được ủ toàn chiều dài bằng cách đốt nóng bằng điện trong "
        "không khí [9–12]. Các thân nhiệt điện đã ủ như vậy có thể được coi là không có độ không "
        "đồng nhất do ứng suất có thể đảo ngược, và do đó, hiệu chuẩn lại chính xác có thể được "
        "biện minh. Tuy nhiên, ủ không thể đảo ngược sự mất hiệu chuẩn từ sự di chuyển, hấp thụ, "
        "hoặc bay hơi của các thành phần hợp kim hoặc ô nhiễm hóa học khác; do đó, hiệu chuẩn lại, "
        "thậm chí của cặp nhiệt điện kim loại quý đã dùng, chỉ nên thực hiện ở nơi khả năng đồng "
        "nhất được xác lập trên thực tế. Không giống như các thân nhiệt điện kim loại cơ bản, vật "
        "liệu thân nhiệt điện kim loại quý thường có thể được tái chế. Ngoài ra, kim loại quý có "
        "giá trị thu hồi vật liệu đáng kể nếu tái chế."))
    b.append(h4("Dây nối dài", "Extension Leads"))
    b.append(p(
        "Các dây nối dài bù, mặc dù là nguồn Seebeck, thường không được hiệu chuẩn. Người ta "
        "thường giả định rằng chúng sẽ chỉ tiếp xúc với một phần nhỏ của khoảng nhiệt độ đang "
        "được đo và, nếu vậy, sẽ đóng góp không đáng kể vào sai số. Các chất cách điện nối dài "
        "được xếp hạng sử dụng liên tục đến nhiệt độ tối đa từ 105°C đến 540°C [43]. Các đặc "
        "tính Seebeck có thể không được xấp xỉ tốt trên khoảng này [1, 10]. Sự đóng góp có thể "
        "có từ các dây nối dài có thể rất lớn. Sai số khả dĩ dễ dàng ước lượng bằng mô hình trong "
        "“Mô hình chức năng của mạch nhiệt điện”. Các sai số hệ quả thường gặp hơn do dây nối dài "
        "phát sinh từ việc không kiểm soát đúng nhiệt độ các mối nối ghép nối tình cờ, như đã mô "
        "tả trong “Mạch cặp nhiệt điện thực tế”."))
    b.append(h4("Bù nhiệt độ mối nối chuẩn", "Reference Temperature Compensation"))
    b.append(p(
        "Các bộ chỉ thị cặp nhiệt điện hiện đại thường cung cấp bù nhiệt độ mối nối chuẩn bên "
        "trong. Một vài bộ cho phép bù như một lựa chọn thay thế có thể chọn. Độ chính xác của "
        "bù mối nối chuẩn, Hình 32.31(a), phụ thuộc vào độ chính xác của (các) cảm biến, f, dùng "
        "để theo dõi nhiệt độ mối nối chuẩn của các kết thúc đẳng nhiệt, nhưng cũng phụ thuộc vào "
        "sự phù hợp của thuật toán tỷ lệ hoặc mạch tương tự với đặc tính của cặp nhiệt điện cá "
        "thể. Cảm biến vùng xác định điện áp bù, E<sub>R</sub>. Một số bộ theo dõi có các khối "
        "đầu cuối đẳng nhiệt thay thế được bao gồm cảm biến nhiệt độ vùng. Thật không may, hầu "
        "hết các thiết kế theo dõi không cho phép hiệu chuẩn nhiệt riêng biệt của cảm biến nhiệt "
        "độ mối nối chuẩn. Chỉ cần nối tắt các đầu cuối đầu vào bộ chỉ thị, b–d, nên tạo ra một "
        "chỉ thị nhiệt độ gần, và thường hơi cao hơn, nhiệt độ môi trường. Các quy định claim độ "
        "không đắc định mối nối khoảng 0,1°C đến 0,5°C và các đóng góp lỗi thường nhỏ nhưng thỉnh "
        "thoảng chúng rất lớn và tiến triển xảo quyệt lên đến nhiều lần dung sai cặp nhiệt điện "
        "chuẩn [35]."))
    b.append(h4("Các dụng cụ theo dõi", "Monitoring Instruments"))
    b.append(p(
        "Độ chính xác của việc chuyển đổi suất điện động Seebeck tại các đầu cuối b–d để suy ra "
        "nhiệt độ T<sub>c</sub> đòi hỏi hiệu chuẩn dụng cụ theo dõi. Cả độ chính xác của đo điện "
        "áp và của tuyến tính hóa đều là nguồn độ không đắc định. Độ chính xác tỷ lệ dựa trên một "
        "xấp xỉ của E(<i>T</i>) xác định, chứ không dựa trên đặc tính cặp nhiệt điện cá thể. Các "
        "thiết kế dụng cụ rất đa dạng. Các nguyên lý chung của hiệu chuẩn xác thực đòi hỏi để "
        "tiếp cận độ không đắc định 0,1°C cho một bộ chỉ thị cặp nhiệt điện cung cấp bù nhiệt độ "
        "mối nối chuẩn bên trong được minh họa bằng mạch của Hình 32.31(b). Một bộ mô phỏng/"
        "hiệu chuẩn cặp nhiệt điện cung cấp một điện áp E<sub>S</sub> đã biết rõ tương ứng, cho "
        "kiểu cặp nhiệt điện chuẩn, với một điểm hiệu chuẩn nhiệt độ mong muốn. Bộ mô phỏng phải "
        "duy trì cân bằng nhiệt trong quá trình hiệu chuẩn, với suất điện động Seebeck không liên "
        "quan được triệt tiêu đúng cách. Nếu điện trở đầu vào của bộ chỉ thị rất lớn, không cần "
        "ghép điện trở của bộ mô phỏng với cặp nhiệt điện. Nếu bộ chỉ thị có điện trở đầu vào "
        "thấp hoặc tự sinh dòng <i>i</i> khi các đầu cuối b–d của nó bị nối tắt, thì sẽ xuất hiện "
        "một sai số nhiệt độ tỉ lệ với dòng bộ chỉ thị và điện trở vòng. Để có độ chính xác với "
        "các bộ chỉ thị như vậy, bộ mô phỏng R<sub>S</sub> cũng phải bắt chước điện trở nguồn "
        "của cặp nhiệt điện cá thể (R<sub>A</sub> + R<sub>B</sub>). Tuy nhiên, điện trở vòng cặp "
        "nhiệt điện đó có thể thay đổi đáng kể trong ứng dụng vì nó phụ thuộc vào sự phân bố nhiệt "
        "độ quanh cặp nhiệt điện trên một dải nhiệt độ rộng. Các đầu cuối đầu vào của bộ chỉ thị "
        "là b và d. Để hiệu chuẩn chính xác, điều thiết yếu là T<sub>b</sub> = T<sub>d</sub> = "
        "T<sub>z</sub>. Một số bộ chỉ thị và bộ bù nhiệt độ mối nối chuẩn nối khối vùng đẳng "
        "nhiệt với các đầu cuối bằng dây dẫn bù cặp nhiệt điện. Đối với những cái này, nếu "
        "T<sub>b</sub> ≠ T<sub>d</sub> ≠ T<sub>z</sub>, một sai số vô hạn phát sinh không thể "
        "khắc phục bằng hiệu chuẩn. Điện áp bộ mô phỏng phải bắt chước hành vi của chỉ cặp nhiệt "
        "điện, b–c–d. Điện áp nó phải cung cấp phụ thuộc vào việc bộ chỉ thị có hay không cung "
        "cấp bù nhiệt độ mối nối chuẩn. Nếu T<sub>b</sub> = T<sub>d</sub> = T<sub>z</sub>, tổng "
        "suất điện động Seebeck đúng là E<sub>S</sub> = E<sub>AB</sub>(T<sub>c</sub>) − "
        "E<sub>AB</sub>(T<sub>z</sub>). Nếu bộ chỉ thị không áp dụng bù E<sub>R</sub>, thì bộ "
        "mô phỏng phải cung cấp E<sub>S</sub> = E<sub>AB</sub>(T<sub>c</sub>) − "
        "E<sub>AB</sub>(T<sub>z</sub>). Nếu bộ chỉ thị có áp dụng E<sub>R</sub>, thì bộ mô phỏng "
        "chỉ phải cung cấp E<sub>S</sub> = E<sub>AB</sub>(T<sub>c</sub>). Điều này đòi hỏi "
        "nhiệt độ T<sub>z</sub> bên trong của bộ chỉ thị phải được bộ mô phỏng biết chính xác. "
        "Một số bộ mô phỏng cho phép đặt một T<sub>z</sub> giả định trong hiệu chuẩn. Những bộ "
        "không cho phép không thể dùng trực tiếp mà không có sai số để hiệu chuẩn các bộ chỉ thị "
        "bù mối nối chuẩn phổ biến. Nhiều bộ hiệu chuẩn dụng cụ cặp nhiệt điện tiện lợi cho phép "
        "đặt hiệu chuẩn mong muốn bằng nhiệt độ thay vì bằng điện áp cho các kiểu cặp nhiệt điện "
        "chuẩn hóa. Sự tiện lợi này đưa vào một tỷ lệ phi tuyến bổ sung và chỉ có sự phù hợp xấp "
        "xỉ với đặc tính chuẩn."))
    return "".join(b)


def sec_32_4f_en():
    b = [h3("Inhomogeneity")]
    b.append(h4("The Nature of Inhomogeneity"))
    b.append(p(
        "A slender thermoelement is inhomogeneous if σ<sub>M</sub>(<i>T</i>) varies along its "
        "length. The environment during application can introduce irregular inhomogeneity in one "
        "or both thermoelements of a pair. The effect is as if one or more additional dissimilar "
        "materials had been added to the circuit."))
    b.append(h4("The Significance of Inhomogeneity"))
    b.append(p(
        "Adequate thermoelectric homogeneity is the most critical assumption of thermocouple "
        "application. It usually is presumed; rarely is it confirmed. Inhomogeneity is a real but "
        "phantom problem. Inhomogeneity often remains undetected even while producing substantial "
        "error. It rarely is discovered by even the most careful conventional calibration [1, 7, "
        "11, 29–31, 33, 34]. In physical thermometry, thermocouple drift is invariably a symptom "
        "of progressing inhomogeneity. Such change is progressive, often insidious, and usually is "
        "misinterpreted [34]. Rather than envisioned correctly as localized degradation of the "
        "Seebeck coefficient, drift is often viewed improperly as a uniform “black-box” "
        "decalibration of the thermocouple rather than progressing inhomogeneity. For this reason, "
        "it is a far more commonplace problem than recognized by most experienced users. It can "
        "occur in use, in fabrication, or in calibration because of mechanical strain, thermal "
        "phase change, surface contamination, chemical interaction between materials, evaporation "
        "or migration of alloy constituents, transmutation under radiation, and a variety of "
        "other realistic causes. Inhomogeneity error in thermocouples, as manufactured, is "
        "intended to be covered by standard tolerances [1, 9, 10, 28]. Troublesome "
        "inhomogeneity is most common in used and abused thermocouples, but can sometimes occur "
        "in new thermocouples that have been individually calibrated to high temperature. It can "
        "occur within and through apparently impervious protective metal sheaths or thermal wells "
        "and between bead insulators. The example, Figure 32.30, illustrated the effect of "
        "improperly controlled junction temperatures that resulted in the subtle introduction of "
        "relative Seebeck emf from an unintended thermal pairing of segments of homogeneous "
        "thermoelements. The analogous inhomogeneity problem, best visualized with the T/X sketch, "
        "arises when a portion of one or both thermoelements locally changes in Seebeck coefficient "
        "over some nonisothermal span of the thermocouple. In effect, this introduces phantom "
        "dissimilar segments of indefinite graduated property and unrecognized location [35]. This "
        "most often occurs over a lengthy region near the measuring junction where the "
        "thermoelements are exposed to damaging environments in an oven or process. The maximum "
        "possible error of inhomogeneity is determined by the location and magnitude of greatest "
        "deviation from normal of the Seebeck coefficient. The actual error depends on the "
        "momentary distribution of temperature during use. In thermometry and in calibration, the "
        "likely error introduced by inhomogeneity is moderated. While present only within an "
        "isothermal region, inhomogeneities introduce no error. Under unfavorable temperature "
        "distributions, inhomogeneity error can be extreme and results in peculiar puzzling "
        "responses [34]. Changes of relative Seebeck coefficient by more than 60% over 25-cm "
        "spans have been observed in individually calibrated, certified, premium-grade fine wire "
        "Type R MIMS thermocouples entirely enclosed within intact platinum sheaths and exposed to "
        "temperature within the tabulated temperature range [18]."))
    b.append(h4("Testing for Inhomogeneity"))
    b.append(p(
        "Many authentic sensitive and accurate tests for thermoelectric inhomogeneity have been "
        "developed, and their practical need has been demonstrated; however, they are rarely used "
        "[33]. All true inhomogeneity tests require moving an abrupt step of temperature "
        "progressively along thermoelements. The commonplace application of a very narrow "
        "symmetric temperature pattern is the antithesis of an inhomogeneity test. It is not a "
        "test for inhomogeneity. Its popular use has misled many to discount inhomogeneity as a "
        "real and significant problem in accurate thermoelectric thermometry. Valid tests range "
        "from simple methods of low resolution to advanced methods that can accurately resolve "
        "inhomogeneity with spatial resolution of a few millimeters [21, 33]. Regrettably, as "
        "inhomogeneity errors usually are not recognized, inhomogeneity is not authentically "
        "tested in commercial practice nor by calibration laboratories. Nevertheless, invalid "
        "though certified NIST-traceable certification to great precision is possible on a "
        "thermocouple that can be accurately measured to be severely inhomogeneous and of "
        "indefinite uncertainty [29–31, 33, 34]."))

    b.append(h3("Calibration"))
    b.append(p(
        "The measurement uncertainty of most kinds of sensors can be reduced by individual "
        "calibration. Initial calibration, periodic recalibration of unused thermocouples, and "
        "even of degraded individual thermocouples, although commonplace, is often less beneficial "
        "(or even harmful) and more costly. Such ill-advised thermocouple calibration has been "
        "mandated by some “quality assurance” programs. Surveys reveal a trend for customers to "
        "demand progressively higher accuracy of thermometry [36]. In some applications, a 1°F "
        "(0.56°C) error now is deemed too large, and 0.1°F tolerance may be specified independent "
        "of temperature level. (Compare with tolerances in Table 32.12.) There are a few "
        "industrial applications that truly require such accuracy. More often, the specification "
        "merely presumes that such accuracy in thermocouple thermometry is routinely attainable "
        "merely by calibration. Calibration is an opiate of quality assurance. The illusion of "
        "accuracy provided by NIST-traceable certified calibration and purported in situ calibration "
        "is counterproductive if it is not authentic. Consideration of the details of thermocouple "
        "calibration suggests why authentic accuracy at the 0.1°C level is unlikely in industrial "
        "thermoelectric thermometry. The approach to achieving authentic calibration of "
        "thermocouple system accuracy (ignoring thermal coupling and transient response errors) is "
        "illustrated in Figure 32.31. Figure 32.31(a) represents the thermocouple system to be "
        "calibrated. Calibration for thermoelectric thermometry must distinguish three system "
        "components: (1) the thermocouple circuit, (2) the reference junction temperature "
        "compensator, and (3) the monitoring instrument. Each separately affects temperature "
        "uncertainty."))
    b.append(fig(31, F.fig(31), "en"))
    b.append(h4("The Principal Thermocouple"))
    b.append(p(
        "Calibration of principal thermocouples is performed by immersing the vicinity of the "
        "measuring junction in the isothermal region of a bath or oven [37]. Several compact "
        "dry-well calibrators available are convenient for calibration at the job site [38]. "
        "Fixed-point cells, liquid baths, and fluidized solid beds can be more accurate and are "
        "widely used in the calibration laboratory [39]. Sufficient depth of immersion into an "
        "isothermal calibration zone, usually at least 10 to 20 times the probe diameter, ensures "
        "that conduction of heat along the thermocouple from the environment does not affect the "
        "junction temperature. The appropriate concern for the effect of longitudinal heat "
        "conduction on measuring junction temperature has led to the misperception that it is the "
        "junction that is being calibrated [30]. Clearly, thermocouple calibration is not of the "
        "measuring junction; it is of unidentified segments of thermoelements, remote from the "
        "measuring junction, only where they enter the isothermal calibration zone through a "
        "temperature transition. Segments of service-induced inhomogeneity that seriously degrade "
        "measurement accuracy are often placed, during unsuccessful attempted recalibration, within "
        "the isothermal region where they contribute no Seebeck emf, so inhomogeneity is not "
        "discovered. The act of calibration at temperatures above 400°C can actually induce "
        "inhomogeneity and degrade accuracy [9, 10]. Not even costly “NIST-traceable” calibration "
        "and certification by competent calibration laboratories, without specific assurance of "
        "homogeneity, are a guarantee of accuracy at any level."))
    b.append(h4("Commercial Tolerances"))
    b.append(p(
        "Standardized tolerances for new thermocouple materials are established by the formal "
        "consensus judgment of many experienced producers, users, and calibration standards "
        "laboratories staff [10, 24, 28]. The tolerances include not only deviation from the "
        "overall Seebeck properties, but also cover inevitable uncertainty from inhomogeneity and "
        "irregular deviations from the smoothed standardized characteristic over small spans of "
        "temperature. They apply to material as delivered and not exposed to excessive temperature. "
        "The conservative tolerances for standard letter-designated thermocouple types as delivered "
        "are usually reliable until the thermocouples are exposed too long to excessive "
        "temperatures or adverse environments. Recalibration of used thermocouples without "
        "separate assurance of homogeneity can be misleading [31]. To address calibration problems "
        "presented by undiscovered inhomogeneity, two practices are common. For inexpensive base "
        "metal thermocouples, it is presumed that unused thermocouples are homogeneous and uniform "
        "within standardized tolerances. The typical Seebeck property of a production batch is "
        "characterized by the manufacturer or user by calibrating one or more expended surrogate "
        "samples. These are discarded after calibration. Their first-cycle calibration is taken as "
        "representative of other thermocouples of the same batch. Used principal thermocouples that "
        "have experienced drift are discarded. A commonplace second approach is recalibration. "
        "This is usually in response to drift observed in service. Drift signals progressing "
        "inhomogeneity. Apart from an authentic inhomogeneity prescreening, recalibration is not "
        "recommended. Even widely promoted in situ recalibration of degraded thermocouples is "
        "ineffective if temperature distribution will vary in use [31]. Platinum-based thermocouple "
        "wire can be annealed full length by electrically heating in air [9–12]. Such annealed "
        "thermoelements can be presumed to be free of reversible strain-induced inhomogeneity and, "
        "thus, accurate recalibration might be justified. However, annealing cannot reverse "
        "decalibration from the migration, absorption, or evaporation of alloy constituents or "
        "other chemical contamination; therefore, recalibration, even of used precious metal "
        "thermocouples, should be performed only where the likelihood of homogeneity is factually "
        "based. Unlike base metal thermoelements, precious metal thermoelement materials often can "
        "be reconditioned. Also, precious metals have a significant material salvage value if "
        "recycled."))
    b.append(h4("Extension Leads"))
    b.append(p(
        "Compensating extension leads, although Seebeck sources, usually are not calibrated. It is "
        "commonly assumed that they will be exposed to only a small fraction of the temperature "
        "span that is being measured and, if so, will contribute insignificantly to error. "
        "Extension insulations are rated for continuous use to maximum temperatures between 105°C "
        "and 540°C [43]. Seebeck characteristics might not be well approximated over this range [1, "
        "10]. The possible contribution from extensions can be very large. The plausible error is "
        "easily estimated using the model in “The Functional Model of Thermoelectric Circuits.” "
        "The more usual consequential errors due to extension leads result from failure to "
        "correctly control the temperatures of incidental splice junctions, as described in "
        "“Practical Thermocouple Circuits”."))
    b.append(h4("Reference Temperature Compensation"))
    b.append(p(
        "Modern thermocouple indicators usually provide internal reference junction temperature "
        "compensation. A few make compensation a selectable alternative. The accuracy of reference "
        "junction compensation, Figure 32.31(a), depends on the accuracy of the sensor(s), f, used "
        "to monitor reference junction temperature of isothermal terminations, but also on the "
        "conformity of the scaling algorithm or analog circuitry to the characteristic of the "
        "individual thermocouple. The zone sensor determines the compensating voltage, E<sub>R</sub>. "
        "Some monitors have replaceable isothermal terminal blocks that include the zone temperature "
        "sensor. Most monitor designs unfortunately do not allow separate thermal calibration of "
        "the reference temperature sensor. Simply shorting the indicator input terminals, b–d, "
        "should produce a temperature indication near, and usually slightly above, ambient "
        "temperature. Specifications claim reference uncertainty on the order of 0.1°C to 0.5°C "
        "and error contributions usually are small but infrequently they have been very large and "
        "insidiously progressive up to many times the standard thermocouple tolerances [35]."))
    b.append(h4("Monitoring Instruments"))
    b.append(p(
        "The accuracy of conversion of the Seebeck voltage at terminals b–d to deduce the "
        "temperature T<sub>c</sub> requires calibration of the monitoring instrument. Both the "
        "accuracy of voltage measurement and of linearization are sources of uncertainty. The "
        "scaling accuracy is based on an approximation of the defining E(<i>T</i>), and not on the "
        "individual thermocouple characteristic. Instrument designs are varied. The general "
        "principles of authentic calibration required to approach 0.1°C uncertainty for a "
        "thermocouple indicator that provides internal reference temperature compensation are "
        "illustrated with the circuit of Figure 32.31(b). A thermocouple simulator/calibrator "
        "supplies a well-known voltage E<sub>S</sub> that corresponds, for the standard "
        "thermocouple type, to a desired temperature calibration point. The simulator must remain "
        "in thermal equilibrium during calibration, with irrelevant Seebeck voltage properly "
        "nulled. If the input resistance of the indicator is very large, resistance matching of the "
        "simulator to the thermocouple is not required. If the indicator has a low input resistance "
        "or it internally produces current <i>i</i> when its terminals b–d are shorted, then a "
        "temperature error proportional to the indicator current and the loop resistance will be "
        "experienced. For accuracy with such indicators, the simulator R<sub>S</sub> must also "
        "mimic the source resistance of the individual thermocouple (R<sub>A</sub> + "
        "R<sub>B</sub>). However, that thermocouple loop resistance may vary considerably in "
        "application as it depends on the temperature distribution around the thermocouple over a "
        "broad range of temperatures. The input terminals of the indicator are b and d. For "
        "accurate calibration, it is essential that T<sub>b</sub> = T<sub>d</sub> = T<sub>z</sub>. "
        "Some indicators and reference temperature compensators connect the isothermal zone block "
        "to the terminals with compensating thermocouple leads. For these, if T<sub>b</sub> ≠ "
        "T<sub>d</sub> ≠ T<sub>z</sub>, an indefinite error results that cannot be overcome by "
        "calibration. The simulator voltage must imitate the behavior of only the thermocouple, "
        "b–c–d. The voltage it must provide depends on whether or not the indicator supplies "
        "internal reference temperature compensation. If T<sub>b</sub> = T<sub>d</sub> = "
        "T<sub>z</sub>, the proper total Seebeck voltage is E<sub>S</sub> = E<sub>AB</sub>"
        "(T<sub>c</sub>) − E<sub>AB</sub>(T<sub>z</sub>). If the indicator does not apply "
        "compensation E<sub>R</sub>, then the simulator must provide E<sub>S</sub> = "
        "E<sub>AB</sub>(T<sub>c</sub>) − E<sub>AB</sub>(T<sub>z</sub>). If the indicator does "
        "apply E<sub>R</sub>, then the simulator must supply only E<sub>S</sub> = "
        "E<sub>AB</sub>(T<sub>c</sub>). This requires that the internal T<sub>z</sub> of the "
        "indicator be accurately known by the simulator. Some simulators allow setting a presumed "
        "T<sub>z</sub> in calibration. Those that do not cannot be used directly without error for "
        "calibration of the commonplace reference temperature compensating indicators. Many "
        "convenient thermocouple instrument calibrators allow setting the desired calibration by "
        "temperature rather than by voltage for standardized thermocouple types. This convenience "
        "introduces an additional nonlinear scaling and only approximate conformity to the standard "
        "characteristic."))
    return "".join(b)


def _t3215(lang):
    vi = lang == "vi"
    hd = (["Kiểu", "0,025", "0,127", "0,254", "0,406", "0,813", "1,600", "3,175"] if vi else
          ["Type", "0.025", "0.127", "0.254", "0.406", "0.813", "1.600", "3.175"])
    rows = [
        ("E", "290", "325", "370", "400", "510", "775", "855"),
        ("J", "230", "275", "305", "350", "460", "600", "750"),
        ("K, N", "690", "730", "790", "840", "950", "1095", "1250"),
        ("T", "90", "110", "150", "185", "270", "370", "375"),
    ]
    cap = ("Bảng 32.15 · Giới hạn nhiệt độ trên cho các đường kính dây khác nhau "
           "(mm / in. / AWG: 0,025 mm = 0,001 in. = AWG 50 … 3,175 mm = 0,125 in. = AWG 8). "
           "Từ Tài liệu [1, 9, 13]." if vi else
           "Table 32.15 · Temperature Upper Limits For Different Wire Diameters "
           "(mm / in. / AWG: 0.025 mm = 0.001 in. = AWG 50 … 3.175 mm = 0.125 in. = AWG 8). "
           "From References [1, 9, 13].")
    return table(hd, rows, cap, small=True)


def _t3216(lang):
    vi = lang == "vi"
    hd = (["Kiểu", "Giàu O₂", "Nghèo O₂", "Khử", "Chân không", "Ẩm",
           "Dưới 0°C (vết)", "Lưu huỳnh", "Bức xạ nơtron"] if vi else
          ["Type", "Oxygen rich", "Oxygen poor", "Reducing", "Vacuum", "Humid",
           "Below 0°C traces", "Sulfur", "Neutron radiation"])
    rows = [
        ("B", "Good", "Good", "Poor", "Fair", "Good", "Poor", "Poor", "Fair"),
        ("E", "Good", "Poor", "Poor", "Poor", "Good", "Good", "Poor", "Poor"),
        ("J", "Fair", "Good", "Good", "Good", "Poor", "Poor", "Fair", "Poor"),
        ("K", "Good", "Poor", "Poor", "Poor", "Good", "Fair", "Poor", "Good"),
        ("N", "Good", "Fair", "Poor", "Poor", "Good", "Good", "Fair", "Good"),
        ("R, S", "Good", "Good", "Poor", "Poor", "Good", "Fair", "Poor", "Poor"),
        ("T", "Fair", "Fair", "Good", "Good", "Good", "Good", "Fair", "Poor"),
    ]
    cap = ("Bảng 32.16 · Khả năng chịu môi trường của các cặp nhiệt điện ký hiệu chữ cái. "
           "Từ Tài liệu [1, 4, 9, 10, 43]." if vi else
           "Table 32.16 · Environmental Tolerance of Letter Designated Thermocouples. "
           "From References [1, 4, 9, 10, 43].")
    return table(hd, rows, cap, small=True)


def sec_32_4g_vi():
    b = [h3("Hỏng và kiểm định cặp nhiệt điện", "Thermocouple Failure and Validation")]
    b.append(p(
        "Một phép đo cặp nhiệt điện đã thất bại khi các chỉ thị của nó vượt quá giới hạn độ "
        "không đắc định yêu cầu cho một phép đo. Cặp nhiệt điện thỉnh thoảng hỏng “hở” khi các "
        "mối nối tách rời hoặc các thân nhiệt điện bị ăn mòn, chảy dẻo, hoặc nóng chảy. Chỉ thị "
        "“mạch hở” rõ ràng là một tính năng được quảng bá của nhiều bộ chỉ thị cặp nhiệt điện "
        "hiện đại. Chỉ thị phổ biến này hữu ích, nhưng không phải là một chỉ thị đầy đủ về tính "
        "toàn vẹn cặp nhiệt điện. Các hỏng mạch ít rõ ràng hơn nhưng thường gặp hơn là do sự rẽ "
        "nhánh không rõ ràng, nối tắt, hoặc độ không đồng nhất tiến triển của các thân nhiệt điện. "
        "Những cái này không được phát hiện bởi chỉ thị “mạch hở”. Việc chỉ thị liên tục một "
        "nhiệt độ khả dĩ không phải là bằng chứng của phép đo nhiệt độ xác thực. Một sự rẽ nhánh "
        "hoặc nối tắt điện deliberate hoặc accidental giữa các thân nhiệt điện ở nhiệt độ môi "
        "trường gần một mối nối chuẩn bù điện tử nên dẫn đến một chỉ thị gần nhiệt độ môi trường, "
        "không phải 0°C. Một sự hỏng cặp nhiệt điện do nối tắt trực tiếp giữa các thân nhiệt điện "
        "ở một khoảng cách nào đó từ các mối nối đo hoặc chuẩn dự định có thể không bị phát hiện "
        "vì nó xảy ra trong một vùng nhiệt độ rất khác với nhiệt độ chuẩn và nơi một phép đo "
        "nhiệt độ hợp lệ hoặc khả dĩ có thể tiếp tục được thực hiện nhưng tại một vị trí không "
        "liên quan, không mong đợi và không được nhận ra [35]. Trong một số tình huống, như trong "
        "các môi trường thù địch có thể dự đoán, sự hỏng như vậy của một số cặp nhiệt điện trong "
        "sử dụng là được dự báo trước. Nơi sự hỏng là do hư hại mạch cặp nhiệt điện, nó có thể "
        "không rõ ràng ngay lập tức (hoặc bao giờ) nếu không có chẩn đoán mạch đặc biệt. Đối với "
        "các tình huống nguy kịch như vậy, các mạch nhiệt điện đặc biệt và các phương pháp theo "
        "dõi đã được phát triển để đánh giá tính toàn vẹn mạch tiếp tục, mặc dù không phải độ "
        "chính xác, của đo nhiệt độ [35]."))
    b.append(h4("Tương thích môi trường", "Environmental Compatibility"))
    b.append(p(
        "Một cân nhắc hàng đầu trong chọn lựa cặp nhiệt điện là sự tương thích của các thân nhiệt "
        "điện với vỏ bảo vệ của chúng và của cả hai thân nhiệt điện với môi trường đo. Các thân "
        "nhiệt điện phải được bảo vệ khỏi các môi trường ăn mòn và chất lỏng hoặc rắn dẫn điện "
        "gây rẽ nhánh. Chất cách điện nhựa, gốm, hoặc sợi, các vỏ kim loại, và các giếng nhiệt "
        "được dùng để phục vụ chức năng này nhưng có thể hỏng trong sử dụng [1, 9–12, 25]. Vật "
        "liệu cách điện dạng hạt nén của cặp nhiệt điện kim loại bọc cách nhiệt khoáng, nếu bị "
        "lộ, nhanh chóng hấp thụ độ ẩm có thể làm suy giảm nghiêm trọng sự cách ly điện trở [1, "
        "10–12]. Khi cắt, các đầu vỏ cặp nhiệt điện MIMS phải được bịt kín lại nhanh chóng để "
        "tránh hấp thụ độ ẩm. Chất cách điện sợi và hạt dễ bị nhiễm bẩn và có thể làm suy giảm "
        "độ chính xác [1, 10]."))
    b.append(h4("Tiếp xúc nhiệt độ", "Temperature Exposure"))
    b.append(p(
        "Các biến môi trường không thể tránh khỏi trong đo nhiệt độ là nhiệt độ và thời gian. "
        "Mặc dù các thân nhiệt điện có thể không bị ảnh hưởng rõ rệt bởi một môi trường, hệ số "
        "Seebeck có thể bị suy giảm đáng kể. Ngay cả nếu chỉ một lớp bề mặt rất mỏng của một "
        "thân nhiệt điện bị biến đổi, hệ số Seebeck cũng có thể thay đổi. Các đặc tính có thể bị "
        "suy giảm bởi sử dụng trong thời gian dài, ở nhiệt độ cực đoan, và trong các môi trường "
        "bất lợi [1, 9–12]. Vì những lý do này, ứng dụng nên giới hạn trong các giới hạn nhiệt "
        "độ được đề xuất (Bảng 32.15). Hiệu chuẩn nên được thực hiện nhanh chóng, chỉ cho phép "
        "thời gian để cân bằng, và chỉ đến nhiệt độ tối đa của sử dụng dự định. Sự suy giảm, "
        "quan sát trong sử dụng như sự không ổn định hoặc trôi, nhất thiết là triệu chứng của độ "
        "không đồng nhất đang tiến triển [30, 31]. Sự tiếp xúc quá mức kéo dài một mình có thể "
        "nhanh chóng làm suy giảm một thân nhiệt điện. Các điểm nóng chảy xác định giới hạn "
        "nhiệt độ tuyệt đối trên của sử dụng cặp nhiệt điện. Tuy nhiên, dưới giá trị xác định "
        "này, có các giới hạn ứng dụng vô hạn mà tại đó độ ổn định có thể bị giảm đáng kể [1, "
        "9–12]. Các bảng cặp nhiệt điện chuẩn chỉ mở rộng đến nhiệt độ lớn nhất của sử dụng đề "
        "xuất cho các môi trường bảo vệ lành tính, thời gian ngắn, và cho vật liệu dây có đường "
        "kính 3 mm hoặc lớn hơn [1, 9, 10]. Các giới hạn nhiệt độ giảm đáng kể áp dụng cho vật "
        "liệu có tiết diện nhỏ hơn, Bảng 32.14 [1]. Các cặp nhiệt điện có tiết diện nhỏ hơn suy "
        "giảm nhanh hơn. Các dung sai chuẩn chỉ áp dụng cho vật liệu khi được sản xuất."))
    b.append(h4("Môi trường hóa học", "Chemical Environment"))
    b.append(p(
        "Có các hướng dẫn rộng cho sự tương thích môi trường. Các khuyến nghị này có điều kiện và "
        "phụ thuộc nghiêm ngặt vào nhiều đặc thù của sự tiếp xúc. Một tóm tắt ngắn gọn về các "
        "đặc tính tương thích môi trường được cho trong Bảng 32.16. Các tài liệu tham khảo nên "
        "được tham khảo để có thông tin tương thích chi tiết [1, 4, 9, 22, 23]. Nhiều danh mục "
        "cặp nhiệt điện bao gồm các bảng các môi trường hóa học thường chịu đựng được cho các "
        "thân nhiệt điện hoặc vật liệu giếng nhiệt [19, 20]. Kinh nghiệm dịch vụ khi làm việc với "
        "khách hàng trong nhiều môi trường quy trình đa dạng đôi khi cho phép các nhà sản xuất tư "
        "vấn cho người dùng về các vấn đề tương thích đặc biệt. Thường, sự phù hợp trong một "
        "dịch vụ cụ thể chỉ có thể được bảo đảm bằng thử nghiệm."))
    b.append(h4("Biến đổi luyện kim", "Metallurgical Change"))
    b.append(p(
        "Các thân nhiệt điện hợp kim có thể thay đổi thành phần cục bộ bằng sự bay hơi các thành "
        "phần khi tiếp xúc với chân không. Các thành phần hợp kim bay hơi từ một vỏ hoặc từ một "
        "thân nhiệt điện có thể bám và phủ các thân nhiệt điện kề cận ngay cả qua chất cách điện "
        "[1, 9–12, 24, 30, 31]. Các thành phần hợp kim có thể di chuyển từ thân nhiệt điện này "
        "sang thân nhiệt điện kia qua mối nối đo. Các vết nhiễm bẩn có thể xuyên qua các lỗ kim "
        "và vết nứt tóc và thực sự có thể khuếch tán qua các vỏ bảo vệ còn nguyên vẹn. Các tạp "
        "chất vi lượng trong vỏ hoặc vật liệu cách điện có thể tương tác với các thân nhiệt điện. "
        "Việc xây dựng MIMS và chọn vật liệu thích hợp thường kéo dài tuổi thọ và tăng giới hạn "
        "nhiệt độ, nhưng sự hư hại có thể xảy ra ngay cả trong các cụm có vẻ hoàn toàn được bọc "
        "[34]. Ứng suất quá mức có thể thay đổi đáng kể cục bộ hệ số Seebeck của một hoặc cả hai "
        "thân nhiệt điện dẫn đến độ không đồng nhất. Sự ứng suất rất cục bộ, như do các uốn cong "
        "sắc, thường có ít tác động đến đo nhiệt độ thực tế."))
    b.append(_t3215("vi"))
    b.append(_t3216("vi"))
    b.append(h3("Thu thập dữ liệu", "Data Acquisition"))
    b.append(h4("Các bộ chỉ thị cặp nhiệt điện", "Thermocouple Indicators"))
    b.append(p(
        "Nhà thiết kế dụng cụ có thể che chở người dùng khỏi nhiều chi tiết phiền toái làm phức "
        "tạp phép đo cho những người tiên phong cặp nhiệt điện. Độ phân giải tín hiệu mức "
        "microvolt, điện trở đầu vào cao, độ ổn định, giảm nhiễu, tỷ lệ phi tuyến, và bù nhiệt độ "
        "mối nối chuẩn giờ đây được cung cấp thường quy để cho phép người dùng tập trung vào phép "
        "đo hơn là vào các chi tiết của chỉ thị hoặc ghi chép nó. Một số bộ chỉ thị cặp nhiệt điện "
        "cầm tay và chỉ chứa một cặp nhiệt điện duy nhất và chỉ của một kiểu duy nhất. Một vài bộ "
        "cung cấp đầu vào kép cặp nhiệt điện và cho phép đo nhiệt độ hiệu trực tiếp mà bù mối nối "
        "chuẩn không được áp dụng trực tiếp. Các đơn vị để bàn khác chứa được nhiều đầu vào cặp "
        "nhiệt điện cùng kiểu hoặc hỗn hợp cặp nhiệt điện và các kiểu cảm biến khác. Độ chính xác "
        "dụng cụ được claim có thể đánh lừa người đọc qua loa. Mặc dù nhiều dụng cụ được cung "
        "cấp đầy đủ với một đầu dò cặp nhiệt điện, một số quy định độ chính xác chỉ mô tả độ "
        "chính xác của đo điện áp đầu cuối đầu vào. Độ chính xác dụng cụ thực tế nên được xác định "
        "bằng hiệu chuẩn điện (xem phần “Hiệu chuẩn”). Thỉnh thoảng, sai số của dụng cụ chỉ thị "
        "trở nên lớn hơn đáng kể so với quy định do trôi bù mối nối chuẩn, offset, hoặc gain. Độ "
        "không đắc định bổ sung của hiệu chuẩn cặp nhiệt điện, Bảng 32.13, và sự khác biệt thường "
        "lớn hơn giữa nhiệt độ mối nối đo và nhiệt độ thực của vật được đo, không thể bao gồm vì "
        "cái sau được chi phối bởi các chi tiết của truyền nhiệt và đáp ứng nhiệt quá độ."))
    b.append(h4("Các bộ truyền cặp nhiệt điện", "Thermocouple Transmitters"))
    b.append(p(
        "Một dạng ít quen thuộc hơn của điều chế tín hiệu cặp nhiệt điện, bộ truyền cặp nhiệt "
        "điện, rất phổ biến trong các ngành công nghiệp quy trình [4, 39]. Hầu hết các bộ truyền "
        "cặp nhiệt điện hai dây (không phải bộ truyền vô tuyến RF) là các thiết bị kênh đơn thực "
        "hiện bù mối nối chuẩn, tuyến tính hóa, và cách ly, và truyền thông tin điều chế đến một "
        "vị trí theo dõi từ xa [1]. Bộ truyền chuyển đổi suất điện động Seebeck được tỷ lệ theo "
        "nhiệt độ thành một tín hiệu tương tự để truyền dây qua các đường dài đến một vị trí ghi "
        "hoặc theo dõi từ xa. Các bộ điều chế tín hiệu đơn cảm biến nhỏ gọn và rẻ tiền như vậy có "
        "sẵn được chuyên biệt hóa cho hầu hết các biến quy trình. Các bộ truyền cặp nhiệt điện rất "
        "thích hợp để theo dõi các nhiệt độ thay đổi chậm tại các vị trí theo dõi xa mối nối đo. "
        "Nhiều bộ được cách ly điện vì an toàn. Một số được thích nghi để sử dụng với hệ thống "
        "lắp ray DIN. Một bộ truyền có thể được lắp gần mỗi cặp nhiệt điện. Một số đủ nhỏ để lắp "
        "trong đầu nối của một giếng nhiệt. Tín hiệu truyền có thể có dạng điều chế dòng hoặc điều "
        "chế áp theo các chuẩn ISA. Bộ truyền kiểu dòng điều chế nhiệt độ, tỉ lệ với nhiệt độ, một "
        "dòng dc cung cấp từ vị trí theo dõi. Tín hiệu nằm trong khoảng từ 4 mA đến 20 mA. Bộ "
        "truyền kiểu dòng truyền thông tin qua những khoảng cách lớn mà không có sự mất áp đi "
        "kèm với truyền áp đường dài. Một số bộ truyền kiểu áp điều chế một điện áp cung cấp trên "
        "khoảng từ 1 Vdc đến 5 Vdc. Offset và tỷ lệ cho một số được điều chỉnh tại bộ truyền. "
        "Một số bộ truyền giờ đây có đầu đọc số tại chỗ, và tỷ lệ và offset có thể được điều "
        "chỉnh từ xa [4, 39]."))
    b.append(h4("Ghi chép", "Recording"))
    b.append(p(
        "Một số bộ ghi dữ liệu cặp nhiệt điện đa kênh giờ đây dùng pin để sử dụng độc lập và nhỏ "
        "gọn đủ để cầm tay [41]. Một số bộ ghi đơn giản giờ đây có giá dưới 200 USD. Các đơn vị "
        "tinh vi hơn chứa được nhiều cặp nhiệt điện cùng kiểu hoặc hỗn hợp. Các bộ ghi dữ liệu số "
        "lớn hơn với bộ ghép kênh tuần tự lấy mẫu đầu ra từ các cặp nhiệt điện cá thể có thể chứa "
        "đến vài trăm đầu vào và có thể ghi hỗn hợp cả tín hiệu cặp nhiệt điện và tín hiệu khác ở "
        "các khoảng lấy mẫu có thể lập trình từ vài miligiây đến vài giờ hoặc ngày. Sự chuyển "
        "mạch ba dây mong muốn giữa các cặp nhiệt điện là phổ biến. Các máy tính cá nhân giờ đây "
        "chứa được các bo mạch thu thập dữ liệu số nội bộ rẻ tiền có thể chuyển đổi máy tính "
        "thành một hệ thống ghi nhiệt độ độ phân giải cao. Máy tính xách tay có thể chấp nhận các "
        "thẻ cắm PCMCIA cỡ lòng bàn tay đặc biệt cho đầu vào cặp nhiệt điện đa kênh. Các hệ thống "
        "thu thập dữ liệu dựa trên máy tính số với phần mềm chuyên biệt cho thu thập, phân tích, "
        "và trình bày dữ liệu, cho phép người dùng áp dụng bù nhiệt độ mối nối chuẩn đặc biệt, "
        "tuyến tính hóa tùy chỉnh các hàm tỷ lệ cặp nhiệt điện cho cả hiệu chuẩn chuẩn hoặc cá "
        "thể và của các kiểu cặp nhiệt điện đặc biệt. Các hệ thống cặp nhiệt điện dựa trên máy "
        "tính với phần mềm thương mại thu thập dữ liệu và khác thích hợp, cung cấp cho thiết kế "
        "thí nghiệm, dự đoán, thu thập dữ liệu, quản lý thông tin, phân tích, báo cáo, lưu trữ, "
        "và truyền thông trong một máy tính xách tay nhỏ gọn, có thể triển khai hiện trường [42]."))
    b.append(h3("Truyền tín hiệu", "Signal Transmission"))
    b.append(p(
        "Chiều dài của cặp nhiệt điện chính nên càng ngắn càng khả thi. Các thân nhiệt điện nên "
        "liên tục giữa mối nối đo và mối nối chuẩn để có độ chính xác tốt nhất, nhưng các cáp nối "
        "dài có thể được dùng nếu cần (xem phần “Mạch cặp nhiệt điện thực tế”). Trong các thí "
        "nghiệm hiện trường và trong giám sát quy trình, việc ghi chép có thể cách mối nối đo "
        "hàng trăm mét. Có một số khả năng thỏa đáng cho truyền tín hiệu qua những khoảng cách "
        "lớn."))
    b.append(h4("Cáp nối dài", "Extension Cable"))
    b.append(p(
        "Các cáp nối dài nhiệt điện khớp và bù (xem phần “Mạch cặp nhiệt điện thực tế”) có sẵn "
        "trong nhiều cấu tạo và chất cách điện [4, 43]. Một cáp nối dài, như một đường truyền, có "
        "thể là một cặp nhiệt điện xoắn đôi đơn hoặc một cáp đa cặp được thiết kế để triệt tiêu cả "
        "nhiễu điện tĩnh và điện từ và để bảo vệ môi trường. Trong khi dây nối dài cách điện "
        "không bọc kém rẻ tiền có sẵn, trong tình huống phổ biến nơi nhiễu điện có khả năng xảy "
        "ra, mỗi dây nối dài nên là một cặp xoắn đôi cách điện, được bọc riêng, và xoắn. Nơi một "
        "số cặp nối dài từ một cụm các cặp nhiệt điện gần nhau kéo dài đến một bộ ghi từ xa, cáp "
        "nhiệt điện đa cặp có sẵn thêm một lớp che chắn tĩnh điện tổng thể, gia cố tăng cường cơ "
        "học, và một áo khoác môi trường bền để bảo vệ khỏi hư hại cơ học và xâm nhập hóa học "
        "trong các môi trường quy trình khắc nghiệt [4, 42]. Việc nối dài nhiệt điện công phu như "
        "vậy đắt hơn cáp dụng cụ đồng; do đó, các hệ thống truyền thay thế nên được xem xét. Việc "
        "sử dụng đúng cách cáp dụng cụ đồng xoắn đôi làm dây nối trung tính, kéo dài từ bù nhiệt "
        "độ mối nối chuẩn bên ngoài, có thể đủ và rẻ hơn các dây nối nhiệt điện. Cáp dụng cụ xoắn "
        "đôi có chất lượng cao hơn cũng có thể cải thiện độ trung thực tín hiệu trong đo nhiệt độ "
        "quá độ. Đối với các dây nối trung tính như vậy, chỉ nên dùng cặp đồng rắn không mạ cách "
        "điện dụng cụ vì độ dày mạ không đều có thể dẫn đến độ không đồng nhất phân bố không đều "
        "và gây nhiễu suất điện động Seebeck. Cáp dụng cụ đồng trục thông thường không bao giờ "
        "được dùng làm dây nối nhiệt điện trung tính dài vì lớp bện ngoài và dây dẫn tâm có hệ số "
        "Seebeck rất khác nhau. Nếu không ở nhiệt độ đồng nhất, cáp có thể là một nguồn đáng kể "
        "của nhiễu suất điện động Seebeck. Các dây nối nhiệt điện và các cụm “pigtailed” nên "
        "được kiểm tra toàn chiều dài để tìm các mối nối ẩn giữa các thân nhiệt điện ghép nối hơi "
        "không khớp và các mối ghép cặp cố ý nhưng ẩn, được làm sai với cực tính bị đảo [10]. Cho "
        "một nguồn nhiệt hẹp đi dọc toàn bộ chiều dài cáp, trong khi theo dõi các bước nhảy cục "
        "bộ của đầu ra gần các mối nối không chủ định đó, bằng một bộ chỉ thị cặp nhiệt điện. "
        "Phép thử này rất hiệu quả để xác định chính xác các mối nối ẩn. Nó không thử nghiệm độ "
        "không đồng nhất [10, 30]."))
    b.append(h4("Truyền vô tuyến", "Wireless Transmission"))
    b.append(p(
        "Trong một số tình huống, truyền dây đồng kém hiệu quả, đắt hơn, hoặc kém tiện lợi hơn "
        "các phương pháp vô tuyến. Một số hệ thống thu thập dữ liệu vô tuyến giá rẻ (không phải "
        "bộ truyền cặp nhiệt điện) giờ đây được thích nghi để kết hợp thu thập dữ liệu cặp nhiệt "
        "điện và truyền tín hiệu từ xa [44]. Các modem vô tuyến truyền dữ liệu từ một vị trí đo "
        "đến các vị trí ghi cách xa đến 5 km. Hầu hết cung cấp truyền phổ trải rộng không đòi hỏi "
        "giấy phép thông tin liên lạc. Truyền dữ liệu vô tuyến có thể đặc biệt kinh tế ở nơi "
        "khoảng cách giữa mối nối đo và bộ ghi lớn, khi nhiều cặp nhiệt điện phải được ghi, khi ít "
        "thời gian thiết lập sẵn cho cáp hiện trường, và nơi thiết lập đo phải thỉnh thoảng di "
        "chuyển. Một số hệ thống kết hợp ghi dữ liệu và thông tin vô tuyến trong một đơn vị duy "
        "nhất. Các hệ thống khác đòi hỏi sử dụng một bộ truyền cặp nhiệt điện, một bộ ghi dữ "
        "liệu, và modem vô tuyến để tạo thành một hệ thống. Cáp sợi quang với các bộ phát thu "
        "điện-quang có thể được dùng cho truyền cáp không nhiễu điện qua khoảng cách dài giữa "
        "điều chế tín hiệu cục bộ tại cặp nhiệt điện và một bộ ghi hoặc theo dõi từ xa."))
    b.append(h3("Các nguồn thông tin ứng dụng cặp nhiệt điện",
                "Sources of Thermocouple Application Information"))
    b.append(h4("Các bài báo kỹ thuật", "Technical Papers"))
    b.append(p(
        "Các nguồn tập trung và rộng nhất của các bài báo kỹ thuật được bình duyệt đề cập đến đo "
        "nhiệt độ cặp nhiệt điện là các kỷ yếu nối tiếp của một hội nghị quốc tế mười năm một lần "
        "về nhiệt độ [25]. Sáu tập đến nay là một nguồn phong phú và đáng tin cậy của dữ liệu ứng "
        "dụng. Các kỷ yếu của các hội nghị thường niên của ISA và NCSL cũng có một vài bài báo mô "
        "tả các phát triển hiện tại trong đo nhiệt độ. Tài liệu [26] có dữ liệu nhiệt điện về sự "
        "đa dạng rộng nhất của các vật liệu thông dụng và không chuẩn. Các bài báo hiện tại dành "
        "riêng, không phải ngẫu nhiên, cho các cặp nhiệt điện thì hiếm và được phân bố rộng rãi "
        "qua các tạp chí thương mại và các tạp chí của các hội nghề nghiệp. Các chi tiết thiết yếu "
        "của đo nhiệt độ cặp nhiệt điện thường được mô tả (nghèo nàn) chỉ ngẫu nhiên trong các "
        "báo cáo của các nghiên cứu thực nghiệm. Một số nhà sản xuất phát hành các tạp chí kỹ "
        "thuật đăng ký chuyên về đo nhiệt độ [45]. Một tạp chí đo lường thường xuyên công bố các "
        "bài về đo nhiệt độ ứng dụng và, hàng năm trong số tháng Sáu, công bố một thư mục rộng "
        "các nhà sản xuất vật liệu cặp nhiệt điện và dụng cụ liên quan [46]. Thư mục bao gồm, cho "
        "vài chục nhà sản xuất được liệt kê, các mô tả ngắn gọn về các sản phẩm được chọn và giá "
        "cả hiện tại."))
    b.append(h4("Sách, báo cáo và chuẩn", "Books, Reports, and Standards"))
    b.append(p(
        "Một chuyên khảo NIST rất chi tiết và có thẩm quyền là nguồn chính cho các đặc tính "
        "Seebeck và đặc tính vật lý của các cặp nhiệt điện ký hiệu chữ cái [9]. Các chuẩn của "
        "ASTM và ISA chấp nhận các giá trị và bổ sung cho báo cáo NIST [10, 24]. Các chuẩn Mỹ "
        "được xem xét và cập nhật ở các khoảng 5 năm hoặc ít hơn. ASTM cũng xuất bản các bảng trung "
        "gian của suất điện động Seebeck cho một vài vật liệu phổ biến chưa được chuẩn hóa [10]. "
        "Nhiều chuẩn được thu thập trong một tập duy nhất, được sửa đổi hàng năm, chuyên về đo "
        "nhiệt độ [10]. Các bảng cặp nhiệt điện dạng giấy cứng từ các tập này giờ đây có sẵn "
        "như các chương trình máy tính chức năng tính E(<i>T</i>) và T(E) của tài liệu NIST 175 "
        "trên các dải, ở các khoảng, và trong các đơn vị do người dùng chọn [46]. Một sổ tay ứng "
        "dụng cặp nhiệt điện toàn diện được ASTM xuất bản [1]. Nhiều nhà xuất bản thương mại phát "
        "hành các sách tham khảo và giáo trình mới đề cập đến đo lường. Hầu hết bao gồm một phần "
        "hoặc chương ngắn gọn mô tả các yếu tố trần của đo nhiệt độ cặp nhiệt điện. Một vài cuốn "
        "dành toàn bộ một tập cho đo nhiệt độ. Có nhiều cách xử lý khoa học sâu hơn về nhiệt điện, "
        "phần lớn trong văn hiến lịch sử [1, 11, 12]. Nhiều tổ chức chuẩn đồng thuận quốc gia và "
        "quốc tế xuất bản các phương pháp thử nghiệm nhiệt điện và đặc trưng vật liệu [10, 21, "
        "25]. Các chuẩn vừa mang tính hướng dẫn vừa là sự hình thức hóa các quy trình và vật "
        "liệu. Các chuẩn ASTM và các chỉ mục của chúng giờ đây có sẵn ở định dạng tệp CD-ROM máy "
        "tính. Một số chuẩn hiện có trên World Wide Web hoặc qua FAX. Các hội có ủy ban chuyên về "
        "các chuẩn nhiệt điện giờ đây có các trang Web Internet (như http://www.isa.org và "
        "astm.org) cung cấp thông tin về các chuẩn có sẵn và giải đáp các câu hỏi kỹ thuật trực "
        "tuyến từ người dùng."))
    b.append(h4("Các hội thảo", "Workshops"))
    b.append(p(
        "Hàng năm, có một số hội thảo xuất sắc kéo dài vài giờ hoặc vài ngày dành cho đo lường, "
        "đo nhiệt độ, và thậm chí cặp nhiệt điện. Các hội nghề nghiệp như ISA, phối hợp với các "
        "hội nghị đặc biệt hoặc các cuộc họp thường niên, trình bày các hội thảo hướng dẫn đặc "
        "biệt. Một số được các nhà sản xuất cung cấp miễn phí. Các khóa học đo lường khác được "
        "cung cấp bởi các chuyên gia đo lường độc lập. Các thông báo về các hội thảo này được đăng "
        "trong các tạp chí kỹ thuật và thương mại."))
    b.append(h4("Tài liệu thương mại", "Trade Literature"))
    b.append(p(
        "Rất nhiều tài liệu thương mại miễn phí, catalog, sổ tay, và quảng cáo Web mô tả phần cứng "
        "cặp nhiệt điện và các sản phẩm thu thập dữ liệu. Một số nhà sản xuất phát hành các catalog "
        "công phu về phần cứng liên quan đến cặp nhiệt điện, phần mềm, và sách [4]. Hầu hết bao "
        "gồm tài liệu hướng dẫn. Một vài bao gồm các bản in lại kỹ thuật, thảo luận về nguyên lý "
        "và thực hành, và trình bày các bảng mở rộng về đặc tính nhiệt điện và đặc tính vật lý "
        "của vật liệu cặp nhiệt điện. Các chương trình demo và thông tin sản phẩm có sẵn từ các "
        "nhà sản xuất trên CD-ROM và trên Internet. Có một số tạp chí thương mại liên quan đến đo "
        "lường, khám phá các vấn đề và phát triển hiện tại, và được phân phối miễn phí cho những "
        "người nhận đủ điều kiện."))
    b.append(h3("Lưu ý", "Caveat"))
    b.append(p(
        "Độc giả được cảnh báo rằng toàn bộ văn liệu hiện hành và lịch sử về đo nhiệt độ nhiệt "
        "điện, các bài báo hướng dẫn (kể cả bài này), các chuẩn, quy định, và lời khuyên từ các "
        "“chuyên gia”, tất cả phải được nghiên cứu rất phê phán với một mô hình nhiệt điện xác "
        "thực trong tâm trí. Ở mọi cấp độ tinh vi, từ quảng cáo đến lý thuyết nhiệt điện tinh vi "
        "và tinh xảo nhất về toán học và vật lý, những hiểu lầm được truyền bá ngây thơ về các "
        "hiệu ứng nhiệt điện là rất phổ biến."))
    b.append(h3("Tóm tắt", "Summary"))
    b.append(p(
        "Hiệu ứng Seebeck có thể dùng để đo nhiệt độ với độ phân giải không gian và thời gian tốt "
        "hơn, trên một dải nhiệt độ rộng hơn, trong các hình học đa dạng hơn, và với chi phí thấp "
        "hơn hầu hết các cảm biến nhiệt điện khác. Sự linh hoạt đặc biệt của cặp nhiệt điện bảo "
        "đảm rằng nó sẽ tiếp tục là phương tiện đo nhiệt độ được lựa chọn cho nhiều ứng dụng bất "
        "chấp sự cạnh tranh từ một sự phong phú ngày càng tăng của các nhiệt kế đặc chủng thay "
        "thế. Tuy nhiên, sự đơn giản có vẻ gạt gẫm của cặp nhiệt điện lý tưởng và sự tiện lợi cũng "
        "như độ chính xác bề ngoài do các dụng cụ điều chế tín hiệu hiện đại có thể gạt gẫm. Ứng "
        "dụng đúng đắn thì đơn giản. Được dùng đúng trong các giới hạn của nó, cặp nhiệt điện có "
        "khả năng đo nhiệt độ chính xác và tin cậy. Được hiểu sai, cặp nhiệt điện dễ bị ứng dụng "
        "sai và sai số không rõ ràng nhưng rất đáng kể. Bản tổng quan phòng ngừa này đã mô tả các "
        "cạm bẫy và cách tránh chúng trong thực hành cặp nhiệt điện. Nó có thể cung cấp cho độc "
        "giả tiếp nhận một cơ sở xác thực để sử dụng có hiểu biết ngay cả các mạch nhiệt điện nối "
        "tiếp và tổng quát phức tạp nhất trong thiết kế mạch, các ứng dụng đa dạng, đặc biệt "
        "trong đo nhiệt độ. Mô hình chức năng đơn giản được trình bày ở đây (và có thể đòi hỏi "
        "một số nghiên cứu) đã được cố ý chế tác để giúp người dùng phân biệt rõ thông tin xác "
        "thực khỏi thông tin gạt gẫm, và để giúp đánh giá các thiết kế và quy định của các nhà "
        "sản xuất sản phẩm nhiệt điện."))
    return "".join(b)


def sec_32_4g_en():
    b = [h3("Thermocouple Failure and Validation")]
    b.append(p(
        "A thermocouple measurement has failed when its indications are beyond uncertainty limits "
        "required for a measurement. Thermocouples sometimes fail “open” as junctions separate or "
        "thermoelements corrode, yield, or melt. Explicit “open circuit” indication is a promoted "
        "feature of many modern thermocouple indicators. This popular indication is useful, but is "
        "not an adequate indicator of thermocouple integrity. The more common but less apparent "
        "circuit failures are by inobvious shunting, shorting, or progressing inhomogeneity of "
        "thermoelements. These are not detected by the “open circuit” indication. The continual "
        "indication of a plausible temperature is not proof of authentic temperature measurement. A "
        "deliberate or accidental electrical shunting or direct short between thermoelements at "
        "ambient temperature local to an electronic compensating reference junction should result in "
        "an indication near ambient temperature, not 0°C. A thermocouple failure resulting from "
        "direct shorting between thermoelements at some distance from the intended measuring or "
        "reference junctions can go undetected because it occurs in a temperature region that is "
        "very different from the reference temperature and where a valid or plausible temperature "
        "measurement can continue to be made but at an irrelevant and unexpected and unrecognized "
        "location [35]. In some situations, as in predictably hostile environments, such failure of "
        "some thermocouples in service is anticipated. Where the failure is because of thermocouple "
        "circuit damage, it may not be evident immediately (or ever) without special circuit "
        "diagnostics. For such critical situations, special thermoelectric circuits and monitoring "
        "methods have been developed to assess the continued circuit integrity, although not the "
        "accuracy, of thermometry [35]."))
    b.append(h4("Environmental Compatibility"))
    b.append(p(
        "A primary consideration in thermocouple selection is compatibility of the thermoelements "
        "with their protective enclosures and of both thermoelements with the environment of "
        "measurement. Thermoelements must be protected from corrosive environments and electrically "
        "conductive fluid or solid shunts. Plastic, ceramic, or fiber insulators, metallic sheaths, "
        "and thermowells are intended to serve this function but may fail in service [1, 9–12, 25]. "
        "The compressed granular insulation of mineral-insulated, metal-sheathed thermocouples, if "
        "exposed, rapidly absorbs moisture that can seriously degrade resistive isolation [1, "
        "10–12]. When cut, ends of MIMS thermocouple sheaths must be quickly resealed to avoid "
        "moisture absorption. Fiber and bead insulators are easily contaminated and can degrade "
        "accuracy [1, 10]."))
    b.append(h4("Temperature Exposure"))
    b.append(p(
        "The unavoidable environmental variables in thermometry are temperature and duration. "
        "Although thermoelements may not be visibly affected by an environment, the Seebeck "
        "coefficient might be substantially degraded. Even if only a very thin surface layer of a "
        "thermoelement is modified, the Seebeck coefficient could be changed. The properties can be "
        "degraded by use for a long period of time, at extreme temperatures, and in adverse "
        "environments [1, 9–12]. For these reasons, application should be limited to within the "
        "suggested temperature limits (Table 32.15). Calibration should be performed quickly, "
        "allowing time only for equilibration, and only to the maximum temperature of intended use. "
        "Degradation, observed in use as instability or drift, is necessarily a symptom of "
        "progressing inhomogeneity [30, 31]. Sustained excessive temperature alone can quickly "
        "degrade a thermoelement. Melting points define the absolute upper temperature range of "
        "thermocouple use. However, below this definite value, there are indefinite application "
        "limits at which stability might be substantially reduced [1, 9–12]. Standard thermocouple "
        "tables extend only to the greatest temperature of recommended use for benign protected "
        "environments, short durations, and for wire materials of 3 mm or greater diameter [1, 9, "
        "10]. Significantly reduced temperature limits apply for materials of smaller cross-section, "
        "Table 32.14 [1]. The thermocouples of smaller cross-section degrade more quickly. The "
        "standard tolerances apply only to material as manufactured."))
    b.append(h4("Chemical Environment"))
    b.append(p(
        "There are broad guidelines for environmental compatibility. These recommendations are "
        "conditional and critically depend on many specifics of exposure. A concise summary of "
        "environmental compatibility characteristics is given in Table 32.16. The references should "
        "be consulted for detailed compatibility information [1, 4, 9, 22, 23]. Many thermocouple "
        "catalogs include tables of usually tolerable chemical environments for thermoelements or "
        "thermowell materials [19, 20]. Service experience in working with customers in a wide "
        "variety of process environments sometimes enables manufacturers to advise users on special "
        "problems of compatibility. Often, suitability in a particular service can be assured only "
        "by trial."))
    b.append(h4("Metallurgical Change"))
    b.append(p(
        "Alloyed thermoelements can locally change composition by evaporation of constituents when "
        "exposed to vacuum. Alloy constituents evaporated from a sheath or from one thermoelement "
        "can deposit and coat adjacent thermoelements even through insulators [1, 9–12, 24, 30, "
        "31]. Alloy components can migrate from one thermoelement to the other through the "
        "measuring junction. Traces of contaminants can penetrate through pinholes and hairline "
        "cracks and can actually diffuse through intact protective sheaths and affect apparently "
        "isolated thermoelements. Minute trace impurities in sheaths or insulating materials can "
        "interact with thermoelements. Appropriate MIMS construction and material selection usually "
        "extends life and increases temperature limits, but damage can occur even within apparently "
        "fully sheathed assemblies [34]. Excessive strain can locally substantially modify the "
        "Seebeck coefficient of one or both thermoelements resulting in inhomogeneity. Very "
        "localized strain, as introduced by sharp bends, usually has little effect on practical "
        "thermometry."))
    b.append(_t3215("en"))
    b.append(_t3216("en"))
    b.append(h3("Data Acquisition"))
    b.append(h4("Thermocouple Indicators"))
    b.append(p(
        "The instrument designer can shelter the user from many troublesome details that "
        "complicated measurement for thermocouple pioneers. Microvolt-level signal resolution, high "
        "input resistance, stability, noise reduction, nonlinear scaling, and reference temperature "
        "compensation are now routinely provided to allow the user to focus on the measurement "
        "rather than on details of its indication or recording. Some thermocouple indicators are "
        "hand-held and accommodate only a single thermocouple and only of a single type. A few "
        "provide dual thermocouple inputs and allow direct differential temperature measurement for "
        "which reference junction compensation must not be directly applied. Other bench-top units "
        "accommodate several thermocouple inputs of the same or of intermixed thermocouple and other "
        "sensor types. Claimed instrument accuracy could mislead the casual reader. Although many "
        "instruments are supplied complete with a thermocouple probe, some accuracy specifications "
        "describe only the accuracy of input terminal voltage measurement. The actual instrument "
        "accuracy should be determined by electrical calibration (see “Calibration” section). "
        "Occasionally, the error of the indicating instrument becomes substantially greater than "
        "specified due to drift of reference compensation, offset, or gain. The additional "
        "uncertainty of thermocouple calibration, Table 32.13, and the often larger discrepancy "
        "between measuring junction temperature and the actual temperature of the object being "
        "measured, cannot be included because the latter are governed by details of heat transfer "
        "and transient thermal response."))
    b.append(h4("Thermocouple Transmitters"))
    b.append(p(
        "A less familiar form of thermocouple signal conditioning, the thermocouple transmitter, "
        "is commonplace in process industries [4, 39]. Most two-wire thermocouple transmitters (not "
        "an RF wireless transmitter) are single-channel devices that perform reference junction "
        "compensation, linearizing, and isolation, and transmit the conditioned information to a "
        "remote monitoring site [1]. The transmitter converts the temperature-scaled Seebeck emf to "
        "an analogous signal for wire transmission over long lines to a remote recording or "
        "monitoring location. Such inexpensive and compact single-sensor signal conditioners are "
        "available specialized to most process variables. Thermocouple transmitters are well suited "
        "for monitoring slowly changing temperatures at monitoring sites distant from the measuring "
        "junction. Many are electrically isolated for safety. Some are adapted for use with the DIN "
        "rail mounting system. A transmitter can be installed near each thermocouple. Some are small "
        "enough to install in the connection head of a thermowell. The transmitted signal can take "
        "either current-modulating or voltage-modulating form following ISA standards. The "
        "current-style transmitter temperature modulates, in proportion to temperature, a dc current "
        "supplied from the monitoring site. The signal ranges between 4 mA and 20 mA. The "
        "current-style transmitter conveys information over great distances without the voltage loss "
        "attendant to long-line voltage transmission. Some of the voltage-style transmitters "
        "modulate a supplied voltage over the span from 1 Vdc to 5 Vdc. Offset and scaling for some "
        "are adjusted at the transmitter. Some transmitters now have a local digital readout, and "
        "the scaling and offset can be remotely adjusted [4, 39]."))
    b.append(h4("Recording"))
    b.append(p(
        "Some multichannel thermocouple data recorders are now battery powered for stand-alone use "
        "and small enough to be hand held [41]. Some simpler recorders now cost less than U.S. "
        "$200. More sophisticated units accommodate multiple thermocouples of the same or intermixed "
        "type. Larger digital data loggers with multiplexers that sequentially sample the output "
        "from individual thermocouples can accommodate up to several hundred inputs and can record a "
        "mix of both thermocouple and other signals at sample intervals programmable from a few "
        "milliseconds to hours or days. Desirable three-wire switching between thermocouples is "
        "commonplace. Personal computers now accommodate inexpensive internal digital data "
        "acquisition boards that can convert the computer to a high-resolution temperature recording "
        "system. Laptop computers can accept special palm-sized PCMCIA plug-in cards for multiple "
        "thermocouple input. Digital computer based data acquisition systems with software "
        "specialized for data acquisition, analysis, and presentation, allow the user to apply "
        "special reference temperature compensation, customized linearization of thermocouple "
        "scaling functions for either standard or individual calibrations and of special "
        "thermocouple types. Computer-based thermocouple systems with suitable commercial data "
        "acquisition and other software, provide for experiment design, prediction, data "
        "acquisition, information management, analysis, reporting, archiving, and communication "
        "within a single compact fieldable laptop computer [42]."))
    b.append(h3("Signal Transmission"))
    b.append(p(
        "The length of the principal thermocouple should be as short as feasible. The "
        "thermoelements should be continuous between measuring junction and reference junctions for "
        "best accuracy, but lengthy extension cables can be used if necessary (see “Practical "
        "Thermocouple Circuits” section). In field experiments and in process monitoring, recording "
        "might be separated from the measuring junction by hundreds of meters. There are several "
        "satisfactory possibilities for signal transmission over great distances."))
    b.append(h4("Extension Cable"))
    b.append(p(
        "Matching and compensating thermoelectric extension cables (see “Practical Thermocouple "
        "Circuits” section) are available in a wide variety of constructions and insulations [4, "
        "43]. An extension cable, as a transmission line, can be a single twisted thermoelectric "
        "pair or a multipair cable designed for suppression of both electrostatic and electromagnetic "
        "noise and for environmental protection. While inexpensive unshielded insulated extension "
        "wire is available, in the common situation where electric noise is likely, each extension "
        "should be an insulated, individually shielded, and twisted pair. Where several extension "
        "pairs from a cluster of nearby thermocouples extend to a remote recorder, multipair "
        "thermoelectric cable is available that adds an overall electrostatic shield, mechanical "
        "strengthening reinforcement, and a robust environmental overjacket to protect from "
        "mechanical damage and chemical intrusion in harsh process environments [4, 42]. Such "
        "elaborate thermoelectric extension is more expensive than copper instrumentation cable; "
        "thus, alternative transmission systems should be considered. The proper use of twisted pair "
        "copper instrumentation cable as neutral extension leads, extending from external reference "
        "junction temperature compensation, can be sufficient and less costly than thermoelectric "
        "extensions. Higher quality twisted-shielded-pair instrumentation cable can also improve "
        "signal fidelity in transient thermometry. For such neutral extension leads, insulated "
        "solid unplated copper instrumentation pair only should be used because nonuniform plating "
        "thickness can result in irregularly distributed inhomogeneity and cause Seebeck emf noise. "
        "Conventional coaxial instrumentation cable should never be used as lengthy neutral "
        "thermoelectric extension leads because the outer braid and center conductors have very "
        "different Seebeck coefficients. If not at uniform temperature, the cable can be a "
        "significant source of Seebeck noise emf. Thermoelectric extensions and “pigtailed” "
        "assemblies should be checked full-length for hidden junctions between slightly mismatched "
        "spliced thermoelements and for deliberate, but hidden, pair splices incorrectly made in "
        "crossed polarity [10]. Pass a narrow heat source along the full length of the cable, while "
        "monitoring for local jumps of output local to such unintended junctions, using a "
        "thermocouple indicator. This test is very effective to pinpoint hidden junctions. It does "
        "not test for inhomogeneity [10, 30]."))
    b.append(h4("Wireless Transmission"))
    b.append(p(
        "In several situations, copper wire transmission is less effective, more expensive, or less "
        "convenient than wireless methods. Several low-cost wireless (not thermocouple transmitter) "
        "data acquisition systems are now adapted to combine thermocouple data acquisition and "
        "remote signal transmission [44]. Radio modems communicate data from a measuring location to "
        "recording sites as much as 5 km away. Most provide spread spectrum transmission that does "
        "not require a communications license. Wireless data transmission can be particularly "
        "economical where the distance between the measuring junction and recorder is great, when "
        "many thermocouples must be recorded, when little setup time is available for field cabling, "
        "and where the measuring setup must be moved occasionally. Some systems combine data "
        "logging and radio communication in a single unit. Others require the use of a thermocouple "
        "transmitter, a data logger, and the radio modem to form a system. Optic fiber cable with "
        "electro-optic transmitters can be used for electric noise-free cable transmission over a "
        "long distance between signal conditioning that is local to the thermocouple and to a remote "
        "recorder or monitor."))
    b.append(h3("Sources of Thermocouple Application Information"))
    b.append(h4("Technical Papers"))
    b.append(p(
        "The most concentrated and broadest sources of refereed technical papers addressing "
        "thermocouple thermometry are the serial proceedings of a decennial international symposium "
        "on temperature [25]. The six volumes to date are a rich and reliable source of application "
        "data. Proceedings of annual symposia of the ISA and NCSL also have a few papers describing "
        "current developments in thermometry. Reference [26] has thermoelectric data on the widest "
        "variety of common and nonstandard materials. Current papers devoted specifically, not "
        "incidentally, to thermocouples are infrequent and are distributed broadly across trade "
        "magazines and journals of professional societies. Essential details of thermocouple "
        "thermometry are more often (poorly) described only incidentally in reports of experimental "
        "studies. Some manufacturers publish subscription technical journals specializing in "
        "thermometry [45]. One measurement journal frequently publishes articles on applied "
        "thermometry and, annually in the June issue, publishes an extensive directory of "
        "manufacturers of thermocouple materials and related instrumentation [46]. The directory "
        "includes, for several dozen listed manufacturers, concise descriptions of selected "
        "products and current prices."))
    b.append(h4("Books, Reports, and Standards"))
    b.append(p(
        "A very detailed and authoritative NIST monograph is the primary source for Seebeck "
        "properties and physical characteristics of letter-designated thermocouples [9]. Standards "
        "of the ASTM and ISA adopt the values and complement the NIST report [10, 24]. U.S. "
        "standards are reviewed and updated at intervals of 5 years or less. The ASTM also "
        "publishes interim tables of Seebeck emf for a few popular materials that have not been "
        "standardized [10]. Many standards are collected in a single, annually revised volume "
        "specializing in thermometry [10]. The hardcopy thermocouple tables from these volumes are "
        "now available as functional computer programs that calculate E(<i>T</i>) and T(E) of the "
        "NIST 175 document over ranges, at intervals, and in units selected by the user [46]. A "
        "comprehensive thermocouple application manual is published by the ASTM [1]. Many commercial "
        "publishers issue new reference and textbooks addressing measurement. Most of these include "
        "a brief obligatory section or chapter describing the bare elements of thermocouple "
        "thermometry. A few devote an entire volume to thermometry. There are many deeper scientific "
        "treatments of thermoelectricity, mostly in the historic literature [1, 11, 12]. Many "
        "national and international consensus standards organizations publish thermoelectric test "
        "methods and material characterizations [10, 21, 25]. Standards are instructive as well as "
        "being formalizations of procedures and materials. ASTM Standards and indexes to them are "
        "now available in computer CD-ROM file format. Some standards now are available on the "
        "World Wide Web or by FAX. Societies with committees that specialize in thermoelectric "
        "standards now have Internet Web sites (such as http://www.isa.org and astm.org) that "
        "provide information about available standards and solicit on-line technical questions from "
        "users."))
    b.append(h4("Workshops"))
    b.append(p(
        "Annually, there are several excellent workshops of a few hours or days duration devoted to "
        "measurement, thermometry, and even thermocouples. Professional societies such as the ISA, "
        "in association with special symposia or annual meetings, present special tutorial "
        "workshops. Some are offered without fee by manufacturers. Other measurement courses are "
        "offered by independent measurement specialists. Announcements of these workshops are "
        "published in the technical and trade journals."))
    b.append(h4("Trade Literature"))
    b.append(p(
        "Abundant, free, commercial catalog literature, handbooks, and Web site advertising "
        "describe thermocouple hardware and data acquisition products. Some manufacturers publish "
        "elaborate catalogs of thermocouple-related hardware, software, and books [4]. Most include "
        "tutorial material. A few include technical reprints, discussion of principles and "
        "practices, and present extensive tables of thermoelectric characteristics and physical "
        "properties of thermocouple materials. Demonstration programs and product information are "
        "available from manufacturers on CD-ROM and on the Internet. There are several trade "
        "journals that relate to measurement, explore current issues and developments, and are "
        "distributed free to qualified recipients."))
    b.append(h3("Caveat"))
    b.append(p(
        "The reader is cautioned that the extensive current and historic literature of "
        "thermoelectric thermometry, tutorial articles (even this one), standards, specifications, "
        "and advice from “experts,” all must be studied very critically with an authentic "
        "thermoelectric model in mind. At every level of sophistication, from the promotional to the "
        "most esteemed esoteric and sophisticated mathematical and physical thermoelectric theory, "
        "innocently propagated misconceptions concerning the thermoelectric effects are very "
        "commonplace."))
    b.append(h3("Summary"))
    b.append(p(
        "The Seebeck effect can be used to measure temperature with finer spatial and time "
        "resolution, over a broader temperature range, in more diverse geometries, and at lower "
        "cost than most other electric temperature sensors. The unique versatility of the "
        "thermocouple ensures that it will continue as the thermometry means of choice for many "
        "applications despite competition from an increasing variety and abundance of alternative "
        "special-purpose thermometers. However, the misleading seeming simplicity of the idealized "
        "thermocouple and the convenience and apparent accuracy afforded by modern signal "
        "conditioning instruments can be misleading. Correct application is simple. Properly used "
        "within its limitations, the thermocouple is capable of accurate reliable thermometry. "
        "Improperly understood, the thermocouple is subject to misapplication and inconspicuous, but "
        "very significant, error. This precautionary overview described pitfalls and their "
        "avoidance in thermocouple practice. This can provide the receptive reader with an "
        "authentic basis for the knowledgeable use of even the most complex series and generalized "
        "thermoelectric circuits in circuit design, diverse applications, particularly in "
        "thermometry. The simple Functional Model presented here (and perhaps requiring some "
        "study) was deliberately crafted to aid the user in clearly distinguishing the authentic "
        "information from the misleading, and to aid in evaluating the designs and specifications of "
        "manufacturers of thermoelectric products."))
    return "".join(b)


def _refs324(lang):
    """§32.4 has its own reference list — numbered 1–47 within the section."""
    vi = lang == "vi"
    items = [
        "1. R. M. Park (ed.), Manual on the Use of Thermocouples in Temperature Measurement, MNL 12, 4th ed., Philadelphia, PA, American Society for Testing and Materials, 1993.",
        "2. R. P. Reed, Thermal effects in industrial electronics circuits, in J. D. Irwin (ed.), CRC Industrial Electronics Handbook, Boca Raton, FL, CRC Press, 1996, 57–70.",
        "3. Catalog, TRANSCAT/EIL, Rochester, NY, 1998.",
        "4. Catalog, The Temperature Handbook, Issue 29, Omega Engineering, Inc., Stamford, CT, 1995.",
        "5. D. D. Pollock, Physics of Engineering Materials, Englewood Cliffs, NJ, Prentice-Hall, 1990.",
        "6. D. M. Rowe (ed.), CRC Handbook of Thermoelectrics, Boca Raton, FL, CRC Press, 1995.",
        "7. R. P. Reed, Principles of thermoelectric thermometry, in R. M. Park (ed.), Manual on the Use of Thermocouples in Temperature Measurement, MNL 12, 4th ed., Philadelphia, PA, American Society for Testing and Materials, 1993, chap. 2, 4–42.",
        "8. R. P. Reed, Absolute Seebeck thermoelectric characteristics — principles, significance, and applications, in J. F. Schooley (ed.), Temperature, Its Measurement and Control in Science and Industry, Vol. 6, Part 1, New York, American Institute of Physics, 1992, 503–508.",
        "9. G. W. Burns, M. G. Scroger, G. F. Strouse, M. C. Croarkin, and W. F. Guthrie, Temperature-Electromotive Force Reference Functions and Tables for the Letter-Designated Thermocouple Types Based on the ITS-90, NIST Monograph 175, Washington, D.C., Department of Commerce, 1993.",
        "10. Annual Book of ASTM Standards, Temperature Measurement, 14.03, Philadelphia, PA, American Society for Testing and Materials, 1998.",
        "11. J. V. Nicholas and D. R. White, Traceable Temperatures — An Introduction to Temperature Measurement and Calibration, New York, John Wiley & Sons, 1994.",
        "12. T. W. Kerlin and R. L. Shepard, Industrial Temperature Measurement, Philadelphia, PA, Instrument Society of America, 1982.",
        "13. Catalog, Analog Devices, Inc., Norwood, MA.",
        "14. Catalog, Equipment for Temperature Measurement and Control Systems, Hades Manufacturing Corp., Farmingdale, NY.",
        "15. R. Morrison, Noise and Other Interfering Signals, New York, John Wiley & Sons, 1992.",
        "16. H. W. Markenstein, Proper shielding reduces EMI, Electron. Packaging & Production, 37, 72–78, 1997.",
        "17. Catalog, Thermagon, Inc., Cleveland, OH.",
        "18. N. R. Keltner and J. V. Beck, Surface temperature measurement errors, J. Heat Transfer, 105, 312–318, 1983.",
        "19. Catalog, RdF Corporation, Hudson, NH.",
        "20. Catalog, Temperature Measurement Handbook, Vol. IX, NANMAC Corporation, Framingham, MA.",
        "21. R. P. Reed, Convolution & deconvolution in measurement and control, professional course, Measurements & Control, (178–188), 1997, 1998.",
        "22. H. M. Hashemian, K. M. Peterson, D. W. Mitchell, M. Hashemian, and D. D. Beverly, In situ response time testing of thermocouples, ISA Trans., 29, 1986.",
        "23. R. P. Reed, The transient response of embedded thin film temperature sensors, Temperature, Its Measurement and Control in Science and Industry, Vol. 4, Part 3, New York, Instrument Society of America, 1972.",
        "24. Standard, Temperature Measurement Thermocouples, ISA/ANSI Standard MC96.1-1982, Research Triangle Park, NC, ISA International Society for Measurement and Control, 1982. (Standard withdrawn 1993.)",
        "25. Temperature, Its Measurement and Control in Science and Industry, Vols. 2–6 (Serial), New York, American Institute of Physics, 1942–1992.",
        "26. P. A. Kinzie, Thermocouple Temperature Measurement, New York, Wiley-Interscience, 1973.",
        "27. H. L. Anderson (ed.), Physics Vade Mecum, New York, American Institute of Physics, 1981.",
        "28. Standard, Norme Internationale/International Standard, IEC 584, Parts 1–3, Thermocouples, International Electrotechnical Commission, Geneva, Switzerland, 1995.",
        "29. R. P. Reed, Thermoelectric thermometry: A functional model, in J. F. Schooley (ed.), Temperature, Its Measurement and Control in Science and Industry, vol. 5, Part 2, New York, American Institute of Physics, 1982, 915–922.",
        "30. R. P. Reed, Ya can't calibrate a thermocouple junction! Measurements & Control, Part 1. Why not?, 178, 137–145; Part 2. So What?, 179, 93–100, 1996.",
        "31. R. P. Reed, Thermocouples: calibration, traceability, instability, and inhomogeneity, Isotech J. Thermometry, 7(2), 91–114, 1996.",
        "32. W. F. Roeser, Thermoelectric thermometry, J. Appl. Phys., 11, 213–232, 1940.",
        "33. R. P. Reed, Thermoelectric inhomogeneity testing. Part I: Principles; Part II: Advanced methods, in J. F. Schooley (ed.), Temperature, Its Measurement and Control in Science and Industry, Vol. 6, Part 1, New York, American Institute of Physics, 1992, 519–530.",
        "34. W. Rosch, A. Fripp, W. Debnum, S. Sorokach, and R. Simchick, Damage of fine diameter platinum sheathed Type R thermocouples at temperatures between 950 and 1100 °C, in J. F. Schooley (ed.), Temperature, Its Measurement and Control in Science and Industry, Vol. 6, Part 1, New York, American Institute of Physics, 1992, 569–574.",
        "35. R. P. Reed, Validation diagnostics for defective thermocouple circuits, in J. F. Schooley (ed.), Temperature, Its Measurement and Control in Science and Industry, 5, Part 2, New York, American Institute of Physics, 1982, 915–922.",
        "36. Survey, Measurement Needs Tracking Study — 1997, Keithley Instruments, Cleveland, OH, 1997.",
        "37. J. P. Tavener, Temperature calibration, Measurements and Control, Sept., 160–164, 1986.",
        "38. T. B. Fisher, Selecting a dry well calibrator, Measurements and Control, (185), 105, 1997.",
        "39. Catalog, Reference Manual for Temperature Products and Services, 1st ed., Isothermal Technology Ltd., Merseyside, England, 1997.",
        "40. Catalog, Moore Industries, Sepulveda, CA, 1997.",
        "41. Catalog, DCC Corporation, Pennsauken, NJ, 1997.",
        "42. Catalog, Instrumentation Reference and Catalogue, National Instruments, Austin, TX, 1997.",
        "43. Catalog, Temperature Sensors, Wire and Cable, Watlow Gordon, Richmond, IL, 1997.",
        "44. Catalog, ENCOM Radio Services, Calgary, Alberta, Canada.",
        "45. Isotech Journal of Thermometry, ISSN 0968-347X, Isothermal Technology, Ltd., Merseyside, England.",
        "46. Measurements and Control magazine, ISSN 0148-0057, Measurements & Data Corporation, Pittsburgh, PA.",
        "47. R. P. Reed, A comparison of programs that convert thermocouple properties to the 1990 international temperature and voltage scales, Measurements and Control, 30(177), 105–109, 1996.",
    ]
    head_ = "<h3 id=\"t32-tltk-4\">Tài liệu tham khảo</h3>" if vi else \
            "<h3 id=\"t32-tltk-4\">References</h3>"
    foot = ("* Ghi chú: Việc nhắc đến các sản phẩm đại diện nhằm giới thiệu độc giả về sự đa dạng "
            "phần cứng liên quan đến cặp nhiệt điện và không phải là sự bảo trợ." if vi else
            "* Note: Mention of representative products is to introduce the reader to the variety "
            "of available thermocouple-related hardware and is not an endorsement.")
    return head_ + wl(items) + \
        '<p style="font-size:.82rem;color:#888;font-style:italic;margin-top:-.6rem">%s</p>' % foot


def sec_32_4_vi():
    return (sec_32_4a_vi() + sec_32_4b_vi() + sec_32_4c_vi() + sec_32_4d_vi()
            + sec_32_4e_vi() + sec_32_4f_vi() + sec_32_4g_vi() + _refs324("vi"))


def sec_32_4_en():
    return (sec_32_4a_en() + sec_32_4b_en() + sec_32_4c_en() + sec_32_4d_en()
            + sec_32_4e_en() + sec_32_4f_en() + sec_32_4g_en() + _refs324("en"))


# ============================================================ §32.5  p75-88
def sec_32_5_vi():
    b = [h2("32.5 Nhiệt kế tiếp giáp bán dẫn", "Semiconductor Junction Thermometers")]
    b.append(authors("Randy Frank", ""))
    b.append(p(
        "Có thể chế tạo cảm biến nhiệt độ rất dễ dàng bằng công nghệ gia công bán dẫn, nhờ dùng "
        "đặc tính nhiệt độ của tiếp giáp <i>pn</i>. Gia công theo mẻ cùng các quy trình chế tạo "
        "được định nghĩa chặt chẽ của công nghệ bán dẫn mang lại cảm biến nhiệt độ giá rẻ với "
        "chất lượng đồng nhất. Độ nhạy nhiệt độ của tiếp giáp <i>pn</i> nằm ngay trong các "
        "phương trình định nghĩa của transistor, và có thể dự đoán khá chính xác trong dải nhiệt "
        "độ làm việc điển hình của chất bán dẫn, từ −55 °C đến +150 °C."))
    b.append(p(
        "Hầu hết cảm biến nhiệt độ tiếp giáp bán dẫn dùng một transistor lưỡng cực nối kiểu "
        "di-ốt (tiếp giáp góp–gốc bị nối tắt) [1]. Dòng không đổi chạy qua tiếp giáp gốc–phát "
        "sinh ra điện áp tiếp giáp giữa gốc và phát (V<sub>be</sub>) là hàm tuyến tính của nhiệt "
        "độ tuyệt đối (Hình 32.32). Độ sụt áp thuận toàn phần có hệ số nhiệt độ xấp xỉ "
        "2 mV °C⁻¹."))
    b.append(p(
        "So với cặp nhiệt điện hay cảm biến nhiệt độ điện trở (RTD), hệ số nhiệt độ của cảm biến "
        "bán dẫn lớn hơn nhưng vẫn khá nhỏ. Điện áp thuận của cảm biến bán dẫn cũng có một độ "
        "lệch (offset) thay đổi đáng kể giữa các cá thể. Tuy nhiên, quan hệ giữa điện áp tiếp "
        "giáp bán dẫn và nhiệt độ tuyến tính hơn nhiều so với cặp nhiệt điện hay RTD. Bên cạnh "
        "phần tử cảm biến nhiệt độ, mạch điện cũng dễ dàng được tích hợp để tạo ra cảm biến "
        "nhiệt độ đơn khối có ngõ ra ghép nối trực tiếp với vi điều khiển, đồng thời cung cấp các "
        "tính năng hữu ích cho những ứng dụng cụ thể. Chẳng hạn, dùng cảm biến nhiệt độ nhúng "
        "cùng mạch bổ trợ, có thể thêm các tính năng bảo vệ cho mạch tích hợp (IC). Một cảm biến "
        "nhiệt độ trở thành <i>phần tử nhúng</i> trong một sản phẩm bán dẫn khi nó đảm nhiệm "
        "mục đích thứ cấp hay bổ trợ thay vì là chức năng chính."))
    b.append(fig(32, F.fig(32), "vi"))

    # ------------------------------------------------------------- transistor
    b.append(h3("Transistor dùng làm cảm biến nhiệt độ",
                "The Transistor as a Temperature Sensor"))
    b.append(p(
        "Một sản phẩm bán dẫn thông dụng dùng để cảm biến nhiệt độ là transistor tín hiệu nhỏ "
        "như 2N2222 hay 2N3904. Bằng cách chọn một dải hẹp trong phân bố chung của V<sub>be</sub> "
        "ở các linh kiện này, thu được cảm biến nhiệt độ có độ biến thiên đặc tính thấp hơn. Độ "
        "biến thiên thấp hơn cho phép thay thế linh kiện mà không cần chỉnh lại khi dung sai chỉ "
        "vài phần trăm là chấp nhận được. Linh kiện này (từng được bán với mã MTS102, nay không "
        "còn sản xuất) minh họa các đặc tính hoạt động của transistor khi dùng làm cảm biến "
        "nhiệt độ [2]."))
    b.append(p(
        "Như Hình 32.33 [2], một cảm biến nhiệt độ silic có ngõ ra danh định 730 mV tại −40 °C "
        "và 300 mV tại 150 °C. Dải V<sub>be</sub> được quy định chặt nằm giữa 580 mV và 620 mV "
        "tại 25 °C. Sai số tuyến tính, tức độ lệch khỏi một đường thẳng, của linh kiện này được "
        "nêu ở Hình 32.34 [2]. Độ chính xác toàn phần nằm trong ±3,0 mV, đã bao gồm phi tuyến, "
        "tương đương điển hình ±1 °C trong dải −40 °C đến 150 °C. Các số đọc này thực hiện với "
        "dòng (góp) không đổi 0,1 mA chạy qua linh kiện nhằm giảm thiểu tự đốt nóng tiếp giáp. "
        "Khi dòng không đổi đặt vào lớn hơn 0,1 mA, phải tính đến tự đốt nóng trong linh kiện. "
        "Sự biến thiên của V<sub>be</sub> theo dòng được nêu ở Hình 32.35 [2]."))
    b.append(fig(33, F.fig(33), "vi"))
    b.append(fig(34, F.fig(34), "vi"))
    b.append(fig(35, F.fig(35), "vi"))

    # -------------------------------------------------------- defining equations
    b.append(h3("Tính chất nhiệt của chất bán dẫn: các phương trình định nghĩa",
                "Thermal Properties of Semiconductors: Defining Equations"))
    b.append(p(
        "Dòng thuận không đổi đưa qua một tiếp giáp <i>pn</i> silic lý tưởng sinh ra độ sụt áp "
        "thuận V<sub>F</sub> [3, 4]:"))
    b.append(eq("<i>V</i><sub>F</sub> = <i>V</i><sub>be</sub> = "
                + _frac("<i>k T</i>", "<i>q</i>")
                + " ln " + _frac("<i>I</i><sub>F</sub>", "<i>I</i><sub>S</sub>"), "32.86"))
    b.append(wl([
        "trong đó &nbsp;<i>k</i> = hằng số Boltzmann (1,38 · 10⁻²³ J K⁻¹)",
        "&nbsp;<i>T</i> = nhiệt độ (K)",
        "&nbsp;<i>q</i> = điện tích electron (1,6 · 10⁻¹⁹ C)",
        "&nbsp;<i>I</i><sub>F</sub> = dòng thuận (A)",
        "&nbsp;<i>I</i><sub>S</sub> = dòng bão hòa ngược của tiếp giáp (A)",
    ]))
    b.append(p(
        "Nếu <i>I</i><sub>S</sub> không đổi thì điện áp tiếp giáp (V<sub>be</sub>) tỉ lệ thuận "
        "trực tiếp với nhiệt độ tuyệt đối. Tiếc là <i>I</i><sub>S</sub> lại phụ thuộc nhiệt độ và "
        "biến thiên theo lập phương của nhiệt độ tuyệt đối. Hệ quả là V<sub>F</sub> có hệ số "
        "nhiệt độ tổng thể xấp xỉ −2 mV °C⁻¹."))
    b.append(p(
        "Để giảm độ biến thiên theo nhiệt độ, người ta tạo một <i>tham chiếu vùng cấm</i> "
        "(bandgap reference) từ hai transistor kề nhau, có hành vi gần như giống hệt nhau và "
        "diện tích vùng phát tỉ lệ với nhau, được thiết kế trong một quy trình mạch tích hợp. "
        "Hai tiếp giáp gốc–phát được phân cực ở những mật độ dòng (<i>I</i>/<i>A</i>) khác nhau, "
        "nhưng tỉ số giữa các mật độ dòng về cơ bản không đổi trong suốt dải nhiệt độ làm việc "
        "(−55 °C đến +150 °C). Phương trình sau cho thấy điện áp vi sai (ΔV<sub>be</sub>) liên hệ "
        "với dòng (<i>I</i>) và diện tích vùng phát (<i>A</i>) của từng transistor:"))
    b.append(eq("Δ<i>V</i><sub>be</sub> = <i>V</i><sub>be1</sub> − <i>V</i><sub>be2</sub> = "
                + _frac("<i>k T</i>", "<i>q</i>") + " ln "
                + _frac("(<i>I</i><sub>1</sub>/<i>A</i><sub>1</sub>)",
                        "(<i>I</i><sub>2</sub>/<i>A</i><sub>2</sub>)"), "32.87"))
    b.append(p(
        "Điện áp vi sai xuất hiện ở đầu ra có thể được khuếch đại như Hình 32.36 và dùng làm chỉ "
        "thị trực tiếp nhiệt độ tuyệt đối. Mạch bổ trợ có thể triệt tiêu điện áp offset tại "
        "0 °C và đưa ra ngõ ra theo độ Celsius hay độ Fahrenheit."))
    b.append(fig(36, F.fig(36), "vi"))
    b.append(p(
        "Khả năng cảm biến nhiệt độ bằng kỹ thuật gia công bán dẫn mang lại hai hệ quả quan "
        "trọng: (1) có thể dùng gia công bán dẫn và thiết kế mạch tích hợp để cải thiện hiệu năng "
        "của cảm biến nhiệt độ cho những ứng dụng cụ thể; và (2) có thể tích hợp cảm biến nhiệt "
        "độ vào bên trong các mạch tích hợp khác để bổ sung tính năng. Hai mục tiếp theo trình "
        "bày các hướng tiếp cận này."))

    # ------------------------------------------------------------- integrated
    b.append(h3("Cảm biến nhiệt độ tích hợp", "Integrated Temperature Sensors"))
    b.append(p(
        "Một khi cảm biến nhiệt độ có thể chế tạo bằng kỹ thuật gia công bán dẫn, nhiều hạn chế "
        "của cảm biến sẽ được khắc phục nhờ mạch bổ trợ tích hợp ngay trong cảm biến, hoặc bằng "
        "kỹ thuật mạch đặt bên ngoài. Có thể kể đến cải thiện độ tuyến tính, bổ sung điện áp "
        "chuẩn chính xác, khuếch đại điện áp chính xác và ngõ ra số để ghép nối trực tiếp với vi "
        "điều khiển (MCU). Hơn nữa, không cần mạch đo điện trở (như cảm biến RTD) hay mạch bù "
        "mối nối lạnh (như cảm biến cặp nhiệt điện). Dưới đây khảo sát ba mạch tích hợp và một "
        "ví dụ mạch ngoài."))

    b.append(h4("Cảm biến nhiệt độ số tích hợp",
                "Integrated Digital Temperature Sensor"))
    b.append(p(
        "Hình 32.37 [3] là cảm biến nhiệt độ tiếp giáp bán dẫn đơn khối (một mảnh silic duy nhất, "
        "LM75 của National Semiconductor) tích hợp nhiều tính năng, trong đó có ngõ ra số. Tín "
        "hiệu tương tự của cảm biến được biến đổi sang dạng số bằng bộ chuyển đổi sigma–delta "
        "ngay trên chip [3]. Giao tiếp nối tiếp hai dây truyền dữ liệu thẳng tới vi điều khiển "
        "chủ. Cảm biến có điểm đặt lập trình được bằng phần mềm, dùng để ngắt hoạt động của bộ "
        "điều khiển hoặc thực hiện bảo vệ [5]. Để tránh kích hoạt nhầm, có thể lập trình số phép "
        "so sánh (tối đa sáu lần quá nhiệt liên tiếp). Có thể vận hành tám cảm biến khác nhau "
        "trên cùng một bus. Độ phân giải là ±½ °C và độ chính xác là ±2 % trong dải −25 °C đến "
        "+100 °C. Cảm biến tiêu thụ 250 µA khi hoạt động và chỉ 10 µA ở chế độ ngủ."))
    b.append(fig(37, F.fig(37), "vi"))

    b.append(h4("Cảm biến nhiệt độ tích hợp ngõ ra tương tự",
                "Analog Output Integrated Temperature Sensor"))
    b.append(p(
        "Một hướng tiếp cận khác của cảm biến nhiệt độ tích hợp được nêu ở Hình 32.38 [4]. Bộ "
        "điều khiển nhiệt độ lập trình bằng điện trở TMP-1 có ngõ ra 5 mV °C⁻¹, các điểm đặt cao "
        "và thấp, cùng ngõ ra báo quá nhiệt và dưới nhiệt độ. Điện áp chuẩn trôi thấp cũng được "
        "tích hợp trong thiết kế có kích thước 70 mil × 78 mil (2,76 mm × 3,07 mm). Hình 32.39 "
        "là ảnh hiển vi của die silic. TMP-1 được quy định hoạt động trong dải −55 °C đến "
        "+125 °C với độ chính xác ±1 °C trên toàn dải."))
    b.append(fig(38, F.fig(38), "vi"))
    b.append(fig(39, F.fig(39), "vi"))

    b.append(h4("Cảm biến nhiệt độ ngõ ra số", "Digital Output Temperature Sensor"))
    b.append(p(
        "Một cảm biến nhiệt độ biến đổi thẳng sang số đã được thiết kế cho các ứng dụng cảm biến "
        "nhiệt độ đa điểm [6]. Mỗi linh kiện được khắc một số seri riêng biệt. Bộ nhớ chỉ đọc "
        "(ROM) 64 bit nhận dạng nhiệt độ của một cảm biến cụ thể trong hệ thống đo, với nhiều "
        "cảm biến cung cấp số đọc từ các vị trí khác nhau. Tín hiệu có thể truyền đi xa tới 300 m."))
    b.append(p(
        "Cảm biến hoạt động từ −55 °C đến 125 °C, lấy nguồn ngay từ đường dữ liệu. Phép đo được "
        "phân giải theo các bước 0,5 °C dưới dạng giá trị số 9 bit, với thời gian biến đổi trong "
        "vòng 200 ms. Thiết bị còn có các ngưỡng báo động do người dùng định nghĩa."))

    b.append(h4("Mạch ngoài loại bỏ nhu cầu hiệu chuẩn",
                "External Circuitry Eliminates Calibration"))
    b.append(p(
        "Có thể thiết kế mạch ngoài để khai thác khả năng cảm biến vốn có của các transistor giá "
        "rẻ mà không phải chịu chi phí mạch tích hợp bổ trợ, cũng không cần hiệu chuẩn từng linh "
        "kiện. Mạch ở Hình 32.40 dùng một mạch tích hợp (LTC1043 của Linear Technology "
        "Corporation) để tạo ngõ ra 0 V đến 10 V ứng với 0 °C đến 100 °C, đạt độ chính xác "
        "±1 °C với <i>bất kỳ</i> transistor tín hiệu nhỏ thông thường nào làm cảm biến [7]. Mạch "
        "thiết lập quan hệ ΔV<sub>be</sub> theo dòng không đổi bất chấp giá trị tuyệt đối của "
        "di-ốt V<sub>be</sub>. Thay thế bằng các transistor lấy từ nhiều nguồn khác nhau cho sai "
        "lệch chưa tới 0,4 °C."))
    b.append(fig(40, F.fig(40), "vi"))

    # ------------------------------------------------------- other applications
    b.append(h3("Các ứng dụng khác của kỹ thuật cảm biến bán dẫn",
                "Other Applications of Semiconductor Sensing Techniques"))
    b.append(p(
        "Nhiều tham số bán dẫn biến thiên tuyến tính trong dải nhiệt độ làm việc. MOSFET công "
        "suất dùng để đóng cắt dòng lớn (điển hình vài ampe) ở điện áp có thể vượt 500 V là một "
        "ví dụ. Như Hình 32.41 [8], điện áp ngưỡng cổng của MOSFET công suất thay đổi từ 1,17 "
        "xuống 0,65 lần giá trị tại 25 °C khi nhiệt độ tăng từ −40 °C lên 150 °C. Điện áp đánh "
        "thủng của MOSFET công suất cũng biến thiên từ 0,9 đến 1,18 lần giá trị tại 25 °C trong "
        "cùng dải nhiệt độ (Hình 32.42) [8]. Các quan hệ này thường được dùng để xác định nhiệt "
        "độ tiếp giáp của một linh kiện bán dẫn trong khi nó thực sự vận hành trong mạch, ở giai "
        "đoạn thiết kế (xem mục “Hàm ý về độ tin cậy”). Đo nhiệt độ ở mặt ngoài của vỏ có thể "
        "thấp hơn nhiệt độ tiếp giáp nhiều độ, nhất là trong các sự kiện đóng cắt nhanh, năng "
        "lượng cao. Nhiệt độ tiếp giáp thực và hệ quả của nó lên các tham số bán dẫn phải được "
        "tính đến để áp dụng linh kiện bán dẫn đúng cách."))
    b.append(fig(41, F.fig(41), "vi"))
    b.append(fig(42, F.fig(42), "vi"))
    b.append(p(
        "Các di-ốt polysilicon (và cả điện trở) cách ly với MOSFET công suất có thể được tạo ra "
        "ngay trong quy trình chế tạo bán dẫn với những sửa đổi nhỏ. Các di-ốt này dùng được làm "
        "phần tử cảm biến nhiệt độ trong ứng dụng thực [9]. Cảm biến nhiệt thực hiện bằng các "
        "phần tử polysilicon là một cải tiến đáng kể so với cảm biến nhiệt độ linh kiện công "
        "suất bằng một phần tử cảm biến đặt bên ngoài. Nhờ dùng di-ốt polysilicon, cảm biến có "
        "thể đặt ngay gần tâm của linh kiện công suất, cạnh các pad dây nguồn, nơi mật độ dòng "
        "lớn nhất và vì thế nhiệt độ die cao nhất."))
    b.append(p(
        "Độ dẫn nhiệt của lớp oxit ngăn cách các di-ốt polysilicon với linh kiện công suất nhỏ "
        "hơn hai bậc so với silic. Tuy nhiên, vì lớp này rất mỏng, phần tử polysilicon vẫn cho "
        "chỉ thị chính xác nhiệt độ đỉnh thực của tiếp giáp."))
    b.append(p(
        "Hình 32.43 [9] là một FET công suất tích hợp di-ốt cảm biến nhiệt độ. Bằng cách theo "
        "dõi điện áp ngõ ra khi cho dòng không đổi chạy qua (các) di-ốt polysilicon tích hợp, "
        "thu được chỉ thị chính xác nhiệt độ die cực đại. Thiết kế thực tế bố trí nhiều di-ốt. "
        "Một di-ốt đơn lẻ trong thiết kế này có hệ số nhiệt độ 1,90 mV °C⁻¹; có thể mắc hai hay "
        "nhiều di-ốt nối tiếp nếu muốn ngõ ra lớn hơn. Để đạt độ chính xác cao hơn, các di-ốt "
        "có thể được chỉnh cắt (trim) khi thử ở mức wafer bằng cách đứt các liên kết cầu chì làm "
        "từ polysilicon. Thời gian đáp ứng của các di-ốt dưới 100 ms — đủ để linh kiện chịu "
        "được phép nối thẳng qua ắc quy ô tô, với mạch ngoài thực hiện ngắt trước khi linh kiện "
        "hỏng. Khả năng cảm biến còn cho phép linh kiện công suất đưa ra chỉ báo (kèm mạch "
        "ngoài) nếu tản nhiệt không đúng khi lắp thiết bị vào mô-đun, hoặc nếu có sự thay đổi "
        "trong ứng dụng mà cuối cùng sẽ gây hỏng hóc."))
    b.append(fig(43, F.fig(43), "vi"))

    # --------------------------------------------------------------- power ICs
    b.append(h3("Cảm biến nhiệt độ trong IC công suất để bảo vệ và chẩn đoán sự cố",
                "Temperature Sensing in Power ICs for Fault Protection and Diagnostics"))
    b.append(p(
        "Cảm biến các điều kiện sự cố, chẳng hạn ngắn mạch, là một phần không thể tách rời của "
        "nhiều IC công suất thông minh (smart power IC). Khả năng tạo cảm biến nhiệt độ ngay "
        "trong quy trình bán dẫn đem lại các tính năng bảo vệ và chẩn đoán cho những linh kiện "
        "này. Chức năng chính của IC công suất là làm giao diện giữa vi điều khiển và tải cho "
        "nhiều loại tải khác nhau. Ở các thiết bị nhiều ngõ ra, việc cảm biến nhiệt độ tiếp giáp "
        "của từng thiết bị cho phép đưa trạng thái của từng thiết bị về vi điều khiển (MCU); khi "
        "cần, MCU có thể ngắt riêng thiết bị đang có sự cố."))
    b.append(p(
        "Một <i>IC công suất thông minh</i> có thể tích hợp nhiều bộ lái công suất trên cùng một "
        "mảnh silic đơn khối [10]. Mỗi bộ lái có thể tích hợp một cảm biến nhiệt độ để xác định "
        "trạng thái làm việc đúng và chỉ ngắt riêng bộ lái đó khi xảy ra sự cố. Hình 32.44 là bộ "
        "lái tám ngõ ra, tự động ngắt độc lập ngõ ra của một bộ lái cụ thể nếu nhiệt độ của nó "
        "quá cao (tức trong khoảng 155 °C đến 185 °C) [10]."))
    b.append(fig(44, F.fig(44), "vi"))
    b.append(p(
        "Chuyển mạch nối tiếp tám ngõ ra (OSS) bổ sung cảm biến nhiệt độc lập thông qua mạch "
        "phát hiện quá nhiệt vào các tính năng bảo vệ. Sự cố có thể được phát hiện cho từng thiết "
        "bị ngõ ra, và có thể ngắt riêng lẻ. Trong IC công suất nhiều ngõ ra, rất mong muốn chỉ "
        "ngắt thiết bị đang gặp sự cố chứ không ngắt tất cả các thiết bị cùng tích hợp trên IC. "
        "Với các ngõ ra nằm ở những vị trí vật lý khác nhau trên chip, rất khó dự đoán gradient "
        "nhiệt có thể xuất hiện trong tình huống sự cố. Vì vậy cần cảm biến nhiệt độ cục bộ tại "
        "mỗi ngõ ra thay vì một cảm biến nhiệt độ toàn cục duy nhất."))
    b.append(p(
        "Như Hình 32.45, tám ngõ ra của thiết bị, mỗi ngõ có cảm biến nhiệt độ riêng, có thể "
        "được ngắt độc lập khi vượt ngưỡng nhiệt 170 °C [10]. Tất cả ngõ ra được nối nguồn 16 V "
        "ở nhiệt độ môi trường phòng, với tổng dòng ban đầu gần 30 A chạy qua thiết bị. Lưu ý "
        "rằng từng thiết bị ngắt một cách độc lập: thiết bị nóng nhất ngắt trước. Sai khác có "
        "thể đến từ chênh lệch mức dòng và điện trở nhiệt. Khi từng thiết bị ngắt, tổng công "
        "suất tiêu tán trên chip giảm và các thiết bị còn bật tản nhiệt hiệu quả hơn."))
    b.append(fig(45, F.fig(45), "vi"))
    b.append(p(
        "Nối thẳng vào ắc quy là một ngắn mạch cứng, lẽ ra có thể bị phát hiện bởi mạch hạn dòng. "
        "Tuy nhiên, <i>ngắn mạch mềm</i> nằm dưới ngưỡng hạn dòng nhưng lại vượt khả năng tiêu "
        "tán công suất của chip, và là tình huống cực kỳ khó phát hiện. Ngắn mạch mềm đòi hỏi "
        "phải có cảm biến quá nhiệt để bảo vệ IC khỏi những mức nhiệt độ phá hủy."))
    b.append(p(
        "Tình trạng quá nhiệt do IC công suất cảm nhận có thể khiến thiết bị tự ngắt để tránh "
        "hỏng trong trường hợp này; nhưng trong tình huống khác, tùy thiết kế mạch sự cố, tín "
        "hiệu sự cố chỉ đưa ra cảnh báo cho MCU mà không có hành động nào được thực hiện, để phần "
        "còn lại của hệ thống tiếp tục hoạt động bình thường. Khi các điều kiện sự cố được đưa "
        "về MCU, có thể thực hiện một quy trình ngắt hệ thống có trật tự. Cảm biến nhiệt độ tích "
        "hợp là thiết yếu để mang lại kiểu bảo vệ này trong IC công suất nhiều ngõ ra."))

    # ------------------------------------------------------------- reliability
    b.append(h3("Hàm ý của nhiệt độ đối với độ tin cậy của linh kiện điện tử",
                "Reliability Implications of Temperature to Electronic Components"))
    b.append(p(
        "Ảnh hưởng của nhiệt độ lên linh kiện điện tử, và lên việc ứng dụng thành công chúng "
        "trong hệ thống điện tử, là một trong những vấn đề phải giải quyết trong giai đoạn thiết "
        "kế hệ thống. Nhiệt độ ảnh hưởng đến hiệu năng và tuổi thọ kỳ vọng của linh kiện bán dẫn. "
        "Ứng suất cơ học sinh ra bởi sự khác biệt giữa các hệ số giãn nở nhiệt có thể gây hỏng "
        "trong các thử nghiệm chu trình nhiệt (không khí sang không khí) hoặc trong các quá trình "
        "chuyển tiếp sốc nhiệt (nước sang nước)."))
    b.append(p(
        "Tần suất hỏng điển hình của linh kiện bán dẫn có thể biểu diễn bằng phương trình "
        "Arrhenius [9]:"))
    b.append(eq("λ = <i>A</i> exp " + _frac("−Ø", "<i>K T</i>"), "32.88"))
    b.append(wl([
        "trong đó &nbsp;λ = tần suất hỏng (failure rate)",
        "&nbsp;<i>A</i> = hằng số",
        "&nbsp;Ø = năng lượng kích hoạt (eV)",
        "&nbsp;<i>K</i> = hằng số Boltzmann (8,62 · 10⁻⁵ eV K⁻¹)",
        "&nbsp;<i>T</i> = nhiệt độ tiếp giáp (K)",
    ]))
    b.append(p(
        "Tần suất hỏng của linh kiện bán dẫn thường được nêu là tăng gấp đôi với mỗi 10 đến "
        "15 °C tăng lên của nhiệt độ làm việc (tức nhiệt độ tiếp giáp). Tuy nhiên, việc thử "
        "nghiệm nhiều hơn và các cải tiến thiết kế đã giảm thiểu các hỏng hóc do những cơ chế "
        "hỏng cụ thể."))
    b.append(p(
        "Một trong các tham số liên quan đến nhiệt độ phải tính đến khi thiết kế một khóa công "
        "suất là đáp ứng nhiệt quá độ, ký hiệu là <i>r</i>(<i>t</i>) · <i>R</i><sub>θJC</sub>, "
        "trong đó <i>r</i>(<i>t</i>) là điện trở nhiệt quá độ đã chuẩn hóa. Giá trị "
        "<i>r</i>(<i>t</i>) được xác định từ bảng dữ liệu của nhà sản xuất bán dẫn, dùng chu kỳ "
        "làm việc (duty cycle) và độ rộng xung của ứng dụng. Mức điện trở nhiệt suy giảm này (xem "
        "mục “Đo nhiệt độ tiếp giáp”), dựa trên việc transistor làm việc ở chế độ đóng cắt và "
        "ngắt trong một khoảng thời gian, tiến về mức một chiều trong vòng một giây. Nhiệt độ "
        "quá mức có thể sinh ra rất nhanh và phải được phát hiện trong vòng vài mili giây để "
        "ngăn hỏng hóc."))

    # --------------------------------------------------- junction temperature
    b.append(h3("Đo nhiệt độ tiếp giáp", "Junction Temperature Measurement"))
    b.append(p(
        "Trong chất bán dẫn, sự thay đổi nhiệt độ liên hệ trực tiếp với công suất tiêu tán qua "
        "điện trở nhiệt. Điện trở nhiệt một chiều ở trạng thái ổn định từ tiếp giáp đến vỏ, "
        "<i>R</i><sub>θJC</sub>, được định nghĩa là độ tăng nhiệt độ trên một đơn vị công suất "
        "so với một điểm chuẩn bên ngoài (điển hình là vỏ). Quan hệ này được nêu ở Phương trình "
        "32.89 [8]:"))
    b.append(eq("<i>R</i><sub>θJC</sub> = "
                + _frac("Δ<i>T</i>", "<i>P</i><sub>D</sub>"), "32.89"))
    b.append(wl([
        "trong đó &nbsp;Δ<i>T</i> = nhiệt độ tiếp giáp trừ nhiệt độ vỏ (°C)",
        "&nbsp;<i>P</i><sub>D</sub> = công suất tiêu tán trong tiếp giáp (W)",
    ]))
    b.append(p(
        "Linh kiện bán dẫn hay die silic thường được bao bọc trong một vỏ ngăn cản việc đo trực "
        "tiếp nhiệt độ tiếp giáp. Nhiệt độ tiếp giáp được đo gián tiếp bằng cách đo nhiệt độ vỏ "
        "<i>T</i><sub>C</sub>; nhiệt độ tản nhiệt <i>T</i><sub>S</sub> đối với các ứng dụng công "
        "suất lớn hơn cần tản nhiệt; nhiệt độ môi trường <i>T</i><sub>A</sub>; và một tham số "
        "điện nhạy nhiệt độ của linh kiện."))
    b.append(p(
        "Bước đầu tiên của quy trình là hiệu chuẩn tham số nhạy nhiệt độ đó. Lấy ví dụ transistor "
        "công suất lưỡng cực: điện áp thuận gốc–phát được đo và ghi lại với một dòng hiệu chuẩn "
        "thấp <i>I</i><sub>M</sub> chạy qua linh kiện — đủ thấp để tránh tự đốt nóng (điển hình "
        "trong khoảng 2 mA đến 10 mA), nhưng cũng đủ lớn để nằm trong vùng tuyến tính của đường "
        "cong điện áp thuận. Quy trình được thực hiện ở nhiệt độ phòng và ở nhiệt độ nâng cao, "
        "điển hình 100 °C."))
    b.append(p(
        "Sau khi hiệu chuẩn, dùng một bộ thử đóng cắt công suất (như Hình 32.46) để luân phiên "
        "cấp và ngắt công suất cho linh kiện [8]. Pha bật kéo dài (điển hình vài mili giây), còn "
        "pha ngắt rất ngắn (chỉ vài trăm micro giây), nhờ đó nhiệt độ vỏ được ổn định và tiếp "
        "giáp hầu như không bị nguội đi. Transistor được cho làm việc ở vùng tích cực, và công "
        "suất tiêu tán được thay đổi bằng cách chỉnh <i>I</i><sub>E</sub> và/hoặc "
        "<i>V</i><sub>CE</sub> cho đến khi tiếp giáp đạt nhiệt độ hiệu chuẩn. Biết được điểm này "
        "bằng cách đo <i>V</i><sub>BE</sub> trong khoảng thời gian mà <i>I</i><sub>M</sub> là "
        "dòng duy nhất đang chảy."))
    b.append(fig(46, F.fig(46), "vi"))
    b.append(p(
        "Khi giá trị <i>V</i><sub>BE</sub> bằng giá trị trên đường cong hiệu chuẩn thì nhiệt độ "
        "tiếp giáp đang ở nhiệt độ hiệu chuẩn. Các phép đo <i>V</i><sub>BE</sub>, "
        "<i>T</i><sub>C</sub> và <i>I</i><sub>E</sub> cho phép tính điện trở nhiệt của linh kiện "
        "theo Phương trình 32.89. Vì <i>R</i><sub>θJC</sub> là hằng số, các phép đo tiếp theo về "
        "<i>T</i><sub>C</sub>, <i>V</i><sub>CE</sub> và <i>I</i><sub>E</sub> trong những điều "
        "kiện vận hành khác nhau có thể dùng để tính nhiệt độ tiếp giáp, nhằm giữ linh kiện "
        "trong vùng hoạt động an toàn trong ứng dụng thực. Với các linh kiện có đặc tính điện "
        "khác đi, chẳng hạn MOSFET công suất nêu trên, người ta dùng những tham số khác có quan "
        "hệ tuyến tính với nhiệt độ để hiệu chuẩn và đo."))

    # -------------------------------------------------------------- packaging
    b.append(h3("Đóng vỏ cảm biến nhiệt độ bán dẫn",
                "Semiconductor Temperature Sensor Packaging"))
    b.append(p(
        "Cảm biến nhiệt độ chế tạo bằng công nghệ bán dẫn thường được đóng trong các loại vỏ "
        "thông dụng của ngành bán dẫn: vỏ kim loại (TO-99), vỏ gốm, và phổ biến hơn là vỏ nhựa "
        "(SOT-23, DIP 8 chân, TO-92, SOIC 8 chân, v.v.). Các vỏ này được thiết kế để hàn lên bo "
        "mạch theo công nghệ xuyên lỗ hoặc công nghệ dán mặt. Vì thế, dạng vỏ có thể khác khá "
        "nhiều so với vỏ của cảm biến nhiệt độ chế tạo bằng các công nghệ khác. Hình 32.47 nêu "
        "ví dụ về năm loại vỏ cảm biến nhiệt độ silic hiện có."))
    b.append(fig(47, F.fig(47), "vi"))

    # ---------------------------------------------------------- defining terms
    b.append(h3("Định nghĩa thuật ngữ", "Defining Terms"))
    b.append(defs([
        ("<b>Tham chiếu vùng cấm</b> (bandgap reference)",
         "Đặc tính tiếp giáp vùng phát phân cực thuận của các transistor kề nhau, dùng để tạo "
         "điện áp ngõ ra có hệ số nhiệt độ bằng không."),
        ("<b>Die</b>",
         "Chip bán dẫn chưa đóng vỏ, đã được tách ra khỏi wafer."),
        ("<b>Cảm biến nhúng</b> (embedded sensor)",
         "Cảm biến được đưa vào bên trong một mạch tích hợp."),
        ("<b>Mạch tích hợp</b>",
         "Nhiều transistor cùng với di-ốt, điện trở, tụ điện, v.v. trên cùng một die silic."),
        ("<b>Tiếp giáp</b> (junction)",
         "Mặt phân cách tại đó kiểu dẫn điện của vật liệu đổi từ loại <i>p</i> sang loại <i>n</i>."),
        ("<b>Điện áp tiếp giáp</b>",
         "Độ sụt áp trên một mặt phân cách <i>pn</i> được phân cực thuận trong transistor "
         "(V<sub>be</sub>) hay trong di-ốt."),
        ("<b>Nhiệt độ tiếp giáp</b>",
         "Nhiệt độ của mặt phân cách <i>pn</i> trong transistor hay di-ốt."),
        ("<b>Đơn khối</b> (monolithic integrated circuit)",
         "Được chế tạo từ một mảnh silic duy nhất."),
        ("<b>IC công suất / IC công suất thông minh</b>",
         "Thiết bị lai hoặc đơn khối (bán dẫn) có thể làm mát bằng dẫn nhiệt, thực hiện điều hòa "
         "tín hiệu, và tích hợp chức năng điều khiển công suất như quản lý sự cố và/hoặc chẩn đoán."),
        ("<b>Tự đốt nóng</b> (self-heating)",
         "Độ tăng nhiệt độ bên trong một linh kiện (bán dẫn) do dòng điện chảy trong chính linh "
         "kiện đó."),
        ("<b>Ngắn mạch mềm</b> (soft short)",
         "Tình trạng tải quá mức gây nhiệt độ quá cao nhưng vẫn nằm dưới ngưỡng hạn dòng của "
         "thiết bị."),
        ("<b>Điện trở nhiệt</b>",
         "Điện trở nhiệt một chiều ở trạng thái ổn định từ tiếp giáp đến vỏ, "
         "<i>R</i><sub>θJC</sub>, là độ tăng nhiệt độ trên một đơn vị công suất so với một điểm "
         "chuẩn bên ngoài (điển hình là vỏ)."),
        ("<b>TinyPak</b>",
         "Nhãn hiệu đã đăng ký của National Semiconductor Corp."),
    ]))
    b.append(note(
        "Chú thích của người dịch: bản quét của nguyên bản (CRC Press, 1999) làm hỏng một số ký "
        "hiệu đơn vị và dấu — cụ thể là ±, µA, µs và °C bị tách rời. Các giá trị trong mục này "
        "(±3,0 mV, 250 µA / 10 µA, ≤ 300 µs, v.v.) được phục hồi theo ngữ cảnh kỹ thuật và bảng "
        "dữ liệu của linh kiện tương ứng; riêng “dưới 100 ms” ở thời gian đáp ứng di-ốt được giữ "
        "nguyên như bản in."))
    return "".join(b) + _refs325("vi")


def sec_32_5_en():
    b = [h2("32.5 Semiconductor Junction Thermometers", "Nhiệt kế tiếp giáp bán dẫn")]
    b.append(authors("Randy Frank", ""))
    b.append(p(
        "Temperature sensors can be produced easily with semiconductor processing technology by "
        "using the temperature characteristics of the <i>pn</i> junction. The batch processing "
        "and well-defined manufacturing processes associated with semiconductor technology can "
        "provide low-cost and consistent-quality temperature sensors. The temperature "
        "sensitivity of the <i>pn</i> junction is part of the transistor's defining equations "
        "and is quite predictable over the typical semiconductor operating range of −55 °C to "
        "+150 °C."))
    b.append(p(
        "Most semiconductor junction temperature sensors use a diode-connected bipolar "
        "transistor (short-circuited collector–base junction) [1]. A constant current passed "
        "through the base–emitter junction produces a junction voltage between base and emitter "
        "(V<sub>be</sub>) that is a linear function of absolute temperature (Figure 32.32). The "
        "overall forward voltage drop has a temperature coefficient of approximately "
        "2 mV °C⁻¹."))
    b.append(p(
        "Compared with a thermocouple or a resistive temperature device (RTD), the temperature "
        "coefficient of a semiconductor sensor is larger but still quite small. Also, the "
        "semiconductor sensor's forward voltage has an offset that varies significantly from "
        "unit to unit. However, the semiconductor junction voltage vs. temperature is much more "
        "linear than that of a thermocouple or RTD. In addition to the temperature-sensing "
        "element, circuitry is easily integrated to produce a monolithic temperature sensor "
        "with an output that can be interfaced easily to a microcontroller, and to provide "
        "features that are useful in specific applications. For example, using an embedded "
        "temperature sensor with additional circuitry, protection features can be added to "
        "integrated circuits (ICs). A temperature sensor becomes an <i>embedded</i> item in a "
        "semiconductor product when it has a secondary or supplemental purpose instead of the "
        "primary function."))
    b.append(fig(32, F.fig(32), "en"))

    # ------------------------------------------------------------- transistor
    b.append(h3("The Transistor as a Temperature Sensor"))
    b.append(p(
        "A common semiconductor product for temperature sensing is a small-signal transistor "
        "such as a 2N2222 or a 2N3904. By selecting a narrow portion of the overall distribution "
        "of V<sub>be</sub> for these devices, a temperature sensor with a lower variation in "
        "characteristics can be obtained. The lower variation can provide part-for-part "
        "replacement when a tolerance of only a few percent is acceptable. This device (formerly "
        "offered as an MTS102 but no longer in production) demonstrates the performance "
        "characteristics of the transistor used as a temperature sensor [2]."))
    b.append(p(
        "As shown in Figure 32.33 [2], a silicon temperature sensor has a nominal output of "
        "730 mV at −40 °C and an output of 300 mV at 150 °C. The narrowly specified "
        "V<sub>be</sub> ranges between 580 mV and 620 mV at 25 °C. The linearity error, or "
        "variation from a straight line, of this device is shown in Figure 32.34 [2]. The total "
        "accuracy is within ±3.0 mV including nonlinearity, which is typically within ±1 °C in "
        "the range −40 °C to 150 °C. These readings are made with a constant (collector) current "
        "of 0.1 mA passing through the device to minimize the effect of self-heating of the "
        "junction. When the constant current applied is larger than 0.1 mA, the effect of "
        "self-heating in the device must be taken into account. The variation of V<sub>be</sub> "
        "with current is shown in Figure 32.35 [2]."))
    b.append(fig(33, F.fig(33), "en"))
    b.append(fig(34, F.fig(34), "en"))
    b.append(fig(35, F.fig(35), "en"))

    # -------------------------------------------------------- defining equations
    b.append(h3("Thermal Properties of Semiconductors: Defining Equations"))
    b.append(p(
        "A constant forward current supplied through an ideal silicon <i>pn</i> junction "
        "produces a forward voltage drop V<sub>F</sub> [3, 4]:"))
    b.append(eq("<i>V</i><sub>F</sub> = <i>V</i><sub>be</sub> = "
                + _frac("<i>k T</i>", "<i>q</i>")
                + " ln " + _frac("<i>I</i><sub>F</sub>", "<i>I</i><sub>S</sub>"), "32.86"))
    b.append(wl([
        "where &nbsp;<i>k</i> = Boltzmann's constant (1.38 · 10⁻²³ J K⁻¹)",
        "&nbsp;<i>T</i> = temperature (K)",
        "&nbsp;<i>q</i> = charge of the electron (1.6 · 10⁻¹⁹ C)",
        "&nbsp;<i>I</i><sub>F</sub> = forward current (A)",
        "&nbsp;<i>I</i><sub>S</sub> = junction's reverse saturation current (A)",
    ]))
    b.append(p(
        "For constant <i>I</i><sub>S</sub>, the junction voltage (V<sub>be</sub>) would be "
        "directly proportional to absolute temperature. Unfortunately, <i>I</i><sub>S</sub> is "
        "temperature dependent and varies with the cube of absolute temperature. As a result, "
        "V<sub>F</sub> has an overall temperature coefficient of approximately −2 mV °C⁻¹."))
    b.append(p(
        "To reduce the temperature variation, a <i>bandgap reference</i> is formed from two "
        "adjacent and essentially identical-behavior transistors with proportional emitter area "
        "designed in an integrated circuit process. The two base–emitter junctions are biased "
        "with different current densities (<i>I</i>/<i>A</i>), but the ratio of current "
        "densities is essentially constant over the operating temperature range (−55 °C to "
        "+150 °C). The following equation shows how the differential voltage "
        "(ΔV<sub>be</sub>) is related to the current (<i>I</i>) and emitter area (<i>A</i>) of "
        "the respective transistors:"))
    b.append(eq("Δ<i>V</i><sub>be</sub> = <i>V</i><sub>be1</sub> − <i>V</i><sub>be2</sub> = "
                + _frac("<i>k T</i>", "<i>q</i>") + " ln "
                + _frac("(<i>I</i><sub>1</sub>/<i>A</i><sub>1</sub>)",
                        "(<i>I</i><sub>2</sub>/<i>A</i><sub>2</sub>)"), "32.87"))
    b.append(p(
        "The differential voltage appearing at the output can be amplified as shown in "
        "Figure 32.36 and used as a direct indication of absolute temperature. Additional "
        "circuitry can eliminate the offset voltage at 0 °C and provide an output in degrees "
        "Celsius or degrees Fahrenheit."))
    b.append(fig(36, F.fig(36), "en"))
    b.append(p(
        "The ability to obtain temperature sensing using semiconductor processing techniques "
        "has two significant consequences: (1) semiconductor processing and integrated circuit "
        "design can be used to improve the temperature sensor's performance for specific "
        "applications, and (2) temperature sensors can be integrated within other integrated "
        "circuits to obtain additional features. The next two sections explain these approaches."))

    # ------------------------------------------------------------- integrated
    b.append(h3("Integrated Temperature Sensors"))
    b.append(p(
        "Once a temperature sensor can be manufactured using semiconductor processing "
        "techniques, a number of shortcomings of the sensor can be corrected by additional "
        "circuitry integrated into the sensor, or by circuit techniques external to the sensor. "
        "The linearity improvement, addition of precision voltage references, precision voltage "
        "amplifiers, and digital output for direct interface to a microcontroller (MCU) are "
        "among the enhancements possible. Furthermore, resistance-measuring circuitry (i.e., "
        "RTD sensors) or cold junction compensation (i.e., thermocouple sensors) are not "
        "required. Three integrated circuits and one external circuit example are discussed."))

    b.append(h4("Integrated Digital Temperature Sensor"))
    b.append(p(
        "A monolithic (one piece of silicon) semiconductor junction temperature sensor (LM75 "
        "from National Semiconductor) that incorporates several features, including a digital "
        "output, is shown in Figure 32.37 [3]. The analog signal of the temperature sensor is "
        "converted to digital format by an on-board sigma–delta converter [3]. Digital "
        "communication is provided directly to a host microcontroller through a serial two-wire "
        "interface. The sensor has a software-programmable setpoint that can be used to "
        "terminate the operation of the controller or implement protection [5]. To avoid false "
        "triggering, a user-programmable number of comparisons (up to six successive "
        "over-temperature occurrences) can be implemented. Eight different sensors can be "
        "operated on the bus. Resolution is ±½ °C and the accuracy is ±2 % from −25 °C to "
        "+100 °C. The sensor consumes 250 µA during operation and only 10 µA in sleep mode."))
    b.append(fig(37, F.fig(37), "en"))

    b.append(h4("Analog Output Integrated Temperature Sensor"))
    b.append(p(
        "Another approach to integrated temperature sensing is shown in Figure 32.38 [4]. The "
        "TMP-1 resistor-programmable temperature controller features a 5 mV °C⁻¹ output, high "
        "and low set points, and over- and under-temperature output. A low-drift voltage "
        "reference is also included in the 70 mil × 78 mil (2.76 mm × 3.07 mm) design. "
        "Figure 32.39 shows a photomicrograph of the silicon die. The TMP-1 is specified for "
        "operation between −55 °C and +125 °C, with ±1 °C accuracy over the entire range."))
    b.append(fig(38, F.fig(38), "en"))
    b.append(fig(39, F.fig(39), "en"))

    b.append(h4("Digital Output Temperature Sensor"))
    b.append(p(
        "A direct-to-digital temperature sensor has been designed for multi-drop temperature "
        "sensing applications [6]. A unique serial number is etched onto each device. The "
        "64-bit read-only memory (ROM) identifies the temperature of a particular sensor in a "
        "measurement system, with several sensors providing readings from different locations. "
        "The signal can be transmitted for distances up to 300 m."))
    b.append(p(
        "The temperature sensor operates from −55 °C to 125 °C with the power supplied from the "
        "data line. The measurement is resolved in 0.5 °C increments as a 9-bit digital value, "
        "with the conversion occurring within 200 ms. User-definable alarm settings are included "
        "in the device."))

    b.append(h4("External Circuitry Eliminates Calibration"))
    b.append(p(
        "External circuitry can be designed to utilize the inherent sensing capability of "
        "low-cost transistors without incurring the additional cost of integrated circuitry or "
        "the need to calibrate each device. The circuit shown in Figure 32.40 uses an integrated "
        "circuit (LTC1043 from Linear Technology Corporation) to provide a 0 V to 10 V output "
        "from 0 °C to 100 °C, with an accuracy of ±1 °C using <i>any</i> common small-signal "
        "transistor as the temperature sensor [7]. The circuitry establishes a "
        "ΔV<sub>be</sub> vs. current relationship that is constant regardless of the "
        "V<sub>be</sub> diode's absolute value. Substituting different transistors from "
        "multiple sources showed a variation of less than 0.4 °C."))
    b.append(fig(40, F.fig(40), "en"))

    # ------------------------------------------------------- other applications
    b.append(h3("Other Applications of Semiconductor Sensing Techniques"))
    b.append(p(
        "Several semiconductor parameters vary linearly over the operating temperature range. "
        "Power MOSFETs used to switch high levels of current (typically several amperes) at "
        "voltages that can exceed 500 V provide an example of these characteristics. As shown "
        "in Figure 32.41 [8], the gate threshold voltage of a power MOSFET changes from 1.17 to "
        "0.65 times its 25 °C value when the temperature increases from −40 °C to 150 °C. "
        "Also, the breakdown voltage of the power MOSFET varies from 0.9 to 1.18 times its "
        "value at 25 °C over the same temperature range (Figure 32.42) [8]. These relationships "
        "are frequently used to determine the junction temperature of a semiconductor component "
        "in actual circuit operation during the design phase (see “Reliability Implications”). "
        "External package-level temperature measurements can be many degrees lower than the "
        "junction temperature, especially during rapid, high-energy switching events. The "
        "actual junction temperature and the resulting effect on semiconductor parameters must "
        "be taken into account for the proper application of semiconductor devices."))
    b.append(fig(41, F.fig(41), "en"))
    b.append(fig(42, F.fig(42), "en"))
    b.append(p(
        "Polysilicon diodes (and resistors) that are isolated from the power MOSFET can be "
        "produced as part of the semiconductor manufacturing process with minor process "
        "modifications. The diodes can be used as temperature sensing elements in an actual "
        "application [9]. The thermal sensing performed by the polysilicon elements is a "
        "significant improvement over power-device temperature sensing performed by an external "
        "temperature sensing element. By sensing with polysilicon diodes, the sensor can be "
        "located close to the centre of the power device near the source bond pads, where the "
        "current density is highest and, consequently, the highest die temperature occurs."))
    b.append(p(
        "The thermal conductivity of the oxide that separates the polysilicon diodes from the "
        "power device is 2 orders of magnitude less than that of silicon. However, because the "
        "layer is thin, the polysilicon element offers an accurate indication of the actual "
        "peak junction temperature."))
    b.append(p(
        "A power FET that incorporates temperature sensing diodes is shown in Figure 32.43 [9]. "
        "By monitoring the output voltage when a constant current is passed through the "
        "integrated polysilicon diode(s), an accurate indication of the maximum die temperature "
        "is obtained. A number of diodes are actually provided in the design. A single diode in "
        "this design has a temperature coefficient of 1.90 mV °C⁻¹. Two or more can be placed in "
        "series if a larger output is desired. For greater accuracy, the diodes can be trimmed "
        "during wafer-level testing by blowing fusible links made from polysilicon. The response "
        "time of the diodes is less than 100 ms, which has allowed the device to withstand a "
        "direct connection across an automobile battery with external circuitry providing "
        "shutdown prior to device failure. The sensing capability also allows the output device "
        "to provide an indication (with additional external circuitry) if the heatsinking is "
        "not proper when the unit is installed in a module, or if a change occurs in the "
        "application that would ultimately cause a failure."))
    b.append(fig(43, F.fig(43), "en"))

    # --------------------------------------------------------------- power ICs
    b.append(h3("Temperature Sensing in Power ICs for Fault Protection and Diagnostics"))
    b.append(p(
        "Sensing for fault conditions, such as a short-circuit, is an integral part of many "
        "smart power (or power) ICs. The ability to obtain temperature sensors in the "
        "semiconductor process provides protection and diagnostics as part of the features of "
        "these devices. The primary function of the power IC is to provide a "
        "microcontroller-to-load interface for a variety of loads. In multiple-output devices, "
        "sensing the junction temperature of each device allows the status of each device to be "
        "provided to the microcontroller (MCU), and, if necessary, the MCU can shut down a "
        "particular unit that has a fault condition."))
    b.append(p(
        "A <i>smart power IC</i> can have multiple power drivers integrated on a single "
        "monolithic piece of silicon [10]. Each of these drivers can have a temperature sensor "
        "integrated to determine the proper operating status and shut off only a specific "
        "driver if a fault occurs. Figure 32.44 shows an eight-output driver that independently "
        "shuts down the output of a particular driver if its temperature is excessive (i.e., "
        "between 155 °C and 185 °C) [10]."))
    b.append(fig(44, F.fig(44), "en"))
    b.append(p(
        "The octal serial switch (OSS) adds independent thermal sensing through "
        "over-temperature detection circuitry to the protection features. Faults can be "
        "detected for each output device, and individual shutdown can be implemented. In a "
        "multiple-output power IC, it is highly desirable to shut down only the device that is "
        "experiencing a fault condition and not all of the devices that are integrated on the "
        "power IC. With outputs in various physical locations on the chip, it is difficult to "
        "predict the thermal gradients that could occur in a fault situation. Local temperature "
        "sensing at each output, instead of a single global temperature sensor, is required."))
    b.append(p(
        "As shown in Figure 32.45, the eight outputs of the device with individual temperature "
        "sensors can be independently shut down when the thermal limit of 170 °C is exceeded "
        "[10]. All of the outputs were connected to a 16 V supply at a room temperature "
        "ambient. A total current of almost 30 A initially flowed through the device. Note that "
        "each device turns off independently — the hottest device turns off first. Variations "
        "can result from differences in current level and thermal resistance. As each device "
        "turns off, the total power dissipation in the chip decreases and the devices that are "
        "still on can dissipate heat more effectively."))
    b.append(fig(45, F.fig(45), "en"))
    b.append(p(
        "Connecting directly to the battery is a hard short that could have been detected by "
        "current limit circuitry. However, a <i>soft short</i> is below the current limit, but "
        "exceeds the power-dissipating capability of the chip, and can be an extremely "
        "difficult condition to detect. Soft shorts require over-temperature sensing to protect "
        "the IC from destructive temperature levels."))
    b.append(p(
        "The over-temperature condition sensed by the power IC could mean that the device turns "
        "itself off to prevent failure in one case; and in another situation, a fault signal "
        "provides a warning to the MCU but no action is taken, depending on the fault circuit "
        "design. The remaining portion of the system is allowed to function normally. With the "
        "fault conditions supplied to the MCU, an orderly system shutdown can be implemented. "
        "Integrated temperature sensing is essential to provide this type of protection in a "
        "multiple-output power IC."))

    # ------------------------------------------------------------- reliability
    b.append(h3("Reliability Implications of Temperature to Electronic Components"))
    b.append(p(
        "The effect of temperature on electronic components and their successful application in "
        "electronic systems is one of the issues that must be addressed during the design of "
        "the system. Temperature affects the performance and expected life of semiconductor "
        "components. Mechanical stress created by different coefficients of thermal expansion "
        "can cause failures in thermal cycling tests (air-to-air) or during thermal shock "
        "(water-to-water) transitions."))
    b.append(p(
        "The typical failure rate for a semiconductor component can be expressed by the "
        "Arrhenius equation [9]:"))
    b.append(eq("λ = <i>A</i> exp " + _frac("−Ø", "<i>K T</i>"), "32.88"))
    b.append(wl([
        "where &nbsp;λ = failure rate",
        "&nbsp;<i>A</i> = constant",
        "&nbsp;Ø = activation energy (eV)",
        "&nbsp;<i>K</i> = Boltzmann's constant (8.62 · 10⁻⁵ eV K⁻¹)",
        "&nbsp;<i>T</i> = junction temperature (K)",
    ]))
    b.append(p(
        "The failure rate of semiconductor components is typically stated to double for every "
        "10 to 15 °C increase in operating (i.e., junction) temperature. However, increased "
        "testing and design improvements have minimized the failures due to specific failure "
        "mechanisms."))
    b.append(p(
        "One of the temperature-related parameters that must be taken into account during the "
        "design phase of a power switch is the transient thermal response, designated "
        "<i>r</i>(<i>t</i>) · <i>R</i><sub>θJC</sub>, where <i>r</i>(<i>t</i>) represents the "
        "normalized transient thermal resistance. The value of <i>r</i>(<i>t</i>) is "
        "determined from the semiconductor manufacturer's data sheet using the duty cycle and "
        "pulse duration used in the application. This reduced level of thermal resistance (see "
        "“Junction Temperature Measurement”), based on the transistor operating in a switching "
        "mode and being off for a period of time, approaches the dc level within a second. "
        "Excessive temperatures can be generated quickly and must be detected within "
        "milliseconds to prevent failure."))

    # --------------------------------------------------- junction temperature
    b.append(h3("Junction Temperature Measurement"))
    b.append(p(
        "In a semiconductor, the change in temperature is directly related to the power "
        "dissipated through the thermal resistance. The steady-state dc thermal resistance "
        "junction-to-case, <i>R</i><sub>θJC</sub>, is defined as the temperature rise per unit "
        "power above an external reference point (typically the case). The relationship is "
        "shown in Equation 32.89 [8]:"))
    b.append(eq("<i>R</i><sub>θJC</sub> = "
                + _frac("Δ<i>T</i>", "<i>P</i><sub>D</sub>"), "32.89"))
    b.append(wl([
        "where &nbsp;Δ<i>T</i> = junction temperature minus the case temperature (°C)",
        "&nbsp;<i>P</i><sub>D</sub> = power dissipated in the junction (W)",
    ]))
    b.append(p(
        "The semiconductor device or silicon die is typically enclosed in a package that "
        "prevents a direct measurement of the junction temperature. The junction temperature is "
        "measured indirectly by measuring the case temperature <i>T</i><sub>C</sub>; the "
        "heatsink temperature <i>T</i><sub>S</sub>, for those higher-power applications that "
        "require a heatsink; the ambient temperature <i>T</i><sub>A</sub>; and a "
        "temperature-sensitive electrical parameter of the device."))
    b.append(p(
        "The first step of the process requires calibrating the temperature-sensitive "
        "parameter. Using a bipolar power transistor as an example, the base–emitter forward "
        "voltage is measured and recorded with a low calibration current "
        "(<i>I</i><sub>M</sub>) flowing through the device that is low enough to avoid "
        "self-heating (typically between 2 mA and 10 mA) and yet sufficiently high to be in the "
        "linear range of the forward voltage curve. The procedure is performed at room and "
        "elevated temperatures, typically 100 °C."))
    b.append(p(
        "After calibration, a power switching fixture (such as Figure 32.46) is used to "
        "alternately apply and interrupt the power to the device [8]. The on portion is long "
        "(typically several milliseconds) and the off portion is short (only a few hundred µs), "
        "so that the temperature of the case is stabilized and junction cooling is minimal. "
        "The transistor is operated in its active region and the power dissipation is varied by "
        "adjusting <i>I</i><sub>E</sub> and/or <i>V</i><sub>CE</sub> until the junction is at "
        "the calibration temperature. This point is known by measuring <i>V</i><sub>BE</sub> "
        "during the time that <i>I</i><sub>M</sub> is the only current flowing."))
    b.append(fig(46, F.fig(46), "en"))
    b.append(p(
        "When the <i>V</i><sub>BE</sub> value equals the value on the calibration curve, the "
        "junction temperature is at the calibration temperature. Measurements of "
        "<i>V</i><sub>BE</sub>, <i>T</i><sub>C</sub>, and <i>I</i><sub>E</sub> allow the thermal "
        "resistance for the device to be calculated using Equation 32.89. Since "
        "<i>R</i><sub>θJC</sub> is a constant, subsequent measurements of <i>T</i><sub>C</sub>, "
        "<i>V</i><sub>CE</sub>, and <i>I</i><sub>E</sub> under different operating conditions "
        "can be used to calculate the junction temperature, to keep the device within its safe "
        "operating range in the actual application. For devices with different electrical "
        "characteristics, such as the power MOSFETs discussed earlier, other parameters that "
        "have a linear relationship to temperature are used for calibration and measurement."))

    # -------------------------------------------------------------- packaging
    b.append(h3("Semiconductor Temperature Sensor Packaging"))
    b.append(p(
        "Temperature sensors manufactured using semiconductor technology are typically "
        "packaged in packages common to the semiconductor industry. These include metal can "
        "(TO-99), ceramic, and the more commonly available plastic (SOT-23, 8-lead DIP, TO-92, "
        "8-lead SOIC, etc.) packages. These packages are designed for circuit board solder "
        "attachment that can be either through-hole or surface-mount technology. As a result, "
        "package form factors can be considerably different from packages for temperature "
        "sensors manufactured using other technologies. Figure 32.47 shows examples of five "
        "available silicon temperature sensor packages."))
    b.append(fig(47, F.fig(47), "en"))

    # ---------------------------------------------------------- defining terms
    b.append(h3("Defining Terms"))
    b.append(defs([
        ("<b>Bandgap reference</b>",
         "Forward-biased emitter junction characteristics of adjacent transistors used to "
         "provide an output voltage with zero temperature coefficient."),
        ("<b>Die</b>", "An unpackaged semiconductor chip separated from the wafer."),
        ("<b>Embedded sensor</b>", "A sensor included within an integrated circuit."),
        ("<b>Integrated circuit</b>",
         "A multiplicity of transistors, as well as diodes, resistors, capacitors, etc., on "
         "the same silicon die."),
        ("<b>Junction</b>",
         "The interface at which the conductivity type of a material changes from <i>p</i> "
         "type to <i>n</i> type."),
        ("<b>Junction voltage</b>",
         "The voltage drop across a forward-biased <i>pn</i> interface in a transistor "
         "(V<sub>be</sub>) or diode."),
        ("<b>Junction temperature</b>",
         "The temperature of the <i>pn</i> interface in a transistor or diode."),
        ("<b>Monolithic (integrated circuit)</b>",
         "Constructed from a single piece of silicon."),
        ("<b>Power IC or smart power IC</b>",
         "Hybrid or monolithic (semiconductor) device that is capable of being "
         "conduction-cooled, performs signal conditioning, and includes a power control "
         "function such as fault management and/or diagnostics."),
        ("<b>Self-heating</b>",
         "Temperature rise within a (semiconductor) device caused by current flowing in the "
         "device."),
        ("<b>Soft short</b>",
         "An excessive load condition that causes excessive temperature but is below the "
         "current limit of a device."),
        ("<b>Thermal resistance</b>",
         "The steady-state dc thermal resistance junction-to-case, "
         "<i>R</i><sub>θJC</sub>, is the temperature rise per unit power above an external "
         "reference point (typically the case)."),
        ("<b>TinyPak</b>", "A trademark of National Semiconductor Corp."),
    ]))
    b.append(note(
        "Translator's note: the scanned source (CRC Press, 1999) drops or spaces several unit "
        "symbols — notably ±, µA, µs and °C. Values in this section (±3.0 mV, 250 µA / 10 µA, "
        "≤ 300 µs, etc.) are restored from the technical context and the corresponding device "
        "data sheets; the diode response time “less than 100 ms” is retained as printed."))
    return "".join(b) + _refs325("en")


def _refs325(lang):
    """§32.5 has its own reference list — numbered 1–10 within the section."""
    vi = lang == "vi"
    items = [
        "1. J. Carr, <i>Sensors and Circuits</i>, Englewood Cliffs, NJ, PTR Prentice-Hall, 1993.",
        "2. <i>Pressure Sensor Device Data</i> DL200/D Rev. 1, Phoenix, AZ, Motorola, 1994.",
        "3. K. Lacanette, Silicon temperature sensors: theory and applications, "
        "<i>Measurements and Control</i>, pp. 120–126, April 1996.",
        "4. R. Wegner and H. Hulsemann, New family of monolithic temperature sensor and "
        "controller circuits present challenges in maintaining temperature measurement "
        "accuracy, <i>Proceedings of Sensors Expo West</i>, Anaheim, CA, Feb. 8–10, 1994.",
        "5. W. Schweber, Temperature sensors fill different needs, <i>EDN</i>, p. 20, 3/14/96.",
        "6. Digital thermometer IC simplifies distributed sensing, <i>Electronic Products</i>, "
        "p. 56, 12/95.",
        "7. J. Williams, High performance signal conditioning for transducers, "
        "<i>Proceedings of Sensors Expo West</i>, San Jose, CA, March 2–4, 1993.",
        "8. <i>TMOS Power MOSFET Transistor Data</i> DL135/D Rev. 4, Phoenix, AZ, Motorola "
        "Semiconductor.",
        "9. R. K. Jurgen (ed.), <i>Automotive Electronics Handbook</i>, New York, McGraw-Hill, "
        "1994.",
        "10. R. Frank, <i>Understanding Smart Sensors</i>, Boston, MA, Artech House, 1995.",
    ]
    head_ = ("<h3 id=\"t32-tltk-5\">Tài liệu tham khảo</h3>" if vi else
             "<h3 id=\"t32-tltk-5\">References</h3>")
    return head_ + wl(items)


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
    ("32.4", "Thermocouple Thermometers", "Nhiệt kế cặp nhiệt điện", [
        ("The Simplest Thermocouple", "Cặp nhiệt điện đơn giản nhất"),
        ("Simple Thermocouple Thermometry", "Đo nhiệt độ bằng cặp nhiệt điện đơn giản"),
        ("Thermoelectric Effects", "Hiệu ứng nhiệt điện"),
        ("The Seebeck Effect", "Hiệu ứng Seebeck", 1),
        ("Absolute Seebeck Properties", "Các đặc tính Seebeck tuyệt đối", 1),
        ("Relative Seebeck Properties", "Các đặc tính Seebeck tương đối", 1),
        ("Realistic Thermocouple Circuits", "Mạch cặp nhiệt điện thực tế", 1),
        ("Reference Temperature", "Nhiệt độ chuẩn", 1),
        ("Extension Leads", "Dây nối dài", 1),
        ("Modular Signal Conditioning Components",
         "Các bộ phận điều chế tín hiệu dạng mô-đun", 1),
        ("Grounding, Shielding, and Noise", "Nối đất, che chắn và nhiễu", 1),
        ("Noise Problems Peculiar to Thermocouples",
         "Những vấn đề nhiễu riêng của cặp nhiệt điện", 2),
        ("Grounding", "Nối đất", 2),
        ("Balanced Thermocouple Circuits", "Mạch cặp nhiệt điện cân bằng", 2),
        ("Filtering", "Lọc", 2),
        ("Thermal Coupling", "Ghép nhiệt", 1),
        ("Static Thermometry", "Đo nhiệt độ tĩnh", 2),
        ("Transient Thermometry", "Đo nhiệt độ quá độ", 2),
        ("Thermocouple Materials", "Vật liệu cặp nhiệt điện"),
        ("Thermocouple Standardization", "Chuẩn hóa cặp nhiệt điện", 1),
        ("Low Temperature Thermometry", "Đo nhiệt độ thấp", 1),
        ("Sensitivity", "Độ nhạy", 1),
        ("Letter Designations", "Ký hiệu chữ cái", 1),
        ("Color Codes", "Mã màu", 1),
        ("Identifying Thermoelements", "Nhận dạng thân nhiệt điện", 1),
        ("The Functional Model of Thermoelectric Circuits",
         "Mô hình chức năng của mạch nhiệt điện"),
        ("The Basic Thermoelectric Circuit Element",
         "Phần tử mạch nhiệt điện cơ bản", 1),
        ("The Law of Seebeck emf", "Luật suất điện động Seebeck", 1),
        ("Corollaries from the Seebeck Law", "Các hệ quả từ Luật Seebeck", 1),
        ("The T/X Visualization Sketch", "Bản phác T/X trực quan hóa", 1),
        ("Inhomogeneity", "Độ không đồng nhất"),
        ("The Nature of Inhomogeneity", "Bản chất của độ không đồng nhất", 1),
        ("The Significance of Inhomogeneity", "Tầm quan trọng của độ không đồng nhất", 1),
        ("Testing for Inhomogeneity", "Kiểm tra độ không đồng nhất", 1),
        ("Calibration", "Hiệu chuẩn"),
        ("The Principal Thermocouple", "Cặp nhiệt điện chính", 1),
        ("Commercial Tolerances", "Dung sai thương mại", 1),
        ("Extension Leads", "Dây nối dài", 1),
        ("Reference Temperature Compensation", "Bù nhiệt độ mối nối chuẩn", 1),
        ("Monitoring Instruments", "Các dụng cụ theo dõi", 1),
        ("Thermocouple Failure and Validation", "Hỏng và kiểm định cặp nhiệt điện"),
        ("Environmental Compatibility", "Tương thích môi trường", 1),
        ("Temperature Exposure", "Tiếp xúc nhiệt độ", 1),
        ("Chemical Environment", "Môi trường hóa học", 1),
        ("Metallurgical Change", "Biến đổi luyện kim", 1),
        ("Data Acquisition", "Thu thập dữ liệu"),
        ("Thermocouple Indicators", "Các bộ chỉ thị cặp nhiệt điện", 1),
        ("Thermocouple Transmitters", "Các bộ truyền cặp nhiệt điện", 1),
        ("Recording", "Ghi chép", 1),
        ("Signal Transmission", "Truyền tín hiệu"),
        ("Extension Cable", "Cáp nối dài", 1),
        ("Wireless Transmission", "Truyền vô tuyến", 1),
        ("Sources of Thermocouple Application Information",
         "Các nguồn thông tin ứng dụng cặp nhiệt điện"),
        ("Technical Papers", "Các bài báo kỹ thuật", 1),
        ("Books, Reports, and Standards", "Sách, báo cáo và chuẩn", 1),
        ("Workshops", "Các hội thảo", 1),
        ("Trade Literature", "Tài liệu thương mại", 1),
        ("Caveat", "Lưu ý"),
        ("Summary", "Tóm tắt"),
    ]),
    ("32.5", "Semiconductor Junction Thermometers", "Nhiệt kế tiếp giáp bán dẫn", [
        ("The Transistor as a Temperature Sensor", "Transistor dùng làm cảm biến nhiệt độ"),
        ("Thermal Properties of Semiconductors: Defining Equations",
         "Tính chất nhiệt của chất bán dẫn: các phương trình định nghĩa"),
        ("Integrated Temperature Sensors", "Cảm biến nhiệt độ tích hợp"),
        ("Integrated Digital Temperature Sensor", "Cảm biến nhiệt độ số tích hợp", 1),
        ("Analog Output Integrated Temperature Sensor",
         "Cảm biến nhiệt độ tích hợp ngõ ra tương tự", 1),
        ("Digital Output Temperature Sensor", "Cảm biến nhiệt độ ngõ ra số", 1),
        ("External Circuitry Eliminates Calibration",
         "Mạch ngoài loại bỏ nhu cầu hiệu chuẩn", 1),
        ("Other Applications of Semiconductor Sensing Techniques",
         "Các ứng dụng khác của kỹ thuật cảm biến bán dẫn"),
        ("Temperature Sensing in Power ICs for Fault Protection and Diagnostics",
         "Cảm biến nhiệt độ trong IC công suất để bảo vệ và chẩn đoán sự cố"),
        ("Reliability Implications of Temperature to Electronic Components",
         "Hàm ý của nhiệt độ đối với độ tin cậy của linh kiện điện tử"),
        ("Junction Temperature Measurement", "Đo nhiệt độ tiếp giáp"),
        ("Semiconductor Temperature Sensor Packaging", "Đóng vỏ cảm biến nhiệt độ bán dẫn"),
        ("Defining Terms", "Định nghĩa thuật ngữ"),
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
            # a third element marks the nesting depth: 1 means one level down
            # (the characteristics under "Electrical Properties"), 2 two levels
            # (§32.4's Grounding / Balanced Circuits / Filtering under Noise
            # Problems, Static / Transient Thermometry under Thermal Coupling)
            deep = item[2] if len(item) > 2 else 0
            indent, size = {0: ("2.4rem", ".9rem"),
                            1: ("4.2rem", ".86rem"),
                            2: ("6.0rem", ".82rem")}[deep]
            out.append('<li style="margin-left:%s;font-size:%s;padding:.15rem 0">'
                       '<a class="t" href="#s32-%s-%s">%s</a></li>'
                       % (indent, size, num.split(".")[1], _slug(sub_en),
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
            + sec_32_3_vi() + sec_32_4_vi() + sec_32_5_vi())


def body_en():
    lede = (
        "Temperature is the most widely measured quantity in industry, and the one with the largest "
        "number of transducer families. This chapter works through eleven of them — bimetallic "
        "strips, resistance thermometers, thermistors, thermocouples, semiconductor junctions, "
        "infrared, pyroelectric, liquid-in-glass, manometric, indicators and fiber-optic probes — "
        "with the equations, figures and data tables for each.")
    return (p(lede) + sec_index(False) + sec_32_1_en() + back_en() + sec_32_2_en()
            + sec_32_3_en() + sec_32_4_en() + sec_32_5_en())


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
    meta = ("Chương 32 · theo Ch32.pdf (CRC Press, 1999) · §32.1–32.5/11 · 46 hình, 92 phương "
            "trình, 18 bảng" if vi else
            "Chapter 32 · §32.1–32.5 of 11 · 46 figures, 92 equations, 18 tables")
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
