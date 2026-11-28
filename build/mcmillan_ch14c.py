# -*- coding: utf-8 -*-
"""Chapter 14, module C - bilingual reader (EN/VI).

Alan McMillan, *Electrical Installations in Hazardous Areas*
(Butterworth-Heinemann, 1998), printed pp. 447-452 (PDF pp. 468-473).

Covers 14.5.3 (sealed devices), 14.5.4 (energy limited apparatus and
circuits) and 14.5.5 (restricted breathing enclosures), with their
unnumbered Construction / Type testing / Testing / Other approaches to
restricted breathing enclosure / Use of the concept subheadings. Tables
14.6 and 14.7 and Fig. 14.5 sit at their printed positions. The chapter
shell owns the chapter h2, the printed references, the glossary, the
source-quirk note and the copyright.

Printed quirks are kept in the English text and bilingual notes are added
for every divergence flagged in survey C; the Vietnamese follows the
intended meaning. Cross-page paragraph halves are joined into one
continuous paragraph with a note recording the page boundary. This is an
unofficial study translation. The source PDF is not republished.
"""
from mcmillan_common import h3, h4, p, note, table, fig, ul, ol
import mcmillanfig14 as F
import mcmillan_tbl14_6_7 as T3


def body_vi():
    b = []

    # Running header on printed p.447 (OCR garbles it to '‘ny 447').
    b.append(note("<b>Lưu ý về ký tự dòng tiêu đề chạy.</b> Trang in chẵn 447 "
                  "mang dòng tiêu đề 'Protection concept ‘N’ (‘n’) 447'; lớp "
                  "văn bản OCR đọc nhầm thành '‘ny 447'. Dấu ngoặc kép kiểu "
                  "cong được giữ nguyên, dấu đọc nhầm chỉ được ghi nhận."))

    # C1 - heading 14.5.3 (printed p.447 / PDF p.468).
    b.append(h3("14.5.3 Thiết bị kín", "14.5.3 Sealed devices"))

    # C2 (printed p.447 / PDF p.468, raw 19279-19283).
    b.append(p("Thiết bị kín hoạt động tương tự như thiết bị kín hàn kín "
               "(hermetically sealed) nhưng dùng các gioăng làm kín và các "
               "lớp chót đổ khuôn, và thường được cố định với nhau bằng các "
               "thứ như đinh tán. Giống như vỏ bọc kín hàn kín, chúng không "
               "được thiết kế để mở trong quá trình sử dụng và do việc dùng "
               "các thứ như đinh tán hoặc keo dán, chúng bị phá hủy khi mở "
               "ra."))

    # C3 - unnumbered subheading 'Construction' (printed p.447).
    b.append(h4("Kết cấu", "Construction"))

    # C4 (printed p.447 / PDF p.468, raw 19285-19288).
    b.append(p("Khác với thiết bị kín hàn kín, thiết bị kín bị giới hạn về "
               "kích thước, ở mức 100 cm³. Các gioăng của chúng được điều "
               "hòa như đối với thiết bị ngắt kín (enclosed break devices) "
               "nhưng tại chỗ, và chúng phải được bảo vệ chống hư hại cơ "
               "học hoặc hư hại do môi trường theo cùng cách. Các lớp chót "
               "đổ khuôn cũng chịu cùng các giới hạn đó."))
    b.append(note("<b>Lưu ý về cách viết '100 cm³'.</b> Lớp văn bản thô ghi "
                  "'100cm3' không có dấu cách và không ở dạng mũ; trang in "
                  "cho thấy '100 cm³' có dấu cách và số 3 ở dạng mũ. Cách "
                  "đọc theo trang in được dùng."))

    # C5 - unnumbered subheading 'Type testing' (printed p.447).
    b.append(h4("Thử nghiệm kiểu", "Type testing"))

    # C6 (printed p.447 / PDF p.468, raw 19290).
    b.append(p("Các thử nghiệm kiểu áp dụng cho thiết bị kín giống hệt như "
               "các thử nghiệm áp dụng cho thiết bị kín hàn kín."))

    # C7 - heading 14.5.4 (printed p.447 / PDF p.468).
    b.append(h3("14.5.4 Thiết bị và mạch giới hạn năng lượng",
                "14.5.4 Energy limited apparatus and circuits"))

    # C8 (printed p.447 / PDF p.468, raw 19292-19296).
    b.append(p("Kỹ thuật này rất giống với an toàn nội tại ở chỗ nó dựa trên "
               "việc giới hạn công suất và năng lượng trong mạch đang xét "
               "tới các mức mà, ngay cả khi được giải phóng dưới dạng tia "
               "lửa hoặc truyền tới sự nóng lên của bề mặt, sẽ không gây ra "
               "tia lửa hay bề mặt nóng có khả năng gây cháy. Cách tiếp cận "
               "này đơn giản hơn nhiều."))

    # C9 (printed p.447 / PDF p.468, raw 19297-19304).
    b.append(p("Có hai loại thiết bị giới hạn năng lượng: loại thứ nhất, "
               "'thiết bị chứa mạch giới hạn năng lượng', là thiết bị được "
               "nối vào một mạch chứa năng lượng có khả năng gây cháy, trong "
               "đó sự giới hạn nằm bên trong thiết bị, nơi có các tiếp điểm "
               "phát tia lửa hoặc các bề mặt nóng có thể có; loại thứ hai, "
               "'Thiết bị để nối vào mạch giới hạn năng lượng', là thiết bị "
               "được nối vào một mạch thường được khởi đầu ở vùng không "
               "nguy hiểm, trong đó toàn bộ mạch ở vùng nguy hiểm – cả bên "
               "trong lẫn bên ngoài thiết bị – không chứa mức năng lượng gây "
               "cháy."))

    # C10 - unnumbered subheading 'Construction' (printed p.447).
    b.append(h4("Kết cấu", "Construction"))

    # C11 + C12 (printed p.447-448 / PDF p.468-469, raw 19306-19330; one
    # continuous paragraph split by the page break).
    b.append(p("Thiết bị chứa mạch giới hạn năng lượng được cấp từ một nguồn "
               "không giới hạn năng lượng và sẽ được giới hạn bằng các phương "
               "tiện đã mô tả trước đó cho mạch không phát tia lửa hoặc bằng "
               "lưới điện. Thiết bị thường chứa thêm các thiết bị hạn chế "
               "điện áp, chẳng hạn như máy biến áp nếu cấp từ lưới, hoặc các "
               "đi-ốt zener. Thường cũng có thêm các thiết bị hạn chế dòng "
               "như điện trở, mục tiêu là xác định rõ công suất và năng "
               "lượng có thể đưa tới các tiếp điểm phát tia lửa hoặc các bề "
               "mặt nóng có khả năng gây cháy. Trong trường hợp tiếp điểm "
               "phát tia lửa, tia lửa luôn hiện diện (khác với tia lửa do sự "
               "cố gây ra) và do đó khả năng tia lửa trùng hợp với khí quyển "
               "nổ được tăng lên. Điều này có nghĩa là điện áp và dòng điện "
               "vượt qua cực đại của các thiết bị hạn chế, trong trường hợp "
               "lưới điện tăng 10 phần trăm, trở nên quan trọng và tạo thành "
               "cơ sở đánh giá an toàn cho cả gây cháy do tia lửa lẫn gây "
               "cháy do bề mặt nóng, thay vì các thông số mạch giới hạn vận "
               "hành bình thường. Như vậy điện áp và dòng điện trong mọi "
               "trường hợp đều dựa trên dung sai của các linh kiện hạn chế "
               "điện áp và dòng điện trong thiết bị. Trong nhiều trường hợp "
               "các phần tử này không tạo thành một phần của mạch vận hành "
               "và do đó, nếu dùng các thiết bị hạn chế điện áp như đi-ốt "
               "zener và sự hỏng của chúng không được nhận diện qua hoạt "
               "động sai của mạch, chúng phải được nhân đôi nếu chúng bảo vệ "
               "một tiếp điểm phát tia lửa. Điều này cũng áp dụng cho các thứ "
               "như điện trở dùng ở chế độ song song để hạn chế điện áp "
               "nhưng không áp dụng cho các thiết bị đó dùng nối tiếp. Khi "
               "các linh kiện như vậy được dùng để triệt tiêu cảm ứng, sự "
               "nối của chúng với cuộn cảm phải được làm cho đáng tin cậy "
               "bằng cách đặt chúng càng gần cuộn cảm càng tốt, với các sắp "
               "xếp để hạn chế khả năng chúng bị ngắt kết nối mà không ngắt "
               "kết nối đồng thời cuộn cảm, trừ khi sự ngắt kết nối của chúng "
               "được nhận diện qua hoạt động sai của thiết bị."))
    b.append(note("<b>Lưu ý về ranh giới trang trong mục 'Kết cấu' của "
                  "14.5.4.</b> Đoạn trên bắt đầu ở cuối trang in 447 bằng "
                  "'It will normally contain further' và tiếp tục ở đầu "
                  "trang in 448 bằng 'voltage limiting devices...'. Hai nửa "
                  "được gộp thành một đoạn liên tục; không có nội dung nào "
                  "được thêm vào."))

    # C13 (printed p.448 / PDF p.469, raw 19331-19335).
    b.append(p("Thiết bị để nối vào mạch giới hạn năng lượng có thể có hoặc "
               "không có bên trong các thiết bị hạn chế để ngăn quá nhiệt "
               "hoặc tia lửa gây cháy nhưng, chúng sẽ dựa trên nguồn giới "
               "hạn năng lượng đã quy định để nối vào thiết bị. Trường hợp "
               "này, các thiết bị đó chủ yếu dùng để hạn chế nhiệt độ hoặc "
               "hạn chế năng lượng trong trường hợp có thể xảy ra sự tích "
               "trữ bên trong thiết bị, chẳng hạn như cuộn cảm hoặc tụ điện "
               "được gồm trong đó."))

    # C14 (printed p.448 / PDF p.469, raw 19336-19343).
    b.append(p("Điều quan trọng ở đây là quy định điện áp hở mạch cực đại, "
               "dòng ngắn mạch cực đại và khả năng truyền công suất cần "
               "thiết trong mạch mà thiết bị được nối vào, cùng với độ tự "
               "cảm và điện dung cực đại (với tỷ số L/R như một khả năng "
               "thay thế cho độ tự cảm) có thể có trong mạch đó. Sau đó "
               "trách nhiệm của người lắp đặt là đảm bảo các thông số này "
               "được tuân thủ. Điều này thường có nghĩa là thiết bị ở vùng "
               "không nguy hiểm chứa sự hạn chế điện áp và dòng điện ở mức "
               "tương tự như mức yêu cầu đối với loại thiết bị này."))
    b.append(note("<b>Lưu ý về cụm 'L/R ration'.</b> Bản in ghi '(with L/R "
                  "ration as a possible alternative to inductance)' dùng "
                  "'ration' thay vì 'ratio'. Cách viết này được giữ nguyên "
                  "trong bản tiếng Anh; bản tiếng Việt theo nghĩa đúng là "
                  "'tỷ số L/R'."))

    # C15 (printed p.448 / PDF p.469, raw 19344-19347).
    b.append(p("Cần nhớ ở đây rằng việc dùng cách tiếp cận mạch không gây "
               "cháy, trong đó toàn bộ mạch là không gây cháy, nhằm cho phép "
               "làm việc khi có điện ở mức tương tự như đối với an toàn nội "
               "tại (xem phần sau trong cuốn sách này)."))

    # C16 - unnumbered subheading 'Testing' (printed p.448).
    b.append(h4("Thử nghiệm", "Testing"))

    # C17 + C18 (printed p.448-449 / PDF p.469-470, raw 19349-19371; one
    # continuous paragraph split by the page break).
    b.append(p("Thử nghiệm tính không gây cháy được thực hiện tại các điểm "
               "mà tia lửa sẽ xuất hiện, dùng thiết bị thử tia lửa và các "
               "hỗn hợp thử giống như đối với an toàn nội tại (xem Chương "
               "13), nhưng trong trường hợp này không dùng hệ số an toàn. "
               "Các hỗn hợp khí thử và dòng hiệu chuẩn cho thiết bị thử tia "
               "lửa được lặp lại trong Bảng 14.6 và Bảng 14.7, với các dòng "
               "hiệu chuẩn bổ sung cho mạch điện trở. Sự hiện diện của các "
               "dòng hiệu chuẩn điện trở bắt nguồn từ quan điểm lịch sử "
               "trong an toàn nội tại, nơi người ta cho rằng sự khác biệt "
               "giữa hiệu chuẩn cảm ứng và hiệu chuẩn điện trở đủ lớn để "
               "đòi hỏi hiệu chuẩn riêng cho mạch điện trở và mạch điện dung "
               "khác với hiệu chuẩn dùng cho mạch cảm ứng. Sự khác biệt này "
               "hiện đã được chấp nhận trong an toàn nội tại là không đáng "
               "kể và chỉ hiệu chuẩn cảm ứng được dùng. Dù có thể mong đợi "
               "rằng tình huống tương tự sẽ xảy ra đối với Loại 'N', hiện "
               "không phải như vậy và do đó hai dòng hiệu chuẩn khác nhau "
               "vẫn còn tồn tại. Một khác biệt khác ở đây là thử nghiệm có "
               "thể được thực hiện với đĩa thiếc trong thiết bị thử tia lửa "
               "thay vì cadmi thông thường. Điều này cho mức công suất và "
               "năng lượng gây cháy cao hơn vì thiếc không có tác dụng tăng "
               "cường gây cháy. Điều này không được phép đối với an toàn nội "
               "tại do khó khăn trong việc loại trừ cadmi, kẽm và magiê, tất "
               "cả đều có tác dụng tăng cường gây cháy. Tuy nhiên, trong Loại "
               "'N', nơi rủi ro ít hơn, người ta kết luận rằng mức độ chú ý "
               "để đảm bảo đầy đủ sự vắng mặt của các vật liệu này có thể "
               "ít nghiêm ngặt hơn và do đó là khả thi. Tuy nhiên, mặc dù "
               "vậy, vẫn khuyến nghị dùng thử nghiệm với đĩa cadmi (tức là "
               "nhạy hơn) khi có thể."))
    b.append(note("<b>Lưu ý về ranh giới trang giữa các trang in 448 và "
                  "449.</b> Đoạn thử nghiệm kết thúc trang in 448 bằng "
                  "'...but in this case no safety factors are used.' và "
                  "tiếp tục ở đầu trang in 449 bằng 'The test gas mixtures...'. "
                  "Hai nửa được gộp thành một đoạn liên tục."))
    b.append(note("<b>Lưu ý về cách viết 'rigourous'.</b> Bản in ghi 'may be "
                  "less rigourous' thay vì 'rigorous'. Cách viết này được "
                  "giữ nguyên trong bản tiếng Anh; bản tiếng Việt dùng từ "
                  "đúng nghĩa."))
    b.append(note("<b>Lưu ý về cụm 'Notwithstanding ths'.</b> Bản in ghi "
                  "'Notwithstanding ths, however,' với 'ths' thay vì 'this'. "
                  "Cách viết này được giữ nguyên trong bản tiếng Anh; bản "
                  "tiếng Việt theo nghĩa đúng."))

    # C19 (printed p.449 / PDF p.470, raw 19372-19374).
    b.append(p("Việc đánh giá các mạch phát tia lửa là có thể đối với loại "
               "'N' bằng cách dùng các đường cong cho trong Chương 13 (Hình "
               "13.5, 13.6, 13.8 và 13.10). Các đường cong có thể được dùng "
               "trực tiếp vì không có các hệ số an toàn bổ sung như trong an "
               "toàn nội tại."))
    b.append(note("<b>Lưu ý về sự thay đổi viết hoa của 'Type ‘N’'.</b> Bản in "
                  "dùng 'Type ‘N’' với chữ T hoa trong đoạn trước nhưng 'type "
                  "‘N’' với chữ t thường ở đây. Sự không nhất quán này được "
                  "giữ nguyên theo bản in."))

    # C20 - Table 14.6 (printed p.449 / PDF p.470).
    b.append(table(T3.HEAD146_VI, T3.ROWS146_VI, T3.CAPTION146_VI))

    # C21 - Table 14.7 (printed p.449 / PDF p.470).
    b.append(table(T3.HEAD147_VI, T3.ROWS147_VI, T3.CAPTION147_VI))
    b.append(note("<b>Lưu ý về dấu ± trong Bảng 14.6 và 14.7.</b> Lớp văn bản "
                  "thô ghi nhầm dấu ± thành các ký tự rác; trang in cho thấy "
                  "'±' trong cả ba hàng. Các ô dòng trong Bảng 14.7 là số "
                  "thuần túy. Cách đọc theo trang in được dùng."))

    # C22 - heading 14.5.5 (printed p.450 / PDF p.471).
    b.append(h3("14.5.5 Vỏ bọc hạn chế hít thở",
                "14.5.5 Restricted breathing enclosures"))

    # C23 (printed p.450 / PDF p.471, raw 19396-19403).
    b.append(p("Đây là một loại hình bảo vệ khá bất thường, không dựa trên "
               "sự bịt kín hoàn toàn mà dựa trên việc hạn chế sự ra vào của "
               "khí (hít thở). Trước đây nó chỉ được dùng cho một số đồ đạc "
               "chiếu sáng ở Vương quốc Anh và không được coi là chấp nhận "
               "được đối với thiết bị phát tia lửa. Tuy nhiên, ở Thụy Sĩ, nơi "
               "kỹ thuật này được dùng nhiều hơn rất nhiều, tình hình lại "
               "hoàn toàn ngược lại. Kỹ thuật do người Thụy Sĩ dùng không "
               "cho phép bề mặt nóng mà chỉ cho phép các tiếp điểm phát tia "
               "lửa. Việc sử dụng nó phổ biến hơn nhiều, ví dụ nó có thể "
               "được áp dụng cho các bảng phân phối lớn."))

    # C24 (printed p.450 / PDF p.471, raw 19404-19416).
    b.append(p("Cách tiếp cận lịch sử của Vương quốc Anh, vẫn còn hiệu lực "
               "hiện nay, là dùng hạn chế hít thở cho các đèn chiếu sáng và "
               "loại trừ nó cho các tiếp điểm phát tia lửa. Điều này bắt "
               "nguồn từ quan điểm rằng các đèn chiếu sáng không được bật "
               "tắt thường xuyên và rằng, ngay cả khi có một số hít thở, "
               "khó có thể có bất cứ thứ gì giống như một khí quyển nổ lý "
               "tưởng tồn tại trong vỏ bọc. Vì lý do này, người ta coi cách "
               "tiếp cận này là chấp nhận được cho Vùng 2 và, thực tế, việc "
               "sử dụng lịch sử cách tiếp cận này không gặp vấn đề gì ủng "
               "hộ điều đó. Dù cách tiếp cận này được coi là phù hợp cho các "
               "đèn chiếu sáng không được bật tắt thường xuyên (tức là không "
               "chịu chu trình làm việc), không có bằng chứng ủng hộ bất kỳ "
               "sử dụng nào khác mà ở đó chu trình nhiệt độ bên trong vỏ "
               "bọc xảy ra thường xuyên hơn. Điều này không phải là vấn đề "
               "đối với Vương quốc Anh vì hạn chế hít thở trước đây chỉ "
               "giới hạn ở đèn chiếu sáng và hiện vẫn tiếp tục như vậy. Sau "
               "đây là tình hình đối với hạn chế hít thở như được thực hành "
               "ở Vương quốc Anh."))
    b.append(note("<b>Lưu ý về cách viết 'practiced'.</b> Bản in dùng 'as "
                  "practiced in the UK' với cách viết kiểu Mỹ thay vì "
                  "'practised'. Cách viết này được giữ nguyên trong bản "
                  "tiếng Anh."))

    # C25 - unnumbered subheading 'Construction' (printed p.450).
    b.append(h4("Kết cấu", "Construction"))

    # C26 (printed p.450 / PDF p.471, raw 19418-19423).
    b.append(p("Không có yêu cầu kết cấu nào đối với vỏ bọc hạn chế hít thở "
               "ngoài việc các gioăng nhiệt dẻo và cao su đàn hồi được điều "
               "hòa trước, như đối với các gioăng trong thiết bị ngắt kín, "
               "trước khi thực hiện bất kỳ thử nghiệm kiểu nào, và rằng "
               "chúng cần được bảo vệ chống hư hại cơ học và môi trường theo "
               "cùng cách. Tương tự, các lớp chót đổ khuôn chịu cùng các "
               "yêu cầu như những lớp trong thiết bị ngắt kín."))

    # C27 (printed p.450 / PDF p.471, raw 19424-19426).
    b.append(p("Các vỏ bọc hạn chế hít thở được yêu cầu phải có phương tiện "
               "để thực hiện thử nghiệm hạn chế hít thở trong quá trình sử "
               "dụng và do đó phải có phương tiện cho phép nối một thiết bị "
               "thử."))

    # C28 - unnumbered subheading 'Testing' (printed p.450).
    b.append(h4("Thử nghiệm", "Testing"))

    # C29 + C30 (printed p.450-451 / PDF p.471-472, raw 19428-19438; one
    # continuous paragraph split by the page break).
    b.append(p("Thử nghiệm kiểu cho vỏ bọc hạn chế hít thở khá đơn giản vì nó "
               "chỉ là thử nghiệm sự hít vào của vỏ bọc (sự thở ra không "
               "quan trọng). Áp suất trong vỏ bọc được giảm xuống dưới 0.97 "
               "× 10⁵ N/m² tuyệt đối (xấp xỉ 0.97 atmotphe) và sau đó đo "
               "thời gian để không khí xâm nhập đủ làm áp suất thay đổi từ "
               "0.97 × 10⁵ lên 0.985 × 10⁵. Thời gian này không được nhỏ hơn "
               "ba phút. Có thể xác định thời gian này chỉ với áp suất dư "
               "bên trong khi có thể chứng minh rằng tính năng của vỏ bọc "
               "đối với áp suất dư cũng giống như đối với áp suất âm."))
    b.append(note("<b>Lưu ý về cụm 'restrictive breathing enclosures'.</b> "
                  "Bản in ghi 'Type testing for restrictive breathing "
                  "enclosures' dùng 'restrictive' thay vì 'restricted'. Cách "
                  "viết này được giữ nguyên trong bản tiếng Anh; bản tiếng "
                  "Việt theo nghĩa đúng là 'vỏ bọc hạn chế hít thở'."))
    b.append(note("<b>Lưu ý về ranh giới trang giữa các trang in 450 và "
                  "451.</b> Đoạn thử nghiệm kết thúc trang in 450 bằng "
                  "'...with an internal overpressure only' và tiếp tục đầu "
                  "trang in 451 bằng 'where it can be shown...'. Lớp văn bản "
                  "thô ghi nhầm '0.97 × 10⁵' thành '0.97 x lo5' và '0.985 × "
                  "10⁵' thành '0.985 x lo5'; cách đọc theo trang in được "
                  "dùng. Hai nửa được gộp thành một đoạn liên tục."))

    # C31 (printed p.451 / PDF p.472, raw 19439-19443).
    b.append(p("Thử nghiệm này có thể cần được thực hiện sau khi đóng lại "
               "thiết bị, đôi khi sau mỗi lần mở, và cần có sự bố trí trong "
               "kết cấu để cho phép thực hiện việc đó. Thường thì điều này "
               "được thực hiện bằng cách có một thiết bị đầu vào cho một "
               "thiết bị hút chân không đơn giản có thể được bịt kín bằng một "
               "van hoặc một vít và gioăng sau khi thử nghiệm."))

    # C32 - unnumbered subheading 'Other approaches to restricted breathing
    # enclosure' (printed p.451). Note the singular 'enclosure'.
    b.append(h4("Cách tiếp cận khác cho vỏ bọc hạn chế hít thở",
                "Other approaches to restricted breathing enclosure"))

    # C33 (printed p.451 / PDF p.472, raw 19445-19451).
    b.append(p("Quốc gia khác từng dùng hạn chế hít thở như một khái niệm "
               "bảo vệ trong lịch sử là Thụy Sĩ, nơi khái niệm này được dùng "
               "theo cách hoàn toàn khác. Ở đây khái niệm này đã được dùng "
               "cho thiết bị có thể phát tia lửa trong vận hành bình thường, "
               "chẳng hạn như thiết bị đóng cắt, và nó bị giới hạn ở thiết bị "
               "mà công suất tiêu tán bên trong không đủ làm nhiệt độ bên "
               "trong tăng quá 10°C. Do đó không thể dùng nó cho đèn chiếu "
               "sáng. Dù các yêu cầu kết cấu cơ bản không khác nhau nhiều, "
               "việc thử nghiệm thì có. Một trong ba thử nghiệm đã được áp "
               "dụng như sau."))

    # C34-C36 - the numbered test list (printed p.451 / PDF p.472).
    b.append(ol([
        "Áp dụng thử nghiệm thời gian bán khuếch tán, trong đó carbon dioxide "
        "được đưa vào vỏ bọc mà không làm tăng áp suất cho đến khi mức nồng "
        "độ carbon dioxide bên trong là 25 phần trăm. Sau đó nồng độ carbon "
        "dioxide bên trong được theo dõi trong thời gian đủ để vẽ được một "
        "đường cong thẳng biểu thị sự giảm nồng độ theo thời gian. Đường cong "
        "này sau đó được ngoại suy để ước tính thời gian cần để nồng độ "
        "carbon dioxide bên trong giảm xuống 12.5 phần trăm, thời gian này "
        "không được nhỏ hơn 80 giờ. Khi thiết bị đo áp suất làm tăng đáng kể "
        "thể tích của vỏ bọc (hơn chẳng hạn 10 phần trăm), thời gian nêu trên "
        "cần được nhân với tổng thể tích chia cho thể tích vỏ bọc.",
        "Ngoài ra, khi vỏ bọc có thể tích nhỏ hơn 10 lít, nó nên được nâng "
        "hoặc hạ (tùy chọn) tới áp suất cao hơn hoặc thấp hơn áp suất khí "
        "quyển 500 N/m² và đo sự giảm chênh lệch áp suất. Thời gian để "
        "chênh lệch giảm từ 400 N/m² xuống 200 N/m² trong trường hợp này "
        "phải ít nhất là 80 giây. Cách nhân thời gian tương tự như đối với "
        "thử nghiệm carbon dioxide được áp dụng khi thiết bị đo có thể tích "
        "đáng kể.",
        "Phương án thứ ba là tạo áp suất trong vỏ bọc cao hơn áp suất khí "
        "quyển 400 N/m² và tính thể tích không khí cần mỗi giờ để duy trì áp "
        "suất dư đó. Thể tích đó, chia cho thể tích vỏ bọc, không được vượt "
        "quá giá trị 0.125.",
    ]))
    b.append(note("<b>Lưu ý về các giá trị trong danh sách thử nghiệm kiểu "
                  "Thụy Sĩ.</b> Các mục trên được đưa vào danh sách đánh số "
                  "của bản in. Lớp văn bản thô ghi nhầm 'less than 10 litres' "
                  "thành 'less than lolitres' và bỏ dấu cách trong '500 N/m²', "
                  "'400 N/m²', '200 N/m²'; trang in cho thấy các giá trị có "
                  "dấu cách như trên. Cách đọc theo trang in được dùng."))

    # C37 - unnumbered subheading 'Use of the concept' (printed p.451).
    b.append(h4("Sử dụng khái niệm", "Use of the concept"))

    # C38 + C39 (printed p.451-452 / PDF p.472-473, raw 19474-19487; one
    # continuous paragraph split by the page break).
    b.append(p("Cũng như cách tiếp cận của Vương quốc Anh, cách tiếp cận của "
               "Thụy Sĩ, như được định nghĩa trong IEC 79–15¹¹, bị giới hạn ở "
               "thiết bị không chịu chu trình làm việc, vì chu trình này có "
               "thể gây ra những thay đổi nhiệt độ đáng kể. Ngoài ra, kỹ thuật "
               "này trong dạng thức Thụy Sĩ/IEC bị giới hạn ở các khí và hơi "
               "có hệ số hạn chế hít thở (s) nhỏ hơn 20. Hệ số này liên quan "
               "đến điểm sôi (bp), trọng lượng phân tử (m) và giới hạn nổ "
               "dưới (LEL) của khí hoặc hơi đang xét và được suy ra từ Hình "
               "14.5. Điểm sôi được xác định trên phía bên trái của Hình 14.5 "
               "và trọng lượng phân tử ở phía bên phải. Sau đó hai điểm này "
               "được nối bằng một đường thẳng, tạo ra một điểm Z trên đường "
               "giữa. LEL của khí hoặc hơi sau đó được xác định trên phía "
               "bên phải của Hình 14.5 và một đường được vẽ sang phía bên "
               "trái đi qua điểm Z trên đường giữa. Khi đó hệ số hạn chế hít "
               "thở có thể được đọc trên phía bên trái."))
    b.append(note("<b>Lưu ý về ranh giới trang giữa các trang in 451 và "
                  "452.</b> Đoạn 'Use of the concept' kết thúc trang in 451 "
                  "bằng '...which can cause' và tiếp tục đầu trang in 452 "
                  "bằng 'significant temperature changes.' Lớp văn bản thô "
                  "ghi nhầm 'IEC 79–15¹¹' thành 'IEC 79-1511'; trang in cho "
                  "thấy dấu gạch ngang và số 11 ở dạng mũ. Hai nửa được gộp "
                  "thành một đoạn liên tục."))

    # C40 (printed p.452 / PDF p.473, raw 19488-19495).
    b.append(p("Dù cách tiếp cận hạn chế hít thở này hiện không được dùng ở "
               "Vương quốc Anh, việc sắp ban hành một Tiêu chuẩn Châu Âu cho "
               "loại bảo vệ 'N' có thể đưa nó vào vì cách tiếp cận này có "
               "trong IEC 79–15¹¹, và tài liệu này sẽ tạo thành cơ sở cho "
               "Tiêu chuẩn Châu Âu. Sự tồn tại của một Tiêu chuẩn Châu Âu như "
               "vậy có thể tạo ra tình huống mà Vương quốc Anh có thể thấy "
               "bắt buộc phải sử dụng loại thiết bị này và vì lý do đó nó "
               "được đưa vào. Tính an toàn của thiết bị như vậy có thể bị "
               "đặt câu hỏi nhưng việc sử dụng lâu dài của nó ở Thụy Sĩ không "
               "đưa ra bằng chứng nào ủng hộ những nghi ngờ đó."))

    # C41 - Fig. 14.5 (printed p.452 / PDF p.473), after the discussion.
    b.append(fig(5, F.fig_f1405()))
    b.append(note("<b>Lưu ý về chú thích của Hình 14.5.</b> Bản in ghi "
                  "'between the material boiling point end its molecular "
                  "weight' dùng 'end' thay vì 'and', và 'less then 40 °C' dùng "
                  "'then' thay vì 'than' (với '40°C' không có dấu cách ở lần "
                  "lặp thứ hai). Các quirk này được giữ nguyên trong chú "
                  "thích tiếng Anh của hình; bản tiếng Việt dùng nghĩa đúng."))

    return "".join(b)


def body_en():
    b = []

    # Running header on printed p.447 (OCR garbles it to '‘ny 447').
    b.append(note("<b>Note on the running header glyph.</b> Even-numbered "
                  "printed p.447 carries the header 'Protection concept "
                  "‘N’ (‘n’) 447'; the OCR text layer garbles it to "
                  "'‘ny 447'. "
                  "The curly quotes are kept and the garbled reading is "
                  "noted but not reproduced."))

    # C1 - heading 14.5.3 (printed p.447 / PDF p.468).
    b.append(h3("14.5.3 Sealed devices", "14.5.3 Sealed devices"))

    # C2 (printed p.447 / PDF p.468, raw 19279-19283).
    b.append(p("Sealed devices are similar in operation to hermetically "
               "sealed devices but use sealing gaskets and poured seals, and "
               "are often secured together by such things as rivets. Like "
               "hermetically sealed enclosures, they are not intended to be "
               "opened in service and by the use of such things as rivets or "
               "adhesives they are destroyed by opening."))

    # C3 - unnumbered subheading 'Construction' (printed p.447).
    b.append(h4("Construction", "Construction"))

    # C4 (printed p.447 / PDF p.468, raw 19285-19288).
    b.append(p("Sealed devices are limited in size, unlike hermetically "
               "sealed devices, to 100 cm³. Their gaskets are conditioned as "
               "for enclosed break devices but in situ and they must be "
               "protected against mechanical damage or environmental damage "
               "in the same way. Poured seals are also subject to the same "
               "limitations."))
    b.append(note("<b>Note on the reading '100 cm³'.</b> The raw text layer "
                  "reads '100cm3' with no space and no superscript; the "
                  "render shows '100 cm³' with a space and a superscript 3. "
                  "The render reading is used."))

    # C5 - unnumbered subheading 'Type testing' (printed p.447).
    b.append(h4("Type testing", "Type testing"))

    # C6 (printed p.447 / PDF p.468, raw 19290).
    b.append(p("The type tests applied to sealed devices are identical to "
               "those for hermetically sealed devices."))

    # C7 - heading 14.5.4 (printed p.447 / PDF p.468).
    b.append(h3("14.5.4 Energy limited apparatus and circuits",
                "14.5.4 Energy limited apparatus and circuits"))

    # C8 (printed p.447 / PDF p.468, raw 19292-19296).
    b.append(p("This technique is very similar to intrinsic safety in that "
               "it relies on the limitation of power and energy in the "
               "circuit in question to levels that, even if released as a "
               "spark or delivered to heating of a surface, will not cause "
               "sparks or hot surfaces which are ignition capable. The "
               "approach is much more simple."))

    # C9 (printed p.447 / PDF p.468, raw 19297-19304).
    b.append(p("There are two types of energy limited apparatus: the first "
               "type, ‘apparatus containing energy limited circuits’, is that "
               "which is connected to a circuit which contains "
               "ignition-capable energy where limitation is within the "
               "apparatus where sparking contacts or possible hot surfaces "
               "are present; the second type, ‘Apparatus for connection to "
               "energy limited circuits’, is that which is connected to a "
               "circuit usually initiated in a non-hazardous area where the "
               "entire circuit in the hazardous area – both within and "
               "outside the apparatus – does not contain incendive levels of "
               "energy."))

    # C10 - unnumbered subheading 'Construction' (printed p.447).
    b.append(h4("Construction", "Construction"))

    # C11 + C12 (printed p.447-448 / PDF p.468-469, raw 19306-19330; one
    # continuous paragraph split by the page break).
    b.append(p("Apparatus containing energy limited circuits is fed from a "
               "supply which is not energy limited and will be either "
               "limited by means described earlier for non-sparking circuits "
               "or by the mains. It will normally contain further voltage "
               "limiting devices, such as a transformer if mains fed, or "
               "zener diodes. Further current limiting by such things as "
               "resistors will normally also be present, the objective being "
               "to define clearly the power and energy which can be fed to "
               "sparking contacts or potentially ignition-capable hot "
               "surfaces. In the case of sparking contacts the sparks are "
               "always there (unlike sparks caused by faults) and the "
               "likelihood of coincidence of a spark and the explosive "
               "atmosphere is thus increased. This means that the maximum "
               "voltage and current let-through of the limiting devices, in "
               "the case of mains with a 10 per cent elevation, become "
               "important and form the basis of evaluation of safety for "
               "both spark ignition, and hot surface ignition rather than "
               "the normal operational limiting circuit parameters. Thus "
               "the voltage and current are in all cases based upon the "
               "tolerances of the voltage and current limiting components in "
               "the apparatus. In many cases these elements will not form a "
               "part of the operational circuit and thus, if voltage "
               "limiters such as zener diodes are used and their failure is "
               "not identified by maloperation of the circuit, they must be "
               "duplicated if they protect a sparking contact. This also "
               "applies to such things as resistors used in a shunt mode to "
               "limit voltage but not to such devices used in series. Where "
               "such components are used to suppress inductances their "
               "connection to the inductance must be made reliable by "
               "placing them as close to it as possible with arrangements to "
               "limit the possibility of their becoming disconnected without "
               "the simultaneous disconnection of the inductor, unless their "
               "disconnection is identified by maloperation of the "
               "apparatus."))
    b.append(note("<b>Note on the page boundary in the 'Construction' "
                  "subsection of 14.5.4.</b> The paragraph begins at the "
                  "foot of printed p.447 with 'It will normally contain "
                  "further' and continues at the top of printed p.448 with "
                  "'voltage limiting devices...'. The two halves are joined "
                  "as one continuous paragraph; nothing is supplied from "
                  "conjecture."))

    # C13 (printed p.448 / PDF p.469, raw 19331-19335).
    b.append(p("Apparatus for connection to energy limited circuits may or "
               "may not have within it limiting devices to prevent overheating "
               "or incendive sparking but, they will be based upon the energy "
               "limited source specified for connection to the apparatus. In "
               "this case such devices will be predominantly for temperature "
               "limitation or for energy limitation in cases where storage "
               "within the apparatus can occur, such as included inductors "
               "or capacitors."))

    # C14 (printed p.448 / PDF p.469, raw 19336-19343).
    b.append(p("The important thing here is to specify the maximum open "
               "circuit voltage, short circuit current, and power transfer "
               "capability required in the circuit to which the apparatus is "
               "connected, together with the maximum inductance and capacity "
               "(with L/R ration as a possible alternative to inductance) "
               "which may be present in that circuit. It is then up to the "
               "installer to ensure that these parameters are complied with. "
               "This will often mean the apparatus in the non-hazardous area "
               "containing voltage and current limitation to a level similar "
               "to that required in this type of apparatus."))
    b.append(note("<b>Note on the phrase 'L/R ration'.</b> The print reads "
                  "'(with L/R ration as a possible alternative to "
                  "inductance)', with 'ration' in place of 'ratio'. The "
                  "printed wording is kept; the Vietnamese follows the "
                  "intended meaning ('L/R ratio')."))

    # C15 (printed p.448 / PDF p.469, raw 19344-19347).
    b.append(p("It must be remembered here that use of the non-incendive "
               "circuit approach, where the entire circuit is non-incendive, "
               "is intended to allow live working to a similar degree as "
               "that for intrinsic safety (see later in this book)."))

    # C16 - unnumbered subheading 'Testing' (printed p.448).
    b.append(h4("Testing", "Testing"))

    # C17 + C18 (printed p.448-449 / PDF p.469-470, raw 19349-19371; one
    # continuous paragraph split by the page break).
    b.append(p("Testing of non-incendivity is carried out at points where "
               "sparking will occur using the spark test apparatus and the "
               "same test mixtures as for intrinsic safety (see Chapter 13) "
               "but in this case no safety factors are used. The test gas "
               "mixtures and calibration currents for the spark test "
               "apparatus are repeated in Tables 14.6 and 14.7, with "
               "additional calibration currents for resistive circuits. The "
               "presence of resistive calibration currents stems from the "
               "historic position in intrinsic safety where it was felt that "
               "the difference between inductive calibration and resistive "
               "calibration was sufficient to warrant separate calibration "
               "for resistive and capacitive circuits to that used for "
               "inductive circuits. This difference has now been accepted in "
               "intrinsic safety as not significant and only the inductive "
               "calibration is used. While it may be expected that the same "
               "will be the case in Type ‘N’ it is not currently so and thus "
               "the two different calibration currents still exist. Another "
               "difference here is that the test may be carried out with a "
               "tin disc in the spark test apparatus rather than the normal "
               "cadmium. This gives higher levels of ignition power and "
               "energy because it does not have an ignition enhancing "
               "effect. It is not permitted for intrinsic safety because of "
               "the difficulty of exclusion of cadmium, zinc and magnesium, "
               "all of which have this ignition enhancing effect. In Type "
               "‘N’, however, where the risk is more remote it is concluded "
               "that the level of attention to adequately ensure the absence "
               "of these materials may be less rigourous and thus possible. "
               "Notwithstanding ths, however, it is recommended that the "
               "cadmium disc (i.e., the more sensitive) test is used where "
               "possible."))
    b.append(note("<b>Note on the page boundary between printed pp.448 and "
                  "449.</b> The testing paragraph ends printed p.448 with "
                  "'...but in this case no safety factors are used.' and "
                  "continues on printed p.449 with 'The test gas mixtures...'. "
                  "The two halves are joined as one continuous paragraph."))
    b.append(note("<b>Note on the spelling 'rigourous'.</b> The print reads "
                  "'may be less rigourous' rather than 'rigorous'. The "
                  "printed spelling is kept; the Vietnamese uses the "
                  "correctly spelled word."))
    b.append(note("<b>Note on the phrase 'Notwithstanding ths'.</b> The "
                  "print reads 'Notwithstanding ths, however,', with 'ths' "
                  "in place of 'this'. The printed wording is kept; the "
                  "Vietnamese follows the intended meaning."))

    # C19 (printed p.449 / PDF p.470, raw 19372-19374).
    b.append(p("Assessment of sparking circuits is possible for type ‘N’ "
               "using the curves given in Chapter 13 (Figs. 13.5, 13.6, 13.8 "
               "and 13.10). The curves can be used directly as there are no "
               "added safety factors as in intrinsic safety."))
    b.append(note("<b>Note on the capitalisation of 'Type ‘N’'.</b> The print "
                  "uses 'Type ‘N’' with a capital T in the preceding "
                  "paragraph but 'type ‘N’' with a lower-case t here. The "
                  "inconsistency is kept as printed."))

    # C20 - Table 14.6 (printed p.449 / PDF p.470).
    b.append(table(T3.HEAD146_EN, T3.ROWS146_EN, T3.CAPTION146_EN))

    # C21 - Table 14.7 (printed p.449 / PDF p.470).
    b.append(table(T3.HEAD147_EN, T3.ROWS147_EN, T3.CAPTION147_EN))
    b.append(note("<b>Note on the ± sign in Tables 14.6 and 14.7.</b> The raw "
                  "text layer garbles the ± sign into stray characters; the "
                  "render shows '±' in all three rows. The current cells in "
                  "Table 14.7 are purely numeric. The render reading is "
                  "used."))

    # C22 - heading 14.5.5 (printed p.450 / PDF p.471).
    b.append(h3("14.5.5 Restricted breathing enclosures",
                "14.5.5 Restricted breathing enclosures"))

    # C23 (printed p.450 / PDF p.471, raw 19396-19403).
    b.append(p("This is a somewhat unusual type of protection relying not on "
               "total sealing but on the limitation of entry and exit of gas "
               "(breathing). Historically it has only been used on certain "
               "lighting fittings in the UK and has not been considered as "
               "acceptable for sparking equipment. In Switzerland, however, "
               "where much more use of the technique has been made, quite "
               "the reverse is the case. The technique used by the Swiss does "
               "not permit hot surfaces and only allows sparking contacts. "
               "Its use is much more prevalent, for example it can be applied "
               "to large switchboards."))

    # C24 (printed p.450 / PDF p.471, raw 19404-19416).
    b.append(p("The historic UK approach, which is still current, is the use "
               "of restricted breathing for luminaires and its exclusion for "
               "sparking contacts. This stems from the view that luminaires "
               "are not regularly switched on and off and that, even if some "
               "breathing occurs, it is unlikely that anything like an ideal "
               "explosive atmosphere will ever exist in the enclosure. For "
               "this reason it is considered that the approach is acceptable "
               "for Zone 2 and, indeed, the historical use of this approach "
               "without problems supports this. While the approach has been "
               "considered as suitable for luminaires which are not regularly "
               "switched on and off (i.e., not subject to duty cycling) the "
               "support for any other use where temperature cycling within "
               "the enclosure occurs more regularly does not exist. This is "
               "not a problem for the UK because restricted breathing has in "
               "the past been restricted to luminaires and this continues to "
               "be the case. The following is the situation for restricted "
               "breathing as practiced in the UK."))
    b.append(note("<b>Note on the spelling 'practiced'.</b> The print reads "
                  "'as practiced in the UK', using the US spelling rather "
                  "than 'practised'. The printed spelling is kept."))

    # C25 - unnumbered subheading 'Construction' (printed p.450).
    b.append(h4("Construction", "Construction"))

    # C26 (printed p.450 / PDF p.471, raw 19418-19423).
    b.append(p("There are no constructional requirements for restricted "
               "breathing enclosures other than that thermoplastic and "
               "elastomeric seals are preconditioned, as for those in "
               "enclosed break devices, before any type testing is carried "
               "out and that they need to be protected against mechanical "
               "and environmental damage in the same way. Likewise poured "
               "seals are subjected to the same requirements as those in "
               "enclosed break devices."))

    # C27 (printed p.450 / PDF p.471, raw 19424-19426).
    b.append(p("Restricted breathing enclosures are required to have "
               "facilities for execution of the restricted breathing test in "
               "service and there has, therefore, to be a facility to allow "
               "the connection of a test device."))

    # C28 - unnumbered subheading 'Testing' (printed p.450).
    b.append(h4("Testing", "Testing"))

    # C29 + C30 (printed p.450-451 / PDF p.471-472, raw 19428-19438; one
    # continuous paragraph split by the page break).
    b.append(p("Type testing for restrictive breathing enclosures is quite "
               "simple as it is solely a test of the inward breathing of the "
               "enclosure (the outward breathing is not important). The "
               "enclosure is reduced in pressure to less than 0.97 × 10⁵ "
               "N/m² absolute (approximately 0.97 atmospheres) and then the "
               "time taken for ingress of air sufficient to change the "
               "pressure from 0.97 × 10⁵ to 0.985 × 10⁵ is measured. This "
               "time must not be less than three minutes. It is possible to "
               "determine this time with an internal overpressure only where "
               "it can be shown that the performance of the enclosure is the "
               "same for overpressure as for underpressure."))
    b.append(note("<b>Note on the phrase 'restrictive breathing "
                  "enclosures'.</b> The print reads 'Type testing for "
                  "restrictive breathing enclosures', using 'restrictive' "
                  "rather than 'restricted'. The printed wording is kept; "
                  "the Vietnamese follows the intended meaning."))
    b.append(note("<b>Note on the page boundary between printed pp.450 and "
                  "451.</b> The testing paragraph ends printed p.450 with "
                  "'...with an internal overpressure only' and continues on "
                  "printed p.451 with 'where it can be shown...'. The raw "
                  "layer garbles '0.97 × 10⁵' as '0.97 x lo5' and '0.985 × "
                  "10⁵' as '0.985 x lo5'; the render readings are used. The "
                  "two halves are joined as one continuous paragraph."))

    # C31 (printed p.451 / PDF p.472, raw 19439-19443).
    b.append(p("This test may need to be carried out after reclosure of the "
               "apparatus, sometimes after each opening, and provision needs "
               "to be made in the construction to allow this to be done. "
               "Usually this is by having an entry device for a simple "
               "evacuating device which can be sealed with a valve or a screw "
               "and gasket after testing."))

    # C32 - unnumbered subheading 'Other approaches to restricted breathing
    # enclosure' (printed p.451). Note the singular 'enclosure'.
    b.append(h4("Other approaches to restricted breathing enclosure",
                "Other approaches to restricted breathing enclosure"))

    # C33 (printed p.451 / PDF p.472, raw 19445-19451).
    b.append(p("The other country which has historically used restricted "
               "breathing as a protection concept is Switzerland where the "
               "concept was used in a quite different way. Here the concept "
               "has been used for equipment which may spark in normal "
               "operation, such as switchgear, and it has been limited to "
               "apparatus where the internally dissipated power is not "
               "sufficient to raise the internal temperature by more than "
               "10°C. Thus it has not been possible to use it for luminaires. "
               "While the basic constructional requirements have not differed "
               "greatly the testing has. One of three tests have been applied "
               "as follows."))

    # C34-C36 - the numbered test list (printed p.451 / PDF p.472).
    b.append(ol([
        "A diffusion half-time test is applied whereby carbon dioxide is "
        "introduced into the enclosure without raising its pressure until "
        "the level of internal carbon dioxide concentration is 25 per cent. "
        "The internal concentration of carbon dioxide is then monitored for "
        "sufficient time to allow a straight line curve showing reduction "
        "of concentration with time to be plotted. This curve is then "
        "extrapolated to estimate the time necessary for the internal "
        "concentration of carbon dioxide to fall to 12.5 per cent which must "
        "not be less than 80 hours. Where the pressure measuring device adds "
        "significant volume to the enclosure volume (more than say 10 per "
        "cent) then the time given above needs to be multiplied by the total "
        "volume divided by the enclosure volume.",
        "Alternatively, where the enclosure has a volume of less than 10 "
        "litres, it should be raised or lowered (alternatives) to a pressure "
        "of 500 N/m² above or below atmospheric pressure and the reduction "
        "in pressure differential measured. The time taken for the difference "
        "to fall from 400 N/m² to 200 N/m² must be at least 80 seconds in "
        "this case. The same multiplication of time as for the carbon "
        "dioxide test is applied where the measuring device has a significant "
        "volume.",
        "A third alternative is to pressurize the enclosure to 400 N/m² above "
        "atmospheric pressure and calculate the volume of air required each "
        "hour to maintain that overpressure. That volume, divided by the "
        "enclosure volume, should not exceed a value of 0.125.",
    ]))
    b.append(note("<b>Note on the values in the Swiss-type testing items.</b> "
                  "The raw layer garbles 'less than 10 litres' as 'less than "
                  "lolitres' and drops spaces in '500 N/m²', '400 N/m²' and "
                  "'200 N/m²'; the render shows the spaced values given "
                  "above. The render readings are used."))

    # C37 - unnumbered subheading 'Use of the concept' (printed p.451).
    b.append(h4("Use of the concept", "Use of the concept"))

    # C38 + C39 (printed p.451-452 / PDF p.472-473, raw 19474-19487; one
    # continuous paragraph split by the page break).
    b.append(p("As with the UK approach the Swiss approach, as defined in IEC "
               "79–15¹¹, has been limited to apparatus that is not subject to "
               "duty cycling, which can cause significant temperature "
               "changes. In addition, the technique in its Swiss/IEC guise is "
               "limited to gases and vapours which have restricted breathing "
               "factors (s) of less than 20. This factor is related to the "
               "boiling point (bp), the molecular weight (m) and the lower "
               "explosive limit (LEL) of the gas or vapour in question and is "
               "derived from Fig. 14.5. The boiling point is identified on "
               "the left-hand side of Fig. 14.5 and the molecular weight on "
               "the right. These are then joined by a straight line which "
               "creates a point Z on the centre line. The LEL of the gas or "
               "vapour is then identified on the right-hand side of Fig. "
               "14.5 and a line drawn to the left-hand side via the point Z "
               "on the centre line. The restricted breathing factor can then "
               "be read off on the left-hand side."))
    b.append(note("<b>Note on the page boundary between printed pp.451 and "
                  "452.</b> The 'Use of the concept' paragraph ends printed "
                  "p.451 with '...which can cause' and continues on printed "
                  "p.452 with 'significant temperature changes.' The raw "
                  "layer garbles 'IEC 79–15¹¹' as 'IEC 79-1511'; the render "
                  "shows the en dash and the superscript 11. The two halves "
                  "are joined as one continuous paragraph."))

    # C40 (printed p.452 / PDF p.473, raw 19488-19495).
    b.append(p("While this approach to restricted breathing is not currently "
               "used in the UK, the imminent production of a European Standard "
               "for type of protection ‘N’ may include it as the approach is "
               "in IEC 79–15¹¹ which will form the basis for the European "
               "Standard. The presence of such a European Standard may create "
               "a situation where it may become incumbent on the UK to "
               "utilize this type of apparatus and for this reason it is "
               "included. The safety of such equipment may be called into "
               "question but its long use in Switzerland produces no evidence "
               "to support any such doubts."))

    # C41 - Fig. 14.5 (printed p.452 / PDF p.473), after the discussion.
    b.append(fig(5, F.fig_f1405()))
    b.append(note("<b>Note on the caption of Fig. 14.5.</b> The print reads "
                  "'between the material boiling point end its molecular "
                  "weight', using 'end' for 'and', and 'less then 40 °C', "
                  "using 'then' for 'than' (with '40°C' without a space on "
                  "its second occurrence). These quirks are kept in the "
                  "English figure caption; the Vietnamese follows the "
                  "intended meaning."))

    return "".join(b)
