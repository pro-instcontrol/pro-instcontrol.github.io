# -*- coding: utf-8 -*-
"""Handbook Chapter 86 — Computers.

A.M. MacLeod, P.F. Martin, W.A. Gillespie (University of Abertay Dundee)

Writes the full Vietnamese translation and the English companion.
Figures: hb86fig.py (86.1–86.7). Tables 86.1–86.6 are printed tables.

The printed chapter has no display equations, so none are numbered here; the
only set-piece is the C fragment in §86.6, which is reproduced verbatim —
including the three missing spaces in its `#define` lines and the missing
semicolon after the first `outportb()` call. Those are printing faults, not
transcription slips, and the translator's note says so and gives the corrected
lines.

Table 86.3 is printed as two side-by-side panels (System | Supplier twice).
It is reflowed here into a single grouped table; no entry is dropped.

Run:  python build/reader_hb_ch86.py
"""
import os

import hb86fig as F86
from reader_handbook import SLUG, head, header, footer
from chapter_nav import nav as chapter_nav

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSLUG = "ch86-computers"
TITLE_EN = "Computers"
TITLE_VI = "Máy tính"
BYLINE = "A. M. MacLeod, P. F. Martin, W. A. Gillespie"
BYLINE_EN = "A. M. MacLeod, P. F. Martin, W. A. Gillespie"
BASE_EN = "/books/read/%s/" % SLUG
BASE_VI = "/vi/books/read/%s/" % SLUG


def fig(num, lang="vi"):
    svg, cap_vi, cap_en, _av, _ae = getattr(F86, "fig_86_%d" % num)()
    return ('<figure class="figure" id="fig-86-%d">%s<figcaption class="figcap">%s</figcaption>'
            '</figure>' % (num, svg, cap_vi if lang == "vi" else cap_en))


def p(t):
    return "<p>%s</p>" % t


def h2(t, en=""):
    return '<h2>%s%s</h2>' % (t, (' <span class="en">%s</span>' % en) if en else "")


def h3(t, en=""):
    return '<h3>%s%s</h3>' % (t, (' <span class="en">%s</span>' % en) if en else "")


def h4(t, en=""):
    return '<h4>%s%s</h4>' % (t, (' <span class="en">%s</span>' % en) if en else "")


def note(t):
    return '<div class="note">%s</div>' % t


def refs(items):
    return '<ol class="ref-list">%s</ol>' % "".join("<li>%s</li>" % i for i in items)


def ul(items):
    return "<ul>%s</ul>" % "".join("<li>%s</li>" % i for i in items)


def ol(items):
    return "<ol>%s</ol>" % "".join("<li>%s</li>" % i for i in items)


def _glossary(items):
    o = ['<dl class="glossary">']
    for term, body in items:
        o.append("<dt>%s</dt><dd>%s</dd>" % (term, body))
    o.append("</dl>")
    return "".join(o)


def _code(lines):
    """A monospaced block. library.css has no `pre` rule, so the styling is inline.

    `width:fit-content` keeps a one-line string from stretching the full column
    while still letting the long C fragment scroll inside `max-width:100%`.
    """
    return ('<pre style="display:block;width:fit-content;max-width:100%%;'
            'box-sizing:border-box;background:#f7f7f5;border:1px solid #e3e3df;'
            'border-radius:6px;padding:10px 14px;overflow-x:auto;'
            'font:12.5px/1.6 ui-monospace,SFMono-Regular,Consolas,Menlo,monospace;'
            'color:#222;margin:0.9em 0"><code>%s</code></pre>'
            % "\n".join(lines))


def _sup(x):
    return "<sup>%s</sup>" % x


def _em(x):
    return "<em>%s</em>" % x


def _b(x):
    return "<b>%s</b>" % x


# ================================================================ TABLES
def _tbl(num, title, head, rows, lang, minw=520, dense=True, cls=""):
    """One printed table. `rows` holds already-localised cells."""
    c = "tbl" + (" dense" if dense else "") + ((" " + cls) if cls else "")
    o = ['<div class="table-wrap"><table class="%s" style="min-width:%dpx">' % (c, minw)]
    o.append("<caption><b>%s</b> %s</caption>" % (num, title))
    o.append("<thead><tr>%s</tr></thead><tbody>"
             % "".join('<th scope="col">%s</th>' % h for h in head))
    for r in rows:
        cells = []
        for i, cell in enumerate(r):
            if i == 0:
                cells.append('<th scope="row">%s</th>' % cell)
            else:
                cells.append("<td>%s</td>" % cell)
        o.append("<tr>%s</tr>" % "".join(cells))
    o.append("</tbody></table></div>")
    return "".join(o)


def _tbl_grouped(num, title, head, groups, lang, minw=560):
    """A table whose first column is a group label spanning several rows."""
    o = ['<div class="table-wrap"><table class="tbl dense" style="min-width:%dpx">' % minw]
    o.append("<caption><b>%s</b> %s</caption>" % (num, title))
    o.append("<thead><tr>%s</tr></thead><tbody>"
             % "".join('<th scope="col">%s</th>' % h for h in head))
    for label, rows in groups:
        for j, r in enumerate(rows):
            cells = []
            for i, cell in enumerate(r):
                if i == 0 and j == 0:
                    cells.append('<th scope="rowgroup" rowspan="%d">%s</th>'
                                 % (len(rows), label))
                cells.append("<td>%s</td>" % cell)
            o.append("<tr>%s</tr>" % "".join(cells))
    o.append("</tbody></table></div>")
    return "".join(o)


def table_86_1(lang="vi"):
    if lang == "vi":
        head = ["Chuẩn bus", "STE", "G96", "VME", "Multibus II"]
        rows = [["Độ rộng dữ liệu (bit)", "8", "8/16", "8/16/32", "8/16/32"],
                ["Địa chỉ tối đa (byte)", "1 M", "32 M", "4 G", "4 G"],
                ["Đồng bộ/không đồng bộ", "Không đồng bộ", "Không đồng bộ",
                 "Không đồng bộ", "Đồng bộ"],
                ["Đầu nối", "64 chân", "96 chân", "96 chân", "96 chân + 32 chân"]]
        title = "Các chuẩn bus vi xử lý tiêu biểu"
    else:
        head = ["Bus Standard", "STE", "G96", "VME", "Multibus II"]
        rows = [["Data width (bits)", "8", "8/16", "8/16/32", "8/16/32"],
                ["Max address (bytes)", "1 M", "32 M", "4 G", "4 G"],
                ["Synchronous/asynchronous", "Async", "Async", "Async", "Sync"],
                ["Connectors", "64 pin", "96 pin", "96 pin", "96 pin + 32 pin"]]
        title = "Typical Microprocessor Bus Standards"
    return _tbl("Bảng 86.1" if lang == "vi" else "Table 86.1", title,
                head, rows, lang, minw=560)


def table_86_2(lang="vi"):
    if lang == "vi":
        head = ["Sản phẩm", "Nền tảng", "Hãng sản xuất"]
        title = ("Các gói phần mềm thu thập và hiển thị dữ liệu tiêu biểu cho hệ đo lường "
                 "dựa trên PC")
        rows = [
            ["DTV", "PC (Windows 3.1 hoặc 95)",
             "Data Translation Inc.<br>101 Locke Drive<br>Marlboro, MA 01752-1192<br>"
             "Tel: (U.S. và Canada) (800) 525-8528<br>(toàn cầu) +1 508-481-3700"],
            ["Labtech Notebook/Notebook Pro", "PC (DOS, Windows 3.1 hoặc 95)",
             "Laboratory Technologies Corporation<br>400 Research Drive<br>"
             "Wilmington, MA 01887<br>Tel. (U.S. và Canada) 800-8799-5228<br>"
             "(toàn cầu) +1 508-658-9972"],
            ["LabVIEW", "PC, Mac, Sun, Power PC",
             "National Instruments<br>6504 Bridge Point Parkway<br>Austin, TX 78730-5039<br>"
             "Tel: +1 512-794-0100"],
            ["LabWindows", "PC (DOS)",
             "National Instruments<br>6504 Bridge Point Parkway<br>Austin, TX 78730-5039<br>"
             "Tel: +1 512-794-0100"],
            ["LabWindows/CVI", "PC (Windows 3.1 hoặc 95), Sun",
             "National Instruments<br>6504 Bridge Point Parkway<br>Austin, TX 78730-5039<br>"
             "Tel: +1 512-794-0100"],
            ["ORIGIN", "PC (Windows 3.1 hoặc 95)",
             "MicroCal Software Inc.<br>One Roundhouse Plaza<br>Northampton, MA 01060<br>"
             "Tel +1 413-586-2013"],
        ]
    else:
        head = ["Product", "Platforms", "Manufacturer"]
        title = ("Typical Data Acquisition and Display Software Packages for PC-Based "
                 "Instrumentation Systems")
        rows = [
            ["DTV", "PC (Windows 3.1 or 95)",
             "Data Translation Inc.<br>101 Locke Drive<br>Marlboro, MA 01752-1192<br>"
             "Tel: (U.S. and Canada) (800) 525-8528<br>(worldwide) +1 508-481-3700"],
            ["Labtech Notebook/Notebook Pro", "PC (DOS, Windows 3.1 or 95)",
             "Laboratory Technologies Corporation<br>400 Research Drive<br>"
             "Wilmington, MA 01887<br>Tel. (U.S. and Canada) 800-8799-5228<br>"
             "(worldwide) +1 508-658-9972"],
            ["LabVIEW", "PC, Mac, Sun, Power PC",
             "National Instruments<br>6504 Bridge Point Parkway<br>Austin, TX 78730-5039<br>"
             "Tel: +1 512-794-0100"],
            ["LabWindows", "PC (DOS)",
             "National Instruments<br>6504 Bridge Point Parkway<br>Austin, TX 78730-5039<br>"
             "Tel: +1 512-794-0100"],
            ["LabWindows/CVI", "PC (Windows 3.1 or 95), Sun",
             "National Instruments<br>6504 Bridge Point Parkway<br>Austin, TX 78730-5039<br>"
             "Tel: +1 512-794-0100"],
            ["ORIGIN", "PC (Windows 3.1 or 95)",
             "MicroCal Software Inc.<br>One Roundhouse Plaza<br>Northampton, MA 01060<br>"
             "Tel +1 413-586-2013"],
        ]
    return _tbl("Bảng 86.2" if lang == "vi" else "Table 86.2", title,
                head, rows, lang, minw=600)


def table_86_3(lang="vi"):
    if lang == "vi":
        head = ["Hệ thống", "Hãng/cung cấp"]
        title = "Các hãng sản xuất/cung cấp hệ thống dựa trên bus và PC công nghiệp"
        groups = [
            ("VME", [
                ["Wordsworth Technology Ltd<br>6 Enterprise Way<br>Edenbridge, Kent TN8 6HF "
                 "U.K.<br>Tel: +44 (0) 1732 866988"],
                ["PEP Modular Computers, Inc.<br>750 Holiday Drive, Building 9<br>Pittsburg, "
                 "PA 15220<br>Tel: (412) 921-3322"],
                ["BVM Ltd, Hobb Lane<br>Hedge End<br>Southampton, SO30 0GH, U.K.<br>"
                 "Tel: +44 (0) 1489 780144"],
                ["Motorola, Inc.<br>Computer Group<br>2900 S Diablo Way<br>Tempe, AZ 85282<br>"
                 "Tel: (800) 759-1107"],
            ]),
            ("STE", [
                ["Arcom Control Systems<br>Units 8-10 Clifton Road<br>Cambridge CB1 4WH, "
                 "U.K.<br>Tel +44 (0) 1223 411200"],
            ]),
            ("G64", [
                ["Gespac SA<br>18 Chemin des Aulx<br>1228 Geneva, Switzerland<br>"
                 "Tel: +41 (22) 794 34 00"],
                ["Altek Microcomponents Ltd.<br>Lifetrend House<br>Heyes Lane<br>Alderley Edge, "
                 "Cheshire SK9 7LW<br>Tel: +44 (0) 1625 584804"],
            ]),
            ("PC công nghiệp" if lang == "vi" else "Industrial PC", [
                ["Blue Chip Technology Ltd.<br>Chowley Oak, Tattenhall<br>Chester, Cheshire "
                 "CH3 9EX, U.K.<br>Tel: +44 (0) 1829 772 000"],
                ["Capax Industrial PC Systems Ltd.<br>Airport House, Purley Way<br>Croydon, "
                 "Surrey, CR0 0XZ, U.K.<br>Tel +44 (0) 181 667 9000"],
            ]),
            ("VXI", [
                ["National Instruments<br>6504 Bridge Point Parkway<br>Austin, TX 78730-5039<br>"
                 "Tel: (512) 794-0100"],
            ]),
            ("Multibus", [
                ["Tadpole Technology, Inc.<br>2001 Gateway Place, Suite 550 West<br>San Jose, "
                 "CA 95110<br>Tel: (408)441-7920"],
                ["Intel Corp.<br>3065 Bowers Avenue<br>Santa Clara, CA 95051"],
                ["Syntel Microsystems<br>Queens Mill Road<br>Huddersfield, HD1 3PG, U.K.<br>"
                 "Tel: +44 (0) 1484 535101"],
            ]),
            ("PC/104", [
                ["ComputerBoards, Inc.<br>125 High Street<br>Mansfield, MA 02048<br>"
                 "Tel: (508) 261-1123"],
                ["Diamond Point International (Europe) Ltd.<br>Unit 9, North Point Business "
                 "Estate, Enterprise Close<br>Rochester, Kent ME2 4LY, U.K.<br>"
                 "Tel +44 (0)1634 718100"],
            ]),
        ]
    else:
        head = ["System", "Manufacturer/Supplier"]
        title = "Manufacturers/Suppliers of Bus-Based Systems and Industrial PCs"
        groups = [
            ("VME", [
                ["Wordsworth Technology Ltd<br>6 Enterprise Way<br>Edenbridge, Kent TN8 6HF "
                 "U.K.<br>Tel: +44 (0) 1732 866988"],
                ["PEP Modular Computers, Inc.<br>750 Holiday Drive, Building 9<br>Pittsburg, "
                 "PA 15220<br>Tel: (412) 921-3322"],
                ["BVM Ltd, Hobb Lane<br>Hedge End<br>Southampton, SO30 0GH, U.K.<br>"
                 "Tel: +44 (0) 1489 780144"],
                ["Motorola, Inc.<br>Computer Group<br>2900 S Diablo Way<br>Tempe, AZ 85282<br>"
                 "Tel: (800) 759-1107"],
            ]),
            ("STE", [
                ["Arcom Control Systems<br>Units 8-10 Clifton Road<br>Cambridge CB1 4WH, "
                 "U.K.<br>Tel +44 (0) 1223 411200"],
            ]),
            ("G64", [
                ["Gespac SA<br>18 Chemin des Aulx<br>1228 Geneva, Switzerland<br>"
                 "Tel: +41 (22) 794 34 00"],
                ["Altek Microcomponents Ltd.<br>Lifetrend House<br>Heyes Lane<br>Alderley Edge, "
                 "Cheshire SK9 7LW<br>Tel: +44 (0) 1625 584804"],
            ]),
            ("Industrial PC", [
                ["Blue Chip Technology Ltd.<br>Chowley Oak, Tattenhall<br>Chester, Cheshire "
                 "CH3 9EX, U.K.<br>Tel: +44 (0) 1829 772 000"],
                ["Capax Industrial PC Systems Ltd.<br>Airport House, Purley Way<br>Croydon, "
                 "Surrey, CR0 0XZ, U.K.<br>Tel +44 (0) 181 667 9000"],
            ]),
            ("VXI", [
                ["National Instruments<br>6504 Bridge Point Parkway<br>Austin, TX 78730-5039<br>"
                 "Tel: (512) 794-0100"],
            ]),
            ("Multibus", [
                ["Tadpole Technology, Inc.<br>2001 Gateway Place, Suite 550 West<br>San Jose, "
                 "CA 95110<br>Tel: (408)441-7920"],
                ["Intel Corp.<br>3065 Bowers Avenue<br>Santa Clara, CA 95051"],
                ["Syntel Microsystems<br>Queens Mill Road<br>Huddersfield, HD1 3PG, U.K.<br>"
                 "Tel: +44 (0) 1484 535101"],
            ]),
            ("PC/104", [
                ["ComputerBoards, Inc.<br>125 High Street<br>Mansfield, MA 02048<br>"
                 "Tel: (508) 261-1123"],
                ["Diamond Point International (Europe) Ltd.<br>Unit 9, North Point Business "
                 "Estate, Enterprise Close<br>Rochester, Kent ME2 4LY, U.K.<br>"
                 "Tel +44 (0)1634 718100"],
            ]),
        ]
    return _tbl_grouped("Bảng 86.3" if lang == "vi" else "Table 86.3", title,
                        head, groups, lang, minw=560)


def table_86_4(lang="vi"):
    if lang == "vi":
        head = ["Loại card", "Chức năng cung cấp"]
        title = "Các thiết bị ngoại vi nội bộ tiêu biểu"
        rows = [
            ["Bộ điều hợp hiển thị", "Cung cấp chức năng video và đồ hoạ"],
            ["Bộ điều hợp truyền thông nối tiếp",
             "Truyền thông nối tiếp với một thiết bị tương tự theo chuẩn RS232, RS422 hoặc "
             "RS485"],
            ["Bộ điều hợp IEEE-488",
             "Giao tiếp với các thiết bị đo thông minh qua bus IEEE-488 (GPIB)"],
            ["Vào/ra số (I/O)",
             "Các đường I/O riêng lẻ, thường được nhóm thành một byte 8 bit, dùng để phát mức "
             "logic cao và thấp (đầu ra) hoặc cảm nhận mức logic cao và thấp (đầu vào); đầu "
             "vào và đầu ra có thể được cách ly quang; đầu ra có thể điều khiển rơ le"],
            ["Bộ đếm/định thời",
             "Bộ đếm–định thời phần cứng cho phép đếm xung ngoài, tạo dạng sóng số hoặc đo độ "
             "rộng xung; bộ đếm/định thời thường có thêm như một chức năng phụ trên các card "
             "I/O số"],
            ["Đầu vào tương tự",
             "Chuyển một điện áp vào tương tự thành một giá trị nguyên mà máy tính có thể đọc; "
             "độ phân giải thường là 8, 10, 12 hoặc 16 bit; dải điện áp vào có thể cố định hoặc "
             "do người dùng chọn; thời gian chuyển đổi từ vài giây đến vài chục nanôgiây"],
            ["Đầu ra tương tự",
             "Tạo ra một điện áp ra tương tự tỉ lệ với đầu vào số; độ phân giải thường là 8, "
             "10, 12 hoặc 16 bit"],
        ]
    else:
        head = ["Card Type", "Facilities Offered"]
        title = "Typical Internal Peripherals"
        rows = [
            ["Display adapter", "Provides video and graphics facilities"],
            ["Serial communications adapter",
             "Serial communication to a similar device using the RS232, RS422, or RS485 "
             "standard"],
            ["IEEE-488 Adapter",
             "Communication with intelligent instruments using the IEEE-488 bus (GPIB)"],
            ["Digital input/output (I/O)",
             "Individual I/O lines, normally grouped as an 8-bit byte, which may be used to "
             "provide logic high and low signals (output) or sense logic high or low signals "
             "(input); inputs and outputs may be optically isolated; outputs may drive relays"],
            ["Counter/timer",
             "Hardware counter timer allowing external pulses to be counted, digital waveforms "
             "generated or pulse widths measured; counter/timers are often available as an "
             "additional facility on digital I/O cards"],
            ["Analog input",
             "Converts an analog input voltage to an integer value which may be read by the "
             "computer; resolution typically 8, 10, 12, or 16 bits; input voltage range may be "
             "fixed or may be user selectable; conversion times vary from several seconds to "
             "tens of nanoseconds"],
            ["Analog output",
             "Produces an analog output voltage proportional to a digital input; resolution "
             "typically be 8, 10, 12, or 16 bits"],
        ]
    return _tbl("Bảng 86.4" if lang == "vi" else "Table 86.4", title,
                head, rows, lang, minw=580)


def table_86_5(lang="vi"):
    if lang == "vi":
        head = ["Tham số", "Mô tả"]
        title = "Các tham số ADC thông dụng"
        rows = [
            ["Độ phân giải",
             "Thay đổi nhỏ nhất ở đầu vào còn phát hiện được ở đầu ra số; độ phân giải thường "
             "được biểu diễn bằng số bit có nghĩa của đầu ra số; do đó độ phân giải 8 bit nghĩa "
             "là 1 phần trong 256; 10 bit là 1 phần trong 1024, và 12 bit là 1 phần trong 4096"],
            ["Tính tuyến tính",
             "Mức độ đầu ra lệch khỏi quan hệ tuyến tính với đầu vào; thiết bị tốt sẽ tuyến "
             "tính trong khoảng ±1 bit có nghĩa nhỏ nhất, nghĩa là giá trị đầu ra được bảo đảm "
             "nằm trong khoảng ±1 so với một phép chuyển đổi tuyến tính chính xác"],
            ["Dải đo",
             "Điện áp vào lớn nhất (và nhỏ nhất); đầu vào có thể đơn cực, ví dụ 0–5 V, hoặc "
             "lưỡng cực ±5 V; điện áp được quy chiếu về đất trừ khi đầu vào là vi sai, ví dụ "
             "những đầu vào thiết kế cho cảm biến cầu"],
            ["Tốc độ chuyển đổi",
             "Thời gian cần để chuyển một điện áp vào thành một đầu ra số, thường từ 1 s đến "
             "1 µs; cũng có thể được nêu dưới dạng tốc độ lấy mẫu"],
            ["Tính tuyến tính",
             "Mức độ mà phép chuyển đổi là tuyến tính, ví dụ độ tuyến tính ±1 bit có nghĩa nhỏ "
             "nhất nghĩa là giá trị đầu ra nằm trong khoảng ±1 so với phép chuyển đổi tuyến "
             "tính lý tưởng"],
            ["Trở kháng vào",
             "Trở kháng giữa đầu nối vào và đất hoặc giữa các đầu vào vi sai."],
        ]
    else:
        head = ["Parameter", "Description"]
        title = "Common ADC Parameters"
        rows = [
            ["Resolution",
             "The smallest change in input detectable in the digital output; resolutions are "
             "commonly expressed in the number of significant bits in the digital output; "
             "hence, 8-bit resolution means 1 part in 256; 10 bit, 1 part in 1024, and 12 bit, "
             "1 part in 4096"],
            ["Linearity",
             "The extent to which the output deviates from a linear relationship with the "
             "input; good devices will be linear to ±1 least-significant bit; i.e., the output "
             "value is guaranteed to be within ±1 of an exactly linear conversion"],
            ["Range",
             "The maximum (and minimum) input voltages; inputs may be unipolar, e.g., 0–5 V or "
             "bipolar ±5 V; voltages are specified relative to ground unless the inputs are "
             "differential, e.g., those designed for bridge sensors"],
            ["Conversion speed",
             "The time taken to convert an input voltage into a digital output, typically 1 s "
             "to 1 µs; may also be quoted as a sample rate"],
            ["Linearity",
             "The extent to which the conversion is linear, e.g., a linearity of ±1 "
             "least-significant bit means that the output value is within ±1 of the ideal "
             "linear conversion"],
            ["Input impedance",
             "The impedance between the input terminal and ground or between differential "
             "inputs."],
        ]
    return _tbl("Bảng 86.5" if lang == "vi" else "Table 86.5", title,
                head, rows, lang, minw=580)


def table_86_6(lang="vi"):
    if lang == "vi":
        head = ["Hệ thống", "HĐH/Nhân", "Hãng sản xuất"]
        title = "Một số hệ điều hành và nhân thời gian thực quan trọng"
        rows = [
            ["OS-9", "HĐH", "Microware Systems Corporation<br>1900 NW 114th Street,<br>"
                            "Des Moines, IA 50325"],
            ["LynxOS", "HĐH", "Lynx Real-Time Systems, Inc.<br>16870 Lark Avenue<br>"
                               "Los Gatos, CA 95030-2315"],
            ["VxWorks", "HĐH", "Wind River Systems<br>1010 Atlantic Avenue<br>Alameda, CA 94501"],
            ["VRTX/OS", "HĐH", "Microtec Research<br>2350 Mission College Blvd.<br>"
                               "Santa Clara, CA 95054"],
            ["VRTX", "Nhân", "Microtec Research<br>2350 Mission College Blvd.<br>"
                              "Santa Clara, CA 95054"],
            ["iRMX", "Nhân", "Intel Corp.<br>3065 Bowers Avenue<br>Santa Clara, CA 95051"],
        ]
    else:
        head = ["System", "OS/Kernel", "Manufacturer"]
        title = "Some Important Real-Time Operating Systems and Kernels"
        rows = [
            ["OS-9", "OS", "Microware Systems Corporation<br>1900 NW 114th Street,<br>"
                           "Des Moines, IA 50325"],
            ["LynxOS", "OS", "Lynx Real-Time Systems, Inc.<br>16870 Lark Avenue<br>"
                             "Los Gatos, CA 95030-2315"],
            ["VxWorks", "OS", "Wind River Systems<br>1010 Atlantic Avenue<br>Alameda, CA 94501"],
            ["VRTX/OS", "OS", "Microtec Research<br>2350 Mission College Blvd.<br>"
                              "Santa Clara, CA 95054"],
            ["VRTX", "Kernel", "Microtec Research<br>2350 Mission College Blvd.<br>"
                                "Santa Clara, CA 95054"],
            ["iRMX", "Kernel", "Intel Corp.<br>3065 Bowers Avenue<br>Santa Clara, CA 95051"],
        ]
    return _tbl("Bảng 86.6" if lang == "vi" else "Table 86.6", title,
                head, rows, lang, minw=540)


# ================================================================ NOTE
def _transnote(lang="vi"):
    if lang == "vi":
        return note(
            "<b>Ghi chú của người dịch.</b> Chương này dịch từ bản in Ch86.pdf của CRC Press "
            "(1999). Đây là một chương khảo sát: <b>bản in không có một công thức hiển thị "
            "nào</b>, nên ở đây cũng không đánh số công thức. Phần duy nhất không phải văn xuôi "
            "là đoạn mã C ở §86.6, và nó được in lại nguyên văn — kể cả ba chỗ thiếu dấu cách "
            "trong các dòng <code>#define</code> và chỗ thiếu dấu chấm phẩy sau lời gọi "
            "<code>outportb()</code> đầu tiên; đó là lỗi của bản in, không phải lỗi chép. Ba "
            "dòng đúng phải là <code>#define PA BASE</code>, <code>#define PB BASE+1</code>, "
            "<code>#define CONTROL BASE+3</code>, và lời gọi phải có dấu chấm phẩy. "
            "<br><br>"
            "Bản in còn <b>tự mâu thuẫn ở bốn chỗ</b>, tất cả đều được giữ nguyên như đã in: "
            "(1) tốc độ bus IEEE-488 được nêu là <b>1,5 MB/s</b> ở mục “Bộ điều hợp IEEE-488” "
            "nhưng là <b>1 MB/s</b> ở mục “Thiết bị IEEE 488”; (2) <b>Bảng 86.5 liệt kê “Tính "
            "tuyến tính” hai lần</b> với hai định nghĩa khác nhau, và dòng thứ hai là dòng lặp "
            "lại ý của dòng thứ nhất; (3) kích thước card Multibus II được ghi là "
            "<b>220 × 233,65 mm</b> trong khi card VME hai tầng cùng chuẩn Eurocard được ghi là "
            "<b>233,35 mm</b> — trị số 233,65 là lỗi in, nhưng vẫn để nguyên; (4) §86.4 mở đầu "
            "bằng cách kể tên ba chuẩn bus PC (ISA, EISA và MCA) rồi <b>không mô tả MCA</b> — "
            "chính nguyên bản nói rõ điều đó. Ngoài ra Hình 86.3 chỉ vẽ bốn đường ray (dữ liệu, "
            "điều khiển, phân xử, tiện ích) trong khi phần chữ nói rằng một nhóm đường ray mang "
            "cả thông tin dữ liệu <i>và</i> địa chỉ; hình không có ray địa chỉ riêng. "
            "<br><br>"
            "<b>Bảng 86.3</b> được in thành hai khối cạnh nhau (Hệ thống | Hãng cung cấp, lặp "
            "lại hai lần). Ở đây nó được dựng lại thành một bảng duy nhất có gộp ô theo hệ "
            "thống, không bỏ sót mục nào. Các số điện thoại, địa chỉ và tên hãng được giữ "
            "nguyên như bản in, kể cả số <i>800-8799-5228</i> của Labtech vốn thừa một chữ số.")
    return note(
        "<b>Translator’s note.</b> Translated from the CRC Press print of Ch86.pdf (1999). "
        "This is a survey chapter: <b>the printed text contains no display equations</b>, so "
        "none are numbered here. The only non-prose passage is the C fragment in §86.6, and it "
        "is reproduced verbatim — including three missing spaces in its <code>#define</code> "
        "lines and a missing semicolon after the first <code>outportb()</code> call. Those are "
        "printing faults, not transcription slips. The three lines should read "
        "<code>#define PA BASE</code>, <code>#define PB BASE+1</code> and "
        "<code>#define CONTROL BASE+3</code>, and the call should be terminated. "
        "<br><br>"
        "The print also <b>contradicts itself in four places</b>, all left as printed: "
        "(1) the IEEE-488 bus is quoted at <b>1.5 MB/s</b> under “IEEE-488 Adapter” but at "
        "<b>1 MB/s</b> under “IEEE 488 Devices”; (2) <b>Table 86.5 lists “Linearity” twice</b>, "
        "with two different definitions, the second restating the first; (3) the Multibus II "
        "card is given as <b>220 × 233.65 mm</b> while the double-height VME card of the same "
        "Eurocard family is given as <b>233.35 mm</b> — 233.65 is a misprint, retained; "
        "(4) §86.4 opens by naming three PC bus standards (ISA, EISA and MCA) and then "
        "<b>never describes MCA</b> — the original says so itself. Separately, Figure 86.3 "
        "draws four rails (data, control, arbitration, utility) while the prose says one group "
        "of tracks carries <i>both</i> data and address information; the figure has no separate "
        "address rail. "
        "<br><br>"
        "<b>Table 86.3</b> is printed as two side-by-side panels (System | Supplier, twice). "
        "It is reflowed here into one table grouped by system, with no entry dropped. "
        "Telephone numbers, addresses and company names are kept exactly as printed, including "
        "Labtech’s malformed <i>800-8799-5228</i>.")


# ================================================================ BODY — VI
def body_vi():
    o = []
    o.append(_transnote("vi"))

    # ---------------------------------------------------------------- 86.1
    o.append(h2("86.1 Giới thiệu", "Introduction"))
    o.append(p("Máy tính là một thành phần thiết yếu của hầu hết các hệ đo lường, nhờ khả năng "
               "giám sát việc thu thập dữ liệu và cho phép xử lý, lưu trữ và hiển thị thông "
               "tin. Nhiều thiết bị đo hiện đại có khả năng cung cấp cho người dùng ở xa quyền "
               "truy cập thông tin đo lường qua các mạng máy tính tiêu chuẩn."))

    # ---------------------------------------------------------------- 86.2
    o.append(h2("86.2 Hệ đo lường dựa trên máy tính", "Computer-Based Instrumentation Systems"))
    o.append(p("Các đặc điểm chính của một hệ đo lường dựa trên máy tính được trình bày ở Hình "
               "86.1. Việc triển khai thực tế của những hệ như vậy sẽ phụ thuộc vào ứng dụng. "
               "Nhiều thiết bị đo được sản xuất thương mại như máy quang phổ hay máy hiện sóng "
               "lưu trữ số tự chúng đã là những hệ đo lường tích hợp dựa trên máy tính. Những "
               "thiết bị đo “độc lập” này có thể được trang bị các giao diện như IEEE-488 hoặc "
               "RS-232 để cho phép điều khiển chúng từ máy tính cá nhân (PC) và đồng thời hỗ "
               "trợ việc chuyển dữ liệu về PC để xử lý và hiển thị tiếp. Cách khác, hệ đo lường "
               "có thể được xây dựng quanh một PC/trạm làm việc hoặc một hệ bus công nghiệp "
               "như VME hay Multibus, cho phép người dùng tuỳ biến máy tính cho phù hợp với "
               "ứng dụng bằng cách chọn một bộ card cắm thêm thích hợp. Gần đây, sự ra đời của "
               "các PC xách tay và sổ tay được trang bị giao diện PCMCIA có khả năng vào/ra đã "
               "mở ra cơ hội phát triển những hệ đo lường có tính di động cao."))
    o.append(fig(1))

    o.append(h3("Máy tính một bảng mạch", "The Single-Board Computer"))
    o.append(p("Dạng đơn giản nhất của một máy tính được xây dựng quanh <b>máy tính một bảng "
               "mạch</b> (single-board computer, SBC), chứa bộ vi xử lý, bộ nhớ và các giao "
               "diện để giao tiếp với những hệ điện tử khác. Những máy tính cá nhân đầu tiên "
               "đơn giản chỉ gồm một SBC cùng với bàn phím, màn hình, ổ đĩa và một bộ nguồn. "
               "Ngày nay SBC vẫn là một giải pháp để thêm trí tuệ hạn chế vào các hệ đo lường, "
               "đồng thời là thành phần của hầu hết các hệ máy tính, ví dụ như bo mạch chủ của "
               "một PC."))
    o.append(p("Hình 86.2 trình bày sơ lược một SBC đơn giản. Bộ vi xử lý, chứa đơn vị xử lý "
               "trung tâm, chịu trách nhiệm thực thi chương trình máy tính và điều khiển luồng "
               "dữ liệu lưu chuyển trên SBC. Bộ nhớ truy cập ngẫu nhiên (RAM) đóng vai trò vùng "
               "lưu trữ tạm thời (tức là bay hơi) cho cả mã chương trình lẫn dữ liệu. Trên bo "
               "mạch chủ của một PC, bộ nhớ chỉ đọc (ROM) phần lớn được dùng để lưu mã mức thấp "
               "dùng cho việc truy cập phần cứng vào/ra, ví dụ BIOS (hệ vào/ra cơ bản). Hệ điều "
               "hành và phần mềm ứng dụng được nạp vào RAM từ ổ đĩa. Trong những hệ nhỏ, "
               "chuyên dụng như một máy hiện sóng, ROM có thể được dùng để lưu mã chương trình "
               "nhằm tránh phải có ổ đĩa. Với các lô sản xuất nhỏ hoặc cho công việc phát "
               "triển, ROM lập trình xoá được (EPROM) được dùng thay cho ROM, cho phép nâng "
               "cấp mã mà không phải chịu chi phí đặt làm một chip ROM mới từ nhà sản xuất."))
    o.append(fig(2))
    o.append(p("Dữ liệu được chuyển trên SBC nhờ <b>bus dữ liệu</b> của nó, thường rộng 8, 16 "
               "hoặc 32 bit (tương ứng với số bit có thể truyền cùng lúc). SBC có bus dữ liệu "
               "8 bit ít phức tạp hơn và do đó rẻ hơn hệ 32 bit, và có thể là giải pháp tối ưu "
               "cho những ứng dụng điều khiển quá trình chỉ cần xử lý tối thiểu trên dữ liệu 8 "
               "bit, ví dụ từ cảm biến nhiệt độ và cảm biến vị trí. Tuy vậy, độ rộng bus 32 bit "
               "của hầu hết PC và trạm làm việc hiện đại là điều thiết yếu để bảo đảm phần mềm "
               "ứng dụng chạy trên Windows hoạt động nhanh."))
    o.append(p("<b>Bus địa chỉ</b> được dùng để xác định đích của dữ liệu trên bus dữ liệu. "
               "Việc truyền dữ liệu thường diễn ra giữa bộ vi xử lý với bộ nhớ hoặc với các "
               "giao diện. Tuy nhiên, một số SBC hỗ trợ DMA (truy cập bộ nhớ trực tiếp), cho "
               "phép dữ liệu được chuyển trực tiếp giữa các giao diện và bộ nhớ mà không cần "
               "thông tin phải đi qua bộ xử lý. DMA vốn nhanh hơn việc truyền dữ liệu do "
               "chương trình điều khiển và được dùng để di chuyển những khối dữ liệu lớn, ví "
               "dụ nạp chương trình từ đĩa hoặc truyền ảnh video đã số hoá."))
    o.append(p("SBC được trang bị các giao diện để có thể giao tiếp với những mạch khác. Giao "
               "diện thực hiện hai chức năng chính. Thứ nhất, chúng bảo đảm các tín hiệu trên "
               "những bus nội bộ của SBC không bị ảnh hưởng bởi việc nối thêm thiết bị ngoại "
               "vi. Thứ hai, chúng bảo đảm tín hiệu có thể đi vào và đi ra khỏi máy tính và "
               "rằng các mức điện áp cũng như điều kiện tải dòng thích hợp đều được thoả mãn. "
               "Một giao diện được thiết kế tốt cũng phải bảo vệ điện cho SBC một cách thoả "
               "đáng trước những quá độ đưa vào qua đường nối ngoài. Giao diện song song cho "
               "phép truyền dữ liệu, thường 8 hoặc 16 bit một lần, và chứa các thanh ghi đóng "
               "vai trò kho dữ liệu tạm thời. Giao diện nối tiếp phải thực hiện việc chuyển dữ "
               "liệu từ dạng song song của bus dữ liệu nội bộ SBC sang và ngược lại từ dạng nối "
               "tiếp mà chuẩn giao diện sử dụng (ví dụ RS-232 hoặc RS-422). Một số SBC có thể "
               "chứa thêm giao diện để hỗ trợ giao tiếp với màn hình (VDU), mạng cục bộ (LAN) "
               "hoặc ổ đĩa. Giao diện có thể dao động rất rộng về độ phức tạp, từ một chip giao "
               "diện song song duy nhất đến một bộ điều khiển LAN có thể chiếm một phần đáng kể "
               "diện tích bảng mạch SBC."))

    o.append(h3("Kiến trúc bus máy tính", "Computer Bus Architectures"))
    o.append(p("Tất cả trừ những hệ máy tính đơn giản nhất đều chứa nhiều card mạch in cắm vào "
               "một bảng mạch nền (backplane) in mạch. Các card này bao gồm ít nhất một SBC và "
               "một số card “cắm thêm” cung cấp những chức năng như giao diện tới thiết bị ngoại "
               "vi (ví dụ LAN, màn hình đồ hoạ, ổ đĩa) hoặc bộ nhớ bổ sung. Cấu trúc thực tế "
               "của các kiến trúc bus khá đa dạng, nhưng mô hình đơn giản ở Hình 86.3 chứa "
               "những đặc điểm thiết yếu. Một nhóm đường mạch sẽ mang thông tin dữ liệu và địa "
               "chỉ, cùng với một nhóm đường thứ hai dùng để điều khiển luồng dữ liệu và bảo "
               "đảm việc truyền tin cậy. Những đường khác được dành cho các tín hiệu phân xử "
               "giữa các card SBC, bảo đảm rằng tại mỗi thời điểm chỉ có một card như vậy nắm "
               "quyền điều khiển bus. Sẽ còn có những đường cung cấp các chức năng tiện ích như "
               "tín hiệu đồng hồ và việc truyền các tín hiệu sự kiện hoặc ngắt."))
    o.append(fig(3))
    o.append(p("Ưu điểm chính của các hệ dựa trên bus là chúng giúp ta xây dựng một hệ máy tính "
               "phức tạp từ những card tiêu chuẩn. Bằng cách tuân theo những bus đã được thoả "
               "thuận (xem Bảng 86.1 để có các ví dụ tiêu biểu), người tích hợp hệ thống có thể "
               "giảm thiểu các vấn đề không tương thích và giữ chi phí hệ thống ở mức thấp "
               "nhất. Độ phức tạp của nhiều hệ bus lớn đến mức một phần đáng kể diện tích mỗi "
               "card được dành cho phần logic cần thiết để giao tiếp với bus, làm tăng đáng kể "
               "chi phí. Thêm vào đó, việc truyền dữ liệu giữa các card, kể cả khi dùng DMA, "
               "vẫn tương đối chậm so với việc truyền giữa các chip trên cùng một SBC. Do đó có "
               "sự đánh đổi giữa việc tích hợp các chức năng trên một SBC duy nhất và sự thiếu "
               "linh hoạt trong việc tuỳ biến hệ thống. Một giải pháp thay thế cho các hệ dựa "
               "trên bus là dùng những bộ xử lý như transputer, vốn được thiết kế để nối trực "
               "tiếp với nhau thành những cấu trúc đa bộ xử lý."))
    o.append(table_86_1("vi"))
    o.append(p("Hầu hết các hệ máy tính hiện đại đều áp dụng một hình thức nào đó của chiến "
               "lược <b>trí tuệ phân tán</b> nhằm giải phóng đơn vị xử lý trung tâm để chạy "
               "chương trình ứng dụng chính. Các card điều khiển đồ hoạ thường dùng một bộ xử "
               "lý đồ hoạ chuyên dụng có khả năng đảm nhận việc tạo ra những đặc điểm cơ bản "
               "như vẽ đường hoặc thay đổi tỉ lệ kích thước các đối tượng. Card điều khiển LAN "
               "cần trí tuệ để xử lý các giao thức mạng và đệm luồng dữ liệu vào và ra khỏi "
               "mạng. Card điều khiển ổ đĩa giải phóng bộ xử lý trung tâm khỏi việc phải xử lý "
               "các quá trình đọc và ghi lên đĩa."))
    o.append(p("Việc dùng một hệ bus với nhiều hơn một SBC cho phép nhà thiết kế dành riêng một "
               "SBC cho quá trình thu thập dữ liệu và lưu trữ dữ liệu tạm thời, nhằm bảo đảm "
               "SBC chính có thể tập trung vào việc xử lý dữ liệu và giao tiếp với người dùng. "
               "Chiến lược như vậy cho phép SBC thu thập dữ liệu duy trì được đáp ứng thời gian "
               "thực khi thực hiện phép đo, đồng thời vẫn cho người dùng truy cập dữ liệu đã xử "
               "lý. Trong hầu hết các hệ, một trong các SBC đóng vai trò <b>bộ điều khiển hệ "
               "thống</b>, có quyền điều khiển tối cao đối với việc sử dụng bus và thường chứa "
               "phần cứng phân xử bus. Tại mỗi thời điểm chỉ một SBC có thể nhận được quyền của "
               "bộ điều khiển để trở thành <b>chủ bus</b> và khởi phát việc truyền dữ liệu. Các "
               "card khác sẽ được cấu hình làm <b>tớ</b> (slave), cho phép chúng đáp ứng các "
               "yêu cầu thông tin từ phía chủ. Trong một số hệ, ví dụ Multibus II, việc phân xử "
               "bus được phân tán trên khắp các card thông minh."))

    o.append(h3("Máy tính công nghiệp", "Industrial Computers"))
    o.append(p("Nhiều hệ đo lường sử dụng PC hoặc trạm làm việc tiêu chuẩn, hoặc được trang bị "
               "card cắm thêm, hoặc được nối với những thiết bị đo thông minh qua các giao thức "
               "tiêu chuẩn như IEEE-488 hoặc RS-232. Trong nhiều môi trường công nghiệp, cần có "
               "biện pháp bảo vệ trước những mối nguy như bụi, hư hại do va đập hoặc rung động, "
               "và truy cập trái phép. Các hệ này có thể phải đáp ứng những yêu cầu về tương "
               "thích điện từ (EMC) khắt khe hơn. Có sẵn những phiên bản công nghiệp hoặc gia "
               "cố của máy tính để bàn để đáp ứng thị trường này. Những khung thẻ (cardframe) "
               "được thiết kế để chứa các hệ bus công nghiệp tiêu chuẩn như VME và Multibus có "
               "thể được tuỳ biến dễ dàng cho phù hợp với đòi hỏi của môi trường công nghiệp, "
               "và cũng có sẵn những phiên bản PC được gia cố. Khi thiết kế máy tính công "
               "nghiệp, phải chú ý chỉ định bộ nguồn thoả đáng, vừa để cung cấp đủ dòng cho các "
               "card cắm thêm, vừa để bảo vệ trước những dao động của nguồn điện lưới. Trong "
               "những ứng dụng trọng yếu về an toàn, cũng có thể cần dùng bộ nguồn không gián "
               "đoạn để bảo đảm hệ thống hoạt động trong những lần mất điện lưới ngắn."))

    o.append(h3("Phần mềm", "Software"))
    o.append(p("Tất cả trừ những hệ máy tính đơn giản nhất đều cần một hệ điều hành để hỗ trợ "
               "hoạt động của phần mềm ứng dụng. Hệ điều hành sẽ cấp phát những vùng bộ nhớ cho "
               "các chương trình ứng dụng dùng và cung cấp cơ chế để truy cập các tài nguyên hệ "
               "thống như máy in hay màn hình. Một số hệ điều hành, như MS DOS, là hệ đơn nhiệm, "
               "nghĩa là chúng chỉ hỗ trợ hoạt động của một chương trình hay một tác vụ tại một "
               "thời điểm. Những hệ đo lường đồng thời thực hiện phép đo, xử lý dữ liệu và cho "
               "phép người dùng truy cập thông tin nói chung cần một hệ điều hành đa nhiệm, như "
               "OS-9, UNIX hay Windows 95. Trong những hệ đo lường như vậy, phần mềm ứng dụng "
               "có thể chỉ là một chương trình duy nhất, nhưng nó có thể sinh ra các tiến trình "
               "hay tác vụ phần mềm, mỗi tiến trình có dữ liệu và mã cục bộ riêng. Hệ điều hành "
               "đa nhiệm sẽ cho phép lập lịch việc thực thi thực tế của các tác vụ này, đồng "
               "thời cung cấp cơ chế trao đổi thông tin giữa các tác vụ và đồng bộ hoá các tác "
               "vụ."))
    o.append(p("Các hệ đo lường là những môi trường thời gian thực, nghĩa là hoạt động của "
               "chúng đòi hỏi các tác vụ phải được thực hiện trong những khoảng thời gian xác "
               "định; ví dụ, việc thu nhận dữ liệu phải xảy ra tại những thời điểm xác định. "
               "Các hệ điều hành áp dụng nhiều chiến lược khác nhau để quyết định việc lập lịch "
               "các tác vụ phần mềm. Lập lịch luân phiên (round-robin), chẳng hạn, cấp cho mỗi "
               "tác vụ thời gian thực thi theo kiểu xoay vòng, với lượng thời gian được quyết "
               "định bởi độ ưu tiên của tác vụ. Những hệ điều hành hỗ trợ lập lịch tiếm quyền "
               "(preemptive) cho phép các tác vụ ưu tiên cao trở nên hoạt động nếu một sự kiện "
               "xác định như tín hiệu kích hoạt xuất hiện. Tốc độ mà hệ điều hành có thể "
               "chuyển từ tác vụ này sang tác vụ khác (tức là chuyển ngữ cảnh) là một thước đo "
               "quan trọng đối với các hệ thời gian thực."))
    o.append(p("Mức độ mà một hệ điều hành có thể đáp ứng một số lượng lớn các sự kiện là cực "
               "kỳ hạn chế, vì những tác vụ ưu tiên thấp sẽ có thời gian đáp ứng kém. Nếu một "
               "hệ đo lường cần thực hiện nhiều phép đo và đồng thời hỗ trợ những hoạt động "
               "khác như hiển thị thông tin, thì giải pháp nói chung là dùng một hệ phân tán "
               "với những SBC chuyên dụng hoạt động như các bộ vi điều khiển để thu thập dữ "
               "liệu. Những bộ vi điều khiển này thường không cần hệ điều hành và mỗi bộ chạy "
               "một chương trình duy nhất, hoặc được nạp xuống từ SBC chính, hoặc nằm trong "
               "ROM."))
    o.append(p("Có sẵn những gói thương mại (xem Bảng 86.2 để có ví dụ) để hỗ trợ các hệ đo "
               "lường dựa trên PC/trạm làm việc. Một hệ tiêu biểu sẽ cung cấp một môi trường "
               "kiểu Windows để điều khiển các phép đo và lưu trữ, xử lý, hiển thị dữ liệu, "
               "đồng thời ngày càng tận dụng khái niệm <b>thiết bị đo ảo</b>, vốn cho phép "
               "người dùng cấu hình hệ đo lường từ một trình đơn trên màn hình. Hầu hết các gói "
               "phần mềm cho phép điều khiển những thiết bị đo độc lập bằng các card giao diện "
               "hỗ trợ những chuẩn như IEEE-488 hay RS-232. Một số gói còn hỗ trợ dùng card cắm "
               "thêm để chuyển đổi tương tự–số hoặc một loạt chức năng điều khiển như chuyển "
               "kênh và tạo dạng sóng; tuy vậy, hạn chế chính của chúng là dải cấu hình phần "
               "cứng mà nhà cung cấp phần mềm hỗ trợ còn hẹp."))
    o.append(table_86_2("vi"))
    o.append(p("Mỗi thiết bị đo độc lập và mỗi card cắm thêm đều cần một đoạn mã gọi là <b>"
               "trình điều khiển thiết bị</b> (device driver) để hệ điều hành có thể truy cập "
               "các tài nguyên phần cứng của card và của thiết bị đo. Do đó, việc phát triển "
               "trình điều khiển thiết bị đòi hỏi hiểu biết sâu sắc về cả phần cứng lẫn hệ điều "
               "hành."))

    o.append(h3("Phát triển hệ thống", "System Development"))
    o.append(p("Thành phần phần mềm của bất kỳ hệ đo lường có máy tính nào cũng có thể chiếm "
               "một tỉ lệ đáng kể trong tổng chi phí. Điều này đặc biệt đúng với những hệ làm "
               "một lần (on-off), tức những hệ cần phần mềm được phát triển riêng cho một ứng "
               "dụng cụ thể, khi mà chi phí triển khai phần mềm và bảo trì nó có thể vượt xa "
               "chi phí phần cứng. Trong những hoàn cảnh như vậy, khả năng tái sử dụng mã sẵn "
               "có cùng việc tiếp cận những hệ phát triển mạnh và công cụ gỡ lỗi là những yếu "
               "tố then chốt. Một số phần mềm gỡ lỗi chỉ hỗ trợ việc chạy từng bước qua hoạt "
               "động của mã viết ở mức mã hợp ngữ. Khi phát triển trình điều khiển thiết bị, "
               "chẳng hạn, sẽ rất hữu ích nếu có một trình gỡ lỗi mức mã nguồn, vốn có thể liên "
               "kết việc thực thi mã viết bằng ngôn ngữ bậc cao với nội dung các thanh ghi của "
               "bộ xử lý."))
    o.append(p("Nhiều SBC được thiết kế để hoạt động như những bộ vi điều khiển độc lập, thay "
               "vì trong các hệ dựa trên bus, thường được hỗ trợ bởi một ngôn ngữ bậc cao như C "
               "hoặc FORTH cùng một môi trường phát triển. Một cách làm phổ biến là dùng một PC "
               "để phát triển mã, rồi nạp mã đó qua một liên kết nối tiếp xuống bộ vi điều "
               "khiển. Một số hỗ trợ gỡ lỗi cho việc thực thi mã trên bộ vi điều khiển cũng "
               "được cung cấp. Việc phát triển những card vi điều khiển Intel 486 hoặc Pentium "
               "nhỏ gọn mà mạnh, chạy những hệ điều hành như MS DOS, có thể rút ngắn đáng kể "
               "thời gian phát triển phần mềm nhờ việc tiếp cận sẵn có phần mềm trên PC. Việc "
               "triển khai những hệ dựa trên bộ vi điều khiển chuyên dụng có thể cần dùng một "
               "máy phân tích logic để xem dữ liệu trên các bus của hệ thống."))

    # ---------------------------------------------------------------- 86.3
    o.append(h2("86.3 Bus máy tính", "Computer Buses"))
    o.append(h3("VMEbus (IEEE P1014)", "The VMEbus (IEEE P1014)"))
    o.append(p("VMEbus [1–3] dùng một bảng mạch nền được trang bị hai đầu nối 96 chân (gọi là "
               "P1 và P2). Đầu nối P1 cung cấp quyền truy cập tới toàn bộ các tín hiệu bus, trừ "
               "các bit 16 đến 31 của bus dữ liệu và các bit 24 đến 31 của bus địa chỉ — những "
               "bit này được cung cấp trên đầu nối P2. Vị trí của các card trong một hệ VME là "
               "quan trọng, vì khe 1 phải chứa bộ điều khiển hệ thống và độ ưu tiên của các SBC "
               "được quyết định bởi khoảng cách của chúng tới SBC điều khiển hệ thống. Vì chỉ "
               "có 32 trong số các chân trên đầu nối P2 là đã được định nghĩa, 64 đường còn lại "
               "trên bảng mạch nền P2 có thể do người dùng tự quy định. Card VME có thể là loại "
               "một tầng (chỉ có đầu nối P1) hoặc hai tầng (có cả đầu nối P1 và P2). Bảng một "
               "tầng cao 100 mm và sâu 160 mm, lắp vào khung thẻ chiều cao 3U. Bảng hai tầng "
               "cao 233,35 mm và sâu 160 mm, lắp vào khung thẻ chiều cao 6U."))

    o.append(h4("Tín hiệu VMEbus", "VMEbus Signals"))
    o.append(p("Có thể mô tả VMEbus như có bốn nhóm tín hiệu riêng biệt."))
    o.append(p("<b>Bus truyền dữ liệu (DTB).</b> DTB cung cấp việc truyền dữ liệu 32 bit với "
               "thông tin địa chỉ 32 bit theo cách không đồng bộ, không ghép kênh. Việc truyền "
               "được hỗ trợ bởi một cơ chế bắt tay đơn giản, trong đó chủ bus khởi phát việc "
               "truyền phát tín hiệu chốt địa chỉ (AS) để báo cho card đích đọc thông tin địa "
               "chỉ. Chủ bus cũng điều khiển hai đường chốt dữ liệu (DS1 và DS2), mà trong một "
               "thao tác ghi cho biết có dữ liệu hợp lệ trên bus dữ liệu, còn trong một thao "
               "tác đọc thì cho biết chủ bus đã sẵn sàng nhận dữ liệu từ tớ. Card tớ dùng tín "
               "hiệu xác nhận dữ liệu (DTACK), trong thao tác đọc để cho biết nó đã đặt dữ "
               "liệu hợp lệ lên bus, và trong thao tác ghi để xác nhận rằng nó đã đọc được dữ "
               "liệu. Rõ ràng có nguy cơ bus bị treo nếu tớ không đáp ứng một yêu cầu truyền dữ "
               "liệu, nên trong hầu hết các hệ VME người ta cung cấp một bộ định thời canh gác "
               "(watchdog timer) để phát tín hiệu trên đường lỗi bus (BERR) nếu không phát hiện "
               "được tín hiệu DTACK trong khoảng thời gian chờ."))
    o.append(p("Bản sửa đổi C của đặc tả bus VME sẽ hỗ trợ các phép truyền dữ liệu 8, 16 và 32 "
               "bit, trong khi bản sửa đổi D hỗ trợ truyền 64 bit bằng cách dùng bus địa chỉ để "
               "truyền thêm 32 bit. Dữ liệu cũng có thể được truyền theo khối lên tới 256 byte "
               "mà không cần phát lại thông tin địa chỉ. Hầu hết các SBC đều có cả giao diện "
               "chủ lẫn giao diện tớ, cho phép bộ nhớ của chúng được truy cập từ những SBC khác "
               "trong hệ. Bus VME cũng hỗ trợ ba kiểu chế độ địa chỉ: ngắn (16 bit), chuẩn "
               "(24 bit) và mở rộng (32 bit), cho phép giảm thiểu mạch giải mã bộ nhớ của các "
               "card trong những hệ nhỏ hoặc đối với các card vào/ra. Sáu đường bộ sửa đổi địa "
               "chỉ (AM0 đến AM5) được dùng để chỉ ra chế độ địa chỉ và đồng thời cung cấp "
               "thông tin về chế độ truyền (ví dụ truyền khối, và việc truyền diễn ra ở chế độ "
               "đặc quyền, giám sát hay không đặc quyền)."))
    o.append(p("<b>Bus phân xử.</b> Bus phân xử cung cấp cơ chế để quyết định chủ nào được phép "
               "nắm quyền điều khiển bus. Bus phân xử cung cấp bốn đường yêu cầu bus (BR0 đến "
               "BR3) và bốn đường cấp bus. SBC ở khe 1 của bus VME đóng vai trò bộ điều khiển "
               "bus, thực hiện việc phân xử bằng một số thuật toán lập lịch. Trong một thuật "
               "toán đơn giản dựa trên độ ưu tiên, mỗi đường yêu cầu bus được gán một độ ưu "
               "tiên; còn trong một hệ luân phiên (round-robin) thì quyền truy cập bus xoay "
               "vòng qua các đường yêu cầu bus. Mỗi trong bốn đường cấp bus thực ra được cấp "
               "hai chân trên đầu nối P1 (xem Hình 86.4). Do đó tín hiệu cấp bus đi xuyên qua "
               "từng card (gọi là chuỗi nối tiếp, daisy chaining); như vậy, ở Hình 86.4 tín "
               "hiệu vào qua BG1IN và ra qua BG1OUT. Sơ đồ này cho phép một card chặn tín hiệu "
               "cấp bus, khiến những card gần bộ điều khiển hệ thống hơn có độ ưu tiên cao hơn. "
               "Một hệ quả của chuỗi nối tiếp là mọi khe card không dùng đến đều phải được gắn "
               "jumper giữa các chân cấp bus."))
    o.append(fig(4))
    o.append(p("<b>Bus ngắt ưu tiên.</b> Bus ngắt ưu tiên cung cấp bảy đường yêu cầu ngắt "
               "(IRQ1 đến IRQ7), trong đó IRQ7 có độ ưu tiên cao nhất. Các yêu cầu ngắt có thể "
               "được xử lý bởi nhiều SBC, miễn là mọi ngắt cùng mức được xử lý bởi cùng một "
               "chủ. Đường xác nhận ngắt được nối chuỗi qua các card theo cách tương tự các "
               "đường cấp bus (các chân được gọi là IACKIN và IACKOUT). Một lần nữa, mọi khe "
               "card không dùng đến đều phải được gắn jumper giữa các chân này."))
    o.append(p("<b>Bus tiện ích.</b> Bus tiện ích cung cấp các đường cấp nguồn, tín hiệu khởi "
               "động lại hệ thống, một đồng hồ 16 MHz và hai đường báo hỏng hệ thống: SYSFAIL, "
               "cho phép một card báo rằng nó đã gặp sự cố, và ACFAIL, do bộ giám sát nguồn "
               "sinh ra. Cả hai đường báo hỏng đều được xử lý bởi SBC điều khiển hệ thống."))
    o.append(p("Gắn liền với VMEbus là VXI (phần mở rộng VMEbus dành cho đo lường). Chuẩn này "
               "kết hợp chuẩn VMEbus IEEE 1014 với bus đo lường IEEE-488, dùng những chân chưa "
               "được cam kết trên đầu nối P2, để tạo thành chuẩn IEEE P1155."))

    o.append(h3("Multibus II (IEEE 1296)", "Multibus II (IEEE 1296)"))
    o.append(p("Multibus II [3] là một hệ bus đồng bộ, được triển khai trên một bảng mạch nền "
               "96 đường duy nhất. Card tuân theo khuôn dạng Eurocard 220 × 233,65 mm; tuy vậy, "
               "bus chỉ cần một đầu nối kiểu DIN 41612 96 chân duy nhất. Đầu nối thứ hai có thể "
               "được dùng để hỗ trợ một bus cục bộ hoặc chỉ để tạo độ ổn định cơ học cho một "
               "card hai tầng."))
    o.append(p("Khác với VME, chuẩn Multibus II có những đặc điểm sau:"))
    o.append(ol([
        "Một bus đồng bộ, nghĩa là việc truyền dữ liệu gắn với đồng hồ bus thay vì với các "
        "đường điều khiển chốt/xác nhận của hệ VME không đồng bộ;",
        "Một bus địa chỉ và dữ liệu ghép kênh 32 bit;",
        "Một chiến lược truyền thông điệp thay thế cho các đường yêu cầu ngắt;",
        "Phân xử bus phân tán thay vì một bộ điều khiển hệ thống tập trung (mỗi card chứa một "
        "chip điều khiển truyền thông điệp, MPC, tham gia thực hiện thuật toán truyền thông "
        "điệp);",
        "Chỉ những card thông minh (tức là có gắn bộ vi xử lý) mới có thể giao tiếp với bus "
        "chính; những card vào/ra (I/O) đơn giản nên dùng một bus cục bộ (ví dụ bus iLBX) qua "
        "đầu nối DIN thứ hai.",
    ]))

    o.append(h4("Tín hiệu Multibus", "Multibus Signals"))
    o.append(p("Có thể mô tả Multibus II như có năm nhóm tín hiệu riêng biệt."))
    o.append(p("<b>Điều khiển trung tâm.</b> Mô-đun dịch vụ trung tâm (CSM) ở khe 0 chịu trách "
               "nhiệm sinh ra nhóm tín hiệu này. CSM có thể được triển khai trên một card "
               "chuyên dụng hoặc được tích hợp vào một SBC. CSM tạo ra đồng hồ bus 10 MHz cùng "
               "một loạt tín hiệu khởi động lại để hỗ trợ cả khởi động nguội lẫn khởi động ấm, "
               "cũng như phục hồi sau sự cố nguồn."))
    o.append(p("<b>Địa chỉ/dữ liệu.</b> Multibus II hỗ trợ một bus địa chỉ/dữ liệu ghép kênh 32 "
               "bit (AD0 đến AD31) với bốn đường chẵn lẻ (PAR0 đến PAR3) cung cấp thông tin "
               "chẵn lẻ cho từng byte dữ liệu. Như trong mọi hệ đồng bộ, dữ liệu chỉ được lấy "
               "mẫu tại một sườn của đồng hồ hệ thống — một đặc điểm giúp tăng khả năng chống "
               "nhiễu."))
    o.append(p("<b>Điều khiển hệ thống.</b> Có mười đường điều khiển hệ thống (SC0 đến SC9) "
               "cung cấp thông tin bắt tay cơ bản để hỗ trợ việc truyền dữ liệu, ví dụ bên yêu "
               "cầu đã sẵn sàng hoặc bên đáp chưa sẵn sàng. Ngoài ra, những đường này còn được "
               "dùng để chuyển tải thông tin như độ rộng dữ liệu, chỉ báo lỗi dữ liệu, và việc "
               "bus đang ở pha yêu cầu hay pha đáp."))
    o.append(p("<b>Tín hiệu ngoại lệ.</b> Có hai tín hiệu ngoại lệ: lỗi bus (BUSERR) và quá "
               "thời (TIMOUT). Bất kỳ card nào phát hiện vấn đề về tính toàn vẹn dữ liệu đều "
               "phải báo cho mọi card khác bằng BUSERR. CSM sinh ra TIMOUT khi nó phát hiện một "
               "cuộc truyền dữ liệu bị treo trên bus."))
    o.append(p("<b>Nhóm phân xử.</b> Các tín hiệu phân xử, vốn quyết định card nào giành được "
               "quyền điều khiển bus, gồm một đường yêu cầu bus duy nhất (BREQ) và sáu đường "
               "phân xử bus (ARB0 đến ARB5). Để yêu cầu độc quyền sử dụng bus, một card đặt "
               "mức tích cực trên đường BREQ và đưa mã nhận dạng phân xử của nó lên ARB0 đến "
               "ARB4. Nó cũng dùng ARB5 để cho biết yêu cầu là ưu tiên cao hay liệu “chế độ "
               "công bằng” có được chấp nhận hay không. Ở chế độ sau, card sẽ không đưa ra yêu "
               "cầu tiếp theo cho đến khi mọi bên yêu cầu khác đã dùng bus. Mỗi card có cùng "
               "phần logic phân xử bus như vậy bên trong chip MPC của nó. Nếu nhiều card cùng "
               "đưa ra yêu cầu ưu tiên cao, thứ tự truy cập được quyết định bởi giá trị số của "
               "mã nhận dạng phân xử."))

    o.append(h4("Truyền thông điệp trên Multibus II", "Message Passing on Multibus II"))
    o.append(p("Multibus II dùng việc truyền thông điệp để thực hiện các phép truyền dữ liệu "
               "theo khối và các yêu cầu ngắt. Mỗi chip MPC chứa một bộ đệm vào trước ra trước "
               "(FIFO), bảo đảm có thể tận dụng toàn bộ băng thông của bus nhờ lưu dữ liệu ngay "
               "trước hoặc ngay sau khi truyền. Trong những lần truyền “có yêu cầu” "
               "(solicited), các MPC phối hợp với nhau bằng cách báo trước cho nhau rằng một "
               "thông điệp sắp được gửi. Những thông điệp này có thể được gửi thành các gói 32 "
               "byte theo cách tương tự cơ chế truyền khối trong VME. Những gói “không yêu cầu” "
               "(unsolicited) mà MPC nhận không chờ trước được dùng để thiết lập một cuộc "
               "truyền khối hoặc đóng vai trò tương đương các tín hiệu yêu cầu ngắt."))

    o.append(h4("Cấu hình hệ thống", "System Configuration"))
    o.append(p("Multibus II áp dụng cách tiếp cận cấu hình bằng phần mềm, trong đó những thông "
               "tin như địa chỉ bộ nhớ gốc và mã nhận dạng phân xử được gửi xuống qua bus thay "
               "vì dùng jumper hay công tắc DIP. Một số thông tin như loại card và số sê-ri "
               "được mã hoá ngay trên card."))

    o.append(h3("Các bus hệ thống khác cho hệ quy mô nhỏ",
                "Other System Buses for Small-Scale Systems"))
    o.append(p("Các chuẩn G64/G96 và STE [3] là những ví dụ về bus rất phù hợp với các hệ đo "
               "lường và điều khiển công nghiệp thời gian thực quy mô nhỏ, nhờ giao diện bus "
               "tương đối đơn giản và do đó rẻ hơn so với VME và Multibus. Cả hai bus đều hỗ "
               "trợ DMA, có phân xử bus đa bộ xử lý và dùng card Eurocard một tầng "
               "(100 × 160 mm). Có sẵn những card tạo mẫu (prototyping) có gắn giao diện bus, "
               "có thể dùng để phát triển những card I/O thiết kế riêng. Nguồn được cấp trên "
               "bus ở mức +5 và ±12 V. Ngoài ra, hệ điều hành đa nhiệm thời gian thực OS-9 đã "
               "được chuyển sang các SBC hoạt động với những bus này. Cũng có sẵn những hệ phát "
               "triển hỗ trợ dùng MS-DOS, nhờ đó tiếp cận được một dải rộng phần mềm dựa trên "
               "PC, đặc biệt cho các ứng dụng đồ hoạ."))
    o.append(p("Bus G64, do hãng Gespac của Thuỵ Sĩ định nghĩa năm 1979, quy định 64 đường bus "
               "được ánh xạ vào các hàng của một đầu nối DIN41612. Bus có một bus dữ liệu 16 "
               "bit không ghép kênh và một bus địa chỉ 16 bit; có thể đạt được các phép truyền "
               "32 bit bằng cách ghép kênh 16 bit trên của bus dữ liệu với bus địa chỉ. Chuẩn "
               "G96 thêm 32 đường bus nữa bằng cách dùng hàng thứ ba của một đầu nối DIN41612 "
               "để mở rộng độ rộng bus địa chỉ lên 24 bit và cung cấp thêm các đường yêu cầu "
               "ngắt. Bus STE cung cấp một bus dữ liệu 8 bit và bus địa chỉ 20 bit không ghép "
               "kênh, dùng các đầu nối DIN41612 64 chân."))

    # ---------------------------------------------------------------- 86.4
    o.append(h2("86.4 Bus máy tính cá nhân", "Personal Computer Buses"))
    o.append(p("Có ba chuẩn bus chính cho máy tính cá nhân — kiến trúc chuẩn công nghiệp "
               "(ISA), ISA mở rộng (EISA) và kiến trúc kênh vi mô (MCA). Ngoài ra, kiến trúc "
               "của Hiệp hội Quốc tế Thẻ nhớ Máy tính Cá nhân (PCMCIA) được phát triển chủ yếu "
               "để dùng trong máy tính xách tay và sổ tay."))
    o.append(p("ISA và EISA tương thích về chân và đều là bus đồng bộ với tốc độ đồng hồ 8 "
               "MHz, bất kể tốc độ đồng hồ của bộ xử lý chính, trong khi bus MCA là một bus "
               "không đồng bộ. Những card cắm thêm đóng vai trò tớ chậm có thể dùng bus ISA và "
               "EISA bằng cách sử dụng một số trạng thái chờ (wait state) thích hợp. Kiến trúc "
               "MCA sẽ không được đề cập trong chương này. Chi tiết thêm về các kiến trúc bus "
               "này được trình bày trong các tài liệu tham khảo 4 đến 6."))

    o.append(h3("Bus ISA", "ISA Bus"))
    o.append(p("Chiếc IBM PC nguyên bản và các bản sao của nó dùng bus PC tiêu chuẩn, vốn hỗ "
               "trợ 8 đường bus dữ liệu và 20 đường bus địa chỉ, và dùng một đầu nối cạnh card "
               "in mạch 62 chân. Khi IBM giới thiệu PC-AT, một đầu nối thứ hai 36 chân được "
               "thêm vào các khe trên bảng mạch nền để cung cấp bus dữ liệu 16 bit và tăng số "
               "đường địa chỉ lên 24. Bus mới này về sau được biết đến với tên bus ISA, và có "
               "khả năng hỗ trợ cả những card thiết kế cho bus PC nguyên bản lẫn những card có "
               "hai đầu nối cung cấp truy cập dữ liệu 16 bit đầy đủ. Đường chủ bus cho phép một "
               "card nắm quyền điều khiển bus; tuy vậy, điều này nói chung chỉ thích hợp cho "
               "những lần nắm quyền dài hạn. Bus ISA hỗ trợ các phép truyền DMA 8 bit và 16 "
               "bit, cho phép truyền hiệu quả các khối dữ liệu, ví dụ khi nạp phần mềm từ đĩa "
               "vào RAM. Bus ISA hỗ trợ chế độ địa chỉ vào/ra của dòng bộ xử lý Intel 80×86 với "
               "một không gian địa chỉ vào/ra 768 vị trí, thêm vào 256 vị trí được dành cho "
               "bảng mạch chủ."))

    o.append(h3("Bus EISA", "EISA Bus"))
    o.append(p("Bus EISA cung cấp đầy đủ các đường bus dữ liệu 32 bit và bus địa chỉ 32 bit. "
               "Card ISA có thể lắp vào các đầu nối bus EISA; tuy vậy, những card thiết kế cho "
               "chuẩn EISA có đầu nối cạnh hai mức, cung cấp số tiếp điểm gấp đôi so với một "
               "card ISA. Sự có mặt của một rãnh trên card EISA cho phép chúng được cắm sâu hơn "
               "vào ổ cắm trên bảng mạch chủ so với card ISA, và nhờ vậy ăn khớp với các tiếp "
               "điểm bổ sung. Chuẩn EISA tăng độ rộng dữ liệu tối đa của ISA trong truyền DMA "
               "lên 32 bit và cũng cung cấp một cơ chế chủ bus mạnh hơn nhiều. Những đặc điểm "
               "sau của EISA đáng được lưu ý."))
    o.append(h4("Phân xử bus", "Bus Arbitration"))
    o.append(p("Mọi hệ EISA đều có một thiết bị điều khiển phân xử trung tâm (CAC) trên bảng "
               "mạch chủ. CAC dùng một sơ đồ phân xử ưu tiên xoay vòng nhiều mức. Mức ưu tiên "
               "cao nhất xoay vòng qua ba khách hàng: bộ điều khiển DMA, bộ điều khiển làm mới "
               "bộ nhớ động, và luân phiên hoặc CPU chính hoặc một trong các card chủ bus. Một "
               "thiết bị không đưa ra yêu cầu sẽ bị bỏ qua trong quá trình xoay vòng. Các chủ "
               "bus lần lượt nhau giành được mức ưu tiên cao nhất. Trong khi ISA chỉ hỗ trợ một "
               "đường yêu cầu bus duy nhất, chuẩn EISA cung cấp một cặp đường yêu cầu "
               "(MREQ0 đến 14) và đường xác nhận (MAK0 đến 14) riêng cho mỗi chủ bus. (Lưu ý: "
               "mặc dù điều này cho phép dùng 15 chủ bus, trong nhiều hệ thì chipset thực hiện "
               "CAC chỉ hỗ trợ chủ bus ở một số ổ cắm EISA nhất định.) CAC hỗ trợ tiếm quyền, "
               "nghĩa là nó cho phép một thiết bị đang đưa ra yêu cầu giành quyền điều khiển từ "
               "một thiết bị khác nếu đến lượt nó. Một card chủ bus phải nhả bus trong vòng 64 "
               "chu kỳ đồng hồ bus, trong khi bộ điều khiển DMA có 32 chu kỳ đồng hồ để trao "
               "trả bus."))
    o.append(h4("Vào/ra", "Input/Output"))
    o.append(p("Bus EISA cung cấp thêm 768 vị trí vào/ra cho mỗi khe, thêm vào 768 vị trí vào/"
               "ra ISA vốn có thể được truy cập từ bất kỳ khe nào. Card EISA chứa bộ nhớ không "
               "bay hơi để lưu thông tin cấu hình (xem bên dưới), và tối thiểu 340 byte trong "
               "không gian địa chỉ vào/ra của mỗi khe được dành cho mục đích này."))
    o.append(h4("Cấu hình hệ thống", "System Configuration"))
    o.append(p("Hệ EISA cung cấp sự hỗ trợ cho việc tự động cấu hình hệ thống, thay thế việc "
               "dùng jumper và công tắc DIP để chỉ định những tham số như địa chỉ bộ nhớ gốc, "
               "số đường yêu cầu ngắt hoặc số kênh DMA mà mỗi card cắm thêm sử dụng. Thông tin "
               "về loại sản phẩm và nhà sản xuất được lưu trên mỗi card cắm thêm EISA, được CPU "
               "đọc trong lúc khởi động hệ thống, nhờ đó có thể nhận ra những khe đang lắp card "
               "EISA đầy đủ. Các nhà sản xuất card ISA và EISA đều nên cung cấp một tệp cấu "
               "hình chứa thông tin về những tuỳ chọn lập trình được sẵn có. Khi một chương "
               "trình cấu hình hệ thống được chạy, một cấu hình tối ưu cho các bảng mạch sẽ "
               "được xác định và thông tin cấu hình được ghi vào không gian vào/ra của mỗi "
               "card EISA. Với card ISA, người dùng có thể được thông báo về các thiết lập "
               "jumper cần thiết."))

    o.append(h3("PCMCIA", "PCMCIA"))
    o.append(p("Kiến trúc PCMCIA được Hiệp hội Quốc tế Thẻ nhớ Máy tính Cá nhân và Hiệp hội "
               "Phát triển Công nghiệp Điện tử Nhật Bản phát triển cho những card cắm thêm tháo "
               "lắp được của máy tính xách tay và sổ tay. Mỗi ổ cắm PCMCIA có bộ điều hợp bus "
               "chủ (HBA) riêng, đóng vai trò giao diện với bus chính của máy tính. Card có thể "
               "được cắm vào ổ cắm PCMCIA trước hoặc sau khi máy tính đã được bật nguồn. Có ba "
               "loại card PC, tất cả đều có cùng kích thước phẳng (54,00 × 85,6 mm) nhưng khác "
               "nhau về độ dày, cụ thể là 3,3 mm với loại I, 5,0 mm với loại II và 10,5 mm với "
               "loại III. Card và ổ cắm được làm khoá rãnh để tránh cắm ngược chiều. Chuẩn "
               "PCMCIA hỗ trợ những card hoạt động ở nhiều mức điện áp khác nhau, cụ thể là "
               "card 5,0 V, card 3,3 V hoặc card hai điện áp 5,0 V/3,3 V."))
    o.append(h4("Cấu hình", "Configuration"))
    o.append(p("Card PC chứa thông tin cấu hình gọi là cấu trúc thông tin thẻ (CIS), được lưu "
               "trong bộ nhớ không bay hơi. Card có thể được cấu hình hoặc khi hệ thống khởi "
               "động nguồn, hoặc khi card được cắm vào ổ cắm (tức là cắm là chạy). Việc cấu "
               "hình được thực hiện bằng một dạng trình điều khiển thiết bị gọi là bộ kích hoạt "
               "(enabler). Bộ kích hoạt có thể dùng thêm hai dịch vụ phần mềm gọi là dịch vụ "
               "thẻ và dịch vụ ổ cắm. Dịch vụ ổ cắm, có thể nằm trong ROM của PC hoặc được nạp "
               "từ đĩa trong lúc khởi động, cung cấp các lời gọi hàm cho phép cấu hình HBA để "
               "phối hợp với card PC. Dịch vụ thẻ, có thể là một phần mở rộng của hệ điều hành "
               "hoặc một trình điều khiển thiết bị cài đặt được, đóng vai trò máy chủ cho bộ "
               "kích hoạt, vốn hoạt động như một máy khách. Dịch vụ thẻ cung cấp một loạt chức "
               "năng như truy cập CIS của card, yêu cầu các tài nguyên hệ thống mà card cần, và "
               "báo cho bộ kích hoạt biết rằng một card đã được cắm vào hoặc rút ra khỏi ổ cắm. "
               "Bộ kích hoạt có thể được phân loại là chuyên dụng cho một card cụ thể hoặc "
               "tổng quát, nghĩa là được thiết kế cho một dải card. Lưu ý rằng những card "
               "PCMCIA đời đầu không được thiết kế để dùng với dịch vụ thẻ."))
    o.append(h4("Giao diện ổ cắm PCMCIA", "The PCMCIA Socket Interface"))
    o.append(p("Ổ cắm PCMCIA gồm một đầu nối 68 chân với 26 đường địa chỉ cung cấp quyền truy "
               "cập tới 64 MB không gian bộ nhớ và một bus dữ liệu 16 bit. Có hai chân Vcc và "
               "bốn chân nối đất. Dòng tối đa có thể cấp cho card là 1,0 A, với tối đa 0,5 A từ "
               "mỗi chân trong hai chân cấp nguồn. Ổ cắm phiên bản 2.x đặt 5,0 V lên các chân "
               "Vcc khi khởi động nguồn và giảm xuống 3,3 V nếu card có khả năng hai điện áp. "
               "Những card chỉ hoạt động ở 3,3 V được làm khoá rãnh để không thể lắp vào loại "
               "ổ cắm này mà chỉ lắp vào ổ cắm điện áp thấp. Điện áp cấp do ổ cắm điện áp thấp "
               "cung cấp phụ thuộc vào trạng thái logic của các đầu vào cảm nhận điện áp của "
               "nó. Một ổ cắm PCMCIA có thể được cấu hình hoặc như một ổ cắm chỉ dùng cho bộ "
               "nhớ, hoặc như một ổ cắm dùng cho bộ nhớ hoặc vào/ra. Ban đầu ổ cắm hoạt động "
               "như một ổ cắm chỉ dùng cho bộ nhớ, nhưng được bộ kích hoạt chuyển thành ổ cắm "
               "bộ nhớ hoặc vào/ra nếu card cần hỗ trợ các chức năng vào/ra. Ở chế độ này, card "
               "có thể sinh một yêu cầu ngắt qua một chân IRQ duy nhất và hỗ trợ cả truyền dữ "
               "liệu vào/ra 8 bit lẫn 16 bit. DMA có thể được hỗ trợ, nhưng không phải bởi các "
               "hệ phiên bản 2.x."))

    o.append(h3("PC/104", "PC/104"))
    o.append(p("Sự phổ biến to lớn của kiến trúc PC đã dẫn đến việc nó được dùng trong các hệ "
               "nhúng. Từ đó nảy sinh nhu cầu về một cách triển khai bus ISA gọn hơn, có thể "
               "đáp ứng những yêu cầu về không gian và công suất giảm bớt của các ứng dụng "
               "nhúng. Đặc tả PC/104 (1992) được chấp nhận làm cơ sở cho một dự thảo tiêu chuẩn "
               "IEEE có tên P996.1 — Tiêu chuẩn cho các mô-đun PC nhúng gọn. Những đặc điểm "
               "then chốt của PC/104 là:"))
    o.append(ul([
        "Kích thước thu gọn còn 90 × 96 mm (3,550 × 3,775 in.);",
        "Bus tự xếp chồng, cho phép các mô-đun được “cõng” lên nhau và loại bỏ bảng mạch nền "
        "hay khung thẻ;",
        "Đầu nối đực và cái 64 tiếp điểm và 40 tiếp điểm chắc chắn thay cho các đầu nối cạnh "
        "của PC (64 + 40 = 104, do đó có tên PC/104);",
        "Công suất tiêu thụ thấp hơn (< 2 W mỗi mô-đun).",
    ]))
    o.append(p("Các mô-đun CPU PC/104 trải từ một bộ XT 9,6 MHz tương thích 8088 cơ bản với một "
               "cổng nối tiếp và một đầu nối bàn phím, đến một bộ 80486DX4 100 MHz với bốn cổng "
               "nối tiếp, cổng song song, bộ điều khiển ổ đĩa IDE, bộ điều khiển hiển thị, bộ "
               "điều hợp Ethernet, cổng bàn phím và tới 64 MB RAM trên bo. Cũng có sẵn những hệ "
               "dựa trên Pentium. Hệ thống có thể được tuỳ biến từ một dải rộng mô-đun, gồm "
               "những bảng thu thập dữ liệu, mô-đun đĩa bán dẫn và hỗ trợ LAN, tất cả trong "
               "cùng một khuôn dạng xếp chồng 3,6 × 3,8 in."))
    o.append(p("Sự sẵn có rộng rãi của các công cụ phát triển phần mềm cho PC, số lượng lớn "
               "những người phát triển phần mềm quen thuộc với môi trường PC, và sự dễ dàng "
               "chuyển phần mềm đã phát triển trên một PC thông thường sang PC/104 khiến khuôn "
               "dạng này ngày càng phổ biến."))
    o.append(p("Bảng 86.3 liệt kê một số nhà sản xuất và nhà cung cấp hệ thống dựa trên bus và "
               "máy tính công nghiệp."))
    o.append(table_86_3("vi"))

    # ---------------------------------------------------------------- 86.5
    o.append(h2("86.5 Thiết bị ngoại vi", "Peripherals"))
    o.append(p("Thiết bị ngoại vi của máy tính chia thuận tiện thành hai loại. Loại thứ nhất "
               "có thể coi là nội bộ đối với hệ máy tính, gồm những card cắm trực tiếp vào một "
               "khe bus của máy tính. Loại thứ hai gồm những thiết bị đo nằm ngoài máy tính "
               "nhưng được máy tính điều khiển. Những thiết bị đo bên ngoài này thường tự chúng "
               "đã “thông minh”, được điều khiển bởi CPU riêng, và được nối với máy tính chính "
               "bằng một đường nối tiếp (RS-232) hoặc bằng bus IEEE-488 (GPIB). Những thiết bị "
               "như vậy thông thường có thể được vận hành ở chế độ độc lập, đáp lại các điều "
               "khiển trên mặt trước của chúng mà không cần một máy tính bên ngoài."))

    o.append(h3("Card nội bộ", "Internal Cards"))
    o.append(p("Có sẵn những card nội bộ để thực hiện một dải rộng chức năng. Bảng 86.4 đưa ra "
               "một danh sách ngắn gọn các loại tiêu biểu. Lưu ý rằng cả giao diện nối tiếp "
               "lẫn bộ điều hợp IEEE-488 cần cho việc điều khiển các thiết bị ngoại vi “thông "
               "minh” bên ngoài đều sẽ được lắp dưới dạng card nội bộ. Hầu như mọi thiết bị "
               "ngoại vi nội bộ đều cần được cấu hình trước khi dùng để thiết lập những tham số "
               "như địa chỉ gốc, các ngắt và/hoặc các kênh DMA được sử dụng. Việc này có thể "
               "bao gồm đặt jumper hoặc công tắc trên card, hoặc có thể được thực hiện dưới sự "
               "điều khiển của phần mềm bằng một tệp cấu hình do nhà sản xuất cung cấp. Để vận "
               "hành các card, các byte được ghi vào hoặc đọc ra từ những địa chỉ thích hợp "
               "trên card bởi SBC điều khiển. Cơ chế thực hiện việc này được bàn thêm trong "
               "phần nói về phần mềm cho thu thập dữ liệu. Chi tiết thêm về một số loại card "
               "được trình bày dưới đây."))
    o.append(table_86_4("vi"))

    o.append(h4("Bộ điều hợp hiển thị", "Display Adapter"))
    o.append(p("Trong khi sự hỗ trợ đồ hoạ thường có sẵn như một tính năng tiêu chuẩn trên một "
               "hệ dựa trên PC, thì điều này không đúng với những hệ dựa trên bus khác như VME "
               "hay Multibus. Những hệ này được cung cấp một cổng nối tiếp có thể nối với một "
               "thiết bị đầu cuối để có được cuộc đối thoại chỉ văn bản với hệ điều hành đang "
               "chạy trên SBC. Trong những hoàn cảnh như vậy, việc chọn bộ điều hợp hiển thị sẽ "
               "do yêu cầu của người dùng quyết định, có tính đến sự hỗ trợ thiết bị mà các gói "
               "phần mềm sẽ dùng cung cấp. Nếu người dùng dự định viết phần mềm đồ hoạ riêng, "
               "thì điều thiết yếu là phải bảo đảm có sẵn một thư viện đồ hoạ từ nhà cung cấp, "
               "tối thiểu cung cấp các tiện ích vẽ đường, vẽ cung và tô màu khối."))

    o.append(h4("Bộ điều hợp IEEE-488", "IEEE-488 Adapter"))
    o.append(p("Thiết bị này cung cấp sự hỗ trợ cho việc truyền thông trên bus IEEE-488 hay "
               "GPIB (bus giao diện đa dụng). Bản thân bus gồm tám đường dữ liệu, năm đường "
               "quản lý giao diện và ba đường bắt tay. Việc truyền là song song, đồng bộ, với "
               "tốc độ lên tới 1,5 MB/s. Bus IEEE-488 và các ứng dụng của nó được bàn thêm "
               "trong phần về các thiết bị đo bên ngoài."))

    o.append(h4("Bộ điều hợp truyền thông nối tiếp", "Serial Communications Adapter"))
    o.append(p("Thiết bị này cung cấp sự hỗ trợ cho truyền thông nối tiếp theo các chuẩn "
               "RS-232, RS-422 hoặc RS-485. Nó được dùng để cung cấp một thiết bị đầu cuối dựa "
               "trên văn bản cho những hệ dựa trên Multibus hoặc VME, và để giao tiếp với những "
               "thiết bị đo “thông minh” như bộ điều khiển vị trí, đồng hồ vạn năng hay máy "
               "hiện sóng lưu trữ được trang bị những giao diện tương tự."))
    o.append(p("Bộ điều hợp nối tiếp chuyển dữ liệu song song sang và từ một dòng bit, trong "
               "đó mỗi byte dữ liệu (5, 7 hoặc 8 bit) được đóng khung bởi một bit khởi đầu, "
               "một bit chẵn lẻ tuỳ chọn và một hoặc nhiều bit dừng. Dòng bit có thể được gửi "
               "qua một mạch chỉ gồm hai dây với tốc độ lên tới 115.200 bit mỗi giây (thường "
               "được gọi là 115200 baud). Những tốc độ bit thông dụng là 300, 600, 1200, 2400, "
               "4800, 9600, 19200, 28800, 38400, 57600, 115200 baud. Cả bộ điều hợp phát lẫn "
               "bộ điều hợp thu đều phải được cấu hình, thường bằng phần mềm, cho cùng tốc độ "
               "baud, cùng số bit dữ liệu, số bit dừng và kiểu chẵn lẻ. Một hình thức điều "
               "khiển luồng nào đó để tránh việc bộ thu bị quá tải vì dữ liệu đến là điều thiết "
               "yếu. Việc này được thực hiện hoặc bằng những đường bắt tay riêng (ví dụ những "
               "đường được ký hiệu RTS và CTS trong chuẩn), hoặc bằng phần mềm, trong đó bộ "
               "thu gửi một byte điều khiển đặc biệt (XOFF) trở lại bộ phát để bảo nó ngừng "
               "gửi cho đến khi nhận được byte điều khiển thứ hai (XON) để cho phép gửi lại. "
               "Vì những lý do lịch sử, chuẩn RS-232 không định nghĩa một thủ tục bắt tay hai "
               "chiều, và các nhà sản xuất buộc phải tự triển khai những sơ đồ riêng của mình, "
               "vốn không phải lúc nào cũng tương thích với nhau."))
    o.append(p("Truyền thông nối tiếp giữa các thiết bị có thể là:"))
    o.append(ul([
        "<b>Song công hoàn toàn</b> (full duplex), trong đó mỗi thiết bị có thể phát hoặc thu "
        "dữ liệu ở bất kỳ thời điểm nào;",
        "<b>Bán song công</b> (half duplex), trong đó cả hai thiết bị đều có khả năng phát hoặc "
        "thu nhưng tại mỗi thời điểm chỉ một bên được phát;",
        "<b>Đơn công</b> (simplex), trong đó một thiết bị là bộ phát, một thiết bị là bộ thu, "
        "và dữ liệu chỉ có thể chảy theo một chiều.",
    ]))
    o.append(p("RS-232, do Hiệp hội Công nghiệp Điện tử (EIA) phát triển, là chuẩn lâu đời "
               "nhất, ban đầu được xây dựng vào đầu những năm 1960 để cho phép máy tính lớn "
               "giao tiếp với các thiết bị đầu cuối qua modem và đường điện thoại. Đây chính "
               "là nguồn gốc tên gọi của một số đường nối (ví dụ RI — chỉ thị chuông, DCD — "
               "phát hiện sóng mang), những cái tên không còn liên quan gì trong các ứng dụng "
               "đang xét ở đây. Một vấn đề liên quan là chuẩn này giả định những thiết bị được "
               "nối là thiết bị đầu cuối dữ liệu (DTE) ở một đầu liên kết và thiết bị truyền "
               "thông dữ liệu (DCE) ở đầu kia. Máy tính và thiết bị đầu cuối là DTE, còn modem "
               "là DCE. Bản sửa đổi được dùng phổ biến nhất của chuẩn, RS-232-C (cũng tồn tại "
               "các bản sửa đổi D và E), được ban hành năm 1969 và vẫn còn được dùng rộng rãi. "
               "Truyền thông nối tiếp được thực hiện bằng các mức điện áp vào khoảng ±12 V, "
               "trên những khoảng cách tới 15 m (50 ft) với tốc độ tới 20000 baud."))
    o.append(p("RS-422, cũng do EIA phát triển, là một cải tiến của chuẩn RS-232. Nó dùng "
               "những bộ phát và bộ thu vi sai, cho phép một bộ phát điều khiển tới mười bộ "
               "thu, dùng một cáp xoắn đôi cho mỗi mạch, với tốc độ bit tới 10 MBaud ở khoảng "
               "cách tới 12 m (40 ft) hoặc 100 kBaud ở khoảng cách tới 1200 m (4000 ft). Các "
               "đường RTS và CTS (được định nghĩa trong chuẩn) được dùng để điều khiển luồng, "
               "trong khi các đường RXD và TXD được dùng để phát và thu dữ liệu. Như vậy, cần "
               "một cáp hai đôi xoắn cho kết nối song công mà không bắt tay bằng phần cứng. Cần "
               "một cáp bốn đôi xoắn nếu dùng bắt tay bằng phần cứng."))
    o.append(p("RS-485 dựa trên RS-422 và cho phép nối tới 32 cặp bộ phát/bộ thu vào một bus "
               "dữ liệu chung (hai đôi xoắn). Rõ ràng là tại mỗi thời điểm chỉ có một thiết bị "
               "được phép phát. Mạch RTS được dùng để vô hiệu hoá những bộ phát khác đang nối "
               "vào bus khi một thiết bị cần phát dữ liệu. Việc bắt tay được thực hiện bằng "
               "phần mềm."))
    o.append(p("Các giao diện nối tiếp trên thiết bị đo thường được cấu hình như những thiết bị "
               "DTE. Ta đứng trước vấn đề nối một thiết bị DTE (giao diện nối tiếp của máy "
               "tính) với một thiết bị DTE khác (thiết bị đo), điều mà chuẩn RS-232 vốn không "
               "được thiết kế để làm. Hơn nữa, vì chuẩn không định nghĩa một thủ tục bắt tay "
               "hai chiều để điều khiển luồng dữ liệu, nên tồn tại nhiều sơ đồ bắt tay không "
               "tương thích với nhau. Một khảo sát toàn diện về những sơ đồ này được trình bày "
               "trong tài liệu tham khảo 7. Một giải pháp phổ biến cho vấn đề nối DTE với DTE "
               "là cái được gọi là <b>null modem</b>, vốn không gì khác hơn là một sợi cáp được "
               "đấu dây đặc biệt. Hình 86.5 cho thấy hai sơ đồ nối như vậy. Một sơ đồ đòi hỏi "
               "thủ tục bắt tay bằng phần mềm, sơ đồ kia thực hiện bắt tay bằng phần cứng hai "
               "chiều. Bạn đọc nên tham khảo tài liệu 7 để biết chi tiết về những sơ đồ khác và "
               "để có định nghĩa của các chữ viết tắt dùng để ghi nhãn các đường nối."))
    o.append(fig(5))
    o.append(p("Một số vấn đề thường gặp trong thực tế là:"))
    o.append(ol([
        "<b>Dữ liệu nhận được là rác.</b> Điều này hầu như luôn là do tốc độ baud, kiểu chẵn "
        "lẻ và số bit dừng không giống nhau ở hai đầu liên kết.",
        "<b>Dữ liệu ban đầu đúng, nhưng thiếu những đoạn ở giữa.</b> Đây có lẽ là vấn đề bắt "
        "tay. Thiết bị phát đang gửi dữ liệu nhanh hơn mức bộ thu có thể xử lý.",
        "<b>Hoàn toàn không truyền thông được.</b> Có lẽ là vấn đề bắt tay, trong đó bộ phát "
        "không cảm nhận được rằng bộ thu đã sẵn sàng.",
    ]))

    o.append(h4("Vào/ra số", "Digital Input and Output"))
    o.append(p("Những card này cung cấp các đường vào/ra, thường theo nhóm tám đường, có thể "
               "được dùng để cảm nhận hoặc tạo ra các tín hiệu số cho những thiết bị bên ngoài "
               "máy tính. Một nhóm tám đường vào được gọi là một cổng vào (8 bit), và một nhóm "
               "tám đường ra được gọi là một cổng ra (8 bit). Mức vào và mức ra thay đổi tuỳ "
               "card, và tốt nhất là tham khảo bảng dữ liệu thích hợp. Thông thường, điện áp "
               "trong khoảng 2,5 đến 5,0 V được coi là mức logic cao, trong khi điện áp trong "
               "khoảng 0,0 đến 0,5 V được coi là mức logic thấp. Những mức này đôi khi được gọi "
               "một cách lỏng lẻo là mức TTL (logic bóng bán dẫn–bóng bán dẫn). Lưu ý rằng các "
               "mức logic thực tế mà những họ TTL khác nhau sử dụng hơi khác so với những mức "
               "này. Các dải “cao” và “thấp” có thể hơi khác nhau giữa đường vào và đường ra. "
               "Các đường ra thường có khả năng cấp dòng và hút dòng hạn chế so với TTL, và do "
               "đó thường cần được đệm. Điều quan trọng là không được để những điện áp vượt quá "
               "giá trị định mức tối đa xuất hiện trên các đầu vào hoặc đầu ra (ví dụ việc cố "
               "đóng cắt một tải cảm tính có thể sinh ra một quá độ điện áp cao nguy hiểm tại "
               "một đầu ra); nếu không thì thiết bị có thể bị hỏng. Ở những nơi điều này có "
               "khả năng thành vấn đề, các đầu vào và đầu ra nên được đệm thích hợp hoặc thậm "
               "chí được cách ly quang, vốn cho khả năng bảo vệ tới vài kilôvôn. Các đầu ra "
               "cũng có thể điều khiển những rơ le được nối thích hợp. Những card vào/ra có sẵn "
               "các tiện ích này trên bo được bán rộng rãi."))
    o.append(p("Ở mức tối thiểu, có thể kỳ vọng một card vào/ra hỗ trợ một thanh ghi điều "
               "khiển, hai cổng vào/ra mỗi cổng có một thanh ghi dữ liệu đi kèm, và một số "
               "đường bắt tay. Các đường bắt tay đôi khi có thể được dùng để sinh ngắt trên SBC "
               "điều khiển. Một byte được ghi vào thanh ghi điều khiển được dùng để cấu hình "
               "các cổng vào/ra, nghĩa là để xác định xem chúng sẽ hoạt động như cổng vào hay "
               "cổng ra, cũng như để chọn chức năng, nếu có, của các đường bắt tay. Có thể "
               "không chọn được chiều của những cổng đã cách ly quang hoặc đã được đệm. Việc "
               "ghi một byte vào một cổng ra khiến một mẫu các mức điện áp cao và thấp xuất "
               "hiện trên các đường, phản ánh mẫu các số 0 và số 1 trong biểu diễn nhị phân của "
               "byte được ghi. Tương tự, khi một byte được đọc từ một cổng vào, con số đọc được "
               "được chỉ định bằng biểu diễn nhị phân thông qua mẫu các mức logic cao và thấp "
               "trên các đường vào. Ví dụ sau minh hoạ điều này."))
    o.append(p("Bộ giao diện ngoại vi lập trình được (PPI) Intel 8255 thường được dùng trong "
               "các card vào/ra số cho PC. Dữ liệu về thiết bị này có sẵn [8]. Chip 8255 cung "
               "cấp ba cổng, ký hiệu A, B và C, cùng một thanh ghi điều khiển. Cổng A và B có "
               "thể được chỉ định là cổng vào 8 bit hoặc cổng ra 8 bit. Cổng C có thể được coi "
               "là hai cổng bốn bit độc lập, có thể được chọn độc lập làm cổng vào hoặc cổng "
               "ra. Cổng C cũng có thể cung cấp các chức năng bắt tay. Có ba chế độ mà chip có "
               "thể hoạt động. Chế độ đơn giản nhất, chế độ 0, cung cấp vào/ra cơ bản không có "
               "bắt tay tự động, được dùng trong ví dụ của chúng ta. Lưu ý rằng 8 bit của một "
               "cổng vào/ra theo quy ước được ghi nhãn từ bit 0 đến bit 7. Đó là vì bit 0 có "
               "trọng số 2" + _sup("0") + ", bit 1 có trọng số 2" + _sup("1") + ", v.v. trong "
               "biểu diễn nhị phân của con số được đọc từ cổng hoặc ghi vào cổng."))
    o.append(p("Để cấu hình PPI hoạt động ở chế độ 0 với cổng A là cổng vào và cổng B là cổng "
               "ra, phải ghi mẫu bit 10011001 vào thanh ghi điều khiển. Con số này tương đương "
               "99 trong hệ thập lục phân hay 153 trong hệ thập phân. Giả sử bây giờ các công "
               "tắc nối với cổng A giữ bit 2 và bit 7 ở mức cao và các bit còn lại ở mức thấp. "
               "Mẫu nhị phân thu được sẽ là 10000100, tương đương 84 thập lục phân hay 132 thập "
               "phân. Khi cổng A được đọc, do đó sẽ thu được con số 132 (thập phân). Để giữ các "
               "đường nối với bit 2, 3 và 5 của cổng B ở mức cao trong khi để các đường còn lại "
               "ở mức thấp, ta thấy rằng mẫu nhị phân 00101100 phải xuất hiện tại cổng B. "
               "00101100 nhị phân tương đương 2C thập lục phân hay 44 thập phân. Do đó ta ghi "
               "con số thập phân 44 vào cổng B."))

    o.append(h4("Bộ đếm/định thời", "Counter/Timers"))
    o.append(p("Những thiết bị này thường cung cấp việc đếm sự kiện, đo xung và đo tần số có "
               "thể lập trình bằng phần mềm. Với vai trò thiết bị ra, chúng có thể tạo một xung "
               "đơn (một lần) khi đã đếm được một số xung vào lập trình được, và tạo ra những "
               "sóng vuông có tần số tuỳ ý và chu trình làm việc phức tạp. Tần số được tạo ra "
               "thường dựa trên một đồng hồ thạch anh trên bo để không phụ thuộc vào tốc độ "
               "đồng hồ nội của máy tính. Card bộ đếm/định thời thường hỗ trợ ít nhất ba bộ đếm "
               "16 bit độc lập."))
    o.append(p("Những ứng dụng thông dụng bao gồm:"))
    o.append(ol([
        "<b>Báo động.</b> Bộ đếm ở chế độ một lần và tạo một xung đơn khi hết thời gian. Xung "
        "này được nối để ngắt máy tính và báo cho người dùng biết ngay giữa tác vụ đang thực "
        "thi.",
        "<b>Bộ định thời canh gác (watchdog timer).</b> Nó được dùng để phát hiện sự cố, đặc "
        "biệt trong những hệ được thiết kế để hoạt động không cần người vận hành can thiệp. "
        "Nó tương tự Báo động mô tả ở trên, chỉ khác là ngắt được dùng để khởi động lại máy "
        "tính. Trong hoạt động bình thường điều này sẽ không bao giờ xảy ra vì mọi tác vụ phần "
        "mềm đang thực thi đều được thiết kế để cập nhật bộ đếm liên tục sao cho nó không bao "
        "giờ đạt tới số đếm cuối. Chỉ khi một sự cố phát triển, ví dụ một vụ “sập” phần mềm, "
        "bộ đếm mới hết thời gian và hệ thống được khởi động lại.",
        "<b>Tạo dạng sóng phức tạp</b>, ví dụ cho điều chế độ rộng xung. Ứng dụng này dùng hai "
        "bộ đếm mắc nối tiếp, một bộ (T1) tạo ra những xung đều ở tần số sóng mang để kích "
        "hoạt bộ kia (T2), ở chế độ một lần, nhằm tạo ra chu trình làm việc thay đổi như ở "
        "Hình 86.6.",
    ]))
    o.append(fig(6))

    o.append(h4("Đầu vào tương tự", "Analog Input"))
    o.append(p("Một card đầu vào tương tự dùng một bộ chuyển đổi tương tự–số (ADC), nhận một "
               "điện áp vào và cung cấp cho máy tính một số nguyên tỉ lệ với điện áp đó. Nhiều "
               "card hiện nay được sản xuất với các mạch điều kiện tín hiệu trên bo, cung cấp "
               "hệ số khuếch đại thay đổi được hoặc bằng công tắc hoặc dưới sự điều khiển của "
               "chương trình. Có sẵn những card với mạch điều kiện tín hiệu chuyên dụng cho các "
               "ứng dụng thông dụng như tuyến tính hoá cặp nhiệt điện hoặc giao tiếp với tenzô "
               "đo biến dạng và các cảm biến cầu khác. Cũng có sẵn việc điều kiện tín hiệu để "
               "bảo vệ những card dự kiến dùng trong môi trường điện khắc nghiệt. Những card rẻ "
               "hơn có thể chỉ cung cấp hệ số khuếch đại cố định và đòi hỏi phải cung cấp thêm "
               "những mạch điều kiện tín hiệu bên ngoài máy tính. Nhiều card còn có các đầu vào "
               "ghép kênh, trong đó một trong nhiều đầu vào có thể được chọn dưới sự điều khiển "
               "của chương trình để đưa tới ADC. Một số tham số quan trọng cần xem xét khi chọn "
               "một bảng đầu vào tương tự được nêu trong Bảng 86.5."))
    o.append(table_86_5("vi"))
    o.append(p("Ở tốc độ trên vài chục kilôhertz, việc thu nhận dữ liệu do ngắt điều khiển là "
               "điều thiết yếu để duy trì tốc độ. Những tốc độ dữ liệu cao hơn cần bộ nhớ trên "
               "bo để tránh làm giảm hiệu năng của SBC điều khiển. Trong trường hợp này, DMA có "
               "thể được dùng để chuyển dữ liệu vào bộ nhớ chính và tăng hiệu năng thêm nữa."))
    o.append(p("Một chức năng định thời thường được tích hợp để cho phép lấy mẫu theo những "
               "khoảng đều đặn, độc lập với việc SBC điều khiển đang làm gì. Một ngắt được sinh "
               "ra khi việc chuyển đổi hoàn tất, và một chương trình phục vụ ngắt sau đó được "
               "kích hoạt để đọc kết quả chuyển đổi vào bộ nhớ. Việc viết và cài đặt các chương "
               "trình phục vụ ngắt không phải là một việc tầm thường và tốt nhất nên để cho "
               "những người hiểu biết sâu sắc về hệ điều hành đang chạy trên SBC đảm nhận. May "
               "thay, hầu hết các nhà sản xuất đều cung cấp phần mềm (trình điều khiển thiết bị) "
               "cho mục đích này. Những bảng đầu vào tương tự đơn giản hơn có thể được điều "
               "khiển bằng cách ghi trực tiếp các giá trị vào những thanh ghi trên chúng theo "
               "cách tương tự ví dụ đã nêu cho các card vào/ra số. Các nhà sản xuất hiện nay "
               "thường cung cấp một thư viện phần mềm có thể được gọi từ nhiều ngôn ngữ bậc cao "
               "khác nhau, cho phép người dùng truy cập card theo cách trực quan hơn. Điều này "
               "được bàn thêm trong phần về phần mềm."))

    o.append(h4("Đầu ra tương tự", "Analog Output"))
    o.append(p("Card đầu ra tương tự có sẵn dưới dạng thiết bị 8, 10 hoặc 12 bit. Thường thì "
               "một card sẽ hỗ trợ nhiều kênh đầu ra tương tự, với khả năng trì hoãn việc cập "
               "nhật các kênh để tất cả có thể được cập nhật đồng thời. Điện áp ra có thể đơn "
               "cực hoặc lưỡng cực, và cũng có sẵn các đầu ra dòng (4 đến 20 mA). Cần điều kiện "
               "tín hiệu (đệm) để điều khiển những tải tiêu thụ dòng lớn hơn vài miliampe. Cần "
               "đặc biệt chú ý với những tải cảm tính, ví dụ động cơ, để tránh làm hỏng thiết "
               "bị bởi các quá độ điện áp. Có sẵn những mô-đun điều khiển vị trí được thiết kế "
               "riêng, tích hợp các đầu vào/ra tương tự và số đã được đệm thích hợp, cho mục "
               "đích này."))

    o.append(h3("Thiết bị ngoại vi ngoài", "External Peripherals"))
    o.append(p("Đây thường là những thiết bị “thông minh”, có thể hoạt động qua các điều khiển "
               "trên mặt trước mà không cần một máy tính khác, nhưng ngoài ra còn có khả năng "
               "được điều khiển bởi máy tính. Nhiều thiết bị đo trong phòng thí nghiệm thông "
               "dụng có sẵn những tiện ích như vậy, gồm bộ nguồn, máy tạo tín hiệu, máy hiện "
               "sóng lưu trữ, vôn kế, máy quang phổ và bộ điều khiển vị trí. Một máy tính có "
               "thể phối hợp hoạt động của nhiều thiết bị như vậy để thu thập, rồi thao tác và "
               "hiển thị dữ liệu theo cách làm tăng sức mạnh của hệ đo lường. Một ví dụ gần như "
               "tầm thường là việc dùng máy tính điều khiển một máy tạo tín hiệu và một vôn kế "
               "để tự động tạo ra đáp ứng tần số của một bộ khuếch đại. Một hệ như vậy có vai "
               "trò rõ ràng trong các giàn thử nghiệm tự động."))
    o.append(p("Hai phương pháp thông dụng được dùng để điều khiển những thiết bị như vậy: một "
               "liên kết nối tiếp, hoặc bus IEEE-488. Trong cả hai trường hợp, các thiết bị "
               "được điều khiển bằng cách gửi những thông điệp gồm chuỗi ký tự ASCII. Thông "
               "thường các chuỗi được chọn sao cho có ý nghĩa hiển nhiên, như trong ví dụ dưới "
               "đây, nhưng không phải lúc nào cũng vậy — đặc biệt với những thiết bị cũ, nơi "
               "tính thân thiện với người dùng thường bị hy sinh do bộ nhớ và năng lực xử lý "
               "hạn chế! Chuỗi thông điệp"))
    o.append(_code(['“FREQ10kHz”', '“SINE”', '“1.0VOLTRMS”']))
    o.append(p("có thể được dùng để đặt một máy tạo tín hiệu tạo ra tín hiệu hình sin 10 kHz ở "
               "1 V hiệu dụng. Có rất ít sự chuẩn hoá về dạng thông điệp thiết bị, mặc dù tiêu "
               "chuẩn IEEE 488.2 có phần nào đi theo hướng này. Các phản hồi từ thiết bị đo "
               "cũng được gửi theo cách tương tự, tức là dưới dạng ký tự ASCII, nên một vôn kế "
               "có thể phản hồi một lệnh yêu cầu đo bằng dữ liệu"))
    o.append(_code(['“AC2.01mV”']))
    o.append(p("để cho biết rằng nó đang ở dải điện áp xoay chiều và đo được 2,1 mV. Một lần "
               "nữa, có rất ít sự chuẩn hoá về khuôn dạng phản hồi. Những khối dữ liệu lớn có "
               "thể được gửi ở dạng nhị phân khi có thể (liên kết nối tiếp 8 bit hoặc bus "
               "IEEE-488) để giảm thiểu lượng dữ liệu phải truyền."))

    o.append(h4("Thiết bị nối tiếp", "Serial Devices"))
    o.append(p("Việc điều khiển thiết bị nối tiếp được thực hiện bằng những liên kết tuân theo "
               "một trong các chuẩn nối tiếp (RS-232, RS-422 hoặc RS-485) đã mô tả ở nơi khác "
               "trong chương này. Đây là một phương pháp điều khiển tương đối đơn giản và có ưu "
               "điểm là phần lớn việc thử nghiệm và gỡ lỗi sơ bộ một hệ thống có thể được thực "
               "hiện bằng một thiết bị đầu cuối hoặc một chương trình giả lập thiết bị đầu cuối "
               "như KERMIT thuộc phạm vi công cộng, lấy từ Kermit Distribution (Columbia "
               "University Academic Information Systems, 612 West 115th Street, New York, NY "
               "10025, Phone: 212-854-3703). Việc viết phần mềm riêng truy cập giao diện nối "
               "tiếp của máy tính điều khiển là tương đối dễ dưới những hệ điều hành thông dụng "
               "gồm DOS, Windows, Windows 95, UNIX và OS-9, dùng những ngôn ngữ như C, Pascal "
               "hoặc BASIC. Ngày càng phổ biến — đặc biệt với các ứng dụng DOS và Windows — "
               "việc các nhà sản xuất cung cấp hỗ trợ phần mềm cho thiết bị của họ."))
    o.append(p("Những nhược điểm của truyền nối tiếp là tốc độ tương đối chậm khi truyền một "
               "lượng lớn dữ liệu, sự thiếu chuẩn hoá trong thông điệp thiết bị, và các tiện "
               "ích điều khiển hạn chế. Những ưu điểm là sự dễ dàng thử nghiệm, sự đơn giản của "
               "phần mềm điều khiển, sự tương đối đơn giản của sơ đồ nối dây, và — đối với các "
               "hệ đo lường từ xa — việc dùng modem cho phép dữ liệu được truyền qua những "
               "khoảng cách lớn bằng đường điện thoại tiêu chuẩn hoặc thậm chí bằng một liên "
               "kết vô tuyến."))

    o.append(h4("Thiết bị IEEE 488", "IEEE 488 Devices"))
    o.append(p("Tiêu chuẩn IEEE 488 được xây dựng vào những năm 1970 và nhanh chóng trở thành "
               "một chuẩn công nghiệp cho việc nối và điều khiển thiết bị thử nghiệm. Tiêu "
               "chuẩn này được sửa đổi đôi chút vào năm 1987 (tiêu chuẩn IEEE 488.1) để cho "
               "phép những cải tiến đáng kể của tiêu chuẩn IEEE 488.2, vốn được giới thiệu "
               "cùng lúc [9,10]. Tiêu chuẩn IEEE 488 nguyên bản quy định những đặc tính điện "
               "của bus, những đặc tính cơ học của các đầu nối, và một tập thông điệp được "
               "truyền giữa các giao diện. Nó không cố gắng cung cấp bất kỳ cú pháp hay cấu "
               "trúc nào cho việc truyền những thông điệp này, không chỉ định những lệnh thông "
               "dụng, cũng không thiết lập một chuẩn cho các thông điệp dành riêng cho thiết "
               "bị. Những vấn đề này được đề cập trong tiêu chuẩn IEEE 488.2."))
    o.append(p("Bản thân bus hỗ trợ những lần truyền dữ liệu song song đồng bộ dùng ba nhóm "
               "đường:"))
    o.append(ul([
        "Một bus dữ liệu 8 bit hai chiều,",
        "Năm đường quản lý giao diện, và",
        "Ba đường bắt tay,",
    ]))
    o.append(p("trên những khoảng cách tới 20 m và với tốc độ truyền dữ liệu tới 1 MB/s."))
    o.append(p("Các thiết bị trên bus được phân loại là bộ phát (talker), bộ nhận (listener) "
               "hoặc bộ điều khiển (controller). Nói chung, hệ máy tính là bộ điều khiển bus, "
               "và cũng có thể phát (gửi dữ liệu) hoặc nhận (thu dữ liệu). Hầu hết thiết bị vừa "
               "là bộ phát vừa là bộ nhận: ví dụ, một vôn kế số sẽ là bộ nhận khi tiếp nhận các "
               "chỉ thị đặt dải điện áp trước khi thực hiện phép đo, nhưng sẽ là bộ phát khi "
               "gửi trả kết quả phép đo cho bộ điều khiển, vốn đang đóng vai trò bộ nhận. Mỗi "
               "thiết bị trên bus phải được gán một địa chỉ duy nhất, là một số trong khoảng từ "
               "0 đến 30. Việc này có thể được thực hiện từ mặt trước của thiết bị, hoặc — kém "
               "thuận tiện hơn — bằng cách đặt các công tắc ở nơi khác trên thiết bị."))
    o.append(p("Viết phần mềm để điều khiển một card IEEE-488 là một quá trình khó, tốn thời "
               "gian và dễ sai sót. Những người mua giao diện IEEE-488 mới được khuyến cáo mạnh "
               "mẽ nên lấy một trình điều khiển thiết bị từ nhà sản xuất. Những trình điều khiển "
               "thiết bị như vậy nay đã sẵn có và tích hợp card vào hệ thống tập tin của hệ điều "
               "hành đang chạy trên máy tính điều khiển. Điều này cho phép truy cập giao diện "
               "một cách tự nhiên từ những ngôn ngữ bậc cao chạy trên bộ điều khiển."))

    # ---------------------------------------------------------------- 86.6
    o.append(h2("86.6 Phần mềm cho hệ đo lường", "Software for Instrumentation Systems"))
    o.append(p("Khó khăn trong việc viết phần mềm cho các hệ đo lường phụ thuộc phần lớn vào sự "
               "hỗ trợ sẵn có từ các nhà sản xuất hệ thống con, vào hệ điều hành (nếu có), và "
               "vào những công cụ phát triển sẵn có. Ở một thái cực, ta có thể đang làm việc "
               "trong một môi trường thiết bị đo ảo, như môi trường do LabVIEW của National "
               "Instrument cung cấp, nơi việc phát triển phần mềm hoàn toàn bằng đồ hoạ và — ít "
               "nhất với những dự án nhỏ — được những người dùng có ít hoặc không có kinh "
               "nghiệm trước đó thực hiện một cách dễ dàng. Ở thái cực kia, ta đứng trước vấn "
               "đề phát triển phần mềm — ít nhất là do ngắt điều khiển và có lẽ là đa nhiệm — "
               "cho một SBC đích không có hệ điều hành thường trú; việc này đòi hỏi chuyên môn "
               "đáng kể về thiết kế và phát triển phần mềm, cùng với sự sẵn có của những công "
               "cụ phát triển như trình biên dịch chéo và trình gỡ lỗi mức mã nguồn."))

    o.append(h3("Thiết bị đo ảo", "Virtual Instruments"))
    o.append(p("Hình 86.7 trình bày một mô hình phân lớp của phần mềm cho một hệ đo lường tổng "
               "quát. Lớp ứng dụng đảm nhận việc thu thập, phân tích và trình bày dữ liệu. Các "
               "<b>trình điều khiển thiết bị đo</b> cung cấp một cơ chế để giao tiếp với các "
               "thiết bị đo theo một cách chuẩn mực mà không đòi hỏi người dùng phải biết về "
               "những chuỗi dữ liệu thường rất khó hiểu cần được gửi đi. Ví dụ, mọi đồng hồ vạn "
               "năng số đều cần tiện ích chọn một dải điện áp vào cụ thể. Cách mã hoá dải, độ "
               "phân giải, v.v. phải được gửi tới đồng hồ vạn năng để đạt được điều đó sẽ khác "
               "nhau tuỳ từng thiết bị đo; tuy vậy, trình điều khiển thiết bị đo cho phép người "
               "viết phần mềm đang lập trình ở lớp ứng dụng gọi một thủ tục như"))
    o.append(_code(["SetVoltageRange(VoltageValue)"]))
    o.append(p("và lời gọi thủ tục này là như nhau với mọi đồng hồ vạn năng. Mặc dù một số nhà "
               "sản xuất dùng thuật ngữ này hơi khác, trình điều khiển thiết bị đo thực chất "
               "chính là thiết bị đo ảo. Viết trình điều khiển thiết bị đo là một công việc tốn "
               "thời gian nhưng không quá khó. Trình điều khiển thiết bị đo cho những gói phần "
               "mềm thiết kế đo lường độc quyền có sẵn từ các nhà sản xuất thiết bị đo. Các "
               "<b>trình điều khiển thiết bị</b> tích hợp giao diện điều khiển (ví dụ IEEE-488, "
               "RS-232 hoặc card nội bộ) vào hệ điều hành của máy tính. Viết một trình điều "
               "khiển thiết bị đòi hỏi hiểu biết chi tiết về phần cứng thiết bị và về hệ điều "
               "hành của máy tính. Đây là một việc khó, và nên mua những giao diện mới kèm theo "
               "một trình điều khiển thiết bị phù hợp với hệ điều hành bất cứ khi nào có thể."))
    o.append(fig(7))
    o.append(p("Hiện nay có sẵn một số môi trường phát triển dựa trên khái niệm thiết bị đo ảo. "
               "Những môi trường này giải phóng người dùng khỏi vấn đề phải viết phần mềm thông "
               "thường để điều khiển thiết bị đo và xử lý dữ liệu sinh ra. Đối với người phát "
               "triển phần mềm, các thiết bị đo hiện ra như những “mặt trước” được vẽ trên màn "
               "hình máy tính, đầy đủ với những nút bấm, núm xoay và màn hiển thị quen thuộc. "
               "Luồng dữ liệu được xử lý bằng cách nối các thiết bị đo trong một sơ đồ khối "
               "bằng chuột, trong một môi trường giống như một gói phần mềm vẽ thông thường. "
               "Người phát triển phần mềm chỉ làm việc trong lớp ứng dụng."))
    o.append(p("Trong khi môi trường đồ hoạ cho phép phát triển nhanh những hệ đơn giản, những "
               "lập trình viên có kinh nghiệm có thể thấy nó hạn chế. Có sẵn những hệ phát "
               "triển phần mềm cho phép lập trình viên truy cập những thư viện chứa trình điều "
               "khiển thiết bị đo, các thường trình phân tích dữ liệu, các hàm đồ hoạ và những "
               "tiện ích trực quan hoá dữ liệu trong những ngôn ngữ bậc cao thông dụng như C, "
               "Pascal, BASIC và FORTRAN. Bảng 86.2 liệt kê những gói phần mềm tiêu biểu."))

    o.append(h3("Làm việc trực tiếp với thiết bị ngoại vi",
                "Working Directly with Peripherals"))
    o.append(p("Đôi khi có thể xảy ra trường hợp chi phí hỗ trợ phần mềm cho một môi trường phát "
               "triển thiết bị đo ảo là không hợp lý đối với một ứng dụng nhỏ. Khi đó phải viết "
               "phần mềm để giao tiếp trực tiếp với thiết bị ngoại vi. Phần trước về vào/ra số "
               "đã giải thích về nguyên tắc những gì cần thiết để lập trình một chip giao diện "
               "đơn giản. Bây giờ ta tiếp tục ví dụ đó và cho thấy có thể làm được điều này như "
               "thế nào bằng ngôn ngữ C."))
    o.append(p("Phương pháp truy cập các thanh ghi của card ngoại vi phụ thuộc vào bộ vi xử lý "
               "được dùng và thậm chí có thể không phải là một tính năng chuẩn của ngôn ngữ "
               "đang được sử dụng. Ở những nơi thiết bị ngoại vi nằm trong cùng không gian địa "
               "chỉ với bộ nhớ máy tính, như trong dòng Motorola 680XX, có thể dùng con trỏ để "
               "đọc và ghi các giá trị trong thanh ghi. Dòng bộ xử lý Intel 80×86 thường đặt "
               "thiết bị ngoại vi vào một không gian địa chỉ riêng mà con trỏ không truy cập "
               "được. Trong trường hợp này cần một phần mở rộng của ngôn ngữ. Turbo C và C++ "
               "của Borland cung cấp các hàm để đọc và ghi những thiết bị ánh xạ vào/ra:"))
    o.append(_code(["unsigned char inportb(int portid)",
                    "void outportb(int portid, unsigned char value)"]))
    o.append(p("Những hàm này được dùng trong đoạn mã thực hiện phần mềm cho ví dụ trước đó. Ta "
               "giả định rằng PPI 8255 có địa chỉ gốc 0x1b0 và rằng chương trình sao chép giá "
               "trị đọc được từ cổng vào (cổng A) trực tiếp sang cổng ra (cổng B), cho đến khi "
               "bit 0 của đầu vào trở thành 0."))
    o.append(_code([
        "/* define the addresses of the registers for the PPI */",
        "#define BASE 0x1b0",
        "#define PABASE",
        "#define PBBASE+1",
        "#define CONTROLBASE+3",
        "",
        "unsigned char xin;/* declare an 8-bit variable */",
        "outportb(CONTROL, 153)/* set port A as input, port B as output */",
        "do",
        "{",
        "        xin = inportb(PA);/* read the input */",
        "        outportb(PB,xin);/* write the output */",
        "}",
        "while(xin &amp; 1);    /* loop if bit 0 is still 1 */",
    ]))
    o.append(p("Đoạn mã này cũng minh hoạ rằng các ngôn ngữ bậc cao nói chung chỉ hỗ trợ việc "
               "vào và ra theo byte. Phải dùng kỹ thuật mặt nạ bit để truy cập từng bit riêng "
               "lẻ."))

    o.append(h3("Lựa chọn hệ điều hành", "The Choice of Operating System"))
    o.append(p("Sự hỗ trợ phát triển phần mềm đã bàn tới nay thường có sẵn dưới DOS, Windows "
               "3.1, Windows 95, Windows NT và UNIX. Khi một hệ là đa nhiệm, nó phải đáp ứng "
               "những ràng buộc thời gian thực khắt khe; tuy vậy, không hệ điều hành nào trong "
               "số này đặc biệt thích hợp. DOS không hỗ trợ đa nhiệm, còn những hệ kia không "
               "được tối ưu cho các hệ thời gian thực vốn cần chuyển ngữ cảnh nhanh và đáp ứng "
               "ngắt nhanh. Yêu cầu nền tảng nhất của các ứng dụng thời gian thực là khả năng "
               "của hệ thống đáp ứng những sự kiện bên ngoài với những độ trễ rất ngắn, có giới "
               "hạn và dự đoán được. Bảng 86.6 liệt kê một số hệ điều hành và nhân thời gian "
               "thực quan trọng."))
    o.append(table_86_6("vi"))
    o.append(p("Các hệ điều hành thời gian thực có xu hướng không có được sự hỗ trợ phát triển "
               "phần mềm chín muồi và mạnh mẽ như những hệ điều hành thông thường. Không thể "
               "đơn giản là phát triển phần mềm trên một hệ điều hành quen thuộc rồi chuyển "
               "những chương trình đang chạy sang hệ đích. Phần lớn việc gỡ lỗi, thử nghiệm và "
               "tích hợp hệ thống sẽ phải được thực hiện ngay trên hệ đích để truy cập phần "
               "cứng. Một giải pháp phổ biến là một hệ phát triển trong đó một trạm làm việc "
               "thông thường được nối với hệ đích. Phần mềm được phát triển trên trạm làm việc "
               "bằng những công cụ quen thuộc, ví dụ một trình soạn thảo trên Windows, sự hỗ "
               "trợ quản lý phiên bản và một hệ thống tập tin mạnh. Bất cứ lúc nào, mã cũng có "
               "thể được biên dịch chéo (nghĩa là biên dịch cho bộ xử lý trên hệ đích) và nạp "
               "xuống hệ đích. Trạm làm việc sau đó có thể giám sát việc thực thi phần mềm đang "
               "chạy trên bộ xử lý đích. Có sẵn những tính năng cho phép người dùng chạy từng "
               "bước qua mã nguồn, hiển thị trong một cửa sổ của trạm làm việc, trong khi xem "
               "trạng thái của những biến then chốt trong một cửa sổ khác. Cũng có thể đặt các "
               "điểm dừng và cho các tiến trình chạy cho đến khi gặp một điểm dừng. Các nhà sản "
               "xuất hệ điều hành thời gian thực thường có khả năng cung cấp cho sản phẩm của "
               "họ sự hỗ trợ phát triển kiểu này trên nhiều loại trạm làm việc khác nhau."))

    # ---------------------------------------------------------------- refs
    o.append(h2("Tài liệu tham khảo", "References"))
    o.append(refs([
        "Micrology pbt, Inc., <i>The VMEbus Specification Manual: Revision C1</i>, PRINTEX, "
        "1985.",
        "S. Heath, <i>VMEbus: A Practical Companion</i>, Boston, MA: Butterworth Heinemann, "
        "1993.",
        "J. Di Giacomo, Ed., <i>Digital Bus Handbook</i>, New York: McGraw-Hill, 1990.",
        "T. Shanley and D. Anderson, <i>ISA System Architecture</i>, 3rd ed., Reading, MA: "
        "Addison-Wesley, 1995.",
        "T. Shanley and D. Anderson, <i>EISA System Architecture</i>, 2nd ed., Reading, MA: "
        "Addison-Wesley, 1995.",
        "T. Shanley and D. Anderson, <i>PCMCIA System Architecture</i>, 2nd ed., Reading, MA: "
        "Addison-Wesley, 1995.",
        "M. D. Seyer, <i>RS232 Made Easy</i>, Englewood Cliffs, NJ: Prentice-Hall, 1984.",
        "Intel Corporation, <i>Intel Microsystems Component Handbook</i>, Vol. 2.",
        "IEEE Std 488.1-1987, <i>IEEE Standard Digital Interface for Programmable "
        "Instrumentation</i>.",
        "IEEE Std 488.2-1987, <i>IEEE Standard Codes, Formats, Protocols and Common Commands</i>.",
    ]))

    o.append(h2("Thuật ngữ", "Glossary"))
    o.append(_glossary(_GLOSS_VI))
    o.append(h2("Đọc thêm", "Further Reading"))
    o.append(refs(_FURTHER_VI))
    return "".join(o)


# ================================================================ BODY — EN
def body_en():
    o = []
    o.append(_transnote("en"))

    o.append(h2("86.1 Introduction"))
    o.append(p("Computers are an essential feature of most instrumentation systems because of "
               "their ability to supervise the collection of data and allow information to be "
               "processed, stored, and displayed. Many modern instruments are capable of "
               "providing a remote user with access to measurement information via standard "
               "computer networks."))

    o.append(h2("86.2 Computer-Based Instrumentation Systems"))
    o.append(p("The main features of a computer-based instrumentation system are shown in "
               "Figure 86.1. The actual implementation of such systems will depend on the "
               "application. Many commercially produced instruments such as spectrophotometers "
               "or digital storage oscilloscopes are themselves integrated computer-based "
               "measurement systems. These “standalone” instruments may be fitted with "
               "interfaces such as IEEE-488 or RS-232 to allow them to be controlled from "
               "personal computers (PCs) and also to support the transfer of data to the PC for "
               "further processing and display. Alternatively, the instrumentation system may "
               "be based around a PC/workstation or an industrial bus system such as a VME or "
               "Multibus, allowing the user the ability to customize the computer to suit the "
               "application by selecting an appropriate set of add-on cards. Recently, the "
               "introduction of laptop and notebook PCs fitted with PCMCIA interfaces with "
               "input/output capability has provided opportunities for the development of "
               "highly portable instrumentation systems."))
    o.append(fig(1, "en"))

    o.append(h3("The Single-Board Computer"))
    o.append(p("The simplest form of a computer is based around the single-board computer (SBC) "
               "which contains a microprocessor, memory, and interfaces for communicating with "
               "other electronic systems. The earliest form of personal computers simply "
               "comprised an SBC together with a keyboard, display, disk drives, and a power "
               "supply unit. Today, the SBC still offers a solution for the addition of limited "
               "intelligence to instrumentation systems as well as forming an element of most "
               "computer systems, e.g., as the motherboard of a PC."))
    o.append(p("An overview of a simple SBC is shown in Figure 86.2. The microprocessor, which "
               "contains the central processor unit, is responsible for executing the computer "
               "program and for controlling the flow of data around the SBC. The random access "
               "memory (RAM) acts as a temporary (i.e., volatile) storage area for both program "
               "code and data. On the motherboard of a PC the read only memory (ROM) is largely "
               "used for storing the low-level code used to access the input/output hardware, "
               "e.g., the BIOS (basic input output system). The operating system and "
               "applications software are loaded into RAM from the disk unit. In small, "
               "dedicated systems such as an oscilloscope the ROM may be used to store the "
               "program code to avoid the need for a disk drive. For small production runs or "
               "development work erasable programmable ROM (EPROM) is used as an alternative to "
               "ROM, allowing the code to be upgraded without the high cost of commissioning a "
               "new ROM chip from the manufacturers."))
    o.append(fig(2, "en"))
    o.append(p("Data are transferred around the SBC on its data bus, which will be typically 8, "
               "16, or 32 bits wide (corresponding to the number of bits that can be transmitted "
               "at the same time). SBCs with 8-bit data buses are less complex and consequently "
               "of lower cost than 32-bit systems and may well be the optimum solution for those "
               "process control applications which require minimal processing of 8-bit data, "
               "e.g., from temperature and position sensors. However the 32-bit bus width of "
               "most modern PCs and workstations is essential to ensure the fast operation of "
               "Windows-based applications software."))
    o.append(p("The address bus is used to identify the destination of the data on the data bus. "
               "Data transfer is usually between the microprocessor and the memory or "
               "interfaces. However, some SBCs support DMA (direct memory access) which allows "
               "data to be transferred directly between interfaces and memory without the need "
               "the information to pass through the processor. DMA is inherently faster than "
               "program-driven data transfer and is used for moving large blocks of data, e.g., "
               "loading programs from disk or the transfer of digitized video images."))
    o.append(p("SBCs are fitted with interfaces to allow them to communicate with other "
               "circuits. Interfaces carry out two main functions. First, they serve to ensure "
               "that the signals on the internal buses of the SBC are not affected by the "
               "connection of peripheral devices. Second, they ensure that signals can pass into "
               "and out of the computer and that appropriate voltage levels and current loading "
               "conditions are met. A well-designed interface should also provide adequate "
               "electrical protection for the SBC from transients introduced via the external "
               "connection. Parallel interfaces allow data to be transferred, usually 8 or 16 "
               "bits at a time, and contain registers that act as temporary data stores. Serial "
               "interfaces must carry out the conversion of data from the parallel format of the "
               "internal SBC data bus to and from the serial format used by the interface "
               "standard (e.g., RS-232 or RS-422). Some SBCs may contain additional interfaces "
               "to support communication with a VDU, local area network (LAN), or a disk drive. "
               "Interfaces can range in complexity from a single parallel interface chip to a "
               "LAN controller which may require a significant fraction of the SBC board area."))

    o.append(h3("Computer Bus Architectures"))
    o.append(p("All but the simplest computer systems contain several circuit board cards which "
               "plug into a printed circuit board backplane. The cards will include at least one "
               "SBC and a number of “add-on” cards providing functions such as interfaces to "
               "peripherals (e.g., a LAN, graphics display, disk unit) or additional memory. The "
               "actual structure of bus architectures is quite variable but the simple model "
               "shown in Figure 86.3 contains the essential features. A group of tracks will "
               "carry the data and address information with a second group of tracks being used "
               "to control the flow of data and to ensure its reliable transfer. Other tracks are "
               "reserved for the signals which provide arbitration between SBC cards to ensure "
               "that only one such card has control of the bus at any given moment. There will "
               "also be tracks which provide utility functions such as clock signals and the "
               "transmission of event or interrupt signals."))
    o.append(fig(3, "en"))
    o.append(p("The main advantage of bus-based systems is that they help one build a complex "
               "computerized system using standard cards. By conforming to agreed standard buses "
               "(see Table 86.1 for typical examples), the system integrator can minimize "
               "problems of incompatibility and keep system costs to a minimum. The complexity "
               "of many bus systems is such that a significant fraction of the area of each card "
               "is dedicated to providing the logic required to interface to the bus, adding "
               "appreciably to the cost. In addition, data transfer between cards, even using "
               "DMA, is relatively slow compared with transfers between chips on the same SBC. "
               "There is, therefore, a trade-off between integrating functions on a single SBC "
               "and a lack of flexibility in customising the system. An alternative to bus-based "
               "systems is to utilize processors such as transputers which are designed to be "
               "connected together directly into multiprocessor structures."))
    o.append(table_86_1("en"))
    o.append(p("Most modern computerized systems adopt some form of distributed intelligence "
               "strategy in order to free the central processor unit to run the main "
               "application. Graphics controller cards generally employ a dedicated graphics "
               "processor able to handle the creation of the basic features such as line drawing "
               "or scaling the size of objects. LAN controller cards require intelligence to "
               "handle the network protocols and buffer the data flow to and from the network. "
               "Disk controller cards relieve the central processor of the need to handle the "
               "processes of reading and writing to the disk."))
    o.append(p("The use of a bus system with more than one SBC allows the designer to dedicate an "
               "SBC to the process of data acquisition and temporary data storage in order to "
               "ensure that the main SBC can concentrate on data processing and communication "
               "with the user. Such a strategy enables the data acquisition SBC to maintain a "
               "real-time response to making measurements while allowing the user access to "
               "processed data. In most systems one of the SBCs acts as a system controller, "
               "which has ultimate control over the use of the bus and will normally contain the "
               "bus arbitration hardware. Only one SBC at a time can obtain the authority of the "
               "controller to act as a bus master and initiate data communication. The other "
               "cards will be configured as slaves allowing them to respond to requests for "
               "information from the master. In some systems, e.g., Multibus II, bus arbitration "
               "is distributed throughout the intelligent cards."))

    o.append(h3("Industrial Computers"))
    o.append(p("Many instrumentation systems utilize standard PCs or workstations either fitted "
               "with add-on cards or linked to intelligent instruments via standard protocols "
               "such as IEEE-488 or RS-232. In many industrial environments there is a need to "
               "provide protection against hazards such as dust, damage by impact or vibration, "
               "and unauthorized access. The systems may have to fit more stringent "
               "electromagnetic compatibility (EMC) requirements. Industrial or ruggedized "
               "versions of desktop computers are available to meet this market. Cardframes "
               "designed to accommodate the standard industrial bus systems such as VME and "
               "Multibus can be readily customized to meet the demands of the industrial "
               "environment and ruggedized versions of PCs are also available. In designing "
               "industrial computers, care must be paid to the specification of adequate power "
               "supplies, both to provide sufficient current for the add-on cards and also to "
               "provide protection against fluctuations in the mains supply. It may also be "
               "necessary in safety-critical applications to use an uninterruptable power supply "
               "that will guarantee the operation of the system during short failures in the "
               "mains supply."))

    o.append(h3("Software"))
    o.append(p("All but the simplest computer systems require an operating system to support the "
               "operation of applications software. The operating system will allocate areas of "
               "memory for use by the applications programs and provide mechanisms to access "
               "system resources such as printers or displays. Some operating systems, such as "
               "MS DOS, are single-tasking systems, meaning that they will only support the "
               "operation of one program or task at a time. Instrumentation systems which "
               "simultaneously take measurements, process data, and allow the user to access "
               "information generally require a multitasking operating system, such as OS-9, "
               "UNIX, or Windows 95. In such instrumentation systems the applications software "
               "may well comprise a single program, but it may generate software processes or "
               "tasks each with their own local data and code. The multitasking operating system "
               "will allow the actual execution of these tasks to be scheduled and also provide "
               "mechanisms for communication of information between tasks and for the "
               "synchronization of tasks."))
    o.append(p("Instrumentation systems are real-time environments, i.e., their operation "
               "requires that tasks be carried out within specified time intervals; for example, "
               "the capture of data must occur at specified moments. Operating systems adopt a "
               "range of strategies for determining the scheduling of software tasks. "
               "Round-robin scheduling, for example, provides each task with execution time on a "
               "rota basis, with the amount of time being determined by the priority of the "
               "task. Operating systems which support preemptive scheduling allow high-priority "
               "tasks to become active if a specified event such as trigger signal occurs. The "
               "speed at which an operating system can switch from one task to another (i.e., "
               "context switch) is a important metric for real-time systems."))
    o.append(p("The extent to which an operating system can respond to a large number of events "
               "is extremely limited, as low-priority tasks will have a poor response time. If "
               "an instrumentation system needs to make a large number of measurements and also "
               "support other activities, such as information display, the solution is generally "
               "to use a distributed system with dedicated SBCs operating as microcontrollers to "
               "capture the data. These microcontrollers will not usually require an operating "
               "system and will each operate a single program which will be either downloaded "
               "from the master SBC or located in ROM."))
    o.append(p("Commercial packages (for examples, see Table 86.2) are readily available to "
               "support PC/workstation based instrumentation systems. A typical system will "
               "provide a Windows-type environment to control measurements and store, process, "
               "and display data and increasingly make use of the virtual-instrument concept "
               "which allows the user to configure instrumentation systems from an on-screen "
               "menu. Most packages will allow stand-alone instruments to be controlled using "
               "interface cards supporting standards such as IEEE-488 or RS-232. Some packages "
               "also support the use of add-on cards for analog-to-digital conversion or a range "
               "of control functions such as channel switching and waveform generation; however, "
               "their main restriction is the limited range of hardware configurations supported "
               "by the software supplier."))
    o.append(table_86_2("en"))
    o.append(p("Each stand-alone instrument and add-on card requires a piece of code called a "
               "device driver so that the operating system can access the hardware resources of "
               "the card and instrument. Therefore, the development of device drivers requires an "
               "intimate knowledge of both the hardware and the operating system."))

    o.append(h3("System Development"))
    o.append(p("The software component of any computerized instrumentation system can form a "
               "significant percentage of its total cost. This is especially true of on-off "
               "systems which require software to be developed for a specific application, where "
               "the cost of the implementation of the software and its maintenance can "
               "considerably exceed the hardware costs. In such circumstances the ability to "
               "reuse existing code and the access to powerful development systems and debugging "
               "tools are of crucial importance. Some debug software only provides support for "
               "stepping through the operation of code written at the assembly code level. When "
               "developing device drivers, for example, access to a source-level debugger which "
               "can link the execution of code written in a high-level language to the contents "
               "of processor registers is useful."))
    o.append(p("Many SBCs that are intended for operation as stand-alone microcontrollers, "
               "instead of in bus-based systems, are often supported by a high-level language "
               "such as C or FORTH and a development environment. A common practice is to "
               "utilize a PC to develop the code which can be downloaded via a serial link to "
               "the microcontroller. Some debugging support for the execution of the code on the "
               "microcontroller is also provided. The development of powerful compact Intel 486 "
               "or Pentium microcontroller cards running operating systems such as MS DOS can "
               "greatly reduce software development time because of the ready access to PC-based "
               "software. The implementation of systems based on dedicated microcontrollers may "
               "require the use of a logic analyzer to view data on system buses."))

    o.append(h2("86.3 Computer Buses"))
    o.append(h3("The VMEbus (IEEE P1014)"))
    o.append(p("The VMEbus [1–3], utilizes a backplane fitted with two 96-pin connectors (called "
               "P1 and P2). The P1 connector provides access to all the bus signals with the "
               "exception of bits 16 to 31 of the data bus and bits 24 to 31 of the address bus, "
               "which are provided on the P2 connector. The location of cards in a VME system is "
               "important, as slot 1 must contain the system controller and the priority of the "
               "SBCs is determined by their proximity to the system controller SBC. As only 32 "
               "of the pins on the P2 connector are defined, the remaining 64 tracks on the P2 "
               "backplane may be specified by the user. VME cards may be single height (fitted "
               "with a P1 connector only) or double height (fitted with both P1 and P2 "
               "connectors). Single-height boards are 100 mm high and 160 mm deep and fit 3U "
               "height cardframes. Double-height boards are 233.35 mm high and 160 mm deep and "
               "fit 6U height cardframes."))

    o.append(h4("VMEbus Signals"))
    o.append(p("The VMEbus can be described as having four distinct groups of signals."))
    o.append(p("<b>Data Transfer Bus (DTB).</b> The DTB provides 32-bit data transfer with "
               "32-bit address information using a nonmultiplexed asynchronous approach. "
               "Transfer is supported by a simple handshake mechanism with the bus master "
               "initiating the transfer providing an address strobe (AS) signal to tell the "
               "destination card to read the address information. The master also controls two "
               "data strobe (DS1 and DS2) lines which in a write operation indicate the presence "
               "of valid data on the data bus and in a read operation that the master is ready "
               "to receive data from the slave. The slave card uses the data acknowledge signal "
               "(DTACK) in a read operation to indicate that it has placed valid data on the bus "
               "and in a write operation to confirm that it has read the data. There is clearly "
               "a danger that the bus will hang up if the slave does not respond to a request "
               "for a data transfer, so in most VME systems a watchdog timer is provided to "
               "produce a signal on the bus error (BERR) line if a DTACK signal is not detected "
               "within the time-out period."))
    o.append(p("Revision C of the VME bus specification will support 8-, 16-, and 32-bit data "
               "transfers, whereas revision D supports 64-bit transfers by making use of the "
               "address bus to transfer the additional 32 bits. Data may also be transferred in "
               "blocks of up to 256 bytes without the need to retransmit the address "
               "information. Most SBCs have both master and slave interfaces allowing their "
               "memory to be accessed from other SBCs in the system. The VME bus also supports "
               "three types of addressing mode, short (16 bit), standard (24 bit), and extended "
               "(32 bit), allowing the memory decoding circuitry of cards to be minimized for "
               "small systems or for input/output cards. Six address modifier lines (AM0 to AM5) "
               "are used to indicate the addressing mode and also to give information about the "
               "mode of transfer (e.g., block transfer and whether the transfer is in privileged, "
               "supervisor, or nonprivileged mode)."))
    o.append(p("<b>Arbitration Bus.</b> The arbitration bus provides a mechanism for deciding "
               "which master is allowed to gain control of the bus. The arbitration bus provides "
               "four bus request lines (BR0 to BR3) and four bus grant lines. The SBC in slot 1 "
               "of the VME bus acts as a bus controller which provides arbitration using a "
               "number of scheduling algorithms. In a simple priority-based algorithm each of "
               "the bus request lines is assigned a priority, whereas in a round-robin system "
               "access to the bus cycles around the bus request lines. Each of the four bus "
               "grant lines is in fact allocated two pins on the P1 connector (see Figure 86.4). "
               "The bus grant signal therefore passes through each card (called daisy chaining); "
               "thus, in Figure 86.4 the signal enters via BG1IN and exits via BG1OUT. This "
               "scheme allows a card to intercept the bus grant signal, giving cards nearer the "
               "system controller a higher priority. A consequence of daisy chaining is that any "
               "unused card slots must be fitted with jumpers between the bus grant pins."))
    o.append(fig(4, "en"))
    o.append(p("<b>Priority Interrupt Bus.</b> The priority interrupt bus provides seven "
               "interrupt request lines (IRQ1 to IRQ7) with IRQ7 having the highest priority. "
               "The interrupt requests may be handled by several SBCs, provided that all "
               "interrupts of the same level are handled by the same master. The interrupt "
               "acknowledge line is daisy chained though the cards in a similar way to the bus "
               "grant lines (the pins are called IACKIN and IACKOUT). Again, any unused card "
               "slots must be fitted with jumpers between these pins."))
    o.append(p("<b>Utility Bus.</b> The utility bus provides the power supply tracks, the system "
               "reset, a 16-MHz clock and two system failure lines, SYSFAIL, which allows a card "
               "to indicate that it has suffered a failure, and ACFAIL, which is generated by "
               "the power supply monitor. Both failure lines are handled by the system "
               "controller SBC."))
    o.append(p("Associated with the VMEbus is VXI (VMEbus extensions for instrumentation). This "
               "blends the IEEE 1014 VMEbus standard with the IEEE-488 instrumentation bus using "
               "the uncommitted pins on the P2 connector to form the IEEE P1155 standard."))

    o.append(h3("Multibus II (IEEE 1296)"))
    o.append(p("Multibus II [3] is a synchronous bus system which is implemented on a single "
               "96-track backplane. Cards conform to the Eurocard format of 220 × 233.65 mm; "
               "however, the bus requires only a single 96-pin DIN 41612-type connector. A second "
               "connector may be used to support a local bus or merely provide mechanical "
               "stability for a double-height card."))
    o.append(p("Unlike VME, the Multibus II standard has the following features:"))
    o.append(ol([
        "A synchronous bus; i.e., data transfer is linked to the bus clock rather than the "
        "strobe/acknowledge control lines of the asynchronous VME system;",
        "A 32-bit multiplexed address and data bus;",
        "A message-passing strategy as an alternative to interrupt request lines;",
        "Distributed bus arbitration rather than a central system controller (each card "
        "contains a message-passing controller, MPC, chip which participates in implementing "
        "the message passing algorithm);",
        "Only intelligent cards (i.e., fitted with microprocessors) that can interface to the "
        "main bus; simple input/output (I/O) cards should make use of a local bus (e.g., the "
        "iLBX bus) using the second DIN connector.",
    ]))

    o.append(h4("Multibus Signals"))
    o.append(p("Multibus II may be described as having five distinct groups of signals."))
    o.append(p("<b>Central Control.</b> The central services module (CSM) in slot 0 is "
               "responsible for the generation of this group of signals. The CSM may be "
               "implemented on a dedicated card or incorporated onto a SBC. The CSM produces the "
               "10-MHz bus clock as well as a range of reset signals to support both a cold and "
               "warm start as well as recovery from power supply failure."))
    o.append(p("<b>Address/Data.</b> Multibus II supports a 32-bit multiplexed address/data bus "
               "(AD0 to AD31) with four parity lines (PAR0 to PAR3) providing parity information "
               "for each data byte. As in all synchronous systems, data are only sampled on an "
               "edge of the system clock, a feature that enhances noise immunity."))
    o.append(p("<b>System Control.</b> There are ten system control lines (SC0 to SC9) which "
               "provide basic handshake information to assist data transfer, e.g., requester is "
               "ready or replier is not ready. In addition, these lines are used to convey "
               "information such as data width, data error indication, and whether the bus is in "
               "the request or reply phase."))
    o.append(p("<b>Exception Signals.</b> Two exception signals, bus error (BUSERR) and time-out "
               "(TIMOUT), are provided. Any card detecting a data integrity problem must report "
               "this to all other cards using BUSERR. The CSM generates a TIMOUT when it detects "
               "a data communications hang up on the bus."))
    o.append(p("<b>Arbitration Group.</b> The arbitration signals, which determine which card "
               "gains control of the bus, consist of a single bus request line (BREQ) and six "
               "Bus Arbitration lines (ARB0 to ARB5). To request exclusive use of the bus, a "
               "card asserts the BREQ line and provides it arbitration ID on ARB0 to ARB4. It "
               "also uses ARB5 to indicate whether the request has high priority or whether "
               "“fairness mode” is acceptable. In this latter mode the card will not make "
               "another request until after all other requesters have used the bus. Each card "
               "has the same bus arbitration logic within its MPC chip. If several cards make "
               "high-priority requests, the order of access is determined by the numerical value "
               "of the arbitration ID."))

    o.append(h4("Message Passing on Multibus II"))
    o.append(p("Multibus II uses message passing to implement block data transfers and interrupt "
               "requests. Each MPC chip contains a first-in first-out (FIFO) buffer, which "
               "ensures that the full bandwidth of the bus can be utilized by storing data "
               "immediately before or after transfer. In “solicited” transfers, the MPCs "
               "cooperate by warning each other that a message is to be sent. These messages may "
               "be sent as 32-byte packets in a manner that is analogous to the block transfer "
               "mechanism in VME. “Unsolicited” packets not expected by the receiving MPC are "
               "used to set up a block transfer or to act as the equivalent of interrupt request "
               "signals."))

    o.append(h4("System Configuration"))
    o.append(p("Multibus II employs a software configuration approach in which information such "
               "as the base memory address and arbitration ID are sent down the bus rather than "
               "by the use of jumpers or dip switches. Some information such as card type and "
               "serial number are coded on the cards themselves."))

    o.append(h3("Other System Buses for Small-Scale Systems"))
    o.append(p("The G64/G96 and STE standards [3] are examples of buses well suited to small "
               "industrial real-time instrumentation and control systems because of their "
               "relatively simple and hence lower-cost bus interfaces, compared with VME and "
               "Multibus. Both buses support DMA, have multiprocessor bus arbitration, and use "
               "single-height Eurocard (100 × 160 mm) cards. Prototyping cards fitted with bus "
               "interfaces are readily available and may be used to develop custom designed I/O "
               "cards. Power is supplied on the buses at +5 and ±12 V. In addition, the real-time "
               "multitasking operating system OS-9 has been ported onto SBCs which operate with "
               "these buses. Development systems that support the use of MS-DOS are also "
               "available, thus providing access to a wide range of PC-based software especially "
               "for graphics applications."))
    o.append(p("The G64 bus, which was defined by the Swiss company Gespac in 1979, specifies 64 "
               "bus lines which are mapped to rows of a DIN41612 connector. The bus has a 16-bit "
               "nonmultiplexed data bus and a 16-bit address bus; 32-bit transfers may be "
               "achieved by multiplexing the upper 16 bits of the data bus with the address bus. "
               "The G96 standard adds a further 32 bus lines by making use of the third row of a "
               "DIN41612 connector to extend the address bus width to 24 bits and provide "
               "additional interrupt request lines. The STE bus provides an unmultiplexed 8-bit "
               "data and 20-bit address bus using 64-pin DIN41612 connectors."))

    o.append(h2("86.4 Personal Computer Buses"))
    o.append(p("There are three main bus standards for personal computers — industry standard "
               "architecture (ISA), extended ISA (EISA), and the microchannel architecture "
               "(MCA). In addition, the Personal Computer Memory Card International Association "
               "(PCMCIA) architecture has been developed primarily for use in laptop and "
               "notebook computers."))
    o.append(p("ISA and EISA are pin compatible and are both synchronous buses with a clock rate "
               "of 8 MHz regardless of the clock rate of the main processor, whereas the MCA bus "
               "is an asynchronous bus. Slow slave add-on cards can utilize the ISA and EISA "
               "buses by using an appropriate number of wait states. The MCA architecture will "
               "not be covered in this chapter. Further details of these bus architectures are "
               "given in References 4 through 6."))

    o.append(h3("ISA Bus"))
    o.append(p("The original IBM PC and its clones used the standard PC bus which supported 8 "
               "data bus and 20 address bus lines and employed a 62-pin printed circuit card "
               "edge connector. When IBM introduced the PC-AT, a second 36-pin connector was "
               "added to the motherboard backplane slots to provide a 16-bit data bus and "
               "increase the number of address lines to 24. This new bus subsequently became "
               "known as the ISA bus and is capable of supporting both cards designed for the "
               "original PC bus, and cards with two connectors providing full 16-bit data "
               "access. The bus master line allows a card to take over control of the bus; "
               "however, this is generally only suited to long-term takeovers. The ISA bus "
               "supports 8-bit and 16-bit DMA transfers allowing efficient transfer of blocks of "
               "data, e.g., while loading software from disk into RAM. The ISA bus supports the "
               "I/O addressing mode of the Intel 80×86 range of processors with an I/O address "
               "space of 768 locations in addition to the 256 locations reserved for the "
               "motherboard."))

    o.append(h3("EISA Bus"))
    o.append(p("The EISA bus provides full 32-bit data and 32-bit address bus lines. ISA cards "
               "can fit into EISA bus connectors; however, cards designed for the EISA standard "
               "have bilevel edge connectors, providing double the number of contacts as an ISA "
               "card. The presence of a notch in the EISA cards allows them to be inserted "
               "farther into the motherboard socket than the ISA cards and thus mate with the "
               "additional contacts. The EISA standard increases the maximum ISA data width in "
               "DMA transfer to 32 bits and also provides a much-enhanced bus master. The "
               "following features of EISA are worthy of note."))
    o.append(h4("Bus Arbitration"))
    o.append(p("All EISA systems have a central arbitration control (CAC) device on the "
               "motherboard. The CAC uses a multilevel rotating priority arbitration scheme. The "
               "top-priority level rotates around three customers, the DMA controller, the "
               "dynamic memory refresh controller, and, alternately, either the main CPU or one "
               "of the bus master cards. A device that does not make a request is skipped over "
               "in the rotation process. The bus masters take it in turns to gain access to the "
               "top-priority level. Whereas ISA supported a single bus request line, the EISA "
               "standard provides a dedicated pair of request lines (MREQ0 to 14) and "
               "acknowledge lines (MAK0 to 14) for each bus master. (Note: Although this allows "
               "15 bus masters to be used, in many systems the chip set which implements the CAC "
               "supports bus masters in a limited number of the EISA sockets.) The CAC supports "
               "preemption, i.e., it allows a device making a request to capture control from "
               "another device if it is next in turn. A bus master card must release the bus "
               "within 64 bus clock cycles, whereas a DMA controller has 32 clock cycles to "
               "surrender the bus."))
    o.append(h4("Input/Output"))
    o.append(p("The EISA bus provides 768 additional I/O locations for each slot in addition to "
               "the 768 ISA I/O locations that may be accessed from any slot. EISA cards contain "
               "nonvolatile memory to store configuration information (see below), and a minimum "
               "of 340 bytes of the I/O address space of each slot is reserved for this "
               "purpose."))
    o.append(h4("System Configuration"))
    o.append(p("The EISA system provides support for automatic system configuration to replace "
               "the use of jumpers and dip switches to specify parameters such as the base "
               "memory address, interrupt request line number, or DMA channel number used by "
               "each add-on card. Information on the product type and manufacturer are stored on "
               "each EISA add-on card is read by the CPU during system start-up, making it "
               "possible to identify the slots that are fitted with full EISA cards. "
               "Manufacturers of both ISA and EISA cards should supply a configuration file "
               "containing information on the programmable options that are available. When a "
               "system configuration program is run, an optimum configuration of the boards will "
               "be determined, and the configuration information written into the I/O space of "
               "each EISA card. For ISA cards, the user can be informed of the required jumper "
               "settings."))

    o.append(h3("PCMCIA"))
    o.append(p("The PCMCIA architecture was developed by the Personal Computer Memory Card "
               "International Association and the Japan Electronics Industry Development "
               "Association for removable add-on cards for laptop and notebook computers. Each "
               "PCMCIA socket has its own host bus adapter (HBA), which acts as an interface to "
               "the main computer bus. Cards may be plugged into PCMCIA sockets either before or "
               "after the computer has been powered up. There are three types of PC card all "
               "with the same planar dimensions (54.00 × 85.6 mm) but with differing thicknesses, "
               "namely, 3.3 mm for type I, 5.0 mm for type II, and 10.5 mm for type III. Cards "
               "and sockets are keyed to prevent them from being inserted the wrong way round. "
               "The PCMCIA standard supports cards that operate at several possible voltage "
               "levels, i.e., 5.0 V cards, 3.3 V cards, or dual-voltage 5.0 V/3.3 V cards."))
    o.append(h4("Configuration"))
    o.append(p("PC cards contain configuration information called the card information structure "
               "(CIS) which is stored in nonvolatile memory. Cards may be configured either on "
               "system power-up or on insertion of the card into the socket (i.e., plug and "
               "play). Configuration is carried out using a form of device driver called an "
               "enabler. The enabler may make use of two additional software services called "
               "card services and socket services. Socket services, which may be contained in "
               "ROM on the PC or loaded from disk during power-up, provide function calls to "
               "allow the HBA to be configured to cooperate with the PC card. Card services, "
               "which may be an extension to the operating system or an installable device "
               "driver, act as a server for the enabler, which performs as a client. Card "
               "services provide a range of functions such as accessing the CIS of the card, "
               "requesting system resources required by the card, and telling the enabler that a "
               "card has been inserted or removed from the socket. Enablers may be classified as "
               "dedicated to one particular card or generic, i.e., designed for a range of "
               "cards. Note that early PCMCIA cards were not designed for use with card "
               "services."))
    o.append(h4("The PCMCIA Socket Interface"))
    o.append(p("The PCMCIA socket comprises a 68-pin connector with 26 address lines providing "
               "access to 64 MB of memory space and a 16-bit data bus. Two Vcc pins and four "
               "ground pins are supplied. The maximum current that can be supplied to the card "
               "is 1.0 A with a maximum of 0.5 A from each of the two power supply pins. Release "
               "2.x sockets apply 5.0 V to the Vcc pins on power-up and reduce this to 3.3 V if "
               "the card has dual-voltage capability. Cards that operate at 3.3 V only are keyed "
               "so they cannot fit into this type of socket and only into low-voltage sockets. "
               "The supply voltage provided by low-voltage sockets depends on the logic state of "
               "its voltage sense inputs. A PCMCIA socket can be configured either as a memory "
               "only socket or as a memory or I/O socket. Initially, the socket acts as a memory "
               "only socket but is converted by the enabler to a memory or I/O socket if the card "
               "is required to support I/O functions. In this mode the card can generate an "
               "interrupt request via a single IRQ pin and support both 8-bit and 16-bit I/O data "
               "transfers. DMA may be supported but not by Release 2.x systems."))

    o.append(h3("PC/104"))
    o.append(p("The enormous popularity of PC architecture resulted in its use in embedded "
               "systems. A need then arose for a more compact implementation of the ISA bus that "
               "could accommodate the reduced space and power requirements of embedded "
               "applications. The PC/104 specification (1992) was adopted as the base for an "
               "IEEE draft standard called the P996.1 Standard for Compact Embedded PC Modules. "
               "The key features of the PC/104 are"))
    o.append(ul([
        "Size reduced to 90 × 96 mm (3.550 × 3.775 in.);",
        "Self-stacking bus allowing modules to be “piggy-backed” and eliminating backplanes or "
        "cardframes;",
        "Rugged 64-contact and 40-contact male and female headers replacing the PC edge "
        "connectors (64 + 40 = 104, hence PC/104);",
        "Lower power consumption (<2 W per module).",
    ]))
    o.append(p("PC/104 CPU modules range from a basic 9.6-MHz, 8088 compatible XT with one "
               "serial port and a keyboard connector to a 100-MHz, 80486DX4 with four serial "
               "ports, parallel port, IDE disk controller, display controller, Ethernet adapter, "
               "keyboard port, and up to 64 MB of on-board RAM. Pentium-based systems are also "
               "available. Systems can be customized from a wide range of modules, including "
               "data acquisition boards, solid-state disk modules, and LAN support, all in the "
               "same 3.6 by 3.8 in. stackable format."))
    o.append(p("The wide availability of software development tools for the PC, the large number "
               "of software developers familiar with the PC environment, and the ease of "
               "transferring software developed on a conventional PC to the PC/104 make this an "
               "increasingly popular format."))
    o.append(p("Table 86.3 lists some manufacturers and suppliers of bus-based systems and "
               "industrial computers."))
    o.append(table_86_3("en"))

    o.append(h2("86.5 Peripherals"))
    o.append(p("Computer peripherals fall conveniently into two categories. The first category "
               "may be considered to be internal to the computer system and comprises cards "
               "plugged directly into a computer bus slot. The second category comprises "
               "instruments external to the computer but controlled by it. These external "
               "instruments are usually themselves “intelligent,” being controlled by their own "
               "CPU, and are linked to the main computer by a serial (RS-232) line or the "
               "IEEE-488 bus (GPIB). Such instruments may normally be operated in a stand-alone "
               "mode in response to their front panel controls without the requirement of an "
               "external computer."))

    o.append(h3("Internal Cards"))
    o.append(p("Internal cards are available to perform a wide range of functions. Table 86.4 "
               "provides a brief list of representative types. Note that both the serial "
               "interface and the IEEE-488 adapter required for the control of external "
               "“intelligent” peripherals will be fitted as internal cards. Almost all internal "
               "peripherals need to be configured before use to set up such parameters as the "
               "base address, the interrupts, and/or DMA channels used. This may involve setting "
               "jumpers or switches on the card or may be accomplished under software control "
               "using a configuration file supplied by the manufacturer. To operate the cards, "
               "bytes are written or read from appropriate addresses on the cards by the "
               "controlling SBC. The mechanism for doing this is discussed further in the section "
               "concerned with software for data acquisition. Further detail on some of the card "
               "types is given below."))
    o.append(table_86_4("en"))

    o.append(h4("Display Adapter"))
    o.append(p("While graphics support is normally available as standard on a PC-based system, "
               "this is not the case with other bus-based systems such as VME or Multibus. These "
               "systems are provided with a serial port that may be connected to a terminal to "
               "provide a text-only dialogue with the operating system running on the SBC. In "
               "such circumstances the choice of display adapter will determined by the user "
               "requirements, taking into account the support for the device provided by any "
               "software packages that are to be used. If the user intends to write custom "
               "graphics software, it is essential to ensure that a graphics library is "
               "available from the vendor providing as a minimum line drawing, arc drawing, and "
               "block color fill facilities."))

    o.append(h4("IEEE-488 Adapter"))
    o.append(p("This device provides support for communications across the IEEE-488 bus or GPIB "
               "(general purpose interface bus). The bus itself comprises eight data lines, five "
               "interface management lines and three handshake lines. Transfers are parallel, "
               "synchronous, and at rates up to 1.5 MB/s. The IEEE-488 bus and its applications "
               "are discussed further in the section on external instruments."))

    o.append(h4("Serial Communications Adapter"))
    o.append(p("This device provides support for serial communications using the RS-232, RS-422, "
               "or RS-485 standards. It is used to provide a text-based terminal for systems "
               "based on Multibus or VME and to communicate with “intelligent” instruments such "
               "as position controllers, multimeters, or storage oscilloscopes fitted with "
               "similar interfaces."))
    o.append(p("Serial adapters convert parallel data to and from a bit stream in which each "
               "data byte (5, 7, or 8 bits) is framed by a start bit, an optional parity bit and "
               "one or more stop bits. The bit stream may be sent via a circuit consisting of "
               "only two wires at rates of up to 115,200 bits per second (commonly referred to "
               "as 115200 baud). Common bit rates are 300, 600, 1200, 2400, 4800, 9600, 19200, "
               "28800, 38400, 57600, 115200 baud. Both the transmitting and receiving adapters "
               "must be configured, normally by software, for the same baud rate, number of data "
               "bits, stop bits, and parity. Some form of flow control to prevent a receiver "
               "from being overloaded with incoming data is essential. This is accomplished "
               "either by separate handshake lines (e.g., those denoted by RTS and CTS in the "
               "standard) or by software where the receiver sends a special control byte (XOFF) "
               "back to the transmitter telling it to stop sending until it receives a second "
               "control byte (XON) to reenable it. For historical reasons the RS-232 standard "
               "does not define a bidirectional handshake procedure, and manufacturers have been "
               "forced to implement their own schemes which are not always compatible with each "
               "other."))
    o.append(p("Serial communication between devices may be"))
    o.append(ul([
        "<b>Full duplex</b>, where either device may transmit or receive data at any time;",
        "<b>Half duplex</b>, where both devices are capable of transmission or reception but "
        "only one may transmit at any instant;",
        "<b>Simplex</b>, where one device is a transmitter, one is a receiver, and data can only "
        "flow in a single direction.",
    ]))
    o.append(p("RS-232, developed by the Electronics Industries Association (EIA), is the oldest "
               "standard, originally developed in the early 1960s, to allow mainframe computers "
               "to communicate with terminals via modems and telephone lines. This is the origin "
               "of the names of some of the connections (e.g., RI ring indicator, DCD data "
               "carrier detect), which have no relevance in the applications considered here. A "
               "related problem is that the standard expects that the devices being connected are "
               "data terminal equipment (DTE), at one end of the link, and data communication "
               "equipment (DCE) at the other. Computers and terminals are DTE, while modems are "
               "DCE. The most commonly used revision of the standard, RS-232-C (revisions D and E "
               "also exist), was made in 1969 and is still widely used. Serial communication is "
               "made using voltage levels in the region of ±12 V, over distances up to 15 m "
               "(50 ft) at speeds up to 20000 baud."))
    o.append(p("RS-422, also developed by the EIA, is an enhancement of the RS-232 standard. "
               "Differential transmitters and receivers are employed which allow one transmitter "
               "to drive up to ten receivers, using a twisted-pair connection for each circuit, "
               "at bit rates up to 10 MBaud at distances up to 12 m (40 ft) or 100 kBaud at "
               "distances up to 1200 m (4000 ft). The RTS and CTS lines (defined in the standard) "
               "are used for flow control, while the RXD and TXD lines are used to transmit and "
               "receive data. Thus, a two-twisted-pair cable is required for duplex connection "
               "without hardware handshaking. A four-twisted-pair cable is required if hardware "
               "handshaking is used."))
    o.append(p("RS-485 is based on RS-422 and allows up to 32 driver/receiver pairs to be "
               "connected to a common data bus (two twisted pairs). Clearly, only one device can "
               "be allowed to transmit at any one time. The RTS circuit is used to disable the "
               "other transmitters connected to the bus if a device is required to transmit "
               "data. Handshaking is performed using software."))
    o.append(p("The serial interfaces on instruments are usually configured as DTE devices. We "
               "are faced with the problem of connecting one DTE device (the computer serial "
               "interface) to another (the instrument), which is not what the RS-232 standard was "
               "designed for. Furthermore, since the standard does not define a bidirectional "
               "handshake to control data flow, several incompatible handshaking schemes exist. "
               "A comprehensive survey of these is presented in Reference 7. A common solution to "
               "the DTE to DTE connection problem is the so-called null modem, which nothing more "
               "than a specially wired cable. Figure 86.5 shows two such connection schemes. One "
               "requires the software handshaking procedure and the other implements a "
               "bidirectional hardware handshake. The reader should refer to Reference 7 for "
               "details of other schemes and for the definitions of the mnemonics used to label "
               "the connections."))
    o.append(fig(5, "en"))
    o.append(p("Some common problems encountered in practice are"))
    o.append(ol([
        "<b>The received data are garbage.</b> This is almost always due to the baud rate, "
        "parity, and number of stop bits not being the same at both ends of the link.",
        "<b>Data initially correct, but parts in the middle are missing.</b> This is probably a "
        "handshake problem. The transmitting device is sending data faster than the receiver can "
        "process it.",
        "<b>No communications at all.</b> Probably a handshake problem where the transmitter "
        "does not sense that the receiver is ready.",
    ]))

    o.append(h4("Digital Input and Output"))
    o.append(p("These cards provide I/O lines, normally in groups of eight, which may be used to "
               "sense or generated digital signals for devices outside the computer. A group of "
               "eight input lines is referred to as an (8-bit) input port and a group of eight "
               "output lines as an (8-bit) output port. Input and output levels vary from card to "
               "card and it is best to consult the appropriate data sheet. Typically, voltages "
               "between 2.5 and 5.0 V are considered as high logic levels, whereas voltages "
               "between 0.0 and 0.5 are considered as low logic levels. These levels are "
               "sometimes referred to loosely as TTL (transistor transistor logic) levels. Note "
               "that the actual logic levels used by the various TTL families differ from these "
               "slightly. The “high” and “low” ranges may be slightly different for input and "
               "output lines. Output lines often have limited current sourcing and sinking "
               "abilities compared with TTL, and it is therefore often necessary to buffer them. "
               "It is important that voltages exceeding the maximum rated values do not appear on "
               "inputs or outputs (e.g., attempting to switch an inductive load might produce a "
               "dangerously high transient voltage at an output); otherwise, the device may be "
               "damaged. Where this is likely to be a problem, inputs and outputs should be "
               "suitably buffered or even optically isolated, which provides protection up to a "
               "few kilovolts. Outputs may also drive appropriately connected relays. I/O cards "
               "with these facilities on board are readily available."))
    o.append(p("As a minimum, an I/O card may be expected to support a control register, two I/O "
               "ports each with an associated data register, and some handshake lines. Handshake "
               "lines may sometimes be used to generate interrupts on the controlling SBC. A byte "
               "written to the control register is used to configure the I/O ports, i.e., to "
               "determine if they are to behave as input or output ports as well as to select the "
               "function, if any, of the handshake lines. It may not be possible to select the "
               "direction of optically isolated or buffered ports. Writing a byte to an output "
               "port causes a pattern of high and low voltages to appear on the lines reflecting "
               "the pattern of zeros and ones in the binary representation of the byte written. "
               "Similarly, when a byte is read from an input port, the number read is specified "
               "in binary representation by the pattern of high and low logic levels on the input "
               "lines. The following example illustrates this."))
    o.append(p("The Intel 8255 Programmable Peripheral Interface (PPI) is commonly used in "
               "digital I/O cards for the PC. Data for this device are readily available [8]. The "
               "8255 provides three ports, denoted A, B and C, and a control register. Ports A "
               "and B may be designated as an 8-bit input port or an 8-bit output port. Port C "
               "may be considered as two independent four-bit ports, which may be chosen "
               "independently as input or output. Port C may also provide handshake functions. "
               "There are three modes in which the chip may operate. The simplest, mode 0, which "
               "provides basic input and output without automatic handshaking, is used in our "
               "example. Note that the 8 bits of an I/O port are conventionally labeled bits 0 to "
               "7. This is because bit 0 is weighted 2" + _sup("0") + ", bit 1 weighted "
               "2" + _sup("1") + ", etc. in the binary representation of the number read from or "
               "written to the port."))
    o.append(p("To configure the PPI to operate in mode 0 with port A as an input port and port B "
               "as an output port the bit pattern 10011001 must be written to the control "
               "register. This number is equivalent to 99 in hexadecimal or 153 in decimal. "
               "Suppose now that switches connected to port A hold bits 2 and 7 high and the "
               "remaining bits low. The resulting binary pattern will be 10000100, which is "
               "equivalent to hexadecimal 84 or decimal 132. When port A is read, the number 132 "
               "(decimal) will therefore be obtained. To hold the lines connected to bits 2, 3, "
               "and 5 of port B high while leaving the remaining lines low, we see that the "
               "binary pattern 00101100 must appear at port B. 00101100 binary is equivalent to "
               "2C hexadecimal or 44 decimal. We therefore write the decimal number 44 to port "
               "B."))

    o.append(h4("Counter/Timers"))
    o.append(p("These devices typically provide software programmable event counting, pulse, and "
               "frequency measurement. As output devices, they may generate a single pulse "
               "(one-shot) when a programmable number of input pulses have been counted and "
               "produce square waves of arbitrary frequency and complex duty cycles. Frequencies "
               "generated are normally based on an on-board crystal clock to provide independence "
               "from the internal clock speed of the computer. Counter/timer cards commonly "
               "support at least three independent 16-bit counters."))
    o.append(p("Common applications include:"))
    o.append(ol([
        "<b>Alarms.</b> The counter is in one-shot mode and generates a single pulse on timeout. "
        "This is connected to interrupt the computer and alert the user in the middle of the "
        "currently executing task.",
        "<b>Watchdog timer.</b> This is used to detect problems, particularly in systems which "
        "are intended to operate without operator intervention. It is similar to the Alarm "
        "described earlier except that the interrupt is used to reset the computer. In normal "
        "operation this will never occur as all software tasks executing are designed to update "
        "the counter constantly so that it never reaches its terminal count. Only if a problem "
        "develops, e.g., a software “crash,” will the counter time out and the system be reset.",
        "<b>The generation of complex waveforms</b>, e.g., for pulse width modulation. This "
        "application uses two counters in cascade, one (T1) to provide regular pulses at the "
        "carrier frequency triggering another (T2), in one-shot mode, to provide the variable "
        "duty cycle as shown in Figure 86.6.",
    ]))
    o.append(fig(6, "en"))

    o.append(h4("Analog Input"))
    o.append(p("An analog input card uses an analog-to-digital converter (ADC) that accepts an "
               "input voltage and supplies an integer proportional to that voltage to the "
               "computer. Many cards now are produced with on-board signal conditioning circuits "
               "that provide for variable gain either by means of switches or under program "
               "control. Cards with specialized signal conditioning circuits for common "
               "applications such as thermocouple linearization or interfacing to strain gages "
               "and other bridge sensors, are available. Signal conditioning to protect cards "
               "destined to be used in hostile electrical environments is also available. Cheaper "
               "cards may provide fixed gain and require additional signal conditioning circuits "
               "to be provided external to the computer. Many cards also feature multiplexed "
               "inputs where one of several inputs may be selected under program control to be "
               "fed to the ADC. Some important parameters to consider in selecting an analog "
               "input board are given in Table 86.5."))
    o.append(table_86_5("en"))
    o.append(p("At rates above a few tens of kilohertz, interrupt-driven data capture is "
               "essential to maintain speed. Faster data rates require on-board memory to avoid "
               "degrading the performance of the controlling SBC. In this case DMA may be used "
               "to transfer data to main memory and increase performance further."))
    o.append(p("A timer function is often incorporated to allow samples to be taken at regular "
               "intervals independently of what the controlling SBC is doing. An interrupt is "
               "generated when the conversion is complete, and an interrupt service routine is "
               "then activated to read the result of the conversion into memory. The writing and "
               "installation of interrupt service routines is not a trivial task and is best "
               "left to those with an intimate knowledge of the operating system running on the "
               "SBC. Fortunately, most manufacturers supply software (device drivers) for this "
               "purpose. The simpler analog input boards may be driven by writing values directly "
               "to registers on them in a similar manner to the example given for digital I/O "
               "cards. Manufactures now commonly provide a software library which may be called "
               "from a variety of high-level languages to allow the user to access the card in a "
               "more intuitive way. This is discussed further in the section on software."))

    o.append(h4("Analog Output"))
    o.append(p("Analog output cards are available as 8-, 10-, or 12-bit devices. Frequently, a "
               "card will support several channels of analog output with provision for delaying "
               "the updating of channels so that all can be updated simultaneously. Output "
               "voltages may be unipolar or bipolar and current outputs (4 to 20 mA) are also "
               "available. Signal conditioning (buffering) is necessary to drive loads drawing "
               "currents of more than a few milliamps. Special care should be taken with "
               "inductive loads, e.g., motors to avoid damage to the device by transient "
               "voltages. Specially designed position control modules incorporating suitably "
               "buffered analog and digital I/O are available for this purpose."))

    o.append(h3("External Peripherals"))
    o.append(p("These are usually “intelligent” devices which can operate via their front panel "
               "controls without another computer but are additionally capable of being "
               "controlled by a computer. Many common laboratory instruments are available with "
               "such facilities, including power supplies, signal generators, storage "
               "oscilloscopes, voltmeters, spectrophotometers, and position controllers. A "
               "computer can coordinate the actions of several such instruments to gather then "
               "manipulate and display data in a way which enhances the power of the "
               "instrumentation system. An almost trivial example is the use of a computer to "
               "control a signal generator and a voltmeter in order to generate the frequency "
               "response of an amplifier automatically. Such a system has an obvious role in "
               "automatic testing rigs."))
    o.append(p("Two common methods are used to control such devices: a serial link or the "
               "IEEE-488 bus. In both cases the devices are controlled by sending messages "
               "consisting of sequences of ASCII characters. Usually the sequences are chosen to "
               "have an obvious meaning, as in the example that follows, but this is not always "
               "the case — particularly with older devices where user friendliness was often "
               "sacrificed as a result of limited memory and processing power! The message "
               "sequence"))
    o.append(_code(["“FREQ10kHz”", "“SINE”", "“1.0VOLTRMS”"]))
    o.append(p("might be used to set a signal generator to produce a 10-kHz sinusoidal signal at "
               "1 V rms. There is little standardization in the form of device messages used "
               "although the IEEE standard 488.2 goes some way in this direction. Responses from "
               "instruments are sent in the same way, i.e., as ASCII characters so that a "
               "voltmeter might respond to a command to make a measurement with the data"))
    o.append(_code(["“AC2.01mV”"]))
    o.append(p("to indicate that it was on an ac voltage range and measured 2.1 mV. Again, there "
               "is little standardization in the format of responses. Large blocks of data may "
               "be send in a binary format where possible (8-bit serial links or IEEE-488 bus) "
               "to minimize the amount of data to be transferred."))

    o.append(h4("Serial Devices"))
    o.append(p("Serial control of devices is accomplished using links conforming to one of the "
               "serial standards (RS-232, RS-422, or RS-485) described elsewhere in this chapter. "
               "This is a relatively simple method of control and has the advantage that much of "
               "the preliminary testing and debugging of a system can be done using a terminal "
               "or a terminal emulator program such as the public domain KERMIT available from "
               "Kermit Distribution (Columbia University Academic Information Systems, 612 West "
               "115th Street, New York, NY 10025, Phone: 212-854-3703). The writing of custom "
               "software that accesses the serial interface of the controlling computer is "
               "relatively easy under common operating systems including DOS, Windows, Windows "
               "95, UNIX, and OS-9 using languages such as C, Pascal, or BASIC. It is "
               "increasingly common, particularly for DOS and Windows applications, for "
               "manufactures to provide software support for their devices."))
    o.append(p("Disadvantages of serial transfers are the relative slowness when large amounts "
               "of data are transferred, the lack of standardization in device messages, and the "
               "limited control facilities available. Advantages are the ease of testing, the "
               "simplicity of the controlling software, the relative simplicity of the "
               "interconnection scheme, and — for remote instrumentation systems — the fact that "
               "with the use of modems data can be transferred over large distances using "
               "standard telephone lines or even a radio link."))

    o.append(h4("IEEE 488 Devices"))
    o.append(p("The IEEE standard 488 was developed in the 1970s and rapidly became an industry "
               "standard for the interconnection and control of test equipment. This standard "
               "was modified slightly in 1987 (IEEE standard 488.1) to allow for the considerable "
               "enhancements of IEEE standard 488.2 which was introduced at the same time [9,10]. "
               "The original IEEE standard 488 specifies the electrical characteristics of the "
               "bus, the mechanical characteristics of its connectors, and a set of messages to "
               "be passed between interfaces. It does not attempt to provide any syntax or "
               "structure for communicating these messages, to specify commonly used commands, "
               "or to establish a standard for device-specific messages. These issues are "
               "addressed in IEEE standard 488.2."))
    o.append(p("The bus itself supports synchronous parallel transfers of data using three "
               "groups of lines,"))
    o.append(ul([
        "A bidirectional 8-bit data bus,",
        "Five interface management lines, and",
        "Three handshake lines,",
    ]))
    o.append(p("over distances of up to 20 m and at data transfer rates of up to 1 MB/s."))
    o.append(p("Devices on the bus are classed as talkers, listeners, or controllers. In "
               "general, the computer system is the bus controller which can also talk (send "
               "data) or listen (receive data). Most devices are both talkers and listeners: for "
               "example, a digital voltmeter will be a listener when receiving instructions to "
               "set the voltage range prior to making a measurement but will be a talker when "
               "returning the result of the measurement to the controller, which is itself acting "
               "as a listener. Each device on the bus must be assigned a unique address which is "
               "a number between 0 and 30. This may be done from the front panel of the device "
               "or, less conveniently, by setting switches elsewhere on the device."))
    o.append(p("It is a difficult, time-consuming, and error-prone process to write software to "
               "drive an IEEE-488 card. Purchasers of new IEEE-488 interfaces are strongly "
               "advised to obtain a device driver from the manufacturer. Such device drivers are "
               "now readily available and integrate the card into the filing system of the "
               "operating system running on the controlling computer. This allows the interface "
               "to be accessed in a natural way from high-level languages running on the "
               "controller."))

    o.append(h2("86.6 Software for Instrumentation Systems"))
    o.append(p("The difficulty involved in writing software for instrumentation systems depends "
               "largely on the support available from the manufacturers of the subsystems, on the "
               "operating system (if any), and on the development tools available. On one "
               "extreme, one may be working in a virtual instrument environment, such as that "
               "provided by the National Instrument LabVIEW, where software development is "
               "entirely graphical and, for small projects at least, is readily undertaken by "
               "users with little or no prior experience. On the other extreme, one is faced with "
               "the problem of developing software, which is at the very least interrupt driven "
               "and probably multitasking, for a target SBC with no resident operating system; "
               "this requires considerable expertise in software design and development together "
               "with the availability of development tools such as cross compilers and "
               "source-level debuggers."))

    o.append(h3("Virtual Instruments"))
    o.append(p("Figure 86.7 shows a layer model of the software for a generalized instrumentation "
               "system. The application layer handles the data acquisition, analysis, and "
               "presentation. The instrument drivers provide a mechanism for communicating with "
               "the instruments in a standard way without requiring the user to know about the "
               "often cryptic data strings which need to be sent. For example, all digital "
               "multimeters will need the facility to chose a specific input voltage range. The "
               "range coding, resolution, etc. that have to be sent to the multimeter to achieve "
               "this will vary from instrument to instrument; however, the instrument driver "
               "allows the software writer programming in the application layer to call a "
               "procedure such as"))
    o.append(_code(["SetVoltageRange(VoltageValue)"]))
    o.append(p("and this procedure call is the same for all multimeters. Although some "
               "manufacturers use the term slightly differently, the instrument driver is in "
               "effect the virtual instrument. Writing instrument drivers is a time-consuming but "
               "not too difficult task. Instrument drivers for proprietary instrumentation "
               "software design packages are readily available from instrument manufacturers. "
               "Device drivers integrate the controlling interface (e.g., IEEE-488, RS-232, or "
               "internal card) into the operating system of the computer. Writing a device driver "
               "requires a detailed knowledge of the device hardware and of the computer "
               "operating system. This is a difficult task and new interfaces should be purchased "
               "with a device driver appropriate for the operating system wherever possible."))
    o.append(fig(7, "en"))
    o.append(p("A number of development environments which are based on the virtual instrument "
               "concept are now available. These free the user from the problems of writing "
               "conventional software to control instruments and handle the data produced. "
               "Instruments appear to the software developer as “front panels” drawn on the "
               "computer screen, complete with familiar buttons, knobs, and displays. Data flow "
               "is handled by linking instruments in a block diagram using a mouse in an "
               "environment that resembles an ordinary drawing package. The software developer is "
               "working only in the application layer."))
    o.append(p("While the graphical environment allows simple systems to be developed rapidly, "
               "experienced programmers may find it restrictive. There are software development "
               "systems available that give the programmer access libraries containing instrument "
               "drivers, data analysis routines, graphics functions and data visualisations "
               "facilities in commonly used high-level languages such as C, Pascal, BASIC, and "
               "FORTRAN. Table 86.2 lists representative software packages."))

    o.append(h3("Working Directly with Peripherals"))
    o.append(p("It may occasionally be the case that the cost of software support for a virtual "
               "instrument development environment is not justified for a small application. "
               "Software must then be written to interface directly with the peripheral. The "
               "earlier section on digital input and output explained in principal what was "
               "necessary to program a simple interface chip. We now continue this example and "
               "show using the language C how this might be achieved."))
    o.append(p("The method of accessing the registers of peripheral cards depends on the "
               "microprocessor involved and may not even be a standard feature of the language "
               "being used. Where the peripheral forms part of the same address space as the "
               "computer memory, such as in the Motorola 680XX series, pointers can be used to "
               "read and write values in the registers. The Intel 80×86 series of processors "
               "often place peripherals in a separate address space which may not be accessed by "
               "pointers. In this case an extension to the language is required. Borland’s Turbo "
               "C and C++ provide functions to read and write I/O mapped devices:"))
    o.append(_code(["unsigned char inportb(int portid)",
                    "void outportb(int portid, unsigned char value)"]))
    o.append(p("These are used in the code fragment which implements the software for our "
               "earlier example. We assume that the 8255 PPI has base address 0x1b0 and that the "
               "program copies the value read from the input port (port A) directly to the output "
               "port (port B), until bit 0 of the input becomes zero"))
    o.append(_code([
        "/* define the addresses of the registers for the PPI */",
        "#define BASE 0x1b0",
        "#define PABASE",
        "#define PBBASE+1",
        "#define CONTROLBASE+3",
        "",
        "unsigned char xin;/* declare an 8-bit variable */",
        "outportb(CONTROL, 153)/* set port A as input, port B as output */",
        "do",
        "{",
        "        xin = inportb(PA);/* read the input */",
        "        outportb(PB,xin);/* write the output */",
        "}",
        "while(xin &amp; 1);    /* loop if bit 0 is still 1 */",
    ]))
    o.append(p("This fragment also illustrates that high-level languages generally only support "
               "input and output of bytes. Masking techniques must be used to access individual "
               "bits."))

    o.append(h3("The Choice of Operating System"))
    o.append(p("The software development support discussed so far is typically available under "
               "DOS, Windows 3.1, Windows 95, Windows NT, and UNIX. When a system is multitasking, "
               "it has to meet stringent real-time constraints; however, none of these operating "
               "systems is particularly appropriate. DOS does not support multitasking, and the "
               "others are not optimized for real-time systems which require speedy context "
               "switching and rapid interrupt response. The most fundamental requirement of "
               "real-time applications is that ability of the system to respond to external "
               "events with very short, bounded, and predictable delays. Table 86.6 lists some "
               "important real-time operating systems and kernels."))
    o.append(table_86_6("en"))
    o.append(p("Real-time operating systems tend not to have the mature and powerful software "
               "development support available for conventional operating systems. It is not "
               "possible simply to develop the software on a familiar operating system and then "
               "transfer the working programs to the target system. Much of the debugging, "
               "testing, and system integration will have to be done on the target itself to "
               "access the hardware. A common solution is a development system in which a "
               "conventional workstation is linked to the target system. Software is developed on "
               "the workstation using familiar tools, e.g., a Windows-based editor, support for "
               "version control, and a powerful filing system. At any time, code can be "
               "cross-compiled (i.e., compiled for the processor on the target system) and "
               "downloaded to the target. The workstation may then monitor the execution of the "
               "software running on the target processor. Features that allow the user to "
               "single-step through the source code, seen in a workstation window, while viewing "
               "the status of key variables in another are available. It is also possible to set "
               "breakpoints and allow the processes to run until one is encountered. Manufacturers "
               "of real-time operating systems are often able to provide development support of "
               "this type for their product for a variety of workstations."))

    o.append(h2("References"))
    o.append(refs([
        "Micrology pbt, Inc., <i>The VMEbus Specification Manual: Revision C1</i>, PRINTEX, "
        "1985.",
        "S. Heath, <i>VMEbus: A Practical Companion</i>, Boston, MA: Butterworth Heinemann, "
        "1993.",
        "J. Di Giacomo, Ed., <i>Digital Bus Handbook</i>, New York: McGraw-Hill, 1990.",
        "T. Shanley and D. Anderson, <i>ISA System Architecture</i>, 3rd ed., Reading, MA: "
        "Addison-Wesley, 1995.",
        "T. Shanley and D. Anderson, <i>EISA System Architecture</i>, 2nd ed., Reading, MA: "
        "Addison-Wesley, 1995.",
        "T. Shanley and D. Anderson, <i>PCMCIA System Architecture</i>, 2nd ed., Reading, MA: "
        "Addison-Wesley, 1995.",
        "M. D. Seyer, <i>RS232 Made Easy</i>, Englewood Cliffs, NJ: Prentice-Hall, 1984.",
        "Intel Corporation, <i>Intel Microsystems Component Handbook</i>, Vol. 2.",
        "IEEE Std 488.1-1987, <i>IEEE Standard Digital Interface for Programmable "
        "Instrumentation</i>.",
        "IEEE Std 488.2-1987, <i>IEEE Standard Codes, Formats, Protocols and Common Commands</i>.",
    ]))

    o.append(h2("Glossary"))
    o.append(_glossary(_GLOSS_EN))
    o.append(h2("Further Reading"))
    o.append(refs(_FURTHER_EN))
    return "".join(o)


# ================================================================ GLOSSARY
_GLOSS_VI = [
    ("Máy tính một bảng mạch (SBC)",
     "Bảng mạch đơn chứa bộ vi xử lý, bộ nhớ và các giao diện; đơn vị cơ bản của một hệ đo "
     "lường dựa trên máy tính."),
    ("Bus", "Tập hợp các đường dẫn điện dùng chung mà nhiều thẻ mạch cùng nối vào để trao đổi "
            "dữ liệu, địa chỉ và tín hiệu điều khiển."),
    ("Bảng mạch nền (backplane)",
     "Bảng mạch in có các khe cắm để gắn nhiều card và nối chúng với nhau qua bus."),
    ("Phân xử bus (arbitration)",
     "Thủ tục quyết định thẻ nào được quyền điều khiển bus tại mỗi thời điểm."),
    ("Chuỗi nối tiếp (daisy chain)",
     "Cách nối trong đó một tín hiệu đi xuyên qua từng card theo thứ tự, cho phép card chặn "
     "tín hiệu lại; dùng cho đường cấp bus và đường xác nhận ngắt của VME."),
    ("Chủ bus / tớ (bus master / slave)",
     "Chủ bus khởi phát việc truyền; tớ đáp ứng yêu cầu của chủ."),
    ("Trình điều khiển thiết bị (device driver)",
     "Đoạn mã tích hợp một card hoặc thiết bị vào hệ điều hành để phần mềm ứng dụng truy cập "
     "được tài nguyên phần cứng của nó."),
    ("Trình điều khiển thiết bị đo (instrument driver)",
     "Lớp phần mềm che giấu những chuỗi lệnh đặc thù của từng thiết bị đo sau một giao diện "
     "thủ tục thống nhất; thực chất chính là thiết bị đo ảo."),
    ("Thiết bị đo ảo (virtual instrument)",
     "Thiết bị đo được dựng bằng phần mềm, hiện ra trên màn hình như một mặt máy với núm và "
     "đồng hồ, thay cho phần cứng chuyên dụng."),
    ("Bộ định thời canh gác (watchdog timer)",
     "Bộ đếm phải được phần mềm cập nhật liên tục; nếu nó hết thời gian thì hệ thống được coi "
     "là đã sự cố và bị khởi động lại."),
    ("Điều chế độ rộng xung (PWM)",
     "Kỹ thuật thay đổi tỉ lệ thời gian có xung trên tổng chu kỳ để điều khiển công suất trung "
     "bình cấp cho tải."),
    ("Null modem",
     "Cáp được đấu dây đặc biệt để nối hai thiết bị DTE với nhau, vốn không phải là cấu hình "
     "mà chuẩn RS-232 được thiết kế cho."),
    ("DTE / DCE",
     "Thiết bị đầu cuối dữ liệu (máy tính, thiết bị đo) và thiết bị truyền thông dữ liệu "
     "(modem). RS-232 giả định một đầu là DTE và đầu kia là DCE."),
    ("Thời gian thực (real-time)",
     "Chế độ hoạt động trong đó mỗi tác vụ phải hoàn thành trong một khoảng thời gian xác định "
     "và dự đoán được."),
]

_GLOSS_EN = [
    ("Single-board computer (SBC)",
     "One board carrying a microprocessor, memory and interfaces; the basic unit of a "
     "computer-based instrumentation system."),
    ("Bus",
     "A set of shared conductors that several circuit cards tap into to exchange data, addresses "
     "and control signals."),
    ("Backplane",
     "A printed circuit board carrying slots for several cards and wiring them together on the "
     "bus."),
    ("Arbitration",
     "The procedure that decides which card may control the bus at any moment."),
    ("Daisy chain",
     "A wiring scheme in which a signal passes through each card in turn, letting a card "
     "intercept it; used for the VME bus-grant and interrupt-acknowledge lines."),
    ("Bus master / slave",
     "The master initiates a transfer; the slave responds to the master's request."),
    ("Device driver",
     "Code that integrates a card or instrument into the operating system so that applications "
     "can reach its hardware resources."),
    ("Instrument driver",
     "A software layer that hides each instrument's idiosyncratic command strings behind one "
     "uniform procedural interface; in effect the virtual instrument."),
    ("Virtual instrument",
     "An instrument built in software, presented on screen as a front panel of knobs and meters "
     "in place of dedicated hardware."),
    ("Watchdog timer",
     "A counter that software must keep refreshing; if it times out the system is assumed to "
     "have failed and is reset."),
    ("Pulse-width modulation (PWM)",
     "Varying the on-time within each period to control the average power delivered to a load."),
    ("Null modem",
     "A specially wired cable that connects two DTE devices, a configuration RS-232 was never "
     "designed for."),
    ("DTE / DCE",
     "Data terminal equipment (computer, instrument) and data communication equipment (modem). "
     "RS-232 assumes one of each."),
    ("Real-time",
     "Operation in which every task must complete within a specified and predictable interval."),
]

_FURTHER_VI = [
    "J. Di Giacomo, Ed., <i>Digital Bus Handbook</i>, New York: McGraw-Hill, 1990. — Khảo sát "
    "so sánh các chuẩn bus công nghiệp, kể cả những chuẩn chỉ được nhắc tên trong chương này.",
    "T. Shanley and D. Anderson, <i>ISA System Architecture</i>, 3rd ed., Reading, MA: "
    "Addison-Wesley, 1995. — Chi tiết về bus ISA, chu trình bus và các trạng thái chờ.",
    "T. Shanley and D. Anderson, <i>PCMCIA System Architecture</i>, 2nd ed., Reading, MA: "
    "Addison-Wesley, 1995. — Cấu trúc thông tin thẻ, dịch vụ thẻ và dịch vụ ổ cắm.",
    "M. D. Seyer, <i>RS232 Made Easy</i>, Englewood Cliffs, NJ: Prentice-Hall, 1984. — Nguồn "
    "tham khảo mà chính chương này dẫn cho các sơ đồ null modem và định nghĩa các chữ viết tắt.",
    "IEEE Std 488.2-1987, <i>IEEE Standard Codes, Formats, Protocols and Common Commands</i>. — "
    "Phần bổ sung cho 488.1 về cú pháp và các lệnh thông dụng.",
]

_FURTHER_EN = [
    "J. Di Giacomo, Ed., <i>Digital Bus Handbook</i>, New York: McGraw-Hill, 1990. — A "
    "comparative survey of industrial bus standards, including those only named in this "
    "chapter.",
    "T. Shanley and D. Anderson, <i>ISA System Architecture</i>, 3rd ed., Reading, MA: "
    "Addison-Wesley, 1995. — Detail on the ISA bus, bus cycles and wait states.",
    "T. Shanley and D. Anderson, <i>PCMCIA System Architecture</i>, 2nd ed., Reading, MA: "
    "Addison-Wesley, 1995. — Card information structure, card services and socket services.",
    "M. D. Seyer, <i>RS232 Made Easy</i>, Englewood Cliffs, NJ: Prentice-Hall, 1984. — The "
    "reference this chapter cites for the null-modem schemes and the mnemonic definitions.",
    "IEEE Std 488.2-1987, <i>IEEE Standard Codes, Formats, Protocols and Common Commands</i>. — "
    "The syntax and common-command companion to 488.1.",
]


# ================================================================ BUILD
def build(lang):
    vi = lang == "vi"
    switch = ("%s%s/" % (BASE_EN, CSLUG)) if vi else ("%s%s/" % (BASE_VI, CSLUG))
    title = ("Chương 86 — %s · Sổ tay Đo lường, Thiết bị đo và Cảm biến" % TITLE_VI if vi
             else "Chapter 86 — %s · Measurement, Instrumentation and Sensors Handbook"
                  % TITLE_EN)
    desc = ("Bản dịch tiếng Việt Chương 86 “Máy tính” của A. M. MacLeod, P. F. Martin và "
            "W. A. Gillespie — máy tính một bảng mạch, kiến trúc bus, VMEbus và Multibus II, "
            "các bus PC (ISA, EISA, PCMCIA, PC/104), thiết bị ngoại vi trong và ngoài, null "
            "modem, và phần mềm cho hệ đo lường, với 7 hình và 6 bảng." if vi
            else
            "Companion to Chapter 86 of the CRC Measurement Handbook — single-board computers, "
            "bus architectures, VMEbus and Multibus II, the PC buses (ISA, EISA, PCMCIA, "
            "PC/104), internal and external peripherals, null modems, and instrumentation "
            "software, with 7 figures and 6 tables.")
    crumb = ('<a href="/vi/books/">Sách</a> · <a href="%s">Sổ tay Đo lường, Thiết bị đo và Cảm '
             'biến</a> · Chương 86' % BASE_VI if vi else
             '<a href="/books/">Books</a> · <a href="%s">Measurement, Instrumentation and Sensors '
             'Handbook</a> · Chapter 86' % BASE_EN)
    meta = ("Chương 86 · theo Ch86.pdf (CRC Press, 1999) · 7 hình, 6 bảng" if vi
            else "Chapter 86 · 7 figures, 6 tables")
    body = ('<main><article class="intranet-content reader"><div class="reader-hero">'
            '<div class="breadcrumb">%s</div><h1>%s</h1><p class="byline">%s</p>'
            '<div class="meta-line">%s</div></div><div class="prose">%s</div>%s</article></main>'
            % (crumb, TITLE_VI if vi else TITLE_EN, BYLINE if vi else BYLINE_EN, meta,
               body_vi() if vi else body_en(), chapter_nav(lang, 86)))
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
