# -*- coding: utf-8 -*-
"""Chapter 5, module E - bilingual reader (EN/VI).

Alan McMillan, *Electrical Installations in Hazardous Areas* (1998),
printed pp. 140-148 (PDF pp. 161-169): the tail of 5.4.2, the dividers
rule, 5.4.3, the single worked Example, sections 5.5-5.7.2 and the
footnote citations. Owns figures 5.14-5.15 and the Example's unnumbered
equation blocks (Equations 4.7, 4.31 and 4.32 are cited by number only).
Unofficial study translation; the shell owns the reference list and the
legal line.
"""
from mcmillan_common import h3, h4, p, note, eq, fig

import mcmillanfig05_b as FB


def body_vi():
    b = []

    # --- 5.4.2 (a), continued from module D ---------------------------------
    b.append(p("Các tình huống này được mô tả trong Hình 5.14. Ảnh hưởng của kiểu "
               "thông gió này cũng có thể được xét đến khi quyết định mức thông "
               "gió chung bổ sung cần thiết cho một vị trí như vậy."))
    b.append(fig(14, FB.fig_f514()))
    b.append(note("<b>Lưu ý về chú giải Hình 5.14.</b> Ghi chú (3) được in là "
                  "'is restricted Table 3.2' — một từ bị thiếu sau 'restricted'; "
                  "cụm từ in được giữ nguyên trong bản vẽ và không được sửa lặng "
                  "lẽ ở đây. Chú giải cũng nêu vận tốc thông gió tại chỗ 2 m/s "
                  "và giá trị tối thiểu 0,5 m."))
    b.append(p("Khi có nguồn phát thải cấp liên tục trong một khu vực không được "
               "thông gió tự do, có thể bố trí thông gió hút tại chỗ (ví dụ, cho "
               "một bể tách dầu/nước trong tòa nhà) để loại bỏ khí hoặc hơi thường "
               "được phát thải. Trừ khi nguồn phát thải có các chế độ phát thải bổ "
               "sung, trong những trường hợp như vậy nó được giảm — đối với khu "
               "vực đang xét — xuống thành nguồn phát thải cấp phụ, trên cơ sở nó "
               "chỉ phát thải vào khu vực khi thông gió tại chỗ bị hỏng. Điều này "
               "giả định thông gió được sửa chữa nhanh chóng nếu bị hỏng; ở đây "
               "cần sửa trong vòng một giờ. Nếu nguồn có thể có các chế độ khác thì "
               "phải xem xét riêng từng chế độ. Khi nguồn phát thải là nguồn điểm "
               "thì, với điều kiện luồng khí quanh nguồn do thông gió đạt ít nhất "
               "0.5 m/s, Vùng 0 sẽ nhỏ hơn 0.5 m."))
    b.append(p("Khi một nguồn phát thải cấp chính được bảo vệ bằng thông gió tại "
               "chỗ, tình huống tương tự như đối với nguồn cấp liên tục, nhưng vì "
               "phát thải không liên tục nên thời gian sửa chữa thông gió có thể "
               "dài hơn; khoảng thời gian trong vòng một ca (tức là tám giờ) được "
               "coi là phù hợp."))
    b.append(p("Khi một nguồn phát thải cấp phụ được bảo vệ bằng thông gió tại "
               "chỗ, thì đối với riêng lần phát thải đó chỉ khu vực ngay tại nguồn "
               "được coi là Vùng 2. Sự cố thông gió trùng đúng với thời điểm phát "
               "thải vật liệu dễ cháy được coi là không xảy ra trong phạm vi phân "
               "loại khu vực, miễn là thông gió được sửa chữa nhanh chóng (lại "
               "trong vòng một ca — tám giờ — là phù hợp). Vùng 2 chỉ giới hạn ở "
               "vùng ngay quanh nguồn phát thải nếu đó là nguồn phát thải duy nhất "
               "trong khu vực. Cần nhấn mạnh một lần nữa rằng do vận tốc phát thải "
               "và lượng vật liệu phát thải từ hầu hết các nguồn cấp phụ, kiểu "
               "giới hạn bằng thông gió nguồn điểm này không dễ áp dụng, hoặc trong "
               "một số trường hợp là không thể."))

    # --- 5.4.2 (b) ---------------------------------------------------------
    b.append(h4("Sử dụng vách ngăn trong tòa nhà cùng với thông gió chọn lọc",
                "Use of dividers in buildings together with selective ventilation"))
    b.append(p("Khu vực nguy hiểm trong một vùng, chẳng hạn như tòa nhà, không được "
               "thông gió tự do cũng có thể được tạo ra nhờ dùng vách ngăn hoặc màn "
               "che, với thông gió được bố trí sao cho luồng khí thường chảy vào "
               "không gian được bao bởi các vách hoặc màn che này. Kỹ thuật này "
               "thường được dùng khi có các hoạt động nạp liệu thủ công và không "
               "thể loại trừ phát thải trong vận hành bình thường."))
    b.append(p("Người ta không coi cách tiếp cận này là chấp nhận được đối với "
               "nguồn phát thải cấp liên tục, vì toàn bộ phần khu vực được bao bởi "
               "vách hoặc màn che sẽ mang phân loại tương ứng với nguồn phát thải, "
               "trong trường hợp này là Vùng 0. Tất nhiên, cách tiếp cận vẫn có thể "
               "dùng khi nguồn phát thải cấp liên tục có thêm thông gió tại chỗ như "
               "đã mô tả trước đó trong chương này."))
    b.append(p("Khi một nguồn phát thải cấp chính nằm trong một vùng không được "
               "thông gió tự do được bao kín thêm bằng vách hoặc màn che sao cho "
               "thông gió trong chỗ được bao kín tạo ra dòng khí nói chung đi vào "
               "qua mọi lỗ mở, thì phân loại của khu vực bên trong vách hoặc màn "
               "che thường là Vùng 1 (nếu thông gió trong khu vực được bao kín là "
               "đủ — xem Chương 4). Tuy nhiên, ảnh hưởng của nguồn phát thải lên "
               "khu vực bên ngoài màn che tương đương với nguồn phát thải cấp phụ, "
               "chỉ cho Vùng 2 ở những khu vực đó. Điều này đương nhiên giả định "
               "rằng sự cố thông gió được khắc phục trong vòng một ca, như trước."))
    b.append(p("Khi một nguồn phát thải cấp phụ nằm trong một vùng không được thông "
               "gió tự do được bao kín thêm bằng vách hoặc màn che đạt được các mục "
               "tiêu nêu trên, thì không cần tính đến nguồn phát thải đó khi xác "
               "định phân loại vùng cho phần còn lại của khu vực, miễn là thông gió "
               "được sửa chữa nhanh chóng sau khi hỏng (chẳng hạn trong vòng một ca "
               "— tám giờ)."))
    b.append(p("Các vách hoặc màn che dùng cho mục đích trên phải có kết cấu kín "
               "khí, ngoại trừ các lỗ mở cố ý hiện diện, chẳng hạn như lối đi, vì "
               "lượng không khí cần thiết nếu không vậy sẽ rất lớn. Đáng chú ý là "
               "màn che dạng dải chồng chéo thẳng đứng đã được dùng thành công "
               "trong hoạt động này."))

    # --- 5.4.3 -------------------------------------------------------------
    b.append(h3("5.4.3 Thông gió độ tin cậy cao",
                "5.4.3 High integrity ventilation"))
    b.append(p("Tất cả những điều trên dựa trên thực tế là thông gió cưỡng bức có "
               "thể hỏng và sự cố là hiện tượng bất thường, do đó chỉ xét đến khi "
               "có nguồn phát thải cấp liên tục hoặc cấp chính. Các loại sự cố "
               "thường gặp là hỏng cơ khí hoặc hỏng điện của chính hệ thống thông "
               "gió. Có thể khắc phục vấn đề này bằng cách nhân đôi hệ thống thông "
               "gió, sao cho sự cố riêng của một hệ thống chỉ đưa hệ thống dự phòng "
               "vào hoạt động. Miễn là sự tách biệt giữa hai hệ thống đủ lớn (ví dụ, "
               "khác bộ phận cơ khí và khác nguồn cấp điện) thì có thể bỏ qua khả "
               "năng cả hai cùng hỏng, vì điều đó đòi hỏi hai sự kiện bất thường "
               "(không cần xét trong phân loại khu vực). Trong những trường hợp như "
               "vậy có thể xác định giới hạn các Vùng trong tòa nhà vì thông gió có "
               "thể được tin cậy, và có thể tiến hành thử nghiệm để cho thấy phạm "
               "vi khu vực nguy hiểm do các phát thải cụ thể tạo ra trong những "
               "trường hợp chưa có kinh nghiệm."))
    b.append(p("Trong những tình huống đó vẫn còn khả năng mất điện toàn bộ, điều "
               "này ít có khả năng trùng với phát thải khi liên quan đến nguồn phát "
               "thải cấp phụ, và trong trường hợp có nguồn phát thải cấp liên tục "
               "hoặc cấp chính thì toàn bộ thiết bị điện sẽ được cắt điện do sự cố. "
               "Trong những hoàn cảnh như vậy, miễn là các bề mặt nóng còn lại trên "
               "thiết bị được xử lý, thì một chu trình xả sạch trước khi cấp điện "
               "cho thiết bị điện sẽ bảo đảm tình huống được chấp nhận. Điều này "
               "đạt được bằng cách tạo độ trễ giữa việc khôi phục luồng khí và việc "
               "cấp điện. Thời gian trễ này phụ thuộc vào hình học của tòa nhà "
               "nhưng nếu tòa nhà được thiết kế tốt để giảm thiểu nguy cơ các túi "
               "không thông gió — như đáng lẽ phải vậy — thì thời gian không cần "
               "vượt quá thời gian cần để một luồng khí tương đương với năm lần "
               "thể tích tòa nhà đi qua."))
    b.append(p("Trong những trường hợp như vậy, phạm vi của mọi khu vực nguy hiểm "
               "có thể được tính trên cơ sở các phương trình trong Chương 4. Phạm "
               "vi khu vực nguy hiểm tạo ra phải dựa trên thể tích hỗn hợp có khả "
               "năng nổ dự kiến."))

    # --- Worked Example -----------------------------------------------------
    b.append(h4("Ví dụ", "Example"))
    b.append(p("<b>Ví dụ.</b> Một thể tích hơi có khối lượng 2.5 × 10<sup>−3</sup> "
               "được phát thải bởi một nguồn phát thải bên trong một tòa nhà có "
               "thông gió độ tin cậy cao. Vật liệu phát thải ở 295 K, có khối lượng "
               "phân tử 50 và giới hạn nổ dưới là 2 %."))
    b.append(note("<b>Lưu ý về đơn vị của khối lượng.</b> Bản in nêu '2.5 × "
                  "10<sup>−3</sup>' mà không kèm đơn vị; theo ngữ cảnh thì đây là "
                  "kg. Giá trị in được giữ nguyên và không gán đơn vị lặng lẽ."))
    b.append(p("Trong tình huống ngoài trời gần mặt đất, phạm vi khu vực nguy hiểm "
               "sẽ được cho bởi Phương trình 4.7 nhân với 1.5 theo Hình 3.3. "
               "Ta được:"))
    b.append(eq("X = 1.5 × 10.8[GT/ME]<sup>0.55</sup> m"))
    b.append(eq("X = 16.2[2.5 × 10 − 03 × 295/50 × 2]<sup>0.55</sup> m"))
    b.append(eq("X = 1.1 (trong tình huống ngoài trời) m"))
    b.append(p("Nếu giả định dùng lượng không khí tối thiểu trong hệ thống thông "
               "gió của khu vực trong nhà thì có thể dùng Phương trình 4.31 và "
               "như sau:"))
    b.append(eq("Q<sub>a</sub> = 0.03 × 2.5 × 10<sup>−3</sup> × 2952/50 × 2 "
                "m<sup>3</sup>/s"))
    b.append(eq("Q<sub>a</sub> = 0.065 m<sup>3</sup>/s"))
    b.append(p("Nếu phòng có thể tích 100 m<sup>3</sup> thì số lần thay không khí "
               "mỗi giây là 6.5 × 10<sup>−4</sup>. Ở lưu lượng thấp như vậy sẽ có "
               "những phần thông gió kém, vì vậy hiệu quả dòng khí thấp được dự "
               "kiến và hệ số f (xem Chương 4) sẽ bằng 5; nếu nguồn phát thải là "
               "nguồn phát thải cấp chính thì k sẽ bằng 0.25. Nếu giờ dùng Phương "
               "trình 4.32 thì ta có thể tích hỗn hợp có khả năng nổ:"))
    b.append(eq("Q = 0.065 × 5/6.5 × 10<sup>−4</sup> × 0.25 m<sup>3</sup>"))
    b.append(eq("Q = 2000 m<sup>3</sup>"))
    b.append(p("Điều này cho phạm vi tuyến tính của khu vực nguy hiểm trong trường "
               "hợp tốt nhất là:"))
    b.append(eq("X = 7.8 m"))
    b.append(p("Do đó, phạm vi khu vực nguy hiểm là khoảng 8 m nếu thể tích là một "
               "hình cầu, nhưng vì nó sẽ không phải là hình cầu do tính định "
               "hướng của thông gió, phạm vi sẽ lớn hơn đáng kể. Ngoài ra, thể "
               "tích phòng cần phải lớn hơn nhiều so với thể tích hỗn hợp nổ, nếu "
               "không toàn bộ phòng sẽ trở thành khu vực nguy hiểm."))
    b.append(note("<b>Lưu ý về các lỗi in trong Ví dụ.</b> (i) Dòng thay số thứ "
                  "nhất in '2.5 × 10 − 03', trong đó số mũ của 10<sup>−3</sup> bị "
                  "xuống cấp thành '− 03'; (ii) dòng Q<sub>a</sub> in '2952' với "
                  "chữ số 2 đặt cùng dòng thay vì ở dạng mũ; (iii) cả ba dòng được "
                  "in với dấu '/' và cách nhóm không rõ ràng — các kết quả 1.1 m, "
                  "0.065 m<sup>3</sup>/s và 2000 m<sup>3</sup> xác nhận mẫu số là "
                  "(50 × 2) và (6.5 × 10<sup>−4</sup> × 0.25); (iv) bản in viết "
                  "'Equation 4.32 from we have', được giữ nguyên trong bản tiếng "
                  "Anh; (v) kết quả thể tích được ký là Q dù Phương trình 4.32 cho "
                  "V<sub>m</sub> — ký hiệu in được giữ nguyên; (vi) dạng rút gọn "
                  "của Phương trình 4.31 in LEL như một thừa số nhưng phép tính "
                  "lại dùng LEL ở mẫu số; (vii) khối lượng được nêu không kèm đơn "
                  "vị (ngầm định là kg); (viii) giá trị trung gian C = 6.5 × "
                  "10<sup>−4</sup> s<sup>−1</sup> chỉ xuất hiện trong thân văn "
                  "bản, không được trình bày dưới dạng phương trình. Không lỗi "
                  "nào được sửa lặng lẽ."))

    # --- 5.5 ---------------------------------------------------------------
    b.append(h3("5.5 Phòng dưới mặt đất", "5.5 Rooms below ground"))
    b.append(p("Các phòng dưới mặt đất phải được xử lý như phòng trên mặt đất "
               "nhưng, vì không thể thông gió tự nhiên qua các lỗ mở, chỉ các giải "
               "pháp thông gió cưỡng bức là khả thi. Việc bố trí cơ chế loại bỏ "
               "hỗn hợp khí/hơi/không khí trong phòng trở nên quan trọng hơn nhiều "
               "vì không có cơ chế nào khác để thay đổi không khí trong phòng. Trừ "
               "khi không khí được thay cưỡng bức trước khi cấp điện cho thiết bị "
               "điện, nguy cơ nổ cao hơn nhiều, vì sự tồn tại của hỗn hợp có khả "
               "năng nổ trong một phòng ngầm không có thông gió cưỡng bức về mặt "
               "lý thuyết là vô hạn."))

    # --- 5.6 ---------------------------------------------------------------
    b.append(h3("5.6 Phòng không có phát thải bên trong nhưng tiếp giáp với khu "
                "vực nguy hiểm bên ngoài",
                "5.6 Rooms without any internal release but which abut external "
                "hazardous areas"))
    b.append(p("Lý tưởng nhất là không có lỗ mở nào trong phần phòng tiếp giáp với "
               "khu vực nguy hiểm bên ngoài, nhưng tình huống lý tưởng như vậy "
               "không phải lúc nào cũng khả thi. Các lắp đặt như ống cáp trong "
               "tường có thể được bịt kín hiệu quả, nhưng thường thì cần có một cửa "
               "trong bức tường mà phía bên kia là khu vực nguy hiểm. Trong những "
               "trường hợp như vậy, giải pháp lý tưởng là tạo tình huống trong đó "
               "hỗn hợp có khả năng nổ không xâm nhập được vào phòng, vì thường thì "
               "cần lắp đặt thiết bị điện có thể là nguồn gây cháy. Tuy nhiên điều "
               "này không phải lúc nào cũng làm được, và kết quả là có nhiều tình "
               "huống khu vực nguy hiểm bên ngoài xâm nhập một phần hoặc toàn bộ "
               "vào phòng. Tình huống chính là phòng có cửa hoặc cửa sổ mở ra khu "
               "vực nguy hiểm."))
    b.append(p("Khi một phòng có lỗ mở tiếp giáp với khu vực nguy hiểm thì, ngay "
               "cả khi lỗ mở là một cửa không được dùng thông thường, nội thất "
               "phòng phải được giả định là bị nhiễm hỗn hợp có khả năng nổ từ "
               "bên ngoài. Vì thông gió bên trong tòa nhà thường không phải là "
               "thông gió tự do, toàn bộ phòng thường phải được giả định là mang "
               "ít nhất phân loại của khu vực bên ngoài."))
    b.append(p("Khi một phòng có cửa thông thường hoặc lỗ mở khác tiếp giáp với "
               "Vùng 1 hoặc 2, toàn bộ phòng phải được giả định là chính nó là "
               "Vùng 1 hoặc 2 (tức là phân loại bên ngoài) ở mức tốt nhất. Nếu "
               "thông gió trong phòng đặc biệt kém thì nội thất sẽ là Vùng 1, ngay "
               "cả khi phân loại bên ngoài là Vùng 2, nhưng tình huống nghiêm "
               "trọng hơn này ít có khả năng xảy ra đối với phòng trên mặt đất "
               "bình thường. Người ta không coi là chấp nhận được việc bất kỳ lỗ "
               "mở nào của phòng tiếp giáp với Vùng 0, vì các vùng này thường được "
               "kỳ vọng là được bao kín."))
    b.append(p("Có thể giảm nhẹ các ảnh hưởng mô tả ở trên trong trường hợp Vùng 1 "
               "và Vùng 2. Ví dụ, nếu phòng có cửa chỉ dùng trong trường hợp khẩn "
               "cấp, có thể lắp cửa về cơ bản kín khí và cho cửa tự đóng hoặc báo "
               "động nếu bị để mở. Các cửa như vậy được giả định là không truyền "
               "khu vực nguy hiểm vào bên trong phòng. Buồng đệm gồm hai cửa tự đóng "
               "cũng được giả định có tác dụng tương tự, cũng như một cửa đơn tự "
               "đóng kín khí kết hợp với cấp khí tươi vào phòng giữ áp suất hơi "
               "dương. Lập luận trong trường hợp sau là ngay cả khi cửa được dùng "
               "thường xuyên thì cũng chỉ có vấn đề nếu thông gió hỏng, và thời "
               "gian cửa mở trong những hoàn cảnh đó ít có khả năng tạo ra tình "
               "huống có lượng khí đáng kể xâm nhập vào phòng, vì nhân viên sẽ "
               "biết rằng thông gió đã hỏng."))
    b.append(p("Giải pháp lý tưởng là thiết kế quá trình hoặc lắp đặt sao cho mọi "
               "bức tường, v.v., tiếp giáp với khu vực nguy hiểm được bịt kín hiệu "
               "quả, và điều này phải làm được trong hầu hết các trường hợp."))

    # --- 5.7 ---------------------------------------------------------------
    b.append(h3("5.7 Các trường hợp đặc biệt", "5.7 Particular circumstances"))
    b.append(p("Thường thì các phòng được dùng cho những trường hợp đặc biệt mà "
               "trong đó có sử dụng vật liệu dễ cháy. Điển hình là buồng phun sơn "
               "(và các phòng tương tự nơi nhân viên làm việc) và lò sấy sơn."))

    b.append(h4("5.7.1 Buồng phun sơn", "5.7.1 The paint spray booth"))
    b.append(p("Trong buồng phun sơn, công nhân thực sự phát thải vật liệu dễ cháy "
               "(dung môi trong sơn) dưới dạng hơi và sương mù trong khi làm việc. "
               "Buồng chắc chắn trở thành khu vực nguy hiểm và, vì việc phun diễn "
               "ra hầu hết thời gian, thông thường là Vùng 0. Súng phun không ở "
               "một chỗ cố định mà di chuyển trong quá trình phun, có nghĩa là "
               "không phần nào của buồng chứa hỗn hợp có khả năng nổ lâu hơn mức "
               "tương ứng với phân loại Vùng 1. Cũng có rủi ro cho công nhân, và "
               "cả hai vấn đề này đòi hỏi thiết kế rất cẩn thận, trong đó luồng "
               "khí được kiểm soát chặt chẽ để bảo đảm dung môi được quét về phía "
               "sau buồng chứ không phát tán khắp nơi. Điều này đạt được bằng cách "
               "giữ vận tốc thông gió tương đối cao và hút qua một lưới (hoặc tương "
               "tự) ở phía sau buồng để làm đồng đều dòng khí. Ngoài ra, hoạt động "
               "phun thường được liên khóa với thông gió để bảo đảm không thể phun "
               "khi thông gió không chạy. Điều này thường đạt được bằng cách tạo "
               "dòng khí màn che ngang qua lối mở của buồng và sắp xếp hoạt động "
               "sao cho việc phun thường hướng về phía sau buồng. Cùng với vận tốc "
               "dòng khí phải lớn hơn 0.5 m/s, điều này tạo ra tình huống mà mọi "
               "Vùng 1 đều nằm trong buồng và trong một đoạn ngắn phía trước nó. "
               "Trong những hoàn cảnh đó, ngay cả khi có luồng khí, cũng thận "
               "trọng khi phân loại một khu vực phía trước buồng là Vùng 1 trong "
               "một đoạn ngắn (chẳng hạn 1 m) và, để tính đến việc phun bị hướng "
               "sai, xác định Vùng 2 trong 3 m phía trước buồng."))
    b.append(p("Hình 5.15 cho thấy phân loại điển hình cho một buồng như vậy. Tuy "
               "nhiên cần nhớ rằng sẽ cần các biện pháp phòng ngừa khác vì lý do "
               "độc hại hoặc các tình huống có nguồn phát thải khác (ví dụ, bình "
               "xăng của phương tiện). Cần tham khảo HSE Note PM 25⁴ về vấn đề "
               "này."))
    b.append(fig(15, FB.fig_f515()))
    b.append(note("<b>Lưu ý về chú giải Hình 5.15.</b> Chú giải in 'A = Grid or mesh "
                  "to increase eveness of airflow' với lỗi chính tả 'eveness' (đáng "
                  "lẽ là 'evenness'); chữ in được giữ nguyên trong bản vẽ. Hình thể "
                  "hiện Vùng 1 trong khoảng 1 m và Vùng 2 trong khoảng 3 m phía "
                  "trước buồng, cùng một vùng 1 m quanh lối thoát của ống dẫn."))

    b.append(h4("5.7.2 Lò sấy sơn", "5.7.2 The paint drying oven"))
    b.append(p("Thiết bị đã sơn thường được sấy trong lò, tạo ra tình huống dung "
               "môi trong sơn bay hơi trong một không gian kín. Điều tệ hơn là luồng "
               "khí qua lò được tuần hoàn lại vì nó được nung nóng đáng kể và chi "
               "phí thông gió khí tươi sẽ rất lớn. Tình huống này làm trầm trọng "
               "thêm vấn đề vì nồng độ vật liệu dễ cháy trong khí sấy tăng dần cho "
               "đến khi đạt trạng thái cân bằng, do một phần được đưa ngược trở lại "
               "lò và cộng thêm vào phần đang bay hơi. Ảnh hưởng này được giảm nhẹ "
               "bởi thực tế là phần lớn dung môi tạo ra bay hơi trong buồng phun "
               "hoặc trong quá trình vận chuyển giữa buồng và lò, và nội thất lò "
               "thường có thể được phân loại là Vùng 1. Vì đây là không gian kín "
               "nên cần các biện pháp phòng ngừa bổ sung và cần tham khảo HSE Note "
               "PM 25⁴."))
    b.append(p("Đường thải của lò phải được phân loại là Vùng 2 để tính đến việc "
               "thông gió có thể phải hút hỗn hợp có khả năng nổ ra khỏi lò lúc "
               "khởi động, nhưng phân loại này chỉ là danh nghĩa vì các dung môi "
               "nói trên có điểm sôi tương đối cao. Do đó, lúc khởi động, chúng ở "
               "nhiệt độ môi trường thấp hơn rất nhiều so với điểm sôi. Nên quy "
               "định khoảng cách 3 m quanh lối thoát."))
    b.append(p("Lò cũng nên được bố trí sao cho trong điều kiện thông gió bình "
               "thường không khí được hút vào qua mọi lỗ mở, chẳng hạn như các lỗ "
               "dùng để đưa mẫu vào, và sau đó nên xác định một khu vực nguy hiểm "
               "danh nghĩa (chẳng hạn) 3 m quanh các lỗ mở này để tính đến các "
               "hoàn cảnh bất thường."))
    return "".join(b)


def body_en():
    b = []

    # --- 5.4.2 (a), continued from module D ---------------------------------
    b.append(p("These situations are described in Fig. 5.14. The effects of this "
               "ventilation may also be considered when deciding on the additional "
               "level of general ventilation necessary for such a location."))
    b.append(fig(14, FB.fig_f514()))
    b.append(note("<b>Figure 5.14 caption note.</b> Note (3) is printed as 'is "
                  "restricted Table 3.2', with a word missing after 'restricted'; "
                  "the printed phrase is retained in the drawing and is not "
                  "silently corrected here. The caption also states a local "
                  "ventilation velocity of 2 m/s and a minimum of 0.5 m."))
    b.append(p("Where a continuous grade source of release is present in an area "
               "which is not freely ventilated, local extract ventilation (e.g., "
               "for an oil/water separator in a building) may be provided locally "
               "to the source of release to remove any gas or vapour which is "
               "normally released. Unless the source of release has additional "
               "modes of release it is, in such cases, reduced, as far as the area "
               "in question is concerned, to a secondary grade source of release "
               "on the basis that it will release into the area only when the local "
               "ventilation fails. This does suppose that the ventilation is "
               "quickly repaired if it does fail and here repair within the hour "
               "will be necessary. If the source can behave in other modes then "
               "these must be separately considered. Where the source of release "
               "can be described as a point source then, provided that the airflow "
               "around the source as a result of the ventilation is at least "
               "0.5 m/s, the Zone 0 will be less than 0.5 m."))
    b.append(p("Where a primary grade source of release is protected by local "
               "ventilation, the situation is similar to that existing for a "
               "continuous grade source of release except that, because the "
               "release is not continuous, the time taken to repair the ventilation "
               "may be longer and a period of within one shift (i.e., eight hours) "
               "is considered appropriate."))
    b.append(p("Where a secondary grade source of release is protected by local "
               "ventilation, only the area local to the source of release is "
               "considered as Zone 2, as far as that release is concerned. Failure "
               "of the ventilation coincident with the actual release of "
               "flammable material is considered as not happening within the scope "
               "of area classification, provided the ventilation is repaired "
               "expeditiously (again, within one shift - eight hours - is "
               "appropriate). The Zone 2 is limited to the immediate locale of the "
               "source of release if it is the only source of release in the area. "
               "It should be stressed, once again, that because of the velocity of "
               "release and quantity of material released from most secondary "
               "grade sources of release this type of limitation by point source "
               "ventilation is not easy or, in some cases, possible."))

    # --- 5.4.2 (b) ---------------------------------------------------------
    b.append(h4("Use of dividers in buildings together with selective ventilation",
                "Use of dividers in buildings together with selective ventilation"))
    b.append(p("Hazardous areas within an area, such as a building, which is not "
               "freely ventilated may also be achieved by the use of dividing walls "
               "or curtains, with ventilation arranged so that airflow is normally "
               "into the space enclosed by the walls or curtains. This technique is "
               "often used where manual loading activities are involved and "
               "releases in normal operation cannot be excluded."))
    b.append(p("It is not considered that such an approach is acceptable for "
               "continuous grade sources of release as the entire part of the area "
               "enclosed by the walls or curtains will adopt the classification "
               "appropriate to the source of release which would be Zone 0 in this "
               "case. The approach could, of course, be used where a continuous "
               "grade source of release has additional local ventilation as "
               "described earlier in this chapter."))
    b.append(p("Where a primary grade source of release, inside an area which is "
               "not freely ventilated, is further enclosed in walls or curtains in "
               "such a way that the ventilation in the enclosed place causes a "
               "general inflow of air through all apertures, the classification of "
               "the area within the walls or curtains will normally be Zone 1 (if "
               "the ventilation within the enclosed area is sufficient - see "
               "Chapter 4). However, the effect of the source of release on the "
               "area outside the curtains will be that of a secondary grade source "
               "of release, giving only Zone 2 in those areas. This, of course, "
               "presumes that ventilation failure is corrected within one shift, "
               "as before."))
    b.append(p("Where a secondary grade source of release, inside an area which is "
               "not freely ventilated, is further enclosed in walls or curtains "
               "achieving the above objectives, the source of release need not be "
               "taken into account in determination of the zonal classification of "
               "the remainder of the area, provided that the ventilation is "
               "expeditiously repaired after breakdown (say within one shift - "
               "eight hours)."))
    b.append(p("The walls or curtains used for the above purposes should be of "
               "gas-tight construction, apart from openings intended to be present, "
               "such as doorways, as the amount of air necessary if this were not "
               "so would be prohibitive. It is worth noting, however, that vertical "
               "overlapping strip curtaining has been used with success in this "
               "activity."))

    # --- 5.4.3 -------------------------------------------------------------
    b.append(h3("5.4.3 High integrity ventilation",
                "5.4.3 High integrity ventilation"))
    b.append(p("All of the above is based upon the fact that forced ventilation can "
               "fail and that failure is an abnormal effect and, therefore, it is "
               "only considered where continuous or primary grade sources of "
               "release are involved. The types of failure involved are normally "
               "mechanical or electrical failure of the ventilation itself. This "
               "problem may be overcome by duplicating the ventilation system so "
               "that a failure particular to one will merely bring the standby "
               "system into operation. Provided the separation between the two "
               "ventilation systems is sufficient (e.g., different mechanical parts "
               "and different electrical supplies) then failure of both systems "
               "can be neglected as it would require two abnormal events (which "
               "need not be considered for area classification purposes). In such "
               "cases it is possible to define limits of Zones within the building "
               "as the ventilation can be relied upon and tests can be carried out "
               "to show the extent of hazardous areas produced by particular "
               "releases in cases where no experience exists."))
    b.append(p("In such situations there remains the possibility of total electrical "
               "failure which is not likely to coincide with a release where "
               "secondary grade sources of release are involved, and in cases where "
               "continuous grade and primary grade sources of release are involved "
               "all electrical equipment will be de-energized by the failure. In "
               "such circumstances, provided that residual hot surfaces in "
               "equipment are addressed, then a pre-purge of the area before "
               "energizing the electrical equipment will ensure that the situation "
               "is acceptable. This can be achieved by introducing a delay between "
               "restoration of the airflow and energization. The time for this "
               "delay will depend upon the geometry of the building but if the "
               "building is properly designed to minimize the risk of unventilated "
               "pockets, which should be the case, the time should not need to "
               "exceed that required for an airflow equivalent to five times the "
               "volume of the building to pass through it."))
    b.append(p("In such circumstances the extent of any hazardous area can be "
               "calculated on the basis of the Equations in Chapter 4. The extents "
               "of the hazardous areas produced should be based upon the volume of "
               "explosive atmosphere expected."))

    # --- Worked Example -----------------------------------------------------
    b.append(h4("Example", "Example"))
    b.append(p("<b>Example.</b> A volume of vapour of mass 2.5 × 10<sup>−3</sup> is "
               "released by a source of release inside a building which has high "
               "integrity ventilation. The material released is at 295 K, has a "
               "molecular weight of 50, and a lower explosive limit of 2 per cent."))
    b.append(note("<b>Note on the mass unit.</b> The print gives '2.5 × "
                  "10<sup>−3</sup>' with no unit stated; from the context this is "
                  "kg. The printed value is retained and no unit has been assigned "
                  "silently."))
    b.append(p("In an open air situation near the ground the extent of the "
               "hazardous area would be given by Equation 4.7 multiplied by 1.5 in "
               "accordance with Fig. 3.3. This gives:"))
    b.append(eq("X = 1.5 × 10.8[GT/ME]<sup>0.55</sup> m"))
    b.append(eq("X = 16.2[2.5 × 10 − 03 × 295/50 × 2]<sup>0.55</sup> m"))
    b.append(eq("X = 1.1 (in an open air situation) m"))
    b.append(p("If we assume the minimum amount of air is used in the ventilation "
               "system of the indoor area then Equation 4.31 can be used and the "
               "following is the case:"))
    b.append(eq("Q<sub>a</sub> = 0.03 × 2.5 × 10<sup>−3</sup> × 2952/50 × 2 "
                "m<sup>3</sup>/s"))
    b.append(eq("Q<sub>a</sub> = 0.065 m<sup>3</sup>/s"))
    b.append(p("If the room is 100 m<sup>3</sup> in volume then the number of air "
               "changes per second is 6.5 × 10<sup>−4</sup>. At this low flow there "
               "will be badly ventilated parts and so a low airflow efficiency is "
               "expected and factor f (see Chapter 4) will be 5 and, if the source "
               "of release is a primary grade source of release, then k will be "
               "0.25. If we now use Equation 4.32 from we have the volume of "
               "explosive atmosphere:"))
    b.append(eq("Q = 0.065 × 5/6.5 × 10<sup>−4</sup> × 0.25 m<sup>3</sup>"))
    b.append(eq("Q = 2000 m<sup>3</sup>"))
    b.append(p("This would give a linear extent of hazardous area in the best case "
               "of:"))
    b.append(eq("X = 7.8 m"))
    b.append(p("Therefore, the extent of the hazardous area is around 8 m if the "
               "volume was a sphere but as it will not be due to the directional "
               "nature of ventilation it will be considerably larger. In addition "
               "the volume of the room would need to be much greater than the "
               "explosive atmosphere or it would result in the entire room being a "
               "hazardous area."))
    b.append(note("<b>Printed-error note for the Example.</b> (i) The first "
                  "substitution prints '2.5 × 10 − 03', the exponent of "
                  "10<sup>−3</sup> having degraded to '− 03'; (ii) the "
                  "Q<sub>a</sub> line prints '2952' with the 2 set inline instead "
                  "of as a superscript; (iii) all three displayed lines carry an "
                  "ambiguous '/' grouping - the results 1.1 m, 0.065 m<sup>3</sup>/s "
                  "and 2000 m<sup>3</sup> confirm denominators of (50 × 2) and "
                  "(6.5 × 10<sup>−4</sup> × 0.25); (iv) the sentence 'Equation 4.32 "
                  "from we have' is preserved verbatim; (v) the volume result is "
                  "labelled Q although Equation 4.32 gives V<sub>m</sub> - the "
                  "printed symbol is retained; (vi) the simplified form of Equation "
                  "4.31 prints LEL as a multiplier although the calculation uses "
                  "LEL in the denominator; (vii) the mass is given without a unit "
                  "(kg is implied); (viii) the intermediate value C = 6.5 × "
                  "10<sup>−4</sup> s<sup>−1</sup> appears only in the prose, not as "
                  "a displayed equation. None of these has been silently corrected."))

    # --- 5.5 ---------------------------------------------------------------
    b.append(h3("5.5 Rooms below ground", "5.5 Rooms below ground"))
    b.append(p("Rooms below ground should be treated as rooms above ground but, as "
               "natural ventilation via openings is not possible, only the forced "
               "ventilation solutions are possible. Provision of mechanisms to "
               "remove the gas vapour/air contents of the room become much more "
               "important as there is no other mechanism for changing the air in "
               "the room. Unless it is forcibly changed before energization of "
               "electrical equipment the risk of explosion is much greater as the "
               "persistence of an explosive atmosphere in an underground room with "
               "no forced ventilation is theoretically infinite."))

    # --- 5.6 ---------------------------------------------------------------
    b.append(h3("5.6 Rooms without any internal release but which abut external "
                "hazardous areas",
                "5.6 Rooms without any internal release but which abut external "
                "hazardous areas"))
    b.append(p("While no opening should exist in the part of a room which is "
               "adjacent to an external hazardous area, such an ideal situation is "
               "not always possible. Installations, such as cable ducts in walls, "
               "can be effectively sealed but it is often necessary to have a door "
               "in a wall, the other side of which is a hazardous area. In such "
               "circumstances the ideal solution would be to produce a situation "
               "where the explosive atmosphere does not access the room, as it is "
               "usually required to install electrical equipment which may be a "
               "source of ignition. This is not always possible, however, and as a "
               "result there are a variety of situations where partial or total "
               "invasion of the room by the external hazardous area occurs. The "
               "principal situation is where a room has a door or window which "
               "opens on to a hazardous area."))
    b.append(p("Where a room has an opening which abuts a hazardous area then, even "
               "if the opening is a door which is not used normally, the interior "
               "of the room must be assumed to be contaminated with the explosive "
               "atmosphere from the outside. As the ventilation inside the building "
               "is not normally free ventilation, the entire room must normally be "
               "assumed to adopt the external classification at least."))
    b.append(p("Where a room has a normal door or other opening which abuts a Zone "
               "1 or 2 the entire room should be assumed to be itself a Zone 1 or 2 "
               "(i.e., the external classification) at best. If ventilation within "
               "the room is unusually poor then the interior would be Zone 1, even "
               "if the external classification is Zone 2, but this more severe "
               "situation would not be likely in the case of normal above-ground "
               "rooms. It is not considered acceptable for any room openings to "
               "abut Zone 0 as such zones are normally expected to be contained."))
    b.append(p("There are several ways to mitigate the effects described above in "
               "the Zone 1 and Zone 2 situations. If, for example, a door is present "
               "in a room and is only used in emergencies, then an essentially "
               "gas-tight door could be fitted and be made either self closing or "
               "to alarm if it is left open. Such doors are assumed not to transmit "
               "the hazardous area to the inside of the room. An airlock comprising "
               "of two self-closing doors is assumed to have a similar effect, as "
               "is a single self-closing gas-tight door coupled with fresh air inlet "
               "ventilation into a room which keeps its pressure slightly positive. "
               "The argument in this latter case is that even if the door is used "
               "regularly there will only be a problem if the ventilation fails and "
               "the time for which the door would be open in these circumstances "
               "would be unlikely to create a scenario where any significant amount "
               "of gas entered the room, bearing in mind that personnel would be "
               "aware that the ventilation had failed."))
    b.append(p("The ideal solution is to design the process or installation so that "
               "all walls, etc., which abut hazardous areas are effectively sealed "
               "and this should be possible in the majority of circumstances."))

    # --- 5.7 ---------------------------------------------------------------
    b.append(h3("5.7 Particular circumstances", "5.7 Particular circumstances"))
    b.append(p("Quite often, rooms are employed for particular circumstances where "
               "flammable materials are used. Typical of these are the paint-spray "
               "booth (and similar rooms where personnel work) and the paint-drying "
               "oven."))

    b.append(h4("5.7.1 The paint spray booth", "5.7.1 The paint spray booth"))
    b.append(p("In a paint-spray booth an operative actually releases a flammable "
               "material (the solvent in the paint) as both a vapour and a mist in "
               "their work. The booth will obviously become a hazardous area and, "
               "as spraying is going on for most of the time, would normally be a "
               "Zone 0. The gun is not in the same place all the time and moves "
               "during the spraying process which means that no part of the booth "
               "will contain an explosive atmosphere for more time than is "
               "appropriate to Zone 1 classification. There is also a risk to the "
               "operative and both of these problems give rise to a very careful "
               "design whereby airflow is carefully controlled to ensure that "
               "solvents are swept to the back of the booth and not spread around. "
               "This is done by keeping the ventilation velocity relatively high "
               "and ventilating by extract via a grid (or similar) at the rear of "
               "the booth to even-out airflow. Also, the spraying activity is "
               "normally interlocked with the ventilation to ensure that spraying "
               "cannot take place unless the ventilation is on. This is normally "
               "achieved by creating curtain flow across the aperture of the booth "
               "and to arrange activities so that the spraying activity is normally "
               "directed to the back of the booth. This coupled with the velocity "
               "of airflow which should be more than 0.5 m/s creates a scenario "
               "where any Zone 1 is within the booth and for a small distance in "
               "front of it. In these circumstances, even with the airflow, it is "
               "prudent to classify an area to the front of the booth as Zone 1 for "
               "a small distance in front of the booth (say 1 m) and to take account "
               "of misdirection of spray, to define a Zone 2 for 3 m in front of the "
               "booth."))
    b.append(p("Figure 5.15 shows a typical classification for a booth of this "
               "type. It should, however, be remembered that other precautions will "
               "need to be taken for reasons of toxicity or situations where other "
               "sources of release occur (e.g., vehicle petrol tanks). HSE Note "
               "PM 25⁴ should be consulted in this regard."))
    b.append(fig(15, FB.fig_f515()))
    b.append(note("<b>Figure 5.15 legend note.</b> The printed legend reads 'A = "
                  "Grid or mesh to increase eveness of airflow', with the "
                  "misspelling 'eveness' (for 'evenness'); the printed word is "
                  "retained in the drawing. The figure shows Zone 1 at about 1 m "
                  "and Zone 2 at 3 m in front of the booth, together with a 1 m "
                  "zone around the duct outlet."))

    b.append(h4("5.7.2 The paint drying oven", "5.7.2 The paint drying oven"))
    b.append(p("Painted equipment is often dried in an oven giving a situation "
               "where solvents in the paint are evaporated in an enclosed space. "
               "What is worse is that the airflow through the oven is recirculated "
               "as it is heated to a significant degree and the cost of fresh-air "
               "ventilation would be abortive. This situation leads to enhancement "
               "of the problem in that the level of flammable material in the "
               "drying air grows until an equilibrium is reached because some of it "
               "is fed back into the oven and added to that which is evaporating. "
               "This effect is mitigated by the fact that much of the solvent "
               "produced is evaporated within the spray booth or in transit between "
               "the booth and the oven and the interior of the oven may normally be "
               "classified as Zone 1. As it is an enclosed space additional "
               "precautions are necessary and HSE Note PM 25⁴ should be consulted."))
    b.append(p("The exhaust of the oven should be classified as Zone 2 to take "
               "account of the fact that the ventilation may have to extract an "
               "explosive atmosphere from the oven on start-up, but such "
               "classification will be nominal as the solvents in question will "
               "have relatively high boiling points. Therefore, on start-up there "
               "will be at ambient temperature which will be very much lower. A "
               "distance of 3 m around the exit is suggested."))
    b.append(p("The oven should also be arranged so that in normal ventilation "
               "circumstances air is drawn in through any aperture, such as those "
               "used for entry of samples, and then a nominal hazardous area of "
               "(say) 3 m should be defined around these apertures to take account "
               "of abnormal circumstances."))
    return "".join(b)
