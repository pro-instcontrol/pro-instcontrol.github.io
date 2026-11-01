# -*- coding: utf-8 -*-
"""Handbook Chapter 28 — Flow Measurement
(Richard Thorn — University of Derby; Adrian Melling, Herbert Köchner,
Reinhard Haak — Universität Erlangen-Nürnberg; Zaki D. Husain,
Donald J. Wass — Daniel Flow Products; David Wadlow — Sensors Research
Consulting; Harold M. Miller — Data Industrial; Halit Eren — Curtin
University of Technology; Hans-Peter Vaterlaus).

The largest chapter in the handbook: 132 source pages, eleven sections,
92 figures, 162 equations and 23 tables. It is translated section by section;
each section is a pair of functions (sec_NN_vi / sec_NN_en) appended to the
two body builders at the bottom, so a later session can add a section without
touching the ones already written.

Run:  python build/reader_hb_ch28.py
"""
import os

import hb28fig as F
from reader_handbook import SLUG, head, header, footer
from chapter_nav import nav as chapter_nav

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSLUG = "ch28-flow-measurement"
TITLE_EN = "Flow Measurement"
TITLE_VI = "Đo lưu lượng"
BYLINE = ("Richard Thorn (University of Derby) · Adrian Melling · Herbert Köchner · "
          "Reinhard Haak (Universität Erlangen-Nürnberg) · Zaki D. Husain · "
          "Donald J. Wass (Daniel Flow Products) · David Wadlow (Sensors Research "
          "Consulting) · Harold M. Miller (Data Industrial) · Halit Eren (Curtin "
          "University of Technology) · Hans-Peter Vaterlaus")
BASE_EN = "/books/read/%s/" % SLUG
BASE_VI = "/vi/books/read/%s/" % SLUG
PREV_EN = "ch27-acoustic-measurement"
PREV_VI = "ch27-acoustic-measurement"
PREV_T_EN = "Acoustic Measurement"
PREV_T_VI = "Đo âm học"


def fig(num, key, lang="vi"):
    svg, cap_vi, cap_en, _av, _ae = key
    cap = cap_vi if lang == "vi" else cap_en
    return ('<figure class="figure" id="fig-28-%d">%s<figcaption class="figcap">%s</figcaption></figure>'
            % (num, svg, cap))


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


def wl(items):
    return ('<p style="font-size:.92rem;color:#333;line-height:1.8;margin:-.3rem 0 1.2rem">'
            + "<br>".join(items) + "</p>")


def defs(items):
    """Defining-terms block. Rendered as a two-column table so it inherits the
    reader's existing .tbl styling — there is no .deflist rule in library.css."""
    rows = "".join('<tr><th scope="row" style="text-align:left;width:30%%">%s</th><td>%s</td></tr>'
                   % (k, v) for k, v in items)
    return ('<div class="table-wrap"><table class="tbl"><tbody>%s</tbody></table></div>' % rows)


def table(hd, rows, cap, cls="tbl"):
    body = "".join("<tr>%s</tr>" % "".join("<td>%s</td>" % c for c in r) for r in rows)
    return ('<div class="table-wrap"><table class="%s"><thead><tr>%s</tr></thead><tbody>%s</tbody></table></div>'
            '<p style="font-size:.84rem;color:#888;font-style:italic">%s</p>'
            % (cls, "".join("<th>%s</th>" % h for h in hd), body, cap))


def h4(t, en=""):
    """Sub-heading one level below h3. There is no .prose h4 rule in library.css,
    so the size and spacing are set inline to sit between h3 and body text."""
    return ('<h4 style="font-size:1rem;font-weight:700;margin:1.7rem 0 .5rem">%s%s</h4>'
            % (t, (' <span class="en">%s</span>' % en) if en else ""))


def ul(items):
    return ('<ul style="margin:-.2rem 0 1.3rem">%s</ul>'
            % "".join("<li>%s</li>" % i for i in items))


# ================================================================ table data

def _t281(lang):
    """Table 28.1 — transposed so eleven columns become four."""
    if lang == "vi":
        hd = ("Chỉ tiêu", "Tấm orifice", "Ống Venturi", "Vòi phun")
        cap = ("Bảng 28.1 · Tính năng và phạm vi ứng dụng của các lưu lượng kế chênh áp thông dụng. "
               "Độ chính xác là số liệu khi chưa hiệu chuẩn; hiệu chuẩn tại chỗ sau khi lắp có thể "
               "cải thiện đáng kể.")
        rows = [
            ["Độ chính xác điển hình (chưa hiệu chuẩn)", "±2 %", "±2 %", "±2 %"],
            ["Dải đo điển hình", "3:1", "3:1", "3:1"],
            ["Đường kính ống điển hình (mm)", "10–1000", "25–500", "25–250"],
            ["Tổn thất áp suất vĩnh viễn", "Cao", "Thấp", "Cao"],
            ["Giá thành tương đối", "Thấp", "Cao", "Trung bình"],
            ["Khí sạch", "Có", "Có", "Có"],
            ["Khí bẩn", "Không", "Có thể", "Có thể"],
            ["Chất lỏng sạch", "Có", "Có", "Có"],
            ["Bùn / huyền phù", "Không", "Có thể", "Không"],
            ["Hơi nước", "Có", "Có thể", "Có"],
        ]
    else:
        hd = ("Performance", "Orifice plate", "Venturi tube", "Nozzle")
        cap = ("Table 28.1 · Performance and application areas of the common differential pressure "
               "flowmeters. Accuracy figures are uncalibrated; calibrating in place after "
               "installation improves them substantially.")
        rows = [
            ["Typical uncalibrated accuracy", "±2 %", "±2 %", "±2 %"],
            ["Typical range", "3:1", "3:1", "3:1"],
            ["Typical pipe diameter (mm)", "10–1000", "25–500", "25–250"],
            ["Permanent pressure loss", "High", "Low", "High"],
            ["Comparative cost", "Low", "High", "Medium"],
            ["Clean gas", "Yes", "Yes", "Yes"],
            ["Dirty gas", "No", "Maybe", "Maybe"],
            ["Clean liquid", "Yes", "Yes", "Yes"],
            ["Slurry", "No", "Maybe", "No"],
            ["Steam", "Yes", "Maybe", "Yes"],
        ]
    return hd, rows, cap


def _t282(lang):
    if lang == "vi":
        hd = ("Công ty", "Địa chỉ · điện thoại")
        cap = "Bảng 28.2 · Một số hãng cung cấp lưu lượng kế chênh áp."
        rows = [
            ["ABB Kent-Taylor", "Oldens Lane, Stonehouse, Gloucestershire GL10 3TA, Anh · "
             "+44 1453 826661 · fax +44 1453 826358"],
            ["Daniel Industries Inc.", "9720 Katy Road, P.O. Box 19097, Houston, TX 77224 · "
             "(713) 467-6000 · fax (713) 827-3880"],
            ["Hartmann &amp; Braun (UK) Ltd.", "Bush Beach Engineering Division, Stanley Green "
             "Trading Estate, Cheadle Hulme, Cheshire SK8 6RN, Anh · +44 161 4858151"],
            ["ISA Controls Ltd.", "Hackworth Industrial Park, Shildon, County Durham DL4 1LH, "
             "Anh · +44 1388 773065"],
            ["Perry Equipment Corporation", "Wolters Industrial Park, P.O. Box 640, Mineral "
             "Wells, TX 76067 · (817) 325-2575"],
        ]
    else:
        hd = ("Company", "Address · telephone")
        cap = "Table 28.2 · A selection of companies that supply differential pressure flowmeters."
        rows = [
            ["ABB Kent-Taylor", "Oldens Lane, Stonehouse, Gloucestershire GL10 3TA, England · "
             "+44 1453 826661 · fax +44 1453 826358"],
            ["Daniel Industries Inc.", "9720 Katy Road, P.O. Box 19097, Houston, TX 77224 · "
             "(713) 467-6000 · fax (713) 827-3880"],
            ["Hartmann &amp; Braun (UK) Ltd.", "Bush Beach Engineering Division, Stanley Green "
             "Trading Estate, Cheadle Hulme, Cheshire SK8 6RN, England · +44 161 4858151"],
            ["ISA Controls Ltd.", "Hackworth Industrial Park, Shildon, County Durham DL4 1LH, "
             "England · +44 1388 773065"],
            ["Perry Equipment Corporation", "Wolters Industrial Park, P.O. Box 640, Mineral "
             "Wells, TX 76067 · (817) 325-2575"],
        ]
    return hd, rows, cap


def _t283(lang):
    if lang == "vi":
        hd = ("Tỉ số đường kính β", "Một cút 90°", "Hai cút 90° cùng mặt phẳng",
              "Hai cút 90° khác mặt phẳng", "Van cầu mở hoàn toàn", "Hạ lưu lưu lượng kế")
        cap = ("Bảng 28.3 · Chiều dài ống thẳng tối thiểu cần có giữa các phụ kiện và tấm orifice "
               "hoặc ống Venturi (theo ISO 5167-1) để bảo đảm mặt cắt đo có phân bố dòng chảy phát "
               "triển đầy đủ. Mọi giá trị là bội số của đường kính ống.")
    else:
        hd = ("Diameter ratio β", "Single 90° bend", "Two 90° bends, same plane",
              "Two 90° bends, different planes", "Globe valve fully open",
              "Downstream of the flowmeter")
        cap = ("Table 28.3 · Minimum straight lengths of pipe required between various fittings and "
               "an orifice plate or Venturi tube (as recommended in ISO 5167-1) so that a fully "
               "developed flow profile exists in the measurement section. All lengths are multiples "
               "of the pipe diameter.")
    rows = [["0.2", "10", "14", "34", "18", "4"],
            ["0.4", "14", "18", "36", "20", "6"],
            ["0.6", "18", "26", "48", "26", "7"],
            ["0.8", "46", "50", "80", "44", "8"]]
    return hd, rows, cap


def _t284(lang):
    if lang == "vi":
        hd = ("Tổ chức", "Tiêu chuẩn", "Nội dung")
        cap = "Bảng 28.4 · Các tiêu chuẩn liên quan đến đo lưu lượng bằng chênh áp."
        rows = [
            ["ANSI (New York)", "ANSI/ASHRAE 41.8",
             "Phương pháp đo lưu lượng chất lỏng trong ống bằng lưu lượng kế orifice"],
            ["ANSI (New York)", "ANSI/ASME MFC-7M", "Đo lưu lượng khí bằng vòi phun Venturi tới hạn"],
            ["ANSI (New York)", "ANSI/ASME MFC-14M", "Đo lưu lượng bằng lưu lượng kế orifice nhỏ, chính xác"],
            ["API (Washington)", "API 2530",
             "Sổ tay tiêu chuẩn đo dầu khí, Ch. 14 §3 — đo khí thiên nhiên bằng orifice"],
            ["ASME (New York)", "ASME MFC-3M", "Đo lưu lượng trong ống bằng orifice, vòi phun và Venturi"],
            ["ASME (New York)", "ASME MFC-8M",
             "Dòng chảy trong ống kín — đấu nối truyền tín hiệu áp giữa thiết bị sơ cấp và thứ cấp"],
            ["BSI (London)", "BS 1042", "Đo lưu lượng chất lưu trong ống kín"],
            ["ISO (Genève)", "ISO 2186", "Đấu nối truyền áp giữa phần tử sơ cấp và thứ cấp"],
            ["ISO (Genève)", "ISO TR 3313", "Đo dòng chảy dao động bằng orifice, vòi phun hoặc Venturi"],
            ["ISO (Genève)", "ISO 5167-1", "Đo lưu lượng bằng các thiết bị chênh áp"],
            ["ISO (Genève)", "ISO 9300", "Đo lưu lượng khí bằng vòi phun Venturi tới hạn"],
        ]
    else:
        hd = ("Body", "Standard", "Scope")
        cap = "Table 28.4 · Standards related to differential pressure flow measurement."
        rows = [
            ["ANSI (New York)", "ANSI/ASHRAE 41.8",
             "Standard methods of measurement of flow of liquids in pipes using orifice flowmeters"],
            ["ANSI (New York)", "ANSI/ASME MFC-7M", "Measurement of gas flow by critical flow Venturi nozzles"],
            ["ANSI (New York)", "ANSI/ASME MFC-14M", "Measurement of fluid flow using small bore precision orifice meters"],
            ["API (Washington)", "API 2530",
             "Manual of Petroleum Measurement Standards, Ch. 14 §3 — orifice metering of natural gas"],
            ["ASME (New York)", "ASME MFC-3M", "Measurement of fluid flow in pipes using orifice, nozzle and Venturi"],
            ["ASME (New York)", "ASME MFC-8M",
             "Fluid flow in closed conduits — connections for pressure signal transmission"],
            ["BSI (London)", "BS 1042", "Measurement of fluid flow in closed conduits"],
            ["ISO (Genève)", "ISO 2186", "Connections for pressure transmission between primary and secondary elements"],
            ["ISO (Genève)", "ISO TR 3313", "Measurement of pulsating fluid flow by orifice plates, nozzles or Venturi tubes"],
            ["ISO (Genève)", "ISO 5167-1", "Measurement of fluid flow by means of pressure differential devices"],
            ["ISO (Genève)", "ISO 9300", "Measurement of gas flow by means of critical flow Venturi nozzles"],
        ]
    return hd, rows, cap


def _t285(lang):
    """Table 28.5 — rotameter prices. The plastic column is empty for metal meters."""
    if lang == "vi":
        hd = ("Loại", "Cỡ", "Giá (nhựa)", "Giá (thép không gỉ, thuỷ tinh borosilicat)")
        cap = ("Bảng 28.5 · Giá tham khảo của rotameter (USD, khoảng năm 1998). Cột “nhựa” để "
               "trống ở các cỡ kim loại vì loại này chỉ có bản kim loại.")
        rows = [
            ["Thuỷ tinh", "&lt; 1/2 in. (12,7 mm)", "50 $", "200 $"],
            ["Nhựa", "1/2 in. (12,7 mm)", "50 $", "200 $"],
            ["Nhựa", "1 in. (25,4 mm)", "70 $", "150 $"],
            ["Nhựa", "2 in. (50,8 mm)", "200 $", "500 $"],
            ["Kim loại", "1/2 in. (12,7 mm)", "—", "500 $"],
            ["Kim loại", "1 in. (25,4 mm)", "—", "600 $"],
            ["Kim loại", "2 in. (50,8 mm)", "—", "700 $"],
            ["Kim loại", "3 in. (76,2 mm)", "—", "1 100 $"],
            ["Kim loại", "4 in. (101,6 mm)", "—", "1 400 $"],
            ["<i>Phụ thêm</i>", "Công tắc giới hạn điện", "—", "100 $"],
            ["<i>Phụ thêm</i>", "Bộ chuyển đổi dòng điện", "—", "500 $"],
            ["<i>Phụ thêm</i>", "Truyền tín hiệu khí nén", "—", "1 200 $"],
        ]
    else:
        hd = ("Type", "Size", "Price (plastic)", "Price (stainless steel, borosilicate glass)")
        cap = ("Table 28.5 · Approximate rotameter prices (US$, circa 1998). The plastic column is "
               "empty for the metal sizes, which are supplied in metal only.")
        rows = [
            ["Glass", "&lt; 1/2 in. (12.7 mm)", "$50", "$200"],
            ["Plastic", "1/2 in. (12.7 mm)", "$50", "$200"],
            ["Plastic", "1 in. (25.4 mm)", "$70", "$150"],
            ["Plastic", "2 in. (50.8 mm)", "$200", "$500"],
            ["Metal", "1/2 in. (12.7 mm)", "—", "$500"],
            ["Metal", "1 in. (25.4 mm)", "—", "$600"],
            ["Metal", "2 in. (50.8 mm)", "—", "$700"],
            ["Metal", "3 in. (76.2 mm)", "—", "$1100"],
            ["Metal", "4 in. (101.6 mm)", "—", "$1400"],
            ["<i>Extras</i>", "Electric limit switch", "—", "$100"],
            ["<i>Extras</i>", "Current transducer", "—", "$500"],
            ["<i>Extras</i>", "Pneumatic transmitter", "—", "$1200"],
        ]
    return hd, rows, cap


def _t286(lang):
    if lang == "vi":
        hd = ("Loại", "Giá")
        cap = ("Bảng 28.6 · Giá tham khảo của lưu lượng kế cánh quay (USD, khoảng năm 1998). "
               "Bản có kim chỉ nối trực tiếp đã bao gồm công tắc lưu lượng điện.")
        rows = [
            ["Bản nhựa (cỡ nhỏ)", "từ 10 $"],
            ["Bản kim chỉ nối trực tiếp, kèm công tắc lưu lượng điện: kim loại, đầu nối ren "
             "1/2 in. (12,7 mm) đến 2 in. (50,8 mm)",
             "400 $ (đồng thau) đến 600 $ (thép không gỉ)"],
            ["Bản mặt bích", "cộng thêm 200 $ (1/2 in., 12,7 mm) đến 400 $ (2 in., 50,8 mm)"],
            ["Chỉ thị ghép từ, thép không gỉ", "1 200 $ (1/2 in., 12,7 mm) đến 2 100 $ (8 in., 203 mm)"],
        ]
    else:
        hd = ("Type", "Price")
        cap = ("Table 28.6 · Approximate movable vane meter prices (US$, circa 1998). The direct "
               "coupled pointer version includes an electric flow switch.")
        rows = [
            ["Plastic versions (small scale)", "From $10"],
            ["Direct coupled pointer versions incl. electric flow switch: metal, screw connections "
             "1/2 in. (12.7 mm) to 2 in. (50.8 mm)",
             "$400 (brass) to $600 (stainless steel)"],
            ["Flanged versions", "Add $200 (1/2 in., 12.7 mm) to $400 (2 in., 50.8 mm)"],
            ["Magnetic coupled indicator, stainless steel", "$1200 (1/2 in., 12.7 mm) to $2100 (8 in., 203 mm)"],
        ]
    return hd, rows, cap


def _t287(lang):
    if lang == "vi":
        hd = ("Công ty", "Địa chỉ · điện thoại")
        cap = "Bảng 28.7 · Các hãng chế tạo rotameter và lưu lượng kế cánh quay."
    else:
        hd = ("Company", "Address · telephone")
        cap = "Table 28.7 · Manufacturers of rotameters and movable vane meters."
    rows = [
        ["Tokyo Keiso Co. Ltd.", "Shiba Toho Building, 1-7-24 Shibakoen, Minato-ku, Tokyo 105, "
         "Nhật Bản · +81-3-3431-1625 · fax +81-3-3433-4922"],
        ["Brooks Instrument Division, Emerson Electric", "407 W. Vine St., Hatfield, PA 19440, "
         "Hoa Kỳ · (215) 362-3500 · fax (215) 362-3745"],
        ["Krohne America Inc.", "7 Dearborn Rd., Peabody, MA 01960, Hoa Kỳ · (508) 535-6060, "
         "(800) 356-9464 · fax (508) 535-1720"],
        ["Bailey Fischer &amp; Porter Co.", "County Line Rd., Warminster, PA 18974, Hoa Kỳ · "
         "(215) 674-6000 · fax (215) 674-7183"],
        ["Bopp &amp; Reuther Heinrichs Messtechnik GmbH", "Stolberger Str. 393, D-50933 Köln, "
         "Đức · +49-221-49708-0 · fax +49-221-497088"],
        ["Porter Instruments Co.", "245 Township Line Road, Hatfield, PA 19440, Hoa Kỳ · "
         "(215) 723-4000 · fax (215) 723-2199"],
        ["Wallace &amp; Tiernan, Inc.", "25 Main St., Belleville, NJ 07109, Hoa Kỳ · "
         "(201) 759-8000 · fax (201) 759-9333"],
        ["KDG-Mobrey Ltd.", "Crompton Way, Crawley, West Sussex RH10 2YZ, Anh · "
         "+44-1293-518632 · fax +44-1293-533095"],
        ["CT Platon", "Jays Close, Viables, Basingstoke, Hampshire RG22 4BS, Anh · "
         "+44-1256-470456 · fax +44-1256-363345"],
        ["Kobold Messring GmbH", "Nordring 22-24, D-65719 Hofheim/Taunus, Đức · "
         "+49 6192 2990 · fax +49 6192 23398"],
        ["Rota Yokogawa GmbH &amp; Co. KG", "Rheinstrasse 8, D-79664 Wehr, Đức · "
         "+49-7761-567-0 · fax +49-7761-567-126"],
    ]
    if lang != "vi":
        rows = [[a, b.replace("Nhật Bản", "Japan").replace("Hoa Kỳ", "USA").replace("Đức", "Germany")
                 .replace(", Anh ·", ", England ·")] for a, b in rows]
    return hd, rows, cap


# ================================================================ 28.1

def sec_28_1_vi():
    b = []
    b.append(h2("28.1 Lưu lượng kế chênh áp", "Differential Pressure Flowmeters"))
    b.append(p("Richard Thorn — Đại học Derby."))
    b.append(p(
        "Đo lưu lượng là việc xảy ra hằng ngày. Từ việc đổ xăng cho ô tô đến việc biết vòi phun "
        "trong vườn đang tiêu bao nhiêu nước, đều cần một lưu lượng kế. Cũng khó hình dung một "
        "ngành công nghiệp nào mà ở đó lưu lượng kế không đóng vai trò nào. Thị trường lưu lượng kế "
        "thế giới được ước khoảng 2.500 triệu USD năm 1995 và dự kiến còn tăng đều trong thời gian "
        "tới. Giá trị sản phẩm được đo bằng các thiết bị này cũng rất lớn: chỉ riêng ở Anh, năm "
        "1994, giá trị dầu thô khai thác ước khoảng 15 tỷ USD."))
    b.append(p(
        "Với quy mô thị trường và giá trị sản phẩm như vậy, khá ngạc nhiên là độ chính xác và năng "
        "lực của nhiều lưu lượng kế lại kém so với các thiết bị đo những biến quá trình thông dụng "
        "khác như áp suất và nhiệt độ. Ví dụ, lưu lượng kế tấm orifice — được dùng thương mại từ đầu "
        "những năm 1900 và có độ chính xác điển hình ±2 % giá trị đọc — vẫn là loại duy nhất được "
        "hầu hết các nước cho phép dùng để đo đối chiếu tài chính khí thiên nhiên. Dù những kỹ thuật "
        "mới như lưu lượng kế Coriolis ngày càng phổ biến, ngành đo lưu lượng vốn bảo thủ và vẫn bị "
        "chi phối bởi các kỹ thuật truyền thống; xem [1] để có tổng quan về phát triển gần đây."))
    b.append(p(
        "Hơn 40 % mọi phép đo chất lỏng, khí và hơi trong công nghiệp vẫn được thực hiện bằng các "
        "loại <b>lưu lượng kế chênh áp</b> thông dụng, tức tấm orifice, ống Venturi và vòi phun. "
        "Nguyên lý của chúng dựa trên quan sát của Bernoulli: nếu đặt một chỗ thắt hình vành khuyên "
        "trong đường ống thì vận tốc chất lưu qua chỗ thắt tăng lên; vận tốc tăng làm áp suất tĩnh "
        "tại tiết diện đó giảm xuống, tạo ra chênh áp hai bên phần tử. Chênh lệch giữa áp suất thượng "
        "lưu và hạ lưu của vật cản này liên hệ với lưu lượng chất lưu qua chỗ thắt, và do đó qua "
        "đường ống. Một lưu lượng kế chênh áp gồm hai phần tử cơ bản: một vật cản gây sụt áp "
        "(<b>phần tử tạo chênh áp</b>) và một cách đo sụt áp đó (<b>đầu dò chênh áp</b>)."))
    b.append(p(
        "Một ưu điểm lớn của tấm orifice, ống Venturi hay vòi phun là có thể dự báo độ bất định của "
        "phép đo mà không cần hiệu chuẩn, miễn là thiết bị được chế tạo và lắp đặt theo một trong các "
        "tiêu chuẩn quốc tế áp dụng cho chúng. Ngoài ra loại lưu lượng kế này đơn giản, không có bộ "
        "phận chuyển động nên đáng tin cậy. Nhược điểm chính là dải đo hẹp (điển hình 3:1), tổn thất "
        "áp suất vĩnh viễn trên đường ống (có thể làm tăng chi phí bơm), và nhạy với ảnh hưởng lắp "
        "đặt (có thể giảm thiểu bằng các đoạn ống thẳng trước và sau lưu lượng kế). Tổng hợp các ưu "
        "điểm này vẫn rất khó vượt qua; tuy còn hạn chế nhưng chúng đã được nghiên cứu kỹ và trong "
        "phần lớn tình huống có thể bù được. Trừ khi cần độ chính xác rất cao hoặc ứng dụng buộc "
        "phải dùng thiết bị không xâm nhập, lưu lượng kế chênh áp vẫn nên được xem xét. Bất chấp "
        "những dự báo về sự cáo chung, chắc chắn nó còn là phương pháp đo lưu lượng phổ biến trong "
        "nhiều năm nữa."))

    b.append(h3("Nguyên lý quan trọng của dòng chảy trong ống", "Important Principles of Fluid Flow in Pipes"))
    b.append(p(
        "Có một số nguyên lý cần hiểu trước khi dùng lưu lượng kế chênh áp một cách tin cậy: phân "
        "biệt chảy tầng và chảy rối, ý nghĩa của số Reynolds, và tầm quan trọng của mặt cắt phân bố "
        "vận tốc."))
    b.append(p(
        "Chuyển động của chất lưu trong ống có thể xếp vào ba loại: chảy tầng, chảy quá độ và chảy "
        "rối. Trong <b>chảy tầng</b>, chất lưu di chuyển thành các lớp song song (gọi là đường dòng) "
        "không trộn vào nhau khi đi theo chiều dòng. Nếu chảy rối, chất lưu không đi thành lớp song "
        "song mà chuyển động hỗn loạn, chỉ có chuyển động trung bình là song song với trục ống. Nếu "
        "chảy <b>quá độ</b> thì cả hai loại có thể cùng tồn tại ở những điểm khác nhau trên tuyến, "
        "hoặc dòng có thể chuyển đổi qua lại giữa hai loại."))
    b.append(p(
        "Năm 1883, Osborne Reynolds thực hiện một loạt thí nghiệm kinh điển tại Đại học Manchester, "
        "chứng minh rằng đặc tính dòng chảy dự báo được bằng một số không thứ nguyên, nay gọi là số "
        "Reynolds. Số Reynolds Re là tỉ số giữa lực quán tính trong dòng (ρ v̄ D) và lực nhớt (η):"))
    b.append(eq("Re = ρ v̄ D ⁄ η", "28.1"))
    b.append(p(
        "trong đó ρ là khối lượng riêng của chất lưu, v̄ là vận tốc trung bình, <i>D</i> là đường "
        "kính ống và η là độ nhớt động lực của chất lưu."))
    b.append(p(
        "Nếu Re nhỏ hơn 2000, lực nhớt chiếm ưu thế và dòng là chảy tầng. Nếu Re lớn hơn 4000, lực "
        "quán tính chiếm ưu thế và dòng là chảy rối. Nếu Re nằm giữa 2000 và 4000, dòng là quá độ và "
        "có thể ở một trong hai chế độ. Số Reynolds chủ yếu tính từ tính chất chất lưu, không kể đến "
        "các yếu tố như độ nhám ống, cút và van — những thứ cũng ảnh hưởng tới đặc tính dòng. Tuy "
        "vậy, nó vẫn là chỉ dẫn tốt cho loại dòng có thể gặp trong hầu hết tình huống."))
    b.append(p(
        "Vận tốc chất lưu trên một mặt cắt ống không hằng số mà phụ thuộc loại dòng. Trong chảy tầng, "
        "mặt cắt vận tốc là parabol vì lực nhớt lớn làm chất lưu đi chậm hơn gần thành ống; khi đó "
        "vận tốc ở tâm ống gấp đôi vận tốc trung bình trên mặt cắt. Mặt cắt chảy tầng không phụ thuộc "
        "độ nhám thành ống. Trong chảy rối, lực quán tính chiếm ưu thế, ảnh hưởng thành ống ít hơn và "
        "mặt cắt vận tốc phẳng hơn, với vận tốc ở tâm khoảng 1,2 lần vận tốc trung bình. Mặt cắt "
        "chính xác của dòng rối phụ thuộc độ nhám thành ống và số Reynolds."))
    b.append(fig(1, F.fig(1), "vi"))
    b.append(p(
        "Hình 28.1 cho mặt cắt dòng “phát triển đầy đủ” của chảy tầng và chảy rối — tức mặt cắt thu "
        "được ở cuối một ống rất dài, khi mọi thay đổi do cút và phụ kiện đã không còn. Để tin được "
        "vào tính năng của lưu lượng kế chênh áp, cả đặc tính lẫn mặt cắt vận tốc của dòng qua lưu "
        "lượng kế đều phải ổn định và đã biết."))

    b.append(h3("Phương trình Bernoulli", "Bernoulli’s Equation"))
    b.append(p(
        "Phương trình Bernoulli xác lập quan hệ giữa vận tốc <i>v</i>, áp suất <i>p</i> và độ cao "
        "<i>h</i> so với một mốc cố định của chất lưu chảy qua ống có tiết diện thay đổi, và là điểm "
        "xuất phát để hiểu nguyên lý lưu lượng kế chênh áp. Với ống thuôn, đặt nghiêng như Hình "
        "28.2, phương trình Bernoulli phát biểu:"))
    b.append(eq("p₁ ⁄ (ρg) + v₁² ⁄ (2g) + h₁ = p₂ ⁄ (ρg) + v₂² ⁄ (2g) + h₂", "28.2"))
    b.append(p(
        "Như vậy tổng của cột áp (<i>p</i>/ρ<i>g</i>), cột vận tốc (<i>v</i>/2<i>g</i>) và cột vị trí "
        "(<i>h</i>) là hằng số dọc theo một đường dòng. Thuật ngữ “cột” được dùng phổ biến vì mỗi số "
        "hạng đều có đơn vị mét. Phương trình 28.2 giả thiết chất lưu không ma sát (độ nhớt bằng 0) "
        "và có khối lượng riêng không đổi (không nén được). Chi tiết về cách suy ra và ý nghĩa của "
        "phương trình Bernoulli có trong hầu hết sách giáo trình cơ học chất lưu đại học (ví dụ [2])."))
    b.append(fig(2, F.fig(2), "vi"))
    b.append(p(
        "Phương trình Bernoulli dùng được để chỉ ra cách một chỗ thắt trong ống đo lưu lượng. Xét "
        "đoạn ống ở Hình 28.3. Vì ống nằm ngang nên <i>h</i>₁ = <i>h</i>₂, và phương trình 28.2 rút "
        "gọn thành:"))
    b.append(eq("(p₁ − p₂) ⁄ ρ = (v₂² − v₁²) ⁄ 2", "28.3"))
    b.append(p("Nguyên lý bảo toàn khối lượng đòi hỏi:"))
    b.append(eq("v₁ A₁ ρ = v₂ A₂ ρ", "28.4"))
    b.append(p("Sắp xếp lại 28.4 và thay <i>v</i>₂ vào 28.3, ta được:"))
    b.append(eq("Q = v₁ A₁ = [A₂ ⁄ √(1 − (A₂ ⁄ A₁)²)] · √(2(p₁ − p₂) ⁄ ρ)", "28.5"))
    b.append(fig(3, F.fig(3), "vi"))
    b.append(p(
        "Điều này cho thấy lưu lượng thể tích <i>Q</i> xác định được bằng cách đo độ giảm áp "
        "(<i>p</i>₁ − <i>p</i>₂) qua chỗ thắt trên đường ống — nguyên lý cơ bản của mọi lưu lượng kế "
        "chênh áp. Phương trình 28.5 có các hạn chế: nó giả thiết chất lưu không nén được (hợp lý với "
        "hầu hết chất lỏng) và không có độ nhớt (cho mặt cắt vận tốc phẳng). Những giả thiết này phải "
        "được bù khi dùng 28.5 cho đo lưu lượng thực tế."))

    b.append(h3("Các lưu lượng kế chênh áp thông dụng", "Common Differential Pressure Flowmeters"))
    b.append(h3("Tấm orifice", "The Orifice Plate"))
    b.append(p(
        "Tấm orifice là loại lưu lượng kế chênh áp đơn giản và rẻ nhất. Nó chỉ là một tấm có khoan "
        "lỗ với kích thước và vị trí xác định, kẹp giữa hai mặt bích trên đường ống (Hình 28.4). "
        "Vận tốc chất lưu tăng khi qua lỗ làm phát sinh sụt áp hai bên tấm. Sau khi qua chỗ thắt, "
        "dòng còn co tiếp cho tới một đường kính nhỏ nhất gọi là vena contracta."))
    b.append(fig(4, F.fig(4), "vi"))
    b.append(p(
        "Nếu dùng 28.5 để tính lưu lượng từ độ sụt áp đo được trên tấm orifice thì sẽ có sai số, vì "
        "<i>A</i>₂ đúng ra phải là diện tích vena contracta — đại lượng dĩ nhiên chưa biết. Ngoài ra "
        "rối giữa vena contracta và thành ống gây tổn thất năng lượng mà phương trình không kể đến."))
    b.append(p(
        "Để khắc phục các vấn đề khi áp dụng 28.5 vào thực tế, người ta thêm hai hệ số hiệu chỉnh xác "
        "định bằng thực nghiệm. Sau một vài biến đổi, 28.5 viết được thành:"))
    b.append(eq("Q = [C ⁄ √(1 − β⁴)] · ε · (π ⁄ 4) d² · √(2(p₁ − p₂) ⁄ ρ)", "28.6"))
    b.append(p(
        "trong đó ρ là khối lượng riêng của chất lưu thượng lưu tấm orifice, <i>d</i> là đường kính "
        "lỗ trên tấm, và β = <i>d</i>/<i>D</i> là tỉ số đường kính, với <i>D</i> là đường kính trong "
        "của ống thượng lưu."))
    b.append(p(
        "Hai hệ số thực nghiệm là <i>C</i> — hệ số lưu lượng — và ε — hệ số giãn nở. <i>C</i> chịu "
        "ảnh hưởng của tỉ số đường kính, số Reynolds, độ nhám ống, độ sắc của cạnh vào và vị trí lấy "
        "chênh áp; tuy vậy với hình học cố định, người ta đã chỉ ra rằng <i>C</i> chỉ phụ thuộc số "
        "Reynolds, nên xác định được cho từng ứng dụng. ε dùng để kể đến tính nén được của chất lưu. "
        "Cả <i>C</i> lẫn ε đều xác định được từ công thức và bảng trong các tài liệu được quốc tế "
        "công nhận, gọi là tiêu chuẩn. Các tiêu chuẩn này không chỉ quy định <i>C</i> và ε mà cả "
        "hình học và điều kiện lắp đặt của tấm orifice cạnh vuông, ống Venturi và vòi phun, và thực "
        "chất là cẩm nang thiết kế cho các loại lưu lượng kế chênh áp thông dụng nhất. Khuyến nghị "
        "lắp đặt nhằm bảo đảm trong tiết diện đo của lưu lượng kế tồn tại dòng rối phát triển đầy "
        "đủ. Tiêu chuẩn thông dụng ở châu Âu là ISO 5167-1 [3], còn ở Mỹ là API 2530 [4]. Giữa hai "
        "tiêu chuẩn có những khác biệt (ví dụ chiều dài tối thiểu của đoạn ống thẳng thượng lưu), "
        "nhưng đang có nỗ lực hài hoà chúng."))
    b.append(p(
        "Phương trình 28.6 cho thấy có lẽ ưu điểm lớn nhất của tấm orifice: có thể tin cậy dự báo "
        "tính năng đo mà không cần hiệu chuẩn, nếu thiết bị được chế tạo, lắp đặt và vận hành theo "
        "một tiêu chuẩn quốc tế. Ngoài ra thiết bị rẻ, không có bộ phận chuyển động, đáng tin cậy và "
        "dùng được cho hầu hết khí sạch, chất lỏng và hơi."))
    b.append(p(
        "Nhược điểm chính của tấm orifice là dải đo hẹp và nhạy với nhiễu loạn dòng. Vì lưu lượng tỉ "
        "lệ với căn bậc hai của chênh áp đo được, dải đo của một tổ hợp một tấm / một bộ truyền "
        "chênh áp chỉ khoảng 3:1. Tỉ số đường kính cần thiết (còn gọi là tỉ số beta) phụ thuộc lưu "
        "lượng cực đại cần đo và dải của đầu dò chênh áp sẵn có; việc chọn cỡ tấm orifice được trình "
        "bày trong hầu hết sách trong danh mục đọc thêm, và ngày nay có cả chương trình máy tính hỗ "
        "trợ. Có thể mở rộng dải đo bằng cách chuyển thang; các cách thực hiện được mô tả trong [5]. "
        "Phương trình 28.6 giả thiết mặt cắt dòng phát triển đầy đủ và ổn định, nên việc lắp đặt là "
        "then chốt, đặc biệt là đủ đoạn ống thẳng thượng lưu. Mòn cạnh vào của tấm có thể làm thay "
        "đổi nghiêm trọng độ chính xác, vì vậy thiết bị này thường chỉ dùng với chất lưu sạch."))
    b.append(p(
        "Chỉ một loại tấm orifice — loại cạnh vuông đồng tâm — được các tiêu chuẩn đề cập. Tuy vậy "
        "còn các loại khác, được thiết kế cho ứng dụng riêng. Một ví dụ là tấm orifice lệch tâm, "
        "thích hợp với chất lưu bẩn. Chi tiết các loại khác có trong [6]."))

    b.append(h3("Ống Venturi", "The Venturi Tube"))
    b.append(p(
        "Ống Venturi cổ điển (hay Herschel) là loại lưu lượng kế chênh áp lâu đời nhất, lần đầu dùng "
        "năm 1887. Như Hình 28.5, chỗ thắt được đưa vào dòng một cách từ từ hơn nhiều so với tấm "
        "orifice. Dòng qua ống Venturi vì thế gần với dự báo lý thuyết của 28.5 hơn, nên hệ số lưu "
        "lượng <i>C</i> gần 1 hơn nhiều, điển hình 0,95. Ngoài ra tổn thất áp suất vĩnh viễn của ống "
        "Venturi thấp hơn, nhưng chênh áp cũng thấp hơn so với tấm orifice cùng tỉ số đường kính. "
        "Thiết kế trơn nhẵn khiến ống Venturi ít nhạy với xói mòn hơn tấm orifice, do đó thích hợp "
        "hơn với khí hoặc chất lỏng bẩn. Nó cũng ít nhạy với nhiễu thượng lưu nên cần đoạn ống thẳng "
        "thượng lưu ngắn hơn tấm orifice hay vòi phun tương đương. Như với tấm orifice và vòi phun, "
        "thiết kế, lắp đặt và sử dụng ống Venturi được nhiều tiêu chuẩn quốc tế đề cập."))
    b.append(fig(5, F.fig(5), "vi"))
    b.append(p(
        "Nhược điểm chính của ống Venturi là kích thước và giá thành. Nó khó chế tạo hơn và do đó "
        "đắt hơn tấm orifice. Vì ống Venturi điển hình dài cỡ 6 đường kính, với cỡ ống lớn nó trở "
        "nên cồng kềnh, kéo theo việc duy trì các đoạn ống thượng và hạ lưu cũng thành vấn đề."))

    b.append(h3("Vòi phun", "The Nozzle"))
    b.append(p(
        "Vòi phun (Hình 28.6) kết hợp một số ưu điểm tốt nhất của tấm orifice và ống Venturi. Nó gọn, "
        "mà nhờ miệng vào cong lại có hệ số lưu lượng gần 1. Có nhiều kiểu vòi phun; loại thông dụng "
        "nhất ở châu Âu là vòi phun ISA-1932, còn ở Mỹ là vòi phun bán kính dài ASME. Cả hai đều "
        "được các tiêu chuẩn quốc tế đề cập."))
    b.append(fig(6, F.fig(6), "vi"))
    b.append(p(
        "Miệng vào trơn nhẵn khiến vòi phun đắt hơn tấm orifice vì độ cong của miệng vào thay đổi "
        "theo tỉ số đường kính, tuy vẫn rẻ hơn ống Venturi. Thiết bị không có cạnh sắc để bị xói mòn "
        "và làm lệch chuẩn, nên rất hợp với chất lưu bẩn và mài mòn. Vòi phun cũng thường dùng cho "
        "ứng dụng vận tốc cao, nhiệt độ cao như đo hơi nước."))
    b.append(p(
        "Một biến thể của vòi phun là vòi phun tới hạn (hay vòi phun Venturi dòng tới hạn), được dùng "
        "cả làm chuẩn hiệu chuẩn để kiểm tra lưu lượng kế khí lẫn làm chuẩn chuyển giao trong so sánh "
        "liên phòng thí nghiệm [7]."))

    b.append(h3("Các lưu lượng kế chênh áp khác", "Other Differential Pressure Flowmeters"))
    b.append(p(
        "Còn nhiều loại lưu lượng kế chênh áp khác, gồm nêm phân đoạn, V-cone, khuỷu và ống Dall. "
        "Mỗi loại có ưu điểm riêng so với tấm orifice, ống Venturi và vòi phun trong những ứng dụng "
        "cụ thể. Ví dụ nêm phân đoạn dùng được với dòng có số Reynolds thấp, và ống Dall có tổn thất "
        "áp suất vĩnh viễn thấp hơn ống Venturi. Tuy vậy chưa loại nào được tiêu chuẩn quốc tế đề "
        "cập, nên phải hiệu chuẩn mới xác định được độ chính xác. Thông tin thêm về những loại này "
        "và các loại ít gặp khác có trong [8]."))

    b.append(h3("Tính năng và ứng dụng", "Performance and Applications"))
    b.append(p(
        "Bảng 28.1 trình bày đặc tính tính năng và vùng ứng dụng chính của tấm orifice cạnh vuông, "
        "ống Venturi và vòi phun. So với các loại lưu lượng kế khác trên thị trường, các lưu lượng kế "
        "chênh áp này chỉ có độ chính xác trung bình, điển hình ±2 % giá trị đọc; dĩ nhiên có thể cải "
        "thiện nếu hiệu chuẩn sau khi lắp. Tuy trong một số tình huống chúng dùng được với khí hoặc "
        "chất lỏng bẩn, thường chỉ chịu được một lượng nhỏ thành phần thứ hai trước khi sai số đo trở "
        "nên lớn. Khi tính chi phí và tính năng của một lưu lượng kế chênh áp phải kể cả phần tử sơ "
        "cấp lẫn đầu dò chênh áp. Dù tấm orifice là phần tử sơ cấp rẻ nhất, chi phí phụ kiện để gắn "
        "nó vào đường ống — nhất là khi cần tháo ra trong lúc đang vận hành — có thể đáng kể."))
    b.append(table(*_t281("vi")))
    b.append(p(
        "Chọn lưu lượng kế nào tốt nhất cho một ứng dụng cụ thể có thể rất khó. Các yếu tố chính ảnh "
        "hưởng là tính năng yêu cầu, tính chất chất lưu cần đo, yêu cầu lắp đặt, môi trường sử dụng "
        "và dĩ nhiên là giá thành. Có hai tiêu chuẩn hỗ trợ chọn lưu lượng kế: BS 1042 mục 1.4 — "
        "hướng dẫn dùng các lưu lượng kế chênh áp tiêu chuẩn [9]; và BS 7405 — nguyên tắc rộng hơn về "
        "chọn lưu lượng kế [10]."))
    b.append(p(
        "Vì cả ba loại có độ chính xác tương đương, một cách chọn là xét xem có lý do chính đáng nào "
        "để không dùng lưu lượng kế rẻ nhất và dùng được với dải cỡ ống rộng nhất — tấm orifice. Khi "
        "tổn thất áp suất vĩnh viễn là quan trọng thì nên xét ống Venturi, dù giá cao của nó thường "
        "chỉ hợp lý khi đo lưu lượng lớn. Với ứng dụng nhiệt độ cao hoặc vận tốc cao nên xét vòi "
        "phun, vì trong điều kiện đó nó dự báo được tốt hơn tấm orifice. Với chất lưu bẩn nên xét ống "
        "Venturi hoặc vòi phun thay cho tấm orifice, việc chọn giữa hai loại tuỳ giá thành và yêu cầu "
        "tổn thất áp suất."))
    b.append(table(*_t282("vi")))

    b.append(h3("Lắp đặt", "Installation"))
    b.append(p(
        "Lắp đặt đúng là điều kiện thiết yếu để dùng tốt lưu lượng kế chênh áp, vì độ bất định dự báo "
        "trong quan hệ lưu lượng – chênh áp ở 28.6 giả thiết một dòng ổn định có mặt cắt vận tốc rối "
        "phát triển đầy đủ đi qua lưu lượng kế. Các tiêu chuẩn có khuyến nghị chi tiết về chiều dài "
        "ống thẳng tối thiểu trước và sau lưu lượng kế để bảo đảm mặt cắt dòng phát triển đầy đủ. Cần "
        "đoạn ống thẳng sau lưu lượng kế vì nhiễu do một van hay cút có thể lan ngược lên thượng lưu "
        "và cũng ảnh hưởng tới lưu lượng kế đã lắp. Bảng 28.3 nêu ví dụ yêu cầu lắp đặt lấy từ ISO "
        "5167-1. Nếu không thể bố trí đủ chiều dài ống thẳng trước và sau lưu lượng kế thì phải hiệu "
        "chuẩn lưu lượng kế tại chỗ sau khi lắp."))
    b.append(table(*_t283("vi")))
    b.append(p(
        "Vấn đề lớn khác khi lắp đặt là sự có mặt của dòng xoáy. Tình trạng này làm méo mặt cắt vận "
        "tốc một cách rất khó dự báo và dĩ nhiên là không mong muốn. Nên tránh những tình huống tạo "
        "xoáy, như hai cút 90° trong các mặt phẳng khác nhau. Nếu không tránh được thì có thể khử xoáy "
        "bằng cách đặt một bộ điều hoà dòng (còn gọi là bộ nắn thẳng dòng) giữa nguồn xoáy và lưu "
        "lượng kế. Có rất nhiều kiểu điều hoà dòng, một số vừa khử xoáy vừa chỉnh lại mặt cắt vận "
        "tốc bị méo [11]. Vì cản trở dòng, mọi bộ điều hoà dòng đều gây tổn thất áp suất không phục "
        "hồi được, và nói chung tổn thất này tăng theo năng lực (và độ phức tạp) của bộ."))

    b.append(h3("Đo chênh áp", "Differential Pressure Measurement"))
    b.append(p(
        "Ngoài phần tử tạo chênh áp, phần tử chính khác của lưu lượng kế chênh áp là đầu dò đo sụt áp "
        "qua phần tử đó. Chọn và lắp đặt đúng đầu dò chênh áp góp phần quan trọng quyết định độ chính "
        "xác của phép đo lưu lượng."))
    b.append(p(
        "Các yếu tố chính cần xét khi chọn đầu dò chênh áp cho một ứng dụng đo lưu lượng là dải chênh "
        "áp cần bao, độ chính xác yêu cầu, áp suất cực đại của đường ống, và loại cùng dải nhiệt độ "
        "của chất lưu cần đo."))
    b.append(p(
        "Hầu hết đầu dò chênh áp hiện đại gồm một capsule áp trong đó dùng kỹ thuật điện dung, tenzơ "
        "hay dây cộng hưởng để phát hiện dịch chuyển của màng. Với các kỹ thuật này, độ chính xác "
        "điển hình ±0,1 % toàn thang đo là khả thi; xem Chương 26, Mục 1 để biết thêm về đầu dò áp "
        "suất. Đầu dò thường là một phần của bộ gọi là bộ truyền (transmitter), chuyển các phép đo "
        "chênh áp, áp tĩnh và nhiệt độ môi trường thành tín hiệu ra tương tự hoặc số được chuẩn hoá. "
        "Bộ truyền “thông minh” dùng một vi xử lý cục bộ để điều chế tín hiệu từ từng cảm biến và "
        "tính lưu lượng thể tích hoặc khối lượng. Những thiết bị này cấu hình được từ xa, và nhờ “trí "
        "tuệ” tích hợp mà có nhiều chức năng chẩn đoán và bảo trì."))
    b.append(p(
        "Về lắp đặt, bộ truyền nên đặt càng gần phần tử tạo chênh áp càng tốt; điều này giúp đáp ứng "
        "động nhanh và giảm vấn đề do rung của ống nối. Vị trí điểm lấy áp cũng quan trọng. Nếu đo "
        "dòng chất lỏng trong ống ngang thì điểm lấy áp nên ở bên hông ống để không bị bẩn bít hay "
        "đọng bọt khí. Với dòng khí ngang, nếu khí sạch thì điểm lấy áp nên đặt thẳng đứng; nếu đo "
        "hơi hoặc khí bẩn thì điểm lấy áp nên ở bên hông ống. Những hướng dẫn chung này cho thấy phải "
        "hết sức cẩn thận khi lắp bộ truyền chênh áp nếu muốn tránh sai số lớn. Chi tiết thêm về lắp "
        "đặt bộ truyền chênh áp xem ISO 2186 [12]."))

    b.append(h3("Tiêu chuẩn", "Standards"))
    b.append(p(
        "Các tiêu chuẩn quốc tế quy định thiết kế, lắp đặt và sử dụng tấm orifice, ống Venturi và vòi "
        "phun, đồng thời cho phép tính độ chính xác mà không cần hiệu chuẩn, có lẽ là lý do chính "
        "khiến loại lưu lượng kế này vẫn được dùng. Bảng 28.4 nêu chi tiết các tiêu chuẩn thông dụng "
        "nhất liên quan đến lưu lượng kế chênh áp. Giữa các tiêu chuẩn vẫn còn những điểm không nhất "
        "quán. Ví dụ ISO 5167-1 nói rằng trước một bộ điều hoà dòng phải có ít nhất 22 đường kính ống "
        "thẳng và sau nó ít nhất 20 đường kính — điều này dường như mâu thuẫn với một công dụng của "
        "bộ điều hoà dòng là rút ngắn đoạn ống thẳng cần có thượng lưu lưu lượng kế."))
    b.append(table(*_t284("vi")))
    b.append(p(
        "Bất chấp những điểm không nhất quán và khác biệt thỉnh thoảng gặp, các tiêu chuẩn này là "
        "những quy tắc được quốc tế chấp nhận để lắp đặt và sử dụng tấm orifice cạnh vuông, ống "
        "Venturi và vòi phun."))

    b.append(h3("Phát triển tương lai", "Future Developments"))
    b.append(p(
        "Dù đã có rất nhiều dữ liệu công bố về lưu lượng kế chênh áp, vẫn cần nghiên cứu tiếp để hiểu "
        "rõ hơn ảnh hưởng của điều kiện dòng và hình học lưu lượng kế lên độ chính xác khi chưa hiệu "
        "chuẩn. Ví dụ, gần đây đã có công trình nhằm xây dựng một công thức cải tiến cho hệ số lưu "
        "lượng của tấm orifice [13]."))
    b.append(p(
        "Đo lưu lượng đa pha là lĩnh vực ngày càng quan trọng. Ngoài việc phát triển kỹ thuật đo mới, "
        "nhiều người đang tìm cách dùng lưu lượng kế truyền thống để đo dòng đa pha; xem [14] để có "
        "tổng quan tốt về việc dùng lưu lượng kế chênh áp cho đo đa pha."))
    b.append(p(
        "Sự phát triển của bộ truyền chênh áp “thông minh” đã khắc phục hạn chế của lưu lượng kế "
        "chênh áp trong một số ứng dụng — ví dụ chúng được dùng để tuyến tính hoá và mở rộng dải đo. "
        "Những tiến bộ trên sẽ giúp bảo đảm lưu lượng kế chênh áp còn phổ biến trong thời gian tới, "
        "bất chấp cạnh tranh ngày càng tăng từ các loại thiết bị mới."))

    b.append(h3("Định nghĩa thuật ngữ", "Defining Terms"))
    b.append(defs([
        ("Lưu lượng kế chênh áp",
         "Lưu lượng kế dùng độ sụt áp qua một chỗ thắt hình vành khuyên đặt trên đường ống để đo lưu "
         "lượng. Các loại thông dụng dùng tấm orifice, ống Venturi hoặc vòi phun làm phần tử sơ cấp."),
        ("Tấm orifice",
         "Phần tử sơ cấp gồm một tấm mỏng khoan một lỗ tròn."),
        ("Ống Venturi",
         "Phần tử sơ cấp gồm miệng vào thu dần, đoạn giữa hình trụ và miệng ra loe dần."),
        ("Vòi phun",
         "Phần tử sơ cấp gồm miệng vào thu dần nối với một đoạn hình trụ."),
        ("Bộ truyền chênh áp",
         "Phần tử thứ cấp đo chênh áp qua phần tử sơ cấp và chuyển thành tín hiệu điện."),
    ]))

    b.append(h3("Tài liệu tham khảo", "References"))
    b.append(wl([
        "1. R. A. Furness, Flowmetering: evolution or revolution, <i>Measurement and Control</i>, "
        "27 (8), 15–18, 1994.",
        "2. B. S. Massey, <i>Mechanics of Fluids</i>, 6th ed., London: Chapman and Hall, 1989.",
        "3. ISO 5167-1, <i>Measurement of Fluid Flow by Means of Pressure Differential Devices — "
        "Part 1: Orifice plates, nozzles and Venturi tubes inserted in circular cross-section "
        "conduits running full</i>, Geneva, 1991.",
        "4. API 2530, <i>Manual of Petroleum Measurement Standards, Chapter 14 — Natural Gas Fluids "
        "Measurement, Section 3 — Orifice Metering of Natural Gas and Other Related Hydrocarbon "
        "Fluids</i>, Washington, 1985.",
        "5. E. L. Upp, <i>Fluid Flow Measurement</i>, Houston: Gulf Publishing, 1993.",
        "6. H. S. Bean, <i>Fluid Meters: Their Theory and Application</i>, 6th ed., New York: ASME, 1983.",
        "7. P. H. Wright, The application of sonic (critical flow) nozzles in the gas industry, "
        "<i>Flow Meas. Instrum.</i>, 4 (2), 67–71, 1993.",
        "8. D. W. Spitzer, <i>Industrial Flow Measurement</i>, 2nd ed., Research Triangle Park, NC: "
        "ISA, 1990.",
        "9. BS 1042, <i>Measurement of Fluid Flow in Closed Conduits — Part 1: Pressure differential "
        "devices — Section 1.4: Guide to the use of devices specified in Sections 1.1 and 1.2</i>, "
        "London, 1992.",
        "10. BS 7405, <i>Guide to the Selection and Application of Flowmeters for Measurement of "
        "Fluid Flow in Closed Conduits</i>, London, 1991.",
        "11. E. M. Laws and A. K. Ouazzane, Compact installations for differential pressure flow "
        "measurement, <i>Flow Meas. Instrum.</i>, 5 (2), 79–85, 1994.",
        "12. ISO 2186, <i>Fluid Flow in Closed Conduits — Connections for Pressure Signal "
        "Transmissions Between Primary and Secondary Elements</i>, Geneva, 1973.",
        "13. M. J. Reader-Harris, J. A. Slattery and E. P. Spearman, The orifice plate discharge "
        "coefficient equation — further work, <i>Flow Meas. Instrum.</i>, 6 (2), 101–114, 1995.",
        "14. F. C. Kinghorn, Two-phase flow measurement using differential pressure meters, "
        "<i>Multi-Phase Flow Measurement Short Course</i>, London, 17–18 June 1985.",
    ]))
    return "".join(b)


def sec_28_1_en():
    b = []
    b.append(h2("28.1 Differential Pressure Flowmeters", "Lưu lượng kế chênh áp"))
    b.append(p("Richard Thorn — University of Derby."))
    b.append(p(
        "Flow measurement is an everyday event. Whether you are filling a car with petrol or wanting "
        "to know how much water the garden sprinkler is consuming, a flowmeter is required. It is "
        "equally hard to think of an industrial sector in which a flowmeter of one type or another "
        "plays no part. The world market in flowmeters was estimated at $2,500 million in 1995 and is "
        "expected to grow steadily for the foreseeable future. The value of the product measured is "
        "also very large: in the U.K. alone the crude oil produced in 1994 was worth an estimated "
        "$15 billion."))
    b.append(p(
        "Given that size, it is somewhat surprising that the accuracy and capability of many "
        "flowmeters are poor compared with instruments used for other common process variables such "
        "as pressure and temperature. The orifice plate flowmeter, first used commercially in the "
        "early 1900s and typically accurate to ±2 % of reading, is still the only flowmeter approved "
        "by most countries for fiscal measurement of natural gas. Although newer techniques such as "
        "Coriolis meters have become increasingly popular, the industry is conservative and still "
        "dominated by traditional techniques; see [1] for a review of recent developments."))
    b.append(p(
        "Over 40 % of all liquid, gas and steam measurements in industry are still made with the "
        "common <b>differential pressure flowmeters</b>: the orifice plate, Venturi tube and nozzle. "
        "Their operation rests on Bernoulli's observation that if an annular restriction is placed in "
        "a pipeline the velocity through the restriction increases; the increase lowers the static "
        "pressure at that section and creates a pressure difference across the element. The "
        "difference between upstream and downstream pressure is related to the rate of flow through "
        "the restriction, and therefore through the pipe. A differential pressure flowmeter has two "
        "basic elements: an obstruction causing the pressure drop (a <b>differential producer</b>) and "
        "a means of measuring that drop (a <b>differential pressure transducer</b>)."))
    b.append(p(
        "One major advantage of the orifice plate, Venturi tube or nozzle is that the measurement "
        "uncertainty can be predicted without calibration, provided the device is manufactured and "
        "installed in accordance with one of the international standards covering it. The device is "
        "also simple, has no moving parts and is therefore reliable. The main disadvantages are the "
        "limited range (typically 3:1), the permanent pressure drop in the pipeline (which can raise "
        "pumping costs), and sensitivity to installation effects (minimized by straight lengths of "
        "pipe before and after the meter). The combination of advantages is still hard to beat, and "
        "the limitations have been well investigated and can mostly be compensated. Unless very high "
        "accuracy is needed, or a nonintrusive device is essential, the differential flowmeter should "
        "be considered. Despite predictions of its demise it will remain a common method for many "
        "years."))

    b.append(h3("Important Principles of Fluid Flow in Pipes", "Nguyên lý quan trọng của dòng chảy trong ống"))
    b.append(p(
        "Several principles must be understood before a differential pressure flowmeter can be used "
        "with confidence: the difference between laminar and turbulent flow, the meaning of Reynolds "
        "number, and the importance of the velocity profile."))
    b.append(p(
        "Fluid motion in a pipe is laminar, transitional or turbulent. In <b>laminar flow</b> the "
        "fluid travels as parallel layers (streamlines) that do not mix as they move along. In "
        "turbulent flow the fluid does not travel in parallel layers but moves haphazardly, only the "
        "average motion being parallel to the pipe axis. In <b>transitional</b> flow both types may "
        "be present at different points, or the flow may switch between them."))
    b.append(p(
        "In 1883 Osborne Reynolds showed at the University of Manchester that the flow character can "
        "be predicted with a dimensionless number, now the Reynolds number: the ratio of inertia "
        "forces (ρ v̄ D) to viscous forces (η)."))
    b.append(eq("Re = ρ v̄ D ⁄ η", "28.1"))
    b.append(p(
        "where ρ is the fluid density, v̄ the mean velocity, <i>D</i> the pipe diameter and η the "
        "dynamic viscosity."))
    b.append(p(
        "Below Re = 2000 viscous forces dominate and the flow is laminar; above 4000 inertia forces "
        "dominate and it is turbulent; between 2000 and 4000 the flow is transitional and either mode "
        "may be present. The number is computed mainly from fluid properties and ignores pipe "
        "roughness, bends and valves, which also affect the flow, but it remains a good guide in most "
        "situations."))
    b.append(p(
        "Velocity across a pipe section is not constant. In laminar flow the profile is parabolic, "
        "because large viscous forces slow the fluid near the walls; the velocity at the centre is "
        "twice the average, and the profile is unaffected by wall roughness. In turbulent flow "
        "inertia dominates, wall effects are less, and the profile is flatter, with the centre "
        "velocity about 1.2 times the mean; the exact profile depends on wall roughness and Reynolds "
        "number."))
    b.append(fig(1, F.fig(1), "en"))
    b.append(p(
        "Figure 28.1 shows the fully developed profiles for laminar and turbulent flow — those "
        "obtained at the end of a very long pipe, where changes due to bends and fittings have "
        "disappeared. For confidence in a differential pressure flowmeter, both the character and the "
        "velocity profile of the flow through it must be stable and known."))

    b.append(h3("Bernoulli’s Equation", "Phương trình Bernoulli"))
    b.append(p(
        "The Bernoulli equation relates fluid velocity <i>v</i>, pressure <i>p</i> and height "
        "<i>h</i> above a fixed point for flow through a pipe of varying cross-section, and is the "
        "starting point for the differential pressure flowmeter. For the inclined, tapered pipe of "
        "Figure 28.2:"))
    b.append(eq("p₁ ⁄ (ρg) + v₁² ⁄ (2g) + h₁ = p₂ ⁄ (ρg) + v₂² ⁄ (2g) + h₂", "28.2"))
    b.append(p(
        "The sum of pressure head (<i>p</i>/ρ<i>g</i>), velocity head (<i>v</i>/2<i>g</i>) and "
        "potential head (<i>h</i>) is constant along a streamline. The term “head” is used because "
        "each has the unit of metres. Equation 28.2 assumes a frictionless fluid of constant density; "
        "derivations are in any undergraduate fluid dynamics text (e.g. [2])."))
    b.append(fig(2, F.fig(2), "en"))
    b.append(p(
        "The equation shows how a restriction can measure flow rate. For the section of Figure 28.3 "
        "the pipe is horizontal, so <i>h</i>₁ = <i>h</i>₂ and 28.2 reduces to:"))
    b.append(eq("(p₁ − p₂) ⁄ ρ = (v₂² − v₁²) ⁄ 2", "28.3"))
    b.append(p("Conservation of mass requires:"))
    b.append(eq("v₁ A₁ ρ = v₂ A₂ ρ", "28.4"))
    b.append(p("Rearranging 28.4 and substituting for <i>v</i>₂ in 28.3:"))
    b.append(eq("Q = v₁ A₁ = [A₂ ⁄ √(1 − (A₂ ⁄ A₁)²)] · √(2(p₁ − p₂) ⁄ ρ)", "28.5"))
    b.append(fig(3, F.fig(3), "en"))
    b.append(p(
        "The volumetric flow rate <i>Q</i> therefore follows from the pressure drop across the "
        "restriction — the basic principle of every differential pressure flowmeter. Equation 28.5 "
        "has limitations: the fluid is assumed incompressible (reasonable for most liquids) and "
        "inviscid (giving a flat profile). Both assumptions must be compensated in practical "
        "measurement."))

    b.append(h3("Common Differential Pressure Flowmeters", "Các lưu lượng kế chênh áp thông dụng"))
    b.append(h3("The Orifice Plate", "Tấm orifice"))
    b.append(p(
        "The orifice plate is the simplest and cheapest differential pressure flowmeter: a plate with "
        "a hole of specified size and position, clamped between flanges (Figure 28.4). The rise in "
        "velocity through the hole develops a pressure drop across the plate. Downstream the jet "
        "keeps contracting to a minimum diameter, the vena contracta."))
    b.append(fig(4, F.fig(4), "en"))
    b.append(p(
        "Using 28.5 on the measured drop would give an error, because <i>A</i>₂ should strictly be "
        "the vena contracta area, which is unknown. Turbulence between the vena contracta and the "
        "wall also causes an energy loss the equation ignores."))
    b.append(p(
        "Two empirically determined correction factors are therefore added. After some "
        "reorganization 28.5 becomes:"))
    b.append(eq("Q = [C ⁄ √(1 − β⁴)] · ε · (π ⁄ 4) d² · √(2(p₁ − p₂) ⁄ ρ)", "28.6"))
    b.append(p(
        "where ρ is the density upstream of the plate, <i>d</i> the hole diameter, and β = "
        "<i>d</i>/<i>D</i> the diameter ratio with <i>D</i> the upstream internal pipe diameter."))
    b.append(p(
        "The two factors are <i>C</i>, the discharge coefficient, and ε, the expansibility factor. "
        "<i>C</i> depends on diameter ratio, Reynolds number, pipe roughness, the sharpness of the "
        "leading edge and the tapping positions; for a fixed geometry it has been shown to depend "
        "only on Reynolds number, so it can be determined for a given application. ε accounts for "
        "compressibility. Both come from equations and tables in internationally recognized "
        "standards, which specify not only <i>C</i> and ε but the geometry and installation "
        "conditions for the square-edged orifice plate, Venturi tube and nozzle — effectively a "
        "design guide for the commonest differential pressure meters. Installation recommendations "
        "aim to ensure fully developed turbulent flow in the measurement section. The commonest "
        "standard in Europe is ISO 5167-1 [3]; in the U.S., API 2530 [4]. The two differ in places "
        "(for example the minimum upstream straight length), and work is under way to resolve this."))
    b.append(p(
        "Equation 28.6 illustrates perhaps the greatest strength of the orifice plate: performance "
        "can be predicted without calibration if the device is manufactured, installed and operated "
        "to a standard. It is also cheap, has no moving parts, is reliable, and meters most clean "
        "gases, liquids and steam."))
    b.append(p(
        "Its main disadvantages are limited range and sensitivity to flow disturbance. Because flow "
        "rate goes as the square root of the measured drop, one plate with one transmitter covers "
        "only about 3:1. The required diameter (beta) ratio depends on the maximum flow and the range "
        "of the available transducer; sizing is covered in most of the further reading, and computer "
        "programs are available. Range can be extended by switching, as described in [5]. Equation "
        "28.6 assumes a fully developed, stable profile, so installation is critical — particularly "
        "sufficient upstream straight pipe. Wear of the leading edge can severely alter accuracy, so "
        "the device is normally used only with clean fluids."))
    b.append(p(
        "Only the square-edged concentric plate is covered by the standards; other types exist for "
        "specific applications. One example is the eccentric orifice plate, suited to dirty fluids. "
        "Details are in [6]."))

    b.append(h3("The Venturi Tube", "Ống Venturi"))
    b.append(p(
        "The classical or Herschel Venturi tube is the oldest differential pressure flowmeter, first "
        "used in 1887. As Figure 28.5 shows, the restriction is introduced far more gradually than an "
        "orifice plate. The flow is closer to that predicted by 28.5, so the discharge coefficient is "
        "much nearer unity, typically 0.95. The permanent pressure loss is lower, but so is the "
        "differential pressure for the same diameter ratio. The smooth design makes it less sensitive "
        "to erosion and therefore better suited to dirty gases or liquids, and less sensitive to "
        "upstream disturbance, so it needs shorter upstream straight lengths than an equivalent "
        "orifice plate or nozzle. Design, installation and use are covered by international "
        "standards."))
    b.append(fig(5, F.fig(5), "en"))
    b.append(p(
        "Its main disadvantages are size and cost. It is harder and therefore more expensive to "
        "manufacture than an orifice plate, and being typically six diameters long it becomes "
        "cumbersome in larger pipe sizes, with the associated maintenance of upstream and downstream "
        "lengths also a problem."))

    b.append(h3("The Nozzle", "Vòi phun"))
    b.append(p(
        "The nozzle (Figure 28.6) combines some of the best features of the orifice plate and the "
        "Venturi tube. It is compact and, because of its curved inlet, has a discharge coefficient "
        "close to unity. Several designs exist; the commonest in Europe is the ISA-1932 nozzle, "
        "while in the U.S. the ASME long radius nozzle is more popular. Both are covered by "
        "international standards."))
    b.append(fig(6, F.fig(6), "en"))
    b.append(p(
        "The smooth inlet makes the nozzle more expensive than an orifice plate, since the inlet "
        "curvature changes with diameter ratio, though it is cheaper than a Venturi tube. There are "
        "no sharp edges to erode and shift the calibration, so it suits dirty and abrasive fluids, "
        "and it is commonly used for high-velocity, high-temperature duty such as steam metering."))
    b.append(p(
        "A variation is the sonic (critical flow Venturi) nozzle, used both as a calibration standard "
        "for testing gas meters and as a transfer standard in interlaboratory comparisons [7]."))

    b.append(h3("Other Differential Pressure Flowmeters", "Các lưu lượng kế chênh áp khác"))
    b.append(p(
        "Many other types exist, including the segmental wedge, V-cone, elbow and Dall tube, each "
        "with advantages over the orifice plate, Venturi tube and nozzle for specific applications. "
        "The segmental wedge, for example, handles low Reynolds number flows, and a Dall tube has a "
        "lower permanent loss than a Venturi. None is yet covered by international standards, so "
        "calibration is needed to establish accuracy. Further information is in [8]."))

    b.append(h3("Performance and Applications", "Tính năng và ứng dụng"))
    b.append(p(
        "Table 28.1 gives the performance and main application areas of the square-edged orifice "
        "plate, Venturi tube and nozzle. Against other meters on the market these are only moderately "
        "accurate, typically ±2 % of reading, though calibrating after installation improves this. "
        "Although they can sometimes handle dirty gases or liquids, usually only small amounts of a "
        "second component can be tolerated before large errors appear. When costing a differential "
        "pressure flowmeter both the primary element and the transmitter must be counted; the orifice "
        "plate is the cheapest primary element, but the fitting needed to mount it — particularly if "
        "on-line removal is required — can be significant."))
    b.append(table(*_t281("en")))
    b.append(p(
        "Choosing the best meter for a given application can be very difficult. The main factors are "
        "the required performance, the properties of the fluid, the installation requirements, the "
        "environment and, of course, cost. Two standards help: BS 1042 Section 1.4, a guide to the "
        "standard differential pressure flowmeters [9], and BS 7405 on the wider principles of "
        "flowmeter selection [10]."))
    b.append(p(
        "Since all three have similar accuracy, one strategy is to ask whether there is any good "
        "reason not to use the cheapest meter that covers the widest range of pipe sizes — the "
        "orifice plate. Where permanent pressure loss matters the Venturi tube should be considered, "
        "though its high cost is usually only justified for large quantities. For high-temperature or "
        "high-velocity duty the nozzle should be considered, being more predictable than the plate "
        "there. For dirty fluids either the Venturi tube or the nozzle should be preferred, the "
        "choice between them depending on cost and pressure-loss requirements."))
    b.append(table(*_t282("en")))

    b.append(h3("Installation", "Lắp đặt"))
    b.append(p(
        "Correct installation is essential, because the predicted uncertainty of 28.6 assumes a "
        "steady flow with a fully developed turbulent profile through the meter. Standards contain "
        "detailed recommendations for minimum straight lengths before and after the meter; lengths "
        "are needed downstream too because disturbances from a valve or bend can travel upstream and "
        "affect the installed meter. Table 28.3 gives examples taken from ISO 5167-1. If the "
        "recommended lengths cannot be fitted, the meter must be calibrated once installed."))
    b.append(table(*_t283("en")))
    b.append(p(
        "The other major installation problem is a rotating flow, or swirl. It distorts the velocity "
        "profile unpredictably and is obviously undesirable. Situations that create swirl, such as "
        "two 90° bends in different planes, should be avoided; if that is impossible, a flow "
        "conditioner (flow straightener) between the source of swirl and the meter will remove it. "
        "Many designs exist, some of which both remove swirl and correct a distorted profile [11]. "
        "Because they obstruct the flow, all conditioners produce an unrecoverable pressure loss, "
        "which generally grows with their capability and complexity."))

    b.append(h3("Differential Pressure Measurement", "Đo chênh áp"))
    b.append(p(
        "Apart from the producer, the other main element is the transducer measuring the drop across "
        "it. Correct selection and installation of the transducer plays an important part in "
        "determining the accuracy of the flow measurement."))
    b.append(p(
        "The main factors to consider are the differential pressure range, the accuracy required, the "
        "maximum pipeline pressure, and the type and temperature range of the fluid."))
    b.append(p(
        "Most modern transducers consist of a pressure capsule in which capacitance, strain gage or "
        "resonant wire techniques detect the movement of a diaphragm, giving a typical accuracy of "
        "±0.1 % of full scale; see Chapter 26, Section 1 for pressure transducers. The transducer is "
        "usually part of a transmitter, which converts differential pressure, static pressure and "
        "ambient temperature into a standardized analog or digital output. “Smart” transmitters use a "
        "local microprocessor to condition the sensor signals and compute volumetric or mass flow; "
        "they can be configured remotely and offer a wide range of diagnostic and maintenance "
        "functions."))
    b.append(p(
        "The transmitter should sit as close to the producer as possible, which helps dynamic "
        "response and reduces problems from vibrating impulse lines. Tapping position also matters. "
        "For liquid in a horizontal pipe the tappings should be at the side, so they cannot be "
        "blocked by dirt or filled with air bubbles. For horizontal gas flow, vertical tappings suit "
        "clean gas; for steam or dirty gas they should be at the side. These guidelines show that "
        "considerable care is needed if large errors are to be avoided; see ISO 2186 [12]."))

    b.append(h3("Standards", "Tiêu chuẩn"))
    b.append(p(
        "The international standards specifying design, installation and use of the orifice plate, "
        "Venturi tube and nozzle — and allowing accuracy to be calculated without calibration — are "
        "probably the main reason this type of meter is still used. Table 28.4 details the commonest. "
        "Inconsistencies remain: ISO 5167-1, for instance, states that any flow conditioner should be "
        "preceded by at least 22 diameters of straight pipe and followed by at least 20, which seems "
        "to contradict one purpose of a conditioner — reducing the upstream straight length needed."))
    b.append(table(*_t284("en")))
    b.append(p(
        "Despite the occasional inconsistency, the standards are the internationally accepted rules "
        "for installing and using the square-edged orifice plate, Venturi tube and nozzle."))

    b.append(h3("Future Developments", "Phát triển tương lai"))
    b.append(p(
        "Despite the vast published data on differential pressure flowmeters, research continues into "
        "the effect of flow conditions and meter geometry on uncalibrated accuracy — work has recently "
        "been done on an improved discharge-coefficient equation for the orifice plate [13]."))
    b.append(p(
        "Multiphase metering is of increasing importance. Besides new techniques, many are "
        "investigating how traditional meters can handle multiphase flow; a good review of "
        "differential pressure meters for this duty is in [14]."))
    b.append(p(
        "“Smart” differential pressure transmitters have overcome the limitations of these meters in "
        "some applications — being used, for example, to linearize and extend their range. These "
        "developments should ensure the continued popularity of the differential pressure flowmeter, "
        "despite competition from newer instruments."))

    b.append(h3("Defining Terms", "Định nghĩa thuật ngữ"))
    b.append(defs([
        ("Differential pressure flowmeter",
         "A flowmeter in which the pressure drop across an annular restriction in the pipeline "
         "measures the flow rate. The commonest use an orifice plate, Venturi tube or nozzle as the "
         "primary device."),
        ("Orifice plate",
         "Primary device consisting of a thin plate with a circular aperture cut in it."),
        ("Venturi tube",
         "Primary device consisting of a converging inlet, a cylindrical mid-section and a diverging "
         "outlet."),
        ("Nozzle",
         "Primary device consisting of a convergent inlet connected to a cylindrical section."),
        ("Differential pressure transmitter",
         "Secondary device that measures the differential pressure across the primary device and "
         "converts it into an electrical signal."),
    ]))

    b.append(h3("References", "Tài liệu tham khảo"))
    b.append(wl([
        "1. R. A. Furness, Flowmetering: evolution or revolution, <i>Measurement and Control</i>, "
        "27 (8), 15–18, 1994.",
        "2. B. S. Massey, <i>Mechanics of Fluids</i>, 6th ed., London: Chapman and Hall, 1989.",
        "3. ISO 5167-1, <i>Measurement of Fluid Flow by Means of Pressure Differential Devices — "
        "Part 1</i>, Geneva, 1991.",
        "4. API 2530, <i>Manual of Petroleum Measurement Standards, Chapter 14, Section 3</i>, "
        "Washington, 1985.",
        "5. E. L. Upp, <i>Fluid Flow Measurement</i>, Houston: Gulf Publishing, 1993.",
        "6. H. S. Bean, <i>Fluid Meters: Their Theory and Application</i>, 6th ed., New York: ASME, 1983.",
        "7. P. H. Wright, The application of sonic (critical flow) nozzles in the gas industry, "
        "<i>Flow Meas. Instrum.</i>, 4 (2), 67–71, 1993.",
        "8. D. W. Spitzer, <i>Industrial Flow Measurement</i>, 2nd ed., Research Triangle Park, NC: "
        "ISA, 1990.",
        "9. BS 1042, <i>Measurement of Fluid Flow in Closed Conduits — Part 1, Section 1.4</i>, "
        "London, 1992.",
        "10. BS 7405, <i>Guide to the Selection and Application of Flowmeters</i>, London, 1991.",
        "11. E. M. Laws and A. K. Ouazzane, Compact installations for differential pressure flow "
        "measurement, <i>Flow Meas. Instrum.</i>, 5 (2), 79–85, 1994.",
        "12. ISO 2186, <i>Fluid Flow in Closed Conduits — Connections for Pressure Signal "
        "Transmissions</i>, Geneva, 1973.",
        "13. M. J. Reader-Harris, J. A. Slattery and E. P. Spearman, The orifice plate discharge "
        "coefficient equation — further work, <i>Flow Meas. Instrum.</i>, 6 (2), 101–114, 1995.",
        "14. F. C. Kinghorn, Two-phase flow measurement using differential pressure meters, "
        "<i>Multi-Phase Flow Measurement Short Course</i>, London, 17–18 June 1985.",
    ]))
    return "".join(b)


# ================================================================ 28.2

def sec_28_2_vi():
    b = []
    b.append(h2("28.2 Lưu lượng kế biến diện tích", "Variable Area Flowmeters"))
    b.append(p("Adrian Melling, Herbert Köchner và Reinhard Haak — Đại học Erlangen-Nürnberg."))
    b.append(p(
        "Thuật ngữ <b>lưu lượng kế biến diện tích</b> dùng để chỉ những lưu lượng kế trong đó diện "
        "tích mặt cắt tối thiểu mà dòng chảy đi qua thay đổi theo lưu lượng. Các loại thuộc nhóm này "
        "được bàn ở mục này gồm rotameter và lưu lượng kế cánh quay dùng cho dòng chảy trong ống, "
        "cùng đập tràn và máng dùng cho dòng chảy hở. Đại lượng được đo là một đại lượng hình học: "
        "độ cao của phao trong rotameter, góc của cánh, hay độ thay đổi mực nước tự do của chất lỏng "
        "chảy qua đập tràn hoặc qua máng."))
    b.append(p(
        "Phần lớn nội dung dưới đây dành cho rotameter, thứ nhất vì số rotameter và lưu lượng kế cánh "
        "quay đã lắp đặt lớn hơn nhiều so với số đập tràn và máng, thứ hai vì cánh quay thường chỉ "
        "được dùng làm chỉ báo lưu lượng hơn là làm dụng cụ đo."))
    b.append(p(
        "Mục tiếp theo trình bày thông tin cơ bản về đặc điểm kết cấu và ứng dụng của từng loại thiết "
        "bị. Mục thứ ba mô tả khá chi tiết nguyên lý đo và thiết kế của rotameter và lưu lượng kế "
        "kênh hở; lưu lượng kế cánh quay không được bàn thêm vì phần lớn khía cạnh thiết kế của nó "
        "giống rotameter. Sau đó là đóng góp của các phương pháp cơ học chất lưu tính toán và thực "
        "nghiệm hiện đại cho việc thiết kế lưu lượng kế, minh hoạ bằng kết quả của một nghiên cứu "
        "chi tiết dòng chảy bên trong thiết bị."))
    b.append(p(
        "Thông tin về các hãng chế tạo rotameter và lưu lượng kế cánh quay, cùng giá tham khảo của "
        "chúng, được lập thành bảng ở Bảng 28.5 đến Bảng 28.7."))

    b.append(h3("Mô tả chung lưu lượng kế biến diện tích", "General Description of Variable Area Flowmeters"))

    b.append(h4("Rotameter"))
    b.append(p(
        "Rotameter là một lưu lượng kế chắc chắn và đơn giản dùng cho khí và chất lỏng, chiếm thị phần "
        "lớn với đường kính ống nhỏ hơn khoảng 100 mm. Ở dạng cơ bản, rotameter gồm một ống thuỷ tinh "
        "trong suốt, thẳng đứng, có dạng côn, chứa một “phao” (Hình 28.7); phao dâng lên trong ống khi "
        "lưu lượng tăng cho tới khi đạt cân bằng giữa trọng lực, lực đẩy và lực cản tác dụng lên nó. "
        "Trong phạm vi của một lưu lượng kế cụ thể (tuỳ hình dạng và khối lượng riêng của phao, hình "
        "dạng ống và khối lượng riêng, độ nhớt của chất lưu), lưu lượng tỉ lệ tuyến tính với độ cao "
        "của phao trong ống và được xác định đơn giản bằng cách đọc mức mép trên của phao. Rotameter "
        "còn được gọi là “lưu lượng kế phần tử nổi”, dù lực đẩy tác dụng lên “phần tử nổi” không đủ "
        "để làm nó nổi."))
    b.append(fig(7, F.fig(7), "vi"))
    b.append(p(
        "Phao thường được tạo thành từ tổ hợp các đoạn trụ và đoạn côn, nhưng với ống đường kính nhỏ "
        "người ta hay dùng phao hình cầu (Hình 28.8). Những dạng phao phức tạp hơn có thể làm giảm độ "
        "nhạy của số đọc với độ nhớt của chất lưu. Phao thường có vài rãnh nông nghiêng quanh vành "
        "trên, gây ra chuyển động quay chậm (tần số khoảng 1 Hz) giúp phao giữ được vị trí ổn định. "
        "Ở các rotameter lớn hơn, nơi ma sát phụ thêm là chấp nhận được, phao có thể trượt lên xuống "
        "theo một thanh dẫn đặt trên trục ống để chống mọi chuyển động ngang."))
    b.append(fig(8, F.fig(8), "vi"))
    b.append(p(
        "Nhiều dạng hình học ống đang được dùng. Yêu cầu cơ bản là diện tích mặt cắt phải tăng dần "
        "theo chiều cao của ống, dẫn tới ống hình côn. Một dạng khác dùng ba gờ xếp theo chu vi ống để "
        "dẫn hướng phao; diện tích dòng chảy giữa các gờ tăng dần theo chiều cao ống. Với phao hình "
        "cầu, ống tiết diện tam giác — trong đó phao luôn tiếp xúc với ba mặt trên suốt chiều cao ống "
        "— vừa chống được chuyển động ngang của phao vừa giữ ma sát ở mức tối thiểu. Thông thường ống "
        "được làm bằng thuỷ tinh để tiện đọc lưu lượng trên thang khắc thẳng lên ống. Với ứng dụng đa "
        "năng, thang có thể khắc theo milimét; khi đó lưu lượng được xác định bằng một hệ số chuyển "
        "đổi phụ thuộc kích thước ống, khối lượng phao, áp suất, nhiệt độ và tính chất của chất lưu. "
        "Với ứng dụng riêng cho một chất lưu trong điều kiện xác định, khắc thẳng lưu lượng lên ống "
        "thuận tiện hơn."))
    b.append(p(
        "Với sử dụng trong phòng thí nghiệm, thiết bị y tế và các ứng dụng lưu lượng nhỏ khác, ống "
        "thuỷ tinh gần như phổ dụng. Các lưu lượng kế phòng thí nghiệm thường có kèm một van lưu lượng "
        "cho phép đặt và đọc lưu lượng trực tiếp. Với nhiều rotameter nhỏ, người ta cung cấp bộ điều "
        "khiển lưu lượng tích hợp; bộ này giữ độ sụt áp và giá trị đặt lưu lượng không đổi ngay cả khi "
        "áp suất thượng lưu hay hạ lưu thay đổi."))
    b.append(p(
        "Phần lớn rotameter có sẵn công tắc giới hạn điện hoặc bộ chuyển đổi tín hiệu điện tương tự. "
        "Với các lưu lượng kế thuỷ tinh và nhựa, người ta dùng công tắc cảm ứng hoặc quang, đặt được "
        "tại mức mong muốn của phao. Trong khi một số thiết bị chỉ phát hiện phao nằm trong vùng tác "
        "động của chúng, những công tắc khác có chế độ hai trạng thái, trong đó công tắc được lật "
        "trạng thái khi phao đi qua."))
    b.append(p(
        "Với ứng dụng công nghiệp, việc đo chất lưu ăn mòn hoặc chất lưu ở nhiệt độ, áp suất cao dẫn "
        "tới việc dùng ống thép không gỉ hoặc nhiều loại vật liệu khác được chọn cho phù hợp yêu cầu "
        "ứng dụng (ví dụ nhiệt độ, áp suất, ăn mòn). Phần lớn rotameter kim loại dùng khớp nối từ vĩnh "
        "cửu giữa phao và kim chỉ của bộ chỉ thị, cho phép đọc lưu lượng tương tự trực tiếp mà không "
        "cần nguồn điện. Tuy vậy vẫn có thể thêm công tắc điện vào bộ chỉ thị, và phần lớn nhà sản "
        "xuất đều cung cấp bộ truyền tín hiệu điện và khí nén cho số đọc lưu lượng. Một số thiết bị có "
        "các tuỳ chọn như bộ tổng hoá lưu lượng, bộ tính lưu lượng khối cho ứng dụng khí (kết hợp cảm "
        "biến nhiệt độ và áp suất), hoặc bộ tính năng lượng. Do rotameter được dùng thường xuyên trong "
        "công nghiệp hoá chất và hoá dầu, các tuỳ chọn điện thường được thiết kế để dùng trong vùng "
        "nguy hiểm cháy nổ."))
    b.append(p("Rotameter có các đặc điểm:"))
    b.append(ul([
        "Kết cấu đơn giản và chắc chắn",
        "Độ tin cậy cao",
        "Tổn thất áp suất thấp",
        "Dùng được cho rất nhiều loại khí và chất lỏng",
        "Dải lưu lượng điển hình 0,04 L h⁻¹ đến 150 m³ h⁻¹ với nước",
        "Dải lưu lượng điển hình 0,5 L h⁻¹ đến 3 000 m³ h⁻¹ với không khí",
        "Dải đo 10:1 với một tổ hợp phao–ống cho trước",
        "Độ bất định 0,4 % đến 4 % lưu lượng cực đại",
        "Không nhạy với sự không đồng đều của dòng vào (không cần đoạn ống thẳng thượng lưu)",
        "Nhiệt độ cực đại điển hình 400 °C",
        "Áp suất cực đại điển hình 4 MPa (40 bar)",
        "Chi phí đầu tư thấp",
        "Chi phí lắp đặt thấp",
    ]))
    b.append(table(*_t285("vi")))
    b.append(table(*_t287("vi")))

    b.append(h4("Lưu lượng kế cánh quay", "Movable Vane Meter"))
    b.append(p(
        "Lưu lượng kế cánh quay là thiết bị chắc chắn, phù hợp để đo lưu lượng lớn khi yêu cầu về độ "
        "chính xác đo chỉ ở mức vừa phải. Chất lưu bẩn cũng đo được. Thiết bị có một cánh lật mà khi "
        "lưu lượng bằng không được giữ đóng bằng một quả cân hoặc một lò xo (Hình 28.9). Dòng chảy "
        "đẩy cánh mở ra cho tới khi lực động của dòng cân bằng với lực phục hồi của quả cân hay lò "
        "xo. Góc của cánh do đó là thước đo lưu lượng, và có thể được chỉ trực tiếp bằng một kim gắn "
        "trên trục của cánh, trên một thang đã chia độ. Lực cản do cánh tạo ra phụ thuộc vị trí cánh, "
        "do đó phụ thuộc lưu lượng hay số Reynolds; vì vậy phải hiệu chuẩn lại khi đổi chất lưu. Một "
        "ứng dụng quan trọng là đo lưu lượng khí nạp trong động cơ ô tô phun xăng điện tử."))
    b.append(fig(9, F.fig(9), "vi"))
    b.append(p(
        "Trong các chỉ báo lưu lượng giá rẻ, một cửa sổ thuỷ tinh hay nhựa cho phép nhìn trực tiếp "
        "cánh lật (Hình 28.10). Đôi khi người ta dùng công tắc quang hoặc công tắc lưỡi gà kết hợp "
        "với một nam châm vĩnh cửu gắn trên cánh làm công tắc lưu lượng điện. Các thiết bị toàn kim "
        "loại dùng khớp nối từ giữa cánh và kim chỉ của bộ chỉ thị, nhờ đó tránh được phần lớn vấn đề "
        "ma sát và vấn đề chọn vật liệu. Nhiều ứng dụng dùng lưu lượng kế cánh quay như một công tắc "
        "lưu lượng với công tắc cơ khí, từ, cảm ứng hoặc quang thích hợp. Việc đặt ngưỡng công tắc "
        "được làm một lần duy nhất khi lắp đặt. Vì không cần chỉ thị lưu lượng liên tục nên độ bất "
        "định của số đọc không thành vấn đề."))
    b.append(fig(10, F.fig(10), "vi"))
    b.append(p(
        "Phần lớn khía cạnh thiết kế và ứng dụng của rotameter áp dụng được cho lưu lượng kế cánh "
        "quay, dù loại sau có độ bất định của số đọc cao hơn. Đặc điểm chung của cả hai loại lưu lượng "
        "kế biến diện tích được tóm tắt, ví dụ, trong tài liệu [1]. Vì kết cấu cơ bản của hai loại rất "
        "giống nhau nên giá thành đơn vị cũng nằm trong cùng một khoảng."))
    b.append(table(*_t286("vi")))

    b.append(h4("Đập tràn, máng", "Weir, Flume"))
    b.append(p(
        "Trong số các phương pháp đo lưu lượng chất lỏng (thường là nước) trong dòng chảy hở, đập tràn "
        "và máng thuộc phạm vi bàn của mục về lưu lượng kế biến diện tích này. Trong cả hai trường hợp, "
        "phép đo dựa trên việc xác định độ chênh mực nước <i>h</i> giữa mặt nước tại chỗ có vật cản "
        "ngang kênh và mặt nước ở vị trí đủ xa về phía thượng lưu. Có rất nhiều dạng hình học đang "
        "được dùng (xem tài liệu [2]), nhưng phần lớn có thể xem là biến thể của ba dạng cơ bản. Trong "
        "<b>đập tràn thành mỏng</b>, còn gọi là đập tràn tấm mỏng (Hình 28.11), ngưỡng hay đỉnh tràn "
        "chỉ dày khoảng 1 mm đến 2 mm. Tấm chất lỏng chảy qua đập tràn, gọi là <i>nappe</i> hay "
        "<i>vein</i>, tách khỏi thân đập sau khi vượt qua đỉnh. Một vùng chứa khí ở áp suất khí quyển "
        "hình thành bên dưới dòng chảy ra, và các đường dòng phía trên đập tràn bị uốn mạnh. Nếu "
        "chiều rộng đập nhỏ hơn chiều rộng kênh thượng lưu (Hình 28.12 và Hình 28.13) thì người ta "
        "thường dùng thuật ngữ “cửa tràn” (notch). <b>Đập tràn đỉnh rộng</b> (Hình 28.14) có ngưỡng đủ "
        "dài để các đường dòng thẳng, song song hình thành phía trên đỉnh. Trong phần này, thuật ngữ "
        "“đập tràn” được dùng chung cho cả đập tràn và cửa tràn."))
    b.append(fig(11, F.fig(11), "vi"))
    b.append(p(
        "Lực cản mà đập tràn đưa vào dòng chảy làm mực nước thượng lưu dâng lên. Nếu giả thiết vận tốc "
        "dòng chảy ở một khoảng cách nào đó phía thượng lưu bằng không thì chỉ cần một phép đo đơn "
        "giản mực nước thượng lưu là đủ để xác định lưu lượng qua một đập tràn có hình học đã biết. "
        "Cũng như trường hợp tấm orifice trong dòng chảy trong ống, sẽ có sự co thắt của <i>nappe</i> "
        "và sức cản ma sát ở hai bên khi nước chảy qua đập tràn. Lưu lượng thực nhỏ hơn lưu lượng lý "
        "thuyết theo một hệ số lưu lượng <i>C</i><sub>d</sub> xác định bằng thực nghiệm. Khi phân tích "
        "cửa tràn và đập tràn chữ nhật, người ta thường giả thiết chiều rộng kênh không đổi, do đó "
        "<i>nappe</i> chỉ co thắt theo phương thẳng đứng khi nước tăng tốc qua vật cản. Khi đập tràn "
        "hẹp hơn kênh thượng lưu thì có thêm co thắt theo phương ngang. Ảnh hưởng của vận tốc tới "
        "(vận tốc dòng chảy phía thượng lưu) đáng kể được kể đến bằng thực nghiệm."))
    b.append(fig(12, F.fig(12), "vi"))
    b.append(fig(13, F.fig(13), "vi"))
    b.append(fig(14, F.fig(14), "vi"))
    b.append(p(
        "Như một phương án thay thế đập tràn, <b>máng</b> (Hình 28.15) cho một cách đo lưu lượng với "
        "tổn thất áp suất tương đối nhỏ. Bằng cách thu hẹp chiều rộng kênh — tương tự ống Venturi "
        "trong dòng chảy trong ống — vận tốc dòng trong đoạn hẹp của kênh tăng lên và mực nước hạ "
        "xuống tương ứng. Phần lớn cột nước được thu hồi trong đoạn khuếch tán của máng. Mực nước "
        "thượng lưu và tại họng máng có thể xác định bằng các phao đơn giản và ghi lên băng giấy bằng "
        "bút vẽ dẫn động cơ khí từ phao. Để theo dõi từ xa, dùng máy dội âm (echo sounder) là thuận "
        "lợi."))
    b.append(fig(15, F.fig(15), "vi"))
    b.append(p(
        "Đập tràn được ưu tiên dùng ở lòng sông tự nhiên, còn máng dùng ở các tuyến dẫn nước đã được "
        "kênh hoá. Máng phải được dùng ở những dòng có vận chuyển bùn cát để tránh tích tụ cặn — điều "
        "sẽ xảy ra ở đoạn dẫn vào đập tràn. Đập tràn và máng có các đặc điểm:"))
    b.append(ul([
        "Đo mực nước đơn giản",
        "Bảo trì đơn giản",
        "Đo lưu lượng lớn một cách tin cậy ở vận tốc dòng nhỏ",
        "Độ chính xác đo hạn chế (tốt nhất khoảng 2 %)",
        "Chi phí lắp đặt cao, đặc biệt với máng",
    ]))
    b.append(p(
        "Các khuyến nghị về lắp đặt đập tràn và máng, về vị trí trạm đo cột nước phía thượng lưu và về "
        "cách xác định lưu lượng từ cột nước đo được được trình bày, ví dụ, trong [2] và [3] cũng như "
        "trong các tiêu chuẩn thích hợp (ví dụ [4–6])."))

    b.append(h3("Nguyên lý đo của lưu lượng kế biến diện tích",
                "Measuring Principles of Variable Area Flowmeters"))

    b.append(h4("Rotameter: phân tích lưu lượng", "Rotameter: Flow Rate Analysis"))
    b.append(p(
        "Các lực tác dụng lên phao dẫn tới cân bằng giữa trọng lượng của phao ρ<sub>b</sub><i>gV</i>"
        "<sub>b</sub> hướng xuống dưới với lực đẩy Archimedes ρ<i>gV</i><sub>b</sub> và lực cản "
        "<i>F</i><sub>d</sub> hướng lên trên, trong đó <i>V</i><sub>b</sub> là thể tích và "
        "ρ<sub>b</sub> là khối lượng riêng của phao, ρ là khối lượng riêng của chất lưu, và <i>g</i> "
        "là gia tốc trọng trường:"))
    b.append(eq("ρ<sub>b</sub>gV<sub>b</sub> = ρgV<sub>b</sub> + F<sub>d</sub>", "28.7"))
    b.append(p(
        "Lực cản sinh ra từ trường dòng bao quanh phao, đặc biệt từ vùng vệt xoáy phía sau phao. "
        "Trong các phân tích dòng dựa trên nguyên lý tương tự, những ảnh hưởng này được kể đến bằng "
        "các hệ số thực nghiệm <i>C</i><sub>L</sub> hoặc <i>C</i><sub>T</sub> trong định luật cản:"))
    b.append(eq('<span style="font-style:italic;margin-right:1.4rem">chảy tầng</span>'
                'F<sub>d</sub> = C<sub>L</sub>μD<sub>b</sub>U', "28.8"))
    b.append(eq('<span style="font-style:italic;margin-right:1.4rem">chảy rối</span>'
                'F<sub>d</sub> = C<sub>T</sub>ρD<sub>b</sub>²U²', "28.9"))
    b.append(p(
        "trong đó μ là độ nhớt chất lưu, <i>D</i><sub>b</sub> là đường kính lớn nhất của phao, và "
        "<i>U</i> là vận tốc trong khe vành khuyên quanh phao tại tiết diện nhỏ nhất."))
    b.append(p("Lưu lượng thể tích qua rotameter là:"))
    b.append(eq("Q̇ = (π/4)(D² − D<sub>b</sub>²)U", "28.10"))
    b.append(p("hay"))
    b.append(eq("Q̇ = m(π/4)D<sub>b</sub>²U", "28.11"))
    b.append(p("trong đó <i>m</i> là tỉ số diện tích mở, định nghĩa là:"))
    b.append(eq("m = (D² − D<sub>b</sub>²) / D<sub>b</sub>²", "28.12"))
    b.append(p("và <i>D</i> là đường kính ống tại độ cao của phao."))
    b.append(p("Kết hợp các Phương trình 28.7, 28.8 và 28.10 ta được với chảy tầng:"))
    b.append(eq("Q̇ = αD<sub>b</sub>⁴(ρ<sub>b</sub> − ρ)g / μ", "28.13"))
    b.append(p(
        "trong đó tham số α được định nghĩa qua một hằng số <i>K</i> = <i>V</i><sub>b</sub> / "
        "<i>D</i><sub>b</sub>³ đặc trưng cho hình dạng của phao:"))
    b.append(eq("α = πmK / (4C<sub>L</sub>)", "28.14"))
    b.append(p("Dùng Phương trình 28.9 thay cho 28.8 ta được với chảy rối:"))
    b.append(eq("Q̇ = βD<sub>b</sub><sup>5/2</sup>√[(ρ<sub>b</sub> − ρ)g / ρ]", "28.15"))
    b.append(p("trong đó"))
    b.append(eq("β = (πm / 4)√(K / C<sub>T</sub>)", "28.16"))
    b.append(p(
        "Với cả chảy tầng lẫn chảy rối qua rotameter, rõ ràng từ các Phương trình 28.13 và 28.15 rằng "
        "lưu lượng tỉ lệ với <i>m</i>. Nếu diện tích mặt cắt của ống được làm tăng tuyến tính theo "
        "chiều dài, tức là:"))
    b.append(eq("D = D<sub>b</sub>(1 + h tan φ)", "28.17"))
    b.append(p(
        "thì vì góc côn φ của ống nhỏ, Phương trình 28.12 có thể viết thành:"))
    b.append(eq("m = 2h tan φ", "28.18"))
    b.append(p("và lưu lượng tỉ lệ trực tiếp với độ cao <i>h</i> của phao."))

    b.append(h4("Phân tích tương tự", "Similarity Analysis"))
    b.append(p(
        "Trong các nghiên cứu đầu tiên về lưu lượng kế phần tử nổi, Ruppel và Umpfenbach [7] đề xuất "
        "đưa vào các đại lượng không thứ nguyên đặc trưng để có thể dùng các hệ số lưu lượng xác định "
        "bằng thực nghiệm trong phân tích lưu lượng kế. Lutz [8] mở rộng các ý tưởng này bằng cách chỉ "
        "ra rằng có thể chuyển hệ số lưu lượng từ lưu lượng kế này sang lưu lượng kế khác nếu tồn tại "
        "tương tự hình học. Các công trình gần đây hơn [9–12] dùng những nguyên lý này để xây dựng các "
        "phương án thiết kế bằng đồ thị hoặc bằng máy tính, và đề xuất các hướng dẫn chung để bố trí "
        "các hệ đo lưu lượng trong thực tế."))
    b.append(p("Tham số tỉ lệ cơ bản của dòng chảy là số Reynolds, định nghĩa là:"))
    b.append(eq("Re = ρU<sub>IN</sub>D<sub>b</sub> / μ", "28.19"))
    b.append(p(
        "trong đó <i>U</i><sub>IN</sub> là vận tốc tại lối vào rotameter, và đường kính ống <i>D</i> "
        "được biểu diễn bằng giá trị tại lối vào, tức bằng đường kính phao <i>D</i><sub>b</sub>. Qua "
        "số Reynolds có thể phân biệt các chế độ chảy tầng hoặc chảy rối, và đặc biệt quan trọng với "
        "rotameter là các chế độ phụ thuộc mạnh hay yếu vào độ nhớt. Xuất phát từ công trình [7], với "
        "rotameter người ta thấy thực tế hơn khi dùng một đặc số thay thế, gọi là số Ruppel, định "
        "nghĩa là:"))
    b.append(eq("Ru = μ / √[m<sub>b</sub>gρ(1 − ρ/ρ<sub>b</sub>)]", "28.20"))
    b.append(p(
        "trong đó <i>m</i><sub>b</sub> = ρ<sub>b</sub><i>D</i><sub>b</sub>³ là khối lượng của phao. "
        "Kết hợp các Phương trình 28.15, 28.16 và 28.20, lưu lượng khối ṁ qua rotameter có thể viết "
        "là:"))
    b.append(eq("ṁ = (π/4)·mD<sub>b</sub>μ / (√C<sub>T</sub>·Ru)", "28.21"))
    b.append(p("Hoặc, từ định nghĩa:"))
    b.append(eq("ṁ = ρQ̇ = ρU<sub>IN</sub>(π/4)D<sub>b</sub>²", "28.22"))
    b.append(p("và Phương trình 28.19, lưu lượng là:"))
    b.append(eq("ṁ = (π/4)D<sub>b</sub>μRe", "28.23"))
    b.append(p(
        "Các Phương trình 28.21 và 28.23 cho quan hệ sau giữa số Ruppel và số Reynolds:"))
    b.append(eq("Ru = m / (√C<sub>T</sub>·Re)", "28.24"))
    b.append(p("Phân tích cho chảy tầng dẫn tới quan hệ:"))
    b.append(eq("Ru = √(m / (C<sub>L</sub>Re))", "28.25"))
    b.append(p(
        "Ưu điểm của số Ruppel là nó không phụ thuộc lưu lượng. Vì số Ruppel chỉ chứa tính chất chất "
        "lưu cùng khối lượng và khối lượng riêng của phao, nó là hằng số với một thiết bị cụ thể."))
    b.append(p(
        "Ở số Ruppel thấp, định luật cản tuyến tính giả thiết trong Phương trình 28.8 đúng và α là "
        "hằng số với <i>m</i> cho trước, như chỉ ra trên Hình 28.16. Ở số Ruppel cao hơn, dòng là quá "
        "độ hoặc chảy rối, và log α giảm tuyến tính theo log <i>Ru</i>. Trên Hình 28.17, các đường "
        "cong của β theo số Ruppel cho thấy log β tăng tuyến tính theo log <i>Ru</i> trong vùng chảy "
        "tầng, sau đó chuyển dần sang các đường nằm ngang khi dòng chảy rối hoàn toàn."))
    b.append(fig(16, F.fig(16), "vi"))
    b.append(fig(17, F.fig(17), "vi"))
    b.append(p(
        "Phân tích tương tự rotameter cho phép tính dễ dàng số đọc lưu lượng khi khối lượng riêng và "
        "độ nhớt của chất lưu thay đổi. Với độ nhớt thấp hơn, chỉ cần kể đến ảnh hưởng của khối lượng "
        "riêng; do đó với phần lớn phép đo khí có thể dùng các hệ số chuyển đổi đơn giản. Với độ nhớt "
        "cao hơn, nhà sản xuất cung cấp hoặc hệ số chuyển đổi gắn với số Ruppel, hoặc bảng hệ số "
        "chuyển đổi hai chiều áp dụng cho các độ cao khác nhau của phao. Một số nhà sản xuất có dịch "
        "vụ hiệu chuẩn lại, cho phép người dùng đặt thang mới cho thiết bị sẽ dùng trong ứng dụng và "
        "môi trường đã thay đổi. Với khách hàng mua số lượng lớn, một số nhà sản xuất cung cấp chương "
        "trình máy tính đơn giản để tính thang đo."))
    b.append(p(
        "Các lý thuyết dựa trên lập luận tương tự có thể dự báo sự thay đổi của hệ số lưu lượng theo "
        "số Ruppel trong chế độ chảy tầng và chảy rối, nhưng không dự báo được ở vùng chuyển tiếp "
        "tầng–rối. Các nghiên cứu thực nghiệm và tính toán chi tiết có thể hỗ trợ phân tích dòng chảy "
        "của lưu lượng kế phần tử nổi. Một ví dụ được trình bày ở mục “Rotameter: phân tích dòng chảy "
        "bên trong”."))

    b.append(h4("Đập tràn và máng: phân tích lưu lượng", "Weir, Flume: Flow Rate Analysis"))
    b.append(p(
        "Mặc dù việc xác định lưu lượng qua một đập tràn hay máng nói chung đòi hỏi phải biết một "
        "hoặc nhiều hệ số thực nghiệm, các phương trình cơ bản mô tả đặc tính cột nước–lưu lượng của "
        "những dạng hình học khác nhau có thể suy ra dễ dàng từ những lập luận cơ học chất lưu đơn "
        "giản."))
    b.append(p(
        "Lưu lượng qua một đập tràn thành mỏng rộng <i>b</i> (Hình 28.11) khi mực nước trên ngưỡng là "
        "<i>h</i> được phân tích bằng cách xét một dải nước nằm ngang dày δ<i>y</i> ở độ sâu <i>y</i> "
        "dưới mặt nước. Vì vận tốc của nước qua dải này là √(2<i>gy</i>), lưu lượng qua dải là:"))
    b.append(eq("δQ̇ = bδy√(2gy)", "28.26"))
    b.append(p("Lưu lượng toàn phần thu được bằng tích phân, có đưa vào hệ số lưu lượng <i>C</i><sub>d</sub>:"))
    b.append(eq("Q̇ = C<sub>d</sub>√(2g)·b∫₀ʰ √y dy", "28.27"))
    b.append(eq("Q̇ = (2/3)C<sub>d</sub>√(2g)·bh<sup>3/2</sup>", "28.28"))
    b.append(p(
        "Các hiệu chỉnh thực nghiệm cho Phương trình 28.28 để kể đến chiều cao đập tràn <i>p</i> được "
        "nêu, ví dụ, trong [3]; nhưng miễn là <i>h</i>/<i>p</i> không vượt quá 0,5 thì dùng Phương "
        "trình 28.28 với hệ số lưu lượng 0,63 là đủ để đạt dung sai lưu lượng 3 %."))
    b.append(p(
        "Với cửa tràn chữ nhật, Phương trình 28.28 cũng áp dụng được với hệ số lưu lượng 0,59 và dung "
        "sai lưu lượng 3 %. Vì trên thực tế hệ số lưu lượng thay đổi chút ít theo cột nước với cả đập "
        "tràn lẫn cửa tràn, đôi khi người ta thích thay Phương trình 28.28 bằng Q̇ = <i>Kbh</i><sup>n</sup>, "
        "trong đó <i>K</i> và <i>n</i> được xác định bằng hiệu chuẩn."))
    b.append(p(
        "Cửa tràn tam giác (Hình 28.13) có ưu điểm là chiều dài mép ướt thay đổi theo cột nước, ngược "
        "với cửa tràn chữ nhật nơi chiều dài này không đổi. Do đó hệ số lưu lượng của cửa tràn tam "
        "giác là hằng số với mọi cột nước. Hơn nữa, dải đo đạt được (tỉ số lưu lượng cực đại trên cực "
        "tiểu) của dạng tam giác lớn hơn. Nếu <i>h</i> là chiều cao mặt nước và θ là góc của cửa tràn, "
        "thì một dải ngang của cửa tràn dày δ<i>y</i> ở độ sâu <i>y</i> có chiều rộng "
        "2(<i>h</i> − <i>y</i>)tan(θ/2). Lưu lượng qua dải này là:"))
    b.append(eq("δQ̇ = 2(h − y)tan(θ/2)δy√(2gy)·C<sub>d</sub>", "28.29"))
    b.append(p("cho lưu lượng toàn phần qua cửa tràn:"))
    b.append(eq("Q̇ = 2C<sub>d</sub>√(2g)·tan(θ/2)∫₀ʰ (h − y)√y dy", "28.30"))
    b.append(eq("Q̇ = (8/15)C<sub>d</sub>√(2g)·tan(θ/2)·h<sup>5/2</sup>", "28.31"))
    b.append(p("Hệ số lưu lượng vào khoảng 0,58."))
    b.append(p(
        "Các góc cửa tràn thường dùng là 90° (tan θ/2 = 1; <i>C</i><sub>d</sub> = 0,578), 53,13° "
        "(tan θ/2 = 0,5; <i>C</i><sub>d</sub> = 0,577) và 28,07° (tan θ/2 = 0,25; <i>C</i><sub>d</sub> "
        "= 0,587). Cửa tràn có θ = 53,13° và θ = 28,07° cho lưu lượng tương ứng bằng một nửa và một "
        "phần tư lưu lượng của cửa tràn 90° ở cùng cột nước."))
    b.append(p(
        "Các suy dẫn trên giả thiết nước chảy ra từ một hồ chứa có diện tích mặt cắt lớn hơn nhiều "
        "diện tích dòng chảy tại đập tràn, sao cho vận tốc thượng lưu không đáng kể. Khi đập tràn được "
        "xây trong một kênh có diện tích mặt cắt <i>A</i>, nước sẽ có vận tốc tới hữu hạn "
        "<i>v</i>₁ = Q̇/<i>A</i>. Ở mức xấp xỉ đầu tiên, Q̇ thu được từ Phương trình 28.28 với giả thiết "
        "vận tốc tới bằng không. Giả thiết thêm rằng <i>v</i>₁ phân bố đều trên đập tràn, sẽ có thêm "
        "một cột nước <i>v</i>₁²/2<i>g</i> tác dụng trên toàn bộ đập tràn. Theo Hình 28.11, lưu lượng "
        "toàn phần khi đó là:"))
    b.append(eq("Q̇ = C<sub>d</sub>√(2g)·b∫<sub>v₁²/2g</sub><sup>h+v₁²/2g</sup> √y dy", "28.32"))
    b.append(eq("Q̇ = (2/3)C<sub>d</sub>√(2g)·b[(h + v₁²/2g)<sup>3/2</sup> − (v₁²/2g)<sup>3/2</sup>]", "28.33"))
    b.append(p(
        "Từ Phương trình 28.33 có thể xác định một giá trị hiệu chỉnh của <i>v</i>₁. Các lần lặp tiếp "
        "theo hội tụ nhanh tới giá trị cuối cùng của lưu lượng Q̇. Phương trình 28.33 có thể viết là:"))
    b.append(eq("Q̇ = (2/3)C<sub>v</sub>C<sub>d</sub>√(2g)·bh<sup>3/2</sup>", "28.34"))
    b.append(p("trong đó"))
    b.append(eq("C<sub>v</sub> = (1 + v₁²/2gh)<sup>3/2</sup> − (v₁²/2gh)<sup>3/2</sup>", "28.35"))
    b.append(p("là hệ số vận tốc, thường được xác định bằng thực nghiệm."))
    b.append(p(
        "Qua một đập tràn đỉnh rộng (Hình 28.14), lưu lượng phụ thuộc cột nước <i>h</i>₁, chiều rộng "
        "<i>b</i> và chiều dài <i>l</i> của ngưỡng. Lưu lượng còn phụ thuộc độ nhám bề mặt ngưỡng và "
        "độ nhớt. Do đó có tổn thất cột nước khi nước chảy qua ngưỡng. Người ta giả thiết ngưỡng đủ "
        "dài để vận tốc phân bố đều với giá trị <i>v</i> trên suốt độ sâu <i>h</i>₂ của nước ở mép hạ "
        "lưu của ngưỡng. Bỏ qua tổn thất:"))
    b.append(eq("v = √[2g(h₁ − h₂)]", ""))
    b.append(p("và lưu lượng là:"))
    b.append(eq("Q̇ = C<sub>d</sub>bh₂v = C<sub>d</sub>b√[2g(h₁h₂² − h₂³)]", "28.36"))
    b.append(p(
        "Từ Phương trình 28.36, lưu lượng đạt cực đại khi (<i>h</i>₁<i>h</i>₂² − <i>h</i>₂³) đạt cực "
        "đại, tức khi <i>h</i>₂ = 2<i>h</i>₁/3. Lưu lượng khi đó là:"))
    b.append(eq("Q̇ = (2/3)<sup>3/2</sup>C<sub>d</sub>b√g·h₁<sup>3/2</sup>", "28.37"))
    b.append(p("Trạng thái ổn định của đập tràn nằm ở lưu lượng cực đại."))
    b.append(p(
        "<b>Phân tích lưu lượng cho máng.</b> Lưu lượng qua một máng phụ thuộc mực nước <i>h</i>, "
        "chiều rộng kênh <i>b</i> và vận tốc <i>v</i> tại mỗi mặt cắt 1 (thượng lưu) và 2 (tại tiết "
        "diện nhỏ nhất) trên Hình 28.15. Áp dụng phương trình Bernoulli cho lối vào và họng máng, bỏ "
        "qua mọi tổn thất, ta được:"))
    b.append(eq("ρgH = ρgh₁ + ½ρv₁² = ρgh₂ + ½ρv₂²", "28.38"))
    b.append(p(
        "trong đó <i>H</i> là cột nước toàn phần. Phân tích sau đó về hình thức giống hệt phân tích "
        "cho đập tràn đỉnh rộng, cho cùng biểu thức lưu lượng như Phương trình 28.37. Dòng qua máng "
        "đạt cực đại khi độ sâu tại họng bằng hai phần ba cột nước toàn phần. Thông thường người ta "
        "đưa vào một hệ số vận tốc để phương trình lưu lượng trở thành:"))
    b.append(eq("Q̇ = (2/3)<sup>3/2</sup>C<sub>v</sub>C<sub>d</sub>b√g·h₁<sup>3/2</sup>", "28.39"))
    b.append(p(
        "Hệ số tổ hợp được xác định bằng thực nghiệm. Trong [3] có nêu giá trị "
        "<i>C</i><sub>v</sub><i>C</i><sub>d</sub> = 1,061 − 0,085."))
    b.append(p(
        "Tính đúng đắn của các hệ số thực nghiệm nêu trên, hoặc của các hệ số khác cho trong các tiêu "
        "chuẩn về đo lưu lượng kênh hở, chỉ có thể bảo đảm với một mức tin cậy nhất định khi hệ đo "
        "thoả mãn những ràng buộc hình học nhất định. Các giới hạn về những đại lượng như <i>b</i>, "
        "<i>h</i>, <i>h</i>/<i>b</i>, v.v. được nêu trong [3] và trong các tiêu chuẩn."))

    b.append(h4("Rotameter: phân tích dòng chảy bên trong",
                "Rotameter: Internal Flow Analysis"))
    b.append('<p style="font-weight:650;margin:1.4rem 0 .45rem">Tính toán dòng chảy bên trong. '
             '<span class="en">Computation of Internal Flow.</span></p>')
    b.append(p(
        "Việc cải tiến thiết kế rotameter có thể được hỗ trợ nhờ hiểu biết chi tiết trường dòng bên "
        "trong — nơi đặc trưng bởi gradient vận tốc rất dốc và các vùng dòng tách. Việc đo trường dòng "
        "bên trong gặp khó khăn vì kích thước khe quanh phao nhỏ và thành ống thuỷ tinh cong mạnh. "
        "Bückle và cộng sự [13] đã dùng thành công phép đo vận tốc bằng laser Doppler [14] cho một "
        "rotameter. Chất lưu làm việc là dung dịch glycerin có chiết suất (1,455) gần với chiết suất "
        "của thuỷ tinh (1,476). Nhờ vậy tránh được vấn đề khúc xạ tia laser tại thành ống cong, nhưng "
        "độ nhớt cao của glycerin hạn chế thí nghiệm ở chế độ chảy tầng với số Reynolds "
        "<i>Re</i> = ρ<i>U</i><sub>IN</sub><i>D</i><sub>b</sub>/μ &lt; 400."))
    b.append(p(
        "Việc áp dụng động lực học chất lưu tính toán cho dòng chảy trong rotameter [13] bao gồm việc "
        "giải bằng thể tích hữu hạn các phương trình bảo toàn khối lượng và động lượng. Với dòng chảy "
        "tầng hai chiều, các phương trình này có thể viết trong hệ toạ độ trụ cực như sau:"))
    b.append(eq("∂ρ/∂t + ∂(ρu)/∂z + (1/r)·∂(ρrv)/∂r = 0", "28.40"))
    b.append(eq("∂(ρu)/∂t + ∂/∂z(ρuu − 2μ∂u/∂z) + (1/r)·∂/∂r[ρruv − μr(∂u/∂r + ∂v/∂z)] = −∂p/∂z", "28.41"))
    b.append(eq("∂(ρv)/∂t + ∂/∂z[ρuv − μ(∂u/∂r + ∂v/∂z)] + (1/r)·∂/∂r(ρrvv − 2μr∂v/∂r) = −∂p/∂r", "28.42"))
    b.append(p(
        "trong đó ρ là khối lượng riêng, <i>u</i>, <i>v</i> và <i>r</i>, <i>z</i> là các thành phần vận "
        "tốc và các hướng toạ độ theo phương trục và phương bán kính, μ là độ nhớt động lực, và "
        "<i>p</i> là áp suất."))
    b.append(p(
        "Để giải số, các phương trình chủ đạo cho một biến vận chuyển tổng quát φ (tức <i>u</i> hoặc "
        "<i>v</i>) được tích phân hình thức trên từng thể tích kiểm soát của lưới tính. Phương trình "
        "cân bằng thông lượng thu được lại có thể rời rạc hoá thành một phương trình đại số cho φ tại "
        "tâm P của mỗi thể tích kiểm soát, theo các giá trị φ<sub>nb</sub> tại bốn điểm lân cận gần "
        "nhất của điểm P và các hàm đã biết <i>A</i>:"))
    b.append(eq("A<sub>P</sub>φ<sub>P</sub> + Σ<sub>nb</sub>A<sub>nb</sub>φ<sub>nb</sub> = S<sub>φ</sub>", "28.43"))
    b.append(p(
        "Với toàn miền nghiệm, ta thu được một hệ phương trình có thể giải bằng một thuật toán thích "
        "hợp (ví dụ [15])."))
    b.append(p(
        "Với rotameter, tính đối xứng của bài toán cho phép chọn miền tính là một nửa mặt phẳng qua "
        "trục. Các điều kiện biên là:"))
    b.append(eq("u = v = 0", "28.44"))
    b.append(p("dọc theo thành, và"))
    b.append(eq("∂u/∂r = v = 0", "28.45"))
    b.append(p(
        "dọc theo trục đối xứng. Tại biên lối vào, mặt cắt ban đầu của thành phần vận tốc <i>u</i> "
        "được lấy từ thực nghiệm. Tại biên lối ra, giả thiết gradient bằng không với mọi biến phụ "
        "thuộc."))
    b.append('<p style="font-weight:650;margin:1.4rem 0 .45rem">Trường dòng tính được. '
             '<span class="en">Computed Flow Field.</span></p>')
    b.append(p(
        "Các tính toán đại diện cho số Reynolds 220 được trình bày dưới dạng vectơ vận tốc (Hình "
        "28.18) và đường dòng (Hình 28.19). Các mặt cắt vận tốc đo được và tính được trên một bán "
        "kính của ống lưu lượng kế được so sánh trên Hình 28.20."))
    b.append(fig(18, F.fig(18), "vi"))
    b.append(fig(19, F.fig(19), "vi"))
    b.append(fig(20, F.fig(20), "vi"))
    b.append(p(
        "Tại <i>z</i> = 45 mm, kết quả tính cho thấy một điểm dừng tại mũi phao, nhưng phép đo cho một "
        "vận tốc trục nhỏ nhưng hữu hạn. Độ lệch khỏi giá trị không là do vị trí phao hơi không ổn "
        "định và do gradient vận tốc hướng tâm rất dốc bị làm nhoè trên thể tích đo. Hiệu ứng này "
        "cũng thấy rõ ở các bán kính tới khoảng 5 mm, nơi kết quả tính cho gradient vận tốc dốc hơn "
        "hẳn so với phép đo. Vận tốc đỉnh đo được và tính được khớp tốt với nhau, dù đỉnh đo được nằm "
        "ở bán kính lớn hơn."))
    b.append(p(
        "Trong vành khuyên hội tụ mạnh giữa phao và thành ống (<i>z</i> = 65 mm) và trên mặt phẳng "
        "<i>z</i> = 88 mm, kết quả tính tái hiện tốt xu hướng của kết quả đo, đặc biệt gần thành lưu "
        "lượng kế. Sự khác biệt trong vùng sát phao là do mặt cắt đo bị bất đối xứng vì đoạn ống nối "
        "phía thượng lưu ống rotameter."))
    b.append(p(
        "Phía trên phao (<i>z</i> = 110 mm) có một dòng hướng lên mạnh trong vùng vành khuyên sát thành "
        "ống và một vùng tuần hoàn quanh trục chiếm gần nửa mặt cắt ống. Các vận tốc thuận chiều khớp "
        "tốt giữa tính toán và đo đạc, nhưng có sự khác biệt rất rõ trong vùng tuần hoàn. Tại "
        "<i>z</i> = 135 mm, vùng tuần hoàn đã kết thúc nhưng vệt xoáy sau phao vẫn còn rất rõ. Ngoài "
        "sai lệch khoảng 10 % trên trục, kết quả của hai phương pháp khớp nhau đáng kể."))
    b.append(p(
        "Ảnh hưởng của chuyển động quay của phao lên trường dòng được xét bằng tính toán có kể thêm "
        "phương trình cho thành phần vận tốc phương vị <i>w</i>."))
    b.append(eq("∂(ρw)/∂t + ∂/∂z(ρuw − μ∂w/∂z) + (1/r)·∂/∂r[ρrvw − μr∂w/∂r] = −ρvw/r − μw/r²", "28.46"))
    b.append(p(
        "Các tính toán với tần số quay 1 Hz cho thấy vận tốc xoáy lớn nhất ở gần trục, phía trên phao. "
        "Không thấy ảnh hưởng rõ rệt của chuyển động quay lên các thành phần vận tốc <i>u</i> và "
        "<i>v</i> [16]."))

    b.append(h3("Tóm tắt", "Summary"))
    b.append(p(
        "Với dòng chảy trong ống, lưu lượng kế biến diện tích phù hợp nhất cho lưu lượng nhỏ của khí "
        "hoặc chất lỏng ở nhiệt độ và áp suất vừa phải. Các ưu điểm gồm kết cấu chắc chắn, độ tin cậy "
        "cao, tổn thất áp suất thấp, lắp đặt dễ và giá thành thấp. Nhược điểm gồm độ bất định đo từ "
        "1 % trở lên, dải đo hạn chế (10:1), đáp ứng chậm và hạn chế về hướng đặt thiết bị. Tỉ số "
        "giá/hiệu năng nói chung tốt đã khiến loại lưu lượng kế này được dùng rộng rãi trong nhiều "
        "dụng cụ khoa học và y tế, và trong nhiều ứng dụng công nghiệp để theo dõi lưu lượng."))
    b.append(p(
        "Lưu lượng kế biến diện tích dùng cho dòng chảy hở có ứng dụng đo lưu lượng ở nhà máy xử lý "
        "nước thải, nhà máy nước, sông suối, hệ thống tưới tiêu và kênh thoát nước. Các ứng dụng thuỷ "
        "văn của đập tràn có ngưỡng hay đỉnh điều chỉnh được gồm điều tiết lưu lượng, đo lưu lượng, "
        "kiểm soát mực nước thượng lưu và xả lưu lượng dư trên sông suối, kênh mương. Sự chắc chắn, "
        "đơn giản và chi phí bảo trì thấp là những đặc tính thuận lợi cho việc dùng các lưu lượng kế "
        "này ngoài hiện trường."))

    b.append(h3("Tài liệu tham khảo", "References"))
    b.append(wl([
        "1. R. A. Furness, BS7045: the principles of flowmeter selection, <i>Flow Meas. Instrum.</i>, "
        "2, 233–242, 1991.",
        "2. W. Boiten, Flow-measuring structures, <i>Flow Meas. Instrum.</i>, 4, 17–24, 1993.",
        "3. R. Hershey, General purpose flow measurement equations for flumes and thin plate weirs, "
        "<i>Flow Meas. Instrum.</i>, 6, 283–293, 1995.",
        "4. ISO 1438, <i>Thin Plate Weirs</i>, International Standards Organisation, Geneva, 1980.",
        "5. ISO 4359, <i>Rectangular, Trapezoidal and U-shaped Flumes</i>, International Standards "
        "Organisation, Geneva, 1983.",
        "6. ISO 8368, <i>Guidelines for the Selection of Flow Gauging Structures</i>, International "
        "Standards Organisation, Geneva, 1985.",
        "7. G. Ruppel and K. J. Umpfenbach, Strömungstechnische Untersuchungen an Schwimmermessern, "
        "<i>Technische Mechanik und Thermodynamik</i>, 1, 225–233, 257–267, 290–296, 1930.",
        "8. K. Lutz, Die Berechnung des Schwebekörper-Durchflußmessers, <i>Regelungstechnik</i>, 10, "
        "355–360, 1959.",
        "9. D. Bender, Ähnlichkeitsparameter und Durchflußgleichungen für "
        "Schwebekörperdurchflußmesser, <i>ATM-Archiv für Technisches Messen</i>, 391, 97–102, 1968.",
        "10. VDE/VDI-Fachgruppe Meßtechnik 3513, <i>Schwebekörperdurchflußmesser, "
        "Berechnungsverfahren</i>, VDE/VDI 3513, 1971.",
        "11. H. Nikolaus, Berechnungsverfahren für Schwebekörperdurchflußmesser, theoretische "
        "Grundlagen und Aufbereitung für die Datenverarbeitungsanlage, <i>ATM-Archiv für Technisches "
        "Messen</i>, 435, 49–55, 1972.",
        "12. H. Nikolaus and M. Feck, Graphische Verfahren zur Bestimmung von Durchflußkennlinien für "
        "Schwebekörperdurchflußmeßgeräte, <i>ATM-Archiv für Technisches Messen</i>, 1247-5, 171–176, "
        "1974.",
        "13. U. Bückle, F. Durst, B. Howe, and A. Melling, Investigation of a floating element flow "
        "meter, <i>Flow Meas. Instrum.</i>, 3, 215–225, 1992.",
        "14. F. Durst, A. Melling, and J. H. Whitelaw, <i>Principles and Practice of Laser-Doppler "
        "Anemometry</i>, 2nd ed., London: Academic Press, 1981.",
        "15. M. Perić, M. Schäfer, and E. Schreck, Computation of fluid flow with a parallel multigrid "
        "solver, <i>Proc. Conf. Parallel Computational Fluid Dynamics</i>, Stuttgart, 1991.",
        "16. U. Bückle, F. Durst, H. Köchner, and A. Melling, Further investigation of a floating "
        "element flowmeter, <i>Flow Meas. Instrum.</i>, 6, 75–78, 1995.",
    ]))
    return "".join(b)


def sec_28_2_en():
    b = []
    b.append(h2("28.2 Variable Area Flowmeters", "Lưu lượng kế biến diện tích"))
    b.append(p("Adrian Melling, Herbert Köchner and Reinhard Haak — Universität Erlangen-Nürnberg."))
    b.append(p(
        "The term <b>variable area flowmeters</b> refers to those meters in which the minimum "
        "cross-sectional area available to the flow through the meter varies with the flow rate. "
        "Meters of this type discussed in this section include the rotameter and the movable vane "
        "meter used in pipe flows, and the weir or flume used in open-channel flows. The measure of "
        "the flow rate is a geometrical quantity such as the height of a bob in the rotameter, the "
        "angle of the vane, or the change in height of the free surface of the liquid flowing over "
        "the weir or through the flume."))
    b.append(p(
        "Most of the discussion here is devoted to the rotameter, firstly because the number of "
        "installed rotameters and movable vane meters is large relative to the number of weirs and "
        "flumes, and secondly because the movable vane is often used simply as a flow indicator "
        "rather than as a meter."))
    b.append(p(
        "The following section includes basic information describing the main constructional "
        "features and applications of each type of meter. In the third section, the principles of "
        "measurement and design of rotameters and open-channel meters are described in some detail; "
        "the movable vane meter is not considered further because most design aspects are similar "
        "to those of rotameters. Then, the contribution of modern computational and experimental "
        "methods of fluid mechanics to flowmeter design is discussed, using the results of a "
        "detailed investigation of the internal flow."))
    b.append(p(
        "Details of manufacturers of rotameters and movable vane meters, together with approximate "
        "costs of these meters, are also tabulated in Tables 28.5 through 28.7."))

    b.append(h3("General Description of Variable Area Flowmeters", "Mô tả chung lưu lượng kế biến diện tích"))

    b.append(h4("Rotameter"))
    b.append(p(
        "The rotameter is a robust and simple flowmeter for gases and liquids, and holds a large "
        "share of the market for pipe diameters smaller than about 100 mm. In its basic form, the "
        "rotameter consists of a conical transparent vertical glass tube containing a “bob” (Figure "
        "28.7), which rises in the tube with increasing flow rate until a balance is reached between "
        "gravitational, buoyancy, and drag forces on the bob. Within the range of a particular "
        "flowmeter (depending on the bob shape and density, the tube shape and the fluid density and "
        "viscosity), the flow rate is linearly proportional to the height of the bob in the tube and "
        "is determined simply by reading the level of the upper edge of the bob. The rotameter is "
        "also known as “floating element flowmeter,” although the buoyancy force on the “floating "
        "element” is not sufficient to make it float."))
    b.append(fig(7, F.fig(7), "en"))
    b.append(p(
        "The bob is commonly formed of a combination of cylindrical and conical sections, but a "
        "spherical bob is often used in small diameter tubes (see Figure 28.8). More complicated bob "
        "geometries can reduce the sensitivity to viscosity of the fluid. Frequently, the bob has "
        "several shallow inclined grooves around the upper rim that induce a slow rotation (frequency "
        "about 1 Hz) of the bob, which helps to maintain a stable position of the bob. In larger "
        "rotameters where the additional friction is acceptable, the bob can be allowed to slide up "
        "and down a rod on the tube axis to prevent any sideways motion."))
    b.append(fig(8, F.fig(8), "en"))
    b.append(p(
        "Various tube geometries are in use. The basic requirement for an increase in the "
        "cross-sectional area up the height of the tube leads to the conical tube. An alternative "
        "form uses three ribs arranged circumferentially around the tube to guide the bob; the flow "
        "area between the ribs increases along the tube height. For spherical bobs, a triangular tube "
        "in which the bob remains in contact with three surfaces over the whole height of the tube "
        "prevents lateral movement of the bob with minimum friction. Commonly, the tube is made of "
        "glass to facilitate the reading of the flow rate from a scale engraved on the tube. For "
        "general-purpose applications, the scale can be marked in millimeters; the flow rate is then "
        "determined by a conversion factor depending on the tube dimensions, the mass of the bob, the "
        "pressure and temperature, and the properties of the fluid. For specific application to a "
        "single fluid under controlled conditions, it is more convenient to have the flow rate "
        "directly marked on the tube."))
    b.append(p(
        "For laboratory use, medical equipment, and other applications with small flow rates, the "
        "glass tube is almost universal. Laboratory meters are often equipped with a flow valve that "
        "allows direct flow setting and reading. For many small rotameters, integrated flow "
        "controllers are offered; these hold the pressure drop and the flow setting constant, even "
        "with changing upstream or downstream pressure."))
    b.append(p(
        "For most rotameters, electric limit switches or analog electric signal transducers are "
        "available. For glass and plastic meters, inductive or optical switches are used that can be "
        "positioned to the desired level of the bob. While some units just detect the bob within "
        "their active area, other switches have bistable operation, wherein the switch is toggled by "
        "the float passing the switch."))
    b.append(p(
        "For industrial applications, the metering of corrosive fluids or fluids at high temperature "
        "or pressure leads to the use of stainless steel tubes or a wide range of other materials "
        "chosen to suit the application requirements (e.g., temperature, pressure, corrosion). Most "
        "metal rotameters use a permanent magnetic coupling between the float and the pointer of the "
        "indicator, enabling a direct analog flow reading without electric supply. Electric switches "
        "can, however, be added to the indicator, and electric and pneumatic transmitters for the "
        "flow reading are offered by most producers. Some units are equipped with options such as "
        "flow totalizers, mass flow calculation units for gas applications in conjunction with "
        "temperature and pressure sensors, or energy calculation units. Due to the frequent "
        "application of the rotameter in the chemical and petrochemical industry, electric options "
        "are often designed for use in hazardous areas."))
    b.append(p("The rotameter is characterized by:"))
    b.append(ul([
        "Simple and robust construction",
        "High reliability",
        "Low pressure drop",
        "Applicable to a wide variety of gases and liquids",
        "Flow range typically 0.04 L h⁻¹ to 150 m³ h⁻¹ for water",
        "Flow range typically 0.5 L h⁻¹ to 3000 m³ h⁻¹ for air",
        "10:1 flow range for a given bob-tube combination",
        "Uncertainty 0.4% to 4% of maximum flow",
        "Insensitivity to nonuniformity in the inflow (no upstream straight piping needed)",
        "Typical maximum temperature 400 °C",
        "Typical maximum pressure 4 MPa (40 bar)",
        "Low investment cost",
        "Low installation cost",
    ]))
    b.append(table(*_t285("en")))
    b.append(table(*_t287("en")))

    b.append(h4("Movable Vane Meter", "Lưu lượng kế cánh quay"))
    b.append(p(
        "The movable vane meter is a robust device suitable for the measurement of high flow rates "
        "where only moderate requirements on the measurement accuracy are made. Dirty fluids can also "
        "be metered. It contains a flap that at zero flow is held closed by a weight or a spring "
        "(Figure 28.9). A flow forces the vane open until the dynamic force of the flow is in balance "
        "with the restoring force of the weight or the spring. The angle of the vane is thus a "
        "measure of the flow rate, which can be directly indicated by a pointer attached to the shaft "
        "of the vane on a calibrated scale. The resistance provided by the vane depends on the vane "
        "position and hence on the flow rate or Reynolds number; a recalibration is therefore "
        "necessary when the fluid is changed. An important application is the metering of the air "
        "flow in automotive engines with fuel injection."))
    b.append(fig(9, F.fig(9), "en"))
    b.append(p(
        "In low-cost flow indicators, a glass or plastic window allows a direct view of the flap "
        "(Figure 28.10). Sometimes, optical or reed switches in combination with a permanent magnet "
        "attached to the flap are used as electric flow switches. All-metal units use a magnetic "
        "coupling between the vane and the pointer of the indicator, thus avoiding most of the "
        "friction and material selection problems. Many applications use the movable vane meter as a "
        "flow switch with appropriate mechanical, magnetic, inductive, or optical switches. The "
        "setting of the switch is done once for all during the installation. Since a continuous flow "
        "indication is not needed, flow reading uncertainties are not of concern."))
    b.append(fig(10, F.fig(10), "en"))
    b.append(p(
        "Most aspects of design and application of rotameters can be applied to movable vane meters, "
        "although the latter are characterized by a higher uncertainty of the flow reading. General "
        "features of both types of variable area flowmeter are summarized, for example, in reference "
        "[1]. Since the basic construction of the two meter types is very similar, the unit costs "
        "also lie in the same range."))
    b.append(table(*_t286("en")))

    b.append(h4("Weir, Flume", "Đập tràn, máng"))
    b.append(p(
        "Of the methods available for the metering of a liquid (generally water) in open-channel "
        "flow, the weir and the flume fall within the scope of this discussion on variable area "
        "flowmeters. In each case, the flow metering depends on measurement of the difference in "
        "height <i>h</i> of the water surface over an obstruction across the channel and the surface "
        "sufficiently far upstream. There is a wide variety of geometries in use (see reference [2]), "
        "but most of these can be described as variants of three basic types. In the <b>sharp "
        "crested weir</b>, also known as the thin plate weir (Figure 28.11), the sill or crest is "
        "only about 1 mm to 2 mm thick. The sheet of liquid flowing over the weir, called the "
        "<i>nappe</i> or <i>vein</i>, separates from the weir body after passing over the crest. An "
        "air-filled zone at atmospheric pressure is formed underneath the outflowing jet, and the "
        "streamlines above the weir are strongly curved. If the width of the weir is less than that "
        "of the upstream channel (Figures 28.12 and 28.13), the term “notch” is frequently used. A "
        "<b>broad crested weir</b> (Figure 28.14) has a sill which is long enough for straight, "
        "parallel streamlines to form above the crest. In this review, the term “weir” is applied "
        "generally to both the weir and the notch."))
    b.append(fig(11, F.fig(11), "en"))
    b.append(p(
        "The resistance to flow introduced by the weir causes the water level upstream to rise. If it "
        "is assumed that the flow velocity some distance upstream of the weir is zero, then a simple "
        "measure of the upstream water level suffices to determine the discharge over a weir of known "
        "geometry. As in the case of an orifice in pipe flow, there will be a contraction of the "
        "nappe and a frictional resistance at the sides as water flows over a weir. The actual "
        "discharge is less than the theoretical discharge according to an empirically determined "
        "coefficient of discharge <i>C</i><sub>d</sub>. In the analysis of rectangular notches and "
        "weirs, it is frequently assumed that the channel width remains constant so that a "
        "contraction of the nappe occurs only in the vertical direction as the water accelerates over "
        "the obstacle. When the weir is narrower than the upstream channel, there is an additional "
        "horizontal contraction. The effect of a significant upstream velocity is accounted for "
        "empirically."))
    b.append(fig(12, F.fig(12), "en"))
    b.append(fig(13, F.fig(13), "en"))
    b.append(fig(14, F.fig(14), "en"))
    b.append(p(
        "As an alternative to the weir, the <b>flume</b> (Figure 28.15) provides a method for flow "
        "metering with relatively low pressure loss. By restricting the channel width, analogous to "
        "the Venturi tube used in pipe flow, the flow velocity in the narrow portion of the channel is "
        "increased and the water level sinks accordingly. Most of the head of water is recovered in "
        "the diffusing section of the flume. The water levels upstream and in the throat of the flume "
        "can be determined by simple floats and recorded on a chart by pens driven mechanically from "
        "the floats. For remote monitoring, the use of echo sounders is advantageous."))
    b.append(fig(15, F.fig(15), "en"))
    b.append(p(
        "The weir is preferentially used in natural river beds and the flume in canalized water "
        "courses. The flume must be used in streams with sediment transport to avoid the accumulation "
        "of deposits that would occur at the approach to a weir. Weirs and flumes are characterized "
        "by:"))
    b.append(ul([
        "Simple measurement of the water level",
        "Simple maintenance",
        "Reliable measurement of large flow rates at low stream velocity",
        "Limited measurement accuracy (at best about 2%)",
        "High installation costs, particularly for flumes",
    ]))
    b.append(p(
        "Recommendations for installation of weirs and flumes, for the location of the head measuring "
        "station upstream, and for determining the discharge from the measured head are given, for "
        "example, in [2] and [3] as well as in appropriate standards (e.g., [4–6])."))

    b.append(h3("Measuring Principles of Variable Area Flowmeters",
                "Nguyên lý đo của lưu lượng kế biến diện tích"))

    b.append(h4("Rotameter: Flow Rate Analysis", "Rotameter: phân tích lưu lượng"))
    b.append(p(
        "The forces acting on the bob lead to equilibrium between the weight of the bob "
        "ρ<sub>b</sub><i>gV</i><sub>b</sub> acting downwards and the buoyancy force "
        "ρ<i>gV</i><sub>b</sub> and the drag force <i>F</i><sub>d</sub> acting upwards, where "
        "<i>V</i><sub>b</sub> is the volume and ρ<sub>b</sub> is the density of the bob, ρ is the "
        "density of the fluid, and <i>g</i> is the gravitational acceleration:"))
    b.append(eq("ρ<sub>b</sub>gV<sub>b</sub> = ρgV<sub>b</sub> + F<sub>d</sub>", "28.7"))
    b.append(p(
        "The drag force results from the flow field surrounding the bob and particularly from the "
        "wake of the bob. In flow analyses based on similarity principles, these influences are "
        "accounted for by empirical coefficient <i>C</i><sub>L</sub> or <i>C</i><sub>T</sub> in the "
        "drag law for:"))
    b.append(eq('<span style="font-style:italic;margin-right:1.4rem">laminar flow</span>'
                'F<sub>d</sub> = C<sub>L</sub>μD<sub>b</sub>U', "28.8"))
    b.append(eq('<span style="font-style:italic;margin-right:1.4rem">turbulent flow</span>'
                'F<sub>d</sub> = C<sub>T</sub>ρD<sub>b</sub>²U²', "28.9"))
    b.append(p(
        "where μ is the fluid viscosity, <i>D</i><sub>b</sub> is the maximum bob diameter, and "
        "<i>U</i> is the velocity in the annular gap around the bob at the minimum cross-section."))
    b.append(p("The volume flow rate through the rotameter is:"))
    b.append(eq("Q̇ = (π/4)(D² − D<sub>b</sub>²)U", "28.10"))
    b.append(p("or"))
    b.append(eq("Q̇ = m(π/4)D<sub>b</sub>²U", "28.11"))
    b.append(p("where <i>m</i> is the open area ratio, defined as:"))
    b.append(eq("m = (D² − D<sub>b</sub>²) / D<sub>b</sub>²", "28.12"))
    b.append(p("and <i>D</i> is the tube diameter at the height of the bob."))
    b.append(p("Combining Equations 28.7, 28.8, and 28.10 gives for laminar flow:"))
    b.append(eq("Q̇ = αD<sub>b</sub>⁴(ρ<sub>b</sub> − ρ)g / μ", "28.13"))
    b.append(p(
        "where the parameter α is defined in terms of a constant <i>K</i> = <i>V</i><sub>b</sub> / "
        "<i>D</i><sub>b</sub>³ characteristic of the shape of the bob:"))
    b.append(eq("α = πmK / (4C<sub>L</sub>)", "28.14"))
    b.append(p("Using Equation 28.9 instead of Equation 28.8 yields for turbulent flow:"))
    b.append(eq("Q̇ = βD<sub>b</sub><sup>5/2</sup>√[(ρ<sub>b</sub> − ρ)g / ρ]", "28.15"))
    b.append(p("where"))
    b.append(eq("β = (πm / 4)√(K / C<sub>T</sub>)", "28.16"))
    b.append(p(
        "With either laminar or turbulent flow through the rotameter, it is clear from Equations "
        "28.13 and 28.15 that the flow rate is proportional to <i>m</i>. If the cross-sectional area "
        "of the tube is made to increase linearly with length, i.e.,"))
    b.append(eq("D = D<sub>b</sub>(1 + h tan φ)", "28.17"))
    b.append(p(
        "then since the cone angle φ of the tube is small, Equation 28.12 can be written as:"))
    b.append(eq("m = 2h tan φ", "28.18"))
    b.append(p("and the flow rate is directly proportional to the height <i>h</i> of the bob."))

    b.append(h4("Similarity Analysis", "Phân tích tương tự"))
    b.append(p(
        "In early studies of floating element flowmeters, Ruppel and Umpfenbach [7] proposed the "
        "introduction of characteristic dimensionless quantities, to permit the use of "
        "experimentally determined flow coefficients in flowmeter analysis. Lutz [8] extended these "
        "ideas by showing that the transfer of flow coefficients from one flowmeter to another is "
        "possible if geometrical similarity exists. More recent works [9–12] have used these "
        "principles to produce graphical or computer-based design schemes and have proposed general "
        "guidelines for laying out practical flow metering systems."))
    b.append(p("The basic scaling parameter for flow is the Reynolds number, defined as:"))
    b.append(eq("Re = ρU<sub>IN</sub>D<sub>b</sub> / μ", "28.19"))
    b.append(p(
        "where <i>U</i><sub>IN</sub> is the velocity at the rotameter inlet, and the tube diameter "
        "<i>D</i> is represented by its value at the inlet, equal to the bob diameter "
        "<i>D</i><sub>b</sub>. Through the Reynolds number regimes of laminar or turbulent flow, and "
        "particularly important for the rotameter flow regimes with strong or weak viscosity "
        "dependence, can be distinguished. Originating in the work [7], it has been found to be "
        "practical for rotameters to use an alternative characteristic number, the Ruppel number, "
        "defined as:"))
    b.append(eq("Ru = μ / √[m<sub>b</sub>gρ(1 − ρ/ρ<sub>b</sub>)]", "28.20"))
    b.append(p(
        "where <i>m</i><sub>b</sub> = ρ<sub>b</sub><i>D</i><sub>b</sub>³ is the mass of the bob. By "
        "combining Equations 28.15, 28.16, and 28.20, the mass flow ṁ through the rotameter can be "
        "written as:"))
    b.append(eq("ṁ = (π/4)·mD<sub>b</sub>μ / (√C<sub>T</sub>·Ru)", "28.21"))
    b.append(p("Alternatively, from the definition:"))
    b.append(eq("ṁ = ρQ̇ = ρU<sub>IN</sub>(π/4)D<sub>b</sub>²", "28.22"))
    b.append(p("and Equation 28.19, the flow rate is:"))
    b.append(eq("ṁ = (π/4)D<sub>b</sub>μRe", "28.23"))
    b.append(p(
        "Equations 28.21 and 28.23 give the following relationship between the Ruppel number and the "
        "Reynolds number:"))
    b.append(eq("Ru = m / (√C<sub>T</sub>·Re)", "28.24"))
    b.append(p("An analysis for laminar flow leads to the relationship:"))
    b.append(eq("Ru = √(m / (C<sub>L</sub>Re))", "28.25"))
    b.append(p(
        "The advantage of the Ruppel number is its independence of the flow rate. Since the Ruppel "
        "number contains only fluid properties and the mass and the density of the bob, it is a "
        "constant for a particular instrument."))
    b.append(p(
        "At low Ruppel numbers the linear resistance law assumed in Equation 28.8 applies and α is a "
        "constant for given <i>m</i>, as shown in Figure 28.16. At higher Ruppel numbers, the flow is "
        "transitional or turbulent, and log α decreases linearly with log <i>Ru</i>. In Figure 28.17, "
        "curves for β against Ruppel number show a linear increase of log β with log <i>Ru</i> in the "
        "laminar region, followed by a gradual transition to horizontal curves in fully turbulent "
        "flow."))
    b.append(fig(16, F.fig(16), "en"))
    b.append(fig(17, F.fig(17), "en"))
    b.append(p(
        "Similarity analysis of rotameters allows the easy calculation of the flow reading with "
        "changing density and viscosity of the fluid. For lower viscosities, only the density effect "
        "has to be taken into account; hence, for most gas measurements, simple conversion factors "
        "can be used. With higher viscosity, manufacturers offer either Ruppel number-related "
        "conversion factors or two-dimensional tables of conversion factors to be applied to "
        "different heights of the bob. Some manufacturers offer recalibration services, allowing the "
        "user to order new scales for instruments to be used in changed applications and "
        "environments. For large-order users, simple computer programs are available from some "
        "manufacturers for scale calculations."))
    b.append(p(
        "Theories based on similarity considerations can predict the variation of the flow "
        "coefficient with the Ruppel number in the laminar and turbulent flow regimes but not in "
        "laminar-turbulent transitional flow. Detailed experimental and computational studies can "
        "assist the flow analysis of floating element flowmeters. An example is given in the section "
        "“Rotameter Internal Flow Analysis.”"))

    b.append(h4("Weir, Flume: Flow Rate Analysis", "Đập tràn và máng: phân tích lưu lượng"))
    b.append(p(
        "Although the determination of the discharge across a weir or a flume generally requires the "
        "knowledge of one or more empirical coefficients, the basic equations describing the "
        "head-discharge characteristics of the various geometrical forms are readily derived from "
        "simple fluid mechanics considerations."))
    b.append(p(
        "The discharge over a sharp crested weir of width <i>b</i> (Figure 28.11) when the water "
        "level over the sill is <i>h</i> is analyzed by considering a horizontal strip of water of "
        "thickness δ<i>y</i> at a depth <i>y</i> below the water surface. Since the velocity of the "
        "water through this strip is √(2<i>gy</i>), the discharge is:"))
    b.append(eq("δQ̇ = bδy√(2gy)", "28.26"))
    b.append(p(
        "The total discharge is obtained by integration, introducing a coefficient of discharge "
        "<i>C</i><sub>d</sub>:"))
    b.append(eq("Q̇ = C<sub>d</sub>√(2g)·b∫₀ʰ √y dy", "28.27"))
    b.append(eq("Q̇ = (2/3)C<sub>d</sub>√(2g)·bh<sup>3/2</sup>", "28.28"))
    b.append(p(
        "Empirical corrections to Equation 28.28 to account for the weir height <i>p</i> are given, "
        "for example, in [3], but provided <i>h</i>/<i>p</i> does not exceed 0.5, it is adequate to "
        "use Equation 28.28 with a discharge coefficient of 0.63 to achieve a flow rate tolerance of "
        "3%."))
    b.append(p(
        "For the rectangular notch, Equation 28.28 also applies with a discharge coefficient of 0.59 "
        "and a flow rate tolerance of 3%. Since in practice the discharge coefficient varies slightly "
        "with the head of water for both weirs and notches, it is sometimes preferred to replace "
        "Equation 28.28 by Q̇ = <i>Kbh</i><sup>n</sup>, where <i>K</i> and <i>n</i> are determined by "
        "calibration."))
    b.append(p(
        "The triangular notch (Figure 28.13) offers the advantage that the length of the wetted edge "
        "varies with the head of water, in contrast with the rectangular notch where it is constant. "
        "Consequently, the discharge coefficient of the triangular notch is constant for all heads. "
        "Furthermore, the achievable range (ratio of maximum to minimum flow rates) is higher for the "
        "triangular geometry. If <i>h</i> is the height of the water surface and θ is the angle of "
        "the notch, then a horizontal strip of the notch of thickness δ<i>y</i> at depth <i>y</i> has "
        "a width 2(<i>h</i> − <i>y</i>)tan(θ/2). The discharge through this strip is"))
    b.append(eq("δQ̇ = 2(h − y)tan(θ/2)δy√(2gy)·C<sub>d</sub>", "28.29"))
    b.append(p("giving a total discharge through the notch:"))
    b.append(eq("Q̇ = 2C<sub>d</sub>√(2g)·tan(θ/2)∫₀ʰ (h − y)√y dy", "28.30"))
    b.append(eq("Q̇ = (8/15)C<sub>d</sub>√(2g)·tan(θ/2)·h<sup>5/2</sup>", "28.31"))
    b.append(p("The discharge coefficient is about 0.58."))
    b.append(p(
        "Commonly used notch angles are 90° (tan θ/2 = 1, <i>C</i><sub>d</sub> = 0.578), 53.13° "
        "(tan θ/2 = 0.5, <i>C</i><sub>d</sub> = 0.577), and 28.07° (tan θ/2 = 0.25, "
        "<i>C</i><sub>d</sub> = 0.587). Notches with θ = 53.13° and θ = 28.07° deliver, "
        "respectively, one half and one quarter of the discharge of the 90° notch at the same head."))
    b.append(p(
        "The above derivations assume that the water is discharging from a reservoir with "
        "cross-sectional area far exceeding the flow area at the weir, so that the velocity upstream "
        "is negligible. When the weir is built into a channel of cross-sectional area <i>A</i>, the "
        "water will have a finite velocity of approach <i>v</i>₁ = Q̇/<i>A</i>. As a first "
        "approximation, Q̇ is obtained from Equation 28.28 assuming zero velocity of approach. "
        "Assuming further that <i>v</i>₁ is uniform over the weir, there will be an additional head "
        "<i>v</i>₁²/2<i>g</i> acting over the entire weir. Referring to Figure 28.11, the total "
        "discharge is then:"))
    b.append(eq("Q̇ = C<sub>d</sub>√(2g)·b∫<sub>v₁²/2g</sub><sup>h+v₁²/2g</sup> √y dy", "28.32"))
    b.append(eq("Q̇ = (2/3)C<sub>d</sub>√(2g)·b[(h + v₁²/2g)<sup>3/2</sup> − (v₁²/2g)<sup>3/2</sup>]", "28.33"))
    b.append(p(
        "From Equation 28.33, a corrected value of <i>v</i>₁ can be determined. Further iterations "
        "converge rapidly to the final value of the discharge Q̇. Equation 28.33 can be written as:"))
    b.append(eq("Q̇ = (2/3)C<sub>v</sub>C<sub>d</sub>√(2g)·bh<sup>3/2</sup>", "28.34"))
    b.append(p("where"))
    b.append(eq("C<sub>v</sub> = (1 + v₁²/2gh)<sup>3/2</sup> − (v₁²/2gh)<sup>3/2</sup>", "28.35"))
    b.append(p("is the coefficient of velocity, which is frequently determined empirically."))
    b.append(p(
        "Over a broad-crested weir (Figure 28.14), the discharge depends on the head <i>h</i>₁, the "
        "width <i>b</i>, and the length <i>l</i> of the sill. There is also a dependence on the "
        "roughness of the sill surface and the viscosity. Consequently, there is a loss of head as "
        "the water flows over the sill. It is assumed that the sill is of sufficient length to allow "
        "the velocity to be uniform at a value <i>v</i> throughout the depth <i>h</i>₂ of the water "
        "at the downstream edge of the sill. Neglecting losses"))
    b.append(eq("v = √[2g(h₁ − h₂)]", ""))
    b.append(p("and the discharge is:"))
    b.append(eq("Q̇ = C<sub>d</sub>bh₂v = C<sub>d</sub>b√[2g(h₁h₂² − h₂³)]", "28.36"))
    b.append(p(
        "From Equation 28.36, the discharge is a maximum when (<i>h</i>₁<i>h</i>₂² − <i>h</i>₂³) "
        "reaches a maximum, i.e., when <i>h</i>₂ = 2<i>h</i>₁/3. This discharge is then:"))
    b.append(eq("Q̇ = (2/3)<sup>3/2</sup>C<sub>d</sub>b√g·h₁<sup>3/2</sup>", "28.37"))
    b.append(p("The stable condition of the weir lies at the maximum discharge."))
    b.append(p(
        "<b>Flow rate analysis for flumes.</b> The discharge through a flume depends on the water "
        "level <i>h</i>, the channel width <i>b</i>, and velocity <i>v</i> at each of the stations 1 "
        "(upstream) and 2 (at the minimum cross-section) in Figure 28.15. Applying Bernoulli’s "
        "equation to the inlet and the throat, neglecting all losses, one obtains:"))
    b.append(eq("ρgH = ρgh₁ + ½ρv₁² = ρgh₂ + ½ρv₂²", "28.38"))
    b.append(p(
        "where <i>H</i> is the total head. The analysis is then formally the same as that for the "
        "broad-crested weir, giving the same expression for the discharge as in Equation 28.37. The "
        "flow through the flume is a maximum when the depth at the throat is two thirds of the total "
        "head. Normally, a coefficient of velocity is introduced so that the discharge equation is:"))
    b.append(eq("Q̇ = (2/3)<sup>3/2</sup>C<sub>v</sub>C<sub>d</sub>b√g·h₁<sup>3/2</sup>", "28.39"))
    b.append(p(
        "The combined coefficient is determined empirically. In [3], a value "
        "<i>C</i><sub>v</sub><i>C</i><sub>d</sub> = 1.061 − 0.085 is quoted."))
    b.append(p(
        "The validity of the empirical coefficients quoted above, or of other coefficients given in "
        "the various standards for metering of open-channel flows, can only be guaranteed with a "
        "given confidence level for meter installations satisfying certain geometrical constraints. "
        "Limits on quantities such as <i>b</i>, <i>h</i>, <i>h</i>/<i>b</i>, etc. are given in [3] "
        "and the standards."))

    b.append(h4("Rotameter: Internal Flow Analysis", "Rotameter: phân tích dòng chảy bên trong"))
    b.append('<p style="font-weight:650;margin:1.4rem 0 .45rem">Computation of internal flow. '
             '<span class="en">Tính toán dòng chảy bên trong.</span></p>')
    b.append(p(
        "Improvement of rotameter design could be assisted by detailed knowledge of the internal flow "
        "field, which is characterized by steep velocity gradients and regions of separated flow. "
        "Measurements of the internal flow field are complicated by the small dimensions of the gap "
        "around the bob and the strongly curved glass tube. Bückle et al. [13] successfully used "
        "laser Doppler anemometry [14] for velocity measurements in a rotameter. The working fluid "
        "was a glycerine solution with an index of refraction (1.455) close to that of glass (1.476). "
        "Problems with refraction of the laser beams at the curved tube wall were thus avoided, but "
        "the high viscosity of glycerine restricted the experiments to laminar flow at Reynolds "
        "numbers <i>Re</i> = ρ<i>U</i><sub>IN</sub><i>D</i><sub>b</sub>/μ &lt; 400."))
    b.append(p(
        "The application of computational fluid dynamics to the flow in a rotameter [13] involves the "
        "finite volume solution of the conservation equations for mass and momentum. For a "
        "two-dimensional laminar flow, these equations can be written in a cylindrical polar "
        "coordinate system as:"))
    b.append(eq("∂ρ/∂t + ∂(ρu)/∂z + (1/r)·∂(ρrv)/∂r = 0", "28.40"))
    b.append(eq("∂(ρu)/∂t + ∂/∂z(ρuu − 2μ∂u/∂z) + (1/r)·∂/∂r[ρruv − μr(∂u/∂r + ∂v/∂z)] = −∂p/∂z", "28.41"))
    b.append(eq("∂(ρv)/∂t + ∂/∂z[ρuv − μ(∂u/∂r + ∂v/∂z)] + (1/r)·∂/∂r(ρrvv − 2μr∂v/∂r) = −∂p/∂r", "28.42"))
    b.append(p(
        "where ρ is the density, <i>u</i>, <i>v</i> and <i>r</i>, <i>z</i> are the velocity "
        "components and coordinate directions in the axial and radial directions, respectively, μ is "
        "the dynamic viscosity, and <i>p</i> is the pressure."))
    b.append(p(
        "For the numerical solution, the governing equations for a generalized transport variable φ "
        "(i.e., <i>u</i> or <i>v</i>) are formally integrated over each control volume (CV) of the "
        "computational grid. The resulting flux balance equation can in turn be discretized as an "
        "algebraic equation for φ at the center P of each CV in terms of the values φ<sub>nb</sub> at "
        "the four nearest neighbors of point P and known functions <i>A</i>:"))
    b.append(eq("A<sub>P</sub>φ<sub>P</sub> + Σ<sub>nb</sub>A<sub>nb</sub>φ<sub>nb</sub> = S<sub>φ</sub>", "28.43"))
    b.append(p(
        "For the whole solution domain, a system of equations results that can be solved by a "
        "suitable algorithm (e.g. [15])."))
    b.append(p(
        "For a rotameter, the symmetry of the problem allows the computational solution domain to be "
        "chosen as one half diametral plane of the rotameter. The boundary conditions are:"))
    b.append(eq("u = v = 0", "28.44"))
    b.append(p("along the walls, and"))
    b.append(eq("∂u/∂r = v = 0", "28.45"))
    b.append(p(
        "along the axis of symmetry. At the input boundary, the initial profile for the "
        "<i>u</i>-velocity is taken from the experiment. At the outlet boundary, zero gradient is "
        "assumed for all dependent variables."))
    b.append('<p style="font-weight:650;margin:1.4rem 0 .45rem">Computed flow field. '
             '<span class="en">Trường dòng tính được.</span></p>')
    b.append(p(
        "Representative calculations for Reynolds number 220 are shown as velocity vectors (Figure "
        "28.18) and streamlines (Figure 28.19). Experimental and computed velocity profiles over a "
        "radius of the flowmeter tube are shown in Figure 28.20."))
    b.append(fig(18, F.fig(18), "en"))
    b.append(fig(19, F.fig(19), "en"))
    b.append(fig(20, F.fig(20), "en"))
    b.append(p(
        "At <i>z</i> = 45 mm, the computations indicate a stagnation point at the bob tip, but the "
        "measurements show a low but finite axial velocity. The deviation from zero is attributable "
        "to slight unsteadiness in the position of the bob and to smearing of the steep radial "
        "velocity gradient along the measuring volume. This effect is also apparent at radii up to "
        "about 5 mm, where the computations show a notably steeper velocity gradient than the "
        "measurements. The measured and computed peak velocities agree well, although the measured "
        "peak is located at a larger radius."))
    b.append(p(
        "In the strongly converging annulus between the bob and the tube wall (<i>z</i> = 65 mm) and "
        "in the plane <i>z</i> = 88 mm, the computations reproduce well the trend of the measured "
        "results, particularly near the flowmeter wall. Discrepancies in the region adjacent to the "
        "bob are attributable to asymmetry in measured profiles arising from the piping upstream of "
        "the rotameter tube."))
    b.append(p(
        "Above the bob (<i>z</i> = 110 mm), there is a strong upward flow in an annular region near "
        "the tube wall and a recirculation region around the axis occupying almost half the tube "
        "cross-section. The forward velocities show a good match between computations and "
        "measurements, but there is a very marked discrepancy in the recirculation zone. At "
        "<i>z</i> = 135 mm, the recirculation zone is finished, but the wake of the bob is still very "
        "evident. Except for a discrepancy of about 10% on the axis, the results from the two methods "
        "agree remarkably well."))
    b.append(p(
        "The effect of rotation of the bob on the flow field was considered by computations, "
        "including an equation for the azimuthal velocity component <i>w</i>."))
    b.append(eq("∂(ρw)/∂t + ∂/∂z(ρuw − μ∂w/∂z) + (1/r)·∂/∂r[ρrvw − μr∂w/∂r] = −ρvw/r − μw/r²", "28.46"))
    b.append(p(
        "Calculations for 1 Hz rotation frequency showed the highest swirl velocities close to the "
        "axis above the bob. There was no observable influence of the rotation on the <i>u</i>- and "
        "<i>v</i>-velocity components [16]."))

    b.append(h3("Summary", "Tóm tắt"))
    b.append(p(
        "For pipe flows, variable area flowmeters are most suitable for low flow rates of gases or "
        "liquids at moderate temperatures and pressures. Favorable features include rugged "
        "construction, high reliability, low pressure drop, easy installation, and low cost. "
        "Disadvantages include measurement uncertainty of 1% or more, limited range (10:1), slow "
        "response, and restrictions on the meter orientation. A generally good price/performance "
        "ratio has led to widespread use of these meters in numerous scientific and medical "
        "instruments and in many industrial applications for flow monitoring."))
    b.append(p(
        "Variable area flowmeters in open-channel flows have applications for flow measurements in "
        "waste water plants, waterworks, rivers and streams, irrigation, and drainage canals. "
        "Hydrological applications of weirs with adjustable sill or crest height include flow "
        "regulation, flow measurement, upstream water level control, and discharge of excess flow in "
        "streams, rivers, and canals. Ruggedness, simplicity, and low maintenance costs are favorable "
        "characteristics for field applications of these meters."))

    b.append(h3("References", "Tài liệu tham khảo"))
    b.append(wl([
        "1. R. A. Furness, BS7045: the principles of flowmeter selection, <i>Flow Meas. Instrum.</i>, "
        "2, 233–242, 1991.",
        "2. W. Boiten, Flow-measuring structures, <i>Flow Meas. Instrum.</i>, 4, 17–24, 1993.",
        "3. R. Hershey, General purpose flow measurement equations for flumes and thin plate weirs, "
        "<i>Flow Meas. Instrum.</i>, 6, 283–293, 1995.",
        "4. ISO 1438, <i>Thin Plate Weirs</i>, International Standards Organisation, Geneva, 1980.",
        "5. ISO 4359, <i>Rectangular, Trapezoidal and U-shaped Flumes</i>, International Standards "
        "Organisation, Geneva, 1983.",
        "6. ISO 8368, <i>Guidelines for the Selection of Flow Gauging Structures</i>, International "
        "Standards Organisation, Geneva, 1985.",
        "7. G. Ruppel and K. J. Umpfenbach, Strömungstechnische Untersuchungen an Schwimmermessern, "
        "<i>Technische Mechanik und Thermodynamik</i>, 1, 225–233, 257–267, 290–296, 1930.",
        "8. K. Lutz, Die Berechnung des Schwebekörper-Durchflußmessers, <i>Regelungstechnik</i>, 10, "
        "355–360, 1959.",
        "9. D. Bender, Ähnlichkeitsparameter und Durchflußgleichungen für "
        "Schwebekörperdurchflußmesser, <i>ATM-Archiv für Technisches Messen</i>, 391, 97–102, 1968.",
        "10. VDE/VDI-Fachgruppe Meßtechnik 3513, <i>Schwebekörperdurchflußmesser, "
        "Berechnungsverfahren</i>, VDE/VDI 3513, 1971.",
        "11. H. Nikolaus, Berechnungsverfahren für Schwebekörperdurchflußmesser, theoretische "
        "Grundlagen und Aufbereitung für die Datenverarbeitungsanlage, <i>ATM-Archiv für Technisches "
        "Messen</i>, 435, 49–55, 1972.",
        "12. H. Nikolaus and M. Feck, Graphische Verfahren zur Bestimmung von Durchflußkennlinien für "
        "Schwebekörperdurchflußmeßgeräte, <i>ATM-Archiv für Technisches Messen</i>, 1247-5, 171–176, "
        "1974.",
        "13. U. Bückle, F. Durst, B. Howe, and A. Melling, Investigation of a floating element flow "
        "meter, <i>Flow Meas. Instrum.</i>, 3, 215–225, 1992.",
        "14. F. Durst, A. Melling, and J. H. Whitelaw, <i>Principles and Practice of Laser-Doppler "
        "Anemometry</i>, 2nd ed., London: Academic Press, 1981.",
        "15. M. Perić, M. Schäfer, and E. Schreck, Computation of fluid flow with a parallel multigrid "
        "solver, <i>Proc. Conf. Parallel Computational Fluid Dynamics</i>, Stuttgart, 1991.",
        "16. U. Bückle, F. Durst, H. Köchner, and A. Melling, Further investigation of a floating "
        "element flowmeter, <i>Flow Meas. Instrum.</i>, 6, 75–78, 1995.",
    ]))
    return "".join(b)


# ================================================================ 28.3

def sec_28_3_vi():
    b = []
    b.append(h2("28.3 Lưu lượng kế thể tích", "Positive Displacement Flowmeters"))
    b.append(p("Zaki D. Husain và Donald J. Wass — Daniel Flow Products."))
    b.append(p(
        "Lưu lượng kế thể tích, thường gọi tắt là lưu lượng kế PD, đo lưu lượng thể tích của một "
        "dòng chảy liên tục bằng cách nhốt tạm thời một phần chất lưu vào một buồng có thể tích đã "
        "biết rồi xả phần đó trở lại dòng chảy ở phía cửa ra của lưu lượng kế. Bằng cách theo dõi số "
        "lần nhốt trong một khoảng thời gian xác định, hoặc số lần nhốt trong một đơn vị thời gian, "
        "có thể xác định được tổng thể tích dòng chảy hoặc lưu lượng của dòng. Tổng thể tích và lưu "
        "lượng sau đó có thể hiển thị tại chỗ hoặc truyền về trạm giám sát từ xa."))
    b.append(p(
        "Lưu lượng kế thể tích đã được dùng từ nhiều chục năm nay để đo cả dòng chất lỏng lẫn dòng "
        "khí. Có thể xem lưu lượng kế PD như một động cơ thuỷ lực có hiệu suất thể tích cao, thường "
        "hấp thụ một lượng năng lượng nhỏ từ chất lưu đang chảy. Năng lượng bị hấp thụ chủ yếu để "
        "thắng trở lực bên trong của các chi tiết chuyển động và phụ kiện của thiết bị. Phần năng "
        "lượng mất đi này được quan sát thấy dưới dạng độ sụt áp qua lưu lượng kế. Chênh áp qua lưu "
        "lượng kế chính là động lực làm quay các chi tiết bên trong của nó."))

    b.append(h3("Kết cấu và chế tạo", "Design and Construction"))
    b.append(p(
        "Một lưu lượng kế thể tích có ba bộ phận cơ bản: vỏ ngoài, cơ cấu bên trong tạo ra buồng chia "
        "nhờ chuyển động lặp lại của nó, và bộ hiển thị hoặc bộ đếm xác định số lần nhốt chất lưu "
        "trong buồng chia để suy ra lưu lượng và tổng thể tích dòng chảy qua lưu lượng kế."))
    b.append(p(
        "Vỏ ngoài đóng vai trò buồng chứa chất lưu trước và sau mỗi lần bị cơ cấu bên trong nhốt. Với "
        "áp suất đường ống thấp, vỏ thường là một lớp; với áp suất làm việc cao hơn, vỏ là hai lớp, "
        "trong đó lớp trong là thành chịu lực của buồng nhốt còn lớp ngoài là bình chịu áp. Với vỏ "
        "hai lớp, thành buồng nhốt chỉ chịu chênh áp qua lưu lượng kế trong khi vỏ ngoài chịu toàn bộ "
        "áp suất đường ống. Nhờ vậy có thể chế tạo buồng trong thành mỏng mà vẫn giữ được hình dạng "
        "và kích thước chính xác, không phụ thuộc áp suất đường ống."))
    b.append(p(
        "Cơ cấu đo gồm những phần tử đo chính xác, đòi hỏi dung sai rất chặt giữa các bề mặt lắp ghép. "
        "Các phần tử này gồm thành bao của buồng đo và những chi tiết chuyển động tạo nên thể tích "
        "nhốt nhờ chuyển động tuần hoàn hay lặp lại của chúng. Những kiểu lưu lượng kế thể tích thông "
        "dụng nhất là kiểu pít-tông dao động, đĩa nghiêng, bánh răng oval, cánh trượt, hai rôto, ba "
        "rôto và kiểu màng."))
    b.append(p(
        "Cơ cấu đếm hay cơ cấu đầu ra chuyển đổi chuyển động của buồng đo bên trong thành số chỉ lưu "
        "lượng hoặc tổng lưu lượng, bằng cách liên hệ số lần nhốt với thể tích nhốt mỗi lần. Nhiều "
        "lưu lượng kế thể tích dùng bộ truyền bánh răng cơ khí, đòi hỏi các vòng bít và hộp nhồi để "
        "truyền chuyển động của cơ cấu bên trong ra bộ đếm bên ngoài. Kiểu hiển thị này cần thêm công "
        "suất dẫn động để thắng trở lực của các chi tiết chuyển động và của các vòng bít, kết quả là "
        "lưu lượng kế có thêm độ sụt áp. Nhiều lưu lượng kế PD truyền chuyển động của cơ cấu bên "
        "trong ra bộ đếm qua đầu ra dạng xung, dùng kỹ thuật cơ điện, từ, quang hoặc hoàn toàn điện "
        "tử để đếm số lần nhốt và hiển thị lưu lượng cùng tổng thể tích. Các kỹ thuật xử lý sau này "
        "thường gây ít sụt áp hơn phương pháp truyền hoàn toàn cơ khí hoặc bán cơ khí. Bộ đếm dẫn "
        "động hoàn toàn cơ khí không cần nguồn điện ngoài và, nếu chọn đúng bộ bánh răng, có thể hiển "
        "thị trực tiếp thể tích hoặc lưu lượng thực. Nhờ vậy có thể đặt lưu lượng kế ở những vị trí "
        "xa không có nguồn điện nào. Lưu lượng kế hiển thị cơ khí không dễ hiệu chỉnh sự thay đổi thể "
        "tích do buồng đo giãn nở hay co lại vì nhiệt độ dòng chảy, và — với vỏ một lớp — không dễ "
        "hiệu chỉnh sự thay đổi thể tích nhốt do áp suất đường ống thay đổi. Một thiết bị đầu ra xử "
        "lý điện tử có thể theo dõi cả áp suất và nhiệt độ của lưu lượng kế để hiệu chỉnh cần thiết "
        "cho đầu ra. Với công nghệ điện tử không ngừng thay đổi và tiến bộ, nhiều lưu lượng kế PD nay "
        "được lắp đầu ra điện tử dùng pin hoặc pin mặt trời cho những nơi không có nguồn điện. Nhiều "
        "bộ hiển thị điện tử cho phép truy cập dữ liệu của lưu lượng kế từ một trạm giám sát trung "
        "tâm qua vô tuyến hoặc vệ tinh."))

    b.append(h3("Một số thiết kế lưu lượng kế thể tích trên thị trường",
                "Some Commercially Available PD Meter Designs"))
    b.append(p(
        "Các lưu lượng kế thể tích bán trên thị trường có cơ cấu làm việc khác nhau rõ rệt, và một "
        "vài thiết kế là độc quyền. Dù mỗi thiết kế và cơ cấu làm việc có thể rất khác nhau, mọi lưu "
        "lượng kế thể tích đều có một thành giữ chất lưu cố định và một cơ cấu nhốt tạm thời chất "
        "lưu đầu vào vào một buồng đã chia rồi xả ra phía hạ lưu của lưu lượng kế. Việc nhốt và xả "
        "chất lưu diễn ra với chuyển động lặp lại và quét liên tục đến mức, trong hầu hết ứng dụng "
        "thực tế, lưu lượng có vẻ đều và ổn định, dù trên thực tế dòng ra vẫn có dao động. Dao động "
        "lưu lượng ra khỏi lưu lượng kế có thể rõ hơn ở một số thiết kế so với các thiết kế khác. Với "
        "mọi thiết kế, dao động này rõ hơn ở lưu lượng thấp. Một số thiết kế phù hợp hơn cho dòng chất "
        "lỏng hoặc dòng khí, một số khác đo được cả hai. Với chất lỏng, lưu lượng kế thể tích làm việc "
        "tốt nhất với chất lỏng có độ nhớt cao. Hầu như mọi lưu lượng kế thể tích đều đòi hỏi các bề "
        "mặt lắp ghép được gia công chính xác, dung sai chặt; do đó chất lưu được đo phải sạch để "
        "lưu lượng kế có tuổi thọ cao và giữ được độ chính xác đo."))

    b.append(h4("Lưu lượng kế thể tích kiểu cánh trượt", "Sliding-Vane Type PD Meter"))
    b.append(p(
        "Hình 28.21 trình bày một chu trình làm việc của lưu lượng kế thể tích kiểu cánh trượt, trong "
        "đó các cánh được thiết kế để trượt ra vào cơ cấu quay bên trong. Vị trí của mỗi cánh trượt "
        "tương ứng với một góc quay xác định của rôto thường được duy trì bằng một cam cơ khí. Trong "
        "thiết kế ở Hình 28.21, mỗi lá cánh được giữ độc lập trong rãnh của nó. Cũng có những thiết "
        "kế dùng số cánh chẵn, trong đó hai cánh đối xứng qua tâm là một chi tiết liền. Ứng dụng áp "
        "suất cao sẽ dùng kết cấu vỏ hai lớp."))
    b.append(fig(21, F.fig(21), "vi"))

    b.append(h4("Lưu lượng kế thể tích kiểu ba rôto", "Tri-Rotor Type PD Meter"))
    b.append(p(
        "Thiết kế này có ba chi tiết quay nhốt chất lưu giữa các rôto và thành vỏ. Chu trình làm việc "
        "của kiểu này được trình bày trên Hình 28.22. Trong thiết kế này, một vòng quay của cơ cấu "
        "trên ứng với hai vòng quay của cánh. Cơ cấu dẫn động và tương quan quay giữa các cánh được "
        "duy trì bằng một cụm ba bánh răng, trong đó trục của mỗi cánh quay nối với một bánh răng của "
        "cụm để giữ đúng tốc độ quay tương đối. Thiết kế này dùng để đo lưu lượng chất lỏng."))
    b.append(fig(22, F.fig(22), "vi"))

    b.append(h4("Lưu lượng kế thể tích kiểu hai rôto", "Birotor PD Meter"))
    b.append(p(
        "Cụm đo của lưu lượng kế hai rôto có hai rôto dạng xoắn được giữ đồng bộ tuyệt đối bằng một "
        "bộ bánh răng chính xác, và được dùng để đo lưu lượng chất lỏng. Dòng chảy có thể vào lưu "
        "lượng kế theo phương vuông góc hoặc song song với trục quay của hai rôto ăn khớp, như trên "
        "Hình 28.23. Bản hai rôto hướng trục giống bản chuẩn cả về chi tiết lẫn nguyên lý; chỉ khác là "
        "cụm đo được lắp song song — chứ không vuông góc — với dòng chảy. Đầu ra của lưu lượng kế được "
        "ghi nhận cơ khí qua một bộ bánh răng đặt ngoài buồng đo, hoặc ghi nhận điện tử bằng một cụm "
        "cảm biến lắp cùng bánh răng định thời. Cách bố trí hướng trục cho phép lắp đặt gọn, độ chính "
        "xác cao hơn và tổn thất áp suất thấp. Bản hướng trục lý tưởng cho những ứng dụng lưu lượng "
        "lớn."))
    b.append(fig(23, F.fig(23), "vi"))

    b.append(h4("Lưu lượng kế thể tích kiểu pít-tông", "Piston Type PD Meter"))
    b.append(p(
        "Một thiết kế điển hình của lưu lượng kế thể tích kiểu pít-tông được trình bày trên Hình "
        "28.24. Một chi tiết quay đặt ở giữa tạo ra chuyển động tịnh tiến cho cả bốn pít-tông của lưu "
        "lượng kế. Chuyển động tịnh tiến của từng pít-tông được định thời sao cho mỗi xi-lanh xả theo "
        "một chu trình, tạo ra dòng xả bán liên tục từ lưu lượng kế. Loại này dùng cho lưu lượng chất "
        "lỏng rất nhỏ. Kết cấu pít-tông – xi-lanh chịu được chênh áp lớn qua lưu lượng kế, nên có thể "
        "đo chất lỏng có độ nhớt cao với độ chính xác rất cao. Các chi tiết cơ khí của loại này đòi "
        "hỏi dung sai rất chặt, làm tăng giá thành sản phẩm."))
    b.append(fig(24, F.fig(24), "vi"))

    b.append(h4("Lưu lượng kế thể tích kiểu bánh răng oval", "Oval Gear PD Meter"))
    b.append(p(
        "Lưu lượng kế bánh răng oval đo lưu lượng thể tích bằng cách tách những thể tích riêng phần "
        "hình thành giữa các bánh răng oval và thành buồng đo, như trên Hình 28.25. Các bánh răng oval "
        "quay được là nhờ chênh áp qua lưu lượng kế. Trong một vòng quay của hai bánh răng, bốn thể "
        "tích riêng phần được chuyển qua. Chuyển động quay của bánh răng được truyền từ buồng đo ra "
        "trục ra trực tiếp qua các vòng bít cơ khí hoặc qua một khớp nối từ. Loại này dùng để đo chất "
        "lỏng có dải độ nhớt rộng."))
    b.append(fig(25, F.fig(25), "vi"))

    b.append(h4("Lưu lượng kế thể tích kiểu đĩa nghiêng", "Nutating-Disk Type PD Meters"))
    b.append(p(
        "Một đĩa đặt trong giới hạn của một thành bao, theo một hướng xác định, có thể gây ra một bất "
        "ổn định dòng chảy làm đĩa lắc hoặc nghiêng qua lại. Chu trình làm việc của một thiết kế như "
        "vậy được trình bày trên Hình 28.26. Việc nhốt và xả chất lưu vào, ra hai buồng diễn ra ở "
        "những pha khác nhau của chu trình lặp lại của đĩa nghiêng. Loại này dùng để đo chất lỏng. "
        "Thiết kế cho phép đo lưu lượng một cách kinh tế ở những nơi không đòi hỏi độ chính xác cao, "
        "và thường được dùng trong đồng hồ nước."))
    b.append(fig(26, F.fig(26), "vi"))
    b.append(p(
        "Các thiết kế mô tả dưới đây dùng cho dòng khí. Lưu lượng kế thể tích đo khí đòi hỏi dung sai "
        "rất chặt của các chi tiết chuyển động để giảm đường rò, và do đó khí phải sạch vì các lưu "
        "lượng kế này kém chịu được hạt rắn."))

    b.append(h4("Lưu lượng kế thể tích kiểu Roots", "Roots PD Meter"))
    b.append(p(
        "Thiết kế lưu lượng kế Roots được trình bày trên Hình 28.27. Đây là loại lưu lượng kế thể tích "
        "được dùng phổ biến nhất để đo dòng khí, và là một trong những thiết kế lâu đời nhất của lưu "
        "lượng kế thể tích. Khe hở cơ khí giữa các rôto và vỏ đòi hỏi các chi tiết được gia công "
        "chính xác. Lưu lượng kế Roots bị ảnh hưởng xấu nếu dòng vào có mức dao động tương đối cao. "
        "Nhược điểm chính của loại này là nó đưa dao động chu kỳ vào dòng chảy. Lưu lượng kế này không "
        "chịu được bẩn và cần lọc phía thượng lưu. Bản một lớp vỏ của lưu lượng kế Roots được dùng ở "
        "áp suất đường ống gần áp suất khí quyển. Thiết kế này được dùng rất rộng rãi trên thị trường "
        "truyền tải và phân phối khí thiên nhiên áp suất thấp. Nếu lưu lượng kế bị kẹt ở bất kỳ vị trí "
        "nào, dòng chảy bị chặn hoàn toàn."))
    b.append(fig(27, F.fig(27), "vi"))

    b.append(h4("Lưu lượng kế CVM", "The CVM Meter"))
    b.append(p(
        "Lưu lượng kế CVM (Hình 28.28) là một thiết kế độc quyền của lưu lượng kế thể tích dùng để đo "
        "dòng khí. Lưu lượng kế này có một bộ bốn cánh quay trong một không gian vành khuyên quanh "
        "tâm của vỏ tròn. Một cửa chắn có hình dạng giống chi tiết giữa của thiết kế ba rôto (Hình "
        "28.22) cho các cánh đi qua nhưng không cho khí đi qua. Độ chính xác đo của lưu lượng kế CVM "
        "tương tự lưu lượng kế Roots, nhưng biên độ dao động cửa ra nhỏ hơn lưu lượng kế Roots với "
        "cùng cỡ và cùng lưu lượng. Thiết kế này cũng ít nhạy với dao động dòng vào hơn, và được dùng "
        "rộng rãi trên thị trường phân phối khí thiên nhiên áp suất thấp ở châu Âu."))
    b.append(fig(28, F.fig(28), "vi"))

    b.append(h4("Đồng hồ kiểu màng", "Diaphragm Meter"))
    b.append(p(
        "Đồng hồ kiểu màng, còn gọi là đồng hồ kiểu ống xếp, đơn giản, tương đối rẻ, có độ chính xác "
        "đo đáng tin cậy và được dùng rộng rãi làm đồng hồ đo khí trong hộ gia đình. Thiết kế này, "
        "trình bày trên Hình 28.29, hoạt động như một lưu lượng kế pít-tông tịnh tiến, trong đó các "
        "ống xếp đóng vai pít-tông. Hoạt động được điều khiển bằng một van trượt đôi. Ở một vị trí, "
        "van trượt nối cửa vào với mặt trong của ống xếp trong khi mặt ngoài của ống xếp thông với "
        "cửa ra. Ở vị trí kia, mặt ngoài nối với cửa vào trong khi mặt trong của ống xếp thông với "
        "cửa ra. Thiết kế này đo được lưu lượng cực nhỏ (ví dụ bấc đánh lửa của bếp gas)."))
    b.append(fig(29, F.fig(29), "vi"))

    b.append(h3("Ưu điểm và nhược điểm của lưu lượng kế thể tích",
                "Advantages and Disadvantages of PD Meters"))
    b.append(p(
        "Lưu lượng kế thể tích chất lượng cao đo với độ chính xác cao trên một dải lưu lượng rộng và "
        "rất đáng tin cậy trong thời gian dài. Khác với phần lớn lưu lượng kế, lưu lượng kế thể tích "
        "không nhạy với méo dạng mặt cắt dòng vào. Nhờ vậy có thể lắp lưu lượng kế PD sát ngay sau "
        "hoặc trước bất kỳ đoạn ống và phụ kiện nào mà không mất độ chính xác. Nói chung lưu lượng kế "
        "thể tích có độ sụt áp nhỏ, nên có thể lắp trong đường ống có áp suất rất thấp. Cho đến khi "
        "xuất hiện các bộ hiệu chỉnh điện tử và các bộ điều khiển lưu lượng trên những loại lưu lượng "
        "kế khác, lưu lượng kế thể tích được dùng rộng rãi nhất trong các ứng dụng nạp và phân phối "
        "theo lô. Mọi thiết bị cơ khí đều có thể lắp ở những vị trí xa."))
    b.append(p(
        "Lưu lượng kế thể tích nói chung cồng kềnh, đặc biệt ở các cỡ lớn. Do khe hở rất nhỏ cần thiết "
        "giữa các bề mặt lắp ghép, chất lưu phải sạch để bảo đảm độ chính xác đo và tuổi thọ của lưu "
        "lượng kế. Các lưu lượng kế thể tích chính xác hơn thì khá đắt. Nếu lưu lượng kế bị kẹt, dòng "
        "chảy sẽ bị chặn hoàn toàn. Nhiều lưu lượng kế thể tích có quán tính lớn ở các chi tiết "
        "chuyển động; do đó thay đổi lưu lượng đột ngột có thể làm hỏng thiết bị. Lưu lượng kế thể "
        "tích thường chỉ phù hợp trong những dải áp suất và nhiệt độ hạn chế. Một số thiết kế đưa dao "
        "động khá mạnh vào dòng chảy. Phần lớn lưu lượng kế thể tích cần chế độ bảo trì tốt và là "
        "những thiết bị có chi phí sửa chữa và bảo trì cao. Chi phí thường xuyên cho việc bảo trì lưu "
        "lượng kế thể tích có thể là một phần đáng kể trong tổng chi phí của lưu lượng kế."))

    b.append(h3("Ứng dụng", "Applications"))
    b.append(p(
        "Lưu lượng kế thể tích đo chất lỏng có thể đo được chất lưu có dải độ nhớt và khối lượng riêng "
        "rộng. Thay đổi nhỏ về độ nhớt của chất lưu ảnh hưởng không đáng kể tới độ chính xác của lưu "
        "lượng kế thể tích. Tuy vậy không có một thiết kế lưu lượng kế thể tích cụ thể nào đáp ứng "
        "được dải ứng dụng rộng như vậy. Tính chất vật lý của chất lưu, đặc biệt là độ nhớt, phải được "
        "xem xét để chọn đúng lưu lượng kế cho ứng dụng. Nhiều thiết kế lưu lượng kế thể tích đo chính "
        "xác vận tốc dòng trên một dải rộng."))
    b.append(p(
        "Cần kiểm soát kích thước cẩn thận để tạo ra những khe hở được quy định chặt quanh các chi "
        "tiết chuyển động của lưu lượng kế thể tích. Các khe hở này tạo ra đường rò quanh cơ cấu đo; "
        "lượng rò phụ thuộc vận tốc tương đối của các chi tiết chuyển động, độ nhớt của chất lưu và "
        "khe hở giữa các chi tiết. Nói chung lưu lượng rò tuân theo phương trình Poiseuille, nghĩa là "
        "lượng rò tỉ lệ thuận với chênh áp và tỉ lệ nghịch với độ nhớt tuyệt đối cùng chiều dài đường "
        "rò."))
    b.append(p(
        "Lưu lượng rò, tính theo phần trăm tổng lưu lượng, là thông tin hữu ích để đánh giá sai số. Ở "
        "lưu lượng thấp, sai số do rò tính theo phần trăm có thể đáng kể; còn ở lưu lượng vừa phải "
        "thì lượng rò có thể không đáng kể. Tuy nhiên chênh áp qua lưu lượng kế thể tích tăng theo "
        "hàm mũ khi lưu lượng tăng. Do đó ở lưu lượng rất cao, lưu lượng rò lại có thể chiếm một phần "
        "đáng kể của tổng lưu lượng. Kết quả là lưu lượng kế thể tích có xu hướng cấp nhiều chất lưu "
        "hơn số chỉ của bộ đếm ở cả hai vùng lưu lượng rất thấp và rất cao. Mức sai số do rò phụ thuộc "
        "thiết kế lưu lượng kế và độ nhớt của chất lưu."))
    b.append(p(
        "Lưu lượng kế thể tích được dẫn động bằng chênh áp qua nó. Các tổn thất chính bên trong lưu "
        "lượng kế là tổn thất ma sát và lực cản nhớt của chất lưu tác dụng lên các chi tiết chuyển "
        "động. Ở lưu lượng rất thấp, tổn thất ở ổ trục chiếm ưu thế; còn ở lưu lượng cao, lực cản "
        "nhớt chiếm ưu thế. Lực cản nhớt tỉ lệ thuận với độ nhớt của chất lưu và vận tốc tương đối "
        "của các chi tiết chuyển động, và tỉ lệ nghịch với khe hở. Trong mỗi thiết kế, chênh áp được "
        "giới hạn ở một giá trị định trước. Chênh áp quá lớn có thể làm hỏng lưu lượng kế. Có thể "
        "tránh chênh áp cao bằng cách giới hạn lưu lượng cực đại, giảm độ nhớt bằng cách gia nhiệt "
        "chất lưu, tăng khe hở, hoặc kết hợp các biện pháp này. Nói chung, nếu giải quyết được giới "
        "hạn chênh áp thì lưu lượng kế thể tích đo chất lưu có độ nhớt cao có sai số đo nhỏ hơn trên "
        "một dải lưu lượng rộng."))
    b.append(p(
        "Độ nhớt của phần lớn chất khí quá thấp để gây ra những vấn đề ứng dụng liên quan tới lực cản "
        "nhớt như đã bàn với lưu lượng kế thể tích đo chất lỏng. Lưu lượng kế thể tích đo khí dùng "
        "khe hở nhỏ hơn lưu lượng kế đo chất lỏng; do đó khí phải rất sạch. Chỉ một hạt tạp chất nhỏ "
        "cũng có thể làm hỏng lưu lượng kế thể tích đo khí. Lưu lượng kế thể tích dùng trong đo dòng "
        "khí chủ yếu thuộc nhóm áp suất đường ống thấp."))

    b.append(h3("Phụ kiện", "Accessories"))
    b.append(p(
        "Có nhiều phụ kiện cho lưu lượng kế thể tích. Trong số những phụ kiện thông dụng và hữu ích "
        "nhất cho lưu lượng kế thể tích đo chất lỏng là bộ tách khí tự động và van đóng cắt nối trực "
        "tiếp dùng cho các thao tác nạp theo lô. Bộ tách khí tự động gồm một vỏ chịu áp bao quanh một "
        "van phao. Khi khí trong dòng chất lỏng đi vào buồng, phao hạ xuống do trọng lực và cho van "
        "phao mở ra để xả khí. Bộ tách khí làm tăng độ chính xác của phép đo lưu lượng trong nhiều "
        "ứng dụng, và là thứ tuyệt đối cần thiết ở những nơi không khí hoặc khí bị giữ lại trong dòng "
        "chảy."))
    b.append(p(
        "Van đóng cắt nối trực tiếp được liên kết trực tiếp với bộ đếm cơ khí. Có thể nhập vào bộ đếm "
        "một lượng chất lưu định trước. Khi lượng đã cấp bằng lượng nhập vào bộ đếm, liên kết cơ khí "
        "sẽ đóng van lại. Van đóng cắt hai cấp thường được dùng để tránh va đập thuỷ lực trong những "
        "ứng dụng cấp lưu lượng lớn. Tương tự, các thiết bị hoàn toàn điện tử có thể điều khiển các "
        "thao tác theo lô. Thiết bị hoàn toàn điện tử rất thuận tiện trong xử lý dữ liệu. Tuy vậy van "
        "cơ khí dẫn động từ bộ đếm lại có ưu điểm về đơn giản trong thiết kế, về bảo trì hay sửa chữa "
        "tại hiện trường và về chi phí ban đầu."))
    b.append(p(
        "Lưu lượng kế thể tích đo khí có thể được trang bị bộ đếm cơ khí hiệu chỉnh tổng lưu lượng "
        "theo áp suất và nhiệt độ. Dải bù áp suất và nhiệt độ của các thiết bị cơ khí bị hạn chế "
        "nhưng, nếu áp dụng đúng, giới hạn này không thành vấn đề. Bộ tổng hoá điện tử cho lưu lượng "
        "kế thể tích đo khí có thể hiệu chỉnh trên dải nhiệt độ và áp suất rộng. Phụ kiện điện tử có "
        "thể cung cấp nhiều khả năng lưu trữ, ghi dữ liệu và truy cập dữ liệu từ xa."))

    b.append(h3("Giá và hiệu năng", "Price and Performance"))
    b.append(p(
        "Nói chung độ chính xác của lưu lượng kế thể tích được phản ánh qua giá bán. Tuy vậy có nhiều "
        "yếu tố khác ảnh hưởng tới giá. Ứng dụng dự kiến, vật liệu chế tạo và cấp áp suất có ảnh "
        "hưởng mạnh tới giá. Dù cho độ chính xác rất tốt, các lưu lượng kế thể tích cỡ nhỏ dùng cho "
        "nước sinh hoạt hoặc khí thiên nhiên hộ gia đình lại rất rẻ. Lưu lượng kế sản xuất cho thị "
        "trường công nghiệp nói chung cho độ chính xác tốt với giá hợp lý, còn lưu lượng kế chế tạo "
        "cho thị trường đường ống hoặc hoá dầu cho độ chính xác rất tốt nhưng đắt."))
    b.append(p(
        "Có những lưu lượng kế thể tích rất rẻ với vỏ nhựa hoặc cơ cấu bên trong bằng nhựa. Lưu lượng "
        "kế bằng nhôm, đồng thau, gang dẻo hoặc gang có giá trung bình. Lưu lượng kế bằng thép tương "
        "đối đắt, đặc biệt với ứng dụng áp suất cao. Nếu phải dùng thép không gỉ hoặc vật liệu đặc "
        "biệt cho chất lưu ăn mòn hay yêu cầu dịch vụ đặc biệt thì giá rất cao. Lưu lượng kế thể tích "
        "được chế tạo với nhiều cỡ, nhiều cấp áp suất và nhiều loại vật liệu, với vô số dải lưu lượng "
        "và độ chính xác phù hợp hầu hết yêu cầu. Giá thành liên quan trực tiếp tới yêu cầu về hiệu "
        "năng."))

    b.append(h3("Thông tin thêm", "Further Information"))
    b.append(wl([
        "D. W. Spitzer (chủ biên), <i>Flow Measurement: Practical Guides for Measurement and "
        "Control</i>, Research Triangle Park, NC: ISA, 1991.",
        "R. W. Miller, <i>Flow Measurement Engineering Handbook</i>, New York: McGraw-Hill, 1989.",
        "<i>Fluid Meters: Their Theory and Application</i>, 6th ed., báo cáo của ASME Research "
        "Committee on Fluid Meters, American Society of Mechanical Engineers, 1971.",
        "V. L. Streeter, <i>Fluid Mechanics</i>, 4th ed., New York: McGraw-Hill, 1966.",
        "V. L. Streeter, <i>Handbook of Fluid Dynamics</i>, New York: McGraw-Hill, 1961.",
        "<i>Measurement of Liquid Hydrocarbons by Displacement Meters</i>, Manual of Petroleum "
        "Measurement Standard, Chapter 5.2, American Petroleum Institute, 1992.",
    ]))
    return "".join(b)



def sec_28_3_en():
    b = []
    b.append(h2("28.3 Positive Displacement Flowmeters", "Lưu lượng kế thể tích"))
    b.append(p("Zaki D. Husain and Donald J. Wass — Daniel Flow Products."))
    b.append(p(
        "A positive displacement flowmeter, commonly called a PD meter, measures the volume flow rate "
        "of a continuous flow stream by momentarily entrapping a segment of the fluid into a chamber "
        "of known volume and releasing that fluid back into the flow stream on the discharge side of "
        "the meter. By monitoring the number of entrapments for a known period of time or number of "
        "entrapments per unit time, the total volume of flow or the flow rate of the stream can be "
        "ascertained. The total volume and the flow rate can then be displayed locally or transmitted "
        "to a remote monitoring station."))
    b.append(p(
        "The positive displacement flowmeter has been in use for many decades to measure both liquid "
        "and gas flows. A PD meter can be viewed as a hydraulic motor with high volumetric efficiency "
        "that generally absorbs a small amount of energy from the flowing fluid. The energy absorption "
        "is primarily to overcome the internal resistance of the moving parts of the meter and its "
        "accessories. This loss of energy is observed as the pressure drop across the meter. The "
        "differential pressure across the meter is the driving force for the internals of the PD "
        "meter."))

    b.append(h3("Design and Construction", "Kết cấu và chế tạo"))
    b.append(p(
        "A positive displacement meter has three basic components: an outer housing, the internal "
        "mechanism that creates the dividing chamber through its repetitive motion, and the display or "
        "counter accessories that determines the number of entrapments of fluid in the dividing "
        "chamber and infers the flow rate and the total volume of flow through the meter."))
    b.append(p(
        "The external housing acts as the holding chamber of the flowing fluid before and after the "
        "entrapments by the internals. For low line pressures, the housing is usually single walled "
        "while, for higher operating pressures, the housing is double walled where the inner wall is "
        "the containment wall for the entrapment chamber and the outer wall is the pressure vessel. "
        "For the double-walled housing, the entrapment chamber walls are subjected to the differential "
        "pressure across the meter while the external housing is subjected to the total line pressure. "
        "This allows fabrication of a thin-walled inner chamber that can retain its precise shape and "
        "dimensions independent of line pressure."))
    b.append(p(
        "The measuring mechanism consists of precise metering elements that require tight tolerances "
        "on the mating parts. The metering elements consist of the containment wall of the metering "
        "chamber and the moving components of the meter that form the entrapment volume of the flowing "
        "fluid by cyclic or repetitive motion of those elements. The most common types of positive "
        "displacement meters are the oscillating piston, nutating disk, oval gear, sliding vane, "
        "birotor, trirotor, and diaphragm designs."))
    b.append(p(
        "The counter or output mechanism converts the motion of the internal measuring chamber of a PD "
        "meter and displays the flow rate or total flow by correlating the number of entrapments and "
        "each entrapped volume. Many positive displacement meters have a mechanical gear train that "
        "requires seals and packing glands to transmit the motion of the inner mechanism to the "
        "outside counters. This type of display requires more driving power to overcome resistance of "
        "the moving parts and the seals, which results in an additional pressure drop for the meter. "
        "Many PD meters transmit the motion of the inner mechanism to the counters through switch "
        "output utilizing electromechanical, magnetic, optical, or purely electronic techniques in "
        "counting the entrapments and displaying the flow rate and total flow volume. The latter "
        "processing techniques normally have less pressure drop than the all-mechanical or "
        "part-mechanical transmission methods. All-mechanical drive counters do not require external "
        "power and, through proper selection of gear train, can display the actual flow volume or the "
        "flow rate. Thus, meters can be installed at remote locations devoid of any external power "
        "source. Meters with mechanical display cannot easily correct for the changes in volume due to "
        "thermal expansion or contraction of the measuring chamber due to flow temperature variation "
        "and, in the case of single-walled housing, the changes in the entrapment volume due to "
        "variations of the line pressure. An electronically processed output device could monitor both "
        "the pressure and temperature of the meter and provide necessary corrections to the meter "
        "output. With constantly changing and improving electronics technology, many PD meters are now "
        "installed with solar or battery-powered electronic output for installations at remote "
        "locations with no external power source. Many electronic displays allow access to meter data "
        "from a central monitoring station via radio or satellite communication."))

    b.append(h3("Some Commercially Available PD Meter Designs",
                "Một số thiết kế lưu lượng kế thể tích trên thị trường"))
    b.append(p(
        "Commercially available PD meters have many noticeably different working mechanisms and a few "
        "designs are unique and proprietary. Although each design and working mechanism can be "
        "noticeably different from another, all positive displacement meters have a stationary fluid "
        "retaining wall and a mechanism that momentarily entraps inlet fluid into a partitioned "
        "chamber before releasing it to the downstream side of the meter. This entrapment and release "
        "of the flowing fluid occur with such repetitive and sweeping motion that, for most practical "
        "purposes, the flow rate appears to be uniform and steady, even though, in reality, the exit "
        "flow does have some pulsation. The flow pulsation out of the meter may be more pronounced for "
        "some designs of positive displacement meters than others. These flow pulsations are more "
        "pronounced at the lower flow rates for all designs. Some designs are more suitable for either "
        "liquid or gas flows, while some designs can measure both gas and liquid. For liquid "
        "applications, PD meters work best for liquids with heavy viscosities. Almost all PD meters "
        "require precisely machined, high-tolerance mating parts; thus, measured fluid must be clean "
        "for longevity of the meter and to maintain the measurement precision."))

    b.append(h4("Sliding-Vane Type Positive Displacement Meter",
                "Lưu lượng kế thể tích kiểu cánh trượt"))
    b.append(p(
        "Figure 28.21 shows a working cycle of a sliding-vane type PD meter where vanes are designed "
        "to move in and out of the rotating inner mechanism. The position of each sliding vane "
        "relative to specific angular rotation of the rotor is usually maintained by a mechanical cam. "
        "In the design shown in Figure 28.21, each blade is independently retained in the slots. There "
        "are designs with even numbers of blades where diametrically opposite blades are one integral "
        "unit. High-pressure application would utilize dual wall construction."))
    b.append(fig(21, F.fig(21), "en"))

    b.append(h4("Tri-Rotor Type PD Meter", "Lưu lượng kế thể tích kiểu ba rôto"))
    b.append(p(
        "This design has three rotating parts that entrap fluid between the rotors and an outer wall. "
        "The working cycle of this type of meter is shown in Figure 28.22. In this design, for one "
        "rotation of the top mechanism, two blades rotate twice. The driving mechanism and rotation of "
        "each blade with respect to the others is maintained by a three-gear assembly where each "
        "rotating blade shaft is connected to one gear of the three-gear assembly to maintain relative "
        "rotational speed. This design is used to measure liquid flows."))
    b.append(fig(22, F.fig(22), "en"))

    b.append(h4("Birotor PD Meter", "Lưu lượng kế thể tích kiểu hai rôto"))
    b.append(p(
        "The measuring unit of the birotor PD meter has two spiral type rotors kept in perfect timing "
        "by a set of precision gears and is used to measure liquid flows. Flow can enter the meter "
        "either perpendicular or parallel to the axis of rotation of the mating rotors, as shown in "
        "Figure 28.23. The axial design birotor is identical to the standard model in component parts "
        "and in principle; however, it utilizes a measuring unit mounted parallel, rather than "
        "perpendicular, to flow. Meter output is registered mechanically through a gear train located "
        "outside the measuring chamber or, electronically, using a pickup assembly mounted with a "
        "timing gear. Axial orientation results in compact installation, improved accuracy, and low "
        "pressure loss. The axial design is ideal for high flow rate applications."))
    b.append(fig(23, F.fig(23), "en"))

    b.append(h4("Piston Type PD Meter", "Lưu lượng kế thể tích kiểu pít-tông"))
    b.append(p(
        "A typical design of a piston type PD meter is shown in Figure 28.24. A centrally located "
        "rotating part generates the reciprocating motion for each of the four pistons of the meter. "
        "The reciprocating motion of each of the pistons is timed such that the discharge from an "
        "individual piston cylinder occurs in a cycle to generate a semicontinuous discharge from the "
        "meter. These PD meters are used for very low flow rates of liquid flows. A piston-cylinder "
        "design can withstand large differential pressures across the meter, so high viscous liquids "
        "can be measured by this type of meters and measurements are very precise. Mechanical "
        "components of this type of meter require very precise mechanical tolerances, which increase "
        "the product cost."))
    b.append(fig(24, F.fig(24), "en"))

    b.append(h4("Oval Gear PD Meter", "Lưu lượng kế thể tích kiểu bánh răng oval"))
    b.append(p(
        "The measurement of volumetric flow of an oval gear meter is obtained by separating partial "
        "volumes formed between oval gears and the measuring chamber wall, as shown in Figure 28.25. "
        "The rotation of the oval gears results from the differential pressure across the flowmeter. "
        "During one revolution of the oval gears, four partial volumes are transferred. The rotation "
        "of the gears is transmitted from the measuring chamber to the output shaft directly with "
        "mechanical seals or via a magnetic coupling. This type of meter is used to measure liquids "
        "having a wide range of viscosity."))
    b.append(fig(25, F.fig(25), "en"))

    b.append(h4("Nutating-Disk Type PD Meters", "Lưu lượng kế thể tích kiểu đĩa nghiêng"))
    b.append(p(
        "A disk placed within the confines of a boundary wall at a specific orientation can induce a "
        "flow instability that can generate a wobbling or nutating motion to the disk. The operating "
        "cycle of one such design is shown in Figure 28.26. The entrapment and discharge of the fluid "
        "to and from the two chambers occur during different phases of the repetitive cycle of the "
        "nutating disk. This type of meter is used to measure liquids. The design provides economic "
        "flow measurement where accuracy is not of great importance and is often used in water "
        "meters."))
    b.append(fig(26, F.fig(26), "en"))
    b.append(p(
        "Meter designs described hereafter are for gas flows. PD meters for gas flows require very "
        "tight tolerances of the moving parts to reduce leak paths and, therefore, the gas must be "
        "clean because the meters are less tolerant to solid particles."))

    b.append(h4("Roots PD Meter", "Lưu lượng kế thể tích kiểu Roots"))
    b.append(p(
        "The Roots meter design is shown in Figure 28.27. This is the most commonly used PD meter to "
        "measure gas flows. This is one of the oldest designs of a positive displacement meter. The "
        "mechanical clearance between the rotors and the housing requires precisely machined parts. "
        "Roots meters are adversely affected if inlet flow to the meter has a relatively high level of "
        "pulsation. The main disadvantage of this meter is that it introduces cyclic pulsations into "
        "the flow. This meter cannot tolerate dirt and requires filtering upstream of the meter. A "
        "Roots meter in single-case design is used at near-ambient line pressures. This meter design "
        "is very widely used in the low-pressure transmission and distribution market of natural gas. "
        "If this meter ever seizes up at any position, the flow is completely blocked."))
    b.append(fig(27, F.fig(27), "en"))

    b.append(h4("The CVM Meter", "Lưu lượng kế CVM"))
    b.append(p(
        "The CVM meter (Figure 28.28) is a proprietary design of a positive displacement meter used to "
        "measure gas flows. This meter has a set of four vanes rotating in an annular space about the "
        "center of the circular housing. A gate similar in shape to the center piece of the trirotor "
        "design (Figure 28.22) allows the vanes to pass — but not the gas. The measurement accuracy of "
        "the CVM meter is similar to the Roots meter, but the amplitude of exit pulsation is lower "
        "than the Roots meter for similar meter size and flow rate. This design is also not as "
        "sensitive to inlet flow fluctuations, and is widely used in the low-pressure, natural gas "
        "distribution market in Europe."))
    b.append(fig(28, F.fig(28), "en"))

    b.append(h4("Diaphragm Meter", "Đồng hồ kiểu màng"))
    b.append(p(
        "The diaphragm meter, also known as a bellows-type meter, is simple, relatively inexpensive, "
        "has reliable metering accuracy, and is widely used as a domestic gas meter. This design, "
        "shown in Figure 28.29, acts like a reciprocating piston meter, where the bellows act as the "
        "piston. The operation is controlled by a double slide valve. In one position, the slide valve "
        "connects the inlet to the inside of the bellows, while the outside of the bellows is open to "
        "the outlet. In the other position, the outside is connected to the inlet while the inside of "
        "the bellows is open to the outlet. This design can measure extremely low flow rates (e.g., "
        "pilot light of a gas burner)."))
    b.append(fig(29, F.fig(29), "en"))

    b.append(h3("Advantages and Disadvantages of PD Meters",
                "Ưu điểm và nhược điểm của lưu lượng kế thể tích"))
    b.append(p(
        "High-quality, positive displacement meters will measure with high accuracy over a wide range "
        "of flow rates, and are very reliable over long periods. Unlike most flowmeters, a positive "
        "displacement meter is insensitive to inlet flow profile distortions. Thus, PD meters can be "
        "installed in close proximity to any upstream or downstream piping installations without any "
        "loss of accuracy. In general, PD meters have minimal pressure drop across the meter; hence, "
        "they can be installed in a pipeline with very low line pressures. Until the introduction of "
        "electronic correctors and flow controls on other types of meters, PD meters were most widely "
        "used in batch loading and dispensing applications. All mechanical units can be installed in "
        "remote locations."))
    b.append(p(
        "Positive displacement meters are generally bulky, especially in the larger sizes. Due to the "
        "tight clearance necessary between mating parts, the fluid must be clean for measurement "
        "accuracy and longevity of the meter. More accurate PD meters are quite expensive. If a PD "
        "meter ever seizes up, it would completely block the flow. Many PD meters have high inertia of "
        "the moving parts; therefore, a sudden change in the flow rate can damage the meter. PD meters "
        "are normally suitable over only limited ranges of pressure and temperature. Some designs will "
        "introduce noticeably high pulsations into the flow. Most PD meters require a good maintenance "
        "schedule and are high repair and maintenance meters. Recurring costs in maintaining a "
        "positive displacement flowmeter can be a significant factor in overall flowmeter cost."))

    b.append(h3("Applications", "Ứng dụng"))
    b.append(p(
        "Liquid PD meters are capable of measuring fluids with a wide range of viscosity and density. "
        "Minor changes in viscosity of the fluid have minimal influence on the accuracy of a PD meter. "
        "However, no one specific design of PD meter is capable of such a broad application range. The "
        "physical properties of the fluid, especially the fluid viscosity, must be reviewed for proper "
        "selection of a meter for the application. Many PD meter designs accurately measure flow "
        "velocities over a wide range."))
    b.append(p(
        "Careful dimensional control is required to produce well-regulated clearances around the "
        "moving parts of the PD meter. The clearances provide a leakage path around the flow "
        "measurement mechanism, and the amount of leakage depends on the relative velocity of the "
        "moving parts, the viscosity of the fluid, and the clearances between parts. In general, the "
        "leakage flow rate follows the Poiseuille equation; that is, leakage is directly proportional "
        "to the differential pressure and inversely proportional to the absolute viscosity and the "
        "length of the leakage path."))
    b.append(p(
        "The leakage flow, in percentage of the total flow rate, is useful information for error "
        "measurement. At low flow rates, percent leakage error can be significant; while with modest "
        "flow rates, leakage can be insignificant. However, the differential pressure across the PD "
        "meter increases exponentially with increasing flow rates. Therefore, at very high flow rates, "
        "leakage flow can again be a significant portion of the total flow. As a result, PD meters "
        "tend to dispense more fluid than is indicated by the register at the very low and very high "
        "flow rates. The amount of error due to leakage depends on the meter design and on the "
        "viscosity of the fluid."))
    b.append(p(
        "PD meters are driven by the differential pressure across the meter. The primary losses within "
        "the meter can be attributed to the friction losses and the viscous drag of the fluid on the "
        "moving parts. At very low flow rates, the bearing losses are predominant, while at high flow "
        "rates, the viscous drags predominate. The viscous drag is directly proportional to the fluid "
        "viscosity and the relative velocity of the moving parts and inversely proportional to the "
        "clearance. Within each design, the differential pressure is limited to a predetermined value. "
        "Excessive differential pressures can damage the meter. High differential pressure can be "
        "avoided by limiting the maximum flow rate, lowering viscosity by heating the fluid, "
        "increasing clearances, or by various combinations of these techniques. In general, if the "
        "differential pressure limit can be addressed, PD meters measuring high-viscosity fluids have "
        "less measurement error over a wide flow rate range."))
    b.append(p(
        "The viscosity of most gases is too low to cause application problems relating to viscous drag "
        "of the form discussed for liquid PD meters. Gas PD meters utilize smaller clearances than "
        "liquid PD meters; therefore, gas must be very clean. Even small particles of foreign material "
        "can damage gas PD meters. PD meters used in gas flow measurement are primarily in the low "
        "line pressure application."))

    b.append(h3("Accessories", "Phụ kiện"))
    b.append(p(
        "Many accessories are available for PD meters. Among the most common and useful accessories "
        "for liquid PD meters are the automatic air eliminator and the direct-coupled shut-off valve "
        "for batch loading operations. The automatic air eliminator consists of a pressure-containing "
        "case surrounding a float valve. When gas in the liquid flow enters the chamber, the float "
        "descends by gravity and allows the float valve to open and purge the gas. An air eliminator "
        "improves the precision of flow measurement in many applications and is an absolute necessity "
        "in applications where air or gas is trapped in the flow stream."))
    b.append(p(
        "The direct-coupled shut-off valve is directly linked to the mechanical register. A "
        "predetermined fluid quantity can be entered into the register. When the dispensed amount "
        "equals the amount entered in the register, the mechanical linkage closes the valve. Two-stage "
        "shut-off valves are often used to avoid line shock in high flow rate dispensing applications. "
        "Similarly, all-electronic units can control batch operations. The all-electronic units "
        "provide great convenience in the handling of data. However, the register-driven mechanical "
        "valves have advantages in simplicity of design, field maintenance or repair, and initial "
        "cost."))
    b.append(p(
        "Gas PD meters can be equipped with mechanical registers that correct the totals for pressure "
        "and temperature. The pressure and temperature compensation range is limited in the mechanical "
        "units but with appropriate application, the range limitation is not a problem. Electronic "
        "totalizers for gas PD meters can correct for broad ranges of temperature and pressure. "
        "Electronic accessories can provide various data storage, logging, and remote data access "
        "capabilities."))

    b.append(h3("Price and Performance", "Giá và hiệu năng"))
    b.append(p(
        "In general, the accuracy of the PD meter is reflected in the sales price. However, several "
        "additional factors influence the cost. The intended application, the materials of "
        "construction, and the pressure rating have a strong influence on the cost. Although they "
        "provide excellent accuracy, small PD meters for residential water or residential natural gas "
        "service are very inexpensive. Meters produced for the general industrial market provide good "
        "accuracy at a reasonable cost, and meters manufactured for the pipeline or petrochemical "
        "markets provide excellent accuracy and are expensive."))
    b.append(p(
        "Very inexpensive PD meters are available with plastic cases or plastic internal mechanisms. "
        "Aluminum, brass, ductile iron, or cast iron PD meters are moderately priced. Steel PD meters "
        "are relatively expensive, especially for high-pressure applications. If stainless steel or "
        "unusual materials are necessary for corrosive fluids or special service requirements, the "
        "costs are very high. PD meters are manufactured in a wide range of sizes, pressure ratings, "
        "and materials, with a multitude of flow rate ranges, and with an accuracy to match most "
        "requirements. The cost is directly related to the performance requirements."))

    b.append(h3("Further Information", "Thông tin thêm"))
    b.append(wl([
        "D. W. Spitzer, Ed., <i>Flow Measurement: Practical Guides for Measurement and Control</i>, "
        "Research Triangle Park, NC: ISA, 1991.",
        "R. W. Miller, <i>Flow Measurement Engineering Handbook</i>, New York: McGraw-Hill, 1989.",
        "<i>Fluid Meters: Their Theory and Application</i>, 6th ed., Report of ASME Research "
        "Committee on Fluid Meters, American Society of Mechanical Engineers, 1971.",
        "V. L. Streeter, <i>Fluid Mechanics</i>, 4th ed., New York: McGraw-Hill, 1966.",
        "V. L. Streeter, <i>Handbook of Fluid Dynamics</i>, New York: McGraw-Hill, 1961.",
        "<i>Measurement of Liquid Hydrocarbons by Displacement Meters</i>, Manual of Petroleum "
        "Measurement Standard, Chapter 5.2, American Petroleum Institute, 1992.",
    ]))
    return "".join(b)



# ================================================================ build

SECTIONS_VI = [sec_28_1_vi, sec_28_2_vi, sec_28_3_vi]
SECTIONS_EN = [sec_28_1_en, sec_28_2_en, sec_28_3_en]


def body_vi():
    out = ['<p class="lede">Chương này trình bày mười một họ lưu lượng kế — từ tấm orifice chênh áp '
           'cổ điển tới lưu lượng kế Coriolis — cùng nguyên lý, cách chế tạo, lắp đặt và sai số của '
           'từng loại. Đây là chương dài nhất trong sổ tay: 132 trang gốc, 92 hình, 162 phương trình '
           'và 23 bảng.</p>']
    for f in SECTIONS_VI:
        out.append(f())
    return "".join(out)


def body_en():
    out = ['<p class="lede">This chapter covers eleven families of flowmeter — from the classical '
           'differential pressure orifice plate to the Coriolis meter — with the principle, '
           'construction, installation and error sources of each. It is the longest chapter in the '
           'handbook: 132 source pages, 92 figures, 162 equations and 23 tables.</p>']
    for f in SECTIONS_EN:
        out.append(f())
    return "".join(out)


def build(lang):
    vi = lang == "vi"
    switch = ("%s%s/" % (BASE_EN, CSLUG)) if vi else ("%s%s/" % (BASE_VI, CSLUG))
    title = ("Chương 28 — %s · Sổ tay Đo lường, Thiết bị đo và Cảm biến" % TITLE_VI if vi
             else "Chapter 28 — %s · Measurement, Instrumentation and Sensors Handbook" % TITLE_EN)
    desc = ("Bản dịch tiếng Việt Chương 28 “Đo lưu lượng” của Richard Thorn và cộng sự — "
            "lưu lượng kế chênh áp, biến diện tích, thể tích, tuabin, cánh quạt, điện từ, siêu âm, "
            "xoáy, nhiệt và Coriolis, cùng nguyên lý, lắp đặt và hiệu chuẩn." if vi
            else
            "Companion to Chapter 28 of the CRC Measurement Handbook — differential pressure, "
            "variable area, positive displacement, turbine, impeller, electromagnetic, ultrasonic, "
            "vortex, thermal and Coriolis flowmeters, with their principles, installation and "
            "calibration.")
    crumb = ('<a href="/vi/books/">Sách</a> · <a href="%s">Sổ tay Đo lường, Thiết bị đo và Cảm biến</a> · '
             'Chương 28' % BASE_VI if vi else
             '<a href="/books/">Books</a> · <a href="%s">Measurement, Instrumentation and Sensors '
             'Handbook</a> · Chapter 28' % BASE_EN)
    meta = ("Chương 28 · theo Ch28.pdf (CRC Press, 1999) · đang dịch: 3/11 mục" if vi else
            "Chapter 28 · in progress: 3 of 11 sections")
    body = ('<main><article class="intranet-content reader"><div class="reader-hero">'
            '<div class="breadcrumb">%s</div><h1>%s</h1><p class="byline">%s</p>'
            '<div class="meta-line">%s</div></div><div class="prose">%s</div>%s</article></main>'
            % (crumb, TITLE_VI if vi else TITLE_EN, BYLINE, meta,
               body_vi() if vi else body_en(), chapter_nav(lang, 28)))
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
