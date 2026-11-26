# -*- coding: utf-8 -*-
"""Unit 6 - ATEX, CE Marking and the IECEx Scheme /
ATEX, dấu CE và chương trình IECEx (EN/VI bilingual).

Source: R. STAHL, *Basics of Explosion Protection*, printed A11-A13 (PDF pp.
12-14), plus the ATEX/CENELEC marking diagram from printed A10 (PDF p11):
ATEX Directive 94/9/EC and its 1 July 2003 deadline, CE marking, the Group I
and Group II equipment/category tables, the old-vs-new directive bullets,
products covered and exclusions, and the IECEx Scheme.  Three HTML tables and
one vector figure (6-1).
"""
from expb_common import p, lead, h2, h3, h4, ul, ol, note, table, fig, refs

import expbfig06 as F

PAGES_SRC = 3
BYLINE = "R. STAHL · Basics of Explosion Protection (Innovative Explosion Protection)"
TITLE_EN = "ATEX, CE Marking and the IECEx Scheme"
TITLE_VI = "ATEX, dấu CE và chương trình IECEx"

_MARK = "II 2G EEx de IIC T6"

_URL_ATEX = "www.europa.eu.int/comm/enterprise/atex/"
_URL_CE = "www.eurunion.org/legislat/standard/standard.htm"
_URL_IECEx = "www.IECEx.com"

_HDR_EN = ["Equipment Category", "Protection",
           "Comparison To Current IEC Classification"]
_HDR_VI = ["Danh mục thiết bị", "Bảo vệ",
           "So sánh với phân loại IEC hiện hành"]

_G1_EN = [
    ["M1", "2 levels of protection; or 2 independent faults", "Group I"],
    ["M2", "1 level of protection based on normal operation", "Group I"],
]
_G1_VI = [
    ["M1", "2 cấp bảo vệ; hoặc 2 lỗi độc lập", "Nhóm I"],
    ["M2", "1 cấp bảo vệ dựa trên vận hành bình thường", "Nhóm I"],
]

_G2_EN = [
    ["1G<br/>1D", "2 levels of protection; or 2 independent faults",
     "Group II, Zone 0 (gas)<br/>Zone 20 (dust)"],
    ["2G<br/>2D",
     "1 level of protection based on frequent disturbances; or equipment faults",
     "Group II, Zone 1 (gas)<br/>Zone 21 (dust)"],
    ["3G<br/>3D", "1 level of protection based on normal operation",
     "Group II, Zone 2 (gas)<br/>Zone 22 (dust)"],
]
_G2_VI = [
    ["1G<br/>1D", "2 cấp bảo vệ; hoặc 2 lỗi độc lập",
     "Nhóm II, Vùng 0 (khí)<br/>Vùng 20 (bụi)"],
    ["2G<br/>2D",
     "1 cấp bảo vệ dựa trên nhiễu loạn thường xuyên; hoặc lỗi thiết bị",
     "Nhóm II, Vùng 1 (khí)<br/>Vùng 21 (bụi)"],
    ["3G<br/>3D", "1 cấp bảo vệ dựa trên vận hành bình thường",
     "Nhóm II, Vùng 2 (khí)<br/>Vùng 22 (bụi)"],
]

_ZONE_HDR_EN = ["Category", "Zone", "Area description"]
_ZONE_HDR_VI = ["Danh mục", "Vùng", "Mô tả khu vực"]
_ZONE_EN = [
    ["1G", "Zone 0",
     "Areas where explosive gas atmosphere is continuously present or present for long periods of time"],
    ["2G", "Zone 1",
     "Areas where explosive gas atmosphere is likely to occur in normal operation or can be expected to be present frequently"],
    ["3G", "Zone 2",
     "Area where explosive gas atmosphere is not likely to occur and if it does, it will only exist for a short period of time"],
    ["1D", "Zone 20",
     "Area where combustible dust is continuously or frequently present"],
    ["2D", "Zone 21",
     "Area where combustible dust clouds are likely to occur during normal operation"],
    ["3D", "Zone 22",
     "Area where combustible dust clouds may occur infrequently during normal operation"],
]
_ZONE_VI = [
    ["1G", "Vùng 0",
     "Môi trường khí nổ hiện diện liên tục hoặc trong thời gian dài"],
    ["2G", "Vùng 1",
     "Môi trường khí nổ có khả năng xuất hiện trong vận hành bình thường hoặc dự kiến hiện diện thường xuyên"],
    ["3G", "Vùng 2",
     "Môi trường khí nổ ít có khả năng xuất hiện; nếu có thì chỉ tồn tại trong thời gian ngắn"],
    ["1D", "Vùng 20", "Bụi dễ cháy hiện diện liên tục hoặc thường xuyên"],
    ["2D", "Vùng 21",
     "Đám mây bụi dễ cháy có khả năng xuất hiện trong vận hành bình thường"],
    ["3D", "Vùng 22",
     "Đám mây bụi dễ cháy có thể xuất hiện không thường xuyên trong vận hành bình thường"],
]


def note_terms(lang):
    if lang == "vi":
        return ("<b>Thuật ngữ chương 6.</b> ATEX Directive 94/9/EC · Liên minh Châu Âu (EU) · "
                "quốc gia thành viên · bầu khí quyển nổ tiềm ẩn · thiết bị điện và không điện · "
                "hệ thống bảo vệ · bắt buộc từ 1 July 2003 · dấu CE (Conformité Européenne) · "
                "Equipment Group I / II · Category M1 / M2 · 1G / 1D, 2G / 2D, 3G / 3D · "
                "Zone 0 / 1 / 2 / 20 / 21 / 22 · firedamp (khí mêtan hầm lò) · "
                "II 2G EEx de IIC T6 · CENELEC EN 50… · Technical File · "
                "flame arrestor · suppression system · IECEx Scheme · "
                "one standard, one certificate and one mark · chứng nhận quốc gia · "
                "thời gian chuyển tiếp")
    return ("<b>Key terms.</b> ATEX Directive 94/9/EC · European Union (EU) · Member States · "
            "potentially explosive atmospheres · electrical and non-electrical equipment · "
            "protective systems · mandatory on July 1, 2003 · CE marking (Conformité "
            "Européenne) · Equipment Group I / II · Category M1 / M2 · 1G / 1D, 2G / 2D, "
            "3G / 3D · Zone 0 / 1 / 2 / 20 / 21 / 22 · firedamp · II 2G EEx de IIC T6 · "
            "CENELEC EN 50… · Technical File · flame arrestor · suppression system · "
            "IECEx Scheme · one standard, one certificate and one mark · national "
            "certification · transitional period")


def body_vi():
    b = []
    b.append(h2(TITLE_VI, TITLE_EN))
    b.append(lead("Chỉ thị ATEX 94/9/EC là một chỉ thị do Liên minh Châu Âu (EU) thông qua nhằm "
                  "thúc đẩy tự do thương mại trong EU bằng cách thống nhất các yêu cầu kỹ thuật "
                  "và pháp lý tại các quốc gia thành viên đối với sản phẩm dùng trong bầu khí "
                  "quyển nổ tiềm ẩn."))
    b.append(p("Chỉ thị này áp dụng cho thiết bị/linh kiện điện và không điện cùng các hệ thống "
               "bảo vệ. Chỉ thị ATEX trở thành bắt buộc từ ngày 1 July 2003 (July 1, 2003)."))
    b.append(p("Thiết bị đặt ngoài bầu khí quyển nổ tiềm ẩn cũng thuộc phạm vi của Chỉ thị ATEX "
               "trong các điều kiện sau:"))
    b.append(ul([
        "Thiết bị là một thiết bị an toàn, bộ điều khiển hoặc bộ điều tiết; và",
        "Thiết bị cần thiết cho hoạt động an toàn của thiết bị hoặc hệ thống bảo vệ liên quan "
        "đến nguy cơ nổ.",
    ]))
    b.append(p("Mọi thiết bị thuộc phạm vi điều chỉnh đều phải mang dấu CE Châu Âu làm bằng chứng "
               "tuân thủ Chỉ thị (dấu CE sẽ không xuất hiện trên linh kiện được định nghĩa trong "
               "Chỉ thị này). Chỉ thị ATEX định nghĩa cụ thể các thủ tục đánh giá thiết kế và sản "
               "xuất sản phẩm dựa trên Nhóm và Danh mục thiết bị. Tóm tắt như sau."))

    b.append(h3("Tổng quan Nhóm thiết bị I", "Equipment Group I Overview"))
    b.append(p("Thiết bị dùng trong các khu vực dưới lòng đất của hầm mỏ và trong những phần "
               "của công trình bề mặt của các hầm mỏ đó có nguy cơ bị đe dọa bởi firedamp và/hoặc "
               "bụi dễ cháy."))
    b.append(table(_HDR_VI, _G1_VI,
                   "Bảng 6-1 · Nhóm thiết bị I: so sánh mức bảo vệ với phân loại IEC hiện hành"))

    b.append(h3("Tổng quan Nhóm thiết bị II", "Equipment Group II Overview"))
    b.append(p("Thiết bị dùng ở những nơi không thuộc Nhóm thiết bị I nhưng có nguy cơ bị đe dọa "
               "bởi bầu khí quyển nổ."))
    b.append(table(_HDR_VI, _G2_VI,
                   "Bảng 6-2 · Nhóm thiết bị II: so sánh mức bảo vệ với phân loại IEC hiện hành"))

    b.append(h3("Ký hiệu ATEX", "ATEX Marking"))
    b.append(p("Việc gắn danh mục vào ký hiệu thiết bị giúp người dùng cuối lựa chọn thiết bị vì "
               "ký hiệu cho biết thiết bị có thể lắp an toàn ở Vùng nào. Đây là cải tiến lớn so với "
               "hệ thống ký hiệu cũ mang tính mật mã, chỉ liệt kê các khái niệm bảo vệ dùng trong "
               "thiết kế. Điều đó có nghĩa là người sử dụng thiết bị phải nắm rõ cả tám khái niệm "
               "bảo vệ được công nhận, lại còn phải biết khái niệm nào phù hợp với từng loại Vùng."))
    b.append(fig(1, F.fig_f601()))
    b.append(p("Ký hiệu ATEX/CENELEC điển hình " + _MARK + " được giải nghĩa trong Hình 6-1; "
               "bảng dưới đây liệt kê danh mục, vùng và mô tả khu vực tương ứng."))
    b.append(table(_ZONE_HDR_VI, _ZONE_VI,
                   "Bảng 6-3 · Danh mục ATEX và các vùng khí/bụi tương ứng"))

    b.append(h3("Khác biệt giữa chỉ thị cũ và mới",
                "Differences Between the Old and New Directives"))
    b.append(p("Những khác biệt chính là:"))
    b.append(ul([
        "Bao gồm cả thiết bị không điện.",
        "Bao gồm cả bầu khí quyển bụi.",
        "Yêu cầu đối với thiết bị liên quan an toàn (flame arrestor, hệ thống dập nổ, v.v.) và "
        "thiết bị dùng ở khu vực an toàn.",
        "Bổ sung yêu cầu về hệ thống chất lượng.",
        "Yêu cầu lập một ‘Technical File’.",
    ]))

    b.append(h3("Sản phẩm được bao phủ", "Products Covered"))
    b.append(p("Chỉ thị bao gồm thiết bị và các thiết bị an toàn hoặc điều khiển được lắp ngoài "
               "khu vực nổ tiềm ẩn nhưng có chức năng bảo vệ chống nổ. Nhiều loại sản phẩm nằm "
               "trong định nghĩa thiết bị, kể đến động cơ điện, máy nén, động cơ diesel, thiết bị "
               "chiếu sáng, thiết bị điều khiển và truyền thông cùng thiết bị giám sát và phát "
               "hiện. ‘Hệ thống bảo vệ’ cũng được bao gồm, gồm những thiết bị ngăn không cho vụ nổ "
               "đã phát sinh lan rộng hoặc gây thiệt hại. Chúng gồm flame arrestor, hệ thống "
               "dập (quenching), tấm xả áp và van ngắt tác động nhanh, kể đến một số loại."))

    b.append(h3("Sản phẩm bị loại trừ", "Product Exclusions"))
    b.append(p("Tuy nhiên, Chỉ thị loại trừ các loại sản phẩm sau:"))
    b.append(ul([
        "Thiết bị y tế.",
        "Sản phẩm dùng trong môi trường có chất nổ.",
        "Sản phẩm dùng trong hộ gia đình.",
        "Tàu đi biển và giàn khoan di động ngoài khơi.",
        "Thiết bị quân sự.",
        "Thiết bị bảo hộ cá nhân thuộc chỉ thị 89/686/EEC.",
        "Phương tiện vận tải bằng đường hàng không, đường bộ, đường sắt hoặc mạng đường "
        "thủy. Xe thiết kế để dùng trong bầu khí quyển nổ không bị loại trừ.",
    ]))
    b.append(p("Để biết thêm thông tin về ATEX, truy cập " + _URL_ATEX + "."))

    b.append(h3("Dấu CE / Conformité Européenne", "CE Marking / Conformité Européenne"))
    b.append(p("Dấu CE là dấu bắt buộc của Châu Âu đối với một số nhóm sản phẩm nhằm chứng tỏ sự "
               "phù hợp với các yêu cầu thiết yếu về sức khỏe và an toàn được nêu trong các Chỉ "
               "thị Châu Âu. Các chữ ‘CE’ là viết tắt của Conformité Européenne, tiếng Pháp nghĩa "
               "là sự phù hợp Châu Âu."))
    b.append(p("Dấu CE phải được gắn lên sản phẩm nếu sản phẩm thuộc phạm vi của các Chỉ thị gọi "
               "là ‘New Approach’. Nếu không có dấu CE, tức là không tuân thủ các quy định của Chỉ "
               "thị, sản phẩm không được đưa ra thị trường hoặc đưa vào sử dụng tại mười lăm "
               "quốc gia thành viên của Liên minh Châu Âu cùng Na Uy, Iceland và Liechtenstein. "
               "Tuy nhiên, nếu sản phẩm đáp ứng các quy định của Chỉ thị Châu Âu áp dụng và được "
               "gắn dấu CE, các quốc gia này không được cấm, hạn chế hay cản trở việc đưa sản phẩm "
               "ra thị trường hoặc đưa vào sử dụng. Như vậy, dấu CE có thể được xem là hộ chiếu "
               "thương mại của sản phẩm tại Châu Âu."))
    b.append(p("Để biết thêm thông tin về dấu CE, truy cập " + _URL_CE + "."))

    b.append(h3("Chương trình IECEx", "IECEx Scheme"))
    b.append(p("Mục tiêu của Chương trình IECEx là thúc đẩy thương mại toàn cầu về thiết bị điện "
               "dùng trong bầu khí quyển nổ bằng cách loại bỏ nhu cầu chứng nhận quốc gia nhiều "
               "lần."))
    b.append(p("Chương trình IECEx tạo điều kiện cho nhà sản xuất thiết bị Ex nhận được chứng thư "
               "phù hợp được chấp nhận ở cấp quốc gia tại mọi quốc gia tham gia. Chứng thư phù hợp "
               "có thể được cấp bởi bất kỳ cơ quan chứng nhận nào được Chương trình chấp nhận. "
               "Chứng thư xác nhận thiết kế thiết bị phù hợp với các Tiêu chuẩn IEC liên quan. Mục "
               "tiêu cuối cùng của Chương trình IECEx là được chấp nhận toàn cầu với one standard, "
               "one certificate and one mark."))
    b.append(p("Để Chương trình IECEx đạt được mục tiêu dài hạn, mọi Tiêu chuẩn quốc gia mà các "
               "quốc gia tham gia nộp đơn áp dụng sẽ cần giống hệt Tiêu chuẩn IEC tương ứng."))
    b.append(p("Đối với các quốc gia mà Tiêu chuẩn quốc gia chưa giống hệt Tiêu chuẩn IEC, cần có "
               "một thời gian chuyển tiếp để các quốc gia thành viên IECEx điều chỉnh tiêu chuẩn "
               "quốc gia theo tiêu chuẩn IEC và hướng tới chấp nhận trên phạm vi quốc gia chứng "
               "thư phù hợp IECEx cùng dấu IECEx."))
    b.append(p("Để biết thêm thông tin về Chương trình IECEx, truy cập " + _URL_IECEx + "."))

    b.append(note("<b>Đặc điểm của nguyên bản.</b> Chương gồm ba trang in (A11–A13; trang in = "
                  "trang PDF − 1), với ba bảng HTML, một hình vector và ba URL gốc. Trang A13 "
                  "là trang Notes để trống. Hình 6-1 được vẽ lại dạng vector từ trang ký hiệu "
                  "ATEX/CENELEC (A10). Mọi mã, số và URL gốc được giữ nguyên: 94/9/EC, 1 July "
                  "2003, 89/686/EEC, M1/M2, 1G/1D, 2G/2D, 3G/3D, " + _MARK + ", EN 50…, "
                  "T1 450° C đến T6 85° C và " + _URL_ATEX + ", " + _URL_CE + ", " + _URL_IECEx + "."))
    b.append(p("<i>Đây là bản dịch không chính thức, dùng cho mục đích học tập. Nội dung "
               "gốc © R. STAHL, Basics of Explosion Protection.</i>"))
    return "".join(b)


def body_en():
    b = []
    b.append(h2(TITLE_EN, TITLE_EN))
    b.append(lead("The ATEX Directive 94/9/EC is a directive adopted by the European Union (EU) "
                  "to facilitate free trade in the EU by aligning the technical and legal "
                  "requirements in the Member States for products intended for use in "
                  "potentially explosive atmospheres."))
    b.append(p("This Directive applies to electrical and non-electrical equipment/components "
               "and protective systems. The ATEX Directive became mandatory on July 1, 2003."))
    b.append(p("Equipment located outside potentially explosive atmospheres are also covered by "
               "the ATEX Directive under the following conditions:"))
    b.append(ul([
        "The equipment is a safety device, controller or regulatory device; and",
        "The equipment is required for the safe function of equipment or protective systems "
        "with respect to the risk of explosion.",
    ]))
    b.append(p("All equipment under its scope is required to bear the European CE Marking as "
               "verification of compliance with the Directive (the CE Marking will not appear "
               "on components defined by this Directive). The ATEX Directive specifically "
               "defines procedures for the evaluation of a product's design and production "
               "based on Equipment Groups and Categories. This is briefly outlined below."))

    b.append(h3("Equipment Group I Overview"))
    b.append(p("Equipment intended for use in underground parts of mines, and to those parts of "
               "surface installations of such mines, liable to be endangered by firedamp and/or "
               "combustible dust."))
    b.append(table(_HDR_EN, _G1_EN,
                   "Table 6-1 · Equipment Group I: protection compared with current IEC classification"))

    b.append(h3("Equipment Group II Overview"))
    b.append(p("Equipment intended for use in other than Equipment Group I places that are liable "
               "to be endangered by explosive atmospheres."))
    b.append(table(_HDR_EN, _G2_EN,
                   "Table 6-2 · Equipment Group II: protection compared with current IEC classification"))

    b.append(h3("ATEX Marking"))
    b.append(p("The marking of the equipment with the category will help the end-user with their "
               "selection of the equipment in that it identifies which Zone it can safely be "
               "installed in. This is a major improvement over the old cryptic marking system "
               "that only listed the protection concepts used in the design of the equipment. "
               "This meant that the user of the equipment had to be familiar with all eight "
               "recognized protection concepts and furthermore had to know which of them was "
               "suitable for a particular type of Zone."))
    b.append(fig(1, F.fig_f601()))
    b.append(p("The typical European ATEX/CENELEC marking " + _MARK + " is broken down in Figure "
               "6-1; the table below lists the categories, zones and corresponding area "
               "descriptions."))
    b.append(table(_ZONE_HDR_EN, _ZONE_EN,
                   "Table 6-3 · ATEX categories and corresponding gas/dust zones"))

    b.append(h3("Differences Between the Old and New Directives"))
    b.append(p("The main differences are:"))
    b.append(ul([
        "The inclusion of non-electrical equipment",
        "The inclusion of dust atmospheres",
        "Requirements for safety related devices (flame arrestors, suppression systems etc) and "
        "safe area equipment",
        "Additional quality system requirements",
        "The need to produce a 'Technical File'",
    ]))

    b.append(h3("Products Covered"))
    b.append(p("The Directive includes equipment and safety or control devices installed outside "
               "the potentially explosive area but having an explosion protection function. A "
               "wide range of products comes within the definition of equipment, including "
               "electric motors, compressors, diesel engines, lighting fittings, control and "
               "communication devices and monitoring and detection equipment, to name but a few. "
               "'Protective Systems' are also included, and include items that prevent an "
               "explosion that has been initiated from spreading or causing damage. They include "
               "flame arrestors, quenching systems, pressure relief panels and fast-acting "
               "shut-off valves to name but a few."))

    b.append(h3("Product Exclusions"))
    b.append(p("The Directive, however, does exclude the following product types:"))
    b.append(ul([
        "Medical devices",
        "Products for use in the presence of explosives",
        "Products for domestic use",
        "Sea-going vessels and mobile offshore units",
        "Military equipment",
        "Personal protective equipment covered by directive 89/686/EEC",
        "Means of transport by air or on road or rail or water networks. Vehicles intended for "
        "use in an explosive atmospheres are not excluded.",
    ]))
    b.append(p("For more info about ATEX, visit " + _URL_ATEX + "."))

    b.append(h3("CE Marking / Conformité Européenne"))
    b.append(p("The CE mark is a mandatory European marking for certain product groups to "
               "indicate conformity with the essential health and safety requirements set out "
               "in European Directives. The letters 'CE' are an abbreviation of Conformité "
               "Européenne, French for European conformity."))
    b.append(p("The CE mark must be affixed to a product if it falls under the scope of the so "
               "called 'New Approach' Directives. Without the CE marking, and thus without "
               "complying with the provisions of the Directives, the product may not be placed "
               "in the market or put into service in the fifteen member states of the European "
               "Union and Norway, Iceland and Liechtenstein. However, if the product meets the "
               "provisions of the applicable European Directives, and the CE mark is affixed to "
               "a product, these countries may not prohibit, restrict or impede the placing in "
               "the market or putting into service of the product. Thus, CE marking can be "
               "regarded as the products trade passport for Europe."))
    b.append(p("For more info about CE marking, visit " + _URL_CE + "."))

    b.append(h3("IECEx Scheme"))
    b.append(p("The objective of the IECEx Scheme is to facilitate global trade in electrical "
               "equipment intended for use in explosive atmospheres by eliminating the need for "
               "multiple national certification."))
    b.append(p("The IECEx Scheme provides the means for manufacturers of Ex equipment to obtain "
               "certificates of conformity that will be accepted at national level in all "
               "participating countries. A certificate of conformity may be obtained from any "
               "certification body accepted into the Scheme. The certificate will attest that "
               "the equipment design conforms to the relevant IEC Standards. The final objective "
               "of the IECEx Scheme is world-wide acceptance of one standard, one certificate "
               "and one mark."))
    b.append(p("For the IECEx Scheme to achieve its long term objective, every national Standard "
               "for which application is made by participating countries will need to be "
               "identical to the corresponding IEC Standard."))
    b.append(p("For countries whose national Standards are not yet identical to the IEC "
               "Standards, a transitional period will be necessary to allow time for "
               "participating IECEx Scheme member countries to adjust their national standards "
               "to the IEC standards and work toward national acceptance of IECEx Certificates "
               "of conformity and the IECEx mark."))
    b.append(p("For more info about IECEx Scheme, visit " + _URL_IECEx + "."))

    b.append(note("<b>Source quirks.</b> The unit spans three printed pages (A11-A13; printed = "
                  "PDF page - 1), with three HTML tables, one vector figure and three source "
                  "URLs. Printed A13 is a blank Notes page. Figure 6-1 was redrawn as a vector "
                  "from the ATEX/CENELEC marking page (A10). All original codes, numbers and "
                  "URLs are retained: 94/9/EC, July 1, 2003 (1 July 2003), 89/686/EEC, M1/M2, 1G/1D, 2G/2D, "
                  "3G/3D, " + _MARK + ", EN 50..., T1 450° C through T6 85° C, " + _URL_ATEX + ", "
                  + _URL_CE + " and " + _URL_IECEx + "."))
    b.append(p("<i>This is an unofficial translation for study purposes. Original content "
               "© R. STAHL, Basics of Explosion Protection.</i>"))
    return "".join(b)
