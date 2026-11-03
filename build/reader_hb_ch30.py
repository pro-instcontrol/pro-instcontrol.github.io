# -*- coding: utf-8 -*-
"""Handbook Chapter 30 — Viscosity Measurement
(G. E. Leblanc — McMaster University; R. A. Secco — The University of Western
Ontario; M. Kostic — Northern Illinois University)

One section with seven subsections, 24 source pages, 12 figures, 4 tables and
46 numbered equations.

Run:  python build/reader_hb_ch30.py
"""
import os

import hb30fig as F
from reader_handbook import SLUG, head, header, footer
from chapter_nav import nav as chapter_nav

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSLUG = "ch30-viscosity-measurement"
TITLE_EN = "Viscosity Measurement"
TITLE_VI = "Đo độ nhớt"
BYLINE = ("G. E. Leblanc (McMaster University) · R. A. Secco (The University of Western Ontario) · "
          "M. Kostic (Northern Illinois University)")
BASE_EN = "/books/read/%s/" % SLUG
BASE_VI = "/vi/books/read/%s/" % SLUG
PREV_EN = "ch29-point-velocity-measurement"
PREV_VI = "ch29-point-velocity-measurement"
PREV_T_EN = "Point Velocity Measurement"
PREV_T_VI = "Đo vận tốc tại một điểm"


def fig(num, key, lang="vi"):
    svg, cap_vi, cap_en, aria_vi, aria_en = key
    if lang == "vi":
        cap = cap_vi
    else:
        cap = cap_en
        # The <svg> tag is built once, in hb30fig, with a Vietnamese aria-label
        # baked in by hbfig.svg(). Swap it for the English one, otherwise a
        # screen reader on this page announces Vietnamese.
        k = svg.find('aria-label="')
        if k >= 0:
            a = k + len('aria-label="')
            b = svg.find('"', a)
            svg = svg[:a] + (aria_en or aria_vi) + svg[b:]
    return ('<figure class="figure" id="fig-30-%d">%s<figcaption class="figcap">%s</figcaption></figure>'
            % (num, svg, cap))


def p(t):
    return "<p>%s</p>" % t


def h2(t, en=""):
    if en == t:
        en = ""
    sid = ""
    if t.startswith("30."):
        head_ = t[3:].split(" ", 1)[0]
        if head_.isdigit():
            sid = ' id="s30-%s"' % head_
    return '<h2%s>%s%s</h2>' % (sid, t, (' <span class="en">%s</span>' % en) if en else "")


def h3(t, en="", anchor=None):
    if en == t:
        en = ""
    a = ' id="%s"' % anchor if anchor else ""
    return '<h3%s>%s%s</h3>' % (a, t, (' <span class="en">%s</span>' % en) if en else "")


def h4(t, en=""):
    """Sub-heading one level below h3. There is no .prose h4 rule in library.css,
    so the size and spacing are set inline to sit between h3 and body text."""
    if en == t:
        en = ""
    return ('<h4 style="font-size:1rem;font-weight:700;margin:1.7rem 0 .5rem">%s%s</h4>'
            % (t, (' <span class="en">%s</span>' % en) if en else ""))


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


def table(hd, rows, cap, cls="tbl", widths=None, group=None):
    """A table with optional full-width group rows.

    group maps a row index to (heading, italic description) and is used for
    Table 30.2, whose three blocks each carry a bold title and a line of
    explanation before their own column header.
    """
    group = group or {}
    body = []
    for i, r in enumerate(rows):
        if i in group:
            g, d = group[i]
            body.append('<tr><td colspan="%d" style="background:#f3f1ec;font-weight:700;'
                        'border-top:1px solid #d9d4c8">%s</td></tr>' % (len(hd), g))
            if d:
                body.append('<tr><td colspan="%d" style="background:#f8f7f4;font-style:italic;'
                            'color:#555;font-size:.86rem">%s</td></tr>' % (len(hd), d))
            body.append('<tr>%s</tr>' % "".join(
                '<td style="background:#f8f7f4;font-size:.82rem;font-weight:600;color:#666">%s</td>'
                % h for h in hd))
        body.append("<tr>%s</tr>" % "".join("<td>%s</td>" % c for c in r))
    ths = "".join('<th%s>%s</th>' % ((' style="width:%s"' % widths[i]) if widths else "", h)
                  for i, h in enumerate(hd))
    return ('<div class="table-wrap"><table class="%s"><thead><tr>%s</tr></thead><tbody>%s</tbody></table></div>'
            '<p style="font-size:.84rem;color:#888;font-style:italic">%s</p>'
            % (cls, ths, "".join(body), cap))


def defs(items):
    """Defining-terms block, rendered as a two-column table so it inherits the
    reader's .tbl styling — there is no .deflist rule in library.css."""
    rows = "".join('<tr><th scope="row" style="text-align:left;width:30%%">%s</th><td>%s</td></tr>'
                   % (k, v) for k, v in items)
    return ('<div class="table-wrap"><table class="tbl"><tbody>%s</tbody></table></div>' % rows)


# ================================================================ table data

def _t301(lang):
    """Table 30.1 — six fluids at 20 °C and 1 atm. Short enough to keep in one
    column pair; the exponents are set with <sup> so the numbers align."""
    rows = [
        ["Air", "1,8 × 10<sup>−4</sup>"],
        ["Water", "1,0 × 10<sup>−3</sup>"],
        ["Mercury", "1,6 × 10<sup>−3</sup>"],
        ["Automotive engine oil (SAE 10W30)", "1,3 × 10<sup>−1</sup>"],
        ["Dish soap", "4,0 × 10<sup>−1</sup>"],
        ["Corn syrup", "6,0"],
    ]
    if lang == "vi":
        hd = ("Chất lưu", "Độ nhớt động lực (Pa·s)")
        cap = ("Bảng 30.1 · Độ nhớt động lực của một số chất lưu thông dụng, ở 20 °C và 1 atm. "
               "Khoảng biến thiên trong bảng đã là bốn bậc mười: từ không khí (10<sup>−4</sup> Pa·s) "
               "đến siro ngô (6 Pa·s).")
        rows = [[a, b.replace(",", ",")] for a, b in rows]
    else:
        hd = ("Fluid", "Shear dynamic viscosity (Pa·s)")
        cap = ("Table 30.1 · Shear dynamic viscosity of some common fluids, at 20 °C and 1 atm. "
               "The range in this table already spans four decades, from air at "
               "10<sup>−4</sup> Pa·s to corn syrup at 6 Pa·s.")
        rows = [[a, b.replace(",", ".")] for a, b in rows]
    return hd, rows, cap


def _t302(lang):
    """Table 30.2 — viscometer classification. Three blocks, each with a bold
    title and a line of explanation, so it needs group rows."""
    if lang == "vi":
        hd = ("Kiểu / hình học", "Đặc điểm cơ bản / ghi chú")
        cap = ("Bảng 30.2 · Phân loại nhớt kế và các đặc trưng cơ bản. Phân loại dựa trên cách "
               "khởi động và duy trì dòng chảy: kéo (bề mặt dụng cụ chuyển động) hay áp (chất lưu "
               "bị ép chảy qua một hình học cố định).")
        rows = [
            ["Trụ đồng tâm quay (Couette)",
             "Tốt cho độ nhớt thấp, tốc độ trượt cao; với R<sub>2</sub>/R<sub>1</sub> ≈ 1, xem "
             "Hình 30.3; khó làm sạch với chất lưu đặc"],
            ["Nón và bản phẳng quay",
             "Trượt đồng nhất, tốt nhất cho chất lưu phi Newton và ứng suất pháp; cần căn chỉnh "
             "tốt, khó nạp mẫu và dễ bay hơi"],
            ["Đĩa song song quay",
             "Giống nón – bản phẳng nhưng trượt không đồng nhất; trượt thay đổi theo chiều cao "
             "khe, dễ nạp mẫu"],
            ["Bản phẳng trượt song song",
             "Trượt đồng nhất, kết cấu đơn giản, tốt cho độ nhớt cao; khó nạp mẫu và khó kiểm "
             "soát khe"],
            ["Vật rơi (bi, trụ)",
             "Rất đơn giản, tốt ở nhiệt độ và áp suất cao; cần biết khối lượng riêng và cần cảm "
             "biến đặc biệt cho chất lưu đục; không tốt cho chất lưu nhớt-đàn hồi"],
            ["Bọt nổi",
             "Tương tự nhớt kế vật rơi; dùng cho chất lưu trong suốt"],
            ["Vật dao động",
             "Cần hằng số dụng cụ, tốt cho kim loại lỏng có độ nhớt thấp"],
            ["Mao quản dài (dòng Poiseuille)",
             "Đơn giản, trượt và dải đo rất cao, nhưng trượt rất không đồng nhất, không tốt cho "
             "chất lưu phụ thuộc thời gian, và tốn thời gian"],
            ["Lỗ / cốc (mao quản ngắn)",
             "Rất đơn giản, đáng tin cậy, nhưng không dùng được cho độ nhớt tuyệt đối và cho chất "
             "lưu phi Newton"],
            ["Khe (dòng áp giữa hai bản song song)",
             "Giống mao quản nhưng khó làm sạch"],
            ["Vành khuyên dọc trục, dòng áp",
             "Giống mao quản, trượt đều hơn, nhưng phức tạp hơn, có vấn đề lệch tâm và khó làm sạch"],
            ["Siêu âm",
             "Tốt cho chất lưu độ nhớt cao, thể tích mẫu nhỏ, cho cả độ nhớt trượt và độ nhớt "
             "thể tích cùng dữ liệu tính đàn hồi; có vấn đề với độ nhẵn bề mặt và căn chỉnh, "
             "việc xử lý số liệu phức tạp"],
        ]
        # Row indices, not block numbers: the drag block is rows 0-6, the
        # pressure block 7-10 and the single ultrasonic row 11. A group entry
        # inserts its heading *before* that row, so the indices must point at the
        # first row of each block, not one past the end of the previous one.
        group = {0: ("Kiểu dòng kéo:", "Dòng được tạo bởi chuyển động của biên/bề mặt dụng cụ "
                                       "nhờ ngoại lực hoặc trọng lực."),
                 7: ("Kiểu dòng áp:", "Chất lưu được đưa vào chuyển động trong một hình học cố "
                                      "định nhờ áp suất ngoài hoặc trọng lực."),
                 11: ("Loại khác:", None)}
        cap += (" Nguồn: C. W. Macosko, <i>Rheology: Principles, Measurements, and Applications</i>, "
                "New York: VCH, 1994.")
    else:
        hd = ("Type / geometry", "Basic characteristics / comments")
        cap = ("Table 30.2 · Viscometer classification and basic characteristics. The classification "
               "follows the way the flow is started and maintained: drag (an instrument surface "
               "moves) or pressure (the fluid is forced through a fixed geometry).")
        rows = [
            ["Rotating concentric cylinders (Couette)",
             "Good for low viscosity, high shear rates; for R<sub>2</sub>/R<sub>1</sub> ≈ 1, see "
             "Figure 30.3; hard to clean thick fluids"],
            ["Rotating cone and plate",
             "Homogeneous shear, best for non-Newtonian fluids and normal stresses; needs good "
             "alignment, problems with loading and evaporation"],
            ["Rotating parallel disks",
             "Similar to cone-and-plate, but inhomogeneous shear; shear varies with gap height, "
             "easy sample loading"],
            ["Sliding parallel plates",
             "Homogeneous shear, simple design, good for high viscosity; difficult loading and gap "
             "control"],
            ["Falling body (ball, cylinder)",
             "Very simple, good for high temperature and pressure; needs density and special "
             "sensors for opaque fluids, not good for viscoelastic fluids"],
            ["Rising bubble",
             "Similar to the falling body viscometer; for transparent fluids"],
            ["Oscillating body",
             "Needs an instrument constant, good for low-viscosity liquid metals"],
            ["Long capillary (Poiseuille flow)",
             "Simple, very high shear and range, but very inhomogeneous shear, bad for time "
             "dependency, and time consuming"],
            ["Orifice / cup (short capillary)",
             "Very simple, reliable, but not for absolute viscosity and non-Newtonian fluids"],
            ["Slit (parallel plates) pressure flow",
             "Similar to capillary, but difficult to clean"],
            ["Axial annulus pressure flow",
             "Similar to capillary, better shear uniformity, but more complex, eccentricity "
             "problem and difficult to clean"],
            ["Ultrasonic",
             "Good for high-viscosity fluids, small sample volume, gives shear and volume viscosity "
             "and elastic property data; problems with surface finish and alignment, complicated "
             "data reduction"],
        ]
        # See the Vietnamese branch above: 0-6 drag, 7-10 pressure, 11 ultrasonic.
        group = {0: ("Drag flow types:", "Flow set by motion of the instrument boundary/surface "
                                         "using external or gravity force."),
                 7: ("Pressure flow types:", "Fluid set in motion in a fixed instrument geometry by "
                                             "external or gravity pressure"),
                 11: ("Others / miscellaneous:", None)}
        cap += (" Adapted from C. W. Macosko, <i>Rheology: Principles, Measurements, and "
                "Applications</i>, New York: VCH, 1994.")
    return hd, rows, cap, group


def _t303(lang):
    """Table 30.3 — the ten error mechanisms, two columns."""
    if lang == "vi":
        hd = ("Sai số / hiệu ứng", "Nguyên nhân / ghi chú")
        cap = ("Bảng 30.3 · Các nguyên nhân gây sai số của nhớt kế. Không bao giờ đạt được dòng "
               "một chiều lý tưởng và hình học lý tưởng, nên mọi phép đo đều phải hiệu chỉnh ít "
               "nhất một vài mục trong bảng này.")
        rows = [
            ["Hiệu ứng đầu / mép", "Tổn thất năng lượng tại lối vào và lối ra của hình học đo chính"],
            ["Tổn thất động năng", "Mất áp suất chuyển thành động năng"],
            ["Dòng thứ cấp", "Tổn thất do dòng thứ cấp không mong muốn, xoáy, v.v.; tăng theo số "
                             "Reynolds"],
            ["Hình học không lý tưởng", "Sai lệch so với hình dạng, căn chỉnh và độ nhẵn lý tưởng"],
            ["Trượt không đồng nhất", "Quan trọng với chất lưu phi Newton"],
            ["Nhiệt độ thay đổi và đốt nóng do nhớt", "Nhiệt độ biến thiên theo thời gian và không "
                                                      "gian, ảnh hưởng tới độ nhớt đo được"],
            ["Rối", "Rối cục bộ và/hoặc từng phần thường xuất hiện ngay ở số Reynolds thấp"],
            ["Sức căng bề mặt", "Chênh lệch sức căng liên bề mặt"],
            ["Hiệu ứng đàn hồi", "Hiệu ứng đàn hồi của kết cấu và của chất lưu"],
            ["Các hiệu ứng khác", "Phụ thuộc mẫu thử: đứt gãy khi nóng chảy, lưu biến trễ, lưu biến "
                                  "tăng, v.v."],
        ]
    else:
        hd = ("Error / effect", "Cause / comment")
        cap = ("Table 30.3 · Different causes of viscometer errors. Neither ideal one-dimensional "
               "flow nor ideal geometry is ever achieved, so every measurement has to correct for "
               "at least a few of these.")
        rows = [
            ["End / edge effect", "Energy losses at the fluid entrance and exit of the main test "
                                  "geometry"],
            ["Kinetic energy losses", "Loss of pressure to kinetic energy"],
            ["Secondary flow", "Energy loss due to unwanted secondary flow, vortices, etc.; "
                               "increases with Reynolds number"],
            ["Non-ideal geometry", "Deviations from ideal shape, alignment and finish"],
            ["Shear rate non-uniformity", "Important for non-Newtonian fluids"],
            ["Temperature variation and viscous heating",
             "Variation in temperature, in time and space, influences the measured viscosity"],
            ["Turbulence", "Partial and/or local turbulence often develops even at low Reynolds "
                           "numbers"],
            ["Surface tension", "Difference in interfacial tensions"],
            ["Elastic effects", "Structural and fluid elastic effects"],
            ["Miscellaneous effects", "Depends on the test specimen: melt fracture, thixotropy, "
                                      "rheopexy"],
        ]
    return hd, rows, cap


def _t304(lang):
    """Table 30.4 — manufacturers. The source prints model and description in one
    ragged cell; two columns read better and lose nothing."""
    if lang == "vi":
        hd = ("Nhà sản xuất", "Model", "Mô tả")
        cap = ("Bảng 30.4 · Các nhà sản xuất nhớt kế. Danh sách giữ nguyên như bản in năm 1999; "
               "mọi hãng trong bảng đều có thể tìm thấy trên Internet, kèm thông tin liên hệ và "
               "mô tả sản phẩm cập nhật, đôi khi cả giá.")
        rows = [
            ["Brookfield Eng. Labs Inc.", "DV-I+", "Trụ đồng tâm"],
            ["Custom Scientific Inst. Inc.", "CS245", "Trụ đồng tâm"],
            ["Reologica Inst.", "Nhiều loại", "Bi rơi, mao quản, quay"],
            ["Haake GmbH", "Nhiều loại", "Bi rơi, quay"],
            ["Cannon Inst. Co.", "Nhiều loại", "Rất nhiều loại nhớt kế mao quản"],
            ["Toyo Seiki Seisaku-Sho Ltd.", "Capirograph", "Mao quản"],
            ["Gottfert Werkstoff-Prufmaschinen GmbH", "Nhiều loại",
             "Rất nhiều loại nhớt kế mao quản"],
            ["Cole-Palmer Inst. Co.", "GV2100", "Bi rơi"],
            ["Paar Physica U.S.A. Inc.", "Nhiều loại", "Trụ đồng tâm, bi rơi, mao quản"],
            ["Monsanto Inst. &amp; Equipment", "ODR 2000", "Nhớt kế dao động"],
            ["Nametre Co.", "Nhớt kế rung", "Nhớt kế dao động"],
            ["Rheometric Scientific Inc.", "RM180<br>RM265",
             "Nón – bản phẳng, bản phẳng song song<br>Trụ đồng tâm"],
            ["T. A. Instruments Inc.", "Nhiều loại", "Trụ đồng tâm"],
        ]
    else:
        hd = ("Manufacturer", "Model", "Description")
        cap = ("Table 30.4 · Viscometer manufacturers. The list is reproduced as printed in 1999; "
               "all of these manufacturers can be found on the Internet, with up-to-date contact "
               "details, product descriptions and in some cases pricing.")
        rows = [
            ["Brookfield Eng. Labs Inc.", "DV-I+", "Concentric cylinder"],
            ["Custom Scientific Inst. Inc.", "CS245", "Concentric cylinder"],
            ["Reologica Inst.", "Various", "Falling sphere, capillary, rotational"],
            ["Haake GmbH", "Various", "Falling sphere, rotational"],
            ["Cannon Inst. Co.", "Various", "Extensive variety of capillary viscometers"],
            ["Toyo Seiki Seisaku-Sho Ltd.", "Capirograph", "Capillary"],
            ["Gottfert Werkstoff-Prufmaschinen GmbH", "Various",
             "Extensive variety of capillary viscometers"],
            ["Cole-Palmer Inst. Co.", "GV2100", "Falling sphere"],
            ["Paar Physica U.S.A. Inc.", "Various", "Concentric cylinder, falling sphere, capillary"],
            ["Monsanto Inst. &amp; Equipment", "ODR 2000", "Oscillating viscometer"],
            ["Nametre Co.", "Vibrational viscometer", "Oscillating viscometer"],
            ["Rheometric Scientific Inc.", "RM180<br>RM265",
             "Cone-and-plate, parallel plate<br>Concentric cylinders"],
            ["T. A. Instruments Inc.", "Various", "Concentric cylinder"],
        ]
    return hd, rows, cap


def _refs30(lang):
    """The 25 numbered references. Numbers live inside the strings, so the list
    must be rendered with wl(), not ol(), which would number them twice."""
    return [
        "1. T. A. Litovitz and C. M. Davis, Structural and shear relaxation in liquids, in "
        "W. P. Mason (ed.), <i>Physical Acoustics: Principles and Methods, Vol. II, Part A, "
        "Properties of Gases, Liquids and Solutions</i>, New York: Academic Press, 1965, 281–349.",
        "2. Y. Bottinga and P. Richet, Silicate melts: The “anomalous” pressure dependence of the "
        "viscosity, <i>Geochim. Cosmochim. Acta</i>, 59, 2725–2731, 1995.",
        "3. J. Ferguson and Z. Kembłowski, <i>Applied Fluid Rheology</i>, New York: Elsevier, 1991.",
        "4. R. W. Whorlow, <i>Rheological Techniques</i>, 2nd ed., New York: Ellis Horwood, 1992.",
        "5. K. Walters, <i>Rheometry</i>, London: Chapman and Hall, 1975.",
        "6. J. M. Dealy, <i>Rheometers for Molten Plastics</i>, New York: Van Nostrand Reinhold, 1982.",
        "7. J. R. Van Wazer, J. W. Lyons, K. Y. Kim, and R. E. Colwell, <i>Viscosity and Flow "
        "Measurement</i>, New York: Interscience, 1963.",
        "8. C. W. Macosko, <i>Rheology: Principles, Measurements, and Applications</i>, New York: "
        "VCH, 1994.",
        "9. W. A. Wakeham, A. Nagashima, and J. V. Sengers (eds.), <i>Measurement of the Transport "
        "Properties of Fluids</i>, Oxford, UK: Blackwell Scientific, 1991.",
        "10. J. A. Jimenez and M. Kostic, A novel computerized viscometer/rheometer, <i>Rev. Sci. "
        "Instrum.</i>, 65(1), 229–241, 1994.",
        "11. DIN 53018 (Part 1 and 2), 53019, German National Standards.",
        "12. <i>Mark’s Standard Handbooks for Mechanical Engineers</i>, New York: McGraw-Hill, 1978.",
        "13. ASTM D445-71 standard.",
        "14. W. D. Kingery, <i>Viscosity in Property Measurements at High Temperatures</i>, New York: "
        "John Wiley &amp; Sons, 1959.",
        "15. H. Faxen, Die Bewegung einer Starren Kugel Längs der Achse eines mit Zaher Flüssigkeit "
        "Gefüllten Rohres: Arkiv för Matematik, <i>Astronomi och Fysik</i>, 27(17), 1–28, 1923.",
        "16. F. Gui and T. F. Irvine Jr., Theoretical and experimental study of the falling cylinder "
        "viscometer, <i>Int. J. Heat and Mass Transfer</i>, 37(1), 41–50, 1994.",
        "17. N. A. Park and T. F. Irvine Jr., Falling cylinder viscometer end correction factor, "
        "<i>Rev. Sci. Instrum.</i>, 66(7), 3982–3984, 1995.",
        "18. G. E. LeBlanc and R. A. Secco, High pressure stokes’ viscometry: a new <i>in-situ</i> "
        "technique for sphere velocity determination, <i>Rev. Sci. Instrum.</i>, 66(10), 5015–5018, "
        "1995.",
        "19. R. Clift, J. R. Grace, and M. E. Weber, <i>Bubbles, Drops, and Particles</i>, San Diego: "
        "Academic Press, 1978.",
        "20. M. Coutanceau and P. Thizon, Wall effect on the bubble behavior in highly viscous "
        "liquids, <i>J. Fluid Mech.</i>, 107, 339–373, 1981.",
        "21. R. Roscoe, Viscosity determination by the oscillating vessel method I: theoretical "
        "considerations, <i>Proc. Phys. Soc.</i>, 72, 576–584, 1958.",
        "22. T. Iida and R. I. L. Guthrie, <i>The Physical Properties of Liquid Metals</i>, Oxford, "
        "UK: Clarendon Press, 1988.",
        "23. H. J. McSkimin, Ultrasonic methods for measuring the mechanical properties of liquids "
        "and solids, in W. P. Mason (ed.), <i>Physical Acoustics: Principles and Methods, Vol. I "
        "Part A, Properties of Gases, Liquids and Solutions</i>, New York: Academic Press, 1964, "
        "271–334.",
        "24. P. Nasch, M. H. Manghnani, and R. A. Secco, A modified ultrasonic interferometer for "
        "sound velocity measurements in molten metals and alloys, <i>Rev. Sci. Instrum.</i>, 65, "
        "682–688, 1994.",
        "25. K. W. Katahara, C. S. Rai, M. H. Manghnani, and J. Balogh, An interferometric technique "
        "for measuring velocity and attenuation in molten rocks, <i>J. Geophys. Res.</i>, 86, "
        "11779–11786, 1981.",
    ]


def _refs30b(lang):
    """The three annotated further-reading entries. The source gives each a short
    description, which is kept because it is the only guidance on which of the
    three to open first."""
    if lang == "vi":
        return [
            "M. P. Ryan and J. Y. K. Blevins, <i>The Viscosity of Synthetic and Natural Silicate "
            "Melts and Glasses at High Temperatures and 1 Bar (10<sup>5</sup> Pascals) Pressure and "
            "at Higher Pressures</i>, U.S. Geological Survey Bulletin 1764, Denver, CO, 1987, 563 — "
            "bản tổng hợp rộng về số liệu độ nhớt, cả dạng bảng và dạng đồ thị, cùng các kỹ thuật "
            "chính dùng để đo độ nhớt trượt.",
            "M. E. O’Neill and F. Chorlton, <i>Viscous and Compressible Fluid Dynamics</i>, "
            "Chichester: Ellis Horwood, 1989 — phương pháp và kỹ thuật toán học, cùng mô tả lý "
            "thuyết về dòng chảy Newton không nén được và nén được lý tưởng.",
            "J. R. Van Wazer, J. W. Lyons, K. Y. Kim, and R. E. Colwell, <i>Viscosity and Flow "
            "Measurement: A Laboratory Handbook of Rheology</i>, New York: Interscience Publishers "
            "Div. of John Wiley &amp; Sons, 1963 — tổng quan toàn diện về các loại nhớt kế và các "
            "phép đo độ nhớt đơn giản trong phòng thí nghiệm.",
        ]
    return [
        "M. P. Ryan and J. Y. K. Blevins, <i>The Viscosity of Synthetic and Natural Silicate Melts "
        "and Glasses at High Temperatures and 1 Bar (10<sup>5</sup> Pascals) Pressure and at Higher "
        "Pressures</i>, U.S. Geological Survey Bulletin 1764, Denver, CO, 1987, 563 — an extensive "
        "compilation of viscosity data in tabular and graphic form and the main techniques used to "
        "measure shear viscosity.",
        "M. E. O’Neill and F. Chorlton, <i>Viscous and Compressible Fluid Dynamics</i>, Chichester: "
        "Ellis Horwood, 1989 — mathematical methods and techniques and a theoretical description of "
        "flows of Newtonian incompressible and ideal compressible fluids.",
        "J. R. Van Wazer, J. W. Lyons, K. Y. Kim, and R. E. Colwell, <i>Viscosity and Flow "
        "Measurement: A Laboratory Handbook of Rheology</i>, New York: Interscience Publishers "
        "Div. of John Wiley &amp; Sons, 1963 — a comprehensive overview of viscometer types and "
        "simple laboratory measurements of viscosity for liquids.",
    ]


# ================================================================ 30.1 (VI)

def sec_30_1_vi():
    b = []
    b.append(h2("30.1 Độ nhớt trượt", "Shear Viscosity"))
    b.append(p("G. E. Leblanc — Đại học McMaster · R. A. Secco — Đại học Western Ontario · "
               "M. Kostic — Đại học Northern Illinois."))
    b.append(p("Một tính chất cơ học quan trọng của chất lưu là <i>độ nhớt</i>. Những hệ vật lý và "
               "ứng dụng đa dạng đến mức khó có thể liệt kê hết — dòng chảy trong ống, dòng chảy của "
               "máu, việc bôi trơn các chi tiết động cơ, động lực học của hạt mưa, các vụ phun trào "
               "núi lửa, sự sinh từ trường của các hành tinh và các ngôi sao — đều liên quan đến "
               "dòng chảy chất lưu và đều bị chi phối ở một mức độ nào đó bởi độ nhớt của chất lưu."))
    b.append(p("<i>Độ nhớt</i> được định nghĩa là ma sát trong của một chất lưu. Bản chất vi mô của "
               "ma sát trong trong chất lưu tương tự với khái niệm vĩ mô về ma sát cơ học trong hệ "
               "một vật chuyển động trên một mặt phẳng đứng yên. Năng lượng phải được cấp (1) để "
               "thắng trạng thái quán tính của vật và mặt phẳng bị khoá vào nhau do độ nhám bề mặt, "
               "và (2) để khởi động và duy trì chuyển động của vật trên mặt phẳng. Trong chất lưu, "
               "năng lượng phải được cấp (1) để tạo ra các đơn vị dòng nhớt bằng cách phá vỡ liên "
               "kết giữa các nguyên tử và phân tử, và (2) để làm cho các đơn vị dòng đó chuyển động "
               "tương đối với nhau. Sức cản của chất lưu đối với việc tạo ra và làm chuyển động các "
               "đơn vị dòng là do độ nhớt của chất lưu, và độ nhớt chỉ thể hiện khi chất lưu đã "
               "được đưa vào chuyển động. Vì độ nhớt gắn với việc vận chuyển khối lượng với một vận "
               "tốc xác định, phản ứng nhớt được gọi là một <i>quá trình vận chuyển động lượng</i>."))
    b.append(p("Vận tốc của các đơn vị dòng trong chất lưu thay đổi tuỳ theo vị trí. Xét một chất "
               "lỏng nằm giữa hai bản phẳng song song đặt rất sát nhau như trên Hình 30.1. Một lực "
               "<i>F</i> tác dụng lên bản trên làm cho lớp chất lưu sát bản trên bị kéo theo phương "
               "của <i>F</i>. Lực tác dụng được truyền sang các lớp chất lưu bên dưới, mỗi lớp gắn "
               "với lớp phía trên đang dẫn động, nhưng với độ lớn giảm dần. Kết quả là vận tốc của "
               "mỗi lớp giảm dần khi ra xa bản trên, như các vectơ vận tốc ngắn dần trên Hình 30.1. "
               "Trong hệ này, lực tác dụng được gọi là <i>lực trượt</i> (khi đặt trên một đơn vị "
               "diện tích thì gọi là <i>ứng suất trượt</i>), còn tốc độ biến dạng tạo ra, minh hoạ "
               "bằng <i>gradien vận tốc</i> d<i>U</i><sub>x</sub>/d<i>z</i>, được gọi là <i>tốc độ "
               "biến dạng trượt</i>, γ̇<sub>zx</sub>. Biểu thức toán học mô tả phản ứng nhớt của hệ "
               "đối với ứng suất trượt rất đơn giản:"))
    b.append(eq("τ<sub>zx</sub> = η d<i>U</i><sub>x</sub> ⁄ d<i>z</i> = η γ̇<sub>zx</sub>", "30.1"))
    b.append(p("trong đó τ<sub>zx</sub>, ứng suất trượt, là lực trên một đơn vị diện tích do bản trên "
               "tác dụng theo phương <i>x</i> (và do đó bằng lực trên một đơn vị diện tích mà chất "
               "lưu tác dụng lên bản trên theo phương <i>x</i> dưới giả thiết có lớp không trượt tại "
               "mặt tiếp giáp chất lưu – bản trên); d<i>U</i><sub>x</sub>/d<i>z</i> là gradien của "
               "vận tốc theo phương <i>x</i> trong chất lưu; và η là <i>hệ số nhớt</i>. Trong trường "
               "hợp này, vì chỉ xét lực trượt làm phát sinh chuyển động của chất lưu, η được gọi "
               "chính xác hơn là <i>độ nhớt động lực</i>. Trong cơ học chất lưu, khuếch tán động "
               "lượng là một cách mô tả độ nhớt hữu ích hơn, ở đó chuyển động của chất lưu được xét "
               "mà không cần viện đến lực. Cách mô tả này gọi là <i>độ nhớt động học</i>, ν, và được "
               "xác định bằng cách chia độ nhớt động lực cho ρ, khối lượng riêng của chất lưu:"))
    b.append(eq("ν = η ⁄ ρ", "30.2"))
    b.append(fig(1, F.fig(1), "vi"))
    b.append(p("Định nghĩa độ nhớt theo phương trình 30.1 chỉ đúng cho dòng <i>tầng</i> (tức là dòng "
               "phân lớp, như các lớp xếp lên nhau) hay dòng chảy theo đường dòng như mô tả trên Hình "
               "30.1, và nó nói về <i>độ nhớt phân tử</i> hay <i>độ nhớt nội tại</i>. Độ nhớt phân tử "
               "là một tính chất của vật liệu, phụ thuộc vi mô vào độ bền liên kết, và được đặc trưng "
               "ở mức vĩ mô bởi sức cản của chất lưu đối với dòng chảy. Khi dòng là rối, sự khuếch "
               "tán động lượng bao gồm cả những đóng góp do chuyển động, đôi khi được gọi là <i>độ "
               "nhớt xoáy</i>, bên cạnh độ nhớt nội tại. Độ nhớt của hệ rối có thể lớn hơn độ nhớt "
               "của hệ chảy tầng tới 10<sup>6</sup> lần, tuỳ theo số Reynolds."))
    b.append(p("<i>Độ nhớt phân tử</i> được tách thành <i>độ nhớt trượt</i> và <i>độ nhớt khối</i> "
               "hay <i>độ nhớt thể tích</i>, η<sub>v</sub>, tuỳ theo kiểu biến dạng mà chất lưu chịu. "
               "Độ nhớt trượt là thước đo sức cản đối với dòng đẳng tích trong một trường trượt, còn "
               "độ nhớt thể tích là thước đo sức cản đối với dòng thể tích trong một trường ứng suất "
               "ba chiều. Với hầu hết chất lỏng, kể cả chất lỏng có liên kết hydro, liên kết yếu hoặc "
               "không liên kết, và các chất lỏng cao phân tử cũng như kim loại lỏng, tỉ số η/η<sub>v"
               "</sub> ≈ 1, cho thấy cơ chế trượt và cơ chế cấu trúc thể tích có liên hệ chặt với "
               "nhau [1]."))
    b.append(p("Độ nhớt trượt của hầu hết chất lỏng giảm khi nhiệt độ tăng và tăng khi áp suất tăng, "
               "ngược với xu hướng tương ứng của chất khí. Nhiệt độ tăng thường làm chất lỏng giãn nở "
               "và kéo theo độ bền liên kết lỏng giảm, đến lượt nó làm giảm ma sát trong. Áp suất "
               "tăng làm thể tích giảm và độ bền liên kết tăng, đến lượt nó làm tăng ma sát trong. "
               "Trong hầu hết tình huống, kể cả các ứng dụng kỹ thuật, ảnh hưởng của nhiệt độ lấn át "
               "ảnh hưởng ngược chiều của áp suất. Tuy vậy, trong bối cảnh các hành tinh, nơi không "
               "thể bỏ qua ảnh hưởng của áp suất, áp suất điều khiển độ nhớt đến mức — tuỳ thành phần "
               "— nó có thể gây ra những thay đổi cơ bản trong cấu trúc phân tử của chất lưu, dẫn đến "
               "độ nhớt giảm dị thường khi áp suất tăng [2]."))

    # ---- Newtonian and non-Newtonian
    b.append(h3("Chất lưu Newton và phi Newton", "Newtonian and Non-Newtonian Fluids",
                anchor="t30-newton"))
    b.append(p("Phương trình 30.1 được gọi là định luật nhớt của Newton, và nó phát biểu định nghĩa "
               "của Sir Isaac Newton về ứng xử nhớt của một lớp chất lưu ngày nay được gọi là chất "
               "lưu Newton."))
    b.append(p("Nếu độ nhớt trong toàn khối chất lưu không phụ thuộc tốc độ biến dạng thì chất lưu "
               "được gọi là <i>chất lưu Newton</i>. Hằng số tỉ lệ là hệ số nhớt, và đồ thị ứng suất "
               "trượt – tốc độ biến dạng của chất lưu Newton là một đường thẳng có độ dốc η, như "
               "đường liền trên Hình 30.2. Ví dụ về chất lưu Newton là chất khí nguyên chất, đơn pha, "
               "không liên kết; chất lỏng và dung dịch có khối lượng phân tử thấp như nước. Tuy "
               "nhiên, có một nhóm lớn chất lưu mà độ nhớt phụ thuộc tốc độ biến dạng. Những chất "
               "lưu như vậy được gọi là chất lưu phi Newton và việc nghiên cứu chúng được gọi là "
               "<i>lưu biến học</i>. Khi phân biệt ứng xử Newton và phi Newton, cần chú ý đến thang "
               "thời gian (cũng như các khác biệt ứng suất pháp và độ lệch pha trong phép thử động) "
               "liên quan đến quá trình chất lưu đáp ứng một nhiễu loạn trượt. Gradien vận tốc, "
               "d<i>U</i><sub>x</sub>/d<i>z</i>, trong chất lưu bằng tốc độ biến dạng trượt, γ̇, và "
               "do đó thang thời gian liên quan đến nhiễu loạn trượt đặt vào trạng thái cân bằng là "
               "<i>t</i><sub>s</sub>, trong đó <i>t</i><sub>s</sub> = γ̇<sup>−1</sup>. Một thang thời "
               "gian thứ hai, <i>t</i><sub>r</sub>, gọi là <i>thời gian trễ</i>, đặc trưng cho tốc độ "
               "mà ở đó biến dạng trong chất lưu có thể hồi phục, và liên quan đến thời gian để một "
               "đơn vị dòng điển hình di chuyển một quãng bằng đường kính trung bình của nó. Với "
               "nước ở nhiệt độ thường, <i>t</i><sub>r</sub> ~ 10<sup>−12</sup> s, và vì tốc độ biến "
               "dạng lớn hơn 10<sup>6</sup> s<sup>−1</sup> là hiếm trong thực tế, thời gian cần để "
               "điều chỉnh nhiễu loạn trượt trong nước ngắn hơn nhiều so với chu kỳ nhiễu loạn (tức "
               "<i>t</i><sub>r</sub> ≪ <i>t</i><sub>s</sub>). Tuy vậy, với các chất lỏng cao phân tử "
               "phi Newton như chất lỏng polymer, huyền phù keo và sợi, cũng như bột nhão và nhũ "
               "tương, thời gian đáp ứng dài của các đơn vị dòng lớn, nhớt dễ làm cho <i>t</i><sub>r"
               "</sub> &gt; <i>t</i><sub>s</sub>. Một ví dụ về chất lưu phi Newton là lưu huỳnh lỏng "
               "nguyên tố, trong đó các chuỗi dài (polymer) gồm tới 100.000 nguyên tử lưu huỳnh tạo "
               "thành những đơn vị dòng dễ vướng vào nhau, gắn chất lỏng thành một mạng “rắn giả”. "
               "Một ví dụ khác được biết đến nhiều là tương cà chua."))
    b.append(p("Theo Hình 30.2, dạng tổng quát hơn của phương trình 30.1 cũng tính đến phản ứng phi "
               "tuyến. Xét ứng suất trượt ban đầu cần để dòng bắt đầu chảy, τ<sub>xy</sub>(0), một "
               "số hạng tuyến tính theo nhiễu loạn nhỏ của tốc độ biến dạng, γ̇∂τ<sub>xy</sub>(0)/∂γ̇, "
               "và một số hạng phi tuyến <i>O</i>(γ̇²), sự phụ thuộc của ứng suất trượt vào tốc độ "
               "biến dạng, τ<sub>xy</sub>(γ̇), có thể được mô tả như sau:"))
    b.append(eq("τ<sub>xy</sub>(γ̇) = τ<sub>xy</sub>(0) + γ̇ ∂τ<sub>xy</sub>(0) ⁄ ∂γ̇ + "
                "<i>O</i>(γ̇²)", "30.3"))
    b.append(p("Với chất lưu Newton, ứng suất ban đầu ở tốc độ biến dạng bằng không là zero và hàm "
               "phi tuyến <i>O</i>(γ̇²) cũng bằng zero, nên phương trình 30.3 rút gọn thành phương "
               "trình 30.1, trong đó ∂τ<sub>xy</sub>(0)/∂γ̇ bằng η. Với chất lưu phi Newton, "
               "τ<sub>xy</sub>(0) có thể khác zero nhưng số hạng phi tuyến <i>O</i>(γ̇²) vẫn khác "
               "zero. Điều này đặc trưng cho chất lưu trong đó ứng suất trượt tăng không tỉ lệ với "
               "tốc độ biến dạng, như trên đường chấm gạch trên Hình 30.2, hoặc giảm không tỉ lệ với "
               "tốc độ biến dạng, như trên đường gạch đứt trên Hình 30.2. Kiểu ứng xử thứ nhất được "
               "gọi là <i>hoá đặc khi trượt</i> hay <i>giãn nở</i> (dilatancy), và một ví dụ là dung "
               "dịch đường đậm đặc trong nước. Kiểu thứ hai, phổ biến hơn nhiều, được gọi là <i>hoá "
               "loãng khi trượt</i> hay <i>giả dẻo</i>; kem, máu, hầu hết polymer và xi măng lỏng đều "
               "là ví dụ. Cả hai kiểu ứng xử đều nảy sinh từ việc định hướng lại phân tử hoặc hạt "
               "trong chất lưu làm tăng hoặc giảm ma sát trong đối với trượt. Ứng xử phi Newton cũng "
               "có thể xuất hiện ở chất lưu mà độ nhớt thay đổi theo thời gian tác dụng ứng suất "
               "trượt. Độ nhớt của tinh bột ngô và nước tăng dần theo thời gian tác dụng, và hiện "
               "tượng này được gọi là <i>lưu biến tăng</i> (rheopectic). Ngược lại, chất lỏng có độ "
               "nhớt giảm dần theo thời gian, như sơn không nhỏ giọt, vốn ứng xử như chất rắn cho đến "
               "khi chổi quét đặt lên nó đủ lâu để nó chảy tự do, được gọi là chất lưu <i>lưu biến "
               "trễ</i> (thixotropic)."))
    b.append(p("Biến dạng không hồi phục sau khi bỏ ứng suất là đặc trưng của phản ứng nhớt thuần "
               "tuý. Phản ứng ở thái cực còn lại đối với ứng suất ngoài là đàn hồi thuần tuý và được "
               "đặc trưng bởi một biến dạng cân bằng hồi phục hoàn toàn khi bỏ ứng suất. Có vô số "
               "mức trung gian hoặc tổ hợp của các phản ứng nhớt/đàn hồi đối với ứng suất ngoài, và "
               "những chất lưu này được gọi là <i>nhớt-đàn hồi</i>. Chất lưu thể hiện đàn hồi ở một "
               "miền ứng suất nào đó cần một ứng suất chảy giới hạn hoặc ứng suất chảy trước khi "
               "chảy như một chất lưu nhớt. Một phương trình cấu thành thực nghiệm đơn giản thường "
               "dùng cho kiểu ứng xử lưu biến này có dạng:"))
    b.append(eq("τ<sub>yx</sub> = τ<sub>y</sub> + γ̇<sup><i>n</i></sup>η<sub>p</sub>", "30.4"))
    b.append(p("trong đó τ<sub>y</sub> là <i>ứng suất chảy</i>, η<sub>p</sub> là <i>độ nhớt biểu "
               "kiến</i> hay còn gọi là độ nhớt dẻo, và số mũ <i>n</i> cho phép một loạt ứng xử phi "
               "Newton: <i>n</i> = 1 là ứng xử giả dẻo Newton và được gọi là <i>chất lưu Bingham</i>; "
               "<i>n</i> &lt; 1 là ứng xử hoá loãng khi trượt; và <i>n</i> &gt; 1 là ứng xử hoá đặc "
               "khi trượt. Bạn đọc muốn tìm hiểu thêm về lưu biến học ứng dụng nên xem [3–9]."))
    b.append(fig(2, F.fig(2), "vi"))

    # ---- Dimensions and units
    b.append(h3("Thứ nguyên và đơn vị của độ nhớt", "Dimensions and Units of Viscosity",
                anchor="t30-donvi"))
    b.append(p("Từ phương trình 30.1, thứ nguyên của độ nhớt động lực là M L<sup>−1</sup> "
               "T<sup>−1</sup> và đơn vị cơ bản trong hệ SI là pascal giây (Pa·s), trong đó "
               "1 Pa·s = 1 N s m<sup>−2</sup>. Đơn vị c.g.s. của dyn s cm<sup>−2</sup> là poise (P). "
               "Thứ nguyên của độ nhớt động học, từ phương trình 30.2, là L² T<sup>−1</sup> và đơn vị "
               "SI là m² s<sup>−1</sup>. Với hầu hết ứng dụng thực tế, đơn vị này thường quá lớn, nên "
               "đơn vị c.g.s. cm² s<sup>−1</sup>, hay stoke (St), được ưa dùng. Bảng 30.1 liệt kê độ "
               "nhớt động lực của một số chất lưu thông dụng ở áp suất khí quyển và 20 °C."))
    hd, rows, cap = _t301("vi")
    b.append(table(hd, rows, cap, widths=("62%", "38%")))

    # ---- Viscometer types
    b.append(h3("Các loại nhớt kế", "Viscometer Types", anchor="t30-loai"))
    b.append(p("Các dụng cụ đo độ nhớt được thiết kế để xác định “sức cản của chất lưu đối với dòng "
               "chảy” — tính chất của chất lưu đã được định nghĩa ở trên là độ nhớt. Dòng chảy của "
               "chất lưu trong một hình học dụng cụ cho trước xác định tốc độ biến dạng, và ứng suất "
               "tương ứng là thước đo sức cản đối với dòng chảy. Nếu tốc độ biến dạng hoặc ứng suất "
               "được đặt và điều khiển thì đại lượng còn lại, trong điều kiện mọi thứ khác như nhau, "
               "sẽ phụ thuộc độ nhớt của chất lưu. Nếu dòng là đơn giản (một chiều nếu có thể) đến "
               "mức có thể xác định chính xác tốc độ biến dạng và ứng suất từ các đại lượng đo được "
               "thì độ nhớt động lực tuyệt đối xác định được; nếu không thì chỉ xác lập được độ nhớt "
               "tương đối. Ví dụ, có thể đặt dòng chất lưu bằng cách kéo chất lưu bằng một bề mặt "
               "trượt hoặc quay, bằng vật rơi xuyên qua chất lưu, hoặc bằng cách ép chất lưu (nhờ áp "
               "suất ngoài hay trọng lực) chảy qua một hình học cố định như ống mao quản, vành "
               "khuyên, khe (giữa hai bản song song) hay lỗ. Sức cản tương ứng với dòng chảy được đo "
               "như lực hoặc mômen trên biên, hoặc như độ giảm áp. Lưu lượng hay thời gian chảy tràn "
               "biểu thị dòng chất lưu ứng với một sức cản dòng đặt trước, như độ giảm áp hay trọng "
               "lực. Nhớt kế được phân loại theo cách khởi động hoặc duy trì dòng chảy, như trong "
               "Bảng 30.2."))
    b.append(p("Nguyên lý cơ bản của mọi nhớt kế là tạo ra động học dòng càng đơn giản càng tốt, tốt "
               "nhất là dòng một chiều (đẳng tích), để xác định tốc độ biến dạng trượt một cách chính "
               "xác, dễ dàng và không phụ thuộc loại chất lưu. Sức cản đối với dòng đó được đo, và từ "
               "đó xác định ứng suất trượt. Độ nhớt trượt sau đó dễ dàng tìm được như tỉ số giữa ứng "
               "suất trượt và tốc độ biến dạng trượt tương ứng. Trên thực tế, không bao giờ đạt được "
               "dòng một chiều mong muốn cũng như hình học lý tưởng, và một số sai số, liệt kê trong "
               "Bảng 30.3, có thể xuất hiện và cần được tính đến [4–8]. Danh sách các nhà sản "
               "xuất/nhà phân phối nhớt kế và lưu biến kế thương mại được cho trong Bảng 30.4."))
    hd, rows, cap, group = _t302("vi")
    b.append(table(hd, rows, cap, widths=("32%", "68%"), group=group))
    hd, rows, cap = _t303("vi")
    b.append(table(hd, rows, cap, widths=("30%", "70%")))
    hd, rows, cap = _t304("vi")
    b.append(table(hd, rows, cap, widths=("36%", "18%", "46%")))

    # ---- concentric cylinders
    b.append(h4("Hai trụ đồng tâm", "Concentric Cylinders"))
    b.append(p("Ưu điểm chính của nhớt kế quay so với nhiều nhớt kế khác là khả năng làm việc liên tục "
               "ở một tốc độ trượt cho trước, nhờ đó có thể thực hiện thuận lợi các phép đo trạng "
               "thái ổn định khác. Nhờ vậy, nếu có phụ thuộc thời gian thì có thể phát hiện và xác "
               "định được. Ngoài ra, các phép đo tiếp theo có thể thực hiện trên cùng một dụng cụ và "
               "lấy mẫu ở các tốc độ trượt, nhiệt độ khác nhau, v.v. Vì những lý do này và các lý do "
               "khác, nhớt kế quay thuộc nhóm dụng cụ được dùng rộng rãi nhất cho các phép đo lưu "
               "biến."))
    b.append(p("Nhớt kế/lưu biến kế kiểu trụ đồng tâm thường được dùng khi cần xác định độ nhớt tuyệt "
               "đối, nghĩa là cần biết tốc độ trượt và ứng suất trượt được xác định tốt. Các dụng cụ "
               "này có nhiều cấu hình khác nhau và dùng được cho gần như mọi chất lưu. Có loại cho "
               "tốc độ trượt thấp và loại cho tốc độ trượt cao. Thảo luận đầy đủ hơn về nhớt kế/lưu "
               "biến kế trụ đồng tâm được trình bày ở nơi khác [4–9]. Trong nhớt kế kiểu Couette, "
               "việc quay trụ ngoài (hay cốc) làm giảm thiểu lực ly tâm — nguyên nhân gây ra xoáy "
               "Taylor. Xoáy này có thể xuất hiện trong nhớt kế kiểu Searle khi trụ trong (hay thỏi) "
               "quay."))
    b.append(p("Thông thường người ta đo mômen trên trụ đứng yên và tốc độ quay của trụ kia để xác "
               "định ứng suất trượt và tốc độ trượt, là những đại lượng cần cho việc tính độ nhớt. "
               "Khi đã đo được mômen <i>T</i>, có thể mô tả đơn giản ứng suất trượt của chất lưu tại "
               "một điểm bất kỳ có bán kính <i>r</i> giữa hai trụ, như trên Hình 30.3."))
    b.append(eq("τ<sub>rθ</sub>(<i>r</i>) = <i>T</i> ⁄ (2π<i>r</i>²<i>L</i><sub>e</sub>)", "30.5"))
    b.append(p("Trong phương trình 30.5, <i>L</i><sub>e</sub> = (<i>L</i> + <i>L</i><sub>c</sub>) là "
               "chiều dài hiệu dụng của trụ tại đó mômen được đo. Ngoài chiều dài <i>L</i> của trụ, "
               "nó còn tính đến hiệu chỉnh hiệu ứng đầu <i>L</i><sub>c</sub> [4–8]."))
    b.append(p("Với khe hẹp giữa hai trụ (β = <i>R</i><sub>2</sub>/<i>R</i><sub>1</sub> ≈ 1), không "
               "phụ thuộc loại chất lưu, prôfin vận tốc có thể xấp xỉ tuyến tính và tốc độ trượt "
               "trong khe sẽ đồng nhất:"))
    b.append(eq("γ̇(<i>r</i>) ≡ Ω<i>R̄</i> ⁄ (<i>R</i><sub>2</sub> − <i>R</i><sub>1</sub>)", "30.6"))
    b.append(p("trong đó Ω = (ω<sub>2</sub> − ω<sub>1</sub>) là tốc độ quay tương đối và "
               "<i>R̄</i> = (<i>R</i><sub>1</sub> + <i>R</i><sub>2</sub>)/2 là bán kính trung bình của "
               "trụ trong (1) và trụ ngoài (2). Thực ra prôfin tốc độ trượt ngang qua khe giữa hai "
               "trụ phụ thuộc tốc độ quay tương đối, các bán kính và cả những tính chất chưa biết "
               "của chất lưu — một bài toán tưởng như “không có lời giải”. Lời giải của bài toán "
               "phức tạp này được trình bày ở nơi khác [4–8] dưới dạng một chuỗi vô hạn, và đòi hỏi "
               "độ dốc của đồ thị logarit của <i>T</i> theo Ω trong miền quan tâm. Lưu ý rằng với "
               "trụ trong đứng yên (ω<sub>1</sub> = 0), là trường hợp thường gặp trong thực tế, Ω trở "
               "thành bằng ω<sub>2</sub>."))
    b.append(fig(3, F.fig(3), "vi"))
    b.append(p("Tuy vậy, có một thủ tục đơn giản hơn [10] cũng đã được tiêu chuẩn hoá trong các tiêu "
               "chuẩn Đức [11]. Với mọi chất lưu, kể cả chất lưu phi Newton, tồn tại một bán kính mà "
               "tại đó tốc độ trượt gần như không phụ thuộc loại chất lưu ứng với một Ω cho trước. "
               "Bán kính này, chỉ là hàm của hình học, được gọi là <i>bán kính đại diện</i>, "
               "<i>R</i><sub>R</sub>, và được xác định là vị trí ứng với cái gọi là ứng suất trượt "
               "đại diện, τ<sub>R</sub> = (τ<sub>1</sub> + τ<sub>2</sub>)/2, tức trung bình của các "
               "ứng suất tại mặt tiếp giáp của trụ ngoài và trụ trong với chất lưu:"))
    b.append(eq("<i>R</i><sub>R</sub> = <i>R</i><sub>1</sub>[2β² ⁄ (1 + β²)]<sup>1/2</sup> = "
                "<i>R</i><sub>2</sub>[2 ⁄ (1 + β²)]<sup>1/2</sup>", "30.7"))
    b.append(p("Vì tốc độ trượt tại bán kính đại diện gần như không phụ thuộc loại chất lưu (dù là "
               "Newton hay phi Newton), tốc độ trượt đại diện được tính đơn giản cho chất lưu Newton "
               "(<i>n</i> = 1) và <i>r</i> = <i>R</i><sub>R</sub>, theo [10]:"))
    b.append(eq("γ̇<sub>R</sub> = γ̇<sub>r=R<sub>R</sub></sub> = ω<sub>2</sub>[(β² + 1) ⁄ "
                "(β² − 1)]", "30.8"))
    b.append(p("Độ chính xác của các tham số đại diện phụ thuộc hình học của các trụ (β) và loại chất "
               "lưu (<i>n</i>)."))
    b.append(p("Tài liệu [10] chỉ ra rằng, với một dải loại chất lưu rộng đến mức không thực tế "
               "(0,35 &lt; <i>n</i> &lt; 3,5) và các hình học trụ (β = 1 đến 1,2), sai số cực đại nhỏ "
               "hơn 1 %. Do đó sai số gắn với khái niệm tham số đại diện là không đáng kể đối với "
               "phép đo thực tế."))
    b.append(p("Cuối cùng, độ nhớt (biểu kiến) của chất lưu được xác định bằng tỉ số giữa ứng suất "
               "trượt và tốc độ trượt tương ứng, dùng các phương trình 30.5 đến 30.8, như sau:"))
    b.append(eq("η ≡ η<sub>R</sub> = τ<sub>R</sub> ⁄ γ̇<sub>R</sub> = [(β² − 1) ⁄ "
                "(4πβ²<i>R</i><sub>1</sub>²<i>L</i><sub>e</sub>)](<i>T</i> ⁄ ω<sub>2</sub>) = "
                "[(β² − 1) ⁄ (4π<i>R</i><sub>2</sub>²<i>L</i><sub>e</sub>)](<i>T</i> ⁄ "
                "ω<sub>2</sub>)", "30.9"))
    b.append(p("Với một hình học trụ cho trước (β, <i>R</i><sub>2</sub> và <i>L</i><sub>e</sub>), có "
               "thể xác định độ nhớt từ phương trình 30.8 bằng cách đo <i>T</i> và ω<sub>2</sub>."))
    b.append(p("Như đã nêu, trong nhớt kế kiểu Couette, xoáy Taylor trong khe gần như bị loại bỏ "
               "hoàn toàn. Tuy vậy, xoáy ở đáy cốc vẫn có thể có mặt, và ảnh hưởng của chúng trở nên "
               "quan trọng khi số Reynolds của dòng đạt giá trị cỡ một [10, 11]. Hơn nữa, hiện tượng "
               "bất ổn định dòng và rối sẽ phát triển khi số Reynolds đạt giá trị 10³ đến 10⁴. Số "
               "Reynolds, Re, của dòng giữa hai trụ đồng tâm được định nghĩa [11] như sau:"))
    b.append(eq("Re = [ρω<sub>2</sub><i>R</i><sub>1</sub>² ⁄ (2η)][β² − 1]", "30.10"))

    # ---- cone and plate
    b.append(h4("Nhớt kế nón – bản phẳng", "Cone-and-Plate Viscometers"))
    b.append(p("Hình học nón – bản phẳng đơn giản cho tốc độ trượt đồng nhất và cho phép đo trực tiếp "
               "ứng suất pháp bậc một. Đây là dụng cụ phổ biến nhất để đo tính chất của chất lưu phi "
               "Newton. Các phương trình ứng suất trượt và tốc độ biến dạng trượt làm việc có thể "
               "được suy ra dễ dàng trong toạ độ cầu, như chỉ ra bởi hình học trên Hình 30.4, và "
               "tương ứng là:"))
    b.append(fig(4, F.fig(4), "vi"))
    b.append(eq("τ<sub>θφ</sub> = 3<i>T</i> ⁄ (2π<i>R</i>³)", "30.11"))
    b.append(p("và"))
    b.append(eq("γ̇ = Ω ⁄ θ<sub>0</sub>", "30.12"))
    b.append(p("trong đó <i>R</i> và θ<sub>0</sub> &lt; 0,1 rad (≈ 6°) là bán kính và góc của nón. Độ "
               "nhớt khi đó được tính dễ dàng như sau:"))
    b.append(eq("η = τ<sub>θφ</sub> ⁄ γ̇ = 3<i>T</i>θ<sub>0</sub> ⁄ (2πΩ<i>R</i>³)", "30.13"))
    b.append(p("Quán tính và dòng thứ cấp làm tăng, trong khi việc đốt nóng do trượt làm giảm mômen "
               "đo được (<i>T</i><sub>m</sub>). Chi tiết xem [4, 5]. Hiệu chỉnh mômen được cho như "
               "sau:"))
    b.append(eq("<i>T</i><sub>m</sub> ⁄ <i>T</i> = 1 + 6·10<sup>−4</sup>Re²", "30.14"))
    b.append(p("trong đó"))
    b.append(eq("Re = ρ[Ωθ<sub>0</sub><i>R</i>²] ⁄ η", "30.15"))

    # ---- parallel disks
    b.append(h4("Hai đĩa song song", "Parallel Disks"))
    b.append(p("Hình học này (Hình 30.5) gồm một đĩa quay trong một khoang hình trụ, tương tự hình "
               "học nón – bản phẳng, và nhiều dụng cụ cho phép dùng một trong hai. Tuy vậy tốc độ "
               "trượt không còn đồng nhất mà phụ thuộc khoảng cách hướng tâm từ trục quay và khe "
               "<i>h</i>, tức là:"))
    b.append(fig(5, F.fig(5), "vi"))
    b.append(eq("γ̇(<i>r</i>) = <i>r</i>Ω ⁄ <i>h</i>", "30.16"))
    b.append(p("Với chất lưu Newton, sau khi tích phân trên diện tích đĩa, mômen có thể được biểu "
               "diễn như hàm của độ nhớt, và từ đó xác định được độ nhớt:"))
    b.append(eq("η = 2<i>Th</i> ⁄ (πΩ<i>R</i>⁴)", "30.17"))

    # ---- capillary
    b.append(h3("Nhớt kế mao quản", "Capillary Viscometers", anchor="t30-maoquan"))
    b.append(p("<i>Nhớt kế mao quản</i> dựa trên lý thuyết dòng chảy tầng đã phát triển đầy đủ trong "
               "ống (dòng Hagen–Poiseuille) và được vẽ trên Hình 30.6. Chiều dài ống mao quản lớn hơn "
               "nhiều lần đường kính nhỏ của nó, nên dòng ở lối vào được bỏ qua hoặc được tính đến "
               "trong các phép đo chính xác hơn hay với ống ngắn hơn. Biểu thức cho ứng suất trượt "
               "tại thành ống là:"))
    b.append(fig(6, F.fig(6), "vi"))
    b.append(eq("τ<sub>w</sub> = (Δ<i>P</i> ⁄ <i>L</i>)·(<i>D</i> ⁄ 4)", "30.18"))
    b.append(p("và"))
    b.append(eq("Δ<i>P</i> = (<i>P</i><sub>1</sub> − <i>P</i><sub>2</sub>) + (<i>z</i><sub>1</sub> − "
                "<i>z</i><sub>2</sub>) − <i>C</i>ρ<i>V</i>² ⁄ 2", "30.19"))
    b.append(p("trong đó <i>C</i> ≥ 1,1; <i>P</i>, <i>z</i>, <i>V</i> = 4<i>Q</i>/[π<i>D</i>²] và "
               "<i>Q</i> lần lượt là hệ số hiệu chỉnh, áp suất, cao độ, vận tốc dòng trung bình và "
               "lưu lượng thể tích của chất lưu. Các chỉ số dưới 1 và 2 chỉ lối vào và lối ra."))
    b.append(p("Biểu thức cho tốc độ trượt tại thành ống là:"))
    b.append(eq("γ̇ = [(3<i>n</i> + 1) ⁄ 4<i>n</i>]·[8<i>V</i> ⁄ <i>D</i>]", "30.20"))
    b.append(p("trong đó <i>n</i> = d[log τ<sub>w</sub>]/d[log (8<i>V</i>/<i>D</i>)] là độ dốc của "
               "đường log(τ<sub>w</sub>) – log(8<i>V</i>/<i>D</i>) đo được. Khi đó độ nhớt được tính "
               "đơn giản như sau:"))
    b.append(eq("η = τ<sub>w</sub> ⁄ γ̇ = [4<i>n</i> ⁄ (3<i>n</i> + 1)]·[Δ<i>PD</i>² ⁄ "
                "(32<i>LV</i>)] = [4<i>n</i> ⁄ (3<i>n</i> + 1)]·[Δ<i>PD</i>⁴π ⁄ (128<i>QL</i>)]",
                "30.21"))
    b.append(p("Lưu ý rằng <i>n</i> = 1 với chất lưu Newton, nên số hạng thứ nhất, "
               "[4<i>n</i>/(3<i>n</i> + 1)], trở thành đơn vị và biến mất khỏi các phương trình trên. "
               "Ưu điểm của nhớt kế mao quản so với nhớt kế quay là chi phí thấp, độ chính xác cao "
               "(đặc biệt với ống dài hơn), và khả năng đạt tốc độ trượt rất cao, ngay cả với mẫu có "
               "độ nhớt cao. Nhược điểm chính là thời gian lưu mẫu lớn và tốc độ trượt thay đổi trên "
               "mặt cắt ngang dòng chảy, có thể làm thay đổi cấu trúc của chất lưu phức tạp, cũng như "
               "việc đốt nóng do trượt với mẫu có độ nhớt cao."))

    b.append(h4("Nhớt kế mao quản thuỷ tinh", "Glass Capillary Viscometers"))
    b.append(p("<i>Nhớt kế mao quản thuỷ tinh</i> rất đơn giản và rẻ. Hình học của chúng giống một ống "
               "chữ U với ít nhất hai bầu chứa nối với một ống mao quản có đường kính trong <i>D</i>. "
               "Chất lưu được hút lên một bầu chứa đã biết thể tích, <i>V</i><sub>0</sub>, giữa các "
               "vạch khắc. Thời gian chảy tràn, Δ<i>t</i>, là thời gian để thể tích đó chảy qua mao "
               "quản dưới tác dụng của trọng lực."))
    b.append(p("Từ phương trình 30.21 và tính đến việc <i>V</i><sub>0</sub> = (Δ<i>t</i>)<i>VD</i>²π/4 "
               "và Δ<i>P</i> = ρ<i>g</i>(<i>z</i><sub>1</sub> − <i>z</i><sub>2</sub>), độ nhớt động học "
               "có thể được biểu diễn như hàm của riêng thời gian chảy tràn, với số hạng cuối, "
               "<i>K</i>/Δ<i>t</i>, được thêm vào để tính đến hiệu chỉnh sai số, trong đó <i>K</i> là "
               "một hằng số [7]:"))
    b.append(eq("ν = η ⁄ ρ = {[4<i>n</i> ⁄ (3<i>n</i> + 1)]·[π<i>g</i>(<i>z</i><sub>1</sub> − "
                "<i>z</i><sub>2</sub>)<i>D</i>⁴ ⁄ (128<i>LV</i><sub>0</sub>)]}(Δ<i>t</i> − "
                "<i>K</i>Δ<i>t</i>)", "30.22"))
    b.append(p("Lưu ý rằng với một nhớt kế mao quản cho trước và <i>n</i> ≈ 1, số hạng trong ngoặc là "
               "hằng số. Số hạng hiệu chỉnh cuối cùng không đáng kể với tỉ số chiều dài/đường kính "
               "<i>L</i>/<i>D</i> lớn, khi đó độ nhớt động học tỉ lệ tuyến tính với thời gian chảy "
               "tràn đo được. Nhiều loại nhớt kế mao quản thuỷ tinh thương mại, như loại Cannon–Fenske "
               "hay tương tự, có thể mua từ các nhà khoa học và/hoặc nhà cung cấp. Chúng là biến thể "
               "của <i>nhớt kế Ostwald</i> đã được cải tiến để giảm thiểu một số hiệu ứng không mong "
               "muốn, để tăng dải đo, hoặc để đáp ứng các yêu cầu cụ thể của chất lưu thử, như tính "
               "đục, v.v. Nhớt kế mao quản thuỷ tinh thường được dùng cho chất lưu độ nhớt thấp."))

    b.append(h4("Lỗ/cốc, mao quản ngắn: nhớt kế Saybolt",
                "Orifice/Cup, Short Capillary: Saybolt Viscometer"))
    b.append(p("Nguyên lý của các nhớt kế này tương tự nhớt kế mao quản thuỷ tinh, chỉ khác là dòng "
               "chảy qua một mao quản ngắn (<i>L</i>/<i>D</i> ≪ 10) không thoả mãn hoặc chỉ xấp xỉ "
               "đúng dòng ống phát triển đầy đủ kiểu Hagen–Poiseuille. Ảnh hưởng của hiệu ứng đầu lối "
               "vào và của cột áp thuỷ tĩnh thay đổi là đáng kể. Khi đọc thời gian chảy tràn, "
               "Δ<i>t</i>, người ta biểu thị độ nhớt tương đối cho các mục đích so sánh và gọi đó là "
               "“giây nhớt kế”, như giây Saybolt hay độ Engler. Mặc dù công thức chuyển đổi, tương tự "
               "công thức của nhớt kế mao quản thuỷ tinh, có dùng các hằng số <i>k</i> và <i>K</i> "
               "trong phương trình 30.23, các hằng số này hoàn toàn là thực nghiệm và phụ thuộc loại "
               "chất lưu."))
    b.append(eq("ν = η ⁄ ρ = <i>k</i>Δ<i>t</i> − <i>K</i> ⁄ Δ<i>t</i>", "30.23"))
    b.append(p("trong đó <i>k</i> = 0,00226; 0,0216; 0,073 và <i>K</i> = 1,95; 0,60; 0,0631; tương ứng "
               "với Saybolt Universal (Δ<i>t</i> &lt; 100 s), Saybolt Furol (Δ<i>t</i> &gt; 40 s) và "
               "nhớt kế Engler, theo [12, 13]. Nhờ tính đơn giản, độ tin cậy và chi phí thấp, các "
               "nhớt kế này được dùng rộng rãi cho chất lưu Newton, như trong công nghiệp dầu và các "
               "ngành khác, nơi cần những tương quan đơn giản giữa các tính chất tương đối và kết quả "
               "mong muốn. Tuy vậy, các nhớt kế này không phù hợp để đo độ nhớt tuyệt đối, cũng không "
               "phù hợp với chất lưu phi Newton."))

    # ---- falling body
    b.append(h3("Phương pháp vật rơi", "Falling Body Methods", anchor="t30-roi"))
    b.append(h4("Bi rơi", "Falling Sphere"))
    b.append(p("Nhớt kế bi rơi là một trong những phương pháp sớm nhất và đơn giản nhất để xác định "
               "độ nhớt trượt tuyệt đối của một chất lưu Newton. Trong phương pháp này, một viên bi "
               "được thả rơi tự do qua một quãng đường đo trong môi trường chất lỏng nhớt và vận tốc "
               "của nó được xác định. Lực cản nhớt của viên bi rơi tạo ra một lực hãm, <i>F</i>, được "
               "mô tả bởi định luật Stokes:"))
    b.append(eq("<i>F</i> = 6πη<i>rU</i><sub>t</sub>", "30.24"))
    b.append(p("trong đó <i>r</i> là bán kính của viên bi và <i>U</i><sub>t</sub> là <i>vận tốc giới "
               "hạn</i> của vật rơi. Nếu một viên bi khối lượng riêng ρ<sub>2</sub> rơi qua một chất "
               "lưu khối lượng riêng ρ<sub>1</sub> trong một bình có kích thước vô hạn, thì khi cân "
               "bằng phương trình 30.24 với hợp lực của trọng lực và lực đẩy Archimedes tác dụng lên "
               "một viên bi đặc, phương trình kết quả cho độ nhớt tuyệt đối là:"))
    b.append(eq("η = 2<i>gr</i><sub>s</sub>²(ρ<sub>2</sub> − ρ<sub>1</sub>) ⁄ "
                "(9<i>U</i><sub>t</sub>)", "30.25"))
    b.append(p("Phương trình 30.25 cho thấy quan hệ giữa độ nhớt của một chất lưu và vận tốc giới hạn "
               "của một viên bi rơi trong đó. Vì thể tích bình chứa là hữu hạn nên cần sửa phương "
               "trình 30.25 để tính đến ảnh hưởng của thành bình (<i>W</i>) và của đáy bình "
               "(<i>E</i>) lên vận tốc của viên bi. Xét một bình trụ có bán kính <i>r</i> và chiều "
               "cao <i>H</i>, dạng hiệu chỉnh của phương trình 30.25 có thể viết là:"))
    b.append(eq("η = 2<i>gr</i><sub>s</sub>²(ρ<sub>2</sub> − ρ<sub>1</sub>)<i>W</i> ⁄ "
                "(9<i>U</i><sub>t</sub><i>E</i>)", "30.26"))
    b.append(p("trong đó"))
    b.append(eq("<i>W</i> = 1 − 2,104(<i>r</i><sub>s</sub> ⁄ <i>r</i>) + "
                "2,09(<i>r</i><sub>s</sub> ⁄ <i>r</i>)³ − 0,95(<i>r</i><sub>s</sub> ⁄ <i>r</i>)⁵",
                "30.27"))
    b.append(eq("<i>E</i> = 1 + 3,3(<i>r</i><sub>s</sub> ⁄ <i>H</i>)", "30.28"))
    b.append(p("Hiệu chỉnh thành bình được rút ra bằng thực nghiệm [15] và đúng trong khoảng 0,16 ≤ "
               "<i>r</i><sub>s</sub>/<i>r</i> ≤ 0,32. Ngoài khoảng này, ảnh hưởng của thành bình làm "
               "suy giảm đáng kể vận tốc giới hạn của viên bi, dẫn đến giá trị độ nhớt cao giả tạo."))
    b.append(fig(7, F.fig(7), "vi"))
    b.append(p("Hình 30.7 là sơ đồ phương pháp bi rơi và cho thấy sức hấp dẫn của phương pháp này — "
               "sự đơn giản về thiết kế. Cách đơn giản và tiết kiệm nhất khi áp dụng phương pháp này "
               "cho chất lỏng trong suốt là dùng một ống đong chia độ lớn chứa đầy chất lỏng. Với một "
               "khoảng cách được đánh dấu trên thành ống theo cả trục dọc và trục hướng tâm (vùng ít "
               "bị ảnh hưởng nhất bởi thành và đáy bình), một viên bi (như bi thép hoặc vật liệu "
               "không phản ứng với chất lỏng) đã biết khối lượng riêng và kích thước, nằm trong giới "
               "hạn hiệu chỉnh của bình, sẽ rơi tự do hết chiều dài ống. Khi viên bi đi qua vùng được "
               "đánh dấu có chiều dài <i>d</i> với vận tốc giới hạn của nó, thời gian đi hết quãng "
               "đường này cho phép tính vận tốc của viên bi. Khi đã đo tất cả các tham số của phương "
               "trình 30.26, có thể xác định độ nhớt trượt của chất lỏng."))
    b.append(p("Phương pháp này hữu ích với chất lỏng có độ nhớt trong khoảng 10<sup>−3</sup> Pa·s đến "
               "10<sup>5</sup> Pa·s. Nhờ sự đơn giản về thiết kế, phương pháp bi rơi đặc biệt thích "
               "hợp cho các nghiên cứu độ nhớt ở nhiệt độ và áp suất cao."))

    b.append(h4("Trụ rơi", "Falling Cylinder"))
    b.append(p("<i>Phương pháp trụ rơi</i> tương tự về ý tưởng với phương pháp bi rơi, chỉ khác là một "
               "trụ đặc, đầu phẳng, rơi tự do theo phương dọc trục của nó xuyên qua một mẫu chất lỏng "
               "trong một bình hình trụ. Sơ đồ cấu hình được trình bày trên Hình 30.8. Xét một trụ dài "
               "vô hạn, khối lượng riêng ρ<sub>2</sub>, bán kính <i>r</i><sub>c</sub>, rơi qua một "
               "chất lưu Newton khối lượng riêng ρ<sub>1</sub> có kích thước vô hạn, độ nhớt trượt "
               "thu được của chất lưu là:"))
    b.append(fig(8, F.fig(8), "vi"))
    b.append(eq("η = <i>gr</i><sub>c</sub>²(ρ<sub>2</sub> − ρ<sub>1</sub>) ⁄ (2<i>U</i><sub>t</sub>)",
                "30.29"))
    b.append(p("Cũng như với bi rơi, thể tích hữu hạn của bình đòi hỏi phải sửa phương trình 30.29 để "
               "tính đến ảnh hưởng của thành và đáy bình. Có thể rút ra một hiệu chỉnh cho ảnh hưởng "
               "của thành bình bằng cách cân bằng lực đẩy và lực hấp dẫn tác dụng lên trụ, có chiều "
               "dài <i>L</i>, với lực trượt trên các mặt bên và lực nén trên đầu trước cùng lực kéo "
               "trên đầu sau của trụ. Hệ số hiệu chỉnh thu được, hay hệ số hình học, <i>G</i>(<i>k</i>) "
               "(với <i>k</i> = <i>r</i><sub>c</sub>/<i>r</i>), phụ thuộc bán kính trụ và bán kính bình "
               "chứa, <i>r</i>, và được cho bởi:"))
    b.append(eq("<i>G</i>(<i>k</i>) = [<i>k</i>²(1 − ln <i>k</i>) − (1 + ln <i>k</i>)] ⁄ "
                "(1 + <i>k</i>²)", "30.30"))
    b.append(p("Khác với dòng chảy quanh một viên bi rơi, dòng chảy quanh một trụ đầu phẳng rơi rất "
               "phức tạp. Ảnh hưởng của đáy bình được giảm thiểu bằng cách tạo một khe nhỏ giữa trụ và "
               "thành bình. Với một trụ dài (được coi là dài nếu ψ ≥ 10, trong đó ψ = <i>L</i>/<i>r</i>) "
               "có bán kính gần bằng bán kính bình chứa, ảnh hưởng của thành sẽ chiếm ưu thế và làm "
               "giảm các hiệu ứng đầu xuống thành hiệu ứng bậc hai. Tuy vậy, một nhược điểm lớn của "
               "cách tiếp cận này là nếu trụ và bình chứa không đồng tâm thì ứng suất trượt không "
               "đồng nhất ở thành sẽ làm chuyển động đi xuống của trụ trở nên lệch tâm. Khả năng lệch "
               "tâm này đã thúc đẩy việc tìm lời giải giải tích gần đây cho dòng chảy quanh đầu trụ "
               "[16]. Một biểu thức giải tích cho hệ số hiệu chỉnh đầu (ECF) sau đó đã được rút ra "
               "[17] và được cho như sau:"))
    b.append(eq("1 ⁄ ECF = 1 + (8<i>k</i> ⁄ π<i>C</i><sub>w</sub>)(<i>G</i>(<i>k</i>) ⁄ ψ)", "30.31"))
    b.append(p("trong đó <i>C</i><sub>w</sub> = 1,003852 − 1,961019<i>k</i> + 0,9570952<i>k</i>². "
               "<i>C</i><sub>w</sub> được rút ra bán thực nghiệm [17] như một hệ số hiệu chỉnh thành "
               "bình kiểu đĩa. Điều này dựa trên ý tưởng rằng lực cản trên các đầu của trụ có thể "
               "được mô tả bằng lực cản trên một đĩa. Phương trình 30.31 đúng với ψ ≤ 30 và phù hợp "
               "với hiệu chỉnh rút ra bằng thực nghiệm [16] trong phạm vi 0,6 %."))
    b.append(p("Khi đã tính đến hiệu chỉnh thành và đầu, công thức làm việc để xác định độ nhớt trượt "
               "của một chất lưu Newton từ nhớt kế trụ rơi là:"))
    b.append(eq("η = [<i>gr</i><sub>c</sub>²(ρ<sub>2</sub> − ρ<sub>1</sub>)<i>G</i>(<i>k</i>)] ⁄ "
                "(2<i>U</i><sub>t</sub> ⁄ ECF)", "30.32"))
    b.append(p("Trước đây, phương pháp này chủ yếu được dùng để xác định độ nhớt tương đối giữa các "
               "chất lưu trong suốt. Chỉ từ khi có ECF [16, 17] phương pháp này mới có thể được dùng "
               "một cách chặt chẽ như một phương pháp độ nhớt tuyệt đối. Với một bình chứa và một trụ "
               "được thiết kế phù hợp, phương pháp này nay có thể cho độ nhớt tuyệt đối chính xác từ "
               "10<sup>−3</sup> Pa·s đến 10<sup>7</sup> Pa·s."))

    b.append(h4("Phương pháp vật rơi trong chất lỏng đục",
                "Falling Methods in Opaque Liquids"))
    b.append(p("Các phương pháp vật rơi mô tả ở trên đã được áp dụng rộng rãi cho chất lỏng trong suốt, "
               "nơi có thể quan sát bằng mắt (thường là quan sát trực tiếp) vật rơi. Với <i>chất lỏng "
               "đục</i> thì khác: phương pháp vật rơi đòi hỏi dùng một kỹ thuật cảm biến nào đó, "
               "thường là <i>tại chỗ</i>, để xác định vị trí của vật rơi theo thời gian. Các kỹ thuật "
               "đã thay đổi nhưng đều có chung khả năng phát hiện vật khi nó đi qua cảm biến. Một "
               "nghiên cứu gần đây ở áp suất cao [18] đã chứng minh rằng có thể lợi dụng sự tương "
               "phản về độ dẫn điện giữa viên bi và chất lỏng đục để cảm nhận động học viên bi đang "
               "chuyển động, nếu các điện cực được bố trí xuyên qua thành bình chứa như trên sơ đồ "
               "Hình 30.9. Các tài liệu tham khảo về những kỹ thuật <i>tại chỗ</i> tương tự được cho "
               "trong [18]."))
    b.append(fig(9, F.fig(9), "vi"))

    b.append(h4("Bọt nổi/giọt nổi", "Rising Bubble/Droplet"))
    b.append(p("Trong nhiều quá trình công nghiệp, nhớt kế bọt nổi đã được dùng hàng chục năm như một "
               "cách so sánh độ nhớt tương đối của chất lỏng trong suốt (như vecni, sơn bóng và bia). "
               "Tuy được dùng rộng rãi, ứng xử thực tế của bọt trong chất lỏng nhớt vẫn chưa được hiểu "
               "đầy đủ cho đến khi phương pháp này được giới thiệu [19]. Phương pháp bọt nổi từng được "
               "coi là một dẫn xuất của phương pháp bi rơi; tuy vậy có những khác biệt cơ bản giữa "
               "hai phương pháp. Khác biệt vật lý chính là (1) khối lượng riêng của bọt nhỏ hơn khối "
               "lượng riêng của chất lỏng xung quanh, và (2) bản thân bọt có một độ nhớt riêng. Mỗi "
               "khác biệt này đều có thể, và thực tế đã, dẫn đến những bài toán lưu biến phức tạp và "
               "chưa được giải thích đầy đủ. Nếu một bọt khí hay giọt chất lỏng có bán kính "
               "<i>r</i><sub>b</sub> và khối lượng riêng ρ′ nổi tự do trong một chất lỏng nhớt bao "
               "quanh có khối lượng riêng ρ thì độ nhớt trượt của chất lỏng bao quanh được xác định "
               "bởi:"))
    b.append(eq("η = (1 ⁄ ε)[2<i>gr</i><sub>b</sub>²(ρ − ρ′) ⁄ (9<i>U</i><sub>t</sub>)]", "30.33"))
    b.append(p("trong đó"))
    b.append(eq("ε = (2η + 3η′) ⁄ [3(η + η′)]", "30.34"))
    b.append(p("với η′ là độ nhớt của bọt. Cần lưu ý rằng khi η′ lớn (bi đặc) thì ε = 1, và phương "
               "trình 30.33 rút gọn thành phương trình 30.25. Với giá trị nhỏ của η′ (bọt khí), ε trở "
               "thành 2/3, và độ nhớt tính theo phương trình 30.33 lớn hơn 1,5 lần độ nhớt tính theo "
               "phương trình 30.25. Từ phương trình 30.33 và 30.25 có thể thấy rõ rằng vì khối lượng "
               "riêng của bọt nhỏ hơn khối lượng riêng của chất lỏng bao quanh nên vận tốc giới hạn "
               "của viên bi là âm, tức là chuyển động hướng lên, do chiều dương được chọn là chiều "
               "đi xuống."))
    b.append(p("Trong quá trình nổi, phải hết sức chú ý tránh nhiễm bẩn bọt và bề mặt bọt bởi tạp chất "
               "trong chất lỏng xung quanh. Tạp chất có thể khuếch tán qua bề mặt bọt và kết hợp với "
               "chất lưu bên trong. Vì bọt có độ nhớt thấp, chuyển động đi lên trong một môi trường "
               "nhớt tạo ra một lực cản tác dụng lên bọt, và lực cản này tạo ra chuyển động xoáy bên "
               "trong bọt. Chuyển động này có thể phân bố tạp chất một cách hiệu quả khắp toàn bộ bọt, "
               "từ đó làm thay đổi độ nhớt và khối lượng riêng của nó. Tạp chất trên bề mặt bọt có "
               "thể tạo thành một “lớp da” có thể ảnh hưởng đáng kể đến ứng xử của bọt, vì lớp da có "
               "khối lượng riêng và độ nhớt riêng không được tính trong phương trình 30.33. Những tạp "
               "chất bề mặt này cũng góp phần đáng kể vào sự phân bố không đồng nhất của lực căng "
               "liên bề mặt. Cân bằng các lực này là điều then chốt để hình thành một bọt cầu. Cách "
               "đơn giản nhất để giảm thiểu các hiệu ứng trên là dùng những bọt thật nhỏ, được tạo ra "
               "bằng cách đưa một thể tích xác định chất lưu (khí hoặc lỏng), bằng xyranh hay một "
               "dụng cụ tương tự, vào đầu dưới của bình trụ. Những bọt rất nhỏ ứng xử như bi đặc, nhờ "
               "đó lực căng liên bề mặt và chuyển động chất lưu bên trong không đáng kể."))
    b.append(p("Trong mọi nhớt kế bọt nổi, bọt được giả thiết là hình cầu. Các nghiên cứu thực nghiệm "
               "về hình dạng của bọt nổi tự do trong một bình hữu hạn [20] cho thấy (với độ chính xác "
               "1 %) bọt sẽ hình thành và giữ được dạng cầu nếu tỉ số giữa bán kính bọt và bán kính "
               "của bình trụ chứa nó nhỏ hơn 0,2. Những nghiên cứu này cũng cho thấy ảnh hưởng của "
               "thành bình lên vận tốc giới hạn của một bọt cầu nổi là làm giảm mạnh (tới 39 %) vận "
               "tốc quan sát được so với vận tốc đo trong một môi trường không bị giới hạn. Điều này "
               "ngụ ý rằng thành bình ảnh hưởng đến vận tốc của bọt nổi sớm hơn cả hình học của nó. "
               "Theo cách này, các hiệu ứng đầu được biết là lớn. Tuy vậy, một hệ số hiệu chỉnh chặt "
               "chẽ, bằng giải tích hoặc bằng thực nghiệm, vẫn chưa xuất hiện. Để lách qua điều này, "
               "tỉ số giữa chiều dài bình chứa và đường kính bọt phải nằm trong khoảng 10 đến 100. "
               "Như trong các phương pháp Stokes khác, điều này cho phép đo vận tốc của bọt tại những "
               "vị trí ít chịu ảnh hưởng của hiệu ứng đầu."))
    b.append(p("Xét tất cả những phức tạp nêu trên, cách tốt nhất để bảo đảm một phép đo độ nhớt ít "
               "bị ảnh hưởng nhất bởi chất lỏng được khảo sát và bởi hình học bình chứa là dùng những "
               "bọt thật nhỏ."))

    # ---- oscillating
    b.append(h3("Phương pháp dao động", "Oscillating Method", anchor="t30-daodong"))
    b.append(p("Nếu một chất lỏng được chứa trong một bình treo trên một hệ xoắn nào đó và được cho "
               "dao động quanh trục thẳng đứng của nó thì chuyển động của bình sẽ chịu một sự tắt "
               "dần dần. Trong trường hợp lý tưởng, sự tắt dần chuyển động của bình chỉ do <i>liên "
               "kết nhớt</i> giữa chất lỏng và bình, và giữa các lớp chất lỏng với nhau. Trong bất kỳ "
               "hệ thực tế nào cũng có thêm tổn thất ma sát trong hệ, góp phần vào sự tắt dần và phải "
               "được tính đến trong phân tích cuối cùng. Từ quan sát biên độ và chu kỳ của dao động "
               "thu được, có thể tính độ nhớt của chất lỏng. Sơ đồ của hệ cơ bản của phương pháp được "
               "vẽ trên Hình 30.10. Sau khi kích thích dao động ban đầu, một nguồn sáng (như laser "
               "công suất thấp) có thể được dùng để đo biên độ và chu kỳ dao động nhờ phản xạ từ gương "
               "gắn trên thanh treo, từ đó cho một số đo chính xác độ giảm lôga của dao động (δ) và "
               "các chu kỳ (<i>T</i>)."))
    b.append(fig(10, F.fig(10), "vi"))
    b.append(p("Nhiều công thức làm việc đã được rút ra để liên hệ chuyển động dao động của một bình "
               "bán kính <i>r</i> với độ nhớt tuyệt đối của chất lỏng. Công thức đáng tin cậy nhất là "
               "phương trình sau đây cho một bình hình trụ [21]:"))
    b.append(eq("η = [<i>I</i>δ ⁄ (π<i>r</i>³<i>HZ</i>)]²[1 ⁄ (πρ<i>T</i>)]", "30.35"))
    b.append(p("trong đó"))
    b.append(eq("<i>Z</i> = (1 + <i>r</i> ⁄ 4<i>H</i>)<i>a</i><sub>0</sub> − [(3 ⁄ 2 + 4<i>r</i> ⁄ "
                "π<i>H</i>) ⁄ ρ] + [(3 ⁄ 8 + 9<i>r</i> ⁄ 4<i>H</i>)<i>a</i><sub>2</sub> ⁄ 2ρ²]", "30.36"))
    b.append(eq("<i>p</i> = (πρ ⁄ η<i>T</i>)<sup>1/2</sup><i>r</i>", "30.37"))
    b.append(eq("<i>a</i><sub>0</sub> = 1 − (δ ⁄ 4π) − (3δ² ⁄ 32π²)", "30.38"))
    b.append(eq("<i>a</i><sub>2</sub> = 1 + (δ ⁄ 4π) + (δ² ⁄ 32π²)", "30.39"))
    b.append(p("<i>I</i> là mômen quán tính khối của hệ treo và ρ là khối lượng riêng của chất lỏng."))
    b.append(p("Một biểu thức thực dụng hơn của phương trình 30.35 thu được bằng cách đưa vào một số "
               "đơn giản hoá. Thứ nhất, có thể coi một cách hợp lý rằng δ là nhỏ (cỡ 10<sup>−2</sup> "
               "đến 10<sup>−1</sup>). Điều này làm <i>a</i><sub>0</sub> và <i>a</i><sub>2</sub> nhận "
               "giá trị 1 và −1 tương ứng. Thứ hai, ảnh hưởng của ma sát trong hệ treo và của môi "
               "trường xung quanh có thể được xác định bằng thực nghiệm và gói vào một biến duy nhất, "
               "δ<sub>0</sub>. Sau đó phải trừ giá trị này khỏi δ đo được. Một cách thông dụng để xác "
               "định δ<sub>0</sub> là quan sát độ giảm lôga của hệ với bình mẫu rỗng rồi trừ giá trị "
               "đó khỏi δ đo được. Với những sửa đổi này, phương trình 30.35 trở thành:"))
    b.append(eq("(δ − δ<sub>0</sub>) ⁄ ρ = [<i>A</i>(η ⁄ ρ)<sup>1/2</sup> − <i>B</i>(η ⁄ ρ) + "
                "<i>C</i>(η ⁄ ρ)<sup>3/2</sup>]", "30.40"))
    b.append(p("trong đó"))
    b.append(eq("<i>A</i> = (π<sup>3/2</sup> ⁄ <i>I</i>)[1 + (<i>r</i> ⁄ 4<i>H</i>)]<i>Hr</i>²"
                "<i>T</i><sup>1/2</sup>", "30.41"))
    b.append(eq("<i>B</i> = (π ⁄ <i>I</i>)[(3 ⁄ 2) + (4<i>r</i> ⁄ π<i>H</i>)]<i>Hr</i>²<i>T</i>",
                "30.42"))
    b.append(eq("<i>C</i> = (π<sup>3/2</sup> ⁄ 2<i>I</i>)[(3 ⁄ 8) + (9<i>r</i> ⁄ 4<i>H</i>)]"
                "<i>HrT</i><sup>3/2</sup>", "30.43"))
    b.append(p("Người ta đã lưu ý [22] rằng dạng giải tích của phương trình 30.40 cần một hệ số hiệu "
               "chỉnh ζ rút ra bằng thực nghiệm, gắn với dụng cụ, để phù hợp với các giá trị η đo được. "
               "Sự khác biệt giữa dạng giải tích và giá trị đo được nảy sinh từ chính những giả thiết "
               "trên. Tuy vậy, những giả thiết này là cần thiết vì việc giải các phương trình vi phân "
               "chuyển động của hệ này rất khó. Hệ số hiệu chỉnh phụ thuộc vật liệu, kích thước và "
               "khối lượng riêng của từng hệ riêng lẻ, nhưng nhìn chung nằm giữa 1,0 và 1,08. Hệ số "
               "hiệu chỉnh thu được bằng cách so sánh các giá trị độ nhớt của vật liệu chuẩn xác định "
               "bằng một hệ riêng lẻ (theo phương trình 30.35) với các giá trị độ nhớt thu được bằng "
               "một phương pháp đáng tin cậy khác, như phương pháp mao quản."))
    b.append(p("Với những xem xét trên, công thức cuối cùng của Roscoe cho độ nhớt trượt tuyệt đối "
               "là:"))
    b.append(eq("(δ − δ<sub>0</sub>) ⁄ ρ = ζ[<i>A</i>(η ⁄ ρ)<sup>1/2</sup> − <i>B</i>(η ⁄ ρ) + "
                "<i>C</i>(η ⁄ ρ)<sup>3/2</sup>]", "30.44"))
    b.append(p("<i>Phương pháp cốc dao động</i> đã và đang được dùng, và thích hợp nhất với các giá "
               "trị độ nhớt thấp trong khoảng 10<sup>−5</sup> Pa·s đến 10<sup>−2</sup> Pa·s. Thiết kế "
               "kín, đơn giản và khả năng dùng ở nhiệt độ cao đã làm phương pháp này rất phổ biến khi "
               "làm việc với kim loại lỏng."))

    # ---- ultrasonic
    b.append(h3("Phương pháp siêu âm", "Ultrasonic Methods", anchor="t30-sieuam"))
    b.append(p("Độ nhớt đóng vai trò quan trọng trong việc hấp thụ năng lượng của một <i>sóng âm</i> "
               "truyền qua chất lỏng. Bằng cách dùng sóng siêu âm (10<sup>4</sup> Hz &lt; <i>f</i> &lt; "
               "10<sup>8</sup> Hz), có thể đo phản ứng đàn hồi, nhớt-đàn hồi và nhớt của một chất lỏng "
               "với thời gian ngắn tới 10 ns. Khi độ nhớt của chất lưu thấp, thang thời gian dẫn đến "
               "giãn cấu trúc ngắn hơn chu kỳ sóng siêu âm và chất lưu được khảo sát ở trạng thái đã "
               "trễ. Chất lưu có độ nhớt cao chịu chuỗi sóng siêu âm sẽ đáp ứng như một chất lưu cứng "
               "hơn, vì cân bằng cấu trúc do nhiễu loạn âm không kịp hoàn tất trước chu kỳ sóng tiếp "
               "theo. Do đó, chất lưu được gọi là ở trạng thái chưa trễ, đặc trưng bởi sự tán sắc "
               "(vận tốc sóng phụ thuộc tần số) và các môđun đàn hồi phản ánh một chất lỏng cứng hơn "
               "nhiều. Sự phụ thuộc tần số của độ nhớt tương đối so với một độ nhớt tham chiếu "
               "(η<sub>0</sub>) ở tần số thấp, η/η<sub>0</sub>, và của độ hấp thụ trên một bước sóng, "
               "αλ, trong đó α là hệ số hấp thụ của chất lỏng và λ là bước sóng của sóng nén, với một "
               "chất lỏng có một thời gian trễ duy nhất, τ, được trình bày trên Hình 30.11. Độ hấp "
               "thụ cực đại trên một bước sóng xảy ra tại <i>tần số trễ</i>, khi ωτ = 1, và đi kèm với "
               "một bước nhảy của η/η<sub>0</sub>, cũng như của các tính chất khác như vận tốc và độ "
               "nén được. Tuỳ ứng dụng của các đại lượng đo được, việc xác định chất lưu đang ở trạng "
               "thái đã trễ hay chưa trễ là quan trọng."))
    b.append(fig(11, F.fig(11), "vi"))
    b.append(p("Sơ đồ một thiết bị điển hình để đo độ nhớt bằng phương pháp siêu âm được vẽ trên Hình "
               "30.12. Dao động cơ học được một <i>đầu biến năng áp điện</i> truyền xuống theo một "
               "trong các thanh đệm (BR-1 trên Hình 30.12) và đi vào mẫu chất lỏng, rồi được một đầu "
               "biến năng tương tự gắn trên thanh đệm kia, BR-2, thu lại. Ở cấu hình thanh đệm cố "
               "định, khi đã đạt trạng thái ổn định, tín hiệu đặt vào được tắt đi nhanh chóng. Tốc độ "
               "tắt dần của tín hiệu thu và khuếch đại, hiển thị trên dao động ký theo biên độ – thời "
               "gian như trên Hình 30.12(a), cho một số đo của α. Biên độ tín hiệu thu tắt dần như "
               "sau:"))
    b.append(eq("<i>A</i> = <i>A</i><sub>0</sub><i>e</i><sup>−(b+αc)t′</sup>", "30.45"))
    b.append(p("trong đó <i>A</i> là biên độ tắt dần thu được, <i>A</i><sub>0</sub> là biên độ vào, "
               "<i>b</i> là một hằng số của thiết bị phụ thuộc các tổn thất khác trong hệ như ở đầu "
               "biến năng, bình chứa, v.v., có thể đánh giá được bằng cách đo suy giảm trong một mẫu "
               "chuẩn, <i>c</i> là vận tốc sóng nén của chất lỏng, và <i>t</i>′ là thời gian. Ở tần số "
               "thấp, hệ số hấp thụ được biểu diễn theo độ nhớt thể tích và độ nhớt trượt như sau:"))
    b.append(eq("(η<sub>v</sub> + 4η ⁄ 3) = αρ<i>c</i>³ ⁄ (2π²<i>f</i>²)", "30.46"))
    b.append(fig(12, F.fig(12), "vi"))
    b.append(p("Một trong những phương pháp siêu âm sớm nhất để đo suy giảm trong chất lỏng dựa trên "
               "<i>giao thoa âm</i> [23]. Ngoài thiết bị cần để di chuyển và xác định vị trí của một "
               "trong các thanh đệm một cách chính xác, thiết bị thực nghiệm về cơ bản giống với cấu "
               "hình thanh đệm cố định [24]. Tuy vậy, phép đo phụ thuộc vào giao thoa sóng âm liên tục "
               "giữa sóng truyền và sóng phản xạ trong mẫu khi một trong các thanh đệm được dịch ra xa "
               "thanh kia. Suy giảm được đặc trưng bởi sự tắt dần của biên độ cực đại như hàm của bề "
               "dày mẫu nóng chảy, như trên giao thoa đồ ở Hình 30.12(b). Việc xác định α từ biên độ "
               "suy giảm quan sát được đòi hỏi lời giải số của một hệ phương trình mô tả sự lan truyền "
               "sóng phức tạp [25]. Các điều kiện lý tưởng được trình bày trong lý thuyết không tính "
               "đến những thứ như mặt sóng cong, đầu thanh đệm không song song, độ nhám bề mặt và lệch "
               "trục. Có thể xử lý những vấn đề này ở giai đoạn khớp hàm biên độ, nhưng điều đó có thể "
               "khó. Bạn đọc quan tâm nên xem [25] để biết thêm chi tiết."))
    b.append(p("Các phương pháp siêu âm chưa và sẽ không trở thành phương pháp chủ yếu để xác định độ "
               "nhớt chất lưu, đơn giản vì chúng phức tạp hơn về kỹ thuật so với các kỹ thuật nhớt kế "
               "thông thường. Và mặc dù nhớt kế siêu âm cung cấp thêm dữ liệu tính chất đàn hồi liên "
               "quan, chỗ đứng của nó là ở khả năng cung cấp độ nhớt thể tích. Vì không có nhớt kế nào "
               "khác đo được η<sub>v</sub>, các phép đo hấp thụ siêu âm giữ một vai trò duy nhất trong "
               "việc nghiên cứu độ nhớt thể tích."))

    # ---- references
    b.append(h3("Tài liệu tham khảo", "References"))
    b.append(wl(_refs30("vi")))
    b.append(h3("Đọc thêm", "Further Information"))
    b.append(wl(_refs30b("vi")))
    return "".join(b)


# ================================================================ English

def sec_30_1_en():
    b = []
    b.append(h2("30.1 Shear Viscosity"))
    b.append(p("G. E. Leblanc — McMaster University · R. A. Secco — The University of Western "
               "Ontario · M. Kostic — Northern Illinois University."))
    b.append(p("An important mechanical property of fluids is <i>viscosity</i>. Physical systems and "
               "applications as diverse as fluid flow in pipes, the flow of blood, lubrication of "
               "engine parts, the dynamics of raindrops, volcanic eruptions, planetary and stellar "
               "magnetic field generation, to name just a few, all involve fluid flow and are "
               "controlled to some degree by fluid viscosity."))
    b.append(p("<i>Viscosity</i> is defined as the internal friction of a fluid. The microscopic "
               "nature of internal friction in a fluid is analogous to the macroscopic concept of "
               "mechanical friction in the system of an object moving on a stationary planar surface. "
               "Energy must be supplied (1) to overcome the inertial state of the interlocked object "
               "and plane caused by surface roughness, and (2) to initiate and sustain motion of the "
               "object over the plane. In a fluid, energy must be supplied (1) to create viscous flow "
               "units by breaking bonds between atoms and molecules, and (2) to cause the flow units "
               "to move relative to one another. The resistance of a fluid to the creation and motion "
               "of flow units is due to the viscosity of the fluid, which only manifests itself when "
               "motion in the fluid is set up. Since viscosity involves the transport of mass with a "
               "certain velocity, the viscous response is called a <i>momentum transport process</i>."))
    b.append(p("The velocity of flow units within the fluid will vary, depending on location. "
               "Consider a liquid between two closely spaced parallel plates as shown in Figure 30.1. "
               "A force, <i>F</i>, applied to the top plate causes the fluid adjacent to the upper "
               "plate to be dragged in the direction of <i>F</i>. The applied force is communicated "
               "to neighboring layers of fluid below, each coupled to the driving layer above, but "
               "with diminishing magnitude. This results in the progressive decrease in velocity of "
               "each fluid layer, as shown by the decreasing velocity vectors in Figure 30.1, away "
               "from the upper plate. In this system, the applied force is called a <i>shear</i> "
               "(when applied over an area it is called a <i>shear stress</i>), and the resulting "
               "deformation rate of the fluid, as illustrated by the <i>velocity gradient</i> "
               "d<i>U</i><sub>x</sub>/d<i>z</i>, is called the <i>shear strain rate</i>, "
               "γ̇<sub>zx</sub>. The mathematical expression describing the viscous response of the "
               "system to the shear stress is simply:"))
    b.append(eq("τ<sub>zx</sub> = η d<i>U</i><sub>x</sub> ⁄ d<i>z</i> = η γ̇<sub>zx</sub>", "30.1"))
    b.append(p("where τ<sub>zx</sub>, the shear stress, is the force per unit area exerted on the "
               "upper plate in the <i>x</i>-direction (and hence is equal to the force per unit area "
               "exerted by the fluid on the upper plate in the <i>x</i>-direction under the "
               "assumption of a no-slip boundary layer at the fluid–upper plate interface); "
               "d<i>U</i><sub>x</sub>/d<i>z</i> is the gradient of the <i>x</i>-velocity in the "
               "<i>z</i>-direction in the fluid; and η is the <i>coefficient of viscosity</i>. In "
               "this case, because one is concerned with a shear force that produces the fluid "
               "motion, η is more specifically called the <i>dynamic viscosity</i>. In fluid "
               "mechanics, diffusion of momentum is a more useful description of viscosity where the "
               "motion of a fluid is considered without reference to force. This type of viscosity "
               "is called the <i>kinematic viscosity</i>, ν, and is derived by dividing dynamic "
               "viscosity by ρ, the mass density:"))
    b.append(eq("ν = η ⁄ ρ", "30.2"))
    b.append(fig(1, F.fig(1), "en"))
    b.append(p("The definition of viscosity by Equation 30.1 is valid only for <i>laminar</i> (i.e., "
               "layered or sheet-like) or streamline flow as depicted in Figure 30.1, and it refers "
               "to the molecular viscosity or <i>intrinsic viscosity</i>. The molecular viscosity is "
               "a property of the material that depends microscopically on bond strengths, and is "
               "characterized macroscopically as the fluid’s resistance to flow. When the flow is "
               "turbulent, the diffusion of momentum is comprised of viscous contributions from the "
               "motion, sometimes called the <i>eddy viscosity</i>, in addition to the intrinsic "
               "viscosity. Viscosities of turbulent systems can be as high as 10<sup>6</sup> times "
               "greater than viscosities of laminar systems, depending on the Reynolds number."))
    b.append(p("<i>Molecular viscosity</i> is separated into <i>shear viscosity</i> and bulk or "
               "<i>volume viscosity</i>, η<sub>v</sub>, depending on the type of strain involved. "
               "Shear viscosity is a measure of resistance to isochoric flow in a shear field, "
               "whereas volume viscosity is a measure of resistance to volumetric flow in a "
               "three-dimensional stress field. For most liquids, including hydrogen bonded, weakly "
               "associated or unassociated, and polymeric liquids as well as liquid metals, "
               "η/η<sub>v</sub> ≈ 1, suggesting that shear and structural viscous mechanisms are "
               "closely related [1]."))
    b.append(p("The shear viscosity of most liquids decreases with temperature and increases with "
               "pressure, which is opposite to the corresponding responses for gases. An increase in "
               "temperature usually causes expansion and a corresponding reduction in liquid bond "
               "strength, which in turn reduces the internal friction. Pressure causes a decrease in "
               "volume and a corresponding increase in bond strength, which in turn enhances the "
               "internal friction. For most situations, including engineering applications, "
               "temperature effects dominate the antagonistic effects of pressure. However, in the "
               "context of planetary interiors where the effects of pressure cannot be ignored, "
               "pressure controls the viscosity to the extent that, depending on composition, it can "
               "cause fundamental changes in the molecular structure of the fluid that can result in "
               "an anomalous viscosity decrease with increasing pressure [2]."))

    # ---- Newtonian and non-Newtonian
    b.append(h3("Newtonian and Non-Newtonian Fluids", anchor="t30-newton"))
    b.append(p("Equation 30.1 is known as Newton’s law of viscosity and it formulates Sir Isaac "
               "Newton’s definition of the viscous behavior of a class of fluids now called "
               "Newtonian fluids."))
    b.append(p("If the viscosity throughout the fluid is independent of strain rate, then the fluid "
               "is said to be a <i>Newtonian fluid</i>. The constant of proportionality is called "
               "the coefficient of viscosity, and a plot of stress vs. strain rate for Newtonian "
               "fluids yields a straight line with a slope of η, as shown by the solid line flow "
               "curve in Figure 30.2. Examples of Newtonian fluids are pure, single-phase, "
               "unassociated gases, liquids, and solutions of low molecular weight such as water. "
               "There is, however, a large group of fluids for which the viscosity is dependent on "
               "the strain rate. Such fluids are said to be non-Newtonian fluids and their study is "
               "called <i>rheology</i>. In differentiating between Newtonian and non-Newtonian "
               "behavior, it is helpful to consider the time scale (as well as the normal stress "
               "differences and phase shift in dynamic testing) involved in the process of a liquid "
               "responding to a shear perturbation. The velocity gradient, "
               "d<i>U</i><sub>x</sub>/d<i>z</i>, in the fluid is equal to the shear strain rate, γ̇, "
               "and therefore the time scale related to the applied shear perturbation about the "
               "equilibrium state is <i>t</i><sub>s</sub>, where <i>t</i><sub>s</sub> = "
               "γ̇<sup>−1</sup>. A second time scale, <i>t</i><sub>r</sub>, called the <i>relaxation "
               "time</i>, characterizes the rate at which the relaxation of the strain in the fluid "
               "can be accomplished and is related to the time it takes for a typical flow unit to "
               "move a distance equivalent to its mean diameter. For Newtonian water, "
               "<i>t</i><sub>r</sub> ~ 10<sup>−12</sup> s and, because shear rates greater than "
               "10<sup>6</sup> s<sup>−1</sup> are rare in practice, the time required for adjustment "
               "of the shear perturbation in water is much less than the shear perturbation period "
               "(i.e., <i>t</i><sub>r</sub> ≪ <i>t</i><sub>s</sub>). However, for non-Newtonian "
               "macromolecular liquids like polymeric liquids, for colloidal and fiber suspensions, "
               "and for pastes and emulsions, the long response times of large viscous flow units "
               "can easily make <i>t</i><sub>r</sub> &gt; <i>t</i><sub>s</sub>. An example of a "
               "non-Newtonian fluid is liquid elemental sulfur, in which long chains (polymers) of "
               "up to 100,000 sulfur atoms form flow units that are easily entangled, which bind the "
               "liquid in a “rigid-like” network. Another example of a well-known non-Newtonian "
               "fluid is tomato ketchup."))
    b.append(p("With reference to Figure 30.2, the more general form of Equation 30.1 also accounts "
               "for the nonlinear response. In terms of an initial shear stress required for flow to "
               "start, τ<sub>xy</sub>(0), an initial linear term in the Newtonian limit of a small "
               "range of strain rate, γ̇∂τ<sub>xy</sub>(0)/∂γ̇, and a nonlinear term "
               "<i>O</i>(γ̇²), the shear stress dependence on strain rate, τ<sub>xy</sub>(γ̇), can be "
               "described as:"))
    b.append(eq("τ<sub>xy</sub>(γ̇) = τ<sub>xy</sub>(0) + γ̇ ∂τ<sub>xy</sub>(0) ⁄ ∂γ̇ + "
                "<i>O</i>(γ̇²)", "30.3"))
    b.append(p("For a Newtonian fluid, the initial stress at zero shear rate is zero and the "
               "nonlinear function <i>O</i>(γ̇²) is zero, so Equation 30.3 reduces to Equation 30.1, "
               "since ∂τ<sub>xy</sub>(0)/∂γ̇ then equals η. For a non-Newtonian fluid, "
               "τ<sub>xy</sub>(0) may be zero but the nonlinear term <i>O</i>(γ̇²) is nonzero. This "
               "characterizes fluids in which shear stress increases disproportionately with strain "
               "rate, as shown in the dashed-dotted flow curve in Figure 30.2, or decreases "
               "disproportionately with strain rate, as shown in the dashed flow curve in Figure "
               "30.2. The former type of fluid behavior is known as <i>shear thickening</i> or "
               "dilatancy, and an example is a concentrated solution of sugar in water. The latter, "
               "much more common type of fluid behavior, is known as <i>shear thinning</i> or "
               "pseudo-plasticity; cream, blood, most polymers, and liquid cement are all examples. "
               "Both behaviors result from particle or molecular reorientations in the fluid that "
               "increase or decrease, respectively, the internal friction to shear. Non-Newtonian "
               "behavior can also arise in fluids whose viscosity changes with time of applied shear "
               "stress. The viscosity of corn starch and water increases with time duration of "
               "stress, and this is called <i>rheopectic behavior</i>. Conversely, liquids whose "
               "viscosity decreases with time, like nondrip paints, which behave like solids until "
               "the stress applied by the paint brush for a sufficiently long time causes them to "
               "flow freely, are called <i>thixotropic fluids</i>."))
    b.append(p("Fluid deformation that is not recoverable after removal of the stress is typical of "
               "the purely viscous response. The other extreme response to an external stress is "
               "purely elastic and is characterized by an equilibrium deformation that is fully "
               "recovered on removal of the stress. There are an infinite number of intermediate or "
               "combined viscous/elastic responses to external stress, which are grouped under the "
               "behavior known as <i>viscoelasticity</i>. Fluids that behave elastically in some "
               "stress range require a limiting or yield stress before they will flow as a viscous "
               "fluid. A simple, empirical, constitutive equation often used for this type of "
               "rheological behavior is of the form:"))
    b.append(eq("τ<sub>yx</sub> = τ<sub>y</sub> + γ̇<sup><i>n</i></sup>η<sub>p</sub>", "30.4"))
    b.append(p("where τ<sub>y</sub> is the <i>yield stress</i>, η<sub>p</sub> is an <i>apparent "
               "viscosity</i> called the plastic viscosity, and the exponent <i>n</i> allows for a "
               "range of non-Newtonian responses: <i>n</i> = 1 is pseudo-Newtonian behavior and is "
               "called a <i>Bingham fluid</i>; <i>n</i> &lt; 1 is shear thinning behavior; and "
               "<i>n</i> &gt; 1 is shear thickening behavior. Interested readers should consult "
               "[3–9] for further information on applied rheology."))
    b.append(fig(2, F.fig(2), "en"))

    # ---- Dimensions and units
    b.append(h3("Dimensions and Units of Viscosity", anchor="t30-donvi"))
    b.append(p("From Equation 30.1, the dimensions of dynamic viscosity are M L<sup>−1</sup> "
               "T<sup>−1</sup> and the basic SI unit is the Pascal second (Pa·s), where "
               "1 Pa·s = 1 N s m<sup>−2</sup>. The c.g.s. unit of dyn s cm<sup>−2</sup> is the poise "
               "(P). The dimensions of kinematic viscosity, from Equation 30.2, are L² T<sup>−1</sup> "
               "and the SI unit is m² s<sup>−1</sup>. For most practical situations, this is usually "
               "too large and so the c.g.s. unit of cm² s<sup>−1</sup>, or the stoke (St), is "
               "preferred. Table 30.1 lists some common fluids and their shear dynamic viscosities "
               "at atmospheric pressure and 20 °C."))
    hd, rows, cap = _t301("en")
    b.append(table(hd, rows, cap, widths=("62%", "38%")))

    # ---- Viscometer types
    b.append(h3("Viscometer Types", anchor="t30-loai"))
    b.append(p("The instruments for viscosity measurements are designed to determine “a fluid’s "
               "resistance to flow,” a fluid property defined above as viscosity. The fluid flow in "
               "a given instrument geometry defines the strain rates, and the corresponding stresses "
               "are the measure of resistance to flow. If strain rate or stress is set and "
               "controlled, then the other one will, everything else being the same, depend on the "
               "fluid viscosity. If the flow is simple (one dimensional, if possible) such that the "
               "strain rate and stress can be determined accurately from the measured quantities, "
               "the absolute dynamic viscosity can be determined; otherwise, the relative viscosity "
               "will be established. For example, the fluid flow can be set by dragging fluid with a "
               "sliding or rotating surface, falling body through the fluid, or by forcing the fluid "
               "(by external pressure or gravity) to flow through a fixed geometry, such as a "
               "capillary tube, annulus, a slit (between two parallel plates), or orifice. The "
               "corresponding resistance to flow is measured as the boundary force or torque, or "
               "pressure drop. The flow rate or efflux time represents the fluid flow for a set flow "
               "resistance, like pressure drop or gravity force. The viscometers are classified, "
               "depending on how the flow is initiated or maintained, as in Table 30.2."))
    b.append(p("The basic principle of all viscometers is to provide as simple flow kinematics as "
               "possible, preferably one-dimensional (isometric) flow, in order to determine the "
               "shear strain rate accurately, easily, and independent of fluid type. The resistance "
               "to such flow is measured, and thereby the shearing stress is determined. The shear "
               "viscosity is then easily found as the ratio between the shearing stress and the "
               "corresponding shear strain rate. Practically, it is never possible to achieve "
               "desired one-dimensional flow nor ideal geometry, and a number of errors, listed in "
               "Table 30.3, can occur and need to be accounted for [4–8]. A list of "
               "manufacturers/distributors of commercial viscometers/rheometers is given in Table "
               "30.4."))
    hd, rows, cap, grp = _t302("en")
    b.append(table(hd, rows, cap, widths=("26%", "74%"), group=grp))
    hd, rows, cap = _t303("en")
    b.append(table(hd, rows, cap, widths=("26%", "74%")))
    hd, rows, cap = _t304("en")
    b.append(table(hd, rows, cap, widths=("34%", "18%", "48%")))

    # ---- Concentric cylinders
    b.append(h4("Concentric Cylinders"))
    b.append(p("The main advantage of the rotational as compared to many other viscometers is its "
               "ability to operate continuously at a given shear rate, so that other steady-state "
               "measurements can be conveniently performed. That way, time dependency, if any, can "
               "be detected and determined. Also, subsequent measurements can be made with the same "
               "instrument and sampled at different shear rates, temperature, etc. For these and "
               "other reasons, rotational viscometers are among the most widely used class of "
               "instruments for rheological measurements."))
    b.append(p("Concentric cylinder-type viscometers/rheometers are usually employed when absolute "
               "viscosity needs to be determined, which in turn requires a knowledge of well-defined "
               "shear rate and shear stress data. Such instruments are available in different "
               "configurations and can be used for almost any fluid. There are models for low and "
               "high shear rates. More complete discussion on concentric cylinder "
               "viscometers/rheometers is given elsewhere [4–9]. In the Couette-type viscometer, the "
               "rotation of the outer cylinder, or cup, minimizes centrifugal forces, which cause "
               "Taylor vortices. The latter can be present in the Searle-type viscometer when the "
               "inner cylinder, or bob, rotates."))
    b.append(p("Usually, the torque on the stationary cylinder and rotational velocity of the other "
               "cylinder are measured for determination of the shear stress and shear rate, which is "
               "needed for viscosity calculation. Once the torque, <i>T</i>, is measured, it is "
               "simple to describe the fluid shear stress at any point with radius <i>r</i> between "
               "the two cylinders, as shown in Figure 30.3."))
    b.append(eq("τ<sub>rθ</sub>(<i>r</i>) = <i>T</i> ⁄ (2π<i>r</i>²<i>L</i><sub>e</sub>)", "30.5"))
    b.append(p("In Equation 30.5, <i>L</i><sub>e</sub> = (<i>L</i> + <i>L</i><sub>c</sub>) is the "
               "effective length of the cylinder at which the torque is measured. In addition to "
               "the cylinder’s length <i>L</i>, it takes into account the end-effect correction "
               "<i>L</i><sub>c</sub> [4–8]."))
    b.append(p("For a narrow gap between the cylinders (β = <i>R</i><sub>2</sub>/<i>R</i><sub>1</sub> "
               "≈ 1), regardless of the fluid type, the velocity profile can be approximated as "
               "linear, and the shear rate within the gap will be uniform:"))
    b.append(eq("γ̇(<i>r</i>) ≡ Ω<i>R̄</i> ⁄ (<i>R</i><sub>2</sub> − <i>R</i><sub>1</sub>)", "30.6"))
    b.append(p("where Ω = (ω<sub>2</sub> − ω<sub>1</sub>) is the relative rotational speed and "
               "<i>R̄</i> = (<i>R</i><sub>1</sub> + <i>R</i><sub>2</sub>)/2 is the mean radius of "
               "the inner (1) and outer (2) cylinders. Actually, the shear rate profile across the "
               "gap between the cylinders depends on the relative rotational speed, radii, and the "
               "unknown fluid properties, which seems an “open-ended” enigma. The solution of this "
               "complex problem is given elsewhere [4–8] in the form of an infinite series, and "
               "requires the slope of a logarithmic plot of <i>T</i> as a function of Ω in the range "
               "of interest. Note that for a stationary inner cylinder (ω<sub>1</sub> = 0), which is "
               "the usual case in practice, Ω becomes equal to ω<sub>2</sub>."))
    b.append(fig(3, F.fig(3), "en"))
    b.append(p("However, there is a simpler procedure [10] that has also been established by German "
               "standards [11]. For any fluid, including non-Newtonian fluids, there is a radius at "
               "which the shear rate is virtually independent of the fluid type for a given Ω. This "
               "radius, being a function of geometry only, is called the <i>representative radius</i>, "
               "<i>R</i><sub>R</sub>, and is determined as the location corresponding to the "
               "so-called representative shear stress, τ<sub>R</sub> = (τ<sub>1</sub> + "
               "τ<sub>2</sub>)/2, the average of the stresses at the outer and inner cylinder "
               "interfaces with the fluid, that is:"))
    b.append(eq("<i>R</i><sub>R</sub> = <i>R</i><sub>1</sub>[2β² ⁄ (1 + β²)]<sup>1/2</sup> = "
                "<i>R</i><sub>2</sub>[2 ⁄ (1 + β²)]<sup>1/2</sup>", "30.7"))
    b.append(p("Since the shear rate at the representative radius is virtually independent of the "
               "fluid type (whether Newtonian or non-Newtonian), the representative shear rate is "
               "simply calculated for Newtonian fluid (<i>n</i> = 1) and <i>r</i> = "
               "<i>R</i><sub>R</sub>, according to [10]:"))
    b.append(eq("γ̇<sub>R</sub> = γ̇<sub>r=R<sub>R</sub></sub> = ω<sub>2</sub>[(β² + 1) ⁄ "
                "(β² − 1)]", "30.8"))
    b.append(p("The accuracy of the representative parameters depends on the geometry of the "
               "cylinders (β) and fluid type (<i>n</i>)."))
    b.append(p("It is shown in [10] that, for an unrealistically wide range of fluid types "
               "(0.35 &lt; <i>n</i> &lt; 3.5) and cylinder geometries (β = 1 to 1.2), the maximum "
               "errors are less than 1%. Therefore, the error associated with the representative "
               "parameters concept is virtually negligible for practical measurements."))
    b.append(p("Finally, the (apparent) fluid viscosity is determined as the ratio between the shear "
               "stress and corresponding shear rate using Equations 30.5 to 30.8, as:"))
    b.append(eq("η ≡ η<sub>R</sub> = τ<sub>R</sub> ⁄ γ̇<sub>R</sub> = [(β² − 1) ⁄ (4πβ² "
                "<i>R</i><sub>1</sub>²<i>L</i><sub>e</sub>)](<i>T</i> ⁄ ω<sub>2</sub>) = [(β² − "
                "1) ⁄ (8πβ²<i>R</i><sub>R</sub>²<i>L</i><sub>e</sub>)](<i>T</i> ⁄ ω<sub>2</sub>)",
                "30.9"))
    b.append(p("For a given cylinder geometry (β, <i>R</i><sub>2</sub>, and <i>L</i><sub>e</sub>), "
               "the viscosity can be determined from Equation 30.9 by measuring <i>T</i> and "
               "ω<sub>2</sub>."))
    b.append(p("As already mentioned, in Couette-type viscometers, the Taylor vortices within the "
               "gap are virtually eliminated. However, vortices at the bottom can be present, and "
               "their influence becomes important when the Reynolds number reaches the value of "
               "unity [10, 11]. Furthermore, flow instability and turbulence will develop when the "
               "Reynolds number reaches values of 10<sup>3</sup> to 10<sup>4</sup>. The Reynolds "
               "number, Re, for the flow between concentric cylinders is defined [11] as:"))
    b.append(eq("Re = [ρω<sub>2</sub><i>R</i><sub>1</sub>² ⁄ (2η)][β² − 1]", "30.10"))

    # ---- Cone and plate
    b.append(h4("Cone-and-Plate Viscometers"))
    b.append(p("The simple cone-and-plate viscometer geometry provides a uniform rate of shear and "
               "direct measurements of the first normal stress difference. It is the most popular "
               "instrument for measurement of non-Newtonian fluid properties. The working shear "
               "stress and shear strain rate equations can be easily derived in spherical "
               "coordinates, as indicated by the geometry in Figure 30.4, and are, respectively:"))
    b.append(fig(4, F.fig(4), "en"))
    b.append(eq("τ<sub>θφ</sub> = 3<i>T</i> ⁄ (2π<i>R</i>³)", "30.11"))
    b.append(p("and"))
    b.append(eq("γ̇ = Ω ⁄ θ<sub>0</sub>", "30.12"))
    b.append(p("where <i>R</i> and θ<sub>0</sub> &lt; 0.1 rad (≈ 6°) are the cone radius and angle, "
               "respectively. The viscosity is then easily calculated as:"))
    b.append(eq("η = τ<sub>θφ</sub> ⁄ γ̇ = 3<i>T</i>θ<sub>0</sub> ⁄ (2πΩ<i>R</i>³)", "30.13"))
    b.append(p("Inertia and secondary flow increase while shear heating decreases the measured "
               "torque (<i>T</i><sub>m</sub>). For more details, see [4, 5]. The torque correction "
               "is given as:"))
    b.append(eq("<i>T</i><sub>m</sub> ⁄ <i>T</i> = 1 + 6·10<sup>−4</sup> Re²", "30.14"))
    b.append(p("where"))
    b.append(eq("Re = ρ[Ωθ<sub>0</sub><i>R</i>²] ⁄ η", "30.15"))

    # ---- Parallel disks
    b.append(h4("Parallel Disks"))
    b.append(p("This geometry (Figure 30.5), which consists of a disk rotating in a cylindrical "
               "cavity, is similar to the cone-and-plate geometry, and many instruments permit the "
               "use of either one. However, the shear rate is no longer uniform, but depends on "
               "radial distance from the axis of rotation and on the gap <i>h</i>, that is:"))
    b.append(fig(5, F.fig(5), "en"))
    b.append(eq("γ̇(<i>r</i>) = <i>r</i>Ω ⁄ <i>h</i>", "30.16"))
    b.append(p("For Newtonian fluids, after integration over the disk area, the torque can be "
               "expressed as a function of viscosity, so that the latter can be determined as:"))
    b.append(eq("η = 2<i>Th</i> ⁄ (πΩ<i>R</i>⁴)", "30.17"))

    # ---- Capillary
    b.append(h3("Capillary Viscometers", anchor="t30-maoquan"))
    b.append(p("The capillary viscometer is based on the fully developed laminar tube flow theory "
               "(Hagen–Poiseuille flow) and is shown in Figure 30.6. The capillary tube length is "
               "many times larger than its small diameter, so that entrance flow is neglected or "
               "accounted for in more accurate measurement or for shorter tubes. The expression for "
               "the shear stress at the wall is:"))
    b.append(fig(6, F.fig(6), "en"))
    b.append(eq("τ<sub>w</sub> = (Δ<i>P</i> ⁄ <i>L</i>)·(<i>D</i> ⁄ 4)", "30.18"))
    b.append(p("and"))
    b.append(eq("Δ<i>P</i> = (<i>P</i><sub>1</sub> − <i>P</i><sub>2</sub>) + "
                "(<i>z</i><sub>1</sub> − <i>z</i><sub>2</sub>) − <i>C</i>ρ<i>V</i>² ⁄ 2", "30.19"))
    b.append(p("where, <i>C</i> &gt; 1.1; <i>P</i>, <i>z</i>, <i>V</i> = 4<i>Q</i>/[π<i>D</i>²], and "
               "<i>Q</i> are correction factor, pressure, elevation, the mean flow velocity, and the "
               "fluid volume-flow rate, respectively. The subscripts 1 and 2 refer to the inlet and "
               "outlet, respectively."))
    b.append(p("The expression for the shear rate at the wall is:"))
    b.append(eq("γ̇ = [(3<i>n</i> + 1) ⁄ 4<i>n</i>]·[8<i>V</i> ⁄ <i>D</i>]", "30.20"))
    b.append(p("where <i>n</i> = d[log τ<sub>w</sub>]/d[log (8<i>V</i>/<i>D</i>)] is the slope of "
               "the measured log(τ<sub>w</sub>) – log(8<i>V</i>/<i>D</i>) curve. Then, the "
               "viscosity is simply calculated as:"))
    b.append(eq("η = τ<sub>w</sub> ⁄ γ̇ = [4<i>n</i> ⁄ (3<i>n</i> + 1)]·[Δ<i>PD</i>² ⁄ "
                "(32<i>LV</i>)] = [4<i>n</i> ⁄ (3<i>n</i> + 1)]·[πΔ<i>PD</i>⁴ ⁄ "
                "(128<i>QL</i>)]", "30.21"))
    b.append(p("Note that <i>n</i> = 1 for a Newtonian fluid, so the first term, "
               "[4<i>n</i>/(3<i>n</i> + 1)] becomes unity and disappears from the above equations. "
               "The advantages of capillary over rotational viscometers are low cost, high accuracy "
               "(particularly with longer tubes), and the ability to achieve very high shear rates, "
               "even with high-viscosity samples. The main disadvantages are high residence time and "
               "variation of shear across the flow, which can change the structure of complex test "
               "fluids, as well as shear heating with high-viscosity samples."))

    # ---- Glass capillary
    b.append(h4("Glass Capillary Viscometers"))
    b.append(p("Glass capillary viscometers are very simple and inexpensive. Their geometry "
               "resembles a U-tube with at least two reservoir bulbs connected to a capillary tube "
               "passage with inner diameter <i>D</i>. The fluid is drawn up into one bulb reservoir "
               "of known volume, <i>V</i><sub>0</sub>, between etched marks. The efflux time, Δ<i>t</i>, "
               "is measured for that volume to flow through the capillary under gravity."))
    b.append(p("From Equation 30.21 and taking into account that <i>V</i><sub>0</sub> = "
               "(Δ<i>t</i>)<i>VD</i>²π/4 and Δ<i>P</i> = ρ<i>g</i>(<i>z</i><sub>1</sub> − "
               "<i>z</i><sub>2</sub>), the kinematic viscosity can be expressed as a function of the "
               "efflux time only, with the last term, <i>K</i>/Δ<i>t</i>, added to account for "
               "error correction, where <i>K</i> is a constant [7]:"))
    b.append(eq("ν = η ⁄ ρ = {[4<i>n</i> ⁄ (3<i>n</i> + 1)]·[π<i>g</i>(<i>z</i><sub>1</sub> − "
                "<i>z</i><sub>2</sub>)<i>D</i>⁴ ⁄ (128<i>LV</i><sub>0</sub>)]}(Δ<i>t</i>) − "
                "<i>K</i> ⁄ Δ<i>t</i>", "30.22"))
    b.append(p("Note that for a given capillary viscometer and <i>n</i> ≈ 1, the bracketed term is a "
               "constant. The last correction term is negligible for a large capillary tube ratio, "
               "<i>L</i>/<i>D</i>, where kinematic viscosity becomes linearly proportional to "
               "measured efflux time. Various kinds of commercial glass capillary viscometers, like "
               "Cannon-Fenske type or similar, can be purchased from scientific and/or supply "
               "stores. They are the modified original Ostwald viscometer design in order to "
               "minimize certain undesirable effects, to increase the viscosity range, or to meet "
               "specific requirements of the tested fluids, like opacity, etc. Glass capillary "
               "viscometers are often used for low-viscosity fluids."))

    # ---- Saybolt
    b.append(h4("Orifice/Cup, Short Capillary: Saybolt Viscometer"))
    b.append(p("The principle of these viscometers is similar to glass capillary viscometers, "
               "except that the flow through a short capillary (<i>L</i>/<i>D</i> ≪ 10) does not "
               "satisfy or even approximate the Hagen–Poiseuille, fully developed, pipe flow. The "
               "influences of entrance end-effect and changing hydrostatic heads are considerable. "
               "The efflux time reading, Δ<i>t</i>, represents relative viscosity for comparison "
               "purposes and is expressed as “viscometer seconds,” like the Saybolt seconds, or "
               "Engler seconds or degrees. Although the conversion formula, similar to glass "
               "capillary viscometers, is used, the constants <i>k</i> and <i>K</i> in Equation "
               "30.23 are purely empirical and dependent on fluid types."))
    b.append(eq("ν = η ⁄ ρ = <i>k</i>Δ<i>t</i> − <i>K</i> ⁄ Δ<i>t</i>", "30.23"))
    b.append(p("where <i>k</i> = 0.00226, 0.0216, 0.073; and <i>K</i> = 1.95, 0.60, 0.0631; for "
               "Saybolt Universal (Δ<i>t</i> &lt; 100 s), Saybolt Furol (Δ<i>t</i> &gt; 40 s), and "
               "Engler viscometers, respectively [12, 13]. Due to their simplicity, reliability, and "
               "low cost, these viscometers are widely used for Newtonian fluids, like in oil and "
               "other industries, where the simple correlations between the relative properties and "
               "desired results are needed. However, these viscometers are not suitable for absolute "
               "viscosity measurement, nor for non-Newtonian fluids."))

    # ---- Falling body
    b.append(h3("Falling Body Methods", anchor="t30-roi"))
    b.append(h4("Falling Sphere"))
    b.append(p("The falling sphere viscometer is one of the earliest and least involved methods to "
               "determine the absolute shear viscosity of a Newtonian fluid. In this method, a "
               "sphere is allowed to fall freely a measured distance through a viscous liquid medium "
               "and its velocity is determined. The viscous drag of the falling sphere results in the "
               "creation of a restraining force, <i>F</i>, described by Stokes’ law:"))
    b.append(eq("<i>F</i> = 6πη<i>r</i><sub>s</sub><i>U</i><sub>t</sub>", "30.24"))
    b.append(p("where <i>r</i><sub>s</sub> is the radius of the sphere and <i>U</i><sub>t</sub> is "
               "the terminal velocity of the falling body. If a sphere of density ρ<sub>2</sub> is "
               "falling through a fluid of density ρ<sub>1</sub> in a container of infinite extent, "
               "then by balancing Equation 30.24 with the net force of gravity and buoyancy exerted "
               "on a solid sphere, the resulting equation of absolute viscosity is:"))
    b.append(eq("η = 2<i>gr</i><sub>s</sub>²(ρ<sub>2</sub> − ρ<sub>1</sub>) ⁄ "
                "(9<i>U</i><sub>t</sub>)", "30.25"))
    b.append(p("Equation 30.25 shows the relation between the viscosity of a fluid and the terminal "
               "velocity of a sphere falling within it. Having a finite container volume "
               "necessitates the modification of Equation 30.25 to correct for effects on the "
               "velocity of the sphere due to its interaction with container walls (<i>W</i>) and "
               "ends (<i>E</i>). Considering a cylindrical container of radius <i>r</i> and height "
               "<i>H</i>, the corrected form of Equation 30.25 can be written as:"))
    b.append(eq("η = 2<i>gr</i><sub>s</sub>²(ρ<sub>2</sub> − ρ<sub>1</sub>)<i>W</i> ⁄ "
                "(9<i>U</i><sub>t</sub><i>E</i>)", "30.26"))
    b.append(p("where"))
    b.append(eq("<i>W</i> = 1 − 2.104(<i>r</i><sub>s</sub> ⁄ <i>r</i>) + "
                "2.09(<i>r</i><sub>s</sub> ⁄ <i>r</i>)³ − 0.95(<i>r</i><sub>s</sub> ⁄ "
                "<i>r</i>)⁵", "30.27"))
    b.append(eq("<i>E</i> = 1 + 3.3(<i>r</i><sub>s</sub> ⁄ <i>H</i>)", "30.28"))
    b.append(p("The wall correction was empirically derived [15] and is valid for 0.16 ≤ "
               "<i>r</i><sub>s</sub>/<i>r</i> ≤ 0.32. Beyond this range, the effects of container "
               "walls significantly impair the terminal velocity of the sphere, thus giving rise to a "
               "false high viscosity value."))
    b.append(fig(7, F.fig(7), "en"))
    b.append(p("Figure 30.7 is a schematic diagram of the falling sphere method and demonstrates the "
               "attraction of this method — its simplicity of design. The simplest and most "
               "cost-effective approach in applying this method to transparent liquids would be to "
               "use a sufficiently large graduated cylinder filled with the liquid. With a distance "
               "marked on the cylinder near the axial and radial center (the region least influenced "
               "by the container walls and ends), a sphere (such as a ball bearing or a material that "
               "is nonreactive with the liquid) with a known density and sized to within the bounds "
               "of the container correction, free falls the length of the cylinder. As the sphere "
               "passes through the marked region of length <i>d</i> at its terminal velocity, a "
               "measure of the time taken to traverse this distance allows the velocity of the "
               "sphere to be calculated. Having measured all the parameters of Equation 30.26, the "
               "shear viscosity of the liquid can be determined."))
    b.append(p("This method is useful for liquids with viscosities between 10<sup>−3</sup> Pa·s and "
               "10<sup>5</sup> Pa·s. Due to the simplicity of design, the falling sphere method is "
               "particularly well suited to high pressure–high temperature viscosity studies."))

    # ---- Falling cylinder
    b.append(h4("Falling Cylinder"))
    b.append(p("The falling cylinder method is similar in concept to the falling sphere method "
               "except that a flat-ended, solid circular cylinder freely falls vertically in the "
               "direction of its longitudinal axis through a liquid sample within a cylindrical "
               "container. A schematic diagram of the configuration is shown in Figure 30.8. Taking "
               "an infinitely long cylinder of density ρ<sub>2</sub> and radius <i>r</i><sub>c</sub> "
               "falling through a Newtonian fluid of density ρ<sub>1</sub> with infinite extent, the "
               "resulting shear viscosity of the fluid is given as:"))
    b.append(fig(8, F.fig(8), "en"))
    b.append(eq("η = <i>gr</i><sub>c</sub>²(ρ<sub>2</sub> − ρ<sub>1</sub>) ⁄ "
                "(2<i>U</i><sub>t</sub>)", "30.29"))
    b.append(p("Just as with the falling sphere, a finite container volume necessitates modifying "
               "Equation 30.29 to account for the effects of container walls and ends. A correction "
               "for container wall effects can be analytically deduced by balancing the buoyancy and "
               "gravitational forces on the cylinder, of length <i>L</i>, with the shear force on "
               "the sides and the compressional force on the cylinder’s leading end and the tensile "
               "force on the cylinder’s trailing end. The resulting correction term, or geometrical "
               "factor, <i>G</i>(<i>k</i>) (where <i>k</i> = <i>r</i><sub>c</sub>/<i>r</i>), "
               "depends on the cylinder radius and the container radius, <i>r</i>, and is given by:"))
    b.append(eq("<i>G</i>(<i>k</i>) = [<i>k</i>²(1 − ln <i>k</i>) − (1 + ln <i>k</i>)] ⁄ "
                "(1 + <i>k</i>²)", "30.30"))
    b.append(p("Unlike the fluid flow around a falling sphere, the fluid motion around a falling "
               "flat-ended cylinder is very complex. The effects of container ends are minimized by "
               "creating a small gap between the cylinder and the container wall. If a long cylinder "
               "(here, a cylinder is considered long if ψ ≥ 10, where ψ = <i>L</i>/<i>r</i>) with a "
               "radius nearly as large as the radius of the container is used, then the effects of "
               "the walls would dominate, thereby reducing the end effects to a second-order effect. "
               "A major drawback with this approach is, however, if the cylinder and container are "
               "not concentric, the resulting inhomogeneous wall shear force would cause the "
               "downward motion of the cylinder to become eccentric. The potential for misalignment "
               "motivated the recently obtained analytical solution to the fluid flow about the "
               "cylinder ends [16]. An analytical expression for the end correction factor (ECF) was "
               "then deduced [17] and is given as:"))
    b.append(eq("1 ⁄ ECF = 1 + (8<i>k</i> ⁄ π<i>C</i><sub>w</sub>)(<i>G</i>(<i>k</i>) ⁄ ψ)", "30.31"))
    b.append(p("where <i>C</i><sub>w</sub> = 1.003852 − 1.961019<i>k</i> + 0.9570952<i>k</i>². "
               "<i>C</i><sub>w</sub> was derived semi-empirically [17] as a disk wall correction "
               "factor. This is based on the idea that the drag force on the ends of the cylinder "
               "can be described by the drag force on a disk. Equation 30.31 is valid for ψ ≤ 30 and "
               "agrees with the empirically derived correction [16] to within 0.6%."))
    b.append(p("With wall and end effects taken into consideration, the working formula to determine "
               "the shear viscosity of a Newtonian fluid from a falling cylinder viscometer is:"))
    b.append(eq("η = [<i>gr</i><sub>c</sub>²(ρ<sub>2</sub> − ρ<sub>1</sub>)<i>G</i>(<i>k</i>)] ⁄ "
                "(2<i>U</i><sub>t</sub> ⁄ ECF)", "30.32"))
    b.append(p("In the past, this method was primarily used as a method to determine relative "
               "viscosities between transparent fluids. It has only been since the introduction of "
               "the ECF [16, 17] that this method could be rigorously used as an absolute viscosity "
               "method. With a properly designed container and cylinder, this method is now able to "
               "provide accurate absolute viscosities from 10<sup>−3</sup> Pa·s to 10<sup>7</sup> "
               "Pa·s."))

    # ---- Opaque liquids
    b.append(h4("Falling Methods in Opaque Liquids"))
    b.append(p("The falling body methods described above have been extensively applied to "
               "transparent liquids where optical (often visual) observation of the falling body is "
               "possible. For <i>opaque</i> liquids, however, falling body methods require the use "
               "of some sensing technique to determine, often <i>in situ</i>, the position of the "
               "falling body with respect to time. Techniques have varied but they all have in "
               "common the ability to detect the body as it moves past the sensor. A recent study at "
               "high pressure [18] demonstrated that the contrast in electric conductivity between a "
               "sphere and opaque liquid could be exploited to dynamically sense the moving sphere "
               "if suitably placed electrodes penetrated the container walls as shown in the "
               "schematic diagram in Figure 30.9. References to other similar <i>in situ</i> "
               "techniques are given in [18]."))
    b.append(fig(9, F.fig(9), "en"))

    # ---- Rising bubble
    b.append(h4("Rising Bubble/Droplet"))
    b.append(p("For many industrial processes, the rising bubble viscometer has been used as a "
               "method of comparing the relative viscosities of transparent liquids (such as "
               "varnish, lacquer, and beer) for decades. Although its use was widespread, the actual "
               "behavior of the bubble in a viscous liquid was not well understood until long after "
               "the method was introduced [19]. The rising bubble method has been thought of as a "
               "derivative of the falling sphere method; however, there are primary differences "
               "between the two. The major physical differences are (1) the density of the bubble is "
               "less than that of the surrounding liquid, and (2) the bubble itself has some unique "
               "viscosity. Each of these differences can, and do, lead to significant and extremely "
               "complex rheological problems that have yet to be fully explained. If a bubble of gas "
               "or droplet of liquid with a radius, <i>r</i><sub>b</sub>, and density, ρ′, is freely "
               "rising in some enclosing viscous liquid of density ρ, then the shear viscosity of "
               "the enclosing liquid is determined by:"))
    b.append(eq("η = (1 ⁄ ε)[2<i>gr</i><sub>b</sub>²(ρ − ρ′) ⁄ (9<i>U</i><sub>t</sub>)]", "30.33"))
    b.append(p("where"))
    b.append(eq("ε = (2η + 3η′) ⁄ [3(η + η′)]", "30.34"))
    b.append(p("where η′ is the viscosity of the bubble. It must be noted that when the value of η′ "
               "is large (solid spheres), ε = 1, which reduces Equation 30.33 to Equation 30.25. For "
               "small values of η′ (gas bubbles), ε becomes 2/3, and the viscosity calculated by "
               "Equation 30.33 is 1.5 times greater than the viscosity calculated by Equation 30.25. "
               "It is apparent from Equations 30.33 and 30.25 that if the density of the bubble is "
               "less than the density of the enclosing liquid, then the terminal velocity of the "
               "sphere is negative, which indicates upward motion since the downward direction is "
               "positive."))
    b.append(p("During the rise, great care must be taken to avoid contamination of the bubble and "
               "its surface with impurities in the surrounding liquid. Impurities can diffuse through "
               "the surface of the bubble and combine with the fluid inside. Because the bubble has a "
               "low viscosity, the upward motion in a viscous medium induces a drag on the bubble "
               "that is responsible for generating a circulatory motion within it. This motion can "
               "efficiently distribute impurities throughout the whole of the bubble, thereby "
               "changing its viscosity and density. Impurities left on the surface of the bubble can "
               "form a “skin” that can significantly affect the rise of the bubble, as the skin layer "
               "has its own density and viscosity that are not included in Equation 30.33. These "
               "surface impurities also make a significant contribution to the inhomogeneous "
               "distribution of interfacial tension forces. A balance of these forces is crucial for "
               "the formation of a spherical bubble. The simplest method to minimize the above "
               "effects is to employ minute bubbles by introducing a specific volume of fluid (gas or "
               "liquid), with a syringe or other similar device, at the lower end of the cylindrical "
               "container. Very small bubbles behave like solid spheres, which makes interfacial "
               "tension forces and internal fluid motion negligible."))
    b.append(p("In all rising bubble viscometers, the bubble is assumed to be spherical. "
               "Experimental studies of the shapes of freely rising gas bubbles in a container of "
               "finite extent [20] have shown that (to 1% accuracy) a bubble will form and retain a "
               "spherical shape if the ratio of the radius of the bubble to the radius of the "
               "confining cylindrical container is less than 0.2. These studies have also "
               "demonstrated that the effect of the wall on the terminal velocity of a rising "
               "spherical bubble is to cause a large decrease (up to 39%) in the observed velocity "
               "compared to the velocity measured within an unbounded medium. This implies that the "
               "walls of the container influence the velocity of the rising bubble sooner than its "
               "geometry. In this method, end effects are known to be large. However, a rigorous, "
               "analytically or empirically derived correction factor has not yet appeared. To "
               "circumvent this, the ratio of container length to sphere diameter must be in the "
               "range of 10 to 100. As in other Stokian methods, this allows the bubble’s velocity "
               "to be measured at locations that experience negligible end effects."))
    b.append(p("Considering all of the above complications, the use of minute bubbles is the best "
               "approach to ensure a viscosity measurement that is least affected by the liquid to "
               "be investigated and the container geometry."))

    # ---- Oscillating method
    b.append(h3("Oscillating Method", anchor="t30-daodong"))
    b.append(p("If a liquid is contained within a vessel suspended by some torsional system that is "
               "set in oscillation about its vertical axis, then the motion of the vessel will "
               "experience a gradual damping. In an ideal situation, the damping of the motion of "
               "the vessel arises purely as a result of the viscous coupling of the liquid to the "
               "vessel and the viscous coupling between layers in the liquid. In any practical "
               "situation, there are also frictional losses within the system that aid in the "
               "damping effect and must be accounted for in the final analysis. From observations of "
               "the amplitudes and time periods of the resulting oscillations, a viscosity of the "
               "liquid can be calculated. A schematic diagram of the basic set-up of the method is "
               "shown in Figure 30.10. Following initial oscillatory excitation, a light source "
               "(such as a low-intensity laser) can be used to measure the amplitudes and periods of "
               "the resulting oscillations by reflection off the mirror attached to the suspension "
               "rod to give an accurate measure of the logarithmic decrement of the oscillations "
               "(δ) and the periods (<i>T</i>)."))
    b.append(fig(10, F.fig(10), "en"))
    b.append(p("Various working formulae have been derived that associate the oscillatory motion of "
               "a vessel of radius <i>r</i> to the absolute viscosity of the liquid. The most "
               "reliable formula is the following equation for a cylindrical vessel [21]:"))
    b.append(eq("η = [<i>I</i>δ ⁄ (π<i>r</i>³<i>HZ</i>)]²[1 ⁄ (πρ<i>T</i>)]", "30.35"))
    b.append(p("where"))
    b.append(eq("<i>Z</i> = (1 + <i>r</i> ⁄ 4<i>H</i>)<i>a</i><sub>0</sub> − [(3 ⁄ 2 + 4<i>r</i> ⁄ "
                "π<i>H</i>) ⁄ ρ] + [(3 ⁄ 8 + 9<i>r</i> ⁄ 4<i>H</i>)<i>p</i> ⁄ ρ]", "30.36"))
    b.append(eq("<i>p</i> = (πρ ⁄ η<i>T</i>)<sup>1/2</sup><i>r</i>", "30.37"))
    b.append(eq("<i>a</i><sub>0</sub> = 1 − (δ ⁄ 4π) − (3δ² ⁄ 32π²)", "30.38"))
    b.append(eq("<i>a</i><sub>2</sub> = 1 + (δ ⁄ 4π) + (δ² ⁄ 32π²)", "30.39"))
    b.append(p("<i>I</i> is the mass moment of inertia of the suspended system and ρ is the density "
               "of the liquid."))
    b.append(p("A more practical expression of Equation 30.35 is obtained by introducing a number of "
               "simplifications. First, it is a reasonable assumption to consider δ to be small (on "
               "the order of 10<sup>−2</sup> to 10<sup>−3</sup>). This reduces <i>a</i><sub>0</sub> "
               "and <i>a</i><sub>2</sub> to values of 1 and −1, respectively. Second, the effects of "
               "friction from the suspension system and the surrounding atmosphere can be "
               "experimentally determined and contained within a single variable, δ<sub>0</sub>. "
               "This must then be subtracted from the measured δ. A common method of obtaining "
               "δ<sub>0</sub> is to observe the logarithmic decrement of the system with an empty "
               "sample vessel and subtract that value from the measured value of δ. With these "
               "modifications, Equation 30.35 becomes:"))
    b.append(eq("(δ − δ<sub>0</sub>) ⁄ ρ = [<i>A</i>(η ⁄ ρ)<sup>1/2</sup> − <i>B</i>(η ⁄ ρ) + "
                "<i>C</i>(η ⁄ ρ)<sup>3/2</sup>]", "30.40"))
    b.append(p("where"))
    b.append(eq("<i>A</i> = (π<sup>3/2</sup> ⁄ <i>I</i>)[1 + (<i>r</i> ⁄ 4<i>H</i>)]<i>Hr</i>²"
                "<i>T</i><sup>1/2</sup>", "30.41"))
    b.append(eq("<i>B</i> = (π ⁄ <i>I</i>)[(3 ⁄ 2) + (4<i>r</i> ⁄ π<i>H</i>)]<i>Hr</i>²<i>T</i>",
                "30.42"))
    b.append(eq("<i>C</i> = (π<sup>3/2</sup> ⁄ 2<i>I</i>)[(3 ⁄ 8) + (9<i>r</i> ⁄ 4<i>H</i>)]"
                "<i>HrT</i><sup>3/2</sup>", "30.43"))
    b.append(p("It has been noted [22] that the analytical form of Equation 30.40 needs an "
               "empirically derived, instrument-constant correction factor (ζ) in order to agree with "
               "experimentally measured values of η. The discrepancy between the analytical form and "
               "the measured value arises as a result of the above assumptions. However, these "
               "assumptions are required as there are great difficulties involved in solving the "
               "differential equations of motion of this system. The correction factor is dependent "
               "on the materials, dimensions, and densities of each individual system, but generally "
               "lies between the values of 1.0 and 1.08. The correction factor is obtained by "
               "comparing viscosity values of calibration materials determined by an individual "
               "system (with Equation 30.35) and viscosity values obtained by another reliable "
               "method such as the capillary method."))
    b.append(p("With the above considerations taken into account, the final working Roscoe’s formula "
               "for the absolute shear viscosity is:"))
    b.append(eq("(δ − δ<sub>0</sub>) ⁄ ρ = ζ[<i>A</i>(η ⁄ ρ)<sup>1/2</sup> − <i>B</i>(η ⁄ ρ) + "
                "<i>C</i>(η ⁄ ρ)<sup>3/2</sup>]", "30.44"))
    b.append(p("The oscillating cup method has been used, and is best suited for use with low values "
               "of viscosity within the range of 10<sup>−5</sup> Pa·s to 10<sup>−2</sup> Pa·s. Its "
               "simple closed design and use at high temperatures has made this method very popular "
               "when dealing with liquid metals."))

    # ---- Ultrasonic
    b.append(h3("Ultrasonic Methods", anchor="t30-sieuam"))
    b.append(p("Viscosity plays an important role in the absorption of energy of an acoustic wave "
               "traveling through a liquid. By using ultrasonic waves (10<sup>4</sup> Hz &lt; "
               "<i>f</i> &lt; 10<sup>8</sup> Hz), the elastic, viscoelastic, and viscous response of "
               "a liquid can be measured down to times as short as 10 ns. When the viscosity of the "
               "fluid is low, the resulting time scale for structural relaxation is shorter than the "
               "ultrasonic wave period and the fluid is probed in the relaxed state. High-viscosity "
               "fluids subjected to ultrasonic wave trains respond as a stiff fluid because "
               "structural equilibration due to the acoustic perturbation does not go to completion "
               "before the next wave cycle. Consequently, the fluid is said to be in an unrelaxed "
               "state that is characterized by dispersion (frequency-dependent wave velocity) and "
               "elastic moduli that reflect a much stiffer liquid. The frequency dependence of the "
               "viscosity relative to some reference viscosity (η<sub>0</sub>) at low frequency, "
               "η/η<sub>0</sub>, and of the absorption per wavelength, αλ, where α is the absorption "
               "coefficient of the liquid and λ is the wavelength of the compressional wave, for a "
               "liquid with a single relaxation time, τ, is shown in Figure 30.11. The maximum "
               "absorption per wavelength occurs at the relaxation frequency when ωτ = 1 and is "
               "accompanied by a step in η/η<sub>0</sub>, as well as in other properties such as "
               "velocity and compressibility. Depending on the application of the measured "
               "properties, it is important to determine if the liquid is in a relaxed or unrelaxed "
               "state."))
    b.append(fig(11, F.fig(11), "en"))
    b.append(p("A schematic diagram of a typical apparatus for measuring viscosity by the ultrasonic "
               "method is shown in Figure 30.12. Mechanical vibrations in a piezoelectric transducer "
               "travel down one of the buffer rods (BR-1 in Figure 30.12) and into the liquid sample "
               "and are received by a similar transducer mounted on the other buffer rod, BR-2. In "
               "the fixed buffer rod configuration, once steady-state conditions have been reached, "
               "the applied signal is turned off quickly. The decay rate of the received and "
               "amplified signal, displayed on an oscilloscope on an amplitude vs. time plot as "
               "shown in Figure 30.12(a), gives a measure of α. The received amplitude decays as:"))
    b.append(eq("<i>A</i> = <i>A</i><sub>0</sub> e<sup>−(b+αc)t′</sup>", "30.45"))
    b.append(p("where <i>A</i> is the received decaying amplitude, <i>A</i><sub>0</sub> is the input "
               "amplitude, <i>b</i> is an apparatus constant that depends on other losses in the "
               "system such as due to the transducer, container, etc. that can be evaluated by "
               "measuring the attenuation in a standard liquid, <i>c</i> is the compressional wave "
               "velocity of the liquid, and <i>t</i>′ is time. At low frequencies, the absorption "
               "coefficient is expressed in terms of volume and shear viscosity as:"))
    b.append(eq("(η<sub>v</sub> + 4η ⁄ 3) = αρ<i>c</i>³ ⁄ (2π²<i>f</i>²)", "30.46"))
    b.append(fig(12, F.fig(12), "en"))
    b.append(p("One of the earliest ultrasonic methods of measuring attenuation in liquids is based "
               "on acoustic interferometry [23]. Apart from the instrumentation needed to move and "
               "determine the position of one of the buffer rods accurately, the experimental "
               "apparatus is essentially the same as for the fixed buffer rod configuration [24]. "
               "The measurement, however, depends on the continuous acoustic wave interference of "
               "transmitted and reflected waves within the sample melt as one of the buffer rods is "
               "moved away from the other rod. The attenuation is characterized by the decay of the "
               "maxima amplitude as a function of melt thickness as shown on the interferogram in "
               "Figure 30.12(b). Determining α from the observed amplitude decrement involves "
               "numerical solution to a system of equations characterizing complex wave propagation "
               "[25]. The ideal conditions represented in the theory do not account for such things "
               "as wavefront curvature, buffer rod end nonparallelism, surface roughness, and "
               "misalignment. These problems can be addressed in the amplitude fitting stage but "
               "they can be difficult to overcome. The interested reader is referred to [25] for "
               "further details."))
    b.append(p("Ultrasonic methods have not been and are not likely to become the mainstay of fluid "
               "viscosity determination simply because they are more technically complicated than "
               "conventional viscometry techniques. And although ultrasonic viscometry supplies "
               "additional related elastic property data, its niche in viscometry is its capability "
               "of providing volume viscosity data. Since there is no other viscometer to measure "
               "η<sub>v</sub>, ultrasonic absorption measurements play a unique role in the study of "
               "volume viscosity."))

    # ---- references
    b.append(h3("References"))
    b.append(wl(_refs30("en")))
    b.append(h3("Further Information"))
    b.append(wl(_refs30b("en")))
    return "".join(b)


SECTIONS_VI = [sec_30_1_vi]
SECTIONS_EN = [sec_30_1_en]

# The handbook gives §30.1 as one section with seven sub-topics listed under the
# heading and no numbers of their own. The index therefore lists them unnumbered
# rather than inventing a 30.1.1–30.1.7 scheme the source does not use.
SUBSECTIONS = [
    ("Chất lưu Newton và phi Newton", "Newtonian and Non-Newtonian Fluids", "t30-newton"),
    ("Thứ nguyên và đơn vị của độ nhớt", "Dimensions and Units of Viscosity", "t30-donvi"),
    ("Các loại nhớt kế", "Viscometer Types", "t30-loai"),
    ("Nhớt kế mao quản", "Capillary Viscometers", "t30-maoquan"),
    ("Phương pháp vật rơi", "Falling Body Methods", "t30-roi"),
    ("Phương pháp dao động", "Oscillating Method", "t30-daodong"),
    ("Phương pháp siêu âm", "Ultrasonic Methods", "t30-sieuam"),
]


def sec_index(lang):
    """The in-page jump index. The chapter is a single long section, so the index
    lists the seven sub-topics instead — otherwise it would have one entry."""
    vi = lang == "vi"
    li = "".join('<li><span class="t"><a href="#%s">%s</a></span></li>'
                 % (a, tvi if vi else ten) for tvi, ten, a in SUBSECTIONS)
    return ('<ul class="toc-list sec-index" aria-label="%s">%s</ul>'
            % ("Mục lục trong chương" if vi else "Contents of this chapter", li))


def body_vi():
    out = ['<p class="lede">Độ nhớt là ma sát trong của chất lưu, và hầu như mọi dòng chảy đều bị '
           'nó chi phối ít nhiều. Chương này đi từ định nghĩa Newton, qua cách phân loại chất lưu '
           'Newton và phi Newton, rồi lần lượt trình bày bảy nhóm nhớt kế — quay, mao quản, vật rơi, '
           'dao động và siêu âm — cùng công thức làm việc và những sai số phải hiệu chỉnh.</p>',
           sec_index("vi")]
    for f in SECTIONS_VI:
        out.append(f())
    return "".join(out)


def body_en():
    out = ['<p class="lede">Viscosity is the internal friction of a fluid, and almost every flow is '
           'governed by it to some degree. This chapter runs from Newton’s definition, through the '
           'Newtonian/non-Newtonian distinction, to seven families of viscometer — rotational, '
           'capillary, falling body, oscillating and ultrasonic — with their working formulae and '
           'the corrections each one needs.</p>', sec_index("en")]
    for f in SECTIONS_EN:
        out.append(f())
    return "".join(out)


def build(lang):
    vi = lang == "vi"
    switch = ("%s%s/" % (BASE_EN, CSLUG)) if vi else ("%s%s/" % (BASE_VI, CSLUG))
    title = ("Chương 30 — %s · Sổ tay Đo lường, Thiết bị đo và Cảm biến" % TITLE_VI if vi
             else "Chapter 30 — %s · Measurement, Instrumentation and Sensors Handbook" % TITLE_EN)
    desc = ("Bản dịch tiếng Việt Chương 30 “Đo độ nhớt” của G. E. Leblanc, R. A. Secco và M. Kostic — "
            "định nghĩa độ nhớt, lưu biến học, và bảy nhóm nhớt kế cùng công thức và sai số." if vi
            else
            "Companion to Chapter 30 of the CRC Measurement Handbook — the definition of viscosity, "
            "rheology, and seven families of viscometer with their formulae and error sources.")
    crumb = ('<a href="/vi/books/">Sách</a> · <a href="%s">Sổ tay Đo lường, Thiết bị đo và Cảm biến</a> · '
             'Chương 30' % BASE_VI if vi else
             '<a href="/books/">Books</a> · <a href="%s">Measurement, Instrumentation and Sensors '
             'Handbook</a> · Chapter 30' % BASE_EN)
    # Recount these whenever a section is added: the meta line is the only place
    # the reader is told how big the chapter is, and a stale count is the kind of
    # error nobody notices until they have read the whole thing.
    meta = ("Chương 30 · theo Ch30.pdf (CRC Press, 1999) · 12 hình, 46 phương trình, 4 bảng" if vi else
            "Chapter 30 · 12 figures, 46 equations, 4 tables")
    body = ('<main><article class="intranet-content reader"><div class="reader-hero">'
            '<div class="breadcrumb">%s</div><h1>%s</h1><p class="byline">%s</p>'
            '<div class="meta-line">%s</div></div><div class="prose">%s</div>%s</article></main>'
            % (crumb, TITLE_VI if vi else TITLE_EN, BYLINE, meta,
               body_vi() if vi else body_en(), chapter_nav(lang, 30)))
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
