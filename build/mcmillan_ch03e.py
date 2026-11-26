# -*- coding: utf-8 -*-
"""Chapter 3, module E - bilingual reader (EN/VI).

Alan McMillan, *Electrical Installations in Hazardous Areas*
(Butterworth-Heinemann, 1998), printed pp. 80-86 (PDF pp. 101-107).

Covers Sections 3.4.9-3.4.11: sampling points, walls and apertures, and
vents. Section 3.4.8 was completed in module D and is not repeated here.
Figures 3.15-3.19 are drawn in mcmillanfig03_d and displayed here with
sequential ids 12-16, following the ids 9-11 used by module D.

Tables 3.2 and 3.7 are named but not tabulated: their data lie outside
this span, in the eight missing pages (PDF pp. 80-87). No rows are invented.
Page-level data and headings are owned by the integration module; this file
defines only the two body functions.

This is an unofficial study translation. The source PDF is not republished.
"""
from mcmillan_common import h4, p, note, fig

import mcmillanfig03_d as FD


def body_vi():
    b = []
    b.append(h4("3.4.9 Điểm lấy mẫu", "3.4.9 Sampling points"))
    b.append(p("Vấn đề với các điểm lấy mẫu là hầu hết được thao tác thủ công. Ngoài "
               "sự khôn ngoan đáng ngờ của việc cố ý tạo ra một khu vực nguy hiểm đáng kể "
               "bằng một thao tác thường quy, còn có vấn đề là nhân viên lấy mẫu sẽ nằm "
               "trong khu vực nguy hiểm tại thời điểm có mặt vật liệu dễ cháy. Vì đa số "
               "vật liệu dễ cháy cũng độc hại (xem HSE Guidance Note EH 40), đây không phải "
               "tình huống có thể chấp nhận. Do đó, bố trí lấy mẫu thường được thiết kế cẩn "
               "thận để giảm thiểu khu vực nguy hiểm hình thành trong vận hành bình thường, "
               "để khu vực nguy hiểm đáng kể chỉ xuất hiện trong vận hành bất thường."))
    b.append(p("<b>Lấy mẫu chất lỏng.</b> Bất kỳ điểm lấy mẫu chất lỏng nào cũng phải được "
               "bố trí sao cho mọi sự cố tràn trong khi lấy mẫu bình thường được loại bỏ "
               "ngay. Muốn vậy, hệ thống lấy mẫu cần có các đặc điểm như hệ thống minh họa "
               "trong Hình 3.15: phễu hứng (tundish) hoặc bộ phận tiếp nhận bên dưới điểm "
               "lấy mẫu phải chuyển lượng chất tràn sang một hệ thống lưu trữ kín an toàn "
               "để xử lý. Đối với chất lỏng có độ bay hơi thấp (được đề xuất là chất có "
               "điểm sôi ở áp suất khí quyển ít nhất gấp bốn lần nhiệt độ môi trường), "
               "thông thường chỉ cần dùng trọng lực là đủ để hứng chất tràn trong phễu; "
               "trong các trường hợp khác, cần có một dạng hệ thống hút để dẫn chất tràn "
               "vào phễu."))
    b.append(fig(12, FD.fig_f315()))
    b.append(p("Nếu dùng các biện pháp đó, lượng vật liệu dễ cháy thoát vào không khí quanh "
               "điểm lấy mẫu trong vận hành bình thường là rất nhỏ và sẽ không có Vùng 1 "
               "đáng kể. Tuy nhiên, vẫn còn khả năng phát thải đáng kể trong vận hành bất "
               "thường, chẳng hạn hỏng van lấy mẫu làm thoát ra nhiều chất lỏng hơn mức "
               "phễu hứng có thể xử lý, hoặc bản thân phễu bị tắc. Trong cả hai trường hợp "
               "sẽ có rò rỉ đáng kể chất lỏng dễ cháy và có thể bắn tung quanh điểm lấy mẫu. "
               "Tình huống này tạo ra một Vùng 2 nhỏ quanh điểm lấy mẫu cùng một vũng chất "
               "lỏng bên dưới; vũng này lớn dần cho đến khi được chứa giới hạn về mặt vật "
               "lý hoặc tốc độ bay hơi cân bằng tốc độ rò rỉ, rồi tạo ra khu vực nguy hiểm "
               "theo Bảng 3.7. Kết quả cho trong Hình 3.15 như sau: không có Vùng 0 và Vùng "
               "1; Vùng 2 gồm một hình cầu bán kính 1 m quanh điểm lấy mẫu cộng với vũng "
               "chất lỏng và khu vực nguy hiểm bao quanh nó. Trong Hình 3.15, a = 1 m, "
               "b = vũng chất lỏng (pool), c = Bảng 3.7."))
    b.append(p("Khi vật liệu dễ cháy không độc hại, có thể dùng bố trí đơn giản hơn, nhưng "
               "không khuyến khích vì chúng có khả năng tạo ra các khu vực nguy hiểm lớn "
               "hơn, mà lý do biện minh cho điều đó rất đáng ngờ khi các bố trí nêu trên "
               "dễ dàng áp dụng. Thông tin chi tiết về độc tính của các vật liệu thông "
               "thường được cho trong HSE Guidance Note EH 40."))
    b.append(p("<b>Lấy mẫu khí và hơi.</b> Việc lấy mẫu khí, hơi và hơi hóa lỏng dưới áp "
               "suất có thể tạo ra khu vực nguy hiểm có quy mô đáng kể và không được phép. "
               "Cần dùng hệ thống lấy mẫu nội tuyến kín (closed in-line) như minh họa trong "
               "Hình 3.16; trong một số trường hợp, phải cho bay hết không gian giữa chai "
               "mẫu và các van cố định trước khi tháo chai mẫu. Điều này nhiều khả năng chỉ "
               "xảy ra với khí hóa lỏng, vì ở các trường hợp khác lượng vật liệu dễ cháy "
               "tích tụ trong khoảng đó sẽ nhỏ nếu hệ thống được thiết kế đúng. Mục tiêu "
               "lại là loại bỏ hiệu quả mọi Vùng 1 để khu vực nguy hiểm chỉ hiện diện trong "
               "vận hành bất thường. Các tình huống bất thường gồm hỏng phớt van, hỏng mối "
               "nối đường ống và kết nối sai bởi nhân viên — trường hợp sau được kỳ vọng "
               "sẽ được sửa ngay vì nhân viên lấy mẫu có mặt tại chỗ."))
    b.append(fig(13, FD.fig_f316()))
    b.append(p("Vì vậy, khu vực nguy hiểm nhiều khả năng nhất do hỏng mối nối đường ống hoặc "
               "hỏng van, cả hai đều được đề cập trong 'sections 3.5.1 and 3.5.2' và trong "
               "Bảng 3.2 (cách đánh số này không tồn tại trong văn bản in — xem ghi chú). "
               "Kết quả như sau: không có Vùng 0 và Vùng 1; Vùng 2 gồm một khu vực theo dòng "
               "3 của Bảng 3.2 quanh thân van và một khu vực theo cột thích hợp của Bảng "
               "3.2 quanh mỗi mối nối, như trong Hình 3.16."))
    b.append(note("<b>Ghi chú của Hình 3.16 (nguyên văn, kể cả lỗi in).</b> 'Note: Release "
                  "from value stems assumed less than joints. If this is not so the "
                  "hazardous area should be adjusted to take account of hazardous areas "
                  "from column 3 of Table 3.2' — 'value stems' là lỗi in của 'valve stems' "
                  "và được giữ lại. Bảng 3.2 chỉ được nhắc tên; số liệu của bảng không nằm "
                  "trong đoạn nguồn này nên không có dòng nào được tạo ra."))

    b.append(h4("3.4.10 Tường và lỗ hổng", "3.4.10 Walls and apertures"))
    b.append(p("Khi phạm vi của khu vực nguy hiểm bị giới hạn bởi một bức tường có cửa, thì "
               "về phía không nguy hiểm của bức tường, cửa đó trở thành một nguồn phát thải "
               "và tạo ra khu vực nguy hiểm như minh họa trong Hình 3.17. Tương tự, khi "
               "bức tường ngắn, khu vực nguy hiểm sẽ lan qua quanh nó như trong Hình 3.18. "
               "Trong cả hai trường hợp, độ lan đó dựa trên phạm vi ban đầu của khu vực "
               "nguy hiểm và khoảng cách giữa nguồn nguy hiểm với bức tường."))
    b.append(fig(14, FD.fig_f317()))
    b.append(fig(15, FD.fig_f318()))
    b.append(p("Ký hiệu dùng cho cả hai hình như sau: a = khoảng cách từ tường đến nguồn "
               "nguy hiểm; b = phạm vi của khu vực nguy hiểm nếu bỏ qua bức tường; "
               "c = b − a, tức phần kéo dài ở phía bên kia tường. Phần kéo dài này được "
               "lấy bằng phạm vi nguyên thủy trừ đi khoảng cách từ nguồn đến tường."))

    b.append(h4("3.4.11 Miệng thông hơi", "3.4.11 Vents"))
    b.append(p("Miệng thông hơi thường chỉ hoạt động trong hoàn cảnh bất thường, chẳng hạn "
               "van xả áp mở ra hoặc đĩa vỡ bị vỡ. Trong những trường hợp đó, một lượng "
               "tương đối lớn khí hoặc hơi dễ cháy được xì trực tiếp ra khí quyển xung "
               "quanh qua miệng thông hơi hoặc tháp đốt. Phần này chỉ đề cập đến các tình "
               "huống xì trực tiếp đó; trong các trường hợp khác, biện pháp chứa thứ cấp "
               "thường là chuẩn mực và được xử lý theo các phần trước của chương này. Người "
               "ta giả định ngọn đốt không bị đánh lửa, vì khả năng đó vẫn tồn tại."))
    b.append(p("Với đĩa vỡ sẽ không có phát thải vật liệu dễ cháy trong vận hành bình "
               "thường, nhưng với van xả áp phải coi là có thể có rò nhẹ qua bề mặt đế van "
               "(không tính thân van điều khiển, phải xử lý riêng). Trong một trường hợp có "
               "thể có Vùng 1 tại miệng thông hơi, trong trường hợp kia thì không. Khi van "
               "mở hoặc đĩa vỡ vỡ, cả hai đều có dòng chảy đáng kể nhưng chỉ trong vận hành "
               "bất thường. Lượng rò nhỏ do rò qua đế van sẽ trôi từ miệng ống ra, trong khi "
               "lượng thoát ra do van hoạt động hoặc đĩa vỡ vỡ là dòng chảy nhanh. Vì vậy, "
               "khu vực nguy hiểm do trường hợp trước là một hình cầu nhỏ vì sự trôi đó bị "
               "gió phân tán, còn trường hợp sau là một chùm (plume) vì độ nhiễu loạn của "
               "tia phun trộn lẫn. Điều này cho ra sự phân bố khu vực nguy hiểm khá bất "
               "thường như Hình 3.19, trong đó Vùng 2 được xét đến sự bóp méo của chùm do "
               "gió."))
    b.append(p("Kết quả như sau: <b>Vùng 0</b> nằm bên trong ống thông hơi nhưng chỉ khi "
               "dùng van xả áp; <b>Vùng 1</b> là một hình cầu bán kính 1 m quanh miệng "
               "ống trong trường hợp dùng van xả áp; <b>Vùng 2</b> là một bán cầu đặt lên "
               "đỉnh miệng thông hơi trong mọi trường hợp, cộng với bên trong ống thông "
               "hơi khi dùng đĩa vỡ. Ghi chú in kèm Hình 3.19 nêu rõ: 'Khi xảy ra từ đĩa "
               "vỡ, Vùng 0 bên trong ống và Vùng 1 ngay quanh ống đều trở thành Vùng 2'. "
               "Trong hình, a = 1 m và b được tính theo Chương 4 dựa trên phương trình độ "
               "phạm vi phun và thể tích khí/hơi thoát ra."))
    b.append(fig(16, FD.fig_f319()))
    b.append(note("<b>Khoảng trống nguồn.</b> Bảng 3.2 và Bảng 3.7 chỉ được nhắc tên trong "
                  "phần này: số liệu của hai bảng nằm ngoài đoạn nguồn (các trang PDF "
                  "80–87 bị thiếu trong bản PDF cung cấp, chỉ còn chữ 'MISSING PAGE'), nên "
                  "không có dòng dữ liệu nào được tái tạo. Các giá trị như bán kính 1 m, "
                  "điểm sôi gấp bốn lần nhiệt độ môi trường và các hệ thức a, b, c được "
                  "giữ nguyên như mô tả của nguồn."))
    return "".join(b)


def body_en():
    b = []
    b.append(h4("3.4.9 Sampling points", "3.4.9 Sampling points"))
    b.append(p("The problem with sampling points is that most are manual and, apart from "
               "the doubtful wisdom of deliberately creating a significant hazardous area "
               "by a routine action, there is the problem that the person taking the sample "
               "is inside the hazardous area at the time when flammable materials are "
               "present. Since the majority of flammable materials are also toxic (see HSE "
               "Guidance Note EH 40), this is not a situation that can be accepted. Sampling "
               "arrangements are therefore usually carefully designed to minimize the "
               "hazardous area created in normal operation, so that the only significant "
               "hazardous area occurs in abnormal operation."))
    b.append(p("<b>Sampling liquids.</b> Any sampling point used for sampling liquids "
               "should be so arranged that any spillages occurring during normal sampling "
               "are removed immediately. To do this, the sampling arrangements should "
               "incorporate features of the kind achieved by the system shown in Figure "
               "3.15: the tundish or receptor of spillages below the sampling point should "
               "transfer any spillage to a closed storage facility and safe disposal "
               "system. For liquids of low volatility (suggested to have atmospheric "
               "boiling points of at least four times ambient temperature) the effects of "
               "gravity will normally be all that is needed to ensure spillage collection "
               "in the tundish, but in other cases some form of extract system will be "
               "needed to draw spillages into the tundish."))
    b.append(fig(12, FD.fig_f315()))
    b.append(p("If these techniques are used, the release of flammable material into the "
               "atmosphere around the sampling point in normal operation will be minimal "
               "and no significant Zone 1 will exist. There will, however, remain the "
               "possibility of significant release in abnormal operation, due for example "
               "to failure of the sampling valve, which will release too much liquid for "
               "the tundish to deal with, or to blockage of the tundish itself. In both "
               "cases there will be significant leakage of flammable liquid and possible "
               "splashing around the sampling point. This produces a small Zone 2 around "
               "the sampling point and a pool below it which grows until it is contained "
               "physically or by the evaporation rate, then creating a hazardous area as "
               "defined in Table 3.7. The result given in Figure 3.15 is as follows: there "
               "are no Zones 0 and 1, and Zone 2 consists of a sphere of 1 m around the "
               "sampling point together with the pool and its surrounding hazardous area. "
               "In Figure 3.15, a = 1 m, b = pool and c = Table 3.7."))
    b.append(p("Where the flammable material is not toxic, simpler arrangements are "
               "possible but are not recommended, as they will probably create larger "
               "hazardous areas whose justification is doubtful given how easily the above "
               "arrangements can be used. Details of toxicity for the more usual materials "
               "are given in HSE Guidance Note EH 40."))
    b.append(p("<b>Sampling gases and vapours.</b> Sampling gases, vapours and liquefied "
               "vapours under pressure can give rise to a hazardous area of significant "
               "proportions and cannot be permitted. It is necessary to use the closed "
               "in-line sampling system shown in Figure 3.16 and, in some cases, even to "
               "allow for evacuation of the spaces between the sample bottle and the fixed "
               "valves before disconnection of the bottle. This is likely only with "
               "liquefied gases, since otherwise the amount of flammable material stored "
               "in the interspace will be small if the system is properly designed. Again "
               "the objective is to eliminate any Zone 1 effectively, so that a hazardous "
               "area is present only in abnormal operation. Such abnormal situations "
               "include valve seal failure, pipe-joint failure and incorrect connection by "
               "personnel, the last of which would be expected to be corrected quickly "
               "because the sampling personnel are present."))
    b.append(fig(13, FD.fig_f316()))
    b.append(p("The hazardous area would therefore be most likely to arise from pipe-joint "
               "or valve failure, both of which are dealt with in sections 3.5.1 and 3.5.2 "
               "and in Table 3.2 (a numbering that does not occur in the printed text; see "
               "the note below). The result is as follows. There are no Zones 0 and 1. Zone "
               "2 consists of an area in accordance with line 3 of Table 3.2 around the "
               "valve stem and an area in accordance with the appropriate column of Table "
               "3.2 around each joint, as shown in Figure 3.16."))
    b.append(note("<b>Note to Figure 3.16 (verbatim, typo retained).</b> 'Note: Release "
                  "from value stems assumed less than joints. If this is not so the "
                  "hazardous area should be adjusted to take account of hazardous areas "
                  "from column 3 of Table 3.2'. The printed 'value stems' is a typo for "
                  "valve stems and is kept. Table 3.2 is named only; its data are outside "
                  "this source span, so no rows are reproduced."))

    b.append(h4("3.4.10 Walls and apertures", "3.4.10 Walls and apertures"))
    b.append(p("Where extents of hazardous areas are defined by a wall that contains a "
               "door, the door becomes a source of release as far as the non-hazardous side "
               "of the wall is concerned and results in a hazardous area as shown in Figure "
               "3.17. Likewise, where a wall is short, the hazardous area extends around it "
               "as shown in Figure 3.18. In both cases the extension is based upon the "
               "original extent of the hazardous area and the distance between the source "
               "of hazard and the wall."))
    b.append(fig(14, FD.fig_f317()))
    b.append(fig(15, FD.fig_f318()))
    b.append(p("The key to both figures is: a = distance of wall from source of hazard; "
               "b = extent of hazardous area ignoring wall; c = b − a, the extension "
               "beyond the wall. The extension is thus the original extent reduced by the "
               "source-to-wall distance."))
    b.append(h4("3.4.11 Vents", "3.4.11 Vents"))
    b.append(p("Vents normally operate only in abnormal circumstances, such as the opening "
               "of a relief valve or the rupture of a bursting disc. In such cases, "
               "relatively large amounts of flammable gas or vapour are released directly "
               "to the surrounding atmosphere through a vent or flare stack. This section "
               "refers only to such direct situations; in other cases secondary containment "
               "is usually the norm and can be dealt with according to earlier sections of "
               "this chapter. The flare is assumed not to be ignited, since that "
               "possibility exists."))
    b.append(p("In the case of a bursting disc there will be no release of flammable "
               "material in normal operation, whereas with a relief valve a slight "
               "leakage through the seat must be considered possible (this does not include "
               "the valve-operating stem, which should be dealt with separately). In the "
               "one case a Zone 1 may be present at the vent exit and in the other not. "
               "When the valve opens or the bursting disc ruptures, a significant flow of "
               "flammable material occurs in both cases, but only in abnormal operation. "
               "The small release from valve-seat leakage will drift from the vent outlet, "
               "whereas release from valve operation or disc rupture will be a rapid flow. "
               "The hazardous area due to the former will therefore be a small sphere, as "
               "the drift is dispersed by wind, while that from the latter will be a plume, "
               "because the jet turbulence will be mixing. This gives the rather unusual "
               "hazardous-area distribution shown in Figure 3.19, where Zone 2 allows for "
               "wind distortion of the plume."))
    b.append(p("The result is as follows. <b>Zone 0</b> is within the vent stack, but only "
               "if a relief valve is used. <b>Zone 1</b> is a sphere of 1 m around the vent "
               "outlet in cases where the relief valve is used. <b>Zone 2</b> is a "
               "hemisphere superimposed upon the top of the vent in all cases, plus the "
               "interior of the vent stack where a bursting disc is used. The printed note "
               "to Figure 3.19 states: 'Where release is from a bursting disc Zone 0 inside "
               "vent and Zone 1 immediately surrounding the vent, both become Zone 2'. In "
               "the figure, a = 1 m and b is calculated from Chapter 4 using the jet-release "
               "extent equation and the volume of gas or vapour released."))
    b.append(fig(16, FD.fig_f319()))
    b.append(note("<b>Source gap.</b> Tables 3.2 and 3.7 are named only in this section: "
                  "their data lie outside this source span (PDF pp. 80-87 are missing from "
                  "the supplied PDF and contain only the words 'MISSING PAGE'), so no rows "
                  "are reproduced. Values such as the 1 m sphere, a boiling point of at "
                  "least four times ambient, and the a, b, c relationships are retained as "
                  "descriptions from the source."))
    return "".join(b)
