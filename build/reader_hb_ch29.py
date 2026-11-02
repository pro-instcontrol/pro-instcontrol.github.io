# -*- coding: utf-8 -*-
"""Handbook Chapter 29 — Point Velocity Measurement
(John A. Kleppe — University of Nevada; John G. Olin — Sierra Instruments;
Rajan K. Menon — TSI Inc.)

Three sections, 55 source pages, 31 figures, 4 tables. Translated section by
section; each section is a pair of functions (sec_NN_vi / sec_NN_en) appended
to the two body builders at the bottom, so a later session can add a section
without touching the ones already written.

Run:  python build/reader_hb_ch29.py
"""
import os

import hb29fig as F
from reader_handbook import SLUG, head, header, footer
from chapter_nav import nav as chapter_nav

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSLUG = "ch29-point-velocity-measurement"
TITLE_EN = "Point Velocity Measurement"
TITLE_VI = "Đo vận tốc tại một điểm"
BYLINE = ("John A. Kleppe (University of Nevada) · John G. Olin (Sierra Instruments, Inc.) · "
          "Rajan K. Menon (TSI Inc.)")
BASE_EN = "/books/read/%s/" % SLUG
BASE_VI = "/vi/books/read/%s/" % SLUG
PREV_EN = "ch28-flow-measurement"
PREV_VI = "ch28-flow-measurement"
PREV_T_EN = "Flow Measurement"
PREV_T_VI = "Đo lưu lượng"


def fig(num, key, lang="vi"):
    svg, cap_vi, cap_en, aria_vi, aria_en = key
    if lang == "vi":
        cap = cap_vi
    else:
        cap = cap_en
        # The <svg> tag is built once, in hb29fig, with a Vietnamese aria-label
        # baked in by hbfig.svg(). Swap it for the English one, otherwise a
        # screen reader on this page announces Vietnamese.
        k = svg.find('aria-label="')
        if k >= 0:
            a = k + len('aria-label="')
            b = svg.find('"', a)
            svg = svg[:a] + (aria_en or aria_vi) + svg[b:]
    return ('<figure class="figure" id="fig-29-%d">%s<figcaption class="figcap">%s</figcaption></figure>'
            % (num, svg, cap))


def p(t):
    return "<p>%s</p>" % t


def h2(t, en=""):
    # A heading whose gloss repeats the title (the usual case on the English
    # page) prints the title twice; drop the redundant span instead.
    if en == t:
        en = ""
    # Section headings carry an anchor so the jump index at the top of the page
    # can link to them.
    sid = ""
    if t.startswith("29."):
        head = t[3:].split(" ", 1)[0]
        if head.isdigit():
            sid = ' id="s29-%s"' % head
    return '<h2%s>%s%s</h2>' % (sid, t, (' <span class="en">%s</span>' % en) if en else "")


def h3(t, en=""):
    if en == t:
        en = ""
    return '<h3>%s%s</h3>' % (t, (' <span class="en">%s</span>' % en) if en else "")


def eq(body, num=""):
    if not num:
        return '<div class="eq">%s</div>' % body
    return '<div class="eq"><span class="n">(%s)</span>%s</div>' % (num, body)


def note(t):
    return '<div class="note">%s</div>' % t


def box(title, items):
    """Worked example. Chapter 29 carries two fully worked numerical examples
    with numbered steps; a bordered block keeps them visibly separate from the
    surrounding argument, which the source achieves with a rule and a bold
    heading."""
    return ('<div style="border:1px solid #ddd6c6;border-left:3px solid #9a8f78;'
            'background:#faf8f3;padding:.9rem 1.1rem .4rem;margin:1.3rem 0 1.6rem;border-radius:3px">'
            '<p style="margin:0 0 .6rem;font-weight:700;font-size:.95rem">%s</p>%s</div>'
            % (title, "".join(items)))


def wl(items):
    return ('<p style="font-size:.92rem;color:#333;line-height:1.8;margin:-.3rem 0 1.2rem">'
            + "<br>".join(items) + "</p>")


def defs(items):
    """Defining-terms block. Rendered as a two-column table so it inherits the
    reader's existing .tbl styling — there is no .deflist rule in library.css."""
    rows = "".join('<tr><th scope="row" style="text-align:left;width:30%%">%s</th><td>%s</td></tr>'
                   % (k, v) for k, v in items)
    return ('<div class="table-wrap"><table class="tbl"><tbody>%s</tbody></table></div>' % rows)


def table(hd, rows, cap, cls="tbl", widths=None):
    body = "".join("<tr>%s</tr>" % "".join("<td>%s</td>" % c for c in r) for r in rows)
    ths = "".join('<th%s>%s</th>' % ((' style="width:%s"' % widths[i]) if widths else "", h)
                  for i, h in enumerate(hd))
    return ('<div class="table-wrap"><table class="%s"><thead><tr>%s</tr></thead><tbody>%s</tbody></table></div>'
            '<p style="font-size:.84rem;color:#888;font-style:italic">%s</p>'
            % (cls, ths, body, cap))


def h4(t, en=""):
    """Sub-heading one level below h3. There is no .prose h4 rule in library.css,
    so the size and spacing are set inline to sit between h3 and body text."""
    if en == t:
        en = ""
    return ('<h4 style="font-size:1rem;font-weight:700;margin:1.7rem 0 .5rem">%s%s</h4>'
            % (t, (' <span class="en">%s</span>' % en) if en else ""))


def h5(t, en=""):
    """Third-level run-in heading, set smaller so the nesting stays visible."""
    if en == t:
        en = ""
    return ('<h5 style="font-size:.92rem;font-weight:700;margin:1.35rem 0 .3rem;'
            'padding-left:.6rem;border-left:2px solid #d8d2c4;color:#2f2f2f">%s%s</h5>'
            % (t, (' <span class="en">%s</span>' % en) if en else ""))


def ul(items):
    return ('<ul style="margin:-.2rem 0 1.3rem">%s</ul>'
            % "".join("<li>%s</li>" % i for i in items))


def ol(items):
    return ('<ol style="margin:-.2rem 0 1.3rem">%s</ol>'
            % "".join("<li>%s</li>" % i for i in items))


# ================================================================ table data

def _t291(lang):
    """Table 29.1 — compressibility factor for air, γ = 1,4. Ten rows; printed
    as two columns of five so it does not run the full page height."""
    vals = [("0,1", "1,003"), ("0,2", "1,010"), ("0,3", "1,023"), ("0,4", "1,041"),
            ("0,5", "1,064"), ("0,6", "1,093"), ("0,7", "1,129"), ("0,8", "1,170"),
            ("0,9", "1,219"), ("1,0", "1,276")]
    if lang == "vi":
        hd = ("<i>M</i>", "(p₀ − p) ⁄ (½ρv²)", "<i>M</i>", "(p₀ − p) ⁄ (½ρv²)")
        cap = ("Bảng 29.1 · Sự biến thiên của “hệ số nén được” theo số Mach với không khí, γ = 1,4. "
               "Cột phải là tỉ số giữa chênh áp thực và chênh áp tính theo công thức dòng không nén "
               "được; giá trị 1,003 ở M = 0,1 nghĩa là sai số do bỏ qua tính nén được chỉ 0,3 %.")
    else:
        hd = ("<i>M</i>", "(p₀ − p) ⁄ (½ρv²)", "<i>M</i>", "(p₀ − p) ⁄ (½ρv²)")
        cap = ("Table 29.1 · Variation of the “compressibility factor” with Mach number for air, "
               "γ = 1.4. The right-hand column is the ratio of the true pressure difference to the "
               "difference predicted by the incompressible formula; a value of 1.003 at M = 0.1 "
               "means the incompressible assumption is off by only 0.3 %.")
    rows = []
    for i in range(5):
        a, b = vals[i]
        c, d = vals[i + 5]
        rows.append([a, b, c, d])
    return hd, rows, cap


def _t292(lang):
    """Table 29.2 — vendors. The source prints name, full postal address,
    telephone/fax and probe type in one ragged cell; four columns of equal
    width read far better."""
    if lang == "vi":
        hd = ("Nhà sản xuất / nhà cung cấp", "Địa chỉ", "Điện thoại · Fax", "Loại đầu dò")
        cap = ("Bảng 29.2 · Một số nhà sản xuất/nhà cung cấp. Danh sách giữ nguyên như bản in năm "
               "1999, kể cả số điện thoại và địa chỉ; đây là tư liệu lịch sử, không phải chỉ dẫn "
               "mua hàng hiện hành.")
        rows = [
            ["EEMC/EMRC", "3730 North Pellegrino Dr.<br>Tucson, AZ 85749",
             "(520) 749-2167<br>(520) 749-3582", "Đầu dò Pitot kiểu S"],
            ["Dwyer Instruments, Inc.", "P.O. Box 373<br>Michigan City, IN 46361",
             "(219) 879-8000<br>(219) 872-9057", "Ống Pitot-tĩnh và đầu dò Pitot kiểu S"],
            ["Rosemount Aerospace, Inc.", "14300 Judicial Rd.<br>Burnsville, MN 55306-4898",
             "(612) 892-4300<br>(612) 892-4430",
             "Cảm biến góc dòng, ống Pitot và Pitot-tĩnh, cảm biến góc tới kiểu cánh, "
             "cảm biến nhiệt độ, máy dò băng và đầu chuyển đổi áp suất"],
            ["Dieterich Standard", "P.O. Box 9000<br>Boulder, CO 80301",
             "(303) 530-9600<br>(303) 530-7064", "ANNUBAR® đa điểm, tự lấy trung bình"],
            ["Air Monitor Corporation", "P.O. Box 6358<br>Santa Rosa, CA 95406",
             "(707) 544-2706<br>(800) AIRFLOW<br>(707) 526-9970", "Đa điểm, tự lấy trung bình"],
            ["United Sciences, Inc.", "5310 North Pioneer Rd.<br>Gibsonia, PA 15044",
             "(412) 443-8610<br>(412) 443-7180", "Auto-PROBE 2000® — thử nghiệm Phương pháp 2 tự động"],
            ["Scientific Engineering Instruments, Inc.",
             "1275 Kleppe Lane, Suite 14<br>Sparks, NV 89431-6499",
             "(702) 358-0937<br>(702) 358-0956",
             "STACKWATCH® — hệ lai đo lưu lượng thể tích trong ống dẫn và ống khói lớn (CEMS)"],
        ]
    else:
        hd = ("Manufacturer / vendor", "Address", "Telephone · Fax", "Probe type")
        cap = ("Table 29.2 · A sample of manufacturers and vendors. The list is reproduced as printed "
               "in 1999, telephone numbers and addresses included; it is a historical record, not a "
               "current buying guide.")
        rows = [
            ["EEMC/EMRC", "3730 North Pellegrino Dr.<br>Tucson, AZ 85749",
             "(520) 749-2167<br>(520) 749-3582", "Type S Pitot probe"],
            ["Dwyer Instruments, Inc.", "P.O. Box 373<br>Michigan City, IN 46361",
             "(219) 879-8000<br>(219) 872-9057", "Pitot-static tubes and type S Pitot probe"],
            ["Rosemount Aerospace, Inc.", "14300 Judicial Rd.<br>Burnsville, MN 55306-4898",
             "(612) 892-4300<br>(612) 892-4430",
             "Flow angle sensors, Pitot and Pitot-static tubes, vane angle-of-attack sensors, "
             "temperature sensors, ice detectors, pressure transducers"],
            ["Dieterich Standard", "P.O. Box 9000<br>Boulder, CO 80301",
             "(303) 530-9600<br>(303) 530-7064", "ANNUBAR® multipoint, self-averaging"],
            ["Air Monitor Corporation", "P.O. Box 6358<br>Santa Rosa, CA 95406",
             "(707) 544-2706<br>(800) AIRFLOW<br>(707) 526-9970", "Multipoint, self-averaging"],
            ["United Sciences, Inc.", "5310 North Pioneer Rd.<br>Gibsonia, PA 15044",
             "(412) 443-8610<br>(412) 443-7180", "Auto-PROBE 2000® automated Method 2 testing"],
            ["Scientific Engineering Instruments, Inc.",
             "1275 Kleppe Lane, Suite 14<br>Sparks, NV 89431-6499",
             "(702) 358-0937<br>(702) 358-0956",
             "STACKWATCH® hybrid system for volumetric flow sensing in large ducts and stacks (CEMS)"],
        ]
    return hd, rows, cap


def _refs291(lang):
    if lang == "vi":
        return [
            "1. B. S. Massey, <i>Mechanics of Fluids</i>, Princeton, NJ: Van Nostrand, 1968.",
            "2. W. F. Hughes and J. A. Brighton, <i>Theory and Problems of Fluid Dynamics</i>, "
            "New York: McGraw-Hill, 1967.",
            "3. J. B. Evett and C. Liu, <i>Fluid Mechanics and Hydraulics: 2500 Solved Problems</i>, "
            "New York: McGraw-Hill, 1989.",
            "4. R. P. Benedict, <i>Fundamentals of Temperature, Pressure and Flow Measurements</i>, "
            "3rd ed., New York: John Wiley &amp; Sons, 1984.",
            "5. ASME/ANSI PTC 19.2-1987, <i>Instruments and Apparatus, Part 2, Pressure Measurement</i>, "
            "1987.",
            "6. S. P. Parker, <i>Fluid Mechanics Source Book</i>, New York: McGraw-Hill, 1988.",
            "7. EPA, CFR 40 Part 60, Appendix A — Test Methods, 1 July 1995.",
            "8. T. C. Elliott, “CEM System: Lynchpin Holding CAA Compliance Together,” "
            "<i>Power</i>, May 1995, 31–40.",
            "9. J. A. Kleppe, “Principles and Applications of Acoustic Sensors Used for Gas "
            "Temperature and Flow Measurement,” <i>Proc. SENSOR EXPO</i>, Boston, May 1995, 337–374.",
            "10. J. A. Kleppe, “Acoustic Gas Flow Measurement in Large Ducts and Stacks,” "
            "<i>Sensors J.</i>, 12(5), 18–24 and 85–87, 1995.",
            "11. <i>Guidelines for Flue Gas Flow Rate Monitoring</i>, EPRI TR-104527, "
            "Project 1961-13 Final Report, June 1995.",
            "12. A. Mann and J. A. Kleppe, “A Report on the Performance of a Hybrid Flow Monitor Used "
            "for CEMS and Heat Rate Applications,” <i>Proc. EPRI 1996 Heat Rate Improvement Conf.</i>, "
            "Dallas, TX, May 1996, Part 33, 1–13.",
        ]
    return [
        "1. B. S. Massey, <i>Mechanics of Fluids</i>, Princeton, NJ: Van Nostrand, 1968.",
        "2. W. F. Hughes and J. A. Brighton, <i>Theory and Problems of Fluid Dynamics</i>, "
        "New York: McGraw-Hill, 1967.",
        "3. J. B. Evett and C. Liu, <i>Fluid Mechanics and Hydraulics: 2500 Solved Problems</i>, "
        "New York: McGraw-Hill, 1989.",
        "4. R. P. Benedict, <i>Fundamentals of Temperature, Pressure and Flow Measurements</i>, "
        "3rd ed., New York: John Wiley &amp; Sons, 1984.",
        "5. ASME/ANSI PTC 19.2-1987, <i>Instruments and Apparatus, Part 2, Pressure Measurement</i>, "
        "1987.",
        "6. S. P. Parker, <i>Fluid Mechanics Source Book</i>, New York: McGraw-Hill, 1988.",
        "7. EPA, CFR 40 Part 60, Appendix A — Test Methods, 1 July 1995.",
        "8. T. C. Elliott, “CEM System: Lynchpin Holding CAA Compliance Together,” "
        "<i>Power</i>, May 1995, 31–40.",
        "9. J. A. Kleppe, “Principles and Applications of Acoustic Sensors Used for Gas "
        "Temperature and Flow Measurement,” <i>Proc. SENSOR EXPO</i>, Boston, May 1995, 337–374.",
        "10. J. A. Kleppe, “Acoustic Gas Flow Measurement in Large Ducts and Stacks,” "
        "<i>Sensors J.</i>, 12(5), 18–24 and 85–87, 1995.",
        "11. <i>Guidelines for Flue Gas Flow Rate Monitoring</i>, EPRI TR-104527, "
        "Project 1961-13 Final Report, June 1995.",
        "12. A. Mann and J. A. Kleppe, “A Report on the Performance of a Hybrid Flow Monitor Used "
        "for CEMS and Heat Rate Applications,” <i>Proc. EPRI 1996 Heat Rate Improvement Conf.</i>, "
        "Dallas, TX, May 1996, Part 33, 1–13.",
    ]


def _t293(lang):
    """Table 29.3 — commercial systems and their 1997 list prices. The long
    equipment note is printed under the price column in the source; it is set
    as a caption here so the table itself stays two columns wide."""
    if lang == "vi":
        hd = ("Sản phẩm", "Giá niêm yết trung bình tại Hoa Kỳ, 1997")
        rows = [
            ["<b>Hệ công nghiệp</b>", ""],
            ["Đầu chuyển đổi lưu lượng khối kiểu cắm", "1.900 USD"],
            ["Lưu lượng kế khối thẳng dòng 50 mm (2 in.) NPT", "2.500 USD"],
            ["Dãy đo lưu lượng công nghiệp thông minh 8 điểm", "15.000 USD"],
            ["<b>Hệ nghiên cứu</b>", ""],
            ["Hệ nhiệt kế gió dây nóng hoặc màng nóng một kênh", "10.000 USD"],
            ["Hệ nhiệt kế gió dây nóng ba thành phần", "21.000 USD"],
            ["Máy đo vận tốc khí cầm tay", "1.000 USD"],
        ]
        cap = ("Bảng 29.3 · Các hệ nhiệt kế gió thương mại điển hình. Giá là trung bình của các nhà "
               "sản xuất trong Bảng 29.4. Đầu dò kiểu cắm dài 25 cm. Lưu lượng kế khối kiểu cắm và "
               "thẳng dòng có: vỏ chống nổ đạt FM/CENELEC gắn trên đầu dò; nguồn vào là điện lưới "
               "xoay chiều; tín hiệu ra 0–5 V dc; kết cấu thép không gỉ 316; và hiệu chuẩn trong "
               "không khí môi trường. Lưu lượng kế khối công nghiệp thẳng dòng có bộ ổn định dòng "
               "tích hợp. Dãy đo lưu lượng công nghiệp gồm bốn đầu dò dài 1 m, 2 điểm mỗi đầu dò, "
               "kết cấu thép không gỉ 316, nguồn điện lưới, tín hiệu ra 0–5 V dc và điện tử thông "
               "minh gắn trên đầu dò. Các hệ nhiệt kế gió nghiên cứu dùng đầu dò dây nóng tiêu "
               "chuẩn, bộ điện tử đa năng nhất, và kèm hiệu chuẩn trong không khí môi trường.")
    else:
        hd = ("Product", "Average 1997 U.S. list price")
        rows = [
            ["<b>Industrial systems</b>", ""],
            ["Insertion mass flow transducer", "$1,900"],
            ["50 mm (2 in.) NPT in-line mass flowmeter", "$2,500"],
            ["8-point smart industrial flow averaging array", "$15,000"],
            ["<b>Research systems</b>", ""],
            ["Single-channel hot-wire or hot-film anemometer system", "$10,000"],
            ["Three-component hot-wire anemometer system", "$21,000"],
            ["Portable air velocity meter", "$1,000"],
        ]
        cap = ("Table 29.3 · Typical commercial thermal anemometer systems. Prices listed are the "
               "average of the manufacturers listed in Table 29.4. Insertion probe is 25 cm in "
               "length. Insertion and in-line mass flowmeters have: probe-mounted FM/CENELEC "
               "approved, explosion-proof housing; ac line voltage input power; 0–5 V dc output "
               "signal; 316 SS construction; and ambient air calibration. In-line industrial mass "
               "flowmeter has built-in flow conditioning. Industrial flow averaging array has four "
               "1 m long probes, 2 points per probe, 316 SS construction, line voltage input power, "
               "0 to 5 V dc output signal, and smart electronics mounted on probe. Research "
               "anemometer systems have standard hot-wire probes, most versatile electronics, and "
               "include ambient air calibrations.")
    return hd, rows, cap


def _t294(lang):
    """Table 29.4 — manufacturers, printed in two columns by market."""
    if lang == "vi":
        hd = ("Hệ công nghiệp và máy đo vận tốc khí cầm tay", "Hệ nghiên cứu và loại cầm tay")
        left = ("<b>Sierra Instruments, Inc.</b><br>5 Harris Court, Building L<br>"
                "Monterey, CA 93940<br>Điện thoại: (831) 373-0200<br>Fax: (831) 373-4402"
                "<br><br><b>Fluid Components, Inc.</b><br>1755 La Costa Meadows Drive<br>"
                "San Marcos, CA 92069<br>Điện thoại: (619) 744-6950<br>Fax: (619) 736-6250"
                "<br><br><b>Kurz Instruments, Inc.</b><br>2411 Garden Road<br>"
                "Monterey, CA 93940<br>Điện thoại: (831) 646-5911<br>Fax: (831) 646-8901")
        right = ("<b>TSI Inc.</b><br>500 Cardigan Road<br>St. Paul, MN 55164<br>"
                 "Điện thoại: (612) 490-2811<br>Fax: (612) 490-3824"
                 "<br><br><b>Dantec Measurement Technology, Inc.</b><br>Đan Mạch<br>"
                 "Điện thoại: (45) 4492 3610<br>Fax: (45) 4284 6136")
        cap = ("Bảng 29.4 · Các nhà sản xuất hệ nhiệt kế gió. Danh sách giữ nguyên như bản in năm "
               "1999, kể cả số điện thoại và địa chỉ.")
    else:
        hd = ("Industrial systems and portable air velocity meters", "Research systems and portables")
        left = ("<b>Sierra Instruments, Inc.</b><br>5 Harris Court, Building L<br>"
                "Monterey, CA 93940<br>Tel: (831) 373-0200<br>Fax: (831) 373-4402"
                "<br><br><b>Fluid Components, Inc.</b><br>1755 La Costa Meadows Drive<br>"
                "San Marcos, CA 92069<br>Tel: (619) 744-6950<br>Fax: (619) 736-6250"
                "<br><br><b>Kurz Instruments, Inc.</b><br>2411 Garden Road<br>"
                "Monterey, CA 93940<br>Tel: (831) 646-5911<br>Fax: (831) 646-8901")
        right = ("<b>TSI Inc.</b><br>500 Cardigan Road<br>St. Paul, MN 55164<br>"
                 "Tel: (612) 490-2811<br>Fax: (612) 490-3824"
                 "<br><br><b>Dantec Measurement Technology, Inc.</b><br>Denmark<br>"
                 "Tel: (45) 4492 3610<br>Fax: (45) 4284 6136")
        cap = ("Table 29.4 · Manufacturers of thermal anemometer systems. The list is reproduced as "
               "printed in 1999, telephone numbers and addresses included.")
    return hd, [[left, right]], cap


def _refs292(lang):
    return [
        "1. H. H. Bruun, <i>Hot-Wire Anemometry: Principles and Signal Analysis</i>, Oxford: Oxford "
        "University Press, 1995.",
        "2. L. M. Fingerson and P. Freymuth, “Thermal anemometers,” in R. J. Goldstein (ed.), "
        "<i>Fluid Mechanics Measurements</i>, Washington, D.C.: Hemisphere, 1983.",
        "3. P. Freymuth, “History of thermal anemometry,” in N. P. Cheremisinoff and R. Gupta (ed.), "
        "<i>Handbook of Fluids in Motion</i>, Ann Arbor, MI: Ann Arbor Science Publishers, 1983.",
        "4. J. C. Gibbings, J. Madadnia, and A. H. Yousif, “The wall correction of the hot-wire "
        "anemometer,” <i>Flow Meas. Instrum.</i>, 6(2), 127–136, 1995.",
        "5. J. C. Gibbings, J. Madadnia, S. Riley, and A. H. Yousif, “The proximity hot-wire probe for "
        "measuring surface shear in air flows,” <i>Flow Meas. Instrum.</i>, 6(3), 201–206, 1995.",
        "6. V. Mikulla, <i>The Measurement of Intensities and Stresses of Turbulence in "
        "Incompressible and Compressible Air Flow</i>, Ph.D. thesis, University of Liverpool, 1972.",
        "7. L. V. King, “On the convection of heat from small cylinders in a stream of fluid: "
        "determination of the convection constants of small platinum wires with application to "
        "hot-wire anemometry,” <i>Phil. Trans. Roy. Soc.</i>, A214, 373–432, 1914.",
        "8. H. Kramers, “Heat transfer from spheres to flowing media,” <i>Physica</i>, 12, 61–80, 1946.",
        "9. S. W. Churchill and M. Bernstein, “A correlating equation for forced convection from gases "
        "and liquids to a circular cylinder in crossflow,” <i>J. Heat Transfer</i>, 99, 300–306, 1997.",
        "10. S. Takagi, “A hot-wire anemometer compensated for ambient temperature variations,” "
        "<i>J. Phys. E.: Sci. Instrum.</i>, 19, 739–743, 1986.",
        "11. J. W. Elsner, “An analysis of hot-wire sensitivity in non-isothermal flow,” <i>Proc. "
        "Dynamics Flow Conf.</i>, Marseille, 1972.",
        "12. R. F. Blackwelder, “Hot-wire and hot-film anemometers,” in R. J. Emrich (ed.), "
        "<i>Methods of Experimental Physics: Fluid Dynamics</i>, New York: Academic Press, 18A, "
        "259–314, 1981.",
        "13. J. A. Borgos, “A review of electrical testing of hot-wire and hot-film anemometers,” "
        "<i>TSI Quart.</i>, VI(3), 3–9, 1980.",
        "14. E. W. Nelson and J. A. Borgos, “Dynamic response of conical and wedge type hot films: "
        "comparison of experimental and theoretical results,” <i>TSI Quart.</i>, IX(1), 3–10, 1983.",
        "15. U. R. Müller, “Comparison of turbulence measurements with single, X and triple hot-wire "
        "probes,” <i>Exp. in Fluids</i>, 13, 208–216, 1992.",
        "16. K. Döbbeling, B. Lenze, and W. Leuckel, “Four-sensor hot-wire probe measurements of the "
        "isothermal flow in a model combustion chamber with different levels of swirl,” <i>Exp. "
        "Thermal and Fluid Sci.</i>, 5, 381–389, 1992.",
        "17. J. G. Olin and R. B. Kiland, “Split-film anemometer sensors for three-dimensional "
        "velocity-vector measurement,” <i>Proc. Symp. on Aircraft Wake Turbulence</i>, Seattle, "
        "Washington, 1970, 57–79.",
        "18. F. E. Jörgenson, “Directional sensitivity of wire and fibre-film probes,” <i>DISA "
        "Info.</i>, (11), 31–37, 1971.",
        "19. I. C. Lekakis, R. J. Adrian, and B. G. Jones, “Measurement of velocity vectors with "
        "orthogonal and non-orthogonal triple-sensor probes,” <i>Experiments in Fluids</i>, 7, "
        "228–240, 1989.",
        "20. J. G. Olin, “A thermal mass flow monitor for continuous emissions monitoring systems "
        "(CEMS),” <i>Proc. ISA/93 Int. Conf. Exhibition &amp; Training Program</i>, (93-404), 1993, "
        "1637–1653.",
        "21. J. G. Olin, “Thermal flow monitors take on utility stack emissions,” "
        "<i>Instrumentation and Control Systems</i>, 67(2), 71–73, 1994.",
    ]


def _refs293(lang):
    """The §29.3 bibliography. Titles are left in the original language, as in
    §29.1 and §29.2: a reader looking a paper up needs the title as printed."""
    return [
        "1. D. Niccum, “A new tool for fiber spinning process control and diagnostics,” <i>Int. Fiber "
        "J.</i>, 10(1), 48–57, 1995.",
        "2. R. Schodl, “On the extension of the range of applicability of LDA by means of the "
        "laser-dual-focus (L-2-F) technique,” <i>The Accuracy of Flow Measurements by Laser Doppler "
        "Methods</i>, Skovlunde, Denmark: Dantec Measurement Technology, 1976, 480–489.",
        "3. R. J. Adrian, “Particle imaging techniques for experimental fluid mechanics,” <i>Annu. "
        "Rev. Fluid Mech.</i>, 23, 261–304, 1991.",
        "4. I. Grant, <i>Selected Papers in Particle Image Velocimetry</i>, SPIE Milestone Series, "
        "MS 99, Bellingham, WA: SPIE Optical Engineering Press, 1994.",
        "5. R. J. Adrian, <i>Bibliography of Particle Velocimetry Using Imaging Methods: "
        "1917–1995</i>, TAM Report, University of Illinois Urbana-Champaign, produced and "
        "distributed in cooperation with TSI Inc., March 1996. (Also available in electronic "
        "format.)",
        "6. W. T. Lai, “Particle image velocimetry: a new approach to experimental fluid research,” "
        "in Th. Dracos (ed.), <i>Three Dimensional Velocity and Vorticity Measuring and Image "
        "Analysis Techniques</i>, Boston: Kluwer Academic, 1996, 61–92.",
        "7. M. M. Koochesfahani, R. K. Cohn, C. P. Gendrich, and D. G. Nocera, “Molecular tagging "
        "diagnostics for the study of kinematics and mixing in liquid phase flows,” <i>8th Int. "
        "Symp. Appl. Laser Techniques Fluid Mechanics</i>, Lisbon, 1996.",
        "8. H. Komine, S. J. Brosnan, A. B. Litton, and E. A. Stappaerts, “Real time Doppler global "
        "velocimetry,” <i>AIAA 29th Aerospace Sciences Meeting</i>, Paper No. AIAA-91-0337, January "
        "1991.",
        "9. R. L. McKenzie, “Measurement capabilities of planar Doppler velocimetry using pulsed "
        "lasers,” <i>Appl. Opt.</i>, 35, 948–964, 1996.",
        "10. C. Berner, “Supersonic base flow investigation over axisymmetric bodies,” <i>Proc. 5th "
        "Int. Conf. Laser Anemometry and Applications</i>, Netherlands, SPIE, 2052, 1993.",
        "11. K. Jaffri, H. G. Hascher, M. Novak, K. Lee, H. Schock, M. Bonne, and P. Keller, “Tumble "
        "and swirl quantification within a four-valve SI engine cylinder based on 3D LDV "
        "measurements,” SAE Paper No. 970792, February 1997.",
        "12. G. G. Podboy and M. J. Krupar, <i>Laser Velocimeter Measurements of the Flow Field "
        "Generated by a Forward-Swept Propfan During Flutter</i>, NASA Technical Memorandum 106195, "
        "1993.",
        "13. Y. O. Han, J. G. Leishman, and A. J. Coyne, “Measurements of the velocity and turbulence "
        "structure of a rotor tip vortex,” <i>AIAA J.</i>, 35, 477–485, 1997.",
        "14. T. Mathur and J. C. Dutton, “Velocity and turbulence measurements in a supersonic base "
        "flow with mass bleed,” <i>AIAA J.</i>, 34, 1153–1159, 1996.",
        "15. E. J. Johnson, P. V. Hyer, P. W. Culotta, and I. O. Clark, “Laser velocimetry in "
        "nonisothermal CVD systems,” <i>Proc. 4th Int. Conf. Laser Anemometry</i>, Cleveland, OH, "
        "August 1991.",
        "16. R. W. Dibble, V. Hartmann, R. W. Schefer, and W. Kollmann, “Conditional sampling of "
        "velocity and scalars in turbulent flames using simultaneous LDV-Raman scattering,” <i>Exp. "
        "Fluids</i>, 5, 103–113, 1987.",
        "17. D. V. Srikantiah and W. W. Wilson, “Detection of a pulsed flow in an MHD environment by "
        "laser velocimetry,” <i>Exp. Fluids</i>, 6, 500–503, 1988.",
        "18. P. O. Witze, “Velocity measurements in end-gas region during homogeneous-charge "
        "combustion in a spark ignition engine,” in Adrian et al. (eds.), <i>Laser Techniques and "
        "Applications in Fluid Mechanics</i>, Lisbon: Ladoan, 1992, 518–534.",
        "19. G. L. Morrison, M. C. Johnson, R. E. DeOtte, H. D. Thames, and B. J. Wiedner, “An "
        "experimental technique for performing 3D LDA measurements inside whirling annular seals,” "
        "<i>Flow Meas. Instrum.</i>, 5, 43–49, 1994.",
        "20. F. Durst, A. Melling, and J. H. Whitelaw, <i>Principles and Practice of Laser Doppler "
        "Anemometry</i>, 2nd ed., New York: Academic Press, 1981.",
        "21. R. J. Adrian (ed.), <i>Selected Papers on Laser Doppler Velocimetry</i>, SPIE Milestone "
        "Series, MS 78, Bellingham, WA: SPIE Optical Engineering Press, 1993.",
        "22. W. D. Bachalo and M. J. Houser, “Phase Doppler spray analyzer for simultaneous "
        "measurements of drop size and velocity distributions,” <i>Opt. Eng.</i>, 23, 583–590, 1984.",
        "23. Y. Yeh and H. Z. Cummins, “Localized fluid flow measurements with an He-Ne laser "
        "spectrometer,” <i>Appl. Phys. Lett.</i>, 4, 176–178, 1964.",
        "24. C. M. Penney, “Differential Doppler velocity measurements,” <i>IEEE J. Quantum "
        "Electron.</i>, QE-5, 318, 1969.",
        "25. L. M. Fingerson and P. Freymuth, “Thermal anemometers,” in R. J. Goldstein (ed.), "
        "<i>Fluid Mechanics Measurements</i>, New York: Hemisphere, 1983, 99–154.",
        "26. G. Smeets and A. George, “Michelson spectrometer for instantaneous Doppler velocity "
        "measurements,” <i>J. Phys. E: Sci. Instrum.</i>, 14, 838–845, 1981.",
        "27. D. Brayton, “Small particle signal characteristics of a dual scatter laser "
        "velocimeter,” <i>J. Appl. Opt.</i>, 13, 2346–2351, 1974.",
        "28. F. Durst and W. H. Stevenson, “Moiré patterns to visually model laser Doppler signals,” "
        "<i>The Accuracy of Flow Measurements by Laser Doppler Methods</i>, Skovlunde, Denmark: "
        "Dantec Measurement Technology, 1976, 183–205.",
        "29. R. J. Adrian, “Laser velocimetry,” in R. J. Goldstein (ed.), <i>Fluid Mechanics "
        "Measurements</i>, New York: Hemisphere, 1983, 155–240.",
        "30. R. J. Adrian and K. L. Orloff, “Laser anemometer signal: visibility characteristics and "
        "application to particle sizing,” <i>Appl. Opt.</i>, 16, 677–684, 1977.",
        "31. L. M. Fingerson, R. J. Adrian, R. K. Menon, S. L. Kaufman, and A. Naqwi, <i>Data "
        "Analysis, Laser Doppler Velocimetry and Particle Image Velocimetry</i>, TSI Short Course "
        "Text, TSI Inc., St. Paul, MN, 1993.",
        "32. H. Kogelnik and T. Li, “Laser beams and resonators,” <i>Appl. Opt.</i>, 5, 1550–1567, "
        "1966.",
        "33. M. C. Whiffen, “Polar response of an LV measurement volume,” <i>Minnesota Symp. Laser "
        "Anemometry</i>, University of Minnesota, 1975.",
        "34. C. Tropea, “A practical aid for choosing the shift frequency in LDA,” <i>Exp. "
        "Fluids</i>, 4, 79–80, 1986.",
        "35. M. K. Mazumder, “Laser Doppler velocity measurement without directional ambiguity by "
        "using frequency shifted incident beams,” <i>Appl. Phys. Lett.</i>, 16, 462–464, 1970.",
        "36. H. Muller, V. Tobben, V. Arndt, V. Strunck, H. Wang, R. Kramer, and D. Dopheide, “New "
        "frequency shift techniques in laser anemometry using tunable semiconductor lasers and "
        "solid state lasers,” <i>Proc. 2nd Int. Conf. Fluid Dynamic Measurement Applications</i>, "
        "Beijing, October 1994, 3–19.",
        "37. E. Muller, H. Nobach, and C. Tropea, “LDA signal reconstruction: application to moment "
        "and spectral estimation,” <i>Proc. 7th Int. Symp. Applications Laser Techniques Fluid "
        "Mechanics</i>, Lisbon, 1994b.",
        "38. R. J. Adrian and W. L. Early, “Evaluation of laser Doppler velocimeter performance using "
        "Mie scattering theory,” <i>Proc. Minnesota Symp. Laser Anemometry</i>, University of "
        "Minnesota, 1975, 429–454.",
        "39. G. Grehan, G. Gouesbet, A. Naqwi, and F. Durst, “Trajectory ambiguities in phase Doppler "
        "systems: study of a new forward and a near-backward geometry,” <i>Part. Part. Syst. "
        "Charact.</i>, 11, 133–144, 1994.",
        "40. D. J. Fry, “Model submarine wake survey using internal LDV probes,” <i>Proc. ASME Fluids "
        "Engineering Meeting</i>, T. T. Huang, J. Turner, M. Kawahashi, and M. V. Otugen (eds.), "
        "FED-Vol. 229, August 1995, 159–170.",
        "41. P. A. Chevrin, H. L. Petrie, and S. Deutsch, “Accuracy of a three-component laser "
        "Doppler velocimeter system using a single lens approach,” <i>J. Fluids Eng.</i>, 115, "
        "142–147, 1993.",
        "42. R. I. Karlsson and T. G. Johansson, “LDV measurements of higher order moments of "
        "velocity fluctuations in a turbulent boundary layer,” in <i>Laser Anemometry in Fluid "
        "Mechanics III</i>, Ladoan-Instituto Superior Técnico, 1096 Lisbon Codex, Portugal, 1988, "
        "273–289.",
        "43. K. M. Ibrahim, G. D. Werthimer, and W. D. Bachalo, “Signal processing considerations for "
        "laser Doppler and phase Doppler applications,” <i>Proc. 5th Int. Symp. Applications Laser "
        "Techniques Fluid Mechanics</i>, Lisbon, 1990.",
        "44. L. Jenson, “LDV digital signal processor based on autocorrelation,” <i>Proc. 6th Int. "
        "Symp. Applications Laser Techniques Fluid Mechanics</i>, Lisbon, 1992.",
        "45. W. W. Hunter and C. E. Nichols (compilers), <i>Wind Tunnel Seeding Systems for Laser "
        "Velocimeters</i>, NASA Conference Publication 2393, 1985.",
        "46. A. Melling, “Seeding gas flows for laser anemometry,” <i>AGARD CP-339</i>, 1986, "
        "8-1–8-11.",
        "47. R. K. Menon and W. T. Lai, “Key considerations in the selection of seed particles for "
        "LDV measurements,” <i>Proc. 4th Int. Conf. Laser Anemometry</i>, Cleveland, OH, August "
        "1991.",
        "48. M. L. Lowe and P. H. Kutt, “Refraction through cylindrical tubes,” <i>Exp. Fluids</i>, "
        "13, 315–320, 1992.",
        "49. R. Budwig, “Refractive index matching methods for liquid flow investigations,” <i>Exp. "
        "Fluids</i>, 17, 350–355, 1994.",
        "50. D. K. McLaughlin and W. G. Tiederman, “Biasing correction for individual realization of "
        "laser anemometer measurements in turbulent flows,” <i>Phys. Fluids</i>, 16, 2082–2088, "
        "1973.",
        "51. R. D. Gould and K. W. Loseke, “A comparison of four velocity bias correction techniques "
        "in laser Doppler velocimetry,” <i>J. Fluids Eng.</i>, 115, 508–514, 1993.",
        "52. R. V. Edwards (ed.), “Report on the special panel on statistical particle bias problems "
        "in laser anemometry,” <i>J. Fluids Eng.</i>, 109, 89–93, 1987.",
        "53. J. B. Roberts, J. Downie, and M. Gaster, “Spectral analysis of signals from a laser "
        "Doppler anemometer operating in the burst mode,” <i>J. Physics, E: Sci. Instrum.</i>, 13, "
        "977–981, 1980.",
        "54. W. T. Mayo, “Spectrum measurements with laser velocimeters,” <i>Proc. Dynamic Flow Conf. "
        "Dynamic Measurements in Unsteady Flows</i>, DISA Electronik A/S, Denmark, 1978, 851–868.",
        "55. H. L. Petrie, “Reduction of noise effects on power spectrum estimates using the "
        "discretized lag product method,” <i>ASME Fluids Engineering Meeting</i>, FED-229, 139–144, "
        "1995.",
        "56. W. D. Bachalo, A. Brena de la Rosa, and S. V. Sankar, “Diagnostics for fuel spray "
        "characterization,” in N. Chigier (ed.), <i>Combustion Measurements</i>, New York: "
        "Hemisphere, 1991, chap. 7.",
        "57. F. Durst and M. Zare, “Laser Doppler measurements in two-phase flows,” <i>The Accuracy "
        "of Flow Measurements by Laser Doppler Methods</i>, Skovlunde, Denmark: Dantec Measurement "
        "Technology, 1976, 480–489.",
        "58. M. Saffman, “The use of polarized light for optical particle sizing,” in Adrian et al. "
        "(eds.), <i>Laser Anemometry in Fluid Mechanics III</i>, Lisbon: Ladoan, 1988, 387–398.",
        "59. A. Naqwi, “Innovative phase Doppler systems and their applications,” <i>Part. Part. "
        "Syst. Charact.</i>, 11, 7–21, 1994.",
        "60. S. V. Sankar, D. A. Robart, and W. D. Bachalo, “An adaptive intensity validation "
        "technique for minimizing trajectory dependent scattering errors in phase Doppler "
        "interferometry,” <i>Proc. 4th Int. Congr. Optical Particle Sizing</i>, Nuremberg, Germany, "
        "March 1995.",
        "61. A. Naqwi and F. Durst, “Light scattering applied to LDA and PDA measurements. 2. "
        "Computational results and their discussion,” <i>Part. Part. Syst. Charact.</i>, 9, 66–80, "
        "1992.",
        "62. A. Naqwi, “In-situ measurement of submicron droplets in electrosprays using a planar "
        "phase Doppler system,” <i>J. Aerosol Sci.</i>, 25, 1201–1211, 1994.",
        "63. S. V. Sankar, D. H. Buermann, D. A. Robart, and W. D. Bachalo, “An advanced rainbow "
        "signal processor for improved accuracy of droplet temperature measurements in spray "
        "flames,” <i>Proc. 8th Int. Symp. Applications Laser Techniques Fluid Mechanics</i>, Lisbon, "
        "1996.",
        "64. J. Evenstad, A. Naqwi, and R. Menon, “A device for phase shift measurement in an "
        "advanced phase Doppler velocimeter,” <i>Proc. 8th Int. Symp. Applications Laser Techniques "
        "Fluid Mechanics</i>, Lisbon, 1996.",
        "65. K. M. Ibrahim and W. D. Bachalo, “A novel architecture for real-time phase "
        "measurement,” <i>Proc. 8th Int. Symp. Applications of Laser Techniques to Fluid "
        "Mechanics</i>, Lisbon, 1996.",
        "66. M. Saffman, P. Buchave, and H. Tanger, “Simultaneous measurement of size, concentration "
        "and velocity of spherical particles by a laser Doppler method,” in R. J. Adrian et al. "
        "(eds.), <i>Laser Anemometry in Fluid Mechanics II</i>, Lisbon: Ladoan, 1986, 85–104.",
        "67. A. Naqwi, “Sizing of irregular particles using a phase Doppler system,” <i>Proc. ASME "
        "Heat Transfer and Fluid Engineering Divisions</i>, FED-Vol. 233, 1995.",
    ]


def _refs293b(lang):
    return [
        "C. A. Greated and T. S. Durrani, <i>Laser Systems and Flow Measurement</i>, New York: "
        "Plenum, 1977.",
        "L. E. Drain, <i>The Laser Doppler Technique</i>, New York: John Wiley &amp; Sons, 1980.",
        "<i>Proc. Int. Symp. (1 to 8) on Applications of Laser Techniques to Fluid Mechanics</i>, "
        "Lisbon, Portugal, 1982, 1984, 1986, 1988, 1990, 1992, 1994, 1996.",
        "P. Buchave, W. K. George, and J. L. Lumley, “The measurement of turbulence with the laser "
        "Doppler anemometer,” <i>Annu. Rev. Fluid Mech.</i>, 11, 443–504, 1979.",
        "<i>Proc. 5th Int. Conf. Laser Anemometry and Applications</i>, Netherlands, SPIE, Vol. 2052, "
        "1993.",
        "<i>Proc. ASME Fluids Engineering Meeting</i>, T. T. Huang, J. Turner, M. Kawahashi, and "
        "M. V. Otugen (eds.), FED-Vol. 229, August 1995.",
        "L. H. Benedict and R. D. Gould, “Experiences using the Kalman reconstruction for enhanced "
        "power spectrum estimates,” <i>Proc. ASME Fluids Engineering Meeting</i>, T. T. Huang, "
        "J. Turner, M. Kawahashi, and M. V. Otugen (eds.), FED 229, 1–8, 1995.",
        "D. Dopheide, M. Faber, G. Reim, and G. Taux, “Laser and avalanche diodes for velocity "
        "measurement by laser Doppler anemometry,” <i>Exp. Fluids</i>, 6, 289–297, 1988.",
        "F. Durst, R. Muller, and A. Naqwi, “Measurement accuracy of semiconductor LDA systems,” "
        "<i>Exp. Fluids</i>, 10, 125–137, 1990.",
        "A. Naqwi and F. Durst, “Light scattering applied to LDA and PDA measurements. 1. Theory and "
        "numerical treatments,” <i>Particle and Particle System Characterization</i>, 8, 245–258, "
        "1991.",
    ]


# ================================================================ 29.2 VI

def sec_29_2_vi():
    b = []
    b.append(h2("29.2 Đo vận tốc bằng nhiệt", "Thermal Anemometry"))
    b.append(p("John G. Olin — Sierra Instruments, Inc."))

    b.append(h3("Mô tả chung", "General Description"))
    b.append(p(
        "Nhiệt kế gió đo vận tốc tại một điểm trong dòng chất lưu — lỏng hoặc khí. Hình 29.17 "
        "trình bày một nhiệt kế gió công nghiệp điển hình dùng để theo dõi vận tốc trong dòng khí. "
        "Nó có hai cảm biến — một cảm biến vận tốc và một cảm biến nhiệt độ — tự động hiệu chỉnh "
        "theo sự thay đổi nhiệt độ khí."))
    b.append(fig(17, F.FIGS[16], "vi"))
    b.append(p(
        "Cả hai cảm biến đều là đầu dò nhiệt điện trở bạch kim (RTD) cấp chuẩn. Điện trở của RTD "
        "tăng khi nhiệt độ tăng. Vì lý do này, chúng là một trong những cảm biến được dùng phổ biến "
        "nhất cho phép đo nhiệt độ chính xác. Mạch điện tử cho dòng điện chạy qua cảm biến vận tốc, "
        "nhờ đó nung nóng nó tới một chênh lệch nhiệt độ không đổi (T<sub>v</sub> − T<sub>a</sub>) "
        "so với nhiệt độ khí T<sub>a</sub>, và đo nhiệt lượng q<sub>c</sub> bị dòng khí nguội hơn "
        "mang đi khi nó chảy qua cảm biến. Vì vậy thiết bị được gọi là “nhiệt kế gió nhiệt độ không "
        "đổi”."))
    b.append(p(
        "Do nhiệt được mang đi bởi chính các phân tử khí, cảm biến được nung nóng đo trực tiếp "
        "<b>vận tốc khối</b> của khí (lưu lượng khối trên một đơn vị diện tích) ρU. Vận tốc khối "
        "thường được biểu diễn bằng U<sub>s</sub> theo đơn vị kỹ thuật là mét chuẩn trên giây, hay "
        "m chuẩn s⁻¹, quy về điều kiện chuẩn 0 °C hoặc 20 °C và 1 atm. Nếu nhiệt độ và áp suất của "
        "chất lưu không đổi thì phép đo của nhiệt kế gió có thể biểu diễn bằng mét thực trên giây, "
        "hay m s⁻¹. Khi nhân vận tốc khối với diện tích mặt cắt của kênh dẫn, ta được lưu lượng "
        "khối qua kênh. Trong phần lớn ứng dụng thực tế và công nghiệp — mọi phản ứng hoá học, quá "
        "trình cháy, gia nhiệt, làm nguội, sấy, trộn, truyền động bằng chất lưu, hô hấp của người, "
        "khí tượng và đối lưu tự nhiên — đại lượng trực tiếp cần biết là lưu lượng khối chứ không "
        "phải lưu lượng thể tích."))
    b.append(p(
        "Nhiệt kế gió thường được gọi là <b>lưu lượng kế khối nhiệt kiểu nhúng</b> vì nó được nhúng "
        "vào dòng chảy, khác với lưu lượng kế khối nhiệt kiểu ống mao dẫn — một phương pháp nhiệt "
        "khác thường được cấu hình thành lưu lượng kế khối thẳng dòng cho dòng khí nhỏ. So với hai "
        "dụng cụ đo vận tốc điểm thông dụng còn lại là ống Pitot và nhiệt kế gió Doppler laser, "
        "nhiệt kế gió có cả ưu điểm lẫn nhược điểm. So với ống Pitot, nhiệt kế gió đo được vận tốc "
        "thấp hơn, có dải đo rộng hơn nhiều và có thể chế tạo nhỏ hơn, nhưng giá thường cao hơn và "
        "không được khuyến nghị cho dòng chất lỏng ngoài mục đích nghiên cứu. So với nhiệt kế gió "
        "Doppler laser, nhiệt kế gió rẻ hơn nhiều, không cần gieo hạt vào dòng, có thể có đáp ứng "
        "thời gian nhanh hơn, có thể có độ phân giải không gian tốt hơn và có thể có tỉ số tín "
        "hiệu trên nhiễu cao hơn. Ngược lại, trong dòng không dao động, nhiệt kế gió Doppler laser "
        "cho một phép đo vận tốc mang tính chuẩn mực, độc lập với nhiệt độ và tính chất chất lưu. "
        "Vì lý do đó, chúng thường được dùng để hiệu chuẩn nhiệt kế gió."))
    b.append(p(
        "Nhiệt kế gió được chia thành hai loại: công nghiệp và nghiên cứu. Hình 29.18 cho thấy các "
        "cảm biến điển hình của nhiệt kế gió công nghiệp và nghiên cứu."))
    b.append(fig(18, F.FIGS[17], "vi"))

    b.append(h4("Nhiệt kế gió công nghiệp", "Industrial Thermal Anemometers"))
    b.append(p(
        "Nhiệt kế gió công nghiệp đo vận tốc điểm hoặc vận tốc khối điểm của khí trong hầu hết ứng "
        "dụng thực tế và công nghiệp. Chúng ít khi được dùng để theo dõi dòng chất lỏng, vì việc "
        "tránh hiện tượng xâm thực buộc nhiệt độ T<sub>v</sub> của cảm biến vận tốc chỉ được cao "
        "hơn nhiệt độ chất lỏng 10 °C đến 20 °C, làm giảm độ nhạy vận tốc và tăng sự phụ thuộc vào "
        "những thay đổi nhỏ của nhiệt độ chất lỏng. Ngoài ra, dòng chất lỏng công nghiệp có thể làm "
        "bẩn và đóng cặn cảm biến."))
    b.append(p(
        "Các khí điển hình được nhiệt kế gió công nghiệp theo dõi gồm không khí, nitơ, oxy, cacbon "
        "đioxit, mêtan, khí tự nhiên, propan, hyđrô, argon, heli và khí ống khói. Các ứng dụng phổ "
        "biến là: không khí cháy; không khí gia nhiệt sơ bộ; khí nhiên liệu; khí ống khói; phân phối "
        "khí tự nhiên; phân phối khí trong sản xuất bán dẫn; sưởi, thông gió và điều hoà không khí; "
        "quét đa điểm các ống dẫn và ống khói lớn; sấy; sục khí và khí hầm ủ; giám sát an toàn và "
        "sức khoẻ nghề nghiệp; các nghiên cứu môi trường, đối lưu tự nhiên và năng lượng mặt trời; "
        "thiết bị lên men; và theo dõi hơi thở của người. Nhiệt kế gió công nghiệp đã trở thành "
        "dụng cụ được dùng phổ biến nhất để theo dõi vận tốc điểm của khí."))
    b.append(p(
        "Cảm biến vận tốc của nhiệt kế gió công nghiệp là một dây bạch kim cấp chuẩn (đường kính "
        "khoảng 25 µm, điện trở 20 Ω) quấn quanh một lõi gốm hình trụ, chẳng hạn alumin. Một cách "
        "khác, cảm biến là một màng bạch kim mỏng lắng trên đế thuỷ tinh hoặc gốm. Để chịu được môi "
        "trường khắc nghiệt gặp trong nhiều ứng dụng công nghiệp, RTD bạch kim hình trụ được gắn "
        "chặt bằng xi măng vào đầu một ống thành mỏng bằng thép không gỉ, Hastelloy hoặc Inconel "
        "(thường đường kính ngoài 3 mm, dài 2 cm đến 6 cm). Vì nhiệt độ khí thường thay đổi trong "
        "ứng dụng công nghiệp, đầu dò nhiệt kế gió công nghiệp gần như luôn có thêm một cảm biến "
        "RTD bạch kim không nung nóng, đặt riêng nhưng gắn liền, để đo nhiệt độ khí cục bộ "
        "T<sub>a</sub>. Khi làm việc ở chế độ nhiệt độ không đổi, chênh lệch nhiệt độ "
        "(T<sub>v</sub> − T<sub>a</sub>) thường nằm trong khoảng 30 °C đến 100 °C. Cảm biến nhiệt "
        "độ được chế tạo giống hệt cảm biến vận tốc nhưng có điện trở trong khoảng 300 Ω đến "
        "1000 Ω. Như trên Hình 29.17, đầu dò hai cảm biến có cảm biến vận tốc và cảm biến nhiệt độ "
        "gắn cạnh nhau trên một thân trụ (thường đường kính 6 mm đến 25 mm, dài 0,1 m đến 3 m). "
        "Thường có một tấm chắn để tránh làm vỡ đầu cảm biến. Độ phân giải không gian của nhiệt kế "
        "gió công nghiệp này là 1 cm đến 2 cm. Bộ điện tử của nhiệt kế gió công nghiệp thường được "
        "gắn trực tiếp trên thân đầu dò trong một vỏ chống nổ. Các hệ nhiệt kế gió công nghiệp như "
        "vậy đo vận tốc khí trong dải 0,5 m chuẩn s⁻¹ đến 150 m chuẩn s⁻¹."))
    b.append(p(
        "Khi sử dụng, đầu dò nhiệt kế gió công nghiệp được đưa xuyên qua một khớp nén kín hoặc một "
        "ống nối có mặt bích trên thành ống dẫn, đường ống, ống khói hay kênh dòng khác. Trong "
        "trường hợp này nó thường được gọi là <b>lưu lượng kế khối nhiệt kiểu cắm</b>. Ở một cấu "
        "hình phổ biến khác, đầu dò hai cảm biến được lắp cố định vào một đường ống hoặc ống nhỏ "
        "(thường đường kính 8 mm đến 300 mm) với các mối nối khí ren hoặc mặt bích. Cấu hình này "
        "được gọi là <b>lưu lượng kế khối nhiệt thẳng dòng</b>. Các lưu lượng kế thẳng dòng được "
        "hiệu chuẩn trực tiếp cho tổng lưu lượng khối của khí chảy qua ống. Nhiều cỡ thân dòng cho "
        "phép theo dõi lưu lượng khối trong dải 10 mg s⁻¹ đến 10 kg s⁻¹."))

    b.append(h4("Nhiệt kế gió nghiên cứu", "Research Thermal Anemometers"))
    b.append(p(
        "Nhiệt kế gió nghiên cứu đo vận tốc điểm và/hoặc độ rối của khí và chất lỏng sạch trong "
        "nghiên cứu, phát triển sản phẩm và ứng dụng phòng thí nghiệm. Vì dễ vỡ hơn, chúng không "
        "được dùng cho ứng dụng công nghiệp. Khí thường là không khí môi trường. Chất lỏng chủ yếu "
        "là nước đã lọc, khử khí, giữ ở nhiệt độ không đổi, nhưng kỹ thuật này cũng đã được áp dụng "
        "cho các hyđrôcacbon lỏng sạch. Như trên Hình 29.18, cảm biến vận tốc của nhiệt kế gió "
        "nghiên cứu là dây nóng hoặc màng nóng. Cảm biến dây nóng có đáp ứng tần số cao và do đó "
        "rất tốt cho đo độ rối trong không khí và các khí khác. Chúng ít khi được dùng trong dòng "
        "chất lỏng vì dễ bị đóng cặn và nhiễm bẩn. Cảm biến màng nóng đánh đổi đáp ứng tần số thấp "
        "hơn để lấy độ bền cao hơn và được dùng trong dòng khí lẫn dòng lỏng. Với dòng chất lỏng, "
        "cảm biến màng nóng được thiết kế để tự làm trôi đi xơ vải và các vật liệu gây bẩn hoặc "
        "nhiễm khác. Bruun [1] là một nguồn tài liệu xuất sắc về lý thuyết và ứng dụng của nhiệt kế "
        "gió dây nóng và màng nóng. Một nguồn toàn diện khác là Fingerson và Freymuth [2]."))
    b.append(p(
        "Các ứng dụng điển hình của nhiệt kế gió dây nóng và màng nóng gồm: nghiên cứu dòng và độ "
        "rối một, hai và ba chiều; kiểm chứng các mã tính toán động lực học chất lưu; các phép đo "
        "môi trường và vi khí tượng; tuabin máy; động cơ đốt trong; nghiên cứu sinh học; nghiên cứu "
        "truyền nhiệt; đo lớp biên; dòng trên âm; dòng hai pha; và đo độ xoáy. Freymuth [3] mô tả "
        "lịch sử 80 năm của nhiệt kế gió nghiên cứu. Ngày nay, nhiệt kế gió dây nóng và màng nóng "
        "đã trở thành những dụng cụ được dùng rộng rãi nhất cho nghiên cứu và phát triển trong cơ "
        "học chất lưu."))
    b.append(p(
        "Cảm biến dây nóng điển hình là một dây vonfram mảnh hàn ở mỗi đầu vào các chân nhỏ được "
        "thiết kế để giảm thiểu ảnh hưởng của chúng lên trường dòng quanh dây. Dây thường được mạ "
        "vàng hoặc đồng một đoạn ngắn ở mỗi đầu để xác định chiều dài cảm biến tích cực, cách xa hai "
        "chân. Để làm việc trong nước, dây được phủ thạch anh nhằm chống điện phân hoặc ngắn mạch, "
        "nhưng khi đó lớp phủ có thể bị nứt. Một dây vonfram điển hình có đường kính 4 µm đến 5 µm, "
        "chiều dài tích cực 1 mm đến 3 mm và điện trở 2 Ω đến 6 Ω. Vì bị oxy hoá trên 350 °C trong "
        "không khí, dây nóng vonfram thường được vận hành ở nhiệt độ không quá 300 °C. Dây bạch "
        "kim, dây 90 % bạch kim + 10 % rhodi và dây 80 % bạch kim + 20 % iridi cũng được dùng. "
        "Chúng có thể được hàn vào chân nhưng yếu hơn vonfram. Trong trường hợp nhiệt độ chất lưu "
        "T<sub>a</sub> thay đổi đủ để gây sai số đo, người ta dùng một cảm biến riêng để đo "
        "T<sub>a</sub> và hiệu chỉnh nhiệt độ. Cảm biến nhiệt độ là một dây nóng hoặc một RTD quấn "
        "dây lớn hơn, gắn trên một đầu dò riêng hoặc liền trên cùng thân đầu dò với cảm biến vận "
        "tốc. Như trên Hình 29.18, với nghiên cứu dòng hai chiều hoặc ba chiều, người ta dùng đầu dò "
        "có hai dây vuông góc xếp theo hình chữ “X” hoặc ba dây trực giao. Các đầu dò siêu nhỏ đặc "
        "biệt và các đầu dò có chân dời khỏi thân được dùng cho công việc gần thành và lớp biên, "
        "cũng như cho các kênh dòng nhỏ. Gibbings và cộng sự [4, 5] mô tả các đầu dò dây nóng dùng "
        "cho nghiên cứu lớp biên rối gần thành."))
    b.append(p(
        "Như trên Hình 29.18, cảm biến màng nóng điển hình là một thanh thạch anh đầu hình nêm hoặc "
        "hình nón, có một màng bạch kim dày 0,1 µm mạ trên đầu bằng phương pháp phún xạ catôt. Màng "
        "bạch kim thường được phủ một lớp thạch anh dày 1 µm đến 2 µm để bảo vệ và tránh ngắn mạch "
        "điện hoặc điện phân trong dòng nước. Vì cảm biến màng nóng có khối lượng lớn hơn nhiều so "
        "với cảm biến dây nóng, đáp ứng tần số của chúng không phẳng bằng, nên chúng không tốt bằng "
        "cho đo độ rối tần số cao. Mikulla [6] cũng đã quan sát thấy hình dạng của một số cảm biến "
        "màng nóng có thể làm giảm đáp ứng với thành phần vận tốc rối vuông góc với bề mặt của nó. "
        "Ngược lại, cảm biến màng nóng ít vỡ hơn và có hình học ổn định hơn cảm biến dây nóng. Các "
        "cấu hình khác của cảm biến màng nóng gồm: thanh thạch anh hình trụ (đường kính khoảng "
        "25 µm đến 150 µm); một hoặc nhiều cảm biến trụ màng tách đôi cho phép đo đa chiều; và các "
        "cảm biến gắn phẳng cho đo truyền nhiệt qua thành."))

    b.append(h3("Nguyên lý làm việc", "Principle of Operation"))
    b.append(h4("Định luật thứ nhất của nhiệt động học", "First Law of Thermodynamics"))
    b.append(p(
        "Hình 29.19 trình bày định luật thứ nhất của nhiệt động học áp dụng cho một thể tích kiểm "
        "soát là cảm biến vận tốc của nhiệt kế gió công nghiệp (như trên Hình 29.17) hoặc của nhiệt "
        "kế gió nghiên cứu. Áp dụng định luật thứ nhất cho cảm biến nhiệt kế gió là cơ sở để xác "
        "định vận tốc điểm. Áp dụng cho Hình 29.19, định luật thứ nhất phát biểu rằng năng lượng "
        "đi vào thể tích kiểm soát bằng năng lượng đi ra cộng với năng lượng tích lại. Với hai giả "
        "thiết đơn giản hoá thực tế là làm việc ở trạng thái ổn định (tức không có năng lượng tích "
        "lại) và không truyền nhiệt bằng bức xạ, ta được:"))
    b.append(eq("w = q<sub>c</sub> + q<sub>L</sub>", "29.28"))
    b.append(fig(19, F.FIGS[18], "vi"))
    b.append(p(
        "Nhiệt lượng q<sub>c</sub> do đối lưu tự nhiên và đối lưu cưỡng bức thường được biểu diễn "
        "qua hệ số truyền nhiệt h như sau:"))
    b.append(eq("q<sub>c</sub> = h A<sub>v</sub> (T<sub>e</sub> − T<sub>a</sub>)", "29.29"))
    b.append(p(
        "trong đó A<sub>v</sub> = πdL là diện tích bề mặt ngoài của cảm biến vận tốc. Công suất "
        "điện w thường được biểu diễn là:"))
    b.append(eq("w = E<sub>v</sub>² ⁄ R<sub>v</sub>", "29.30"))
    b.append(p(
        "trong đó E<sub>v</sub> là điện áp trên cảm biến và R<sub>v</sub> là điện trở của nó."))
    b.append(p(
        "Với cảm biến vận tốc công nghiệp trên Hình 29.17, q<sub>L</sub> là nhiệt dẫn từ đầu phần "
        "được nung nóng có chiều dài L ra phần còn lại của cảm biến. Phần lớn nhiệt này được chất "
        "lưu đang chảy mang đi bằng đối lưu, một phần nhỏ dẫn vào thân đầu dò. Với cảm biến dây nóng "
        "hoặc màng nóng hình trụ dùng trong nghiên cứu, q<sub>L</sub> dẫn vào hai chân, trong đó "
        "phần lớn được mang đi bằng đối lưu và phần nhỏ đi vào thân đầu dò. Ở các cảm biến vận tốc "
        "được thiết kế tốt, q<sub>L</sub> nhiều nhất bằng 10 % đến 15 % của w, và tỉ lệ này giảm khi "
        "vận tốc tăng."))
    b.append(p(
        "Với cảm biến vận tốc nghiên cứu, nhiệt độ bề mặt T<sub>e</sub> trùng với nhiệt độ dây hoặc "
        "màng T<sub>v</sub>. Tuy nhiên, nhiệt độ bề mặt T<sub>e</sub> của cảm biến vận tốc công "
        "nghiệp có vỏ bọc thép không gỉ thấp hơn một chút so với nhiệt độ T<sub>v</sub> của cuộn "
        "bạch kim, vì cần có một độ giảm nhiệt độ để dẫn nhiệt q<sub>c</sub> qua lớp “da” trung "
        "gian — lớp xi măng và ống thép không gỉ. Điều này được biểu diễn là:"))
    b.append(eq("T<sub>e</sub> = T<sub>v</sub> − q<sub>c</sub> R<sub>s</sub>", "29.31"))
    b.append(p(
        "trong đó R<sub>s</sub> là trở nhiệt của lớp da, đơn vị K W⁻¹. R<sub>s</sub> là hằng số với "
        "một cảm biến cho trước và bằng tổng các trở nhiệt của lớp xi măng và ống thép không gỉ. Với "
        "cảm biến vận tốc nghiên cứu, R<sub>s</sub> = 0 và T<sub>e</sub> = T<sub>v</sub> trong "
        "phương trình 29.31. Ở cảm biến vận tốc công nghiệp có vỏ bọc được thiết kế tốt, "
        "R<sub>s</sub> được giảm tới mức tối thiểu, khoảng 1 K W⁻¹. Như phương trình 29.31 cho thấy, "
        "ảnh hưởng của trở nhiệt lớp da tăng khi vận tốc (tức q<sub>c</sub>) tăng. Ở vận tốc thấp, "
        "ảnh hưởng gần như không đáng kể; nhưng ở vận tốc cao, nó chính là nguyên nhân gây ra độ "
        "cong đặc trưng ở phần cuối của đường cong hiệu chuẩn công suất theo vận tốc."))
    b.append(p(
        "Vì dòng bao quanh một hình trụ đặt ngang dòng bị chi phối bởi sự tách lớp biên và sự phóng "
        "xoáy, bài toán này không có nghiệm giải tích. Do đó hệ số màng h trong phương trình 29.29 "
        "được tìm bằng các tương quan thực nghiệm. Các tương quan cho h được biểu diễn qua các tham "
        "số không thứ nguyên sau:"))
    b.append(eq("Nu = ℑ(Re, Pr, Gr, M, Kn)", "29.32"))
    b.append(defs([
        ("Nu = hd ⁄ k", "Số Nusselt (tham số truyền nhiệt)"),
        ("Re = ρVd ⁄ μ", "Số Reynolds (tỉ số giữa lực động học và lực nhớt)"),
        ("Pr = μC<sub>p</sub> ⁄ k", "Số Prandtl (tham số tính chất chất lưu)"),
        ("M", "Số Mach (tham số nén được của khí)"),
        ("Kn", "Số Knudsen (tỉ số giữa quãng đường tự do trung bình của phân tử khí và d)"),
    ]))
    b.append(p(
        "Trong đó k là độ dẫn nhiệt của chất lưu, μ là độ nhớt và C<sub>p</sub> là nhiệt dung riêng "
        "ở áp suất không đổi. Nếu lấy trường hợp thực tế trong đó: (1) đối lưu tự nhiên đã được "
        "tính đến trong Re và Pr, (2) vận tốc nhỏ hơn một phần ba tốc độ âm của chất lưu (tức "
        "< 100 m s⁻¹ trong không khí môi trường), và (3) dòng không ở trong chân không cao, thì có "
        "thể bỏ qua ảnh hưởng của Gr, M và Kn một cách tương ứng. Khi đó:"))
    b.append(eq("Nu = ℑ(Re, Pr)", "29.33"))
    b.append(p(
        "Qua nhiều năm, đã có nhiều nỗ lực tìm các tương quan phổ dụng cho truyền nhiệt từ hình trụ "
        "đặt ngang dòng. Với chất lưu đẳng nhiệt ở áp suất không đổi, King [7] biểu diễn phương "
        "trình 29.33 thành:"))
    b.append(eq("Nu = A + B Re<sup>0,5</sup>", "29.34"))
    b.append(p(
        "trong đó A và B là các hằng số hiệu chuẩn thực nghiệm, khác nhau với mỗi chất lưu và mỗi "
        "nhiệt độ, áp suất. Kramers [8] đề nghị tương quan sau:"))
    b.append(eq("Nu = 0,42 Pr<sup>0,2</sup> + 0,57 Pr<sup>0,33</sup> Re<sup>0,50</sup>", "29.35"))
    b.append(p(
        "Tương quan này tính đến sự biến thiên của các tính chất chất lưu (k, μ và Pr) theo nhiệt "
        "độ. Kramers [8] đánh giá các tính chất này ở cái gọi là nhiệt độ “màng” "
        "(T<sub>v</sub> + T<sub>a</sub>)/2, chứ không phải ở T<sub>a</sub>. Một tương quan toàn diện "
        "khác được Churchill và Bernstein [9] đưa ra. Một số tương quan khác tương tự phương trình "
        "29.35 nhưng có số mũ của số Reynolds nằm trong khoảng 0,4 đến 0,6. Một số khác dùng 0,36 "
        "và 0,38 cho số mũ của số Prandtl. Các phương trình 29.34 và 29.35 chỉ thực sự đúng cho cảm "
        "biến dây nóng có tỉ số L/d rất lớn, khi đó q<sub>L</sub> và R<sub>s</sub> bằng không. Tương "
        "quan phổ dụng sau được đề nghị cho các cảm biến vận tốc thực tế có nhiệt độ chất lưu thay "
        "đổi và q<sub>L</sub>, R<sub>s</sub> khác không:"))
    b.append(eq("Nu = A + B Pr<sup>0,33</sup> Re<sup>n</sup>", "29.36"))
    b.append(p(
        "trong đó các hằng số A, B và n được xác định qua hiệu chuẩn lưu lượng. Phương trình 29.36 "
        "áp dụng được cho hầu hết cảm biến vận tốc thương mại, cả công nghiệp lẫn nghiên cứu."))
    b.append(p(
        "Kết hợp các phương trình 29.28, 29.29, 29.30 và 29.36, đồng thời nhận ra rằng h = kNu/d, "
        "ta được:"))
    b.append(eq("E<sub>v</sub>² ⁄ R<sub>v</sub> = (A k + B k Pr<sup>0,33</sup> Re<sup>n</sup>)"
                "(T<sub>e</sub> − T<sub>a</sub>)", "29.37"))
    b.append(p(
        "trong đó A và B là các hằng số mới. A, B và n được xác định qua hiệu chuẩn lưu lượng và "
        "tính đến mọi yếu tố không lý tưởng, kể cả dẫn nhiệt ở đầu và trở nhiệt lớp da. Phương "
        "trình 29.37 áp dụng được cho hầu hết cảm biến vận tốc thương mại, cả công nghiệp lẫn "
        "nghiên cứu. Các nhà sản xuất nhiệt kế gió công nghiệp có thể thêm các hằng số hiệu chuẩn "
        "khác vào phương trình 29.37 để tăng độ khớp với số liệu hiệu chuẩn lưu lượng."))
    b.append(p(
        "Sự có mặt của dẫn nhiệt ở đầu khiến nhiệt độ của cảm biến vận tốc thay đổi theo toạ độ "
        "trục y trên Hình 29.19. Nhiệt độ T mà cảm biến vận tốc thực sự cảm nhận là nhiệt độ trung "
        "bình trên chiều dài L, tức:"))
    b.append(eq("T<sub>v</sub> = (1 ⁄ L) ∫<sub>0</sub><sup>L</sup> T<sub>v</sub>(y) dy", "29.38"))
    b.append(p(
        "Bruun [1] trình bày một nghiệm giải tích cho T<sub>v</sub>(y) với cảm biến dây nóng. Phương "
        "trình 29.38 là biểu thức đúng cho T<sub>v</sub> trong phương trình 29.37 và được hiểu như "
        "vậy từ đây về sau."))
    b.append(p(
        "Với nhiệt độ chất lưu dưới 200 °C, điện trở của cảm biến vận tốc và cảm biến nhiệt độ kiểu "
        "RTD thường được biểu diễn là:"))
    b.append(eq("R<sub>v</sub> = R<sub>v0</sub> [1 + α<sub>v</sub> (T<sub>v</sub> − T<sub>0</sub>)]",
                "29.39"))
    b.append(eq("R<sub>T</sub> = R<sub>T0</sub> [1 + α<sub>T</sub> (T<sub>T</sub> − T<sub>0</sub>)]",
                "29.40"))
    b.append(p(
        "trong đó R<sub>v0</sub> và R<sub>T0</sub> lần lượt là điện trở của cảm biến vận tốc và cảm "
        "biến nhiệt độ ở nhiệt độ T<sub>0</sub> (thường là 0 °C hoặc 20 °C), còn α<sub>v</sub> và "
        "α<sub>T</sub> là các hệ số nhiệt độ của điện trở suất ở nhiệt độ T<sub>0</sub>. Người ta "
        "thêm các số hạng khác vào phương trình 29.39 và 29.40 khi nhiệt độ chất lưu vượt 200 °C. "
        "Khi đánh giá ở nhiệt độ chất lưu T<sub>a</sub>, điện trở R<sub>a</sub> của cảm biến vận "
        "tốc là:"))
    b.append(eq("R<sub>a</sub> = R<sub>v0</sub> [1 + α<sub>v</sub> (T<sub>a</sub> − T<sub>0</sub>)]",
                "29.41"))
    b.append(p(
        "Với các ứng dụng có nhiệt độ chất lưu dao động rộng, người ta thêm các số hạng khác vào "
        "phương trình 29.39–29.41. Ở 20 °C, α<sub>v</sub> và α<sub>T</sub> xấp xỉ 0,0036 °C⁻¹ với "
        "dây vonfram; 0,0038 °C⁻¹ với dây bạch kim nguyên chất; 0,0016 °C⁻¹ với dây 90 % bạch kim + "
        "10 % rhodi; 0,0024 °C⁻¹ với màng bạch kim; và 0,0040 °C⁻¹ với màng vonfram. R<sub>v</sub> "
        "và R<sub>a</sub> lần lượt được gọi là điện trở “nóng” và “nguội” của cảm biến vận tốc. Tỉ "
        "số R<sub>v</sub>/R<sub>a</sub> được gọi là <b>tỉ số quá nhiệt</b>. Với dòng khí, cảm biến "
        "vận tốc công nghiệp có vỏ bọc được vận hành ở tỉ số quá nhiệt từ 1,1 đến 1,4 "
        "(T<sub>v</sub> − T<sub>a</sub> = 30 °C đến 100 °C). Với dòng khí, tỉ số quá nhiệt của cảm "
        "biến dây nóng và màng nóng vonfram thường được đặt xấp xỉ 1,8 (T<sub>v</sub> − "
        "T<sub>a</sub> = 200 °C đến 300 °C) và 1,4 (T<sub>v</sub> − T<sub>a</sub> = 150 °C đến "
        "200 °C). Với dòng nước, tỉ số quá nhiệt của cảm biến màng nóng xấp xỉ 1,05 đến 1,10 "
        "(T<sub>v</sub> − T<sub>a</sub> = 10 °C đến 20 °C). Mikulla [6] cho thấy tầm quan trọng của "
        "ảnh hưởng của tỉ số quá nhiệt lên đáp ứng tần số."))
    b.append(p("Kết hợp các phương trình 29.39 và 29.41, ta được:"))
    b.append(eq("T<sub>v</sub> − T<sub>a</sub> = (R<sub>v</sub> − R<sub>a</sub>) ⁄ "
                "(α<sub>v</sub> R<sub>v0</sub>)", "29.42"))
    b.append(p("Thay biểu thức này vào phương trình 29.37, ta được:"))
    b.append(eq("E<sub>v</sub>² ⁄ [R<sub>v</sub> (R<sub>v</sub> − R<sub>a</sub>)] = A k + "
                "B k Pr<sup>0,33</sup> Re<sup>n</sup>", "29.43"))
    b.append(p(
        "trong đó các hằng số mới A và B đã hấp thụ các hằng số α<sub>v</sub> và R<sub>v0</sub>."))

    b.append(h5("Các bộ điều khiển điện tử và mạch cầu", "Electronic Drives and the Bridge Circuit"))
    b.append(p(
        "Các Hình 29.20 đến 29.22 trình bày ba bộ điều khiển điện tử điển hình cho cảm biến nhiệt "
        "kế gió. Hình 29.20 là mạch cầu Wheatstone của nhiệt kế gió nhiệt độ không đổi, loại được "
        "dùng phổ biến, do Takagi [10] mô tả. Hình 29.21 tương tự nhưng được điều khiển và vận hành "
        "qua một máy vi tính cá nhân. Ở chế độ nhiệt độ không đổi, điện trở nóng R<sub>v</sub> — và "
        "do đó nhiệt độ của cảm biến vận tốc — gần như không đổi, bất kể vận tốc thay đổi. Khi có "
        "thêm cảm biến nhiệt độ như trên Hình 29.20, mạch cầu cũng bù được sự thay đổi của nhiệt độ "
        "chất lưu T<sub>a</sub>, như sẽ trình bày sau. Một bộ điều khiển cảm biến tương tự khác "
        "thường gặp là nhiệt kế gió dòng không đổi. Ở chế độ này, một dòng điện không đổi được cho "
        "chạy qua cảm biến vận tốc và nhiệt độ của cảm biến giảm khi vận tốc tăng. Vì toàn bộ khối "
        "lượng của cảm biến phải tham gia vào sự thay đổi nhiệt độ này, cảm biến đáp ứng chậm hơn "
        "với thay đổi vận tốc. Vì nhiệt kế gió nhiệt độ không đổi có đáp ứng tần số phẳng hơn, tỉ "
        "số tín hiệu trên nhiễu xuất sắc [2] và dễ dùng hơn, nó được phần lớn các nhà nghiên cứu và "
        "nhà sản xuất ưa chuộng hơn nhiệt kế gió dòng không đổi cho các phép đo vận tốc và độ rối. "
        "Nhiệt kế gió dòng không đổi với tỉ số quá nhiệt rất thấp thường được dùng làm cảm biến "
        "nhiệt độ. Từ đây về sau, mọi đề cập tới điện tử của cảm biến sẽ dựa trên nhiệt kế gió "
        "nhiệt độ không đổi."))
    b.append(fig(20, F.FIGS[19], "vi"))
    b.append(p(
        "Trong bộ điều khiển nhiệt kế gió nhiệt độ không đổi trên Hình 29.20, các điện trở R₁ và R₂ "
        "được chọn để: (1) cực đại hoá dòng ở nhánh cảm biến vận tốc của cầu để nó tự nung nóng, và "
        "(2) cực tiểu hoá dòng ở nhánh cảm biến nhiệt độ của cầu để nó không tự nung nóng và độc "
        "lập với vận tốc. Ngoài ra, cảm biến nhiệt độ phải đủ lớn để tránh tự nung nóng. Tỉ số "
        "R₂/R₁ được gọi là <b>tỉ số cầu</b>. Tỉ số cầu thường dùng là 5:1 đến 20:1; nhưng để có đáp "
        "ứng tần số tối ưu và bù cho chiều dài cáp lớn, có thể dùng tỉ số cầu 1:1. Trên Hình 29.20, "
        "khuếch đại thuật toán trong một vòng điều khiển hồi tiếp cảm nhận điện áp sai lệch "
        "(e₂ − e₁) và đưa vào đỉnh cầu đúng lượng dòng cần thiết để (e₂ − e₁) tiến về không. Ở "
        "trạng thái đó, cầu cân bằng, nghĩa là:"))
    b.append(eq("R₁ ⁄ (R<sub>v</sub> + R₃) = R₂ ⁄ (R<sub>T</sub> + R₄)", "29.44"))
    b.append(p("hay"))
    b.append(eq("R<sub>v</sub> = (R₁ ⁄ R₂)(R<sub>T</sub> + R₄) − R₃", "29.45"))
    b.append(p(
        "Từ phương trình 29.45 có thể thấy R<sub>v</sub> là hàm tuyến tính của R<sub>T</sub>. Quan "
        "hệ này là cơ sở của phép bù nhiệt độ tương tự."))
    b.append(p(
        "Biểu diễn điện áp E<sub>v</sub> trên cảm biến vận tốc theo điện áp cầu E, ta được:"))
    b.append(eq("E<sub>v</sub> = E R<sub>v</sub> ⁄ (R₁ + R₃ + R<sub>v</sub>)", "29.46"))
    b.append(p(
        "Thay biểu thức này vào phương trình 29.43, ta đi tới biểu thức tổng quát của định luật thứ "
        "nhất của nhiệt động học cho cảm biến vận tốc của nhiệt kế gió:"))
    b.append(eq("E² = G [A k + B k (ρ<sub>s</sub> U<sub>s</sub> ⁄ μ)<sup>n</sup> "
                "Pr<sup>0,33</sup>]", "29.47"))
    b.append(p(
        "trong đó G = (R₁ + R₃ + R<sub>v</sub>)² (R<sub>v</sub> − R<sub>a</sub>) ⁄ R<sub>v</sub>, và "
        "A, B lại là các hằng số mới. Trong phương trình 29.47, có thể nhận ra rằng yêu cầu bảo "
        "toàn khối lượng đòi hỏi ρU = ρ<sub>s</sub>U<sub>s</sub>, trong đó ρ và U quy về nhiệt độ và "
        "áp suất thực của chất lưu, còn ρ<sub>s</sub> và U<sub>s</sub> quy về điều kiện chuẩn 0 °C "
        "hoặc 20 °C và 1 atm. Để viết phương trình 29.47 theo U, chỉ cần thay ρ<sub>s</sub> bằng ρ "
        "và U<sub>s</sub> bằng U."))
    b.append(fig(21, F.FIGS[20], "vi"))

    b.append(h4("Bù nhiệt độ", "Temperature Compensation"))
    b.append(p(
        "Mục đích của bù nhiệt độ là làm cho điện áp cầu E trong phương trình 29.47 độc lập với sự "
        "thay đổi của nhiệt độ chất lưu T<sub>a</sub>. Điều này đạt được nếu: (1) số hạng G trong "
        "phương trình 29.47 độc lập với T<sub>a</sub>, và (2) có bù cho sự thay đổi của các tính "
        "chất chất lưu (k, μ và Pr) theo T<sub>a</sub>. Vì các tính chất chất lưu này phụ thuộc "
        "nhiệt độ yếu hơn G trong phương trình 29.47, với những thay đổi nhiệt độ nhỏ (dưới ±10 °C) "
        "trong dòng khí, chỉ G cần được bù."))
    b.append(p(
        "Phương pháp hai nhiệt độ là một thủ tục điển hình để bù cho cả G lẫn các tính chất chất "
        "lưu. Trong phương pháp này, các điện trở cầu cố định R₁, R₂ và R₄ trên Hình 29.20 được "
        "chọn sao cho E giống nhau ở hai nhiệt độ khác nhau nhưng cùng lưu lượng khối. Thủ tục này "
        "được thực hiện trong quá trình hiệu chuẩn lưu lượng và có khác biệt giữa các nhà sản xuất."))
    b.append(p(
        "Phương pháp hai nhiệt độ bù thoả đáng cho những biến thiên nhiệt độ dưới khoảng ±50 °C. "
        "Trong các ứng dụng dòng khí nhiệt độ cao hơn, như dòng không khí cháy được gia nhiệt sơ bộ "
        "và khí ống khói, biến thiên nhiệt độ thường lớn hơn. Bộ điều khiển cảm biến số dùng vi xử "
        "lý trên Hình 29.22 bù được cho biến thiên nhiệt độ từ ±50 °C đến ±150 °C. Bộ điều khiển "
        "cảm biến này không có cầu tương tự. Thay vào đó nó có một cầu số ảo duy trì "
        "(T<sub>v</sub> − T<sub>a</sub>) không đổi trong phạm vi 0,1 °C và có các thuật toán tự "
        "động bù cho sự thay đổi nhiệt độ của k, μ và Pr. Với bộ điều khiển cảm biến số này, định "
        "luật thứ nhất của nhiệt động học được suy ra từ phương trình 29.37 là:"))
    b.append(eq("w = [A k + B k (ρ<sub>s</sub> U<sub>s</sub> ⁄ μ)<sup>n</sup> Pr<sup>0,33</sup>] ΔT",
                "29.48"))
    b.append(p(
        "trong đó ΔT = (T<sub>v</sub> − T<sub>a</sub>) nay là một hằng số đã biết."))
    b.append(fig(22, F.FIGS[21], "vi"))

    b.append(h4("Hiệu chuẩn lưu lượng", "Flow Calibration"))
    b.append(p(
        "Hình 29.23 trình bày một đường cong hiệu chuẩn lưu lượng điển hình cho bộ điện tử số trên "
        "Hình 29.22. Đường cong là phi tuyến, có dạng lôgarit. Tính phi tuyến này bất lợi vì đòi hỏi "
        "mạch tuyến tính hoá, nhưng có lợi vì nó cho dải đo tới 1000:1 với một cảm biến duy nhất. "
        "Ngoài ra, tín hiệu ra mức cao vài vôn cho độ lặp lại xuất sắc và không cần khuếch đại gì "
        "thêm ngoài khuếch đại để đặt dải. Vì các kích thước tới hạn của cảm biến nhiệt kế gió quá "
        "nhỏ, công nghệ chế tạo hiện nay không thể duy trì dung sai đủ nhỏ để bảo đảm tính tái lặp "
        "của cảm biến. Do đó mỗi nhiệt kế gió đều phải được hiệu chuẩn lưu lượng, ví dụ như trên "
        "Hình 29.23, trên toàn dải vận tốc của nó — hoặc ở đúng nhiệt độ chất lưu khi sử dụng, hoặc "
        "trên dải nhiệt độ mà nó sẽ gặp nếu cần bù nhiệt độ. Cần hiệu chuẩn vận tốc 10 đến 20 điểm "
        "để xác định chính xác các hằng số hiệu chuẩn A, B và n trong phương trình 29.47. Thường "
        "người ta áp dụng thủ tục khớp đường cong bình phương tối thiểu. Hiệu chuẩn lưu lượng đúng "
        "đòi hỏi hai yếu tố then chốt: (1) một cơ sở tạo dòng ổn định, tái lặp được, và (2) một "
        "chuẩn truyền vận tốc chính xác. Bruun [1] và Gibbings và cộng sự [4] cung cấp thêm hiểu "
        "biết về khớp đường cong."))
    b.append(fig(23, F.FIGS[22], "vi"))
    b.append(p(
        "Cơ sở tạo dòng có hai loại — hở và kín. Một cơ sở hở gồm: (1) một nguồn dòng như quạt, bơm, "
        "bồn chứa trên cao hoặc nguồn khí nén; (2) một đoạn làm êm dòng, như buồng lắng có bộ nắn "
        "thẳng dòng, lưới chắn hoặc phương tiện khác để giảm xoáy, độ rối hay các bất đồng đều "
        "khác của dòng; (3) một vòi phun để tăng tốc dòng và làm phẳng thêm, tức làm đều, prôfin "
        "vận tốc; (4) một đoạn thử hoặc tia tự do để đưa đầu dò nhiệt kế gió vào; và (5) phương "
        "tiện giữ và làm kín đầu dò nhiệt kế gió cùng chuẩn truyền vận tốc. Đoạn thử hoặc tia tự do "
        "phải có: prôfin vận tốc đều trong khoảng 0,5 % đến 1,0 % ở phần giữa; cường độ rối nhỏ "
        "hơn khoảng 0,5 %; và diện tích đủ lớn để diện tích hình chiếu của đầu dò vận tốc nhỏ hơn "
        "5 % đến 10 % diện tích mặt cắt. Các nhà sản xuất bộ hiệu chuẩn lưu lượng hở nhỏ thường xác "
        "định vận tốc dòng hiệu chuẩn bằng cách đo độ sụt áp qua vòi phun."))
    b.append(p(
        "Cơ sở tạo dòng kín, hay ống khí động, có các bộ phận như trên, nhưng đầu ra của đoạn thử "
        "được nối bằng hệ ống dẫn về đầu vào của quạt hoặc bơm để khối không khí bên trong cơ sở "
        "được bảo toàn. Cơ sở hở rẻ hơn ống khí động kín và gọn hơn nhiều, nên phù hợp cho hiệu "
        "chuẩn lưu lượng tại hiện trường. Nhưng một bộ hiệu chuẩn dòng khí hở trong phòng thí "
        "nghiệm dùng quạt làm nguồn dòng thực ra là kín, với vòng kín nằm trong phòng thí nghiệm. "
        "Với vận tốc khí dưới khoảng 5 m s⁻¹, các bộ hiệu chuẩn hở có thể bị trôi do áp suất, nhiệt "
        "độ hoặc điều kiện khác trong phòng thay đổi. Các ống khí động kín được thiết kế đúng tạo "
        "ra vận tốc khí chính xác và tái lặp được từ khoảng 0,5 m s⁻¹ đến 150 m s⁻¹. Khi được trang "
        "bị bộ làm lạnh nước, chúng loại bỏ nhiệt do nén và cho dòng khí nhiệt độ không đổi trong "
        "phạm vi ±2 °C. Khi được trang bị bộ gia nhiệt điện và cách nhiệt đúng, chúng cho nhiệt độ "
        "khí tới 300 °C. Gibbings [4] mô tả một giàn dịch chuyển bằng hộp nước để hiệu chuẩn lưu "
        "lượng ở vận tốc rất thấp, trong dải 0,1 m s⁻¹ đến 4 m s⁻¹."))
    b.append(p(
        "Ống Pitot và nhiệt kế gió Doppler laser là hai chuẩn truyền vận tốc thông dụng nhất dùng để "
        "hiệu chuẩn nhiệt kế gió. Cả hai đã được mô tả chi tiết ở phần trước của chương này. Ống "
        "Pitot thường có dạng chữ “L” cổ điển và đường kính ngoài khoảng 3 mm. Đầu của nó được đặt "
        "trong cùng mặt phẳng với đầu dò nhiệt kế gió trong đoạn thử nhưng không gần hơn khoảng "
        "3 cm. Thể tích hội tụ của nhiệt kế gió Doppler laser cũng được đặt tương tự. Ống Pitot rẻ "
        "hơn nhiều và dễ vận hành hơn, nhưng khó dùng nếu vận tốc khí nhỏ hơn khoảng 3 m s⁻¹. Một "
        "chuẩn truyền lưu lượng bằng ống Pitot đúng chuẩn phải được cấp lại chứng nhận hiệu chuẩn "
        "6 tháng một lần bởi một phòng thí nghiệm chuẩn được công nhận. Ngược lại, nhiệt kế gió "
        "Doppler laser là một chuẩn cơ bản, đo chính xác vận tốc khí từ khoảng 0,5 m s⁻¹ đến "
        "100 m s⁻¹. Vì cho phép đo không tiếp xúc, nó dùng được ở nhiệt độ cao. Nhược điểm chính là "
        "giá cao và những phức tạp liên quan tới việc gieo hạt đúng cách vào dòng."))

    b.append(h3("Các phép đo", "Measurements"))
    b.append(h4("Vận tốc điểm", "Point Velocity"))
    b.append(p(
        "Dựa trên định luật thứ nhất của nhiệt động học biểu diễn bằng phương trình 29.47, nay có "
        "thể giải tìm đại lượng mong muốn — hoặc vận tốc điểm thực U (m s⁻¹), hoặc vận tốc khối "
        "điểm U<sub>s</sub> (m chuẩn s⁻¹). Ở đây giả thiết vectơ vận tốc vuông góc với cảm biến dòng. "
        "Các phép đo vận tốc hai và ba chiều được bàn sau. Trong phần dưới, A, B và n là các hằng số "
        "nhưng khác nhau với mỗi trường hợp."))
    b.append(p(
        "Trường hợp đơn giản nhất là dòng đẳng nhiệt với cảm biến dây nóng có tỉ số chiều dài trên "
        "đường kính (L/d) rất lớn. Khi đó số mũ n trong phương trình 29.47 bằng 0,5, như phương "
        "trình 29.34 cho thấy. Định luật thứ nhất và biểu thức vận tốc áp dụng được là:"))
    b.append(eq("E² = A + B U<sup>0,5</sup>", "29.49"))
    b.append(p("và"))
    b.append(eq("U = [(E² − A) ⁄ B]²", "29.50"))
    b.append(p(
        "Với một cảm biến thực tế trong dòng đẳng nhiệt, chỉ có tổn thất ở đầu hoặc có cả tổn thất ở "
        "đầu lẫn trở nhiệt lớp da, ta được:"))
    b.append(eq("E² = A + B U<sup>n</sup>", "29.51"))
    b.append(p("và"))
    b.append(eq("U = [(E² − A) ⁄ B]<sup>1/n</sup>", "29.52"))
    b.append(p(
        "Phương trình 29.52 thường được thay bằng một đa thức dạng U = F(E²), trong đó F( ) là đa "
        "thức bậc bốn với các hệ số xác định từ số liệu hiệu chuẩn lưu lượng bằng phần mềm khớp "
        "đường cong bình phương tối thiểu. Với trường hợp như trên nhưng dòng không đẳng nhiệt, "
        "định luật thứ nhất được biểu diễn bằng phương trình 29.47, và vận tốc được biểu diễn là:"))
    b.append(eq("U<sub>s</sub> = (μ ⁄ ρ<sub>s</sub>) [(E² ⁄ G − A k) ⁄ (B k Pr<sup>0,33</sup>)]"
                "<sup>1/n</sup>", "29.53"))
    b.append(p(
        "Với bộ điều khiển cảm biến số trên Hình 29.22, định luật thứ nhất cho bởi phương trình "
        "29.48, và vận tốc bởi:"))
    b.append(eq("U<sub>s</sub> = (μ ⁄ ρ<sub>s</sub>) [(w ⁄ ΔT − A k) ⁄ (B k Pr<sup>0,33</sup>)]"
                "<sup>1/n</sup>", "29.54"))
    b.append(p(
        "Các hệ nhiệt kế gió công nghiệp thương mại hiện nay có điện tử bù nhiệt độ và “tuyến tính "
        "hoá” tự động tính U<sub>s</sub> như một hàm tuyến tính của E hoặc w, dựa trên các quan hệ "
        "trên."))

    b.append(h4("Độ rối", "Turbulence"))
    b.append(p(
        "Đo độ rối là ứng dụng phổ biến thứ hai của nhiệt kế gió nghiên cứu. Phép đo này đòi hỏi "
        "đáp ứng tần số cao của nhiệt kế gió nghiên cứu dây nóng và màng nóng làm việc ở chế độ "
        "nhiệt độ không đổi. Phần lớn các dòng chất lưu là chảy rối. Chỉ những dòng có số Reynolds "
        "rất thấp mới không rối, tức là chảy tầng. Dòng rối biến thiên theo thời gian và thường được "
        "tách thành phần trung bình theo thời gian và phần dao động như sau:"))
    b.append(eq("U(t) = Ū + u<br>V(t) = V̄ + v<br>W(t) = W̄ + w<br>"
                "T<sub>a</sub>(t) = T̄<sub>a</sub> + θ<br>E = Ē + e", "29.55"))
    b.append(p(
        "trong đó U(t), V(t), W(t) là các thành phần trực giao theo phương x, y và z, tương ứng, như "
        "trên Hình 29.18 với đầu dò dây nóng 3-D. T<sub>a</sub>(t) là nhiệt độ chất lưu và E(t) là "
        "điện áp cầu. Ū, V̄, W̄, T̄<sub>a</sub> và Ē là các phần trung bình theo thời gian, còn u(t), "
        "v(t), w(t), θ(t) và e(t) là các phần dao động phụ thuộc thời gian. Các phần trung bình theo "
        "thời gian được lấy trung bình trong khoảng đủ dài để không còn phụ thuộc vào dao động rối, "
        "nhưng vẫn đáp ứng được với sự thay đổi của dòng chính theo thời gian. Ở mục trước, các "
        "biểu thức đưa ra là cho vận tốc trung bình theo thời gian. Trong nghiên cứu độ rối, người "
        "ta chủ yếu quan tâm tới trung bình thời gian của tích hai thành phần vận tốc dao động (các "
        "tương quan rối), vì những số hạng này xuất hiện trong phương trình Navier–Stokes lấy trung "
        "bình theo thời gian. Hai tương quan rối quan trọng là <span style=\"text-decoration:"
        "overline\">u²</span> và <span style=\"text-decoration:overline\">uv</span>. Tương quan "
        "<span style=\"text-decoration:overline\">u²</span> chia cho Ū được gọi là <b>cường độ "
        "rối</b>. Các nhà sản xuất hệ nhiệt kế gió nghiên cứu cung cấp điện tử tự động tính các "
        "tương quan rối."))
    b.append(p(
        "Với một chất lưu có thay đổi nhiệt độ đủ nhỏ để các tính chất chất lưu coi như không đổi, "
        "có thể viết phương trình 29.47 dưới dạng sau:"))
    b.append(eq("E² = (A + B U<sup>n</sup>)(T<sub>v</sub> − T<sub>a</sub>)", "29.56"))
    b.append(p(
        "trong đó A, B và n là hằng số, và R<sub>v</sub> gần như không đổi vì nhiệt kế gió làm việc "
        "ở chế độ nhiệt độ không đổi. Elsner [11] chỉ ra rằng điện áp dao động e tìm được bằng cách "
        "lấy vi phân toàn phần phương trình 29.56, như sau:"))
    b.append(eq("e = S<sub>u</sub> u + S<sub>θ</sub> θ", "29.57"))
    b.append(p("trong đó"))
    b.append(eq("S<sub>u</sub> = ∂E ⁄ ∂U = (n B U<sup>n−1</sup> ⁄ 2) "
                "[(T<sub>v</sub> − T<sub>a</sub>) ⁄ (A + B U<sup>n</sup>)]<sup>1/2</sup>"
                " = độ nhạy vận tốc", "29.58"))
    b.append(eq("S<sub>θ</sub> = ∂E ⁄ ∂T<sub>a</sub> = −(1 ⁄ 2) "
                "[(A + B U<sup>n</sup>) ⁄ (T<sub>v</sub> − T<sub>a</sub>)]<sup>1/2</sup>"
                " = độ nhạy nhiệt độ", "29.59"))
    b.append(p(
        "Từ các phương trình 29.58 và 29.59 có thể thấy rằng tăng (T<sub>v</sub> − T<sub>a</sub>), "
        "tức vận hành cảm biến càng nóng càng tốt, sẽ cực đại hoá độ nhạy vận tốc và cực tiểu hoá "
        "độ nhạy với dao động nhiệt độ. Đây là lý do dây nóng vonfram được vận hành ở nhiệt độ cao "
        "(thường 200 °C đến 300 °C)."))
    b.append(p(
        "Các thành phần dao động của vận tốc có phổ tần số rộng, từ 10⁻² Hz đến 10⁵ Hz, và đôi khi "
        "còn cao hơn. Do đó, đáp ứng tần số của nhiệt kế gió nghiên cứu nhiệt độ không đổi nhất "
        "thiết phải phẳng, nghĩa là suy giảm biên độ và dịch pha ở tần số cao là tối thiểu. "
        "Blackwelder [12] và một số nhà nghiên cứu khác đã nghiên cứu đáp ứng tần số của nhiệt kế "
        "gió dây nóng. Với phép đo độ rối, Borgos [13] mô tả các hệ nhiệt kế gió nghiên cứu thương "
        "mại với những tính năng như: bộ lọc thông thấp để giảm nhiễu điện tử; một mạch con để xác "
        "định và đặt tỉ số quá nhiệt; một máy phát xung vuông để kiểm tra đáp ứng tần số; và hai "
        "hoặc nhiều nút điều chỉnh để tối ưu đáp ứng tần số với các dao động nhanh. Các hệ gần đây "
        "có điện tử bù suy giảm tần số. Khi dùng với cảm biến dây nóng đường kính 5 µm trong không "
        "khí, các hệ thương mại có thể đạt đáp ứng tần số gần phẳng và độ trễ pha rất nhỏ từ 0 Hz "
        "đến khoảng 10⁴ Hz. Như Nelson và Borgos [14] báo cáo, cảm biến màng nóng hình nêm và hình "
        "nón trong nước có đáp ứng tương đối phẳng từ 0 Hz đến 10 Hz với vận tốc trên 0,3 m s⁻¹."))
    b.append(p(
        "Các phép đo vận tốc và độ rối hai và ba thành phần được thực hiện bằng nhiệt kế gió nghiên "
        "cứu dây nóng hoặc màng nóng, như trên Hình 29.18. Như Müller [15] mô tả, đầu dò dây nóng "
        "hoặc màng nóng hình trụ ở cấu hình chữ “X” được dùng để đo các thành phần vận tốc U và V. "
        "Trong một dãy ba cảm biến trực giao, chúng đo U, V và W. Döbbeling, Lenze và Leuckel [16] "
        "cùng các nhà nghiên cứu khác đã phát triển các dãy bốn dây để đo U, V và W. Olin và Kiland "
        "[17] mô tả một dãy trực giao gồm ba cảm biến màng nóng hình trụ tách đôi. Mỗi cảm biến "
        "trong dãy này có hai màng nóng vận hành riêng, ngăn cách bởi hai khe dọc đối nhau 180° "
        "suốt chiều dài. Hai màng tách đôi tận dụng sự phân bố truyền nhiệt không đều quanh một "
        "hình trụ đặt ngang dòng."))
    b.append(p(
        "Trong các dãy nhiều cảm biến, vectơ vận tốc không nhất thiết vuông góc với cảm biến hình "
        "trụ. Nếu giới hạn thảo luận trong dòng đẳng nhiệt, định luật thứ nhất biểu diễn bằng phương "
        "trình 29.47 trở thành:"))
    b.append(eq("E² = A + B V<sub>e</sub><sup>n</sup>", "29.60"))
    b.append(p(
        "trong đó V<sub>e</sub> là vận tốc hiệu dụng mà một cảm biến hình trụ trong dãy cảm nhận "
        "được, còn A, B và n là các hằng số. Jörgenson [18] mô tả V<sub>e</sub> như sau:"))
    b.append(eq("V<sub>e</sub>² = U<sub>N</sub>² + a² U<sub>T</sub>² + b² U<sub>B</sub>²", "29.61"))
    b.append(defs([
        ("U<sub>N</sub>", "Thành phần vận tốc vuông góc với cảm biến"),
        ("U<sub>T</sub>", "Thành phần tiếp tuyến"),
        ("U<sub>B</sub>", "Thành phần vuông góc với cả cả U<sub>N</sub> và U<sub>T</sub> "
                          "(tức thành phần song pháp tuyến)"),
    ]))
    b.append(p(
        "Các hằng số a và b trong phương trình 29.61 lần lượt được gọi là hệ số lệch ngang và lệch "
        "dọc của cảm biến, và được xác định qua hiệu chuẩn lưu lượng. Giá trị điển hình của a và b "
        "với cảm biến dây nóng có mạ là 0,2 và 1,05. Thay phương trình 29.61 vào phương trình 29.60, "
        "ta được biểu thức sau cho tín hiệu ra của một cảm biến trong dãy:"))
    b.append(eq("E² = A + B (U<sub>N</sub>² + a² U<sub>T</sub>² + b² U<sub>B</sub>²)"
                "<sup>n/2</sup>", "29.62"))
    b.append(p(
        "Các biểu thức như trên, hoặc tương tự như Lekakis, Adrian và Jones [19] đưa ra, được viết "
        "cho mọi cảm biến trong dãy. Các biểu thức này cùng lượng giác sau đó được dùng để giải tìm "
        "các thành phần vận tốc U, V và W trong hệ quy chiếu cố định theo không gian x, y, z."))

    b.append(h4("Dòng trong kênh", "Channel Flows"))
    b.append(p(
        "Dựa trên quan hệ sau, một nhiệt kế gió công nghiệp kiểu cắm đo tại một điểm có thể theo "
        "dõi lưu lượng khối ṁ (kg s⁻¹) trong ống dẫn, đường ống, ống khói hay kênh dòng khác bằng "
        "cách đo vận tốc U<sub>s,c</sub> tại đường tâm của kênh:"))
    b.append(eq("ṁ = ρ<sub>s</sub> γ U<sub>s,c</sub> A<sub>c</sub>", "29.63"))
    b.append(p(
        "trong đó U<sub>s,c</sub> là thành phần vận tốc song song với trục kênh, đo tại đường tâm "
        "kênh và quy về điều kiện chuẩn 0 °C hoặc 20 °C và 1 atm; ρ<sub>s</sub>, một hằng số, là "
        "khối lượng riêng của chất lưu ở cùng điều kiện chuẩn; A<sub>c</sub>, một hằng số khác, là "
        "diện tích mặt cắt của kênh; và γ là một hằng số được định nghĩa là γ = "
        "U<sub>s,ave</sub>/U<sub>s,c</sub>, trong đó U<sub>s,ave</sub> là vận tốc trung bình trên "
        "diện tích A<sub>c</sub>. Vận tốc trong dòng kênh ít khi đều, và do đó γ không bằng một. Nếu "
        "kênh dòng có tỉ số chiều dài trên đường kính từ 40 đến 60 thì prôfin dòng của nó trở nên "
        "không đổi và được gọi là “phát triển đầy đủ”. Trong dòng phát triển đầy đủ, độ nhớt của "
        "chất lưu đã làm chậm vận tốc gần thành, và do đó γ luôn nhỏ hơn một. Nếu số Reynolds của "
        "kênh nhỏ hơn 2000, dòng là chảy tầng; prôfin phát triển đầy đủ là một parabol hoàn hảo; và "
        "γ bằng 0,5. Nếu số Reynolds lớn hơn 4000, dòng là chảy rối; prôfin phát triển đầy đủ có "
        "dạng parabol bẹt; và với ống có thành nhám điển hình, γ bằng 0,79; 0,83 và 0,83 ứng với số "
        "Reynolds 10⁴, 10⁵ và 10⁶. Nếu số Reynolds nằm giữa 2000 và 4000, dòng đang chuyển tiếp giữa "
        "chảy tầng và chảy rối, và γ nằm trong khoảng 0,5 đến 0,8."))
    b.append(p(
        "Đáng tiếc là trong phần lớn ống dẫn và ống khói lớn, không có đoạn thẳng dài 40 đến 60 "
        "đường kính trước vị trí theo dõi lưu lượng. Thay vào đó, prôfin dòng thường rất không đều, "
        "có xoáy, và trong các ống dẫn không khí sơ bộ cũng như trong ống khói còn bị làm phức tạp "
        "thêm bởi sự không đều của nhiệt độ. Trong những trường hợp này, theo dõi tại một điểm là "
        "không nên. May thay, theo dõi đa điểm bằng các dãy đo lưu lượng trung bình của nhiệt kế gió "
        "công nghiệp, như trên Hình 29.18, đã tỏ ra thành công trong những ứng dụng này. Như Olin "
        "[20] mô tả, phương pháp này gồm tổng cộng N cảm biến nhiệt kế gió công nghiệp (thường "
        "N = 4, 8 hoặc 12), mỗi cảm biến giống như trên Hình 29.17, đặt tại trọng tâm của một phần "
        "diện tích bằng nhau A<sub>c</sub>/N trong diện tích mặt cắt A<sub>c</sub> của kênh. Lưu "
        "lượng khối riêng ṁ<sub>i</sub> mà mỗi cảm biến theo dõi là ρ<sub>s</sub> "
        "U<sub>s,i</sub>(A<sub>c</sub>/N), trong đó U<sub>s,i</sub> là vận tốc riêng mà cảm biến "
        "theo dõi tại điểm i. Đại lượng mong muốn — tổng lưu lượng khối ṁ qua kênh — là tổng các "
        "lưu lượng khối riêng, tức:"))
    b.append(eq("ṁ = Σ<sub>i=1</sub><sup>N</sup> ṁ<sub>i</sub> = ρ<sub>s</sub> A<sub>c</sub> "
                "U<sub>s,ave</sub>", "29.64"))
    b.append(p(
        "trong đó U<sub>s,ave</sub> là trung bình cộng của N vận tốc riêng U<sub>s,i</sub>. Như Olin "
        "[21] mô tả, nhiệt kế gió nhiệt đa điểm công nghiệp được dùng làm bộ theo dõi lưu lượng "
        "trong các hệ giám sát phát thải liên tục của ống khói mà các cơ quan quản lý ô nhiễm không "
        "khí của chính phủ yêu cầu."))

    b.append(h3("Hệ thiết bị đo", "Instrumentation Systems"))
    b.append(p(
        "Bảng 29.3 liệt kê các ví dụ về hệ nhiệt kế gió thương mại điển hình. Bảng 29.4 liệt kê các "
        "nhà sản xuất chính của chúng. Hệ nhiệt kế gió gồm ba phần: cảm biến, đầu dò và điện tử. Cảm "
        "biến và đầu dò đã được mô tả ở các mục trước. Điện tử của các hệ công nghiệp được đặt trong "
        "vỏ chống nổ hoặc vỏ cấp công nghiệp khác, gắn trực tiếp trên đầu dò hoặc đặt xa (thường "
        "trong vòng 30 m). Điện tử được cấp nguồn bằng 24 V dc hoặc bằng điện lưới 100, 115 hay "
        "230 V xoay chiều. Tín hiệu ra điển hình là 0 đến 5 V dc, 4 đến 20 mA, RS232 hoặc RS485, tỉ "
        "lệ tuyến tính với vận tốc khối của khí U<sub>s</sub> trong dải 0,5 m chuẩn s⁻¹ đến "
        "150 m chuẩn s⁻¹. Các lưu lượng kế khối thẳng dòng có cùng các lựa chọn tín hiệu ra và được "
        "hiệu chuẩn trực tiếp theo lưu lượng khối ṁ (kg s⁻¹)."))
    _hd, _rows, _cap = _t293("vi")
    b.append(table(_hd, _rows, _cap, widths=("62%", "38%")))
    _hd, _rows, _cap = _t294("vi")
    b.append(table(_hd, _rows, _cap, widths=("50%", "50%")))
    b.append(p(
        "Các lưu lượng kế thẳng dòng nay có sẵn bộ ổn định dòng tích hợp để loại bỏ sai số do nhiễu "
        "động thượng lưu như khuỷu, van và chỗ mở rộng ống. Các hệ có thể dùng điện tử tương tự rẻ "
        "hơn hoặc điện tử thông minh dùng vi xử lý. Độ lặp lại của các hệ này là ±0,2 % toàn dải. Độ "
        "chính xác điển hình của một hệ công nghiệp thông minh là ±2 % giá trị đọc trong khoảng "
        "10 % đến 100 % toàn dải và ±0,5 % toàn dải dưới 10 % toàn dải. Bù nhiệt độ tự động cho hệ "
        "số nhiệt độ ±0,04 % giá trị đọc trên mỗi °C trong phạm vi ±20 °C quanh nhiệt độ hiệu chuẩn "
        "và ±0,08 % giá trị đọc trên mỗi °C trong phạm vi ±40 °C. Các ứng dụng nhiệt độ cao có bù "
        "nhiệt độ trên dải ±150 °C. Ảnh hưởng của áp suất là không đáng kể trong phạm vi ±300 kPa "
        "quanh áp suất hiệu chuẩn."))
    b.append(p(
        "Các hệ nhiệt kế gió nghiên cứu thường được nối với một máy vi tính cá nhân, như trên "
        "Hình 29.21. Máy tính cung cấp việc thiết lập và điều khiển hệ, cũng như hiển thị và phân "
        "tích số liệu. Các hệ hiện đại có mạch nhiễu thấp cùng công nghệ tối ưu hoá cầu thông minh "
        "loại bỏ việc chỉnh tay và tự động cho đáp ứng tần số phẳng tới 300.000 Hz. Các thiết bị rẻ "
        "hơn cho đáp ứng phẳng tới 10.000 Hz. Một mạch cặp nhiệt điện tích hợp giúp đơn giản hoá "
        "phép đo nhiệt độ. Phần mềm chạy trên Windows của máy tính cho hiển thị gần thời gian thực "
        "vận tốc, phân bố xác suất và cường độ rối. Xử lý sau cho thêm các thống kê khác, gồm: vận "
        "tốc trung bình; cường độ rối; độ lệch chuẩn; độ xiên; độ bẹt; ứng suất pháp cho đầu dò một, "
        "hai và ba thành phần; cũng như ứng suất tiếp, hệ số tương quan và góc phương dòng cho đầu "
        "dò hai và ba chiều. Ngoài ra có thể hiển thị phổ công suất, tự tương quan và tương quan "
        "chéo. Phần mềm tự động xử lý việc thiết lập hiệu chuẩn lưu lượng và tính vận tốc hiệu "
        "chuẩn. Hệ có các phiên bản 1, 2, 8 và 16 kênh."))
    b.append(p(
        "Các hệ nhiệt kế gió công nghiệp và nghiên cứu thương mại được giới thiệu lần đầu vào đầu "
        "những năm 1960. Ban đầu, nhiệt kế gió công nghiệp không được coi là đủ bền cho sự khắc "
        "nghiệt của môi trường công nghiệp. Với sự ra đời của cảm biến có vỏ bọc thép không gỉ và "
        "điện tử dùng vi xử lý, nhiệt kế gió công nghiệp nay có được uy tín mà trước đây chỉ dành "
        "cho các cách tiếp cận lưu lượng kế truyền thống. Các hệ nghiên cứu ban đầu đòi hỏi người "
        "dùng có hiểu biết cao và phải tham gia đáng kể vào việc vận hành. Ngược lại, các hệ nghiên "
        "cứu hiện nay có đáp ứng tần số gần phẳng, độ chính xác cao và các nút điều khiển dễ dùng, "
        "cho sự linh hoạt mà nhà nghiên cứu cần. Các hệ nghiên cứu dựa trên máy vi tính cá nhân có "
        "giao diện đồ hoạ, làm tăng cả hiệu năng lẫn sự đơn giản trong vận hành."))

    b.append(h3("Tài liệu tham khảo", "References"))
    b.append(wl(_refs292("vi")))
    b.append(h3("Đọc thêm", "Further Information"))
    b.append(wl([
        "J. A. Fay, <i>Introduction to Fluid Mechanics</i>, Cambridge, MA: MIT Press, 1994.",
        "A. Bejan, <i>Convection Heat Transfer</i>, New York: John Wiley &amp; Sons, 1995.",
    ]))
    return "".join(b)


# ================================================================ 29.1 VI

def sec_29_1_vi():
    b = []
    b.append(h2("29.1 Đo vận tốc bằng ống Pitot", "Pitot Probe Anemometry"))
    b.append(p("John A. Kleppe — Đại học Nevada."))

    b.append(p(
        "Ống Pitot là dụng cụ đo vận tốc điểm lâu đời nhất và vẫn là dụng cụ phổ biến nhất. "
        "Nguyên lý của nó chỉ gói trong một câu: làm dừng một dòng chất lưu một cách đoạn nhiệt "
        "rồi đo độ tăng áp suất do việc làm dừng ấy gây ra. Toàn bộ phần còn lại của mục này là "
        "những gì cần thêm vào câu đó để biến nó thành một phép đo dùng được — áp suất tĩnh lấy ở "
        "đâu, hình dạng đầu dò ảnh hưởng ra sao, khi nào phải kể tới tính nén được, và khi nào "
        "sóng xung kích làm hỏng cả nguyên lý."))

    b.append(h3("Cơ sở lý thuyết", "Theory"))
    b.append(p(
        "Ôn lại vắn tắt các nguyên lý động lực học chất lưu là việc có ích để hiểu lý thuyết và "
        "ứng dụng của ống Pitot. Xét một chất lưu khối lượng riêng không đổi chảy ổn định, không "
        "ma sát qua thiết bị đơn giản trên Hình 29.1. Nếu giả thiết không có nhiệt được thêm vào "
        "và không có công trục do chất lưu sinh ra, có thể lập một biểu thức đơn giản mô tả dòng "
        "chảy này:"))
    b.append(eq("p₁ ⁄ w + v₁² ⁄ (2g) + z₁ = p₂ ⁄ w + v₂² ⁄ (2g) + z₂", "29.1"))
    b.append(p("trong đó:"))
    b.append(defs([
        ("p₁, v₁, z₁", "Áp suất, vận tốc và độ cao tại lối vào"),
        ("p₂, v₂, z₂", "Áp suất, vận tốc và độ cao tại lối ra"),
        ("w", "<i>ρg</i> — trọng lượng riêng của chất lưu"),
        ("ρ", "Khối lượng riêng"),
        ("g", "9,80665 m s⁻²"),
    ]))
    b.append(p(
        "Phương trình 29.1 chính là phương trình Bernoulli quen thuộc. Ví dụ sau minh hoạ cách "
        "dùng phương trình 29.1 và mở đường cho phần lý thuyết ống Pitot."))
    b.append(fig(1, F.FIGS[0], "vi"))

    b.append(box("Ví dụ", [
        p("Một áp kế [2] được dùng để đo áp suất động của cụm ống trên Hình 29.2 [3]. Chất lưu "
          "trong áp kế là thuỷ ngân, khối lượng riêng 13.600 kg m⁻³. Với độ chênh cao đo được "
          "Δh = 2,5 cm, hãy tính lưu lượng trong ống nếu chất lưu chảy là (a) nước, (b) không khí. "
          "Bỏ qua mọi tổn thất, giả thiết không khí trong ống ở điều kiện STP và g = 9,81 m s⁻²."),
        h4("Lời giải"),
        p("Bắt đầu bằng cách viết biểu thức áp suất tại điểm 3:"),
        eq("p₃ = h₁ w + (h₃ − h₁) w<sub>Hg</sub> + p₁", "29.2"),
        p("và"),
        eq("p₃ = h₂ w + (h₃ − h₂) w<sub>Hg</sub> + p₂", "29.3"),
        p("Trừ hai phương trình này và sắp xếp lại, ta được biểu thức chênh áp:"),
        eq("p₂ − p₁ = Δh (w<sub>Hg</sub> − w)", "29.4"),
        p("trong đó w là trọng lượng riêng của nước hoặc không khí, tuỳ trường hợp."),
        p("Cũng từ phương trình 29.1, với z₁ = z₂ và v₂ = 0, có thể chứng minh rằng:"),
        eq("p₂ − p₁ = w v₁² ⁄ (2g)", "29.5"),
        p("(a) Với nước:"),
        eq("p₂ − p₁ = Δh (w<sub>Hg</sub> − w<sub>H₂O</sub>)<br>"
           "= 0,025 [13.600 (9,81) − 998 (9,81)]<br>= 3090,6 Pa", "29.6"),
        p("Suy ra:"),
        eq("3090,6 = (998)(9,81) v₁² ⁄ [2(9,81)]", "29.7"),
        p("hay"),
        eq("v₁ = 2,5 m s⁻¹", "29.8"),
        p("Lưu lượng Q khi đó tính được là:"),
        eq("Q = A₁ v₁ = π d₁² v₁ ⁄ 4 = π(0,076)²(2,5) ⁄ 4 = 0,011 m³ s⁻¹", "29.9"),
        p("(b) Với không khí, dùng đúng các bước trên có thể chứng minh:"),
        eq("Q = 0,34 m³ s⁻¹", "29.10"),
    ]))
    b.append(fig(2, F.FIGS[1], "vi"))

    b.append(p(
        "Một điểm trong dòng chất lưu mà tại đó vận tốc giảm về không được gọi là <b>điểm ứ</b> "
        "(stagnation point) [1]. Bất kỳ vật không quay nào đặt trong dòng cũng tạo ra một điểm "
        "ứ x, như trên Hình 29.3. Một áp kế nối tới điểm x sẽ ghi áp suất ứ của chất lưu."))
    b.append(fig(3, F.FIGS[2], "vi"))
    b.append(p(
        "Từ phương trình Bernoulli (29.1), đại lượng p + ½ρv² + ρgz là hằng số dọc theo một đường "
        "dòng trong dòng ổn định của chất lưu khối lượng riêng không đổi. Do đó, nếu vận tốc v tại "
        "một điểm nào đó bị đưa về không, áp suất tại điểm ấy tăng từ p lên p + ½ρv². Với chất lưu "
        "khối lượng riêng không đổi, đại lượng p + ½ρv² được gọi là <b>áp suất ứ</b> p₀ của đường "
        "dòng đó, còn số hạng ½ρv² — phần áp suất ứ do chuyển động mà có — được gọi là <b>áp suất "
        "động</b>. Một áp kế nối tới điểm x sẽ đo áp suất ứ; và nếu biết thêm áp suất tĩnh p thì "
        "có thể suy ra ½ρv². Có thể chứng minh:"))
    b.append(eq("p<sub>t</sub> = p + p<sub>v</sub>", "29.11"))
    b.append(defs([
        ("p<sub>t</sub>", "Áp suất toàn phần — tổng của áp suất tĩnh và áp suất động, cảm nhận được "
                          "bởi một đầu dò đứng yên so với biên của hệ khi nó làm ứ chất lưu tại chỗ "
                          "một cách đoạn nhiệt"),
        ("p", "Áp suất thực của chất lưu, dù đang chuyển động hay đứng yên; cảm nhận được bởi một "
              "đầu dò đứng yên so với chất lưu và không làm nhiễu chất lưu theo bất kỳ cách nào"),
        ("p<sub>v</sub>", "Áp suất động — tương đương áp suất của động năng có hướng của chất lưu"),
    ]))
    b.append(p("Dùng phương trình 29.11 có thể lập biểu thức liên hệ với vận tốc chất lưu:"))
    b.append(eq("p<sub>v</sub> = ½ ρ v²,  tức  p<sub>t</sub> = p + ½ ρ v²", "29.12"))
    b.append(p("hay, giải theo v:"))
    b.append(eq("v = √[2 (p<sub>t</sub> − p) ⁄ ρ]", "29.13"))

    b.append(p(
        "Xét ví dụ cụm ống trên Hình 29.4. Một ống vuông góc, đủ lớn để bỏ qua hiệu ứng mao dẫn, "
        "có một đầu A hướng vào dòng. Khi đạt cân bằng, chất lưu tại A đứng yên và áp suất trong "
        "ống vượt áp suất của dòng bao quanh một lượng ½ρv². Chất lỏng bị đẩy lên phần thẳng đứng "
        "của ống tới độ cao:"))
    b.append(eq("Δh = Δp ⁄ w = v² ⁄ (2g)", "29.14"))
    b.append(fig(4, F.FIGS[3], "vi"))
    b.append(p("Quan hệ này đã được dùng trong ví dụ trình bày ở trên để giải tìm v."))

    b.append(p(
        "Cần nhớ rằng áp suất toàn phần trong một chất lưu chỉ có thể cảm nhận được bằng cách làm "
        "dòng ứ lại <i>một cách đoạn nhiệt</i>, nghĩa là khi entropy của nó như nhau tại mọi điểm "
        "trong dòng. Việc làm ứ như vậy thực hiện được bằng ống Pitot, do Henri de Pitot phát "
        "triển lần đầu năm 1732 [4]. Để đo vận tốc trên sông Seine (Pháp), Pitot dùng hai ống "
        "nhúng trong nước. Hình 29.5 cho thấy phương pháp ống Pitot cơ bản của ông. Lỗ phía dưới "
        "của một trong hai ống được coi là phép đo áp suất tĩnh; độ dâng của chất lưu trong ống "
        "vuông góc 90° được dùng làm chỉ thị vận tốc dòng. Vì những lý do sẽ bàn sau, cách đo áp "
        "suất tĩnh của Pitot rất không đạt và ngày nay bị coi là sai [4]."))
    b.append(fig(5, F.FIGS[4], "vi"))

    b.append(p(
        "Một cụm ống Pitot-tĩnh hiện đại được trình bày trên Hình 29.6 [5]. Áp suất tĩnh được đo "
        "bằng các “lỗ tĩnh” hay điểm lấy áp trên thành. Điểm lấy áp thường có dạng một lỗ khoan "
        "trên thành ống dẫn và được giả định là cảm nhận được áp suất tĩnh “thực”. Khi chất lưu "
        "chuyển động ngang qua lỗ — thường là như vậy — lỗ sẽ không chỉ đúng áp suất tĩnh thực."))
    b.append(fig(6, F.FIGS[5], "vi"))
    b.append(p(
        "Các đường dòng bị lệch vào trong lỗ như trên Hình 29.7, tạo nên một hệ xoáy. Độ cong "
        "của đường dòng làm áp suất tại “miệng” lỗ khác với áp suất thực của chất lưu. Tổ hợp các "
        "yếu tố này cho áp suất tại miệng lỗ cao hơn áp suất thực — một <b>sai số dương</b>. Độ "
        "lớn của sai số này là hàm của số Reynolds tính theo vận tốc trượt và đường kính lỗ [5]. "
        "Lỗ có đường kính lớn hơn và vận tốc cao hơn cho sai số lớn hơn [5]. Ảnh hưởng của tính "
        "nén được lên sai số lỗ chưa được hiểu hay chứng minh đầy đủ, dù đã có những tương quan "
        "được đề xuất cho hiệu ứng này [5]. Có thể giảm sai số lỗ bằng cách dời vị trí lấy áp tới "
        "một nơi dòng không tăng tốc, hoặc dùng lỗ có đường kính nhỏ hơn. Ảnh hưởng của ba via "
        "cạnh lỗ cũng đáng lưu ý: phải mài sạch mọi ba via."))
    b.append(fig(7, F.FIGS[6], "vi"))
    b.append(p(
        "Còn một sai số nữa phát sinh theo góc tới của ống Pitot so với phương dòng. Hình 29.8 "
        "cho thấy sự biến thiên của chỉ thị áp suất toàn phần theo góc tới. Có thể thấy sai số "
        "nhỏ nếu góc tới nhỏ hơn ±10°."))
    b.append(fig(8, F.FIGS[7], "vi"))

    b.append(p(
        "Một biến thể được dùng rộng rãi của ống Pitot-tĩnh là cụm ống Pitot kiểu S trên "
        "Hình 29.9. Nó phải được thiết kế và chế tạo cẩn thận để bảo đảm đo đúng áp suất tĩnh. "
        "Ống “tĩnh” quay mặt về phía sau, vào vùng khuấy phía sau đầu dò, nơi áp suất thường hơi "
        "thấp hơn áp suất tĩnh không bị nhiễu. Vì vậy ống Pitot kiểu S cần áp dụng một hệ số hiệu "
        "chỉnh (thường trong khoảng 0,84). Hệ số hiệu chỉnh này chỉ đúng trong một dải vận tốc đo "
        "hạn chế. Bù lại, ống Pitot kiểu S có ưu điểm gọn và tương đối rẻ. Có thể quét ống Pitot "
        "kiểu S ngang một ống dẫn hay ống khói để xác định prôfin vận tốc và từ đó tính tổng lưu "
        "lượng thể tích; phần này bàn ở dưới."))
    b.append(fig(9, F.FIGS[8], "vi"))

    b.append(h3("Ống Pitot trong dòng có khối lượng riêng thay đổi",
                "The Pitot Tube in Flow with Variable Density"))
    b.append(p(
        "Khi dùng ống Pitot-tĩnh để xác định vận tốc của một chất lưu khối lượng riêng không đổi, "
        "không cần đo riêng áp suất ứ và áp suất tĩnh: chỉ cần đo hiệu của chúng là đủ. Tuy nhiên, "
        "một dòng khí vận tốc cao có thể thay đổi khối lượng riêng đáng kể khi bị làm dừng trước "
        "đầu ống Pitot-tĩnh; trong hoàn cảnh đó phải đo riêng áp suất ứ và áp suất tĩnh. Hơn nữa, "
        "nếu dòng ban đầu là trên âm thì một sóng xung kích hình thành trước ống, và do đó kết quả "
        "cho dòng trên âm khác về bản chất so với dòng dưới âm. Trước hết hãy xét ống Pitot-tĩnh "
        "trong dòng dưới âm đều, như trên Hình 29.10."))
    b.append(fig(10, F.FIGS[9], "vi"))
    b.append(p(
        "Quá trình chất lưu bị làm dừng tại mũi ống được giả thiết là không ma sát và đoạn nhiệt. "
        "Từ phương trình năng lượng cho khí lý tưởng, có thể chứng minh [1]:"))
    b.append(eq("v² = 2 C<sub>p</sub> (T₀ − T) = 2 C<sub>p</sub> T₀ {1 − (p ⁄ p₀)<sup>(γ−1)/γ</sup>}",
                "29.15"))
    b.append(defs([
        ("v", "Vận tốc"),
        ("C<sub>p</sub>", "Nhiệt dung riêng ở áp suất không đổi"),
        ("T", "Nhiệt độ tuyệt đối của khí"),
        ("T₀", "Nhiệt độ tuyệt đối tại điều kiện ứ"),
        ("p₀", "Áp suất toàn phần"),
        ("γ", "Tỉ số các nhiệt dung riêng"),
    ]))
    b.append(note(
        "<b>Ghi chú của người dịch.</b> Danh mục ký hiệu trong bản in gốc ghi “p = Áp suất toàn "
        "phần”, nhưng phương trình (29.15) dùng p₀ cho áp suất toàn phần và p cho áp suất tĩnh. "
        "Bản dịch giữ đúng ký hiệu trong phương trình và sửa lại danh mục cho khớp."))
    b.append(p(
        "Để đo T₀, người ta thường gắn vào dụng cụ một cặp nhiệt điện nhỏ đặt trong một vỏ bọc hở "
        "hai đầu. Nếu biết T₀ và tỉ số giữa áp suất tĩnh và áp suất ứ thì có thể xác định vận tốc "
        "của dòng từ phương trình 29.15."))

    b.append(p(
        "Ảnh hưởng của tính nén được được minh hoạ rõ nhất qua số Mach M. Có thể chứng minh [1]:"))
    b.append(eq("p₀ ⁄ p = [1 + ((γ − 1) ⁄ 2) M²]<sup>γ/(γ−1)</sup>", "29.16"))
    b.append(p(
        "Với dòng dưới âm, [(γ − 1)/2]M² < 1, nên vế phải của phương trình 29.16 có thể khai triển "
        "theo định lý nhị thức:"))
    b.append(eq("p₀ ⁄ p = 1 + (γ ⁄ 2) M² + (γ ⁄ 8) M⁴ + [γ(2 − γ) ⁄ 48] M⁶ + …", "29.17"))
    b.append(eq("p₀ − p = (ρ γ M² ⁄ 2) {1 + M² ⁄ 4 + [(2 − γ) ⁄ 24] M⁴ + …}", "29.18"))
    b.append(eq("= ½ ρ v² {1 + M² ⁄ 4 + [(2 − γ) ⁄ 24] M⁴ + …}", "29.19"))
    b.append(p(
        "Đại lượng trong dấu ngoặc là <b>hệ số nén được</b> và biểu thị ảnh hưởng của tính nén "
        "được. Bảng 29.1 cho thấy sự biến thiên của hệ số nén được theo M với không khí, γ = 1,4."))
    _hd, _rows, _cap = _t291("vi")
    b.append(table(_hd, _rows, _cap, widths=("22%", "28%", "22%", "28%")))
    b.append(p(
        "Có thể thấy rằng với M < 0,2, tính nén được ảnh hưởng tới chênh áp dưới 1 %, và khi đó "
        "công thức đơn giản cho dòng khối lượng riêng không đổi đủ chính xác. Với M lớn hơn, "
        "tuy nhiên, phải kể tới tính nén được."))

    b.append(p(
        "Với dòng trên âm, phương trình 29.16 không còn đúng, vì một sóng xung kích hình thành "
        "trước ống Pitot — như trên Hình 29.11 — nên chất lưu không được làm dừng một cách đoạn "
        "nhiệt. Mũi ống phải được tạo hình sao cho sóng xung kích tách rời, tức là nửa góc phải "
        "lớn hơn 45,6° [1]. Nếu trục ống song song với dòng tới, có thể coi sóng là pháp tuyến với "
        "đường dòng dẫn tới điểm ứ. Khi đó độ tăng áp qua sóng cho bởi:"))
    b.append(fig(11, F.FIGS[10], "vi"))
    b.append(eq("p₀ ⁄ p₁ = (1 + γ M₁²) ⁄ (1 + γ M₂²)", "29.20"))
    b.append(p(
        "Trong vùng dưới âm phía sau sóng, có một sự tăng áp dần dần theo kiểu đoạn nhiệt, biểu "
        "diễn được như sau:"))
    b.append(eq("p₀ ⁄ p₁ = (p₀ ⁄ p₂)(p₂ ⁄ p₁) = [1 + ((γ − 1) ⁄ 2) M₂²]<sup>γ/(γ−1)</sup>"
                " · (1 + γ M₁²) ⁄ (1 + γ M₂²)", "29.21"))
    b.append(p("Cuối cùng, ta được công thức Rayleigh:"))
    b.append(eq("p₀ ⁄ p₁ = {[(γ + 1)<sup>γ+1</sup> ⁄ (2γ M₁² − γ + 1)] · (M₁² ⁄ 2)<sup>γ</sup>}"
                "<sup>1/(γ−1)</sup>", "29.22"))
    b.append(p("Biểu thức này, với không khí, rút gọn thành:"))
    b.append(eq("p₀ ⁄ p₁ = 166,9 M₁⁷ ⁄ (7 M₁² − 1)<sup>2,5</sup>  khi γ = 1,4", "29.23"))

    b.append(p(
        "Tuy ống Pitot-tĩnh thông thường cho kết quả thoả đáng ở những số Mach đủ thấp để không "
        "hình thành sóng xung kích, nó không dùng được trong dòng trên âm: các “lỗ tĩnh” hay "
        "“điểm lấy áp” của nó nằm trong vùng phía sau sóng nên không ghi p₁; chúng cũng không ghi "
        "p₂, vì giá trị này chỉ có trên đường dòng trung tâm, ngay sau phần pháp tuyến của sóng "
        "xung kích. Do đó, tốt nhất là xác định p₁ một cách độc lập — ví dụ qua một lỗ trên thành "
        "ống, ở vị trí đủ xa về phía thượng lưu của sóng. Khi không thể đo p₁ độc lập, có thể "
        "dùng một ống Pitot-tĩnh đặc biệt, trong đó các lỗ tĩnh lùi về phía sau rất xa so với mũi "
        "(khoảng 10 lần đường kính ngoài của ống). Khi đó sóng xiên ở mỗi bên ống đã suy biến "
        "thành sóng Mach, mà qua đó độ tăng áp rất nhỏ."))
    b.append(p(
        "Khi M₁ = 1, độ tăng áp qua sóng là vô cùng nhỏ, nên cả phương trình 29.16 và 29.22 đều "
        "cho:"))
    b.append(eq("p₀ ⁄ p₁ = {(γ + 1) ⁄ 2}<sup>γ/(γ−1)</sup> = 1,893  (với không khí)", "29.24"))
    b.append(p(
        "Một giá trị p₀/p nhỏ chỉ ra dòng dưới âm; một giá trị lớn hơn chỉ ra dòng trên âm."))
    b.append(p(
        "Lưu ý rằng phương trình 29.22 cho phép tính số Mach thượng lưu từ tỉ số giữa áp suất ứ và "
        "áp suất tĩnh. Vì nhiệt độ ứ không đổi qua sóng xung kích:"))
    b.append(eq("C<sub>p</sub> T₀ = C<sub>p</sub> T₁ + v₁² ⁄ 2 = C<sub>p</sub> (v₁² ⁄ (γ R M₁²))"
                " + v₁² ⁄ 2", "29.25"))
    b.append(p("Như vậy cũng có thể tính v₁ nếu xác định được T₀."))

    b.append(h3("Đo lưu lượng thể tích", "Volumetric Flow Measurements"))
    b.append(p(
        "Phương pháp hiện được chấp nhận để đo lưu lượng thể tích khí trong ống dẫn và ống khói "
        "là dùng ống Pitot để lấy vận tốc tại các điểm có diện tích bằng nhau trên mặt cắt của "
        "ống khói [7]. Ví dụ, Hình 29.12 cho trường hợp ống khói tròn có diện tích mặt cắt A được "
        "chia thành mười hai (12) phần bằng nhau. Một ước lượng vận tốc lưu lượng trung bình được "
        "xác định theo quan hệ sau:"))
    b.append(eq("v̄<sub>n</sub> = Σ v<sub>n</sub> A<sub>n</sub> ⁄ A"
                " = A Σ v<sub>n</sub> ⁄ (N A<sub>i</sub>) = (1 ⁄ N) Σ v<sub>n</sub>", "29.26"))
    b.append(defs([
        ("A<sub>i</sub>", "Một trong các phần diện tích bằng nhau"),
        ("N", "Số phần diện tích bằng nhau"),
        ("v<sub>n</sub>", "Vận tốc đo tại từng điểm của phần diện tích bằng nhau"),
    ]))
    b.append(fig(12, F.FIGS[11], "vi"))
    b.append(p(
        "Quan hệ này cho thấy có thể ước lượng vận tốc lưu lượng trung bình bằng cách đo vận tốc "
        "tại từng điểm của các phần diện tích bằng nhau rồi lấy trung bình cộng của các số đo ấy. "
        "Rõ ràng sẽ thu được một kết quả khác nếu đơn giản là đo vận tốc tại các điểm cách đều "
        "nhau trên mặt phẳng đo rồi lấy trung bình cộng của các số đo: khi đó kết quả là vận tốc "
        "trung bình theo tuyến, v̄<sub>p</sub>, và sẽ mắc sai số."))
    b.append(p(
        "Vị trí lấy mẫu và số điểm quét được chỉ định sẽ ảnh hưởng tới chất lượng của phép đo lưu "
        "lượng thể tích. Tính chấp nhận được của quy trình lấy mẫu thường được xác định bằng "
        "khoảng cách từ các nhiễu động gần nhất ở thượng lưu và hạ lưu (vật cản hoặc chỗ đổi "
        "hướng) tới dòng khí. Các yêu cầu tối thiểu cho một quy trình lấy mẫu chấp nhận được có "
        "thể tìm trong tài liệu [7]. Một hệ tự động thực hiện phép đo này được trình bày trên "
        "Hình 29.13 [8]."))
    b.append(fig(13, F.FIGS[12], "vi"))

    b.append(h3("Một hệ lai", "A Hybrid System"))
    b.append(p(
        "Một hệ lai kết hợp công nghệ âm học (siêu âm) với công nghệ ống Pitot đã được phát triển "
        "để đo lưu lượng thể tích trong các ống dẫn và ống khói lớn [9–12]. Sơ đồ khối của hệ này "
        "được trình bày trên Hình 29.14. Các cảm biến (Hình 29.15) được gắn ở hai phía đối diện "
        "của ống khói hoặc ống dẫn, nghiêng một góc θ so với phương dòng. Phần âm học của cảm "
        "biến đo thời gian bay của sóng âm khi đi xuôi và khi đi ngược dòng khí. Có thể dễ dàng "
        "chứng minh [9] rằng bằng cách phát và thu sóng âm theo hai chiều ngược nhau, vận tốc "
        "trung bình theo tuyến của môi chất khí xác định được từ:"))
    b.append(fig(14, F.FIGS[13], "vi"))
    b.append(eq("v̄<sub>p</sub> = d ⁄ (2 cos θ) · [(τ₁ − τ₂) ⁄ (τ₁ τ₂)]  m s⁻¹", "29.27"))
    b.append(defs([
        ("v̄<sub>p</sub>", "Vận tốc trung bình theo tuyến của khí (m s⁻¹)"),
        ("d", "Khoảng cách giữa hai bộ thu phát (m)"),
        ("θ", "Góc, tính bằng độ, của tuyến nối hai đầu dò so với phương thẳng đứng"),
        ("τ₁", "Thời gian bay của sóng âm xuôi theo dòng khí (s)"),
        ("τ₂", "Thời gian bay của sóng âm ngược dòng khí (s)"),
    ]))
    b.append(note(
        "<b>Ghi chú của người dịch.</b> Bản in gốc định nghĩa θ là góc giữa tuyến truyền sóng và "
        "<i>phương thẳng đứng</i>, nhưng công thức (29.27) lại chia cho cos θ. Nếu θ tính từ phương "
        "thẳng đứng thì thành phần vận tốc dọc trục phải là d sin θ; công thức chỉ đúng khi θ là "
        "góc giữa tuyến sóng và <i>trục ống</i>. Giữ nguyên như đã in, vì Hình 29.14 cũng vẽ θ từ "
        "phương thẳng đứng, nhưng người dùng công thức cần lưu ý điểm này."))
    b.append(fig(15, F.FIGS[14], "vi"))
    b.append(p(
        "Kết quả của phần này trong toàn bộ phép đo là diện tích nằm dưới đường cong vận tốc trên "
        "Hình 29.16. Các ống Pitot cung cấp phép đo chênh áp tại hai điểm trong ống khói. Chênh áp "
        "được chuyển thành vận tốc theo một cách riêng. Thời gian bay của sóng âm, khi được kết "
        "hợp đúng với số đọc của cảm biến nhiệt độ, cho một phép đo khối lượng phân tử của khí "
        "thải ướt. Giá trị này sau đó được dùng để thu được các phép đo vận tốc điểm, ký hiệu V₂ "
        "và V₃ trên Hình 29.16. Đường cong prôfin dòng thực khi đó được ước lượng từ các giá trị "
        "V₁, V₂, V₃ và V₄ cùng diện tích dưới đường cong prôfin do phần âm học của hệ tạo ra. Phần "
        "cuối của phép đo dùng các số đo áp suất tĩnh và các số đo nhiệt độ ống khói để tính tổng "
        "lưu lượng thể tích chuẩn, tính bằng scfh (ướt)."))
    b.append(fig(16, F.FIGS[15], "vi"))

    b.append(h3("Tình trạng thương mại", "Commercial Availability"))
    b.append(p(
        "Có nhiều loại vật liệu được dùng để chế tạo ống Pitot, vì ống Pitot được dùng để đo rất "
        "nhiều loại chất lưu. Ví dụ, để dùng ống Pitot kiểu S trong ống khói của một nhà máy điện "
        "lớn có tháp rửa ướt, nơi môi trường cực kỳ khắc nghiệt và ăn mòn, phải dùng thép không gỉ "
        "316 hoặc C276 (Hastaloy®). Điều này, dĩ nhiên, làm cho giá ống Pitot đa dạng như chính "
        "ứng dụng của nó. Nhiều đầu dò ống Pitot kiểu S cơ bản được chế tạo bởi một vài công ty "
        "nhỏ, rồi các công ty này bán lại cho bên khác theo dạng OEM."))
    b.append(p(
        "Một cụm ống Pitot kiểu S điển hình, như cụm trên Hình 29.9, chế tạo bằng thép không gỉ "
        "316, có thể mua (với số lượng nhỏ) với giá 310 USD mỗi chiếc, từ:"))
    b.append(wl(["EEMC/EMRC", "3730 North Pellegrino Drive", "Tucson, AZ 85749",
                 "Điện thoại: (520) 749-2167", "Fax: (520) 749-3582"]))
    b.append(p(
        "Một cụm Pitot-tĩnh hiện đại điển hình, như cụm trên Hình 29.6, có thể mua (với số lượng "
        "nhỏ) với giá 34 USD, từ:"))
    b.append(wl(["Dwyer Instruments, Inc.", "P.O. Box 373", "Michigan City, IN 46361",
                 "Điện thoại: (219) 879-8000", "Fax: (219) 872-9057"]))
    b.append(p(
        "Các đầu dò Pitot-tĩnh phức tạp hơn, được thiết kế và chế tạo riêng để dùng trên máy bay, "
        "có thể mua từ:"))
    b.append(wl(["Rosemount Aerospace Inc.", "14300 Judicial Road",
                 "Burnsville, MN 55306-4898", "Điện thoại: (612) 892-4300",
                 "Fax: (612) 892-4430"]))
    b.append(p(
        "Bảng 29.2 liệt kê một số nhà sản xuất/nhà cung cấp bán ống Pitot và các thiết bị đo chênh "
        "áp nói chung."))
    _hd, _rows, _cap = _t292("vi")
    b.append(table(_hd, _rows, _cap, widths=("22%", "26%", "18%", "34%")))

    b.append(h3("Tài liệu tham khảo", "References"))
    # The reference numbers are carried in the strings, so this must be a
    # <br>-separated block rather than an <ol>: an ordered list would print
    # "1. 1. B. S. Massey". Chapter 28 does the same.
    b.append(wl(_refs291("vi")))
    return "".join(b)


# ================================================================ 29.1 EN

def sec_29_1_en():
    b = []
    b.append(h2("29.1 Pitot Probe Anemometry"))
    b.append(p("John A. Kleppe — University of Nevada."))

    b.append(p(
        "The Pitot tube is the oldest instrument for measuring point velocity and remains the most "
        "widely used. Its principle fits in one sentence: bring a flowing fluid to rest "
        "adiabatically and measure the rise in pressure that the arrest produces. Everything else "
        "in this section is what has to be added to that sentence to turn it into a usable "
        "measurement — where the static pressure is taken, how the shape of the probe matters, "
        "when compressibility must be accounted for, and when a shock wave destroys the principle "
        "altogether."))

    b.append(h3("Theory"))
    b.append(p(
        "It is instructive to review briefly the principles of fluid dynamics in order to understand "
        "Pitot tube theory and applications. Consider, for example, a constant-density fluid flowing "
        "steadily without friction through the simple device shown in Figure 29.1. If it is assumed "
        "that there is no heat being added and no shaft work being produced by the fluid, a simple "
        "expression can be developed to describe this flow:"))
    b.append(eq("p₁ ⁄ w + v₁² ⁄ (2g) + z₁ = p₂ ⁄ w + v₂² ⁄ (2g) + z₂", "29.1"))
    b.append(p("where"))
    b.append(defs([
        ("p₁, v₁, z₁", "Pressure, velocity and elevation at the inlet"),
        ("p₂, v₂, z₂", "Pressure, velocity and elevation at the outlet"),
        ("w", "<i>ρg</i>, the specific weight of the fluid"),
        ("ρ", "Density"),
        ("g", "9.80665 m s⁻²"),
    ]))
    b.append(p(
        "Equation 29.1 is the well-known Bernoulli equation. The following example demonstrates the "
        "use of Equation 29.1 and leads to a discussion of the theory of Pitot tubes."))
    b.append(fig(1, F.FIGS[0], "en"))

    b.append(box("Example", [
        p("A manometer [2] is used to measure the dynamic pressure of the tube assembly shown in "
          "Figure 29.2 [3]. The manometer fluid is mercury with a density of 13,600 kg m⁻³. For a "
          "measured elevation change, Δh, of 2.5 cm, calculate the flow rate in the tube if the "
          "flowing fluid is (a) water, (b) air. Neglect all losses and assume STP conditions for "
          "the air flowing in the tube and g = 9.81 m s⁻²."),
        h4("Solution"),
        p("Begin by writing expressions for the pressure at point 3:"),
        eq("p₃ = h₁ w + (h₃ − h₁) w<sub>Hg</sub> + p₁", "29.2"),
        p("and"),
        eq("p₃ = h₂ w + (h₃ − h₂) w<sub>Hg</sub> + p₂", "29.3"),
        p("Subtracting these equations and rearranging yields an expression for the pressure "
          "difference:"),
        eq("p₂ − p₁ = Δh (w<sub>Hg</sub> − w)", "29.4"),
        p("where w is the specific weight for water or air, as the case may be."),
        p("Also using Equation 29.1, one can show that for z₁ = z₂ and v₂ = 0:"),
        eq("p₂ − p₁ = w v₁² ⁄ (2g)", "29.5"),
        p("(a) For water:"),
        eq("p₂ − p₁ = Δh (w<sub>Hg</sub> − w<sub>H₂O</sub>)<br>"
           "= 0.025 [13,600 (9.81) − 998 (9.81)]<br>= 3090.6 Pa", "29.6"),
        p("Then:"),
        eq("3090.6 = (998)(9.81) v₁² ⁄ [2(9.81)]", "29.7"),
        p("or"),
        eq("v₁ = 2.5 m s⁻¹", "29.8"),
        p("The flow Q is then calculated to be:"),
        eq("Q = A₁ v₁ = π d₁² v₁ ⁄ 4 = π(0.076)²(2.5) ⁄ 4 = 0.011 m³ s⁻¹", "29.9"),
        p("(b) For air, one can use these same methods to show that:"),
        eq("Q = 0.34 m³ s⁻¹", "29.10"),
    ]))
    b.append(fig(2, F.FIGS[1], "en"))

    b.append(p(
        "A point in a fluid stream where the velocity is reduced to zero is known as a "
        "<b>stagnation point</b> [1]. Any nonrotating object placed in the fluid stream will "
        "produce a stagnation point, x, as seen in Figure 29.3. A manometer connected to point x "
        "would record the stagnation pressure of the fluid."))
    b.append(fig(3, F.FIGS[2], "en"))
    b.append(p(
        "From Bernoulli’s equation (Equation 29.1), the quantity p + ½ρv² + ρgz is constant along a "
        "streamline for the steady flow of a fluid of constant density. Consequently, if the "
        "velocity v at a particular point is brought to zero, the pressure there is increased from "
        "p to p + ½ρv². For a constant-density fluid, the quantity p + ½ρv² is known as the "
        "<b>stagnation pressure</b> p₀ of that streamline, while the term ½ρv² — that part of the "
        "stagnation pressure due to the motion — is termed the <b>dynamic pressure</b>. A manometer "
        "connected to point x would measure the stagnation pressure, and if the static pressure p "
        "were also known, then ½ρv² could be obtained. One can show that:"))
    b.append(eq("p<sub>t</sub> = p + p<sub>v</sub>", "29.11"))
    b.append(defs([
        ("p<sub>t</sub>", "Total pressure — the sum of the static and dynamic pressures, sensed by a "
                          "probe at rest with respect to the system boundaries when it locally "
                          "stagnates the fluid isentropically"),
        ("p", "The actual pressure of the fluid, whether in motion or at rest; sensed by a probe at "
              "rest with respect to the fluid that does not disturb the fluid in any way"),
        ("p<sub>v</sub>", "The dynamic, or velocity, pressure — the equivalent of the directed "
                          "kinetic energy of the fluid"),
    ]))
    b.append(p("Using Equation 29.11, one can develop an expression that relates to the velocity of "
               "the fluid:"))
    b.append(eq("p<sub>v</sub> = ½ ρ v²,  i.e.  p<sub>t</sub> = p + ½ ρ v²", "29.12"))
    b.append(p("or, solving for v:"))
    b.append(eq("v = √[2 (p<sub>t</sub> − p) ⁄ ρ]", "29.13"))

    b.append(p(
        "Consider as an example the tube arrangement shown in Figure 29.4. A right-angled tube, "
        "large enough to neglect capillary effects, has one end A facing the flow. When equilibrium "
        "is attained, the fluid at A is stationary and the pressure in the tube exceeds that of the "
        "surrounding stream by ½ρv². The liquid is forced up the vertical part of the tube to a "
        "height:"))
    b.append(eq("Δh = Δp ⁄ w = v² ⁄ (2g)", "29.14"))
    b.append(fig(4, F.FIGS[3], "en"))
    b.append(p("This relationship was used in the example given earlier to solve for v."))

    b.append(p(
        "It must be remembered that the total pressure in a fluid can be sensed only by stagnating "
        "the flow <i>isentropically</i>; that is, when its entropy is identical at all points in the "
        "flow. Such stagnation can be accomplished by a Pitot tube, as first developed by Henri de "
        "Pitot in 1732 [4]. In order to obtain a velocity measurement in the River Seine (in "
        "France), Pitot made use of two tubes immersed in water. Figure 29.5 shows his basic Pitot "
        "tube method. The lower opening in one of the tubes was taken to be a measurement of the "
        "static pressure. The rise of fluid in the 90° tube was used as an indication of the "
        "velocity of the flow. For reasons to be discussed later, Pitot’s method for measuring the "
        "static pressure was highly inadequate and would be considered incorrect today [4]."))
    b.append(fig(5, F.FIGS[4], "en"))

    b.append(p(
        "A modern-day Pitot-static tube assembly is shown in Figure 29.6 [5]. The static pressure is "
        "measured using “static holes” or pressure taps in the boundary. A pressure tap usually "
        "takes the form of a hole drilled in the side of a flow passage and is assumed to sense the "
        "“true” static pressure. When the fluid is moving past the tap, which is usually the case, "
        "the tap will not indicate the true static pressure."))
    b.append(fig(6, F.FIGS[5], "en"))
    b.append(p(
        "The streamlines are deflected into the holes as shown in Figure 29.7, setting up a system "
        "of eddies. The streamline curvature results in a pressure at the tap “mouth” different from "
        "the true fluid pressure. These factors in combination result in a higher pressure at the "
        "tap mouth than the true fluid pressure, a <b>positive pressure error</b>. The magnitude of "
        "this pressure error is a function of the Reynolds number based on the shear velocity and "
        "the tap diameter [5]. Larger tap diameters and high velocities give larger errors [5]. The "
        "effect of compressibility on tap errors is not well understood or demonstrated, although "
        "correlations for this effect have been suggested [5]. It is possible to reduce tap errors "
        "by moving the location of the tap to a nonaccelerating flow location, or by using pressure "
        "taps of smaller diameter. The effect of edge burrs is also noteworthy: all burrs must be "
        "removed."))
    b.append(fig(7, F.FIGS[6], "en"))
    b.append(p(
        "There is also an error that results with the angle of attack of the Pitot tube with the "
        "flow direction. Figure 29.8 shows the variation of total pressure indications as a function "
        "of the angle of attack. It can be seen that little error results if the angle of attack is "
        "less than ±10°."))
    b.append(fig(8, F.FIGS[7], "en"))

    b.append(p(
        "A widely used variation of the Pitot-static tube is the type S Pitot tube assembly shown in "
        "Figure 29.9. It must be carefully designed and fabricated to ensure that it will properly "
        "measure the static pressure. The “static” tube faces backwards into the wake behind the "
        "probe, where the pressure is usually somewhat lower than the undisturbed static pressure. "
        "The type S Pitot tube therefore requires the application of a correction factor (usually in "
        "the range of 0.84). This correction factor will be valid only over a limited range of "
        "velocity measurement. The type S Pitot tube does, however, have the advantage of being "
        "compact and relatively inexpensive. A type S Pitot tube can be traversed across a duct or "
        "stack to determine the velocity profile and hence the total volumetric flow; this is "
        "discussed later."))
    b.append(fig(9, F.FIGS[8], "en"))

    b.append(h3("The Pitot Tube in Flow with Variable Density"))
    b.append(p(
        "When a Pitot-static tube is used to determine the velocity of a constant-density fluid, the "
        "stagnation pressure and static pressure need not be separately measured: it is sufficient "
        "to measure their difference. A high-velocity gas stream, however, can undergo an "
        "appreciable change of density in being brought to rest at the front of the Pitot-static "
        "tube; under these circumstances, stagnation and static pressures must be separately "
        "measured. Moreover, if the flow is initially supersonic, a shock wave is formed ahead of "
        "the tube, and thus results for supersonic flow differ essentially from those for subsonic "
        "flow. Consider first the Pitot-static tube in uniform subsonic flow, as in Figure 29.10."))
    b.append(fig(10, F.FIGS[9], "en"))
    b.append(p(
        "The process by which the fluid is brought to rest at the nose of the tube is assumed to be "
        "frictionless and adiabatic. From the energy equation for a perfect gas, it can be shown "
        "that [1]:"))
    b.append(eq("v² = 2 C<sub>p</sub> (T₀ − T) = 2 C<sub>p</sub> T₀ {1 − (p ⁄ p₀)<sup>(γ−1)/γ</sup>}",
                "29.15"))
    b.append(defs([
        ("v", "Velocity"),
        ("C<sub>p</sub>", "Specific heat at constant pressure"),
        ("T", "Absolute temperature of the gas"),
        ("T₀", "Absolute temperature at stagnation conditions"),
        ("p₀", "Total pressure"),
        ("γ", "Ratio of specific heats"),
    ]))
    b.append(note(
        "<b>Translator’s note.</b> The source’s list of symbols defines “p = Total pressure”, but "
        "Equation 29.15 uses p₀ for the total pressure and p for the static pressure. The "
        "translation keeps the symbols as they appear in the equation and corrects the list to "
        "match."))
    b.append(p(
        "For measuring T₀, it is usual to incorporate in the instrument a small thermocouple "
        "surrounded by an open-ended jacket. If T₀ and the ratio of static to stagnation pressure "
        "are known, the velocity of the stream can then be determined from Equation 29.15."))

    b.append(p(
        "The influence of compressibility is best illustrated using the Mach number, M. It can be "
        "shown that [1]:"))
    b.append(eq("p₀ ⁄ p = [1 + ((γ − 1) ⁄ 2) M²]<sup>γ/(γ−1)</sup>", "29.16"))
    b.append(p(
        "For subsonic flow, [(γ − 1)/2]M² < 1 and so the right side of Equation 29.16 can be expanded "
        "by the binomial theorem to give:"))
    b.append(eq("p₀ ⁄ p = 1 + (γ ⁄ 2) M² + (γ ⁄ 8) M⁴ + [γ(2 − γ) ⁄ 48] M⁶ + …", "29.17"))
    b.append(eq("p₀ − p = (ρ γ M² ⁄ 2) {1 + M² ⁄ 4 + [(2 − γ) ⁄ 24] M⁴ + …}", "29.18"))
    b.append(eq("= ½ ρ v² {1 + M² ⁄ 4 + [(2 − γ) ⁄ 24] M⁴ + …}", "29.19"))
    b.append(p(
        "The bracketed quantity is the <b>compressibility factor</b> and represents the effect of "
        "compressibility. Table 29.1 indicates the variation of the compressibility factor with M "
        "for air with γ = 1.4."))
    _hd, _rows, _cap = _t291("en")
    b.append(table(_hd, _rows, _cap, widths=("22%", "28%", "22%", "28%")))
    b.append(p(
        "It is seen that for M < 0.2, compressibility affects the pressure difference by less than "
        "1 %, and the simple formula for flow at constant density is then sufficiently accurate. For "
        "larger values of M, however, compressibility must be taken into account."))

    b.append(p(
        "For supersonic flow, Equation 29.16 is not valid because a shock wave forms ahead of the "
        "Pitot tube, as shown in Figure 29.11, and thus the fluid is not brought to rest "
        "isentropically. The nose of the tube must be shaped so that the shock wave is detached, "
        "i.e. the semiangle must be greater than 45.6° [1]. If the axis of the tube is parallel to "
        "the oncoming flow, the wave can be assumed normal to the streamline leading to the "
        "stagnation point. The pressure rise across the shock can therefore be given by:"))
    b.append(fig(11, F.FIGS[10], "en"))
    b.append(eq("p₀ ⁄ p₁ = (1 + γ M₁²) ⁄ (1 + γ M₂²)", "29.20"))
    b.append(p(
        "In the subsonic region downstream of the shock, there is a gradual isentropic pressure rise "
        "that can be represented as:"))
    b.append(eq("p₀ ⁄ p₁ = (p₀ ⁄ p₂)(p₂ ⁄ p₁) = [1 + ((γ − 1) ⁄ 2) M₂²]<sup>γ/(γ−1)</sup>"
                " · (1 + γ M₁²) ⁄ (1 + γ M₂²)", "29.21"))
    b.append(p("Finally, one obtains Rayleigh’s formula:"))
    b.append(eq("p₀ ⁄ p₁ = {[(γ + 1)<sup>γ+1</sup> ⁄ (2γ M₁² − γ + 1)] · (M₁² ⁄ 2)<sup>γ</sup>}"
                "<sup>1/(γ−1)</sup>", "29.22"))
    b.append(p("This expression for air reduces to:"))
    b.append(eq("p₀ ⁄ p₁ = 166.9 M₁⁷ ⁄ (7 M₁² − 1)<sup>2.5</sup>  when γ = 1.4", "29.23"))

    b.append(p(
        "Although a conventional Pitot-static tube gives satisfactory results at Mach numbers low "
        "enough for no shock waves to form, it is unsuitable in supersonic flow because its “static "
        "holes” or “pressure taps”, being in the region downstream of the shock, do not then "
        "register p₁; nor do they register p₂, since this is found only on the central streamline, "
        "immediately behind the normal part of the shock wave. Consequently, p₁ is best determined "
        "independently — for example, through an orifice in a boundary wall well upstream of the "
        "shock. Where independent measurement of p₁ is not possible, a special Pitot-static tube can "
        "be used, in which the static holes are much further back (about 10 times the outside "
        "diameter of the tube) from the nose. The oblique shock wave on each side of the tube has by "
        "then degenerated into a Mach wave, across which the pressure rise is very small."))
    b.append(p(
        "When M₁ = 1, the pressure rise across the shock is infinitesimal and, thus, Equations 29.16 "
        "and 29.22 both give:"))
    b.append(eq("p₀ ⁄ p₁ = {(γ + 1) ⁄ 2}<sup>γ/(γ−1)</sup> = 1.893  (for air)", "29.24"))
    b.append(p("A small value of p₀/p therefore indicates subsonic flow, a larger value supersonic "
               "flow."))
    b.append(p(
        "Notice that Equation 29.22 enables the upstream Mach number to be calculated from the ratio "
        "of stagnation to static pressure. Since the stagnation temperature does not change across "
        "a shock wave:"))
    b.append(eq("C<sub>p</sub> T₀ = C<sub>p</sub> T₁ + v₁² ⁄ 2 = C<sub>p</sub> (v₁² ⁄ (γ R M₁²))"
                " + v₁² ⁄ 2", "29.25"))
    b.append(p("Thus, v₁ can also be calculated if T₀ is determined."))

    b.append(h3("Volumetric Flow Measurements"))
    b.append(p(
        "The currently accepted method for measuring volumetric gas flow in ducts and stacks "
        "involves the use of Pitot tubes to obtain the velocity at points of equal area of the "
        "cross-sectional areas of the stack [7]. For example, Figure 29.12 shows a case where the "
        "circular stack of cross-sectional area A has been divided into twelve (12) equal areas. An "
        "estimate of the average volumetric flow velocity is determined using the following "
        "relationship:"))
    b.append(eq("v̄<sub>n</sub> = Σ v<sub>n</sub> A<sub>n</sub> ⁄ A"
                " = A Σ v<sub>n</sub> ⁄ (N A<sub>i</sub>) = (1 ⁄ N) Σ v<sub>n</sub>", "29.26"))
    b.append(defs([
        ("A<sub>i</sub>", "One segment of the equal-area segments"),
        ("N", "Number of equal-area segments"),
        ("v<sub>n</sub>", "Velocity measured at each point of an equal-area segment"),
    ]))
    b.append(fig(12, F.FIGS[11], "en"))
    b.append(p(
        "This relationship shows that one can estimate the average volumetric flow velocity by "
        "taking velocity measurements at each point of equal area and then calculating the "
        "arithmetic mean of these measurements. It is clearly seen that a different result would be "
        "obtained if one were to simply take velocity measurements at equidistant points across the "
        "measurement plane and then take the arithmetic mean of these measurements. What would "
        "result in this case would be the path-averaged velocity, v̄<sub>p</sub>, which would be in "
        "error."))
    b.append(p(
        "The sampling site and the number of traverse points designated will affect the quality of "
        "the volumetric flow measurement. The acceptability of the sampling procedure is generally "
        "determined by the distances from the nearest upstream and downstream disturbances "
        "(obstruction or change in direction) to gas flow. The minimum requirements for an "
        "acceptable sampling procedure can be found in the literature [7]. An automated system for "
        "accomplishing this measurement is shown in Figure 29.13 [8]."))
    b.append(fig(13, F.FIGS[12], "en"))

    b.append(h3("A Hybrid System"))
    b.append(p(
        "A hybrid system that combines sonic (acoustic) and Pitot tube technology has been developed "
        "to measure volumetric flow in large ducts and stacks [9–12]. A block diagram of this system "
        "is shown in Figure 29.14. The sensors (Figure 29.15) are mounted on opposite sides of the "
        "stack or duct at an angle θ to the flow direction. The acoustic portion of the sensor "
        "measures the flight time of the sound waves with and against the gas flow. It can easily be "
        "shown [9] that by transmitting and receiving the sound waves in opposite directions, the "
        "path average velocity of the gaseous medium can be determined from:"))
    b.append(fig(14, F.FIGS[13], "en"))
    b.append(eq("v̄<sub>p</sub> = d ⁄ (2 cos θ) · [(τ₁ − τ₂) ⁄ (τ₁ τ₂)]  m s⁻¹", "29.27"))
    b.append(defs([
        ("v̄<sub>p</sub>", "Path average velocity of the gas (m s⁻¹)"),
        ("d", "Distance between the transceivers (m)"),
        ("θ", "Angle, in degrees, of the path of the transducers with the vertical"),
        ("τ₁", "Flight time of the sound with the gas flow (s)"),
        ("τ₂", "Flight time of the sound against the gas flow (s)"),
    ]))
    b.append(note(
        "<b>Translator’s note.</b> The source defines θ as the angle between the transducer path and "
        "the <i>vertical</i>, yet Equation 29.27 divides by cos θ. If θ were measured from the "
        "vertical the axial velocity component would be d sin θ; the formula is correct only when θ "
        "is the angle between the path and the <i>duct axis</i>. Left as printed — Figure 29.14 also "
        "draws θ from the vertical — but the user of the formula should be aware of the point."))
    b.append(fig(15, F.FIGS[14], "en"))
    b.append(p(
        "The result of this part of the total measurement is the area under the velocity curve "
        "plotted in Figure 29.16. The Pitot tubes provide differential pressure measurements at two "
        "points within the stack. The differential pressure is converted to velocity in a unique "
        "manner. The flight times of the acoustic wave, when properly combined with the temperature "
        "sensor reading, provide a measurement of the molecular weight of the wet flue gas. This "
        "value is then used to obtain the point velocity measurements shown as V₂ and V₃ in "
        "Figure 29.16. The actual flow profile curve is then estimated using the values V₁, V₂, V₃ "
        "and V₄ and the area under the flow profile curve generated by the acoustic portion of the "
        "system. The final part of the measurement involves using the static pressure measurements "
        "and the stack temperature measurements to calculate the total standard volumetric flow in "
        "scfh (wet)."))
    b.append(fig(16, F.FIGS[15], "en"))

    b.append(h3("Commercial Availability"))
    b.append(p(
        "There are a variety of materials used to construct Pitot tubes. The reasons for this are "
        "that Pitot tubes are used to measure a wide range of fluids. For example, to use a type S "
        "Pitot tube in a large power plant stack with a wet scrubber where the environment is "
        "extremely hostile and corrosive, stainless steel 316 or C276 (Hastaloy®) must be used. "
        "This, of course, makes the price of the Pitot tube as varied as its application. Many of "
        "the basic type S Pitot tube probes themselves are manufactured by a few small companies "
        "who, in turn, supply them on an OEM basis to others."))
    b.append(p(
        "A typical type S Pitot tube assembly, such as that shown in Figure 29.9, constructed using "
        "stainless steel 316 can be purchased (in small quantities) for $310 each. They are "
        "available from:"))
    b.append(wl(["EEMC/EMRC", "3730 North Pellegrino Drive", "Tucson, AZ 85749",
                 "Tel: (520) 749-2167", "Fax: (520) 749-3582"]))
    b.append(p(
        "A typical modern Pitot-static assembly, such as that shown in Figure 29.6, can be "
        "purchased (in small quantities) for $34 and is available from:"))
    b.append(wl(["Dwyer Instruments, Inc.", "P.O. Box 373", "Michigan City, IN 46361",
                 "Tel: (219) 879-8000", "Fax: (219) 872-9057"]))
    b.append(p(
        "More complex, custom-designed and fabricated Pitot-static probes for use on aircraft are "
        "available from:"))
    b.append(wl(["Rosemount Aerospace Inc.", "14300 Judicial Road",
                 "Burnsville, MN 55306-4898", "Tel: (612) 892-4300", "Fax: (612) 892-4430"]))
    b.append(p(
        "Table 29.2 lists a number of manufacturers and vendors that sell Pitot tube and general "
        "differential pressure measurement instrumentation."))
    _hd, _rows, _cap = _t292("en")
    b.append(table(_hd, _rows, _cap, widths=("22%", "26%", "18%", "34%")))

    b.append(h3("References"))
    b.append(wl(_refs291("en")))
    return "".join(b)


# ================================================================ 29.2 EN

def sec_29_2_en():
    b = []
    b.append(h2("29.2 Thermal Anemometry"))
    b.append(p("John G. Olin — Sierra Instruments, Inc."))

    b.append(h3("General Description"))
    b.append(p(
        "A thermal anemometer measures the velocity at a point in a flowing fluid — a liquid or a "
        "gas. Figure 29.17 shows a typical industrial thermal anemometer used to monitor velocity in "
        "gas flows. It has two sensors — a velocity sensor and a temperature sensor — that "
        "automatically correct for changes in gas temperature."))
    b.append(fig(17, F.FIGS[16], "en"))
    b.append(p(
        "Both sensors are reference-grade platinum resistance temperature detectors (RTDs). The "
        "electric resistance of RTDs increases as temperature increases. For this reason, they are "
        "one of the most commonly used sensors for accurate temperature measurements. The "
        "electronics circuit passes current through the velocity sensor, thereby heating it to a "
        "constant temperature differential (T<sub>v</sub> − T<sub>a</sub>) above the gas temperature "
        "T<sub>a</sub>, and measures the heat q<sub>c</sub> carried away by the cooler gas as it flows "
        "past the sensor. Hence, it is called a “constant-temperature thermal anemometer.”"))
    b.append(p(
        "Because the heat is carried away by the gas molecules, the heated sensor directly measures "
        "gas <b>mass velocity</b> (mass flow rate per unit area) ρU. The mass velocity is typically "
        "expressed as U<sub>s</sub> in engineering units of normal metres per second, or normal "
        "m s⁻¹, referenced to normal conditions of 0 °C or 20 °C temperature and 1 atm pressure. If "
        "the fluid’s temperature and pressure are constant, then the anemometer’s measurement can be "
        "expressed as actual metres per second, or m s⁻¹. When the mass velocity is multiplied by "
        "the cross-sectional area of a flow channel, the mass flow rate through the channel is "
        "obtained. Mass flow rate, rather than volumetric flow rate, is the direct quantity of "
        "interest in most practical and industrial applications, such as any chemical reaction, "
        "combustion, heating, cooling, drying, mixing, fluid power, human respiration, meteorology, "
        "and natural convection."))
    b.append(p(
        "The thermal anemometer is often called an <b>immersible thermal mass flowmeter</b> because "
        "it is immersed in the flow stream, in contrast to the capillary-tube thermal mass "
        "flowmeter, another thermal methodology commonly configured as an in-line mass flowmeter for "
        "low gas flows. The thermal anemometer has some advantages and disadvantages when compared "
        "with the two other common point-velocity instruments — Pitot tubes and laser Doppler "
        "anemometers. Compared with Pitot tubes, the thermal anemometer measures lower velocities, "
        "has much wider rangeability, and can be made smaller, but it generally has a higher cost "
        "and is not recommended for nonresearch liquid flows. When thermal anemometers are compared "
        "with laser Doppler anemometers, they have a much lower cost, do not require seeding the "
        "flow with particles, can have a faster time response, can be made to have better spatial "
        "resolution, and can have a higher signal-to-noise ratio. On the other hand, in "
        "nonfluctuating flows, laser Doppler anemometers provide a fundamental measurement of "
        "velocity, independent of temperature and fluid properties. For this reason, they are often "
        "used to calibrate thermal anemometers."))
    b.append(p(
        "Thermal anemometers are subdivided into two categories: industrial and research. "
        "Figure 29.18 shows typical sensors of industrial and research thermal anemometers."))
    b.append(fig(18, F.FIGS[17], "en"))

    b.append(h4("Industrial Thermal Anemometers"))
    b.append(p(
        "Industrial thermal anemometers measure the point velocity or point mass velocity of gases in "
        "most practical and industrial applications. They seldom are used to monitor liquid flows "
        "because avoidance of cavitation problems limits the temperature T<sub>v</sub> of the "
        "velocity sensor to only 10 °C to 20 °C above the liquid temperature, resulting in reduced "
        "velocity sensitivity and increased dependence on small changes in liquid temperature. "
        "Additionally, industrial liquid flows can cause sensor contamination and fouling."))
    b.append(p(
        "Typical gases monitored by industrial thermal anemometers include air, nitrogen, oxygen, "
        "carbon dioxide, methane, natural gas, propane, hydrogen, argon, helium, and stack gases. "
        "Common applications are: combustion air; preheated air; fuel gas; stack gas; natural gas "
        "distribution; semiconductor manufacturing gas distribution; heating, ventilation, and air "
        "conditioning; multipoint traversals of large ducts and stacks; drying; aeration and digester "
        "gas; occupational safety and health monitoring; environmental, natural convection, and "
        "solar studies; fermentors; and human inhalation monitoring. Industrial thermal anemometers "
        "have become the most commonly used instrument for monitoring the point velocity of gases."))
    b.append(p(
        "The velocity sensor of an industrial thermal anemometer is a reference-grade platinum wire "
        "(approximately 25 µm in diameter and 20 Ω in resistance) wound around a cylindrical ceramic "
        "mandrel, such as alumina. Alternatively, the sensor is a thin platinum film deposited on a "
        "glass or ceramic substrate. To withstand the harsh environment encountered in many "
        "industrial applications, the cylindrical platinum RTD is tightly cemented into the tip of a "
        "thin-walled, stainless-steel, Hastelloy, or Inconel tube (typically 3 mm outside diameter "
        "and 2 cm to 6 cm long). Because the gas temperature usually varies in industrial "
        "applications, industrial thermal anemometer probes almost always have a separate, but "
        "integrally mounted, unheated platinum RTD sensor for measuring the local gas temperature "
        "T<sub>a</sub>. When operated in the constant-temperature anemometer mode, the temperature "
        "difference (T<sub>v</sub> − T<sub>a</sub>) is usually in the 30 °C to 100 °C range. The "
        "temperature sensor is constructed just like the velocity sensor, but has a resistance in the "
        "300 Ω to 1000 Ω range. As shown in Figure 29.17, the dual-sensor probe has the velocity and "
        "temperature sensor mounted side-by-side on a cylindrical probe stem (usually 6 mm to 25 mm "
        "in diameter and 0.1 m to 3 m long). A shield usually is provided to prevent breakage of the "
        "sensing head. The spatial resolution of this industrial thermal anemometer is 1 cm to 2 cm. "
        "The electronics for the industrial thermal anemometer is usually mounted directly on the "
        "probe stem in an explosion-proof housing. Industrial thermal anemometer systems like this "
        "measure gas velocity over the range of 0.5 normal m s⁻¹ to 150 normal m s⁻¹."))
    b.append(p(
        "In use, the industrial thermal anemometer probe is inserted through a sealed compression "
        "fitting or flanged stub in the wall of a duct, pipe, stack, or other flow passage. In this "
        "case, it is usually called an <b>insertion thermal mass flowmeter</b>. In another common "
        "configuration, the dual-sensor probe is permanently fitted into a pipe or tube (typically "
        "8 mm to 300 mm in diameter) with either threaded or flanged gas connections. This "
        "configuration is called an <b>in-line thermal mass flowmeter</b>. In-line meters are directly "
        "calibrated for the total gas mass flow rate flowing through the pipe. The several flow body "
        "sizes facilitate mass flow monitoring over the range of 10 mg s⁻¹ to 10 kg s⁻¹."))

    b.append(h4("Research Thermal Anemometers"))
    b.append(p(
        "Research thermal anemometers measure the point velocity and/or turbulence of clean gases and "
        "liquids in research, product development, and laboratory applications. Because of their more "
        "fragile nature, they are not used for industrial applications. Typically, the gas is ambient "
        "air. Constant-temperature, filtered, degasified water is the primary liquid application, but "
        "the technique has also been applied to clean hydrocarbon liquids. As shown in Figure 29.18, "
        "the research anemometer’s velocity sensor is either a hot wire or a hot film. Hot-wire "
        "sensors have a high frequency response and, therefore, are excellent for turbulence "
        "measurements in air and other gases. They are seldom used in liquid flows because they are "
        "susceptible to fouling and contamination. Hot-film sensors trade off lower frequency "
        "response for increased ruggedness and are used in gas and liquid flows. For liquid flows, "
        "hot-film sensors are designed to shed lint and other fouling or contaminating materials. "
        "Bruun [1] is an excellent reference source for the theory and applications of hot-wire and "
        "hot-film anemometers. Another comprehensive source is Fingerson and Freymuth [2]."))
    b.append(p(
        "Typical applications for hot-wire and hot-film anemometers include: one-, two-, and "
        "three-dimensional flow and turbulence studies; validation of computational fluid dynamics "
        "codes; environmental and micrometeorological measurements; turbomachinery; internal "
        "combustion engines; biological studies; heat-transfer research; boundary-layer measurements; "
        "supersonic flows; two-phase flows; and vorticity measurements. Freymuth [3] describes the "
        "80-year history of research thermal anemometers. Today, hot-wire and hot-film anemometers "
        "have become the most widely used instruments for fluid mechanics research and development "
        "studies."))
    b.append(p(
        "The typical hot-wire sensor is a fine tungsten wire welded at each end to miniature prongs "
        "designed to minimize their influence on the wire’s flow field. The wire is usually gold or "
        "copper plated a short length at each end to define an active sensor length away from the two "
        "prongs. For work in water, the wire is quartz coated to prevent electrolysis or electrical "
        "shorting, but, in this case, cracking of the coating can occur. A typical tungsten wire has a "
        "diameter of 4 µm to 5 µm, an active length of 1 mm to 3 mm, and an electrical resistance of "
        "2 Ω to 6 Ω. Because it oxidizes above 350 °C in air, tungsten hot wires are usually operated "
        "at a temperature not exceeding 300 °C. Platinum, 90 % platinum + 10 % rhodium, and 80 % "
        "platinum + 20 % iridium wires also are used. They can be soldered onto the prongs, but are "
        "weaker than tungsten. In cases where the fluid temperature T<sub>a</sub> changes enough to "
        "cause measurement errors, a separate sensor is used to measure T<sub>a</sub> and make "
        "temperature corrections. The temperature sensor is either a hot wire or a larger wire-wound "
        "RTD mounted either on a separate probe or integrally on the same probe stem as the velocity "
        "sensor. As shown in Figure 29.18, for two-dimensional or three-dimensional flow studies, "
        "probes with two perpendicular wires in an “X” pattern or three orthogonal wires are used, "
        "respectively. Special subminiature probes and probes with the prongs displaced from the probe "
        "stem are used for near-wall, boundary-layer work and small flow passages. Gibbings et al. "
        "[4, 5] describe hot-wire probes for use in near-wall, turbulent boundary-layer studies."))
    b.append(p(
        "As shown in Figure 29.18, the typical hot-film sensor is a wedge-tipped or cone-tipped "
        "quartz rod with a thin 0.1 µm thick platinum film plated on its tip via cathode sputtering. "
        "The platinum film usually is coated with a 1 µm to 2 µm layer of quartz for protection and "
        "to avoid electrical shorting or electrolysis in water flows. Because hot-film sensors have a "
        "much larger mass than hot-wire sensors, their frequency response is not as flat as hot "
        "wires; hence, they are not quite as good for high frequency turbulence measurements. It also "
        "has been observed by Mikulla [6] that the shape of some hot-film sensors can suppress "
        "response to the turbulent velocity component normal to its surface. On the other hand, "
        "hot-film sensors have less breakage and a more stable geometry than hot-wire sensors. Other "
        "configurations of hot-film sensors include cylindrical quartz rods (approximately 25 µm to "
        "150 µm in diameter); one or more split-film cylindrical sensors for multidimensional "
        "measurements; and flush-mounted sensors for wall heat-transfer measurements."))

    b.append(h3("Principle of Operation"))
    b.append(h4("First Law of Thermodynamics"))
    b.append(p(
        "Figure 29.19 shows the first law of thermodynamics applied to a control volume consisting of "
        "the velocity sensor of either an industrial thermal anemometer, such as shown in "
        "Figure 29.17, or a research thermal anemometer. Application of the first law to thermal "
        "anemometer sensors provides the basis for determining point velocity. Applied to "
        "Figure 29.19, the first law states that the energy into the control volume equals the energy "
        "out plus the energy stored. Making the practical simplifying assumptions of steady-state "
        "operation (i.e., no energy stored) and no heat transfer via radiation, one obtains:"))
    b.append(eq("w = q<sub>c</sub> + q<sub>L</sub>", "29.28"))
    b.append(fig(19, F.FIGS[18], "en"))
    b.append(p(
        "The heat transfer q<sub>c</sub> due to natural and forced convection normally is expressed in "
        "terms of the heat transfer coefficient h as:"))
    b.append(eq("q<sub>c</sub> = h A<sub>v</sub> (T<sub>e</sub> − T<sub>a</sub>)", "29.29"))
    b.append(p(
        "where A<sub>v</sub> = πdL is the external surface area of the velocity sensor. The electric "
        "power w usually is expressed as:"))
    b.append(eq("w = E<sub>v</sub>² ⁄ R<sub>v</sub>", "29.30"))
    b.append(p(
        "where E<sub>v</sub> is the voltage across the sensor, and R<sub>v</sub> is its electric "
        "resistance."))
    b.append(p(
        "For the industrial velocity sensor shown in Figure 29.17, q<sub>L</sub> is the heat "
        "conducted from the end of the heated velocity sensor of length L to the remainder of the "
        "sensor’s length. Most of this heat is convected away by the flowing fluid, and a small "
        "fraction is conducted to the probe stem. In the case of research hot-wire or cylindrical "
        "hot-film sensors, q<sub>L</sub> is conducted to the two prongs, of which a major fraction is "
        "convected away and a minor fraction enters the probe stem. In well-designed velocity "
        "sensors, q<sub>L</sub> is at most 10 % to 15 % of w, a fraction that decreases as velocity "
        "increases."))
    b.append(p(
        "For research velocity sensors, the surface temperature T<sub>e</sub> is identical to the "
        "wire or film temperature T<sub>v</sub>. However, the surface temperature T<sub>e</sub> of "
        "industrial velocity sensors with stainless-steel sheaths is slightly less than the "
        "temperature T<sub>v</sub> of the platinum winding because a temperature drop is required to "
        "pass the heat q<sub>c</sub> through the intervening “skin” — the cement layer and the "
        "stainless-steel tube. This is expressed as:"))
    b.append(eq("T<sub>e</sub> = T<sub>v</sub> − q<sub>c</sub> R<sub>s</sub>", "29.31"))
    b.append(p(
        "where R<sub>s</sub> is the thermal skin resistance in units of K W⁻¹. R<sub>s</sub> is a "
        "constant for a given sensor and is the sum of the thermal resistances of the cement layer "
        "and the stainless-steel tube. For research velocity sensors, R<sub>s</sub> = 0 and "
        "T<sub>e</sub> = T<sub>v</sub> in Equation 29.31. In well-designed, sheathed, industrial "
        "velocity sensors, R<sub>s</sub> is minimized and is approximately 1 K W⁻¹. As evidenced by "
        "Equation 29.31, the effect of skin resistance increases as velocity (i.e., q<sub>c</sub>) "
        "increases. The effect is almost negligible at low velocity; but at high velocity, it is "
        "responsible for the characteristic droop in power vs. velocity flow-calibration curves."))
    b.append(p(
        "Because the flow around cylinders in cross flow is confounded by boundary-layer separation "
        "and vortex shedding, it has defied analytical solution. Therefore, the film coefficient h in "
        "Equation 29.29 is found using empirical correlations. Correlations for h are expressed in "
        "terms of the following nondimensional parameters:"))
    b.append(eq("Nu = ℑ(Re, Pr, Gr, M, Kn)", "29.32"))
    b.append(defs([
        ("Nu = hd ⁄ k", "Nusselt number (the heat-transfer parameter)"),
        ("Re = ρVd ⁄ μ", "Reynolds number (the ratio of dynamic to viscous forces)"),
        ("Pr = μC<sub>p</sub> ⁄ k", "Prandtl number (the fluid properties parameter)"),
        ("M", "Mach number (the gas compressibility parameter)"),
        ("Kn", "Knudsen number (the ratio of the gas mean free path to d)"),
    ]))
    b.append(p(
        "In the above, k is the fluid’s thermal conductivity; μ is its viscosity; and C<sub>p</sub> "
        "is its coefficient of specific heat at constant pressure. If one takes the practical case "
        "where: (1) natural convection is embodied in Re and Pr, (2) the velocity is less than one "
        "third the fluid’s speed of sound (i.e., < 100 m s⁻¹ in ambient air), and (3) the flow is not "
        "in a high vacuum, then one can ignore the effects of Gr, M, and Kn, respectively. Thus,"))
    b.append(eq("Nu = ℑ(Re, Pr)", "29.33"))
    b.append(p(
        "Over the years, many attempts have been made to find universal correlations for the heat "
        "transfer from cylinders in cross flow. For an isothermal fluid at constant pressure, King "
        "[7] expresses Equation 29.33 as:"))
    b.append(eq("Nu = A + B Re<sup>0.5</sup>", "29.34"))
    b.append(p(
        "where A and B are empirical calibration constants that are different for each fluid and each "
        "temperature and pressure. Kramers [8] suggests the following correlation:"))
    b.append(eq("Nu = 0.42 Pr<sup>0.2</sup> + 0.57 Pr<sup>0.33</sup> Re<sup>0.50</sup>", "29.35"))
    b.append(p(
        "This correlation accounts for the variation in fluid properties (k, μ, and Pr) with "
        "temperature. Kramers [8] evaluates these properties at the so-called “film” temperature "
        "(T<sub>v</sub> + T<sub>a</sub>)/2, rather than at T<sub>a</sub> itself. Another comprehensive "
        "correlation is given by Churchill and Bernstein [9]. Several other correlations are similar "
        "to Equation 29.35, but have exponents for the Reynolds number ranging from 0.4 to 0.6. "
        "Others have 0.36 and 0.38 for the exponent of the Prandtl number. Equations 29.34 and 29.35 "
        "are strictly valid only for hot-wire sensors with very high L/d ratios, in which case "
        "q<sub>L</sub> and R<sub>s</sub> are zero. The following universal correlation is suggested "
        "for real-world velocity sensors with variable fluid temperature and nonzero q<sub>L</sub> "
        "and R<sub>s</sub>:"))
    b.append(eq("Nu = A + B Pr<sup>0.33</sup> Re<sup>n</sup>", "29.36"))
    b.append(p(
        "where constants A, B, and n are determined via flow calibration. Equation 29.36 is "
        "applicable to most commercial industrial and research velocity sensors."))
    b.append(p(
        "Combining Equations 29.28, 29.29, 29.30, and 29.36, and recognizing that h = kNu/d, one "
        "obtains:"))
    b.append(eq("E<sub>v</sub>² ⁄ R<sub>v</sub> = (A k + B k Pr<sup>0.33</sup> Re<sup>n</sup>)"
                "(T<sub>e</sub> − T<sub>a</sub>)", "29.37"))
    b.append(p(
        "where A and B are new constants. A, B, and n are determined via flow calibration and account "
        "for all nonidealities, including end conduction and skin resistance. Equation 29.37 is "
        "applicable to most commercial industrial and research velocity sensors. Manufacturers of "
        "industrial thermal anemometers can add other calibration constants to Equation 29.37 to "
        "enhance its correlation with flow-calibration data."))
    b.append(p(
        "The presence of end conduction means that the temperature of the velocity sensor varies with "
        "the axial coordinate y in Figure 29.19. The temperature T actually sensed by the velocity "
        "sensor is the average temperature over length L, or:"))
    b.append(eq("T<sub>v</sub> = (1 ⁄ L) ∫<sub>0</sub><sup>L</sup> T<sub>v</sub>(y) dy", "29.38"))
    b.append(p(
        "Bruun [1] presents an analytical solution for T<sub>v</sub>(y) for hot-wire sensors. "
        "Equation 29.38 is the correct expression for T<sub>v</sub> in Equation 29.37 and is so "
        "defined hereafter."))
    b.append(p(
        "For fluid temperatures less than 200 °C, the electric resistance of the RTD velocity and "
        "temperature sensors is usually expressed as:"))
    b.append(eq("R<sub>v</sub> = R<sub>v0</sub> [1 + α<sub>v</sub> (T<sub>v</sub> − T<sub>0</sub>)]",
                "29.39"))
    b.append(eq("R<sub>T</sub> = R<sub>T0</sub> [1 + α<sub>T</sub> (T<sub>T</sub> − T<sub>0</sub>)]",
                "29.40"))
    b.append(p(
        "where R<sub>v0</sub> and R<sub>T0</sub> are, respectively, the electric resistances of the "
        "velocity sensor and the temperature sensor at temperature T<sub>0</sub> (usually 0 °C or "
        "20 °C), and α<sub>v</sub> and α<sub>T</sub> are the temperature coefficients of resistivity "
        "at temperature T<sub>0</sub>. Additional terms are added to Equations 29.39 and 29.40 when "
        "fluid temperatures exceed 200 °C. When evaluated at the fluid temperature T<sub>a</sub>, the "
        "resistance R<sub>a</sub> of the velocity sensor is:"))
    b.append(eq("R<sub>a</sub> = R<sub>v0</sub> [1 + α<sub>v</sub> (T<sub>a</sub> − T<sub>0</sub>)]",
                "29.41"))
    b.append(p(
        "For applications with wide excursions in fluid temperature, additional terms are added to "
        "Equations 29.39–29.41. At 20 °C, α<sub>v</sub> and α<sub>T</sub> are approximately "
        "0.0036 °C⁻¹ for tungsten wire; 0.0038 °C⁻¹ for pure platinum wire; 0.0016 °C⁻¹ for 90 % "
        "platinum + 10 % rhodium wire; 0.0024 °C⁻¹ for platinum film; and 0.0040 °C⁻¹ for tungsten "
        "film. R<sub>v</sub> and R<sub>a</sub> are called the “hot” and “cold” resistances of the "
        "velocity sensor, respectively. The ratio R<sub>v</sub>/R<sub>a</sub> is called the "
        "<b>overheat ratio</b>. For gas flows, sheathed industrial velocity sensors are operated at "
        "overheat ratios from 1.1 to 1.4 (T<sub>v</sub> − T<sub>a</sub> = 30 °C to 100 °C). For gas "
        "flows, the overheat ratio of tungsten hot-wire and hot-film sensors are usually set to "
        "approximately 1.8 (T<sub>v</sub> − T<sub>a</sub> = 200 °C to 300 °C) and 1.4 "
        "(T<sub>v</sub> − T<sub>a</sub> = 150 °C to 200 °C), respectively. For water flows, the "
        "overheat ratio of hot-film sensors is approximately 1.05 to 1.10 (T<sub>v</sub> − "
        "T<sub>a</sub> = 10 °C to 20 °C). Mikulla [6] shows the importance of the effect of overheat "
        "ratio on frequency response."))
    b.append(p("Combining Equations 29.39 and 29.41, one obtains:"))
    b.append(eq("T<sub>v</sub> − T<sub>a</sub> = (R<sub>v</sub> − R<sub>a</sub>) ⁄ "
                "(α<sub>v</sub> R<sub>v0</sub>)", "29.42"))
    b.append(p("Inserting this into Equation 29.37 obtains:"))
    b.append(eq("E<sub>v</sub>² ⁄ [R<sub>v</sub> (R<sub>v</sub> − R<sub>a</sub>)] = A k + "
                "B k Pr<sup>0.33</sup> Re<sup>n</sup>", "29.43"))
    b.append(p(
        "where new constants A and B have absorbed the constants α<sub>v</sub> and "
        "R<sub>v0</sub>."))

    b.append(h5("Electronic Drives and the Bridge Circuit"))
    b.append(p(
        "Figures 29.20 to 29.22 show three typical electronic drives for thermal anemometer sensors. "
        "Figure 29.20 shows the commonly used constant-temperature anemometer Wheatstone bridge "
        "circuit described by Takagi [10]. Figure 29.21 is similar, but is controlled and operated "
        "via a personal computer. In the constant-temperature mode, the hot resistance "
        "R<sub>v</sub>, and hence the velocity sensor’s temperature, remains virtually constant, "
        "independent of changes in velocity. With the addition of the temperature sensor shown in "
        "Figure 29.20, the bridge circuit also compensates for variations in fluid temperature "
        "T<sub>a</sub>, as described later. Another common analog sensor drive is the "
        "constant-current anemometer. In this mode, a constant current is passed through the velocity "
        "sensor, and the sensor’s temperature decreases as the velocity increases. Because the entire "
        "mass of the sensor must participate in this temperature change, the sensor is slower in "
        "responding to changes in velocity. Because the constant-temperature anemometer has a flatter "
        "frequency response, excellent signal-to-noise ratio [2], and is easier to use, it is favored "
        "over constant-current anemometers by most researchers and manufacturers for velocity and "
        "turbulence measurements. The constant-current anemometer with a very low overheat ratio is "
        "often used as the temperature sensor. Subsequently, references made herein to sensor "
        "electronics will be based on the constant-temperature anemometer."))
    b.append(fig(20, F.FIGS[19], "en"))
    b.append(p(
        "In the constant-temperature anemometer drive shown in Figure 29.20, the resistances R₁ and "
        "R₂ are chosen to: (1) maximize the current on the velocity-sensor side of the bridge so it "
        "becomes self-heated and (2) minimize the current on the temperature-sensor side of the "
        "bridge so it is not self-heated and is independent of velocity. Additionally, the "
        "temperature sensor must be sufficiently large in size to avoid self-heating. The ratio "
        "R₂/R₁ is called the <b>bridge ratio</b>. A bridge ratio of 5:1 to 20:1 is normally used; but "
        "for optimum frequency response and compensation for long cable length, a bridge ratio of "
        "1:1 can be used. In Figure 29.20, the operational amplifier, in a feedback control loop, "
        "senses the error voltage (e₂ − e₁) and feeds the exact amount of current to the top of the "
        "bridge necessary to make (e₂ − e₁) approach zero. In this condition, the bridge is "
        "balanced; that is,"))
    b.append(eq("R₁ ⁄ (R<sub>v</sub> + R₃) = R₂ ⁄ (R<sub>T</sub> + R₄)", "29.44"))
    b.append(p("or"))
    b.append(eq("R<sub>v</sub> = (R₁ ⁄ R₂)(R<sub>T</sub> + R₄) − R₃", "29.45"))
    b.append(p(
        "From Equation 29.45, one sees that R<sub>v</sub> is a linear function of R<sub>T</sub>. This "
        "relationship forms the basis for analog temperature compensation."))
    b.append(p(
        "Expressing the voltage E<sub>v</sub> across the velocity sensor in terms of the bridge "
        "voltage E, one obtains:"))
    b.append(eq("E<sub>v</sub> = E R<sub>v</sub> ⁄ (R₁ + R₃ + R<sub>v</sub>)", "29.46"))
    b.append(p(
        "Inserting this into Equation 29.43, one arrives at the generalized expression for the first "
        "law of thermodynamics for the thermal anemometer velocity sensor:"))
    b.append(eq("E² = G [A k + B k (ρ<sub>s</sub> U<sub>s</sub> ⁄ μ)<sup>n</sup> "
                "Pr<sup>0.33</sup>]", "29.47"))
    b.append(p(
        "where G = (R₁ + R₃ + R<sub>v</sub>)² (R<sub>v</sub> − R<sub>a</sub>) ⁄ R<sub>v</sub>, and "
        "where A and B again are new constants. In Equation 29.47, one recognizes that "
        "conservation-of-mass considerations require that ρU = ρ<sub>s</sub>U<sub>s</sub>, where ρ "
        "and U are referenced to the actual fluid temperature and pressure, and ρ<sub>s</sub> and "
        "U<sub>s</sub> are referenced to normal conditions of 0 °C or 20 °C temperature and 1 atm "
        "pressure. To write Equation 29.47 in terms of U, one simply replaces ρ<sub>s</sub> by ρ and "
        "U<sub>s</sub> by U."))
    b.append(fig(21, F.FIGS[20], "en"))

    b.append(h4("Temperature Compensation"))
    b.append(p(
        "The objective of temperature compensation is to make the bridge voltage E in Equation 29.47 "
        "independent of changes in the fluid temperature T<sub>a</sub>. This is accomplished if: (1) "
        "the term G in Equation 29.47 is independent of T<sub>a</sub> and (2) compensation is made for "
        "the change in fluid properties (k, μ, and Pr) with T<sub>a</sub>. Since these fluid "
        "properties have a weaker temperature dependence than G in Equation 29.47, for small "
        "temperature changes (less than ±10 °C) in gas flows, only G requires compensation."))
    b.append(p(
        "The two-temperature method is a typical procedure for compensating for both G and fluid "
        "properties. In this method, fixed-bridge resistors R₁, R₂, and R₄ in Figure 29.20 are "
        "selected so that E is identical at two different temperatures, but at the same mass flow "
        "rate. This procedure is accomplished during flow calibration and has variations among "
        "manufacturers."))
    b.append(p(
        "The two-temperature method adequately compensates for temperature variations less than "
        "approximately ±50 °C. In higher temperature gas flow applications, such as the flow of "
        "preheated combustion air and stack gas, temperature variations typically are higher. The "
        "microprocessor-based digital sensor drive in Figure 29.22 provides temperature compensation "
        "for temperature variations ranging from ±50 °C to ±150 °C. This sensor drive has no analog "
        "bridge. Instead, it has a virtual digital bridge that maintains (T<sub>v</sub> − "
        "T<sub>a</sub>) constant within 0.1 °C and has algorithms that automatically compensate for "
        "temperature variations in k, μ, and Pr. For this digital sensor drive, the first law of "
        "thermodynamics is found from Equation 29.37 as:"))
    b.append(eq("w = [A k + B k (ρ<sub>s</sub> U<sub>s</sub> ⁄ μ)<sup>n</sup> Pr<sup>0.33</sup>] ΔT",
                "29.48"))
    b.append(p("where ΔT = (T<sub>v</sub> − T<sub>a</sub>) is now a known constant."))
    b.append(fig(22, F.FIGS[21], "en"))

    b.append(h4("Flow Calibration"))
    b.append(p(
        "Figure 29.23 shows a typical flow calibration curve for the digital electronics drive shown "
        "in Figure 29.22. The curve is nonlinear of a logarithmic nature. The nonlinearity is "
        "disadvantageous because it requires linearization circuitry, but is advantageous because it "
        "provides rangeabilities up to 1000:1 for a single sensor. Additionally, the high-level "
        "output of several volts provides excellent repeatability and requires no amplification other "
        "than that for spanning. Since the critical dimensions of thermal anemometer sensors are so "
        "small, current manufacturing technology is incapable of maintaining sufficiently small "
        "tolerances to ensure sensor reproducibility. Therefore, each thermal anemometer must be flow "
        "calibrated, for example as in Figure 29.23, over its entire velocity range, either at the "
        "exact fluid temperature of its usage or over the range of temperatures it will encounter if "
        "it is to be temperature compensated. A 10 to 20 point velocity calibration is required to "
        "accurately determine the calibration constants A, B, and n in Equation 29.47. A "
        "least-squares curve-fitting procedure usually is applied. Proper flow calibration requires "
        "two critical elements: (1) a stable, reproducible, flow-generating facility and (2) an "
        "accurate velocity transfer standard. Bruun [1] and Gibbings et al. [4] provide more insight "
        "into curve fitting."))
    b.append(fig(23, F.FIGS[22], "en"))
    b.append(p(
        "Flow-generating facilities are of two types — open loop and closed loop. An open-loop "
        "facility consists of: (1) a flow source such as a fan, pump, elevated tank, or compressed "
        "gas supply; (2) a flow-quieting section, such as a plenum with flow straighteners, screens, "
        "or other means to reduce swirling, turbulence, or other flow nonuniformities; (3) a nozzle "
        "to accelerate the flow and further flatten, or uniformize, the velocity profile; (4) a test "
        "section or free jet into which the thermal anemometer probe is inserted; and (5) a means for "
        "holding and sealing the thermal anemometer probe and velocity transfer standard. The test "
        "section or free jet must have: a velocity profile which is uniform within approximately "
        "0.5 % to 1.0 % in its central portion; a turbulence intensity less than about 0.5 %; and an "
        "area large enough so that the projected area of the velocity probe is less than 5 % to 10 % "
        "of the cross-sectional area. Manufacturers of small open-loop flow calibrators often "
        "determine the calibration flow velocity by measuring the pressure drop across the nozzle."))
    b.append(p(
        "The closed-loop flow-generating facility, or wind tunnel, has the same components, but the "
        "exit of the test section is connected via ductwork to the inlet of the fan or pump so that "
        "the air mass inside the facility is conserved. Open-loop facilities are less expensive than "
        "closed-loop tunnels and are far more compact, making them suitable for flow calibrations in "
        "the field. But, a laboratory open-loop air-flow calibrator with a fan as the flow generator "
        "actually is closed loop, with the loop closing within the laboratory. For air velocities "
        "less than about 5 m s⁻¹, open-loop calibrators can experience shifts due to changing "
        "pressure, temperature, or other conditions in the laboratory. Properly designed closed-loop "
        "wind tunnels generate precise, reproducible air velocities from about 0.5 m s⁻¹ to "
        "150 m s⁻¹. When fitted with water chillers, they remove compression heating and provide a "
        "constant-temperature air flow within ±2 °C. When fitted with an electric heater and proper "
        "thermal insulation, they provide air temperatures up to 300 °C. Gibbings [4] describes a "
        "water box displacement rig for flow calibration at very low velocities in the range of "
        "0.1 m s⁻¹ to 4 m s⁻¹."))
    b.append(p(
        "Pitot tubes and laser Doppler anemometers are the two most common velocity transfer "
        "standards used to calibrate thermal anemometers. Both have detailed descriptions earlier in "
        "this chapter. The Pitot tube usually has the classical “L” shape and an outside diameter of "
        "about 3 mm. Its tip is located in the same plane in the test section as the thermal "
        "anemometer probe but is no closer than approximately 3 cm. The focal volume of the laser "
        "Doppler anemometer is similarly located. The Pitot tube is far less expensive and easier to "
        "operate, but is difficult to use if air velocities are less than about 3 m s⁻¹. A proper "
        "Pitot-tube flow transfer standard should have its calibration recertified every 6 months by "
        "an accredited standards laboratory. On the other hand, the laser Doppler anemometer is a "
        "fundamental standard that accurately measures air velocity from approximately 0.5 m s⁻¹ to "
        "100 m s⁻¹. Since it provides noncontact anemometry, it is usable at high temperatures. Its "
        "primary disadvantages are high expense and complications associated with properly seeding "
        "the flow with particles."))

    b.append(h3("Measurements"))
    b.append(h4("Point Velocity"))
    b.append(p(
        "Based on the first law of thermodynamics expressed by Equation 29.47, one now can solve for "
        "the desired quantity — either the actual point velocity U (m s⁻¹) or the point mass velocity "
        "U<sub>s</sub> (normal m s⁻¹). Here, one assumes that the velocity vector is normal to the "
        "flow sensor. Two- and three-dimensional velocity measurements are discussed later. In the "
        "following, A, B, and n are constants, but are different for each case."))
    b.append(p(
        "The simplest case is isothermal flow with a hot-wire sensor having a very high "
        "length-to-diameter ratio (L/d). In this case, the exponent n in Equation 29.47 is 0.5, as "
        "shown by Equation 29.34. The applicable first law and velocity expressions are:"))
    b.append(eq("E² = A + B U<sup>0.5</sup>", "29.49"))
    b.append(p("and"))
    b.append(eq("U = [(E² − A) ⁄ B]²", "29.50"))
    b.append(p(
        "In the case of a real-world sensor in an isothermal flow having either end loss only or both "
        "end loss and skin resistance, one obtains:"))
    b.append(eq("E² = A + B U<sup>n</sup>", "29.51"))
    b.append(p("and"))
    b.append(eq("U = [(E² − A) ⁄ B]<sup>1/n</sup>", "29.52"))
    b.append(p(
        "Often, Equation 29.52 is replaced with a polynomial of the form U = F(E²), where the "
        "function F( ) is a fourth-order polynomial whose coefficients are determined from flow "
        "calibration data using least-squares curve-fitting software. For the same case as above, but "
        "with nonisothermal flow, the first law is expressed by Equation 29.47, and the velocity is "
        "expressed as:"))
    b.append(eq("U<sub>s</sub> = (μ ⁄ ρ<sub>s</sub>) [(E² ⁄ G − A k) ⁄ (B k Pr<sup>0.33</sup>)]"
                "<sup>1/n</sup>", "29.53"))
    b.append(p(
        "For the digital sensor drive of Figure 29.22, the first law is given by Equation 29.48, and "
        "the velocity by:"))
    b.append(eq("U<sub>s</sub> = (μ ⁄ ρ<sub>s</sub>) [(w ⁄ ΔT − A k) ⁄ (B k Pr<sup>0.33</sup>)]"
                "<sup>1/n</sup>", "29.54"))
    b.append(p(
        "Current commercial industrial thermal anemometer systems have temperature-compensation and "
        "“linearization” electronics that automatically calculate U<sub>s</sub> as a linear function "
        "of E or w, based on the foregoing relationships."))

    b.append(h4("Turbulence"))
    b.append(p(
        "Turbulence measurements are the second most common application of research thermal "
        "anemometers. This measurement requires the high-frequency response of hot-wire and hot-film "
        "research anemometers operated in the constant-temperature mode. The vast majority of fluid "
        "flows are turbulent. Only flows with very low Reynolds numbers are nonturbulent, or laminar. "
        "Turbulent flows are time variant and usually are separated as follows into time-mean and "
        "fluctuating parts:"))
    b.append(eq("U(t) = Ū + u<br>V(t) = V̄ + v<br>W(t) = W̄ + w<br>"
                "T<sub>a</sub>(t) = T̄<sub>a</sub> + θ<br>E = Ē + e", "29.55"))
    b.append(p(
        "where U(t), V(t), W(t) are the orthogonal components in the x, y, and z directions, "
        "respectively, such as shown in Figure 29.18 for the 3-D hot-wire probe. T<sub>a</sub>(t) is "
        "the fluid temperature, and E(t) is the bridge voltage. Ū, V̄, W̄, T̄<sub>a</sub>, and Ē are the "
        "time-mean parts, and u(t), v(t), w(t), θ(t), and e(t) are the time-dependent fluctuating "
        "parts. The time-mean parts are averaged sufficiently long to become independent of turbulent "
        "fluctuations, yet respond to changes with time in the main flow. In the previous subsection, "
        "the expressions given were for the time-mean velocity. In the study of turbulence, one is "
        "primarily interested in the time average of the product of two fluctuating velocity "
        "components (turbulence correlations) because these terms appear in the time-averaged "
        "Navier–Stokes equation. Two important turbulence correlations are "
        "<span style=\"text-decoration:overline\">u²</span> and "
        "<span style=\"text-decoration:overline\">uv</span>. The correlation "
        "<span style=\"text-decoration:overline\">u²</span> divided by Ū is called the <b>turbulence "
        "intensity</b>. Manufacturers of research anemometer systems provide electronics for "
        "automatically computing turbulence correlations."))
    b.append(p(
        "For a fluid with changes in temperature sufficiently small that fluid properties are "
        "essentially constant, one can write Equation 29.47 in the following form:"))
    b.append(eq("E² = (A + B U<sup>n</sup>)(T<sub>v</sub> − T<sub>a</sub>)", "29.56"))
    b.append(p(
        "where A, B, and n are constant and where R<sub>v</sub> is virtually constant because the "
        "anemometer is in the constant-temperature mode. Elsner [11] shows that the fluctuating "
        "voltage e is found by taking the total derivative of Equation 29.56, as follows:"))
    b.append(eq("e = S<sub>u</sub> u + S<sub>θ</sub> θ", "29.57"))
    b.append(p("where"))
    b.append(eq("S<sub>u</sub> = ∂E ⁄ ∂U = (n B U<sup>n−1</sup> ⁄ 2) "
                "[(T<sub>v</sub> − T<sub>a</sub>) ⁄ (A + B U<sup>n</sup>)]<sup>1/2</sup>"
                " = velocity sensitivity", "29.58"))
    b.append(eq("S<sub>θ</sub> = ∂E ⁄ ∂T<sub>a</sub> = −(1 ⁄ 2) "
                "[(A + B U<sup>n</sup>) ⁄ (T<sub>v</sub> − T<sub>a</sub>)]<sup>1/2</sup>"
                " = temperature sensitivity", "29.59"))
    b.append(p(
        "It is seen from Equations 29.58 and 29.59 that increasing (T<sub>v</sub> − T<sub>a</sub>), "
        "i.e., operating the sensor as hot as possible, maximizes the velocity sensitivity and "
        "minimizes the sensitivity to temperature fluctuations. This is why tungsten hot wires are "
        "operated at high temperatures (typically 200 °C to 300 °C)."))
    b.append(p(
        "The fluctuating components of velocity have a broad frequency spectrum, ranging from "
        "10⁻² Hz to 10⁵ Hz, and sometimes even higher. Therefore, it is imperative that the frequency "
        "response of constant-temperature research anemometers have a flat frequency response, i.e., "
        "minimized attenuation and phase shift at higher frequencies. Blackwelder [12] and several "
        "other investigators have studied the frequency response of hot-wire anemometers. For "
        "turbulence measurements, Borgos [13] describes commercial research anemometer systems with "
        "features such as: low-pass filters to decrease electronics noise; a subcircuit for "
        "determining and setting overheat ratio; a square-wave generator for frequency response "
        "testing; and two or more controls to optimize the frequency response to fast fluctuations. "
        "Recent systems have electronics that compensate for frequency attenuation. When used with "
        "5 µm diameter hot-wire sensors in air, commercial systems are capable of nearly flat "
        "frequency response and very small phase lag from 0 Hz to approximately 10⁴ Hz. As reported by "
        "Nelson and Borgos [14], wedge and conical hot-film sensors in water have a relatively flat "
        "response from 0 Hz to 10 Hz for velocities above 0.3 m s⁻¹."))
    b.append(p(
        "Two- and three-component velocity and turbulence measurements are made using hot-wire or "
        "hot-film research anemometers, such as shown in Figure 29.18. As described by Müller [15], "
        "hot-wire or cylindrical hot-film probes in the “X”-configuration are used to measure the U "
        "and V velocity components. In a three-sensor orthogonal array, they measure U, V, and W. "
        "Döbbeling, Lenze, and Leuckel [16] and other investigators have developed four-wire arrays "
        "for measurement of U, V, and W. Olin and Kiland [17] describe an orthogonal array of three "
        "cylindrical split hot-film sensors. Each of the three sensors in this array has two "
        "individually operated hot-films separated by two axial splits 180° apart along its entire "
        "length. The two split films take advantage of the nonuniform heat-transfer distribution "
        "around a cylinder in cross flow."))
    b.append(p(
        "In multisensor arrays, the velocity vector is not necessarily normal to a cylindrical "
        "sensor. If the discussion is limited to isothermal flows, the first law expressed by "
        "Equation 29.47 becomes:"))
    b.append(eq("E² = A + B V<sub>e</sub><sup>n</sup>", "29.60"))
    b.append(p(
        "where V<sub>e</sub> is the effective velocity sensed by a single cylindrical sensor in the "
        "array, and A, B, and n are constants. Jörgenson [18] describes V<sub>e</sub> as follows:"))
    b.append(eq("V<sub>e</sub>² = U<sub>N</sub>² + a² U<sub>T</sub>² + b² U<sub>B</sub>²", "29.61"))
    b.append(defs([
        ("U<sub>N</sub>", "Velocity component normal to the sensor"),
        ("U<sub>T</sub>", "Tangential component"),
        ("U<sub>B</sub>", "Component perpendicular to both U<sub>N</sub> and U<sub>T</sub> "
                          "(i.e., binormal)"),
    ]))
    b.append(p(
        "The constants a and b in Equation 29.61 are referred to as the sensor’s yaw and pitch "
        "coefficients, respectively, and are determined via flow calibration. Typical values for a "
        "and b for a plated hot-wire sensor are 0.2 and 1.05, respectively. Inserting Equation 29.61 "
        "into Equation 29.60, we get the following expression for the output signal of a single "
        "sensor in the array:"))
    b.append(eq("E² = A + B (U<sub>N</sub>² + a² U<sub>T</sub>² + b² U<sub>B</sub>²)"
                "<sup>n/2</sup>", "29.62"))
    b.append(p(
        "Expressions like this, or similar ones such as given by Lekakis, Adrian, and Jones [19], are "
        "written for all sensors in the array. These expressions and trigonometry are then used to "
        "solve for the components of velocity U, V, and W in the x, y, z spatially fixed reference "
        "frame."))

    b.append(h4("Channel Flows"))
    b.append(p(
        "Based on the following relationship, a single-point industrial insertion thermal anemometer "
        "monitors the mass flow rate ṁ (kg s⁻¹) in ducts, pipes, stacks, or other flow channels by "
        "measuring the velocity U<sub>s,c</sub> at the channel’s centreline:"))
    b.append(eq("ṁ = ρ<sub>s</sub> γ U<sub>s,c</sub> A<sub>c</sub>", "29.63"))
    b.append(p(
        "where U<sub>s,c</sub> is the velocity component parallel to the channel’s axis measured at "
        "the channel’s centreline and referenced to normal conditions of 0 °C or 20 °C temperature "
        "and 1 atmosphere pressure; ρ<sub>s</sub>, a constant, is the fluid’s mass density at the "
        "same normal conditions; A<sub>c</sub>, another constant, is the cross-sectional area of the "
        "channel; and γ is a constant defined as γ = U<sub>s,ave</sub>/U<sub>s,c</sub>, where "
        "U<sub>s,ave</sub> is the average velocity over area A<sub>c</sub>. The velocity in channel "
        "flows is seldom uniform and therefore γ is not unity. If the flow channel has a "
        "length-to-diameter ratio of 40 to 60, then its flow profile becomes unchanging and is called "
        "“fully developed.” In fully developed flows, the fluid’s viscosity has retarded the velocity "
        "near the walls, and hence γ is always less than unity. If the channel’s Reynolds number is "
        "less than 2000, the flow is laminar; the fully developed profile is a perfect parabola; and "
        "γ is 0.5. If the Reynolds number is larger than 4000, the flow is turbulent; the fully "
        "developed profile has a flattened parabolic shape; and for pipes with typical rough walls, γ "
        "is 0.79, 0.83, and 0.83 for Reynolds numbers of 10⁴, 10⁵, and 10⁶, respectively. If the "
        "Reynolds number is between 2000 and 4000, the flow is transitioning between laminar and "
        "turbulent flows, and γ ranges between 0.5 and 0.8."))
    b.append(p(
        "Unfortunately, in most large ducts and stacks, 40 to 60 diameters of straight run preceding "
        "the flow monitoring location does not exist. Instead, the flow profile usually is highly "
        "nonuniform, swirling, and, in air-preheater ducts and in stacks, is further confounded by "
        "temperature nonuniformities. In these cases, single-point monitoring is ill-advised. "
        "Fortunately, multipoint monitoring with industrial thermal anemometer flow-averaging arrays, "
        "such as shown in Figure 29.18, have proven successful in these applications. As described by "
        "Olin [20], this method consists of a total of N (usually, N = 4, 8, or 12) industrial "
        "thermal anemometer sensors, each similar to that shown in Figure 29.17, located at the "
        "centroid of an equal area A<sub>c</sub>/N in the channel’s cross-sectional area "
        "A<sub>c</sub>. The individual mass flow rate ṁ<sub>i</sub> monitored by each sensor is "
        "ρ<sub>s</sub>U<sub>s,i</sub>(A<sub>c</sub>/N), where U<sub>s,i</sub> is the individual "
        "velocity monitored by the sensor at point i. The desired quantity, the total mass flow rate "
        "ṁ through the channel, is the sum of the individual mass flow rates, or:"))
    b.append(eq("ṁ = Σ<sub>i=1</sub><sup>N</sup> ṁ<sub>i</sub> = ρ<sub>s</sub> A<sub>c</sub> "
                "U<sub>s,ave</sub>", "29.64"))
    b.append(p(
        "where U<sub>s,ave</sub> is the arithmetic average of the N individual velocities "
        "U<sub>s,i</sub>. As described by Olin [21], industrial multipoint thermal anemometers are "
        "used as the flow monitor in stack continuous emissions monitoring systems required by "
        "governmental air-pollution regulatory agencies."))

    b.append(h3("Instrumentation Systems"))
    b.append(p(
        "Table 29.3 lists examples of typical commercial thermal anemometer systems. Table 29.4 lists "
        "their major manufacturers. Thermal anemometer systems include three elements: sensors, "
        "probe, and electronics. Sensors and probes have been described in previous sections. The "
        "electronics of industrial systems are enclosed in an explosion-proof or other "
        "industrial-grade housing mounted either directly on the probe or remotely (usually within "
        "30 m). The electronics is powered with a 24 V dc source or with 100, 115, or 230 V ac line "
        "voltage. The output signal typically is 0 to 5 V dc, 4 to 20 mA, RS232, or RS485 linearly "
        "proportional to gas mass velocity U<sub>s</sub> over the range of 0.5 normal m s⁻¹ to "
        "150 normal m s⁻¹. In-line mass flowmeters have the same output-signal options and are "
        "calibrated directly in mass flow rate ṁ (kg s⁻¹)."))
    _hd, _rows, _cap = _t293("en")
    b.append(table(_hd, _rows, _cap, widths=("62%", "38%")))
    _hd, _rows, _cap = _t294("en")
    b.append(table(_hd, _rows, _cap, widths=("50%", "50%")))
    b.append(p(
        "In-line meters are now available with built-in flow conditioners that eliminate errors "
        "associated with upstream disturbances, such as elbows, valves, and pipe expansions. Systems "
        "are available either with lower cost analog electronics or with smart microprocessor-based "
        "electronics. The repeatability of these systems is ±0.2 % of full scale. The typical "
        "accuracy of a smart industrial system is ±2 % of reading over 10 to 100 % of full scale and "
        "±0.5 % of full scale below 10 % of full scale. Automatic temperature compensation "
        "facilitates temperature coefficients of ±0.04 % of reading per °C within ±20 °C of "
        "calibration temperature and ±0.08 % of reading per °C within ±40 °C. High-temperature "
        "applications have temperature compensation over a range of ±150 °C. Pressure effects are "
        "negligible within ±300 kPa of calibration pressure."))
    b.append(p(
        "Research thermal anemometer systems usually are coupled with a personal computer, as shown "
        "in Figure 29.21. The PC provides system set-up and control, as well as data display and "
        "analysis. Modern systems feature low-noise circuits, together with smart bridge optimization "
        "technology that eliminates tuning and automatically provides flat frequency response up to "
        "300,000 Hz. Lower cost units provide flat response up to 10,000 Hz. A built-in thermocouple "
        "circuit simplifies temperature measurement. The PC’s windows-based software provides near "
        "real-time displays of velocity, probability distribution, and turbulence intensity. "
        "Post-processing gives additional statistics, including: mean velocity; turbulence intensity; "
        "standard deviation; skewness; flatness; normal stress for one-, two-, and three-component "
        "probes; as well as shear stress, correlation coefficients and flow-direction angle for two- "
        "and three-dimensional probes. In addition, power spectrum, auto correlations, and cross "
        "correlations can be displayed. The software automatically handles flow calibration set-up "
        "and calculates calibration velocity. Systems are available in 1-, 2-, 8-, and 16-channel "
        "versions."))
    b.append(p(
        "Commercial industrial and research thermal anemometer systems were first introduced in the "
        "early 1960s. At first, industrial thermal anemometers were not considered sufficiently "
        "durable for the rigors of industrial use. With the advent of stainless-steel sheathed "
        "sensors and microprocessor-based electronics, industrial thermal anemometers now enjoy the "
        "credibility formerly attributed to only traditional flowmeter approaches. Initial research "
        "systems required a high level of user knowledge and considerable involvement in operation. "
        "In contrast, current research systems have nearly flat frequency response, high accuracy, "
        "and easy-to-use controls providing the flexibility researchers require. Research systems "
        "based on personal computers have graphical user interfaces that enhance both performance and "
        "simplicity of operation."))

    b.append(h3("References"))
    b.append(wl(_refs292("en")))
    b.append(h3("Further Information"))
    b.append(wl([
        "J. A. Fay, <i>Introduction to Fluid Mechanics</i>, Cambridge, MA: MIT Press, 1994.",
        "A. Bejan, <i>Convection Heat Transfer</i>, New York: John Wiley &amp; Sons, 1995.",
    ]))
    return "".join(b)


def sec_29_3_vi():
    b = []
    b.append(h2("29.3 Đo vận tốc bằng laser", "Laser Anemometry"))
    b.append(p("Rajan K. Menon — TSI Inc."))

    b.append(p(
        "Đo vận tốc bằng laser, hay đo vận tốc bằng quang học laser, chỉ mọi kỹ thuật dùng laser để "
        "đo vận tốc. Cách tiếp cận phổ biến nhất dùng nguyên lý dịch Doppler để đo vận tốc của một "
        "chất lưu đang chảy tại một điểm, và được gọi là đo vận tốc Doppler laser (LDV) hay nhiệt kế "
        "gió Doppler laser (LDA). Kỹ thuật này — còn được gọi là kỹ thuật hai chùm tia, Doppler vi "
        "sai hay chế độ vân — dùng hai chùm laser giao nhau (đã được hội tụ), và cũng được dùng để "
        "đo chuyển động của các bề mặt [1]. Trong một số tình huống dòng đặc biệt, người ta dùng một "
        "cách tiếp cận khác với hai chùm laser hội tụ không giao nhau, gọi là kỹ thuật hai tiêu điểm "
        "(hay L2F), để đo vận tốc dòng tại một điểm [2]. Gần đây hơn, việc chiếu sáng bằng các tấm "
        "sáng laser được dùng để đo trường dòng toàn cục và được gọi là đo vận tốc bằng ảnh hạt "
        "(PIV) [3]. Thế mạnh của PIV (kể cả đo vận tốc bằng theo dõi hạt) nằm ở khả năng ghi lại các "
        "cấu trúc rối trong dòng và các hiện tượng chuyển tiếp, cũng như khảo sát các dòng không "
        "dừng [4]. Việc phát triển kỹ thuật này để thu được đồng thời thông tin không gian lẫn thời "
        "gian về trường dòng đang biến nó thành một công cụ chẩn đoán mạnh trong nghiên cứu cơ học "
        "chất lưu [5, 6]. Các cách tiếp cận khác để đo vận tốc dòng toàn cục thuộc phạm trù đo vận "
        "tốc bằng đánh dấu phân tử [7] hoặc đo vận tốc Doppler toàn cục [8, 9]."))
    b.append(p(
        "Tính chất không xâm nhập của kỹ thuật LDV cùng khả năng đo vận tốc chính xác với độ phân "
        "giải không gian và thời gian cao, ngay cả trong các dòng rối mạnh, đã khiến LDV được dùng "
        "rộng rãi để đo dòng. Các vận tốc từ vài micrômét trên giây tới tốc độ siêu âm đã được đo "
        "bằng hệ LDV. Người ta đã dùng LDV để đo dòng rối mạnh [10], dòng trong máy quay [11], đặc "
        "biệt ở vùng giữa các cánh rôto [12, 13], dòng có vận tốc rất cao [14] hoặc rất thấp [15], "
        "dòng ở nhiệt độ cao [16] và trong các môi trường khắc nghiệt khác [17, 18], và dòng trong "
        "không gian hẹp [19]. Tính linh hoạt và mức độ phổ biến của cách tiếp cận LDV trong việc đo "
        "dòng một cách chính xác đã dẫn tới việc gọi kỹ thuật này là đo vận tốc bằng laser hay "
        "nhiệt kế gió laser. Nhiều chi tiết của kỹ thuật, kể cả một số phát triển ban đầu về phần "
        "cứng, được trình bày trong sách của Durst [20]. Adrian [21] đã biên soạn một thư mục các "
        "bài báo mốc của LDV."))
    b.append(p(
        "Với trường hợp các hạt tán xạ hình cầu, kỹ thuật này cũng đã được mở rộng để đo kích thước "
        "của các hạt đó. Khi ấy, tín hiệu ánh sáng tán xạ từ một hệ thu đặt ở vị trí thích hợp được "
        "xử lý để thu được đường kính của hạt, theo kỹ thuật pha Doppler [22]."))
    b.append(p(
        "Các phép đo dòng chất lưu đầu tiên được công bố dùng nguyên lý LDV là của Yeh và "
        "Cummins [23]. Tuy trong trường hợp đó người ta dùng một bố trí quang học gọi là hệ chùm "
        "tia chuẩn để đo độ dịch Doppler, nhưng trong gần như mọi ứng dụng đo, bố trí được dùng "
        "hiện nay là bố trí hai chùm tia hay Doppler vi sai [24]. Bố trí này, còn được gọi là chế "
        "độ “vân”, dùng hai chùm laser giao nhau (Hình 29.24) để đo một thành phần vận tốc. Các ưu "
        "điểm của kỹ thuật LDV khi đo dòng gồm (1) vùng đo nhỏ (tức là đo tại một điểm), (2) độ "
        "chính xác đo cao, (3) khả năng đo bất kỳ thành phần vận tốc mong muốn, (4) đo chính xác "
        "cường độ rối cao, kể cả dòng đảo chiều, (5) dải động rộng, (6) không cần hiệu chuẩn vận "
        "tốc, (7) không có đầu dò trong dòng (không làm nhiễu dòng; đo được trong môi trường khắc "
        "nghiệt), và (8) đáp ứng tần số tốt."))
    b.append(fig(24, F.FIGS[23], "vi"))
    b.append(p(
        "Kỹ thuật LDV dựa vào ánh sáng tán xạ bởi các tâm tán xạ trong chất lưu để đo vận tốc dòng. "
        "Các tâm tán xạ này cũng được gọi là hạt, với hiểu rằng bọt khí hoặc bất cứ thứ gì có chiết "
        "suất khác với chất lưu đều có thể là nguồn ánh sáng tán xạ. Các hạt — đối tượng được đo "
        "vận tốc — phải đủ nhỏ (nói chung cỡ micrômét) để đi theo được các biến đổi của dòng, và đủ "
        "lớn để cho cường độ tín hiệu đủ cho bộ xử lý tín hiệu đưa ra phép đo vận tốc. Cần lưu ý "
        "rằng tín hiệu chỉ tồn tại khi có một hạt “phát hiện được” nằm trong vùng đo, và do đó tín "
        "hiệu là gián đoạn. Điều này, cùng với các tính chất khác của tín hiệu, đặt ra những yêu "
        "cầu riêng cho hệ xử lý tín hiệu và hệ phân tích dữ liệu tiếp theo. Tín hiệu ánh sáng tán "
        "xạ được xử lý để thu tần số dịch Doppler, và từ đó suy ra vận tốc của hạt. Vì vậy, tốc độ "
        "thực hiện các phép đo vận tốc phụ thuộc vào tốc độ hạt đến. Nên có nồng độ hạt cao để có "
        "được sự cập nhật vận tốc gần như liên tục. Trong các thí nghiệm được kiểm soát cẩn thận, "
        "hệ LDV có thể cho độ chính xác rất cao (0,1 % hoặc tốt hơn) đối với vận tốc trung bình. "
        "Các hệ nhiệt kế gió nhiệt nói chung chỉ đo được mức rối thấp hơn so với hệ LDV [25]. Tuy "
        "có thể đo trực tiếp tần số dịch Doppler của một chùm laser đơn do một hạt chuyển động gây "
        "ra [26], hầu hết hệ LDV dùng nguyên lý ngoại sai để chỉ thu và xử lý tần số (sai) "
        "Doppler."))

    b.append(h3("Nguyên lý hoạt động", "Principle of Operation"))
    b.append(h4("Cách tiếp cận hai chùm tia", "Dual-Beam Approach"))
    b.append(p(
        "Cách tiếp cận hai chùm tia là bố trí quang học phổ biến nhất trong các hệ LDV dùng cho đo "
        "dòng. Sơ đồ (Hình 29.24) cho thấy các bộ phận cơ bản của một hệ LDV hoàn chỉnh để đo một "
        "thành phần vận tốc. Quang học phát gồm một phần tử quang tách chùm laser ban đầu thành hai "
        "chùm song song và một hệ thấu kính hội tụ và làm hai chùm giao nhau. Vùng giao nhau của hai "
        "chùm trở thành vùng đo. Quang học thu (được bố trí theo hướng tới) gom một phần ánh sáng "
        "tán xạ bởi các hạt trong dòng chảy đi qua vùng giao nhau của hai chùm (vùng đo) và dẫn ánh "
        "sáng này tới một đầu dò quang, nơi biến cường độ ánh sáng tán xạ thành tín hiệu điện tương "
        "tự. Tần số của tín hiệu này tỉ lệ với vận tốc của hạt. Một bộ xử lý tín hiệu trích thông "
        "tin tần số từ đầu ra của đầu dò quang và cung cấp nó dưới dạng một con số tương ứng với "
        "vận tốc tức thời của hạt. Hệ xử lý dữ liệu thu được các tính chất chi tiết của dòng từ "
        "những phép đo vận tốc tức thời này. Tín hiệu lý tưởng của đầu dò quang, ứng với một hạt đi "
        "qua tâm vùng đo, được vẽ ở góc dưới bên trái Hình 29.24. Tín hiệu thực sẽ có nhiễu chồng "
        "lên; và dạng tín hiệu sẽ thay đổi tuỳ theo quỹ đạo của hạt qua vùng đo [27]."))

    b.append(h5("Mô tả theo mô hình vân", "Fringe Model Description"))
    b.append(p(
        "Tuy có nhiều cách mô tả các đặc điểm của một hệ hai chùm tia, cách mô tả dựa trên mô hình "
        "vân có lẽ là đơn giản nhất. Để đơn giản, giả thiết đường kính và cường độ của cả hai chùm "
        "là như nhau. Sau khi đi qua thấu kính phát, đường kính mỗi chùm giảm liên tục tới một giá "
        "trị cực tiểu (eo chùm) tại tiêu điểm của thấu kính, rồi lại tăng lên. Như vậy các eo chùm "
        "giao nhau tại chỗ hai chùm laser cắt nhau (tại tiêu điểm của thấu kính), và các mặt sóng "
        "trong hai chùm giao thoa với nhau, tạo ra một hệ vân [28]. Trong hệ vân này, với giả thiết "
        "hai chùm có cường độ bằng nhau và các phẩm chất cần thiết khác, cường độ sáng biến thiên "
        "từ không (vân tối) tới cực đại (vân sáng), và các vân cách đều nhau. Các hạt trong dòng đi "
        "qua vùng giao nhau (vùng đo) tán xạ ánh sáng theo mọi hướng. Một hệ quang học, gồm một "
        "thấu kính thu (để chuẩn trực ánh sáng tán xạ thu được) và một thấu kính hội tụ, được dùng "
        "để gom ánh sáng tán xạ và hội tụ nó lên bộ thu. Khẩu độ trước bộ thu dùng để chắn ánh sáng "
        "lạc và phản xạ, chỉ gom ánh sáng tán xạ từ vùng đo."))
    b.append(p(
        "Khi một hạt trong dòng, có vận tốc u, đi qua các vân, dạng cường độ của ánh sáng do hạt "
        "tán xạ giống như vẽ ở góc dưới bên trái Hình 29.24. Thành phần vận tốc u<sub>y</sub> "
        "(vuông góc với trục quang và nằm trong mặt phẳng của các chùm tới) có thể thu được từ tỉ "
        "số giữa khoảng cách giữa hai vân (hay khoảng vân, d<sub>f</sub>) và thời gian t (= "
        "1/f<sub>D</sub>) để hạt đi qua một cặp vân, trong đó f<sub>D</sub> là tần số của tín hiệu. "
        "Sự biến thiên biên độ của tín hiệu phản ánh phân bố cường độ Gauss ngang qua chùm laser. "
        "Quang học thu của hệ hai chùm tia có thể đặt ở bất kỳ góc nào, và tín hiệu thu được vẫn có "
        "cùng tần số. Tuy nhiên, chất lượng và cường độ tín hiệu sẽ thay đổi nhiều theo góc đặt "
        "quang học thu."))

    b.append(h5("Giải thích theo độ dịch Doppler", "Doppler Shift Explanation"))
    b.append(p(
        "Cách mô tả hệ hai chùm tia theo nguyên lý dịch Doppler như sau. Tại bộ thu, tần số của ánh "
        "sáng dịch Doppler do một hạt tán xạ từ chùm một và chùm hai được cho bởi:"))
    b.append(eq("ν<sub>D1</sub> = ν<sub>01</sub> + (<b>u</b> ⁄ λ) · (r̂ − Ŝ<sub>1</sub>) ; "
                "&nbsp;&nbsp; ν<sub>D2</sub> = ν<sub>02</sub> + (<b>u</b> ⁄ λ) · "
                "(r̂ − Ŝ<sub>2</sub>)", "29.65"))
    b.append(p(
        "trong đó ν<sub>01</sub> và ν<sub>02</sub> là tần số của chùm laser 1 và chùm laser 2; r̂ là "
        "vectơ đơn vị hướng từ vùng đo tới quang học thu; Ŝ<sub>1</sub> và Ŝ<sub>2</sub> là các "
        "vectơ đơn vị theo hướng của chùm tới 1 và chùm tới 2; <b>u</b> là vectơ vận tốc của hạt "
        "(tâm tán xạ); và λ là bước sóng ánh sáng. Tần số của tín hiệu tổng (ngoại sai) ra khỏi hệ "
        "đầu dò quang được cho bởi hiệu giữa ν<sub>D1</sub> và ν<sub>D2</sub>."))
    b.append(eq("f<sub>D</sub> = f<sub>S</sub> + (<b>u</b> ⁄ λ) · (Ŝ<sub>2</sub> − Ŝ<sub>1</sub>)",
                "29.66"))
    b.append(p(
        "trong đó f<sub>S</sub> = ν<sub>01</sub> − ν<sub>02</sub> là hiệu tần số giữa hai chùm tới. "
        "Hiệu tần số này thường được áp đặt có chủ ý (xem phần dịch tần) để cho phép đo không nhập "
        "nhằng chiều dòng và cường độ rối cao. Giả thiết f<sub>S</sub> = 0, tần số mà đầu dò quang "
        "phát hiện là:"))
    b.append(eq("f<sub>D</sub> = (<b>u</b> ⁄ λ) · (Ŝ<sub>2</sub> − Ŝ<sub>1</sub>) = "
                "2u<sub>y</sub> sin κ", "29.67"))
    b.append(p("Do đó,"))
    b.append(eq("u<sub>y</sub> = f<sub>D</sub> λ ⁄ (2 sin κ) = f<sub>D</sub> d<sub>f</sub>", "29.68"))
    b.append(p(
        "Đây là phương trình cho u<sub>y</sub> và cho thấy tần số tín hiệu f<sub>D</sub> tỉ lệ trực "
        "tiếp với vận tốc u<sub>y</sub>. Việc trộn ngoại sai ánh sáng tán xạ từ hai chùm laser tại "
        "đầu dò quang thực ra cho cả tần số tổng lẫn tần số hiệu. Tuy nhiên, tần số tổng quá cao để "
        "có thể phát hiện, nên chỉ tần số hiệu (ν<sub>D1</sub> − ν<sub>D2</sub>) được đưa ra khỏi "
        "đầu dò quang dưới dạng tín hiệu điện. Tần số f<sub>D</sub> thường được gọi là tần số "
        "Doppler của tín hiệu ra, và tín hiệu ra được gọi là tín hiệu Doppler."))
    b.append(note(
        "<b>Ghi chú của người dịch.</b> Phương trình 29.67 chỉ đúng khi hình chiếu của vectơ vận tốc "
        "lên phương vuông góc với các vân được lấy là u<sub>y</sub>: số hạng (<b>u</b> ⁄ λ) · "
        "(Ŝ<sub>2</sub> − Ŝ<sub>1</sub>) là một tích vô hướng, và nó chỉ rút về 2u<sub>y</sub> sin κ "
        "khi thành phần vận tốc theo phương của các chùm tới bị triệt tiêu. Trong bản gốc, các vectơ "
        "đơn vị được in bằng chữ có dấu mũ và vectơ vận tốc bằng chữ có mũi tên; ở đây chúng tôi "
        "giữ dấu mũ cho các vectơ đơn vị và dùng chữ in đậm cho vectơ vận tốc."))
    b.append(p(
        "Có thể thấy từ phương trình 29.68 rằng tần số Doppler không phụ thuộc vào vị trí bộ thu "
        "(r̂). Vì vậy có thể chọn vị trí hệ thu dựa trên các yếu tố như cường độ tín hiệu, dễ căn "
        "chỉnh và khả năng tiếp cận rõ ràng tới vùng đo. Các biểu thức cho những cấu hình quang học "
        "khác cũng có thể được rút gọn tương tự [29], cho cùng một phương trình của tần số dịch "
        "Doppler f<sub>D</sub>. Cần lưu ý rằng mô tả bằng vân không liên quan tới “dịch Doppler” và "
        "trên thực tế không phải lúc nào cũng thích hợp. Mô hình vân thì tiện lợi và cho biểu thức "
        "đúng của tần số. Tuy nhiên, nó có thể gây nhầm lẫn khi khảo sát chi tiết tín hiệu Doppler "
        "(ví dụ tỉ số tín hiệu trên nhiễu) và các tham số quan trọng khác, ví dụ độ sâu điều biến "
        "hay độ rõ (V̄) của tín hiệu [30]."))
    b.append(p(
        "Thời gian hạt đi qua vùng đo được gọi là thời gian đi qua, thời gian lưu trú hay tổng thời "
        "gian chùm, t<sub>B</sub>, và tương ứng với độ dài của tín hiệu ánh sáng tán xạ. Số chu kỳ "
        "(N) trong tín hiệu (bằng số vân mà hạt đi qua) bằng tích của thời gian đi qua "
        "(t<sub>B</sub>) và tần số (f<sub>D</sub>) của tín hiệu."))
    b.append(p(
        "Cũng cần lưu ý rằng khoảng vân (d<sub>f</sub>) chỉ phụ thuộc vào bước sóng của ánh sáng "
        "laser (λ) và góc (2κ) giữa hai chùm. Có thể chứng minh rằng ảnh hưởng của chiết suất chất "
        "lưu lên hai đại lượng này có xu hướng triệt tiêu lẫn nhau, và do đó giá trị của khoảng vân "
        "không phụ thuộc vào môi trường chất lưu [31]. Các giá trị của λ và κ đã biết với mọi hệ hai "
        "chùm tia, nên không cần hiệu chuẩn vận tốc thực tế. Trong một số trường hợp, người ta đã "
        "hiệu chuẩn vận tốc thực tế bằng vành của một bánh xe quay được điều khiển chính xác, để "
        "khắc phục các sai số khi đo chính xác góc giữa hai chùm."))
    b.append(p(
        "Phân bố cường độ trong một chùm laser làm việc ở mode TEM<sub>00</sub> là phân bố "
        "Gauss [32]. Dùng lý thuyết sóng và giả thiết quang học giới hạn nhiễu xạ, có thể định nghĩa "
        "đường kính hiệu dụng của chùm laser và kích thước của vùng đo. Cách tiếp cận thông thường "
        "để định nghĩa đường kính chùm laser và các kích thước của vùng đo dựa trên các vị trí mà "
        "tại đó cường độ sáng bằng 1/e² cường độ cực đại (tại tâm chùm). Cách định nghĩa này tương "
        "tự cách định nghĩa độ dày lớp biên. Các kích thước d<sub>m</sub> và l<sub>m</sub> của vùng "
        "đo hình elipxoit (Hình 29.25) dựa trên tiêu chí 1/e² và được cho bởi:"))
    b.append(eq("d<sub>m</sub> = 4 f λ ⁄ (π D<sub>e−2</sub>) ; &nbsp; l<sub>m</sub> = "
                "d<sub>m</sub> ⁄ tan κ ; &nbsp; N<sub>FR</sub> = d<sub>m</sub> ⁄ d<sub>f</sub>",
                "29.69"))
    b.append(p(
        "N<sub>FR</sub> là số vân cực đại trong vùng đo hình elipxoit. Lưu ý rằng khi giá trị "
        "D<sub>e−2</sub> tăng, vùng đo trở nên nhỏ hơn. Trong các ứng dụng đo dòng, quan hệ này được "
        "khai thác để đạt được kích thước mong muốn của vùng đo."))
    b.append(fig(25, F.FIGS[24], "vi"))
    b.append(p(
        "Các tham số vùng đo cho tình huống ví dụ sau là bước sóng λ = 514,5 nm (vạch lục của laser "
        "argon-ion), D<sub>e−2</sub> = 1,1 mm, d = 35 mm và f = 250 mm. Khi đó κ = 4°, "
        "d<sub>m</sub> = 149 µm và l<sub>m</sub> = 2,13 mm. Khoảng vân d<sub>f</sub> là 3,67 µm và "
        "số vân cực đại (N<sub>FR</sub>) trong vùng đo (số chu kỳ trong một chùm tín hiệu ứng với "
        "một hạt đi qua tâm vùng đo theo phương y) là 40. Xét một hạt đi qua tâm vùng đo với vận "
        "tốc (vuông góc với các vân) 15 m s⁻¹. Nó sẽ tạo ra một tín hiệu có tần số khoảng "
        "4,087 MHz. Thời gian đi qua của hạt (bằng độ dài của tín hiệu) sẽ xấp xỉ 9,93 µs."))

    b.append(h3("Dịch tần", "Frequency Shifting"))
    b.append(p(
        "Sự có mặt của cường độ rối cao và các vùng dòng hồi lưu hay dao động là phổ biến trong hầu "
        "hết các tình huống đo dòng. Trong mô tả bằng mô hình vân và bằng dịch Doppler (với "
        "f<sub>S</sub> = 0) của hệ hai chùm tia, tín hiệu Doppler không cho biết ảnh hưởng của dấu "
        "(dương hay âm) của vận tốc. Hơn nữa, một hạt đi qua vùng đo song song với các vân sẽ không "
        "cắt vân nào, và do đó không tạo ra tín hiệu có dạng chu kỳ, dẫn tới việc không đo được "
        "thành phần vận tốc pháp tuyến (với các vân) bằng không. Ngoài ra, phần cứng xử lý tín hiệu "
        "dùng để trích thông tin tần số thường đòi hỏi tín hiệu phải có một số chu kỳ tối thiểu. "
        "Điều này, cũng như khả năng đo dòng đảo chiều, đạt được nhờ một phương pháp dịch tần số "
        "gọi là <b>dịch tần</b>. Dịch tần cũng được dùng để đo các thành phần vận tốc nhỏ vuông góc "
        "với hướng dòng chủ đạo và để tăng dải đo vận tốc hiệu dụng của các bộ xử lý tín hiệu [31]."))
    b.append(p(
        "Bằng cách đưa một độ lệch pha hay lệch tần (f<sub>s</sub>) vào một trong hai chùm của hệ "
        "hai chùm tia, có thể giải quyết được sự nhập nhằng về chiều. Theo quan điểm mô hình vân, "
        "tình huống này tương ứng với một hệ vân đang chuyển động (thay vì đứng yên). Một hạt đứng "
        "yên trong vùng đo sẽ cho một tín hiệu liên tục ở đầu ra đầu dò quang, có tần số bằng hiệu "
        "tần số f<sub>s</sub> giữa hai chùm tới. Nói cách khác, như trên Hình 29.26(b), đường tuyến "
        "tính giữa vận tốc và tần số được dịch theo chiều tần số dương một lượng bằng dịch tần "
        "f<sub>s</sub>. Chuyển động của hạt theo chiều ngược với chiều chuyển động của vân sẽ làm "
        "tăng tần số tín hiệu, còn chuyển động của hạt theo chiều chuyển động của vân sẽ làm giảm "
        "tần số. Để tạo ra tín hiệu có đủ số chu kỳ ngay cả khi đo vận tốc âm (ví dụ dòng đảo chiều, "
        "dòng hồi lưu), người ta thường dùng một quy tắc kinh nghiệm để chọn dịch tần. Cách làm là "
        "chọn dịch tần (f<sub>s</sub> ≈ 2u<sub>max</sub>/d<sub>f</sub>) xấp xỉ hai lần tần số ứng "
        "với độ lớn của vận tốc âm cực đại (u<sub>max</sub>) dự kiến trong dòng. Điều này cho xác "
        "suất đo gần như bằng nhau với mọi quỹ đạo hạt qua vùng đo [33, 34]."))
    b.append(p(
        "Dịch tần thường đạt được bằng cách cho chùm laser đi qua một tế bào Bragg (Hình "
        "29.26(a)), được điều khiển bởi một dao động ngoài [35]. Thông thường, sự lan truyền của "
        "sóng âm 40 MHz (do tần số điều khiển 40 MHz tạo ra) trong tế bào làm ảnh hưởng tới chùm đi "
        "qua tế bào, tạo ra một dịch tần 40 MHz cho chùm đó. Bằng cách điều chỉnh thích hợp góc của "
        "tế bào so với chùm tới và chặn các chùm không mong muốn, có thể thu lại tới khoảng 80 % "
        "cường độ sáng vào trong chùm đã dịch tần. Cách dùng tế bào Bragg cho một dịch tần 40 MHz "
        "trong tín hiệu ra của đầu dò quang. Để cải thiện độ phân giải đo của bộ xử lý tín hiệu, "
        "tín hiệu đầu dò quang thu được thường được “hạ tần” để có một dịch tần thích hợp hơn (dựa "
        "trên giá trị dịch theo quy tắc kinh nghiệm) cho các vận tốc dòng đang đo. Dịch tần dùng "
        "hai tế bào Bragg (mỗi chùm một tế bào) làm việc ở các tần số khác nhau thì hấp dẫn với các "
        "hệ có băng thông đầu dò quang bị hạn chế. Tuy nhiên, việc phải điều chỉnh lại chỗ giao "
        "nhau của hai chùm mỗi khi thay đổi dịch tần khiến cách này (kỹ thuật hai tế bào Bragg) "
        "không hấp dẫn với các ứng dụng cần thay đổi dịch tần [31]."))
    b.append(p(
        "Gần đây hơn, các tế bào Bragg được dùng ở chế độ đa chức năng để tách chùm laser tới thành "
        "hai chùm cường độ bằng nhau, trong đó một chùm có dịch tần 40 MHz. Điều này đạt được bằng "
        "cách điều chỉnh góc tế bào Bragg khác đi. Ngoài tế bào Bragg, cách tử nhiễu xạ quay và các "
        "cách tiếp cận cơ học khác cũng đã được dùng để dịch tần. Tuy nhiên, những hạn chế về tốc "
        "độ quay và các khía cạnh cơ học khác khiến các hệ này bị giới hạn về dải tần [20]. Một số "
        "kỹ thuật dịch tần khác đã được đề xuất cho laser điốt [36, 37]. Vì rất nhiều ứng dụng đo "
        "dòng có các vùng hồi lưu và cường độ rối cao, dịch tần gần như luôn là một phần của hệ LDV "
        "dùng để đo dòng."))
    b.append(fig(26, F.FIGS[25], "vi"))

    b.append(h3("Cường độ tín hiệu", "Signal Strength"))
    b.append(p(
        "Hiểu được ảnh hưởng của các tham số khác nhau của một hệ LDV lên tỉ số tín hiệu trên nhiễu "
        "(SNR) của tín hiệu đầu dò quang sẽ cho ta các phương pháp hay cách tiếp cận để nâng cao "
        "chất lượng tín hiệu và do đó cải thiện hiệu năng của hệ đo. Phương trình cơ bản cho tỉ số "
        "công suất tín hiệu trên công suất nhiễu (SNR) của tín hiệu đầu dò quang có thể viết "
        "là [38]:"))
    b.append(eq("SNR = A<sub>1</sub> (η<sub>q</sub> P<sub>0</sub> ⁄ Δf) [ (D<sub>a</sub> ⁄ "
                "r<sub>a</sub>)(D<sub>e−2</sub> ⁄ f) ]² d<sub>p</sub>² Ḡ V̄²", "29.70"))
    b.append(p(
        "Phương trình 29.70 cho thấy công suất laser cao hơn (P<sub>0</sub>) cho chất lượng tín hiệu "
        "tốt hơn. Hiệu suất lượng tử của đầu dò quang, η<sub>q</sub>, phụ thuộc vào loại đầu dò "
        "quang được dùng và nói chung là cố định. SNR tỉ lệ nghịch với băng thông Δf của tín hiệu "
        "Doppler. Số hạng trong ngoặc liên quan tới các tham số quang học của hệ: “số f” của quang "
        "học thu, D<sub>a</sub>/r<sub>a</sub>, và của quang học phát, D<sub>e−2</sub>/f. Sự phụ "
        "thuộc bình phương của SNR vào các tham số này khiến chúng trở thành lựa chọn hàng đầu để "
        "cải thiện chất lượng tín hiệu và do đó độ chính xác đo. Tiêu cự của thấu kính phát (f) và "
        "thấu kính thu (r<sub>a</sub>) nói chung được quyết định bởi kích thước của cơ sở thí nghiệm "
        "dòng. Dùng các giá trị nhỏ nhất có thể cho chúng sẽ tăng chất lượng tín hiệu. Tỉ số thứ "
        "nhất (D<sub>a</sub> là đường kính thấu kính thu) quyết định lượng ánh sáng tán xạ được "
        "gom, và tỉ số thứ hai quyết định đường kính (và do đó cường độ sáng trong) vùng đo. Ba số "
        "hạng cuối là đường kính d<sub>p</sub> của tâm tán xạ và hai số hạng (độ lợi tán xạ Ḡ, độ rõ "
        "V̄) liên quan tới các tính chất của ánh sáng tán xạ. Chúng cần được đánh giá bằng các "
        "phương trình tán xạ Mie [38] hay lý thuyết Lorentz–Mie tổng quát [39]."))

    b.append(h3("Đo nhiều thành phần vận tốc", "Measuring Multiple Components of Velocity"))
    b.append(p(
        "Cần một cặp chùm laser giao nhau để đo (Hình 29.24) một thành phần vận tốc. Khái niệm này "
        "được mở rộng để đo hai thành phần vận tốc (vuông góc với trục quang) bằng cách dùng hai "
        "cặp chùm có vùng giao nhau chồng lên nhau. Khi ấy, mặt phẳng của mỗi cặp chùm được đặt "
        "vuông góc với mặt phẳng của cặp kia. Cách phổ biến nhất để đo hai thành phần vận tốc là "
        "dùng một nguồn laser có thể phát ra các chùm đa bước sóng, sao cho bước sóng của một cặp "
        "chùm khác với cặp kia. Các tín hiệu Doppler ứng với hai thành phần vận tốc được tách theo "
        "bước sóng [31]."))
    b.append(p(
        "Trong lịch sử, các hệ LDV được lắp ghép từ nhiều môđun quang học khác nhau. Các môđun này "
        "gồm bộ tách chùm, bộ tách màu, bộ quay phân cực và các hệ gom ánh sáng tán xạ. Kích thước "
        "của một hệ môđun như vậy phụ thuộc vào số thành phần vận tốc cần đo."))
    b.append(p(
        "Việc dùng sợi quang cùng các phần tử quang đa chức năng đã làm cho các hệ trở nên gọn hơn, "
        "linh hoạt hơn và dễ thực hiện phép đo hơn. Laser, quang học tạo ra số chùm cần thiết (thông "
        "thường một cặp cho mỗi thành phần vận tốc cần đo), các đầu dò quang và điện tử có thể được "
        "tách khỏi vị trí đo [40]. Các sợi quang mang các chùm laser được tạo ra như vậy được bố trí "
        "trong đầu dò để đạt được hình học chùm mong muốn cho việc đo các thành phần vận tốc. Nhờ "
        "đó, việc lập bản đồ trường dòng chỉ cần di chuyển các đầu dò sợi quang, trong khi phần còn "
        "lại của hệ đứng yên. Để đạt hiệu suất truyền công suất và chất lượng chùm cực đại, người "
        "ta dùng các sợi quang đơn mẫu đặc biệt giữ phân cực cùng các bộ ghép nối chính xác. Trong "
        "hầu hết trường hợp, các đầu dò sợi quang này cũng có một hệ thu và một sợi riêng (đa mẫu) "
        "để gom (theo hướng tán xạ ngược) ánh sáng tán xạ và mang về hệ đầu dò quang."))
    b.append(fig(27, F.FIGS[26], "vi"))
    b.append(p(
        "Sơ đồ bố trí một hệ đầu dò sợi quang để đo một thành phần vận tốc được vẽ trên Hình 29.27. "
        "Trong các ứng dụng đo dòng, các hệ LDV dùng loại đầu dò sợi quang này đã thay thế phần lớn "
        "các hệ môđun trước đây."))
    b.append(p(
        "Cách tốt nhất để đo ba thành phần vận tốc là dùng một bố trí với hai đầu dò [13]. Khi ấy, "
        "trục quang của hệ đo thành phần vận tốc thứ ba (u<sub>x</sub>) vuông góc với trục quang "
        "của hệ hai thành phần. Đáng tiếc là những khó khăn về tiếp cận và/hoặc dịch chuyển thường "
        "khiến bố trí này không thực tế hoặc kém hấp dẫn. Trong hầu hết tình huống thực tế, góc "
        "giữa hai đầu dò được chọn nhỏ hơn 90°. Một bố trí như vậy dùng hai đầu dò sợi quang để đo "
        "đồng thời ba thành phần vận tốc được vẽ trên Hình 29.28."))
    b.append(fig(28, F.FIGS[27], "vi"))

    b.append(h3("Xử lý tín hiệu", "Signal Processing"))
    b.append(h4("Bản chất của tín hiệu", "Nature of the Signal"))
    b.append(p(
        "Mỗi lần một hạt đi qua vùng đo, mức tín hiệu ánh sáng tán xạ (Hình 29.29) đột ngột tăng "
        "lên (“chùm”). Các đặc trưng của tín hiệu chùm là (1) biên độ trong chùm không hằng, (2) chỉ "
        "kéo dài trong một thời gian ngắn, (3) biên độ thay đổi từ chùm này sang chùm khác, (4) có "
        "nhiễu, (5) tần số cao, và (6) đến ngẫu nhiên."))
    b.append(fig(29, F.FIGS[28], "vi"))
    b.append(p(
        "Nhiệm vụ chính của bộ xử lý tín hiệu là trích thông tin tần số từ tín hiệu chùm do một hạt "
        "đi qua vùng đo tạo ra, và cung cấp một đầu ra tương tự hoặc số tỉ lệ với tần số của tín "
        "hiệu. Bản chất đặc thù của các tín hiệu đòi hỏi phải dùng một hệ xử lý tín hiệu riêng để "
        "trích thông tin vận tốc."))
    b.append(p(
        "Nhiều kỹ thuật khác nhau đã được dùng để xử lý tín hiệu Doppler. Các bộ xử lý tín hiệu đã "
        "dựa trên nguyên lý phân tích phổ, bám tần, tương quan photon, đếm tần, biến đổi Fourier và "
        "tự tương quan. Sự tiến hoá của các kỹ thuật xử lý tín hiệu cho thấy sự cải thiện khả năng "
        "xử lý những tình huống đo khó hơn (nói chung là tín hiệu nhiễu hơn), cho phép đo chính xác "
        "hơn và có tốc độ xử lý cao hơn."))
    b.append(p(
        "Dụng cụ truyền thống để đo tần số tín hiệu là máy phân tích phổ. Yêu cầu đo vận tốc của "
        "từng hạt riêng lẻ, và thu được diễn biến thời gian cùng các tính chất khác của dòng, đã "
        "loại bỏ việc dùng các máy phân tích phổ “tiêu chuẩn” [29]. Có thể coi “bộ bám” là một bộ "
        "lọc băng thông cố định “bám theo” tần số Doppler khi vận tốc chất lưu thay đổi. Kỹ thuật "
        "“bám dòng” này làm việc khá tốt ở vận tốc vừa phải và ở nơi nồng độ tâm tán xạ đủ cao để "
        "cho một tín hiệu về cơ bản là liên tục. Tuy nhiên, rất thường xuyên những điều kiện này "
        "không thể đạt được trong các dòng được quan tâm nhất [29]."))
    b.append(p(
        "Khi mức ánh sáng tán xạ rất thấp, đầu ra của đầu dò quang bộc lộ sự có mặt của từng xung "
        "photon riêng lẻ. Bằng cách tương quan các xung photon thực tế từ một đầu dò quang băng "
        "thông rộng, bộ tương quan photon được thiết kế để làm việc trong những tình huống mà cường "
        "độ tín hiệu đạt được rất thấp (SNR thấp). Tuy nhiên, như thường được dùng, nó không thể cho "
        "vận tốc của từng hạt riêng lẻ mà chỉ cho các đại lượng trung bình, như vận tốc trung bình "
        "và cường độ rối."))
    b.append(p(
        "Bộ xử lý kiểu “đếm” được phát triển tiếp theo, và về cơ bản đo thời gian của một số chu kỳ "
        "nhất định (thường là tám) của tín hiệu Doppler. Tuy nó đo vận tốc của từng hạt riêng lẻ, nó "
        "phụ thuộc vào việc đặt hệ số khuếch đại và đặc biệt là các mức ngưỡng một cách cẩn thận để "
        "phân biệt giữa nhiễu nền và tín hiệu chùm. Bộ đếm là bộ xử lý được ưa chuộng trong nhiều "
        "năm, và người ta đã thu được những phép đo xuất sắc [42]. Tuy nhiên, sự phụ thuộc vào kỹ "
        "năng người dùng, khó khăn khi xử lý tín hiệu SNR thấp, khả năng thu được các phép đo sai, "
        "xu hướng bỏ qua tín hiệu từ các hạt nhỏ, và mong muốn đo gần bề mặt cũng như trong các "
        "dòng phức tạp đã dẫn tới nhu cầu về một bộ xử lý tín hiệu tốt hơn."))

    b.append(h4("Xử lý tín hiệu số", "Digital Signal Processing"))
    b.append(p(
        "Bước phát triển mới nhất trong xử lý tín hiệu là ở lĩnh vực các bộ xử lý tín hiệu số. Những "
        "tiến bộ gần đây trong xử lý tín hiệu số tốc độ cao nay cho phép dùng các kỹ thuật này để "
        "trích tần số từ từng chùm Doppler riêng lẻ đủ nhanh để thực sự bám theo dòng khi nồng độ "
        "gieo hạt đủ lớn trong một phạm vi rộng các tình huống đo. Bằng cách số hoá tín hiệu tới và "
        "dùng các thuật toán biến đổi Fourier [43] hay tự tương quan [44], các bộ xử lý số mới này "
        "có thể làm việc với tín hiệu SNR thấp hơn (so với bộ đếm), trong khi nói chung tránh được "
        "các đầu ra dữ liệu sai. Tuy các thiết bị dùng những kỹ thuật này chắc chắn không mới, các "
        "thiết bị tiêu chuẩn không được thiết kế để thực hiện nhanh các phép đo riêng lẻ trên những "
        "tín hiệu chùm nhiễu, ngắn và có biên độ thay đổi — vốn là đặc trưng của các chùm Doppler."))
    b.append(p(
        "Vì vận tốc dòng và do đó tần số tín hiệu thay đổi từ chùm này sang chùm khác, tốc độ lấy "
        "mẫu cần được thay đổi tương ứng. Và vì tần số tín hiệu không biết trước, khả năng lấy mẫu "
        "tối ưu tín hiệu là một trong những thách thức quan trọng nhất trong xử lý tín hiệu số. "
        "Trong một bộ xử lý tín hiệu số, vấn đề quyết định tốc độ lấy mẫu được giải quyết bằng một "
        "bộ phát hiện chùm dùng SNR để nhận biết sự có mặt của tín hiệu [44]. Ngoài ra, bộ phát hiện "
        "chùm cung cấp độ dài và một ước lượng gần đúng tần số của từng tín hiệu chùm. Ước lượng tần "
        "số này được dùng để chọn đầu ra của bộ lấy mẫu (trong nhiều bộ lấy mẫu) đã lấy mẫu tín hiệu "
        "chùm ở tốc độ tối ưu. Bên cạnh việc tối ưu tốc độ lấy mẫu cho từng chùm, thông tin từ bộ "
        "phát hiện chùm còn được dùng để tập trung vào và xử lý phần giữa của chùm, nơi SNR là cực "
        "đại. Các sơ đồ tối ưu này, tiếp theo là xử lý tín hiệu số, cho một đầu ra số chính xác tỉ "
        "lệ với tần số tín hiệu, và do đó với vận tốc chất lưu."))

    b.append(h3("Gieo hạt và các khía cạnh khác", "Seeding and Other Aspects"))
    b.append(p(
        "Hiệu năng của một hệ LDV có thể được cải thiện đáng kể bằng cách tối ưu nguồn tín hiệu — "
        "hạt tán xạ. Phản ứng đầu tiên của nhiều nhà thực nghiệm là dựa vào các hạt vốn có trong "
        "dòng. Có một vài tình huống (ví dụ hệ LDV làm việc theo hướng tán xạ tới để đo dòng nước "
        "hay chất lỏng) mà các hạt vốn có trong dòng đủ về số lượng và kích thước để cho chất lượng "
        "tín hiệu tốt và do đó phép đo tốt. Trong hầu hết tình huống đo dòng, người ta thêm hạt vào "
        "dòng (nói chung gọi là gieo hạt cho dòng) để có đủ số tâm tán xạ thích hợp. Dùng đúng loại "
        "hạt có thể làm chất lượng tín hiệu (SNR) tăng lên nhiều bậc, và do đó có thể có tác động "
        "lớn hơn lên chất lượng tín hiệu so với việc thay đổi bất kỳ bộ phận nào khác của hệ LDV. "
        "Lý tưởng là các hạt gieo phải nổi tự nhiên trong chất lưu, cho cường độ ánh sáng tán xạ "
        "đủ, có nồng độ số đủ lớn và có tính chất đồng nhất từ hạt này sang hạt khác. Tuy lý tưởng "
        "này khó đạt được, người ta đã phát triển được các nguồn hạt và hệ phân phối hạt thoả "
        "đáng [29, 45–47]."))
    b.append(p(
        "Các phép đo LDV dòng bên trong như trong kênh, ống dẫn và buồng cháy khiến các chùm laser "
        "(cũng như ánh sáng tán xạ) phải đi qua các thành trong suốt hay “cửa sổ”. Trong nhiều "
        "trường hợp, cửa sổ phẳng và do đó ảnh hưởng của khúc xạ ánh sáng có thể chỉ là một sự dịch "
        "chuyển đơn giản của vùng đo. Với dòng bên trong có thành cong, mỗi chùm có thể khúc xạ một "
        "lượng khác nhau và vị trí của vùng đo cần được ước lượng cẩn thận [48]. Với dòng bên trong "
        "các mô hình có hình học phức tạp, cần chọn đường tiếp cận của chùm cẩn thận để các chùm "
        "giao nhau ở bên trong. Hơn nữa, để đo gần thành trong một dòng bên trong, cần giảm thiểu "
        "ảnh hưởng khúc xạ của vật liệu thành lên đường đi của chùm. Một trong các cách là dùng một "
        "chất lỏng [49] có cùng chiết suất với vật liệu thành."))

    b.append(h3("Phân tích dữ liệu", "Data Analysis"))
    b.append(p(
        "Vận tốc dòng được “lấy mẫu” bởi hạt đi qua vùng đo, và phép đo vận tốc chỉ thu được khi "
        "tín hiệu Doppler do hạt tạo ra được xử lý và xuất ra thành một điểm dữ liệu bởi bộ xử lý "
        "tín hiệu. Tuy việc lấy trung bình các phép đo để có, ví dụ, vận tốc trung bình có vẻ hợp "
        "lý, phương pháp này cho kết quả sai. Điều này nảy sinh từ việc số hạt đi qua vùng đo trong "
        "một đơn vị thời gian lớn hơn ở vận tốc cao so với ở vận tốc thấp. Trên thực tế có một "
        "tương quan giữa đại lượng được đo (vận tốc) và quá trình lấy mẫu (hạt đến). Do đó, một "
        "phép trung bình đơn giản các điểm dữ liệu sẽ làm lệch giá trị trung bình (và các tham số "
        "thống kê khác) về phía vận tốc cao, và được gọi là <b>thiên lệch vận tốc</b> [50]. Độ lớn "
        "của sai số thiên lệch phụ thuộc vào độ lớn của các biến thiên vận tốc quanh giá trị trung "
        "bình. Nếu các biến thiên vận tốc đủ nhỏ, sai số có thể không đáng kể."))
    b.append(p(
        "Nếu tốc độ dữ liệu thực tế cao đến mức đầu ra về cơ bản mô tả được dòng (diễn biến thời "
        "gian), thì có thể lấy mẫu đầu ra theo các bước thời gian đều. Điều này tương tự thủ tục "
        "thường dùng để lấy mẫu một tín hiệu tương tự liên tục bằng một bộ chuyển đổi A/D. Cách này "
        "cho giá trị đúng cho cả giá trị trung bình lẫn phương sai khi tốc độ dữ liệu đủ cao so với "
        "các tốc độ dựa trên thang vi mô Taylor cho biến thiên thời gian của vận tốc. Đây được gọi "
        "là tình huống <b>mật độ dữ liệu cao</b> [29]."))
    b.append(p(
        "Trong nhiều tình huống đo thực tế, tốc độ dữ liệu không đủ cao (mật độ dữ liệu thấp) để "
        "thực sự mô tả được dòng. Khi ấy, việc lấy mẫu đầu ra của bộ xử lý tín hiệu theo các bước "
        "thời gian đều sẽ không hiệu quả, vì xác suất có được một vận tốc cập nhật (điểm dữ liệu "
        "mới) cao hơn ở vận tốc cao so với vận tốc thấp (thiên lệch vận tốc). Lời giải cho vấn đề "
        "thiên lệch vận tốc là đánh trọng số cho từng phép đo bằng một hệ số tỉ lệ nghịch với xác "
        "suất thực hiện phép đo."))
    b.append(eq("Ū = Σ<sub>j</sub> u<sub>j</sub> τ<sub>Bj</sub> ⁄ Σ<sub>j</sub> τ<sub>Bj</sub>",
                "29.71"))
    b.append(defs([("u<sub>j</sub>", "Vận tốc của hạt j"),
                   ("τ<sub>Bj</sub>", "Thời gian đi qua của hạt j")]))
    b.append(p(
        "Các thủ tục tương tự có thể được dùng để thu được các ước lượng không thiên lệch cho "
        "phương sai và các tính chất thống kê khác của dòng [29]. Các bộ xử lý tín hiệu hiện đại "
        "cung cấp thời gian lưu trú và khoảng thời gian giữa các điểm dữ liệu cùng với dữ liệu vận "
        "tốc. Gould và Loseke [51] đã trình bày so sánh một số cách tiếp cận khác nhau để hiệu chỉnh "
        "thiên lệch. Edwards [52] đã tóm tắt một số loại thiên lệch khác gắn với LDV."))
    b.append(p(
        "Nhiều kỹ thuật khác nhau để thu thông tin phổ của vận tốc dòng từ đầu ra dữ liệu ngẫu nhiên "
        "của các bộ xử lý tín hiệu đã được thử. Mục tiêu của mọi kỹ thuật này là thu được thông tin "
        "phổ chính xác và không thiên lệch ở tần số cao nhất có thể. Ước lượng phổ trực tiếp từ đầu "
        "ra số của các bộ xử lý [53] cho thấy các ước lượng phổ ở tần số cao kém tin cậy hơn. Kỹ "
        "thuật “chia rãnh” [54, 55] — ước lượng tự tương quan của dữ liệu vận tốc (ngẫu nhiên) rồi "
        "biến đổi Fourier — vẫn hấp dẫn từ quan điểm tính toán. Để có ước lượng phổ tin cậy ở tần "
        "số cao, nhiều phương pháp nhằm nội suy các giá trị vận tốc đo được đã được thử. Chúng nói "
        "chung được gọi là các kỹ thuật tái tạo dữ liệu hay tái tạo tín hiệu. Một bài tổng quan [37] "
        "nhấn mạnh sự cần thiết phải hiệu chỉnh thiên lệch vận tốc trong các ước lượng phổ. Bài này "
        "cũng đề cập một số thuật toán tái tạo gần đây và chỉ ra những khó khăn khi tìm ra một cách "
        "tiếp cận dùng chung."))

    b.append(h3("Mở rộng sang đo kích thước hạt", "Extension to Particle Sizing"))
    b.append(p(
        "Trong LDV, tần số của tín hiệu ánh sáng tán xạ cho vận tốc của tâm tán xạ. Việc xử lý ánh "
        "sáng tán xạ để thu thông tin về tâm tán xạ khác ngoài vận tốc luôn là một đề tài được quan "
        "tâm lớn trong chẩn đoán dòng và hạt. Một trong những phát triển hứa hẹn nhất là việc mở "
        "rộng kỹ thuật LDV để đo độ cong bề mặt, và do đó đường kính, của một tâm tán xạ hình "
        "cầu [22]. Cách tiếp cận này (chỉ giới hạn cho hạt hình cầu) dùng thông tin pha của tín hiệu "
        "ánh sáng tán xạ để trích thông tin kích thước. Để có được một quan hệ duy nhất và tốt nhất "
        "là đơn điệu giữa pha của tín hiệu và kích thước của hạt, cần chọn cẩn thận hướng và hình "
        "học (khẩu độ) của hệ gom ánh sáng tán xạ. Trong phần sau, trừ khi có nói khác, các hạt được "
        "giả thiết là hình cầu."))
    b.append(p(
        "Ánh sáng tán xạ bởi một hạt nói chung chứa các đóng góp từ những cơ chế tán xạ khác nhau — "
        "phản xạ, khúc xạ, nhiễu xạ và (các) phản xạ bên trong. Có thể chứng minh rằng bằng cách "
        "chọn vị trí của hệ gom ánh sáng tán xạ, có thể làm cho đóng góp từ một cơ chế tán xạ trội "
        "hơn các cơ chế khác. Mục tiêu trong các phép đo pha Doppler là có được hướng của hệ thu sao "
        "cho ánh sáng tán xạ thu được đến từ một cơ chế tán xạ trội. Mức độ phổ biến của kỹ thuật "
        "được thể hiện qua việc nó được dùng rộng rãi để đo đường kính và vận tốc hạt trong rất "
        "nhiều ứng dụng, đặc biệt trong lĩnh vực phun sương chất lỏng [56]. Kỹ thuật này cũng đã "
        "được dùng để chẩn đoán các trường dòng gắn với quá trình cháy, xâm thực, các quá trình sản "
        "xuất và các dòng hai pha khác."))

    b.append(h3("Nguyên lý hệ pha Doppler", "Phase Doppler System: Principle"))
    b.append(p(
        "Cách tiếp cận pha Doppler, được phác hoạ như một mở rộng của hệ LDV, được Durst và "
        "Zare [57] đề xuất đầu tiên để đo vận tốc và kích thước của các hạt hình cầu. Các hệ pha "
        "Doppler thực tiễn đầu tiên dùng một bộ thu duy nhất được Bachalo và Houser [22] đề xuất."))
    b.append(p(
        "Sơ đồ bố trí một hệ pha Doppler được vẽ trên Hình 29.30(a). Hình này cho thấy một bố trí "
        "hệ thu gom, tách và hội tụ ánh sáng tán xạ lên nhiều đầu dò quang. Nói chung, khẩu độ của "
        "hệ thu được chia thành ba phần và ánh sáng tán xạ gom qua các phần này được hội tụ vào ba "
        "đầu dò quang riêng biệt. Để đơn giản, trên Hình 29.30(a) chỉ vẽ đầu ra của hai đầu dò. Vị "
        "trí không gian khác nhau của các đầu dò (các khẩu độ thu) khiến tín hiệu mà mỗi đầu dò nhận "
        "được có pha hơi khác nhau. Nói chung, hiệu pha giữa các tín hiệu từ các đầu dò được dùng để "
        "thu đường kính của hạt, còn tần số tín hiệu cho vận tốc của hạt."))
    b.append(fig(30, F.FIGS[29], "vi"))
    b.append(h4("Giải thích bằng mô hình vân", "Fringe Model Explanation"))
    b.append(p(
        "Mô hình vân cho một cách tiếp cận dễ và thẳng để đi tới các biểu thức của tần số Doppler và "
        "độ dịch pha do một hạt đi qua vùng đo tạo ra. Khi hạt chuyển động qua các vân trong vùng "
        "đo, nó tán xạ hệ vân (Hình 29.30(b)). Có thể khảo sát độ dịch pha trong các tín hiệu bằng "
        "cách xem hệ vân tán xạ. Nếu hạt tác động như một gương cầu (phản xạ trội) hay một thấu "
        "kính cầu (khúc xạ trội), nó chiếu các vân từ vùng đo ra không gian xung quanh thành những "
        "dải sáng tối phân kỳ, gọi là các vân tán xạ. Các vân tán xạ nhìn trên một màn đặt trước "
        "các bộ thu được vẽ trên Hình 29.30(b). Khoảng cách giữa các vân tán xạ tại mặt phẳng của "
        "bộ thu là s<sub>f</sub>. Hệ thu vẽ trên Hình 29.30(b) có hai khẩu độ. Khoảng cách giữa các "
        "trọng tâm của hai khẩu độ thu là s<sub>r</sub>. Các vân tán xạ chuyển động ngang qua các "
        "bộ thu khi hạt chuyển động trong vùng đo, tạo ra các tín hiệu dao động theo thời gian. Hai "
        "tín hiệu ra của hai đầu dò quang lệch pha nhau một góc bằng s<sub>r</sub>/s<sub>f</sub> lần "
        "360° [31]. Các hạt lớn tạo ra một hệ vân tán xạ có khoảng vân nhỏ hơn (so với hạt nhỏ), "
        "tức là đường kính hạt tỉ lệ nghịch với s<sub>f</sub>, trong khi s<sub>f</sub> tỉ lệ nghịch "
        "với hiệu pha. Như vậy mô hình vân cho thấy đường kính hạt tỉ lệ thuận với hiệu pha. Cũng có "
        "thể thấy rằng độ nhạy (số độ lệch pha trên một micrômét) của hệ pha Doppler có thể được "
        "tăng lên bằng cách tăng khoảng cách (s<sub>r</sub>) giữa các đầu dò."))
    b.append(p(
        "Hệ pha Doppler vẽ ở trên đo hiệu pha giữa hai đầu dò trong hệ thu để thu đường kính hạt. "
        "Điều này dẫn tới hạn chế là giá trị pha cực đại có thể đo được là 2π. Một bố trí ba đầu dò "
        "trong hệ thu được dùng để khắc phục sự nhập nhằng 2π này. Hình 29.31 vẽ bố trí ba đầu dò "
        "(ba khẩu độ). Ánh sáng tán xạ gom qua các khẩu độ 1, 2 và 3 được hội tụ vào các đầu dò 1, "
        "2 và 3. Φ<sub>13</sub> là hiệu pha giữa đầu dò 1 và 3 và cho độ nhạy pha cao hơn nhờ khoảng "
        "cách giữa chúng lớn hơn so với giữa đầu dò 1 và 2. Khi Φ<sub>13</sub> vượt quá 2π, giá trị "
        "của Φ<sub>12</sub> vẫn dưới 360° và được dùng để theo dõi Φ<sub>13</sub>. Cần lưu ý rằng "
        "cách tiếp cận đơn giản theo tán xạ hình học cho một quan hệ tuyến tính giữa hiệu pha và "
        "đường kính của hạt."))
    b.append(fig(31, F.FIGS[30], "vi"))
    b.append(p(
        "Người ta đã chỉ ra rằng các sai số đáng kể trong kích thước đo được có thể xuất hiện do "
        "tán xạ phụ thuộc quỹ đạo [58]. Có thể giảm thiểu các sai số này bằng cách chọn cấu hình "
        "quang học thích hợp cho hệ pha Doppler [59]. Một kỹ thuật kiểm chứng dựa trên cường độ "
        "cũng đã được đề xuất để giảm sai số [60]."))
    b.append(p(
        "Để khảo sát các giới hạn vật lý cơ bản về khả năng áp dụng của kỹ thuật pha Doppler, một mô "
        "hình chặt chẽ dựa trên lý thuyết điện từ của ánh sáng đã được phát triển. Naqwi và "
        "Durst [61] cũng đã trình bày các kết quả tính toán dựa trên tán xạ Mie, so sánh với cách "
        "tiếp cận tán xạ hình học và các hạn chế của nó. Những kết quả này cung cấp một cách tiếp "
        "cận hệ thống để phát triển các giải pháp mới cho các bài toán đo kích thước hạt. Một cách "
        "tiếp cận mới (bố trí PLANAR) để đạt độ phân giải đo cao đã cho khả năng mở rộng dải đo tới "
        "các hạt dưới micrômét. Hệ đo vận tốc pha Doppler thích nghi (APV) [59] dùng bố trí này sử "
        "dụng một hệ gom ánh sáng tán xạ với các bộ thu độc lập. Trong hệ APV, khoảng cách giữa các "
        "đầu dò có thể chọn được và không phụ thuộc vào khẩu độ số của hệ thu. Một hệ như vậy đã "
        "được dùng để đo các giọt dưới micrômét trong một vòi phun tĩnh điện [62]. Bằng cách tích "
        "hợp một hệ đo vận tốc pha Doppler với một hệ khúc xạ kế cầu vồng, có thể xác định được vận "
        "tốc, kích thước và chiết suất của một giọt [63]."))
    b.append(p(
        "Thông tin vận tốc và đường kính thu được bằng cách xử lý các tín hiệu ra của đầu dò quang. "
        "Tần số của tín hiệu ra đầu dò quang cho thông tin vận tốc. Nói chung, hệ xử lý tín hiệu "
        "cho các phép đo vận tốc được mở rộng để đo hiệu pha giữa hai tín hiệu đầu dò quang. Các "
        "cách tiếp cận xử lý tín hiệu số mô tả ở trên đã được bổ sung bằng việc thêm các kỹ thuật đo "
        "pha chính xác [64, 65]."))
    b.append(p(
        "Tuy kỹ thuật pha Doppler chỉ giới hạn cho hạt hình cầu, luôn có mối quan tâm mở rộng kỹ "
        "thuật này sang các hạt không cầu. Trước đây, người ta đã dùng các phép kiểm tra đối "
        "xứng [66] và các kỹ thuật tương tự để kiểm tra tính cầu của hạt. Một cách tiếp cận “hình "
        "cầu tương đương” đã được dùng để mô tả các hạt không cầu này. Đo kích thước các hạt không "
        "đều là một bài toán phức tạp hơn vì khái niệm bán kính cong cục bộ không còn ý nghĩa trong "
        "những trường hợp này. Một cách tiếp cận mô hình hoá ngẫu nhiên mới đã được dùng để nghiên "
        "cứu các hạt không đều bằng một hệ pha Doppler [67]."))

    b.append(h3("Kết luận", "Conclusion"))
    b.append(p(
        "LDV đã trở thành kỹ thuật được ưa chuộng để đo vận tốc dòng trong một phạm vi rộng các ứng "
        "dụng. Khả năng đo vận tốc một cách không xâm nhập, không cần hiệu chuẩn, của bất kỳ chất "
        "lưu trong suốt đang chảy nào đã khiến nó hấp dẫn để đo gần như mọi loại dòng. Phép đo vận "
        "tốc của các bề mặt chuyển động bằng LDV được dùng để giám sát và điều khiển các quá trình "
        "công nghiệp. Việc dùng laser điốt, sợi quang cùng những tiến bộ trong xử lý tín hiệu và "
        "phân tích dữ liệu đang làm giảm cả chi phí lẫn độ phức tạp của các hệ đo. Việc mở rộng LDV "
        "sang kỹ thuật pha Doppler cho một phương pháp không tiếp xúc hấp dẫn để đo kích thước và "
        "vận tốc của các hạt hình cầu. Những phát triển gần đây của kỹ thuật pha Doppler đã tạo ra "
        "một phương pháp đo kích thước cả các hạt dưới micrômét. Những ý tưởng này cũng đã được mở "
        "rộng để khảo sát các hạt không đều."))

    b.append(h3("Lời cảm ơn", "Acknowledgments"))
    b.append(p(
        "Những đóng góp và nhận xét của TS. L. M. Fingerson và TS. A. Naqwi thuộc TSI Inc. là vô "
        "cùng quý giá trong quá trình chuẩn bị phần này của chương. Tác giả chân thành biết ơn sự "
        "giúp đỡ của họ."))

    b.append(h3("Tài liệu tham khảo", "References"))
    # The numbers live inside the strings, so this must be a <br>-separated block
    # rather than an <ol>: an ordered list would print "1. 1. R. Schodl".
    b.append(wl(_refs293("vi")))
    b.append(h3("Đọc thêm", "Further Information"))
    b.append(wl(_refs293b("vi")))
    return "".join(b)


def sec_29_3_en():
    b = []
    b.append(h2("29.3 Laser Anemometry"))
    b.append(p("Rajan K. Menon — TSI Inc."))

    b.append(p(
        "Laser anemometry, or laser velocimetry, refers to any technique that uses lasers to measure "
        "velocity. The most common approach uses the Doppler shift principle to measure the velocity "
        "of a flowing fluid at a point, and is referred to as Laser Doppler Velocimetry (LDV) or "
        "Laser Doppler Anemometry (LDA). This technique — also known as the dual-beam, differential "
        "Doppler or fringe mode technique — incorporates intersecting (focused) laser beams, and is "
        "also used to measure the motion of surfaces [1]. In some special flow situations another "
        "approach, using two non-intersecting focused laser beams and known as the dual-focus (L2F) "
        "technique, is used to measure flow velocity at a point [2]. More recently, laser "
        "illumination by light sheets has been used for global flow measurements under the name "
        "particle image velocimetry (PIV) [3]. The strength of PIV (including particle tracking "
        "velocimetry) lies in its ability to capture turbulence structures within the flow and "
        "transient phenomena, and to examine unsteady flows [4]. Developing the technique to obtain "
        "both spatial and temporal information about flow fields is making it a powerful diagnostic "
        "tool in fluid mechanics research [5, 6]. Other approaches to measuring global flow "
        "velocities come under the category of molecular tagging velocimetry [7] or Doppler global "
        "velocimetry [8, 9]."))
    b.append(p(
        "The non-invasive nature of the LDV technique, and its ability to make accurate velocity "
        "measurements with high spatial and temporal resolution even in highly turbulent flows, have "
        "led to the widespread use of LDV for flow measurement. Flow velocities ranging from "
        "micrometres per second to hypersonic speeds have been measured with LDV systems. "
        "Measurements of highly turbulent flows [10], flows in rotating machinery [11], especially "
        "in the interblade region of rotors [12, 13], very high [14] or very low [15] velocity "
        "flows, flows at high temperatures [16] and in other hostile environments [17, 18], and "
        "flows in small spaces [19] have been performed with the LDV technique. The versatility of "
        "the approach, and its widespread use for measuring flows accurately, has resulted in the "
        "technique being called laser velocimetry or laser anemometry. Many details of the "
        "technique, including some of the early development of the hardware, are given in the book "
        "by Durst [20]. A bibliography of the landmark papers in LDV has been compiled by "
        "Adrian [21]."))
    b.append(p(
        "For the case of spherical scatterers the technique has also been extended to measure the "
        "size of these particles. Here the scattered light signal from a suitably placed receiver "
        "system is processed to obtain the diameter of the particle, using the phase Doppler "
        "technique [22]."))
    b.append(p(
        "The first reported fluid flow measurements using LDV principles were by Yeh and "
        "Cummins [23]. Although in that case an optical arrangement referred to as the reference "
        "beam system was used to measure the Doppler shift, in almost all measurement applications "
        "the dual-beam or differential Doppler arrangement [24] is used now. This arrangement, also "
        "referred to as the “fringe” mode of operation, uses two intersecting laser beams (Figure "
        "29.24) to measure one velocity component. The advantages of the LDV technique in measuring "
        "flows include (1) a small measuring region (that is, point measurement), (2) high "
        "measurement accuracy, (3) the ability to measure any desired velocity component, (4) "
        "accurate measurement of high turbulence intensities, including flow reversals, (5) a large "
        "dynamic range, (6) no required velocity calibration, (7) no probe in the flow (it does not "
        "disturb the flow, and measures in hostile environments), and (8) good frequency response."))
    b.append(fig(24, F.FIGS[23], "en"))
    b.append(p(
        "The LDV technique relies on the light scattered by scattering centres in the fluid to "
        "measure flow velocity. These scattering centres will also be referred to as particles, "
        "with the understanding that bubbles or anything else whose refractive index differs from "
        "that of the fluid could be the source of scattered light. The particles, whose velocities "
        "are measured, must be small enough (generally in the micrometre range) to follow the flow "
        "variations and large enough to provide signal strength adequate for the signal processor to "
        "give velocity measurements. It should be noted that the signal exists only when a "
        "“detectable” particle is in the measuring volume and is therefore discontinuous. This, "
        "along with other properties of the signal, adds special requirements on the signal "
        "processing and the subsequent data analysis systems. The scattered light signal is "
        "processed to obtain the Doppler shift frequency and from that the velocity of the particle. "
        "Hence the rate at which velocity measurements are made depends on the rate of particle "
        "arrival. It is desirable to have a high particle concentration to obtain a nearly "
        "continuous update of velocity. In carefully controlled experiments the LDV system can "
        "provide very high accuracy (0.1 % or better) in mean velocity. Thermal anemometer systems "
        "are generally able to measure lower turbulence levels than an LDV system [25]. While the "
        "direct measurement of the Doppler-shifted frequency from a single laser beam caused by a "
        "moving particle is possible [26], most LDV systems employ the heterodyne principle to "
        "obtain and process only the Doppler shift (difference) frequency."))

    b.append(h3("Principle of Operation"))
    b.append(h4("Dual-Beam Approach"))
    b.append(p(
        "The dual-beam approach is the most common optical arrangement used in LDV systems for flow "
        "measurement. The schematic (Figure 29.24) shows the basic components of a complete LDV "
        "system for measuring one component of velocity. The transmitting optics include an optical "
        "element to split the original laser beam into two parallel beams and a lens system to focus "
        "and cross the two beams. The intersection region of the two beams becomes the measuring "
        "region. The receiving optics (shown set up in the forward direction) collect a portion of "
        "the light scattered by the particles in the fluid stream passing through the beam-crossing "
        "region (measuring volume) and direct this light to a photodetector, which converts the "
        "scattered light intensity into an analog electrical signal. The frequency of this signal is "
        "proportional to the velocity of the particle. A signal processor extracts the frequency "
        "information from the photodetector output and provides it as a number corresponding to the "
        "instantaneous velocity of the particle. The data processing system obtains the detailed "
        "flow properties from these instantaneous velocity measurements. The idealized photodetector "
        "signal for a particle passing through the centre of the measuring volume is shown in the "
        "lower left of Figure 29.24. Actual signals will have noise superimposed on them, and the "
        "signal shape will vary depending on the particle trajectory through the measuring "
        "volume [27]."))

    b.append(h5("Fringe Model Description"))
    b.append(p(
        "While there are several ways to describe the features of a dual-beam system, the "
        "description based on a fringe model is perhaps the simplest. For simplicity the diameter "
        "and the intensity of both beams are assumed to be the same. After the beams pass through "
        "the transmitting lens, the diameter of each beam continuously decreases to a minimum value "
        "(beam waist) at the focal point of the lens, and then increases again. Thus the beam waists "
        "cross where the two laser beams intersect (at the focal point of the lens), and the "
        "wavefronts in the beams interfere with each other, creating a fringe pattern [28]. In this "
        "pattern, assuming equal-intensity beams and the other needed qualities of the beams, the "
        "light intensity varies from zero (dark fringe) to a maximum (bright fringe), and the "
        "fringes are equally spaced. The particles in the flow passing through the intersection "
        "region (measuring region) scatter light in all directions. An optical system, including a "
        "receiving lens (to collimate the scattered light collected) and a focusing lens, is used to "
        "collect the scattered light and focus it onto the receiver. The aperture in front of the "
        "receiver blocks out stray light and reflections and collects only the light scattered from "
        "the measuring region."))
    b.append(p(
        "As a particle in the flow, with velocity u, moves across the fringes, the intensity pattern "
        "of the light scattered by the particle resembles that shown in the lower left of Figure "
        "29.24. The velocity component u<sub>y</sub> (perpendicular to the optical axis and in the "
        "plane of the incident beams) can be obtained from the ratio of the distance between "
        "fringes (the fringe spacing, d<sub>f</sub>) to the time t (= 1/f<sub>D</sub>) for the "
        "particle to cross one pair of fringes, where f<sub>D</sub> is the frequency of the signal. "
        "The amplitude variation of the signal reflects the Gaussian intensity distribution across "
        "the laser beam. Collection (receiving) optics for the dual-beam system can be placed at any "
        "angle, and the resulting signal from the receiving system will still give the same "
        "frequency. However, signal quality and intensity will vary greatly with the collection "
        "optics angle."))

    b.append(h5("Doppler Shift Explanation"))
    b.append(p(
        "The description of the dual-beam system using the Doppler shift principle is as follows. At "
        "the receiver, the frequencies of the Doppler-shifted light scattered by a particle from "
        "beam one and beam two are given by:"))
    b.append(eq("ν<sub>D1</sub> = ν<sub>01</sub> + (<b>u</b> ⁄ λ) · (r̂ − Ŝ<sub>1</sub>) ; "
                "&nbsp;&nbsp; ν<sub>D2</sub> = ν<sub>02</sub> + (<b>u</b> ⁄ λ) · "
                "(r̂ − Ŝ<sub>2</sub>)", "29.65"))
    b.append(p(
        "where ν<sub>01</sub> and ν<sub>02</sub> are the frequencies of laser beam 1 and laser beam "
        "2; r̂ is the unit vector directed from the measuring volume to the receiving optics; "
        "Ŝ<sub>1</sub> and Ŝ<sub>2</sub> are the unit vectors in the direction of incident beam 1 "
        "and incident beam 2; <b>u</b> is the velocity vector of the particle (scattering centre); "
        "and λ is the wavelength of light. The frequency of the net (heterodyne) signal output from "
        "the photodetector system is given by the difference between ν<sub>D1</sub> and "
        "ν<sub>D2</sub>."))
    b.append(eq("f<sub>D</sub> = f<sub>S</sub> + (<b>u</b> ⁄ λ) · (Ŝ<sub>2</sub> − Ŝ<sub>1</sub>)",
                "29.66"))
    b.append(p(
        "where f<sub>S</sub> = ν<sub>01</sub> − ν<sub>02</sub> is the difference in frequency "
        "between the two incident beams. This difference frequency is often intentionally imposed "
        "(see the section on frequency shifting) to permit unambiguous measurement of flow direction "
        "and high turbulence intensities. Assuming f<sub>S</sub> = 0, the frequency detected by the "
        "photodetector is:"))
    b.append(eq("f<sub>D</sub> = (<b>u</b> ⁄ λ) · (Ŝ<sub>2</sub> − Ŝ<sub>1</sub>) = "
                "2u<sub>y</sub> sin κ", "29.67"))
    b.append(p("Hence,"))
    b.append(eq("u<sub>y</sub> = f<sub>D</sub> λ ⁄ (2 sin κ) = f<sub>D</sub> d<sub>f</sub>", "29.68"))
    b.append(p(
        "This is the equation for u<sub>y</sub>, and it shows that the signal frequency "
        "f<sub>D</sub> is directly proportional to the velocity u<sub>y</sub>. The heterodyning of "
        "the scattered light from the two laser beams at the photodetector actually gives both the "
        "sum and the difference frequency. However, the sum frequency is too high to be detected, so "
        "only the difference frequency (ν<sub>D1</sub> − ν<sub>D2</sub>) is output from the "
        "photodetector as an electrical signal. The frequency f<sub>D</sub> is often referred to as "
        "the Doppler frequency of the output signal, and the output signal as the Doppler signal."))
    b.append(note(
        "<b>Translator's note.</b> Equation 29.67 holds only when the velocity component taken is "
        "the one normal to the fringes: the term (<b>u</b> ⁄ λ) · (Ŝ<sub>2</sub> − Ŝ<sub>1</sub>) "
        "is a scalar product, and it reduces to 2u<sub>y</sub> sin κ only when the component along "
        "the incident beams vanishes. In the source the unit vectors are printed with a hat and the "
        "velocity vector with an arrow above it; here the hats are kept for the unit vectors and the "
        "velocity vector is set in bold."))
    b.append(p(
        "It can be seen from Equation 29.68 that the Doppler frequency is independent of the "
        "receiver location (r̂). Hence the receiver system location can be chosen on grounds such as "
        "signal strength, ease of alignment, and clear access to the measuring region. The "
        "expressions for the other optical configurations can be reduced similarly [29], giving the "
        "identical equation for the Doppler shift frequency f<sub>D</sub>. It should be noted that "
        "the fringe description does not involve a “Doppler shift” and is in fact not always "
        "appropriate. The fringe model is convenient and gives the correct expression for the "
        "frequency. However, it can be misleading when studying the details of the Doppler signal "
        "(for example the signal-to-noise ratio) and other important parameters such as the "
        "modulation depth or visibility (V̄) of the signal [30]."))
    b.append(p(
        "The time taken by the particle to cross the measuring volume is referred to as the transit "
        "time, residence time, or total burst time, t<sub>B</sub>, and corresponds to the duration of "
        "the scattered light signal. The number of cycles (N) in the signal (the same as the number "
        "of fringes the particle crosses) is given by the product of the transit time "
        "(t<sub>B</sub>) and the frequency (f<sub>D</sub>) of the signal."))
    b.append(p(
        "It should also be noted that the fringe spacing (d<sub>f</sub>) depends only on the "
        "wavelength of the laser light (λ) and the angle (2κ) between the two beams. It can be shown "
        "that the effect of the fluid refractive index on these two terms tends to cancel out, and "
        "hence the value of the fringe spacing is independent of the fluid medium [31]. The values "
        "of λ and κ are known for any dual-beam system, and hence an actual velocity calibration is "
        "not needed. In some cases an actual velocity calibration using the rim of a precisely "
        "controlled rotating wheel has been performed, to overcome the errors in measuring "
        "accurately the angle between the beams."))
    b.append(p(
        "The intensity distribution in a laser beam operating in the TEM<sub>00</sub> mode is "
        "Gaussian [32]. Using wave theory and assuming diffraction-limited optics, the effective "
        "diameter of the laser beam and the size of the measurement region can be defined. The "
        "conventional approach to defining laser beam diameter and measuring volume dimensions is "
        "based on the locations where the light intensity is 1/e² of the maximum intensity (at the "
        "centre of the beam). This definition of the dimensions is analogous to that of the boundary "
        "layer thickness. The dimensions d<sub>m</sub> and l<sub>m</sub> of the ellipsoidal measuring "
        "volume (Figure 29.25) are based on the 1/e² criterion and are given by:"))
    b.append(eq("d<sub>m</sub> = 4 f λ ⁄ (π D<sub>e−2</sub>) ; &nbsp; l<sub>m</sub> = "
                "d<sub>m</sub> ⁄ tan κ ; &nbsp; N<sub>FR</sub> = d<sub>m</sub> ⁄ d<sub>f</sub>",
                "29.69"))
    b.append(p(
        "N<sub>FR</sub> is the maximum number of fringes in the ellipsoidal measuring region. Note "
        "that as the value of D<sub>e−2</sub> increases, the measuring volume becomes smaller. In "
        "flow measurement applications this relationship is exploited to arrive at the desired size "
        "of the measuring volume."))
    b.append(fig(25, F.FIGS[24], "en"))
    b.append(p(
        "The measuring volume parameters for the following sample situation are: wavelength λ = "
        "514.5 nm (green line of an argon-ion laser), D<sub>e−2</sub> = 1.1 mm, d = 35 mm and f = "
        "250 mm. Then κ = 4°, d<sub>m</sub> = 149 µm and l<sub>m</sub> = 2.13 mm. The fringe "
        "spacing d<sub>f</sub> is 3.67 µm, and the maximum number (N<sub>FR</sub>) of fringes in the "
        "measuring volume (the number of cycles in a signal burst for a particle going through the "
        "centre of the measuring volume in the y direction) is 40. Consider a particle passing "
        "through the centre of the measuring region with a velocity (normal to the fringes) of "
        "15 m s⁻¹. This would generate a signal with a frequency of about 4.087 MHz. The transit "
        "time of the particle (the same as the duration of the signal) would be approximately "
        "9.93 µs."))

    b.append(h3("Frequency Shifting"))
    b.append(p(
        "The presence of high turbulence intensity and of recirculating or oscillatory flow regions "
        "is common in most flow measuring situations. In the fringe model and the Doppler shift "
        "(with f<sub>S</sub> = 0) descriptions of the dual-beam system, the Doppler signal does not "
        "indicate the influence of the sign (positive or negative) of the velocity. Further, a "
        "particle passing through the measuring volume parallel to the fringes would not cross any "
        "fringes and hence would not generate a signal having the cyclic pattern, resulting in the "
        "inability to measure the zero normal (to the fringes) component of velocity. In addition, "
        "signal processing hardware used to extract the frequency information often requires the "
        "signals to have a minimum number of cycles. This, as well as the ability to measure flow "
        "reversals, is achieved by a method of frequency offsetting referred to as <b>frequency "
        "shifting</b>. Frequency shifting is also used to measure small velocity components "
        "perpendicular to the dominant flow direction and to increase the effective velocity "
        "measuring range of the signal processors [31]."))
    b.append(p(
        "By introducing a phase or frequency offset (f<sub>s</sub>) to one of the two beams in a "
        "dual-beam system, the directional ambiguity can be resolved. From the fringe model "
        "standpoint this situation corresponds to a moving (instead of a stationary) fringe system. "
        "A stationary particle in the measuring volume will provide a continuous signal at the "
        "photodetector output whose frequency equals the difference in frequency, f<sub>s</sub>, "
        "between the two incident beams. In other words, as shown in Figure 29.26(b), the linear "
        "curve between velocity and frequency is offset along the positive frequency direction by an "
        "amount equal to the frequency shift f<sub>s</sub>. Motion of a particle in a direction "
        "opposite to fringe movement would provide an increase in signal frequency, while particle "
        "motion in the direction of fringe motion would provide a decrease in frequency. To create a "
        "signal with an adequate number of cycles even while measuring negative velocities (for "
        "example flow reversals, recirculating flows), a convenient rule-of-thumb approach for "
        "frequency shifting is often used. The approach is to select the frequency shift "
        "(f<sub>s</sub> ≈ 2u<sub>max</sub>/d<sub>f</sub>) to be approximately twice the frequency "
        "corresponding to the magnitude of the maximum negative velocity (u<sub>max</sub>) expected "
        "in the flow. This provides approximately equal probability of measurement for all particle "
        "trajectories through the measuring volume [33, 34]."))
    b.append(p(
        "Frequency shifting is most commonly achieved by sending the laser beam through a Bragg cell "
        "(Figure 29.26(a)) driven by an external oscillator [35]. Typically the propagation of the "
        "40 MHz acoustic wave (created by a 40 MHz drive frequency) inside the cell affects the beam "
        "passing through the cell to yield a frequency shift of 40 MHz for that beam. By properly "
        "adjusting the angle the cell makes with the incoming beam and blocking off the unwanted "
        "beams, up to about 80 % of the input light intensity is recovered in the shifted beam. The "
        "Bragg cell approach provides a 40 MHz frequency shift in the photodetector output signal. To "
        "improve the measurement resolution of the signal processor, the resulting photodetector "
        "signal is often “downmixed” to have a more appropriate frequency shift (based on the "
        "rule-of-thumb shift value) for the flow velocities being measured. Frequency shifting using "
        "two Bragg cells (one for each beam of a dual-beam system) operating at different frequencies "
        "is attractive for systems where the bandwidth of the photodetector is limited. However, the "
        "need to readjust the beam crossing with a change in frequency shift has not made this "
        "approach (the double Bragg cell technique) attractive for applications where the frequency "
        "shift needs to be varied [31]."))
    b.append(p(
        "More recently, Bragg cells have been used in a multifunctional mode to split the incoming "
        "laser beam into two equal-intensity beams, one of them having the 40 MHz frequency shift. "
        "This is accomplished by adjusting the Bragg cell angle differently. In addition to Bragg "
        "cells, rotating diffraction gratings and other mechanical approaches have been used for "
        "frequency shifting. However, limits on rotational speed and other mechanical aspects of "
        "these systems make them limited in frequency range [20]. Other frequency shifting "
        "techniques have been suggested for use with laser diodes [36, 37]. Because so many flow "
        "measurement applications involve recirculating regions and high turbulence intensities, "
        "frequency shifting is almost always a part of an LDV system used for flow measurement."))
    b.append(fig(26, F.FIGS[25], "en"))

    b.append(h3("Signal Strength"))
    b.append(p(
        "Understanding the influence of the various parameters of an LDV system on the "
        "signal-to-noise ratio (SNR) of the photodetector signal provides methods or approaches to "
        "enhance signal quality and hence improve the performance of the measuring system. The basic "
        "equation for the ratio of signal power to noise power (SNR) of the photodetector signal can "
        "be written as [38]:"))
    b.append(eq("SNR = A<sub>1</sub> (η<sub>q</sub> P<sub>0</sub> ⁄ Δf) [ (D<sub>a</sub> ⁄ "
                "r<sub>a</sub>)(D<sub>e−2</sub> ⁄ f) ]² d<sub>p</sub>² Ḡ V̄²", "29.70"))
    b.append(p(
        "Equation 29.70 shows that higher laser power (P<sub>0</sub>) provides better signal quality. "
        "The quantum efficiency of the photodetector, η<sub>q</sub>, depends on the type of "
        "photodetector used and is generally fixed. The SNR is inversely proportional to the "
        "bandwidth Δf of the Doppler signal. The term in brackets relates to the optical parameters "
        "of the system: the “f-number” of the receiving optics, D<sub>a</sub>/r<sub>a</sub>, and of "
        "the transmitting optics, D<sub>e−2</sub>/f. The square dependence of SNR on these parameters "
        "makes them the prime choice for improving signal quality and hence measurement accuracy. The "
        "focal length of the transmitting (f) and receiving (r<sub>a</sub>) lenses is generally "
        "decided by the size of the flow facility. Using the smallest possible values for these "
        "would increase the signal quality. The first ratio (D<sub>a</sub> is the diameter of the "
        "receiving lens) determines the amount of scattered light that is collected, and the second "
        "ratio determines the diameter of (and hence the light intensity in) the measuring volume. "
        "The last three terms are the diameter d<sub>p</sub> of the scattering centre and the two "
        "terms (scattering gain Ḡ, visibility V̄) relating to properties of the scattered light. "
        "These need to be evaluated using the Mie scattering equations [38] or the generalized "
        "Lorentz–Mie theory [39]."))

    b.append(h3("Measuring Multiple Components of Velocity"))
    b.append(p(
        "A pair of intersecting laser beams is needed to measure (Figure 29.24) one component of "
        "velocity. This concept is extended to measure two components of velocity (perpendicular to "
        "the optical axis) by having two pairs of beams with an overlapping intersection region. In "
        "this case the plane of each pair of beams is set orthogonal to that of the other. The most "
        "common approach to measuring two components of velocity is to use a laser source that can "
        "generate multiwavelength beams, so that the wavelength of one pair of beams differs from "
        "that of the other pair. The Doppler signals corresponding to the two components of velocity "
        "are separated by wavelength [31]."))
    b.append(p(
        "Historically, LDV systems were assembled by putting together a variety of optical modules. "
        "These modules included beam splitters, colour separators, polarization rotators and "
        "scattered light collection systems. The size of such a modular system depended on the "
        "number of velocity components to be measured."))
    b.append(p(
        "The use of optical fibres along with multifunctional optical elements has made the systems "
        "more compact, more flexible and easier to use for measurements. The laser, the optics that "
        "generate the necessary number of beams (typically one pair per velocity component to be "
        "measured), the photodetectors and the electronics can be isolated from the measurement "
        "location [40]. The fibres carrying the laser beams thus generated are arranged in the probe "
        "to achieve the desired beam geometry for measuring the velocity components. Hence flow field "
        "mapping is achieved by moving only the fibre-optic probes, while keeping the rest of the "
        "system stationary. To achieve maximum power transmission efficiency and beam quality, "
        "special single-mode, polarization-preserving optical fibres along with precision couplers "
        "are used. In most cases these fibre probes also have a receiving system and a separate "
        "(multimode) fibre to collect the scattered light (in back scatter) and carry it back to the "
        "photodetector system."))
    b.append(fig(27, F.FIGS[26], "en"))
    b.append(p(
        "A schematic arrangement of a fibre probe system for measuring one component of velocity is "
        "shown in Figure 29.27. In flow measurement applications, LDV systems using these types of "
        "fibre-optic probes have largely replaced the earlier modular systems."))
    b.append(p(
        "The best way to make three-component velocity measurements is to use an arrangement with "
        "two probes [13]. In this case the optical axis of the system measuring the third component "
        "of velocity (u<sub>x</sub>) is perpendicular to that of the two-component system. "
        "Unfortunately, access and/or traversing difficulties often make this arrangement "
        "impractical or less attractive. In most practical situations the angle between the two "
        "probes is selected to be less than 90°. Such an arrangement, using two fibre-optic probes to "
        "measure three components of velocity simultaneously, is shown in Figure 29.28."))
    b.append(fig(28, F.FIGS[27], "en"))

    b.append(h3("Signal Processing"))
    b.append(h4("Nature of the Signal"))
    b.append(p(
        "Every time a particle passes through the measuring region, the scattered light signal level "
        "(Figure 29.29) suddenly increases (a “burst”). The characteristics of the burst signal are "
        "(1) the amplitude in the burst is not constant, (2) it lasts for only a short duration, (3) "
        "the amplitude varies from burst to burst, (4) noise is present, (5) the frequency is high, "
        "and (6) the arrival is random."))
    b.append(fig(29, F.FIGS[28], "en"))
    b.append(p(
        "The primary task of the signal processor is to extract the frequency information from the "
        "burst signal generated by a particle passing through the measuring volume, and to provide "
        "an analog or digital output proportional to the frequency of the signal. The unique nature "
        "of the signals demands the use of a special signal processing system to extract the velocity "
        "information."))
    b.append(p(
        "A variety of techniques has been used for processing Doppler signals. Signal processors "
        "have been based on spectrum analysis, frequency tracking, photon correlation, frequency "
        "counting, Fourier transform and autocorrelation principles. The evolution of the signal "
        "processing techniques shows the improvement in their ability to handle more difficult "
        "measuring situations (which generally means noisier signals), to give more accurate "
        "measurements, and to have higher processing speed."))
    b.append(p(
        "The traditional instrument for measuring signal frequency is a spectrum analyzer. The need "
        "to measure individual particle velocities, and to obtain the time history and other "
        "properties of the flow, has eliminated the use of “standard” spectrum analyzers [29]. The "
        "“tracker” can be thought of as a fixed-bandwidth filter that “tracked” the Doppler frequency "
        "as the fluid velocity changed. This technique of “tracking the flow” worked quite well at "
        "modest velocities and where the concentration of scattering centres was high enough to "
        "provide an essentially continuous signal. However, too frequently these conditions could "
        "not be met in the flows of most interest [29]."))
    b.append(p(
        "When the scattered light level is very low, the photodetector output reveals the presence of "
        "individual photon pulses. By correlating the actual photon pulses from a wide-bandwidth "
        "photodetector, the photon correlator was designed to work in situations where the "
        "attainable signal intensity was very low (low SNR). However, as normally used it could not "
        "provide the velocity of individual particles, only averaged quantities such as mean "
        "velocity and turbulence intensity."))
    b.append(p(
        "The “counter” type of processor was developed next, and basically measured the time for a "
        "certain number (typically eight) of cycles of the Doppler signal. Although it measured the "
        "velocity of individual particles, it depended on the careful setting of amplifier gain and, "
        "especially, threshold levels to discriminate between background noise and burst signals. "
        "Counters were the processors of choice for many years, and excellent measurements were "
        "obtained [42]. However, the reliance on user skill, the difficulty in handling low-SNR "
        "signals, the possibility of getting erroneous measurements, the inclination to ignore "
        "signals from small particles, and the desire to make measurements close to surfaces and in "
        "complex flows led to the need for a better signal processor."))

    b.append(h4("Digital Signal Processing"))
    b.append(p(
        "The latest development in signal processing is in the area of digital signal processors. "
        "Recent developments in high-speed digital signal processing now permit the use of these "
        "techniques to extract the frequency from individual Doppler bursts fast enough to actually "
        "follow the flow when the seeding concentration is adequate, in a wide range of measurement "
        "situations. By digitizing the incoming signal and using Fourier transform [43] or "
        "autocorrelation [44] algorithms, these new digital processors can work with lower-SNR "
        "signals (than counters) while generally avoiding erroneous data outputs. While instruments "
        "using these techniques are certainly not new, standard instruments were not designed to "
        "make rapid individual measurements on the noisy, short-duration burst signals with varying "
        "amplitudes that are typical of Doppler bursts."))
    b.append(p(
        "Because the flow velocity, and hence the signal frequency, varies from one burst to the "
        "next, the sampling rate needs to be varied accordingly. And because the signal frequency is "
        "not known a priori, the ability to sample the signal optimally has been one of the most "
        "important challenges in digital signal processing. In one of the digital signal processors "
        "the question of deciding the sample rate is addressed by a burst detector that uses SNR to "
        "identify the presence of a signal [44]. In addition, the burst detector provides the "
        "duration and an approximate estimate of the frequency of each of the burst signals. This "
        "frequency estimate is used to select the output of the sampler (from the many samplers) that "
        "had sampled the burst signal at the optimum rate. Besides optimizing the sample rate for "
        "each burst, the burst detector information is also used to focus on and process the middle "
        "portion of the burst, where the SNR is maximum. These optimization schemes, followed by "
        "digital signal processing, provide an accurate digital output proportional to the signal "
        "frequency, and hence to the fluid velocity."))

    b.append(h3("Seeding and Other Aspects"))
    b.append(p(
        "The performance of an LDV system can be significantly improved by optimizing the source of "
        "the signal, the scattering particle. The first reaction of many experimentalists is to rely "
        "on the particles naturally present in the flow. There are a few situations (for example LDV "
        "systems operating in forward scatter to measure water or liquid flows) where the particles "
        "naturally present in the flow are sufficient in number and size to provide good signal "
        "quality and hence good measurements. In most flow measurement situations, particles are "
        "added to the flow (generally referred to as seeding the flow) to obtain an adequate number "
        "of suitable scatterers. Use of a proper particle can result in orders-of-magnitude increase "
        "in signal quality (SNR), and hence can have a greater impact on signal quality than the "
        "modification of any other component in the LDV system. Ideally the seed particles should be "
        "naturally buoyant in the fluid, provide adequate scattered light intensity, have a large "
        "enough number concentration, and have uniform properties from particle to particle. While "
        "this ideal is difficult to achieve, adequate particle sources and distribution systems have "
        "been developed [29, 45–47]."))
    b.append(p(
        "LDV measurements of internal flows such as those in channels, pipes and combustion chambers "
        "result in the laser beams (as well as the scattered light) going through transparent walls "
        "or “windows”. In many cases the window is flat, and hence the effect of light refraction can "
        "be a simple displacement of the measuring region. In the case of internal flows with curved "
        "walls, each beam can refract by different amounts and the location of the measuring region "
        "needs to be carefully estimated [48]. For internal flows in models with complex geometries, "
        "the beam access needs to be carefully selected so that the beams cross inside. Further, to "
        "make measurements close to the wall in an internal flow, the refraction effect of the wall "
        "material on the beam path needs to be minimized. One of the approaches is to use a liquid "
        "[49] that has the same refractive index as the wall material."))

    b.append(h3("Data Analysis"))
    b.append(p(
        "The flow velocity is “sampled” by the particle passing through the measuring volume, and the "
        "velocity measurement is obtained only when the Doppler signal created by the particle is "
        "processed and output as a data point by the signal processor. While averaging the "
        "measurements to get, for example, the mean velocity would seem reasonable, this method "
        "gives the wrong answer. This arises from the fact that the number of particles going "
        "through the measuring region per unit time is higher at high velocities than at low "
        "velocities. In effect there is a correlation between the measured quantity (velocity) and "
        "the sampling process (particle arrival). Hence a simple average of the data points will bias "
        "the mean value (and other statistical parameters) toward the high-velocity end, and is "
        "referred to as <b>velocity bias</b> [50]. The magnitude of the bias error depends on the "
        "magnitude of the velocity variations about the mean. If the variations in velocity are "
        "sufficiently small, the error might not be significant."))
    b.append(p(
        "If the actual data rate is so high that the output data is essentially able to characterize "
        "the flow (time history), then the output can be sampled at uniform time increments. This is "
        "similar to the procedure normally used for sampling a continuous analog signal with an ADC. "
        "It gives the proper value for both the mean and the variance when the data rate is "
        "sufficiently high compared with the rates based on the Taylor microscale for the temporal "
        "variation of velocity. This is referred to as a <b>high data density</b> situation [29]."))
    b.append(p(
        "In many actual measurement situations the data rate is not high enough (low data density) to "
        "actually characterize the flow. Here, sampling the output of the signal processor at uniform "
        "time increments will not work, because the probability of getting an updated velocity (a new "
        "data point) is higher at high velocity than at low velocity (velocity bias). The solution to "
        "the velocity bias problem is to weight the individual measurements with a factor inversely "
        "proportional to the probability of making the measurement."))
    b.append(eq("Ū = Σ<sub>j</sub> u<sub>j</sub> τ<sub>Bj</sub> ⁄ Σ<sub>j</sub> τ<sub>Bj</sub>",
                "29.71"))
    b.append(defs([("u<sub>j</sub>", "Velocity of particle j"),
                   ("τ<sub>Bj</sub>", "Transit time for particle j")]))
    b.append(p(
        "Similar procedures can be used to obtain unbiased estimators for the variance and other "
        "statistical properties of the flow [29]. Modern signal processors provide the residence "
        "time and the time between data points along with the velocity data. A comparison of some of "
        "the different approaches to bias correction has been presented by Gould and Loseke [51]. "
        "Some of the other types of bias associated with LDV have been summarized by "
        "Edwards [52]."))
    b.append(p(
        "A variety of techniques to obtain spectral information of the flow velocity from the random "
        "data output of the signal processors have been tried. The goal of all these techniques has "
        "been to get accurate and unbiased spectral information at as high a frequency as possible. "
        "Direct spectral estimation from the digital output of the processors [53] shows the spectrum "
        "estimates at high frequency to be less reliable. The “slotting” technique [54, 55] — "
        "estimating the autocorrelation of the (random) velocity data followed by a Fourier "
        "transform — continues to be attractive from a computational standpoint. To obtain reliable "
        "spectrum estimates at high frequencies, a variety of methods aimed at interpolating the "
        "measured velocity values have been attempted. These are generally referred to as data or "
        "signal reconstruction techniques. A review article [37] emphasizes the need to correct for "
        "velocity bias in the spectrum estimates. It also covers some of the recent reconstruction "
        "algorithms and points out the difficulties in coming up with a general-purpose approach."))

    b.append(h3("Extension to Particle Sizing"))
    b.append(p(
        "In LDV the frequency of the scattered light signal provides the velocity of the scatterer. "
        "Processing the scattered light to get information about the scatterer other than velocity "
        "has always been a topic of great interest in flow and particle diagnostics. One of the most "
        "promising developments is the extension of the LDV technique to measure the surface "
        "curvature, and hence the diameter, of a spherical scatterer [22]. This approach (limited to "
        "spherical particles) uses the phase information of the scattered light signal to extract the "
        "size information. To obtain a unique and preferably monotonic relation between the phase of "
        "the signal and the size of the particle, the orientation and the geometry (aperture) of the "
        "scattered light collection system need to be carefully chosen. In the following, unless "
        "otherwise mentioned, the particles are assumed to be spherical."))
    b.append(p(
        "The light scattered by a particle generally contains contributions from the different "
        "scattering mechanisms — reflection, refraction, diffraction and internal reflection(s). It "
        "can be shown that, by selecting the position of the scattered light collection set-up, the "
        "contribution from one scattering mechanism can be made dominant over the others. The aim in "
        "phase Doppler measurements is to have the orientation of the receiver system such that the "
        "scattered light collected comes from one dominant scattering mechanism. The popularity of "
        "the technique is evidenced by its widespread use for measuring particle diameter and "
        "velocity in a large number of applications, especially in the field of liquid sprays [56]. "
        "The technique has also been used in diagnosing flow fields associated with combustion, "
        "cavitation, manufacturing processes and other two-phase flows."))

    b.append(h3("Phase Doppler System: Principle"))
    b.append(p(
        "The phase Doppler approach, outlined as an extension to an LDV system, was first proposed by "
        "Durst and Zare [57] to measure the velocity and size of spherical particles. The first "
        "practical phase Doppler systems using a single receiver were proposed by Bachalo and "
        "Houser [22]."))
    b.append(p(
        "A schematic arrangement of a phase Doppler system is shown in Figure 29.30(a). It shows a "
        "receiver system that collects, separates and focuses the scattered light onto multiple "
        "photodetectors. In general the receiving system aperture is divided into three parts, and "
        "the scattered light collected through these is focused onto three separate photodetectors. "
        "For simplicity, in Figure 29.30(a) the outputs of only two detectors are shown. The "
        "different spatial locations of the detectors (receiving apertures) result in the signals "
        "received by each detector having a slightly different phase. In general the difference in "
        "phase between the signals from the detectors is used to obtain the particle diameter, while "
        "the signal frequency provides the velocity of the particle."))
    b.append(fig(30, F.FIGS[29], "en"))
    b.append(h4("Fringe Model Explanation"))
    b.append(p(
        "The fringe model provides an easy and straightforward approach to arriving at the "
        "expressions for the Doppler frequency and phase shift created by a particle going through "
        "the measuring volume. As the particle moves through the fringes in the measuring volume it "
        "scatters the fringe pattern (Figure 29.30(b)). The phase shift in the signals can be "
        "examined by looking at the scattered fringe pattern. If the particle acts like a spherical "
        "mirror (dominant reflection) or a spherical lens (dominant refraction), it projects fringes "
        "from the measuring volume into space all around as diverging bands of bright and dark light, "
        "known as scattered fringes. Scattered fringes as seen on a screen placed in front of the "
        "receivers are shown in Figure 29.30(b). The spacing between the scattered fringes at the "
        "plane of the receiver is s<sub>f</sub>. The receiver system shown in Figure 29.30(b) has two "
        "apertures. The distance between the centroids of the two receiving apertures is "
        "s<sub>r</sub>. Scattered fringes move across the receivers as the particle moves in the "
        "measuring volume, generating temporally fluctuating signals. The two photodetector output "
        "signals are shifted in phase by s<sub>r</sub>/s<sub>f</sub> times 360° [31]. Large particles "
        "create a scattered fringe pattern with a smaller fringe spacing (compared with that for "
        "small particles), that is, particle diameter is inversely proportional to s<sub>f</sub>, "
        "while s<sub>f</sub> is inversely proportional to the phase difference. Thus the fringe model "
        "shows the particle diameter to be directly proportional to the phase difference. It can "
        "also be seen that the sensitivity (degrees of phase difference per micrometre) of the phase "
        "Doppler system can be increased by increasing the separation (s<sub>r</sub>) between the "
        "detectors."))
    b.append(p(
        "The phase Doppler system shown above measures the phase difference between two detectors in "
        "the receiver system to obtain the particle diameter. This brings in the limitation that the "
        "maximum value of phase that can be measured is 2π. A three-detector arrangement in the "
        "receiver system is used to overcome this 2π ambiguity. Figure 29.31 shows the three-detector "
        "(three-aperture) arrangement. Scattered light collected through apertures 1, 2 and 3 is "
        "focused into detectors 1, 2 and 3. Φ<sub>13</sub> is the phase difference between detectors "
        "1 and 3 and provides the higher phase sensitivity, because of their greater separation "
        "compared with detectors 1 and 2. As Φ<sub>13</sub> exceeds 2π, the value of Φ<sub>12</sub> "
        "is below 360° and is used to keep track of Φ<sub>13</sub>. It should be noted that the "
        "simplified approach in terms of geometrical scattering provides a linear relationship "
        "between the phase difference and the diameter of the particle."))
    b.append(fig(31, F.FIGS[30], "en"))
    b.append(p(
        "It has been pointed out that significant errors in measured size can occur because of "
        "trajectory-dependent scattering [58]. These errors could be minimized by choosing the "
        "appropriate optical configuration of the phase Doppler system [59]. An intensity-based "
        "validation technique has also been proposed to reduce the errors [60]."))
    b.append(p(
        "To explore the fundamental physical limits on the applicability of the phase Doppler "
        "technique, a rigorous model based on the electromagnetic theory of light has been "
        "developed. Computational results based on Mie scattering, and a comparison with the "
        "geometric scattering approach and its limitations, have also been outlined by Naqwi and "
        "Durst [61]. These provided a systematic approach to developing innovative solutions to "
        "particle sizing problems. A new approach (the PLANAR arrangement) to achieve high "
        "measurement resolution provided the ability to extend the measurement range to "
        "submicrometre particles. The Adaptive Phase Doppler Velocimeter (APV) system [59], which "
        "incorporates this layout, uses a scattered light collection system that employs independent "
        "receivers. In the APV system the separation between the detectors is selectable and does "
        "not depend on the numerical aperture of the receiving system. Such a system was used for "
        "measuring submicrometre droplets in an electrospray [62]. By integrating a phase Doppler "
        "velocimeter system with a rainbow refractometer system, the velocity, size and refractive "
        "index of a droplet could be determined [63]."))
    b.append(p(
        "The velocity and diameter information is obtained by processing the photodetector output "
        "signals. The frequency of the photodetector output signal provides the velocity "
        "information. In general the signal processing system for velocity measurements is expanded "
        "to measure the phase difference between two photodetector signals. The digital signal "
        "processing approaches described earlier have been complemented by the addition of accurate "
        "phase measurement techniques [64, 65]."))
    b.append(p(
        "Although the phase Doppler technique is limited to spherical particles, there has always "
        "been an interest in extending it to nonspherical particles. In the past, symmetry checks "
        "[66] and other similar techniques have been used to check the sphericity of particles. An "
        "equivalent-sphere approach has been used to describe these nonspherical particles. Sizing "
        "irregular particles is a more complex problem, because the concept of local radius of "
        "curvature is not meaningful in these cases. An innovative stochastic modelling approach has "
        "been used to study irregular particles with a phase Doppler system [67]."))

    b.append(h3("Conclusion"))
    b.append(p(
        "LDV has become the preferred technique for measuring flow velocity in a wide range of "
        "applications. The ability to measure non-invasively the velocity, without calibration, of "
        "any transparent flowing fluid has made it attractive for measuring almost any type of flow. "
        "Velocity measurement of moving surfaces by LDV is used to monitor and control industrial "
        "processes. The use of laser diodes and fibre optics, and advances in signal processing and "
        "data analysis, are reducing both the cost and the complexity of measuring systems. The "
        "extension of LDV to the phase Doppler technique provides an attractive, non-contact method "
        "for measuring the size and velocity of spherical particles. Recent developments in the "
        "phase Doppler technique have generated a method to size submicrometre particles as well. "
        "These ideas have been extended to examine irregular particles also."))

    b.append(h3("Acknowledgments"))
    b.append(p(
        "The input and comments from Dr. L. M. Fingerson and Dr. A. Naqwi of TSI Inc. have been "
        "extremely valuable in the preparation of this chapter section. The author is sincerely "
        "grateful to them for the help."))

    b.append(h3("References"))
    b.append(wl(_refs293("en")))
    b.append(h3("Further Information"))
    b.append(wl(_refs293b("en")))
    return "".join(b)


SECTIONS_VI = [sec_29_1_vi, sec_29_2_vi, sec_29_3_vi]
SECTIONS_EN = [sec_29_1_en, sec_29_2_en, sec_29_3_en]

SECTIONS = [
    ("29.1", "Đo vận tốc bằng ống Pitot", "Pitot Probe Anemometry"),
    ("29.2", "Đo vận tốc bằng nhiệt", "Thermal Anemometry"),
    ("29.3", "Đo vận tốc bằng laser", "Laser Anemometry"),
]


def sec_index(lang):
    """The in-page jump index. Three sections, but each is long enough to be
    worth jumping between.

    Only the sections that have been written are listed: the module is built up
    one section at a time, and an index entry pointing at an anchor that does
    not exist yet is a broken link.
    """
    vi = lang == "vi"
    n_done = len(SECTIONS_VI if vi else SECTIONS_EN)
    li = []
    for n, tvi, ten in SECTIONS[:n_done]:
        li.append('<li><span class="n">%s</span><span class="t"><a href="#s29-%s">%s</a></span></li>'
                  % (n, n.split(".")[1], tvi if vi else ten))
    return ('<ul class="toc-list sec-index" aria-label="%s">%s</ul>'
            % ("Mục lục trong chương" if vi else "Contents of this chapter", "".join(li)))


def body_vi():
    out = ['<p class="lede">Ba phương pháp đo vận tốc tại một điểm — ống Pitot, đo nhiệt và Doppler '
           'laser — được trình bày trong chương này. Cả ba cùng trả lời một câu hỏi: vận tốc của '
           'chất lưu tại đúng chỗ đặt đầu dò là bao nhiêu. Chúng khác nhau ở dải đo, ở việc có xâm '
           'nhập vào dòng chảy hay không, và ở mức độ can thiệp vào dòng.</p>', sec_index("vi")]
    for f in SECTIONS_VI:
        out.append(f())
    return "".join(out)


def body_en():
    out = ['<p class="lede">Three methods of point velocity measurement — the Pitot probe, thermal '
           'anemometry and laser Doppler anemometry — are presented in this chapter. All three '
           'answer the same question: what is the fluid velocity at the exact location of the '
           'probe? They differ in range, in whether they intrude into the flow, and in how much '
           'they disturb it.</p>', sec_index("en")]
    for f in SECTIONS_EN:
        out.append(f())
    return "".join(out)


def build(lang):
    vi = lang == "vi"
    switch = ("%s%s/" % (BASE_EN, CSLUG)) if vi else ("%s%s/" % (BASE_VI, CSLUG))
    title = ("Chương 29 — %s · Sổ tay Đo lường, Thiết bị đo và Cảm biến" % TITLE_VI if vi
             else "Chapter 29 — %s · Measurement, Instrumentation and Sensors Handbook" % TITLE_EN)
    desc = ("Bản dịch tiếng Việt Chương 29 “Đo vận tốc tại một điểm” của John A. Kleppe và cộng sự — "
            "ống Pitot, đo nhiệt và Doppler laser, cùng lý thuyết, sai số và cách lắp đặt." if vi
            else
            "Companion to Chapter 29 of the CRC Measurement Handbook — Pitot probe, thermal and "
            "laser Doppler anemometry, with their theory, error sources and installation.")
    crumb = ('<a href="/vi/books/">Sách</a> · <a href="%s">Sổ tay Đo lường, Thiết bị đo và Cảm biến</a> · '
             'Chương 29' % BASE_VI if vi else
             '<a href="/books/">Books</a> · <a href="%s">Measurement, Instrumentation and Sensors '
             'Handbook</a> · Chapter 29' % BASE_EN)
    # Recount these whenever a section is added: the meta line is the only place
    # the reader is told how big the chapter is, and a stale count is the kind of
    # error nobody notices until they have read the whole thing.
    meta = ("Chương 29 · theo Ch29.pdf (CRC Press, 1999) · 31 hình, 71 phương trình, 4 bảng" if vi else
            "Chapter 29 · 31 figures, 71 equations, 4 tables")
    body = ('<main><article class="intranet-content reader"><div class="reader-hero">'
            '<div class="breadcrumb">%s</div><h1>%s</h1><p class="byline">%s</p>'
            '<div class="meta-line">%s</div></div><div class="prose">%s</div>%s</article></main>'
            % (crumb, TITLE_VI if vi else TITLE_EN, BYLINE, meta,
               body_vi() if vi else body_en(), chapter_nav(lang, 29)))
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
