# -*- coding: utf-8 -*-
"""Chapter 11, module C - bilingual reader (EN/VI).

Alan McMillan, *Electrical Installations in Hazardous Areas*
(Butterworth-Heinemann, 1998), printed pp. 286-289 (PDF pp. 307-310).

Covers the tail of the "Infallible containment" material, the unnumbered
subheads "Containment with limited release capability" and "Containment with
unlimited release" with both Q1/Q2 flowrate formulas, Section 11.5
"Enclosures, ducting and internal components" and Section 11.5.1
"Enclosures". Figures 11.2 and 11.3 are printed on the closing page and are
inserted at that printed position.

Printed quirks are kept in the English text - the capitalised 'Pressurization',
"release is possible. and To be considered", "with confidence.In such cases",
"weather proof", the missing space after a full stop, the superscript footnote
markers and the dangling "All" - with bilingual notes. The Vietnamese follows
the intended meaning. The chapter shell owns the chapter h2, the references
and the end matter.

This is an unofficial study translation. The source PDF is not republished.
"""
from mcmillan_common import h3, h4, p, note, fig
import mcmillanfig11 as F


def body_vi():
    b = []

    # Printed p.286: tail of the "Infallible containment" paragraph.
    b.append(p("các tình huống có thể xảy ra khi chỉ sử dụng trong môi trường "
               "nổ, nhưng thực hành kỹ thuật thông thường là phù hợp để xác "
               "định tính phù hợp của chúng. Chứa không thể hỏng không được coi "
               "là giải phóng vật liệu dễ cháy và do đó, cho mục đích tạo áp, "
               "bất kỳ vỏ bọc nào mà sự chứa đựng các vật liệu dễ cháy đi vào "
               "được coi là không thể hỏng thì có thể được xem như một vỏ bọc "
               "không có sự xâm nhập của vật liệu dễ cháy."))
    b.append(note("<b>Ghi chú về cách diễn đạt trong bản in.</b> Bản in viết "
                  "hoa 'Pressurization' giữa câu trong cụm 'for the purposes "
                  "of Pressurization'. Bản tiếng Anh giữ nguyên dạng in; bản "
                  "tiếng Việt theo nghĩa thông thường."))

    # Unnumbered subhead, printed p.286.
    b.append(h4("Sự chứa đựng có khả năng giải phóng hạn chế",
                "Containment with limited release capability"))
    b.append(p("Khi các hệ thống chứa đựng bên trong vỏ bọc được tạo áp chứa, "
               "ví dụ, các phớt nén và các mối nối ren, thì có thể xảy ra sự "
               "giải phóng. Để được coi là giải phóng hạn chế, lưu lượng của "
               "vật liệu dễ cháy được giải phóng phải được kiểm soát ở một giá "
               "trị tối đa đã biết. Trừ khi kích thước của vết rò rỉ có thể "
               "được xác định chính xác, cách duy nhất để đạt được điều này là "
               "đưa vào một đặc tả kỹ thuật cho một thiết bị hạn chế lưu lượng "
               "do người lắp đặt lắp bên ngoài vỏ bọc, hoặc đặt bộ điều khiển "
               "đó bên trong vỏ bọc - trong trường hợp đó hệ thống chứa đựng "
               "cho đến và bao gồm cả bản thân bộ điều khiển phải không thể "
               "hỏng. Ngoài ra, khi sử dụng các mối nối như mối nối nén "
               "kim loại/kim loại hoặc mối nối vặn vít, có thể đủ để quy định "
               "áp suất của vật liệu dễ cháy đi vào hệ thống chứa đựng và tính "
               "toán tốc độ giải phóng ở áp suất tối đa nhằm xác định mức giải "
               "phóng hạn chế (xem Chương 4)."))
    b.append(note("<b>Ghi chú về cách diễn đạt trong bản in.</b> Bản in viết "
                  "'release is possible. and To be considered as limited "
                  "release' với chữ 'and' thường sau dấu chấm và chữ 'To' viết "
                  "hoa. Đây là lỗi của nguyên bản; bản tiếng Anh giữ nguyên "
                  "dạng in, bản tiếng Việt theo cấu trúc đúng ý định."))
    b.append(p("Ngoài sự giải phóng hạn chế do rò rỉ, còn có những trường "
               "hợp, chẳng hạn như trong máy sắc ký, nơi vật liệu dễ cháy được "
               "giải phóng có chủ đích. Trong những trường hợp này, tốc độ "
               "giải phóng tối đa trong điều kiện vận hành xấu nhất phải tương "
               "đối dễ xác định. Cần lưu ý, tuy nhiên, rằng có những hạn chế "
               "bổ sung khi việc giải phóng là có chủ đích, trong đó hình thức "
               "tạo áp duy nhất được chấp nhận là tạo áp bằng pha loãng liên "
               "tục với không khí."))
    b.append(p("Thể tích không khí cần thiết để đảm bảo hỗn hợp khí rời khỏi "
               "vỏ bọc có nồng độ dưới 25 phần trăm giới hạn nổ dưới có thể "
               "được tính toán nếu biết thể tích khí được giải phóng cùng với "
               "phần trăm vật liệu dễ cháy trong khí đó. Công thức cho việc "
               "này là:"))
    b.append(p("Q₁ = Q₂ × (Y₁/100) × (100/Y₂) × (100/F)    m³/hour"))
    b.append(p("trong đó Q₁ = Lưu lượng dòng nhỏ nhất của khí bảo vệ    "
               "m³/hour"))
    b.append(p("Q₂ = Tốc độ giải phóng lớn nhất của khí hoặc hơi    "
               "m³/hour"))
    b.append(p("Y₁ = Phần trăm thể tích của vật liệu dễ cháy trong sự giải "
               "phóng    % v/v"))
    b.append(p("Y₂ = Giới hạn nổ dưới thể tích của vật liệu dễ cháy trong "
               "không khí    % v/v"))
    b.append(p("F = Phần trăm giới hạn nổ dưới yêu cầu (trong trường hợp này "
               "là 25 phần trăm)    % v/v"))

    # Printed p.287.
    b.append(p("Khi có nhiều hơn một vật liệu dễ cháy trong hỗn hợp được giải "
               "phóng, lượng không khí nên được tính toán riêng cho từng thành "
               "phần và sau đó cộng các lượng lại với nhau để có lưu lượng "
               "không khí tối thiểu yêu cầu."))

    # Unnumbered subhead, printed p.287.
    b.append(h4("Sự chứa đựng với giải phóng không hạn chế",
                "Containment with unlimited release"))
    b.append(p("Mô tả này đề cập đến sự chứa đựng mà, nếu nó giải phóng khí "
               "hoặc hơi, sẽ được gọi là chứa đựng với giải phóng hạn chế, "
               "nhưng lại giải phóng chất lỏng dễ cháy có thể sinh ra hơi dễ "
               "cháy với tốc độ không thể định lượng một cách chắc chắn. "
               "Trong những trường hợp này, rõ ràng là trong khi tốc độ giải "
               "phóng chất lỏng có thể được xác định thì tốc độ bay hơi lại "
               "không dễ dàng quy định. Do đó không thể pha loãng một cách "
               "hiệu quả hơi được tạo ra với độ tin cậy."))
    b.append(note("<b>Ghi chú về cách diễn đạt trong bản in.</b> Bản in viết "
                  "'with confidence.In such cases, obviously,' không có dấu "
                  "cách sau dấu chấm. Bản tiếng Anh giữ nguyên dạng in; bản "
                  "tiếng Việt thêm dấu cách để dễ đọc."))
    b.append(p("Khi điều này xảy ra, cũng có thể có oxy được cuốn theo "
               "(thường là dưới dạng không khí) trong sự giải phóng, và việc "
               "sử dụng tạo áp bằng khí trơ với dòng khí liên tục, là lựa "
               "chọn duy nhất được chấp nhận ở đây, phải đảm bảo rằng hỗn hợp "
               "rời khỏi vỏ bọc không chứa nhiều hơn 2 phần trăm oxy theo thể "
               "tích. Hỗn hợp hơi và oxy tại điểm giải phóng không được chứa "
               "nhiều hơn 21 phần trăm oxy. Mục tiêu của yêu cầu sau cùng này "
               "là chỉ cho phép không khí được cuốn theo trong sự giải phóng, "
               "vì bất kỳ khí nào được cuốn theo có mức oxy cao hơn có thể "
               "khiến tiêu chí này không được đáp ứng nếu tốc độ bay hơi của "
               "chất lỏng thấp."))
    b.append(p("Việc tính toán lưu lượng tối thiểu của khí trơ để giảm hàm "
               "lượng oxy của một sự giải phóng xuống mức 2 phần trăm yêu cầu "
               "có thể được thực hiện theo cách tương tự như pha loãng bằng "
               "không khí đã thảo luận ở trên:"))
    b.append(p("Q₁ = Q₂ × 100/Y₁    m³/hour"))
    b.append(p("trong đó Q₁ = Lưu lượng dòng nhỏ nhất của khí trơ    "
               "m³/hour"))
    b.append(p("Q₂ = Thể tích oxy trong sự giải phóng    m³/hour"))
    b.append(p("Y₁ = Phần trăm oxy được phép ở đầu ra từ vỏ bọc (trong "
               "trường hợp này là 2 phần trăm)    % v/v"))

    # Printed pp.287-288. Section 11.5 and 11.5.1.
    b.append(h3("11.5 Vỏ bọc, ống dẫn và các linh kiện bên trong",
                "11.5 Enclosures, ducting and internal components"))
    b.append(h4("11.5.1 Vỏ bọc", "11.5.1 Enclosures"))
    b.append(p("Các vỏ bọc dùng cho thiết bị được tạo áp phải đủ bền chịu được "
               "sử dụng bình thường mà không bị hư hỏng, cũng như các khái "
               "niệm bảo vệ khác, và có thể được chế tạo bằng vật liệu kim "
               "loại hoặc phi kim loại, với điều kiện nếu là phi kim loại thì "
               "vật liệu chế tạo không bị ảnh hưởng bất lợi bởi môi trường tạo "
               "áp cũng như bởi bất kỳ vật liệu dễ cháy nào được giải phóng "
               "trong vỏ bọc. Độ bền của vỏ bọc cũng phải sao cho chúng không "
               "bị hư hỏng bởi áp suất tối đa có thể xảy ra trong khi sử dụng. "
               "Mặc dù một cách dễ dàng để đạt được điều này là quy định một "
               "áp suất tối đa rồi để người lắp đặt đảm bảo không vượt quá áp "
               "suất đó, nhưng cách tiếp cận như vậy không thực tế. Trong "
               "nhiều trường hợp, lắp một thiết bị giảm áp quá áp trong vỏ bọc "
               "sẽ dễ dàng hơn, sao cho nếu có bất kỳ sự tăng áp suất không "
               "mong muốn nào trong khi sử dụng thì vỏ bọc được tự động bảo "
               "vệ."))
    b.append(p("Yêu cầu vỏ bọc phải chống thời tiết là không cần thiết vì các "
               "yêu cầu tạo áp sẽ thực sự ngăn ngừa sự xâm nhập của độ ẩm. "
               "Tuy nhiên, việc ngăn ngừa sự xâm nhập của các vật thể lạ rắn "
               "vẫn là cần thiết vì những vật này vẫn có thể xâm nhập do bản "
               "chất của chúng và, không giống như độ ẩm, sẽ không dễ dàng bị "
               "loại bỏ bằng cách thổi sạch nếu chúng xâm nhập trước khi cấp "
               "điện."))
    b.append(note("<b>Ghi chú về cách diễn đạt trong bản in.</b> Bản in viết "
                  "'weather proof' thành hai từ. Bản tiếng Anh giữ nguyên "
                  "dạng in."))
    b.append(p("Một yêu cầu là vỏ bọc phải có chỉ số nguyên vẹn không thấp "
               "hơn IP40 theo BS/EN 60529⁸ khi không có khí tạo áp. Trong "
               "trường hợp máy quay, nơi các chỉ số IP được định nghĩa hơi "
               "khác đi do bản chất của thiết bị, Tiêu chuẩn được sử dụng là "
               "EN 60034-5, được xuất bản tại Vương quốc Anh với tên "
               "BS 4999, Part 105.⁹"))
    b.append(note("<b>Ghi chú về ký hiệu chú thích và OCR.</b> Bản in ghi "
                  "'BS/EN 60529⁸' và 'BS 4999, Part 105.⁹' với các chữ số chú "
                  "thích viết ở dạng mũ; lớp OCR gộp các chữ số vào ký hiệu "
                  "('605298', 'Part 105.9') và chèn dấu cách vào số mục như "
                  "'1 1.5.1'. Bản dịch giữ dạng mũ và số mục đúng như bản in."))
    b.append(p("Khi xem xét chỉ số IP của vỏ bọc, các lỗ mở cố ý để đầu vào "
               "và đầu ra của khí thổi sạch có thể được bỏ qua. Tuy nhiên, "
               "các lỗ này phải được bố trí để đảm bảo thổi sạch đầy đủ và "
               "tránh các điểm chết nơi bất kỳ khí hoặc hơi dễ cháy nào có thể "
               "tồn đọng ngay cả sau khi thổi sạch. Điều này có thể chỉ cần "
               "bố trí cẩn thận các lỗ đơn ở mỗi trường hợp nhưng có thể, khi "
               "hình dạng vỏ bọc phức tạp hoặc các linh kiện tạo ra các vách "
               "ngăn trong vỏ bọc, cần nhiều lỗ đầu vào và đầu ra. Việc lựa "
               "chọn chỉ có thể được đưa ra riêng lẻ nhưng nhiều lỗ không có "
               "khả năng là trường hợp phổ biến."))
    b.append(p("Khi các lỗ đầu ra được lắp trên vỏ bọc được tạo áp bằng tạo "
               "áp tĩnh hoặc tạo áp bằng bù rò rỉ, các lỗ này phải được bố trí "
               "sao cho có thể được đóng hoặc bịt kín sau khi thổi sạch bằng "
               "các thiết bị tạo thành một phần của thiết bị."))
    b.append(p("Cần thừa nhận rằng thiết bị sẽ, cũng như các loại thiết bị "
               "khác, được lắp cửa và nắp cho phép tiếp cận bên trong vỏ bọc. "
               "Phương pháp lý tưởng để xử lý những cái này trong trường hợp "
               "tạo áp bằng bù rò rỉ và tạo áp bằng pha loãng liên tục là sử "
               "dụng một liên kết khóa ngắt nguồn điện và mọi kết nối điện "
               "khác (xem Hình 11.2) khi cửa hoặc nắp được mở. Vì điều này sẽ "
               "hạn chế cơ hội điều chỉnh, có thể đưa vào một hệ thống vô hiệu "
               "hóa liên kết khóa (xem Hình 11.3) cho phép những người có năng "
               "lực mở vỏ bọc, theo một hệ thống kiểm soát, để điều chỉnh và "
               "các mục đích tương tự mà không cần ngắt điện. Sau những công "
               "việc đó, khi vỏ bọc được đóng lại, điều quan trọng là hệ thống "
               "phải đi qua chu kỳ thổi sạch đầy đủ để loại bỏ bất kỳ khí nào "
               "đã xâm nhập, mặc dù không cần thiết phải ngắt nguồn điện trong "
               "thời gian này."))
    b.append(p("Khi cần một dụng cụ hoặc chìa khóa để mở cửa hoặc tháo nắp thì "
               "không cần ngắt điện, nhưng chu kỳ thổi sạch cần được khởi động "
               "sau khi đóng lại. Trong trường hợp này, việc đó phải được "
               "thực hiện thủ công. Có thể lắp một thiết bị nhận biết việc mở "
               "hoặc tháo và ngắt nguồn điện với một cơ chế ghi đè như đã mô "
               "tả ở trên. Yêu cầu dụng cụ hoặc chìa khóa trong trường hợp này "
               "không cho thấy bất kỳ yêu cầu nào về 'phần cố định đặc biệt' "
               "hoặc tương tự (xem Chương 8)."))
    b.append(p("Trong trường hợp tạo áp tĩnh, cửa và nắp sẽ không được cung "
               "cấp để điều chỉnh sau khi tạo áp do bản chất của cách tiếp "
               "cận. All"))
    b.append(note("<b>Ghi chú về phạm vi nguồn.</b> Nguồn được giao kết thúc "
                  "giữa câu tại '...due to the nature of the approach. All'; "
                  "phần tiếp theo của câu nằm trên trang in 289 và nằm ngoài "
                  "mô-đun này. Đoạn dang dở được giữ nguyên theo bản in."))

    # Printed p.289: Figs 11.2 and 11.3 occupy the page after the prose.
    b.append(fig(2, F.fig_f1102()))
    b.append(fig(3, F.fig_f1103()))
    return "".join(b)


def body_en():
    b = []

    # Printed p.286: tail of the "Infallible containment" paragraph.
    b.append(p("possible situations associated with use in explosive "
               "atmospheres alone, but normal engineering practice is "
               "appropriate to determine their suitability. Infallible "
               "containment is not considered to release flammable material "
               "and so, for the purposes of Pressurization, any enclosure "
               "where the containment of flammable materials which enter is "
               "deemed infallible, it may be treated as an enclosure without "
               "entry of flammable material."))
    b.append(note("<b>Note on printed wording.</b> The print capitalises "
                  "'Pressurization' in mid-sentence in 'for the purposes of "
                  "Pressurization'. The printed form is retained in English; "
                  "the Vietnamese follows the intended sense in lower case."))

    # Unnumbered subhead, printed p.286.
    b.append(h4("Containment with limited release capability",
                "Containment with limited release capability"))
    b.append(p("Where containment systems inside pressurized enclosures "
               "contain, for example, compression seals and threaded joints, "
               "release is possible. and To be considered as limited release, "
               "the flow of released flammable material must be controlled to "
               "a known maximum value. Unless the size of leak can be "
               "accurately identified, the only way to achieve this is to "
               "include a specification for a flow-limiting device to be "
               "installed outside the enclosure by the installer, or to place "
               "such a controller inside the enclosure -in which case the "
               "containment up to and including the controller itself must be "
               "infallible. Alternatively, where such joints as metal/metal "
               "compression joints, or screwed joints, etc., are used it may "
               "be sufficient to specify the pressure of the flammable "
               "material entering the containment and calculating the release "
               "rate at the maximum pressure for the purposes of defining the "
               "limited release (see Chapter 4)."))
    b.append(note("<b>Note on printed wording.</b> The print reads 'release is "
                  "possible. and To be considered as limited release', with a "
                  "lowercase 'and' after a full stop and a capital 'To'. This "
                  "is a source typo; the printed form is retained in English "
                  "and the Vietnamese follows the intended construction."))
    b.append(p("In addition to limited release caused by leaks, there are "
               "cases, such as those in chromatographs, where flammable "
               "material is deliberately released. In such cases it should be "
               "relatively easy to define the maximum release rate in the "
               "worst operating conditions. It should be noted, however, that "
               "further restrictions exist where the release is deliberate "
               "where the only form of pressurization acceptable is "
               "pressurization with continuous dilution using air."))
    b.append(p("The volume of air required to ensure that the gas mixture "
               "leaving the enclosure is less than 25 per cent lower explosive "
               "limit can be calculated if the volume of gas released is known "
               "together with the percentage of flammable material in that "
               "gas. The formula for this is:"))
    b.append(p("Q₁ = Q₂ × (Y₁/100) × (100/Y₂) × (100/F)    m³/hour"))
    b.append(p("where Q₁ = Minimum flowrate of protective gas    m³/hour"))
    b.append(p("Q₂ = Maximum release rate of gas or vapour    m³/hour"))
    b.append(p("Y₁ = Volumetric percentage of flammable material in the "
               "release    % v/v"))
    b.append(p("Y₂ = Volumetric lower explosive limit of the flammable "
               "material in air    % v/v"))
    b.append(p("F = The percentage lower explosive limit required (25 per "
               "cent in this case)    % v/v"))

    # Printed p.287.
    b.append(p("Where there is more than one flammable material in the "
               "released mixture, the amount of air should be calculated for "
               "each component individually and then the quantities added to "
               "give the required minimum airflow."))

    # Unnumbered subhead, printed p.287.
    b.append(h4("Containment with unlimited release",
                "Containment with unlimited release"))
    b.append(p("This description addresses containment that, if it released "
               "gas or vapour would be called containment with limited "
               "release, releases flammable liquid which can evolve "
               "flammable vapours at rates which cannot be quantified with "
               "confidence.In such cases, obviously, while the liquid release "
               "rate can be defined the rate of vaporization is not so easy "
               "to specify. Therefore it is not possible to effectively "
               "dilute the vapour produced with confidence."))
    b.append(note("<b>Note on printed wording.</b> The print reads 'with "
                  "confidence.In such cases, obviously,' with no space after "
                  "the full stop. The printed form is retained in English; "
                  "the Vietnamese inserts the space for readability."))
    b.append(p("Where this occurs there may also be oxygen entrained (usually "
               "as air) in the release and the use of inert gas pressurization "
               "with continuous gas flow, which is the only option acceptable "
               "here, must ensure that the mixture leaving the enclosure does "
               "not contain more than 2 per cent oxygen by volume. The mixture "
               "of vapour and oxygen at the point of release must not contain "
               "more than 21 per cent oxygen. The objective of this latter "
               "requirement is to allow only entrained air in the release, as "
               "any gas entrained with a higher level of oxygen could cause "
               "this criterion not to be met if vaporization rates of the "
               "liquid were low."))
    b.append(p("Calculation of the minimum flow of inert gas to reduce the "
               "oxygen content of a release to the required 2 per cent may be "
               "carried out in the same way as the air dilution already "
               "discussed:"))
    b.append(p("Q₁ = Q₂ × 100/Y₁    m³/hour"))
    b.append(p("where Q₁ = Minimum flowrate of inert gas    m³/hour"))
    b.append(p("Q₂ = Volume of oxygen in the release    m³/hour"))
    b.append(p("Y₁ = Percentage oxygen permitted in outlet from enclosure "
               "(2 per cent in this case)    % v/v"))

    # Printed pp.287-288. Section 11.5 and 11.5.1.
    b.append(h3("11.5 Enclosures, ducting and internal components",
                "11.5 Enclosures, ducting and internal components"))
    b.append(h4("11.5.1 Enclosures", "11.5.1 Enclosures"))
    b.append(p("The enclosures used for pressurized apparatus are required to "
               "be sufficiently strong to withstand normal use without "
               "damage, in common with other protection concepts, and may be "
               "manufactured of metallic or non-metallic materials provided "
               "that, if non-metallic, the material of construction is not "
               "adversely affected by either the pressurization medium or any "
               "flammable material released in the enclosure. The strength of "
               "enclosures must also be such that they are not damaged by the "
               "maximum pressure which can occur in service. While an easy "
               "method of achieving this is to specify a maximum pressure and "
               "then leave it to the installer to ensure that it is not "
               "exceeded, such an approach is not practical. In many cases it "
               "is easier to install an over-pressure relief device in the "
               "enclosure so that if there is any unwanted pressure elevation "
               "in service the enclosure is automatically safeguarded."))
    b.append(p("A requirement for the enclosure to be weather proof is not "
               "necessary as the pressurization requirements will effectively "
               "prevent the ingress of moisture. Prevention of entry of solid "
               "foreign bodies, however, remains necessary as these may still "
               "enter due to their nature and, unlike moisture, will not be "
               "easily removed by purging if they enter prior to "
               "energization."))
    b.append(note("<b>Note on printed wording.</b> The print uses 'weather "
                  "proof' as two words. The printed form is retained in "
                  "English."))
    b.append(p("A requirement is for the enclosure to have an integrity of "
               "not less than IP40 in accordance with BS/EN 60529⁸ in the "
               "absence of the pressurizing gas. In the case of rotating "
               "machines where IP-ratings are defined slightly differently, "
               "due to the nature of such apparatus, the Standard used is EN "
               "60034-5, which is published in the UK as BS 4999, Part 105.⁹"))
    b.append(note("<b>Note on footnote markers and OCR.</b> The print shows "
                  "'BS/EN 60529⁸' and 'BS 4999, Part 105.⁹' with superscript "
                  "footnote markers; the OCR layer merges the digits into the "
                  "designations ('605298', 'Part 105.9') and inserts spaces "
                  "into section numbers such as '11.5.1'. The printed "
                  "superscripts and correct section numbering are kept."))
    b.append(p("When considering the IP-rating of the enclosure, the "
               "deliberate apertures for inlet and outlet of the purge gas "
               "may be ignored. These, however, must be sited to ensure "
               "adequate purging and the avoidance of dead spots where any "
               "flammable gas or vapour may dwell even after purging. This "
               "may only require careful siting of single apertures in each "
               "case but may, where enclosure shapes are complex or "
               "components create divisions in the enclosure, need several "
               "inlet and outlet apertures. The choice is one which can only "
               "be made individually but it is not likely that multiple "
               "apertures will be the norm."))
    b.append(p("Where outlet apertures are fitted to enclosures which are "
               "pressurized by static pressurization or pressurization with "
               "leakage compensation, these must be arranged so that they can "
               "be closed or sealed after purging by devices which form part "
               "of the apparatus."))
    b.append(p("It is recognized that the apparatus will, in common with "
               "other types of apparatus, be fitted with doors and covers "
               "which permit access to the interior of the enclosure. The "
               "ideal method of dealing with these in the case of "
               "pressurization with leakage compensation, and pressurization "
               "with continuous dilution, is to utilize an interlock which "
               "isolates the electrical supplies and any other electrical "
               "connections (see Fig. 11.2) when the door or cover is opened. "
               "Because this would limit the opportunity for adjustment it is "
               "possible to introduce an interlock defeat system (see Fig. "
               "11.3) which would permit competent persons to open the "
               "enclosures, under a system of control, for adjustment and "
               "similar purposes without electrical isolation. After such "
               "work, when the enclosure is reclosed it is important that the "
               "system goes through its full purge cycle to remove any gas "
               "which has entered, although it is not necessary to isolate "
               "the electrical supplies during this period."))
    b.append(p("Where a tool or key is required to open doors or remove "
               "covers isolation is not necessary, but the purge cycle needs "
               "initiating after reclosure. In this case it will have to be "
               "done manually. A device can be fitted which recognizes "
               "opening or removal, and isolates electrical supplies with an "
               "override as already described. The tool or key requirement in "
               "this case does not indicate any requirement for "
               "‘special fasteners’ or the like (see Chapter 8)."))
    b.append(p("In the case of static pressurization, doors and covers will "
               "not be provided for adjustment after pressurization due to "
               "the nature of the approach. All"))
    b.append(note("<b>Note on the source span.</b> The assigned source ends "
                  "mid-sentence at '...due to the nature of the approach. "
                  "All'; the continuation of that sentence is on printed "
                  "p.289 and belongs outside this module. The printed "
                  "fragment is kept verbatim."))

    # Printed p.289: Figs 11.2 and 11.3 occupy the page after the prose.
    b.append(fig(2, F.fig_f1102()))
    b.append(fig(3, F.fig_f1103()))
    return "".join(b)
