# -*- coding: utf-8 -*-
"""Unit 1 — Hazardous Locations and the Two Systems / Vị trí nguy hiểm và hai hệ thống phân loại.

EN/VI bilingual reader of R. STAHL, *Basics of Explosion Protection:
Understanding Global Explosion Protection*, printed A–A2 (PDF pp. 1–3).
Reproduces all prose, three printed tables (with footnotes) and the two
vector risk charts redrawn in `expbfig01.py`.
"""
from expb_common import fig, h2, h3, lead, note, p, table

import expbfig01 as F

PAGES_SRC = 3
BYLINE = "R. STAHL · Basics of Explosion Protection (Innovative Explosion Protection)"
TITLE_EN = "Hazardous Locations and the Two Systems"
TITLE_VI = "Vị trí nguy hiểm và hai hệ thống phân loại"


def note_terms(lang):
    if lang == "vi":
        return ("<b>Thuật ngữ chương 1.</b> vị trí nguy hiểm (hazardous location) · hệ Class "
                "và Division · hệ Zone · hệ Class-Zone · CENELEC · IEC · NEC® (National "
                "Electrical Code) · CEC® (Canadian Electrical Code) · Class I / II / III · "
                "Division 1 / Division 2 · Zone 0 / 1 / 2 / 20 / 21 / 22 · khí hoặc hơi dễ "
                "cháy · chất lỏng dễ cháy · bụi cháy được · sợi và mảnh bay dễ bắt lửa · "
                "hỗn hợp nổ · hỗn hợp có thể bắt lửa · tự nhiên / gián đoạn theo chu kỳ / "
                "điều kiện bất thường · tần suất xuất hiện · mức độ rủi ro · thời gian khí "
                "hiện diện · 1 giờ, 10 giờ và 1000 giờ mỗi năm · grade of release "
                "(cấp độ thoát khí) · continuous / primary / secondary / unclassified · "
                "API RP505 Tables 2 and 3 · 10% / 0,1% đến 10% / 0,01% đến 0,1% / dưới "
                "0,01% · ước tính bảo thủ 0,01 giờ mỗi năm")
    return ("<b>Key terms.</b> hazardous location · Class and Division System · Zone System "
            "· Class-Zone System · CENELEC · IEC · NEC® (National Electrical Code) · CEC® "
            "(Canadian Electrical Code) · Class I / II / III · Division 1 / Division 2 · "
            "Zone 0 / 1 / 2 / 20 / 21 / 22 · flammable gases or vapors · flammable liquids "
            "· combustible dusts · easily ignitable fibers or flyings · explosive or "
            "ignitible mixtures · continuous / intermittent periodically / abnormal "
            "condition · frequency of occurrence · risk assessment · duration of time gas "
            "is present · 1, 10 and 1000 hours per year · grade of release · continuous / "
            "primary / secondary / unclassified · API RP505 Tables 2 and 3 · 10% / 0.1% to "
            "10% / 0.01% to 0.1% / less than 0.01% · conservative 0.01 hours per year")


_T1_HEADER_VI = ["Vật liệu nguy hiểm", "Hệ Class/Division", "Hệ Zone ➀"]
_T1_ROWS_VI = [
    ["Khí hoặc hơi ➀", "Class I, Division 1", "Zone 0<br>Zone 1"],
    ["", "Class I, Division 2", "Zone 2"],
    ["Bụi cháy được ➁", "Class II, Division 1", "Zone 20<br>Zone 21"],
    ["", "Class II, Division 2", "Zone 22"],
    ["Sợi hoặc mảnh bay", "Class III, Division 1", ""],
    ["", "Class III, Division 2", "No Equivalent"],
]
_T1_HEADER_EN = ["Hazardous Materials", "Class/Division System", "Zone System ➀"]
_T1_ROWS_EN = [
    ["Gasses or Vapors ➀", "Class I, Division 1", "Zone 0<br>Zone 1"],
    ["", "Class I, Division 2", "Zone 2"],
    ["Combustible Dusts ➁", "Class II, Division 1", "Zone 20<br>Zone 21"],
    ["", "Class II, Division 2", "Zone 22"],
    ["Fibers or Flyings", "Class III, Division 1", ""],
    ["", "Class III, Division 2", "No Equivalent"],
]
_T1_FN_VI = ("➀ Hoa Kỳ và Canada đã áp dụng Zone cho khí và hơi. "
             "➁ Zone cho bụi chưa được xây dựng ở Bắc Mỹ.")
_T1_FN_EN = ("➀ The United States and Canada have adopted Zones for Gasses and Vapors. "
             "➁ Zones for Dust are not yet developed for North America.")

_T2_HEADER_VI = ["Tần suất xuất hiện", "Hệ Division", "Hệ Zone"]
_T2_ROWS_VI = [
    ["Liên tục", "Class I, Division 1", "Zone 0"],
    ["", "", "Zone 1"],
    ["Gián đoạn, theo chu kỳ", "Class I, Division 2", "Zone 2"],
    ["Điều kiện bất thường", "", ""],
]
_T2_HEADER_EN = ["Frequency of Occurrence", "Division System", "Zone System"]
_T2_ROWS_EN = [
    ["Continuous", "Class I, Division 1", "Zone 0"],
    ["", "", "Zone 1"],
    ["Intermittent Periodically", "Class I, Division 2", "Zone 2"],
    ["Abnormal Condition", "", ""],
]

_T3_HEADER_VI = ["Cấp độ thoát khí", "Zone", "Hỗn hợp dễ cháy hiện diện"]
_T3_ROWS_VI = [
    ["Liên tục", "0", "1000 giờ mỗi năm trở lên (10%)"],
    ["Chính", "1", "Từ 10 đến 1000 giờ mỗi năm trở lên (0,1% đến 10%)"],
    ["Phụ", "2", "Dưới 10 giờ mỗi năm (0,01% đến 0,1%)"],
    ["Không phân loại", "-", "Dưới 1 giờ mỗi năm (dưới 0,01%)➀"],
]
_T3_HEADER_EN = ["Grade of Release", "Zone", "Flammable Mixture Present"]
_T3_ROWS_EN = [
    ["Continuous", "0", "1000 hours per year or more (10%)"],
    ["Primary", "1", "Between 10 and 1000 hours per year or more (0.1% to 10%)"],
    ["Secondary", "2", "Less than 10 hours per year (0.01% to 0.1%)"],
    ["Unclassified", "-", "Less than 1 hour per year (Less than 0.01%)➀"],
]
_T3_FN_VI = ("Đây là sự kết hợp của Tables 2 và 3 từ API RP505. "
             "➀ Mức 1 giờ mỗi năm dùng trong API RP505 bị một số chuyên gia trong ngành "
             "coi là cao. Ước tính bảo thủ của con số này nên là 0,01 giờ mỗi năm.")
_T3_FN_EN = ("This is a combination of Tables 2 and 3 from API RP505. "
             "➀ The 1-hour per year used in API RP505 is considered to be high by some "
             "industry experts. Conservative estimates of this figure should be "
             "0.01 hours per year.")


def body_vi():
    b = []
    b.append(h2(TITLE_VI, TITLE_EN))
    b.append(lead("Tìm hiểu bảo vệ chống nổ toàn cầu / Understanding Global Explosion "
                  "Protection — Hệ Class và Division · Hệ Class-Zone · Hệ Zone CENELEC · IEC."))

    b.append(h3("Vị trí nguy hiểm", "Hazardous Locations"))
    b.append(p("Vị trí nguy hiểm được định nghĩa là khuôn viên, tòa nhà hoặc một phần của "
               "chúng nơi có thể tồn tại nguy cơ cháy hoặc nổ do sự hiện diện của khí hoặc "
               "hơi dễ cháy, chất lỏng dễ cháy, bụi dễ cháy hoặc sợi và mảnh bay dễ bắt lửa."))
    b.append(p("Dù khí, hơi dễ cháy và bụi dễ cháy gần như tồn tại ở khắp nơi, may mắn là "
               "chúng chỉ hiện diện với số lượng rất nhỏ. Chỉ vì có khí hoặc hơi dễ cháy, "
               "hoặc bụi dễ cháy hiện diện thì chưa chắc đã là vị trí nguy hiểm. Số lượng "
               "hoặc nồng độ phải đủ để tạo ra nguy cơ nổ tiềm ẩn."))
    b.append(p("Các quy chuẩn điện đề cập đến những loại vị trí nguy hiểm này không đề cập "
               "đến vật liệu như chất nổ mạnh, chẳng hạn dynamite, đạn dược hoặc pháo hoa. "
               "Các quy tắc và quy định khác đề cập đến khu vực liên quan đến những vật "
               "liệu đó."))

    b.append(h3("Hiểu yêu cầu vị trí nguy hiểm “toàn cầu”",
                "Understanding “Global” Hazardous Location Requirements"))
    b.append(p("Sự phát triển của các quy chuẩn và tiêu chuẩn điện về vị trí nguy hiểm trên "
               "thế giới đã đi theo hai hướng riêng biệt. Ở Bắc Mỹ, hệ thống “Class, "
               "Division” đã được dùng trong nhiều thập kỷ làm cơ sở phân loại khu vực cho "
               "các vị trí nguy hiểm (được phân loại). Vì mức nguy hiểm và phương pháp bảo "
               "vệ thiết bị điện khỏi các mối nguy đó khác nhau đối với từng loại vật liệu, "
               "vị trí nguy hiểm được chia thành ba Class và hai Division. Class dựa trên "
               "loại mức nguy hiểm và đặc tính nổ của vật liệu, còn Division dựa trên tần "
               "suất xuất hiện hoặc mức độ rủi ro cháy nổ do vật liệu gây ra. Dù Hoa Kỳ và "
               "Canada có một số khác biệt về phương pháp đi dây được chấp nhận và tiêu "
               "chuẩn sản phẩm, hai hệ thống này rất giống nhau."))
    b.append(p("Ở các nơi khác trên thế giới, khu vực chứa khí quyển có khả năng nổ được xử "
               "lý bằng “Hệ Zone”. Zone chủ yếu dựa trên tiêu chuẩn của Ủy ban Kỹ thuật Điện "
               "Quốc tế (IEC) và Ủy ban Tiêu chuẩn hóa Điện kỹ thuật Châu Âu (CENELEC). Trong "
               "khi Bắc Mỹ xử lý nhiều loại khí quyển nguy hiểm khác nhau, Hệ Zone của Bắc "
               "Mỹ hiện chỉ đề cập đến khí và hơi dễ cháy, tương đương với vị trí Class I của "
               "Bắc Mỹ. Điểm khác biệt quan trọng nhất của hệ Zone là mức độ xác suất nguy "
               "hiểm được chia thành ba Zone thay vì hai Division."))
    b.append(p("Dù yêu cầu cụ thể có khác nhau, Hoa Kỳ và Canada đã đưa Hệ Zone vào vị trí "
               "Class I nguy hiểm trong các bản cập nhật quy chuẩn điện gần đây. Cả hai hệ "
               "thống đều đưa ra giải pháp hiệu quả cho thiết bị điện dùng trong vị trí "
               "nguy hiểm và đều có thành tích an toàn xuất sắc."))

    b.append(h3("Kiến thức cơ bản về vị trí nguy hiểm", "Hazardous Location Basics"))
    b.append(p("Ở Bắc Mỹ, vị trí nguy hiểm được tách thành ba “Class” hay loại dựa trên đặc "
               "tính nổ của vật liệu. Class hay loại vật liệu lại được tách tiếp thành "
               "“Division” hoặc “Zone” dựa trên mức độ rủi ro cháy hoặc nổ do vật liệu gây "
               "ra. Hệ Zone có ba mức nguy hiểm, trong khi Hệ Division có hai mức."))
    b.append(table(_T1_HEADER_VI, _T1_ROWS_VI,
                   caption="Bảng A1. Vật liệu nguy hiểm / Class-Division / Zone."))
    b.append(p("<small>" + _T1_FN_VI + "</small>"))

    b.append(h3("Vị trí Class I", "Class I, Locations"))
    b.append(p("Vị trí Class I là nơi có khí hoặc hơi dễ cháy hiện diện hoặc có thể hiện diện "
               "trong không khí với số lượng đủ để tạo thành hỗn hợp nổ hoặc hỗn hợp có thể "
               "bắt lửa. Thuật ngữ “khí hoặc hơi” phân biệt giữa vật liệu ở trạng thái khí "
               "trong điều kiện khí quyển bình thường, chẳng hạn hydro hoặc methane, và hơi "
               "bay ra từ chất lỏng trong điều kiện khí quyển bình thường, chẳng hạn xăng."))
    b.append(p("Việc chia vị trí Class I thành “Division” hoặc “Zone” dựa trên xác suất có "
               "khí quyển nổ hiện diện tại vị trí đó. Nếu rủi ro cực thấp, vị trí được coi là "
               "không nguy hiểm. Một ví dụ tốt về khu vực rủi ro thấp là một hộ gia đình dùng "
               "lò sưởi khí tự nhiên hoặc propane. Khí có thể — và trong những dịp cực hiếm "
               "có — rò rỉ vào nhà, gặp nguồn đánh lửa và gây nổ, thường với hậu quả tàn "
               "khốc. Tuy nhiên, vì rủi ro rất thấp nhờ các hệ thống an toàn tích hợp trong "
               "nguồn cấp khí và thiết bị sưởi, những khu vực này không phải là “vị trí được "
               "phân loại nguy hiểm”."))
    b.append(p("Các phiên bản gần đây của NEC® (National Electrical Code) và CEC® (Canadian "
               "Electrical Code) đã đưa định nghĩa quốc tế về “Zone” cho vị trí Class I vào. "
               "Hai quy chuẩn này tiếp tục đề cập đến hệ thống “Division”, dù phương pháp "
               "có phần khác nhau."))
    b.append(p("Tần suất xuất hiện quyết định mức độ nguy hiểm của một vị trí. Nói một cách "
               "đơn giản, vật liệu hiện diện càng lâu thì rủi ro càng lớn."))
    b.append(table(_T2_HEADER_VI, _T2_ROWS_VI,
                   caption="Bảng A2. Tần suất xuất hiện — so sánh hệ Division và hệ Zone."))
    b.append(p("Các biểu đồ dưới đây so sánh hệ Division và hệ Zone về đánh giá rủi ro."))
    b.append(fig(1, F.fig_f101()))
    b.append(fig(2, F.fig_f102()))
    b.append(p("Các điều kiện bất thường xuất hiện, tức các khu vực rủi ro thấp, trong hệ Zone "
               "và hệ Division về cơ bản là giống nhau. Tuy nhiên, ở những khu vực mà mối nguy "
               "dự kiến xuất hiện trong vận hành bình thường, hệ Zone xử lý riêng các khu vực "
               "rủi ro cao nhất, còn rủi ro tại phần còn lại được coi là thấp hơn. Hệ Division "
               "có xu hướng ít cụ thể hơn khi xét đến Division 1. Hệ Division đối xử như nhau "
               "với mọi khu vực mà mối nguy dự kiến xuất hiện trong vận hành bình thường."))
    b.append(p("Biểu đồ sau minh họa sự khác biệt giữa các Zone."))
    b.append(table(_T3_HEADER_VI, _T3_ROWS_VI,
                   caption="Bảng A3. Cấp độ thoát khí / Zone / Hỗn hợp dễ cháy hiện diện."))
    b.append(p("<small>" + _T3_FN_VI + "</small>"))
    b.append(note("<b>Đặc điểm của nguyên bản.</b> Chương gồm ba trang in (A, A1, A2; PDF "
                  "trang 1–3), có ba bảng và hai biểu đồ rủi ro được vẽ lại dạng vector. Các "
                  "bảng giữ nguyên mọi số liệu và chú thích gốc, gồm 1, 10 và 1000 giờ mỗi "
                  "năm, 10% / 0,1% đến 10% / 0,01% đến 0,1% / dưới 0,01%, và các ghi chú "
                  "từ Tables 2 và 3 của API RP505. Lỗi gõ “Unites States” trong nguyên bản "
                  "được giữ nguyên ở bản tiếng Anh. Ước tính bảo thủ 0,01 giờ mỗi năm được "
                  "giữ lại trong chú thích ➀."))
    b.append(p("<i>Đây là bản dịch không chính thức, dùng cho mục đích học tập. Nội dung gốc "
               "© R. STAHL.</i>"))
    return "".join(b)


def body_en():
    b = []
    b.append(h2(TITLE_EN, TITLE_EN))
    b.append(lead("Understanding Global Explosion Protection — Class and Division System · "
                  "Class-Zone System · CENELEC Zone System · IEC."))

    b.append(h3("Hazardous Locations", "Hazardous Locations"))
    b.append(p("Hazardous locations are defined as premises, buildings or parts thereof where "
               "fire or explosion hazards may exist due to the presence of flammable gases "
               "or vapors, flammable liquids, combustible dusts, or easily ignitable fibers "
               "or flyings."))
    b.append(p("Although, flammable gases, vapors and combustible dusts exist almost "
               "everywhere, fortunately, they are present only in minute quantities. Simply "
               "because flammable gasses or vapors, or combustible dusts are present, there "
               "is not necessarily a hazardous location. The quantities or concentrations "
               "must be sufficient to present a potential explosion hazard."))
    b.append(p("The electrical codes that deal with these types of hazardous locations areas "
               "do not deal with materials such as high explosives, such as dynamite, "
               "munitions, or fireworks. Other rules and regulations deal with areas "
               "involving these materials."))

    b.append(h3("Understanding “Global” Hazardous Location Requirements",
                "Understanding “Global” Hazardous Location Requirements"))
    b.append(p("The evolution of hazardous location electrical codes and standards throughout "
               "the world has taken two distinct paths. In North America, a “Class, Division” "
               "System has been used for decades as the basis for area classification of "
               "hazardous (classified) locations. Because the hazards and methods of "
               "protecting electrical equipment against these hazards differ for different "
               "materials, hazardous locations are divided into three Classes, and two "
               "Divisions. The Classes are based on the type of hazard and the explosive "
               "characteristics of the material with the Divisions being based on the "
               "occurrence or risk of fire or explosion that the material presents. While "
               "the United States and Canada have some differences in acceptable wiring "
               "methods and product standards, their systems are very similar."))
    b.append(p("In other parts of the world, areas containing potentially explosive "
               "atmospheres are dealt with using a “Zone System”. Zones are based "
               "predominantly on the International Electrotechnical Commission (IEC) and "
               "European Committee for Electrotechnical Standardization (CENELEC) standards. "
               "Whereas North America deals with multiple types of hazardous atmospheres, "
               "the North American Zone System presently addresses only flammable gases and "
               "vapors which is the equivalent to North America’s Class I locations. The most "
               "significant difference in the Zone system is that the level of hazard "
               "probability is divided into three Zones as oppose to two Divisions."))
    b.append(p("While specific requirements differ, the Unites States and Canada have "
               "incorporated the Zone System for Class I, hazardous locations into their "
               "recent electrical code updates. Both systems provide effective solutions "
               "for electrical equipment used in hazardous locations and both have "
               "excellent safety records."))

    b.append(h3("Hazardous Location Basics", "Hazardous Location Basics"))
    b.append(p("In North America, hazardous locations are separated into three “Classes” or "
               "types based on the explosive characteristics of the materials. The Classes or "
               "type of material is further separated into “Divisions” or “Zones” based on "
               "the risk of fire or explosion that the material poses. The Zone system has "
               "three levels of hazard versus the Division System’s two levels."))
    b.append(table(_T1_HEADER_EN, _T1_ROWS_EN,
                   caption="Table A1. Hazardous Materials / Class-Division / Zone."))
    b.append(p("<small>" + _T1_FN_EN + "</small>"))

    b.append(h3("Class I, Locations", "Class I, Locations"))
    b.append(p("Class I locations are those in which flammable \"gases or vapors\" are, or may "
               "be, present in the air in quantities sufficient to produce explosive or "
               "ignitible mixtures. The terms, \"gases or vapors\" differentiates between "
               "materials that are in a gaseous state under normal atmospheric conditions, "
               "such as hydrogen or methane, and a vapor that is flashed off from a liquid, "
               "under normal atmospheric conditions, such as gasoline."))
    b.append(p("The subdivision of Class I, locations into “Divisions” or “Zones” is based on "
               "the probability that an explosive gas atmosphere may be present in a "
               "location. If the risk is extremely low, the location is considered "
               "non-hazardous. A good example of a low risk area is a single family home with "
               "natural gas or propane furnace for heating. The gas could, and does on "
               "extremely rare occasions, leak into the home, encounter an ignition source "
               "and an explosion occurs, usually with devastating results. However, since "
               "the risk is so low, because of the safety systems built into the gas supply "
               "and heating equipment, these areas are not “hazardous classified locations”."))
    b.append(p("Recent editions of the NEC® (National Electrical Code) and CEC® (Canadian "
               "Electrical Code) have incorporated the international definitions for "
               "“Zones” for Class I, locations. The two codes continue to address the "
               "“Division” system although the methods are somewhat different."))
    b.append(p("The frequency of occurrence determines the level of hazard for a location. "
               "Simply stated, the longer the material is present, the greater the risk."))
    b.append(table(_T2_HEADER_EN, _T2_ROWS_EN,
                   caption="Table A2. Frequency of Occurrence — Division System vs. Zone System."))
    b.append(p("The charts below compare the Division and Zone systems in terms of risk "
               "assessment."))
    b.append(fig(1, F.fig_f101()))
    b.append(fig(2, F.fig_f102()))
    b.append(p("The abnormal conditions of occurrence, or lower risk areas, in the Zone and "
               "Division system are basically identical. However, in areas where a hazard is "
               "expected to occur in normal operation, the Zone system deals with highest "
               "risk areas separately, and risk associated with the remaining location is "
               "considered lower. The Division system tends to be less specific in its "
               "consideration of Division 1. The Division system treats all areas where a "
               "hazard is expected to occur in normal operation the same."))
    b.append(p("The following chart illustrates the differences between the various Zones."))
    b.append(table(_T3_HEADER_EN, _T3_ROWS_EN,
                   caption="Table A3. Grade of Release / Zone / Flammable Mixture Present."))
    b.append(p("<small>" + _T3_FN_EN + "</small>"))
    b.append(note("<b>Source quirks.</b> The chapter spans three printed pages (A, A1, A2; "
                  "PDF pp. 1–3), with three tables and two vector risk charts. The tables "
                  "retain every printed number and footnote, including 1, 10 and 1000 hours "
                  "per year; 10% / 0.1% to 10% / 0.01% to 0.1% / less than 0.01%; and the "
                  "note that this is a combination of Tables 2 and 3 from API RP505. The "
                  "printed typo “Unites States” is retained in this English text. The "
                  "conservative 0.01 hours per year estimate is retained in footnote ➀."))
    b.append(p("<i>This is an unofficial translation for study purposes. Original content "
               "© R. STAHL.</i>"))
    return "".join(b)
