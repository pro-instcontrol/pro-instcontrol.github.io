# -*- coding: utf-8 -*-
"""Chapter 10, module G — continuation of 10.3.5 Component parts.

Printed pp. 264-268 (PDF pp. 285-289), raw LF 11890-12072: tail of the
arcing/sparking paragraph, Obstacles near flamepaths, Liquids, Breathing and
draining devices, Cable glands with Figs 10.23-10.24, and the opening of
Stopping boxes. The stopping-box paragraph continues in module H.
"""
from mcmillan_common import h3, h4, p, note, fig
import mcmillanfig10c as FC


def body_vi():
    b = []
    b.append(p("thông tin trong chương này có thể không đủ để bảo đảm vỏ bọc đạt "
               "tính chống cháy. Khó có thể hình dung làm thế nào các bộ phận đó lại có thể "
               "được bố trí ở vị trí gần tương tự các mối nối mở rộng và mối nối trụ, nhưng "
               "trong những trường hợp đặc biệt mà vị trí đặt như vậy được xác định thì các "
               "vấn đề tương tự lại phát sinh."))

    b.append(h4("Chướng ngại vật gần đường ngọn lửa", "Obstacles near flamepaths"))
    b.append(p("Các chướng ngại vật đặt gần đường ngọn lửa của vỏ chống cháy cũng được biết "
               "là ảnh hưởng đến mặt trước ngọn lửa và cho phép ngọn lửa truyền qua trong khi "
               "lẽ ra không xảy ra nếu không có chúng. Điều này quan trọng khi chế tạo vỏ "
               "chống cháy mà các bộ phận của vỏ có thể có các vật khác gắn lên (ví dụ, một "
               "điện thoại chống cháy). Đã thực hiện nhiều công việc về vấn đề này, chủ yếu để "
               "khắc phục các vấn đề lắp đặt, nhưng các giải pháp tìm ra cũng áp dụng tương tự "
               "cho người chế tạo. Để tránh khả năng một vỏ bọc có các thiết bị gắn ngoài — "
               "dù nếu không có chúng vỏ vẫn đáp ứng các yêu cầu đối với vỏ chống cháy — "
               "không đạt các thử nghiệm truyền ngọn lửa, không được đặt chướng ngại vật nào "
               "trong vùng thoát của đường ngọn lửa trong vòng 1 cm từ mép đường ngọn lửa đối "
               "với nhóm phụ IIA, trong vòng 3cm từ mép đường ngọn lửa đối với nhóm phụ IIB, "
               "hoặc trong vòng 4cm từ mép đường ngọn lửa đối với nhóm phụ IIC."))

    b.append(h4("Chất lỏng", "Liquids"))
    b.append(p("Vỏ chống cháy có thể chứa thiết bị hoặc cần chất lỏng để hoạt động (ví dụ, "
               "các thiết bị điện thủy lực), hoặc hoạt động nhờ chất lỏng (ví dụ, một máy sắc "
               "ký). Những tình huống này không bị cấm, nhưng phải cẩn thận bảo đảm rằng bất kỳ "
               "chất lỏng nào xâm nhập không bị phân hủy do bất kỳ tình huống nào xảy ra bên "
               "trong vỏ, kể cả trong điều kiện bất thường, và tạo ra hơi thuộc nhóm phụ nguy "
               "hiểm hơn nhóm phụ mà vỏ được thiết kế. Trong những trường hợp đó, vỏ phải được "
               "thiết kế cho nhóm phụ nguy hiểm hơn vì hơi sinh ra có thể thoát ra ở các mặt "
               "bích và tạo thành môi trường nổ bên ngoài, ngoài việc có mặt bên trong vỏ."))
    b.append(p("Bất kỳ chất lỏng hoặc khí nào bên trong vỏ mà có thể bị tăng áp không được "
               "làm tăng áp cho vỏ nếu được giải phóng vào bên trong, nếu không có thể xảy ra "
               "hiệu ứng tương tự như pressure piling (chồng áp suất). Nếu chất lỏng hoặc khí "
               "dưới áp suất được phép có bên trong vỏ thì phải có phương pháp thông hơi hoặc "
               "xả để bảo đảm vỏ không bị tăng áp trong trường hợp xấu nhất là giải phóng bên "
               "trong. Phương pháp thông hơi hoặc xả phải duy trì tính chống cháy của vỏ và "
               "tuân theo các yêu cầu kết cấu cụ thể."))

    b.append(h4("Thiết bị thông hơi và xả", "Breathing and draining devices"))
    b.append(p("Thiết bị thông hơi và xả dùng để xả chất lỏng và khí từ vỏ mà không làm tăng "
               "áp suất đáng kể. Chúng không được dùng ở nơi chất lỏng hoặc khí giải phóng bên "
               "trong vỏ làm tăng áp suất bên trong quá 1 × 10⁴ N/m², và cũng không được dùng "
               "để giảm áp suất bên trong do một vụ nổ gây ra, dù bản thân chúng có thể chịu "
               "được vụ nổ như vậy. Do đó, vỏ mà áp suất bên trong tăng do chất lỏng hoặc khí "
               "giải phóng bên trong phải chịu được áp suất bên trong phát sinh khi không có "
               "thiết bị (bị bịt), và không được truyền vụ nổ ra môi trường bên ngoài. Điều "
               "này đòi hỏi các yêu cầu kết cấu đặc biệt không nằm trong các yêu cầu đối với vỏ "
               "chống cháy. Áp suất bên trong do một vụ nổ bên trong sinh ra cũng phải được "
               "xem xét như áp suất xảy ra khi thiết bị bị bịt."))
    b.append(note("<b>Ghi chú của người dịch.</b> Bản in ghi 'liquid core gas'; nghĩa đúng là "
                  "'liquid or gas' (chất lỏng hoặc khí). Bản tiếng Anh giữ nguyên cụm từ in."))
    b.append(p("Do kết cấu của chúng (sẽ được mô tả sau), thiết bị thông hơi và xả thường được "
               "chế tạo bằng đồng hoặc đồng thau. Dù điều này nhìn chung được chấp nhận, cần "
               "lưu ý rằng đồng khi có acetylene có thể tạo thành các acetylide đồng, về thực "
               "chất là các chất nổ rắn. Vì lý do này, các thiết bị chứa đồng hoặc hợp kim có "
               "chứa hơn 60 phần trăm đồng không được phép dùng trong thiết bị thông hơi hoặc "
               "xả cho vỏ dùng trong các ứng dụng mà có thể có acetylene. Điều này là cần thiết "
               "vì, dù người sử dụng sẽ nhận biết vỏ chứa đồng là không phù hợp và không dùng "
               "chúng, có thể không rõ ràng rằng một thiết bị thông hơi hoặc xả chứa đồng đang "
               "được lắp trên một vỏ mà nếu không có thiết bị đó thì hoàn toàn không chứa đồng."))
    b.append(note("<b>Ghi chú của người dịch.</b> Câu in 'it may not be clear to that a "
                  "copper-containing breathing or draining device …' bị thiếu tân ngữ sau 'to "
                  "that'; bản dịch diễn đạt theo ý nghĩa tự nhiên, bản tiếng Anh giữ nguyên câu "
                  "in."))
    b.append(p("Có hai loại thiết bị thông hơi hoặc xả, đó là loại có đường ngọn lửa có thể đo "
               "được qua các khe hở và loại mà các đường này không thể đo được."))
    b.append(p("Các yêu cầu đối với thiết bị thông hơi và xả mà mọi kích thước đều đo và kiểm "
               "soát được để bảo đảm mỗi phép đo lặp lại được trong một dung sai cụ thể hoặc theo "
               "một giá trị tối đa cụ thể thì khá đơn giản. Các khe hở và khe hở nhỏ đo được "
               "không cần tuân thủ các kích thước khe hở đã nêu trước đó trong chương này đối "
               "với khe hở mặt bích, khe hở mở rộng và khe hở trụ, miễn là thiết bị không truyền "
               "vụ nổ bên trong ra môi trường bên ngoài khi được thử theo cách tương tự như các "
               "khe hở đó và, thêm vào đó, thiết bị chịu được vụ nổ bên trong vỏ mà không hư "
               "hỏng khi thử áp suất được áp dụng cho vỏ với thiết bị bị bịt."))
    b.append(p("Như thường lệ, trong mọi phân loại đều có ngoại lệ và trong trường hợp này "
               "thiết bị thông hơi và xả dải kim loại cuộn (crimped-ribbon) là một ngoại lệ. "
               "Các thiết bị này có thể có khe hở bên trong mà kích thước tối đa và tối thiểu "
               "có thể quy định được, và trong trường hợp này chúng là thiết bị thông hơi và xả "
               "có khe hở đo được. Trong những trường hợp như vậy, chúng được thử về khả năng "
               "truyền vụ nổ bên trong ra môi trường bên ngoài với khe hở tối đa cho phép. Tuy "
               "nhiên, vật liệu chế tạo của chúng bị hạn chế ở chỗ không vật liệu nào được dùng "
               "chứa magiê, nhôm hoặc titan, vì các vật liệu này hoạt động mạnh, có thể cháy và "
               "do đó ảnh hưởng bất lợi đến hoạt động của thiết bị theo cách không định lượng "
               "được. Người ta thể hiện sự ưu tiên đối với cupronickel hoặc thép không gỉ nhưng "
               "không bắt buộc, miễn là kim loại dùng không bị phản ứng với các khí liên quan vì "
               "điều đó sẽ ảnh hưởng bất lợi đến hoạt động của thiết bị xét về tính chống cháy "
               "(flameproofness) của nó."))
    b.append(p("Có một số loại thiết bị thông hơi và xả mà khe hở và khe hở nhỏ của chúng không "
               "thể đo được, và cần một chiến lược thay thế để xác định chúng theo khả năng "
               "truyền vụ nổ bên trong ra môi trường bên ngoài. Cách tiếp cận được dùng là xác "
               "định kích thước tổng thể của các thiết bị. Sau đó xác định mật độ của chúng theo "
               "BS 5600 Part 3¹⁶, rồi đến kích thước lỗ xếp bọt khí (bubble pore size) theo "
               "cùng tiêu chuẩn Anh này. Dù tiêu chuẩn đó liên quan đến các phần tử kim loại "
               "thiêu kết, các phương pháp xác định vẫn có thể dễ dàng áp dụng cho các loại "
               "thiết bị thông hơi và xả khác. Việc xác định và quy định hai thông số này sẽ "
               "xác định đầy đủ hoạt động của các thiết bị để tạo sự tin cậy vào tính chất "
               "chống cháy của chúng, miễn là chúng đáp ứng các yêu cầu chống cháy trong các thử "
               "nghiệm kiểu về truyền nổ."))
    b.append(note("<b>Ghi chú của người dịch.</b> Chỉ số trên số 16 trong 'BS 5600 Part 3¹⁶' là "
                  "ký hiệu tham chiếu tài liệu, không phải một phần của tên tiêu chuẩn; cùng "
                  "trang này sau đó trích dẫn 'BS 5600, Part 3' có dấu phẩy."))
    b.append(p("BS/EN 50018 đặt ra yêu cầu đối với các phương pháp xác định độ xốp hoặc độ thẩm "
               "thấu chất lỏng, những yếu tố quyết định hiệu quả của thiết bị như một thiết bị "
               "thông hơi hoặc xả, và yêu cầu các phương pháp đó được xác định theo BS 5600, "
               "Part 3. Lý do là hoạt động của thiết bị thông hơi hoặc xả có liên quan đến áp "
               "suất có thể phát triển bên trong vỏ trước khi một vụ nổ bên trong bắt đầu. Nếu "
               "thiết bị hoạt động không hiệu quả thì việc chất lỏng xâm nhập vào vỏ là không "
               "chấp nhận được vì nó có thể dẫn đến tăng áp sơ bộ (pre-pressurization)."))
    b.append(p("Các phần tử có khe hở không đo được phải tuân theo bốn yêu cầu kết cấu cơ bản. "
               "Thứ nhất, các phần tử dải kim loại cuộn phải, như đối với các phần tử có khe hở "
               "đo được, bằng kim loại và magiê, nhôm, titan hoặc hợp kim chứa các vật liệu này "
               "là không được chấp nhận. Người ta thể hiện sự ưu tiên đối với cupronickel hoặc "
               "thép không gỉ nhưng việc dùng các kim loại này không bắt buộc, miễn là kim loại "
               "hoặc hợp kim chọn không phản ứng với các chất lỏng hiện diện theo cách ảnh hưởng "
               "bất lợi đến tính chất chống cháy của thiết bị. Đặc biệt, khi có acetylene, phải "
               "tuân thủ giới hạn trên 60 phần trăm đồng trong bất kỳ hợp kim nào dùng để tránh "
               "các acetylide đồng, có xu hướng hoạt động như các chất nổ rắn."))
    b.append(note("<b>Ghi chú của người dịch.</b> Mệnh đề in 'shall, as for those with "
                  "measurable elements, of metal and magnesium, aluminium, titanium … are not "
                  "acceptable' bị lỗi ngữ pháp; ý nghĩa đúng là các phần tử phải bằng kim loại, "
                  "còn magiê, nhôm, titan và hợp kim chứa các kim loại này thì không được chấp "
                  "nhận. Bản tiếng Anh giữ nguyên câu in."))
    b.append(p("Thứ hai, các phần tử dây ép (pressed wire) phải bằng kim loại và đáp ứng các yêu "
               "cầu tương tự như phần tử dải kim loại cuộn về vật liệu chế tạo. Kết cấu ban đầu "
               "của chúng cũng phải bắt đầu bằng việc nén dây hoặc bện dây vào một khuôn để tạo "
               "thành ma trận đồng nhất, sau đó có thể xem như vật liệu rắn cho việc gia công "
               "tiếp theo."))
    b.append(p("Thứ ba, thiết bị kim loại thiêu kết có thể được chế tạo từ bất kỳ kim loại nào "
               "nhưng các hạn chế áp dụng cho phần tử dây ép cũng áp dụng cho chúng. Kim loại "
               "ưu tiên trong trường hợp này là thép không gỉ hoặc, khi không có acetylene, "
               "đồng - thiếc 90/10."))
    b.append(p("Thứ tư, kết cấu của các phần tử bọt kim loại cụ thể hơn nhiều vì phương pháp "
               "sản xuất bọt kim loại. Các phần tử cần được sản xuất bằng cách phủ nickel lên "
               "bọt polyurethane dạng lưới, sau đó loại bỏ polyurethane bằng phân hủy nhiệt. "
               "Nickel sau đó phải được chuyển thành hợp kim nickel/chrome bằng một quá trình "
               "như khuếch tán khí, rồi nén bọt kim loại thu được. Sau khi nén, các thiết bị "
               "phải chứa ít nhất 15 phần trăm chrome theo trọng lượng."))

    b.append(h4("Đầu bịt cáp", "Cable glands"))
    b.append(p("Đầu bịt cáp dùng trong vỏ chống cháy có thể thuộc hai loại: đầu bịt nén thông "
               "thường có vòng đệm (xem Hình 10.23), hoặc đầu bịt dùng hợp chất bịt kín (xem "
               "Hình 10.24). Loại được chọn tùy thuộc vào loại cáp dùng cho một lắp đặt cụ thể, "
               "vì đầu bịt nén chỉ phù hợp khi có thể bịt kín hiệu quả các khe hở của cáp bằng "
               "cách nén. Trong cả hai trường hợp, ren trên phần đầu bịt được vặn vào vỏ phải "
               "đáp ứng các yêu cầu đối với mối nối ren và, thêm vào đó, phải dài ít nhất 8mm "
               "và gồm ít nhất sáu ren đầy để bảo đảm mức tối thiểu năm ren quy định cho một mối "
               "nối ren. Nếu đầu bịt có một rãnh lõm (undercut) để bảo đảm đáy của nó bằng phẳng "
               "với thành vỏ, phải có vòng đệm và vòng này phải đủ không nén được để rãnh lõm "
               "không lọt vào ren cái và làm giảm chiều dài ren ăn khớp xuống dưới năm ren."))
    b.append(fig(23, FC.fig_f1023()))
    b.append(fig(24, FC.fig_f1024()))
    b.append(p("Đầu bịt nén dùng cho mục đích chung phải có khả năng chấp nhận một dải vòng đệm "
               "có cùng đường kính ngoài nhưng đường kính trong khác nhau, phù hợp với kích "
               "thước cáp mà chúng được thiết kế. Các vòng đệm này phải có chiều dài trục chưa "
               "nén là 20 mm đối với cáp có đường kính nhỏ hơn 20 mm (chu vi 60 mm đối với cáp "
               "không tròn), tăng lên 25 mm đối với cáp lớn hơn. Nếu đầu bịt được thiết kế chỉ "
               "nhận một vòng đệm và chỉ định cho một đường kính cáp duy nhất, chiều dài trục "
               "có thể giảm xuống 5 mm, miễn là vỏ không định dùng trong nhóm phụ IIC và không "
               "có thể tích lớn hơn 2000 cm³."))
    b.append(p("Các đầu bịt cáp có vòng đệm phải chịu thử áp suất thủy lực với vòng đệm được "
               "bịt kín trên một trục gá (mandrill) và 30 × 10⁵ N/m² được áp dụng ở một phía "
               "của vòng đệm. Rò rỉ chất lỏng sau đó được xác định bằng các giọt từ phía kia rơi "
               "lên giấy thấm."))
    b.append(p("Đầu bịt cáp dùng hợp chất bịt kín được bố trí sao cho chỉ các lõi dẫn, sau khi "
               "loại bỏ lớp vỏ bọc và vật liệu độn lót toàn phần (lớp vỏ trong đối với cáp bọc "
               "thép), đi qua hợp chất. Cần bảo đảm có đủ hợp chất bịt kín, với số lõi lớn nhất "
               "có kích thước lớn nhất mà đầu bịt được thiết kế đi qua phần tử bịt kín. Để làm "
               "được điều đó, phần tử bịt kín phải được cấu tạo sao cho luôn có ít nhất 20 phần "
               "trăm tiết diện của phần tử được lấp đầy bằng hợp chất bịt kín."))
    b.append(p("Các đầu bịt cáp dùng hợp chất bịt kín cũng chịu một thử nghiệm thủy lực tương tự "
               "về bịt kín, trong đó áp dụng áp suất 30×10⁵ N/m² cho chất lỏng tiếp xúc với một "
               "đầu của vòng đệm và kiểm tra các giọt chất lỏng rơi lên giấy thấm từ đầu kia của "
               "vòng đệm."))

    b.append(h4("Hộp bịt", "Stopping boxes"))
    b.append(p("Hộp bịt chỉ đơn giản là một thiết bị mà các dây dẫn đi qua (tức là không phải "
               "cáp mà chỉ là các dây dẫn), sau đó được lấp đầy bằng"))
    return "".join(b)


def body_en():
    b = []
    b.append(p("the information in this chapter may not be sufficient to ensure that an "
               "enclosure is flameproof. It is difficult to see how such parts could be placed "
               "in similar proximity to spigot and cylindrical parts, but in exceptional "
               "circumstances where such possible siting is identified the same problems "
               "arise."))

    b.append(h4("Obstacles near flamepaths", "Obstacles near flamepaths"))
    b.append(p("Obstacles placed near flamepaths of flameproof enclosures are likewise known to "
               "affect the flamefront and allow transmission of flame where none would occur in "
               "their absence. This is important when constructing a flameproof enclosure where "
               "parts of the enclosure may have other items mounted on them (e.g., a flameproof "
               "telephone). Much work has been done on this problem, mainly to overcome "
               "installation problems, but the solutions identified are just as applicable for "
               "constructors. To avoid the possibility of an enclosure with outside fixtures, "
               "which otherwise satisfies the requirements for flameproof enclosures, failing "
               "flame transmission tests no obstructions should be placed in the exit area of a "
               "flamepath within 1 cm of the flamepath edge for sub-group IIA, within 3cm of the "
               "flamepath edge for sub-group IIB, or within 4cm of the flamepath edge for "
               "sub-group IIC."))

    b.append(h4("Liquids", "Liquids"))
    b.append(p("Flameproof enclosures may contain apparatus which either requires a liquid to "
               "operate (e.g., electrohydraulic devices) or operates on a liquid (e.g., a "
               "chromatograph). These situations are not prohibited but care needs to be taken "
               "to ensure that any liquid entering cannot decompose due to any situation "
               "occurring within the enclosure, even in abnormal conditions, and create a "
               "vapour belonging to a more onerous sub-group than that for which the enclosure "
               "is designed. In these circumstances the enclosure must be designed for the more "
               "onerous sub-group as the vapour produced may exit the enclosure at the flanges "
               "and form the external explosive atmosphere in addition to being present within "
               "the enclosure."))
    b.append(p("Any liquid or gas within the enclosure which may be pressurized must not "
               "pressurize the enclosure if released therein, or an effect similar to pressure "
               "piling may occur. If liquid or gas under pressure is permitted within an "
               "enclosure there must be a method of breathing or draining to ensure that the "
               "enclosure is not pressurized in the worst case of internal release. The method "
               "of breathing or draining needs to maintain the flameproof nature of the "
               "enclosure and is subject to specific construction requirements."))

    b.append(h4("Breathing and draining devices", "Breathing and draining devices"))
    b.append(p("Breathing and draining devices are for draining liquids and gases from an "
               "enclosure without any significant pressure increase. They may not be used where "
               "a liquid core gas released within an enclosure increases the internal pressure "
               "by more than 1 × 10⁴ N/m² and they may not be used to reduce internal pressure "
               "caused by an explosion, even though they themselves may withstand such an "
               "explosion. Therefore, an enclosure where the internal pressure is increased by "
               "liquid or gas release within it must withstand the internal pressure produced "
               "in the absence (blockage) of the device, and must not transmit the explosion to "
               "the outside atmosphere. This will require special construction requirements not "
               "included in those for flameproof enclosures. The internal pressure generated by "
               "an internal explosion must also be considered as that occurring with the device "
               "blocked."))
    b.append(note("<b>Translator's note.</b> The printed text reads 'liquid core gas'; the "
                  "intended meaning is 'liquid or gas'. The printed wording is retained here."))
    b.append(p("Breathing and draining devices, due to their construction (which will be "
               "described later), are often manufactured in copper or brass. While this is "
               "generally acceptable it must be borne in mind that copper in the presence of "
               "acetylene may form copper acetylides, which are in effect solid explosives. For "
               "this reason devices containing copper or of alloys containing more than 60 per "
               "cent copper are not permitted in breathing or draining devices for enclosures "
               "for applications where acetylene may be present. This is necessary because, "
               "although users will identify enclosures containing copper as unsuitable and not "
               "use them, it may not be clear to that a copper-containing breathing or draining "
               "device is present in an otherwise copper-free enclosure."))
    b.append(note("<b>Translator's note.</b> The printed sentence 'it may not be clear to that "
                  "a copper-containing breathing or draining device …' lacks an object after "
                  "'to that'; the meaning is supplied in the Vietnamese translation while the "
                  "printed wording is kept here."))
    b.append(p("There are two types of breathing or draining device, namely those with "
               "measurable flamepaths through their interstices, and those where these paths "
               "cannot be measured."))
    b.append(p("The requirements for breathing and draining devices, whose dimensions are all "
               "measurable and controllable to ensure that each measurement is repeatable within "
               "a specific tolerance or against a specific maximum value, are fairly "
               "straightforward. The measured gaps and interstices need not comply with the gap "
               "dimensions specified earlier in this chapter for flange, spigot and cylindrical "
               "gaps, provided the device does not transmit an internal explosion to the outside "
               "atmosphere when tested in the same manner as these gaps and, in addition, the "
               "device withstands an internal explosion within enclosure without damage when a "
               "pressure test is applied to the enclosure with the device blocked."))
    b.append(p("As with all divisions there are exceptions and in this case the crimped-ribbon "
               "breathing and draining device is one. These devices may have gaps within them "
               "which can be specified as to their maximum and minimum sizes and in this case "
               "they are breathing and draining devices with measurable gaps. In such cases "
               "they are tested for their ability to transmit an internal explosion to the "
               "outside atmosphere with the maximum gaps permitted. Their material of "
               "construction is, however, restricted in that no material used may contain "
               "magnesium, aluminium or titanium because these materials are active in that "
               "they can burn and, therefore, adversely affect the performance of the device "
               "in an unquantifiable manner. A preference for cupronickel or stainless steel is "
               "expressed but this is not mandatory, provided that the metal used is not "
               "subject to any reaction with the gases involved as this would adversely affect "
               "the performance of the device insofar as its flameproofness is concerned."))
    b.append(p("There are several types of breathing and draining device whose gaps and "
               "interstices cannot be measured and an alternative strategy is necessary to "
               "define these with regard to their ability to transmit an internal explosion to "
               "the outside atmosphere. The approach used is to define the overall dimensions "
               "of the devices. Their density in accordance with BS 5600 Part 3¹⁶ is then "
               "determined, followed by their bubble pore size in accordance with the same "
               "British Standard. Although this Standard is concerned with sintered metal "
               "elements, the determination methods can be readily applied to other types of "
               "breathing and draining device. Determination and specification of these two "
               "parameters will adequately define the performance of the devices for the "
               "purposes of confidence in their flameproof properties, provided that they "
               "satisfy the flameproof requirements on explosion transmission type tests."))
    b.append(note("<b>Translator's note.</b> The superscript 16 in 'BS 5600 Part 3¹⁶' is a "
                  "reference marker, not part of the standard designation; the same page later "
                  "cites 'BS 5600, Part 3' with a comma."))
    b.append(p("BS/EN 50018 places requirements on the methods used for determination of "
               "porosity or fluid permeability which determine the effectiveness of the device "
               "as a breathing or draining device, requiring them to be determined in "
               "accordance with BS 5600, Part 3. The reason for this is that the performance of "
               "the device as a breathing or draining device is pertinent to the pressure which "
               "can be developed within the enclosure prior to the initiation of an internal "
               "explosion. If the device does not perform effectively then the entry of fluids "
               "into the enclosure is not acceptable as it could lead to pre-pressurization."))
    b.append(p("Elements with non-measurable gaps are subject to four basic constructional "
               "requirements. First, crimped-ribbon elements shall, as for those with "
               "measurable elements, of metal and magnesium, aluminium, titanium, or alloys "
               "containing these materials are not acceptable. A preference for cupronickel or "
               "stainless steel is expressed but use of these metals is not mandatory, provided "
               "the metal or alloy chosen does not react with the fluids present in a way which "
               "would adversely affect the flameproof properties of the device. In particular, "
               "where acetylene is involved the upper limit of 60 per cent copper in any alloy "
               "used must be observed to avoid copper acetylides, which tend to behave as solid "
               "explosives."))
    b.append(note("<b>Translator's note.</b> The printed clause 'shall, as for those with "
                  "measurable elements, of metal and magnesium, aluminium, titanium … are not "
                  "acceptable' is ungrammatical; the intended sense is that the elements shall "
                  "be of metal and that magnesium, aluminium, titanium and alloys containing "
                  "them are not acceptable. The printed wording is retained here."))
    b.append(p("Second, pressed wire elements are required to be metal and to satisfy the same "
               "requirements as crimped-ribbon elements, as far as their materials of "
               "construction are concerned. Their initial construction must also begin by the "
               "compression of the wire or wire braid into a die to form a homogeneous matrix "
               "which can then be treated as a solid material as far as further machining is "
               "concerned."))
    b.append(p("Third, sintered metal devices may be constructed of any metal but the same "
               "restrictions as for pressed wire elements apply to these. The preferred metals "
               "in this case are stainless steel or, where acetylene is not present, 90/10 "
               "copper - tin bronze."))
    b.append(p("Fourth, the construction of metal-foam elements is much more specific because "
               "of the method of production of as metal foam. The elements need to be produced "
               "by coating a reticulated polyurethane foam with nickel and then removing the "
               "polyurethane by thermal decomposition. The nickel must then be converted into "
               "nickel/chrome alloy by a process such as gaseous diffusion and subsequent "
               "compression of the metal foam produced. After compression the devices should "
               "contain at least 15 per cent chromium by weight."))

    b.append(h4("Cable glands", "Cable glands"))
    b.append(p("Cable glands used in flameproof enclosure may be of two types; a normal "
               "compression gland with a sealing ring (see Fig. 10.23), or a gland using a "
               "sealing compound (see Fig. 10.24). The type chosen depends upon the type of "
               "cable used for a particular installation, in that a compression gland is only "
               "suitable where effective sealing of the cable interstices is possible by "
               "compression. In both cases the thread on the part of the gland which is screwed "
               "into the enclosure is required to satisfy the requirements for threaded joints "
               "and, in addition, required to be at least 8mm long and comprise at least six "
               "full threads to ensure the five thread minimum specified for a threaded joint. "
               "If the gland has an undercut to ensure that its base is flush with the enclosure "
               "side, washer must be provided and be sufficiently non-compressible to ensure "
               "that the undercut does not enter the female thread and reduce the engaged "
               "thread length to less than five threads."))
    b.append(fig(23, FC.fig_f1023()))
    b.append(fig(24, FC.fig_f1024()))
    b.append(p("A compression gland for general use will be capable of accepting a range of "
               "sealing rings all with the same outside diameter but with differing internal "
               "diameters, matched to the size of cable for which they are designed. These "
               "sealing rings are required to have an uncompressed axial length of 20 mm for "
               "cables of less than 20 mm diameter (60 mm circumference for non-circular "
               "cables), rising to 25 mm for larger cables. If the gland is designed to accept "
               "only one sealing ring and is intended for one cable diameter only, the axial "
               "length may be reduced to 5 mm, provided the enclosure is not intended for use "
               "in sub-group IIC and does not have a volume greater than 2000 cm³."))
    b.append(p("Cable glands with sealing rings are subjected to a hydraulic pressure test with "
               "the sealing ring sealed onto a mandrill and 30 × 10⁵ N/m² applied to one side "
               "of the seal. Liquid leakage is then identified by drips from the other side "
               "onto blotting paper."))
    b.append(p("A cable gland using a sealing compound is arranged so that only the cores, "
               "after removal of the overall sheath and bedding elements (the inner sheath in "
               "the case of armoured cables), pass through the compound. It is necessary to "
               "ensure that sufficient sealing compound is present, with the maximum number of "
               "cores of the maximum size for which the gland is intended passing through the "
               "sealing element. To do this the sealing element should be constructed to ensure "
               "that there is always at least 20 per cent of the cross section of the element "
               "filled with the sealing compound."))
    b.append(p("Cable glands using sealing compounds are subject to a similar hydraulic test of "
               "sealing which involves applying the pressure of 30×10⁵ N/m² to a liquid in "
               "contact with one end of the seal, and looking for drips of liquid onto blotting "
               "paper from the other end of the seal."))

    b.append(h4("Stopping boxes", "Stopping boxes"))
    b.append(p("A stopping box is merely a device through which conductors pass (i.e., not the "
               "cable but only the conductors) which is subsequently filled with"))
    return "".join(b)
