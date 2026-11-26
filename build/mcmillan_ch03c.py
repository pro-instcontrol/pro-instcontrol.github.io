# -*- coding: utf-8 -*-
"""Chapter 3, module C - bilingual reader (EN/VI).

Alan McMillan, *Electrical Installations in Hazardous Areas*
(Butterworth-Heinemann, 1998), printed pp. 67-72 (PDF pp. 88-93).

Covers the surviving tail of Section 3.3.5 (moving seals), Section 3.4
and Sections 3.4.1-3.4.3 (fixed roof vented tank, floating roof tank and
tanks holding gas, vapour or liquefied vapours). Figures 3.9-3.11 are
drawn in mcmillanfig03_b; they are displayed here with sequential ids 6-8.

Module B already carries the explicit source-gap note for the eight
missing pages; this module only adds a one-sentence bridge and does not
repeat it. Tables 3.9/3.10 are named but their data lie in the missing
pages, so no rows are fabricated. The integration module owns PAGES_SRC,
refs, note_terms, the end note, the copyright line and the h2 heading.

This is an unofficial study translation. The source PDF is not republished.
"""
from mcmillan_common import h3, h4, p, note, fig

import mcmillanfig03_b as FB


def body_vi():
    b = []
    b.append(note("Mục 3.3.5 được tiếp tục ở đây, sau các trang bị thiếu, "
                  "với phần văn bản còn lại về phát thải từ phớt chuyển động."))
    b.append(h4("3.3.5 Phát thải từ phớt chuyển động",
                "3.3.5 Releases from moving seals"))
    b.append(p("<b>Bơm có phớt nhồi hoặc phớt cơ khí.</b> Khi phát thải là "
               "khí nén, hiện diện Vùng 1 với bán kính 1 m. Vùng 2 nên lấy "
               "theo Bảng 3.2 đối với gioăng gia cố xoắn ốc, đồng thời phải "
               "tính đến ảnh hưởng của mặt đất gần chỗ rò (xem Hình 3.3 và "
               "Hình 3.4)."))
    b.append(p("Mặc dù có thể dùng phớt nhồi cho tất cả các tình huống trên, "
               "nên dùng phớt cơ khí, đặc biệt với khí và chất lỏng có điểm "
               "sôi ở áp suất khí quyển đã bị vượt, vì hiệu năng chống mài "
               "mòn tốt hơn. Cũng nên dùng bạc tiết lưu (throttle bush) trong "
               "các trường hợp này để tăng độ tin cậy về tốc độ rò tối đa. "
               "Khi có sự tập trung đông đảo bơm và máy nén quay, phải nhận "
               "diện tình huống này và xử lý các khu vực nguy hiểm như đối "
               "với van."))
    b.append(p("<b>Phớt chuyển động tịnh tiến.</b> Máy nén và bơm tịnh tiến rò "
               "quanh piston vào hộp trục khuỷu hoặc buồng sau piston. Nếu "
               "hộp trục khuỷu được thông gió, khu vực nguy hiểm xuất hiện "
               "tại lối thoát gió, có thể ở xa điểm nén, nên một khu vực nguy "
               "hiểm khác có thể hình thành ở nơi khác. Trong vận hành bình "
               "thường, Vùng 1 bán kính 1 m quanh điểm phát thải ra khí quyển "
               "là đủ. Trong trường hợp bất thường, phát thải cả tại điểm xả "
               "khí bình thường lẫn ngay tại phớt nên xử lý như đối với "
               "gioăng gia cố xoắn ốc (Bảng 3.2); do chế độ làm việc của máy "
               "nén, điều này có thể tạo ra các khu vực nguy hiểm đáng kể."))
    b.append(h3("3.4 Các tình huống thực tế khác có thông gió tốt",
                "3.4 Other practical well-ventilated situations"))
    b.append(p("Các mục trước đã thảo luận cách vật liệu dễ cháy rò ra từ các "
               "nguồn rò kinh điển hơn, chẳng hạn như mặt bích đường ống và "
               "phớt bơm/máy nén, nhưng nhiều tình huống cụ thể đòi hỏi xem "
               "xét riêng."))
    b.append(h4("3.4.1 Bể chứa mái cố định thông hơi",
                "3.4.1 The fixed roof vented stock tank"))
    b.append(p("Loại bể này rất phổ biến trong các nhà máy công nghệ để chứa "
               "vật liệu dễ cháy thường ở dạng lỏng. Hầu hết đặt ở khu vực "
               "ngoài trời thông gió tốt, có ống thông hơi tự do để hơi thoát "
               "ra khi nạp và không khí vào khi xả. Tuy nhiên, khi phơi nắng "
               "trực tiếp có thể xảy ra hấp thụ nhiệt mặt trời, đặc biệt "
               "trong không gian hơi, và nhiệt độ có thể vượt quá mức môi "
               "trường điển hình tối đa 32 °C. Mức hấp thụ này không được "
               "quy định trực tiếp, nhưng một quy chuẩn của công ty đưa ra "
               "47.5 °C cho bể nhỏ, và tài liệu HSE HS(G)50 (1996) định "
               "nghĩa chất lỏng dễ cháy là chất có điểm cháy đến 55 °C. Nên "
               "thận trọng lấy giá trị sau làm cơ sở thảo luận ở đây và "
               "không chứa trong các bể này chất lỏng nào có điểm sôi dưới "
               "55 °C."))
    b.append(p("Các bể này thường có bể chắn (bund) để chứa chất lỏng tràn do "
               "quá đầy hoặc rò ràng lớn, và bể chắn quyết định kích thước "
               "vũng chất lỏng dễ cháy (trừ khi một bể chắn chung bao quanh "
               "nhiều bể, khi đó áp dụng cách xác định kích thước vũng thông "
               "thường). Để bể chắn có hiệu quả, điểm gần nhất của nó luôn "
               "phải cách bể hơn 1 m để chất lỏng rò từ bể luôn chảy vào đó; "
               "bể chắn cũng phải chứa được toàn bộ lượng chất lỏng trong "
               "bể với hệ số an toàn khoảng 1.1."))
    b.append(p("Có hai tình huống bình thường cần xét — bên trong bể và bên "
               "ngoài bể trong khi nạp và xả — cùng với trường hợp bất "
               "thường là quá đầy đưa chất lỏng dễ cháy vào bể chắn và có "
               "thể kèm rò tại mặt bích gần đó. Với các giả định này, cách "
               "phân loại bể và khu vực xung quanh được thể hiện trong Hình "
               "3.9."))
    b.append(fig(6, FB.fig_f309()))
    b.append(p("<b>Vùng 0.</b> Do chu kỳ xả liên tục hút không khí vào không "
               "gian hơi và trộn với hơi, rất có thể tồn tại bầu khí nổ ở "
               "một vị trí nào đó trong không gian này. Vì không xác định "
               "được vị trí cụ thể, toàn bộ không gian hơi phải được xếp "
               "vào Vùng 0."))
    b.append(p("<b>Vùng 1.</b> Chu kỳ nạp thải hỗn hợp hơi dễ cháy và không "
               "khí ra khỏi ống thông hơi; hơi này gần như chắc chắn nặng "
               "hơn không khí nên bầu khí nổ hình thành quanh miệng thông "
               "hơi và có xu hướng đi xuống, lan ra theo mặt mái bể, có thể "
               "vượt qua cả mép bể. Vũng lỏng trong bể chắn, trong trường "
               "hợp bất thường, bay hơi và nếu bể chắn không quá rộng và "
               "nông thì cản trở sự phân tán, nên bên trong bể chắn cũng "
               "rất có thể là Vùng 1."))
    b.append(p("<b>Vùng 2.</b> Nếu bể bị quá đầy, chất lỏng dễ cháy tràn qua "
               "ống thông hơi, chảy xuống thành bể và tụ lại trong bể chắn. "
               "Sự bay hơi từ mặt ngoài bể và từ mặt vũng tạo Vùng 2 quanh "
               "bể và vượt ra ngoài bờ bể chắn. Rò rỉ từ bể và đường ống "
               "liên quan cũng tạo Vùng 2 nhưng nằm gọn trong vùng do quá "
               "đầy gây ra."))
    b.append(p("<b>Hạn chế và các lưu ý khác.</b> Khi xây dựng Hình 3.9 đã "
               "dùng bể dung tích khoảng 250 m³, không xét có bơm hoặc thiết "
               "bị tạo áp nào trong bể chắn. Hệ thống thoát nước của bể chắn "
               "cũng không được xét, giả định không truyền chất lỏng hoặc "
               "hơi dễ cháy ra ngoài; nếu thiết kế không đạt thì phải tính "
               "đến khả năng này. Khi nắng làm chất lỏng gần đến điểm sôi, "
               "nên xem xét che bể để hết nắng trực tiếp; khi đó nhiệt độ tối đa "
               "bên trong giảm về khoảng 32 °C. Nếu mái che phẳng, toàn bộ "
               "không gian bên dưới trở thành Vùng 1 cộng thêm 1 m theo "
               "phương ngang từ mép mái và khoảng cách tương tự tính từ "
               "bất kỳ lỗ thông hơi nào. Không nên dùng mái che có thành "
               "bên, vì có thể làm xấu đáng kể thông gió giữa mái bể và mái "
               "che, tệ nhất là tạo Vùng 0 trong khoảng đó, đặc biệt khi "
               "không có lỗ thông hơi trên mái để tạo hiệu ứng ống khói."))
    b.append(h4("3.4.2 Bể chứa mái nổi",
                "3.4.2 The floating roof tank"))
    b.append(p("Ở loại bể này mái được chất lỏng nâng và đi lên xuống theo "
               "mức chất lỏng. Có một phớt giữa mái chuyển động và thành bể, "
               "hơi chỉ hiện diện khi chính hơi hoặc một lượng nhỏ chất "
               "lỏng đi qua phớt đó. Đây là tình huống 'vận hành bình "
               "thường' hoặc, nếu lượng chất lỏng qua phớt đủ tạo bầu khí "
               "nổ, là tình huống liên tục. Thành bể phía trên mái cũng có "
               "thể cản phân tán và làm bầu khí nổ tồn lâu hơn; hiệu ứng này "
               "tăng lên nếu lắp mái che. Kết quả được thể hiện trong Hình "
               "3.10 và về cơ bản như sau."))
    b.append(fig(7, FB.fig_f310()))
    b.append(p("<b>Vùng 0.</b> Không tồn tại bên trong bể, khác với trường "
               "hợp mái cố định, vì mái tiếp xúc trực tiếp với chất lỏng. Với "
               "điều kiện không gian phía trên mái không bị cản trở, hơi dễ "
               "cháy tích tụ không đủ để tạo Vùng 0, nên bể mái nổi có lợi "
               "thế hơn bể mái cố định."))
    b.append(p("<b>Vùng 1.</b> Bên trong bể phía trên mái là Vùng 1, kéo dài "
               "1.5 m lên phía trên và sang hai bên mép bể. Vì hơi thường "
               "nặng hơn không khí, Vùng 1 được dự kiến kéo dài thêm xuống "
               "dọc thành bể. Trong trường hợp bất thường bể hoạt động như "
               "bể mái cố định: chất lỏng tràn vào bể chắn, vũng hình thành "
               "và không gian hơi phía trên vũng chứa bầu khí nổ. Do thành "
               "bể chắn cản thông gió, sự tồn lưu trong bể chắn khiến "
               "không gian hơi bên trong là Vùng 1."))
    b.append(p("<b>Vùng 2.</b> Như ở bể mái cố định, khả năng bất thường là "
               "tràn chất lỏng vào bể chắn, nên có Vùng 2 kéo dài 1.5 m từ "
               "đỉnh bể và quanh thành bể; vùng này không thể hiện riêng vì "
               "trùng với Vùng 1 nên bị che lấp. Ngoài ra còn có Vùng 2 kéo "
               "dài 2.5 m theo phương thẳng đứng và nằm ngang tính từ bờ bể "
               "chắn, như trường hợp bể mái cố định."))
    b.append(p("<b>Hạn chế và các lưu ý khác.</b> Tương tự bể mái cố định, đã "
               "xét bể dung tích khoảng 250 m³, không có bơm hay thiết bị "
               "tương tự trong bể chắn. Lại giả định hệ thống thoát nước "
               "không truyền chất lỏng dễ cháy ra ngoài bể chắn. Ảnh hưởng "
               "của mái che cũng tương tự như ở bể mái cố định, nhưng do "
               "cấu tạo của bể mà khả năng có mái che ở đây lớn hơn."))
    b.append(h4("3.4.3 Bể chứa khí, hơi hoặc hơi đã hóa lỏng",
                "3.4.3 Tanks containing gas, vapour or liquefied vapours"))
    b.append(p("Các bể này thường được bịt kín vì khí, hơi hoặc chất lỏng "
               "nằm dưới áp suất. Rò từ chúng nên xử lý như rò từ mối nối "
               "đường ống và các mối nối tương tự, vì ngay cả chất lỏng thoát "
               "ra cũng hóa hơi rất nhanh. Tuy nhiên, các bể này có thể được "
               "bao quanh bằng bể chắn để xử lý phát thải khối lượng lớn; dù "
               "nằm ngoài phạm vi phân loại khu vực thông thường (ví dụ "
               "trường hợp thảm họa), vẫn cần tính đến. Nếu dùng bể chắn đó, "
               "dù phát thải là cấp thứ cấp (bất thường), bể chắn vẫn có thể "
               "tạo điều kiện cho bầu khí nổ tồn lưu bên trong, nên nội "
               "thất của chúng, như ở bể chứa chất lỏng, được coi là Vùng 1."))
    b.append(p("Đối với tích trữ áp suất thấp, chẳng hạn bể chứa khí "
               "(gasholder), thường dùng phớt nước. Khi đó phải xét khả năng "
               "khí thoát qua chất lỏng nếu áp suất bên trong bể quá cao, "
               "hoặc sự xả tại van xả áp được lắp để tránh quá áp. Trong "
               "những trường hợp này có thể dùng cách phân loại sau, được "
               "minh họa trong Hình 3.11. Không được có Vùng 0 bên trong "
               "cũng như gần bể chứa, vì điều đó tương đương với việc tích "
               "trữ và đưa một bầu khí nổ vào quy trình; hơn nữa, cách bố "
               "trí bịt bằng chất lỏng phải đạt điều kiện tương tự như ở bể "
               "mái nổi. Rất có thể phát thải hạn chế tại van xả áp xảy ra "
               "trong vận hành bình thường; phát thải giới hạn này tạo Vùng "
               "1 nhưng do áp suất rất thấp nên Vùng 1 có kích thước hạn "
               "chế. Mức 3 m được đề xuất là đủ cho trường hợp này."))
    b.append(fig(8, FB.fig_f311()))
    b.append(p("Trong trường hợp bất thường, quá áp do quá đầy bể gây phát "
               "thải lớn hơn đáng kể tại van xả áp và thêm phát thải tại "
               "phớt nước. Khu vực bị nhiễm khi đó lớn hơn, và người ta đề "
               "xuất cần có khu vực nguy hiểm 10 m tính từ cả van xả áp lẫn "
               "phớt nước."))
    b.append(p("<b>Hạn chế và các lưu ý khác.</b> Khi chọn các khu vực nguy "
               "hiểm trên, người ta giả định thông hơi bình thường qua một "
               "lỗ tiết diện khoảng 2 cm² ở 10⁴ N/m², với sự đi qua màng "
               "hoặc phớt nước của van xả áp chỉ là một phần. Trường hợp "
               "bất thường thì ngược lại, coi như đi qua hoàn toàn van xả "
               "áp, hoặc qua một phần đáng kể của phớt nước."))
    b.append(note("<b>Khoảng trống nguồn.</b> Bảng 3.9 và Bảng 3.10 chỉ được "
                  "nhắc tên ở đây: dữ liệu của hai bảng nằm trong các trang "
                  "bị thiếu, nên không có dòng dữ liệu nào được tái tạo."))
    return "".join(b)


def body_en():
    b = []
    b.append(note("Section 3.3.5 resumes here, beyond the missing pages, "
                  "with the surviving text on releases from moving seals."))
    b.append(h4("3.3.5 Releases from moving seals",
                "3.3.5 Releases from moving seals"))
    b.append(p("<b>Pump with packed gland or mechanical seal.</b> Where the "
               "leakage is of compressed gas, a Zone 1 of 1 m radius is "
               "present. Zone 2 should be taken from Table 3.2 for a "
               "spirally supported gasket, and account should also be taken "
               "of the proximity of the ground to the leak (see Figures 3.3 "
               "and 3.4)."))
    b.append(p("Although packed gland seals can be used in all of the "
               "situations above, mechanical seals are recommended, "
               "particularly for gases and liquids above their "
               "atmospheric-pressure boiling points, because of their "
               "better wear performance. Throttle bushes are also "
               "recommended in these cases to give added confidence in "
               "maximum leak rates. Where concentrations of rotating pumps "
               "and compressors are present, this situation must be "
               "identified and the hazardous areas treated as for valves."))
    b.append(p("<b>Moving reciprocating seals.</b> Reciprocating compressors "
               "and pumps leak around their pistons into a crankcase or the "
               "chamber behind the piston. If the crankcase is ventilated, "
               "the hazardous area appears at the ventilation exit, which "
               "may be some distance from the point of compression, so a "
               "further hazardous area may be created elsewhere. In normal "
               "operation a Zone 1 of 1 m radius around the point where the "
               "leakage reaches the atmosphere is sufficient. For abnormal "
               "circumstances, the release at both the normal exhaust point "
               "and local to the seal should be treated as for a spirally "
               "supported gasket (Table 3.2); because of compressor duty "
               "this can produce significant hazardous areas."))
    b.append(h3("3.4 Other practical well-ventilated situations",
                "3.4 Other practical well-ventilated situations"))
    b.append(p("The previous sections have discussed the performance of "
               "leaking flammable material from the more classic leak "
               "sources, such as pipe flanges and pump/compressor seals, but "
               "many particular situations require specific consideration."))
    b.append(h4("3.4.1 The fixed roof vented stock tank",
                "3.4.1 The fixed roof vented stock tank"))
    b.append(p("This type of tank is extremely common on process plant for "
               "storing flammable materials that are normally liquids. Most "
               "are in well-ventilated outdoor areas with free vents to let "
               "vapour escape during filling and air enter during emptying. "
               "In direct sunlight, however, solar gain can occur, especially "
               "in the vapour space, and temperatures above the typical "
               "ambient maximum of 32 °C can be reached. The extent of this "
               "gain is not specified directly, but one company code gives "
               "47.5 °C for small tanks, and the HSE booklet HS(G)50 (1996) "
               "defines flammable liquids as those with flashpoints up to "
               "55 °C. It is prudent to adopt the latter as the basis here "
               "and not to store any liquid with a boiling point below "
               "55 °C in such tanks."))
    b.append(p("Such tanks are normally bunded to contain spillages from "
               "gross overfilling or leakage, and the bunding determines "
               "the extent of the pool of flammable liquid (unless a single "
               "bund surrounds several tanks, in which case normal pool "
               "sizing applies). To be effective, the nearest point of the "
               "bund should always be more than 1 m from the tank so that "
               "liquid leaking from the tank falls into it; the bund should "
               "also hold the entire tank contents with a safety factor of "
               "about 1.1."))
    b.append(p("There are two normal situations to consider, inside the tank "
               "and outside it during filling and emptying, together with "
               "the abnormal case of overfilling that puts flammable liquid "
               "into the bund and may also involve flange leakage nearby. On "
               "these assumptions the classification of the tank and its "
               "surroundings is as shown in Figure 3.9."))
    b.append(fig(6, FB.fig_f309()))
    b.append(p("<b>Zone 0.</b> Because the emptying cycle constantly draws "
               "air into the vapour space and mixes it with vapour, an "
               "explosive atmosphere is likely to exist somewhere in that "
               "space. Since the actual part cannot be defined, the entire "
               "vapour space must be classified as Zone 0."))
    b.append(p("<b>Zone 1.</b> The filling cycle exhausts a mixture of "
               "flammable vapour and air from the vent; this vapour is "
               "almost certain to be heavier than air, so an explosive "
               "atmosphere forms around the vent and tends to travel "
               "downwards and outwards along the tank top, possibly "
               "overlapping the tank edges. In abnormal circumstances the "
               "liquid pool in the bund gives off vapour which, unless the "
               "bund is very large and shallow, is impeded from dispersing, "
               "so the interior of the bund is also likely to be Zone 1."))
    b.append(p("<b>Zone 2.</b> If the tank is overfilled, flammable liquid "
               "exits the vent, travels down the sides of the tank and "
               "collects in the bund. Vaporization from the outside of the "
               "tank and from the surface of the pool creates a Zone 2 "
               "around the tank and beyond the bund wall. Leakage from the "
               "tank and associated pipework also produces a Zone 2, but "
               "this is contained within the Zone 2 caused by overfilling."))
    b.append(p("<b>Limitations and other considerations.</b> In producing "
               "Figure 3.9, a tank of some 250 m³ capacity has been used and "
               "no pumps or other pressurizing devices have been considered "
               "as present within the bund. The water drainage facilities "
               "associated with the bund have also not been considered, as "
               "they are assumed not to transmit flammable liquid or vapour "
               "from the bund; their design should achieve this in any "
               "properly designed installation, but if it does not, such "
               "possibilities must be considered. Where solar gain brings "
               "the contained liquid near its boiling point, a cover should "
               "be considered to prevent direct sunlight; this removes "
               "solar gain and reduces internal maximum temperatures to "
               "around 32 °C. If the cover is flat, the area under it all "
               "becomes Zone 1 with a distance of 1 m laterally from the "
               "edge of the cover and a similar radial distance from any "
               "vents in its top. A cover with sides is not recommended, as "
               "it can severely affect ventilation between the tank top and "
               "the cover, at worst creating a Zone 0 in that space, "
               "particularly if there are no top vents to give a chimney "
               "effect."))
    b.append(h4("3.4.2 The floating roof tank",
                "3.4.2 The floating roof tank"))
    b.append(p("In these tanks the roof is supported by the liquid within "
               "the tank and moves up and down with its level. A seal is "
               "provided between the moving roof and the walls of the tank, "
               "and vapour can only be present where it, or small quantities "
               "of liquid, pass that seal. This is either a situation of "
               "normal operation or, where the amount of liquid passing the "
               "seal normally gives sufficient vapour to create an "
               "explosive atmosphere, a continuous situation. The walls of "
               "the tank above the roof may also restrict dispersion and "
               "cause the explosive atmosphere to persist, an effect "
               "exacerbated where a cover is fitted. The result is shown in "
               "Figure 3.10 and is basically as follows."))
    b.append(fig(7, FB.fig_f310()))
    b.append(p("<b>Zone 0.</b> This does not exist within the tank, unlike "
               "the fixed roof case, as the roof is in intimate contact "
               "with the stored liquid. Provided the space in the tank "
               "above the roof is unimpeded, the retention of flammable "
               "vapour is not sufficient to create a Zone 0 in that space, "
               "so some advantage over fixed roof tanks is apparent."))
    b.append(p("<b>Zone 1.</b> The interior of the tank above the roof is "
               "Zone 1, extending 1.5 m above and laterally from the edges "
               "of the tank. As the vapour is generally heavier than air, "
               "Zone 1 can be expected to extend further down the sides of "
               "the tank. In abnormal circumstances the tank behaves like a "
               "fixed roof tank: liquid overflows into the bund, a pool "
               "forms and the vapour space above it contains an explosive "
               "atmosphere. Because the bund wall is likely to interfere "
               "with ventilation, there will be persistence within the "
               "bund and its interior vapour space is Zone 1."))
    b.append(p("<b>Zone 2.</b> As for the fixed roof tank there is the "
               "abnormal possibility of overflow into the bund, so a Zone 2 "
               "of 1.5 m from the top of the tank and around its sides will "
               "be present; this will not show where Zone 1 exists, as it "
               "has a similar extent and is thus masked. A Zone 2 will also "
               "exist from the bund limits for a vertical and horizontal "
               "distance of 2.5 m, as for the fixed roof tank."))
    b.append(p("<b>Limitations and other considerations.</b> As for the "
               "fixed roof tank, a tank of some 250 m³ capacity has been "
               "considered with no pumps or similar equipment contained "
               "within the bund. Drainage devices are again assumed not to "
               "transmit flammable liquid out of the bund. The effects of a "
               "cover will also be similar to those for the fixed roof tank, "
               "although a cover is more likely here in view of the "
               "construction of the tank."))
    b.append(h4("3.4.3 Tanks containing gas, vapour or liquefied vapours",
                "3.4.3 Tanks containing gas, vapour or liquefied vapours"))
    b.append(p("These tanks are normally sealed as the gas, vapour or liquid "
               "will be under pressure. Leaks from them should be treated as "
               "for leaks from pipe and similar joints, since even if it is "
               "liquid that is released it will rapidly vaporize. Such tanks "
               "may, however, be bunded to take care of massive releases "
               "which, although outside the scope of area classification "
               "(for example catastrophic), may need to be provided for. If "
               "such bunds are used then, even if the releases are secondary "
               "grade (abnormal), the bunds may create conditions in which "
               "the explosive atmosphere persists within them, and their "
               "interiors, as for liquid storage tanks, should be considered "
               "as Zone 1."))
    b.append(p("For low pressure storage, such as gasholders, water seals "
               "are often used. Where this is the case, the possibility of "
               "gas exiting through the liquid must be considered if the "
               "pressure inside the holder is too high, or venting at "
               "pressure relief valves provided to prevent overpressurizing. "
               "In such circumstances the following classification may be "
               "appropriate and is shown diagrammatically in Figure 3.11. "
               "There should be no Zone 0 either inside or in the proximity "
               "of the storage holder, as this would be tantamount to "
               "storing and delivering an explosive atmosphere to a process; "
               "in any event the liquid sealing arrangements should achieve "
               "the same conditions as in a floating roof tank. Release at "
               "pressure relief valves to a limited extent is highly likely "
               "in normal operation; this limited release gives rise to a "
               "Zone 1, but as the pressure will be very low the Zone 1 will "
               "be of limited size. A figure of 3 m is suggested as adequate "
               "to cover this eventuality."))
    b.append(fig(8, FB.fig_f311()))
    b.append(p("In abnormal circumstances, overpressurizing due to "
               "overfilling the tank will cause significantly more release "
               "at the pressure relief valve and, in addition, releases at "
               "the water seal or seals. The area contaminated in these "
               "circumstances will be larger, and a hazardous area of 10 m "
               "from both of these leakage points is suggested as necessary "
               "to cover this eventuality."))
    b.append(p("<b>Limitations and other considerations.</b> In selecting "
               "the above hazardous areas, normal venting is assumed to be "
               "from an orifice of around 2 cm² at 10⁴ N/m², the passage "
               "through the diaphragm or water seal of the pressure relief "
               "valve being considered partial. This is not so in abnormal "
               "situations, where full passage through the pressure relief "
               "valve, or a significant part of the water seal, is "
               "considered."))
    b.append(note("<b>Source gap.</b> Tables 3.9 and 3.10 are named here "
                  "only: their data lie in the missing pages, so no rows "
                  "are reproduced."))
    return "".join(b)
