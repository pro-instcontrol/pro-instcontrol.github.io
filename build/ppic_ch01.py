# -*- coding: utf-8 -*-
"""Book 9, Chapter 1 - The Effect of Different Parameters on the Efficiency
of the Catalytic Reduction of Dissolved Oxygen (EN/VI bilingual).

Source: L. N. Jalali (ed.), *Handbook on Power Plant Instrumentation and
Control* (Bibliotex, 2019), PDF pp. 17-28, printed pp. 1-12 (PDF p. 28 is
blank).  PAGES_SRC = 12 counts the assigned source span.

The chapter has five numbered figures (Figure 1 - Figure 5), redrawn as
vectors in `ppicfig.py`, and four numbered tables (Table 1 - Table 4),
reproduced here from the printed pages.  The three chemical equations and
the table data exist only as images in the text layer; the equations are
rendered symbolically in place and the tables are transcribed from the
page images.
"""

import ppic_common as C          # noqa: F401  (page shell, used by C.build)
import ppicfig as F
from ppic_common import (eq, fig, h2, h3, lead, note, ol, p, refs, table, ul)

PAGES_SRC = 12
BYLINE = ("Adnan Moradian · Farid Delijani · Fateme Ekhtiary Koshky · "
          "Handbook on Power Plant Instrumentation and Control (Bibliotex, 2019)")
TITLE_EN = "The Effect of Different Parameters on the Efficiency of the Catalytic Reduction of Dissolved Oxygen"
TITLE_VI = "Ảnh hưởng của các thông số khác nhau đến hiệu quả khử xúc tác oxy hòa tan"


# ---------------------------------------------------------------------------
# Reference list (source printed pp. 10-11).  Citation text is kept as printed.
# ---------------------------------------------------------------------------
_REFS = [
    "Martinola, F. B, &amp; Thomas, P. Saving Energy by Catalytic Reduction of Oxygen in "
    "Feedwater”, 45th International Water Conference, Eng. Soc. Pittsburgh,PA, ((1980).",
    "Chua, I, Tai, M. S. L, Li, K, Zhang, H, Sourirajan, S, Ng, W. J, &amp; Teo, W. K. "
    "Ultrapure water quality and production for industrial uses”, Journal of The "
    "Institution of Engineers ((1993).",
    "Li, K, Chua, I, Ng, W. J, &amp; Teo, W. K. Removal of dissolved oxygen in ultrapure "
    "water production using a membrane reactor”, Chem. Eng.Sci. (1995). , 50(1995), "
    "3547-3556.",
    "Tan, X, Capar, G, &amp; Li, K. Analysis of dissolved oxygen removal in hollow fibre "
    "membrane modules: effect of water vapour”, Journal of Membrane Science (2005). , "
    "251(2005), 111-119.",
    "Li, K, &amp; Tan, X. Development of membrane-UV reactor for dissolved oxygen removal "
    "from water”, Chem. Eng. Sci. (2001). , 56(2001), 5073-5083.",
    "Moon, J. S, Park, K. K, Kim, J. H, &amp; Seo, G. Reductive removal of dissolved oxygen "
    "in water by hydrazine over cobalt oxide catalyst supported on activated carbon fiber”, "
    "Appl. Catal. A-Gen. (2000). , 201(2000), 81-89.",
    "Butler, I. B, Schoonen, M. A. A, &amp; Rickard, D. T. Removal of dissolved oxygen from "
    "water: A comparison of four common techniques”,Talanta (1994). , 41(1994), 211-215.",
    "Ito, A, Yamagiwa, K, Tamura, M, &amp; Furusawa, M. Removal of dissolved oxygen using "
    "non-porous hollow-fiber membranes”, J. Membrane Sci. (1998). , 145(1998), 111-117.",
    "Tan, X, &amp; Li, K. Investigation of novel membrane reactors for removal of dissolved "
    "oxygen from water”,Chem. Eng. Sci. (2000). , 55(2000), 1213-1224.",
    "Suppiah, S, Kutchcoskie, K. J, Balakrishnan, P. V, &amp; Chuang, K. T. Can.” Dissolved "
    "oxygen removal by combination with hydrogen using wetproofed catalysts”, J. of Chem. "
    "Eng., 66, ((1988).",
    "Moradian, A, &amp; Delijani, F. F.Ekhtiary Koshky, “ The Effect of Contact Time and "
    "concentration of Oxygen on the Efficiency of the Catalytic Reduction of Dissolved "
    "Oxygen”, J. of Middle-East journal of scientific research., (2012). , 11(2012), "
    "1036-1040.",
    "LANXESS Energizing Chemistry: wwwlanxess.com",
]


# ---------------------------------------------------------------------------
# Tables 1-4.  Both language versions share the same numeric rows; only the
# column headings are localized.  Grouped headings use <br> inside the <th>.
# ---------------------------------------------------------------------------
def _tbl_header(vi):
    if vi:
        return ["Mẫu", "Thời gian lấy mẫu (phút)", "Oxy hòa tan đầu vào (ppm)",
                "Nhiệt độ (°C)<br>Cột trộn", "Nhiệt độ (°C)<br>Lò phản ứng xúc tác",
                "Áp suất (bar)<br>Cột trộn", "Áp suất (bar)<br>Lò phản ứng xúc tác",
                "Áp suất cấp hydro (bar)", "Lưu lượng nước (lít/giờ)",
                "Oxy hòa tan còn lại (ppb)"]
    return ["Sample No.", "Sampling Time (min)", "Inlet Dissolved Oxygen (ppm)",
            "Temperature (°C)<br>Mixing Column",
            "Temperature (°C)<br>Catalytic Reactor",
            "Pressure (bar)<br>Mixing Column",
            "Pressure (bar)<br>Catalytic Reactor",
            "Hydrogen Injection Pressure (bar)", "Water flow rate (lit/hr)",
            "Remaining dissolved Oxygen (ppb)"]


_TBL1 = [
    ["1", "35", "7.2", "22", "23", "1.5", "1.5", "2", "120", "8"],
    ["2", "40", "6.9", "22", "23", "1.5", "1.5", "2", "120", "6"],
    ["3", "45", "6.2", "22", "23", "1.5", "1.5", "2", "120", "5"],
    ["4", "50", "5.8", "22", "23", "1.5", "1.5", "2", "120", "4"],
    ["5", "55", "5.2", "22", "23", "1.5", "1.5", "2", "120", "4"],
    ["6", "60", "4.6", "22", "23", "1.5", "1.5", "2", "120", "4"],
    ["7", "65", "4.1", "22", "24", "1.5", "1.5", "2", "120", "3"],
    ["8", "80", "3.5", "22", "24", "1.5", "1.5", "2", "120", "2"],
]

# The source cells print "28"/>" and "24"/>" - a typesetting artifact for
# values above the instrument range, read here as >28 and >24 ppb.
_TBL2 = [
    ["1", "35", "7.2", "22", "22", "1.5", "1.5", "2", "240", "&gt;28"],
    ["2", "40", "6.8", "23", "23", "1.5", "1.5", "2", "240", "&gt;28"],
    ["3", "45", "6.1", "23", "23", "1.5", "1.5", "2", "240", "&gt;28"],
    ["4", "50", "5.8", "23", "23", "1.5", "1.5", "2", "240", "&gt;28"],
    ["5", "55", "5.1", "23", "23", "1.5", "1.5", "2", "240", "&gt;24"],
    ["6", "60", "4.5", "24", "23", "1.5", "1.5", "2", "240", "22"],
    ["7", "65", "4", "24", "24", "1.5", "1.5", "2", "240", "16"],
    ["8", "70", "3.5", "25", "24", "1.5", "1.5", "2", "240", "10"],
]

_TBL3 = [
    ["1", "40", "4.5", "24", "24", "1.5", "1.5", "2", "240", "26"],
    ["2", "45", "4.6", "26", "26", "1.6", "1.6", "2", "240", "22"],
    ["3", "50", "4.5", "28", "28", "1.7", "1.7", "2", "240", "20"],
    ["4", "55", "4.6", "30", "30", "1.8", "1.8", "2.1", "240", "18"],
    ["5", "60", "4.5", "32", "32", "1.8", "1.8", "2.2", "240", "17"],
    ["6", "65", "4.5", "34", "34", "2", "2", "2.3", "240", "15"],
    ["7", "70", "4.6", "36", "36", "2.1", "2.1", "2.4", "240", "13"],
    ["8", "75", "4.5", "40", "40", "2.2", "2.2", "2.5", "240", "12"],
]

_TBL4 = [
    ["1", "40", "1", "24", "24", "1", "1", "2", "640", "&gt;28"],
    ["2", "45", "1.1", "24", "24", "1.1", "1.1", "2", "640", "&gt;28"],
    ["3", "50", "1", "25", "25", "1.2", "1.2", "2", "640", "&gt;28"],
    ["4", "55", "1.1", "25", "25", "1.3", "1.3", "2", "640", "&gt;28"],
    ["5", "60", "1", "26", "26", "1.4", "1.4", "2", "640", "&gt;28"],
    ["6", "70", "1", "27", "27", "1.5", "1.5", "2", "640", "28"],
    ["7", "80", "1", "27", "27", "1.6", "1.6", "2", "640", "26"],
    ["8", "90", "1", "28", "28", "1.7", "1.7", "2", "640", "22"],
]


def note_terms(lang):
    if lang == "vi":
        return ("<b>Thuật ngữ chính.</b> oxy hòa tan — dissolved oxygen (DO) · khử xúc tác — "
                "catalytic reduction · hiệu quả — efficiency · lưu lượng nước — water flow rate · "
                "thời gian tiếp xúc — contact time · thời gian lưu — residence time · cột trộn — "
                "mixing column · lò phản ứng xúc tác — catalytic reactor · nhựa xúc tác — resin "
                "catalyst · định luật Henry — Henry's law · hằng số Henry — Henry constant · "
                "hòa tan — solution · nước đã xử lý — treated water · phần triệu — ppb · "
                "phần triệu (ppm) — ppm.")
    return ("<b>Key terms.</b> dissolved oxygen (DO) · catalytic reduction · efficiency · water "
            "flow rate · contact time · residence time · mixing column · catalytic reactor · "
            "resin catalyst · Henry's law · Henry constant · solution · treated water · ppb · ppm.")


# ===========================================================================
def _body(lang):
    vi = lang == "vi"
    b = []

    def P(v, e):
        b.append(p(v if vi else e))

    def H(v, e, lvl=h2):
        b.append(lvl(v if vi else e))

    def U(v, e):
        b.append(ul(v if vi else e))

    def FIG(n, fn):
        b.append(fig(n, fn))

    def TB(header, rows):
        b.append(table(header, rows))

    # ---------------------------------------------------------------- lead
    b.append(lead(
        "Chương này khảo sát ảnh hưởng của các thông số vận hành — nhiệt độ, áp suất, lưu lượng "
        "nước, thời gian tiếp xúc và nồng độ oxy hòa tan đầu vào — đến hiệu quả khử xúc tác oxy "
        "hòa tan bằng hydro có mặt nhựa xúc tác, và trình bày kết quả thí nghiệm dưới dạng năm "
        "đồ thị và bốn bảng."
        if vi else
        "This chapter examines how operating parameters - temperature, pressure, water flow "
        "rate, contact time and inlet dissolved-oxygen concentration - affect the efficiency "
        "of the catalytic reduction of dissolved oxygen by hydrogen over a resin catalyst, "
        "and reports the experimental results in five graphs and four tables."))

    # ---------------------------------------------------------------- 1.1
    H("1.1 Mở đầu", "1.1 Introduction")
    P("Nhiều thiết bị, đặc biệt là bộ sinh hơi của lò phản ứng điện hạt nhân và cuộn dây stato "
      "làm mát bằng nước trong máy phát tua-bin, bị ăn mòn ở nhiều dạng khác nhau do sự hiện diện "
      "của oxy hòa tan [1]. Việc loại bỏ oxy hòa tan (DO) khỏi nước là một công đoạn cần thiết "
      "trong nhiều ngành công nghiệp, bao gồm dược phẩm, thực phẩm, điện và bán dẫn. Mức DO chấp "
      "nhận được thay đổi tùy theo mục đích sử dụng của nước; ví dụ, trong ngành điện, việc loại "
      "bỏ DO là cần thiết để ngăn ngừa ăn mòn trong nồi hơi và đường ống, và cần mức khoảng 5 ppm. "
      "Ngược lại, nước siêu tinh khiết như dùng để rửa tấm wafer silicon trong công nghiệp bán dẫn "
      "có thể là trường hợp khắt khe nhất về mức DO, với một số ứng dụng yêu cầu mức cực thấp "
      "khoảng 0,1 ppb [2, 3].",
      "Many equipment, in particular steam generators of power reactors and water cooled stator "
      "windings in turbine generators, suffer from various forms of corrosion induced by the "
      "presence of dissolved Oxygen [1]. Removal of dissolved Oxygen (DO) from water is a "
      "necessary process in many industries including pharmaceutical, food, power and "
      "semiconductor. Acceptable levels of DO vary depending on the intended use of the water; "
      "in the power industry, for example, removal of DO is necessary to prevent corrosion in "
      "boilers and pipes, and levels of around 5 ppm are necessary. In comparison, ultrapure "
      "water, as used in the washing of silicon wafers in the semiconductor industry, is perhaps "
      "the most demanding in terms of DO level with some applications requiring extremely low "
      "DO levels of around 0.1 ppb [2, 3].")
    P("Oxy hòa tan có thể được loại bỏ khỏi nước bằng nhiều phương pháp, được xếp rộng rãi thành "
      "các hệ thống hóa học, vật lý và lai (hybrid) sử dụng sự kết hợp của các phương pháp này. "
      "Các phương pháp vật lý được dùng gồm khử khí nhiệt, khử khí chân không hoặc khử khí bằng "
      "bọt nitơ, theo truyền thống được thực hiện trong các tháp đệm. Nhược điểm của các phương "
      "pháp này gồm chi phí vận hành cao và diện tích bề mặt nhỏ trên một đơn vị thể tích. Với các "
      "phương pháp vật lý này, khó giảm nồng độ DO từ mức mg/L xuống mức μg/L. Các phương pháp vật "
      "lý có những thiếu sót cố hữu là cồng kềnh, tốn kém và thiếu linh hoạt trong vận hành [4]. "
      "Gần đây, thiết bị tiếp xúc màng sợi rỗng với hiệu suất cao và một số ưu điểm khác đã được "
      "dùng để loại bỏ oxy hòa tan, nhưng việc sử dụng vẫn chưa phổ biến [5]. Các phương pháp hóa "
      "học như dùng natri sunfit, hydrazin, carbohydrazide, β-ketogluconate và axit gallic, hoặc "
      "khử xúc tác, có nhược điểm đáng kể là đưa thêm một tạp chất thường có độc vào hệ thống "
      "[6, 7].",
      "Dissolved Oxygen can be removed from water using a variety of methods broadly grouped "
      "into chemical, physical and hybrid systems, which make use of a combination of these "
      "methods. Physical methods used including thermal degassing, vacuum degassing or nitrogen "
      "bubble deaerations are traditionally carried out in packed towers. Disadvantages with "
      "these methods include high operating costs and a small surface area per unit volume. "
      "Using these physical methods, it is difficult to reduce the DO concentration from mg/L "
      "to μg/L levels. Physical methods have inherent deficiencies of being bulky, costly and "
      "inflexible in operation [4]. Recently, hollow fiber membrane contactor with high "
      "efficiency and some other advantages have been utilized to remove dissolved Oxygen but "
      "their use is still not common [5]. Chemical methods such as the use of sodium sulphite "
      "hydrazine, carbohydrazide, β-ketogluconate, and gallic acid or catalytic reduction offer "
      "a significant disadvantage in that a further, often toxic, impurity is introduced into "
      "the system [6, 7].")
    P("Natri sunfit là một tác nhân khác để loại bỏ oxy có sẵn trong công nghiệp, vì thế nó được "
      "dùng trong các hệ thống áp suất thấp. Dùng natri sunfit ở áp suất cao gặp hai vấn đề. Thứ "
      "nhất, việc tiêu thụ tác nhân này làm tăng lượng chất rắn trong hệ thống nồi hơi tuần "
      "hoàn, nơi việc kiểm soát thông số này trong phạm vi thích hợp lại quan trọng hơn. Thứ hai, "
      "ở nồi hơi áp suất cao, natri sunfit phân hủy tạo thành lưu huỳnh dioxide hoặc hydro "
      "sulfide; cả hai đều là khí ăn mòn, đi ra cùng hơi nước từ nồi hơi, làm pH của hơi và nước "
      "ngưng thấp và gây ăn mòn trong toàn hệ thống.",
      "Sodium sulfite is another agent for Oxygen removal available in the industry which "
      "accounts for its use in low pressure systems. Using Sodium Sulfite at high pressure faces "
      "two problems. At first, the consumption of this agent increase solids in the circulating "
      "boiler system where the controlling of this parameter at proper range is more important. "
      "Second, at high pressure boilers, Sodium sulfite breaks down to form Sulfur dioxide or "
      "Hydrogen Sulfide those both are corrosive gases which leave the boiler with steam "
      "resulting in low pH steam and condensate and cause the corrosion throughout the system.")
    P("Hydrazin (N<sub>2</sub>H<sub>4</sub>) là một tác nhân khử mạnh phản ứng với oxy hòa tan để "
      "tạo thành nitơ và nước như sau:",
      "Hydrazine (N<sub>2</sub>H<sub>4</sub>) is a powerful reducing agent that reacts with "
      "dissolved Oxygen to form nitrogen and water as follows:")
    b.append(eq("N<sub>2</sub>H<sub>4</sub> + O<sub>2</sub> ⇒ N<sub>2</sub> + 2H<sub>2</sub>O"))
    P("Ở nhiệt độ và áp suất cao, amonia cũng được tạo ra, làm tăng pH nước cấp và giảm nguy cơ "
      "ăn mòn axit. Hydrazin cũng phản ứng với lớp hematit mềm trên ống nồi hơi và tạo thành lớp "
      "magnetit cứng, về sau bảo vệ ống nồi hơi khỏi ăn mòn tiếp theo. Điều này xảy ra nhờ phản "
      "ứng hóa học:",
      "At high temperature and pressure, ammonia is also formed, which increases the feedwater "
      "pH level, reducing the risk of acidic corrosion. Hydrazine also reacts with soft "
      "haematite layers on the boiler tubes and forms a hard magnetite layer, which subsequently "
      "protects the boiler tubes from further corrosion. This occurs as a result of the "
      "chemical reaction:")
    b.append(eq("N<sub>2</sub>H<sub>4</sub> + 6Fe<sub>2</sub>O<sub>3</sub> ⇒ "
                "4Fe<sub>3</sub>O<sub>4</sub> + N<sub>2</sub> + 2H<sub>2</sub>O"))
    P("Vì vậy, để giảm hoặc loại bỏ amonia, nên giảm hoặc ngừng việc phun hydrazin. Gần đây, việc "
      "dùng hydro có mặt chất xúc tác là một phương pháp hấp dẫn; tái kết hợp xúc tác oxy hòa tan "
      "với hydro để tạo thành nước là phương pháp hấp dẫn vì không tạo sản phẩm phụ [8, 9]. Hơn "
      "nữa, phương pháp xúc tác có thể giảm mức oxy xuống dưới một phần tỷ [10]. Trong nghiên cứu "
      "này, việc loại bỏ oxy hòa tan trong nước bằng phương pháp khử xúc tác đã được điều tra. "
      "Ngoài ra, các điều kiện vận hành như nhiệt độ, áp suất, lưu lượng nước, thời gian tiếp xúc "
      "và nồng độ oxy hòa tan đầu vào đã được nghiên cứu về ảnh hưởng đến hiệu quả khử xúc tác oxy "
      "hòa tan. Một phần kết quả của công trình này đã được công bố trên Tạp chí Quốc tế MEJSR "
      "[11].",
      "Thus in order to reduce or remove the Ammonia, the injection of hydrazine should be "
      "reduced or stopped. Recently use of Hydrogen in the presence of catalyst is an "
      "attractive method; catalytically recombining the dissolved Oxygen with Hydrogen to form "
      "water is an attractive method, as it produces no byproduct [8,9]. Also, the catalytic "
      "method can reduce Oxygen levels below one part per billion [10]. In this study removal "
      "of dissolved Oxygen in water through reduction catalytic method, was investigated. Also "
      "the operation condition such as temperature, pressure, flow rate of water, contact time "
      "and inlet dissolved Oxygen concentration was studied on the efficiency of the catalytic "
      "reduction of dissolved Oxygen. The part of the results of this work has been published "
      "in International Journal of MEJSR [11].")

    # ---------------------------------------------------------------- 1.2
    H("1.2 Khử xúc tác oxy hòa tan", "1.2 Catalytic Reduction of Dissolved Oxygen")
    P("Trong quá trình khử xúc tác oxy hòa tan, hydro và oxy phản ứng với nhau có mặt chất xúc "
      "tác để tạo thành nước:",
      "In the process of catalytic reduction of dissolved Oxygen, Hydrogen and Oxygen react in "
      "the presence of a catalyst to produce water:")
    b.append(eq("O<sub>2</sub> + 2H<sub>2</sub> → 2H<sub>2</sub>O\u00a0\u00a0\u00a0"
                "ΔH = −68.3 kcal/mol"))
    P("Sản phẩm của phản ứng là nước, không có tác động bất lợi đến hệ thống. Một thiết bị thí "
      "nghiệm đã được chế tạo để khảo sát các thông số ảnh hưởng đến quá trình khử xúc tác oxy "
      "hòa tan. Hình (1) cho thấy tổng quan của quá trình này. Nước được bơm từ bình chứa đến bộ "
      "trộn hydro/nước. Bộ trộn là một giường đệm dòng khí-lỏng đi lên cùng chiều. Nước đã bão "
      "hòa cả oxy lẫn hydro sau đó đi vào bình nhựa xúc tác, nơi hydro và oxy phản ứng có mặt "
      "chất xúc tác. Phản ứng được xúc tác bằng 1,5 lít nhựa xúc tác K6333 (Công ty Lanxess [12]). "
      "Tất cả kết quả thu được trong các điều kiện sau:",
      "The production of reaction is water that has no adverse effect on the system. An "
      "experimental setup was constructed to investigate the effective parameters in the "
      "catalytic reduction of dissolved Oxygen. Figure (1) shows the overview of this process. "
      "Water is pumped from the water tank to the Hydrogen/water mixer. The mixer is a "
      "concurrent gas–liquid upflow packed bed. The water saturated both with Oxygen and "
      "Hydrogen then enters the catalytic resin vessel where the Hydrogen and Oxygen react in "
      "presence of the catalyst. The reaction is catalyzed using 1.5 liter of K6333 resin "
      "catalyst (Lanxess Co. [12]). All results have been obtained under the following "
      "conditions:")
    U(["Áp suất vận hành: 2-3 bar",
       "Để xác định oxy còn lại trong sản phẩm, dùng ASTM D888-81",
       "Khí hydro có độ tinh khiết 99,99%"],
      ["Operating pressure: 2- 3 bar",
       "For determination of remaining Oxygen in the product, used of ASTM D888-81",
       "Hydrogen gas with 99.99% purity"])
    FIG(1, F.fig_f01())

    # ---------------------------------------------------------------- 1.3
    H("1.3 Kết quả và thảo luận", "1.3 Results and Discussion")
    H("Ảnh hưởng của nhiệt độ và áp suất", "Effect of Temperature and Pressure", h3)
    P("Để đạt được điều kiện vận hành tối ưu, nhiều thí nghiệm đã được thực hiện ở các áp suất và "
      "nhiệt độ khác nhau. Như thể hiện trong Hình (2), dải nhiệt độ thích hợp cho hệ thống này "
      "là giữa 10-50 °C. Ở nhiệt độ thấp hơn 10 °C, hiệu quả và sự hấp thụ oxy sẽ giảm. Điều này "
      "là do ở nhiệt độ thấp, phản ứng giữa oxy và hydro không còn có thể xảy ra và chất xúc tác "
      "không có khả năng tăng tốc phản ứng này. Mặt khác, tăng nhiệt độ cao hơn 50 °C có thể gây "
      "hư hỏng chất xúc tác.",
      "In order to achieve optimum operation condition, various experimental is implemented at "
      "different pressures and temperatures. As shown in Figure (2) the proper temperature "
      "range for this system is between 10-50 °C. At temperature lower than 10 °C, the "
      "efficiency and the absorption of Oxygen would be reduced. This is due to the fact that at "
      "low temperature, the reaction between Oxygen and Hydrogen is no more possible and the "
      "catalyst is not able to accelerate this reaction. In other hand further increase in "
      "temperature upper than 50 °C may cause damage in the catalyst.")
    FIG(2, F.fig_f02())
    P("Ngoài ra, như có thể thấy trong Hình (3), dải áp suất thích hợp cho quá trình này là giữa "
      "1,7-3 atm. Như đã mô tả trước đó, sự hòa tan của hydro trong nước là hàm của áp suất theo "
      "định luật Henry. Hằng số Henry đối với dung dịch hydro là (7,07 × 10<sup>4</sup> "
      "atm.mol H<sub>2</sub>O/mol H<sub>2</sub> (25 °C)), do đó sự hòa tan của khí này trong "
      "nước diễn ra chậm, cho thấy áp suất tối thiểu cần thiết để duy trì quá trình ở pha lỏng. "
      "Các kết quả này cũng cho thấy ở nhiệt độ cao hơn thì áp suất phải cao hơn so với ở nhiệt "
      "độ thấp. Dù sao, sự gia tăng hòa tan hydro theo áp suất làm hiệu quả hệ thống được cải "
      "thiện.",
      "Also as can be seen in Figure (3), the appropriate pressure range for this process is "
      "between 1.7-3 atm. As previously described the solution of Hydrogen in water is a "
      "function of the pressure based on Henry’s law. The Henry constant for Hydrogen solution "
      "is (7.07 ×104 atm.mo1 H2O/mo1H2 (25°C)), therefore the solution of this gas in water take "
      "places slowly, Indicating that the minimum pressure required to maintain the process in a "
      "liquid phase. These results also show that at upper temperatures, the pressure should be "
      "higher than that at low temperatures. Anyway the increase of Hydrogen solution with "
      "pressure results in the system efficiency improvement.")
    FIG(3, F.fig_f03())

    H("Ảnh hưởng của lưu lượng nước", "Effect of Water Flow Rate", h3)
    P("Các thí nghiệm khác được thực hiện để minh họa ảnh hưởng của lưu lượng nước. Trước hết, "
      "mức oxy đầu vào được giảm trong khi các thông số khác giữ không đổi. Kết quả thể hiện "
      "trong Bảng (1) cho thấy trong trường hợp này oxy còn lại không vượt quá mức giới hạn khi "
      "lưu lượng nước là 120 lít/giờ. Trong thí nghiệm khác, lưu lượng nước được tăng lên "
      "240 lít/giờ và các thông số khác không đổi. Trong điều kiện này, như có thể thấy trong "
      "Bảng (2), có thể giảm oxy hòa tan bằng cách tăng lưu lượng nước ở mức oxy đầu vào thấp. "
      "Trong điều kiện đó, quá trình trở nên hiệu quả hơn.",
      "Other experiments are implemented to illustrate the effect of water flow rate. At first, "
      "the inlet Oxygen level is reduced while other parameters remain constant. The results "
      "shown in Table (1) indicate that in this case the remaining Oxygen is not upper than the "
      "limited level when the water flow rate is 120 lit/hr. In other experiment the water flow "
      "rate would be 240 lit/hr and other parameters are constant. In this condition as can be "
      "seen in Table (2), it is possible to reduce dissolved Oxygen by means of increasing the "
      "water flow rate at low inlet Oxygen level. In this condition the process would be more "
      "efficient.")
    P("<b>Bảng 1.</b> Hiệu quả của hệ thống ở các giá trị oxy đầu vào khác nhau.",
      "<b>Table 1.</b> The performance of system at various values of inlet Oxygen.")
    TB(_tbl_header(vi), _TBL1)
    P("<b>Bảng 2.</b> Ảnh hưởng của việc tăng lưu lượng nước.",
      "<b>Table 2.</b> The effect of increasing of water flow rate.")
    TB(_tbl_header(vi), _TBL2)
    P("Ngoài ra, hiệu quả của hệ thống cũng được khảo sát ở mức oxy đầu vào cao hơn bằng cách "
      "thiết lập điều kiện khác cho kết quả của Bảng (2). Ví dụ, khi oxy đầu vào có giá trị 4,5 "
      "ppm, mức oxy còn lại cao hơn mức giới hạn (22 ppb). Trong trường hợp này, mức oxy đầu vào "
      "và lưu lượng nước được giữ không đổi và các điều kiện khác đã được thay đổi một cách có "
      "hiệu quả. Như thể hiện trong Bảng (3), hiệu quả của hệ thống đã được cải thiện khi tăng "
      "cả áp suất và nhiệt độ, nên mức oxy còn lại đạt thấp hơn 20 ppb, nhưng những thay đổi này "
      "diễn ra dần dần và chậm. Điều này có thể giải thích bằng thực tế là tăng áp suất chỉ có "
      "tác động đến một giá trị nhất định và tăng thêm sau đó chỉ gây hòa tan thêm hydro mà không "
      "ảnh hưởng đến hiệu quả hệ thống.",
      "Also the performance of system is investigated at higher level of inlet Oxygen by "
      "providing other condition for the results of Table (2). For example when the inlet "
      "Oxygen has value of 4.5 ppm, the remaining Oxygen level is upper than limited level "
      "(22 ppb). In this case the level of inlet Oxygen and the flow rate of water are "
      "maintained constant and other condition have been effectively changed. As shown in Table "
      "(3), the performance of system has been improved with increasing both the pressure and "
      "temperature, so the remaining Oxygen level reaches lower than 20 ppb but these changes "
      "occurred gradually and slowly. This could be explained by the fact that the pressure "
      "increasing is effective only to a certain value and further increase after that only "
      "cause the further solution of Hydrogen without any effect on the system performance. In")
    P("Ở mặt khác, mặc dù tăng nhiệt độ có lợi cho phản ứng giữa hydro và oxy, nhưng tăng nhiệt độ "
      "cao hơn 50 có tác động ngược đến sự hòa tan hydro trong nước và bất kỳ sự tăng nhiệt độ "
      "nào ở áp suất không đổi đều làm giảm hòa tan hydro.",
      "other hand, although the increase of temperature is effective for reaction of Hydrogen "
      "and Oxygen but the increase of temperature higher than 50 has an inverse effect on "
      "Hydrogen solution in water and any increase of temperature at constant pressure results "
      "in reduction of Hydrogen solution.")
    P("<b>Bảng 3.</b> Ảnh hưởng của các thông số khác đến hiệu quả hệ thống (mức oxy đầu vào: "
      "4,5 ppm).",
      "<b>Table 3.</b> The effect of other parameters on system performance (inlet Oxygen "
      "level: 4.5 ppm)")
    TB(_tbl_header(vi), _TBL3)

    # ---------------------------------------------------------------- 1.4
    H("1.4 Hiệu quả của hệ thống ở mức oxy đầu vào thấp và lưu lượng nước cao",
      "1.4 The System Performance in Low Level of Inlet Oxygen and High Water Flow Rate")
    P("Để khảo sát hiệu quả của hệ thống ở mức oxy đầu vào thấp và lưu lượng nước cao, một thí "
      "nghiệm khác được thực hiện với giá trị oxy đầu vào 1 ppm và lưu lượng nước 640 lít/giờ. "
      "Kết quả liệt kê trong Bảng (4) cho thấy oxy hòa tan giảm theo thời gian. Tuy nhiên, thời "
      "gian lưu giảm ở cả tháp hydro và tháp xúc tác do lưu lượng nước tăng. Vì vậy, trong điều "
      "kiện này, thời gian là không đủ để hydro hòa tan hoàn toàn và phản ứng với oxy. Ví dụ, "
      "sau 75 phút, oxy còn lại là 22 ppb trong khi thời gian đủ cho sự khử này đã đạt được gần "
      "30 phút trước đó.",
      "In order to investigate the system performance in low level of inlet Oxygen and high "
      "water flow rates, another experiment is implemented with the value of 1ppm of inlet "
      "Oxygen and the water flow rate of 640 lit/hr. The results listed in Table (4) show the "
      "reduction of dissolved Oxygen with time. However the residence time is reduced in both "
      "Hydrogen and catalytic towers because of increasing in water flow rate. Thus under this "
      "condition, the time is not enough for complete solution of Hydrogen and reaction with "
      "Oxygen. For example after 75 min, the remaining Oxygen is 22 ppb while the sufficient "
      "time for this reduction has obtained almost 30 min before.")
    P("<b>Bảng 4.</b> Hiệu quả của hệ thống ở mức oxy đầu vào thấp và lưu lượng nước cao.",
      "<b>Table 4.</b> The system performance in low level of inlet Oxygen and high water flow rate")
    TB(_tbl_header(vi), _TBL4)

    H("Ảnh hưởng của thời gian tiếp xúc", "Effect of Contact Time", h3)
    P("Một thông số quan trọng để điều khiển quá trình là thời gian tiếp xúc, chịu ảnh hưởng của "
      "kích thước cột, thể tích nhựa và vận tốc tuyến tính của nước. Thực chất, thời gian tiếp "
      "xúc là thời gian lưu của chất lỏng trong cột xúc tác, tại đó DO trên bề mặt xúc tác phản "
      "ứng với hydro. Kết quả thí nghiệm trong các điều kiện khác nhau được thể hiện trong Hình "
      "(4). Trong mọi điều kiện, hiệu quả là mức hấp thụ oxy so với lượng oxy hòa tan đầu vào "
      "trong nước.",
      "An important parameter to control the process is the contact time that influenced by "
      "column dimensions, volume of resin and the linear velocity of water. In fact the contact "
      "time is fluid residence time in the catalyst column in which DO on the catalyst surface "
      "reacts with Hydrogen. The results of experiments in different conditions are shown in "
      "Figure (4). In all conditions efficiency is the Oxygen absorption relative to the input "
      "of dissolved Oxygen in water.")
    P("Như thấy trong Hình 4, với thời gian tiếp xúc dưới 45 giây, không thể giảm oxy hòa tan "
      "xuống dưới 5 ppb. Khó có thể giảm mức oxy hòa tan xuống dưới 10 ppb khi thời gian tiếp "
      "xúc dưới 30 giây. Vì vậy, thời gian lý tưởng nên được xác định dựa trên mức giảm oxy hòa "
      "tan mong muốn. Đối với sử dụng trong nhà máy điện hơi, nơi mức oxy hòa tan phải dưới "
      "5 ppb, thời gian ít nhất là khoảng 45 giây.",
      "As seen in Figure 4 in the contact time of less than 45 seconds, the decrease in "
      "dissolved Oxygen levels below 5 ppb is not possible. It is hard to reduce the dissolved "
      "Oxygen level of less than 10 ppb when the exposure time is less than 30 seconds. "
      "Therefore, the ideal time should be considered based on desired reduction of dissolved "
      "Oxygen. For use in steam power plants that dissolved Oxygen levels should be less than "
      "5 ppb, time is at least about 45 seconds.")
    FIG(4, F.fig_f04())

    H("Ảnh hưởng của nồng độ oxy hòa tan đầu vào",
      "Effect of Inlet Dissolved Oxygen Concentration", h3)
    P("Lượng oxy hòa tan trong nước đầu vào tại thời điểm bắt đầu của hệ thống có ảnh hưởng đến "
      "thời gian vận hành. Nói cách khác, thời gian cần để đạt nồng độ giới hạn của oxy còn lại "
      "trong nước đầu ra của cột xúc tác chịu ảnh hưởng của oxy hòa tan trong nước đầu vào. Ở thể "
      "tích xúc tác cố định, lượng oxy hòa tan trong nước càng ít thì lượng nước chảy qua giường "
      "xúc tác càng lớn. Trong điều kiện đó, kết quả mong muốn đạt được và tốc độ phun hydro "
      "thấp hơn. Kết quả thí nghiệm ở các nồng độ oxy hòa tan khác nhau được thể hiện trong Hình "
      "(5). Ví dụ, khi đầu vào oxy hòa tan là 0,5 ppm, thời gian cần để đạt điểm mong muốn 5 ppb "
      "DO còn lại là ngắn ngay cả ở thời gian tiếp xúc 30 giây.",
      "The amount of dissolved Oxygen in the water inlet at the start time of the system is "
      "effective on the operating time. In other words, the time required to reach the limit "
      "concentration for the remaining Oxygen in the outlet water of the catalytic column, is "
      "influenced by the dissolved Oxygen in water input. In a fixed volume of catalyst, the "
      "less amount of dissolved Oxygen in water, a higher amount of the water flows through the "
      "catalyst bed. In this condition the desired results would be achieved and the Hydrogen "
      "injection rate would be lower. The results of experiments in different concentrations of "
      "dissolved Oxygen are shown in Figure (5). For example when the input of dissolved Oxygen "
      "is 0.5 ppm, the time needed to reach to the desired point of 5 ppb of remaining DO is "
      "short even at the contact time of 30 seconds.")
    FIG(5, F.fig_f05())

    # ---------------------------------------------------------------- 1.5
    H("1.5 Kết luận", "1.5 Conclusion")
    P("Điều kiện vận hành là một trong những thông số quan trọng nhất ảnh hưởng đến hiệu quả "
      "khử xúc tác oxy hòa tan. Ưu điểm của quá trình này là vận hành ở nhiệt độ trung bình và áp "
      "suất thấp. Vai trò của áp suất là hỗ trợ sự hòa tan hydro trong hệ thống. Ngoài ra, áp suất "
      "hydro ngăn sự hình thành dòng chảy hai pha sau cột trộn. Có thể giảm oxy hòa tan bằng cách "
      "tăng lưu lượng nước ở mức oxy đầu vào thấp. Trong điều kiện đó, quá trình trở nên hiệu "
      "quả hơn.",
      "The operation condition is one of the most important parameters that influence on the "
      "efficiency of the catalytic reduction of dissolved Oxygen. The advantage of this process "
      "is its operation at moderate temperature and low pressure. The role of pressure is "
      "helping for Hydrogen solution in the system. Also the Hydrogen pressure prevents the "
      "formation of two phase flow after the mixing column. It is possible to reduce dissolved "
      "Oxygen by means of increasing the water flow rate at low inlet Oxygen level. In this "
      "condition the process would be more efficient.")
    P("Ngoài ra, thời gian tiếp xúc và nồng độ oxy là những thông số quan trọng nhất ảnh hưởng "
      "đến hiệu quả khử xúc tác oxy hòa tan. Trong các nhà máy điện hơi, nơi mức oxy hòa tan phải "
      "dưới 5 ppb, thời gian ít nhất là khoảng 45 giây. Ngoài ra, ở thể tích xúc tác cố định, với "
      "lượng oxy hòa tan thấp trong nước đầu vào, có thể tăng lưu lượng nước và giảm lượng phun "
      "hydro, từ đó đạt được nồng độ oxy đầu ra mong muốn.",
      "Also, The contact time and Oxygen concentration are the most important parameters that "
      "influence on the efficiency of the catalytic reduction of dissolved Oxygen. In steam "
      "power plants that dissolved oxygen levels should be less than 5ppb, time is at least "
      "about 45 seconds. Also In a fixed volume of catalyst, at low amount of dissolved Oxygen "
      "in water inlet, it would be possible to increase water flow rate and decrease the "
      "Hydrogen injection and therefore reach to desired outlet Oxygen concentration.")

    # ---------------------------------------------------------------- 1.6
    H("1.6 Tài liệu tham khảo", "1.6 References")
    b.append(refs(_REFS))

    # ---------------------------------------------------------------- about
    H("Về nguồn tài liệu", "About the source", h3)
    P("Chương 1 chiếm PDF tr. 17-28 (tr. 28 để trống), tương ứng tr. 1-12 của bản in; PAGES_SRC = "
      "12 đếm toàn bộ phân đoạn nguồn này. Các mục theo mục lục là Introduction, Catalytic "
      "Reduction of Dissolved Oxygen, Results and Discussion, The System Performance in Low Level "
      "of Inlet Oxygen and High Water Flow Rate, Conclusion và References. Nguyên bản có đúng năm "
      "hình đánh số Figure 1 - Figure 5 và bốn bảng đánh số Table 1 - Table 4; tất cả được dựng "
      "lại dạng vector hoặc chép lại từ trang in ở đây.",
      "Chapter 1 occupies PDF pp. 17-28 (PDF p. 28 is blank), corresponding to printed pp. "
      "1-12; PAGES_SRC = 12 counts this whole source span. Its sections are Introduction, "
      "Catalytic Reduction of Dissolved Oxygen, Results and Discussion, The System Performance "
      "in Low Level of Inlet Oxygen and High Water Flow Rate, Conclusion and References. The "
      "source contains exactly five numbered figures, Figure 1 - Figure 5, and four numbered "
      "tables, Table 1 - Table 4; all are redrawn as vectors or transcribed from the printed "
      "pages here.")
    b.append(note(
        ("<b>Đặc điểm của nguyên bản.</b> Ba phương trình hóa học và dữ liệu của bốn bảng chỉ "
         "tồn tại dưới dạng hình ảnh trong lớp văn bản; các phương trình được viết lại bằng ký "
         "hiệu tại chỗ còn bốn bảng được chép từ trang in. Trong Bảng 2 và Bảng 4, những ô in kèm "
         "ký hiệu lỗi trình bày sau số 28 và 24 được hiểu là giá trị lớn hơn 28 và 24 ppb và được "
         "ghi là “&gt;28” và “&gt;24”. Một số lỗi chính tả và lỗi OCR của nguồn được giữ nguyên "
         "trong bản Anh (ví dụ “various experimental is implemented”, “no more possible”, “In other "
         "hand”, “mo1 H2O/mo1H2”, “use of sodium sulphite hydrazine”, “this take places slowly”, "
         "“Anyway the increase”), còn bản Việt dùng nghĩa đúng. PDF tr. 28 (tr. in 12) để trống "
         "nhưng vẫn nằm trong phân đoạn nguồn và được tính vào PAGES_SRC = 12."
         if vi else
         "<b>Source quirks.</b> The three chemical equations and the data of the four tables "
         "exist only as images in the text layer; the equations are rendered symbolically in "
         "place and the tables are transcribed from the printed pages. In Tables 2 and 4, cells "
         "printed with a stray typesetting mark after 28 and 24 are read as values greater than "
         "28 and 24 ppb and shown as “&gt;28” and “&gt;24”. A number of source typos and OCR "
         "artifacts are kept in the English text (e.g. 'various experimental is implemented', "
         "'no more possible', 'In other hand', 'mo1 H2O/mo1H2', 'use of sodium sulphite "
         "hydrazine', 'this take places slowly', 'Anyway the increase'), while the Vietnamese "
         "uses the intended meaning. PDF p. 28 (printed p. 12) is blank but lies inside the "
         "assigned source span and is counted in PAGES_SRC = 12.")))
    P("<i>Đây là bản dịch không chính thức, dùng cho mục đích học tập. Nội dung gốc © 2019 "
      "Bibliotex; các chương của sách phát hành theo giấy phép Creative Commons.</i>",
      "<i>This is an unofficial translation for study purposes. Original content © 2019 "
      "Bibliotex; the individual chapters are released under Creative Commons.</i>")
    return "".join(b)


def body_vi():
    return _body("vi")


def body_en():
    return _body("en")
