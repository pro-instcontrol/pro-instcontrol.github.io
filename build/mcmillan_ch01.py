# -*- coding: utf-8 -*-
"""Chapter 1 - Introduction / Gioi thieu.

EN/VI bilingual study reader of Alan McMillan, *Electrical Installations in
Hazardous Areas* (Butterworth-Heinemann, 1998), printed pp. 1-21.
Covers all eight printed sections (1.1-1.8), the two printed tables, the six
redrawn vector figures and the sixteen numbered references.

This is an unofficial study translation. The source PDF is not republished.
"""
from mcmillan_common import fig, h2, h3, h4, lead, note, p, quote, refs, table, ul, ol

import mcmillanfig01_a as FA
import mcmillanfig01_b as FB

PAGES_SRC = 21
BYLINE = "Alan McMillan · Electrical Installations in Hazardous Areas (Butterworth-Heinemann, 1998)"
TITLE_EN = "Introduction"
TITLE_VI = "Giới thiệu"


# ---------------------------------------------------------------- glossary
def note_terms(lang):
    if lang == "vi":
        return ("<b>Thuật ngữ chương 1.</b> bầu khí quyển nổ (explosive atmosphere) · "
                "tam giác nổ (explosion triangle) · firedamp (methane) · vỏ chống cháy nổ "
                "(flameproof enclosure) · mạch an toàn nội tại (intrinsically safe circuit) · "
                "phân loại khu vực (area classification) · Chỉ thị 76/117/EEC và 94/9/EC · "
                "CENELEC · Dấu nhận biết Cộng đồng (Distinctive Community Mark) · cơ quan được "
                "phê duyệt hoặc thông báo (approved/notified body) · Giấy chứng nhận phù hợp "
                "(Certificate of Conformity) · nhóm khí IIA/IIB/IIC · cấp nhiệt độ T1-T6 · "
                "HOTL · dấu CE · BS/EN/ISO 9002 và 9003.")
    return ("<b>Key terms in Chapter 1.</b> explosive atmosphere · explosion triangle · "
            "firedamp (methane) · flameproof enclosure · intrinsically safe circuit · area "
            "classification · Directives 76/117/EEC and 94/9/EC · CENELEC · Distinctive "
            "Community Mark · approved (notified) body · Certificate of Conformity · gas "
            "groups IIA/IIB/IIC · temperature classes T1-T6 · HOTL · CE mark · BS/EN/ISO "
            "9002 and 9003.")


# ------------------------------------------------------------- Table 1.1
_T11_HEADER_VI = ["Châu Âu hiện hành", "GB lịch sử - Chống cháy nổ",
                  "GB lịch sử - An toàn nội tại", "Đức", "Hoa Kỳ"]
_T11_ROWS_VI = [
    ["nhóm phụ IIA", "Group II", "class 2c", "class 1", "Group D"],
    ["nhóm phụ IIB", "Group III", "class 2d", "class 2", "Group C"],
    ["nhóm phụ IIC", "Group IV", "class 2e và 2f", "class 3a và 3n", "Group B và A"],
]
_T11_FN_VI = ("Ghi chú: 1. Nhóm IV chống cháy nổ của Anh loại trừ acetylene, được xử lý riêng. "
              "2. class 2e an toàn nội tại của Anh không gồm acetylene, nhưng class 2f thì có. "
              "3. class 3a của Đức loại trừ acetylene, cũng như Group B của Hoa Kỳ và class 2e "
              "của Anh; acetylene được đưa vào class 3n của Đức, Group A của Hoa Kỳ và class 2 "
              "của Anh. 4. Tại Hoa Kỳ còn có các Group sau: E - bụi dẫn điện; F - bụi không dẫn "
              "điện; G - bụi bột mì và ngũ cốc. 5. Thêm phức tạp, thiết bị Hoa Kỳ được xếp theo "
              "mục đích sử dụng: Class A cho khí và hơi, Class B cho bụi, Class C cho sợi và "
              "mảnh bay.")

_T11_HEADER_EN = ["Current European", "Historic GB - Flame proof",
                  "Historic GB - Intrinsic Safety", "German", "USA"]
_T11_ROWS_EN = [
    ["sub-group IIA", "Group II", "class 2c", "class 1", "Group D"],
    ["sub-group IIB", "Group III", "class 2d", "class 2", "Group C"],
    ["sub-group IIC", "Group IV", "class 2e and 2f", "class 3a and 3n", "Group B and A"],
]
_T11_FN_EN = ("Notes: 1. UK Flameproof Group IV excludes acetylene, which was treated "
              "separately. 2. UK intrinsic safety class 2e did not include acetylene, but 2f "
              "did. 3. German class 3a excludes acetylene, as does USA Group B and UK Class 2e; "
              "acetylene is included in German class 3n, USA Group A and UK Class 2. 4. In the "
              "USA the following groups are also present: E - conducting dusts; F - "
              "nonconducting dusts; G - flour and grain dust. 5. To add further complexity, USA "
              "apparatus is classed as to its intended use: Class A for gases and vapours, "
              "Class B for dusts and Class C for fibres and flyings.")


# ------------------------------------------------------------- Table 1.2
_T12_HEADER_VI = ["Châu Âu và Anh", "Đức", "Hoa Kỳ"]
_T12_ROWS_VI = [
    ["T1", "G1", "T1"],
    ["T2", "G2", "T2"],
    ["–", "–", "T2A (280 °C)"],
    ["–", "–", "T2B (260 °C)"],
    ["–", "–", "T2C (230 °C)"],
    ["–", "–", "T2D (215 °C)"],
    ["T3", "G3", "T3"],
    ["–", "–", "T3A (180 °C)"],
    ["–", "–", "T3B (165 °C)"],
    ["–", "–", "T3C (160 °C)"],
    ["T4", "G4", "T4"],
    ["–", "–", "T4A (120 °C)"],
    ["T5", "G5", "T5"],
    ["T6", "T6", "–"],
]
_T12_FN_VI = ("Ghi chú: Trước khi có hệ thống phân loại nhiệt độ riêng tại Hoa Kỳ, phân loại "
              "nhiệt độ được liên kết với hệ thống phân nhóm như sau: các Nhóm A, B và D được "
              "quy nhiệt độ tối đa 280 °C; Nhóm C được quy nhiệt độ tối đa 180 °C; các Nhóm E và "
              "F được quy 200 °C; còn Nhóm G là 165 °C.")

_T12_HEADER_EN = ["European and UK", "German", "USA"]
_T12_ROWS_EN = [
    ["T1", "G1", "T1"],
    ["T2", "G2", "T2"],
    ["-", "-", "T2A (280 °C)"],
    ["-", "-", "T2B (260 °C)"],
    ["-", "-", "T2C (230 °C)"],
    ["-", "-", "T2D (215 °C)"],
    ["T3", "G3", "T3"],
    ["-", "-", "T3A (180 °C)"],
    ["-", "-", "T3B (165 °C)"],
    ["-", "-", "T3C (160 °C)"],
    ["T4", "G4", "T4"],
    ["-", "-", "T4A (120 °C)"],
    ["T5", "G5", "T5"],
    ["T6", "T6", "-"],
]
_T12_FN_EN = ("Note: Prior to the introduction of a separate temperature classification system "
              "in the USA, temperature classification was associated with the grouping system "
              "as follows: Groups A, B and D were given a maximum temperature of 280 °C; Group "
              "C was given a maximum temperature of 180 °C; Groups E and F were given a "
              "temperature of 200 °C; and Group G a temperature of 165 °C.")


# ------------------------------------------------------------- References
_REFS_VI = [
    "Hicks, W. F và Brown, K. J (1971). Đánh giá xác suất nổ đối với thiết bị an toàn nội tại "
    "(Hội nghị IEE về an toàn điện trong môi trường nguy hiểm, 16-18 tháng 3).",
    "The Electricity (Factories Act) Special Regulations 1908 và 1944.",
    "The Factories Act 1961 (Đạo luật Nhà máy 1961).",
    "The Health and Safety at Work Act 1974 (Đạo luật An toàn và Sức khỏe Lao động 1974).",
    "Electricity at Work Regulations 1989 (Quy định Điện tại Nơi làm việc 1989).",
    "Institute of Petroleum Area Classification Code for Petroleum Installations (1990) "
    "(Quy chuẩn phân loại khu vực cho cơ sở dầu khí).",
    "RoSPA/ICI Engineering Codes and Regulations, Electrical Installations in Flammable "
    "Atmospheres (1973), Group C (Electrical), Volume 1.5.",
    "76/117/EEC (1975). Chỉ thị Hội đồng về hội tụ pháp luật các Quốc gia Thành viên liên quan "
    "đến thiết bị điện dùng trong môi trường có khả năng nổ. 18 tháng 12 năm 1975.",
    "Comite Europeen de Normalisation Electrique (CENELEC), Rue de Stassart 35, B-1050 Brussels.",
    "Các chỉ thị bổ sung cho 76/117/EEC: Chỉ thị Hội đồng 79/196/EEC; Chỉ thị Ủy ban 84/47/EEC; "
    "Chỉ thị Ủy ban 88/571/EEC; Chỉ thị Hội đồng 90/487/EEC.",
    "94/9/EC (1994). Chỉ thị của Nghị viện và Hội đồng Châu Âu về hội tụ pháp luật các Quốc gia "
    "Thành viên liên quan đến thiết bị và hệ thống bảo vệ dự định dùng trong môi trường có khả "
    "năng nổ. 23 tháng 3.",
    "Official Journal of the European Communities (Công báo các Cộng đồng Châu Âu).",
    "The Electrical Equipment for Explosive Atmospheres (Certification) Regulations 1990.",
    "6430/92 EN. Đề xuất Chỉ thị Hội đồng về các yêu cầu tối thiểu nhằm cải thiện an toàn, sức "
    "khỏe và bảo vệ người lao động trong môi trường có khả năng nổ (dự thảo).",
    "HOTL là nhóm công tác do Ủy ban Châu Âu thành lập và tài trợ, gồm người đứng đầu của mọi Cơ "
    "quan được phê duyệt (thông báo) và đại diện Tổng Giám đốc III và Tổng Giám đốc V của Ủy ban.",
    "BS/EN/ISO 9002: (1994) Quality Systems - Specification for production, installation and "
    "servicing.",
]

_REFS_EN = [
    "Hicks, W. F. and Brown, K. J. (1971). Assessment of explosion probability for intrinsically "
    "safe apparatus. IEE Conference on electrical safety in hazardous environments, 16-18 March.",
    "The Electricity (Factories Act) Special Regulations 1908 and 1944.",
    "The Factories Act 1961.",
    "The Health and Safety at Work Act 1974.",
    "Electricity at Work Regulations 1989.",
    "Institute of Petroleum Area Classification Code for Petroleum Installations (1990).",
    "RoSPA/ICI Engineering Codes and Regulations, Electrical Installations in Flammable "
    "Atmospheres (1973). Group C (Electrical), Volume 1.5.",
    "76/117/EEC (1975). Council Directive on the approximation of the laws of Member States "
    "concerning electrical equipment for use in potentially explosive atmospheres. 18 December 1975.",
    "Comite Europeen de Normalisation Electrique (CENELEC), Rue de Stassart 35, B-1050 Brussels.",
    "Directives supplementary to 76/117/EEC: Council Directive 79/196/EEC; Commission Directive "
    "84/47/EEC; Commission Directive 88/571/EEC; Council Directive 90/487/EEC.",
    "94/9/EC (1994). Directive of the European Parliament and Council on the approximation of "
    "the laws of Member States concerning equipment and protective systems intended for use in "
    "potentially explosive atmospheres. 23 March.",
    "Official Journal of the European Communities.",
    "The Electrical Equipment for Explosive Atmospheres (Certification) Regulations 1990.",
    "6430/92 EN. Proposal for a Council Directive concerning minimum requirements for improving "
    "the safety and health and protection of workers in potentially explosive atmospheres "
    "(Draft document).",
    "HOTL is a working party set up and funded by the Commission comprising the heads of all "
    "Approved (Notified) Bodies and representatives of Directorate General III and Directorate "
    "General V of the Commission.",
    "BS/EN/ISO 9002: (1994) Quality Systems - Specification for production, installation and "
    "servicing.",
]


# ==================================================================== VI
def body_vi():
    b = []
    b.append(h2(TITLE_VI, TITLE_EN))
    b.append(lead("Bảo vệ chống nổ cho thiết bị điện · các sự cố lịch sử · pháp luật Anh và "
                  "Châu Âu · chứng nhận · ghi nhãn · định hướng tương lai."))

    # ---- opening pages (un-numbered introduction)
    b.append(p("Khi vật liệu dễ cháy hoặc cháy được được lưu trữ hoặc chế biến, trong hầu hết "
               "trường hợp có khả năng chúng rò rỉ hoặc bằng cách khác tạo thành cái có thể gọi "
               "là bầu khí quyển nổ khi kết hợp với oxy có trong không khí. Điều này đúng với "
               "khí, hơi, sương mù và bụi. Vì điện được dùng rộng rãi trong công nghiệp và nhiều "
               "nơi có thể xuất hiện bầu khí quyển nổ đó, khả năng năng lượng điện tạo ra tia "
               "lửa hoặc bề mặt nóng dẫn đến nguy cơ bầu khí quyển bị đánh lửa, gây cháy hoặc nổ."))
    b.append(p("Mối nguy này đã được nhận biết từ nhiều thập kỷ, gần như ngay từ khi điện bắt "
               "đầu được đưa vào khai thác mỏ và các ngành công nghiệp khác. Các biện pháp phòng "
               "ngừa cơ bản để khắc phục vấn đề này đã được hình thành từ đầu thế kỷ hai mươi "
               "hoặc sớm hơn."))
    b.append(p("Không thể ngăn ngừa hoàn toàn vụ nổ trong các ngành mà có thể xuất hiện bầu khí "
               "quyển nổ, vì mọi nỗ lực của con người đều có thể sai sót. Cần phát triển hoạt "
               "động đến mức các vụ nổ trở nên hiếm đến mức rủi ro của chúng được bù đắp xa bởi "
               "lợi ích của quá trình mà chúng có thể xảy ra."))
    b.append(p("Ngành khai thác than minh họa rõ sự cân bằng này: rủi ro tổng thể khi làm việc "
               "dưới lòng đất, trong đó nổ là một thành phần, được xem là chính đáng dựa trên "
               "nhu cầu nhiên liệu của xã hội. Các rủi ro được giảm thiểu ở mức phù hợp với yêu "
               "cầu khai thác than, nhưng tai nạn vẫn xảy ra. Điều cốt yếu là mức rủi ro đã được "
               "giảm xuống mức xã hội chấp nhận, đặc biệt là những người làm việc trong ngành."))
    b.append(p("Điều đó không có nghĩa là khi một sự cố làm lộ ra rủi ro thì không có hành động "
               "gì. Chúng ta luôn học hỏi từ các sự cố và hầu như luôn thay đổi hệ thống vận "
               "hành và thiết bị để giảm thiểu khả năng lặp lại. Dù có mọi nỗ lực, tai nạn quy "
               "mô lớn vẫn xảy ra với tần suất khiến tất cả chúng ta lo ngại."))

    # ---- 1.1
    b.append(h3("Ví dụ về các sự cố lịch sử", "Examples of historic incidents"))
    b.append(p("Sau đây là ví dụ về những sự cố đáng kể nhất xảy ra tại Vương quốc Anh. Dù "
               "chúng không nhất thiết do điện gây ra, ở ít nhất một trường hợp có nghi ngờ "
               "nguồn đánh lửa từ điện; như đã nêu, điện được xem là tác nhân đánh lửa rõ rệt."))
    b.append(ul([
        "<b>Senghennyd - 1913.</b> Một vụ nổ firedamp (methane) dưới hầm làm sập trần, cắt "
        "đứt đường ra của hơn 400 thợ mỏ tại một khu vực đang cháy. Hầu hết tử vong do ngạt thở.",
        "<b>Flixborough - 1974.</b> Một sửa đổi đối với nhà máy công nghệ, theo báo cáo tai nạn "
        "là không được xem xét thỏa đáng, được xác định là nguyên nhân phát thải lớn khí dễ "
        "cháy, gây một vụ nổ khổng lồ trên không trung. Thiệt mạng trên nhà máy may mắn là thấp "
        "(có lẽ vì hôm đó là ngày thứ Bảy), nhưng thiệt hại cho nhà máy và các khu dân cư, tài "
        "sản quanh đó rất đáng kể.",
        "<b>Piper Alpha - 1988.</b> Giàn khoan dầu này bị phá hủy gần như hoàn toàn bởi một vụ "
        "nổ khí do phát thải lớn, được cho là do vận hành công nghệ sai. Vụ nổ ban đầu và các "
        "vụ nổ, đám cháy sau đó khiến việc sơ tán có kiểm soát trở nên vô hiệu và gây tổn thất "
        "nhân mạng nặng nề.",
        "<b>Nhà máy lọc dầu Texaco Pembroke - 1994.</b> Một vụ nổ hơi lớn xảy ra, dẫn đến đám "
        "cháy lớn cực kỳ khó dập tắt. Nhà máy cháy trong một thời gian dài, gây tác động xấu "
        "đến môi trường địa phương. Thương vong ít nhưng nhà máy bị hư hại đáng kể.",
    ]))
    b.append(p("Những ví dụ trên cho thấy rõ mối nguy hiện hữu, đặc biệt tại những nơi việc "
               "thoát ra của con người rất khó khăn. Vì vậy, điều thiết yếu là tất cả những "
               "người liên quan phải hiểu công nghệ được dùng để giảm thiểu rủi ro nổ."))
    b.append(p("Ngay cả khi đã cân nhắc việc phòng ngừa tai nạn vào thiết kế, vẫn cần ghi nhận "
               "rằng các sự cố nghiêm trọng tiếp tục xảy ra, và mỗi lần như vậy thường dẫn đến "
               "thay đổi quy trình vận hành và thiết bị nhằm giảm khả năng lặp lại."))

    # ---- 1.2
    b.append(h3("Cách tiếp cận công nghệ", "Technological approach"))
    b.append(p("Mục tiêu của công nghệ liên quan đến việc dùng thiết bị điện trong môi trường "
               "có khả năng nổ là giảm rủi ro nổ xuống mức có thể chấp nhận được. Để có vụ nổ "
               "cần ba yếu tố: nhiên liệu, oxy và nguồn đánh lửa (xem Hình 1.1)."))
    b.append(fig(1, FA.fig_f101()))
    b.append(p("Oxy có trong không khí ở mức đủ để duy trì sự cháy và thông thường không thể "
               "loại bỏ, nên chỉ còn nhiên liệu và nguồn đánh lửa là các yếu tố có thể tác động "
               "vào. Đây là nền tảng của công nghệ từ đầu thế kỷ hai mươi, khi vấn đề lần đầu "
               "được xác định trong ngành khai thác mỏ."))
    b.append(p("Ở những lĩnh vực rủi ro khác, cách tiếp cận thường dựa nặng hơn vào phân tích "
               "thống kê. Đối với môi trường nổ, cách tiếp cận đã được thiết lập và chấp nhận "
               "từ đầu những năm 1900. Nhiều yếu tố chủ quan làm cho phân tích thống kê trở nên "
               "khó khăn; dù đã có nhiều nỗ lực áp dụng phương pháp này, công nghệ hiện tại và "
               "trong tương lai gần vẫn dựa trên nền tảng đã được thiết lập. Không có dấu hiệu "
               "của sự thay đổi căn bản theo hướng xem xét lại công nghệ trên cơ sở thống kê như "
               "được thực hiện, ví dụ, trong ngành công nghiệp hạt nhân."))
    b.append(p("Một nỗ lực điển hình nhằm phân tích mức độ an toàn thống kê đạt được liên quan "
               "đến sự phát thải khí, hơi và sương mù là bài báo của W. A. Hicks và K. J. Brown "
               "tại Hội nghị 1971 của Viện Kỹ sư Điện, trong đó rủi ro đánh lửa được xác định "
               "nằm trong khoảng 10<sup>-5</sup> đến 10<sup>-14</sup>. Nhiều người khác đưa ra "
               "con số khác nhau, vì các giả định về những yếu tố chủ quan của công nghệ khác "
               "nhau."))
    b.append(p("Công nghệ hiện nay dựa trên việc xác định rủi ro có bầu khí quyển nổ hiện diện "
               "tại một nơi cụ thể, kết hợp với việc xác định khả năng thiết bị điện trong bầu "
               "khí quyển đó hỏng theo cách biến nó thành nguồn đánh lửa trùng thời điểm với "
               "sự hiện diện của bầu khí quyển nổ."))
    b.append(p("Mục tiêu không chỉ là nhận diện những sự trùng hợp này, mà còn là dùng thông "
               "tin thu được để ảnh hưởng đến thiết kế của các nhà máy công nghệ và các tình "
               "huống vận hành tương tự, sao cho giảm thiểu rủi ro hình thành bầu khí quyển nổ, "
               "từ đó giảm rủi ro nổ do thiết bị điện."))
    b.append(p("Nguyên tắc chung là tìm ra các tình huống mà bầu khí quyển nổ hiện diện thường "
               "xuyên theo yêu cầu tất yếu của công đoạn, những tình huống mà khả năng hiện "
               "diện cao, và những tình huống mà khả năng hiện diện thấp nhưng vẫn nhận biết "
               "được. Trong kịch bản này, thảm họa không đóng vai trò; dù cần lập kế hoạch cho "
               "thảm họa, các kế hoạch đó nhìn chung nằm ngoài phạm vi của công nghệ này."))
    b.append(p("Công nghệ này không nên được dùng riêng lẻ mà là một phần của chiến lược an "
               "toàn tổng thể cho khu vực phát sinh vấn đề. Sau khi xác định sự hiện diện có thể "
               "có của bầu khí quyển nổ, cần xác định những thiết bị điện thực sự cần hiện "
               "diện, thay vì những thiết bị chỉ thuận tiện, và bảo đảm chúng được bảo vệ sao "
               "cho rủi ro nổ tổng thể đủ thấp."))

    # ---- 1.3
    b.append(h3("Lịch sử phát triển", "History of development"))
    b.append(p("Việc dùng thiết bị điện trong môi trường nổ ban đầu là lĩnh vực của ngành khai "
               "thác mỏ. Dù công nghệ cũng được dùng trong công nghiệp mặt đất, các bước phát "
               "triển đáng kể ở lĩnh vực latter mang tính hiện đại hơn, phần lớn là sau chiến "
               "tranh."))
    b.append(p("Cách tiếp cận hiện nay là giảm thiểu khả năng phát thải vật liệu dễ cháy, hoặc "
               "khi đã phát thải thì giảm thiểu sự tích tụ của vật liệu trong không khí. Có lẽ "
               "đáng ngạc nhiên là trong giai đoạn khai thác than sơ khai, phương pháp xử lý "
               "sự phát thải methane (firedamp) lại là cố ý đốt cháy bầu khí quyển nổ."))
    b.append(p("Công việc này do một thợ mỏ được chỉ định riêng, gọi là 'firelighter', thực "
               "hiện. Phương pháp tận dụng thực tế là methane nhẹ hơn không khí (tỷ trọng tương "
               "đối khoảng 0.55), do đó hỗn hợp methane và không khí tích tụ ưu tiên gần trần "
               "đường hầm. Tín hiệu báo hiệu là sự thay đổi màu ngọn lửa của đèn thợ mỏ, sau đó "
               "khu vực khai thác được dọn sạch."))
    b.append(p("Một ngọn đuốc được đưa vào đám khí methane và không khí, đánh lửa và đốt cháy "
               "lượng methane. Kỹ thuật này sớm bị xem là không còn phù hợp vì những lý do rõ "
               "ràng, và được thay thế bằng thông gió để hạn chế khả năng hình thành bầu khí "
               "quyển nổ, cùng với việc dùng đèn an toàn (Hình 1.2) nhằm giảm rủi ro đánh lửa."))
    b.append(fig(2, FA.fig_f102()))
    b.append(p("Việc đưa điện vào sử dụng vào cuối thế kỷ mười chín và đầu thế kỷ hai mươi dẫn đến "
               "nhiều rủi ro mới đáng kể được xác định. Ban đầu điện được dùng cho chiếu sáng "
               "và tạo động lực."))
    b.append(p("Ánh sáng thường do đèn dây tóc bóng đèn cung cấp, vì khi đó chưa có các loại đèn "
               "tinh vi hơn, còn động lực thường do máy một chiều hoặc máy xoay chiều rô-to "
               "dây quấn, là những loại động cơ điển hình thời kỳ đầu. Cả chiếu sáng lẫn máy "
               "móc đều cần thiết bị điều khiển, đôi khi chỉ là một công tắc, nhưng thiết bị "
               "này lại đưa vào các rủi ro liên quan đến bề mặt nóng và tia lửa, cùng với khả "
               "năng có mặt đồng thời của methane và bụi than."))
    b.append(p("Giải pháp cho các vấn đề liên quan đến phát thải khí, hơi và sương mù được phát "
               "triển ở cả Anh và Đức theo những hướng rất giống nhau và trong những khung thời "
               "gian tương tự. Tại Đức, tổ chức chủ yếu tham gia là cái hiện được gọi là "
               "Berggewerkschaftlichen Versuchsstrecke (BVS); Dr Ing. Carl Beyling của tổ chức "
               "này đã được trao Huy chương Vàng của Viện Kỹ sư Khai thác Anh năm 1938 cho công "
               "trình của ông trong lĩnh vực này."))
    b.append(p("Tại Anh, một tổ chức tương tự nhưng thuộc chính phủ đã tham gia đáng kể vào các "
               "phát triển tương tự. Tổ chức này hiện là Phòng Thí nghiệm An toàn và Sức khỏe "
               "của Cơ quan An toàn và Sức khỏe, nhưng được biết đến nhiều hơn với tên cũ là "
               "Safety in Mines Research Establishment (Trạm Nghiên cứu An toàn Hầm mỏ)."))
    b.append(p("Kỹ thuật bảo vệ thiết bị điện ban đầu là cái hiện gọi là vỏ chống cháy nổ "
               "(flameproof enclosure), dành cho thiết bị điện công suất lớn mà mức năng lượng "
               "điện cần để vận hành luôn đủ để gây đánh lửa nếu thoát ra dưới dạng tia lửa hoặc "
               "nhiệt. Kỹ thuật này đã phát triển tốt từ rất sớm, vào năm 1905."))
    b.append(p("Ngay sau đó là kỹ thuật thứ hai, hiện gọi là mạch an toàn nội tại (intrinsically "
               "safe circuit). Kỹ thuật này được phát triển cho hệ thống tín hiệu hầm mỏ và dựa "
               "trên thực tế là thông tin có thể truyền đi bằng rất ít năng lượng điện, và nếu "
               "thoát ra thì năng lượng đó không đủ để đánh lửa bất kỳ bầu khí quyển nổ dự kiến "
               "nào. Ưu điểm của kỹ thuật này là tính linh hoạt, vì không cần những vỏ bảo vệ "
               "lớn và nặng."))
    b.append(p("Ban đầu hai kỹ thuật này được phát triển cho ngành khai thác mỏ, nơi methane là "
               "vật liệu dễ cháy nhạy nhất hiện diện. Khi bắt đầu được áp dụng cho công nghiệp "
               "mặt đất, hai khác biệt quan trọng nhanh chóng trở nên rõ rệt. Thứ nhất, phát "
               "thải vật liệu dễ cháy thường đến từ thiết bị đã lắp đặt và dự đoán được về số "
               "lượng và tần suất. Thứ hai, thay vì chỉ xử lý một loại khí và một loại bụi như "
               "trong hầm mỏ, công nghiệp mặt đất phải xử lý vô số vật liệu khác nhau, mỗi loại "
               "có đặc tính riêng."))
    b.append(p("Nhận thức này dẫn đến sự phát triển của kỹ thuật phân loại khu vực (area "
               "classification) để xác định rủi ro hình thành bầu khí quyển nổ tại các vị trí "
               "cụ thể, và đến việc phát triển thêm các loại bảo vệ khác nhằm phản ánh tốt hơn "
               "các mức nguy hiểm khác nhau có thể xác định được. Chính hai yếu tố này dẫn đến "
               "thực tiễn công nghiệp hiện hành của Anh và quốc tế mà cuốn sách này muốn mô tả."))

    # ---- 1.4
    b.append(h3("Pháp luật Vương quốc Anh", "UK legislation"))
    b.append(p("Nền tảng pháp luật lịch sử của Anh liên quan đến việc dùng thiết bị điện trong "
               "môi trường nổ là các Quy định Điện trong Đạo luật Nhà máy. Quy định 27 của các "
               "quy định này nêu:"))
    b.append(quote("Mọi dẫn dây và thiết bị tiếp xúc với thời tiết, ẩm ướt, ăn mòn, môi trường "
                   "dễ cháy hoặc bầu khí quyển nổ, hoặc được dùng trong bất kỳ công đoạn nào hay "
                   "cho mục đích đặc biệt nào khác ngoài chiếu sáng hoặc cung cấp điện, phải "
                   "được chế tạo hoặc bảo vệ, và phải thực hiện các biện pháp phòng ngừa đặc "
                   "biệt cần thiết để ngăn ngừa nguy hiểm một cách thỏa đáng do sự tiếp xúc "
                   "hoặc sử dụng đó.",
                   "Quy định 27, Quy định Điện (Đạo luật Nhà máy)"))
    b.append(p("Quy định này nêu rõ mục tiêu cần đạt được nhưng không định nghĩa phương thức "
               "đạt được mục tiêu đó. Ý định của nó là cho phép phạm vi cách tiếp cận rộng nhất "
               "có thể, từ đó trao cho công nghiệp sự tự do tối đa trong vận hành, đồng thời đặt "
               "ra yêu cầu ngành phải đạt được mức an toàn thỏa đáng trong hoạt động của mình."))
    b.append(p("Quy định 27 vẫn còn hiệu lực, ngay cả sau khi Đạo luật An toàn và Sức khỏe Lao "
               "động 1974 được ban hành, cho đến khi được thay thế bởi Quy định 6 của Quy định "
               "Điện tại Nơi làm việc 1989. Quy định 6 nêu:"))
    b.append(quote("Thiết bị điện mà theo dự kiến hợp lý có thể tiếp xúc với:<br>"
                   "(a) hư hỏng cơ học;<br>"
                   "(b) tác động của thời tiết, thiên tai, nhiệt độ hoặc áp suất;<br>"
                   "(c) tác động của điều kiện ẩm, bẩn, bụi hoặc ăn mòn; hoặc<br>"
                   "(d) bất kỳ chất dễ cháy hoặc nổ nào, kể cả bụi, hơi hoặc khí,<br>"
                   "phải có kết cấu hoặc, khi cần, được bảo vệ để ngăn ngừa, trong phạm vi hợp "
                   "lý có thể, nguy hiểm phát sinh từ sự tiếp xúc đó.",
                   "Quy định 6, Quy định Điện tại Nơi làm việc 1989"))
    b.append(p("Bốn hạng mục tiếp xúc được liệt kê rõ ràng là:"))
    b.append(ul([
        "(a) hư hỏng cơ học, ví dụ va chạm hoặc rung động;",
        "(b) tác động của thời tiết, thiên tai, nhiệt độ hoặc áp suất;",
        "(c) tác động của điều kiện ẩm, bẩn, bụi hoặc ăn mòn;",
        "(d) bất kỳ chất dễ cháy hoặc nổ nào, kể cả bụi, hơi và khí.",
    ]))
    b.append(p("Âm hưởng của quy định mới, hiện đang có hiệu lực, rất giống với quy định trước "
               "đó. Mục tiêu cần đạt được được nêu rõ, và trong mục tiêu đó công nghiệp được "
               "trao tự do tối đa về phương thức đạt được."))
    b.append(p("Cách lập pháp nêu trên, dù phổ biến ở Anh, khác biệt đáng kể với pháp luật ở "
               "những nước như Đức, nơi luật pháp có xu hướng cụ thể hơn và đưa ra chi tiết hơn "
               "nhiều về các biện pháp phòng ngừa cần áp dụng. Tuy nhiên, hầu như không có bằng "
               "chứng cho thấy cách tiếp cận này hay cách kia cho kết quả an toàn tốt hơn. "
               "Cách tiếp cận của Anh đáng được khen ngợi vì tính linh hoạt tối đa, nhưng ngược "
               "lại, những người thực hành tại Anh phải đủ năng lực để xử lý sự linh hoạt được "
               "cho phép đó."))
    b.append(p("Đối với bụi, Đạo luật Nhà máy có thêm một quy định phản ánh bản chất khác của "
               "vật liệu này: khi bụi được phát thải, nó không phân tán như khí, hơi và sương "
               "mùi mà lắng xuống và tạo thành một lớp, có thể bị chuyển thành đám mây bất kỳ "
               "lúc nào do một tác động vật lý. Đó là Quy định 31(1), nêu:"))
    b.append(quote("Khi, liên quan đến bất kỳ công đoạn nghiền, sàng hoặc công đoạn khác phát "
                   "sinh bụi, có thể thoát ra bụi có tính chất và mức độ có khả năng nổ khi bắt "
                   "lửa, thì phải thực hiện mọi bước khả thi để ngăn ngừa vụ nổ đó bằng cách "
                   "bao kín thiết bị của công đoạn, bằng cách loại bỏ hoặc ngăn ngừa sự tích tụ "
                   "của bụi thoát ra dù đã bao kín, và bằng cách loại trừ hoặc bao kín hiệu quả "
                   "các nguồn đánh lửa có thể có.",
                   "Quy định 31(1), Đạo luật Nhà máy"))
    b.append(p("Dù không đề cập riêng đến thiết bị điện, quy định này vẫn bao gồm thiết bị điện "
               "như một nguồn đánh lửa có thể có và xác định phương pháp bảo vệ là bao kín hiệu "
               "quả. Điều này khả thi vì bụi không xâm nhập mạnh như khí, hơi hay sương mù và "
               "có thể bị loại trừ dễ dàng hơn nhiều."))
    b.append(p("Để làm nền tảng cho các quy định và đưa ra hướng dẫn, nhiều Tiêu chuẩn và Quy "
               "chuẩn Anh đã được xây dựng, chứa chi tiết về các phương thức tuân thủ được "
               "chấp nhận và các cơ sở chứng nhận của bên thứ ba, nhằm tạo sự tin tưởng cho "
               "người mua thiết bị điện. Tuy nhiên, các chương trình chứng nhận này không mở "
               "rộng đến việc lắp đặt và sử dụng."))
    b.append(p("Trước đây, khi các tiêu chuẩn chế tạo thiết bị còn hạn chế và thiếu chi tiết, "
               "cần rất nhiều chuyên môn trong các cơ quan chứng nhận, vì chính họ phải giải "
               "nghĩa các phát biểu chung trong tiêu chuẩn thực sự có nghĩa là gì. Không có gì "
               "ngạc nhiên khi cơ quan chứng nhận tại Anh liên kết với Cơ quan An toàn và Sức "
               "khỏe và tổ chức Safety in Mines Research Establishment, những đơn vị đã đóng "
               "góp lớn cho nền tảng công nghệ chi tiết hiện có."))
    b.append(p("Ngày nay, với các yêu cầu chi tiết hơn nhiều, mối liên hệ đó tuy vẫn hữu ích "
               "nhưng không còn là cần thiết. Không thể đánh giá thấp đóng góp của các tổ chức "
               "như Safety in Mines Research Establishment và Hiệp hội Nghiên cứu Điện (nay là "
               "ERA Technology Ltd), tổ chức sau thông qua các dự án được tài trợ bởi ngành, "
               "đối với các chi tiết hiện có trong tiêu chuẩn và quy chuẩn hiện hành."))
    b.append(p("Bên cạnh các tổ chức nêu trên, vốn chủ yếu liên quan đến việc chế tạo thiết bị, "
               "ngành công nghiệp nói chung và các tổ chức như Viện Dầu khí (Institute of "
               "Petroleum) đã thực hiện nhiều công việc; Viện đã xây dựng quy chuẩn thực hành "
               "an toàn mẫu cho ngành dầu khí."))
    b.append(p("Khác với các tổ chức chính phủ, ngành tập trung phần lớn công việc vào các vấn "
               "đề liên quan đến cách hình thành khu vực nguy hiểm và đến việc lắp đặt, bảo "
               "trì. Các công ty riêng lẻ cũng có đóng góp đáng kể. Ví dụ, Quy chuẩn Thực hành "
               "RoSPA/ICI về sử dụng thiết bị điện trong môi trường nổ trong công nghiệp hóa "
               "chất có lẽ là một trong những tài liệu tốt nhất từng được viết về loại hình này."))

    # ---- 1.5
    b.append(h3("Pháp luật Châu Âu", "European legislation"))
    b.append(p("Với việc Vương quốc Anh gia nhập EU, nước này chịu sự điều chỉnh của pháp luật "
               "EU trong lĩnh vực này. Đạo luật đầu tiên là Chỉ thị Môi trường Nổ 1975, còn được "
               "trích dẫn là 1975/76/117/EEC hoặc Chỉ thị 76/117/EEC ngày 18 tháng 12 năm 1975. "
               "Chỉ thị này giới hạn ở thiết bị cho rủi ro khí, hơi và sương mù, và là cái gọi "
               "là chỉ thị tùy chọn, chỉ quan tâm đến rào cản thương mại."))
    b.append(p("Chỉ thị không quy định cái gì phải được dùng trong môi trường nổ mà chỉ xác định "
               "thiết bị mà các quốc gia thành viên riêng lẻ không được tuyên bố là không phù "
               "hợp để sử dụng trong nước họ. Chỉ thị đề cập đến mọi bộ phận cấu thành của lắp "
               "đặt điện có thể dùng trong môi trường có khả năng nổ, ngoại trừ hầm mỏ, và "
               "Điều 4 mở đầu như sau:"))
    b.append(quote("Các Quốc gia Thành viên không được, vì lý do yêu cầu an toàn về thiết kế và "
                   "chế tạo thiết bị điện dùng trong Môi trường Có khả năng Nổ, cấm việc bán, "
                   "lưu thông tự do hoặc sử dụng đúng mục đích thiết bị điện được Chỉ thị bao "
                   "phủ.",
                   "Điều 4, Chỉ thị 76/117/EEC (1975)"))
    b.append(p("Dù điều này rõ ràng ngăn các quốc gia thành viên khăng khăng rằng mọi thiết bị "
               "dùng đều phải tuân thủ yêu cầu quốc gia riêng, nó không ngăn thiết bị tuân thủ "
               "yêu cầu quốc gia được dùng bên cạnh thiết bị tuân thủ Chỉ thị, dù hai bộ có thể "
               "khác nhau."))
    b.append(p("Chỉ thị 1975 cũng phải xác định yêu cầu đối với thiết bị để tuân thủ, dẫn đến "
               "sự nhấn mạnh đáng kể vào công việc của Ủy ban Tiêu chuẩn hóa Điện Châu Âu "
               "(CENELEC), tổ chức đã đưa ra loạt tiêu chuẩn rất chi tiết mô tả cấu tạo của "
               "thiết bị điện phù hợp (dải tiêu chuẩn Châu Âu EN 50---)."))
    b.append(p("Các tiêu chuẩn này sau đó được trao tư cách pháp lý nhờ được viện dẫn trong các "
               "chỉ thị bổ sung hoặc Công báo EU. Để bảo đảm thiết bị thực sự tuân thủ, chỉ thị "
               "cơ bản thừa nhận Dấu nhận biết Cộng đồng (Distinctive Community Mark, Hình 1.3), "
               "chỉ được gắn lên thiết bị "
               "phù hợp với tiêu chuẩn được viện dẫn trong các thỏa thuận bổ sung, và yêu cầu "
               "sự phù hợp đó được chứng nhận bằng Giấy chứng nhận phù hợp (Certificate of "
               "Conformity) hoặc Giấy chứng nhận kiểm tra (Inspection Certificate) do một cơ "
               "quan được phê duyệt cấp."))
    b.append(fig(3, FA.fig_f103()))
    b.append(p("Giấy chứng nhận phù hợp dành cho thiết bị tuân thủ một trong các tiêu chuẩn "
               "CENELEC được công nhận viện dẫn trong các chỉ thị bổ sung; Giấy chứng nhận kiểm "
               "tra dành cho thiết bị không tuân thủ nhưng được cơ quan phê duyệt xem là có độ "
               "an toàn ít nhất tương đương. Trường hợp sau, tuy nhiên, tất cả cơ quan được phê "
               "duyệt ở mọi quốc gia thành viên đều phải đồng ý về tính tương đương, vì thế dù "
               "tuyến này cho phép một số linh hoạt, nó ít khi được dùng do tính chất tốn kém "
               "và mất thời gian."))
    b.append(p("Chỉ thị Môi trường Nổ 1975 vẫn có hiệu lực đến năm 1996, khi nó được thay thế "
               "bởi một chỉ thị mới về vấn đề này, Chỉ thị 94/9/EC. Chỉ thị mới theo đuổi cách "
               "tiếp cận 'mới' của EU, trong đó các yêu cầu kỹ thuật được đưa vào ngay trong "
               "chỉ thị thay vì viện dẫn tiêu chuẩn."))
    b.append(p("Khác với chỉ thị trước, chỉ thị này có yêu cầu bắt buộc là sau một ngày giới hạn "
               "nhất định mọi thiết bị đưa vào sử dụng đều phải tuân thủ; và cũng khác với chỉ "
               "thị trước, nó gồm cả bụi, đưa thiết bị dùng cho rủi ro bụi vào màng lưới chứng "
               "nhận do chỉ thị tiền nhiệm thiết lập. Điều 2 của chỉ thị nêu:"))
    b.append(quote("Các Quốc gia Thành viên phải thực hiện mọi biện pháp thích hợp để bảo đảm "
                   "rằng thiết bị, hệ thống bảo vệ và thiết bị cài đặt mà Chỉ thị này áp dụng "
                   "chỉ được đưa ra thị trường và đưa vào sử dụng khi, được lắp đặt và bảo trì "
                   "đúng cách và dùng đúng mục đích, chúng không gây nguy hiểm cho sức khỏe và "
                   "an toàn của con người và, khi thích hợp, của động vật nuôi trong nhà hoặc "
                   "tài sản.",
                   "Điều 2, Chỉ thị 94/9/EC (1994)"))
    b.append(p("Vì các yêu cầu thiết yếu về sức khỏe và an toàn được đưa vào chỉ thị này, nó "
               "loại trừ trên thực tế mọi thiết bị khác. Việc loại trừ thiết bị không tuân thủ, "
               "kể cả thiết bị tuân thủ Chỉ thị 1976, sẽ có hiệu lực vào ngày 30 tháng 6 năm "
               "2003 (30 June 2003)."))
    b.append(p("Tiêu chuẩn Châu Âu không còn được viện dẫn trong chỉ thị mới nhưng sẽ được xác "
               "định trong Công báo EU là phương tiện được chấp nhận để tuân thủ chỉ thị, chứ "
               "không phải, như trước đây, là phương tiện duy nhất để tuân thủ. Ngoài ra, thiết "
               "bị và hệ thống không dùng điện cũng được đưa vào phạm vi của chỉ thị mới."))
    b.append(p("Cả hai chỉ thị được đưa vào hiệu lực tại Great Britain bằng Quy định Môi trường "
               "Nổ (Chứng nhận) 1990 và tại Bắc Ireland bằng pháp luật tương tự."))
    b.append(p("Các chỉ thị EU và pháp luật thực thi quốc gia nói trên chỉ đề cập đến cấu tạo "
               "của thiết bị, không đề cập đến lắp đặt và sử dụng, vẫn là vấn đề của luật quốc "
               "gia. Một chỉ thị đang được thảo luận trong EU sẽ giải quyết việc lắp đặt và sử "
               "dụng; tài liệu tham khảo 14 ghi đề xuất 6430/92 EN."))
    b.append(p("Chỉ thị đó vẫn ở giai đoạn khá sơ khởi nhưng ý nghĩa của nó rất sâu rộng. Nó "
               "chuẩn hóa yêu cầu đối với người sử dụng lao động trong việc xác định khu vực "
               "nguy hiểm (có biển báo), phân loại các khu vực đó và tham vấn, thông báo cho "
               "người lao động. Nó cũng chuẩn hóa yêu cầu sử dụng chuyên gia, tức nhân sự được "
               "đào tạo và có kinh nghiệm phù hợp, tại nơi làm việc để giám sát các lắp đặt."))
    b.append(p("Dù phần lớn nội dung là đúng và là lẽ thường, nó bổ sung mức độ trang trọng "
               "chưa từng có ở Anh, vì thế khi được ban hành có thể có tác động đáng kể đến "
               "công nghiệp Anh. Tuy vậy, phần lớn nội dung của chỉ thị đề xuất phù hợp với "
               "khuyến nghị và hướng dẫn trong cuốn sách này cũng như trong các tài liệu hướng "
               "dẫn khác."))

    # ---- 1.6
    b.append(h3("Chứng nhận", "Certification"))
    b.append(p("Như đã nêu, tại Anh không có yêu cầu cụ thể về chứng nhận đối với thiết bị dùng "
               "trong khu vực nguy hiểm, ngoài yêu cầu liên quan đến các chỉ thị EU về cấu tạo "
               "và tiếp thị thiết bị cùng luật quốc gia phát sinh. Tuy nhiên, chứng nhận đã trở "
               "thành chuẩn mực được chấp nhận, ít nhất trong những khu vực nguy hiểm hơn, và là "
               "một khía cạnh quan trọng của công nghệ."))
    b.append(p("Qua các năm, quan niệm về chứng nhận đã thay đổi: từ việc kiểm tra bởi một cơ "
               "quan chuyên gia về công nghệ khu vực nguy hiểm, như Safety in Mines Research "
               "Establishment và các đơn vị liên quan, dựa trên những tiêu chuẩn không rất cụ "
               "thể, sang việc kiểm tra bởi một phòng thí nghiệm thử nghiệm có năng lực, dựa "
               "trên những tiêu chuẩn rất chi tiết, không còn đòi hỏi mức chuyên môn cao như "
               "trước."))
    b.append(p("Trong EU hiện có khoảng 17 cơ quan được phê duyệt cho chứng nhận này, bao gồm "
               "các nước Châu Âu không thuộc EU và các nước Bắc Âu mà EU có thỏa thuận. Theo "
               "pháp luật EU, tất cả các cơ quan này đều tương đương và chứng nhận từ bất kỳ "
               "cơ quan nào cũng đủ để chứng minh thiết bị đáp ứng yêu cầu của tiêu chuẩn Châu "
               "Âu tương ứng."))
    b.append(p("Thiết bị được chứng nhận bởi một trong 17 cơ quan được phê duyệt thường được "
               "nhà sản xuất nhận diện bằng cách gắn Dấu nhận biết Cộng đồng lên thiết bị, bên "
               "cạnh bất kỳ dấu hiệu nào liên quan đến chứng nhận."))
    b.append(p("17 cơ quan được phê duyệt, xếp theo quốc gia, là:"))
    b.append(ul([
        "<b>Bỉ (EU)</b> - Institut Scientifique de Service Public (ISSEP).",
        "<b>Đan Mạch (EU)</b> - Danmarks Elektriske Materielkontrol (DEMKO).",
        "<b>Đức (EU)</b> - Physikalisch-Technische Bundesanstalt (PTB); Bergbau-Versuchsstrecke (BVS).",
        "<b>Tây Ban Nha (EU)</b> - Laboratorio Oficial Jose Maria Madariaga (LOM).",
        "<b>Pháp (EU)</b> - Institut National de l'Environnement Industriel et des Risques "
        "(INERIS); Laboratoire Central des Industries Electriques (LCIE).",
        "<b>Ý (EU)</b> - Centro Elettrotecnico Sperimentale Italiano (CESI).",
        "<b>Hà Lan (EU)</b> - NV KEMA.",
        "<b>Great Britain (EU)</b> - Electrical Equipment Certification Service (EECS); Sira "
        "Certification Service (SCS).",
        "<b>Bắc Ireland (EU)</b> - Industrial Science Centre (không có bộ chữ viết tắt).",
        "<b>Phần Lan (EU)</b> - Technical Research Centre of Finland (VTT).",
        "<b>Na Uy (không thuộc EU)</b> - Norges Elektriske Materiellkontroll (NEMKO).",
        "<b>Áo (EU)</b> - Bundesversuchs-und-Forschungsanstalt Arsenal (BVFA); TUV Austria.",
        "<b>Thụy Điển (EU)</b> - Swedish National Testing and Research Institute (SP).",
    ]))
    b.append(p("Cần lưu ý rằng trong trường hợp Industrial Science Centre tại Bắc Ireland, "
               "không có bộ chữ viết tắt nào đặt sau tên. Điều này có ý nghĩa, vì chính các chữ "
               "viết tắt là những ký hiệu xuất hiện trên giấy chứng nhận do các cơ quan được phê "
               "duyệt cấp. Lý do nằm ở quan hệ hơi đặc biệt giữa Great Britain và Bắc Ireland: "
               "pháp luật Anh trong lĩnh vực này không áp dụng cho Bắc Ireland, dẫn đến nhu cầu "
               "có một cơ quan được phê duyệt tại đây, dù tổ chức này không có kế hoạch cấp "
               "chứng nhận nào và hiện chắc chắn là không cấp."))
    b.append(p("Có thể cũng thấy lạ khi Safety in Mines Research Establishment, hay người kế "
               "tiếp là Phòng Thí nghiệm An toàn và Sức khỏe, không có mặt dù có lịch sử chuyên "
               "môn lâu dài trong lĩnh vực này. Đó là vì tổ chức này từng là một phần của Dịch vụ "
               "Dân sự Anh. Cơ quan nhà nước hiện nay là Electrical Equipment Certification "
               "Service, có cùng nguồn gốc và tiếp cận được cùng chuyên môn như Safety in Mines "
               "Research Establishment."))
    b.append(p("Một số cơ quan trong danh sách có logo, được thể hiện trong Hình 1.4 để hỗ trợ "
               "nhận diện."))
    b.append(fig(4, FB.fig_f104()))
    b.append(p("Giấy chứng nhận do tất cả các cơ quan được phê duyệt này cấp đều có cùng định "
               "dạng, giúp việc sử dụng dễ dàng bất kể nguồn gốc. Chúng xác định thiết bị được "
               "chứng nhận, cùng mã chứng nhận (mô tả sau) và nhà sản xuất. Một ví dụ về giấy "
               "chứng nhận điển hình được cho trong Hình 1.5."))
    b.append(fig(5, FB.fig_f105()))
    b.append(p("Điều cần lưu ý là giới hạn của giấy chứng nhận. Nó chỉ xác nhận thiết bị phù hợp "
               "với các yêu cầu cấu tạo chi tiết trong tiêu chuẩn được quy định và không đề cập "
               "đến lắp đặt, vốn thay đổi tùy theo quốc gia lắp đặt. Vì vậy cần cẩn trọng khi xem "
               "xét cách lắp đặt thiết bị, bảo đảm các yếu tố an toàn vốn có trong cấu tạo "
               "không bị vô hiệu hóa bởi phương thức lắp đặt."))
    b.append(p("Các cơ quan được phê duyệt trong danh sách họp định kỳ trong một nhóm công tác "
               "có tên Heads of Test Houses Liaison Committee (HOTL), do Ủy ban EU thành lập. "
               "Mục tiêu của nhóm là bảo đảm mọi cơ quan được phê duyệt dùng tiêu chuẩn theo "
               "cùng cách và trình bày giấy chứng nhận theo cùng cách. Nhóm không được dự định "
               "là cơ quan quyết định nghĩa của những phần chưa rõ trong tiêu chuẩn, dù tất "
               "yếu nó cũng dính vào hoạt động đó."))
    b.append(p("Việc làm rõ và giải thích tiêu chuẩn thuộc về các cơ quan soạn thảo tiêu chuẩn "
               "(trường hợp này là CENELEC), nhưng những cơ quan này bản chất là cồng kềnh, nên "
               "các thắc mắc về tiêu chuẩn có thể mất nhiều thời gian để giải quyết. Vì tính "
               "thương mại của việc dùng chứng nhận, HOTL đóng vai trò có giá trị trong việc "
               "cung cấp làm rõ tạm thời nhanh chóng trong lúc chờ quyết định của cơ quan soạn "
               "thảo, và các thành viên HOTL thông báo cho cơ quan đó mọi làm rõ tạm thời mà họ "
               "đã áp dụng."))
    b.append(p("Cơ quan soạn thảo sau đó có thể phê chuẩn hoặc bác bỏ các làm rõ đó tùy ý, theo "
               "thời gian của mình. Điều này thường không gây vấn đề cho người giữ giấy chứng "
               "nhận dựa trên một làm rõ của HOTL sau đó bị cơ quan soạn thảo bác bỏ, vì trừ khi "
               "có nguy hiểm rõ ràng được xác định liên quan đến quyết định của HOTL, giấy chứng "
               "nhận vẫn được giữ nguyên, dù các thành viên HOTL sẽ tự động áp dụng cách làm rõ "
               "chính thức ngay khi có cho các chứng nhận trong tương lai."))
    b.append(p("Nhiều cơ quan được phê duyệt cấp chứng nhận cho thiết bị phù hợp với tiêu chuẩn "
               "của chính họ hoặc tiêu chuẩn quốc gia, bên cạnh thiết bị phù hợp với tiêu chuẩn "
               "Châu Âu được viện dẫn trong chỉ thị. Những chứng nhận này không được chỉ thị bao "
               "phủ và việc chấp nhận chúng là vấn đề của từng người sử dụng. Điều này cũng đúng "
               "với chứng nhận do các cơ quan không được EU phê duyệt cấp, dù họ có thể là cơ "
               "quan quốc gia."))
    b.append(p("Khi các chứng nhận sau này liên quan đến tiêu chuẩn Châu Âu, chỉ cần xem xét chuyên "
               "môn của cơ quan chứng nhận không được phê duyệt; nhưng trong các trường hợp khác "
               "(ví dụ Factory Mutual Research Corporation và Underwriters Laboratories tại Hoa "
               "Kỳ), tiêu chuẩn mà thiết bị được chứng nhận, hay được 'listing' theo cách gọi ở "
               "Hoa Kỳ, khác biệt đáng kể, và cần xem xét cả ảnh hưởng của điều đó."))

    # ---- 1.7
    b.append(h3("Thông tin chứng nhận và ghi nhãn", "Certificate and labelling information"))
    b.append(p("Không có cách tắt thực sự để nhận diện thiết bị phù hợp, vì các bảng kèm theo "
               "giấy chứng nhận phù hợp và giấy chứng nhận kiểm tra chứa thông tin cần thiết cho "
               "người sử dụng. Những thông tin này luôn phải được cung cấp cho người mua thiết "
               "bị đã chứng nhận, và có nghĩa vụ pháp lý đối với nhà cung cấp trong phạm vi an "
               "toàn phụ thuộc vào thông tin đó. Tuy nhiên, có một mã hóa chuẩn thường xuất hiện "
               "trên cả giấy chứng nhận và nhãn, như sau."))
    b.append(p("<b>Chữ viết tắt của cơ quan chứng nhận.</b> Thường xuất hiện dưới dạng một bộ chữ "
               "viết tắt, ví dụ PTB, LCIE, EECS hoặc SCS."))
    b.append(p("<b>Số giấy chứng nhận.</b> Xuất hiện như sau:"))
    b.append(p("<b>Ex 96 D 2 123 (X)</b>"))
    b.append(p("Các phần của mã này có nghĩa như sau:"))
    b.append(ul([
        "Ex - thiết bị được bảo vệ chống nổ.",
        "96 - hai chữ số cuối của năm cấp.",
        "D - trạng thái sửa đổi của tiêu chuẩn dùng để chứng nhận.",
        "2 - phương pháp bảo vệ chính: 1 = chống cháy nổ hoặc áp lực; 2 = an toàn nội tại; "
        "3 = an toàn tăng cường; 4 = thiết bị loại N (n); 5 = bảo vệ đặc biệt; 6 = xe dùng "
        "pin (thường dùng nhiều hơn một loại bảo vệ); 7 = ngâm dầu hoặc nhồi bột.",
        "123 - số thứ tự của giấy chứng nhận trong năm.",
        "X - cho thấy có điều kiện lắp đặt đặc biệt (bất thường) liên quan đến thiết bị và "
        "được nêu trong giấy chứng nhận. Nếu xuất hiện U thay vì X, hoặc không có hậu tố, thiết "
        "bị được xem là linh kiện và không được dùng trừ khi được lắp vào thiết bị khác và được "
        "chứng nhận tiếp.",
    ]))
    b.append(p("<b>Mã bảo vệ.</b> Thường xuất hiện ở dạng sau:"))
    b.append(p("<b>EEx d IIC T4</b>"))
    b.append(p("Ý nghĩa của các ký hiệu này là:"))
    b.append(ul([
        "E - thiết bị tuân thủ tiêu chuẩn Châu Âu; ký hiệu này không có nếu không đúng như vậy.",
        "Ex - thiết bị được bảo vệ chống nổ.",
        "d - loại bảo vệ được dùng: o = ngâm dầu; p = cấp áp lực; q = nhồi bột; d = vỏ chống "
        "cháy nổ; e = an toàn tăng cường; i = an toàn nội tại (thường có thêm hậu tố như ia hoặc "
        "ib); m = đóng kín; n = thiết bị loại n (đôi khi là N để chỉ tiêu chuẩn quốc gia Anh, "
        "không phải tiêu chuẩn Châu Âu).",
        "IIC - bầu khí quyển nổ mà thiết bị được thử đánh lửa bằng tia lửa: IIA - hỗn hợp lý "
        "tưởng propane và không khí; IIB - hỗn hợp lý tưởng ethylene và không khí; IIC - hỗn "
        "hợp lý tưởng hydrogen và không khí. Khi loại bảo vệ ngăn được tia lửa, chữ cái được "
        "bỏ và chỉ còn II, vì không cần phân nhóm.",
        "T4 - nhiệt độ tối đa đạt được ở bất kỳ bộ phận có khả năng đánh lửa nào, nghĩa là không "
        "bộ phận nào vượt quá T1 450 °C, T2 300 °C, T3 200 °C, T4 135 °C, T5 100 °C hoặc T6 85 °C.",
    ]))
    b.append(p("Nhiệt độ môi trường 40 °C được giả định trừ khi có quy định khác trên nhãn và "
               "giấy chứng nhận."))
    b.append(p("Trong lịch sử đã có các phương pháp mã hóa khác ở Châu Âu và vẫn có cách khác "
               "tại Hoa Kỳ, được thể hiện trong Bảng 1.1 và Bảng 1.2. Tuy nhiên cần lưu ý rằng "
               "vì cơ sở thông tin hơi khác nhau, mối quan hệ giữa các hệ thống chỉ là tương đối."))
    b.append(table(_T11_HEADER_VI, _T11_ROWS_VI,
                   caption="Bảng 1.1. Mối quan hệ giữa các hệ thống phân nhóm và phân loại."))
    b.append(p("<small>" + _T11_FN_VI + "</small>"))
    b.append(p("Các hệ thống phân loại nhiệt độ có quan hệ như Bảng 1.2. Một lần nữa, mối quan "
               "hệ này chỉ là tương đối."))
    b.append(table(_T12_HEADER_VI, _T12_ROWS_VI,
                   caption="Bảng 1.2. Mối quan hệ giữa các hệ thống phân loại nhiệt độ."))
    b.append(p("<small>" + _T12_FN_VI + "</small>"))

    # ---- 1.8
    b.append(h3("Tương lai của chứng nhận", "The future of certification"))
    b.append(p("Như đã nêu, tình hình chứng nhận chịu ảnh hưởng đáng kể bởi Chỉ thị 1990, có "
               "hiệu lực từ đầu năm 1996, tức Chỉ thị 94/9/EC. Dù ban đầu chỉ thị này dựa vào "
               "tiêu chuẩn Châu Âu được viện dẫn trong Công báo Châu Âu, chắc chắn độ rộng của "
               "các yêu cầu thiết yếu trong chỉ thị cuối cùng sẽ được áp dụng."))
    b.append(p("Vì các yêu cầu thiết yếu được diễn đạt bằng thuật ngữ chung chung hơn nhiều so "
               "với tiêu chuẩn, các cơ quan được phê duyệt sẽ phải quay lại việc giải thích "
               "chuyên gia đối với các yêu cầu chung chung hơn, gần như đã làm trước khi có các "
               "tiêu chuẩn chi tiết. Do đó, mức độ chuyên môn của các cơ quan chứng nhận một lần "
               "nữa trở nên tối quan trọng."))
    b.append(p("Vì mục đích đó, nhóm HOTL sẽ có ý nghĩa lớn hơn nhiều, và khó có thể có đủ chuyên "
               "môn nếu không đưa chuyên môn công nghiệp vào. Cách làm điều này mà không biến "
               "nhóm thành một cơ quan soạn thảo tiêu chuẩn cồng kềnh chắc chắn sẽ trở thành "
               "vấn đề được tranh luận nhiều trong tương lai không xa."))
    b.append(p("Việc đưa vào thiết bị không dùng điện, vốn có mức độ chuẩn hóa chi tiết thấp hơn "
               "nhiều trong lĩnh vực này, sẽ khiến vấn đề chứng nhận theo yêu cầu của chỉ thị mới "
               "xuất hiện sớm hơn. Không chỉ các cơ quan hiện được phê duyệt sẽ không có tiêu "
               "chuẩn chi tiết nào, họ nhiều khả năng chỉ có chuyên môn hạn chế trong các lĩnh "
               "vực không dùng điện được bao phủ. Kết quả là rất có thể một bộ cơ quan được phê "
               "duyệt mới sẽ xuất hiện, tách biệt với nhóm trong lĩnh vực điện."))
    b.append(p("Một nội dung khác được đưa vào chỉ thị mới là yêu cầu nhà sản xuất hoặc nhà cung "
               "cấp, trong hầu hết trường hợp, phải có hệ thống quản lý chất lượng và hệ thống "
               "đó cũng phải được chứng nhận theo một bộ yêu cầu tương tự BS/EN/ISO 9002 (dù các "
               "yêu cầu lại được ghi trong chỉ thị). Điều này tạo sự tin tưởng hơn cho người dùng "
               "rằng hàng mua phản ánh chính xác chứng nhận, nhưng vì yêu cầu quản lý chất lượng "
               "lại rất chủ quan, nó sẽ gây không ít vấn đề giải thích và là lý do tiếp tục cần "
               "mở rộng HOTL."))
    b.append(p("Đường đi đến chứng nhận theo chỉ thị mới được thể hiện trong Hình 1.6. Khi nhà "
               "sản xuất đã có giấy chứng nhận kiểu cho sản phẩm, dùng hệ thống trong Hình 1.6(a) "
               "theo tiêu chuẩn EN tương ứng hoặc các yêu cầu thiết yếu của chỉ thị, thì các "
               "bước minh họa trong Hình 1.6(b) được áp dụng cho thiết bị category 1 và category 2."))
    b.append(fig(6, FB.fig_f106()))
    b.append(p("Đối với thiết bị category 1 (dùng cho Zone 0), cơ quan thông báo chứng nhận hệ "
               "thống chất lượng sản xuất theo BS/EN/ISO 9002 và giám sát hệ thống cùng sản phẩm; "
               "hoặc nhà sản xuất tự chịu trách nhiệm vận hành hệ thống chất lượng và cơ quan "
               "thông báo kiểm tra, thử nghiệm toàn bộ thiết bị."))
    b.append(p("Đối với thiết bị category 2 (dùng cho Zone 1), cơ quan thông báo chứng nhận hệ "
               "thống chất lượng theo BS/EN/ISO 9003 và giám sát hệ thống; hoặc nhà sản xuất tự "
               "chịu trách nhiệm vận hành hệ thống chất lượng và cơ quan thông báo kiểm tra toàn "
               "bộ thiết bị được sản xuất."))
    b.append(p("Đối với thiết bị category 3 (dùng cho Zone 2), không cần chứng nhận bởi cơ quan "
               "được phê duyệt (thông báo). Nhà sản xuất xác nhận sự tuân thủ bằng bản khai và "
               "việc gắn dấu CE."))

    b.append(note("<b>Về bản dịch.</b> Đây là bản dịch không chính thức dùng cho mục đích học "
                  "tập. Toàn bộ tám mục (1.1-1.8), hai bảng với chú thích, sáu hình được vẽ lại "
                  "dạng vector và mười sáu tài liệu tham khảo được giữ nguyên theo nguyên bản."))
    b.append(refs(_REFS_VI))
    return "".join(b)


# ==================================================================== EN
def body_en():
    b = []
    b.append(h2(TITLE_EN, TITLE_EN))
    b.append(lead("Explosion protection for electrical installations · historic incidents · "
                  "UK and EU legislation · certification · marking · future directions."))

    # ---- opening pages (un-numbered introduction)
    b.append(p("Where combustible or flammable materials are stored or processed, there is in "
               "most circumstances a possibility that they may leak or otherwise produce what "
               "may be described as an explosive atmosphere in conjunction with the oxygen "
               "present in air. This is true for gases, vapours, mists and dusts. Because "
               "electricity is widely used in industries and other places where such explosive "
               "atmospheres can occur, the propensity of electrical energy to create sparking or "
               "hot surfaces presents a possibility that the explosive atmosphere may be "
               "ignited, with resultant fire or explosion."))
    b.append(p("This hazard has been recognised for many decades, almost since electricity was "
               "introduced into mining and other industries. The precautions taken to overcome "
               "this problem date, in their basic inception, to the turn of the twentieth "
               "century and before."))
    b.append(p("There is no way in which explosions can be totally prevented in industries where "
               "explosive atmospheres can occur, as all human endeavour is fallible. It is "
               "necessary to develop our operations to a degree where such explosions are so "
               "rare that their risk is far outweighed by the benefits of the processes in which "
               "they may occur."))
    b.append(p("The coalmining industry illustrates this balance: the overall risks associated "
               "with working underground, of which explosions are one constituent, have been "
               "seen as justifiable on the basis of society's need for fuel. The risks are "
               "minimised as far as possible, but only to a level consistent with the need to win "
               "coal, and accidents still occur. What remains true is that the risk of these "
               "accidents has been reduced to a level acceptable to our society and particularly "
               "to those working in the industry."))
    b.append(p("That is not to say that when a risk is identified by an incident nothing is done. "
               "We always learn from these and invariably they result in changes to our operating "
               "systems and equipment in order to minimise the risk of a repeat. Notwithstanding "
               "all of our efforts, however, accidents of significant proportion still occur "
               "with a degree of regularity which causes us all concern."))

    # ---- 1.1
    b.append(h3("Examples of historic incidents", "Examples of historic incidents"))
    b.append(p("The following are examples of the more significant incidents occurring in the "
               "UK. Although they were not necessarily caused by electricity, in at least one of "
               "the cases there was a suspicion of electrical initiation, and electricity, as has "
               "already been indicated, is seen as an obvious igniting agent."))
    b.append(ul([
        "<b>Senghennyd colliery - 1913.</b> An underground firedamp (methane) explosion caused a "
        "roof fall which cut off over 400 miners from a shaft in a burning section of the "
        "colliery. Most of them died from the resulting suffocation.",
        "<b>Flixborough - 1974.</b> A modification to a process plant, said by the accident "
        "report not to have been properly considered, was identified as causing a major release "
        "of flammable gas resulting in an immense aerial explosion. Loss of life on the plant was "
        "mercifully low (probably because it was Saturday) but damage to the plant and "
        "surrounding residential and other properties was significant.",
        "<b>Piper Alpha - 1988.</b> This oil platform was effectively destroyed by a gas "
        "explosion which resulted from a major release of gas suggested to be due to erroneous "
        "process operation. The initial and subsequent explosions and fire effectively prevented "
        "controlled evacuation of the platform and heavy loss of life was caused.",
        "<b>Texaco Pembroke refinery - 1994.</b> A major vapour explosion occurred leading to a "
        "major fire which was extremely difficult to extinguish. The refinery burned for a "
        "considerable time with consequent adverse effects on the local environment. Casualties "
        "were light but the refinery suffered considerable damage.",
    ]))
    b.append(p("The above examples clearly demonstrate the dangers present, particularly in "
               "locations where escape of personnel is difficult. It is essential, therefore, "
               "that all involved have an understanding of the technology used to minimise the "
               "risk of explosion."))
    b.append(p("Even where incidents have been taken into account in design, accidents of "
               "significant proportion still occur, and each in its turn usually results in "
               "changes to operating systems and equipment so as to minimise the chance of a "
               "repeat."))

    # ---- 1.2
    b.append(h3("Technological approach", "Technological approach"))
    b.append(p("The objective of the technology associated with the use of electrical equipment "
               "in potentially explosive atmospheres is to reduce the risk of an explosion to an "
               "acceptable level. To have an explosion three elements are necessary, namely fuel, "
               "oxygen and a source of ignition (see Fig. 1.1)."))
    b.append(fig(1, FA.fig_f101()))
    b.append(p("Oxygen is present in air to a sufficient extent to support combustion and cannot "
               "normally be excluded, which leaves only the fuel and ignition sources as "
               "elements to which influence can be applied. This has formed the basis for "
               "technology since the turn of the twentieth century when the problem was first "
               "identified in the mining industry."))
    b.append(p("While in other areas of risk the approach is often based much more heavily on "
               "statistical analysis than is the case here, the approach in respect of explosive "
               "atmospheres is well established and accepted, having been in use since the early "
               "1900s. The presence of many subjective areas which make statistical analysis "
               "difficult has also limited the statistical approach, although there have been "
               "many attempts to apply such an approach. Thus current and foreseeable future "
               "technology is based upon that currently used, and there is no indication of a "
               "radical change to readdress the technology on a statistical basis as is done, for "
               "example, in the nuclear industry."))
    b.append(p("A typical attempt to analyse the statistical level of security achieved in "
               "relation to gas, vapour and mist releases is that in a paper by W. A. Hicks and "
               "K. J. Brown at the 1971 Institution of Electrical Engineers Conference, which "
               "identified the risk of ignition as between 10<sup>-5</sup> and 10<sup>-14</sup>. "
               "Many others however have produced different figures as the assumptions made in "
               "respect of the subjective elements of the technology vary."))
    b.append(p("The technology is currently based upon the identification of the risk of an "
               "explosive atmosphere being present in a particular place coupled with the "
               "identification of the likelihood of electrical equipment within the explosive "
               "atmosphere malfunctioning in a way which would cause it to become a source of "
               "ignition coincident with the presence of that explosive atmosphere."))
    b.append(p("The objectives are not just to identify these coincidences but to utilise the "
               "information so obtained to influence the design of particular process plants and "
               "similar operational situations in a way so as to minimise the risk of creation "
               "of an explosive atmosphere, and hence the risk of an explosion due to electrical "
               "installations."))
    b.append(p("To this end, the generality of the approach is to seek out situations where an "
               "explosive atmosphere is normally present of necessity due to the process "
               "involved, situations where the likelihood of its presence is high, and situations "
               "where the likelihood of its presence is low but identifiable. In this scenario "
               "catastrophe does not play a part and although it is necessary to plan for "
               "catastrophe such plans are by and large outside the scope of this technology."))
    b.append(p("In addition this technology should not be used in isolation but as part of an "
               "overall safety strategy for a location where the problem occurs. Having "
               "identified the possible presence of an explosive atmosphere it is then part of "
               "the technology to identify those electrical installations which really need to "
               "be present rather than those which convenience would make desirable, and ensure "
               "that these are protected in a way which makes the overall risk of an explosion "
               "sufficiently low."))

    # ---- 1.3
    b.append(h3("History of development", "History of development"))
    b.append(p("The use of electrical equipment in explosive atmospheres was originally the "
               "province of the mining industry and, although the technology was used in surface "
               "industry, significant developments in this latter area are more contemporary "
               "being to a large extent post war."))
    b.append(p("While the present approach is to minimise the chance of a release of flammable "
               "material, or where a release occurs to minimise the build up of the material in "
               "the atmosphere, it is probably somewhat surprising that in early coal production "
               "the method used to deal with releases of methane (firedamp) was to deliberately "
               "burn off the explosive atmosphere."))
    b.append(p("This was done by a specifically designated miner called the 'firelighter'. The "
               "method used took advantage of the fact that methane is lighter than air (relative "
               "density is around 0.55) and thus methane/air mixtures collected preferentially "
               "near the roof of the workings. Warning was given by changes in colour of the "
               "flames of the lamps used by miners and the workings were then cleared."))
    b.append(p("A torch was inserted into the methane air cloud, igniting it and burning off the "
               "methane. The technique fell into disrepute for obvious reasons and was replaced "
               "by the introduction of the use of ventilation to restrict the possibility of "
               "explosive atmospheres forming and the employment of a safety lamp (Fig. 1.2) to "
               "minimise the risk of ignition."))
    b.append(fig(2, FA.fig_f102()))
    b.append(p("The introduction of electricity in the latter part of the nineteenth century and "
               "the early part of the twentieth century led to significant other risks being "
               "identified. Initially electricity was utilised for lighting and motive force."))
    b.append(p("The lighting was typically provided by incandescent filament lamps, none of the "
               "more sophisticated lamps having been developed at the time, and the motive force "
               "usually by either dc or wound rotor ac machines which were initially typical of "
               "the motors available. Both lighting and machines required control equipment "
               "(often as simple as a switch) but this equipment also introduced risks "
               "associated with hot surfaces and sparks, together with the possibility of the "
               "presence of both methane and coal dust."))
    b.append(p("The solutions to these problems in relation to gas, vapour and mist releases were "
               "developed in both the UK and Germany along very similar lines and in very similar "
               "time scales. In Germany the organisation principally involved was what is now "
               "known as the Berggewerkschaftlichen Versuchsstrecke (BVS) and Dr Ing. Carl Beyling "
               "of that organisation was awarded the Gold Medal of the UK Institution of Mining "
               "Engineers in 1938 for his work in this area."))
    b.append(p("In the UK a similar but governmental organisation had significant involvement in "
               "similar developments. This is now as the Health and Safety Laboratory of the "
               "Health and Safety Executive but is better known by its earlier title of the "
               "Safety in Mines Research Establishment."))
    b.append(p("The initial technique for protection of electrical equipment was what we now know "
               "as flameproof enclosure and intended for high-power electrical equipment where "
               "the level of electrical energy necessary for equipment operation was always "
               "sufficient to initiate ignition if released in a spark or as heat. This was well "
               "developed as early as 1905."))
    b.append(p("It was rapidly followed by a second technique, now known as the intrinsically safe "
               "circuit. This second technique was developed for mine signalling systems and "
               "relied upon the fact that intelligence could be transmitted by very small amounts "
               "of electrical energy which, if released, was not sufficient to ignite any "
               "expected explosive atmosphere. The advantage of this latter technique was in the "
               "flexibility which it offered as large heavy protective enclosures were not "
               "necessary."))
    b.append(p("Initially these two techniques were developed for the mining industry where "
               "methane was the most sensitive flammable material present but as the techniques "
               "began to be applied to surface industry two significant differences in approach "
               "became rapidly apparent. First it was recognised that releases of flammable "
               "material were normally from installed equipment and more predictable in quantity "
               "and frequency, and second the recognition that far from dealing with one gas and "
               "one dust, as in mining, surface industry was dealing with a myriad of different "
               "materials each with its own characteristics."))
    b.append(p("This recognition led to development of the technique of area classification to "
               "define the risks of explosive atmospheres occurring in specific locations and "
               "the development of additional types of protection to more readily reflect the "
               "varying levels of hazard which could be identified. It is these two factors that "
               "led to the current UK and international industrial practice which this book seeks "
               "to describe."))

    # ---- 1.4
    b.append(h3("UK legislation", "UK legislation"))
    b.append(p("The basic historic UK legislation covering the use of electrical equipment in "
               "explosive atmospheres is that included in the Electricity Regulations of the "
               "Factories Acts. Regulation 27 of these regulations states:"))
    b.append(quote("All conductors and apparatus exposed to the weather, wet, corrosion, "
                   "inflammable surroundings or explosive atmosphere, or used in any process or "
                   "for any special purpose other than for lighting or power, shall be so "
                   "constructed or protected, and such special precautions shall be taken as may "
                   "be necessary adequately to prevent danger in view of such exposure or use.",
                   "Regulation 27, Electricity Regulations (Factories Acts)"))
    b.append(p("This regulation clearly states the objective to be achieved but does not define "
               "the method of its achievement. While one may be concerned at this, its intent is "
               "to allow the widest possible range of approaches to the achievement of the "
               "required level of security and thus to give the maximum freedom of operation to "
               "industry, while at the same time laying upon that industry the requirement to "
               "achieve an adequate level of security in its operation."))
    b.append(p("Regulation 27 remained in force, even after the enactment of the Health and "
               "Safety at Work Act 1974, until replaced by Regulation 6 of the 1989 Electricity at "
               "Work Regulations. Regulation 6 states:"))
    b.append(quote("Electrical equipment which may reasonably foreseeably be exposed to:-<br>"
                   "(a) mechanical damage;<br>"
                   "(b) the effects of weather, natural hazards, temperature or pressure;<br>"
                   "(c) the effects of wet, dirty, dusty or corrosive conditions; or<br>"
                   "(d) any flammable or explosive substance, including dusts, vapours or "
                   "gases,<br>"
                   "shall be of such construction or as necessary protected as to prevent, so far "
                   "as is reasonably practicable, danger arising from such exposure.",
                   "Regulation 6, Electricity at Work Regulations 1989"))
    b.append(p("The four categories of exposure are set out explicitly as:"))
    b.append(ul([
        "(a) mechanical damage, such as impact or vibration;",
        "(b) the effects of weather, natural hazards, temperature or pressure;",
        "(c) the effects of wet, dirty, dusty or corrosive conditions;",
        "(d) any flammable or explosive substance, including dusts, vapours and gases.",
    ]))
    b.append(p("The tenor of this new regulation, now current, is very much the same as its "
               "predecessor. The objective to be achieved is specified and within that objective "
               "maximum freedom is given to industry in methods of its achievement."))
    b.append(p("The above method of legislating, while common in the UK, contrasts significantly "
               "with legislation in countries such as Germany where legislation tends to be more "
               "specific, giving much more detail in respect of the precautions to be adopted. "
               "There is, however, little or no evidence available to suggest that one or the "
               "other approach produces a better result as far as safety is concerned. Thus, the "
               "UK approach has much to commend it providing as it does maximum flexibility but, "
               "conversely, practitioners in the UK must be fully competent to deal with the "
               "flexibility permitted."))
    b.append(p("In respect of dusts, a further regulation exists in the Factories Acts which "
               "reflects the different nature of such materials, in that when a dust is released "
               "it does not disperse as is the case with gases, vapours and mists but settles and "
               "forms a layer which can be re-formed as a cloud at any time by any sort of "
               "physical intervention. The regulation in question is Regulation 31(1) which "
               "states:"))
    b.append(quote("When, in connection with any grinding, sieving, or other process giving rise "
                   "to dust, there may escape dust of such a character and to such an extent as "
                   "to be liable to explode on ignition, all practicable steps shall be taken to "
                   "prevent such an explosion by enclosure of the plant used in the process, and "
                   "by removal or prevention of accumulation of any dust that may escape in spite "
                   "of the enclosure, and by exclusion or effective enclosure of possible sources "
                   "of ignition.",
                   "Regulation 31(1), Factories Acts"))
    b.append(p("While not specifically referring to electrical equipment, this regulation "
               "includes it as a possible source of ignition and identifies the method of "
               "protection as effective enclosure. This is possible as dust is nothing like as "
               "penetrative as gas, vapour or mist and can effectively be excluded with much less "
               "difficulty."))
    b.append(p("To underpin these regulations and give guidance, many British Standards and Codes "
               "containing details of acceptable methods of compliance and third-party "
               "certification facilities have been developed to give purchasers of electrical "
               "equipment confidence. These certification schemes do not, however, extend to "
               "installation and use."))
    b.append(p("In the past, when equipment construction Standards were limited and lacked "
               "detail, a great deal of expertise was necessary within the certification bodies "
               "as it was they who had to interpret what general statements within Standards "
               "actually meant. Thus, it was not surprising that the certification body in the UK "
               "was associated with the Health and Safety Executive and the Safety in Mines "
               "Research Establishment organisations which made great contributions to the more "
               "detailed technological base currently available."))
    b.append(p("Now, with much more detailed requirements, this relationship, while remaining "
               "useful, is no longer necessary. The contribution of organisations such as the "
               "Safety in Mines Research Establishment, and the Electrical Research Association "
               "(now ERA Technology Ltd), the latter through its industry sponsored project "
               "work, to the detail existing in current Standards and Codes cannot however be "
               "overstated."))
    b.append(p("In addition to the above organisations, which were principally associated with "
               "the construction of equipment, a great deal of work was done by industry in "
               "general and organisations such as The Institute of Petroleum which produced a "
               "model code of safe practice for the oil industry."))
    b.append(p("Industry, unlike the governmental organisations, concentrated much of its work on "
               "the matters associated with how hazardous areas were formed and matters "
               "associated with installation and maintenance. Individual companies also made "
               "significant contributions and, as an example of this, the RoSPA/ICI Code of "
               "Practice covering use of electrical equipment in explosive atmospheres in the "
               "chemical industry is probably one of the finest documents of its type ever "
               "produced."))

    # ---- 1.5
    b.append(h3("European legislation", "European legislation"))
    b.append(p("With the accession of the UK to the EU it became subject to EU legislation in "
               "this field. The first such legislation produced was the Explosive Atmospheres "
               "Directive 1975, also cited as 1975/76/117/EEC or Directive 76/117/EEC of 18 "
               "December 1975. This Directive was limited to equipment for gas, vapour and mist "
               "risks and was what is described as an optional Directive, solely concerned with "
               "barriers to trade."))
    b.append(p("It did not dictate what must be used in explosive atmospheres but merely "
               "identified equipment which could not be defined by individual member states as "
               "unsuitable for use in their country. The Directive referred to all constituent "
               "parts of electrical installations capable of use in potentially explosive "
               "atmospheres, other than mines, and its Article 4 set the scene as follows:"))
    b.append(quote("Member States may not, on grounds of safety requirements for the design and "
                   "manufacture of electrical equipment for use in Potentially Explosive "
                   "Atmosphere, prohibit the sale or free movement or the use, for its proper "
                   "purpose of the electrical equipment (covered by the Directive).",
                   "Article 4, Directive 76/117/EEC (1975)"))
    b.append(p("While this clearly prevented individual member countries from insisting that all "
               "equipment used must comply with individual national requirements, it did not "
               "prevent equipment complying with national requirements from use in addition to "
               "that complying with the Directive even though these could differ."))
    b.append(p("The 1975 Directive also had to define what was required of equipment to comply "
               "with it, and this led to considerable emphasis on the work of the European "
               "Committee for Electrical Standardization (CENELEC) which produced a range of very "
               "detailed Standards describing the construction of suitable electrical equipment "
               "(the EN 50--- range of European Standards)."))
    b.append(p("These Standards were then given legal status by being referred to in "
               "Supplementary Directives or the EU Journal. To ensure that equipment did indeed "
               "comply the basic Directive recognised the Distinctive Community Mark (Fig. 1.3) "
               "which could only be affixed to equipment in compliance with the Standards "
               "referred to in the Supplementary arrangements and required that this compliance "
               "be attested by a Certificate of Conformity or Inspection Certificate issued by an "
               "approved body."))
    b.append(fig(3, FA.fig_f103()))
    b.append(p("The Certificate of Conformity was for equipment which complied with one of the "
               "recognised CENELEC Standards referred to in the Supplementary Directives, and the "
               "Inspection Certificate for equipment which did not comply but was considered by "
               "the approved body to be of at least equivalent safety. In this latter case, "
               "however, all of the approved bodies in all member states had to agree on "
               "equivalence and thus, although this route allowed some flexibility, it was seldom "
               "used due to its expensive and time consuming nature."))
    b.append(p("The Explosive Atmospheres Directive 1975 remained in force until 1996 when it was "
               "superseded by a new Directive on the subject, Directive 94/9/EC. The new Directive "
               "followed the EU 'new approach' in which the technical requirements were included "
               "within the Directive, rather than by reference to Standards."))
    b.append(p("Unlike its predecessor, in this Directive there was a mandatory requirement that "
               "after a certain cut-off date all equipment put into use must of necessity comply "
               "with it and, unlike its predecessor, included dusts - bringing equipment for use "
               "in dust risks into the certification net set up by its predecessor. Article 2 of "
               "this Directive states:"))
    b.append(quote("Member States shall take all appropriate measures to ensure that the "
                   "equipment, protective systems and devices to which this Directive applies may "
                   "be placed on the market and put into service only if, when properly installed "
                   "and maintained and used for their intended purpose, they do not endanger the "
                   "health and safety of persons and, where appropriate, domestic animals or "
                   "property.",
                   "Article 2, Directive 94/9/EC (1994)"))
    b.append(p("As the essential requirements for health and safety are included in this Directive "
               "it effectively excludes all other equipment. The exclusion of non-complying "
               "equipment (including that complying with the 1976 Directive) will come into force "
               "in on 30 June 2003."))
    b.append(p("European Standards are no longer referred to in the new Directive but will be "
               "identified in the EU Journal as acceptable as a means of compliance with the "
               "Directive (but not, as before, the only means of compliance). In addition "
               "non-electrical equipment and systems have been brought into the scope of the new "
               "Directive."))
    b.append(p("Both of the Directives are brought into effect in Great Britain by the Explosive "
               "Atmosphere (Certification) Regulations 1990 and in Northern Ireland by similar "
               "legislation."))
    b.append(p("The EU Directives and National Implementation legislation referred to above "
               "refer only to the construction of equipment and not to its installation and use "
               "which is still a matter for National Law. A Directive is in discussion within the "
               "EU however which will address matters of installation and use; reference 14 records "
               "the proposal 6430/92 EN."))
    b.append(p("This Directive is still at a relatively early stage but its implications are far "
               "reaching. It formalises the requirements on employers to identify hazardous areas "
               "(with notices), to classify such areas and to consult with and inform employees. "
               "It also formalises the requirement for the use of experts (properly trained and "
               "experienced personnel) in the workplace to oversee installations."))
    b.append(p("While much of what is included is correct and is commonsense, it adds a degree of "
               "formality not hitherto seen in the UK and thus, when promulgated, may have a "
               "significant effect on UK industry. Having said that, much of what is in the "
               "proposed Directive is in accordance with the recommendations and guidance in this "
               "book and other guides."))

    # ---- 1.6
    b.append(h3("Certification", "Certification"))
    b.append(p("As has been stated there is no specific requirement for certification in respect "
               "of equipment used in hazardous areas in the UK, other than that associated with "
               "the EU Directives associated with construction and marketing of equipment and "
               "ensuing National Law. Certification has, however, become accepted as the norm, at "
               "least in the more hazardous of the affected areas and is an important aspect of "
               "the technology."))
    b.append(p("It must be noted however that over the years the vision of certification has "
               "changed from that of inspection by a body expert in hazardous area technology, "
               "such as the Safety in Mines Research Establishment and its associates, against "
               "not very specific standards, to inspection by a competent test laboratory against "
               "very detailed standards not requiring anything like the previous level of "
               "expertise."))
    b.append(p("Within the EU there are now some 17 approved bodies for such certification, "
               "including the non-EU European and Scandinavian countries with whom the EU has "
               "agreements. As far as EU legislation is concerned, these are all equivalent and a "
               "certificate from any one of them is sufficient to demonstrate that the equipment "
               "satisfies the requirements of the appropriate European Standard."))
    b.append(p("Equipment which is certified by any one of these 17 approved bodies is normally "
               "identified by the manufacturer by marking the apparatus with the Distinctive "
               "Community Mark in addition to any marking associated with the certification."))
    b.append(p("The 17 approved bodies, grouped by country, are:"))
    b.append(ul([
        "<b>Belgium (EU)</b> - Institut Scientifique de Service Public (ISSEP).",
        "<b>Denmark (EU)</b> - Danmarks Elektriske Materielkontrol (DEMKO).",
        "<b>Germany (EU)</b> - Physikalisch-Technische Bundesanstalt (PTB); "
        "Bergbau-Versuchsstrecke (BVS).",
        "<b>Spain (EU)</b> - Laboratorio Oficial Jose Maria Madariaga (LOM).",
        "<b>France (EU)</b> - Institut National de l'Environnement Industriel et des Risques "
        "(INERIS); Laboratoire Central des Industries Electriques (LCIE).",
        "<b>Italy (EU)</b> - Centro Elettrotecnico Sperimentale Italiano (CESI).",
        "<b>Netherlands (EU)</b> - NV KEMA.",
        "<b>Great Britain (EU)</b> - Electrical Equipment Certification Service (EECS, formerly "
        "BASEEFA); Sira Certification Service (SCS).",
        "<b>Northern Ireland (EU)</b> - Industrial Science Centre (no initials are given).",
        "<b>Finland (EU)</b> - Technical Research Centre of Finland (VTT).",
        "<b>Norway (non-EU)</b> - Norges Elektriske Materiellkontroll (NEMKO).",
        "<b>Austria (EU)</b> - Bundesversuchs-und-Forschungsanstalt Arsenal (BVFA); TUV Austria.",
        "<b>Sweden (EU)</b> - Swedish National Testing and Research Institute (SP).",
    ]))
    b.append(p("It will be noted that in the case of the Industrial Science Centre in Northern "
               "Ireland no set of initials is given after the title. This is significant as the "
               "initials are those which appear on the certificates issued by the approved "
               "bodies. The reason for this lies in the slightly unusual nature of the "
               "relationship between Great Britain and Northern Ireland in that British "
               "legislation in this area does not apply to Northern Ireland, which results in the "
               "need for an approved body in Northern Ireland even though that organisation has no "
               "plans to issue any certificates and it certainly does not at present."))
    b.append(p("It might also be thought odd that the Safety in Mines Research Establishment or "
               "its successor, the Health and Safety Laboratory, is not present despite its long "
               "history of expertise in this area. This is because it was part of the British "
               "Civil Service (Government Service). The current Government associated body is the "
               "Electrical Equipment Certification Service which comes from the same roots and "
               "has access to the same expertise as did the Safety in Mines Research Establishment."))
    b.append(p("Some of the listed bodies have logos and these are shown in Fig. 1.4 to assist in "
               "their recognition."))
    b.append(fig(4, FB.fig_f104()))
    b.append(p("The certificates issued by all of these approved bodies have exactly the same "
               "format which assists in their usage whatever their source. They identify the "
               "equipment certified, together with its certification code (described later) and "
               "the manufacturer. An example of a typical certificate is given in Fig. 1.5."))
    b.append(fig(5, FB.fig_f105()))
    b.append(p("What should be noted is the limit of the certificate. It only specifies the "
               "equipment as being in accordance with the detailed construction requirements in "
               "the specified Standard and does not address installation which will vary "
               "depending upon the country of installation. Therefore care needs to be taken in "
               "careful consideration of the way in which equipment is installed, so as to ensure "
               "that the safety elements included in its construction are not negated by its "
               "method of installation."))
    b.append(p("The listed approved bodies meet regularly in a working group titled Heads of "
               "Test Houses Liaison Committee (HOTL) which was set up by the Commission of the "
               "EU. The object of this group is to ensure that all approved bodies use the "
               "Standards in the same way and present their certificates in the same way. It is "
               "not intended to be a body for the deciding of the meaning of unclear parts of the "
               "Standards although it, of necessity, becomes involved in such activity."))
    b.append(p("The clarification and interpretation of Standards is for the Standards' writing "
               "bodies (CENELEC in this case) but such bodies are by their nature cumbersome and "
               "thus queries on Standards can take considerable time to resolve. Because of the "
               "commercial nature of the use of certification HOTL performs a valuable role in "
               "providing speedy temporary clarification pending the decision of the Standards "
               "writing body and to this end HOTL members notify that body of all temporary "
               "clarifications which they have adopted."))
    b.append(p("The Standards writing body may then endorse or override them as it wishes, in its "
               "own good time. This does not normally represent any problem for the holder of a "
               "certificate based on an HOTL clarification later overturned by the Standards "
               "writing body because, unless a prima-facie danger is identified in relation to "
               "the HOTL decision, the certificate would be allowed to stand, although members of "
               "HOTL would automatically adopt the official clarification as soon as it was "
               "available for future certification."))
    b.append(p("Many of the approved bodies issue certificates to equipment complying with their "
               "own or national Standards in addition to equipment complying with the European "
               "Standards referred to in the Directive. These are not covered by the Directive "
               "and their acceptance is a matter for the individual user. This is likewise true "
               "of certificates issued by bodies not approved by the EU even though they may be "
               "national bodies and likewise acceptance is a matter for the individual."))
    b.append(p("Where these latter certificates are in relation to the European Standards then it "
               "is only the expertise of the non-approved certification body which must be "
               "considered but in other cases (e.g. Factory Mutual Research Corporation and "
               "Underwriters Laboratories in the USA) the Standards to which the equipment is "
               "certified (or listed which is what the activity is called in the USA) differ "
               "significantly, and the effect of this must also be considered."))

    # ---- 1.7
    b.append(h3("Certificate and labelling information", "Certificate and labelling information"))
    b.append(p("There is no real short cut to identification of suitable equipment as the "
               "schedules issued with certificates of conformity and inspection certificates "
               "contain information which is necessary to the user. These should always be made "
               "available to the purchasers of certified equipment and there is a legal obligation "
               "upon suppliers to do this insofar as safety is dependent upon such information. "
               "There is, however, a standard coding which appears on both certificate and label "
               "usually and this is as follows."))
    b.append(p("<b>Certifying body reference.</b> This appears usually as a set of initials and "
               "these are those shown in brackets in Section 1.5 of this chapter (e.g. PTB, LCIE, "
               "EECS or SCS)."))
    b.append(p("<b>Certificate number.</b> This appears as follows:"))
    b.append(p("<b>Ex 96 D 2 123 (X)</b>"))
    b.append(p("The various parts of this Code have the following meanings:"))
    b.append(ul([
        "Ex - explosion protected equipment.",
        "96 - the last two digits of the year of issue.",
        "D - amendment status of the Standard used for certification.",
        "2 - principal method of protection: 1 = flameproof or pressurized (see Chapters 10 and "
        "11); 2 = intrinsic safety (see Chapter 13); 3 = increased safety (see Chapter 12); "
        "4 = type N (n) apparatus (see Chapter 14); 5 = special protection (apparatus which does "
        "not wholly comply with one of the Standards but is considered as suitable); 6 = battery "
        "operated vehicles (usually using more than one type of protection); 7 = oil immersed or "
        "powder filled (see Chapter 9).",
        "123 - serial number of the certificate within the year.",
        "X - indicates that there are special (unusual) installation conditions associated with "
        "the equipment and these will be specified on the certificate. If U appears instead of X "
        "or no suffix, it means that the equipment is considered to be a component and cannot be "
        "used unless incorporated in other equipment and further certified.",
    ]))
    b.append(p("<b>Protection coding.</b> This normally appears in the following form:"))
    b.append(p("<b>EEx d IIC T4</b>"))
    b.append(p("The meaning of these symbols is as follows:"))
    b.append(ul([
        "E - indicates that the equipment complies with a European Standard. The symbol will not "
        "be present if such is not the case.",
        "Ex - indicates explosion protected equipment.",
        "d - indicates the type of protection used: o = oil immersion (see Chapter 9); p = "
        "pressurization (see Chapter 11); q = powder filling (see Chapter 9); d = flameproof "
        "enclosure (see Chapter 10); e = increased safety (see Chapter 12); i = intrinsic safety "
        "(see Chapter 13, usually with a further suffix such as ia or ib); m = encapsulation (see "
        "Chapter 9); n = type n equipment (see Chapter 14), sometimes appearing as N to indicate a "
        "UK national Standard rather than a European Standard.",
        "IIC - indicates the explosive atmosphere in which the apparatus was tested for spark "
        "ignition: IIA - equipment is tested in an ideal mixture of propane and air; IIB - "
        "equipment is tested in an ideal mixture of ethylene and air; IIC - equipment is tested in "
        "an ideal mixture of hydrogen and air. Where the equipment is to a type of protection "
        "where sparking is prevented the letter will be omitted and only II will appear as "
        "sub-grouping is not necessary.",
        "T4 - indicates the maximum temperature achieved by any ignition capable part of the "
        "equipment and indicates that no part of the equipment will exceed T1 450 °C, T2 300 °C, "
        "T3 200 °C, T4 135 °C, T5 100 °C or T6 85 °C.",
    ]))
    b.append(p("An ambient temperature of 40 °C is assumed unless otherwise stated on the label "
               "and certificate."))
    b.append(p("Historically, there have been other methods of coding in Europe and remain "
               "different methods in the USA. These are shown in Tables 1.1 and 1.2. It must "
               "however be noted that because of slightly differing information forming the "
               "basis for these that the relationship between the systems is only approximate."))
    b.append(table(_T11_HEADER_EN, _T11_ROWS_EN,
                   caption="Table 1.1. Relationship of grouping and classification systems."))
    b.append(p("<small>" + _T11_FN_EN + "</small>"))
    b.append(p("The temperature classification systems are related as shown in Table 1.2. Again, "
               "the relationship is only approximate."))
    b.append(table(_T12_HEADER_EN, _T12_ROWS_EN,
                   caption="Table 1.2. Relationship of temperature classification systems."))
    b.append(p("<small>" + _T12_FN_EN + "</small>"))

    # ---- 1.8
    b.append(h3("The future of certification", "The future of certification"))
    b.append(p("As has been stated, the situation in regard to certification is significantly "
               "affected by the 1990 Directive which came into force early in 1996, Directive "
               "94/9/EC. While this will initially rely on European Standards referred to in the "
               "European Journal it is certain that the breadth of the essential requirements "
               "contained within the Directive will ultimately be used."))
    b.append(p("As these essential requirements are couched in much more general terms than the "
               "Standards, then the approved bodies will have to revert to the expert "
               "interpretation of more general requirements much as they did before the advent of "
               "the more detailed Standards. The level of expertise of the certification bodies "
               "will once again, therefore, become of paramount importance."))
    b.append(p("To this end the HOTL grouping will assume a much greater significance and it is "
               "unlikely that it will contain sufficient expertise without introducing "
               "industrial expertise into it. How this can be done without making it as "
               "cumbersome as a Standards-making body will no doubt become a matter for "
               "considerable debate in the not too distant future."))
    b.append(p("The inclusion of non-electrical equipment for which the level of detailed "
               "standardization in this area is much lower will mean that the problem of "
               "certification to the requirements contained in the new Directive will be apparent "
               "much sooner. Not only will the currently approved bodies not have any detailed "
               "Standards but they will probably have only limited expertise in the non-electrical "
               "areas covered. As a result of this it is likely that a new set of approved bodies "
               "will appear separately from those in the electrical sphere."))
    b.append(p("Another inclusion in this new Directive is the requirement for a manufacturer or "
               "supplier to have a quality management system in most cases and to have that also "
               "certified to a set of requirements similar to BS/EN/ISO 9002 (although the "
               "requirements are again enshrined in the Directive). This will give more confidence "
               "to the user that purchases will accurately reflect the certification but, as the "
               "quality management requirements are again extremely subjective, it will cause "
               "considerable interpretive problems and is a further need for an expanded HOTL."))
    b.append(p("The route to certification under the new Directive is given in Fig. 1.6. When the "
               "manufacturer has obtained a type certificate for a product, using the system in "
               "Fig. 1.6(a) in accordance with the appropriate EN Standard or the essential "
               "requirements of the Directive, the steps illustrated by Fig. 1.6(b) are followed "
               "in respect of category 1 and category 2 equipment."))
    b.append(fig(6, FB.fig_f106()))
    b.append(p("For category 1 equipment (that intended for Zone 0) a notified body certifies the "
               "production quality system to BS/EN/ISO 9002 and monitors the system and product; "
               "alternatively the manufacturer operates a quality system of own responsibility "
               "and the notified body examines and tests all equipment."))
    b.append(p("For category 2 equipment (that intended for Zone 1) a notified body certifies the "
               "quality system to BS/EN/ISO 9003 and monitors it; alternatively the manufacturer "
               "operates a quality system of own responsibility and the notified body examines "
               "all equipment produced."))
    b.append(p("For category 3 equipment (that intended for Zone 2) no certification by an "
               "approved (notified) body is necessary. The manufacturer confirms compliance by "
               "declaration and application of the CE mark."))

    b.append(note("<b>About this translation.</b> This is an unofficial study translation. All "
                  "eight printed sections (1.1-1.8), the two tables with their notes, the six "
                  "redrawn vector figures and the sixteen numbered references are retained from "
                  "the source."))
    b.append(refs(_REFS_EN))
    return "".join(b)
