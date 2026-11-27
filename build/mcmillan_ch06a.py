# -*- coding: utf-8 -*-
"""Chapter 6, module A - bilingual reader (EN/VI).

Alan McMillan, *Electrical Installations in Hazardous Areas*
(Butterworth-Heinemann, 1998), printed pp. 149-151 (PDF pp. 170-172).

Covers the chapter opener (the three Factories Acts actions, the historic
Zone Z and Zone Y), the adoption of the three-Zone approach with Table 6.1,
and sections 6.1 and the opening of 6.1.1. Owns the chapter h2 and the h3
and h4 for sections 6.1 and 6.1.1, plus prose only. Table 6.1 is supplied
by mcmillan_tbl61. The Godbert-Greenwald discussion and all later sections
belong to the next module. There are no figures or equations here. The
integration shell owns the page shell, references and end matter.

This is an unofficial study translation. The source PDF is not republished.
"""
from mcmillan_common import h2, h3, h4, p, note, table
import mcmillan_tbl61 as T61


def body_vi():
    b = []
    b.append(h2("6 — Thực hành phân loại khu vực nguy hiểm đối với bụi",
                "6 — Area classification practice for dusts"))
    b.append(p("Trong các chương trước, việc phân loại khu vực nguy hiểm của "
               "các bầu khí quyển nổ được cấu thành từ khí, hơi và sương mù "
               "chất lỏng cùng với không khí đã được thảo luận, cùng với pháp "
               "luật giải quyết toàn bộ vấn đề về bầu khí quyển nổ. Trong số "
               "các quy định đó có những yêu cầu về xử lý bụi cháy được (thuật "
               "ngữ 'cháy được' đồng nghĩa với thuật ngữ 'dễ cháy' dùng cho "
               "khí, hơi và sương mù chất lỏng). Như đã thảo luận trong Chương "
               "1, Quy định 31(1) và 31(2) của các Đạo luật Nhà máy¹ yêu cầu "
               "thực hiện một số hành động khi có thể có hoặc có thể phát "
               "thải bụi cháy được."))
    b.append(p("Thứ nhất, quy định này yêu cầu các dây chuyền chế biến có thể "
               "tạo ra đám mây bụi hoặc phát thải bụi phải được bao kín ở mức "
               "tối đa có thể để ngăn sự hình thành chung của một đám mây bụi. "
               "Điều này đã được thực hiện trong trường hợp các thiết bị như "
               "cyclone, nơi bụi được chứa giữ trong cyclone trong quá trình "
               "chế biến, nhưng quy định này cũng đòi hỏi hành động bổ sung để "
               "hạn chế sự di chuyển của bất kỳ phát thải nào (nói cách khác, "
               "đòi hỏi phải có những nỗ lực tích cực nhằm che chắn và xác "
               "định giới hạn phạm vi di chuyển của bụi được phát thải)."))
    b.append(p("Thứ hai, quy định yêu cầu rằng, khi có thể phát thải bụi, sự "
               "tích tụ bụi trong những khu vực được bao kín đó phải được hạn "
               "chế bằng công tác dọn dẹp loại bỏ các lớp bụi và tương tự để "
               "ngăn tích tụ theo thời gian. Cần nhớ rằng khi phát thải, bụi "
               "không phân tán dần theo thời gian như khí hoặc hơi mà lắng "
               "xuống thành một lớp; để ngăn các lớp này tích tụ, bụi lắng "
               "xuống phải được loại bỏ thường xuyên, tự động hoặc bằng thủ "
               "công. Các nguồn bắt lửa phải được loại trừ ở những nơi đám mây "
               "bụi hoặc lớp bụi lắng có thể xuất hiện với mật độ hoặc độ dày "
               "đủ để cấu thành mối nguy hiểm."))
    b.append(p("Thứ ba, quy định yêu cầu loại trừ hoặc bao kín hiệu quả bất kỳ "
               "nguồn bắt lửa nào trong một khu vực mà, ngay cả sau khi đã "
               "thực hiện tất cả các hành động nêu trên, đám mây bụi hoặc lớp "
               "bụi lắng vẫn có thể xuất hiện và không thể loại trừ được nguồn "
               "bắt lửa."))
    b.append(note("<b>Lưu ý về cách trích dẫn 'các Đạo luật Nhà máy'.</b> Thân "
                  "văn bản dùng số nhiều 'các Đạo luật Nhà máy¹' (tại đây và "
                  "trong phần 6.1), trong khi tài liệu tham khảo in số 1 mang "
                  "tên số ít 'The Factories Act 1961'. Cách viết trong thân "
                  "văn bản được giữ nguyên theo bản in và không được sửa cho "
                  "khớp với danh mục tài liệu tham khảo."))
    b.append(p("Sự khác biệt về đặc tính giữa khí và bụi không thể được nhấn "
               "mạnh quá mức. Trong trường hợp khí, hơi và sương mù chất lỏng, "
               "người ta đặt nhiều kỳ vọng vào việc cung cấp các phương tiện "
               "phân tán hiệu quả nhất có thể, trong khi đối với bụi, dọn dẹp "
               "và che chắn lại là những yếu tố hàng đầu. Điểm chung của cả hai "
               "là yêu cầu đặt lên ngành công nghiệp phải giảm thiểu nguy cơ "
               "phát thải của từng loại, và chỉ tiến hành bảo vệ chống lại hậu "
               "quả của phát thải khi phát thải đó không thể ngăn ngừa một "
               "cách hợp lý."))
    b.append(p("Những khu vực có bụi hiện diện ở mức độ có thể xảy ra bắt lửa "
               "đã từng được phân loại theo truyền thống chỉ khi bụi có thể "
               "được phát thải từ quá trình chế biến, thành Vùng Z và Vùng Y. "
               "Định nghĩa của hai Vùng này được đưa ra trong Chương 2 và rõ "
               "ràng chỉ đề cập đến các vấn đề phát thải trong vùng đó."))
    b.append(note("<b>Lưu ý về lỗi lặp từ trong bản in.</b> Bản in viết "
                  "'have historically been been classified' (từ 'been' bị "
                  "lặp lại). Cách viết này được giữ nguyên trong bản dịch "
                  "tiếng Anh và được ghi nhận tại đây; không sửa thành 'have "
                  "historically been classified'."))
    b.append(p("Theo định nghĩa, Vùng Z tương tự như Vùng 1 đối với khí, còn "
               "Vùng Y tương tự như Vùng 2. Điều này được củng cố thêm bởi "
               "thực tế là BS 6467, Part 2² loại trừ bên trong các bình chứa "
               "khỏi phạm vi áp dụng. Sự loại trừ này rõ ràng dựa trên hiểu "
               "biết rằng việc lắp đặt thiết bị điện bên trong bình chứa, "
               "silo, v.v., nói chung chỉ được chấp nhận trong những trường "
               "hợp đặc biệt. Giờ đây đã có sự thay đổi quan điểm về vấn đề "
               "này, vì IEC 1241–3³ thừa nhận ba Vùng rủi ro đối với bụi. "
               "Những định nghĩa này đồng nghĩa hơn nhiều với các định nghĩa "
               "dành cho khí và hơi, cho mối quan hệ như trong Bảng 6.1."))
    b.append(table(T61.HEAD61_VI, T61.ROWS61, T61.CAPTION61_VI))
    b.append(note("<b>Lưu ý về các ký hiệu tiêu chuẩn trong Bảng 6.1.</b> Bảng "
                  "in dùng 'BS 5345, Part 2 (1983)', 'BS 6467, Part 2 (1988)' "
                  "và 'IEC 1241–3 (1994) (Draft)'; thân văn bản dùng 'BS 6467, "
                  "Part 2²' và 'IEC 1241–3³' kèm ký hiệu chú thích. Các dạng "
                  "in này được giữ nguyên, không thống nhất lại với nhau."))
    b.append(p("Trong chương này, cách tiếp cận ba Vùng mới sẽ được dùng vì "
               "tài liệu được viện dẫn là một dự thảo Tiêu chuẩn Anh, dựa trên "
               "một dự thảo Tiêu chuẩn IEC (Ủy ban Kỹ thuật Điện Quốc tế), và "
               "sẽ trở thành Tiêu chuẩn Anh trong tương lai gần. Ngoài ra, kỹ "
               "thuật ba Vùng này đã được một công ty lớn sử dụng từ năm 1973 "
               "với thành công đáng kể và, vì mối liên hệ của nó với phân loại "
               "khí và hơi, cách tiếp cận này có vẻ hợp lý hơn."))
    b.append(p("IEC 1241–3³ cũng hình dung đến việc phát thải bụi bên ngoài "
               "các tòa nhà, một tình huống bất thường vì tác động của môi "
               "trường khiến những khu vực mà bụi được xử lý, lưu trữ hoặc chế "
               "biến thường nằm trong nhà hoặc ít nhất là được che chắn. Việc "
               "sử dụng các vật liệu tạo ra bụi cháy được ngoài trời cần được "
               "thận trọng. Trong một số trường hợp (ví dụ, các đầu ra của hệ "
               "thống thông gió hút, nơi trong trường hợp bất thường không thể "
               "loại trừ khả năng phát thải bụi), sự hiện diện của một cơ sở "
               "nạp liệu (đặc biệt là nạp thủ công) mà tại đó bụi chịu tác động "
               "của các dòng khí ngoài trời thông thường do gió tạo ra thì khó "
               "có thể biện minh, vì sự phân bố của bất kỳ phát thải bụi nào trở "
               "nên khó xác định hơn nhiều. Một số tình huống ngoài trời có thể "
               "chấp nhận được, nhưng sự kiểm soát có thể thực hiện được trong "
               "các tòa nhà đối với phát thải bụi lại có lợi đến mức khó có thể "
               "bỏ qua. Ngay cả khi các hoạt động ngoài trời được xem xét, cũng "
               "cần tính đến việc che chắn một phần để đạt được một mức độ tin "
               "cậy nhất định về đặc tính của lớp bụi lắng và đám mây bụi."))
    b.append(note("<b>Lưu ý về sự thận trọng khi phát thải ngoài trời.</b> Bản "
                  "in nêu rằng các đầu ra của thông gió hút — nơi không thể "
                  "loại trừ khả năng phát thải bụi trong trường hợp bất thường "
                  "— có thể được chấp nhận, nhưng một cơ sở nạp liệu thủ công "
                  "tiếp xúc với gió thông thường thì khó biện minh vì sự phân "
                  "bố bụi rất khó xác định. Câu văn in có cấu trúc hơi khó "
                  "đọc; ý được giữ nguyên theo bản in, không sửa lại."))

    b.append(h3("6.1 Tính chất của bụi", "6.1 Properties of dusts"))
    b.append(p("Có hai tính chất của bụi quan trọng đối với phân loại khu vực, "
               "đó là nhiệt độ bắt lửa cần thiết cho một đám mây bụi và nhiệt "
               "độ bắt lửa cần thiết cho một lớp bụi lắng. Cần lưu ý rằng năng "
               "lượng bắt lửa không được đề cập đến. Điều này không phải vì "
               "bụi không có năng lượng bắt lửa (xem Bảng 6.2), mà vì các "
               "phương pháp bảo vệ thiết bị điện trong những khu vực trở nên "
               "nguy hiểm do bụi dựa vào việc loại trừ bụi một cách đầy đủ khỏi "
               "các bộ phận điện bên trong thiết bị. Vì vậy, nói chung năng "
               "lượng bắt lửa không phải là thông tin cần thiết."))
    b.append(p("Thông tin về cả hai giá trị này cho nhiều loại bụi được cho "
               "trong Bảng 6.2. Cần lưu ý rằng các số liệu bắt lửa lớp bụi lắng "
               "dựa trên độ dày lớp là 5 mm, vì các lớp dày hơn thường không "
               "được chấp nhận do có thể rõ ràng vi phạm Section 31 của các "
               "Đạo luật Nhà máy¹, và cần dọn dẹp duy trì các lớp ở độ dày nhỏ "
               "hơn. Nếu trong một trường hợp cụ thể không làm được điều đó thì "
               "các số liệu trong Bảng 6.2 không phù hợp và phải tiến hành thử "
               "nghiệm để xác định nhiệt độ bắt lửa ở độ dày liên quan."))
    b.append(p("Ngoài ra, kích thước và phân bố hạt trong bụi cùng với độ ẩm "
               "có sự thay đổi, và theo đó cả năng lượng bắt lửa lẫn nhiệt độ "
               "bắt lửa cũng thay đổi. Bảng 6.2 dựa trên thành phần kích thước "
               "hạt cụ thể của bụi, trong một số trường hợp đã được xác định. "
               "Một lần nữa, nếu bụi trong một trường hợp cụ thể, dù có trong "
               "Bảng 6.2, có thành phần khác biệt đáng kể thì các số liệu trong "
               "Bảng 6.2 có thể không chính xác và có thể cần xác định nhiệt độ "
               "bắt lửa riêng của nó. Tuy nhiên, các số liệu trong Bảng 6.2 là "
               "thước đo tốt vì dựa trên các loại bụi tương đối mịn và có thể "
               "dùng với mức độ tin cậy khá trong hầu hết các tình huống thực "
               "tế."))
    b.append(p("Sau khi đã nói rằng năng lượng bắt lửa không phải là thông tin "
               "cần thiết đối với phát thải bụi, không nên bỏ qua việc nhiều "
               "nhà máy chứa cả khí/hơi dễ cháy lẫn bụi cháy được, và cần bảo vệ "
               "chống bắt lửa cho cả hai. Ngoài ra, một số bụi có thể phân hủy "
               "giải phóng hơi dễ cháy. Khi có khí/hơi dễ cháy, việc bắt lửa "
               "chúng rất có thể sẽ làm cháy đám mây bụi hoặc lớp bụi lắng, vì "
               "vậy phải đảm bảo bảo vệ chống cả hai rủi ro."))
    b.append(p("(Cần lưu ý rằng, dù việc sản xuất chất nổ được loại trừ rõ ràng "
               "bởi hầu hết các Tiêu chuẩn và Quy phạm mà cuốn sách này viện "
               "dẫn, cả hơi dễ cháy lẫn bụi cháy được đều hiện diện trong các "
               "giai đoạn đầu của sản xuất chất nổ, và có thể cần áp dụng các "
               "cách tiếp cận trong cuốn sách này để ngăn việc bắt lửa các hơi "
               "và bụi đó, vốn có thể đóng vai trò là ngòi nổ cho vụ nổ chất "
               "nổ.)"))

    b.append(h4("6.1.1 Sự bắt lửa của các đám mây bụi",
                "6.1.1 The ignition of dust clouds"))
    b.append(p("Khi bụi được trộn với không khí ở mức độ cần thiết để tạo thành "
               "một bầu khí quyển nổ, hỗn hợp rất đặc và nhìn rõ ràng. Những "
               "đám mây bụi có kích thước bất kỳ có khả năng này sẽ rất hiếm vì "
               "những vấn đề môi trường mà chúng có thể gây ra. Tỷ lệ bụi trên "
               "không khí là một đại lượng thay đổi tùy thuộc vào kích thước "
               "hạt, v.v., và không có một hỗn hợp lý tưởng cụ thể nào được "
               "đưa ra, khác với tình huống đối với khí và hơi. Cũng không thể "
               "bảo đảm nồng độ bụi đồng đều trong toàn bộ đám mây."))
    return "".join(b)


def body_en():
    b = []
    b.append(h2("6 — Area classification practice for dusts",
                "6 — Area classification practice for dusts"))
    b.append(p("In previous chapters the area classification of explosive "
               "atmospheres constituted of gases, vapours and mists and air "
               "had been discussed together with the legislation which "
               "addresses the total problem of explosive atmospheres. Among "
               "this legislation are requirements for the handling of "
               "combustible dusts (the term combustible is synonymous with "
               "the term flammable which is applied to gases, vapours and "
               "mists). As discussed in Chapter 1, Regulation 31(1) and 31(2) "
               "of the Factories Acts¹ requires certain actions where "
               "Combustible Dusts may be present or released."))
    b.append(p("First, it requires that processing plant which may produce "
               "dust clouds or release dust be enclosed as far as possible to "
               "prevent the general development of a dust cloud. This is "
               "already done in the case of such things as cyclones, where "
               "the dust is contained by the cyclone during processing, but "
               "it also requires further action to restrict the travel of "
               "any release (in other words it requires positive attempts to "
               "be made to contain and define the limits of travel of "
               "released dust)."))
    b.append(p("Second, it requires that, where dust can be released, "
               "accumulation of dust in these enclosed areas be limited by "
               "housekeeping which removes layers of dust and the like to "
               "prevent accumulation over time. It must be remembered that "
               "on release dust does not, like gas or vapour, disperse over "
               "time but settles as a layer and, to prevent such layers "
               "accumulating, dust which settles should be regularly removed "
               "either automatically or manually. Sources of ignition should "
               "be excluded where dust clouds or layers can occur in such "
               "density or thickness to constitute a hazard."))
    b.append(p("Third, it requires exclusion or effective enclosure of any "
               "source of ignition in an area where, even after taking all of "
               "the actions described above, dust clouds or layers may occur "
               "and sources of ignition cannot be excluded."))
    b.append(note("<b>Note on the 'Factories Acts' citation.</b> The body text "
                  "uses the plural 'Factories Acts¹' here and in section 6.1, "
                  "while printed reference 1 is worded in the singular, 'The "
                  "Factories Act 1961'. The body wording is preserved as "
                  "printed and is not aligned with the reference list."))
    b.append(p("The differences between the performance of gases and dusts "
               "cannot be overstressed. In the case of gases, vapours and "
               "mists great reliance is placed on providing the most "
               "effective means of dispersion possible, while in the case of "
               "dusts, housekeeping and containment come to the fore. The one "
               "thing that both have in common is the requirement placed "
               "upon industry to minimize the risks of release of either, and "
               "to approach the protection of the results of release only "
               "when the release cannot reasonably be prevented."))
    b.append(p("The areas where dust is present, to an extent where ignition "
               "could occur, have historically been been classified only "
               "where dust could be released from process as Zone Z and Zone "
               "Y. The definitions of these two Zones are given in Chapter 2 "
               "and clearly address only problems of release in that zone."))
    b.append(note("<b>Note on the doubled word in the print.</b> The print "
                  "reads 'have historically been been classified', with the "
                  "word 'been' repeated. The wording is preserved verbatim in "
                  "the English text and noted here; it has not been corrected "
                  "to 'have historically been classified'."))
    b.append(p("Zone Z (by definition) appears similar to Zone 1 for gases "
               "and Zone Y to Zone 2. This is further reinforced by the fact "
               "that BS 6467, Part 2² excludes the interior of vessels from "
               "its scope. This exclusion was clearly based upon the "
               "understanding that the inclusion of electrical apparatus "
               "inside vessels and silos, etc., was generally only acceptable "
               "in special circumstances. There has now been a change of view "
               "in this regard as IEC 1241–3³ recognizes three Zones of risk "
               "in respect of dusts. These definitions are much more "
               "synonymous with those for gases and vapours, giving the "
               "relationship shown in Table 6.1."))
    b.append(table(T61.HEAD61_EN, T61.ROWS61, T61.CAPTION61_EN))
    b.append(note("<b>Note on the standards designations in Table 6.1.</b> The "
                  "printed table uses 'BS 5345, Part 2 (1983)', 'BS 6467, Part "
                  "2 (1988)' and 'IEC 1241–3 (1994) (Draft)', while the body "
                  "uses 'BS 6467, Part 2²' and 'IEC 1241–3³' with footnote "
                  "markers. Each printed form is preserved and has not been "
                  "harmonised."))
    b.append(p("In this chapter the new three-Zone approach will be used as "
               "the document referred to is a draft British Standard, is "
               "based upon a draft IEC (International Electrotechnical "
               "Commission) Standard and will become a British Standard in "
               "the near future. In addition, this three-Zone technique has "
               "been used in one large company since 1973 with considerable "
               "success and, because of its relationship with the gas and "
               "vapour classification, the approach appears more logical."))
    b.append(p("IEC 1241–3³ also envisages dust releases outside buildings, "
               "which is an unusual situation as the effect of the "
               "environment is such that areas where dust is handled, stored "
               "or processed are normally indoors, or at least protected. "
               "The use of materials producing combustible dusts outdoors "
               "should be treated with caution. While in some cases (e.g., "
               "the outlets of extract ventilation systems where, in "
               "abnormal cases, the possibility of dust release cannot be "
               "ruled out) the presence of a loading facility (particularly "
               "a manual one) where dust is subject to normal exterior air "
               "currents provided by wind is difficult to justify as the "
               "distribution of any dust release becomes much more difficult "
               "to determine. Some external situations may be acceptable but "
               "the control which can be exercised within buildings in the "
               "case of dust releases is so advantageous it is hard to "
               "ignore. Even if outside operations are considered, partial "
               "enclosure to give some degree of confidence as to the "
               "performance of dust layers and clouds should be addressed."))
    b.append(note("<b>Note on the outdoor-release caution.</b> The print "
                  "allows that the outlets of extract ventilation systems, "
                  "where the possibility of dust release cannot be ruled out "
                  "in abnormal cases, may be acceptable, but a manual loading "
                  "facility exposed to normal wind is difficult to justify "
                  "because the distribution of any release becomes much "
                  "harder to determine. The printed sentence is awkward in "
                  "construction; the sense is preserved as printed and has "
                  "not been smoothed out."))

    b.append(h3("6.1 Properties of dusts", "6.1 Properties of dusts"))
    b.append(p("Two properties of dusts are important to area classification "
               "and these are the ignition temperature required for a dust "
               "cloud and the ignition temperature required for a dust layer. "
               "It should be noted that ignition energy is not mentioned. "
               "This is not because dusts do not have an ignition energy (see "
               "Table 6.2) but because the methods of protection of "
               "electrical apparatus in areas made hazardous by dusts rely on "
               "adequate exclusion of dust from the electrical parts within "
               "the apparatus. Therefore, ignition energy is not a necessary "
               "piece of information in general."))
    b.append(p("Information on both of these values for a variety of dusts is "
               "given in Table 6.2. It should be noted that the layer ignition "
               "figures are based upon a layer thickness of 5 mm, as thicker "
               "layers are not normally acceptable because they could clearly "
               "be in contravention of Section 31 of the Factories Acts¹ and "
               "it is required that housekeeping normally maintains layers at "
               "smaller thicknesses. If, in a particular case, this is not "
               "possible then the figures in Table 6.2 are not appropriate "
               "and tests must be carried out to determine the ignition "
               "temperature at the relevant thickness."))
    b.append(p("In addition, particle size and distribution in dusts, "
               "together with moisture content varies and with it both "
               "ignition energy and temperature. Table 6.2 is based upon "
               "particular particle size make-up of dusts, which is in some "
               "cases identified. Once again, if the dust in a particular "
               "case, while being included in Table 6.2, has a significantly "
               "different constitution then the figures in Table 6.2 may not "
               "be accurate and it may be necessary to determine its "
               "particular ignition temperature. The figures in Table 6.2, "
               "however, are a good yardstick as they are based on relatively "
               "fine dusts and may be used with a fair degree of confidence "
               "in most practical situations."))
    b.append(p("Having stated that ignition energy is not a necessary item of "
               "information for dust releases it should not be overlooked "
               "that many plants contain both flammable gases/vapours and "
               "combustible dusts and protection is necessary against the "
               "ignition of both. Also, some dusts may decompose to give off "
               "flammable vapours. Where flammable gases/vapours do occur "
               "ignition of these may well ignite the dust cloud or layer and "
               "protection against both risks must be provided."))
    b.append(p("(It is worthy of note that, although the manufacture of "
               "explosives is specifically excluded by the majority of the "
               "Standards and Codes to which this book refers, both "
               "flammable vapours and combustible dusts are present in the "
               "early stages of explosives production and the approaches in "
               "this book may need to be implemented to prevent the ignition "
               "of such vapours and dusts which could otherwise act as "
               "triggers for detonation of the explosives.)"))

    b.append(h4("6.1.1 The ignition of dust clouds",
                "6.1.1 The ignition of dust clouds"))
    b.append(p("When dust is mixed with air to the degree necessary to form "
               "an explosive atmosphere, the mixture is very dense and "
               "clearly visible. Dust clouds of any size which exhibit this "
               "possibility will be rare because of the environmental "
               "problems which they may create. The ratio of dust to air is a "
               "variable quantity depending upon particle size, etc., and no "
               "specific ideal mixture is given, unlike the situation in "
               "respect of gases and vapours. It is also not possible to "
               "ensure an even concentration of dust throughout the cloud."))
    return "".join(b)
