# -*- coding: utf-8 -*-
"""Book 7c, Chapter 11 - Sustainability (EN/VI bilingual).

Source: Emerson, *Control Valve Handbook*, 6th ed. (2020), printed pp. 240-249.
This is a short chapter: sustainability and the energy transition, energy
efficiency and optimization, decarbonization and the Paris temperature goals,
the three "Greening" practices, the GHG protocol Scope 1, 2 and 3 emissions,
net-zero ambitions and new technologies, environmental and social and
governance (ESG) approaches, collaboration, and a glossary of common terms.
Three numbered figures are redrawn as legible vectors in `cvh6fig11.py` and
placed in numbered order at their logical prose points.
"""

import cvh6_common as C  # noqa: F401
from cvh6_common import fig, h2, h3, h4, lead, note, p, ul
import cvh6fig11 as F11

PAGES_SRC = 10         # source printed pp. 240-249 inclusive
BYLINE = "Emerson Flow Controls · Control Valve Handbook, 6th ed. (2020)"
TITLE_EN = "Sustainability"
TITLE_VI = "Tính bền vững"


def note_terms(lang):
    """A one-line glossary box of the chapter's key terms."""
    if lang == "vi":
        return (
            "<b>Thuật ngữ chính của chương.</b> tính bền vững — sustainability · "
            "chuyển dịch năng lượng — energy transition · phi carbon hóa — decarbonization · "
            "giảm nhẹ carbon — carbon mitigation · khí nhà kính — greenhouse gas · "
            "giao thức khí nhà kính — greenhouse gas protocol · dấu vết khí nhà kính — "
            "greenhouse gas footprint · phát thải trực tiếp — direct emissions · "
            "phát thải gián tiếp — indirect emissions · Phạm vi 1, 2, 3 — Scope 1, 2, 3 · "
            "chuỗi giá trị — value chain · phát thải thượng nguồn và hạ nguồn — upstream and "
            "downstream emissions · thu giữ, sử dụng và lưu trữ carbon (CCUS) — Carbon, Capture, "
            "Utilization and Storage · phát thải ròng bằng không — net-zero · trung hòa carbon — "
            "carbon neutral · dấu vết carbon — carbon footprint · hiệu quả năng lượng — energy "
            "efficiency · năng lượng tái tạo — renewable energy · điện hóa — electrification · "
            "năm cơ sở — baseline year · mục tiêu dựa trên khoa học — science-based targets · "
            "SBTi — Science Based Target initiatives · ESG — môi trường, xã hội và quản trị "
            "(environmental, social and governance) · quản lý phát thải — emissions management · "
            "bể hấp thụ carbon — carbon sinks · trồng lại rừng — reforestation")
    return (
        "<b>Key terms in this chapter.</b> sustainability · energy transition · "
        "decarbonization · carbon mitigation · greenhouse gas · greenhouse gas protocol · "
        "greenhouse gas footprint · direct emissions · indirect emissions · Scope 1, 2, 3 · "
        "value chain · upstream and downstream emissions · Carbon, Capture, Utilization and "
        "Storage (CCUS) · net-zero · carbon neutral · carbon footprint · energy efficiency · "
        "renewable energy · electrification · baseline year · science-based targets · "
        "SBTi (Science Based Target initiatives) · ESG (environmental, social and governance) · "
        "emissions management · carbon sinks · afforestation · reforestation")


def source_notes(lang):
    """Source quirks and translation notes for this chapter."""
    if lang == "vi":
        return (
            "<b>Ghi chú về nguồn.</b> (1) Tiêu đề mục 11.8 in là «11. 8 ESG», có một dấu cách lạc "
            "sau «11.»; bản tiếng Anh giữ nguyên, bản tiếng Việt viết «11.8 ESG». (2) Nguồn viết "
            "«2C» và «1.5C» thay vì 2 °C và 1,5 °C ở mục 11.3 và 11.11; bản tiếng Anh giữ nguyên "
            "«2C» và «1.5C», bản tiếng Việt dùng ký hiệu nhiệt độ đúng. (3) Ký tự bullet OCR lạc "
            "«» xuất hiện ở cuối nhiều đoạn và trước các danh mục; nó được thay bằng đoạn văn "
            "hoặc danh sách bullet bình thường. (4) Các tiêu đề «Greening OF», «Greening By» và "
            "«Greening With» được giữ nguyên như bản in, kèm bản dịch tiếng Việt. (5) Một số lỗi "
            "chính tả và ngữ pháp được giữ trong tiếng Anh và sửa trong tiếng Việt: «accomodate», "
            "«indepth analysis», «Science Based Target initiatives's», «UNs Principles», «its "
            "controls systems», «sequesters them underground», «limit the efforts to 1.5C», và "
            "câu mở đầu bằng «To meet the internationally agreed goal...» không có động từ chính. "
            "(6) Mục 11.4 liệt kê hai lần mục «Replace control system for chilled water process - "
            "tune scheduling and setpoints»; cả hai lần đều được giữ. (7) Tiêu đề «New and "
            "Emerging Technologies» bị dump thành một dòng chảy liền: «Hydrogen Decarbonization- "
            "Carbon Capture Alternative Fuel and Biochemical Renewables Electrification and "
            "Storage»; ở đây được tách thành bốn nhóm, trong đó «Blue hydrogen» cũng xuất hiện "
            "hai lần như bản in. (8) Tiêu đề mục 11.9 in là «11.9 ESG - Approach by Companies», "
            "trong khi chú thích Hình 11.3 lại là «ESG Approach by Different Industries»; cả hai "
            "cách gọi được giữ nguyên tại vị trí tương ứng. Hình 11.3 cũng được chèn giữa câu "
            "«Remote oil and gas...» và phần tiếp theo trên trang 247; câu được nối lại để dễ đọc. "
            "(9) Đếm bullet theo bản in: Môi trường 6, Xã hội 8, Quản trị 4; Hình 11.3 vì thế có "
            "8 mục Xã hội, không phải 9. (10) Mục «Scope 1, 2, and 3 Emissions» thực sự nằm trong "
            "mục 11.6 trên trang 243, ngay trước chú thích Hình 11.1, dù nội dung liên quan chặt "
            "đến mục 11.3; thứ tự bản in được giữ nguyên. (11) Cụm «saunders valves» không xuất "
            "hiện trong chương này. (12) Các hình trong bản in là sơ đồ và danh sách bullet, không "
            "có dữ liệu số; chúng được vẽ lại dạng vector, không phải ảnh raster.")
    return (
        "<b>Source notes.</b> (1) The heading of section 11.8 prints as «11. 8 ESG», with a stray "
        "space after «11.»; the English text keeps it, while the Vietnamese text writes "
        "«11.8 ESG». (2) The source writes «2C» and «1.5C» instead of 2 °C and 1.5 °C in sections "
        "11.3 and 11.11; the English text keeps «2C» and «1.5C», while the Vietnamese text uses "
        "the correct temperature notation. (3) A stray OCR bullet glyph «» appears at the end of "
        "many paragraphs and before list entries; it is replaced by ordinary paragraphs or bullet "
        "lists. (4) The headings «Greening OF», «Greening By» and «Greening With» are kept as "
        "printed, with a Vietnamese translation alongside. (5) Several spelling and grammar "
        "quirks are retained in English and corrected in Vietnamese: «accomodate», «indepth "
        "analysis», «Science Based Target initiatives's», «UNs Principles», «its controls systems», "
        "«sequesters them underground», «limit the efforts to 1.5C», and the sentence fragment "
        "beginning «To meet the internationally agreed goal...». (6) Section 11.4 lists "
        "«Replace control system for chilled water process - tune scheduling and setpoints» "
        "twice; both occurrences are kept. (7) The «New and Emerging Technologies» heading is "
        "flattened in the dump into one run-on line, «Hydrogen Decarbonization- Carbon Capture "
        "Alternative Fuel and Biochemical Renewables Electrification and Storage»; it is split "
        "here into four groups, and «Blue hydrogen» appears twice exactly as printed. (8) The "
        "heading of section 11.9 prints as «11.9 ESG - Approach by Companies» while the Figure "
        "11.3 caption reads «ESG Approach by Different Industries»; both wordings are kept at "
        "their respective places. Figure 11.3 also interrupts the sentence beginning «Remote oil "
        "and gas...» before it continues on page 247; the sentence is joined here for legibility. "
        "(9) Printed bullet counts are Environmental 6, Social 8 and Governance 4; Figure 11.3 "
        "therefore has 8 Social items, not 9. (10) The subsection «Scope 1, 2, and 3 Emissions» is "
        "printed inside section 11.6 on page 243, just before the Figure 11.1 caption, although "
        "its content relates closely to section 11.3; the printed order is preserved. (11) The "
        "string «saunders valves» does not occur in this chapter. (12) The printed figures are "
        "a diagram and bullet lists with no numeric data; they are redrawn as vectors rather than "
        "raster images.")


def _body(lang):
    vi = lang == "vi"
    b = []

    def P(v, e):
        b.append(p(v if vi else e))

    def H(v, e, lvl=h2):
        b.append(lvl(v if vi else e))

    def B(v, e):
        b.append(ul(v if vi else e))

    def FIG(n, fn):
        b.append(fig(n, fn, lang))

    def N(v, e):
        b.append(note(v if vi else e))

    # ------------------------------------------------------------ lead
    b.append(lead(
        "Chương này trình bày tính bền vững trong lĩnh vực điều khiển quy trình: chuyển dịch năng "
        "lượng, hiệu quả và tối ưu hóa năng lượng, phi carbon hóa, phát thải khí nhà kính theo ba "
        "phạm vi, khát vọng phát thải ròng bằng không, và cách tiếp cận môi trường, xã hội và quản "
        "trị (ESG). Ba hình trong bản in được vẽ lại dạng vector và đặt theo thứ tự số tại vị trí "
        "văn bản hợp lý."
        if vi else
        "This chapter presents sustainability in the process control world: the energy transition, "
        "energy efficiency and optimization, decarbonization, greenhouse gas emissions across "
        "three scopes, net-zero ambitions, and the environmental, social and governance (ESG) "
        "approach. The three printed figures are redrawn as vectors and placed in numbered order "
        "at their logical prose points."))
    N(note_terms("vi"), note_terms("en"))

    # ------------------------------------------------------------ 11.1
    H("11.1 Tính bền vững", "11.1 Sustainability")
    P("Tính bền vững đã trở thành trục chính của quá trình chuyển dịch năng lượng từ các nguồn "
      "hóa thạch truyền thống sang một cơ cấu năng lượng đa dạng và bền vững hơn. Nhiều cuộc "
      "thảo luận vẫn còn mở và đang được xem xét về việc nên đặt mục tiêu bền vững nào và cách "
      "đạt được các mục tiêu đó. Những vấn đề bền vững then chốt quan trọng đối với lĩnh vực "
      "điều khiển quy trình gồm phi carbon hóa, quản lý phát thải, điện hóa, và hiệu quả và tối "
      "ưu hóa năng lượng. Các công nghệ như kiến trúc tích hợp cung cấp cái nhìn sâu sắc về vận "
      "hành từng đơn vị hoặc trên toàn ngành sẽ giúp hỗ trợ các nỗ lực bền vững và phi carbon "
      "hóa. Thiết bị hiện trường thông minh, phần mềm điều khiển và tối ưu hóa, cùng các công cụ "
      "mô phỏng quy trình có thể giúp công ty đạt được mục tiêu bền vững. Các công ty đang thay "
      "thế nhiên liệu ít carbon hơn như khí tự nhiên và hydrogen, đồng thời sử dụng năng lượng "
      "tái tạo từ gió, mặt trời, thủy điện, địa nhiệt và các nguồn nhiên liệu xanh. Trong khi "
      "đầu tư vào các lựa chọn năng lượng mới, sạch hơn, các công ty cũng phải tìm cách giảm phát "
      "thải trong ngắn hạn, trung hạn và dài hạn. Cụ thể, họ đang xem xét các giải pháp hiện có "
      "để: ngăn rò rỉ ngay từ đầu; tạo phát thải thấp đến bằng không bằng nguồn có cường độ carbon "
      "thấp hơn; và vận hành quy trình với quá trình cháy hiệu quả hơn và phát thải thấp hơn.",
      "Sustainability has become the main pivot in relation to energy transition from traditional "
      "fossil sources to a diverse and more sustainable mix of energy sources. Several "
      "conversations remain open and under discussion as to what sustainability targets to be set "
      "and ways of achieving those targets. The key sustainability issues that are important to "
      "the process control world, includes decarbonization, emissions management, electrification, "
      "and energy efficiency and optimization. Technologies such as integrated architectures that "
      "provide critical insights into operations unit by unit or across entire industries will "
      "help support sustainability and decarbonization efforts. Intelligent field devices, control "
      "and optimization software, and process simulation tools can help companies meet their "
      "sustainability targets. Companies are substituting less carbon-intensive fuels such as "
      "natural gas and hydrogen, as well as employing renewable energy from wind, solar, "
      "hydroelectric, geothermal, and green fuel sources. While companies invest in new, cleaner "
      "energy alternatives, they must also look for ways to cut emissions in the short-, mid-, and "
      "long-term. Specifically, they are looking at available today to: prevent leaks in the first "
      "place; produce low to zero emissions by using lower carbon intensity sources; and run "
      "processes with more efficient combustion and lower emissions.")
    P("Các quy trình thu giữ, sử dụng và lưu trữ carbon (CCUS) tách phát thải carbon tại nguồn và "
      "cô lập chúng dưới lòng đất. Công nghệ này có khả năng loại bỏ 90 đến 99% phát thải carbon "
      "của một cơ sở công nghiệp. Nó cũng hỗ trợ mở rộng quy mô sản xuất hydrogen các-bon thấp "
      "bằng cách chuyển phát thải thành nguồn nhiên liệu thay thế. Theo Cơ quan Năng lượng Quốc "
      "tế, CCUS là nhóm công nghệ duy nhất vừa góp phần trực tiếp giảm phát thải trong các lĩnh "
      "vực then chốt, vừa loại bỏ CO2 khỏi khí quyển để cân bằng các phát thải khó tránh nhất. "
      "Đây là một phần then chốt để đạt được mục tiêu phát thải ròng bằng không mà số lượng "
      "chính phủ và công ty ngày càng lớn đã tự đặt ra cho mình. Việc thu giữ carbon tại điểm "
      "phát thải, rồi sử dụng trong sản phẩm hoặc cô lập an toàn trong các tầng địa chất dưới "
      "lòng đất, sẽ là yếu tố quyết định để đạt đến một thế giới phát thải ròng bằng không.",
      "Carbon, Capture, Utilization and Storage (CCUS) processes extract point-source carbon "
      "emissions and sequesters them underground. The technology has the potential to remove 90 "
      "to 99% of an industrial facility's carbon emissions. It also supports scaling up production "
      "of low-carbon hydrogen by converting emissions into the alternative fuel source. According "
      "to the International Energy Agency, CCUS is the only group of technologies that contributes "
      "both to reducing emissions in key sectors directly and to removing CO2 from the atmosphere "
      "to balance the emissions that are the hardest to prevent. A crucial part of reaching the "
      "net-zero emissions goals that a growing number of governments and companies have set for "
      "themselves. Capturing carbon at the point of emissions and either utilizing it in products "
      "or sequestering it safely in underground geological formations will be critical to getting "
      "to a net-zero world.")

    # ------------------------------------------------------------ 11.2
    H("11.2 Giảm tiêu thụ năng lượng và nâng cao hiệu quả",
      "11.2 Energy Reduction and Efficiencies")
    P("Hiệu quả và tối ưu hóa năng lượng vẫn là chiến lược bền vững then chốt của thế giới. Chỉ "
      "khoảng một phần ba năng lượng sơ cấp được sản xuất hiện nay thực sự thực hiện chức năng "
      "mong muốn — sưởi ấm và làm mát ngôi nhà, di chuyển phương tiện, hoặc nấu ăn. Hai phần ba "
      "năng lượng đi vào hệ thống năng lượng bị thất thoát qua các trung gian như nhiệt thoát qua "
      "cửa sổ, phanh trên phương tiện, tổn thất đường dây điện trên quãng đường dài, các quá trình "
      "chuyển đổi năng lượng khác nhau, và các quy trình chưa được tối ưu. Có một cơ hội lớn để "
      "tiếp tục nâng cao hiệu quả năng lượng, như phản ánh trong nhiều lộ trình được xây dựng nhằm "
      "cung cấp các hệ thống năng lượng của tương lai.",
      "Energy efficiency and optimization remains a critical sustainability strategy for the "
      "world. Only about one-third of the primary energy produced today actually performs the "
      "desired function — heating and cooling a home, moving a vehicle, or cooking food. "
      "Two-thirds of the energy that goes into the energy system is lost through mediums like heat "
      "escaping through windows, brakes applied in vehicles, electrical line losses over long "
      "distances, various energy transformations, and unoptimized processes. There is a major "
      "opportunity to continue enhancing energy efficiency as reflected in many of the roadmaps "
      "developed to deliver tomorrows energy systems.")
    P("Các ngành công nghiệp tiêu thụ nhiều năng lượng đang chịu áp lực trở nên bền vững hơn và "
      "đạt được mức giảm đáng kể phát thải khí nhà kính. Cũng có nhiều quy trình năng lượng tái "
      "tạo và giải pháp công nghệ tiềm năng, như hydrogen tái tạo (xanh), thu giữ carbon, nhiên "
      "liệu sinh học, hóa chất sinh học và tái chế nhựa, cho thấy khả năng giảm đáng kể hoặc loại "
      "bỏ phát thải khí nhà kính. Các giải pháp thúc đẩy tiến bộ bền vững môi trường bao gồm bốn "
      "lĩnh vực chiến lược: phi carbon hóa nguồn năng lượng, điện hóa và tích hợp hệ thống, hiệu "
      "quả và tối ưu hóa năng lượng, và quản lý phát thải.",
      "Energy intense industries are under pressure to become more sustainable and reach "
      "significant reduction in Greenhouse Gas emissions. There are also many potential renewable "
      "energy processes and technology solutions, like renewable (green) hydrogen, carbon capture, "
      "biofuels, biochemicals, and plastic recycling that show substantial reduction or "
      "elimination of Greenhouse Gas emissions. Solutions that enable the environmental "
      "sustainability progress cover four strategic areas: Energy Source Decarbonization, "
      "Electrification and System Integration, Energy Efficiency and Optimization, and Emissions "
      "Management.")

    # ------------------------------------------------------------ 11.3
    H("11.3 Phi carbon hóa", "11.3 Decarbonization")
    P("Phi carbon hóa ngày càng được chú ý khi nhiệt độ toàn cầu tăng lên trong những năm gần "
      "đây, so với mục tiêu của Thỏa thuận Paris là giữ nhiệt độ trong mức 2C đến năm 2050. Giảm "
      "nhẹ carbon đã trở thành vấn đề quan trọng và cấp bách trong xã hội, thâm nhập vào nhiều "
      "lĩnh vực đời sống gồm chính trị, văn hóa, kinh tế, môi trường và công nghiệp. Hội nghị "
      "Thượng đỉnh Khí hậu Paris năm 2015 đã đạt được thỏa thuận với mục tiêu giữ mức tăng nhiệt "
      "độ trung bình toàn cầu ở mức thấp hơn nhiều so với 2C so với thời kỳ tiền công nghiệp "
      "trong thế kỷ này, và tiếp tục nỗ lực hạn chế mức tăng đó ở mức 1.5C (IPCC, 2014). Nhiều "
      "ngành trong lĩnh vực hóa chất, điện, dầu và khí, hybrid, khai khoáng, xi măng, thép, giấy "
      "và bột giấy đang tìm kiếm các lộ trình khả thi để phi carbon hóa các quy trình công nghiệp "
      "nặng và tiêu thụ nhiều carbon này. Kết quả là hầu hết các ngành này đã xác định và xây "
      "dựng lộ trình phi carbon hóa dẫn đến phát thải carbon ròng bằng không vào năm 2050. Nhằm "
      "đạt được mục tiêu đã được thỏa thuận quốc tế là hạn chế mức nóng lên toàn cầu tối đa 1.5C "
      "so với thời kỳ tiền công nghiệp, các ngành đang xem xét hai phương pháp chung.",
      "Decarbonization has gained prominence with increasing global temperatures over recent "
      "years, as against the goal of the Paris Agreement for limiting the temperature within 2C "
      "until 2050. Carbon mitigation has become an important and urgent issue in society, "
      "infiltrating into various societal fields including politics, culture, economy, environment, "
      "and industry. The Paris Climate Summit in 2015 reached an agreement declaring the objective "
      "of keeping the increase in global average temperature to well below 2C above preindustrial "
      "levels within the century and further to pursue efforts to limit the efforts to 1.5C "
      "(IPCC, 2014). Several industries in the chemical, power, oil and gas, hybrid, mining, "
      "cement, steel, paper, and pulp are exploring plausible pathways towards decarbonizing these "
      "heavy and carbon intensive industrial processes. As a result, most of these industries have "
      "identified and developed decarbonization pathways that will lead to total net-zero carbon "
      "emissions by 2050. To meet the internationally agreed goal of limiting global climate "
      "warming to a maximum of 1.5C versus the preindustrial period. Industries are considering "
      "two general methods.")
    B(["Giảm nhẹ nguồn phát thải carbon: tăng mạnh tỷ trọng nguồn tái tạo và cải thiện hiệu quả "
       "cho các quy trình công nghiệp tiêu thụ nhiều carbon.",
       "Triển khai công nghệ CCUS và củng cố các bể hấp thụ carbon như trồng rừng mới và trồng "
       "lại rừng."],
      ["Mitigation of carbon sources: massive penetration of renewable resources and efficiency "
       "improvement for carbon intensive industrial processes.",
       "Deployment of CCUS technologies and reinforcement of carbon sinks such as afforestation "
       "and reforestation."])

    # ------------------------------------------------------------ 11.4
    H("11.4 Xanh hóa từ bên trong (Greening OF)", "11.4 Greening OF")
    P("Xanh hóa từ bên trong (Greening OF) tập trung vào việc công ty hoặc tổ chức thiết lập các "
      "sáng kiến và mục tiêu nội bộ nhằm giảm phát thải khí nhà kính. Greening OF cũng bao gồm "
      "việc gắn kết các đối tác thượng nguồn để đảm bảo họ giảm phát thải khí nhà kính trong các "
      "sản phẩm họ cung cấp cho bạn với tư cách khách hàng. Một ví dụ về cách công ty có thể thể "
      "hiện cam kết và đầu tư mạnh mẽ vào Greening OF là tổ chức các cuộc tìm kiếm tại tất cả địa "
      "điểm để truy tìm cơ hội giảm tiêu thụ năng lượng.",
      "Greening OF is focused on a company or organization setting in-house initiatives and goals "
      "to reduce greenhouse gas emission. Greening OF also involves engaging upstream partners in "
      "making sure they are reducing greenhouse gas emissions in the products they provide to you "
      "as a customer. An example of ways companies can show strong commitment and investment in "
      "Greening OF is with treasure hunts at all locations looking for opportunities to reduce "
      "energy consumption.")
    P("Có thể triển khai các sáng kiến giúp cải thiện hiệu quả bền vững nội bộ. Bằng cách lôi kéo "
      "các nhà cung cấp năng lượng, đối tác chuỗi cung ứng và dịch vụ logistics cùng hỗ trợ mục "
      "tiêu tương tự là xanh hóa quy trình của họ. Một số sáng kiến bền vững có tác động đáng kể "
      "đến giảm phát thải khí nhà kính:",
      "Initiatives can be implemented to help improve internal sustainability performance. By "
      "enlisting energy providers, supply chain partners and logistics services to support "
      "similar objectives of greening their processes. Some sustainable initiatives that have "
      "significant impact on greenhouse gas reduction:")
    B(["Cải tạo hệ thống chiếu sáng sang LED",
       "Tắt chiếu sáng tự động",
       "Phát hiện rò rỉ khí nén",
       "Thay thế hệ thống điều khiển cho quy trình nước lạnh - điều chỉnh lịch trình và điểm đặt",
       "Thay đồ đèn trong phòng thí nghiệm lưu lượng sang LED",
       "Thay thế hệ thống điều khiển cho quy trình nước lạnh - điều chỉnh lịch trình và điểm đặt"],
      ["LED lighting retrofits",
       "Automated lighting shutdown",
       "Compressed air leak detection",
       "Replace control system for chilled water process - tune scheduling and setpoints",
       "Changeout flow lab light fixtures to LED",
       "Replace control system for chilled water process - tune scheduling and setpoints"])
    P("Đạt phát thải ròng bằng không và triển khai lộ trình phi carbon hóa trong khuôn khổ một "
      "công ty dẫn đến việc thúc đẩy giảm phát thải tại nơi chúng ta có thể tạo tác động lớn nhất "
      "— với nhà cung cấp và đối tác.",
      "Getting to net-zero and implementing decarbonization roadmaps within the four walls of a "
      "company lead to catalyze emission reductions where we can have the greatest impact — with "
      "suppliers and partners.")

    # ------------------------------------------------------------ 11.5
    H("11.5 Xanh hóa thông qua sản phẩm (Greening By)", "11.5 Greening By")
    P("Với tư cách là công nghệ hỗ trợ quá trình chuyển dịch các-bon thấp của thế giới, những đóng "
      "góp tích cực cho môi trường và khí hậu sẽ đến từ việc áp dụng công nghệ và thiết bị mới "
      "tiết kiệm năng lượng, dù là hệ thống điều khiển, phần mềm hay phần cứng. Cơ hội hỗ trợ các "
      "mục tiêu bền vững và phi carbon hóa bằng sản phẩm và dịch vụ — dù là nâng cấp bao bì thân "
      "thiện môi trường, giải pháp điện hóa hay giám sát tình trạng van — thì công nghệ và sản "
      "phẩm sẽ là một phần quan trọng trong việc phi carbon hóa lĩnh vực quy trình trong tương "
      "lai. Bất kỳ phân khúc ngành nào có phát thải thoát hơi hoặc phát thải khí nhà kính đều là "
      "ứng viên để xanh hóa quy trình của mình, từ điện, năng lượng, hóa chất, sản xuất kim loại, "
      "xi măng, đến chuỗi lạnh, quản lý chất thải, và sưởi ấm và làm mát trong tòa nhà thương mại "
      "và dân cư. Nhưng nỗ lực bổ sung từ khu vực công và tư sẽ là then chốt để làm cho lưới điện "
      "thông minh hơn, phát thải ít carbon hơn và bền vững hơn.",
      "As technology enablers of the world's low-carbon transition, positive environmental and "
      "climate contributions will come from the adoption of new energy efficient technologies and "
      "equipment, whether its controls systems, software, or hardware. The opportunity to support "
      "sustainability and decarbonization goals with products and services —whether it is "
      "upgrading to environmental packing, electric solution or valve condition monitoring, — "
      "technology and products will be an important part of decarbonizing the process world going "
      "forward. Any industry segment that has fugitive emissions or greenhouse gas emission is a "
      "candidate for greening their process, from power, energy, chemicals, metals production, "
      "cement, to the cold chain, waste management, as well as heating and cooling in commercial "
      "and residential buildings. But additional public and private sector efforts will be "
      "critical to make energy grids smarter, produce lower carbon, and be more resilient.")

    # ------------------------------------------------------------ 11.6
    H("11.6 Xanh hóa cùng đối tác (Greening With)", "11.6 Greening With")
    P("Khi thế giới tiếp tục tăng tốc hướng tới phát thải carbon ròng bằng không, việc chia sẻ "
      "trong cộng đồng toàn cầu và địa phương về công nghệ tương lai cần đáp ứng nhu cầu này, cũng "
      "như những điều chỉnh hoặc cải tiến cần thực hiện để thích ứng với các thay đổi, luôn quan "
      "trọng. Cách tiếp cận này bao gồm tham gia các diễn đàn hàng đầu của ngành, hợp tác với các "
      "viện nghiên cứu để thúc đẩy đổi mới, và tạo điều kiện chủ động làm việc với các chính phủ "
      "trên toàn thế giới. Bền vững môi trường liên quan đến nhiều bất định, nhưng một điều rõ "
      "ràng là — quy mô, phạm vi và độ phức tạp của quá trình chuyển dịch các-bon thấp đến mức "
      "không một bên liên quan nào (chính phủ, doanh nghiệp, cộng đồng hay giới học thuật) có thể "
      "tự mình quản lý. Các liên minh đa bên là điều cần thiết để vượt qua những thách thức này.",
      "As the world continues to accelerate towards total net zero carbon emissions, it is always "
      "important to share as a global and local community on what technologies should look like "
      "in the future to meet this demand and what adjustments or improvements must be made to "
      "accomodate these changes. This approach involves participation in leading industry forums, "
      "collaborating with research institutions to drive innovation, and enabling proactive "
      "engagement with governments worldwide. Environmental sustainability involves many "
      "uncertainties, but one thing is clear — the scale, scope, and complexity of the low-carbon "
      "transition is such that no one stakeholder (government, business, communities, or academia) "
      "can manage it alone. Multi-stakeholder alliances are essential to overcome its challenges.")

    H("Phát thải Phạm vi 1, 2 và 3", "Scope 1, 2, and 3 Emissions", h4)
    P("Giao thức khí nhà kính phân loại dấu vết khí nhà kính của công ty thành ba phạm vi khác "
      "nhau. Phát thải Phạm vi 1 là phát thải trực tiếp từ các nguồn thuộc sở hữu hoặc kiểm soát, "
      "chẳng hạn phát thải từ hệ thống sưởi ấm trong văn phòng hoặc từ các ứng dụng công nghiệp "
      "tại cơ sở sản xuất của chúng tôi. Phát thải Phạm vi 2 là phát thải gián tiếp từ việc sản "
      "xuất điện năng đã mua. Các phát thải này được coi là gián tiếp vì dù phát thải là kết quả "
      "của hoạt động của chúng tôi, chúng lại xảy ra tại điểm phát điện, thường là nguồn nhiên "
      "liệu hóa thạch như than hoặc khí tự nhiên.",
      "The greenhouse gas protocol categorizes a company's greenhouse gas footprint into three "
      "different scopes. Scope 1 emissions are direct emissions from owned or controlled sources, "
      "such as emissions from comfort heating in our offices or from industrial applications in "
      "our manufacturing sites. Scope 2 emissions are indirect emissions from the generation of "
      "purchased electricity. These emissions are considered indirect because even though the "
      "emissions are a result of our activities, the emissions occur at the point of generation, "
      "typically a fossil fuel source like coal or natural gas.")
    FIG(1, F11.fig_f11_01())
    P("Một số công ty đã báo cáo phát thải Phạm vi 1 và Phạm vi 2 nhưng chưa đo lường đầy đủ phát "
      "thải Phạm vi 3. Phát thải Phạm vi 3 là tất cả phát thải gián tiếp khác xảy ra trong chuỗi "
      "giá trị. Phạm vi 3 thường là đóng góp đáng kể vào tổng phát thải của tổ chức, vì nó đóng "
      "vai trò là “danh mục gom chung” cho mọi phát thải liên quan đến năng lượng không thuộc "
      "Phạm vi 1 hoặc Phạm vi 2, và gồm 14 danh mục phát thải khác, bao gồm phát thải thượng "
      "nguồn và hạ nguồn. Phát thải hạ nguồn phát sinh từ phân phối, từ việc khách hàng sử dụng "
      "sản phẩm tại nhà và cơ sở của họ, và từ cách sản phẩm được xử lý khi hết vòng đời. Phát "
      "thải thượng nguồn phát sinh từ sản xuất và vật liệu dùng trong các linh kiện được mua, "
      "hoặc từ phát thải trực tiếp của nhà cung cấp. Phạm vi 3 cũng gồm các phát thải khác phát "
      "sinh từ hoạt động gián tiếp như đi công tác và đi lại của nhân viên.",
      "Some companies have reported on Scope 1 and Scope 2 emissions but have not fully measured "
      "on Scope 3 emissions. Scope 3 emissions are all other indirect emissions that occur within "
      "the value chain. Scope 3 is typically a significant contributor to total organization "
      "emissions, as it acts as a “catch all” for any energy-related emissions not included in "
      "Scope 1 or Scope 2, and includes 14 other categories of emissions, including upstream and "
      "downstream emissions. Downstream emissions stem from distribution, from customers use of "
      "the products in their homes and facilities, and from how products are treated at end of "
      "life. Upstream emissions stem from the manufacturing and materials used in the parts that "
      "are purchased, or the direct emissions of suppliers. Scope 3 also includes miscellaneous "
      "emissions stemming from indirect activities like business travel and employee commuting.")
    H("Phạm vi 3 gồm 15 danh mục khác nhau", "Scope 3 Includes 15 Different Categories", h4)
    B(["Hàng hóa và dịch vụ đã mua",
       "Hàng hóa vốn",
       "Hoạt động liên quan đến nhiên liệu và năng lượng không thuộc Phạm vi 1 hoặc Phạm vi 2",
       "Phân phối thượng nguồn",
       "Chất thải phát sinh trong vận hành",
       "Đi công tác",
       "Đi lại của nhân viên",
       "Tài sản thuê thượng nguồn",
       "Phân phối hạ nguồn",
       "Chế biến sản phẩm đã bán",
       "Sử dụng sản phẩm đã bán",
       "Xử lý sản phẩm đã bán khi hết vòng đời",
       "Tài sản thuê hạ nguồn",
       "Nhượng quyền thương mại",
       "Đầu tư"],
      ["Purchased goods and services",
       "Capital goods",
       "Fuel- and energy-related activities not included in Scope 1 or Scope 2",
       "Upstream distribution",
       "Waste generated in operations",
       "Business travel",
       "Employee commuting",
       "Upstream leased assets",
       "Downstream distribution",
       "Processing of sold products",
       "Use of sold products",
       "End-of-life treatment of sold products",
       "Downstream leased assets",
       "Franchises",
       "Investments"])
    P("Từ số liệu trung bình của ngành, chúng ta biết rằng hàng hóa và dịch vụ mua thượng nguồn "
      "thực sự chiếm một phần lớn phát thải Phạm vi 3; trung bình phần này đóng góp khoảng 20-30% "
      "tổng Phạm vi 3. Ngoài ra, việc sử dụng sản phẩm đã bán chiếm khoảng 60-65%, đi công tác và "
      "đi lại của nhân viên khoảng 2-3%, và logistics (đầu vào và đầu ra) cũng khoảng 2-3%.",
      "We know from the industry averages that upstream purchased goods and services does tend to "
      "have a large chunk of Scope 3 emissions, the average is that this piece contributes just "
      "about 20-30% of the total Scope 3. Also, use of products sold tends to be around 60-65%, "
      "business travel and employee commute will be about 2-3% and logistics (in and outbound) "
      "around 2-3% as well.")
    P("Nhìn chung, độ chính xác liên quan đến phát thải Phạm vi 3 sẽ tiếp tục cải thiện khi có thêm "
      "dữ liệu được ghi nhận, cho danh mục này cũng như các danh mục khác. Mục tiêu ở đây là, dù "
      "hiện công ty chưa bị yêu cầu báo cáo về Phạm vi 3, một số đơn vị đã chủ động đo lường thông "
      "tin này ngay từ nay, với kỳ vọng họ sẽ được yêu cầu báo cáo thông tin này trong tương lai "
      "rất gần.",
      "In general, the precision around the Scope 3 emissions will continue to get better as more "
      "data is recorded, for this category and for the other categories. The objective here, is "
      "that while companies are not being asked to report out on Scope 3 today, some are being "
      "proactive and measuring this information now, with the expectation that they will be asked "
      "to report out on this information in the very near future.")

    # ------------------------------------------------------------ 11.7
    H("11.7 Khát vọng phát thải ròng bằng không", "11.7 Net-Zero Ambitions")
    P("Khi thế giới đối mặt với những thách thức lớn và cấp bách do biến đổi khí hậu, ngành công "
      "nghiệp đang đáp ứng các yêu cầu này bằng cách thảo luận và giải quyết các hoạt động giúp "
      "giảm nhẹ tác động tiêu cực đến môi trường. Các công ty đặt mục tiêu đạt phát thải khí nhà "
      "kính ròng bằng không trên Phạm vi 1, Phạm vi 2 và Phạm vi 3 bằng cách phân tích chuyên sâu "
      "tổng phát thải của mình và dùng thông tin này để xác định năm cơ sở. Sau khi năm cơ sở "
      "được thiết lập, công ty có thể đặt mục tiêu giảm phát thải khí nhà kính với năm mục tiêu "
      "đạt phát thải ròng bằng không. Để đảm bảo mục tiêu của chúng ta tuân theo khoa học khí hậu "
      "mới nhất, tốt nhất là điều chỉnh theo một tổ chức được quốc tế công nhận như Tiêu chuẩn "
      "Phát thải ròng bằng không của Sáng kiến Mục tiêu dựa trên Khoa học (Science Based Target "
      "initiatives, SBTi). SBTi là tổ chức hàng đầu thế giới thúc đẩy việc áp dụng các mục tiêu "
      "dựa trên khoa học. Một thiết kế phát thải ròng bằng không vững chắc đòi hỏi giảm tuyệt đối "
      "phát thải khí nhà kính ít nhất 90%, cho phép trung hòa carbon chất lượng cao ở các phần "
      "khác của hệ sinh thái đối với phát thải còn lại không thể giảm bằng cách khác.",
      "As the world grapples with huge and urgent challenges posed by climate change, industry is "
      "rising to these demands by discussing and addressing activities that would help mitigate "
      "negative impacts on the environment. Companies establish targets to reach net-zero "
      "greenhouse gas emissions across Scope 1, Scope 2, and Scope 3 by completing indepth "
      "analysis of their total emissions and using this information to set a baseline year. Once "
      "the baseline year has been established, the company then can set a goal to reduce "
      "greenhouse gas emissions with a target year to be net-zero. To ensure our goals follow the "
      "latest climate science, it is best to be aligned with an internationally recognized "
      "organization like Science Based Target initiatives's (SBTi) Net-Zero Standard to set goals. "
      "SBTi is the world's leading organization in driving the adoption of science-based targets. "
      "A robust net-zero design requires the absolute reduction of greenhouse gas emissions by at "
      "least 90%, allowing for high-quality carbon neutralization in other parts of the ecosystem "
      "for any residual emissions, which cannot be otherwise abated.")
    P("Sau khi công ty hoặc tổ chức đã đặt mục tiêu giảm phát thải khí nhà kính, điều quan trọng "
      "là theo dõi và đo lường tiến độ hàng năm. Việc thúc đẩy chương trình bền vững và phi carbon "
      "hóa trong nội bộ công ty là then chốt để duy trì động lực và sự quan tâm đối với lĩnh vực "
      "bền vững quan trọng và đáng giá này. Chuyển dịch năng lượng và phi carbon hóa áp dụng cho "
      "cả dự án mới và dự án hiện hữu, cùng các cơ hội bảo trì, sửa chữa và đại tu (MRO), cho phép "
      "khách hàng xanh hóa quy trình của mình bằng cách giảm phát thải khí nhà kính nhằm hỗ trợ "
      "mục tiêu phát thải ròng bằng không toàn diện vào năm 2050.",
      "Once a company or organization set greenhouse gas emission reduction targets, it is "
      "important to monitor and measure progress on a yearly basis. It is crucial to drive the "
      "sustainability and decarbonization agenda within a company to maintain motivation and "
      "interest in this all important and rewarding area of sustainability. The energy transition "
      "and decarbonization applies to green and brownfield projects along with MRO opportunities "
      "allowing customers the ability to green their processes by reducing greenhouse gas "
      "emissions in support of total net-zero goals by 2050.")

    H("Công nghệ mới và mới nổi", "New and Emerging Technologies", h4)
    P("Phi carbon hóa hydrogen · Thu giữ carbon · Nhiên liệu thay thế và hóa chất sinh học · "
      "Điện hóa và lưu trữ",
      "Hydrogen Decarbonization · Carbon Capture · Alternative Fuel and Biochemical Renewables · "
      "Electrification and Storage")
    B(["Điện phân nước sản xuất hydrogen xanh",
       "Hydrogen xanh dương",
       "Amonia xanh",
       "Hỗn hợp hydrogen và khí tự nhiên",
       "Hóa lỏng",
       "Vận chuyển",
       "Lưu trữ hydrogen"],
      ["Green hydrogen electrolyzers",
       "Blue hydrogen",
       "Green ammonia",
       "Blended hydrogen and natural gas",
       "Liquefaction",
       "Transportation",
       "Hydrogen storage"])
    B(["Phát thải thoát hơi",
       "Hydrogen xanh dương",
       "CCUS",
       "Giảm tiêu thụ năng lượng và hiệu quả năng lượng"],
      ["Fugitive emissions",
       "Blue hydrogen",
       "CCUS",
       "Energy reduction and energy efficiency"])
    B(["Giảm phát thải khí nhà kính",
       "Nhiên liệu sinh học / năng lượng sinh học / rác thải thành năng lượng",
       "Nhiên liệu tái tạo - diesel bền vững: SAF",
       "Nhựa sinh học",
       "Tái chế nhựa",
       "Nhựa phân hủy sinh học",
       "Khí sinh học - khí đốt tái tạo",
       "Năng lượng mặt trời - chuỗi giá trị polysilicon",
       "Trang trại gió ngoài khơi",
       "Địa nhiệt"],
      ["Greenhouse gas emissions reduction",
       "Bio fuel / bio energy / waste to energy",
       "Renewable fuel - sustainable diesel: SAF",
       "Bio plastics",
       "Plastic recycling",
       "Biodegradable plastics",
       "Biogas - renewable natural gas",
       "Solar - polysilicon value chain",
       "Offshore wind farms",
       "Geothermal"])
    B(["Khai thác lithium và nickel",
       "Chế biến kim loại pin",
       "Tái chế pin",
       "Điện hóa bộ truyền động",
       "Bể chứa muối nóng chảy"],
      ["Lithium and nickel mining",
       "Battery metal processing",
       "Battery recycling",
       "Actuator electrification",
       "Molten salt reservoirs"])
    FIG(2, F11.fig_f11_02())

    # ------------------------------------------------------------ 11.8
    H("11.8 ESG", "11. 8 ESG")
    P("Đầu tư vào các công ty ủng hộ các vấn đề môi trường, xã hội và quản trị (ESG) đã được thảo "
      "luận trong nhiều thập kỷ nhưng hiện đang tiến lên vị trí hàng đầu trong các sáng kiến doanh "
      "nghiệp. ESG có thể đã trở thành hiện thực vào năm 2004 khi Tổng Thư ký Liên Hợp Quốc Kofi "
      "Annan mời 50 giám đốc điều hành của các tổ chức tài chính lớn tham gia một sáng kiến tìm "
      "cách tích hợp các khái niệm ESG vào thị trường toàn cầu. Trong báo cáo năm 2006 về Nguyên "
      "tắc Đầu tư Trách nhiệm của Liên Hợp Quốc (PRI), thuật ngữ ESG đã được đặt ra nhằm giải "
      "thích cách việc ủng hộ các yếu tố ESG mang lại lợi ích kinh doanh, tạo ra thị trường bền "
      "vững và mang lại lợi ích cho xã hội. Từ đó đến nay, phong trào đã đạt được sức nóng, với "
      "nhiều nhà đầu tư và bên liên quan tích cực yêu cầu công ty thực hiện cải tiến ESG và công "
      "khai thể hiện tiến bộ trong các lĩnh vực then chốt.",
      "Investing in firms that champion environmental, social, and governance (ESG) issues has "
      "been discussed for decades but is now moving to the forefront of corporate initiatives. "
      "ESG may have transitioned to reality in 2004 when the United Nations Secretary, Kofi Annan, "
      "asked 50 major financial institution Chief Executive Officers to join an initiative for "
      "finding ways to integrate ESG concepts into global markets. In the 2006 UNs Principles for "
      "Responsible Investment (PRI) report, the term ESG was coined that explained how championing "
      "ESG factors made good business sense, created sustainable markets, and benefited society. "
      "Since that time, the movement has gained traction, with many investors and stakeholders "
      "actively demanding that companies engage in ESG improvements and publicly show their "
      "progress in key areas.")
    P("Những lời kêu gọi mạnh đến mức Ủy ban Chứng khoán và Giao dịch Hoa Kỳ (SEC) đang xây dựng "
      "hướng dẫn báo cáo để công ty có thể cung cấp các mô tả nhất quán và chính xác về chương "
      "trình ESG của mình, bên cạnh báo cáo tài chính tiêu chuẩn. “Ở mức đơn giản nhất, ESG cung "
      "cấp một khung tổng thể để xem xét tác động và sự phụ thuộc của công ty đối với môi trường "
      "và xã hội, cũng như chất lượng quản trị doanh nghiệp.”",
      "The calls have been so great that the U.S. Securities and Exchange Commission (SEC) is "
      "creating reporting guidelines so companies can provide consistent and accurate accounts of "
      "their ESG programs, alongside their standard financial reports. “At its simplest, ESG "
      "provides an umbrella framework to consider a company's impact and dependencies on the "
      "environment and society as well as the quality of its corporate governance.”")

    # ------------------------------------------------------------ 11.9
    H("11.9 ESG - Tiếp cận theo từng công ty",
      "11.9 ESG - Approach by Companies")
    P("Dù các vấn đề xã hội và quản trị áp dụng cho hầu hết mọi công ty, các công ty hóa dầu tự "
      "nhiên tập trung nhiều hơn vào các vấn đề môi trường. Có một áp lực công chúng rất lớn đối "
      "với ngành nhằm phi carbon hóa các dòng sản "
      "phẩm và giảm phát thải chất ô nhiễm, đặc biệt là khí nhà kính. Để đạt được những mục tiêu "
      "này, hầu hết công ty đang dùng cách tiếp cận đa hướng. Một sáng kiến lớn là dùng nguyên liệu "
      "đầu vào tái chế và tái tạo để tạo nhiên liệu thay thế các-bon thấp. Các nguyên liệu này có "
      "thể gồm dầu đậu nành, dầu ngô, mỡ bò, mỡ trắng và dầu ăn đã qua sử dụng, cũng như dầu từ "
      "tảo, hạt cải dầu và carinata. Các quy trình khác thu khí sinh học từ nhiều nguồn nông nghiệp "
      "và chất thải, rồi chuyển những phát thải khí nhà kính tiềm ẩn đó thành biomethane có thể "
      "bán để bơm vào đường ống khí tự nhiên. Một nguồn cải thiện môi trường khác đến từ việc "
      "giảm phát thải methane có chủ đích và phát thải thoát hơi. Các vùng sản xuất dầu khí xa "
      "xôi và đường ống thường dùng khí tự nhiên làm động lực cho thiết bị đo và truyền động van, "
      "và methane được xả ra sau mỗi hành trình hoặc rỉ liên tục.",
      "While societal and governance issues apply to nearly all companies, petrochemical companies "
      "are naturally more focused on environmental issues. There is a great deal of public "
      "pressure on the industry to decarbonize product streams and reduce emissions of pollutants, "
      "especially greenhouse gases. To accomplish these goals, most firms are utilizing a "
      "multipronged approach. One major initiative is the use of recycled and renewable feedstocks "
      "to create low-carbon alternative fuels. Such feedstocks might include soybean oil, corn oil, "
      "beef tallow, white grease and used cooking oils, as well as oils from algae, rapeseed and "
      "carinata. Other processes collect biogas from various agricultural and waste sources and "
      "then convert those potential greenhouse gas emissions to saleable biomethane for injection "
      "into natural gas pipelines. Another source of environmental improvements comes from the "
      "reduction of intentional and fugitive methane emissions. Remote oil and gas production "
      "areas and pipelines often use natural gas as a motive force for instrumentation and valve "
      "actuation, and methane is vented with each stroke or bled continuously.")
    B(["Giảm phát thải khí nhà kính",
       "Theo dõi dấu vết môi trường",
       "Phi carbon hóa nguồn năng lượng: hỗ trợ các cam kết carbon thấp",
       "Quản lý phát thải",
       "Hợp tác với các trường đại học trên thế giới",
       "Bảo vệ chất lượng thực phẩm và tính bền vững môi trường"],
      ["Reducing greenhouse gas emissions",
       "Tracking environmental footprint",
       "Energy source decarbonization: supporting low carbon commitments",
       "Emissions management",
       "Collaboration with universities around the world",
       "Protecting food quality and environmental sustainability"])
    B(["Thúc đẩy an toàn và an ninh",
       "An toàn nơi làm việc",
       "Đa dạng, công bằng và hòa nhập",
       "Giáo dục khoa học, công nghệ, kỹ thuật và toán học (STEM)",
       "Gắn kết nhân viên",
       "Đào tạo và phát triển",
       "Đào tạo cho nơi làm việc tương lai",
       "Thúc đẩy tương lai của cộng đồng"],
      ["Enabling safety and security",
       "Workplace safety",
       "Diversity, Equity, and Inclusion",
       "Science, technology, engineering, and mathematics education (STEM)",
       "Employee engagement",
       "Training and development",
       "Training the workplace of the future",
       "Advancing the future of communities"])
    B(["Cơ cấu và tính đa dạng của hội đồng quản trị",
       "Hành động quản trị doanh nghiệp",
       "Quản lý rủi ro và giám sát",
       "Chính trực và đạo đức"],
      ["Board diversity and structure",
       "Corporate governance actions",
       "Risk management and oversight",
       "Integrity and ethics"])
    FIG(3, F11.fig_f11_03())
    P("Ngoài ra, hầu hết van điều khiển và/hoặc bơm trong dịch vụ hóa chất có xu hướng thải chất "
      "ô nhiễm qua rò rỉ đệm và phớt. Tất cả nguồn phát thải này có thể được giảm đáng kể, thậm "
      "chí loại bỏ, thông qua thiết kế thiết bị phù hợp, thay thế bằng bộ truyền động điện, hoặc "
      "cải tiến thiết kế đệm. Một yếu tố hỗ trợ khác cho việc giảm đáng kể phát thải khí nhà kính "
      "là thiết kế mới trong truyền động van cho phép thay van dùng khí tự nhiên bằng các giải "
      "pháp phát thải thấp, thậm chí không phát thải. Thường được bán dạng bộ nâng cấp cải tạo, "
      "các bản nâng cấp này giảm mạnh phát thải methane và khí nhà kính. Bổ sung vào đó, một số "
      "nhà cung cấp tự động hóa đưa ra nhiều lựa chọn phát thải thấp cho thiết bị dùng khí tự "
      "nhiên, cũng như các giải pháp điện công suất rất thấp có thể chạy bằng điện từ hệ thống "
      "mặt trời nhỏ. Trong nhiều trường hợp, khoản tiết kiệm từ giảm phát thải methane, giảm yêu "
      "cầu thử nghiệm và tăng sản lượng khí tự nhiên chính là trả tiền cho việc nâng cấp thiết "
      "bị. Các loại thiết bị này thường đáp ứng các quy định nghiêm ngặt về phát thải methane do "
      "chính quyền địa phương áp đặt.",
      "Also, most control valves and/or pumps in chemical service tend to emit pollutants through "
      "packing and seal leaks. All these emissions sources can be substantially curtailed and even "
      "eliminated through proper equipment design, replacement with electric actuators, or "
      "improved packing designs. Another enabler of significant greenhouse gas emissions reduction "
      "are new designs in valve actuation that allow natural gas-actuated valves to be replaced "
      "with low and even zero-emissions alternatives. Often sold as retrofit kits, these upgrades "
      "provide dramatic reduction in methane and greenhouse gas emissions. Additionally, some "
      "automation suppliers offer a variety of low-bleed alternatives for natural gas-powered "
      "instrumentation, as well as very low power electrical alternatives, which can run on the "
      "power provided by small solar systems. In many cases the savings generated from the reduced "
      "methane emissions, reduced testing requirements, and additional natural gas production, "
      "pay for the instrument upgrade. These equipment types often meet stringent methane "
      "emissions regulations imposed by local governments.")

    # ------------------------------------------------------------ 11.10
    H("11.10 Tối đa hóa ESG thông qua hợp tác",
      "11.10 Maximizing ESG through Collaboration")
    P("Dù cả ngành dầu khí lẫn nhà cung cấp tự động hóa đều đang đạt được bước tiến đáng kể hướng "
      "tới mục tiêu môi trường của mình, tiến bộ tốt nhất thường đến từ sự hợp tác giữa hai nhóm "
      "này. Điều này đã đang diễn ra ở một số lĩnh vực, với các chuyên gia dầu khí làm việc cùng "
      "các nhà dẫn đầu về tự động hóa để giải quyết những thách thức cấp bách nhất bằng cách "
      "thiết kế phương pháp sáng tạo cho các vấn đề ESG.",
      "While both oil and gas industry and automation suppliers are making significant strides "
      "towards achieving their environmental goals, best progress often results from a "
      "collaboration between these two groups. This is already happening in some areas, with oil "
      "and gas specialists working with automation leaders to address the most pressing challenges "
      "by designing innovative methods to address ESG issues.")
    P("Một lĩnh vực hợp tác khác nằm ở quan hệ đối tác chung giữa các nhà dẫn đầu về tự động hóa "
      "và các trường đại học. Nhà cung cấp tự động hóa thường xuyên tài trợ diễn đàn bền vững, "
      "trao tài trợ và học bổng để thúc đẩy nghiên cứu trong nhiều lĩnh vực môi trường khác nhau. "
      "Những nỗ lực này thường dẫn đến thế hệ thiết bị đo và quy trình hóa học tiếp theo, mang "
      "lại cải thiện đáng kể cho môi trường.",
      "Another area of collaboration can be found in joint partnerships between automation leaders "
      "and universities. Automation suppliers routinely fund sustainability forums, award grants, "
      "and provide scholarships to further research in a variety of environmental fields. These "
      "efforts often result in next generation instrumentation and chemical processes, yielding "
      "significant environmental improvements.")
    P("Kết quả thành công nhất cho hành tinh của chúng ta đến từ sự hợp tác giữa các ngành công "
      "nghiệp. Những nỗ lực hợp tác dạng này đã đang được tiến hành, với lợi ích đang được hiện "
      "thực hóa và còn nhiều hơn nữa sẽ đến trong tương lai gần. Các cải thiện mang lại lợi ích "
      "ngay lập tức cho xã hội và môi trường, nhưng cũng cho phép công ty xác định vai trò của "
      "mình và lựa chọn con đường tốt nhất để đạt mục tiêu ESG.",
      "The most successful outcome for our planet results from collaboration between industries. "
      "These types of collaborative efforts are already underway, with benefits being realized "
      "now, and more to come soon. Improvements immediately benefit society and the environment, "
      "but they also allow a company to define its role and choose the best path forward to meet "
      "ESG goals.")

    # ------------------------------------------------------------ 11.11
    H("11.11 Kết luận", "11.11 Conclusion")
    P("Áp lực công chúng ngày càng tăng, các quy định môi trường nghiêm ngặt và nỗ lực hướng tới "
      "bền vững và phi carbon hóa đã đặt ra yêu cầu rất lớn cho hầu hết các ngành trong việc xác "
      "định và xây dựng lộ trình phi carbon hóa dẫn đến phát thải carbon ròng bằng không vào năm "
      "2050. Những nỗ lực này sẽ giúp đạt được mục tiêu đã thỏa thuận quốc tế là hạn chế mức nóng "
      "lên toàn cầu tối đa 1.5C so với thời kỳ tiền công nghiệp.",
      "Increasing public pressure, stringent environmental regulations, and efforts towards "
      "sustainability and decarbonization has placed immense demand on most industries to identify "
      "and develop decarbonization pathways that will lead to total net-zero carbon emissions by "
      "2050. These efforts will help meet the internationally agreed goal of limiting global "
      "climate warming to a maximum of 1.5C versus the preindustrial period.")

    # ------------------------------------------------------------ 11.12
    H("11.12 Các thuật ngữ thường dùng về tính bền vững",
      "11.12 Commonly Used Terms in Sustainability")
    B(["Trung hòa carbon nghĩa là bất kỳ CO2 nào thải vào khí quyển từ hoạt động của công ty được "
       "cân bằng bằng một lượng tương đương được loại bỏ.",
       "Phát thải carbon ròng bằng không nghĩa là một hoạt động thải phát thải carbon ròng bằng "
       "không vào khí quyển.",
       "Tổng phát thải ròng bằng không = Phát thải ròng bằng không",
       "Trung hòa carbon và phát thải ròng bằng không là hai thuật ngữ tương tự. Trong cả hai "
       "trường hợp, công ty đều nỗ lực giảm và cân bằng dấu vết carbon của mình. Khi trung hòa "
       "carbon đề cập đến việc cân bằng lượng phát thải carbon, thì phát thải carbon ròng bằng "
       "không có nghĩa là không có carbon nào được thải ra ngay từ đầu, do đó không cần thu giữ "
       "hay bù đắp carbon."],
      ["Carbon neutral means that any CO2 released into the atmosphere from a company's activities "
       "is balanced by an equivalent amount being removed.",
       "Net-zero carbon emissions mean that an activity releases net-zero carbon emissions into the "
       "atmosphere.",
       "Total Net-Zero = Net Zero",
       "Carbon-neutral and net-zero are two similar terms. In both cases, companies are working to "
       "reduce and balance their carbon footprint. When carbon-neutral refers to balancing out the "
       "amount of carbon emissions, net-zero carbon means no carbon was emitted from the get-go, "
       "so no carbon needs to be captured or offset."])

    # ------------------------------------------------------------ source notes
    H("Ghi chú về nguồn", "Source notes", h3)
    N(source_notes("vi"), source_notes("en"))
    P("Chương 11 chiếm tr. 240–249 của bản in (10 trang) trong Emerson, Control Valve Handbook, "
      "ấn bản 6 (2020). Nội dung gồm mười hai mục 11.1–11.12, từ tính bền vững, hiệu quả năng "
      "lượng, phi carbon hóa và ba phạm vi phát thải khí nhà kính đến ESG, hợp tác và bảng thuật "
      "ngữ. Ba hình được vẽ lại dạng vector và đặt theo thứ tự số tại vị trí văn bản hợp lý.",
      "Chapter 11 occupies printed pp. 240-249 (10 pages) of Emerson, Control Valve Handbook, 6th "
      "edition (2020). It contains twelve sections, 11.1-11.12, from sustainability, energy "
      "efficiency and decarbonization and the three greenhouse gas emission scopes to ESG, "
      "collaboration, and a glossary of terms. The three numbered figures are redrawn as vectors "
      "and placed in numbered order at their logical prose points.")
    P("<i>Đây là bản dịch không chính thức, dùng cho mục đích học tập. Nội dung gốc © 2020 Emerson "
      "Flow Controls.</i>",
      "<i>This is an unofficial translation for study purposes. Original content © 2020 Emerson "
      "Flow Controls.</i>")
    return "".join(b)


def body_vi():
    return _body("vi")


def body_en():
    return _body("en")
