# -*- coding: utf-8 -*-
"""Handbook Chapter 93 — Plasma-Driven Flat Panel Displays
(R.T. McGrath, R. Veerasingam — Penn State; W.C. Moffatt, R.B. Campbell — Sandia).

Writes the full Vietnamese translation and the English companion.
Figures: hb93fig.py (93.1–93.10), hb93figb.py (93.11–93.20).
Run:  python build/reader_hb_ch93.py
"""
import os

import hb93fig as A
import hb93figb as B
from reader_handbook import SLUG, head, header, footer
from chapter_nav import nav as chapter_nav

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSLUG = "ch93-plasma-driven-flat-panel-displays"
TITLE_EN = "Plasma-Driven Flat Panel Displays"
TITLE_VI = "Màn hình phẳng phóng điện plasma"
BYLINE = ("Robert T. McGrath · Ramanapathy Veerasingam — Đại học Bang Pennsylvania · "
          "William C. Moffatt · Robert B. Campbell — Phòng thí nghiệm Quốc gia Sandia")
BYLINE_EN = ("Robert T. McGrath · Ramanapathy Veerasingam, The Pennsylvania State University · "
             "William C. Moffatt · Robert B. Campbell, Sandia National Laboratories")
BASE_EN = "/books/read/%s/" % SLUG
BASE_VI = "/vi/books/read/%s/" % SLUG

FIGS = {n: getattr(A, "fig_93_%d" % n) for n in range(1, 11)}
FIGS.update({n: getattr(B, "fig_93_%d" % n) for n in range(11, 21)})


def fig(num, lang="vi"):
    svg, cap_vi, cap_en, _av, _ae = FIGS[num]()
    return ('<figure class="figure" id="fig-93-%d">%s<figcaption class="figcap">%s</figcaption>'
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


def table(hd, rows, cap, cls="", style="", nw=(), colw=()):
    # `tbl-wrap` is the class the stylesheet actually styles (overflow-x:auto);
    # `table-wrap` is kept for the other chapters' markup.
    # `nw` lists the columns that must not wrap (short codes: brand, ratio, pixel count).
    def cell(tag, i, c):
        st = ' style="white-space:nowrap"' if i in nw else ""
        return "<%s%s>%s</%s>" % (tag, st, c, tag)

    body = "".join("<tr>%s</tr>" % "".join(cell("td", i, c) for i, c in enumerate(r))
                   for r in rows)
    head = "".join(cell("th", i, h) for i, h in enumerate(hd))
    colg = ""
    if colw:
        colg = "<colgroup>%s</colgroup>" % "".join('<col style="width:%dpx">' % w for w in colw)
    return ('<div class="table-wrap"><table class="tbl%s"%s>%s<thead><tr>%s</tr></thead>'
            '<tbody>%s</tbody></table></div>'
            '<p style="font-size:.84rem;color:#888;font-style:italic">%s</p>'
            % (cls, (' style="%s"' % style) if style else "", colg, head, body, cap))


# ================================================================ EQUATIONS
_EQ = {
    "93.1": ("Ne + <i>e</i><sup>–</sup> → Ne<sup>+</sup> + 2<i>e</i><sup>–</sup>"),
    "93.2a": ("Ne + <i>e</i><sup>–</sup> → Ne<sup>*x</sup> + <i>e</i><sup>–</sup>"),
    "93.2b": ("Ne<sup>*x</sup> → Ne + <i>h</i>ν"),
    "93.3": ("Ne<sup>*</sup> + Ar → Ne + Ar<sup>+</sup> + <i>e</i><sup>–</sup>"),
    "93.4": ("∇·<b>E</b>(<i>x</i>) = 4πρ(<i>x</i>) = 4π<i>e</i>[<i>n</i><sub>i</sub>(<i>x</i>) − "
             "<i>n</i><sub>e</sub>(<i>x</i>)]"),
    "93.5": ("λ<sub>D</sub> = √[<i>kT</i><sub>e</sub> / 4π<i>e</i><sup>2</sup>"
             "<i>n</i><sub>e</sub>(<i>x</i>)]"),
    "93.6": ("<i>V</i><sub>a</sub> = <i>I</i>(<i>R</i> + <i>R</i><sub>P</sub>) ≈ <i>IR</i>"),
    "93.7": ("<i>V</i><sub>a</sub>(<i>t</i>) = <i>I</i>(<i>t</i>)<i>R</i> + (1/<i>C</i>)"
             "∫<sub>0</sub><sup><i>t</i></sup><i>I</i>(<i>t</i>′)d<i>t</i>′ = "
             "<i>I</i>(<i>t</i>)<i>R</i> + <i>Q</i>(<i>t</i>)/<i>C</i>"),
    "93.8": ("<i>V</i><sub>a</sub>(<i>t</i>) = (1/<i>C</i>)∫<sub>0</sub><sup><i>t</i></sup>"
             "<i>I</i>(<i>t</i>′)d<i>t</i>′ = <i>Q</i>(<i>t</i>)/<i>C</i>"),
    "93.9": ("1/<i>C</i> = 1/<i>C</i><sub>PbO</sub> + 1/<i>C</i><sub>MgO</sub> + "
             "1/<i>C</i><sub>gas</sub>"),
    "93.10": ("<i>C</i><sub>i</sub> = ε<sub>i</sub><i>A</i> / <i>d</i><sub>i</sub>"),
    "93.11": ("<i>I</i>(<i>t</i>) = <i>C</i> d<i>V</i>(<i>t</i>)/d<i>t</i>"),
}


def _eq(num):
    return _EQ[num]


# ================================================================ TABLES
# TABLE 93.1 — panel specifications and manufacturers' plans
_T1 = [
    ("Fujitsu", "42", "16:9", "852 × 480", "300", "70:1", "0,7", "350 (bộ) / 300 (tấm)",
     "Miyazaki", "20", "10.000", "Châu Âu, Nhật"),
    ("NEC", "33", "4:3", "640 × 480", "200", "150:1", "1,2", "270 (bộ) / 190 (tấm)",
     "Tamagawa", "5", "2.000", "Nhật"),
    ("Pioneer", "40", "4:3", "640 × 480", "400", "150:1", "1,2", "350 (bộ)", "Kofu", "5",
     "10.000", "Nhật"),
    ("Mitsubishi", "40", "4:3", "640 × 480", "350", "200:1", "0,8", "350 (bộ) / 300 (tấm)",
     "Kyoto", "14,8", "10.000", "Hoa Kỳ"),
    ("MEC", "42", "16:9", "852 × 480", "450", "150:1", "10", "300 (tấm)", "Kyoto", "10",
     "5.000", "Nhật, Hoa Kỳ"),
    ("Photonics", "21", "5:4", "1280 × 1024", "100", "50:1", "—", "300 (tấm)", "Ohio", "—",
     "—", "—"),
    ("Hitachi", "25", "4:3", "1024 × 768", "150", "50:1", "—", "250 (bộ)", "Yokohama", "3",
     "1.000", "—"),
    ("NHK", "40", "16:9", "1344 × 800", "93", "80:1", "—", "—", "—", "—", "—", "—"),
]

_T1_EN = [
    ("Fujitsu", "42", "16:9", "852 × 480", "300", "70:1", "0.7", "350 (set) / 300 (panel)",
     "Miyazaki", "20", "10,000", "Europe, Japan"),
    ("NEC", "33", "4:3", "640 × 480", "200", "150:1", "1.2", "270 (set) / 190 (panel)",
     "Tamagawa", "5", "2,000", "Japan"),
    ("Pioneer", "40", "4:3", "640 × 480", "400", "150:1", "1.2", "350 (set)", "Kofu", "5",
     "10,000", "Japan"),
    ("Mitsubishi", "40", "4:3", "640 × 480", "350", "200:1", "0.8", "350 (set) / 300 (panel)",
     "Kyoto", "14.8", "10,000", "U.S."),
    ("MEC", "42", "16:9", "852 × 480", "450", "150:1", "10", "300 (panel)", "Kyoto", "10",
     "5,000", "Japan, U.S."),
    ("Photonics", "21", "5:4", "1280 × 1024", "100", "50:1", "—", "300 (panel)", "Ohio", "—",
     "—", "—"),
    ("Hitachi", "25", "4:3", "1024 × 768", "150", "50:1", "—", "250 (set)", "Yokohama", "3",
     "1,000", "—"),
    ("NHK", "40", "16:9", "1344 × 800", "93", "80:1", "—", "—", "—", "—", "—", "—"),
]


def _table1(lang):
    if lang == "vi":
        hd = ["Hãng", "Inch", "Tỉ lệ", "Điểm ảnh", "Độ chói (cd/m²)", "Tương phản", "lm/W",
              "Công suất (W)", "Nhà máy", "Vốn ($M)", "SL/tháng", "Thị trường"]
        cap = ("Bảng 93.1 · Thông số tấm hiển thị plasma và kế hoạch kinh doanh của nhà sản "
               "xuất (số liệu cam kết tính đến tháng 1/1997). Nguồn in “50.1” cho tương phản "
               "của Hitachi, rõ ràng là 50:1.")
        return hd, _T1, cap
    hd = ["Company", "Inch", "Aspect", "Pixels", "Luminance (cd/m²)", "Contrast", "lm/W",
          "Power (W)", "Factory", "Capital ($M)", "Units/month", "Region"]
    cap = ("TABLE 93.1 · Plasma panel specifications and manufacturers' business plans "
           "(commitments as of January 1997). The source prints “50.1” for Hitachi's contrast, "
           "evidently 50:1.")
    return hd, _T1_EN, cap


# TABLE 93.2 — phosphors. The source text layer mangles several formulae; the
# plausible compound is printed here and the printed form is listed in the note.
_T2 = [
    ("NTSC lục", "—", "—", "—", "0,21", "0,71"),
    ("(La<sub>0,87</sub>Tb<sub>0,13</sub>)PO<sub>4</sub>", "1,1", "1,4", "13", "0,34", "0,57"),
    ("(La<sub>0,6</sub>Ce<sub>0,27</sub>Tb<sub>0,13</sub>)PO<sub>4</sub>", "1,1", "1,5", "12",
     "0,33", "0,59"),
    ("(Y<sub>0,85</sub>Ce<sub>0,1</sub>Tb<sub>0,05</sub>)PO<sub>4</sub>", "1,1", "1,1", "—", "—",
     "—"),
    ("(Y<sub>0,6</sub>Ce<sub>0,27</sub>Tb<sub>0,13</sub>)PO<sub>4</sub>", "1,35", "1,35", "—",
     "—", "—"),
    ("(Gd<sub>0,87</sub>Ce<sub>0,1</sub>Tb<sub>0,03</sub>)PO<sub>4</sub>", "1,0", "1,1", "10",
     "0,34", "0,58"),
    ("(Gd<sub>0,6</sub>Ce<sub>0,27</sub>Tb<sub>0,13</sub>)PO<sub>4</sub>", "1,35", "1,45", "—",
     "—", "—"),
    ("(Ce,Tb)MgAl<sub>11</sub>O<sub>19</sub>", "0,9", "1,4", "—", "—", "—"),
    ("Sr<sub>0,9</sub>Al<sub>2</sub>O<sub>4</sub>:Eu<sup>2+</sup> (3 %)", "0,4", "0,7", "0,01",
     "0,26", "0,59"),
    ("Zn<sub>2</sub>SiO<sub>4</sub>:Mn", "1,2", "1,3", "12,5", "0,21", "0,72"),
    ("Zn<sub>2</sub>SiO<sub>4</sub>:Mn", "1,1", "1,5", "9,8", "—", "—"),
    ("Zn<sub>2</sub>SiO<sub>4</sub>:Mn", "0,45", "0,55", "5,4", "—", "—"),
    ("Zn<sub>2</sub>SiO<sub>4</sub>:Mn", "1,0", "1,1", "5", "—", "—"),
    ("Zn<sub>2</sub>SiO<sub>4</sub>:Mn", "1,0", "—", "—", "0,21", "0,72"),
    ("BaAl<sub>12</sub>O<sub>19</sub>:Mn", "1,1", "—", "—", "0,16", "0,74"),
    ("BaMgAl<sub>14</sub>O<sub>23</sub>:Mn", "0,92", "—", "—", "0,15", "0,73"),
    ("SrAl<sub>12</sub>O<sub>19</sub>:Mn", "0,62", "—", "—", "0,16", "0,75"),
    ("ZnAl<sub>12</sub>O<sub>19</sub>:Mn", "0,54", "—", "—", "0,17", "0,74"),
    ("CaAl<sub>12</sub>O<sub>19</sub>:Mn", "0,34", "—", "—", "0,15", "0,75"),
    ("YBO<sub>3</sub>:Tb", "1,1", "—", "—", "0,33", "0,61"),
    ("LuBO<sub>3</sub>:Tb", "1,1", "—", "—", "0,33", "0,61"),
    ("GdBO<sub>3</sub>:Tb", "0,53", "—", "—", "0,33", "0,61"),
    ("ScBO<sub>3</sub>:Tb", "0,36", "—", "—", "0,35", "0,60"),
    ("Sr<sub>4</sub>Si<sub>8</sub>O<sub>8</sub>Cl<sub>4</sub>:Eu", "1,3", "—", "—", "0,14",
     "0,33"),
    ("NTSC đỏ", "—", "—", "—", "0,67", "0,33"),
    ("Y<sub>2</sub>O<sub>3</sub>:Eu", "—", "0,67", "—", "0,65", "0,34"),
    ("Y<sub>2</sub>SiO<sub>5</sub>:Eu", "—", "0,62", "—", "0,66", "0,34"),
    ("Y<sub>3</sub>Al<sub>5</sub>O<sub>12</sub>:Eu", "—", "0,47", "—", "0,63", "0,37"),
    ("Zn<sub>8</sub>(PO<sub>4</sub>)<sub>2</sub>:Mn", "—", "0,34", "—", "0,67", "0,33"),
    ("YBO<sub>3</sub>:Eu", "—", "1,0", "—", "0,65", "0,35"),
    ("(Y,Gd)BO<sub>3</sub>:Eu", "—", "1,2", "—", "0,65", "0,35"),
    ("GdBO<sub>3</sub>:Eu", "—", "0,94", "—", "0,64", "0,36"),
    ("ScBO<sub>3</sub>:Eu", "—", "0,94", "—", "0,61", "0,39"),
    ("LuBO<sub>3</sub>:Eu", "—", "0,74", "—", "0,63", "0,37"),
    ("NTSC lam", "—", "—", "—", "0,14", "0,08"),
    ("CaWO<sub>4</sub>:Pb", "—", "0,74", "—", "0,17", "0,17"),
    ("Y<sub>2</sub>SiO<sub>5</sub>:Ce", "—", "1,1", "—", "0,16", "0,09"),
    ("BaMgAl<sub>14</sub>O<sub>23</sub>:Mn", "—", "1,6", "—", "0,14", "0,09"),
]


def _table2(lang):
    if lang == "vi":
        hd = ["Phosphor", "QE tương đối (174 nm)", "QE tương đối (170 nm)",
              "Thời gian tắt 10 % (ms)", "x", "y"]
        cap = ("Bảng 93.2 · Hiệu suất lượng tử tương đối và toạ độ màu của một số phosphor. "
               "Các giá trị QE phía trên đường kép tính theo chuẩn natri salicylat, phía dưới "
               "tính theo Zn<sub>2</sub>SiO<sub>4</sub>:Mn.")
        return hd, _T2, cap
    hd = ["Phosphor", "Rel. QE (174 nm)", "Rel. QE (170 nm)", "Lifetime 10% (ms)", "x", "y"]
    cap = ("TABLE 93.2 · Relative quantum efficiencies and chromaticity coordinates for "
           "selected phosphors. QEs above the double rule are relative to sodium salicylate, "
           "those below to Zn<sub>2</sub>SiO<sub>4</sub>:Mn.")
    return hd, _T2, cap


# TABLE 93.3 — noncontact profiling equipment
_T3 = [
    ("Nguyên lý", "Tam giác hoá laser", "Giao thoa ánh sáng trắng quét",
     "Giao thoa laser"),
    ("Chiều dày/bậc cao tối đa", "150 µm (đầu đo phân giải cao)", "100 µm (chuẩn), tới 5 mm "
     "với trục z", "70 µm"),
    ("Phân giải theo phương đứng", "0,38 µm", "100 pm", "150 pm hoặc 0,5 %"),
    ("Phân giải không gian", "&gt; 0,5 µm", "0,22 µm", "0,5 µm"),
    ("Đường kính điểm đo / trường nhìn", "5,1 µm", "140 × 110 µm", "20 µm"),
    ("Tốc độ quét", "10 điểm/s", "2 hoặc 4 mm/s", "tối đa 75 mm/s"),
    ("Kích thước mẫu tối đa", "Theo bàn dịch chuyển", "10 × 15 cm", "47 × 37 cm"),
    ("Khối lượng mẫu tối đa", "Theo bàn dịch chuyển", "4,5 kg", "4,5 kg (kể cả giá đỡ)"),
    ("Phân tích nguyên tố", "Không", "Không", "Không"),
]

_T3_EN = [
    ("Physical principle", "Laser triangulation", "Scanning white light interferometry",
     "Laser interferometry"),
    ("Maximum thickness/step height", "150 µm (high-resolution head)", "100 µm (standard), to "
     "5 mm with z-drive", "70 µm"),
    ("Vertical resolution", "0.38 µm", "100 pm", "150 pm or 0.5%"),
    ("Spatial resolution", "&gt; 0.5 µm", "0.22 µm", "0.5 µm"),
    ("Spot diameter / FOV", "5.1 µm", "140 × 110 µm", "20 µm"),
    ("Scan rate", "10 points/s", "2 or 4 mm/s", "75 mm/s max."),
    ("Maximum sample size", "Based on table", "10 × 15 cm", "47 × 37 cm"),
    ("Maximum sample weight", "Based on table", "4.5 kg", "4.5 kg (including holder)"),
    ("Elemental detection", "N.A.", "N.A.", "N.A."),
]


def _table3(lang):
    if lang == "vi":
        hd = ["Thông số", "CyberOptics Point Range Sensor", "Zygo NewView 200",
              "Leitz FTM400"]
        cap = ("Bảng 93.3 · Thiết bị đo biên dạng không tiếp xúc và phân tích hoá học màng "
               "mỏng. Bản gốc in các đơn vị chiều dày bằng “mm” do lớp văn bản làm mất ký tự "
               "µ; ở đây đã khôi phục thành µm.")
        return hd, _T3, cap
    hd = ["Parameter", "CyberOptics Point Range Sensor", "Zygo NewView 200", "Leitz FTM400"]
    cap = ("TABLE 93.3 · Equipment for noncontact profiling and chemical characterisation of "
           "thin films. The original prints the thickness units as “mm” because the text layer "
           "lost the µ; they are restored here as µm.")
    return hd, _T3_EN, cap


# TABLE 93.4 — advanced techniques
_T4 = [
    ("Nguyên lý", "Tán xạ ngược beta", "Vi huỳnh quang tia X"),
    ("Chiều dày/bậc cao tối đa", "Vài µm", "50 µm"),
    ("Phân giải theo phương đứng", "Khoảng 0,1 nm", "0,1 µm"),
    ("Phân giải không gian", "Phụ thuộc kích thước lỗ kim", "50 µm đến 2 mm"),
    ("Đường kính điểm đo / trường nhìn", "Phụ thuộc kích thước lỗ kim", "100 µm"),
    ("Tốc độ quét", "&lt; 1 phút/lần đo", "1 điểm/phút"),
    ("Kích thước mẫu tối đa", "Không hạn chế", "24 × 21,5 cm"),
    ("Khối lượng mẫu tối đa", "Không hạn chế", "4,5 kg"),
    ("Phân tích nguyên tố", "Không", "&lt; 10 – 300 ppm"),
]

_T4_EN = [
    ("Physical principle", "β-backscatter", "X-ray microfluorescence"),
    ("Maximum thickness/step height", "A few µm", "50 µm"),
    ("Vertical resolution", "About 0.1 nm", "0.1 µm"),
    ("Spatial resolution", "Depends on pinhole size", "50 µm to 2 mm"),
    ("Spot diameter / FOV", "Depends on pinhole size", "100 µm"),
    ("Scan rate", "&lt; 1 min/measurement", "1 spot/min"),
    ("Maximum sample size", "No restriction", "24 × 21.5 cm"),
    ("Maximum sample weight", "No restriction", "4.5 kg"),
    ("Elemental detection", "N.A.", "&lt; 10 – 300 ppm"),
]


def _table4(lang):
    if lang == "vi":
        hd = ["Thông số", "Tán xạ ngược beta", "Vi huỳnh quang tia X"]
        cap = ("Bảng 93.4 · Hai kỹ thuật tiên tiến để đo biên dạng không tiếp xúc và phân tích "
               "hoá học màng mỏng; theo hiểu biết của các tác giả, năm 1999 chưa có thiết bị "
               "thương mại.")
        return hd, _T4, cap
    hd = ["Parameter", "β-backscatter", "X-ray microfluorescence"]
    cap = ("TABLE 93.4 · Two advanced techniques for noncontact profiling and chemical "
           "characterisation of thin films; to the authors' knowledge no commercial system "
           "existed in 1999.")
    return hd, _T4_EN, cap


# ================================================================ REFERENCES
_REFS = [
    ("D.L. Bitzer and H.G. Slottow, “The plasma display panel — a digitally addressable display "
     "with inherent memory,” 1966 Fall Joint Computer Conf., Washington, D.C., <i>AFIPS Conf. "
     "Proc.</i>, 29, 541, 1966."),
    "H.G. Slottow, “Plasma displays,” <i>IEEE Trans. Electron Devices</i>, 23, 760–772, 1976.",
    ("T.N. Criscimagna and P. Pleshko, “AC plasma display,” Chapter 3 in <i>Topics in Applied "
     "Physics</i>, Vol. 40, <i>Display Devices</i>, Springer-Verlag, Berlin, 91–150, 1980."),
    ("L.F. Weber, “Plasma displays,” Chapter 10 in <i>Flat Panel Displays and CRTs</i>, L.E. "
     "Tannas, Jr., Ed., Van Nostrand Reinhold, New York, 1985."),
    ("J. Nolan, “Gas discharge display panel,” 1969 International Electron Devices Meeting, "
     "Washington, D.C., 1969."),
    ("H.J. Hoehn and R.A. Martel, “A 60 line per inch plasma display panel,” <i>IEEE Trans. "
     "Electron Devices</i>, 18, 659–663, 1971."),
    ("O. Sahni and W.P. Jones, “Spatial distribution of wall charge density in AC plasma "
     "display panels,” <i>IEEE Trans. Electron Devices</i>, 25, 223–226, 1979."),
    ("O. Sahni and C. Lanza, “Origin of the bistable voltage margin in the AC plasma display "
     "panel,” <i>IEEE Trans. Electron Devices</i>, 24, 853–859, 1977."),
    ("C. Lanza and O. Sahni, “Numerical calculation of the characteristics of an isolated ac "
     "gas discharge display panel cell,” <i>IBM J. Res. Dev.</i>, 22, 641–646, 1978."),
    ("O. Sahni and M.O. Aboelfotoh, “The pressure dependence of the bistable voltage margin of "
     "an AC plasma panel cell,” <i>Proc. SID</i>, 22, 212–218, 1981."),
    ("O. Sahni and C. Lanza, “Importance of the secondary electron emission coefficient on E/P₀ "
     "for Paschen breakdown curves in AC plasma panels,” <i>J. Appl. Phys.</i>, 47, 1337, 1976."),
    ("O. Sahni and C. Lanza, “Influence of the secondary electron emission coefficient of argon "
     "on Paschen breakdown curves in AC plasma panels for neon + 0.1% argon mixture,” <i>J. "
     "Appl. Phys.</i>, 47, 5107, 1976."),
    "C. Lanza, “Analysis of an ac gas display panel,” <i>IBM J. Res. Dev.</i>, 18, 232–243, 1974.",
    ("O. Sahni, C. Lanza, and W.E. Howard, “One-dimensional numerical simulation of ac "
     "discharges in a high-pressure mixture of Ne + 0.1% Ar confined to a narrow gap between "
     "insulated metal electrodes,” <i>J. Appl. Phys.</i>, 49, 2365, 1978."),
    ("O. Sahni and C. Lanza, “Failure of Paschen's scaling law for Ne–0.1% Ar mixtures at high "
     "pressures,” <i>J. Appl. Phys.</i>, 52, 196, 1981."),
    ("H. Wakabayashi, “Display market projections,” report from the Nomura Research Institute, "
     "paper presented at Imaging 2001: The U.S. Display Consortium Business Conference, January "
     "28, 1997, San Jose, CA."),
    "K. Werner, “Plasma hits the ground running,” <i>Inf. Display</i>, 12(12), 30–34, 1996.",
    "<i>Nikkei Materials &amp; Technology</i>, [135], November 1993, pp. 22–23.",
    ("H. Murakami and R. Toyonaga, “A pulse discharge panel display for producing a color TV "
     "picture with high luminance and luminous efficiency,” <i>IEEE Trans. Electron Devices</i>, "
     "29, 988, 1982."),
    ("M. Ushirozawa, Y. Motoyama, T. Sakai, K. Wani, and K. Takahashi, “Color dc-PDP with an "
     "improved resistor design in each cell,” paper 33.2, 719–722, <i>SID '94 Symp. Dig.</i>, "
     "1994."),
    ("S. Mikoshiba, “Color plasma displays: where are we now?,” <i>Inf. Display</i>, 10(10), 21, "
     "1994."),
    "Y. Takano et al., “A 40-in. DC-PDP with new pulse memory drive scheme,” <i>SID '97 Dig.</i>, 1997.",
    ("P.S. Friedman, “Are plasma display panels a low-cost technology?,” <i>Inf. Display</i>, "
     "11(10), 22–25, 1995."),
    "<i>Inf. Display</i>, 10(7 &amp; 8), 28, 1994.",
    "A. von Engel, <i>Ionized Gases</i>, AIP Press, New York, 1994.",
    ("S. Brown, <i>Basic Data of Plasma Physics — The Fundamental Data on Electrical Discharges "
     "in Gas</i>, American Institute of Physics Press, New York, 1993."),
    "F.F. Chen, <i>Introduction to Plasma Physics</i>, Plenum Press, New York, 1977.",
    ("D. Miller, J. Ogle, R. Cola, B. Caras, and T. Maloney, “An improved performance self-scan "
     "I panel design,” <i>Proc. SID</i>, 22, 159–163, 1981."),
    ("M.H. Miller and R.A. Roig, “Transition probabilities of Xe I and Xe II,” <i>Phys. Rev. A</i>, "
     "8, 480, July 1973."),
    "<i>Atomic Data and Nuclear Data Tables</i>, Vol. 21, No. 6, Academic Press, New York, 1978.",
    ("R.S. Van Dyck, C.E. Johnson, and H.A. Shugart, “Lifetime lower limits for the ³P₀ and ³P₂ "
     "metastable states of neon, argon and krypton,” <i>Phys. Rev. A</i>, 5, 991–993, 1972."),
    ("A.A. Kruithof and F.M. Penning, “The Townsend ionization coefficient and some elementary "
     "processes in neon with small admixtures of argon,” <i>Physica</i>, 4(6), 450, 1937."),
    ("F.L. Jones and W.R. Galloway, “The sparking potential of mercury vapor,” <i>Proc. Phys. "
     "Soc. Lond.</i>, 50, 207–212, 1938."),
    ("R.T. McGrath, R. Veerasingam, J.A. Hunter, P.D. Rockett, and R.B. Campbell, “Measurements "
     "and simulations of VUV emissions from plasma flat panel display pixel microdischarges,” "
     "<i>IEEE Trans. Plasma Sci.</i>, 26(5), 1998."),
    ("P. Hines, “Spectroscopic and electrical measurements on opposed electrode ac plasma "
     "display pixels,” Honors engineering senior thesis, The Pennsylvania State University, "
     "University Park, 1997."),
    ("R. Veerasingam, R.B. Campbell, and R.T. McGrath, “One-dimensional single and multipulse "
     "simulations of the ON/OFF voltages and bistable margin for He, Xe, and He/Xe filled plasma "
     "display pixels,” <i>IEEE Trans. Plasma Sci.</i>, 24(6), 1399–1410, 1996."),
    ("R. Veerasingam, R.B. Campbell, and R.T. McGrath, “Two-dimensional simulations of plasma "
     "flow and charge spreading in ac plasma displays,” <i>IEEE Trans. Plasma Sci.</i>, 24, "
     "1411–1421, 1996."),
    "M. Scott, Los Alamos National Laboratory, private communication, 1997.",
    ("H. Uchiike, K. Miura, N. Nakayama, T. Shinoda, and Y. Fukushima, “Secondary electron "
     "emission characteristics of dielectric materials in AC-operated plasma display panels,” "
     "<i>IEEE Trans. Electron Devices</i>, 23, 1211–1217, 1976."),
    ("N.J. Chou and O. Sahni, “Comments on ‘Secondary emission characteristics of dielectric "
     "materials in AC operated plasma display panels’,” <i>IEEE Trans. Electron Devices</i>, 25, "
     "60–62, 1978."),
    ("T. Shinoda, H. Uchiike, and S. Andoh, “Low-voltage operated AC plasma-display panels,” "
     "<i>IEEE Trans. Electron Devices</i>, 26, 1163–1167, 1979."),
    ("M. Aboelfotoh and J.A. Lorenzen, “Influence of secondary-electron emission from MgO "
     "surfaces on voltage-breakdown curves in Penning mixtures for insulated-electrode "
     "discharges,” <i>J. Appl. Phys.</i>, 48, 4754–4759, 1977."),
    ("T. Nenadovic, B. Perraillon, Z. Bogdanov, Z. Djordjevic, and M. Milic, “Sputtering and "
     "surface topography of oxides,” <i>Nucl. Instrum. Methods Phys. Res.</i>, B48, 538–543, "
     "1990."),
    ("D. Schone, D. Walsh, R.T. McGrath, and J.H. Burkhart, “Microbeam Rutherford backscattering "
     "measurements of flat panel display thin film erosion,” <i>Nucl. Instrum. Methods Phys. "
     "Res. B</i>, 130(1–4), 543–550, 1998."),
    ("<i>CRC Handbook of Chemistry and Physics</i>, 48th ed., R.C. Weast and S.M. Selby, Eds., "
     "The Chemical Rubber Co., Cleveland, OH, 1967."),
    "S. Matsumoto, <i>Electronic Display Devices</i>, John Wiley &amp; Sons, New York, 1990.",
    ("G.E. Holz, “The primed gas discharge cell — a cost and capability improvement for gas "
     "discharge matrix displays,” <i>Proc. SID</i>, 13(2), 1972."),
    ("T. Yamamoto, T. Kuriyama, M. Seki, T. Katoh, H. Murakami, K. Shimada, and H. Ishiga, “A 40 "
     "in. diagonal HDTV plasma display,” <i>SID '93 Symp. Dig.</i>, 165–168, 1993."),
    "J. Deschamps and H. Doyeus, “Plasma displays,” <i>Phys. World</i>, June 1977.",
    ("N. Yocum, R.S. Meltzer, K.W. Jang, and M. Grimm, “New green phosphors for plasma "
     "displays,” <i>J. SID</i>, 4/3, 169–172, 1996."),
    ("H. Fujii, H. Tanabe, H. Ishiga, M. Harayama, and M. Oka, “A sandblasting process for "
     "fabrication of color PDP phosphor screens,” paper 37.5, 728–731, <i>SID '92 Symp. Dig.</i>, "
     "1992."),
    ("M.C. Castex, “Experimental determination of the lowest excited Xe₂ molecular states from "
     "VUV absorption spectra,” <i>J. Chem. Phys.</i>, 74, 759–771, 1981."),
    ("M.R. Flannery, K.J. McCann, and N.W. Winter, “Cross sections for electron impact ionisation "
     "of metastable rare gas excimers (He₂*, Kr₂*, Xe₂*),” <i>J. Phys. B Mol. Phys.</i>, 14, "
     "3789–3796, 1981."),
    ("K. Tachibana, “Spatio-temporal measurement of excited Xe(1s₄) atoms in a discharge cell of "
     "a plasma display panel by laser induced spectroscopic microscopy,” <i>Appl. Phys. Lett.</i>, "
     "65, 935–937, 1994."),
    "T. Holstein, “Imprisonment of resonance radiation in gases,” <i>Phys. Rev.</i>, 72, 1212, 1947.",
    ("De Husk and S.E. Schnatterly, “Quantum efficiency and linearity of 16 phosphors in the soft "
     "x-ray regime,” <i>J. Opt. Soc. Am. B</i>, 9, 660–663, 1992."),
    ("J. Koike, T. Kojima, and R. Toyonaga, “New tricolor phosphors for gas discharge display,” "
     "<i>J. Electrochem. Soc. Solid-State Sci. Tech.</i>, 1008, June 1979."),
    ("P.N. Yocum, “Future requirements of display phosphors from an historical perspective,” "
     "<i>J. SID</i>, 4/3, 149, 1996."),
    ("L.E. Tannas, Jr., Ed., <i>Flat Panel Displays and CRTs</i>, Van Nostrand Reinhold, New "
     "York, 1985."),
    ("S.G. McLean and W.W. Duley, “VUV absorption in thin MgO films,” <i>J. Phys. Chem. Solids</i>, "
     "45, 223, 1984."),
    "R. Kuntz, CyberOptics, private communication, 1-800-746-6315.",
    "Zygo, private communication, 1-860-347-8506, www.zygo.com.",
    ("A. Machura, Leica, private communication, +49 (0) 6441 29-2316, "
     "Andreas.Machura@lmw.leica.com."),
    ("B.E. Mills, D.A. Buchenauer, A.E. Pontau, and M. Ulrickson, “Characterization of "
     "deposition and erosion on the TFTR bumper limiter and wall,” <i>J. Nucl. Mater.</i>, "
     "162–164, 343–349, 1989."),
]


# ================================================================ VIETNAMESE
def body_vi():
    b = []

    # ------------------------------------------------------------ 93.1
    b.append(h2("93.1 Giới thiệu về màn hình phẳng phóng điện plasma",
                "An Introduction to Plasma-Driven Flat Panel Displays"))
    b.append(h3("Lịch sử phát triển và tình hình hiện nay",
                "Development History and Present Status"))
    b.append(p(
        "Điểm ảnh của màn hình phẳng phóng điện plasma được Bitzer và Slottow phát minh tại Đại "
        "học Illinois năm 1966 [1–3]. Hình 93.1 cho thấy một trong những thiết kế đầu tiên của "
        "hai tác giả và cho thấy sự giản dị của nó. Các bộ dây dẫn mảnh song song được lắng lên "
        "hai tấm nền thuỷ tinh, sau đó hai tấm được gắn sao cho hai bộ dây dẫn vuông góc với "
        "nhau. Một vòng đệm — ở đây là thuỷ tinh điện môi đục lỗ — giữ khoảng cách giữa hai tấm "
        "khoảng 100 µm. Khoảng trống sau đó được nạp khí trơ, thường ở áp suất nửa atmosphere. "
        "Mỗi điểm ảnh hình thành tại chỗ giao của hai dây dẫn được căn thẳng với một lỗ của vòng "
        "đệm. Điểm ảnh phát sáng khi đặt giữa hai dây dẫn giao nhau một điện áp đủ lớn để khởi "
        "phát đánh thủng khí. Qua nhiều năm, thiết kế cơ bản này đã được cải tiến rất nhiều, "
        "nhưng ý tưởng nền tảng vẫn còn được dùng rộng rãi."))
    b.append(fig(1))
    b.append(p(
        "Suốt những năm 1980, các sản phẩm màn hình plasma trên thị trường đều đơn sắc và làm "
        "việc với khí gốc neon, phát trực tiếp trong thể tích phóng điện các photon nhìn thấy màu "
        "đỏ cam (585–640 nm) đặc trưng cho cấu trúc mức năng lượng lượng tử của nguyên tử neon. "
        "Các màn hình ma trận điểm như trên Hình 93.2 được dùng rộng rãi [3,4]. Công trình đầu "
        "tiên của Owens-Illinois đã cải thiện kỹ thuật hàn kín thuỷ tinh và đỡ vòng đệm [5,6], "
        "còn công trình của IBM đã giúp hiểu và điều khiển phóng điện tốt hơn [7–15]. Những tiến "
        "bộ này cuối cùng đã mở đường cho việc chế tạo màn hình đơn sắc diện tích lớn, độ phân "
        "giải cao. Tấm hiển thị plasma có diện tích lớn nhất từng được chế tạo do Photonics "
        "Imaging sản xuất: màn hình đơn sắc đường chéo 1 m, hơn 2 triệu điểm ảnh, bước điểm ảnh "
        "20 điểm ảnh/cm (50 dòng/in.) [4]."))
    b.append(fig(2))
    b.append(p(
        "Tiến bộ trong kỹ thuật quang khắc, tạo hình và phosphor đã giúp hiệu năng và độ phân "
        "giải của màn hình plasma tiếp tục được cải thiện. Ngày nay nhiều hãng cung cấp màn hình "
        "phẳng plasma màu hoàn chỉnh. Bảng 93.1 liệt kê thông số tấm hiển thị của một số hãng "
        "lớn đang đầu tư vào sản xuất màn hình phẳng plasma, do Viện Nghiên cứu Quốc gia tổng hợp "
        "[16]. Theo Stanford Research, Inc., doanh số tấm hiển thị plasma năm 1995 đạt 230 triệu "
        "USD, và dự báo năm 2002 là 4,1 tỉ USD [17]. NEC dự báo mức tăng trưởng mạnh hơn: 2,0 tỉ "
        "USD vào năm 2000 và 7,0 tỉ USD vào năm 2002 [17]. Công suất sản xuất trong Bảng 93.1 "
        "phản ánh các khoản đầu tư đã cam kết tính đến tháng 1/1997. Khi các cơ sở này đi vào "
        "hoạt động, sản lượng màn hình phẳng plasma màu sẽ tăng tới gần 40.000 chiếc/tháng vào "
        "cuối năm 1998 và hơn 100.000 chiếc/tháng vào đầu năm 2000. Năm 1993, Fujitsu là hãng "
        "đầu tiên đưa ra thị trường màn hình phẳng plasma màu dung lượng thông tin cao: đường "
        "chéo 21 in., điều khiển xoay chiều, mảng điểm ảnh 640 × 480 [17,18]. Hai ví dụ mới hơn "
        "được trình bày trên Hình 93.3 và 93.4."))
    hd1, rows1, cap1 = _table1("vi")
    b.append(table(hd1, rows1, cap1, cls=" dense", nw=(0, 1, 2, 3), colw=(72, 34, 34, 78, 44, 52, 32, 62, 74, 34, 52, 62)))
    b.append(fig(3))
    b.append(p(
        "Ví dụ thứ nhất là màn hình truyền hình độ phân giải cao (HDTV) màu, đường chéo 102 cm "
        "(40 in.) của NHK [19–22]. Hệ thống gồm 1.075.000 điểm ảnh màu (1344 × 800) với bước "
        "điểm 0,65 mm theo cả hai phương (15,4 điểm ảnh/cm). Màn hình điều khiển một chiều kiểu "
        "xung này có độ chói đỉnh 93 cd/m², tỉ số tương phản 80:1 và tạo được 256 mức xám. Toàn "
        "bộ màn hình chỉ dày 8 cm và nặng 8 kg. Kích thước bản thân tấm hiển thị là 87,5 × 52,0 "
        "cm với độ dày chỉ 6 mm. Hình 93.4 là màn hình plasma xoay chiều màu, đường chéo 76 cm "
        "(30 in.), do Photonics Imaging chế tạo [23,24]. Màn hình chứa mảng 1024 × 768 điểm ảnh "
        "màu. Với mật độ 16,8 điểm ảnh/cm (bước điểm ảnh 0,59 mm), đây là màn hình plasma màu có "
        "độ phân giải cao nhất được chế tạo cho đến nay. Thiết bị có 64 mức xám cho mỗi kênh màu "
        "và độ chói trung bình vùng trắng lớn hơn 10³ cd/m² (30 fL)."))
    b.append(fig(4))

    b.append(h3("Điểm ảnh plasma một chiều và xoay chiều", "dc and ac Plasma Pixels"))
    b.append(p(
        "Như đã nêu, điểm ảnh màn hình plasma có thể được thiết kế để làm việc một chiều hoặc "
        "xoay chiều. Hình 93.5 là sơ đồ của hai thiết kế đơn giản nhất. Trong cả hai trường hợp, "
        "các bộ dây dẫn song song được lắng lên tấm nền thuỷ tinh. Phần lớn các nhà sản xuất giữ "
        "giá thành thấp bằng cách dùng thuỷ tinh nổi soda-lime thông thường. Hai tấm thuỷ tinh "
        "được gắn cách nhau khoảng 100 µm, với hai bộ dây dẫn vuông góc nhau. Khoảng trống giữa "
        "hai tấm chứa khí trơ; khí này phóng điện và làm sáng điểm ảnh khi đặt đủ điện áp giữa "
        "hai dây dẫn giao nhau."))
    b.append(fig(5))
    b.append(p(
        "Với điểm ảnh một chiều (Hình 93.5a), khí làm việc tiếp xúc trực tiếp với điện cực. Các "
        "điện tử sinh ra trong thể tích phóng điện chảy nhanh về anode, còn các ion sinh ra chảy "
        "chậm hơn về cathode. Ở 53,3 kPa (400 Torr), khe khí 100 µm và điện áp đặt 200 V, thời "
        "gian bay của điện tử và ion qua khe tương ứng khoảng 0,2 ns và 20 ns. Khi đã khởi phát "
        "đánh thủng, điện trở của phóng điện không đáng kể. Vì vậy, chế độ một chiều buộc phải "
        "mắc thêm điện trở nối tiếp với từng điểm ảnh để hạn chế biên độ dòng. Điểm ảnh một chiều "
        "thường được vận hành ở chế độ phóng điện xung, dùng điều chế tần số để xác định độ chói. "
        "Với cả hai kiểu, tần số phát cơ bản điển hình là 50 kHz — mắt người không kịp thấy nhấp "
        "nháy bật–tắt ở tần số này, nhưng vẫn đủ dư địa để điều khiển cường độ và làm tươi. Khi "
        "đọc tài liệu về màn hình plasma, rất dễ lẫn điểm ảnh một chiều với xoay chiều, vì điểm "
        "ảnh một chiều cũng thường được chạy ở chế độ xung và có đảo cực điện cực để chia đều "
        "tổn thương do phún xạ cho cả hai mặt điện cực. Dấu hiệu nhận biết điểm ảnh một chiều là "
        "điện cực dẫn tiếp xúc trực tiếp với khí phóng điện và có điện trở hạn dòng trong mạch "
        "của từng điểm ảnh. Đảo cực là tuỳ chọn với điểm ảnh một chiều, nhưng lại bắt buộc với "
        "điểm ảnh xoay chiều như sẽ trình bày dưới đây. Mạch điều khiển, hạn dòng, thang xám và "
        "các khía cạnh khác của cả hai kiểu được bàn kỹ ở các mục sau."))
    b.append(p(
        "Hình 93.5b là sơ đồ cấu hình điểm ảnh plasma xoay chiều. Có thể thấy khác biệt về hình "
        "học giữa hai kiểu là nhỏ, nhưng khác biệt về vận hành thì lớn. Ở điểm ảnh xoay chiều, "
        "các dây dẫn được phủ một lớp màng điện môi. Thường dùng chì oxit (PbO) có hằng số điện "
        "môi khoảng 15, lắng thành màng dày khoảng 25 µm. Phần lớn điểm ảnh xoay chiều còn có "
        "thêm lớp màng mỏng magie oxit (MgO) dày 50–200 nm phủ lên PbO và tiếp xúc với khí làm "
        "việc. Màng điện môi hai lớp này đảm nhận hai chức năng chính: tích điện và phát xạ điện "
        "tử thứ cấp."))
    b.append(p(
        "Điện áp chính xác cần để đánh thủng khí phụ thuộc vào độ rộng khe, áp suất khí, thành "
        "phần khí và trạng thái bề mặt MgO. Với các thông số điểm ảnh trên Hình 93.5b, cần điện "
        "áp đặt ngoài khoảng 120–180 V để khởi phát phóng điện. Ở điểm ảnh xoay chiều, khi phóng "
        "điện đã khởi phát, điện tử và ion cũng chảy về anode và cathode như ở điểm ảnh một "
        "chiều. Nhưng trong trường hợp xoay chiều, hạt tải không thể tới được dây dẫn mà tích lại "
        "thành điện tích bề mặt trên lớp phủ điện môi. Điện trường trong khe khí luôn là tổng của "
        "điện trường do điện áp đặt ngoài và điện trường do điện tích bề mặt. Trong lúc điểm ảnh "
        "phóng điện, nếu điện áp đặt ngoài chỉ được giữ không đổi trong vài micro giây, điện "
        "trường tổng trong khe khí giảm rất nhanh (khoảng 100–200 ns). Độ giảm thế do điện tích "
        "bề mặt tạo ra sẽ che chắn phần thế do điện áp ngoài tạo ra. Cuối cùng, điện trường trong "
        "khe không đủ duy trì phóng điện và điểm ảnh tắt. Như vậy mỗi điểm ảnh xoay chiều tự hạn "
        "chế dòng và, khác với điểm ảnh một chiều, không cần điện trở ngoài nối tiếp. Vào đầu nửa "
        "chu kỳ xoay chiều tiếp theo, điện áp đặt ngoài đảo dấu. Khi đó điện áp trên khe khí là "
        "tổng của điện áp ngoài và điện áp do điện tích bề mặt tích được trong lần phóng điện "
        "trước. Nếu lượng điện tích bề mặt đủ lớn, một xung phóng điện mới có thể được khởi phát "
        "chỉ bằng điện áp ngoài mà tự nó không đủ đánh thủng khí. Trong phóng điện mới, hạt tải "
        "chảy nhanh để đảo dấu mật độ điện tích bề mặt. Một lần nữa, điện trường trong khe giảm "
        "và phóng điện tắt. Việc tích điện bề mặt khiến điểm ảnh xoay chiều dễ điều khiển và đem "
        "lại cho nó tính nhớ cố hữu. Sự có mặt hay vắng mặt của điện tích bề mặt quyết định điểm "
        "ảnh có phóng điện hay không ở đầu nửa chu kỳ xoay chiều kế tiếp. Chi tiết cách dùng các "
        "động học phóng điện này để ghi, xoá và duy trì từng điểm ảnh được bàn ở các mục sau, "
        "cùng với cơ chế điều khiển thang xám và làm tươi mảng điểm ảnh."))

    b.append(h3("Các thuộc tính chung của màn hình plasma",
                "General Attributes of Plasma Displays"))
    b.append(p(
        "Màn hình phẳng phóng điện plasma có nhiều ưu điểm so với các công nghệ hiển thị cạnh "
        "tranh. Tính phi tuyến mạnh của đặc tính điện ở mỗi điểm ảnh, cùng tính nhớ cố hữu, có "
        "thể được tận dụng khi thiết kế mạch điều khiển làm tươi và cập nhật mảng điểm ảnh. Cấu "
        "trúc điểm ảnh giản dị khiến các bài toán chế tạo diện tích lớn — như căn thẳng và độ "
        "đồng đều chiều dày màng — bớt khó khăn hơn. So với màn hình tinh thể lỏng ma trận chủ "
        "động màu (AMLCD) vốn dùng transistor màng mỏng (TFT) để điều khiển từng điểm ảnh, chế "
        "tạo ít phức tạp hơn và mạch điều khiển ít phức tạp hơn cho màn hình phẳng plasma lợi thế "
        "trong các ứng dụng diện tích lớn. Ngược lại, màn hình plasma cần mạch điều khiển chắc "
        "chắn hơn với điện áp 100–275 V. Màn hình plasma cũng không phù hợp cho thiết bị xách tay "
        "vì công suất tiêu thụ cao so với các công nghệ khác — tuy không đến mức hạn chế việc "
        "dùng trong văn phòng hay gia đình. Màn hình màu đường chéo 76 cm (30 in.) của Photonics "
        "Imaging trên Hình 93.4 chỉ tiêu thụ đỉnh 300 W [23]. Ở mức công suất cao, màn hình "
        "phẳng plasma đủ sáng để đọc dưới ánh nắng. Màn hình cũng dễ dàng thích ứng điều kiện "
        "ánh sáng yếu bằng cách điều chế biên độ hay tần số phóng điện."))
    b.append(p(
        "Màn hình phẳng plasma rất phù hợp cho các ứng dụng diện tích lớn (0,5–5 m) như hội nghị "
        "truyền hình, màn hình phòng họp lớn, màn hình ngoài trời và mô phỏng cần vùng nhìn rộng. "
        "Màn hình plasma màu mỏng, độ phân giải cao, diện tích lớn cũng rất hấp dẫn cho máy trạm "
        "để bàn hay máy tính cá nhân cần đồ hoạ phân giải cao. Cũng cần lưu ý rằng màn hình "
        "phẳng plasma có góc nhìn rất rộng, nhiều thiết kế vượt 160° [22–24]. Với màn hình dùng "
        "điện cực kim loại, người ta thường thấy góc nhìn tốt nhất hơi lệch khỏi pháp tuyến, vì "
        "dây điện cực phía trước che một phần phát xạ của điểm ảnh. Điều này xảy ra cả với điểm "
        "ảnh đơn sắc phát xạ nhìn thấy ngay trong thể tích phóng điện, lẫn với màn hình plasma "
        "màu nơi người xem nhận phát xạ đỏ, lục, lam (RGB) từ phosphor được kích thích bằng "
        "photon tử ngoại chân không (VUV). Một số nhà sản xuất đã thử dùng điện cực trong suốt "
        "như indi thiếc oxit (ITO), nhưng phải đánh đổi công suất tiêu thụ vì độ dẫn của ITO "
        "kém hơn điện cực kim loại [18]. Trong các thiết kế hiện nay, bề rộng dây dẫn kim loại "
        "nhỏ (khoảng 20 µm) nên độ mờ của nó không phải vấn đề lớn."))
    b.append(p(
        "Với điểm ảnh màu, hỗn hợp khí phóng điện được điều chỉnh để phát xạ trong vùng VUV. Về "
        "mọi phương diện khác, nguyên lý vận hành phóng điện plasma ở điểm ảnh là như nhau với "
        "màn hình màu và đơn sắc. Lý tưởng nhất, ở màn hình plasma màu không có phát xạ nhìn thấy "
        "nào sinh ra ngay trong phóng điện, mà dùng phosphor phát quang được kích thích bằng VUV "
        "để tạo ánh sáng RGB cần thiết. Thiết kế điểm ảnh màu xoay chiều trên Hình 93.6 là kiểu "
        "Fujitsu đang dùng [18]. Các vách ngăn thẳng, dài, cao khoảng 100 µm, được tạo song song "
        "và nằm giữa các dây dẫn hướng thẳng đứng trên tấm nền phía sau. Thành bên của các vách "
        "này lần lượt được phủ phosphor đỏ, lục, lam. Cần lưu ý rằng tấm của Fujitsu dùng thiết "
        "kế điểm ảnh phóng điện bề mặt ba điện cực, điều khiển xoay chiều — phức tạp hơn một chút "
        "so với kiểu điện cực đối diện trên Hình 93.5b. Chương này sẽ trở lại cấu hình phóng điện "
        "bề mặt và các khía cạnh khác của thiết kế, vận hành điểm ảnh màu sau khi đã điểm qua vật "
        "lý phóng điện và ứng xử điện chi phối hoạt động của điểm ảnh."))
    b.append(fig(6))

    # ------------------------------------------------------------ 93.2
    b.append(h2("93.2 Cơ sở hoạt động của điểm ảnh plasma", "Fundamentals of Plasma Pixel Operation"))
    b.append(h3("Các quá trình vật lý nguyên tử", "Atomic Physics Processes"))
    b.append(p(
        "Tuy thiết kế giản dị, điểm ảnh màn hình plasma là một môi trường phong phú để nghiên cứu "
        "vật lý nguyên tử cơ bản, các quá trình va chạm điện tử, sinh và vận chuyển photon, và "
        "tương tác plasma–bề mặt. Sự ghép nối các quá trình này trong một phóng điện điểm ảnh "
        "đơn sắc neon–argon đã được Weber tóm tắt rất gọn trong sơ đồ được in lại ở Hình 93.7 "
        "[4]. Bạn đọc muốn tìm hiểu thêm về vật lý phóng điện cơ bản nên tham khảo một trong "
        "những giáo trình tốt trong lĩnh vực này [25–27]."))
    b.append(fig(7))
    b.append(p(
        "Các quá trình vật lý chi phối hoạt động của phóng điện điểm ảnh gắn bó chặt với nhau và "
        "tạo thành một hệ kín. Phần thảo luận bắt đầu bằng giả thiết có một điện tử mồi nằm trong "
        "khe khí và chịu tác dụng của điện trường sinh ra khi đặt điện áp ngoài lên hai dây dẫn "
        "tạo nên điểm ảnh đó. Một số quá trình trong khí và trên bề mặt sinh ra điện tử mồi sẽ "
        "dần hiện ra trong quá trình thảo luận. Để bảo đảm khởi phát phóng điện tin cậy, các hạt "
        "mồi — điện tử, photon sinh điện tử, hoặc nguyên tử metastable — thường được cung cấp từ "
        "một nguồn có điều khiển, có thể nằm ngoài điểm ảnh đang phóng điện. Một số tấm hiển thị "
        "có điện cực sinh hạt mồi ở mép tấm, ngoài vùng nhìn, hoặc giấu sau các dây dẫn mờ. Các "
        "tấm khác dùng trình tự thời gian được kiểm soát chặt để các điểm ảnh lân cận cung cấp "
        "hạt mồi cho nhau [4,19,28]. Trình tự địa chỉ điểm ảnh sẽ được bàn tiếp ở phần sau của "
        "chương."))
    b.append(p(
        "Sự vận chuyển điện tử hay ion qua khe khí là cân bằng giữa gia tốc bởi điện trường và "
        "mất mát năng lượng do va chạm. Trong ví dụ ở Hình 93.7, khí chủ yếu là neon (98–99,9 %) "
        "nên điện tử được gia tốc chủ yếu va chạm với nguyên tử Ne. Giản đồ mức năng lượng lượng "
        "tử để kích thích nguyên tử Ne được vẽ ở Hình 93.7 [29]. Mức kích thích thấp nhất nằm "
        "16,6 eV trên mức cơ bản, còn năng lượng ion hoá là 21,6 eV. Nghĩa là điện tử có năng "
        "lượng dưới 16,6 eV chỉ có thể va chạm đàn hồi với nguyên tử Ne. Khi điện tử được điện "
        "trường gia tốc tới năng lượng vượt 16,6 eV, có thể xảy ra va chạm không đàn hồi, truyền "
        "năng lượng từ điện tử tới tới một trong các điện tử lớp ngoài của nguyên tử Ne. Điện tử "
        "tới có động năng vượt 21,6 eV có thể gây phản ứng ion hoá:"))
    b.append(eq(_eq("93.1"), "93.1"))
    b.append(p(
        "Va chạm kích thích và ion hoá truyền năng lượng từ tập hợp điện tử sang các nguyên tử "
        "trung hoà trong khí. Đồng thời, số điện tử có khả năng ion hoá Ne tiếp tục tăng lên sau "
        "mỗi sự kiện ion hoá. Kết quả là thác phóng điện như vẽ ở Hình 93.7, mà trên thực nghiệm "
        "biểu hiện thành sự tăng nhanh dòng điện chạy trong khe khí của điểm ảnh. Ở tấm một "
        "chiều, một điện trở ngoài khoảng <i>R</i> = 500 kΩ được mắc nối tiếp với mỗi điểm ảnh. "
        "Biên độ điện áp do mạch điều khiển cấp, <i>V</i><sub>a</sub>, được giữ không đổi, nên "
        "tổng điện áp trên khe khí <i>V</i><sub>g</sub> = <i>V</i><sub>a</sub> − <i>IR</i> giảm "
        "khi dòng mạch <i>I</i> tăng. Rất nhanh sau đó, một dòng một chiều ổn định trong khe khí "
        "và trong mạch được thiết lập. Độ chói và thang xám được điều khiển bằng điều chế tần số "
        "của các xung phóng điện một chiều, với tần số cơ bản khoảng 50 kHz. Ở phóng điện điểm "
        "ảnh xoay chiều, điện tử và ion được điện trường đưa về anode và cathode đã phủ điện môi. "
        "Sự tích điện trên bề mặt điện môi che chắn vùng khe khỏi điện trường do điện áp ngoài "
        "tạo ra. Cuối cùng điện trường trong khe giảm xuống dưới mức đủ duy trì phóng điện và "
        "điểm ảnh tắt."))
    b.append(p(
        "Với điện tử có năng lượng lớn hơn 16,6 eV, va chạm với nguyên tử Ne có thể kích thích "
        "các điện tử lớp ngoài lên một trong nhiều trạng thái kích thích trên Hình 93.7."))
    b.append(eq(_eq("93.2a"), "93.2a"))
    b.append(eq(_eq("93.2b"), "93.2b"))
    b.append(p(
        "Phần lớn các trạng thái kích thích này có thời gian sống ngắn, từ một phần đến vài chục "
        "nanogiây [30], và nhanh chóng rã về các trạng thái lượng tử thấp hơn, kèm phát xạ một "
        "photon đặc trưng, ký hiệu <i>h</i>ν trong phương trình 93.2 — tích của hằng số Planck "
        "với tần số photon. Như thấy trên Hình 93.8, phát xạ đỏ cam đặc trưng của khí Ne sinh ra "
        "từ các chuyển mức của điện tử trong nguyên tử, từ trạng thái lượng tử 2p năng lượng cao "
        "xuống mức 1s thấp hơn [30,31]. Hai trong bốn mức 1s phát xạ về mức cơ bản, cho photon "
        "VUV có bước sóng 74,4 và 73,6 nm. Do nguyên lý loại trừ của cơ học lượng tử, sự rã của "
        "điện tử từ hai mức 1s còn lại phức tạp hơn, phụ thuộc chi tiết hàm sóng điện tử và những "
        "tương tác nhiễu loạn rất nhỏ [31]. Vì vậy thời gian sống của các trạng thái gọi là "
        "metastable này được đo bằng giây — rất dài so với các quá trình động học khác chi phối "
        "phóng điện điểm ảnh như vận chuyển điện tích hay hạt trung hoà. Một nguyên tử Ne có điện "
        "tử bị giữ ở một trong các mức metastable mang theo 16,6 eV năng lượng ẩn. Nguyên tử "
        "metastable, Ne*, không thể tiêu tán năng lượng dự trữ khi va chạm với nguyên tử Ne ở "
        "mức cơ bản, nhưng lại dễ dàng giải phóng năng lượng mỗi khi có cấu hình năng lượng thấp "
        "hơn để chuyển sang. Hai kênh chính trong hệ này là va chạm của Ne* với Ar, và Ne* đập "
        "vào bề mặt bên trong điểm ảnh."))
    b.append(fig(8))
    b.append(p(
        "Hình 93.8 vẽ giản đồ mức năng lượng rút gọn của một số khí trơ. Vị trí tương đối của "
        "các mức cho phép cho thấy cách năng lượng được trao đổi trong ghép nối va chạm. Năng "
        "lượng ion hoá của nguyên tử Ar là 15,8 eV, thấp hơn trạng thái metastable Ne* 0,8 eV. "
        "Vì vậy Ne* có đủ năng lượng dự trữ để ion hoá nguyên tử Ar:"))
    b.append(eq(_eq("93.3"), "93.3"))
    b.append(p(
        "Phản ứng ion hoá kiểu này gọi là phản ứng Penning, và hỗn hợp khí dựa vào trạng thái "
        "metastable của thành phần đa số (Ne) để ion hoá thành phần thiểu số (Ar) được gọi là "
        "hỗn hợp khí Penning [25,26,32]. Hình 93.9 cho thấy hiệu quả tạo cặp điện tích trong "
        "phóng điện của khí Penning Ne/Ar với các tỉ lệ Ar khác nhau. Các đường cong cho thấy "
        "với mọi áp suất, số cặp ion tạo được trên mỗi vôn đặt vào là tối ưu ở tỉ lệ Ar thấp "
        "(0–10 %), trừ trường hợp <i>E</i>/<i>P</i> rất lớn — trên 75 V/m/Pa (100 V/cm/Torr) — "
        "với <i>E</i> là cường độ điện trường và <i>P</i> là áp suất khí. Hỗn hợp khí Penning đã "
        "được nghiên cứu từ nhiều năm. Hình 93.9 là dữ liệu gốc về đánh thủng khí Ne/Ar do "
        "Kruithof và Penning công bố năm 1937 [32]. Từ đó đến nay đã có rất nhiều tài liệu về "
        "quá trình Penning trong khí trơ; bạn đọc quan tâm có thể tìm ở các giáo trình tốt vừa "
        "được American Vacuum Society và MIT Press tái bản [25,26]."))
    b.append(fig(9))
    b.append(p(
        "Điểm ảnh màn hình plasma thường làm việc ở áp suất gần 53,3 kPa (400 Torr) để có đủ "
        "lượng photon và độ chói. Điện trường điển hình trong điểm ảnh khoảng 100 MV/m. Do đó "
        "điểm ảnh plasma làm việc với <i>E</i>/<i>P</i> gần 18,8 V/m/Pa (25 V/cm/Torr). Khi đó "
        "cả việc tạo cặp điện tích lẫn hiệu suất phát sáng đều tối ưu với tỉ lệ Ar trong khoảng "
        "0,1–10 %, tuỳ áp suất khí, độ rộng khe và điện áp điều khiển của điểm ảnh. Với một điện "
        "áp đặt cho trước, tích của áp suất khí (<i>P</i>) và kích thước khe khí (<i>d</i>) là "
        "thước đo cân bằng giữa gia tốc điện tử bởi điện trường và mất mát năng lượng do va chạm "
        "với khí nền. Đường cong Paschen — điện áp đánh thủng khí theo tích <i>Pd</i> — cho một "
        "số hỗn hợp khí trơ được vẽ ở Hình 93.10 [26,33,45]. Trong mỗi trường hợp, điện áp đánh "
        "thủng cực tiểu xảy ra ở một giá trị <i>Pd</i> phụ thuộc mức ion hoá, độ va chạm và các "
        "kênh năng lượng trong khí. Ví dụ, ở Ne các quá trình kích thích và ion hoá chiếm ưu "
        "thế, còn trong không khí phần lớn năng lượng khí hấp thụ đi vào dao động, quay và phân "
        "ly phân tử — những quá trình không ion hoá."))
    b.append(fig(10))
    b.append(p(
        "Với áp suất cố định, đường cong Paschen cho thấy khe càng rộng thì cường độ điện trường "
        "trên mỗi vôn đặt vào càng nhỏ và cần điện áp lớn mới đánh thủng. Ngược lại, nếu giảm "
        "<i>d</i> ở áp suất cho trước, cường độ điện trường có thể lớn, nhưng điện tử bay qua khe "
        "mà không gây đủ số va chạm để tạo thác phóng điện như ở Hình 93.7. Nếu giữ <i>d</i> cố "
        "định và thay đổi áp suất, dạng đường cong Paschen cũng được giải thích bằng gia tốc điện "
        "tử và các quá trình va chạm. Ở áp suất cao, quãng đường tự do trung bình giữa hai va chạm "
        "ngắn, điện tử không kịp tăng tốc tới năng lượng đủ gây ion hoá trừ khi điện trường đặc "
        "biệt mạnh. Ở áp suất thấp, điện tử có thể được gia tốc tới năng lượng đủ gây ion hoá "
        "nhưng ít va chạm với khí nền, nên thác cũng khó khởi phát. Quá trình Penning đặc biệt "
        "hiệu quả trong việc gây ion hoá. Đưa 0,1 % Ar vào khí neon hạ điện áp đánh thủng cực "
        "tiểu từ khoảng 250 V trên Hình 93.10 xuống còn khoảng 150 V. Với hỗn hợp này, cực tiểu "
        "xảy ra ở tích <i>Pd</i> bằng 40 Pa·m (30 Torr·cm)."))

    b.append(h3("Vật lý phóng điện của điểm ảnh plasma",
                "Discharge Physics for Plasma Pixels"))
    b.append(p(
        "Trong bất kỳ phóng điện nào, điện tử chuyển động rất nhanh trong khi các ion nặng hơn "
        "chuyển động chậm hơn nhiều. Trong một plasma trung hoà về điện chịu điện trường ngoài, "
        "các điện tử linh động phản ứng nhanh với điện trường và lao về anode. Các ion ì ạch hơn "
        "bắt đầu chuyển động về cathode theo cách chậm hơn nhiều. Rất nhanh sau đó, một mất cân "
        "bằng điện tích cục bộ được thiết lập vì điện tử tới anode nhanh hơn tốc độ ion tới "
        "cathode. Phương trình Poisson"))
    b.append(eq(_eq("93.4"), "93.4"))
    b.append(p(
        "cho thấy một điện trường cục bộ được thiết lập để đáp lại mật độ điện tích dương thực "
        "ρ(<i>x</i>) trong vùng plasma. Ở đây <i>n</i><sub>i</sub>(<i>x</i>) và "
        "<i>n</i><sub>e</sub>(<i>x</i>) là prôfin không gian của mật độ ion và điện tử, còn "
        "<i>e</i> là điện tích điện tử. Điện trường được thiết lập làm chậm tốc độ điện tử thoát "
        "ra khỏi một thể tích bất kỳ trong cột plasma và buộc chúng đi theo chuyển động tổng hợp "
        "của ion. Chuyển động trôi của ion cũng được gia tốc tương ứng, nhưng mức gia tốc này "
        "nhỏ hơn theo một hệ số tỉ lệ với tỉ số khối lượng giữa điện tử và ion. Chuyển động tổng "
        "hợp của ion và điện tử gọi là dòng lưỡng cực (ambipolar), được trình bày chi tiết trong "
        "nhiều giáo trình vật lý plasma cơ bản [25–27]."))
    b.append(p(
        "Trong phóng điện điểm ảnh plasma một chiều ở trạng thái ổn định, biên độ dòng chạy "
        "trong mạch và trong khe khí được xác định bởi điện áp đặt và điện trở nối tiếp với "
        "điểm ảnh. Vận hành ổn định đòi hỏi không thể có tích điện trong vùng khe. Tốc độ các "
        "cặp hạt tải tới điện cực phải bằng tốc độ sinh ra chúng do ion hoá. Đồng thời, tốc độ "
        "ion và điện tử rời thể tích plasma — tới cathode và anode — phải bằng nhau. Cân bằng "
        "được duy trì nhờ prôfin thế không gian trong khe khí như trên Hình 93.11a. Nhờ độ linh "
        "động điện tử cao, plasma che chắn điện trường ngoài cực kỳ hiệu quả. Kết quả là prôfin "
        "thế phẳng trên suốt khe khí của một điểm ảnh đang duy trì phóng điện phát triển đầy đủ. "
        "Toàn bộ độ giảm thế tập trung trong một vùng nhỏ gọi là lớp vỏ (sheath) sát mỗi điện "
        "cực. Phạm vi không gian của lớp vỏ được quyết định bởi hiệu quả che chắn điện trường "
        "của tập hợp điện tử. Độ dài Debye,"))
    b.append(eq(_eq("93.5"), "93.5"))
    b.append(p(
        "cho thước đo khoảng cách che chắn. Biểu thức của λ<sub>D</sub> cho thấy bề dày lớp vỏ "
        "tăng khi nhiệt độ điện tử <i>T</i><sub>e</sub> tăng và giảm khi mật độ điện tử "
        "<i>n</i><sub>e</sub> tăng. Với phóng điện điểm ảnh phát triển đầy đủ, tích của hằng số "
        "Boltzmann với nhiệt độ điện tử <i>kT</i><sub>e</sub> nhiều nhất chỉ vài electron vôn, "
        "còn <i>n</i><sub>e</sub> cỡ 10<sup>16</sup>/m³. Vì vậy bề dày lớp vỏ vào khoảng 5 µm. "
        "Thế trong vùng plasma, <i>V</i><sub>P</sub>, tăng tới giá trị chỉ cao hơn điện áp đặt "
        "một chút ở anode. Do đó chỉ những điện tử năng lượng nhất mới vượt được hàng rào thế ở "
        "anode, và thế này tự điều chỉnh sao cho tốc độ mất điện tử ở anode bằng tốc độ mất ion "
        "ở cathode. Với điểm ảnh plasma xoay chiều, prôfin thế tương tự cũng được thiết lập "
        "nhưng thay đổi động theo diễn biến xung điểm ảnh. Các cặp điện tích đập vào anode và "
        "cathode trong điểm ảnh xoay chiều bị giữ lại ở đó bởi lớp điện môi phủ dây dẫn. Vì vậy "
        "thế ở biên phóng điện giảm dần khi điện tích bề mặt tích tụ ở mỗi điện cực, như trên "
        "Hình 93.11b. Cuối cùng phóng điện kết thúc khi điện trường do điện tích bề mặt triệt "
        "tiêu điện trường do điện áp ngoài. Khi mật độ hạt tải giảm gần lúc kết thúc xung phóng "
        "điện xoay chiều, hiệu quả che chắn điện trường của điện tử trong khe cũng giảm. Trong "
        "tình huống đó, độ giảm thế trên lớp vỏ nhỏ nhưng vùng vỏ lại chiếm phần lớn khe [36,37]."))
    b.append(fig(11))

    b.append(h3("Tương tác plasma – bề mặt", "Plasma Surface Interactions"))
    b.append(p("<b>Phát xạ điện tử thứ cấp do ion</b>"))
    b.append(p(
        "Các ion tới lớp vỏ cathode được gia tốc bởi độ giảm thế trên lớp vỏ. Ion tới đập vào "
        "cathode với động năng bằng thế plasma <i>V</i><sub>p</sub>, trong ví dụ ở Hình 93.12a "
        "là hơn 200 V một chút. Ion tới cathode nhanh chóng bắt một điện tử, đồng thời để lại "
        "trên mặt cathode một năng lượng bằng năng lượng tái hợp hay năng lượng ion hoá của "
        "nguyên tử đó. Việc bồi tụ năng lượng trên mặt cathode thúc đẩy hai quá trình quan trọng "
        "với điểm ảnh plasma: phát xạ điện tử thứ cấp do ion và phún xạ. Quá trình thứ nhất làm "
        "tăng đáng kể hiệu suất phát sáng của điểm ảnh plasma. Quá trình thứ hai rút ngắn tuổi "
        "thọ vận hành, như bàn ở các mục sau."))
    b.append(p(
        "Phát xạ điện tử thứ cấp do ion xảy ra khi năng lượng ion truyền cho bề mặt làm bật ra "
        "điện tử. Điện tử thứ cấp đặc biệt hiệu quả trong việc gây ion hoá phóng điện, vì chúng "
        "nhận được lượng lớn động năng khi được gia tốc qua lớp vỏ cathode và vì chúng có nhiều "
        "cơ hội va chạm ion hoá khi bay qua toàn bộ chiều rộng khe khí. Hệ số phát xạ điện tử "
        "thứ cấp γ được định nghĩa là số điện tử bật ra trên mỗi ion tới [25,26]. Như có thể dự "
        "đoán, γ thay đổi theo năng lượng ion tới và theo vật liệu cathode. Phần lớn tấm hiển thị "
        "plasma xoay chiều tận dụng khả năng phát xạ điện tử thứ cấp mạnh của MgO — vật liệu này "
        "cũng là chất cách điện tốt, đúng yêu cầu để tích điện bề mặt trong chế độ xoay chiều. "
        "Việc đo γ của MgO rất khó, nhất là với ion năng lượng thấp (dưới 500 eV), và còn phức "
        "tạp thêm vì mẫu bị tích điện trong lúc đo [38]. Thông thường người ta suy ra giá trị "
        "tương đối của hiệu suất điện tử thứ cấp cho các vật liệu khác nhau từ phép đo cường độ "
        "phóng điện [11,12,39–42]. Chou đã đo trực tiếp hệ số phát xạ điện tử thứ cấp do ion của "
        "MgO, dùng chùm ion dạng xung và trung hoà bề mặt mẫu giữa các xung. Với ion tới 200 eV, "
        "ông thu được γ = 0,45 cho Ne<sup>+</sup> và γ = 0,05 cho Ar<sup>+</sup> [39]. Cũng cần "
        "lưu ý rằng photon và nguyên tử metastable đập vào bề mặt điện cực cũng có thể khởi phát "
        "phát xạ điện tử thứ cấp, như trên Hình 93.7. Vì photon và metastable không chịu tác dụng "
        "của điện trường trong khe khí, chúng lan truyền đẳng hướng trong toàn thể tích khí và "
        "thường được dùng làm hạt mồi."))
    b.append(fig(12))
    b.append(p("<b>Phún xạ</b>"))
    b.append(p(
        "Ion được gia tốc qua lớp vỏ bồi năng lượng lên mặt cathode. Điều này thường khởi phát "
        "phún xạ: một nguyên tử trong vật liệu cathode bị bật khỏi bề mặt. Quá trình phún xạ bào "
        "mòn mặt cathode và làm suy giảm hiệu năng điểm ảnh. Tạp chất từ bề mặt bị phún xạ nhiễm "
        "vào phóng điện có thể làm giảm hiệu suất phát sáng, vì nguyên tử hay phân tử tạp phát xạ "
        "ánh sáng nhìn thấy và làm hỏng độ tinh khiết màu của điểm ảnh. Các lớp phủ ngoài ý muốn "
        "do vật liệu lắng lại cũng có thể làm hỏng đặc tính điện của điểm ảnh, hoặc trong ứng "
        "dụng màu thì che phosphor khỏi photon VUV, càng làm giảm hiệu suất phát sáng. Với chùm "
        "ion argon Ar<sup>+</sup> 2 keV bắn phá mặt MgO, hiệu suất phún xạ đo được hơi lớn hơn "
        "một nguyên tử bật ra trên mỗi ion tới [43]. Dữ liệu về hiệu suất phún xạ với ion năng "
        "lượng thấp rất khó thu. Vì hiệu suất nhỏ nên cần dòng ion tới lớn mới có tín hiệu đo "
        "được, và mẫu lại bị tích điện. Dù thiếu dữ liệu chi tiết về phún xạ MgO năng lượng "
        "thấp, các nhà sản xuất tấm plasma xoay chiều vẫn đạt được tuổi thọ màn hình vượt xa "
        "10.000 h [18,23]. Shone và cộng sự [44] đã chứng minh có thể dùng tán xạ ngược "
        "Rutherford của hạt alpha năng lượng cao (2,8 MeV) để đo chiều dày màng MgO trên nền "
        "PbO, với độ chính xác ±1,5 nm. Vì kỹ thuật này cần một máy gia tốc hạt lớn (và đắt), nó "
        "là công cụ nghiên cứu rất tốt nhưng không phù hợp cho đo trên dây chuyền sản xuất."))

    # ------------------------------------------------------------ 93.3
    b.append(h2("93.3 Tính chất điện của điểm ảnh", "Pixel Electrical Properties"))
    b.append(h3("Tính chất điện của điểm ảnh một chiều", "Electrical Properties of dc Pixels"))
    b.append(p(
        "Hình 93.5 cho sơ đồ và mô hình mạch của điểm ảnh một chiều và xoay chiều. Với trường hợp "
        "một chiều, khe khí của điểm ảnh có chức năng điện như một điện trở có trở kháng thay "
        "đổi. Trước khi đánh thủng khí, điện trở lớn và điểm ảnh là một phần tử hở mạch. Khi "
        "đánh thủng đã khởi phát, plasma là vật dẫn rất tốt và chỉ có điện trở nhỏ "
        "<i>R</i><sub>P</sub> đối với dòng. Vì <i>R</i> ≫ <i>R</i><sub>P</sub>, phương trình mạch "
        "rút gọn thành"))
    b.append(eq(_eq("93.6"), "93.6"))
    b.append(p(
        "và dòng mạch <i>I</i> được xác định bởi biên độ điện áp đặt và trị số điện trở nối tiếp "
        "<i>R</i>. Điện áp đặt ngoài <i>V</i><sub>a</sub> thường là xung vuông 50 kHz với sườn "
        "lên nhanh (khoảng 50 ns). Điện áp điều khiển một chiều nằm trong khoảng 175–275 V và "
        "giá trị điển hình của điện trở nối tiếp là <i>R</i> = 500 kΩ. Khi đó dòng điểm ảnh nằm "
        "trong khoảng 0,35–0,55 mA. Cần lưu ý rằng nếu không có điện trở lớn nối tiếp, dòng sẽ "
        "bị giới hạn bởi một hư hỏng vật lý nào đó, ví dụ nóng chảy điện cực điểm ảnh."))
    b.append(p(
        "Hình 93.12 cho đặc tuyến dòng–áp của một điểm ảnh một chiều có điện áp đánh thủng 250 V "
        "[4]. Khi điện áp tăng từ 0 đến 250 V, chỉ có dòng rất nhỏ do vài hạt tải lang thang chạy "
        "qua khe khí, và điểm ảnh vẫn ở trạng thái tắt. Tại điện áp đánh thủng, tình huống trở "
        "nên động: dòng tăng nhanh và điện áp trên khe khí giảm theo. Điểm làm việc ổn định đạt "
        "được là giao của đường tải <i>V</i><sub>a</sub> = <i>IR</i> với đặc tuyến dòng–áp của "
        "phóng điện, như trên Hình 93.12. Với điện áp đặt 175 V, điểm ảnh luôn tắt; với "
        "<i>V</i><sub>a</sub> = 275 V, điểm ảnh luôn sáng. Với điện trở đường 500 kΩ, chế độ hai "
        "trạng thái và tính nhớ của điểm ảnh một chiều ở <i>V</i> = 225 V hiện rõ trên hình. Nếu "
        "điện áp đặt 225 V được đưa lên từ phía điện áp thấp, điểm ảnh vẫn tắt. Ngược lại, nếu "
        "đặt một điện áp lớn rồi hạ xuống <i>V</i><sub>a</sub> = 225 V, điểm ảnh sẽ ở trạng thái "
        "sáng. Cần lưu ý rằng vùng mà đường tải 225 V/500 kΩ cắt phần điện trở âm của đặc tuyến "
        "là không ổn định: phóng điện điểm ảnh sẽ nhanh chóng chuyển sang điểm làm việc sáng ổn "
        "định hoặc tắt ổn định. Trên thực tế, không thể đo được vùng điện trở âm của đặc tuyến "
        "trong mạch điểm ảnh có điện trở nối tiếp 500 kΩ. Thay vào đó, như trên hình, người ta "
        "dùng điện trở nối tiếp lớn hơn nhiều, <i>R</i> = 5 MΩ, để đường tải có độ dốc đủ nhỏ và "
        "cho phép vận hành ổn định trong vùng điện trở âm."))

    b.append(h3("Tính chất điện của điểm ảnh xoay chiều", "Electrical Properties of ac Pixels"))
    b.append(p(
        "Thiết kế vật lý của điểm ảnh xoay chiều điện cực đối diện được vẽ ở Hình 93.5b. Về điện, "
        "điểm ảnh hoạt động như một tụ điện có đánh thủng và được mô tả bằng phương trình mạch:"))
    b.append(eq(_eq("93.7"), "93.7"))
    b.append(p(
        "trong đó <i>V</i><sub>a</sub> là điện áp đặt ngoài, <i>I</i> là dòng mạch, <i>C</i> là "
        "điện dung điểm ảnh và <i>Q</i> là điện tích tích được. Với điểm ảnh xoay chiều, điện "
        "trở đường <i>R</i> được giảm tối đa để giảm công suất tiêu thụ, và phương trình 93.7 rút "
        "gọn thành"))
    b.append(eq(_eq("93.8"), "93.8"))
    b.append(p("Điện dung của mỗi điểm ảnh là tổng nối tiếp điện dung của từng lớp màng điện môi "
               "và của khe khí:"))
    b.append(eq(_eq("93.9"), "93.9"))
    b.append(p("Trong mỗi trường hợp,"))
    b.append(eq(_eq("93.10"), "93.10"))
    b.append(p(
        "với <i>i</i> là chỉ số vật liệu và diện tích bề mặt <i>A</i> xấp xỉ bằng bình phương bề "
        "rộng dây dẫn. Như trên Hình 93.5b, điểm ảnh xoay chiều thường được chế tạo với màng PbO "
        "dày <i>d</i> = 25 µm, còn màng mỏng MgO dày 50–200 nm. Chì oxit có hằng số điện môi "
        "khoảng ε<sub>PbO</sub> = 15ε<sub>0</sub>, còn MgO có ε<sub>MgO</sub> = 6ε<sub>0</sub>, "
        "giá trị chính xác phụ thuộc độ tinh khiết và vi cấu trúc của màng [45]. Cần lưu ý rằng "
        "phần đóng góp của MgO vào tổng điện dung là không đáng kể, và vật liệu này được đưa vào "
        "thiết kế chính vì khả năng phát xạ điện tử thứ cấp tuyệt vời. Trước khi đánh thủng khí, "
        "điện dung của điểm ảnh chủ yếu là điện dung của khe khí. Với dây dẫn rộng 20 µm, điện "
        "dung khe khí của một điểm ảnh trước khi đánh thủng vào khoảng 500 pF. Đạo hàm theo thời "
        "gian của phương trình 93.8 cho dòng mạch:"))
    b.append(eq(_eq("93.11"), "93.11"))
    b.append(p(
        "Dòng dịch chuyển điện tích này xuất hiện thành đỉnh dòng lớn ban đầu trên Hình 93.13 — "
        "hình vẽ đáp ứng dòng theo thời gian của mảng 45 × 45 điểm ảnh xoay chiều với một xung "
        "đơn trong chuỗi xung vuông 50 kHz. Phép đo điện trong hình dùng một đầu dò vòng cảm ứng "
        "đơn giản để đo dòng và một đầu dò điện áp trở kháng cao (1 MΩ, 3 pF) để theo dõi điện áp "
        "đặt. Tín hiệu được thu bằng dao động ký tốc độ cao (300 MHz)."))
    b.append(fig(13))
    b.append(p(
        "Nếu biên độ điện áp đặt thấp hơn ngưỡng đánh thủng khí, chỉ thấy dòng dịch chuyển nạp tụ "
        "điện xác định bởi phương trình 93.11, như trên Hình 93.13a. Nếu vượt quá điện áp đánh "
        "thủng khí, sẽ thấy thêm một xung dòng thứ hai do dòng phóng điện plasma trong khe khí, "
        "như trên Hình 93.13b. Xung plasma tất nhiên đi kèm phát xạ photon mạnh từ vùng khe khí. "
        "Tổng điện tích dịch chuyển trong xung phóng điện, theo biên độ điện áp xung vuông đặt "
        "vào, được vẽ trên Hình 93.14 cho hỗn hợp khí Penning heli–xenon (2 %) [35]. Tính trễ — "
        "tức tính nhớ cố hữu của điểm ảnh xoay chiều — hiện rõ. Khi biên độ điện áp tăng từ 0 lên "
        "180 V, không có dòng đo được nào chạy qua khe khí. Khi chưa có điện tích bề mặt, dưới "
        "180 V điện trường trong khe không đủ đưa va chạm điện tử vào chế độ thác. Với biên độ "
        "vượt 180 V, phóng điện khí được khởi phát và điểm ảnh bật. Nếu điểm ảnh chỉ nhận một "
        "xung điện áp có biên độ dưới 135 V, nó sẽ tắt kể cả khi đang có điện tích bề mặt."))
    b.append(fig(14))
    b.append(p(
        "Ở điểm ảnh xoay chiều, các cặp điện tích sinh ra trong một xung phóng điện tích lại trên "
        "bề mặt các màng điện môi ở biên khe khí và có sẵn để hỗ trợ hình thành xung phóng điện "
        "kế tiếp trong chuỗi. Trong một phóng điện điểm ảnh xoay chiều phát triển đầy đủ, lượng "
        "điện tích bề mặt tích trên màng điện môi tạo ra trong khe khí một điện trường triệt tiêu "
        "điện trường do điện áp ngoài. Điều này được thể hiện trên Hình 93.15 — một biểu diễn tổng "
        "hợp từ phép đo dòng thực nghiệm và dự đoán của mô hình tính toán về lượng điện tích bề "
        "mặt tạo nên điện áp bề mặt (điện áp thành) [34,36]. Khi điện áp đặt đảo cực, độ giảm thế "
        "do điện tích bề mặt và độ giảm thế do điện áp đặt đột nhiên cộng lại, như trên hình. Khe "
        "khí tạm thời chịu một điện trường mạnh, sinh ra từ độ giảm thế xấp xỉ hai lần điện áp "
        "đặt. Sự có mặt hay vắng mặt của điện tích bề mặt tạo nên ứng xử dòng–áp hai trạng thái "
        "như trên Hình 93.14."))
    b.append(fig(15))
    b.append(p(
        "Việc địa chỉ điểm ảnh xoay chiều được thực hiện dễ dàng nhờ tận dụng tính nhớ cố hữu của "
        "điểm ảnh, vốn có được từ ứng xử dòng–áp hai trạng thái này. Với các tính chất điện trên "
        "Hình 93.14, mỗi điểm ảnh được cấp liên tục một chuỗi xung vuông xoay chiều có biên độ "
        "160 V, gọi là điện áp duy trì <i>V</i><sub>sustain</sub>. Nếu điểm ảnh đang ở trạng thái "
        "tắt, nó sẽ tắt mãi vì không có điện tích bề mặt nào để tăng cường điện trường do điện áp "
        "duy trì tạo ra. Để bật điểm ảnh, người ta đặt qua hai điện cực một xung điện áp biên độ "
        "lớn, gọi là xung địa chỉ (hay xung ghi). Trong ví dụ này, xung địa chỉ 200 V khởi phát "
        "một phóng điện mà các cặp điện tích tích lại trên bề mặt điện môi bên trong điểm ảnh. "
        "Tính tự hạn chế của điểm ảnh xoay chiều khiến mật độ điện tích bề mặt của một phóng điện "
        "phát triển đầy đủ che chắn hoàn toàn vùng khe khỏi điện trường ngoài. Khi lần đảo cực "
        "duy trì kế tiếp xảy ra, khe khí của điểm ảnh chịu một điện áp bằng tổng điện áp duy trì "
        "(160 V) và điện áp do điện tích bề mặt của xung trước tạo ra — trong trường hợp này "
        "<i>V</i><sub>surface</sub> = 200 V. Điện áp mới trên khe là 360 V, quá đủ để khởi phát "
        "phóng điện thứ hai và thiết lập một lượng điện tích bề mặt mới có cực tính ngược với "
        "xung trước. Một lần nữa, điện tích bề mặt điều chỉnh để tạo ra điện áp triệt tiêu chính "
        "xác điện trường của điện áp đặt. Với xung này <i>V</i><sub>wall</sub> = 160 V, và lần "
        "đảo cực duy trì kế tiếp đặt lên khe một hiệu điện thế <i>V</i><sub>gap</sub> = "
        "<i>V</i><sub>sustain</sub> + <i>V</i><sub>address</sub> = 160 + 160 = 320 V, lại đủ để "
        "khởi phát một xung phóng điện mới. Vì vậy điểm ảnh duy trì trạng thái sáng cho đến khi "
        "có tác động làm mất đi hoặc giảm bớt lượng điện tích bề mặt tích theo mỗi lần phóng "
        "điện. Việc này được thực hiện bằng một xung điện áp thấp, gọi là xung xoá, có biên độ "
        "<i>V</i><sub>erase</sub> = 120 V trong ví dụ ở Hình 93.14 và 93.15. Xung xoá tạo ra độ "
        "giảm thế trên khe khí <i>V</i><sub>gap</sub> = <i>V</i><sub>applied</sub> + "
        "<i>V</i><sub>surface</sub> = 120 + 160 = 280 V. Xung xoá gây một phóng điện cường độ "
        "thấp hơn, không đủ thiết lập lại lượng điện tích bề mặt đảo cực. Vì vậy phóng điện xoá "
        "làm giảm mật độ điện tích bề mặt đến mức không có phóng điện nào được khởi phát trong "
        "xung kế tiếp của chuỗi duy trì. Lý tưởng nhất, xung xoá đưa mật độ điện tích bề mặt về "
        "đúng bằng không, nhưng điều này hiếm khi xảy ra trên thực tế và cũng không cần thiết cho "
        "vận hành điểm ảnh xoay chiều, như thấy trên Hình 93.15. Những phóng điện cường độ rất "
        "thấp, gần như không tạo photon, sẽ đưa điểm ảnh về trạng thái tắt lý tưởng trong vài chu "
        "kỳ xoay chiều. May mắn là các sai lệch nhỏ so với trạng thái tắt lý tưởng này ít ảnh "
        "hưởng đến các xung ghi về sau trong chế độ điều chế tần số, nên không ảnh hưởng đến "
        "nhịp địa chỉ và làm tươi điểm ảnh — nội dung của mục tiếp theo."))

    # ------------------------------------------------------------ 93.4
    b.append(h2("93.4 Mồi, địa chỉ, làm tươi và thang xám",
                "Display Priming, Addressing, Refresh, and Gray Scale"))
    b.append(p(
        "Việc mồi điểm ảnh là cần thiết để cung cấp nguồn điện tử ban đầu — dòng mồi — đủ để khởi "
        "phát thác phóng điện. Nguyên tử metastable hoặc photon cũng có thể dùng làm hạt mồi vì "
        "chúng sinh điện tử qua ion hoá khí nền. Mồi bằng ô mồi và tự mồi là hai phương án đang "
        "dùng trong các sản phẩm thương mại hiện nay. Trong phương án mồi bằng ô mồi, một ô riêng "
        "sinh điện tử được đặt gần điểm ảnh cần địa chỉ. Ô mồi thường nằm ở rìa màn hình, ngoài "
        "vùng nhìn, nhưng vẫn có thể cung cấp điện tử mồi khắp màn hình. Trong phương án tự mồi, "
        "một phóng điện phụ tạo ngay trong mỗi điểm ảnh cung cấp nguồn điện tử mồi cho phóng điện "
        "chính. Các phóng điện mồi này thường được giấu sau các dây dẫn mờ. Đưa một lượng rất nhỏ "
        "đồng vị phóng xạ Kr<sup>85</sup> vào hỗn hợp khí là một phương án mồi thụ động: bức xạ "
        "ion hoá từ Kr<sup>85</sup> sinh điện tử mồi đều khắp bên trong màn hình. Vì nồng độ Kr "
        "cần thiết thấp và bức xạ beta sinh ra không xuyên qua được vỏ thuỷ tinh của màn hình, "
        "nguy cơ phơi nhiễm cho người dùng là không đáng kể. Tuy vậy, việc chế tạo màn hình có "
        "gieo hạt phóng xạ kéo theo nguy cơ sức khoẻ khi xử lý vật liệu phóng xạ. Vì vậy phương "
        "án này, dù rất hiệu quả, hiện không được dùng trong sản phẩm thương mại."))
    b.append(p(
        "Một sơ đồ quét đơn giản để làm sáng điểm ảnh được vẽ trên Hình 93.2, in lại từ tài liệu "
        "4. Các chuyển mạch quét trên một trục đóng và mở lần lượt theo chu kỳ, trong khi các "
        "chuyển mạch dữ liệu trên trục kia quyết định điểm ảnh có phóng điện trong lần quét đó "
        "hay không. Cách làm tươi và cập nhật dữ liệu giản dị này không tận dụng được các tính "
        "chất phóng điện hay chức năng nhớ cố hữu của điểm ảnh plasma. Màn hình động độ phân giải "
        "cao dùng sơ đồ địa chỉ này sẽ không cạnh tranh được về giá, vì mạch điều khiển chiếm một "
        "phần đáng kể trong tổng giá thành màn hình plasma. Giá mạch điều khiển cũng tăng theo "
        "điện áp ra yêu cầu. Vì vậy cần thiết kế màn hình plasma có điện áp làm việc càng thấp "
        "càng tốt và cần ít chip điều khiển nhất. Các nhà thiết kế cố gắng tối đa hoá số điểm ảnh "
        "do một chip điều khiển."))
    b.append(p(
        "Với điểm ảnh một chiều không có tính nhớ, một cách giảm số chuyển mạch điều khiển ngoài "
        "là quét lặp đi lặp lại các phóng điện mồi theo từng hàng điểm ảnh, như trong mạch tự quét "
        "do Burroughs phát triển [46,47]. Gần đây hơn, NHK đã phát triển sơ đồ điều khiển nhớ "
        "xung cho màn hình plasma một chiều HDTV đường chéo 102 cm (40 in.) của mình, và sơ đồ "
        "này đang được dùng rộng rãi [48]. Chế độ duy trì tần số cao được dùng để tận dụng các "
        "cặp điện tích dư và nguyên tử metastable còn trong thể tích khí của điểm ảnh sau lần "
        "phóng điện trước [49]. Theo cách đó, mỗi điểm ảnh tự mồi, với lượng hạt mồi phụ thuộc "
        "thời gian trôi qua kể từ khi phóng điện trước kết thúc. Vận hành tần số cao đủ nhanh để "
        "tận dụng tính nhớ thời gian ngắn của điểm ảnh một chiều. Khi chuỗi xung duy trì được đặt "
        "lên điện cực của một điểm ảnh, điểm ảnh sẽ ở nguyên trạng thái sáng hoặc tắt cho đến khi "
        "có xung địa chỉ hay xung xoá. Trong sơ đồ NHK, một anode phụ được dùng để hỗ trợ thao tác "
        "địa chỉ. Hình 93.16a là sơ đồ khối của hệ như vậy, còn Hình 93.16b là trình tự thời "
        "gian của sơ đồ [48]. Cần lưu ý rằng các xung là một chiều và xung trạng thái sáng có "
        "điện áp khe lớn hơn xung xoá. Trình tự thời gian là yếu tố then chốt để địa chỉ chọn lọc "
        "một điểm ảnh trong ma trận. Việc thực hiện sơ đồ này cần (1) mạch điều khiển anode hiển "
        "thị, (2) mạch điều khiển anode phụ, (3) mạch điều khiển cathode, và (4) giao diện để giải "
        "mã tín hiệu HDTV cấp cho các mạch điều khiển."))
    b.append(fig(16))
    b.append(p(
        "Với màn hình xoay chiều có tính nhớ, mạch điều khiển chỉ cần cấp (1) xung địa chỉ (hay "
        "xung ghi), (2) xung duy trì và (3) xung xoá. Không cần tín hiệu quét làm tươi phức tạp, "
        "vì một tín hiệu duy trì được cấp liên tục, kết hợp với tính nhớ cố hữu của điểm ảnh xoay "
        "chiều, duy trì mỗi điểm ảnh ở trạng thái sáng hoặc tắt một cách đơn giản. Điểm ảnh đáp "
        "ứng xung địa chỉ, duy trì và xoá như mô tả ở mục trước. Tương tự cách điều khiển động "
        "điểm ảnh một chiều đã bàn, việc địa chỉ điểm ảnh xoay chiều đòi hỏi đặt các dạng sóng "
        "điện áp đúng nhịp lên hàng và cột của ma trận, sao cho điện áp thích hợp xuất hiện trên "
        "điện cực của điểm ảnh cần chọn mà không làm thay đổi trạng thái các điểm ảnh bên cạnh. "
        "Bạn đọc muốn biết chi tiết hơn về địa chỉ điểm ảnh xoay chiều có thể xem tài liệu 4 "
        "hoặc 47."))
    b.append(p(
        "Thang xám đạt được với màn hình plasma một chiều hay xoay chiều bằng cách điều chế dòng "
        "phóng điện, hoặc điều chế độ rộng xung với dòng không đổi. Điều chế biên độ điện áp đặt "
        "để thay đổi dòng phóng điện ít được dùng vì khó điều khiển hiệu quả đáp ứng phi tuyến "
        "của dòng phóng điện. Ngược lại, điều chế độ rộng xung là kỹ thuật khả thi cho cả màn "
        "hình một chiều điều khiển nhớ xung lẫn màn hình xoay chiều có tính nhớ. Trong cả hai "
        "trường hợp, điều chế độ rộng xung đòi hỏi thiết kế mạch phức tạp để cấp xung bật và tắt "
        "đúng nhịp. Thang xám đạt được bằng cách thay đổi tỉ lệ thời gian điểm ảnh sáng so với "
        "tắt trong mỗi chu kỳ làm tươi. Ở tần số 50 kHz, một nửa chu kỳ duy trì là 10 µs. Photon "
        "VUV thường được phát xạ trong chưa tới 1 µs. Với màn hình màu, phát xạ ánh sáng nhìn "
        "thấy kéo dài lâu hơn nhiều, phosphor nhanh nhất có thời gian duy trì 10 % khoảng 5 ms. "
        "Các phosphor điển hình hơn có thời gian duy trì 10 % trong khoảng 5–10 ms [50]. Nếu ảnh "
        "được cập nhật mỗi 40 ms, tương ứng tốc độ làm tươi 25 ảnh/giây, thì độ sáng mức 1/8 đạt "
        "được bằng cách cho điểm ảnh sáng 5 ms và tắt 35 ms trong chu kỳ làm tươi đó. Thời gian "
        "sáng được rải rác trong suốt 40 ms nhờ thiết kế mạch định thời phù hợp. Ví dụ, màn hình "
        "NHK 102 cm (40 in.) có 2<sup>8</sup> hay 256 mức xám cho mỗi màu, cho tổng cộng 16 triệu "
        "(256³) mức màu [48]."))

    # ------------------------------------------------------------ 93.5
    b.append(h2("93.5 Màn hình phẳng plasma màu", "Color Plasma Flat Panel Displays"))
    b.append(h3("Cấu trúc điểm ảnh màu", "Color Pixel Structures"))
    b.append(p(
        "Trong tấm hiển thị plasma màu, phosphor phát quang cung cấp các phát xạ quang học RGB sơ "
        "cấp cần cho hiển thị ảnh màu. Khi đó phải triệt tiêu phát xạ nhìn thấy ngay trong phóng "
        "điện để tránh nhiễm màu. Cách làm phổ biến là dùng xenon làm thành phần thiểu số trong "
        "hỗn hợp khí Penning của tấm. Cấu trúc và cách bố trí phosphor của màn hình plasma màu "
        "một chiều đường chéo 102 cm (40 in.) của NHK được vẽ ở Hình 93.17, còn màn hình màu xoay "
        "chiều đường chéo 53 cm (21 in.) của Fujitsu ở Hình 93.6. Cả hai đều dùng in lưới và kỹ "
        "thuật quang khắc với mặt nạ cứng hoặc mặt nạ chống mài mòn để lắng dây dẫn, xác định "
        "vách ngăn và lắng phosphor [51]. Trong thiết kế NHK, ô thứ tư trong cấu trúc điểm ảnh "
        "màu tổ ong chứa một điểm ảnh con phosphor lục dư, để bù cho độ phát quang của phosphor "
        "lục thấp hơn phosphor đỏ và lam. Ở một cấu trúc điểm ảnh màu một chiều tổ ong tương tự, "
        "Panasonic lại đặt một điện trở nối tiếp vào vị trí điểm ảnh con thứ tư này [20]. Việc in "
        "điện trở nối tiếp cho từng điểm ảnh trên tấm nền thuỷ tinh làm phức tạp khâu chế tạo "
        "nhưng đơn giản hoá yêu cầu thiết kế mạch điều khiển. Ở Fujitsu, với cấu trúc điểm ảnh "
        "màu xoay chiều điện cực đối diện trên Hình 93.6, các vách ngăn chạy song song và nằm "
        "giữa các dây dẫn được tạo trên tấm nền phía sau. Chiều cao vách ngăn thường 100–150 µm. "
        "Vách ngăn của điểm ảnh xoay chiều và lưới tổ ong của điểm ảnh một chiều thường được làm "
        "từ cùng loại điện môi dày PbO dùng để phủ dây dẫn."))
    b.append(fig(17))

    b.append(h3("Sinh và sử dụng photon VUV trong màn hình plasma màu",
                "VUV Photon Production and Utilization for Color Plasma Flat Panel Displays"))
    b.append(p(
        "Hỗn hợp khí của màn hình plasma màu dùng xenon làm thành phần thiểu số được tối ưu cho "
        "việc tạo phát xạ VUV, dùng để kích thích phosphor phát quang RGB. Cả tổ hợp neon–xenon "
        "lẫn heli–xenon đều thông dụng. Năng lượng ion hoá của xenon là 12,3 eV, thấp hơn trạng "
        "thái kích thích thấp nhất của neon và heli, như trên Hình 93.8. Vì vậy điện tử được gia "
        "tốc bởi điện trường trong thể tích điểm ảnh sẽ ưu tiên truyền động năng cho nguyên tử "
        "xenon. Ngoài ra, các trạng thái kích thích của He hay Ne được tạo ra cũng dễ dàng truyền "
        "năng lượng dự trữ cho nguyên tử xenon qua va chạm Penning ion hoá. Do đó phát xạ nhìn "
        "thấy đỏ cam đặc trưng của phóng điện Ne bị triệt tiêu khi nồng độ Xe tăng. Fujitsu dùng "
        "khí làm việc Ne–10 % Xe trong màn hình màu của mình [18], còn Photonics Imaging thích "
        "dùng khí nền gốc heli [23], nơi có thể triệt tiêu các phát xạ quang không mong muốn ở "
        "nồng độ xenon thấp hơn một chút."))
    b.append(fig(18))
    b.append(p(
        "Xu hướng lấp đầy lớp điện tử ngoài cùng của xenon dẫn tới sự hình thành phân tử dimer "
        "xenon Xe₂*, mà các trạng thái năng lượng cũng được vẽ trên Hình 93.8 [52,53]. Sự phân ly "
        "phát xạ của dimer tạo photon có bước sóng gần 173 và 150 nm. Hình 93.18 cho thấy phát xạ "
        "của dimer chiếm ưu thế trong phổ VUV của phóng điện khí He–Xe khi tỉ lệ Xe tăng. Vì "
        "photon VUV bị thuỷ tinh hấp thụ hoàn toàn, phổ trong hình được đo bằng cách đặt các điểm "
        "ảnh điện cực đối diện bên trong một buồng chân không chứa hỗn hợp khí cần khảo sát. Biên "
        "của tấm thuỷ tinh không được hàn kín, nhờ đó có thể quan sát phóng điện điểm ảnh từ cạnh, "
        "dùng một máy đơn sắc McPherson 0,2 m kết hợp với hệ phân tích đa kênh quang học CCD của "
        "Princeton Instrument [34]. Hỗn hợp khí nền được thay đổi để có các nồng độ Xe trong He "
        "khác nhau, trong khi tổng áp suất khí giữ ở 53,3 kPa (400 Torr). Ở nồng độ Xe thấp, "
        "photon từ các trạng thái 1s<sub>4</sub> và 1s<sub>5</sub> của nguyên tử Xe chiếm ưu thế "
        "trong phổ, tạo vạch 147 nm và vạch 129 nm yếu hơn nhiều. Các phép đo quang phổ kích thích "
        "bằng laser của Tachibana cho thấy diễn biến không gian và thời gian của trạng thái "
        "nguyên tử Xe 1s<sub>4</sub> trong phóng điện màn hình plasma He/Xe [54]. Cả hai vạch "
        "nguyên tử này đều bị hấp thụ và tái phát xạ cộng hưởng mạnh. Vì vậy cường độ vạch đo "
        "được phụ thuộc mạnh vào quãng đường photon đi và áp suất riêng phần của Xe trong khí nền "
        "[55]. Với phổ trên Hình 93.18, cửa sổ vào bằng lithi florua (LiF) của buồng quang phổ đã "
        "hút chân không được đặt cách các phóng điện điểm ảnh gần nhất 100–150 nm — xấp xỉ vị trí "
        "của phosphor so với phóng điện trong một tấm hiển thị màu xoay chiều điện cực đối diện; "
        "ví dụ xem Hình 93.5."))
    b.append(p(
        "Nhớ lại rằng việc tạo cặp điện tích trên mỗi vôn đặt vào trong phóng điện khí Penning là "
        "tối ưu ở nồng độ thành phần thiểu số thấp tới 0,1 %; xem Hình 93.9. Tuy nhiên điểm ảnh "
        "plasma màu phải tối ưu lượng photon dùng được trên mỗi oát trong khi vẫn giữ yêu cầu "
        "nghiêm ngặt về độ tinh khiết màu. Vì vậy điểm ảnh plasma màu thường làm việc với nồng độ "
        "xenon trong khoảng 2–10 %. Hình 93.18 cho thấy nồng độ xenon tăng dẫn tới hình thành "
        "dimer đáng kể và phát xạ từ phân ly dimer. Vì phân ly dimer là quá trình ba hạt, gồm một "
        "photon và hai nguyên tử xenon, các phương trình bảo toàn động lượng và năng lượng không "
        "đòi hỏi nghiệm duy nhất. Do đó các vạch phát xạ tạo ra trải trên một dải phổ rộng tới "
        "vài chục nanomét. Phát xạ dimer tăng đi kèm triệt tiêu phát xạ nguyên tử xenon, vì năng "
        "lượng trong các tập mức nguyên tử tiếp tục chảy về các mức nguyên tử thấp nhất; xem Hình "
        "93.8. Cũng cần lưu ý rằng các vạch phát xạ dimer không bị hấp thụ cộng hưởng. Vì vậy "
        "cường độ đo được phản ánh phát xạ dimer từ mọi hàng điểm ảnh nằm trong đường ngắm của "
        "máy quang phổ (bốn hàng với dữ liệu trên Hình 93.18). Ngược lại, do hấp thụ cộng hưởng "
        "mạnh của các vạch nguyên tử, hơn 90 % cường độ đo được của vạch 147 nm sinh ra ở hàng "
        "điểm ảnh sát cửa sổ máy quang phổ [34,55]. Khi phân tích dữ liệu phát xạ cần chú ý đến "
        "những khác biệt lớn về quãng đường tự do trung bình của photon này."))

    b.append(h3("Kích thích và phát xạ của phosphor trong màn hình plasma màu",
                "Phosphor Excitation and Emission for Color Plasma Flat Panels"))
    b.append(p(
        "Nhiều loại phosphor phát quang có bán trên thị trường. Hiệu suất chuyển photon VUV thành "
        "phát xạ nhìn thấy phụ thuộc phức tạp vào bước sóng photon kích thích, như thấy trên Hình "
        "93.19 — hình vẽ hiệu suất chuyển đổi lượng tử tương đối so với chuẩn natri salicylat cho "
        "một số phosphor lục có sẵn [50]. Hiệu suất chuyển đổi của phosphor đỏ, lam và các "
        "phosphor lục khác có thể tìm ở tài liệu 56 và 57. Bảng 93.2 cho thành phần của một số "
        "phosphor thương mại chọn lọc và hiệu suất lượng tử tương đối của chúng với các vạch phát "
        "xạ chính của phóng điện xenon. Cần lưu ý rằng các hiệu suất lượng tử liệt kê là giá trị "
        "tương đối, và phosphor chuyển photon 8,4 eV thành photon nhìn thấy gần 2,3 eV chỉ có "
        "hiệu suất tuyệt đối 27 %. Về nguyên tắc có thể tạo hai hay nhiều photon nhìn thấy từ một "
        "photon năng lượng cao, nhưng đến nay chưa có phosphor như vậy [58]. Bảng 93.2 cũng liệt "
        "kê toạ độ trên giản đồ màu — thước đo độ tinh khiết màu của phổ phát xạ RGB. Giản đồ màu "
        "có thể tìm ở nhiều tài liệu, trong đó có tài liệu 59. Một yếu tố nữa khi chọn phosphor "
        "cho màn hình plasma là thời gian duy trì. Phần lớn phosphor trong Bảng 93.2 cần 5–13 ms "
        "để cường độ phát xạ giảm còn 10 % giá trị cực đại. Với điểm ảnh xoay chiều làm việc ở "
        "50 kHz, mỗi nửa chu kỳ điện áp duy trì chỉ kéo dài 10 µs, trong khi phóng điện chỉ tạo "
        "phát xạ VUV trong một phần nhỏ của khoảng đó. Các nỗ lực phát triển phosphor đáp ứng "
        "nhanh hơn vẫn đang tiếp tục. Ví dụ, phosphor lục Eu<sup>2+</sup> có thời gian tắt 10 % "
        "chỉ 5–10 µs và hiệu suất lượng tử tốt ở gần 173 nm đã được phát triển [50]."))
    hd2, rows2, cap2 = _table2("vi")
    b.append(table(hd2, rows2, cap2))
    b.append(fig(19))

    b.append(h3("Các yếu tố tuổi thọ của màn hình plasma màu",
                "Color Plasma Display Lifetime Considerations"))
    b.append(p(
        "Phosphor cho màn hình phẳng plasma phải chịu được môi trường khắc nghiệt do phóng điện "
        "điểm ảnh tạo ra. Cơ chế suy giảm của phosphor phát quang hiện chưa được hiểu rõ. Việc "
        "phosphor nhiễm vào phóng điện là mối lo nghiêm trọng. Mô hình hoá phóng điện cho thấy "
        "tổn thương chủ yếu do liều tích luỹ của bức xạ photon và nguyên tử metastable, dù điện "
        "trường rìa và sự tích điện bề mặt kéo dài cũng có thể dẫn tới bắn phá ion [37]. Phần lớn "
        "màn hình plasma xoay chiều dùng MgO để tăng cường độ phóng điện bằng cách phủ thêm một "
        "màng mỏng MgO lên bề mặt điện môi trên các điện cực. Để dễ chế tạo, MgO thường được lắng "
        "bằng bay hơi chùm điện tử, ở một trong những bước cuối cùng trước khi hàn kín thuỷ tinh "
        "và nạp khí. Nếu không dùng mặt nạ, MgO cũng có thể phủ lên phosphor. Màng MgO vừa tạo "
        "lớp bảo vệ cho phosphor, vừa làm suy giảm cường độ dòng photon VUV dùng để kích thích "
        "phosphor. Hình 93.20 cho độ truyền qua của photon VUV theo bước sóng qua các màng MgO "
        "[34,60]. Các phép đo cho thấy các vạch phát xạ nguyên tử chính của Xe ở 129 và 147 nm bị "
        "một màng MgO chỉ dày 75 nm làm suy giảm gần 95 %. Ngược lại, các vạch phát xạ dimer "
        "quanh 173 nm ít bị suy giảm hơn nhiều, với hệ số truyền qua tương ứng 30–50 % cho màng "
        "MgO dày 200 và 75 nm. Vì vậy nhà thiết kế màn hình plasma xoay chiều thường phải cân "
        "bằng giữa việc tăng cường phóng điện nhờ phát xạ điện tử thứ cấp của MgO, sự suy giảm "
        "phóng điện do MgO hấp thụ photon, và độ phức tạp chế tạo gắn với việc lắng MgO — yếu tố "
        "ảnh hưởng tới giá thành cuối cùng của màn hình. Ngoài ra, nhà thiết kế còn phải tính đến "
        "sự lão hoá hay suy giảm độ chói theo thời gian, một phần do tốc độ bào mòn MgO bởi phún "
        "xạ như đã bàn sơ lược ở trên."))
    b.append(fig(20))

    # ------------------------------------------------------------ 93.6
    b.append(h2("93.6 Kiểm tra và đo lường", "Inspection and Metrology"))
    b.append(p(
        "Việc chế tạo tấm hiển thị plasma dùng một số bước công nghệ điển hình của chế tạo linh "
        "kiện bán dẫn. Tuy kích thước đặc trưng lớn hơn nhiều so với yêu cầu của bán dẫn, phạm vi "
        "kích thước mà tính toàn vẹn của hình dạng phải được bảo đảm cũng lớn hơn nhiều. Việc "
        "khẳng định quy trình chế tạo màn hình đang trong tầm kiểm soát, hoặc mô tả định lượng "
        "nhanh độ lệch so với giới hạn công nghệ chấp nhận được, là điều thiết yếu để sản xuất "
        "màn hình chất lượng cao với hiệu suất cao. Cần thông tin ở nhiều thang độ dài khác nhau. "
        "Việc lắng vật liệu phủ toàn bộ lên đế phải đồng đều; phải tránh sai lệch lớn về chiều "
        "dày giữa một điểm trên đế và một điểm cách xa. Tương tự, độ nhám của các lớp lắng phải "
        "nằm trong giới hạn xác định. Cuối cùng, thành phần hoá học của các lớp lắng và độ đồng "
        "nhất không gian của chúng cần được đo và kiểm soát."))
    b.append(p(
        "Ba thiết bị đo biên dạng thương mại — CyberOptics, Zygo và Leitz — dựa trên tam giác hoá "
        "hoặc giao thoa bằng laser hay ánh sáng trắng; xem Bảng 93.3 [61–63]. Các máy này rất "
        "phù hợp để xác định biên dạng lớp kim hoá sau khi tạo hình. Chúng có vẻ không hữu ích để "
        "đo chiều dày các lớp mờ, và chẳng hạn không thể đo chiều dày lớp kim hoá phủ toàn bộ "
        "trước khi tạo hình. Thiết bị CyberOptics được dùng rộng rãi trong công nghiệp đóng gói "
        "điện tử nhờ tín hiệu ít nhiễu. Cải thiện phân giải theo phương đứng sẽ làm tăng giá trị "
        "của nó cho việc kiểm soát quy trình chế tạo màn hình. Máy Zygo có phân giải phương đứng "
        "tốt hơn nhưng không có khả năng quét thực sự. Máy Leitz được thiết kế riêng để đo linh "
        "kiện tinh thể lỏng chưa hoàn thiện, và có lẽ được tối ưu cho ứng dụng đó. Cả CyberOptics "
        "và Zygo đều có nhiều đầu đo với phân giải và trường nhìn khác nhau. Tuy nhiên khoảng "
        "cách theo phương đứng mà hiện tượng giao thoa có thể xảy ra trong máy Zygo rất hạn chế, "
        "nên máy có thể không phù hợp để đo các chi tiết có kích thước phương đứng lớn."))
    hd3, rows3, cap3 = _table3("vi")
    b.append(table(hd3, rows3, cap3))
    b.append(p(
        "Tuỳ yêu cầu hệ thống, có thể mua một hệ đo laser hữu ích với giá chỉ 20.000 USD. Hệ đầy "
        "đủ tính năng có thể dễ dàng lên tới 100.000 USD. Tuy nhiên phần lớn chi phí nằm ở các bàn "
        "dịch chuyển chính xác dùng để di chuyển mẫu một cách được kiểm soát chặt bên dưới các đầu "
        "đo cố định. Vì bàn dịch chuyển chính xác đáp ứng yêu cầu của thiết bị đo có thể đã là một "
        "phần của quy trình sản xuất màn hình, hoặc chỉ cần nâng cấp nhỏ để phù hợp, chi phí đưa "
        "năng lực đo lường vào vận hành có thể nhỏ hơn nhiều so với các con số trên. Vì giá đầu đo "
        "laser thấp, cũng có thể dùng nhiều đầu đo cố định để tăng tốc độ kiểm tra và đo lường."))
    b.append(p(
        "Bảng 93.4 liệt kê đặc tính của hai kỹ thuật đo tiên tiến để đo biên dạng không tiếp xúc "
        "và phân tích hoá học. Theo hiểu biết của các tác giả, hệ thống loại này chưa có trên thị "
        "trường. Tuy vậy chúng đang được các nhà nghiên cứu ở Phòng thí nghiệm Quốc gia Sandia sử "
        "dụng và cho thấy triển vọng thương mại. Trong phép đo tán xạ ngược beta, phổ năng lượng "
        "của các hạt beta tán xạ ngược cho thước đo chính xác thành phần nguyên tố của bề mặt. Kỹ "
        "thuật này đã được dùng để đo chiều dày màng mỏng kim loại lắng với lượng vết trên bề mặt "
        "diện tích lớn (vài mét vuông) trong các tokamak [64]. Với phân giải chiều sâu khoảng 100 "
        "pm, tán xạ ngược beta có thể là cơ sở vật lý cho một thiết bị đo biên dạng bề mặt độ nhạy "
        "cao. Phép đo huỳnh quang tia X, thường được thực hiện trong không khí, cho thông tin về "
        "chiều dày và thành phần màng; các thông số hiệu năng của kỹ thuật này cũng được liệt kê "
        "trong Bảng 93.4. Phải dùng chân không khi khảo sát các nguyên tố nhẹ như carbon — một sản "
        "phẩm cháy không mong muốn tiềm tàng của chất kết dính phosphor — vì tia X tạo ra là tia "
        "X “mềm”. Dù thiết bị huỳnh quang tia X có thể có phân giải ngang tốt, kích thước điểm đo "
        "lớn hơn có thể hữu ích khi cần thông tin đã lấy trung bình nhiều hơn, ví dụ chiều dày "
        "màng. Cuối cùng, phép đo dòng xoáy có thể là phương pháp nhanh và tin cậy để xác định "
        "chiều dày lớp kim hoá mờ phủ toàn bộ trước khi tạo hình. Kỹ thuật này được cho là có thể "
        "đạt độ chính xác đo chiều dày 10 % với lớp dẫn mỏng tới 1 µm."))
    hd4, rows4, cap4 = _table4("vi")
    b.append(table(hd4, rows4, cap4))
    b.append(p(
        "Nhiều thiết bị đo định lượng chiều dày và thành phần hoá học của các lớp lắng có nhược "
        "điểm là trường nhìn khá hạn chế. Cần những kỹ thuật đặc trưng cho phép nhận diện nhanh "
        "các khuyết tật thị giác trong lớp lắng phủ toàn bộ và trong các lớp đã tạo hình từ đó. "
        "Thiết bị kiểm tra bằng mắt đã có cho việc nhận diện khuyết tật trong màn hình tinh thể "
        "lỏng. Các hãng sản xuất gồm Minato Electronics, Advantest, ADS, Photon Dynamics và "
        "Teradyne. Tất cả đều dùng linh kiện CCD và thuật toán riêng để nhận diện khuyết tật dạng "
        "đường và dạng vùng. Các khuyết tật gặp trong sản xuất màn hình plasma khối lượng lớn có "
        "thể đủ giống về ngoại hình với khuyết tật trong sản xuất màn hình tinh thể lỏng để thiết "
        "bị này tỏ ra hữu ích sau những điều chỉnh thích hợp. Tuy nhiên các thiết bị này đắt."))
    b.append(p(
        "Dù các nhà nghiên cứu và nhà sản xuất thiết bị tin rằng các thiết bị và kỹ thuật mô tả "
        "trên sẽ phù hợp để kiểm soát quy trình trực tuyến trong sản xuất màn hình plasma, tất cả "
        "đều đồng ý rằng cần phát triển thêm. Cần đặc trưng hoá kỹ lưỡng các chi tiết thật trên "
        "thiết bị thương mại cụ thể trong môi trường sản xuất trước khi có thể kết luận về mức "
        "phù hợp của thiết bị và kỹ thuật cho ứng dụng dự kiến. Điều này đặc biệt đúng với những "
        "phép đo khó hơn, như đo chiều dày lớp điện môi trên các đường dẫn. Rõ ràng không có một "
        "thiết bị duy nhất nào đáp ứng mọi yêu cầu đo kích thước màng và chi tiết, cũng như mọi "
        "yêu cầu đặc trưng hoá học. Sẽ cần một số thiết bị để đo một cách tin cậy các thông số "
        "phục vụ kiểm tra, đặc trưng hoá và kiểm soát quy trình chế tạo màn hình plasma."))

    # ------------------------------------------------------------ notes
    b.append(h2("Ghi chú của người dịch", "Translator's note"))
    b.append(note(
        "<b>Chữ và ký hiệu bị mất trong lớp văn bản.</b> Bản PDF gốc là bản scan; lớp văn bản làm "
        "mất ký tự µ, × và một số chữ Hy Lạp. Những chỗ đã khôi phục: “100 mm” của khe khí là "
        "100 µm; “25 mm” của màng PbO là 25 µm; “20 mm” của dây dẫn là 20 µm; “5 mm” của lớp vỏ "
        "là 5 µm; “10 ms” của nửa chu kỳ duy trì ở 50 kHz là 10 µs; “1 ms” của phát xạ VUV là "
        "1 µs; “1 mm” của lớp dẫn trong mục 93.6 là 1 µm; “852 ´ 480” là 852 × 480; “R = 500 kW” "
        "là 500 kΩ; “R = 5 MW” là 5 MΩ; đầu dò “1 MW, 3 pF” là 1 MΩ, 3 pF. Trong Bảng 93.3 và "
        "93.4, toàn bộ đơn vị chiều dày in là “mm” đã được khôi phục thành µm, trừ hai giá trị "
        "phân giải 100 pm và 150 pm vốn đã đúng. "
        "<b>Chữ Hy Lạp bị thay bằng chữ Latin.</b> Hệ số phát xạ điện tử thứ cấp in là “g” là γ; "
        "mật độ điện tích trong phương trình Poisson in là “r(x)” là ρ(x); độ dài Debye in là "
        "“lD” là λ<sub>D</sub>; tích hằng số Planck với tần số in là “hn” là <i>h</i>ν; “h” trong "
        "mục 93.1 (hiệu suất) không xuất hiện trong chương này. "
        "<b>Hai lỗi số liệu của bản gốc.</b> (1) Chú thích Hình 93.5 in “3 Pa (~400 Torr)”, nhưng "
        "400 Torr là 53,3 kPa; hình trong bản dịch ghi 3×10<sup>4</sup> Pa, đúng với 400 Torr và "
        "với con số 53,3 kPa dùng trong toàn chương. (2) Bảng 93.1 in tương phản của Hitachi là "
        "“50.1”, rõ ràng là 50:1; bảng giữ nguyên giá trị đã sửa và ghi chú lại. "
        "<b>Một chỗ không nhất quán về đường tải.</b> Hình 93.12 in bốn đường tải cho 500 kΩ ở "
        "175, 225, 275 V và 5 MΩ ở 175 V, nhưng các đường này không cắt đặc tuyến ở những chỗ mà "
        "quan hệ <i>I</i> = (<i>V</i><sub>a</sub> − <i>V</i><sub>g</sub>)/<i>R</i> đòi hỏi nếu "
        "trục hoành là điện áp trên khe khí. Hình trong bản dịch vẽ lại đúng hình học đã in, kèm "
        "ba chú thích “stable on / unstable / stable off”, và không tự ý sửa các đường tải. "
        "<b>Công thức hoá học trong Bảng 93.2.</b> Lớp văn bản làm hỏng một số chỉ số dưới: bản "
        "gốc in “LuBO8:Tb”, “ScBO8:Tb”, “GbBO3:Eu”, “Zn3SiO4:Mn”, “(Y,Gd)BO8:Eu”; ở đây in theo "
        "hợp chất hợp lý tương ứng là LuBO<sub>3</sub>, ScBO<sub>3</sub>, GdBO<sub>3</sub>, "
        "Zn<sub>2</sub>SiO<sub>4</sub> và (Y,Gd)BO<sub>3</sub>. "
        "<b>Một chỗ sai chính tả của bản gốc.</b> Tên tác giả tài liệu 44 in là “Schone”, trong "
        "khi tài liệu 44 tự ghi “Schone, D. Walsh…” — giữ nguyên như đã in. "
        "<b>Không có mục Định nghĩa thuật ngữ.</b> Chương này không có khối định nghĩa thuật ngữ, "
        "nên nó không thêm mục nào vào trang /glossary.html."))

    b.append(h2("Tài liệu tham khảo", "References"))
    b.append(refs(_REFS))

    return "".join(b)


# ================================================================ ENGLISH
def body_en():
    b = []

    b.append(h2("93.1 An Introduction to Plasma-Driven Flat Panel Displays"))
    b.append(h3("Development History and Present Status"))
    b.append(p(
        "Plasma-driven flat panel display pixels were invented by Bitzer and Slottow at the "
        "University of Illinois in 1966 [1–3]. Figure 93.1 shows one of the inventors' early "
        "designs: parallel sets of thin conducting wires are deposited on two glass substrates, "
        "which are then mounted with the conductor sets perpendicular to one another. A spacer — "
        "here a perforated glass dielectric — maintains a gap of about 100 µm, and the gap is "
        "filled with an inert gas at roughly half an atmosphere. Pixels form where two wires "
        "cross, aligned with the perforations, and light when the voltage between the wires is "
        "enough to break the gas down. The basic design has been refined endlessly since, but the "
        "underlying idea is still in wide use."))
    b.append(fig(1, "en"))
    b.append(p(
        "Through the 1980s plasma products were monochrome and neon-based, producing the red-orange "
        "585–640 nm emission characteristic of the neon atom directly in the discharge volume. Dot "
        "matrix displays of the kind in Figure 93.2 were common [3,4]. Owens-Illinois improved "
        "glass sealing and spacer supports [5,6] and IBM improved the understanding and control of "
        "the discharge [7–15]; together these made large-area, high-resolution monochrome panels "
        "possible. The largest plasma panels ever built were Photonics Imaging's 1 m diagonal "
        "monochrome displays: over two million pixels at 20 pixels/cm (50 lines/in.) [4]."))
    b.append(fig(2, "en"))
    b.append(p(
        "Lithography, patterning and phosphor work then drove colour. Table 93.1 collects panel "
        "specifications and manufacturing plans for the major investors as of January 1997 [16]. "
        "Stanford Research put 1995 plasma panel sales at $230 million and projected $4.1 billion "
        "for 2002; NEC projected $2.0 billion by 2000 and $7.0 billion by 2002 [17]. Capacity was "
        "expected to reach nearly 40,000 units per month by the end of 1998 and over 100,000 by "
        "early 2000. Fujitsu shipped the first high-information-content full-colour panel in 1993 "
        "— 21 in. diagonal, ac-driven, 640 × 480 [17,18]. Figures 93.3 and 93.4 show two later "
        "entries."))
    hd1, rows1, cap1 = _table1("en")
    b.append(table(hd1, rows1, cap1, cls=" dense", nw=(0, 1, 2, 3), colw=(72, 34, 34, 78, 44, 52, 32, 62, 74, 34, 52, 62)))
    b.append(fig(3, "en"))
    b.append(p(
        "The first is NHK's 102 cm (40 in.) full-colour HDTV panel [19–22]: 1,075,000 colour "
        "pixels (1344 × 800) at a 0.65 mm pitch in both directions (15.4 pixels/cm), pulsed "
        "dc-driven, peak luminance 93 cd/m², contrast 80:1, 256 grey levels, 8 cm thick and 8 kg. "
        "The panel itself measures 87.5 × 52.0 cm and is only 6 mm wide. The second, in Figure "
        "93.4, is Photonics Imaging's 76 cm (30 in.) ac colour panel [23,24]: 1024 × 768 colour "
        "pixels at 16.8 pixels/cm (0.59 mm pitch), the highest-resolution full-colour plasma "
        "display built to that date, with 64 grey levels per channel and an average white "
        "luminance above 10³ cd/m² (30 fL)."))
    b.append(fig(4, "en"))

    b.append(h3("dc and ac Plasma Pixels"))
    b.append(p(
        "Plasma pixels can be built for dc or ac operation; Figure 93.5 shows the two simplest "
        "designs. In both, parallel conductor sets sit on glass substrates — usually ordinary "
        "soda-lime float glass, to keep cost down — mounted about 100 µm apart with the sets "
        "perpendicular. The gap holds an inert gas that discharges and lights the pixel when "
        "enough voltage appears across two crossing wires."))
    b.append(fig(5, "en"))
    b.append(p(
        "In a dc pixel (Figure 93.5a) the gas touches the electrodes. At 53.3 kPa, a 100 µm gap "
        "and 200 V, electrons cross the gap in about 0.2 ns and ions in about 20 ns. Once "
        "breakdown starts the discharge resistance is negligible, so dc operation requires an "
        "external series resistor at every pixel to limit current. dc pixels are usually run in "
        "pulsed mode with frequency modulation setting brightness, at a base frequency of 50 kHz — "
        "too fast for the eye to see flicker, slow enough to leave room for intensity and refresh "
        "control. dc and ac pixels are easy to confuse in the literature, because dc pixels are "
        "often pulsed and often use polarity reversal to spread sputter damage over both "
        "electrodes; the reliable markers of a dc pixel are electrodes in direct contact with the "
        "gas and a current-limiting resistor in each pixel circuit."))
    b.append(p(
        "Figure 93.5b shows an ac pixel. The geometry differs only slightly; the operation differs "
        "a great deal. The conductors are covered with a dielectric — typically lead oxide (PbO, "
        "ε ≈ 15) about 25 µm thick, with a 50–200 nm magnesium oxide (MgO) film on top, in contact "
        "with the gas. That dual film does two jobs: charge storage and secondary electron "
        "emission. Breakdown needs about 120–180 V for the parameters shown."))
    b.append(p(
        "In an ac pixel the carriers cannot reach the conductors; they collect as surface charge "
        "on the dielectric. The field in the gap is always the sum of the applied field and the "
        "field of that surface charge, and the second cancels the first within 100–200 ns, so the "
        "pixel turns itself off and needs no series resistor. At the next half cycle the applied "
        "voltage reverses and the gap sees the sum of the new applied voltage and the wall voltage "
        "left by the previous discharge — enough to fire again even though the applied voltage "
        "alone would not break the gas down. That stored charge is the pixel's memory: its "
        "presence or absence decides whether the pixel fires at the next half cycle."))

    b.append(h3("General Attributes of Plasma Displays"))
    b.append(p(
        "The strongly nonlinear pixel characteristic, with inherent memory, simplifies the drive "
        "electronics needed to refresh and update the array. The simple pixel makes large-area "
        "manufacturing problems — alignment, film-thickness uniformity — more tractable, and "
        "against colour AMLCDs, which need a thin-film transistor at every pixel, plasma wins on "
        "manufacturing and drive simplicity for large areas. It loses on drive voltage (100–275 V) "
        "and on power: plasma is a poor fit for portable products, though not restrictive for "
        "office or domestic use — Photonics Imaging's 30 in. panel draws only 300 W peak [23]. At "
        "high power plasma panels are bright enough to read in sunlight, and dim easily by "
        "amplitude or frequency modulation."))
    b.append(p(
        "Plasma suits 0.5–5 m applications — video conferencing, large meeting-room displays, "
        "outdoor signage, wide-view simulators — and thin high-resolution colour panels are "
        "attractive for high-resolution desktop graphics. Viewing angles exceed 160° in many "
        "designs [22–24]; with metal electrodes the best angle is slightly off normal, because the "
        "front wire shadows part of the emission. That holds both for monochrome pixels emitting "
        "in the discharge and for colour panels where the viewer sees red, green and blue from "
        "VUV-stimulated phosphors. Transparent electrodes such as ITO have been tried, at a cost "
        "in power because ITO conducts worse than metal [18]; in current designs the metal line is "
        "only about 20 µm wide, so its opacity is not a major problem."))
    b.append(p(
        "For colour pixels the gas mixture is changed to emit in the VUV; everything else about "
        "the discharge is the same. Ideally nothing visible is emitted in the discharge itself and "
        "VUV-stimulated phosphors supply the RGB. Figure 93.6 shows the ac colour pixel used by "
        "Fujitsu [18]: straight barrier structures about 100 µm tall run parallel to and between "
        "the vertical conductors on the rear plate, their sidewalls coated alternately with red, "
        "green and blue phosphor. Fujitsu uses a three-electrode surface-discharge design, "
        "slightly more complicated than the opposed-electrode cell of Figure 93.5b; the chapter "
        "returns to it after the discharge physics."))
    b.append(fig(6, "en"))

    b.append(h2("93.2 Fundamentals of Plasma Pixel Operation"))
    b.append(h3("Atomic Physics Processes"))
    b.append(p(
        "The pixel is a rich environment for atomic physics, electron collisions, photon "
        "production and transport, and plasma–surface interaction. Weber's diagram of these "
        "processes for a neon–argon pixel is reproduced as Figure 93.7 [4]; standard texts cover "
        "the underlying physics [25–27]. The processes form a closed loop, and the discussion "
        "starts from a single seed electron in the gap, accelerated by the field of the applied "
        "voltage. Seed particles — electrons, electron-producing photons, or metastable atoms — "
        "are usually supplied from a controlled source that may be outside the pixel being fired: "
        "electrodes at the panel edge, hidden behind opaque wires, or neighbour pixels primed by "
        "careful timing [4,19,28]."))
    b.append(fig(7, "en"))
    b.append(p(
        "Electron transport is a balance between field acceleration and collisional loss. In "
        "Figure 93.7 the gas is 98–99.9% neon, so electrons collide mostly with Ne. The lowest "
        "excited state is 16.6 eV above ground and the ionisation energy is 21.6 eV: electrons "
        "below 16.6 eV can only scatter elastically, above 16.6 eV they can excite an outer-shell "
        "electron, and above 21.6 eV they can ionise:"))
    b.append(eq(_eq("93.1"), "93.1"))
    b.append(p(
        "Excitation and ionisation move energy from the electron population to the neutral gas, "
        "and every ionisation adds an electron able to ionise again: the avalanche of Figure 93.7, "
        "seen experimentally as a rapid rise in gap current. dc panels put about 500 kΩ in series "
        "with each pixel, so with <i>V</i><sub>a</sub> fixed the gap voltage "
        "<i>V</i><sub>g</sub> = <i>V</i><sub>a</sub> − <i>IR</i> falls as the current rises, and a "
        "steady state establishes quickly; brightness and grey scale come from frequency "
        "modulation of the pulsed discharge at about 50 kHz. In ac pixels the charge that collects "
        "on the dielectric shields the gap and the discharge extinguishes itself."))
    b.append(p(
        "Collisions above 16.6 eV also excite outer-shell electrons into the many states of Figure "
        "93.7:"))
    b.append(eq(_eq("93.2a"), "93.2a"))
    b.append(eq(_eq("93.2b"), "93.2b"))
    b.append(p(
        "Most of those states live for fractions of a nanosecond to tens of nanoseconds [30] and "
        "decay with the emission of a characteristic photon, <i>h</i>ν in Eq. 93.2. The red-orange "
        "neon emission comes from 2p → 1s transitions [30,31]; two of the four 1s levels radiate to "
        "ground at 74.4 and 73.6 nm, while decay from the other two is hindered by selection "
        "rules, giving the metastable states lifetimes measured in seconds [31]. A metastable Ne "
        "atom carries 16.6 eV of latent energy that it cannot shed against ground-state neon but "
        "readily releases whenever a lower configuration is available — chiefly in collisions with "
        "argon, or at the pixel walls."))
    b.append(fig(8, "en"))
    b.append(p(
        "Figure 93.8 compares the level structures of the inert gases, which is what makes the "
        "energy exchange legible. Argon's ionisation energy, 15.8 eV, sits 0.8 eV below the neon "
        "metastable, so the metastable can ionise it:"))
    b.append(eq(_eq("93.3"), "93.3"))
    b.append(p(
        "This is a Penning reaction, and a mixture that relies on the metastables of the majority "
        "species to ionise the minority is a Penning mixture [25,26,32]. Figure 93.9 shows how "
        "efficiently charge pairs are produced in Ne/Ar Penning gas at various argon fractions: "
        "ion pairs per volt are best at low argon fractions (0–10%) except at very large "
        "<i>E</i>/<i>P</i>, above 75 V/m/Pa (100 V/cm/torr). The data are Kruithof and Penning's "
        "original 1937 measurements [32]."))
    b.append(fig(9, "en"))
    b.append(p(
        "Pixels run near 53.3 kPa (400 torr) for enough photon production, with fields around "
        "100 MV/m, so <i>E</i>/<i>P</i> ≈ 18.8 V/m/Pa (25 V/cm/torr) and both charge-pair "
        "production and luminous efficiency are optimised at 0.1–10% argon, depending on pressure, "
        "gap and drive voltage. For a given voltage the product <i>Pd</i> measures the balance "
        "between field acceleration and collisional loss, which is exactly what the Paschen curves "
        "of Figure 93.10 plot [26,33,45]. Each gas has its minimum at its own <i>Pd</i>, set by "
        "its ionisation levels and energy channels: in neon, excitation and ionisation dominate; "
        "in air, much of the energy goes into vibrational, rotational and dissociative modes that "
        "do not ionise."))
    b.append(fig(10, "en"))
    b.append(p(
        "At fixed pressure a wider gap lowers the field per volt and needs more voltage; a "
        "narrower gap gives a strong field but too few collisions to build an avalanche. At fixed "
        "gap, high pressure shortens the mean free path so electrons cannot gain ionising energy "
        "unless the field is very strong, and low pressure gives too few collisions. Penning "
        "processes are especially efficient: 0.1% argon in neon drops the minimum from about 250 V "
        "to about 150 V, at <i>Pd</i> = 40 Pa·m (30 torr·cm)."))

    b.append(h3("Discharge Physics for Plasma Pixels"))
    b.append(p(
        "Electrons move far faster than ions. In a neutral plasma under an applied field the "
        "electrons rush to the anode, the ions follow slowly, and a local charge imbalance builds "
        "up because electrons arrive faster than ions. Poisson's equation"))
    b.append(eq(_eq("93.4"), "93.4"))
    b.append(p(
        "shows the local field that answers the net positive charge density ρ(<i>x</i>), with "
        "<i>n</i><sub>i</sub> and <i>n</i><sub>e</sub> the ion and electron profiles and <i>e</i> "
        "the electron charge. That field slows the electrons leaving any volume and forces them to "
        "follow the ion motion; the ions are accelerated in turn, by a factor set by the "
        "electron-to-ion mass ratio. The combined motion is ambipolar flow [25–27]."))
    b.append(p(
        "In a steady dc discharge the current is set by the applied voltage and the series "
        "resistor, and no net charge can accumulate in the gap: pairs arrive at the electrodes as "
        "fast as ionisation creates them, and ions and electrons leave at equal rates. The "
        "equilibrium is carried by the potential profile of Figure 93.11a. Because electrons "
        "shield so well, the potential is flat across the gap and the whole drop sits in a thin "
        "sheath at each electrode. The Debye length,"))
    b.append(eq(_eq("93.5"), "93.5"))
    b.append(p(
        "measures that shielding distance: the sheath thickens with electron temperature and thins "
        "with density. With <i>kT</i><sub>e</sub> of a few electron volts and "
        "<i>n</i><sub>e</sub> of order 10<sup>16</sup>/m³ the sheath is about 5 µm. The plasma "
        "potential rises to just above the applied voltage at the anode, so only the most "
        "energetic electrons surmount the anode barrier, which adjusts until electron loss at the "
        "anode equals ion loss at the cathode. An ac pixel has a similar profile, but it evolves "
        "as the pulse proceeds: charge arriving at the dielectric is trapped, the boundary "
        "potential falls (Figure 93.11b), and the discharge ends when the wall field cancels the "
        "applied field. As the carrier density falls near the end of the pulse the shielding "
        "weakens: the sheath drop becomes small but the sheath fills much of the gap [36,37]."))
    b.append(fig(11, "en"))

    b.append(h3("Plasma Surface Interactions"))
    b.append(p("<b>Ion-induced secondary electron emission.</b>"))
    b.append(p(
        "Ions crossing the cathode sheath strike the surface with kinetic energy equal to the "
        "plasma potential — just over 200 V in the example of Figure 93.12a — and capture an "
        "electron, depositing the recombination energy as well. That energy drives two processes "
        "that matter here: secondary electron emission, which raises luminous efficiency, and "
        "sputtering, which shortens life. Secondary electrons are excellent at driving ionisation: "
        "they gain a lot of energy crossing the sheath and then have the whole gap in which to "
        "ionise. The coefficient γ is the number of electrons ejected per incident ion [25,26], "
        "and it varies with ion energy and cathode material. ac panels exploit MgO, which is also "
        "a good insulator, as charge storage requires. Measuring γ for MgO is hard, especially "
        "below 500 eV, and sample charging complicates it [38]; relative yields are usually "
        "deduced from discharge intensity [11,12,39–42]. Chou, using a pulsed ion beam with "
        "surface neutralisation between pulses, found γ = 0.45 for Ne⁺ and 0.05 for Ar⁺ at 200 eV "
        "[39]. Photons and metastables also eject electrons (Figure 93.7); being insensitive to "
        "the field, they propagate isotropically and often serve as the seed population."))
    b.append(fig(12, "en"))
    b.append(p("<b>Sputtering.</b>"))
    b.append(p(
        "Ions accelerated across the sheath deposit energy at the cathode and eject surface atoms. "
        "Sputtering erodes the cathode and degrades the pixel: sputtered impurities contaminate "
        "the discharge and emit visible light that spoils colour purity, and redeposited films "
        "degrade the electrical behaviour or, in colour panels, shield the phosphor from VUV. For "
        "2 keV Ar⁺ on MgO the measured yield is slightly above one atom per ion [43]; low-energy "
        "data are hard to obtain because the yields are small, the currents must be large and the "
        "samples charge. Despite the gap in the data, ac panel makers demonstrate lifetimes well "
        "beyond 10,000 h [18,23]. Shone et al. [44] used Rutherford backscattering of 2.8 MeV "
        "alpha particles to measure MgO thickness on PbO to ±1.5 nm — an excellent research tool, "
        "but it needs a large accelerator and is unsuited to a fabrication line."))

    b.append(h2("93.3 Pixel Electrical Properties"))
    b.append(h3("Electrical Properties of dc Pixels"))
    b.append(p(
        "The dc gap behaves as a variable resistor: open circuit before breakdown, then a good "
        "conductor with only a small resistance <i>R</i><sub>P</sub>. Since <i>R</i> ≫ "
        "<i>R</i><sub>P</sub>,"))
    b.append(eq(_eq("93.6"), "93.6"))
    b.append(p(
        "so the current is set by the applied amplitude and the series resistor. The drive is "
        "typically a 50 kHz square wave with a ~50 ns rise, 175–275 V, <i>R</i> = 500 kΩ, giving "
        "0.35–0.55 mA. Without a large series resistance the current is limited only by some "
        "physical failure such as melting the electrodes."))
    b.append(p(
        "Figure 93.12 shows the characteristic of a pixel that breaks down at 250 V [4]. Below "
        "breakdown only leakage flows and the pixel is off; at breakdown the situation is dynamic, "
        "current rising and gap voltage falling until the load line <i>V</i><sub>a</sub> = "
        "<i>IR</i> intersects the discharge characteristic. At 175 V the pixel is always off, at "
        "275 V always on, and at 225 V with 500 kΩ the two stable states are both reachable: "
        "approaching 225 V from below leaves it off, dropping from a high voltage leaves it on. "
        "The intersection with the negative-resistance region is unstable and the pixel moves to "
        "one of the two stable points. That negative-resistance region cannot be measured through "
        "500 kΩ; the figure uses a 5 MΩ line to reach it."))

    b.append(h3("Electrical Properties of ac Pixels"))
    b.append(p("The ac pixel is a breakdown capacitor:"))
    b.append(eq(_eq("93.7"), "93.7"))
    b.append(p(
        "with <i>V</i><sub>a</sub> the applied voltage, <i>I</i> the current, <i>C</i> the pixel "
        "capacitance and <i>Q</i> the collected charge. <i>R</i> is minimised to save power, so"))
    b.append(eq(_eq("93.8"), "93.8"))
    b.append(p("The capacitance is the series combination of the two dielectric films and the gas gap:"))
    b.append(eq(_eq("93.9"), "93.9"))
    b.append(p("with, for each layer,"))
    b.append(eq(_eq("93.10"), "93.10"))
    b.append(p(
        "where <i>A</i> is roughly the square of the conductor width. A typical pixel has 25 µm of "
        "PbO (ε ≈ 15ε<sub>0</sub>) and 50–200 nm of MgO (ε ≈ 6ε<sub>0</sub>, depending on purity "
        "and microstructure [45]). MgO contributes negligibly to the capacitance; it is there for "
        "its secondary emission. Before breakdown the capacitance is essentially that of the gap — "
        "about 500 pF for 20 µm conductors. Differentiating Eq. 93.8 gives the current:"))
    b.append(eq(_eq("93.11"), "93.11"))
    b.append(p(
        "That displacement current is the first, large peak in Figure 93.13, which shows the "
        "current response of a 45 × 45 ac array to one pulse of a 50 kHz train. The measurement "
        "used an induction loop for current and a high-impedance probe (1 MΩ, 3 pF) for voltage, "
        "captured on a 300 MHz oscilloscope."))
    b.append(fig(13, "en"))
    b.append(p(
        "Below the breakdown threshold only the displacement current of Eq. 93.11 appears "
        "(Figure 93.13a). Above it a second pulse — the discharge current — appears as well "
        "(Figure 93.13b), accompanied by strong photon emission. Figure 93.14 plots total charge "
        "displacement against applied amplitude for a helium–xenon (2%) Penning mixture [35], and "
        "the hysteresis is the memory: nothing flows from 0 to 180 V with no wall charge present; "
        "above 180 V the pixel fires; a single pulse below 135 V turns it off even with wall charge "
        "present."))
    b.append(fig(14, "en"))
    b.append(p(
        "Charge pairs from one pulse collect on the dielectric and help form the next. In a fully "
        "developed discharge the wall charge cancels the applied field, as Figure 93.15 shows — a "
        "composite of measured current and computed surface charge [34,36]. When the applied "
        "voltage reverses, wall and applied voltages add, and the gap briefly sees about twice the "
        "applied voltage. That is what produces the bistable behaviour of Figure 93.14."))
    b.append(fig(15, "en"))
    b.append(p(
        "Addressing follows directly. Each pixel is continuously supplied with a 160 V square wave "
        "— the sustain voltage. A pixel that is off stays off, since there is no wall charge to "
        "reinforce the sustain field. A single 200 V address pulse fires it, and the charge "
        "collected on the dielectric then shields the gap completely. At the next sustain reversal "
        "the gap sees 160 V of sustain plus 200 V of wall voltage: 360 V, far more than enough to "
        "fire again and leave a wall charge of the opposite polarity, this time exactly cancelling "
        "the applied field at 160 V. The next reversal gives 160 + 160 = 320 V and the pixel keeps "
        "firing. To stop it, a single low-voltage erase pulse — 120 V in this example — produces "
        "120 + 160 = 280 V across the gap, a weaker discharge that does not re-establish a "
        "reversed wall charge, so the following sustain pulse finds too little charge to fire. "
        "Ideally the erase drives the wall charge exactly to zero; in practice it rarely does, and "
        "Figure 93.15 shows the residue being cleaned up by very weak, essentially dark discharges "
        "over a few cycles — which does not disturb subsequent write pulses in frequency-modulated "
        "operation."))

    b.append(h2("93.4 Display Priming, Addressing, Refresh, and Gray Scale"))
    b.append(p(
        "Priming supplies the first electrons. Metastables and photons work too, since they ionise "
        "the background gas. Pilot-cell priming puts a separate electron-generating cell near the "
        "pixel to be addressed, often at the panel periphery but able to seed the whole display; "
        "self-priming creates an auxiliary discharge inside each pixel, usually hidden behind an "
        "opaque conductor. A trace of radioactive Kr<sup>85</sup> in the gas is a passive option: "
        "its beta radiation seeds electrons uniformly, the concentration needed is low, and the "
        "betas cannot penetrate the glass, so user exposure is negligible — but handling "
        "radioactive material is a manufacturing hazard, so the technique is not used "
        "commercially."))
    b.append(p(
        "Figure 93.2 shows the simplest scan: switches on one axis close in turn while data "
        "switches on the other decide which pixels fire. It wastes the properties that make plasma "
        "attractive, and a high-resolution display built this way would not be cost-competitive, "
        "because drivers are a large share of panel cost and driver cost rises with output "
        "voltage. The design aim is therefore the lowest possible operating voltage and the fewest "
        "driver chips, hence the most pixels per chip."))
    b.append(p(
        "For non-memory dc pixels one way to cut switch count is to sweep priming discharges along "
        "each row, as in Burroughs' self-scan circuitry [46,47]. NHK's pulse-memory scheme for its "
        "40 in. dc HDTV panel is now widely used [48]: high-frequency sustain exploits the residual "
        "charge pairs and metastables left by the previous discharge, so each pixel self-seeds "
        "with a population that depends on the time since the last discharge. Once the sustain "
        "train is applied the pixel holds its state until an address or erase pulse arrives. NHK "
        "uses an auxiliary anode to help the address access; Figure 93.16a is the block diagram "
        "and 93.16b the timing [48]. The pulses are dc, on-state pulses have larger gap voltages "
        "than erase pulses, and the timing is critical. Implementing the scheme needs display "
        "anode drivers, auxiliary anode drivers, cathode drivers, and an interface to decode the "
        "HDTV signal."))
    b.append(fig(16, "en"))
    b.append(p(
        "For ac panels the drivers need only supply address (write), sustain and erase pulses: no "
        "complex refresh scan, because a continuous sustain signal plus the pixel's own memory "
        "holds each pixel on or off. Addressing still requires well-timed waveforms on rows and "
        "columns so that the right voltage appears across the selected pixel without disturbing "
        "its neighbours; Reference 4 or 47 gives the detail."))
    b.append(p(
        "Grey scale comes from modulating the discharge current or, more practically, the duty "
        "cycle at fixed current. Amplitude modulation is little used because the discharge current "
        "is hard to control linearly; duty-cycle modulation works for both pulse-memory dc and ac "
        "panels but needs careful timing. Brightness is set by the fraction of each refresh cycle "
        "the pixel is on. At 50 kHz a sustain half cycle is 10 µs and the VUV emission lasts under "
        "1 µs, while visible emission persists much longer: the fastest phosphors reach 10% in "
        "about 5 ms, typical ones in 5–10 ms [50]. At a 40 ms frame (25 images/s), one-eighth "
        "brightness means 5 ms on and 35 ms off, spread through the frame by the timing circuit. "
        "NHK's 40 in. panel has 2<sup>8</sup> = 256 levels per colour, 16 million (256³) in total "
        "[48]."))

    b.append(h2("93.5 Color Plasma Flat Panel Displays"))
    b.append(h3("Color Pixel Structures"))
    b.append(p(
        "In a colour panel, photoluminescent phosphors supply the RGB primaries, so visible "
        "emission from the discharge itself must be suppressed. The usual approach is xenon as the "
        "minority species in the Penning mixture. Figure 93.17 shows NHK's 40 in. dc colour panel "
        "and Figure 93.6 Fujitsu's 21 in. ac panel; both use screen printing plus hard-mask or "
        "abrasive-resistant lithography for conductors, barriers and phosphors [51]. In NHK's "
        "honeycomb the fourth cell of each group carries a redundant green subpixel, compensating "
        "for the weaker green phosphor; Panasonic's honeycomb dc design puts a series resistor "
        "there instead [20], which complicates panel manufacture but simplifies the drive. In the "
        "Fujitsu opposed-electrode ac design the barrier ribs run between and parallel to the "
        "conductors on the rear plate, 100–150 µm tall, and both rib structures and honeycomb "
        "lattices are made from the same PbO thick-film dielectric that covers the conductors."))
    b.append(fig(17, "en"))

    b.append(h3("VUV Photon Production and Utilization"))
    b.append(p(
        "Neon–xenon and helium–xenon mixtures are both popular. Xenon's 12.3 eV ionisation energy "
        "lies below the lowest excited states of neon and helium (Figure 93.8), so accelerated "
        "electrons preferentially give their energy to xenon, and excited He or Ne transfers energy "
        "to xenon by Penning collisions. The neon red-orange emission is therefore suppressed as "
        "xenon rises: Fujitsu uses Ne–10% Xe [18], Photonics prefers a helium background where "
        "suppression needs somewhat less xenon [23]."))
    b.append(fig(18, "en"))
    b.append(p(
        "Xenon's tendency to fill its outer shell forms the dimer Xe₂*, whose states also appear "
        "in Figure 93.8 [52,53]; its radiative dissociation gives photons near 173 and 150 nm. "
        "Figure 93.18 shows the dimer dominating the VUV spectrum as xenon rises. Because glass "
        "absorbs VUV completely, the spectra were taken with opposed-electrode pixels inside a "
        "vacuum chamber filled with the mixture, the panel edges unsealed so the discharge could "
        "be viewed edge-on through a McPherson 0.2 m monochromator and a Princeton CCD "
        "multichannel analyser [34]; total pressure stayed at 53.3 kPa (400 torr). At low xenon the "
        "atomic 1s₄ and 1s₅ lines dominate at 147 nm and, much more weakly, 129 nm; Tachibana's "
        "laser-induced measurements follow the 1s₄ state in space and time [54]. Both lines suffer "
        "strong resonance absorption and re-emission, so measured intensities depend on path length "
        "and xenon partial pressure [55]. For Figure 93.18 the LiF entrance window sat 100–150 nm "
        "from the nearest discharges, roughly where the phosphor sits in an opposed-electrode ac "
        "colour pixel."))
    b.append(p(
        "Optimum charge-pair production per volt occurs at minority fractions as low as 0.1% "
        "(Figure 93.9), but colour pixels must optimise usable photons per watt while holding "
        "colour purity, so they run at 2–10% xenon. Figure 93.18 shows the consequence: more "
        "dimer, less atomic emission as energy flows to the lowest levels. Dimer dissociation is a "
        "three-body process, so momentum and energy conservation admit a continuum of solutions and "
        "the emission spans tens of nanometres. Dimer lines are not resonance-absorbed, so the "
        "measured intensity comes from every row in the spectrometer's line of sight — four rows "
        "for these data — whereas over 90% of the 147 nm intensity originates in the row nearest "
        "the window [34,55]."))

    b.append(h3("Phosphor Excitation and Emission"))
    b.append(p(
        "Conversion efficiency depends strongly on excitation wavelength, as Figure 93.19 shows for "
        "green phosphors against a sodium salicylate standard [50]; References 56 and 57 cover red, "
        "blue and other greens. Table 93.2 lists compositions, relative quantum efficiencies at the "
        "principal xenon lines and chromaticity coordinates. The efficiencies are relative, and a "
        "phosphor converting 8.4 eV photons to 2.3 eV photons has an absolute efficiency of only "
        "27%; two visible photons per VUV photon is possible in principle but no such phosphor "
        "exists [58]. Persistence matters too: most entries need 5–13 ms to fall to 10%, while a "
        "50 kHz sustain half cycle lasts 10 µs and the VUV burst is a fraction of that. Faster "
        "phosphors are being developed — Eu<sup>2+</sup> greens reaching 10% in 5–10 µs with good "
        "efficiency near 173 nm [50]."))
    hd2, rows2, cap2 = _table2("en")
    b.append(table(hd2, rows2, cap2))
    b.append(fig(19, "en"))

    b.append(h3("Color Plasma Display Lifetime Considerations"))
    b.append(p(
        "Phosphors must survive the discharge environment, and the degradation mechanisms are not "
        "well understood. Contamination of the discharge by phosphor material is a serious "
        "concern; modelling points to accumulated photon and metastable fluence as the main damage "
        "channel, with fringe fields and prolonged wall charge possibly adding ion bombardment "
        "[37]. Most ac panels coat the dielectric over the electrodes with MgO to boost the "
        "discharge, deposited by electron-beam evaporation as one of the last steps before sealing "
        "and gas fill. Without a mask the MgO also covers the phosphor: it protects the phosphor "
        "but attenuates the VUV reaching it. Figure 93.20 gives the transmission [34,60]: the 129 "
        "and 147 nm xenon lines lose nearly 95% through only 75 nm of MgO, while the dimer band "
        "near 173 nm keeps 30–50% through 200 and 75 nm films. Designers therefore balance "
        "discharge enhancement from MgO secondary emission, discharge loss from MgO absorption, "
        "and the process complexity — and hence the cost — of depositing it, against the ageing "
        "that MgO sputter erosion partly controls."))
    b.append(fig(20, "en"))

    b.append(h2("93.6 Inspection and Metrology"))
    b.append(p(
        "Panel manufacture borrows process steps from semiconductor manufacturing, but at much "
        "larger feature sizes — and over much larger distances across which integrity must hold. "
        "Knowing that the process is in control, or characterising the deviation from acceptable "
        "limits quickly, is essential to yield. Information is needed at several length scales: "
        "blanket depositions must be uniform from point to distant point, roughness must stay "
        "within limits, and composition and its spatial homogeneity must be measured."))
    b.append(p(
        "The three commercial profilers — CyberOptics, Zygo and Leitz — use laser or white-light "
        "triangulation and interferometry (Table 93.3) [61–63]. They suit patterned metallisation "
        "well, are not useful for opaque blanket layers, and cannot measure blanket metal "
        "thickness before patterning. CyberOptics is widely used in electronic packaging for its "
        "low-noise signal and would gain from better vertical resolution; Zygo resolves better "
        "vertically but has no real scanning; Leitz is built for unfinished LCD components. Both "
        "CyberOptics and Zygo offer several heads with different resolutions and fields of view, "
        "but Zygo's interference range in depth is limited, which may rule out tall features."))
    hd3, rows3, cap3 = _table3("en")
    b.append(table(hd3, rows3, cap3))
    b.append(p(
        "A useful laser system costs as little as $20,000; a full-featured one $100,000, most of "
        "it in the precision transport tables that move samples under fixed heads. Since the "
        "production line may already have such tables, or need only minor upgrades, the real cost "
        "of adding metrology can be far lower — and because heads are cheap, several fixed heads "
        "can be used to speed inspection up."))
    b.append(p(
        "Table 93.4 lists two advanced techniques. Neither was commercially available to the "
        "authors' knowledge, but both were in use at Sandia and look promising. Beta "
        "backscattering reads elemental composition from the energy spectrum of backscattered "
        "betas and has measured trace metal films over square metres in tokamaks [64]; with about "
        "100 pm depth resolution it could underpin a sensitive surface profiler. X-ray "
        "fluorescence, routinely done in air, gives thickness and composition, but light elements "
        "such as carbon — a possible phosphor binder burnout product — need vacuum because the "
        "x-rays are soft. A larger spot is useful where averaged information is wanted. Eddy "
        "current measurement may be the fast, reliable way to get blanket opaque metal thickness "
        "before patterning, to 10% on layers as thin as 1 µm."))
    hd4, rows4, cap4 = _table4("en")
    b.append(table(hd4, rows4, cap4))
    b.append(p(
        "Most quantitative tools have a limited field of view, so techniques are also needed to "
        "find visual defects quickly in blanket and patterned layers. Visual inspection equipment "
        "exists for LCDs — Minato Electronics, Advantest, ADS, Photon Dynamics and Teradyne all "
        "use CCDs and special algorithms for line and area defects — and plasma defects may look "
        "similar enough for it to work with adjustment, though such equipment is expensive."))
    b.append(p(
        "Everyone agrees more development is needed: real parts must be characterised on specific "
        "commercial equipment in production before the suitability of these tools can be judged, "
        "especially for harder measurements such as dielectric thickness over conductor lines. No "
        "single instrument covers all the dimensional and chemical requirements; several will be "
        "needed to inspect, characterise and control plasma display manufacturing."))

    b.append(h2("Translator's note"))
    b.append(note(
        "The source is a scan whose text layer loses µ, × and several Greek letters. Restored here: "
        "“100 mm” of gap is 100 µm, “25 mm” of PbO is 25 µm, “20 mm” conductors are 20 µm, the "
        "“5 mm” sheath is 5 µm, the “10 ms” sustain half cycle at 50 kHz is 10 µs, the “1 ms” VUV "
        "emission is 1 µs, the “1 mm” conductor layer in §93.6 is 1 µm, “852 ´ 480” is 852 × 480, "
        "“R = 500 kW” is 500 kΩ, “R = 5 MW” is 5 MΩ and the “1 MW, 3 pF” probe is 1 MΩ, 3 pF. In "
        "Tables 93.3 and 93.4 every thickness unit printed as “mm” is restored to µm, except the "
        "100 pm and 150 pm resolutions, which were already correct. Greek letters replaced by "
        "Latin ones: the secondary emission coefficient “g” is γ, the charge density “r(x)” in "
        "Poisson's equation is ρ(x), the Debye length “lD” is λ<sub>D</sub> and “hn” is "
        "<i>h</i>ν. Two numerical faults in the source: the caption of Figure 93.5 prints “3 Pa "
        "(~400 Torr)”, but 400 torr is 53.3 kPa, so the redrawn figure shows 3×10<sup>4</sup> Pa; "
        "and Table 93.1 prints Hitachi's contrast as “50.1”, evidently 50:1. One inconsistency is "
        "left alone: the four load lines of Figure 93.12 do not intersect the characteristic where "
        "<i>I</i> = (<i>V</i><sub>a</sub> − <i>V</i><sub>g</sub>)/<i>R</i> requires if the "
        "abscissa is the gap voltage, so the redrawn figure reproduces the printed geometry and "
        "says so rather than inventing new lines. Several formulae in Table 93.2 are mangled by "
        "the text layer (“LuBO8”, “ScBO8”, “GbBO3”, “Zn3SiO4”, “(Y,Gd)BO8”); they are printed here "
        "as the plausible compounds LuBO<sub>3</sub>, ScBO<sub>3</sub>, GdBO<sub>3</sub>, "
        "Zn<sub>2</sub>SiO<sub>4</sub> and (Y,Gd)BO<sub>3</sub>. The chapter has no Defining Terms "
        "block, so it adds nothing to the site glossary."))

    b.append(h2("References"))
    b.append(refs(_REFS))
    return "".join(b)


# ================================================================ BUILD
def build(lang):
    vi = lang == "vi"
    switch = ("%s%s/" % (BASE_EN, CSLUG)) if vi else ("%s%s/" % (BASE_VI, CSLUG))
    title = ("Chương 93 — %s · Sổ tay Đo lường, Thiết bị đo và Cảm biến" % TITLE_VI if vi
             else "Chapter 93 — %s · Measurement, Instrumentation and Sensors Handbook" % TITLE_EN)
    desc = ("Bản dịch tiếng Việt Chương 93 “Màn hình phẳng phóng điện plasma” của McGrath, "
            "Veerasingam, Moffatt và Campbell — lịch sử và cấu trúc điểm ảnh plasma, vật lý "
            "phóng điện và các quá trình Penning, tính chất điện của điểm ảnh một chiều và xoay "
            "chiều, mồi và địa chỉ, màn hình màu dùng photon VUV, và phép đo trong sản xuất, với "
            "20 hình, 4 bảng và 11 phương trình." if vi
            else
            "Companion to Chapter 93 of the CRC Measurement Handbook — plasma pixel history and "
            "structure, discharge physics and Penning processes, dc and ac pixel electrical "
            "properties, priming and addressing, colour panels driven by VUV photons, and "
            "production metrology, with 20 figures, 4 tables and 11 equations.")
    crumb = ('<a href="/vi/books/">Sách</a> · <a href="%s">Sổ tay Đo lường, Thiết bị đo và Cảm biến</a> · '
             'Chương 93' % BASE_VI if vi else
             '<a href="/books/">Books</a> · <a href="%s">Measurement, Instrumentation and Sensors '
             'Handbook</a> · Chapter 93' % BASE_EN)
    meta = ("Chương 93 · theo Ch93.pdf (CRC Press, 1999) · 20 hình, 4 bảng, 11 phương trình" if vi
            else "Chapter 93 · 20 figures, 4 tables, 11 equations")
    body = ('<main><article class="intranet-content reader"><div class="reader-hero">'
            '<div class="breadcrumb">%s</div><h1>%s</h1><p class="byline">%s</p>'
            '<div class="meta-line">%s</div></div><div class="prose">%s</div>%s</article></main>'
            % (crumb, TITLE_VI if vi else TITLE_EN, BYLINE if vi else BYLINE_EN, meta,
               body_vi() if vi else body_en(), chapter_nav(lang, 93)))
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
