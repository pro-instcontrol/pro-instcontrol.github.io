# -*- coding: utf-8 -*-
"""Handbook Chapter 89 — Electromagnetic Compatibility.

89.1 Grounding and Shielding in Industrial Electronic Systems
     Daryl Gerke and William Kimmel (Kimmel Gerke Associates, Ltd.)
89.2 EMI and EMC Test Methods
     Jeffrey P. Mills (Illinois Institute of Technology)

Writes the full Vietnamese translation and the English companion.
Figures: hb89fig.py (89.1–89.5). Tables 89.1–89.4 were all re-read from the
page rasters — the text extract loses every unit symbol. See the translator's
note at the head of the body for the full list of source defects.
Run:  python build/reader_hb_ch89.py
"""
import os

import hb89fig as F89
from reader_handbook import SLUG, head, header, footer
from chapter_nav import nav as chapter_nav

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSLUG = "ch89-electromagnetic-compatibility"
TITLE_EN = "Electromagnetic Compatibility"
TITLE_VI = "Tương thích điện từ"
BYLINE = "Daryl Gerke, William Kimmel và Jeffrey P. Mills"
BYLINE_EN = "Daryl Gerke, William Kimmel and Jeffrey P. Mills"
BASE_EN = "/books/read/%s/" % SLUG
BASE_VI = "/vi/books/read/%s/" % SLUG

FIGS = {1: F89.fig_89_1, 2: F89.fig_89_2, 3: F89.fig_89_3,
        4: F89.fig_89_4, 5: F89.fig_89_5}


def fig(num, lang="vi"):
    svg, cap_vi, cap_en, _av, _ae = FIGS[num]()
    return ('<figure class="figure" id="fig-89-%d">%s<figcaption class="figcap">%s</figcaption>'
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

    No `.frac` class exists in library.css and adding one would touch every
    reader page, so the styling stays inline (same helper as Chapter 90).
    """
    return ('<span style="display:inline-block;vertical-align:middle;text-align:center;'
            'max-width:100%%;font-size:%s;line-height:1.25;margin:0 0.2em">'
            '<span style="display:block;border-bottom:1.2px solid currentColor;'
            'padding:0 0.4em 2px">%s</span>'
            '<span style="display:block;padding:2px 0.4em 0">%s</span></span>'
            % (size, num, den))


def _sq(inner):
    """A square root: the radical sign followed by an overlined radicand."""
    return ('√<span style="border-top:1.2px solid currentColor;padding:0 .14em">%s</span>'
            % inner)


def _glossary(items):
    o = ['<dl class="glossary">']
    for term, body in items:
        o.append("<dt>%s</dt><dd>%s</dd>" % (term, body))
    o.append("</dl>")
    return "".join(o)


def _cap(t):
    return '<p style="font-size:.84rem;color:#888;font-style:italic">%s</p>' % t


# ================================================================ TABLES
def table_89_1(lang="vi"):
    if lang == "vi":
        hd = ("Loại", "Tần số", "Mức dòng điện điển hình", "Thời lượng điển hình")
        rows = [("Nguồn điện", "50/60 Hz", "10–1 000 A", "Giây hoặc phút"),
                ("Sét", "300 kHz", "100 000 A", "Hàng chục mili giây"),
                ("ESD", "300 MHz", "10–50 A", "Hàng chục nano giây"),
                ("EMI", "dc – ánh sáng", "µA–A", "Nano giây đến hàng năm")]
        cap = ("Bảng 89.1 · Một đường nối đất có thể làm việc trên một dải tần rất rộng. "
               "“dc – ánh sáng” là cách nói trong nguyên bản (dc–daylight), ý chỉ toàn bộ dải tần "
               "từ dòng một chiều tới ánh sáng.")
    else:
        hd = ("Type", "Frequency", "Typical Current Levels", "Typical Duration")
        rows = [("Power", "50/60 Hz", "10–1 000 A", "Seconds or minutes"),
                ("Lightning", "300 kHz", "100 000 A", "Tens of milliseconds"),
                ("ESD", "300 MHz", "10–50 A", "Tens of nanoseconds"),
                ("EMI", "dc–Daylight", "µA–A", "Nanoseconds to years")]
        cap = ("Table 89.1 · A ground may work over wide frequency ranges. "
               "“dc–Daylight” is the original's shorthand for the whole spectrum, from direct "
               "current to light.")
    body = "".join("<tr>%s</tr>" % "".join("<td>%s</td>" % c for c in r) for r in rows)
    return ('<div class="table-wrap"><table class="tbl"><thead><tr>%s</tr></thead><tbody>%s'
            '</tbody></table></div>%s'
            % ("".join("<th>%s</th>" % h for h in hd), body, _cap(cap)))


def table_89_2(lang="vi"):
    rows = [("10", "0,0033", "1,01", "0,006", "0,63", "63"),
            ("12", "0,0052", "1,05", "0,007", "0,66", "66"),
            ("14", "0,0083", "1,10", "0,007", "0,69", "69"),
            ("16", "0,0132", "1,15", "0,007", "0,72", "72"),
            ("18", "0,0209", "1,19", "0,007", "0,75", "75"),
            ("20", "0,0333", "1,24", "0,008", "0,78", "78"),
            ("22", "0,0530", "1,29", "0,009", "0,81", "81"),
            ("24", "0,0842", "1,33", "0,010", "0,84", "84"),
            ("26", "0,1339", "1,38", "0,012", "0,87", "87"),
            ("28", "0,1688", "1,40", "0,019", "0,88", "88"),
            ("30", "0,2129", "1,43", "0,022", "0,90", "90")]
    if lang == "vi":
        hd = ("Cỡ dây (AWG)", "Ω/m", "µH/m", "Z tại 10 kHz", "Z tại 1 MHz", "Z tại 100 MHz")
        cap = ("Bảng 89.2 · Tham số trở kháng của dây dài 10 cm. Hai cột đầu là giá trị trên mỗi "
               "mét; ba cột Z là trở kháng của đoạn dây dài đúng 10 cm ở tần số ghi trong tiêu đề "
               "cột. Số liệu giữ nguyên như bản in.")
    else:
        hd = ("Gage", "Ω/m", "µH/m", "Z @ 10 kHz", "Z @ 1 MHz", "Z @ 100 MHz")
        cap = ("Table 89.2 · Impedance parameters for 10-cm-length wires. The first two columns are "
               "per-metre values; the three Z columns are the impedance of exactly 10 cm of wire at "
               "the frequency named in the column head. Values as printed.")
    body = "".join("<tr>%s</tr>" % "".join("<td>%s</td>" % c for c in r) for r in rows)
    return ('<div class="table-wrap"><table class="tbl dense">'
            '<thead><tr>%s</tr></thead><tbody>%s</tbody></table></div>%s'
            % ("".join("<th>%s</th>" % h for h in hd), body, _cap(cap)))


def table_89_3(lang="vi"):
    rows = [("60 Hz", "172 µΩ", "17,2 µΩ", "1,83 µΩ"),
            ("1 kHz", "172", "17,5", "11,6"),
            ("10 kHz", "172", "33,5", "36,9"),
            ("100 kHz", "175", "116", "116"),
            ("1 MHz", "335", "369", "369"),
            ("10 MHz", "1,16 mΩ", "1,16 mΩ", "1,16 mΩ"),
            ("100 MHz", "3,69", "3,69", "3,69"),
            ("1000 MHz", "11,6", "11,6", "11,6")]
    if lang == "vi":
        hd1 = ("Tần số", "Độ dày")
        hd2 = ("0,1 mm", "1 mm", "10 mm")
        cap = ("Bảng 89.3 · Trị số trở kháng của mặt phẳng đất. Đơn vị đổi giữa bảng: từ 60 Hz đến "
               "1 MHz là micro-ôm (µΩ), từ 10 MHz trở lên là mili-ôm (mΩ) — nguyên bản chỉ in đơn "
               "vị ở ô đầu mỗi khối. Trở kháng tính bằng “ôm trên ô vuông”, tức trở kháng đo chéo "
               "qua một mảnh vuông của mặt phẳng.")
    else:
        hd1 = ("Frequency", "Thickness")
        hd2 = ("0.1 mm", "1 mm", "10 mm")
        cap = ("Table 89.3 · Impedance values for a ground plane. The unit changes inside the "
               "table: micro-ohms (µΩ) from 60 Hz to 1 MHz, milli-ohms (mΩ) from 10 MHz up — the "
               "original prints a unit only in the first cell of each block. Impedance is given in "
               "“ohms per square”, i.e. measured diagonally across a square of the plane.")
    body = "".join("<tr>%s</tr>" % "".join("<td>%s</td>" % c for c in r) for r in rows)
    head_rows = ('<tr><th rowspan="2">%s</th><th colspan="3" style="text-align:center">%s</th>'
                 '</tr><tr>%s</tr>'
                 % (hd1[0], hd1[1], "".join("<th>%s</th>" % h for h in hd2)))
    return ('<div class="table-wrap"><table class="tbl"><thead>%s</thead><tbody>%s</tbody></table>'
            '</div>%s' % (head_rows, body, _cap(cap)))


def table_89_4(lang="vi"):
    if lang == "vi":
        hd = ("Phương pháp", "Thiết bị cần có", "Không gian cần có", "Độ chính xác",
              "Ảnh hưởng bên ngoài", "Chi phí", "Ghi chú")
        rows = [
            ("Phòng thường", "Anten và máy thu", "Bán kính 3 hoặc 10 m quanh EUT",
             "Trung bình, phụ thuộc kết cấu phòng; ±20 dB",
             "Có thể mạnh, tuỳ vị trí", "Thấp nhất",
             "Thường chấp nhận được cho các phép thử sơ bộ"),
            ("Phòng có vỏ chắn", "Phòng có vỏ chắn, anten và máy thu",
             "Bán kính 4 đến 6 m quanh EUT", "Kém, ±30–40 dB do phản xạ",
             "Thường không", "Trung bình", "Dùng cho thử sơ bộ ở nơi nhiều nhiễu"),
            ("Buồng TEM", "Buồng TEM và máy thu", "1 đến 3 m³", "Rất tốt, ±10 dB",
             "Thường không", "Trung bình",
             "Không dùng được cho EUT lớn vì xuất hiện mode bậc cao"),
            ("Bãi trường mở", "Anten và máy thu",
             "Bãi trống 17 × 20 m, xung quanh không có công trình",
             "Rất tốt, thường ±6 dB", "Có thể mạnh, tuỳ vị trí",
             "Cao, do phải lo hạ tầng cho bãi thử (điện, thời tiết, …)",
             "Phương pháp thử chuẩn"),
            ("Buồng không vang có vỏ chắn", "Buồng không vang, anten và máy thu",
             "Bán kính 6 đến 15 m quanh EUT", "Rất tốt, ±10 dB",
             "Thường không", "Rất cao", "Dùng cho các phép thử chính xác ở nơi nhiều nhiễu"),
        ]
        cap = ("Bảng 89.4 · So sánh các phương pháp đo EMI. EUT là thiết bị cần đo "
               "(equipment under test).")
    else:
        hd = ("Method", "Equipment required", "Space required", "Accuracy",
              "Outside influence", "Cost", "Comments")
        rows = [
            ("Ordinary room", "Antenna and receiver", "3 or 10 m radius around EUT",
             "Medium, affected by structure; ±20 dB", "May be severe, depending on location",
             "Minimum", "Usually acceptable for preliminary tests"),
            ("Shielded room", "Shielded room, antenna, and receiver",
             "4 to 6 m radius around EUT", "Poor, ±30–40 dB due to reflections",
             "Usually none", "Moderate", "Use for preliminary tests in noisy areas"),
            ("TEM cell", "TEM cell and receiver", "1 to 3 m³", "Very good, ±10 dB",
             "Usually none", "Moderate", "Unusable for large EUT due to high-order modes"),
            ("Open field", "Antenna and receiver",
             "17 × 20 m open field with no nearby structures", "Excellent, usually ±6 dB",
             "May be severe, depending on location",
             "High, due to logistics of site (power, weather, etc.)", "Standard test method"),
            ("Shielded anechoic chamber", "Anechoic chamber, antenna, and receiver",
             "6 to 15 m radius around EUT", "Very good, ±10 dB", "Usually none", "Very high",
             "Use for accurate tests in noisy areas"),
        ]
        cap = ("Table 89.4 · Comparison of EMI measurement methods. EUT is the equipment under "
               "test.")
    cols = ('<colgroup><col style="width:14%"><col style="width:15%"><col style="width:15%">'
            '<col style="width:13%"><col style="width:13%"><col style="width:9%">'
            '<col style="width:21%"></colgroup>')
    body = "".join("<tr>%s</tr>" % "".join("<td>%s</td>" % c for c in r) for r in rows)
    return ('<div class="table-wrap"><table class="tbl dense" style="min-width:700px">%s'
            '<thead><tr>%s</tr></thead><tbody>%s</tbody></table></div>%s'
            % (cols, "".join("<th>%s</th>" % h for h in hd), body, _cap(cap)))


# ================================================================ GLOSSARY 89.1
_GLOSS1_VI = [
    ("Dẫn", "Năng lượng hay nhiễu lan truyền theo vật dẫn, chẳng hạn dây nguồn, dây nối đất hay "
            "dây giao diện tín hiệu."),
    ("EFT", "Quá độ nhanh điện (electrical fast transient); một chùm năng lượng tần số cao trên "
            "đường dây nguồn."),
    ("EMC", "Tương thích điện từ; trạng thái trong đó các thiết bị điện và điện tử cùng làm việc "
            "thành công khi ở gần nhau."),
    ("EMI", "Nhiễu điện từ; năng lượng điện không mong muốn có thể làm suy giảm chức năng của "
            "thiết bị điện tử."),
    ("Phát xạ", "Năng lượng điện phát ra từ một nguồn điện tử."),
    ("ESD", "Phóng tĩnh điện; sự phóng điện nhanh thường xảy ra sau khi điện tích tĩnh tích tụ."),
    ("EU", "Liên minh châu Âu; trước đây gọi là Cộng đồng châu Âu."),
    ("FCC", "Uỷ ban Truyền thông Liên bang (cơ quan chính phủ Hoa Kỳ)."),
    ("Đất", "Một đường về cho dòng điện."),
    ("Bức xạ", "Năng lượng hay nhiễu lan truyền bằng bức xạ điện từ trong không gian."),
    ("RFI", "Nhiễu tần số vô tuyến; thuật ngữ cũ để chỉ EMI, nay thường dùng cho nhiễu gây ra bởi "
            "một máy phát vô tuyến ở gần."),
    ("Vỏ chắn", "Một vỏ kim loại dùng để giảm mức điện trường hoặc từ trường."),
    ("Tính nhạy nhiễu", "Mức độ dễ bị tổn thương của thiết bị điện tử trước các nguồn nhiễu bên "
                        "ngoài; thường dùng thay cho “tính miễn nhiễm”."),
]

_GLOSS1_EN = [
    ("Conducted", "Energy or interference that is propagated by a conductor, such as power, "
                  "grounding, or signal interface wiring."),
    ("EFT", "Electrical fast transient; a high-frequency burst of energy on power wiring."),
    ("EMC", "Electromagnetic compatibility; the condition wherein electric and electronic "
            "equipment operate successfully in close proximity."),
    ("EMI", "Electromagnetic interference; unwanted electric energy that may impair the function "
            "of electronic equipment."),
    ("Emissions", "Electric energy emanating from an electronic source."),
    ("ESD", "Electrostatic discharge; the rapid discharge that often follows a buildup of static "
            "charge."),
    ("EU", "European Union; formerly called the European Community."),
    ("FCC", "Federal Communications Commission (U.S. government)."),
    ("Ground", "A return path for current."),
    ("Radiated", "Energy or interference that is propagated by electromagnetic radiation through "
                 "space."),
    ("RFI", "Radio frequency interference; an older term for EMI, now usually used to describe "
            "interference caused by a nearby radio transmitter."),
    ("Shield", "A metallic enclosure used to reduce electric or magnetic field levels."),
    ("Susceptibility", "Vulnerability of electronic equipment to external sources of interference; "
                       "often used interchangeably with immunity."),
]

# ================================================================ GLOSSARY 89.2
_GLOSS2_VI = [
    ("Hệ số anten", "Chiều dài hiệu dụng của anten, biểu diễn bằng decibel âm."),
    ("Balun", "Thiết bị giao diện dùng để cách ly một anten lưỡng cực (hay anten cân bằng khác) "
              "khỏi ảnh hưởng của một máy thu có một cực nối đất."),
    ("Ghép dẫn", "Ghép nhiễu do điện áp đặt lên một nguồn điện dùng chung."),
    ("Anten lưỡng cực", "Anten gồm hai thanh đồng trục, đường tiếp điện nối vào giữa hai thanh."),
    ("Trở kháng điểm tiếp điện", "Tỉ số giữa điện áp và dòng điện tại điểm tiếp điện (thường là "
                                 "điểm giữa) của anten."),
    ("Chiều dài hiệu dụng", "Tỉ số giữa điện áp đo được tại điểm tiếp điện của anten và cường độ "
                            "điện trường mà anten thu được."),
    ("Tương thích điện từ (EMC)", "Khả năng của hai hay nhiều thiết bị điện cùng làm việc đồng "
                                  "thời mà không gây nhiễu lẫn nhau."),
    ("Nhiễu điện từ (EMI)", "Mọi tác động không mong muốn của thiết bị điện này lên thiết bị điện "
                            "khác, do trường điện từ bức xạ hoặc do điện áp đặt lên một nguồn điện "
                            "dùng chung."),
    ("Phân cực elip", "Phân cực của một sóng điện từ gồm hai điện trường vuông góc với nhau và "
                      "lệch pha."),
    ("Phát xạ", "Trường hoặc điện áp dẫn do một thiết bị điện sinh ra."),
    ("Vùng xa", "Mọi vị trí cách nguồn điện trường hay từ trường một khoảng lớn hơn nhiều lần "
                "λ/2π, với λ là bước sóng ở tần số đang xét."),
    ("EMI giữa các hệ thống", "Nhiễu điện từ giữa hai hay nhiều hệ thống với nhau."),
    ("EMI trong một hệ thống", "Nhiễu điện từ giữa hai hay nhiều bộ phận của cùng một hệ thống."),
    ("Vùng gần", "Mọi vị trí cách nguồn điện trường hay từ trường một khoảng nhỏ hơn nhiều lần "
                 "λ/2π, với λ là bước sóng ở tần số đang xét."),
    ("Bãi thử trường mở", "Một địa điểm thử không có vật dẫn nào có thể ảnh hưởng tới trường điện "
                          "từ và làm sai lệch kết quả."),
    ("Phân cực", "Hướng của điện trường E của một sóng điện từ."),
    ("Mật độ công suất", "Công suất bức xạ trên một đơn vị diện tích tiết diện."),
    ("Ghép bức xạ", "Ghép nhiễu do trường điện, trường từ hay trường điện từ bức xạ."),
    ("Suy hao hiện trường", "Đại lượng đo mức độ trường điện từ tại một bãi thử bị xáo trộn bởi "
                            "những bất thường của môi trường, thu được bằng cách so sánh tính "
                            "toán với kết quả đo."),
    ("Tính nhạy nhiễu", "Mức độ một thiết bị điện bị ảnh hưởng bởi trường hoặc điện áp dẫn sinh "
                        "ra từ bên ngoài."),
    ("Buồng TEM", "Buồng thử tương đối nhỏ, trong đó trường điện từ được kiểm soát chính xác nhờ "
                  "hình học của buồng."),
]

_GLOSS2_EN = [
    ("Antenna factor", "Its effective length expressed in negative decibels."),
    ("Balun", "An interface device used to isolate a dipole or other balanced antenna from the "
              "effects of a receiver having one grounded terminal."),
    ("Conducted coupling", "Coupling due to voltages imposed on a shared power source."),
    ("Dipole antenna", "An antenna consisting of two collinear rods with the feed line connected "
                       "between them."),
    ("Driving-point impedance", "The ratio of voltage to current at the driving point (normally "
                                "the center) of an antenna."),
    ("Effective length", "The ratio of the voltage observed at the driving-point of an antenna to "
                         "the strength of its received electric field."),
    ("Electromagnetic compatibility (EMC)", "The capability of two or more electrical devices to "
                                            "operate simultaneously without mutual interference."),
    ("Electromagnetic interference (EMI)", "Any undesired effect of one electrical device upon "
                                           "another due to radiated electromagnetic fields or due "
                                           "to voltages imposed on a shared power source."),
    ("Elliptical polarization", "Polarization of an electromagnetic wave consisting of two "
                                "perpendicular electric fields of differing phase."),
    ("Emissions", "Fields or conducted voltages generated by an electrical device."),
    ("Far-field region", "Any location that is much farther than λ/2π from an electric or magnetic "
                         "field source, where λ is the wavelength at the frequency of concern."),
    ("Intersystem EMI", "Electromagnetic interference between two or more systems."),
    ("Intrasystem EMI", "Electromagnetic interference between two or more parts of the same "
                        "system."),
    ("Near-field region", "Any location that is much nearer than λ/2π to an electric or magnetic "
                          "field source, where λ is the wavelength at the frequency of concern."),
    ("Open-field site", "A test location free of any conductors which would affect electromagnetic "
                        "fields and taint the results."),
    ("Polarization", "The direction of the electric field, E, of an electromagnetic wave."),
    ("Power density", "Radiated power per unit of cross-sectional area."),
    ("Radiated coupling", "Coupling due to radiated electric, magnetic, or electromagnetic "
                          "fields."),
    ("Site attenuation", "A measure of the degree to which electromagnetic fields at a test site "
                         "are disturbed by environmental irregularities, obtained by comparing "
                         "calculations with measured experimental results."),
    ("Susceptibility", "The degree to which an electrical device is affected by externally "
                       "generated fields or conducted voltages."),
    ("Transverse electromagnetic (TEM) cell", "A relatively small test chamber in which fields can "
                                              "be accurately controlled by its geometric "
                                              "properties."),
]

# ================================================================ REFERENCES
_FURTHER1 = [
    "D.D. Gerke and W.D. Kimmel, <i>EDN's Designer's Guide to Electromagnetic Compatibility</i>, "
    "Newton, MA: Cahners Publishing, 1994. Giới thiệu cơ bản về các vấn đề EMC do chính các tác "
    "giả viết; rất phù hợp với kỹ sư không chuyên về EMC.",
    "W.D. Kimmel and D.D. Gerke, <i>Electromagnetic Compatibility in Medical Equipment</i>, "
    "New York: IEEE Press and Interpharm Press, 1995. Giới thiệu chi tiết về các vấn đề EMC trong "
    "thiết bị y tế, do chính các tác giả viết; áp dụng được cho phần lớn thiết bị điều khiển công "
    "nghiệp.",
    "W.D. Kimmel and D.D. Gerke, Internet World Wide Web Home Page [trực tuyến]. "
    "Địa chỉ http://www.emiguru.com, St. Paul, MN, 1996. Rất nhiều thông tin EMC hữu ích.",
    "R. Morrison, <i>Grounding and Shielding Techniques in Instrumentation</i>, New York: John "
    "Wiley &amp; Sons, 1986. Trình bày chi tiết cho mạch tương tự, nhấn vào các vấn đề tín hiệu "
    "mức thấp.",
    "H.W. Ott, <i>Noise Reduction Techniques in Electronic Systems</i>, New York: John Wiley &amp; "
    "Sons, 1988. Giới thiệu tốt về các vấn đề EMC, đặc biệt ở mức hệ thống và mạch tương tự.",
    "C.R. Paul, <i>Introduction to Electromagnetic Compatibility</i>, New York: John Wiley &amp; "
    "Sons, 1992. Viết như giáo trình đại học, khá nặng về phân tích nhưng bao quát rất tốt các vấn "
    "đề EMC.",
]

_FURTHER1_EN = [
    "D.D. Gerke and W.D. Kimmel, <i>EDN's Designer's Guide to Electromagnetic Compatibility</i>, "
    "Newton, MA: Cahners Publishing, 1994. Basic introduction on EMC issues written by the authors. "
    "Very good for non-EMC engineers.",
    "W.D. Kimmel and D.D. Gerke, <i>Electromagnetic Compatibility in Medical Equipment</i>, "
    "New York: IEEE Press and Interpharm Press, 1995. Detailed introduction to EMC issues in "
    "medical instrumentation, written by the authors. Applicable to most industrial control "
    "instrumentation.",
    "W.D. Kimmel and D.D. Gerke, Internet World Wide Web Home Page [online]. Available "
    "http://www.emiguru.com, St. Paul, MN, 1996. Wide range of useful EMC information.",
    "R. Morrison, <i>Grounding and Shielding Techniques in Instrumentation</i>, New York: John "
    "Wiley &amp; Sons, 1986. Detailed analog coverage, with emphasis on low-level signal issues.",
    "H.W. Ott, <i>Noise Reduction Techniques in Electronic Systems</i>, New York: John Wiley &amp; "
    "Sons, 1988. Good introduction to EMC issues, particularly system and analog issues.",
    "C.R. Paul, <i>Introduction to Electromagnetic Compatibility</i>, New York: John Wiley &amp; "
    "Sons, 1992. Written as a college text, quite analytical with very good coverage of EMC "
    "issues.",
]

_REFS2 = [
    "E.C. Jordan and K.G. Balmain, <i>Electromagnetic Waves and Radiating Systems</i>, 2nd ed., "
    "Englewood Cliffs, NJ: Prentice-Hall, 1968, 540–547.",
    "J.P. Mills, <i>Electromagnetic Interference Reduction in Electronic Systems</i>, Englewood "
    "Cliffs, NJ: Prentice-Hall, 1993, 232–233.",
    "M.L. Crawford, Generation of standard EM fields using TEM transmission cells, <i>IEEE Trans. "
    "Electromagn. Compat.</i>, EMC-16, 189–195, 1974.",
    "M.L. Crawford and J.L. Workman, Predicting free-space radiated emissions from electronic "
    "equipment using TEM cell and open-field site measurements, <i>IEEE Int. Symp. Electromagn. "
    "Compat.</i>, Baltimore, MD, Oct 7–9, IEEE, Piscataway, NJ, 1980, 80–85.",
    "Part 15 — Radio Frequency Devices, in <i>Code of Federal Regulations</i>, Volume 47: "
    "Telecommunications, Washington, D.C.: U.S. Government Printing Office, 1991, subpt. A-B.",
    "Methods of measurement of radio-noise emissions from low-voltage electrical and electronic "
    "equipment (ANSI C63.4-1988), American National Standards Institute (ANSI) Standards, New York: "
    "The Institute of Electrical and Electronics Engineers, 1989.",
]

_FURTHER2 = [
    "Guide for construction of open area test sites for performing radiated emission measurements "
    "(ANSI C63.7-1988), American National Standards Institute (ANSI) Standards, New York: The "
    "Institute of Electrical and Electronics Engineers, 1988.",
    "H.W. Ott, <i>Noise Reduction Techniques in Electronic Systems</i>, 2nd ed., New York: John "
    "Wiley &amp; Sons, 1988.",
    "W.H. Hayt, <i>Engineering Electromagnetics</i>, 5th ed., New York: McGraw-Hill, 1989.",
    "J.D. Kraus, <i>Electromagnetics</i>, 4th ed., New York, NY: McGraw-Hill, 1992.",
    "S. Ramo, J.R. Whinnery, and T. Van Duzer, <i>Fields and Waves in Communication Electronics</i>, "
    "2nd ed., New York: John Wiley &amp; Sons, 1984.",
]


# ================================================================ BODY — VI
def body_vi():
    b = []
    b.append(note(
        "<b>Ghi chú của người dịch.</b> Bản trích văn bản làm hỏng gần như toàn bộ ký hiệu toán và "
        "đơn vị, nên mọi công thức và cả bốn bảng đều được đọc lại trực tiếp từ trang in. Cụ thể: "
        "(89.2) in là <i>E</i>(V/m) = 5,5 √(PA)/<i>d</i>; bản trích mất cả dấu căn lẫn phép chia "
        "nên thành “5.5 PA d”. (89.3) in là SE (dB) = <i>R</i>(dB) + <i>A</i>(dB); bản trích đảo "
        "thành “SE dB () = RA () dB + () dB”. (89.1) in là <i>f</i> = 1/(π<i>t</i><sub>r</sub>), "
        "và câu ngay sau đó viết thời gian lên của sét là <b>1 µs</b> — bản trích ghi nhầm thành "
        "“1 ms”, trong khi 1/(π × 1 µs) ≈ 318 kHz mới đúng là con số 300 kHz mà tác giả dẫn. Các "
        "ký hiệu bị thay bằng chữ cái Latinh: Ω (ôm) thành “W”, µ thành “m”, π thành “p”, λ thành "
        "“l”, ε thành “e”, × thành “´”, ≈ thành “»”, và mọi chỉ số trên/dưới đều bị "
        "kéo xuống dòng. Vì vậy “377 W” là 377 Ω, “64 W” là 64 Ω, “1 to 10 W” là 1 đến 10 Ω, "
        "“1 to 100 mH” là 1 đến 100 µH, “0.4p (approximately 1.257) mT·m/A” là 0,4π µT·m/A, "
        "“10–8/3” là 10<sup>−8</sup>/3, “3·108/f” là 3 × 10<sup>8</sup>/<i>f</i>, và “l/2p” là "
        "λ/2π. Bảng 89.3 đổi đơn vị giữa bảng — µΩ ở nửa trên, mΩ ở nửa dưới — nhưng nguyên bản "
        "chỉ in đơn vị ở ô đầu mỗi khối, nên bản trích biến cả bảng thành “mW”. Bảng 89.2 có tiêu "
        "đề “dây dài 10 cm” nhưng hai cột đầu lại là giá trị trên mỗi mét; ba cột Z mới là trở "
        "kháng của đoạn 10 cm. Ba lỗi văn bản khác được giữ nguyên như bản in: chú thích Hình 89.1 "
        "viết “All three elements must be necessary” (đúng ra là “must be present”), mục 89.2 viết "
        "“superhetrodyne” (đúng là <i>superheterodyne</i>) và “It is expected that that wireless "
        "LANs” (lặp “that”). Ngoài ra, mục 89.1 nói khoảng cách “lớn hơn 1/6 bước sóng”, còn mục "
        "89.2 nói λ/2π ≈ λ/6 — hai cách viết của cùng một ngưỡng."))

    # ------------------------------------------------------------ 89.1
    b.append(h2("89.1 Nối đất và che chắn trong hệ điện tử công nghiệp",
                "Grounding and Shielding in Industrial Electronic Systems"))
    b.append(p('<span style="color:#777">Daryl Gerke và William Kimmel — Kimmel Gerke Associates, '
               'Ltd.</span>'))

    b.append(p(
        "Tương thích điện từ (EMC) là yếu tố then chốt để hệ thống công nghiệp vận hành thành "
        "công. Do hàm lượng điện tử trong hầu hết các bộ điều khiển công nghiệp tăng lên, các vấn "
        "đề nhiễu điện từ (EMI) đã gia tăng mạnh trong những năm gần đây. Hai chìa khoá để thành "
        "công về EMC là nối đất và che chắn. Mục này bàn ngắn gọn cách triển khai hai chiến lược "
        "EMC then chốt đó, đồng thời giới thiệu tổng quát về các vấn đề EMI trong hệ điện tử công "
        "nghiệp ngày nay. Trọng tâm là những hiểu biết và ý tưởng thực tiễn rút ra từ việc xử lý "
        "rất nhiều sự cố điều khiển công nghiệp."))

    b.append(h3("Hiểu các vấn đề EMI", "Understanding EMI Problems"))
    b.append(p("Dưới đây là ba nhận xét chung khi xử lý các vấn đề EMI trong điện tử công nghiệp."))
    b.append(p(
        "<b>Thứ nhất, môi trường công nghiệp rất khắc nghiệt.</b> Các mối đe doạ EMI chính là biến "
        "động nguồn, nhiễu tần số vô tuyến (RFI) và phóng tĩnh điện (ESD). Ngoài ra, các mạch cảm "
        "biến tương tự còn thường xuyên bị vòng đất 50/60 Hz quấy rầy. Điện tử công nghiệp cần "
        "được chăm sóc EMC nhiều hơn phần lớn thiết bị điện tử thương mại, thậm chí nhiều hơn "
        "không ít hệ thống quân sự."))
    b.append(p(
        "<b>Thứ hai, điện tử thường chỉ đóng vai trò thứ yếu trong hệ thống.</b> Khác với hệ thống "
        "máy tính, nơi điện tử là công nghệ lõi, điện tử công nghiệp thường được dùng để hỗ trợ một "
        "công nghệ khác, chẳng hạn chức năng hoá học, cơ khí hay công nghệ quá trình. Điều này tạo "
        "ra những thách thức EMC khi tích hợp phần điện tử với các công nghệ phi điện tử."))
    b.append(p(
        "<b>Thứ ba, các quy định và luật lệ về EMC cuối cùng đã bắt kịp điện tử công nghiệp.</b> "
        "Trong nhiều năm, điện tử công nghiệp được miễn trừ các quy định EMC bắt buộc, nên trừ khi "
        "xảy ra sự cố thật sự, EMC thường bị bỏ qua. Với các chỉ thị EMC của Liên minh châu Âu "
        "(EU) nay đã có hiệu lực, điện tử công nghiệp không còn được miễn trừ nữa."))

    b.append(p("<b>Ba loại vấn đề.</b> Vấn đề EMC có ba mặt: phát xạ, tính nhạy nhiễu (còn gọi là "
               "tính miễn nhiễm) và tự tương thích. Phát xạ phát sinh bên trong thiết bị và có thể "
               "quấy rối thiết bị khác ở gần. Ở chiều ngược lại, năng lượng bên ngoài có thể quấy "
               "rối thiết bị, dẫn tới tính nhạy nhiễu (hay thiếu tính miễn nhiễm). Cuối cùng, năng "
               "lượng bên trong hệ thống có thể gây nhiễu các mạch nội bộ khác, tạo ra vấn đề tự "
               "tương thích."))
    b.append(p(
        "Các vấn đề về cả phát xạ lẫn tính nhạy nhiễu đã dẫn tới việc ban hành quy định EMC. Hai "
        "bộ quy định nổi tiếng nhất là quy định của FCC (Uỷ ban Truyền thông Liên bang) về phát xạ "
        "ở Hoa Kỳ, và quy định của EU về cả phát xạ lẫn tính miễn nhiễm ở châu Âu. Các bộ điều "
        "khiển công nghiệp xưa nay vẫn được miễn trừ quy định của FCC, nhưng không được miễn trừ "
        "quy định của EU — bộ quy định trở thành bắt buộc từ tháng 1 năm 1996."))

    b.append(p("<b>Bốn mối đe doạ EMC chính.</b> Phần lớn các vấn đề EMC công nghiệp rơi vào một "
               "trong bốn nhóm: phát xạ, biến động nguồn, nhiễu tần số vô tuyến và phóng tĩnh điện. "
               "Trước đây, hệ thống công nghiệp thường chỉ quan tâm tới biến động nguồn; ngày nay "
               "cả bốn mối đe doạ đều phải được tính đến."))
    b.append(p(
        "<b><i>Phát xạ.</i></b> Phát xạ là năng lượng điện phát sinh bên trong thiết bị và có thể "
        "gây nhiễu thiết bị khác. Mối quan tâm hàng đầu của loại đe doạ này là làm nhiễu máy thu "
        "truyền hình gần đó — đây chính là cơ sở của các quy định phát xạ EU hiện nay mang tính "
        "bắt buộc. Tuy vậy, các vấn đề phát xạ giữa những hệ điện tử công nghiệp với nhau lại hiếm "
        "khi xảy ra. Dù về nguyên tắc có thể gây nhiễu bất kỳ thiết bị nào ở gần, phần lớn điện tử "
        "công nghiệp chỉ sinh ra một lượng nhiễu dẫn và nhiễu bức xạ rất nhỏ, thấp hơn nhiều so "
        "với ngưỡng gây rối loạn của mạch số hay mạch tương tự."))
    b.append(p(
        "Phát xạ được xử lý tốt nhất ngay ở khâu thiết kế thiết bị. Các chiến lược gồm kỹ thuật "
        "thiết kế bảng mạch in, lọc tần số cao trên các giao diện nguồn và tín hiệu, cáp có vỏ "
        "chắn, và vỏ hộp che chắn. Các biện pháp khắc phục tại hiện trường thường chỉ giới hạn ở "
        "cáp hoặc vỏ hộp có che chắn, bộ lọc lắp thêm, và kẹp ferrit trên cáp."))
    b.append(p(
        "<b><i>Biến động nguồn.</i></b> Biến động nguồn có nhiều dạng, từ xung quá độ ngắn đến sụt "
        "áp kéo dài, tăng áp, hoặc mất điện hoàn toàn. Ba mối đe doạ nguồn nghiêm trọng nhất với "
        "điều khiển công nghiệp là xung quá độ, sụt áp và mất điện. Dòng điện 50/60 Hz lạc đường "
        "cũng có thể gây rắc rối cho các mạch tương tự nhạy, đặc biệt do vòng đất (sẽ bàn ở dưới). "
        "Các biến động nguồn khác như thay đổi tần số hay dạng sóng thường ít ảnh hưởng tới hệ "
        "điện tử."))
    b.append(p(
        "Biến động nguồn rất phổ biến trong môi trường công nghiệp. Vì vậy, phần lớn hệ thống công "
        "nghiệp khá vững trước mối đe doạ này, ít nhất là ở tần số thấp. Các mối đe doạ tần số "
        "cao, chẳng hạn xung quá độ nhanh hay nhiễu RF trên đường dây nguồn, vẫn có thể gây rắc "
        "rối. Các phép thử của EU mô phỏng những mối đe doạ này bằng thử nghiệm EFT (quá độ nhanh "
        "điện) và thử nghiệm bơm RF."))
    b.append(p(
        "Phần lớn biến động nguồn là do thiết bị ở gần gây ra chứ không phải từ nguồn bên ngoài. "
        "(Một ngoại lệ quan trọng là sét, có thể tạo ra những xung áp và xung dòng rất khó chịu.) "
        "Các giải pháp cho biến động nguồn gồm nối đất, bộ lọc nguồn, thiết bị bảo vệ chống quá độ "
        "và, trong trường hợp cực đoan, hệ thống nguồn liên tục (UPS)."))
    b.append(p(
        "<b><i>Nhiễu tần số vô tuyến.</i></b> RFI liên quan tới các mối đe doạ trong dải RF. RFI "
        "khá phổ biến trong môi trường công nghiệp và nhiều khả năng sẽ còn tệ hơn khi bộ đàm cầm "
        "tay và điện thoại di động trở nên phổ dụng. Có thể dự đoán rằng mạng cục bộ không dây "
        "(wireless LAN) cũng sẽ mang lại những thách thức EMI thú vị. Đã có trường hợp bộ đàm cầm "
        "tay bị cấm sử dụng vì gây nhiễu EMI lặp đi lặp lại với điện tử công nghiệp."))
    b.append(p(
        "Hoá ra chiếc bộ đàm cầm tay ở gần là mối đe doạ lớn hơn nhiều so với một đài phát thanh "
        "thương mại lớn cách xa vài cây số. Một đại lượng đo quan trọng là cường độ điện trường, "
        "đo bằng “vôn trên mét”. Đại lượng này phụ thuộc cả công suất máy phát lẫn khoảng cách tới "
        "anten, và có thể tính nhanh bằng công thức:"))
    b.append(eq("<i>E</i>(V/m) = 5,5 " + _frac(_sq("PA"), "<i>d</i>"), "89.2"))
    b.append(p(
        "trong đó <i>P</i> là công suất máy phát tính bằng oát, <i>A</i> là hệ số khuếch đại của "
        "anten, và <i>d</i> là khoảng cách tới anten tính bằng mét. Ví dụ, điện trường từ một máy "
        "phát 1 W với anten có hệ số khuếch đại bằng không, ở khoảng cách 1 m, là khoảng 5 V/m; "
        "trong khi điện trường từ một đài phát 10 000 W ở khoảng cách 1 km chỉ khoảng 0,5 V/m. Vì "
        "thiết bị không được bảo vệ có thể hỏng trong dải 0,1 đến 1 V/m, các sự cố hoàn toàn có "
        "thể xảy ra. Giới hạn 10 V/m của EU cho môi trường “công nghiệp nặng” rõ ràng nhằm bảo vệ "
        "chống lại chính chiếc bộ đàm cầm tay ở gần."))
    b.append(p(
        "Các giải pháp cho vấn đề RFI gồm lọc tần số cao trên cáp nguồn và cáp tín hiệu, cáp có vỏ "
        "chắn, và vỏ hộp che chắn. Mạch tương tự đặc biệt dễ bị RFI, nên thường cần bảo vệ thêm. "
        "Cũng đừng quên biện pháp cấm máy phát vô tuyến trong phạm vi lân cận. Giữ khoảng cách 3 "
        "đến 10 m thường đã đủ để giải quyết vấn đề."))
    b.append(p(
        "<b><i>Phóng tĩnh điện.</i></b> ESD là sự phóng điện đột ngột có thể xảy ra sau khi điện "
        "tích tụ dần. ESD thường gắn với con người (chạm vào bảng điều khiển hay bàn phím), nhưng "
        "ESD cũng có thể do phóng điện hồ quang bên trong thiết bị, khi giấy, nhựa v.v. chuyển "
        "động. Các vấn đề ESD bên trong thiết bị đang gia tăng trong hệ thống công nghiệp."))
    b.append(p(
        "Tuy điện tích có thể tích tụ trong thời gian dài (hàng giây, thậm chí hàng phút), sự "
        "phóng điện gần như tức thời (cỡ nano giây hoặc ngắn hơn). Hơn nữa, thủ phạm là dòng điện "
        "đột ngột chứ không phải điện áp. Hiệu ứng này hơi giống việc vỡ đập: dòng ESD giống như "
        "nước chảy xuống núi, phá huỷ mọi thứ trên đường đi. May mắn là xung dòng không kéo dài "
        "quá lâu, nên mức năng lượng không cao. Tuy vậy, mức đó vẫn đủ để làm hỏng hoặc làm rối "
        "loạn các linh kiện điện tử."))
    b.append(p(
        "Sự phóng điện cực nhanh tạo ra các tần số rất cao, lên tới dải UHF. Với 1 ns, độ rộng "
        "băng của xung quá độ đã vượt 300 MHz. Vì thế, không cần một cú “sét đánh trực tiếp” bằng "
        "ESD cũng đủ gây sự cố. Những rối loạn do ESD ở cách xa 5 đến 10 m không phải là hiếm, do "
        "trường điện từ rất mạnh gắn với biến cố ESD. Những vấn đề này đặc biệt khó lần ra, vì "
        "biến cố ESD có thể đang xảy ra trên một thiết bị khác."))
    b.append(p(
        "Các giải pháp cho vấn đề ESD gồm bảo vệ chống quá độ, lọc tần số cao, che chắn cáp và che "
        "chắn vỏ hộp. Nối đất là yếu tố rất quan trọng trong bảo vệ ESD, nhưng phải được thiết kế "
        "cho tần số cao. Vì ESD nhiều khi gây ra sự cố “reset”, nên chú ý thêm cho các mạch reset "
        "của vi xử lý là rất có lợi."))

    b.append(p("<b>Nguồn, đường dẫn và đối tượng thu.</b> Một khó khăn thường gặp với vấn đề EMI là "
               "thu thập và tổ chức dữ liệu, đặc biệt khi lần tìm sự cố EMI tại hiện trường. Mô "
               "hình “nguồn – đường – đối tượng thu” được dùng phổ biến. Nói đơn giản, mọi vấn đề "
               "EMI đều cần ba yếu tố:"))
    b.append(ul(["phải có một nguồn năng lượng;",
                 "phải có một đối tượng thu bị năng lượng đó làm rối loạn;",
                 "phải có một đường ghép nhiễu giữa nguồn và đối tượng thu."]))
    b.append(p(
        "Cả ba yếu tố phải cùng tồn tại; thiếu bất kỳ yếu tố nào thì không có vấn đề EMI. Có khi "
        "xác định được cả ba, có khi chỉ đoán được. Tuy nghe có vẻ đơn giản, đây là công cụ hữu "
        "ích để sắp xếp thông tin về EMI."))
    b.append(p(
        "Hình 89.1 minh hoạ mô hình này, kèm những nguồn, đường dẫn và đối tượng thu điển hình. "
        "Một số nguồn khả dĩ đã được bàn tới: phát xạ từ mạch số, ESD, RFI từ máy phát thông tin, "
        "và biến động nguồn (kể cả sét). Một số đối tượng thu cũng đã được nêu: máy thu thông tin, "
        "điện tử tương tự và điện tử số. Cần để ý hai loại đường dẫn: bức xạ và dẫn. Trong cả hai "
        "trường hợp, mục tiêu là chặn năng lượng không mong muốn không cho tới đối tượng thu — "
        "bằng che chắn (với đường bức xạ) và bằng lọc (với đường dẫn)."))
    b.append(fig(1))

    b.append(h3("Nối đất", "Grounding"))
    b.append(p(
        "Nối đất có lẽ là khía cạnh quan trọng nhất nhưng cũng ít được hiểu nhất của việc kiểm "
        "soát EMI. Mọi mạch đều được nối vào một loại “đất” nào đó, nên mọi mạch đều chịu ảnh "
        "hưởng của các vấn đề nối đất trong EMC."))

    b.append(p("<b>Đất là gì?</b> Vấn đề lớn của chủ đề nối đất là sự mơ hồ của thuật ngữ. Định "
               "nghĩa ưa thích của chúng tôi là định nghĩa phổ biến trong cộng đồng EMC: đất đơn "
               "giản chỉ là một đường về cho dòng điện chạy. Những dòng này có thể là dòng chủ định "
               "hoặc không chủ định. Các dòng không chủ định thường được gọi là “đường đất lén” "
               "(sneak ground) và có thể gây ra nhiều loại sự cố EMI. Cuối cùng, ở tần số cao, "
               "thậm chí không cần một mối nối vật lý, vì điện dung hoặc điện cảm ký sinh có thể "
               "tạo thành một phần của đường đất."))

    b.append(p("<b>Các loại đất khác nhau.</b> Đất được dùng vì nhiều lý do: nguồn điện, an toàn, "
               "sét, EMI và ESD. Tuy có thể chia sẻ chức năng chung, các loại đất này khác nhau "
               "rất nhiều về tần số và biên độ dòng điện. Nhận ra những khác biệt then chốt đó là "
               "chìa khoá để hiểu các vấn đề nối đất."))
    b.append(p(
        "Bảng 89.1 cho thấy yêu cầu về tần số và biên độ của một số loại đất. Cần lưu ý rằng đất "
        "nguồn và đất an toàn phải chịu dòng lớn, nhưng chỉ ở tần số thấp. Ngược lại, đất cho EMI "
        "và ESD thường phải chịu tần số cao với mức dòng tương đối nhỏ. Đất chống sét phải chịu "
        "dòng cực lớn, nhưng ở tần số vừa phải."))
    b.append(table_89_1("vi"))
    b.append(p(
        "Tần số của các biến cố quá độ được tính bằng công thức <i>f</i> = 1/(π<i>t</i><sub>r</sub>), "
        "trong đó <i>f</i> là tần số tương đương và <i>t</i><sub>r</sub> là thời gian lên/xuống của "
        "xung. Hệ thức này có thể suy ra bằng phân tích Fourier. Ví dụ, ESD có tần số tương đương "
        "khoảng 300 MHz ứng với thời gian lên điển hình 1 ns, còn sét có tần số tương đương khoảng "
        "300 kHz ứng với thời gian lên 1 µs."))
    b.append(eq("<i>f</i> = " + _frac("1", "π<i>t</i><sub>r</sub>"), "89.1"))
    b.append(p(
        "Cần lưu ý rằng trong tất cả các loại đất nêu trên, chỉ một loại thật sự cần nối với đất "
        "tự nhiên (Earth): đó là đất chống sét. Các loại đất khác có thể được nối với đất tự nhiên "
        "theo quy ước hoặc vì lý do an toàn. Ví dụ, dây trung tính nguồn được nối với đất tự nhiên "
        "ở nhiều nơi trên thế giới để hỗ trợ chống sét. Ngược lại, ở nhiều nơi khác, hệ thống điện "
        "lại không có nối đất tự nhiên. Khi làm việc với nối đất nguồn, quy chuẩn an toàn địa "
        "phương sẽ quyết định phương pháp nối đất tự nhiên thích hợp."))

    b.append(p("<b>Trở kháng của đất.</b> Một đường đất tốt phải có trở kháng đủ thấp để giảm "
               "thiểu sụt áp trên hệ thống đất, và phải là đường ưu tiên cho dòng điện chạy qua. "
               "Chìa khoá thành công là duy trì trở kháng thấp đó trên toàn bộ dải tần quan tâm. "
               "Điểm này không thể nhấn mạnh quá mức. Phần lớn sự cố nối đất trong EMC là do dùng "
               "sai cách tiếp cận cho một dải tần nhất định."))
    b.append(p(
        "Trở kháng của một dây dẫn đất gồm cả điện trở lẫn điện cảm (<i>Z</i> = <i>R</i> + "
        "jω<i>L</i>). Ở tần số từ một chiều tới khoảng 10 kHz, điện trở là yếu tố chính, nên dây "
        "cỡ lớn thường được dùng làm dây đất tần số thấp. Tuy nhiên, khi tần số tăng lên, điện cảm "
        "trở thành yếu tố giới hạn trở kháng. Theo quy tắc kinh nghiệm, điện cảm của dây tròn vào "
        "khoảng 10 nH/cm."))
    b.append(p(
        "Bảng 89.2 cho biết điện trở, điện cảm và điện kháng cảm ứng của các cỡ dây điển hình dùng "
        "trong mạch nguồn và mạch tín hiệu của thiết bị đo. Rõ ràng là ở tần số nguồn và tần số âm "
        "thanh (từ một chiều đến 10 kHz), điện trở là yếu tố trội trong trở kháng đất. Vậy ở tần số "
        "thấp, hãy tìm cách giảm điện trở, thường là dùng dây lớn hơn. Ở tần số trên dải âm thanh "
        "(> 10 kHz), điện cảm trở thành yếu tố trội. Vậy ở tần số cao, hãy tìm cách giảm điện cảm "
        "của đường đất; điều này đạt được bằng mặt phẳng đất, lưới đất và dây dẹt."))
    b.append(table_89_2("vi"))
    b.append(p(
        "Bảng 89.3 cho trị số trở kháng của mặt phẳng đất đặc ở các tần số khác nhau. Ở đây trở "
        "kháng tính bằng “ôm trên ô vuông”, tức trở kháng đo chéo qua một bề mặt. So sánh bảng này "
        "với Bảng 89.2 có thể thấy rằng ở tần số cao (chẳng hạn 100 MHz), trở kháng của mặt phẳng "
        "đất có thể thấp hơn trở kháng của một sợi dây vài bậc độ lớn. Hơn nữa, ở tần số cao, độ "
        "dày không còn là yếu tố, vì trở kháng bị giới hạn bởi hiệu ứng bề mặt."))
    b.append(table_89_3("vi"))

    b.append(p("<b>Cấu trúc nối đất.</b> Sau khi đã xem xét trở kháng đất theo tần số, ta có thể "
               "bàn tới cấu trúc nối đất theo tần số. Những giới hạn về trở kháng dẫn tới hai cách "
               "tiếp cận nối đất tuỳ theo tần số. Với các vấn đề tần số thấp (từ một chiều đến "
               "10 kHz), nên dùng nối đất một điểm; còn ở tần số cao (trên 10 kHz), nối đất nhiều "
               "điểm cùng với mặt phẳng hoặc lưới đất trở thành cách tiếp cận được ưa dùng."))
    b.append(p(
        "Sự phân đôi này thường gây lúng túng với điều khiển công nghiệp, nhưng có thể giảm bớt "
        "bằng cách xác định tần số của mối đe doạ EMI rồi chọn cách nối đất thích hợp. Trong nhiều "
        "trường hợp, có thể phải dùng đồng thời cả hai cách, dẫn tới “nối đất lai” — dùng tụ điện "
        "và cuộn cảm để thay đổi cấu trúc nối đất theo tần số."))
    b.append(p(
        "<b><i>Nối đất một điểm.</i></b> Ở tần số thấp, người ta thường có thể điều khiển dòng "
        "điện bằng dây dẫn. Vì điện cảm nhỏ, yếu tố giới hạn chính là điện trở của dây. Hơn nữa, "
        "ghép điện dung từ dây đất sang các dây hay bề mặt lân cận là nhỏ, nên gần như toàn bộ "
        "dòng điện đi theo đường dây."))
    b.append(p(
        "Hình 89.2 cho thấy một sơ đồ nối đất công nghiệp điển hình. Hãy để ý điều gì xảy ra nếu "
        "hệ thống được nối đất ở cả hai đầu. Mọi dòng nhiễu chung trong đường đất chung nay được "
        "ghép vào mạch qua “trở kháng đất chung”. Kết quả là “vòng đất” đáng sợ, sẽ bàn ngay sau "
        "đây. Nối đất một điểm loại bỏ vòng đất, vì không còn trở kháng chung nào để sinh ra điện "
        "áp cách chung. Vì vậy, nối đất một điểm là cách rất thực tế để hạn chế các vấn đề “nhiễu "
        "đất” khi mối đe doạ là dòng đất tần số thấp. Đây là tình huống rất điển hình của dòng "
        "50/60 Hz lọt vào các mạch thiết bị đo tương tự nhạy."))
    b.append(fig(2))
    b.append(p(
        "<b><i>Nối đất nhiều điểm.</i></b> Đáng tiếc là khi tần số tăng, điện kháng cảm ứng của "
        "dây dẫn cũng tăng. Đồng thời, điện kháng điện dung ký sinh sang các dây hay bề mặt lân "
        "cận giảm xuống, và chẳng bao lâu thì không còn có thể duy trì một đường đất một điểm thật "
        "sự, dù hệ thống có được đi dây theo kiểu đó. Lựa chọn duy nhất còn lại là hạ trở kháng "
        "của đường đất, và điều đó đạt được bằng mặt phẳng hoặc lưới đất. Hơn nữa, các mối nối một "
        "điểm vào lưới hay mặt phẳng thường không đủ vì hiệu ứng đường truyền, nên nối đất nhiều "
        "điểm (kết hợp với mặt phẳng/lưới) trở thành cách tiếp cận ưu tiên trên 10 kHz."))
    b.append(p(
        "Lưới đất đã được dùng nhiều năm trong các phòng máy tính và đang được dùng ngày càng "
        "nhiều trong các cơ sở công nghiệp. Khoảng cách khuyến nghị giữa các dây lưới là không quá "
        "1/20 bước sóng ở tần số cao nhất cần xét. Lưới trong phòng máy tính thường có bước khoảng "
        "0,7 m (khoảng 2 ft), đáp ứng tiêu chí này từ một chiều tới khoảng 25 MHz. Điều này rất có "
        "lợi khi xử lý nhiễu đất do sét và các xung quá độ nguồn khác — những hiện tượng thường ở "
        "dải 1 MHz trở xuống. Nhưng lưới bước 0,7 m không giúp gì với các vấn đề vô tuyến VHF/UHF "
        "hay ESD. Trong những trường hợp đó, có thể cần tới các bề mặt đặc."))
    b.append(p(
        "<b><i>Vòng đất.</i></b> Vòng đất là vấn đề nghiêm trọng với các mạch tương tự nhạy phải "
        "đối mặt với mối đe doạ tần số thấp. Ở tần số cao, vòng đất nói chung không gây đe doạ "
        "nghiêm trọng nếu đã có các biện pháp phòng ngừa tần số cao thích hợp khi thiết kế hệ "
        "thống nối đất."))
    b.append(p(
        "Vòng đất tồn tại mỗi khi có nhiều đường đất. Dòng điện không mong muốn có thể đi theo "
        "những đường không mong muốn, tạo ra điện áp nhiễu không mong muốn ở những nơi không mong "
        "muốn. Vấn đề đặc biệt gay gắt với hệ tương tự nhạy, nơi chỉ vài microvôn cũng đủ làm "
        "nhiễu tín hiệu mong muốn. Một ví dụ kinh điển là dòng đất 60 Hz gây ù trong hệ âm thanh."))
    b.append(p(
        "Hình 89.2 cho thấy một vấn đề vòng đất điển hình. Cần để ý rằng phải hội đủ ba điều kiện "
        "của mọi vấn đề EMI: nguồn, đường và nạn nhân. Ở đây, nguồn có thể là dòng điện nguồn "
        "chạy vòng, đường là trở kháng đất chung, và nạn nhân thường là mạch tương tự nhạy. Với "
        "nhiều sự cố hệ thống, người ta không thể làm gì với nguồn hay nạn nhân, nên giải pháp nằm "
        "ở đường đất. Như đã thấy, nối đất một điểm hiệu quả ở tần số thấp, còn mặt phẳng/lưới đất "
        "hiệu quả ở tần số cao hơn."))
    b.append(p(
        "Nếu không thể thay đổi đường đất, vẫn có thể tấn công vòng đất bằng cách “phá vỡ” nó ở "
        "chỗ khác. Ví dụ, có thể dùng biến áp hay bộ cách ly quang (hoặc cả sợi quang) trong các "
        "mối nối cáp; chúng sẽ chặn dòng nhiễu cách chung trong khi vẫn cho tín hiệu vi sai mong "
        "muốn đi qua. Có thể dùng mạch vào/ra (I/O) cân bằng để “triệt” nhiễu nhờ khả năng nén "
        "tín hiệu cách chung. Tất cả các biện pháp này hiệu quả nhất ở 50/60 Hz và trở nên kém "
        "hiệu quả hơn ở tần số cao do điện dung ký sinh."))

    b.append(p("<b>Các nguyên tắc nối đất.</b> Đến đây hẳn đã rõ rằng không có giải pháp thần kỳ "
               "cho việc nối đất. Thay vào đó, các phương pháp và cách tiếp cận khác nhau là cần "
               "thiết cho các mạch và điều kiện vận hành khác nhau. Hai tham số then chốt là tần số "
               "của mối đe doạ (thấp hay cao) và mức tín hiệu làm việc của mạch. Dưới đây là một "
               "số nguyên tắc, nhưng cần nhớ rằng ngay cả những nguyên tắc này cũng có thể phải "
               "sửa đổi cho một tình huống cụ thể."))
    b.append(p(
        "<b><i>Mạch tương tự.</i></b> Vì phần lớn mạch tương tự làm việc ở tần số thấp và chịu "
        "các mối đe doạ tần số thấp, nên nối đất một điểm được ưa dùng. Các mối đe doạ điển hình "
        "là dòng về nguồn 50/60 Hz, dòng điện lạc từ bộ nguồn xung, và có thể cả dòng về của mạch "
        "số (nếu không có nguồn và đất riêng cho phần tương tự và phần số). Các mạch tương tự mức "
        "thấp dễ bị tổn thương nhất, vì mức tín hiệu nhỏ."))
    b.append(p(
        "Cần nhớ rằng các mối đe doạ tần số cao (chẳng hạn một máy phát VHF) đối với mạch tần số "
        "thấp có thể đòi hỏi các giải pháp nối đất tần số cao, như nối đất nhiều điểm. Thường có "
        "thể làm được điều này bằng các tụ điện tần số cao nhỏ (điển hình 1000 pF); ở 100 MHz tụ "
        "này gần như nối tắt, nhưng ở 50/60 Hz vẫn có trở kháng cao."))
    b.append(p(
        "<b><i>Mạch số.</i></b> Phần lớn mạch số ngày nay làm việc ở tần số tương đối cao, nên nối "
        "đất nhiều điểm cùng mặt phẳng và lưới đất được ưa dùng. Các mối nối giữa mạch và đất của "
        "chúng cần ngắn, to và trực tiếp để giảm thiểu điện cảm."))
    b.append(p(
        "Mạch số, đặc biệt các mạch vào/ra, dễ bị tổn thương trước các mối đe doạ tần số cao bên "
        "ngoài như RF và ESD. Chúng cũng là nguồn phát xạ tần số cao quan trọng và là nguồn gây "
        "các vấn đề nội bộ như nhiễu chéo. Với mạch số, nên dùng bảng nhiều lớp có mặt phẳng đất "
        "bên trong. Các mặt phẳng đất này thường được nối với vỏ kim loại bằng nhiều mối nối điện "
        "cảm thấp."))
    b.append(p(
        "Cần đặc biệt chú ý nơi mạch số và mạch tương tự gặp nhau. Thường nên dùng mối nối một "
        "điểm để giảm thiểu vòng đất, nhưng lắp thêm một điện trở nhỏ (điển hình 1 đến 10 Ω) hoặc "
        "một cuộn cảm (điển hình 1 đến 100 µH) tại điểm đó thường có ích để tăng thêm cách ly. Có "
        "thể phải thử nghiệm để tìm ra giải pháp tối ưu."))
    b.append(p(
        "<b><i>Nối đất an toàn nguồn.</i></b> Đã có cả sách viết về chủ đề này, và đúng là nên "
        "như vậy; đây là vấn đề an toàn cực kỳ quan trọng. Mối quan tâm chính ở đây là an toàn con "
        "người và phòng chống điện giật. Ở phần lớn nơi trên thế giới, phần kim loại lộ ra của "
        "thiết bị dùng điện lưới phải được liên kết với một dây dẫn nối đất an toàn. Hơn nữa, các "
        "quy chuẩn đi dây điện (chẳng hạn National Electrical Code ở Hoa Kỳ) đưa ra những hướng "
        "dẫn rất cụ thể về cách thực hiện nối đất nguồn."))
    b.append(p(
        "Phải tuân thủ các hướng dẫn này khi đi dây cho bất kỳ hệ điều khiển công nghiệp nào, và "
        "tuyệt đối không được thoả hiệp bằng những “đất nguồn cách ly” hay những trò dại dột tương "
        "tự. Cuối cùng, nếu bao giờ có xung đột giữa nối đất cho EMI và nối đất an toàn thì các "
        "vấn đề an toàn phải luôn thắng."))

    # ------------------------------------------------------------ shielding
    b.append(h3("Che chắn", "Shielding"))
    b.append(p(
        "Nhiều hệ thống ngày nay cần ít nhất một mức che chắn nào đó để làm việc đúng hoặc để đáp "
        "ứng yêu cầu về phát xạ hay miễn nhiễm bức xạ. Nhiều kỹ sư coi che chắn thuần tuý là vấn "
        "đề cơ khí, nhưng không gì sai hơn thế. Che chắn EMI cần hiểu biết cả về điện lẫn về cơ "
        "khí đối với những vấn đề then chốt thì mới chắc thành công."))
    b.append(p(
        "Hai trong số những vấn đề then chốt đó là chọn đúng vật liệu và duy trì tính toàn vẹn của "
        "vỏ chắn trên dải tần mong muốn. Trong khi phần lớn người ta lo nhiều hơn về việc chọn vật "
        "liệu, tính toàn vẹn của vỏ chắn thường quan trọng hơn nhiều. Ta sẽ thấy ngay rằng ngay cả "
        "những lớp phủ kim loại rất mỏng cũng có thể là vỏ chắn hiệu quả, vậy mà những lỗ hay chỗ "
        "xuyên rất nhỏ lại có thể phá huỷ hoàn toàn một vỏ chắn. Cũng như nối đất, che chắn không "
        "thể để tuỳ tiện mà phải được thiết kế và triển khai đúng cách."))

    b.append(p("<b>Che chắn hoạt động như thế nào.</b> Che chắn EMI gồm hai cơ chế độc lập: phản "
               "xạ và hấp thụ. Ở cơ chế phản xạ, sóng điện từ dội lại khỏi bề mặt, giống như ánh "
               "sáng dội lại khỏi gương. Ở cơ chế hấp thụ, sóng điện từ xuyên vào vật liệu và bị "
               "hấp thụ khi đi qua, giống như thất thoát nhiệt qua một bức tường cách nhiệt."))
    b.append(p("Hiệu quả che chắn thường được biểu diễn như sau:"))
    b.append(eq("SE (dB) = <i>R</i>(dB) + <i>A</i>(dB)", "89.3"))
    b.append(p(
        "trong đó SE là tổng hiệu quả che chắn tính bằng dB, còn <i>R</i> và <i>A</i> là suy hao "
        "phản xạ và suy hao hấp thụ tính bằng dB. Phản xạ là cơ chế chính của che chắn tần số cao "
        "(phát xạ, RFI, ESD), trong khi hấp thụ là cơ chế then chốt của che chắn từ trường tần số "
        "thấp. Các công thức thực tế để tính suy hao phản xạ và hấp thụ khá phức tạp và nằm ngoài "
        "phạm vi chương này, nhưng một số tài liệu được liệt kê ở mục thông tin thêm."))

    b.append(p("<b>Ba loại trường.</b> Khi bàn về che chắn, người ta thường dùng ba loại “trường” "
               "để giải thích. Ba loại trường này giải thích sự khác biệt về hiệu năng che chắn do "
               "khác biệt về tần số và mức trở kháng của mạch. Chúng cũng giải thích vì sao cùng "
               "một vỏ chắn lại xử sự khác nhau với các nguồn năng lượng khác nhau. Đó là sóng "
               "phẳng, từ trường và điện trường. Hình 89.3 cho thấy các đường cong che chắn điển "
               "hình của đồng, có chỉ rõ từng loại trường."))
    b.append(p(
        "<b><i>Trường sóng phẳng.</i></b> Nếu ở cách nguồn điểm một khoảng lớn hơn khoảng 1/6 bước "
        "sóng, trở kháng sóng (tỉ số giữa cường độ điện trường và cường độ từ trường) là hằng số "
        "377 Ω trong không gian tự do. Trường này được gọi là “trường xa” hay “trường bức xạ”, vì "
        "ở đây năng lượng thực chiếm ưu thế và lan truyền như một “sóng phẳng”. Vì suy hao phản xạ "
        "là do sự không khớp giữa trở kháng sóng (377 Ω) và trở kháng bề mặt của vỏ chắn kim loại "
        "(điển hình là cỡ miliôm hoặc nhỏ hơn), nên hiệu quả che chắn với nguồn sóng phẳng thường "
        "rất cao."))
    b.append(fig(3))
    b.append(p(
        "Ở tần số từ 30 MHz trở lên, một khi đã cách xa khoảng 1 m, ta đang ở vùng sóng phẳng. Vì "
        "vậy, ngay cả những vỏ chắn rất mỏng cũng làm việc tốt với các vấn đề phát xạ, ESD và RFI, "
        "với phản xạ là cơ chế che chắn chính."))
    b.append(p(
        "<b><i>Điện trường và từ trường.</i></b> Nếu ở cách nguồn một khoảng nhỏ hơn khoảng 1/6 "
        "bước sóng, trở kháng sóng phụ thuộc vào trở kháng của mạch. Vùng này được gọi là “trường "
        "gần”, vì ở đây năng lượng phản kháng chiếm ưu thế. Vùng này lại được chia thành trường "
        "“điện” và trường “từ”, cả hai đều phụ thuộc trở kháng của mạch nguồn. Với nguồn có trở "
        "kháng cao (điện trường), suy hao phản xạ vẫn cao; nhưng với nguồn có trở kháng thấp (từ "
        "trường), trở kháng có thể khá thấp. Trong trường hợp sau, suy hao phản xạ có thể trở nên "
        "rất nhỏ."))
    b.append(p(
        "Ở tần số của đường dây nguồn, trường gần gần như luôn chiếm ưu thế. Kết quả là các vật "
        "liệu như nhôm hay đồng không có suy hao phản xạ và gần như trong suốt với từ trường của "
        "đường dây nguồn. (Như một quy tắc, hãy nhớ rằng lá nhôm trong suốt với từ trường 60 Hz.) "
        "Để giải quyết vấn đề này, cần dùng vật liệu có độ từ thẩm cao để tăng độ dày điện từ với "
        "một độ dày vật lý cho trước. Thép hoặc các hợp kim mu có độ từ thẩm cao thường được dùng "
        "để hấp thụ (chứ không phản xạ) từ trường. Dù vậy, việc che chắn từ trường tần số thấp "
        "vẫn có thể rất khó khăn."))

    b.append(p("<b>Vì sao che chắn thất bại.</b> Chọn vật liệu là quan trọng, nhưng còn phải xét "
               "các yếu tố khác. Với các mối đe doạ tần số thấp/trở kháng thấp (từ trường của bộ "
               "nguồn hay đường dây nguồn), cần dùng thép hoặc vật liệu có độ từ thẩm cao khác. "
               "Tuy nhiên, với các mối đe doạ tần số cao, ngay cả vật liệu rất mỏng như sơn dẫn "
               "điện cũng cho mức che chắn cao. Song ở tần số cao có hai vấn đề: lỗ hở và chỗ "
               "xuyên trên vỏ chắn. Không chú ý tới hai chỗ này có thể làm mất gần như toàn bộ "
               "hiệu quả che chắn ở tần số cao. Hình 89.4 minh hoạ hai kiểu hỏng này."))
    b.append(p(
        "Trực giác cho rằng bất kỳ lỗ hở nào trên vỏ chắn cũng có thể rò, giống như một cửa sổ mở. "
        "Điều bất ngờ là với rò rỉ điện từ, đại lượng tới hạn không phải diện tích mà là chiều "
        "dài lớn nhất. Ví dụ, một lỗ 100 × 1 mm rò nhiều gấp khoảng mười lần một lỗ vuông 10 × "
        "10 mm. Và khe đó có khi chẳng dễ thấy: nó có thể là một đường ghép đã sơn phủ, hoặc một "
        "tấm panel hay cánh cửa lắp không khít."))
    b.append(fig(4))
    b.append(p(
        "Khe đóng vai trò như những anten nhỏ. Vì là anten, khe càng dài thì bức xạ càng tốt. Nửa "
        "bước sóng là rất hiệu quả, nhưng theo quy tắc kinh nghiệm, chúng tôi muốn giới hạn khe ở "
        "mức 1/20 bước sóng hoặc nhỏ hơn tại tần số cao nhất cần xét. Với 100 MHz, con số này là "
        "15 cm (khoảng 6 in.); ở 300 MHz (tần số của ESD), giảm xuống 5 cm (khoảng 2 in.); và ở "
        "1000 MHz chỉ còn 1,5 cm (2/3 in.). Thậm chí những kích thước này có thể vẫn còn quá lớn, "
        "vì chúng chỉ bảo đảm 20 dB (mười lần) che chắn qua khe. Rõ ràng là ngay cả những khe nhỏ "
        "và các lỗ hở khác cũng đồng nghĩa với vấn đề che chắn lớn ở tần số cao."))
    b.append(p(
        "Cách khác để phá huỷ một vỏ chắn tần số cao là cho kim loại không được kết cuối xuyên qua "
        "vỏ. Ở đây kích thước lỗ không quan trọng, và ngay cả một lỗ kim với một sợi dây có cách "
        "điện xuyên qua cũng có thể mang một lượng lớn năng lượng qua hàng rào che chắn. Đại "
        "lượng thật sự quan trọng là chỗ xuyên kéo dài bao xa về mỗi phía của vỏ chắn. Một lần "
        "nữa, khoảng cách tới hạn là 1/20 bước sóng hoặc hơn."))

    b.append(p("<b>Các nguyên tắc che chắn.</b> Sau khi đã xem che chắn hoạt động (và thất bại) như "
               "thế nào, hãy xem cách thiết kế vỏ chắn điện từ tốt. Trọng tâm chủ yếu là che chắn "
               "RF trong dải 30 đến 1000 MHz, cần cho phát xạ, ESD và RFI."))
    b.append(p(
        "<b><i>Chọn vật liệu.</i></b> Ta đã thấy rằng với các vấn đề nhiễu từ trường tần số thấp, "
        "cần vật liệu có từ tính như thép hoặc hợp kim mu. Phần lớn vấn đề của thiết bị đo hoặc có "
        "bản chất trở kháng cao, hoặc có bản chất tần số cao, nên phần lớn trường hợp vật liệu dẫn "
        "điện mỏng là đủ. Tuy nhiên, với tần số cao, phải chú ý tới khe và chỗ xuyên."))
    b.append(p(
        "Nhiều vỏ hộp ngày nay làm bằng nhựa. Với che chắn tần số cao, lớp phủ dẫn điện cũng làm "
        "việc khá tốt. Các cách xử lý bề mặt phổ biến gồm sơn dẫn điện, lắng đọng chân không, mạ "
        "hoá học không dùng điện, và cả vải kim loại. Nhựa dẫn điện cũng có bán, nhưng nhìn chung "
        "không đạt hiệu năng gần bằng các cách xử lý bề mặt ở tần số cao."))
    b.append(p(
        "<b><i>Gioăng và lưới chắn.</i></b> Các lỗ hở lớn như cửa thông gió hay vùng màn hình có "
        "thể được bịt bằng vật liệu lưới. Các đường ghép hoặc khe có thể được lấp bằng gioăng dẫn "
        "điện. Trong cả hai trường hợp, bí quyết là bảo đảm tiếp xúc kim loại – kim loại đầy đủ và "
        "liên tục tại mọi mối nối. Với che chắn tần số cao, các mối nối phải gần như kín nước. "
        "Kém hơn thế là tự chuốc lấy rắc rối."))
    b.append(p(
        "Với vật liệu lưới, lỗ càng nhỏ thì che chắn càng cao. Lưới chắn cửa sổ có bước gần như "
        "hiệu quả bằng vật liệu đặc từ một chiều tới 1000 MHz, và ngay cả lỗ 5 mm (khoảng 1/4 in.) "
        "cũng thường chấp nhận được ở 1000 MHz. Trong mọi trường hợp, không được vượt quá 1/20 "
        "bước sóng tại tần số cao nhất cần xét."))
    b.append(p(
        "<b><i>Kết cuối cáp và bộ lọc.</i></b> Kết cuối kém của cáp có vỏ chắn có thể gây vấn đề "
        "lớn ở tần số cao. Nếu cáp có vỏ chắn không được kết cuối trực tiếp tại hàng rào che chắn, "
        "một lượng lớn năng lượng sẽ rò ra, làm giảm chất lượng cả vỏ chắn của cáp lẫn của hộp. "
        "Mối nối kiểu “đuôi lợn” (pigtail) — phổ biến khi kết cuối vỏ chắn cáp tần số thấp — đặc "
        "biệt phiền toái ở tần số cao. Thật vậy, đây là nguyên nhân hàng đầu gây hỏng EMI với RFI, "
        "phát xạ và ESD. Theo quy tắc kinh nghiệm, không nên dùng mối nối kiểu đuôi lợn cho vỏ "
        "chắn cáp ở tần số trên khoảng 1 MHz."))
    b.append(p(
        "Cáp không có vỏ chắn cũng có thể gây vấn đề ở tần số cao. Trong trường hợp đó, cần lọc "
        "tần số cao ngay tại giao diện để bảo đảm vỏ chắn không bị giảm hiệu quả ở tần số cao. Các "
        "giải pháp thông dụng là bộ lọc EMI trên đường nguồn và đường tín hiệu, hoặc hạt ferrit "
        "trên dây hay trên cáp. Những thứ này phải được lắp càng gần chỗ xuyên qua vỏ chắn càng "
        "tốt. Tình huống tốt nhất là gắn bộ lọc ngay trên vỏ chắn, tuy điều này không phải lúc nào "
        "cũng cần với các vấn đề ở mức vừa phải."))
    b.append(p(
        "<b><i>Vỏ chắn bên trong.</i></b> Cuối cùng, đừng bỏ qua việc dùng vỏ chắn bên trong cho "
        "các mạch quan trọng. Các nhà thiết kế radio và truyền hình đã làm việc này nhiều năm, dùng "
        "vỏ chắn chọn lọc cho bộ dao động, bộ khuếch đại công suất và những khối tương tự. Một ví "
        "dụ kinh điển của cách làm này là bộ kênh TV — bộ phận nhạy nhất của một máy thu truyền "
        "hình. Đó là một chiến lược che chắn rẻ tiền nhưng rất hiệu quả."))

    b.append(h2("Định nghĩa thuật ngữ", "Defining Terms"))
    b.append(_glossary(_GLOSS1_VI))

    b.append(h2("Thông tin thêm", "Further Information"))
    b.append('<ul class="ref-list">%s</ul>' % "".join("<li>%s</li>" % i for i in _FURTHER1))

    # ------------------------------------------------------------ 89.2
    b.append(h2("89.2 Các phương pháp thử EMI và EMC", "EMI and EMC Test Methods"))
    b.append(p('<span style="color:#777">Jeffrey P. Mills — Illinois Institute of Technology</span>'))
    b.append(p(
        "Điện trường và từ trường phải được đo vì nhiều lý do. Một đài phát thanh hay truyền hình "
        "được cấp phép để phủ sóng ổn định trên một vùng địa lý xác định, và mọi máy thu hoạt động "
        "đúng phải bắt được tín hiệu đó rồi đáp ứng đúng. Điều này chỉ có thể bảo đảm nếu tín hiệu "
        "phát có cường độ tối thiểu được cam kết. Đồng thời, tín hiệu cũng không được mạnh tới mức "
        "gây nhiễu một đài ở xa dùng chung tần số. Trường phát phải được đo trên toàn vùng phủ "
        "sóng để chắc chắn nó thoả mãn cả hai tiêu chí."))
    b.append(p(
        "Nhiều thiết bị điện bức xạ trường điện từ ngoài ý muốn. Ví dụ:"))
    b.append(ul(["Bộ dao động trong máy thu thanh hay truyền hình đổi tần;",
                 "Mạch logic số;",
                 "Tiếp điểm công tắc, đặc biệt khi không có mạch dập hồ quang;",
                 "Hệ thống đánh lửa ô tô."]))
    b.append(p(
        "Trường lạc (phát xạ) từ những thiết bị này có "
        "thể gây nhiễu thiết bị khác, hoặc thậm chí gây nhiễu chính thiết bị bức xạ. Quá trình này "
        "được gọi là nhiễu điện từ, viết tắt là EMI. Nhiễu giữa hai thiết bị được gọi là EMI giữa "
        "các hệ thống, còn nếu một thiết bị tự gây nhiễu chính nó thì gọi là EMI trong một hệ "
        "thống. EMI trong một hệ thống thường dễ phát hiện vì bản thân thiết bị không làm việc "
        "đúng. EMI giữa các hệ thống thường khó khoanh vùng hơn. Kết quả có thể chỉ là chuyện khó "
        "chịu, chẳng hạn tiếng ồn trên máy thu thanh hay truyền hình do máy hút bụi hay máy khoan "
        "điện gây ra. Nhưng cũng có thể nghiêm trọng hơn nhiều: một máy thu thanh xách tay có thể "
        "ảnh hưởng tới dẫn đường máy bay hoặc tới thông tin liên lạc quan trọng."))
    b.append(p(
        "Một thiết bị cũng có thể nhạy nhiễu với trường do máy phát được cấp phép cố ý tạo ra, "
        "chẳng hạn máy phát phát thanh hay máy phát vô tuyến di động. Ví dụ:"))
    b.append(ul(["Hệ thống thông báo công cộng;",
                 "Hệ thống âm nhạc (hi-fi);",
                 "Đường dây và máy điện thoại;",
                 "Mạch logic số."]))
    b.append(p(
        "Một lần nữa, kết quả có thể chỉ là chuyện khó chịu, nhưng cũng có thể nghiêm trọng hơn "
        "nhiều: người ta đã quan sát thấy các bề mặt điều khiển của máy bay chuyển động không kiểm "
        "soát được do trường điện từ mạnh. Vì trong những trường hợp này không thể loại bỏ chính "
        "trường, nên phải làm cho thiết bị miễn nhiễm với trường điện từ."))
    b.append(p(
        "Trong các trường hợp trên, nhiễu thường qua điện trường và/hoặc từ trường trong không "
        "gian, nên quá trình được gọi là ghép bức xạ. Còn một đường ghép khác nếu hai thiết bị "
        "dùng chung một nguồn điện. Một thiết bị có thể sinh ra điện áp tần số cao không mong muốn "
        "trên dây nguồn của nó, và điện áp đó lại xuất hiện trên dây nguồn của thiết bị kia. Thiết "
        "bị thứ hai có thể hỏng chức năng vì điện áp tần số cao này. Đây được gọi là ghép dẫn. Vậy "
        "phải xét cả nhiễu bức xạ lẫn nhiễu dẫn."))
    b.append(p(
        "Không thực tế nếu đòi loại bỏ hoàn toàn mọi trường gây nhiễu, nên phải có một thoả hiệp. "
        "Một trường lạc sẽ không gây EMI nếu nó rất yếu so với trường mong muốn — chẳng hạn trường "
        "của tín hiệu phát thanh. Cường độ cho phép của trường lạc phụ thuộc cường độ trường mong "
        "muốn: trường mong muốn càng mạnh thì càng dung nạp được nhiều trường lạc. Nó cũng phụ "
        "thuộc thiết bị bị nhiễu (nạn nhân); một số máy thu loại bỏ tín hiệu không mong muốn tốt "
        "hơn những máy khác. Vì có rất nhiều tổ hợp nguồn nhiễu và nạn nhân, người ta tìm một kịch "
        "bản xấu nhất có thể bảo vệ phần lớn tình huống thực tế. Kịch bản đó là khi tín hiệu phát "
        "thanh hay truyền hình hợp pháp yếu nhất (trong vùng phủ sóng được cấp phép) được thu bởi "
        "máy thu kém nhất hiện có."))
    b.append(p(
        "Cường độ trường lạc tối đa mà không gây EMI trong kịch bản xấu nhất đó được đưa vào các "
        "quy định của chính phủ. Trường thực tế do mỗi thiết bị bức xạ sau đó phải được đo để chắc "
        "chắn nó không vượt mức này ở khoảng cách thực tế gần nhất tính từ thiết bị, thường là 10 "
        "hoặc 30 m. Để quy định và đo chính xác các cường độ trường này, phải hiểu bản chất của "
        "điện trường và từ trường."))
    b.append(p(
        "Khác với phần lớn các chủ đề kỹ thuật điện khác, việc kiểm soát EMI không chính xác lắm "
        "vì phần cứng thực tế rất phức tạp. Gần như không thể dự đoán nhiễu chính xác hơn mức sai "
        "số ba lần, và thường biên sai số còn tệ hơn. Kết quả đo có thể khác nhau đáng kể giữa hai "
        "mẫu được cho là giống hệt, do sai khác nhỏ về kích thước vật lý. Nếu đo EMI của hai thiết "
        "kế khác nhau, thiết kế có EMI thấp hơn có lẽ tốt hơn — nhưng không phải lúc nào cũng vậy. "
        "Kỹ sư thường có thể phán đoán được có vấn đề EMI hay không, nhưng không bao giờ được dựa "
        "vào độ chính xác thường được mong đợi ở các nhánh khác của kỹ thuật điện."))

    b.append(h3("Bản chất của điện trường và từ trường",
                "Nature of Electric and Magnetic Fields"))
    b.append(p(
        "Điện trường được sinh ra bởi một phân bố điện tích. Nếu phân bố đó thay đổi theo thời "
        "gian thì điện trường cũng thay đổi theo. Từ trường có thể được sinh ra bởi một nam châm "
        "vĩnh cửu hoặc bởi một dòng điện. Nếu nam châm vĩnh cửu hay đường dòng điện chuyển động, "
        "hoặc nếu độ lớn dòng điện biến thiên theo thời gian, thì từ trường cũng biến thiên theo "
        "thời gian. Điện trường biến thiên theo thời gian tạo ra từ trường, và ngược lại."))
    b.append(p(
        "Điện trường, ký hiệu <i>E</i>, thường được biểu diễn bằng vôn trên mét (V/m). Từ trường, "
        "ký hiệu <i>H</i>, được biểu diễn bằng ampe trên mét (A/m). Thường gặp hơn, từ trường được "
        "nhận biết qua mật độ từ thông, ký hiệu <i>B</i>, biểu diễn bằng vêbe trên mét vuông "
        "(Wb/m²), còn gọi là tesla (T). Một đơn vị ngoài SI, đôi khi gặp trong tài liệu cũ, là "
        "gauss, bằng 10<sup>−4</sup> T. Tất nhiên, mọi đơn vị đều có thể được ghép thêm tiền tố "
        "như micro hay pico. Trong không gian tự do, <i>B</i> = µ<sub>0</sub><i>H</i>, với "
        "µ<sub>0</sub> = 0,4π (xấp xỉ 1,257) µT·m/A (tương đương µH/m)."))
    b.append(p(
        "Gần một nguồn điện trường biến thiên theo thời gian, chẳng hạn một phân bố điện tích, từ "
        "trường tương đối yếu, nhưng sẽ mạnh lên khi quan sát từ xa hơn. Ở khoảng cách đủ lớn, tỉ "
        "số <i>E</i>/<i>H</i> tiến tới √(µ/ε); trong không gian tự do giá trị này bằng 120π (xấp "
        "xỉ 377) Ω. Với một hàm điều hoà theo thời gian có tần số <i>f</i>, điều này xảy ra ở mọi "
        "khoảng cách lớn hơn nhiều so với λ/2π (xấp xỉ λ/6). Ở đây λ là bước sóng ứng với <i>f</i>, "
        "bằng 3 × 10<sup>8</sup>/<i>f</i> m nếu <i>f</i> tính bằng hertz. Những khoảng cách lớn "
        "hơn nhiều lần λ/2π được coi là thuộc vùng xa; những khoảng cách gần hơn thuộc vùng gần. "
        "Với một hàm không điều hoà theo thời gian, phải xét riêng từng thành phần tần số Fourier, "
        "và vùng xa bắt đầu gần nguồn hơn đối với các thành phần tần số cao hơn."))
    b.append(p(
        "Gần một nguồn từ trường biến thiên theo thời gian, chẳng hạn một vòng dây mang dòng, "
        "điện trường yếu, nhưng mạnh lên khi quan sát từ khoảng cách lớn hơn. Ở những khoảng cách "
        "lớn hơn nhiều lần λ/2π (vùng xa), tỉ số <i>E</i>/<i>H</i> lại tiến tới 120π Ω."))
    b.append(p(
        "Vì ở vùng xa, với cả hai loại nguồn, <i>H</i> = √(ε/µ)<i>E</i> và <i>B</i> = µ<i>H</i> = "
        "√(µε)<i>E</i>, nên chỉ cần đo <i>E</i> hoặc <i>B</i>, đại lượng còn lại có thể tính dễ "
        "dàng. Trong không gian tự do, √(µε) ≈ 10<sup>−8</sup>/3 T·m/V (tương đương s/m), nên nếu "
        "<i>E</i> tính bằng vôn trên mét thì <i>B</i> ≈ 3,33<i>E</i> nT. Bằng cách chọn anten thích "
        "hợp, có thể đo được trường này hay trường kia. Cường độ trường xa thường được quy định "
        "theo điện trường <i>E</i>, bất kể đo được <i>E</i> hay <i>B</i>."))
    b.append(p(
        "Cách khác, cường độ trường xa có thể được quy định theo mật độ công suất, biểu diễn bằng "
        "oát trên mét vuông. Đại lượng này cho biết lượng công suất bức xạ đi qua mỗi mét vuông "
        "của một bề mặt vuông góc với hướng ra xa nguồn. Mật độ công suất đỉnh <i>P</i> bằng "
        "<i>EH</i>, và với nguồn điều hoà, mật độ công suất trung bình bằng nửa giá trị đó. Với "
        "nguồn không điều hoà, phải xét riêng từng thành phần tần số, và tổng công suất trung bình "
        "là tổng các công suất trung bình của mọi tần số. Vì <i>H</i> = √(ε/µ)<i>E</i>, suy ra "
        "<i>P</i> = <i>E</i><sup>2</sup>/377 Ω."))
    b.append(p(
        "Ở các vùng khác ngoài vùng xa, tỉ số <i>E</i>/<i>H</i> biến thiên rất mạnh, tiến tới vô "
        "cùng với nguồn điện trường hoặc tới không với nguồn từ trường. Một nguồn có thể sinh ra "
        "đồng thời cả điện trường và từ trường; ví dụ, một điện tích chuyển động giữa hai điện cực "
        "làm dòng điện chạy giữa chúng. Khi đó tỉ số <i>E</i>/<i>H</i> có thể nhận bất kỳ giá trị "
        "nào. Vì vậy, ở khoảng cách nhỏ hơn λ/2π tính từ nguồn trường, phải đo riêng cả trường "
        "<i>E</i> lẫn trường <i>B</i>."))
    b.append(p(
        "Ở vùng xa, cả điện trường và từ trường đều vuông góc với hướng lan truyền của sóng điện "
        "từ, và cũng vuông góc với nhau. Điều này vẫn thường cho phép các trường định hướng theo "
        "nhiều góc khác nhau so với mặt đất. Hướng của điện trường được gọi là phân cực của sóng, "
        "có thể là thẳng đứng, nằm ngang, hoặc ở giữa. Hoặc sóng có thể phân cực elip, sinh ra từ "
        "hai sóng không hoàn toàn cùng pha, một sóng phân cực thẳng đứng và một sóng phân cực nằm "
        "ngang. Nếu hai sóng có biên độ bằng nhau và lệch pha đúng 90°, sóng được gọi là phân cực "
        "tròn. Để tính đến mọi trường hợp đó, phải kiểm tra riêng mọi trường với sóng phân cực "
        "thẳng đứng và sóng phân cực nằm ngang."))

    b.append(h3("Anten đo", "Measurement Antennas"))
    b.append(p(
        "Phần lớn linh kiện và thiết bị điện tử được thiết kế để đáp ứng với điện áp hay dòng "
        "điện, chứ không phải với trường. Để đo cường độ trường, phải chuyển tác dụng của trường "
        "thành điện áp hoặc dòng điện. Việc này do anten đảm nhận. Tuy nhiều anten chỉ là những "
        "hình dẫn điện đơn giản, chúng phải được phân tích cẩn thận nếu muốn có phép đo định lượng "
        "chính xác."))
    b.append(p(
        "Một dây dẫn thẳng đặt trong điện trường biến thiên theo thời gian sẽ xuất hiện dòng điện. "
        "Nếu vật liệu dây dẫn là tuyến tính (trường hợp thường gặp), dòng điện sẽ tỉ lệ với điện "
        "trường đặt vào, nên tỉ số của chúng là hằng số. Tuy nhiên, tỉ số này phụ thuộc rất nhiều "
        "vào kích thước hình học của dây dẫn và tần số của điện trường. Phải biết tỉ số đó để hiệu "
        "chuẩn anten."))
    b.append(p(
        "Tương tự, một vòng dây dẫn kín đặt trong từ trường biến thiên theo thời gian cũng sẽ xuất "
        "hiện dòng điện. Một lần nữa, nếu dây dẫn là tuyến tính, tỉ số giữa dòng điện và cường độ "
        "từ trường là hằng số, nhưng phụ thuộc kích thước vòng và tần số của từ trường."))
    b.append(p(
        "Cách dễ nhất để hiệu chuẩn một anten là đặt nó trong một điện trường hay từ trường đã "
        "biết và đo dòng điện hoặc điện áp tại đầu cực anten. Vấn đề chính là tạo ra trường đã "
        "biết đó. Để biết cường độ của nó, phải dùng một anten “chuẩn” mà tỉ số dòng-điện trên "
        "trường có thể tính được."))
    b.append(p(
        "Để tính tỉ số cần thiết, phải giải hệ phương trình Maxwell với các điều kiện biên của dây "
        "dẫn làm anten. Với phần lớn anten, không thể có nghiệm chính xác dạng đóng. Tuy nhiên, "
        "với một điện trường biến thiên điều hoà gặp một dây dẫn hình trụ thẳng gọi là anten lưỡng "
        "cực, nghiệm như vậy là có, dù khó [1]. Khi đã có nghiệm, tỉ số cần thiết trở thành một "
        "biểu thức đơn giản nếu anten ở trạng thái cộng hưởng hay được điều hưởng. Điều này xảy ra "
        "ở một chiều dài chính xác, hơi nhỏ hơn nửa bước sóng λ của trường biến thiên. Rõ ràng "
        "anten chỉ cộng hưởng ở một tần số, nên tỉ số chỉ đúng với trường biến thiên điều hoà ở "
        "đúng tần số đó. Với trường không điều hoà, phải đo riêng từng thành phần tần số Fourier "
        "và phải thay đổi chiều dài anten khi đo các tần số khác nhau. Để đơn giản việc thay đổi "
        "chiều dài, người ta thường dùng hai thanh lồng vào nhau, lắp nối tiếp, để làm anten lưỡng "
        "cực. Thiết bị đo được nối vào giữa hai thanh qua một đường truyền."))
    b.append(p(
        "Ở một tần số cho trước, tại mỗi điểm trên anten có một dòng điện <i>I</i> nhất định chạy "
        "trong đó, và cũng có một điện áp <i>V</i> nhất định so với đất. Tỉ số phasor <i>V</i>/<i>I</i> "
        "được gọi là trở kháng điểm tiếp điện. Chiều dài cộng hưởng chính xác của anten là chiều "
        "dài mà tại đó <i>V</i> và <i>I</i> hoàn toàn cùng pha, tức trở kháng điểm tiếp điện là "
        "thuần thực. Như đã nói, chiều dài này hơi nhỏ hơn nửa bước sóng λ, và còn phụ thuộc độ "
        "dày của các thanh lồng vào nhau (tr. 547–548 của Tài liệu 1). Với thanh có độ dày λ/400, "
        "chiều dài cộng hưởng là 0,476λ. Trở kháng điểm tiếp điện của một anten lưỡng cực có kích "
        "thước như vậy là 64 Ω. Nếu một thiết bị đo điện áp như máy thu hay máy phân tích phổ được "
        "nối vào đầu cực anten qua một đường truyền và được phối hợp đúng với trở kháng 64 Ω, thì "
        "điện áp đo được <i>V</i><sub>m</sub> sẽ bằng 0,148λ<i>E</i>, trong đó <i>E</i> là cường độ "
        "trường đặt vào và λ là bước sóng ở tần số đang đo. Tỉ số <i>V</i><sub>m</sub>/<i>E</i>, "
        "bằng 0,148λ, được gọi là chiều dài hiệu dụng (<i>l</i><sub>e</sub>) của anten, vì nó liên "
        "hệ cường độ trường tính bằng vôn trên mét với điện áp đo được tại đầu cực tính bằng vôn. "
        "Rõ ràng nó không bằng chiều dài vật lý của anten mà xấp xỉ một phần ba giá trị đó. Khi đã "
        "biết tỉ số này, có thể dễ dàng tính cường độ điện trường <i>E</i> gây ra một điện áp đầu "
        "cực <i>V</i><sub>m</sub> nhất định."))
    b.append(p(
        "Để đơn giản tính toán, <i>E</i> thường được biểu diễn bằng decibel so với một trường chuẩn "
        "1 µV/m và ký hiệu là <i>E</i><sub>d</sub>. Tương tự, <i>V</i><sub>m</sub> được biểu diễn "
        "bằng decibel so với một điện áp chuẩn 1 µV và ký hiệu là <i>V</i><sub>d</sub>. Hệ số anten "
        "(AF) được định nghĩa là chiều dài hiệu dụng biểu diễn bằng decibel âm, tức AF = "
        "−20 log(<i>l</i><sub>e</sub>). Khi đó phép nhân trở thành phép cộng: <i>E</i><sub>d</sub> "
        "= <i>V</i><sub>d</sub> + AF."))
    b.append(p(
        "Hệ số anten trên giả định anten được phối hợp hoàn hảo với máy thu, nghĩa là truyền công "
        "suất cực đại. Sự không phối hợp sẽ làm thay đổi hệ số anten. Vì vậy, do trở kháng điểm "
        "tiếp điện của anten thường không bằng trở kháng đầu vào của máy thu, phải chèn một mạch "
        "phối hợp giữa anten và máy thu. Một yếu tố thiết yếu khác là cân bằng của anten. Phần lớn "
        "máy thu và máy phân tích phổ có một đầu cực vào nối đất. Nếu đầu cực nối đất đó được nối "
        "vào một trong hai đầu cực của anten lưỡng cực, các trở kháng nối vào hai đầu cực anten sẽ "
        "không còn bằng nhau so với đất. Điều này cũng làm hỏng hệ số anten, vì một phía của anten "
        "sẽ không được phối hợp đúng với máy thu. Để tránh điều đó, phải chèn một mạng cân bằng – "
        "không cân bằng (balun) giữa anten và máy thu. Mạch như vậy tạo trở kháng cao so với đất "
        "cho cả hai đầu cực vào, đồng thời tạo trở kháng vào đúng (chẳng hạn 64 Ω) giữa hai đầu "
        "cực của nó. Thông thường, một mạng duy nhất đảm nhận cả chức năng phối hợp lẫn cân bằng."))
    b.append(p(
        "Đáng tiếc là trừ khi anten lưỡng cực có chiều dài chính xác, hệ số anten của nó phức tạp "
        "hơn nhiều. Ngay cả khi tần số đang đo chỉ lệch vài phần trăm so với tần số cộng hưởng của "
        "anten, hệ số anten trở nên không dự đoán được và trở kháng điểm tiếp điện trở thành phức. "
        "Khi đó không thể dễ dàng tính điện trường từ điện áp đo được tại đầu cực. Để có được hệ số "
        "anten đơn giản như mô tả ở trên, phải đo từng tần số một và điều chỉnh chiều dài anten "
        "lưỡng cực cho phù hợp với mỗi tần số. Không thể quét phổ nhanh, như khi dùng máy phân tích "
        "phổ, trừ khi chiều dài anten cũng có thể thay đổi theo — điều này dẫn tới khó khăn cơ khí "
        "và thường không thực tế."))
    b.append(p(
        "Tuy nhiên, các loại anten khác ít nhạy với tần số hơn. Ví dụ là anten hai hình nón "
        "(biconical) và anten loga-chu kỳ. Anten hai hình nón làm việc chấp nhận được trong dải 20 "
        "đến 300 MHz, còn anten loga-chu kỳ dùng được từ 300 đến 1000 MHz. Hệ số anten của chúng "
        "tương đối ổn định, thường chỉ thay đổi không quá 20 dB trên dải tần dùng được. Các hệ số "
        "anten này thường quá khó tính, nhưng có thể đo dễ dàng bằng cách quan sát điện áp đầu cực "
        "gây ra bởi một trường biến thiên điều hoà đã biết cường độ. Trường đã biết đó trước hết "
        "được đo bằng một anten lưỡng cực điều hưởng, loại anten mà hệ số có thể tính được. Hệ số "
        "anten được đo theo cách này tại vài tần số trong dải dùng được, và kết quả được vẽ thành "
        "đồ thị để dùng kèm với anten."))
    b.append(p(
        "Khác với lưỡng cực điều hưởng, anten hai hình nón và loga-chu kỳ không có trở kháng điểm "
        "tiếp điện không đổi trên dải tần dùng được. Vì không thể làm cho trở kháng vào của máy "
        "thu bám theo sự biến thiên của trở kháng điểm tiếp điện theo tần số, không thể phối hợp "
        "chính xác. Điều này ảnh hưởng tới hệ số anten đúng như với một lưỡng cực điều hưởng không "
        "được phối hợp. Để bù lại, phải đo hệ số anten khi anten được kết cuối vào một trở kháng "
        "đã biết, và trở kháng đó phải được dùng cho mọi phép đo với anten này. Khi đó sự không "
        "phối hợp đã được tính ngay trong hệ số anten. Sự không phối hợp có làm anten tái bức xạ "
        "tín hiệu thu được, nhưng có thể giảm thiểu hiệu ứng này bằng cách thực hiện phép đo tại "
        "một bãi thử trường mở, sẽ bàn ở phần sau."))
    b.append(p(
        "Anten lưỡng cực điều hưởng, anten hai hình nón và anten loga-chu kỳ đều là anten phân cực "
        "tuyến tính, vì chúng chỉ đáp ứng một thành phần phân cực của sóng lan truyền. Nếu anten "
        "được định hướng nằm ngang, chỉ thành phần phân cực ngang của sóng tác động lên nó. Tương "
        "tự, chỉ thành phần phân cực thẳng đứng tác động lên anten định hướng thẳng đứng. Vì vậy, "
        "với hai phép đo, mọi anten phân cực tuyến tính sẽ phát hiện được mọi kiểu phân cực của "
        "trường. Các loại anten khác, chẳng hạn anten xoắn, được thiết kế để phát hiện sóng phân "
        "cực tròn. Chúng sẽ phát hiện được sóng phân cực thẳng đứng và nằm ngang, nhưng có thể bỏ "
        "sót một sóng phân cực tròn theo chiều ngược lại (chẳng hạn ngược chiều kim đồng hồ thay "
        "vì cùng chiều). Do đó, anten phân cực tròn bị cấm dùng cho nhiều loại phép đo trường."))
    b.append(p(
        "Mọi anten bàn ở trên đều đáp ứng với điện trường <i>E</i>. Như đã nói, ở vùng xa, từ "
        "trường <i>B</i> đơn giản bằng 3,33 nT nhân với giá trị của <i>E</i> tính bằng vôn trên "
        "mét. Tuy nhiên, ở bất kỳ vùng nào khác, <i>B</i> không liên hệ đơn giản như vậy với "
        "<i>E</i> và phải được đo riêng, bằng một anten đáp ứng với từ trường. Một vòng dây hay "
        "cuộn dây tròn chính là anten như vậy. Vòng được cắt tại một điểm và máy thu hay máy phân "
        "tích phổ được nối vào hai đầu của nó. Để đo định lượng, phải biết hệ số anten của nó. Có "
        "thể đo hệ số này bằng cách đặt anten trong một từ trường đã biết và đo điện áp tại đầu "
        "cực. Để tìm cường độ từ trường đã biết đó, trước hết đo điện trường ở vùng xa bằng một "
        "anten lưỡng cực điều hưởng đã biết hệ số. Từ trường khi đó bằng 3,33 nT nhân với giá trị "
        "điện trường tính bằng vôn trên mét. Khi đã xác định được từ trường, có thể tính hệ số "
        "anten của vòng như mong muốn."))

    b.append(h3("Môi trường đo", "Measurement Environment"))
    b.append(p(
        "Một khó khăn lớn của phép đo trường điện từ là tính lặp lại của kết quả. Trường điện từ "
        "bị ảnh hưởng bởi mọi vật liệu ở gần, kể cả vật dẫn kém và chất điện môi. Vì vậy, môi "
        "trường đo phải được xác định cẩn thận, và phải dùng những môi trường tương tự nhau cho "
        "mọi phép đo có thể so sánh được."))
    b.append(p(
        "Môi trường lý tưởng là môi trường trong đó (1) nguồn trường điện từ duy nhất là thiết bị "
        "cần đo (EUT) và (2) hoàn toàn không có vật liệu “lạ” nào có thể ảnh hưởng tới trường đang "
        "đo. Đáng tiếc là nơi duy nhất trong tự nhiên đạt được điều đó là ngoài vũ trụ, vì chính "
        "Trái Đất cũng ảnh hưởng tới trường điện từ. Vì điều đó không thực tế, người ta tìm cách "
        "mô phỏng môi trường này ngay trên Trái Đất."))
    b.append(p(
        "Một khoảng trống lớn ngoài trời mô phỏng một bán cầu không gian tự do. Bãi thử như vậy "
        "được gọi đúng tên là bãi thử trường mở. Nếu độ dẫn điện, hằng số điện môi và độ từ thẩm "
        "của Trái Đất là hằng số thì mọi bãi thử trường mở sẽ có cùng tác dụng lên trường điện từ "
        "bức xạ từ EUT. Tuy nhiên, các tham số của Trái Đất thay đổi. Để bù lại sự thay đổi đó, "
        "người ta trải một sàn dẫn điện lớn, hay mặt phẳng đất, dưới EUT. Việc này làm mọi sóng "
        "điện từ phản xạ hoàn toàn khỏi mặt phẳng đất, nhờ đó các tính chất của Trái Đất không còn "
        "tác dụng. Mặt phẳng đất phải đủ lớn để trông như vô hạn đối với EUT và thiết bị đo đi "
        "kèm. Kích thước chấp nhận được là 1,73<i>d</i> × 2<i>d</i>, với <i>d</i> là khoảng cách "
        "giữa anten đo và EUT, thường là 3 hoặc 10 m."))
    b.append(p(
        "Phát xạ bức xạ phải được đo theo mọi hướng từ EUT và ở nhiều góc nghiêng khác nhau. Cách "
        "dễ nhất là đặt EUT trên một bàn xoay rồi xoay bàn trong khi thử. Để đo được ở nhiều góc "
        "nghiêng, phải thay đổi độ cao anten thu, và việc này được thực hiện bằng cách treo anten "
        "trên một hệ ròng rọc. Hình 89.5 cho thấy một bãi thử trường mở điển hình."))
    b.append(fig(5))
    b.append(p(
        "Bãi thử trường mở chỉ cho dữ liệu lặp lại được nếu xung quanh không có cây cối hay công "
        "trình có thể gây phản xạ không mong muốn. Trước khi có thể dùng tin cậy, bãi thử phải "
        "được kiểm tra. Việc này được làm bằng cách tạo một trường điện từ đã biết rồi đo nó. "
        "Trường thường được tạo bởi một bộ dao động tần số vô tuyến điều khiển một anten lưỡng cực "
        "điều hưởng, loại anten mà bức xạ có thể tính được (tr. 237–238 của Tài liệu 2). Bức xạ "
        "này sau đó được đo như thể nó do một thiết bị điển hình đang được thử tạo ra. Tỉ số giữa "
        "điện áp tại đầu cực anten phát và điện áp tại đầu cực anten thu được gọi là suy hao hiện "
        "trường. Nếu suy hao hiện trường nằm trong 3 dB so với giá trị tính được, bãi thử được coi "
        "là chấp nhận được."))
    b.append(p(
        "Tuy bãi thử trường mở loại bỏ được phản xạ, các nguồn trường bên ngoài như máy phát được "
        "cấp phép vẫn gây rắc rối. Vì bức xạ điện từ có thể truyền đi hàng nghìn dặm, không bãi "
        "thử trường mở nào hoàn toàn không có trường điện từ. Để loại bỏ tác dụng của các nguồn lạ "
        "này, phải thử bên trong một vỏ chắn. Tuy nhiên, ở đó lại xảy ra phản xạ mạnh, và phép đo "
        "trở nên thiếu chính xác và không lặp lại được."))
    b.append(p(
        "Một môi trường thử lý tưởng sẽ là một vỏ chắn được lót bằng vật liệu không phản xạ sóng "
        "điện từ. Vỏ như vậy được gọi là buồng không vang, với hàm ý tên gọi nhắc tới tiếng vang "
        "điện từ. Cho tới gần đây, những buồng như vậy không thực tế, trừ ở tần số rất cao, nhưng "
        "các cải tiến không ngừng được đưa ra. Một vỏ như vậy được chấp nhận để thử nếu nó đáp ứng "
        "yêu cầu về suy hao hiện trường của một bãi trường mở thật. Suy hao hiện trường phải được "
        "đo tại vài điểm bên trong buồng để chắc chắn sự gần kề của các bức tường không có tác "
        "dụng. Đáng tiếc là hiện nay những buồng như vậy rất đắt."))
    b.append(p(
        "Một loại buồng thử khác là buồng điện từ ngang (TEM). Buồng này gồm một đoạn ống dẫn "
        "sóng phình to, trong đó trường điện từ có thể được dự đoán chính xác [3,4]. Chúng chỉ phù "
        "hợp để thử các thiết bị nhỏ ở tần số tương đối thấp. Buồng TEM không được lớn hơn một "
        "bước sóng ở tần số đang thử. Ví dụ, để thử ở 200 MHz, buồng không được lớn hơn 1,5 m (5 "
        "ft), và bản thân thiết bị không được vượt quá 1/6 giá trị đó, tức 10 in. Tuy nhiên, với "
        "các thiết bị nhỏ, buồng TEM rất chính xác và không bị ảnh hưởng bởi các nguồn trường lạ."))
    b.append(p(
        "Nếu không có buồng không vang phù hợp, có thể thử thiết bị trong một vỏ chắn thông thường "
        "để biết nó phát xạ ở những tần số nào. Cường độ trường sẽ không chính xác do phản xạ bên "
        "trong. Sau đó thiết bị được thử tại một bãi trường mở thật, và các tần số nghi ngờ được đo "
        "định lượng. Mọi trường vượt giới hạn chấp nhận được sau đó được quan sát khi thiết bị đã "
        "tắt. Nếu trường không mất đi, rõ ràng nó không do EUT tạo ra. Thủ tục này chấp nhận được, "
        "tuy không đơn giản bằng thử trong buồng không vang."))
    b.append(p(
        "Thậm chí có thể thực hiện các phép đo sơ bộ trong một căn phòng thường. Chúng sẽ không so "
        "sánh được với các phép đo tương tự thực hiện ở nơi khác, vì ảnh hưởng của vật dẫn và chất "
        "điện môi ở gần. Ở đây cũng vậy, phải tắt thiết bị để xác định xem có phát xạ nào đến từ "
        "nguồn bên ngoài lạ thay vì từ EUT hay không. Thủ tục này cho một ước lượng thô về phát xạ "
        "của EUT và thường tiết kiệm thời gian cho các lần thử sau tại một bãi trường mở thật. Các "
        "phương pháp đo khác nhau được tóm tắt trong Bảng 89.4."))
    b.append(table_89_4("vi"))
    b.append(p(
        "Các mức phát xạ cho phép được nêu trong Bộ luật Liên bang Hoa Kỳ [5]. Những quy định này "
        "giả định phép đo tại bãi trường mở, tức phép đo chính xác nhất có thể. Ngay ở đó, sai "
        "khác ±6 dB cũng là điển hình. Vì vậy, nhà sản xuất nên dành một hệ số an toàn khi thực "
        "hiện các phép đo nhằm bảo đảm tuân thủ quy định của chính phủ. Nếu không, thiết bị có thể "
        "đạt khi nhà sản xuất thử nhưng lại trượt nếu sau đó chính phủ thử bằng một thủ tục được "
        "cho là giống hệt. Vì khi đó kết quả đo của chính phủ là kết quả có hiệu lực, uy tín của "
        "nhà sản xuất có thể bị nghi ngờ."))
    b.append(p("Các chi tiết khác về kỹ thuật đo có trong Tài liệu 2 và 6."))

    b.append(h2("Định nghĩa thuật ngữ", "Defining Terms"))
    b.append(_glossary(_GLOSS2_VI))

    b.append(h2("Tài liệu tham khảo", "References"))
    b.append(refs(_REFS2))

    b.append(h2("Thông tin thêm", "Further Information"))
    b.append('<ul class="ref-list">%s</ul>' % "".join("<li>%s</li>" % i for i in _FURTHER2))
    return "".join(b)


# ================================================================ BODY — EN
def body_en():
    b = []
    b.append(note(
        "<b>Translator's note.</b> The text extract destroys almost every mathematical symbol and "
        "unit, so every equation and all four tables were re-read from the printed page. "
        "Specifically: (89.2) is printed <i>E</i>(V/m) = 5.5 √(PA)/<i>d</i>; the extract loses both "
        "the radical and the division and gives &ldquo;5.5 PA d&rdquo;. (89.3) is printed "
        "SE (dB) = <i>R</i>(dB) + <i>A</i>(dB); the extract scrambles it into &ldquo;SE dB () = RA "
        "() dB + () dB&rdquo;. (89.1) is printed <i>f</i> = 1/(π<i>t</i><sub>r</sub>), and the "
        "sentence immediately after it gives the lightning rise time as <b>1 µs</b> — the extract "
        "says &ldquo;1 ms&rdquo;, whereas 1/(π × 1 µs) ≈ 318 kHz, which is the 300 kHz the author "
        "quotes. Symbols were replaced by Latin letters: Ω (ohm) became &ldquo;W&rdquo;, µ became "
        "&ldquo;m&rdquo;, π became &ldquo;p&rdquo;, λ became &ldquo;l&rdquo;, ε became "
        "&ldquo;e&rdquo;, × became &ldquo;´&rdquo;, ≈ became &ldquo;»&rdquo;, and every "
        "super/subscript was flattened onto the baseline. Hence &ldquo;377 W&rdquo; is 377 Ω, "
        "&ldquo;64 W&rdquo; is 64 Ω, &ldquo;1 to 10 W&rdquo; is 1 to 10 Ω, &ldquo;1 to 100 "
        "mH&rdquo; is 1 to 100 µH, &ldquo;0.4p (approximately 1.257) mT·m/A&rdquo; is 0.4π "
        "µT·m/A, &ldquo;10–8/3&rdquo; is 10<sup>−8</sup>/3, &ldquo;3·108/f&rdquo; is "
        "3 × 10<sup>8</sup>/<i>f</i>, and &ldquo;l/2p&rdquo; is λ/2π. Table 89.3 changes unit "
        "inside the table — µΩ in the upper block, mΩ in the lower — but the original prints a unit "
        "only in the first cell of each block, so the extract turns the whole table into "
        "&ldquo;mW&rdquo;. Table 89.2 is titled &ldquo;10-cm-Length Wires&rdquo; yet its first two "
        "columns are per-metre values; only the three Z columns are for the 10 cm length. Three "
        "further textual defects are reproduced as printed: the Figure 89.1 caption reads "
        "&ldquo;All three elements must be necessary&rdquo; (it should be <i>must be present</i>), "
        "89.2 prints &ldquo;superhetrodyne&rdquo; (read: <i>superheterodyne</i>) and &ldquo;It is "
        "expected that that wireless LANs&rdquo; (doubled <i>that</i>). Note also that 89.1 says "
        "&ldquo;greater than about 1/6 wavelength&rdquo; while 89.2 says λ/2π ≈ λ/6 — two spellings "
        "of the same threshold."))

    # ------------------------------------------------------------ 89.1
    b.append(h2("89.1 Grounding and Shielding in Industrial Electronic Systems"))
    b.append(p('<span style="color:#777">Daryl Gerke and William Kimmel — Kimmel Gerke Associates, '
               'Ltd.</span>'))

    b.append(p(
        "EMC (electromagnetic compatibility) is crucial to successful operation of industrial "
        "systems. Due to the increased electronic content of most industrial controls, "
        "electromagnetic interference (EMI) problems have increased dramatically in recent years. "
        "Two keys to EMC success are grounding and shielding. This section will briefly discuss how "
        "to implement these two crucial EMC strategies. It will also provide a general introduction "
        "to EMI problems in today's industrial electronic systems. The primary emphasis will be on "
        "practical insights and ideas gained in dealing with numerous industrial control problems."))

    b.append(h3("Understanding EMI Problems"))
    b.append(p("Here are three general observations on dealing with EMI problems in industrial "
               "electronics."))
    b.append(p(
        "<b>First, the industrial environment is harsh.</b> The primary EMI threats are power "
        "disturbances, RFI (radio frequency interference), and ESD (electrostatic discharge). In "
        "addition, analog sensor circuits are often plagued with 50/60 Hz &ldquo;ground loop&rdquo; "
        "problems. Industrial electronics need more EMC care than most commercial electronics, and "
        "even more than many military systems."))
    b.append(p(
        "<b>Second, electronics often play a secondary role in electronics systems.</b> Unlike a "
        "computer system, where electronics is the core technology, industrial electronics are "
        "often used to support another technology, such as chemical, mechanical, or process "
        "functions. This leads to EMC challenges when integrating the electronics to nonelectronic "
        "technologies."))
    b.append(p(
        "<b>Third, EMC rules and regulations are finally catching up to industrial "
        "electronics.</b> For many years, industrial electronics were exempt from mandatory EMC "
        "rules, so unless there was an actual problem, EMC was often ignored. With the EMC "
        "directives of the European Union (EU) now in force, industrial electronics are no longer "
        "exempt."))

    b.append(p("<b>Three types of problems.</b> There are three aspects of the EMC problem: "
               "emissions, susceptibility (also known as immunity), and self-compatibility. "
               "Emissions originate within the equipment, and may upset other nearby equipment. On "
               "the other hand, external energy may upset equipment, leading to susceptibility (or "
               "a lack of immunity). Finally, energy internal to the system may interfere with "
               "other internal circuits, resulting in a self-compatibility problem."))
    b.append(p(
        "Problems with both emissions and susceptibility have led to EMC regulations. Two of the "
        "best known are the FCC (Federal Communications Commission) regulations for emissions in "
        "the U.S., and the EU regulations for both emissions and immunity in Europe. Industrial "
        "controls have always been exempt from the FCC regulations, but they are not exempt from "
        "the EU regulations which became mandatory in January 1996."))

    b.append(p("<b>Four major EMC threats.</b> Most industrial EMC problems fall into one of four "
               "key areas: emissions, power disturbances, radio frequency interference, and "
               "electrostatic discharge. In the past, industrial systems were usually only "
               "concerned with power disturbances. Today, all four threats must be considered."))
    b.append(p(
        "<b><i>Emissions.</i></b> Emissions refer to electric energy originating within equipment "
        "that can interfere with other equipment. The prime concern of this threat is jamming "
        "nearby television receivers, which is the basis for the now mandatory EU emissions "
        "regulations. Emissions problems between industrial electronic systems, however, are rare. "
        "While it is possible to interfere with any other nearby equipment, most industrial "
        "electronics generate only minute amounts of conducted and radiated interference, well "
        "below upset thresholds for digital or analog circuits."))
    b.append(p(
        "Emissions are best addressed at the equipment design stage. Strategies include printed "
        "circuit board design techniques, high-frequency filtering on power and signal interfaces, "
        "shielded cables, and enclosure shielding. Fixes in the field are usually limited to "
        "shielded cables or enclosures, add-on filters, and ferrite clamps on cables."))
    b.append(p(
        "<b><i>Power disturbances.</i></b> Power disturbances can take many forms, from short "
        "transients to long sags, surges, or complete power outages. The three most serious power "
        "threats to industrial controls are transients, voltage sags, and power outages. Stray "
        "50/60 Hz currents can also cause problems with sensitive analog circuits, particularly due "
        "to ground loops (to be discussed later). Other power disturbances, like frequency or "
        "waveform variations, often have little effect on electronic systems."))
    b.append(p(
        "Power disturbances are very common in industrial environments. As a result, most "
        "industrial systems are pretty robust against this threat, at least at low frequencies. "
        "High-frequency threats, such as fast transients or RF on the power lines, can still cause "
        "problems. The EU tests simulate these threats with the EFT (electrical fast transient) and "
        "injected RF tests."))
    b.append(p(
        "Most power disturbances are caused by nearby equipment, rather than external sources. (One "
        "critical exception is lightning, which can result in some nasty voltage and current "
        "surges.) Power disturbance solutions include grounding, power filters, transient "
        "protectors, and in extreme cases, uninterruptible power systems (UPS)."))
    b.append(p(
        "<b><i>Radio frequency interference.</i></b> RFI deals with threats in the RF range. RFI is "
        "quite common in industrial environments, and will likely get worse with the proliferation "
        "of handheld radios and cellular telephones. It is expected that wireless LANs (local area "
        "networks) will also provide some interesting EMI challenges. There have been cases where "
        "handheld radios were banned from use due to repeated EMI problems with industrial "
        "electronics."))
    b.append(p(
        "It turns out that the nearby handheld radio is a much bigger threat than a large "
        "commercial broadcast station several kilometers away. A key metric is electric field "
        "intensity, measured in &ldquo;volts/meter&rdquo;. This is a function of both transmitter "
        "power, and distance from the antenna, and can be quickly predicted by the formula:"))
    b.append(eq("<i>E</i>(V/m) = 5.5 " + _frac(_sq("PA"), "<i>d</i>"), "89.2"))
    b.append(p(
        "where <i>P</i> = transmitter power in watts, <i>A</i> = antenna gain, and <i>d</i> = "
        "distance from the antenna in meters. For example, the electric field from a 1-W radio with "
        "a zero gain antenna at 1 m is about 5 V/m, while the electric field from a 10,000 W "
        "broadcast station at 1 km is about 0.5 V/m. Since unprotected equipment can fail in the "
        "0.1 to 1 V/m range, problems can and do occur. The EU &ldquo;heavy industrial&rdquo; limits "
        "of 10 V/m are clearly aimed at protecting against the nearby handheld radio."))
    b.append(p(
        "Solutions to RFI problems include high-frequency filtering on power and signal cables, "
        "shielded cables, and shielded enclosures. Analog circuits are particularly vulnerable to "
        "RFI, so they often need extra protection. Do not overlook banning radio transmitters in "
        "the immediate vicinity. Often, maintaining a 3 to 10 m distance is enough to solve the "
        "problem."))
    b.append(p(
        "<b><i>Electrostatic discharge.</i></b> ESD refers to the sudden discharge that can occur "
        "after a gradual buildup of electric charge. ESD is most commonly associated with humans "
        "(touching controls or keyboards), but ESD can also be caused by internal arcing due to the "
        "movement of paper, plastic, etc. Internal ESD problems are increasing in industrial "
        "systems."))
    b.append(p(
        "Although the static buildup can take a long time (seconds or even minutes), the discharge "
        "is almost instantaneous (nanoseconds or less). Furthermore, it is the sudden current, not "
        "the voltage, that is the culprit. The effect is a bit like having a dam burst — the ESD "
        "current is like water running down a mountain, destroying anything in its path. "
        "Fortunately, the current surge does not last too long, so the energy levels are not high. "
        "They are high enough, however, to damage or upset electronic devices."))
    b.append(p(
        "The extremely fast discharge results in high frequencies well into the UHF range. At 1 ns, "
        "the transient bandwidth is over 300 MHz. As a result, it does not take a &ldquo;direct ESD "
        "hit&rdquo; to cause a problem. ESD upsets 5 to 10 m away are not uncommon, due to the "
        "intense electromagnetic fields associated with an ESD event. These problems are "
        "particularly insidious, since the ESD event may be occurring on a different piece of "
        "equipment."))
    b.append(p(
        "Solutions to ESD problems include transient protection, high-frequency filtering, cable "
        "shielding, and enclosure shielding. Grounding is a very important factor in ESD "
        "protection, but it must be designed for high frequencies. Since many times ESD causes "
        "&ldquo;reset&rdquo; problems, extra attention to microprocessor reset circuits is "
        "beneficial."))

    b.append(p("<b>Sources, paths, and receptors.</b> A common EMI problem is gathering and "
               "organizing data. This is particularly important when troubleshooting EMI in the "
               "field. The &ldquo;source–path–receptor&rdquo; model is popular. Simply stated, three "
               "elements are necessary for any EMI problem:"))
    b.append(ul(["There must be a source of energy;",
                 "There must be a receptor that is upset by that energy;",
                 "There must be a coupling path between the source and receptor."]))
    b.append(p(
        "All three elements must exist at the same time, and if any one is missing, there is no EMI "
        "problem. Sometimes one can identify all three, and, other times, one can only guess. While "
        "this may seem simple, it is a useful tool to organize EMI information."))
    b.append(p(
        "Figure 89.1 illustrates this model, giving typical sources, paths, and receptors. Several "
        "possible sources have been discussed: emissions from digital circuits, ESD, RFI from "
        "communications transmitters, and power disturbances (including lightning). Several "
        "different receptors have also been suggested: communications receivers, analog "
        "electronics, and digital electronics. Note the two types of paths: radiated and conducted. "
        "In both cases, the object is to block unwanted energy from reaching a receptor, which is "
        "done with shielding (for the radiated path) and filtering (for the conducted path)."))
    b.append(fig(1, "en"))

    b.append(h3("Grounding"))
    b.append(p(
        "Grounding is probably the most important, yet least understood, aspect of EMI control. "
        "Every circuit is connected to some sort of &ldquo;ground&rdquo;, so every circuit is "
        "affected by EMI grounding issues."))

    b.append(p("<b>What is a ground?</b> A major problem with the subject of grounding is the "
               "ambiguity of the term. Our favorite definition is one popular in the EMC community, "
               "which says that a ground is simply a return path for current flow. These currents "
               "can be intended, or unintended. The unintended currents are often referred to as "
               "&ldquo;sneak grounds&rdquo;, and can cause many kinds of EMI problems. Finally, a "
               "physical connection is not even necessary at higher frequencies, where parasitic "
               "capacitance or inductance may form part of a ground path."))

    b.append(p("<b>Different types of grounds.</b> Grounds are used for many reasons, including "
               "power, safety, lightning, EMI, and ESD. Although they may share common functions, "
               "they may vary widely when it comes to frequencies and current amplitudes. "
               "Recognizing these key differences is key to understanding grounding issues."))
    b.append(p(
        "Table 89.1 shows some frequency and amplitude requirements of several different types of "
        "grounds. Note that power and safety grounds must handle high currents, but only at low "
        "frequencies. Grounds for EMI and ESD, on the other hand, must often handle high "
        "frequencies at relatively low current levels. Lightning grounds must handle extremely high "
        "currents, but at moderate frequencies."))
    b.append(table_89_1("en"))
    b.append(p(
        "The frequency of transient events is calculated using the formula "
        "<i>f</i> = 1/(π<i>t</i><sub>r</sub>), where <i>f</i> is the equivalent frequency, and "
        "<i>t</i><sub>r</sub> is the transient rise/fall time. This relationship can be derived "
        "using Fourier analysis. For example, ESD has an equivalent frequency of about 300 MHz "
        "based on a typical 1 ns rise time, and lightning has an equivalent frequency of about "
        "300 kHz based on a 1 µs rise time."))
    b.append(eq("<i>f</i> = " + _frac("1", "π<i>t</i><sub>r</sub>"), "89.1"))
    b.append(p(
        "Note that of all these types of grounds, only one actually needs an Earth connection — "
        "lightning. Other grounds may be connected to Earth by convention or for other safety "
        "reasons. For example, power neutrals are connected to Earth in many parts of the world to "
        "help provide lightning protection. On the other hand, in many other parts of the world, "
        "the power systems do not have Earth connections. When dealing with power grounding, the "
        "local safety codes will determine the proper Earth grounding methods."))

    b.append(p("<b>Ground impedances.</b> A good ground must have a low enough impedance to "
               "minimize voltage drop in the ground system, and must provide the preferred path for "
               "current flow. The key to success is maintaining that low impedance over the entire "
               "frequency range of interest. We cannot overemphasize this point. Most EMI grounding "
               "problems are due to using the wrong approach for a given range."))
    b.append(p(
        "The impedance of a ground conductor consists of both resistance and inductance "
        "(<i>Z</i> = <i>R</i> + jω<i>L</i>). For frequencies from dc through about 10 kHz, the "
        "resistance is the major factor, so heavy-gage wires are often used for low-frequency "
        "ground conductors. As the frequency increases, however, the inductance becomes the "
        "limiting factor for impedance. As a rule of thumb, the inductance for round wires is in "
        "the range of 10 nH/cm."))
    b.append(p(
        "Table 89.2 gives the resistance, inductance, and inductive reactance for typical wire "
        "sizes used in instrumentation power and signal circuits. It is apparent that at power and "
        "audio frequencies (dc to 10 kHz), resistance is the dominant factor in ground impedance. "
        "Thus, at low frequencies, look for ways to reduce resistance, typically by using larger "
        "wires. At frequencies above the audio range (>10 kHz), inductance becomes the dominant "
        "factor in ground impedance. Thus, at higher frequencies, look for ways to reduce the "
        "inductance of the ground path. This is accomplished by using ground planes, grids, and "
        "straps to lower the inductance."))
    b.append(table_89_2("en"))
    b.append(p(
        "Table 89.3 gives the impedances for solid ground planes at various frequencies. In this "
        "case, the impedances are in &ldquo;ohms-per-square&rdquo;, which is a measure of impedance "
        "across a diagonal surface. By comparing this with Table 89.2, one can see that at high "
        "frequencies (such as 100 MHz) the ground plane impedance may be several orders of "
        "magnitude below the impedance of a wire. Furthermore, at high frequencies the thickness is "
        "not a factor, since the impedance is limited by the skin effect."))
    b.append(table_89_3("en"))

    b.append(p("<b>Ground topologies.</b> Now that we have looked at ground impedance vs. "
               "frequency, we are ready to look at ground topologies vs. frequency. The impedance "
               "limitations yield two different grounding approaches, dependent on frequency. For "
               "low-frequency problems (dc to 10 kHz), single-point grounds are preferred, while at "
               "high frequencies (above 10 kHz), multipoint grounds with planes or grids become the "
               "preferred approach."))
    b.append(p(
        "This dichotomy often causes confusion with industrial controls, but this can be minimized "
        "by determining the frequency of the EMI threat and then selecting the appropriate "
        "grounding approach. In many cases, both approaches may be necessary at the same time, "
        "leading to &ldquo;hybrid&rdquo; grounds, which use capacitors and inductors to alter the "
        "ground topology with frequency."))
    b.append(p(
        "<b><i>Single-point grounds.</i></b> At low frequencies, one can usually steer current via "
        "wires. Since the inductance is low, the limiting factor is the wire resistance itself. "
        "Furthermore, capacitive coupling from the ground wires to adjacent wires or surfaces is "
        "small, so virtually all the current follows the wiring path."))
    b.append(p(
        "Figure 89.2 shows a typical industrial grounding scheme. Note what happens if the system "
        "is grounded at both ends. Any common noise current in the common ground path is now "
        "coupled into the circuit via the &ldquo;common ground impedance&rdquo;. This results in "
        "the dreaded &ldquo;ground loop&rdquo;, which will be discussed shortly. A single-point "
        "ground eliminates the ground loop, since there is no common impedance across which a "
        "common-mode voltage can be generated. Thus, single-point grounding is a very practical way "
        "to limit &ldquo;ground noise&rdquo; problems with the threat of low-frequency ground "
        "currents. This is very typical of 50/60 Hz currents getting into sensitive analog "
        "instrumentation circuits."))
    b.append(fig(2, "en"))
    b.append(p(
        "<b><i>Multipoint grounds.</i></b> Unfortunately, as the frequency increases, the inductive "
        "reactance of the wires increases. At the same time, parasitic capacitive reactance to "
        "adjacent wires or surfaces decreases, and soon it is no longer possible to maintain a true "
        "single-point ground, even if the system is wired that way. The only option left is to "
        "lower the ground path impedance, and that is accomplished with planes or grids. "
        "Furthermore, single-point connections to a grid or plane are usually not adequate because "
        "of transmission line effects, so multipoint grounds (combined with planes/grids) become "
        "the preferred approach above 10 kHz."))
    b.append(p(
        "Ground grids have been used for years in computer facilities, and are seeing increasing "
        "use in industrial facilities. The recommended spacing for grids is no more than 1/20 of a "
        "wavelength at the highest frequency of concern. Computer room grids are often spaced about "
        "0.7 m (about 2 ft), which meets this criteria from dc to about 25 MHz. This is very "
        "beneficial in addressing ground noise due to lightning and other power transients, which "
        "are usually in the 1 MHz range and below. But a 0.7-m grid does not help with VHF/UHF "
        "radio problems or ESD. In those cases, solid surfaces may be necessary."))
    b.append(p(
        "<b><i>Ground loops.</i></b> Ground loops are a serious problem for sensitive analog "
        "circuits facing low-frequency threats. At high frequencies, ground loops generally do not "
        "pose serious threats if proper high-frequency precautions are taken when designing the "
        "ground system."))
    b.append(p(
        "A ground loop exists whenever multiple ground paths exist. Unwanted currents can take "
        "unwanted paths, resulting in unwanted noise voltages at unwanted places. The problem is "
        "particularly acute with sensitive analog systems, where even a few microvolts can jam "
        "intended signals. A classic example is 60 Hz ground currents causing hum in an audio "
        "system."))
    b.append(p(
        "Figure 89.2 shows a typical ground loop problem. Note that there must be the three "
        "conditions of any EMI problem: a source, a path, and a victim. In this case, the source can "
        "be circulating power currents, the path the common ground impedance, and the victim is "
        "often the sensitive analog circuit. With many systems problems, one cannot do anything "
        "about either the source or victim, so the solution is with the ground path. As we have "
        "already seen, single-point grounding is effective at low frequencies, and ground "
        "planes/grids are effective at higher frequencies."))
    b.append(p(
        "If one cannot change the ground paths, one can still attack the ground loop by "
        "&ldquo;breaking&rdquo; it in other places. For example, transformers or optical isolators "
        "(or even fiber optics) can be used in cable connections, which will block common mode "
        "noise currents while passing intended differential mode signals. Balanced input/output "
        "(I/O) circuits can be used to &ldquo;cancel&rdquo; the noise through common-mode "
        "rejection. All of these are most effective at 50/60 Hz, and become less effective at "
        "higher frequencies due to parasitic capacitance."))

    b.append(p("<b>Grounding guidelines.</b> By now it should be apparent that there is no magic "
               "solution for grounding. Rather, different methods and approaches are necessary for "
               "different circuits and operating conditions. Two key parameters are the threat "
               "frequency (low vs. high), and the circuit operating levels. Here are some "
               "guidelines, but keep in mind that even these may need to be modified for a "
               "particular situation."))
    b.append(p(
        "<b><i>Analog circuits.</i></b> Since most analog circuits operate at low frequencies and "
        "are subject to low-frequency threats, single-point grounds are preferred. Typical threats "
        "are 50/60 Hz power return currents, stray switching power supply currents, and perhaps "
        "digital circuit return currents (if separate analog and digital power and grounds are not "
        "provided). Low-level analog circuits are the most vulnerable, since the signal levels are "
        "small."))
    b.append(p(
        "Keep in mind that high-frequency threats (such as a VHF radio) to low-frequency circuits "
        "may require high-frequency grounding solutions, such as multipoint grounds. Often, this "
        "can be accomplished by using small high-frequency capacitors (1000 pF typical) which "
        "appear as a short at 100 MHz, yet still appear as a high impedance at 50/60 Hz."))
    b.append(p(
        "<b><i>Digital circuits.</i></b> Most digital circuits today operate at relatively high "
        "frequencies, so multipoint grounds and ground planes and grids are preferred. The "
        "connections between the circuits and their grounds need to be short, fat, and direct to "
        "minimize inductance."))
    b.append(p(
        "Digital circuits, particularly I/O circuits, are vulnerable to external high-frequency "
        "threats like RF and ESD. They are also a key source of high-frequency emissions and "
        "internal problems like cross talk. For digital circuits, multilayer boards with internal "
        "ground planes are preferred. These ground planes typically are connected to a metallic "
        "enclosure through multiple low-inductance connections."))
    b.append(p(
        "Pay particular attention to where digital and analog circuits meet. A single-point "
        "connection is usually preferred to minimize ground loops, but installing a small resistor "
        "(1 to 10 Ω typical) or inductor (1 to 100 µH typical) at that point is often helpful in "
        "providing additional isolation. One may need to experiment with this to determine the "
        "optimum solutions."))
    b.append(p(
        "<b><i>Power safety grounding.</i></b> Entire books have been written about this subject, "
        "and rightly so; this is an extremely important safety issue. The key concern here is human "
        "safety and prevention of electric shock. In most parts of the world, exposed metal on "
        "line-powered equipment must be bonded to a safety grounding conductor. Furthermore, the "
        "electric wiring codes (such as the National Electrical Code in the U.S.) give very "
        "specific guidelines on how power grounding must be accomplished."))
    b.append(p(
        "These guidelines must be followed when wiring any industrial control system, and must "
        "never be compromised by &ldquo;isolated&rdquo; power grounds or other similar foolishness. "
        "Finally, if there is ever a conflict between EMI and safety grounding, the safety issues "
        "must always prevail!"))

    # ------------------------------------------------------------ shielding
    b.append(h3("Shielding"))
    b.append(p(
        "Many systems today require at least some shielding for proper operation or to meet "
        "radiated emission or immunity requirements. Many engineers consider shielding purely a "
        "mechanical issue, but nothing could be farther from the truth. EMI shielding needs both an "
        "electrical and a mechanical understanding of key issues to assure success."))
    b.append(p(
        "Two of these key issues are selecting the right material and maintaining the shielding "
        "integrity over the desired frequency range. While most people worry more about the "
        "selection, shield integrity is usually much more important. We will soon see that even "
        "very thin metallic coatings can be effective shields, yet even very small holes or "
        "penetrations can completely destroy a shield. Like grounding, shielding cannot be left to "
        "chance, and must be properly designed and implemented."))

    b.append(p("<b>How shielding works.</b> EMI shielding involves two independent mechanisms: "
               "reflection and absorption. In reflection, an electromagnetic wave bounces off the "
               "surface, just like light off a mirror. In absorption, the electromagnetic wave "
               "penetrates the material and is absorbed as it passes through, much like heat loss "
               "through an insulating wall."))
    b.append(p("Shielding effectiveness is usually expressed as follows:"))
    b.append(eq("SE (dB) = <i>R</i>(dB) + <i>A</i>(dB)", "89.3"))
    b.append(p(
        "where SE is the total shielding effectiveness in dB, and <i>R</i> and <i>A</i> are the "
        "reflection and absorption losses expressed in dB. Reflection is the primary mechanism for "
        "high-frequency shielding (emissions, RFI, ESD), while absorption is the key mechanism for "
        "low-frequency magnetic field shielding. The actual formulas for calculating reflection and "
        "absorption losses are a bit complex, and beyond the scope of this chapter, but several "
        "sources are included in the further information section."))

    b.append(p("<b>Three types of fields.</b> It is customary when dealing with shielding to use "
               "three types of &ldquo;fields&rdquo; to explain shielding. These three fields "
               "account for differences in shielding performance due to differences in frequency "
               "and circuit impedance levels. They also explain why the same shield can behave "
               "differently for different energy sources. These are plane waves, magnetic fields, "
               "and electric fields. Figure 89.3 shows typical shielding curves for copper, with "
               "references to each type of field."))
    b.append(p(
        "<b><i>Plane wave fields.</i></b> If one is located greater than about 1/6 wavelength from "
        "a point source, the wave impedance (ratio of electric field intensity to magnetic field "
        "intensity) is a constant 377 Ω in free space. This field is known as the &ldquo;far "
        "field&rdquo; or &ldquo;radiation field&rdquo;, since real energy predominates here and "
        "propagates as a &ldquo;plane wave&rdquo;. Since reflection losses are due to a mismatch "
        "between the wave impedance (377 Ω) and a metallic shield surface impedance (typically "
        "milliohms or less), shielding effectiveness is usually very high for plane wave "
        "sources."))
    b.append(fig(3, "en"))
    b.append(p(
        "At frequencies 30 MHz and above, once one is more than about 1 m away, one is in the plane "
        "wave region. Thus, even very thin shields work well for emissions, ESD, and RFI problems, "
        "with reflection as the prime shielding mechanism."))
    b.append(p(
        "<b><i>Electric and magnetic fields.</i></b> If one is located less than about 1/6 "
        "wavelength from the source, then the wave impedance is dependent on the circuit impedance. "
        "This region is known as the &ldquo;near field&rdquo;, since reactive energy predominates "
        "here. This region is further divided into &ldquo;electric&rdquo; and "
        "&ldquo;magnetic&rdquo; fields, both dependent on source circuit impedance. For "
        "high-impedance sources (electric fields), the reflection losses are still high, but for "
        "low-impedance sources (magnetic fields), the impedance can be quite low. In the latter "
        "case, the reflection losses can become minimal."))
    b.append(p(
        "For power line frequencies, the near field almost always predominates. As a result, "
        "materials like aluminum or copper have no reflection losses and are virtually transparent "
        "to power line magnetic fields. (As a rule, remember that aluminum foil is transparent to "
        "60 Hz magnetic fields.) To solve this problem, permeable materials are needed to boost the "
        "electric thickness for a given physical thickness. Steel or high-permeability mu-metals "
        "are usually used to absorb (not reflect) the magnetic fields. Even so, it can still be "
        "very difficult to shield for low-frequency magnetic fields."))

    b.append(p("<b>Why shielding fails.</b> While material selection is important, other factors "
               "must also be considered. For low-frequency/low-impedance threats (power supply or "
               "power line magnetic fields), steel or other high-permeability materials are needed. "
               "For high-frequency threats, however, even very thin materials like conductive "
               "paints provide high levels of shielding. Two problems at high frequencies, however, "
               "are shield openings and shield penetrations. Lack of attention to these areas can "
               "result in a loss of virtually all shielding effectiveness at high frequencies. "
               "Figure 89.4 illustrates these two high-frequency failure modes."))
    b.append(p(
        "Intuition suggests that any opening in a shield can leak, much like an open window. The "
        "surprise is that for electromagnetic leakage it is not the area that is critical, but the "
        "longest dimension. For example, a 100 × 1 mm opening is about ten times more leaky than a "
        "10 × 10 mm square hole. And that slot may not even be obvious. It could be a painted seam "
        "or a poorly fitting panel or door."))
    b.append(fig(4, "en"))
    b.append(p(
        "Slots act like small antennas. Because they are antennas, the longer they are, the better "
        "they radiate. While a half wavelength is very efficient, as a rule of thumb, we like to "
        "limit slots to 1/20 wavelength or less at the highest frequency of concern. For 100 MHz, "
        "this is 15 cm (about 6 in.); at 300 MHz (ESD frequencies), this drops to 5 cm (about 2 "
        "in.), and at 1000 MHz, it is only 1.5 cm (2/3 in.). And even these dimensions may be too "
        "large, as they only assure 20 dB (tenfold) of shielding through the slot. Clearly, even "
        "small slots and other openings mean big shielding problems at high frequencies."))
    b.append(p(
        "The other way to destroy a high-frequency shield is to pass unterminated metal through a "
        "shield. Hole dimensions do not matter here, and even a pinhole with an insulated wire "
        "passing though can carry large amounts across the shielding barrier. The dimension that "
        "does matter is how far the penetration extends on either side of the shield. Once again, "
        "the critical distance is 1/20 wavelength or more."))

    b.append(p("<b>Shielding guidelines.</b> Now that we have looked at how shielding works (and "
               "fails), let us look at how to design good electromagnetic shields. Most of our focus "
               "will be on RF shielding in the 30 to 1000 MHz range, necessary for emissions, ESD, "
               "and RFI."))
    b.append(p(
        "<b><i>Material selection.</i></b> We have already seen that for low-frequency magnetic "
        "interference problems, ferrous material like steel or mu-metals are necessary. Most "
        "instrumentation problems are either high impedance or high frequency in nature, so most of "
        "the time, thin conductive materials will work fine. For high frequencies, however, "
        "attention must be given to slots and penetrations."))
    b.append(p(
        "Many enclosures today are made of plastic. For high-frequency shielding, conductive "
        "coatings also work quite well. Popular surface treatments include conductive paints, "
        "vacuum deposition, electroless plating, and even metal fabrics. Conductive plastics are "
        "also available, but they generally do not perform nearly as well as surface treatments for "
        "high frequencies."))
    b.append(p(
        "<b><i>Gasketing and screening.</i></b> Large openings, such as ventilation ports or "
        "display areas, can be sealed with screening material. Seams or slots can be filled with "
        "conductive gaskets. In both cases, the secret is to provide complete and continuous "
        "metal-to-metal contact at all junctions. For high-frequency shielding, the connections "
        "must be almost watertight. Anything less is asking for problems."))
    b.append(p(
        "For screening material, the smaller the openings, the higher the shielding. Window screen "
        "spacing is almost as effective as solid materials from dc to 1000 MHz, and even 5-mm "
        "(about 1/4 in.) openings are often acceptable at 1000 MHz. In any case, do not exceed 1/20 "
        "wavelength at the highest frequency of concern."))
    b.append(p(
        "<b><i>Cable terminations and filters.</i></b> Poor termination of shielded cables can "
        "cause big problems at high frequencies. If a shielded cable is not terminated directly at "
        "the shielding barrier, a lot of energy leaks, degrading both the cable and the enclosure "
        "shield. Pigtail connections, popular for terminating low-frequency cable shields, are "
        "particularly bothersome at high frequencies. In fact, this is a leading cause of EMI "
        "failures for RFI, emissions, and ESD. As a rule of thumb, pigtail connections should not "
        "be used on cable shields at frequencies above about 1 MHz."))
    b.append(p(
        "Unshielded cables can also cause problems at high frequencies. In those cases, "
        "high-frequency filtering is needed directly at the interface to assure that the shield is "
        "not degraded at high frequencies. Common solutions are EMI filters on power and signal "
        "lines, or ferrite beads on the lines or cables. These must be installed as close to the "
        "shield penetration as possible. The best situation is to mount the filter directly in the "
        "shield itself, although this is not always necessary for moderate problems."))
    b.append(p(
        "<b><i>Internal shields.</i></b> Finally, do not overlook using internal shields on "
        "critical circuits. Radio and television designers have been doing this for years, using "
        "selective shields on oscillators, power amplifiers, and the like. A classic example of "
        "this approach is the TV tuner, the most sensitive part of a television receiver. It is an "
        "inexpensive, yet highly effective shielding strategy."))

    b.append(h2("Defining Terms"))
    b.append(_glossary(_GLOSS1_EN))

    b.append(h2("Further Information"))
    b.append('<ul class="ref-list">%s</ul>' % "".join("<li>%s</li>" % i for i in _FURTHER1_EN))

    # ------------------------------------------------------------ 89.2
    b.append(h2("89.2 EMI and EMC Test Methods"))
    b.append(p('<span style="color:#777">Jeffrey P. Mills — Illinois Institute of '
               'Technology</span>'))
    b.append(p(
        "Electric and magnetic fields must be measured for a variety of reasons. A radio or TV "
        "broadcast station is licensed to provide reliable coverage over a specified geographic "
        "area, and any properly operating receiver must pick up the signal and properly respond to "
        "it. This can be assured only if the broadcast signal is of a guaranteed minimum strength. "
        "Also, the signal must not be so strong that it interferes with a distant station sharing "
        "the same frequency. The broadcast field must be measured over its geographic area of "
        "coverage to be sure that it satisfies both criteria."))
    b.append(p(
        "Many electric devices unintentionally radiate electromagnetic fields. Examples include:"))
    b.append(ul(["Oscillators in superheterodyne radio or TV receivers",
                 "Digital logic circuits",
                 "Switching contacts, particularly if unsuppressed",
                 "Automotive ignition systems"]))
    b.append(p(
        "Stray fields (emissions) from these devices can interfere with other devices, or even with "
        "the radiating device itself. This process is known as electromagnetic interference, "
        "commonly abbreviated EMI. Interference between two devices is known as intersystem EMI, "
        "whereas if a device interferes with itself it is intrasystem EMI. Intrasystem EMI is "
        "usually easy to spot because the device itself does not operate correctly. Intersystem EMI "
        "is usually more difficult to isolate. Its result might be a simple annoyance, such as "
        "noise on a radio and TV receiver caused by an electric vacuum cleaner or a power drill. It "
        "could, however, be much more serious; a portable radio receiver might affect aircraft "
        "navigation or critical communications."))
    b.append(p(
        "It is also possible for a device to be susceptible to fields intentionally generated by a "
        "licensed transmitter such as a broadcast or mobile-radio transmitter. Examples include:"))
    b.append(ul(["Public-address systems",
                 "Music (high-fidelity) systems",
                 "Telephone lines and instruments",
                 "Digital logic circuits"]))
    b.append(p(
        "Again, the result may be only an annoyance, or it could be much more serious; aircraft "
        "control surfaces have been observed to move uncontrollably due to strong electromagnetic "
        "fields. Since the fields themselves cannot be eliminated in these cases, the devices must "
        "be made immune to electromagnetic fields."))
    b.append(p(
        "In the above cases, the interference is usually through electric and/or magnetic fields in "
        "space, so the process is known as radiated coupling. Another coupling path exists if two "
        "devices share the same power source. One device may generate undesired high-frequency "
        "voltages on its power leads, which then appear on the power leads of the other. The second "
        "device may then malfunction because of this high-frequency voltage. This is known as "
        "conducted coupling. So we must consider both radiated and conducted noise."))
    b.append(p(
        "It is not practical to eliminate all interfering fields completely, so a compromise must "
        "be reached. A stray field will not cause EMI if it is very weak compared with the desired "
        "field, which might be the field of a broadcast signal. The permissible strength of the "
        "stray field depends on the strength of the desired field; the stronger the desired field, "
        "the more stray field can be tolerated. It also depends on the device that is being "
        "interfered with (the victim); some receivers can reject undesired signals better than "
        "others. Since there are many combinations of interference sources and victims, a "
        "worst-case scenario is sought that will protect most real-life situations. This occurs "
        "where the weakest legal radio or TV signal (in its licensed area of coverage) is received "
        "by the poorest available receiver."))
    b.append(p(
        "The maximum stray field strength that causes no EMI for this worst-case scenario is "
        "incorporated into government regulations. The field actually radiated by every device must "
        "then be measured to be sure that it does not exceed this level at the nearest practical "
        "distance from it, usually 10 or 30 m. To specify and measure these field strengths "
        "accurately, the nature of electric and magnetic fields must be understood."))
    b.append(p(
        "Unlike most electrical engineering topics, EMI control is not very precise because of the "
        "complexity of practical hardware. It is virtually impossible to predict interference more "
        "precisely than within a factor of three, and usually the margin of error is even worse. "
        "Measurements can vary significantly between two supposedly identical samples, due to "
        "slight variations in physical dimensions. If one measures the EMI resulting from two "
        "different designs, the design that exhibits less EMI is probably better, but not always. "
        "An engineer can often judge if an EMI problem exists, but one must never rely on the "
        "accuracy normally expected in other branches of electrical engineering."))

    b.append(h3("Nature of Electric and Magnetic Fields"))
    b.append(p(
        "An electric field is generated by a distribution of electric charge. If the distribution "
        "changes with time, then so will the electric field. A magnetic field may be generated by a "
        "permanent magnet or by an electric current. If the permanent magnet or the current path "
        "moves, or if the current magnitude varies with time, the magnetic field will vary with "
        "time. A time-varying electric field creates a magnetic field, and conversely."))
    b.append(p(
        "Electric fields, designated <i>E</i>, are normally expressed in volts per meter (V/m). "
        "Magnetic fields are designated <i>H</i> and expressed in amperes per meter (A/m). More "
        "often, magnetic fields are perceived as magnetic flux density, which is designated "
        "<i>B</i> and expressed in webers per square meter (Wb/m²), also known as teslas (T). A "
        "non-SI unit, sometimes found in older literature, is the gauss, equal to "
        "10<sup>−4</sup> T. Of course, any unit may be preceded by a scaling prefix such as micro "
        "or pico. In free space, <i>B</i> is equal to µ<sub>0</sub><i>H</i>, where µ<sub>0</sub> is "
        "equal to 0.4π (approximately 1.257) µT·m/A (equivalent to µH/m)."))
    b.append(p(
        "Near a time-varying electric field source such as a charge distribution, the magnetic "
        "field is relatively weak, but it becomes stronger when observed from farther away. At a "
        "great enough distance, the ratio of <i>E</i> to <i>H</i> approaches √(µ/ε), which in free "
        "space is equal to 120π (approximately 377) Ω. For a sinusoidal function of time with a "
        "frequency <i>f</i>, this occurs at any distance that is large compared with λ/2π "
        "(approximately λ/6). Here, λ is the wavelength corresponding to <i>f</i>, equal to "
        "3 × 10<sup>8</sup>/<i>f</i> m if <i>f</i> is specified in hertz. Distances much greater "
        "than λ/2π are considered to be in the far-field region; nearer distances are in the "
        "near-field region. For a nonsinusoidal function of time, each Fourier frequency component "
        "must be considered separately, and the far-field region begins closer to the source for "
        "its higher frequency components."))
    b.append(p(
        "Near a time-varying magnetic field source such as a current loop, the electric field is "
        "weak, becoming stronger when observed from a greater distance. At distances that are large "
        "compared with λ/2π (the far-field region), the ratio of <i>E</i> to <i>H</i> again "
        "approaches 120π Ω."))
    b.append(p(
        "Since <i>H</i> = √(ε/µ)<i>E</i> and <i>B</i> = µ<i>H</i> = √(µε)<i>E</i> in the far-field "
        "region for either type of source, only <i>E</i> or <i>B</i> must be measured, and the "
        "other can easily be calculated from it. In free space, √(µε) ≈ 10<sup>−8</sup>/3 T·m/V "
        "(equivalent to s/m), so, if <i>E</i> is expressed in volts per meter, <i>B</i> ≈ "
        "3.33<i>E</i> nT. By choice of a suitable antenna, either field can be measured. Far-field "
        "strengths are normally specified in terms of the <i>E</i> field, no matter whether the "
        "<i>E</i> or <i>B</i> field is measured."))
    b.append(p(
        "Alternatively, the far-field strength may be specified in terms of power density, "
        "expressed in watts per square meter. This denotes the amount of radiated power passing "
        "through each square meter of a surface perpendicular to the direction away from the "
        "source. The peak power density <i>P</i> is equal to <i>EH</i>, and, for a sinusoidal "
        "source, the average power density is half this value. For a nonsinusoidal source, each "
        "frequency component must be considered separately, and the total average power is the sum "
        "of the average powers for all frequencies. Since <i>H</i> = √(ε/µ)<i>E</i>, it follows "
        "that <i>P</i> = <i>E</i><sup>2</sup>/377 Ω."))
    b.append(p(
        "In regions other than the far field, the ratio of <i>E</i> to <i>H</i> varies greatly, "
        "approaching infinity for an electric field source or zero for a magnetic field source. A "
        "source may generate both electric and magnetic fields; for example, a charge moving "
        "between two electrodes causes a current to flow between them. Then the ratio of <i>E</i> "
        "to <i>H</i> may be any value at all. Therefore, at distances less than λ/2π from a field "
        "source, both the <i>E</i> and <i>B</i> fields must be measured separately."))
    b.append(p(
        "In the far-field region, both the electric and magnetic fields are perpendicular to the "
        "direction that an electromagnetic wave is propagating, and they are also perpendicular to "
        "each other. This still usually allows the fields to be oriented at many different angles "
        "with respect to the surface of the Earth. The direction of the electric field is called "
        "the polarization of the wave, which may be vertical, horizontal, or somewhere between. Or "
        "the wave may be elliptically polarized, which results from two waves that are not exactly "
        "in phase, one polarized vertically and the other horizontally. If the waves are equal in "
        "magnitude and exactly 90° out of phase, the wave is circularly polarized. To account for "
        "all these cases, all fields must be checked separately for vertically and horizontally "
        "polarized waves."))

    b.append(h3("Measurement Antennas"))
    b.append(p(
        "Most electronic components and instruments are designed to respond to voltages or "
        "currents, not fields. To measure a field strength it is necessary to convert its effect to "
        "a voltage or a current. This is achieved by an antenna. Although many antennas are simple "
        "conductor shapes, they must be analyzed carefully if accurate quantitative measurements "
        "are desired."))
    b.append(p(
        "A straight conductor immersed in a time-varying electric field will develop a current in "
        "it. If the conductor material is linear (the usual case), the current will be proportional "
        "to the applied electric field, so their ratio will be constant. This ratio, however, "
        "depends greatly on the geometric dimensions of the conductor and the frequency of the "
        "electric field. It must be known to calibrate the antenna."))
    b.append(p(
        "Similarly, a closed conductive loop immersed in a time-varying magnetic field will develop "
        "a current in it. Again, if the conductor is linear, the ratio of the current to the "
        "magnetic field strength is constant but depends on the dimensions of the loop and the "
        "frequency of the magnetic field."))
    b.append(p(
        "The easiest way to calibrate an antenna is to immerse it in a known electric or magnetic "
        "field and measure the current or voltage at the antenna terminals. The principal problem "
        "is generating the known field. To find its strength, one must use a &ldquo;standard&rdquo; "
        "antenna for which the current-to-field ratio can be calculated."))
    b.append(p(
        "To calculate the required ratio, Maxwell's equations must be solved subject to the "
        "boundary conditions of the antenna conductor. For most antennas an exact closed-form "
        "solution is impossible. However, for a sinusoidally varying field encountering a straight "
        "cylindrical conductor called a dipole antenna, such a solution is possible, though "
        "difficult [1]. Once the solution is obtained, the required ratio becomes a simple "
        "expression if the antenna is resonant or tuned. This occurs for a precise length that is "
        "slightly less than one half the wavelength, λ, of the time-varying field. Obviously, the "
        "antenna will be resonant at only one frequency, so the ratio will be valid only for a "
        "field varying sinusoidally at that frequency. For nonsinusoidal fields, each Fourier "
        "frequency component must be measured separately, and the antenna length must be changed as "
        "different frequencies are measured. To simplify changing its length, two telescoping rods, "
        "mounted end to end, are normally used to make the dipole antenna. The measuring instrument "
        "is connected between these two rods via a transmission line."))
    b.append(p(
        "For a given frequency, at any point on the antenna, there is a certain current <i>I</i> "
        "flowing in it, and there is also a certain voltage <i>V</i> on it with respect to ground. "
        "The ratio of these phasors, <i>V</i>/<i>I</i>, is known as the driving-point impedance. The "
        "precise resonant antenna length is that for which <i>V</i> and <i>I</i> are exactly in "
        "phase, i.e., for which the driving-point impedance is purely real. As mentioned above, "
        "this length is slightly less than half the wavelength, λ, and it also depends on the "
        "thickness of the telescoping rods (pp. 547–548 of Reference 1). For a rod thickness of "
        "λ/400, the resonant length is 0.476λ. The driving-point impedance of a dipole antenna of "
        "these dimensions is 64 Ω. If a voltage-measuring instrument such as a radio receiver or "
        "spectrum analyzer is connected to the antenna terminals via a transmission line, and is "
        "properly matched to the 64 Ω impedance, the measured voltage <i>V</i><sub>m</sub> will be "
        "equal to 0.148λ<i>E</i>, where <i>E</i> is the applied field strength and λ is the "
        "wavelength at the frequency being measured. The ratio <i>V</i><sub>m</sub>/<i>E</i>, equal "
        "to 0.148λ, is known as the effective length (<i>l</i><sub>e</sub>) of the antenna, since it "
        "relates the field strength in volts per meter to the measured terminal voltage in volts. "
        "Obviously, it is not equal to the physical antenna length but is instead approximately one "
        "third of that value. With this ratio known, the electric field strength <i>E</i> that "
        "causes a certain terminal voltage <i>V</i><sub>m</sub> can easily be calculated."))
    b.append(p(
        "To simplify calculations, <i>E</i> is often expressed in decibels with respect to a "
        "reference field of 1 µV/m and is designated <i>E</i><sub>d</sub>. Similarly, "
        "<i>V</i><sub>m</sub> is expressed in decibels with respect to a reference voltage of 1 µV "
        "and is designated <i>V</i><sub>d</sub>. The antenna factor (AF) is defined as the effective "
        "length expressed in negative decibels, or AF = −20 log(<i>l</i><sub>e</sub>). Then the "
        "multiplication becomes an addition, i.e., <i>E</i><sub>d</sub> = <i>V</i><sub>d</sub> + "
        "AF."))
    b.append(p(
        "The above antenna factor assumes that the antenna is perfectly matched to the receiver, "
        "which implies maximum power transfer. A mismatch would change the antenna factor. "
        "Therefore, since the antenna driving-point impedance usually is not equal to the receiver "
        "input impedance, a matching circuit must be inserted between the antenna and receiver. "
        "Another essential consideration is antenna balance. Most receivers and spectrum analyzers "
        "have one input terminal grounded. If this grounded terminal is connected to one of the "
        "dipole antenna terminals, the impedances connected to the two antenna terminals will be "
        "unequal with respect to ground. This also will upset the antenna factor, since one side of "
        "the antenna will not be properly matched to the receiver. To prevent this, a "
        "balanced-to-unbalanced (balun) network must be inserted between the antenna and receiver. "
        "Such a circuit provides a high impedance with respect to ground for both input terminals, "
        "while providing the correct input impedance (such as 64 Ω) between its input terminals. "
        "Normally, a single network provides both the matching and balancing functions."))
    b.append(p(
        "Unfortunately, unless the dipole antenna is precisely the correct length, its antenna "
        "factor is much more complicated. Even if the frequency being measured differs only a few "
        "percent from the antenna resonant frequency, the antenna factor becomes unpredictable and "
        "the driving-point impedance becomes complex. Thus, the electric field cannot be easily "
        "calculated from the measured terminal voltage. To achieve the simple antenna factor "
        "described above, the frequencies must be measured one at a time and the dipole antenna "
        "length properly adjusted for each frequency. It is impossible to sweep the spectrum "
        "rapidly, as when using a spectrum analyzer, unless the antenna length can somehow be "
        "varied also. This leads to mechanical difficulties and is usually impractical."))
    b.append(p(
        "Other types of antennas, however, are less sensitive to frequency. Examples are the "
        "biconical antenna and the log-periodic antenna. A biconical antenna can perform acceptably "
        "over a range of 20 to 300 MHz, and a log-periodic antenna is useful from 300 to 1000 MHz. "
        "Their antenna factors are relatively constant, usually varying by no more than 20 dB, over "
        "their useful frequency ranges. The antenna factors are usually too difficult to calculate, "
        "but they may easily be measured simply by observing the terminal voltage resulting from a "
        "sinusoidally varying field of known strength. The known field is first measured using a "
        "tuned dipole antenna, for which the antenna factor can be calculated. The antenna factor is "
        "measured in this manner at several frequencies throughout its useful range, and the results "
        "are plotted for use with the antenna."))
    b.append(p(
        "Unlike the tuned dipole, the biconical and log-periodic antennas do not exhibit constant "
        "driving-point impedances over their useful frequency range. Since the receiver input "
        "impedance cannot be made to follow the variation of driving-point impedance with "
        "frequency, an exact match is impossible. This affects the antenna factor just as it would "
        "for a mismatched tuned dipole. To compensate for this, the antenna factor must be measured "
        "with the antenna terminated into a known impedance, which must then be used for all "
        "measurements made with that antenna. Then the mismatch is accounted for in the antenna "
        "factor itself. The mismatch does cause the antenna to reradiate the received signal, but "
        "this effect may be minimized by performing the measurements in an open-field site, which "
        "will be discussed later."))
    b.append(p(
        "Tuned dipole, biconical, and log-periodic antennas are linearly polarized antennas because "
        "they respond to only one polarization component of a propagating wave. If the antenna is "
        "oriented horizontally, only the horizontally polarized component of the wave will affect "
        "it. Similarly, only the vertically polarized component will affect a vertically oriented "
        "antenna. Thus, with two measurements, any linearly polarized antenna will detect any type "
        "of field polarization. Other types of antennas, such as the spiral antenna, are designed "
        "to detect a circularly polarized wave. They will detect vertically and horizontally "
        "polarized waves, but they could miss a wave that is circularly polarized in the reverse "
        "direction (counterclockwise instead of clockwise, for example). Consequently, circularly "
        "polarized antennas are forbidden for many types of field measurements."))
    b.append(p(
        "All antennas discussed above respond to the electric field, <i>E</i>. As mentioned "
        "earlier, in the far-field region, the magnetic field, <i>B</i>, is simply 3.33 nT times the "
        "value of <i>E</i> expressed in volts per meter. In any other region, however, <i>B</i> is "
        "not so simply related to <i>E</i> and must be measured separately, using an antenna that "
        "responds to magnetic fields. A circular loop or coil of wire is such an antenna. The loop "
        "is cut at one point and the radio receiver or spectrum analyzer is connected between its "
        "two ends. For quantitative measurements, its antenna factor must be known. The factor can "
        "be measured by immersing the antenna in a known magnetic field and measuring its terminal "
        "voltage. To find the known magnetic field strength, the electric field is first measured, "
        "in the far-field region, using a tuned dipole antenna for which the factor is known. The "
        "magnetic field is then 3.33 nT times this value expressed in volts per meter. With the "
        "magnetic field thus determined, the antenna factor of the loop may be calculated, as "
        "required."))

    b.append(h3("Measurement Environment"))
    b.append(p(
        "A major difficulty with electromagnetic field measurements is repeatability of results. "
        "Electromagnetic fields are affected by any materials in their vicinity, even by poor "
        "conductors and dielectrics. The measurement environment must therefore be carefully "
        "defined, and similar environments must be used for all comparable measurements."))
    b.append(p(
        "The ideal environment would be one where (1) the only electromagnetic field source is the "
        "equipment under test (EUT) and (2) there is no &ldquo;foreign&rdquo; material at all that "
        "could affect the fields being measured. Unfortunately, the only natural location where "
        "this could be achieved is in outer space, since the Earth itself affects electromagnetic "
        "fields. Since this is impractical, attempts are made to simulate this environment on "
        "Earth."))
    b.append(p(
        "A large outdoor open area simulates a hemisphere of free space. Such a test site is "
        "appropriately called an open-field site. If the conductivity, permittivity, and "
        "permeability of the Earth were constant, every open-field site would have the same effect "
        "on the electromagnetic fields radiating from the EUT. The Earth's parameters do vary, "
        "however. To compensate for this variation, a large conductive floor, or ground plane, is "
        "laid under the EUT. This causes all electromagnetic waves to be totally reflected from the "
        "ground plane, so that the Earth's properties have no effect. The ground plane must be large "
        "enough so that it appears infinite with respect to the EUT and the associated test "
        "equipment. Acceptable dimensions are 1.73<i>d</i> × 2<i>d</i>, where <i>d</i> is the "
        "distance between the measurement antenna and the EUT, normally 3 or 10 m."))
    b.append(p(
        "Radiated emissions must be measured in all directions from the EUT, and at various angles "
        "of inclination. This is most easily achieved by placing the EUT on a turntable, which is "
        "then rotated during the test. To allow measurement at various inclination angles, the "
        "receiving antenna height must be varied, and this is accomplished by mounting it on a "
        "halyard. A typical open-field site appears in Figure 89.5."))
    b.append(fig(5, "en"))
    b.append(p(
        "An open-field site provides repeatable data only if there are no nearby trees or "
        "structures that could cause undesirable reflections. Before it can be reliably used, it "
        "must be tested. This is done by generating a known electromagnetic field and measuring it. "
        "The field is normally generated by a radio frequency oscillator driving a tuned dipole "
        "antenna, for which the radiation can be calculated (pp. 237–238 of Reference 2). This "
        "radiation is then measured as though it were generated by a typical device being tested. "
        "The ratio of the voltage at the transmitting antenna terminals to that at the receiving "
        "antenna terminals is known as the site attenuation. If the site attenuation is within 3 dB "
        "of its calculated value, the test site is deemed acceptable."))
    b.append(p(
        "Although an open-field site eliminates reflections, external field sources, such as "
        "licensed transmitters, still cause problems. Since electromagnetic radiation can travel "
        "thousands of miles, no open-field site will be completely free of electromagnetic fields. "
        "To eliminate the effects of these stray sources, testing must be performed inside a "
        "shielded enclosure. There, however, severe reflections occur, and measurements become "
        "inaccurate and unrepeatable."))
    b.append(p(
        "An ideal test environment would be a shielded enclosure lined with material that does not "
        "reflect electromagnetic waves. Such an enclosure is called an anechoic chamber, with the "
        "understanding that the name refers to electromagnetic echoes. Until recently, such "
        "chambers were not practical except at very high frequencies, but improvements are "
        "constantly being made. Such an enclosure is acceptable for testing if it meets the "
        "site-attenuation requirements of a true open field. The site attenuation must be measured "
        "at several points inside the chamber, to assure that the proximity of the chamber walls "
        "has no effect. Unfortunately, such chambers are at present very expensive."))
    b.append(p(
        "Another type of test chamber is the transverse electromagnetic (TEM) cell. This consists "
        "of an enlarged section of waveguide, in which the electromagnetic fields can be accurately "
        "predicted [3,4]. They are suitable only for testing small devices at relatively low "
        "frequencies. The TEM cell can be no larger than a wavelength at the frequency being "
        "tested. For example, to test at 200 MHz, the cell could be no larger than 1.5 m, or 5 ft, "
        "and the device itself must not exceed 1/6 of this value, or 10 in. For small devices, "
        "however, the TEM cell is very accurate and is unaffected by stray field sources."))
    b.append(p(
        "If a suitable anechoic chamber is not available, a device may be tested in an ordinary "
        "shielded enclosure to learn what frequencies it emits. The field strengths will be "
        "inaccurate due to the internal reflections. Then the device is tested in a true open-field "
        "site, and the suspected frequencies are measured quantitatively. Any field that exceeds "
        "the acceptable limits is then observed while the device is shut off. If it does not "
        "disappear, it is obviously not being generated by the EUT. This procedure is acceptable, "
        "although not as simple as testing inside an anechoic chamber."))
    b.append(p(
        "Preliminary measurements may even be performed in an ordinary room. They will not be "
        "comparable with similar measurements made anywhere else, because of the effects of nearby "
        "conductors and dielectrics. Here, also, the device must be shut off to decide if any "
        "emissions are from stray external sources instead of from the EUT. This procedure provides "
        "a rough estimate of the emissions from the EUT, and it usually saves time during any later "
        "testing at a true open-field site. The various measurement methods appear in Table "
        "89.4."))
    b.append(table_89_4("en"))
    b.append(p(
        "Permissible emission levels appear in the Code of Federal Regulations [5]. These rules "
        "assume open-field measurements, which are the most accurate possible. Even there, "
        "variations of ±6 dB are typical. Therefore, a manufacturer should allow a safety factor "
        "when performing measurements intended to assure compliance with government regulations. "
        "Otherwise, a device may pass when tested by the manufacturer but fail if later tested by "
        "the government using a supposedly identical test procedure. Since the government's "
        "measurements then prevail, the manufacturer's integrity could be questioned."))
    b.append(p("Further details on measurement techniques are available in References 2 and 6."))

    b.append(h2("Defining Terms"))
    b.append(_glossary(_GLOSS2_EN))

    b.append(h2("References"))
    b.append(refs(_REFS2))

    b.append(h2("Further Information"))
    b.append('<ul class="ref-list">%s</ul>' % "".join("<li>%s</li>" % i for i in _FURTHER2))
    return "".join(b)


# ================================================================ PAGE
def build(lang):
    vi = lang == "vi"
    switch = ("%s%s/" % (BASE_EN, CSLUG)) if vi else ("%s%s/" % (BASE_VI, CSLUG))
    title = ("Chương 89 — %s · Sổ tay Đo lường, Thiết bị đo và Cảm biến" % TITLE_VI if vi
             else "Chapter 89 — %s · Measurement, Instrumentation and Sensors Handbook"
                  % TITLE_EN)
    desc = ("Bản dịch tiếng Việt Chương 89 “Tương thích điện từ” của Daryl Gerke, William Kimmel và "
            "Jeffrey P. Mills — nối đất và che chắn trong hệ điện tử công nghiệp, rồi các phương "
            "pháp thử EMI và EMC, với 5 hình, 4 bảng, 3 công thức, hai bảng thuật ngữ và 12 tài "
            "liệu tham khảo." if vi
            else
            "Companion to Chapter 89 of the CRC Measurement Handbook — grounding and shielding in "
            "industrial electronic systems, then EMI and EMC test methods, with 5 figures, 4 tables, "
            "3 equations, two glossaries and 12 references.")
    crumb = ('<a href="/vi/books/">Sách</a> · <a href="%s">Sổ tay Đo lường, Thiết bị đo và Cảm '
             'biến</a> · Chương 89' % BASE_VI if vi else
             '<a href="/books/">Books</a> · <a href="%s">Measurement, Instrumentation and Sensors '
             'Handbook</a> · Chapter 89' % BASE_EN)
    meta = ("Chương 89 · theo Ch89.pdf (CRC Press, 1999) · 5 hình, 4 bảng, 3 công thức" if vi
            else "Chapter 89 · 5 figures, 4 tables, 3 equations")
    body = ('<main><article class="intranet-content reader"><div class="reader-hero">'
            '<div class="breadcrumb">%s</div><h1>%s</h1><p class="byline">%s</p>'
            '<div class="meta-line">%s</div></div><div class="prose">%s</div>%s</article></main>'
            % (crumb, TITLE_VI if vi else TITLE_EN, BYLINE if vi else BYLINE_EN, meta,
               body_vi() if vi else body_en(), chapter_nav(lang, 89)))
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
