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
    return ('<h4 style="font-size:1rem;font-weight:700;margin:1.7rem 0 .5rem">%s%s</h4>'
            % (t, (' <span class="en">%s</span>' % en) if en else ""))


def ul(items):
    return ('<ul style="margin:-.2rem 0 1.3rem">%s</ul>'
            % "".join("<li>%s</li>" % i for i in items))


def ol(items):
    """Numbered list. The source uses numbered lists for enumerations whose
    order carries meaning (the naming variants, the six sensing methods), so
    the numbering is reproduced rather than flattened to bullets."""
    return ('<ol style="margin:-.2rem 0 1.3rem">%s</ol>'
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



def _t288(lang):
    """Table 28.8 — examples of turbine and vaned flowmeters."""
    if lang == "vi":
        hd = ("Kiểu", "Cỡ (in.)", "Mô tả", "Ứng dụng tiêu biểu", "Nhà chế tạo", "Giá tham khảo")
        cap = ("Bảng 28.8 · Ví dụ về lưu lượng kế tuabin và lưu lượng kế có cánh. Giá là giá tham "
               "khảo thời điểm sách xuất bản, tính bằng USD.")
        na, tbd = "—", "Không có"
    else:
        hd = ("Type", "Size(s), in.", "Description", "Example application(s)", "Manufacturer",
              "Approx. price range")
        cap = ("Table 28.8 · Examples of turbine and vaned flowmeters. Prices are those quoted at the "
               "time of publication, in US dollars.")
        na, tbd = "—", "Not available"
    rows = [
        ["Axial", "0,5" if lang == "vi" else "0.5", "FT 4-8, with SIL smart transmitter",
         "Máy bay trực thăng — nhiên liệu" if lang == "vi" else "Helicopters — fuel",
         "EG&amp;G Flow Technology", "$2,500"],
        ["Axial", "1", "6700 series, type 60",
         "Sữa tươi, nước khử ion" if lang == "vi" else "Raw milk, de-ionized water",
         "Flow Automation", "$1,500"],
        ["Axial", "16", "Parity series",
         "Chuyển giao dầu thương mại" if lang == "vi" else "Custody transfer oil",
         "Fisher-Rosemount Petroleum", "$30,000–$38,000"],
        ["Axial " + ("hai rôto" if lang == "vi" else "dual rotor"), "12",
         "Auto-Adjust Turbo-Meter",
         "Chuyển giao khí thương mại" if lang == "vi" else "Custody transfer gas",
         "Equimeter", "$42,000"],
        ["Axial " + ("hai rôto" if lang == "vi" else "dual rotor"), "0,25–2" if lang == "vi" else "0.25–2",
         "DR Series",
         "Nhiên liệu — bệ thử động cơ phản lực lớn" if lang == "vi"
         else "Fuel — large jet engine test stands",
         "Exact Flow", "$1,300–$1,800"],
        ["Propeller" if lang == "vi" else "Propeller", "48", "FM182 (150 PSI)",
         "Nước cấp đô thị" if lang == "vi" else "Municipal water", "Sparling", "$6,500"],
        ["Propeller" if lang == "vi" else "Propeller", "6", "FM102 (150 PSI)",
         "Tưới tiêu" if lang == "vi" else "Irrigation", "Sparling", "$850"],
        ["Tiếp tuyến đặc biệt" if lang == "vi" else "Special tangential", na, "Wright Mark 8",
         "Phế dung kế theo dõi" if lang == "vi" else "Monitoring spirometer",
         "Ferraris Medical", "$800"],
        ["Axial", na, "MS03/MS04 MicroPlus",
         "Phế dung kế chẩn đoán" if lang == "vi" else "Diagnostic spirometer",
         "Micro Medical", "$600"],
        ["Axial", "4", "WTX802",
         "Định lượng hoá chất xử lý nước" if lang == "vi"
         else "Chemical dosing for water treatment",
         "SeaMetrics", "$450–$550"],
        ["Axial " + ("kiểu chèn" if lang == "vi" else "insertion"), "1,5–10" if lang == "vi" else "1.5–10",
         "TX101",
         "Nước cấp đô thị, nước — điều hoà không khí" if lang == "vi"
         else "Municipal water, water — HVAC",
         "SeaMetrics", "$450"],
        ["Axial " + ("kiểu chèn" if lang == "vi" else "insertion"), "2+", "VTS-300",
         "Hơi nước áp suất cao" if lang == "vi" else "High pressure steam",
         "Flow Automation", "$2,900"],
        ["Axial " + ("kiểu chèn" if lang == "vi" else "insertion"), "3+", "VL-150-LP",
         "Điều khiển đốt đuốc" if lang == "vi" else "Flare stack control",
         "Flow Automation", "$2,500"],
        ["Axial " + ("kiểu chèn hai rôto" if lang == "vi" else "insertion dual rotor"),
         "2,5–72" if lang == "vi" else "2.5–72", "F-1200",
         "Nước — điều hoà không khí" if lang == "vi" else "Water — HVAC", "Onicon", "$900"],
        ["Mômen động lượng" if lang == "vi" else "Angular momentum", na,
         "Model 9-217 True Mass Fuel Flowmeter",
         "Máy bay phản lực lớn, ví dụ Airbus A320, A321" if lang == "vi"
         else "Large jet aircraft, e.g. Airbus A320, A321",
         "Eldec", tbd],
        ["Đa tia" if lang == "vi" else "Multijet", "1", "1720",
         "Nước sinh hoạt" if lang == "vi" else "Domestic water",
         "ABB Kent Messtechnik", "$170"],
        ["Đa tia" if lang == "vi" else "Multijet", "1,5" if lang == "vi" else "1.5", "AMD3000",
         "Chiết rót và định lượng chất lỏng hoá chất" if lang == "vi"
         else "Chemical liquid filling and dosing",
         "Aquametro AG", "$950"],
        ["Đa tia hướng trục" if lang == "vi" else "Multijet axial", "9/32", "DFS-2W",
         ("Dây chuyền chiết rót dược phẩm, thẩm phân thận, bình chiết đồ uống, OEM" if lang == "vi"
          else "Pharmaceutical filling lines, kidney dialysis dialyte, beverage dispensers, OEM"),
         "Digiflow Systems",
         ("$42 trở xuống, phần đầu đo; $235 phần điện tử" if lang == "vi"
          else "$42 or less, transducer; $235 electronics")],
    ]
    return table(hd, rows, cap, widths=("13%", "9%", "19%", "25%", "17%", "17%"))


def _t289(lang):
    """Table 28.9 — manufacturer contact information."""
    if lang == "vi":
        hd = ("Nhà chế tạo", "Nhà phân phối tại Hoa Kỳ", "Loại sản phẩm liên quan")
        cap = ("Bảng 28.9 · Thông tin liên hệ của nhà chế tạo. Địa chỉ và số điện thoại giữ nguyên "
               "như trong bản gốc năm 1999.")
        ax = ("Tuabin hướng trục — chất lỏng và khí, gồm loại vệ sinh 3A",)
        axl = "Tuabin hướng trục — chất lỏng"
        ins = "Tuabin hướng trục kiểu chèn — chất lỏng và khí"
        insl = "Tuabin hướng trục kiểu chèn — chất lỏng"
        dual_g = "Tuabin hướng trục hai rôto — khí"
        dual_l = "Tuabin hướng trục hai rôto — chất lỏng"
        prop = "Đồng hồ cánh quạt"
        spi_t = "Phế dung kế theo dõi kiểu tuabin tiếp tuyến"
        spi_a = "Phế dung kế chẩn đoán kiểu tuabin hướng trục"
        mj = "Tuabin đa tia"
        ang = "Lưu lượng kế mômen động lượng"
        mjx = "Tuabin hướng trục “đa tia” — chất lỏng"
        na = "Không áp dụng"
    else:
        hd = ("Manufacturer", "U.S. distributor", "Relevant types")
        cap = ("Table 28.9 · Manufacturer contact information. Addresses and telephone numbers are "
               "reproduced as printed in the 1999 original.")
        ax = ("Axial turbines — liquid and gas, including 3A sanitary",)
        axl = "Axial turbines — liquid"
        ins = "Insertion axial turbines — liquid and gas"
        insl = "Insertion axial turbines — liquid"
        dual_g = "Dual rotor axial turbines — gas"
        dual_l = "Dual rotor axial turbines — liquid"
        prop = "Propeller meters"
        spi_t = "Tangential turbine monitoring spirometers"
        spi_a = "Axial turbine diagnostic spirometers"
        mj = "Multijet turbines"
        ang = "Angular momentum flowmeters"
        mjx = "‘Multijet’ axial turbines — liquid"
        na = "Not applicable"
    rows = [
        ["EG&amp;G Flow Technology, Inc.<br><span style=\"font-size:.8rem;color:#666\">4250E Broadway "
         "Road<br>Phoenix, AZ 85040<br>Tel: (602) 437-1315</span>", na,
         ax[0] + "<br>" + ins],
        ["Flow Automation, Inc.<br><span style=\"font-size:.8rem;color:#666\">9303 W. Sam Houston "
         "Pkwy S.<br>Houston, TX 77099<br>Tel: (713) 272-0404</span>", na,
         ins + "<br>" + ax[0]],
        ["Fisher-Rosemount Petroleum<br><span style=\"font-size:.8rem;color:#666\">Highway 301 "
         "North<br>P.O. Box 450<br>Statesboro, GA 30459<br>Tel: (912) 489-0200</span>", na, axl],
        ["Equimeter, Inc.<br><span style=\"font-size:.8rem;color:#666\">805 Liberty Blvd.<br>DuBois, "
         "PA 15801<br>Tel: (814) 371-8000</span>", na, ax[0] + "<br>" + dual_g],
        ["Exact Flow, LLC<br><span style=\"font-size:.8rem;color:#666\">P.O. Box 14515<br>Scottsdale, "
         "AZ 85267-4545<br>Tel: (602) 922-7446</span>", na, dual_l],
        ["Sparling Instruments Co., Inc.<br><span style=\"font-size:.8rem;color:#666\">4097 North "
         "Temple City Blvd.<br>P.O. Box 5988<br>El Monte, CA 91734<br>Tel: (818) 444-0571</span>",
         na, prop],
        ["Ferraris Medical, Ltd<br><span style=\"font-size:.8rem;color:#666\">Ferraris House<br>Aden "
         "Road<br>Enfield, Middlesex EN3 7SE<br>U.K.<br>Tel: 44 (0)181 805 9055</span>",
         "Ferraris Medical, Inc.<br><span style=\"font-size:.8rem;color:#666\">P.O. Box 344<br>9681 "
         "Wagner Road<br>Holland, NY 14080<br>(716) 537-2391</span>", spi_t],
        ["Micro Medical, Ltd.<br><span style=\"font-size:.8rem;color:#666\">The Admiral’s "
         "Offices<br>The Chatham Historic Dockyard<br>Chatham, Kent ME4 4TQ<br>U.K.<br>44 (0)163 "
         "843383</span>",
         "Micro Direct, Inc.<br><span style=\"font-size:.8rem;color:#666\">P.O. Box 239<br>Auburn, ME "
         "04212<br>(800) 588-3381</span>", spi_a],
        ["SeaMetrics Inc.<br><span style=\"font-size:.8rem;color:#666\">P.O. Box 1589<br>Kent, WA "
         "98035<br>Tel: (206) 872-0284</span>", na,
         axl + "<br>" + insl + "<br>" + mj],
        ["Onicon, Inc.<br><span style=\"font-size:.8rem;color:#666\">2161 Logan St.<br>Clearwater, FL "
         "34625<br>Tel: (813) 447-6140</span>", na,
         axl + "<br>" + ("Tuabin hướng trục kiểu chèn, một và hai rôto — chất lỏng" if lang == "vi"
                         else "Insertion axial turbines, single and dual rotor — liquid")],
        ["Eldec Corporation<br><span style=\"font-size:.8rem;color:#666\">16700 13th Avenue W.<br>P.O. "
         "Box 97027<br>Lynnwood, WA 98046<br>Tel: (206) 743-8499</span>", na, ang],
        ["ABB Kent Messtechnik GmbH<br><span style=\"font-size:.8rem;color:#666\">Otto-Hahn-Strasse "
         "25<br>D-68623 Lampertheim<br>Germany<br>49 6206 9330</span>",
         "ISTEC Corporation<br><span style=\"font-size:.8rem;color:#666\">415 Hope Avenue<br>Roselle, "
         "NJ 07203<br>(908) 241-8880</span>", mj],
        ["Aquametro AG<br><span style=\"font-size:.8rem;color:#666\">Ringstrasse 75<br>CH-4106 "
         "Therwil<br>061 725 11 22</span>",
         "ISTEC Corporation<br><span style=\"font-size:.8rem;color:#666\">415 Hope Avenue<br>Roselle, "
         "NJ 07203<br>(908) 241-8880</span>", mj],
        ["Digiflow Systems B.V.<br><span style=\"font-size:.8rem;color:#666\">Postbus 46<br>6580 AA "
         "Malden<br>The Netherlands<br>31 243 582929</span>",
         "Digiflow Systems<br><span style=\"font-size:.8rem;color:#666\">781 Clifton Blvd.<br>"
         "Mansfield, OH 44907<br>(419) 756-1746</span>", mjx],
    ]
    return table(hd, rows, cap)


def sec_28_4_vi():
    b = []
    b.append(h2("28.4 Lưu lượng kế tuabin và cánh", "Turbine and Vane Flowmeters"))
    b.append(p("David Wadlow — Sensors Research Consulting."))
    b.append(p(
        "Mục này mô tả một loạt lưu lượng kế cho ống kín dùng phần tử chuyển đổi dạng cánh quay, "
        "trọng tâm là lưu lượng kế tuabin hướng trục. Lưu lượng kế tuabin một tia và tuabin tiếp "
        "tuyến kiểu chèn — còn gọi là lưu lượng kế bánh guồng — được trình bày ở một mục khác. Các "
        "loại lưu lượng kế có cánh dùng cho đo lưu lượng trong kênh hở và dòng chảy tự do không thuộc "
        "phạm vi mục này."))

    # ---------------------------------------------------------------- axial
    b.append(h3("Lưu lượng kế tuabin hướng trục", "Axial Turbine Flowmeters"))
    b.append(p(
        "Lưu lượng kế tuabin hướng trục hiện đại, khi được lắp đặt và hiệu chuẩn đúng, là một thiết "
        "bị đáng tin cậy có thể đạt độ chính xác cao nhất trong số các cảm biến lưu lượng hiện có, "
        "với cả đo thể tích chất lỏng lẫn chất khí. Nó là kết quả của nhiều thập kỷ đổi mới và hoàn "
        "thiện nguyên lý cánh hướng trục, vốn được ghi nhận lần đầu cho Woltman năm 1790 và khi đó "
        "được ứng dụng để đo dòng nước. Động lực ban đầu cho những phát triển hiện đại phần lớn đến "
        "từ nhu cầu ngày càng tăng của ngành khí tự nhiên Hoa Kỳ trong cuối thập niên 1940 và thập "
        "niên 1950 về một phương tiện đo chính xác lưu lượng trong các tuyến ống khí liên bang có "
        "đường kính lớn và áp suất cao. Ngày nay, nhờ thành công to lớn của nguyên lý này, các lưu "
        "lượng kế tuabin hướng trục với nhiều thiết kế khác nhau — thường là độc quyền — được dùng "
        "cho nhiều ứng dụng đòi hỏi độ chính xác, độ tin cậy và dải đo rộng trong nhiều ngành công "
        "nghiệp lớn ngoài nước và khí tự nhiên, gồm dầu khí, hoá dầu, công nghệ hoá chất, kỹ thuật "
        "lạnh sâu, sữa và đồ uống, hàng không vũ trụ, y sinh và nhiều ngành khác."))
    b.append(p(
        "Hình 28.30 là mặt cắt dọc theo trục đối xứng, mô tả các bộ phận chính của một lưu lượng kế "
        "điển hình. Có thể thấy thiết bị là một cảm biến nối tiếp, gồm một rôto tuabin duy nhất lắp "
        "đồng tâm trên một trục trong vỏ hình trụ mà dòng chảy đi qua. Trục hoặc các ổ trục được định "
        "vị bằng các gối tựa ở hai đầu, nằm trong những kết cấu khí động học treo ở phía trước và "
        "phía sau, gọi là bộ khuếch tán, cánh dẫn hướng, hay đơn giản là hình nón. Nhờ vậy dòng chảy "
        "đi qua một vùng vành khuyên có các cánh rôto. Cánh, thường phẳng nhưng có thể hơi xoắn, "
        "nghiêng một góc so với vận tốc dòng tới và do đó chịu một mômen làm quay rôto. Tốc độ quay "
        "— có thể tới vài · 10⁴ vòng/phút với các lưu lượng kế nhỏ — được phát hiện bởi một đầu thu, "
        "thường là loại từ tính; việc ghi nhận mỗi lần một cánh rôto đi qua cho phép suy ra sự đi qua "
        "của một thể tích chất lưu xác định."))
    b.append(fig(30, F.fig(30), "vi"))

    b.append(h4("Đặc tính làm việc chung", "General Performance Characteristics"))
    b.append(p(
        "Tuabin hướng trục làm việc tốt nhất khi đo những dòng chảy sạch, đã được xử lý và ổn định "
        "của khí và chất lỏng có độ nhớt động học thấp (dưới khoảng 10⁻⁵ m²/s, tức 10 cSt, mặc dù "
        "chúng vẫn được dùng tới 10⁻⁴ m²/s, tức 100 cSt), và có đáp tuyến tuyến tính với dòng chảy "
        "rối dưới âm. Trong những điều kiện này, độ ổn định cơ học cố hữu của kết cấu lưu lượng kế "
        "đem lại độ lặp lại rất tốt. Không kể trường hợp riêng của đồng hồ nước sẽ nói ở phần sau, "
        "các đặc tính làm việc chính là:"))
    b.append(ul([
        "Kích thước (đường kính trong) từ 6 mm đến 760 mm (1/4 in. đến 30 in.).",
        "Lưu lượng đo lớn nhất từ 0,025 A m³/h đến 25.500 A m³/h (0,015 ACFM đến 15.000 ACFM) với "
        "khí, và từ 0,036 m³/h đến 13.000 m³/h (0,16 gpm đến 57.000 gpm, tức 82.000 thùng mỗi giờ) "
        "với chất lỏng, trong đó A có nghĩa là “thực tế”.",
        "Độ lặp lại điển hình là ±0,1 % giá trị đọc với chất lỏng và ±0,25 % với khí, có thể tới "
        "±0,02 % với những lưu lượng kế độ chính xác cao. Độ tuyến tính điển hình (trước khi tuyến "
        "tính hoá bằng điện tử) nằm giữa ±0,25 % và ±0,5 % giá trị đọc với chất lỏng, và giữa ±0,5 % "
        "và ±1,0 % với khí. Các lưu lượng kế độ chính xác cao có độ tuyến tính ±0,15 % với chất lỏng "
        "và ±0,25 % với khí, thường được đặc tả trên dải động 10:1 dưới lưu lượng danh định lớn nhất. "
        "Khả năng truy xuất chuẩn tới NIST (National Institute of Standards and Technology) thường có "
        "sẵn, cho phép ước lượng độ chính xác tuyệt đối tổng thể của lưu lượng kế trong những điều "
        "kiện xác định. Trong điều kiện lý tưởng, độ chính xác tuyệt đối của những thiết kế và cách "
        "lắp đặt tối ưu có thể xấp xỉ năng lực của NIST, vốn được công bố là ±0,13 % với dòng chất "
        "lỏng và ±0,25 % với không khí.",
        "Dải đo, khi định nghĩa là tỷ số các lưu lượng mà đặc tả tuyến tính còn đúng, điển hình từ "
        "10:1 đến 100:1.",
        "Nhiệt độ làm việc trải từ −270 °C đến 650 °C (−450 °F đến 1200 °F).",
        "Áp suất làm việc trải từ chân không thô đến 414 MPa (60.000 psi).",
        "Độ sụt áp tại lưu lượng danh định lớn nhất từ khoảng 0,3 kPa (0,05 psi) với khí đến khoảng "
        "70 kPa (10 psi) với chất lỏng.",
    ]))

    # ---------------------------------------------------------------- theory
    b.append(h3("Lý thuyết", "Theory"))
    b.append(p(
        "Tài liệu hiện hành mô tả hai cách phân tích đặc tính của tuabin hướng trục. Cách thứ nhất mô "
        "tả mômen dẫn động của chất lưu theo trao đổi động lượng, cách thứ hai mô tả nó theo lực nâng "
        "khí động qua lý thuyết cánh. Cách thứ nhất có ưu điểm là cho ngay những kết quả giải tích mô "
        "tả nguyên lý làm việc cơ bản, trong đó có một số kết quả chưa từng xuất hiện trong phân tích "
        "theo lý thuyết cánh. Cách thứ hai có ưu điểm cho phép mô tả đầy đủ hơn với ít giả thiết hơn, "
        "nhưng nặng về toán và nhanh chóng dẫn tới các lời giải phải tính trên máy. Một trong những "
        "người tiên phong nổi bật của cách tiếp cận động lượng là Lee [1], người sau đó đã phát minh "
        "một trong số ít lưu lượng kế tuabin hai rôto đang thành công hiện nay; trong khi Thompson và "
        "Grey [2] đưa ra một trong những mô hình đầy đủ nhất hiện có theo lý thuyết cánh, mô hình này "
        "chẳng hạn đã tính tới hiệu ứng tương tác giữa các cánh. Phần dưới đây dùng cách tiếp cận "
        "trao đổi động lượng để làm nổi bật những khái niệm cơ bản của lưu lượng kế tuabin hướng trục."))
    b.append(p(
        "Trong một tình huống giả định, khi không có lực nào làm chậm rôto, rôto sẽ quay với tốc độ "
        "sao cho vectơ vận tốc dòng chất lưu tại bề mặt cánh được giữ nguyên. Hình 28.31 là giản đồ "
        "vectơ cho một rôto cánh phẳng có góc nghiêng cánh bằng β. Giả thiết cánh rôto phẳng và vận "
        "tốc đồng đều ở mọi nơi, song song với trục rôto, khi đó từ Hình 28.31 ta có:"))
    b.append(fig(31, F.fig(31), "vi"))
    b.append(eq("rω<sub>i</sub> = tanβ / V", "28.47"))
    b.append(p("Khi đưa tổng lưu lượng vào, phương trình trở thành:"))
    b.append(eq("ω<sub>i</sub> / Q = tanβ / (<span style='text-decoration:overline'>r</span> A)", "28.48"))
    b.append(defs([
        ("ω<sub>i</sub>", "tốc độ quay “lý tưởng”"),
        ("Q", "lưu lượng thể tích"),
        ("A", "diện tích mặt cắt vành khuyên của dòng chảy"),
        ("<span style='text-decoration:overline'>r</span>", "trung bình bình phương của bán kính trong và bán kính ngoài của cánh, (R, a)"),
    ]))
    b.append(p(
        "Khử chiều thời gian ở vế trái sẽ quy đại lượng này về số vòng quay của rôto trên một đơn vị "
        "thể tích chất lưu, về bản chất chính là hệ số K mà hầu hết nhà chế tạo công bố. Như vậy, theo "
        "phương trình 28.48, trong điều kiện lý tưởng đáp tuyến của lưu lượng kế là hoàn toàn tuyến "
        "tính và chỉ do hình học quyết định. (Trong một số thiết kế, cánh rôto được xoắn theo đường "
        "vít để tăng hiệu suất, đặc biệt với các cánh có tỷ số bán kính (R/a) lớn. Nếu giả thiết biên "
        "dạng vận tốc phẳng thì góc cánh trong trường hợp này được mô tả bằng tanβ = hằng số · r; "
        "đôi khi gọi là cánh xoắn “lý tưởng”.) Trong thực tế lại tồn tại một số mômen cản của rôto "
        "với độ lớn tương đối khác nhau. Dưới dòng chảy ổn định, rôto nhận tốc độ thoả mãn cân bằng "
        "sau:"))
    b.append(eq(
        "Mômen dẫn động của chất lưu = mômen cản do ma sát chất lưu trên mặt cánh rôto<br>"
        "+ mômen cản do ma sát chất lưu ở moay-ơ và khe hở đỉnh cánh<br>"
        "+ mômen cản của cảm biến tốc độ quay + mômen cản do ma sát ổ trục", "28.49"))
    b.append(p(
        "Trở lại Hình 28.31, hiệu giữa tốc độ thực của rôto, rω, và tốc độ lý tưởng, rω<sub>i</sub>, "
        "là vận tốc trượt của rôto gây ra bởi tác động tổng hợp của mọi mômen cản đã mô tả trong "
        "phương trình 28.49; chính vì thế vectơ vận tốc chất lưu bị lệch đi một góc gọi là góc ra hay "
        "góc xoáy, θ. Ký hiệu biến bán kính là r và cho tốc độ thay đổi tổng mômen động lượng của "
        "chất lưu đi qua rôto bằng mômen cản, ta được:"))
    b.append(eq("∫<sub>a</sub><sup>R</sup> [ρQ·2πr²(rω<sub>i</sub> − rω)] / [π(R² − a²)] dr = N<sub>T</sub>", "28.50"))
    b.append(p("từ đó:"))
    b.append(eq("<span style='text-decoration:overline'>r</span>²ρQ(ω<sub>i</sub> − ω) = N<sub>T</sub>", "28.51"))
    b.append(p(
        "trong đó ρ là khối lượng riêng của chất lưu và N<sub>T</sub> là tổng mômen cản. Kết hợp các "
        "phương trình 28.47 và 28.51 rồi sắp xếp lại, ta được:"))
    b.append(eq("ω / Q = tanβ / (<span style='text-decoration:overline'>r</span> A) − N<sub>T</sub> / (<span style='text-decoration:overline'>r</span>²ρQ²)", "28.52"))
    b.append(p(
        "Các xu hướng thể hiện trong phương trình 28.52 phản ánh sự suy giảm đặc trưng của đáp tuyến "
        "lưu lượng kế ở lưu lượng rất thấp, và giải thích vì sao người ta hay dùng ổ trục ít ma sát "
        "hơn cùng đầu thu ít cản hơn cho khí so với chất lỏng, và cho các lưu lượng kế đường kính nhỏ. "
        "Trong hầu hết thiết kế, đặc biệt với chất lỏng, ba trong bốn mômen cản nêu ở phương trình "
        "28.49 là nhỏ trong điều kiện làm việc bình thường so với mômen do lực cản cảm ứng trên bề mặt "
        "cánh. Như chỉ ra trên Hình 28.31, lực F do hiệu ứng này tác dụng theo phương dọc bề mặt cánh "
        "và có độ lớn:"))
    b.append(eq("F = (ρV² / 2) C<sub>D</sub> S", "28.53"))
    b.append(p(
        "trong đó C<sub>D</sub> là hệ số cản và S là diện tích bề mặt cánh tính cho một phía. Dùng "
        "biểu thức hệ số cản ứng với dòng chảy rối, được Pate và cộng sự [3] cùng nhiều tác giả khác "
        "chọn, có thể ước lượng lực này bằng:"))
    b.append(eq("F = ρV² · 0,074 Re<sup>−0,2</sup> · S", "28.54"))
    b.append(p(
        "trong đó Re là số Reynolds của dòng chảy tính theo dây cung cánh, ký hiệu là kích thước c ở "
        "Hình 28.31. Giả thiết θ nhỏ so với β, sau khi tích phân, độ lớn mômen cản do lực cản cảm ứng "
        "dọc bề mặt cánh của một rôto có n cánh là:"))
    b.append(eq("N<sub>D</sub> = n(R + a)ρV² · 0,037 Re<sup>−0,2</sup> · S · sinβ", "28.55"))
    b.append(p("Kết hợp các phương trình 28.55 và 28.52 rồi sắp xếp lại, ta được:"))
    b.append(eq("ω / Q = tanβ / (<span style='text-decoration:overline'>r</span> A) − 0,036 n(R + a) S A² Re<sup>−0,2</sup> sinβ / <span style='text-decoration:overline'>r</span>²", "28.56"))
    b.append(note(
        "<b>Ghi chú của người dịch.</b> Ba chỗ trong bản in gốc có sai sót, được giữ nguyên như đã in. "
        "Thứ nhất, (28.47) phải là rω<sub>i</sub> = V·tanβ: dạng in ra không cùng thứ nguyên với "
        "(28.48) và trái với giản đồ vectơ ở Hình 28.31. Thứ hai, thừa số trong (28.56) phải là "
        "S/A² — tức mẫu số <span style='text-decoration:overline'>r</span>²A² — chứ không phải S·A², nếu không thì không thể suy ra từ (28.52) và "
        "(28.55). Thứ ba, hệ số 0,036 ở (28.56) đáng lẽ là 0,037 như ở (28.55)."))
    b.append(p(
        "Phương trình 28.56 là một biểu thức gần đúng cho hệ số K, vì nó bỏ qua ảnh hưởng của một số "
        "mômen cản của rôto cùng nhiều yếu tố thiết kế và khí động quan trọng, chẳng hạn độ đặc của "
        "rôto và biên dạng vận tốc dòng chảy. Tuy vậy, nó cho thấy rằng các biến thiên tuyến tính "
        "trong điều kiện làm việc danh định thông thường là hàm của một số yếu tố hình học cơ bản và "
        "của số Reynolds. Những kết quả này phản ánh các xu hướng chung chi phối thiết kế và hiệu "
        "chuẩn. Ngoài ra, sự lệch rõ rệt khỏi quan hệ xấp xỉ ρV² — thực ra là ρ<sup>0,8</sup>V<sup>1,8</sup>"
        "μ<sup>−0,2</sup> qua Re trong phương trình 28.54 — của mômen cản do lực cản chất lưu theo các "
        "tính chất dòng chảy trong chế độ rối, chuyển sang những quan hệ khác trong chế độ chuyển tiếp "
        "và chảy tầng, gây ra những biến thiên lớn của hệ số K theo lưu lượng và theo tính chất môi "
        "chất ở số Reynolds thấp. Đây là lý do then chốt khiến lưu lượng kế tuabin hướng trục thường "
        "được khuyến nghị dùng để đo dòng chảy rối."))

    # ---------------------------------------------------------------- calibration
    b.append(h3("Hiệu chuẩn, lắp đặt và bảo trì", "Calibration, Installation, and Maintenance"))
    b.append(p(
        "Lưu lượng kế tuabin hướng trục có dải động làm việc ít nhất 10:1 mà trên đó độ tuyến tính "
        "được đặc tả. Lưu lượng lớn nhất do các yếu tố thiết kế liên quan tới kích thước so với độ "
        "sụt áp lớn nhất và tốc độ rôto lớn nhất quyết định. Giới hạn dưới của dải do chính đặc tả "
        "tuyến tính quyết định. Do những sai lệch chế tạo nhỏ không tránh được, đường cong sai số "
        "tuyến tính là duy nhất cho từng lưu lượng kế và thường do nhà chế tạo cung cấp. Tuy nhiên, "
        "dù được khuyến nghị khi có thể, điều kiện của ứng dụng thường không thể và cũng không nhất "
        "thiết phải trùng với điều kiện của lần hiệu chuẩn ban đầu, thậm chí cả những lần sau. Điều "
        "này có tầm quan trọng then chốt với những ứng dụng mà điều kiện làm việc thực tế là khắc "
        "nghiệt, hoặc môi chất đắt tiền hay khó xử lý. Hình 28.32 mô tả một đường cong hiệu chuẩn "
        "điển hình — độ tuyến tính theo lưu lượng — biểu diễn qua nhiều cách đo thay thế, và người ta "
        "có thể gặp nhiều tổ hợp khác nhau của chúng trong thực tế. Trục tung vì thế có thể là sai số "
        "tuyến tính tính theo phần trăm lưu lượng, là hệ số K biểu diễn bằng số xung từ đầu ra của "
        "cảm biến tốc độ quay trên một đơn vị thể tích chất lưu, hoặc là độ lệch so với mức đăng ký "
        "100 % — cách cuối chỉ áp dụng cho lưu lượng kế có đầu thu cơ khí. Trục hoành có thể là lưu "
        "lượng tính theo thể tích/thời gian, là số Reynolds (Re), hoặc là tần số xung (từ cảm biến "
        "tốc độ quay với loại không cơ khí) chia cho độ nhớt động học, (f/v), với đơn vị Hz trên "
        "m²/s (Hz/cSt hay Hz/SSU; 10⁻⁶ m²/s = 1 centistoke = 31,0 giây Saybolt Universal), trong đó "
        "độ nhớt động học là tỷ số giữa độ nhớt tuyệt đối (μ) và khối lượng riêng. Việc hiệu chuẩn "
        "tốt nhất nên biểu diễn theo Re hoặc f/v, vì f/v tỷ lệ với Re. Chỗ gồ lên trên đường cong là "
        "đặc điểm thường gặp ở Re thấp, do ảnh hưởng của biên dạng vận tốc. Đường cong hiệu chuẩn hệ "
        "số K theo f/v được gọi riêng là đường cong độ nhớt phổ dụng (UVC) và với hầu hết lưu lượng "
        "kế đều có thể mua từ nhà chế tạo với một khoản phụ phí. Công dụng then chốt của UVC là khi "
        "loại và tính chất môi chất khác đáng kể so với lần hiệu chuẩn gốc, vẫn có thể đạt được độ "
        "chính xác cao hơn hẳn sai số tuyến tính tổng thể nhờ UVC của lưu lượng kế, miễn là biết độ "
        "nhớt động học của ứng dụng. Một kỹ thuật hiệu chuẩn tiên tiến khác [4] là biểu diễn đáp "
        "tuyến theo số Strouhal phụ thuộc Re, hoặc theo số Roshko. Cách này chưa được dùng rộng rãi, "
        "nhưng đặc biệt thích hợp cho những ứng dụng đòi hỏi độ chính xác cao và nhiệt độ khắc "
        "nghiệt, vì nó còn cho phép bù đúng sai số do giãn nở nhiệt của lưu lượng kế."))
    b.append(fig(32, F.fig(32), "vi"))
    b.append(p(
        "Độ chính xác của lưu lượng kế tuabin hướng trục bị giảm bởi dòng chảy không được xử lý, đặc "
        "biệt là dòng xoáy. Nhìn chung nên dùng một cách lắp đặt có bộ xử lý dòng chảy cùng những "
        "đoạn ống thẳng xác định ở thượng nguồn và hạ nguồn [5]. Một số lưu lượng kế tuabin hướng trục "
        "có thể đặt mua kèm bộ nắn thẳng dòng cỡ lớn gắn ngay trước thân lưu lượng kế, hoặc tấm xử lý "
        "dòng chảy tích hợp vào thân. Nhà chế tạo là nguồn thông tin đầu tiên về lắp đặt. Sai số do "
        "mạch động vận tốc dòng chảy là một mối lo khác, đặc biệt trong một số hệ thống khí. Tuy "
        "nhiên, chưa có kỹ thuật chuẩn nào được chấp nhận để chống lại một cách hiệu quả nguồn sai số "
        "này. Cần bảo trì, kiểm tra và hiệu chuẩn lại định kỳ, vì đường hiệu chuẩn sẽ dịch chuyển "
        "theo thời gian do mài mòn, hư hỏng hoặc nhiễm bẩn. Với một số ứng dụng, đặc biệt những ứng "
        "dụng liên quan tới chuyển giao thương mại dầu và khí tự nhiên, đã có các tiêu chuẩn quốc "
        "gia, tiêu chuẩn quốc tế và những khuyến nghị khác quy định yêu cầu tối thiểu cho lưu lượng "
        "kế tuabin về các mặt này [6–10]."))

    # ---------------------------------------------------------------- design
    b.append(h3("Kết cấu và chế tạo", "Design and Construction"))
    b.append(p(
        "Có rất nhiều thiết kế — thường là độc quyền — với những biến thể về rôto, ổ trục, đầu thu và "
        "các bộ phận khác, về hình thức và vật liệu, nhằm phục vụ những ứng dụng khác nhau. Thân lưu "
        "lượng kế có nhiều loại đầu nối tiêu chuẩn. Trong giới hạn của ứng dụng, mục tiêu chính "
        "thường là tối ưu độ ổn định cơ học tổng thể và độ khít lắp, để đạt được độ lặp lại tốt. Các "
        "cân nhắc về hiệu năng, ứng dụng và chế tạo tác động tới từng bộ phận bên trong, nhưng nhiều "
        "nhất là tới rôto — về hình dạng và bước cánh, số cánh, cân bằng và độ cứng so với lực cản, "
        "ứng suất và quán tính; tới ổ trục — về độ chính xác so với ma sát, tốc độ danh định và độ "
        "bền; và tới bộ thu tốc độ quay — về hiệu năng và lực cản."))
    b.append(p(
        "Hầu hết cánh có tỷ số bán kính thấp được phay phẳng, còn cánh tỷ số cao thường xoắn. Số cánh "
        "thay đổi từ khoảng 6 đến 20 hoặc hơn, tuỳ góc nghiêng và tỷ số bán kính cánh, sao cho đạt độ "
        "đặc rôto cần thiết. Độ đặc rôto là thước đo mức “thoáng” của rôto đối với dòng chảy: rôto có "
        "độ đặc cao gắn kết chặt hơn với dòng chảy và đạt dải động tốt hơn. Góc nghiêng, yếu tố chủ "
        "yếu quyết định tốc độ rôto, điển hình là 30° đến 45° nhưng có thể nhỏ hơn ở những lưu lượng "
        "kế dành cho khí có khối lượng riêng thấp. Cụm rôto thường lắp khít với mặt trong của vỏ. Với "
        "lưu lượng kế đường kính lớn, rôto thường có thêm vành bao quanh chu vi ngoài để tăng độ ổn "
        "định. Ngoài ra, vì lưu lượng kế lớn thường dùng cho sản phẩm dầu nặng, bằng cách chọn khe hở "
        "thành thích hợp, lực cản chất lưu sinh ra ở khe hở này thường được thiết kế để bù lại xu "
        "hướng tăng tốc của lưu lượng kế ở số Reynolds thấp khi môi chất có độ nhớt cao. Vật liệu chế "
        "tạo trải từ thép không từ tính đến thép từ tính và chất dẻo."))
    b.append(p(
        "Ổ bi thép không gỉ thường dùng cho lưu lượng kế khí và cho chất lỏng ít bôi trơn như chất "
        "lỏng lạnh sâu và freon, trong khi ổ trượt và ổ chặn bằng cacbua vonfram hoặc gốm tổ hợp "
        "thường được coi là tốt nhất cho nhiều lưu lượng kế chất lỏng khác, tuỳ độ bôi trơn của môi "
        "chất. Ổ chất lưu (đôi khi gọi là thiết kế “không ổ trục”) thường được dùng kèm loại sau, "
        "nhưng đôi khi cả với khí, để giảm lực cản. Chúng làm việc theo nhiều thiết kế khác nhau, "
        "dùng lực do dòng chảy sinh ra để giữ rôto cân bằng, tách khỏi hai đầu trục. Việc bôi trơn ổ "
        "trục hoặc lấy từ chính môi chất được đo, hoặc nhờ một hệ thống bôi trơn trong hay ngoài. Các "
        "ổ trục chóp chống tâm bằng đá quý, mỏng manh hơn, cũng được dùng trong một số ứng dụng khí và "
        "lưu lượng kế nhỏ. Lưu lượng kế cho ngành thực phẩm dược phẩm có thể có lỗ xả trong cụm ổ trục "
        "để đáp ứng tiêu chuẩn 3A về khe nứt và khe khuất."))
    b.append(p(
        "Các loại cảm biến tốc độ quay thông dụng nhất là từ tính, sóng mang điều chế và cơ khí, "
        "ngoài ra còn dùng loại quang, điện dung và điện trở. Trong nghiên cứu, người ta cũng đã báo "
        "cáo một cảm biến tốc độ quay dùng thông lượng bức xạ hạt nhân được điều chế, để dùng trong "
        "một số lò phản ứng hạt nhân [11, 12]. Đầu thu cơ khí, đôi khi có khớp nối từ, là truyền "
        "thống trong một số ứng dụng và có thể có độ phân giải cao; một ưu điểm là không cần nguồn "
        "điện. Tuy nhiên lực cản của đầu thu thường lớn. Loại từ tính và loại sóng mang điều chế đều "
        "dùng ít nhất một cuộn dây trong một cụm đầu thu vặn vào vỏ lưu lượng kế gần rôto. Ở loại cảm "
        "ứng từ, nay ít phổ biến hơn, cánh hoặc vành bao mang các miếng chèn đã từ hoá và tín hiệu "
        "được cảm ứng trong cuộn dây nhờ từ trường đi qua. Ở loại từ trở phổ biến hơn — một ví dụ "
        "được vẽ trên Hình 28.30 — cuộn dây quấn quanh một nam châm vĩnh cửu hoặc một cực từ trong "
        "cụm đầu thu, cụm này được gắn cạnh một rôto có cánh (hoặc vành bao được gia công) bằng vật "
        "liệu có độ từ thẩm cao. Vật liệu sau thường là một mác thép không gỉ từ tính như 416, 430 "
        "hoặc 17-4Ph. Khi rôto quay, từ trở của mạch từ thay đổi, sinh ra tín hiệu trong cuộn dây. Ở "
        "loại sóng mang điều chế đắt hơn, rôto chỉ cần dẫn điện. Cuộn dây là một phần của mạch dao "
        "động tần số vô tuyến (RF) và sự lại gần của cánh rôto làm thay đổi trở kháng mạch, tạo ra "
        "điều chế ở một tần số thấp hơn và được tách ra. Loại RF có lực cản nhỏ hơn nhiều, mức tín "
        "hiệu cao hơn ở lưu lượng thấp, và có thể làm việc ở nhiệt độ trên điểm Curie của các vật "
        "liệu sắt từ thông thường. Chúng được ưu tiên cho ứng dụng dải động rộng và nhiệt độ cao. Lưu "
        "lượng kế hai chiều thường có hai đầu thu từ để xác định chiều dòng chảy; điều này hữu ích, "
        "chẳng hạn khi theo dõi việc nạp và xả bồn chứa trong các ứng dụng thực phẩm dược phẩm. Một "
        "số thiết kế còn dùng nhiều đầu thu từ để tăng độ phân giải đo."))
    b.append(p(
        "Về đầu ra, có nhiều loại khuếch đại xung, bộ tổng hợp, máy tính lưu lượng để hiệu chỉnh áp "
        "suất và nhiệt độ khí, cùng các giao thức ghép nối tiêu chuẩn như 4–20 mA, phù hợp với từng "
        "ứng dụng. Như một ví dụ về bộ truyền tiên tiến, ít nhất một nhà chế tạo (EG&G Flow "
        "Technology, Inc.) cung cấp một bộ truyền “thông minh” thu nhỏ, lập trình lại được, làm việc "
        "theo thời gian thực, tích hợp trong vỏ đầu thu cùng một cảm biến nhiệt độ thân lưu lượng kế, "
        "để bù độ nhớt đầy đủ và tuyến tính hoá theo UVC. Những thiết bị này dùng cho các ứng dụng "
        "chuyên biệt, chẳng hạn quản lý nhiên liệu trên máy bay, nơi đã biết quan hệ độ nhớt – nhiệt "
        "độ của môi chất."))
    b.append(p(
        "Một số ứng dụng có yêu cầu thiết kế và lời giải hoàn toàn khác biệt; hai trường hợp được bàn "
        "riêng dưới đây."))

    b.append(h4("Đồng hồ cánh quạt", "Propeller Meters"))
    b.append(p(
        "Đồng hồ cánh quạt được dùng để đo lưu lượng nước cấp đô thị, nước tưới tiêu hoặc nước thải. "
        "Mặc dù trong một số thiết kế, đồng hồ cánh quạt và đồng hồ tuabin trông gần như giống hệt "
        "nhau và làm việc theo cùng nguyên lý rôto hướng trục, loại lưu lượng kế này hiện được phân "
        "biệt về mặt thương mại và tiêu chuẩn [13, 14] thành một phạm trù riêng, tách khỏi tuabin "
        "hướng trục. Đường kính có thể tới 2440 mm (96 in.). Lưu lượng của một đồng hồ cánh quạt "
        "đường kính 1800 mm (72 in.) lên tới khoảng 25.000 m³/h (110.000 gpm). Độ chính xác điển hình "
        "là ±2 % giá trị đọc. Yêu cầu hàng đầu là độ chắc chắn, và chính ở những thiết kế phù hợp "
        "nhất với môi trường khắc nghiệt thì hình thức mới khác biệt rõ nhất. Cụm rôto và đầu thu "
        "thường được bắt mặt bích vào vỏ và có thể tháo ra. Rôto có khe hở lớn, thường được công xôn "
        "vào dòng chảy và đỡ bằng một ổ trục kín không có cánh dẫn hướng. Rôto điển hình làm bằng chất "
        "dẻo hoặc cao su, mang chỉ ba cánh xoắn mạnh với tỷ số bán kính lớn. Đầu thu luôn là loại cơ "
        "khí và thường có khớp nối từ."))

    b.append(h4("Phế dung kế", "Spirometers"))
    b.append(p(
        "Phế dung kế theo dõi đo thể tích khí đi vào và đi ra phổi, và cũng có thể được tích hợp vào "
        "các mạch máy thở. Phế dung kế chẩn đoán dùng để theo dõi mức độ và tính chất của hô hấp. Với "
        "những thiết bị này, bác sĩ có thể xác định tình trạng hô hấp của bệnh nhân qua nhiều phép đo "
        "và nghiệm pháp lâm sàng khác nhau. Chi phí thấp, khối lượng nhẹ, đáp ứng nhanh và an toàn "
        "cho bệnh nhân là những yêu cầu chính. Năng lực đo gồm thể tích khí của một lần thở ra, và "
        "với loại chẩn đoán còn có lưu lượng thở ra đỉnh, đo tương ứng bằng lít và lít trên giây. "
        "Nhiều công nghệ khác nhau được sử dụng. Tuy nhiên, phế dung kế Wright — mang tên người phát "
        "minh ban đầu [15] — ngày nay dùng để chỉ một loại phế dung kế theo dõi cầm tay dùng một kiểu "
        "đầu đo tuabin tiếp tuyến đặc biệt với rôto hai cánh nối với đầu thu cơ khí và mặt số hiển "
        "thị thể tích. Những phế dung kế này được các kỹ thuật viên hô hấp dùng thường quy để cai máy "
        "thở cho bệnh nhân và kiểm tra máy thở. Cũng có những lưu lượng kế dựa trên tuabin hướng trục "
        "khác dùng cho đo thông khí, chẳng hạn đo chuyển hoá của bệnh nhân. Một phế dung kế chẩn đoán "
        "dựa trên tuabin hướng trục do Micro Medical, Ltd. chế tạo hiện chiếm phần lớn thị trường "
        "châu Âu. Thiết bị này dùng đầu thu quang hồng ngoại và có màn hiển thị điều khiển bằng vi xử "
        "lý chạy pin. Trong các thiết bị y tế này, rôto thường bằng chất dẻo với tỷ số bán kính cánh "
        "lớn. Việc xử lý dòng chảy là tối thiểu hoặc không có. Các lưu lượng kế này thường chính xác "
        "tới ± vài phần trăm giá trị đọc. Tại Hoa Kỳ, phế dung kế được xếp vào thiết bị y tế loại 2, "
        "vì thế cần một số phê duyệt của FDA về chế tạo và tiếp thị. Ở EU, chúng là thiết bị y tế loại "
        "IIb theo một hệ thống khác, và cần những phê duyệt khác."))

    b.append(h4("Tuabin hướng trục hai rôto", "Dual-Rotor Axial Turbines"))
    b.append(p(
        "Tuabin hướng trục hai rôto có những đặc tính mà thiết kế một rôto không có. Năm 1981, Lee và "
        "cộng sự [16] được cấp bằng sáng chế Hoa Kỳ cho một lưu lượng kế tuabin hai rôto tự hiệu "
        "chỉnh và tự kiểm tra, hiện chỉ do Equimeter, Inc. chế tạo và bán với tên Auto-Adjust. Đây là "
        "lưu lượng kế độ chính xác cao, chủ yếu dành cho các tuyến ống khí tự nhiên lớn, nơi ngay cả "
        "những sai số đo nhỏ không bị phát hiện cũng có thể gây tốn kém. Thiết bị gồm hai rôto tuabin "
        "ghép sát nhau, quay cùng chiều. Rôto thượng nguồn là rôto chính, còn rôto thứ hai — có góc "
        "cánh nông hơn nhiều — là rôto cảm biến. Việc hiệu chỉnh liên tục và tự động các sai số đo do "
        "ma sát ổ trục thay đổi được thực hiện bằng cách tính lưu lượng dựa trên hiệu tốc độ hai rôto. "
        "Như chỉ ra trên Hình 28.31 và đã bàn trong phần lý thuyết, góc ra của dòng chảy là do tổng "
        "mômen cản của rôto. Nếu mômen này tăng ở rôto chính, làm giảm tốc độ của nó, thì góc ra tăng "
        "và tốc độ rôto cảm biến cũng giảm theo. Lưu lượng kế cũng không nhạy với góc xoáy ở đầu vào, "
        "vì dòng xoáy ảnh hưởng tới cả hai tốc độ rôto theo cùng một chiều và hiệu ứng này bị trừ đi "
        "khi tính lưu lượng. Thiết bị còn tự kiểm tra mài mòn và hư hỏng bằng cách theo dõi tỷ số hai "
        "tốc độ rôto và so sánh con số này với giá trị lúc lắp đặt [17]."))
    b.append(p(
        "Một lưu lượng kế chất lỏng hai rôto do Ruffner và cộng sự [18] phát minh gần đây được Exact "
        "Flow, LLC giới thiệu. Nó được chào bán như một lưu lượng kế độ chính xác cao (tới ±0,1 % độ "
        "chính xác và ±0,02 % độ lặp lại), với dải động rộng bất thường 500:1 cho một chất lỏng có "
        "một độ nhớt. Lưu lượng kế này đã thành công thương mại bước đầu trong đo lưu lượng nhiên "
        "liệu tại các bệ thử động cơ phản lực lớn, nơi dải động rộng đặc biệt hữu ích [19]. Thiết bị "
        "gồm hai rôto ghép sát nhau về mặt thuỷ lực, quay ngược chiều. Nhờ góc ra do rôto thứ nhất tạo "
        "ra, rôto thứ hai vẫn tiếp tục quay tới những lưu lượng thấp hơn nhiều so với rôto thứ nhất."))

    b.append(h4("Đo dòng hai pha bằng tuabin hướng trục", "Two-Phase Flow Measurement Using Axial Turbines"))
    b.append(p(
        "Một lưu lượng kế tạo chênh áp, chẳng hạn ống Venturi mắc nối tiếp với một tuabin, được biết "
        "là phương pháp phù hợp về kỹ thuật và đơn giản để đo lưu lượng thể tích và khối lượng của "
        "một số sol khí rắn mịn. Tuy nhiên, mục này nêu bật một hướng nghiên cứu hiện nay về việc áp "
        "dụng lưu lượng kế tuabin rôto hướng trục cho một loạt bài toán đo lưu lượng công nghiệp có "
        "dòng hai pha khí/lỏng. Thông thường, lưu lượng kế tuabin không được thiết kế cho và không thể "
        "đo chính xác những dòng như vậy. Sai số cỡ 10 % xuất hiện khi đo chất lỏng có phần rỗng "
        "khoảng 20 %. Những dòng như thế thường được đo sau các thiết bị tách khí. Mặc dù vấn đề này "
        "không chỉ giới hạn ở các ngành đó, động lực chính hiện nay cho nghiên cứu là đo trực tiếp "
        "dầu thô trong các hệ thống khai thác đa pha ngoài khơi, đo hỗn hợp nước/hơi trong vòng làm "
        "mát của lò phản ứng hạt nhân, và đo dòng freon lỏng – hơi trong thiết bị lạnh và điều hoà "
        "không khí. Một số kỹ thuật đã được khảo sát tới nay dùng thêm một cảm biến phụ, có thể là cảm "
        "biến phần rỗng hoặc một thiết bị đo độ sụt áp như ống Venturi hay đĩa cản, trong đó cách tiếp "
        "cận dùng độ sụt áp có vẻ hứa hẹn hơn về kỹ thuật [20, 21]. Xét về mặt thực tiễn, các tỷ trọng "
        "kế gamma để đo phần rỗng là thiết bị bổ sung, đắt tiền và chẳng hạn không thích hợp lắm cho "
        "các mỏ dầu dưới đáy biển. Hai kỹ thuật đang được nghiên cứu không cần cảm biến phụ nối tiếp. "
        "Kỹ thuật thứ nhất dùng chính lưu lượng kế tuabin làm vật cản và kết hợp tín hiệu của tuabin "
        "với tín hiệu của một cảm biến chênh áp nhỏ mắc song song qua vùng vào và vùng ra. Kỹ thuật "
        "này cần một bộ đồng nhất hoá trước tuabin, và độ chính xác ±3 % cho lưu lượng thể tích của "
        "cả hai pha đã được báo cáo gần đây với hỗn hợp không khí/nước có phần rỗng tới 80 % [22]. Kỹ "
        "thuật thứ hai hoàn toàn dựa trên phân tích tín hiệu ra của tuabin và đã cho những tương quan "
        "đáng kể giữa dao động tín hiệu với phần rỗng. Độ chính xác ±2 % khi đo lưu lượng thể tích "
        "nước đã được báo cáo với hỗn hợp không khí/nước có phần rỗng tới 25 % [23]."))

    b.append(h4("Lưu lượng kế tuabin hướng trục kiểu chèn", "Insertion Axial Turbine Flowmeters"))
    b.append(p(
        "Những lưu lượng kế này gồm một rôto hướng trục nhỏ lắp trên một cán chèn xuyên qua thành ống "
        "theo phương bán kính, thường qua một van khoá. Chúng đo vận tốc dòng tại vị trí rôto, từ đó "
        "suy ra lưu lượng thể tích. Đây là lời giải kinh tế cho bài toán đo lưu lượng khi đường kính "
        "ống lớn và yêu cầu độ chính xác vừa phải, và cũng có thể được ưu tiên về kỹ thuật khi độ sụt "
        "áp không đáng kể là một lợi thế, như trong dòng chảy tốc độ cao. Chúng thường tuyến tính hơn "
        "lưu lượng kế tuabin tiếp tuyến kiểu chèn và cạnh tranh cả với lưu lượng kế kiểu chèn điện từ "
        "và kiểu xoáy. Chúng có sẵn để đo nhiều loại chất lỏng và khí, kể cả hơi nước, tương tự dải "
        "môi chất của tuabin hướng trục toàn phần, và có đáp tuyến tuyến tính tương tự. Flow "
        "Automation, Inc. hiện là nhà chế tạo hàng đầu. Rôto, thường bằng kim loại nhưng có thể bằng "
        "chất dẻo, điển hình có đường kính 25 mm đến 51 mm (1 in. đến 2 in.). Chúng có thể chèn vào "
        "ống có đường kính từ 51 mm đến 2032 mm (2 in. đến 80 in.). Dải đo vận tốc phủ 0,046 m/s đến "
        "91 m/s (9 ft/phút đến 18.000 ft/phút) với khí và 0,03 m/s đến 30 m/s (6 ft/phút đến 6.000 "
        "ft/phút) với chất lỏng. Dải động thay đổi giữa 10:1 và 100:1. Lưu lượng đo lớn nhất trong "
        "một ống đường kính 1836 mm (72 in.) có thể lên tới gần 56.500 m³/h (khoảng 250.000 gpm). Vì "
        "đây là cảm biến vận tốc cục bộ, muốn tính lưu lượng thể tích phải biết biên dạng vận tốc "
        "theo diện tích và diện tích dòng chảy thực. Do đó việc xử lý dòng chảy đặc biệt quan trọng "
        "đối với đo thể tích chính xác, còn việc định vị theo phương bán kính — thêm một trách nhiệm "
        "của người dùng — phải theo khuyến nghị của nhà chế tạo, có thể là ở đường tâm, ở một phần ba "
        "đường kính, ở 12 % đường kính, hoặc xác định bằng cách “lấy biên dạng”. Quick [24] bàn về "
        "vận hành và lắp đặt cho đo khí tự nhiên. Mặc dù độ tuyến tính hay “độ chính xác” có thể được "
        "công bố tới ±1 % vận tốc, đạt được độ chính xác tương tự cho lưu lượng thể tích thì tuy có "
        "thể nhưng thường khó hoặc không thực tế. Ở khía cạnh này, một thiết kế hai rôto độc đáo, "
        "riêng của Onicon, Inc. và chủ yếu dùng để đo lưu lượng nước lạnh trong hệ thống điều hoà "
        "không khí, đòi hỏi ít xử lý dòng chảy hơn các thiết kế một rôto. Cụm tuabin hai rôto của "
        "Onicon được vẽ trên Hình 28.33."))
    b.append(fig(33, F.fig(33), "vi"))
    b.append(p(
        "Thiết bị gồm hai rôto quay ngược chiều. Đầu ra dựa trên tốc độ trung bình của hai rôto. Mọi "
        "dòng xoáy hiện diện do xử lý dòng chảy kém sẽ làm thay đổi tốc độ quay của mỗi rôto một "
        "lượng như nhau nhưng ngược dấu. Vì thế sai số do xoáy gần như không còn trong đầu ra đã lấy "
        "trung bình. Ngoài ra, việc lấy mẫu biên dạng dòng chảy cũng tốt hơn so với một rôto. Các "
        "thiết bị được hiệu chuẩn bằng bình chuẩn thể tích, và độ chính xác công bố ±2 % giá trị đọc "
        "là cho lưu lượng thể tích chứ không phải vận tốc. Đây là sai số tổng, đã bao gồm dung sai cho "
        "các biến thiên kích thước của ống tiêu chuẩn công nghiệp."))

    b.append(h4("Lưu lượng kế mômen động lượng", "Angular Momentum Flowmeters"))
    b.append(p(
        "Đây là những lưu lượng kế khối lượng chất lỏng chính xác, tuyến tính, dùng các bộ phận có "
        "cánh, và được dùng trong các ứng dụng hàng không vũ trụ. Hiện chúng là thiết bị được chọn "
        "cho đo lưu lượng nhiên liệu trên máy bay, trong các động cơ phản lực của máy bay thương mại "
        "lớn và một số máy bay quân sự cho ứng dụng đốt tăng lực. Chúng đắt hơn các lưu lượng kế tuabin "
        "tương đương dùng cho ứng dụng này, nhưng cho kết quả đo lưu lượng khối lượng một cách trực "
        "tiếp và không bị ảnh hưởng bởi biến thiên khối lượng riêng của nhiên liệu. Độ chính xác điển "
        "hình nằm giữa ±0,5 % và ±1,0 % trên dải động 40:1 hoặc rộng hơn. Dải đo có sẵn cho lưu lượng "
        "nhiên liệu từ khoảng 0,01 đến 6 kg/s (70 đến 46.000 PPH)."))
    b.append(p(
        "Nguyên lý làm việc đã có từ lâu và dựa trên việc truyền mômen động lượng cho dòng chất lưu "
        "bằng một bánh công tác cánh phẳng được dẫn động. Lực cần thiết để dẫn động bánh công tác ở "
        "tốc độ không đổi được theo dõi như một chỉ báo tỷ lệ với lưu lượng khối lượng khi đại lượng "
        "này thay đổi. Một số thiết kế dùng động cơ điện để dẫn động bánh công tác, nhưng xu hướng "
        "thiết kế hiện nay là không dùng động cơ. Trong thiết bị như vậy, tốc độ dẫn động không đổi "
        "khoảng 100 vòng/phút đến 200 vòng/phút do một hoặc nhiều rôto tuabin được dòng chảy dẫn động "
        "tạo ra. Một cụm van tiết lưu song song thay đổi được, đặt cạnh rôto tuabin, đóng mở bằng cơ "
        "khí theo áp suất động của dòng và nhờ đó tự động duy trì tốc độ quay không đổi, miễn là lưu "
        "lượng còn trên giới hạn dưới của dải đo. Bánh công tác được dẫn động mang các cánh song song "
        "với dòng chảy và nằm trên cùng một trục với rôto tuabin. Một bộ nắn thẳng dòng bảo đảm dòng "
        "song song đi qua bánh công tác. Giữa trục tuabin và bánh công tác có một khớp lò xo có tốc "
        "độ không đổi được thiết kế cẩn thận, sao cho góc lệch giữa hai chi tiết tỷ lệ với mômen tác "
        "dụng, và đại lượng này tỷ lệ trực tiếp với lưu lượng khối lượng. Hai cuộn dây thu cảm nhận "
        "chuyển động quay của tuabin và của bánh công tác có cánh, và người ta chỉ đo chênh lệch thời "
        "gian giữa các xung trong hai tín hiệu này để tính lưu lượng. Chiles và cộng sự [25] trình bày "
        "hình minh hoạ và giải thích chi tiết về cơ cấu tinh xảo này."))

    b.append(h4("Lưu lượng kế tuabin đa tia", "Multijet Turbine Flowmeters"))
    b.append(p(
        "Đây là những lưu lượng kế thể tích tuyến tính dành cho đo chất lỏng, gồm một bánh công tác "
        "một tầng cánh hướng tâm, lắp thẳng đứng trên một ổ trục trong một buồng dòng bị chia theo "
        "phương thẳng đứng, đôi khi gọi là bộ phân phối. Bánh công tác thường bằng chất dẻo và thậm "
        "chí có thể cân bằng nổi trong nước. Có nhiều thiết kế khác nhau, nhưng điển hình thì cả hai "
        "ngăn đều thông với một loạt tia phân bố theo phương bán kính và đặt nghiêng. Các tia ở ngăn "
        "dưới nối với cửa vào của lưu lượng kế và phân phối dòng chảy theo phương tiếp tuyến vào vùng "
        "dưới của cánh bánh công tác, còn loạt tia ở ngăn trên — nghiêng theo chiều ngược lại — cho "
        "dòng chảy thoát ra. Nhờ vậy dạng dòng trong buồng là một đường xoắn ốc thẳng đứng, và áp suất "
        "động làm bánh công tác quay bám theo dòng. Thiết kế này cho lưu lượng kế độ nhạy tốt ở lưu "
        "lượng thấp. Nhờ nguyên lý phân phối, lưu lượng kế cũng không nhạy với điều kiện dòng ở "
        "thượng nguồn. Đầu thu chuyển động quay của bánh công tác luôn là loại cơ khí, thường ghép từ, "
        "và thường cũng nối với bộ truyền tiếp điểm điện. Chúng chủ yếu được dùng trong đo nước, gồm "
        "đo nước uống cho mục đích tính tiền của hộ gia đình và cơ sở kinh doanh, và dùng cùng các hệ "
        "thống quản lý năng lượng như toà nhà dùng nước nóng hay hệ thống sưởi tập trung; ít hơn nhiều "
        "là trong một số ngành hoá chất và dược phẩm cho các hệ thống định lượng và chiết rót liên "
        "quan tới dung môi, chất làm lạnh, axit và kiềm có độ nhớt tuyệt đối dưới 4,5 mPa·s "
        "(0,045 poise). Kích thước có sẵn từ 15 mm đến 50 mm. Dải động nằm giữa 25:1 và 130:1, lưu "
        "lượng đo phủ 0,03 đến 30 m³/h (0,13 đến 130 gpm). Độ tuyến tính đo nằm giữa ±1 % và ±2 %, độ "
        "lặp lại điển hình ±0,3 %. Nhiệt độ làm việc từ bình thường đến 90 °C (200 °F) và áp suất làm "
        "việc lớn nhất có sẵn tới 6,9 MPa (1000 psi). Một số hệ thống đo nước uống đi kèm các tuỳ chọn "
        "viễn trắc tinh vi cho phép truy vấn từ xa qua vô tuyến hoặc điện thoại. Với ứng dụng nước "
        "uống tại Hoa Kỳ, các lưu lượng kế này thường tuân theo tiêu chuẩn AWWA áp dụng [26], còn ở "
        "châu Âu thì áp dụng tiêu chuẩn EEC, DIN và các tiêu chuẩn quốc gia khác."))
    b.append(p(
        "Theo ý tác giả, còn một loại lưu lượng kế có cánh nữa có thể xếp vào kiểu tuabin đa tia. Loại "
        "này gồm một bánh công tác có cánh lắp theo phương trục, với một bộ phận ở thượng nguồn tạo "
        "xoáy xoắn ốc cho dòng chảy. Đầu đo điển hình là một chi tiết chất dẻo nhỏ, giá thấp, đôi khi "
        "dùng một lần, và thường được thiết kế cho chất lỏng (nhưng cả cho khí với độ chính xác thấp "
        "hơn), cho lưu lượng nhỏ (xuống tới 50 mL/phút). Dải động cao và độ chính xác tới ±0,5 %. Goss "
        "[27] mô tả một thiết kế cụ thể đang được dùng. Các ứng dụng chuyên biệt phủ các ngành dược "
        "phẩm, y tế và đồ uống."))

    b.append(h4("Lưu lượng kế rôto trụ", "Cylindrical Rotor Flowmeter"))
    b.append(p(
        "Thay vì ghép với dòng rối nhờ áp suất động hay thông lượng động lượng của chất lưu như ở hầu "
        "hết tuabin hướng trục và tiếp tuyến, một thiết bị nghiên cứu đã được chứng minh của Wadlow "
        "và cộng sự [28] cho phép đo thể tích tuyến tính ở lưu lượng khí thấp bằng một rôto tiếp tuyến "
        "hình trụ nhẵn, quán tính thấp, quay nhờ ma sát bề mặt khi ghép với dòng chảy tầng. Về hình "
        "học, đây là một cánh quay một mặt. Một dòng Poiseuille phẳng được tạo ra, đi theo phương vị "
        "qua phần lớn bề mặt cong của rôto trong một khe vành khuyên hẹp giữa rôto và vỏ đồng tâm. "
        "Rôto được động cơ dẫn động qua một mạch điều khiển phản hồi nối với một cảm biến chênh áp "
        "sinh tín hiệu sai lệch, mắc song song qua các cửa khí, sao cho độ sụt áp của lưu lượng kế "
        "luôn bằng không. Trong điều kiện đó, đáp tuyến — thể hiện qua tốc độ trục động cơ — là tuyến "
        "tính chính xác, chỉ do hình học quyết định và không phụ thuộc khối lượng riêng hay độ nhớt "
        "của khí. Thiết bị đã báo cáo có rôto đường kính 40 mm và cửa khí đường kính 15 mm. Nó đo tối "
        "đa 25 L/phút theo cả hai chiều, có dải động tuyến tính lớn hơn 100:1, không nhạy với điều "
        "kiện dòng thượng nguồn, và có thời gian đáp ứng bước 1/e là 42 ms, chỉ bị giới hạn bởi mômen "
        "động cơ ngoài cùng quán tính tổng hợp của động cơ và rôto."))

    # ---------------------------------------------------------------- makers
    b.append(h3("Nhà chế tạo", "Manufacturers"))
    b.append(p(
        "Có sự cạnh tranh mạnh và năng động giữa nhiều nhà chế tạo các loại lưu lượng kế mô tả trong "
        "mục này. Ở mọi loại lưu lượng kế, phần lớn nhà chế tạo đều có quyền sáng chế độc quyền cho "
        "một hay nhiều chi tiết thiết kế khiến sản phẩm của họ làm việc khác với sản phẩm cạnh tranh. "
        "Cứ vài năm lại có thể nhận ra một hay nhiều công ty lưu lượng kế tuabin lớn đã đổi chủ và đổi "
        "tên, hoặc lập quan hệ đối tác mới. Việc nhận diện đối thủ và chọn nhà chế tạo là những phần "
        "quan trọng và đôi khi tốn thời gian của quá trình chọn và đặc tả lưu lượng kế. Để hỗ trợ việc "
        "này, Bảng 28.8 nêu một vài ví dụ chọn lọc từ các nhà chế tạo khác nhau, cho tất cả các loại "
        "lưu lượng kế đã mô tả trong mục này. Bảng 28.9 cho thông tin liên hệ tương ứng của những nhà "
        "chế tạo được chọn đó, cùng các loại sản phẩm nói chung mà mỗi hãng cung cấp."))
    b.append(_t288("vi"))
    b.append(_t289("vi"))

    # ---------------------------------------------------------------- conclusion
    b.append(h3("Kết luận", "Conclusion"))
    b.append(p(
        "Dù những cảm biến cơ khí tinh xảo có vẻ lỗi thời đến đâu giữa công nghệ cao thường ngày hiện "
        "nay, vẫn có những lý do cơ bản khiến tuabin hướng trục nhiều khả năng tiếp tục được duy trì "
        "và phát triển chứ không bị đào thải, đặc biệt với các ứng dụng nối tiếp đòi hỏi độ chính xác "
        "thể tích cỡ phần mười phần trăm. Ghép nối cơ khí là tương tác thể tích trực tiếp nhất với "
        "một chất lưu đang chảy, và đó là lý do vì sao các lưu lượng kế cơ khí ra đời sớm nhất trong "
        "lịch sử và vẫn tiếp tục là loại lưu lượng kế chính xác và đáng tin cậy nhất cho rất nhiều "
        "chất lưu khác nhau. Vì thế, những cách tiếp cận phi cơ khí khác — có lẽ công nghệ cao hơn, "
        "hoặc mới hơn — phải đối mặt với yêu cầu cao về bù trừ chính xác để làm cho những kỹ thuật "
        "ghép thể tích kém trực tiếp hơn ấy trở nên chính xác nói chung, hoặc chính xác hơn. Đó là vì "
        "sai số của từng hệ số hiệu chỉnh hay từng giả thiết trong một kỹ thuật gián tiếp đều đóng "
        "góp vào sai số tổng. Công nghệ lưu lượng kế độ chính xác cao tiếp tục được các ứng dụng thúc "
        "đẩy, chẳng hạn chuyển giao thương mại dầu và khí tự nhiên có giá trị lớn, vốn đòi hỏi độ "
        "chính xác và độ tin cậy cao. Nhu cầu về lưu lượng kế nước chính xác và đáng tin cậy vẫn tiếp "
        "diễn. Nhờ kinh nghiệm thực địa lâu năm đã được chứng minh, tuabin và các thiết bị kiểu cánh "
        "khác đã trở thành một trong số ít kỹ thuật được chấp nhận rộng rãi trong nhiều ứng dụng lớn "
        "như vậy, nơi nhu cầu về cảm biến lưu lượng là đáng kể hoặc đang tăng."))

    # ---------------------------------------------------------------- refs
    b.append(h3("Tài liệu tham khảo", "References"))
    b.append(wl([
        "[1] W. F. Z. Lee và H. J. Evans, “Density effect and Reynolds number effect on gas turbine "
        "flowmeters”, <i>Trans. ASME, J. Basic Eng.</i>, 87(4): 1043–1057, 1965.",
        "[2] R. E. Thompson và J. Grey, “Turbine flowmeter performance model”, <i>Trans. ASME, J. Basic "
        "Eng.</i>, 92(4), 712–723, 1970.",
        "[3] M. B. Pate, A. Myklebust và J. H. Cole, “A computer simulation of the turbine flow meter "
        "rotor as a drag body”, <i>Proc. Int. Comput. in Eng. Conf. and Exhibit 1984</i>, Las Vegas: "
        "184–191, New York: ASME, 1984.",
        "[4] P. D. Olivier và D. Ruffner, “Improved turbine meter accuracy by utilization of "
        "dimensionless data”, <i>Proc. 1992 National Conf. Standards Labs. (NCSL) Workshop and "
        "Symp.</i>, Boulder, CO: NCSL, 1992, 595–607.",
        "[5] ISA-RP 31.1, <i>Specification, Installation and Calibration of Turbine Flowmeters</i>, "
        "Research Triangle Park, NC: ISA, 1977.",
        "[6] ANSI/ASME MFC-4M-1986 (R1990), <i>Measurement of Gas Flow by Turbine Meters</i>, New York: "
        "ASME.",
        "[7] API MPM, <i>Measurement of Liquid Hydrocarbons by Turbine Meters</i>, 3rd ed., "
        "Washington, D.C.: API (Amer. Petroleum Inst.), 1995, chap. 5.3.",
        "[8] AGA Transmission Meas. Committee Rep. No. 7, <i>Measurement of fuel gas by turbine "
        "meters</i>, Arlington, VA: AGA (Amer. Gas Assoc.), 1981.",
        "[9] Int. Recommendation R32, <i>Rotary piston gas meters and turbine gas meters</i>, Paris: "
        "OIML (Int. Organization of Legal Metrology), 1989.",
        "[10] ISO 9951:1993, <i>Measurement of gas flow in closed conduits — turbine meters</i>, "
        "Geneva, Switzerland: Int. Organization for Standardization (also available ANSI), 1993.",
        "[11] T. H. J. J. Van Der Hagen, “Proof of principle of a nuclear turbine flowmeter”, "
        "<i>Nucl. Technol.</i>, 102(2), 167–176, 1993.",
        "[12] K. Termaat, W. J. Oosterkamp và W. Nissen, “Nuclear turbine coolant flow meter”, U.S. "
        "Patent No. 5,425,064, 1995.",
        "[13] AWWA C704-92, <i>Propeller-type meters for waterworks applications</i>, Denver, CO: "
        "Amer. Water Works Assoc., 1992.",
        "[14] ANSI/AWWA C701-88, <i>Cold water meters — turbine type, for customer service</i>, "
        "Denver, CO: Amer. Water Works Assoc., 1988.",
        "[15] B. M. Wright và C. B. McKerrow, “Maximum forced expiratory flow rate as a measure of "
        "ventilatory capacity”, <i>Br. Med. J.</i>, 1041–1047, 1959.",
        "[16] W. F. Z. Lee, R. V. White, F. M. Sciulli và A. Charwat, “Self-correcting self-checking "
        "turbine meter”, U.S. Patent No. 4,305,281, 1981.",
        "[17] W. F. Z. Lee, D. C. Blakeslee và R. V. White, “A self-correcting and self-checking gas "
        "turbine meter”, <i>Trans. ASME, J. Fluids Eng.</i>, 104, 143–149, 1982.",
        "[18] D. F. Ruffner và P. D. Olivier, “Wide range, high accuracy flow meter”, U.S. Patent No. "
        "5,689,071, 1997.",
        "[19] D. F. Ruffner, trao đổi riêng, 1996.",
        "[20] A. Abdul-Razzak, M. Shoukri và J. S. Chang, “Measurement of two-phase refrigerant "
        "liquid-vapor mass flow rate. III. Combined turbine and venturi meters and comparison with "
        "other methods”, <i>ASHRAE Trans.: Research</i>, 101(2), 532–538, 1995.",
        "[21] W. J. Shim, T. J. Dougherty và H. Y. Cheh, “Turbine meter response in two-phase flows”, "
        "<i>Proc. Int. Conf. Nucl. Eng. — 4</i>, 1 part B: 943–953, New York: ASME, 1996.",
        "[22] K. Minemura, K. Egashira, K. Ihara, H. Furuta và K. Yamamoto, “Simultaneous measuring "
        "method for both volumetric flow rates of air-water mixture using a turbine flowmeter”, "
        "<i>Trans. ASME, J. Energy Resources Technol.</i>, 118, 29–35, 1996.",
        "[23] M. W. Johnson và S. Farroll, “Development of a turbine meter for two-phase flow "
        "measurement in vertical pipes”, <i>Flow Meas. Instrum.</i>, 6(4), 279–282, 1995.",
        "[24] L. A. Quick, “Gas measurement by insertion turbine meter”, <i>Proc. 70th Int. School "
        "Hydrocarbon Meas.</i>, OK, 1995. (Có thể lấy từ E. Blanchard, Arrangements Chair, Shreveport, "
        "LA, (318) 868–0603.)",
        "[25] W. E. Chiles, L. E. Vetsch và J. V. Peterson, “Shrouded flowmeter turbine and improved "
        "fluid flowmeter using the same”, U.S. Patent No. 4,012,957, 1977.",
        "[26] ANSI/AWWA C708-91, <i>Cold-water meters, multi-jet-type</i>, Denver, CO: Amer. Water "
        "Works Assoc., 1991.",
        "[27] J. Goss, “Flow meter”, U.S. Patent No. 5,337,615, 1994.",
        "[28] D. Wadlow và L. M. Layden, “Controlled flow volumetric flowmeter”, U.S. Patent No. "
        "5,284,053, 1994.",
        "[29] C. R. Sparks, trao đổi riêng, 1996.",
    ]))

    b.append(h3("Thông tin thêm", "Further Information"))
    b.append(p(
        "D. W. Spitzer (chủ biên), <i>Flow Measurement</i>, Research Triangle Park, NC: ISA, 1991, là "
        "một cẩm nang kỹ thuật thực hành phổ biến dày 646 trang, trong đó bốn chương bàn về lưu lượng "
        "kế tuabin, lưu lượng kế cho ngành thực phẩm dược phẩm, lưu lượng kế kiểu chèn và các vấn đề "
        "chuyển giao thương mại."))
    b.append(p(
        "A. J. Nicholl, “Factors affecting the performance of turbine meters”, <i>Brown Bov. Rev.</i>, "
        "64(11), 684–692, 1977, mô tả một số yếu tố thiết kế cơ bản ít được bàn ở nơi khác."))
    b.append(p(
        "J. W. DeFeo, “Turbine flowmeters for measuring cryogenic liquids”, <i>Adv. Instrum. Proc.</i>, "
        "47 pt.1, 465–472, ISA, 1992, đưa ra hướng dẫn cho một ứng dụng ít được bàn tới, trong đó "
        "tuabin hướng trục làm việc tốt."))
    b.append(p(
        "ATS, “Standardization of spirometry, 1994 Update”, <i>Am. J. Respir. Care Med.</i>, 152, "
        "1107–1136, 1995, là bản mới nhất của hướng dẫn chính thức Hoa Kỳ về phế dung do Hiệp hội Lồng "
        "ngực Hoa Kỳ soạn."))
    b.append(p(
        "M. D. Lebowitz, “The use of expiratory flow rate measurements in respiratory disease”, "
        "<i>Ped. Pulmonol.</i>, 11, 166–174, 1991, điểm lại giá trị chẩn đoán của lưu lượng thở ra "
        "đỉnh (PEFR) khi dùng phế dung kế xách tay."))
    b.append(p(
        "W. M. Jungowski và M. H. Weiss, “Effects of flow pulsation on a single-rotor turbine meter”, "
        "<i>Trans. ASME, J. Fluids Eng.</i>, 118(1), 198–201, 1996."))
    b.append(p(
        "C. R. Sparks và R. J. McKee, “Method and apparatus for assessing and quantifying pulsation "
        "induced error in gas turbine flow meters”, U.S. Patent No. 5,481,924, 1996, được giao cho Gas "
        "Research Institute, Chicago, là một lời giải tiềm năng cho bài toán đo chính xác dòng khí "
        "mạch động, sẽ cần được phát triển kỹ thuật và một cảm biến tốc độ quay hiệu năng cao [29]."))
    b.append(p(
        "K. Ogawa, S. Ito và C. Kuroda, “Laminar-turbulent velocity profile transition for flows in "
        "concentric annuli, parallel plates and pipes”, <i>J. Chem. Eng. Japan</i>, 13(3), 183–188, "
        "1990, trình bày mô tả toán học của các biên dạng vận tốc."))
    b.append(p(
        "J. Lui và B. Huan, “Turbine meter for the measurement of bulk solids flow rate”, <i>Powder "
        "Technol.</i>, 82, 145–151, 1995, mô tả lý thuyết và thực nghiệm của một thiết kế rất đơn giản "
        "cho một ứng dụng độc đáo, đó là đo thể tích dòng nút của cát trong ống."))
    return "".join(b)


def sec_28_4_en():
    b = []
    b.append(h2("28.4 Turbine and Vane Flowmeters", "Turbine and Vane Flowmeters"))
    b.append(p("David Wadlow — Sensors Research Consulting."))
    b.append(p(
        "This section describes a range of closed-conduit flowmeters that use rotating vaned "
        "transduction elements, with particular emphasis on axial turbine flowmeters. Single-jet and "
        "insertion tangential turbines, also known as paddlewheel flowmeters, are described in "
        "another section. The various vaned flowmeters used for open-channel and free-field flow "
        "measurement are not included here."))

    # ---------------------------------------------------------------- axial
    b.append(h3("Axial Turbine Flowmeters", "Axial Turbine Flowmeters"))
    b.append(p(
        "The modern axial turbine flowmeter, when properly installed and calibrated, is a reliable "
        "device capable of providing the highest accuracies attainable by any currently available "
        "flow sensor for both liquid and gas volumetric flow measurement. It is the product of "
        "decades of intensive innovation and refinement of the original axial vaned flowmeter "
        "principle first credited to Woltman in 1790, at that time applied to measuring water flow. "
        "The initial impetus for modern development activity was largely the increasing need of the "
        "U.S. natural gas industry in the late 1940s and 1950s for a means to measure accurately the "
        "flow in large-diameter, high-pressure, interstate natural gas lines. Today, because of the "
        "tremendous success of this principle, axial turbine flowmeters of different and often "
        "proprietary designs are used in a variety of applications where accuracy, reliability and "
        "rangeability are required, in numerous major industries besides water and natural gas — oil, "
        "petrochemical, chemical process, cryogenics, milk and beverage, aerospace, biomedical and "
        "others."))
    b.append(p(
        "Figure 28.30 is a schematic longitudinal section through the axis of symmetry depicting the "
        "key components of a typical meter. The meter is an in-line sensor comprising a single turbine "
        "rotor, concentrically mounted on a shaft within a cylindrical housing through which the flow "
        "passes. The shaft or shaft bearings are located by end supports inside suspended upstream and "
        "downstream aerodynamic structures called diffusers, stators, or simply cones. The flow thus "
        "passes through an annular region occupied by the rotor blades. The blades, usually flat but "
        "sometimes slightly twisted, are inclined at an angle to the incident flow velocity and hence "
        "experience a torque that drives the rotor. The rate of rotation — up to several × 10⁴ rpm for "
        "smaller meters — is detected by a pickup, usually of the magnetic type, and registration of "
        "each rotor blade passing infers the passage of a fixed volume of fluid."))
    b.append(fig(30, F.fig(30), "en"))

    b.append(h4("General Performance Characteristics", "General Performance Characteristics"))
    b.append(p(
        "Axial turbines perform best when measuring clean, conditioned, steady flows of gases and "
        "liquids with low kinematic viscosities (below about 10⁻⁵ m²/s, 10 cSt, although they are used "
        "up to 10⁻⁴ m²/s, 100 cSt), and are linear for subsonic, turbulent flows. Under these "
        "conditions the inherent mechanical stability of the meter design gives rise to excellent "
        "repeatability. Not including the special case of water meters, described later, the main "
        "performance characteristics are:"))
    b.append(ul([
        "Sizes (internal diameter) range from 6 mm to 760 mm (1/4 in. to 30 in.).",
        "Maximum measurement capacities range from 0.025 A m³/h to 25,500 A m³/h (0.015 ACFM to "
        "15,000 ACFM) for gases and 0.036 m³/h to 13,000 m³/h (0.16 gpm to 57,000 gpm, or 82,000 "
        "barrels per hour) for liquids, where A denotes actual.",
        "Typical measurement repeatability is ±0.1% of reading for liquids and ±0.25% for gases, with "
        "up to ±0.02% for high-accuracy meters. Typical linearities (before electronic linearization) "
        "are between ±0.25% and ±0.5% of reading for liquids, and ±0.5% and ±1.0% for gases. "
        "High-accuracy meters have linearities of ±0.15% for liquids and ±0.25% for gases, usually "
        "specified over a 10:1 dynamic range below maximum rated flow. Traceability to NIST (National "
        "Institute of Standards and Technology) is frequently available, allowing one to estimate the "
        "overall absolute accuracy of a flowmeter under specified conditions. Under ideal conditions, "
        "absolute accuracies for optimum designs and installations can come close to the accuracy "
        "capabilities at NIST, which are stated as ±0.13% for liquid flows and ±0.25% for air.",
        "Rangeability, when defined as the ratio of flow rates over which the linearity specification "
        "applies, is typically between 10:1 and 100:1.",
        "Operating temperature ranges span −270 °C to 650 °C (−450 °F to 1200 °F).",
        "Operating pressure ranges span coarse vacuum to 414 MPa (60,000 psi).",
        "Pressure drop at the maximum rated flow rate ranges from around 0.3 kPa (0.05 psi) for gases "
        "to in the region of 70 kPa (10 psi) for liquids.",
    ]))

    # ---------------------------------------------------------------- theory
    b.append(h3("Theory", "Theory"))
    b.append(p(
        "There are two approaches described in the current literature for analysing axial turbine "
        "performance. The first describes the fluid driving torque in terms of momentum exchange; the "
        "second describes it in terms of aerodynamic lift via airfoil theory. The former has the "
        "advantage that it readily produces analytical results describing basic operation, some of "
        "which have not appeared via airfoil analysis. The latter allows more complete descriptions "
        "using fewer approximations, but is mathematically intensive and leads rapidly into "
        "computer-generated solutions. One prominent pioneer of the momentum approach is Lee [1] who, "
        "using this approach, later went on to invent one of the few currently successful dual-rotor "
        "turbine flowmeters, while Thompson and Grey [2] provided one of the most comprehensive models "
        "currently available using the airfoil approach, which for example took into account blade "
        "interference effects. In the following, the momentum exchange approach is used to highlight "
        "the basic concepts of the axial turbine flowmeter."))
    b.append(p(
        "In a hypothetical situation where there are no forces acting to slow down the rotor, it will "
        "rotate at a speed that exactly maintains the fluid flow velocity vector at the blade "
        "surfaces. Figure 28.31 is a vector diagram for a flat-bladed rotor with a blade pitch angle "
        "equal to β. Assuming that the rotor blades are flat and that the velocity is everywhere "
        "uniform and parallel to the rotor axis, then referring to Figure 28.31, one obtains:"))
    b.append(fig(31, F.fig(31), "en"))
    b.append(eq("rω<sub>i</sub> = tanβ / V", "28.47"))
    b.append(p("When one introduces the total flow rate, this becomes:"))
    b.append(eq("ω<sub>i</sub> / Q = tanβ / (<span style='text-decoration:overline'>r</span> A)", "28.48"))
    b.append(defs([
        ("ω<sub>i</sub>", "“ideal” rotational speed"),
        ("Q", "volumetric flow rate"),
        ("A", "area of the annular flow cross-section"),
        ("<span style='text-decoration:overline'>r</span>", "root-mean-square of the inner and outer blade radii, (R, a)"),
    ]))
    b.append(p(
        "Eliminating the time dimension from the left-hand-side quantity reduces it to the number of "
        "rotor rotations per unit fluid volume, which is essentially the flowmeter K factor specified "
        "by most manufacturers. Hence, according to Equation 28.48, in the ideal situation the meter "
        "response is perfectly linear and determined only by geometry. (In some designs the rotor "
        "blades are helically twisted to improve efficiency, especially blades with large radius "
        "ratios, (R/a). If the flow velocity profile is assumed flat, the blade angle in this case can "
        "be described by tanβ = constant × r; this is sometimes called the “ideal” helical blade.) In "
        "practice there are instead a number of rotor retarding torques of varying relative "
        "magnitudes. Under steady flow, the rotor assumes a speed that satisfies the following "
        "equilibrium:"))
    b.append(eq(
        "Fluid driving torque = rotor blade surfaces fluid drag torque<br>"
        "+ rotor hub and tip clearance fluid drag torque<br>"
        "+ rotation sensor drag torque + bearing friction retarding torque", "28.49"))
    b.append(p(
        "Referring again to Figure 28.31, the difference between the actual rotor speed, rω, and the "
        "ideal rotor speed, rω<sub>i</sub>, is the rotor slip velocity due to the combined effect of "
        "all the rotor retarding torques described in Equation 28.49; as a result the fluid velocity "
        "vector is deflected through an exit or swirl angle, θ. Denoting the radius variable by r, and "
        "equating the total rate of change of angular momentum of the fluid passing through the rotor "
        "to the retarding torque, one obtains:"))
    b.append(eq("∫<sub>a</sub><sup>R</sup> [ρQ·2πr²(rω<sub>i</sub> − rω)] / [π(R² − a²)] dr = N<sub>T</sub>", "28.50"))
    b.append(p("which yields:"))
    b.append(eq("<span style='text-decoration:overline'>r</span>²ρQ(ω<sub>i</sub> − ω) = N<sub>T</sub>", "28.51"))
    b.append(p(
        "where ρ is the fluid density and N<sub>T</sub> is the total retarding torque. Combining "
        "Equations 28.47 and 28.51 and rearranging yields:"))
    b.append(eq("ω / Q = tanβ / (<span style='text-decoration:overline'>r</span> A) − N<sub>T</sub> / (<span style='text-decoration:overline'>r</span>²ρQ²)", "28.52"))
    b.append(p(
        "The trends evident in Equation 28.52 reflect the characteristic decline in meter response at "
        "very low flows, and why lower-friction bearings and lower-drag pickups tend to be used in gas "
        "versus liquid applications and in small-diameter meters. In most designs, especially for "
        "liquids, the latter three of the four retarding torques described in Equation 28.49 are small "
        "under normal operating conditions compared with the torque due to induced drag across the "
        "blade surfaces. As shown in Figure 28.31, the force F due to this effect acts along the blade "
        "surface and has a magnitude given by:"))
    b.append(eq("F = (ρV² / 2) C<sub>D</sub> S", "28.53"))
    b.append(p(
        "where C<sub>D</sub> is the drag coefficient and S is the blade surface area per side. Using "
        "the expression for drag coefficient corresponding to turbulent flow, selected by Pate et al. "
        "[3] and others, this force can be estimated by:"))
    b.append(eq("F = ρV² × 0.074 Re<sup>−0.2</sup> × S", "28.54"))
    b.append(p(
        "where Re is the flow Reynolds number based on the blade chord shown as dimension c in Figure "
        "28.31. Assuming θ is small compared with β, then after integration the magnitude of the "
        "retarding torque due to induced drag along the blade surfaces of a rotor with n blades is "
        "found to be:"))
    b.append(eq("N<sub>D</sub> = n(R + a)ρV² × 0.037 Re<sup>−0.2</sup> × S × sinβ", "28.55"))
    b.append(p("Combining Equations 28.55 and 28.52, and rearranging, yields:"))
    b.append(eq("ω / Q = tanβ / (<span style='text-decoration:overline'>r</span> A) − 0.036 n(R + a) S A² Re<sup>−0.2</sup> sinβ / <span style='text-decoration:overline'>r</span>²", "28.56"))
    b.append(note(
        "<b>Translator’s note.</b> Three slips in the printed source are reproduced as they stand. "
        "First, (28.47) should read rω<sub>i</sub> = V·tanβ: the printed form is not dimensionally "
        "consistent with (28.48) and contradicts the vector diagram of Figure 28.31. Second, the "
        "factor in (28.56) should be S/A² — that is, a denominator of <span style='text-decoration:overline'>r</span>²A² — not S·A², otherwise it "
        "does not follow from (28.52) and (28.55). Third, the coefficient 0.036 in (28.56) should be "
        "0.037 as in (28.55)."))
    b.append(p(
        "Equation 28.56 is an approximate expression for the K factor because it neglects several of "
        "the rotor retarding torques and a number of important detailed design and aerodynamic "
        "factors, such as rotor solidity and flow velocity profile. Nevertheless it reveals that "
        "linearity variations under normal specified operating conditions are a function of certain "
        "basic geometric factors and Reynolds number. These results reflect general trends that "
        "influence design and calibration. Additionally, the marked departure from an approximate ρV² "
        "(actually ρ<sup>0.8</sup>V<sup>1.8</sup>μ<sup>−0.2</sup> via Re in Equation 28.54) dependence "
        "of the fluid drag retarding torque on flow properties under turbulent flow, to other "
        "relationships under transitional and laminar flow, gives rise to major variations in the K "
        "factor versus flow rate and media properties at low flow Reynolds numbers. This is the key "
        "reason why axial turbine flowmeters are generally recommended for turbulent flow "
        "measurement."))

    # ---------------------------------------------------------------- calibration
    b.append(h3("Calibration, Installation, and Maintenance", "Calibration, Installation, and Maintenance"))
    b.append(p(
        "Axial turbine flowmeters have a working dynamic range of at least 10:1 over which linearity "
        "is specified. The maximum flow rate is determined by design factors relating size to maximum "
        "pressure drop and maximum rotor speed; the minimum of the range is determined by the "
        "linearity specification itself. Owing to small, unavoidable manufacturing variances, "
        "linearity error curves are unique to individual meters and are normally provided by the "
        "manufacturer. However, although recommended where possible, the conditions of the "
        "application cannot usually — and need not necessarily — duplicate those of the initial or "
        "even subsequent calibrations. This has pivotal importance where actual operating conditions "
        "are extreme or the medium is expensive or difficult to handle. Figure 28.32 depicts a "
        "typically shaped calibration curve of linearity versus flow rate expressed in multiple "
        "alternative measures, various combinations of which can be found in current use. The "
        "vertical axis thus represents either the linearity error as a percentage of flow rate, a K "
        "factor expressed as the number of pulses from the rotation sensor output per volume of "
        "fluid, or the deviation from 100% registration; the latter applies only to flowmeters with "
        "mechanical pickups. The horizontal axis can be expressed as flow rate in volume units per "
        "time, Reynolds number (Re), or pulse frequency (from the rotation sensor, for non-mechanical "
        "types) divided by kinematic viscosity, (f/v), in units of Hz per m²/s (Hz/cSt or Hz/SSU; "
        "10⁻⁶ m²/s = 1 centistoke = 31.0 seconds, Saybolt Universal), where kinematic viscosity is the "
        "ratio of absolute viscosity (μ) to density. Calibrations are preferably expressed versus Re "
        "or f/v, which is proportional to Re. The hump shown in the curve is a characteristic "
        "frequently observed at lower Re and is due to velocity profile effects. K factor versus f/v "
        "calibration curves are specifically called universal viscosity curves (UVC) and, for most "
        "meters, are available from the manufacturer for an extra charge. A key utility of the UVC is "
        "that where media type and properties differ significantly from those of the original "
        "calibration, accuracies much greater than the overall linearity error can still readily be "
        "obtained via the flowmeter UVC if the kinematic viscosity of the application is known. An "
        "alternative, advanced calibration technique [4] is to provide response in terms of Strouhal "
        "number versus Re, or Roshko number. This approach is not widely adopted, but is particularly "
        "relevant to high-accuracy and extreme-temperature applications because it further allows "
        "correct compensation for flowmeter thermal expansion errors."))
    b.append(fig(32, F.fig(32), "en"))
    b.append(p(
        "The accuracy of axial turbine flowmeters is reduced by unconditioned flow, especially swirl. "
        "An installation incorporating flow conditioners along with specific upstream and downstream "
        "straight pipe lengths is generally recommended [5]. Some axial turbine flowmeters can be "
        "purchased with additional large flow straighteners that mount directly ahead of the meter "
        "body, or with conditioning plates integral to the body. The manufacturer is the first source "
        "of information regarding installation. Errors due to flow velocity pulsations are another "
        "concern, particularly in certain gas installations; however, no standard technique for "
        "effectively counteracting this source of error has yet been adopted. Periodic maintenance, "
        "testing and recalibration is required because the calibration will shift over time due to "
        "wear, damage or contamination. For certain applications, especially those involving custody "
        "transfer of oil and natural gas, national standards, international standards and other "
        "recommendations exist that specify the minimum requirements for turbine meters with respect "
        "to these aspects [6–10]."))

    # ---------------------------------------------------------------- design
    b.append(h3("Design and Construction", "Design and Construction"))
    b.append(p(
        "There are numerous, often proprietary designs incorporating variations in rotors, bearings, "
        "pickups and other components in form and materials, tailored to different applications. "
        "Meter bodies are available with a wide range of standard end-fittings. Within application "
        "constraints, the primary objective is usually to optimize overall mechanical stability and "
        "fit in order to achieve good repeatability. Design considerations for performance, "
        "application and manufacture affect every internal component, but most of all the rotor — "
        "with respect to blade shape and pitch, blade count, balance and rigidity versus drag, stress "
        "and inertia; the bearings — with respect to precision versus friction, speed rating and "
        "durability; and the rotation pickup — with respect to performance and drag."))
    b.append(p(
        "Most low-radius-ratio blades are machined flat, while high-ratio blades tend to be twisted. "
        "The blade count varies from about 6 to 20 or more, depending on the pitch angle and blade "
        "radius ratio, so that the required rotor solidity is achieved. Rotor solidity is a measure of "
        "the “openness” to the flow: higher-solidity rotors are more highly coupled to the flow and "
        "achieve a better dynamic range. The pitch angle, which primarily determines rotor speed, is "
        "typically 30° to 45° but can be lower in flowmeters designed for low-density gas "
        "applications. Rotor assemblies are usually a close fit to the inside of the housing. In "
        "large-diameter meters the rotor often incorporates a shroud around the outer perimeter for "
        "enhanced stability. Also, since large meters are often used for heavy petroleum products, by "
        "selection of a suitable wall clearance the fluid drag resulting from this clearance gap is "
        "often designed to offset the tendency at high media viscosities for the meter to speed up at "
        "lower Reynolds numbers. Materials of construction range from non-magnetic to magnetic steels "
        "to plastics."))
    b.append(p(
        "Stainless steel ball bearings tend to be used for gas meters and low-lubricity liquids such "
        "as cryogenic liquids and freon, while combination tungsten carbide or ceramic journal and "
        "thrust bearings are often considered best for many other liquid meters, depending on the "
        "medium lubricity. Fluid bearings (sometimes called “bearingless” designs) are often used in "
        "conjunction with the latter, but also sometimes with gases, to reduce drag. They operate by "
        "various designs that use flow-induced forces to balance the rotor away from the shaft ends. "
        "Bearing lubrication is either derived from the metered medium or provided by an internal or "
        "external system. The more fragile jewelled pivot bearings are also used in certain gas "
        "applications and small meters. Sanitary meters can incorporate flush holes in the bearing "
        "assembly to meet 3A crack and crevice standards."))
    b.append(p(
        "The most common types of rotation sensor are magnetic, modulated carrier and mechanical, "
        "while optical, capacitive and electric resistance types are also used. In research, a "
        "modulated nuclear radiation flux rotation sensor for use in certain nuclear reactors has also "
        "been reported [11, 12]. Mechanical pickups, which sometimes incorporate a magnetic coupling, "
        "are traditional in some applications and can have high resolution; one advantage is that "
        "they require no electric power, but the pickup drag tends to be high. The magnetic and "
        "modulated carrier types use at least a coil in a pickup assembly that screws into the meter "
        "housing near the rotor. In magnetic inductance types, now less common, the blades or shroud "
        "carry magnetized inserts and signals are induced in the coil by the traversing magnetic "
        "fields. In the more prevalent magnetic reluctance type — an example of which is schematically "
        "depicted in Figure 28.30 — the coil is wrapped around a permanent magnet or magnet pole piece "
        "in the pickup assembly, mounted next to a high-permeability bladed rotor (or machined "
        "shroud). The latter is typically made of a magnetic grade of stainless steel such as 416, 430 "
        "or 17-4Ph. As the rotor turns, the reluctance of the magnetic circuit varies, producing "
        "signals in the coil. In the more expensive modulated carrier types the rotor need only be "
        "electrically conductive: the coil is part of a radio frequency (RF) oscillator circuit and "
        "the proximity of the rotor blades changes the circuit impedance, giving rise to modulation at "
        "a lower frequency that is recovered. RF types have much lower drag, higher signal levels at "
        "low flow, and can operate at temperatures above the Curie point of typical ferromagnetic "
        "materials; they are preferred for wide dynamic range and high-temperature applications. "
        "Bidirectional flowmeters usually have two magnetic pickups to determine flow direction, which "
        "is useful for example in monitoring container filling and emptying in sanitary applications. "
        "Multiple magnetic pickups are also used in some designs to provide increased measurement "
        "resolution."))
    b.append(p(
        "Regarding output, various pulse amplifiers, totalizers, flow computers for gas pressure and "
        "temperature correction, along with 4–20 mA and other standard interface protocols, are "
        "available to suit particular applications. As an example of advanced transmitters, at least "
        "one manufacturer (EG&amp;G Flow Technology, Inc.) provides a real-time, miniature, "
        "reprogrammable “smart” transmitter integrated into the pickup housing together with a meter "
        "body temperature sensor, for full viscosity compensation and UVC linearization. These are for "
        "dedicated applications, such as airborne fuel management, where the medium "
        "viscosity–temperature relationship is known."))
    b.append(p(
        "Certain applications have uniquely different design requirements and solutions; two are "
        "discussed separately below."))

    b.append(h4("Propeller Meters", "Propeller Meters"))
    b.append(p(
        "Propeller meters are used in municipal, irrigation or wastewater measurement. Although in "
        "some designs propeller and turbine meters look almost identical and operate on the same "
        "axial rotor principle, this type of flowmeter is currently commercially and officially [13, "
        "14] distinguished as a separate category, distinct from the axial turbine. Diameters up to "
        "2440 mm (96 in.) are available. The flow capacity of a 1800 mm (72 in.) diameter propeller "
        "meter is up to about 25,000 m³/h (110,000 gpm). Typical accuracies are ±2% of reading. A "
        "primary requirement is ruggedness, and it is in the designs most suited to harsh environments "
        "that the formats are most distinctive. Rotor and pickup assemblies are generally flanged to "
        "the housing and removable. The rotors have large clearances, are often cantilevered into the "
        "flow, and are supported via a sealed bearing without stators. They are typically made of "
        "plastic or rubber and carry as few as three highly twisted, high-radius-ratio blades. Pickups "
        "are always mechanical and frequently have magnetic couplings."))

    b.append(h4("Spirometers", "Spirometers"))
    b.append(p(
        "Monitoring spirometers measure the volumes of gas flows entering and leaving the lungs and "
        "can also be incorporated in ventilator circuits. Diagnostic spirometers monitor the degree "
        "and nature of respiration; with these a clinician can determine patient respiratory condition "
        "by various measures and clinical manoeuvres. Low cost, light weight, speed of response and "
        "patient safety are major considerations. Measurement capabilities include the gas volume of a "
        "single exhalation and, for diagnostic types, the peak expiratory flow, measured in litres and "
        "litres per second respectively. Various technologies are used. However, the Wright "
        "respirometer, named after the original inventor [15], today refers to a type of hand-held "
        "monitoring spirometer that uses a special tangential turbine transducer with a two-bladed "
        "rotor connected to a mechanical pickup and a dial readout for the volume. These spirometers "
        "are routinely used by respiratory therapists for patient weaning and ventilator checking. "
        "Other axial-turbine-based flowmeters are available for ventilation measurements, for example "
        "patient metabolic measurements. One axial-turbine-based diagnostic spirometer made by Micro "
        "Medical, Ltd. currently claims most of the European market; it uses an infrared optical "
        "pickup and has a battery-powered microprocessor-controlled display. In these medical devices "
        "the rotors tend to be plastic with a large blade radius ratio, flow conditioning is minimal "
        "or absent, and the meters are typically accurate to ± a few percent of reading. In the U.S., "
        "spirometers are designated class 2 medical devices and as such certain FDA approvals are "
        "required concerning manufacture and marketing; in the EU they are class IIb devices under a "
        "different system, and other approvals are required."))

    b.append(h4("Dual-Rotor Axial Turbines", "Dual-Rotor Axial Turbines"))
    b.append(p(
        "Dual-rotor axial turbines have performance features not found in single-rotor designs. In "
        "1981 Lee et al. [16] were issued a U.S. patent for a self-correcting, self-checking "
        "dual-rotor turbine flowmeter, currently manufactured exclusively by Equimeter, Inc. and sold "
        "as the Auto-Adjust. This is a high-accuracy flowmeter primarily intended for large natural "
        "gas lines where even small undetected measurement errors can be costly. It incorporates two "
        "closely coupled turbine rotors that rotate in the same direction. The upstream rotor is the "
        "main rotor; the second rotor, which has a much shallower blade angle, is the sensor rotor. "
        "Continuous and automatic correction of measurement errors due to varying bearing friction is "
        "achieved by calculating the flow rate from the difference between the rotor speeds. As shown "
        "in Figure 28.31 and discussed in the theory section, the flow exit angle is due to the net "
        "rotor retarding torque: if this torque increases in the main rotor, reducing its speed, the "
        "exit angle increases and the speed of the sensor rotor is also reduced. The meter is also "
        "insensitive to inlet swirl angle, because swirl affects both rotor speeds in the same sense "
        "and the effect is then subtracted in the flow calculation. The meter also checks itself for "
        "wear and faults by monitoring the ratio of the two rotor speeds and comparing this with the "
        "installation value [17]."))
    b.append(p(
        "A dual-rotor liquid flowmeter invented by Ruffner et al. [18] was recently introduced by "
        "Exact Flow, LLC. It is offered as a high-accuracy flowmeter (up to ±0.1% accuracy and ±0.02% "
        "repeatability) with an extraordinarily wide dynamic range of 500:1 on a single-viscosity "
        "liquid. It has had early commercial success in fuel flow measurement in large jet engine test "
        "stands, where the wide dynamic range is particularly useful [19]. The meter comprises two "
        "closely and hydraulically coupled rotors that rotate in opposite directions; because of the "
        "exit angle generated by the first rotor, the second continues to rotate to much lower flow "
        "rates than the first."))

    b.append(h4("Two-Phase Flow Measurement Using Axial Turbines",
                "Two-Phase Flow Measurement Using Axial Turbines"))
    b.append(p(
        "A differential-pressure-producing flowmeter such as a venturimeter in series with a turbine "
        "is known to be a technically appropriate and straightforward method for measuring the "
        "volumetric and mass flow rates of some fine solid aerosols. This section, however, "
        "highlights a current research area in the application of axial rotor turbine meters to a "
        "range of industrial flow measurement problems where gas/liquid two-phase flows are "
        "encountered. Customarily, turbine meters are not designed for and cannot measure such flows "
        "accurately: errors of the order of 10% arise in metering liquids with void fractions of "
        "around 20%. Such flows are normally measured after gas separators. Although the problem is "
        "not restricted to these industries, the current main impetuses for research are direct "
        "measurement of crude oil in offshore multiphase production systems, measurement of "
        "water/steam mixtures in the cooling loops of nuclear reactors, and measurement of freon "
        "liquid–vapour flows in refrigeration and air conditioning equipment. Several techniques "
        "investigated so far use an auxiliary sensor — either a void fraction sensor or a pressure "
        "drop device such as a venturimeter or drag disk, of which the pressure drop approach appears "
        "technically more promising [20, 21]. From a practical standpoint, gamma densitometers for "
        "measuring void fraction are additional and expensive equipment, and are not, for example, "
        "well adapted to undersea oil fields. Two techniques currently being studied do not require an "
        "auxiliary in-line sensor. The first uses the turbine meter itself as the drag body and "
        "combines the turbine output with that of a small differential pressure sensor connected "
        "across the inlet and outlet regions; it requires a homogenizer ahead of the turbine, and "
        "accuracies of ±3% for the volumetric flow rates of both phases have recently been reported "
        "for air/water mixtures up to a void fraction of 80% [22]. The second is based entirely on "
        "analysis of the turbine output signal and has provided significant correlations of the signal "
        "fluctuations with void fraction; accuracies of ±2% for water volumetric flow rate have been "
        "reported for air/water mixtures with void fractions up to 25% [23]."))

    b.append(h4("Insertion Axial Turbine Flowmeters", "Insertion Axial Turbine Flowmeters"))
    b.append(p(
        "These flowmeters comprise a small axial rotor mounted on a stem inserted radially through the "
        "conduit wall, often through a shut-off valve. They measure the flow velocity at the rotor "
        "position, from which the volumetric flow rate is inferred. They are an economical solution "
        "where pipe diameters are large and accuracy requirements moderate, and may also be "
        "technically preferred where negligible pressure drop is an advantage, as in high-speed flows. "
        "They are typically more linear than insertion tangential turbine flowmeters and compete also "
        "with magnetic and vortex shedding insertion flowmeters. They are available for a range of "
        "liquids and gases, including steam, similar to the media range of full-bore axial turbines, "
        "and have a similarly linear response. Flow Automation, Inc. is currently the leading "
        "manufacturer. The rotors, usually metal but sometimes plastic, typically have diameters of 25 "
        "mm to 51 mm (1 in. to 2 in.) and can be inserted into pipes from 51 mm to 2032 mm (2 in. to "
        "80 in.). Velocity ranges cover 0.046 m/s to 91 m/s (9 fpm to 18,000 fpm) for gases and 0.03 "
        "m/s to 30 m/s (6 fpm to 6000 fpm) for liquids; dynamic ranges vary between 10:1 and 100:1. "
        "The maximum flow capacity in a 1836 mm (72 in.) pipe can be nearly 56,500 m³/h (about "
        "250,000 gpm). Since these devices are local velocity sensors, calculating the volumetric flow "
        "rate requires knowledge of the area velocity profile and the actual flow area. Flow "
        "conditioning is therefore particularly important for accurate volumetric measurement, while "
        "radial positioning — a further responsibility of the user — must follow the manufacturer’s "
        "recommendation, which can be centreline, one third of the diameter, 12% of the diameter, or "
        "determined by “profiling”. Quick [24] discusses operation and installation for natural gas "
        "measurement. Although linearities or “accuracies” can be quoted to ±1% of velocity, achieving "
        "the same accuracy for volumetric flow rate, although possible, can be difficult or "
        "impractical. In this respect a unique dual-rotor design, exclusive to Onicon, Inc. and "
        "primarily used for chilled-water flow measurement in HVAC systems, requires less flow "
        "conditioning than single-rotor designs. An Onicon dual-rotor turbine assembly is depicted in "
        "Figure 28.33."))
    b.append(fig(33, F.fig(33), "en"))
    b.append(p(
        "It comprises two rotors that rotate in opposite directions. The output is based on the "
        "average rotor speed. Any flow swirl present due to poor flow conditioning changes the speed "
        "of each rotor by the same but opposite amounts, so swirl-induced error is virtually absent "
        "from the averaged output; flow profile sampling is also improved over a single rotor. The "
        "devices are calibrated using a volumetric prover and the specified accuracy of ±2% of reading "
        "is for volumetric flow rate rather than velocity. This is the total error and includes an "
        "allowance for dimensional variations in industry-standard pipes."))

    b.append(h4("Angular Momentum Flowmeters", "Angular Momentum Flowmeters"))
    b.append(p(
        "These are accurate, linear, liquid mass flowmeters that use vaned components and are used in "
        "aerospace applications. They are currently the instrument of choice for airborne jet engine "
        "fuel flow measurement on large commercial aircraft and some military aircraft for afterburner "
        "applications. They are more expensive than the equivalent turbine flowmeters for this "
        "application, but provide mass flow rate directly and are unaffected by fuel density "
        "variations. Typical accuracies lie between ±0.5% and ±1.0% over a 40:1 or greater dynamic "
        "range; measurement ranges are available for fuel flows from about 0.01 to 6 kg/s (70 to "
        "46,000 PPH)."))
    b.append(p(
        "The principle of operation is long established and based on imparting angular momentum to the "
        "flow using a driven, flat-bladed impeller. The force required to drive the impeller at "
        "constant speed is monitored as a proportional indication of mass flow rate as this quantity "
        "varies. Some designs use an electric motor to drive the impeller, but the current trend is "
        "motorless: a constant driving speed in the region of 100 to 200 rpm is provided by one or "
        "more flow-driven turbine rotors. A variable shunt metering valve assembly adjacent to the "
        "turbine rotor mechanically opens and closes in response to flow dynamic pressure and thereby "
        "automatically maintains a constant speed of rotation, provided the flow rate is above the "
        "minimum of the range. The driven impeller carries vanes parallel to the flow and resides on a "
        "common axis with the turbine rotor; a flow straightener ensures parallel flow past the "
        "impeller. A carefully engineered constant-rate spring connection between turbine shaft and "
        "impeller makes the angular deflection between the two proportional to the applied torque, and "
        "this quantity is directly proportional to mass flow rate. Two pickup coils sense the "
        "rotations of the turbine and the vaned impeller, and only the time difference between the "
        "pulses in these two signals is measured and used to calculate the flow rate. Chiles et al. "
        "[25] provide a detailed illustration and explanation of the intricate mechanism."))

    b.append(h4("Multijet Turbine Flowmeters", "Multijet Turbine Flowmeters"))
    b.append(p(
        "These are linear volumetric flowmeters designed for liquid measurement, comprising a single "
        "radial-vaned impeller mounted vertically on a shaft bearing within a vertically divided flow "
        "chamber, sometimes called a distributor. The impeller is often plastic and can even be "
        "neutrally buoyant in water. There are various designs, but typically both chambers access a "
        "series of radially distributed and angled jets: the lower chamber jets connect to the meter "
        "input port and distribute the flow tangentially onto the lower region of the impeller blades, "
        "while the upper series, angled oppositely, allow the flow to exit. The flow pattern within "
        "the chamber is thus a vertical spiral, and dynamic pressure drives the impeller to track the "
        "flow. This design gives good sensitivity at low flow rates and, because of the distribution "
        "principle, the meters are also insensitive to upstream flow condition. Impeller rotation "
        "pickups are always mechanical, often magnetically coupled, and frequently also connect with "
        "electric contact transmitters. They are primarily used in water measurement, including "
        "potable water for domestic and business billing and in conjunction with energy management "
        "systems such as hot water building or district heating, and to a much lesser extent in some "
        "chemical and pharmaceutical industries for dosing and filling systems involving solvents, "
        "refrigerants, acids and alkalis with absolute viscosities below 4.5 mPa·s (0.045 poise). "
        "Available sizes range from 15 mm to 50 mm; dynamic ranges lie between 25:1 and 130:1 and flow "
        "ranges cover 0.03 to 30 m³/h (0.13 to 130 gpm). Measurement linearities range between ±1% and "
        "±2%, with typical repeatabilities of ±0.3%. Operating temperatures range from normal to 90 °C "
        "(200 °F) and maximum operating pressures are available up to 6.9 MPa (1000 psi). A number of "
        "potable water measurement systems come with sophisticated telemetry options allowing remote "
        "interrogation by radio or telephone. For potable water in the U.S. these meters normally "
        "comply with the applicable AWWA standard [26], while in Europe EEC, DIN and other national "
        "standards apply."))
    b.append(p(
        "In the author’s opinion there is also another type of vaned flowmeter that could be classified "
        "as a multijet turbine: an axially mounted vaned impeller with an upstream element that imparts "
        "a helical swirl to the flow. The transducer is typically a small, low-cost, sometimes "
        "disposable plastic component, usually designed for liquids (but also, to lower accuracies, "
        "gases) at low flow rates (down to 50 mL/min). The dynamic range is high and accuracies range "
        "up to ±0.5%. Goss [27] describes one particular design in current use; specialized "
        "applications cover the pharmaceutical, medical and beverage industries."))

    b.append(h4("Cylindrical Rotor Flowmeter", "Cylindrical Rotor Flowmeter"))
    b.append(p(
        "Instead of coupling to a turbulent flow through fluid dynamic pressure or momentum flux, as "
        "in most axial and tangential turbines, a demonstrated research device due to Wadlow et al. "
        "[28] provides linear volumetric low-gas-flow measurement using a single low-inertia smooth "
        "cylindrical tangential rotor that couples to a laminar flow via surface friction. The "
        "geometry is conceptually that of a single-surfaced rotating vane. A plane Poiseuille flow is "
        "created that passes azimuthally over most of the curved rotor surface in a narrow annular "
        "passage between rotor and concentric housing. The rotor is motor-driven through a feedback "
        "control loop connected to an error-signal-producing differential pressure sensor across the "
        "gas ports, so as to maintain meter pressure drop equal to zero. Under this condition the "
        "response, indicated by motor shaft speed, is exactly linear, determined only by geometry, and "
        "independent of gas density and viscosity. The demonstration device reported has a 40 mm "
        "diameter rotor and 15 mm diameter gas ports; it measures up to 25 Lpm bidirectionally, has a "
        "linear dynamic range greater than 100:1, is insensitive to upstream flow condition, and has a "
        "1/e step response time of 42 ms, limited only by external motor torque and combined motor and "
        "rotor inertia."))

    # ---------------------------------------------------------------- makers
    b.append(h3("Manufacturers", "Manufacturers"))
    b.append(p(
        "There is significant and dynamic competition among the numerous manufacturers of the "
        "different types of flowmeter described in this section. In all types, most manufacturers have "
        "exclusive patent rights concerning one or more detailed design aspects that make their "
        "products perform differently from those of the competition. Every few years one or more "
        "major turbine flowmeter companies can be identified that have changed ownership and name, or "
        "formed a new partnership. Identifying the competition and selecting the manufacturer are "
        "important and sometimes time-consuming parts of the flowmeter selection and specification "
        "process. To assist with this, Table 28.8 gives a few selected examples from different "
        "manufacturers of all the flowmeter types described in this section. Table 28.9 gives the "
        "corresponding contact information, along with the general types offered by each."))
    b.append(_t288("en"))
    b.append(_t289("en"))

    # ---------------------------------------------------------------- conclusion
    b.append(h3("Conclusion", "Conclusion"))
    b.append(p(
        "However anachronistic intricate mechanical sensors might appear amid everyday high "
        "technology, there are fundamental reasons why axial turbines are likely to experience "
        "continued support and development rather than obsolescence, especially for in-line "
        "applications requiring in the region of tenth-percent volumetric accuracy. Mechanical "
        "coupling is the most direct volume interaction for a flowing fluid, which is why mechanical "
        "meters historically developed first and continue to be the most accurate and reliable types "
        "of flowmeter for so many different fluids. Other non-mechanical — perhaps higher-technology "
        "or newer — approaches thus face high demands for accurate compensation to render such less "
        "directly volume-coupled techniques as generally accurate, or more accurate. This is because "
        "the error in each corrected factor or assumption in an indirect technique contributes to the "
        "overall error. The technology of high-accuracy flowmeters continues to be driven by "
        "applications such as custody transfer of valuable oil and natural gas, which demand high "
        "accuracy and reliability. There is a continuing demand for accurate and reliable water "
        "flowmeters. By reason of long proven field experience, turbine and other vane-type devices "
        "have become one of a few broadly accepted techniques in many major applications such as these "
        "where the demand for flow sensors is significant or growing."))

    # ---------------------------------------------------------------- refs
    b.append(h3("References", "References"))
    b.append(wl([
        "[1] W. F. Z. Lee and H. J. Evans, “Density effect and Reynolds number effect on gas turbine "
        "flowmeters”, <i>Trans. ASME, J. Basic Eng.</i>, 87(4): 1043–1057, 1965.",
        "[2] R. E. Thompson and J. Grey, “Turbine flowmeter performance model”, <i>Trans. ASME, J. "
        "Basic Eng.</i>, 92(4), 712–723, 1970.",
        "[3] M. B. Pate, A. Myklebust and J. H. Cole, “A computer simulation of the turbine flow meter "
        "rotor as a drag body”, <i>Proc. Int. Comput. in Eng. Conf. and Exhibit 1984</i>, Las Vegas: "
        "184–191, New York: ASME, 1984.",
        "[4] P. D. Olivier and D. Ruffner, “Improved turbine meter accuracy by utilization of "
        "dimensionless data”, <i>Proc. 1992 National Conf. Standards Labs. (NCSL) Workshop and "
        "Symp.</i>, Boulder, CO: NCSL, 1992, 595–607.",
        "[5] ISA-RP 31.1, <i>Specification, Installation and Calibration of Turbine Flowmeters</i>, "
        "Research Triangle Park, NC: ISA, 1977.",
        "[6] ANSI/ASME MFC-4M-1986 (R1990), <i>Measurement of Gas Flow by Turbine Meters</i>, New "
        "York: ASME.",
        "[7] API MPM, <i>Measurement of Liquid Hydrocarbons by Turbine Meters</i>, 3rd ed., "
        "Washington, D.C.: API (Amer. Petroleum Inst.), 1995, chap. 5.3.",
        "[8] AGA Transmission Meas. Committee Rep. No. 7, <i>Measurement of fuel gas by turbine "
        "meters</i>, Arlington, VA: AGA (Amer. Gas Assoc.), 1981.",
        "[9] Int. Recommendation R32, <i>Rotary piston gas meters and turbine gas meters</i>, Paris: "
        "OIML (Int. Organization of Legal Metrology), 1989.",
        "[10] ISO 9951:1993, <i>Measurement of gas flow in closed conduits — turbine meters</i>, "
        "Geneva, Switzerland: Int. Organization for Standardization (also available ANSI), 1993.",
        "[11] T. H. J. J. Van Der Hagen, “Proof of principle of a nuclear turbine flowmeter”, <i>Nucl. "
        "Technol.</i>, 102(2), 167–176, 1993.",
        "[12] K. Termaat, W. J. Oosterkamp and W. Nissen, “Nuclear turbine coolant flow meter”, U.S. "
        "Patent No. 5,425,064, 1995.",
        "[13] AWWA C704-92, <i>Propeller-type meters for waterworks applications</i>, Denver, CO: "
        "Amer. Water Works Assoc., 1992.",
        "[14] ANSI/AWWA C701-88, <i>Cold water meters — turbine type, for customer service</i>, "
        "Denver, CO: Amer. Water Works Assoc., 1988.",
        "[15] B. M. Wright and C. B. McKerrow, “Maximum forced expiratory flow rate as a measure of "
        "ventilatory capacity”, <i>Br. Med. J.</i>, 1041–1047, 1959.",
        "[16] W. F. Z. Lee, R. V. White, F. M. Sciulli and A. Charwat, “Self-correcting "
        "self-checking turbine meter”, U.S. Patent No. 4,305,281, 1981.",
        "[17] W. F. Z. Lee, D. C. Blakeslee and R. V. White, “A self-correcting and self-checking gas "
        "turbine meter”, <i>Trans. ASME, J. Fluids Eng.</i>, 104, 143–149, 1982.",
        "[18] D. F. Ruffner and P. D. Olivier, “Wide range, high accuracy flow meter”, U.S. Patent No. "
        "5,689,071, 1997.",
        "[19] D. F. Ruffner, private communication, 1996.",
        "[20] A. Abdul-Razzak, M. Shoukri and J. S. Chang, “Measurement of two-phase refrigerant "
        "liquid-vapor mass flow rate. III. Combined turbine and venturi meters and comparison with "
        "other methods”, <i>ASHRAE Trans.: Research</i>, 101(2), 532–538, 1995.",
        "[21] W. J. Shim, T. J. Dougherty and H. Y. Cheh, “Turbine meter response in two-phase flows”, "
        "<i>Proc. Int. Conf. Nucl. Eng. — 4</i>, 1 part B: 943–953, New York: ASME, 1996.",
        "[22] K. Minemura, K. Egashira, K. Ihara, H. Furuta and K. Yamamoto, “Simultaneous measuring "
        "method for both volumetric flow rates of air-water mixture using a turbine flowmeter”, "
        "<i>Trans. ASME, J. Energy Resources Technol.</i>, 118, 29–35, 1996.",
        "[23] M. W. Johnson and S. Farroll, “Development of a turbine meter for two-phase flow "
        "measurement in vertical pipes”, <i>Flow Meas. Instrum.</i>, 6(4), 279–282, 1995.",
        "[24] L. A. Quick, “Gas measurement by insertion turbine meter”, <i>Proc. 70th Int. School "
        "Hydrocarbon Meas.</i>, OK, 1995. (Available from E. Blanchard, Arrangements Chair, "
        "Shreveport, LA, (318) 868–0603.)",
        "[25] W. E. Chiles, L. E. Vetsch and J. V. Peterson, “Shrouded flowmeter turbine and improved "
        "fluid flowmeter using the same”, U.S. Patent No. 4,012,957, 1977.",
        "[26] ANSI/AWWA C708-91, <i>Cold-water meters, multi-jet-type</i>, Denver, CO: Amer. Water "
        "Works Assoc., 1991.",
        "[27] J. Goss, “Flow meter”, U.S. Patent No. 5,337,615, 1994.",
        "[28] D. Wadlow and L. M. Layden, “Controlled flow volumetric flowmeter”, U.S. Patent No. "
        "5,284,053, 1994.",
        "[29] C. R. Sparks, private communication, 1996.",
    ]))

    b.append(h3("Further Information", "Further Information"))
    b.append(p(
        "D. W. Spitzer (ed.), <i>Flow Measurement</i>, Research Triangle Park, NC: ISA, 1991, is a "
        "popular 646-page practical engineering guide of which four chapters concern turbine "
        "flowmeters, sanitary flowmeters, insertion flowmeters and custody transfer issues."))
    b.append(p(
        "A. J. Nicholl, “Factors affecting the performance of turbine meters”, <i>Brown Bov. Rev.</i>, "
        "64(11), 684–692, 1977, describes some basic design factors not commonly discussed "
        "elsewhere."))
    b.append(p(
        "J. W. DeFeo, “Turbine flowmeters for measuring cryogenic liquids”, <i>Adv. Instrum. Proc.</i>, "
        "47 pt.1, 465–472, ISA, 1992, provides guidance for a less frequently discussed application in "
        "which axial turbines perform well."))
    b.append(p(
        "ATS, “Standardization of spirometry, 1994 Update”, <i>Am. J. Respir. Care Med.</i>, 152, "
        "1107–1136, 1995, is the latest version of the official U.S. guideline for spirometry "
        "generated by the American Thoracic Society."))
    b.append(p(
        "M. D. Lebowitz, “The use of expiratory flow rate measurements in respiratory disease”, "
        "<i>Ped. Pulmonol.</i>, 11, 166–174, 1991, reviews the diagnostic usefulness of PEFR using "
        "portable spirometers."))
    b.append(p(
        "W. M. Jungowski and M. H. Weiss, “Effects of flow pulsation on a single-rotor turbine meter”, "
        "<i>Trans. ASME, J. Fluids Eng.</i>, 118(1), 198–201, 1996."))
    b.append(p(
        "C. R. Sparks and R. J. McKee, “Method and apparatus for assessing and quantifying pulsation "
        "induced error in gas turbine flow meters”, U.S. Patent No. 5,481,924, 1996, assigned to the "
        "Gas Research Institute, Chicago, is a potential solution to the accurate measurement of "
        "pulsating gas flows which will require engineering development and a high-performance "
        "rotation sensor [29]."))
    b.append(p(
        "K. Ogawa, S. Ito and C. Kuroda, “Laminar-turbulent velocity profile transition for flows in "
        "concentric annuli, parallel plates and pipes”, <i>J. Chem. Eng. Japan</i>, 13(3), 183–188, "
        "1990, provides mathematical descriptions of velocity profiles."))
    b.append(p(
        "J. Lui and B. Huan, “Turbine meter for the measurement of bulk solids flow rate”, <i>Powder "
        "Technol.</i>, 82, 145–151, 1995, describes theory and experiments relating to a very simple "
        "design for a unique application: the volumetric measurement of plug flows of sands in a "
        "pipe."))
    return "".join(b)


def _t2810(lang):
    """Table 28.10 — U.S. manufacturers of impeller flowmeters."""
    if lang == "vi":
        hd = ("Nhà chế tạo", "Thành phố, bang", "Điện thoại")
        cap = ("Bảng 28.10 · Các nhà chế tạo lưu lượng kế cánh guồng tại Hoa Kỳ. Số điện thoại của "
               "Hoffer bị cắt cụt ngay trong bản gốc vì cột quá hẹp.")
    else:
        hd = ("Manufacturer", "City, State", "Phone number")
        cap = ("Table 28.10 · U.S. manufacturers of impeller flowmeters. Hoffer's second number is "
               "truncated in the original, where the column runs out of width.")
    rows = [
        ["Data Industrial Corp.", "Mattapoisett, MA", "(508) 758-6390"],
        ["G. Fischer (Signet)", "Tustin, CA", "(714) 731-8800"],
        ["SeaMetrics", "Kent, WA", "(206) 872-0284"],
        ["Roper Flow Technology, Inc.", "Phoenix, AZ", "(602) 437-1315"],
        ["Blancett", "Altus, OK", "(405) 482-0036"],
        ["Hoffer Flow Controls, Inc.", "Elizabeth City, NC", "(800) 628-4584; (919) 331…"],
        ["McMillan Co.", "Georgetown, TX", "(512) 863-0231"],
        ["Flowmetrics, Inc.", "Canoga Park, CA", "(818) 346-4492"],
        ["Proteus Industries, Inc.", "Mountain View, CA", "(415) 964-4163"],
    ]
    return table(hd, rows, cap, widths=("45%", "30%", "25%"))


def sec_28_5_vi():
    b = []
    b.append(h2("28.5 Lưu lượng kế cánh guồng", "Impeller Flowmeters"))
    b.append(p("Harold M. Miller — Data Industrial."))
    b.append(p(
        "Lưu lượng kế cánh guồng, đôi khi gọi là lưu lượng kế bánh guồng, là một trong những loại "
        "lưu lượng kế được dùng phổ biến nhất. Cảm biến lưu lượng kiểu cánh guồng là hậu duệ trực "
        "tiếp của chiếc guồng nước cấp dưới cổ điển. Đây là một phương án thay thế tiết kiệm cho lưu "
        "lượng kế tuabin, và có thể dùng trong những ứng dụng khó xử lý bằng các loại thiết bị đo "
        "lưu lượng khác. Về kết cấu cơ khí, chúng thường rất đơn giản; mọi sự tinh xảo đều nằm ở "
        "phần điện tử dùng để phát hiện tốc độ quay của cánh guồng, và ở việc chọn vật liệu chế tạo "
        "phù hợp với tính ăn mòn hoá học của chất lưu được đo. Chúng có họ hàng với lưu lượng kế "
        "tuabin ở chỗ cả hai loại đều dùng một phần tử cơ khí quay để tạo ra tín hiệu đầu ra. Chúng "
        "khác ở chỗ lưu lượng kế cánh guồng có trục quay vuông góc với dòng chảy, trong khi trục của "
        "lưu lượng kế tuabin song song với dòng chảy."))
    b.append(p(
        "Những thiết bị này có hai kiểu cơ bản. Kiểu chèn là phổ biến nhất (xem Hình 28.34(b) và "
        "28.35). Cảm biến được lắp trực tiếp vào một lỗ trên thành ống, với bộ nối kiểu yên ngựa "
        "hoặc bộ nối hàn đặt tại chỗ xuyên qua để làm kín cảm biến với ống. Cảm biến cũng có thể "
        "được lắp sẵn trong những ống chữ T phù hợp trên tuyến. Hầu hết nhà cung cấp đều có thiết kế "
        "lắp được vào hệ thống đường ống đang vận hành, gần như không mất chất lưu trong quá trình "
        "lắp. Kiểu cánh guồng còn được cung cấp dưới dạng cảm biến nối tiếp (xuyên dòng) cho những "
        "ứng dụng cần đến kiểu này (Hình 28.34(a)). Lưu lượng kế nối tiếp thường có độ chính xác "
        "cao hơn kiểu chèn một chút."))
    b.append(fig(34, F.fig(34), "vi"))
    b.append(p(
        "Lưu lượng kế nối tiếp là những lưu lượng kế thể tích, suy diễn, tuyến tính, dùng để đo dòng "
        "chất lỏng và chất khí, và nhạy hơn ở lưu lượng thấp so với, chẳng hạn, lưu lượng kế tuabin "
        "hướng trục. (Điều này tất nhiên là do góc tới của dòng lên cánh lớn hơn nhiều.) Ngược lại, "
        "lưu lượng kế cánh guồng kiểu chèn chỉ đo vận tốc dòng trong một vùng nhỏ bên trong ống."))
    b.append(p(
        "Nhìn chung, lưu lượng kế cánh guồng phù hợp với những dải lưu lượng thấp hơn nhiều so với "
        "tuabin hướng trục cùng cỡ, và vì thế thường được dùng ở những nơi không thể dùng tuabin "
        "hướng trục. Đó là ưu điểm chính, cùng với xu hướng giá thành thấp hơn và độ tin cậy cao. Sự "
        "cạnh tranh với tuabin hướng trục nối tiếp chỉ xảy ra ở những dải lưu lượng thiết kế chồng "
        "lấn nhau."))
    b.append(p(
        "Một số lưu lượng kế nối tiếp có các cỡ tấm orifice thay thế được, cho phép dùng cùng một "
        "thân cho nhiều dải lưu lượng khác nhau. Lưu lượng kế nối tiếp có tấm orifice điển hình là "
        "không nhạy với điều kiện dòng. Ngược lại, lưu lượng kế kiểu chèn rất nhạy với điều kiện dòng "
        "nếu lưu lượng thể tích được suy ra từ vận tốc cục bộ. Đây là một phân biệt quan trọng, và có "
        "thể mở rộng thành những khác biệt về yêu cầu đối với từng phiên bản nối tiếp cụ thể. Việc "
        "lắp đặt là quan trọng: nó ảnh hưởng tới người dùng khi thiết kế một hệ lắp đặt, khi chọn lưu "
        "lượng kế, và khi quyết định đặt bao nhiêu tin cậy vào số đọc."))
    b.append(fig(35, F.fig(35), "vi"))
    b.append(p(
        "Lưu lượng kế bánh guồng không bao giờ được dùng cho các ứng dụng chuyển giao thương mại "
        "hydrocarbon lỏng. Năng lực đo lưu lượng không đủ để cạnh tranh trong việc theo dõi những "
        "lượng chuyển giao lớn, và độ chính xác cũng không đủ cho những chất lưu có giá trị cao."))
    b.append(p(
        "Những lưu lượng kế này có nhiều tên gọi khác nhau, tuỳ theo tên mà nhà chế tạo chọn và tuỳ "
        "theo ứng dụng. Một nguồn gốc lịch sử thường được nhắc tới là tuabin xung kích do Pelton phát "
        "minh ở thế kỷ 19, và chính nó đã sinh ra cách gọi “tuabin bánh xe Pelton” mà một số nhà cung "
        "cấp hiện dùng. Một thiết bị như vậy nguyên thuỷ được dùng để dẫn động trực tiếp các bánh "
        "nghiền quay quanh trục thẳng đứng, chứ không qua một bộ truyền bánh răng vuông góc như ở "
        "bánh xe cấp dưới đã mô tả. Một tên gọi phổ biến khác, ngoài bánh guồng và kiểu cánh guồng — "
        "ít nhất là theo cách mô tả của các nhà cung cấp cho loại nối tiếp — là tuabin tiếp tuyến một "
        "tia, hay gọn hơn là tuabin tiếp tuyến. Cách gọi thứ nhất phân biệt thiết kế này với lưu "
        "lượng kế tuabin tiếp tuyến đa tia, nên đáng được nhắc tới. Như vậy hiện có một loạt tên gọi "
        "gây lẫn lộn, tất cả đều chỉ về cùng một nguyên lý đo lưu lượng bằng cánh có guồng:"))
    b.append(ol([
        "Kiểu cánh guồng: kiểu chèn và kiểu nối tiếp",
        "Kiểu bánh guồng: kiểu chèn và kiểu nối tiếp",
        "Kiểu bánh xe tuabin Pelton: kiểu nối tiếp",
        "Lưu lượng kế tuabin tiếp tuyến: kiểu chèn và kiểu nối tiếp",
        "Lưu lượng kế tuabin tiếp tuyến một tia: kiểu nối tiếp",
        "Lưu lượng kế tuabin xung kích: kiểu nối tiếp",
    ]))
    b.append(p(
        "Về lịch sử, cảm biến cánh guồng bắt nguồn từ những đồng hồ tốc độ điện tử đời đầu dùng trên "
        "ca nô giải trí. Signet, rồi ngay sau đó là Data Industrial, đã cải biến thiết kế cơ bản của "
        "những dụng cụ hàng hải ấy để đáp ứng yêu cầu tuổi thọ phục vụ khắt khe hơn nhiều của đo "
        "lường công nghiệp. Những lưu lượng kế thu được, cùng các thế hệ sau của chúng, đã được dùng "
        "rộng rãi từ năm 1975. Những nỗ lực kỹ thuật đáng kể đã cho ra đời những thiết bị có độ tin "
        "cậy cao, dùng trong nhiều ứng dụng cực kỳ khắt khe."))

    # ---------------------------------------------------------------- sensing
    b.append(h3("Nguyên lý cảm biến", "Sensing Principles"))
    b.append(p(
        "Mọi cảm biến lưu lượng kiểu cánh guồng đều phải phát hiện chuyển động quay của cánh guồng, "
        "và ở dạng thông thường thì truyền đi một chuỗi xung có tần số liên quan tới vận tốc quay của "
        "cánh. Vì đầu ra về bản chất là tín hiệu số, cảm biến cánh guồng thường truyền được tín hiệu "
        "đi khá xa, tới 1 km khi cần. Các nguyên lý phát hiện được dùng gồm:"))
    b.append(ol([
        "Một hay nhiều nam châm giữ trong cánh guồng hoặc nối cơ khí với nó, dùng điểm cắt không của "
        "một từ trường xoay chiều cảm ứng để tạo chuỗi xung.",
        "Một hay nhiều phần tử ghép nằm trong cánh guồng, điều chế một tần số được truyền đi rồi xử "
        "lý để tạo chuỗi xung.",
        "Một hay nhiều bia kim loại đặt trong cảm biến, được phát hiện bằng bất kỳ kỹ thuật đầu thu "
        "tiệm cận nào có bán trên thị trường, để tạo xung đầu ra.",
        "Một hay nhiều nam châm giữ trong cánh guồng, dùng để đóng cắt một phần tử hiệu ứng Hall, "
        "tạo chuỗi xung đầu ra.",
        "Các phần tử quang, cả kiểu truyền qua lẫn kiểu phản xạ, đã được dùng để phát hiện mỗi lần "
        "cánh guồng đi qua và tạo chuỗi xung đầu ra.",
        "Đo sự thay đổi điện kháng do các cánh guồng đi qua vùng từ trường đo, rồi xử lý thành chuỗi "
        "xung đầu ra.",
    ]))
    b.append(p(
        "Mỗi nhà cung cấp có thể chế tạo nhiều kiểu lưu lượng kế cánh guồng, mỗi kiểu dùng một phương "
        "pháp phát hiện khác nhau tuỳ yêu cầu thị trường. Vì cánh guồng có thể quay tới 4000 "
        "vòng/phút hoặc hơn, tần số đầu ra có thể cao tới 500 Hz. Ở lưu lượng thấp, tần số có thể "
        "thấp tới 0,2 Hz. Yếu tố này cần được xét sớm trong quá trình chọn thiết bị, vì thiết bị đầu "
        "ra được chọn phải đáp ứng được dải tần số đầu ra của cảm biến."))
    b.append(p(
        "Hầu hết nhà chế tạo cảm biến đều có thể cung cấp hoặc chỉ định một bộ hiển thị phù hợp để "
        "liên hệ đầu ra của cảm biến với lưu lượng theo đơn vị kỹ thuật, hoặc theo hệ đo Hoa Kỳ hoặc "
        "theo SI. Những bộ hiển thị này thường hiển thị được cả lưu lượng tức thời lẫn lưu lượng "
        "tích luỹ của cảm biến nối với nó. Có thêm các đầu ra khác, dạng độc lập hoặc kết hợp với bộ "
        "hiển thị, cung cấp xung định kỳ theo những bước lưu lượng đặt được, hoặc đầu ra tương tự "
        "được chia tỷ lệ theo lưu lượng. Ngoài ra, một số chức năng điều khiển, cảnh báo và những "
        "tính năng đặc biệt khác mà các thị trường khác nhau yêu cầu cũng thường được tích hợp trong "
        "những bộ hiển thị này."))

    # ---------------------------------------------------------------- ranges
    b.append(h3("Dải lưu lượng", "Flow Ranges"))
    b.append(p(
        "Lưu lượng kế cánh guồng kiểu chèn, kể cả khi được lắp qua ống chữ T, vẫn là một thiết bị cảm "
        "biến cục bộ: nó chỉ đo vận tốc dòng trong một phần của dòng chảy. Nhà chế tạo hiệu chuẩn lưu "
        "lượng kế theo lưu lượng trung bình trên toàn mặt cắt ống. Vị trí bánh guồng thường nằm gần "
        "đường kính trong của ống, trong một vùng dòng có vận tốc thấp hơn đáng kể so với vận tốc "
        "trung bình trong ống. Nhờ cách hiệu chuẩn đúng của nhà chế tạo, lưu lượng kế vẫn làm việc "
        "hiệu quả ở lưu lượng ứng với vận tốc trung bình chỉ 10 cm/s, bất chấp vận tốc cục bộ thấp "
        "tại cánh guồng. Nói chung, có thể đo những dòng có số Reynolds thấp tới 5000 mà không cần "
        "hiệu chuẩn đặc biệt, và thường vẫn xử lý được những số Reynolds thấp hơn mà không gặp khó "
        "khăn gì. Đặc tả dải thông thường là lưu lượng tương ứng với vận tốc trung bình từ 0,3 đến "
        "10 m/s. Sự đa dạng của sản phẩm cho phép làm việc ở vận tốc thấp hơn 0,3 m/s khá nhiều, thực "
        "tế xuống tới 0,07 m/s ở một số lưu lượng kế cánh guồng chuyên dụng."))

    # ---------------------------------------------------------------- install
    b.append(h3("Lắp đặt", "Installation"))
    b.append(h4("Cỡ ống", "Pipe sizes"))
    b.append(p(
        "Các cỡ ống mà những cảm biến này đã được lắp trải rộng từ ống cỡ nhỏ tới ống có đường kính "
        "ngoài 2,3 m. Chính những cỡ ống lớn là nơi tiết kiệm được nhiều nhất về chi phí lắp đặt so "
        "với các hệ đo khác. Thực vậy, lưu lượng kế cánh guồng có thể tiết kiệm trong bất kỳ ứng dụng "
        "đo lưu lượng nào phù hợp với độ chính xác của thiết bị, đặc biệt nếu ứng dụng có liên quan "
        "tới điều khiển bơm hoặc van."))
    b.append(h4("Hạn chế của hệ thống đường ống", "Piping system restrictions"))
    b.append(p(
        "Hầu hết nhà cung cấp yêu cầu tối thiểu 10 lần đường kính ống đoạn thẳng phía thượng nguồn "
        "và 5 lần phía hạ nguồn tính từ chỗ lắp. Những điều kiện này nhằm giảm thiểu tính bất đối "
        "xứng của dòng chảy quanh cánh guồng trong tuyến ống đã lắp, vốn có thể do khuỷu, ống chữ T "
        "và van gây ra. Càng dài càng tốt; không nhà cung cấp nào phàn nàn rằng đoạn thẳng thượng "
        "nguồn quá dài. Ngắn hơn có thể ảnh hưởng xấu tới hiệu chuẩn của cảm biến do vận tốc biến "
        "thiên cục bộ gây ra bởi nhiễu dòng."))
    b.append(h4("Áp suất làm việc", "Operating pressure"))
    b.append(p(
        "Các sản phẩm tiêu chuẩn của nhà chế tạo thường phù hợp với giới hạn áp suất của vật liệu chế "
        "tạo đường ống — với hệ ống nhựa là giới hạn của nhựa, còn với ống thép hoặc đồng thau thì "
        "thường tới 2,7 MPa. Áp suất cao hơn có sẵn nhưng thường đắt hơn một chút. Độ sụt áp do lưu "
        "lượng kế đã lắp thường thấp; nhà chế tạo thường cung cấp được thông tin về độ sụt áp dự "
        "kiến."))
    b.append(h4("Hiệu chuẩn", "Calibration"))
    b.append(p(
        "Việc hiệu chuẩn cảm biến thường do nhà chế tạo quy định. Một số nhà chế tạo cung cấp hệ số "
        "hiệu chuẩn theo gallon trên xung hoặc xung trên gallon. Những hãng khác, như Data "
        "Industrial, cung cấp số liệu liên hệ tần số với lưu lượng theo GPM hoặc đơn vị lưu lượng "
        "thể tích khác. Với cảm biến kiểu chèn, bất kỳ thiết bị nào như vậy cũng phải hiệu chuẩn được "
        "tại hiện trường để thích ứng với sự thay đổi quan hệ giữa vận tốc quay của cánh guồng và lưu "
        "lượng trung bình khi cỡ ống thay đổi."))
    b.append(h4("Độ chính xác", "Accuracy"))
    b.append(p(
        "Độ chính xác của lưu lượng kế cánh guồng nối tiếp thay đổi đáng kể nhưng có thể cao, từ "
        "±0,2 % giá trị đọc với chất lỏng ở một nhà chế tạo, tới vài phần trăm toàn thang ở một số "
        "hãng khác. Cần đặc biệt lưu ý sự khác nhau giữa độ chính xác đặc tả theo % toàn thang và "
        "theo % giá trị đọc. Các nhà chế tạo dùng cả hai cách, đặc biệt với loại lưu lượng kế này. "
        "Một thiết bị ±1 % toàn thang thường kém chính xác hơn nhiều so với, chẳng hạn, một thiết bị "
        "±2 % giá trị đọc: ở lưu lượng nhỏ nhất của dải đo với tỷ số giảm 10:1, thiết bị thứ nhất "
        "mắc sai số 10 %, trong khi thiết bị ±2 % giá trị đọc vẫn chỉ mắc sai số ±2 %."))
    b.append(p(
        "Độ chính xác của đầu ra thường được đặc tả là ±1 % lưu lượng danh định lớn nhất. Đặc tả này "
        "đủ rộng để bao trùm những biến thiên về kích thước và ma sát của cảm biến khi chế tạo. Một "
        "số nhà sản xuất hiệu chuẩn riêng cho từng cảm biến để đáp ứng yêu cầu đặc biệt, nhưng chỉ "
        "nên làm vậy khi có thể gửi được cả đoạn ống vào và ra lắp với cảm biến tới nhà chế tạo và "
        "nhà chế tạo nhận lắp được. Ngoài ra, nhà chế tạo thường có thể cung cấp giá trị hiệu chuẩn "
        "mới nếu biết mã hiệu bộ hiển thị đang dùng, biết số đọc của nó và biết lưu lượng thực tại ít "
        "nhất hai điểm trên đường cong lưu lượng. Khi buộc phải hiệu chuẩn tại chỗ, độ chính xác dự "
        "kiến nằm trong khoảng ±0,5 % toàn thang hoặc 1 % lưu lượng chỉ thị, lấy giá trị nào lớn hơn."))
    b.append(p(
        "Độ lặp lại của số đọc thường vào cỡ 0,5 %. Độ tuyến tính, trừ ở hai đầu mút của dải lưu "
        "lượng, cũng được kỳ vọng không kém hơn 0,5 %, và trên toàn dải thiết kế của lưu lượng kế "
        "thường chính xác trong phạm vi ±1 % lưu lượng danh định lớn nhất."))
    b.append(p(
        "Để đạt được những độ chính xác nêu trên, phải hết sức chú ý lắp đặt đúng, đặc biệt là độ "
        "sâu chèn."))
    b.append(h4("Đặc điểm kết cấu", "Design features"))
    b.append(p(
        "Những cảm biến lưu lượng này được cung cấp với vật liệu chế tạo tương thích với một loạt "
        "rộng các dung dịch nước, cả pH cao lẫn pH thấp, và với nước khử ion. Với dịch vụ nước khử "
        "ion, cần xem lại lịch sử của cảm biến, đặc biệt về khả năng sinh hạt. Những dòng có nồng độ "
        "chất rắn cao, đặc biệt là chất rắn dạng sợi, cần được xem xét cẩn thận khi cân nhắc dùng "
        "cảm biến cánh guồng. Kết cấu khá dễ dung nạp với hạt rắn, nhưng vẫn cần thận trọng trong "
        "những ứng dụng như vậy. Chất lưu truyền nhiệt cũng tương thích với cảm biến của ít nhất hai "
        "nhà cung cấp. Cần thảo luận các giới hạn ứng dụng cơ bản với nhà cung cấp, vì họ phải có "
        "lịch sử ứng dụng thành công rộng để hậu thuẫn cho khuyến nghị của mình, cũng như có vật liệu "
        "cảm biến với kết quả thử nghiệm riêng cho chất lưu được đo. Có các phiên bản “khoan nóng” "
        "hay “khoan ướt” để lắp vào đường ống đang vận hành và cho dịch vụ nối tiếp hoặc trực tuyến. "
        "Một số nhà cung cấp có phiên bản chịu ngập, đo được trong hố bơm ngập nước trong thời gian "
        "dài. Ít nhất hai nhà chế tạo cung cấp cảm biến “an toàn tia lửa” cho môi trường nguy hiểm "
        "cháy nổ."))
    b.append(h4("Lĩnh vực ứng dụng", "Areas of application"))
    b.append(p(
        "Cảm biến lưu lượng cánh guồng được dùng rộng rãi và khá thành công trong các lĩnh vực sau:"))
    b.append(ul([
        "Tưới tiêu nông nghiệp và trồng trọt",
        "Hệ thống nước khử ion, kể cả chế tạo wafer silic",
        "Sưởi, thông gió và điều hoà không khí, quản lý năng lượng",
        "Xử lý chất thải công nghiệp",
        "Hệ thống lọc công nghiệp",
        "Định lượng và pha chế hoá chất",
        "Hệ thống nước cấp đô thị (nước uống được)",
    ]))
    b.append(p(
        "Cảm biến có thể được cung cấp với đầu ra tương tự cho các ứng dụng điều khiển, nếu muốn."))
    b.append(p(
        "Một số nhà cung cấp đã phát triển những lưu lượng kế cánh guồng chuyên dụng, được điều chỉnh "
        "để có tuổi thọ dài, độ chắc chắn và khả năng bảo trì mà những ứng dụng khắt khe hơn đòi hỏi. "
        "Cần xem lại với nhà cung cấp lịch sử làm việc được chấp nhận trong những ứng dụng tương tự "
        "với ứng dụng đang dự kiến cho hệ đo. Các ứng dụng chuyển giao thương mại thường không phù "
        "hợp với cảm biến cánh guồng."))

    # ---------------------------------------------------------------- makers
    b.append(h3("Nhà chế tạo", "Manufacturers"))
    b.append(p(
        "Dưới đây là một số nhà chế tạo tại Hoa Kỳ. Địa chỉ và số điện thoại của họ được liệt kê "
        "trong Bảng 28.10."))
    b.append(_t2810("vi"))
    b.append(h4("Data Industrial"))
    b.append(p(
        "Lưu lượng kế nối tiếp và kiểu chèn: vận tốc chất lưu 0,07 đến 18 m/s (0,25 đến 60 ft/s). Vật "
        "liệu sẵn có đáp ứng hầu hết chất lưu công nghiệp. Nhiệt độ từ −29 °C đến 152 °C (−20 °F đến "
        "305 °F). Theo dõi năng lượng. Đầu ra dạng số và/hoặc tương tự. Kết cấu NEMA 4, 4X và 6P. "
        "Chứng nhận FM, CSA."))
    b.append(h4("G. Fischer (Signet)"))
    b.append(p(
        "Lưu lượng kế nối tiếp và kiểu chèn: vận tốc chất lưu 0,1 đến 7 m/s (0,3 đến 20 ft/s). Vật "
        "liệu sẵn có đáp ứng hầu hết chất lưu công nghiệp. Nhiệt độ tới 149 °C (300 °F). Theo dõi "
        "năng lượng. Đầu ra dạng số và/hoặc tương tự. Kết cấu NEMA 4, 4X. Chứng nhận FM, CE."))
    b.append(h4("SeaMetrics"))
    b.append(p(
        "Loại nối tiếp: cỡ 3/8 in. đến 2 in.; nhựa, đồng thau; ứng dụng nước sạch; lưu lượng 0,05 đến "
        "40,0 gpm; độ chính xác ±1 % toàn thang (FS). Loại chèn: dải đầu đo IP; nhựa, đồng thau, thép "
        "không gỉ; ổ trục sapphire và trục cacbua; tới 250 °F; 0,3 đến 30 ft/s; độ chính xác ±1 % đến "
        "±2 % FS."))
    b.append(h4("Roper Flow Technology"))
    b.append(p(
        "Lưu lượng kế nối tiếp: OmniFlow®, chất lỏng và chất khí, độ chính xác cao; dải 7,6 đến 5677 "
        "mL/phút (chất lỏng), 0,0025 đến 0,68 A m³/h (chất khí). Chịu lạnh sâu tới 593 °C, áp suất tới "
        "60.000 psi, có bù độ nhớt. Optiflo®, kết cấu nhựa, chỉ cho chất lỏng, với khả năng làm việc "
        "giảm đi đôi chút."))
    b.append(h4("Hoffer"))
    b.append(p(
        "Dòng MF (Miniflow): lưu lượng kế nối tiếp lưu lượng thấp, hiệu năng cao, dùng “rôto Pelton” "
        "cho chất lỏng và chất khí. Dải lưu lượng chất lỏng từ 57 mL/phút đến 11,5 rpm [nguyên văn]. "
        "Độ tuyến tính ±1 % giá trị đọc trên dải 10:1. Độ lặp lại điển hình ±0,1 %. Dải lưu lượng khí "
        "tuỳ khối lượng riêng, từ 0,02 ACFM đến 1,0 ACFM; độ tuyến tính ±1,5 % giá trị đọc; độ lặp "
        "lại ±0,2 %. Nhiều loại ổ trục khác nhau; ổ bi dùng cho ứng dụng đòi hỏi độ chính xác cao. Có "
        "đường cong UVC. Có bộ truyền “thông minh” để bù nhiệt – độ nhớt và tuyến tính hoá."))
    b.append(h4("McMillan"))
    b.append(p(
        "Chất lỏng độ nhớt thấp: lưu lượng kế nối tiếp, dải 13 mL/phút đến 10 L/phút, độ chính xác "
        "±1 % đến ±3 % toàn thang, cảm biến tốc độ quay hồng ngoại. Có phiên bản Teflon cho chất ăn "
        "mòn."))
    b.append(p(
        "Chất khí: phiên bản Teflon cho clo, flo, v.v., độ chính xác ±3 % toàn thang, dải 25 A mL/phút "
        "đến 5 A mL/phút."))
    b.append(h4("Flowmetrics"))
    b.append(p(
        "Series 600: tuabin tiếp tuyến nối tiếp bằng thép không gỉ cho chất khí và chất lỏng. Dải: "
        "0,001 đến 2,0 GPM với chất lỏng; 0,001 đến 2,0 ACFM với chất khí. Độ tuyến tính thay đổi "
        "theo dải, từ ±1 % FS đến ±5 % FS. Độ lặp lại ±0,05 %, truy xuất chuẩn NIST."))
    b.append(h4("Proteus"))
    b.append(p(
        "Lưu lượng kế bánh guồng nối tiếp và công tắc dòng — chỉ cho chất lỏng. Thường dùng cho đường "
        "nước làm mát của thiết bị điện hoặc thiết bị chân không. Được công bố dùng với chất lỏng tới "
        "120 cSt. Môi chất gồm nước, nước đã xử lý, nước khử ion, ethylene glycol, dầu nhẹ, v.v. Dải "
        "0,08 đến 60 gpm. Độ chính xác thay đổi giữa các model trong khoảng ±3 % đến ±4 % FS. Thân "
        "đồng hồ có thể tích hợp thêm đầu đo nhiệt độ và áp suất. Những lưu lượng kế này còn có sẵn "
        "giao thức ghép nối máy tính Fluid Talk™ cùng phần mềm PC để xây dựng hệ điều khiển nhúng cho "
        "lưu lượng, nhiệt độ và áp suất."))

    # ---------------------------------------------------------------- refs
    b.append(h3("Tài liệu tham khảo", "References"))
    b.append(wl([
        "[1] N. P. Cheremisinoff, <i>Applied Fluid Flow Measurement</i>, New York: Marcel Dekker, "
        "1979, 106.",
        "[2] H. S. Bean (chủ biên), <i>Fluid Meters</i>, ấn bản 6, New York: American Society of "
        "Mechanical Engineers, 1971, 99.",
        "[3] <i>Flow Meter Finder™ Impeller-Type Flow Meters</i>, "
        "http://www.seametrics.com/flowmeter-finder/impeller.htm.",
        "[4] R. Koch và D. Palmer, <i>Revisiting Measurement Technologies, Multijet vs. Positive "
        "Displacement Meters in 1996</i>, "
        "http://www.wateronline.com/companies/mastermeterinc/tech.html.",
        "[5] L. C. Kjelstrom, “Methods of measuring pumpage through closed conduit irrigation "
        "systems”, <i>J. Irrigation Drainage Eng.-ASCE</i>, 117, 748–757, 1991.",
    ]))
    return "".join(b)


def sec_28_5_en():
    b = []
    b.append(h2("28.5 Impeller Flowmeters", "Impeller Flowmeters"))
    b.append(p("Harold M. Miller — Data Industrial."))
    b.append(p(
        "Impeller flowmeters, sometimes called paddlewheel meters, are one of the most commonly used "
        "flowmeter varieties. The impeller flow sensor is a direct offshoot of the old-fashioned "
        "undershot waterwheel. They are a cost-effective alternative to turbine meters, and can be "
        "used in applications that are difficult to handle with other types of flow metering "
        "instruments. In their mechanical construction they are usually very simple, with any "
        "sophistication residing in the electronics used to detect the rotation rate of the impeller, "
        "and in the choice of materials of construction for the chemical corrosion attributes of the "
        "metered fluids. They are related to turbine meters in that both types use a rotating "
        "mechanical element to produce the output signal. They differ in that the impeller meter has "
        "its rotary axis transverse to the flow stream, as opposed to the turbine meter axis, which "
        "is parallel thereto."))
    b.append(p(
        "These devices are available in two basic types. The insertion style is the most common (see "
        "Figures 28.34(b) and 28.35). The sensor is installed directly into a hole in a pipe, with a "
        "saddle or welded fitting installed at the entry to seal the sensor to the pipe. The sensor "
        "can also be preinstalled in appropriate tees in the pipeline. Most suppliers have designs "
        "that can be installed in operating pipe systems, with little, if any, loss of fluid during "
        "the installation process. The impeller design is also supplied in in-line (through-flow) "
        "sensors for those applications where such use is desirable (Figure 28.34(a)). The in-line "
        "meters are commonly of somewhat higher accuracy than the insertion style."))
    b.append(fig(34, F.fig(34), "en"))
    b.append(p(
        "In-line meters are linear, inferential, volumetric flowmeters for measuring liquid and gas "
        "flows, and are more sensitive at lower flow rates compared with, for example, axial turbine "
        "flowmeters. (This is of course because the flow blade incidence angle is much greater.) "
        "Insertion impeller flowmeters instead measure the flow velocity in a small region within a "
        "flow conduit."))
    b.append(p(
        "Impeller flowmeters are generally suited to much lower flow rate ranges than the same size "
        "axial turbines, and hence often find applications where axial turbines cannot be used. This, "
        "and a tendency for lower cost and high reliability, are key strengths. Competition with "
        "in-line axial turbines can only occur in overlapping design flow ranges."))
    b.append(p(
        "Some in-line meters have interchangeable orifice sizes, allowing the same body to be used "
        "over different flow ranges. The orificed in-line meters are typically insensitive to flow "
        "condition. Insertion meters are, of course, very sensitive to flow condition if volumetric "
        "measurements are inferred. This is an important distinction and can extend to differences "
        "between requirements for specific in-line versions. Installation is important: it affects "
        "the user when designing an installation, selecting a flowmeter, and deciding how much "
        "confidence to place in the measurement reading."))
    b.append(fig(35, F.fig(35), "en"))
    b.append(p(
        "Paddlewheel flowmeters are never used in liquid hydrocarbon custody transfer applications. "
        "The flow measurement capacity is insufficient to compete in monitoring large-volume "
        "transfers, and accuracy is not sufficient for valuable fluids."))
    b.append(p(
        "These meters go by a variety of names, depending on which name the manufacturer selects and "
        "also the application. One often-quoted historical root is the impulse turbine invented by "
        "Pelton in the 19th century, which has given rise to the “Pelton wheel turbine” description "
        "currently used by some suppliers. A device like this was originally used to drive milling "
        "wheels directly about the vertical axis, rather than through a right-angle gear as in the "
        "“undershot” wheel described. Another common name, besides paddlewheel and impeller-type — "
        "based at least on suppliers' descriptions for the in-line variety — is single-jet "
        "tangential, or simply tangential, turbine. The former description distinguishes this design "
        "from that of multijet tangential turbine flowmeters and therefore deserves mention. There "
        "are thus a confusing variety of names in current use, all relating to essentially the same "
        "impeller-like, vaned flowmetering principle:"))
    b.append(ol([
        "Impeller type: insertion and in-line",
        "Paddlewheel type: insertion and in-line",
        "Pelton turbine wheel type: in-line",
        "Tangential turbine flowmeter: insertion and in-line",
        "Single-jet tangential turbine flowmeter: in-line",
        "Impulse turbine flowmeter: in-line",
    ]))
    b.append(p(
        "Historically, the impeller sensor is based on early electronic speedometers used in pleasure "
        "boating. Signet, followed quickly by Data Industrial, moved to modify the basic design of "
        "such marine instruments to meet the significantly more demanding service life requirements "
        "of industrial flow measurement. The resulting flowmeters, and their descendants, have been "
        "widely used since 1975. Significant engineering efforts have resulted in highly reliable "
        "instruments used in many extremely demanding applications."))

    # ---------------------------------------------------------------- sensing
    b.append(h3("Sensing Principles", "Sensing Principles"))
    b.append(p(
        "All impeller flow sensors must detect the rotation of the impeller, and in their usual form "
        "transmit a pulse train at a frequency related to the rotational velocity of the impeller. "
        "Being essentially a digital output, impeller sensors can typically transmit signals over "
        "quite long distances, up to 1 km when so required. Detection principles used include:"))
    b.append(ol([
        "One or more magnets retained in the impeller or mechanically connected thereto, using the "
        "zero crossing of an induced ac field to generate the pulse train.",
        "One or more coupling devices contained within the impeller, modulating a transmitted "
        "frequency that is processed to produce the pulse train.",
        "One or more metallic targets installed within the sensor, sensed by any of the proximity "
        "pickup techniques commercially available, to produce output pulses.",
        "One or more magnets retained in the impeller, used to switch a Hall effect device, producing "
        "the output pulse train.",
        "Optical devices, both transmissive and reflective, used to sense the passage of the impeller "
        "blades to produce the output pulse train.",
        "Measurement of the change in electric reactance due to the passage of impeller vanes through "
        "the measurement field area, conditioned to produce the output pulse train.",
    ]))
    b.append(p(
        "Any given supplier can produce several types of impeller flowmeter, each type using a "
        "different detection method depending on market requirements. Since the impeller can operate "
        "to rotational velocities of 4000 rpm or higher, output frequencies can be as high as 500 Hz. "
        "At low flow rates the frequencies can be as low as 0.2 Hz. This factor should be addressed "
        "early in the selection procedure, because the chosen output device must be capable of the "
        "frequency output range of the sensor."))
    b.append(p(
        "Most sensor manufacturers can either supply or specify an appropriate meter to relate sensor "
        "output to flow rate in engineering units, either U.S. Customary or SI. These meters are "
        "usually capable of displaying both flow rate and accumulated flow for the sensor to which "
        "they are connected. Additional outputs are available, either stand-alone or in combination "
        "with the meter, providing periodic pulse outputs at definable flow increments or analog "
        "outputs scaled to flow rate. In addition, certain control functions, alarms and other "
        "special features required by the various markets served are often incorporated in these "
        "meters."))

    # ---------------------------------------------------------------- ranges
    b.append(h3("Flow Ranges", "Flow Ranges"))
    b.append(p(
        "The insertion style of impeller meter, even when tee-installed, is a local sensing device, "
        "measuring the flow velocity in only part of the flow stream. The manufacturer calibrates the "
        "meter for average flow across the entire cross-section of the pipe. The paddlewheel location "
        "is usually close to the inner diameter of the pipe, in a region of flow with a velocity "
        "significantly below the average flow velocity in the pipe. Proper calibration practices by "
        "the manufacturer make the meters effective at flow rates as low as 10 cm/s average velocity, "
        "in spite of the low local velocities at the impeller. Generally speaking, flows at Reynolds "
        "numbers as low as 5000 can be run with no requirement for special calibration, and "
        "frequently lower numbers can be handled with no difficulty. The usual range specification is "
        "a flow rate equivalent to 0.3 to 10 m/s average flow velocity. The diversity of products "
        "available allows operation to velocities considerably lower than the 0.3 m/s range, indeed "
        "to as low as 0.07 m/s in certain specialty impeller flowmeters."))

    # ---------------------------------------------------------------- install
    b.append(h3("Installation", "Installation"))
    b.append(h4("Pipe sizes", "Pipe sizes"))
    b.append(p(
        "Pipe sizes in which these sensors have been installed run the gamut from small-bore tubing "
        "to 2.3 m outside diameter. The larger pipe sizes are those that show the greatest installed "
        "cost savings over alternative metering systems. The impeller meter, in fact, can be "
        "cost-effective in any flowmeter application that is consistent with the accuracy of the "
        "instrument, particularly if the application involves pump or valve control."))
    b.append(h4("Piping system restrictions", "Piping system restrictions"))
    b.append(p(
        "Most suppliers require at least 10 pipe-diameter lengths of straight pipe upstream of the "
        "installed meter, and 5 downstream. These conditions are required to minimize the asymmetry "
        "of the flow stream in the neighbourhood of the impeller, in the installed piping, which can "
        "be caused by elbows, tees and valves. More is better; no supplier is likely to complain that "
        "there is too great a straight pipe length upstream. Less can adversely affect the "
        "calibration of the sensor, due to the local variations of velocity resulting from flow "
        "disturbances."))
    b.append(h4("Operating pressure", "Operating pressure"))
    b.append(p(
        "Manufacturers' standard offerings are usually consistent with the pressure limitations of "
        "the materials of construction of the piping system — with plastic piping systems, the "
        "plastic limit; with steel or brass piping, commonly as high as 2.7 MPa. Higher pressures are "
        "available, but are usually somewhat more expensive. Pressure drop generated by the installed "
        "flowmeter is usually low. Manufacturers can usually supply information on the anticipated "
        "pressure drop."))
    b.append(h4("Calibration", "Calibration"))
    b.append(p(
        "Calibration of the sensors is usually specified by the manufacturer. Some manufacturers "
        "provide a calibration factor in terms of gallons per pulse or in pulses per gallon. Others, "
        "such as Data Industrial, provide data relating frequency to flow rate in GPM or other "
        "volumetric rate units. For insertion-style sensors, any such instrument must be field "
        "calibratable to accommodate the variation in the relation of impeller rotational velocity "
        "with average flow rate with pipe size variation."))
    b.append(h4("Accuracy", "Accuracy"))
    b.append(p(
        "Accuracies for in-line impeller flowmeters vary considerably but can be high, ranging from "
        "±0.2% of reading for liquids for one manufacturer to several percent of full scale for "
        "several others. The difference between accuracies specified as % full scale and % reading "
        "should be particularly noted. Manufacturers use both, particularly with this class of "
        "meter. A ±1% full-scale device is often far less accurate than, for example, a ±2% reading "
        "device: it is in error by 10% at the minimum of its flow range if the turndown is 10:1, "
        "whereas the ±2% reading device is still only in error by ±2%."))
    b.append(p(
        "Output accuracy is usually specified as ±1% of full rated flow. This specification is broad "
        "enough to handle the dimensional and frictional variations in the sensors as manufactured. "
        "Some producers will custom-calibrate the sensors to meet special needs, but this task should "
        "be performed only when the mating pipe entry and exit can be shipped to, and accommodated "
        "by, the manufacturer. Alternatively, the manufacturer can usually provide new calibration "
        "values if the meter used is identified, the meter reading is known, and the actual flow is "
        "known for at least two points on the flow curve. When calibration in place is required, the "
        "anticipated accuracy is in the range of ±0.5% of full scale or 1% of indicated flow, "
        "whichever is greater."))
    b.append(p(
        "Repeatability of readings is usually on the order of 0.5%. Linearity, except at the extremes "
        "of the flow range, is also expected to be no worse than 0.5%, and over the full design range "
        "of the meter is normally accurate within ±1% of full rated flow."))
    b.append(p(
        "To achieve the accuracies noted above, careful attention must be paid to proper "
        "installation, particularly with regard to insertion depth."))
    b.append(h4("Design features", "Design features"))
    b.append(p(
        "These flow sensors are offered in materials of construction compatible with a broad range of "
        "aqueous solutions, of both high and low pH, and with deionized water. For this latter "
        "service, the history of the sensor — particularly for particle generation — should be "
        "reviewed. Flow streams with high concentrations of solids, and particularly of fibrous "
        "solids, should be carefully reviewed when the impeller sensor is under consideration. "
        "Construction is reasonably forgiving with particulates, but caution in such applications is "
        "warranted. Heat transfer fluids are also compatible with sensors from at least two of the "
        "suppliers. Basic application limits should be discussed with the supplier, who should have a "
        "broad history of successful applications to back up recommendations, as well as sensor "
        "materials with test results specific to the measured fluid. So-called “hot tap” or “wet tap” "
        "versions are available for installation in operating pipelines and in-line or on-line "
        "service. A submersible version capable of metering in flooded well pits for extended periods "
        "of time is available from some suppliers. At least two manufacturers provide “intrinsically "
        "safe” sensors for application in hazardous environments."))
    b.append(h4("Areas of application", "Areas of application"))
    b.append(p("Impeller flow sensors are widely used in the following fields with considerable success:"))
    b.append(ul([
        "Agricultural and horticultural irrigation",
        "Deionized water systems, including silicon wafer fabrication",
        "Heating, ventilating and air conditioning, energy management",
        "Industrial waste treatment",
        "Industrial filtration systems",
        "Chemical reagent metering and batching",
        "Municipal water systems (potable water)",
    ]))
    b.append(p(
        "The sensors can be supplied with analog output for control applications, if desired."))
    b.append(p(
        "Some suppliers have developed specialty impeller meters adapted to provide the long life, "
        "ruggedness and maintainability required in more demanding applications. The history of "
        "acceptable operation in applications similar to that proposed for the metering system should "
        "be reviewed with the supplier. Custodial transfer applications are normally unsuitable for "
        "the impeller sensor."))

    # ---------------------------------------------------------------- makers
    b.append(h3("Manufacturers", "Manufacturers"))
    b.append(p(
        "The following is a selection of U.S. manufacturers. Their locations and phone numbers are "
        "listed in Table 28.10."))
    b.append(_t2810("en"))
    b.append(h4("Data Industrial"))
    b.append(p(
        "In-line and insertion meters: 0.07 to 18 m/s (0.25 to 60 fps) fluid velocity. Available "
        "materials to accommodate most industrial fluids. Temperatures from −29 °C to 152 °C (−20 °F "
        "to 305 °F). Energy monitoring. Digital and/or analog meter outputs. NEMA 4, 4X and 6P "
        "constructions. FM, CSA approvals."))
    b.append(h4("G. Fischer (Signet)"))
    b.append(p(
        "In-line and insertion meters: 0.1 to 7 m/s (0.3 to 20 fps) fluid velocity. Available "
        "materials to accommodate most industrial fluids. Temperatures to 149 °C (300 °F). Energy "
        "monitoring. Digital and/or analog meter outputs. NEMA 4, 4X constructions. FM, CE approvals."))
    b.append(h4("SeaMetrics"))
    b.append(p(
        "In-line meter: sizes 3/8 in. to 2 in.; plastic, brass; clean water applications; flows from "
        "0.05 to 40.0 gpm; accuracy ±1% of full scale (FS). Insertion: range of IP probes; plastic, "
        "brass, stainless; sapphire bearings and carbide shafts; up to 250 °F; 0.3 to 30 fps; "
        "accuracy ±1% to ±2% FS."))
    b.append(h4("Roper Flow Technology"))
    b.append(p(
        "In-line meters: OmniFlow®, liquids and gases, highly precise, range 7.6 to 5677 mL/min "
        "(liquid), 0.0025 to 0.68 A m³/h (gases). Cryogenics to 593 °C, pressure to 60,000 psi, "
        "viscosity compensated. Optiflo®, plastic construction for liquids only, with some reduction "
        "in performance capabilities."))
    b.append(h4("Hoffer"))
    b.append(p(
        "MF Series (Miniflow): high-performance, in-line low-flow meters using a “Pelton rotor” for "
        "liquids and gases. Liquid flow ranges from 57 mL/min to 11.5 rpm [sic]. Linearity ±1% "
        "reading over 10:1 range. Repeatability ±0.1% typical. Gas flow ranges depending on density "
        "from 0.02 ACFM to 1.0 ACFM; linearity ±1.5% reading; repeatability ±0.2%. Various bearings "
        "available; ball bearings used for high-accuracy applications. UVC curves available. “Smart” "
        "transmitter available for temperature–viscosity correction plus linearization."))
    b.append(h4("McMillan"))
    b.append(p(
        "Low-viscosity liquids: in-line meters, ranges from 13 mL/min to 10 L/min, accuracies ±1% to "
        "±3% full scale, IR rotation sensors. Have a Teflon version for corrosives."))
    b.append(p(
        "Gases: Teflon version for chlorine, fluorine, etc., accuracy ±3% full scale, ranges 25 A "
        "mL/min to 5 A mL/min."))
    b.append(h4("Flowmetrics"))
    b.append(p(
        "Series 600: stainless steel, in-line tangential turbine for gases and liquids. Ranges: 0.001 "
        "to 2.0 GPM liquids; 0.001 to 2.0 ACFM gases. Linearities vary according to range from ±1% FS "
        "to ±5% FS. Repeatabilities ±0.05%, traceable NIST."))
    b.append(h4("Proteus"))
    b.append(p(
        "In-line paddlewheel flowmeters and flow switches — liquids only. Typically used for water "
        "cooling lines on electrical or vacuum equipment. Quoted for use with liquids up to 120 cSt. "
        "Media include water, treated water, deionized water, ethylene glycol, light oils, etc. Range "
        "0.08 to 60 gpm. Accuracies vary between models in the ±3% to ±4% FS range. Meter bodies can "
        "incorporate optional integral temperature and pressure transducers. These meters are also "
        "available with a Fluid Talk™ computer interface protocol and PC software for constructing "
        "embedded control systems for flow, temperature and pressure."))

    # ---------------------------------------------------------------- refs
    b.append(h3("References", "References"))
    b.append(wl([
        "[1] N. P. Cheremisinoff, <i>Applied Fluid Flow Measurement</i>, New York: Marcel Dekker, "
        "1979, 106.",
        "[2] H. S. Bean (ed.), <i>Fluid Meters</i>, 6th ed., New York: American Society of Mechanical "
        "Engineers, 1971, 99.",
        "[3] <i>Flow Meter Finder™ Impeller-Type Flow Meters</i>, "
        "http://www.seametrics.com/flowmeter-finder/impeller.htm.",
        "[4] R. Koch and D. Palmer, <i>Revisiting Measurement Technologies, Multijet vs. Positive "
        "Displacement Meters in 1996</i>, "
        "http://www.wateronline.com/companies/mastermeterinc/tech.html.",
        "[5] L. C. Kjelstrom, “Methods of measuring pumpage through closed conduit irrigation "
        "systems”, <i>J. Irrigation Drainage Eng.-ASCE</i>, 117, 748–757, 1991.",
    ]))
    return "".join(b)


def _t2811(lang):
    """Table 28.11 — manufacturers of electromagnetic flowmeters."""
    if lang == "vi":
        hd = ("Nhà chế tạo", "Địa chỉ", "Điện thoại / Fax")
        cap = ("Bảng 28.11 · Danh sách một số nhà chế tạo lưu lượng kế điện từ. Địa chỉ và số điện "
               "thoại in lại đúng như bản gốc năm 1999.")
    else:
        hd = ("Manufacturer", "Address", "Phone / Fax")
        cap = ("Table 28.11 · A list of several manufacturers of electromagnetic flowmeters. "
               "Addresses and telephone numbers are reproduced as printed in the 1999 original.")
    rows = [
        ["ABB K-Flow Inc.", "P.O. Box 849, 45 Reese Rd., Millville, NJ 08332",
         "Tel: (800) 294-8116<br>Fax: (609) 825-1678"],
        ["Control Warehouse", "Shores Industrial Park, Ocala, FL 34472",
         "Tel: (800) 633-0319<br>Fax: (352) 687-8925"],
        ["Davis Instruments", "4701 Mount Hope Dr., Baltimore, MD 21215",
         "Tel: (410) 358-3900<br>Fax: (410) 358-0252"],
        ["Fischer Porter", "50 Northwestern Dr., P.O. Box 1167T, Salem, NH 03079-1137",
         "Tel: (603) 893-9181<br>Fax: (603) 893-7690"],
        ["Johnson Yokogawa", "Dept. P, Dart Rd., Newman, GA 30265",
         "Tel: (800) 394-9134<br>Fax: (770) 251-6427"],
        ["Marsh-McBirney, Inc.", "4539 Metropolitan Court, Frederick, MD 21704",
         "Tel: (301) 879-5599<br>Fax: (301) 874-2172"],
        ["Nusonics Inc.", "11391 E. Tecumseh St., Tulsa, OK 74116-1606",
         "Tel: (918) 438-1010<br>Fax: (918) 438-6420"],
        ["Rosemount Inc.", "Dept. MCA 15, 12001 Technology Dr., Eden Prairie, MN 55344",
         "Tel: (612) 828-3006<br>Fax: (612) 828-3088"],
        ["Sparling Instruments Co., Inc.", "4097 Temple City Blvd., P.O. Box 5988, "
         "El Monte, CA 91734-1988", "Tel: (800) 423-4539"],
        ["Universal Flow Monitors, Inc.", "1751 E. Nine Mile Rd., Hazel Park, MI 48030",
         "Tel: (313) 542-9635<br>Fax: (313) 398-4274"],
    ]
    return table(hd, rows, cap, widths=("26%", "44%", "30%"))


def sec_28_6_vi():
    b = []
    b.append(h2("28.6 Lưu lượng kế điện từ", "Electromagnetic Flowmeters"))
    b.append(p("Halit Eren."))
    b.append(p(
        "Lưu lượng kế từ đã được dùng rộng rãi trong công nghiệp từ nhiều năm nay. Khác với nhiều "
        "loại lưu lượng kế khác, chúng cho phép đo thực sự không xâm nhập. Chúng dễ lắp đặt và dễ sử "
        "dụng đến mức những đường ống đang tồn tại trong một quy trình có thể biến thành lưu lượng kế "
        "chỉ bằng cách thêm các điện cực bên ngoài và nam châm phù hợp. Chúng đo được dòng chảy ngược "
        "và không nhạy với độ nhớt, khối lượng riêng và nhiễu loạn dòng. Lưu lượng kế điện từ đáp ứng "
        "nhanh với thay đổi lưu lượng và là thiết bị tuyến tính trên một dải đo rộng. Những năm gần "
        "đây, các cải tiến công nghệ đã cho ra những thiết bị kinh tế hơn, chính xác hơn và nhỏ gọn "
        "hơn nhiều so với các phiên bản trước."))
    b.append(p(
        "Như với nhiều thiết bị điện khác, nguyên lý nền tảng của lưu lượng kế điện từ là định luật "
        "cảm ứng điện từ Faraday. Điện áp cảm ứng trong lưu lượng kế điện từ tỷ lệ tuyến tính với vận "
        "tốc trung bình của chất lỏng, hoặc với lưu lượng thể tích. Như trong nhiều ứng dụng, nếu "
        "thành ống làm bằng vật liệu không dẫn điện thì điện áp cảm ứng không phụ thuộc vào tính chất "
        "của chất lưu."))
    b.append(p(
        "Độ chính xác của những thiết bị này có thể tốt tới 0,25 %, và trong phần lớn ứng dụng người "
        "ta dùng độ chính xác 1 %. Trong trường hợp xấu nhất, một số ứng dụng khó chỉ đạt 5 %, khi "
        "chất lỏng có tạp chất và điện trở tiếp xúc của điện cực kém, như với các dung dịch natri có "
        "độ tinh khiết thấp."))

    # ---------------------------------------------------------------- faraday
    b.append(h3("Định luật cảm ứng Faraday", "Faraday's Law of Induction"))
    b.append(p(
        "Định luật này phát biểu rằng nếu một vật dẫn có chiều dài <i>l</i> (m) chuyển động với vận "
        "tốc <i>v</i> (m s<sup>−1</sup>) vuông góc với một từ trường có mật độ từ thông <i>B</i> "
        "(Tesla), thì điện áp cảm ứng <i>e</i> trên hai đầu vật dẫn được biểu diễn bằng:"))
    b.append(eq("e = B l v", "28.57"))
    b.append(p(
        "Nguyên lý áp dụng định luật Faraday cho lưu lượng kế điện từ được trình bày ở Hình 28.36. Từ "
        "trường, chiều chuyển động của vật dẫn và suất điện động cảm ứng đôi một vuông góc với nhau."))
    b.append(fig(36, F.fig(36), "vi"))
    b.append(p(
        "Hình 28.37 minh hoạ chi tiết hơn một lưu lượng kế điện từ giản lược. Các nam châm điện đặt "
        "bên ngoài tạo ra một từ trường đều xuyên qua ống và chất lỏng bên trong. Khi chất lỏng dẫn "
        "điện đang chảy cắt qua từ trường, một điện áp được sinh ra dọc theo đường đi của chất lỏng, "
        "giữa hai điện cực đặt ở hai phía đối diện của ống."))
    b.append(p(
        "Với lưu lượng kế điện từ, vật dẫn chính là chất lỏng chảy trong ống, và chiều dài vật dẫn là "
        "khoảng cách giữa hai điện cực, tức bằng đường kính ống. Vận tốc của vật dẫn tỷ lệ với vận "
        "tốc trung bình của chất lỏng. Do đó điện áp cảm ứng trở thành:"))
    b.append(eq("e = B D v", "28.58"))
    b.append(p(
        "trong đó <i>D</i> (m) là đường kính ống. Nếu từ trường không đổi và đường kính ống cố định "
        "thì độ lớn của điện áp cảm ứng chỉ tỷ lệ với vận tốc chất lỏng. Nếu hai đầu vật dẫn — ở đây "
        "là các cảm biến — được nối vào một mạch ngoài thì điện áp cảm ứng sẽ gây ra dòng điện "
        "<i>i</i>, và dòng này có thể được xử lý thích hợp để làm thước đo lưu lượng. Điện trở của "
        "vật dẫn chuyển động ký hiệu là <i>R</i>, cho ta điện áp đầu cực <i>v</i><sub>T</sub> của vật "
        "dẫn chuyển động: <i>v</i><sub>T</sub> = <i>e</i> − <i>iR</i>."))
    b.append(p(
        "Lưu lượng kế điện từ thường được hiệu chuẩn để xác định lưu lượng thể tích của chất lỏng. Lưu "
        "lượng thể tích <i>Q</i> (L s<sup>−1</sup>) liên hệ với vận tốc trung bình của chất lưu theo:"))
    b.append(eq("Q = A v", "28.59"))
    b.append(p("Viết diện tích <i>A</i> (m<sup>2</sup>) của ống dưới dạng:"))
    b.append(eq("A = πD<sup>2</sup> / 4", "28.60"))
    b.append(p("ta được điện áp cảm ứng như một hàm của lưu lượng:"))
    b.append(eq("e = 4BQ / πD", "28.61"))
    b.append(p(
        "Phương trình 28.61 cho thấy rằng ở một lưu lượng kế được thiết kế cẩn thận, nếu mọi tham số "
        "khác giữ không đổi thì điện áp cảm ứng chỉ tỷ lệ tuyến tính với lưu lượng chất lỏng."))
    b.append(p(
        "Dựa trên định luật cảm ứng Faraday, có nhiều loại lưu lượng kế điện từ khác nhau: loại xoay "
        "chiều, loại một chiều và loại dùng nam châm vĩnh cửu. Hai loại dùng phổ biến nhất là xoay "
        "chiều và một chiều; mục này chủ yếu tập trung vào hai loại đó."))
    b.append(p(
        "Mặc dù điện áp cảm ứng tỷ lệ trực tiếp với giá trị trung bình của lưu lượng, khó khăn chính "
        "khi dùng lưu lượng kế điện từ là biên độ điện áp cảm ứng nhỏ so với các điện áp lạ và nhiễu. "
        "Các nguồn nhiễu gồm:"))
    b.append(ul([
        "Điện áp lạ trong chất lỏng công nghệ",
        "Ghép điện dung giữa mạch tín hiệu và mạch nguồn",
        "Ghép điện dung trong dây dẫn nối",
        "Suất điện động điện–cơ cảm ứng trong điện cực và trong chất lưu",
        "Ghép cảm ứng của nam châm bên trong lưu lượng kế",
    ]))

    # ---------------------------------------------------------------- construction
    b.append(h3("Kết cấu và nguyên lý làm việc", "Construction and Operation of Electromagnetic Flowmeters"))
    b.append(p(
        "Điểm chung của cả lưu lượng kế điện từ xoay chiều và một chiều là các cuộn dây tạo ra từ "
        "trường xuyên qua ống và chất lưu. Khi chất lưu dẫn điện chảy qua lưu lượng kế, một điện áp "
        "được cảm ứng giữa các điện cực tiếp xúc với chất lỏng. Các điện cực được đặt ở vị trí có "
        "chênh lệch điện thế lớn nhất. Điện cực được cách điện với thành ống bằng lớp lót không dẫn "
        "điện để tránh làm ngắn mạch tín hiệu điện cực. Lớp lót còn bảo vệ ống khỏi ăn mòn điện ly và "
        "ăn mòn do tiếp xúc kim loại. Điện cực được giữ bởi các bộ giữ, đồng thời làm luôn nhiệm vụ "
        "làm kín."))
    b.append(p(
        "Về kích thước, lưu lượng kế từ được chế tạo với đường kính từ 2 mm đến 1,2 m. Trong một ứng "
        "dụng cụ thể, việc xác định cỡ lưu lượng kế là chọn thiết bị xử lý được vận tốc chất lỏng dự "
        "kiến. Vận tốc dự kiến phải nằm trong dải tuyến tính của thiết bị. Như một ví dụ hướng dẫn "
        "chọn cỡ, khả năng của các cỡ lưu lượng kế khác nhau được cho ở Hình 28.38."))
    b.append(fig(37, F.fig(37), "vi"))
    b.append(p(
        "Một số lưu lượng kế điện từ được làm với ống dòng thay thế được, trong đó cuộn dây đặt hoàn "
        "toàn bên ngoài ống. Ở loại này, hai mặt bích được đặt cách xa nhau để giảm ảnh hưởng xấu của "
        "chúng tới độ chính xác, nên kích thước tổng thể tương đối lớn. Ở loại khác, cuộn dây đặt gần "
        "ống hơn hoặc tích hợp hẳn vào ống; khi đó mặt bích có thể đặt gần nam châm và điện cực hơn, "
        "cho kích thước nhỏ hơn. Còn các lưu lượng kế điện từ kiểu thu nhỏ và kiểu không điện cực thì "
        "nhỏ gọn đến mức khoảng cách mặt bích – mặt bích đủ ngắn để lắp vào giữa hai mặt bích của "
        "đường ống."))
    b.append(fig(38, F.fig(38), "vi"))
    b.append(p(
        "Các bộ phận ướt của lưu lượng kế từ gồm lớp lót, điện cực và bộ giữ điện cực. Nhiều vật liệu "
        "khác nhau như cao su, teflon, polyurethane, polyethylene… được dùng trong chế tạo để phù hợp "
        "với tính ăn mòn, tính mài mòn và giới hạn nhiệt độ của quy trình. Thân lưu lượng kế và điện "
        "cực có thể chế tạo từ thép không gỉ, tantan, titan và nhiều hợp kim khác. Lớp lót được chọn "
        "chủ yếu để chịu được tính mài mòn và ăn mòn của chất lỏng. Điện cực phải được chọn sao cho "
        "không bị phủ lớp cặn cách điện của chất lỏng trong thời gian vận hành dài."))
    b.append(p(
        "Ống nằm giữa các nam châm điện của lưu lượng kế phải làm bằng vật liệu không nhiễm từ để từ "
        "trường xuyên qua chất lưu mà không bị méo. Vì vậy ống dòng thường được chế tạo bằng thép "
        "không gỉ hoặc nhựa. Dùng thép là lựa chọn tốt hơn vì tăng độ bền kết cấu. Mặt bích được bảo "
        "vệ bằng lớp lót thích hợp và không tiếp xúc với chất lưu."))
    b.append(p(
        "Ở một số lưu lượng kế điện từ, điện cực được làm sạch liên tục hoặc định kỳ bằng siêu âm hay "
        "bằng điện. Siêu âm được chỉ định cho cả lưu lượng kế từ xoay chiều và một chiều khi dự kiến "
        "điện cực thường xuyên bị phủ lớp cách điện dày, có thể làm lưu lượng kế ngừng làm việc đúng "
        "như mong đợi."))
    b.append(p(
        "Vận hành của lưu lượng kế từ nói chung bị giới hạn bởi các yếu tố như đặc tính tuyến tính, "
        "cấp áp suất của mặt bích và nhiệt độ của chất lưu. Giới hạn nhiệt độ lớn nhất phụ thuộc "
        "phần lớn vào vật liệu lớp lót và thường được đặt khoảng 200 °C. Chẳng hạn, lớp lót gốm chịu "
        "được nhiệt độ cao nhưng dễ nứt nếu nhiệt độ chất lưu thay đổi đột ngột."))
    b.append(p(
        "Khi chọn lưu lượng kế điện từ, cần đánh giá cẩn thận các ràng buộc về vận tốc để bảo đảm "
        "hiệu năng chính xác trên dải dự kiến. Vận tốc toàn thang của lưu lượng kế điển hình là 0,3 "
        "đến 10 m s<sup>−1</sup>. Một số lưu lượng kế đo được vận tốc thấp hơn với độ chính xác kém "
        "hơn đôi chút. Nói chung, nên cân nhắc kỹ khi dùng lưu lượng kế điện từ ở vận tốc trên "
        "5 m s<sup>−1</sup>, vì ống và lớp lót có thể bị xói mòn đáng kể."))
    b.append(p(
        "Độ chính xác của lưu lượng kế từ thông thường được biểu diễn theo phần trăm toàn thang (FS), "
        "điển hình 0,5 % đến 1 % FS. Tuy nhiên lưu lượng kế một chiều có điểm không xác định rõ nhờ "
        "khả năng tự chỉnh không, nên độ chính xác theo phần trăm giá trị đọc tốt hơn loại xoay "
        "chiều, điển hình 0,5 % đến 2 %."))

    # ---------------------------------------------------------------- types
    b.append(h3("Các loại lưu lượng kế điện từ", "Types of Electromagnetic Flowmeters"))
    b.append(h4("Lưu lượng kế điện từ xoay chiều", "AC magnetic flowmeters"))
    b.append(p(
        "Ở nhiều lưu lượng kế điện từ thương mại, dòng xoay chiều 50 Hz đến 60 Hz chạy trong cuộn dây "
        "tạo ra từ trường kích thích chất lỏng chảy trong ống. Một điện áp được cảm ứng trong chất "
        "lỏng theo định luật cảm ứng Faraday như đã trình bày. Giá trị điển hình của suất điện động "
        "cảm ứng ở một lưu lượng kế xoay chiều lắp trên ống đường kính trong 50 mm, lưu lượng "
        "500 L phút<sup>−1</sup>, vào khoảng 2,5 mV."))
    b.append(p(
        "Trong lịch sử, lưu lượng kế từ xoay chiều là loại được dùng phổ biến nhất vì chúng giảm hiệu "
        "ứng phân cực ở điện cực. Nói chung chúng ít bị ảnh hưởng bởi prôfin dòng chảy trong ống. "
        "Chúng cho phép dùng bộ khuếch đại trở kháng vào cao, độ trôi thấp, cùng bộ lọc thông cao để "
        "loại bỏ các trôi điện áp chậm và giả tạo, chủ yếu sinh ra từ hiệu ứng cặp nhiệt điện và hiệu "
        "ứng điện ly. Những lưu lượng kế này có nhiều ứng dụng đa dạng, tới mức đo lưu lượng máu "
        "trong cơ thể sống. Cảm biến thu nhỏ cho phép đo trên ống và bình chỉ 2 mm đường kính; ở những "
        "ứng dụng này tần số kích thích cao hơn loại công nghiệp, từ 200 Hz đến 1000 Hz."))
    b.append(p(
        "Nhược điểm chính của lưu lượng kế xoay chiều là từ trường xoay chiều mạnh cảm ứng các tín "
        "hiệu xoay chiều giả trong mạch đo. Điều này buộc phải chỉnh điểm không của đầu ra một cách "
        "định kỳ ở điều kiện lưu lượng bằng không — thường xuyên hơn so với loại một chiều. Ngoài ra, "
        "trong một số ứng dụng công nghiệp khắc nghiệt, dòng trong từ trường có thể thay đổi do điện "
        "áp và tần số lưới biến động. Ảnh hưởng của biến động từ trường có thể được giảm thiểu bằng "
        "một điện áp chuẩn tỷ lệ với cường độ từ trường để bù các thay đổi đó. Để tránh ảnh hưởng của "
        "nhiễu và biến động, phải dùng cách đi dây và cách hiệu chuẩn đặc biệt theo khuyến nghị của "
        "nhà chế tạo. Thường phải dùng hai ống dẫn riêng — một cho tín hiệu và một cho nguồn. Chiều "
        "dài cáp cũng phải đặt ở một mức nhất định để giảm thiểu vấn đề nhiễu và độ nhạy."))
    b.append(p(
        "Lưu lượng kế xoay chiều làm việc ở 50, 60 hoặc 400 Hz đều sẵn có. Nói chung lưu lượng kế xoay "
        "chiều làm việc được từ 10 Hz đến 5000 Hz. Tần số cao được ưa dùng khi cần xác định hành vi "
        "tức thời của quá độ và dòng nhấp nháy. Tuy vậy, ở những ứng dụng dùng chất lưu dẫn điện rất "
        "tốt và kim loại lỏng, tần số phải giữ thấp để tránh hiệu ứng bề mặt. Ngược lại, nếu chất lưu "
        "dẫn điện kém thì tần số không được cao đến mức quá trình giãn điện môi không còn tức thời."))
    b.append(h4("Lưu lượng kế điện từ một chiều", "DC magnetic flowmeters"))
    b.append(p(
        "Khác với lưu lượng kế từ xoay chiều, lưu lượng kế từ một chiều hay xung kích thích chất lỏng "
        "bằng từ trường làm việc ở 3 Hz đến 8 Hz. Khi bật dòng điện vào nam châm, một điện áp một "
        "chiều được cảm ứng ở các điện cực. Tín hiệu quan sát tại điện cực là tổng của điện áp cảm "
        "ứng và nhiễu, như ở Hình 28.39. Khi ngắt dòng trong cuộn dây, tín hiệu chỉ còn là nhiễu. Lấy "
        "số đo khi không có dòng qua nam châm trừ đi số đo khi có dòng sẽ khử được ảnh hưởng của "
        "nhiễu."))
    b.append(fig(39, F.fig(39), "vi"))
    b.append(p(
        "Nếu cuộn dây được nuôi bằng dòng một chiều thông thường thì có thể xảy ra một số vấn đề: "
        "phân cực — tức sự hình thành một lớp khí quanh điện cực đo — cùng các hiệu ứng điện hoá và "
        "điện–cơ. Một số vấn đề này có thể khắc phục bằng cách kích thích cuộn dây ở tần số cao hơn "
        "hoặc bằng xoay chiều. Tuy nhiên tần số cao và xoay chiều lại sinh ra hiệu ứng biến áp trong "
        "dây tín hiệu và trong đường đi của chất lưu. Vì vậy cuộn dây được kích bằng xung một chiều "
        "với tần số lặp thấp để loại bỏ hiệu ứng biến áp. Ở một số lưu lượng kế, nhờ kỹ thuật lấy mẫu "
        "và xử lý tín hiệu số thích hợp, sai số điểm không và nhiễu được loại bỏ đáng kể."))
    b.append(p(
        "Khả năng bù không cố hữu của lưu lượng kế từ một chiều loại bỏ nhu cầu chỉnh điểm không. Điều "
        "này cho phép tách tín hiệu lưu lượng bất kể sự dịch điểm không do nhiễu giả tạo hay do phủ "
        "cặn điện cực. Khác với lưu lượng kế xoay chiều, ở đây chịu được lớp phủ cách điện dày hơn, "
        "có thể làm thay đổi độ dẫn điện hiệu dụng đáng kể mà không ảnh hưởng tới hiệu năng. Chừng "
        "nào độ dẫn điện hiệu dụng còn đủ cao thì lưu lượng kế một chiều vẫn làm việc tốt. Vì thế "
        "lưu lượng kế một chiều ít bị ảnh hưởng bởi trôi, bởi lớp phủ điện cực và bởi thay đổi điều "
        "kiện công nghệ hơn so với lưu lượng kế xoay chiều thông thường."))
    b.append(p(
        "Lưu lượng kế từ một chiều không có thời gian đáp ứng tốt do bản chất xung chậm. Tuy nhiên, "
        "chừng nào prôfin dòng không thay đổi nhanh thì thời gian đáp ứng từ không đến toàn thang cỡ "
        "vài giây không gây vấn đề gì trong phần lớn ứng dụng. Yêu cầu về nguồn cũng nhỏ hơn nhiều vì "
        "nam châm chỉ được cấp điện một phần thời gian, cho lợi ích tiết kiệm điện tới 75 %."))
    b.append(p(
        "Nếu dòng một chiều vào nam châm không đổi thì từ trường tỷ lệ theo cũng giữ được ổn định, do "
        "đó biên độ điện áp một chiều sinh ra ở điện cực sẽ tỷ lệ tuyến tính với lưu lượng. Nhưng "
        "trong thực tế dòng vào nam châm thay đổi chút ít do điện áp và tần số lưới biến động. Như "
        "với lưu lượng kế xoay chiều, biến động điện áp và tần số có thể buộc phải dùng một điện áp "
        "chuẩn. Vì ảnh hưởng của nhiễu dễ loại bỏ hơn nên yêu cầu về cáp không ngặt nghèo bằng."))
    b.append(p(
        "Để tránh phân cực điện ly ở điện cực, người ta đã thiết kế lưu lượng kế một chiều xung lưỡng "
        "cực. Việc cải tiến lưu lượng kế một chiều cũng dẫn tới sự ra đời của lưu lượng kế từ một "
        "chiều thu nhỏ kiểu wafer cho một số ứng dụng hạn chế; kiểu wafer giảm cả khối lượng lẫn yêu "
        "cầu về nguồn."))
    b.append(p("Bảng 28.11 liệt kê một số nhà chế tạo lưu lượng kế điện từ."))
    b.append(_t2811("vi"))

    # ---------------------------------------------------------------- installation
    b.append(h3("Lắp đặt và ứng dụng thực tế", "Installation and Practical Applications"))
    b.append(p(
        "Lưu lượng kế từ xoay chiều và một chiều thông thường có mặt bích ở đầu vào và đầu ra, cần bắt "
        "bu-lông vào mặt bích của đường ống. Khoảng cách mặt bích – mặt bích của lưu lượng kế từ khác "
        "nhau giữa các nhà chế tạo; do đó khi thay một lưu lượng kế bằng thiết bị của hãng khác, có "
        "thể phải làm lại hệ thống đường ống."))
    b.append(p(
        "Yêu cầu về đoạn ống thẳng phía trước và phía sau khác nhau tuỳ lưu lượng kế và tuỳ đặc tả của "
        "nhà chế tạo. Theo quy tắc kinh nghiệm, đoạn ống thẳng phải dài ít nhất 5D/2D tính từ điện "
        "cực và 5D/5D tính từ mặt bích lưu lượng kế, tương ứng theo chiều thượng nguồn và hạ nguồn. "
        "Để có độ chính xác tốt, nên tuân thủ cẩn thận khuyến nghị của nhà chế tạo về yêu cầu đường "
        "ống. Ở một số lưu lượng kế từ, cuộn dây được bố trí sao cho từ trường phân bố trong cuộn nhằm "
        "giảm thiểu ảnh hưởng của đường ống."))
    b.append(p(
        "Để đo chính xác, lưu lượng kế từ phải luôn đầy chất lỏng. Nếu chất lỏng không tiếp xúc với "
        "điện cực thì không thể đo được. Hình 28.40 minh hoạ điểm này. Nếu phép đo được thực hiện ở "
        "dòng không phải thẳng đứng thì nên đặt điện cực theo phương nằm ngang để loại trừ ảnh hưởng "
        "xấu của bọt khí, vì bọt khí có xu hướng tập trung ở phần trên của chất lỏng."))
    b.append(fig(40, F.fig(40), "vi"))
    b.append(p(
        "Khi chọn lưu lượng kế từ, phải tính đến một số yếu tố như:"))
    b.append(ul([
        "Chi phí, tính đơn giản, độ chính xác và độ tái lập",
        "Các khía cạnh luyện kim",
        "Prôfin vận tốc và nhiễu loạn phía thượng nguồn",
    ]))
    b.append(p(
        "Phần lớn quy trình dùng ống tròn, điều này làm cho việc xây dựng hệ thống đơn giản hơn. Lưu "
        "lượng kế nối với ống tròn cho kết quả tương đối tốt hơn so với ống chữ nhật hay ống vuông, "
        "và prôfin vận tốc của chất lỏng không bị ảnh hưởng bởi tính bất đối xứng. Tuy nhiên ở ống "
        "tròn, hiện tượng rìa của từ trường có thể đáng kể, khiến phải dùng hiệu chuẩn thực nghiệm."))
    b.append(p(
        "Việc chọn vật liệu chế tạo kênh dẫn của lưu lượng kế từ đòi hỏi cẩn trọng. Nếu chất lưu không "
        "phải kim loại thì một kênh không dẫn điện hoặc được cách điện là đủ; khi đó phải dùng điện "
        "cực ướt. Điện cực phải được thiết kế đủ lớn để giữ trở kháng đầu ra ở mức chấp nhận được. "
        "Đồng thời phải xử lý tín hiệu điện cực cẩn thận, vì trong nhiều trường hợp, hỏng hóc của "
        "phần điện tử xử lý tín hiệu chuẩn là nguyên nhân chính làm lưu lượng kế ngừng làm việc."))
    b.append(fig(41, F.fig(41), "vi"))
    b.append(p(
        "Lưu lượng kế từ không cần bảo trì liên tục, trừ việc hiệu chuẩn định kỳ. Tuy vậy vẫn có thể "
        "xảy ra phủ cặn điện cực, hư hỏng lớp lót và hỏng phần điện tử. Mọi sửa đổi hay sửa chữa phải "
        "được xử lý cẩn thận vì khi lắp lại có thể mất một phần độ chính xác; sau mỗi lần sửa đổi hay "
        "sửa chữa thường phải hiệu chuẩn lại."))
    b.append(p(
        "Lớp lót của lưu lượng kế từ thường bị hư hỏng do có mảnh vụn và chất rắn trong chất lỏng. "
        "Ngoài ra, việc dùng chất lỏng không tương thích với lớp lót, mài mòn, nhiệt độ quá cao, cùng "
        "việc lắp đặt và tháo dỡ cũng góp phần làm hỏng lớp lót. Ăn mòn điện cực cũng có thể là yếu "
        "tố góp phần. Trong một số trường hợp, lưu lượng kế từ có thể sửa tại chỗ dù hư hỏng nặng; "
        "trong trường hợp khác phải gửi về nhà chế tạo. Thường nhà chế tạo cung cấp phụ tùng cho điện "
        "cực, lớp lót, ống dòng và các linh kiện điện tử."))
    b.append(p(
        "Hiệu chuẩn lưu lượng kế điện từ được thực hiện bằng bộ hiệu chuẩn lưu lượng kế từ hoặc bằng "
        "phương pháp điện tử. Bộ hiệu chuẩn là thiết bị chính xác đưa tín hiệu đầu ra mô phỏng của "
        "phần sơ cấp vào bộ biến đổi, dùng để kiểm tra hoạt động đúng của các linh kiện điện tử và "
        "chỉnh mạch điện tử. Cách khác là đưa tín hiệu thử thích hợp vào từng linh kiện điện tử rời. "
        "Trong một số trường hợp phải hiệu chuẩn thực nghiệm ở lưu lượng bằng không, khi lưu lượng kế "
        "đã đầy chất lưu đứng yên."))
    b.append(p(
        "Chỉ có thể ứng dụng lưu lượng kế từ với chất lỏng dẫn điện như axit, bazơ, bùn, thực phẩm, "
        "thuốc nhuộm, polymer, nhũ tương và các hỗn hợp phù hợp có độ dẫn điện lớn hơn mức tối thiểu "
        "yêu cầu. Nói chung lưu lượng kế từ không phù hợp với chất lỏng chứa vật liệu hữu cơ và "
        "hydrocarbon. Theo quy tắc kinh nghiệm, có thể dùng lưu lượng kế từ nếu hỗn hợp chứa tối "
        "thiểu khoảng 10 % chất lỏng dẫn điện."))
    b.append(p(
        "Việc không có ràng buộc trực tiếp nào về số Reynolds cùng thiết kế không có vật cản của lưu "
        "lượng kế từ khiến chúng thực dụng cho những ứng dụng có chất lỏng dẫn điện độ nhớt cao — loại "
        "có thể làm tắc các lưu lượng kế khác. Chúng cũng đo được dòng hai chiều."))
    b.append(p(
        "Trái với niềm tin phổ biến, lưu lượng kế từ thể hiện một mức độ nhạy nhất định với prôfin "
        "dòng. Một khía cạnh quan trọng khác là ảnh hưởng của dòng rối. Đáng tiếc là có rất ít thông "
        "tin về hành vi của dòng rối khi nằm trong từ trường ngang. Hình 28.41 cho một ví dụ về prôfin "
        "dòng bị nhiễu loạn: chất lưu bị hãm gần tâm kênh và được gia tốc ở phía trên và phía dưới, "
        "gần các điện cực."))
    b.append(p(
        "Một điểm quan trọng ở lưu lượng kế điện từ là hiệu ứng thuỷ động lực từ, đặc biệt rõ ở chất "
        "lưu có tính từ. Thuỷ động lực từ là khả năng của từ trường làm biến đổi prôfin dòng. Ở một số "
        "ứng dụng, nhiễu loạn vận tốc do hiệu ứng này đủ lớn để ảnh hưởng tới độ chính xác, như với "
        "natri lỏng và các dung dịch của nó."))

    # ---------------------------------------------------------------- conductivity
    b.append(h3("Ảnh hưởng của độ dẫn điện của chất lưu", "Effects of Electric Conductivity of Fluid"))
    b.append(p(
        "Để lưu lượng kế điện từ làm việc chính xác, chất lỏng phải có độ dẫn điện tối thiểu từ "
        "1 µS cm<sup>−1</sup> đến 5 µS cm<sup>−1</sup>. Phần lớn ứng dụng thông thường dùng chất lỏng "
        "có độ dẫn điện lớn hơn 5 µS cm<sup>−1</sup>. Tuy vậy, để làm việc chính xác, yêu cầu về độ "
        "dẫn điện tối thiểu có thể bị ảnh hưởng bởi chiều dài dây dẫn từ cảm biến tới phần điện tử của "
        "bộ biến đổi."))
    b.append(p(
        "Lưu lượng kế xoay chiều nhạy với lớp phủ không dẫn điện trên điện cực, có thể gây dịch "
        "hiệu chuẩn hoặc mất tín hiệu hoàn toàn. Ngược lại, lưu lượng kế một chiều không bị ảnh hưởng "
        "nhiều đến vậy, trừ khi độ dẫn điện giữa hai điện cực xuống dưới mức tối thiểu. Ở một số lưu "
        "lượng kế, điện cực thay thế dễ dàng; ở loại khác, điện cực có thể được làm sạch bằng phương "
        "pháp thích hợp. Nếu phủ cặn là vấn đề thường xuyên thì nên xét tới biện pháp làm sạch bằng "
        "siêu âm và các phương pháp khác."))
    b.append(p(
        "Việc chỉnh điểm không của lưu lượng kế từ xoay chiều đòi hỏi bù nhiễu. Nếu chỉnh điểm không "
        "bằng chất lưu nào khác ngoài chất lưu công nghệ thì có thể gây sai số nghiêm trọng do độ dẫn "
        "điện khác nhau. Tương tự, nếu điện cực bị phủ một chất cách điện thì độ dẫn điện hiệu dụng "
        "của điện cực thay đổi, gây dịch hiệu chuẩn. Nếu lớp phủ thay đổi theo thời gian thì lưu lượng "
        "kế có thể liên tục phải hiệu chuẩn lại mới cho số đọc tái lập được."))
    b.append(p(
        "Điện trở giữa hai điện cực có thể tính gần đúng bằng <i>R</i> = 1/<i>δd</i>, trong đó "
        "<i>δ</i> là độ dẫn điện của chất lưu và <i>d</i> là đường kính điện cực. Với nước máy, "
        "<i>δ</i> = 200 µS cm<sup>−1</sup>; với xăng, <i>δ</i> = 0,01 µS cm<sup>−1</sup>; với cồn, "
        "<i>δ</i> = 0,2 µS cm<sup>−1</sup>. Một điện cực đường kính 0,74 cm tiếp xúc với nước máy cho "
        "điện trở 6756 Ω."))

    # ---------------------------------------------------------------- demodulation
    b.append(h3("Thu nhận tín hiệu và giải điều chế", "Signal Pickup and Demodulation Techniques"))
    b.append(p(
        "Lưu lượng kế từ là thiết bị bốn dây, cần nguồn điện ngoài để làm việc. Riêng với lưu lượng kế "
        "từ xoay chiều, cáp nguồn cao áp và cáp tín hiệu hạ áp phải đi riêng, tốt nhất là trong hai "
        "ống dẫn khác nhau; còn với lưu lượng kế một chiều, cáp nguồn và cáp tín hiệu có thể đi chung "
        "một ống, vì điện áp và tần số kích thích nam châm thấp hơn nhiều. Một số nhà chế tạo cung cấp "
        "cáp đặc biệt kèm theo lưu lượng kế."))
    b.append(p(
        "Ở lưu lượng kế xoay chiều, tín hiệu điện cực có thể được khuếch đại dễ dàng hơn nhiều so với "
        "loại một chiều. Đó là lý do lưu lượng kế xoay chiều đã được dùng thành công để đo lưu lượng "
        "rất nhỏ, cũng như dòng của chất lưu dẫn điện rất yếu. Tuy vậy, lưu lượng kế xoay chiều phức "
        "tạp hơn, cồng kềnh hơn, đắt hơn và cần nam châm điện có gông ghép lá thép cùng nguồn nuôi ổn "
        "định. Ở một số lưu lượng kế, có thể thu được đầu ra tín hiệu đủ lớn mà không cần gông, bằng "
        "cách tạo từ trường bằng cuộn dây trần; khi đó hiệu ứng biến áp lên dây nối giảm đáng kể."))
    b.append(p(
        "Một trong những nhược điểm chính của lưu lượng kế xoay chiều là khó tách tín hiệu do hiệu ứng "
        "biến áp ra khỏi tín hiệu có ích. Việc tách hai tín hiệu dựa trên thực tế là tín hiệu phụ "
        "thuộc lưu lượng và tín hiệu biến áp lệch pha nhau 90°: tín hiệu có ích tỷ lệ với cường độ từ "
        "trường, còn tín hiệu biến áp tỷ lệ với đạo hàm theo thời gian của cường độ từ trường. Tổng "
        "điện áp <i>v</i><sub>T</sub> có thể viết:"))
    b.append(eq("v<sub>T</sub> = v<sub>F</sub> + v<sub>t</sub> = V<sub>F</sub> sin(ωt) + "
                "V<sub>t</sub> cos(ωt)", "28.62"))
    b.append(p("trong đó <i>v</i><sub>F</sub> là điện áp cảm ứng do lưu lượng chất lỏng, còn "
               "<i>v</i><sub>t</sub> là điện áp do hiệu ứng biến áp trên dây dẫn, v.v."))
    b.append(p(
        "Có thể dùng kỹ thuật giải điều chế nhạy pha để loại bỏ điện áp do hiệu ứng biến áp. Dòng từ "
        "hoá cuộn dây <i>i</i><sub>m</sub> = <i>I</i><sub>m</sub> sin(ω<i>t</i>) được cảm nhận và nhân "
        "với tổng điện áp <i>v</i><sub>T</sub>, cho:"))
    b.append(eq("v<sub>T</sub> i<sub>m</sub> = [V<sub>F</sub> sin(ωt) + V<sub>t</sub> cos(ωt)] "
                "I<sub>m</sub> sin(ωt)", "28.63"))
    b.append(p(
        "Lấy tích phân Phương trình 28.63 trên một chu kỳ từ 0 đến 2π sẽ loại bỏ điện áp biến áp, chỉ "
        "còn lại điện áp tỷ lệ với lưu lượng:"))
    b.append(eq("V<sub>f</sub> = V<sub>F</sub> I<sub>m</sub> π", "28.64"))
    b.append(p(
        "trong đó <i>V</i><sub>f</sub> là điện áp sau khi tích phân. Điện áp này tỷ lệ với điện áp cảm "
        "ứng, có điều chỉnh bởi các hằng số <i>I</i><sub>m</sub> và π."))
    b.append(p(
        "Trong thực tế tình hình có thể phức tạp hơn nhiều do dịch pha gây ra bởi dòng xoáy trong các "
        "vật rắn và vật dẫn gần đó. Các lý do khác làm phức tạp thêm gồm các hài do tính phi tuyến "
        "như hiện tượng trễ, và ghép điện dung."))
    b.append(p(
        "Cần nối đất tốt cho lưu lượng kế từ, như ở Hình 28.42, để cách ly điện thế đồng pha tương "
        "đối cao. Nguồn điện thế đất có thể nằm trong chất lỏng hoặc trong đường ống. Trong thực tế, "
        "nếu ống dẫn điện và tiếp xúc với chất lỏng thì phải nối đất lưu lượng kế vào ống. Nếu ống làm "
        "bằng vật liệu không dẫn điện thì phải lắp các vòng nối đất để duy trì tiếp xúc với chất lỏng."))
    b.append(fig(42, F.fig(42), "vi"))
    b.append(p(
        "Nếu lưu lượng kế không được nối đất cẩn thận theo điện thế của chất lưu trong ống thì các "
        "điện cực có thể phải chịu điện áp đồng pha quá lớn, làm giảm nghiêm trọng độ chính xác. "
        "Trong một số trường hợp, điện thế đất quá cao có thể làm hỏng phần điện tử, vì đường có trở "
        "kháng thấp nhất xuống đất của mọi điện áp lạ trong chất lỏng sẽ là qua các điện cực."))
    b.append(p(
        "Một số lưu lượng kế từ thương mại đã được phát triển để làm việc với dạng sóng răng cưa hoặc "
        "xung vuông. Cho tới nay vẫn chưa có chuẩn thống nhất cho lưu lượng kế từ cũng như quy trình "
        "hiệu chuẩn chung; các nhà chế tạo dùng thiết kế riêng cho kênh dẫn, nam châm điện, cuộn dây "
        "và bộ xử lý tín hiệu. Phần lớn nhà chế tạo cung cấp dữ liệu hiệu chuẩn của riêng mình."))

    # ---------------------------------------------------------------- further
    b.append(h3("Thông tin thêm", "Further Information"))
    b.append(wl([
        "J. P. Bentley, <i>Principles of Measurement Systems</i>, ấn bản 2, New York: Longman "
        "Scientific and Technical, 1988.",
        "E. O. Doebelin, <i>Measurement Systems: Application and Design</i>, ấn bản 4, New York: "
        "McGraw-Hill, 1990.",
        "J. P. Holman, <i>Experimental Methods for Engineers</i>, ấn bản 5, New York: McGraw-Hill, "
        "1989.",
        "J. A. Shercliff, <i>Electromagnetic Flow-Measurements</i>, New York: Cambridge University "
        "Press, 1987.",
        "D. W. Spitzer, <i>Industrial Flow Measurement</i>, Research Triangle Park, NC: Instrument "
        "Society of America, 1990.",
    ]))
    return "".join(b)


def sec_28_6_en():
    b = []
    b.append(h2("28.6 Electromagnetic Flowmeters", "Electromagnetic Flowmeters"))
    b.append(p("Halit Eren."))
    b.append(p(
        "Magnetic flowmeters have been widely used in industry for many years. Unlike many other types "
        "of flowmeters, they offer true noninvasive measurements. They are easy to install and use to "
        "the extent that existing pipes in a process can be turned into meters simply by adding "
        "external electrodes and suitable magnets. They can measure reverse flows and are insensitive "
        "to viscosity, density, and flow disturbances. Electromagnetic flowmeters can rapidly respond "
        "to flow changes and they are linear devices for a wide range of measurements. In recent "
        "years, technological refinements have resulted in much more economical, accurate, and smaller "
        "instruments than the previous versions."))
    b.append(p(
        "As in the case of many electric devices, the underlying principle of the electromagnetic "
        "flowmeter is Faraday's law of electromagnetic induction. The induced voltages in an "
        "electromagnetic flowmeter are linearly proportional to the mean velocity of liquids or to the "
        "volumetric flow rates. As is the case in many applications, if the pipe walls are made from "
        "nonconducting elements, then the induced voltage is independent of the properties of the "
        "fluid."))
    b.append(p(
        "The accuracy of these meters can be as low as 0.25% and, in most applications, an accuracy of "
        "1% is used. At worst, 5% accuracy is obtained in some difficult applications where impurities "
        "of liquids and the contact resistances of the electrodes are inferior as in the case of "
        "low-purity sodium liquid solutions."))

    # ---------------------------------------------------------------- faraday
    b.append(h3("Faraday's Law of Induction", "Faraday's Law of Induction"))
    b.append(p(
        "This law states that if a conductor of length <i>l</i> (m) is moving with a velocity <i>v</i> "
        "(m s<sup>−1</sup>), perpendicular to a magnetic field of flux density <i>B</i> (Tesla), then "
        "the induced voltage <i>e</i> across the ends of the conductor can be expressed by:"))
    b.append(eq("e = B l v", "28.57"))
    b.append(p(
        "The principle of application of Faraday's law to an electromagnetic flowmeter is given in "
        "Figure 28.36. The magnetic field, the direction of the movement of the conductor, and the "
        "induced emf are all perpendicular to each other."))
    b.append(fig(36, F.fig(36), "en"))
    b.append(p(
        "Figure 28.37 illustrates a simplified electromagnetic flowmeter in greater detail. Externally "
        "located electromagnets create a homogeneous magnetic field passing through the pipe and the "
        "liquid inside it. When a conducting flowing liquid cuts through the magnetic field, a voltage "
        "is generated along the liquid path between two electrodes positioned on the opposite sides "
        "of the pipe."))
    b.append(p(
        "In the case of electromagnetic flowmeters, the conductor is the liquid flowing through the "
        "pipe, and the length of the conductor is the distance between the two electrodes, which is "
        "equal to the tube diameter. The velocity of the conductor is proportional to the mean flow "
        "velocity of the liquid. Hence, the induced voltage becomes:"))
    b.append(eq("e = B D v", "28.58"))
    b.append(p(
        "where <i>D</i> (m) is the diameter of the pipe. If the magnetic field is constant and the "
        "diameter of the pipe is fixed, the magnitude of the induced voltage will only be proportional "
        "to the velocity of the liquid. If the ends of the conductor, in this case the sensors, are "
        "connected to an external circuit, the induced voltage causes a current, <i>i</i>, to flow, "
        "which can be processed suitably as a measure of the flow rate. The resistance of the moving "
        "conductor can be represented by <i>R</i> to give the terminal voltage <i>v</i><sub>T</sub> of "
        "the moving conductor as <i>v</i><sub>T</sub> = <i>e</i> − <i>iR</i>."))
    b.append(p(
        "Electromagnetic flowmeters are often calibrated to determine the volumetric flow of the "
        "liquid. The volume of liquid flow, <i>Q</i> (L s<sup>−1</sup>), can be related to the average "
        "fluid velocity as:"))
    b.append(eq("Q = A v", "28.59"))
    b.append(p("Writing the area, <i>A</i> (m<sup>2</sup>), of the pipe as:"))
    b.append(eq("A = πD<sup>2</sup> / 4", "28.60"))
    b.append(p("gives the induced voltage as a function of the flow rate:"))
    b.append(eq("e = 4BQ / πD", "28.61"))
    b.append(p(
        "Equation 28.61 indicates that in a carefully designed flowmeter, if all other parameters are "
        "kept constant, then the induced voltage is linearly proportional to the liquid flow only."))
    b.append(p(
        "Based on Faraday's law of induction, there are many different types of electromagnetic "
        "flowmeters available, such as ac, dc, and permanent magnet types. The two most commonly used "
        "ones are the ac and dc types; this section concentrates mainly on those two."))
    b.append(p(
        "Although the induced voltage is directly proportional to the mean value of the liquid flow, "
        "the main difficulty in the use of electromagnetic flowmeters is that the amplitude of the "
        "induced voltage is small relative to extraneous voltages and noise. Noise sources include:"))
    b.append(ul([
        "Stray voltage in the process liquid",
        "Capacitive coupling between signal and power circuits",
        "Capacitive coupling in connection leads",
        "Electromechanical emf induced in the electrodes and the process fluid",
        "Inductive coupling of the magnets within the flowmeter",
    ]))

    # ---------------------------------------------------------------- construction
    b.append(h3("Construction and Operation of Electromagnetic Flowmeters",
                "Construction and Operation of Electromagnetic Flowmeters"))
    b.append(p(
        "Common to both ac and dc electromagnetic flowmeters, the magnetic coils create a magnetic "
        "field that passes through the flow tube and process fluid. As the conductive fluid flows "
        "through the flowmeter, a voltage is induced between the electrodes in contact with the "
        "process liquid. The electrodes are placed at positions where maximum potential differences "
        "occur. The electrodes are electrically isolated from the pipe walls by nonconductive liners "
        "to prevent short-circuiting of electrode signals. The liner also serves as protection to the "
        "flow tube to eliminate galvanic action and possible corrosion due to metal contacts. "
        "Electrodes are held in place by holders that also act as sealing."))
    b.append(p(
        "Dimensionally, magnetic flowmeters are manufactured from 2 mm to 1.2 m in diameter. In a "
        "particular application, the determination of the size of the flowmeter is a matter of "
        "selecting the one that can handle the anticipated liquid velocities. The anticipated velocity "
        "of the liquid must be within the linear range of the device. As an example of a typical guide "
        "for selection, the capacities of various size flowmeters are given in Figure 28.38."))
    b.append(fig(37, F.fig(37), "en"))
    b.append(p(
        "Some electromagnetic flowmeters are made from replaceable flow tubes whereby the field coils "
        "are located external to the tubes. In these flowmeters, the flanges are located far apart in "
        "order to reduce their adverse effects on the accuracy of measurements; hence, they are "
        "relatively larger in dimensions. Whereas in others, the field coils are located closer to the "
        "flow tube or even totally integrated together; in this case the flanges could be located "
        "closer to the magnets and the electrodes, giving relatively smaller dimensions. On the other "
        "hand, the miniature and electrodeless magnetic flowmeters are so compact in size that "
        "face-to-face dimensions are short enough to allow them to be installed between two flanges."))
    b.append(fig(38, F.fig(38), "en"))
    b.append(p(
        "The wetted parts of a magnetic flowmeter include the liners, electrodes, and electrode "
        "holders. Many different materials such as rubber, teflon, polyurethane, polyethylene, etc. are "
        "used in the construction to suit process corrosivity, abrasiveness, and temperature "
        "constraints. The main body of a flowmeter and electrodes can be manufactured from stainless "
        "steel, tantalum, titanium, and various other alloys. Liners are selected mainly to withstand "
        "the abrasive and corrosive properties of the liquid. The electrodes must be selected such "
        "that they cannot be coated with insulating deposits of the process liquid during long periods "
        "of operation."))
    b.append(p(
        "The pipe between the electromagnets of a flowmeter must be made from nonmagnetic materials to "
        "allow the field to penetrate the fluid without any distortion. Therefore, the flow tubes are "
        "usually constructed of stainless steel or plastics. The use of steel is a better option "
        "because it adds strength to the construction. Flanges are protected with appropriate liners "
        "and do not make contact with the process fluid."))
    b.append(p(
        "In some electromagnetic flowmeters, electrodes are cleaned continuously or periodically by "
        "ultrasonic or electric means. Ultrasonics are specified for ac and dc type magnetic "
        "flowmeters when frequent severe insulating coating is expected on the electrodes, which might "
        "cause the flowmeter to cease to operate in an anticipated manner."))
    b.append(p(
        "The operation of a magnetic flowmeter is generally limited by factors such as linear "
        "characteristics, pressure ratings of flanges, and temperatures of the process fluids. The "
        "maximum temperature limit is largely dependent on the liner material selection and usually is "
        "set to around 200 °C. For example, ceramic liners can withstand high temperatures, but are "
        "subject to cracking in case of sudden changes in temperature of the process fluid."))
    b.append(p(
        "During the selection of electromagnetic flowmeters, the velocity constraints should be "
        "evaluated carefully to secure accurate performance over the expected range. The full-scale "
        "velocity of the flowmeter is typically 0.3 m s<sup>−1</sup> to 10 m s<sup>−1</sup>. Some "
        "flowmeters can measure lower velocities with somewhat poorer accuracy. Generally, employment "
        "of electromagnetic flowmeters over a velocity of 5 m s<sup>−1</sup> should be considered "
        "carefully because erosion of the pipe and damage to liners can be significant."))
    b.append(p(
        "The accuracy of a conventional magnetic flowmeter is usually expressed as a function of full "
        "scale (FS), typically 0.5% to 1% FS. However, dc flowmeters have a well-defined zero due to "
        "their automatic zeroing capabilities; therefore, they have a percentage rate of accuracy "
        "better than ac types, typically 0.5% to 2%."))

    # ---------------------------------------------------------------- types
    b.append(h3("Types of Electromagnetic Flowmeters", "Types of Electromagnetic Flowmeters"))
    b.append(h4("AC magnetic flowmeters", "AC magnetic flowmeters"))
    b.append(p(
        "In many commercial electromagnetic flowmeters, an alternating current of 50 Hz to 60 Hz in "
        "coils creates the magnetic field to excite the liquid flowing within the pipe. A voltage is "
        "induced in the liquid due to Faraday's law of induction, as explained above. A typical value "
        "of the induced emf in an ac flowmeter fixed on a 50 mm internal diameter pipe carrying "
        "500 L min<sup>−1</sup> is about 2.5 mV."))
    b.append(p(
        "Historically, ac magnetic flowmeters were the most commonly used types because they reduced "
        "polarization effects at the electrodes. In general, they are less affected by the flow "
        "profiles of the liquid inside the pipes. They allow the use of high-input-impedance amplifiers "
        "with low drift and high pass filters to eliminate slow and spurious voltage drifts emanating "
        "mainly from thermocouple and galvanic actions. These flowmeters find many applications as "
        "diverse as the measurement of blood flow in living specimens. Miniaturized sensors allow "
        "measurements on pipes and vessels as small as 2 mm in diameter; in these applications the "
        "excitation frequencies are higher than industrial types, 200 Hz to 1000 Hz."))
    b.append(p(
        "A major disadvantage of the ac flowmeter is that the powerful ac field induces spurious ac "
        "signals in the measurement circuits. This necessitates periodic adjustment of zero output at "
        "zero velocity conditions — more frequently than for dc counterparts. Also, in some harsh "
        "industrial applications, currents in the magnetic field can vary, due to voltage fluctuations "
        "and frequency variations in the power lines. The effect of fluctuations in the magnetic field "
        "can be minimized by the use of a reference voltage proportional to the strength of the "
        "magnetic field to compensate for these variations. To avoid the effects of noise and "
        "fluctuations, special cabling and calibration practices recommended by the manufacturers must "
        "be used to ensure accurate operation. Usually, the use of two conduits is required — one for "
        "signals and one for power. The cable lengths should also be set to certain levels to minimize "
        "noise and sensitivity problems."))
    b.append(p(
        "Ac flowmeters operating at 50, 60, or 400 Hz are readily available. In general, ac flowmeters "
        "can operate from 10 Hz to 5000 Hz. High frequencies are preferred in determining the "
        "instantaneous behavior of transients and pulsating flows. Nevertheless, in applications where "
        "extremely good conducting fluids and liquid metals are used, the frequency must be kept low "
        "to avoid skin effects. On the other hand, if the fluid is a poor conductor, the frequency must "
        "not be so high that dielectric relaxation is not instantaneous."))
    b.append(h4("DC magnetic flowmeters", "DC magnetic flowmeters"))
    b.append(p(
        "Unlike ac magnetic flowmeters, direct current or pulsed magnetic flowmeters excite the "
        "flowing liquid with a field operating at 3 Hz to 8 Hz. As the current to the magnet is turned "
        "on, a dc voltage is induced at the electrodes. The signals observed at the electrodes "
        "represent the sum of the induced voltage and the noise, as illustrated in Figure 28.39. When "
        "the current in the magnetic coils is turned off, the signal represents only the noise. "
        "Subtracting the measurement of the flowmeter when no current flows through the magnet from "
        "the measurement when current flows through the magnet effectively cancels out the effect of "
        "noise."))
    b.append(fig(39, F.fig(39), "en"))
    b.append(p(
        "If the magnetic field coils are energized by normal direct current, then several problems can "
        "occur: polarization, which is the formation of a layer of gas around the measured electrodes, "
        "as well as electrochemical and electromechanical effects. Some of these problems can be "
        "overcome by energizing the field coils at higher frequencies or ac. However, higher "
        "frequencies and ac generate transformer action in the signal leads and fluid path. Therefore, "
        "the coils are excited by dc pulses at low repetition rates to eliminate the transformer "
        "action. In some flowmeters, by appropriate sampling and digital signal processing techniques, "
        "the zero errors and the noise can be rejected substantially."))
    b.append(p(
        "The zero compensation inherent in dc magnetic flowmeters eliminates the necessity of zero "
        "adjustment. This allows the extraction of flow signals regardless of zero shifts due to "
        "spurious noise or electrode coating. Unlike ac flowmeters, a larger insulating electrode "
        "coating can be tolerated that could shift the effective conductivity significantly without "
        "affecting performance. If the effective conductivity remains high enough, a dc flowmeter will "
        "operate satisfactorily. Therefore, dc flowmeters are less susceptible to drifts, electrode "
        "coatings, and changes in process conditions in comparison with conventional ac flowmeters."))
    b.append(p(
        "Dc magnetic flowmeters do not have good response times due to the slow pulsed nature of their "
        "operation. However, as long as there are no rapid variations in the flow patterns, zero to "
        "full-scale response times of a few seconds do not create problems in the majority of "
        "applications. Power requirements are also much less as the magnet is energized part of the "
        "time. This gives an advantage in power saving of up to 75%."))
    b.append(p(
        "If the dc current to the magnet is constant, the proportional magnetic field can be kept "
        "steady, so the amplitudes of the dc voltages generated at the electrodes will be linearly "
        "proportional to the flow. However, in practice, the current to the magnet varies slightly due "
        "to line voltage and frequency variations. As in the case of ac flowmeters, voltage and "
        "frequency variations could necessitate the use of a reference voltage. Because the effect of "
        "noise can be eliminated more easily, the cabling requirements are not as stringent."))
    b.append(p(
        "To avoid electrolytic polarization of the electrodes, bipolar pulsed dc flowmeters have been "
        "designed. Modification of dc flowmeters also led to the development of miniature dc magnetic "
        "flowmeters with wafer design for a limited range of applications; the wafer design reduces "
        "the weight as well as the power requirements."))
    b.append(p("Table 28.11 provides a listing of several manufacturers of electromagnetic flowmeters."))
    b.append(_t2811("en"))

    # ---------------------------------------------------------------- installation
    b.append(h3("Installation and Practical Applications",
                "Installation and Practical Applications"))
    b.append(p(
        "Conventional ac and dc magnetic flowmeters have flanges at the inlet and the outlet that need "
        "to be bolted to the flanges of the pipe. Face-to-face dimensions of magnetic flowmeters differ "
        "between manufacturers; therefore, once the flowmeter is installed, new piping arrangements "
        "could be necessary if a flowmeter is replaced by one from a different manufacturer."))
    b.append(p(
        "Upstream and downstream straight piping requirements can vary from one flowmeter to another, "
        "depending on the manufacturer's specifications. As a rule of thumb, the straight portion of "
        "the pipe should be at least 5D/2D from the electrodes and 5D/5D from the face of the flowmeter "
        "in upstream and downstream directions, respectively. For good accuracy, one should adhere "
        "carefully to the recommendations of manufacturers for piping requirements. In some magnetic "
        "flowmeters, coils are used in such a way that the magnetic field is distributed in the coil to "
        "minimize the piping effect."))
    b.append(p(
        "For accurate measurements, magnetic flowmeters must be kept full of liquid at all times. If "
        "the liquid does not contact the electrodes, measurements cannot be taken. Figure 28.40 "
        "illustrates this point. If the measurements are made in other than vertical flows, the "
        "electrodes should be located in horizontal directions to eliminate the possible adverse "
        "effect of air bubbles, because air bubbles tend to concentrate on the top vertical part of the "
        "liquid."))
    b.append(fig(40, F.fig(40), "en"))
    b.append(p(
        "In the selection of magnetic flowmeters, a number of considerations must be taken into "
        "account, such as:"))
    b.append(ul([
        "Cost, simplicity, precision, and reproducibility",
        "Metallurgical aspects",
        "Velocity profiles and upstream disturbances",
    ]))
    b.append(p(
        "Most processes employ circular piping, which adds simplicity to the construction of the "
        "system. Flowmeters connected to circular pipes give relatively better results compared with "
        "rectangular or square-shaped pipes, and velocity profiles of the liquid are not affected by "
        "the asymmetry. However, in circular pipes, the fringing of the magnetic field can be "
        "significant, making it necessary to employ empirical calibrations."))
    b.append(p(
        "Selection of materials for constructing the channel of the magnetic flowmeter demands care. "
        "If the fluid is nonmetallic, a nonconducting or an insulated channel should be sufficient; in "
        "this case, wetted electrodes must be used. Electrodes must be designed to have sufficiently "
        "large dimensions to keep the output impedance at acceptable levels. Also, careful handling of "
        "electrode signals must be observed because, in many cases, malfunctioning of reference signal "
        "electronics is the main cause of flowmeter failure."))
    b.append(fig(41, F.fig(41), "en"))
    b.append(p(
        "Magnetic flowmeters do not require continuous maintenance, except for periodic calibration. "
        "Nevertheless, electrode coating, damage to the liners, and electronic failures can occur. Any "
        "modification or repair must be treated carefully because, when installed again, some accuracy "
        "can be lost; after each modification or repair, recalibration is usually necessary."))
    b.append(p(
        "Often, magnetic flowmeter liners are damaged by the presence of debris and solids in the "
        "process liquid. The use of liquid incompatible with the liners, wear due to abrasion, excess "
        "temperature, and installation and removal can also contribute to damage of the liners. "
        "Corrosion in the electrodes can be a further contributing factor. In some cases, magnetic "
        "flowmeters can be repaired on site even if severe damage occurs; in other cases, they must be "
        "shipped to the manufacturer for repair. Usually, manufacturers supply spare parts for "
        "electrodes, liners, flow tubes and electronic components."))
    b.append(p(
        "Calibration of electromagnetic flowmeters is achieved with a magnetic flowmeter calibrator or "
        "by electronic means. Magnetic flowmeter calibrators are precision instruments that inject "
        "simulated output signals of the primary flowmeter into the transmitter; effectively, this "
        "signal is used to check correct operation of electronic components and make adjustments to the "
        "electronic circuits. Alternatively, calibrations can also be made by injecting suitable test "
        "signals into discrete electronic components. In some cases, empirical calibrations must be "
        "performed at zero flow while the flowmeter is filled with the stationary process liquid."))
    b.append(p(
        "Application of magnetic flowmeters can only be realized with conductive liquids such as "
        "acids, bases, slurries, foods, dyes, polymers, emulsions, and suitable mixtures that have "
        "conductivities greater than the minimum conductivity requirements. Generally, magnetic "
        "flowmeters are not suitable for liquids containing organic materials and hydrocarbons. As a "
        "rule of thumb, magnetic flowmeters can be applied if the process liquid constitutes a minimum "
        "of about 10% conductive liquid in the mixture."))
    b.append(p(
        "The lack of any direct Reynolds number constraints and the obstructionless design of magnetic "
        "flowmeters make them practical for applications that involve conductive liquids of high "
        "viscosity, which could plug other flowmeters. They also measure bidirectional flows."))
    b.append(p(
        "Despite the contrary belief, magnetic flowmeters demonstrate a certain degree of sensitivity "
        "to flow profiles. Another important aspect is the effect of turbulence. Unfortunately, there "
        "is very little information available on the behavior of turbulent flows when they are in "
        "transverse magnetic fields. Figure 28.41 shows an example of a flow profile in which the "
        "velocity profile is perturbed: the fluid is being retarded near the center of the channel and "
        "accelerated at the top and bottom near the electrodes."))
    b.append(p(
        "An important point in electromagnetic flowmeters is the effect of magneto-hydrodynamics, "
        "especially prominent in fluids with magnetic properties. Hydrodynamics here is the ability of "
        "a magnetic field to modify the flow pattern. In some applications, the velocity perturbation "
        "due to the magneto-hydrodynamic effect can be serious enough to influence the accuracy of "
        "operation, as in the case of liquid sodium and its solutions."))

    # ---------------------------------------------------------------- conductivity
    b.append(h3("Effects of Electric Conductivity of Fluid", "Effects of Electric Conductivity of Fluid"))
    b.append(p(
        "For electromagnetic flowmeters to operate accurately, the process liquid must have a minimum "
        "conductivity of 1 µS cm<sup>−1</sup> to 5 µS cm<sup>−1</sup>. Most common applications involve "
        "liquids with conductivities greater than 5 µS cm<sup>−1</sup>. Nevertheless, for accurate "
        "operation, the requirement for the minimum conductivity of the liquid can be affected by the "
        "length of the leads from the sensors to the transmitter electronics."))
    b.append(p(
        "Ac flowmeters are sensitive to the nonconductive coating of the electrodes that may result in "
        "calibration shift or complete loss of signal. The dc flowmeters, on the other hand, should not "
        "be affected by nonconductive coating to such a great extent, unless the conductivity between "
        "the electrodes is less than the minimum required value. In some flowmeters, electrodes can be "
        "replaced easily; in others, they can be cleaned by suitable methods. If coating is a continual "
        "problem, ultrasonic and other cleaning methods should be considered."))
    b.append(p(
        "Zero adjustment of ac magnetic flowmeters requires compensation for noise. If the zero "
        "adjustment is performed with any fluid other than the process fluid, serious errors can result "
        "because of possible differences in conductivity. Similarly, if the electrodes are coated with "
        "an insulating substance, the effective conductivity of the electrodes can be altered, thereby "
        "causing a calibration shift. If the coating changes with time, the flowmeter can continually "
        "require calibration for repeatable readings."))
    b.append(p(
        "The resistance between electrodes can be approximated by <i>R</i> = 1/<i>δd</i>, where "
        "<i>δ</i> is the fluid conductivity and <i>d</i> is the electrode diameter. For tap water, "
        "<i>δ</i> = 200 µS cm<sup>−1</sup>; for gasoline, <i>δ</i> = 0.01 µS cm<sup>−1</sup>; and for "
        "alcohol, <i>δ</i> = 0.2 µS cm<sup>−1</sup>. A typical electrode with a 0.74 cm diameter in "
        "contact with tap water results in a resistance of 6756 Ω."))

    # ---------------------------------------------------------------- demodulation
    b.append(h3("Signal Pickup and Demodulation Techniques",
                "Signal Pickup and Demodulation Techniques"))
    b.append(p(
        "Magnetic flowmeters are four-wire devices that require an external power source for "
        "operation. Particularly in ac magnetic flowmeters, the high-voltage power cables and "
        "low-voltage signal cables must run separately, preferably in different conduits; whereas in dc "
        "magnetic flowmeters, the power and signal cables can be run in one conduit, because in dc-type "
        "magnetic flowmeters the voltage and the frequency of excitation of the electromagnets are "
        "relatively much lower. Some manufacturers supply special cables along with their flowmeters."))
    b.append(p(
        "In ac flowmeters, the electrode signals can be amplified much more readily compared with their "
        "dc counterparts. That is the reason why ac flowmeters have been used successfully to measure "
        "very low flow rates, as well as the flow of very weakly conducting fluids. Nevertheless, ac "
        "flowmeters tend to be more complicated, bulky and expensive, and they require electromagnets "
        "with laminated yokes together with stabilized power supplies. In some magnetic flowmeters, it "
        "is feasible to obtain sufficiently large flow signal outputs without the use of a yoke, by "
        "producing a magnetic field with naked coils; in this case, the transformer action to the "
        "connecting leads can be reduced considerably."))
    b.append(p(
        "One of the main drawbacks of ac-type flowmeters is that it is difficult to eliminate the "
        "signals due to transformer action from the useful signals. The separation of the two signals "
        "is achieved by exploiting the fact that the flow-dependent signal and the transformer signal "
        "are in quadrature: the useful signal is proportional to the field strength, and the "
        "transformer action is proportional to the time derivative of the field strength. The total "
        "voltage <i>v</i><sub>T</sub> can be expressed as:"))
    b.append(eq("v<sub>T</sub> = v<sub>F</sub> + v<sub>t</sub> = V<sub>F</sub> sin(ωt) + "
                "V<sub>t</sub> cos(ωt)", "28.62"))
    b.append(p("where <i>v</i><sub>F</sub> is the induced voltage due to liquid flow and "
               "<i>v</i><sub>t</sub> is the voltage due to transformer action on wires, etc."))
    b.append(p(
        "Phase-sensitive demodulation techniques can be employed to eliminate the transformer action "
        "voltage. The coil magnetizing current, <i>i</i><sub>m</sub> = <i>I</i><sub>m</sub> sin(ω<i>t</i>), "
        "is sensed and multiplied by the total voltage <i>v</i><sub>T</sub>, giving:"))
    b.append(eq("v<sub>T</sub> i<sub>m</sub> = [V<sub>F</sub> sin(ωt) + V<sub>t</sub> cos(ωt)] "
                "I<sub>m</sub> sin(ωt)", "28.63"))
    b.append(p(
        "Integration of Equation 28.63 over one period between 0 and 2π eliminates the transformer "
        "voltage, yielding only the voltage that is proportional to the flow:"))
    b.append(eq("V<sub>f</sub> = V<sub>F</sub> I<sub>m</sub> π", "28.64"))
    b.append(p(
        "where <i>V</i><sub>f</sub> is the voltage after integration. This voltage is proportional to "
        "the induced voltage modified by the constants <i>I</i><sub>m</sub> and π."))
    b.append(p(
        "In reality, this situation can be much more complicated because of phase shift due to eddy "
        "currents in nearby solids and conductors. Other reasons for complexity include the harmonics "
        "because of nonlinearity such as hysteresis, and capacitive pickup."))
    b.append(p(
        "A good electrical grounding of magnetic flowmeters, as illustrated in Figure 28.42, is "
        "required to isolate relatively high common mode potential. The sources of ground potential "
        "can be in the liquid or in the pipes. In practice, if the pipe is conductive and makes contact "
        "with the liquid, the flowmeter should be grounded to the pipe. If the pipe is made from "
        "nonconductive materials, ground rings should be installed to maintain contact with the process "
        "liquid."))
    b.append(fig(42, F.fig(42), "en"))
    b.append(p(
        "If the flowmeter is not grounded carefully relative to the potential of the fluid in the pipe, "
        "then the flowmeter electrodes could be exposed to excessive common mode voltages that can "
        "severely limit the accuracy. In some cases, excessive ground potential can damage the "
        "electronics because the least-resistance path to ground for any stray voltage in the liquid "
        "would be via the electrodes."))
    b.append(p(
        "Some commercial magnetic flowmeters have been developed that can operate on saw-tooth or "
        "square waveforms. Universally standardized magnetic flowmeters and generalized calibration "
        "procedures still do not exist, and manufacturers use their own particular design of flow "
        "channels, electromagnets, coils, and signal processors. Most manufacturers provide their own "
        "calibration data."))

    # ---------------------------------------------------------------- further
    b.append(h3("Further Information", "Further Information"))
    b.append(wl([
        "J. P. Bentley, <i>Principles of Measurement Systems</i>, 2nd ed., New York: Longman "
        "Scientific and Technical, 1988.",
        "E. O. Doebelin, <i>Measurement Systems: Application and Design</i>, 4th ed., New York: "
        "McGraw-Hill, 1990.",
        "J. P. Holman, <i>Experimental Methods for Engineers</i>, 5th ed., New York: McGraw-Hill, 1989.",
        "J. A. Shercliff, <i>Electromagnetic Flow-Measurements</i>, New York: Cambridge University "
        "Press, 1987.",
        "D. W. Spitzer, <i>Industrial Flow Measurement</i>, Research Triangle Park, NC: Instrument "
        "Society of America, 1990.",
    ]))
    return "".join(b)


def _t2812(lang):
    """Table 28.12 — manufacturers of ultrasonic transit time flowmeters.
    The source prints the nine companies in two columns; the two-column layout
    carries no meaning, so it is flattened to a single list."""
    if lang == "vi":
        hd = ("Công ty", "Địa chỉ và liên hệ")
        cap = ("Bảng 28.12 · Các công ty chế tạo và phân phối lưu lượng kế siêu âm thời gian truyền. "
               "Địa chỉ in lại đúng như bản gốc năm 1999.")
    else:
        hd = ("Company", "Address and contact")
        cap = ("Table 28.12 · Companies manufacturing and distributing ultrasonic transit time "
               "flowmeters. Addresses are reproduced as printed in the 1999 original.")
    rows = [
        ["Rittmeyer AG",
         "P.O. Box 2143, CH-6302 Zug, Switzerland<br>"
         "Tel: (+4141)-767-1000<br>Fax: (+4141)-767-1075<br>"
         "instrumentation@rittmeyer.ch<br>http://www.rittmeyer.com/"],
        ["Krohne Messtechnik GmbH&amp;Co.KG",
         "Postfach 10 08 62, Ludwig-Krohne-Strasse 5, 4100 Duisburg 1, Germany<br>"
         "http://www.krohne.com/"],
        ["Danfoss A/S", "DK-6430 Nordborg, Denmark<br>Tel: (+45) 74 88 22 22"],
        ["Panametrics, Inc.",
         "221 Crescent Street, Waltham, MA 02254<br>Tel: (617) 899-2719<br>"
         "http://www.panametrics.com/"],
        ["Accusonic Division, ORE International, Inc.",
         "P.O. Box 709, Falmouth, MA 02541<br>Tel: (508) 548-5800<br>http://www.ore.com/"],
        ["Fuji Electric Co., Ltd.",
         "12-1 Yurakucho 1-chome, Chiyoda-ku, Tokyo 100, Japan<br>Tel: Tokyo 211-7111"],
        ["Crouzet SA",
         "Division “Aérospatial”, 25, rue Jules-Védrines, 26027 Valence Cedex, France<br>"
         "Tel: 75 79 85 11"],
        ["Nusonics Inc.",
         "11391 E. Tecumseh St., Tulsa, OK 74116-1602<br>Tel: (918) 438-1010"],
        ["Ultraflux",
         "le technoparc, 17, rue Charles Edouard Jeanneret, 78306 Poissy Cedex, France<br>"
         "Tel: 33(1)39 79 26 40"],
    ]
    return table(hd, rows, cap, widths=("30%", "70%"))


def sec_28_7_vi():
    b = []
    b.append(h2("28.7 Lưu lượng kế siêu âm", "Ultrasonic Flowmeters"))
    b.append(p("Hans-Peter Vaterlaus, Thomas Hossle, Paolo Giordano và Christophe Bruttin."))
    b.append(p(
        "Lưu lượng là một trong những đại lượng vật lý quan trọng nhất được đo trong công nghiệp và "
        "trong quản lý nước. Có nhiều loại lưu lượng kế khác nhau, tuỳ theo yêu cầu do từng phân khúc "
        "thị trường đặt ra. Trong nhiều năm, lưu lượng kế kiểu chênh áp là thiết bị đo lưu lượng được "
        "dùng rộng rãi nhất cho dòng chất lưu trong ống và trong kênh hở, khi cần đo chính xác với chi "
        "phí hợp lý. Tuy nhiên, ở những thị trường như thuỷ điện, cấp nước, thuỷ lợi..., lưu lượng "
        "phải được đo mà không gây bất kỳ tổn thất cột áp hay sụt áp nào. Điều đó có nghĩa là không "
        "được phép có chi tiết chuyển động, không có thiết bị thứ cấp, cũng không có chỗ thắt nào. "
        "Hiện có hai loại lưu lượng kế thoả mãn yêu cầu này: lưu lượng kế điện từ và lưu lượng kế "
        "siêu âm. Trong khi lưu lượng kế siêu âm có thể dùng được với gần như mọi loại chất lỏng đang "
        "chảy, lưu lượng kế điện từ đòi hỏi chất lỏng phải có độ dẫn điện tối thiểu để hoạt động. "
        "Ngoài ra, giá thành lưu lượng kế siêu âm gần như không phụ thuộc đường kính ống, trong khi "
        "giá lưu lượng kế điện từ tăng rất mạnh theo đường kính ống."))
    b.append(p("Có nhiều kiểu lưu lượng kế siêu âm đang được dùng để đo lưu lượng:"))
    b.append(ol([
        "<b>Thời gian truyền:</b> đây là công nghệ hiện đại nhất và là kiểu được dùng rộng rãi nhất "
        "hiện nay, sẽ được trình bày trong mục này. Kiểu lưu lượng kế siêu âm này lợi dụng sự khác "
        "nhau về thời gian để một xung âm đi một quãng đường cố định, trước hết ngược chiều dòng rồi "
        "theo chiều dòng. Lưu lượng kế thời gian truyền nhạy với chất rắn lơ lửng hoặc bọt khí trong "
        "chất lưu.",
        "<b>Doppler:</b> kiểu này phổ biến hơn và rẻ hơn, nhưng không được coi là chính xác bằng lưu "
        "lượng kế thời gian truyền. Nó lợi dụng độ dịch tần số Doppler gây ra bởi âm phản xạ hoặc tán "
        "xạ từ các hạt lơ lửng trên đường đi của dòng, và vì vậy mang tính bổ sung nhiều hơn là cạnh "
        "tranh với lưu lượng kế thời gian truyền.",
        "<b>Tương quan chéo:</b> hai đoạn đo được đặt cách nhau một khoảng xác định. Cả hai đo độ hấp "
        "thụ năng lượng của tín hiệu siêu âm. Một phép tương quan chéo sẽ tính ra vận tốc dòng.",
        "<b>Dịch pha:</b> pha của tín hiệu phát và tín hiệu thu được đo theo chiều dòng và ngược chiều "
        "dòng. Góc dịch pha thu được tỷ lệ trực tiếp với vận tốc dòng.",
        "<b>Trôi:</b> độ trôi của một tín hiệu siêu âm đi qua dòng được đo bằng độ suy giảm tín hiệu.",
    ]))

    # ---------------------------------------------------------------- transit time
    b.append(h3("Lưu lượng kế thời gian truyền", "Transit Time Flowmeter"))
    b.append(h4("Nguyên lý làm việc", "Principle of Operation"))
    b.append(p(
        "Phương pháp âm học đo lưu lượng dựa trên thực tế là vận tốc lan truyền của sóng âm và vận tốc "
        "dòng chảy cộng vector với nhau. Loại lưu lượng kế này đo hiệu thời gian truyền giữa hai xung "
        "siêu âm phát ngược chiều dòng <i>t</i><sub>21</sub> và xuôi chiều dòng "
        "<i>t</i><sub>12</sub> qua dòng chảy, như trên Hình 28.43. Nếu trong ống không có thành phần "
        "vận tốc ngang, hai thời gian truyền của các xung âm học này được cho bởi:"))
    b.append(eq("t<sub>12</sub> = L<sub>w</sub> / (c + v̄<sub>a</sub> cos φ) &nbsp;&nbsp;và&nbsp;&nbsp; "
                "t<sub>21</sub> = L<sub>w</sub> / (c − v̄<sub>a</sub> cos φ)", "28.65"))
    b.append(defs([
        ("<i>L</i><sub>w</sub>", "Khoảng cách trong chất lưu giữa hai đầu dò"),
        ("<i>c</i>", "Tốc độ âm thanh ở điều kiện làm việc"),
        ("φ", "Góc giữa trục ống và đường truyền âm"),
        ("v̄<sub>a</sub>", "Vận tốc dọc trục trung bình trên quãng đường <i>L</i><sub>w</sub>"),
    ]))
    b.append(fig(43, F.fig(43), "vi"))
    b.append(p(
        "Vì các đầu dò thường được dùng đồng thời làm bộ phát và bộ thu, hiệu thời gian truyền có thể "
        "xác định được với cùng một cặp đầu dò. Như vậy vận tốc dọc trục trung bình v̄<sub>a</sub> dọc "
        "theo đường truyền được cho bởi:"))
    b.append(eq("v̄<sub>a</sub> = (L<sub>w</sub> / 2 cos φ) (1/t<sub>21</sub> − 1/t<sub>12</sub>) = "
                "(D / 2 cos φ sin φ) (1/t<sub>21</sub> − 1/t<sub>12</sub>)", "28.66"))
    b.append(p(
        "Ví dụ sau cho thấy những yêu cầu đặt ra đối với kỹ thuật đo thời gian: giả sử một ống kín có "
        "đường kính <i>D</i> = 150 mm, góc φ = 60°, vận tốc dòng v̄<sub>a</sub> = 1 m s<sup>−1</sup> và "
        "nhiệt độ nước 20 °C. Kết quả là thời gian truyền vào khoảng 116 µs và hiệu thời gian Δ<i>t</i> "
        "(Δ<i>t</i> = <i>t</i><sub>12</sub> − <i>t</i><sub>21</sub>) vào cỡ 78 ns. Để đạt độ chính xác "
        "1 % của dải đo tương ứng, Δ<i>t</i> phải được đo với độ phân giải ít nhất 100 ps "
        "(1 × 10<sup>−10</sup> s)."))
    b.append(note(
        "Bản gốc in “116 s” — rõ ràng là thiếu ký hiệu micro. Với <i>D</i> = 150 mm, φ = 60° và "
        "<i>c</i> ≈ 1482 m s<sup>−1</sup> ở 20 °C, quãng đường <i>L</i><sub>w</sub> = <i>D</i>/sin φ ≈ "
        "0,173 m cho thời gian truyền 116,9 µs; giá trị 78 ns của Δ<i>t</i> trong bản gốc cũng chỉ "
        "khớp với đơn vị micro giây. Bản dịch ghi 116 µs."))
    b.append(p(
        "Các kỹ thuật đo thời gian tiêu chuẩn không thể đáp ứng những yêu cầu như vậy, nên phải áp "
        "dụng các kỹ thuật đặc biệt. Ưu điểm của cách tiếp cận đo số thực hiện hoàn toàn bằng kỹ thuật "
        "số hiện đại là giá trị đo được xử lý trực tiếp bằng một vi xử lý. Vấn đề khó nhất là đạt được "
        "độ phân giải yêu cầu và xử lý được jitter của các cổng logic số. Trong kỹ thuật đo, người ta "
        "biết rằng nếu tín hiệu được lấy mẫu nhiều lần (<i>N</i><sub>n</sub>), độ phân giải tăng theo "
        "số mẫu (“lấy mẫu bội”) [1]. Hiểu biết này không chỉ được áp dụng cho tín hiệu tương tự mà còn "
        "cho tín hiệu thời gian truyền, và được dùng trong công nghệ lưu lượng kế ngày nay. Thời gian "
        "lan truyền <i>t</i> (<i>t</i><sub>12</sub>, <i>t</i><sub>21</sub>), phụ thuộc quãng đường xung "
        "âm phải đi qua chất lưu, được đo nhiều lần. Do đó ta thu được hệ thức sau [2]:"))
    b.append(eq("<i>t</i> = (1/<i>N</i><sub>n</sub>) ∫<sub>0</sub><sup>τ</sup> (1/<i>f</i>) d<i>t</i>",
                "28.67"))
    b.append(p("trong đó τ là thời gian tích phân, và <i>f</i> là tần số."))
    b.append(p(
        "Theo sơ đồ khối trên Hình 28.44, người ta dùng hai bộ đếm. Một bộ đếm <i>N</i><sub>t</sub> "
        "được đồng hồ hoá trong suốt thời gian đo bằng một bộ dao động thạch anh ổn định; bộ kia đếm "
        "số mẫu <i>N</i><sub>n</sub>. Phép đo dừng sau một khoảng thời gian vài miligiây và sau khi "
        "<i>N</i><sub>n</sub> đã đạt một giá trị nguyên. Hai số đếm <i>N</i><sub>t</sub> và "
        "<i>N</i><sub>n</sub> được dùng để tính thời gian lan truyền <i>t</i><sub>12</sub> hoặc "
        "<i>t</i><sub>21</sub> bằng cách chia <i>N</i><sub>t</sub> cho <i>N</i><sub>n</sub>. Độ phân "
        "giải <i>r</i> được tính bằng:"))
    b.append(eq("<i>r</i> = 1 / (<i>N</i><sub>n</sub> <i>f</i>)", "28.68"))
    b.append(fig(44, F.fig(44), "vi"))
    b.append(p("Ưu điểm của phương pháp đo này đối với lưu lượng kế thời gian truyền là:"))
    b.append(ol([
        "Độ phân giải của phép đo vận tốc là không đổi (giá trị điển hình 0,8 mm s<sup>−1</sup>).",
        "Độ chính xác gần như chỉ phụ thuộc độ ổn định và hệ số nhiệt độ của bộ dao động thạch anh.",
        "Nhờ lấy mẫu nhiều lần, jitter của logic số được lấy trung bình.",
    ]))

    # ---------------------------------------------------------------- sensors
    b.append(h4("Cảm biến", "Sensors"))
    b.append(p(
        "Đầu dò gồm phần tử áp điện biến đổi năng lượng điện thành năng lượng âm, cùng kết cấu cơ bản "
        "để đỡ gốm áp điện và tạo các kết nối điện. Thiết kế đầu dò bao gồm việc chọn phần tử áp điện, "
        "xác định kích thước và tần số cộng hưởng thích hợp, và chế tạo sao cho chịu được ứng suất "
        "nhiệt và cơ, xem Hình 28.45. Xét theo mô hình đường truyền [3, 4], đáp ứng điện–âm tối ưu và "
        "sự phối hợp tốt nhất các trở kháng âm <i>Z</i> = ρ<i>c</i> của các phần tử đầu dò khác nhau "
        "là quan trọng. Không chỉ phải thu được dạng sóng thích hợp để điện tử phát hiện, mà còn phải "
        "cực tiểu hoá tổn thất năng lượng khi sóng đi qua nhiều mặt phân cách. Do sự đa dạng rộng của "
        "kích thước ống và điều kiện dòng chảy, có một số cấu hình cảm biến khác nhau cho lưu lượng kế "
        "thời gian truyền."))
    b.append(fig(45, F.fig(45), "vi"))
    b.append(h4("Kiểu dọc trục", "Axial"))
    b.append(p(
        "Do hiệu quãng đường nhỏ trong các ống đường kính nhỏ, cần cho xung âm đi thẳng dọc theo trục "
        "ống để bảo đảm quãng đường đủ dài. Hình 28.46 cho một ví dụ về đoạn ống cảm biến kiểu dọc "
        "trục. Giới hạn trên về cỡ ống cho loại cảm biến này là khoảng 0,075 m [5]."))
    b.append(fig(46, F.fig(46), "vi"))
    b.append(h4("Kiểu hướng tâm", "Radial"))
    b.append(p(
        "Nhiều nhà chế tạo cung cấp các đoạn ống đo hoàn chỉnh với đầu dò âm gắn sẵn ở hai bên của một "
        "đoạn ống nối. Những cảm biến này, như trên Hình 28.47, thường được gọi là “hướng tâm” do cách "
        "bố trí đầu dò. Giới hạn dưới về cỡ ống của cảm biến kiểu hướng tâm là khoảng 100 mm."))
    b.append(fig(47, F.fig(47), "vi"))
    b.append(h4("Lắp đặt tại hiện trường", "Field Mounting"))
    b.append(p(
        "Cảm biến kiểu hướng tâm thường được dùng để trang bị cho một tuyến ống đang tồn tại, khi muốn "
        "thực hiện việc lắp đặt mà không phải cắt bỏ một đoạn ống. Để đáp ứng yêu cầu này, có thể dùng "
        "các đầu dò lắp tại hiện trường, được gắn keo, khoan hoặc hàn vào đoạn ống đang có. Bằng cách "
        "này có thể đạt được các đoạn ống đo có đường kính tới 13 m hoặc hơn."))
    b.append(h4("Kiểu kẹp ngoài", "Clamp-on"))
    b.append(p(
        "Nếu cần một cách lắp đặt mà thành ống không bị đầu dò xuyên qua thì hệ kẹp ngoài là lựa chọn "
        "đúng. Đạt độ chính xác thấp hơn và hiệu chuẩn có phần phức tạp hơn, hệ kẹp ngoài vẫn có chỗ "
        "đứng trong những ứng dụng đòi hỏi phải di chuyển đoạn ống đo một cách dễ dàng, hoặc nơi không "
        "thể ngắt một quy trình đang chạy. Các đầu dò được gắn trên một thiết bị hiệu chuẩn và được "
        "ghép âm với thành ống bằng mỡ và/hoặc epoxy."))
    b.append(h4("Kênh hở và các ứng dụng đặc biệt", "Open Channels and Special Applications"))
    b.append(p(
        "Trong kênh hở, các đầu dò thường được gắn lên hoặc chôn vào thành kênh. Hình 28.48 cho một ví "
        "dụ về cảm biến đo kênh hở. Phần tử gốm áp điện được đặt trên một quả cầu để có nhiều khả năng "
        "bố trí. Đôi khi các đoạn ống đang tồn tại được bọc hoàn toàn bằng đá hoặc bê tông. Trong những "
        "trường hợp này, có thể cố định các đầu dò trong thành ống dẫn. Với đường kính nhỏ, phải tính "
        "đến phần nhô của đầu dò vào trong đoạn ống đo."))
    b.append(fig(48, F.fig(48), "vi"))

    # ---------------------------------------------------------------- closed conduits
    b.append(h4("Đo lưu lượng trong ống kín", "Measurement of Flow in Closed Conduits"))
    b.append(p(
        "Vấn đề quan trọng nhất khi dùng lưu lượng kế siêu âm là hiểu được ảnh hưởng của prôfin vận tốc "
        "của chất lưu chảy trong ống. Prôfin dòng phụ thuộc vào chất lưu, số Reynolds Re, độ nhám tương "
        "đối và hình dạng của ống, các nhiễu động phía thượng lưu và hạ lưu, cùng các yếu tố khác. Lưu "
        "lượng kế thời gian truyền cho một vận tốc dòng trung bình v̄ dọc theo đường âm. Do đó lưu "
        "lượng âm <i>Q</i><sub>ADM</sub> được tính qua <i>Q</i> = v̄<i>A</i>, với v̄ là vận tốc dòng "
        "trung bình theo diện tích và <i>A</i> là mặt cắt của ống. Để có được vận tốc trung bình theo "
        "diện tích v̄, vận tốc đo được v̄<sub>a</sub> phải được hiệu chỉnh bằng một hệ số thuỷ lực "
        "<i>k</i><sub>h</sub> phụ thuộc vào kiểu ống và số Reynolds. Để đạt hiệu năng và độ chính xác "
        "tối đa của lưu lượng kế siêu âm, phải tuân thủ các yêu cầu về đoạn ống thẳng đủ dài như minh "
        "hoạ cho một số ví dụ trên Hình 28.49. Làm được như vậy thì có thể đạt độ chính xác điển hình "
        "1 % giá trị đọc hoặc tốt hơn, ngay cả khi dùng hệ đo một đường. Đoạn ống thẳng bị rút ngắn "
        "dẫn tới độ chính xác giảm. Trong một số ứng dụng, độ chính xác giảm này là chấp nhận được; "
        "nếu không thì phải lắp một lưu lượng kế siêu âm nhiều đường. Những lưu lượng kế này lấy trung "
        "bình các thành phần dòng gây sai số khác nhau. Có thể đạt độ chính xác 0,5 % giá trị đọc ngay "
        "cả trong điều kiện không lý tưởng hoặc đoạn ống thẳng không đủ. Hình 28.50 cho bốn ví dụ về "
        "cách bố trí đường âm có thể có trong một ống kín."))
    b.append(note(
        "Bản gốc dẫn “Figure 28.50” cho bốn cách bố trí đường âm, nhưng bốn cách bố trí đó là Hình "
        "28.51; Hình 28.50 là đồ thị hệ số <i>k</i><sub>h</sub> theo số Reynolds. Câu sau trong bản gốc "
        "cũng dẫn đúng “Figure 28.51”. Bản dịch giữ nguyên nội dung và ghi rõ chỗ nhầm này."))
    b.append(fig(49, F.fig(49), "vi"))

    b.append(h4("Một đường với mặt cắt tròn và chữ nhật",
                "Single Path with Circular and Rectangular Cross-sections"))
    b.append(p("Số Reynolds Re được cho bởi:"))
    b.append(eq("Re = (v̄ · <i>D</i>) / ν", "28.69"))
    b.append(defs([
        ("v̄", "Vận tốc trung bình trên mặt cắt [m s<sup>−1</sup>]"),
        ("<i>D</i>", "Đường kính ống"),
        ("ν", "Độ nhớt động học phụ thuộc nhiệt độ"),
    ]))
    b.append(p(
        "Trong đường ống thông thường, dòng chảy tầng tồn tại chừng nào số Reynolds còn dưới khoảng "
        "2600. Hình dạng prôfin vận tốc tuân theo một parabol, và vận tốc tại một điểm trên prôfin "
        "được cho bởi:"))
    b.append(eq("<i>v</i>(<i>r</i>) = <i>v</i><sub>max</sub> [1 − (<i>r</i>/<i>R</i>)<sup>2</sup>]",
                "28.70"))
    b.append(defs([
        ("<i>r</i>", "Bán kính biến thiên"),
        ("<i>R</i>", "Bán kính ống"),
    ]))
    b.append(p(
        "Giữa số Reynolds 2600 và 4000 xuất hiện chế độ chảy quá độ, với sự chuyển đổi liên tục giữa "
        "prôfin tầng và prôfin rối. Khi số Reynolds vượt 4000, prôfin vận tốc bước vào chế độ chảy "
        "rối. Nikuradse [6] đã chỉ ra rằng prôfin vận tốc rối của một dòng đối xứng trục trong ống "
        "kín, không có xoáy, có các đoạn vào và ra đủ dài và thành nhẵn, có thể biểu diễn bằng:"))
    b.append(eq("<i>v</i>(<i>r</i>) = <i>v</i><sub>max</sub> [(<i>R</i> − <i>r</i>)/<i>R</i>]"
                "<sup>1/<i>n</i></sup>", "28.71"))
    b.append(p(
        "trong đó, theo Nikuradse, <i>n</i> là số mũ phụ thuộc số Reynolds, cho bởi:"))
    b.append(eq("<i>n</i> = 1 / (0,2525 − 0,0229 × log(Re))", "28.72"))
    b.append(p("Với định nghĩa hệ số hiệu chỉnh thuỷ lực <i>k</i><sub>h</sub> cho bởi:"))
    b.append(eq("<i>k</i><sub>h</sub> = v̄ / v̄<sub>a</sub>", "28.73"))
    b.append(defs([
        ("v̄", "Vận tốc trung bình trên mặt cắt"),
        ("v̄<sub>a</sub>", "Vận tốc trung bình dọc đường âm"),
    ]))
    b.append(p("và tích phân trên mặt cắt theo:"))
    b.append(eq("<i>k</i><sub>h</sub> = [ (1/<i>A</i>) ∫<sub>0</sub><sup>R</sup> "
                "∫<sub>0</sub><sup>2π</sup> <i>v</i>(<i>r</i>) <i>r</i> d<i>r</i> dθ ] / "
                "[ (1/2<i>R</i>) ∫<sub>−R</sub><sup>R</sup> <i>v</i>(<i>r</i>) d<i>r</i> ]", "28.74"))
    b.append(p(
        "ta được với dòng chảy tầng một hệ số hiệu chỉnh thuỷ lực <i>k</i><sub>h</sub> = 0,75."))
    b.append(p(
        "Trong chế độ chảy rối, theo Nikuradse [6], hệ số hiệu chỉnh thuỷ lực <i>k</i><sub>h</sub>, "
        "phụ thuộc số Reynolds Re, có thể biểu diễn bằng:"))
    b.append(eq("<i>k</i><sub>h</sub> = 1 / (1,125 − 0,011 × log(Re))", "28.75"))
    b.append(p("cho mặt cắt tròn, và"))
    b.append(eq("<i>k</i><sub>h</sub> = 0,79 + 0,02 × log(Re)", "28.76"))
    b.append(p("cho mặt cắt chữ nhật."))
    b.append(fig(50, F.fig(50), "vi"))
    b.append(p(
        "Trong các ứng dụng thuỷ điện, số Reynolds Re thường vượt giá trị 4000. Hình 28.50 cho thấy sự "
        "phụ thuộc của hệ số <i>k</i><sub>h</sub> trong ống kín có mặt cắt tròn vào số Reynolds. Số "
        "Reynolds không chỉ thay đổi giá trị theo vận tốc dòng v̄ với một đường kính <i>D</i> cho "
        "trước, mà còn phụ thuộc mạnh vào độ nhớt động học phụ thuộc nhiệt độ ν(<i>T</i>). Không tính "
        "đến giá trị đúng của Re có thể dễ dàng dẫn tới sai số của hệ số <i>k</i><sub>h</sub> và do đó "
        "của lưu lượng <i>Q</i> vào cỡ 2 % đến 3 %. Các lưu lượng kế thời gian truyền hiện đại có vi xử "
        "lý cập nhật hệ số <i>k</i><sub>h</sub> với tốc độ 4 lần một giây và bằng cách đo nhiệt độ "
        "<i>T</i> của chất lưu với cùng tốc độ đó. Kết quả là thu được một hệ số <i>k</i><sub>h</sub> "
        "đúng, và do đó một lưu lượng <i>Q</i> đã được bù theo nhiệt độ và số Reynolds."))

    b.append(h4("Tích phân nhiều đường trong mặt cắt tròn",
                "Multipath Integration in Circular Cross-sections"))
    b.append(p(
        "Tuy nhiên, trên thực tế không phải lúc nào cũng giữ được các yêu cầu về đoạn ống thẳng như đã "
        "định nghĩa trên Hình 28.49. Ngoài ra, sai số do dòng xiên xuất hiện khi các thành phần vận tốc "
        "không dọc trục trong ống làm thay đổi thời gian truyền của một xung giữa các cảm biến. Vận "
        "tốc không dọc trục do những nhiễu động trong ống kín như khuỷu, dòng vào không đối xứng, và "
        "các gián đoạn trên thành ống hoặc máy bơm gây ra. Việc loại bỏ độ nhạy của lưu lượng kế âm với "
        "phân bố vận tốc bằng cách tăng số đường âm <i>n</i> đã trở thành một thực tiễn được chấp "
        "nhận. Các đường bổ sung không chỉ làm giảm đáng kể sai số do phân bố vận tốc, mà còn giảm sai "
        "số tích phân số cũng như sai số do lệch đường. Điều này cho thấy rằng với những phép đo chính "
        "xác mà sai số vài phần mười phần trăm là đáng kể, chi phí lắp thêm cảm biến cho một bố trí bốn "
        "đường theo Hình 28.51 có thể là hợp lý. Trong một hệ đo nhiều đường, theo phương pháp tích "
        "phân mô tả trong IEC 41, Phụ lục J1 [7], lưu lượng <i>Q</i><sub>ADM</sub> có thể biểu diễn "
        "bằng:"))
    b.append(eq("<i>Q</i><sub>ADM</sub> = <i>k</i> (<i>D</i>/2) Σ<sub><i>i</i>=1</sub><sup><i>n</i></sup> "
                "v̄<sub>a<i>i</i></sub> <i>W</i><sub><i>i</i></sub> <i>L</i><sub>w<i>i</i></sub> "
                "sin φ<sub><i>i</i></sub>", "28.77"))
    b.append(defs([
        ("v̄<sub>a<i>i</i></sub>", "Vận tốc dọc đường âm thứ <i>i</i>"),
        ("<i>W</i><sub><i>i</i></sub>", "Trọng số tương ứng"),
        ("<i>L</i><sub>w<i>i</i></sub>", "Chiều dài đường tương ứng"),
        ("φ<sub><i>i</i></sub>", "Góc của đường tương ứng"),
    ]))
    b.append(fig(51, F.fig(51), "vi"))
    b.append(p(
        "Phương pháp mô tả trong IEC 41 đòi hỏi định vị đầu dò rất chính xác, do các trọng số "
        "<i>W</i><sub><i>i</i></sub> thu được bằng phân tích toán học chỉ đúng khi các cảm biến được "
        "đặt đúng vị trí. Việc lệch các đường âm kết hợp với trọng số cố định có thể dẫn tới sai số "
        "đáng kể."))
    b.append(note(
        "Bản gốc dẫn “IEC 41, Appendix J1 [7]”, nhưng trong danh mục tài liệu tham khảo thì [7] là "
        "Brand (1987) còn IEC 41 là [8]. Bản dịch giữ nguyên số [7] như đã in."))

    # ---------------------------------------------------------------- open channels
    b.append(h3("Đo lưu lượng trong kênh hở", "Measurement of Flow in Open Channels"))
    b.append(p(
        "Đo lưu lượng kênh hở được dùng trong nhiều ứng dụng, gồm mạng cấp nước, thuỷ văn, phân phối "
        "nước cho thuỷ lợi và nông nghiệp, trạm xử lý nước thải... Việc đo lưu lượng trên sông và kênh "
        "hở thường được tính bằng một đường quan hệ mực nước – lưu lượng, dùng để chuyển các bản ghi "
        "mức nước thành lưu lượng. Đường quan hệ này được xây dựng từ một tập hợp các phép đo lưu lượng "
        "và mực nước trên dòng, và phải được kiểm tra định kỳ để bảo đảm quan hệ mực nước – lưu lượng "
        "vẫn không đổi; nhiều hiện tượng có thể làm đường quan hệ thay đổi, khiến cùng một mực nước ghi "
        "được lại cho một lưu lượng khác. Đó là trường hợp các kênh hở dưới điều kiện thuỷ lực thay "
        "đổi, ví dụ do hiệu ứng nước dềnh, do cửa van, và nơi không tồn tại một quan hệ mực nước – lưu "
        "lượng đơn trị. Trong bối cảnh đó, việc ứng dụng lưu lượng kế âm học là cực kỳ thú vị và hiện "
        "đang rất thành công trong quản lý nước. Thực vậy, trong khi các giá trị lưu lượng khác nhau có "
        "thể ứng với một mực nước cho trước tuỳ theo đặc tính thuỷ lực, thì giữa vận tốc lan truyền "
        "sóng âm trong một chất lưu đang chảy và chính chất lưu đang chảy luôn có một quan hệ đơn trị."))
    b.append(p(
        "Bằng kỹ thuật siêu âm, lưu lượng qua kênh hở có thể xác định được bằng công nghệ một đường và "
        "nhiều đường. Trong cấu hình một đường, phải đặc biệt chú ý xác định phân bố vận tốc theo "
        "phương đứng (Hình 28.52) để đạt độ chính xác tốt bằng một số đọc vận tốc “đường” duy nhất "
        "v̄<sub>a<i>z</i></sub> ở độ cao <i>z</i> trên đáy. Ngược lại, trong cấu hình nhiều đường, "
        "prôfin vận tốc đường trung bình được mô tả tốt. Trong trường hợp này, phải đặc biệt chú ý tới "
        "phương pháp tích phân dùng để xác định lưu lượng từ các số đọc trên đường âm."))
    b.append(fig(52, F.fig(52), "vi"))

    b.append(h4("Một đường", "Single Path"))
    b.append(p(
        "Trong phép đo một đường, dùng phương pháp diện tích – vận tốc, lưu lượng <i>Q</i> được tính "
        "qua <i>Q</i> = v̄<i>A</i>, với v̄ (m s<sup>−1</sup>) là vận tốc dòng trung bình theo diện tích "
        "và <i>A</i> là mặt cắt. Để có vận tốc trung bình v̄ trên toàn mặt cắt, vận tốc đường trung "
        "bình v̄<sub>a<i>z</i></sub>, do lưu lượng kế âm đo ở một độ sâu <i>z</i> cho trước, phải được "
        "hiệu chỉnh bằng một hệ số hiệu chỉnh thuỷ lực không thứ nguyên <i>k</i><sub>h</sub> theo hệ "
        "thức v̄ = <i>k</i><sub>h</sub> v̄<sub>a<i>z</i></sub>. Nói chung, hệ số <i>k</i><sub>h</sub> "
        "phản ánh ảnh hưởng của prôfin vận tốc theo phương ngang và phương đứng. Nó chủ yếu phụ thuộc "
        "mực nước, hình dạng mặt cắt và độ nhám biên. Prôfin vận tốc đứng trung bình có thể được mô tả "
        "bằng quy luật logarit quen thuộc (Hình 28.53), cho bởi [8]."))
    b.append(eq("v̄(<i>z</i>) = (v̄<sub>*</sub> / <i>k</i>) ln(<i>z</i>/<i>z</i><sub>0</sub>)", "28.78"))
    b.append(defs([
        ("v̄(<i>z</i>)", "Vận tốc dòng trung bình ở độ cao <i>z</i> trên đáy"),
        ("<i>k</i>", "Hằng số rối của von Kármán"),
        ("<i>z</i>", "Khoảng cách trên đáy"),
        ("v̄<sub>*</sub>", "Vận tốc ma sát"),
        ("<i>z</i><sub>0</sub>", "Hằng số tích phân, phụ thuộc độ nhám của biên"),
    ]))
    b.append(fig(53, F.fig(53), "vi"))
    b.append(p(
        "Khi mặt biên thuỷ lực nhám, người ta thấy <i>z</i><sub>0</sub> chỉ phụ thuộc chiều cao nhám "
        "<i>k</i><sub>s</sub> theo hệ thức <i>z</i><sub>0</sub> = <i>k</i><sub>s</sub>/30. Tích phân "
        "Phương trình 28.78 trên toàn bộ chiều cao nước <i>h</i> và thay v̄, ta được phương trình sau:"))
    b.append(eq("<i>k</i><sub>h</sub> = [ln(<i>h</i>/<i>k</i><sub>s</sub>) − 1] / "
                "ln(<i>z</i>/<i>k</i><sub>s</sub>)", "28.79"))
    b.append(p("với giả thiết <i>z</i><sub>0</sub> không đáng kể so với <i>h</i>."))
    b.append(p(
        "Trên Hình 28.54, hệ số <i>k</i><sub>h</sub> theo quy luật logarit được biểu diễn cho hai độ "
        "nhám đáy khác nhau. Tuy nhiên, trong nhiều ứng dụng thực tế, việc xác định đúng giá trị của "
        "<i>k</i><sub>s</sub> thường khó. Vì lý do đó, một mô hình <i>k</i><sub>h</sub> khác đã được "
        "xây dựng trên cơ sở quy luật luỹ thừa [9, 10]. Trong công thức này, số mũ 1/<i>m</i> không "
        "còn là hằng số mà phụ thuộc độ nhám và bán kính thuỷ lực, để tính đến ảnh hưởng của hình "
        "dạng kênh. Prôfin vận tốc đứng trung bình v̄(<i>z</i>), theo quy luật luỹ thừa, có thể biểu "
        "diễn bằng công thức sau (Hình 28.55):"))
    b.append(fig(54, F.fig(54), "vi"))
    b.append(eq("v̄(<i>z</i>) = v̄<sub>s</sub> (<i>z</i>/<i>h</i>)<sup>1/<i>m</i></sup>", "28.80"))
    b.append(defs([
        ("<i>h</i>", "Mực nước hiện thời"),
        ("v̄<sub>s</sub>", "Vận tốc đường trung bình tại mặt tự do (giá trị cực đại)"),
        ("1/<i>m</i>", "Số mũ"),
    ]))
    b.append(fig(55, F.fig(55), "vi"))
    b.append(p(
        "Từ việc tích phân Phương trình 28.80 trên toàn bộ chiều sâu nước, ta thu được biểu thức sau "
        "cho hệ số <i>k</i><sub>h</sub>:"))
    b.append(eq("<i>k</i><sub>h</sub> = [<i>m</i>/(<i>m</i> + 1)] "
                "(<i>h</i>/<i>z</i>)<sup>1/<i>m</i></sup>", "28.81"))
    b.append(p(
        "Giá trị của <i>m</i>, phụ thuộc độ nhám, có thể biểu diễn bằng hệ số ma sát không thứ nguyên "
        "<i>f</i> của công thức Darcy–Weisbach [8], theo:"))
    b.append(eq("<i>m</i> = <i>k</i> √(8/<i>f</i>)", "28.82"))
    b.append(p(
        "trong đó <i>k</i> là hằng số von Kármán, biến thiên từ 0,2 đến 0,4. <i>k</i> phụ thuộc tải "
        "lượng lơ lửng (giá trị thấp khi độ đục cao), hoặc có thể biểu diễn bằng công thức Manning theo "
        "hệ thức [11]:"))
    b.append(eq("<i>m</i> = (<i>k</i>/√<i>g</i>) <i>R</i><sub>h</sub><sup>1/6</sup> / <i>n</i>", "28.83"))
    b.append(defs([
        ("<i>g</i>", "Gia tốc trọng trường"),
        ("<i>n</i>", "Hệ số nhám Manning"),
        ("<i>R</i><sub>h</sub>", "Bán kính thuỷ lực"),
    ]))
    b.append(fig(56, F.fig(56), "vi"))
    b.append(p(
        "Trên Hình 28.56, hệ số hiệu chỉnh được biểu diễn cho mặt nhẵn và mặt nhám. Nhờ hệ thức này, "
        "việc áp dụng ngoài hiện trường trở nên dễ hơn do sự quen thuộc rộng rãi với công thức Manning "
        "trong tính toán dòng kênh hở, bởi hình thức đơn giản, tính linh hoạt cao và kết quả thoả đáng "
        "của nó."))

    b.append(h4("Nhiều đường", "Multipath"))
    b.append(p(
        "Các phương trình trên về prôfin vận tốc đứng trung bình trong kênh hở dự đoán rằng vận tốc "
        "trung bình cực đại xuất hiện tại mặt tự do. Tuy nhiên, các phép đo ngoài hiện trường và trong "
        "phòng thí nghiệm chứng minh rằng vận tốc trung bình cực đại xuất hiện dưới mặt tự do, phụ "
        "thuộc mạnh vào tỷ số <i>B</i>/<i>h</i>, với <i>B</i> là chiều rộng kênh. Những quan sát này "
        "cho thấy một quy luật phân bố vận tốc một chiều không phải lúc nào cũng mô tả đầy đủ prôfin "
        "dòng trong kênh hở. Vì vậy, để giảm bất định trong mô tả prôfin vận tốc và đạt độ chính xác "
        "cao ngay cả trong điều kiện thuỷ lực bất lợi, phải dùng một cấu hình nhiều đường."))
    b.append(p(
        "Trong phép đo nhiều đường, dùng “phương pháp mặt cắt trung bình”, vận tốc dòng được đo ở nhiều "
        "mức giữa mặt tự do và đáy kênh (Hình 28.57). Tổng lưu lượng <i>Q</i><sub>ADM</sub> được thực "
        "hiện theo hệ thức [12]:"))
    b.append(eq("<i>Q</i><sub>ADM</sub> = <i>Q</i><sub>b</sub> + <i>Q</i><sub>t</sub> + "
                "Σ<sub><i>i</i>=1</sub><sup><i>n</i></sup> [ (v̄<sub>a<i>i</i></sub> + "
                "v̄<sub>a<i>i</i>+1</sub>)/2 · (<i>A</i>(<i>z</i><sub><i>i</i>+1</sub>) − "
                "<i>A</i>(<i>z</i><sub><i>i</i></sub>)) ]", "28.84"))
    b.append(defs([
        ("<i>Q</i><sub>b</sub>", "Lưu lượng trong mặt cắt đáy, với vận tốc đáy thu được từ vận tốc "
                                  "đường thấp nhất sau khi hiệu chỉnh ma sát đáy"),
        ("<i>Q</i><sub>t</sub>", "Lưu lượng tại mặt cắt hoạt động cao nhất, với vận tốc "
                                  "<i>v</i><sub>top</sub> nội suy từ prôfin vận tốc"),
        ("v̄<sub>a<i>i</i></sub>", "Vận tốc trung bình dọc đường âm thứ <i>i</i>"),
        ("<i>A</i>(<i>z</i><sub><i>i</i></sub>)", "Mặt cắt phía dưới đường thứ <i>i</i>"),
    ]))
    b.append(fig(57, F.fig(57), "vi"))
    b.append(p(
        "Các lưu lượng kế siêu âm điều khiển bằng vi xử lý hiện đại có thể đáp ứng cả phép đo một "
        "đường lẫn nhiều đường trong kênh hở, dùng quy luật logarit hoặc quy luật luỹ thừa cho phép đo "
        "một đường. Ngoài ra, các hệ thống mô-đun hoàn toàn hiện đại có thể dùng phần lớn thiết bị cho "
        "việc đo cả trong kênh hở lẫn trong ống kín."))

    # ---------------------------------------------------------------- application
    b.append(h3("Ứng dụng: phát hiện rò rỉ ống áp lực có tháp điều áp",
                "Application: Penstock Leak Detection with Surge Chambers"))
    b.append(p(
        "Phát hiện rò rỉ ống áp lực là một ứng dụng điển hình của lưu lượng kế âm học [13]. Nó được "
        "dùng để nhận biết ngay lập tức vỡ ống và tổn thất do rò rỉ trong ống áp lực. Hai lưu lượng kế "
        "được lắp ở hai đầu đối diện của ống áp lực: một để đo <i>Q</i><sub>up</sub> càng gần cửa nhận "
        "nước càng tốt, cái kia để đo <i>Q</i><sub>down</sub> tại cửa vào nhà máy. Trong cách mô tả "
        "này, lưu lượng thượng lưu được so với lưu lượng hạ lưu và hiệu lưu lượng Δ<i>Q</i> = "
        "<i>Q</i><sub>up</sub> − <i>Q</i><sub>down</sub> được tính và giám sát. Nếu hiệu Δ<i>Q</i> vượt "
        "một ngưỡng cho trước, hệ thống phát cảnh báo hoặc đưa ra tiếp điểm đóng van."))
    b.append(p(
        "Trong các ứng dụng thuỷ điện, một vấn đề khác nảy sinh do có tháp điều áp (Hình 28.58). Kết "
        "cấu thuỷ lực này gây dao động khối lượng do tải tuabin thay đổi. Cho tới nay, nếu trong ống "
        "áp lực có một tháp điều áp thì có hai khả năng. Một là chia ống áp lực thành hai phần: một "
        "trước tháp điều áp, một sau nó, và bảo vệ chúng riêng rẽ. Giải pháp này đắt và rất thường "
        "không thực tế, vì tháp điều áp được xây trong đá và không thể tiếp cận. Hai là xây dựng một "
        "thứ giống “thuật toán phát hiện rò rỉ”, bao gồm cả hành vi dao động của ống áp lực. Tuy nhiên, "
        "một hệ như vậy cần nhiều thử nghiệm hiện trường và kiến thức để đặt chính xác tần số cộng "
        "hưởng, hệ số tắt dần và các ngưỡng. Công nghệ mới nhất trong lưu lượng kế siêu âm, kết hợp "
        "với các cảm biến mực nước chính xác, có thể đưa ra một giải pháp cho vấn đề này. Bằng cách áp "
        "dụng công thức:"))
    b.append(eq("Δ<i>Q</i> = <i>Q</i><sub>up</sub> − <i>Q</i><sub>down</sub> − "
                "Δ<i>V</i><sub>chamber</sub> / Δ<i>t</i>", "28.85"))
    b.append(p(
        "các thay đổi thể tích của tháp điều áp do dao động khối lượng được tính đến, dẫn tới hành vi "
        "tốt hơn và thực tế hơn của việc phát hiện rò rỉ ống áp lực khi có tháp điều áp."))
    b.append(fig(58, F.fig(58), "vi"))

    # ---------------------------------------------------------------- manufacturers
    b.append(h3("Thiết bị và nhà chế tạo/nhà phân phối",
                "Instrumentation and Manufacturers/Distributors"))
    b.append(p(
        "Bảng 28.12 cho một cái nhìn tổng quan về một số công ty chế tạo và phân phối lưu lượng kế thời "
        "gian truyền. Giá lưu lượng kế thời gian truyền có dải rất rộng do tính đa dạng của các ứng "
        "dụng khác nhau, và vì vậy khó liệt kê chính xác. Nói chung, lưu lượng kế siêu âm hiếm khi được "
        "bán như một thiết bị “đóng gói sẵn”. Vì lý do đó, giá của một đoạn ống đo, kể cả lắp đặt, dao "
        "động từ vài nghìn đô la Mỹ tới gần 100 000 đô la Mỹ."))
    b.append(_t2812("vi"))

    # ---------------------------------------------------------------- references
    b.append(h3("Tài liệu tham khảo", "References"))
    b.append(wl([
        "1. M. Barmettler and P. Gruber, Anwendung von Oversampling-Verfahren zur Erhöhung der "
        "Auflösung digital erfasster Signale, <i>Technisches Messen</i>, Oldenbourg Verlag, 1992.",
        "2. D. Hoppe, Kombinierte Zählung und Abstandsbestimmung von Impulssignalen, <i>Technisches "
        "Messen</i>, Oldenbourg Verlag, 10, 1991.",
        "3. R. Krimholtz, D. Leedom, and G. Matthaei, New equivalent circuits for elementary "
        "piezoelectric transducers, <i>Electronics Lett.</i>, 6, 398, 1970.",
        "4. P. D. Edmonds, <i>Methods of Experimental Physics, Ultrasonics</i>, New York: Academic "
        "Press, 1981.",
        "5. D. W. Spitzer, <i>Flow Measurement, Practical Guides for Measurement and Control</i>, "
        "Research Triangle Park, NC: Instrument Society of America, 1991.",
        "6. J. Nikuradse, Gesetzmässigkeiten der turbulenten Strömung in glatten Rohren, VDI Verlag "
        "GmbH, 1932.",
        "7. F. L. Brand, Akustische Verfahren zur Durchflussmessung, <i>Messen, Prüfen "
        "Automatisieren</i>, April 1987.",
        "8. International Standard IEC 41, 3rd ed., 1991.",
        "9. R. H. French, <i>Open Channel Hydraulics</i>, New York: McGraw-Hill, 1985, 30.",
        "10. Chen-Iung Chen, <i>J. Hydraulic Eng.</i>, 379, 117, 1990.",
        "11. M. F. Karim and J. F. Kennedy, <i>J. Hydraulic Eng.</i>, 162, 113, 1987.",
        "12. G. Grego, M. Baldin, et al., Application of an Acoustic Flowmeter for Discharge "
        "Measurement in the Po.",
        "13. G. Grego and M. Baldin, <i>Energia Elettrica</i>, 1, 52, 72, 1995.",
        "14. H. P. Vaterlaus and H. Gabler, A new intelligent ultrasonic flowmeter for hydropower "
        "applications, <i>Int. Water Power &amp; Dam Construction</i>, 1994.",
    ]))
    return "".join(b)


def sec_28_7_en():
    b = []
    b.append(h2("28.7 Ultrasonic Flowmeters", "Ultrasonic Flowmeters"))
    b.append(p("Hans-Peter Vaterlaus, Thomas Hossle, Paolo Giordano, and Christophe Bruttin."))
    b.append(p(
        "Flow is one of the most important physical parameters measured in industry and water "
        "management. There are various kinds of flowmeters available, depending on the requirements "
        "defined by the different market segments. For many years, differential pressure types of "
        "flowmeters have been the most widely applied flow measuring device for fluid flows in pipes "
        "and open channels that require accurate measurement at reasonable cost. In markets like "
        "waterpower, water supply, irrigation, etc., however, flow must be measured without any head "
        "losses or any pressure drop. This means no moving parts, no secondary devices, nor are any "
        "restrictions allowed. Two types of flowmeters presently fulfill this requirement: "
        "electromagnetic and ultrasonic flowmeters. Whereas ultrasonic flowmeters can be applied in "
        "nearly any kind of flowing liquid, electromagnetic flowmeters require a minimum electric "
        "conductivity of the liquid for operation. In addition, the cost of ultrasonic flowmeters is "
        "nearly independent of pipe diameter, whereas the price of electromagnetic flowmeters "
        "increases drastically with pipe diameter."))
    b.append(p("There are various types of ultrasonic flowmeters in use for discharge measurement:"))
    b.append(ol([
        "<b>Transit time:</b> this is today’s state-of-the-art technology and most widely used type, "
        "and will be discussed in this chapter section. This type of ultrasonic flowmeter makes use "
        "of the difference in the time for a sonic pulse to travel a fixed distance, first against "
        "the flow and then in the direction of flow. Transit time flowmeters are sensitive to "
        "suspended solids or air bubbles in the fluid.",
        "<b>Doppler:</b> this type is more popular and less expensive, but is not considered as "
        "accurate as the transit time flowmeter. It makes use of the Doppler frequency shift caused "
        "by sound reflected or scattered from suspensions in the flow path and is therefore more "
        "complementary than competitive to transit time flowmeters.",
        "<b>Cross-correlation:</b> two measuring sections are installed with a certain distance to "
        "each other. Both measure the energy absorption of the ultrasonic signal. A cross-correlation "
        "calculates the flow velocity.",
        "<b>Phase shift:</b> the phase position of the transmitting and receiving signal is measured "
        "in the direction of the flow and against it. The resulting phase shift angle is directly "
        "proportional to the flow velocity.",
        "<b>Drift:</b> the drift of an ultrasonic signal crossing the flow is measured by signal "
        "attenuation.",
    ]))

    # ---------------------------------------------------------------- transit time
    b.append(h3("Transit Time Flowmeter", "Transit Time Flowmeter"))
    b.append(h4("Principle of Operation", "Principle of Operation"))
    b.append(p(
        "The acoustic method of discharge measurement is based on the fact that the propagation "
        "velocity of an acoustic wave and the flow velocity are summed vectorially. This type of "
        "flowmeter measures the difference in transit times between two ultrasonic pulses transmitted "
        "upstream <i>t</i><sub>21</sub> and downstream <i>t</i><sub>12</sub> across the flow, as shown "
        "in Figure 28.43. If there are no transverse flow components in the conduit, these two "
        "transit times of acoustic pulses are given by:"))
    b.append(eq("t<sub>12</sub> = L<sub>w</sub> / (c + v̄<sub>a</sub> cos φ) &nbsp;&nbsp;and&nbsp;&nbsp; "
                "t<sub>21</sub> = L<sub>w</sub> / (c − v̄<sub>a</sub> cos φ)", "28.65"))
    b.append(defs([
        ("<i>L</i><sub>w</sub>", "Distance in the fluid between the two transducers"),
        ("<i>c</i>", "Speed of sound at the operating conditions"),
        ("φ", "Angle between the axis of the conduit and the acoustic path"),
        ("v̄<sub>a</sub>", "Axial flow velocity averaged along the distance <i>L</i><sub>w</sub>"),
    ]))
    b.append(fig(43, F.fig(43), "en"))
    b.append(p(
        "Since the transducers are generally used both as transmitters and receivers, the difference "
        "in travel time can be determined with the same pair of transducers. Thus, the mean axial "
        "velocity v̄<sub>a</sub> along the path is given by:"))
    b.append(eq("v̄<sub>a</sub> = (L<sub>w</sub> / 2 cos φ) (1/t<sub>21</sub> − 1/t<sub>12</sub>) = "
                "(D / 2 cos φ sin φ) (1/t<sub>21</sub> − 1/t<sub>12</sub>)", "28.66"))
    b.append(p(
        "The following example shows the demands on the time measurement technique: assuming a closed "
        "conduit with diameter <i>D</i> = 150 mm, angle φ = 60°, flow velocity v̄<sub>a</sub> = "
        "1 m s<sup>−1</sup>, and water temperature = 20 °C. This results in transit times of about "
        "116 µs and a time difference Δ<i>t</i> (Δ<i>t</i> = <i>t</i><sub>12</sub> − "
        "<i>t</i><sub>21</sub>) on the order of 78 ns. To achieve an accuracy of 1% of the "
        "corresponding full-scale range, Δ<i>t</i> has to be measured with a resolution of at least "
        "100 ps (1 × 10<sup>−10</sup> s)."))
    b.append(note(
        "The original prints “116 s” — plainly a dropped micro sign. With <i>D</i> = 150 mm, φ = 60° "
        "and <i>c</i> ≈ 1482 m s<sup>−1</sup> at 20 °C, the path <i>L</i><sub>w</sub> = <i>D</i>/sin φ "
        "≈ 0.173 m gives a transit time of 116.9 µs, and the printed Δ<i>t</i> of 78 ns is consistent "
        "only with microseconds. This edition reads 116 µs."))
    b.append(p(
        "Standard time measurement techniques are not able to meet such requirements so that special "
        "techniques must be applied. The advantage of the approach of state-of-the-art real digital "
        "measurement is to process the measured value directly by a microcomputer. The most difficult "
        "problem is to reach the required resolution and to cope with the jitter of digital logic "
        "gates. It is well known in the measurement technique that, if signals are sampled multiple "
        "times (<i>N</i><sub>n</sub>), the resolution increases with the number of samples "
        "(“oversampling”) [1]. This knowledge is not only applied for analog signals but also for "
        "transit time signals and is used in today’s technology of flowmeters. The propagation time "
        "<i>t</i> (<i>t</i><sub>12</sub>, <i>t</i><sub>21</sub>), depending on the distance the sound "
        "pulse has to travel through the fluid, is measured several times. Due to this fact, one "
        "obtains the following relation [2]:"))
    b.append(eq("<i>t</i> = (1/<i>N</i><sub>n</sub>) ∫<sub>0</sub><sup>τ</sup> (1/<i>f</i>) "
                "d<i>t</i>", "28.67"))
    b.append(p("where τ is integration time, and <i>f</i> is the frequency."))
    b.append(p(
        "According to the block diagram in Figure 28.44, two counters are used. One counter "
        "<i>N</i><sub>t</sub> is clocked during the measuring period by a stable quartz oscillator; "
        "the other one counts the number of samples <i>N</i><sub>n</sub>. The measurement stops after "
        "a certain period of some milliseconds and after having reached an integer value for "
        "<i>N</i><sub>n</sub>. The two counts of <i>N</i><sub>t</sub> and <i>N</i><sub>n</sub> are "
        "used to calculate propagation time <i>t</i><sub>12</sub> or <i>t</i><sub>21</sub> by "
        "dividing <i>N</i><sub>t</sub> by <i>N</i><sub>n</sub>. The resolution <i>r</i> is calculated "
        "by:"))
    b.append(eq("<i>r</i> = 1 / (<i>N</i><sub>n</sub> <i>f</i>)", "28.68"))
    b.append(fig(44, F.fig(44), "en"))
    b.append(p("Advantages of this measurement method for transit time flowmeters are:"))
    b.append(ol([
        "The resolution of the velocity measurement is constant (typical value 0.8 mm s<sup>−1</sup>).",
        "The accuracy depends almost only on the stability and the temperature coefficient of the "
        "quartz oscillator.",
        "Due to the multiple sampling, the jitter of the digital logic is averaged.",
    ]))

    # ---------------------------------------------------------------- sensors
    b.append(h4("Sensors", "Sensors"))
    b.append(p(
        "The transducer comprises the piezoelectric element that converts electric to acoustic energy "
        "and the basic structure for supporting the piezoceramic and providing electric connections. "
        "Transducer design entails choice of the piezoelectric element, determination of suitable "
        "dimensions and resonant frequency, and construction to withstand thermal and mechanical "
        "stress, see Figure 28.45. Considering the transmission line model [3, 4], the optimal "
        "electroacoustic response and the best matching of acoustic impedances <i>Z</i> = ρ<i>c</i> of "
        "the different transducer elements is important. Not only must suitable waveforms to be "
        "detected by the electronics be obtained, but also the energy loss must be minimized when "
        "crossing several interface boundaries. Because of the wide versatility of pipe sizes and flow "
        "conditions, there are a number of different sensor configurations for transit time "
        "flowmeters."))
    b.append(fig(45, F.fig(45), "en"))
    b.append(h4("Axial", "Axial"))
    b.append(p(
        "Due to the small differences in small diameter pipes, it is necessary to pass the sonic pulse "
        "directly down the axis of the pipe to ensure that there is sufficient path length. Figure "
        "28.46 shows an example of an axial sensor pipe section. The upper pipe size limit for this "
        "kind of sensor is about 0.075 m [5]."))
    b.append(fig(46, F.fig(46), "en"))
    b.append(h4("Radial", "Radial"))
    b.append(p(
        "Many manufacturers supply complete metering sections with built-in sonic transducers on "
        "either side of a spool section. Such sensors, shown in Figure 28.47, are generally called "
        "“radial” because of the transducer placement. A lower pipe size limit of radial type sensors "
        "is about 100 mm."))
    b.append(fig(47, F.fig(47), "en"))
    b.append(h4("Field Mounting", "Field Mounting"))
    b.append(p(
        "Radial-type sensors are often used to instrument an existing line, where it is desirable to "
        "make the installation without cutting out a section of the pipe. To meet this requirement, "
        "field-mountable transducers, cemented, drilled, or welded into an existing pipe section, can "
        "be used. Metering sections with diameters up to 13 m or more can be achieved in this way."))
    b.append(h4("Clamp-on", "Clamp-on"))
    b.append(p(
        "If there is a need for an installation where the pipe wall is not penetrated by the "
        "transducers, clamp-on systems are the right choice. Achieving a lower accuracy and being "
        "somewhat more complex to calibrate, clamp-on systems have their entitlement in applications "
        "where an easy movement of the metering section is an important requirement or where an "
        "existing process cannot be interrupted. The transducers are mounted on a calibration device "
        "and acoustically coupled to the pipe wall with grease and/or epoxy."))
    b.append(h4("Open Channels and Special Applications", "Open Channels and Special Applications"))
    b.append(p(
        "In open channels, the transducers are normally mounted on or dug into the channel walls. "
        "Figure 28.48 shows an example of an open-channel sensor. The piezoceramic element is placed "
        "on a sphere to achieve a wide range of mounting possibilities. Sometimes, existing pipe "
        "sections are completely enclosed with rock or concrete. In these cases, the transducers can "
        "be fixed in the wall of the conduit. For small diameters, the resulting protrusion of the "
        "transducers into the metering section must be taken into account."))
    b.append(fig(48, F.fig(48), "en"))

    # ---------------------------------------------------------------- closed conduits
    b.append(h4("Measurement of Flow in Closed Conduits", "Measurement of Flow in Closed Conduits"))
    b.append(p(
        "The most important issue in applying ultrasonic flowmeters is an understanding of the effects "
        "of the velocity profile of the flowing fluid within the conduit. The flow profile depends on "
        "the fluid, the Reynolds number Re, the relative roughness and shape of the conduit, upstream "
        "and downstream disturbances, and other factors. Transit time flowmeters give an average flow "
        "velocity v̄ along the sonic path. The acoustic flow rate <i>Q</i><sub>ADM</sub> is therefore "
        "calculated through <i>Q</i> = v̄<i>A</i>, with v̄ the area-averaged flow velocity and <i>A</i> "
        "the cross-section of the conduit. In order to obtain the area-averaged flow velocity v̄, the "
        "measured velocity v̄<sub>a</sub> must be corrected by a hydraulic coefficient "
        "<i>k</i><sub>h</sub> that depends on the type of the conduit and the Reynolds number. In "
        "order to achieve maximum performance and accuracy of ultrasonic flowmeters, one has to keep "
        "to sufficient straight run requirements as shown for some examples in Figure 28.49. By doing "
        "so, a typical accuracy of 1% of reading or better can be achieved, even when applying a "
        "single-path measurement system. Reduced straight runs lead to reduced accuracy. In some "
        "applications, this reduced accuracy is acceptable; if not, a multipath ultrasonic flowmeter "
        "must be installed. These flowmeters provide averaging of the various error-producing flow "
        "components. Accuracy of 0.5% of reading can be achieved even under nonideal conditions or "
        "insufficient straight runs. Figure 28.50 shows four examples of possible sonic path "
        "arrangements in a closed conduit."))
    b.append(note(
        "The original cites “Figure 28.50” for the four sonic path arrangements, but those "
        "arrangements are Figure 28.51; Figure 28.50 is the graph of the <i>k</i><sub>h</sub> factor "
        "against Reynolds number. A later sentence in the original cites “Figure 28.51” correctly. "
        "The text is reproduced as printed, with the discrepancy flagged here."))
    b.append(fig(49, F.fig(49), "en"))

    b.append(h4("Single Path with Circular and Rectangular Cross-sections",
                "Single Path with Circular and Rectangular Cross-sections"))
    b.append(p("The Reynolds number Re is given by:"))
    b.append(eq("Re = (v̄ · <i>D</i>) / ν", "28.69"))
    b.append(defs([
        ("v̄", "Mean velocity over the cross section [m s<sup>−1</sup>]"),
        ("<i>D</i>", "Pipe diameter"),
        ("ν", "Temperature-dependent kinematic viscosity"),
    ]))
    b.append(p(
        "In normal piping, a laminar flow exists as long as the Reynolds number is below about 2600. "
        "The shape of the velocity profile conforms to a parabola, and the velocity of a point on the "
        "profile is given by:"))
    b.append(eq("<i>v</i>(<i>r</i>) = <i>v</i><sub>max</sub> [1 − (<i>r</i>/<i>R</i>)<sup>2</sup>]",
                "28.70"))
    b.append(defs([
        ("<i>r</i>", "Variable radius"),
        ("<i>R</i>", "Pipe radius"),
    ]))
    b.append(p(
        "Between a Reynolds number Re of 2600 and 4000, the transitional flow regime with continuous "
        "switching between laminar and turbulent velocity profile comes into existence. When the "
        "Reynolds number exceeds 4000, the velocity profile enters the turbulent flow regime. "
        "Nikuradse [6] showed that the turbulent velocity profile of an axis-symmetrical flow in a "
        "closed conduit without swirl and sufficient inlet and outlet sections and smooth walls can "
        "be expressed by:"))
    b.append(eq("<i>v</i>(<i>r</i>) = <i>v</i><sub>max</sub> [(<i>R</i> − <i>r</i>)/<i>R</i>]"
                "<sup>1/<i>n</i></sup>", "28.71"))
    b.append(p("where, according to Nikuradse, <i>n</i> is a Reynolds number-dependent exponent given "
               "by:"))
    b.append(eq("<i>n</i> = 1 / (0.2525 − 0.0229 × log(Re))", "28.72"))
    b.append(p("With the definition of a hydraulic corrective coefficient <i>k</i><sub>h</sub> given "
               "by:"))
    b.append(eq("<i>k</i><sub>h</sub> = v̄ / v̄<sub>a</sub>", "28.73"))
    b.append(defs([
        ("v̄", "Mean velocity over the cross-section"),
        ("v̄<sub>a</sub>", "Mean velocity along the sonic path"),
    ]))
    b.append(p("and integrating over the cross-section according to:"))
    b.append(eq("<i>k</i><sub>h</sub> = [ (1/<i>A</i>) ∫<sub>0</sub><sup>R</sup> "
                "∫<sub>0</sub><sup>2π</sup> <i>v</i>(<i>r</i>) <i>r</i> d<i>r</i> dθ ] / "
                "[ (1/2<i>R</i>) ∫<sub>−R</sub><sup>R</sup> <i>v</i>(<i>r</i>) d<i>r</i> ]", "28.74"))
    b.append(p("one obtains for laminar flow a hydraulic corrective coefficient of "
               "<i>k</i><sub>h</sub> = 0.75."))
    b.append(p(
        "In the turbulent flow regime, according to Nikuradse [6], the hydraulic corrective "
        "coefficient <i>k</i><sub>h</sub>, dependent on the Reynolds number Re, can be expressed by:"))
    b.append(eq("<i>k</i><sub>h</sub> = 1 / (1.125 − 0.011 × log(Re))", "28.75"))
    b.append(p("for a circular cross-section, and"))
    b.append(eq("<i>k</i><sub>h</sub> = 0.79 + 0.02 × log(Re)", "28.76"))
    b.append(p("for a rectangular cross-section."))
    b.append(fig(50, F.fig(50), "en"))
    b.append(p(
        "In hydropower applications, the Reynolds number Re generally exceeds the value of 4000. "
        "Figure 28.50 shows the dependence of the <i>k</i><sub>h</sub> factor in closed conduits with "
        "circular cross-section on the Reynolds number. The Reynolds number not only changes its value "
        "as a function of the flow velocity v̄ for a given diameter <i>D</i>, but is also strongly "
        "dependent on the temperature-dependent kinematic viscosity ν(<i>T</i>). Not taking into "
        "account for correct value of Re can easily lead to errors of the <i>k</i><sub>h</sub> factor "
        "and thus to the flowrate <i>Q</i> on the order of 2% to 3%. Modern transit time meters with "
        "microprocessors update the <i>k</i><sub>h</sub> factor at a rate of 4 times a second and by "
        "measuring the temperature <i>T</i> of the fluid at the same rate. A correct "
        "<i>k</i><sub>h</sub> factor is obtained and hence a temperature and Reynolds "
        "number-compensated flow rate <i>Q</i>."))

    b.append(h4("Multipath Integration in Circular Cross-sections",
                "Multipath Integration in Circular Cross-sections"))
    b.append(p(
        "In reality, however, the straight run requirements as defined in Figure 28.49 cannot always "
        "be kept. In addition, cross flow errors occur when nonaxial components of velocity in a pipe "
        "alter the transit times of a pulse between the sensors. Nonaxial velocities are caused by "
        "such disturbances in closed conduits as bends, asymmetric intake flows, and discontinuities "
        "in the pipe wall or pumps. It has become accepted practice to eliminate the sensitivity of an "
        "acoustic flowmeter to velocity distributions by increasing the number of acoustic paths "
        "<i>n</i>. Additional paths not only decrease substantially the velocity distribution error, "
        "but also reduce the numerical integration error as well as errors due to path misalignment. "
        "This suggests that for accurate measurements for which a few tenths of a percent error are "
        "significant, the cost of installing more sensors for a four-path arrangement according to "
        "Figure 28.51 can be justified. In a multipath measurement system, according to the "
        "integration method described by IEC 41, Appendix J1 [7], the flowrate "
        "<i>Q</i><sub>ADM</sub> can be expressed by:"))
    b.append(eq("<i>Q</i><sub>ADM</sub> = <i>k</i> (<i>D</i>/2) Σ<sub><i>i</i>=1</sub><sup><i>n</i></sup> "
                "v̄<sub>a<i>i</i></sub> <i>W</i><sub><i>i</i></sub> <i>L</i><sub>w<i>i</i></sub> "
                "sin φ<sub><i>i</i></sub>", "28.77"))
    b.append(defs([
        ("v̄<sub>a<i>i</i></sub>", "Velocities along the acoustic path <i>i</i>"),
        ("<i>W</i><sub><i>i</i></sub>", "Corresponding weighting factor"),
        ("<i>L</i><sub>w<i>i</i></sub>", "Corresponding path length"),
        ("φ<sub><i>i</i></sub>", "Corresponding path angle"),
    ]))
    b.append(fig(51, F.fig(51), "en"))
    b.append(p(
        "The method described in IEC 41 needs a very accurate transducer positioning due to the fact "
        "that the weighting factors <i>W</i><sub><i>i</i></sub> obtained by mathematical analysis are "
        "only valid when the sensors are positioned at the correct locations. Misalignment of the "
        "acoustic paths in conjunction with fixed weights can lead to considerable errors."))
    b.append(note(
        "The original cites “IEC 41, Appendix J1 [7]”, but in the reference list [7] is Brand (1987) "
        "and IEC 41 is [8]. The printed number is kept here."))

    # ---------------------------------------------------------------- open channels
    b.append(h3("Measurement of Flow in Open Channels", "Measurement of Flow in Open Channels"))
    b.append(p(
        "Open-channel flow measurement is used in many applications, including water supply networks, "
        "hydrography, allocation of water for irrigation and agricultural purposes, sewage treatment "
        "plants, etc. Discharge measurements in rivers and open channels are often computed by means "
        "of a rating curve, used to convert records of water level readings into flow rates. The "
        "rating curve is developed using a set of discharge measurements and water level in the "
        "stream, and must be checked periodically to ensure that the level-discharge relationship has "
        "remained constant; many phenomena can cause the rating curve to change so that the same "
        "recorded water level produces a different discharge. This is the case of open channels under "
        "changeable hydraulic conditions due, for example, to backwater effects, gates, and where an "
        "univocal stage-discharge relationship does not exist. In this context, acoustic flowmeter "
        "application is extremely interesting and is currently experiencing wide success in water "
        "management. In fact, while different flow rate values can correspond to a given water level "
        "in relation to the hydraulic characteristics, there is always an univocal relationship "
        "between the acoustic wave propagation velocity in a flowing fluid and the flowing fluid "
        "itself."))
    b.append(p(
        "By means of the ultrasonic technique, discharge through open channels can be determined using "
        "single- and multipath technology. In a single-path configuration, particular attention must "
        "be paid to define the vertical velocity distribution (Figure 28.52) in order to achieve a "
        "good level of accuracy by a single “line” velocity reading v̄<sub>a<i>z</i></sub> at the "
        "distance <i>z</i> above the bottom. On the other hand, in a multipath configuration, the mean "
        "line velocity profile is well described. In this case, special attention must be paid to the "
        "integration method used to determine the flow rate from the acoustic path readings."))
    b.append(fig(52, F.fig(52), "en"))

    b.append(h4("Single Path", "Single Path"))
    b.append(p(
        "In single-path measurements, using the area-velocity method, the flow rate <i>Q</i> is "
        "calculated through <i>Q</i> = v̄<i>A</i> with v̄ (m s<sup>−1</sup>) the area-averaged flow "
        "velocity and <i>A</i> the cross-section. To obtain the velocity average v̄ over the entire "
        "cross-section, the mean path velocity v̄<sub>a<i>z</i></sub>, measured by the acoustic "
        "flowmeter at a given depth <i>z</i>, must be corrected by a dimensionless hydraulic corrective "
        "coefficient <i>k</i><sub>h</sub> according to the relation v̄ = <i>k</i><sub>h</sub> "
        "v̄<sub>a<i>z</i></sub>. In general, the coefficient <i>k</i><sub>h</sub> reflects the "
        "influence of the horizontal and vertical velocity profile. It mainly depends on the water "
        "level, on the cross-section shape, and on the boundary roughness. The mean vertical velocity "
        "profile can be described by the well-known logarithmic law (Figure 28.53) given by [8]."))
    b.append(eq("v̄(<i>z</i>) = (v̄<sub>*</sub> / <i>k</i>) ln(<i>z</i>/<i>z</i><sub>0</sub>)", "28.78"))
    b.append(defs([
        ("v̄(<i>z</i>)", "Mean flow velocity at a distance <i>z</i> above the bottom"),
        ("<i>k</i>", "Von Kármán’s turbulence constant"),
        ("<i>z</i>", "Distance above the bottom"),
        ("v̄<sub>*</sub>", "Shear velocity"),
        ("<i>z</i><sub>0</sub>", "Constant of integration, dependent on the boundary roughness"),
    ]))
    b.append(fig(53, F.fig(53), "en"))
    b.append(p(
        "When the boundary surface is hydraulically rough, <i>z</i><sub>0</sub> has been found to "
        "depend solely on the roughness height <i>k</i><sub>s</sub> according to the relation "
        "<i>z</i><sub>0</sub> = <i>k</i><sub>s</sub>/30. Integrating Equation 28.78 over the total "
        "water height <i>h</i> and substituting for v̄, the following equation is obtained:"))
    b.append(eq("<i>k</i><sub>h</sub> = [ln(<i>h</i>/<i>k</i><sub>s</sub>) − 1] / "
                "ln(<i>z</i>/<i>k</i><sub>s</sub>)", "28.79"))
    b.append(p("assuming <i>z</i><sub>0</sub> negligible with respect to <i>h</i>."))
    b.append(p(
        "In Figure 28.54, the logarithmic <i>k</i><sub>h</sub> factor is represented for two different "
        "bottom roughnesses. However, in many practical applications, it is often difficult to define "
        "correct values for <i>k</i><sub>s</sub>. For this reason, another <i>k</i><sub>h</sub> model "
        "has been developed on the basis of the power law [9, 10]. In this formula, the exponent "
        "1/<i>m</i> is not constant anymore, but depends on the roughness and the hydraulic radius to "
        "take into account the influence of the channel shape. The mean vertical velocity profile "
        "v̄(<i>z</i>), according to the power law, can be expressed by the following formula (Figure "
        "28.55):"))
    b.append(fig(54, F.fig(54), "en"))
    b.append(eq("v̄(<i>z</i>) = v̄<sub>s</sub> (<i>z</i>/<i>h</i>)<sup>1/<i>m</i></sup>", "28.80"))
    b.append(defs([
        ("<i>h</i>", "Current water level"),
        ("v̄<sub>s</sub>", "Mean line velocity at the free surface (maximum value)"),
        ("1/<i>m</i>", "Exponent"),
    ]))
    b.append(fig(55, F.fig(55), "en"))
    b.append(p(
        "From the integration of Equation 28.80 over the total water depth, one obtains the following "
        "expression for the <i>k</i><sub>h</sub> factor:"))
    b.append(eq("<i>k</i><sub>h</sub> = [<i>m</i>/(<i>m</i> + 1)] "
                "(<i>h</i>/<i>z</i>)<sup>1/<i>m</i></sup>", "28.81"))
    b.append(p(
        "The value of <i>m</i>, depending on the roughness, can be expressed using the adimensional "
        "friction factor <i>f</i> of the Darcy–Weisbach formula [8], according to:"))
    b.append(eq("<i>m</i> = <i>k</i> √(8/<i>f</i>)", "28.82"))
    b.append(p(
        "where <i>k</i> = Von Kármán constant, varying from 0.2 to 0.4. <i>k</i> depends on the "
        "suspended load (low values for high turbidity), or can be expressed using the Manning formula "
        "by the relation [11]:"))
    b.append(eq("<i>m</i> = (<i>k</i>/√<i>g</i>) <i>R</i><sub>h</sub><sup>1/6</sup> / <i>n</i>", "28.83"))
    b.append(defs([
        ("<i>g</i>", "Gravity acceleration"),
        ("<i>n</i>", "Manning’s roughness coefficient"),
        ("<i>R</i><sub>h</sub>", "Hydraulic radius"),
    ]))
    b.append(fig(56, F.fig(56), "en"))
    b.append(p(
        "In Figure 28.56, the corrective factor is represented for smooth and rough surfaces. By means "
        "of this relation, an easier field application has been obtained due to wide familiarity with "
        "the Manning formula in open-channel flow computation because of its simplicity of form, high "
        "versatility, and satisfactory results."))

    b.append(h4("Multipath", "Multipath"))
    b.append(p(
        "The foregoing equations for the mean vertical velocity profile in open channels predict that "
        "the maximum mean velocity occurs at the free surface. Field and laboratory measurements, "
        "however, demonstrate that the maximum mean velocity occurs below the free surface, strongly "
        "depending on the ratio <i>B</i>/<i>h</i>, with <i>B</i> being the channel width. These "
        "observations show that a one-dimensional velocity distribution law cannot always completely "
        "describe flow profiles in open channels. Therefore, to reduce uncertainties in velocity "
        "profile description and to achieve high accuracies even under unfavorable hydraulic "
        "conditions, a multipath configuration must be used."))
    b.append(p(
        "In multipath measurement, using the “mean section method,” the flow velocity is measured at "
        "several levels between the free surface and the channel bottom (Figure 28.57). The total "
        "discharge <i>Q</i><sub>ADM</sub> is performed by the relation [12]:"))
    b.append(eq("<i>Q</i><sub>ADM</sub> = <i>Q</i><sub>b</sub> + <i>Q</i><sub>t</sub> + "
                "Σ<sub><i>i</i>=1</sub><sup><i>n</i></sup> [ (v̄<sub>a<i>i</i></sub> + "
                "v̄<sub>a<i>i</i>+1</sub>)/2 · (<i>A</i>(<i>z</i><sub><i>i</i>+1</sub>) − "
                "<i>A</i>(<i>z</i><sub><i>i</i></sub>)) ]", "28.84"))
    b.append(defs([
        ("<i>Q</i><sub>b</sub>", "Flow rate in the bottom section with the bottom velocity obtained "
                                  "from the lowest path velocity by correction for bottom friction"),
        ("<i>Q</i><sub>t</sub>", "Flow rate at the highest active section with velocity "
                                  "<i>v</i><sub>top</sub>, interpolated from the velocity profile"),
        ("v̄<sub>a<i>i</i></sub>", "Mean velocity along the <i>i</i>th acoustic path"),
        ("<i>A</i>(<i>z</i><sub><i>i</i></sub>)", "Cross-section below the <i>i</i>th path"),
    ]))
    b.append(fig(57, F.fig(57), "en"))
    b.append(p(
        "Modern microprocessor-controlled ultrasonic flowmeters can cope with either single-path or "
        "multipath measurement in open channels, using the logarithmic or the power law for "
        "single-path measurement. In addition, up-to-date completely modular systems are able to use "
        "the major part of the equipment for measuring both in open channels and closed conduits."))

    # ---------------------------------------------------------------- application
    b.append(h3("Application: Penstock Leak Detection with Surge Chambers",
                "Application: Penstock Leak Detection with Surge Chambers"))
    b.append(p(
        "Penstock leak detection is a typical acoustic flowmeter application [13]. It is used for "
        "immediate recognition of pipe rupture and leak losses in penstocks. Two flowmeters are "
        "installed at opposite ends of the penstock: one for measuring <i>Q</i><sub>up</sub> as near "
        "as possible to the intake, the other for measuring <i>Q</i><sub>down</sub> at the powerhouse "
        "entrance. In this description, the upstream flow is compared to the downstream flow and the "
        "flow difference Δ<i>Q</i> = <i>Q</i><sub>up</sub> − <i>Q</i><sub>down</sub> is calculated and "
        "supervised. If the difference Δ<i>Q</i> exceeds a given threshold, the system enunciates "
        "alarms or valve closure contacts."))
    b.append(p(
        "In hydropower applications another problem arises due to the presence of surge chambers "
        "(Figure 28.58). This hydraulic structure causes mass oscillations due to load changes of the "
        "turbine. Up to now, if there was a surge tank in a penstock, one had two possibilities. On "
        "the one hand, one could divide the penstock into two parts: one before the surge chamber, one "
        "after it, and protect them separately. This solution is expensive and very often impractical "
        "because the surge chamber is built into the rock and inaccessible. On the other hand, one "
        "could develop something like a “leak detection algorithm,” which includes the oscillatory "
        "behavior of a penstock. Such a system, however, needs extensive field tests and the knowledge "
        "for exact settings of resonant frequency, damping factor, and thresholds. The latest "
        "technology in ultrasonic flowmeters, combined with accurate water level sensors, can offer a "
        "solution to this problem. By applying the formula:"))
    b.append(eq("Δ<i>Q</i> = <i>Q</i><sub>up</sub> − <i>Q</i><sub>down</sub> − "
                "Δ<i>V</i><sub>chamber</sub> / Δ<i>t</i>", "28.85"))
    b.append(p(
        "changes of the volume of the surge chamber due to mass oscillations are taken into account, "
        "leading to a better and more realistic behavior of penstock leak detection in the presence of "
        "surge tanks."))
    b.append(fig(58, F.fig(58), "en"))

    # ---------------------------------------------------------------- manufacturers
    b.append(h3("Instrumentation and Manufacturers/Distributors",
                "Instrumentation and Manufacturers/Distributors"))
    b.append(p(
        "Table 28.12 gives an overview of some companies manufacturing and distributing transit time "
        "flowmeters. Prices of transit time flowmeters have a very wide range due to the wide "
        "versatility of different applications and are therefore difficult to list accurately. "
        "Generally, ultrasonic flowmeters are seldom sold as a “prepacked” instrument. For this "
        "reason, the price for a metering section, including installation, varies from a few $1000 to "
        "nearly $100,000."))
    b.append(_t2812("en"))

    # ---------------------------------------------------------------- references
    b.append(h3("References", "References"))
    b.append(wl([
        "1. M. Barmettler and P. Gruber, Anwendung von Oversampling-Verfahren zur Erhöhung der "
        "Auflösung digital erfasster Signale, <i>Technisches Messen</i>, Oldenbourg Verlag, 1992.",
        "2. D. Hoppe, Kombinierte Zählung und Abstandsbestimmung von Impulssignalen, <i>Technisches "
        "Messen</i>, Oldenbourg Verlag, 10, 1991.",
        "3. R. Krimholtz, D. Leedom, and G. Matthaei, New equivalent circuits for elementary "
        "piezoelectric transducers, <i>Electronics Lett.</i>, 6, 398, 1970.",
        "4. P. D. Edmonds, <i>Methods of Experimental Physics, Ultrasonics</i>, New York: Academic "
        "Press, 1981.",
        "5. D. W. Spitzer, <i>Flow Measurement, Practical Guides for Measurement and Control</i>, "
        "Research Triangle Park, NC: Instrument Society of America, 1991.",
        "6. J. Nikuradse, Gesetzmässigkeiten der turbulenten Strömung in glatten Rohren, VDI Verlag "
        "GmbH, 1932.",
        "7. F. L. Brand, Akustische Verfahren zur Durchflussmessung, <i>Messen, Prüfen "
        "Automatisieren</i>, April 1987.",
        "8. International Standard IEC 41, 3rd ed., 1991.",
        "9. R. H. French, <i>Open Channel Hydraulics</i>, New York: McGraw-Hill, 1985, 30.",
        "10. Chen-Iung Chen, <i>J. Hydraulic Eng.</i>, 379, 117, 1990.",
        "11. M. F. Karim and J. F. Kennedy, <i>J. Hydraulic Eng.</i>, 162, 113, 1987.",
        "12. G. Grego, M. Baldin, et al., Application of an Acoustic Flowmeter for Discharge "
        "Measurement in the Po.",
        "13. G. Grego and M. Baldin, <i>Energia Elettrica</i>, 1, 52, 72, 1995.",
        "14. H. P. Vaterlaus and H. Gabler, A new intelligent ultrasonic flowmeter for hydropower "
        "applications, <i>Int. Water Power &amp; Dam Construction</i>, 1994.",
    ]))
    return "".join(b)


# ================================================================ build

SECTIONS_VI = [sec_28_1_vi, sec_28_2_vi, sec_28_3_vi, sec_28_4_vi, sec_28_5_vi, sec_28_6_vi,
               sec_28_7_vi]
SECTIONS_EN = [sec_28_1_en, sec_28_2_en, sec_28_3_en, sec_28_4_en, sec_28_5_en, sec_28_6_en,
               sec_28_7_en]


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
    meta = ("Chương 28 · theo Ch28.pdf (CRC Press, 1999) · đang dịch: 7/11 mục" if vi else
            "Chapter 28 · in progress: 7 of 11 sections")
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
