# -*- coding: utf-8 -*-
"""Handbook Chapter 94 — Electroluminescent Displays
(William A. Barrow, Planar Systems).

Writes the full Vietnamese translation and the English companion.
Run:  python build/reader_hb_ch94.py
"""
import os

import hb94fig as F
from reader_handbook import SLUG, head, header, footer
from chapter_nav import nav as chapter_nav

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSLUG = "ch94-electroluminescent-displays"
TITLE_EN = "Electroluminescent Displays"
TITLE_VI = "Hiển thị điện phát quang"
BYLINE = "William A. Barrow · Planar Systems"
BASE_EN = "/books/read/%s/" % SLUG
BASE_VI = "/vi/books/read/%s/" % SLUG


def fig(num, key, lang="vi"):
    svg, cap_vi, cap_en, _av, _ae = key
    return ('<figure class="figure" id="fig-94-%d">%s<figcaption class="figcap">%s</figcaption>'
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


def dt(term, definition):
    return p("<b>%s:</b> %s" % (term, definition))


def table(hd, rows, cap, cls=""):
    body = "".join("<tr>%s</tr>" % "".join("<td>%s</td>" % c for c in r) for r in rows)
    return ('<div class="table-wrap"><table class="tbl%s"><thead><tr>%s</tr></thead><tbody>%s'
            '</tbody></table></div><p style="font-size:.84rem;color:#888;font-style:italic">%s</p>'
            % (cls, "".join("<th>%s</th>" % h for h in hd), body, cap))


# ================================================================ EQUATIONS
# One shared dictionary so the Vietnamese and English pages cannot drift.
# The source prints these as ∫ with a subscripted limit and stacked fractions;
# they are re-set with slash fractions inside brackets, mathematics unchanged.
_EQ = {
    "94.1": ("<i>E</i><sub>P</sub> = ∫<sub>D</sub> <i>I</i>(<i>t</i>)"
             "<i>V</i>(<i>t</i>)&nbsp;d<i>t</i>"),
    "94.2": "η = π<i>LA</i>/<i>P</i>",
    "94.3": "<i>Q</i> = <i>C</i><sub>S</sub><i>V</i><sub>S</sub>",
    "94.4": "<i>E</i> = ∫<i>V</i>(<i>t</i>)&nbsp;d<i>Q</i>",
    "94.5": ("<i>Q</i><sub>P</sub>(<i>t</i>) = [(<i>C</i><sub>i</sub> + "
             "<i>C</i><sub>P</sub>)/<i>C</i><sub>i</sub>]<i>Q</i>(<i>t</i>) − "
             "<i>C</i><sub>P</sub><i>V</i>(<i>t</i>)"),
    "94.6": ("<i>F</i><sub>P</sub>(<i>t</i>) = (1/<i>d</i><sub>P</sub>)"
             "[<i>Q</i>(<i>t</i>)/<i>C</i><sub>i</sub> − <i>V</i>(<i>t</i>)]"),
}


def _eq(num):
    return _EQ[num]


# ================================================================ TABLES
# TABLE 94.1 — instrument types. The source leaves the type cell blank for the
# continuation rows; the type is filled in here from the instrument name.
_T1 = [
    ("Quang kế", "PR880", "Photo Research"),
    ("Quang kế/quang phổ kế bức xạ", "PR650", "Photo Research"),
    ("Quang kế Pritchard", "Pritchard 1980B", "Photo Research"),
    ("Máy ảnh đo bức xạ", "GS-1280 RadOMAcam", "Gamma Scientific (EG&amp;G)"),
    ("Ống nhân quang", "—", "Oriel Corp."),
    ("Ống nhân quang", "—", "Hamamatsu"),
    ("Photodiode", "PIN 10AP", "UDT Sensors, Inc."),
    ("Hệ kiểm tra màn phẳng", "FIS 250", "Photon Dynamics, Inc."),
]

_T1_EN = [
    ("Photometer", "PR880", "Photo Research"),
    ("Photometer/spectroradiometer", "PR650", "Photo Research"),
    ("Pritchard photometer", "Pritchard 1980B", "Photo Research"),
    ("Radiometric camera", "GS-1280 RadOMAcam", "Gamma Scientific (EG&amp;G)"),
    ("Photomultiplier tubes", "—", "Oriel Corp."),
    ("Photomultiplier tubes", "—", "Hamamatsu"),
    ("Photodiode", "PIN 10AP", "UDT Sensors, Inc."),
    ("Flat panel inspection system", "FIS 250", "Photon Dynamics, Inc."),
]

_T2 = [
    ("Photo Research",
     "9330 DeSoto Avenue, P.O. Box 2192<br>Chatsworth, CA 91313-2192<br>(818) 341-5151"),
    ("Gamma Scientific (EG&amp;G)",
     "8581 Aero Dr.<br>San Diego, CA 92123-1876<br>(619) 279-8034"),
    ("Oriel Corp.",
     "252 Long Beach Blvd., P.O. Box 872<br>Stratford, CT 06497-0872<br>(203) 380-4200"),
    ("Hamamatsu Photonics Systems Corp.",
     "360-T Foothill Road, P.O. Box 6910<br>Bridgewater, NJ 08807-0910"),
    ("UDT Sensors, Inc.",
     "12525 Chadron Ave.<br>Hawthorne, CA 90250<br>(310) 978-0516"),
    ("Photon Dynamics, Inc.",
     "6325 San Ignacio Ave.<br>San Jose, CA 95119<br>(408) 226-9900"),
]


def _table1(lang):
    if lang == "vi":
        hd = ["Loại dụng cụ", "Model", "Hãng sản xuất"]
        cap = ("Bảng 94.1 · Các dụng cụ đo ánh sáng. Ô loại dụng cụ trong bản gốc để trống ở những "
               "dòng nối tiếp; ở đây loại dụng cụ được ghi rõ theo tên máy.")
        return hd, _T1, cap
    hd = ["Instrument type", "Model", "Manufacturer"]
    cap = ("TABLE 94.1 · Light measurement instruments. The source leaves the type cell blank on "
           "the continuation rows; the instrument type is filled in here from the model name.")
    return hd, _T1_EN, cap


def _table2(lang):
    if lang == "vi":
        hd = ["Hãng", "Địa chỉ liên hệ"]
        cap = ("Bảng 94.2 · Địa chỉ các hãng sản xuất dụng cụ đo ánh sáng nêu trong Bảng 94.1 "
               "(nguyên văn địa chỉ và số điện thoại của bản gốc năm 1999).")
        return hd, _T2, cap
    hd = ["Manufacturer", "Contact address"]
    cap = ("TABLE 94.2 · Manufacturers of light measurement instruments listed in Table 94.1 "
           "(addresses and telephone numbers as printed in the 1999 original).")
    return hd, _T2, cap


# ================================================================ REFERENCES
_REFS = [
    "Y.A. Ono, <i>Electroluminescent Displays</i>, Singapore: World Scientific, 1995.",
    ("T. Inoguchi, M. Takeda, Y. Kakihara, Y. Nakata, and M. Yoshida, “Stable high-brightness "
     "thin-film electroluminescent panels,” <i>Dig. 1974 SID International Symposium</i>, 84, 1974."),
    ("C.N. King, R.E. Coovert, and W.A. Barrow, “Full-color 320 × 240 TFEL display panel,” "
     "<i>Eurodisplay ’87</i>, 14, 1987."),
    ("W.A. Barrow, R.E. Coovert, C.N. King, and M.J. Ziuchkovski, “Matrix-addressed full-color "
     "TFEL display,” <i>Dig. 1988 SID International Symposium</i>, 284, 1988."),
    ("R. Tueta and M. Braguier, “Fabrication and characterization of indium tin oxide thin films "
     "for electroluminescent applications,” <i>Thin Solid Films</i>, 80: 143, 1981."),
    ("J.D. Davidson, J.F. Wager, and I. Khormaei, “Electrical characterization and SPICE modeling "
     "of ZnS:Mn ACTFEL devices,” <i>Dig. 1991 SID International Symposium</i>, 77, 1991."),
    ("A.A. Douglas and J.F. Wager, “ACTFEL device response to systematically varied pulse "
     "waveforms,” in <i>Electroluminescence — Proceedings of the Sixth International Workshop on "
     "Electroluminescence</i>, V.P. Singh and J.C. McClure, Eds., El Paso, TX: Cinco Puntos Press, "
     "1992."),
    "D.H. Smith, “Modeling AC thin-film electroluminescent devices,” <i>J. Lumin.</i>, 23: 209, 1981.",
    ("P.M. Alt, “Thin-film electroluminescent displays: device characteristics and performance,” "
     "<i>Proc. SID</i>, 25: 123, 1984."),
    ("Y.A. Ono, H. Kawakami, M. Fuyama, and K. Onisawa, “Transferred charge in the active layer and "
     "EL device characteristics of TFEL cells,” <i>Jpn. J. Appl. Phys.</i>, 26: 1482, 1987."),
    "E. Bringuier, “Charge transfer in ZnS-type electroluminescence,” <i>J. Appl. Phys.</i>, 66: 1314, 1989.",
    ("A. Abu-Dayah, S. Kobayashi, and J.F. Wager, “Internal charge-phosphor field characteristics "
     "of alternating-current thin-film electroluminescent devices,” <i>Appl. Phys. Lett.</i>, "
     "62: 744, 1993."),
    ("A. Mikami, K. Terada, K. Okibayashi, K. Tanaka, M. Yoshida, and S. Nakajima, “Aging "
     "characteristics of ZnS:Mn electroluminescent films grown by a chemical vapor deposition "
     "technique,” <i>J. Appl. Phys.</i>, 72: 773, 1992."),
]


# ================================================================ VIETNAMESE
def body_vi():
    b = []

    # ------------------------------------------------------------ 94.1
    b.append(h2("94.1 Giới thiệu", "Introduction"))
    b.append(p(
        "Điện phát quang (EL) là sự phát sáng không do nhiệt, sinh ra khi đặt một điện trường lên "
        "một chất. Chất phát sáng nói chung là một tinh thể phát quang. Hầu hết các màn hiển thị EL "
        "đơn sắc bán trên thị trường đều dùng ZnS:Mn làm vật liệu phát quang. Màn hiển thị EL đã "
        "trở nên rất quan trọng trong một số thị trường hiển thị nhất định, gồm thiết bị y tế, thiết "
        "bị điều khiển công nghiệp, thiết bị đo xách tay và xe quân sự. Những thuộc tính khiến màn "
        "hiển thị EL hấp dẫn trong các ứng dụng ấy là độ bền cơ học, tương đối không nhạy với nhiệt "
        "độ môi trường, đáp ứng hiển thị nhanh, góc nhìn gần như không hạn chế, nhỏ gọn và nhẹ."))
    b.append(p(
        "Có bốn loại linh kiện EL: màng mỏng xoay chiều, bột xoay chiều, màng mỏng một chiều và bột "
        "một chiều. Loại màng mỏng xoay chiều hiện chiếm ưu thế áp đảo. Một số màn hiển thị tinh thể "
        "lỏng dùng EL bột xoay chiều làm đèn nền. Hiện gần như không có ứng dụng thương mại nào của "
        "linh kiện EL một chiều, dù là màng mỏng hay bột [1]. Trọng tâm ở đây là linh kiện EL màng "
        "mỏng xoay chiều (ACTFEL). Tuy chưa có kỹ thuật đo tiêu chuẩn nào được thiết lập rộng rãi cho "
        "các loại linh kiện EL khác, vẫn có thể áp dụng những phép đo tương tự như mô tả trong chương "
        "này cho ACTFEL, với những sửa đổi thích hợp theo cách kích thích linh kiện."))

    # ------------------------------------------------------------ 94.2
    b.append(h2("94.2 Cấu trúc và hoạt động của linh kiện",
                "Device Structure and Operation"))
    b.append(p(
        "Sơ đồ mặt cắt của cấu trúc ACTFEL cơ bản [2] được trình bày ở Hình 94.1. Đế đỡ thường làm "
        "bằng thuỷ tinh có hàm lượng natri rất thấp. Nếu lắng một lớp rào ion thích hợp giữa đế và "
        "điện cực dưới của linh kiện EL thì có thể dùng thuỷ tinh soda-lime. Điện cực dưới, thường "
        "là một vật dẫn trong suốt như indi thiếc ôxit (ITO), được lắng tiếp theo. ITO thường dày "
        "trong khoảng 350 và 120 nm, cho điện trở tấm trong khoảng 5 đến 15 Ω/vuông. Trên điện cực "
        "ITO lắng một lớp cách điện dưới, điển hình là SiON hoặc nhôm titan ôxit (ATO), dày thường "
        "khoảng 200 nm. Lớp phát quang, điển hình là ZnS:Mn, được lắng giữa lớp cách điện dưới và "
        "một lớp cách điện trên tương tự. Độ dày lớp phát quang thường trong khoảng 200 đến 1000 nm "
        "tuỳ ứng dụng. Điện cực trên, điển hình bằng nhôm, được lắng trên lớp cách điện trên; nhôm "
        "thường dày 100 đến 200 nm."))

    b.append(fig(1, F.fig(1)))

    b.append(p(
        "Màn hiển thị đơn sắc địa chỉ hoá ma trận được tạo ra bằng cách chia các điện cực trên và "
        "dưới thành những dãy sọc trực giao. Linh kiện EL khi đó được kích thích cục bộ bằng cách "
        "đặt một điện áp giữa một cặp điện cực giao nhau, làm xuất hiện một điện trường giữa chúng "
        "và điện trường này kích thích chất phát quang. Màn hiển thị màu có thể tạo ra bằng cách "
        "chia lớp phát quang thành những sọc phát xạ đỏ, lục và lam thẳng hàng với một trong hai bộ "
        "sọc điện cực [3,4], như trên Hình 94.2. Cũng có thể tạo màn hiển thị màu bằng cách dùng một "
        "lớp phát quang không tạo hình, phát xạ phổ rộng gồm đỏ, lục và lam, rồi lọc phát xạ bằng "
        "một kính lọc màu có tạo hình thẳng hàng với các sọc điện cực, hoặc bằng kính lọc màu theo "
        "trình tự khung hình."))

    b.append(fig(2, F.fig(2)))

    # ------------------------------------------------------------ 94.3
    b.append(h2("94.3 Chế tạo linh kiện", "Device Fabrication"))
    b.append(h3("Các phương pháp lắng màng mỏng", "Thin-Film Deposition Methods"))
    b.append(p(
        "Nhiều kỹ thuật lắng khác nhau được các nhà sản xuất và nhà nghiên cứu dùng trong chế tạo "
        "linh kiện ACTFEL. Các vật liệu điện cực ITO và nhôm thường được lắng bằng kỹ thuật lắng pha "
        "hơi vật lý (PVD). ITO gần như phổ biến được lắng bằng phún xạ magnetron một chiều từ một "
        "bia ITO dẫn hoặc từ một bia hợp kim kim loại [5]. Độ dẫn ITO tối ưu đạt được nhờ ủ sau lắng "
        "trong môi trường rất ít ôxy. Nhôm được lắng bằng phún xạ magnetron một chiều từ bia kim "
        "loại Al, hoặc bằng bay hơi chùm điện tử từ Al kim loại. Các lớp cách điện và phát quang "
        "được lắng bằng cả lắng pha hơi hoá học (CVD) lẫn PVD. Lớp phát quang đã được lắng bằng bay "
        "hơi nhiệt cũng như bay hơi chùm điện tử, phún xạ, CVD kim loại–hữu cơ (MOCVD) và epitaxy "
        "lớp nguyên tử (ALE). Lớp cách điện đã được lắng bằng bay hơi chùm điện tử, phún xạ tần số "
        "vô tuyến (RF), CVD tăng cường plasma (PECVD) và ALE."))
    b.append(h3("Các phương pháp tạo hình màng mỏng", "Thin-Film Patterning Methods"))
    b.append(p(
        "Việc tạo hình các điện cực nói chung được thực hiện bằng ăn mòn hoặc bằng bóc lớp "
        "(liftoff), mặc dù một số tác giả thời đầu tạo hình điện cực nhôm trên bằng cách bay hơi qua "
        "mặt nạ bóng. Nhôm dễ ăn mòn ướt hoặc khô; trên thị trường có sẵn các dung dịch ăn mòn ướt "
        "cho Al. Ăn mòn khô Al có thể thực hiện bằng các hoá học clo tiêu chuẩn, ví dụ "
        "Cl<sub>2</sub>/BCl<sub>3</sub>. Cũng có thể tạo hình Al bằng cách bay hơi lên một mẫu "
        "photoresist đảo rồi bóc phần kim loại thừa. ITO có thể ăn mòn ướt hoặc khô; dung dịch ăn "
        "mòn ướt ITO thường là hỗn hợp HCl và HNO<sub>3</sub>, còn ăn mòn khô ITO có thể thực hiện "
        "trong HI hoặc HBr. Tạo hình các lớp phát quang thì khó hơn. Có dung dịch ăn mòn cho hầu hết "
        "vật liệu phát quang ACTFEL nhưng chúng thường là bí quyết của nhà sản xuất. Chất phát quang "
        "màng mỏng khó ăn mòn vì chúng thường nhạy với nước, và một số chất phát quang màu chứa kim "
        "loại nặng khó bay hơi trong quá trình ăn mòn khô."))

    # ------------------------------------------------------------ 94.4
    b.append(h2("94.4 Hoạt động của linh kiện", "Device Operation"))
    b.append(h3("Cơ chế phát quang", "Luminescence Mechanisms"))
    b.append(p(
        "Như cấu trúc ở Hình 94.1 cho thấy, linh kiện ACTFEL được ghép điện dung. Vì chỉ có dòng dịch "
        "chuyển có thể chạy qua các lớp cách điện, tín hiệu điều khiển buộc phải là một dạng sóng "
        "đảo cực tính. Một dạng sóng thang lưỡng cực điển hình được trình bày ở Hình 94.3. Nếu điện "
        "áp đỉnh <i>V</i><sub>P</sub> trên Hình 94.3 lớn hơn điện áp ngưỡng <i>V</i><sub>th</sub> "
        "của linh kiện, thì khi đặt xung dương của dạng sóng giữa các điện cực Al và ITO của cấu "
        "trúc trên Hình 94.1, giản đồ vùng năng lượng của linh kiện ACTFEL sẽ như trên Hình 94.4. "
        "Các điện tử — hạt tải đa số trong linh kiện ACTFEL — đường hầm thoát khỏi các trạng thái "
        "bề mặt ở phía bên trái và vào vùng dẫn. Khi đã ở trong vùng dẫn, điện tử được gia tốc bởi "
        "điện trường lớn, khoảng 1 MV/cm = 100 kV/mm. Điện tử vùng dẫn trôi ngang qua lớp ZnS:Mn "
        "cho tới khi va chạm kích thích một tâm Mn<sup>2+</sup>, truyền một phần năng lượng cho một "
        "điện tử của tâm này và làm nó chuyển lên một trạng thái kích thích. Điện tử vùng dẫn có "
        "thể va chạm thêm, cuối cùng tới bề mặt bên phải và bị bẫy tại các trạng thái bề mặt ở đó, "
        "chờ xung điện áp kế tiếp có cực tính ngược lại. Xung này làm các điện tử đường hầm thoát "
        "ra và trôi ngược qua lớp ZnS:Mn, truyền năng lượng cho các tâm Mn<sup>2+</sup> trên đường "
        "đi, cho tới khi lại bị bẫy ở bề mặt bên trái. Sự chuyển dịch điện tích qua lại giữa các "
        "trạng thái bề mặt cứ tiếp diễn chừng nào còn đặt tín hiệu điều khiển đảo cực tính có biên "
        "độ đỉnh lớn hơn điện áp ngưỡng của linh kiện. Phát xạ ánh sáng xảy ra khi các tâm "
        "Mn<sup>2+</sup> đã bị kích thích do va chạm bởi điện tử nóng chuyển về trạng thái cơ bản "
        "[6–8]. Như vậy phát xạ ánh sáng là kết quả của chuyển mức của điện tử bên trong các tâm "
        "Mn<sup>2+</sup>, chứ không phải tái hợp cặp điện tử–lỗ trống gần một chuyển tiếp <i>pn</i> "
        "như xảy ra trong điốt phát quang (LED)."))

    b.append(fig(3, F.fig(3)))
    b.append(fig(4, F.fig(4)))

    b.append(h3("Mô tả dòng điện tích", "Description of Charge Flow"))
    b.append(p(
        "Nếu vẽ điện tích ngoài <i>Q</i> chảy vào linh kiện ACTFEL theo điện áp đặt vào từ ngoài "
        "<i>V</i>, đường cong thu được gọi là vòng QV [9,10]. Nếu biên độ các xung điện áp đặt vào "
        "nhỏ hơn điện áp ngưỡng của linh kiện, vòng QV chỉ là một đường thẳng có độ dốc bằng điện "
        "dung tổng của chồng cách điện/phát quang/cách điện. Nếu biên độ xung lớn hơn điện áp "
        "ngưỡng, vòng QV mở ra. Các vòng QV dưới và trên ngưỡng được trình bày ở Hình 94.5. Trên "
        "ngưỡng, công suất bị tiêu tán trong linh kiện ACTFEL. Diện tích bao bởi vòng QV bằng năng "
        "lượng cấp cho linh kiện trong mỗi chu kỳ của dạng sóng điều khiển."))
    b.append(p(
        "Vòng QV được đo trực tiếp. Một mở rộng lý thuyết của vòng QV mà đôi khi được các nhà nghiên "
        "cứu vật lý linh kiện ACTFEL dùng là đồ thị điện tích thực chạy qua lớp phát quang, "
        "<i>Q</i><sub>P</sub>, theo điện trường trong lớp phát quang, <i>F</i><sub>P</sub>. Các đại "
        "lượng cần cho đồ thị <i>Q</i><sub>P</sub><i>F</i><sub>P</sub> có thể tính từ dữ liệu QV nếu "
        "biết độ dày và hằng số điện môi của các lớp cách điện và lớp phát quang. Điện tích thực "
        "chạy qua lớp phát quang được tính bằng cách trừ điện tích phản kháng khỏi điện tích tổng. "
        "Điện trường trong lớp phát quang được tính bằng cách cộng điện trường đặt vào từ ngoài với "
        "điện trường phân cực bên trong do dòng điện tích thực chạy qua lớp phát quang. Một vòng "
        "<i>Q</i><sub>P</sub><i>F</i><sub>P</sub> tương ứng với vòng QV trên ngưỡng ở Hình 94.5 được "
        "trình bày ở Hình 94.6. Vòng <i>Q</i><sub>P</sub><i>F</i><sub>P</sub> hữu ích vì nó biểu diễn "
        "các đặc trưng điện bên trong của lớp phát quang trong quá trình linh kiện hoạt động."))

    b.append(fig(5, F.fig(5)))
    b.append(fig(6, F.fig(6)))

    b.append(h3("Kích thích linh kiện", "Device Excitation"))
    b.append(p(
        "Dù đối tượng đo là một điểm thử hay một màn hiển thị ma trận, dạng sóng điều khiển buộc phải "
        "được ghép xoay chiều. Màn hiển thị ma trận địa chỉ hoá thụ động được quét từng hàng một. Dữ "
        "liệu được nạp vào các mạch lái cột cho một hàng điểm ảnh, và các điểm ảnh được chọn trong "
        "hàng cùng bật đồng thời. Xung hàng đưa điện áp trên mỗi điểm ảnh trong hàng lên mức vừa dưới "
        "ngưỡng. Các cột chứa điểm ảnh được chọn sau đó được đánh xung để đưa điện áp trên các điểm "
        "ảnh được chọn lên trên ngưỡng, và các điểm ảnh bật sáng. Trong khung hình kế tiếp, cực tính "
        "điện áp trên các điểm ảnh được đảo lại."))
    b.append(p(
        "Mỗi điểm ảnh riêng lẻ chịu một tín hiệu điều khiển tương tự như ở Hình 94.3. Để kích hoạt "
        "hoàn toàn một điểm ảnh cần giữ điện áp trên <i>V</i><sub>th</sub> trong 10 đến 20 µs. Vì mỗi "
        "hàng phải được quét tuần tự, một màn hiển thị điển hình khoảng 500 hàng cần ít nhất 5 ms để "
        "quét một khung. Tốc độ khung lớn nhất do đó khoảng 200 Hz. Màn hiển thị địa chỉ hoá bằng ma "
        "trận transistor tích cực không bị quét từng hàng như màn địa chỉ hoá thụ động mà được lái "
        "đồng loạt. Chúng có một điện cực chung không tạo hình, thường là một lớp ITO phía trên, "
        "được đặt tín hiệu điều khiển xoay chiều. Mỗi điểm ảnh nối đất qua một transistor, và "
        "transistor này hạ bớt một phần điện áp điều khiển khi điểm ảnh không được chọn. Với loại "
        "màn này, dạng sóng điều khiển có thể là bất kỳ tín hiệu xoay chiều nào có điện áp thích "
        "hợp; đã dùng dạng sin, thang và tam giác. Màn hiển thị ma trận tích cực có thể được lái với "
        "tốc độ khung cao hơn màn ma trận địa chỉ hoá thụ động một hệ số bằng số hàng của màn, vì "
        "không cần quét từng hàng. Do mỗi xung điện áp phát ra một xung sáng, độ chói trung bình tỉ "
        "lệ với tốc độ khung, dẫn tới khả năng độ chói cao hơn nhiều cho màn ma trận tích cực."))

    # ------------------------------------------------------------ 94.5
    b.append(h2("94.5 Các phép đo tiêu chuẩn", "Standard Measurements"))
    b.append(p(
        "Các đại lượng đo được quan tâm gồm độ chói, hiệu suất sáng, phổ phát xạ, ảnh lưu và khuyết "
        "tật. Độ chói của màn hiển thị ACTFEL là hàm của điện áp đỉnh và tần số dạng sóng điều khiển, "
        "của hiệu suất nội tại của chồng cách điện/phát quang/cách điện, và của lịch sử vận hành (sự "
        "già hoá). Hiệu suất là hàm của hình dạng và tần số dạng sóng điều khiển cũng như nhiều "
        "thông số linh kiện. Phổ phát xạ chủ yếu do vật liệu nền của chất phát quang và các chất hoạt "
        "hoá quyết định, tuy cũng chịu ảnh hưởng của điều kiện lắng và ủ, và trong một số trường hợp "
        "là của điện áp và tần số điều khiển. Ảnh lưu là sự in vết vĩnh viễn của một hình cố định "
        "được hiển thị trong thời gian dài. Nó có thể xuất hiện như một ảnh tối mờ chồng lên nền "
        "sáng, hoặc như một ảnh sáng mờ chồng lên nền tối. Sự hình thành ảnh lưu chịu ảnh hưởng chủ "
        "yếu của tính đối xứng dạng sóng điều khiển và các thông số công nghệ chế tạo linh kiện. "
        "Khuyết tật hiển thị gồm khuyết tật điểm ảnh, khuyết tật đường và khuyết tật vệt (mura)."))

    # ------------------------------------------------------------ 94.6
    b.append(h2("94.6 Các phép đo phân giải thời gian", "Time-Resolved Measurements"))
    b.append(p(
        "Các phép đo độ chói, hiệu suất và phổ phát xạ giới thiệu đến đây đều liên quan tới phát xạ "
        "ánh sáng trung bình theo thời gian. Có hai phép đo phân giải thời gian khá phổ biến với "
        "phát xạ ACTFEL: thời gian tắt phát quang và quang phổ phát xạ phân giải thời gian. Thời "
        "gian tắt phát quang τ là thời gian để phát xạ từ một xung kích thích giảm còn 1/<i>e</i> "
        "lần giá trị ban đầu. Phép đo τ được bắt đầu ngay sau sườn sau của xung kích thích. Điều này "
        "là cần thiết để giá trị τ đo được không bị ảnh hưởng bởi việc tiếp tục kích thích thêm các "
        "tâm phát xạ, nhờ đó nó biểu diễn thời gian hồi phục nội tại của tâm phát xạ. Với linh kiện "
        "dùng chất phát quang ZnS:Mn lắng bằng bay hơi, τ là hàm mạnh của nồng độ Mn, nên có thể "
        "dùng nó như một kỹ thuật phân tích để xác định nồng độ Mn. Quang phổ phân giải thời gian là "
        "phép đo phổ phát xạ trong những phần xác định của quá trình kích thích và phát xạ. Một ví "
        "dụ ứng dụng của kỹ thuật này là nghiên cứu các xung sáng riêng rẽ phát ra ở sườn trước và "
        "sườn sau của xung kích thích với chất phát quang phát xạ lam SrS:Ce. Cả hai kỹ thuật này "
        "thường được dùng để giúp làm rõ cơ chế kích thích và phát xạ trong các chất phát quang "
        "ACTFEL."))

    # ------------------------------------------------------------ 94.7
    b.append(h2("94.7 Đặc trưng hoá điểm thử", "Test Dot Characterization"))
    b.append(h3("Độ chói và hiệu suất", "Luminance and Efficiency"))
    b.append(p(
        "Sơ đồ một hệ đo để thu dữ liệu độ chói và hiệu suất theo điện áp trên một điểm thử được "
        "trình bày ở Hình 94.7. Một bộ tạo dạng sóng tuỳ ý cung cấp tín hiệu điều khiển với dạng "
        "sóng, tần số và điện áp đỉnh do một máy tính điều khiển xác định. Tín hiệu ra của bộ tạo "
        "dạng sóng được khuếch đại từ dải ±5 V lên dải ±300 V. Một quang kế, cũng do máy tính điều "
        "khiển, đo độ chói <i>L</i> của điểm thử. Một dao động ký đo điện áp trên điểm thử và điện "
        "áp trên điện trở cảm biến. Dòng điện được tính bằng cách chia điện áp trên điện trở cảm "
        "biến cho trị số của nó. Nhờ vậy máy tính điều khiển có thể tăng và giảm điện áp đỉnh rồi "
        "thu dữ liệu độ chói, cùng các dạng sóng biểu diễn điện áp trên điểm thử và dòng chạy qua "
        "nó. Năng lượng <i>E</i><sub>P</sub> tiêu tán trong mỗi xung điều khiển được tính là"))

    b.append(eq(_eq("94.1"), "94.1"))

    b.append(p(
        "trong đó <i>I</i>(<i>t</i>) và <i>V</i>(<i>t</i>) lần lượt là dạng sóng dòng và dạng sóng áp, "
        "còn <i>D</i> là độ dài của xung điều khiển dương hoặc xung điều khiển âm. Phép tích phân "
        "này có thể do hầu hết các dao động ký thực hiện, hoặc dữ liệu <i>I</i>(<i>t</i>) và "
        "<i>V</i>(<i>t</i>) có thể được chuyển sang máy tính điều khiển để tính, tuy cách này nói "
        "chung chậm hơn. Năng lượng trung bình <i>E</i> tiêu tán trong mỗi chu kỳ của dạng sóng điều "
        "khiển là trung bình của <i>E</i><sub>P</sub> cho một xung dương và một xung âm. Công suất "
        "trung bình <i>P</i> tiêu tán có thể tính bằng cách nhân <i>E</i> với tần số của dạng sóng "
        "điều khiển. Hiệu suất η được tính như sau:"))

    b.append(eq(_eq("94.2"), "94.2"))

    b.append(p(
        "trong đó <i>L</i> là độ chói tính bằng cd/m<sup>2</sup>, <i>A</i> là diện tích điểm thử "
        "tính bằng m<sup>2</sup>, và <i>P</i> là công suất trung bình tính bằng oát. Các giá trị "
        "<i>L</i> và η được thu cho điện áp đỉnh từ 10 V dưới ngưỡng tới 40 hoặc 50 V trên ngưỡng. "
        "Đồ thị <i>L</i> và η theo điện áp đỉnh của một linh kiện điển hình được trình bày ở "
        "Hình 94.8."))

    b.append(fig(7, F.fig(7)))
    b.append(fig(8, F.fig(8)))

    b.append(h3("Dòng điện tích và điện trường", "Charge Flow and Electric Field"))
    b.append(p(
        "Vòng QV được đo bằng một mạch giống hệt mạch ở Hình 94.7, chỉ khác là điện trở cảm biến "
        "được thay bằng một tụ cảm biến và không dùng quang kế. Trị số của tụ cảm biến được chọn lớn "
        "hơn nhiều so với điện dung của linh kiện ACTFEL để điện áp rơi trên tụ cảm biến là nhỏ. Vì "
        "tụ cảm biến và linh kiện ACTFEL mắc nối tiếp, điện tích tích trên chúng bằng nhau. Do đó "
        "điện tích <i>Q</i> trên linh kiện ACTFEL là"))

    b.append(eq(_eq("94.3"), "94.3"))

    b.append(p(
        "trong đó <i>C</i><sub>S</sub> là điện dung của tụ cảm biến và <i>V</i><sub>S</sub> là điện "
        "áp xuất hiện trên nó. Khi vẽ <i>Q</i>(<i>t</i>) theo <i>v</i>(<i>t</i>) ta được vòng QV. "
        "Trong vòng QV lý tưởng ở Hình 94.5, <i>V</i><sub>th</sub> (C) là điện áp ngưỡng, "
        "<i>V</i><sub>to</sub> (B) là điện áp mở, và <i>V</i><sub>P</sub> (D,E) là điện áp đỉnh của "
        "dạng sóng điều khiển. Điện áp ngưỡng là điện áp tại đó xuất hiện điểm gãy đầu tiên của "
        "đường cong <i>L–V</i>. Nếu <i>C</i><sub>T</sub> là điện dung tổng của linh kiện dưới "
        "ngưỡng, thì đây cũng là điện áp tại đó đường <i>Q</i> = <i>C</i><sub>T</sub><i>V</i> cắt "
        "vòng QV mở trên ngưỡng (C). Trong thực tế, đôi khi ngưỡng được định nghĩa là điện áp mà "
        "tại đó đạt tới một giá trị độ chói nhất định ở một tần số cho trước, ví dụ điện áp tại đó "
        "độ chói là 1 cd/m<sup>2</sup> ở 60 Hz. <i>V</i><sub>to</sub> là điện áp tại đó độ dốc của "
        "vòng QV chuyển từ <i>C</i><sub>T</sub> sang <i>C</i><sub>I</sub>, với <i>C</i><sub>I</sub> "
        "là điện dung của các lớp cách điện."))
    b.append(p(
        "Vì một phần tử năng lượng vi phân cấp cho linh kiện ACTFEL là d<i>E</i> = "
        "<i>V</i>(<i>t</i>)d<i>Q</i>, nên"))

    b.append(eq(_eq("94.4"), "94.4"))

    b.append(p(
        "Năng lượng cấp trong mỗi chu kỳ của dạng sóng điều khiển do đó bằng diện tích bao bởi vòng "
        "QV. Công suất tiêu tán chỉ là năng lượng mỗi chu kỳ nhân với tần số. Trong thực tế, diện "
        "tích vòng QV được đo bằng tích phân số. Phép tính có thể thực hiện trên dao động ký nếu máy "
        "có khả năng phân tích, hoặc dữ liệu có thể được chuyển sang máy tính điều khiển để tích "
        "phân."))
    b.append(p(
        "Việc tạo vòng <i>Q</i><sub>P</sub><i>F</i><sub>P</sub> không cần phép đo điện nào khác ngoài "
        "những phép đo đã dùng cho vòng QV. <i>Q</i><sub>P</sub> là điện tích phân ly trên lớp phát "
        "quang và <i>F</i><sub>P</sub> là điện trường trong lớp phát quang. Nếu biết độ dày và hằng "
        "số điện môi của các lớp cách điện và lớp phát quang, có thể tính <i>Q</i><sub>P</sub> và "
        "<i>F</i><sub>P</sub> từ các giá trị <i>Q</i>(<i>t</i>) và <i>V</i>(<i>t</i>) trên vòng QV. "
        "Việc này được thực hiện bằng các phương trình sau [11,12]:"))

    b.append(eq(_eq("94.5"), "94.5"))
    b.append(p("và"))
    b.append(eq(_eq("94.6"), "94.6"))

    b.append(p(
        "trong đó <i>C</i><sub>i</sub> là điện dung của các lớp cách điện, <i>C</i><sub>P</sub> là "
        "điện dung của lớp phát quang, và <i>d</i><sub>P</sub> là độ dày của lớp phát quang."))

    b.append(h3("Các phép đo phân giải thời gian", "Time-Resolved Measurements"))
    b.append(p(
        "Thiết bị đo τ được trình bày ở Hình 94.9. Một ống nhân quang (PMT) được dùng để phát hiện "
        "phát xạ ánh sáng theo thời gian. Hệ điều khiển được đặt để tạo ra các xung điều khiển tương "
        "đối hẹp, điển hình 10 µs, ở tần số tương đối thấp, điển hình 60 Hz. Cách này hiệu quả với "
        "các chất phát quang có thời gian tắt tương đối dài, cỡ 100 µs đến vài miligiây. Đó là "
        "trường hợp của nhiều chất phát quang ACTFEL thông dụng như ZnS:Mn và ZnS:Tb. Tuy vậy, những "
        "chất như SrS:Ce có thời gian tắt rất nhanh và không thể đo theo cách này. Trong trường hợp "
        "ấy phải đo thời gian tắt quang phát quang bằng một laser xung để kích thích chất phát "
        "quang, cùng với thời gian đáp ứng RC đủ nhỏ của hệ phát hiện ánh sáng."))
    b.append(p(
        "Sơ đồ chung để đo phổ phát xạ phân giải thời gian của linh kiện ACTFEL được trình bày ở "
        "Hình 94.10. Dao động ký được kích hoạt theo dạng sóng điều khiển và khoảng tích phân tín "
        "hiệu được đặt vào vùng quan tâm. Cũng có thể dùng một bộ tích phân boxcar để tích phân tín "
        "hiệu ánh sáng trong cửa sổ thời gian mong muốn. Bước sóng của máy đơn sắc được quét và phổ "
        "phát xạ được thu cho phần đã chọn của quá trình phát xạ."))

    b.append(fig(9, F.fig(9)))
    b.append(fig(10, F.fig(10)))

    b.append(h3("Sự già hoá", "Aging"))
    b.append(p(
        "Linh kiện ACTFEL có xu hướng ổn định sau vài chục giờ đốt cháy, nhưng có thể có hành vi già "
        "hoá phức tạp trong quá trình đốt cháy. Ví dụ, đường cong độ chói theo điện áp của linh kiện "
        "ZnS:Mn có lớp phát quang lắng bằng bay hơi có xu hướng dịch về điện áp cao hơn một chút "
        "trong quá trình đốt cháy [2]. Đường cong độ chói theo điện áp của linh kiện có ZnS:Mn lắng "
        "bằng ALE lại có xu hướng dịch về điện áp thấp hơn một chút [13]. Dữ liệu già hoá được thu "
        "bằng cách đo độ chói theo điện áp tại những khoảng thời gian chọn trước trong quá trình "
        "già hoá. Phép đo được thực hiện như đã mô tả ở trên cho các phép đo độ chói theo điện áp. "
        "Việc già hoá được thực hiện bằng cách vận hành linh kiện liên tục ở một điện áp cố định "
        "hoặc ở một điện áp cố định trên ngưỡng. Quá trình già hoá có thể được tăng tốc bằng cách "
        "vận hành linh kiện ở tần số cao hơn."))

    # ------------------------------------------------------------ 94.8
    b.append(h2("94.8 Đặc trưng hoá màn hiển thị địa chỉ hoá ma trận",
                "Characterization of Matrix-Addressed Displays"))
    b.append(p(
        "Việc đặc trưng hoá màn hiển thị địa chỉ hoá ma trận khác với đặc trưng hoá điểm thử vì ít "
        "có khả năng điều khiển dạng sóng điều khiển hơn. Các mạch lái hàng và cột không cho nhiều "
        "mềm dẻo, tuy vẫn có thể gây ảnh hưởng phần nào bằng cách thay đổi dạng sóng điều khiển tổng "
        "hợp và các tín hiệu điều khiển gửi tới các chip lái. Tuy vậy, những sửa đổi như vậy đòi hỏi "
        "hiểu biết chi tiết về điện tử địa chỉ hoá và điều khiển liên quan, và tốt nhất nên để nhà "
        "sản xuất màn hiển thị gốc thực hiện."))
    b.append(p(
        "Những phép đo dễ tiếp cận hơn và được quan tâm chung hơn gồm đặc trưng hoá độ chói, độ màu, "
        "độ đồng đều, tuổi thọ màn hiển thị, ảnh lưu và khuyết tật. Với những phép đo này, màn hiển "
        "thị cần đo được điều khiển bằng máy tính qua một đầu ra video chuẩn hoặc qua một giao diện "
        "hiển thị video riêng đi kèm màn. Điện áp và tần số vận hành của màn được cố định. Màn được "
        "đặt trong một phòng tối hoặc một vỏ kín. Độ chói được đo bằng quang kế. Độ màu được đo bằng "
        "quang phổ kế, hoặc bằng quang kế có gắn các kính lọc ba kích thích. Độ đồng đều có thể đo "
        "bằng cách gắn màn hiển thị hoặc quang kế/quang phổ kế lên một hệ dịch chuyển rồi thu dữ liệu "
        "tại các điểm trong một mảng đều trên khắp bề mặt màn. Tuổi thọ màn hiển thị được đặc trưng "
        "hoá bằng cách vận hành màn ở một hình bật toàn bộ, luân phiên qua các hình bàn cờ, v.v., và "
        "đo độ chói tại những khoảng thời gian tăng theo cấp số nhân. Ảnh lưu được tạo bằng cách "
        "hiển thị những khối nhỏ ở nhiều vị trí cố định và nhiều mức xám cố định khác nhau (nếu có) "
        "một cách liên tục trong thời gian dài. Nó được đặc trưng hoá bằng cách đặt toàn bộ màn hình "
        "về từng mức xám có được và đo độ chói tại những vị trí đã hiển thị khối trong quá trình "
        "già hoá cũng như tại những vùng chưa già hoá gần đó. Ảnh lưu là phần trăm chênh lệch độ "
        "chói giữa các khối đã già hoá và các vùng chưa già hoá gần đó. Ảnh lưu điển hình được đo "
        "sau khi già hoá hình khối trong 1000 h. Khuyết tật được phân thành khuyết tật điểm ảnh, "
        "khuyết tật đường và khuyết tật vệt. Chúng được đặc trưng hoá bằng kiểm tra bằng mắt với sự "
        "trợ giúp của một kính lúp, hoặc bằng một hệ kiểm tra màn phẳng tự động."))

    # ------------------------------------------------------------ 94.9
    b.append(h2("94.9 Thiết bị kích thích và đo", "Excitation and Measurement Equipment"))
    b.append(h3("Kích thích điểm thử", "Excitation of Test Dots"))
    b.append(p(
        "Điểm thử có thể được kích thích bằng bất kỳ nguồn tín hiệu nào cung cấp được xung lưỡng cực "
        "tới điện áp đỉnh 300 V, với khả năng cấp và hút dòng đủ để nạp và xả điện dung của linh "
        "kiện. Có thể chế tạo bộ lái xung lưỡng cực đủ điện áp và dòng ra từ các linh kiện bán trên "
        "thị trường. Một op-amp mạch lai do Apex Microtechnology sản xuất cho điện áp ra và đáp ứng "
        "tần số đủ dùng. Có thể thêm một tầng tăng cường dòng ở đầu ra nếu điện dung của đối tượng "
        "đo quá lớn để lái trực tiếp. Cách dùng bộ khuếch đại này rất mềm dẻo vì có thể dùng bất kỳ "
        "dạng sóng nào mà bộ tạo dạng sóng tuỳ ý tạo ra được. Cũng có một số bộ khuếch đại thương "
        "mại hiệu quả để lái điểm thử cho một số phép đo nhất định. Chúng thường có băng thông hạn "
        "chế và phải dùng thận trọng trong những trường hợp phép đo nhạy với hình dạng chính xác "
        "của xung điều khiển; ví dụ đó là trường hợp của các phép đo QV và thường cả của các phép đo "
        "hiệu suất."))
    b.append(h3("Kích thích màn hiển thị địa chỉ hoá ma trận",
                "Excitation of Matrix-Addressed Displays"))
    b.append(p(
        "Kích thích màn hiển thị địa chỉ hoá ma trận khá đơn giản vì điện tử điều khiển đã được tích "
        "hợp với màn. Nói chung chỉ cần một ổ điện xoay chiều chuẩn và một máy tính có card video "
        "thích hợp. Có thể tạo các hình thử để đo bằng những chương trình máy tính đơn giản."))

    # ------------------------------------------------------------ 94.10
    b.append(h2("94.10 Dụng cụ đo", "Measurement Instruments"))
    b.append(h3("Đo điện áp và dòng điều khiển", "Measurement of Drive Voltage and Current"))
    b.append(p(
        "Mọi phép đo điện mô tả trong chương này đều dùng dao động ký số. Có thể mua dụng cụ thích "
        "hợp từ nhiều hãng, trong đó có Tektronix và Hewlett-Packard. Băng thông 100 MHz là quá đủ. "
        "Khả năng phân tích dạng sóng rất hữu ích nhưng không thực sự cần thiết. Cần có các giao diện "
        "RS-232 hoặc IEEE 488 để điều khiển bằng máy tính và truyền dữ liệu."))
    b.append(h3("Đo ánh sáng phát xạ", "Measurement of Emitted Light"))
    b.append(p(
        "Người ta dùng nhiều loại dụng cụ để đo phát xạ ánh sáng từ màn hiển thị ACTFEL. Quang kế "
        "dùng cho các phép đo độ chói. Quang phổ kế dùng để đo phổ phát xạ và, với phần mềm thích "
        "hợp, cũng cho được các phép đo độ chói. Các phép đo phân giải thời gian được thực hiện bằng "
        "cách dùng ống nhân quang hoặc photodiode. Bảng 94.1 liệt kê một số ví dụ về quang kế, quang "
        "phổ kế bức xạ, ống nhân quang và photodiode cùng tên các hãng sản xuất. Một phát triển "
        "tương đối mới để đặc trưng hoá đặc tính phát xạ ánh sáng của màn hiển thị phẳng, kể cả màn "
        "ACTFEL, là hệ kiểm tra màn phẳng. Đây là một hệ đo lớn gồm một camera CCD, một vỏ kín chắn "
        "sáng, một máy tính điều khiển, một bộ xử lý ảnh và phần mềm chuyên dụng. Hệ loại này tạo "
        "ảnh toàn bộ màn hiển thị phẳng trên camera CCD rồi đo độ chói, độ màu và các khuyết tật "
        "khác nhau bằng cách phân tích ảnh. Những hệ này nhắm tới môi trường sản xuất có thông lượng "
        "cao và có giá vài trăm nghìn đô la. Một ví dụ về hệ loại này cũng được đưa vào Bảng 94.1. "
        "Thông tin liên hệ của các hãng nêu trong Bảng 94.1 được cung cấp ở Bảng 94.2."))

    hd1, rows1, cap1 = _table1("vi")
    b.append(table(hd1, rows1, cap1))
    hd2, rows2, cap2 = _table2("vi")
    b.append(table(hd2, rows2, cap2))

    # ------------------------------------------------------------ terms
    b.append(h2("Định nghĩa thuật ngữ", "Defining Terms"))
    b.append(dt("Điện phát quang (<i>electroluminescence</i>)",
                "sự phát sáng không do nhiệt, sinh ra khi đặt một điện trường lên một chất, thường "
                "là một tinh thể phát quang."))
    b.append(dt("Ảnh lưu (<i>latent image</i>)",
                "ảnh bóng ma của một hình đã hiển thị trước đó, đôi khi còn thấy được trên toàn bộ "
                "màn hình của một màn hiển thị điện tử."))
    b.append(dt("Thời gian tắt phát quang (<i>light emission decay time</i>)",
                "thời gian để phát xạ ánh sáng từ một xung kích thích giảm còn 1/<i>e</i> lần giá "
                "trị ban đầu."))
    b.append(dt("Điện tích phân cực (<i>polarization charge</i>)",
                "điện tích bị bẫy tại bề mặt chất phát quang/cách điện sau khi đặt một xung điều "
                "khiển."))
    b.append(dt("Điện trường phân cực (<i>polarization field</i>)",
                "điện trường trong lớp phát quang sinh ra bởi điện tích phân cực."))
    b.append(dt("Vòng <i>Q</i><sub>P</sub><i>F</i><sub>P</sub> (<i>Q</i><sub>P</sub><i>F</i><sub>P</sub> loop)",
                "đường cong kín thu được khi vẽ dòng điện tích bên trong chạy qua lớp phát quang "
                "(<i>Q</i><sub>P</sub>) theo điện trường trong lớp phát quang "
                "(<i>F</i><sub>P</sub>)."))
    b.append(dt("Vòng QV (<i>QV loop</i>)",
                "đường cong kín thu được khi vẽ điện tích ngoài (<i>Q</i>) chảy vào một linh kiện "
                "TFEL theo điện áp đặt vào từ ngoài (<i>V</i>)."))
    b.append(dt("Điện áp ngưỡng (<i>threshold voltage</i>)",
                "biên độ điện áp của dạng sóng điều khiển mà trên mức đó dòng điện chạy qua lớp phát "
                "quang và linh kiện TFEL phát xạ ánh sáng."))
    b.append(dt("Điện áp mở (<i>turn-on voltage</i>)",
                "điện áp ứng với điểm gãy đầu tiên trong vòng QV của một linh kiện TFEL; đây là điện "
                "áp tại đó điện tích bắt đầu chạy qua lớp phát quang. Điện áp này nói chung nhỏ hơn "
                "điện áp ngưỡng vì điện trường bên trong lớp phát quang được tăng cường bởi điện "
                "trường phân cực một khi điện tích phân cực đã tích luỹ tới trạng thái dừng."))

    # ------------------------------------------------------------ note
    b.append(h2("Ghi chú của người dịch", "Translator's note"))
    b.append(note(
        "Bản gốc là bản quét có lớp văn bản bị mất một số ký hiệu, và có vài chỗ nội bộ không nhất "
        "quán. Sáu điểm sau đã được xử lý như sau. <b>(1)</b> Các ký hiệu Hy Lạp và một số dấu bị "
        "mất trong lớp văn bản: “5 to 15 W/square” là 5–15 Ω/vuông (ký hiệu ôm thành chữ W); “30 ms” "
        "ở chú thích Hình 94.3 là 30 µs; “10 ms pulse width” ở mục 94.7 là 10 µs; “100 ms to a few "
        "milliseconds” là 100 µs đến vài miligiây; “320 ´ 240” ở tài liệu [3] là 320 × 240. Ở đây "
        "đã khôi phục đúng đơn vị, vì một xung 30 ms ở tần số 60 Hz không thể lọt vào khung hình "
        "16,7 ms. <b>(2)</b> Hai chữ Hy Lạp bị thay bằng chữ Latinh trong bản gốc: hiệu suất “h” "
        "chính là η (kể cả trong phương trình 94.2 in là “h p = LA / P”), và thời gian tắt phát "
        "quang “t” chính là τ. Bản dịch dùng lại η và τ. <b>(3)</b> Độ dày ITO in là “350 and 120 "
        "nm”, một khoảng bị đảo (350 > 120); bản dịch giữ nguyên như bản gốc và ghi nhận rằng giá "
        "trị hợp lý nhiều khả năng là 35–120 nm, vì một lớp ITO dày 350 nm sẽ quá dày so với điện "
        "trở tấm 5–15 Ω/vuông đi kèm. <b>(4)</b> Độ rộng xung điều khiển được nêu hai giá trị khác "
        "nhau: chú thích Hình 94.3 ghi 30 µs còn mục 94.7 ghi 10 µs. Cả hai được giữ nguyên vì "
        "chúng ứng với hai thí nghiệm khác nhau (dạng sóng minh hoạ và thiết bị đo thời gian tắt). "
        "<b>(5)</b> Thứ tự hai mốc <i>V</i><sub>to</sub> và <i>V</i><sub>th</sub>: phần thân bài gán "
        "<i>V</i><sub>to</sub> cho điểm B và <i>V</i><sub>th</sub> cho điểm C, và mục Định nghĩa "
        "thuật ngữ khẳng định điện áp mở nói chung nhỏ hơn điện áp ngưỡng. Hình 94.5 ở bản dịch đặt "
        "hai vạch theo đúng cách gán này, tức là ngược với thứ tự trái sang phải của hình trong bản "
        "gốc. <b>(6)</b> “Mura” là một thuật ngữ tiếng Nhật trong công nghiệp màn phẳng, chỉ loại "
        "khuyết tật vệt loang không đều, độ tương phản thấp; chưa có cách dịch tiếng Việt ổn định "
        "nên được giữ nguyên và chú là “khuyết tật vệt”."))

    b.append(h2("Tài liệu tham khảo", "References"))
    b.append(refs(_REFS))

    return "".join(b)


# ================================================================ ENGLISH
def body_en():
    b = []

    b.append(h2("94.1 Introduction"))
    b.append(p(
        "Electroluminescence (EL) is the nonthermal generation of light resulting from the "
        "application of an electric field to a substance. The light-emitting substance is generally "
        "a luminescent crystal. Most commercially available monochrome EL displays utilize ZnS:Mn as "
        "the luminescent material. EL displays have become very important in certain display "
        "markets. These include medical instrumentation, industrial control equipment, portable "
        "instrumentation, and military vehicles. The attributes of EL displays that make them "
        "attractive in these types of applications are mechanical ruggedness, relative insensitivity "
        "to ambient temperature, rapid display response, essentially unlimited viewing angle, "
        "compactness, and light weight."))
    b.append(p(
        "There are four types of EL devices: ac thin film, ac powder, dc thin film, and dc powder. "
        "The ac thin-film display is by far the dominant device type. Some liquid crystal displays "
        "use ac powder EL for backlights. There is currently little or no commercial application of "
        "dc EL devices, either thin film or powder [1]. The focus here is on ac thin-film EL "
        "(ACTFEL) devices. While there are no widely established standard measurement techniques for "
        "the other EL device types, measurements similar to those described herein for ACTFEL "
        "devices could be applied with appropriate modifications to the other methods of device "
        "excitation."))

    b.append(h2("94.2 Device Structure and Operation"))
    b.append(p(
        "A schematic, cross-sectional representation of the basic ACTFEL device structure [2] is "
        "shown in Fig. 94.1. The supporting substrate is usually made of very low sodium glass. If a "
        "suitable ion barrier layer is deposited between the substrate and lower electrode of the EL "
        "device, soda-lime glass can be used. The lower electrode, usually a transparent conductor "
        "such as indium tin oxide (ITO), is deposited next. The ITO is usually between 350 and "
        "120 nm in thickness, providing sheet resistance in the range of 5 to 15 Ω/square. On top of "
        "the ITO electrode a lower insulator is deposited. This layer is typically SiON or aluminum "
        "titanium oxide (ATO). The thickness is normally around 200 nm. The phosphor layer, "
        "typically ZnS:Mn, is deposited between the lower insulator and a similar upper insulator. "
        "The phosphor thickness is typically in the range 200 to 1000 nm, depending on the "
        "application. The upper electrode, typically aluminum, is deposited on top of the upper "
        "insulator. The aluminum is generally 100 to 200 nm thick."))
    b.append(fig(1, F.fig(1), "en"))
    b.append(p(
        "A matrix-addressed monochrome display is created by dividing the upper and lower electrodes "
        "into orthogonal arrays of electrode stripes. The EL device is then excited locally by "
        "applying a voltage between a pair of crossing electrodes, causing an electric field to "
        "exist between them, which excites the phosphor. A color display can be created by dividing "
        "the phosphor into stripes of red-, green- and blue-emitting phosphors which are aligned with "
        "one of the sets of electrode stripes [3,4]. This is shown schematically in Fig. 94.2. Color "
        "displays can also be created by using an unpatterned phosphor which emits a broad spectrum "
        "including red, green, and blue and filtering the emission using either a patterned color "
        "filter which is aligned with the electrode stripes or a frame sequential color filter."))
    b.append(fig(2, F.fig(2), "en"))

    b.append(h2("94.3 Device Fabrication"))
    b.append(h3("Thin-Film Deposition Methods"))
    b.append(p(
        "A wide variety of deposition techniques are used by various manufacturers and researchers in "
        "the fabrication of ACTFEL devices. The electrode materials ITO and aluminum are usually "
        "deposited by physical vapor deposition (PVD) techniques. ITO is almost universally deposited "
        "by dc magnetron sputtering from either a conductive ITO target or from a metal alloy target "
        "[5]. Optimum ITO conductivity is obtained by postdeposition annealing in a very low oxygen "
        "environment. Al is deposited either by dc magnetron sputtering from an Al metal target or by "
        "electron beam evaporation of Al metal. The insulator and phosphor layers are deposited by "
        "chemical vapor deposition (CVD) as well as PVD. Phosphor layers have been deposited by "
        "thermal as well as e-beam evaporation, sputtering, metal–organic CVD (MOCVD), and atomic "
        "layer epitaxy (ALE). Insulator layers have been deposited by e-beam evaporation, radio "
        "frequency (RF) sputtering, plasma-enhanced CVD (PECVD), and ALE."))
    b.append(h3("Thin-Film Patterning Methods"))
    b.append(p(
        "Patterning of the electrodes is generally accomplished either through etching or liftoff, "
        "although some early workers patterned the upper aluminum electrodes by evaporating through a "
        "shadow mask. Aluminum is easily etched wet or dry. There are commercially available wet "
        "etches for Al. Dry etching of Al can be carried out using standard chlorine chemistries, "
        "e.g., Cl<sub>2</sub>/BCl<sub>3</sub>. Al can also be patterned by evaporating onto a "
        "reversed photoresist pattern and lifting off excess metal. ITO can be etched wet or dry. ITO "
        "wet etches generally consist of mixtures of HCl and HNO<sub>3</sub>. ITO can be dry-etched "
        "in HI or HBr. Patterning of the phosphor layers is more problematic. Phosphor etches exist "
        "for most ACTFEL phosphor materials, but they are generally proprietary. Thin-film phosphors "
        "are difficult to etch because they are usually water sensitive, and some color phosphors "
        "contain heavy metals which are difficult to volatilize in a dry-etch process."))

    b.append(h2("94.4 Device Operation"))
    b.append(h3("Luminescence Mechanisms"))
    b.append(p(
        "As the device structure shown in Fig. 94.1 indicates, ACTFEL devices are capacitively "
        "coupled. Since only displacement current can flow across the insulator layers, the drive "
        "signal must be an alternating polarity waveform. A typical alternating polarity, trapezoidal "
        "waveform is shown in Fig. 94.3. If the peak voltage, <i>V</i><sub>P</sub>, in Fig. 94.3 is "
        "larger than the threshold voltage of the device, <i>V</i><sub>th</sub>, then, when the "
        "positive pulse of the waveform is applied between the Al and ITO electrodes of the device "
        "structure shown in Fig. 94.1, the energy band diagram of the ACTFEL device will be as shown "
        "in Fig. 94.4. Electrons, which are the majority carriers in ACTFEL devices, tunnel out of "
        "the interface states on the left and into the conduction band. Once in the conduction band "
        "the electrons are accelerated by the large electric field, which is approximately "
        "1 MV/cm = 100 kV/mm. The conduction electrons drift across the ZnS:Mn layer until they "
        "impact excite an Mn<sup>2+</sup> center, transferring some energy to one of its electrons "
        "and causing it to undergo a transition to an excited state. The conduction electron may "
        "undergo additional collisions, eventually reaching the right interface and getting trapped "
        "in interface states there until the next voltage pulse, which is of the opposite polarity. "
        "This pulse causes the electrons to tunnel out and drift back across the ZnS:Mn layer, "
        "transferring energy to Mn<sup>2+</sup> centers along the way, until eventually they are "
        "trapped again at the left interface. This transfer of charge back and forth between the "
        "interface states continues as long as the alternating polarity drive signal with a peak "
        "amplitude above the threshold voltage of the device continues to be applied. Light emission "
        "occurs when the Mn<sup>2+</sup> centers, which have been impact excited by the hot "
        "electrons, relax [6–8]. The light emission thus results from transitions of the electrons "
        "within the Mn<sup>2+</sup> centers, rather than electron–hole pair recombination near a "
        "<i>pn</i> junction as occurs in a light-emitting diode (LED)."))
    b.append(fig(3, F.fig(3), "en"))
    b.append(fig(4, F.fig(4), "en"))
    b.append(h3("Description of Charge Flow"))
    b.append(p(
        "If the external charge, <i>Q</i>, flowing into the ACTFEL device is plotted vs. the "
        "externally applied voltage, <i>V</i>, the resulting curve is called a QV loop [9,10]. If the "
        "amplitude of the applied voltage pulses is less than the threshold voltage of the device, "
        "the QV loop is simply a straight line with slope equal to the total capacitance of the "
        "insulator/phosphor/insulator stack. If the amplitude of the applied voltage pulses is "
        "greater than the threshold voltage of the device, the QV loop opens up. QV loops below and "
        "above threshold are shown in Fig. 94.5. Above threshold, power is dissipated in the ACTFEL "
        "device. The area encompassed by the QV loop is equal to the energy delivered to the device "
        "per period of the drive waveform."))
    b.append(p(
        "The QV loop is measured directly. A theoretical extension of the QV loop that is sometimes "
        "used by researchers studying the physics of ACTFEL devices is a plot of the actual charge "
        "flow across the phosphor layer, <i>Q</i><sub>P</sub>, vs. the electric field across the "
        "phosphor layer, <i>F</i><sub>P</sub>. The quantities required for a plot of "
        "<i>Q</i><sub>P</sub><i>F</i><sub>P</sub> can be calculated from the QV data if the "
        "thicknesses and dielectric constants of the insulator layers and phosphor layer are known. "
        "The actual charge flow across the phosphor is calculated by subtracting the reactive charge "
        "from the total charge. The field in the phosphor layer is calculated by adding the "
        "externally applied field to the internal polarization field due to the actual flow of "
        "charges across the phosphor layer. A <i>Q</i><sub>P</sub><i>F</i><sub>P</sub> loop "
        "corresponding to the above threshold QV loop of Fig. 94.5 is shown in Fig. 94.6. The "
        "<i>Q</i><sub>P</sub><i>F</i><sub>P</sub> loop is useful because it expresses the internal "
        "electrical characteristics of the phosphor layer during device operation."))
    b.append(fig(5, F.fig(5), "en"))
    b.append(fig(6, F.fig(6), "en"))
    b.append(h3("Device Excitation"))
    b.append(p(
        "Whether the device under test is a test dot or a matrix display, the drive waveform must be "
        "ac coupled. Passively addressed matrix displays are scanned one row at a time. Data are "
        "loaded into the column drivers for a single row of pixels and the selected pixels in the row "
        "are all turned on simultaneously. The row pulse brings the voltage across each pixel in the "
        "row to a level just below threshold. The columns of selected pixels are then pulsed to bring "
        "the voltage across selected pixels to a level above threshold and the pixels are turned on. "
        "During the following frame the voltage polarities across the pixels are reversed."))
    b.append(p(
        "Each individual pixel is subjected to a drive signal similar to that shown in Fig. 94.3. To "
        "activate a pixel fully requires the voltage to be held above <i>V</i><sub>th</sub> for 10 to "
        "20 µs. Since each row must be scanned in sequence, a typical display with approximately 500 "
        "rows requires at least 5 ms to scan one frame. The maximum frame rate is thus approximately "
        "200 Hz. Displays that are addressed by an active matrix of transistors are not scanned a "
        "line at a time as passively addressed displays are, but instead are bulk driven. They have "
        "one unpatterned common electrode, usually an upper layer of ITO, to which an ac drive signal "
        "is applied. Each pixel is connected to ground through a transistor which drops a portion of "
        "the applied drive voltage when the pixel is not selected. In this type of display the drive "
        "waveform can be any ac signal of the appropriate voltage. Sine, trapezoid, and triangle "
        "waveforms have been used. An active matrix display can be driven with a frame rate higher "
        "than a passive matrix-addressed display by a factor equal to the number of rows in the "
        "display, since row-at-a-time scanning is not required. Since a light pulse is emitted for "
        "each voltage pulse, the average luminance is proportional to the frame rate, resulting in "
        "much higher luminance capability for active matrix-addressed displays."))

    b.append(h2("94.5 Standard Measurements"))
    b.append(p(
        "Measurable quantities of interest include luminance, luminous efficiency, emission "
        "spectrum, latent image, and defects. The luminance of an ACTFEL display is a function of the "
        "peak voltage and frequency of the drive waveform, the intrinsic efficiency of the "
        "insulator/phosphor/insulator stack, and the operating history (aging). The efficiency is a "
        "function of the drive waveform shape and frequency as well as various device parameters. The "
        "emission spectrum is primarily determined by the phosphor host material and activators, "
        "although it is also affected by deposition and anneal conditions and in some cases by the "
        "drive voltage and frequency. Latent image is the burning in of a permanent image of a fixed "
        "pattern which is displayed for long periods. It can appear as a faint dark image "
        "superimposed on a bright background or as a faint bright image superimposed on a dark "
        "background. Formation of latent image is affected primarily by drive waveform symmetry and "
        "device processing parameters. Display defects include pixel, line, and mura defects."))

    b.append(h2("94.6 Time-Resolved Measurements"))
    b.append(p(
        "Measurements of luminance, efficiency, and emission spectra as introduced so far involve "
        "time-averaged light emission. There are two fairly common time-resolved measurements of "
        "ACTFEL light emission: light emission decay time and time-resolved light emission "
        "spectroscopy. The light emission decay time, τ, is the time it takes for the light emission "
        "from one excitation pulse to fall to 1/<i>e</i> times its initial value. The measurement of "
        "τ is started just after the trailing edge of the excitation pulse. This is necessary in "
        "order that the measured value of τ not be affected by the continuing excitation of "
        "additional emission centers, so that it represents the intrinsic relaxation time of the "
        "emission center. In devices with evaporated ZnS:Mn phosphor, τ is a strong function of the "
        "Mn concentration. It can thus be used as an analytical technique to determine the Mn "
        "concentration. Time-resolved spectroscopy is the measurement of the emission spectrum "
        "occurring during specific portions of the excitation and emission process. An example of the "
        "application of this technique is the study of the separate light pulses emitted during the "
        "leading and trailing edges of the excitation pulse with the blue-emitting phosphor SrS:Ce. "
        "Both of these techniques are frequently used to help elucidate the excitation and emission "
        "mechanisms in ACTFEL phosphors."))

    b.append(h2("94.7 Test Dot Characterization"))
    b.append(h3("Luminance and Efficiency"))
    b.append(p(
        "A schematic representation of a measurement system for collecting luminance and efficiency "
        "vs. voltage data on a test dot is shown in Fig. 94.7. An arbitrary waveform generator "
        "provides a drive signal with the waveshape, frequency, and peak voltage determined by a "
        "control computer. The waveform generator output signal is amplified from a ±5 V range to a "
        "±300 V range. A photometer, also under computer control, measures the luminance, <i>L</i>, "
        "of the test dot. An oscilloscope measures the voltage across the test dot and the voltage "
        "across the sense resistor. The current is calculated by dividing the voltage across the "
        "sense resistor by its resistance. The control computer can thus adjust the peak voltage up "
        "and down and collect the luminance data, as well as the waveforms representing the voltage "
        "across the test dot and the current through it. The energy dissipated, "
        "<i>E</i><sub>P</sub>, during each drive pulse is calculated as"))

    b.append(eq(_eq("94.1"), "94.1"))

    b.append(p(
        "where <i>I</i>(<i>t</i>) and <i>V</i>(<i>t</i>) are the current and voltage waveforms, "
        "respectively, and <i>D</i> is the duration of either the positive or negative drive pulse. "
        "This integration can be carried out by most oscilloscopes or the <i>I</i>(<i>t</i>) and "
        "<i>V</i>(<i>t</i>) data can be transferred to the control computer for the calculation, "
        "although this approach is generally slower. The average energy dissipated per period of the "
        "drive waveform, <i>E</i>, is the average of <i>E</i><sub>P</sub> for a positive pulse and a "
        "negative pulse. The average power dissipated, <i>P</i>, can be calculated by multiplying "
        "<i>E</i> by the frequency of the drive waveform. The efficiency, η, is calculated as "
        "follows:"))

    b.append(eq(_eq("94.2"), "94.2"))

    b.append(p(
        "where <i>L</i> is the luminance in cd/m<sup>2</sup>, <i>A</i> is the area of the test dot "
        "in m<sup>2</sup>, and <i>P</i> is the average power in watts. Values of <i>L</i> and η are "
        "collected for peak voltages ranging from 10 V below threshold to 40 or 50 V above threshold. "
        "Plots of <i>L</i> and η vs. peak voltage for a typical device are shown in Fig. 94.8."))
    b.append(fig(7, F.fig(7), "en"))
    b.append(fig(8, F.fig(8), "en"))
    b.append(h3("Charge Flow and Electric Field"))
    b.append(p(
        "The QV loop is measured using a circuit identical to that in Fig. 94.7, except that the "
        "sense resistor is replaced by a sense capacitor and the photometer is not used. The sense "
        "capacitor value is chosen to be much larger than the capacitance of the ACTFEL device so "
        "that the voltage dropped by the sense capacitor is small. Since the sense capacitor and the "
        "ACTFEL device are in series, the charges stored on them are equal. The charge, <i>Q</i>, on "
        "the ACTFEL device is thus"))

    b.append(eq(_eq("94.3"), "94.3"))

    b.append(p(
        "where <i>C</i><sub>S</sub> is the capacitance of the sense capacitor and "
        "<i>V</i><sub>S</sub> is the voltage appearing across it. When <i>Q</i>(<i>t</i>) is plotted "
        "vs. <i>v</i>(<i>t</i>), the QV loop results. In the idealized QV loop shown in Fig. 94.5, "
        "<i>V</i><sub>th</sub> (C) is the threshold voltage, <i>V</i><sub>to</sub> (B) is the turn "
        "on voltage, and <i>V</i><sub>P</sub> (D,E) is the peak voltage of the drive waveform. "
        "Threshold voltage is the voltage at which the first knee in the <i>LV</i> curve occurs. If "
        "<i>C</i><sub>T</sub> is the total capacitance of the device below threshold, this is also "
        "the voltage at which the line <i>Q</i> = <i>C</i><sub>T</sub><i>V</i> intersects the open, "
        "above-threshold QV loop (C). In practice, it is sometimes defined as the voltage at which a "
        "certain luminance value occurs at a given frequency, e.g., the voltage at which the "
        "luminance is 1 cd/m<sup>2</sup> at 60 Hz. <i>V</i><sub>to</sub> is the voltage at which the "
        "slope of the QV loop changes from <i>C</i><sub>T</sub> to <i>C</i><sub>I</sub>, where "
        "<i>C</i><sub>I</sub> is the capacitance of the insulator layers."))
    b.append(p(
        "Since a differential element of energy delivered to the ACTFEL device is d<i>E</i> = "
        "<i>V</i>(<i>t</i>)d<i>Q</i>, then"))

    b.append(eq(_eq("94.4"), "94.4"))

    b.append(p(
        "The energy delivered per period of the drive waveform is thus equal to the area encompassed "
        "by the QV loop. The power dissipated is just the energy per period multiplied by the "
        "frequency. In practice, the area of the QV loop is measured by numerical integration. The "
        "calculation can be carried out on the oscilloscope if it has analysis capabilities or the "
        "data can be transferred to the control computer for integration."))
    b.append(p(
        "Generation of the <i>Q</i><sub>P</sub><i>F</i><sub>P</sub> loop does not require any "
        "electrical measurements other than those required for the QV loop. <i>Q</i><sub>P</sub> is "
        "the charge separation across the phosphor layer and <i>F</i><sub>P</sub> is the electric "
        "field across the phosphor layer. If the thicknesses and dielectric constants of the "
        "insulator and phosphor layers are known, <i>Q</i><sub>P</sub> and <i>F</i><sub>P</sub> can "
        "be calculated from the values of <i>Q</i>(<i>t</i>) and <i>V</i>(<i>t</i>) on the QV loop. "
        "This is accomplished by applying the following equations [11,12]:"))

    b.append(eq(_eq("94.5"), "94.5"))
    b.append(p("and"))
    b.append(eq(_eq("94.6"), "94.6"))

    b.append(p(
        "where <i>C</i><sub>i</sub> is the capacitance of the insulators, <i>C</i><sub>P</sub> is "
        "the capacitance of the phosphor layer, and <i>d</i><sub>P</sub> is the thickness of the "
        "phosphor layer."))
    b.append(h3("Time-Resolved Measurements"))
    b.append(p(
        "The apparatus for measuring τ is shown in Fig. 94.9. A photomultiplier tube (PMT) is used to "
        "detect the light emission as a function of time. The drive system is set to provide "
        "relatively narrow drive pulses, typically 10 µs pulse width, at relatively low frequency, "
        "typically 60 Hz. This approach works well for phosphors with relatively long decay times, on "
        "the order of 100 µs to a few milliseconds. This is the case for many common ACTFEL phosphors "
        "such as ZnS:Mn and ZnS:Tb. Phosphors such as SrS:Ce, however, have very fast decay times and "
        "cannot be measured in this manner. In such cases the photoluminescent decay time must be "
        "measured using a pulsed laser to excite the phosphor and appropriately low RC response time "
        "of the light detection system."))
    b.append(p(
        "The general setup for measuring time-resolved emission spectra from ACTFEL devices is shown "
        "schematically in Fig. 94.10. The oscilloscope is triggered on the drive waveform and the "
        "signal integration period is set to the region of interest. A boxcar integrator can also be "
        "used to integrate the light signal during the desired time window. The monochrometer "
        "wavelength is scanned and the emission spectrum is collected for the selected portion of the "
        "emission process."))
    b.append(h3("Aging"))
    b.append(fig(9, F.fig(9), "en"))
    b.append(fig(10, F.fig(10), "en"))
    b.append(p(
        "ACTFEL devices tend to stabilize after a few tens of hours of burn-in, but can exhibit "
        "complex aging behavior during the burn-in process. The luminance vs. voltage curves for "
        "ZnS:Mn devices in which the phosphor layer is deposited by evaporation, for example, tend to "
        "shift to slightly higher voltage during burn-in [2]. Luminance vs. voltage curves for "
        "devices in which the ZnS:Mn is deposited by ALE tend to shift to slightly lower voltage "
        "[13]. Aging data is collected by measuring luminance vs. voltage at selected time intervals "
        "during aging. The measurement is carried out as described earlier for luminance vs. voltage "
        "measurements. The aging is done by continuously operating the device at a fixed voltage or "
        "at a fixed voltage above threshold. The aging process can be accelerated by operating the "
        "device at higher frequency."))

    b.append(h2("94.8 Characterization of Matrix-Addressed Displays"))
    b.append(p(
        "The characterization of matrix-addressed displays differs from characterization of test dots "
        "because less control of the drive waveform is readily available. The row and column drivers "
        "do not provide great flexibility, although some control can be exercised by varying the "
        "composite drive waveform and the control signals to the driver chips. These types of "
        "modifications, however, require detailed knowledge of the addressing and control electronics "
        "involved and are best left to the original display manufacturer."))
    b.append(p(
        "Measurements that are more accessible and of more general interest involve characterization "
        "of the luminance, chromaticity, uniformity, display life, latent image, and defects. For "
        "these measurements the display under test is controlled by a computer through a standard "
        "video output or a custom video display interface provided with the display. The display "
        "operating voltage and frequency are fixed. The display is placed in a dark room or "
        "enclosure. Luminance is measured with a photometer. Chromaticity is measured with a "
        "spectrophotometer or a photometer equipped with tristimulus filters. Uniformity can be "
        "measured by mounting either the display or the photometer/spectrophotometer on a translation "
        "system and collecting data at points in a regular array of locations throughout the display "
        "surface. Display life is characterized by operating the display in a full-on pattern, "
        "cycling through checkerboard patterns, etc., and making luminance measurements at "
        "exponentially increasing time intervals. Latent image is formed by displaying small blocks "
        "in various fixed locations and various fixed gray levels (if available) continuously for "
        "long periods. It is characterized by setting the entire screen to each gray level available "
        "and measuring the luminance in the locations which had blocks displayed during aging as well "
        "as unaged areas nearby. Latent image is the percent luminance difference between aged blocks "
        "and nearby unaged areas. Latent image is typically measured after aging the block pattern "
        "for 1000 h. Defects are classified into pixel, line, and mura defects. They are "
        "characterized by visual inspection with the aid of an eye loupe or by an automated flat "
        "panel inspection system."))

    b.append(h2("94.9 Excitation and Measurement Equipment"))
    b.append(h3("Excitation of Test Dots"))
    b.append(p(
        "Test dots can be excited by any signal source that provides bipolar pulses up to a peak "
        "voltage of 300 V and sufficient current sourcing and sinking capability to charge and "
        "discharge the device capacitance. Bipolar pulse drivers with sufficient voltage and current "
        "output can be built with commercially available components. A hybrid circuit op amp, "
        "produced by Apex Microtechnology, provides sufficient voltage output and frequency response. "
        "A current boosting stage can be added to the output if the DUT capacitance is too large to "
        "drive directly. This amplifier approach is very flexible since any waveform that can be "
        "generated by the arbitrary waveform generator can be used. There are also some commercial "
        "amplifiers available that are effective for driving test dots for some measurements. They "
        "tend to have limited bandwidth and must be used with caution in situations in which the "
        "measurement is sensitive to the exact shape of the drive pulse. This would be the case, for "
        "example, in QV measurements and often in efficiency measurements."))
    b.append(h3("Excitation of Matrix-Addressed Displays"))
    b.append(p(
        "Excitation of matrix-addressed displays is straightforward since the drive electronics are "
        "integrated with the display. Generally, only a standard ac power outlet and a computer with "
        "an appropriate video card are required. Test patterns for measurement can be created using "
        "simple computer programs."))

    b.append(h2("94.10 Measurement Instruments"))
    b.append(h3("Measurement of Drive Voltage and Current"))
    b.append(p(
        "Digital oscilloscopes are used for all of the electrical measurements described in this "
        "chapter. Suitable instruments are available from several manufacturers, including Tektronix "
        "and Hewlett-Packard. A bandwidth of 100 MHz is more than sufficient. Waveform analysis "
        "capabilities are very helpful but not absolutely necessary. RS-232 or IEEE 488 interfaces "
        "are required for computer control and data transfer."))
    b.append(h3("Measurement of Emitted Light"))
    b.append(p(
        "Several types of instruments are used for measuring light emission from ACTFEL displays. "
        "Photometers are used for luminance measurements. Spectrophotometers are used for measuring "
        "the emission spectrum and with suitable software can also provide luminance measurements. "
        "Time-resolved measurements are accomplished by using photomultiplier tubes or photodiode "
        "detectors. Table 94.1 lists some examples of photometers, spectroradiometers, "
        "photomultipliers, and photodiodes along with the names of the companies that manufacture "
        "them. A relatively new development for characterizing the light emission characteristics of "
        "flat panel displays, including ACTFEL displays, is the flat panel inspection system. This is "
        "a large measurement system comprising a CCD camera detector, light-tight enclosure, control "
        "computer, image processor, and specialized software. This type of system images an entire "
        "flat panel display on the CCD camera and measures luminance, chromaticity, and various "
        "defects by analyzing the image. These systems are intended for high throughput manufacturing "
        "environments and cost several hundred thousand dollars. An example of this type of system is "
        "also included in Table 94.1. Contact information for the companies listed in Table 94.1 is "
        "provided in Table 94.2."))

    hd1, rows1, cap1 = _table1("en")
    b.append(table(hd1, rows1, cap1))
    hd2, rows2, cap2 = _table2("en")
    b.append(table(hd2, rows2, cap2))

    b.append(h2("Defining Terms"))
    b.append(dt("Electroluminescence",
                "the nonthermal generation of light resulting from the application of an electric "
                "field to a substance, usually a luminescent crystal."))
    b.append(dt("Latent image",
                "the ghost image of a previously displayed pattern which can sometimes be seen in a "
                "full field on an electronic display screen."))
    b.append(dt("Light emission decay time",
                "the time it takes for the light emission from one excitation pulse to fall to "
                "1/<i>e</i> times its initial value."))
    b.append(dt("Polarization charge",
                "the charge trapped at the phosphor/insulator interface following the application of "
                "a drive pulse."))
    b.append(dt("Polarization field",
                "the field across the phosphor layer resulting from the polarization charge."))
    b.append(dt("<i>Q</i><sub>P</sub><i>F</i><sub>P</sub> loop",
                "the closed curve which results from plotting the internal charge flow across the "
                "phosphor layer (<i>Q</i><sub>P</sub>) vs. the electric field across the phosphor "
                "layer (<i>F</i><sub>P</sub>)."))
    b.append(dt("QV loop",
                "the closed curve which results from plotting the external charge (<i>Q</i>) flowing "
                "into a TFEL device vs. the externally applied voltage (<i>V</i>)."))
    b.append(dt("Threshold voltage",
                "the voltage amplitude of the drive waveform above which current flows across the "
                "phosphor layer and light is emitted from a TFEL device."))
    b.append(dt("Turn-on voltage",
                "the voltage corresponding to the first knee in the QV loop of a TFEL device. This "
                "is the voltage at which charge begins to flow across the phosphor layer. This "
                "voltage is generally less than the threshold voltage because the internal field "
                "across the phosphor layer is enhanced by the polarization field once the "
                "polarization charge has built up in the steady state."))

    b.append(h2("Translator's note"))
    b.append(note(
        "The original is a scan whose text layer lost several symbols, and it contains a few "
        "internal inconsistencies. Six points were handled as follows. <b>(1)</b> Greek letters and "
        "some signs were lost in the text layer: “5 to 15 W/square” is 5–15 Ω/square (the ohm sign "
        "became a W); “30 ms” in the Fig. 94.3 caption is 30 µs; “10 ms pulse width” in Section 94.7 "
        "is 10 µs; “100 ms to a few milliseconds” is 100 µs to a few milliseconds; “320 ´ 240” in "
        "Ref. [3] is 320 × 240. The units are restored here, since a 30 ms pulse at 60 Hz cannot fit "
        "inside a 16.7 ms frame. <b>(2)</b> Two Greek letters were replaced by Latin ones in the "
        "original: the efficiency “h” is η (including Eq. 94.2, printed as “h p = LA / P”), and the "
        "decay time “t” is τ. This translation uses η and τ. <b>(3)</b> The ITO thickness is printed "
        "as “350 and 120 nm”, an inverted range (350 > 120); it is left as printed, with the note "
        "that the plausible value is 35–120 nm, since a 350 nm ITO would be far too thick for the "
        "5–15 Ω/square sheet resistance quoted alongside it. <b>(4)</b> Two different drive pulse "
        "widths are quoted: 30 µs in the Fig. 94.3 caption and 10 µs in Section 94.7. Both are kept, "
        "as they refer to two different experiments (the illustrative waveform and the decay-time "
        "apparatus). <b>(5)</b> The order of the two markers <i>V</i><sub>to</sub> and "
        "<i>V</i><sub>th</sub>: the body text assigns <i>V</i><sub>to</sub> to point B and "
        "<i>V</i><sub>th</sub> to point C, and the Defining Terms block states that the turn-on "
        "voltage is generally less than the threshold voltage. Fig. 94.5 in this translation places "
        "the two ticks accordingly, i.e. the reverse of the left-to-right order in the original "
        "figure. <b>(6)</b> “Mura” is a Japanese term of art in the flat-panel industry for a "
        "blotchy, low-contrast non-uniformity; it has no settled Vietnamese equivalent and is kept "
        "untranslated, glossed as “khuyết tật vệt” (streak defect)."))

    b.append(h2("References"))
    b.append(refs(_REFS))

    return "".join(b)


# ================================================================ BUILD
def build(lang):
    vi = lang == "vi"
    switch = ("%s%s/" % (BASE_EN, CSLUG)) if vi else ("%s%s/" % (BASE_VI, CSLUG))
    title = ("Chương 94 — %s · Sổ tay Đo lường, Thiết bị đo và Cảm biến" % TITLE_VI if vi
             else "Chapter 94 — %s · Measurement, Instrumentation and Sensors Handbook" % TITLE_EN)
    desc = ("Bản dịch tiếng Việt Chương 94 “Hiển thị điện phát quang” của William A. Barrow — cấu "
            "trúc và chế tạo linh kiện EL màng mỏng xoay chiều, cơ chế điện phát quang, vòng QV và "
            "vòng QPFP, các phép đo độ chói, hiệu suất và phân giải thời gian, với 10 hình, 2 bảng "
            "và 6 phương trình." if vi
            else
            "Companion to Chapter 94 of the CRC Measurement Handbook — ACTFEL structure and "
            "fabrication, the electroluminescence mechanism, QV and QPFP loops, and luminance, "
            "efficiency and time-resolved measurements, with 10 figures, 2 tables and 6 equations.")
    crumb = ('<a href="/vi/books/">Sách</a> · <a href="%s">Sổ tay Đo lường, Thiết bị đo và Cảm biến</a> · '
             'Chương 94' % BASE_VI if vi else
             '<a href="/books/">Books</a> · <a href="%s">Measurement, Instrumentation and Sensors '
             'Handbook</a> · Chapter 94' % BASE_EN)
    meta = ("Chương 94 · theo Ch94.pdf (CRC Press, 1999) · 10 hình, 2 bảng, 6 phương trình" if vi else
            "Chapter 94 · 10 figures, 2 tables, 6 equations")
    body = ('<main><article class="intranet-content reader"><div class="reader-hero">'
            '<div class="breadcrumb">%s</div><h1>%s</h1><p class="byline">%s</p>'
            '<div class="meta-line">%s</div></div><div class="prose">%s</div>%s</article></main>'
            % (crumb, TITLE_VI if vi else TITLE_EN, BYLINE, meta,
               body_vi() if vi else body_en(), chapter_nav(lang, 94)))
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
