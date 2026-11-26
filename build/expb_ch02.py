# -*- coding: utf-8 -*-
"""Unit 2 — Classes, Groups and Temperature Classes / Class, nhóm vật liệu và cấp nhiệt độ.

EN/VI bilingual reader of R. STAHL, *Basics of Explosion Protection:
Understanding Global Explosion Protection*, printed A3–A4 (PDF pp. 4–5).
Reproduces all prose, three printed tables (gas groups, Class II dust
groups, full T1–T6 temperature table) and the vector Fire Triangle
redrawn in `expbfig02.py`.
"""
from expb_common import fig, h2, h3, lead, note, p, table, ul

import expbfig02 as F

PAGES_SRC = 2
BYLINE = "R. STAHL · Basics of Explosion Protection (Innovative Explosion Protection)"
TITLE_EN = "Classes, Groups and Temperature Classes"
TITLE_VI = "Class, nhóm vật liệu và cấp nhiệt độ"


def note_terms(lang):
    if lang == "vi":
        return ("<b>Thuật ngữ chương 2.</b> nhóm khí (gas groups) · Class/Division Gas Groups "
                "· Zone Gas Groups · nhóm A / B / C / D · II C / II B / II A · “IIB + hydrogen” "
                "· vị trí Class II · bụi dễ cháy hoặc dẫn điện · nhóm E / F / G · bụi kim loại "
                "dạng bột · bụi cháy · bụi nông nghiệp · nhiệt độ bắt lửa / nhiệt độ tự bắt "
                "lửa (ATI) · hiệu ứng chăn nhiệt · Zone 20 / 21 / 22 · vị trí Class III · sợi "
                "và mảnh bay dễ bắt lửa · cháy nhanh (flash fire) · cấp nhiệt độ / temperature "
                "class · T code · T1 đến T6 · T2A–T2D · T3A–T3C · 450°C/842°F đến 85°C/185°F "
                "· +40°C (+104°F) · –20°C đến +40°C · nhiệt độ môi trường · tam giác lửa "
                "(Fire Triangle) · LEL / UEL · giới hạn cháy dưới / trên · loại bảo vệ "
                "chống cháy “d” (flameproof) · explosionproof · Div. 1 / Zone 1 · lớp vỏ "
                "bọc · khe hở mối nối · hệ số an toàn")
    return ("<b>Key terms.</b> gas groups · Class/Division Gas Groups · Zone Gas Groups · "
            "groups A / B / C / D · II C / II B / II A · “IIB + hydrogen” · Class II "
            "locations · combustible or electrically conductive dusts · groups E / F / G · "
            "powdered metals · carbonaceous dusts · agricultural dusts · ignition temperature "
            "/ auto-ignition temperature (ATI) · thermal blanketing effect · Zone 20 / 21 / 22 "
            "· Class III locations · easily ignitable fibers or flyings · flash fire · "
            "temperature class · T code · T1 to T6 · T2A–T2D · T3A–T3C · 450°C/842°F to "
            "85°C/185°F · +40°C (+104°F) · –20°C to +40°C · ambient temperature · Fire "
            "Triangle · LEL / UEL · Lower / Upper Explosive Limit · flameproof type of "
            "protection “d” · explosionproof · Div. 1 / Zone 1 · enclosure · joints · "
            "safety factors")


_GAS_HEADER_VI = ["Khí điển hình", "Class/Division Gas Groups", "Zone Gas Groups"]
_GAS_ROWS_VI = [
    ["Acetylene (axetilen)", "A", ""],
    ["Hydrogen (hydro)", "B", "II C"],
    ["Ethylene (etilen)", "C", "II B"],
    ["Propane (propan)", "D", "II A"],
]
_GAS_HEADER_EN = ["Typical Gas", "Class/Division Gas Groups", "Zone Gas Groups"]
_GAS_ROWS_EN = [
    ["Acetylene", "A", ""],
    ["Hydrogen", "B", "II C"],
    ["Ethylene", "C", "II B"],
    ["Propane", "D", "II A"],
]
_GAS_FN_VI = "(Hoa Kỳ đã thêm nhóm “IIB + hydrogen” để giải quyết một số hạn chế về cấu trúc.)"
_GAS_FN_EN = '(The US has added a "IIB + hydrogen" group to address certain construction limitations.)'

_DUST_HEADER_VI = ["Nhóm", "Loại vật liệu", "Ví dụ"]
_DUST_ROWS_VI = [
    ["E", "Bụi dẫn điện", "Kim loại dạng bột như nhôm hoặc magie"],
    ["F", "Bụi chứa carbon", "Bột carbon, bụi than hoặc bụi coke"],
    ["G", "Bụi nông nghiệp", "Ngũ cốc, bột mì, đường, gia vị và một số polymer"],
]
_DUST_HEADER_EN = ["Groups", "Type of Material", "Examples"]
_DUST_ROWS_EN = [
    ["E", "Electrically Conductive Dusts", "Powdered Metals such as Aluminum or Magnesium"],
    ["F", "Carbonaceous Dusts", "Carbon Black, Coal Dust or Coke Dust"],
    ["G", "Agricultural Dusts", "Grain, Flour, Sugars, Spices and certain Polymers"],
]
_DUST_FN_VI = ("(IEC đã xây dựng Zone cho khí quyển chứa bụi dễ cháy, lại chia khu vực "
               "thành ba Zone 20, 21 và 22.)")
_DUST_FN_EN = ("(The IEC has developed Zones for atmospheres containing combustible dusts, "
               "which again separates areas in to three Zones 20, 21 and 22.)")

_TEMP_HEADER_VI = ["Mã nhiệt độ Bắc Mỹ", "Cấp nhiệt độ IEC/CENELEC/NEC 505",
                   "Nhiệt độ tối đa °C", "Nhiệt độ tối đa °F"]
_TEMP_HEADER_EN = ["North American Temperature Code",
                   "IEC/CENELEC/NEC 505 Temperature Classes",
                   "Maximum Temperature °C", "Maximum Temperature °F"]
_TEMP_ROWS = [
    ["T1", "T1", "450°C", "842°F"],
    ["T2", "T2", "300°C", "572°F"],
    ["T2A", "-", "280°C", "536°F"],
    ["T2B", "-", "260°C", "500°F"],
    ["T2C", "-", "230°C", "446°F"],
    ["T2D", "-", "215°C", "419°F"],
    ["T3", "T3", "200°C", "392°F"],
    ["T3A", "-", "180°C", "356°F"],
    ["T3B", "-", "165°C", "329°F"],
    ["T3C", "-", "160°C", "320°F"],
    ["T4", "T4", "135°C", "275°F"],
    ["T4A", "-", "120°C", "248°F"],
    ["T5", "T5", "100°C", "212°F"],
    ["T6", "T6", "85°C", "185°F"],
]


def body_vi():
    b = []
    b.append(h2(TITLE_VI, TITLE_EN))
    b.append(lead("Tìm hiểu bảo vệ chống nổ toàn cầu / Understanding Global Explosion "
                  "Protection — Class, nhóm vật liệu và cấp nhiệt độ."))

    b.append(h3("Nhóm khí", "Gas Groups"))
    b.append(p("Vị trí Class I được chia tiếp thành các nhóm dựa trên đặc tính nổ của vật liệu "
               "hiện diện. Bắc Mỹ truyền thống dùng bốn nhóm, trong khi IEC và CENELEC dùng "
               "ba nhóm."))
    b.append(p("Biểu đồ dưới đây so sánh hai hệ thống."))
    b.append(table(_GAS_HEADER_VI, _GAS_ROWS_VI,
                   caption="Bảng A4. So sánh nhóm khí: Class/Division và Zone."))
    b.append(p("<small>" + _GAS_FN_VI + "</small>"))

    b.append(h3("Vị trí Class II", "Class II Locations"))
    b.append(p("Vị trí Class II là nơi nguy hiểm do sự hiện diện của bụi dễ cháy hoặc bụi dẫn "
               "điện. Bụi phải hiện diện với số lượng đủ để có nguy cơ cháy hoặc nổ. Việc có "
               "một ít bụi dễ cháy hiện diện không có nghĩa là đã tồn tại vị trí nguy hiểm "
               "Class II."))
    b.append(p("Các chất Class II được chia thành ba nhóm vì những lý do tương tự như vật liệu "
               "Class I: thiết kế thiết bị và phân loại khu vực. Nhóm Class II dựa trên các "
               "đặc tính khác với nhóm Class I, do yêu cầu để một vụ nổ xảy ra và các phương "
               "pháp bảo vệ cần thiết cho thiết bị. Tại vị trí Class II, nhiệt độ bắt lửa, độ "
               "dẫn điện và hiệu ứng chăn nhiệt của bụi là yếu tố then chốt khi xử lý thiết bị "
               "sinh nhiệt, chẳng hạn đồ chiếu sáng và động cơ. Chính những yếu tố này quyết "
               "định nhóm Class II."))
    b.append(table(_DUST_HEADER_VI, _DUST_ROWS_VI,
                   caption="Bảng A5. Nhóm bụi Class II — loại vật liệu và ví dụ."))
    b.append(p("<small>" + _DUST_FN_VI + "</small>"))

    b.append(h3("Vị trí Zone 20, 21 và 22", "Zone 20, 21 and 22 Locations"))
    b.append(p("IEC gần đây đã đưa hệ ba Zone vào vị trí bụi dễ cháy. Các Zone này chưa được "
               "đưa vào quy chuẩn Bắc Mỹ. Định nghĩa như sau:"))
    b.append(ul([
        "<b>Zone 20</b> — khu vực mà bụi dễ cháy, dưới dạng đám mây, hiện diện liên tục hoặc "
        "thường xuyên trong vận hành bình thường với số lượng đủ để tạo thành hỗn hợp nổ.",
        "<b>Zone 21</b> — khu vực mà bụi dễ cháy, dưới dạng đám mây, có khả năng xuất hiện "
        "trong vận hành bình thường với số lượng đủ để tạo thành hỗn hợp nổ.",
        "<b>Zone 22</b> — khu vực mà đám mây bụi dễ cháy có thể xuất hiện không thường xuyên "
        "và chỉ tồn tại trong thời gian ngắn, hoặc nơi có thể có sự tích tụ hoặc lớp bụi trong "
        "điều kiện bất thường.",
    ]))

    b.append(h3("Vị trí Class III", "Class III Locations"))
    b.append(p("Vị trí Class III là nơi nguy hiểm do sự hiện diện của sợi hoặc mảnh bay dễ bắt "
               "lửa. Tuy nhiên, vật liệu không được lơ lửng trong không khí với số lượng đủ để "
               "tạo thành hỗn hợp có thể bắt lửa."))
    b.append(p("Sợi và mảnh bay dễ bắt lửa gây nguy cơ cháy nghiêm trọng, nhưng thường không "
               "phải nguy cơ nổ. Nguy hiểm lớn hơn với vật liệu Class III là nếu một lớp vật "
               "liệu hình thành khắp cơ sở, một nguồn đánh lửa sẽ gây cháy nhanh (flash fire) "
               "lan với tốc độ gần bằng tốc độ nổ."))

    b.append(h3("Cấp nhiệt độ", "Temperature Classes"))
    b.append(p("Nhiệt độ bắt lửa hay nhiệt độ tự bắt lửa (ATI) là nhiệt độ thấp nhất của bề mặt "
               "mà tại đó khí quyển nổ bắt lửa. Hơi và khí dễ cháy có thể được phân loại theo "
               "cấp nhiệt độ dựa trên nhiệt độ bắt lửa của chúng. Nhiệt độ tối đa của một thiết "
               "bị phải luôn thấp hơn nhiệt độ bắt lửa của hỗn hợp khí – không khí hoặc hỗn hợp "
               "hơi – không khí mà thiết bị được đặt trong đó. Thiết bị phải được ghi nhãn thể "
               "hiện nhiệt độ vận hành hoặc cấp nhiệt độ tham chiếu đến môi trường +40°C "
               "(+104°F). Cấp nhiệt độ (T code) được ghi trên nhãn của nhà sản xuất và dựa trên "
               "bảng dưới đây."))
    b.append(table(_TEMP_HEADER_VI, _TEMP_ROWS,
                   caption="Bảng A6. Mã nhiệt độ Bắc Mỹ / cấp nhiệt độ IEC, CENELEC, NEC 505 / "
                           "nhiệt độ tối đa (°C, °F)."))

    b.append(h3("Nhiệt độ môi trường", "Ambient Temperature"))
    b.append(p("Nhiệt độ môi trường là nhiệt độ của môi trường xung quanh nơi lắp đặt thiết bị, "
               "dù trong nhà hay ngoài trời. Dải nhiệt độ tiêu chuẩn để thiết kế thiết bị là "
               "–20°C đến +40°C; với dải này không yêu cầu ghi nhãn nhiệt độ môi trường trên "
               "sản phẩm. Đối với thiết bị điện được thiết kế để dùng trong dải nhiệt độ môi "
               "trường khác –20°C đến +40°C, dải nhiệt độ môi trường thực tế phải được ghi "
               "trên nhãn thiết bị."))
    b.append(p("Các dòng sản phẩm của R. STAHL, trong hầu hết trường hợp, vượt yêu cầu –20°C "
               "đến +40°C. Hãy tham khảo các trang catalog thích hợp để biết “Ambient "
               "Temperature Range” cụ thể của từng sản phẩm. Mọi dải nhiệt độ ngoài –20°C đến "
               "+40°C đều được ghi trên nhãn sản phẩm."))
    b.append(p("Các ứng dụng cần sản phẩm có dải nhiệt độ môi trường cực đoan nằm ngoài các dải "
               "tiêu chuẩn nêu dưới tiêu đề “Ambient Temperature Range” được quy định dưới "
               "tiêu đề “Special Ambient Temperature Range”. Chỉ những sản phẩm có thông tin "
               "bổ sung này trong catalog mới có thể được tùy chỉnh cho các ứng dụng nhiệt độ "
               "cực đoan. Vui lòng liên hệ nhà máy cho nhu cầu đặc biệt của bạn."))

    b.append(h3("Thiết kế và cấu tạo thiết bị", "Equipment Design and Construction"))
    b.append(p("Có nhiều phương pháp bảo vệ thiết bị điện, ngăn không cho một vụ nổ xảy ra khi "
               "dùng trong khí quyển khí dễ cháy, trong sự hiện diện của bụi dễ cháy hoặc sợi dễ "
               "bắt lửa."))
    b.append(p("Ba yếu tố là cần thiết để một vụ nổ xảy ra — nhiên liệu, oxy và nguồn nhiệt "
               "hoặc nguồn đánh lửa phải hiện diện. Nhiên liệu và oxy phải ở đúng tỷ lệ hỗn "
               "hợp. Quá ít nhiên liệu, hoặc hỗn hợp nghèo, hoặc quá nhiều nhiên liệu, hỗn hợp "
               "giàu, đều không thể bắt lửa. Các giới hạn nổ này được định nghĩa là “Lower "
               "Explosive Limit” (LEL) và “Upper Explosive Limit” (UEL)."))
    b.append(p("Mỗi phương pháp bảo vệ đều tác động đến Tam giác lửa theo một cách nào đó: hoặc "
               "chứa một vụ nổ bên trong, hoặc loại bỏ một hay nhiều thành phần cần thiết để "
               "vụ nổ xảy ra."))
    b.append(fig(1, F.fig_f201()))
    b.append(p("Các phương pháp bảo vệ phổ biến nhất ở Bắc Mỹ là thiết bị explosionproof cho vị "
               "trí Class I và thiết bị chống bắt lửa bụi (dust-ignition proof) cho vị trí Class "
               "II. R. STAHL sản xuất nhiều loại thiết bị dùng trong vị trí nguy hiểm theo "
               "nhiều phương pháp bảo vệ khác nhau."))

    b.append(h3("Loại bảo vệ chống cháy “d” hay thiết bị Explosionproof",
                "Flameproof Type of Protection “d” — or Explosionproof Equipment"))
    b.append(p("Dù thuật ngữ “explosionproof” của Bắc Mỹ và thuật ngữ “flameproof” của IEC là "
               "cùng một khái niệm, yêu cầu trong tiêu chuẩn sản phẩm lại khác nhau. "
               "Explosionproof là công nghệ Div. 1, có thể dùng trong môi trường Zone 1 được "
               "định nghĩa bởi NEC hoặc CEC. Flameproof là công nghệ Zone 1 và không thể dùng "
               "trong môi trường Div. 1."))
    b.append(p("Vì khí và hơi dễ cháy dự kiến hiện diện bên trong lớp vỏ bọc, thiết bị phải có "
               "khả năng chịu được một vụ nổ do tiếp điểm đánh lửa của các bộ phận, nhiệt độ "
               "cao hoặc lỗi điện. Lớp vỏ được thiết kế sao cho khí nóng sinh ra trong vụ nổ "
               "bên trong được làm nguội xuống dưới nhiệt độ bắt lửa của khí quyển dễ cháy xung "
               "quanh khi thoát ra qua các khe hở của thiết bị."))
    b.append(p("Ngoài ra, bề mặt bên ngoài của lớp vỏ không được nóng đến mức bắt lửa khí quyển "
               "xung quanh do năng lượng nhiệt bên trong thiết bị. Năng lượng nhiệt này có thể "
               "là kết quả của vận hành bình thường của thiết bị sinh nhiệt, hoặc của một hồ "
               "quang điện tới lớp vỏ từ lỗi tiếp địa phát hồ quang. Các hệ số an toàn được áp "
               "dụng cho mọi thử nghiệm của loại vỏ này để đảm bảo thiết bị không bị vỡ do một "
               "vụ nổ bên trong."))
    b.append(note("<b>Đặc điểm của nguyên bản.</b> Chương gồm hai trang in (A3, A4; PDF trang "
                  "4–5), có ba bảng và một tam giác lửa được vẽ lại dạng vector. Bảng đầu so "
                  "sánh nhóm khí A/B/C/D với II C/II B/II A kèm ghi chú “IIB + hydrogen”; bảng "
                  "thứ hai liệt kê nhóm bụi E/F/G với ví dụ; bảng cuối là bảng đầy đủ T1–T6, "
                  "gồm T2A–T2D và T3A–T3C cùng giá trị °C/°F. Mọi số liệu, mã và chú thích gốc "
                  "được giữ nguyên, gồm +40°C (+104°F), –20°C đến +40°C, 450°C/842°F đến "
                  "85°C/185°F, LEL/UEL và sự phân biệt flameproof “d” (Zone 1) với "
                  "explosionproof (Div. 1)."))
    b.append(p("<i>Đây là bản dịch không chính thức, dùng cho mục đích học tập. Nội dung gốc "
               "© R. STAHL.</i>"))
    return "".join(b)


def body_en():
    b = []
    b.append(h2(TITLE_EN, TITLE_EN))
    b.append(lead("Understanding Global Explosion Protection — Classes, Groups and "
                  "Temperature Classes."))

    b.append(h3("Gas Groups", "Gas Groups"))
    b.append(p("Class I locations are further divided into Groups based on the explosive "
               "properties of the materials present. North America has traditionally used "
               "four groups while the IEC and CENELEC use three."))
    b.append(p("The chart below compares the two systems."))
    b.append(table(_GAS_HEADER_EN, _GAS_ROWS_EN,
                   caption="Table A4. Typical Gas / Class-Division Gas Groups / Zone Gas Groups."))
    b.append(p("<small>" + _GAS_FN_EN + "</small>"))

    b.append(h3("Class II Locations", "Class II Locations"))
    b.append(p("Class II locations are those which are hazardous due to the presence of "
               "combustible or electrically conductive dusts. The dust must be present in "
               "sufficient quantities for a fire or explosion hazard to exist. The fact that "
               "there is some combustible dust present does not mean a Class II hazardous "
               "location exists."))
    b.append(p("Class II substances are divided into three groups for similar reasons to those "
               "of Class I materials: equipment design and area classification. Class II "
               "groups are based on different characteristics than those of Class I, given "
               "the requirements for an explosion to occur and the protection methods required "
               "for equipment. In Class II locations the ignition temperature, the electrical "
               "conductivity, and the thermal blanketing effect of the dust are critical when "
               "dealing with heat-producing equipment, such as lighting fixtures and motors. "
               "It is these factors which are the deciding factors in determining the Class II "
               "groups."))
    b.append(table(_DUST_HEADER_EN, _DUST_ROWS_EN,
                   caption="Table A5. Class II Groups — type of material and examples."))
    b.append(p("<small>" + _DUST_FN_EN + "</small>"))

    b.append(h3("Zone 20, 21 and 22 Locations", "Zone 20, 21 and 22 Locations"))
    b.append(p("The IEC has recently introduced the three-Zone system for combustible dust "
               "locations. These have not been included in North American codes yet. The "
               "definitions are as follows:"))
    b.append(ul([
        "<b>Zone 20</b> - an area in which a combustible dust, as a cloud, is present "
        "continuously or frequently during normal operations in sufficient quantities to "
        "produce an explosive mixture.",
        "<b>Zone 21</b> - an area in which a combustible dust, as a cloud, is likely to occur "
        "during normal operations in sufficient quantities to produce an explosive mixture.",
        "<b>Zone 22</b> - an area in which combustible dust clouds may occur infrequently and "
        "persist for only short periods of time or in which accumulations or layers may be "
        "present under abnormal conditions.",
    ]))

    b.append(h3("Class III Locations", "Class III Locations"))
    b.append(p("Class III locations are those which are hazardous due to the presence of "
               "easily ignitable fibers or flyings. However, the material is not suspended in "
               "the air in quantities sufficient to produce ignitable mixtures."))
    b.append(p("Easily ignitable fibers and flyings present a serious fire risk, not normally "
               "an explosion hazard. The greater danger with Class III materials is that if a "
               "layer forms throughout a facility, an ignition will cause a flash fire which "
               "moves at near explosive speeds."))

    b.append(h3("Temperature Classes", "Temperature Classes"))
    b.append(p("Ignition temperature or auto-ignition temperature (ATI) is the minimum "
               "temperature of a surface at which an explosive atmosphere ignites. Flammable "
               "vapors and gases can be classified into temperature classes according to their "
               "ignition temperature. The maximum temperature of a piece of equipment must "
               "always be lower than the ignition temperature of the gas - air mixture or "
               "vapor - air mixture in which it is placed. Equipment shall be marked to show "
               "the operating temperature or temperature class referenced to a +40°C (+104°F) "
               "ambient. The temperature class (T code) is indicated on the manufacturers "
               "nameplate and is based on the table below."))
    b.append(table(_TEMP_HEADER_EN, _TEMP_ROWS,
                   caption="Table A6. North American Temperature Code / IEC, CENELEC and NEC "
                           "505 Temperature Classes / maximum temperature (°C, °F)."))

    b.append(h3("Ambient Temperature", "Ambient Temperature"))
    b.append(p("The ambient temperature is the surrounding temperature of the environment in "
               "which a piece of equipment is installed, whether it is indoors or outdoors. "
               "The standard temperature range for equipment design is –20°C to +40°C; for "
               "this range no ambient temperature marking is required on the product. "
               "Electrical equipment that is designed for use in a range of ambient "
               "temperature other than –20°C to +40°C the actual ambient temperature range "
               "shall be marked on the equipment nameplate."))
    b.append(p("The R. STAHL product lines, in most cases, exceed the –20°C to +40°C "
               "requirement. Refer to the appropriate catalog pages for the product-specific "
               "“Ambient Temperature Range”. Any ranges outside –20°C to +40°C are marked on "
               "the product nameplate."))
    b.append(p("Applications requiring product with extreme ambient temperature ranges outside "
               "those standard ranges stated under the heading “Ambient Temperature Range” are "
               "specified under the heading of “Special Ambient Temperature Range”. Only "
               "products with this additional catalog information can be customized for "
               "extreme temperature applications. Please consult factory for your special "
               "needs."))

    b.append(h3("Equipment Design and Construction", "Equipment Design and Construction"))
    b.append(p("There are a number of methods of protecting electrical equipment, which "
               "prevent an explosion when used in a flammable gas atmosphere, in the presence "
               "of combustible dust or easily ignited fibers."))
    b.append(p("Three elements are required for an explosion to occur - fuel, oxygen and a heat "
               "or ignition source must be present. The fuel and oxygen must be in the correct "
               "mixture. Too little fuel, or a lean mixture, or too much fuel, a rich mixture "
               "cannot ignite. These explosive limits are defined as the “Lower Explosive "
               "Limit” (LEL) and the “Upper Explosive Limit” (UEL)."))
    b.append(p("Each method of protection addresses the Fire Triangle in some manner. Either "
               "by containing an internal explosion or eliminating one or more of the "
               "components necessary for an explosion to occur."))
    b.append(fig(1, F.fig_f201()))
    b.append(p("The most common North American methods of protection are explosionproof "
               "equipment for Class I locations, and dust-ignition proof equipment for Class II "
               "locations. R. STAHL produces a wide range of equipment for use in hazardous "
               "locations using various methods of protection."))

    b.append(h3("Flameproof Type of Protection “d” — or Explosionproof Equipment",
                "Flameproof Type of Protection “d” — or Explosionproof Equipment"))
    b.append(p("Although the North American term “explosionproof” and IEC term “flameproof” "
               "are identical concepts, the requirements in the product standards are "
               "different. Explosionproof is a Div. 1 technology which can be used in a NEC or "
               "CEC defined Zone 1 environment. Flameproof is a Zone 1 technology and can not "
               "be used in a Div. 1 environment."))
    b.append(p("Since flammable gases and vapors are expected inside an enclosure, the "
               "equipment must be capable of withstanding an explosion caused by sparking "
               "contacts of devices, high temperatures, or an electrical fault. The enclosure "
               "is designed so that hot gases generated during an internal explosion are "
               "cooled below the ignition temperature of the surrounding flammable atmosphere "
               "as they escape through the joints of the unit."))
    b.append(p("In addition, the external surfaces of the enclosure must not become hot enough "
               "to ignite the surrounding atmosphere due to heat energy within the unit. This "
               "heat energy may be the result of normal operation of heat-producing equipment, "
               "or the result of an electrical arc to the enclosure from an arcing ground "
               "fault. Safety factors are applied to all testing of this type of enclosure to "
               "ensure the unit will not rupture as a result of an internal explosion."))
    b.append(note("<b>Source quirks.</b> The chapter spans two printed pages (A3, A4; PDF pp. "
                  "4–5), with three tables and one vector Fire Triangle. The first table "
                  "compares groups A/B/C/D with II C/II B/II A and includes the “IIB + "
                  "hydrogen” note; the second lists Class II groups E/F/G with examples; the "
                  "third is the full T1–T6 table with T2A–T2D and T3A–T3C and their °C/°F "
                  "values. All printed numbers, codes and footnotes are retained, including "
                  "+40°C (+104°F), –20°C to +40°C, 450°C/842°F to 85°C/185°F, LEL/UEL and "
                  "the distinction between flameproof “d” (Zone 1) and explosionproof "
                  "(Div. 1)."))
    b.append(p("<i>This is an unofficial translation for study purposes. Original content "
               "© R. STAHL.</i>"))
    return "".join(b)
